# POWER_THETA_SCHUR_DENSITY_075 — Positive density of the regularized denominator

Status: **PROVED/APPROVED**, independent review POWER_THETA_SCHUR_DENSITY_AUDIT_075.md. Property of the real Phi of 073. It does not prove the sign of the remainder G, of the second-order Schur kernel nor of three generators. Papers untouched; no new computations.

## 1. Corpus and precise change

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread POWER_SCHUR_003 and the theta sources 073. The searches for regularized denominator, Schur density and sinh/cosh formulas did not find this object in phase 211/103 nor a literal construction in the corpus. The Schur regularization antecedents of other phases belong to other operators; their general algorithm is not presented as new.

Step 003 gave real positivity of the first quotient, without preserving its kernel. The continuation 074 identified two-sided weights with sign change and left open the positivity of the denominator after removing its known real zeros. Here EXACTLY that obligation is resolved by an explicit positive density. It is not replaced by another function, nor is it claimed that a quotient of positive transforms is a positive logarithmic derivative.

## 2. Theta data and definitions

Let Phi be the even positive smooth function of CONE001/073; V=−logPhi. The already proved real results are used

    V'''(x)>0 for ALL x>0,
    Z(z)=∫_R Phi(x)e^(zx)dx,
    M(u)=Z'(u)/Z(u), M''(u)<0 for u>0.

Phi and its derivatives decay faster than any exponential. Therefore Z is entire, all the following integrations by parts have vanishing boundary terms and all moments used are finite. Moreover V'(x)/x tends to infinity by the explicit theta tail.

Fix u>0 and write

    c=M(u)>0, a=M'(0)=∫x²Phi(x)dx/Z(0)>0,
    D_u(z)=zcZ(z)−uZ'(z).

Strict concavity of M and M(0)=0 imply c<ua. Define on the whole line

    h_u(x)=−cPhi'(x)−uxPhi(x)
           =Phi(x)[cV'(x)−ux],
    k_u(x)=∫_x^infinity h_u(y)dy.

Finally, with x real,

    Phi_u(x)=(1/u)∫_|x|^infinity sinh(u(y−|x|))k_u(y)dy.  (NEW-PHI)

## 3. Two controlled sign changes, one in each weight

Since V is even, V'(0)=0. For x>0,

    d/dx[V'(x)/x]
      =[xV''(x)−V'(x)]/x²
      =(1/x²)∫_0^x tV'''(t)dt>0.

Integration by parts gives ∫xV'(x)Phi(x)dx=Z(0). Thus the average of V'(x)/x under the probability x²Phi(x)/(aZ(0)) is 1/a. The strictly increasing function is not constant, so its limit at 0 is less than 1/a. Since u/c>1/a and the limit at infinity is infinite, there exists a UNIQUE b>0 with V'(b)/b=u/c.

Consequently h_u is odd and has negative sign on 0<x<b and positive on x>b. Its integral over the whole line is 0. Hence k_u is even and k_u'=−h_u; on the positive half-line it first increases strictly up to b and then decreases strictly to 0 from positive values.

Parity allows applying Fubini only on the positive half-line, where ∫_0^infinity y|h_u(y)|dy is finite. Then integration by parts gives

    ∫_R k_u(x)dx=2∫_0^infinity k_u(x)dx
                 =2∫_0^infinity y h_u(y)dy
                 =∫_R x h_u(x)dx=Z(0)(c−ua)<0.          (NEG-MASS)

This forces k_u(0)<0: otherwise the previous monotonicity would make k_u>=0 on the whole line. Since k_u(b)>0, there exists exactly ONE beta in (0,b) with

    k_u(x)<0 for 0<=x<beta,
    k_u(x)>0 for x>beta.                              (ONE-CROSS)

All interchanges are absolutely convergent by the theta tail; the sign of k is not inferred only from the sign of its integral.

## 4. Exact cancellation and positivity of the new density

The bilateral transform of h_u is D_u(z), since ∫−Phi'(x)e^(zx)dx=zZ(z). Since k_u'=−h_u, another integration by parts gives

    D_u(z)=z∫_R k_u(x)e^(zx)dx.

The equality D_u(u)=0 and the parity of k imply

    ∫_0^infinity cosh(uy)k_u(y)dy=0.                    (BALANCE)

For each x>=0, set

    w_x(y)=sinh(u(y−x))1_(y>=x)/cosh(uy), y>=0.

This function is continuous, nondecreasing and strictly increasing for y>x, because there

    w_x'(y)=u cosh(ux)/cosh²(uy)>0.

The signed measure dnu(y)=cosh(uy)k_u(y)dy has total mass 0 and ONE negative/positive sign crossing at beta. Therefore

    ∫w_x dnu=∫[w_x(y)−w_x(beta)]dnu(y)>0.

The integrand of the last integral is nonnegative on both sides of beta. Strict positivity comes, for example, from y>max(x,beta), where k_u>0 and w_x(y)>w_x(beta). The tails guarantee integrability.

By NEW-PHI,

    Phi_u(x)>0 for ALL real x.                       (POSITIVE)

This step keeps the cancellation BALANCE before comparing weights, instead of taking absolute values of k_u.

## 5. Differential equation and exact transform

For x>0, differentiating NEW-PHI gives

    Phi_u'(x)=−∫_x^infinity cosh(u(y−x))k_u(y)dy,
    Phi_u''(x)−u²Phi_u(x)=k_u(x).

BALANCE implies Phi_u'(0+)=0. The even extension is therefore smooth and satisfies the equation on the whole line, without delta mass at 0.

For all A>u, the theta tail allows |k_u(y)|<=C_Ae^(−Ay); NEW-PHI and its first-derivative formula give bounds of the same type for Phi_u and Phi_u'. Since A is arbitrary, the bilateral transforms are entire and the boundary terms of integration by parts vanish for all complex z. One obtains exactly

    ∫_R Phi_u(x)e^(zx)dx
      =D_u(z)/[z(z²−u²)].                              (TRANSFORM)

The values at 0, ±u are removable by the entire identity. In particular the positive mass is

    ∫_R Phi_u(x)dx=Z(0)(ua−c)/u²>0.

An explicit positive representation of the regularized denominator has been constructed, not merely a proof that its value on the real axis is positive.

## 6. Real corollary: positivity and strict log-convexity

Define H_u(z)=∫Phi_u(x)e^(zx)dx by TRANSFORM. For all real z, H_u(z)>0 and

    (log H_u)''(z)=Var_(Phi_u exp(zx)/H_u(z))(X)>0.

The identity is obtained by differentiating under the integral, justified by the superexponential tail. The variance is strictly positive because Phi_u is positive on the whole line, not a point mass. By parity, H_u is even and its logarithmic derivative is odd and increasing. Neither the sign of (log H_u)''' nor hazard convexity of Phi_u is inferred.

## 7. Comparison still missing for the Schur step

The transform of 003 is

    F_1(z)=c[zM(z)−uc]/[zc−uM(z)].

If H_u(z)=∫Phi_u(x)e^(zx)dx, exact algebra using TRANSFORM gives

    F_1(z)=(c²/u) Z(z)/[zH_u(z)]−cz/u.

The residue at 0 is R_u=uc²/(ua−c)>0. Therefore

    G_u(z)=F_1(z)−R_u/z
      =(c²/(uz))[Z(z)/H_u(z)−Z(0)/H_u(0)]−cz/u.

POSITIVE does not automatically order the quotient Z/H_u nor identify it with a logarithmic derivative. A specific inequality comparing Phi and Phi_u and controlling the kernel of G or that of F_1 is missing. The generic class of hypotheses of 073 does not imply positivity of order three, as 074 already records; this result does not remove that limit. Neither positivity of three generators, of all orders nor a new time window is deduced.
