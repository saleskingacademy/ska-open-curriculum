#!/usr/bin/env python3
"""Refresh named legacy topics without reallocating unchanged paragraph addresses.

First rebuild symbols with the canonical sat_pairs.js builder. This command
consumes those symbols, preserves existing records for unchanged paragraphs,
appends registry allocations for changed paragraphs, and updates ancestors.
It never modifies core chain algorithms or deletes retired registry entries.
Run edu16.py --verify afterward; this is not an academic validation tool.
"""
from pathlib import Path
import copy
import json
import sys
import edu16 as E

ROOT = Path(__file__).resolve().parents[1]

def refresh(topics):
    chapters_path = ROOT/'map/edu16_chapters.json'
    index = json.loads(chapters_path.read_text())
    registry = E.load_reg()
    original_registry = copy.deepcopy(registry)
    documents = {}
    symbols = {}
    for path in (ROOT/'symbols').glob('*/*.json'):
        if path.stem in topics:
            if path.stem in symbols:
                raise ValueError(f'Ambiguous symbol topic: {path.stem}')
            symbols[path.stem] = json.loads(path.read_text())
    preserved = replaced = 0
    for topic in sorted(topics):
        home = index['chapters'][topic]['subject']
        path = ROOT/'edu16'/f'{home}.json'
        if home not in documents:
            documents[home] = json.loads(path.read_text())
        document = documents[home]
        chapter = next(c for c in document['chapters'] if c['key']==topic and not c.get('cross_listed'))
        symbol = symbols[topic]
        if symbol['path'] != chapter['path']:
            raise ValueError(f'Topic path migration requires separate review: {topic}')
        source = (ROOT/chapter['path']).resolve()
        source.relative_to(ROOT/'knowledge')
        se = document['edu16']
        ce = chapter['edu16']
        ff, sss, ccc = int(ce[:2]), int(ce[2:5]), int(ce[5:8])
        oldsections = {s['id']:s for s in chapter['sections']}
        sections = []
        for section in symbol['sections']:
            skey = topic+'/'+section['id']
            old = oldsections.get(section['id'])
            if old:
                xe = old['edu16']
                xxx = int(xe[9:12])
            else:
                xxx = E.alloc('sections',skey,topic,registry)
                xe = E.edu16(ff,sss,ccc,0,xxx,0,3)
            prior = {(p['pid'],p['int16']):p for p in (old or {}).get('paragraphs',[])}
            paragraphs = []
            psigs = []
            for p in section['paragraphs']:
                integrity = E.d16(p['id']+'|'+p['sig']+'|'+str(p.get('words')))
                matching = prior.get((p['id'],integrity))
                if matching:
                    paragraphs.append(matching)
                    preserved += 1
                else:
                    ppp = E.alloc('paragraphs',skey+'/'+p['id']+'@'+integrity,skey,registry)
                    pe = E.edu16(ff,sss,ccc,0,xxx,ppp,4)
                    sym16 = E.d16(p['sig'])
                    paragraphs.append({'edu16':pe,'t16':E.t16(pe),'spent':E.spent(pe),
                        'pid':p['id'],'words':p.get('words'),'sym16':sym16,'int16':integrity,
                        's128':''.join(E.lanes(se,pe,sym16,integrity))})
                    replaced += 1
                psigs.append(p['sig'])
            sig = E.agg_sig(psigs)
            sym16 = E.d16(sig)
            integrity = E.d16('|'.join(p['int16'] for p in paragraphs))
            sections.append({'edu16':xe,'t16':E.t16(xe),'spent':E.spent(xe),
                'id':section['id'],'title':section['title'],'sig':sig,'sym16':sym16,
                'int16':integrity,'s128':''.join(E.lanes(se,xe,sym16,integrity)),
                'paragraphs':paragraphs})
        chapter['sections'] = sections
        chapter['sig'] = E.agg_sig([s['sig'] for s in sections])
        chapter['sym16'] = E.d16(chapter['sig'])
        chapter['int16'] = E.d16(source.read_text())
        chapter['s128'] = ''.join(E.lanes(se,ce,chapter['sym16'],chapter['int16']))
        index['chapters'][topic].update(int16=chapter['int16'],s128=chapter['s128'])
    # Existing registry assignments are immutable, including retired allocations.
    for table in ('subjects','chapters','sections','paragraphs'):
        assert all(registry[table].get(k)==v for k,v in original_registry[table].items())
    for home, document in documents.items():
        children = [c for c in document['chapters'] if not c.get('cross_listed')]
        document['sig'] = E.agg_sig([c['sig'] for c in children])
        document['sym16'] = E.d16(document['sig'])
        document['int16'] = E.d16('|'.join(c['int16'] for c in children))
        document['s128'] = ''.join(E.lanes(document['edu16'],document['edu16'],document['sym16'],document['int16']))
        (ROOT/'edu16'/f'{home}.json').write_text(json.dumps(document,ensure_ascii=False,separators=(',',':')))
    chapters_path.write_text(json.dumps(index,separators=(',',':'),sort_keys=True))
    Path(E.REG).write_text(json.dumps(registry,separators=(',',':'),sort_keys=True))
    print(json.dumps({'topics':sorted(topics),'subjects_refreshed':len(documents),
        'unchanged_paragraph_addresses_preserved':preserved,'changed_paragraph_records':replaced,
        'new_registry_paragraph_entries':len(registry['paragraphs'])-len(original_registry['paragraphs'])}))

if __name__=='__main__':
    if len(sys.argv)<2:
        raise SystemExit('Supply explicit topic keys; no implicit full-corpus refresh.')
    refresh(set(sys.argv[1:]))
