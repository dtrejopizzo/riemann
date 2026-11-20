# Frequency of the crossings of the critical level

For every fixed h>0 and every Z large enough there is a crossing of H(x)=Σ_{r≤x}μ(r)/√r−1/ζ(1/2) inside [Z,Z^(1+h)]. In particular the last admissible crossing D in 141, with 2D log D≤X, satisfies log D/log X→1. The statement is unconditional and presupposes neither simple zeros nor bounds on their individual residues at large heights.

**Localization by a finite contour.** Let U(t)=H(exp t) for t≥0 and zero for t<0. Its Laplace transform in σ>1/2 is L(s)=1/[sζ(1/2+s)]−1/[sζ(1/2)]. It continues meromorphically and is regular at the origin. Fix a relative width 0<δ<1. For t normal with mean T and variance cT, Iτ=E[U(t)exp(−iτt)] is the vertical integral on Re s=3/4 of

    L(s) exp(T(s−iτ)+(cT/2)(s−iτ)²) ds/(2πi).

This follows by Fourier of the Gaussian and Fubini using exp(−3t/4)U(t) integrable. The physical part |t−T|>δT costs O(exp(−T)) by taking c small enough, by |U(t)|≪exp(t/2) for t≥0 and Cauchy–Schwarz as in 115.

The poles in the strip −2≤Re s≤3/4 are precisely z=ρ−1/2 with multiplicity; the first trivial zero would correspond to −5/2. Their rate in the average is

    fτ(z)=b+(c/2)(b²−(γ−τ)²),    z=b+iγ.

For each fixed τ the maximum is attained, since |b|≤1/2. If some b>0 exists, fix one and take c small. If max f₀≥0, centering τ at the ordinate of a maximizer gains cγ²/2>0; if max f₀<0, centering at the pole with b>0 gives a positive rate. On an open set of frequencies max fτ>max(0,max f₀); choose τ avoiding ties between distinct poles. For equal γ the rate increases strictly with b when c<1, and for different γ there is only one tie frequency per pair. If all poles lie on the line b=0, take τ exactly equal to the ordinate of one of them: the maximum is unique as a point, of rate zero, and max f₀<0. In both cases the dominant pole may have multiplicity.

For these two frequencies, 0 and τ, fix a large height G free of poles on the boundary, including all maximizers. On the right line, outside [−G,G], the modulus of L is uniformly bounded by absolute convergence and the Gaussian exponent allows the cost to be made O(exp(−T)). Shift only the finite segment to Re s=−2. There the rate is at most −2+2c<−1. On the horizontal sides the whole rate is <−1 by increasing G. The constants of the fixed contour may depend on G; G is not sent to infinity after taking residues. For a pole of order m the term is its exponential times a polynomial in T of degree m−1: the leading coefficient contains the principal Laurent coefficient times (1+c(z−iτ))^(m−1)/(m−1)!, nonzero. By uniqueness of the maximum and finiteness, |Iτ| strictly dominates |I₀| and the error of the physical tails for T large, also when its rate is zero.

The non-negative weights 1±cos(τt+φ), with phase chosen to obtain I₀±|Iτ|, produce averages of opposite signs even after cutting to [(1−δ)T,(1+δ)T]. There U takes both signs. Choose T=(1+h/2)log Z and δ with both endpoints strictly inside [log Z,(1+h)log Z]. An interior crossing of the step function is obtained, with the jump error of 141.

**Consequence for the pending band.** Let B be the real solution of 2B log B=X. Apply the result to Z=B^(1/(1+h)). For all X large enough there is a crossing D between B^(1/(1+h)) and B. Since h>0 is arbitrary and log B/log X→1, the last D(X) has the announced exponent. By 141 the normalized contribution of r≤D(X) is √π/(4ζ(1/2))+O(X^(−1/2+o(1))). In the remaining one-sided obligation only D(X)<r≤10X log X need be kept. Neither a band of fixed ratio nor a bound for its sum is obtained.

**Cross-check.** 115 uses the separation of Gaussian rates for absolutely summable series of exponentials. 133 applies it to an explicit formula for ψ. For H one works with the reciprocal of ζ and a fixed rectangle after choosing the frequency: thus there is no need to assume that the series of residues of 1/ζ is absolutely summable. This answers the lack of a rate for the cuts in 141.
