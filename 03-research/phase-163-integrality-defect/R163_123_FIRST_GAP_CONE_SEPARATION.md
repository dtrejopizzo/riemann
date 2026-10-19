# R163_123 — Two tests on the same gap, two incompatible cones

**Status:** cone separation proved; does not close Row D. It makes explicit why `R163_117`'s negative detector cannot be obtained as a positive square/autocorrelation of the class used by Weil-type and PC-ren arguments.

## 1. The positive-definite test of R163_116

For `0<b<1/10`, `R163_116` builds

```
f_b(u)=[e^{−|u|/b}−e^{−1}]_+,
B_δ(u)=2[cosh(δu)−1]/(δ²u²).
```

It proves `\widehat{f_b B_δ}(γ)>0` for every `γ∈ℝ`, `0≤δ≤1/2`. In particular `f_b` is positive-definite (non-negative Fourier transform) and, for the stripped current `r=Σ_j δ_j² B_{δ_j}\cos(γ_j u)`,

```
⟨r,f_b⟩=Σ_jδ_j²\widehat{f_bB_{δ_j}}(γ_j)>0
```

if quartets exist. Extending the pairing from smooth tests is justified in `R163_116`; the contact term at `u=0` is excluded by the `o(T)` weighted mass.

## 2. The negative test falls outside the cone

For `b=1/2`, `R163_117` uses `H_b(u)=|u|(b−|u|)_+²`, also non-negative and supported within the first prime gap. However,

```
\widehat{H_bB_δ}(γ)<0   for |γ|≥14,
⟨r,H_b⟩<0              if effective quartets exist.
```

In particular `\widehat{H_b}(γ)<0` for `|γ|≥14` (take `δ=0`), so `H_b` is **not** positive-definite. There is no representation

```
H_b=Σ_i c_i(φ_i*\tilde φ_i),   c_i≥0,
```

not even as a distributional limit of such sums: every term's Fourier transform is non-negative, and the cone of positive-definite distributions is closed under distributional convergence. The same obstruction holds for `H_bB_δ` for every `δ≤1/2`.

## 3. Design consequence for the arithmetic gate

The two tests are non-negative in the physical variable and live before `log2`; they differ in the **sign of the Fourier transform at the heights where exterior zeros might exist**. The positivity of a Weil form over autocorrelations, or a square of `(PC-ren)`, only controls the positive-definite cone. By pure decomposition into squares with positive coefficients, it cannot produce an opposite inequality for `H_b` or `R163_117`'s localized negativity.

This is not a NO-GO for every possible construction: a new identity could contain an **oriented, signed** term transporting information from the squares cone to the `H_b` test, while preserving the Euler defects and the polar/Tate corrections. But that transport must be proved independently; replacing `H_b` with a square removes precisely the sign that distinguishes the quartets. The Epstein/DH and Beurling–DMV models remain mandatory tests for that transport.
