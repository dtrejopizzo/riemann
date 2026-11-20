# POWER_GREEN_PAIR_TP2_SCOPE_111 — Individual monotonicities insufficient for TP2

Status: **PROVED analytically; independent mathematical and literal audits approved.** Auxiliary compact counterexample to a precise generic implication. It is not the real theta pair. No computation is run and no paper is modified.

Extension of section 5.3: the same family is completely monotone in x=p^2 for each fixed t; mathematical argument approved, independent audit of that extension pending. This additional condition does not imply TP2 either.

## 1. Consultation, class and difference from the real program

Consulted: the project rules, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md and CROSSWORD-TO-D.md; cross-checked 074/083/091/101/103/105. The specific search for `sinh(px0)`, `sinh(pL)`, `Vp/K`, `V_p/K`, `ratio individual`, `monotonías individuales` and `Green compacto` in the three indices and the POWER corpus did not find this falsifier.

074/101 study sufficiency of potential inequalities for kernels of divided sums; 091/105 study signs of concrete auxiliary kernels. Here another implication is considered: if an even pair J,K has J/K nondecreasing and ALL its balanced Green functions V_p are positive and V_p/K strictly decreasing, is the family V(p,t) TP2? The counterexample satisfies these three conditions for ALL p>0, but produces order-2 minors of both signs with the SAME two parameters.

The declared class allows even, bounded, compact, piecewise smooth densities, positive in the interior of a common support; the Green functions are even C1 and satisfy the global equation in the distributional sense with no deltas. The initial construction has J/K nondecreasing, and an analytic perturbation preserves all individual monotonicities for ALL p while making J/K strictly increasing. LOCAL stability of the two signs under smooth regularization of both densities is also proved for two fixed parameters; global monotonicity for all parameters after that second regularization is not claimed.

It is essential that the REAL compatibility J'=-tPhi, K''=aPhi-J is not part of this class; this example does not satisfy it. Neither MIXED4 nor its analogue is imposed. No induction using these specific properties is refuted, nor the real family of 103, nor the all-orders goal. Only replacing them by the three generic conditions indicated is excluded.

## 2. Pair, balance and exact global solution

Fix, with no parameters to search for,

    K(t)=1_(|t|<2),
    J(t)=[1+1_(1<|t|<2)]K(t).

They are even, bounded functions with support [-2,2]. On the interior t>=0, J/K equals 1 up to 1 and 2 afterwards: it is nondecreasing. For p>0 define the average and the Green function exactly as in 103:

    lambda_p=[int_0^2 cosh(ps)J(s)ds]
                  /[int_0^2 cosh(ps)K(s)ds]
             =2-1/[2cosh(p)],
    V_p(t)=(1/p)int_|t|^2 sinh[p(s-|t|)]
                            [J(s)-lambda_p K(s)]ds
             for |t|<=2,
    V_p(t)=0 for |t|>=2.

The formula for lambda uses sinh(2p)=2sinh(p)cosh(p), and guarantees the exact cosh balance. Put B_p=1/[2cosh(p)] and A_p=1-B_p. The force equals -A_p on 0<t<1 and B_p on 1<t<2. Integrating its two parts gives

    V_p(t)=[A_p-B_p cosh(pt)]/p^2,       0<=t<=1,
    V_p(t)=B_p[cosh(p(2-t))-1]/p^2,      1<=t<=2. (EXPLICIT)

The two formulas and their first derivatives agree at 1; V_p(2)=V_p'(2)=0 and V_p'(0)=0. The even extension by zero is therefore C1, compact, and satisfies on ALL of R

    V_p''-p^2V_p=J-lambda_p K.

There are no deltas at 0,1,2 nor at their reflections: V_p and V_p' are continuous at those points. The equation is also verified directly piecewise.

## 3. Positivity and individual monotonicity for ALL parameters

On 1<t<2, EXPLICIT gives V_p>0 and

    V_p'(t)=-B_p sinh[p(2-t)]/p<0.

On 0<t<1,

    V_p'(t)=-B_p sinh(pt)/p<0.

Since V_p(1)>0 and it decreases up to that point, it is also positive before 1. The derivatives at 1 agree and are negative. Thus, for ALL p>0,

    V_p(t)>0 and (V_p/K)'(t)=V_p'(t)<0
      on the WHOLE interior 0<t<2.                 (INDIVIDUAL)

The quotient is not defined outside the support, where both densities vanish. INDIVIDUAL is a global statement on the common interior, not a check at a few points.

## 4. Two fixed parameters and minors of both signs

For any q>p>0 and 1<t<2, put delta=2-t. The factors B_q/powers are positive and independent of t, and

    V_q/V_p=positive_constant
                *[cosh(q delta)-1]/[cosh(p delta)-1].

The logarithmic derivative with respect to delta is

    q coth(q delta/2)-p coth(p delta/2)>0.

The inequality follows from z coth(z) being strictly increasing for z>0: its derivative is [sinh(z)cosh(z)-z]/sinh(z)^2>0. Hence V_q/V_p DECREASES in t on all of 1<t<2.

To show that reversing the orientation does not suffice, now fix p=1,q=2. For 0<t<=1/2, put c=cosh(1), z=cosh(t) and c2=2c^2-1. EXPLICIT and the double-angle identity give

    V_2/V_1=[c/(2c2)]*[c2-z^2]/[2c-1-z].

The denominator is positive. The sign of its derivative with respect to z is that of

    F(z,c)=z^2-2(2c-1)z+2c^2-1.

We have c>3/2 and 1<=z<=cosh(1/2)<8/7. The last bound comes from the positive Taylor expansion: cosh(1/2)<=1+1/8+(1/384)/(1-1/120)<8/7. Since derivative_c F=4(c-z)>0,

    F(z,c)>F(z,3/2)=z^2-4z+7/2
              >=F(8/7,3/2)=23/98>0.

Thus V_2/V_1 INCREASES on 0<t<=1/2. The same two parameters therefore produce

    det[[V_1(1/4),V_2(1/4)],
         [V_1(1/2),V_2(1/2)]]>0,

    det[[V_1(3/2),V_2(3/2)],
         [V_1(7/4),V_2(7/4)]]<0.                 (OPPOSITE-MINORS)

The family is not TP2, nor is it sign-regular of order 2 after reversing the orientation of one axis. Changing the coordinate p to x=p^2 does not alter the signs, because it is strictly increasing.

## 5. Strictly increasing quotient J/K and local stability

### 5.1. Perturbation preserving the individual monotonicities for ALL p

If J/K is required to be strictly increasing, keep K=1_(|t|<2) and, for delta>0, define

    J_delta(t)=[1+1_(1<|t|<2)+delta t^2]K(t).

Its quotient r_delta=J_delta/K is strictly increasing on 0<t<2, with a positive jump at 1. Define lambda_(delta,p) by the same cosh average and V_(delta,p) by the same anticausal Green function. The boundaries are still V'(0)=V'(2)=0, since the first comes from the cosh balance and the second from the terminal integral.

Put W=V_(delta,p)' on the open interval (0,2). The exact equation, in the distributional sense inside that interval, is

    W''-p^2W=2delta t+delta_1,
    W(0)=W(2)=0,

where delta_1 denotes the Dirac mass of weight 1 at t=1, not the parameter delta. The Dirichlet Green function of this problem is

    G_D(t,s)=-sinh[p min(t,s)]sinh[p(2-max(t,s))]
                     /[p sinh(2p)]<0

for 0<t,s<2. Integrating against the positive measure 2delta s ds+delta_1 gives W(t)<0 for ALL 0<t<2 and ALL p>0. Since V_(delta,p)(2)=0, also V_(delta,p)>0 on that interior. Thus r_delta is strictly increasing and V_(delta,p)/K remains strictly decreasing for ALL parameters, not only the two used in the minors.

For p=1,2 and the four fixed times, V_(delta,p) depends continuously on delta: the average lambda and the force are affine in delta, and the same holds for the Green function. Therefore the two minors of OPPOSITE-MINORS keep their signs for all delta>0 small enough. No numerical value needs to be chosen or searched for. This variant proves that the lack of strict growth of J/K does not explain the counterexample.

One can also smooth only the INTERIOR step of r_delta, keeping K an indicator: choose a smooth nondecreasing transition near 1 and keep delta t^2. Then r_delta'>0 for t>0, the same Dirichlet Green function proves W<0 for ALL p, and the two minors persist by continuity for a narrow enough transition. This does not smooth the compact boundary of K nor produce a pair positive on all of R.

### 5.2. Smoothing both densities: only local stability is claimed

Take an even nonnegative mollifier with support [-epsilon,epsilon] and integral 1, and define K_epsilon as its convolution with 1_[-2,2]. Then K_epsilon is smooth, even, nonnegative, equals 1 on |t|<=2-epsilon and has support [-2-epsilon,2+epsilon]. Choose an even smooth function r_epsilon, nondecreasing for t>=0, approximating 1+1_(|t|>1), with transition inside 1-epsilon<|t|<1+epsilon, and put J_epsilon=r_epsilon K_epsilon.

J_epsilon,K_epsilon converge to J,K in L1 with any fixed exponential weight; their supports stay in [-3,3] for small epsilon. For p=1 and p=2, the averages lambda_p converge and the Green functions converge in local C1 by domination of sinh and cosh on that compact set. Therefore the two strict minors of OPPOSITE-MINORS keep their signs for epsilon small enough.

Moreover K_epsilon=1 on neighbourhoods of the four chosen points. The strictly negative derivatives of V_1,V_2 there remain negative by C1 convergence; the individual monotonicities are preserved LOCALLY on those neighbourhoods for those two parameters. Positivity of the regular Green functions follows from the same negative/positive crossing and cosh balance.

It has not been proved that V_(epsilon,p)/K_epsilon is globally decreasing on the WHOLE support for ALL p simultaneously. Hence the regularization is not used to claim a falsifier of a stronger smooth class. Its role is only to show that the opposite strict minors do not depend on evaluating at a discontinuity.

### 5.3. The family is also completely monotone in x=p^2

This extension uses no new data. It refers to the indicator K and the original J, or to J_delta of 5.1; it does not attribute this property to the real pair. Write

    V(x,t)=V_(sqrt(x))(t), q_x(t)=-partial_t V(x,t), x>0.

On the interval (0,2), the Dirichlet argument of 5.1 gives

    (-D_t^2+x)q_x=mu,
    q_x(0)=q_x(2)=0,
    mu=Dirac_1 for the original example,
    mu=Dirac_1+2delta t dt for J_delta.

mu is a nonzero positive measure, independent of x. The Green function of the operator -D_t^2+x with these boundaries is the NEGATIVE of the G_D written in 5.1, so it is strictly positive in the interior. We have q_x>0.

The dependence on x is smooth: it can be seen directly in the explicit Green function, whose denominators are nonzero for x>0, on any compact set of x. This allows differentiating under the integrals against the finite measure mu and then integrating in t. Let q_n=partial_x^n q_x. Differentiating the equation n times, keeping the same boundaries, gives the elementary recurrence

    (-D_t^2+x)q_n=-n q_(n-1), n>=1,
    q_n(0)=q_n(2)=0.

By induction and the positive Green function,

    (-1)^n q_n(t)>0
       for ALL n>=0, x>0, 0<t<2.

Since V(x,2)=0,

    V(x,t)=int_t^2 q_x(s)ds,
    (-1)^n partial_x^n V(x,t)
       =int_t^2 (-1)^n q_n(s)ds>0
       for ALL n>=0, x>0, 0<=t<2.             (COMPLETE-MONOTONICITY)

Thus PARAMETRIC complete monotonicity of unbounded order also holds in this counterclass. The two opposite minors of section 4 remain for the original example and, by continuity, for the strict variant of 5.1. Therefore adding complete monotonicity in x to the individual positivities and monotonicities does not imply TP2 of the family in (x,t).

COMPLETE-MONOTONICITY has been neither proved nor refuted for the real densities of 103. Nor is it claimed that complete monotonicity is equivalent to TP of all orders, or that it is useless in an argument using more structure. Only the concrete generic implication towards TP2 is refuted here, even under that additional parametric requirement.

## 6. Scope of the limited NO-GO

The refuted implication is only: compact even pair with J/K nondecreasing (even strictly increasing), all Green functions V_p positive and all quotients V_p/K decreasing on the common interior, EVEN ADDING complete monotonicity of V in x=p^2 for each fixed t, IMPLIES TP2 of the parametric family. The hypotheses hold exactly and the two opposite minors are analytic, with no numerical data. The strict variant uses existence by continuity of a small enough positive delta, not a numerical choice presented as explicit.

The pair is not the real Phi/J/K and does not satisfy the program's differential compatibility nor its specific four-density comparisons. No failure of the real route 103 is inferred, no previously proved sign is withdrawn, and no impossibility of building a cone with more structure is claimed. No certificate or campaign was run.
