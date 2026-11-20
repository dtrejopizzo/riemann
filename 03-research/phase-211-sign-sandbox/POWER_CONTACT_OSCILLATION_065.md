# POWER_CONTACT_OSCILLATION_065 — Exact number of sign changes for all N,k

Status: **PROVED/APPROVED**, independent review in POWER_CONTACT_OSCILLATION_AUDIT_065.md and a further re-check. Theorem on the autocorrelation and the sign of the arithmetic tail; NOT on the sign of W. Papers untouched.

## 1. Antecedents and change of object

Read the project rules, ROUTES-TRIED-INDEX/README, master grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reviewed ARITHMETIC_DIFFERENCES019 and its audit, DESCENT016 and the antecedents on Bessel derivatives, Laguerre, Descartes, bell-shaped and total positivity. The targeted search did not find in the POWER corpus a statement of the exact number of roots for ALL k.

019 proves a single frontier for k=1 via the coefficient ratio j(j+1)-2N and Descartes. That computation is not relaunched under another name. Here the object changes: the derivatives of order2k of C_(N+k) are considered and their exact number of roots is counted via cancellation of2k moments and one-sided exponential convolutions. The proof uses Rolle with a boundary at infinity, not an assumption of total positivity of another kernel. The last-root bound obtained here is deliberately coarser than that of019 for k=1.

## 2. Statement and exact coefficients

Let u>0, integers N>=1,k>=1 and

    F_(N,k)(s)=s^k/(s+u)^(N+k),
    K_(N,k)(t)=c_(f_(N,k))(t).

Then K_(N,k) has exactly k roots in(0,infinito), ALL simple, and no other zero there. It is positive at0 and its signs alternate when crossing those roots. If chi_(N,k) is the largest root in the coordinate x=u t, then

    chi_(N,k) < 4k(N+k-1).                              (LAST)

To give the coefficients, set d=N+k-1 and

    p_d(x)=sum_(j=0)^d a_j x^j,
    a_j=(2d-j)!/[2^(d-j)(d-j)!j!],
    r_(d,k)(x)=(1-D_x)^(2k)p_d(x).

The gamma formulas of019 and the Fourier rule give exactly, for t>=0,

    K_(N,k)(t)=(-1)^k C_(N+k)^(2k)(t)
      =(-1)^k exp(-x)r_(d,k)(x)
                 /[2^(d+1)u^(2N-1)d!], x=ut.           (PROFILE)

Its coefficient of x^j is

    [x^j]r_(d,k)
      =sum_(ell=0)^min(2k,d-j)
          (-1)^ell binom(2k,ell)(j+ell)! a_(j+ell)/j!.

Equivalently, using falling factorial powers,

    [x^j]r_(d,k)/a_j
      =sum_(ell=0)^min(2k,d-j)
          binom(2k,ell)(-2)^ell
                    (d-j)_fall_ell/(2d-j)_fall_ell.     (COEFF)

The term ell=0 equals1. All denominators of the terms present are positive. The sum is not extended to terms with zero denominator. The degree of r is exactly d and its leading coefficient is1.

## 3. Two elementary counting facts

As an algebraic illustration, at N=1 and x=u|t| the first three NORMALIZED profiles are

    K_(1,1)(t)/K_(1,1)(0)=exp(-x)(1-x),
    K_(1,2)(t)/K_(1,2)(0)=exp(-x)(1-5x/3+x²/3),
    K_(1,3)(t)/K_(1,3)(0)=exp(-x)(1-11x/5+4x²/5-x³/15).

They are exact substitutions in PROFILE, not new computations of W. The following argument proves that they have, respectively, one, two and three simple positive roots and extends that pattern to ALL N,k without enumerating cases.

**Moments.** For all N>=1,k>=1,

    int_R t^ell K_(N,k)(t)dt=0, 0<=ell<2k.              (ZERO-MOMENTS)

Indeed, its transform is tau^(2k)/(u²+tau²)^(N+k), which has a zero of order2k at tau=0. The temporal moments are absolutely convergent: PROFILE is exponential times a polynomial on each half-line. Moreover

    K_(N,k)(0)=(1/(2pi))int_R tau^(2k)/(u²+tau²)^(N+k)dtau>0.

**Moments force changes.** If a nonzero real continuous function has absolute moments up to order r-1 and all those moments are zero, and it has finitely many zeros, it must have at least r sign changes. Otherwise, multiplying it by the polynomial product of the factors(t-b) over its s<r change points produces, after choosing a global sign, a nonnegative function not identically zero. Its integral would be positive, contradicting the vanishing of the moments up to degree s.

## 4. One-sided convolution lemma: simple zeros preserved

Let

    e_+(t)=exp(-ut)1_(t>=0),
    e_-(t)=exp(ut)1_(t<=0).

Suppose f is real continuous, with exponential-times-polynomial tails, exactly r simple zeros, and zero moments of orders0,...,r-1. Each convolution e_+*f and e_-*f also has exactly r zeros, all simple, and keeps those zero moments.

Preservation of moments is verified by Fubini and the binomial expansion of(t+y)^ell; both factors have absolute moments of all orders. The tails remain exponential times polynomial. In the application, each half-line keeps exactly the form exp(-u|t|) times a polynomial. No convolution can vanish identically on an interval: its equation g'=f-u g (or g'=u g-f) would force f to vanish there too, contradicting its finitely many simple zeros. Thus the polynomials on both half-lines are not identically zero and the intermediate ones have finitely many zeros; the Rolle count below furthermore provides an independent proof of that finiteness.

For g=e_+*f one has g'=f-u g. Set h(t)=exp(ut)g(t), so that

    h'=exp(ut)f(t), h(-infinito)=0.

Thus h' has exactly r simple zeros. A zero of g is simple if f does not vanish there. If g(b)=f(b)=0, then g'(b)=0 and g''(b)=f'(b)!=0, so that zero would be double. The derivative exists at b by the simplicity of f there. There are no other types of multiplicity.

If h had m zeros counted with multiplicity, Rolle forces h' to have at least m: there are the corresponding zeros of reduced multiplicity at each multiple zero, one between each pair of distinct zeros and ONE before the first. This last one exists because h tends to0 at the left end, equals0 at the first zero and is not identically zero on the interval: it attains a nonzero interior extremum. The total count is

    sum of multiplicities - number of distinct zeros
       + (number of distinct zeros-1)+1 = m.

The same argument on any finite collection of zeros excludes infinitely many zeros. Hence m<=r. Moment cancellation forces at least r sign CHANGES, so m=r and all zeros are simple. In particular double tangencies are excluded.

For e_-*f it suffices to reflect t; equivalently, use h=exp(-ut)g, h'=-exp(-ut)f and the boundary h(+infinito)=0. This proves the lemma without invoking a general property of other kernels.

## 5. Base case and propagation to ALL N

For N=1, the polynomial r_(k,k) of PROFILE has degree k. Thus K_(1,k) has at most k positive zeros. It is even and does not vanish at0, so it has at most2k distinct real zeros. ZERO-MOMENTS forces at least2k sign changes. One concludes that it has exactly k positive roots, all simple, and their negative reflections.

The function C_1(t)=exp(-u|t|)/(2u) satisfies exactly

    C_1=e_+*e_-.

By multiplication of transforms,

    K_(N+1,k)=C_1*K_(N,k).

Applying the one-sided lemma successively to e_- and e_+ preserves the2k simple zeros and the2k vanishing moments. Induction on N proves that K_(N,k) has exactly2k simple real zeros for ALL N>=1. Since it is even and positive at0, exactly k lie on the positive half-line.

The initial sign is positive. The leading coefficient of r is positive, so the final sign in PROFILE is(-1)^k; it coincides with alternating k times from the initial sign.

## 6. Elementary bound on the last zero

For x>0, since all coefficients of p_d are positive,

    0<=p_d^(ell)(x)/p_d(x)<= (d)_fall_ell/x^ell
                                    <=(d/x)^ell.

The first bound follows term by term from(j)_fall_ell<=(d)_fall_ell, and holds with zero derivative when ell>d. Hence

    |r_(d,k)(x)-p_d(x)|/p_d(x)
      <=sum_(ell=1)^(2k)binom(2k,ell)(d/x)^ell
      =(1+d/x)^(2k)-1.

If x>=4kd,

    (1+d/x)^(2k)<=exp(1/2)<2.

The last inequality is obtained by comparing the exponential series with the geometric one of ratio1/2, strictly from the quadratic term on. Thus r_(d,k)(x)>0 for ALL x>=4kd. There are no zeros in that interval and LAST follows. Optimality is not claimed nor is the better bound019 at k=1 replaced.

## 7. Complete arithmetic tail, with its correct sign

Assume u>1/2 to guarantee absolute convergence of the comb. For ALL integers q>=2 with

    u log q >= 4k(N+k-1),

PROFILE and LAST give

    sign K_(N,k)(log q)=(-1)^k.

Hence each nonzero term of the contribution

    -2 Lambda(q)q^(-1/2)K_(N,k)(log q)

has sign(-1)^(k+1). The sum over ALL those q has that same strict sign: there are arbitrarily large powers of2 with Lambda>0. Lambda is neither truncated nor modified. In particular the tail helps W for odd k and is adverse for even k.

For k=0 the case is separated: K_(N,0)=C_N is strictly positive, has no roots and the complete comb is negative, as019 already records. The cutoff formula with k=0 is not used as if it produced a transition.

The theorem does not estimate the magnitude of the tail nor the compensation against the prefix, ARCH and polar. It does not prove W>=0, a new row, a new window T or the global sign. Its result is the oscillation pattern for ALL N,k and an explicit frontier beyond which the WHOLE tail has known sign.
