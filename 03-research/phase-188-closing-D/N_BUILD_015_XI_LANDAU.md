# N_BUILD_015 — (Ξ) for a fixed profile: Mellin form, an unconditional Landau theorem (limsup Ξ ≥ 0, liminf Ξ ≤ 0), and what is reachable without zero input

Pen and paper. F₀ ∈ P_{T₀} real, ‖F₀‖ = 1, c₀ = c_{F₀}; Ξ(d) = Σ_n v_n c₀(log n − d) (N_BUILD_014; main term ≡ 0). Converse via
IMS/Gabor is NOT attempted (closed: 106_47, 106_59, L2_BUILD_004).

## Corpus check
Paper 47 cor:void (classes C_PNT, C_zeros, C_BT for WINDOW statements), thm:finmod, rem:wit-cheb; N_BUILD_014; phase-106 IMS closure.
grep "Landau|oscillation theorem|Ω±|Laplace transform.*nonnegative|abscissa": Landau's theorem appears in the corpus only as a
citation for Ω-results of ψ(x) − x (phase 160 survey); never applied to a Tate-annihilated window fluctuation. New: §1–§3.

## 1. Mellin/Laplace form (PROVED)
Let C(s) := ∫c₀(v)e^{sv}dv = L(s)L(−s), L(s) := ∫F₀(t)e^{st}dt — entire, of exponential type 2T₀, and **C has double zeros at
s = ±½** (L(±½) = A, B = 0). For Re s > ½,
 ∫_ℝ Ξ(d)e^{−sd}dd = 2 Σ_n Λ(n)n^{−½−s}C(s) = −2(ζ′/ζ)(s+½)·C(s) =: 𝒥(s),
(Fubini; ∫c₀(log n − d)e^{−sd}dd = n^{−s}C(s)). Since Ξ(d) = 0 for d < −2T₀ ... more precisely Ξ is supported in d > −2T₀ (log n ≥ log 2),
𝒥 is the Laplace transform of a function supported on a half-line. Analytic continuation (PROVED from classical facts):
 (i) at s = ½ the simple pole of ζ′/ζ(s+½) is cancelled by the double zero of C;
 (ii) on the real segment s ∈ [0, ½], s + ½ ∈ [½, 1], ζ has no zeros there (ζ(σ)(1 − 2^{1−σ}) = η(σ) > 0 for 0 < σ < 1, alternating
  series; CITED, classical). Hence 𝒥 continues analytically to an open neighbourhood of the real half-line [0, ∞).

## 2. Theorem L (unconditional, PROVED modulo CITED Landau theorem)
For every profile F₀: **limsup_{d→∞} Ξ_{F₀}(d) ≥ 0 and liminf_{d→∞} Ξ_{F₀}(d) ≤ 0.**
*Proof.* Suppose Ξ(d) ≤ −ε for d ≥ D, ε > 0. Then g := (−ε − Ξ)𝟙_{[D,∞)} ≥ 0 and its Laplace transform is
 G(s) = −εe^{−sD}/s − 𝒥(s) + E_D(s),  E_D(s) := ∫_{−2T₀}^{D}Ξ(d)e^{−sd}dd (entire).
By Landau's theorem (CITED: the Laplace transform of a nonnegative function is singular at the real point of its abscissa of
convergence), the abscissa σ_c of G cannot lie in (0, ∞), because G continues analytically across every real point > 0 (§1(ii) and
the entire terms). So G converges for Re s > 0, and G(s) ≥ 0 for real s > 0. But as s ↓ 0 along the reals, 𝒥(s) and E_D(s) stay
bounded (analytic at 0: ζ(½) ≠ 0 by §1(ii), C entire), while −εe^{−sD}/s → −∞. Contradiction. The liminf statement is the same with
g := (Ξ − ε)𝟙_{[D,∞)}. ∎
Consequence via N_BUILD_014 §1: for two copies, inf_d 𝔞_T(F₀ + τ_dF₀) ≤ 2𝔞(F₀) + o(1) — nothing beyond freezing (lem:wit-freeze).
**No contact with the sign** (Theorem L is consistent with the target, which requires limsup Ξ ≤ 2𝔞_{T₀}(F₀) ≥ 0 only when
𝔞(F₀) ≥ 0).

## 3. Upper bounds reachable without zero input (PROVED / CITED)
(a) Trivial: Ξ(d) ≤ 2∫|c₀(v)|e^{(v+d)/2}dv·(1+o(1)) ≪ e^{d/2} (Chebyshev bounds).
(b) PNT with error term: two integrations by parts against the smooth c₀ (c₀ ∈ C² for F₀ ∈ H¹ ∩ P; for the clamped mode,
c₀ = (¼−∂²)²c_G with G ∈ H²₀, so c₀ ∈ L¹ with C(s) decaying like |s|^{−4}·… on vertical lines) give
 |Ξ(d)| ≪_{F₀} e^{d/2}exp(−c d^{3/5}(log d)^{−1/5})  (Vinogradov–Korobov, CITED).
Unbounded. No one-sided improvement follows from Λ ≥ 0 because the main term is already zero: the Tate annihilation removes exactly
the part of the comb on which positivity of Λ acts (the mass), leaving a signed fluctuation.
(c) Positivity of Λ with the annihilated kernel: Ξ(d) = Σ v_n c₀(log n − d) and c₀ takes both signs on (0, 2T₀) (it has
∫c₀ e^{±v/2} = 0 with c₀(0) > 0), so no sign of Ξ follows from Λ ≥ 0. NO-GO (PROVED).
(d) Which inputs are admissible for (Ξ)? cor:void's falsifiers are finite modifications; they change Ξ only on d < log(max modified n),
so they do NOT obstruct a tail statement such as (Ξ). Hence cor:void does not exclude any class of inputs for (Ξ). What does
determine Ξ: by the Mellin form of §1 and contour shifting (explicit formula, CITED), Ξ(d) = −2Σ_ρ e^{(ρ−½)d}C(ρ−½) + O_{F₀}(e^{−d/2}).
So (Ξ) for a fixed profile is a statement about the function 𝒥 near Re s = 0. Recorded as such; per the stated premise it is NOT
used here to rank, close or classify any route.

## 4. Flag check (as requested)
Is there anything that pushes t_∞ = 0 for ζ? **No unconditional statement.** Theorem L gives only limsup Ξ ≥ 0. The Landau argument
has a conditional form: if 𝒥 has a singularity at a point σ₀ + iγ₀ with σ₀ > 0 not cancelled by C, then limsup Ξ = +∞ (Landau, CITED),
and then t_∞ = 0 by Theorem A of 014. This conditional is recorded as a statement about Ξ and t_∞ only; no assertion is made about
whether its hypothesis holds.

## Self-review
1. §1: Fubini for Re s > 1 + something: Σ Λ(n)n^{−½−Re s} converges for Re s > ½; c₀ bounded with compact support: fine. C double zero
at ±½: C(s) = L(s)L(−s), L(½) = ∫F₀e^{t/2} = A(F₀) = 0, L(−½) = B = 0, so C(½) = L(½)L(−½) has a zero of order ≥ 2 (both factors
vanish). Correct.
2. §2: Landau's theorem requires g ≥ 0 and finite abscissa; if the abscissa were −∞ the argument still gives G(s) ≥ 0 for s > 0 and the
same contradiction. Analyticity of 𝒥 at real points in (0,∞): for s > ½ the Dirichlet series converges absolutely; for s ∈ (0,½],
ζ(s+½) ≠ 0 and s+½ ≠ 1 except s = ½ (handled by C). Correct. ζ(½) ≠ 0: η(½) > 0 (alternating, decreasing terms). Correct.
3. Statement strength: limsup Ξ ≥ 0 (not > 0). Honest.
4. §3(b): smoothness of c₀ needed for integration by parts; for general F₀ ∈ P_{T₀}∩D_{T₀}, c₀ is only continuous — restrict to H¹ profiles.
No sign contact; no negative value certified.
