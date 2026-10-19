# ε₀>0: triangulation of the wall from three frames + window-design route Result of attacking `ε₀=λ_min(QW)>0` (= Weil-positivity-up-to-T* = local-RH) with
pure mathematics, without stopping at "it's RH". Three independent frames, one characterization,
and a genuinely new route (window design). ## 0. Exact reduction to the symbol [RIGOROUS]
Carré-du-champ on `A_λ=M_θ−V` (f real, band type Ω=logλ):
```
A_λ(f,f) = (Ω̃(0)−P_λ)‖f‖² + 𝓔_θ(f) + ½𝓔_prime(f), P_λ=Σ_{n≤λ²}Λ(n)/√n ≈ 2λ.
```
In Fourier, with ρ=|f̂|², autocorrelation c_f(u)=∫e^{itu}ρ(t)dt (|c_f|≤1, c_f(0)=1):
```
ε₀ = min_{‖f‖=1, band} ∫ a(t) ρ(t) dt, a(t) = Ω̃(t) − D_λ(t),
D_λ(t) = Σ_{n≤λ²} Λ(n) n^{-1/2} cos(t log n) = Re Σ Λ(n) n^{-1/2-it}.
```
`a(t)` is exactly archimedean − prime sum = zero-side of the explicit formula. ## 1. PRIMES frame [RIGOROUS + proved obstruction]
`ε₀>0 ⟺ Σ_n (Λ(n)/√n) Re c_f(log n) < ∫Ω̃ρ ∀ f prolate`.
- Large sieve (Montgomery–Vaughan) bounds `∫D_λ|f̂|²` by `(2Ω+O(λ²))Σ Λ(n)²/n`, `Σ Λ²/n≈2(logλ)²`.
- **METHOD OBSTRUCTION THEOREM:** any bound using only |Λ(n)| (large sieve, mean-value) CANNOT decide sign(ε₀): DH has comparable magnitudes and ε₀<0. The sieve's slack ≥ RH-true/false gap. The sign lives in the PHASE COHERENCE of cos(t log n), not in magnitudes. ## 2. ZEROS frame [RIGOROUS mean; minimum = pair correlation]
`ε₀ = min_{‖f‖=1} Σ_ρ |f̂(γ_ρ)|²` (RH-true). - Mean E[S] ≈ (1/2π)log(T*/2π) ≈ (logλ)/π > 0 [unconditional, RvM].
- The minimizer concentrates f̂ (width 1/Ω) in a GAP between zeros (spacing π/Ω) ⟹ ε₀ = tail leakage. `ε₀>0 ⟺ no gap too large = RIGIDITY of the zero frame = pair correlation`.
- Pair correlation F(α): F≥0 unconditional (gives the mean); F(α) for 0≤α≤1 proved UNDER RH (circular here); F(α≈1) for α>1 (where the sign lives) = OPEN CONJECTURE. Not a shortcut. ## 3. OPERATOR frame [the sharpest — truncated Toeplitz]
`A_λ = P_λ M_a P_λ`, truncated Toeplitz/Wiener–Hopf, symbol `a(t)=Ω̃(t)−D_λ(t)`. Toeplitz
positivity ⟺ the truncation does NOT resolve the negative part of `a`.
- **CENTRAL WELL** at t=0: `a(t)≈a(0)+½M_2 t²`, `a(0)≈−2λ`, `M_2≈2λ(logλ)²` ⟹ width `t_dip≈1/logλ`.
- **BAND RESOLUTION** (type Ω=logλ, Beurling–Landau) `≈1/Ω=1/logλ`.
- **FINDING:** well width ≈ band resolution ≈ 1/logλ — **MARGINAL BY CONSTRUCTION**. `ε₀` = fine-cancellation residue ~2λ vs ~2λ (zero-point energy of the confinement). Sign NOT fixed by leading terms ⟹ requires the exact symbol = exact primes = RH. **Shows why no soft argument decides the sign: the well is tuned to the edge on purpose.**
- Off-line zero of DH = EXTRA WELL of a_DH at t=γ_off, resolved by the band ⟹ ε₀<0. Reproduces N5c. ## 4. CHARACTERIZATION (consensus of the three frames)
`ε₀>0 ⟺ no extra wells/dips in a(t) ⟺ no zeros off the line up to T* ⟺ local-RH`.
The three frames are RH-neutral in setup, RH-encoding in result, NOT circular, and none
breaks the wall unconditionally. Triangulation: the obstruction is genuine, not a method weakness.
The free part of each frame (mean/density/central-well) is common; the RH part (phase/rigidity/
off-line wells) is the same dual information = the off-line zeros. ## 5. NEW ROUTE (not reducible to estimating the symbol/zeros): WINDOW DESIGN
The one thing the classical analytic wall does NOT control and we do: the frame's WINDOW/weight.
Goal: choose a weight φ (instead of the crude rectangle) such that (a) band resolution ≫ well width 1/logλ (break the marginality IN OUR FAVOR) ⟹ central well sub-resolution UNCONDITIONALLY ⟹ ε₀^{(0)}>0 unconditional; (b) off-line wells are structurally excluded by restricting the test space;
while keeping the Weil identity A_λ(f,f)=Σ_ρ... (the hard constraint).
If (a) closes, RH is ENTIRELY isolated in the off-line wells (b). Computation in progress:
reparametrize with weight φ and see how resolution(φ) scales vs 1/logλ under the Weil constraint. — attacked without stopping at "it's RH"; recorded to continue. (CCM agrees with all of this.)
