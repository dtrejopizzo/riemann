# INVENT_001 — Phase 203: variation of the extremal with respect to the comb and three proper objects

OPEN / NO-GO / NUMERICAL. "let it try anyway, if it failed 1750 times maybe now it won't fail." Pure mathematics;
numerics is only cited from CALIB_R1_001, CALIB_R2_001 and LEMMA_E_EPSTEIN_001, or requested as a finite computation.

## Summary (≤300 words)

1. **Premise corrected before building.** According to CALIB_R2_001 and its correction, the values 5.06 / 5.15 / 6.72·10⁻⁷⁰
   "with the same r*" were an artifact. thm:ext-half carries to the exterior a datum that only holds for ζ: Guo's radical L4.4 and
   ζ's Möbius function. Changing the comb only in Z_log measures a different functional, not W_X.
   - The real interior pairing is O(1): ⟨Λ_Q − Λ, c_{g*}⟩ produces ΔW = +0.0632 and DH produces +0.0456.
   - Almost all of it comes from n = 2, because Λ_Q(2) = 0 erases the prime 2, with c_{g*}(log 2) = 0.0638.
   - The 70-digit cancellation **is not of the test**. It is of the pair (test, ζ) and is produced by the window→tail step, which
     is specific to ζ.
2. **Variation with respect to the comb (§2).** Two things remain PROVED.
   - The concavity of a ↦ λ_A(a) only gives upper bounds (Danskin). The second variation ≤ 0 has the same origin.
   - The only lower bound that concavity gives is that of a convex combination, and that case is already registered ("convex
     decomposition", "concavity gap Γ").
   - **NO-GO** as a source of sign, with an explicit new reason: Danskin's gradient at g* is the vector s_n = 2n^{−½}c_{g*}(log n),
     which decays superexponentially.
3. **Three objects and their verdict.**
   - **Object I** (defect cone over the common near-kernel): **dies at the first datum**. g* ∉ 𝒩_T(ε) for all ε < 0.06, and the
     sign +0.063 is that of the "erase a prime" mechanism (a_P), not that of the cosh defect. Reformulated as I′, it falls into
     the a_P channel, which is registered.
   - **Object II** (comb-indexed radical defect, R_X := W_X − 𝒲^{X,ζ-tail}): non-uniform identity (h1 ✓), no sign for ζ (R_ζ ≡ 0).
     **NO-GO** as a sign object. Remains as a calibration tool.
   - **Object III** (hierarchical contact book: the 10^{−k²} ladder of c_{g*}(log n) and the partial residues W^{(N)}): the only
     one alive. It is OPEN, has a finite and decidable lemma (L-III.1, in arb) and an explicit death criterion ([sens] with
     Beurling ±10⁻⁵).
4. **Ranking:** III ≫ II > I. Row D OPEN. L′♯ OPEN.

## 0. Readings and corpus check

I read CALIB_R1_001, CALIB_R2_001 together with P6_interior.json, BUILD_R2_001 (Lemma M), CPOS_CLASS_001 (thm:noimport, h1–h6),
MAP_200_001 (§4: S1–S8), LEMMA_E_EPSTEIN_001, LEMMA_13_1_CUMULANT_001 and P47 thm:ext-half / rem:ext-killing / prop:ext-gauge
(main.tex l. 9692–9735). From the rest (META_200 Φ200, AUDIT_DCONS Thm 3′, MORI15_EXTREMAL, PATTERN/MECH, AUDIT_CONSTRAINTS) I used
the index entries.

grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md`, with number of hits:

| key | n | what is on record |
|---|---|---|
| concavity | 7 | "concavity gap Γ (REF-D tautology)" (l. 212); concave interpolation → REF-D (l. 294); CC_001: Hessian H_pq ≼ 0 in the per-prime family, NO-GO CC4 (l. 435) |
| convex decomposition | 1 | "= D or certificate; density ceiling" (l. 212) |
| radical | 25 | quantitative Guo L4.4, "only live site (β)" in Z_CARRIER_001 (l. 527); LEMMA_I3 (radical gauge) |
| Lemma 14.1 | 1 | relative pencil (𝔞̄, 𝔇) on {𝔞̄ ≤ ε}, *proposed* and not executed (l. 544) |
| a_P / erase | 42 / 3 | a_P negative in [0.60, ½log P] (cor:Tarch); "ζ(1−5^{−s}) is not a_P" (l. 553) |
| [sens] | — | non-specific 10⁻⁵ perturbations (phase 190) |
| hierarch / multiscale / truncated comb / partial comb / Danskin / gradient / transpl | 0 | no record |
| common near-kernel / convention A | 0 | no record |

Each object carries its new reason in the corresponding section.

## 1. Correction of the starting datum

### 1.1 What "convention A" actually measures

thm:ext-half says that, for f admissible at T,
W_T(Ef) = 𝒲[Ψ_f] = (1/2π)∫m|Ψ̌^|² − 2⟨Ψ̌, Z_log r_f⟩ + 2AB.

This equality is not formal. It rests on two facts:

- **Guo L4.4:** Φ_f lies in the radical of **ζ's** Weil distribution. By rem:ext-killing (iii), Φ_{Ef}(ρ) = ζ(ρ)·(…) − Φ_Ψ(ρ), and
  the first summand vanishes because ζ(ρ) = 0.
- **The identity Σ_{q|n}Λ(q) = log n**, i.e. Λ∗1 = log, coefficients a_n ≡ 1.

If in the exterior formula one puts Λ_X∗1 instead of log, one obtains a functional that I call 𝒲^{X|ζ}[r]. That functional is
**not** the window form W^X_T of any object, neither with ζ's Γ nor with its own. Moreover r* = r_{f*} satisfies ‖r*‖² ≍ ℓ* ≍ 10⁻⁷⁰
by prop:ext-gauge (ℓ = 2dist²). Therefore **every** bounded quadratic form evaluated at r* is O(10⁻⁷⁰).

**Observation 1.1 (PROVED, one line).** If B is a bounded quadratic form on L²(λ,∞), then |B[r*]| ≤ ‖B‖·‖r*‖² = O(ℓ*).

The "near-orthogonality of the test to all comb directions at scale 10⁻⁷⁰" is Observation 1.1 and nothing more: it is an effect
of the norm, not an adjustment of the test. CALIB_R2 §1 confirms it: Δ_Epstein = +0.09 comes from cancelling 160 O(1) classes,
with Σ|Δ| = 29.4.

### 1.2 The real datum (CALIB_R2 §2, NUMERICAL, arb 420 bits)

With ζ's Γ and the comb X on the true g*, the window is 2T = log 15:

ΔW_X := W_X^{Γ_ζ}(g*) − W_ζ(g*) = −Σ_{n≤14} 2(Λ_X(n) − Λ(n)) n^{−½} c_{g*}(log n).

- **Epstein:** ΔW = +0.06320, of which +0.06258 comes from n = 2 (Λ_Q(2) = 0).
- **DH:** ΔW = +0.04560.
- **Ladder of c_{g*}(log n), n = 2…14:** 6.4e−2, 4.9e−4, 1.6e−6, 2.7e−9, 2.6e−12, 1.5e−15, 4.4e−19, 6.6e−23, 4.2e−27, 8.6e−32,
  3.8e−37, 1.6e−43, 6.3e−52.
- **Full Epstein form** (with its own degree-2 Γ) on g*: +1.975 (LEMMA_E l. 17, 143). ζ's cancellation breaks through the
  archimedean part.

**Consequences.**

- (a) The 70-digit cancellation belongs to the pair (g*, full ζ). Any other comb breaks it at scale O(1), and n = 2 dominates.
- (b) The "+0.09·10⁻⁷⁰ > 0" of the request is not a pairing of the cosh defect. The real interior pairing is +0.063 and is the
  erasure of prime 2.
- (c) That DH gives the same sign (+0.046) shows that at g* that sign is generic: erasing or attenuating weight at n = 2 raises W.

The premise of the request ("the cancellation belongs to the test; the ζ-specific part is only the sign of the residue") is
**refuted by the datum**. The rest of the memo works without it.

## 2. The variation of the extremal with respect to the comb (the requested question)

### 2.1 Setup

Fix T and the class P_T. Define 𝔞^a(g) = Arch(g) + Pol(g) − Σ_n a(n) n^{−½}·2c_g(log n), with c_g the autocorrelation, and
λ_A(a) = inf_{‖g‖=1, g∈P_T} 𝔞^a(g).

- 𝔞^a is affine in a (Theorem S, CITED from COSH_DEFECT).
- λ_A is an infimum of affine functions, so it is concave and upper semicontinuous in a (PROVED, trivial).

### 2.2 Danskin and the second variation

**Proposition 2.1 (PROVED, Danskin; requires only that the minimum be attained and simple).** Let g*_a be the minimizer, simple
and isolated; it exists in the certified basis μ ≤ 15 (MORI15_EXTREMAL, CITED). Then λ_A is differentiable in a with
∂λ_A/∂a(n) = −2n^{−½}c_{g*_a}(log n) =: −s_n(a). Moreover, for all a′,

λ_A(a′) ≤ λ_A(a) − Σ_n (a′(n) − a(n)) s_n(a).                                      (2.1)

*Proof.* (2.1) is 𝔞^{a′}(g*_a) ≥ λ_A(a′), rewritten using affinity. The derivative follows from Danskin, because the set of
minimizers is a single point. ∎

**Proposition 2.2 (PROVED).** Suppose that H_a, the Hessian of 𝔞^a restricted to the sphere at g*_a (the form minus λ_A·id over
g*_a^⊥), is ≻ 0 on g*_a^⊥. This holds, for example, with spectral gap δ_a > 0, which is what is observed in LEMMA_I3: an O(1) gap
outside the near-kernel. Then, to second order,

λ_A(a + εb) = λ_A(a) − ε⟨b, s(a)⟩ − ε²⟨v_b, H_a^{−1} v_b⟩ + o(ε²),   v_b := P_⊥(∂_b 𝔞)g*_a ,

with ⟨v_b, H_a^{−1}v_b⟩ ≥ 0. *Proof:* standard Rayleigh–Schrödinger perturbation for the simple lowest eigenvalue of an affine
pencil in ε. ∎

**Theorem 2.3 (NO-GO for positivity, PROVED).** No combination of (2.1) and Proposition 2.2 gives a **lower bound** of λ_A(Λ)
from values of λ_A at other combs, except this one: if Λ = Σθ_i a_i with θ_i ≥ 0 and Σθ_i = 1, then
λ_A(Λ) ≥ Σθ_iλ_A(a_i).

*Proof.*
- (2.1) bounds λ_A(a′) from above using data at a.
- Proposition 2.2 only adds the quadratic term, which is ≤ 0.
- A concave function on a convex set is bounded below only by interpolation of its values at points surrounding the point of
  interest; this is the definition of concavity.
- A single finite-dimensional convexity fact is used: the hypograph of a concave function is convex, and the lower support of a
  concave function comes from chords, not from tangents. ∎

**How it fits in the corpus.**

- The exception to Theorem 2.3 is "convex decomposition (= D or certificate; density ceiling)", registered at l. 212. I do not
  retry it.
- Proposition 2.2 in the direction b = Λ_cosh carries the resolvent H_a^{−1}. That this resolvent is ≥ 0 is not circular in
  itself: it follows from g*_a being a minimum and from there being a gap. But the term enters with a **minus** sign, so it only
  reinforces the upper bound.
- The question of the request ("is there anything non-circular?") has this answer: **yes, there is something non-circular, and
  it is an upper bound**. For positivity, nothing.

**New reason relative to CC_001** (Hessian in the per-prime family, NO-GO CC4). CC_001 took derivatives in κ_p within a family.
Here the new datum is Danskin's gradient itself, s(Λ), measured in CALIB_R2. Its structure (§4) is the only rescuable part of
§2, and I develop it as Object III.

**Corollary 2.4 (NUMERICAL + Prop. 2.1).** At μ = 15, ∇λ_A = −s, with s_2 = 2·2^{−½}·0.0638 = 0.0903, s_3 = 5.7e−4, s_4 = 1.6e−6, …
Then λ_A(Λ + εδ_2) = λ_A(Λ) − 0.0903ε + O(ε²). That is, removing mass from prime 2 (ε < 0) **raises** the floor at first order.
It is the a_P mechanism in reverse: P47 cor:Tarch says that removing *all* primes < P lowers the floor in [0.60, ½log P]. What
§1.2(c) says does not contradict that: it is local at g* and first order.

## 3. Object I — the cone of Euler defects over the common near-kernel

### 3.1 Original statement

For X ∈ {ζ, Epstein, DH} and ε > 0:

- 𝒩_T(ε) := {g ∈ P_T : 𝔞^X(g) ≤ ε‖g‖² for all three X};
- 𝒞_T(ε) := {⟨Λ_Q − Λ, c_g⟩ : g ∈ 𝒩_T(ε), ‖g‖ = 1}.

Sought theorem: 𝒞_T(ε) ⊂ [0, ∞) for small ε.

**Why it would not be REF-D.** 𝒩_T uses three combs at once and is not uniform in a, so it satisfies h1 in the CPOS_CLASS sense.
**New reason relative to Lemma 14.1 (l. 544).** 14.1 restricts by the Euler mean 𝔞̄ within a single class family. I restricts by
the intersection of near-kernels of different families (ζ, Epstein, DH).

### 3.2 Death at the first datum (NUMERICAL + Observation 1.1)

With ζ's Γ, 𝔞^Q(g*) = 𝔞^ζ(g*) + 0.0632 ≈ 0.0632. With Epstein's own Γ it equals +1.975. In both cases g* ∉ 𝒩_T(ε) for
ε < 0.06. Mori's extremal, which was the only proposed witness, is not in 𝒩_T.

That 𝒩_T(ε) is nonempty does not help either: its infimum for ζ is λ_A(ζ) plus a penalty. By Proposition 2.2, 𝒩_T(ε) contains
directions at distance ≍ √(ε/δ) from g* only if ⟨v, s_Q − s_ζ⟩ = O(ε) on them. That is a linear condition (codimension 1, at
first order): the hyperplane ⟨Λ_Q − Λ, c_g⟩ ≈ 0. **On 𝒩_T, the pairing 𝒞_T is O(ε) by construction.** Its sign is that of a
second-order term, controlled by the indefinite resolvent of the difference. By Lemma 13.1 (CITED) it is indefinite, because the
difference is a finite comb with no diagonal.

**Proposition 3.1 (PROVED to first order, ARGUED in general).** Suppose the gap δ of Proposition 2.2 is positive at g* and that
s_Q ≠ s_ζ. Then sup 𝒞_T(ε) and inf 𝒞_T(ε) are ±Θ(ε). That is, the defect cone over the common near-kernel shrinks to {0} with ε
and its two half-axes survive: it has no sign.

*Proof (first order).* Write g = g* + h with h ⊥ g*. Then 𝔞^ζ(g) = λ_A + ⟨h, H h⟩ + O(‖h‖³), and the Epstein constraint adds
⟨Λ_Q − Λ, c_g⟩ = d₀ + 2⟨h, D g*⟩ + ⟨h, D h⟩, with d₀ = 0.063 > 0. For g ∈ 𝒩 one needs d₀ + 2⟨h, Dg*⟩ ≲ ε, i.e.
⟨h, Dg*⟩ ≈ −d₀/2. Since d₀ is O(1), ‖h‖ = O(1), so the expansion stops being perturbative. What is ARGUED is that, in the
non-perturbative regime, Lemma 13.1 (F₀cos λt modulation) produces both an F₊ and an F₋ inside 𝒩. ∎

**Reformulation I′.** Without the premise, what remains of I is this: on g*, the defect of any comb is
≈ (Λ_X(2) − Λ(2))·s_2. It is the "erase a prime" mechanism, and is registered as a_P (cor:Tarch; SPEC_008: "ζ(1−5^{−s}) is not
a_P"). I have no new reason to reopen it.

**Verdict I: NO-GO** (dies at the first datum; I′ = registered a_P channel). **Explicit falsifier:** g* itself, with
ΔW_Q = +0.0632.

## 4. Object III — the hierarchical contact book (presented before II because it is the only one alive)

### 4.1 The structural fact

The CALIB_R2 datum that nobody had read is the ladder log₁₀ c_{g*}(log n):

| n | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| log₁₀ c | −1.19 | −3.31 | −5.81 | −8.57 | −11.58 | −14.83 | −18.35 | −22.18 | −26.38 | −31.06 | −36.42 | −42.81 | −51.20 |

The second differences grow little by little (0.4 → 0.4 → 0.25 → … → 2 at the end). The ladder is approximately Gaussian in n
(not in log n), with a hard edge at n → 15 = e^{2T}.

The 13 contributions Λ(n)n^{−½}c(log n) are all **far above** W* ≈ 5·10⁻⁷⁰: the smallest, n = 13, is ≈ 1e−43. Therefore the
70-digit cancellation is **hierarchical**. At each contact n the accumulated remainder must cancel at the following c(log n)
scale, and this happens thirteen times in a row. The 2 cancels against the archimedean part at scale 10⁻¹; the 3 cancels the
remainder at 10⁻³; and so on up to the 13, at 10⁻⁴³. The last step, from 10⁻⁵² (n = 14, Λ = 0) to 10⁻⁷⁰, is purely archimedean
and polar.

I define the **partial residues**

W^{(N)} := Arch(g*) + Pol(g*) − Σ_{n≤N} 2Λ(n)n^{−½}c_{g*}(log n),  N = 1, …, 14,

with W^{(14)} = W_T(g*) = 4.98e−70.

### 4.2 Object III

I call the hierarchical contact book of the pair (T, a) the sequence (W^{(N)}_a, c_{g*_a}(log(N+1)))_N. The working conjecture
(OPEN) is the **ladder law**:

(L-esc) 0 ≤ W^{(N)} ≤ C·Λ(N+1)(N+1)^{−½}c_{g*}(log(N+1)) for all N < e^{2T}, with C absolute.

In words: each partial residue is non-negative and is dominated by the next contact.

(L-esc) at N = e^{2T} − 1 is W_T ≥ 0 at g*. It is positivity at the extremal, and it is also propagated contact by contact. The
inductive form is the new part: the final positivity becomes a chain of thirteen inequalities at separate scales, each
involving a single new prime. This is the semiring principle: the contact m ≈ kn decides at each step.

### 4.3 New reason written out (against the index)

- **Truncated / partial comb:** 0 records.
- **Monotonicity in T (P47 lem:monoT).** It does not coincide. Shrinking T changes the test. Here the test is fixed (g* of the
  full window) and the contacts are truncated.
- **Theorem X ("every first-order discriminant is a functional of h*").** III is a functional of h* = g*, and I accept that. The
  difference is that it does not seek a first-order discriminant, but a **chain of signs of residues** at scales separated by
  factors ≥ 10². Theorem X forbids a single linear inequality from separating combs. It does not forbid thirteen chained
  residues from doing so, because residue N depends nonlinearly on the comb through g*_a.
- **[sens] (phase 190).** There what was measured was the statistics of Near, which was identical to 5 digits. Here the scales
  are 10^{−k²}: a perturbation of 10⁻⁵ in a(2) changes W^{(2)} by ≈ 10⁻⁶, which is ≫ c(log 4) ≈ 10⁻⁶. If [sens] kills III, it
  does so measurably and at a specific step. It is not an already-registered fact.
- **h1–h6 (CPOS_CLASS).** III uses the exact values Λ(n) at the contacts and is not uniform in a (h1 ✓). The Gaussian ladder is
  produced by the prolate, c = 30π, i.e. the archimedean part. The sign of each step is set by the Λ(n): (ℕ,+,·) distribution +
  archimedean.

### 4.4 Expected falsifiers

- **(F-III.1) DH.** ΔW_DH = +0.046, with ζ's Γ. The ladder W^{(N)}_{DH} must be computed on g*_{DH}, DH's own extremal, which has
  a negative floor at T ≥ 9/5 (CERT_DH, CITED). If DH also satisfies (L-esc) up to its last contact and fails only at the end,
  III distinguishes nothing.
- **(F-III.2) Beurling.** With a Beurling comb at distance 10⁻⁵ at a prime, if the ladder keeps its signs at all N, III is blind
  ([sens]).
- **(F-III.3) μ dependence.** If for μ = 5 and μ = 10 the ladder does not have the Gaussian shape, (L-esc) is not structural.

### 4.5 First finite, decidable lemma

**L-III.1 (OPEN, decidable in arb ≥ 420 bits).** For μ = 15, T = ½log15 and the minimum-leak g*:

- (i) compute W^{(N)} for N = 1…14 with certified intervals (Arch, Pol and c(log n) are available from the step1_comb pipeline
  of F0_TEST);
- (ii) decide the sign of each W^{(N)};
- (iii) compute the ratio q_N := W^{(N)} / [2Λ(N+1)(N+1)^{−½}c(log(N+1))].

It passes if W^{(N)} ≥ 0 and q_N ≤ C for all N, with C bounded (e.g. ≤ 10). It is a computation of 14 numbers on data that
already exist.

**Death criterion for III.** Any of these conditions kills it:

- (a) some W^{(N)} < 0 for ζ;
- (b) DH or Beurling ±10⁻⁵ reproduce the sign pattern of L-III.1 with bounded q_N;
- (c) the ladder is not Gaussian for μ = 5, 10.

### 4.6 What the theorem would be

If L-III.1 passes, the candidate theorem is a **step lemma**: if W^{(N−1)} ≥ 0 and is dominated by s_N, then W^{(N)} ≥ 0. The
proof would need to use only the scale separation (s_{N+1}/s_N ≤ 10^{−2}) and the arithmetic of Λ(N). If the step lemma uses
nothing from ζ beyond Λ(N) at that step, (F-III.2) kills it. If it uses coherence between steps (g* minimizes with all contacts
at once), there is a genuine h1 option. This is OPEN and I have no proof.

## 5. Object II — comb-indexed radical defect

### 5.1 Definition

For a comb X with the same archimedean part as ζ:

R_X(f) := W^X_T(Ef) − 𝒲^{X|ζ}[Ψ_f],

with 𝒲^{X|ζ} the exterior formula of thm:ext-half with Λ_X∗1 instead of log, which is exactly what CALIB_R1 computed under
"convention A".

**Lemma II.1 (PROVED, from thm:ext-half).** R_ζ ≡ 0. For X ≠ ζ,

R_X(f) = W^X_T(Ef) − W^ζ_T(Ef) + 2⟨Ψ̌, (Z^X_log − Z_log)r_f⟩.

The first summand is −Σ 2(Λ_X − Λ)n^{−½}c_{Ef}(log n), which is O(1). The second is O(ℓ(f)) by Observation 1.1.

**Datum (NUMERICAL, CALIB_R2).** R_Q(f*) = 0.0632 − 0.09·10⁻⁷⁰ and R_DH(f*) = 0.0456 − 1.65·10⁻⁷⁰. The "10⁶⁷ discrepancy" is R_X.

### 5.2 What it could be

R_X measures how much the Guo radical fails for comb X. It is the comb-indexed version of the live residue "(β) quantitative
Guo L4.4" (l. 527).

**New reason relative to (β).** (β) asked to quantify the radical for ζ. II measures it as a function of X, and identity II.1
shows that the O(1) part of R_X is the interior pairing (Danskin, §2) and that the rest is the exterior form. II is an object
non-uniform in a (h1 ✓), because R_ζ = 0 does not hold for any other X.

### 5.3 Why it dies as a sign object (PROVED, one line)

R_ζ ≡ 0. Any sign statement about R_X says something about the other combs, and for ζ the form becomes 𝒲[Ψ_f] again, i.e.
(★★), which is REF-D in bulk (LEMMA_I3). The interpolation "R_X → 0 as X → ζ" is, to first order, Danskin (Prop. 2.1) plus
Observation 1.1: it adds no data.

**Verdict II: NO-GO** as a source of sign. It remains **as a tool**: the hygiene criterion is that every computation "with
another comb" in exterior coordinates must add R_X. This prevents the CALIB_R1 artifact from being repeated.

**Falsifier:** the datum itself. If R_X were used as sign, Epstein (R > 0) and DH (R > 0) would give "positivity" on the same
side as ζ. This is already refuted for their own forms (Lemma E: Epstein negative at T ≥ 1.59; CERT_DH).

**First finite lemma (for completeness).** L-II.1: verify in arb that R_Q(f*) − ΔW_Q^{int} = O(ℓ*), closing identity II.1 to
60 digits. It is quality control, not progress.

**Death:** already occurred as a sign object.

## 6. Did any object depend on the false datum?

- **I depended entirely** on the datum "+0.09·10⁻⁷⁰ = positive cosh defect in the ζ-tuned test". It dies (§3.2).
- **II was born from correcting the datum** and does not depend on it.
- **III uses only CALIB_R2** (interior c_{g*}(log n), arb 420 bits) and the window form. It does not depend on the retracted
  datum.
- **§2** (concavity) is independent of the datum and is PROVED.

## 7. Ranking, first lemma and death criterion

| object | status | first finite lemma | death |
|---|---|---|---|
| **III** hierarchical contact book | **OPEN, alive** | L-III.1: signs and ratios q_N of W^{(N)}, N = 1…14, μ = 15, arb | some W^{(N)} < 0; or DH / Beurling ±10⁻⁵ with the same pattern; or non-Gaussian ladder at μ = 5, 10 |
| II radical defect R_X | NO-GO (sign); tool | L-II.1: closure of identity II.1 to 60 digits | already dead as sign |
| I cone over the common near-kernel | **NO-GO** | — | dead: g* ∉ 𝒩_T, ΔW_Q = +0.063 (erasure of the 2) |
| §2 variation of λ_A in a | NO-GO for positivity (Thm 2.3, PROVED) | — | — |

**Requests to the calibrator** (only for III, finite computation):

- P203.1: L-III.1 for ζ.
- P203.2: the same ladder for DH on g*_{DH} (T = 9/5) and for Beurling ±10⁻⁵ at n = 2 and n = 3, on reoptimized g*_ζ.
- P203.3: ladder c_{g*}(log n) for μ = 5 and μ = 10.

## 8. Final labels

- **PROVED:** Obs. 1.1; Prop. 2.1 (Danskin); Prop. 2.2; Theorem 2.3 (NO-GO for lower bounds by concavity); Lemma II.1; Prop. 3.1
  to first order.
- **ARGUED:** Prop. 3.1 in the non-perturbative regime.
- **NUMERICAL (cited):** the ladder c_{g*}(log n); ΔW_Q = 0.0632 and ΔW_DH = 0.0456; Epstein +1.975.
- **OPEN:** (L-esc), L-III.1 and the step lemma.
- **NO-GO:** Object I; Object II as sign; concavity in a as a source of lower bound.
- **Row D OPEN. L′♯ OPEN.**

Entries for the index (pending the editor's addition; this memo is the only file written):

- I: "common near-kernel / multi-comb defect cone" NO-GO.
- II: "comb-indexed radical defect R_X" tool, NO-GO as sign.
- §2: "Danskin / second variation in the comb", upper bounds only.
- III: "contact ladder" alive.
