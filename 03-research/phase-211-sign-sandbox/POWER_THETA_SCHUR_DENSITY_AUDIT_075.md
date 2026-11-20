# POWER_THETA_SCHUR_DENSITY_AUDIT_075

Status: **APPROVED** POWER_THETA_SCHUR_DENSITY_075, after a complete reading and the clarification of Fubini in NEG-MASS. Analytic proof, without new computations. Papers untouched.

Consulted the antecedents in index/grid/crossword, SCHUR003, THETA073 and the scope limit 074. The literal construction of this density was not found in the targeted searches. The Schur algorithm and its first quotient are earlier; the new object is a POSITIVE representation of the regularized denominator for the SAME Phi. The source does not identify it with an unproved logarithmic derivative.

## First weights and mass

073 gives c=M(u)>0 and c<ua for all u>0. V even implies V′(0)=0, and V‴>0 proves that V′(x)/x is strictly increasing. Its average under x²Phi/(aZ0) is 1/a by integration by parts; the limit at 0 is strictly less than that average and, therefore, less than u/c. The limit at infinity is infinite for the real theta tail. This provides exactly one crossing of h_u on the positive half-line, from negative to positive.

h_u is odd and of total integral 0, so its primitive towards infinity k_u is even and decays in both tails. On x>0, k′=−h makes k increase up to the crossing of h and then decrease to 0 from positive values. For NEG-MASS Fubini is applied AFTER using parity: 2integral_0∞ k=2integral_0∞ y h(y)dy, whose absolute majorant is finite. The absolute double integral over all of R is not interchanged. The resulting integration by parts gives Z0(c−ua)<0. This forces k(0)<0 and, by the described monotonicity, exactly one negative/positive crossing of k.

## Cancellation and positive density

The bilateral transform of h is D_u(z)=zcZ−uZ′. The identity k′=−h gives D_u=z Laplace(k), with vanishing boundary terms. D_u(u)=0 implies the exact cancellation of the signed mass cosh(uy)k(y)dy on [0,∞).

The quotient w_x(y)=sinh(u(y−x))1_(y>=x)/cosh(uy) is continuous, nondecreasing and has derivative u cosh(ux)/cosh²(uy)>0 for y>x. Subtracting its value at the single crossing of k leaves a nonnegative integrand; it is strictly positive on a nonempty tail. The cancellation is preserved before comparing weights. The factor 1/u is positive and correctly included. Thus Phi_u(x)>0 for all x, including 0.

## Equation and transform

Two differentiations of the integral towards infinity give Phi_u″−u²Phi_u=k, with the correct positive sign of k. The first derivative at 0 is the negative of the balanced cosh integral and therefore vanishes. The even extension is smooth: the equation with smooth even k and the Neumann datum 0 allows extending all derivatives without jump or delta mass.

The theta tails of h and k are smaller than any exponential; the sinh kernel preserves this fact for each fixed u, choosing an exponent larger than u. The same holds for the first derivative of Phi_u, sufficient for the boundary terms of the equation. One obtains exactly

    H_u(z)=Laplace(Phi_u)(z)=D_u(z)/[z(z²−u²)].

The singularities 0, ±u are removable by the entire identity. At 0 the mass is Z0(ua−c)/u²>0, without a factor 2 lost by the use of half-lines. Positivity of Phi_u and all its moments justify H_u>0 and (logH_u)″>0 on the whole real axis.

## First transform and scope

Verified algebraically the identity

    F1(z)=−cz/u+c² Z(z)/(u z H_u(z)).

The residue at 0 is u c²/(ua−c)>0; subtracting it gives exactly the expression G_u of the source. Nothing proved turns F1 into H_u′/H_u nor automatically orders Z/H_u. The hypothesis V_u‴>0 is not assumed to be preserved, nor is a second-order Pick kernel for F1 proved.

The new positive density is a real and specific structural restriction of the regularized denominator. It does not contradict 074, does not prove three generators nor all orders and adds neither a time window nor a global sign of W. The comparison between Phi and Phi_u needed by the next step remains explicitly open.
