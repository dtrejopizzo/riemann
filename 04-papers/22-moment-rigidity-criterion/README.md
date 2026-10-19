# Paper 22 — The Riemann Hypothesis as moment rigidity over Meixner–Pollaczek polynomials

Let m_∞ be the archimedean spectral probability measure (2π)^{−3/2}|Γ(¼+is/2)|² ds from the work of Connes, Consani and Moscovici, with orthonormal polynomials P_n (a rescaled Meixner–Pollaczek family). Let ζ_on be obtained by projecting every nontrivial zero horizontally onto the critical line, and let ν = (|ζ(½+is)|² − |ζ_on(½+is)|²) m_∞. The paper proves unconditionally that ν is a finite, non-negative, even measure with all moments finite, and that RH is equivalent to constancy in n of Δ_n = ∫ P_n² dν. The proof uses triangularity, Carleman's condition and Hardy's theorem; no orthogonal-polynomial asymptotics or kernel positivity. It is an equivalence, not a proof.

## Main results
- `prop:mp` (Meixner–Pollaczek identification): Jacobi coefficients a_n = ½√((2n+1)(2n+2)). PROVED.
- `prop:positivity` (Pointwise domination; vanishing iff RH): ν ≥ 0, ν = 0 ⟺ RH. PROVED.
- `prop:moments`: ν finite, even, all moments finite. PROVED.
- `thm:rigidity` (Moment rigidity): constant Δ_n forces ν = c·m_∞ (Carleman determinacy). PROVED.
- `thm:main` (RH as moment rigidity): RH ⟺ Δ_n constant in n. PROVED (equivalence; Hardy's theorem CITED).

## Files
- `main.tex`, `main.pdf` — source and compiled paper.

## Relation to other papers
- The measure ν is the one studied in Paper 24; the criterion is invoked there as the moment-rigidity criterion.
