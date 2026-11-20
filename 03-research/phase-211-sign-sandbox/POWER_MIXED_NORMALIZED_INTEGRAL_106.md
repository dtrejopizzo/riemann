# POWER_MIXED_NORMALIZED_INTEGRAL_106 — Uniform holomorphic control for the mixed system

Status: **ANALYTIC LEMMA PROVED; independent audits approved. GLOBAL SIGN OPEN.** No new theta datum, point, quadrature or run. The final execution budget remains PENDING. Uniform control of domain and errors is proved to enable a certificate, not positivity of the Wronskian. Papers untouched.

## 1. Consultation and precise difference

Consulted the project rules, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked077/089/093/095/099/103/104 and the Volterra obligations of105. The object is the EVEN mixed system[K,J,Phi,J''], sufficient for the next REAL crossing of103, not the stronger odd system093/095 nor the condition T_h already closed in099.

104 only proves the sign at the origin without radius and for t>=64. Here that test is not repeated and no new preservation is claimed. A different difficulty is resolved: the normalized integrals are made holomorphic with bounds independent of the superexponential amplitude of Phi and with explicit tails. This allows evaluating jets DIRECTLY, avoiding that an error in initial values is amplified when propagating a stiff ODE.

Keep p=−Phi'/Phi,a=M'(0),0<a<1,

    J(z)=int_z^infinito sPhi(s)ds,
    K(z)=int_z^infinito(s−z)[aPhi(s)−J(s)]ds,
    tau=J/Phi, kappa=K/Phi, X=zp−1=J''/Phi.

The integral identities are understood first on reals; their holomorphic continuation is justified below. The bound a<1 is already contained in the complete certificates098/103; a is not estimated via new data.

## 2. Phi and Theta do not vanish on a uniform strip

Let

    S={z: Re z>=−1/16, |Im z|<=1/16},
    y=pi exp(2z), Y=|y|,
    Theta(y)=sum_(m>=1)m²(2m²y−3)exp[−(m²−1)y].

Phi(z)=pi exp(5z/2)exp(−y)Theta(y). The bounds pi>3,exp(−1/8)>7/8 and cos(1/8)>31/32 give

    Y>21/8,
    Re y>(31/32)Y>5/2.

Write Theta(y)=(2y−3)(1+Rtheta(y)). For all m>=2,

    |m²(2m²y−3)/(2y−3)|
       <=m^4(2Y+3)/(2Y−3)<4m^4.

The terms m^4 exp[−(5/2)(m²−1)] have ratios less than1/2 from m=2: (3/2)^4 exp(−25/2)<1/2 suffices. The exponential series gives exp(5/2)>8. Hence the COMPLETE tail satisfies

    |Rtheta|<128exp(−15/2)<1/4.                 (ZERO-FREE)

Thus neither Theta nor Phi vanishes on S. The argument uses no samples, truncations without remainder nor a lower bound of real Phi informally transferred to complex.

Also, for w=y+v,v>=0 real, |w|>=Y,Re w>5/2. The same proof applies to Theta(w). In particular

    |Theta(y)|>9Y/14,
    |Theta(w)|<55|w|/14,
    |Theta(y+v)/Theta(y)|<(55/9)|y+v|/Y
                            <7|y+v|/Y.         (THETA-RATIO)

This form with |y+v| allows cancelling the Jacobian exactly in the next bound; |y+v| is not improperly replaced by Y+v in a complex denominator.

## 3. Exact normalized integrals with tail exp(−v)

Set, for v>=0,

    r(z,v)=(1/2)Log(1+v/y),
    A(z,v)=exp(−v)(1+v/y)^(5/4)
              Theta(y+v)/[2(y+v)Theta(y)].

Log and the power use the principal branch. They are holomorphic in z inside the strip: Re(1+v/y)>0, Re(y+v)>0 and ZERO-FREE excludes the denominators. Moreover

    |r(z,v)|<=v/[2 Re y]<v/Y.

The inequality is obtained by integrating1/(y+s) from0 to v; it does not assume the complex logarithm to be ordered.

For real z, the EXACT change v=y(z+s)−y(z) transforms the anticausal tail, with ds=dv/[2(y+v)]. Fubini for K gives

    tau(z)=int_0^infinito (z+r)A(z,v)dv,
    kappa(z)=int_0^infinito [a r−(z+r)r²/2]A(z,v)dv. (NORMALIZED)

The second formula uses

    K(z)=a int_0^infinito sPhi(z+s)ds
            −(1/2)int_0^infinito(z+s)s²Phi(z+s)ds.

For complex z it is not claimed that a change of variable in a horizontal integral automatically produces real v. One proceeds by analytic identity: both expressions of NORMALIZED coincide on the real axis; the right side is holomorphic on S and locally dominated by the integrable bound of§4. The left side is too, by the entire primitives and ZERO-FREE. By analytic identity they coincide on the connected strip. This avoids an unjustified contour deformation.

The factor exp(−v) is independent of y. No ratio of two almost-zero quantities exp(−pi exp(2t)) is computed and no small tail is subtracted from global moments.

## 4. Uniform column bounds and complete v tail

THETA-RATIO implies exactly

    |A(z,v)|<7/(2Y) exp(−v)(1+v/Y)^(5/4)
             <=7/(2Y) exp(−v)(1+v)^2.

For bounded |z|, NORMALIZED is dominated by integrable functions independent of z. Use

    int_0^infinito(1+v)^2exp(−v)dv=5,
    int_0^infinito v(1+v)^2exp(−v)dv=11,
    int_0^infinito v²(1+v)^2exp(−v)dv=38,
    int_0^infinito v³(1+v)^2exp(−v)dv=174.

One obtains, with all tails included,

    Y|tau(z)|<(7/2)(5|z|+11)<100(1+|z|),
    Y²|kappa(z)|<(7/2)(98+19|z|)<1000(1+|z|). (COLUMN)

For |z|<65, the same pointwise estimates of the integrand give

    Y |integrand_tau|<512 exp(−v)(1+v)^5,
    Y²|integrand_kappa|<512 exp(−v)(1+v)^5.

When using centre constants Yc=pi exp(2c),c in[0,64], and |z−c|<=1/32, Yc/Y<16/15<2 and(Yc/Y)^2<2. The conservative common bound

    2048exp(−v)(1+v)^5

may be used for BOTH integrands scaled by Yc and Yc². If L=512 is fixed, the complete tail of those functions is less than

    2048exp(−512)sum_(j=0)^5 binom(5,j)513^(5−j)j!
      <2^62 exp(−512)<2^(−450).                 (V-TAIL)

The finite sum is less than2*513^5<2^51; exp1>2 pays the last inequality. It is a uniform holomorphic bound, not an observed value. Cauchy on the disc of radius1/32 turns V-TAIL into coefficient errors<=2^(−450)32^j for the direct jets. Those jets must not be obtained by propagating uncertain initial values via an ODE.

## 5. Complete mode tail and its effect on the integrated function

Let Theta16 be the sum m=1,...,16 and T16=Theta−Theta16. At either argument w=y or y+v of§3,

    |T16(w)|<=8*17^4 |w| exp(−720).

The consecutive ratio for m>=17 is less than(18/17)^4exp(−175/2)<1/2. Dividing by the lower bound9|w|/14 of Theta gives the conservative bound

    |delta(w)|=|T16(w)/Theta(w)|<2^(−698).       (MODE-TAIL)

We used17^4<2^17 and exp1>2; the prefactor8*14/9 is less than16. Theta16 does not vanish either, since Theta16=Theta(1−delta).

Replacing Theta by Theta16 in both factors of the quotient changes A by less than4*2^(−698)|A|. By the integrable estimates of§4, the TOTAL function error for Yc tau and Yc² kappa, before truncating v, is less than2^(−675). The bound is deliberately conservative: integrating2048exp(−v)(1+v)^5 costs less than2^20. By Cauchy its coefficient errors at a centre are<=2^(−675)32^j.

To also complete the local column X, set p16=2y−5/2−derivative_z logTheta16(y). Since delta(y(z)) is holomorphic on S with modulus less than2^(−698), |log(1−delta)|<2^(−697). Cauchy of radius1/32 around each z in|z−c|<=1/32 stays in S and gives

    |p−p16|<2^(−692),
    |(X−X16)/Yc|<2^(−687), X16=zp16−1.

We used|z|<65,Yc>3. Its coefficient error is<=2^(−687)32^j, and hence the conservative bound2^(−675)32^j covers ALL non-constant columns. The real mode tail is not differentiated informally.

These bounds pay for ALL omitted modes in numerator and denominator. It is not enough to add an error only to the numerator nor to treat an approximation of the denominator as if it were exact. V-TAIL and MODE-TAIL are distinct errors and are added before asking for a sign.

## 6. Cauchy budget of the Wronskian and removable origin

This step is a bound, not a closed execution design. For c in[0,64] keep the scales Yc²,Yc,1,Yc^(−1) constant and define the four columns

    [Yc² kappa,Yc tau,1,X/Yc].

Their Wronskian is Yc² Wmixed/Phi^4. On |z−c|<=1/32, COLUMN gives bounds2^17 and2^13 for the first two. For the first column the precise factor (Yc/Y)^2<(16/15)^2 is kept: 1000*66*256/225<2^17; it is not replaced here by the coarser bound2. ZERO-FREE and Cauchy for log(1+Rtheta) on a disc of radius1/32 inside S give |p|<10Y, hence |X/Yc|<2^10. On the inner disc|z−c|<=1/64, each derivative of order j<=3 costs at most j!64^j<2^21. The constant column has zero higher derivatives. The bound of24 products provides

    |Yc² Wmixed/Phi^4|<2^108<2^120.             (W-BOUND)

By parity, the four quotients are even holomorphic near0; their Wronskian has a zero of order at least6. The function

    F_c(z)=Yc² Wmixed(z)/[Phi(z)^4 z^6]

is holomorphic after removing that zero. On |z−c|<=1/128, if |z|>=1/256, W-BOUND gives |F_c|<2^168. If |z|<=1/256, then c<=3/256 andYc²/pi²<2. Applying the maximum principle to Wmixed/[Phi^4 z^6] on the circle|z|=1/128, where W-BOUND with centre0 holds, gives again

    |F_c(z)|<2^168.                             (REGULARIZED-BOUND)

This is a possible uniform Cauchy budget to remove the t^6 cancellation at the origin. Neither degree nor number of final panels has been chosen yet, nor has a lower bound of the sign on the compact been proved.

## 7. Pending execution and controls that cannot be omitted

The future design must fix, BEFORE data, a rigorous quadrature for the finite integral v in[0,512], tolerances and limits, precision, jet order, time partition and Taylor remainder bound. If acb.integral is used, the callback must respect analytic: only declare holomorphy when the balls prove Re(y+v)>0 and Re(1+v/y)>0, with Theta16(y) separated from0; otherwise it must return a non-finite value and allow rigorous subdivision. Constants and branches will be audited before execution.

The change to a normalized integral does not prove that the sign is positive. Nor does the internal subdivision of a rigorous quadrature decide a family of parameters: it must be applied only to the fixed compact obligation. No new quadrature, jet, sample or probe was executed for this source. GLOBAL SIGN and preservation remain OPEN.

## 8. Extension: fixed vector quadrature with complex control

Status: **ANALYTIC LEMMA PROVED; independent mathematical review approved before data.** It is a tool for the future program, not the execution of107 nor a sign certificate. The normalized columns and the domain of this source are reused. The consultation of the three indices and of104–106 did not find this quadrature budget; none of their data is re-evaluated.

Split the integration variable into the TEN intervals

    [0,1], [1,2], [2,4], ..., [256,512].

For each, let b be its centre, h its half-width and R=2h. On the complex disc |v-b|<=R, the first interval has Re v>=-1/2 and |v|<=3/2. The remaining ones have b=3h, Re v>=h and |v|<=5h. In all of them Re(y+v)>2. For 0<=s<=1 one moreover verifies

    Re(1+s v/y)>4/5.

Indeed, the minimum of Re(v/y) is (b cos(arg y)-2h)/Y. On the first disc it is larger than -1/5 using cos(arg y)>31/32 and Y>21/8; on the others it is positive. Hence the principal branch and the denominators are holomorphic on these discs, and

    |r(z,v)| <= 5|v|/(8Y) < |v|/Y.

For w=y+v, Re w>2 and |w|>2. The absolute sum gives

    |Theta16(w)| <= (7/2)|w| sum_(m>=1) m^4 exp[-2(m^2-1)]
                  <7|w|.

The sum is less than2: the first term is1, the term m=2 is less than1/4 and the subsequent ratios are less than1/2. By MODE-TAIL,

    |Theta16(y)|>9Y/28.

Consequently the coupled quotient, including the Jacobian, satisfies

    |Theta16(y+v)/[(y+v)Theta16(y)]|<22/Y.

With |z|<65 and the constant scales Yc,Yc^2 of§4, the TWO truncated integrand functions, for tau and kappa respectively, are bounded by

    4096 exp(-Re v)(1+|v|)^5.

For example, using Yc/Y<2 and (Yc/Y)^2<2, their polynomial factors are bounded by 22(65+u)(1+u)^2 and 22[u+(65/2)u^2+u^3/2](1+u)^2, with u=|v|; both are less than4096(1+u)^5. This estimate is for Theta16, so it can be used directly to bound the quadrature error. The complete mode errors of§5 are added separately.

On the first disc the bound is less than2^20. On the others, h>=1/2, 1+5h<=7h and h^5 exp(-h)<=5!=120, so

    4096 exp(-h)(1+5h)^5 <=4096*7^5*120<2^34.

Thus M=2^34 is a common majorant. For any real centre t in[0,64], Cauchy in the time variable, with radius1/32, bounds the time coefficient of order j of the integrand by

    M_j=2^34*32^j.

The argument is also uniform for the coefficients on a real subinterval of half-width at most1/64, with scales fixed at its centre c. The discs of radius1/32 around its points lie in |z-c|<=3/64, inside S; there Yc/Y<2 and (Yc/Y)^2<2, and |z|<65. This explicitly pays for the width of the parameter, without reusing a local bound outside its domain. Uncertain initial values are not propagated via an ODE.

On each v interval, use Gauss–Legendre with64 nodes and positive weights. Its exactness up to degree127 allows comparing both the integral and the quadrature with the Taylor polynomial of degree127 at b. At the nodes and on the interval, the remainder of that Taylor polynomial is at most M_j(h/R)^128/(1-h/R). The integral costs2h times that bound and the sum of quadrature weights is also2h. Hence the analytic error per interval is

    4h M_j (1/2)^128/(1-1/2)=8h M_j 2^(-128).

Since the sum of all half-widths is256, the total error for coefficient j is

    2^(-83+5j),
    in particular <=2^(-68) for j=0,1,2,3.       (GAUSS-ERROR)

This proof uses no numerically estimated derivative error and does not assume that the integrand is real for complex parameters. It uses only holomorphy, the majorant, polynomial exactness and positive weights. The implementation must rigorously enclose nodes and weights: the local API `arb.legendre_p_root(64,k,weight=True)` provides those balls. Their rounding errors are propagated by interval arithmetic and are ADDITIONAL to the analytic error above, not informally absorbed into it.

The640 total nodes allow evaluating together the time jets of order0 to3. Before forming the Wronskian, GAUSS-ERROR, the v and mode tails, and all arithmetic errors must be added; to obtain derivatives, multiply the coefficients by their factorials. The complete design of the time partition, the treatment of the origin, the precision and the execution limits remain pending. No theta evaluation nor sign test has been executed for this extension.
