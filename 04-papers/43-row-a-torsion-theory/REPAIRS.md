# Paper 43: repairs of 

Source audit: adversarial audit AUDIT_43, defects D1–D16.
Backups: `main_pre_repair.tex`, `main_pre_repair.pdf`.
Numbering below is the **tex numbering** of the repaired `main.tex` (63 pages,
two pdflatex passes, no undefined references, no overfull boxes). Where it
changed, the old number is given in brackets.

## Defects and changes

| # | Change |
|---|---|
| D1 | Def. 6.5 now defines W_∞ on **all** of D_A through two profiles b_±(t)=F(j_∞(±e^t)) and two kernels K_s, K_c (eq. (37)). Convention 6.6 states the convention, proves absolute convergence, gives the even-part reduction (38) (the old formula) and the identity (39) W_∞(F)=∫_{R^×}F(j_∞x)τ_∞(x)dx/2|x| for F vanishing near 1. Thm 7.2(b): the parity formula (56) is now *derived* from (37), the regularized integral ∫' is defined explicitly, and the odd closed form (57) is proved by the reflection formula of ψ. b(1)/b(0) inconsistency removed (everything is b_+(0)=F(1)). |
| D2 | New Lemma 5.6 (block lemma, proved): rapid orthogonal sums of unital blocks; the subcomplex of words with an unmatched edge is contracted by inserting the unit at the first unmatched edge. Lemma 5.7 (non-unit twist) reproved with it: blocks χ_pE_p and shells j<0, then Thm 5.2 on A_*=functions on Z_p twisted by a **unital endomorphism** (σ′ or ρ), then the block lemma on shells. No excision used. The old Lemma 5.4 (orthsum) is **deleted**: its homotopy does not satisfy bs+sb=id on mixed words (counterexample a_0⊗a_1⊗a_2, a_0,a_1∈A_1, a_2∈A_2). Thm 5.2 now allows unital endomorphisms with σ(I)⊆I (proof unchanged). |
| D3 | Thm 5.4 [5.3] Step 3 rewritten: support grading of C(⊗E_v^+) (faces preserve the union of supports), induction on |S| with T=I^+⊗J^+, ideals K=I⊗J ⊂ I⊕K ⊂ T (genuine ideals), two applications of excision, vanishing of HH(Q′)^{(12)}. Statement weakened to an isomorphism in homology induced by a zigzag of continuous quasi-isomorphisms, with Tot⊗̂ of complexes. |
| D4 | Lemma 5.8 [5.6] restated for all units u≠1 via H_u = closure of ⟨u⟩: reduced HH_0 = H_u-invariants; dim = (p−1)p^{k−1} on 1+q_pZ_p (q_p=p odd, q_2=4); 2^{k′−1} for p=2, u∈3+4Z_2, u≠−1, k′=v_2(1+u); ∞ for u=−1. New (ii): for u of infinite order the image (1−σ)F^{(j)} is **not closed** (conductor weights are polynomial in the exponent, |1−κ(u)|≍p^{−(m−k)}), so only the reduced HH_0 is computed; the old "closed and complemented" claim was false. Remark 5.10 [5.8] gives the p=2 counterexamples u=3, u=−1. Prop 6.13 [6.12] rewritten as a comparison (a)–(c), including where it fails; the old "Haar-regularized rank per unit of test mass" and the trace formula derived from it are removed. |
| D5 | New Thm 5.3: excision CITED for σ=id (Wodzicki 1989 Thm 3.1, algebraic; Brodzki–Lykova 2001, Fréchet with continuous linear section). The twisted form is **not** in these sources and is recorded as hypothesis (Exc_σ), eq. (25). Consequences marked: Thm 5.4 CONDITIONAL on (Exc_σ); Thm 5.12(b) [5.10(b)] CONDITIONAL; Cor 5.14 [5.12] global part CONDITIONAL; Thm 5.12(a),(c), Lemmas 5.6–5.8 unconditional. Remark 5.5. Intro updated. |
| D6 | Abstract, intro and Thm 13.7(e): "realizes Weil's decomposition" replaced by: a pair, not a sum; first component is the full I_A(F,G), not a primitive pairing; the analogy is formal. |
| D7 | Thm 13.4: "no scalar determinant built from T̂_S can extend…; forced" replaced by the statement proved for L_S only. Same in §9 and Remark 13.8. |
| D8 | Lemma 8.12, eq. (76): |T̂(c,τ)| ≤ A_c + B_S log(2+|τ|), A_c = A_S + Σ c(κ_p) log p depends on the component; uniform on finite sets of components only; sup_c A_c = ∞. Uses in Thm 8.13(b) and Thm 15.1 adjusted. |
| D9 | Thm 15.1(a),(b): explicit Gram estimate (116) with three regions; sequential choice of windows (mass η_k of earlier functions in the new window) and tails ε_k; explicit constants ε_k=η_k=K_0 2^{−4k−12}; dominance bound |G_jk| ≤ 2^{−j−k−2}. |
| D10 | Mertens theorem moved to **Appendix A** (Thm A.1 [15.2]), "Auxiliary: … not part of the construction"; status paragraph; abstract/intro/Convention 6.11 updated. |
| D11 | New Remark 11.5: T is not compatible with restriction R_{S′S}; only inflation-with-correction (eq. chartcomp) and exact invariance of T_∞ hold. |
| D12 | New Remark 3.6: G is semisimple (C_S-graded vector spaces), formal properties of little depth. |
| D13 | Def 4.2: v=λU_γ: E_a→E_b (a=γb) has v† := λ̄U_γ : E_{b^{-1}}→E_{a^{-1}}; proof of Thm 4.3 adjusted. |
| D14 | Thm 14.1: theta characteristic assumed defined over k after a finite extension; stated as an assumption. |
| D15 | Thm 8.11: completeness/nuclearity of D_A′ cited (Schaefer IV.6.1, III.7.4, IV.9.6; Trèves 50.6). Thm 10.2: Fatou replaced by convergence in the two complete weighted L¹ spaces; injectivity A_tr→L¹ proved. |
| D16 | README status rewritten (tex numbering). Cross-paper drift (P44 "globally", P46 main.md numbering, P45 Haar vol(Z_p^×)=log p) listed below; not edited here. |

## Exported objects (final statements, tex numbering)

**Carrier.** S finite, ∞∈S, S_f≠∅; A_S=R×∏_{p∈S_f}Q_p; Γ_S positive S-units;
C_S=Γ_S\A_S^× ≅ R^×∏Z_p^× via φ(x)=∏p^{v_p(x_p)} (Lemma 2.2), |x|_S=|x_∞|.
Haar: each Z_p^× mass 1, d*x_∞=dx/(2|x|) (eq. archmeasure). Note: vol(Z_p^×)=1;
the factor log p is the *shell volume in W_p*, not a Haar normalization of C_S.
**Test algebra** D_A=C_c^∞(C_S), convolution, F†(u)=conj F(u^{-1}) (Def 2.4).
**Densities** τ_v(x)=|x|_v^{1/2}/|1−x|_v; τ_∞(±e^t)=1/(2|sinh(t/2)|), 1/(2cosh(t/2)).

**Trace (Def 6.5).** T(F)=Σ_{v∈S}W_v(F)+cF(1); c=0 where a normalization is needed.
- W_p(F)=∫_{v_p(x)≠0}a τ_p d*x + (log p)∫_{Z_p^×}(a(u)−a(1))|1−u|_p^{-1}du, a=F∘j_p, each shell of volume log p, du probability Haar.
- **W_∞ convention (Def 6.5 + Convention 6.6), verbatim content:** with b_±(t):=F(j_∞(±e^t)), K_s(t)=1/(4 sinh(t/2)), K_c(t)=1/(4 cosh(t/2)), K=K_s+K_c=e^{−t/2}/(1−e^{−2t}),
  W_∞(F) = (γ+log 4π) b_+(0) + ∫_0^∞ [K_s(t)(b_+(t)+b_+(−t)) − 2K(t) b_+(0) e^{−t/2}] dt + ∫_0^∞ K_c(t)(b_−(t)+b_−(−t)) dt,
  for **every** F∈D_A, no parity assumption. Equivalently W_∞(F)=∫'_{R^×}F(j_∞x)τ_∞(x)dx/(2|x|), regularized only at x=+1; for F vanishing near 1 it is the absolutely convergent integral (39). For F even under j_∞(−1) it reduces to the old formula (38).
- **Symbol (Thm 7.2).** For χ=(ε,τ;(κ_q)):
  Ŵ_∞(0,τ)=log π − Re ψ(1/4+iτ/2);  Ŵ_∞(1,τ)=log π − Re ψ(3/4+iτ/2)=Ŵ_∞(0,τ) − π/cosh(πτ);
  general: Ŵ_∞(ε,τ)=½∫'_R e^{iτt}dt/(2|sinh(t/2)|) + (−1)^ε ½∫_R e^{iτt}dt/(2cosh(t/2)), with ½∫_R e^{iτt}/(2cosh(t/2))dt=π/(2cosh πτ).
  Ŵ_p = 2(log p)Re(ζ_p/(1−ζ_p)) if κ_p=1 (ζ_p=p^{−1/2}·conj η_p), = −c(κ_p) log p if κ_p≠1.
  T̂=Ŵ_∞+ΣŴ_p real-analytic, bounded above, → −∞ on each component; Plancherel T(H)=∫Ĥ(T̂+c)dχ.
  Growth (Lemma 8.12, eq. 76): |T̂(c,τ)| ≤ A_c + B_S log(2+|τ|), A_c depends on the conductors — **not uniform over all components**.
- ML / Tate poles (Thm 7.4): on the even principal component, residues ∓i(|S_f|+1) at ±i/2; the odd component has no pole at ±i/2.

**Numerical theory.** I_A(F,G)=T(F⋆G†) (Def 8.1), radical zero (Thm 8.4); Tate λ_∓(F)=∫F|u|_S^{∓1/2}, M=(λ_−,λ_+), B_T=C², β_T=[[0,1],[1,0]] (Thm 7.1); Tate sequence (Thm 8.8); completion N_A^dist (Thm 8.11); rulings (Thm 8.13); signature indefinite, infinite index both signs for c>−m (Thm 15.1); λ_RR=(L_S, λ_per∘(M×M)) (Def 13.3, Thm 13.7), L_S trivial on rulings (Thm 13.4); colimit trace T_∞ (Thm 11.6 [11.5]).

**Shadow (§5).** Lemma 5.7: non-unit twist ⇒ C(E_p,(E_p)_σ)≃C[0] (PROVED). Lemma 5.8: unit twist ⇒ reduced HH_0 infinite-dim (PROVED). Thm 5.4 Künneth, Thm 5.12(b), Cor 5.14 global: CONDITIONAL on (Exc_σ).

**Appendix A (Thm A.1, ex-15.2):** uses Λ(N) and Mertens; auxiliary, not part of the construction.

## Number changes relevant to Papers 44–47
5.3→5.4 (Künneth), 5.5→5.7, 5.6→5.8, 5.8→5.10, 5.9→5.11 (prop:crossed), 5.10→5.12 (shadow), 5.12→5.14 (blind), 6.12→6.13 (prop:haarrank, content changed), 11.5→11.6 (colimtrace), 15.2→A.1 (Mertens). Lemma 5.4 (orthsum) removed. Unchanged: 2.2, 2.4, 6.5, 7.1, 7.2, 7.4, 8.1, 8.4, 8.8, 8.11–8.13, 13.4, 13.7, 14.1, 15.1.

## Alignment items for other papers (not edited here)
- P44: drop "globally" on the log bound (use eq. 76); adopt the W_∞ convention above for odd F; Thm 5.10→5.12, Prop 6.12→6.13 (now a comparison, not a derivation).
- P45: Thm 15.2→A.1, now explicitly outside the construction; Haar vol(Z_p^×)=1 (log p is the shell volume); prop:trace odd component per the convention above.
- P46: cites main.md numbering ("Theorem 14.1" signature = tex Thm 15.1; "(10.10)" = eq:weilformula (107); "9.14a" = Thm 8.13).

## Second pass: (Exc_σ) proved

Adversarial check of `EXC_SIGMA.md`, line by line: pattern decomposition A=L⊕I;
Step 1 filtration q=n−m+1 (first L at m) — head faces preserve q, d_{m−1}, tail faces and the
twisted face lower q or land in C(I,I_σ); graded piece B′(I)⊗̂Y with b′ on the head, contracted
by h⊗id (right linearity gives (id⊗μ)(h⊗id)=hμ; degree 1: μh=id). Step 2 filtration r=m−1
(first I at m) — head faces and d_{m−1} lower r or land in C(A,I_σ); tail faces and the L-part of
the twisted face preserve r; graded piece ≅ (−1)^m · I⊗̂_A Bar(X), X=L^{⊗(r+1)} with action
π_L(σ(b)·), a module since σ(b)π_I(·)∈I, I·X=0 since σ(I)⊆I; H_{≥1} vanishes by the retract
ΨΦ=μh⊗id through I⊗̂Bar (Φ chain map = right linearity), H_0 by ∂_1(h⊗id)=id. All maps are
finite composites of multiplications, σ, π_L, π_I, h, unit insertions: continuous. Filtrations
start at 0 and are finite per degree. No gap found; no counterexample.
Caveat closed: for E_V the partition of Lemma 3.7 at the places of V only satisfies (summable)
(product of one-place geometric estimates, no lattice weights); h(a)=Σe_i⊗ρ_i a has μh=id,
and h(ab)=h(a)b for b in the ambient unital algebra T or Q′ by associativity + continuity.

Changes in main.tex (backup `main_pre_excsigma.tex`): Thm 5.3 now has (a) cited
(σ=id) and (b) twisted form PROVED, with proof and an unnumbered paragraph verifying the
hypotheses in Step 3; eq. (25) is the conclusion of (b), not a hypothesis. CONDITIONAL removed
from Thm 5.4, Thm 5.12(b), Cor 5.14 (global); Remark 5.5 and intro updated. **Theorem
numbering unchanged** (65 pages, 2 passes, 0 undefined refs, 0 overfull). Papers 44/45 need
no renumbering.

**Shadow status (replaces the line above):** Lemma 5.7, Lemma 5.8, Thm 5.3(b), Thm 5.4,
Thm 5.12, Cor 5.14: PROVED.

## Complete old→new number map (pre-repair → current tex)
§3: 3.6→3.7 (lem:partition), 3.7→3.8 (lem:projective), 3.8→3.9 (lem:idealproduct),
3.9→3.10 (lem:cech), 3.10→3.11 (thm:exctriangle), 3.11→3.12 (lem:excvanish),
3.12→3.13 (thm:excision); 3.6 is the new Remark (D12).
§5: as listed above (5.3→5.4, 5.5→5.7, 5.6→5.8, 5.8→5.10, 5.9→5.11, 5.10→5.12, 5.12→5.14;
orthsum deleted).
§6: 6.6→6.7 (thm:absconv), 6.7→6.8 (thm:unique), 6.8→6.9 (prop:comparison),
6.9→6.10 (rem:diagonal), 6.10→6.11 (conv:c), 6.11→6.12 (thm:separate),
6.12→6.13 (prop:haarrank); 6.6 is the new Convention (W_∞).
§11: 11.5→11.6 (thm:colimtrace). §15: 15.2→A.1 (thm:mertens), 15.3→A.2 (rem:mertensmeaning).
Note: Paper 44 line 286 cites "Thm. 6.7" of 43 together with Conv. 6.6/Thm 11.6, i.e. already
in the new numbering (thm:absconv); check intent if it meant old 6.7 (thm:unique).
