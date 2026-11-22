# POWER_PARTICULAR_TAIL_095 — Analytic tail of the particular Wronskian

Status: **PROVED by the following analytic estimates; independent audit approved.** See `POWER_PARTICULAR_TAIL_AUDIT_095.md`. No new theta evaluation, compact certificate, explored parameter or grid. Papers untouched. The required sign of the PARTICULAR Wronskian is proved for all t>=64, not for all t>0 nor for a new window T of Paper46.

## 1. Data, consultation and difference from088/092

Consulted the project rules, README ROUTES-TRIED-INDEX, R162_2300_MASTER_GRID and CROSSWORD-TO-D, and077/078/087–094.088 controls the original Wronskian of four densities.092 shows that universal elimination via Delta is not globally invertible.093 verifies the sign of the particular solution on an unquantified neighbourhood of the origin. Here the integral selection of THAT particular solution is used to prove a complete tail; Delta is not inverted and no real equivalent without remainder is differentiated.

Phi is the REAL theta density, even, positive and with supertails, and

    w=tPhi, v=−Phi', a=M'(0)>1/25, c=1/a<25,
    zeta=v−cw,
    K(t)=integral_t^infinito(s−t)zeta(s)ds.

The inequality a>1/25 is the real anchor078, not an approximation of the moments. K(0)=0 by the exact moment integral_0^infinito t zeta(t)dt=0. Its odd extension is smooth and K''=zeta. The object is

    Wpart(t)=W_t(w,v,w'',K).

## 2. Complete complex control of the theta logarithm

On the larger strip Re z>=2, |Im z|<=1/8, write y=pi exp(2z),Y=|y|. The elementary bounds pi>3,exp4>54 and cos(1/4)>31/32 give

    Y>162, Re y>(31/32)Y>156.

The function factors exactly

    Phi(z)=pi exp(5z/2)(2y−3)exp(−y)[1+Rtheta(z)],
    Rtheta=sum_(m>=2)m²(2m²y−3)/(2y−3) exp[−(m²−1)y].

Since Y>162, the rational factor has modulus less than2m^4. The terms m^4 exp[−156(m²−1)] have successive ratios less than1/2: from m=2, (1+1/m)^4<6 and the increment of the exponent is at least780. Hence the WHOLE tail satisfies

    |Rtheta|<64 exp(−468)<2^(−462)<2^(−460).

This includes all modes m>=2; they are not discarded. The series log(1+Rtheta) is holomorphic with modulus less than2^(−459). On each disc of radius1/32 around Re z>=3,|Im z|<=1/16, one stays in the larger strip. Cauchy gives

    |[log(1+Rtheta)]'|<32*2^(−459)<1,
    |[log(1+Rtheta)]''|<2*32²*2^(−459)<1.

Neither 2y−3 nor1+Rtheta vanishes. Define the logarithmic derivative p(z)=−Phi'(z)/Phi(z), without needing a global choice of the logarithm of Phi. For the first mode,

    p_first=2y−9/2−6/(2y−3),
    p_first'=4y+24y/(2y−3)².

On the inner strip Re z>=3,|Im z|<=1/16 one concludes

    |p−2y|<6, |p'|<=5Y, Re p>=Y, |p|>=Y.        (COMPLEX)

The last comparison uses Re(2y)>=2Y cos(1/8), cos(1/8)>127/128 and Y>162. Thus all quotients used below are holomorphic on that strip.

## 3. Horizontal representation and integration by parts with remainder

For z in the inner strip,

    K(z)=integral_0^infinito [1−cs(z+s)]Phi(z+s)ds. (HORIZONTAL)

For real z it follows from integrating by parts the term−Phi' in the definition of K. The identity extends to the strip by holomorphy: the horizontal integrals converge uniformly on compacta by Re y>0 and the theta supertails.

Fixing z and s>=0, COMPLEX implies

    |Phi(z+s)/Phi(z)|
       <=exp[−integral_0^s Y exp(2r)dr]
       <=exp(−Ys).

Let H0(z)=integral_0^infinito Phi(z+s)ds. The exact integration by parts, with vanishing boundary term at infinity, gives

    H0(z)/Phi(z)=1/p(z)
      −integral_0^infinito [Phi(z+s)/Phi(z)]p'(z+s)/p(z+s)² ds.

Here |p'(z+s)/p(z+s)²|<=5/[Y exp(2s)]<=5/Y. Hence

    |H0/Phi−1/p|<=5/Y².

The second term of HORIZONTAL is controlled keeping its complete structure:

    |K/Phi−H0/Phi|
      <=25 integral_0^infinito s(|z|+s)exp(−Ys)ds
      =25|z|/Y²+50/Y³.

Since Y>50,

    |K/Phi−1/p|< (6+25|z|)/Y².                 (IBP-REM)

It is a bound for holomorphic functions on a strip, not just a real O. It allows controlling derivatives by Cauchy without informally differentiating an asymptotic remainder.

## 4. Three column errors and their derivatives up to order3

Fix real t>=4 and y0=pi exp(2t). On the disc |z−t|<=1/32 one has

    (15/16)y0<Y<(16/15)y0,
    |z|<t+1.

The bounds exp(−1/16)>15/16 and exp(1/16)<16/15 are used. Dividing all columns by Phi, the common-factor rule of the Wronskian gives

    Wpart/Phi(t)^4=W_t[t,p,t(p²−p')−2p,K/Phi].

Compare with the model of analytic functions

    [t,q,tq²,1/q], q(z)=2pi exp(2z).

The first column is exact. For the second, COMPLEX gives |p−q|<6. For the third,

    |t(p²−p')−2p−tq²|
       <=[35|z|+6]Y
       <200(1+t)y0.

In this estimate t inside the analytic function means z; the real t only names the centre. We used |p+q|<5Y,|p'|<=5Y,|p|<3Y. For the fourth, IBP-REM and

    |1/p−1/q|<=3/Y²

give

    |K/Phi−1/q|<200(1+t)y0^(−2).

Cauchy on the fixed disc of radius1/32 controls the derivatives0,...,3 of ALL these errors. With

    H=200*3!*32³=39321600,

the moduli of the entries of the error columns, in any row of derivatives0,...,3 of the Wronskian, are respectively less than

    H, H(1+t)y0, H(1+t)y0^(−2).                (COL-ERR)

The boundaries of the discs are admissible because one works in a neighbourhood of the closed strip; alternatively the same bound is obtained as a limit of smaller radii. No O is differentiated without control.

## 5. Model determinant and explicit finite remainder

At the real centre, the four model columns and their derivatives up to order3 have entries bounded in modulus by

    [t,16y0,512t y0²,4/y0].

Indeed q'=2q and the derivatives of tq² are4y0²[4^r t+r4^(r−1)],r<=3, bounded by512t y0² for t>=4. The exact polynomial computation of the model determinant is

    W[t,q,tq²,1/q]
      =−128q²(6t²+4t−1)
      <=−3072t²y0².                            (MODEL)

No theta values are used for this identity. Expanding multilinearly in the three errors COL-ERR produces seven terms. Each determinant is bounded by24 times the product of the maxima of its columns. Using1+t<=2t,t>=4,y0>=1, the three terms with one error sum to at most445440H t³y0; the three with two errors,26304H²t³y0; and the one with three errors,96H³t³y0. Consequently

    |Wpart/Phi^4−Wmodel|<C t³y0,
    C=10^6(1+H)³,
    445440H+26304H²+96H³<C<2^98.                (DET-REM)

The last inequalities are integer arithmetic: H+1<2^26 and10^6<2^20. The simultaneous effect of the errors is kept; the sign of separate columns is not extrapolated.

## 6. Analytic threshold and result

The function y0/t=pi exp(2t)/t is strictly increasing for t>1/2. At t=64, using exp1>2,

    y0>2^128,
    C*64<2^104,
    y0>C*64.

Thus y0>Ct for ALL t>=64. MODEL and DET-REM then give

    Wpart(t)/Phi(t)^4<−3071t²y0²<0,
    W_t(tPhi,−Phi',(tPhi)'',K)<0 for ALL t>=64. (TAIL-PARTICULAR)

The number64 is obtained only from the above majorants and integer powers, without evaluating the determinant at points nor adjusting a threshold to observed signs.

## 7. Scope and remaining obligation

093 verifies this same sign near0; the present proof verifies the whole tail t>=64. The intermediate interval remains open. It is not inferred that four-density systems preserve the sign by mere inversion of D², nor that the Delta chart of092 is regular; this proof avoids that chart and directly uses the particular solution selected by its boundary conditions.

The parameter t here is the internal time variable of the theta densities, **not a new window T**. Neither positivity for five generators nor all orders, nor an extension of the coverage of W, is claimed. A global proof of the particular sign would still be needed for the corresponding application. No numerical verifier is created: only the explicit analytic identities and inequalities above are used.
