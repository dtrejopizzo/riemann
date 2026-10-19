# INV_F_001 — The ∂log wall: which positivity cones cross f ↦ −f′/f (track F, phase 194)

Track F. Positivity is assumed true; the work is to find the tool. Labels:
PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / REF-D. Pure mathematics, no numerics.
Notation as in Paper 47 (eq:symbol, eq:form): 𝔞_T(F) = (2π)^{−1}∫ σ_T |F̂|², σ_T = m − P_T, P_T(τ) = Σ_{n∈N_T} v_n cos(τ log n),
v_n = 2Λ(n)n^{−½}, F ∈ 𝒫_T; c_F = F∗F̃ the autocorrelation (the task's "F = g∗g̃").

## 0. Corpus / index check (mandatory)
Searched ROUTES-TRIED-INDEX (README, 01–06, 05b, audits), grid, crossword, phase 194 files. Relevant indexed entries:
- Herglotz/Pick/Kreĭn/de Branges/Hermite–Biehler: ES-16 (CIRCULAR/Conrey–Li), P0-3, G2F-phase-102/115,116 (Weil–Herglotz positive boundary
  measure, REF-D), thm:KEPdich (Kreĭn indeterminacy, REF-D, phase 155 r5), W1/REF-D cluster (thm:Z one-sided smoothing), L16, L20, L38,
  PHASE193 audit #86 (Θ′ not pointwise > 0; σ_T(0) < 0).
- Laguerre–Pólya / PF / Schoenberg: README line 32 (heat flow / dBN / LP / Jensen: N5, circular), L23, L48, L75, L76, AUDIT_A §1
  (Michalowski: PF₅ fails for the dBN kernel).
- ∂log appearances: INV_C_001 Identity 5, INV_D_001 G2, INV_E_001 Thm E2 (class 𝓒_0, hypertranscendence).
- Scaling: Paper 47 lem:shape-scale (O_4 lists "an Euler product ζ^c" as O_4-preserved).
**New reason for this memo (not a retry).** None of the entries above asks the *structural* question: for which cones K does
f ∈ K ⇒ −f′/f ∈ (some cone), and is every such cone automatically O_4-closed? The LP/Pick/Kreĭn entries are used here only as
classified items (§2), not re-attacked. The new object is the ∂log-transfer map on cones itself (Theorems F1–F3).

## 1. The general mechanism (PROVED)
∂log is a group homomorphism (multiplicative → additive): −(fg)′/(fg) = −f′/f − g′/g, and for sums
  −(f+g)′/(f+g) = ω·(−f′/f) + (1−ω)·(−g′/g),  ω = f/(f+g),
a *function-valued* (in the Dirichlet algebra: convolution-valued, ω = f∗(f+g)^{∗−1}) weight. So:

**Lemma F0 (PROVED).** Let S be a convex cone. Then M_S := {f : −f′/f ∈ S} is a multiplicative semigroup, and M_S is closed under addition
iff the weights ω, 1−ω act positively on S — which fails as soon as ω has a sign-changing (convolution-)expansion.
"Free positivities" (counts, norms, traces, |ζ|², class numbers) are convex cones closed under +; ∂log-carried positivities are
semigroups closed under ×. The two structures meet only where log is linear, i.e. on infinitely divisible (ID) objects.

## 2. Classification of the classical cones under ∂log
Write 𝒟 for formal Dirichlet series f = 1 + Σ_{n≥2} a_n n^{−s}, L for log-multiplication (n ↦ log n).

| # | Cone P | Carried by ∂log? | Exact ∂log image / reason | Label |
|---|---|---|---|---|
| C1 | a_n ≥ 0 (counts, linear in data) | **NO** | f = 1 + 2^{−s}: −f′/f = log2·Σ_k (−1)^{k+1}2^{−ks}, coefficient at 4 is −log 2 | PROVED |
| C2 | M₊ := {log f has coefficients ≥ 0} (Dirichlet-ID) | **YES, exactly** | −f′/f = Σ (c_n log n) n^{−s}, c = coefficients of log f; b_n ≥ 0 ⇔ c_n ≥ 0 | PROVED |
| C3 | M₊ is not convex | — | f = (ζ_2+ζ_3)/2 (ζ_p local factors, both in M₊): coefficient of log f at 6 is −¼ | PROVED |
| C4 | Bochner p.d. functions φ(t) | **NO** in general | ½+½cos t is p.d., has zeros; log undefined; Bernoulli law not ID | CITED (classical) |
| C5 | ID characteristic functions (Lévy–Khintchine) | **YES** | log φ = ψ conditionally negative-definite (Schoenberg); ∂log of the Lévy exponent = Lévy-measure moment | CITED; = P60-1 / INV_A_001 (indexed) |
| C6 | Pick (Nevanlinna) functions f | **log carried, ∂log NOT** | log f is Pick (arg ∈ (0,π)); f′ and −f′/f are not Pick in general (f = −1/z is Pick, −f′/f = 1/z is anti-Pick) | PROVED |
| C7 | Laguerre–Pólya / Hermite–Biehler (real entire) | **YES, iff** | f ∈ LP ⇔ −f′/f Pick on ℂ₊ (poles of a Pick function are real) | CITED (Levin, Ch. VII) |
| C8 | Pólya frequency kernels PF∞ | **YES** (Schoenberg) | Λ PF∞ ⇔ 1/𝓛Λ ∈ LP; ∂log image is the C7 Pick condition | CITED; PF₅ fails for dBN kernel (indexed AUDIT_A) |
| C9 | PF₂ / log-concavity | **YES** (one sign) | (log f)″ ≤ 0 — a sign of the ∂log image, nothing more | PROVED (definition) |
| C10 | TP₂ kernels K(x,y) | **YES** | TP₂ ⇔ ∂_x∂_y log K ≥ 0 (log-supermodularity) | CITED (Karlin) |
| C11 | positive measures, Laplace transform | log-convexity only | (log 𝓛μ)″ ≥ 0 by Cauchy–Schwarz; sign of (−f′/f)′ only, not of −f′/f | PROVED |

**Theorem F1 (exact carried cone in 𝒟; PROVED).** For f ∈ 𝒟 the following are equivalent: (i) −f′/f has nonnegative coefficients;
(ii) log f has nonnegative coefficients; (iii) f = exp(μ) with μ a positive measure on (ℕ_{≥2},·) — f is the "Dirichlet characteristic
function" of a compound-Poisson (ID) law on the multiplicative semigroup. The set M₊ is a multiplicative semigroup, closed under
f ↦ f^c for every c > 0, and not convex (C3). The convex cone of C1 is not carried (C1).
*Proof.* (i)⇔(ii): b_n = c_n log n, log n > 0 for n ≥ 2. (ii)⇔(iii): definition. Powers: log f^c = c log f. ∎

So the only cones that cross ∂log are, up to equivalence, **ID cones** (C2, C5, C10 on the multiplicative side) and the
**real-zero/Pick cone** (C7–C8). The convex "linear in data" cones (C1, C4, C11, h⁰, Hecke/Petersson traces, H ≥ 0) do not cross.
This is the general form of INV_C_001 Identity 5, INV_D_001 G2, INV_E_001 Thm E2.

## 3. What each surviving cone says about 𝔞_T on 𝒫_T
**(a) ID cone C2/C5 (verifiable from the Euler product, σ > 1; condition (b) of the task: YES).** For ζ, log ζ = Σ Λ(n)/log n · n^{−s}
has nonnegative coefficients (Euler product; linear in the log-data). Its ∂log image is exactly Λ ≥ 0 (C2), i.e. the comb ν_T =
½Σ v_n(δ_{log n}+δ_{−log n}) is a positive measure. On 𝔞_T this yields only |P_T(τ)| ≤ P_T(0) = 𝒜_T, hence
  𝔞_T(F) ≥ (2π)^{−1}∫ (m − 𝒜_T)|F̂|² ≥ (C_0 − 𝒜_T)‖F‖²   (C_0 = −5.372…),
negative. Positivity of the comb measure points the wrong way: the comb is subtracted, and ν_T(c_F) has no sign for F ∈ 𝒫_T (ν̂_T = P_T
changes sign). Transport to σ = ½ is not needed here — the information is the same at every σ (weights Λ n^{−σ} ≥ 0).
**(b) Pick/LP cone C6–C8 (Hadamard side).** In z = −i(s−½), −Ξ′/Ξ(z) = Σ_ρ (γ−z)^{−1} (symmetric summation). For Im z > ½ (σ > 1), every
term has positive imaginary part since |Im γ| < ½: **Im(−Ξ′/Ξ) > 0 on Im z > ½ (CITED, Hadamard; unconditional).** Its boundary value
on the line Im z = η > ½ is a pointwise-positive shifted symbol σ^{(η)}(τ) = m_η(τ) − Σ_n 2Λ(n)n^{−½−η}cos(τ log n) + Π_η(τ), where
Π_η > 0 is the Poisson kernel of the poles s = 0, 1. Two facts close it:
 - Π_η is a Poisson kernel, not a rank-two term: no subspace of codimension 2 (the 𝒫_T analogue) annihilates it, so positivity of
   m_η − comb_η on a primitive subspace does not follow (PROVED: Π_η(τ) > 0 for all τ, so ∫Π_η|F̂|² > 0 for every F ≠ 0).
 - Moving η ↓ 0 with pointwise positivity is exactly one-sided smoothing / Herglotz boundary measure: thm:Z and G2F-phase-102/115
   (REF-D, indexed). Pointwise positivity at η = 0 is false (σ_T(0) < 0; audit #86). Not retried.
**(c) Can either reach Λ with exact weights before the line?** (a) reaches Λ exactly (it *is* Λ ≥ 0) but carries only the trivial bound.
(b) carries a genuine sign, but it is a zero-side statement ((R)(4) fails) and its σ > 1 content is again the Euler-product bound
|−ζ′/ζ(σ+it)| ≤ −ζ′/ζ(σ) plus archimedean growth plus the pole; nothing beyond (a) survives subtraction of the pole.

## 4. The NO-GO (Theorem F2) and its exact hypothesis
**Theorem F2 (∂log-cone NO-GO; PROVED, using lem:shape-scale of Paper 47).** Let 𝒦 be any family of statements about the arithmetic factor
of the form "log ζ ∈ K" or "−ζ′/ζ ∈ K′" on Re s > 1, with each K, K′ a cone (closed under multiplication by c > 0; convexity not
needed), true for ζ — in particular C2, C5, C10, the Bochner/ID statements in t, and any ∂log image of an ID cone. Let 𝒜 be the deduction
class whose arithmetic premises are 𝒦 together with comb-generic identities (thm:shape(B″)) and the archimedean data. Then 𝒜 is closed
under O_4 (Λ ↦ cΛ, archimedean factor fixed), so by thm:shape(A) and lem:shape-scale it contains no valid deduction of WP_T at every
T > ½log2 (c large) and every T ≥ 0.60 (c small).
*Proof.* log(ζ^c) = c·log ζ ∈ K and −(ζ^c)′/ζ^c = c(−ζ′/ζ) ∈ K′, so every premise in 𝒦 holds for ζ^c, whose comb is cΛ; the archimedean
data are untouched; comb-generic identities hold for every weight vector. Hence 𝒜 is O_4-closed. Apply lem:shape-scale. ∎
**Corollary F3 (PROVED).** Combining Theorem F1 and Theorem F2: every positivity that crosses ∂log on the Euler-product side is a cone
condition on log ζ, hence O_4-blind; every positivity that is not a cone condition on log ζ but is free (C1, C4, C11, h⁰, Hecke, Petersson,
class numbers) does not cross ∂log (Lemma F0/F1). The Pick/LP cone (C7) crosses ∂log but is verified only at σ > 1 via Hadamard
(zero side), and its transport is thm:Z (REF-D).
Answer to the task's decision (a)∧(b)∧(c): **no cone in the classified list satisfies all three.** No new partial positivity of 𝔞_T is
obtained; the only consequence ((a) above) is the trivial bound (C_0 − 𝒜_T)‖F‖², which is not new.

**The one hypothesis an invention must break: homogeneity (H_cone).** Every ∂log-carried premise is invariant under log ζ ↦ c·log ζ.
An invention must use a property of ζ that is **not conic in log ζ** yet is **multiplicative enough to cross ∂log**. The canonical
non-conic datum is integrality of the additive side: the coefficients of exp(log ζ) are exactly 1 (ζ = Σ n^{−s}), which holds for c = 1
and fails for ζ^c (d_c(n) ∉ ℤ for c ∉ ℕ; for c ∈ ℕ, d_c(n) ≠ 1). This is precisely the (ℕ,+,·) link of the semiring principle: "log-data
nonnegative (·) AND exponential has all coefficients 1 (+)". Any certificate must therefore use a **curved** constraint coupling
log ζ with exp(log ζ) — a constraint of the form Φ(log ζ, ζ) = 0 that pins c = 1 (integrality, or the functional equation, which also
pins c = 1 at conductor 1). Statement of the residue (OPEN, unindexed as a *class*): find a non-homogeneous positivity on the pair
(Λ, 1_ℕ) jointly, e.g. a quadratic inequality in which both the counting coefficients (=1) and Λ appear, with Λ entering through the
exact convolution identity 1∗Λ = L·1 (log n = Σ_{d|n} Λ(d)), which is linear in each of Λ and 1 and needs no ∂log. Note: 1∗Λ = L
is the ∂log identity written *before* inversion; using it as a constraint (not solving for Λ) avoids the wall of Lemma F0. Whether
any positive form built on (1, Λ, L) with 1∗Λ = L is O_4-non-closed and comb-specific is OPEN; it must not reduce to Selberg-sieve /
Λ² weights (check index before building).

## 5. Verdict
- PROVED: Lemma F0, Theorem F1, C1/C3/C6/C9/C11 rows, Theorem F2 (from lem:shape-scale), Corollary F3, §3(a) bound, Π_η > 0 remark.
- CITED: C4, C5, C7, C8, C10 (Schoenberg, Lévy–Khintchine, Levin, Karlin), Hadamard positivity on Im z > ½.
- REF-D: transport of the Pick cone to the line (thm:Z, G2F-phase-102/115; not retried).
- NO-GO (class 𝒜 = cone premises on log ζ / −ζ′/ζ + comb-generic identities): Theorem F2.
- OPEN: non-conic constraint coupling (1, Λ, L) via 1∗Λ = L (hypothesis to break: H_cone).
- No new partial positivity. No contact with the sign.

