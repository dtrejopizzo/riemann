# POWER_WEIGHTED_COEFFICIENT_034 — Oscillation of the Erlang weighted prefixes

Status: **PROVED**, independent review approved in POWER_COMPARISON_AUDIT_034.md and an additional review. Fixed rate u=63/2.

Theorem: the REAL numbers T_m of 033 take strictly positive and strictly negative values at arbitrarily large indices. In particular the sufficient condition T_m>=0 for ALL m, and even its version up to finitely many exceptions, is false. Not claimed: negative W, or an impediment to controlling the gamma combination of signs. Papers untouched.

## 1. Corpus and new reason

Read the project rules, COEFFICIENT_BALANCE033 and its audit, CONE001§§2,7 (positive REAL cosh representation of the exponential functional), TABLE_DESCENT018 (real positive T1), and the exact generator 033. Consulted ROUTES-TRIED-INDEX, master grid and CROSSWORD-TO-D.md on Pringsheim, series with positive coefficients, absolute monotonicity and Erlang mixtures.

The classical continuation lemma for a series with positive coefficients appears in antecedents on tails of phase 164; it is not presented as a new tool. The difference is the object and the hypothesis: a claim is proved about the specific sequence T_m of finite weighted prefixes, not about the full form W. Only the positive REAL representation already established for the exponential functional, its parity and coefficient series are used. The continuation lemma is proved below, instead of being invoked as an opaque box.

Relative to 033, no other index nor a campaign of diagnostics is added. The analytic structure gives a UNIFORM pattern and refutes the concrete premise of the sign of all T_m. The result is not turned into a conclusion about the sign of the real gamma combinations, whose positive Abel coefficients can still compensate the signs of T_m.

## 2. Real exponential functional and positive cosh representation

For v>1/2, the full normalized functional of an exponential is

    E(v)=psi((v+1/2)/2)−logpi+4v/(v²−1/4)
                        −2sum_(q>=2)Lambda(q)q^(−v−1/2).

It is EXACTLY the E0(v)=2L_power(v+1/2) of 033, with all arithmetic and polar terms. CONE001 establishes, via the real theta integral and Poisson, that

    E(v)=2Theta'(v)/Theta(v),
    Theta(v)=C int_0^infty Phi(t)cosh(vt)dt, C>0,
    Phi(t)=sum_(n>=1) pi n² e^(5t/2)
             [2pi n² e^(2t)−3]e^(−pi n² e^(2t))>0.

The constant factor does not affect the quotient. The doubly exponential decay justifies all derivatives and the analytic extension of this integral on compact sets. Theta is EVEN and Theta(v)>0 for ALL real v. In a small neighborhood of any real point v0, its real part remains strictly positive; there logTheta is defined analytically. Therefore the above quotient provides a real-analytic function E on the WHOLE real line and

    E(−v)=−E(v).                                         (ODD)

This is only a real/analytic property of the positive integral. No hypothesis is added about the behavior outside those neighborhoods of real points.

## 3. Correct generator and parity around 1

With the exact prefixes 033,

    T_m=sum_(j=1)^m j L[S_j],
    S_j(t)=e^(−ut)sum_(r=0)^j(ut)^r/r!,

the generator, initially convergent near z=0, is

    F(z):=sum_(m>=1)T_m z^(m−1)
         =[E(v)−vE'(v)]/(1−z)^3, v=u(1−z).             (GEN)

The factor z of the formula 033 has been divided ONCE. There is no second factor z in GEN.

By ODD, near v=0,

    E(v)=alpha1 v+alpha3 v³+alpha5 v⁵+...,
    E(v)−vE'(v)=−2alpha3 v³−4alpha5 v⁵−... .

Thus the apparent division by (1−z)^3 extends analytically at z=1 and

    F(1+s)=F(1−s),
    F^(q)(1)=0 for EVERY ODD integer q>=1.              (PARITY)

GEN and the real analyticity of E show moreover that F admits a local holomorphic continuation around EACH point of the positive real half-line. It is not claimed that the original Taylor series converges there without an additional hypothesis on its coefficients.

## 4. Real decay and nontriviality

The elementary real bounds for psi, logx−1/x<=psi(x)<=logx, and psi'(x)<=1/x+1/x², together with Lambda(q)<=logq, give for large positive v

    E(v)=log(v/(2pi))+O(1/v),
    E'(v)=O(1/v).

For the prime series and its derivative it suffices to compare with sum q^(−v+3/2), which is exponentially small; the polar rational term and its derivative are O(1/v), O(1/v²). These estimates use the explicit real expression of §2. By ODD, E' is even and the same bounds in modulus hold on the negative half-axis.

Letting real positive z tend to infinity, v=u(1−z) is negative and of modulus comparable to z. GEN implies

    F(z)=O(logz/z³)->0.                                 (DECAY)

F is not the zero function. For example F(0)=T1=L[S1] is precisely W[g2]/norm², which TABLE_DESCENT018 proves >1/8 at u=63/2. Nontriviality also follows from E growing like logv, so it cannot be a linear function cv.

## 5. Elementary continuation lemma for a positive tail

**Lemma.** Let f be real-analytic in a neighborhood of EACH point x>=0, with a Taylor germ f(z)=sum c_nz^n at 0 of positive radius. If c_n>=0 except for finitely many indices, that Taylor series has infinite radius.

Proof. Subtracting the polynomial of the first indices reduces to the case of ALL coefficients nonnegative without changing the possibility of local continuation at real points. Suppose finite radius R>0. The continuation given by f coincides with the initial germ along (0,R), by uniqueness of analytic continuation.

Choose small epsilon>0 such that f is holomorphic on |z−R|<epsilon and epsilon<R. Take a=R−epsilon/4. The Taylor series around a converges, for example, for h=epsilon/2. Its coefficients are

    f^(k)(a)/k!=sum_(n>=k)c_n binom(n,k)a^(n−k)>=0,

because a<R. Tonelli and the binomial theorem give

    sum_(k>=0)h^k f^(k)(a)/k!
      =sum_(n>=0)c_n sum_(k=0)^n binom(n,k)a^(n−k)h^k
      =sum_(n>=0)c_n(a+h)^n<infinity.

But a+h=R+epsilon/4>R, contradicting the radius. Hence there is no finite radius. QED.

The same argument holds for eventually nonpositive coefficients by applying it to −f. This lemma is the elementary form of the classical Pringsheim property needed; it neither requires nor provides external data about the arithmetic function.

## 6. Infinite oscillation theorem for T_m

Suppose T_m>=0 for ALL sufficiently large m. The lemma and §3 make the Taylor series of F entire; its sum coincides with the previous real continuation by uniqueness along the positive half-line. Choose an odd integer q larger than all exceptional indices (recalling that the coefficient of z^n is T_(n+1)). Then

    0=F^(q)(1)
      =sum_(n>=q) n!/(n−q)! ·T_(n+1).

Term-by-term differentiation and absolute convergence at 1 are justified NOW by the infinite radius; they were not presumed before. All summands are nonnegative. Therefore ALL T_(n+1) with n>=q vanish and F is a polynomial. DECAY forces that polynomial to be identically zero, contradicting §4.

Thus the T_m CANNOT be eventually nonnegative. Applying exactly the argument to −F proves that they cannot be eventually nonpositive either. Since the coefficients are real, one concludes

    for EVERY M there exist m_+>M, m_−>M
       with T_(m_+)>0 and T_(m_−)<0.                       (OSC)

This refutes in particular the premise 033 «T_m>=0 for ALL m». The proof does not locate the first negative index nor require evaluating it. Nor is it inferred that the series sum T_m or its moments converge at 1 for the real datum: those convergences only appeared under the eventually-positive hypothesis that led to contradiction.

## 7. Scope relative to the real gamma function

The exact identity 033 remains

    W[g_N]/norm²=sum_(m=1)^(N−1)
                      [v_Nm−v_N,m+1]T_m,
    v_Nm−v_N,m+1>=0.

OSC shows that a proof of the sign of these combinations cannot consist in declaring each T_m nonnegative, nor in correcting only finitely many exceptions. It does NOT say that the gamma combination is negative: its real weights may compensate infinitely many sign changes in a sequence of prefixes that are not all admissible autocorrelations.

The result is a refutation of the concrete sufficient criterion of 033, not a global NO-GO. The constructive continuation requires a signed bound on the adverse contributions AGAINST the real gamma weights, or a different arithmetic grouping preserving that compensation. The W obligation is not abandoned and no campaign over indices is extended.

## 8. Validation

The proof is analytic and does not need to evaluate new m or N. POWER_COMPARISON_AUDIT_034.md independently approves the normalization of GEN, the REAL cosh/ODD representation, the cancellation at z=1, the continuation lemma, the conditional use of series at 1 and the scope restricted to the T_m criterion. An additional review also read and approved those steps. Papers untouched.
