# Translation Gram kernel: uniform identity and obstruction of the layers

Status: **PROVED as an identity and as the obstruction of a class of certificates; independent targeted deduplication confirmed; final literal audit (cases/cross-check) approved.** Mathematical proof reviewed against cases. No new computations and no papers modified. The result does NOT decide the sign of the full integral kernel nor that of W for the real Phi.

**Additional independent audit:** fresh_global read §§2.1–2.2,8–8.3 and the addenda literally and issued a mathematical PASS: constants, transform domains, tail bounds and index ranges. The summary of tail repairs was corrected to distinguish Phi_M (all M>=1) from Q_M (M sufficiently large). This audit adds no real positivity.

## 1. Consultation and the object that changes

Consulted: the project rules, ROUTES-TRIED-INDEX/README.md and catalogues 03/04, the grid R162_2300_MASTER_GRID.md and CROSSWORD-TO-D.md; cross-checked POWER_THETA_SCHUR_DENSITY_075, POWER_RECIPROCAL_PFAFFIANS_083, POWER_GREEN_PAIR_TP2_SCOPE_111 and POWER_REAL_SECOND_PAIR_AND_TP2_112. Targeted searches: PSD slices/layers, t+s+2r, Lyapunov, CND/conditionally negative and Gram/double integral. The independent targeted cross-check confirms that it did not find the literal formula. The Gram/Pólya framework is classical; absence in this search is not presented as worldwide novelty.

075 keeps a cancellation to obtain a positive density, but not a Gram of arbitrary size. 083 factorizes all sizes and leaves a sign obligation on Pfaffians. 111 shows that individual monotonicities, even full parametric monotonicity, do not prove TP2. 112 proves TP2 for the REAL family, without claiming TP of all orders. The following proof tries to avoid that unproved inheritance via a single kernel in two variables, whose positive representation, if it existed, would pay for all sizes simultaneously.

The CND of C9/ROUND_003_B belongs to the metric of prime exponents; it is not the differential kernel appearing here. The actual failure of the raw Volterra kernel 105 is not the present obstruction either: the operator, the auxiliary variable and the refuted necessary condition all change. No absolute novelty is claimed for the integration procedure or for the Gram criteria.

**Public antecedent located later (2026-11-06).** Dylan Suvlu, draft of 24 September 2026, [Theta correlations and a causal range criterion for the Weil form, §3, (18)–(23)](https://dsuvlu.github.io/weil-form-operators/paper/theta-correlations-causal-range.pdf), contains this same normalized kernel. Algebraic cross-check new_structural_sign PASS; no refereed publication nor a full audit of the manuscript is claimed. If Z0=integral_R Phi and p=Phi/Z0, its j(x,y) satisfies EXACTLY j=A/Z0²: set tau=(x+y)/2,delta=(x-y)/2; p(v+delta)p(v-delta) is even in v, which allows replacing the endpoint |tau| by tau, and then v=tau+r. Its logarithmic response coincides with M of this note. The manuscript distinguishes pointwise positivity of the coupling from positivity of its form; it leaves the latter open. It is a direct antecedent of the representation, not a proof of the sign nor an automatic identification of RES-SOS§17 or of the certificate §19.9 with others' results. The previous targeted search had not located it; novelty must not be attributed to A or to this bridge because of that absence.

## 2. Exact kernel and convergence of its transform

Let phi be an even, positive, smooth function. For this section a Gaussian bound suffices

    phi(t)<=C exp(-N t^2), N>0,

together with sufficient decay of phi' for the differentiations and integrations by parts. The real Phi has these bounds, for every N>0, by its supertails; the quartic model of section 4 also satisfies the conditions with some N>0. Define

    Z(u)=integral_R exp(ut)phi(t)dt,
    A(t,s)=integral_0^infinito
               (t+s+2r)phi(t+r)phi(s+r)dr.             (A)

The factor t+s+2r may change sign. Its integral, however, is positive. Write

    tau=(t+s)/2, delta=(t-s)/2,
    P_delta(sigma)=phi(sigma+delta)phi(sigma-delta).

P_delta is even in sigma. Therefore

    A(t,s)=integral_tau^infinito 2sigma P_delta(sigma)dsigma
          =integral_|tau|^infinito 2sigma P_delta(sigma)dsigma>0.

This cancellation precedes any absolute estimate. The second expression and the Gaussian bound give

    0<A(t,s)<=C^2 exp(-2N delta^2)
                    integral_|tau|^infinito 2sigma exp(-2N sigma^2)dsigma
              =[C^2/(2N)]exp[-N(t^2+s^2)].             (DOM)

Consequently, for all complex u,v, the double transform of A converges absolutely, and all its derivatives in u,v are dominated uniformly on compacts. The order of no conditional integral is inverted.

The operator partial_t+partial_s is partial_tau. The fundamental theorem of calculus in the first integral of A proves

    (partial_t+partial_s)A(t,s)=-(t+s)phi(t)phi(s).

Integrating by parts against exp(ut+vs), with DOM and the supertails at the boundaries, gives

    (u+v) integral_R^2 exp(ut+vs)A(t,s)dt ds
       =Z'(u)Z(v)+Z(u)Z'(v).                          (LT)

There is no additional factor 2. For u+v!=0 one may divide; at u+v=0 the integral provides the removable continuation. All functions in LT are entire.

For u,v>0 and M=Z'/Z one obtains

    [M(u)+M(v)]/(u+v)
       =[integral_R^2 exp(ut+vs)A(t,s)dt ds]/[Z(u)Z(v)].

If A were a PSD kernel, this formula would produce the Gram of all finite blocks of the kernel of M. To justify the use of non-compact exponentials, truncate them first; DOM allows passing to the limit in each finite quadratic form. This is a precise sufficiency, NOT a proof of PSD of the real A.

### 2.1. Converse under DOM: exponents from an open interval suffice

**PROVED, independent literal review against cases; targeted cross-check.** The search did not find this literal converse in the cross-checked sources. It is a sharpening of the temporal bridge, not a new sign inequality. Let I be any nonempty open interval contained in (0,infinito). Under the hypotheses of §2, A is PSD on all of R if and only if the kernel K_M is PSD for all finite sets of nodes in I.

Sufficiency of A is already proved. For the converse, set w(t)=exp(-N t²) and H=L²(R,w(t)dt). DOM implies bilinear continuity of the temporal form:

    |integral A(t,s)f(t)conjugado(g(s))dt ds|
       <=[C²/(2N)](integral w) ||f||_H ||g||_H.

The span of e^(ut), with u ranging over I, is dense in H. Indeed, if h is orthogonal to all of them, J(z)=integral h(t)w(t)exp(zt)dt is entire by Cauchy–Schwarz and Gaussian domination, also for its derivatives on compacts. J vanishes on I, hence on the whole plane. At z=i tau it is the Fourier transform of h w, which is integrable by Cauchy–Schwarz. Fourier uniqueness (or Gaussian convolution followed by approximation of the identity) gives h w=0 and h=0.

LT and Z(u)>0 show that PSD of K_M on I gives nonnegativity of the temporal form on that span. Density and continuity extend it to H. For arbitrary temporal nodes t_i and coefficients c_i, approximate sum_i c_i delta_(t_i) by smooth compact bumps of mass c_i. Each bump belongs to H; continuity of A on compacts allows passing to the limit of their quadratic values and gives sum_ij c_i conjugado(c_j)A(t_i,t_j)>=0. It is not required that the norms of the bumps remain bounded.

Density of a discrete ladder of exponents under a mere Gaussian bound is not claimed. Nor does any fixed matrix size suffice: the hypothesis uses all sizes within I. For the real Phi, this identifies exactly the scope of the temporal target without proving it. For the hyperbolic model, the Gram of all orders already proved in POWER_HYPERBOLIC_MODEL_GRAM now does imply PSD of its full A; this does not transfer to the real Phi.

### 2.2. For the real Phi, local temporal positivity implies global

**PROVED, independent review against cases; targeted cross-check.** This literal formulation was not found in the cross-checked sources; no worldwide novelty is attributed to the continuation principle for analytic kernels. This sharpening corrects the earlier caution that proving A PSD on the positive half-line would necessarily leave an independent obligation on its cross blocks: for the real Phi, analyticity allows recovering those crossings. The hypothesis is still PSD in ALL sizes, not positivity of entries nor of a fixed number of minors.

The theta series defining Phi converges holomorphically in |Im z|<pi/4. On each compact of that strip, Re(exp(2z)) has a positive lower bound times exp(2Re z). Hence, in the integral defining A(t,s), the tail in r is dominated uniformly on compacts of the product of strips by a polynomial in r,exp(2r) times exp(-c exp(2r)), c>0. The theta series and the integral give a function A jointly holomorphic in

    |Im t|<pi/4, |Im s|<pi/4.

Suppose now that A is PSD on some nonempty open real interval I. Fix 0<rho<pi/4, for instance rho=pi/8. If a set E is already PSD and contains an interval around c, the mixed matrices formed by arbitrary points of E and evaluation derivatives of orders 0,...,m at c are PSD. Indeed, each derivative is approximated by finite differences of evaluations inside that interval; the approximating matrices are congruences of PSD matrices of points of E and their limit preserves PSD.

For any new point x with |x-c|<rho, formally replace its evaluation by

    T_m(x)=sum_(j=0)^m (x-c)^j partial^j delta_c/j!.

Every joint matrix of old points and these T_m(x) is PSD by the previous step. The double Taylor series of A in the bidisc centred at (c,c) converges absolutely for the new points; the single series of A(t,y), with y a fixed old point, does the same for the crossings. Sending m to infinity gives exactly the matrix of A at the old and new points. Thus E united with (c-rho,c+rho) is still PSD.

Starting from I and choosing interior centres near the endpoints, the fixed radius allows successive extension to intervals covering all of R. One concludes that, for the real A, PSD on ANY open temporal interval is equivalent to global PSD. It is not necessary to control the crossings A(t,-s) separately once that local all-sizes hypothesis is proved. The square-root separation discussed later does not prove such a hypothesis: its remainder still lacks a signed bound.

This continuation only changes the scope of the bridge; it gives no factorization, proves no new real minor and does not enlarge T. Combined with §2.1, it identifies the local and global formulations without replacing the sign obligation.

### 2.3. Restriction of the translational Hankel factorization; classical antecedent

**PROVED as a representation restriction, review fresh_global.** No novelty is attributed to the mechanism: [Blower, Integrable operators and the squares of Hankel operators](https://eprints.lancs.ac.uk/id/eprint/615/1/integrablepaper.pdf), Theorem 1.2 and (1.15)–(1.16), obtains factorizations under concrete ODE and sign hypotheses. Its §2.5, (2.14), exhibits the same obstacle through the factor x+y for parabolic cylinder functions. The present application allows an arbitrary auxiliary Hilbert space.

The A of §2, with phi positive, does not admit on t,s>0 a representation

    A(t,s)=integral_0^infinito <h(t+r),h(s+r)>_H dr,  (HANKEL)

with h measurable and finite diagonal integrals. Indeed, for delta>0, subtracting the same translated representation gives

    A(t,s)-A(t+delta,s+delta)
       =integral_0^delta <h(t+r),h(s+r)>_H dr,

a PSD kernel. Dividing by delta and using differentiability of the known A forces -(partial_t+partial_s)A=(t+s)phi(t)phi(s) to be PSD. At two distinct points t,s its determinant is

    -(t-s)²phi(t)²phi(s)²<0,

a contradiction. h is not differentiated and no additional regularity is imposed. The argument excludes (HANKEL) in the original variables; it does not exclude PSD of A, a general Gram representation, other coordinates or an additional transformation. Nor does it contradict an expression as a sum of two products of Hankel operators. It is a sharpening of the scope of a classical tool, not a sign proof nor a new general obstruction.

## 3. Layer decomposition and sufficient certificate

In the second integral of A set v=sigma^2-tau^2. The Jacobian is dv=2sigma dsigma and one obtains exactly

    A(t,s)=integral_0^infinito S_v(t,s)dv,
    S_v(t,s)=phi(sqrt(tau^2+v)+delta)
                   phi(sqrt(tau^2+v)-delta).           (SLICE)

Each layer is pointwise positive and symmetric in t,s. These two properties do NOT imply PSD. If S_v were PSD for all v>=0, then A would be: for any number of nodes and real coefficients, integrate its nonnegative quadratic form. The integrals of the entries are finite by DOM. The same argument covers complex coefficients by separating real and imaginary parts.

The **class of positive-layer certificates** refers only to this condition: S_v PSD for ALL v>=0 and ALL finite sets of real nodes. Section 5 refutes that condition for the real Phi. It does not refute other positive representations of the same A.

## 4. An integrable model where the layers are Gram

Take phi(t)=exp(-a t^4-b t^2), with a>0 and b real; a=0,b>0 is also allowed. Exact expansion of the powers gives

    S_v(t,s)=phi(t)phi(s)
       *exp[-2av^2-2bv-4av(t^2+s^2)]*exp(4avts).     (QUARTIC)

For v>=0, the last factor is a PSD kernel because

    exp(4avts)=sum_(n>=0) [(4av)^n/n!] t^n s^n.

On each finite set of nodes the series is absolutely convergent and its quadratic form is a sum of squares with nonnegative coefficients. The other factors of QUARTIC are a positive scalar and a positive diagonal congruence. Thus ALL layers are PSD and so is A. The argument does not extrapolate this property from the quartic class to the real theta.

### 4.1. The conditionally positive logarithm demands more than the quartic Gram

**PROVED for the model, not for Phi.** Construction, independent algebraic review theta_joint and targeted cross-check (2026-11-05). This literal application was not found in the cross-checked sources. The classical criterion considered here is CPD of log A: for every finite set and real coefficients summing to zero, sum c_i c_j log A(t_i,t_j)>=0. It is equivalent to PSD of the anchored logarithm B(t,s)=log A(t,s)-log A(t,0)-log A(0,s)+log A(0,0). If B is PSD, the exponential series and the Schur product make exp(B) PSD; a diagonal congruence recovers A. Thus it would suffice for all orders. Normalizing A by its diagonal does not change CPD of the logarithm. CND of the layers of §5 is not being asked for.

This additional condition fails even for the positive model of §4 with b=0. Indeed,

    A(t,s)=exp[-a(t^4+s^4)] Z(4a(t²-ts+s²)),
    Z(c)=integral_0^infinito exp(-2av²-cv)dv, a>0.

Let V be the positive variable with density proportional to exp(-2av²). The expansion of log Z around 0 has coefficients (-1)^k kappa_k(V)/k!. Its moments, computed via Gaussian integrals, give

    kappa_5(V)=(2sqrt(a))^(-5)sqrt(2/pi)
                  *[3-40/pi+96/pi²] < 0.

The sign requires no numerical approximation: 3x²-40x+96 decreases on [314159/100000,314160/100000], an interval containing pi, and its value at the left endpoint is -548368157/10^10. Since the coefficient of t^5s^5 in (t²-ts+s²)^5 is -51,

    [t^5s^5]log A=(51/120)(4a)^5 kappa_5(V)<0.

Take the six nodes t_j=jh, j=0,...,5, with c_j=(-1)^(5-j)binom(5,j). Their sum is zero and they annihilate all powers of degree less than 5. By analyticity, the form of log A on these coefficients is h^10(5!)²[t^5s^5]log A+o(h^10), negative for h>0 sufficiently small. Therefore log A is not CPD even though A and all its layers are PSD. This rules out inferring the logarithmic criterion from those general properties; it does NOT refute log A for the real Phi nor real positivity.

**Separate real diagnostic, NUMERICAL, not certified:** a single anchored matrix was evaluated at the nodes {0,1/4,1/2,1,2}, with anchor 0, 60 digits, ten theta modes and normalized quadrature in r from 0 to 2. The four approximate eigenvalues were 0.000708516447944, 0.0271085148761, 0.329726647588 and 2.85506271832. Truncation/quadrature errors were not rigorously enclosed. This diagnostic does not falsify the candidate, but neither does it prove CPD nor authorize extrapolating sizes. No search over nodes was undertaken.

For t,s>0 one can write exactly, with q=t+s+2r, p=-Phi'/Phi and probability mu proportional to q Phi(t+r)Phi(s+r)dr,

    partial_t partial_s log A
      = Cov_mu(p(t+r),p(s+r))
        - Cov_mu(1/q,p(t+r)+p(s+r)) - (E_mu[1/q])².

The last term is negative and mu depends on both nodes: the covariance notation does not constitute a Gram. A specific estimate proving the criterion for theta is still missing. There is no new sign coverage nor T window.

**Second real diagnostic, pointwise and NUMERICAL (2026-11-05):** only the coefficient [t^5s^5]log A at the origin was examined, motivated by the preceding quartic falsifier. With Phi_i=Phi^(i), the exact coefficients are

    a_ij = 1/(i!j!) integral_0^infinito
           [2r Phi_i(r)Phi_j(r)
            +i Phi_(i-1)(r)Phi_j(r)+j Phi_i(r)Phi_(j-1)(r)]dr,

omitting terms with negative index. Parity annihilates odd i+j; hence, to extract t^5s^5 from log(A/A00), the expansion log(1+z) up to z^5 in the truncated algebra i,j<=5 suffices. The twelve independent symmetric integrals of even total degree were computed, with analytic derivatives up to 5, ten theta modes, 70 digits and fixed panels in r from 0 to 2. Approximate result: A00=0.01006067751793984255436 and [t^5s^5]log A=+1.90430357842542673366828848575517. The corresponding mixed derivative multiplies by (5!)². There is no enclosure of tail/quadrature errors: it is not a sign certificate. The cancellation among the five terms of the expansion was retained. No other orders or blocks were searched. This test does not reproduce the quartic falsifier in theta and does not prove CPD, not even all local minors.

**Scope decision:** the two real diagnostics do not refute the criterion, but they do not supply the missing uniform estimate. Starting a table of orders or extrapolating from these values is not justified. The real condition remains OPEN, with no new W/T positivity.

**Update, 2026-11-06: complex diagonal tests at the alternating and even cusps eventually positive (PROVED).** Computation global_restart_checked; independent mathematical audit arithmetic_fresh_candidate PASS and a second review PASS for both mechanisms. The targeted cross-check of formula and locus in indices, grid, crossword and phase 209/211 sources located no literal antecedent; already-registered tools are combined, without claiming priority. For z=x+iy, x>=0, 0<y<pi/4, define

    F=A(z,bar z)=2 integral_x^infinito v|Phi(v+iy)|²dv>0,
    b=|Phi(z)|², L=integral_x^infinito |Phi(v+iy)|²dv,
    J=integral_x^infinito v|Phi'(v+iy)|²dv,
    K=integral_x^infinito v Phi'(v+iy)conjugado(Phi(v+iy))dv,
    D=(F/2)J-|K|²>=0.

The last inequality is Cauchy–Schwarz with weight v. The superexponential boundaries and integration by parts give Re K=-(xb+L)/2, partial_t A=L+2K and partial_t partial_s A=2J-b at (z,bar z). Therefore, for H=partial_t partial_s log A, defined locally there because F>0,

    F² H(z,bar z)=F(2J-b)-|L+2K|²=4D+L²+2xbL-Fb,
    D=(F/2) min_(a complejo) integral_x^infinito
                                     v|Phi'(v+iy)-a Phi(v+iy)|²dv.

The second identity is the orthogonal projection onto the COMPLEX line generated by Phi in L²(v dv); its minimum is J-|K|²/(F/2).

**Alternating cusp, x=0.** Set epsilon=cos(2y), h=log(2)/2. The FULL theta bounds SMALL/LARGE and the global Gaussian bound of «Modular cusps» in POWER_GLOBAL_ROUTE_REVIEW give L>=c epsilon^(-4), integrating LARGE over [h,h+epsilon]; F<=C epsilon^(-5), integrating the global bound from 0; and b<=C epsilon^(-N)exp(-a/epsilon), with positive constants and N fixed. Hence F²H>=c²epsilon^(-8)-C epsilon^(-N-5)exp(-a/epsilon)>0 for epsilon sufficiently small.

**Even cusp, x=h: the projection defect is bounded, not the total integral.** For 0<=u<=1, w=exp(2(h+epsilon u+iy))=2i+zeta satisfies zeta=2epsilon(1+2iu)+O(epsilon²), with uniform C1 remainder. Full Poisson gives theta(2i+zeta)=zeta^(-1/2)+R(zeta). On this segment Re(1/zeta)>=c/epsilon; R and its derivatives up to order 3 are bounded by a fixed power of epsilon^(-1) times exp(-c'/epsilon). This is proved by differentiating the series of nonzero dual modes: each derivative only adds powers of their indices and of zeta^(-1), absorbed by extracting part of the Gaussian exponential. With Phi=w^(5/4)[w theta''+(3/2)theta'], the leading term is (3/4)(2i)w^(5/4)zeta^(-5/2), by exact cancellation of the zeta^(-3/2) term. Thus there exists C0 different from 0 such that

    Phi(h+epsilon u+iy)=C0 epsilon^(-5/2) f_epsilon(u),
    f_epsilon -> f(u)=(1+2iu)^(-5/2) en C1([0,1]).

The minimum m(f)=min_(beta complejo) integral_0^1|f'-beta f|²du is positive and continuous under this convergence, by its projection formula and because integral|f|²>0. More precisely, with I0=integral_0^1|f|²<=1,

    m(f)=(1/(2I0)) integral_0^1 integral_0^1
                       |f'(u)f(v)-f(u)f'(v)|²du dv,
    |f'(u)f(v)-f(u)f'(v)|²
        =100(u-v)²[(1+4u²)(1+4v²)]^(-7/2),
    m(f)>=100/(2*6*5^7)=1/9375.

One uses integral integral(u-v)²=1/6. Eventually m(f_epsilon)>=1/18750 and |f_epsilon(0)|²<=2. Restricting the integral of the global minimum to [h,h+epsilon], using v>=h and substituting beta=epsilon a preserves the minimum over ALL complex scalars; one gets

    min_(a complejo) integral_h^infinito v|Phi'-a Phi|²dv
        >=h|C0|² epsilon^(-6)/18750,
    b<=2|C0|² epsilon^(-5),
    F²H>=4D-Fb
        >=F|C0|² epsilon^(-6)[h/9375-2epsilon]>0

for epsilon sufficiently small. No upper bound on F is needed, nor excluding contributions from other cusps. No numerical threshold is fixed: the C1 convergence provides an eventual interval, not quantified here.

**Scope.** Only these two necessary tests PASS: CPD of log A and the global sign remain OPEN, with no new route nor W/T coverage. Non-vanishing outside these diagonals is not assumed, nor is an asymptotic of the total integral used from the profile of a single cusp; in particular the local coefficient 7/16 is not attributed to the full H. No computations or changes to papers.

**Limit of the joint-projection extension (PROVED, same update).** Computation global_restart_checked; independent audit arithmetic_fresh_candidate PASS and second review PASS. Targeted cross-check in the three indices and corpus with no literal antecedent located; E73_025§7/E73_030 regularize another Cauchy projection via Hermite coordinates, and R164_401/491 use difference quotients for density. The finite-difference tool is classical. Fix FIRST z0=h+iy inside the strip, close to the even cusp with Phi(z0)!=0, a compact interval I=[0,ell],ell>0, and a fixed positive continuous weight w. In L²(I,w du), set f0(u)=Phi(z0+u), f_eta(u)=Phi(z0+eta+u), and P_eta the projection onto their COMPLEX span. For eta=i tau, tau real nonzero sufficiently small, both nodes keep real part h. The uniform C2 bound of Phi on the interior compact of the strip gives

    ||f0'-(f_eta-f0)/eta||=O(|eta|),
    R_00=||(I-P_eta)f0'||²=O(|eta|²),
    R_ij=<(I-P_eta)f_i',(I-P_eta)f_j'>, i,j en{0,eta}.

With b_i=f_i(0), B=bb*, one has B_00=|Phi(z0)|²>0 fixed. Hence there is NO c>0 independent of eta such that R>=cB for all these pairs: it suffices to evaluate at the first coordinate vector. Independence of f0,f_eta is not needed nor assuming A PSD. Even if c depends on z0,I,w, uniformity in the separation fails. Only THIS payment of the boundary by THIS residual is excluded; not c(eta), separation-dependent renormalizations, other terms of the scalar identity, other boundary/projection matrices nor general Gram approaches. CPD and global sign remain OPEN. Moreover, proving only S=A^(odot2) odot H PSD does not prove H PSD: entrywise division by A² does not preserve positivity in general. No new route, computations or edited papers.

**Full horizontal average on a fixed band (PROVED, 2026-11-06).** Proposal, computation global_restart_checked and joint_sign_fresh_review; independent audits arithmetic_fresh_candidate PASS and second review PASS. The targeted cross-check in the three indices and corpus did not locate this literal estimate; GLOBAL already had local lower epsilon^-4 and horizontal upper epsilon^-5. The difference is keeping ALL modes and estimating their integrated oscillatory crossings, without isolating a cusp. With epsilon=cos(2y) decreasing to 0, sigma=sin(2y), define

    B_y=integral_2^4 [log(t)/(2t)] |Phi((log t)/2+iy)|²dt.

Then, with c_*=315(log2)²/(512sqrt2)>0,

    epsilon^(9/2) B_y -> c_*,
    A(iy,-iy)>=B_y>=c epsilon^(-9/2)

for epsilon sufficiently small and some c>0. The equivalent is claimed ONLY for B_y, not for the full A.

**Crossings and infinite sums.** The exact modal formula is

    Phi((log t)/2+iy)
      =2pi² t^(9/4) exp(9iy/2) S_4(t)
         -3pi t^(5/4) exp(5iy/2) S_2(t),
    S_j(t)=sum_(n>=1) n^j exp[-pi t(epsilon+i sigma)n²].

For each fixed epsilon>0, the series, the double products and the following amplitude derivatives converge absolutely and uniformly in t∈[2,4]. Thus one integrates and differentiates first with absolutely convergent sums. For n!=m, set Q=n²+m², d=n²-m² and a_nm(t)=[log(t)/(2t)]t^(9/2)exp(-pi epsilon t Q). Integrating by parts against exp(-i pi sigma d t), with sigma>=1/2 eventually, gives

    |integral_2^4 a_nm(t)exp(-i pi sigma d t)dt|
        <=C exp(-pi epsilon Q)/|d|.

Indeed, the boundary term and the integral of |a_nm'| are bounded by C(1+epsilon Q)exp(-2pi epsilon Q); the additional factor is absorbed in half of the exponential. Since n4m4/(n²-m²)<=n7/(n-m) for n>m, ALL crossings of the S_4 term have absolute sum

    <=C sum_(n>=1) n7(1+log n)exp(-pi epsilon n²)
    <=C epsilon^(-4)[1+log(1/epsilon)]
     =o(epsilon^(-9/2)).

The second bound follows from log n<=log(1/epsilon)/2+n sqrt(epsilon) and the Gaussian bounds for power sums. Near-resonances are not discarded: their exact phases are integrated on this fixed band.

**Diagonal and constant.** For f_t(s)=s8 exp(-2pi t s²) and q=sqrt(epsilon),

    epsilon^(9/2) sum_(n>=1)n8 exp(-2pi epsilon t n²)
       =q sum_(n>=1) f_t(nq)
       -> integral_0^infinito f_t(s)ds
        =Gamma(9/2)/[2(2pi t)^(9/2)]

uniformly in t∈[2,4]. The error of the Riemann sum is bounded by q integral|f_t'|=O(q), uniform on that compact. Using Gamma(9/2)=105sqrt(pi)/16, the factor 4pi4t^(9/2) reduces the diagonal limit to 105/(128sqrt2); integrating the weight log(t)/(2t) contributes 3(log2)²/4 and gives c_*. The weighted L² norm of the leading term is O(epsilon^(-9/4)); the absolute Gaussian bound sum n²exp(-pi epsilon t n²)<=C epsilon^(-3/2) gives norm O(epsilon^(-3/2)) for the lower term. Its square is O(epsilon^-3) and its crossing with the leading term is O(epsilon^(-15/4)), by Cauchy–Schwarz, both o(epsilon^(-9/2)). This completes the equivalent of B_y with the full theta series, without computations.

**An isolated cusp does not approximate the full integral.** For h=log2/2 and each FIXED c0>0, the preceding full local Poisson bounds |Phi(v+iy)|<=C_(c0)epsilon^(-5/2) on h<=v<=h+c0 epsilon. Therefore

    integral_h^(h+c0 epsilon) 2v|Phi(v+iy)|²dv
       =O_(c0)(epsilon^-4),
    [ese integral]/A(iy,-iy)=O_(c0)(sqrt(epsilon))->0.

Only this segment of the even cusp h, with width c0 epsilon and c0 fixed, is claimed. It is not extrapolated to bands of arbitrary cusps nor is an asymptote of the total A or of H deduced. The result controls the positive part of a full horizontal integral; it does not prove CPD, PSD of A, global sign nor new W/T coverage. No new route nor changes to papers.

The equivalent of the full A for the fixed integer scales is proved later in §16 via an additional argument over ALL t>=1; it is not inferred from the equivalent of B_y.

### 4.2. The full theta kernel is not log-supermodular on the whole half-line

**PROVED, independent review theta_joint/cases; targeted deduplication (2026-11-05).** This refutes a property of entries, not matrix positivity. For any compact K contained in (0,infinito), uniformly in s in K, as t tends to infinity,

    H(t,s)=partial_t partial_s log A(t,s)
           =-1/(t+s)²+O_K(exp(-2t)) < 0

for t sufficiently large. Therefore A is not TP2 on the whole positive half-line. The difference with §5 is essential: here the full theta INTEGRAL is kept; not only its layers are refuted. The TP2 results of 073/112 concern other kernels.

**Proof with differentiated error.** Set Y=pi exp(2t), u=t+s, p=-Phi'/Phi. The first mode gives exactly

    Phi(t)=2pi² exp(9t/2) exp(-Y)(1-3/(2Y))(1+R(Y)),

with R and its logarithmic derivatives up to any fixed order bounded by a polynomial in Y times exp(-3Y), for Y large. This is obtained term by term from the theta series: the modes n>=2 carry the factor exp[-(n²-1)Y], and their derivatives only add powers of n and Y. Introduce v=Y(exp(2r)-1) and r=log(1+v/Y)/2. Then

    A(t,s)/(Phi(t)Phi(s))=[u J(Y,s)+K_1(Y,s)]/(2Y),
    J=integral_0^infinito exp(-v)(1+v/Y)^(5/4)
          B_Y(v) Phi(s+r)/Phi(s) dv,
    K_1=integral_0^infinito exp(-v)(1+v/Y)^(5/4)
          B_Y(v) Phi(s+r)/Phi(s) log(1+v/Y) dv,
    B_Y(v)=[(1-3/(2(Y+v)))/(1-3/(2Y))]
            *[(1+R(Y+v))/(1+R(Y))].

The exponent 5/4 includes the Jacobian; the sum of remaining modes is not omitted. Taylor in v/Y gives

    J=1+(5/4-p(s)/2)/Y+O_K(Y^-2),
    K_1=1/Y+O_K(Y^-2).

These remainders keep their order under (Y partial_Y)^j partial_s^k with j+k<=2. To justify this, first differentiate the integrands on the fixed domain v>=0. For v<=sqrt(Y), Taylor with remainder of the smooth functions (including Phi near K) produces bounds by C_K(1+v)^m/Y² for some fixed m, integrable against exp(-v), also after those derivatives. The rational factors of B are regular for Y large and their corrections begin at order v/Y²; the theta correction is exponentially smaller. For v>=sqrt(Y), Phi and its derivatives of fixed order are bounded on the half-line starting at min K, while min_K Phi>0. The derivatives of r have bounded growth, and the other factors have at most polynomial growth in v and Y. Because of exp(-v), the integrals of that tail, after differentiation, are O_K(Y^-N) for each fixed N. No merely pointwise approximation is differentiated and no terms of a moving cutoff are discarded.

Consequently, with a differentiated remainder as well,

    log A=log Phi(t)+log Phi(s)+log u-log(2Y)
           +(5/4-p(s)/2+1/u)/Y+O_K(Y^-2).

Differentiating once in each variable gives, more precisely,

    H(t,s)=-1/u²
       +[p'(s)+2/u²+2/u³]/Y+O_K(Y^-2).

The first contribution dominates because s stays in a compact and Y grows exponentially. This proves the announced negative sign. By continuity, around one of those pairs there exist small increments h,k>0 such that

    A(t,s)A(t+h,s+k)-A(t,s+k)A(t+h,s)<0.

These are RECTANGULAR minors with different row and column sets, not principal minors of a Gram matrix. The inequality rules out global TP2/log-supermodularity and, for H, a representation via products of functions all nonnegative. **It does NOT rule out a Gram of signed functions, PSD of H, CPD of log A nor PSD of A.** The candidate of §4.1 remains OPEN. There is no new W/T positivity nor modification of papers.

### 4.3. The leading tail model is not a PSD reference either

**PROVED, cases/theta_joint; targeted cross-check (2026-11-05).** It is a corollary of the continuation principle of §2.2 applied to two distinct explicit objects. Define

    G0(t,s)=(t+s)/(exp(2t)+exp(2s)),
    H0(t,s)=sech²(t-s)-1/(t+s)², t,s>0.

Neither G0 nor H0 is PSD in all sizes on ANY nonempty open interval contained in (0,infinito). This includes every tail, however far it starts. It is not a falsifier of the real A nor H.

For G0, the denominator does not vanish on the product of strips |Im t|,|Im s|<pi/4: both exponentials have positive real part. If G0 were PSD on an interval, the finite differences and Taylor series of §2.2 would extend it by steps of fixed radius to the whole real line. But G0(t,t)=t exp(-2t)<0 for t<0, a contradiction.

For H0, fix any compact [a,b] of the positive half-line connecting the assumed interval with t*=1/4. With radius rho<min(a/4,pi/8), neither t+s nor cosh(t-s) vanish on the bidiscs and the required mixed domains. The same old-points-plus-jets argument propagates PSD along the compact. This contradicts H0(1/4,1/4)=-3. No attempt is made to reach 0 with a fixed radius; the contradictory point is strictly positive. On the positive half-line, exactly H0=partial_t partial_s log G0 holds.

**Relation with the full theta.** Fix x,y in a compact and set t=L+x,s=L+y, L large. Write Yt=pi exp(2t), Ys=pi exp(2s), E=Yt+Ys and u=t+s. The change v=E(exp(2r)-1), with h=v/E, keeps all modes and gives

    A/(Phi(t)Phi(s))=(1/(2E)) integral_0^infinito exp(-v)
          [u+log(1+h)](1+h)^(7/2) B_t(v)B_s(v)dv,

with B_j=[(1-3/(2Yj(1+h)))/(1-3/(2Yj))]·[(1+R(Yj(1+h)))/(1+R(Yj))], using the theta R of §4.2. Now Yt,Ys are comparable to E. The expansion, with remainders stable under t,s derivatives of total order up to 2, is

    A/(Phi(t)Phi(s))=u/(2E)
       *[1+(7/2+1/u)/E+O(E^-2)].

The justification is that of §4.2: prior differentiation on the fixed integration domain, Taylor for v<=sqrt(E) and exponential control of the tail. The factors B_t B_s contribute only O((1+v)^m/E²), apart from the exponential theta corrections. Consequently,

    A(t,s)=[Phi(t)Phi(s)/(2pi)]G0(t,s)[1+O(exp(-2L))],
    H(t,s)=H0(t,s)+O(exp(-2L)),

uniformly for x,y in that compact. The first equality includes a positive diagonal congruence. The entry estimates, although differentiated, do NOT allow transferring the indefiniteness of G0/H0 to the real kernel: the block size and the negative vector of the model are not controlled uniformly in L.

**Consequence for the method.** Using G0 or H0 as the PSD reference of a perturbative all-orders proof is not appropriate. Nor can a symmetric sandwich (1-epsilon)H0 <= H <= (1+epsilon)H0 in the order of forms hold, with epsilon>0: adding the two PSD differences would give 2epsilon H0 PSD, which is false; identical argument for the direct model after congruence. A one-sided bound with respect to an indefinite model does not close the sign without paying for its negative directions. Other positive references and an exact signed compensation are not excluded. Real positivity and the logarithmic criterion remain OPEN; no new W/T sign.

## 5. Infinitesimal necessary condition and failure for the real Phi

Set V=-log phi and f=V'. Choose positive nodes, so that tau>0. At v=0,

    S_0(t,s)=phi(t)phi(s),
    B_v(t,s)=S_v(t,s)/[phi(t)phi(s)],
    B_0(t,s)=1,
    partial_v B_v(t,s)|_(v=0)
           =-[f(t)+f(s)]/(t+s)=-K_f(t,s).             (JET)

For t=s the formula is K_f(t,t)=f(t)/t. Nodes with t+s=0 are not needed. For each finite set of nodes, smoothness gives a first-order expansion with remainder o(v).

If all layers were PSD, for every vector c with sum_i c_i=0 one would have

    0<=c^T B_v c=-v c^T K_f c+o(v),

and, dividing by v>0 and passing to the limit,

    c^T K_f c<=0.                                    (CND)

This is only a necessary condition. Next, an exact violation of it is constructed under a specific growth hypothesis.

Fix two numbers 0<alpha<beta and add a third node R>beta. Write k_ij=K_f(t_i,t_j), t=(alpha,beta,R), and define

    Q_ab=k11+k22-2k12,
    Q_bR=k22+k33-2k23,
    B=k13-k12-k23+k22.

For c=(1,-1-epsilon,epsilon), whose sum is 0,

    c^T K_f c=Q_ab+2epsilon B+epsilon^2 Q_bR.          (TRIPLE)

Now assume f(R)/R^3->+infinito. The constants involving only alpha,beta are fixed. From the formulas of the entries one obtains

    B/[f(R)/R^2]->beta-alpha,
    Q_bR/[f(R)/R]->-1.                               (ASYM)

For example, the dominant part of B is

    f(R)[1/(R+alpha)-1/(R+beta)]
      =(beta-alpha)f(R)/[(R+alpha)(R+beta)],

and that of Q_bR is f(R)[1/R-2/(R+beta)]. The other terms are constants or O(1/R), negligible at those scales. Thus, for R sufficiently large but FINITE, Q_bR<0 and B>0. Choose exactly

    epsilon=-B/Q_bR>0.

Then TRIPLE equals Q_ab+B^2/(-Q_bR), and

    [B^2/(-Q_bR)]/[f(R)/R^3]->(beta-alpha)^2>0.

The value is positive for some finite R. This contradicts CND.

To translate the contradiction into a concrete layer, fix those nodes and that vector c. If Q=c^T K_f c>0, JET implies c^T B_v c=-vQ+o(v)<0 for all v>0 sufficiently small. With d_i=c_i/phi(t_i) one has d^T S_v d=c^T B_v c<0. Therefore there exists a FINITE layer, at three positive real nodes, which is not PSD. Neither R nor v has been computed, nor is it required.

The REAL Phi satisfies the hypothesis: the audited tail of POWER_MIXED_VOLTERRA_OBSTRUCTION_105, section 4, gives

    f(R)=V'(R)=2pi exp(2R)+O(1), R->infinito.

In particular f(R)/R^3->+infinito. The obstruction applies to the real datum, using its specific growth, without invoking any generic class discarded in 074/101/111.

## 6. Exact scope

Proved: the identity LT, the uniform sufficiency of PSD layers, the quartic model and the impossibility that ALL layers of the real Phi be PSD. The negative inequality found belongs to a layer S_v; it is NOT a negative inequality for its integral A, nor for a block of the kernel of M, nor for W.

A sum or integral of indefinite kernels may be PSD. The present obstruction does not exclude cancellation between layers, a signed rearrangement, another Gram nor a specific joint inequality of the real layers. Nor does it enlarge a finite dimension or a temporal window of the known sign.

Finally, the diagonal of the full kernel is

    A(t,t)=integral_t^infinito 2u phi(u)^2du,

not J(t)=integral_t^infinito u phi(u)du of the CORE. The opposite entry is

    A(t,-t)=integral_0^infinito 2r phi(r+t)phi(r-t)dr.

The sign of its minor is not inferred from the failure of a layer. This note contains no falsifier of PSD of the full integral kernel.


## 7. Generic hypotheses and positive operations

**PROVED, analytic consequences without new computations.** 074 has V(t)=g(t²) with g a convex polynomial, nonnegative coefficients and all its derivatives nonnegative; it satisfies V'''(t)>0 for t>0 but its transformed kernel 3 is indefinite. By LT its A is not PSD either. It is a corollary of the existing falsifier, not a real theta falsifier.

Positive mixtures do not preserve A PSD. For two distinct centred normalized Gaussians, Z(u)=C1 exp(v1 u²/2)+C2 exp(v2 u²/2), C_i,v_i>0. N=M/u is the tilted average of v_i and N'=u Var_u(v)>0. Hence uM'>M, contrary to the criterion 001§3. The minor at nodes u,u+h has h² coefficient equal to [M²-u²M'²]/(4u⁴)<0. By LT, A is not PSD for that mixture, although each Gaussian belongs to the positive model of §4.

Convolution does preserve the transformed kernel: Z=Z1Z2 implies M=M1+M2, a sum of PSD kernels. But a convolution with a nonzero factor exp(-at⁴-bt²) and another positive factor with mass on a compact has lower bound c exp(-C(1+|t|⁴)). So does a nonzero positive mixture of such factors: restrict the parameter measure to a bounded box of positive finite mass. This excludes those exact representations of the real Phi, by its supertail. It does not exclude other factors nor signed mixtures.

The integration-by-parts identity with B(t,s)=(t+s)/(f(t)+f(s)), f=V', keeps a correction: A=B Phi(t)Phi(s)+integral_0^infinito (partial_t+partial_s)B(t+r,s+r)Phi(t+r)Phi(s+r)dr, wherever defined and the boundaries vanish. It cannot be certified by making both terms PSD: on the positive diagonal, (partial_t+partial_s)B=(f-tf')/f²<0, a consequence of 073. It is an obstruction to that discard, not to the joint balance.

Nor does a positive operator representing tPhi suffice. The same Gaussian mixture has Fourier transform H=Σ A_i exp(-omega²/(4a_i))>0. The multiplier b0=-H'/(omega H), removable at 0, is an average of 1/(2a_i), and defines a bounded self-adjoint positive operator satisfying Bop(-Phi')=tPhi. For h smooth compact and F(r)=integral h(t)Phi(t+r)dt, Fubini gives Q_A(h)=-2 Re integral_0^infinito Bop F'(r) conjugado(F(r))dr. Positivity of the operator does not control this form on the half-line, and A is already indefinite in this example. It is not required to apply the derivative to the function cut by the half-line.

The targeted search for hazard, quotients and Lyapunov in indices/corpus found 103_42/43 and 073, about curvature/pair objects, with no literal duplicate of this integration by parts. The diagonal failure is an immediate consequence of 073 and is not presented as a new tool. PSD of the REAL A remains OPEN.


### 7.1. Gaussian convolution: converse via a node tending to infinity

**PROVED as a sign equivalence, review against cases and targeted cross-check.** Preservation under convolution in §7 was already known. A converse is added under a decay condition on the kernel that the real Phi does satisfy. It is not the flow multiplying the density by exp(lambda t²), nor the Gaussian representation of the gamma tests.

**Rank-one lemma.** Let K be a real symmetric kernel on (0,infinito) such that, for each fixed u,

    K(u,R)->0,   K(R,R)->0   cuando R->infinito.

For any b>=0, K+b is PSD on all finite blocks if and only if K is. Sufficiency is immediate. For necessity, if a block U=(u_i) and a vector c give q=sum c_i c_j K(u_i,u_j)<0, add a node R larger than all u_i and the coefficient d=-sum c_i. The constant contribution b cancels exactly, and the new form equals

    q+2d sum_i c_i K(u_i,R)+d²K(R,R) -> q<0.

For R sufficiently large it contradicts PSD of K+b. The proof uses all sizes and arbitrarily large nodes; it does not establish an equivalence at fixed size or on a bounded range of nodes.

**Condition verified for Phi.** Let F(u)=log(Z(u)/Z(0)), with u>=0. Positivity and parity of Phi give F>=0 and M=F'>=0; F is convex. For all N>0, Phi(t)<=C_N exp(-Nt²), whence F(u)<=u²/(4N)+D_N. By convexity,

    0<=M(u)/u <=[F(2u)-F(u)]/u² <=1/N+D_N/u².

Since N is arbitrary, M(u)/u->0. Thus K(u,v)=(M(u)+M(v))/(u+v) satisfies both conditions of the lemma.

**Application.** Let G_sigma be the centred normalized Gaussian of variance sigma², sigma>0. Its temporal convolution with Phi has

    Z_sigma(u)=exp(sigma²u²/2)Z(u),
    M_sigma(u)=M(u)+sigma²u,
    K_sigma(u,v)=K(u,v)+sigma².

Therefore K_sigma is PSD in all orders for ONE fixed variance sigma² if and only if K is. Multiplying G_sigma*Phi by exp(-sigma²/8) moreover preserves the moment Z(1/2)=1/4; that constant does not modify M_sigma nor K_sigma. Parity and pointwise positivity are preserved.

**Remaining obligation.** An independent proof of the sign of a single smoothed density would close the sign of the original kernel. No such proof is obtained here. Nor can one assume that smoothing turns a globally indefinite kernel into a PSD one: the lemma forbids it in this class. This does not rule out using the equivalence to find a more tractable representation, nor exclude other convolutions. There is no new positivity of W, T window or modification of papers.

## 8. No individual theta mode provides a local Gram of all orders

**PROVED, independent mathematical review against cases; targeted cross-check.** The modal antecedent 103_47/48 already contains the following translation; it is not presented as new. The difference from the mere crossing identity is a falsifier of the positivity of each modal kernel, followed by its LOCAL scope via §2.2. No numerical computations and no bibliographic priority claimed.

Write

    h(x)=pi exp(5x/2)[2pi exp(2x)-3]exp(-pi exp(2x)),
    Phi_n(t)=n^(-1/2)h(t+log n),
    A_n(t,s)=integral_0^infinito
                (t+s+2r)Phi_n(t+r)Phi_n(s+r)dr.

The even cancellation of §2 is not applied to Phi_n: each individual mode is NOT even. One has exactly

    A_n(t,t)=(2/n)integral_(t+log n)^infinito
                         (x-log n)h(x)^2 dx.

The mass H=integral_R h(x)^2 dx and its first absolute moment are finite. We will show that m=H^(-1)integral xh(x)^2 dx<0. Thus

    lim_(t→-infinito) A_n(t,t)=(2H/n)(m-log n)<0

for ALL integers n>=1, including the first mode.

Elementary proof of the moment. Set z=2pi exp(2x), alpha=5/2. Up to a positive constant, h(x)^2dx=z^(alpha-1)(z-3)^2exp(-z)dz. Define

    I_alpha=integral_0^infinito z^(alpha-1)exp(-z)dz,
    J_alpha=integral_0^infinito log(z)z^(alpha-1)exp(-z)dz.

Integrating by parts gives I_(alpha+1)=alpha I_alpha and J_(alpha+1)=alpha J_alpha+I_alpha. At alpha=5/2,

    I_(alpha+2)-6I_(alpha+1)+9I_alpha=(11/4)I_alpha,
    J_(alpha+2)-6J_(alpha+1)+9J_alpha=(11/4)J_alpha.

In the second equality the additional term is (2alpha+1-6)I_alpha=0. Since x=(log z-log(2pi))/2,

    m=(1/2)[J_alpha/I_alpha-log(2pi)].

Strict Jensen for log under the probability z^(alpha-1)exp(-z)dz/I_alpha gives J_alpha/I_alpha<log(alpha), since its mean is alpha. Therefore m<(1/2)log(5/(4pi))<0. This verifies the sign without estimating a series or truncating the arithmetic.

Each A_n is jointly holomorphic on the product of strips |Im t|,|Im s|<pi/4: for r→infinito the same domain of exponential convergence of §2.2 applies; neither parity nor positivity of h is required. The analytic propagation principle, which only uses that holomorphy, shows that A_n CANNOT be PSD of all sizes on any open real interval. Otherwise it would be globally PSD, contradicting the negative diagonal just proved. In particular, this holds on positive intervals where Phi_n is positive and A_n has positive diagonal. No explicit size of the local negative minor is obtained, nor is a campaign launched to find it.

Scope: certifying the full kernel via separate Grams of each theta mode is ruled out, even starting on a temporal tail. A of the real Phi is not refuted: A includes all pairs of modes n,m, not only sum_n A_n, and its global symmetry allows cancellations absent in each mode. Nor is a joint estimate or a different regrouping with controlled crossings ruled out.


### 8.1. The full theta prefix also fails: all its crossings are kept

**PROVED for every sufficiently large prefix, independent review against cases and targeted cross-check.** Change with respect to §8: Phi_M=sum_(n=1)^M Phi_n is introduced IN FULL into the definition of A; all pairs n,m<=M are included. The antecedents of correlated tails 103_47/48 and Euler truncation are not this statement about the square of a theta prefix. No threshold M is computed nor is a campaign started.

Define f_M(x)=M^(-1/2)Phi_M(x-log M). With a_x=pi exp(2x),

    f_M(x)=pi exp(5x/2)(1/M)sum_(n=1)^M
       (n/M)^2[2a_x(n/M)^2-3]exp[-a_x(n/M)^2].

For fixed x it is a Riemann sum. Since the derivative of z³exp(-a_x z²) is z²[3-2a_x z²]exp(-a_x z²),

    f_M(x)→F(x)=-pi exp(5x/2)exp[-pi exp(2x)].

It is necessary to control the mass that moves with M, not just this pointwise limit. For x<=0, a_x<=pi and the preceding sum gives |f_M(x)|<=C exp(5x/2), uniformly in M. For x>=0 set lambda=a_x/M². Then

    |f_M(x)|<=3pi exp(5x/2)M^(-3)
                 sum_(n>=1)n²(1+lambda n²)exp(-lambda n²).

On v∈[n-1/2,n], n²<=4v², 1+lambda n²<=4(1+lambda v²) and exp(-lambda n²)<=exp(-lambda v²). Integrating over these disjoint intervals of length 1/2,

    sum_(n>=1)n²(1+lambda n²)exp(-lambda n²)
      <=32 integral_0^infinito v²(1+lambda v²)exp(-lambda v²)dv
      =C0 lambda^(-3/2).

Thus |f_M(x)|<=C1 exp(-x/2) for x>=0. Both majorants are square integrable with weight 1+|x|. Dominated convergence proves f_M→F in L²((1+|x|)dx), whence

    H_M=integral f_M²→H=integral F²>0,
    J_M=integral x f_M²→J=integral x F².

The change-of-variable identity is exact:

    integral_R t Phi_M(t)^2dt=M[J_M-log(M)H_M],
    [integral t Phi_M²]/[M log M]→-H<0.

Therefore that moment is negative for ALL M sufficiently large. For each such M,

    lim_(t→-infinito) A_[Phi_M](t,t)
          =2 integral_R x Phi_M(x)^2dx<0.

Finiteness of the absolute moment also follows directly from the tails of the finite sum. A_[Phi_M] is holomorphic on the same strips as each mode; §2.2 implies that it is NOT PSD of all sizes on any open real interval. The lack of parity of the prefix prevents using the cancellation of §2, but does not affect the analytic principle.

The failure does not disappear by including the crossings inside the prefix. The quadratic mass of the prefix is M H_M~M H and shifts towards t=-log M; that is why convergence of the theta series on compacts is not convergence of these prefixes in the global norm weighted by 1+|t|. The infinite Phi is even and its first quadratic moment equals 0, without contradiction. This result rules out a proof via eventually PSD theta prefixes; it does not rule out a joint estimate with the omitted tail, a different reorganization nor the sign of the full real kernel. It proves no positive bound and does not enlarge T.


**Strengthening: the discard holds for ALL M>=1.** Independent review against cases, with targeted cross-check of antecedents. The preceding asymptotic describes the mass defect, but it is not needed to exclude small prefixes. Substituting z=pi exp(2t) in the transform of h gives, for u>-5/2,

    Z_h(u)=C(u)(u-1/2),
    C(u)=(1/2)pi^(-u/2-1/4)Gamma(u/2+5/4)>0.

By the translation of each mode,

    Z_[Phi_M](u)=(u-1/2)H_M(u),
    H_M(u)=C(u)sum_(n=1)^M n^(-u-1/2)>0.

H_M is C¹ near 1/2. Therefore, for u<1/2 sufficiently close and still positive, Z_[Phi_M](u)<0 while its derivative H_M(u)+(u-1/2)H_M'(u)>0. These are signs of an explicit formula of the approximant; no argument about zeros is used.

LT also holds here without parity. For phi=Phi_M, set B(t)=[integral_t^infinito(1+x²)phi(x)^2dx]^(1/2). The inequality (x+y)²<=(1+x²)(1+y²) and Cauchy–Schwarz give |A_phi(t,s)|<=B(t)B(s). B is bounded on the left and has a supertail on the right; thus integral exp(ut)B(t)dt is finite for each u>0. This bound and the tails of phi justify the double transform, the integration by parts in LT and the truncation of the exponential test. At the chosen u,

    integral integral exp[u(t+s)]A_[Phi_M](t,s)dt ds
                       =Z_[Phi_M](u)Z_[Phi_M]'(u)/u<0.

Hence A_[Phi_M] is not PSD for any M>=1, and analytic continuation excludes PSD on any open interval. This also extends to ALL M the discard of repairs that keep a right tail of the raw prefix intact. The scope of Q_M in §8.2 is still eventual; it is not changed by this proof.

### 8.2. Adding the continuous tail improves convergence, but does not restore PSD

**PROVED, independent review against cases and cross-check.** The approximant of §8.1 is changed: now

    Q_M(t)=Phi_M(t)+pi M³exp(5t/2)exp[-pi M²exp(2t)].

The second term is exactly integral_M^infinito Phi_n(t)dn, treating n as a real variable. The Euler–Maclaurin operation is not presented as new. The specific result is that Q_M→Phi in L²((1+|t|)dt), but its temporal kernel is still not PSD for all M sufficiently large. The crossings of the correction with the prefix and with the real Phi are kept.

Set E_M=Q_M-Phi and g_x(z)=z^(-1/2)h(x+log z). The exact identity of the tail is

    E_M(x-log M)=sqrt(M)[integral_1^infinito g_x(z)dz
                           -(1/M)sum_(n>M)g_x(n/M)].

The trapezoidal rule with step 1/M, summed over the half-line, gives

    E_M(x-log M)=h(x)/(2sqrt(M))+R_M(x),
    |R_M(x)|<=G(x)/(8M^(3/2)),
    G(x)=integral_1^infinito |g_x''(z)|dz.              (TRAP)

The elementary bound is obtained by integrating the remainder against the quadratic kernel of each cell, whose height is at most 1/(8M²). The boundaries at infinity vanish.

To verify that the bound works globally, write H(v)=v²(2pi v²-3)exp(-pi v²). Then g_x(z)=pi exp(x/2)H(exp(x)z), and

    G(x)=pi exp(3x/2)integral_(exp x)^infinito |H''(v)|dv.

Thus G(x)<=C exp(3x/2) on the left and has a doubly exponential tail on the right. In particular h and G belong to L²((1+|x|)dx). TRAP and the change t=x-log M give the announced weighted convergence and

    integral t E_M(t)^2dt
      =-[||h||²/(4M)]log M+O(1/M+log M/M²).           (ERR-MOM)

The crossings still need to be paid; they are not eliminated by declaring E_M small. For any alpha>0 there exists C_alpha with |h(x)|<=C_alpha exp(-alpha x) for all x: its right tail is doubly exponential and its left tail decays. The supertails of Phi therefore imply

    integral |t|Phi(t)|h(t+log M)|dt=O_alpha(M^(-alpha)).

The cross contribution of the leading boundary term of TRAP is then O(M^(-3/2)), taking alpha=1. By weighted Cauchy–Schwarz, that of the remainder is O(M^(-3/2)sqrt(1+log M)); the weaker bound O(M^(-3/2)log M) may be used for M>=2. Since Phi is even, integral tPhi(t)^2dt=0. One obtains

    integral t Q_M(t)^2dt
      =-[||h||²/(4M)]log M
           +O(1/M+log M/M^(3/2))<0                  (Q-MOM)

for M sufficiently large. No threshold needs to be computed.

Each Q_M is holomorphic in the strip and has finite absolute square moments. The diagonal limit of its A is twice Q-MOM; §2.2 again excludes PSD on any open temporal interval. Unlike the raw prefix, here the negative defect tends to 0 and there is global convergence of densities: that does not prove that the approximation preserves the sign, nor does it decide that of the limit. Exactly this first continuous correction is discarded as a source of eventually PSD approximants, not other corrections nor a different joint control. No new data nor modifications of papers.


### 8.3. Symmetrizing the corrected prefix does not restore PSD either

**PROVED for ALL M>=1, independent review against cases and targeted cross-check.** Another hypothesis changes: S_M(t)=[Q_M(t)+Q_M(-t)]/2 is even, so that the odd moment used in §8.2 now vanishes exactly. The following proof uses the full transformed quadratic form; it does not reapply that falsifier. No argument about zeros is necessary.

Let C=pi^(-1/4)Gamma(5/4)/4>0. The substitution z=pi exp(2t) and integration by parts give integral h=-C, and the integral of the continuous correction of Q_M is 2C sqrt(M). Thus

    integral S_M=integral Q_M
       =C[2sqrt(M)-sum_(n=1)^M n^(-1/2)]>=C>0,

since sum n^(-1/2)<=1+integral_1^M x^(-1/2)dx=2sqrt(M)-1. On the other hand, expanding the exponents in the left tail gives

    Q_M(t)=-[pi M(3M+1)/2]exp(5t/2)+O_M(exp(9t/2)).

Exactly sum_(n=1)^M n²=M(M+1)(2M+1)/6 was used. The right tail of Q_M is doubly exponential. Therefore

    S_M(t)=-D_M exp(-5|t|/2)+O_M(exp(-9|t|/2)),
    D_M=pi M(3M+1)/4>0.

Its transform Z_M(u)=integral exp(ut)S_M(t)dt exists for |Re u|<5/2, satisfies Z_M(0)>0 and

    Z_M(u)=-D_M/(5/2-u)+O_M(1)→-infinito,
                   u→(5/2) desde abajo.

Choose the first positive point where Z_M reaches the level Z_M(0)/2. On the preceding interval Z_M is positive; the mean value theorem gives a point u>0 with Z_M(u)>0 and Z_M'(u)<0. This only uses a strictly positive level, not information about zeros.

LT must be justified for these tails, which are not Gaussian. For any even S with |S(t)|<=C0 exp(-beta|t|), the even cancellation in the integral of A remains valid even though S has variable sign. With tau=(t+s)/2 and d=(t-s)/2,

    |A_S(t,s)|<=C0² integral_|tau|^infinito
                       2sigma exp[-2beta max(sigma,|d|)]dsigma
       <=C_beta(1+t²+s²)exp[-beta(|t|+|s|)].

This proves absolute convergence and integration by parts in LT for |Re u|,|Re v|<beta. Applying beta=5/2 to the preceding point yields

    integral_R² exp[u(t+s)]A_[S_M](t,s)dt ds
                       =Z_M(u)Z_M'(u)/u<0.

Truncating the exponentials preserves the negative value for a sufficiently large cutoff by dominated convergence. Approximating the compact integral by sums gives a finite negative matrix: A_[S_M] is not PSD. Its integral is jointly holomorphic on the same strips (the tail in r is now exponential, uniform on compacts), so §2.2 excludes PSD on any open temporal interval.

The symmetrization keeps the weighted convergence to Phi of §8.2 and eliminates its odd moment, but introduces negative tails at both ends; it does not provide positive approximants, for any M>=1. It does not refute A_[Phi], whose tails are positive and doubly exponential. Nor does it exclude other corrections simultaneously preserving parity and tail structure. There is no new positivity nor T window.


**Common scope of §§8–8.3: repairing only the left does not change the negative test.** Review against cases. If a density psi coincides with f on [R,infinito), then A_psi(t,s)=A_f(t,s) for t,s>=R, directly because r>=0 in the integral. The negative minor of A_f in (R,R+1) is preserved exactly. Analyticity of psi is not required, only that its integral exist at those nodes. Therefore reflecting or smoothing near the origin, keeping a right tail of the excluded approximants intact, does not repair them: all modes, all S_M and all Phi_M are covered (M>=1 in the last two cases); for Q_M the result holds for M sufficiently large. Corrections that alter the right tail, even small ones, are not excluded; nor is a universal fixed size of the negative minor known. It is a consequence of the preceding results, not a new mechanism nor an obstruction for the full Phi.


**Extension of the modal discard to smooth cutoffs of infinite support.** Review against cases and cross-check, no literal antecedent found. Let w_n>=0, not all zero, with sum_n w_n n²<infinito, and phi_w(t)=sum_n w_n Phi_n(t). This condition includes w_n=exp(-epsilon n²), epsilon>0, and the finite cutoffs, but NOT the full real weights w_n=1. The change with respect to the prefix is to allow a smoothed infinite sum keeping all its crossings; it is not heat in the temporal variable nor truncation of an Euler product.

The global bound |h(x)|<=C exp(5x/2) controls the left tail of phi_w by C exp(5t/2)sum w_n n². On the right the polynomial factor is absorbed in exp(-pi n² exp(2t)), obtaining C exp(5t/2)exp[-(pi/2)exp(2t)]sum w_n n². On compact substrips of the strip |Im t|<pi/4 the same bounds are obtained with modified positive constants; the additional factors from derivatives are absorbed in the exponential. There is normal convergence and the associated A is jointly holomorphic.

For u>0, absolute Fubini gives

    Z_[phi_w](u)=(u-1/2)H_w(u),
    H_w(u)=C(u)sum_n w_n n^(-u-1/2)>0,

with C(u) as in the strengthening of §8.1. H_w is C¹ near 1/2: the factor log n of the derivative is dominated by the hypothesis sum w_n n²<infinito. Thus Z<0 and Z'>0 immediately to the left of 1/2. The bound B of §8.1 legitimizes LT and the truncation of the test, giving a negative quadratic value ZZ'/u. By §2.2, A_[phi_w] is not PSD on any open interval.

These smooth cutoffs are excluded as positive approximants, even when, on removing the regularization, they converge on compacts to Phi. The factorization/exchange is not extended to the weight w_n=1 under these hypotheses; nor are different regularizations that keep the full compensation discarded. There is no negative result on A_[Phi] nor a new T window.

### 8.4. A cancelled exponential moment excludes PSD; cutoffs of the Jacobi product

**PROVED, explicit class and moment.** Independent mathematical review against cases; targeted cross-check of antecedents. The preceding subsections use signs of concrete weights or coefficients. Here a signed density is allowed and the common reason is isolated: a vanishing exponential moment. The application to polynomials in exp(-pi exp(2t)) includes signed coefficients and the cutoffs of the Jacobi product, not only prefixes of square modes. No worldwide priority is claimed nor is external information about the target sign used.

**Lemma.** Let phi be real, continuous and not identically zero. Suppose, for some eta>0, decay O(exp(eta t)) on the left and decay faster than any exponential on the right. Let c>0 be such that

    Z(c)=integral_R exp(ct)phi(t)dt=0.                 (CANCEL)

Then A_phi(t,s)=integral_0^infinito(t+s+2r)phi(t+r)phi(s+r)dr is not PSD on the whole line. If moreover A_phi is jointly holomorphic on a product of strips of positive width, it is not PSD on any nonempty open real interval.

**Proof.** For u,v>0, setting x=t+r,y=s+r inside the triple integral gives, with absolute convergence,

    integral_R² exp(ut+vs)A_phi(t,s)dt ds
       =[Z'(u)Z(v)+Z(u)Z'(v)]/(u+v).                 (LT-CANCEL)

Indeed, the absolute value before integrating in r is bounded by exp(-(u+v)r) times

    (integral |x|exp(ux)|phi(x)|dx)(integral exp(vy)|phi(y)|dy)
      +(integral exp(ux)|phi(x)|dx)(integral |y|exp(vy)|phi(y)|dy),

which is finite by the assumed tails. Neither parity nor pointwise sign of phi is needed. If A_phi were PSD, approximating the compact integrals by finite sums and removing the cutoff via this bound would give Z(u)Z'(u)/u>=0 for all u>0. Thus (Z(u)²)' >=0. Since Z(c)²=0, necessarily Z(u)=0 for all 0<u<c.

This forces phi=0: Z is holomorphic in Re u>-eta by the same bounds; the identity on an interval implies identity on that half-plane, and on an interior vertical line it is the Fourier transform of an integrable density exp(u0 t)phi(t). Its uniqueness gives the contradiction. Equivalently, some u0 in (0,c) satisfies Z(u0)²>0, and the mean value applied between u0 and c produces a u with Z(u)Z'(u)<0. LT-CANCEL and truncation give a negative quadratic test; Riemann sums give a finite negative block. The last statement of the lemma follows from the analytic PSD continuation of §2.2.

**Polynomial application.** Let P be a nonconstant real polynomial, q(t)=exp(-pi exp(2t)), and define

    F_P(t)=exp(t/2)P(q(t)),
    phi_P(t)=(D²-1/4)F_P(t)/4.

If P(q)=p0+sum_(k>=1)p_k q^k, an exact differentiation gives

    phi_P=(1/2)sum_(k>=1)p_k Phi_[sqrt(k)],
    Phi_[b](t)=pi b² exp(5t/2)(2pi b²exp(2t)-3)
                  exp(-pi b²exp(2t)).

The term p0 disappears; the smallest scale with nonzero coefficient dominates the right tail, so phi_P is not identically zero. The left tail is O(exp(5t/2)), the right one is superexponential and A_phiP is holomorphic in |Im t|,|Im s|<pi/4. The required moment is obtained keeping the boundaries:

    integral_R exp(t/2)phi_P(t)dt
      =(1/4)[exp(t/2)(F_P'(t)-F_P(t)/2)]_-infinito^infinito=0.

At both ends the boundary is -2pi exp(3t)q(t)P'(q(t)) and tends to 0. Integrability of F_P, which may grow on the right, is not presupposed. The lemma with c=1/2 proves that A_phiP fails PSD on any open real interval.

**Jacobi product.** The classical identity theta_3(0,q)=prod_(n>=1)(1-q^(2n))(1+q^(2n-1))² is in [DLMF20.5.3](https://dlmf.nist.gov/20.5.E3). For each J>=1, its cutoff

    P_J(q)=prod_(n=1)^J(1-q^(2n))(1+q^(2n-1))²

is a nonconstant real polynomial, so the preceding result applies. It includes ALL crossings of its signed coefficients, although each factor of the product is positive for 0<q<1. J=0 produces the zero density and is outside the statement.

**Scope.** CANCEL cannot be passed to the infinite product via convergence on compacts: for the full, positive Phi, integral exp(t/2)Phi(t)dt is strictly positive. The discard is not a refutation of its kernel nor of a reorganization keeping the full moment. It does prevent using these polynomial cutoffs as PSD approximants. No inequality for the full product, new T window or global proof has been obtained; papers untouched.

### 8.5. Symmetrizing the Jacobi cutoffs: corollary of the pair criterion

**PROVED for all J>=1, review against cases and cross-check.** The pair criterion comes from CONE001§3; it is not presented as a new principle. The following application did not appear in the cross-checked sources. Unlike §8.4 parity is restored; unlike §8.3 the resulting tail is POSITIVE and the negative test requires two nodes, not a negative diagonal.

With P_J and phi_PJ from §8.4, let S_J(t)=[phi_PJ(t)+phi_PJ(-t)]/2. As q tends to 1 from below,

    P_J(q)=8^J J!(1-q)^J[1+O(1-q)].

Thus, for beta=2J+1/2 and A_J=8^J J!pi^J, the left tail of F_PJ is A_J exp(beta t)[1+O(exp(2t))]. Differentiating this convergent expansion and using the right supertail gives

    S_J(t)=D_J exp(-beta|t|)+O(exp(-(beta+2)|t|)),
    D_J=A_J(beta²-1/4)/8>0.                          (SJ-TAIL)

In particular, for u<beta close to beta, the transform Z of S_J satisfies

    Z(u)=D_J/(beta-u)+O(1),
    Z'(u)=D_J/(beta-u)²+O(1),
    M(u)=Z'(u)/Z(u)=1/(beta-u)+O(1).

The remainders and their derivatives come from integrals convergent in a neighbourhood of beta after separating the leading tail. Z(u)>0 on that stretch. For u1=beta-epsilon and u2=beta-2epsilon, both positive if epsilon is sufficiently small, the kernel K(u,v)=(M(u)+M(v))/(u+v) satisfies

    epsilon [K(ui,uj)] -> (1/(2beta)) [[2,3/2],[3/2,1]],
    epsilon² det[K(ui,uj)] -> -1/(16beta²)<0.

This computation makes explicit the failure of the two-point criterion of 001. LT-CANCEL is justified here by the finite absolute moments for 0<u,v<beta; the same substitution and triple bound of §8.4 are valid on that interval. Multiplying the matrix K by the positive factors Z(ui)Z(uj) preserves the negative sign of the determinant. Truncating the exponential tests and approximating by finite sums produces a negative block of A_[S_J].

S_J is holomorphic in |Im t|<pi/4. The tail in the integral of A_[S_J] decays exponentially in r, uniformly on compacts of the product of strips, by (SJ-TAIL) and the finite expressions of §8.4. By §2.2, A_[S_J] is not PSD on any nonempty open real interval.

The conclusion excludes this symmetrization for all J>=1. Global pointwise positivity of S_J is not claimed; only its positive tail, sufficient for the argument. It does not affect the full Phi, with supertail, nor repairs that change these tails. No new computations, T enlargement or changes to papers.

### 8.6. Weights n^(-delta): even an arbitrarily weak damping fails

**PROVED for all real delta different from 0, review against cases and targeted deduplication.** The full infinite sum and all its crossings are kept:

    phi_delta(t)=sum_(n>=1)n^(-delta)Phi_n(t).

The preceding addendum on smooth cutoffs only covered this family for delta>3 via sum w_n n²<infinito. Here that restriction is removed, including arbitrarily small positive delta and negative delta. Neither parity of phi_delta nor a Gaussian bound on the left is assumed; those hypotheses are not available in this deformation.

**Transform on its absolute domain.** With h of §8 and Phi_n(t)=n^(-1/2)h(t+log n), substitution and absolute Fubini give

    Z_delta(u)=C(u)(u-1/2)sum_(n>=1)n^(-u-1/2-delta),
    C(u)=(1/2)pi^(-u/2-1/4)Gamma(u/2+5/4),
    u>max(-5/2,1/2-delta).                            (DELTA-LT)

The absolute integral of the atom h converges for u>-5/2; after scaling, the absolute series has exactly the weight n^(-u-1/2-delta). For the first absolute moment at most a factor 1+log n is added, which also sums strictly inside the domain. C(u)>0 for u>0. Therefore the identity LT-CANCEL of §8.4, proved by Fubini in the triple integral, is valid here for

    u,v>max(0,1/2-delta).

The lemma of §8.4 is not applied outside its tail hypotheses: its integral identity is used directly, with the absolute moments just justified.

**Case delta>0.** Near u=1/2, H_delta(u)=C(u)sum n^(-u-1/2-delta) is positive and C¹. Since Z_delta=(u-1/2)H_delta, there are points u<1/2 inside the domain where Z_delta<0 and Z_delta'>0. Thus Z_delta Z_delta'/u<0.

**Case delta<0.** Set c=1/2-delta>1/2. For p>1 close to 1,

    sum_(n>=1)n^(-p)=1/(p-1)+R(p),

with R and R' bounded near 1. This is proved without additional information about the series: subtract sum_n integral_n^(n+1)x^(-p)dx; the series of differences and its derivative converge uniformly in a neighbourhood of p=1, by bounds O((1+log n)n^(-p-1)). Inserting p=u+1/2+delta into (DELTA-LT) gives, as u decreases to c from above,

    Z_delta(u)=D/(u-c)+O(1),
    Z_delta'(u)=-D/(u-c)²+O(1),
    D=C(c)(-delta)>0.

Again Z_delta Z_delta'/u<0 for u sufficiently close to c. The differentiated remainder is bounded because C is smooth and R is C¹; the constant term resulting from expanding C(u)(u-1/2) is kept.

**From the test to the local kernel.** In both cases LT gives a negative exponential test for A_[phi_delta]. Absolute convergence allows truncating it and passing to a finite negative matrix. The modal series converges normally on compacts of |Im t|<pi/4 for any real delta; its right tail is superexponential uniformly on those compacts, since exp(-b n²exp(2r)) absorbs any fixed power of n. The integral of A is jointly holomorphic on the product of strips. By §2.2, A_[phi_delta] is not PSD on any nonempty open real interval.

**Discontinuity of the moment and scope.** For all delta>0, Z_delta(1/2)=0; for delta=0, the cancellation of the factor u-1/2 with the term 1/(u-1/2) of the series gives Z_Phi(1/2)=C(1/2)=1/4. Although phi_delta converges to Phi on compacts as delta tends to 0,

    integral_R exp(t/2)|phi_delta(t)-Phi(t)|dt>=1/4

for all delta>0. Therefore local convergence and weak damping of each mode do not preserve this moment. The case delta=0 is completely outside the discard. No negative sign of A_[Phi] or W is proved, nor are other regularizations keeping the full compensation excluded. There are no new computations, T coverage or modifications of papers.

### 8.7. Positive, even and analytic perturbations with arbitrarily small relative error

**PROVED, cases/theta_joint; targeted cross-check (2026-11-05).** For every epsilon>0 there exists a strictly positive density psi, even and holomorphic in |Im t|<pi/4, such that

    sup_(t real) |psi(t)/Phi(t)-1| < epsilon,
    psi(t)/Phi(t) -> 1 cuando |t| -> infinito,

but A_psi is NOT PSD. In fact PSD fails on every nonempty open real interval. The real supertails of Phi and any finite number of terms of its relative expansion in exp(-2|t|) are kept. The moments are not kept exactly nor is the modal arithmetic structure. This does not decide the sign of A_Phi: it shows that relative closeness of densities, even in this regular class, does not guarantee the sign of the perturbed kernel.

**Antecedent and difference.** §§8.1–8.3 already discard the prefixes Phi_M and establish tail locality, but their previous global approximants lost positivity, parity or the tails. The following construction keeps positivity and parity, obtains uniform RELATIVE error and recovers analyticity by mollifying that error, not the density. Convolution is not used here as a sign-preserving operation.

**1. Smooth positive repair.** Fix chi even C∞, 0<=chi<=1, equal to 0 on |t|<=1/2 and to 1 on |t|>=1. For t>=0, all modes Phi_n(t) are positive. With y=pi exp(2t)>=pi>3,

    Phi_n(t)/Phi_1(t)
      = n²(2n²y-3)/(2y-3) exp[-(n²-1)y]
      <=2n^4 exp[-pi(n²-1)].

Set h_M(t)=chi(t) sum_(n>M)Phi_n(|t|)/Phi(t) and psi_M=Phi(1-h_M). Near 0 h_M is identically zero, so the reflection introduces no loss of smoothness. Then h_M is even, smooth, integrable and

    0<=h_M<=epsilon_M:=2 sum_(n>M)n^4 exp[-pi(n²-1)]
       <=4(M+1)^4 exp[-pi((M+1)²-1)] ->0.

The last bound uses that the successive ratio of the summands is at most 16 exp(-3pi)<1/2. For M large, epsilon_M<1. The density psi_M is strictly positive and even; it coincides with Phi_M on t>=1. By §8.1 and tail locality, there are finite nodes t_i in (1,2) and real coefficients c_i with

    sum_ij c_i c_j A_(psi_M)(t_i,t_j)<0.

The block size may depend on M and is not estimated.

**2. Recovering analyticity without losing the negative block.** Let gamma_sigma be the normalized Gaussian of variance sigma² and g_sigma=h_M*gamma_sigma. On the line, g_sigma is even and 0<=g_sigma<=epsilon_M. Moreover it is entire, since for z=x+iy,

    |g_sigma(z)|<=epsilon_M exp[y²/(2sigma²)],

and the derivatives of the Gaussian justify uniform differentiation on compacts. Since h_M belongs to C0(R), g_sigma->h_M uniformly as sigma decreases to 0. Define

    psi_(M,sigma)=Phi(1-g_sigma).

It is positive, even and holomorphic in the strip of Phi, with relative error <=epsilon_M. Fix the negative block of step 1 BEFORE choosing sigma. If delta_sigma=||g_sigma-h_M||_infinito, for those positive nodes

    |A_(psi_(M,sigma))(t_i,t_j)-A_(psi_M)(t_i,t_j)|
      <=2 delta_sigma A_Phi(t_i,t_j) ->0.

This only uses pointwise positivity of Phi and of t_i+t_j+2r; it does NOT assume PSD of A_Phi. The negative quadratic form persists for sigma sufficiently small. Choosing first M large and then sigma small one obtains the statement.

**3. Tails and scope.** For each B>0, the modal ratio of h_M satisfies h_M(t)<=C_B exp(-B|t|). Gaussian convolution preserves that bound with another constant, by the inequality |t-r|>=|t|-|r| and integrability of exp(B|r|)gamma_sigma(r). Thus g_sigma=o(exp(-N|t|)) for each fixed N, and psi_(M,sigma)/Phi->1 with all the declared finite exponential corrections. The modal terms of doubly exponential scale are not kept. On fixed substrips g_sigma is bounded by the preceding complex bound; therefore the integral of A_(psi_(M,sigma)) is jointly holomorphic as in §2.2. That continuation principle transports its PSD failure to any open interval.

Taking M→infinito and choosing for each M a sufficiently small sigma_M as in step 2, the relative error also implies convergence in L²(w(t)dt) for each FIXED weight with integral w Phi² finite, including exponential and Gaussian weights. Uniform closeness in a complex-strip norm or in all jets is not claimed: the complex constants may grow as sigma decreases. Nor are the additional inequalities 073/077/112 or exact moments imposed. The result excludes a positivity guarantee based solely on small relative error, parity, positivity of the density and these tails. It does not exclude a signed comparison in form norm nor a use of the exact theta structure. No new numerical evaluations, W/T sign or modifications of papers.

### 8.8. Any finite family of independent moments can be preserved

**PROVED, construction and independent review against cases; targeted cross-check (2026-11-05).** §8.7 is strengthened: fix real even continuous weights w_1,...,w_d, linearly independent when restricted to (-1,1), such that integral Phi|w_i| is finite. For every epsilon>0 there exists psi with all the properties of §8.7 and A_psi not PSD, which moreover satisfies EXACTLY

    integral_R w_i(t)psi(t)dt = integral_R w_i(t)Phi(t)dt, i=1,...,d.

The weights and their number are fixed BEFORE choosing the approximant. The construction constants depend on that family. For example one can preserve normalization, a finite list of even polynomial moments and values/derivatives of the transform at a finite list of parameters, taking a basis of the corresponding analytic weights. Preservation of an infinite family is neither required nor obtained.

**1. Smooth correction without altering the tail containing the negative test.** Define L_i(f)=integral Phi(t)w_i(t)f(t)dt. It is a continuous functional for the uniform norm, with constant integral Phi|w_i|. There exist smooth even functions b_1,...,b_d, compactly supported in (-1,1), for which the matrix B_ij=L_i(b_j) is invertible. Indeed, by independence one can choose x_j in (0,1) with matrix [w_i(x_j)] invertible; otherwise, the evaluation vectors would generate a proper subspace and there would be a combination of the w_i identically zero. Even bumps around ±x_j, normalized with Phi, approximate that matrix and preserve its invertibility.

Use h_M of §8.7, d_(M,i)=L_i(h_M), a_M=B^(-1)d_M and

    p_M=-h_M+sum_j a_(M,j)b_j.

Then L_i(p_M)=0, ||p_M||_infinito<=C_w epsilon_M→0 and p_M=-h_M for |t|>=1. The density Phi(1+p_M) is positive for M large and coincides with Phi_M on t>=1. It therefore has a finite negative block of A, with nodes in (1,2). First choose M so that ||p_M||<min(epsilon/4,1/4), and fix that block. The correction is signed; it is not presupposed that the a_j have a single sign.

**2. Analyticity and exact moments simultaneously.** Mollify by the same Gaussian:

    p_(M,sigma)=p_M*gamma_sigma,
    b_(j,sigma)=b_j*gamma_sigma,
    B_(sigma,ij)=L_i(b_(j,sigma)),
    r_(sigma,i)=L_i(p_(M,sigma)).

Uniform convergence of the approximations of the identity and continuity of L_i imply B_sigma→B and r_sigma→0. For small sigma B_sigma is invertible. Set

    c_sigma=-B_sigma^(-1)r_sigma,
    q_sigma=p_(M,sigma)+sum_j c_(sigma,j)b_(j,sigma),
    psi=Phi(1+q_sigma).

One has L_i(q_sigma)=0 EXACTLY, c_sigma→0 and q_sigma→p_M uniformly. Therefore, as sigma decreases, psi remains positive and its relative error is less than epsilon. For the fixed block, if ||p_M|| and ||q_sigma|| are <=1/2, the difference of entries of A is bounded by 3||q_sigma-p_M||_infinito A_Phi(t_i,t_j); thus its negative quadratic form persists. The factor 2 of §8.7 is not reused, since now the corrections can have both signs. The convolutions are entire and even as in §8.7, even for signed p_M using its absolute norm in the bounds. They also decay faster than any fixed exponential, so that the tail quotient and the relative expansions declared there are preserved. Holomorphy of A and its failure on any interval are justified as in §8.7.

**Consequence for finite checks of the kernel.** Given distinct positive parameters u_1,...,u_m, take as weights cosh(u_i t) and t sinh(u_i t). They are linearly independent even analytic functions: a vanishing combination would be a sum of exponentials with linear prefactors; ordering the u_i and sending t to infinity successively eliminates both coefficients of the largest exponent. For even densities these moments are precisely Z(u_i) and Z'(u_i). Thus psi can have EXACTLY the same values of

    K(u_i,u_j)=[Z'(u_i)/Z(u_i)+Z'(u_j)/Z(u_j)]/(u_i+u_j)

as Phi on any previously chosen FINITE collection of blocks, and yet A_psi fail to be PSD. Under the tails of §8.7, the bridge §2.1 also implies failure of K_psi on some other block. No counterexample to K_Phi has been given. This argument alone does not guarantee preserving the infinite families of two, three or four generators. The additional control of §8.9 does preserve up to four on the admissible domain.

This goes beyond the abstract countermodel of 018 and of §8.7: here there is a positive, even and analytic density arbitrarily close to Phi with exact finite data and compatible tails. The full theta identity, the arithmetic comb and all the structural inequalities 073/077/112 are not preserved. It is not concluded that every method based on exact identities is impossible. A universal guarantee based only on those finite data, relative closeness and regularity is excluded. No new computations, W/T sign or changes to papers.

### 8.9. Stability of ALL admissible blocks of order up to four

**PROVED, construction (preserver), independent audit against cases and targeted cross-check (2026-11-05).** The certified results 084/085 are used; no new computations were run. Define

    ||h||_20=sup_(t real) exp(20|t|)|h(t)|.

There exists delta_*>0 such that every even positive density psi=Phi(1+h) with ||h||_20<delta_* has K_psi PD on ALL blocks of up to four distinct nodes u_i>1/2. Repetitions are grouped and give PSD. The threshold is existential, not a new certified value.

The difference from §8.8 is a uniform control of the jets of Z entering the scalar numerators 085, even when the nodes merge or escape. A uniform eigenvalue margin of the matrices is not assumed.

**1. Weighted error and jets.** Set delta=||h||_20<=1/2 and Delta Z=Z_psi-Z_Phi. For j<=4, use |t|^j<=C_j exp(4|t|). For u large,

    |Delta Z^(j)(u)|
      <=C_j delta integral Phi(t)exp(ut-16|t|)dt
      <=C_j delta Z_Phi(u-16).

The last inequality also holds for t<0. The lower bound M_Phi(s)>=(1/2)log s-C of 084 implies, from a fixed sufficiently large U (one may choose U>256),

    Z_Phi(u-16)/Z_Phi(u)
      =exp[-integral_(u-16)^u M_Phi(s)ds] <=C u^-8.

The arithmetic formulas 084 for M and its first three derivatives give Z_Phi^(j)/Z_Phi=O((1+log u)^j), j<=4, via the identities of exponential differentiation. Moreover 1-delta<=Z_psi/Z_Phi<=1+delta. Applying the formulas for logarithmic derivatives up to order 4 gives

    |M_psi^(k)-M_Phi^(k)|
       <=C delta u^-8(1+log u)^4, k=0,...,3.

No O-notation is differentiated: the algebraic expressions of the jets are estimated. The constants are independent of h for delta<=1/2. On each compact u∈[1/2,U], continuity of the same jets, with a bound linear in delta, follows from integrability of Phi(t)|t|^j exp(U|t|).

**2. Strict numerators.** For c=M, D=uM', E=u²M'', F=u³M''', 085 defines

    N_R=3c²+c(-6D-6E-2F)+3D²+6DE+2DF-3E²,
    N_S=3c²+c(6D+6E+2F)-9D²-6DE+2DF-3E².

They are quadratic polynomials. Step 1 and c=O(log u), D,E,F=O(1) for Phi imply

    |Delta N_R|+|Delta N_S|
        <=C delta u^-5(1+log u)^5

for u>=U. 084 proves N_R>1/4 and N_S>19/4 for Phi on u>=127.5. On [1/2,U], 085 together with 084 gives strictly positive minima. Choosing delta_* sufficiently small preserves both signs for ALL u>=1/2.

**3. Lower signs without assuming 073 for psi.** For x=u², set R=u/M_psi(u), S=uM_psi(u). By positivity and parity, M_psi(u)>0 for u>0. The identities 084 give

    T_R=2R'R'''-3(R'')²=N_R/(16M_psi^4 u^6)>0,
    T_S=2S'S'''-3(S'')²=N_S/(16u^6)>0,

with derivatives in x. The inherited asymptotics are M_psi=(1/2)log(u/(2pi))+O(1/u), uM_psi'→1/2 and u²M_psi''→-1/2. From them, R',S'>0 in the tail and R'',S''→0. T_f>0 prevents f'=0, so the positive sign of the tail is preserved on all x>=1/4. Then f'''>0; since f'' increases strictly towards 0, it is negative.

BASE073 is not invoked nor is M_psi''<0 assumed. The two-node Pfaffians 083 are positive by growth; the three-node ones are -det[1,x_i,f(x_i)]/producto_(i<j)(u_i+u_j), positive by strict concavity. For four, Rolle 084 applies with f'>0,f''<0,T_f>0. 083 and Sylvester give all blocks PD of orders <=4.

**4. Application to the negative approximants.** On the active support of the cutoff of §8.7, |t|>=1/2. For n>=2, the function exp[20t-pi(n²-1)exp(2t)] decreases from 1/2. Therefore

    ||h_M||_20
      <=2 exp(10) sum_(n>M)n^4 exp[-pi e(n²-1)] ->0.

The compact moment corrections of §8.8 have finite 20-norm and coefficients tending to 0. The mollification satisfies

    ||p*gamma_sigma||_20
      <=E exp(20|G_sigma|)||p||_20
      <=2 exp(200)||p||_20, 0<sigma<=1.

It also converges to p in this norm when exp(20|t|)p(t) belongs to C0: translations are continuous in the 20-norm, and the majorant exp(20|r|) controls the Gaussian integral. Both p_M and the bumps of §8.8 satisfy that condition. Thus the subsequent moment corrections, with coefficients tending to 0, allow q_sigma→p_M in 20-norm. Choosing first M large and then sigma small simultaneously imposes the neighbourhood delta_*, the exact moments, any desired relative precision and the persistence of the fixed negative block.

**Conclusion.** There exist positive, even and analytic densities, arbitrarily close to Phi in the weighted relative norm 20, which preserve ALL admissible blocks of up to four generators, any finite family of moments of §8.8 and the tails of §8.7, but whose A and full K are NOT PSD. By §2.1 there exists a negative block of K with u>1/2; it necessarily has more than four distinct nodes.

The arithmetic theta identity is not preserved, nor is K_Phi refuted. The argument of §8.9 alone does not guarantee preserving ALL thirteen generators of 053; that point is treated in §8.10. Preserving the inequalities 077/112 is not claimed. This conclusion clearly distinguishes the four continuous orders from the global obligation: neither those orders, nor this proximity and the exact finite data, force it by themselves in the declared class. It is not an enlargement of the real sign nor of T. Papers untouched.

### 8.10. Uniform relative control and preservation of the thirteen high poles

**PROVED, construction (preserver), independent audit against cases and targeted cross-check of antecedents (2026-11-05).** The following lemma controls the form relative to the Cauchy Gram, not only its entries. It avoids a bound that degenerates when the nodes merge or separate a lot.

**Contractive interpolation lemma.** Fix a>0 and n. Let mu be real smooth on [a,infinito), such that

    F(z)=mu(a(1+z)/(1-z))

extends to C^(n-1)[0,1]. For any set of up to n rates u_i>=a and complex coefficients c_i,

    |sum_ij c_i conjugado(c_j)[mu(u_i)+mu(u_j)]/(u_i+u_j)|
      <=2 B_n sum_ij c_i conjugado(c_j)/(u_i+u_j),
    B_n=sum_(j=0)^(n-1) (2^j/j!) ||F^(j)||_infinito.

The same bound holds for the confluent limits, interpreted as parametric derivatives of the kernel and exponentials times polynomials.

Proof. On E=span{exp(-u_i r)}, with the L²(0,infinito) norm, A=-D_r preserves E and

    2 Re<Af,f>=|f(0)|²>=0.

A+a is invertible. The identity

    ||(A+a)v||²-||(A-a)v||²=4a Re<Av,v>>=0

makes Q=(A-a)(A+a)^(-1) a contraction. Its eigenvalues z_i=(u_i-a)/(u_i+a) belong to [0,1). Interpolate F via Newton: the divided-difference coefficients of order j are bounded by ||F^(j)||/j!, and each factor Q-z_iI has norm <=2. Hence the interpolating polynomial P, of degree <=n-1, satisfies ||P(Q)||<=B_n. Moreover P(Q)exp(-u_i r)=mu(u_i)exp(-u_i r). For f=sum c_i exp(-u_i r), the form on the left is 2Re<P(Q)f,f>, while the Gram on the right is ||f||². This proves the bound without assuming that mu is holomorphic on a whole complex half-line. Repeated nodes are treated by Hermite interpolation or limits of finite differences; the constant is uniform and the rates may merge one-sidedly at a. Thus all numerators of the corresponding rational spaces are included.

**Application to mu=M_psi-M_Phi.** Write psi=Phi(1+h), even positive, and delta=||h||_100=sup exp(100|t|)|h(t)|<=1/2. For j<=13, |t|^j<=C_j exp(4|t|), so that

    |Delta Z^(j)(u)|/Z_Phi(u)
      <=C_j delta Z_Phi(u-96)/Z_Phi(u)
      <=C_j' delta u^-48

for u sufficiently large. The second bound comes from integrating the lower bound M_Phi(s)>=(1/2)log s-C of 084 over [u-96,u]. On compacts all those moments have bounds linear in delta.

To control the normalized moments of Phi without needing arithmetic formulas of order 13, set alpha=1/log u. The upper bound M_Phi(s)=O(log u) on [u-alpha,u+alpha] gives

    E_u exp(alpha|t|)
       <=[Z_Phi(u+alpha)+Z_Phi(u-alpha)]/Z_Phi(u)<=C.

Therefore E_u|t|^j<=C j!(log u)^j. The algebraic formulas of logarithmic differentiation up to order 13 and Z_psi/Z_Phi∈[1/2,3/2] imply

    |Delta M^(k)(u)|
       <=C delta u^-48(1+log u)^13, k=0,...,12.

No asymptotic remainders are differentiated. Fix a=63/2. In the derivatives up to order 12 of F(z)=Delta M(a(1+z)/(1-z)), the chain rule introduces at most factors C_a u^24. Thus all those derivatives tend to 0 on reaching z=1, extend continuously and

    ||F||_(C12[0,1])<=C delta.

The lemma with n=13 proves, for ALL rates u_i>=63/2, with multiplicities allowed,

    |Q_psi[f]-Q_Phi[f]|<=C_13 delta ||f||².

Here Q_psi is DEFINED by the kernel K_psi and its confluent limits. For Phi, CONE001§1 identifies Q_Phi exactly with the form W on those exponentials; its temporal coefficients include the corresponding congruences when starting from the rho data. An unproved arithmetic Weil identity is not being attributed to psi.

FULL_THIRTEEN053 proves W[f]>||f||²/4000 for all thirteen poles >=63/2 and numerators of degree <13. Choosing delta sufficiently small for C_13 delta<1/8000 gives

    Q_psi[f]>||f||²/8000

on ALL that family. It is an analytic consequence of the existing certificate, without new numerical verifications. No effective delta is computed.

**Compatibility with the negative approximants.** For M sufficiently large, the same monotonicity used in §8.9 gives

    ||h_M||_100
      <=2 exp(50) sum_(n>M)n^4 exp[-pi e(n²-1)] ->0.

The compact moment corrections have finite 100-norm and coefficients tending to 0. For sigma<=1, Gaussian convolution has weighted norm at most 2 exp(5000); it also approximates the identity for the functions used, since exp(100|t|)p_M(t) belongs to C0. Therefore §8.8 can be realized with arbitrarily small 100-norm, without losing exact moments or the fixed negative block. Since ||h||_20<=||h||_100, the global order-4 conclusion of §8.9 is also preserved.

Consequently, there are positive, even and analytic approximants, arbitrarily close to Phi, which simultaneously preserve ALL admissible blocks of up to four generators, ALL thirteen poles of rates >=63/2 (even confluent), the preassigned finite moments and the tails of §8.7, and yet do NOT have a globally PSD kernel. By §2.1 there is a negative block on any open interval of rates contained in (63/2,infinito); it necessarily has more than thirteen distinct nodes.

The full arithmetic theta identity is not preserved, nor is K_Phi refuted. Nor does this argument preserve a family of unbounded dimensions: B_n and the required weighted regularity depend on n. The lemma does provide a tool of uniform control at fixed dimension; not a global closure nor an enlargement of T. Papers untouched.

### 8.11. No positive Cauchy margin can be uniform in all orders

**PROVED, cases/preserver; targeted cross-check (2026-11-06).** Corollary of the continuation principle of §2.2. Let M be real analytic on (0,infinito), with M(u)=O(u) as u decreases to 0. For any c>0 and any nonempty open interval I contained in (0,infinito), the kernel

    F_c(u,v)=[M(u)+M(v)-c]/(u+v)
            =K_M(u,v)-c G(u,v), G(u,v)=1/(u+v),

is NOT PSD on all finite sets of nodes of I. It is not assumed that K_M is PSD.

**Proof.** Suppose PSD on I. On each positive compact, real analyticity of M gives a holomorphic extension to a complex neighbourhood; the denominator u+v does not vanish on sufficiently small neighbourhoods either. The argument of mixed matrices of evaluations and jets of §2.2, followed by Taylor, allows propagating PSD from I to any positive point along a compact connecting them. The radii are chosen uniform on that compact; no attempt is made to reach 0 with fixed radius. For a sufficiently small u*>0, however,

    F_c(u*,u*)=M(u*)/u*-c/(2u*)<0,

since the first term is bounded. This negative diagonal contradicts the propagated positivity.

For the real Phi, Z(u)>0 on the line and its exponential moments are finite; M=Z'/Z is real analytic and, by parity,

    M(u)=[integral t²Phi(t)dt / integral Phi(t)dt] u+O(u³).

Therefore the corollary applies to the full REAL kernel. It also applies to the even hyperbolic model. In the exponential norm of §8.10, it means that for every c>0 and every admissible I there exist a nonzero finite combination f with rates in I and a block such that Q_Phi[f]<c||f||². It is not claimed that this value is negative nor that it has an already proved lower bound. If global PSD were moreover proved, the infimum of those quotients would be exactly 0.

**Consequence for the programme.** The margin 1/4000 of 053 and the stable margin of §8.10 cannot be extended with a fixed positive constant to arbitrary dimension, even if all rates lie in a high interval. If I is inside (63/2,infinito) and c<1/4000, the test of the corollary necessarily needs more than thirteen distinct rates: the lower orders have the margin 053. This does not refute the target of nonnegativity without margin, nor the fixed-dimension theorems.

The review of the functional calculus does not allow shifting the half-plane for free either: even if the rates u_i are >=a, A-a is not accretive in general. For f(r)=exp(-ar)-exp(-br), b>a, one has f(0)=0 and Re<(A-a)f,f>=-a||f||²<0. Hence controlling a function only on Re u>=a does not authorize applying a contraction bound to the Cayley transform of A-a. A dimension-free absolute error bound, even if it existed, would not by itself supply the compensation relative to a model without uniform margin. No such compensation has been constructed; no new W/T positivity nor changes to papers.


## 9. Strict positivity of all temporal pairs by convexity in the squares

**PROVED**; independent mathematical audit arithmetic_fresh_candidate PASS. Targeted cross-check diagonal_gauge_dedup with no literal antecedent located in the consulted indices and primary sources, not exhaustive nor a claim of worldwide priority. V'''(x)>0, x>0, proved for the full theta in POWER_THETA_TWO_COPY_073 and its certificates, and SLICE of §3 are combined. No novelty is attributed to the elementary convexity principle. It is not the power-pairs theorem 073: the nodes here are arbitrary real temporal variables.

Let V=-logPhi, even and real-analytic. For x>0,

    xV''(x)-V'(x)=integral_0^x rV'''(r)dr>0.

The constant at 0 is zero by parity. For G(u)=V(sqrt(u)), u>=0,

    G''(u)=[sqrt(u)V''(sqrt(u))-V'(sqrt(u))]/(4u^(3/2))>0

when u>0. The even analyticity of V allows extending G regularly to 0. Thus G is strictly convex on [0,infinito); it is not necessary to assume V''(0)>0.

Fix real t!=s and v>0. Set m=(t+s)/2, delta=(t-s)/2 and

    a=sqrt(m²+v)+delta, b=sqrt(m²+v)-delta,
    x=t²+v, y=s²+v.

Then a²+b²=x+y, while

    |a²-b²|=4|delta|sqrt(m²+v)>4|delta*m|=|x-y|.

All these squares are nonnegative, even when a or b is negative. For a fixed sum S, the function G(S/2+r)+G(S/2-r) increases strictly with r>=0 inside its domain: its derivative is G'(S/2+r)-G'(S/2-r)>0 for r>0. Therefore

    V(a)+V(b)=G(a²)+G(b²)>G(t²+v)+G(s²+v).

Using SLICE and the diagonals S_v(t,t)=Phi(sqrt(t²+v))² one obtains

    S_v(t,s)^2<S_v(t,t)S_v(s,s), v>0,t!=s.          (PAIR-SLICE)

The diagonals are strictly positive, hence every matrix of two distinct nodes of S_v is positive definite. For v=0, S_0(t,s)=Phi(t)Phi(s), and the matrix is only positive semidefinite of rank one.

For any nonzero vector c of two coefficients, c* S_v c>0 for ALL v>0. Integrating the quadratic form using A=integral S_v dv and the integrability of entries already proved in §2 proves

    [A(t_i,t_j)]_(i,j=1,2) es definida positiva si t_1!=t_2.

In particular 0<A(t,s)<sqrt(A(t,t)A(s,s)) for every distinct real pair. This conclusion is not deduced solely from positivity of entries.

**Scope and exact pattern.** The layers in the variable v are PSD on all blocks of size one and two, but §5 already proves that a real theta layer has a non-PSD block of three positive nodes. Three is therefore the minimal possible size of a falsifier of THAT layer decomposition. The raw layers in r of §2.3 are another object and do fail at size two; there is no contradiction. The integral A has all its pairs positive, but its sign in all orders remains OPEN: integrating indefinite layers can compensate them, without a proved joint bound. There is no new W coverage nor enlargement of T; the global bridge does not allow identifying finite sizes between the two kernels. No new computations or changes to papers.


## 10. Real compensation proved on symmetric temporal triples

**PROVED**; mathematical audit arithmetic_fresh_candidate PASS; targeted cross-check diagonal_gauge_dedup with no literal antecedent located in indices and primary sources. 073 and §§4.3,5,9 are used; the principle that an integral may compensate indefinite layers is not presented as new. The difference is proving BOTH signs for the real theta at THE SAME nodes (-R,0,R). The following analytic refinement fixes R>=8 both for positivity of the integral and for the existence of initially negative layers; it does not quantify their interval v_R nor claim uniformity in R. No changes to papers.

**Positivity of the full integral.** By symmetry and joint parity, its matrix is

    [[d,c,b],[c,d0,c],[b,c,d]],
    d=A(R,R), d0=A(0,0), b=A(-R,R), c=A(R,0).

All are positive. In the antisymmetric sector, the eigenvalue is d-b>0 by §9. In the orthonormal basis of the symmetric sector, the block is [[d+b,sqrt(2)c],[sqrt(2)c,d0]]. It suffices to prove c²/d->0.

Set Y=pi exp(2R), P=Phi(R) and B=sup_(x real)Phi(x)<infinito. The full theta expansion gives p(x)=-Phi'(x)/Phi(x)>=pi exp(2x) for x sufficiently large. Thus, for R large and r>=0,

    Phi(R+r)<=P exp(-Yr).

The formula of A and the bound Phi(r)<=B imply

    0<c<=BP integral_0^infinito (R+2r)exp(-Yr)dr
         =BP(R/Y+2/Y²).

By §4.3, d/P²~R/(2Y), so that d>=RP²/(4Y) eventually. Therefore

    c²/d<=4B²(Y/R)(R/Y+2/Y²)²->0.

Since d0 is a positive constant and b>0, for R large d0(d+b)>2c² holds. Both sectors are positive definite: the whole three-node matrix is SPD. This argument only uses tail bounds and positivity of pairs; it does not need a differentiated asymptotic of the crossing c.

**Refinement of the same result: the integral is SPD for ALL R>=8.** No other route is opened nor is a sweep used. By §12, p>0 on the half-line, hence B=sup Phi=Phi(0). For f(x)=x(2x-3)exp(-x), f'(x)=(-2x²+7x-3)exp(-x)<0 if x>3. Since pi>3 and exp(3)>20 (positive rational Taylor, also used in 088),

    B=sum_(n>=1)f(pi n²)
      <18 sum_(n>=1)n^4/20^(n²)<=450/499<1.

The consecutive ratio of the majorant is <=16/20³=1/500. All modes are included.

For R>=1, 088 gives p(R+r)>2Y_r-6>=Y_r>=Y, with Y_r=Y exp(2r)>21. Thus the preceding bound c<=BP(R/Y+2/Y²) already holds on that whole region. To obtain an explicit lower bound for d, restrict its integral to 0<=r<=1/(4Y). There

    p(R+r)<2Y exp(1/(2Y))+1<3Y.

The last inequality follows from exp(x)<=1/(1-x), 0<=x<1, and Y>21. Therefore Phi(R+r)>=P exp(-3Yr), and

    d>=2R P² integral_0^(1/(4Y)) exp(-6Yr)dr
      =R P²[1-exp(-3/2)]/(3Y)>R P²/(4Y),

since exp(3/2)>4 by its positive Taylor up to degree 3.

On 0<=r<=1/16 all theta modes are positive and Phi>=Phi_1>9/256: indeed pi>3, 2pi exp(2r)-3>3, pi exp(2r)<4exp(1/8)<5 and exp(5)<256, using exp(1/8)<8/7 and e<3. Hence

    d0=integral_0^infinito 2r Phi(r)²dr>81/2^24.

If RY>=40, the bounds on c and d imply

    2c²/d<8B²(R/Y)[1+2/(RY)]²<9B²R/Y<=9R/Y.

For ALL R>=8, RY>40 holds; moreover R/Y decreases for R>=8. Using pi>3 and exp(2)>7,

    9R/Y<=72/[pi exp(16)]<24/7^8<81/2^24<d0.

The central rational comparison is equivalent to 402653184<466948881. One obtains 2c²<d0*d<d0(d+b), and d-b>0 by §9. Both sectors are therefore SPD for ALL R>=8. Arbitrary triples, intermediate R or all orders are not covered.

**Initially negative layers at those same nodes.** Normalize B_v(t,s)=S_v(t,s)/(Phi(t)Phi(s)). Here B_0 is the constant kernel 1. For p=V' odd analytic,

    partial_v B_v(t,s)|_(v=0)=-(p(t)+p(s))/(t+s).

The removable values are -p'(R) at (-R,R) and -p'(0) at (0,0). They are also justified by expanding V(R+sqrt(v))+V(R-sqrt(v)) and 2V(sqrt(v)); parity eliminates the odd powers of sqrt(v).

For eta=(1,-2,1), of zero sum, the computation at (-R,0,R) gives

    eta^T B_v eta=-v Q_R+o(v),
    Q_R=2p'(R)-6p(R)/R+4p'(0).

The full bounds of 088 give p'(R)>4Y-1 and p(R)<2Y+1 for R>=1; §12 proves p'(0)>0. Thus, for ALL R>=8,

    Q_R>(8-12/R)Y-2-6/R+4p'(0)
       >(13/2)Y-11/4>0.

For each R>=8, eta^T B_v eta<0 when v>0 is sufficiently small. The vector in the original layer is

    w_R=(1/P,-2/Phi(0),1/P),
    w_R^T S_v w_R<0 for 0<v<v_R

with some v_R>0; uniformity in R of that interval is not claimed.

**Effective compensation, limited scope.** For ALL R>=8 and that same vector w_R, positivity of the integral block proves

    integral_0^infinito w_R^T S_v w_R dv=w_R^T A w_R>0,

although the integrand is negative on (0,v_R). The entries are integrable, so the positive part outside that interval strictly exceeds its loss. It is a joint inequality proved for this concrete family, not a uniform compensation bound over all nodes, sizes or vectors. They are not power triples 080; they are temporal triples. No global positivity, W/T enlargement nor an induction on dimension is deduced. No numerical computations.


## 11. The fully paired Andréief expansion keeps negative signs

**PROVED**, positive_identity_attempt; independent audit arithmetic_fresh_candidate PASS; targeted cross-check diagonal_gauge_dedup with no literal duplicate located in indices and primary sources, with no exhaustive claim nor claim of worldwide priority. A pointwise limitation of the following expansion is proved, not the negative sign of its integral. The difference from §2.3 is grouping the eight choices of the full order-three determinant, before asking for a sign, instead of asking for PSD of each raw layer.

Fix three distinct temporal nodes t1<t2<t3, positive, and define column vectors

    f_i(r)=Phi(t_i+r), g_i(r)=(t_i+r)Phi(t_i+r),
    u_0=f, u_1=g.

Then A_ij=integral_0^infinito[g_i(r)f_j(r)+f_i(r)g_j(r)]dr. Andréief on the product space (0,infinito) times {0,1}, with Lebesgue and counting measure, gives exactly

    det[A_ij]=(1/6)integral_(0,infinito)^3 S(r1,r2,r3)dr1dr2dr3,
    S=sum_(epsilon in {0,1}^3)
       det[u_(epsilon_j)(r_j)] det[u_(1-epsilon_j)(r_j)].

All exchanges are absolutely convergent by the supertails of Phi and the linear growth added in g. The Andréief principle is classical; no novelty is attributed to this identity.

Set r1=r2=r>0, r3=r+h. The choices with epsilon1=epsilon2 vanish; the other four give

    S(r,r,r+h)=-4 det[g(r),f(r),f(r+h)]
                    times det[g(r),f(r),g(r+h)].

Let x_i=t_i+r and p=-Phi'/Phi. Since f'=-pf and g'=(1-xp)f, Taylor and the divided differences give

    det[g,f,f_h]=h C p[x1,x2,x3]+O(h²),
    det[g,f,g_h]=h C (xp)[x1,x2,x3]+O(h²),
    C=product_i Phi(x_i) product_(i<j)(x_j-x_i)>0.

The signs are checked by det[x,1,-p]=det[1,x,p] and det[x,1,1-xp]=det[1,x,xp]. Choose r sufficiently large: the full differentiated theta expansions prove p''>0 and (xp)''=2p'+xp''>0 on the interval containing the three x_i. Both divided differences are then positive. For h>0 sufficiently small one obtains S(r,r,r+h)<0. Although r1=r2 is a set of measure zero, continuity and r>0 allow perturbing to an OPEN region with 0<r1<r2<r3 where S<0.

**Scope.** Only pointwise positivity of THIS integrand is refuted, even after summing all its choices. It is not proved that det A is negative nor is compensation between integration regions, another non-local pairing or a different Gram excluded. A determinant identity is not promoted to an inequality. The attempt produces no new W/T positivity; no computations or changes to papers.


## 12. Reciprocal of the potential: moment criterion and explicit tail

**PROVED as an identity, sufficient implication, exterior bound and compact closure by Arb certificate.** Construction positive_identity_attempt; independent audit arithmetic_fresh_candidate PASS (identity with boundaries, tail and static review of the compact certificate); independent reproduction FULL PASS, exit 0 and same SHA256. Prior targeted consultation of indices, grid, crossword and 073/086/088/103_43. The object is p(r)=V'(r), NOT M=Z'/Z: the concavity of sqrt(lambda)/M(sqrt(lambda)) of 086 does not prove the following condition. No worldwide priority is claimed.

Set u=r², G(u)=V(sqrt(u)), a(u)=2G'(u)=p(r)/r, w=exp(-2G), and E the expectation with density w/integral(w). Let H=integral_0^infinito r Phi², J=integral r(Phi')², K=integral r(Phi'')². Then integral(w)=2H and

    J/H=E[u a²]=E[a+u a'],
    K/H=E[(u a²-a-2u a')²],
    (HK-J²)/H²=Var(a+u a')+E[u²(2a'²-a a'')].

The last identity results from integrating by parts with ua, u²a³ and u²aa'. At zero, a is regular by even analyticity and the factors u,u² annihilate the boundaries. At infinity, the theta supertails and the differentiated expansions justify integrability and vanishing of the boundaries. No boundary term of the original integration in r is omitted.

If a>0 and (1/a)''>=0 on the WHOLE half-line, then 2a'²-aa''=a³(1/a)''>=0 and HK>=J². Equality would force a+ua' constant; regularity at zero forces a constant. For theta, a'>0 by §9; the following compact certificate moreover completes the strict global condition.

**Explicit tail proved.** Write q(u)=1/a(u)=r/p(r). Direct differentiation gives

    q''(u)=N/(4r³p³),
    N=2r²p'²-r²pp''-rpp'-p².

For r>=1, Y=pi exp(2r)>21. The first mode satisfies

    p1=2Y-9/2-6/(2Y-3),
    p1'=4Y+24Y/(2Y-3)²,
    p1''=8Y-48Y(2Y+3)/(2Y-3)³.

POWER_THETA_DENSITY_OUTER_088§§3–4 controls the FULL tail and gives errors smaller than eta<1 in p,p',p''. Consequently

    0<p<2Y+1, 4Y-1<p'<4Y+2, p''<8Y+1.

Substituting with the correct signs (p''>0 is not needed) yields

    N>r²(16Y²-26Y+1)-r(8Y²+8Y+2)-(4Y²+4Y+1)
      >=r²(4Y²-38Y-2)>2r²Y²>0.

One uses r>=1 and 2Y²-38Y-2>0 for Y>21. Thus q''(u)>0 for ALL u>=1.

**History of the gate.** At the origin the convexity test, if V''(0)>0, is 10V^(4)(0)²-3V''(0)V^(6)(0)>=0; it is not deduced from V'''>0. mpmath60 diagnostics with 20 modes at the origin and r=1/4,1/2,3/4,1,3/2 gave a favourable sign, but were NOT certified and are not used in the following proof.

### 12.1. Compact closure with full theta and exact parity

**PROVED by Arb ball certificate, 2026-11-06.** Reproducible source: `tools/power_temporal_reciprocal_compact_verify.py`; output exit 0/FULL PASS in `tools/power_temporal_reciprocal_compact_verify.log`. SHA256 of the script: `498e199ae7bb52f7fedeef02847a1b8642a635b76bb036212259bc2f875e93fa`. Python-flint 0.9.0, precision 512 bits. Fixed parameters: 16 theta modes, degree 40 and 256 panels at the origin; 8192 panels and Taylor degree 24/cap 28 on the rest. No parameter search was run. The first direct interval evaluation of the rest was inconclusive due to dependency; it was replaced by the following entire polynomial. Degree 16 left an excessive absolute remainder near r=1; the a priori Cauchy bound fixed degree 24 before running the final version, keeping mesh and precision.

**Origin, without singular temporal quotients.** The FULL even function defines f(u)=Phi(sqrt(u)), holomorphic for |u|<=1/16, with |f|<1000 by 089§2. Its Taylor expansion up to degree 40 is obtained from the even coefficients of Phi at zero. Parity of the 16-mode prefix is not assumed: first ALL jets of the full series are enclosed and then the parity of Phi is used. On |z|<=1/4, the modal tail has modulus less than

    epsilon_O=304*17^4/4^289.

Cauchy gives error epsilon_O*4^j on each temporal coefficient of order j; the full odd coefficients include 0. For the derivatives of orders j=0,...,3 of the Taylor polynomial of f, on 0<=u<=1/64 the full remainder is bounded by

    2000*(41!/(41-j)!)*16^41*(1/64)^(41-j).

One uses |[u^k]f|<=1000*16^k and the consecutive ratio of the majorant, less than 1/2. The 256 panels of width 1/16384 certify f>0, f'<0 and

    L3=f''' f²-3f''f'f+2f'^3>2/5.

The output records the most precise lower bound, greater than 0.40639. Since a=-2f'/f, one concludes a>0 and a''=-2L3/f³<0; therefore (1/a)''>0 on ALL 0<=u<=1/64, including both endpoints.

**Rest, entire polynomial and controlled absolute errors.** On r∈[1/8,1], write F=Phi(r) and its temporal derivatives. The exact identity is

    T=N F³=-r²F'²F''+2r²F F''²-r²F F'F'''
              +rF'^3-rF F'F''-F F'².

On each disc |z-r|<=1/64, Re exp(2z)>1, |exp(2z)|<9 and |exp(5z/2)|<16. Thus |Phi_m(z)|<4800m^4*8^(-m²), |Phi(z)|<10000 and the tail after 16 modes is bounded by

    epsilon_R=9600*17^4/8^289.

The consecutive ratio of the modal majorant is less than 1/2. Cauchy gives error epsilon_R*64^j on each temporal Taylor coefficient. These errors are included BEFORE forming T. For |z-r|<=1/128, |Phi^(j)(z)|<=Pj=10000*j!*128^j, j<=3, and |z|<2. Substituting into the exact polynomial gives

    |T|<=4(P1²P2+2P0P2²+P0P1P3)
            +2(P1³+P0P1P2)+P0P1²<10^24.

The 8192 panels have half-width h=7/131072, so that 128h=7/1024. The remainder after degree 24 is, uniformly,

    REM_R=10^24*(7/1024)^25/(1-7/1024)<10^(-30).

Each panel certifies T(center) minus the sum of moduli of the nonconstant Taylor terms and REM_R strictly positive. The common lower bound of the output is greater than 10^(-17). The CLOSED cells and the endpoints 1/8,1 are covered; the sign is not inferred from sampled points.

**Denominators and assembly.** The origin also certifies a(0)=V''(0)>0. 073 proves V'''>0 on the whole half-line, hence V''(r)>V''(0)>0 and p(r)>0 for ALL r>0 since p(0)=0. Thus a>0 globally. Phi>0, T>0 and the formula for N prove q''>0 on 1/64<=u<=1. The origin covers 0<=u<=1/64; the tail of §12 covers u>=1. One obtains

    a(u)>0 y q''(u)>0 for EVERY u>=0,
    HK>J².

Strictness of the moments results directly from the identity of §12: u²(2a'²-aa'')=u²a³q'' is positive for u>0 and the density w is positive. The boundaries and integrability already justified there remain valid.

### 12.2. Local consequence for symmetric temporal triples

For the d,b,c,d0 of §10, set B=Phi(0)Phi''(0). Taylor under the full integrals, parity and supertails give

    d0=2H,
    c=2H-J R²+(K-B)R^4/12+O(R^6),
    d+b=4H-4J R²+(4K-B)R^4/3+O(R^6),
    D(R)=d0(d+b)-2c²=2(HK-J²)R^4+O(R^6).

The B terms keep the boundaries at zero and cancel exactly in D. In particular integral Phi Phi'''=-B and integral r Phi Phi''''=K+B are used; those boundaries are not discarded. The symmetrized integral identity of the previous attempt also provides D/d0=R^4(K-J²/H)+O(R^6).

Since HK>J², there exists R0>0 such that D(R)>0 for ALL 0<R<R0. The other sector has d-b>0 by §9. Therefore A at the three nodes (-R,0,R) is SPD for ALL sufficiently small positive R. R0 is not quantified nor is an interval certified by search. Together with §10 there are small and large families; NOT all intermediate R, arbitrary triples nor all orders are covered. There is no closure of the global sign, new W/T coverage or changes to papers.


### 12.3. Scope with respect to falsifier 074 and layer positivity

Cross-check and computation arithmetic_fresh_candidate, reviewed; consequences of existing formulas, not a proof of global sufficiency. In 074, n=999999 and a(u)=A[1+(u/4)^n]. Differentiating q=1/a gives

    q''(u)=n*4^(-n)*u^(n-2)*[(n+1)(u/4)^n-(n-1)]
             /[A(1+(u/4)^n)^3]<0 para0<u<=1.

Therefore falsifier 074 does NOT satisfy the new hypothesis of §12: it cannot be invoked to refute sufficiency of that additional hypothesis. This does not prove such sufficiency.

As an explicit contrast, V(r)=r²/2+r⁴/4+epsilon*r⁶/6, 0<epsilon<=1, satisfies a=1+u+epsilon*u², a'>0 and

    a³ q''=2(1-epsilon)+6epsilon*u+6epsilon²*u²>0, u>0.

However V'(R)/R³ tends to infinity, so the layer falsifier of §5 applies: the new condition does not make all layers S_v positive. Neither a falsifier nor a global proof of the INTEGRAL A was obtained for this family; the quartic case epsilon=0 of §4 does not authorize extrapolation. The constructive review did not produce a bound of the integral deficit D(R) for all R from convex q either. Intermediate R and all orders remain OPEN.


## 13. Reciprocal convexity does not suffice for all orders either

**PROVED, declared generic class.** Construction arithmetic_fresh_candidate, independent stability review positive_identity_attempt. Prior consultation of the three indices and §§8.7–8.9,12. Difference: the relative error is now controlled in C6, which preserves the new GLOBAL differential inequality, not only finite data. The real Phi is not refuted nor is its full arithmetic identity preserved.

There exist positive, even densities psi, holomorphic in the strip of Phi and arbitrarily close to Phi in C6 relative error, with the relative tails of §8.7, which satisfy

    V_psi'''(r)>0 for r>0,
    a_psi(u)=V_psi'(sqrt(u))/sqrt(u)>0,
    (1/a_psi)''(u)>0 for u>=0,

but whose A_psi is NOT PSD. The size of a negative block is not specified. These densities do satisfy HK>J² and positivity of small symmetric temporal triples by §12; there is no contradiction between those finite conclusions and the global failure.

**1. The relative cutoff of §8.7 is also small in derivatives.** With the same fixed even cutoff chi, n>=2, x=pi exp(2t)>=pi e for t>=1/2, set r_n=Phi_n/Phi_1. The explicit modal formula and D=2x partial_x give, for 0<=j<=6,

    |D^j r_n(t)|<=C_j n^(4+2j)(1+x)^j exp[-(n²-1)x].

The rational factors only have denominators 2x-3, separated from zero. The series of those bounds converge uniformly in x>=pi e. Therefore 1+sum_(n>=2)r_n and its first six derivatives are bounded, the denominator is >=1 and the derivatives of its inverse are bounded. Thus

    h_M=chi * [sum_(n>M)r_n]/[1+sum_(n>=2)r_n]

satisfies, for each fixed B>=0,

    ||h_M||_(B,6):=max_(j<=6) sup_t exp(B|t|)|D^j h_M(t)|
       <=C_B sum_(n>M)n^16 exp[-(n²-1)pi e/2] ->0.

The polynomial factors of x and exp(Bt)=(x/pi)^(B/2) are absorbed against half of the exponential. The derivatives of the cutoff only change C_B; h_M is zero near the origin. Uniform control in all orders of differentiation is not claimed.

**2. Stability of the differential inequalities.** For psi=Phi exp(-E), E even with ||E||C6<=delta, set beta(u)=E'(r)/r, u=r². The integral identities for an even function give on 0<=u<=1

    |beta|<=delta, |beta'|<=delta/6, |beta''|<=delta/60.

For example beta=integral_0^1 E''(tr)dt; differentiating using parity and the fundamental theorem of calculus gives beta'=(1/2)integral_0^1 t² integral_0^1 E^(4)(str)dsdt, and beta''=(1/4)integral t⁴ s² E^(6)(vstr)dvd sdt. The coefficients result from integrating those weights. By §12, a and S=2a'²-aa'' have strictly positive minima on [0,1]. The perturbation a+beta preserves both if delta is sufficiently small.

On r>=1, 088 gives |p|,|p'|,|p''|<=128Y, Y=pi exp(2r)>21, and §12 gives N>2r²Y². For delta<=1 the segments of perturbed jets are bounded by 129Y. The sum of the moduli of the three partial derivatives of the polynomial N with respect to p,p',p'' is <=1290r²Y. Hence

    |N_psi-N|<=1290delta r²Y.

Taking delta<=1/100 preserves N_psi>r²Y²>0 and p_psi>0, since p>2Y-6. This completes the global stability of a>0 and q''>0.

V'''>0 is also preserved: 073 certifies V^(4)>=m4>0 near 0, while |E'''(r)|<=delta r by parity. On a compact separated from 0 there is a positive minimum of V'''; in the tail V'''~8Y tends to infinity. Reducing delta preserves the three stretches. Therefore a_psi'>0 also follows from the same identity used in §9.

**3. Analyticity and negative block, in the correct order.** Take g=h_M*gamma_sigma with 0<sigma<=1. The derivatives commute with the convolution and

    ||g||_(B,6)<=||h_M||_(B,6) integral exp(B|z|)gamma_sigma(z)dz.

The factor is uniformly bounded for sigma<=1. Moreover 0<=g<=epsilon_M, and E=-log(1-g) is small in C6 when M is large. Choose FIRST M ensuring the preceding stability for all those sigma. The smooth density Phi(1-h_M) coincides with the prefix Phi_M on t>=1; §8.7 provides a finite negative block with nodes in (1,2). Choose AFTERWARDS sigma sufficiently small to preserve that block via the uniform convergence g->h_M and the entry bound 2||g-h_M||infinito A_Phi of §8.7. The final density psi=Phi(1-g) is even, positive and analytic; it preserves the declared tails and all the preceding differential inequalities.

**Scope.** Global sufficiency of this class of differential hypotheses is refuted, even together with C6 relative closeness and the indicated tails. An argument using the full theta structure, a specific additional compensation, or the investigation of intermediate triples of the real Phi are not ruled out. No new W/T window, no change to papers and no new computation.


## 14. The temporal reciprocal does not admit the proposed positive Laplace representation

**PROVED, arithmetic_fresh_candidate; independent mathematical review.** Targeted consultation of indices, grid and crossword by diagonal_gauge_dedup with no literal antecedent located: 086 concerns the reciprocal of M, 111 monotonicity in another parameter, and the HCM discards another density. The new question is q(u)=sqrt(u)/V'(sqrt(u)) of §12, not the sign of the original kernel. The argument only uses theta, Poisson, a finite Gauss sum and analytic uniqueness; it uses no external equivalence of the sign problem.

**Statement.** q, defined for u>0, has no holomorphic extension to ALL of Re u>0. In particular there is no positive measure mu on [0,infinito) such that

    q(u)=integral exp(-us)dmu(s), u>0.

Finiteness of that integral for each u>0 would imply holomorphy in the half-plane: on a compact Re u>=a>0 all derivatives are dominated by a constant times exp(-as/2), integrable. It is not necessary to assume finite total mass beforehand.

**1. Identity without denominators.** If Q were that extension, on the convex domain

    D={z=x+iy: x>|y|, |y|<pi/4}

one would have Q(z²)Phi'(z)+zPhi(z)=0. Both terms are holomorphic and the equality holds on the positive real axis by §12. Analytic uniqueness extends it to D. One does not divide by Phi' on that domain.

**2. Rational cusps and nonzero coefficient.** For each odd m>=3, take tau_m=16+2/m, w0=i tau_m and w=w0+delta, delta>0. The decomposition by residues modulo m and Poisson give exactly

    theta(w0+delta)=delta^(-1/2)/m
       *sum_(nu entero) exp[-pi nu²/(m²delta)] G_m(nu),
    G_m(nu)=sum_(j mod m) exp[-2pi i j²/m+2pi i nu j/m].

The term 16 does not change the phase. If G_m=G_m(0), then |G_m|²=m: on expanding the square, changing variables a=j-k,b=j+k modulo m is invertible and the sum is sum_(a,b)exp(-2pi i ab/m)=m. Therefore G_m is nonzero. For each fixed m,

    theta(w0+delta)=(G_m/m)delta^(-1/2)+resto.

The remainder and its first three derivatives are O_m(delta^(-N)exp(-c_m/delta)) for some N and c_m>0. It is obtained by differentiating the series over nu!=0: only powers of nu and delta^(-1) appear, dominated by part of the Gaussian exponential. Uniformity in m is not required.

**3. Limit of the reciprocal and contradiction.** With z=(1/2)Log w on the first-quadrant branch,

    Phi(z)=w^(5/4)[w theta''(w)+(3/2)theta'(w)].

The algebraic terms of order delta^(-3/2) cancel exactly. Thus

    Phi(z)=(3G_m/(4m))w0 w^(5/4)delta^(-5/2)+resto,
    Phi'(z)/Phi(z)=-5w0/delta+O_m(1).

Control of the differentiated remainder justifies both equivalents; the leading terms are nonzero. The identity of step 1 forces

    Q(z²)=-zPhi(z)/Phi'(z) ->0 cuando delta baja a0.

These z belong to D and converge to z_m=(log tau_m)/2+i pi/4. Moreover Re(z_m²)>0, since (log tau_m)/2>log4>1>pi/4. By continuity of the hypothetical extension, Q(z_m²)=0 for all odd m. The points z_m² are distinct and converge to the interior point (log4+i pi/4)² of the half-plane. Analytic uniqueness forces Q identically zero there, contrary to q(u)>0 on the real axis. This proves the statement.

**Scope of the moment test.** Before this proof, the coefficients of q of orders 0,...,39 were evaluated using the FULL jets already enclosed in the certificate of §12 (degree 40 of Phi(sqrt u)); all their alternating signs are strictly positive. That test is not used in the proof nor extrapolated. The discard only concerns the proposed positive representation of q and its holomorphic extension; it does not refute q''>0, HK>J², the positive triples nor A_Phi. No new W/T nor changes to papers.


## 15. Convex G does not suffice even for symmetric temporal triples

**PROVED by elementary countermodel.** Construction positive_identity_attempt, review arithmetic_fresh_candidate PASS. Targeted consultation of indices, grid, crossword and 074/101 with no literal temporal falsifier of this kind located. Difference: the sufficiency of convex G for the block (-R,0,R) is decided, not a block of the exponent kernel nor all orders at once.

Take exactly epsilon=1/1000 and

    phi(r)=exp(-r²/2-epsilon*r⁶/6),
    G(u)=u/2+epsilon*u³/6, u=r².

G'>0, G''=epsilon*u>0 for u>0 and V'''(r)=20epsilon*r³>0 for r>0. The density is even, positive and entire; its supertails justify all boundaries and differentiations of §12. In particular its temporal pairs are SPD by §9.

With a=1+epsilon*u², w=exp(-u-epsilon*u³/3), Z=integral_0^infinito w and E the normalized expectation, the identity of §12 gives

    Delta=(HK-J²)/H²
      =-2epsilon E[u²]+epsilon²(15E[u⁴]-9E[u²]²).

Define I_j=integral u^j w. The elementary inequality exp(-x)>=1-x and the factorial integrals give

    I_2>=2!-epsilon*5!/3=2-40epsilon=49/25,
    I_4<=4!=24.

Discarding only the nonpositive term of Delta yields

    Delta<=(epsilon/Z)[-2I_2+15epsilon I_4]
         <=-89/(25000Z)<0.

By the expansion of §12.2, the determinant of the symmetric sector satisfies D(R)=2(HK-J²)R⁴+O(R⁶)<0 for ALL sufficiently small R>0. Thus the three-node temporal matrix (-R,0,R) is indefinite. No search or numerical evaluation of R is required.

This potential does not satisfy the new reciprocal convexity: q(u)=1/(1+epsilon*u²) has q''(0)=-2epsilon<0. The result does not contradict §12 for the real theta nor refute the power triples 080. Nor does it say that convex q suffices for arbitrary triples. Only the sufficiency of convex G (even accompanied by V'''>0) for symmetric temporal triples is discarded. No computations, new W/T or changes to papers.


## 16. Equivalent of the full kernel at fixed integer scales

**PROVED, 2026-11-06.** Construction joint_sign_fresh_review, computation and independent verification global_restart_checked; independent mathematical audit arithmetic_fresh_candidate PASS and second review PASS, including prefactors and corollary. Consulted: the project rules, the three indices and the relevant primary sources; targeted cross-check with no literal antecedent located for the following equivalent of A. The arithmetic Grams of phase209 [CONSTRUCTOR_005](../phase-209-nonlocal-kernel/CONSTRUCTOR_005.md) and [AUDIT_005](../phase-209-nonlocal-kernel/AUDIT_005.md) are explicit antecedents: the gcd kernel and its positivity are classical, not new. The difference is identifying here the leading term of the FULL REAL A, with its near-resonances controlled, not replacing A by a favourable arithmetic Gram. The band average of §4.1 is an antecedent of the oscillatory method; by itself it did not give this equivalent on the whole half-line.

### 16.1. Statement and exact formula

Let k,l be FIXED positive integers, z_k=(log k)/2+iy, epsilon=cos(2y) decreasing to 0 and L=log(1/epsilon). Define rho(k,l)=0 if k,l do not have the same squarefree part. If k=d a²,l=d b² with d squarefree, set

    rho(k,l)=gcd(a,b)/sqrt(ab).

Then

    A(z_k,conjugado(z_l))
      =[105/(512sqrt2)] rho(k,l) epsilon^(-9/2) L²
         +O_(k,l)(epsilon^(-9/2) L).                 (INT-ASYM)

The remainder is complex in general; its constants depend on k,l. Uniformity in those integers, the number of nodes or their separation is not claimed.

For sigma=sin(2y), t=exp(2r)>=1 and c_kl=(log k+log l)/2, the exact representation keeps the temporal factor:

    A(z_k,conjugado(z_l))
       =integral_1^infinito w_kl(t) Phi_k(t) conjugado(Phi_l(t))dt,
    w_kl(t)=[log t+c_kl]/(2t),
    Phi_k(t)=Phi((log(kt))/2+iy)=U_k(t)+V_k(t),
    U_k(t)=2pi²(kt)^(9/4)exp(9iy/2)
                   sum_(n>=1)n4 exp[-pi(epsilon+i sigma)kt n²],
    V_k(t)=-3pi(kt)^(5/4)exp(5iy/2)
                   sum_(n>=1)n² exp[-pi(epsilon+i sigma)kt n²].

For fixed epsilon>0, the series and their products are absolutely integrable on t>=1 with this weight; the Gaussian exponential dominates all polynomial and logarithmic factors. Thus Fubini and the following amplitude differentiations are justified before taking epsilon to 0. The leading product has the EXACT prefactor

    4pi4(kl)^(9/4) sum_(n,m>=1)n4m4
       integral_1^infinito w_kl(t)t^(9/2)
          exp[-pi epsilon t(kn²+lm²)]
          exp[-i pi sigma t(kn²-lm²)]dt.             (MAIN)

### 16.2. Near-resonances: elementary control also for quadratic approximations

With the prime indicating kn²!=lm², one proves for ALL delta>0

    S_delta=sum' n4m4 exp[-delta(kn²+lm²)]/|kn²-lm²|
       <=C_(k,l) delta^-4 log(2+1/delta).            (NEAR)

To see it, decompose into dyadic boxes with max(n,m) comparable to N. Outside a region where sqrt(k)n and sqrt(l)m are comparable, the denominator is >=c_(k,l)N²; the sum of numerators is O(N10), and the block is O(N8). In the comparable region, set alpha=sqrt(k/l); the denominator is comparable to N|alpha n-m|.

If alpha is irrational, integrality of kq²-lp² implies |alpha q-p|>=c_(k,l)/q for the nearest integer p and q>=1. The residues alpha n of a box of length O(N) are therefore separated on the circle by at least c_(k,l)/N and also at that distance from 0. Ordering their distances to the integers gives sum_n dist(alpha n,Z)^(-1)<=C_(k,l)N log(2N). The nearest m contribute O(log(2N)) to the sum of inverse denominators of the box; the other m contribute the same by the harmonic sum of their distances. Multiplying by n4m4<=C N8, one obtains O(N8 log(2N)). If alpha is rational, the nonzero distances have a fixed denominator; only the exact resonances are omitted and the same harmonic bound suffices. This keeps, in particular, the approximations with |kn²-lm²| small and nonzero.

Summing O(N8 log(2N))exp(-c delta N²) over dyadic N proves (NEAR) for delta<=1. For delta>=1, extracting part of the exponential gives S_delta<=C exp(-c delta)<=C' delta^-4, which completes the formula for all delta.

On t∈[T,2T], T=2^j>=1, integrate by parts against the phase of (MAIN). With Q=kn²+lm² and d_nm=kn²-lm² different from 0, the boundary and the derivative of the amplitude are bounded by

    C_(k,l) T^(7/2)(1+log T)
         (1+epsilon T Q)exp(-pi epsilon T Q).

The additional factor is absorbed in part of the exponential. Since sigma>=1/2 eventually, the oscillatory integral is <=C T^(7/2)(1+log T)exp(-c epsilon T Q)/|d_nm|. Applying (NEAR) with delta=c epsilon T and summing over all T gives, for ALL non-resonant pairs of (MAIN),

    <=C_(k,l) epsilon^-4
        sum_(T=2^j) T^(-1/2)(1+log T)log(2+1/(epsilon T))
    <=C'_(k,l) epsilon^-4 log(2+1/epsilon).          (OFF)

The dyadic sum T^(-1/2)(1+log T) converges. No uniform bound for arbitrary real ratios has been used nor have near-resonances been deleted.

### 16.3. Exact resonances and constant of the equivalent

If k,l do not share a squarefree part, there are no exact resonances. Otherwise, write k=d a²,l=d b²,g=gcd(a,b). All resonances are

    n=(b/g)j, m=(a/g)j, j>=1,
    kn²=lm²=Lambda j², Lambda=d(ab/g)²,
    (kl)^(9/4)n4m4=(kl)^(1/4)(Lambda j²)^4,
    (kl)^(1/4)/sqrt(Lambda)=rho(k,l).

Set F(s)=s^(9/2)sum_(j>=1)j8 exp(-2pi s j²). The same uniform Riemann argument of §4.1 gives

    F(s)=F0+O(sqrt s), s bajando a0,
    F0=Gamma(9/2)/[2(2pi)^(9/2)],
    F(s)<=C s^(9/2)exp(-c s), s>=1.

The full resonant contribution is exactly

    4pi4 rho(k,l) epsilon^(-9/2)
       integral_1^infinito [log t+c_kl]/(2t) F(epsilon Lambda t)dt.

With s=epsilon Lambda t, replacing F by F0 on epsilon Lambda<=s<=1 yields F0 log²(1/epsilon)/4+O_(k,l)(L). The error O(sqrt s) is integrated against [log(s/(epsilon Lambda))+c_kl]/s and is O_(k,l)(L); the tail s>=1 is also O_(k,l)(L) by its exponential decay. The constant shifts log Lambda and c_kl only affect that remainder. Since

    4pi4 F0=105/(128sqrt2),

one obtains the coefficient 105 rho(k,l)/(512sqrt2) of (INT-ASYM).

### 16.4. Lower terms, corollary and scope

The absolute Gaussian bounds, valid for all t>=1, give

    |U_k(t)|<=C_k epsilon^(-5/2)t^(-1/4),
    |V_k(t)|<=C_k epsilon^(-3/2)t^(-1/4).

The weight w_kl(t)t^(-1/2) is integrable on [1,infinito). Therefore the L²(w_kl dt) norms of U_k,V_k are O_(k,l)(epsilon^(-5/2)) and O_(k,l)(epsilon^(-3/2)). Cauchy–Schwarz bounds the crossings U_k conjugado(V_l), V_k conjugado(U_l) by O_(k,l)(epsilon^-4), and the lower product by O_(k,l)(epsilon^-3). Together with (OFF), they are absorbed in the remainder O_(k,l)(epsilon^(-9/2)L). It is not previously assumed that A is PSD.

**Corollary for a fixed list.** For any FIXED finite list of distinct positive integers k_i, the matrix [rho(k_i,k_j)] is positive definite. Distinct squarefree parts give separate blocks. Within each block, congruence by sqrt(a_i) produces [gcd(a_i,a_j)]. The CLASSICAL identity gcd(a,b)=sum_(q|a,q|b)phi(q), with phi(q)>0, gives a Gram of divisor incidences; over the distinct ordered a_i, the columns q=a_i form a triangular matrix with diagonal 1. Thus the Gram is positive definite. This identity and the arithmetic positivity are not presented as new.

Consequently, for each such list, the complex Hermitian block [A(z_(k_i),conjugado(z_(k_j)))] is positive definite when epsilon is sufficiently small: dividing by epsilon^(-9/2)L² one obtains [105/(512sqrt2)]rho+O_lista(1/L), whose limit has positive minimal eigenvalue. The threshold DEPENDS on the list; there is no uniformity in dimension or integers nor is a numerical value of the threshold certified. Repeated integers only duplicate nodes and do not give strict definiteness.

The result identifies an arithmetic leading term of the full original kernel and proves this corollary for fixed COMPLEX blocks. It does not prove PSD of A on a real window, CPD of log A, positivity of H, a uniform relative comparison of all orders nor the global sign. It is not confused with the renormalized kernel of phase209 nor is its norm transferred to the carrier of the paper. No campaigns, numerical data, new W/T coverage or changes to papers.

### 16.5. The comparator rho gives no uniform domination even after normalizing the diagonal

**PROVED, same date and entry.** Proposal, computation global_restart_checked; independent audit arithmetic_fresh_candidate PASS and second review PASS. Targeted cross-check in the three indices and corpus phase209/211 with no literal antecedent located for this limit of consecutive integers. The antecedent of §4.3 studies another tail with real variables; here y∈(0,pi/4) is fixed FIRST, hence epsilon=cos2y>0 and sigma=sin2y, and AFTERWARDS k tends to infinity with l=k+1. That order is not exchanged with (INT-ASYM).

Set x_k=(log k)/2, u=x_k+x_l and E=epsilon(k+l)+i sigma(k-l). For k,l in {k,k+1}, the FULL theta series, normalized by its first mode, gives uniformly in r>=0, with s=exp(2r)-1,

    Phi(z_k+r)/Phi(z_k)
      =(1+s)^(9/4)exp[-pi k exp(2iy)s] B_k(s),
    B_k(s)=1+O_y(1/k)+O_y(exp(-3pi epsilon k)).

Indeed, the quotient of the rational factor of the first mode is [1-a_k/(1+s)]/[1-a_k], a_k=3/[2pi k exp(2iy)], and differs from 1 by O(1/k) uniformly. The full relative tail is bounded by C_y sum_(n>=2)n4 exp[-pi(n²-1)epsilon k(1+s)]<=C'_y exp(-3pi epsilon k). For k sufficiently large, those factors also show Phi(z_k)!=0. With D_kl(s)=B_k(s)conjugado(B_l(s)), one obtains exactly

    A(z_k,conjugado(z_l))/[Phi(z_k)conjugado(Phi(z_l))]
       =(1/2)integral_0^infinito [u+log(1+s)](1+s)^(7/2)
                           exp(-pi E s) D_kl(s)ds.

Here D_kl=1+O_y(1/k) uniformly and Re E is comparable to k for fixed y. The amplitude without D is u+O((u+1)s(1+s)^(7/2)); integrating the error against exp(-pi Re E s) gives O_y((u+1)/k²). Thus

    A(z_k,conjugado(z_l))/[Phi(z_k)conjugado(Phi(z_l))]
       =u/(2pi E) [1+O_y(1/k)],
    A(z_k,conjugado(z_k))/|Phi(z_k)|²
       =x_k/(2pi epsilon k) [1+O_y(1/k)].

The diagonals of A are positive by their horizontal integral. Define the normalized block C_y(k,l)=A(z_k,conjugado(z_l))/sqrt(A(z_k,conjugado(z_k))A(z_l,conjugado(z_l))). For l=k+1, the preceding formulas imply

    |C_y(k,k+1)|
       =[epsilon sqrt(k(k+1))(x_k+x_(k+1))
          /(sqrt(x_k x_(k+1)) |epsilon(2k+1)-i sigma|)]
            *[1+O_y(1/k)] ->1.

But rho(k,k+1)=0: if they shared a squarefree part, 1=d(b²-a²), impossible for positive a,b. The rho block is therefore I_2, while the minimal eigenvalue of the C_y block is 1-|C_y(k,k+1)| and tends to 0. For ANY y fixed as above there is no c_y>0 such that C_y>=c_y rho on all integer blocks, even if c_y depends on y. Likewise sup_(k,l)|C_y(k,l)-rho(k,l)|>=1 for each fixed y; in particular there is no uniform o(1) approximation to rho as epsilon decreases to 0.

Only these two statements about the comparator rho WITH THIS diagonal normalization are discarded. No negative value of A is proved, A is not assumed PSD and other models, weights or compensations are not excluded. The equivalent for fixed nodes of §16.1 and its corollary remain valid; the escape limit shows why they do not extend uniformly in the integers. A joint variable regime of epsilon,k or a transition law is not claimed here. Global sign OPEN; no new route, computations, W/T coverage or changes to papers.


## 17. Exact sum of squares for the full resonant part

**PROVED, 2026-11-06.** Construction joint_sign_fresh_review, independent verification global_restart_checked; independent mathematical audit arithmetic_fresh_candidate PASS and second review PASS for the SOS identity, its strict positivity and the antecedent of an individual frequency. Read: the project rules, the three indices, POWER_SIGNED_MEAN_019 with its audit and phase209 CONSTRUCTOR_005/AUDIT_005; targeted cross-check without this literal identity located. The tools of divisors, factorials and sums of squares are known. The difference is keeping the EXACT resonant part of the kernel A and constructing an SOS that couples distinct frequencies via change of scale. A mean is not inverted by Möbius as in 019 nor is the object replaced by the renormalized Gram of 209.

Fix real y with |y|<pi/4, including y=0; set a_y=exp(2iy), epsilon=cos(2y)>0 and z_k=(log k)/2+iy for k a positive integer. In the exact modal expansion of §16, define R_res as the contribution of ALL pairs with kn²=lm², keeping the full integral t>=1 and both terms of the modal polynomial. The remaining contribution of A contains kn²!=lm². To fix the normalizations, set

    h_lambda(t)=pi(lambda t)^(5/4)(2pi a_y lambda t-3)
                         exp(5iy/2)exp(-pi a_y lambda t),
    Phi((log(kt))/2+iy)=sum_(n>=1)n^(-1/2)h_(kn²)(t),
    H(u)=|h_u(1)|²
        =pi²u^(5/2)|2pi a_y u-3|²exp(-2pi epsilon u),
    I_lambda=lambda^(-1/2)integral_lambda^infinito H(u)/(2u)du,
    J_lambda=lambda^(-1/2)integral_lambda^infinito
                                      log(u/lambda)H(u)/(2u)du.

For lambda>=1, H(u)>0 on u>=lambda, since 2pi u>3; therefore I_lambda,J_lambda>0. The whole argument uses fixed epsilon>0, without boundary approximation.

**Later bibliographic cross-check (2026-11-06).** The representation of a graph form via squared differences and potential has a general antecedent in Keller–Pinchover–Pogorzelski, [Criticality theory for Schrödinger operators on graphs, §4.2](https://arxiv.org/html/1708.09664#S4.SS2). Alexeev et al., [Primitive sets and von Mangoldt chains, Example 2.4 and §10.1](https://arxiv.org/html/2605.00301v1#S10.SS1), use the chain P(q→q/m)=Lambda(m)/log q. For each d, the weight nu_d(q)=I_(dq²)log q, q>=2, reproduces exactly the conductances Lambda(m)I_(dq²) of the following SOS; q=1 is the absorbing endpoint. Abbreviating I_q=I_(dq²), J_q=J_(dq²), its potential is D_q=J_q+log(d)I_q+Out_q−In_q, with Out_q=log(q)I_q and In_q=sum_(m>=2)Lambda(m)I_(qm). The subinvariance of the different weights of the article is not transferred: D_q>0 is proved here by the following bounds. No novelty is attributed to completing squares, to the divisor graph or to the factorial identity. The targeted search fresh_global did not locate the same theorem with these theta weights and this bound on D_q; that does NOT establish worldwide priority. The chain does not estimate the products of profiles of distinct frequencies of the non-resonant remainder; §17.6 still applies. This bibliographic comparison adds no sign nor a closure method.

### 17.1. An individual frequency can be indefinite

At the nodes k=1,4, the common frequency lambda=4 corresponds to n=2,m=1. Its matrix, using I_4,J_4 just defined, is exactly

    [[J_4, sqrt2(J_4+log2 I_4)],
     [sqrt2(J_4+log2 I_4), 2(J_4+2log2 I_4)]],
    det=-2(log2)² I_4²<0.

This discard of positivity per frequency does NOT apply to the sum of all of them. The following construction proves precisely compensation between frequencies; it does not require each individual resonant block to be PSD.

### 17.2. Direct divisorial transformation and SOS identity

Resonances only couple integers with the same squarefree part. Fix one of those groups k=d a², with d squarefree, and complex coefficients c_a of FINITE support. Abbreviate I_q=I_(dq²), J_q=J_(dq²), and define

    f_q=sum_(a|q)sqrt(a)c_a,
    g_q=sum_(a|q)sqrt(a)log(a)c_a.

The frequency lambda=dq² receives exactly the indices a|q, with n=q/a. The factor n^(-1/2)=sqrt(a/q) and the change u=lambda t, with sqrt(d)/sqrt(lambda)=1/q, give

    R_res[c]/sqrt(d)
       =sum_(q>=1)[(J_q+log(d)I_q)|f_q|²
                               +2I_q Re(g_q conjugado(f_q))].

The elementary identity sum_(m|r)Lambda(m)=log r gives DIRECTLY

    g_q=log(q)f_q-sum_(m|q,m>=2)Lambda(m)f_(q/m).

Completing the squares and reindexing the terms of |f_(q/m)|² produces the exact identity

    R_res[c]/sqrt(d)
       =sum_(q>=1) D_q |f_q|²
          +sum_(q>=1)sum_(m|q,m>=2)
                     Lambda(m)I_q |f_q-f_(q/m)|²,             (RES-SOS)
    D_q=J_q+[log d+log q]I_q
                    -sum_(m>=2)Lambda(m)I_(qm).

To check factors and orientation: the squares contribute log(q)I_q to the diagonal q via sum_(m|q)Lambda(m)=log q, and contribute sum_(m>=2)Lambda(m)I_(qm) on reindexing the other diagonal. The rest is exactly D_q, while the crossing is -2Lambda(m)I_q Re(f_q conjugado(f_(q/m))). No signed terms have been eliminated nor has a Möbius inversion been introduced.

### 17.3. The diagonal coefficient D_q is strictly positive

With lambda=dq², rescaling in each I_(qm) and applying Tonelli to its nonnegative summands gives

    D_q=lambda^(-1/2)integral_lambda^infinito H(u)/(2u)
       *[log u-log q
          -sum_(2<=m<=sqrt(u/lambda))Lambda(m)/m]du.          (DIAG)

For X>1, N=floor X, the factorial identity and floor(X/m)>=X/(2m), m<=X, imply

    log(N!)=sum_(m<=X)Lambda(m)floor(X/m)
       >=(X/2)sum_(2<=m<=X)Lambda(m)/m,
    sum_(2<=m<=X)Lambda(m)/m
       <=2log(N!)/X<2log X.

The last inequality is strict for ALL X>1, including 1<X<2: log(N!)<Xlog X. For u>lambda, take X=sqrt(u/lambda). The bracket of (DIAG) is strictly greater than

    log u-log q-log(u/lambda)=log d+log q>=0.

Since H(u)>0 on u>=lambda, one concludes D_q>0 for ALL d,q>=1. It also holds when d=q=1: the constant lower bound is then 0, but the bracket is strictly positive on all u>lambda.

### 17.4. Convergence, definiteness and scope

For fixed epsilon>0, I_(dq²),J_(dq²) are bounded by a polynomial in q times exp(-c_y d q²); this follows directly from the polynomial-times-Gaussian form of H. The f_q,g_q are bounded because c has finite support. In particular the preceding expressions converge absolutely. For the squares of (RES-SOS), sum_(m|q)Lambda(m)=log q and the boundedness of f suffice. The reindexed sum of incoming diagonals also converges, since sum_q sum_(m>=2)Lambda(m)I_(qm)=sum_r log(r)I_r<infinito. These bounds justify the square expansions and all reindexings; the original modal sums are likewise absolutely integrable for fixed epsilon>0.

The weights of (RES-SOS) are nonnegative and D_q is strictly positive. If c is nonzero, choose a0 minimal with c_(a0)!=0; its proper divisors have coefficient 0, hence f_(a0)=sqrt(a0)c_(a0)!=0. The first sum is therefore strictly positive. Summing the squarefree groups, which do not couple in R_res, proves that R_res is a POSITIVE DEFINITE kernel on ANY finite set of distinct positive integers k, for EACH real y with |y|<pi/4, including 0. There is no size restriction nor a list-dependent threshold for THIS exact part. Repeated indices are grouped and only give semidefiniteness as a redundant representation.

The change u=lambda t and the direct divisorial transformation couple distinct frequencies lambda, each potentially indefinite. That is why the proof avoids requiring PSD of the layers or of each frequency; it does not erase the arithmetic structure. Nor does the result contradict §16.5: R_res is the exact resonant part, not the limiting comparator rho nor a domination of A by it.

**Scope of the sign obtained.** All orders of R_res on the positive INTEGER indices k are proved. NOT all real nodes of the kernel A nor the sign of the contribution kn²!=lm² are proved. A joint control of that non-resonant contribution is still missing. The later bridge of §18 eliminates the additional obligation of passing from the FULL integer A to all real nodes; it does not transfer R_res separately nor prove the missing sign. No A PSD, CPD, positivity of the kernel partial_t partial_s log A, new W/T window or global closure is inferred. No campaigns, numerical data, auxiliary files or changes to papers.

### 17.5. Uniform bound in the exact divisorial energy

**PROVED, same date and entry.** Refinement joint_sign_fresh_review; independent verification global_restart_checked, audit arithmetic_fresh_candidate PASS and second review PASS. For ALL d,q>=1 and ALL 0<epsilon<=1 of the preceding family,

    D_q>=c_* I_q,
    c_*=(log2/3)*(4pi-3)²exp(-6pi)
                /[(4pi+3)²+(4pi-3)²exp(-6pi)]>0.             (UNIF-D)

If dq>=2, the proof of §17.3 already gives D_q>=log(dq)I_q>=log2 I_q, stronger. Only d=q=1,lambda=1 remains. For X>=2 and N=floor X, at least floor(N/2) factors of N!/N^N are <=1/2; therefore

    N!<=N^N 2^(-floor(N/2)),
    sum_(2<=m<=X)Lambda(m)/m
       <=2log(N!)/X
       <=2log X-[2floor(N/2)/X]log2
       <=2log X-log2/3.

One used 2floor(N/2)>=N-1 and (N-1)/X>(N-1)/(N+1)>=1/3. In the bracket of (DIAG) for d=q=1, set X=sqrt u. For u>=4 the preceding bound gives a lower bound beta=log2/3. For 2<=u<4 the sum is empty and the bracket is log u>=log2. Thus that same lower bound beta holds on ALL u>=2; on [1,2] the bracket is nonnegative by §17.3.

Write C for the mass of H(u)/(2u) on [1,2] and T for its mass on [2,infinito). Since |a_y|=1 and 0<epsilon<=1,

    C<=C_max=pi²sqrt2(4pi+3)²,
    T>=integral_2^3 H(u)/(2u)du
       >=T_min=pi²sqrt2(4pi-3)²exp(-6pi).

The first bound uses u^(3/2)<=2sqrt2, |2pi a_yu-3|<=4pi+3 and exp(-2pi epsilon u)<=1. The second uses u^(3/2)>=2sqrt2, |2pi a_yu-3|>=4pi-3 and exp(-2pi epsilon u)>=exp(-6pi) on [2,3]. Therefore

    D_1>=beta T,
    D_1/I_1>=beta T/(C+T)
              >=beta T_min/(C_max+T_min)=c_*.

This completes (UNIF-D). For a finite vector on the integers k, separate k=d a² and set f_(d,q)=sum_(a|q)sqrt(a)c_(d a²). The identity (RES-SOS) implies

    R_res[c]>=c_* E_y[c],
    E_y[c]=sum_(d libre de cuadrados)sqrt(d)
                    sum_(q>=1) I_(dq²)|f_(d,q)|².            (DIV-LOWER)

The constant c_* is uniform in epsilon,d,q and support size, but E_y keeps the EXACT weights I_(dq²), which depend on epsilon and on the indices. It is not a uniform margin with respect to the Euclidean norm of the coefficients nor a comparison for the full A. The non-resonant term remains uncontrolled. The later bridge of §18 transfers the eventual positivity of the FULL integer A to all real nodes; it does not transfer this resonant bound separately nor add a W/T window or global closure. No computations, new route or changes to papers.

### 17.6. The energy E_y does not dominate the non-resonant damage uniformly

**PROVED, same date and entry.** Proposal, independent verification global_restart_checked; audit arithmetic_fresh_candidate PASS and second review PASS for the following limits and scopes, including the extension to y=0. Consulted the three indices, §16.5 and §17.5; targeted cross-check with no literal antecedent located for Off_y/E_y. Fix FIRST y∈[0,pi/4) and AFTERWARDS let k tend to infinity. Abbreviate A_y(k,l)=A(z_k,conjugado(z_l)) and Off_y=A_y-R_res,y, without assigning a sign to either of the two full matrices.

For a single index k=d a², the exact diagonals of (DIV-LOWER) and of the resonant part are

    e_k=E_y[delta_k]=sqrt(k)sum_(n>=1)I_(kn²),
    r_k=R_res,y(k,k)
       =sqrt(k)sum_(n>=1)[J_(kn²)+log(k)I_(kn²)].

The change u=lambda+s in the integrals of I,J, with fixed y, gives

    I_lambda=H(lambda)/[4pi epsilon lambda^(3/2)]
                       *[1+O_y(1/lambda)],
    J_lambda/I_lambda=O_y(1/lambda),
    sum_(n>=2)I_(kn²)/I_k=O_y(exp(-6pi epsilon k)).

These bounds do not differentiate an asymptotic remainder: one writes H(u)/(2u)=p_y(u)exp(-2pi epsilon u), with p_y(u) comparable to u^(7/2) and logarithmic derivative O_y(1/u) for u large. After u=lambda+s, the quotient p_y(lambda+s)/p_y(lambda) has error bounded by C_y s(1+s)^M/lambda; it is integrated against exp(-2pi epsilon s). For J one uses log(1+s/lambda)<=s/lambda. The tail in n is bounded by C_y sum_(n>=2)n6 exp[-2pi epsilon k(n²-1)], which gives the last formula. In particular

    r_k/e_k=log k+O_y(1/k).

The FULL theta tail of §16.5 is O_y(exp(-3pi epsilon k)) relative to the first mode, uniformly in r>=0. Its contribution to A_y(k,k) relative to the square of that mode has that same relative error, since the diagonal weight is positive. The tail of squares of modes in r_k has relative error O_y(exp(-6pi epsilon k)). Therefore

    Off_y(k,k)/e_k=O_y(log k exp(-3pi epsilon k))->0,
    A_y(k,k)/e_k=log k+o(1).

The consecutive integers k,l=k+1 have distinct squarefree parts. Thus E_y and R_res,y have crossing 0 at that pair, while Off_y(k,l)=A_y(k,l). The correlation of §16.5, with error O_y(1/k), implies

    |A_y(k,k+1)|/sqrt(e_k e_(k+1))=log k+o(1).

At y=0, §16.5 is not invoked outside its statement: its endpoint proof applies directly with epsilon=1,sigma=0,E=k+l>0. The full tail is still O(exp(-3pi k)), and the same integral D_kl gives A_0(k,l)/[Phi(x_k)Phi(x_l)]=(x_k+x_l)/[2pi(k+l)]*(1+O(1/k)). This also proves the necessary correlation at y=0. There A_0(k,l)>0 and the real coefficients can be chosen with signs (+,-).

Choose c^(k) with two entries of moduli (2e_k)^(-1/2),(2e_(k+1))^(-1/2) and phase making the crossing of A_y negative. Then

    E_y[c^(k)]=1,
    Off_y[c^(k)]
       =(1/2)[Off_y(k,k)/e_k+Off_y(k+1,k+1)/e_(k+1)]
             -|A_y(k,k+1)|/sqrt(e_k e_(k+1))
       =-log k+o(1)->-infinito,
    R_res,y[c^(k)]=log k+o(1),
    A_y[c^(k)]=o(1),
    A_y[c^(k)]/R_res,y[c^(k)]->0.

There is no finite C_y such that Off_y>=-C_y E_y on all integer blocks. Nor is there delta_y>0 with A_y>=delta_y R_res,y uniformly, or equivalently Off_y>=-(1-delta_y)R_res,y. Both constants could depend on y and still fail already on these pairs, INCLUDING y=0. This limits the payment via the margin E_y and the perturbation strictly smaller than R_res; it does NOT prove A negative nor decide the critical inequality Off_y>=-R_res,y. At y=0 the real pairs are SPD by §9 and these vectors have A_0[c^(k)]>0, although their quotient with R_res,0 tends to 0. The SOS of §17 and its lower bound (DIV-LOWER) remain valid. No new general impossibility principle, route, computations, W/T window or edited papers.

### 17.7. The scalar logarithmic bound also fails on the exact theta carrier

**PROVED, same date and entry.** Construction joint_sign_fresh_review, independent verification global_restart_checked; audit arithmetic_fresh_candidate PASS and second review PASS. Prior cross-check: phase199 [PROOF_L_SHARP_C_001§4, Prop4.2](../phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_C_001.md) already proves unboundedness of the direct dilation map on L²; [PROOF_L_SHARP_E_001§3, Rem3.1](../phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_E_001.md) already contains the comb operator via the divisorial commutator. [BRIDGE002§3](POWER_BRIDGE_002.md) uses C1 approximation by polynomials, [AUDIT_L_SHARP_1§2.4](../phase-199-frontier-pattern/proof-L-sharp/AUDIT_L_SHARP_1.md) uses compact Möbius inversion on another map and 019§§3–5 keeps the limit of inverting means. Unboundedness of dilations is not presented as a new principle. The bounded difference is checking THIS quadratic inequality with logarithmic weight on EXACT theta aggregates, using density in a norm where the operator is continuous.

Here y=0, t>=1. Define T_mF(t)=F(mt), so that T_m²F(t)=F(m²t), and

    C=sum_(m>=2) Lambda(m)m^(-1/2) T_m²,
    Theta_k(t)=Phi((log(kt))/2), k entero positivo,
    Q_C(F)=integral_1^infinito (CF)(t)conjugado(F(t))dt/(2t),
    W(F)=integral_1^infinito (1+log t)|F(t)|²dt/(2t).

There is NO finite M such that |Q_C(F)|<=M W(F) for all F in the FINITE complex span of the Theta_k.

**Continuity in a strong norm and density of the carrier.** For 0<gamma<2pi, use the EXPONENTIAL space

    H_gamma=L²([1,infinito), exp(gamma t)dt/t).

It is not a power weight. The change u=m²t gives

    ||T_m²F||_(H_gamma)²
       =integral_(m²)^infinito exp(gamma u/m²)|F(u)|²du/u
       <=exp[-gamma(m²-1)]||F||_(H_gamma)².

Hence C is bounded on H_gamma, since sum_(m>=2)Lambda(m)m^(-1/2)exp[-gamma(m²-1)/2] converges. Q_C and W are continuous forms on H_gamma; for W one uses 1+log t<=C_gamma exp(gamma t). The Theta_k belong to that space by their full Gaussian tail.

Set h(u)=pi u^(5/4)(2pi u-3)exp(-pi u). The theta expansion and its inversion, absolutely convergent in H_gamma, are

    Theta_k(t)=sum_(n>=1)n^(-1/2)h(kn²t),
    h(kt)=sum_(n>=1)mu(n)n^(-1/2)Theta_(kn²)(t).

Norm convergence follows from the polynomial-times-exp(-c_gamma kn²) bounds for the norms of those summands; it also justifies regrouping the inversion via sum_(n|j)mu(n). Thus the closure of the theta span contains each h(kt).

For G smooth with compact support in [1,infinito), set g(t)=G(t)/(pi t^(5/4)) and

    L=-2t(d/dt)-3,
    P(t)=(1/2)t^(-3/2)integral_t^infinito s^(1/2)g(s)ds.

Then LP=g and P is smooth and zero for t sufficiently large. With x=exp(-pi t), Q(x)=P(t)/x is smooth on [0,exp(-pi)] and zero near 0. Approximating Q in C1 by polynomials Q_N gives

    pi t^(5/4)L[xQ_N(x)] -> G en H_gamma.

Each approximant is a FINITE combination of h(kt): for the monomial x^k, pi t^(5/4)Lx^k=k^(-5/4)h(kt), k>=1. The error is bounded by C eta_N t^(5/4)(1+t)exp(-pi t), with eta_N->0, integrable in H_gamma because gamma<2pi. Density of smooth compact functions completes the proof that the finite theta span is dense in H_gamma. This norm is not confused with the space B of BRIDGE002 nor with the compact map of phase199.

**Contradiction with real plateaus.** A bound |Q_C|<=M W valid on the theta span would extend by those two continuities to ALL of H_gamma. For R>1, the test F_R=1_[1,R] belongs to H_gamma and gives exactly

    Q_C(F_R)=(1/2)sum_(2<=m<=sqrt R)
                       Lambda(m)m^(-1/2)log(R/m²),
    W(F_R)=(1/2)log R+(1/4)(log R)².

For R large, restricting the nonnegative sum to m<=R^(1/4) gives Q_C(F_R)>=(log R/4)sum_(m<=R^(1/4))Lambda(m)/sqrt m. The elementary bound psi(X)>=cX for X large implies that this is >=c'R^(1/8)log R. That bound can be obtained without external data: for N=floor(X/2), psi(X)>=log binom(2N,N)>=2Nlog2-log(2N+1), comparing the prime valuations of the binomial with the prime powers up to 2N. Also sum_(m<=X)Lambda(m)/sqrt m>=psi(X)/sqrt X. Therefore Q_C(F_R)/W(F_R) tends to infinity.

The order is: fix R, approximate F_R in H_gamma by theta aggregates and pass the hypothetical inequality to the limit; AFTERWARDS let R tend to infinity. Uniform approximation in R is not needed nor is it claimed that F_R is already a finite aggregate. This refutes only this scalar logarithmic bound of the operator C on the declared theta carrier. It does not control the non-resonant remainder by R_res, does not prove A negative nor alter the target sign; it certifies no W/T window. No new route, campaigns, auxiliary files or changes to papers.

### 17.8. The conjugated resolvents are not all accretive in the physical metric

**PROVED, same date and entry.** Construction joint_sign_fresh_review; independent verification global_restart_checked, audit arithmetic_fresh_candidate PASS and second review PASS. Targeted cross-check in the three indices and corpus without this literal example located. Antecedents: [phase199 E§3, Rem3.1](../phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_E_001.md) and [phase188 N_BUILD_007](../phase-188-closing-D/N_BUILD_007_CONE_ORDER_ON_A_T.md)/[N_BUILD_018](../phase-188-closing-D/N_BUILD_018_LINEAR_CENTRE_REDUCES_TO_OMEGA_MU.md) treat comb operators, other kernels and cone orders; they do not prove accretivity of THIS conjugation in THIS metric. No general impossibility of resolvent methods is proposed.

On t>=1, set

    T=pi t^(5/4)[-2t(d/dt)-3], A0=-d/dt,
    (R_s f)(t)=integral_t^infinito exp[-s(u-t)]f(u)du, s>0,
    T^(-1)F(t)=(1/(2pi))t^(-3/2)
                           integral_t^infinito u^(-3/4)F(u)du,
    Rtilde_s=T R_s T^(-1).

The inverse is the solution with lim_(t->infinito) t^(3/2)P(t)=0, a condition that excludes the homogeneous solution P(t)=constante*t^(-3/2); the correct weight is u^(-3/4). The physical product integral f conjugado(g)dt/(2t) is used, not that of H_gamma. For f∈C_c^infinito((1,infinito)), integration by parts without boundaries gives exactly

    q=Re<T A0 f,Tf>_fis
      =(pi²/2)[7 integral_1^infinito t^(5/2)|f'|²dt
                      -(9/2)integral_1^infinito t^(1/2)|f|²dt].

With f(t)=t^(-3/4)u(log t), u smooth with compact support in (0,infinito), this is

    q=(pi²/2)[7 integral|u'|²dx-(9/16)integral|u|²dx].

Choosing a nonzero real bump u_R(x)=chi(x/R), chi∈C_c^infinito((1,2)), makes q<0 for R sufficiently large: the two integrals scale as R^(-1) and R. Then fix 0<s<-q/||Tf||_fis² and v=T(A0+s)f. The identity R_s(A0+s)f=f implies

    Rtilde_s v=Tf,
    Re<Rtilde_s v,v>_fis=q+s||Tf||_fis²<0.             (RES-NEG)

**Transfer to the finite theta span.** Density in a norm where the operator is discontinuous does not suffice. Use exactly the exponential H_gamma of §17.7, 0<gamma<2pi. The integral formula of the conjugation is

    Rtilde_s F(t)=t^(3/4)integral_t^infinito v^(-3/4)F(v)dv
      -(1/2)t^(5/4)(2st+3)
          *integral_t^infinito exp[-s(u-t)]u^(-3/2)
                       integral_u^infinito v^(-3/4)F(v)dv du.

It is obtained by substituting T^(-1) and differentiating R_s, first for smooth compact data, where all exchanges are absolute. The unitary conjugation U_gamma F(t)=exp(gamma t/2)t^(-1/2)F(t) takes H_gamma to L²(dt). With r=v-t>=0, the moduli of the transformed kernels of the two terms are bounded respectively by

    exp(-gamma r/2),
    (s+3/2)r exp(-gamma r/2).

For the second one uses integral_t^v exp[-s(u-t)]u^(-3/2)du<=r t^(-3/2), together with (t/v)^(1/4)<=1 and t>=1. The convolution bound by the L1 norm of those kernels gives

    ||Rtilde_s||_(H_gamma -> H_gamma)
        <=2/gamma+4(s+3/2)/gamma².

Thus the formula defines a bounded extension, which coincides with the conjugation also on smooth theta aggregates with exponential decay. Its physical quadratic form is continuous on H_gamma. Approximating the real v of (RES-NEG) by real FINITE theta aggregates, via the density of §17.7, preserves the strictly negative inequality. Therefore there also exists a finite theta aggregate with Re<Rtilde_s F,F>_fis<0; it is not claimed that v itself is already one of them.

**Scope.** Only the statement that ALL these Rtilde_s are accretive in the physical product on the declared carrier is refuted. The pertinent integral representation of the logarithm contains MINUS R_s; therefore (RES-NEG) is NOT a falsifier of positivity of the conjugated logarithm. It does not exclude the full resolvent method, another inner product nor a joint balance with C; it does not prove A negative, a control of the non-resonant term or the global sign. No new route, computations, auxiliary files, W/T coverage or changes to papers.


## 18. The full A on integer scales suffices for all real nodes

**PROVED, 2026-11-06.** Independent construction joint_sign_fresh_review, verification global_restart_checked; audit arithmetic_fresh_candidate PASS and second review PASS. Consulted the project rules, the three indices and corpus; targeted cross-check without this literal bridge located. [BRIDGE002§3](POWER_BRIDGE_002.md) already uses C1 polynomial approximation in an exponential variable; [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md) and [SCALAR_BRIDGE017](POWER_SCALAR_BRIDGE_017.md) transfer other rational families. The density of §17.7 controls F in H_gamma, but NOT by itself the second term G of the full form. Here the pair (F,G) is approximated simultaneously, using a two-derivative norm before applying the logarithmic operator and C. No novelty is attributed to the polynomial instrument nor to Möbius inversion.

**Statement.** For the real Phi, the following are equivalent:

1. A(.5log k,.5log l) is PSD for ALL finite blocks of positive integers k,l.
2. A(x,z) is PSD for ALL finite blocks of real nodes x,z.

The second statement implies the first by restriction. For the remaining direction the FULL A at y=0 is kept, including all pairs of different frequencies.

### 18.1. Graph identity for every positive scale

For t>=1 and kappa>0 define

    P_kappa(t)=kappa^(5/4)sum_(n>=1)n² exp(-pi kappa n²t),
    Theta_kappa(t)=Phi(.5log(kappa t)),
    T=pi t^(5/4)(-2tD-3),
    Lg P(t)=integral_0^infinito
                    [exp(-pi r)P(t)-P(t+r)]dr/r,
    F(P)=TP,   G(P)=(1/2)T Lg P-C TP,
    (CF)(t)=sum_(m>=2)Lambda(m)/sqrt(m) F(m²t).

Frullani on each exponential gives Lg[exp(-pi b t)]=log b exp(-pi b t). The series of P_kappa and their derivatives converge absolutely with Gaussian tails, also with factors log n. Therefore

    F(P_kappa)=Theta_kappa,
    G(P_kappa)=(1/2)log(kappa)Theta_kappa.           (GRAPH)

Indeed, the additional term of (1/2)T Lg P_kappa has coefficient log n in mode n. In C Theta_kappa the change n=mj produces exactly sum_(m|n)Lambda(m)=log n, which cancels it. No modes are suppressed nor is their sign estimated separately.

If P=sum_i c_i P_(kappa_i), x_i=.5log kappa_i, the change t=exp(2r) in A gives exactly

    sum_ij c_i conjugado(c_j) A(x_i,x_j)
      =integral_1^infinito
          [log t |F(P)|²+2Re(G(P)conjugado(F(P)))]dt/(2t).
                                                        (A-GRAPH)

### 18.2. Continuity preserving both terms

Fix a FINITE list of kappa_i>0 and choose

    0<a<pi min(1,min_i kappa_i),  0<gamma<2a,
    ||P||_(a,2)=max_(0<=j<=2) sup_(t>=1) exp(at)|P^(j)(t)|.

Split Lg into r<1 and r>=1. For j=0,1, the small numerator is at most r(pi+1)exp(-at)||P||_(a,2); the large one is dominated by exp(-at)[exp(-pi r)+exp(-ar)]||P||_(a,2). This justifies differentiating under the integral and proves

    ||Lg P||_(a,1)<=C_a||P||_(a,2),
    C_a=pi+1+exp(-pi)/pi+exp(-a)/a.

Thus |TP(t)|<=5pi t^(9/4)exp(-at)||P||_(a,2), and the same bound with factor C_a holds for T Lg P. The integral of t^(7/2)exp[-(2a-gamma)t] over [1,infinito) is finite. Together with C bounded on H_gamma=L²(exp(gamma t)dt/t) by §17.7, continuity results

    P en B_a² -> (F(P),G(P)) en H_gamma x H_gamma.

The weight 1+log t is dominated by a constant times exp(gamma t). Cauchy–Schwarz proves that the form on the right-hand side of (A-GRAPH) is continuous in that pair of norms. PSD of A is not presupposed.

### 18.3. Approximation by integer scales in the graph norm

Each target P=sum_i c_i P_(kappa_i) has exp(at)P^(j)(t)->0 for j=0,1,2. Cutting it off smoothly at large t approximates it in B_a²: the derivatives of the cutoff are controlled and the weighted tails tend to zero. This step is claimed for THESE targets, not for every element of B_a².

For the smooth cutoff P_c, set x=exp(-pi t) and Q(x)=P_c(t)/x. Q extends smoothly by zero near x=0 on [0,exp(-pi)]. Approximate Q in C² by polynomials Q_N: approximate Q'' uniformly and integrate twice adjusting Q(0),Q'(0). Then P_N(t)=x Q_N(x) is a FINITE combination of exp(-pi k t), k a positive integer, and

    |D^j(P_N-P_c)(t)|<=C eta_N exp(-pi t),
    j=0,1,2,  eta_N->0.

Since a<pi, there is B_a² convergence. To lift each exponential use the exact identity

    exp(-pi k t)=k^(-5/4)
          sum_(n>=1)mu(n)/sqrt(n) P_(kn²)(t).       (MOB-P)

On expanding P_(kn²), the coefficient of mode j is j² sum_(n|j)mu(n), which keeps only j=1. The series is ABSOLUTE in B_a², since for K>=1

    ||P_K||_(a,2)<=C_a' K^(13/4)exp(-pi K)

by the Gaussian bounds of the series of n²,n4,n6 and a<pi. Truncating (MOB-P) produces FINITE combinations of integer P_k. A successive selection of cutoff, polynomial and truncations gives P_l in the FINITE span of the integer P_k with P_l->P in B_a². In particular F(P_l),G(P_l) converge simultaneously in H_gamma.

### 18.4. Transfer of the inequality and scope

Under hypothesis 1, the form (A-GRAPH) is nonnegative for each integer P_l. By continuity it is so for any finite list of kappa_i>0 and complex coefficients. Since x_i=.5log kappa_i ranges over ALL of R, 2 is proved.

Thus no additional transfer gate remains between the FULL A on all integers and the global real A. Combined with §2 and the K bridges of [CONE001](POWER_CONE_001.md)/[BRIDGE002](POWER_BRIDGE_002.md), proving that full integer sign is sufficient for the declared target; the converse for the target lambda_A(T)>=0 for ALL T is verified later in §18.9; no minimum at fixed T is identified. The SOS of §17 only signs R_res: the joint control of the non-resonant part, or directly the full integer sign, remains OPEN. R_res is not transferred separately nor is a new W/T window, global positivity or change to papers obtained.


### 18.5. The conjugation T does not preserve positive jump rates

**PROVED, specific scope.** joint_sign_fresh_review, independent verification global_restart_checked; audit arithmetic_fresh_candidate PASS and second review PASS. Cross-checked the three indices and [106_31](../phase-106-global-modular-star-audit/106_31_FULL_KERNEL_DOOB_VARIANCE_IDENTITY.md), [ROUND005D](ROUND_005_D.md) and [L2_BUILD008](../phase-188-closing-D/L2_BUILD_008_GROUND_STATE_AND_T0.md): these treat other forms, ground-state transformations and metrics, without this conjugation T nor the following kernel. The literal statement was not found in that cross-check.

Write D_(m²)P(t)=P(m²t) and

    B=Lg-2sum_(m>=2)Lambda(m)m² D_(m²),  p=P_1>0.

By the same modal identity sum_(m|n)Lambda(m)=log n of (GRAPH), Bp=0. For P=pf with f smooth with compact support in [1,infinito), without requiring f(1)=0, before applying T there is the exact positive-rate identity

    B(pf)(t)=integral_0^infinito
                    p(t+r)[f(t)-f(t+r)]dr/r
       +2sum_(m>=2)Lambda(m)m²p(m²t)[f(t)-f(m²t)].

This does not ensure its preservation after the differential conjugation. Define U_rP(t)=P(t+r). Substituting the weighted terminal inverse of §17.8 and differentiating gives

    (T U_r T^-1 F)(t)=(t/(t+r))^(9/4)F(t+r)
       -(3/2)r t^(5/4)(t+r)^(-5/2)
                         integral_(t+r)^infinito v^(-3/4)F(v)dv.

For smooth F with support separated from t, the local term of Lg does not contribute and the exchanges are absolute. Integrating the second term in r, using

    (3/2)integral_0^(v-t)(t+r)^(-5/2)dr
                       =t^(-3/2)-v^(-3/2),

and combining it with the translation produces the kernel with respect to dv

    (T Lg T^-1 F)(t)=integral_t^infinito K(t,v)F(v)dv,
    K(t,v)=t^(-1/4)v^(-3/4)
                    -t^(5/4)v^(-5/4)/(v-t).        (JUMP-K)

This formula is used only for separated supports, without imposing a diagonal renormalization. With w=v/t,

    K(t,v)=t^-1 w^(-5/4)[sqrt(w)-1/(w-1)]>0
                       cuando 2<w<3.

Moreover T[m²D_(m²)]T^-1=m^(-1/2)D_(m²), hence TBT^-1=T Lg T^-1-2C. Choose t0=2 and F>=0 smooth nonzero, with compact support in (9/2,11/2). Then F is zero near 2 and CF(2)=0, since 2m²>=8 for m>=2. By (JUMP-K),

    (TBT^-1F)(2)=integral_(9/2)^(11/2)K(2,v)F(v)dv>0.

Fix the convention of the representation being refuted:

    (JF)(t)=integral[F(t)-F(v)]nu_t(dv)+V(t)F(t),
    nu_t>=0,

with V local finite. For this test F(2)=0, any operator of that class satisfies JF(2)<=0; local killing does not change that value. Therefore TBT^-1 does NOT admit that positive-rate representation on the declared smooth carrier. Conjugating moreover by Theta_1(t)=Phi(.5log t)>0 does not change the off-diagonal sign either: use the test F/Theta_1. Everything is kept on t>=1; the lower boundary is not eliminated.

**Scope.** Only the shortcut of preserving positive rates AFTER T (also after that positive conjugation) fails. Negativity of the quadratic form Q or A is not proved, nor an impossibility for every Doob transformation, another metric or the joint treatment of the operator. The full integer sign and, by §18, the global real sign remain OPEN. No new route, campaigns, auxiliary files, W/T window or changes to papers.


### 18.6. The complex boundary of §16 does not give a direct minimum principle

**PROVED, specific scope.** Proposal, independent verifications global_restart_checked/arithmetic_fresh_candidate PASS and second review PASS. Read the three indices, §§2.2,16 and [OUTER088](POWER_THETA_DENSITY_OUTER_088.md); targeted cross-check without a resolved literal transport located. For fixed real shifts x_i, set

    A_ij(x,y)=integral_x^infinito w_ij(s)P_ij(s,y)ds,
    w_ij(s)=x_i+x_j+2s,
    P_ij(s,y)=Phi(x_i+s+iy)conjugado(Phi(x_j+s+iy)).

In |y|<pi/4, the supertails allow all differentiations and eliminate the boundaries at infinity. With Delta=partial_x²+partial_y², integrating by parts keeping the lower boundary gives exactly

    Delta A_ij(x,y)
      =4integral_x^infinito w_ij(s)
          Phi'(x_i+s+iy)conjugado(Phi'(x_j+s+iy))ds
         -4P_ij(x,y).                              (PDE-A)

No matrix sign is assigned to this source. What is refuted is the superharmonicity required by a direct minimum principle: take x_i=x_j=0,y=0,x>=1. Write Y(s)=pi exp(2s), p(s)=-Phi'(s)/Phi(s). The first-mode formula and the full-tail bounds of 088 give p(s)>2Y(s)-6>Y(s) for s>=1 (Y>21). Therefore

    I=integral_x^infinito 2s p(s)²Phi(s)²ds
      >Y(x)integral_x^infinito 2s p(s)Phi(s)²ds
      =Y(x)[xPhi(x)²+integral_x^infinito Phi(s)²ds]
      >Phi(x)².

Here (Phi²)'=-2pPhi² was used, with the boundary xPhi(x)² retained and the tail at infinity zero; xY(x)>1. Thus Delta A_ii(x,0)=4[I-Phi(x)²]>0. The diagonal function is neither harmonic nor superharmonic on that domain, and the positivity near y=pi/4 of §16 cannot be transported to y=0 via that minimum principle without another estimate.

**Scope.** The threshold of §16 depends on each fixed block; it does not by itself provide joint PSD on an open real interval, which is the hypothesis of the continuation of §2.2. This identity and this test do not prove an indefinite matrix source, Q/A negative nor an impossibility for every PDE or other transport. Only the superharmonicity premise of the declared shortcut fails; global joint sign OPEN. No new route, computations, auxiliary files, W/T or papers.


### 18.7. Every integer tail suffices; no finite observable sustains a positive margin

**PROVED, extension of the bridge.** joint_sign_fresh_review, independent verification global_restart_checked; audit arithmetic_fresh_candidate PASS and second review PASS. Consulted the three indices, §18.3 and [DESCENT_AUDIT016§§8–9](POWER_DESCENT_AUDIT_016.md), in addition to [BRIDGE002§3](POWER_BRIDGE_002.md). Antecedent 016 already proves density of each tail of another rational family and the insufficiency of the sign of its diagonals for W4; here the exact carrier P_k, the norm of the full graph of A and the conclusion about minorants change. No novelty is attributed to the abstract mechanism of dense tails.

Fix an integer K>=1. For the targets P=sum_i c_i P_(kappa_i) and the parameters a,gamma of §18.2, §18.3 can be carried out using ONLY indices k>=K. After the cutoff P_c, write

    x=exp(-pi t),  Q(x)=P_c(t)/x^K.

Q is smooth and zero near x=0. Approximating it in C² by polynomials Q_N gives x^KQ_N(x), a finite combination of exp(-pi k t) with k>=K, and derivative errors of orders 0,1,2 bounded by C_K eta_N exp(-pi Kt). Since a<pi<=pi K, they converge in B_a². The inversion (MOB-P) only introduces indices kn²>=K and is still absolute in that norm. Therefore span{P_k:k>=K} approximates each target of §18 in B_a² and in the graph (F,G). Density of compacts in all of B_a² or uniformity of the constants in K is not claimed.

In particular, PSD of ALL blocks of ANY fixed tail k>=K is equivalent to PSD of the global real A, by the same continuity step of §18.4. This keeps the obligation on ALL sizes, not only the late diagonals.

**Completing a prefix with energy tending to zero.** Abbreviate A_0[c]=sum_kl c_k conjugado(c_l)A(.5log k,.5log l), with finite support. Fix J and any c_1,...,c_J. Apply the density of the tail k>J to the target -sum_(k<=J)c_k P_k. One obtains completions c^(n), all of finite support, with that SAME prefix, such that

    sum_k c_k^(n)P_k ->0 en B_a²,
    A_0[c^(n)] ->0.                                (TAIL-ZERO)

PSD is not presupposed for this convergence. If A_0 were PSD, the infimum over the completions of each prefix would be exactly 0; without that hypothesis no sign is assigned to that infimum.

If ell is any nonzero FINITELY supported linear functional on the coefficients, choose J containing its support and a prefix with ell(c)=1. The tails do not alter it. By (TAIL-ZERO), it is impossible that

    A_0[c]>=delta |ell(c)|² for all finite c,
    con delta>0.                                   (NO-FIN-MARGIN)

Consequently, there is no nontrivial minorant sum_k w_k|c_k|² with ALL w_k>=0 and some strictly positive either, even if the weights decay arbitrarily. The same reason excludes diagonal minorants with NONNEGATIVE weights on the finitely-dependent divisorial observables of §17: f_(d,q) only uses indices d a²<=dq², a|q. It suffices to fix a prefix making nonzero an observable whose weight is positive. Those f_(d,q) are not identified with other coordinates d_lambda; their finite dependence suffices.

As a corollary of the same (NO-FIN-MARGIN), a SINGLE identity compatible for ALL supports is excluded

    A_0[c]=sum_alpha w_alpha|ell_alpha(c)|²,
    w_alpha>=0,

with some nonzero summand and ALL ell_alpha of finite support, even if their sizes have no uniform bound: each positive summand would by itself be the already forbidden minorant. This does NOT exclude factorizing each finite principal block separately; those factorizations do not constitute the single identity on the whole carrier. [FIXED_BLOCK_ASSEMBLY](POWER_FIXED_BLOCK_ASSEMBLY_OBSTRUCTION.md) already excludes assemblies of uniformly bounded sizes for another kernel; here the obstruction affects any fixed local observable of this global identity.

**Scope.** Result for the FULL A at y=0, not an automatic extension to all complex y. It refutes positive margins on finitely supported observables and their nonnegative diagonal energies; it does not exclude energies of continuous global observables nor non-diagonal sums of squares preserving them. It does not prove A negative nor the global sign, which remains OPEN. No new route, computations, auxiliary files, W/T or changes to papers.


### 18.8. No individual real exponential moment gives a positive minorant

**PROVED, specific corollary.** joint_sign_fresh_review, independent verification global_restart_checked; audit arithmetic_fresh_candidate PASS and second review PASS. Cross-checked the three indices, §§8.4,18, [BRIDGE002](POWER_BRIDGE_002.md), [106_31](../phase-106-global-modular-star-audit/106_31_FULL_KERNEL_DOOB_VARIANCE_IDENTITY.md), [ROUND005D](ROUND_005_D.md) and [106_36](../phase-106-global-modular-star-audit/106_36_JOINT_COMPLEMENT_AND_EXPANDER_GATE.md), without this literal statement located. The earlier capacity/variance and continuity identities have other objects; §8.4 alters the density and cancels a moment, while here the exact Phi is kept and a rank-one minorant is refuted.

For fixed REAL sigma and finite coefficients define

    ell_sigma(c)=integral_0^infinito exp(sigma u)
                     sum_k c_k Phi(.5log k+u)du
                =(1/2)integral_1^infinito F(t)t^(sigma/2)dt/t.

This functional is continuous on H_gamma for all gamma>0, since Cauchy–Schwarz gives

    |ell_sigma(F)|²<=(1/4)||F||_(H_gamma)²
                         integral_1^infinito t^(sigma-1)exp(-gamma t)dt,

with finite integral. If A_0[c]>=delta|ell_sigma(c)|² for ALL finite c and some delta>0, the graph approximation of §18 would also preserve ell_sigma, transferring the inequality to any real node x. Take x=-R, define F_x(t)=Phi(x+.5log t)=Theta_(exp(2x))(t), and use the positive parity of Phi:

    A(-R,-R)=d(R)=2integral_R^infinito sPhi(s)²ds,
    ell_sigma(F_(-R))
       =exp(sigma R)integral_(-R)^infinito exp(sigma s)Phi(s)ds
       ~Z_sigma exp(sigma R),
    Z_sigma=integral_(-infinito)^infinito exp(sigma s)Phi(s)ds>0.

The supertails of Phi give d(R)exp(CR)->0 for ALL fixed real C. Hence

    A(-R,-R)/|ell_sigma(F_(-R))|² ->0,

contradicting any delta>0. This holds even for sigma<0, when the moment of the node also tends to 0: d(R) decreases faster than any exponential.

**Scope.** Only positive minorants by an individual REAL exponential moment of the exact carrier are excluded. General signed moments, combinations with cancellations or distinct global observables are not excluded, nor is A proved negative. No result is claimed for complex sigma nor a spectral test. Global sign OPEN, no new route, computations, auxiliary files, W/T or papers.


### 18.9. Equivalence of the target for all windows and exact primitive constraints

**PROVED as scope, not as sign.** joint_sign_fresh_review, independent verification global_restart_checked; audit arithmetic_fresh_candidate PASS and second review PASS. Reread the project rules, the three indices, the definitions eq:form, eq:W and eq:target of [Paper46](../../04-papers/46-row-d-sign-radial-intersection-form/main.tex), [BRIDGE002](POWER_BRIDGE_002.md), [CONFLUENT_BRIDGE014§3](POWER_CONFLUENT_BRIDGE_014.md) and the lemma ALREADY proved in [GLOBAL, Primitive comparisons](POWER_GLOBAL_ROUTE_REVIEW.md). The new scope is applying that lemma to D=M_Phi itself and verifying the step from the primitive windows to their causal mixtures; no new analytic principle nor a positivity proof is presented.

The following global targets are equivalent:

1. lambda_A(T)>=0 for ALL T>0, with the two Tate moments and the logarithmic domain declared in Paper46.
2. K_(M_Phi)(u,v)=[M_Phi(u)+M_Phi(v)]/(u+v) is PSD in all sizes.
3. A is PSD on all real nodes.
4. A(.5log k,.5log l) is PSD on all blocks of positive integers; equivalently, on all blocks of any fixed tail of these.

The equivalences 2–3 and 3–4 are §§2.1,18,18.7. The implication 2=>1 is the sufficiency of CONE001/BRIDGE002, keeping the full form before restricting to the primitive subspace.

**Converse 1=>2 without changing the problem.** Use the causal mixture

    f(r)=sum_i d_i exp(-u_i r),  r>=0, u_i>1/2,
    sum_i d_i/(u_i-1/2)=sum_i d_i/(u_i+1/2)=0.

This is the causal physical function entering W, not an automatic identification with the exterior datum h=Zrho of another convention. Choose 1/2<eta<min_i u_i. Cutting f off smoothly only at infinity converges in H_eta of 014. The two moment errors tend to 0. Choose two fixed smooth bumps interior to the half-line, with invertible moment matrix exp(±r/2), and correct those errors via coefficients tending to 0. One obtains compact causal functions f_R, EXACTLY primitive and converging to f in H_eta.

f_R(0)=0 is not required. The extension by zero of H¹ on the half-line belongs continuously to H^s(R) for 0<s<1/2, even with that jump, and hence to the logarithmic domain of Paper46. Translating each compact support inside some I_T preserves the two vanishing moments and W; on primitives W=a_T. Hypothesis 1 gives W[f_R]>=0. Continuity 014 allows passing to the limit: W[f]>=0.

The identity CONE001 is W[f]=sum_ij d_i conjugado(d_j)K_(M_Phi)(u_i,u_j). Hence PSD of K has been proved on ALL blocks subject to those two constraints. M_Phi=Z'/Z is odd and real-analytic on all of R because Phi is even and Z is strictly positive on R. Applying the lemma of GLOBAL with c=1/2,D=M_Phi: congruence by u²-c², two anchors, analytic continuation and null rows at ±c turn that restricted positivity into full PSD. This proves 1=>2.

**The constraints in the graph P are two conditions, not three.** For any P of the carrier of §18, integration by parts with vanishing tail gives exactly

    ell_sigma(TP)=pi P(1)
       +pi(sigma/2-1/4)integral_1^infinito
                                      t^(sigma/2+1/4)P(t)dt.

Here ell_sigma is the physical moment of §18.8. In particular

    ell_(1/2)(TP)=pi P(1),
    ell_(-1/2)(TP)=pi P(1)-(pi/2)integral_1^infinito P(t)dt.

Thus the two Tate moments are EXACTLY equivalent to P(1)=0 and integral_1^infinito P=0. They do NOT impose P'(1)=0. The preimage of L2_BUILD008 is another transformation; its boundary conditions are not imported to T.

**Primitive completions with arbitrary prefix.** The result (TAIL-ZERO) of §18.7 remains valid if EACH completion is required to be exactly primitive. To see it, the map of the two moments has rank 2 on smooth compact P in [1,infinito): a bump touching 1 with P(1)!=0 and another interior one with nonzero integral give rank 2 by the preceding formula. Two only-interior bumps would not work, since both would have P(1)=0.

The density proof for each tail of §18.7 also approximates those two compacts directly. The moments are continuous in B_a², so two FIXED finitely supported vectors in the tail can be chosen whose moment matrix is invertible. Approximate -P_prefijo by that tail; the two moments of the total tend to 0. Correcting them with those two fixed vectors and coefficients tending to 0 imposes both moments EXACTLY without changing the prefix nor the graph convergence to 0. By continuity, A_0 of the completions tends to 0.

Consequently, the exclusion of finitely supported minorants and compatible local SOS of §18.7 remains valid on the primitive subspace. In contrast §18.8 for sigma=±1/2 is vacuous there because those moments are zero; for other sigma its non-primitive falsifier does NOT transfer automatically.

**Scope.** All the preceding equivalences include the quantifier FOR ALL T and all sizes. They do not identify full/primitive minima nor forms of a fixed window T. They are internal equivalences of the declared explicit problem; no external statement is used nor is the sign of any of the equivalent targets proved. Global OPEN; no new W/T window, computations, auxiliary files or changes to papers.


## 19. First primitive thermal polynomial: full sign of a fixed vector

**PROVED, 2026-11-06.** Construction fresh_global; independent mathematical audit arithmetic_fresh_candidate FULLPASS and verification of the factors, the tail partition and the parameter correction. Consulted the project rules, README of ROUTES-TRIED-INDEX, master grid and crossword; targeted corpus cross-check without the following literal family located. Antecedents: the full graph of §18, its exact primitive constraints of §18.9 and the rate identity before T of §18.5. E101_061 treats nodal interpolation polynomials, not these polynomials in the thermal time. The previous physical gamma/Laguerre families and the exponential tilts are not this family.

The concrete difference is keeping p=P_1 EXACT and multiplying it by a real polynomial in t, where t=exp(2r), allowing both signs. The theta density is not truncated to define the vector. Only the first primitive vector of that family is signed; this sign computation does not claim a positive recurrence among its degrees. Sufficient density of the family is proved separately in §19.8; it is not deduced from the sign of this vector. The following estimates keep all theta and prime contributions via bounds of their infinite tails. The proof does not need a decimal value of the form.

### 19.1. Vector, parameters and exact constraints

For t>=1 set

    p(t)=sum_(n>=1) n² exp(-pi n²t),
    S_j=sum_(n>=1) n^(-j)exp(-pi n²),
    a=1+(2/pi)S_4/S_2,
    R(t)=(t-1)(t-a),   P(t)=p(t)R(t).

These are full series, absolutely convergent with all the derivatives used. Integrating each exponential gives

    integral_1^infinito (t-1)p(t)dt=pi^(-2)S_2,
    integral_1^infinito t(t-1)p(t)dt
         =pi^(-2)S_2+2pi^(-3)S_4.

Thus a is exactly the mean of t for the positive weight w(t)=(t-1)p(t), and a>1. The polynomial t-a is the first nonconstant orthogonal polynomial for that weight. One has

    P(1)=0,   integral_1^infinito P(t)dt=0.

By §18.9, these are precisely the two Tate moments of F=TP; P'(1)=0 is not added. The function P and its derivatives have exponential decay, so they belong to the graph domains used here.

Use, as in §18,

    T=pi t^(5/4)(-2tD-3),
    B=Lg-2sum_(m>=2)Lambda(m)m²D_(m²),
    Q(P)=integral_1^infinito
           [log(t)|TP(t)|²+Re(TBP(t)conjugado(TP(t)))]dt/(2t)
         =Q_log(P)+Q_B(P).

The identity Bp=0 preserves the full arithmetic cancellation. Moreover Q_log(P)>=0, simply because t>=1. It will be proved that Q_B(P)>1/2000.

### 19.2. Exact expansion of B and modal normalization

For j=1,2 define

    D_j(n)=sum_(m|n,m>=2)Lambda(m)(m^(2j)-1).

In particular D_j(1)=0 and

    0<=D_j(n)<=n^(2j)log n,

by sum_(m|n)Lambda(m)=log n. Applying §18.5 to R, or expanding the differences R(t)-R(t+r) and R(t)-R(m²t), gives exactly

    BP=(a+1-2t)U_1-U_2+2(a+1)tV_1-2t²V_2,
    U_1=pi^(-1)sum_n exp(-pi n²t),
    U_2=pi^(-2)sum_n n^(-2)exp(-pi n²t),
    V_j=sum_n n²D_j(n)exp(-pi n²t).

The formula for V_j keeps all divisor pairs: reindexing n=mk in the initial sum over m and k produces the factor n²D_j(n). Equivalently,

    BP(t)=sum_(n>=1)exp(-pi n²t)L_n(t),
    L_n(t)=(a+1-2t)/pi-1/(pi²n²)
             +2n²(a+1)tD_1(n)-2n²t²D_2(n).

Set

    H_n=(2pi n²t-3)R-2tR',
    J_n=(2pi n²t-3)L_n-2tL_n'.

Then the two expansions, with their distinct factors, are

    TP=pi t^(5/4)sum_n n²exp(-pi n²t)H_n,
    TBP=pi t^(5/4)sum_n exp(-pi n²t)J_n.

Therefore

    Q_B(P)=(pi²/2)sum_(n,m>=1)n²
        integral_1^infinito t^(3/2)exp[-pi(n²+m²)t]H_n(t)J_m(t)dt.
                                                        (POLY-QB)

No second factor m² is introduced in J_m. The polynomial bounds of D_j and the exponentials absolutely justify this double series, the differentiations and the following integrations.

### 19.3. The leading mode and an elementary lower bound

Write a_0=1+2/pi. First evaluate only the term (n,m)=(1,1) of (POLY-QB) at a=a_0, denoted Q_(B,11)(a_0). With x=t-1 one obtains

    H_1=2pi x³+(2pi-11)x²+(10/pi-8)x+4/pi,
    J_1=-4x²+(12/pi-4)x+6/pi-3/pi².

For I_r=integral_1^infinito t^(r+3/2)exp(-2pi t)dt, integration by parts gives

    I_r=exp(-2pi)/(2pi)+(r+3/2)I_(r-1)/(2pi), r>=1.

Expanding H_1J_1 and applying this recurrence up to r=5 produces the exact identity

    Q_(B,11)(a_0)=(pi²/2)[A I_0-B_0 exp(-2pi)],
    A=(4pi-3)(176pi²-88pi+445)/(128pi⁴)>0,
    B_0=(176pi²-344pi+267)/(64pi⁴).

Convexity of (1+x)^(3/2) gives I_0/exp(-2pi)>=1/(2pi)+3/(8pi²). Consequently

    [A I_0-B_0 exp(-2pi)]/exp(-2pi)
      >=(4096pi³+1264pi²+792pi-4005)/(1024pi⁶)
      >120339/1024000.

Here 3<pi<22/7 and (22/7)^6<1000 suffice. Also exp(2pi)<600: the elementary bounds exp(1)<11/4 and

    exp(2/7)<=1+2/7+(2/7)²/[2(1-(2/7)/3)]<4/3

give exp(2pi)<(11/4)^6(4/3)<600, since 2pi<44/7. The written exponential bound follows from k!>=2*3^(k-2) for k>=2. One concludes

    Q_(B,11)(a_0)>(9/2)*120339/(1024000*600)>1/1200.
                                                        (POLY-11)

### 19.4. Correction of the exact parameter a

Let delta=a-a_0. The definition via S_4/S_2 implies delta<0 and

    |delta|<=(2/pi)sum_(n>=2)n^(-2)exp[-pi(n²-1)]
       <exp(-9)/[6(1-exp(-15))]<1/40000.             (POLY-A)

One used n²-1>=3+5(n-2), pi>3 and exp(3)>20. This last inequality already results from summing the series of exp(3) up to degree 8. In particular

    163/100<a<a_0<5/3.

For ALL parameters between a and a_0, the first-mode polynomials satisfy, on t>=1,

    |H_1|<=7t³, |J_1|<=4t²,
    |partial_a H_1|<=7t², |partial_a J_1|<=2t.

Indeed partial_a H_1=-(2pi t-3)(t-1)+2t and partial_a J_1=2t-3/pi; the other bounds follow directly from 1<a<2 and 3<pi<22/7. Differentiating the integral of the leading mode, absolutely convergent, gives

    |partial_a Q_(B,11)|
       <=210 integral_1^infinito t^(11/2)exp(-6t)dt
       <210exp(-6)<21/40<1.

For the intermediate inequality, t^(11/2)<=t^6 and finite integration by parts gives

    integral_1^infinito t^6exp(-6t)dt
      =exp(-6)sum_(k=0)^6 6!/[(6-k)!6^(k+1)]<exp(-6).

By (POLY-A),

    |Q_(B,11)(a)-Q_(B,11)(a_0)|<1/40000.          (POLY-AERR)

### 19.5. The two crossings between modes 1 and 2

In the following table [b_0,...,b_d] means that the modulus of the polynomial in x=t-1>=0 is at most sum_j b_jx^j. ALL bounds are for the EXACT parameter a of (POLY-A), not only for a_0:

| Polynomial | Coefficients of the absolute majorant |
| --- | --- |
| H_1 | [4/3,5,5,44/7] |
| J_1 | [2,1/5,4] |
| H_2 | [4/3,20,5/2,176/7] |
| J_2 | [660,3210,4670,2112] |

To verify H_n, with alpha=a-1, its coefficients in x are

    [2alpha, -2pi n²alpha+5alpha-4,
                    2pi n²(1-alpha)-7, 2pi n²].

For J_1 they are

    [6/pi-3/pi²+delta(2-3/pi), 12/pi-4+2delta, -4].

The bounds of (POLY-A), 63/100<alpha<2/3 and 3<pi<22/7 prove the first three rows. For the fourth, D_1(2)=3log2 and D_2(2)=15log2, so that

    L_2(t)=(a+1-2t)/pi-1/(4pi²)
                   +24(a+1)log2*t-120log2*t².

If L_2=l_0+l_1x+l_2x², the inequalities 2/3<log2<7/10 give

    37<-l_0<40, 117<-l_1<125, 80<-l_2<84.

The coefficients j_k of J_2 are exactly

    j_0=(8pi-3)l_0-2l_1,
    j_1=8pi l_0+(8pi-5)l_1-4l_2,
    j_2=8pi l_1+(8pi-7)l_2,
    j_3=8pi l_2.

Those intervals show that all are negative and their moduli are smaller than the four numbers of the table.

Denote by H_i^+,J_i^+ the majorant polynomials of the table and set

    V(x)=[H_1^+(x)J_2^+(x)+4H_2^+(x)J_1^+(x)]
                         *(1+3x/2+3x²/8).

The factor 4 is the n² of the mode n=2 in TP. The negative third derivative of (1+x)^(3/2) proves

    (1+x)^(3/2)<=1+3x/2+3x²/8, x>=0.

The preceding rational polynomial product satisfies, exactly,

    sum_j [x^j]V *j!/15^(j+1)
       =92107822417/664453125<139.

Integrating x^jexp(-15x) then gives, using pi²/2<5, 5pi>15 and exp(3)>20,

    |Q_(B,12)+Q_(B,21)|
       <5*139/20^5<1/4500.                         (POLY-12)

No sign is assigned to either of those crossings; their full cost is kept.

### 19.6. Remainder of the infinite double series

From D_j(n)<=n^(2j)log n, a<5/3 and t>=1 one obtains for n>=2

    |L_n(t)|<=4n^6log(n)t²,
    |L_n'(t)|<=6n^6log(n)t,
    |J_n(t)|<=32n^8log(n)t³.

For example, the terms of L_n are bounded by (2/3)t+6n^4log(n)t+2n^6log(n)t²; on dividing by n^6log(n)t², one uses n>=2 and log n>2/3. The derivative is treated similarly. Moreover |R|<=t(t-1), |R'|<=2t and 2pi n²>4 give |H_n|<=2pi n²t³ for all n>=1. Therefore the summands F_n of TP and Z_n of TBP satisfy

    |F_n(t)|<=22n^4t^(17/4)exp(-pi n²t), n>=1,
    |Z_n(t)|<=101n^8log(n)t^(17/4)exp(-pi n²t), n>=2,
    |Z_1(t)|<=13t^(17/4)exp(-pi t).

The last bound uses |J_1|<=4t². These are bounds of the full series, not of a numerically chosen cutoff.

For N>=2 and d<=9, the ratio between consecutive terms of n^dexp(-3n²) is less than

    (3/2)^9/20^5<1/1000.

Thus

    sum_(n>=N)n^dexp(-3n²)
       <(101/100)N^dexp(-3N²).                    (POLY-TAIL)

For an integer h>=8,

    integral_1^infinito t^(15/2)exp(-pi h t)dt
       <=exp(-pi h)/(pi h-15/2),

by log t<=t-1. The denominator is greater than 22 if h>=10 and greater than 16 if h>=8. Now separate the remaining pairs of (POLY-QB) into n=1,m>=3; n>=3,m=1; and n,m>=2. Use log n<=n and (POLY-TAIL), with exp(3)>20. The total absolute cost is less than or equal to

    (1111/22)(101/100)*3^9/20^10
       +(143/22)(101/100)*3^4/20^10
       +(1111/16)(101/100)²*2^13/20^8
     =11655533623/512000000000000<1/30000.          (POLY-REST)

The factors 1111=22*101/2 and 143=22*13/2 include the measure dt/(2t). The last product includes ALL pairs n,m>=2, in particular the pair (2,2); it omits no crossings between large modes. The three classes, together with (1,1),(1,2),(2,1), partition the whole double series.

### 19.7. Sign and scope

Combining (POLY-11), (POLY-AERR), (POLY-12) and (POLY-REST) gives

    Q_B(P)>1/1200-1/40000-1/4500-1/30000
            =199/360000>1/2000.

Since Q_log(P)>=0,

    Q(P)>1/2000.                                  (POLY-POS)

THIS exact primitive vector is signed, with all arithmetic and theta contributions kept. The leading mode was only used as the reference term of a bound with full tail; it was not claimed to be a PSD approximant in all orders. The auxiliary rational checks of the coefficients and finite sums above were reproduced in the audit; no decimal quadrature enters the proof.

The case corresponds to the first nonconstant orthogonal polynomial for w=(t-1)p. It does not prove that the result is preserved for higher degrees, arbitrary combinations of those polynomials, or their crossings. The computation (POLY-POS) also does not by itself prove a core property, a recurrence, a new K minor of fixed order, a W/T window nor the global sign of Paper46. The sufficient density property is verified independently in §19.8, without inheriting sign in higher degrees. No paper has been modified nor has an ideas or computation file been created.


### 19.8. The polynomials times p are a sufficient core; all their primitive blocks are equivalent to the global target

**PROVED as density and scope, not as sign of the family.** Independent constructions fresh_global; independent audit global_restart_checked PASS of the norm continuation, the primitive correction and both physical links. Consulted the project rules, the three indices, [BRIDGE002§3](POWER_BRIDGE_002.md), [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md), [DESCENT_AUDIT016§§8–9](POWER_DESCENT_AUDIT_016.md) and §18. Targeted cross-check without this literal family/core located. Polynomial approximation and strong density have explicit antecedents; what changes is the carrier p(t)R(t) with exact p=P1 and the simultaneous control of the graph (F,G), not just a physical L² norm. No worldwide priority is attributed.

**Continuation in B_a² without functional separation.** Fix 0<a<pi and let V be the COMPLEX closure of span{p(t)t^j:j>=0} in B_a² of §18.2. For r=0,1,2, the full theta series give |p^(r)(t)|<=C_r exp(-pi t), t>=1: after removing exp(-pi t), the remaining sums are dominated by sum_n n^(2+2r)exp[-pi(n²-1)]. Define

    H(z)(t)=p(t)exp(zt), Re z<pi-a.

For a centre z0 of that half-plane, set b=pi-a-Re z0>0. Differentiating in t up to order 2, and using

    sup_(t>=1) exp(-bt)t^j/j! <= b^(-j),

one obtains for ALL j>=0

    ||p exp(z0t)t^j/j!||_(a,2)
                         <=C_(z0)(1+b)² b^(-j).

Indeed each derivative of t^j/j! is t^(j-r)/(j-r)!; the terms with r>j disappear. Therefore the Taylor series of H at z0 converges in B_a² for |z-z0|<b and coincides with p exp(zt), also after two temporal derivatives. At z0=0 its coefficients are in V; thus H(z) belongs to V for |z|<pi-a.

If a real interval of parameters already has H(z) in V, its derivatives of any order at an interior centre also belong to V by finite differences and closure. The Taylor series at that centre extends membership to the disc of radius pi-a-z0. Successive negative real centres, separated by (pi-a)/2, give by overlapping discs

    p(t)exp(-nu t) pertenece a V for EVERY nu>0.

Hahn–Banach is not used nor is density inferred from pointwise convergence.

**Compacts and declared targets.** For P_c smooth with compact support in [1,infinito), set x=exp(-t) and Q(x)=P_c(t)/(p(t)x). Since p>0 and P_c vanishes for large t, Q is smooth on [0,exp(-1)] and zero near 0. Approximate Q in C² by polynomials Q_N. The functions p x Q_N(x) are finite combinations of p exp(-nu t), nu positive integers, and belong to V. For temporal derivatives of orders 0,1,2, the error is bounded by C eta_N exp[-(pi+1)t], eta_N->0. Thus P_c belongs to V. Each finite target of §18 has its weighted jets tending to 0 and is approximated by such cutoffs; by closure it belongs to V and admits FINITE approximants pR in B_a². This is not claimed for all of B_a²: in particular, density of compacts is not assumed when the weighted jets do not tend to 0.

The continuity of §18.2 turns this approximation into simultaneous convergence of F=TP and G=.5T LgP-C TP in H_gamma for 0<gamma<2a, and hence of the full Q.

**Exact correction of the two moments.** For a primitive target P, the conditions are P(1)=integralP=0 by §18.9. The approximants pR_n have errors tending to 0 in both continuous functionals of B_a². Correct them via two FIXED vectors p and tp: the matrix of the functionals (P(1),integralP) has determinant

    p(1)[integral_1^infinito t p(t)dt
                              -integral_1^infinito p(t)dt]>0.

Their correction coefficients tend to 0. EXACT primitive approximants pR_n remain without losing the graph convergence. Since p(1)>0, their polynomials are exactly

    R_n(t)=(t-1)S_n(t),
    integral_1^infinito w(t)S_n(t)dt=0,
    w(t)=(t-1)p(t)>0 for t>1.

All moments of w are finite and its moment matrix is positive definite on each degree. Let q_j be its monic orthogonal polynomials, with q_0=1. Then every S with vanishing integral against w is a FINITE combination of the q_j,j>=1. The primitive polynomial carrier is precisely span{E_j=p(t)(t-1)q_j(t):j>=1}. The vector of §19.1 is E_1, with q_1=t-a and R of degree 2; the profile p=P1 of the integer scales is another object.

**Sufficient and necessary equivalence for all windows.** Define the Hermitian matrix Gamma_ij by polarization of Q(E_i,E_j), with the FULL form Q, not only Q_B. PSD of ALL initial blocks Gamma_(1..N) is equivalent to Q>=0 on the whole primitive polynomial carrier. In turn it is equivalent to the target lambda_A(T)>=0 for ALL T, as follows.

For sufficiency, take a smooth compact primitive physical test f and translate it to support inside (0,infinito), preserving Tate and W. Set F(t)=f(.5log t) and

    P(t)=T^-1F(t)=(1/(2pi))t^(-3/2)
                         integral_t^infinito v^(-3/4)F(v)dv.

It is smooth and zero for t sufficiently large. Moreover the vanishing positive Tate moment makes P(1)=0; if F vanishes near 1, P also vanishes there. The other moment gives integralP=0 by §18.9. Thus P is a primitive compact of the preceding domain. The primitive polynomial approximation preserves the full graph and gives Q(P)>=0 under the hypothesis on ALL Gamma. Under u=.5log t, Q(P)=W[f], with the constants and the causal boundary verified in [GLOBAL](POWER_GLOBAL_ROUTE_REVIEW.md), operational control of §18.5. Therefore W is nonnegative on smooth compact primitive tests. Their density in the primitive domain of each window is obtained from the density of the form core and correction of its two Tate errors with two fixed interior bumps; the moments are continuous. Passing to the limit gives lambda_A(T)>=0 for ALL T.

Conversely, if that global target holds, for any primitive polynomial P=pR the physical function f(u)=(TP)(exp(2u)), u>=0, has a supertail with all derivatives and both Tate moments zero. It belongs to H_eta of 014 for any eta>1/2. Cutting it off only at infinity and correcting the moments with two fixed physical bumps produces EXACTLY primitive compacts converging in H_eta. The causal jump at 0, if it exists, is allowed in the logarithmic domain; P'(1)=0 is not imposed. Each compact is translated to some window and has W>=0 by the hypothesis. Continuity 014 gives Q(P)=W[f]>=0. This signs all blocks Gamma and completes the equivalence.

**Scope.** It is proved that THIS primitive polynomial family is sufficient if ALL its degrees and crossings are signed; its positivity in all sizes remains OPEN. The first vector is certified in §19.7 and the two-vector block is certified separately in §19.9. No sign is inherited in the next degree nor in combinations from density, orthogonality of w or individual positive vectors. Nor is a minimum at fixed T or a new W/T window identified. This bridge incorporates no computations and modifies no papers.


### 19.9. Full primitive block of dimension two and failure of the separate sign of Q_B

**PROVED via rational/Arb certificate with full analytic tails, 2026-11-06.** Design arithmetic_fresh_candidate, prior mathematical review fresh_global; implementation arithmetic_fresh_candidate, literal audit of the corrected code fresh_global and independent reproduction completed exit 0/FULLPASS. Parameters fixed before execution: precision 192 bits, 960 equal panels of width 1/64 on [1,16], Taylor degree 40, four modes to enclose the parameters and two modes for the reference integrals. There is no parameter search, adaptive quadrature or sign decision in ordinary floating point.

Reproducible sources: [verifier](tools/power_thermal_primitive_two_verify.py) and [log](tools/power_thermal_primitive_two_verify.log). SHA256 of the CORRECTED verifier used in the construction and in the independent reproduction:

    e589fb2b9d98d76f021418427a903794f17aa629832f400f2154c21add52f170

The certificate keeps order 41 in each truncated series via exact algebraic polynomial derivatives and precision asserts; it does not differentiate a truncated series by reducing its order. The following bounds explain the whole error budget and the scope of the certificate, without depending solely on reading the log.

**Vectors and exact parameters.** Use x=t-1, p and w=(t-1)p of §19.1. For j=0,1,2,3,

    mu_j=integral_1^infinito x^j w(t)dt
        =(j+1)! S_(2j+2)/pi^(j+2),
    Delta=mu_2 mu_0-mu_1²>0,
    b=mu_1/mu_0,
    alpha=(mu_3 mu_0-mu_2 mu_1)/Delta,
    beta=(mu_3 mu_1-mu_2²)/Delta.

Strict positivity of Delta is the nonzero variance of the positive weight w, multiplied by mu_0². Define

    R_1=x(x-b),
    R_2=x(x²-alpha x+beta),
    E_1=pR_1,  E_2=pR_2.

The name E_i avoids confusing these vectors with the profile P_1 of the integer scales. E_1 coincides with the vector of §19.1, since a=1+b. The parameters of R_2 impose exactly

    mu_2-alpha mu_1+beta mu_0=0,
    mu_3-alpha mu_2+beta mu_1=0.

Thus E_1,E_2 are the first two vectors of the primitive basis of §19.8, although there the orthogonal polynomials are written in t instead of x. Both satisfy E_i(1)=0 and integral E_i=0. They are linearly independent by their degrees 2 and 3; every nonzero real pair of coefficients represents a nonzero, exactly primitive function.

To enclose the parameters, the first four terms of EACH S_j, j=2,4,6,8, are summed. The full positive remainder satisfies

    0<sum_(n>=5)n^(-j)exp(-pi n²)
         <(101/100)5^(-j)20^(-25).

One uses pi>3, exp(3)>20 and the geometric comparison of consecutive terms; the factor 101/100 is greater than 1/(1-1/1000). Evaluation with 192-bit balls, adding that positive interval BEFORE forming mu,Delta,b,alpha,beta, certifies

    63/100<b<2/3,
    19/10<alpha<48/25,
    3/5<beta<31/50,
    Delta>0.

All uncertainty of these parameters remains inside each subsequent coefficient. They are not replaced by their midpoints.

**Modal expansion and polarization.** For i=1,2 and n>=1 set

    L_(i,n)(t)=-sum_(j=1)^3
                  R_i^(j)(t)/[j pi^j n^(2j-2)]
          +2n²sum_(m|n,m>=2)Lambda(m)
                              [R_i(t)-R_i(m²t)],
    H_(i,n)=(2pi n²t-3)R_i-2tR_i',
    J_(i,n)=(2pi n²t-3)L_(i,n)-2tL_(i,n)'.

The derivative sum actually ends at the degree of R_i. The identity Bp=0 and the same difference expansion of §19.2 give

    F_i=TE_i=pi t^(5/4)sum_(n>=1)n²exp(-pi n²t)H_(i,n),
    Z_i=TBE_i=pi t^(5/4)sum_(n>=1)exp(-pi n²t)J_(i,n).

The full real symmetric matrix being certified is

    Q_ij=integral_1^infinito
       [log(t)F_i(t)F_j(t)+(F_i(t)Z_j(t)+F_j(t)Z_i(t))/2]
                                                         dt/(2t).
                                                        (BLOCK-Q)

In particular Q(P)=c^t Q c for P=c_1E_1+c_2E_2. The symmetric average of the crossings is kept; Q_B is not replaced by a one-sided non-symmetrized expression. For the separation diagnostic one also integrates DIRECTLY

    Q_B(E_1+E_2)=integral_1^infinito
                         (F_1+F_2)(Z_1+Z_2)dt/(2t).

**Real bounds for all modes.** The intervals of b,alpha,beta prove for t>=1

    |R_i|<=t³, |R_i'|<=3t², |R_i''|<=6t, |R_i'''|<=6.

For example x²-alpha x+beta>=beta-alpha²/4>-1 and its upper bound is less than x²+1; this gives |R_2|<=t³. For R_2'=3x²-2alpha x+beta, the negative term is bounded by 4x<=3t²; the other derivatives and R_1 satisfy the written bounds directly.

The derivative part of L_(i,n) has modulus at most (38/27)t³. For n>=2, its derivative has modulus at most (25/12)t². The arithmetic part and its derivative are bounded respectively by

    2n²log(n)(1+n^6)t³<=(65/32)n^8log(n)t³,
    6n²log(n)(1+n^6)t²<=(195/32)n^8log(n)t².

Here the full difference R_i(t)-R_i(m²t) was kept, using sum_(m|n)Lambda(m)=log n. Since n^8log n>512/3 for n>=2, one deduces

    |L_(i,n)|<=3n^8log(n)t³,
    |L_(i,n)'|<=7n^8log(n)t²,
    |J_(i,n)|<=23n^10log(n)t^4, n>=2.

For n=1, |L_(i,1)|<3t²/2 and |L_(i,1)'|<=7t/3 suffice. By the rational inequalities verified with pi,

    pi(2pi+6)<39, 23pi<73,
    pi(3pi+14/3)<45,

the modal summands of F_i,Z_i satisfy uniformly for i=1,2

    |F_(i,n)|<=39n^4t^(21/4)exp(-pi n²t), n>=1,
    |Z_(i,1)|<=45t^(21/4)exp(-pi t),
    |Z_(i,n)|<=73n^10log(n)t^(21/4)exp(-pi n²t), n>=2.
                                                        (BLOCK-MODES)

These bounds also justify the absolute convergence of the expansions and integrals of (BLOCK-Q).

**Error from omitting modes n>=3 in the integration reference.** Abbreviate

    C=101/100,
    T_d(N)=C N^d/20^(N²),
    Sbar_4=1/20+T_4(2).

For N>=2,d<=11, the ratio between consecutive terms of n^dexp(-3n²) is less than (3/2)^11/20^5<1/1000; therefore its tail is less than C N^dexp(-3N²). Every omitted pair has h=n²+m²>=10. The pertinent integrals satisfy

    integral_1^infinito t^(19/2)exp(-pi h t)dt
          <=exp(-pi h)/(pi h-19/2)<exp(-3h)/20,
    integral_1^infinito t^(21/2)exp(-pi h t)dt
          <exp(-3h)/19.

For the second, log t<=t was used. Applying (BLOCK-MODES) and log n<=n gives the absolute budgets, for EACH symmetrized entry,

    r_B=(39/40)[73 Sbar_4 T_11(3)
                  +45 T_4(3)/20+73 T_4(3)T_11(2)]
       =510613632029241/409600000000000000000
       <1/500000,
    r_log=(1521/19)T_4(3)Sbar_4
       =623421823401/972800000000000000000
       <1/10^9.
                                                        (BLOCK-MODERR)

The first budget covers Z of index >=3 against all F, and F of index >=3 against Z of index 1 or >=2. It may count some pairs twice, which only increases the majorant. The average of two terms in Q_B,ij keeps the same bound r_B. For the direction E_1+E_2, the error of Q_B is at most 4r_B. No pair of large indices nor a prime-power contact is eliminated.

**Temporal tail after 16.** The same majorants, even looser, give for each i

    |F_i(t)|<=663t^(21/4)exp(-pi t),
    |Z_i(t)|<=149549t^(21/4)exp(-pi t).

Cexp(-9)<1 was used, so that the relative tails are bounded by 2^4 and 2^11, and 39(1+2^4)=663,45+73*2^11=149549. These bounds hold for the full series and, in particular, for the two retained modes. For r=10,11,

    integral_16^infinito t^r exp(-6t)dt
       <=16^r exp(-96)/(6-r/16)<16^r/(5*20^32).

By log t<=t, valid budgets for each entry are

    e_B=663*149549*16^10/[10*20^32],
    e_log=663²*16^11/[10*20^32],
    e_B+e_log<1/10^20.

The integer exponents 10,11 majorize respectively 19/2 and 21/2 for t>=16. The direction E_1+E_2 needs 4e_B for its Q_B part.

**Reference integration with verified Taylor remainder.** Only in this finite evaluation are the modes n=1,2 kept; the preceding errors pay for all the others on the full half-line. For n=2, the only nontrivial divisor is 2, so L_(i,2) contains exactly 8log2[R_i(t)-R_i(4t)]. Its derivative is evaluated algebraically as 8log2[R_i'(t)-4R_i'(4t)] plus the derivative of the derivative part. It is not replaced by numerical differences.

On each complex disc of radius 1/8 centred in [1,16] one has Re z>7/8, |z|<17, |z-1|<18 and |4z-1|<69. The principal branches of log z and z^(5/4) are holomorphic there. The preceding parameter intervals give

    |R_i(z)|<10^4, |R_i'(z)|<2000,
    |R_i''(z)|<200, |R_i'''(z)|<=6,
    |R_i(4z)|<4*10^5, |R_i'(4z)|<15000.

Denote by F_i^[2],Z_i^[2] the reference sums with n=1,2 only. By the exact modal formulas of those two modes, using |exp(-pi n²z)|<1,

    |H_(i,n)|<10^7, |L_(i,n)|<4*10^6,
    |L_(i,n)'|<5*10^5, |J_(i,n)|<3*10^9,
    |F_i^[2](z)|<2*10^11, |Z_i^[2](z)|<10^13.

Moreover |log z|<4 and |1/(2z)|<1. Therefore M=10^30 dominates the modulus of each REFERENCE integrand of Q_11,Q_12,Q_22 and of the direct integrand of Q_B(E_1+E_2), including their polarization factors. The errors (BLOCK-MODERR) separately keep all the modes not included in that reference. These are complex bounds for the integrands, not real estimates transferred without proof.

The 960 panels have width 1/64 and half-width 1/128. For the Cauchy radius 1/8, the ratio is 1/16. The even terms of the Taylor polynomial of degree 40 are integrated exactly, with 192-bit ball arithmetic. The total truncation error is bounded by

    e_Taylor=15*10^30*(1/16)^41/(1-1/16)<1/10^18.

The verifier builds R_i',R_i'',R_i''' and L_(i,n)' by exact polynomial formulas. It explicitly checks that the fields F_i,Z_i, the four integrands and the series entering the integration have precision 41 on EACH panel. Thus the degree-40 remainder corresponds to the order actually used.

**Inflation and final gates.** Before any sign comparison, symmetric balls of radii

    e_Q=r_B+r_log+e_B+e_log+e_Taylor<1/400000,
    e_direction=4r_B+4e_B+e_Taylor

are added. The parameter uncertainty is already incorporated in all coefficients and is not omitted from these intervals. The main run and the independent reproduction, with the same corrected hash, ended exit 0/FULLPASS and certified

    Q_11>179/100000,
    Q_22>17/10000,
    |Q_12|<79/50000,
    Q_B(E_1+E_2)<-1/20000.

By exact rational arithmetic,

    det Q> (179/100000)(17/10000)-(79/50000)²
           =2733/5000000000>0.

Hence the FULL block Q on span{E_1,E_2} is positive definite: EVERY nonzero real combination has Q>0. The signs of its two coefficients are not restricted. At the same time, E_1+E_2 is exactly primitive and has Q_B<0. The promotion of the separate sign Q_B(E_1)>0 of §19.7 to this two-dimensional family is refuted; the contribution Q_log is necessary in that argument. This does NOT produce a negative value of Q nor a counterexample to the sign of the paper.

**Scope.** This is an assisted certificate of a single primitive 2x2 block with all its crossings and full tails. By §19.8, signing ALL blocks of the family would be sufficient and necessary for the global target; here only two dimensions have been signed. There is no automatic inheritance to the next degree, positive recurrence, new uniform margin nor new W/T window. The orthogonal polynomials of w do not by themselves diagonalize Q. No paper has been modified nor is a global sign inferred.


### 19.10. All blocks of any fixed tail of degrees are equivalent to the global target

**PROVED as scope, not as new positivity.** joint_sign_fresh_review; independent audits arithmetic_fresh_candidate and fresh_global PASS before recording. Consulted the project rules, the three indices, §§18.9,19.8, [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md), [RECIPROCAL_PFAFFIANS083](POWER_RECIPROCAL_PFAFFIANS_083.md) and [GLOBAL, «Primitive comparisons»](POWER_GLOBAL_ROUTE_REVIEW.md). The analytic lemma proved there is applied, with an arbitrary FINITE number of constraints, to the already established thermal core. No other positive inequality nor a new continuation principle is presented; the difference with respect to §19.8 is keeping exactly the additional moments that eliminate any fixed prefix of degrees.

**Statement.** Fix an integer J>=1 and the E_j=p(t)(t-1)q_j(t) of §19.8. The following are equivalent:

1. Q is nonnegative on EVERY finite combination of E_j with j>=J, including all their crossings; equivalently, all blocks Gamma_(J..N), N>=J, are PSD.
2. lambda_A(T)>=0 for ALL T>0.

The tail is fixed before quantifying the sizes. 1 is not replaced by the sign of the diagonals, of a finite block, or of a union of positive packets of growing dimension.

**Exact constraints of the tail.** By orthogonality of q_j for w=(t-1)p, a polynomial P=pR belongs to the FINITE span{E_j:j>=J} exactly when

    P(1)=0,
    integral_1^infinito t^k P(t)dt=0, 0<=k<J.       (TAIL-MOM)

Indeed P(1)=0 is equivalent to R=(t-1)S; the other conditions say that S is orthogonal in L²(w dt) to all polynomials of degree <J. Its FINITE polynomial expansion in the q_j then starts at J.

For F=TP and f(r)=F(exp(2r)), r>=0, the identity of §18.9 gives

    ell_sigma(f)=pi P(1)
        +pi(sigma/2-1/4)integral_1^infinito
                                      t^(sigma/2+1/4)P(t)dt.

Therefore (TAIL-MOM) is equivalent to ell_sigma(f)=0 for the list of J+1 DISTINCT real numbers

    Sigma_J={1/2} union {2k-1/2:0<=k<J}.          (TAIL-SIGMA)

For sigma=1/2 one obtains pi P(1); for sigma=2k-1/2 the coefficient of the integral is pi(k-1/2), which does not vanish for integer k. P'(1)=0 is not imposed.

**Finite extension of the lemma already proved in GLOBAL.** Let sigma_1,...,sigma_m be distinct reals, D odd real-analytic on ALL of R and K_D(u,v)=(D(u)+D(v))/(u+v), with removable continuation. If K_D is PSD on ALL blocks of an open interval I contained in (max_l sigma_l,infinito), subject to

    sum_i d_i/(u_i-sigma_l)=0, 1<=l<=m,           (CPD-m)

then K_D is fully PSD. To prove it set

    V(u)=prod_(l=1)^m(u-sigma_l),
    d_i=V(u_i)b_i,
    L(u,v)=V(u)V(v)K_D(u,v).

The polynomials V(u)/(u-sigma_l) form a basis of those of degree <=m-1: evaluating at the sigma_l proves their independence. Thus (CPD-m) is equivalent to sum_i b_i u_i^k=0, 0<=k<m. Choose m distinct anchors in I and subtract from each delta_x its Lagrange interpolant on those anchors. The resulting measures E_x annihilate those m moments and C(x,y)=L(E_x,E_y) is PSD on I. L and C are jointly real-analytic on ALL of R² because D is odd. The continuation of §2.2 propagates PSD of C to all of R, exactly as in the case m=2 of GLOBAL.

For any finite measure with those vanishing moments the anchor corrections cancel, so that its energy L is nonnegative. The rows L(sigma_l,v) are zero. Given an arbitrary vector with nodes outside the sigma_l, divide its coefficients by V and add masses at the m points sigma_l to annihilate the m moments. The matrix of that repair is Vandermonde and invertible; the null rows ensure the energy does not change. Full PSD of K_D results outside those points and, by continuity, also at them. The converse by restriction is immediate. Only a FINITE fixed number of moments is used, not a continuation uniform in m.

**Thermal approximation with the J+1 constraints.** All functionals P(1), integral t^kP, 0<=k<J, are continuous on B_a², 0<a<pi. The core of §19.8 approximates any smooth P_c with compact support in [1,infinito) by pR_n in that norm and in the full graph (F,G). If P_c satisfies (TAIL-MOM), the J+1 errors tend to zero. Repair them with the FIXED polynomial vectors

    p, (t-1)p, t(t-1)p,...,t^(J-1)(t-1)p.

The boundary row is (p(1),0,...,0). The remaining block, on the last J vectors, is the Hankel

    H_kj=integral_1^infinito t^(k+j)w(t)dt,
    0<=k,j<J,

which is positive definite because w>0 for t>1 and all its moments are finite. The total matrix has determinant p(1)det H>0. Its inverses and the repair vectors are FIXED for this J; their correcting coefficients tend to zero. The corrected approximants satisfy (TAIL-MOM) exactly, belong to the finite span of E_j,j>=J and converge in the graph. Under hypothesis 1, continuity gives Q(P_c)>=0 for every compact of this subspace.

**Physical cutoff BEFORE applying the core.** To pass from those compacts to (CPD-m), take the list (TAIL-SIGMA), choose U>max(1/2,max_(sigma en Sigma_J)|sigma|), and rates u_i>U. Let h(r)=sum_i d_i exp(-u_i r), r>=0, with sum_i d_i/(u_i-sigma)=0 for each sigma of the list. Choose eta with max(1/2,max Sigma_J)<eta<min_i u_i. Then h belongs to H_eta of 014 and all moments ell_sigma are continuous there.

Cutting h off smoothly only at infinity produces errors in those moments tending to zero. There exist J+1 FIXED physical bumps with invertible moment matrix: take psi smooth nonnegative, supported inside (1,2) and positive on an interval, and the bumps psi(r)exp(sigma_l r). The moment matrix is the Gram of the exponentials exp(sigma_l r) in L²(psi dr), positive definite by their linear independence. Correcting with those bumps gives compact h_n EXACTLY subject to (TAIL-SIGMA), converging to h in H_eta. h_n(0)=0 is not required; the possible jump of the causal extension is allowed in the logarithmic domain, as in §18.9.

Now, and only now, set F_n(t)=h_n(.5log t) and P_n=T^-1F_n with the terminal inverse of §17.8. Each P_n is smooth up to 1 and zero for t sufficiently large. The moment identity gives (TAIL-MOM), without imposing P_n'(1)=0. The preceding repaired thermal approximation signs Q(P_n)=W[h_n]>=0. Continuity 014 and the exact identity of CONE001 give

    W[h]=sum_ij d_i conjugado(d_j)K_(M_Phi)(u_i,u_j)>=0

on the subspace (CPD-m) on any open interval contained in (U,infinito). M_Phi is odd and real-analytic on all of R, by the parity and real positivity of Z. The extended lemma applied to D=M_Phi yields full PSD of K_(M_Phi). The bridges §§2,18.9/BRIDGE002 then give target 2.

This order avoids applying the B_a² core directly to T^-1 of an uncut physical exponential mixture: that preimage has power tails and it has NOT been claimed that it belongs to B_a². The norms of the compacts or their constants may depend on the cutoff and on J; only convergence for each fixed list is required.

Conversely, target 2 signs all primitive blocks by §19.8 and therefore their restriction to any fixed tail. This completes the equivalence.

**Scope.** It is an application of the antecedents of continuation, finite moment repair and core, not a new positive inequality. The sign of all blocks of any of these tails remains OPEN. The block E_1,E_2 of §19.9 does not automatically control any tail nor the crossings with it; nor is it proved that any tail cannot be signed. No minimum at fixed T is identified, there is no uniformity in J nor new margin, W/T window, computation or change to papers.


### 19.11. The first-mode reference is not PSD on the exact primitive polynomial domain

**PROVED as an application of an earlier falsifier to this domain.** Construction joint_sign_fresh_review; audits of the short version joint_sign_fresh_review/fresh_global/arithmetic_fresh_candidate and second review PASS. Consulted the project rules and the three indices; antecedents [PRIME_PATTERN_FALSIFIER008§4](POWER_PRIME_PATTERN_FALSIFIER_008.md), [AUDIT008](POWER_AUDIT_008.md), [CONFLUENT_BRIDGE014](POWER_CONFLUENT_BRIDGE_014.md), §§18.9,19.8 and the operational control of §18.5 in [GLOBAL](POWER_GLOBAL_ROUTE_REVIEW.md). The need to keep the arithmetic was already recorded in 008. Here that deficit is only transported to the first-mode reference and to the EXACT constraints of this polynomial family, without computing another degree or another numerical vector.

Set p_0(t)=exp(-pi t), p(t)=sum_(n>=1)n²exp(-pi n²t), t>=1, and define for real polynomials R

    Q_0(R)=integral_1^infinito
       [log t |T(p_0R)|²
          +Re(T Lg(p_0R) conjugado(T(p_0R)))]dt/(2t).
                                                        (FIRST-REF)

C does not appear in this reference: p is replaced by p_0 and B by Lg. It is claimed that there exists a real polynomial R such that

    R(1)=0, integral_1^infinito p(t)R(t)dt=0,
    Q_0(R)<0.                                   (FIRST-NEG)

The first two conditions make pR, the vector of the REAL family, exactly primitive. They do NOT say that p_0R has both Tate moments zero.

**Physical identity without comb.** For a temporal profile P smooth with compact support or with sufficient exponential decay, denote by A_P(P) the right-hand side of (FIRST-REF) with p_0R replaced by P. The physical identity already verified for the full graph in GLOBAL, operational control of §18.5, on removing C, gives exactly

    A_P(P)=Arch[f]+2Re(ell_+(f)conjugado(ell_-(f))),
    f(u)=(TP)(exp(2u)), u>=0,
    ell_+(f)=pi P(1), ell_-(f)=pi P(1)-(pi/2)integral P.

The causal boundary is kept. This identity is used only on smooth compacts and the subsequent polynomial exponential profiles, where all pieces converge. A_P is continuous on B_a², 0<a<pi, by §18.2 with G=(1/2)T LgP and without C. Moreover Q_0(R)=A_P(p_0R).

**A three-dimensional negative physical plane.** The bound of 008§4 is

    m(tau)<=-4+17tau²,
    Arch[f]<=-4||f||²+17||f'||²

for smooth compact physical tests, by Parseval. Fix a nonzero real bump phi in C_infinito,c((0,1)), c=||phi'||²/||phi||², and choose L>0 with L²>17c/4. The three vectors

    f_j(u)=L^(-1/2)phi(u/L-3j), j=1,2,3,

have disjoint supports inside the half-line and separated from 0. On ALL of their real span V, both the norms and the derivative norms add without crossings; thus ||f'||²/||f||²=c/L² for each nonzero f and Arch[f]<0. No new determinant is evaluated nor is the sign of the full comb used.

**Two constraints leave a negative direction.** For each f in V, set F(t)=f(.5log t) and P=T^-1F with the terminal inverse of §17.8. This map is linear and injective; each P is smooth up to 1 and zero for t sufficiently large. Define

    rho(t)=p(t)/p_0(t)
          =sum_(n>=1)n²exp[-pi(n²-1)t].

The function rho is positive and bounded on [1,infinito). Intersect in V the two real kernels

    P(1)=0, integral_1^infinito rho(t)P(t)dt=0.

From dimension three minus at most two constraints some nonzero f remains. For this vector ell_+(f)=0, so the polar product vanishes and A_P(P)=Arch[f]<0. ell_-(f)=0 is not needed nor is integralP=0 claimed. Since F vanishes near 1, the condition P(1)=0 also makes P zero near 1; in particular it is an admissible interior compact for the core.

**Passing to a polynomial with the exact constraints.** The core argument of §19.8 also applies to p_0: its first two derivatives are constants times exp(-pi t), the continuation in B_a² of p_0exp(zt) has the same half-plane Re z<pi-a, and the C² approximation of compacts proceeds exactly the same. Thus there exist real polynomials R_n with p_0R_n->P in B_a². The errors of P(1) and integral rho P tend to zero; the second functional is continuous because rho is bounded and exp(-at) is integrable.

Repair them with the two FIXED profiles p_0,tp_0. The matrix of these functionals has determinant

    p_0(1)[integral_1^infinito t p(t)dt
                              -integral_1^infinito p(t)dt]
       =exp(-pi)integral_1^infinito (t-1)p(t)dt>0.

The correcting coefficients tend to zero. Therefore the corrected profiles still converge to P in B_a² and are p_0 times real polynomials, again called R_n, with R_n(1)=0 and integral p R_n=0 EXACTLY. Continuity of A_P preserves negativity for some finite n. This proves (FIRST-NEG), without computing the degree or the coefficients of the resulting polynomial.

**Scope.** Only universal PSD of the reference (FIRST-REF) on the EXACT primitive domain defined via p is refuted. It is an application of the archimedean deficit of 008 and of the existing core, not a new principle of arithmetic necessity. It is not a negative value of the full Q, of A or of the kernel of a truncated theta density; nor does it refute every perturbative comparison or every compensation between modes. The positive certificates §§19.7,19.9 remain intact and the full global sign remains OPEN. No new degree evaluated, campaign, computation, auxiliary file, W/T window or change to papers.

### 19.12. Causal adjoint and local potential: negative sign to the right of log2

**PROVED, with full tail and elementary proof.** Construction joint_sign_fresh_review; independent audit arithmetic_fresh_candidate FULLPASS of normalizations, inequalities and all tails, second review PASS prior to recording. Reread the project rules and the three indices; cross-checked §18.5, GLOBAL (operational control of the causal change), [106_31](../phase-106-global-modular-star-audit/106_31_FULL_KERNEL_DOOB_VARIANCE_IDENTITY.md) and [ROUND005D](ROUND_005_D.md). Picone/Doob and logarithmic killing have those antecedents. The difference examined is the potential of the CAUSAL adjoint of this exact J, with the metric dt/(2t), and its sign at a concrete jump point. This literal computation was not found in the targeted cross-check; neither exhaustive reading nor worldwide priority is claimed. The following proof does NOT use the external justification of the radical identity of 106_31.

**Identity of the adjoint, keeping the endpoint 1.** Set

    p=P_1, Theta(t)=Tp(t)=Phi(.5log t)>0,
    J=TBT^(-1), r=.5log t, dt/(2t)=dr.

The identity Bp=0 of §18.5 holds for ALL t>0: the theta series and the sums with logarithms converge absolutely on each compact of t>0. In the coordinate r, the full forward operator L_f=logt+J is translation invariant, with the diagonal renormalization already fixed in GLOBAL. Its off-diagonal kernel, directed towards r+h, is 2k(h), where

    k(h)=2cosh(h/2)-exp(-h/2)/(1-exp(-2h))
                       -sum_(n>=2)Lambda(n)/sqrt(n) delta_(log n)(h), h>0.

The diagonal term is kept via the Frullani formula; a singular kernel is not integrated separately. From JTheta=0 one obtains L_f Phi(r)=2rPhi(r) on ALL of R. Reflecting this identity using even Phi gives L_b Phi(r)=-2rPhi(r) for the backward operator with the same renormalization. Therefore their average H_full satisfies H_full Phi=0, deduced only from Bp=0, parity and the physical identities of §18.5/GLOBAL.

Let H_+ be the symmetric average on r>=0. For r>0, removing the part s<0 of the full average leaves exactly

    g(r):=H_+Phi(r)=-integral_0^infinito k(r+s)Phi(s)ds.       (POT-G)

There is no diagonal singularity in this integral when r>0. Since H_+=logt+(J+J*)/2 and JTheta=0,

    (J*Theta)(exp(2r))=2g(r)-4rPhi(r).                       (CAUSAL-ADJ)

Here J*Theta is understood as the weak causal adjoint against smooth compact tests; membership in a global domain of the Hilbertian adjoint is not postulated. The restriction r>=0 and its boundary are included in (POT-G), not replaced by a convolution without boundary.

To relate it to the path proposal, define Q_phys(F):=Q(T^(-1)F), keeping Q(P) as in §19. Write F=Theta f and use the off-diagonal SIGNED measure

    dnu(t,v)=dt/(2t) [K(t,v)dv
                  -2sum_(m>=2)Lambda(m)/sqrt(m) delta_(m²t)(dv)],

with K of §18.5 and v>t. JTheta=0 and the identity
Re(conj(a)(b-a))=(|b|²-|a|²-|b-a|²)/2 give, for f smooth with compact support, with the differences making the diagonal boundary integrable,

    Q_phys(Theta f)=-.5 integral Theta(t)Theta(v)|f(v)-f(t)|² dnu + V(f),
    V(f)=integral_0^infinito Phi(r)g(r)|f(exp(2r))|²dr.      (POT-V)

It is equivalent to keeping logt Theta²+.5Theta J*Theta in the physical metric. It is not assumed that the physical measure is stationary because J has a null vector on the right.

**Explicit formula and right side of the jump.** For h>0,

    2cosh(h/2)-exp(-h/2)/(1-exp(-2h))
             =exp(h/2)-sum_(j>=1)exp(-(2j+1/2)h).

With the positive constants

    A_+=integral_0^infinito exp(s/2)Phi(s)ds=pi p(1),
    A_0=integral_0^infinito Phi(s)ds,
    A_j=integral_0^infinito exp(-(2j+1/2)s)Phi(s)ds, j>=1,

one obtains, almost everywhere for r>0,

    g(r)=sum_(n>exp r)Lambda(n)/sqrt(n) Phi(log n-r)
                    -exp(r/2)A_+
                    +sum_(j>=1)exp(-(2j+1/2)r)A_j.       (POT-EXPLICIT)

The equality A_+=pi p(1) is exactly the identity of the positive moment of §18.9. The supertails of Phi justify the series absolutely; the prime series converges uniformly on compacts of r away from its jump points. At r=log2 from the RIGHT, the term n2 has disappeared. Define

    P_3=sum_(n>=3)Lambda(n)/sqrt(n) Phi(log(n/2)),
    Gamma=sum_(j>=1)2^(-2j-1/2)A_j.

Then g(log2+)=P_3-sqrt(2)A_++Gamma. Since A_j<=A_0<=A_+,

    Gamma<=A_+/(3sqrt(2)),
    g(log2+)<=P_3-[5/(3sqrt(2))]A_+.                     (POT-BUDGET)

**Generous polar bound.** The inequalities pi>3, pi<16/5 and exp(16/5)<25 prove

    A_+>=pi exp(-pi)>3/25.

Taylor gates for the exponentials are given below. Since sqrt(2)<3/2, the net loss of (POT-BUDGET) is strictly greater than 2/15.

**FULL prime/theta tail.** For n>=3 the exact positive series is

    Phi(log(n/2))=pi sum_(m>=1)m²(n/2)^(5/2)
              [(pi/2)m²n²-3]exp(-pi m²n²/4).

Multiplying by Lambda(n)/sqrt(n) and extracting the leading part leaves

    [pi²/(8sqrt(2))] Lambda(n)m^4 n^4
       [1-6/(pi m²n²)]exp(-pi m²n²/4).

Use pi²<10, sqrt(2)>7/5, Lambda(n)<=log n and log3<9/8. In the ONLY isolated pair (n,m)=(3,1), keep the bracketed factor, less than 4/5 because pi<10/3. Since pi>25/8 implies 9pi/4>7 and exp7>1000,

    contribucion_(3,1)
      <(25/28)·81·(9/8)·(4/5)/1000=3645/56000.          (POT-FIRST)

For ALL other pairs set q=mn>=4 and omit only the negative term -3 in an upper bound. The divisor-pairing identity and the bounds tau(q)<=q, log q<=q/2 for q>=4 give

    sum_(n|q,n>=3)log n
         <=sum_(n|q)log n=tau(q)log q/2<=q²/4.

The prefactor pi²/(8sqrt(2))<25/28<1 and pi/4>25/32 prove for the full remainder

    resto<sum_(q>=4)(q^6/4)exp(-25q²/32).

The ratio between consecutive terms is at most

    (5/4)^6 exp(-225/32)<4/1000=1/250.

With exp(25/2)>250000, summing this geometric tail yields

    resto<1024/249000,
    P_3<3645/56000+1024/249000<7/100.                    (POT-TAIL)

The grouping includes every mode m and every prime-power integer n>=3; it is not a truncation without remainder nor a change of the weights Lambda.

**Sufficient elementary gates.** To make the preceding exponential budgets explicit, set S8=sum_(k=0)^8 3^k/k!. The rational comparisons

    S8>20,
    S8+(3^9/9!)/(1-3/10)<81/4

give 20<exp3<81/4; the upper bound uses the ratio of terms of the tail from order 9, at most 3/10. Moreover

    exp(1/5)<6/5+3/140<49/40,
    exp(16/5)<(81/4)(49/40)=3969/160<25,
    exp7=(exp3)² exp1>20²·(8/3)>1000,
    exp(25/2)=(exp3)^4 exp(1/2)>20^4·(13/8)>250000.

The upper bound on exp(1/5) sums from degree 2 with ratio at most 1/15; exp1>8/3 and exp(1/2)>13/8 follow from their positive series. The inequality log3<9/8 follows from sum_(k=0)^4(9/8)^k/k!>3: FIVE terms are used, degree 4. The preceding bounds on pi are the usual elementary rational ones; for example pi>25/8 follows from pi=4[arctan(1/2)+arctan(1/3)] and

    4[(1/2-1/24+1/160-1/896)+(1/3-1/81)]>25/8,

via the lower alternating sums of arctan. All the gates and the final rational comparison (POT-TAIL) were checked in the independent audit, without quadrature or campaign.

**Sign and scope.** Combining (POT-BUDGET) and (POT-TAIL) gives strictly

    g(log2+)<7/100-2/15=-19/300<-1/20.                  (POT-NEG)

Local uniform convergence to the right of log2, before the next jump log3, keeps g<0 on some open interval I. Since Phi>0, choosing a nonzero smooth f with physical support in I makes V(f)<0 in (POT-V). The same negative sign is kept with EXACT primitivity: take three smooth, nonzero real bumps chi_i with disjoint supports inside I. On their 3-dimensional space the two functionals

    b -> integral_I exp(r/2)Phi(r)sum_i b_i chi_i(r)dr,
    b -> integral_I exp(-r/2)Phi(r)sum_i b_i chi_i(r)dr

have a common kernel of dimension at least 1. Choose nonzero b in it and set f(exp(2r))=sum_i b_i chi_i(r). The physical F(exp(2r))=Phi(r)sum_i b_i chi_i(r) has both Tate moments zero. The disjoint supports ensure F nonzero, and Phi g<0 on I gives V(f)<0 strictly. Its preimage P=T^(-1)F is smooth compact and satisfies P(1)=integralP=0 by §18.9; P'(1)=0 is not imposed. No radius, degree or other sign test is computed. By contrast, the boundary r towards 0 has g(r)=[Phi(0)/2]log(1/r)+O(1): the known favourable logarithmic killing of ROUND005D§1 does not control this interior interval.

ONLY the requirement V(f)>=0 for all local bumps in this exact decomposition is refuted, EVEN restricting F to exact primitivity via the combination of three bumps. The difference term of (POT-V) keeps mixed sign and can compensate V<0: it is NOT proved that Q is negative, A negative, the full primitive form of Paper46 negative, nor a general NO-GO for paths, three points or joint treatments. Global remains OPEN; certificates §§19.7,19.9 intact. No new files, campaign, new W/T window or changes to papers.
