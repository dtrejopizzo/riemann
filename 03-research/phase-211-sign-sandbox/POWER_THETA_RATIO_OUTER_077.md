# POWER_THETA_RATIO_OUTER_077 — Two local signs for the real Phi on x>=1

Status: **PROVED/APPROVED by independent review**, proof read and Fraction verifier with three PASS; also an independent symbolic check. Only the exterior range of the hypotheses 077. Papers and phase 103 untouched.

## 1. Object and antecedents

Consulted the project rules, index/grid/crossword and the antecedents 073–076. The exterior range 10343 controls only the third log-derivative. Here two different local combinations are checked, with derivatives up to order 4, which the tail-quotient criterion 077 needs. Positivity of a transform is not relabelled as the sign of a quotient, nor is it claimed that these hypotheses are verified near the origin.

Let V=−logPhi and, for x>0,

    p=V′, q=V″, r=V‴, s=V⁗,
    C=p³+xp²q−pq−xpr+xq²,
    C′=4p²q+2xpq²+xp²r−2pr+xqr−xps,
    J=(xq−p)C′−xrC.

We prove for ALL x>=1:

    C>3(1+x)y³>0, J>31x²y⁴>0, y=pi exp(2x)>21.       (OUTER)

Therefore L=(xq−p)/C is positive and strictly decreasing there, because L′=−J/C². Also L tends to 0. The positivity xq−p>0 comes from 073.

## 2. First mode: certificate on a larger region

Set b=2y−3. The four potential derivatives of the first mode are

    p0=2y−9/2−6/b,
    q0=4y+24y/b²,
    r0=8y−48y(2y+3)/b³,
    s0=16y+96y(4y²+24y+9)/b⁴.

Define C0, J0 with those same formulas. The rational identities and signs are checked

    C0>4(1+x)y³,
    J0>32x²y⁴,                         ALL x>=1,y>=21. (MODE)

The relation between x and y is not needed for this step: it is a valid strengthening on the WHOLE quadrant. The exact evidence is in tools/power_theta_ratio_outer_077_verify.py, which uses only Fraction and operations on two-variable polynomials.

The script substitutes

    p0=P/(2b), P=8y²−30y+15,
    q0=Q/b², Q=16y³−48y²+60y,
    r0=R/b³, R=8yb³−48y(2y+3),
    s0=S/b⁴, S=16yb⁴+96y(4y²+24y+9).

For C it uses the positive denominator 8b⁴ and for J 8b⁷. After subtracting the margins of MODE and changing x=1+X, y=21+Y, ALL coefficients of both numerators are strictly positive: 16 and 36 nonzero terms, respectively, including their constant terms. The formulas for J expand exactly as

    J=−4p³q+2p²r
       +x(−2p³r+2p²q²+p²s−2pqr)
       +x²(2pq³−pqs+pr²).

This certifies MODE for the whole quadrant, without sampling or selection by eigenvalues. If common factors are cancelled one recovers 12 and 27 positive coefficients with denominators 8b² and b⁴, but those cancellations are not necessary for the certificate.

## 3. Complete theta tail up to the fourth derivative

Write Phi=f1(1+Rtheta), and for m>=2 use a=m²−1>=3, z=ay. The audited bound 10343 gives

    0<r_m=f_m/f1<=(32/9)a² exp(−ay).

The first three log-derivatives have moduli <3z, 5z, 10z. For the fourth, write

    B(y)=48y(2y+3)/(2y−3)³,
    DB(y)=−96y(4y²+24y+9)/(2y−3)⁴.

For y>=21, |DB(y)|<3: it suffices that 4+24/y+9/y²<6 and 2−3/y>9/5. Hence |D⁴logr_m|<=16z+6<20z. The Bell formula for the fourth derivative gives

    |D⁴r_m|/r_m
      <=81z⁴+270z³+195z²+20z<100z⁴, z>=63.

The same 100z⁴ also majorizes orders 0,1,2,3. Extending the actual a of the sum to ALL integers a>=3 results in

    |D^ell Rtheta|
      <=(3200/9)y⁴ sum_(a>=3)a⁶ exp(−ay), 0<=ell<=4.

Exp(3)>16 by a positive Taylor sum up to degree 7. The ratio of terms of the last sum is <=(4/3)^6/16^7<1/2. Moreover y⁴exp(−3y) decreases for y>=21. Thus, simultaneously,

    |D^ell Rtheta|
      < E=(6400/9)3⁶21⁴/2⁸⁴ <10^−12, 0<=ell<=4.     (TAIL)

The sum is complete, not only a prefix of modes. Since Rtheta>=0, the denominators of the log-derivatives are >=1. The formulas for log(1+Rtheta) up to order 4 have moduli bounded by

    epsilon+7epsilon²+12epsilon³+6epsilon⁴<10^−10,
    epsilon=10^−12.

Therefore each of p, q, r, s differs from its first-mode value by less than eta=10^−10.

## 4. Explicit payment of the local error

On y>=21, the first mode satisfies 0<p0<2y, 0<q0<5y, 0<r0<8y and 0<s0<17y. In particular, all segments between the four exact derivatives and their first-mode values lie inside the box |p|,|q|,|r|,|s|<=20y.

The sum of the moduli of the three partial derivatives of C on that box is <=2520xy² for x>=1, y>=21. For J expanded above, the degree-4 monomials sum to absolute coefficient by degree 40 and those of degree 3 sum to 21. Hence the sum of moduli of its four partial derivatives is <=328400x²y³. The multivariable mean value theorem gives

    |C−C0|<=2520xy²eta,
    |J−J0|<=328400x²y³eta.

Since 2520eta<21 and 328400eta<21, the margins MODE prove exactly OUTER. The rational comparisons of TAIL, Bell and these losses are included in the same verifier.

## 5. Boundary terms and scope

For x>=1, the real relation y=pi exp(2x) ensures y>21 by pi>3 and exp2>7. The numerator xq−p is positive by 073 and is bounded, for example, by 20(1+x)y. Together with OUTER this gives

    0<L(x)<=20/(3y²) ->0.

Also p>=y and q<=6y there; therefore w=1+xq/p<=1+6x. The theta tail implies wPhi->0 and the integrability of bPhi in the criterion 077. These boundary facts are not deduced from C>0 alone: they are checked with the specific REAL tail.

The interval 0<x<1 is not resolved by this memo. Without that verification and without the later conditional argument, G positive, a positive Schur kernel or three generators are not declared. The result is exclusively the uniform analytic check of TWO local signs on the exterior range.
