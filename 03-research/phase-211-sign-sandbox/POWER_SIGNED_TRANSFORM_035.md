# POWER_SIGNED_TRANSFORM_035 — Specific positive law of the signed gamma transform

Status: **PROVED**, identities and analytic bounds approved in independent review POWER_BOUNDARY_AUDIT_035.md; symbolic verifier PASS reproduced. FIXED rate u=63/2. No sign of W is declared for all N. Papers untouched.

Quantitative results: exact law of the Abelgamma weights; uniform O(R^4/N²) bound on initial mass; explicit tails and Gamma(shape2) limit at scale m²/(4N). The signed T_m of034 is kept, without postulating its positivity again.

## 1. Corpus and new reason

The project rules, COEFFICIENT_BALANCE033, WEIGHTED_COEFFICIENT034 and their audits were read; the ROUTES-TRIED-INDEX index, the master grid and CROSSWORD-TO-D.md were consulted on positive transforms, Abel, mixtures, Riesz and coefficients. The premise T_m>=0, refuted034 with infinitely many sign changes, is not reopened.

The difference is to study the POSITIVE and SPECIFIC transform of the gamma weights, not an abstract class of measures. The analytic parity034 is folded through an explicit quadratic substitution; the transform has a combinatorial law with uniform bounds that quantify where the compensation must be kept. The identities alone are not promoted to a sign proof. The new inequalities are the mass and finite-budget bounds of§§4–6, valid at ALL N of the declared range without a campaign.

## 2. Real Abel and exact probabilistic normalisation

With d=N−1>=2, keep033:

    a0=a1=1,
    a_(m+1)/a_m=2(d−m)/(2d−m), a_(d+1)=0,
    v_m=a_m/(2d−m), v_(d+1)=0,
    A_N:=W[g_N]/norm²=sum_(m=1)^d (v_m−v_(m+1))T_m.

Define h_m=m(m+1)/2 and t_m=T_m/h_m. The normalisation

    P_d(m)=h_m(v_m−v_(m+1))
      =a_m m(m−1)(m+1)/[2(2d−m)(2d−m−1)], 1<=m<=d,     (P)

is nonnegative (P_d(1)=0) and sums exactly to1. Indeed, summation by parts gives sum h_m(v_m−v_(m+1))=sum m v_m=sum w_m=1. Therefore

    A_N=sum_(m=1)^d P_d(m)t_m.                           (AVERAGE)

This is a positive average of SIGNED values. The profiles defining t_m are not assumed to be admissible autocorrelations. For d1, A_2=T1 and it is treated separately as the already proved case018.

## 3. Catalan substitution preserving parity, without sign inference

Let c_d=binom(2d,d)/4^d. The recurrence by differentiation in u² of the full form gives near z0

    B(z):=sum_(d>=0)c_d A_(d+1)z^d
         =E(u sqrt(1−z))/sqrt(1−z),
    E(v)=L[e^(−vt)].

To justify it, write f(s)=E(sqrt(s))/(2sqrt(s)). Linearity of the form in its rational density and its polar term gives W[g_(d+1)]=(-1)^d f^(d)(u²)/d!, while norm²=c_d/(2u^(2d+1)). Taylor produces the formula. One may differentiate separately in ARCH, comb and polar for |z| small enough; all converge absolutely there.

With F of034 and phi(z)=1−sqrt(1−z),

    B'(z)=(1/2)F(phi(z)),
    F(w)=[E(v)−vE'(v)]/(1−w)^3, v=u(1−w).               (FOLD)

phi has positive Catalan coefficients and satisfies z=phi(2−phi). For d>=2, formal Lagrange inversion gives

    [z^(d−1)]phi(z)^(m−1)
      =(m−1)/(d−1)·binom(2d−m−2,d−m)·2^(−2d+m+1),
      2<=m<=d.

Dividing by2d c_d reproduces EXACTLY the Abel coefficient v_m−v_(m+1). The real transform is not replaced by a freely chosen mixture.

Moreover F(1+s)=F(1−s) implies that F(phi(z)) depends locally on(1−phi(z))²=1−z: the apparent local branching at z1 cancels. This keeps a genuine cancellation of coefficients. It does not prove that the coefficients of B are positive; nor has the continuation around the WHOLE positive real half-axis required by the argument034 been proved for B. Hence OSC034 does not carry over as a conclusion about the sign of the A_N.

## 4. EXACT tails of the gamma law

**Theorem.** For2<=r<=d,

    P_d(M>=r)
      =a_r[1+r(r−1)/(2(2d−r))].                         (TAIL)

Proof: sum P by parts up to r−1. One obtains

    P_d(M<=r−1)=1−a_r−[r(r−1)/2]v_r,

which is equivalent to TAIL. There is no approximation and no hypothesis on T_m.

In particular, for1<=R<=d,

    P_d(M<=R)
      <=min{1,R(R−1)(R+1)(R+2)/[8d(d−1)]}.               (SMALL)

By(P), a_m<=1 and (2d−m)(2d−m−1)>=d(d−1); summing m(m²−1) from1 to R gives R(R−1)(R+1)(R+2)/4. This proves SMALL.

Also, setting x_r=r(r−1)/(4d),

    P_d(M>=r)<=min{1,(1+2x_r)e^(−x_r)}.                  (LARGE)

Indeed

    a_r=prod_(j=0)^(r−1)(1−j/d)/(1−j/(2d))
       <=exp(−sum_(j=0)^(r−1)j/(2d))=e^(−x_r),

while the correction in TAIL is <=1+2x_r because2d−r>=d. The inequalities are uniform in d and do not derive the sign of A_N from a moment identity.

## 5. Scale m~sqrt(N) with explicit remainder

For2<=r<=d/2, expanding log(1−y) in its absolutely convergent series gives

    −x_r−r³/(3d²)<=log a_r<=−x_r.

The remainder is bounded by sum_(j<r)(j/d)², since for0<=y<=1/2,

    0<=−log(1−y)+log(1−y/2)−y/2
       <=y²/[2(1−y)]<=y².

The exact correction in TAIL belongs to[1+x_r,1+x_r+x_r r/d]. Thus

    (1+x_r)e^(−x_r−r³/(3d²))
      <=P_d(M>=r)
      <=(1+x_r+x_r r/d)e^(−x_r).                        (WINDOW)

Consequently M(M−1)/(4d) converges in distribution to the Gamma(shape2) law, whose survival function is(1+x)e^(−x). For r=O(sqrt(d)), WINDOW directly exhibits an error tending to0. No uniform convergence is claimed for r of order d and the limit law is not used to replace the arithmetic kernel in a sign proof.

The structural consequence is concrete: the gamma transform does not select a fixed index. The relevant indices follow a MOVING window of order sqrt(N). The infinitely many sign changes034 must be compensated against that real law.

## 6. Real signed budget of any FINITE prefix

For the real arithmetic t_m, define B_R=max_(1<=m<=R)t_m^−. SMALL proves for ALL d>=max(2,R)

    sum_(m<=R)P_d(m)t_m
      >=−B_R min{1,R(R−1)(R+1)(R+2)/[8d(d−1)]}.           (BUDGET)

Thus any FIXED set of adverse prefixes has adverse contribution to the gamma mixture O(N^(-2)), with explicit constant. It is not necessary to modify their signs or to assume the others positive. It is a quantitative inequality of the real transform and not the statement W>=0 rewritten.

BUDGET does not control all negative t_m: they are infinitely many by034 and their magnitudes may grow. LARGE controls tail probabilities, not automatically the product with an arithmetic functional of unknown magnitude. It is not concluded that SMALL/LARGE alone prove A_N>=0. The remaining obligation lives in the moving window and in its tails weighted by t_m.

## 7. Scope of a generic symmetry restriction

As a brief limit, the weights above and the positive cosh symmetry alone do not force the sign of their average. The model already used in CONE001, rescaled to Theta_model(v)=3+cosh(av), a=log2/u, gives for the exponential E_model=2Theta_model'/Theta_model

    A_2,model=E_model(u)−uE_model'(u)
      =2a(51−76log2)/289<0.

This model keeps the positive cosh representation and the parity required in034; it is not the real arithmetic and the same prime datum is not attributed to it. The computation only prevents turning a generic symmetry property into a sign argument for AVERAGE. It is not a new refutation of real W nor a global NO-GO. The real arithmetic needs to supply the quantitative compensation of t_m against P_d.

## 8. Evidence and residue

The script tools/power_signed_transform_035_verify.py symbolically verifies the mass/CDF identities, the polynomial sum of SMALL and the quotients; it evaluates no new N nor a list of m. The proof of WINDOW and of the limit scale is analytic. The script uses SymPy for formal identities and the intervals003 only in the generic-model check of§7; PASS.

No new W region or windowT is claimed. The result is a specific averaging representation together with uniform bounds and a finite signed budget. The next constructive step must estimate the arithmetic average at scale sqrt(N), not return to the refuted premise T_m>=0 nor build a list of positive cases. Papers untouched.
