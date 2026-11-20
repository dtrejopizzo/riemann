# POWER_STATE_075 — Positive density of the Schur denominator

Status: **PROVED/APPROVED**, source POWER_THETA_SCHUR_DENSITY_075.md and independent audit POWER_THETA_SCHUR_DENSITY_AUDIT_075.md. Analytic proof; no new numerical parameters or matrices. Papers untouched.

## Specific result

`POWER_THETA_SCHUR_DENSITY_075.md`, `POWER_THETA_SCHUR_DENSITY_AUDIT_075.md` and `POWER_STATE_075.md`. For the REAL Phi of073, Z(z)=∫Phi(x)e^(zx)dx, u>0,c=M(u),a=M'(0), the denominator D_u=zcZ−uZ' admits the explicit positive representation H_u(z)=D_u(z)/[z(z²−u²)]=∫Phi_u(x)e^(zx)dx. Here h_u=−cPhi'−uxPhi, k_u(x)=∫_x∞h_u(y)dy and Phi_u(x)=u^−1∫_|x|∞sinh(u(y−|x|))k_u(y)dy>0. h_u and k_u each have ONE negative/positive crossing on the half-line; the exact cancellation∫cosh(uy)k_u(y)dy=0 and an increasing ratio prove the sign before taking absolute values. The equation Phi_u''−u²Phi_u=k_u, with no delta at0, gives the entire transform and its removable values.

Difference relative to003/074: a positive measure is constructed for the regularised denominator that remained pending, not only positive real values of the Schur quotient. H_u>0 and(logH_u)''>0 on the line. F1=−cz/u+c²Z/(uzH_u) is kept exactly, with residue R=uc²/(ua−c)>0 at0. F1 is not identified with a logarithmic derivative nor is G=F1−R/z obtained positive: comparing Phi with Phi_u is missing. No positivity of three generators, all orders or new windowT. No computations or campaigns; papers untouched and global sign OPEN.

## Next obligation

If R=uc²/(ua−c), the exact remainder is

    G_u(z)=c²/(uz)·[Z(z)/H_u(z)−Z(0)/H_u(0)]−cz/u.

Positivity of Phi_u does not control the quotient Z/H_u. A quantitative comparison between the TWO densities implying the mixed Schur bound is missing; applying Cauchy again to a form whose positivity is not proved is not enough. The general hypothesis of073 already has a recorded order-three limit074.075 does not eliminate that limit and only resolves the declared positive construction.

## Query076 — mass comparison and precise sufficient criterion

The following identities were reviewed by cases, via insight048 and in two further checks. Define J(x)=int_|x|^infinito y Phi(y)dy and tau(x)=J(x)/Phi(x). For x>0, V'>0 and V'/x strictly increasing give

    J(x)<[x/V'(x)] Phi(x),
    tau'(x)=V'(x)tau(x)−x<0.

The first inequality integrates y/V'(y)<x/V'(x) against V'(y)Phi(y)dy. This comparison is proved, but does not imply the necessary comparison with Phi_u.

Set beta=u²a/(ua−c) and define the defect

    T_u(z)=Z(z)−[Z(0)/H_u(0)+z²/c]H_u(z).

Its exact bilateral density, using k_u=cPhi−uJ and the equation of075, is

    t_u(x)=Phi(x)−[Z(0)/H_u(0)]Phi_u(x)−Phi_u''(x)/c
          =(u/c)[J(x)−beta Phi_u(x)].

The masses satisfy int_R J=aZ(0)=beta H_u(0); hence int_R t_u=0. Moreover G_u(z)=c²T_u(z)/(uzH_u(z)). If the difference J−beta Phi_u had exactly one negative/positive crossing in x>0, its pairing with cosh(zx) would be positive for all z>0 and one would obtain G_u(z)>0. A stronger sufficient condition is that J/Phi_u be strictly increasing, that is,

    J'(x)Phi_u(x)−J(x)Phi_u'(x)>0, x>0.

That Wronskian has not been proved for the real Phi. Nor would G_u>0 by itself prove the two-node kernel of the transform: this obligation is distinguished from full order-three positivity.

The simpler comparison r=Phi_u/Phi was not decided either. Its exact equation is

    r''−2V'r'+[(V')²−V''−u²]r=c−u tau.

Although the right-hand side is increasing, that does not fix r' without controlling the other terms. An asymptotic tail suggestion is not turned into global monotonicity.

The generic limit074 remains pertinent even after constructing Phi_u: its auxiliary potential also satisfies the conditions used075. In that same auxiliary, u=A, delta=1/10000 and c=M(A), the integration-by-parts identities give c<1 and Aa<=1;074 gives c>1−delta, while073 gives c<Aa. Thus0<Aa−c<delta. With m3=M(3A) in(2−delta,2+delta),

    F1(3A)<(5+4delta)/(1−4delta)<6,
    R/(3A)> (1−delta)²/(3delta)>3000,
    G_A(3A)<0.

For c<1 one uses E[v'(X)]=1 and positivity of the mean of the odd monomial under positive tilt; for Aa<=1, E[X V'(X)]=1>=A E[X²] at zero tilt. These are not new numerical evaluations. It is an application of the SAME auxiliary074 that prevents assuming the crossing as a generic consequence of073/075, not a failure of the real Phi nor a negative direction of W. The query identifies the specific pending comparison; it does not extend the sign coverage.
