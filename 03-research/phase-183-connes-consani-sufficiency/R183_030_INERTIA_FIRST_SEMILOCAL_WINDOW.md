# R183.030 — Inertia in the first semilocal window (ξ metric)

Sources: R183_019 §1 (dictionary h = ½ξ − ξ′), R183_023 (B_2, Thm 3.1),
R183_026 (§2–§4), R183_027 (low-band falsifier), CC 2006.13771 (102)–(104), Lemma 6.9–6.10,
Thm 6.11, Rem 6.12. Paper 46: thm:log5A, thm:log5W, lem:monoT.
Scripts (NUMERICAL, outside the repo): `scratchpad/r183_030_inertia.py` and `scratchpad/r183_030_scan.py`
(session scratchpad d9ffd571…).

## 0. Verdict

1. **Correction to the initial formulation.** ½log3 = 0.5493. The points T = 0.60, 0.70, and 0.80 are **not** in the
   window ½log2 < T < ½log3: there, 3 (T > 0.549) and 4 (T > log2 = 0.693) have already entered. Hence
   three forms are computed: S = {∞} (archimedean), S = {∞,2} fixed, and S = S(T) = {∞} ∪ {p^k < e^{2T}}.
2. **With S = S(T), n₋ = 0 on primitives for every T computed** (0.35–0.90). For
   T ≤ ½log5 this is a theorem (CITED, Paper 46 thm:log5A). From it comes the gap in the ξ metric:
   c_T ≥ λ_A/4 ≥ 6·10⁻¹³ (PROVED given Paper 46, §3). Alignment is automatic: a_min = 0. But
   the gap falls off superexponentially (table §2.3). At T ≈ 0.9 it is already in double-precision
   noise.
3. **With S = {∞,2} fixed**, positivity survives beyond ½log3 up to **T ≈ 0.5668** and breaks
   after that: n₋ = 1, and n₋ = 2 at T = 0.60 (NUMERICAL). Prime 3 is needed starting at 0.567, not
   from 0.549.
4. **Archimedean structure of one aligned direction (CC).** On primitives, n₋(W_∞) becomes
   1 at T₁ = 0.5967 and 2 at T₂ = 0.8039. **On ker ℓ ∩ primitives, n₋(W_∞) = 0 up to
   exactly T₂ = 0.8039**, and equals 1 up to T ≈ 1.0015. Hence the archimedean negative
   direction is "aligned" with ℓ (ℓ kills it) for every T < T₂. CC's mechanism of one aligned
   direction, with no primes, holds up to **T_max^{∞} ≈ 0.8039 ≈ ½log5 − 0.0008** (NUMERICAL; the proximity
   to ½log5 = 0.80472 has no explanation).
5. **K_{S,T} has no meaningful "#λ>1" count**: with the archimedean Sonin fixed, it is +∞ (§1.3).
   The well-defined quantity is n₋ of the full form, which, under RH, equals 0 for every T. Thus, "N_T with
   zero directions" for every T is exactly RH (Paper 46). The index gives a reformulation, not a
   mechanism. Neither RH nor the closure of D is claimed.

## 1. Exact definitions

### 1.1 The full form in the ξ variable (PROVED, bookkeeping)

For ξ ∈ C_c^∞(I_T), I_T = [−T,T], set h = ½ξ − ξ′. Then ∫h e^{−x/2} = 0 automatically,
∫h e^{x/2} = ∫ξ e^{x/2} and ℓ(ξ) := ĝ(0) = ½∫ξ (R183_019 (1.2)–(1.3)). Also ĥ(s) = (½+is)ξ̂(s),
with ĥ(s) = ∫h e^{isx}. The semilocal form is

    W_S(h) = (1/2π)∫|ĥ|² m(s) ds − 2 Σ_{n∈⟨S⟩, log n<2T} Λ(n) n^{−1/2} c_h(log n),
    m(s) = Re ψ(¼+is/2) − log π,   c_h(a) = ∫h(x)h(x+a)dx.

On primitives (ĥ(±i/2) = 0) the polar terms vanish. With S = S(T) one has W_S = W_T,
Paper 46's Weil form.

**Lemma 1.1 (PROVED).** c_h(a) = ¼c_ξ(a) + c_{ξ′}(a) = [(¼ − ∂_a²)c_ξ](a).
*Proof.* The cross term is −½[∫ξ(x)ξ′(x+a) + ∫ξ′(x)ξ(x+a)]. Integrating by parts with compact
support, the second summand is −∫ξ(x)ξ′(x+a). The two cancel. Also c_{ξ′} = −c_ξ″. ∎

Thus, the prime term in ξ is B_S := −Σ Λ(n)n^{−1/2}(¼ − ∂²)(τ_{log n} + τ_{−log n}), compressed to
I_T. This matches the kernel √2 log2 (¼ − ∂∂)·½(δ_{log2} + δ_{−log2}) of R183_023/027 (up to the
global sign, which here is written explicitly).

### 1.2 CC's convention: what is positive and what is counted

By CC (83), Son = W_∞ + E, with Son(h) = ‖Sϑ(h)‖²_{HS} ≥ 0 (Thm 4.7). By (102)–(104),
E(h) = −κ⟨ξ,(Id − K_{I_T})ξ⟩ with κ := 2ε′(1⁺) ≈ 45.99 (R183_026 §3's normalization; R183_019 §1.3
notes Prop 5.5's variant ½(1+ε), which only changes κ). Hence

    W_∞(h) = Son(h) + κ⟨ξ,(Id − K_{I_T})ξ⟩.

The **positive part** is Son. The **operator whose inertia CC count** is K_{I_T}: the
negative directions of κ(Id − K) are #{λ(K_{I_T}) > 1}. For |I| > log2, K_{I_T} is *defined* by this
identity (compression of the translation kernel). CC's Prop 5.5 only covers |I| ≤ log2
(R183_026, point 3).

### 1.3 K_{S,T} (definition; PROVED that its count is infinite)

    W_S(h) = Son(h) + κ⟨ξ,(Id − K_{S,T})ξ⟩,   K_{S,T} := K_{I_T} − κ^{−1} B_S.

K_{I_T} is Hilbert–Schmidt on L²(I_T). B_S contains ∂², so it is bounded on H¹_0 but not on L²
(R183_023). Its spectrum, relative to the H¹_0 form, is {0, ±log2/√2} with infinite multiplicity in
the first window. Hence K_{S,T} is unbounded and "#{λ(K_{S,T}) > 1}" is not a finite
spectral count. What is well defined is n₋(κ(Id − K_{S,T})) = n₋(W_S − Son), and this number is **+∞** for
T > ½log2 (R183_018 Thm 5.1 / R183_019 Thm 4.1: NO-GO for the entire Sonin space). The honest question is
then n₋(W_S) **with Son included**, which is what is computed below.

## 2. Interlacing and computation

### Lemma 2.1 (interlacing; PROVED)

Let q be a real symmetric bilinear form on a space D. Let C ⊂ D be the subspace of
primitives, or of primitives in ker ℓ. Let V_1 ⊂ V_2 ⊂ … be a chain of finite-dimensional
subspaces. Define n₋(q|V) as the maximal dimension of a subspace U ⊂ V with q < 0 on U∖{0}. By
Sylvester's law, n₋(q|V) is the number of negative eigenvalues of q's matrix in any basis,
and does not depend on the metric (ξ or L² of h). Then:

(a) M ↦ n₋(q|V_M ∩ C) is nondecreasing and ≤ n₋(q|C).
(b) Fix an inner product ⟨·,·⟩; let μ_j(M) be the j-th Rayleigh–Ritz value of q relative
to ⟨·,·⟩ on V_M ∩ C. Then μ_j(M) is nonincreasing in M and μ_j(M) ≥ μ_j(C) (min-max).
(c) Suppose D has a norm ‖·‖_* with |q(x,y)| ≤ C‖x‖_*‖y‖_*, that the functionals defining C are
‖·‖_*-continuous, and that ∪_M V_M ∩ C is dense in C. Then n₋(q|V_M ∩ C) → n₋(q|C),
including the case ∞.

*Proof.* (a) If U ⊂ V_M ∩ C is negative, it is also negative as a subspace of V_{M+1} ∩ C and of C.
(b) It is the Courant–Fischer principle over increasing classes of subspaces. (c) Let U ⊂ C be negative
of dimension k, with a ⟨·,·⟩_*-orthonormal basis u_i. There is δ > 0 with q ≤ −δ on U's unit sphere.
Choose v_i ∈ V_M ∩ C with ‖u_i − v_i‖_* < ε. For x = Σa_iu_i unit and y = Σa_iv_i one has
|q(x) − q(y)| ≤ C(2+kε)kε, which is < δ/2 for small ε. The v_i are independent and q < 0 on their
span, so n₋(q|V_M ∩ C) ≥ k. ∎

**Application.** Let ‖h‖²_* = (1/2π)∫|ĥ|² log(e+|s|) ds. W_S is ‖·‖_*-continuous: |m(s)| ≤ C log(e+|s|)
and the prime term is L²-bounded. The arena is V_M = {ξ = (1 − (x/T)²)²p(x/T): deg p < M}. By
density of (1−u²)²·polynomials in H²_0(−1,1) (standard, CITED), the corresponding h are dense in
the form's domain with the restrictions. The restrictions are ∫ξe^{x/2} = 0 (primitive) and
∫ξ = 0 (ker ℓ).

### 2.2 Implementation (NUMERICAL)

- Quadrature: ξ̂ by Gauss–Legendre with 1600 nodes in x, and s ∈ [0,700] via 24-point Gauss
  panels. With the basis (1−u²)², |ĥ|² log s = O(s^{−4}log s), so the tail is negligible.
- Prime terms: c_h(log n) via Gauss on [−T, T − log n], for all n = p^k with log n < 2T.
- Double precision is used, no intervals. Rayleigh–Ritz eigenvalues are upper bounds
  (Lemma 2.1(b)), and the n₋ counts are lower bounds on the true n₋.
- Control: at T = ½log2, λ_min(L²h) = +0.547 is obtained, matching R183_026's +0.549.

### 2.3 Table (NUMERICAL; M = 28 / M = 40)

Notation: λ_ξ is the minimum relative to ‖ξ‖² over primitives. c_ξ is the same minimum over
ker ℓ ∩ primitives (the gap). λ_h is the minimum relative to ‖h‖²_{L²} over primitives.

| T | S | n₋ prim | n₋ kerℓ | λ_ξ (M=40) | c_ξ (M=40) | λ_h (M=40) |
|---|---|---|---|---|---|---|
| 0.3466 | {∞}=S(T) | 0 | 0 | +46.4 | +145 | +0.547 |
| 0.45 | {∞} | 0 | 0 | +14.4 | +59.7 | +0.285 |
| 0.45 | {∞,2}=S(T) | 0 | 0 | +3.40 | +50.8 | +0.0667 |
| 0.5393 (=½log3−0.01) | {∞,2}=S(T) | 0 | 0 | +0.0618 | +4.18 | +1.50e−3 |
| 0.60 | {∞} | 1 | 0 | −0.189 | +17.0 | −6.6e−3 |
| 0.60 | {∞,2} | 2 | 1 | −2.79 | −2.79 | −0.047 |
| 0.60 | S(T)={2,3} | 0 | 0 | +2.63e−3 | +0.217 | +6.8e−5 |
| 0.70 | {∞} | 1 | 0 | −3.46 | +5.92 | −0.164 |
| 0.70 | {∞,2} | 2 | 2 | −5.52 | −5.38 | −0.083 |
| 0.70 | S(T)={2,3,4} | 0 | 0 | +2.1e−6 | +4.0e−4 | +5.9e−8 |
| 0.80 | {∞} | 1 | 0 | −4.90 | +0.131 | −0.301 |
| 0.80 | {∞,2} | 2 | 2 | −15.7 | −9.59 | −0.253 |
| 0.80 | S(T)={2,3,4} | 0 | 0 | +2.3e−10 | +6.5e−8 | +6.6e−12 |
| 0.90 | {∞} | 2 | 1 | −5.50 | −3.00 | −0.424 |
| 0.90 | S(T) | 0 | 0 | ~1.7e−13 | ~1.1e−11 | ~6e−15 (noise) |
| 1.00 | S(T) | 0/1 | 0 | ±4e−13 | | machine noise |

Stabilization. The n₋ counts are stable between M = 16, 28, and 40 on every row with |λ| ≫ 10⁻¹².
The minima decrease with M (they are upper bounds) by 1–4% from M = 28 to M = 40. On S(T) with T = 0.80
they decrease by a factor ≈2, i.e. only the order of magnitude is stabilized. For T ≥ 0.9 double
precision does not resolve the sign: the rows at 0.9 and 1.0 prove nothing.

Cross-check. λ_h(0.80, S(T)) ≈ 6.6·10⁻¹² (upper bound) versus the certified lower bound
λ_A ≥ 2.5·10⁻¹² at ½log5 from Paper 46. They are compatible and of the same order.

### 2.4 Thresholds by bisection (M = 28, NUMERICAL)

| form | first T with n₋ ≥ 1 | first T with n₋ ≥ 2 |
|---|---|---|
| W_∞, primitives | T₁ = 0.59669 | T₂ = 0.80387 |
| W_∞, ker ℓ ∩ primitives | **0.80387 (= T₂)** | 1.0015 |
| W_{∞,2} (fixed S), primitives | 0.56676 | (≤ 0.60) |
| W_{∞,2}, ker ℓ ∩ primitives | 0.56676 | |

T₁ and T₂ reproduce R183_026's 0.5963 and 0.8033 with a different basis. In the form with prime 2 the
threshold is the same with or without ker ℓ: the negative direction created by prime 2 is **not**
aligned with ℓ.

## 3. The gap in the window (PROVED given Paper 46)

**Proposition 3.1.** For 0 < T ≤ ½log5 and S = S(T), on primitives one has

    W_T(h) ≥ λ_A ‖h‖²_{L²} ≥ (λ_A/4)‖ξ‖²_{L²},   λ_A ≥ 2.5·10⁻¹².

*Proof.* The first inequality is Paper 46's thm:log5A with lem:monoT (CITED, verified in
ball arithmetic). For the second, by Plancherel ‖h‖² = (1/2π)∫(¼+s²)|ξ̂|² ≥ ¼‖ξ‖². ∎

Consequences:
- n₋(W_T|C) = 0 throughout the window and up to ½log5.
- The gap is c_T ≥ 6.25·10⁻¹³ in the ξ metric, on primitives and hence also on
  ker ℓ ∩ primitives.
- In R183_019's Thm 3.1/Cor 3.2, a = 0 suffices: Q ≥ 0 with no correction |e⟩⟨e|. Alignment is
  automatic because there is no direction to align.

In the genuine first window (T < ½log3, S = {∞,2}) the numerical values are much
larger: c_ξ ≈ 4.2 and λ_ξ ≈ 0.062 at ½log3 − 0.01.

Caveat. It must be checked that Paper 46's P_T (two moments ĥ(±i/2) = 0, L²(I_T)) matches
our C. See review point 1.

## 4. The inductive step and T_max

**Inductive statement (I_k).** For T ∈ [T_k, T_{k+1}), between two consecutive entries of
prime powers:

    E_{S(T)} ≥ c_T‖ξ‖² on ker ℓ ∩ C.

By §§2–3 it holds with c_T > 0 up to ½log5 (PROVED) and numerically up to ≈ 0.85 (beyond
precision afterward).

**What breaks it.**

(i) **Archimedean band.** n₋(W_∞|C) ≈ 4T − 2: equals 1 from 0.597 and 2 from 0.804. Restricting
to ker ℓ absorbs exactly one direction up to T₂ (§2.4). Beyond that, the archimedean term only
contributes ≥ 1 unaligned negative direction.

(ii) **Each prime adds a ± non-compact term.** With fixed S, positivity drops shortly after
each entry (with {∞,2}: at 0.567). From there the band worsens (R183_026 Prop 5.1: the
slope rises from 4 to 9 to 15). With S = S(T), the new primes *repair* positivity. No visible
mechanism: in the table the gap falls off like e^{−αT²}-superexponentially.

**Proposition 4.1 (upper bound; PROVED given R183_023 Thm 3.1 and Lemma ε-L∞).** For every
η ∈ (0,1],

    n₋(W_{S(T)}|C) ≤ N(η,T) ≲ 4T·e^{2A_T/η},   A_T = Σ_{n<e^{2T}} Λ(n)n^{−1/2}·(const),

because B_S ≥ −(1−η)Son − (finite rank ≤ N(η,T)) and W_∞ − Son has a bounded kernel. Since A_T ~ 2e^T,
the bound is finite for each T but doubly exponential: it does not give n₋ ≤ 1.

**Proposition 4.2 (lower bound; CONDITIONAL(RH), R183_027).** For any fixed-η partition,

    n₋(W_{S(T)} − (1−η)Son|C) ≥ 2γ₁T/π − O(log T) − 3,

so the "one aligned remainder direction" version fails for T ≥ T_max(η) < ∞. The constant
O(log T) is not explicit in 027, so T_max(η) is not yet computable (OPEN). For the full form W_{S(T)},
under RH n₋ = 0 for every T: there is no lower bound.

**Conclusion on T_max.**

| version of "one aligned direction" | T_max | label |
|---|---|---|
| pure archimedean (CC, K_{I_T}, ℓ kills the direction) | ≈ 0.8039 (T₂ = threshold on ker ℓ) | NUMERICAL |
| fixed S = {∞,2} | ≈ 0.5668 | NUMERICAL |
| remainder W − (1−η)Son, fixed η | finite, not explicit | CONDITIONAL(RH) |
| full form W_{S(T)}, zero directions | proved up to ½log5; ∀T ⟺ RH | PROVED (≤ ½log5) / ⟺ RH |

A "aligned direction" mechanism cannot hold for every T. What can hold for every T
is "zero directions" of the full form, which is D.

## Status

```text
Def. K_{S,T}; c_h=(¼−∂²)c_ξ; n₋(W_S−Son)=+∞ for T>½log2                PROVED
Lemma 2.1 interlacing (monotonicity, bound, convergence with density)   PROVED (density CITED)
n₋(W_{S(T)}|C)=0 and ξ gap ≥ 6.25e-13 for T ≤ ½log5                     PROVED given Paper 46 (CITED)
Table §2.3, thresholds §2.4 (0.5967, 0.8039, 0.5668; kerℓ=T₂)           NUMERICAL (double precision)
Superexponentially small gap in T                                       NUMERICAL
Prop 4.1 upper bound N(η,T)                                              PROVED given R183_023
Prop 4.2 lower bound for fixed η                                        CONDITIONAL(RH)
Explicit T_max(η)                                                        OPEN
N_T with zero directions ∀T                                              ⟺ RH; row D OPEN
```

## Review points

1. **The space C versus Paper 46's P_T.** Prop 3.1 imports λ_A exactly as Paper 46 defines it
   (§1, def. of P_T). It must be confirmed that they are the same two moment conditions, the same
   normalization of W_T, and the same L²(I_T). If not, Prop 3.1 remains CONDITIONAL.
2. **κ = 2ε′(1⁺).** R183_019 §1.3 gives a different normalization. The count does not depend on κ, but
   "K_{S,T} = K − B/κ" does.
3. **Thresholds.** With M = 28 one has lower bounds on n₋, so the true threshold is
   ≤ the reported one. The 5-digit agreement T₂(prim, 2nd direction) = T₁(ker ℓ) may be
   structural (the first eigenvector is nearly the constant, CC α ≈ 0.95) or an artifact. It is not
   verified with a different basis.
4. **Precision.** For T ≥ 0.85 with S(T), the minima are below 10⁻¹¹ and double precision
   does not decide the sign. No row in that range is used as evidence.
5. **Density of the arena.** (1−u²)²·polynomials in H²_0 is standard, but convergence in M is
   slow (upper bounds drop ~1% per 12 modes). The counts are stable; the gap values are
   stable only in order of magnitude.

## Note (R183_032)

* Thresholds T₁, T₂ have not converged in M: M=16/28/40/52 give
  T₁ = 0.5981/0.5967/0.5961/0.5956 and T₂ = 0.80596/0.80387/0.80316/0.80273.
  Only T₁ < 0.5956 and T₂ < 0.8027 are claimed. The proximity to ½log5 = 0.80472
  is a truncation artifact.
* By contrast the equality λ₁(ker ℓ) = λ₂(primitives) holds to 8 digits
  across all M: a structural identity still to be proved (OPEN).
* The minimum at ½log2 with M=40 is 0.5459, not 0.549.
* Minor script bug: the {∞,2} mode omits n=4 for T ≥ 0.70.
