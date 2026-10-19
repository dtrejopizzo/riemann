# CA_D_SYNTHESIS — Front D (phase / Hardy-function area), phase 193

Pen and paper; no numerics. **No sign contact. No negative value for ζ. No clause of (R) moved.**

## Seeds and verdicts (CA_D_000; no wrong keep or discard)
| seed | verdict |
|---|---|
| D1 first moment of e^{iΘ}F̂ (Mandel / time delay) | coordinate, (B″), linear in Θ |
| D2 Hardy-amplitude transfer | PROVED tool (CA_D_001); FE-class generic, so not a sign step |
| D3 Landau / positive coefficients of Z_X (lead (a)) | DEAD, retry of R164_102 (W-Landau) |
| D4 Kramers–Kronig / DtN | (R)(4) or Cauchy–Riemann coordinate |
| D5 Riemann–Siegel FM (lead (b)) | DEAD, R163_603; linear |
| D6 scattering causality | ⟺ zero-free half-plane, (R)(4) |
| D7 de Branges / Kreĭn | Θ′ not pointwise positive; certificate (thm:Z) |
| D8 amplitude-exponent homotopy | non-integer powers need zero information; integers do not decide α = 0 |
| D9 density of the transferred cone | NO-GO, PROVED (CA_D_002) |

## PROVED tools
- **Thm 1 (CA_D_001).** For F ∈ P_T: (1/π)∫Θ_X′|F̂|²Z_T² = 2∫_T^∞u|R_F|² ≥ 2Tρ_F, with ρ_F = (1/2π)∫|F̂|²(Z_T²−1) ≥ 0. Inputs: the Euler gap,
  the FE phase identity, and the Tate condition cancelling the pole at abscissa ½.
- **Mean-value inequality (Cor 1.1).** ∫|F̂|²|ζ(½+iτ)|²e^{−2C_X(τ)}dτ ≥ ∫|F̂|² on P_T.
- **Thm 1′.** The same for the powers Z_T^{2k}, with Tate conditions of order k.
- **Thm 1″.** The same for every real FE Dirichlet series with at most a simple pole at 1 (DH, Epstein, ζ_K). Hence it is not ζ-specific.
- **Lead (a).** The sign of z_X is never used; only the gap matters.
- **Thm 2 (CA_D_002).** The vague closure of the transferred cone (bounded powers, bounded mass and energy) meets the P_T-densities only
  in {0}. Selberg and Jensen CITED, used only inside this NO-GO.
- **Thm 2′ (zero-free).** Elements of the closure are smaller than ε·6.6e^{−√2B_X} on the central cell |τ| ≤ π/(8T).

## Residuals and why they are dead (CA_D_003 §2)
- Statements at the on-line ordinates: (R)(4).
- Tests concentrated on the central cell: none exist in P_T; soft localization is W-loc, (R)(5).
- The centre packet γ = 0: exactly critical, retry.
- The split by Z_T²: REF-D.
- The unimodular factor e^{−iΘ} alone: coordinate D1.

## The s_w family (CA_D_003 §1)
Transfer does not apply, for three reasons, each PROVED: the family is an amplitude-one statement; it lacks the e^{−C_X} amplitude; and its
phase is −θ, not −Θ_{X′}. The exact split is
  πQ_M = c²[∫θ′F̂₀²|ζ|²] − c²∫comb_{X′}·F̂₀²|ζ|² + (polar P_M terms) + (ρ_M terms).
The bracket is ≥ 2T₀c²∫F̂₀²(|ζ|²−1) ≥ 0 (PROVED, FE-generic).
**ARGUED:** the bracket is not critical. The M^{−3} criticality lives in the last three terms, at bounded height on the central cell.

## Conclusion
In the phase picture, row D lives on {|ζ/Z_{<X}| < 1}, in particular on the central Nyquist cell where the comb is coherent. This is
consistent with (R)(7) and R9. No admissible candidate remains in this area. Front D stops.
