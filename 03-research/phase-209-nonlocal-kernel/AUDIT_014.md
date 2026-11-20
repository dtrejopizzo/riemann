# AUDIT_014 — Gaussian component after removing the rank one

2026-10-19. Independent check. **PROVED, with declared CITED input from Paper47.**

Review of `LINK_014_REMOVING_RANK_ONE.md`. Consulted: the project rules, routes index, grid and crossword. The difference with respect to 013 is substantive: its lower bound depended on κvv*; here a smaller subform, Π, is studied via an independent argument. An obstruction for a smaller form is not deduced from the obstruction for a larger one.

## 1. Domain and positive kernel

For d≥2, W_d(u)<0 and f_d(y)=q_d(y)−1/d<0. Each summand of K_y is positive, and on compact sets convergence is uniform by an O(d⁻²) majorant. Its global integral is computed via the absolutely convergent Mellin of m:

`∫2e^(x/2)W_d(e^(2x))dx=−κ(d^(−1/2)−d⁻¹)`.

Tonelli proves exactly `∫K_y=κΣv_d(1/d−q_d(y))=C(y)`, with 0<C(y)≤κ[ζ(3/2)−ζ(2)]. A majorant uniform in x is not required to interchange sum and global integral: positivity is used. For bounded F, |F|K_y is integrable and justifies the pointwise identity of B_F. The partial sums also converge in the Gaussian factor by 011; a subsequence converges almost everywhere and coincides with the pointwise sum. Hence the energy identity (3) is legitimate.

## 2. Local limit and passage to the integral

The Fourier inversion has prefactor √(k/T)/(2π), phase √k zx/T and limit exp(−z²/6). Its integral gives `g₀=√(3(21/e)/(2π))`, with the correct normalisation. Gaussian domination on |z|≤√k and the two tails in v prove both the local limit and the uniform supremum. The Fourier moments give `||G_T^(j)||∞=O(T^((1−j)/2))`; for j=2,4 their contributions to F_T/√T vanish uniformly.

Consequently F_T/√T converges pointwise to −γ₁²g₀/4 and is uniformly bounded. K_y∈L¹ allows dominated convergence for each y; convergence on the whole Gaussian space is not assumed. Fatou on [1,2] suffices to obtain `liminf E_Π(F_T)/T≥L₀>0`. C(y) is measurable and bounded, τ is positive continuous on that interval and C(y)>0 at every point. The sequential argument justifies the liminf for real T.

Fixing T≥1 when presenting the family guarantees k≥8, sufficient derivatives and membership in the form domain; it does not affect any asymptotic conclusion.

## 3. Cross-check with the declared form

The CITED bound refers to these concrete F_T, as verified in 013 against the proof in Paper47; a bound for a test is not extracted from the spectral infimum. With ||F_T||²=O(T^(3/2)), one gets |Q_T|=O(T^(5/2)e^(−15.449T)). Dividing by E_Π≥c₀T gives the quotient O(T^(3/2)e^(−15.449T)) and excludes every fixed positive constant for Π and for S−κvv*.

Smooth approximation in H¹ preserves the polar condition and the strict inequality: Q is continuous in H¹ and the reduced energies are continuous in L² of each window by 011 and domination by S. The necessity for a possible scale c(T) is only an upper bound; neither existence nor impossibility of such a scale is claimed.

## Verdict

**Favourable.** Removing the rank one from the kernel does not repair the uniform domination with map011. No new positivity of D was obtained, nor an obstruction for other maps or for T-dependent coefficients. The use of zero information is declared and limited to the falsifier.

## Final addendum — §7 and combinations of the three pieces

The full extension of §7 reviewed. **Favourable verdict, PROVED with the same CITED input.**

The covariance with index 2 is zero for odd d and `(1−1/√2)d^(−1/2)` for even d; G_s(2,2)=1/√2−1/2>0. The series L₂ converges absolutely and Cauchy–Schwarz applies to the PSD form G_s, also for the limit series because κG_s≤S and the expansion of 011 converges in S.

The Riemann sum over even indices has density 1/2: `(1/N)Σ_(2|d)g(d/N)→(1/2)∫g=κ/4`. The factor −2(1−1/√2) gives h₂(−∞)=−κβ, β=(1−1/√2)/2. The same integrable majorants of 013 justify the tails; the remaining positive term is O(N^(−1/2)) because m≤1 and Σd^(−3/2)<∞. Local continuity and the right-hand limit via the Gaussian bounds complete the global boundedness of the profile.

The even part of the profile tends to −κβ/2 at both ends. By escape of mass of G_T/T and derivatives of L¹ norm=o(T), `L₂(F_T)/T→γ₁²κβ/8`. The factors of two in (11) and (12) are correct. Cauchy–Schwarz delivers E_G(F_T)≳T²; hence this piece alone also fails as a uniform domination with fixed positive scale.

The corollary A,B,C≥0, not all zero, is valid: each energy is nonnegative, the smallest guaranteed growth rate among the pieces is T and Q decays exponentially with a polynomial prefactor. The conclusion covers any fixed nonzero nonnegative combination with exactly the coefficients a_d(F) of 011. It does not cover signed cancellations, another map or T-dependent factors. It completes the examination of the three existing pieces; not a general NO-GO for D.
