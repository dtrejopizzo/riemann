# Paper 45 — repairs of 

Source: adversarial audit AUDIT_44_45. Backups:
`main_pre_repair.tex/.pdf`. Theorem numbering unchanged (aux label
tables diffed; added text unnumbered).

| Id | Location (tex) | Repair |
|---|---|---|
| D-C1 | Prop 2.1 | Haar measure of `C_S` = `d*x_∞ ⊗` probability Haar of each `Z_p^×` (Paper 43 Lemma 2.2); `vol(Z_p^×) = log p` is the normalization of the **local** measure on the slice `Q_p^×`. Now consistent with the later use (Cor 9.4). |
| D-C2 | Prop 2.2 (`W_p`) | Shell term integrates against the probability measure `du`; `log p` appears once. |
| D-B1 alignment | Prop 2.2 (`W_∞`) | Displayed `W_∞` stated as the form for sign-even tests; general tests per Paper 43 (Def 6.5 + convention: `K_s` on the positive, `K_c` on the negative half-line). All tests to which `W_∞` is applied are radial, hence sign-even: no result affected. |
| D-C3 | Appendix (E3b) | Dangling citation fragment removed. |
| D-C4 | Remark 3.3 | Over-citation fixed: Paper 44 Thms 4.2, 4.7, 6.11 cover radial and Frobenius classes; shell measures are singular measures acting as functionals, no separate completion theorem claimed. |
| C.2 | new unnumbered paragraph after Prop 2.6 | States that clause C.2 is met only in reinterpreted form (`M` into `(B_T, β_T)`, polar packet `β_T(M,M)`; no Meyer-type realization). |
| README | README.md | Rewritten: label as recorded in PLAN.md, tex numbering, md-only material (`B_nuc`, ledgers, 9.6′) flagged; removed phrases outside the author's rule. |

No theorem statement or proof changed. Compiled twice, 0 errors, 0 undefined
references.

## Alignment with repaired Paper 43

Checked against Paper 43 `main.tex` as repaired  (pre/post `.aux`
label tables diffed).

| Location (45) | Old citation | New citation |
|---|---|---|
| Prop 2.2 (`prop:trace`) | Def 6.5 and Convention 6.10 | Def 6.5, Conventions 6.6 (W_∞ on all tests) and 6.11 (constant c) |
| Prop 2.2, general-F sentence | "the convention following it" | Convention 6.6; K_s on x_∞>0, K_c on x_∞<0, K=K_s+K_c, verified verbatim; displayed even form = 43 eq. (38) with b(0)=b_+(0)=F(1). |
| Prop 2.3 (`prop:offidentity`) | Thm 6.6 | Thm 6.7 (absolute convergence off the identity) |
| Prop 2.4 (`prop:symbol`) | Thms 7.2, 15.1(c) | Thms 7.2(c),(d), 15.1(c); symbol formulas (Ŵ_p=2 log p Re ζ_p/(1−ζ_p), Ŵ_∞(0,τ)=log π−Re ψ(1/4+iτ/2)) and bound ≈5.3722 verified. |
| Prop 2.8 (`prop:colimit`) | Thm 11.5 | Thm 11.6 |
| Prop 2.9 (`prop:indefinite`) | Thm 15.1 | Thm 15.1(b),(d) |
| Rem `mertens-scope`, fact (E8) | Thm 15.2 | Thm A.1 (appendix of 43, auxiliary, outside its construction); 45 already stated no main theorem depends on it. |
| Unchanged, verified | Lemma 2.2, Def 2.4, Lemma 6.2(i), Prop 8.2, Thms 7.1, 8.4, 8.8, 8.9(a), 8.11, 8.13, 8.15, Def 8.16, Thm 8.17 | same numbers and content. Haar: vol(Z_p^×)=1 on C_S, log p = shell volume in W_p — consistent with 43. |

**Dependency on (Exc_σ).** None. 45 cites nothing from §5 of 43 (no shadow,
Künneth, excision or blindness statement); its inputs are the trace, symbol,
Tate functionals, rulings, colimit trace and signature (§§2, 6–8, 11, 15),
none of which uses (Exc_σ) — 43 marks only Thm 5.4, Thm 5.12(b) and the global
part of Cor 5.14 conditional, and Prop 6.13 / Cor 5.14 are consumed only by
remarks inside 43. The radial classes imported from 44 (Def 3.11 etc.) do not
depend on (Exc_σ) either (see 44's alignment section). Paper 47 (main.tex,
main_short.tex) cites neither 43 nor 44; it cites 45 Thms 8.4 and 11.3 only,
hence is free of (Exc_σ) transitively. Labels unchanged.

Recompiled: pdflatex ×2, 0 errors, 0 undefined references.
