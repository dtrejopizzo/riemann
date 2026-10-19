# R162_791 — Audit of R162_703 §3 (D3: complete Weil form certified at T = ½log5)

Scope: Theorem 3.1 of R162_703 — W_{T₀} ≥ 10⁻¹⁸ on L²_ev(I_{T₀}) and ≥ 10⁻¹⁶ on
L²_odd(I_{T₀}), T₀ = ½log5 — and `scripts/c3/d3_cert_W.py` with its outputs. No commits were made.

## Verdict: **CERTIFIED** (with cosmetic remarks only; none affects the bound)

## 1. Complete-form definition vs Paper 47

- eq:W: W_T(F) = 𝔞_T(F) + 2 Re(A(F) B̄(F)). thm:parityschur(o): on real F this equals
  [𝔞_T(F_e) + 2ℓ_ev(F_e)²] + [𝔞_T(F_o) − 2ℓ_odd(F_o)²]. So W_par = 𝔞_T + 2ε_par ℓ_par², with
  ε_ev = +1, ε_odd = −1 and φ_ev = cosh(t/2)1_I, φ_odd = sinh(t/2)1_I ✓.
- Bordered form b(F,ξ) = b_μ(F) + 2ξℓ(F) + cξ², c = −ε/2:
  - odd, c = +½: min_ξ b = b_μ − 2ℓ² = (lower bound of) W_odd − μ‖F‖² ✓;
  - even, c = −½: b = b_μ + 2ℓ² − ½(ξ − 2ℓ)². The substitution η = ξ − 2ℓ(F) is a congruence that
    splits b into (b_μ + 2ℓ²) ⊕ (−½η²). So n₋(b) = n₋(b_μ + 2ℓ²) + 1 ✓.
  Code: `cxi = +1/2 if par == 1 else -1/2` ✓. The sign is correct in both parities.
- The pole term is represented exactly, not truncated. χ_l = √((2l+1)/2T)·2T·i_l(T/2). This is
  ∫P_l(x)e^{ax}dx = 2i_l(a), restricted to parity. Its norm is ‖φ_ev‖² = sinh T + T and
  ‖φ_odd‖² = sinh T − T. I re-derived both ✓. The χ components on the explicit Y₁ block
  (K ≤ l < K₂) enter exactly. The tail l ≥ K₂ enters through ‖P_{≥K₂}χ‖, computed as the exact norm
  minus the partial sum, clipped to ≥ 0 ✓.
- The ξξ entry is c − δ′ with δ′ = sup(‖P_Yχ‖²/q_Y) ≥ the true Schur term. Lowering one diagonal entry
  can only lower the form, so the inequality points the right way ✓.

## 2. Inertia and sector coverage

- The rows are all parity-par Legendre indices, split as E = {l < K}, Y₁ = {K ≤ l < K₂}, and the
  tail {l ≥ K₂}. The tail enters through the Λ*_{K₂} box (β) and the P_{≥K₂}χ box. E ⊕ Y is the whole of
  L²_par(I_T). The certificate is therefore on the full parity sector, not on P_T ✓.
- b_Y ≥ q_Y = 0.70079 > 0 gives b_Y⁻¹ ≤ q_Y⁻¹. Then the true Schur complement 𝔰 onto E ⊕ ξ
  satisfies 𝔰 ≥ 𝖱′ (R162_391 §2 argument, unchanged here). Since b_Y > 0, n₋(b) = n₋(𝔰) ≤ n₋(𝖱′).
- Odd sector: interval Cholesky of the whole (d+1)×(d+1) matrix 𝖱′ has all pivots > 0. So 𝖱′ ≻ 0,
  b ≥ 0, and W_odd − μ ≥ 0 ✓.
- Even sector: H is exact binary64 with ‖HᵀH − I‖_∞ < 1 certified, so diag(H,1) is a congruence.
  det B < 0 is certified, so inertia(B) = (1,1). The Haynsworth Schur complement S passes interval
  Cholesky. Hence n₋(𝖱′) = 1, so n₋(b) ≤ 1, n₋(b_μ + 2ℓ²) = 0, and W_ev − μ ≥ 0 ✓.
- The remaining machinery is unchanged from c3_cert.py, which R162_391 already certified: the
  truncated symbol minorant, the Gram and tail boxes, and the Trefethen quadrature bound. I checked
  the diff: the only changes are the docstring, the ξξ entry, the odd Cholesky branch, disabled
  diagnostic dumps, and the output names.

## 3. Rerun (independent, in scratchpad, same arguments)

`python3 d3_cert_W.py log5 <0|1> 0,1e-20,1e-18,1e-16,1e-14,1e-12 240 640 280 330 46`
took about 375 s per parity. The outputs are **bit-identical** to the stored JSONs in every field
except `seconds`.

| sector | μ certified | min pivot | max radius of 𝖱 |
|---|---|---|---|
| even | 0, 1e-20, **1e-18** (fails at 1e-16) | [4.473075643e-4 ± 4.4e-14] | 4.36e-41 |
| odd | 0, 1e-20, 1e-18, **1e-16** (fails at 1e-14) | [8.144e-14 ± 7.4e-25] at 1e-16 | 4.37e-41 |

The odd margin is small (≈8e-14) but its radius is 11 orders of magnitude smaller, so the result is
rigorous. A failed μ is not evidence of negativity; R162_703 correctly makes no claim there.

## 4. Rigour of the enclosures

- Every quantity is an Arb ball at 640 bits: ψ, the Bessel functions j_l and i_l, the Gauss–Legendre
  nodes and weights (`legendre_p_root`), log n, and π.
- The comparisons (`>`, `<`) are Arb predicates, which are true only if they hold for the whole ball.
- s_inf is a dyadic strictly below the certified lower end.
- The Bessel ball width is asserted < 1e-60.
- The quadrature error is added as a ball to every G entry.
- The Λ* tail is geometric, with a 2·term bound.
- The only floating-point object is H. It is used as an exact matrix, and its invertibility is
  certified. ✓

## Cosmetic remarks (no effect on the bound)

1. The odd-branch JSON omits s_inf, ω±, the quadrature error and β. They are identical to the even
   run, but for self-containment they should be printed.
2. In the docstring, "Original docstring follows" leaves two headers. This is harmless.
3. In the R162_703 §3 table, the odd "min pivot 8.3·10⁻¹⁴" is the value at μ = 0. At the claimed
   μ = 10⁻¹⁶ it is 8.14·10⁻¹⁴, so the table should state which μ it refers to.
