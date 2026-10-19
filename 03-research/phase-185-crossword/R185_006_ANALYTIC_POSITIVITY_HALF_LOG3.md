# R185.006 — Analytic positivity in the first window with a prime (½log2 < T ≤ ½log3)

Sources: R183_018, R183_019 §1, R183_023, R183_026, R183_030 (+ editor's note),
R184_003, CC 2006.13771 §6, Paper 47 (def:W, 𝒫_T, eq:nuw, thm:C, thm:log5A).
Scripts (NUMERICAL, outside the repo, scratchpad d9ffd571…): `r185_006.py`, `r185_006b.py`, `r185_006c.py`
(reuse `r183_030_inertia.py`: base ξ = (1−u²)²P_j(u), h = ½ξ − ξ′, Rayleigh–Ritz in double precision).

## 0. Verdict

**There is no complete analytic proof. The result is a REDUCTION to a finite check.** The
goal's route (archimedean bound in L² followed by the exact norm of B_2) is **NO-GO**, and the exact
step that fails has been identified. The route that survives is different: exact symbol, truncation and compact.

1. **(PROVED) Symbol identity.** For T ≤ ½log3 and h real with supp h ⊂ I_T = [−T,T]:
   W_T(h) = (1/2π)∫|ĥ(s)|² θ(s) ds, with θ(s) = m(s) − √2·log2·cos(s·log2),
   m(s) = Re ψ(¼+is/2) − log π. That is, in the first window W_T is a **truncated
   Wiener–Hopf form with an explicit symbol**. θ(0) = −6.352, and θ < 0 exactly for |s| < 3.305 (NUMERICAL,
   simple root). θ → +∞ like log|s|.
2. **(NO-GO, exact step) Archimedean bound, then norm of B_2.** One needs gap_∞(T) > ‖B_2‖ = log2/√2 =
   0.4901 in L² over 𝒫_T. But gap_∞(½log3) ≈ 0.083 (NUMERICAL, upper bound via Rayleigh–Ritz).
   The inequality breaks at **T_norm ≈ 0.3671**, barely above ½log2 = 0.3466. Hence
   no analytic improvement of the K_I bound (Weyl, interlacing, HS norm of the added strip)
   can save this route. What is needed is *alignment* between B_2 and the archimedean form, not just
   sizes.
3. **(NO-GO) Localized Cauchy–Schwarz.** Using |c_h(log2)| ≤ ‖h_J‖‖h_{J+log2}‖, with
   J = [−T, T−log2], one requires A_∞ ≥ (log2/√2)(‖h_J‖² + ‖h_{J+log2}‖²). This breaks at
   **T_CS ≈ 0.478 < ½log3** (NUMERICAL). The extremal of W_T needs the pointwise correlation
   h(x) ↔ h(x+log2), not just the mass at the endpoints.
4. **(PROVED the reduction / NUMERICAL the residual) Symbol truncation.** For δ > 0 we have
   θ ≥ min(θ,δ) = δ − g_δ, with g_δ = (δ−θ)_+ ∈ [0, δ+6.353], of compact support. Hence

       W_T(h) ≥ δ‖h‖² − ⟨h, G_δ h⟩,   G_δ = P_T (ǧ_δ *) P_T ≥ 0, of finite trace.

   Thus **W_T ≥ 0 on 𝒫_T follows from λ_max(G_δ|𝒫_T) ≤ δ**. This is a finite-dimensional problem
   plus a tail controlled by prolate spheroidal functions. Numerically, at T = ½log3 the truncation does not destroy the
   gap if δ ≳ 1.5 (δ = 2: gap 7.7·10⁻⁴; δ = 3: 9.3·10⁻⁴; untruncated: 9.5·10⁻⁴). The effective
   dimension is **N ≈ 18** eigenvalues of G_2 above δ/10 (NUMERICAL). The analytic bound
   on the prolate tail gives N ≲ 45 (§3).
5. **T_max of the method.** With S = {∞,2} the symbol θ is the same for every T < log2. The truncation
   method can only work while the symbol form θ is positive over the primitives,
   i.e. up to **T ≈ 0.5668** (R183_030 §2.4, NUMERICAL). In the window T ≤ ½log3 = 0.5493 there is
   margin, but small: gap ≈ 10⁻³ in L². This is consistent with the super-exponential decay (TK).
   T₁ ≈ 0.5956 (pure archimedean) is **not** the relevant threshold: prime 2 lowers it to 0.567.

RH is not asserted, nor row D's closure.

## 1. Symbol identity (PROVED)

By def:W / eq:nuw of Paper 47 (in R183_030 §1.1's normalization), over h ∈ 𝒫_T the polar
terms vanish and

    W_T(h) = (1/2π)∫|ĥ|² m ds − 2 Σ_{log n < 2T} Λ(n) n^{−1/2} c_h(log n).

For ½log2 < T ≤ ½log3 the only n with Λ(n) ≠ 0 and log n < 2T is n = 2 (3 enters when 2T > log3 and 4 when
2T > log4). For h real with compact support, c_h is even and c_h(a) = (1/2π)∫|ĥ(s)|² cos(sa) ds
(Plancherel). Hence 2Λ(2)2^{−1/2}c_h(log2) = (1/2π)∫|ĥ|²·√2 log2·cos(s log2) ds, from which
the identity follows. ∎

*Remark.* This gives the exact reading of R183_023 ("spectrum of B_2 = {0, ±log2/√2}"): the
multiplier √2 log2 cos(s log2) has range [−0.980, 0.980] **on L²(ℝ)**. Compression to I_T with
2T < 2log2 reduces the norm to log2/√2 (2×2 Toeplitz blocks in the fibers r ∈ [0, log2)). The two
descriptions are compatible. The symbol one is the useful one.

## 2. Why the "archimedean + ‖B_2‖" route cannot work (NUMERICAL, with its grounding)

Let gap_∞(T) := inf{A_∞(h)/‖h‖² : h ∈ 𝒫_T}. By Lemma 2.1(b) of R183_030 (min-max), the Rayleigh–Ritz
values are **upper bounds** on gap_∞. Consequently, "gap_∞ < 0.49" is a
reliable NO-GO conclusion, up to quadrature error.

| T | gap_∞ (M=28/40) | gap_∞ − log2/√2 | min of A_∞ − (log2/√2)·1_{J∪J′} | λ_h(W_T) |
|---|---|---|---|---|
| 0.35 | — | +0.048 | +0.534 | — |
| 0.37 | — | −0.008 | +0.410 | — |
| 0.45 | — | −0.205 | +0.062 | — |
| 0.50 | 0.178 | −0.312 | −0.053 | 1.19e−2 |
| 0.5393 | 0.101 | −0.389 | −0.166 | 1.50e−3 |
| 0.5493 | 0.083 | −0.407 | −0.197 | 9.6e−4 |

Thresholds by bisection (M = 28): T_norm = 0.3671 and T_CS = 0.4781. The values are stable between
M = 16 and M = 40 to within ±0.004.

**Conclusion.** The step "extend CC's K_I argument from |I| = log2 to log3 via Weyl" would give,
at most, gap_∞ > 0 (numerically true up to T₁ ≈ 0.5956). It would not give gap_∞ > 0.49. The
positivity of W_T at ½log3 is a cancellation of order 10⁻³ between two forms of size O(1). The
only way to capture it is to treat A_∞ − B_2 as **one** form, with its symbol θ.

## 3. Reduction to a finite check (PROVED except for the residual)

**Proposition 3.1 (PROVED).** Let ½log2 < T ≤ ½log3, δ > 0, g_δ := (δ − θ)_+ and
s_δ := sup{s : θ(s) < δ}. Let G_δ be the operator on L²(I_T) with kernel ǧ_δ(x−y), where
ǧ_δ(x) = (1/2π)∫g_δ(s)e^{isx}ds. Then:

(a) W_T(h) ≥ δ‖h‖² − ⟨h, G_δ h⟩ for every h ∈ 𝒫_T.
(b) 0 ≤ G_δ ≤ ‖g_δ‖_∞ · P_T B_{s_δ} P_T, where B_Ω is the band projection |s| < Ω. Consequently,
    μ_k(G_δ) ≤ (δ − θ(0))·λ_k(c), with λ_k(c) the Slepian prolate eigenvalues for c = T·s_δ.
(c) Let N be such that (δ − θ(0))λ_{N+1}(c) < δ. Let U_N be the upper eigenspace of G_δ and ℓ_± the
    functionals ĥ(±i/2) (continuous on L²(I_T), with representatives e^{∓x/2}). Then
    "δ − G_δ ≥ 0 on ker ℓ_+ ∩ ker ℓ_−" is equivalent to a Weinstein–Aronszajn secular
    condition with N explicit terms plus a positive tail bounded by ‖ℓ‖²/(δ − μ_{N+1}).

*Proof.* (a) By §1, θ ≥ min(θ,δ) = δ − g_δ and Plancherel. (b) Because 0 ≤ g_δ ≤ ‖g_δ‖_∞1_{|s|<s_δ},
θ ≥ θ(0) everywhere (m is increasing in |s| and m(0) − √2 log2 = θ(0); the cosine ≥ −1), and by
min-max. (c) This is standard: q = δ − G_δ is positive on U_N^⊥ with lower bound δ − μ_{N+1}, and the
restriction to a codimension-2 subspace is decided by the bordered determinant. ∎

*Note on θ ≥ θ(0).* Uses that m is even and increasing in s ≥ 0 (ψ(¼+is/2) has increasing real
part in s; CITED, standard digamma property). Also −√2 log2 cos ≥ −√2 log2. So
θ(s) ≥ m(0) − √2 log2 = θ(0) = −6.3524. PROVED.

**Constants (NUMERICAL except where noted).**

| δ | s_δ | c = T s_δ | ‖g_δ‖_∞ | prolate N (λ_{N+1} < δ/‖g‖) | effective N (μ_k > δ/10) | gap of min(θ,δ) on 𝒫_T |
|---|---|---|---|---|---|---|
| 1.6 | ≈ 2π e^{2.58} ≈ 83 | ≈ 45 | 7.95 | ≈ 30–32 | 13 | +3.4e−4 |
| 2 | 118.3 | 65.0 | 8.35 | ≈ 43–45 | 18 | +7.7e−4 |
| 3 | 335.5 | 184 | 9.35 | ≈ 118–120 | — | +9.3e−4 |

(‖g_δ‖_∞ = δ − θ(0): PROVED. Prolate N: estimate using Landau–Widom's 2c/π + O(log c), CITED in
asymptotic form and not certified here. For δ ≤ 1.4 the truncated gap is negative, so the
reduction requires δ ≳ 1.5.)

**Theorem 3.2 (reduction; PROVED except for the marked residual).** Let ½log2 < T ≤ ½log3. If the
secular matrix of 3.1(c) with δ = 2 and N = 45 is positive definite (a dimension-≤ 47 check
with the explicit tail), then W_T ≥ 0 on 𝒫_T, with gap ≥ that of this matrix. Numerically the gap
is ≈ 7.7·10⁻⁴ in L² at T = ½log3 (NUMERICAL, consistent with thm:C's 8.86·10⁻⁵ in
Paper 47's normalization, which is not the same; the value is not being compared).

**What is missing for PROVED.** (i) Computing the μ_k and the secular matrix with balls/intervals: this
requires certified quadrature of ǧ_δ and of its products with e^{∓x/2}. (ii) Giving a non-
asymptotic bound on λ_{N+1}(c) (Bonami–Karoui give explicit bounds; not verified here: CITED with
reservation). Neither is analytic in the strong sense. The new content is the reduction:
the problem in the first window is positive minus compact, with explicit symbol and effective
dimension ~ 20.

## 4. Comparison with the goal and with the thresholds

* The CC K_I + Weyl route proves, at most, archimedean positivity. **It does not close the window**
  (§2): the deficit is 0.41 against the size of the prime, not an ε.
* The real advantage of the first window is that **W_T is a truncated Toeplitz form with a single
  symbol** (§1). This no longer holds from ½log3 on: with 3 the symbol changes, but the identity
  still holds with θ_{S(T)} = m − 2Σ Λ(n)n^{−1/2}cos(s log n). The §3 reduction is the same for any
  fixed T, with N(δ,T) ≈ (2T/π)·s_δ(T). So the reduction extends to every T. What does not extend is
  the **margin**: the gap decays super-exponentially (R183_030 §2.3), δ must grow and N grows like
  T·e^{δ}. This is the explicit version of the N ≲ 4T e^{2A/η} of R183_023.
* T_max of the method (with a fixed T and the finite check done): there is no obstruction in the
  method; the obstruction is the precision of the check. For S = {∞,2} fixed, the method fails
  exactly where positivity fails, at T ≈ 0.567 (R183_030).

## State

```text
Identity W_T = (1/2π)∫|ĥ|²θ, θ = m − √2log2·cos(s log2), ½log2<T≤½log3    PROVED
θ ≥ θ(0) = −6.3524; ‖g_δ‖_∞ = δ − θ(0)                                       PROVED (digamma monotonicity CITED)
Route "gap_∞ > log2/√2": fails at T_norm ≈ 0.367 < ½log3                      NO-GO (NUMERICAL, RR upper bound)
Endpoint Cauchy–Schwarz route: fails at T_CS ≈ 0.478 < ½log3                  NO-GO (NUMERICAL)
gap_∞(½log3) ≈ 0.083 in L² over 𝒫_T                                           NUMERICAL
Prop 3.1 (truncation → δ − G_δ, G_δ ≥ 0 trace, prolate bound)                 PROVED
Theorem 3.2: W_T ≥ 0 on 𝒫_T ⟸ secular check of dim ≤ 47 (δ=2)                PROVED (reduction)
The finite check itself; gap ≈ 7.7e-4 (δ=2), effective N ≈ 18                 NUMERICAL (no interval arithmetic)
Non-asymptotic bound on prolate λ_{N+1}(c)                                     CITED with reservation / OPEN
Complete analytic proof of W_T ≥ 0 at ½log3                                   OPEN (thm:C remains the proof)
```

## For the audit

1. **Normalization.** The §1 identity uses R183_030 §1.1's normalization (factor 2Λ(n)n^{−1/2}).
   It must be cross-checked against def:W/eq:nuw of Paper 47, word for word (editor's rule). If Paper 47
   has Λ(n)n^{−1/2} without the 2, the cosine's coefficient becomes log2/√2 and all tables change.
   R183_030's was calibrated against λ_A of thm:log5A (compatible order of magnitude), but that is not
   a verification.
2. **𝒫_T.** In the base h = ½ξ − ξ′ one moment is automatic and the other is imposed. This is the same
   identification as R183_030 (its audit item 1, not closed).
3. **Direction of the numerical inequalities.** The §2 NO-GOs use *upper* bounds
   (Rayleigh–Ritz), hence are reliable in the stated direction. The positive gap of §3 is
   also an upper bound, so it **proves** nothing: it only indicates that the finite check
   has margin.
4. **θ < 0 only for |s| < 3.305.** This is a simple root found by sweeping with step 0.05. There are
   other roots (6.94, 10.53) where θ dips below 0 again due to the cosine's oscillation. The
   positivity of θ for s > 10.53 (m ≥ 0.98 from s ≈ 2πe^{0.98}) is easy to prove; the
   intermediate intervals are not used in the proof.
5. **Prolate N.** "N ≈ 43–45" uses the Landau–Widom asymptotic. For PROVED it must be replaced by
   an explicit bound on λ_k(c).

## For Paper 47

* **Do not** replace thm:C with an analytic argument: there is none.
* A remark can be added after thm:C: "in the first window W_T is the truncated
  Wiener–Hopf form with symbol θ(s) = m(s) − √2 log2 cos(s log2). The bound 'archimedean part
  minus prime norm' fails from T ≈ 0.367, and positivity at ½log3 is a cancellation of
  order 10⁻³. Truncating the symbol at δ = 2 the problem becomes positive minus trace-class, with
  effective dimension ≈ 20". Labels: identity PROVED; thresholds NUMERICAL.
* This explains why the LP certificate is the right tool (Problem A): positivity does not
  come from a dominance of sizes.

## Note (R185_093)

* MAJOR: the tail bound ‖ℓ‖²/(δ−μ_{N+1}) of Prop 3.1(c)/Thm 3.2 is ~0.5 against a gap of 7.7e-4: the dim-47 check as it stands certifies nothing. Correction: tail ‖(1−P_N)ℓ‖²μ_{N+1}/(δ(δ−μ_{N+1})) and require #{μ_k>δ} ≤ 2. The implication "check ⟹ W_T ≥ 0" is indeed proved.
* Remove "T_max ≈ 0.567" (threshold with S={∞,2} frozen). Symbol identity PROVED (v_2 = √2 log 2). NO-GO confirmed (gap_∞(½log3) = 0.084).
