# CALIB_R5_001 — Calibrator, phase 205, Piece 5: 𝔪 and comb in the Dirichlet sine basis (NUMERICAL)

Everything is **NUMERICAL**.
Data in `CALIB_001_data/`:
- `P205_sine_compressions.json` (complete; also P205.log);
- `P205_inertia_robust.json`;
- script `P205.py`.

## 0. Conventions and precision
- **Basis.** s_k(x) = sin(πk(x+T)/2T), with k = 1…N, normalized by √T. The even sector is odd k and the odd sector, even k.
- **Sizes.** N(T) = ⌈2Tt₀/π⌉ − 1, with t₀ = 6.28983598883690. N(T), 2N and 4N were used.
- **Archimedean (P47 eq:Aform, Lévy form).** 𝔪 = (C₀ + κ_T)·c(0) + ∫₀^{2T}(c(0) − c(u))K(u)du.
  - ζ: C₀ = ψ(¼) − log π.
  - Epstein: its own Γ_ℝ(s)Γ_ℝ(s+1), conductor 20 and K = 1/sinh(u/2).
  - a_P (P = {2}): the archimedean of ζ.
- **Comb.** C = −Σ_{log n<2T} v_n c(log n), with v_n = 2Λ_X(n)/√n.
- **Precision.** mpmath at 40 digits. The Lévy integral was done with GL of 5 panels × 60 nodes. With 200 nodes, all eigenvalues of magnitude larger than 1e−12 are stable.
- **Eigenvalues ~1e−15.** They are quadrature noise: one disappears with 200 nodes. They are counted separately as "tiny", with threshold |e| < 1e−10.

## 1. Closed formula (requests b and e)
c_{kk′}(u) = ∫_{−T}^{T−u} s_k(x)s_{k′}(x+u)dx, with a = πk/2T, b = πk′/2T and L = 2T − u:

- a ≠ b: c = ½[ (sin((a−b)L − bu) + sin(bu))/(a−b) − (sin((a+b)L + bu) − sin(bu))/(a+b) ]
- a = b: c = ½[ L cos(bu) − (sin(2bL + bu) − sin(bu))/(2b) ]

It is symmetrized in (k, k′).

**Toeplitz−Hankel reading (exact, not asymptotic).**
- The first term depends only on the frequency difference τ_k − τ_{k′}: it is the Toeplitz part.
- The second depends only on the sum τ_k + τ_{k′}: it is the Hankel part.
- Writing sin((a∓b)L ± bu) in the form cos(...)·A, the truncation factors are A, B = 1/(a∓b) through the phase sine with L = 2T − log n.
- This is more exact than the form cos·A − cos·B, which is an approximation: the phase includes the shift ±b·log n.

**Verification.** Compared against direct quadrature at (k, k′) = (1,3), u = log 2: relative error of 1e−41 to 4e−40 across the six T.

## 2. ζ (requests c and d)
| T | N(T) | n₋(𝔪) total | n₋(𝔪) even/odd | n₋(𝔄_ev): N / 2N / 4N | minimum eigenvalue 𝔄_ev | cos(v_min, χ_ev) | n₋(𝔄_odd) |
|---|---|---|---|---|---|---|---|
| ½log3 | 2 | 2 | 1/1 | 1/1/1 | −1.81 / −2.02 / −2.09 | 1.0000 / 0.99999 / 0.9959 | 0 |
| 1 | 4 | 4 | 2/2 | 1/1/1 | −3.85 / −4.09 / −4.18 | 0.99999 / 0.99999 / 0.9984 | 0 |
| ½log5 | 3 | 3 | 2/1 | 1/1/1 | −3.02 / −3.14 / −3.24 | 0.99999 / 0.99999 / 0.9987 | 0 |
| ½log15 | 5 | 5 | 3/2 | 1/1/1 (+1 tiny) | −5.77 / −5.98 / −6.14 | 0.99999 / 0.99998 / 0.99992 | 0 (+1 tiny) |
| 2 | 8 | 8 | 4/4 | 1/1/1 (+5 tiny) | −10.3 / −10.8 / −11.0 | 0.99999 / 0.99998 / 0.9998 | 0 (+5 tiny) |
| 3 | 12 | 12 | 6/6 | 1/1/1 (+7 tiny) | −23.8 / −24.9 / −25.4 | 0.99999 | 0 (+7 tiny) |

- **Theorem A∞ check.** n₋(𝔪_N) = N(T) **exactly** at the 6 T, with split ⌈N/2⌉ / ⌊N/2⌋.
- **cor:H1minus check.** n₋(𝔄_ev) = 1 at all T and all three sizes, if the ~1e−15 eigenvalues are counted separately.
  - **The complement E_N^⊥ is not needed:** the cancellation of N − 1 directions happens **inside E_N**.
  - The odd sector remains ≻ 0. Its floor decreases with N (6.7e−3 → 7e−7 → 3e−12 at T = 1), consistent with a truly tiny floor (CALIB_R4).
- **The negative eigenvector is the polar direction.** cos(v_min, P_{E_N}χ_ev) ≥ 0.998 throughout; above 0.9999 at N(T).
- **The "tiny" ones.** These are the almost-exactly-cancelled directions, of size ≈ 1e−15 to 1e−17. Their sign is not resolved by this quadrature. This figure becomes the bottleneck for N ≥ 2N(T).

## 3. Epstein and a_P (request f)
**Epstein (own archimedean):**
- **Up to T = ½log15:** n₋(𝔄_ev) = 1 and 𝔄_odd ≻ 0. There is little cancellation because n₋(𝔪) is already small: 1 in the even sector and 0 in the odd sector up to T ≈ 1.6.
- **T = 2, even inertia:** n₋(𝔄_ev) goes from 1 (N, 2N) to **2 (4N = 32)**; the second eigenvalue is −1.47.
- **T = 2, odd sector:** at 4N an eigenvalue −1.05 appears.
- **T = 3:** the even sector gives 1 / 2 / 3, and the odd sector has eigenvalue −7.6e−7, −0.014 and −7.46 at N, 2N and 4N.
- **Where the inertia changes.** Going from N to 4N adds sines of k > N(T), i.e. of frequency τ_k > t₀. **Epstein's hyperbolic pair (H1PLUS) lives at frequencies above t₀**: with k ≤ N(T) it is not seen.

**a_P (P = {2}, archimedean of ζ):**
- **There is no cancellation** at any T.
- n₋(𝔄_ev) is greater than or equal to n₋(𝔪): 1/1/1, 2/3/3, 2/2/2, 3/4/6, 4/6/9 and 5/9/16, and grows with N.
- The odd sector also has n₋ ≥ 1 at all T, with floor ≈ −0.30 … −0.57 stable in N.
- **Reading.** Removing the 2 leaves all the negative archimedean directions intact and creates new ones above t₀ (k > N(T)).
- The minimum eigenvector remains the polar direction (cos ≥ 0.988).

## 4. Not done and limits
- **The sign of the ~1e−15 eigenvalues** in ζ for N ≥ 2N(T). Requires more precision in the Lévy integral: tanh-sinh or a closed form for ∫(c(0) − c(u))K. Not done.
- **The exact localization in k** of Epstein's and a_P's inertia change. It is only bounded to the band k ∈ (N, 4N]; the eigenvectors were not projected onto each k.
- **DH.** Not requested in this piece.
