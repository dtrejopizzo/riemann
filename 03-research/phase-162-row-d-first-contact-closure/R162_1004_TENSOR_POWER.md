# R162_1004 — The d→∞ tensor-power limit of a first contact

Status: **NO-GO (PROVED)**. No sign is claimed. Pure mathematics; no numerics.

Corpus check (done first). grep "tensor power", "Deligne" in 03-research: phase 149 (additive pencil, Deligne
ingredients (i)–(v), missing (iii) = a-priori poles of the family, (P149)); Paper 46 T5 (Thm 27.3–27.4, no
single-fibre extraction); R151_005 T6; R157_002 row 22 (Deligne route over Z: EXCL); R160_S5 B8; R162_903 Thm 5.1
(tensor lift). None of these treats the **d→∞ limit of the first-contact vector itself** (q(F^{⊗d}) = q(F)^d
with d-th roots), nor Kazhdan/de Finetti/CLT on N^{⊗d}. This file closes that gap negatively.

Notation: H_T ≥ 0 on P_T for T ≤ T_*, H_{T_*}F = 0, N = ker H_{T_*}; 𝐇^{(d)}_T = Σ_i I⊗…⊗H_T⊗…⊗I on P_T^{⊗d}
(R162_903 Thm 5.1).

## 1. Correcting the set-up: ζ^d does not change the window and its weights are dΛ, not τ_d

**Prop 1.1 (log-linearity; PROVED).** The Weil form is built from −L'/L, not from the Dirichlet coefficients of L.
For L = ζ^d: −(ζ^d)'/ζ^d = d·(−ζ'/ζ), weights dΛ; the zeros are those of ζ with multiplicity d; Γ-factor Γ_ℝ^d. Hence
W_{ζ^d,T} = d·W_{ζ,T} on the same test space and the same window T. The d-fold convolution τ_d = 1^{*d} enters only
the coefficients of ζ^d, and is removed by the logarithmic derivative (log ζ^d = d log ζ).
*Proof.* Explicit formula is linear in log L. ∎

Consequences. (a) A first contact of ζ at T_* gives a first contact of ζ^d at **T_*, not d·T_***. (b) The
single-variable ζ^d form carries no information beyond ζ. (c) A window d·T_* arises only by the dilation
F(x) ↦ F(x^{1/d}), which is not a tensor operation (§3).

**Prop 1.2 (tensor spectrum; PROVED).** spec 𝐇^{(d)}_T = {λ_{i_1}+…+λ_{i_d}}; min spec = d·λ_0(T). For T < T_*,
𝐇^{(d)} ≥ dλ_0 > 0; at T_*, ker 𝐇^{(d)} = N^{⊗d}; for T > T_* (if RH fails) min = dλ_0 < 0.
*Proof.* Tensor sums of commuting self-adjoint operators on the product spectral decomposition. ∎

## 2. Multiplicative functionals: the tensor-power trick is idempotent on this algebra

**Thm 2.1 (base determination; PROVED).** Let q be a functional on the algebra 𝔄^{(d)} of Thm 5.1 with
q(F^{⊗d}) = q(F)^d, e.g. q_φ(F) = ⟨F, φ(H_T)F⟩/‖F‖² with φ Borel, since
⟨F^{⊗d}, φ(H_T)^{⊗d}F^{⊗d}⟩ = ⟨F,φ(H_T)F⟩^d. Then:
(i) a bound |q(F^{⊗d})| ≤ C d^k for all d is equivalent to |q(F)| ≤ 1 (d-th root, d→∞);
(ii) at a first contact with φ(0) = 1 (e.g. φ = e^{−tH}): q_φ(F) = 1 **exactly**;
(iii) any bound on the tensor side proved inside 𝔄^{(d)} (coordinatewise identities, B1 coordinatewise, Thm 3.2's
log Z^{⊗} = Σ log Z_i) is the d-th power of the same bound on the base.
*Proof.* (i) standard. (ii) H_{T_*}F = 0. (iii) the algebra is generated coordinatewise (Thm 5.1 proof); a statement
about q(F^{⊗d}) is a statement about q(F)^d. ∎

**Reading.** The tensor-power trick converts polynomial bounds into the *non-strict* inequality |q| ≤ 1. A first
contact saturates exactly that inequality (q = 1). The trick can never contradict a first contact at T_*; at most it
could rule out λ_0(T) < 0 for T > T_* (q = ⟨F,e^{−tH_T}F⟩ > 1 there), which is RH on the window range itself, and
by (iii) it needs as input a base bound of the same strength.

**Prop 2.2 (Kazhdan / de Finetti / CLT; PROVED, weight-blind).**
(a) Kazhdan-type gap: gap(𝐇^{(d)}) = gap(H_T) = λ_0(T) for every d (Prop 1.2); uniform-in-d property T is the
base gap, zero at T_*.
(b) de Finetti: on the symmetric sector Sym^d P_T, exchangeable states are, as d→∞, mixtures of product states
ρ^{⊗d}; the energy per copy (1/d)⟨𝐇^{(d)}⟩ → ∫ tr(ρH_T) dμ(ρ) ≥ λ_0. The infimum is attained on products: no new
constraint.
(c) CLT: under the product state ω^{⊗d}, (𝐇^{(d)} − d⟨H⟩_ω)/√d → N(0, Var_ω H). The Gaussian limit sees only
mean and variance of the base; at F ∈ N both are 0 (degenerate Gaussian δ_0). No sign.
*Proof.* (a) Prop 1.2; (b) quantum de Finetti (Størmer/Hudson–Moody) plus linearity of the tensor sum; (c) classical
CLT for commuting sum of i.i.d. copies. ∎

## 3. The genuine multiplicative structure of zeros is dilation, and its tensor-power bound is RH

The only operation with x^ρ ↦ (x^ρ)^d is dilation X ↦ X^d: x^{dρ} = (x^d)^ρ. For one zero, |X^{d(ρ−1/2)}| ≤ C d^k
for all d forces Re ρ ≤ 1/2 — Deligne's "|a|^d ≤ C ⇒ |a| ≤ 1".

**Thm 3.1 (dilation tensor-power = RH; PROVED, E1).** The statement "for a fixed smooth test g and all d,
|Σ_ρ ĝ_d(ρ) X^{d(ρ−1/2)}| ≤ C_g d^k" (explicit formula at scale X^d, normalized by X^{d/2}) is equivalent to
ψ_g(Y) = Y ĝ(0) + O(Y^{1/2}(log Y)^k), hence to RH. Unconditional inputs (zero-free region, Vinogradov–Korobov)
give Y·exp(−c(log Y)^{3/5}(loglog Y)^{−1/5}), whose d-th root at Y = X^d is X^{1/2}·X^{1/2}: trivial.
*Proof.* Substitute Y = X^d; the d-th root of the de la Vallée Poussin bound tends to X. ∎

**Prop 3.2 (why Deligne gains and Z does not; PROVED as a structural statement).** Deligne's trick gains because the
d-th power object (Sym^d / tensor power sheaf) carries an **a priori bound independent of the base**: its trace is
bounded by dim H^*(Sym^d) · q^{dw/2} with polynomial dim H^*, from cohomology (Grothendieck–Lefschetz). Over Z:
(a) Sym^d of the trivial GL_1 datum is trivial; the Satake parameters of ζ at p equal 1, so Ramanujan is empty and
RH is not a Ramanujan statement for GL_1; (b) the tensor object ζ^d (or ⊗ in d variables) has no a priori bound
beyond d·(base) (Prop 1.1, Thm 2.1(iii)); (c) the a-priori count of the tensor family is exactly ingredient (iii)
of phase 149, missing ((P149)), and single-fibre extraction is excluded by Paper 46 T5 (Thm 27.3).

## 4. Falsifiers

| model | Euler product (multiplicativity) | Prop 1.1–1.2, Thm 2.1, Prop 2.2 | Thm 3.1 dilation | has first contacts |
|---|---|---|---|---|
| DH | no | hold verbatim (form defined from any weights; first contacts lift) | identity holds formally, bound false | yes |
| deletion Λ1_{n≥5}, κ-models | yes/partly | lift unchanged (R162_903 §5) | bound status = that of the model | yes |
| Λχ₂ (ζ archimedean data) | yes | hold | bound false | yes |
| Beurling DMV | **yes** | hold | bound false (zeros → Re s = 1) | yes |

DH fails the multiplicativity line as expected, but Beurling and Λχ₂ have Euler products and satisfy every line of
§§1–3. Hence "multiplicativity from the Euler product + polynomial-in-d bound" cannot close: the bound would have to
use integer structure (killing Beurling) and the character 1 (killing Λχ₂), and by Thm 2.1(iii) it must already be a
base bound of RH strength.
**F1.** λ > 0 eigenvectors lift to eigenvalue dλ with q_φ < 1; all identities hold unchanged. The only λ = 0 input is
q = 1, saturation of the non-strict inequality. Not passed.
**F2.** q_φ and 𝐇^{(d)} are even in F and in A_M. Not passed.
**F3/F4.** Weight-blind (Prop 2.2) / no linear limit used. Not a mechanism.

## 5. Verdict

NO-GO (PROVED). Labels: Prop 1.1, Prop 1.2, Thm 2.1, Prop 2.2, Thm 3.1, Prop 3.2 PROVED.
(1) ζ^d has the same window T_* and weights dΛ (log-linearity); the task's "window d·T_*" occurs only under dilation.
(2) On the tensor algebra of Thm 5.1 the tensor-power trick is idempotent: it outputs |q| ≤ 1, which a first contact
saturates (q = 1); no contradiction is possible at T_*.
(3) Kazhdan gap, de Finetti, CLT all reduce to base λ_0 and are weight-blind.
(4) The genuinely multiplicative structure (dilation x^{dρ}) turns the tensor-power trick into RH itself (E1); the
unconditional input is dlVP-level and its d-th root is trivial (killer M/dlVP cap, as phase 151).
(5) The Deligne gain requires an a priori bound on the d-th object independent of the base; over Z that is (P149)(iii)
/ T5. Beurling and Λχ₂ pass every line.

Add to R162_590 §1c: "tensor-power / d→∞ limit, Kazhdan, de Finetti, CLT, dilation Deligne trick — R162_1004 —
log-linearity (ζ^d same window, weights dΛ), idempotence (q=1 saturates |q|≤1), dilation bound ⟺ RH; Beurling,
Λχ₂ pass — F1, F2, Φ, E1, (P149)".
