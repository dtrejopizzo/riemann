# POWER_PARTICULAR_ORIGIN_DESIGN_093 — Prior design and decision of a single particular sign

**Independent audit:** design, literal and final source approved in `POWER_PARTICULAR_ORIGIN_AUDIT_093.md`; run37905 exit0/PASS, independent reproduction94506 exit0/FULL PASS128 and matching hash.

Status: **PROVED POINTWISE by run exit0/PASS; mathematical audit of design and literal approved before the run, final reading pending.** All the following parameters were fixed before execution. The prior design and its conditions are kept; the result is in§6. Papers untouched.

## 1. Specific object and antecedents

Consulted the project rules, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D, and073/077/078/087/089/090/092.092 discards a universal globally invertible elimination; it does not decide the sign for particular K. Here a necessary condition of that sign is checked at ONE point, using the global selection of K by its two boundary conditions. No other pivot, parameter or sign grid.

With w=tPhi,v=−Phi', a=M'(0),c=1/a, K''=v−cw,K(0)=K(infinity)=0, write Phi/Phi0=sum a_j t^(2j). Then

    W(w,v,w'',K)=64 Phi0^4 t^10[Dpart+O(t²)],
    Dpart=P kappa+Qc+R,
    kappa=K'(0)/Phi0=c tau0−1,
    tau0=I1/Phi0, a=I2/I0, Ir=integral_0^infinito t^r Phi(t)dt.

The columns of the matrix determining Dpart have the rows

    [1,−2a1,6a1,kappa],
    [a1,−4a2,20a2,−(2a1+c)/6],
    [2a2,−12a3,84a3,−(4a2+ca1)/10],
    [6a3,−48a4,432a4,−(6a3+ca2)/7].

The rational intervals of a1,...,a4 and Phi0 from087 are reused, without modifying its script. The exact coefficients are

    P=192(6a1a3a4−8a2²a4+3a2a3²),
    Q=(16/35)(126a1³a4−51a1²a2a3+10a1a2³
          −588a1a2a4+210a1a3²+30a2²a3+420a3a4),
    R=−(192/35)(28a1²a2a4−20a1²a3²+2a1a2²a3
          −70a1a3a4+56a2²a4−15a2a3²).

The sign of

    NUM=Q Phi0 I0+P I1 I0+(R−P)Phi0 I2
       =Phi0 I0 a Dpart

will be decided. The factor is positive. The final assert will accept NUM>0 **or** NUM<0; the sign is not predetermined. If it does not separate0, the result will be inconclusive with these parameters, without exploratory adjustments.

## 2. Fixed parameters and uniform complex bound

Integrate only [0,2] with128 panels of length1/64, half-width h=1/128, dyadic centres(2j+1)/128,j=0,...,127. Precision512bits, Taylor degree64, cap65,16 theta modes. Complex Cauchy radius r=1/32, ratio h/r=1/4.

On the discs around those centres, use the larger region

    −1/32<=Re t<=65/32, |Im t|<=1/32, |t|<3.

With y=pi exp(2t), e<3,pi<4, exp(−1/16)>15/16 and cos(1/16)>511/512:

    Re y>3(15/16)(511/512)>5/2,
    |y|<4 exp(65/16)<4*256=1024,
    |exp(5t/2)|<exp(325/64)<exp(6)<3^6<1024.

For each theta mode

    Phi_m=pi exp(5t/2)m²(2m²y−3)exp(−m²y),

one has |Phi_m|<2^24 m^4 8^(−m²), since exp(5/2)>8 (exp2>7,exp(1/2)>3/2). The sum of m^4 8^(−m²) is less than1/4: first term1/8 and all ratios are less than1/2. Thus |Phi|<2^22 and for r=0,1,2,

    |t^r Phi(t)|<9*2^22<10^8.

The COMPLETE tail of modes m>=17 has bound

    EPS=2^25*17^4/8^289,

by consecutive ratio <=(18/17)^4/8^35<1/2. At each centre outward errors EPS*32^k are added to ALL coefficients Phi[k],k=0,...,64, BEFORE multiplying by t^r.

## 3. Taylor quadrature and its exact error

Jets are evaluated only at exact centres, without parameter balls. For each t^rPhi the Taylor polynomial of degree64 is integrated exactly on the symmetric panel: odd terms vanish and the even term k contributes2coef[k]h^(k+1)/(k+1). The arb arithmetic keeps all rounding outward.

The pointwise error of the complete series on a panel is bounded by10^8(1/4)^65/(1−1/4). Integrating and summing over the panels, whose total length is2,

    REM=2*10^8*4^(−65)/(1−1/4)<10^(−28).

This remainder is added symmetrically to the truncated moment. It is independent of the observed values and of the theta tail errors already included in the coefficients.

## 4. Complete time tail t>2

For t>=2, pi>3,pi<4 and a geometric sum over all modes give

    Phi(t)<64 exp(9t/2−3exp(2t)).

Indeed the factor2m²y−3 is dominated by8m²exp(2t), and sum m^4 exp(−3m²exp(2t))<2exp(−3exp(2t)). The rational Taylor assert of exp4>54 fixes

    Phi(2)<64*3^9*2^(−162)<2^(−140).

The logarithmic derivative of the majorant is9/2−6exp(2t)<−300. Hence, with s=t−2,

    Phi(2+s)<2^(−140)exp(−300s),
    (2+s)^r<=4exp(2s), r=0,1,2,
    0<integral_2^infinito t^rPhi(t)dt<2^(−140).

The positive interval[0,2^(−140)] is added to each moment; the bound042, which required a different range of N, is not applied.

## 5. Implementation conditions and scope

ctx.prec=512,ctx.cap=65 explicit. Require Phi.prec>=65 and finite coefficients0..64 at all centres. Add the tails before multiplying by t or t². Convert the rational intervals of087 to arb using both endpoints and outward rounding, without taking decimals. Verify I0,I1,I2 and Phi0 strictly positive before any optional quotient. NUM is the main test and keeps its positive factors without unnecessary divisions.

The result only decides the jet of the real particular solution at the origin. If NUM>0, it refutes that sufficient condition near0, not the form W. If NUM<0, it only verifies it near0 without certified radius; it does not prove the global sign of QF nor a new order of generators.


## 6. Run result, reproduction and final scope

After independent approval of the design and of the literal, the SINGLE run37905 ended exit0/PASS128 panels with the above parameters, without modification during the run. The assert accepting either of the two signs obtained

    PASS093: particular-origin determinant sign NEGATIVE.

Outward interval output of Arb:

    I0 [0.124280194547078527478193434921 +/- 5.46e-31]
    I1 [0.021528707625566523248989621992 +/- 6.74e-31]
    I2 [0.005742986078786359383812469124 +/- 6.04e-31]
    a [0.04620998623083794157786762086 +/- 2.33e-30]
    tau0 [0.048195336934403062728348027284 +/- 4.42e-31]
    NUM [-55.56138101164184468956750 +/- 9.92e-24]
    Dpart [-21658.19847758362431307814 +/- 2.30e-21].

The proved sign comes from the strict interval comparison of the script, not from substituting the centres of these intervals. The moments include both the quadrature errors and ALL theta tails and the time tail. The small radius of NUM/Dpart includes the propagation of the rational jets of087 and conservatively lost dependencies; common errors are not excluded by informal cancellation.

By Dpart<0 and analyticity,

    W_t(w,v,w'',K)<0 for all sufficiently small t>0.

This result **verifies**, and does not refute, the required particular local condition on that neighbourhood. It provides neither a neighbourhood radius, a sign for all t>0, a cone invariance, nor a repair of the Delta chart of092. For F=K/w, the equivalent sign of ((F'/B')'/J)' is verified locally by the positive factors of the Wronskian; it has not been proved globally. It does not change the coverage of W nor the number of generators; the global goal remains OPEN.

Reproducible command from the root of the repository:

    python3 03-research/phase-211-sign-sandbox/tools/power_particular_origin_093_verify.py

SHA256 of the script, unchanged during the run:

    57c0656deb1767e00a4de674a0f5f6556886eca06edbc93ae1ef8488b032c67e.

The imported script087 remains intact, hash f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7. The independent reproduction and final reading will be recorded in audit093.
