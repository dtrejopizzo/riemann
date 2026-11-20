# POWER_MIXED_FOUR_ORIGIN_DESIGN_104 — Positive pointwise gate and tail of the real mixed system

Status: **PROVED the positive pointwise gate and the analytic tail; final independent reading pending.** Design and literal were approved independently BEFORE the run. The previous design is kept; the result is in§7. Reuse of the program087 INTACT via runpy to recover its non-persisted intervals was authorized. No new modes, precision, point or theta tail. Papers untouched.

## 1. Exact object and deduplication

Consulted the project rules, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D, and077/078/087/089/090/093/095/099/102/103. Keep the EVEN densities

    J(t)=integral_t^infinito sPhi(s)ds,
    K(t)=integral_t^infinito(s−t)[aPhi(s)−J(s)]ds,
    a=M'(0)=I2/I0, Ir=integral_0^infinito t^rPhi(t)dt.

Here K is the EVEN density of078, not the odd primitive093/095. The proposed mixed system is

    [K,J,Phi,J''].

103§11.4 already proves the three initial Wronskians strictly positive for the order[K,J,Phi,J'']. Hence a mixed W4 strictly positive on the whole half-line would complete ECT4. Its global Chebyshev4 would suffice for the new crossing argument localized by the exact identity beta D_p+p²Psi_p=lambda K. That property is not presupposed and it is not claimed that it is necessary for the sign of W or of the particular numerator. This test can only discard or let pass a necessary gate of THAT stronger property.

093 does NOT decide this origin: if f(lambda)=[K,J,Phi,J'']/Phi(0), lambda=t², then

    W_lambda(f')(0)=−a Dpart093/16>0,

but the object of104 is W_lambda(f)(0). They are minors of jet rows1,...,4 and0,...,3 respectively. The identity is obtained by differentiating the four even functions: their derivatives are[−aK_odd,−tPhi,Phi',−(tPhi)''], with the orientations of093. The sign of a shifted minor at a point does not transfer to the previous one; a global comparison that is not proved would be needed.099 only controls the corresponding Laplace-transformed version; it does not invert that transport to control pointwise densities.

## 2. Regularized matrix without t=0 cancellations

Write Phi(t)/Phi0=sum z_j lambda^j,z0=1, and set

    tau=I1/Phi0,
    kappa=(aI1−I3/2)/Phi0=K(0)/Phi0.

From J'=-tPhi and K''=aPhi−J, the rows of lambda derivatives0,...,3 give exactly

    H=[[kappa,tau,1,−1],
       [(a−tau)/2,−1/2,z1,−3z1],
       [(az1+1/2)/6,−z1/2,2z2,−10z2],
       [(az2+z1/4)/5,−z2,6z3,−42z3]].

The factors k! are included. With Dmix=detH,

    W_t(K,J,Phi,J'')
      =64Phi0^4 t^6[Dmix+O(t²)].                 (ORIGIN)

The factor t^6 is the change of variable of a Wronskian of FOUR EVEN functions: (2t)^6. Do not confuse it with t^10, which appears for four odd functions with a common factor t.

Only Phi0,z1,z2,z3 from087 and I0,I1,I2,I3 from103 are needed. Either sign will be accepted; an interval that does not separate0 leaves this fixed design inconclusive.

## 3. Already certified data and authorized recovery

087 uses outward rational intervals of scale10^70, pi by Machin128, exponential Taylor128 and11 squarings,8 modes and the WHOLE tail m>=9. Recovering its variables by runpy reproduces exactly THAT same pointwise obligation; the script087 is not altered. Its mandatory hash is

    f8f28e5f33659ec7245e23906ab11addc5a04243f1d502a8a070dbf12d13d7b7.

The data of103 are imported as EXACT rational intervals from their outward Arb outputs, without rerunning their quadrature:

    I0=0.12428019454707852747819343 +/- 6.89e−27,
    I1=0.02152870762556652324898962 +/- 3.96e−27,
    I2=0.00574298607878635938381247 +/- 2.84e−27,
    I3=0.00191588830192231322996545 +/- 4.90e−27.

These balls already include the complete mode tail, quadrature remainder and time tail. Their decimal centres are converted via Fraction, and their respective radii are689,396,284,490 divided by10^29. The SAME class I of087 is used to form all quotients and products, with outward rounding to10^70. Precision is not increased.

Check Phi0>0,I0>0 and1/25<a<1 before the quotients; the last box is already contained in103 and pays for the following exterior proof. Evaluate detH by its24 permutations. The assert accepts Dmix>0 OR Dmix<0, without imposing an orientation beforehand. The recovered intervals Phi0,z1,z2,z3 will be printed so as not to lose these data again.

## 4. Exterior orientation with complete holomorphic remainder

It is justified BEFORE data that the mixed Wronskian has POSITIVE orientation on a tail. Reuse COMPLEX of095: for Re z>=3,|Im z|<=1/16,y=pi exp(2z),Y=|y|,

    |p−2y|<6, |p'|<=5Y, Re p>=Y, p=−Phi'/Phi,
    |Phi(z+r)/Phi(z)|<=exp(−Yr), r>=0.

095 proves these bounds with the WHOLE theta tail and zero-free holomorphic discs; the mode correction is not erased. Define T1=integral_0^infinito rPhi(z+r)dr/Phi(z). Two exact integrations by parts give

    T1=1/p²−integral_0^infinito [Phi(z+r)/Phi(z)]
                   [2p'(z+r)/p(z+r)^3+r p'(z+r)/p(z+r)^2]dr,
    |T1−1/p²|<=15/Y³.

Also J(z)/Phi(z)=z H0(z)/Phi(z)+T1, where095 gives |H0/Phi−1/p|<=5/Y². Hence

    |J/Phi−z/p|< (5|z|+2)/Y².

The definition of K is K/Phi=aT1−integral_0^infinito rJ(z+r)dr/Phi(z). With a<1 and

    |J(z+r)/Phi(z+r)|< (|z|+r)/(Y exp(2r))
                          +1/[Y²exp(4r)],

one obtains

    |K/Phi−a/p²|< (16+|z|)/Y³.

All horizontal integrals are holomorphic and absolutely convergent on compacta of the strip. No real O without remainder is differentiated.

## 5. Exterior model and payment of the determinant

Fix t>=4 real,y0=pi exp(2t),P=2y0 and disc|z−t|<=1/32. Compare the normalized columns

    [K/Phi,J/Phi,1,J''/Phi]
    with [a/P²,t/P,1,tP].

The first formulas and |p−2y|<6 imply complex error bounds less than

    50(1+t)y0^(−3),20(1+t)y0^(−2),0,7(1+t).

Here J''/Phi=zp−1 exactly. The factors(16/15)^2,(16/15)^3 are less than2 in the changes from Y to y0. Cauchy on the fixed disc controls derivatives0,...,3 with the common bound

    Hstar=200*3!*32³=39321600,
    column errors <=Hstar(1+t)[y0^(−3),y0^(−2),0,1].

The model entries and their derivatives up to3 are bounded by

    [16/y0²,16t/y0,1,32t y0].

The exact algebraic identity is

    W_t[a/P²,t/P,1,tP]
       =128a(6t²+4t−1)/P²
       >=192a t²/y0²>7t²/y0², t>=4.

Multilinearity and24 terms per determinant give the total error

    |Wmixed/Phi^4−Wmodel|
      <=[61440Hstar+6144Hstar²+192Hstar³]t³/y0³
      <Cstar t³/y0³,
    Cstar=10^6(1+Hstar)^3<2^98.

The coefficients come from the three simple errors, three double ones and one triple; we use1+t<=2t,y0>=1 and a<1. It is finite arithmetic without evaluating theta. Since y0/t is increasing for t>1/2, and at64 one has y0>2^128 and64Cstar<2^104,

    Wmixed(t)/Phi(t)^4>6t²/y0²>0,
    for ALL t>=64.                            (POSITIVE-TAIL)

The positive orientation is therefore rigorous and prior to the origin test. t is the internal time variable, not a window T.

## 6. Predetermined reading of the gate

- **Dmix<0:** ORIGIN and POSITIVE-TAIL produce evaluation determinants with opposite orientations, by confluence at sufficiently close points. By continuity in the four-node chamber, the mixed system CANNOT be globally Chebyshev4. This would refute only THAT sufficient condition for the continuation, not the crossing of the particular U, the positivity of its primitive, its kernel, W or other mechanisms.
- **Dmix>0:** only verifies the origin sign on an existing neighbourhood, without radius. It does not prove global Chebyshev4 nor indefinite preservation.
- **Dmix contains0:** inconclusive with the fixed design, without new parameters.

The implementation will follow the independent approval of the design; it will not be executed until its literal is also audited. Afterwards ONE exact recovery087 and ONE evaluation of this polynomial will be allowed, not a campaign of points, pivots or precisions.


## 7. Result of the single recovery and gate

After independent mathematical and literal approval, the run ended exit0/PASS with the fixed script. There was no modification of parameters, coefficients, precision or inputs after observing the sign. The decision was

    PASS104: mixed-four origin sign POSITIVE.

The complete rational endpoints are

    lower=20910875038731301173957476100644455719909401587771537215845430471153/
          5000000000000000000000000000000000000000000000000000000000000000000000,

    upper=41821750077462602464978622735022256356361140514400545338810504099651/
          10000000000000000000000000000000000000000000000000000000000000000000000.

Both numerators and denominators are strictly positive; the approximate figure0.00418217500774626 is only a reading, not the proof. The interval is obtained with the rational class I70 of087 and the complete inputs103, without removing tails nor inferring jets from approximate decimals.

The COMPLETE output is persisted in

    tools/power_mixed_four_origin_104_verify.log.

That file also stores the recovered rational endpoints of Phi0,z1,z2,z3, together with the hash087 and its tail/parity proofs. It allows reusing them in the future without rerunning theta. The script087 was not altered.

SHA256 of104:

    063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105.

Command from the root directory:

    python3 03-research/phase-211-sign-sandbox/tools/power_mixed_four_origin_104_verify.py

ORIGIN and Dmix>0 prove Wmixed>0 on an existing neighbourhood of0, without certified radius. POSITIVE-TAIL proves the same sign for ALLt>=64. **The intermediate interval remains open**: global Chebyshev4, preservation of the pair, the particular crossing of U and positivity of a new primitive are not proved. No refutation of the route was found by this gate. Nor is a new W sign, generators, all orders or window T claimed.

The same script was reproduced with exit0/PASS and the same hash063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105. The documentary closure and final reading will be recorded in audit104. The result does not authorize additional tests of undesigned parameters or points.

## Analytic extension: keeping powers of the remainder reduces the tail to t>=16

**PROVED / independent review, without new theta data.** In the seven multilinear terms of§5 it is not necessary to discard all additional powers of y. Keeping them one obtains

`error <=61440 Hstar t³/y³+6144 Hstar² t³/y⁴+192 Hstar³ t³/y⁵`.

The three simple terms have y^-3; the three double ones have y^-4 and the triple y^-5. The same entry majorants and1+t<=2t are kept. For y>=Hstar, the error is less than2^17 Hstar t³/y³, since61440+6144+192=67776<2^17.

With Hstar=39321600, positive Taylor up to degree5 proves exp2>7; the exact integer computation gives

`3*7^16=99698791708803 >16*2^17*Hstar=82463372083200`.

Hence y(16)=pi exp32>3*7^16 and, since y/t grows for t>1/2, for ALLt>=16 one has y>=Hstar anderror<t²/y². The previous model is larger than7t²/y², so that

`Wmixed(t)/Phi(t)^4>6t²/y²>0 for ALLt>=16`.

It is an improvement of the remainder of104, not a new evaluation of theta nor a change of parameters of110. Run110 is kept intact. No sign of the compact nor global coverage is inferred without the corresponding proofs and reproduction.
