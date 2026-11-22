# BARRIER_D1_001 — Quantitative Hamburger at ζ: tangent, exact Euler-family defect, symmetric-defect NO-GO (door D1)

No audit yet.
positivity of 𝔞_T on P_T assumed true; this memo builds/tests the tool asked for by BARRIER_001 §6 (D1).

## 0. Corpus check and new reason (routes-tried rule)

Read: BARRIER_001 (Thm 5, §6), Paper 46 `lem:degen`, `prop:shape-eulerdel`; index entries G5G-R162_2601c (Hamburger in the
atomic class, tool, no sign), G4F-R162_2801 (quantitative Hamburger for off-line quartets, zero side, DEAD on Beurling),
G5F-R163_1001c (window Hamburger, pinning, REF-D), R163_1001 Thm O, INV_A_001 (rigidity 𝔐={ζ} = retry), N_009/010
(Φ fixed point, CONDITIONAL Hamburger), INV_L_001 (local FE O_6-stable), INV_P_001/INV_Q_001 (D_{S_N}, band defect), phases
194–197 with AUDIT tags. Grep "Bohr/Kronecker/tangent/stability" in the index: no item computes the *tangent space* of the
conductor-1 FE locus at ζ in comb coordinates, nor the *exact* FE defect along Euler deformations, nor tests it against w_T.
**New reason:** the object is neither the zero set (R162_2801) nor a pinning identity (R163_1001c): it is the sublevel set
{Δ ≤ ε} of a comb-side global-FE defect, of positive dimension, and the question is purely its *shape* relative to the
half-space H_T of BARRIER_001 Thm 5. This was never asked; the answer is a NO-GO for a precisely declared class.

## 1. Setting

Comb a, f_a(s)=exp(Σ_{n≥2} a(n)n^{-s}/log n) = Σ b_n(a) n^{-s}, ξ_a(s)=Γ_ℝ(s)s(s−1)f_a(s). Window coordinates of a and of b
correspond by a triangular polynomial diffeomorphism (b_n depends on a(m), m|… , m≤n), so window statements may be made in
either. From lem:degen (PROVED in P46): for every a, λ_A(T;a) ≤ λ_A(T;Λ) − ⟨π_N(a−Λ), w_T⟩.
An **FE-defect atom** is S_ε={a : Δ(a) ≤ ε}, Δ ≥ 0, Δ(Λ)=0, Δ built from ξ_a(s) − ξ_a(1−s).

## 2. First order: the tangent space is {0} (PROVED, from CITED Hamburger)

**Prop 1.** Let H = {Dirichlet series D over ℕ, finite order, meromorphic with at most a simple pole at s=1, with
Γ_ℝ(s)D(s)=Γ_ℝ(1−s)D(1−s)}. Then H = ℂζ (Hamburger 1921, CITED). H is a *linear* space. Hence the exact FE locus in
b-coordinates is the line ℂ·(1,1,1,…), and with b_1=1 the single point b=1, i.e. a=Λ. Its tangent at Λ (any smooth curve
a(t) in the locus) is 0 in every coordinate n≥2, and its pairing with w_T is 0.
*Proof.* A tangent vector at ζ is a Dirichlet series k=∂_t f_{a(t)}|_0 ∈ H (H linear), so k=cζ; b_1≡1 forces c=0. ∎
Consequence: the signed question cannot be first order on the exact locus; it lives in the defect, at second order.

## 3. Exact defect on the Euler family (PROVED)

Family E_N: f_α(s)=∏_{p<N}(1−α_p p^{-s})^{-1}∏_{p≥N}(1−p^{-s})^{-1}, α_p real, |α_p|<√p; a_α(p^k)=α_p^k log p.
Put R=f_α/ζ=∏_{p<N}(1−p^{-s})/(1−α_p p^{-s}); ξ_α=ξ·R, so FE ⟺ R(s)=R(1−s) ⟺ R(½+it)∈ℝ ∀t (real coefficients).
Defect: Δ(α) := M_t |Im R(½+it)|² (Bohr mean).

**Theorem 2 (exact defect).** Δ(α) = ½( ∏_{p<N} [1 + (α_p−1)²/(p−α_p²)] − 1 ).
*Proof.* Im R = (R−R̄)/2i, so |Im R|²=½(|R|²−Re R²). By Kronecker (log p independent) the Bohr mean of a product of
functions of distinct x_p=p^{-½-it} is the product of torus means. M R² = ∏ (constant term of a power series in x_p with
constant term 1) = 1. (1−x)/(1−αx)=1+(α−1)Σ_{k≥1}α^{k−1}x^k, so M|·|²=1+(α−1)²Σ_k α^{2k−2}p^{−k}=1+(α−1)²/(p−α²). ∎
Second order, t_p=α_p−1: Δ = Σ_{p<N} t_p²/(2(p−1)) + O(|t|³), positive definite (consistent with Prop 1); the cubic
correction t_p³/(p−1)² (Δ grows faster for t_p>0) is the only asymmetry. Tail primes p≥N enter as further independent
factors: the Schur complement over the tail is trivial (no tail compensation). On falsifiers: a_P (α_p=0, p<P):
Δ=½(∏_{p<P}(1+1/p)−1) ≍ ½(log P·e^γ… −1), bounded away from 0 — separated (PROVED). cΛ: not in E_N; its Γ_ℝ-defect
grows with |t| (Stirling phase (c−1)·t log t), infinite Bohr mean — separated (ARGUED). Beurling generic / Ξ_Q: outside
the ℕ-Euler family; ARGUED separated (no FE with Γ_ℝ, conductor 1 over ℕ by Hamburger).

**Corollary 3 (local signed rigidity fails at second order, PROVED).** With W_p := log p Σ_{k≥1, p^k<N} k w_T(p^k):
sup_{S_ε∩E_N} ⟨a−Λ,w_T⟩ = √(2ε Σ_{p<N}(p−1)W_p²)·(1+O(√ε)). Hence S_ε∩E_N ⊆ H_T iff (to leading order)
ε ≤ λ_A(T;Λ)² / (2Σ_{p<N}(p−1)W_p²), and then, by lem:degen, a uniform method on this premise decides T only if
λ_A(T;Λ) ≥ √(2εΣ(p−1)W_p²) > 0: **a strict strengthening of WP_T(Λ) (REF-D⁺)**. The premise supplies no sign; it is an
ellipsoid, symmetric in ±t to leading order. (Degenerate case W≡0 is lem:degen's degenerate case, not known to occur.)

## 4. General NO-GO: symmetric (analytic) defects (PROVED)

**Theorem 4.** Let Δ ≥ 0 on a finite-dimensional deformation family {Λ+u(t)}, t∈ℝ^d, u real-analytic, u(0)=0, Δ∘u
real-analytic, vanishing only at t=0 (Hamburger, Prop 1, makes this automatic for FE defects that vanish exactly on the FE
locus). If some direction t* has ⟨Du(0)t*, w_T⟩>0, then for small ε, π_N S_ε contains a curve Λ+u(st*), |s|≤c ε^{1/2m}
(2m = even vanishing order of s↦Δ(u(st*))), and every uniform method with premise S_ε deciding T implies
λ_A(T;Λ) ≥ c ε^{1/2m}⟨Du(0)t*,w_T⟩(1+o(1)) > 0.
*Proof.* s↦Δ(u(st*)) is analytic, ≥0, not ≡0, so its leading term is c₀s^{2m}, c₀>0: both signs of s are admitted at the
same scale. lem:degen + uniform soundness (BARRIER_001 Thm 5 argument). ∎
**Class declared (𝒦_FE^an):** premises {Δ≤ε} with Δ analytic (or C^{2m} with non-degenerate leading form) along some
w-positive analytic curve. NO-GO for D1: they are "w-blind at leading order"; deciding with them is REF-D⁺. Unsigned
quantitative Hamburger (coefficients within δ(ε) of Λ on the window) is the same: a δ-ball needs λ_A(T;Λ) ≥ δ‖w_T‖_*.

## 5. What survives (OPEN, specification sharpened)

An escaping D1 atom must have **one-sided** behaviour at Λ: along w-positive directions Δ grows at order strictly lower
than along w-negative ones (e.g. Δ(Λ+su) ≥ c s for s>0, = o(s) for s<0). Locally such a premise is a cone condition
C ⊆ {⟨u,w_T⟩ ≤ 0} for every T≥0.60 simultaneously — i.e. it must encode the sign of the minimizer's autocorrelation pairing,
which no FE-defect norm (analytic in coefficients) does; non-smooth (positive-part/sup) defects are, at first order,
cone/certificate premises (A2 / dual certificate, BARRIER_001 Thm 3 (ii)). Remaining honest options: (i) non-analytic
FE-defect functionals whose non-smoothness at ζ is *not* a sup of linear forms (none known); (ii) door D2 (non-uniform Ψ),
not touched here. Clause check of the studied object: non-pinning ✓ (positive-dimensional ellipsoid), non-linear ✓,
non-cone ✓, but **place-wise ✗ on E_N** (Thm 2: the global-FE Bohr defect factorizes over primes by Kronecker) and
w-blind ✗ (Thm 4). Row D: OPEN. No sign obtained.

## 6. Labels
Prop 1: PROVED given Hamburger (CITED). Thm 2: PROVED. Cor 3: PROVED (leading order; constant explicit). Thm 4: PROVED
(elementary, from lem:degen). Separation of cΛ, Beurling, Ξ_Q: ARGUED. §5: OPEN specification. Not numerically checked.

## 7. Reframing after AUDIT_197_HOSTILE (points 1–4)

(1) Separation of a_P needs no FE (a(2)=log 2 already separates on the window): accepted; (D1.a) of BARRIER_001 is mis-stated.
Nothing above uses that claim; Thm 2 merely records that the FE defect *also* separates a_P.
(2) The global FE is not a functional of π_N a: accepted. Here Δ is always a functional of the **full** series (all primes,
tail p≥N included), and the window premise is the projection π_N S_ε = {π_N a : ∃ tail, Δ(a) ≤ ε}, i.e. the reduced defect
Δ_red(π_N a) = inf_tail Δ. What the FE constrains on the window via off-window coefficients is, on E_N extended by arbitrary
tail parameters α_p (p≥N): Δ = ½(∏_{all p}(1+(α_p−1)²/(p−α_p²)) − 1), every factor ≥1, so inf_tail is attained at α_p=1
(p≥N) and Δ_red = Δ restricted to p<N (PROVED): **off-window Euler coefficients cannot relieve any window FE defect**; the
window constraint is exactly the ellipsoid of Cor 3. (Outside Euler families tail compensation is OPEN.)
(3) The signed statement as rigidity among Euler products ≠ ζ: Cor 3 / Thm 4 settle it negatively at leading order in the
analytic-defect class (NO-GO), so the near-retry flag is moot for this class.
(4) Non-unique F⋆: Cor 3 and Thm 4 hold for *every* real unit minimizer (lem:degen holds for each); the obstruction needs only
one with W ≠ 0. If all minimizers have w_T=0 (lem:degen degenerate case, unknown), Thm 4 is vacuous at that T: CONDITIONAL on
w_T ≠ 0, as the audit says.
