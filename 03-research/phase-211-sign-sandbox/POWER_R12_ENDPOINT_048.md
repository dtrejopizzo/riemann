# POWER_R12_ENDPOINT_048 — First endpoint of the restricted arithmetic transport

Status: rational certificate of the confluent endpoint; independent review APPROVED in POWER_R12_AUDIT_048.md and verifier reproduced. OPEN uniform R12 for all rates. Papers untouched.

## Antecedents and difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, R162_2300_MASTER_GRID, CROSSWORD-TO-D and PRIME_TRANSFER014, SIGNED_TRANSFER014 and ARITHMETIC_BLOCK007. No explicit later closure of R12 was found. The universal falsifier014 uses huge order; it does not belong to V12. Here the positive base V12 is kept exactly and only the first natural endpoint v=u is checked, without sweeping rates or orders.

## Exact form and restriction

Let u=63/2, and let e_j be the causal orthonormal basis with transforms

    E_j(s)=sqrt(2u)(s−u)^j/(s+u)^(j+1), 0≤j≤12.

E2=ARCH+POLAR−sqrt(2)log(2)c(log2) is kept, without omitting the polar or replacing the contact by a norm. For F0 in V12, G(s)=sF0(s)/(s+u) belongs to V13 and G(0)=0. Conversely each G in V13 with G(0)=0 has that representation with F0 in V12. The restriction in real coordinates z is sum_j(−1)^j z_j=0.

The verifier tools/power_r12_endpoint_048_verify.py reproduces the audited rational bounds007, extended by one band: ARCH by power sums from16 with Euler tail and explicit remainder; exact polar; contact2 with log2 enclosed by atanh. The bands are Toeplitz. The rational centre uses denominator10^15 and the norm error by row sum is less than10^−10.

The congruence from thirteen to twelve dimensions has columns C_i=e_i−(−1)^i e_12, 0≤i≤11. The rational LDL checks positivity of

    Cᵀ[T_centre−(1/50+10^−10)I]C.

Hence, without numerical diagonalisation,

    E2[G] > (1/50)||G||²,   G∈V13, G(0)=0, G≠0.       (ENDPOINT)

The tail of the remaining primes has not been included in this claim: R12 was posed precisely for E2. Nor is the bound of that tail on V12 imported to V13.

## Local consequence and pending obligation

For any c<1/50, in particular c=1/2500 (also below the certified base coercivity007), ENDPOINT proves R12 at v=u. Moreover there exists ε>0 such that R12 holds simultaneously for all F0∈V12 and u≤v≤u+ε. Indeed, in a fixed basis of V12, the matrices of E2[sF0/(s+v)]−c||sF0/(s+v)||² are continuous in v. The archimedean integral is uniformly dominated near u by an integrable function with factor log(2+|τ|); the polar and contact terms are continuous by their causal rational integrals. The matrix at u is positive definite; its smallest eigenvalue keeps its sign in a neighbourhood. No effective radius is given here.

This local consequence does not prove R12 for all v≥u. Monotonicity of ARCH under pole movement does not order the oscillatory symbol of contact2 nor its polar change. Nor does it authorise successive movements: after the first one the base is no longer confluent V12. The original uniform obligation remains OPEN. The new result is the certificate of the restricted correction at the endpoint, with margin, and the exclusion of a falsifier at that endpoint; not a closure of the transport or of the full sign.

## Complement: the polar of the highpass orbit has an effective remainder

The relevant geometric expansion was already proved in GEOMETRIC_TRANSFER015; it is not presented here as new. To use it on V12 one needs an effective cut J after which ARCH on Q^jV12 dominates contact2 and the polar, and certificates of all previous indices. ENDPOINT only covers j=1.

The disappearance of the polar can be quantified simply, without resorting to a worst-order estimate. Let Q(s)=s/(s+u). In the basis e_0,...,e_11, the compression of q=|Q(iτ)|² is tridiagonal with diagonal1/2 and adjacent entries1/4: with z=(iτ−u)/(iτ+u), q=(2+z+z̄)/4 and the spectral measure of e_0 is the uniform measure on the circle. For a real or complex vector a, alternating signs gives the difference energy with two zero endpoints. By telescoping and Cauchy,

    <qF,F> ≥ ||F||²/(4·12²)=||F||²/576.

For M_j=||Q^jF||², Cauchy gives M_(j+1)M_(j−1)≥M_j²; thus M_j≥576^−j M_0. On the other hand Q(−1/2)Q(1/2)=−1/3968, and therefore

    Polar[Q^jF]=(−1/3968)^j Polar[F],
    |Polar[Q^jF]|/M_j ≤ (9/62)^j |Polar[F]|/M_0.

An explicit uniform bound for the last quotient is the norm of the exact polar matrix12 of007; its sum of absolute values can be used. This pays the polar remainder of an eventual proof by cut J. It does not by itself give an effective archimedean cut nor the sign of the intermediate blocks; no campaign over those blocks has been run.
