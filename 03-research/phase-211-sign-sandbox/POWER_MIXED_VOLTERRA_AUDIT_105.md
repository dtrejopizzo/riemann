# Audit105 — raw mixed Volterra kernel

Status: **Mathematical proof and literal reading of the source APPROVED.** No new computations. Papers untouched.

Cross-checked against103 (CT3 and mixed prefixes), the complete jets088/095 and091 (Peano). The object105 is a Volterra kernel for the time slope, distinct from the Peano cofactor quotient091. The scope is only the candidate positivity of the RAW kernel, not every Volterra representation, gauges, mixed W4 or W.

## Exact identity

With p=V',q=V'',r=V''', tau=J/Phi, kappa=K/Phi, E=−tau'>0, S=kappa'/tau'>0, w=−S'>0, D=tau S−kappa, X=tp−1 and Y=p²−q, start from

`kappa''−2p kappa'+Y kappa=a−tau`.

Use kappa'=−SE, tau'=−E and E'=1−q tau+pE. Differentiating yields exactly

`E w'+(2−2q tau)w+X'S−Y'D=E`.

Thus B=(2−2q tau)/E, R=X'/E,T=Y'/E and w'+Bw+RS−TD=1. No derivatives or boundary terms are omitted.

CT3 gives S strictly decreasing; kappa/tau is its tail average and tends to0, hence S(infinity)=0. Then S=int_t^infinito w; D'=−tau w and D(infinity)=0 give D=int_t^infinito tau(s)w(s)ds. The integral term is the kernel R(t)−T(t)tau(s), s>=t.

## Real sign change of the kernel

The complete theta jets give p→infinity, q/p→2 and r/p²→0. For tau(t)=int_0^infinito(t+h)Phi(t+h)/Phi(t)dh, change u=p(t)h. Convexity of V dominates the normalized integrand by(1+u)e^(−u), for pt>=1. The jets give pointwise convergence of the exponent to u; thus tau p/t→1 by domination, without differentiating a real O.

Then `[X'−tau Y']/(tp)→2−4=−2`. The diagonal numerator is negative for large t and, by continuity in s, also for some s>t. For fixed t, tau(s)→0 and X'(t)=p+tq>0 imply a positive kernel when s is sufficiently large; T>0 need not be assumed for that step. The raw kernel is not nonnegative on its whole domain. None of this determines the sign of the signed integral, w', mixed W4, particular U or W.

Complete final reading of `POWER_MIXED_VOLTERRA_OBSTRUCTION_105.md` approved: intermediate identity Ew+XS−YD=a−tau, boundary terms of S/D, absolute Volterra integrability and the DOMCONV step all correct. The sign change is proved for s>t, not only on an excluded diagonal. No audit items remain pending for this source.
