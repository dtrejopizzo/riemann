# INV_B_002 — Making PRR-log concrete and testing it (phase 194, track B)
Labels: DEFINITION / PROVED / NO-GO (within declared class) / CONJECTURE / OPEN. Pen and paper, no numerics. No negative value for ζ.
Notation: F = g*g̃, ζ_X(s) = Σ_{n≤X} n^{−s}, dμ_X(t) = |ζ_X(½+it)|² dt/2π (a POSITIVE measure), h⁰_X(Γ_F) = ∫ F̂ dμ_X (INV_B_001).
Key fact (PROVED, Fourier): W(F) is LINEAR in F (quadratic in g). Any mechanism must produce a linear functional of F as the k²-coefficient.

## 1. Three candidate definitions of kD
(a) Dilation D_k: F_k(u) = F(u/k). Window grows to kT. ∫F̂_k dμ_X = ∫F̂(t)|ζ_X(½+it/k)|² dt/2π: as k→∞ concentrates at t≈0 where |ζ_X(½)|² ~ (polar) X-growth. PROVED (dominated convergence): leading term is polar (F̂ mass at 0 times |ζ_X(½)|²), no k² term carrying the prime/archimedean data. Rejected.
(b) Convolution power ("tensor power", composition of correspondences Γ_g^{∘k}): F_k = F^{*k}, F̂_k = F̂^k (F̂ = |ĝ|² ≥ 0). This is the natural one: Γ_a∘Γ_b = Γ_{ab}, so kD = k-fold composition, exactly as O(kD) = O(D)^{⊗k}. Window kT.
  h⁰_X(kD) = ∫ F̂(t)^k dμ_X(t) = ∫ e^{k log F̂(t)} dμ_X(t) — a moment generating function in k.
  PROVED (Hölder): k ↦ log h⁰_X(kD) is convex; its cumulants are κ₁ = E_{μ_X}[log F̂] (tilted at k), κ₂ = Var(log F̂) ≥ 0.
  PROVED (Laplace): as k→∞, log h⁰ = k·log max F̂ + O(log k), max F̂ = F̂(0)-ish (or F̂(±i/2) after the polar shift if one moves the contour). Growth is EXPONENTIAL in k with a LINEAR log, not k²·⟨D,D⟩.
  κ₂ is a variance of log F̂ = log|ĝ|², quadratic in log|ĝ| — not the window form (which is linear in |ĝ|²). NO-GO: no exact match; the k² coefficient of log h⁰ is ½κ₂, with no identity to 𝔞_T(g).
(c) Exponent power of the Euler product: M_F(k) := ∫ F̂(t)|ζ_X(½+it)|^{2k} dt / ∫F̂. Then
  d/dk log M_F |_{k=0} = E_{F̂}[log|ζ_X(½+it)|²] = 2 Σ_{n} (Λ(n)/(log n))·n^{−1/2}·F(log n)/F̂(0) + (truncation terms)  (PROVED for the Euler-truncated variant; log ζ = Σ Λ(n)/(n^s log n)).
  This is a FIRST cumulant and carries Λ(n)/log n, not Λ(n). Inserting log n is u-multiplication, i.e. d/dt on F̂: W(F) ≈ ∫ F̂(t)·(−d/dt) arg ζ ... i.e. the window form is the first k-cumulant of the measure F̂(t)·(d/dt)-differentiated. First cumulants are linear and carry NO sign. κ₂ = Var_{F̂}(log|ζ|²) ≥ 0 but it is quadratic in log|ζ| (Selberg-CLT size), not 𝔞_T.

## 2. Is the variance mechanism G0? (PROVED structural lemma)
Suppose 𝔞_T(g) = Var_ν(L_g) for a positive measure ν and an observable L_g linear in g. Then 𝔞_T(g) = ∫|L_g|²dν − |∫L_g dν|², i.e. a Gram form minus a rank-one (polar) correction. This is precisely the Gram factorization G0 / REF-D (positive spectral measure realizing the form). So "second cumulant = window form" with g-linear observable IS G0, not new. The only escape is an observable NONlinear in g (like log F̂ in (b)), and then κ₂ is not the (g-quadratic) window form. CONCLUSION (PROVED): in the class {MGF k ↦ ∫ e^{kφ}dν, ν ≥ 0, φ any}, the window form is the second cumulant only via G0; otherwise it is a first cumulant (signless).

## 3. What survives: two-parameter version (CONJECTURE, new)
Use σ as the second parameter: H_X(k,σ) := ∫ F̂(t)^k |ζ_X(σ+it)|² dt/2π (PROVED convex in k, log-convex in σ by Hölder in the Dirichlet coefficients? — log-convexity in σ is PROVED for ∫|Σa_n n^{−σ−it}|² = Σ|a_n|² n^{−2σ} in the diagonal (mean-value) limit, since that is an MGF in σ with positive weights).
∂_σ log H_X at σ=½ = 2 E[Re ζ_X'/ζ_X] under the tilted measure F̂^k|ζ_X|² — the log-derivative of the h⁰ density, as the coordinator noted. The window form is a σ-derivative, not a k-cumulant. CONJECTURE PRR-log′: the MIXED cumulant ∂_k∂_σ log H_X |_{k=0,σ=½} equals 𝔞_T(g)/‖g‖² + (explicit polar term) + o(1) as X→∞, and positivity would follow from a joint log-convexity of H_X in (k,σ) (Hessian ≥ 0) — which is NOT automatic (a mixed derivative of a jointly convex function is bounded by the diagonal ones, |κ_{kσ}|² ≤ κ_{kk}κ_{σσ}, not signed). So PRR-log′ gives at best |𝔞_T| ≤ √(κ_kk κ_σσ): a Castelnuovo–Severi-type BOUND (CS of INV_B_001), not a sign. OPEN: whether a Hodge-type sign arises by restricting to a ray in (k,σ) where the form is "primitive" (orthogonal to the ample direction σ-only).

## 4. Effectivity lemma
DEFINITION: D = Γ_F is effective iff F ≥ 0 pointwise (a positive current on 𝒮); nef iff ⟨D,Γ_a⟩ ≥ 0 for all a.
PROVED: under convolution powers effectivity and positive-definiteness are both stable (F^{*k} ≥ 0, F̂^k ≥ 0).
PROVED: for effective F the finite intersection part −Σ Λ(n)n^{−1/2}(F(log n)+F(−log n)) is ≤ 0: on 𝒮 effective classes are exactly where primes cost. Hence "h⁰ grows ⇒ effective ⇒ nef" (the F_q chain) is reversed in sign at the prime meetings; nefness must come from the archimedean + polar parts dominating. Since h⁰_X(kD) > 0 for every test class (Bochner), "h⁰ grows" is automatic and carries no information: NO-GO for the naive effectivity lemma. Needed (OPEN): a SHARPER h⁰ — sections constrained on the near-coincidence locus (e.g. Σ over (m,n) with n/m not a prime power, or with the counting measure on ℕ×ℕ minus its multiplicative-diagonal part), whose growth is not Bochner-trivial.

## Verdict
- kD = convolution power (k-fold composition) is the right definition. h⁰(kD) is an MGF; log h⁰ convex (PROVED); no k²·𝔞_T term (NO-GO for (a),(b),(c) as stated).
- "Variance = window form" with g-linear observable is G0/REF-D (PROVED); not new.
- New residue: two-parameter (k,σ) cumulant; gives CS-type bound, sign OPEN (PRR-log′).
- Effectivity: naive version vacuous; needs a constrained h⁰ on the near-coincidence locus (OPEN, named: "h⁰ off the multiplicative diagonal").

