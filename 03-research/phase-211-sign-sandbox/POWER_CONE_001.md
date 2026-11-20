# POWER_CONE_001 — Elementary cone of powers in the exterior form

Status: PROVED (identities and finite criteria); OPEN (arbitrary real mixtures for the arithmetic datum). Modifies no paper.

## Antecedents and declared difference

Consulted the index ROUTES-TRIED-INDEX/README.md:393,655; NODE_001.md:195; grid/part3.md:12 and part5.md:7; CROSSWORD-TO-D.md (search theta/cosh/Pick). General positivity of Pick-type kernels and the insufficiency of theta positivity are already recorded. That route is not relaunched. The difference is a closed computation of particular cases of the exterior form, with an exact algebraic frontier for two generators and a verifiable rational counterexample. No novelty is attributed to the general principle.

## 1. Identity by direct integration

Let a>1, rho_a(X)=X^{-a}, X>1. Although these functions do not belong to PW_N, they are data of the exterior universal form with all integrals absolutely convergent. Their image is

    Z rho_a(e^y)=zeta(a) exp(-(a-1/2)y), y>0.

Define L(a) by the explicit real expression

    L(a)=1/a+1/(a-1)-(log pi)/2+psi(a/2)/2+zeta'(a)/zeta(a).

No spectral representation is needed. For h_b(y)=exp(-by)1_{y>0}, b=a-1/2:

* squared norm: 1/(2b);
* autocorrelation: exp(-bu)/(2b), u>=0;
* archimedean term: [psi(a/2)-log pi]/(2b), via the Poisson integral of psi;
* comb: zeta'(a)/(b zeta(a));
* polar: 2/[a(a-1)].

The sum is L(a)/b. By polarization, if rho=Σ c_i X^{-a_i}, a_i>1, d_i=c_i zeta(a_i), then

    Q[rho]=Σ_ij d_i d_j [L(a_i)+L(a_j)]/(a_i+a_j-1).

The polar factor cancels exactly the rational terms separating L from psi and zeta'/zeta. This formula fixes the normalization.

## 2. Proved positive case

L(a)>0 for a>1: the real completed function has a representation H(u)=C∫_0^∞ Phi(t)cosh(ut)dt with u=a-1/2 and Phi(t)>0. Positivity of the kernel is seen in each summand (2 pi n² exp(2t)-3)>0 for t>=0; by differentiation H'(u)>0 and L(a)=H'(u)/H(u)>0. This proof uses only the theta integral and its Poisson derivation.

Consequently Q[rho]>0 for every nonzero combination c_i>=0. It also holds if all c_i<=0. The result does not pass to combinations of arbitrary signs by polarization.

## 3. Two generators: exact criterion

Set u=a-1/2, v=b-1/2, u>=v>1/2. The determinant of the two-point kernel is nonnegative exactly when

    (u+v)^2 L(a)L(b)>=uv(L(a)+L(b))²,

or, equivalently,

    v/u <= L(a)/L(b) <= u/v.

For all pairs of an interval this is equivalent to

    |u d/du log L(u+1/2)|<=1.

Proof: take logarithms of the ratio criterion, divide by log u-log v and pass to the limit; conversely integrate the differential inequality. Positivity of H and its log-convexity only prove L>0 and L'>=0; they do not prove the upper bound u L'<=L.

## 4. False generic-theta lemma: exact counterexample

Counterexample: H(u)=3+cosh u, L(u)=H'(u)/H(u). H is even, positive, the bilateral transform of a positive measure; L>0 and L'>0 for u>0. For x=log2, y=2log2,

    L(x)=3/17, L(y)=15/41, L(y)/L(x)=85/41>2=y/x.

Thus [ (L(u_i)+L(u_j))/(u_i+u_j) ] has negative determinant. A positive cosh representation does not suffice to control even two generators. It is not a counterexample to the arithmetic datum of the paper.

## 5. Positive progress: every plane of powers with exponents >=32 (PROVED)

For a>=32, u=a-1/2, one has L(a)-u L'(a)>0. Indeed the rational terms of this difference are positive. The elementary inequalities ψ(t)>=log t-1/t and ψ'(t)<=1/t+1/t² give

    L-uL' >= (1/2)log(a/(2pi))-1/2-2/a-S(a),
    S(a)=Σ_{n>=2}Lambda(n)n^{-a}(1+u log n).

The first inequality for ψ is obtained from its integral (or Euler--Maclaurin with signed remainder); the second from ψ'(t)=Σ_{k>=0}(t+k)^{-2} and integral comparison. Since Lambda(n)<=log n<=n and u<a,

    S(a)<=2^{-(a-1)}(1+2/(a-2))
           +a 2^{-(a-2)}(1+2/(a-3))<1/100.

One used Σ_{n>=2}n^{-p}<=2^{-p}(1+2/(p-1)). Both bounds of the last line decrease for a>=32, and at a=32 their sum is less than 1/100 by rational arithmetic. Via pi<4 and log2>2/3,

    (1/2)log(a/(2pi))-1/2-2/a
       >= log2-9/16 > 5/48 >1/10.

Thus L-uL'>0 without numerical evaluation of special functions. The positive cosh representation moreover proves L'>=0: log H is convex, by Cauchy--Schwarz for its positive bilateral measure. Hence, for a>=b>=32,

    1<=L(a)/L(b)<=(a-1/2)/(b-1/2).

The criterion of §3 proves Q[c X^{-a}+d X^{-b}]>=0 for any real c,d and a,b>=32 (strict for a!=b and nonzero datum). It is positivity on a union of planes, not on their sum: positivity of matrices of order three is not claimed. It is moreover an exterior case outside PW_N; a bridge to the admissible tails of the paper is missing.

## 6. Precise constructive residue

The next local target is to extend the inequality of §5 towards 1<a<32, using the convergent series of zeta'/zeta and the integrals of psi. Its composition over three generators further requires the order-three determinant; the order-two minors do not suffice. No sign on PW_N/gauge has been obtained.

## 7. Independent review and theta detail

The normalization, the two-point criterion and the estimate a>=32 were reviewed independently. One may take, up to a positive constant, Phi(t)=Σ pi n² exp(5t/2)(2pi n² exp(2t)-3) exp(-pi n² exp(2t)), t>=0. Each summand is positive; the doubly exponential decay justifies all derivatives under the cosh integral on compacts in u. The bilateral measure is not concentrated at a point, whence (log H)''>0.

For the falsifier, (42,-41)K(42,-41)^t=-129/(34 log2) exactly.
