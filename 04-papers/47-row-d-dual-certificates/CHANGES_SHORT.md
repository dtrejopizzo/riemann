# main_short.tex — changes relative to main.tex

Source main.tex is unchanged. main_short.tex compiles with pdflatex (two passes, inline bibliography):
66 pp. (body 57 pp., Appendix A computer verifications 7 pp., Appendix B numerical values 1 p.),
no undefined references, no errors.

## Structure
1 Introduction (target eq. (target): λ_A(T) ≥ 0 ∀T; results; barriers; open problem; related work; conventions)
2 Preliminaries (lem:K, thm:S, thm:A, rem:Kprim, cor:mono, lem:mbounds, lem:monoT, lem:contT, new lem:compact, lem:contA)
3 Primal and dual programs (def:PD, prop:weak, lem:gbounds, thm:D1, thm:O, lem:W, prop:P, lem:roughEF)
4 Tail lemmas and an explicit certificate (lem:F1, prop:T0, lem:T, cor:T2, lem:hybrid, thm:E, thm:C)
5 The dual variable is the explicit formula (def:W, thm:Z, thm:Zexh, lem:Rrig, cor:nontermwise, lem:smooth,
  lem:fdict, thm:finDet, thm:finZ, cor:infinite, thm:Dtail, cor:comb; Kreĭn problem per window: def:KEP,
  lem:polar, thm:KEP1(i)(ii), thm:KEP2, thm:KEPdich = old KEP3(a))
6 Lattice certificates (prob:A, prop:TK, thm:Bbeta, lem:val, thm:N, thm:Np, lem:R1, thm:R, cor:R3,
  thm:latedge = old thm:AL (corrected Θ(1/M) statement), cor:ALdef)
7 The archimedean form (prop:arch, prop:nodes, lem:parity, lem:zeroext, lem:strict, thm:index, cor:Tarch,
  prop:archneg, thm:arena, cor:arena)
8 Obstructions (thm:Vp, prop:env, thm:SC, cor:SC1, prop:finite, lem:cpos, thm:finmod, prop:finsupp, cor:void,
  thm:inertia-nogo, margin: lem:Ncount, lem:zerosum, lem:testfam, thm:margin, cor:margin1, cor:margin2(i)(ii))
9 Complete form at one window (lem:Onat, thm:Al(a)(b), thm:parityschur, prop:polarcap)
10 Certified positivity up to ½log5 (thm:log5A, thm:log5W, cor:KEPlog5, lem:gmono, prop:onewindow, cor:convfail)
11 A finite reduction (def:coer-V, lem:coer-decomp, lem:coer-lowpass, thm:coer-B, prop:coer-prime, cor:coer-L1,
   thm:coer-schur, rem:coer-honest)
12 First contact (lem:firstcontact, operators, thm:PCfinite, Gamma observation, collars, prop:GEgap, prob:annihilate)
13 Open problems. App. A: lem:KyFan (=old thm:P), cor:P1, enclosures of thm:N/Np, prop:TAY, lem:border,
   lem:multiband, prop:haynsworth, prop:negplane, lem:polround, lem:rzero, prop:lowercert. App. B: numerical values.

## Dropped
All statements equivalent-to/conditional-on RH (cor:RH, KEP1(iii), KEP3(b), rem:nonzero, cor:margin2(iii),
prop:uniform, thm:Al(c), §11.1 chain, rem:RHcert, prob:B, concluding remarks, cor:Li/app:li); Paper 42
dependence (all citations; lem:firstcontact now uses thm:log5A, giving T_* > ½log5); cor:KEP08 (superseded);
thm:W; thm:P3/cor:AP/rem:P3exp/cor:CP; prop:M; §6.4 two-prime windows; rem:normline; rem:loc; prop:finuniv;
cor:zeros; cor:bprof; prop:NC, cor:P3, rem:P4, thm:J, cor:H1, Birman–Schwinger paragraph, rem:PF2;
prop:decide, §11.2 scales, rem:margin; rem:regimes, cor:Qp, rem:resweights, lem:degen, rem:twohalves,
prop:band/align/negtrace; def:Al, lem:Alband, rem:excess, rem:Cheb; all of §14 (log 2 direction: prop:schur,
thm:w11, thm:nest, prop:bprime, prop:shifts, lem:N, prop:G, rem:galerkin); §16 except thm:inertia-nogo
(Sonin split, B2 [its content folded into prop:coer-prime], inertia-finite, quartets, rank, exclusions);
§17 semilocal Sonin (CONDITIONAL); thm:coer-A and its lemmas, coer-K1, coer-sector, rem:coer-A/B/size/nogo/labels;
rem:completecontact, rem:Sren, rem:returnremarks; lem:bern; app:diag (replaced by short App. B);
unused bibliography entries.

## Defect fixes
- First-contact bridge: stated as proved (lem:contA) in abstract/intro/§12; obsolete "open" claims removed.
- lem:mbounds and new lem:compact proved before use (contT, contA, thm:O, first contact); lem:contA moved to §2.
- Truncated sentence in cor:convfail(ii) completed ("[θ*,1] with 0.8148<θ*<1"); θ*<1 now from thm:log5W, not Zhu.
- Notation: one shift V_a (old τ_a → V_{-a}, S_ℓ → V_ℓ); one reflection J (old R); polar matrix D_pol;
  archimedean form 𝔪_T (old Γ_T/Γ); λ_A(T) single notation (macro); block half-length r (old τ);
  rows Y_k (old W_k); w·cosh is Ω (old W); test kernel ϑ (old φ); intervals 𝓘_0; Gamma map 𝒪 (old R);
  𝓛_F (old K_F); S'_N (old K_N); Σ_L (old S_L); pr_T (old Π); K-operator 𝖪; leakage ε_lp; m_lo named;
  truncation height H (old Γ); smoothness order p in thm:latedge.
- thm:AL renamed thm:latedge "the edge cost of lattice sampling"; "corrected statement"/"working notes" text removed.
- Numerical references: λ_A(½log3)=9.448e-4 (thm:C margin now "9.4%"), λ_A(log2)=9.83e-8, λ_A(½log5)=3.10e-12,
  all labelled numerical; "log 2 bottom not known" removed.
- Imports from Paper 45: only Thm 8.4 (Thm 11.3 no longer needed).
- W^0_ε paragraph isolated as a remark marked as not used.
- thm:Zexh proof typo D(0.3)→d_*(0.3).

## Not done / caveats
Length is 57 pp. of body, above the 40–45 pp. target; further cuts would remove proved results
(KEP subsection, finite-zero-set theorems, thm:Np, cor:SC1 discussion are the candidates).

## Adversarial review
Checks run: every \ref resolves (zero undefined after two passes); no forward use of a lemma/theorem inside a
proof except as noted below; no references to removed results; no forbidden vocabulary, memo IDs or
logbook phrasing; numerical values 9.448e-4, 9.83e-8, 3.10e-12 labelled numerical, certified bounds
(8.8577e-5, 2.5e-12, 3.0e-10) unchanged; statements of thm:C, thm:latedge, lem:firstcontact, thm:log5A,
cor:convfail compared with main.tex (hypotheses kept; firstcontact proof valid with thm:log5A in place of Paper 42).

Issues and fixes:
1. Notation residue: proof of cor:convfail (i),(ii) still used the old archimedean form Γ_T (3 occurrences,
   undefined in the short version). Replaced by 𝔪_T (\mT), consistent with §1.6 and §7.
2. App. B false comparison: "3.62e-10 (odd) ... below the value 3.10e-12 above, as it must be" — 3.62e-10 is
   not below 3.10e-12. Rewritten: both midpoint values labelled numerical; certified bounds of thm:log5A lie
   below them; the smaller one (2.53e-12) is consistent with 3.10e-12.
3. Forward reference inside a proof: thm:parityschur (§9) used ‖Π_T‖ ≤ A_T from prop:coer-prime (§11).
   The one-line reason (|c_F(log n)| ≤ ‖F‖²) is now given in place, with a pointer to prop:coer-prime(i).
   (The pointer to cor:margin1 at the end of the proof of thm:margin only names the next corollary; kept.)
Recompiled: 66 pp., zero undefined references, zero errors.
