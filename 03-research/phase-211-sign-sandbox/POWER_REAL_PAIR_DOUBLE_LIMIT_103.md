# POWER_REAL_PAIR_DOUBLE_LIMIT_103 — Normalised real limit and transfer to finite parameters

Status: **PROVED analytic and pointwise test NEGATIVE, with independent audits approved and reproduction of the certificate.** See `POWER_REAL_PAIR_DOUBLE_LIMIT_AUDIT_103.md`. The later analytic extensions prove H/K strictly decreasing and, for the limiting REAL pair (J,K), E_q/K strictly decreasing, the unique crossing of U_*(q) and its positive double primitive for EVERY q>0. No global crossing is claimed for finite p nor a new W sign. Papers untouched.

Section11 adds an EXACT bridge to finite p: (Psi_p/K)'<0 and (D_p/K)'>0. The global crossing of the next finite U remains conditional on a mixed comparison different from EVEN4, still open.

## 1. Consultation and concrete target

Consulted the project rules, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md and CROSSWORD-TO-D.md; cross-checked075/077/078/081/089/099 and102 with its audited corollary. The search in those three indexes and the POWER corpus for `B−gamma E`, `B-gamma E`, `NEXT-REST`, `J4` and `ECT5` did not find this pointwise limit nor its test.102 already builds E>0 and locates U=B-gamma E, but does not decide the crossing of U.

The difference is to study a pointwise value of that REAL U by means of two rigorous limits and positive scalings. A positive sign in the limit would refute the proposed negative/positive crossing for FINITE parameters; a negative sign would only verify a condition at the origin. It is neither a new reformulation of W nor a test of generic potentials.

## 2. Positive scalings that preserve the sign of U

Keep all the definitions of102. For p>0, write c=M(p), a=M'(0) and

    Q_p=J-beta D_p, beta=ap^2/(ap-c), Psi_p''=Q_p.

Normalise the pair by

    A_p=pD_p, B_p=(ap/c)Psi_p.                     (SCALE)

Both scalings are positive. For an arbitrary pair A,B, the step102 with q>0 uses

    F(z)=z ZB(z)/ZA(z), d=F(q),
    E=G_q(dA-qB), gamma=ZB(0)/ZE(0), U=B-gamma E,
    G_q h(t)=(1/q)int_|t|^infinito sinh[q(s-|t|)]h(s)ds.

If A is multiplied by s>0 and B by t>0, then F,d are multiplied by t/s; the forcing dA-qB, E and U are multiplied by t, and gamma does not change. For SCALE, therefore,

    d_hat=(a/c)d, E_hat=(ap/c)E,
    gamma_hat=gamma, U_hat=(ap/c)U.                (SIGN-SCALE)

All sign statements about U_hat are statements of the same sign about the original U.

## 3. Convergence as p tends to infinity with derivatives and moments

075/081 prove c/p->0 and c->infinito; moreover pc->infinito suffices. Define the two-sided probabilistic convolution

    R_p f(t)=(p/2)int_R exp[-p|t-s|]f(s)ds.

The solution of D_p''-p^2D_p=cPhi-pJ with the boundary conditions of075 gives exactly

    A_p=R_pJ-(c/p)R_pPhi.                         (A-EXACT)

The anticausal representation with growing factors is not used to take this limit.

For sigma>0 and an integer k>=0 use the norm

    ||f||_(sigma,k)=int_R exp(sigma|t|)|f(t)|dt
          +sum_(j=0)^k sup_t exp(sigma|t|)|f^(j)(t)|.

Phi and J have these norms finite for every sigma,k. For p>sigma, R_p commutes with derivatives and its norm on each of these spaces is at most p/(p-sigma). This is obtained using exp(sigma|t|)<=exp(sigma|s|)exp(sigma|t-s|) and the exact integral of the kernel. Two integrations by parts, or integral Taylor of f(t+r)+f(t-r)-2f(t), give

    R_pf-f=R_p f''/p^2.

Thus R_pf->f in each declared norm, with cost at most [p/(p-sigma)]||f''||_(sigma,k)/p^2. A-EXACT implies A_p->J in all of them.

For B_p, put epsilon=c/(ap), which tends to0. The equation of Psi_p and the resolvent identity give the other exact formula

    B_p''=[a R_pPhi-J-a R_pJ''/(pc)]/(1-epsilon).
                                                               (B-EXACT)

Indeed beta D_p=[R_pJ-(c/p)R_pPhi]/(1-epsilon) and R_pJ-J=R_pJ''/p^2. Hence B_p''->aPhi-J in all the previous norms.

For even functions f with zero mass define

    G_0 f(t)=int_|t|^infinito(s-|t|)f(s)ds.

This operator is continuous on the declared spaces: on the parts of order0, the weighted output norm is bounded by sigma^-2 times the input one; for the first derivative the factor is sigma^-1, and from the second derivative on one uses (G_0 f)''=f. Zero mass ensures (G_0f)'(0)=0; parity of f ensures smoothness of the remaining derivatives. These bounds come from integrating the kernels r exp(-sigma r) and exp(-sigma r) over r>=0. All forcings B_p'' have zero mass by077, as does aPhi-J.

Since B_p=G_0(B_p'') and K=G_0(aPhi-J), it follows that

    A_p -> J, B_p -> K
    in ALL the norms ||.||_(sigma,k).          (PAIR-LIMIT)

In particular the values and derivatives on compacts converge, all polynomial moments, and all two-sided transforms and their derivatives on each real compact. No uniform superexponential bound in p has been required.

## 4. Continuity of the next step for each fixed q

Fix q>0 and apply102 to the normalised pair A_p,B_p. PAIR-LIMIT with sigma>q implies convergence of d_hat_p=q ZB_p(q)/ZA_p(q) to d_*=q ZK(q)/ZJ(q). The limiting denominator is positive.

The operator G_q is continuous with the weights sigma>q: the cost for order0 is the integral

    int_0^infinito exp(-sigma r)sinh(qr)/q dr
      =1/(sigma^2-q^2).

For the first derivative one uses the integral with cosh and for the higher ones the equation (G_qh)''-q^2G_qh=h. The even boundary conditions are preserved by the cosh balance already proved102. Thus, for fixed q, E_hat_p converges with moments and values to

    E_*(q)=G_q[d_*J-qK]>0.

Positivity and positive mass of E_* follow directly from102 applied to J,K, because K/J is strictly decreasing to0. By continuity of the masses,

    U_hat_(p,q) -> U_*(q)
      =K-[ZK(0)/ZE_*(q)(0)]E_*(q)                 (FIXED-Q)

pointwise, with derivatives and moments. Hence the first limit p to infinity is legitimate for each fixed positive q.

## 5. Limit q to zero of the pair (J,K)

Put Jmass=int_0^infinito J, Kmass=int_0^infinito K and b0=Kmass/Jmass>0. Using half-line or two-sided masses gives the same quotients. By the supertails,

    d_*/q=ZK(q)/ZJ(q) -> b0.

Then

    E_*(q)/q
      =G_q[(d_*/q)J-K] -> H=G_0(b0J-K).           (H-LIMIT)

Convergence holds with derivatives and moments. It is justified by domination of sinh(qr)/q by r exp(q0r), for fixed 0<q<=q0, using any weight sigma>q0. The kernels of the first derivative also converge; the higher derivatives follow from the differential equation. A non-dominated integral is not interchanged with the limit q->0.

Since K/J decreases strictly to0, b0 is a strict average of that quotient under J; hence 0<b0<(K/J)(0). The forcing b0J-K has zero mass and a unique negative/positive crossing. Its tail integral is strictly positive; hence H'<0 and H>0, by the same elementary argument used for Psi_p. In particular

    Hmass=int_0^infinito H>0.

H-LIMIT and the convergence of masses imply

    U_*(q) -> U_lim=K-(Kmass/Hmass)H.              (U-LIMIT)

This order is precisely p->infinito first, q->0 afterwards. No joint uniformity in p,q nor an unproved diagonal choice is needed.

## 6. Exact pointwise formula with I0,...,I6

Define I_m=int_0^infinito t^mPhi(t)dt for m=0,...,6. Absolutely convergent Fubini gives

    a=I2/I0, Jmass=I2,
    K(0)=aI1-I3/2,
    Kmass=aI2/2-I4/6,
    b0=Kmass/I2=a/2-I4/(6aI0),
    H(0)=(b0/2-a/6)I3+I5/24,
    Hmass=(b0/6-a/24)I4+I6/120.                   (FORMULAS)

For example int tJ=I3/2 and int tK=aI3/6-I5/24; the formulas for H follow from H=G_0(b0J-K). For the mass of H one uses int G_0f=(1/2)int t^2f. All denominators are strictly positive by the previous constructions.

The exact pointwise test is

    U_lim(0)=K(0)-[Kmass/Hmass]H(0).

It is preferable to decide the numerator without divisions

    N=K(0)Hmass-Kmass H(0),
    sign U_lim(0)=sign N,                         (POINT-TEST)

with the normalisation a=I2/I0 kept or with I0 positive clearing the denominators. Its sign has NOT been evaluated here. The separate pointwise design must fix in advance the integration parameters of the seven moments and accept either sign, without a campaign or adjustment after observing it.

## 7. Implication for finite parameters and limits of the inference

If POINT-TEST gave U_lim(0)>0, U-LIMIT would allow choosing a FINITE q>0 with U_*(q)(0)>0. For that fixed q, FIXED-Q would allow choosing a FINITE and sufficiently large p>0 with U_hat_(p,q)(0)>0. SIGN-SCALE would imply U_(p,q)(0)>0 for the original REAL remainder. By continuity, U would be positive in a neighbourhood of the origin, which would refute its proposed negative/positive single-crossing pattern.

If the value were negative, it would only verify the sign at the origin in this limit; neither the global crossing nor all parameters would be proved. A zero value or an enclosure that did not separate it would leave the test inconclusive. No alternative by itself implies a negative sign of W or closure of the global sign. No result102 is modified.

## 8. Single pointwise result and independent reproduction

After the prior audit of proof, design and code, the SINGLE run68812 ended exit0/FULL PASS128 panels. The independent reproduction91737 also ended exit0/FULL PASS128 with the same result and hash:

    P=[-3.1683047444094325e-13 +/- 2.16e-30],
    U_lim(0)=[-1.35855717857699839e-6 +/- 8.09e-24],
    hash=5090a71fd7dd4ae786a3f785ca8a4c32d6691cf92af912d4e5fffff9e583d080.

These are outward enclosures produced by `tools/power_real_pair_limit_origin_103_verify.py`, not approximations used as proof. Both endpoints of each enclosure are strictly negative. All design parameters were kept without adjustment and no additional tests were run.

Hence U_lim(0)<0. The proved limits also allow choosing a sufficiently small and FIXED q>0 with U_*(q)(0)<0, and for that q choosing a sufficiently large FINITE p with U_(p,q)(0)<0; the scalings are positive. No quantitative threshold of those parameters is obtained. This verifies a necessary condition of the crossing at the origin and is NOT a falsifier. It does not prove the global crossing of U, positivity of Xi, preservation under new reductions, new W/T coverage nor all orders. The positive branch of section7 remains as a correct conditional implication, but it is not the result of this run.

## 9. Later analytic extension: H/K decreases and the limiting U has a unique crossing

Status: **PROVED analytic, independent audits approved.** This deduction was obtained AFTER the pointwise test of section8. It requires no new data or certificates. The search for `H/K`, `H−rK`, `H-rK` and `Xi_limit` in the three indexes and the POWER corpus did not find this monotonicity; the occurrences of U_lim were only the formulas and the pointwise result103. EVEN4 is used directly, already proved102 from089.

Recall b0=Kmass/Jmass>0, H>0 and

    H''=b0J-K, K''=aPhi-J.

For r>0 put F_r=H-rK. Differentiating four times, keeping all contributions, gives

    F_r''''=(b0+r)J''-raPhi''-aPhi+J.             (FOURTH)

It is a combination of EVEN4=[J,Phi,J'',Phi''] not identically zero: its coefficient of J is1. By102 it has at most three positive roots counting multiplicities. All functions and derivatives of FOURTH have the same parities and supertails already justified; F_r and F_r'' are even and neither is identically zero.

If F_r had two positive roots counting multiplicities, lemma D2 of102 would force at least three positive roots of F_r'' and, applying it again to this even function, at least four of F_r''''. This contradicts the bound of EVEN4. Hence F_r has at most one simple positive root.

Let rho_H=H/K>0. If rho_H'(t0)=0 at t0>0, choosing r=rho_H(t0) would produce a double root of F_r, impossible. Thus rho_H' does not vanish on the half-line.

The direction is determined in time. For t large enough, tau(t)<=a/2. With I(t)=int_t^infinito(s-t)Phi(s)ds>0 and using that tau decreases,

    K(t)=int_t^infinito(s-t)[aPhi(s)-J(s)]ds
           >=(a/2)I(t),
    H(t)=int_t^infinito(s-t)[b0J(s)-K(s)]ds
           <=b0 int_t^infinito(s-t)J(s)ds
           <=b0 tau(t)I(t).

Hence

    0<rho_H(t)<=2b0 tau(t)/a ->0.

The continuous never-zero derivative has constant sign. Positivity and limit0 exclude the positive sign, so that

    (H/K)'(t)<0 for EVERY t>0.                    (H-RATIO)

Now define gamma_lim=Kmass/Hmass>0. Its reciprocal Hmass/Kmass is the average of rho_H under the positive density K on the half-line, so

    0<1/gamma_lim<rho_H(0).

By continuity, H-RATIO and its limit0, there exists a unique t0>0 where rho_H(t0)=1/gamma_lim. Consequently

    U_lim=K-gamma_lim H=K[1-gamma_lim rho_H]

is strictly negative before t0 and strictly positive after. The crossing is simple: at t0 its derivative is -gamma_lim K(t0)rho_H'(t0)>0. Moreover U_lim has zero mass by the choice of gamma_lim. We conclude

    Xi_lim(t)=int_|t|^infinito(s-|t|)U_lim(s)ds>0,
    Xi_lim''=U_lim, Xi_lim'(0)=0.                 (LIMIT-PRIMITIVE)

Positivity follows from the unique crossing and zero mass: the tail integral of U_lim is positive for t>0; hence Xi_lim'<0 and Xi_lim tends to0 from positive values. Parity, smoothness and supertails are preserved as in the previous primitives.

This GLOBAL proof for the limiting object implies retrospectively U_lim(0)<0, so that the previous pointwise certificate becomes logically redundant for that sign. Its chronology, design and result are kept; it is not presented as a computational consequence of this later theorem.

The sequential convergence103 does not automatically transfer the GLOBAL root count to finite parameters: it provides no uniform control of the tails nor excludes additional roots escaping from the compacts. Hence the unique crossing of U_(p,q) for ALL finite parameters, positivity of its Xi and indefinite preservation remain OPEN. No new W/T coverage nor all orders is obtained here.

## 10. Limiting pair (J,K): global crossing for EVERY q>0 without a second limit

Status: **PROVED analytic, independent audits approved.** This second extension was obtained after section9 and also uses no new certificates. The additional search for `E_q/K`, `E_*(q)/K`, `E−rK`, `E-rK` and the formula of the forcing in the three indexes and the POWER corpus did not find this consequence. Here p->infinito is kept, but q->0 is NO longer needed to conclude the crossing.

For q>0, write in this section

    d_q=q ZK(q)/ZJ(q)>0,
    E_q=G_q(d_qJ-qK)>0,
    E_q''-q^2E_q=d_qJ-qK.

It is exactly E_*(q) of sections4-5. All its derivatives have the even boundary conditions and supertails already justified102. For r>0 fix F=E_q-rK. Using K''=aPhi-J and commuting the constant operators,

    Lq(F'')=(d_q+r)J''-raPhi''
             +a(rq^2-q)Phi+(q-rq^2)J.            (ALL-Q-FORCING)

The combination of EVEN4 is nontrivial, since d_q+r>0 is its coefficient of J''. Hence it has at most three positive roots counting multiplicities. If F had two, D2 followed by Lq would force at least four of ALL-Q-FORCING, by GAIN102. Hence F has at most one simple positive root.

Consequently, for any q,t>0,

    derivative_t [E_q(t)/K(t)] != 0:

a stationary point and r=E_q(t)/K(t)>0 would produce a forbidden double root of F. To fix its sign a tail estimate of the quotient is NOT presupposed. Fix any t>0. The function

    q -> derivative_t [E_q(t)/K(t)]

is continuous in q>0: d_q and the Green kernel depend continuously on q, with uniform superexponential domination on each compact of q. Section5 already proves C1 convergence E_q/q->H as q->0. Thus

    (1/q) derivative_t[E_q(t)/K(t)]
       -> derivative_t[H(t)/K(t)]<0.

For that fixed t the derivative is negative when q is small enough. Since it is continuous and never zero, it cannot change sign on the connected interval q>0. Since t was arbitrary,

    derivative_t[E_q(t)/K(t)]<0
      for ALL q,t>0.                          (ALL-Q-RATIO)

For each q define gamma_q=Kmass/Emass_q>0 and rho_q=E_q/K. The function rho_q is positive, strictly decreasing, and therefore has a limit ell_q>=0 at infinity. The average of rho_q under the positive density K is strictly interior:

    ell_q<Emass_q/Kmass<rho_q(0).

The inequalities are strict because rho_q decreases strictly and K is positive on the whole half-line. There is no need to prove ell_q=0. The level Emass_q/Kmass=1/gamma_q is attained exactly once at some t_q>0. Hence

    U_*(q)=K-gamma_q E_q=K[1-gamma_q rho_q]

has exactly one negative/positive crossing, simple by ALL-Q-RATIO. The mass of U_*(q) is zero and one obtains

    Xi_q(t)=int_|t|^infinito(s-|t|)U_*(q)(s)ds>0,
    Xi_q''=U_*(q), Xi_q'(0)=0,
      for EVERY q>0.                             (ALL-Q-PRIMITIVE)

Positivity and smoothness follow from the same tail and zero-mass argument of the previous primitives. If the normalisation of the next remainder102 is kept for F_*(z)=zZK(z)/ZJ(z), its regularised remainder is exactly

    R_*(q;z)=d_q z ZXi_q(z)/ZE_q(z)>0
      for ALL q,z>0.

This is positivity of the scalar remainder of the limiting pair, not a statement about all minors of its kernel.

The final scope of103 improves on the pointwise test alone and the double limit: for p->infinito, the pair (J,K) admits the next positive numerator FOR ALL q>0. That global count is not transferred to FINITE p by convergence on compacts or moments. The global crossing of U_(p,q) for all finite p,q, later preservation and all orders remain OPEN. The previous pointwise certificate and its chronology are kept; no additional tests were run.

## 11. Exact bridge to FINITE p and sufficient mixed criterion still open

Status: **Identities and monotonicities PROVED, independent audits approved; additional criterion CONDITIONAL.** The antecedents093/095, the three indexes and the corpus were cross-checked before posing the criterion. The mixed comparison is not presented as new under another name: its relation with the particular Wronskian already recorded is identified below. No other certificate is run.

### 11.1. The finite pair contains exactly the Green function of the pair (J,K)

Fix p>0 and keep c=M(p), beta=ap^2/(ap-c), lambda=p^2c/(ap-c). The exact numerical identities are

    beta c=a lambda, beta p-p^2=lambda.

D-EQ, PSI-EQ and K''=aPhi-J imply

    (beta D_p+p^2Psi_p)''
      =beta(cPhi-pJ+p^2D_p)+p^2(J-beta D_p)
      =a lambda Phi-lambda J=lambda K''.

The difference beta D_p+p^2Psi_p-lambda K has zero second derivative and decays at infinity together with its first derivative. It is therefore identically zero:

    beta D_p+p^2Psi_p=lambda K,
    LpPsi_p=J-lambda K.                           (FINITE-BRIDGE)

Taking the two-sided transform of the second equation and evaluating at z=p gives ZJ(p)=lambda ZK(p). For the d_p of section10,

    d_p=pZK(p)/ZJ(p)=p/lambda,
    Lp E_p=(p/lambda)(J-lambda K).

The solution with the two superexponential boundary conditions is unique: a homogeneous difference would be a combination of exp(pt),exp(-pt), incompatible with both boundary conditions. Hence

    Psi_p=(lambda/p)E_p.                         (FINITE-GREEN)

ALL-Q-RATIO of section10 now applies EXACTLY, without a limit in p. Since lambda/p>0,

    (Psi_p/K)'<0,
    (D_p/K)'=-(p^2/beta)(Psi_p/K)'>0,
      for ALL FINITE p,t>0.                  (FINITE-RATIOS)

These are additional time comparisons of the real pair; not an informal transfer from p infinite.

### 11.2. Mixed forcing of the new numerator

For the next step of102, write A=D_p, B=Psi_p, F(z)=zZB(z)/ZA(z), d=F(q)>0 and E=G_q(dA-qB)>0. Define

    C=d lambda/beta>0, D=dp^2/beta+q>0,
    gamma=massPsi_p/massE>0,
    alpha=gamma q-q^2>0,
    U=Psi_p-gamma E.

alpha>0 is precisely the positivity of the residue102: gamma-q=r_q/d>0. Using FINITE-BRIDGE,

    LqE=CK-DPsi_p,
    Cp^2-Dlambda=-qlambda.

Commuting the two constant operators and keeping all contributions gives

    LpLqU=J''-a(lambda+gamma C)Phi
       +[lambda-q^2+gamma(C+D)]J
       -lambda alpha K.                          (MIXED-FORCING)

Thus it suffices to study a combination of the MIXED family

    [K,J,Phi,J''].                               (MIXED4)

J^(4) does not appear, but MIXED4 is NOT EVEN4=[J,Phi,J'',Phi''];102 does not prove that MIXED4 is Chebyshev. The real coefficient restrictions of MIXED-FORCING are kept instead of turning them into an already assumed generic statement.

### 11.3. What a mixed bound would prove, and why it is only sufficient

If MIXED4 were Chebyshev of dimension4 on the whole half-line with multiplicities, MIXED-FORCING would have at most three positive roots. It would not be identically zero, since its coefficient of J'' is1. Two applications of the Lp/Lq lemma of102, with parity and superexponential boundary conditions, would imply that U has at most one positive root counting multiplicity. Its mass is zero and it would not be zero, so it would have exactly one simple crossing.

To orient that crossing no limit of parameters is taken.099 proves all triples of the kernel of G_p at positive nodes, and hence also of the kernel of F=G_p/c. Taking a node to0 one obtains an auxiliary PSD block on {0,q,z}.102 proves that its two successive pivots are positive: d/q>0 and aF-d/q>0, with aF=F'(0). The double Schur congruence of099 leaves the diagonal R_next(z)/z; consequently

    R_next(z)>=0 for z>0.                       (SCALAR-INPUT)

For orientation this non-strict inequality suffices, and it is preserved when passing to the auxiliary node0. For z different from q the congruence is used directly; the removable value z=q is obtained by continuity. By the zero mass of U, Xi=G_0U has correct even boundary conditions even before knowing its sign. NEXT-REST102 gives exactly R_next(z)=d z ZXi(z)/ZE(z).

If the unique crossing of U were positive/negative, all its tail integrals would be negative, so that Xi'>0 and Xi(infinito)=0 would imply Xi<0. Its two-sided transform would be strictly negative and R_next(z)<0, contradicting SCALAR-INPUT. Hence the crossing would be negative/positive and Xi>0, as in the previous primitives. Then also R_next(z)>0.

The Chebyshev criterion MIXED4 is SUFFICIENT; it has not been proved to be necessary. MIXED-FORCING occupies a restricted class of combinations, and a direct proof for that class would also serve. Neither of these root bounds is claimed here.

The global sufficient route has an exact antecedent093/095. If K_odd=-K'/a, then K_odd''=v-w/a, with w=tPhi,v=-Phi', and K_odd(0)=K_odd(infinito)=0. The derivative of MIXED4 is, up to constant factors and column order,

    [w,v,w'',K_odd].

It is the PARTICULAR Wronskian of093/095. A global extended Chebyshev system of those four odd functions would imply MIXED4 by the lemma of one endpoint at infinity.093 controls an existing neighbourhood of the origin and095 the whole tail t>=64; the intermediate interval remains open. That antecedent is not hidden nor are its local signs extrapolated to the whole half-line.

The unconditional advance of this section is FINITE-RATIOS and the exact identification FINITE-GREEN. The next crossing of U for finite p, its positive numerator Xi, later preservation and all orders remain OPEN. No campaign has been opened and no paper has been modified.

### 11.4. The first three mixed levels are controlled globally

This comparison is deduced from EVEN4 without assuming the criterion MIXED4. For real coefficients not all zero, let

    f=A K+B Phi+C J.

Then

    f''=AaPhi-AJ+B Phi''+C J''

is a nontrivial combination of EVEN4: its coefficients cannot all be zero unless A=B=C=0. Hence it has at most three positive roots counting multiplicities. If f had three positive roots, lemma D2 would produce at least four of f'', a contradiction. Thus [K,Phi,J], and any reordering of those three functions, is Chebyshev3 on the whole half-line with multiplicities.

The time convexity contained in this result can also be fixed. Put

    tau=J/Phi, kappa=K/Phi=tau(K/J),
    S=kappa'/tau'.

tau'<0 by077 and (K/J)'<0 by102 imply kappa'<0, so S>0. Both quotients tau,kappa tend to0 at infinity. The Wronskian is exactly

    W(Phi,J,K)=Phi^3 tau'^2 S'.

Chebyshev3 with multiplicities implies that this Wronskian does not vanish: if it did, a nontrivial combination of the three functions would have a positive root of multiplicity at least3. Hence S' is continuous, does not vanish and has constant sign.

Suppose S'>0. For any t>0, the limits tau,kappa->0 give the tail average identity

    kappa(t)/tau(t)
      =[int_t^infinito S(s)(-tau'(s))ds]
                    /[int_t^infinito(-tau'(s))ds]
      >S(t).

The integrability of the numerator is exactly kappa(t), not an additional hypothesis on S. Consequently

    derivative_t[kappa/tau]
       =tau'[S-kappa/tau]/tau>0,

contradicting kappa/tau=K/J strictly decreasing. We conclude

    S'<0,
    d^2 kappa/d tau^2=S'/tau'>0.                 (MIXED-CONVEXITY)

Thus kappa is strictly convex as a function of the coordinate tau, on its whole range of values. In the order MIXED4=[K,J,Phi,J''], its first three Wronskians are strictly positive:

    W1=K>0,
    W2=W(K,J)=K^2(J/K)'>0,
    W3=W(K,J,Phi)=-W(Phi,J,K)>0.

The third equality is the exchange of the extreme columns. Only the FOURTH mixed Wronskian remains undischarged, or a direct sufficient bound for the restricted class MIXED-FORCING. That fourth sign is not inferred from MIXED-CONVEXITY nor is inheritance of order4 claimed.
