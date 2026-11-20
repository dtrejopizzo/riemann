# Audit111 — individual monotonicities and TP2 parametric sign

Status: **Base source and extensions approved mathematically and literally.** Source: `POWER_GREEN_PAIR_TP2_SCOPE_111.md`. No new computations or data. Papers untouched.

The difference with respect to 074/101 and 091/105 is the generic implication from ALL the individual monotonicities Vp/K to the fixed sign of the parametric minors. The REAL theta compatibility is not used, nor is it claimed that the abstract object satisfies it.

## Exact solution and minors

Verified: lambda_p=2−1/(2coshp), the two formulas Vp, their values and derivatives at 1, and the boundaries Vp'(0)=Vp(2)=Vp'(2)=0. The even compact extension is C1, with no δ in the second-order operator. The interior force is −A, the exterior one B. Vp>0 and Vp'<0 for ALL p>0 on 0<t<2; the quotient is not used outside the support.

For q>p, the ratio decreases on 1<t<2 by the logarithmic derivative q coth(qδ/2)−p coth(pδ/2)>0 with δ=2−t. For p1,q2 on 0<t<=.5, the exact formula of the ratio and F(z,c) are correct. The step c>1.5 requires ∂cF=4(c−z)>0, valid for z<=8/7<c; hence F>=23/98>0. The same params 1,2 give two minors of opposite signs at the four fixed nodes, not a numerical test. It is neither TP2 nor sign-regular of order 2 after reversing an axis.

The smooth regularization only preserves signs of fixed minors and local monotonicities for 1,2. The source does NOT assume global all-p after mollifying. Its class enclosure is bounded and honest.

## Extension with strictly increasing r

For r_epsilon=1+step_(t>1)+epsilon t², K=1_(|t|<2), epsilon>0, λ is still the cosh average. On (0,2), W=Vepsilon' satisfies (D²−p²)W=δ1+2epsilon t and W(0)=W(2)=0. The Dirichlet Green function is

`−sinh(p min(t,s)) sinh(p(2−max(t,s)))/(p sinh(2p))<0`.

Thus W<0 for ALL p>0 and Vepsilon(t)=−integral_t^2W>0. The even extension by zero is C1, while r_epsilon is strictly increasing on the common interior. The two minors depend continuously on epsilon and are strict at epsilon0; therefore opposite signs persist for epsilon>0 small enough. It is an existence statement, not an explicit numerical cutoff epsilon. No smooth compact density with global all-p properties is claimed. The counterexample is still not REAL Phi/W.

Final complete reading of §5.1/5.2 approved. The strict extension and the option of smoothing only the interior step keep all-p while K remains an indicator; the source does not promote the smoothing of both densities to a global all-p hypothesis. The existence of delta>0 by continuity is expressly non-numerical. No pending items remain for audit111.

## Proposed extension — complete monotonicity in the parameter

Mathematical proof and final literal reading of §5.3 APPROVED. For x=p², q_x=−derivative_tV_x solves A_xq_x=mu, A_x=−D²+x, Dirichlet 0 at 0,2 and mu=Dirac1 (plus 2delta tdt in the strict variant). The positive Green kernel is continuous, with analytic dependence on x>0 and with uniform derivatives for x in compacts. Thus the interchange with the finite measure mu is legitimate, including Dirac; no nonexistent regularity of the source is presupposed.

Put q_n=(−1)^n derivative_x^nq_x. Differentiating A_xq_x=mu gives A_xq_n=nq_(n−1), with Dirichlet 0 boundaries. Positivity of the Green function and a nonzero initial source imply q_n>0 on the whole interior for ALL n. V_x(t)=integral_t^2q_x(s)ds allows interchanging the derivatives on the finite interval. Then V_x(t) is strictly completely monotone in x>0 for interior t. The opposite TP2 minors of 111 remain the same: CM in the parameter, plus all-p individual monotonicities, does not imply TP2. CM of the REAL family is not claimed, nor is a method using more structure excluded.

The final version of §5.3 was read with the convention q_n=partial_x^n q_x: the recurrence A_xq_n=−nq_(n−1) and the alternating signs are correct. The fixed Dirac measure does not obstruct differentiating the Green function; the compactness and boundary arguments are explicit. No audit items remain pending for the extension.
