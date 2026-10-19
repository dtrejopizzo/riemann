# 2b part (i): the localized form is an EXACT restriction — CLOSED ## Theorem (i)
For every λ>1, the localized Weil form A_λ coincides with the full Weil form A_∞
restricted to the subspace E_λ (functions supported on [λ⁻¹,λ]): **A_λ(f,g) = A_∞(f,g) ∀ f,g ∈ E_λ.** ## Proof
A_∞ = M_θ − Σ_{all n} Λ(n) T(n), with ⟨f|T(n)g⟩ = n^{−1/2}((f**g)(n)+(f**g)(n⁻¹)).
If f,g ∈ E_λ (support [λ⁻¹,λ]), then f**g has support in [λ⁻²,λ²] (multiplicative convolution
adds supports). Therefore (f**g)(n)=0 for n>λ², i.e. ⟨f|T(n)g⟩ = 0 for all n > λ².
Thus on E_λ only the primes p^k ≤ λ² contribute, which are exactly those of A_λ. ∎ **Verified numerically** (exact_i.py): max|QW[primes≤λ²] − QW[primes≤100]| = 0.00e+00
(exact) on E_λ. (log 17/L = 1.083 > 1: prime 17 falls outside the support [0,L]; log 13/L
= 0.980: 13 is the last one inside.) ## Consequence: 2b is NOT a tail perturbation of primes This **corrects** the previous picture (that (i) was "PNT-controlled"). There is no prime
tail to bound: the truncation is EXACT by support. Then: - A_λ = A_∞|_{E_λ}, and E_λ ↑ L²(0,∞) as λ→∞ (the subspaces grow, nested).
- The ground state ξ_λ = minimizer of A_∞ over E_λ = **Galerkin/Rayleigh–Ritz approximation** of the bottom of A_∞ by growing subspaces.
- ε_0(λ) ↓ inf σ(A_∞) monotonically (min-max). inf σ(A_∞) = 0 ⟺ RH (Weil positivity). **2b reduces to Galerkin convergence of the minimizer to a NON-isolated bottom** (the
eigenvalues accumulate at 0 — exponentially small gaps). That is the hard case of
Galerkin theory, and is where all the content of 2b lives. (i) is zero-independent and
exact; the real game is in (ii).
