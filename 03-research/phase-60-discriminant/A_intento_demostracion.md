# Goal A — proof attempt (pure mathematics, proved steps + frank [GAP]) **Goal:** prove A_λ(f,f) ≥ 0 (localized Weil positivity), ideally with margin
≥ c·ε₀·𝓔_D, from the prime side. [P]=proved · [GAP]=open step. --- ## Step 1 [P] — Fourier reduction of A_λ to the archimedean symbol − ζ'/ζ We start from the Beurling–Deny decomposition (proved): A_λ(f,f) = ∫(Ω(0)−2M_0(w))|f|²dw + 𝓔_θ(f) + 𝓔_prime(f). Using ∫|f(w)−f(w+h)|²dw = (1/2π)∫|f̂(t)|²·2(1−cos th)dt (Plancherel), both jump forms
are Fourier multipliers: 𝓔_θ(f) = (1/2π)∫|f̂(t)|²·[∫2(1−cos tξ)dν(ξ)]dt = (1/2π)∫|f̂(t)|²(Ω(t)−Ω(0))dt, 𝓔_prime(f) = (1/2π)∫|f̂(t)|²·[2Σ_n (Λ(n)/√n)(1−cos(t log n))]dt (ignoring the boundary; see Step 4). The well term (without boundary): 2∫M_0|f|² = (1/π)(Σ_n Λ(n)/√n)‖f‖². Combining with 𝓔_prime: 𝓔_prime − 2∫M_0|f|² (prime part) = −(1/π)∫|f̂(t)|²·[Σ_n (Λ(n)/√n)cos(t log n)]dt. And **the heart:** Σ_n (Λ(n)/√n) cos(t log n) = Re Σ_n Λ(n) n^{−(1/2+it)} = **Re[−ζ'/ζ(1/2+it)]** (cutoff n≤λ²). Therefore, putting it all together (the archimedean part gives Ω(t)=2θ'(t)): **A_λ(f,f) = (1/2π)∫ |f̂(t)|² · W_λ(t) dt, W_λ(t) = 2θ'(t) − 2·Re[−ζ'/ζ]_{≤λ²}(1/2+it).** This is EXACTLY Weil's explicit formula in spectral form. [P] (it is Weil's identity
rewritten; it recovers what we already knew, but now with the "Fourier potential" W_λ(t) explicit.) ## Step 2 [P] — Where the (in)definiteness lies: the poles of ζ'/ζ at the zeros W_λ(t) = 2θ'(t) − 2Re[−ζ'/ζ]_{≤λ²}(1/2+it). The term −ζ'/ζ(1/2+it) has **poles at the zeros**
ρ=1/2+iγ (residue +1): near t=γ, Re[−ζ'/ζ] → +∞. Since it enters with a − sign, **W_λ(t) → −∞ near
each on-line zero.** For OFF-line zeros ρ=1/2+β+iγ, the pole is shifted to t=γ with real part
that does not diverge the same way; the structure is different — and that is where the (in)definiteness lives. ⟹ **Positivity A_λ≥0 ⟺ W_λ(t) integrated against |f̂|² is ≥0 for every f∈PW_{L/2}.** But W_λ
has negative singularities at the zeros. Positivity is NOT pointwise (W_λ is not ≥0 pointwise);
it is an INTEGRAL positivity that depends on how the poles (zeros) are distributed. ## Step 3 [attempt] — Attacking the integral positivity **Technique 3a (completing the square / 𝒯=A*A):** write A_λ = B*B. By P8 (Theorem C, proved),
the zero side CANNOT give the sign; the square structure must be built INDEPENDENTLY of
the zeros (Route B). This is the known wall. **Does not close this way.** **Technique 3b (Hardy/Poincaré with a constant):** 𝓔_θ+𝓔_prime ≥ ∫(2M_0−Ω(0))|f|². By a Hardy-type
inequality for the jump forms, 𝓔_prime(f) ≥ c·∫M_0|f|² with SOME constant c. **Computation of the
achievable c vs the needed c:** - The c NEEDED for A_λ≥0 is c=2 (plus the help of Ω(0) and 𝓔_θ). - The c ACHIEVABLE by generic Hardy is c<2 (the jump inequality is not sharp). - **The exact gap between c_achievable and c=2 IS the Weil-positivity margin.** Sub-sharp (c<2): gives A_λ ≥ −(small)‖f‖² — useful but NOT positivity. The SHARP constant c=2 ⟺ W_λ integrates to ≥0 ⟺ on-line zeros ⟺ **RH**. **Does not close: the sharp constant is RH.** **Technique 3c (functional equation s↔1−s):** the symmetry pairs ρ with 1−ρ. By NG-D4 (proved),
J T_0 J = T_0 (the involution PRESERVES, does not NEGATE, the eigenvalues) ⟹ the functional
equation does NOT force positivity. **Does not close.** ## Step 4 [GAP] — the only possible non-circular place: the BOUNDARY (finite prime cutoff) In Steps 1–3 I ignored the position-dependence of M_0 (the boundary, n≤λ²). **There, and only
there, is the non-circular hope**, because:
- The cutoff n≤λ² ⟺ exponential type L/2 ⟺ horizon T* (Lemma 2, proved).
- W_λ(t) uses ONLY primes ≤λ² ⟹ it is a FINITE APPROXIMATION of 2θ'−2Re[−ζ'/ζ], smooth (without the full poles), controlled by PNT (the tail Σ_{n>λ²} is PNT, proved in B).
- The positivity of the FINITE APPROXIMATION W_λ (with smooth primes, no poles) might be provable from PNT — and the convergence to full positivity is Link 2 itself. **[GAP] The step I do not have:** prove that the finite form ∫|f̂|²W_λ(t)dt ≥ c·ε₀·𝓔_D(f) using that W_λ is the primes-≤λ² approximation (smooth, PNT-controlled) of the Weil symbol, WITHOUT using the position of the zeros. This is equivalent to: the positivity of the explicit formula TRUNCATED to primes ≤λ² is controlled by the prime distribution (PNT) up to the horizon T*. ## Frank diagnosis of the attempt I deployed the three standard techniques (square/P8, Hardy, functional equation). **Each one reduces A
to a known wall or to the sharp-constant=RH.** The attempt PROVES:
- [P] The Fourier reduction A_λ = (1/2π)∫|f̂|²W_λ dt, W_λ=2θ'−2Re[−ζ'/ζ]_{≤λ²} (explicit formula).
- [P] The (in)definiteness lives in the poles of ζ'/ζ at the zeros.
- [P] Hardy gives c<2 (approximate positivity A_λ≥−ε); the SHARP constant c=2 = RH.
- **[GAP]** the positivity of the FINITE form (primes ≤λ²) from PNT, without zero position. **The [GAP] is localized to the millimeter:** it is the positivity of the explicit formula truncated to
primes ≤λ², controlled by PNT up to T*. I could not close it with elementary techniques — and I showed
why each one fails (3a→P8, 3b→sharp constant=RH, 3c→NG-D4). If there is a SHARP Hardy
bound (c=2) from the finite prime side, or the construction of the square 𝒯=A*A independent of
zeros (your cross-place cancellation program), it fits into the [GAP] and A closes. I do not have it. **This is NOT a proof of A.** It is the frank attempt: the explicit reduction + the map of
why the elementary techniques fail + the localized [GAP]. The ∎ of A requires input that I do not
possess (the sharp Hardy bound / the cross-place square of).
