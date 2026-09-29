// SKA SYMBOL256 (Kaleb, 2026-09-24). Shared by tools/build_symbols.js and worker.js - keep identical.
// 4 layers x 64 digits, each layer = lanes S I I S (Chain256 pattern). Stable lanes = 16 +/- pairs of the
// knowledge unit (stored). Interlocked lanes = live reading of the SAME 16 pairs at trigger time (question,
// tone, relevance) - recomputed every beat, never stored. Every dimension has a positive and a negative twin.
var SYM256 = {
  GENESIS_MS: Date.UTC(2018, 6, 1),
  LAYERS: ["cognitive_frame", "reasoning", "education_relevance", "emotion_behavior"],
  NEG: /\b(not|never|no|avoid|don't|do not|doesn't|does not|isn't|aren't|won't|cannot|can't|shouldn't|should not|without|nobody|nowhere|neither|nor)\b/,
  // [name+, name-, mode, positive cues, negative cues, guardrail]
  P: [
    ["who","who_not","role","customer customers buyer buyers seller sellers client clients prospect prospects manager managers leader leaders team founder ceo employee employees people user users stakeholder stakeholders partner partners who",""],
    ["what","what_not","role","is are means refers defined definition consists known what",""],
    ["when","when_not","role","when before after during until timing stage phase first then next early late while once daily weekly monthly quarter",""],
    ["where","where_not","role","where market markets channel channels online region location platform industry environment workplace field setting",""],
    ["how","how_not","role","how using through step steps process method methods technique techniques approach framework procedure",""],
    ["why","why_not","role","why purpose goal goals aim objective reason reasons",""],
    ["which","which_not","role","which choose choice select selection option options best",""],
    ["whether","whether_not","role","whether true false yes",""],
    ["how_much","how_little","polar","many much large larger largest significant major high higher","few little small smaller minimal minor low lower"],
    ["how_often","how_rarely","polar","always often frequently regularly routinely constantly usually","rarely seldom occasionally sometimes infrequently"],
    ["condition","unconditional","polar","if provided assuming depends depending whenever","regardless unconditionally universally"],
    ["exception","no_exception","polar","unless except however although exception exceptions","every universally invariably"],
    ["certain","uncertain","polar","must definitely proven clearly certainly always","may might perhaps possibly unclear uncertain likely"],
    ["necessary","optional","polar","required essential necessary critical mandatory","optional voluntary discretionary"],
    ["allow","forbid","polar","allowed permitted permit enable enables","forbidden prohibited banned disallowed"],
    ["include","exclude","polar","include includes including add combine integrate","exclude excluding remove omit omitted"],
    ["cause","correlation","polar","because causes caused cause leads due drives","correlated correlation associated linked coincide"],
    ["evidence","no_evidence","polar","data study studies research evidence shows measured survey experiment","anecdote anecdotal assume assumption belief unproven"],
    ["supported","unsupported","polar","therefore proves demonstrates confirms confirmed validated","claims alleged speculative myth rumor"],
    ["example","counterexample","polar","example instance illustrates illustration","counterexample contrast fails failure"],
    ["benefit","cost","polar","benefit benefits advantage advantages gain gains improve improves value","cost costs disadvantage disadvantages loss losses expense drawback drawbacks"],
    ["solution","problem","polar","solution solutions solve solves fix resolve remedy","problem problems issue issues challenge challenges obstacle bottleneck"],
    ["fact","opinion","polar","fact facts data statistics recorded","believe think feel opinion arguably seems"],
    ["known","unknown","polar","known established standard proven widely","unknown debated unresolved open unclear"],
    ["long_term","short_term","polar","long sustainable years lasting lifetime durable","immediate quick temporary short instant"],
    ["general","specific","polar","generally overall broad broadly general typically","specifically particular exactly precise precisely"],
    ["rule","violation","polar","rule rules principle principles law standard standards practice","violation violations breach mistake mistakes error errors noncompliance"],
    ["theory","application","polar","theory theories concept concepts model models principle","apply applied practice implement implementation real case"],
    ["sequence","unordered","polar","first second third then next finally step steps","simultaneously randomly parallel"],
    ["increase","decrease","polar","increase increases grow growth rise boost raise expand","decrease decreases reduce reduces decline drop cut shrink"],
    ["similar","different","polar","similar like same equivalent comparable","different unlike versus whereas contrast differs"],
    ["simple","complex","polar","simple basic easy straightforward","complex complicated sophisticated intricate"],
    ["foundational","advanced","polar","basic fundamental fundamentals introduction foundations foundational","advanced expert mastery cutting sophisticated"],
    ["understand","misconception","polar","understand understanding explains explanation clarifies","misconception misconceptions myth misunderstanding confusion"],
    ["apply","theory_only","polar","apply exercise practice hands implement","abstract theoretical conceptual"],
    ["analyze","surface","polar","analyze analysis examine evaluate breakdown investigate","overview summary briefly outline"],
    ["evaluate","unjudged","polar","assess assessment evaluate measure metrics criteria benchmark","untested unmeasured unassessed"],
    ["create","replicate","polar","create design build develop invent innovate","copy replicate template imitate"],
    ["core","peripheral","polar","key core central essential critical crucial","minor peripheral secondary tangential"],
    ["prerequisite","follow_on","polar","prerequisite prerequisites requires foundation beforehand","builds extends subsequent afterwards"],
    ["current","outdated","polar","modern current recent today emerging","traditional outdated historical legacy obsolete"],
    ["verified","unverified","polar","verified validated tested confirmed audited","unverified untested unconfirmed anecdotal"],
    ["complete","partial","polar","complete comprehensive full entire thorough","partial incomplete limited some"],
    ["practical","academic","polar","practical real business workplace applied","academic scholarly literature theoretical"],
    ["novice","expert","polar","beginner beginners novice learners newcomers","practitioners professionals experts specialists"],
    ["clear","ambiguous","polar","clearly clear defined precisely explicit","ambiguous vague unclear depends"],
    ["safe","hazardous","polar","safe safety secure protect protected","dangerous hazard hazardous harm injury weapon toxic","guard"],
    ["lawful","legal_risk","polar","legal lawful compliant compliance regulated","illegal fraud fraudulent lawsuit liability unlawful","guard"],
    ["joy","sadness","polar","happy joy delighted pleased excited satisfied","sad unhappy disappointed regret grief"],
    ["trust","disgust","polar","trust trusted reliable credibility confidence","distrust disgust suspicious skeptical"],
    ["anticipation","surprise","polar","expect anticipate plan planned prepared","surprise surprised unexpected sudden shock"],
    ["calm","fear_anger","polar","calm relaxed steady composed patient","fear afraid anxious angry anger frustrated stress"],
    ["confidence","doubt","polar","confident confidence assured certain","doubt doubtful hesitant unsure insecure"],
    ["empathy","indifference","polar","empathy empathize understand listen care concerns","indifferent ignore ignoring dismiss dismissive"],
    ["respect","contempt","polar","respect respectful courteous appreciate","contempt disrespect insult belittle"],
    ["approach","avoid","polar","engage approach pursue reach contact","avoid avoiding withdraw retreat evade"],
    ["cooperate","compete","polar","cooperate collaborate collaboration partnership together","compete competition competitor rival win"],
    ["assertive","passive","polar","assertive direct firm confident propose","passive submissive timid concede"],
    ["ask","tell","polar","ask asking question questions inquire probe","tell telling instruct explain present"],
    ["listen","speak","polar","listen listening hear acknowledge","talk speak pitch present"],
    ["commit","hesitate","polar","commit commitment decide agree close","hesitate hesitation delay stall postpone"],
    ["honest","deceptive","polar","honest honesty transparent truthful disclose","deceive deceptive mislead misleading lie exaggerate","guard"],
    ["autonomy","pressure","polar","choice consent voluntary respect decide","pressure manipulate manipulation force coerce trick","guard"],
    ["ethical","unethical","polar","ethical ethics fair integrity responsible","unethical exploit exploitative unfair bribe","guard"]
  ],
  _rx: null,
  rx() {
    if (SYM256._rx) return SYM256._rx;
    var mk = function (s) { return s ? new RegExp("\\b(" + s.trim().split(/\s+/).join("|") + ")\\b", "g") : null; };
    SYM256._rx = SYM256.P.map(function (p) { return [mk(p[3]), mk(p[4])]; });
    return SYM256._rx;
  },
  // 128 stable digits: pair i -> digits 2i (positive), 2i+1 (negative)
  stable(text) {
    var t = " " + String(text || "").toLowerCase() + " ", R = SYM256.rx(), neg = SYM256.NEG.test(t), out = "";
    for (var i = 0; i < 64; i++) {
      var pm = R[i][0] ? t.match(R[i][0]) : null, pn = pm ? pm.length : 0, nn = 0;
      if (SYM256.P[i][2] === "role") { if (neg && pn) { nn = pn; pn = Math.max(0, pn - 1); } }
      else { var nm = R[i][1] ? t.match(R[i][1]) : null; nn = nm ? nm.length : 0;
        if (SYM256.P[i][5] === "guard" && neg && nn) { pn += nn; nn = 0; } }   // "never pressure" = advice against -> positive twin
      out += String(Math.min(9, pn)) + String(Math.min(9, nn));
    }
    return out;
  },
  // live reading of a question on the same 128 digits: interrogatives weigh heavily, negation routes to the twin
  read(q) {
    var t = String(q || "").toLowerCase(), d = SYM256.stable(t).split("").map(Number), neg = SYM256.NEG.test(" " + t + " ");
    var W = { who: 0, what: 1, when: 2, where: 3, how: 4, why: 5, which: 6, whether: 7 };
    Object.keys(W).forEach(function (w) { if (new RegExp("\\b" + w + "\\b").test(t)) d[W[w] * 2 + (neg ? 1 : 0)] = 9; });
    if (/\b(mistake|mistakes|avoid|pitfall|wrong)\b/.test(t)) { d[3] = 9; d[53] = 9; }
    return d.join("");
  },
  // Chain256 layout: layer L = S(16) I(16) I(16) S(16); S from stable, I from live
  lanes(stable128, live128) {
    var s = "";
    for (var L = 0; L < 4; L++) s += stable128.substr(L * 32, 16) + live128.substr(L * 32, 16) + live128.substr(L * 32 + 16, 16) + stable128.substr(L * 32 + 16, 16);
    return s;
  },
  score(live128, stable128) { var s = 0; for (var i = 0; i < 128; i++) s += (+live128[i]) * Math.min(3, +stable128[i]); return s; },
  guard(stable128) {
    var hit = [];
    for (var i = 0; i < 64; i++) if (SYM256.P[i][5] === "guard" && +stable128[i * 2 + 1] >= 1) hit.push(SYM256.P[i][1]);
    return hit;
  },
  beat(now) { return Math.floor(((now || Date.now()) - SYM256.GENESIS_MS) / 1000); }
};
if (typeof module !== "undefined") module.exports = SYM256;
