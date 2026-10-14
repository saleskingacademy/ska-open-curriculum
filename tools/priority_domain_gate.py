#!/usr/bin/env python3
import json, pathlib, re, sys
from collections import Counter

ROOT=pathlib.Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'curriculum/PRIORITY_DOMAIN_MANIFEST.json'
FRONT=('key','title','program','dna16','l4_address','chain256_anchor','license')
MARKERS=('foundation','application','advanced','worked example','case study','review question','answer key')
BAD=('[object Object]','TODO: write','PLACEHOLDER','lorem ipsum')

def frontmatter(text):
    if not text.startswith('---\n'): return {},text
    end=text.find('\n---\n',4)
    if end<0: return {},text
    meta={}
    for line in text[4:end].splitlines():
        if ':' in line:
            k,v=line.split(':',1);meta[k.strip()]=v.strip().strip(chr(34)).strip(chr(39))
    return meta,text[end+5:]

def dup_ratio(body):
    clean=re.sub(r'```.*?```',' ',body,flags=re.S)
    clean=re.sub(r'\s+',' ',clean)
    ss=[s.strip().lower() for s in re.split(r'(?<=[.!?])\s+',clean) if len(s.split())>=12]
    if not ss:return 0.0
    counts=Counter(ss);return sum(n-1 for n in counts.values() if n>1)/len(ss)

def inspect(rel,status):
    p=ROOT/rel;errors=[];warnings=[]
    if not p.exists():return {'path':rel,'errors':['missing_file'],'warnings':[]}
    text=p.read_text(encoding='utf-8');meta,body=frontmatter(text)
    for k in FRONT:
        if not meta.get(k):errors.append('missing_frontmatter:'+k)
    if meta.get('key') and meta['key']!=p.stem:errors.append('key_path_mismatch')
    if any(x.lower() in body.lower() for x in BAD):errors.append('placeholder_or_serialization_artifact')
    if rel.startswith('knowledge/sales_king_academy/') and 'all-rights-reserved' not in meta.get('license','').lower():errors.append('proprietary_license_missing')
    words=len(re.findall(r"\b[\w'-]+\b",body));sections=len(re.findall(r'(?m)^#{2,4}\s+.+$',body));dup=dup_ratio(body)
    key=meta.get('key') or p.stem;program=meta.get('program') or p.parent.name
    sym=(ROOT/'symbols'/program/(key+'.json')).exists();study=(ROOT/'study'/(key+'.json')).exists()
    coverage={m:(m in body.lower()) for m in MARKERS}
    if dup>0.08:warnings.append('high_sentence_repetition')
    if sections<4:warnings.append('thin_section_structure')
    if not sym:warnings.append('symbol_artifact_missing')
    if not study:warnings.append('study_artifact_missing')
    if status=='complete':
        if words<1500:errors.append('complete_claim_too_thin_for_scope')
        if sections<8:errors.append('complete_claim_missing_section_depth')
        miss=[m for m,v in coverage.items() if not v]
        if miss:errors.append('complete_claim_missing_coverage:'+','.join(miss))
        if dup>0.05:errors.append('complete_claim_repetition_exceeds_gate')
        if not sym or not study:errors.append('complete_claim_missing_derived_artifacts')
    return {'path':rel,'words':words,'sections':sections,'duplicate_sentence_ratio':round(dup,4),'coverage':coverage,'errors':errors,'warnings':warnings}

def main():
    data=json.loads(MANIFEST.read_text(encoding='utf-8'));hard=[]
    print('PRIORITY DOMAIN QUALITY GATE')
    for group,spec in data['groups'].items():
        status=spec.get('status','in_progress');print('\n['+group+'] '+status)
        for rel in spec.get('files',[]):
            r=inspect(rel,status);print('- %s: %s words, %s sections, dup %.1f%%'%(rel,r.get('words',0),r.get('sections',0),100*r.get('duplicate_sentence_ratio',0)))
            for e in r['errors']:
                print('  ERROR '+e)
                if status=='complete' or e.startswith(('missing_file','missing_frontmatter','key_path_mismatch','placeholder_or_serialization_artifact','proprietary_license_missing')):hard.append((rel,e))
            for w in r['warnings']:print('  WARN  '+w)
    print('\nHard failures:',len(hard))
    return 1 if hard else 0

if __name__=='__main__':raise SystemExit(main())
