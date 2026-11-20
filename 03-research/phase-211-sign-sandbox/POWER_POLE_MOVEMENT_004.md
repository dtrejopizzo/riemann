# POWER_POLE_MOVEMENT_004 — Individual pole movement by covariance

Status: PROVED (pole movement of the archimedean part and uniform prime/polar control); CITED the confluent rational certificate of POWER_CONFLUENT_004. Does not modify papers.

Independent review: the covariance, the common identification of numerators and min–max for all eigenenergies were approved; WT=1302 was also approved and the confluent certificate was rerun (margin 79/700>1/10). The bounds of this note are deliberately somewhat weaker than those obtained in that review.

## 1. Corpus and concrete difference

Targeted searches: ROUTES-TRIED-INDEX index (Takenaka, model space, confluent, pole movement, Müntz), master grid/parts, crossword, phase211. General antecedents on rational bases and completely monotone functions do not prove the movement. POWER_ARCH_TRIPLE_004 explicitly records the local conjecture and a diagnostic without proof. The new reason is an EXACT comparison of Rayleigh quotients keeping the rational numerator when a single pole is moved; it is neither a global dilation nor differentiation of fixed coefficients in a moving basis.

## 2. Theorem: all archimedean eigenenergies grow when poles increase

Let u_1,...,u_n>0, allowing multiplicities; the corresponding space is the span of y^k exp(-u_j y)1_{y>0}, with k less than each multiplicity. Its Fourier transform is exactly

    fhat(tau)=P(i tau)/Π_j(u_j+i tau), deg P<n.

The coefficients of P are real for real f; the same argument admits complex ones. It is a FIXED space of numerators, independent of the poles.

If v_j>=u_j for each j, for the same numerator P the new spectral weight is the old one multiplied by

    R(tau)=Π_j (u_j²+tau²)/(v_j²+tau²).

R is positive, bounded and increasing as a function of |tau|. The multiplier m(tau)=Re psi(1/4+i tau/2)-log pi is also increasing in |tau|: each summand of its series

    m(tau)=m(0)+Σ_{k>=0} [(tau/2)²/((k+1/4)((k+1/4)²+(tau/2)²))]

is strictly so. Normalise the old weight to a probability dμ. Then

    Rayleigh_v(P)-Rayleigh_u(P)
      =Cov_μ(m,R)/E_μ R >=0.

The inequality requires no property of P: the covariance is half the double integral of

    [m(tau)-m(sigma)][R(tau)-R(sigma)],

nonnegative because both factors have the same sign when comparing |tau| and |sigma|. Integrability comes from deg P<n and m=O(log(2+|tau|)). By min–max over the same polynomial space, ALL ordered compressed eigenenergies are nondecreasing when the poles are individually increased. In particular

    lambda_min_arch(u_1,...,u_n)
        >=lambda_min_arch(u,...,u),  u=min_j u_j.             (PM)

Repeated poles are allowed from the outset, without a numerical stability argument. The comparison between spaces uses the rational correspondence P/D_u -> P/D_v; it does not claim that a fixed time function keeps its coefficients when poles move.

## 3. Exact differential form and strictness

Varying only u_k and keeping P,

    d Rayleigh/du_k = Cov_μ(m, -2u_k/(u_k²+tau²)) >=0.

This second function is increasing in |tau|. One can differentiate under the integral, since on compacts u_k>0 the logarithmic factor is bounded and m is integrable against the rational weights. It is a formula that includes the variation of the norm denominator; omitting that term would give an incorrect derivative. If the pole increases strictly and P is not zero, the covariance is strictly positive, since the density is not concentrated on a single |tau|.

## 4. Uniform comb and polar without an upper bound on the poles

For u_j>=u, the rational orthonormal basis has transform

    F_j(s)=sqrt(2u_j)/(s+u_j) Π_{k<j}(s-u_k)/(s+u_k).

Each all-pass factor in time is delta_0-2b exp(-by)1_{y>0}. Multiplying by exp(uy/2) conjugates the convolution; the L1 norm of each weighted filter is at most

    1+2b/(b-u/2)<=5.

The normalised initial exponential has weighted L2 norm <=sqrt2. By Young and Cauchy--Schwarz on the orthonormal coefficients,

    ||exp(uy/2) f||² <= B_n ||f||²,
    B_n=2Σ_{j=0}^{n-1}25^j=(25^n-1)/12.                     (WT)

This implies |c_f(t)|<=sqrt(B_n)exp(-ut/2)||f||². For n=3 and u>=63/2, B_3=1302 and

    |comb|<=2sqrt1302 Σ_{q>=2}Lambda(q)q^{-(u+1)/2}||f||²
          <=74 Σ_{q>=2}q^-15 ||f||²
          <=74/(28672)||f||² < (3/1000)||f||².

We used sqrt1302<37, Lambda(q)<=logq<=q and (u-1)/2>=61/4>15, and Σ_{q>=2}q^-15<=2^-15(1+2/14)=1/28672.

For the polar, let A=∫f exp(y/2), B=∫f exp(-y/2). For real f,

    2AB=(A+B)²/2-(A-B)²/2 >=-(A-B)²/2.

The exact weighted integral is

    ∫_0^∞4sinh²(y/2)exp(-uy)dy=2/[u(u²-1)].

By (WT) and Cauchy--Schwarz,

    polar >=-1302/[u(u²-1)] ||f||² >-(21/500)||f||²

for u>=63/2, by rational arithmetic. The cancellation A≈B is kept; the crude bound by |AB| destroys it.

## 5. Consequence for ALL triples of exponents >=32

POWER_CONFLUENT_004 certifies with rational arithmetic lambda_min_arch(63/2,63/2,63/2)>1/10 (input CITED here). By (PM) and §4, for ALL triples of exponents a_i>=32 and all real coefficients,

    Q[Σ c_i X^-a_i] >= (1/10-21/500-3/1000)||f||²
                     =11/200 ||f||² >||f||²/20,

with f=Σ c_i zeta(a_i)exp(-(a_i-1/2)y). The same reasoning includes confluent limits of three powers, interpreted as exponentials times polynomials.

This result does NOT extend to arbitrary n with fixed u by §4: B_n grows like 25^n, and moreover the smallest confluent eigenenergy decreases as n increases. Uniform archimedean positivity in dimension has not been proved. The analytic advance is to eliminate completely the separation and the upper bound of the three rates, by means of the new theorem of individual pole movement.
