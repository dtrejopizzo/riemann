# Paper 44 — repairs of 

Source: adversarial audit AUDIT_44_45. Backups:
`main_pre_repair.tex/.pdf`. Theorem numbering unchanged (verified
by diffing the `.aux` label tables before/after; new text is unnumbered).

| Id | Location (tex) | Repair | Label |
|---|---|---|---|
| D-B1 | Prop 2.3, eq. (archterm), (b); new unnumbered paragraph after Prop 2.3; Thm 6.3 (frobarch) and proof; Thm 9.1 (gramarch) | Aligned with Paper 43's convention for `W_∞` on all tests (Paper 43 Def 6.5 + Convention `conv:Winf`, in its tex of ): profiles `b_±(t)=F(j_∞(±e^t))`, kernels `K_s=1/(4 sinh(t/2))` on the positive half-line and `K_c=1/(4 cosh(t/2))` on the negative one, regularization at the identity only. Smeared Frobenii live in `x_∞>0`, so their archimedean values carry `K_s`, not `K`. Conclusions used (vanishing for large `N`, no archimedean block) unchanged. | PROVED |
| D-B2 | Thm 9.1 (gramarch) and proof | Written for both orientations: `∫K_s[g(e^t)+g(e^{-t})]`, exactly one term surviving (`n<m` vs `n>m`). | PROVED |
| D-B3 | Thm 9.1 hypothesis `ε_0(A,S)`, proof | `ε_0` taken over the points `q^{-k}` for **all** primes (T = T_∞ samples primes outside `S_f`); existence noted; proof covers the colimit prime terms. | PROVED |
| D-B4 | Cor 9.3 (FFdagger), (diagvalue), proof | Restated and proved directly: `F⋆F† = V_N(n) G` with `G = 1[x_∞>0] ψ(log x_∞) ∏ 1_{U_r}`, `ψ(0)=‖h‖²`; `I_A(F,F) = V_N(n)‖h‖²[−Σ(log r)((r−2)/(r−1)+N−1) − log(1/ε) + O(1+ε²‖ψ″‖/‖h‖²)]`, error `O_η(1)` for rescaled profiles. The earlier formula (no `‖h‖²`, unit-height even idempotent) is withdrawn. Rem 9.4's use (no limit, negative divergences) survives. | PROVED |
| D-B5 | Lem 6.2 | Weak-* convergence requires `h ≥ 0`, `∫h d*x_∞ = 1`; stated. | PROVED |
| D-B6 | Thm 9.7(iii) | Level set meets `Im j_∞` in two points `j_∞(±1/n)`. | PROVED |
| D-B7 | Thm 9.11 proof; abstract, intro | Sign typo `ζ_p = p^{-1/2+iτ}` fixed; "explicit primitive class" → "explicit up to one sufficiently large parameter". | — |
| README | README.md | Rewritten: current unconditional label, tex numbering, md-only material (transfer theorem 8bis.7, `(H_L)`, ledgers) flagged as absent from tex; removed phrases outside the author's rule. | — |

Not changed: the prior-version subsection placement of Cor 9.5 (cosmetic).
Compiled twice, 0 errors, 0 undefined references.

## Alignment with repaired Paper 43

Checked against Paper 43 `main.tex` as repaired  (label tables of the
pre-repair and repaired `.aux` diffed; the number map in 43's REPAIRS file is
incomplete: §6 also shifts, 6.6→6.7, 6.7→6.8, …, 6.10→6.11, 6.12→6.13).

| Location (44) | Old citation | New citation / change |
|---|---|---|
| Prop 2.3 (`prop:trace`) header | §§6, 11 | Def 6.5, Conv 6.6, Thm 6.7, §11, Thm 11.6 |
| Prop 2.3, after (archterm) | "Def 6.5 and the convention following it" | Def 6.5 and Convention 6.6. Formula verified verbatim: `(γ+log4π)b_+(0)+∫_0^∞[K_s(b_+(t)+b_+(−t))−2K b_+(0)e^{−t/2}]+∫_0^∞K_c(b_−(t)+b_−(−t))`, `K_s=1/(4sinh(t/2))`, `K_c=1/(4cosh(t/2))`, `K=e^{−t/2}/(1−e^{−2t})`; off-identity form = 43 eq. (39)/Thm 6.7. |
| Prop 2.4 (`prop:tate`) | "\|T̂\| ≤ A_S+B_S log(2+\|τ\|) globally" | Per component, `A_c=A_S+Σc(κ_p)log p` (43 Lemma 8.12, eq. (76)); not uniform over all components. Symbol (eq:symbol), ζ_p, max Ŵ_∞(0,·)=log π−ψ(1/4) verified against 43 Thm 7.2. |
| Prop 2.5 (`prop:completion`) | — | Adds `A_B:=max A_c` over the d_{N_B} components met by B. Uses at the proofs of Thm 4.x (η(R), two places) and the constant `C_B` now use `A_B`; every such integrand is supported on those components, so the proofs are unchanged in substance. |
| Prop 2.6 (`prop:shadow`) | Thm 5.10, Prop 6.12; "T is the Haar-regularized Lefschetz number of a categorical shadow" | Lemma 5.7, Thm 5.12(c), Prop 6.13(a). Restated as the **local** statement C(E_p,(E_p)_x)≃C[0] for v_p(x)≠0, plus τ_p and shell volume log p; the Lefschetz-number claim is removed (43 now says the trace is not derived from the shadow; 6.13 is a comparison). |
| Thm 9.1 proof | Thm 11.4 | Thm 11.6(b) (eq. Tinf: prime terms of T_∞ at ℓ∉S_f sample δ_S(ℓ^{−k})). |
| Unchanged, verified | Lemma 2.2, Def 2.4, Thms 7.1, 7.2, 7.4, 8.4, 8.11, 8.14 | same numbers and content. |

**Dependency on (Exc_σ).** None. The only results of 43 that 44 imports from
§5 are the local computations Lemma 5.7 / Thm 5.12(c) (non-unit twist ⇒ C[0]),
which 43 proves without excision. 44 never uses the Künneth Theorem 5.4,
Thm 5.12(b), or the global part of Cor 5.14 (identification of the local
complexes as tensor factors of Sh(E_w)). The uses of Prop 2.6 (Rem 7.x
`rem:complexshadow`, Thm `carrierside`(i), the degree-identification theorem,
the remark before §8) need only the local rank-one statement; the impossibility
statements rest on Prop `noZp`, which is pure category theory. The integral
shadow Sh_Z of §8 is an independent ℤ-linear construction. Labels unchanged.

Recompiled: pdflatex ×2, 0 errors, 0 undefined references.
