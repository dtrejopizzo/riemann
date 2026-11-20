# Hyperbolic model: Gram of all orders through a positive Green function

Status: **PROVED for the indicated model**, independent mathematical review (cases/new invariant). **OPEN** any transfer to the real Phi. No new positivity of W, admissible dimension or window T of Paper47. Papers untouched.

## 1. Object and prior consultation

For fixed a>0, let phi_a(t)=exp(-a cosh(2t)), Z_a(u)=integral_R exp(ut)phi_a(t)dt and M_a=Z_a'/Z_a. Here a is a parameter of the model, not an exponent of a test of Paper47. We prove that

    [(M_a(u_i)+M_a(u_j))/(u_i+u_j)]_ij is PSD

for any number of positive parameters u_i. phi_a is not identified with the real theta.

Consulted ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; targeted searches in the corpus and an independent cross-check. No literal result for this model was found in the sources consulted. The inverse Bessel functions of POWER019 and the mentions of Macdonald polynomials belong to other objects. No worldwide bibliographic novelty is claimed.

The difference from POWER_GRAM_SLICES_OBSTRUCTION is concrete: the model has supertails, and its f(t)=(-log phi_a)'=2a sinh(2t) satisfies f(t)/t³→infinity. By section 5 of that note, some of its layers are NOT PSD. The following proof signs the complete kernel through a differential equation in the scale, without requiring a sign for each layer nor extrapolating the quartic model. Compared with 083, here the positive Green function providing the representation is constructed; no Stieltjes measure is postulated.

## 2. Integral and differential equation

For x>=0 and r>=0, define directly

    y_x(r)=integral_0^infinity exp(-a exp(r) cosh v) cosh(sqrt(x)v)dv.

The integrand and all necessary derivatives are absolutely integrable, uniformly on compacts of x,r. At x=0 the derivatives are interpreted through the cosh series. Changing v=2t and using parity gives EXACTLY

    Z_a(u)=y_(u²/4)(0).

There is no pending factor 2. With b=a exp(r), the difference between the second r-derivative of the factor exp(-b cosh v) and its second v-derivative is b² exp(-b cosh v). Two integrations by parts in v, with vanishing derivatives at 0 and superdecay at infinity, give

    y_x''(r)=[a² exp(2r)+x] y_x(r).                    (ODE)

Moreover y_x>0. Comparing the integrands for r+h and r proves

    y_x(r+h)/y_x(r)
      <=exp[-a exp(r)(exp(h)-1)]<=exp[-a exp(r)h].     (RATIO)

These inequalities hold for all h>=0 and x>=0.

## 3. Boundaries when differentiating in the parameter

Put z_x=partial_x log y_x. The differentiated equation implies

    (y_x² z_x')'=y_x².

Both boundaries are needed, not only the decay of y_x. The expectation under the density proportional to the integrand satisfies, by integrating the v-derivative of that density,

    1=E[b v sinh v-sqrt(x) v tanh(sqrt(x)v)]
      >=(b-x)E[v²], b=a exp(r).

We use v sinh v>=v² and tanh w<=w. Hence, when b>x,

    0<=z_x(r)=E[v tanh(sqrt(x)v)/(2sqrt(x))]
      <=E[v²]/2<=1/[2(b-x)],

with the removable value at x=0. Hence z_x(infinity)=0. The other boundary y_x² z_x'→0 is obtained directly from y_x partial_x y_x'-y_x' partial_x y_x. For b>=1, exp(-b cosh v)<=exp(-b/2)exp(-cosh v/2). The factors v², cosh v and cosh(sqrt(x)v) are integrable against the second factor. Thus y_x, partial_x y_x are O_x(exp(-b/2)), and their r-derivatives are O_x(b exp(-b/2)); the parametric Wronskian is O_x(b exp(-b)) and tends to 0. No O notation is differentiated without control. Thus

    z_x'(r)=-y_x(r)^(-2) integral_r^infinity y_x(s)²ds,
    z_x(0)=integral_0^infinity y_x(r)^(-2)
                         integral_r^infinity y_x(s)²ds dr. (LOG-DER)

RATIO dominates the last integral by integral_0^infinity (2a exp(r))^(-1)dr=1/(2a). In particular all these integrals are finite.

## 4. Green function and positive trace

Let H=-D_r²+a² exp(2r) on the half-line with Dirichlet boundary at 0. It can be defined through the integral form of |f'|²+a²exp(2r)|f|². It is positive and H>=a². Its shifted inverse R_x=(H+x)^(-1) has the explicit Green function

    G_x(r,s)=y_x(r)y_x(s) integral_0^min(r,s) y_x(t)^(-2)dt.

Indeed it vanishes at r=0, decays at infinity, satisfies the homogeneous equation off r=s and its derivative has the jump -1 required by -D². This formula also factors G_x as a continuous Gram: its factors are y_x(r)/y_x(t) times 1_(t<=r).

Tonelli and LOG-DER give

    Tr R_x=integral_0^infinity G_x(r,r)dr
          =partial_x log y_x(0)<=1/(2a).              (TRACE)

The trace is justified without a determinant: the previous Gram factorization is the product of a Hilbert–Schmidt operator with its adjoint, since the integral of its square is exactly LOG-DER. The same results are obtained via Green functions on finite intervals and passage to the limit of the positive integrals.

By the chain rule,

    M_a(u)/u=(1/2)Tr (H+u²/4)^(-1).                  (REP)

This is a constructed representation, with positive H independent of u.

## 5. Sum of squares for any size

Write R_i=(H+u_i²/4)^(-1). The resolvent identity, or multiplying the two denominators, proves

    (u_i R_i+u_j R_j)/(u_i+u_j)
       =(H+u_i u_j/4) R_i R_j.

Taking traces and using REP expresses the kernel as

    K_ij=(1/2)Tr(H R_i R_j)+(u_i u_j/8)Tr(R_i R_j).

All necessary products are trace class: H R_i²<=R_i and TRACE controls the right-hand side. For real coefficients c_i, put A=sum_i c_i R_i and B=sum_i c_i u_i R_i. Then

    sum_ij c_i c_j K_ij
        =(1/2)||H^(1/2) A||_HS²+(1/8)||B||_HS²>=0.   (GRAM)

GRAM can be read solely as integrals of squares. If F(r,s)=sum_i c_i G_(u_i²/4)(r,s) and B(r,s)=sum_i c_i u_i G_(u_i²/4)(r,s), the right-hand side is

    (1/2) integral integral [|partial_r F|²+a²exp(2r)|F|²]dr ds
      +(1/8) integral integral |B(r,s)|²dr ds.

The energy identities of the Green function justify these integrals; the boundaries are Dirichlet at 0 and decay at infinity. This proves all sizes simultaneously, without a tower of minors.

## 6. Scope and pending transfer

The model shows positively that the failure of PSD layers does not prevent a uniform proof for the complete kernel: here the mechanism is the Green function of an ODE in the scale. No ODE/Green function with the identity REP for Z of the real Phi has been constructed. The similarity of the tails does not provide that identity.

Nor does it transfer by mixing positive densities: GRAM_SLICES§7 already shows that such mixtures do not in general preserve the sign of the kernel of the logarithmic derivative. No campaign of models is proposed and no closure of W is claimed. The input that would have to be transported is the parameter-independent positive representation, not merely an approximation of phi_a to Phi.

Audit: the normalization Z_a=y_(u²/4)(0), the boundaries, the factor 1/2 of REP and the coefficients 1/2, 1/8 of GRAM were verified independently, together with a targeted cross-check of antecedents. No numerical computations.

## 7. Direct positive transfers: the real prefactor prevents two representations

**PROVED for the two declared classes; independent review.** Prior consultation of the three indices and GRAM_SLICES§7: there the quartic exclusion compares different orders of decay. Here both models have double-exponential order; the decisive difference is the prefactor, not only that order. No general prohibition of transfers or of positive operators is recorded.

The real theta series of CONE001 gives, isolating n=1 and bounding the tail n>=2,

    Phi(t)~2pi² exp(9t/2) exp(-pi exp(2t)), t→infinity. (THETA-TAIL)

Indeed the first term is pi exp(5t/2)(2pi exp(2t)-3)exp(-pi exp(2t)); the remaining ones, after dividing by their main term, are dominated by a constant times sum_(n>=2) n^4 exp[-pi(n²-1)exp(2t)], which tends to 0 by domination. Both the rate -log(Phi)/exp(2t)→pi and the unbounded prefactor are used.

### 7.1 Pure positive mixtures

There is no positive measure mu on a>0 such that

    Phi(t)=integral exp(-a cosh(2t))dmu(a)

for all t. mu of infinite total mass is allowed; only the finite value at 0, integral exp(-a)dmu(a)=Phi(0), is required.

Put q=cosh(2t) and d sigma=exp(-a)dmu. Sigma is finite. If it has positive mass below 2pi, some interval a<=2pi-epsilon has positive mass and provides a minorant constant times exp[-(2pi-epsilon)(q-1)]. This contradicts THETA-TAIL, since -log(Phi)/q→2pi. Hence sigma is supported on [2pi,infinity), so that

    Phi(t)<=Phi(0) exp[-2pi(q-1)].

But THETA-TAIL gives exp(2pi q)Phi(t)~2pi² exp(9t/2)→infinity, a contradiction. Positive amplitudes depending on a and normalizations of each model are absorbed into mu; t-dependent factors do not belong to this class.

### 7.2 Convolution with a finite positive measure

For any fixed a>0, there is no nonzero finite positive measure nu on R with Phi=phi_a*nu. nu is not assumed even or compactly supported.

Put S=(1/2)log(a/(2pi)). If nu has mass above S, there is a finite interval [b,c], b>S, of mass m>0. For y in that interval,

    a cosh(2(t-y))
       <=(a/2)exp(2t-2b)+(a/2)exp(-2t+2c).

The contribution of the interval then gives

    limsup_(t→infinity) -log(Phi(t))/exp(2t)
       <=(a/2)exp(-2b)<pi,

contrary to THETA-TAIL. Hence nu is supported on (-infinity,S]. For all such y,

    phi_a(t-y)<=exp[-(a/2)exp(2t-2y)]
               <=exp[-pi exp(2t)].

Integrating proves Phi(t)<=nu(R)exp[-pi exp(2t)], again incompatible with the prefactor of THETA-TAIL. The argument covers unbounded support before deducing its upper restriction.

These exclusions do not affect the model theorem of §5. Nor do they exclude time prefactors, differentiations, signed combinations or other Green potentials. They do not give a negative W nor an inequality for the real kernel. They only prevent using the two previous exact positive representations as an automatic bridge.

## 8. Verified positive operation: affine prefactor and Robin boundary

**PROVED for the extension of the model; real transfer OPEN.** Prior consultation of the three indices and targeted cross-check: the previous appearances of Robin/Neumann in 014, 075, 102 and the arithmetic Neumann series are not this operation on the scale of the model. Independent review. No campaign of prefactors is started.

For fixed a>0 and beta>=0, define

    phi_(a,beta)(t)=[beta+a cosh(2t)]exp[-a cosh(2t)].

Its bilateral transform, with the previous conventions, is

    Z_(a,beta)(u)=beta y_x(0)-y_x'(0), x=u²/4,

since differentiating the integrand of y in r introduces -a cosh v at r=0. The parameters a,beta stay independent of x.

Let m_x=-y_x'(0)/y_x(0)>0 and k_x(r)=y_x(r)/y_x(0). The parametric Wronskian of §3 gives

    partial_x m_x=integral_0^infinity k_x(r)²dr>0.

The operator H_beta has the same expression -D²+a²exp(2r), now with boundary condition f'(0)=beta f(0). Its form is

    integral [|f'|²+a²exp(2r)|f|²]dr+beta|f(0)|²,

so H_beta>=a². The sign of the boundary term is positive. Its Green function is obtained explicitly from the Dirichlet one:

    R_(beta,x)=R_x+[k_x tensor k_x]/(m_x+beta).       (ROBIN)

To check the boundary, partial_r G_x(0,s)=k_x(s), while k_x'(0)=-m_x; hence the right-hand side satisfies partial_r G_(beta,x)(0,s)=beta G_(beta,x)(0,s). The interior jump and the decay are the same. RATIO gives integral k_x²<=1/(2a), and -y_x'/y_x>=a at r=0, so the correction is trace class. Consequently,

    Tr R_(beta,x)=Tr R_x+(partial_x m_x)/(m_x+beta)
      =partial_x log[beta y_x(0)-y_x'(0)].           (ROBIN-TRACE)

Hence M_(a,beta)(u)/u=(1/2)Tr(H_beta+u²/4)^(-1). The GRAM proof of §5 applies unchanged to any number of positive parameters. In the writing as integrals of squares there also appears the nonnegative term

    (beta/2) integral_0^infinity |F(0,s)|²ds.

Beta=0 is the Neumann case and is equivalent, up to the positive factor a, to differentiating the base density with respect to -a. This is a concrete operation whose positivity is proved through the boundary, not a general claim that differentiating or multiplying densities preserves the logarithmic kernel.

The prefactor obtained grows like exp(2t), while that of THETA-TAIL grows like exp(9t/2). The extension does not identify Z_(a,beta) with the real Z, nor does it provide a positive representation of the latter. No sign of W nor new window T is inferred. A construction reproducing the complete theta and keeping the trace representation is missing.

## 9. The scale flow of the model has no matrix order in all sizes

**PROVED, precise auxiliary class and datum.** For each a>0, K_a is the positive kernel of the model of §5. However,

    D_a(u,v)=-a partial_a K_a(u,v), u,v>0,

is NOT PSD in all sizes. This is not claimed for the flow of the real theta. It is proved to test the proposal of integrating a positive matrix derivative from large scales; positivity of all the K_a does not authorize that step.

Prior consultation: indices/grid/crossword and comparison with POWER_SIMULTANEOUS_SHIFT_OBSTRUCTION, 073 and the recorded flows. SHIFT changes the exponents of the test; here the scale of an explicit auxiliary density changes. The covariance comparison of 073 only signs scalar quantities. No novelty is attributed to the abstract computation with moments. Independent mathematical audit; no computations nor arguments about the original function via zeros.

Write V_a(r)=a²exp(2r), H=H_a and R_x=(H+x/4)^(-1), where now x=u². By REP and the resolvent differentiation identity,

    P_a(x):=-a partial_a[M_a(sqrt(x))/sqrt(x)]
           =Tr(R_x V_a R_x).                         (SQUARE-RES)

The factor is 1, since a partial_a H=2V_a and REP contributes 1/2. The identity is valid as a differentiation of forms: 0<V_a<=H and the finite trace of H^(-1) dominate the products. Differentiating eigenvalues is not needed.

The inverse of H is positive, compact and trace class by §4. In an orthonormal basis of its eigenvectors, write H psi_j=lambda_j psi_j and v_j=<psi_j,V_a psi_j>. Then

    0<v_j<=lambda_j,
    P_a(x)=sum_j v_j/(lambda_j+x/4)²,
    sum_j v_j/lambda_j²<=Tr H^(-1)<infinity.

This decomposition concerns only the explicit positive operator of the model. Group, if necessary, the repeated eigenvalues. The smallest value lambda_* has finite multiplicity and is separated from the next distinct value. For |x|<4lambda_* the series is absolutely convergent and

    P_a(x)=sum_(n>=0)(-1)^n A_n x^n,
    A_n=(n+1)sum_j w_j t_j^n,
    w_j=v_j/lambda_j²>0, t_j=1/(4lambda_j).

Put t_*=max t_j, W_*=sum_(t_j=t_*)w_j>0 and rho=(next t_j)/t_*<1. The mass sum w_j is finite, so that

    A_n=(n+1)W_* t_*^n[1+epsilon_n],
    0<=epsilon_n<=C rho^n.

In particular,

    A_n A_(n+2)-A_(n+1)²
      =-W_*² t_*^(2n+2)[1+O(n²rho^n)]<0             (NEG-MOM)

for all sufficiently large n. The negative main factor comes from (n+1)(n+3)-(n+2)²=-1; the exponential rate of the error is necessary to keep it.

On the other hand, D_a(u,v)=[uP_a(u²)+vP_a(v²)]/(u+v). Its coefficient of u^(2i)v^(2j) in the expansion around (0,0) is (-1)^(i+j)A_(i+j). If D_a were PSD for all finite sets of positive nodes, its finite coefficient matrices would be PSD: approximate each derivative by finite differences with strictly positive nodes, divide by the factorials and pass to the limit. Diagonal congruence by (-1)^i would then give

    [A_(i+j)]_ij PSD.

Its minor with indices k,k+1 requires A_(2k)A_(2k+2)-A_(2k+1)²>=0, contrary to NEG-MOM for large k. By continuity of the finite differences there is a FINITE set of positive nodes with D_a indefinite; its size is not computed and no parameter campaign is needed.

Restricted conclusion: the Gram of §5 remains valid for each scale, but its scale derivative does not preserve PSD at all orders. This excludes deducing an automatic matrix monotonicity from that Gram or from positive diagonal covariances. It does not decide the derivative of the theta flow nor the sign of W, and does not exclude a different integrated compensation.

## 10. The fixed prefactor does not produce a scalar potential independent of the parameter

**PROVED, restricted scope.** Proposal and independent review; targeted cross-check in indices, grid, crossword and sources, with no literal antecedent identified and no claim of worldwide priority. The difference from §7 is that here an arbitrary fixed time prefactor is allowed, but the scalar equation in the scale with parameter-independent potential is required to be kept. Other equations and preserving operations are not excluded.

Let q be an even C² function, strictly positive, with |q(v)|+|q'(v)|+|q''(v)|<=C exp(C|v|). For b>0 and real nu define

    Y_nu(b)=integral_0^infinity exp(-b cosh v)q(v)cosh(nu v)dv.

With b=a exp(r), two integrations by parts give exactly

    partial_r² Y_nu=(b²+nu²)Y_nu+F_nu(b),
    F_nu(b)=integral exp(-b cosh v)
              [q''(v)cosh(nu v)+2nu q'(v)sinh(nu v)]dv
           =integral exp(-b cosh v)
              [-q''(v)+2b sinh(v)q'(v)]cosh(nu v)dv.       (FORCE)

The boundary terms vanish because q'(0)=0 and by the double-exponential decay. Suppose that at two distinct scales b1,b2 there exist numbers E(bi), independent of nu, such that F_nu(bi)=E(bi)Y_nu(bi) for all nu in some open real interval. Then necessarily q is constant and E(b1)=E(b2)=0.

Proof: for each fixed b, the cosh transform of

    h_b(v)=exp(-b cosh v)[-q''(v)+2b sinh(v)q'(v)-E(b)q(v)]

is entire in nu by the declared bounds. Its vanishing on an interval implies vanishing also at nu=i tau. The even extension of h_b therefore has zero Fourier transform and is zero. To make the uniqueness used explicit: convolving h_b with any Gaussian writes that convolution as the integral of its zero Fourier transform against another Gaussian (Fubini is absolute); narrowing the Gaussian, the approximate identity recovers h_b. By continuity,

    -q''(v)+2b sinh(v)q'(v)=E(b)q(v)              for all v>=0.

Subtracting the identities for b1,b2 and evaluating at v=0 gives [E(b1)-E(b2)]q(0)=0. Since q(0)>0, both E coincide. For v>0 there remains 2(b1-b2)sinh(v)q'(v)=0: q'=0. Substituting proves E=0. The parameter interval of the carrier suffices; the identity is not originally assumed for imaginary parameters.

Application to the real attempt: a=2pi and q(v)=Phi(v/2)exp(2pi cosh v) give Y_(u/2)(a)=Z_real(u) exactly. Parity and smoothness of Phi make q even and smooth. The first term of the theta series and its two derivatives grow at most exponentially after removing exp(-pi exp(v)); the tail n>=2 and its derivatives are dominated by polynomials in exp(v) multiplied by exp[-pi(n²-1)exp(v)]. Hence q satisfies the above bounds. Moreover §7 gives q(v)~2pi² exp(9v/4), so it is not constant. This family does not satisfy an equation Y''=[b²+nu²+E(b)]Y with E independent of nu on an interval of scales.

A different Green function, an additional transformation, a matrix system or a b-dependent prefactor are not refuted. In particular Robin §8 uses q_b(v)=beta+b cosh(v), which depends on the scale, and does not belong to the excluded class. Nor is a negative sign of the real kernel proved. The compensation of the nu-dependent source still lacks a uniform signed estimate.


### 10.1. Allowing a first derivative: complete classification within this family

**PROVED, independent review; targeted dedup.** Explicit change with respect to §10: an arbitrary coefficient of the first derivative in r is now allowed. The fixed prefactor q, the regularity and growth hypotheses of §10, the coordinate b=a exp(r) and the coefficient ONE of nu² are kept. The same class is not reopened without modifying hypotheses.

Suppose that, for b in an open positive interval and nu in an open real interval,

    Y_rr=A(b)Y_r+[b²+nu²+E(b)]Y,                       (DRIFT)

with A,E independent of nu. Then the only possibilities are

    q(v)=C>0,                  A=0,  E=0;
    q(v)=C cosh(v/2), C>0,     A=-1, E=-b-1/4.

Both do satisfy DRIFT. No positive representation of the second case is claimed here.

Proof. Y_r=-b integral exp(-b cosh v)q(v)cosh(v)cosh(nu v)dv. The uniqueness already justified in §10 turns DRIFT into

    -q''/q+2b sinh(v)q'/q=-b A(b)cosh(v)+E(b).          (D1)

Subtracting D1 at two distinct scales gives constants alpha,beta such that

    2sinh(v)q'/q=alpha cosh(v)+beta.

Evaluating at 0 forces beta=-alpha. For v>0, q'/q=(alpha/2)tanh(v/2); integrating and using continuity at 0 gives q=C cosh(v/2)^alpha. Hence

    q''/q=alpha²/4+(alpha-alpha²)sech²(v/2)/4.

On substituting into D1, all other terms lie in the span of 1 and cosh(v). The function sech²(v/2) does not belong to that span: its limit 0 at infinity forces first the coefficient of cosh to vanish and then the constant. Thus alpha-alpha²=0. Substituting alpha=0 or 1 gives exactly the announced coefficients, and also verifies sufficiency.

The real prefactor of §10 grows like exp(9v/4), incompatible both with a constant and with cosh(v/2). DRIFT is excluded for that real family, even allowing a first derivative.

Also excluded is a nonzero scalar multiplication g(r), C² and independent of nu, turning this Y into z=gY with z_rr=[nu²+V(r)]z: dividing the identity by g one obtains DRIFT with A=-2g'/g and E=V-g''/g-b². This consequence concerns only that multiplication and that coordinate. It does not exclude changes of variable, integral transforms, nu-dependent normalizations, b-dependent prefactors, matrix systems or other Green functions. It is not a refutation of the real sign nor of the relative comparison of forms.


**Extension for the real q: variable spectral weight and change of scale.** Independent review and cross-check. The previous reservation about changes of variable can be withdrawn for the precise operation that follows, not for general transformations. Now suppose Y_rr=A(b)Y_r+[w(b)nu²+B(b)]Y, with coefficients independent of nu. Two integrations by parts transfer nu² to the second v-derivative of exp(-b cosh v)q(v); the uniqueness of §10 gives

    (1-w)b²cosh²(v)+[(w-1)+A]b cosh(v)+wb²-B
       -w q''/q+2wb sinh(v)q'/q=0.                    (WEIGHT)

Coefficients of nu are not compared formally between nu-dependent functions. For real q, its first theta mode writes exactly

    q(v)=2pi² exp(9v/4)exp(pi exp(-v))
          [1-(3/(2pi))exp(-v)+R(v)],

with R and its first two derivatives superexponentially small: they come from n>=2 and keep factors exp[-pi(n²-1)exp(v)] after differentiation. Consequently q'/q=9/4+O(exp(-v)) and q''/q=81/16+O(exp(-v)). Dividing WEIGHT by cosh²(v) and sending v to infinity forces w(b)=1 for each b. The equation returns to DRIFT with E=B-b², impossible for real q by the previous classification.

In particular, if t=h(r) is C² with nonvanishing h' and z(h(r))=g(r)Y(r), g C² nonvanishing, both independent of nu, the equation z_tt=[nu²+V(t)]z would imply

    w=h'^2, A=h''/h'-2g'/g,
    B=h'^2 V(h(r))-g''/g+(g'/g)(h''/h').

WEIGHT forces h'^2=1 and by continuity h'=1 or -1 on each connected interval. There is therefore no repair through this change of scale and scalar multiplication. The result does not classify variable weights for arbitrary q, nor exclude new integral families, parameter-dependent transformations or matrix systems. It does not prove a sign of W nor refute the relative comparison of forms.

## 11. Transfer through products of cosh: exact representation excluded

**PROVED, restricted scope.** Independent mathematical review; transversal search for antecedents in index, grid, crossword and selected sources, without attribution of worldwide bibliographic novelty. The difference from §7 is that now the model may be multiplied in time by positive factors, not mixed or convolved. Unlike §10, no differential equation is required and no assumption is made on how sign preservation would be proved. The exact representation is discarded before attempting that preservation.

There do not exist C>0, a>0 and a finite or countable family of numbers alpha_j>0, with sum_j alpha_j²<infinity, such that for all real t

    Phi(t)=C exp(-a cosh(2t)) prod_j cosh(alpha_j t).   (CP)

The empty product is also excluded. These are factors without shifts and with unit exponent; real powers, quotients, sums or signed combinations are not included.

### 11.1. The scale and the sum of exponents are forced

The inequality 0<=log cosh(x)<=x²/2 ensures convergence of the product on real compacts and

    0<=sum_j log cosh(alpha_j t)<=t² sum_j alpha_j²/2.

The known theta tail gives log Phi(t)/exp(2t)->-pi. Dividing the logarithm of (CP) by exp(2t) forces a=2pi. Let Q(t)=Phi(t)exp(2pi cosh(2t)). Its expansion is

    Q(t)=2pi² exp(9t/2)
          [1+c1 exp(-2t)+O(exp(-4t))],
    c1=pi-3/(2pi),    2<c1<3.                        (TAIL-CP)

To justify the remainder, the mode n=1 contributes exactly

    2pi² exp(9t/2) exp(pi exp(-2t))
        [1-(3/(2pi))exp(-2t)].

The modes n>=2, after dividing by exp(9t/2), are O(exp(-3pi exp(2t))) for t large enough: with y=pi exp(2t)>=1, their absolute values are bounded by a constant times sum_(n>=2)(n^4+n²)exp(-(n²-1)y), and exp(-3y) is extracted. Hence they do not modify the first two coefficients. The bounds 3<pi<22/7 and the monotonicity of x-3/(2x) prove 2<c1<3 without numerical computation.

For each alpha>0, log cosh(alpha t)/t increases to alpha as t increases from 0: the sign of the derivative reduces to x tanh(x)-log cosh(x)>=0, whose derivative is x sech²(x)>=0. Monotone convergence for the series and (TAIL-CP) give

    sum_j alpha_j=lim_(t->infinity) log(Q(t)/C)/t=9/2.

### 11.2. Infinitely many factors do not preserve the leading coefficient

If there were infinitely many factors, the previous sum would allow writing

    exp(-9t/2) prod_j cosh(alpha_j t)
      =prod_j [(1+exp(-2alpha_j t))/2].

All factors belong to (0,1]. For each N, the complete product is at most the product of the first N factors, whose limit is 2^(-N). Making N arbitrarily large, the limit of the complete product is 0. This contradicts (TAIL-CP), which would require the positive limit 2pi²/C.

### 11.3. Finitely many factors require a non-integer multiplicity

There remain m factors, with sum 9/2 and C 2^(-m)=2pi². Let alpha_* be their minimum and k>=1 its integer multiplicity. Dividing by the main term,

    prod_(j=1)^m(1+exp(-2alpha_j t))
      =1+k exp(-2alpha_* t)+o(exp(-2alpha_* t)).

Comparing with (TAIL-CP) forces alpha_*=1 and k=c1. But 2<c1<3, impossible for an integer. This concludes the exclusion of (CP).

**Decision and limits.** One need not decide whether multiplying a model by cosh preserves its kernel to discard (CP): not even a universal preservation would give that representation of Phi. Such preservation has been neither proved nor refuted. Nor are approximations by other classes, relative comparisons of forms, products with real powers or a new joint representation excluded. There is no new sign of W, extension of T nor changes in papers.


### 11.4. Nor is there uniform approximation on compacts at fixed scale (2026-11-06)

**PROVED; independent mathematical and literal audit; targeted cross-check.** Difference from §11: a class of approximations not covered by the discard of exact representations is decided. Consulted the three indices and antecedents; this literal application was not found. The compactness lemma is not presented as a new principle nor as worldwide novelty.

There is no sequence

    phi_n(t)=C_n exp(-2pi cosh(2t)) prod_(j=1)^(m_n) cosh(alpha_nj t),
    C_n>0, alpha_nj>0,

converging to Phi uniformly on each real compact. The scale 2pi is FIXED; the numbers of factors and all their parameters may vary.

**Closure lemma.** If Q_n(t)=prod_j cosh(alpha_nj t) converges locally uniformly to a positive function Q, then

    Q(t)=exp(gamma t²) prod_(j>=1)cosh(alpha_j t),
    gamma>=0, sum_j alpha_j²<infinity.

Zero factors are allowed, omitted from the product. Indeed Q_n(0)=Q(0)=1 and log Q_n converges locally uniformly to log Q. A bound log Q_n(1)<=L gives alpha_nj<=A for a finite A. Since logcosh(x)/x² has limit 1/2 at 0 and is positive on [0,A], there is c>0 with logcosh(x)>=c x² there. Thus sum_j alpha_nj²<=B=L/c.

Order the parameters decreasingly, pad with zeros and extract a diagonal subsequence with alpha_nj→alpha_j for each j and S_n=sum_j alpha_nj²→S. Fatou gives sum_j alpha_j²<=S<=B. Moreover alpha_n,J+1²<=B/(J+1). For each finite T, Taylor with uniform remainder on [-AT,AT] gives

    |logcosh(alpha t)-alpha²t²/2|<=C_T alpha⁴, |t|<=T.

Hence the error of replacing the tail j>J by its quadratic term is at most C_T B²/(J+1), uniformly in n and |t|<=T. Passing first n→infinity, then J→infinity, proves

    log Q(t)=sum_j logcosh(alpha_jt)
             +(t²/2)(S-sum_j alpha_j²).

The series converges uniformly on compacts by logcosh(x)<=x²/2. This proves the lemma, including all quadratic mass that could be lost in the extraction.

**Application to Phi.** If the declared approximants existed, normalizing at t=0 would give

    Q_n(t)→Q(t)=Phi(t)exp(2pi(cosh(2t)-1))/Phi(0).

By §11.1, log Q(t)/t→9/2 as t→infinity. In the representation of the lemma all logcosh summands are nonnegative. Hence gamma>0 is impossible and gamma=0. One obtains an exact representation of Phi as a positive constant times exp(-2pi cosh(2t)) and a cosh product with finite sum alpha_j², contradicting §11.1–11.3.

**Scope.** Only this locally uniform approximation at fixed scale by positive unit products without shifts is excluded. Abstract sign preservation when multiplying by cosh is not decided. Variable scales, real powers, sums, quotients, other topologies without a proved bridge and relative comparisons are not excluded. The result avoids attempting to transfer positivity through this closure; it does not prove a negative sign of Phi nor new positivity of W/T. Papers untouched; no computations.


## 12. A finite vector of fixed prefactors does not absorb the source without a first derivative (2026-11-06)

**PROVED; independent mathematical and literal audit; targeted cross-check.** Difference from §10: arbitrary matrices and any FINITE number of components are allowed, not only a scalar potential. A precise class is kept: b-independent prefactors and no matrix term multiplying Y_r. General systems remain outside this discard.

Let Q(v) be a vector of d even C² functions, with Q,Q',Q'' of at most exponential growth, and Q_1(v)=q_theta(v)=Phi(v/2)exp(2pi cosh v). Define componentwise

    Y_nu(b)=integral_0^infinity exp(-b cosh v)Q(v)cosh(nu v)dv,
    b=a exp(r).

There do not exist two distinct scales b1,b2 and matrices E(b1),E(b2), independent of nu, such that at both scales, for all nu in an open real interval,

    Y_rr=(b²+nu²)Y+E(b)Y.

Proof. The identity FORCE of §10 and uniqueness of the cosh transform, componentwise, force

    -Q''(v)+2b sinh(v)Q'(v)=E(b)Q(v).

Subtracting the equations at the two scales gives

    sinh(v)Q'(v)=B Q(v),
    B=[E(b2)-E(b1)]/[2(b2-b1)],

with B constant. For v>0 put w(v)=log tanh(v/2). We have w'(v)=1/sinh(v), hence dQ/dw=BQ and, for any v0>0,

    Q(v)=exp(B[w(v)-w(v0)])Q(v0).

As v tends to infinity, w(v) tends to 0. The exponential of a finite matrix is continuous, so Q(v) has a finite limit. This contradicts the complete tail q_theta(v)~2pi²exp(9v/4), already justified in §10. There is no need to diagonalize B, assume independence of the components or impose a sign on the matrices.

**Scope.** This closure fails before asking whether the matrix potential would be self-adjoint or positive. Terms A(b)Y_r, b-dependent prefactors, infinite systems, other transformations or other Green realizations are not discarded. It does not prove negativity of K_Phi nor modify the global obligation. No computations, new W/T positivity nor changes in papers.


### 12.1. Adding a matrix first derivative does not close this class either (2026-11-06)

**PROVED; two independent mathematical reviews, literal audit and targeted cross-check.** The cross-check of the three indices and selected primary sources did not locate an earlier literal antecedent, excluding this same entry. E101_070§5 treats a hierarchy without automatic finite-band closure, not this discard for arbitrary matrices via a rational annihilator. No worldwide novelty nor exhaustive rereading of the corpus is claimed. The term A(b)Y_r, expressly excluded from the scope of §12, is now allowed. The prefactors Q remain fixed, the dimension finite and the coefficient of nu² the identity. This is not a discard of general matrix systems.

With the hypotheses and definitions of §12, there also do not exist matrices A(b_i),E(b_i), independent of nu, at two distinct scales, such that

    Y_rr=(b²+nu²)Y+A(b)Y_r+E(b)Y.

**Reduction to a rational system.** Since Y_r is the transform of the vector -b cosh(v)Q(v), FORCE and uniqueness give

    -Q''+2b sinh(v)Q'=-b A(b)cosh(v)Q+E(b)Q.

Subtracting the two scales gives sinh(v)Q'=(C cosh(v)+B)Q, where

    C=-(b2 A(b2)-b1 A(b1))/(2(b2-b1)),
    B=(E(b2)-E(b1))/(2(b2-b1)).

Writing x=exp(v)>1 and Qtilde(x)=Q(log x), we get

    Qtilde_x=R(x)Qtilde,
    R(x)=[C(x²+1)+2Bx]/[x(x²-1)].

R is a regular rational matrix on x>1; this equation automatically raises the regularity to C-infinity. The rational rows r_0=e_1^t, r_(j+1)=r_j'+r_j R satisfy (Qtilde_1)^(j)=r_j Qtilde. The first d+1 rows are dependent over the field R(x). Hence a nonzero scalar rational differential operator would annihilate q_theta(log x). Independence of the components is not assumed.

**The complete series admits no such operator.** The exact theta formula gives

    q_theta(log x)=h(x)g(x),
    h(x)=pi x^(5/4)exp(pi/x),
    g(x)=sum_(n>=1)n²(2pi n²x-3)exp(-lambda_n x),
    lambda_n=pi(n²-1).

Since h'/h=5/(4x)-pi/x² is rational, conjugating the operator by h and clearing denominators would give a nonzero operator

    L=sum_(k=0)^d p_k(x)D_x^k,  p_k polynomials,

annihilating g. Let m be the maximal degree of the nonzero p_k. Termwise differentiation is legitimate on x>=x0>1: each fixed order only introduces factors polynomial in n and x, dominated by the tails exp(-pi n²x). Thus

    0=Lg=sum_(n>=1)P_n(x)exp(-lambda_n x),

with deg P_n<=m+1 and coefficients of polynomial growth in n. For each fixed N, the tail n>N is O(x^(m+1)exp(-lambda_(N+1)x)) when x>=2; extracting that exponential leaves a convergent series of powers of n times exp(-2(lambda_n-lambda_(N+1))).

Isolating the first mode proves P_1=0: an exponentially decaying polynomial is zero. Removing it and repeating gives P_N=0 for all N. However the coefficient of x^(m+1) in P_n is

    2pi n^4 sum_(k:deg p_k=m) lead(p_k)(-lambda_n)^k.

The polynomial in lambda of this expression is nonzero by definition of m. It cannot vanish at the infinitely many distinct lambda_n. Contradiction. The complete arithmetic series is kept throughout the proof; there is no numerical truncation nor argument about zeros of transformed functions.

**Scope.** This finite closure of fixed prefactors is excluded even with a matrix first derivative and arbitrary matrices, without needing self-adjointness or positivity. Outside remain b-dependent prefactors, infinite dimension, matrix spectral coefficient different from the identity and other representations. No negativity of K_Phi, new W/T positivity nor changes in papers.


### 12.2. Infinite dimension: rigidity under two symmetric operators

**PROVED for the declared strong class, 2026-11-06.** Two independent audits PASS. Targeted consultation of the project rules, the three indices, §§12–12.1 and E101_070; additional Hankel/Hilbert search with no literal antecedent located. No bibliographic novelty is claimed. The difference from §12 is allowing an infinite-dimensional Hilbert space and unbounded operators, in exchange for requiring symmetry on a common domain. The finite proof via the matrix exponential does not decide this class.

**Lemma.** Let Q:(0,infinity)->H be a C² function in the norm of a real or complex Hilbert space. Let B,C be symmetric linear operators on a common linear domain D containing all the Q(v). Suppose, as strong identities,

    sinh(v)Q'(v)=B Q(v),       Q''(v)=C Q(v).             (INF-SYM)

Then there exist constants A,c>=0 such that

    ||Q(v)||²=A+c log(cosh v).                           (INF-NORM)

In particular every continuous linear observation ell satisfies |ell(Q(v))|=O(sqrt(1+v)). Boundedness of B or C, self-adjointness, semiboundedness or Q(v) in Dom(B²) are not required.

**Proof.** Put w=log(tanh(v/2))<0 and q(w)=Q(v(w)). Since dw/dv=1/sinh(v), we have q_w=Bq. For K(w,z)=<q(w),q(z)>, symmetry of B gives K_w=K_z. Each segment of constant sum w+z in the negative quadrant is connected; hence K(w,z)=F(w+z), with F C² on (-infinity,0). Hermitian symmetry implies that F is real.

The chain rule gives

    Q''(v)=a(w) q_ww(w)+b(w) q_w(w),
    a(w)=(cosh(2w)-1)/2,
    b(w)=sinh(2w)/2.

Symmetry of C, applied to Q(v(w)) and Q(v(z)), produces

    [cosh(2w)-cosh(2z)]F''(w+z)
       +[sinh(2w)-sinh(2z)]F'(w+z)=0.

For w!=z, divide by 2sinh(w-z) and put s=w+z. Every s<0 admits such a choice; there remains

    sinh(s)F''(s)+cosh(s)F'(s)=0.

Thus F(s)=A+kappa log|tanh(s/2)|. On the diagonal, tanh(w(v))=-1/cosh(v), so ||Q(v)||²=A-kappa log(cosh v). Its nonnegativity for all v>0 forces A>=0 and kappa<=0. Putting c=-kappa proves (INF-NORM). All differentiations are performed on the C² kernel; B is never applied to Q' and no unbounded operator is interchanged with an integral.

**Application to the strong closure without first derivative.** Let b1!=b2 be positive and E1,E2 symmetric on a common domain D. If Q is C² in norm, takes values in D and satisfies

    -Q''+2b_i sinh(v)Q'=E_i Q,   i=1,2,                 (INF-FORCE)

then B=(E2-E1)/(2(b2-b1)) and C=2b1 B-E1 are symmetric on D and satisfy (INF-SYM). Therefore there cannot exist a continuous linear observation ell with

    ell(Q(v))=q_theta(v)=Phi(v/2)exp(2pi cosh v),

since the complete theta tail of §10 is q_theta(v)~2pi²exp(9v/4), incompatible with (INF-NORM).

**Domains and scope.** The result excludes (INF-FORCE) in infinite dimension, even with unbounded operators. To deduce (INF-FORCE) from an integral equation for Y_nu one must additionally justify passing the operator through the integral and the uniqueness of the transform; for example, through suitable integrability in graph norm. That interchange is not declared automatic. Systems with first derivative, non-symmetric operators, non-continuous observations, scale-dependent prefactors, variable metrics or other Green realizations are not excluded. The finite class with drift of §12.1 and this infinite symmetric class without drift have different scopes. This does not refute K_Phi, does not prove a global sign nor extend T. No computations nor changes in papers.


### 12.3. Constant scalar drift: kernel forced by symmetry and parity

**PROVED for the declared strong class, 2026-11-06.** Independent reviews PASS; literal audit PASS. Consulted the project rules, the three indices, §§12–12.2 and the theta cusps of GLOBAL/GRAM§16. Difference from §12.2: a constant scalar first derivative of any sign is allowed, in infinite dimension; even regularity up to the origin is now required. No worldwide novelty is attributed to the kernel method.

**Hypotheses.** Let Q:R->H be even and C² in norm, with values in a common linear domain D of symmetric operators B,C. For some fixed real alpha suppose

    sinh(v)Q'(v)+alpha cosh(v)Q(v)=B Q(v),
    Q''(v)=C Q(v).                                      (DRIFT-SYM)

It suffices to require it for v>=0: parity extends the identities. Neither boundedness nor self-adjointness of the operators is assumed. Let A=||Q(0)||².

**Exact kernel.** For real v,z, necessarily

    <Q(v),Q(z)> = (A/2)[cosh((v+z)/2)^(-2alpha)
                         +cosh((v-z)/2)^(-2alpha)].      (DRIFT-K)

To prove it, symmetry of C implies K_vv=K_zz. The condition Q'(0)=0 gives K_z(v,0)=0, and d'Alembert with f(v)=<Q(v),Q(0)> provides K(v,z)=[f(v+z)+f(v-z)]/2. Moreover f is even and real: K(v,0)=K(0,v), together with hermiticity. Symmetry of B gives

    sinh(v)K_v-sinh(z)K_z
                    +alpha(cosh(v)-cosh(z))K=0.

With x=v+z, y=v-z positive, dividing by sinh(x/2)sinh(y/2) reduces this equality to H(x)+H(y)=0, where H(x)=coth(x/2)f'(x)+alpha f(x). The identity holds for any x>y>0; by continuity as y tends to x, H(x)=0. Solving f'=-alpha tanh(x/2)f with f(0)=A gives f=A cosh(x/2)^(-2alpha), proving (DRIFT-K).

**Vector continuation, not only scalar.** The right-hand side of (DRIFT-K) has a holomorphic extension in two variables to the product of strips |Im v|,|Im z|<pi/2. The branches of logcosh continued from the real axis are taken; cosh has no zeros there. This analytic kernel forces Q to be analytic in norm. In detail, the inner products of finite difference quotients are computed with K; differences of quotients are Cauchy by the derivatives of the kernel, successively providing Q^(n). The Cauchy estimate on a bidisc of radius R<pi/2 centred at a real point r gives

    ||Q^(n)(r)/n!|| <= sqrt(M_R) R^(-n),

since the square of that norm is the mixed coefficient (n,n) of the kernel. The Hilbertian Taylor series converge, agree with Q on the real axis by the identity of their inner products and glue together on the strip. Polarizing and continuing (DRIFT-K) gives, for Z=X+iY, |Y|<pi/2,

    ||Q_hol(Z)||²=(A/2)[cosh(X)^(-2alpha)
                                  +cos(Y)^(-2alpha)].   (DRIFT-HOL)

It is not claimed that the formula is a positive kernel for all alpha: if Q exists, its positivity and this identity are necessary consequences. No unbounded operator is applied to the complex continuation.

**Incompatibility with the theta observation.** If alpha>=0, (DRIFT-K) on the real diagonal bounds ||Q(v)||² by A. This prevents ell(Q(v))=q_theta(v) for any continuous linear functional ell, because q_theta(v)~2pi²exp(9v/4).

If alpha<0, (DRIFT-HOL) stays bounded with X=log2 and Y tending to pi/2 from below. The observation ell(Q_hol(Z)) must also stay bounded. But the real equality with q_theta continues holomorphically. For w=exp(Z)=2i+zeta, the complete Poisson computation in GLOBAL, «The diagonal at the two cusps», proves

    Phi(Z/2)=w^(5/4)[(3i/2)zeta^(-5/2)+E(zeta)],
    |E(zeta)|<=C |zeta|^(-M) exp(-b/|zeta|)

on a sector around the positive real half-axis. The path Z=log2+iY enters that sector, with arg zeta tending to 0. The factor exp(2pi cosh Z) has a finite nonzero limit. Hence |q_theta(Z)| diverges, contradicting (DRIFT-HOL). The EVEN cusp w=2i is used: the alternating cusp w=i does not serve, since the theta decays there. Thus no real alpha allows the theta observation in this class.

**Relation with FORCE and limits.** Two strong identities

    -Q''+2b_i sinh(v)Q'
        =-2alpha b_i cosh(v)Q+E_iQ,   b1!=b2,

with E_i symmetric on D produce (DRIFT-SYM), taking B=(E2-E1)/(2(b2-b1)), C=2b1B-E1. They correspond to the attempt Y_rr=(b²+nu²)Y+2alpha Y_r+E(b)Y, only when the interchanges and domains needed to obtain FORCE have been justified. FORCE is not inferred formally from that integral equation. The discard concerns even fixed prefactors, CONSTANT scalar drift, symmetry on a common domain and continuous observation. Outside remain scale-dependent or genuinely operatorial drift, variable metrics, other representations and non-continuous observations. No negativity of K_Phi nor global positivity is obtained; no computations, new window T or changes in papers.


### 12.4. The scale-dependent scalar drift is forced to be constant

**PROVED for the declared strong class, 2026-11-06.** Independent audits PASS, including a literal review. Consulted the project rules, the three indices and §§10.1, 12–12.3. The scalar classification of §10.1 did not cover observations of an infinite Hilbertian vector. Compared with §12.3, different values of the first-derivative coefficient at two scales are now allowed; neither symmetry nor the common domain is modified.

Let Q:(0,infinity)->H be C² in norm, not identically zero, with values in a common linear domain D of symmetric E1,E2. Let b1,b2>0 be distinct and a1,a2 real. Suppose strong FORCE:

    -Q''+2b_i sinh(v)Q'=-b_i a_i cosh(v)Q+E_iQ,
    i=1,2.                                             (VAR-FORCE)

Then NECESSARILY a1=a2. For this conclusion alone neither parity nor extension to the origin is needed.

**Proof.** With Delta=b2-b1, define

    alpha=(b2 a2-b1 a1)/(2Delta),
    B=(E2-E1)/(2Delta), C=2b1 B-E1,
    beta=b1 b2(a1-a2)/Delta.

B,C are symmetric on D. Subtracting and substituting (VAR-FORCE) gives

    sinh(v)Q'+alpha cosh(v)Q=BQ,
    Q''=CQ+beta cosh(v)Q.                               (VAR-SYS)

Put w=logtanh(v/2)<0, q(w)=(sinh v)^alpha Q(v). Then q_w=Bq. By symmetry of B, as in §12.2, <q(w),q(z)>=F(w+z), with F real C². The computation of the second derivative is

    Q''/(sinh v)^(-alpha)
       =sinh²(w) q_ww+(2alpha+1)sinh(w)cosh(w) q_w
                       +[alpha(alpha+1)sinh²(w)+alpha²]q.

Since cosh v=-coth w, the symmetry of C applied to (VAR-SYS), and the hyperbolic difference identities, give for w!=z and s=w+z

    sinh(s)[F''(s)+alpha(alpha+1)F(s)]
       +(2alpha+1)cosh(s)F'(s)
       = beta F(s)/(sinh(w)sinh(z)).                    (VAR-ID)

B or C is not applied to a derivative of Q; derivatives are taken only on its C² kernel. For fixed s<0, one can vary d=w-z with |d|<-s. The denominator is

    sinh(w)sinh(z)=[cosh(s)-cosh(d)]/2>0,

which takes different values for two nonzero d of different absolute value. The left-hand side of (VAR-ID) depends only on s. Hence beta F(s)=0 for each s<0. Since Q is not identically zero, there is w0 with F(2w0)=||q(w0)||²>0. Thus beta=0 and a1=a2.

**Consequence for theta and scope.** If moreover Q is even C² up to 0 and a continuous linear observation produces q_theta, the equality a1=a2 reduces exactly to §12.3, which gives a contradiction. Hence, in this strong symmetric construction, an arbitrary scalar drift a(b) does not allow the theta observation either: two scales already suffice to force equality of its values. Continuity of a(b) is not assumed.

As a corollary, a nonzero REAL scalar multiplication g(r), C² and independent of nu, in the SAME coordinate r=log(b/a), cannot transform this Y into Z=gY with Z_rr=[nu²+V(r)]Z and V symmetric on the common domain either: undoing it produces the scalar drift -2g'/g and E=V-g''/g-b²I. This corollary presupposes, like the previous sections, the justification of FORCE from the integrals; it does not obtain it formally for unbounded operators. It does not exclude genuinely operatorial drift, change of coordinate with variable spectral weight, variable metrics, b-dependent prefactors, non-continuous observations or other representations. No global sign, new window T, computations or changes in papers.


**Control of the operatorial scope of §12.4 (2026-11-06).** Independent algebraic check. Targeted consultation of the three indices and §§12.1–12.4. The scalar reduction does NOT extend automatically to a symmetric operator D in sinh(v)Q'+cosh(v)DQ=BQ, Q''=CQ. An exact example is

    Q(v)=(1,2cosh v), C=diag(0,1), D=diag(-4,-1),
    B=[[0,-2],[-2,0]].

The first identity has both sides (-4cosh v,-2); the second is immediate. B,C,D are symmetric and [B,D]!=0, with full domains in dimension 2. The kernel K=<Q(v),Q(z)> still satisfies K_vv=K_zz, but the other identity contains L=<DQ(v),Q(z)>:

    sinh(v)K_v-sinh(z)K_z+(cosh(v)-cosh(z))L=0.

L cannot be replaced by alpha K. This example does not contain q_theta, so it neither contradicts §12.1 nor proves a positive opportunity for theta. For Y_rr=(b²+nu²)Y+2DY_r+(-C+2bB)Y, the gauge Z=exp(-rD)Y leaves V=b²I+D²+exp(-rD)(-C+2bB)exp(rD). Its cross entries are -4b exp(3r) and -4b exp(-3r): the potential is not symmetric in the usual metric except at r=0. Hence no positive Green function is obtained from this example. Other metrics and the general operatorial drift are not discarded; their compatible construction, semiboundedness and the trace identity representing the target kernel are missing. Only the scope of the scalar discard is verified, with no global sign, computations or changes in papers.


**Local metric for the previous example: repair impossible (2026-11-06).** Independent audit PASS. Targeted cross-check of the project rules/three indices/§12.4: the repair by metric is decided for THAT example, not for other systems. For L=-partial_r²+2D partial_r+b²I+E(b), with D,E symmetric and D constant, a Hermitian matrix metric M(r)>0 of class C² makes L formally symmetric on compact tests if and only if

    M'=-DM-MD,             [E(b)+D²,M]=0.

The conditions are obtained by comparing the first-derivative and zero-order coefficients after integrating by parts. The first forces M=exp(-rD)M0 exp(-rD), M0>0 constant. In the gauge Z=exp(-rD)Y the second is equivalent to M0V=V* M0, with V=b²I+D²+exp(-rD)E exp(rD).

For the example Q=(1,2coshv), D=diag(-4,-1), C=diag(0,1), B with cross entries -2, write M0=[[a,c],[conj(c),d]]. Here V has diagonals b²+16,b² and cross entries -4bexp(3r),-4bexp(-3r). The Hermitian condition imposes c real and

    -4ab exp(3r)+4db exp(-3r)-16c=0.

Since b=a0exp(r), a0>0, the functions exp(4r), exp(-2r), 1 are linearly independent on any open interval. They force a=d=c=0, incompatible with M0>0. There is therefore no such positive LOCAL matrix metric for this example, not even on an open interval. The leading coefficient -I is not modified and no new connection is added. Non-local metrics or other B,C,D are not excluded; semiboundedness or global sign are not inferred. No computations nor changes in papers.


**Comparison update, 2026-11-06.** GLOBAL, «Closure of the small hyperbolic comparison», refutes K_Phi>=epsilon K_(2pi) for all epsilon>0 through the first mode of H and a certified physical theta integral. This does not alter the positivity of the model proved here nor exclude other models; global sign OPEN. See proof, three audits and reproducible certificate there.


### 12.5. The operatorial drift also determines a wave kernel

**PROVED in the declared regular class, 2026-11-07.** Independent check and audit PASS. Targeted cross-check all3 and §12.4: the equation for the kernel with insertion D is recorded there; here that equation is solved without replacing D by a scalar. That is the explicit difference from the scalar discards. No worldwide priority nor positivity of theta is claimed.

Let Q:R->H be even, C4 in norm. Suppose Q(v) lies in a common domain of symmetric operators B,C,D, that v->DQ(v) is continuous in norm, and

    Q''(v)=C Q(v),
    sinh(v)Q'(v)+cosh(v)D Q(v)=B Q(v).

Put K(v,z)=<Q(v),Q(z)>, F(t)=K(t,0), L(v,z)=<DQ(v),Q(z)>. L is a Hermitian kernel with insertion of a symmetric operator; PSD of L or positivity of D is NOT presupposed.

Symmetry of C gives K_vv=K_zz and parity gives K_z(v,0)=0. The wave formula is

    K(v,z)=[F(v+z)+F(v−z)]/2.

F is even C4. Symmetry of B and D gives

    (cosh(v)−cosh(z))L(v,z)=sinh(z)K_z(v,z)−sinh(v)K_v(v,z).

With X=v+z, Y=v−z, the right-hand side is

    −cosh(X/2)sinh(Y/2)F'(X)
    −sinh(X/2)cosh(Y/2)F'(Y).

Dividing by 2sinh(X/2)sinh(Y/2) proves, off the diagonals,

    L(v,z)=[G(v+z)+G(v−z)]/2,
    G(t)=−coth(t/2)F'(t),   G(0)=−2F''(0).

The singularity is removable: F'(t)/t=integral_0^1 F''(st)ds, of class C2, and coth(t/2)−2/t is smooth and odd near 0. Hence G is even C2. Continuity of L extends the identity to v=±z. In particular

    L_vv=L_zz.

**Operatorial reading only under additional hypotheses.** If also Q(v) belongs to Dom(DC), DQ(v) to Dom(C), and v->Q(v) is C2 in the graph norm of D (so that (DQ)''=DQ''), the wave equality implies

    <DCQ(v),Q(z)>=<DQ(v),CQ(z)>=<CDQ(v),Q(z)>.

Thus <[D,C]Q(v),Q(z)>=0 for all v,z. Without density of the span of Q, vector vanishing of the commutator is not deduced; even with it, strong commutation of unbounded operators is not deduced. No operators are applied to derivatives without these hypotheses.

**Scope.** The second kernel is not a free datum: it is determined by F and satisfies another wave equation. This restricts a compatible operatorial construction, but does NOT realize B,C,D for theta, does NOT produce a metric or a positive Green function and does NOT sign A. The previous example Q=(1,2cosh v) satisfies the formula: F=1+4cosh v, G=−4(1+cosh v), L=−4−4cosh v cosh z. The general operatorial possibility remains OPEN. No web, numerical computations nor modifications of papers.


### 12.6. Explicit operatorial realization with exact theta observation

**PROVED as a realization, not as a sign, 2026-11-07.** Independent audit PASS and second review. Consulted the project rules, all3, §§12.4–12.5 and GLOBAL. Concrete difference: §12.5 only imposed necessary identities on Q,B,C,D; here those objects, their domains and a continuous observation that is exactly theta are constructed. No scalar drift is used; no worldwide priority is attributed. The metric and the positive Green function remain unconstructed.

**Space and vectors.** For omega>=0 put rho(omega)=sech(pi omega/2), and lambda_j=j+1/4, j=0,1,2. Work in the real space

    H=L²((0,infinity),rho(omega)domega) direct-sum R³,
    Q(v)=(cos(omega v), cosh(lambda_0 v),cosh(lambda_1 v),cosh(lambda_2 v)),
    F(t)=sech(t)+sum_(j=0)^2 cosh(lambda_j t).

The cosine formula integral_0^infinity rho(omega)cos(omega t)domega=sech(t) has normalization integral rho=1. The product identities give

    <Q(v),Q(z)>=[F(v+z)+F(v-z)]/2.

Q is even and C^infinity in norm. Define C as multiplication by -omega² on the continuum and by lambda_j² on the masses, on its maximal domain; it is self-adjoint and Q''=CQ.

**Construction of D.** Define G(t)=-coth(t/2)F'(t), with the singularity removed. The identities

    -coth(t/2)(sech t)'=sech t+sech²t,
    coth(t/2)sinh(t/4)=cosh(t/4)-(1/2)sech(t/4),
    coth(t/2)sinh(5t/4)=cosh(5t/4)+2cosh(t/4)-(1/2)sech(t/4),
    coth(t/2)sinh(9t/4)=cosh(9t/4)+2cosh(5t/4)+2cosh(t/4)-(1/2)sech(t/4)

give G with masses (-29/4,-23/4,-9/4) and cosine density

    sigma(omega)=rho(omega)+omega/sinh(pi omega/2)+(15/2)sech(2pi omega).

We use integral_0^infinity [omega/sinh(pi omega/2)]cos(omega t)domega=sech²t and the scaled sech formula. All are absolutely convergent integrals (also at omega=0 by continuity).

Hence define D on its maximal domain as the multiplier

    d(omega)=sigma/rho
      =1+omega coth(pi omega/2)+(15/2)cosh(pi omega/2)/cosh(2pi omega)

together with the three previous masses. D is self-adjoint, d=O(1+omega), and

    <DQ(v),Q(z)>=[G(v+z)+G(v-z)]/2.

The exponential tails of rho justify all derivatives in the graph norms of C,D,CD,DC. In this concrete realization C and D are simultaneous multipliers and DCQ=CDQ; this is not inferred from an abstract weak commutation.

**Construction and domain of B.** Let S=span{Q(v):v>=0}. Define linearly

    BQ(v)=sinh(v)Q'(v)+cosh(v)DQ(v).

It is well defined: for distinct nonnegative v_i, a finite relation among the Q(v_i) would imply sum c_i cos(omega v_i)=0 on an interval of omega, and independence of exponentials forces c_i=0. To prove density of S, a vector orthogonal to all Q(v) would give a bounded cosine transform (Cauchy–Schwarz and integral rho=1) plus three cosh of distinct positive rates. Growth as v->infinity successively eliminates the three masses; Fourier uniqueness eliminates the continuous component.

The identities K,L of §12.5, verified here through the explicit F,G, give

    <BQ(v),Q(z)>=<Q(v),BQ(z)>.

Thus B is densely defined and symmetric on S, and hence closable. It is not declared self-adjoint. S is contained in the domains of C,D and contains all the Q(v); invariance of S under C or D is not assumed.

**Exact observation, including the whole theta tail.** Put

    q_theta(t)=Phi(t/2) exp(2pi cosh t),
    d_(9/4)=2pi², d_(5/4)=2pi³-3pi, d_(1/4)=pi^4-3pi²,
    H_theta(t)=q_theta(t)-2sum_j d_(lambda_j)cosh(lambda_j t).

On each substrip |Im t|<=b<pi/2, the mode n=1 gives, as Re t->infinity,

    q_theta(t)=2pi²exp(9t/4)+(2pi³-3pi)exp(5t/4)
                   +(pi^4-3pi²)exp(t/4)+O_b(exp(-3Re t/4)).

The modes n>=2 have the factor exp(-pi(n²-1)exp(t)) and are bounded uniformly by a superexponential tail on those substrips. Parity handles the other end. Subtracting the cosh adds their decreasing branches, so the CORRECT bound is

    H_theta(t)=O_b(exp(-|Re t|/4)),

not exp(-3|Re t|/4). H_theta is even, real on R and holomorphic on |Im t|<pi/2.

With the convention k(omega)=pi^(-1)integral_R H_theta(t)exp(-i omega t)dt, Fourier inversion gives H_theta(v)=integral_0^infinity k(omega)cos(omega v)domega. Shifting the contour to Im t=-pi/3 for omega>=0 (the vertical sides vanish by the previous bound) proves |k(omega)|<=C exp(-pi omega/3). Consequently

    integral_0^infinity |k|²/rho < infinity,

since the integrand is O(exp(-pi omega/6)). The vector h=(k/rho, 2d_(lambda_0),2d_(lambda_1),2d_(lambda_2)) belongs to H and defines an exact continuous observation

    <Q(v),h>=q_theta(v),  v real.

**Strict scope.** Q,B,C,D and the theta observation have been realized, including the domains required by §12.5. No metric making the complete energy positive was constructed, nor a positive Green identity reproducing A. The scalar observation does not automatically transfer positivity of the Gram of Q to the target kernel. Global OPEN. No web, numerical computations nor changes in papers.


**Integral realization and strong equation (same result, independent audit PASS).** For b>0, real nu and r=log b, define

    Y_nu(b)=integral_0^infinity exp(-b cosh v)cosh(nu v)Q(v)dv.

The norms of Q,Q',CQ,DQ,BQ are bounded by C exp(13v/4), enlarging C when necessary. The superdamping exp(-b cosh v) allows integrating in the graphs of C,D and of the closure Bbar; Riemann sums in S justify the passage to the closed graph of Bbar. It also allows all b-derivatives locally on b>0 and in the required graphs. The sum of operators is not assumed self-adjoint.

Put w=exp(-b cosh v). Two integrations by parts transfer the second derivative of cosh(nu v) to wQ. The boundary terms at 0 vanish because Q'(0)=w'(0)=(cosh(nu v))'_(v=0)=0, and at infinity by the same superdamping. Thus

    nu²Y=CY-2b integral w sinh(v)Q'(v)cosh(nu v)dv
             +integral w[b²sinh²(v)-b cosh(v)]Q(v)cosh(nu v)dv.

On the other hand Y_rr has integrand w[b²cosh²(v)-b cosh(v)]Q(v)cosh(nu v). Substituting sinh(v)Q'=BQ-cosh(v)DQ proves the strong equality

    Y_rr=(b²+nu²)Y+2D Y_r+(-C+2b Bbar)Y.

The continuous observation constructed above satisfies exactly

    <Y_nu(2pi),h>=integral_0^infinity Phi(v/2)cosh(nu v)dv=Z(2nu),
    Z(a)=integral_R exp(at)Phi(t)dt.

Hence the realization reproduces the complete theta datum and its equation, with domains and interchanges justified. A metric and a POSITIVE Green identity signing A are still missing; this equality does not prove them. Reviews PASS.


### 12.7. The realization 12.6 admits no compatible bounded positive local metric

**PROVED in the declared class, 2026-11-07.** Independent constructions; audit PASS of graph limits, coefficients and scope. Consulted all3 and §12.4. There a metric was discarded for a 2-dimensional example without theta observation; here the exact realization 12.6 is studied, in infinite dimension, and diagonality of the metric is NOT imposed. The mechanism of comparing exponents has antecedent 12.4; it is not a new tool.

**Class.** M(r) is a bounded, strictly positive self-adjoint operator on H for each r in an open interval I, with sufficient local regularity in operator norm for the integrations by parts (C² suffices). Neither a bounded inverse nor commutation with C or D is required. Metrics are sought for the operator of 12.6, with leading coefficient -I and without adding connections, satisfying the necessary compatibility conditions, in forms on S and their graph limits:

    M'=-DM-MD,
    E(r)=-C+D²+2b Bbar is symmetric in the product M(r),
    b=b_0 exp(r), b_0>0.

The first equality is understood weakly: <M' u,v>=-<M Du,v>-<M u,Dv>. The second is <M Eu,v>=<M u,Ev>, without applying E to Mu. These are the conditions of §12.4 derived by integration by parts, when the products and limits are justified; the following proof shows directly that no M satisfies them. The statement is not extended to unbounded metrics or metrics non-local in r.

**Two vectors accessible in the graph.** Write e_j for the three discrete vectors. The explicit formula for BQ(v) has continuous part of norm O(exp v), because omega and d(omega) belong to L²(rho). Its three coordinates are

    (BQ)_0=-(7/2)cosh(5v/4)-(15/4)cosh(3v/4),
    (BQ)_1=-(9/4)cosh(9v/4)-(7/2)cosh(v/4),
    (BQ)_2=-(9/4)cosh(5v/4).

Dividing Q(v) by cosh(9v/4) and letting v->infinity proves in the joint graph of Bbar,C,D² that

    e_2 belongs to Dom(Bbar), Bbar e_2=-(9/4)e_1.

Then subtract cosh(9v/4)e_2 and divide by cosh(5v/4). The continuous part O(exp v) of BQ vanishes in that limit; we get

    e_1 belongs to Dom(Bbar), Bbar e_1=-(7/2)e_0-(9/4)e_2.

The vectors using e_2 are approximated from S by diagonal selection in the same graphs. For e_0 only approximation in the graph of D is needed, subtracting both larger masses and dividing by cosh(v/4). B is NOT applied to e_0. Boundedness of M,M' allows passing the metric identities to those limits.

**Contradiction without diagonalizing M.** The discrete eigenvalues of D are

    d_0=-29/4, d_1=-23/4, d_2=-9/4.

The metric equation on pairs e_i,e_j forces, writing M_ij=<M e_i,e_j>,

    M_ij(r)=m_ij exp(-(d_i+d_j)r).

Moreover (-C+D²)e_1=(63/2)e_1 and (-C+D²)e_2=0. Hence

    E e_2=-(9/2)b e_1,
    E e_1=(63/2)e_1-7b e_0-(9/2)b e_2.

Symmetry of E applied to the pair e_2,e_1 gives exactly

    b[-9M_11+14M_20+9M_22]-63M_21=0.

After substituting the solution for M_ij, the r-exponents of the four terms are, respectively, 25/2, 21/2, 11/2, 8. They are distinct, so their linear independence on any open interval forces m_11=m_22=0 (it also kills the other two coefficients). This contradicts <M e_j,e_j>>0. The entries mixing continuum and masses have not been assumed zero: they simply do not enter this pair of identities.

**Scope.** The exact realization 12.6 remains valid. What fails is turning ITS equation, with the declared leading coefficient and connection, into a symmetric energy through a bounded positive local metric of this class. Non-local metrics, unbounded metrics with other domains, new connections and other realizations are not excluded. No negativity of A nor global sign is obtained. No web, numerical computations or changes in papers.


## 13. Shifted cosh products: the real bound forces an entire extension

2026-11-07. **PROVED in the declared class; independent mathematical audit PASS and second review PASS.** Prior novelty filter PASS after targeted cross-check of Paper48, the three indices and primary sources. Antecedents: §§11–11.4 (products without shifts) and §12.3 (even cusp). Allowing variable c removes the integer-multiplicity obstacle of §11.3. The difference examined is the closure of this enlarged class; the following argument uses holomorphic normality instead of classifying all limit products. No worldwide novelty is attributed to the compactness principle nor to the cusp.

**Class.** For each n, let

    Q_n(z)=prod_(j=1..m_n) (cosh(b_nj z)-c_nj)/(1-c_nj),
    b_nj>0, -1<c_nj<1, m_n finite.

Empty products are allowed. If Q_n converges uniformly on real compacts to Q, then Q is the restriction of an entire function. In particular it cannot be

    q_theta(t)=Phi(t)/Phi(0) * exp[2pi(cosh(2t)-1)].       (SHIFTED-Q)

**1. A single real bound controls all factors.** Convergence implies Q_n(1)<=M for some M>=1, uniform in n. Put

    d_nj=(cosh(b_nj)-1)/(1-c_nj)>=0.

Since prod_j(1+d_nj)>=1+sum_j d_nj, we get sum_j d_nj<=M-1. Moreover 1-c_nj<2 implies cosh(b_nj)-1<=2(M-1). Hence b_nj<=B:=arcosh(2M-1). If M=1, all products are empty and the conclusion is immediate.

**2. Uniform complex bound.** For |z|<=R and 0<b<=B, the cosh series gives

    |cosh(bz)-1| <= (b²R²/2)cosh(BR),
    cosh(b)-1 >= b²/2.

Consequently, with C_R=R²cosh(BR),

    |Q_n(z)| <= prod_j(1+C_R d_nj)
               <= exp[C_R(M-1)].                       (ENTIRE-BOUND)

There is no need for 1-c_nj to be bounded away from zero: its effect is already included in d_nj.

**3. Entire limit and identification.** The bound on each disc and the Cauchy bounds give a subsequence converging uniformly on every complex compact to an entire function F (diagonal extraction over discs). On the real axis F=Q by the assumed convergence. This subsequence suffices; complex convergence is not presumed from real convergence without the previous bound.

**4. Specific incompatibility with theta.** SHIFTED-Q is holomorphic on |Im t|<pi/4. If it coincided there with an entire function, the identity principle would extend the equality from the real axis. Take

    Z=log(2)+iY, t=Z/2, Y->pi/2 from below,
    w=exp(Z)=2i+zeta.

The expansion at the even cusp already proved in §12.3, with its Poisson source in GLOBAL, gives

    Phi(Z/2)=w^(5/4)[(3i/2)zeta^(-5/2)+E(zeta)],
    |E(zeta)|<=C |zeta|^(-K) exp(-beta/|zeta|), beta>0,

on the sector containing this path. Its modulus diverges. The factor exp[2pi(cosh Z-1)] has a finite nonzero limit and Phi(0)>0. Thus |q_theta(Z/2)| diverges when approaching the FINITE point (log2)/2+i pi/4, which contradicts F being entire.

**Consequence for approximants of the profile.** There is no sequence

    phi_n(t)=C_n exp[-2pi cosh(2t)] Q_n(t), C_n>0,

converging to Phi uniformly on real compacts. Indeed phi_n(0)=C_n exp(-2pi) converges to Phi(0)>0; dividing by this value and removing the fixed base would produce Q_n->q_theta. Infinite products of this class defined as locally uniform limits of their partial products are also excluded.

**Scope.** Only FIXED base scale 2pi, real factors with b>0 and -1<c<1, finite products or their real locally uniform closure. Whether an isolated factor preserves PSD of A_phi is not decided. Variable base scales, other multipliers, sums, quotients, real powers or comparisons of forms are not excluded. It is a discard of this approximation before investing work in sign preservation; it does not prove A negative, does not sign A and does not extend T. No numerical computations, web nor changes in papers.


### 13.1. The variable positive scale is also bounded

2026-11-07. **PROVED in the declared class; independent audit PASS and second review PASS.** Prior filter PASS after targeted cross-check of all3/Paper48 and primary sources. Difference from §13: allowing a_n->infinity destroys its initial bound on Q_n(1). The following three-value inequality controls that escape without presupposing convergence of derivatives.

**Statement.** Nor is there a real locally uniform approximation of Phi by

    phi_n(t)=C_n exp[-a_n cosh(2t)] Q_n(t), C_n>0, a_n>0,

with the same products Q_n of §13, even if a_n varies without a prior bound.

**1. Concavity in the square of the variable.** For -1<c<1 define f_c(x)=log[(cosh x-c)/(1-c)]. On x>0,

    x f_c''(x)-f_c'(x)
      =[x-sinh(x)cosh(x)+c(sinh(x)-x cosh(x))]/(cosh(x)-c)².

Since sinh(x)-x cosh(x)<0, the numerator is at most its value at c=-1, which is (1+cosh x)(x-sinh x)<0. By the chain rule, the second derivative of f_c(b sqrt(s)) has the sign of x f_c''(x)-f_c'(x), x=b sqrt(s), for s>0. At s=0 the extension is smooth by the even series and 1-c>0. Thus s->log Q_n(sqrt(s)) is concave on [0,infinity).

**2. Three values bound the scale.** Put H(s)=cosh(2sqrt(s)) and

    delta=H(0)+H(2)-2H(1)>0.

Strict positivity follows from H(s)=sum_(k>=0) 4^k s^k/(2k)!: the terms k=0,1 have zero difference and the terms k>=2 have positive difference. With L_n(s)=log phi_n(sqrt(s)), the previous concavity gives

    L_n(0)+L_n(2)-2L_n(1) <= -a_n delta,
    0<a_n<=[2L_n(1)-L_n(0)-L_n(2)]/delta.              (SCALE-BOUND)

If phi_n->Phi locally uniformly on R, their values at 0, 1, sqrt(2) converge to positive values. Hence the right-hand side stays bounded and there is A<infinity with 0<a_n<=A for all n. Convergence of phi_n is not differentiated.

**3. Recovery of normality and contradiction.** Since Q_n(0)=1,

    Q_n(1)=phi_n(1)/phi_n(0) * exp[a_n(cosh2-1)],
    C_n=phi_n(0)exp(a_n).

Both sequences are bounded. The bound ENTIRE-BOUND of §13 again gives local complex boundedness of Q_n. Moreover, on |z|<=R,

    |exp[-a_n cosh(2z)]|<=exp[A cosh(2R)].

Consequently phi_n is a locally bounded family of entire functions. A subsequence converges on complex compacts to an entire function that agrees with Phi on R. The even cusp at (log2)/2+i pi/4, used in §13, contradicts that extension. This proves the statement.

**Updated scope.** The reservation of §13 is withdrawn only for variable POSITIVE scales a_n in the SAME base cosh(2t), with the declared factors and convergence. It does not cover frequency changes of that base, parameters c outside (-1,1), other factors, sums, quotients, real powers or comparisons of forms. It does not decide preservation of PSD by factors nor the sign of A. No numerical computations, web, new window T nor changes in papers.
