# POWER_STRIP_CUBIC_NECESSITY_064 — For all numerators, uniform STRIP requires exponent at least 3

Status: PROVED/APPROVED, independent review in POWER_STRIP_CUBIC_AUDIT_064.md, including the improvement to the threshold j≥10^6n. Only a limitation of an absolute contour bound; not a counterexample to W nor to the global sign. Papers untouched.

## 1. Quantitative statement and scope

Fix u=63/2 and any height 0<η<u. For ALL integers n≥4 and j≥10^6n there exists a nonzero REAL polynomial P_(n,j), of degree <n, such that the full density of the causal rational test

    F_(n,j)(s)=s^j P_(n,j)(s)/(s+u)^(n+j),
    ρ_(n,j)(z)=z^(2j)P_(n,j)(iz)P_(n,j)(−iz)/(u²+z²)^(n+j)

satisfies

    ∫_R |ρ_(n,j)(x+iη)|dx / ∫_R ρ_(n,j)(x)dx
       ≥1+η²n³/(1152u²j).                              (LOWER)

Therefore, for no C>0 and p<3 can there exist a finite constant D, independent of n, j and the numerator, that bounds this quotient for ALL tests with j≥C n^p. To see this it suffices to choose

    j_n=max{ceil(C n^p),ceil(10^6n)}.

Then j_n=o(n³), and LOWER diverges.

The conclusion is only an obstruction to the absolute STRIP STRATEGY with fixed height and constant. It does not claim W[F]<0, does not exclude a W sign cone of smaller exponent and does not require a spectral concentration claim that has not been proved. The numerators are constructed explicitly via orthogonal polynomials determined by a positive weight; no cases are selected by computation.

## 2. Antecedents and new difference

Consulted the project rules, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; read JOINT_SCALE016, QUADRATIC017, STRIP_NECESSITY059 and UNIFORM_STRIP060. 059 proves, with P=1, that a uniform STRIP cannot cover the subquadratic scale. 060 establishes sufficiency for ALL numerators in j≥10^12(nq_n)^3, q_n=ceil(log2(n+1)).

The present difference is that the numerator varies with n, j and uses the highest-degree direction of the exact Student weight. The inverse translation generator has a cubic component that leaves the original degree. That component is quantified via an orthogonal projection and the rational remainder is paid with an explicit bound. This yields the new necessity p≥3, versus p≥2 for the constant numerator.

The Gaussian limit is not extrapolated to complex tails, nor is it assumed that a narrow peak implies small variance. The initial construction with Hermite packets was replaced by this exact Student proof, which suffices for the contour objective. The global sign remains open and the arithmetic forms and contacts are not modified.

## 3. Exact weight and recurrence

Set M=n+j and

    w(y)=(1+y²/j)^−M.

Let p_k be the monic orthogonal polynomials for w, and e_k=p_k/||p_k||_w. The weight is even, so p_k has parity k. All moments used up to degree n+5 exist: M>n+5+1/2 under the present hypotheses.

The Pearson proof of 060 applies without changes. The symmetric operator

    L=−(j+y²)∂²+2(M−1)y∂

preserves each degree and has eigenvalue λ_k=k(2M−k−1) on p_k. Comparing the subleading coefficient in p_k=y^k+c_k y^(k−2)+... gives

    c_k=−j k(k−1)/[2(2M−2k+1)].

The monic and the orthonormal recurrences are, respectively,

    yp_k=p_(k+1)+β_k p_(k−1),
    ye_k=√β_(k+1)e_(k+1)+√β_k e_(k−1),
    β_k=j k(2M−k)/[(2M−2k+1)(2M−2k−1)].                (REC)

These identities follow from orthogonality, parity and β_k=c_k−c_(k+1); no Hermite asymptotics are presupposed. The boundary terms of the Pearson operator vanish because the maximal degree is far below M−1/2.

For 1≤k≤n+4, the hypotheses n≥4, j≥10^6n imply

    k≤2n, M≤2j,
    2M−k≥2j,
    2M−2k−1≥2j−9≥j.

Therefore the denominators of REC are positive and

    k/8≤β_k≤4k.                                        (BETA)

The lower bound uses that its numerator is ≥2j²k and the denominator ≤(2M)²≤16j². The upper bound uses numerator ≤4j²k and denominator ≥j².

## 4. A degree n+2 component that cannot cancel

Fix d=n−1 and take

    R=e_d, ||R||_w=1.

The exact generator of 060 is

    A R=y²R′+yR−M y³R/(j+y²).

Rewrite it without approximation:

    A R=y²R′+yR−(M/j)y³R+(M/j)y^5R/(j+y²).              (SPLIT)

The first two terms have degree ≤d+1, so their projection onto e_(d+3) is ZERO. In y³e_d, the coefficient of e_(d+3) only comes from raising three times in REC and equals

    √(β_(d+1)β_(d+2)β_(d+3))
      ≥sqrt(n(n+1)(n+2))/sqrt(8³)>n^(3/2)/24.

Since M/j≥1, this is a lower bound for the modulus of the leading component in SPLIT before paying its remainder.

For any polynomial S of degree r≤n+3, BETA and the decomposition of multiplication into its raising and lowering parts give

    ||yS||_w≤4√(r+1)||S||_w.

Applying it five times, starting at degree d, proves

    ||y^5R||_w≤4^5(n+4)^(5/2).

Moreover M/j≤2 and j+y²≥j. The rational remainder of SPLIT satisfies

    ||(M/j)y^5R/(j+y²)||_w
       ≤(2/j)4^5(n+4)^(5/2)
       ≤12288 n^(5/2)/j
       ≤n^(3/2)/48.                                    (REM)

We used n+4≤2n, 2^(5/2)<6 and j≥10^6n≥589824n. Projecting SPLIT onto the unit vector e_(d+3), using Cauchy for the remainder and subtracting REM gives

    ||A R||_w≥n^(3/2)/48.                              (GEN-LOWER)

It is not claimed that A preserves the degree-d space: precisely its degree-d+3 component is the mechanism of the lower bound.

## 5. Admissible real numerator and phase-free amplitude

Let a=u√j and define

    p(z)=(z/a)^d R(a/z),
    P_(n,j)(s)=p(−is).

Since R has parity d, all powers d−r that appear in p are EVEN and nonnegative. Therefore p is a real even polynomial, nonzero and of degree ≤d<n; P_(n,j) also has real coefficients. There is no hidden inadmissible complex numerator in this construction.

The phase-free amplitude of 060 is

    H(z)=z^j p(z)/(u²+z²)^(M/2),

with the positive holomorphic branch on the line. H is real on the line. The inverse change is used only for the norms, treating the two half-lines with their possible constant phases as in 060. One has EXACTLY

    ||H||²=a^(1−2n)||R||_w²,
    ||H′||²=a^(−1−2n)||A R||_w².

GEN-LOWER proves

    ||H′||²/||H||²≥n³/(2304u²j).                       (DER-LOWER)

Moreover P_(n,j)(iz)=p(z) and P_(n,j)(−iz)=p(−z)=p(z). Consequently the density of the original causal test is

    ρ_(n,j)(z)=H(z)²                                    (DENSITY)

in the whole strip. This equality uses that p is REAL EVEN; a generic complex product is not identified with a square.

## 6. From the derivative lower bound to the absolute contour

For |t|<u, define N(t)=||H(·+it)||². As in 060, differentiation and integration by parts give

    N″(t)=4||H′(·+it)||².

All functions and their derivatives decay in closed substrips; no boundary terms are omitted. Since H is real on the line, N is even and N′(0)=0. The function D(t)=||H′(·+it)||² is also even and convex, because

    D″(t)=4||H″(·+it)||²≥0.

Thus D(t)≥D(0). Integrating twice proves, for 0<η<u,

    N(η)≥N(0)+2η²||H′||².

By DENSITY, ∫|ρ(x+iη)|dx=N(η), while ∫ρ(x)dx=N(0). Inserting DER-LOWER gives exactly LOWER.

This inequality is not deduced from the sign of W nor from Cauchy–Schwarz in a form not proved positive. It is an ordinary L² identity/convexity of an explicit holomorphic amplitude.

## 7. Scaling consequence and limit of the result

If one asked for a bound STRIP≤D for ALL numerators and ALL j≥C n^p with p<3, the tests constructed with j_n=max(ceil(C n^p),ceil(10^6n)) belong to that class. But j_n=o(n³), so LOWER tends to infinity, contradicting finite D.

This fixes a necessary exponent of at least 3 for this type of ABSOLUTE control, while 060 gives sufficiency at order n³ log³n. No optimality of the logarithmic factors is claimed and no attempt is made to optimize constants.

The obstruction does not prove negative W, does not rule out mechanisms that keep arithmetic cancellation instead of the contour modulus, and does not decide the sufficient scalar interior 017. The real Λ, the polar and the symbol remain unchanged. No numerical campaigns or computations of new sign cases were run. Papers untouched.
