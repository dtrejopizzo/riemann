# AUDIT_016 — Dense range of map011

2026-10-19. Independent check. **PASS / PROVED.** Review of
`LINK_016_DENSE_RANGE.md` against LINK011, CONSTRUCTOR015, AUDIT015, the
corresponding entries of the index, the grid and the current crossword.
No new numerics, no modification of papers and no new sign route.

## 1. Annihilator and normalisations

The bound of 011 gives `|η_d|≤C||h||d^(-1/4)` at α=1/4. Hence
`c=Ση_d/d` converges absolutely and the function b_h is well defined and
holomorphic on `|Im z|<π/4`, by uniform convergence of the Gaussian
series on compact sets. Orthogonality to the even polar-free origin forces
its even part to be λcosh(x/2); analytic continuation extends this
identity from any window T>0 to the whole real axis.

The convention of 006 is `τ=θ−1`, with both signs of the integers. Thus the
distribution μ of 016 satisfies exactly
`Θ_μ(y)=Ση_dτ(d²y)−cτ(y)`. No factor 2 is missing. The even identity implies

`Θ_μ(y)+y^(-1/2)Θ_μ(1/y)=(λ/2)(1+y^(-1/2))`.

Consequently `μ′=μ−(λ/2)δ_0` is the correct correction. Its coefficients
have polynomial growth and μ′ is an even tempered distribution.

## 2. Gaussian injectivity and periodicity

Lemma2 is valid in S′. Differentiating the Gaussians at y=1 in the Schwartz
topology delivers the even moments; parity kills the odd ones.
The function `G(z)=⟨ν,exp(−πx²+zx)⟩` is entire because all Schwartz
seminorms of its derivatives are uniformly controlled on compact sets
of z. Its vanishing Taylor coefficients give G=0.

On the imaginary axis, the identity with the Fourier transform of
`exp(−πx²)ν` is justified by duality in Schwartz space; that transform is a
smooth function of polynomial growth. The frequency normalisation
for z=it is −t/(2π), with no effect on the vanishing. Fourier
injectivity gives `exp(−πx²)ν=0`. Multiplying compact tests by exp(πx²)
recovers ν=0 locally and, by density of compact tests in Schwartz space,
also as a tempered distribution. No citation of Hermite completeness
is needed.

The exact transform of the Gaussian gives
`Θ_(𝓕ν)(y)=y^(-1/2)Θ_ν(1/y)`. Applying the lemma to μ′+𝓕μ′, which is even,
proves `𝓕μ′=−μ′`. Since μ′ is a sum of pure deltas at integers,
its Fourier transform is 1-periodic; hence so is μ′. Comparing the masses forces
constant coefficients, including the mass at 0. At y=1, the
antisymmetric identity kills that constant because θ(1)>0. One gets μ′=0, λ=0,
c=0 and, by induction on divisors, η_d=0 for all d≥2. The density
of the span of f_d in the definition of H concludes h=0. The proof does not classify
distributions with derivatives of deltas, which do not appear here.

## 3. Core and scope

The smooth even core with vanishing polar moment is dense in the corresponding L²
subspace: smooth even approximation and moment correction with a
fixed test. Boundedness of U_T transports that approximation. Dense
range is obtained for each T>0 also from that core.

A continuous Hermitian form on H positive on that image is positive
on all of H by continuity. By 015, the consequence for the real span of
the three pieces is exactly the nonnegative orthant. Combined with 014,
the exclusion refers to fixed nonzero combinations and to the same map011;
it does not extend to T-dependent coefficients.

Density does not imply injectivity, surjectivity or bounded inverse
of U_T. Nor does it imply density of the image of a finite block: such an
image is finite-dimensional and closed. It does not identify V with the whole
Gaussian ambient space, does not control other maps or discontinuous forms and does not
produce equality, domination or sign of Q_T. Row D does not change status.

## Independent editorial note: file 06

The corrections of [margin] and R6 in
`05-meta-and-planning/ROUTES-TRIED-INDEX/06_OPEN_RESIDUES_DEAD_SUBROUTES.md`
agree with P46 cor:margin1 and rem:moriceiling: the proved ceiling for λ_A
is `4·10^9 T exp(−15.449T)`, T≥1. Mori's doubly exponential ceiling
is recorded as cited and unverified, and corresponds to λ_W. The relation
λ_W≤λ_A does not transfer it to λ_A. From
`L(T)(1−o(1))≤λ_A(T)≤4·10^9 T exp(−15.449T)`, with L>0, one does deduce
`L(T)≤(1+o(1))4·10^9 T exp(−15.449T)`. **No failures detected.**
