# POWER_CENTERED_CUTOFF_049 — Effective cutoff j=14 via integration by parts

Status: **PROVED, independent review APPROVED in POWER_R12_AUDIT_049.md and proof re-checked.** Moment and ARCH bound for the WHOLE orbit Q^j V12, j>=14. This isolated lemma proves no global sign of W nor R12; its assembly with the finite segment is in POWER_R12_TRANSPORT_049.md. Papers untouched.

## 1. Corpus and new reason

Consulted ROUTES-TRIED-INDEX/README, the master grid, CROSSWORD-TO-D, HIGHPASS015 and R12_ENDPOINT048; search for Jacobi, Gegenbauer, weighted Bernstein and inverse frequency. JOINT_SCALE016 and DESCENT_AUDIT016 already contain Jacobi coordinates for rational sectors; they are not presented as new. HIGHPASS015 proves uniform eventual positivity at fixed dimension, but without an effective cutoff. ENDPOINT048 gives j=1 and an effective polar tail, leaving that cutoff open.

The difference is a quantitative FINITE inverse-moment inequality for ALL numerators of dimension12 and ALL j>=14. It is proved by integration by parts and a weighted polynomial bound proved below. It is not a campaign over indices, nor an asymptotic without constant, nor a claim of uniformity as the dimension grows.

## 2. Statement

Let P be a nonzero complex polynomial of degree<=11 on the circle, and

    q=(2+z+zbar)/4,
    dmu_j=q^j |P(z)|² dtheta / int q^j |P(z)|² dtheta.

For EVERY integer j>=14,

    E_mu_j[(1-q)/q] < 49/20.                              (MOMENT)

In the exact correspondence of ENDPOINT048, z=(i tau-u)/(i tau+u), u=63/2, one has q=tau²/(u²+tau²). Hence, for EVERY F0!=0 in V12 and G=Q^j F0,

    E_G[tau^(-2)] < 1/405 < 1/400.                       (INVERSE)

The measure E_G is |G(i tau)|² d tau/(2pi ||G||²). All complex coefficients are allowed; in particular the real ones are covered.

## 3. Weighted polynomial bound, with proof

For a>0, w_a(y)=(1-y²)^a on[-1,1], and a polynomial p of degree<=d, define

    M=int w_a |p|²,
    D=d(d+2a+1).

One has

    int (1-y²)w_a |p'|² <= D M.                          (BERNSTEIN)

Elementary proof: L_a p=-(1-y²)p''+(2a+2)yp' preserves each space of polynomials of degree<=n. Integration by parts shows it is symmetric in L²(w_a), and that its form is the left-hand side of BERNSTEIN; the boundary vanishes because a+1>0. If p_n is the monic orthogonal polynomial of degree n obtained by Gram-Schmidt, L_a p_n is orthogonal to all lower degrees by symmetry and degree preservation. Its leading coefficient is n(n+2a+1). Thus p_n is an eigenpolynomial with that eigenvalue. Expanding p in this basis and using that those values increase with n proves BERNSTEIN, also for complex coefficients. No external citation is required.

Now let

    r=int [y²/(1-y²)]w_a |p|² / M.

Integrating the derivative of y w_a |p|² gives

    2a r = 1 + 2 Re int y w_a p' conj(p)/M
         <= 1 + 2sqrt(rD).                              (IBP)

The boundaries vanish because a>0; the integral with singularity of order(1-y²)^(-1) is finite by the same condition. The inequality uses Cauchy on y p/sqrt(1-y²) and sqrt(1-y²)p', then BERNSTEIN. This is an effective bound for ALL polynomials of the indicated degree.

## 4. Exact reduction from the circle to two sectors

Parametrize z=exp(2ix), -pi/2<=x<=pi/2. Then q=cos²x. Multiplying P(exp(2ix)) by exp(-11ix) keeps its modulus and leaves only odd frequencies between-11 and11. Its even part is a combination of cos((2l+1)x), and its odd part a combination of sin((2l+1)x). With y=sin x one writes exactly

    exp(-11ix)P(exp(2ix)) = cos x R(y)+S(y),

with R even of degree<=10 and S odd of degree<=11, allowing complex coefficients. This follows from the elementary multiple-angle formulas: cos((2l+1)x)/cos x is an even polynomial in sin x of degree2l, and sin((2l+1)x) is an odd polynomial of degree2l+1.

The cross term is odd in x, so it integrates to zero both in the norm and after multiplying by (1-q)/q. Using dx=dy/sqrt(1-y²), both integrals are sums of two sectors:

    S: a=j-1/2, d<=11;
    R: a=j+1/2, d<=10.

The ratio MOMENT is a positive mixture of the ratios r of those two sectors; an identically zero sector is simply omitted.

## 5. Uniformity in ALL j>=14 and rational constants

In sector S, IBP implies

    r <= 1/(2j-1) + 2sqrt[11(2j+11)]/(2j-1) sqrt r.

Both right-hand coefficients decrease for j>=14. For the second, it suffices to differentiate (2j+11)/(2j-1)²: its derivative is negative for j>=1. In sector R one has a larger denominator2j+1 and a smaller D 10(2j+12)<11(2j+11), so the same bound dominates both sectors. Hence, for ALL j>=14 and both sectors,

    27 r <= 1+2sqrt(429r).                               (UNIFORM)

The quadratic inequality in sqrt r forces r below its unique positive root. That root is STRICTLY less than b=49/20, since

    27b-1=1303/20>0,
    (27b-1)²-4·429·b=16129/400>0.

Equivalently, the polynomial27t²-2sqrt429 t-1 has a single positive root and is positive at t=sqrt b. Thus each sector ratio is less than49/20, and so is their mixture. This proves MOMENT.

Since u²=3969/4,

    (49/20)/u²=1/405,
    1/400-1/405=1/32400>0,

which proves INVERSE. No Gram matrix per j has been evaluated nor a uniform limit assumed.

## 6. Effective archimedean consequence

The digamma bound used in QUADRATIC017§6 is

    m(tau)>=log(|tau|/(2pi))-1/|tau|-1/(2tau²), tau!=0.

Jensen for log and Cauchy, applied to INVERSE, give

    ARCH[G]/||G||²
      >= -(1/2)log E_G[tau^-2]-log(2pi)
                   -sqrt(E_G[tau^-2])-(1/2)E_G[tau^-2]
      > log(10/pi)-1/20-1/800
      > 859/800.                                         (ARCH)

For the last inequality log(10/pi)>9/8 suffices. It is elementary: pi<22/7 gives10/pi>35/11. Moreover exp1<11/4 and exp(1/8)<8/7 imply exp(9/8)<22/7<35/11. The bound on exp1 is obtained by summing up to degree3 and dominating the tail from degree4 by5/96, giving exp1<87/32<11/4; that on exp(1/8) is obtained from the geometric series. The logarithms are integrable for these rational functions; near zero j>=1 suffices, and at infinity the rational decay dominates log.

An effective archimedean cutoff J=14 has been obtained for the WHOLE Q^j V12. Contact2 and the polar must be added with their bounds and the indices j<14 must be treated separately before concluding a uniform claim of E2 or R12 transport. This memo certifies neither those indices nor controls the complete tail of the other primes. Global sign OPEN.
