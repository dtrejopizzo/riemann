# SPEC_SIGN_OBJECT_005 — Round 11: discontinuous output, ring/class defect, multiplicative theta with Poisson

Phase 200 ("sign object"), round-11 synthesizer. Pure mathematics; no new numerics (the only numbers
cited come from LEMMA_E_EPSTEIN_001 and COSH_DEFECT_001, already certified or labeled there).


## Summary (≤300 words)

The thesis of the round (positivity = discontinuous property of the comb, concentrated at isolated points) is formalized in the
family Z_τ. **(A)** δ_ring(τ) = [Λ_τΛ_τ : Λ_τ] ∈ ℕ ∪ {∞} is defined and it is proved (elementary, PROVED) that it equals a(τ) — the
leading coefficient of the primitive form of τ — if τ is quadratic and ∞ otherwise; then 𝔖(τ) := h(D_τ) − 1 (∞ if τ is not
quadratic) is the invariant that truly governs the family: the ring condition (a=1) is necessary but not sufficient. The **exact
decomposition** is given (PROVED/CITED Hecke): Z_Q = (w/h)Σ_χ χ̄(C)L_K(s,χ), Λ_Q = Λ_K + Λ_def with
Λ_def(n) = log n·Σ_k (−1)^{k+1}k^{−1}E^{*k}(n), E = Σ_{χ≠1}χ̄(C)L_χ/ζ_K, identically zero ⟺ 𝔖 = 0. **(B)** Lemma H
(PROVED): the window form is 0-homogeneous in the theta coefficients (r ↦ cr does not change it), so **there does not exist**
an exact identity 𝔞_T(g) = quadratic form (nor non-constant homogeneous polynomial) in θ. Normalizing r(1)=1, 𝔞_T is a
polynomial of unbounded degree in r; its order-2 truncation is exactly the multiplicative Hankel matrix 𝒬_g of COSH_DEFECT
(without sign, NO-GO already recorded). Bochner/complete monotonicity of θ only uses r ≥ 0: comb-generic. **(C)** Decisive test
a_P: its theta ϑ_P = Σ_{d|P}μ(d)ϑ(d²t) passes multiplicativity and has a clean 1/√t term, but **loses the
constant term** (the lattice origin, Σ_{d|P}μ(d)=0) and its Poisson transform is not self-dual (two-term mirror per prime). The
correct discriminant is "index set = additive subgroup (lattice) ∧ multiplicative norm count" = ring h=1.
**But it is a classifier, not an engine of sign**: positivity of 𝔞^{ζ_K} (h=1) remains OPEN and every writing in theta falls into
already-indexed routes (V2, symbol rigidity, Maass–Selberg, G1). New restriction **C-hom**. **(D)** Ranking: 𝔖 as selector (calibration) > first
exact lemma (Λ_def at order 2 = 𝒬_g, consistency check) > theta-Bochner (NO-GO). L′♯ OPEN; row D OPEN.

---

## 0. Corpus and index (mandatory)

Searches (grep on `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` for theta, Poisson, multiplicative, Hecke, Rankin,
Bochner, class) and reading of README, META_200_BARRIER_001, SPEC_004 (Prop 2.1, M200′), LEMMA_E_EPSTEIN_001,
COSH_DEFECT_001 (C-θ), Q2_DEGREE2_001 (Prop 4.1, C-τ), LEMMA_I3_001, LEDGER_L5. Index entries touching this round:

| Index entry | What it closes | Relation to this round |
|---|---|---|
| Phase 193 front N, **V2** | "Tate/lattice Poisson exists but Epstein shares it and it is lost in the log derivative" | Part (B) is exactly this. New reason: here the multiplicativity of r is added as a second ingredient and a *quadratic* kernel in θ is asked for. Result: Lemma H explains *why* it is lost (0-homogeneity) and turns it into an exact impossibility. |
| Phase 193 front N, **V3 / Thm 5** | everything constructible holds for Epstein x²+5y² | The candidate 𝔖 does **not** hold for x²+5y² (𝔖=1): it is not "constructible" in the sense of Thm 5, because it is not a bound but a classification invariant. But it also produces no sign (§4). |
| **EI_003, symbol rigidity** (PROVED) | no exact identity with FE, Euler, Mellin, Poisson is non-linear in Λ | The polynomial expansion of §3 is non-linear in r but **linear in Λ**; in the Euler case it collapses to Λ. Compatible; it does not escape rigidity. |
| Phase 193 front A | multiplicativity of Hecke in σ_T (comb-generic, PROVED); Maass–Selberg = window form of ζ(2s) on the squares | The "window form over θ_ℤ" is this same writing. Not retried. |
| **G1** (PROVED) | the free monoid ℕ^× does not distinguish ζ from Beurling nor from ideal monoids | 𝔖 also uses the additive subgroup (lattice) ⇒ it escapes G1 by construction; see §5.2. |
| Front H, (S⁺) Erdős; semiring principle | the sign must come from (+,·) | (a) δ_ring = closure of an additive lattice under · : genuine (+,·) interaction. Stated in §1.3. |
| COSH_DEFECT_001 (C-θ, 𝒬_g without sign) | definite sign of the cosh defect | §2 generalizes the cosh defect to arbitrary h; no sign is claimed. |
| Q2_DEGREE2_001 (C-τ, Prop 4.1) | continuous bounds in τ | 𝔖 is discontinuous: it respects C-τ by design. |

New reason explicitly stated: the round does not repeat V2 or front A as a *sign construction*; it uses them as a
filter and produces (i) an integer classification invariant whose zero set exactly equals the set where C-τ
allows positivity, (ii) an exact decomposition of the comb by class characters for arbitrary h, (iii) a new
impossibility (Lemma H) that closes the "quadratic form in θ" variant before it is built.

---

## 1. Task A — Ring defect and class defect

### 1.1 Notation

For τ ∈ ℍ, Λ_τ = ℤ + ℤτ, Q_τ(m,n) = |m + nτ|²/Im τ (normalized covolume), Z_τ(s) = Σ'_{(m,n)} Q_τ(m,n)^{−s} with the
fixed Γ factor of Q2_DEGREE2_001. Z_τ depends only on the class of τ modulo SL₂(ℤ). The window form 𝔞_T^{(τ)} is that of
LEMMA_E_EPSTEIN_001 §1.3 with comb v_n = 2Λ_τ(n)/√n, where −Z_τ′/Z_τ = Σ Λ_τ(n) n^{−s} (generalized Dirichlet series if Q_τ
does not take integer values after rescaling).

### 1.2 δ_ring

**Definition.** δ_ring(τ) := [Λ_τΛ_τ : Λ_τ] if the ℤ-module Λ_τΛ_τ = ⟨1, τ, τ²⟩ is a lattice (rank 2), and ∞ if not.

**Proposition A.1 (PROVED, elementary).**
(i) δ_ring(τ) < ∞ ⟺ τ is imaginary quadratic.
(ii) If τ is a root of the primitive form aX² + bX + c (a > 0, gcd(a,b,c)=1, D = b² − 4ac < 0), then δ_ring(τ) = a.
(iii) Λ_τ is a ring ⟺ δ_ring(τ) = 1 ⟺ a = 1; in that case Λ_τ = 𝒪_D = ℤ[τ], the order of discriminant D.

*Proof.* (i) ⟨1,τ,τ²⟩ has rank 2 over ℤ ⟺ τ² ∈ ℚ + ℚτ ⟺ the degree of τ is ≤ 2; τ ∈ ℍ excludes degree 1.
(ii) τ² = −(bτ + c)/a, so ΛΛ = Λ + ℤ·(bτ+c)/a. The class of (bτ+c)/a in (Λ⊗ℚ)/Λ has order a/gcd(a,b,c) = a,
and the quotient ΛΛ/Λ is cyclic generated by it; index = a. (iii) immediate from (ii); Λ_τ = ℤ[τ] when a = 1 and its
discriminant is D. ∎

δ_ring is **not** a class invariant: τ and −1/τ give a and c. The invariant version is min_{γ∈SL₂(ℤ)} δ_ring(γτ) =
minimum of Q on primitive vectors (scaled to integers) — it equals 1 ⟺ Q ~ the principal form ⟺ [Λ_τ] is the trivial class of
Cl(D) (CITED, Gauss/Dirichlet). So, for each discriminant with h(D) > 1 there is τ with δ_ring = 1 (the principal form) whose Z
is **not** an Euler product. Therefore:

**Corollary A.2 (PROVED given the CITED facts).** The condition (a) "the lattice is a ring" is necessary but not sufficient for
Z_τ to be an Euler product. The invariant that decides is the class invariant.

### 1.3 δ_cl and the invariant 𝔖

**Definition.** 𝔖(τ) := h(D_τ) − 1 if τ is quadratic (D_τ the discriminant of its primitive form), 𝔖(τ) := ∞ if not.

**Proposition A.3 (CITED: Hecke; Heegner–Baker–Stark).**
(i) 𝔖 takes values in ℕ ∪ {∞}, is SL₂(ℤ)-invariant and discontinuous at every point: {𝔖 = ∞} is dense, and {𝔖 ≥ 1} is dense
(Heilbronn, already used in Q2 Prop 6.1).
(ii) Z_τ is (w/h times) an Euler product ⟺ 𝔖(τ) = 0 ⟺ τ is SL₂(ℤ)-equivalent to one of the 13 Heegner points
of the orders with h = 1 (D ∈ {−3,−4,−7,−8,−11,−12,−16,−19,−27,−28,−43,−67,−163}).
(iii) {𝔖 = 0} coincides with the set that contains S_∞ (positive ∀T) according to Q2 Prop 4.1 (CONDITIONAL there, 4.2).

*Comment on (ii), the ⇐ and ⇒ directions.* ⇐: with h = 1 every ideal is principal, the lattice points modulo units are
in bijection with the ideals and Z_τ = w·ζ_{𝒪}(s) (for non-maximal orders with h = 1 one must use the order zeta function; the
13 discriminants include the four non-fundamental ones −12,−16,−27,−28, whose order zeta is ζ_K times a Dirichlet
polynomial in the conductor; CITED, with the caveat that the Euler product is over primes coprime to the conductor plus explicit
local factors — noted, not re-derived). ⇒: §2 (E ≢ 0). If τ is not quadratic, 𝔖 = ∞ and the non-Eulerianity
is that of Q2 Prop 4.1(e) (ARGUED there).

**Reading (+,·).** δ_ring measures how much an additive lattice (subgroup of (ℂ,+)) fails to be closed under ·: distributivity of
the semiring applied to Λ. δ_cl measures how much the bijection "lattice points / units ↔ ideals" fails, i.e. how much the
additive count (r_Q(n) = #{λ ∈ Λ : N(λ) = n}) fails to be multiplicative. Both are (+,·) interaction in the sense of the
semiring principle; neither is purely monoid (G1) nor purely additive (generic Poisson). Claim fulfilled.

---

## 2. Task A (cont.) — exact decomposition of the Z_Q form by class characters

Let D < 0 be fundamental (to avoid dealing with orders), K = ℚ(√D), h = h(D), w = |𝒪_K^×|, Q primitive of class C ∈ Cl(K).

**Proposition A.4 (CITED: Hecke; standard derivation).**
Z_Q(s) = w · Σ_{𝔞 ∈ C^{-1}, 𝔞 integral} N𝔞^{−s} = (w/h) Σ_{χ ∈ Ĉl(K)} χ(C) L_K(s,χ)
(the sign of the convention C ↔ C^{−1} does not matter for what follows; χ(C) is fixed by definition). All the L_K(s,χ),
χ ∈ Ĉl, have the same Γ factor (Γ_ℂ(s)) and the same conductor |D|; L_K(s,1) = ζ_K has a simple pole at s = 1, the others
are entire (CITED, Hecke).

**Theorem A.5 (exact decomposition of the comb; PROVED given A.4).** Let
  E_C(s) := Σ_{χ ≠ 1} χ(C) L_K(s,χ) / ζ_K(s) = Σ_{n ≥ 1} e_C(n) n^{−s},
a formal Dirichlet series with e_C(1) = h − 1 in general. Rewrite with the correct normalization: since
Z_Q = (w/h)ζ_K·(1 + E_C) and 1 + E_C has constant term h, set 1 + E_C = h·(1 + Ẽ_C), Ẽ_C(1) = 0. Then
  Λ_Q(n) = Λ_K(n) + Λ_def^{C}(n),   Λ_def^{C}(n) = log n · Σ_{k ≥ 1} ((−1)^{k+1}/k) Ẽ_C^{*k}(n),
where * is Dirichlet convolution; the sum over k is finite for each n (Ẽ^{*k}(n) = 0 if 2^k > n). Consequently, for
every admissible g and every T,
  𝔞_T^{Q}(g) = 𝔞_T^{K}(g) + 𝔇_g^{C},   𝔇_g^{C} = −Σ_n Λ_def^{C}(n) n^{−½} c_g(log n)·(normalization of P46 eq:Aform),
with **the same** archimedean and polar terms on both sides (same Γ, same pole at s=1; the factor w/h and h cancel
because −Z′/Z is scale-invariant: Lemma H below).

*Proof.* log Z_Q = log(w) + log ζ_K + log(1 + Ẽ_C); −d/ds of Σ ℓ(n)n^{−s} is Σ ℓ(n) log n n^{−s}; log(1+Ẽ) =
Σ_k (−1)^{k+1}Ẽ^{*k}/k as a formal series (Ẽ(1)=0). Archimedean and polar terms: the form depends on Z only via −Z′/Z, Γ and the
pole; Z_Q and ζ_K share Γ (A.4) and the simple pole at s=1 (the L_χ, χ≠1, are entire and do not move it). ∎

**Corollary A.6 (PROVED given A.4 + linear independence of the L_K(s,χ), CITED).**
Λ_def^{C} ≡ 0 ⟺ Ẽ_C ≡ 0 ⟺ h = 1 ⟺ 𝔖 = 0. For h > 1, Λ_def^{C} ≢ 0 and its support is not contained in prime powers
(precisely: Λ_Q is not supported on norms of prime ideal powers, while Λ_K is).

**Case h = 2 (consistency with Lemma E).** Ĉl = {1, ψ} (ψ a real genus character). For Q principal, Z_Q = ζ_K + L_ψ
(w/h = 1 for D = −20), Ẽ = ½(L_ψ/ζ_K − 1). The symmetric decomposition of LEMMA_E (Λ_Q = ½(Λ_K+Λ_ψ) + Λ_cosh) and the
anchored one of A.5 (Λ_Q = Λ_K + Λ_def) are two exact writings of the same identity:
Λ_def = ½(Λ_ψ − Λ_K) + Λ_cosh. With the PROVED values of LEMMA_E at the witness (T = 1.59): 𝔞^K = +5.049, 𝔞^ψ = +1.785,
cosh defect −3.479, so 𝔞^Q = 3.417 − 3.479 = −0.062 and **𝔇^{C=1} = 𝔞^Q − 𝔞^K = −5.111** (arithmetically derived from
certified values; not a new certificate). The anchored defect is large and negative at the witness; in the symmetric basis half
of it is the difference of two Euler forms (both positive at the witness) and the other half is the cosh term.

**What A.5 does NOT give (honestly).** 𝔇_g^{C} has no definite sign in g (COSH_DEFECT: 𝒬_g ∈ [−4.02, 4.01] at T=1.6, NUMERICAL;
NO-GO PROVED for the quadratic term). The identity 𝔞^{Q} = 𝔞^{K} + 𝔇 shifts the problem to the positivity of 𝔞^{K},
which is OPEN (it is a statement of the same type as L′♯, in degree 2). The sought theorem **cannot** be "𝔇 ≤ 0".

---

## 3. Task B — the window form as a function of theta

### 3.1 The impossibility of an exact quadratic form in θ

For a lattice (or a comb of coefficients) let r = (r(n))_{n≥1} be the vector of coefficients of the Dirichlet series
Z(s) = Σ r(n) n^{−s} (for Epstein, r = r_Q; for ζ(2s) via θ_ℤ, r(n) = 1_{n=□}); θ(t) = Σ r(n) e^{−πnt} (+ origin
term) and Z is its Mellin transform up to Γ.

**Lemma H (0-homogeneity; PROVED).** For every c > 0, 𝔞_T^{cr}(g) = 𝔞_T^{r}(g). Consequently, if Φ is a function of r
defined on a cone (closed under r ↦ cr) and Φ(r) = 𝔞_T^{r}(g) on that cone, then Φ is 0-homogeneous. No non-zero
quadratic form Φ(r) = Σ_{m,n} K(m,n) r(m)r(n) (nor any homogeneous polynomial of degree ≥ 1, nor any
four-point form in θ) can represent 𝔞_T(g) exactly on a family that contains both r and 2r, unless 𝔞_T(g) = 0 there.

*Proof.* −(cZ)′/(cZ) = −Z′/Z; Γ and the pole do not depend on c. If Φ is homogeneous of degree d ≥ 1: Φ(2r) = 2^d Φ(r) = Φ(r) ⇒ Φ(r)=0. ∎

**Corollary H.1.** The question "does there exist an exact writing of 𝔞_T(g) for ζ as a quadratic form in θ (or
θ−1, or Jacobi) with a Poisson kernel?" has the answer **NO** in its literal form (PROVED). Only the following remain: (α) quotients
(Φ = N(r)/D(r) with N,D homogeneous of the same degree), (β) functions of normalized r (r(1) = 1), (γ) forms in log θ or
in log Z.

### 3.2 The normalized writing: unbounded-degree polynomial

**Proposition H.2 (PROVED).** With r(1) = 1, for each n, Λ_r(n) = log n · ℓ_r(n), where ℓ_r = log(1 + (r − δ₁)) in the
ring of formal Dirichlet series, i.e. ℓ_r(n) = Σ_k ((−1)^{k+1}/k)(r − δ₁)^{*k}(n): a polynomial in
{r(d) : d | n, d > 1} of degree ≤ Ω(n). Then
  𝔞_T^{r}(g) = A_T(g) + P_T(g) − Σ_n w_g(n) Σ_k ((−1)^{k+1}/k) (r − δ₁)^{*k}(n),
with w_g(n) = 2 log n · n^{−½} c_g(log n) (P46 convention) and A_T, P_T the archimedean and polar terms. The k = 1 term is linear in r,
the k = 2 term is the **multiplicative Hankel quadratic form** −½ Σ_{m,n>1} r(m)r(n) w_g(mn), and so on.

*Comment.* This is the only "quadratic form in θ" that exists: the order-2 term of an infinite polynomial expansion. It is literally
the structure 𝒬_g[b] of COSH_DEFECT §8 (there with b = coefficients of
½log(L₂/L₁)). The products r(m)r(n) appear evaluated at mn: **that is the m·n term of the semiring
principle**, and it is already known (PROVED) to have no sign.

**Proposition H.3 (multiplicative collapse; PROVED).** If r is multiplicative (r(mn) = r(m)r(n) for (m,n)=1) then
ℓ_r is supported on prime powers and the whole expansion of H.2 sums to the expression linear in Λ_r supported on
p^k. For r completely determined by a degree-d Euler product, the polynomial relations among the order-≥2
terms are exactly those that annihilate ℓ_r outside prime powers.

*Reading.* Multiplicativity of theta coefficients **does not** produce a new quadratic form: it makes
(by exact cancellation) all non-linear terms outside p^k disappear. What remains is the arithmetic side of the explicit
formula, linear in Λ. It is symbol rigidity (EI_003, PROVED) seen from θ.

### 3.3 Bochner and Poisson

- **Bochner/Bernstein (PROVED, comb-generic).** θ(t) = Σ r(n)e^{−πnt} is completely monotone in t ⟺ r ≥ 0. It is
  "positive-type" positivity of θ as the Laplace transform of a positive measure. It holds for Epstein with
  any h, for Beurling (with θ_B := Σ e^{−π n_j t}) and for cΛ with c>0. It discriminates nothing: NO-GO as a sign object
  (comb-generic filter; already covered by the phase 193 index E, Thm 2: Bochner measure without factorization).
- **Self-dual Poisson (PROVED for lattices).** θ_Λ(1/t) = t·covol⁻¹·θ_{Λ*}(t) (dimension 2) and for Λ_τ normalized
  θ_{Λ*} ~ θ_Λ (binary lattices of covolume 1 are self-dual up to rotation). All Epstein forms share this (V2, index).
- **Poisson + multiplicativity together** (the requested combination). For positive binary lattices: "self-dual Poisson"
  ∧ "r_Λ multiplicative" ⟺ Λ is homothetic to an order with h = 1 (PROVED given A.3/A.4: r_Q multiplicative ⟺ Z_Q
  an Euler product ⟺ 𝔖 = 0). That is, the conjunction that the question identifies as "the object" **is** 𝔖 = 0. It is a
  closed algebraic condition with discontinuous output: it satisfies (i)–(ii) of Task B. It lacks (iii): an inequality.

### 3.4 Is the positivity ∀T of 𝔞^{Euler} a statement about the ring 𝒪_K?

Honest question from the brief. What can be stated:
- By H.3, 𝔞^{ζ_K} is a function of the comb Λ_K, which is determined by the ideal monoid of 𝒪_K and the norms.
  So yes, it is a statement about (𝒪_K, N) — trivially, like everything that depends on Λ_K.
- By G1 (index, PROVED), the ideal monoid of 𝒪_K as a free monoid alone does not distinguish ζ_K from a Beurling system. What the ring
  adds is the **norm** (an additive weight log N𝔭 with values in log ℕ) and the lattice (Poisson). It is the same
  pair (monoid with integer weights, FE) that ζ already has.
- A Rankin–Selberg-type identity Σ r(n)²n^{−s} = L(s, Sym²)·ζ(s)/ζ(2s)·… exists (CITED, classical for CM
  weight-1 forms) and is a *positive* quadratic form in r. But its positivity is that of |r|², holds for any real r, and does
  not enter 𝔞_T: the index (phase 193 front A) closes it as "blind to the comb and to h*". By Lemma H, moreover, it cannot
  equal the window form.
- Conclusion ARGUED: no exact identity was found writing 𝔞^{ζ_K}(g) as a sum of squares over ideals
  or over lattice points without going through one of the three exits of H.1 (quotient, normalization, logarithm), and all three
  return to the form linear in Λ (REF-D if the kernel is the form) or to the term 𝒬_g (without sign).

---

## 4. Task C — the candidate theorem and its tests

### 4.1 Statement

**Candidate Theorem Θ-𝔖 (structure PROVED, sign OPEN).** Let 𝒫 be the class of combs a with FE and fixed Γ of degree 2
(family Z_τ) or degree 1 (ζ). Define 𝔖(a) ∈ ℕ ∪ {∞} by: 𝔖(a) = h − 1 if a = Λ_Q for a binary quadratic lattice of
discriminant D and class number h; 𝔖(a) = 0 for ζ (lattice ℤ ⊂ ℝ, ring, h = 1); 𝔖(a) = ∞ otherwise. Then:
1. (PROVED given A.3–A.5) 𝔖(a) = 0 ⟺ a is the comb of an Euler product with FE in the class (ζ, or ζ_𝒪 with h(𝒪) = 1).
2. (PROVED) 𝔞_T^{a}(g) = 𝔞_T^{Euler(a)}(g) + 𝔇_g(a), with Euler(a) := ζ_K the trivial factor of decomposition
   A.4 and 𝔇_g(a) = −Σ w_g(n)Λ_def(n) ≡ 0 ⟺ 𝔖(a) = 0. 𝔇 has an exact polynomial expansion in Ẽ with order-2 term
   equal to a multiplicative Hankel matrix.
3. (OPEN) 𝔞_T^{a}(g) ≥ 0 ∀T, ∀g ∈ P_T when 𝔖(a) = 0.
4. (CONDITIONAL on Q2 4.2 + DH) 𝔖(a) ≥ 1 ⟹ ∃T: 𝔞_T^{a} ≱ 0. (For x²+5y², PROVED: Lemma E.)

**Is it REF-D?** Points 1, 2, 4 are not REF-D: 𝔖 is an integer defined by the lattice, without looking at the form, and
identity 2 has an explicit kernel (w_g and the class characters), distinct from the form. Point 3 **is** indeed the
form itself restricted to the points 𝔖 = 0: the candidate contributes no sign mechanism. Global label: **PROVED classifier,
sign engine absent (NO-GO as sign object, ARGUED: §3.4).**

### 4.2 Battery tests

| Comb | Self-dual Poisson | Multiplicative count | Indices = subgroup (origin) | 𝔖 | Comment |
|---|---|---|---|---|---|
| ζ (Mori μ=15) | yes (θ_ℤ) | yes (1_□) | yes | 0 | 𝔖 says nothing about the extremal: Mori's certificate lives in 𝔞^{ζ}, which is point 3 (OPEN in general, certified up to ½log15). Test passed without information. |
| x²+5y² (Lemma E) | yes | **no** (r_Q(2)=0, r_Q(3)=0, r_Q(6)=4 ≠ r_Q(2)r_Q(3)) | yes | 1 | Separates. Λ_def ≢ 0 (A.6); 𝔇 = −5.111 at the witness (derived). |
| Generic Epstein τ | yes | no (non-integer) | yes | ∞ | Separates (C-τ). |
| Beurling | **no** | yes (formal) | no (no lattice) | ∞ | Separates by Poisson. |
| a_P | **not self-dual** (§4.3) | yes | **no** (origin missing) | ∞ | Decisive test, §4.3. |
| cΛ, c ∉ ℕ | no lattice theta | d_c(n) ∉ ℕ | no | ∞ | Separates. c = 2: ζ(s)² is not Epstein (Γ_ℝ(s)² ≠ fixed Γ; Q2 §7). |
| ζ_K·L with h=1 in another family | — | — | — | 0 | Within the "positivity allowed" set; same OPEN status as ζ. |

### 4.3 a_P exact (the decisive test)

Let P = ∏_{p∈S} p squarefree, a_P the comb of ζ_P(s) := ζ(s)∏_{p∈S}(1 − p^{−s}) (deletion of Euler factors). In
the variable 2s its theta is ϑ_P(t) := Σ_{n≥1,(n,P)=1} e^{−πn²t}.

**Proposition C.1 (PROVED).**
(i) ϑ_P(t) = Σ_{d|P} μ(d) ϑ(d²t), ϑ = (θ_ℤ − 1)/2.
(ii) Poisson: ϑ_P(t) = (φ(P)/P)·(1/(2√t)) + Σ_{d|P} (μ(d)/(2d√t))·(θ_ℤ(1/(d²t)) − 1). The constant term
  −½Σ_{d|P}μ(d) is **0** for P > 1. That is: ϑ_P has a clean 1/√t term (with mass φ(P)/P) and **no
  constant term**.
(iii) The Mellin transform ∫₀^∞ ϑ_P(t) t^{s} dt/t = π^{−s}Γ(s)ζ(2s)∏_{p|P}(1 − p^{−2s}) has no pole at s = 0
  (the zero of ∏(1−p^{−2s}) cancels that of ζ(0)·Γ(s)… precisely: the residue −½ of the Mellin transform of ϑ at s = 0 is multiplied
  by ∏(1−1) = 0).
(iv) The Poisson dual of ϑ_P is Σ_{d|P} (μ(d)/d) ϑ(t/d²)/√t — a combination of **inverse dilations**, not a
  multiple of ϑ_P. There is no self-dual FE: the quotient of the factors ∏(1−p^{−2s}) / ∏(1−p^{2s−1}) is not of
  Γ·exponential type (it is a quotient of Dirichlet polynomials with zeros on Re s = 0 and Re s = ½ respectively).

*Proof.* (i) inclusion–exclusion. (ii) θ_ℤ(u) = u^{−½}θ_ℤ(1/u) applied to u = d²t; Σ_{d|P}μ(d)/d = φ(P)/P,
Σ_{d|P}μ(d) = 0. (iii) term-by-term Mellin transform of (i). (iv) from (ii). ∎

**Reading.** a_P passes multiplicativity (it is Euler) and has the singular part 1/√t; what it lacks is **the lattice origin**:
the index set {n : (n,P)=1} is not a subgroup of ℤ, the constant term (which in θ_ℤ is the contribution of the
point 0, i.e. the "a_n ≡ 1 / residue at s=0" of the question) cancels, and with it self-duality. The property that
separates ζ from a_P is additive and group-theoretic (0 ∈ indices, closed under subtraction), combined with the multiplicative one: (+,·) again.
This refines SPEC_003's restriction ("a_P shares the gap but not the mirror of a term"): the mirror of a term of ζ
is exactly the constant term of θ_ℤ, present because ℤ is a group. (PROVED as an identity; the connection with
SPEC_003's "mirror of a term" is ARGUED — same object in another coordinate, not verified term by term.)

**Consequence for the candidate.** The correct discriminant in the class is the conjunction
  (G) indices = lattice (additive subgroup, with origin) ∧ (M) multiplicative norm count,
which in degree ≤ 2 with fixed Γ is 𝔖 = 0. It is a closed, discrete condition, and passes the full battery. **But**, by
Lemma H and H.3, neither (G) nor (M) enters the window form except through Λ (linear) and the FE (archimedean +
polar): the form "sees" (M) only through the support of Λ on p^k and (G) only through the existence of the FE. There is no term of the
form in which (G)∧(M) appears as a square.

### 4.4 New restriction C-hom

**C-hom (PROVED, Lemma H + H.2/H.3).** Every sign object expressed in the coefficients r of a theta (or of Z) must
be 0-homogeneous in r. Quadratic/four-point forms in θ are excluded; the normalized expressions are
polynomials of unbounded degree whose order-2 term is 𝒬_g (without sign) and which, under multiplicativity, collapse to the
form linear in Λ. Operational corollary: the semiring interaction m·n enters the form **only** as cancellation (the H.3
collapse), never as a surviving quadratic term in the Euler case. A sign object seeking "the mn term" must look for it in
an object where cancellation H.3 is *not* complete — for instance, outside the form (a second coupled object) — or in
the *way* the collapse occurs (which polynomial identity produces it), not in a residual term.

---

## 5. Discussion of the round's thesis

### 5.1 What is confirmed
- Positivity, if it holds, in Z_τ lives in {𝔖 = 0}, a discrete set (13 orbits) — consistent with C-τ and with Prop 4.1
  (CONDITIONAL). In degree 1 with fixed Γ, SPEC_004's Prop 2.1 gives the isolated point ζ. The "discontinuous output" thesis is
  correct as a description of the positivity set.
- The natural discontinuous invariant exists, is an integer and is of (+,·) type: 𝔖 = h − 1 (with δ_ring as its non-
  invariant version). PROVED/CITED.

### 5.2 What is not confirmed
- The implicit thesis "the sign object *is* that invariant" does not hold: a discontinuous invariant decides **where**
  positivity may occur but does not **produce** it. The identity 𝔞^{a} = 𝔞^{Euler(a)} + 𝔇 transfers the whole burden to
  point 3 (OPEN), which for ζ is L′♯ itself. ARGUED, but firm: no construction in §§2–4 writes 𝔞^{Euler} without
  using the form.
- The route "theta + Bochner with a Poisson kernel and multiplicative coefficients" is closed off by exact C-hom and by
  V2/front A/symbol rigidity (index).

### 5.3 What remains alive (honest residue)
- **R11.1 (OPEN, new).** The polynomial identity realizing the H.3 collapse is a family of relations among the
  terms (r−δ₁)^{*k}(n), k ≥ 2, n not a prime power. In the Euler case they sum to zero; for Epstein h ≥ 2 they do not. Question: is the
  collapse, restricted to n with two prime factors m ≈ kn of the window (near-coincidences, problem (S)), an
  identity of the form "square = square" (e.g. r(p)r(q) = r(pq)) usable as a **restriction** in P46's dual LP
  (a cut valid only for Euler combs)? This would be a use of discontinuous (M), compatible with C-θ and C-τ, that
  acts on the certificate and not on the form. Risk: P46's LP is already linear in Λ and the cut may be empty there;
  one must check the index to see whether "multiplicative cuts in the LP" is already there (it does not appear under that name in the grep).
- **R11.2 (OPEN).** The lattice origin (constant term of θ) as an object: the exact difference ζ vs a_P is C.1(ii).
  Is there a form of the archimedean/polar term of 𝔞_T that "is" the constant term of θ and whose interaction with the
  deleted primes is what causes a_P to fail? This connects with the pole (P46) and not with the comb. High risk of REF-D
  (the pole is already in the form).

---

## 6. Task D — Ranking, first exact lemma, risk

| Rank | Object | Status | Value |
|---|---|---|---|
| 1 | 𝔖 = h − 1 as a **selector/calibrator** for every proposal (a proposal that does not vanish exactly at 𝔖 = 0 and does not distinguish 𝔖 = 1 is comb-generic or false by C-τ) | PROVED/CITED | hard filter for subsequent rounds |
| 2 | R11.1: multiplicative cuts (H.3 collapse relations) in the dual LP, localized at m ≈ kn | OPEN | the only use of non-linear (M) that does not clash with C-hom |
| 3 | Decomposition A.5 for h = 3 (D = −23): first case with a **complex** class character; Λ_def has a part that is not even in any y | PROVED as an identity; sign not expected | new falsifier/calibrator, no numerics unless necessary |
| 4 | R11.2: lattice origin ↔ polar term | OPEN | REF-D risk |
| — | Quadratic / four-point form in θ with a Poisson kernel | **NO-GO PROVED** (C-hom) | do not retry |
| — | Bochner/complete monotonicity of θ | NO-GO (comb-generic, PROVED) | do not retry |
| — | "𝔇 ≤ 0" for the class defect | NO-GO (COSH_DEFECT) | do not retry |

**First exact lemma (for the round-12 construction).**
*Lemma 12.1 (to be proved, PROVED expected).* In the normalization of A.5, the k = 2 term of Λ_def^{C} is
−½ log n · Ẽ_C^{*2}(n), and for h = 2 it coincides, modulo the change of basis Λ_def = ½(Λ_ψ − Λ_K) + Λ_cosh, with the
term κ₁ b^{*2} of COSH_DEFECT (κ₁ = ½). For h = 3 (D = −23, Ĉl ≅ ℤ/3, χ, χ̄ complex conjugates) write explicitly
Ẽ_C, Ẽ_C^{*2} and the associated multiplicative Hankel matrix 𝒬_g, and verify that it is real (PROVED expected: χ(C)L_χ + χ̄(C)L_χ̄ is
real for real s). Goal: have the 𝔇 term for h=2,3 in a single formula; without claiming sign.

*Lemma 12.2 (R11.1, OPEN).* Formulate the H.3 collapse relations of order 2 as linear restrictions on the
dual LP variables of P46 in the coordinates c_N, N ∈ [μ, 2μ) (SPEC_001: c_N = −μ(N), PROVED) and decide whether any is
non-trivial in that window. If all are trivial (implied by linearity in Λ), record NO-GO.

**Risk.** High. This round's candidate is a correct and new classifier as a formalization, but Lemma H and
symbol rigidity prove that the (+,·) information of the lattice reaches the window form only as exact cancellation
and as FE; the sign cannot be extracted from a discontinuous invariant without a mechanism that makes that
discontinuity work inside an inequality. R11.1 is the only identified channel; it may turn out empty.

---

## 7. Entry for the index (to be copied by the coordinator; this file does not edit the index)

- **SPEC_SIGN_OBJECT_005 (phase 200, round 11):** δ_ring(τ) = [ΛΛ:Λ] = a(τ) (PROVED); 𝔖 = h(D) − 1 discontinuous integer
  invariant, zero exactly at the 13 Heegner h=1 points (CITED); exact decomposition Λ_Q = Λ_K + Λ_def by class
  characters for arbitrary h, Λ_def = log n·log(1+Ẽ_C) (PROVED given Hecke); Lemma H: the window form is 0-homogeneous in
  the theta coefficients ⇒ **NO-GO PROVED** for every exact "quadratic form / four-point in θ" identity (restriction
  C-hom); normalized expansion = degree-Ω(n) polynomial with order-2 term = Hankel matrix 𝒬_g; multiplicative collapse to Λ
  linear (H.3). a_P: ϑ_P without constant term (origin missing), non-self-dual Poisson (PROVED). Bochner of θ comb-generic
  (NO-GO). 𝔖 = classifier, not a sign engine (NO-GO as sign object, ARGUED). Do not retry: quadratic form in θ,
  Bochner of θ, Poisson+multiplicativity as an inequality. Residues: R11.1 (multiplicative cuts in the dual LP, OPEN),
  R11.2 (lattice origin ↔ pole, OPEN).

L′♯: OPEN. Row D: OPEN.
