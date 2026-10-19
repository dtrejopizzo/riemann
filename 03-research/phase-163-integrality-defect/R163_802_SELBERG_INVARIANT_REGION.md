# R163_802 — Selberg-invariant regions K ⊂ ∩_T 𝒫_T: verification, b-language, NO-GO

Pure math. No numerics. Status labels: PROVED / ARGUED / NO-GO.
Standing convention (as in R162_801 L4): W_T^a(F) is the window-T Weil form with the
archimedean and pole terms of ζ held fixed and the prime side Σ_{2≤n<e^{2T}} a(n)n^{-1/2}(h(log n)+h(−log n)),
h = F∗F̃, supp F ⊂ [−T,T]; λ_A(T;a) = inf_{‖F‖=1} W_T^a(F); 𝒫_T = {a : λ_A(T;a) ≥ 0}.
Everything below that says "fails ∩𝒫_T" uses only this convention.

## 1. The review's three facts

**Fact 1 (RH ⟺ Λ ∈ 𝒫_T ∀T). PROVED (classical).** ∩_T{λ_A(T;Λ) ≥ 0} is positivity of Weil's
functional on all compactly supported test functions h = F∗F̃, which is Weil's criterion
(compact-support form, Bombieri 2000). Nothing new.

**Fact 2 (concavity, convexity, closedness). PROVED.** a ↦ W_T^a(F) is affine in the finitely many
coordinates a(n), n < e^{2T}; an infimum of affine maps is concave; 𝒫_T = ∩_F {W_T^a(F) ≥ 0} is
an intersection of closed half-spaces, so it is convex and closed. *Monotonicity is false.* Each
a(n) enters with coefficient −n^{-1/2}·2h(log n), and h(log n) has either sign. This confirms the
 R162_990: the clause "nonincreasing in each a(n)" in R162_801 L4 must be struck.

**Fact 3 (Selberg fixed point attracts). PROVED.** Selberg's identity Λ·log + Λ∗Λ = μ∗log²
holds. Since a(1) = 0, (a∗a)(n) involves only 1<d<n, so
𝒮(a)(n) = [(μ∗log²)(n) − (a∗a)(n)]/log n depends only on a at proper divisors. Write
d = a − Λ. The deviation then evolves **exactly** as

  (E) d_{𝒮(a)} = −(2Λ∗d + d∗d)/log.

If d vanishes on {Ω ≤ k}, then d_{𝒮(a)} vanishes on {Ω ≤ k+1}, and d_{𝒮(a)}(p) = 0 for every p.
So 𝒮^k(a) → Λ pointwise (each coordinate is constant from k = Ω(n) on). Hence any K that is closed
in the product topology, nonempty, and has 𝒮(K) ⊂ K contains Λ. Each 𝒫_T is closed in that
topology because it depends on finitely many coordinates. Λ is the unique fixed point (§2).

## 2. b-language. PROVED

Let A(s) = Σ a(n)n^{-s} and B = exp(Σ a(n)/log n · n^{-s}), i.e. b = exp_∗(a/log). Then B′ = −AB,
i.e. b·log = a∗b. For every a, −A′ + A² = B″/B. So Selberg's equation for a is
B″/B = ζ″/ζ. Then (B′ζ − Bζ′)′ = 0, and B′ζ − Bζ′ has no n = 1 term, so (B/ζ)′ = 0. Hence B = ζ,
i.e. b ≡ 1. Put Q = B/ζ (q = μ∗b). The map is A_{𝒮} = A + ∫_s^∞ (Q′ζ²)′/(Qζ²). Its linearization
in u = (log_∗ q)·log is u ↦ −2(u∗Λ)/log, which is the linear part of (E).

**Proposition O (sign flip, exact). PROVED.** Let a ≠ Λ and let n₀ be divisibility-minimal in
supp d. Then b(n₀) − 1 = d(n₀)/log n₀. For every prime p, (E) gives

  b_{𝒮(a)}(n₀p) − 1 = −2 log p · d(n₀)/log²(n₀p)

at the new minimal points n₀p: the d∗d term vanishes there and b_{𝒮(a)} − 1 = d_{𝒮}/log to first
order at minimal support. So the sign of b − 1 flips under 𝒮.

Example: b(p) = 1 − τ gives b_{𝒮}(p²) = 1 + τ/2 − τ²/4. This is exact, because 𝒮(a)(p²) uses only
a(p).

**Corollary O (order cones die). NO-GO.** If K ⊂ {b ≤ 1} or K ⊂ {b ≥ 1} and 𝒮(K) ⊂ K, then K ⊂ {Λ}.
In particular the proposed C = {0 ≤ b ≤ 1, N_b(x) = ρx + O(x^θ)} is **not 𝒮-invariant**:

- a = 0 (b = δ) gives b_{𝒮}(pq) = 1 + 2 log p log q/log²(pq) > 1;
- b = 1 − δ_p gives b_{𝒮}(p²) = 5/4.

The alternating cone (−1)^{Ω}(b−1) ≤ 0 also fails. With d = εδ_p, (E) gives
d_{𝒮}(p³) = −2ε/3 < 0, which breaks the pattern at Ω = 3. **Norm balls** {|d(n)| ≤ r n^α}
can be made invariant (α ≥ 2 and r small; the quadratic term needs a weight that controls the
number of divisors τ(n)). But they are neighbourhoods of Λ and are killed by §3.

## 3. Is K ⊂ 𝒫_T possible? NO-GO (the decisive part)

**Lemma D (one-sided perturbations). PROVED, unconditional.** Let ν ≥ 0 be nonzero with
Σ ν(n)n^{-1/2} < ∞. Then Λ − ν ∉ ∩_T 𝒫_T and Λ + ν ∉ ∩_T 𝒫_T.

*Proof.* W^{Λ∓ν}(F) = W^Λ(F) ± ∫|F̂|²φ_ν dt/2π, where φ_ν(t) = 2Σν(n)n^{-1/2}cos(t log n) is
continuous and almost periodic with mean 0. Also φ_ν(0) > 0.

- For Λ + ν: localize F̂ near t = 0.
- For Λ − ν: φ_ν < 0 somewhere. For a single atom n₁ this happens at t = π/log n₁ < 14. In
  general it happens on an open set, which can be chosen away from zero ordinates, and every
  zero ρ has |Im ρ| ≤ ½.

Take F of support W ≤ 2T with F̂ concentrated, to width O(1/W), in that zero-free region. The
contribution of W^Λ is Σ_ρ ĥ(γ), which is exponentially small in W·dist. The φ_ν term is of order
1 and has the needed sign. ∎

**Theorem U (rigidity of ∩𝒫_T in the summable class). PROVED under RH; this is the relevant case.**
If a = Λ + d with Σ|d(n)|n^{-1/2} < ∞ and a ∈ ∩_T 𝒫_T, then d = 0.

*Proof.* Under RH the spectral measure of W^Λ is the atomic Σ_γ δ_γ. That of W^a is
Σ_γ δ_γ − φ_d dt, with φ_d continuous, almost periodic and of mean 0. Positive-definiteness forces
the absolutely continuous part to be ≥ 0, so φ_d ≤ 0 everywhere. Mean 0 then gives φ_d ≡ 0, and
uniqueness of almost-periodic Fourier coefficients gives d = 0. ∎

**Lemma G (growth gate). ARGUED.** a ∈ ∩𝒫_T ⇒ |a(n)| ≤ C√n·log n.

*Argument.* Take the two-bump test F = φ + cφ(·−log n₀), with width δ < 1/(2n₀), ‖φ‖ = 1 and
c = ±1. Then W ≈ 2C' log n₀ + O(1) − 2|a(n₀)|n₀^{-1/2}. The pole terms are O(1).

**Consequence for the programme. NO-GO.** Every K ⊂ ∩𝒫_T satisfies
K ∩ (Λ + ℓ¹(n^{-1/2})) = {Λ} (under RH; Lemma D gives it unconditionally on the cones Λ ± ν).
So the condition C must reject every b = ζ·exp(G) with G an absolutely convergent Dirichlet
series at σ ≥ ½ with no constant term. Such b satisfy N_b = e^{G(1)}x + O(1), i.e. **θ = 0**, with
**any ρ, including ρ = 1** (take G(1) = 0). Hence:

**No Beurling-regularity condition N_b = ρx + O(x^θ), for any θ ≥ 0 and any ρ, and no order
condition, can define K ⊂ ∩𝒫_T.**

Task (3) is answered more strongly than expected. The proposal fails in the continuous class
ζ_θ (R163_101), and it fails just as well **inside the discrete integer class**. Discreteness
does not rescue it, because the falsifiers are integer-supported with bounded error (compare
Thm R of R163_102, where lattice rigidity constrains N_b but not B/ζ).

## 4. Falsifiers (all integer-supported, all satisfy C with θ = 0)

| falsifier | b | in C? | in ∩𝒫_T? |
|---|---|---|---|
| deletion of p | 1_{(n,p)=1}, ρ = 1−1/p | yes | no (Lemma D, ν = Λ_p) |
| fractional deletion ηΛ_2 | ζ(1−2^{-s})^η, b ∈ (0,1] | yes, ρ = 2^{-η} | no (Lemma D) |
| sΛ, s ∈ [0,1) | d_s, 0 ≤ b ≤ 1 | no: N_b ≍ x(log x)^{s−1} | expected no (no proof here) |
| sΛ, s > 1 | d_s > 1 | no | — |
| two atoms Λ − uδ_{n₁} − vδ_{n₂} | 1∗exp(u′n₁^{-s}+v′n₂^{-s}), u′,v′ ∈ [−1,0] | yes, θ = 0 | no (Lemma D) |
| 1 − δ_2 (ρ = 1) | B = ζ − 2^{-s} | yes, ρ = 1, θ = 0 | ARGUED no (see below) |

On the 1 − δ_2 row: B has zeros with 1 < σ by Bohr–Jessen, since ζ_odd = z(1−z) with
z = 2^{-s}, so a(n) grows like n^{σ₀}. Lemma G kills it only if σ₀ > 3/2, which is not established.
This row is therefore ARGUED.

## 5. Verdict

- **PROVED:** Facts 1–3, after striking the monotonicity clause; (E); Proposition O; Corollary O;
  Lemma D; Theorem U.
- **NO-GO:**
  - Every order-type invariant region collapses to {Λ}.
  - Every K ⊂ ∩𝒫_T is {Λ} modulo non-summable perturbations.
  - Integer-side Beurling or density conditions cannot separate Λ from θ = 0 twists ζ·exp(G).

The Selberg-invariance route moves the whole difficulty into "C ⇒ b ≡ 1 up to non-ℓ¹ junk".
That statement is RH-strength and has no global convex certificate visible. Close the route.
What could survive: a C that excludes all absolutely convergent twists, i.e. a condition on
B/ζ itself rather than on N_b. That is a restatement (compare R162 "restatement" verdicts).
