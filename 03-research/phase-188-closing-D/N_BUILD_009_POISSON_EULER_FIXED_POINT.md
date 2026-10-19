# N_BUILD_009 — A new object: the Poisson–Euler map Φ on prime-power combs, whose unique nonnegative fixed point is Λ

Rule: after 008, invent an object, give axioms, prove basic properties, test against the input map L2_BUILD_011.

## Corpus check
- R162_903 Thm 3.2 (terminating BCH: log Z = M_T(Λ/log) exactly) — **this overlaps N_BUILD_005 §1** (recorded; 005's
  𝔄_T formulation is the measure-algebra version of R162_903's compressed operator algebra 𝒜_T). R162_903 Prop 6.1, Thm
  4.2, 5.1: nonlinear uses of Λ*1 = log alone collapse (valid for any unipotent coefficient system).
- R164_102 Prop I (Hamburger 1921, CITED): integer-supported Dirichlet series with FE + Γ_ℝ + simple pole is cζ.
- phase 170 / R184_002: Euler–Maclaurin port, identities without sign (W12).
- L2_BUILD_011 §2: survivors must couple Euler over ℕ × FE (q = 1) × ℤ-integrality, non-linearly; L2_BUILD_012 §3:
  the three meet in log(M + B).
grep "fixed point|punto fijo|Φ(Λ)|self-dual|autodual|Poisson.*Euler|cosine transform" (whole corpus): no map whose
fixed point is Λ built from Poisson and the Euler logarithm. New: the map Φ, its axioms, uniqueness, falsifier table.

## 1. The object
Let 𝔐⁺ be the cone of measures λ = Σ_{n≥2} a(n)δ_{log n} on (0,∞) with a ≥ 0, supported on log of prime powers,
a(n) ≤ C log n (so all formal series below converge for Re s > 1 in Laplace variable). For λ ∈ 𝔐⁺ put
 Z[λ] := exp_*(λ_{/log}) (convolution exponential of Σ a(n)/log n · δ_{log n}; an Euler product with nonnegative
 coefficients, exact in every 𝔄_T), Z[λ] = Σ_n z_λ(n)δ_{log n}.
Let 𝒞 be the Poisson involution on measures on (0,∞)_x: for an even-extended test f, ⟨ν, f⟩ ↦ ⟨ν, 𝒞f⟩, 𝒞f(k) := 2∫₀^∞ f(x)
cos(2πkx)dx (cosine transform, unitary, 𝒞² = I), transported to u = log x with the weight x^{−½} (s = ½ normalization).
**Definition (Poisson–Euler map).** Φ(λ) := −∂_s log( M + 𝒞^*(Z[λ] − M) )|_{s=½} in 𝔄_∞, where M = δ₀ + e^{u/2}du is the
pole/main measure of N_BUILD_007 §0, whenever M + 𝒞^*(Z[λ] − M) is a unipotent element (δ₀ + atom-free part).
**Axioms of a Poisson–Euler comb (PE):** (E) λ ∈ 𝔐⁺ (Euler, positivity, prime-power support, ℕ-integral positions);
(P) Z[λ] − M = 𝒞^*(Z[λ] − M) (Poisson self-duality of the integer comb with conductor 1); equivalently λ = Φ(λ).

## 2. Basic properties
**Prop 1 (Λ is a fixed point; PROVED from classical Poisson).** Z[Λ] = Σ_{n≥1} δ_{log n} (Euler product), and Poisson
summation Σ_{n≥1} f(n) − ∫₀^∞ f − ½f(0) = Σ_{k≥1} 𝒞f(k) − ½𝒞f(0)·0… for even Schwartz f (the δ₀/½ conventions are absorbed
in M as in N_BUILD_007 §0) gives (P). Hence Φ(Λ) = Λ. ∎
**Prop 2 (uniqueness; CITED + PROVED).** If λ satisfies (PE) then λ = Λ. *Proof.* (E) makes Σ z_λ(n)n^{−s} an integer-
supported Dirichlet series with positive coefficients, z_λ(1) = 1; (P) is, after Mellin transform, the functional equation
with Γ_ℝ and a simple pole at s = 1 (Riemann's second proof read backwards: the Mellin symbol of 𝒞 is π^{½−s}Γ(s/2)/Γ((1−s)/2));
Hamburger (CITED) gives Σ z_λ(n)n^{−s} = ζ(s) (normalization z(1) = 1), so z_λ ≡ 1 and λ = Λ by Möbius inversion over ℕ. ∎
**Prop 3 (the axioms are independent; PROVED).** (P) without (E): Epstein-type and periodic Gauss-sum combs violate
(E) (signs/non-prime-power support of their log) — and an integer comb z(n) satisfying (P) need not have an Euler
logarithm in 𝔐⁺. (E) without (P): every a_P, every finite Euler product, every Z^{α} (α ≠ 1) satisfies (E) and not (P)
(their coefficients are not ≡ 1, Prop 2).
**Prop 4 (non-linearity; PROVED).** Φ is not affine on 𝔐⁺: Φ(αΛ) for α ≠ 1 is defined (Z[αΛ] = Z^{α}) and
Φ(αΛ) ≠ αΛ + (1−α)Φ(0) in general (Φ(0) = −∂_s log M + …); the map passes through exp and log.

## 3. Test against the input map (L2_BUILD_011)
| falsifier | (E) | (P) | fixed point of Φ? |
|---|---|---|---|
| a_P = Λ1_{p≥P} (row 8) | yes | no (coefficients 0 at P-smooth n > 1) | no |
| Epstein / DH (row 10) | no (log has signs / non-prime-power support) | lattice Poisson with 𝒞_Q ≠ 𝒞 | no |
| Beurling DMV (rows 4, 9) | positions not log n | no (1-dim Poisson needs ℤ) | no |
| M_m, f_t (row 13), Λ̃ (row 14) | violates prime-power/positivity pattern or (P) | no | no |
| W-tail Λ1_{n<n₀}; (1±ε)Λ | (E) yes | no (Prop 2) | no |
| b_θ, Λχ₂ (row 15) | (E) fails or conductor ≠ 1 | no | no |
Odlyzko–te Riele: the object asserts no bound on Möbius sums; compatible.
So (PE) is a survivor in the sense of L2_011 §2(b): it uses Euler over ℕ × FE(q = 1) × ℤ jointly, and non-linearly (Φ).
By Prop 2 it identifies Λ — as it must (L2_011 §2(c), I5); its value is the structure (fixed point of an explicit map),
not the class.

## 4. What it gives for the window form (PROVED reduction + OPEN core)
WP_T is a statement about λ|_{[0,2T)} paired with c_F. The fixed-point equation is global (𝒞 mixes all scales), but by
non-stationary phase (N_BUILD_006 §1: modes decay like (2πk)^{−r} with constants uniform in T for C^r tests) the dual side
of (P) seen by a window test is a rapidly convergent sum over k. Define the **window defect of a comb λ**
 δ_T(λ; F) := 𝔞_T^{(λ)}(F)  (the window form built with λ),
and the fixed-point residual r(λ) := λ − Φ(λ). Question (Ω_Φ), OPEN: is there a functional inequality
 min_{F ∈ P_T, ‖F‖=1} δ_T(λ; F) ≥ −𝒦_T(r(λ))  for λ ∈ 𝔐⁺, with 𝒦_T(0) = 0 and 𝒦_T ≥ 0,
i.e. "window negativity is controlled by the failure of Poisson–Euler self-duality"? At λ = Λ this is WP_T. All
falsifiers have r(λ) ≠ 0, which is consistent (they may be negative). (Ω_Φ) is a stability statement for the fixed point,
the first statement in this program that is not a variant of a tool in the record.
First test (pen and paper, next memo): linearize Φ at Λ, compute DΦ(Λ) on perturbations supported on one prime power
(the amplification falsifier Λ + c1_{n=2}): r(Λ + cδ_{log2}) = c(δ_{log2} − DΦ(Λ)δ_{log2}) + O(c²), and compare its size with
c_*(T,2) of thm:finmod(ii). If ‖r‖ is of order c while the window form drops below 0 only at c > c_*(T,2) > 0, (Ω_Φ) is
consistent at first order on that falsifier.

## Self-review
1. Prop 1: Poisson for f(x) = x^{−½}g(log x) with g compactly supported in (0, ∞) needs f Schwartz-like on (0,∞) and even
extension smooth at 0: f vanishes near 0, fine; at ∞ compact support. Correct for C_c^∞ tests; the identity Z − M = 𝒞^*(Z−M)
is meant in this weak sense. The ½-conventions: with M = δ₀ + e^{u/2}du the n = 1 atom sits in M; Poisson's ½f(0) is at x = 0
(u = −∞), irrelevant for tests vanishing near x = 0. OK.
2. Prop 2: Hamburger requires finite order/growth conditions on G(s)ζ_λ(s); (E) with a(n) ≤ C log n gives absolute convergence
for Re s > 1 and (P) gives meromorphic continuation with the Γ factor; Hamburger's hypotheses (G entire of finite order, CITED)
are not all checked here → Prop 2 is CONDITIONAL on the growth hypothesis of Hamburger's theorem for the continuation
provided by (P). Downgrade to CONDITIONAL (classical; very likely routine).
3. Φ's domain: M + 𝒞^*(Z[λ] − M) unipotent — for λ near Λ it is Z[Λ] itself; elsewhere not guaranteed. Domain stated.
4. Prop 4 is weak (non-affinity), honest.
5. The window question (Ω_Φ) is a new formulation; it is not shown non-vacuous. If 𝒦_T is allowed arbitrary, (Ω_Φ) is
trivially true (take 𝒦_T = ∞ off Λ) — the content must be a quantitative 𝒦_T (e.g. a norm of r(λ) restricted to scales
≤ 2T). Stated as the next test.
No sign contact; no negative value certified.
