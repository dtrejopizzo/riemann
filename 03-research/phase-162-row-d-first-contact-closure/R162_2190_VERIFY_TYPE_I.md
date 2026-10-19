# R162_2190 — Numerical verification of R162_2001 (Type I first contacts on the two-atom comb)

Referee pass. **All numbers are UNCERTIFIED double-precision float.** No sign or label is claimed or moved.
Scripts were kept in a scratch directory and are not in the repo: `cosv.py` (operator), `run2.py` (T_*, Type I root),
`run3.py` (first-contact scan, s₂=1 row).

## Verdict: CONFIRMED (float level)

A different discretization reproduces the R162_2001 Type I point and the s₂ = 1 near-alignment. On the row s₂ = 1 the
margin collapse is real and does not come from the discretization or the constraint.

## 1. Form audit (t2001_typeI_search.py and t1601_nodal_rerun against Paper 47 eq:symbol/eq:form/eq:W)

- Comb weights: w_n = 2Λ(n)/√n = v_n of eq:symbol. The symbol is m − Σ v_n cos(τ log n), and the comb enters as −s_n·v_n.
  The gate log n < 2T matches N_T. This is correct.
- Legendre prefactor: F̂ of the normalised P_l(t/T) is 2T(−i)^l j_l(τT)·√((2l+1)/2T). So (1/2π)∫_ℝ = (1/π)∫_0^∞, which gives
  (2T/π)√(2a+1)√(2b+1)·i^{b−a}. The `sign` matrix is i^{b−a} on same-parity pairs. This is correct.
- Tail: j_a j_b averages to cos((b−a)π/2)/(2x²), so the tail of G is sign·∫m/(2t²T²). After the outer `sign` it adds a
  positive contribution to the block. This is correct, and it is the R162_1590 fix. No abs() remains.
- Primitive constraint: for even F, A(F)=B(F) and P_T ⟺ ∫F cosh(t/2)=0. The vector used is φ_l = √((2l+1)/2T)·2T·i_l(T/2). This is correct.
  The constraint is imposed by exact QR projection. It enters **only λ** (and therefore T_*). μ₂, u₂ and ⟨u₂,φ̂⟩ are
  computed from the unconstrained A^ev.
- Sign convention: u₂(0⁺) > 0 only fixes the sign. The Type I statement (μ₂ = 0 and ⟨u₂,φ̂⟩ = 0 at the same T) does not
  depend on it, because |⟨u₂,φ̂⟩| itself passes through 10⁻¹⁵.

## 2. Independent re-implementation

- Basis: even cosines on [−T,T], e_0 = (2T)^{−1/2}, e_k = T^{−1/2}cos(kπt/T), N = 60…320.
  F̂_k = T[sinc((τ−κ)T)+sinc((τ+κ)T)], with no Bessel functions.
- τ-quadrature: Gauss–Legendre, 20 nodes per panel of width 1.5, on [0, 20000]. The analytic mean tail is (2/π)(−1)^{j+k}e_j(0)e_k(0)∫_L^∞ m/τ².
- The comb uses the same τ-space formula. φ coefficients are in closed form: 2∫_0^T cos(κt)cosh(t/2)dt.
- Convergence is slower than Legendre, about N^{−1.5} in λ, because of the cosine boundary behaviour. Richardson extrapolation is used where needed.

| quantity | cosine basis | R162_2001 Legendre (K=34/46) | agreement |
|---|---|---|---|
| λ(T=0.59; 0,0) | 0.0099799 (N=320), extrapolated ≈ 0.009970 | 0.0099775 / 0.0099714 | ~2e-6 (5 digits) |
| ⟨u₂,φ̂⟩(0.59; 0,0) | −0.1365245 (N=320) | −0.1365245 / −0.1365249 | 6 digits |
| T_*(0,0) | 0.595841 / 0.595830 / 0.595825 (N=120/180/240), extrapolated ≈ 0.59581 | 0.59582 | 4–5 digits |
| s₂^c (s₃=0) | 0.99976781 / 0.99976781 (N=120/180) | 0.99976734 / 0.99976760 | ~2e-7 (6 digits) |
| T_c (s₃=0) | 0.592948 / 0.592939 (N=120/180), decreasing | 0.59310 / 0.59304 | ~1e-4 (3–4 digits); T_c is the least stable output in both codes |
| g(0) at Type I | −0.40942 | −0.4093 | 4 digits |
| μ₁, μ₃ at Type I | −2.31546, 0.54577 | −2.3157, 0.5458 | 4 digits |

**Sign change at s₃ = 0.** The table gives h(T) = ⟨u₂,φ̂⟩ at the s₂ for which λ(T;s₂)=0 (N=240; N=120 and 180 agree to ≤ 4e-7 in h):
T=0.585: +1.9955e-4 (s₂=1.003211), T=0.590: +8.60e-5 (s₂=1.001276), T=0.593: −2.08e-6 (s₂=0.999731), T=0.600: −2.66e-4 (s₂=0.994908).
At every point μ₂ ≈ ⟨u₂,φ̂⟩²/|g(0)| (Type II law). At the root, λ = μ₂ = ⟨u₂,φ̂⟩ = 0 to 1e-15, μ₂ is simple (gap 0.55 to μ₃
and 2.3 to μ₁), and g(0) = −0.409 < 0. The Type I characterisation of R162_1901 Thm 1 is therefore reproduced.

**First contact.** At s₂ = 0.99977, s₃ = 0 (N=120), λ on the grid T = 0.30, 0.33, …, 0.57 is positive and decreases
monotonically (0.692 → 0.00081). The scan step is 0.03, which is coarser than R162_2001's 0.004. This is not a proof that no earlier zero exists in (0.54, 0.593),
where λ is only ~1e-3.

## 3. The row s₂ = 1: real, not an artifact

Cosine basis, N = 120:
- s₃=0: T_* = 0.592530, μ₂ = 4.20e-10, ⟨u₂,φ̂⟩ = +1.312e-5. R162_2001 has 0.5927 / 4.2e-10 / +1.3e-5.
- s₃=2.5: T_* = 0.557187, μ₂ = 5.01e-11, ⟨u₂,φ̂⟩ = +4.652e-6. R162_2001 has 0.55734–0.55743 / 4.99e-11 / +4.67e-6 to +4.69e-6.
- φ is **not** close to an eigenvector. ‖Aφ̂ − (φ̂·Aφ̂)φ̂‖ = 0.44 (s₃=0) and 0.31 (s₃=2.5). The overlaps of φ̂ with u₁, u₂, u₃, u₄
  are (0.993, 1.3e-5, 0.064, −0.075). So φ̂ lies mostly along u₁ with O(0.07) leakage, and only the u₂ overlap is tiny.
- The constraint cannot create the collapse, because μ₂ and u₂ are unconstrained quantities (§1). The collapse is simply
  μ₂(T_*) ≈ ⟨u₂,φ̂⟩²/|g(0)| (Type II law) evaluated 2.3e-4 (s₃=0) or 7e-5 (s₃=2.5) in s₂ from the Type I curve. The slope is
  dh/ds₂ ≈ 0.056, so 1.3e-5 is exactly what the distance predicts. **Why** the Type I curve sits within 10⁻⁴ of the
  arithmetic weight s₂ = 1 is not explained by either code. That is a structural question (Perron–Tate near-alignment, 1701/1803) and not a numerical defect.

## 4. Residual caveats (audit)

- Everything is float. The sign margin |h| ~ 1e-5 at |s₂−1| ~ 2e-4 is 20–100× the cross-discretization spread (≤ 5e-7 in h).
  That is enough for a float confirmation, but it is not a certificate.
- T_c differs by ~1e-4 between the two codes. s₂^c agrees to 2e-7. So the curve's T-parametrisation is soft and its s₂-location is firm.
- Not re-checked here: the s₃ ≠ 0 Type I points (only the s₂ = 1 row at s₃ = 2.5 was checked), the (0.75,0) small-margin region, and K=46 grid entries.
