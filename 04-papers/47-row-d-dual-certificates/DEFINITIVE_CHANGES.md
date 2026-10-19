# Paper 47 — definitive version: changes, structure, sources

Backup of the previous main: main_pre_definitive.tex / .pdf (104 pp, logbook-like).
New main.tex: base = main_short.tex (66 pp clean rewrite, CHANGES_SHORT.md), with all proved material the
short version dropped restored, plus the phase-186 structural theory and barriers. pdflatex x2:
**128 pp, 0 errors, 0 undefined references, 0 multiply-defined labels** (11 minor overfull boxes).

## Structure and source of every section
| § | Title | Source |
|---|---|---|
| 1 | Introduction | main_short §1; new: abstract sentence, "Operator structure", "Witnesses", barrier paragraph, rewritten "What remains open", new "Organization" |
| 2 | Preliminaries: the archimedean multiplier | main_short §2 |
| 3 | Primal and dual programs | main_short §3 + thm:W (Euler–Lagrange, old main) |
| 4 | Tail lemmas and an explicit certificate | main_short §4 + concentration subsection (thm:P3, cor:AP, rem:P3exp), prop:M |
| 5 | The dual variable is the explicit formula | main_short §5 + cor:zeros, rem:Zcheck, prop:loc (old rem:loc), prop:finuniv, cor:bprof (new proof), rem:comblp |
| 6 | Lattice certificates and their ceilings | main_short §6 |
| 7 | The archimedean form | main_short §7 + subsec "The negative index" (prop:NC, cor:P3, rem:P4, thm:J, cor:nasym, cor:H1, rem:odd080) + subsec "The negative set of the symbol" (prop:band, prop:align, prop:negtrace) |
| 8 | Obstructions to general methods | main_short §8 + rem:PF2, cor:CP (moved after thm:Vp), prop:decide (rewritten proof), rem:regimes, cor:Qp, rem:resweights, lem:degen, rem:twohalves |
| 9 | Inertia and remainders | old main §16 / DRAFT_SECTION_INERTIA_BARRIERS (thm:inertia-split/-B2/-finite/-quartet/-rank; exclusion now conditional on a stated index count) |
| 10 | The semilocal Sonin decomposition at the first prime | old main §17; new lem:sl-lac; log-structure CONDITIONAL on (H_G), stated in thm:sl-L2 |
| 11 | The complete form at a single window | main_short §9 + def:Al, lem:Alband, rem:excess, rem:Cheb + subsec "One direction at T = log 2" (prop:schur, thm:w11, thm:nest, prop:bprime, prop:shifts, lem:N, prop:G, rem:galerkin) |
| 12 | Certified positivity up to ½log5 | main_short §10 |
| 13 | A finite reduction | main_short §11 + short-window coercivity (lem:coer-K/-K1/-sector/-tail/-w/-poinc, thm:coer-A) and remarks (C1 correction: bilinear norm π, quadratic π/2) |
| 14 | The window form as a truncated Wiener–Hopf operator | DRAFT_SECTION_WIENER_HOPF_STRUCTURE (C-W1/2/3/4/10/11 resolved) + determinants subsection (Birman–Schwinger, inheritance theorem) |
| 15 | Sampling at the Nyquist mesh and two-sector structure | NEW (phase 186: Nyquist identity with truncated Lévy symbol + aliasing identity, window measure, two sectors/half-shift, primal cone, two-sector Schur reduction) |
| 16 | First contact | main_short §12 + rem:completecontact, rem:Sren, rem:returnremarks |
| 17 | Witnesses | NEW (absorption, freezing, node lemma, model forms with proved witnesses, (E_γ), coherence on the mesh, Chebyshev form, sensitivity) |
| 18 | Barriers for classes of arguments | NEW (W-lin: one-half lemma, direct bound, accounting at τ=0, positive exterior measures; W-fam: transport, thm:famblind unconditional, thm:famFE CONDITIONAL on (H_f); W-pat: quartet models, cor:pattern; W-loc: compressions, thm:nolocal, Theorem X corrected, flow lemma). W-det and W-mom are in §14, W-coh in §17 |
| 19 | Open problems | rewritten: (L2) S_{T,k(T)} ⪰ 0 for T>½log5; (N) signed pointwise twisted-Chebyshev bound at Nyquist points; secondary items |
| A | Computer verifications | main_short App. A + lem:bern |
| B | Numerical values | main_short App. B (9.448e-4, 9.83e-8, 3.10e-12 numerical; certified bounds unchanged) |
| C | Numerical observations | old app:diag, purged of superseded values |

Imports from Paper 45: only Thm 8.4 (Thm 11.3 was used only in RH-equivalence passages, all removed).
Excluded (RH-equivalent/conditional on RH): as in CHANGES_SHORT.md; plus no f_t-type statement without explicit hypothesis.

## Adversarial self-review (integrator)
- Duplicates removed: rem:Zcheck/rem:comblp (body vs appendix); quartet lemma kept once in proof form (lem:wh-Q; lem:quartet records the integral form and points to it); rank-two Kreĭn criterion kept once (prop:wh-K); "quartet models negative" kept once (thm:wit-model(iii)); duplicate ½log5 midpoint item removed from App. C.
- Forward use inside proofs: cor:CP used thm:Vp from a later section → moved after thm:Vp. Remaining forward refs inside proofs are to the appendix verifications (by design) and to a remark (rem:Kprim, next paragraph).
- Broken sentence after cor:Tarch completed; old-notation residue W_k → Y_k in prop:TAY.
- grep: no memo IDs, phases, rounds, editor or author, no "RH"/Riemann-hypothesis statement (only bibliographic titles), no old λ_A values (1.042e-7, 9.486e-4, 3.84e-12).
- Corrections made by the restoring/drafting passes (see per-pass tables below): Birman–Schwinger "no gap" paragraph omitted (false); Landau–Widom count weakened to (2τ₀/π)T(1+o(1)); prop:M τ=0 claim fixed; prop:decide proof rebuilt; direct bound corrected beyond ½log3; R186_051 δ* values not used (inconsistent); window-Bochner statement only as remark; sandwich of the pencil fixed (C-W1); λ_A ≤ min(c,λ_S) corrected.
- Open/not done: ~~Kahane–Mandelbrojt venue to confirm~~ **verified  (RECORDS-CLEANUP): Ann. Sci. École Norm. Sup. (3) 75 (1958), no. 1, 57–80, DOI 10.24033/asens.1066, numdam ASENS_1958_3_75_1_57_0; bibitem correct, DOI added**; ~~11 overfull boxes (cosmetic)~~ fixed  (see RECORDS-CLEANUP); certification of c_X values and of the Nyquist-model certificates remains numerical.

## Per-fragment status tables (from the drafting passes)

---
# INSERT_A (run A) — fragments in $S/A/, merge script $S/A/insert.py, test build $S/test_A.tex (74 pp, 0 errors, 0 undefined refs)
Each fragment is inserted IMMEDIATELY BEFORE the anchor (exact string in main_short.tex).
| file | anchor (insert before) | new labels | status | source (main.tex) |
|---|---|---|---|---|
| A01_thmW | `\subsection{The polar multiplier}` (i.e. after rem:OvsB) | thm:W (new subsection "The Euler--Lagrange equation") | PROVED | 607-624; operator renamed \mathsf S_T, sign-change range made precise, density step added |
| A02_conc | `\subsection{Lattice atoms: the graded periodic tail}` (sec:tails) | subsec:conc, thm:P3, cor:AP, rem:P3exp | PROVED (remark: proved via thm:Vp(ii)) | 712-783; W->\mathsf V, TV value 48.7 -> 90.75 (thm:C), app:diag ref dropped |
| A03_propM | `\subsection{An explicit certificate at` (after thm:E) | prop:M | PROVED (proof of Fourier-support claim added; false "<0 at tau=0" claim replaced by Thm O) | 890-908 |
| A04_corzeros + A13a_Zcheck | `\begin{theorem}[exhaustion by flat-top weights]` (after thm:Z) | cor:zeros, rem:Zcheck | PROVED / NUMERICAL | 1231-1240 ("Under RH" sentence removed); 6263 |
| A05_remloc | `\begin{corollary}[finite sets of zeros do not suffice]` (after thm:finZ) | prop:loc (old rem:loc, promoted, hypotheses made precise, phase computed) | PROVED | 1394-1410 |
| A06_finuniv | `The mechanism is the following. A finite $Z$` (after cor:infinite) | prop:finuniv | PROVED (old (iii) was vacuous for Z⊂R; restated as Bochner) | 1432-1455 |
| A07_bprof + A13b_comblp | `\subsection{The Kre\u{\i}n extension problem at one window}` (after cor:comb) | cor:bprof, rem:comblp | PROVED (proof supplied; old had none) / NUMERICAL | 1618-1626; 6274 |
| A08_corCP | `\subsection{Sampling a flat-top certificate}` (after cor:R3) | cor:CP | PROVED ((iii) new short proof of non-uniformity) | 2168-2190 |
| A09_negindex | `\subsection{Competing even modes}` | subsec:negindex, prop:NC, cor:P3, rem:P4, thm:J, cor:nasym (new), cor:H1, rem:odd080 + 2 unlabelled remarks | PROVED; rem:P4/rem:odd080 NUMERICAL parts flagged | 2568-2830, 6379; Gamma_T -> \mT |
| A10_PF2 | `\section{Obstructions to general methods}` (after cor:arena paragraph) | rem:PF2 | PROVED/CITED | 2903-2919 |
| A11_decide | `\subsection{Bounded remainders}` (end of subsec:finite) | prop:decide (new subsection) | PROVED (proof rewritten: exponential columns + Lemma T instead of lattice atoms; primitive step functions via explicit moment correction) | 2939-2962 |
| A12_bern | `\subsection{The certificates of Theorem~\ref{thm:index}}` (after prop:TAY) | lem:bern | PROVED | 5796-5830 |
| A_bib | Karlin1968, LandauWidom1980 before `\bibitem{Krein1940}`; Schoenberg1951 before `\bibitem{SSV2012}` | — | CITED | |
External labels referenced (all exist in main_short): lem:mbounds, lem:gbounds, prop:weak, thm:O, thm:Vp, prop:env, thm:C, thm:S, lem:K, eq:m, prop:T0, lem:T, cor:T2, thm:E, thm:Z, eq:fw, eq:Z, thm:finZ, lem:smooth, thm:Dtail, cor:comb, thm:R, lem:KyFan, cor:P1, thm:index, lem:strict, prop:haynsworth, cor:mono, thm:arena, prop:nodes, thm:A, prop:TAY, app:encl, subsec:conc. No new macros. No cross-pass labels.

---
# INSERT_B — restored PROVED material from old main.tex (l. 3163–6486) into main_short.tex

All fragments: S/B/*.tex (no preamble). Each file starts with a `% ---- ` comment giving the exact insertion
point; files with several points are split by further `% ---- ` lines. Automated insertion: `python3 S/B/insert.py`
-> S/test_B.tex (compiles: 0 errors, 0 undefined refs/cites, 88 pp vs 66; one new 2.5pt overfull). No new macros.

| file | insertion point in main_short | labels defined |
|---|---|---|
| B1a_regimes.tex | §subsec:finite, after proof of prop:finite | rem:regimes |
| B1b_Qp.tex | after proof of lem:cpos (+1 paragraph) | cor:Qp |
| B1c_degen.tex | after proof of thm:finmod | rem:resweights, lem:degen |
| B1d_twohalves.tex | after proof of cor:void | rem:twohalves |
| B2_band.tex | new \subsection "The negative set of the symbol" at end of §sec:archstr (before \section{Obstructions…}) | subsec:band, prop:band, rem:bandvalues, prop:align, rem:taulast, prop:negtrace (defines Pos_T, Neg_T, tau_last, tau^lo) |
| B4_inertia.tex | new \section "Inertia and remainders" after §sec:negative (before \section{The complete form…}) | sec:inertia, thm:inertia-split, thm:inertia-B2, thm:inertia-finite, thm:inertia-quartet, thm:inertia-rank, subsec:inertia-excl, rem:inertia-conv |
| B4b_semilocal.tex | new \section right after B4 | sec:semilocal, subsec:sl-dict, def:FS, lem:sl-phase, prop:sl-AS, lem:sl-linear, subsec:sl-trace, thm:sl-gap, lem:sl-TC, lem:sl-lac, thm:sl-L2, eq:sl-HG, thm:sl-84, rem:sl-level, subsec:sl-split, cor:sl-split, rem:sl-not, rem:sl-new |
| B3a_alignment.tex | §sec:complete, after proof of thm:Al (before "\emph{The per-window converse.}") | def:Al, lem:Alband, rem:excess, rem:Cheb, eq:Cheb |
| B3b_log2.tex | new \subsection "One direction at T=log2" at end of §sec:complete (before \section{Certified positivity…}) | subsec:schur, prop:schur, thm:w11, thm:nest, prop:bprime, prop:shifts, lem:N, prop:G, rem:galerkin |
| B5a_coer_blocks.tex | §subsec:coer-blocks, after proof of lem:coer-decomp | lem:coer-K1, eq:coer-cross, lem:coer-sector, eq:coer-diag |
| B5b_coer_short.tex | new \subsection before \subsection{Coercivity of the archimedean form on V_k} | subsec:coer-short, lem:coer-K, lem:coer-tail, lem:coer-w, lem:coer-poinc, thm:coer-A, eq:coer-A, rem:coer-A, rem:coer-prec |
| B5c_coer_remarks.tex (3 parts) | (1) after proof of thm:coer-B; (2) after proof of cor:coer-L1; (3) after rem:coer-honest | rem:coer-B, rem:coer-size, rem:coer-nogo |
| B6_firstcontact.tex (3 parts) | (1) after proof of lem:firstcontact; (2) after the paragraph ending "cannot determine the sign of the Weil form." (after thm:PCfinite); (3) end of §sec:firstcontact, before \section{Open problems} | rem:completecontact, rem:Sren, rem:returnremarks |
| B7_appdiag.tex | new appendix \section after app:num (before thebibliography) | app:diag, rem:nodal, rem:signrule, rem:bandtable, rem:polarcapdiag, rem:Zcheck, rem:comblp |
| bib_B.tex | add to thebibliography | CCquasi2020, CCM2023, CCM2024, CvS2025, DavenportHeilbronn1936, HLP, Kim2026, Simon2005 |

External labels referenced (all exist in main_short): prop:finite, lem:cpos, thm:finmod, cor:void, cor:margin1, thm:margin,
lem:compact, lem:contA, lem:contT, lem:monoT, lem:Onat, thm:Al, thm:Z, thm:Zexh, prop:env, lem:mbounds, lem:gbounds, lem:K,
thm:S, thm:A, eq:Aform, eq:m, eq:fw, eq:Z, def:W, def:PD, cor:mono, prop:arch, prop:nodes, lem:parity, thm:index,
cor:Tarch, prop:archneg, thm:SC, prop:finsupp, thm:inertia-nogo, lem:roughEF, lem:KyFan, prop:coer-prime,
thm:coer-B, thm:coer-schur, cor:coer-L1, lem:coer-lowpass, thm:parityschur, cor:convfail, thm:log5A, thm:log5W,
thm:C, prop:TK, thm:latedge, cor:comb, lem:smooth, prob:annihilate, eq:equivgate, eq:Qspectral, eq:annihilate,
eq:PCfinite, app:num. Cross-pass: prop:band / prop:negtrace / Pos_T / Neg_T / tau_last / thm:inertia-quartet are
defined HERE for the Wiener–Hopf run (labels kept identical to the old ones). None of my fragments needs another run's label.

## Status and source of each result
- rem:regimes, rem:resweights, rem:twohalves, rem:excess, rem:Cheb (eq:Cheb identity PROVED in the remark),
  rem:completecontact, rem:Sren, rem:returnremarks, rem:inertia-conv, rem:sl-level, rem:sl-not, rem:sl-new,
  rem:coer-prec: remarks (no new claims beyond proved ones; numerics flagged). main.tex 3196–3424, 3899–3934, 5344–5354, 5436–5452, 5652–5666, 4413–4420, 4630–4704.
- cor:Qp, lem:degen: PROVED (main.tex 3231–3337).
- prop:band, prop:align, prop:negtrace: PROVED (main.tex 3426–3530); constants in prop:align and rem:bandvalues/rem:taulast are
  double-precision evaluations of explicit elementary functions (stated). prop:negtrace(v) rewritten with S_c of lem:KyFan
  (old prop:NC dropped); proof of (i) made explicit.
- def:Al, lem:Alband: PROVED (main.tex 3534–3555). thm:Al(c) and the chain "WP ⟹ ... ⟹ WP" EXCLUDED.
- prop:schur, prop:bprime, prop:shifts, lem:N, prop:G: PROVED (main.tex 3946–4134). prop:shifts: non-compactness proof
  rewritten (weakly null sequence; old text was a sketch). prop:schur(iii) restated with the operator H of lem:compact.
- thm:w11, thm:nest: PROVED with computer verification in interval arithmetic (main.tex 3967–4069; certificate data
  "accompanying the paper" as in old text). rem:galerkin REWRITTEN: old text said Galerkin values at log 2 do not
  stabilize; replaced by the converged reference value 9.83e-8 (BRIEF).
- thm:inertia-split: CITED+PROVED (from Connes–Consani Thm 4.7, (83),(152)–(154)); thm:inertia-B2, thm:inertia-finite,
  thm:inertia-quartet, thm:inertia-rank: PROVED (main.tex 4245–4386; CHECK_TABLE part I rows 1–6). Changes: O(s^{-2}) → O(|s|^{-1})
  in thm:inertia-finite (lem:mbounds gives only O(1/s)); odd case of the quartet independence written out; rank lemma
  proof written; the unproved sentence "Son grows like w^{-3}log(1/w)" dropped.
- subsec:inertia-excl: "Sonin-norm bounds" = consequence of proved theorems; "Inertia alone" is CONDITIONAL, with the
  hypothesis n_-(W^{Z'}_T|P_T) ≥ 2m written as "Assume" (not proved). The old "witness decorrelator" paragraph and
  "What remains" (refers to dropped prob:B; unproved) are EXCLUDED.
- sec:semilocal (CHECK_TABLE part II; memos R186_007–014, R186_093–098): def:FS, lem:sl-phase CITED+verified;
  prop:sl-AS PROVED (compactness also CITED); lem:sl-linear PROVED (Simon CITED), not new; thm:sl-gap PROVED — proof
  rewritten (old statement/proof was a sketch; new proof via X=(1-P)F_S P, X*X=P-Z_S^2, and zeta_n defined for all n);
  lem:sl-TC PROVED (CC Lemma D.1, Simon CITED); lem:sl-lac NEW, PROVED (closes one of the two gaps flagged in
  CHECK_TABLE II.7); thm:sl-L2: density formula PROVED, the log-expansion/L^p/not-L^infty part CONDITIONAL on the
  explicitly stated hypothesis (H_G) sup_u ||G_0(u,.)||_{L^2(0,λ)} < ∞ (the second gap of II.7, only argued in R186_012);
  the old claim "pointwise series diverges at 2^j" DROPPED (sketchy, not needed); thm:sl-84(i) PROVED for every λ;
  (ii) PROVED at λ=1 given CC Thm 4.7 & (84) (CITED); cor:sl-split: identity PROVED at λ=1 (given CC), Hilbert–Schmidt
  and δ-finite index CONDITIONAL on (H_G). (Old text claimed these unconditionally; downgraded.)
  Notation changes to avoid clashes: F_S,F_∞ → \mathsf F_S,\mathsf F_∞; A_S → Z_S; E_S(f) → Hal_S(f); W (unitary) → \mathsf W;
  E → \mathsf E; ϑ (scaling) → \mathcal U; I → J; T (translation) → qV_{-log2}; ε → ε_∞; Γ_T → \mT.
- lem:coer-K1, lem:coer-sector, lem:coer-K, lem:coer-tail, lem:coer-w, lem:coer-poinc, thm:coer-A: PROVED
  (main.tex 4780–4920; CHECK_TABLE III.2–III.8, R186_025/105); w(2)=2.1045 is an evaluation of an elementary function.
  Notation: τ (block/short window) → r, Γ → \mT, w(s) → \mathsf w(s), δ → ε_lp, K → \mathsf K.
- rem:coer-A, rem:coer-B, rem:coer-size: numerics flagged "numerical", rounded to 1–2 digits.
- rem:coer-nogo: NO-GO for the declared splitting route; C1 applied (bilinear K_1-norm π, quadratic coupling π/2; k ≥ 70).
  Pair norm PROVED (Hilbert's inequality CITED HLP Thm 316). Carleman sentence (old (b)) dropped (uncited source);
  Carleman1923 bib entry therefore optional.
- app:diag: NUMERICAL only. Removed: every value superseded by BRIEF (9.893e-4, Galerkin "not stabilize", old two-prime
  optimizer values, LP lattice orders, thm:P3/prop:NC/subsec:where items, unpublished-work item, tr M_- ). Quoted
  ratios/values rounded to 1–2 significant digits; λ_A(½log3) quoted as ≈9.4e-4 consistent with 9.448e-4.

## Not restored (excluded per instructions or not provable as stated)
prop:uniform, thm:Al(c), cor:RH-type chains, sentence "if RH is true every true statement implies it", rem:excess clause
"RH is the statement lim λW ≥ 0", "What remains" (inertia), witness decorrelator paragraph, rem:odd080, the chain at one
window (uses thm:KEP3/RH), rem:P4-type items.

Rough size: ≈22 pages added (88 vs 66).

---
# INSERT_C — section "The window form as a truncated Wiener–Hopf operator" (sec:wh)

Fragment: C/sec_wh.tex (~10.5 pp in main_short layout). Bib: C/bib_wh.tex (3 \bibitem, alphabetical slots: Bottcher before Bombieri? -> place BottcherSilbermann2006 after Bombieri2000, Halmos1969 after Groskin2026, Simon2005 after Schilling/SSV2012).
Placement: new \section immediately AFTER sec:coer ("A finite reduction") and BEFORE \section{First contact} (sec:firstcontact).
Reason: uses lem:compact, thm:parityschur, thm:log5W (earlier); sits next to the other finite reduction. (After sec:log5 would also compile, but sec:coer is the natural neighbour.)
Test: test_C.tex, pdflatex x2: 0 errors, no overfull boxes in the fragment, 66 -> 77 pp.

New macros: none. Theorem envs: existing (theorem/lemma/proposition/corollary/definition/remark).
External labels referenced: eq:Aform lem:compact lem:mbounds lem:monoT lem:parity lem:polar sec:log5 thm:log5W thm:parityschur (all in main_short);
 prop:band prop:negtrace prop:NC (to be restored by other tracks, same labels; undefined in my test).
 Used parts: prop:band(iii),(iv) and tau_last; prop:negtrace notation Pos_T/Neg_T, sigma_pm, (i) trace class; prop:NC only for the name S_{T,tau_1}.
New labels: sec:wh subsec:wh-{pencil,angles,krein,prolate,schur,quartet,moments,det,oldnew,index} lem:wh-cP def:wh-B thm:wh-pencil eq:wh-sandwich
 rem:wh-pencil thm:wh-angles cor:wh-nogap prop:wh-notangles lem:wh-krein cor:wh-step rem:wh-model def:wh-V lem:wh-W thm:wh-necessary lem:wh-neg
 lem:wh-pos thm:wh-LW rem:wh-LWnum lem:wh-schurabs thm:wh-schur rem:wh-schur lem:wh-Q prop:wh-K lem:wh-mom lem:wh-T lem:wh-Tprime rem:wh-mom
 thm:wh-det thm:wh-detinherit cor:wh-negonly rem:wh-det prop:wh-oldnew lem:wh-birth lem:wh-shannon eq:wh-aW prop:wh-index prop:wh-polarres rem:wh-index

Notation changes vs the draft (clashes with main_short): W_T (complement) -> \mathcal X_T; W_T(sigma_beta) -> \mathfrak w_beta; H_T (prolate block) -> \mathsf M_T;
V_T -> \mathcal E_T, \mathcal E^P_T; Pi -> \mathrm{pr}_T; psi (prolates) -> e_i^pm, f_i^pm; J_i -> Delta_i; Q_pm -> \mathsf Q_pm; Q_z -> \mathfrak Q_z;
A_WW -> c_X (bottom); Gamma_T(phi_ev) -> \mT(\chi_ev); varphi_par -> chi_par; sigma_par -> r_par; K (Schur map) -> \mathsf K.

| result | status | source |
|---|---|---|
| lem:wh-cP, def:wh-B, thm:wh-pencil (sandwich C-W1 fixed: u_1 lower end, h* upper end; (iv) also with nu_j(Neg_T)) | PROVED | R186_034 Thm 2.1, 2.2; R186_042 Thm 2.1; CHECK IV.1-3 |
| rem:wh-pencil | NUMERICAL (one sig. fig.) | R186_034 §2.3 |
| thm:wh-angles (C-W2: cot^2 of angle to ran Q_-), cor:wh-nogap, prop:wh-notangles (+ proof beta_1>0) | PROVED | R186_042 Thm 2.3, Cor 2.4, Prop 2.5; IV.6-8 |
| lem:wh-krein (C-W3: rank-one value is a LOWER bound of beta_1, necessary only), cor:wh-step | PROVED | R186_043 M0 + R186_115 §1.1; IV.9-10 |
| rem:wh-model | NUMERICAL; slope law dropped (ARGUED, fitted) | R186_042 §3, R186_043, R186_115 |
| def:wh-V (pr_T V, C-W4), lem:wh-W, thm:wh-necessary, lem:wh-neg, lem:wh-pos (not exact at s=0, C-W11), thm:wh-LW | PROVED (constants symbolic) | R186_047 + R186_116; R186_044 Thm 1 |
| rem:wh-LWnum: c_X values, incl. the "modulo floating quadrature" ones | NUMERICAL (stated as such) | R186_047 §3, R186_116 MAJOR-1 |
| lem:wh-schurabs (new self-contained proof; draft's "lambda_A <= min(c,lambda_S)" corrected: lambda_A <= c_X, lambda_A <= lambda_S only if lambda_S >= 0), thm:wh-schur incl. two-sided inheritance lambda_A/||M|| <= 1-rho <= (1+||K||)^2 lambda_A/lambda_min(M) | PROVED (conditional on c_X>0, stated as hypothesis) | R186_044 Thm 2 + R186_115 §5, R186_116 §1.5 |
| lem:wh-Q, prop:wh-K | PROVED | R186_044 Lemma Q, Prop K (Lemma P ARGUED: dropped) |
| lem:wh-mom, lem:wh-T, lem:wh-Tprime | PROVED (barriers for universal criteria; class declared) | R186_045 |
| thm:wh-det (D_B entire genus 0, n_- = #zeros in (0,1), lambda_A>0 iff no zero in [0,1]) for every admissible splitting | PROVED | R186_034 Thm 2.1 |
| thm:wh-detinherit (exact inheritance 1-1/s_1 in [lambda_A/p(u_1), lambda_A/p(h*)], D(1)=lambda_A*R, leading term with eps_0<1 is a two-sided estimate of lambda_A, eps_0>=1 never decides), cor:wh-negonly (det(1+Neg), angles, any function of (sigma_-,U_T) cannot decide) | PROVED / NO-GO for declared class | R186_034 Thm 2.2, 3.1 (reformulated: R186_107 1d — barrier stated about approximants, not about all proofs; structural certificates excluded explicitly) |
| rem:wh-det (Szegő/Kac–Akhiezer) | CITED [BottcherSilbermann2006 §10.9]; numerics NUMERICAL | R186_034 §1.3, §4 |
| prop:wh-oldnew, lem:wh-birth, lem:wh-shannon | PROVED | R186_049 Prop 2.1; R186_048 Lemma 3.1, 2.3 |
| prop:wh-index (i),(ii),(iii) | PROVED (uses thm:log5W, not Zhu: C-W10) | R186_028 Thm 1.2, 1.4 + R186_106/107 |
| prop:wh-polarres (eigenvalue -1 explained) | PROVED under stated invertibility hypotheses | R186_028 Thm 2.1 |
| rem:wh-index: "n_-(a_T|D_T)=1 on [0.12, ½log5]" | NUMERICAL (rests on 1-D sign of m_T(chi_ev), uncertified) | R186_028 Cor 1.3 |

Dropped: rem:wh-labels/rem:wh-honest bookkeeping; prop:wh-basis (pure change of basis); first-order quartet law (ARGUED); all memo IDs;
old/unconverged lambda_A values (3.9e-12, 1.7e-11); comparison with prop:NC counts (different form, A_inf); "invisible newborn" numerics.
R186_112 (prolate tail / near-balanced directions = low-zero sampling) not entered: only numerical.

---
# INSERT_D — run D (Nyquist sampling / two sectors; Witnesses)

## Fragments and insertion points (base: main_short.tex)
1. frag_D_nyquist.tex  -> new \section "Sampling at the Nyquist mesh and two-sector structure" (\label{sec:nyq}).
   Insert immediately AFTER sec:coer ("A finite reduction") and BEFORE \section{First contact} (sec:firstcontact). ~6 pp.
2. frag_D_witnesses.tex -> new \section "Witnesses" (\label{sec:wit}).
   Insert AFTER sec:firstcontact and BEFORE \section{Open problems} (sec:open). ~6 pp.
   (It uses lem:roughEF, thm:log5A, thm:C, cor:margin1/2 and sec:nyq; it does not depend on sec:firstcontact,
   so it may also go right after sec:nyq.)
Test: test_D.tex = main_short + both \input's + bibitem; pdflatex x2: 0 errors, 0 undefined refs, no new overfull boxes; 66 -> 78 pp.

## New macros: none. (Uses \mathscr from mathrsfs, already loaded.)
## Bibliography: add
\bibitem{Boas1954} R.~P.~Boas, \emph{Entire Functions}, Academic Press, New York, 1954.
(cited as \cite[\S7.5]{Boas1954} for Akhiezer's factorization). Also uses existing IK, Krein1940.

## New labels
sec:nyq, eq:nyq-sT, lem:nyq-sampling, thm:nyq, eq:nyq, eq:nyq-r, prop:nyq-alias, rem:nyq-num, prop:nyq-LK,
rem:nyq-circle, thm:nyq-sectors, cor:nyq-sandwich, prop:nyq-nopoint, rem:nyq-pointwise, thm:nyq-cone, rem:nyq-dual,
thm:nyq-schur, rem:nyq-schur-num;
sec:wit, def:wit, lem:wit-basic, thm:wit-Tc, lem:wit-freeze, thm:wit-asym, lem:wit-node, def:wit-model, thm:wit-model,
cor:wit-consistent, rem:wit-model-num, lem:wit-conc, prop:wit-Egamma, prop:wit-coh, prop:wit-cheb, rem:wit-cheb,
prop:wit-sens, rem:wit-sens.
## External labels referenced (all exist in main_short)
thm:A, eq:Aform, eq:m, eq:target, lem:K, thm:S, lem:mbounds, lem:monoT, lem:contA, lem:compact, prop:P, lem:roughEF,
prop:finite, subsec:finite, cor:void, cor:margin1, cor:margin2, thm:log5A, thm:C, thm:coer-schur, app:num.
No labels from other tracks needed.

## Status of each result (source memo + review checked)
### sec:nyq
- lem:nyq-sampling (sampling of c_F; annihilator (-1)^k): PROVED (new short proof by Parseval on L^2(-2T,2T), no Poisson). Src R186_051 Thm 4.1(a-c), R186_117 §1, R186_052 §2.6.
- thm:nyq (Nyquist identity with s_T = sigma_T + int_{2T}^inf cos(tau u)K): PROVED, with the mu_eps + monotone convergence repair of R186_117 m1; absolute convergence exactly on D_T (proved directly, no Plancherel-Polya needed). Mesh closed form of r_T: PROVED. Src R186_051 Thm 4.1(d) as corrected by R186_117 MAJOR-1.
- prop:nyq-alias (aliasing with sigma_T; Tate-moment expansion; m=0 term vanishes on P_T): PROVED. Src R186_117 §0-§1, R186_052 "Alias de m".
- rem:nyq-num: NUMERICAL (alias on minimizer ~5e-4,1e-4,5e-5). Src R186_117 §2.
- prop:nyq-LK (window measure mu_T; Levy-Khintchine form; conditional negative definiteness with CORRECTED sign (R186_118 m3); s_T(omega_k)->inf; c_T<0 for T>=1/2 log2): PROVED. Src R186_052 §1, §4.2; R186_118 §3.
- thm:nyq-sectors (a_T = 1/2(s_per+s_anti) as parity splitting of the Nyquist identity; Delta_T reflection identity = aliasing identity R186_052 Thm 2.4; H Laurent symbol e^{i theta/2}, unitary, H^2 shift; l^2 model 1/2(D_e+H^T D_o H)): PROVED. Presented as corollary of the Nyquist identity split by parity, per R186_118 (m6). Existence of Delta_T as an improper integral proved (not in memo).
- cor:nyq-sandwich: PROVED (R186_052 Lemma 6.2).
- prop:nyq-nopoint (no common eigenvector of the two sectors; sectors are functionals of c_F): PROVED — stronger than R186_053 Prop 1.3 (which only argued non-commutation).
- rem:nyq-pointwise (joint LP with Tate multipliers and annihilator fails at 1/2log3, log2, 1/2log5, 1, 2): NUMERICAL. Src R186_118 §4 (joint LP values).
- thm:nyq-cone (primal cone via Akhiezer + Blaschke; Tate = double zeros; P_T=(1/4-d^2)H^2_0; hyperplane): PROVED, Akhiezer CITED. Src R186_052 Thm 3.1/Cor 3.2 + R186_118 §4.
- rem:nyq-dual: R186_052 Thm 3.3 ("window Bochner") NOT stated as theorem — false as written (R186_118 MAJOR-1), only modulo (-1)^k and conditional on a weighted Riesz extension; recorded as remark, "neither proved nor used".
- thm:nyq-schur (i) coercivity c_eta=1/2(s+^e+s+^o), (ii) exact Schur via Riesz/Lax-Milgram (form version; avoids operator inverse), (iii) S^low certificate without inversion, with explicit L^2 representer g_F, (iv) monotonicity under truncation: all PROVED. Src R186_053 Thm 2.1, 2.2, Cor 2.3, Lemma 2.4. (Lemma 2.5 omitted.)
- rem:nyq-schur-num: NUMERICAL (S^low positive in Galerkin model at the three windows; ratios ~0.7/0.9/0.95; negative for quartet model). Barrier d_eta >~ lambda_A^{-1/p}: NOT proved (ARGUED in R186_053, relies on a conjectural decay law) -> stated as heuristic in the remark only.
- RETRACTED and NOT included: the "99.4% antiperiodic sector" reading and "lambda_A is a cancellation of two sectors" (R186_118 MAJOR-3).

### sec:wit
Adversarial coverage: R186_050 has no dedicated adversarial review; I checked it against R186_114 (falsifier audit: M_m form-level object PROVED, f_t primitive witness only ARGUED/CONDITIONAL — f_t NOT used), R186_117 and the README entry (which corrects 050: no lower bound -exp(-e^{cT}) exists; N8 direction). I re-derived every proof.
- def:wit, lem:wit-basic (cone, open, J-invariant, parity; N3a low-frequency bound; N4a alignment dichotomy; N8 value bound): PROVED. Src R186_050 Lemma 1.2, (N1a),(N3a),(N4a),(N8).
- thm:wit-Tc (absorption; set of T with witness = (T_c,inf), T_c > 1/2 log5 (strict, from thm:log5A+continuity; memo had >=); equivalences; along a sequence 1/2 log n_k; dichotomy of the limit stated with cor:margin1): PROVED. Src R186_050 Lemma 1.3, Thm 1.4, Prop 4.7(a). Prop 4.7(b) "L in {0,-inf}" (ARGUED, uses zeros) NOT included.
- lem:wit-freeze, thm:wit-asym: PROVED. Src R186_050 Lemma 4.1, Thm 4.2 (made into a precise set statement).
- lem:wit-node: PROVED, with explicit error constants. Src R186_050 Lemma 3.1, R186_114 §1.1.
- def:wit-model, thm:wit-model: (i) shared structure PROVED; (ii) Weyl bounds PROVED (R186_050 Cor 3.2); (iii) witnesses at EVERY window for quartet multiplicity m>=m0(T,delta,gamma): PROVED here (new, elementary; replaces the citation of R162_2501 Prop 1, whose upper bound assumes the location of the other zeros and so cannot be used); (iv) single quartet witness => 4T(g(delta T)-1) > lambda_A (R186_051 Thm 4.4) PROVED, plus a proved corollary: no witness at 1/2 log3 for delta <= 0.013 (uses certified thm:C); (v) degenerate quartet PROVED.
- cor:wit-consistent (= R186_050 Thm 4.6 in proved form): PROVED as a transfer statement about arguments (wording per R186_114 §1.2). The numerical items (1)-(7) of Thm 4.6 for M_1 are NOT asserted.
- rem:wit-model-num: NUMERICAL (M_1 witnesses at log2; first window ~0.57; thresholds delta* recomputed with the reference lambda_A values: ~0.05, 3e-4, 1.5e-6 — NOTE R186_051's 0.093/8.9e-4/2.6e-6 are inconsistent with its own formula and were not used).
- lem:wit-conc, prop:wit-Egamma (target => (E_gamma)): PROVED (concentration lemma proved with a fixed bump eta(t/T); memo used a different cutoff). Growth of the quartet term along F_T: NUMERICAL only (R186_051 Lemma 2.3 asymptotics not reproduced as theorem).
- prop:wit-coh (i) sampling of the coherence + witness => weighted coherence < -b_T (R186_051 Thm 4.1(c), Cor 4.2): PROVED; (ii) = R186_051 Prop 2.2(a): PROVED sup bound 4(g-1); the separation claim at log 2 is NUMERICAL (stated after the proof).
- prop:wit-cheb (= precise part of R186_051 Prop 3.3/Lemma 1.7: polar term <=4, Chebyshev form, crude bound): PROVED; rem:wit-cheb: the VK bound CITED (IK §8.5); the "no intermediate form / equivalent to absence of quartets" part of Prop 3.3 NOT included (it is a zero-side statement).
- prop:wit-sens (= proved part of R186_051 Prop 4.5: Lipschitz bound, Rayleigh flip with kappa_T, coherence moves <= eps A_T/4T): PROVED; rem:wit-sens: NUMERICAL kappa_{log2} ~ 0.09, flip at eps ~ 1e-6.

## Not proved / downgraded
- Thm 3.3 of R186_052 (dual cone = B_T-smoothing of positive measures): remark only.
- Barrier d_eta >~ lambda_A^{-1/p}: heuristic remark.
- (E_gamma) violation rate e^{2 delta T}/T for the model: numerical remark.
- Primitive witness of the single-quartet model M_1 at large T: not proved (needs zero-location input); replaced by the proved multiplicity version (thm:wit-model(iii)).

---
# INSERT_E (run E): Barriers for classes of arguments

Fragment: E_barriers.tex (about 8 pp.; test build test_E.tex/test_E.pdf goes from 66 to 74 pp., 0 errors).
Placement: a new \section{Barriers for classes of arguments}\label{sec:barriers}, inserted IMMEDIATELY BEFORE
\section{Open problems}\label{sec:open}. It must come after run C's Wiener-Hopf section, which defines thm:wh-schur.
Alternative: right after sec:negative. That works only if it follows C's section, so before Open problems is preferred.
Suggested one-line addition to Intro "Barriers": "Linear bounds in a fixed frame, families of windows, observable
patterns and local criteria are limited in \S\ref{sec:barriers}."

## New macros: none.
## Bibliography (add to thebibliography):
\bibitem{Bochner1951} S.~Bochner, \emph{Some properties of modular relations}, Ann.\ of Math.\ (2) \textbf{53} (1951), 332--363.
\bibitem{KahaneMandelbrojt1958} J.-P.~Kahane and S.~Mandelbrojt, \emph{Sur l'\'equation fonctionnelle de Riemann et la formule sommatoire de Poisson}, Ann.\ Sci.\ \'Ecole Norm.\ Sup.\ (3) \textbf{75} (1958), 57--80.   [venue to double-check: one memo says Ann. Inst. Fourier]
\bibitem{LandauWidom1980} H.~J.~Landau and H.~Widom, \emph{Eigenvalue distribution of time and frequency limiting}, J.\ Math.\ Anal.\ Appl.\ \textbf{77} (1980), 469--481.
\bibitem{McClellanParks1972} J.~H.~McClellan and T.~W.~Parks, \emph{Eigenvalue and eigenvector decomposition of the discrete Fourier transform}, IEEE Trans.\ Audio Electroacoust.\ \textbf{20} (1972), 66--74.

## Labels defined
sec:barriers, subsec:bar-lin, subsec:bar-fam, subsec:bar-pat, subsec:bar-loc, lem:transfer, lem:half, cor:directbound,
rem:directbound, prop:acct, thm:posext, eq:posext, rem:posext, prop:primeblind, rem:bar-lin, lem:transport,
thm:famblind, lem:selfdual, prop:ft, thm:famFE, rem:bar-fam, lem:quartet, def:quartetmodel, prop:quartetmodel,
thm:quartetneg, prop:Krein2, rem:quartetnum, cor:pattern, rem:bar-pat, lem:compress, thm:nolocal, thm:X, rem:X,
lem:flowdet, rem:bar-loc.
Local notation introduced: U_T := {sigma_T < 0} (subsec:bar-loc), the time-band operator S_U, E_eta(U), Q_z, Phi_c, Phi_s,
xi_{z,k}, f_t, lambda_A(T;f_t), lambda_A(T;xi_{z,k}). If run C also defines U_T, use C's definition and drop the line here.

## External labels referenced
In main_short: sec:negative, prop:P, eq:m, lem:mbounds, laminfP (macro), thm:C, thm:log5A, thm:log5W, thm:N, prop:TK, thm:R,
lem:Rrig, cor:nontermwise, eq:nuw, lem:monoT, lem:contA, lem:compact, lem:roughEF, thm:finmod, cor:void, subsec:finite,
rem:Kprim, thm:coer-schur, eq:target, eq:form, eq:W.
From run C (undefined in my test build): thm:wh-schur (twice: before thm:nolocal and in rem:bar-loc).
Not used: R186_053 Prop 1.3 (run D), lem:wh-birth (run C), the W-det/W-mom/W-coh material.

## Status and source of each result
- lem:transfer: PROVED (logic).
- lem:half: PROVED (R186_031 §2,§4; adversarial R186_108 §5 confirms that the constant 1/2 is optimal for every a in (T,2T)).
- cor:directbound: PROVED. CORRECTED: R186_031 wrote "lambda_A >= lambda_A^inf - v2/2 for 1/2log2 < T < log2". For
  T > 1/2 log 3 the contact 3 also enters, so the clean statement is now the general bound plus the case T <= 1/2 log 3.
- rem:directbound: NUMERICAL (T_1^D ~ 0.367, R186_031 §5).
- prop:acct: PROVED (R186_030 §3.1, R186_108 §3; the values of Delta were recomputed with mpmath). The "thm:C is tight at tau=0"
  reading (refuted by R186_108 M2) is not used.
- thm:posext: PROVED (weak duality; R186_030 Thm 3, the excluded class corrected per R186_108 M4 to nu>=0 AND beta=(2,0);
  b = sqrt(beta/alpha) written explicitly per M3).
- rem:posext: NUMERICAL. kappa = -0.13767 (1/2 log 3) and -0.12840 (1/2 log 5) were recomputed by me with mpmath
  (25 digits, quadrature not enclosed; the script is E_kappa.py in this directory). The free-beta class with nu>=0 is
  stated as NOT excluded (only an LP indication).
- prop:primeblind: PROVED (lem:mbounds(iii) + almost periodicity; the "real prime-side obstruction" of R186_108 §1).
  Thm 2 of R186_030 (ARGUED) is omitted.
- rem:bar-lin: points to lem:Rrig/cor:nontermwise ("Lemma R"), thm:N, prop:TK, thm:R.
- lem:transport: PROVED (R186_036 Lemma 1, 1'; the "exactly the inherited certificates" claim was rejected by R186_110
  and is not made; the identity with eq:nuw is stated).
- thm:famblind: PROVED and UNCONDITIONAL. This is NEW relative to the memos: the falsifier is the amplification
  Lambda + c 1_{n=n0} with n0 > e^{2T_1} from thm:finmod(ii), which agrees with zeta on every window <= T_1 and is negative
  later. It replaces the f_t falsifier for the class (values on bounded J + monotonicity + continuity + any
  amplification-closed weight class).
- lem:selfdual: PROVED (R163_901 Lemma 2.1; McClellan-Parks multiplicity CITED).
- prop:ft (i): PROVED, given the CITED FE for self-dual measures [Bochner, Kahane-Mandelbrojt]. (ii): PROVED (R163_901
  Thm F.4). The argument is phrased purely in terms of the window form, with no zeros involved.
- thm:famFE: CONDITIONAL on (H_f) "lambda_A(T; f_t) < 0 at some T" (the primitive witness; ARGUED in R163_901 Cor F,
  CONDITIONAL in R186_114 §2.4). Hypothesis stated in the theorem; rem:bar-fam explains why it does not follow from (ii).
  As R186_110 requires, rem:bar-fam says two-sided asymptotic laws are NOT excluded.
- lem:quartet: PROVED (R186_044 Lemma Q; R186_114 §1.1 derivation).
- def:quartetmodel / prop:quartetmodel: PROVED. I used the polynomial model xi * (quartet)^k, which is the definition the code
  runs (R186_114 MINOR 5). Zero-side identity via lem:roughEF. Monotonicity and continuity are proved as perturbations.
- thm:quartetneg: PROVED and NEW. Negativity at EVERY window T > 0 for multiplicity k large, through an explicit test with
  Phi_c = 0 and Phi_s != 0. This is how I supply a proved primitive witness without RH. R162_2501 Prop 1 is stated under
  "exactly m off-line quartets", i.e. all other zeros of zeta on the line. That is an RH-type hypothesis, forbidden here,
  so it is NOT used.
- prop:Krein2: PROVED (R186_044 Prop K).
- rem:quartetnum: NUMERICAL (phase-187 DATA_MM_FALSIFIER.csv, PATTERN_REPORT §3.4, R186_114 §1.3 recomputation; values
  -1.52e-3 / -2.85e-2 at log 2, -4.97e-3 at 1/2 log 5; delta->0 limit = triple zero, per R186_114 correcting the report).
- cor:pattern: transfer; NUMERICAL for k=1 sharing, PROVED for the k-large negativity and the shared structural properties.
- rem:bar-pat: restates thm:finmod / cor:void as the arithmetic-side members of the same family (reference only, no duplication).
- lem:compress: PROVED (R186_044 Thm 1). The exact Schur converse is referenced as thm:wh-schur (run C).
- thm:nolocal: PROVED and NEW in this form. The explicit falsifier is sigma^(eta) = min(sigma_T, eta): same negative set,
  same values on {sigma_T < eta}, negative bottom for small eta. It replaces the numerical "M1 passes C_T" statement of
  R186_044, which is kept only as a numerical remark (rem:bar-loc).
- thm:X: PROVED (R186_046 §1-2: identity + lambda_A >= 0, with the sign corrected against R186_045; Observation 2.1 = (iv)).
  §3 of R186_046 (rejected by R186_116 FATAL-1) is NOT used. The Landau-Widom count is CITED in rem:X. The numerical
  c_E values are those R186_116 reproduced.
- lem:flowdet: PROVED (R186_045 Lemma 1.1, stated in finite dimension: Jacobi + Hellmann-Feynman). rem:bar-loc gives the
  consequence and the numerical blind-regime facts (R186_044 §4).

## Omitted (with reasons)
- Lemma N and the dominance identity (R186_031): they need the semilocal Sonin machinery (Son_S, C_S) and cannot be stated
  without it.
- Lemma H (R186_029): ARGUED.
- R186_030 Thm 2 (Euler -> zeros): ARGUED/incorrect (R186_108 M1).
- R186_037 (leaves, compactness lemmas A-E, Prop G): not self-contained; it depends on the BR barrier framework and on
  R185 memos.
- R186_036 Lemma 2 (fold at prime entry): CONDITIONAL on (REG) and contradicted numerically at 4 of 5 thresholds
  (PATTERN_REPORT §1.3).
- Pattern laws (-ln lambda_A ~ 13 e^{2T} ...): CONJECTURE/NUMERICAL, not stated.

## Adversarial review (sections 12–19)
- Amplification falsifier (thm:finmod(ii), cor:void, thm:famblind): checked line by line. F_+ of lem:cpos is real, smooth, in P_T (codim-2 intersection of an infinite-dimensional image) with c_F(log n_0)=||phi||^2>0. The amplified form is a_T(F) - (2c/sqrt n_0) c_F(log n_0), negative for c>c_*. a stays >=0, zeta_a = zeta*exp(c n_0^{-s}/log n_0), so it has the zeros and pole of zeta. In thm:famblind, n_0>e^{2T_1} leaves lambda_A unchanged on J. Monotonicity holds by zero extension, and continuity by lem:contA, which uses only finite weights. VERDICT: PROVED, unconditional. Its scope is the declared class: lambda|_J (J bounded), monotonicity, continuity, and membership in a class closed under one-term amplification. It does NOT cover classes that require the functional equation.
- thm:famFE: correctly CONDITIONAL on (H_f). prop:ft(ii) proves negativity only for the COMPLETE form, and rem:bar-fam says so. No change.
- Barrier classes: famblind, famFE and cor:void state their classes explicitly, and lem:transfer is stated as excluding the deduction, not the conclusion. No change.
- (L2) FIXED. The old wording said the least eigenvalue of S_{T,k} "inherits the size of lambda_A ... times a factor of order one", which is not proved. It now reads lambda_A <= lambda_S, and lambda_S <= (1+||K||)^2 lambda_A when lambda_S < c. The margin bound is restricted to T>=1 (cor:margin1). The claim that the problem "requires an input beyond ..." was replaced with "the barriers exclude, each within its declared class, ...".
- (N): consistent with prop:wit-coh, prop:wit-sens, rem:wit-cheb and prop:wit-Egamma. All labels resolve.
- thm:coer-schur (iii) follows from the sandwich (eq:coer-sandwich). lem:firstcontact uses monoT, contA, log5A and compact. Complete.
- C-W1/C-W2: present in thm:wh-pencil and thm:wh-angles as recorded above. Not re-derived.
- Recompiled (pdflatex x2): 128 pp, 0 undefined references.

## Adversarial review (sections 1–11)

Scope: §§1–11 and appendices A–C of main.tex. Every theorem, lemma and proposition statement was diffed against main_pre_definitive.tex (66 statements changed, 7 new). Proofs were read in the new notation (§2 conventions: mT, PiT, Q_T, V_a, J, D_T). Numerical constants were recomputed independently with mpmath: C_0, tau_0, v_2, v_3, tau_a, tau_b, tau_b', y_0, tau^lo, 68.513, T_0(A) for A=0,…,5, Cor. SC1, U(T) of prop:archneg, the bounds of cor:mono, the cor:arena evaluations, eps_k and the constant 3.97e9 of cor:margin1, and the comb values of rem:taulast. All agree. Numerical values (9.448e-4, 9.83e-8, 3.10e-12) and certified bounds (8.8577e-5, 2.5e-12, 1e-18) are unchanged and labelled correctly. No memo IDs, no logbook tone, and no RH equivalence remain in scope; the RH clauses of old thm:KEP1(iii), cor:margin2(iii) and thm:Al(c) were already removed.

Issues found and fixed (local edits):
1. prop:decide: MATHEMATICAL ERROR introduced in the definitive version. Search (b) looked for F in P_T with a_T(F)<0. That detects lambda_A<0, not lambda_P<0, so the procedure need not terminate when lambda_P<0<=lambda_A. The statement also contradicted itself ("F in P_T with a_T(F)<0 … not the sign of lambda_A"). FIXED: (b) now enumerates feasible points of (P) (mixtures of two step-function measures, moment-corrected by four fixed witnesses as in thm:Vp(ii)). It uses attainment of the primal and the real/imaginary splitting of a minimizer. The statement now says that it produces a feasible point of (P) of negative value.
2. thm:finZ ("in particular") and cor:infinite: the claim "for every H>0" was false for H<gamma_1, where the truncation is empty and equal to 0. The theorem also needs a real multiset. FIXED: H >= gamma_1 and H below the height to which the zeros are on the line (Platt–Trudgian), with w continuous. The proof of cor:infinite now records these two properties.
3. lem:W: the proof showed only that 0 is interior to the convex hull (the measure version). The claim about the image of the unit sphere was unproved. FIXED with a direct three-line argument.
4. prop:negtrace(iv) used WP_T about 190 lines before its definition (subsec:finite). Replaced with "lambda_A >= 0".
5. Paragraph before prop:archneg: it claimed to "improve the bound T*_{inf,P} >= 0.58". The proposition bounds T*_inf instead. FIXED: it now says the two thresholds are distinct.
6. prop:env/remark: "checked on [0, tau_1+NP], tau_1+NP≈442" was arithmetically wrong (30+2·137.26=304.5). FIXED: tau_1+(N+1)P ≈ 442. This error was inherited.
7. §8 (after cor:SC1): ½log31 = 1.71699, not 1.71673. Inherited.
8. Remark after thm:C: "mean |a_j| … 0.02 at u≈40" is impossible, because the last atom is u_460 = 21.06. FIXED to "a few hundredths near the last atom". Inherited.
9. thm:Dtail case (b): the bound on |R''| was missing the factor 2 on |w'| and misplaced e^{-u/2}. FIXED.
10. thm:sl-L2: the absolute form (sl-84(ii)) relies on "the first sentence, which does not use (H_G)", but the proof did not show that. FIXED by adding the argument: G_0R' is Hilbert–Schmidt and the G_0 kernel is locally integrable, so d_S ∈ L^1_loc unconditionally, and (H_G) is used only for the O_R(1) bound.
11. §9: the bound ||PiT|| <= A_T was cited forward to prop:coer-prime (§13). It is now proved inline (|c_F(log n)| <= ||F||^2).
12. §8 margin facts were labelled (X19), (X19′), (X-N), which are memo-style labels. Renamed (Z1), (Z2), (Z3).
13. Missing full stop after "T=0.80" in the remark after thm:index.
14. App. A (enclosures of thm:N): the test kernel was written \varphi, which clashes with the Bernstein function varphi, and the period was written W, which clashes with W_T. Changed to \vartheta and \mathcal I_0, as in the proof of thm:N.
15. App. A: the sentence "A run at T=0.90 lies outside the range" was truncated. It is completed from the old version ("condition T<0.88137 and is not used").

Checked and correct, no change: lem:mbounds, lem:monoT, lem:contT, lem:contA, lem:compact, thm:S, thm:A, cor:mono, prop:weak, lem:gbounds, thm:D1 (determinant sinhT coshT + T), thm:O, thm:W (sT(0)=C_0−A_T), prop:P, lem:roughEF, thm:P3, cor:AP, lem:F1, lem:T, cor:T2, thm:E, prop:M, thm:Z, thm:Zexh (d_*(0.3)>0), lem:Rrig, lem:smooth, thm:finDet, prop:loc (signs c_k), thm:Dtail, cor:comb, cor:bprof, thm:KEP1/2/dich, prop:TK, thm:Bbeta, lem:val, thm:N/Np (divisor reductions), thm:R, cor:R3, thm:latedge (E_edge constants, factor 1.862), prop:arch, prop:nodes, lem:parity, lem:strict, thm:index, cor:Tarch, prop:archneg, prop:NC, cor:P3, thm:J, cor:nasym (4.0042), cor:H1, thm:arena, cor:arena, prop:band, prop:align, prop:negtrace, thm:Vp, cor:CP, thm:SC, prop:finite, lem:cpos, cor:Qp, thm:finmod, lem:degen, prop:finsupp, cor:void, thm:inertia-nogo/-B2/-finite, quartet lemma, inertia-rank, lem:Ncount (6.11), lem:zerosum, lem:testfam, thm:margin, cor:margin1/2, §10 (sl-gap, sl-TC, sl-lac, sl-84, sl-split), thm:parityschur, prop:polarcap, prop:schur, thm:w11, thm:nest, prop:shifts, lem:N, prop:G, lem:KyFan, prop:TAY, lem:bern (1/8), lem:multiband (m'' summand), prop:haynsworth, prop:negplane, lem:rzero, prop:lowercert (c=±½ algebra).

Labels: the conditional statements are labelled honestly. (H_G) is stated as an assumption in thm:sl-L2 and cor:sl-split and listed in §open, and the "Assume n_-(W^{Z'}) >= 2m" clause in subsec:inertia-excl is marked as not proved. Forward references from §§2–11 into §§12–19 are to results with no circular dependence: log5A/log5W are cited only as comparison, coer-prime is now inline, and shifts and convfail are cited only in remarks.

Recompiled (pdflatex x2): 128 pp, 0 errors, 0 undefined references. Sections 12–19 were not touched.


## Label alignment (adversarial review of the secondary items, , later the same day)

The entries above describing thm:sl-L2 / cor:sl-split as CONDITIONAL on (H_G) and thm:famFE as CONDITIONAL on (H_f)
are superseded: (H_G) is Lemma lem:sl-HG (PROVED) and (H_f) is Proposition prop:ftprim (PROVED), both inserted in
the secondary pass (SECONDARY_ITEMS.md) and confirmed by the independent adversarial review recorded there.
Current labels: thm:sl-L2 PROVED (unconditional), cor:sl-split PROVED (Hilbert–Schmidt C_{ε_S}, δ-finite index),
thm:famFE PROVED (unconditional). Rows 10 and 18 of the table above and the notes at lines referring to (H_G)/(H_f)
are to be read with this correction.

#— Section "The shape of a proof" (sec:shape) and Problem (R)

Source: 03-research/phase-190-near-coincidence-experiment/memos/SHAPE_THEOREM.md, reviewed by an independent adversarial pass
(SHAPE_THEOREM_REVIEW.md, same day). Backup: main_pre_shape.tex. pdflatex ×3: **155 pp, 0 errors,
0 undefined references, 0 multiply-defined labels, 0 overfull boxes** (was 146 pp).

## What was inserted (before §Open problems)
| label | content | label of record |
|---|---|---|
| def:shape-obj / def:shape-ops / def:shape-class | form objects, modifications O₁–O₁₅ (two structural extras), deduction classes | definitions |
| lem:shape-del, -amp, -tail, -scale | O₁–O₄ (thm:finmod, cor:void, prop:finsupp, cor:wtail, lem:cpos, lem:degen, cor:Tarch; O₄^ε via prop:wit-sens) | PROVED; O₄^ε CONDITIONAL (κ_T ≠ 0) |
| lem:shape-weight | O₅ one weight (rem:resweights; admissibility ε ≤ Λ(n₀) for s = −1) | CONDITIONAL |
| prop:shape-eulerdel | **new in the paper**: a_P = Λ·1{p ≥ P}: Euler product over ℕ, integral, same zeros/pole, breaks only the FE, fails WP_T on [0.60, ½log P]; proof included | PROVED |
| lem:shape-quartet, lem:shape-ft | O₇, O₈ (thm:wit-model(iii), prop:quartetmodel, prop:ft, prop:ftprim) | PROVED |
| prop:shape-twist | **new in the paper**: ζ̃ = ζR (FE, reality, four poles in the strip, R ∈ [1/16,1] on the line, line identity Re ζ̃′/ζ̃ = −½m, ∫\|log R\| = 4πδ, curvature +3/(2δ²)); no argument from FE + line identity + finitely many strict mean-value bounds bounds ℓ″ pointwise; class excludes holomorphy ∧ order 1; proof included. Stated explicitly as NOT a window-form falsifier | PROVED (elementary) |
| lem:shape-epstein | O₁₀ Epstein (rem:twohalves, Weil's criterion, Davenport–Heilbronn): complete form negative; primitive witness not written | CITED / ARGUED |
| lem:shape-beurling | O₁₁ Beurling systems: no window form shown negative; not used in thm:shape(A) | ARGUED |
| lem:shape-field | O₁₂ field change: transfer principle only; falsifier open; the proof of Paper 46 Thm 18.1 is not used | PROVED (principle) / OPEN |
| lem:shape-fam, -local, -poisson, -classes | O₁₃–O₁₅; progression/sieve/zero-information/pattern classes | PROVED (patterns: NUMÉRICO for the full observable list) |
| lem:shape-margin | margin (cor:margin1) + universal moment/Lipschitz/determinant criteria (lem:wh-T, lem:wh-Tprime, thm:wh-detinherit(iii)) — stated as precision constraints, not transfers | PROVED (inputs CITED) |
| prop:shape-crit | (a) centre: prop:boundary + termwise vanishing of the paired zero sum; (b) packets: prop:Egamma-exact; collapse of the additive constant CONDITIONAL on convergence of the Riesz means; (c) **new in the paper**: Cesàro mean square of the comb = ½Σv_n² = 4T²(1+o(1)) (Mertens CITED), RMS 2T vs m(e^{2T}) = 2T + O(1); (d) thm:ceiling, thm:kappa with κ_* ≥ ¼\|C₀\| = 1.343; (e) thm:wit-Tc(iv) | PROVED except (b) CONDITIONAL |
| lem:shape-antisym, -lin, -misc, -flow | rem:fe; prop:opcalc + thm:sos/thm:D1; prop:cone/relative/posext/primeblind; lem:flowdet/thm:X | PROVED (readings ARGUED, rem:posext values floating) |
| prop:shape-inputs | the three inputs (Euler over ℕ, FE at q = 1, integrality) enter jointly: (i) a_P PROVED, (ii) Ξ_Q CITED, (iii) Beurling ARGUED, (iv) quartets/f_t keep the FE and break the Euler product over ℕ; Hamburger CITED (Titchmarsh §2.13) | as listed |
| lem:shape-restate | internal restatements: thm:Z, thm:KEPdich, thm:oneprofile, prop:AM, thm:coer-schur, wit-Tc(iv) | PROVED |
| thm:shape | three tiers: (A) transfer PROVED for O₁, O₂, O₃, O₄ (all c), O₆, O₇, O₈, O₁₃, O₁₄, O₁₅ and derived classes; (A′) with labels (O₄^ε, O₅ CONDITIONAL; O₁₀ CITED/ARGUED; O₁₁ ARGUED; O₁₂ OPEN; O₉ pointwise curvature only); (B) structure; (C) positive form | bookkeeping theorem |
| cor:shape | (a) exact and non-linear use of the window vector; (b) joint inputs; (c) the sign is a correlation (lem:degen supergradient; numerics labelled); (d) no slack | |
| rem:shape-scope | what the theorem does not say; upgrades for each unproved clause | |
| prob:region (sec:open, item (R)) | the admissible region as the paper's formal open problem, ten properties; objects not excluded listed | OPEN |

## Bibliography
Added \bibitem{Paper46} (Row D: the sign) and \bibitem{Titchmarsh1986} (Hamburger's theorem).

## Adversarial-review corrections carried into the paper (vs. the memo draft)
Theorem no longer claims transfer for O₉–O₁₂ or for the two structural modifications; Beurling ARGUED (no window form in the record);
universal criteria moved to the structural part (bottom 0, not < 0); T₀(0) = 0.74921; κ_* ≥ 1.343 (lower bound); Lemma I's branch
bookkeeping (quartets and f_t keep the FE); Corollary (e)10 no longer imports the Hodge-index-form requirements of Paper 46;
f_t primitive witness PROVED (prop:ftprim, confirmed by the independent review of ). Forbidden-vocabulary grep on the
inserted text (RH, GRH, memo IDs, "round", "phase"): none.

##— Shape theorem completed: estimates and exact identities

Backup: `main_pre_shape2.tex`. Sources: phase 191 SPEC_A/SPEC_B, phase 192 EI_001–003 with adversarial reviews and summary.

| item | content | label |
|---|---|---|
| subsec:shape-est | definitions: 𝓕_T^{(a)}, estimate (E_T,R_T), "decides by the estimate", μ_T | definitions |
| lem:shape-est | (i) pinching μ_T − R_T ≤ λ_A ≤ μ_T + R_T; at T ≥ 1, 0 ≤ μ_T − R_T ≤ 4·10⁹Te^{−15.449T}; (ii) exact Schur reductions (finite E) inherit: λ_A ≤ λ_S ≤ (1+‖K‖)²λ_A; (iii) slack > 𝔄_Tλ_A/\|κ_T\| gives the falsifier (1+δ)Λ; (iv) "no estimate carries the sign step" | (i),(ii) PROVED; (iii) CONDITIONAL (κ_T ≠ 0); (iv) ARGUED |
| rem:shape-est | doubly exponential precision only under Zhu's conjectural law (not used); (E_γ) exact threshold PROVED, no-slack CONDITIONAL; Nyquist pointwise form false (σ_T(0) < 0); integer family collapses through Λ∗1 = log | as stated |
| prop:shape-ext | exterior field of a primitive h: polar edge moment − Chebyshev fluctuation − K₁ tail | PROVED |
| prop:shape-family | (i) collapse D_w(N) = 2c log N − small-divisor defects; (ii) spectral form with Re R_{X′}; (iii) Mellin form of the test (growth of ζ CITED); (iv) second-order vanishing of the continuous term by both Tate conditions, ∫Ψ_w = 0 with the cut y ≥ 1, Chebyshev split | PROVED |
| prop:shape-phase | σ_T = 2Θ_T′; Z_T real; R_X = Θ_T′ + iZ_T′/Z_T | PROVED |
| lem:shape-ident | identities valid for every weight vector do not break closure under O₁–O₆; the three propositions are comb-generic (and survive O₁₁, O₁₅ where stated) | PROVED |
| rem:shape-ident | sign content of each identity (Schur step ARGUED; family inequality, restatement only under a NUMÉRICO hypothesis; phase identity none); "symbol rigidity" is a tautology, not a barrier; Fact N2 stays NUMÉRICO; ℤ²-self-duality not used | as stated |
| thm:shape | new items (B′) no estimate, (B″) no comb-generic identity; proof updated | as labelled |
| cor:shape | new items (e), (f) | |
| rem:shape-scope (iii) | upgrade conditions for (B′) | |
| prob:region | clause (11): the sign step is ζ-specific by construction (no estimate with remainder, no comb-generic identity); identities listed as coordinates, not objects of the region | OPEN |

Not claimed: any doubly exponential margin as proved (only e^{−15.449T} is); EI_002's "Fact N2 PROVED"; EI_003 Thm 2 as a NO-GO; EI_002 Thm 5(d). Own adversarial re-read against eq:symbol, eq:form, prop:sharp, lem:polarelim, prop:wit-sens, lem:wh-schurabs, prop:AM, lem:transl: fixed a.e.-in-t qualification (prop:shape-ext), the λ_S < c_X hypothesis in thm:shape(B′), and the pointwise mesh statement (stated for σ_T, not the polar-free form, whose value at 0 has no proved sign). Compilation: 159 pages, 0 errors, 0 undefined references, 0 overfull boxes.
