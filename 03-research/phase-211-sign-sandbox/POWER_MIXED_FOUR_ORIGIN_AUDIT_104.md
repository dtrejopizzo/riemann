# Audit104 — mixed pointwise gate and exterior orientation

Status: **PROVED / audit approved. Run and independent reproduction exit0/PASS.** Source: `POWER_MIXED_FOUR_ORIGIN_DESIGN_104.md`. The project rules and the consultation of antecedents087/093/095/099/102/103 and the three indices are kept. Papers untouched.

The family is[K_even,J,Phi,J''], different from the shifted minor093. The matrix H correctly includes the derivative factors in lambda=t²: in particular the third and fourth rows of K are(az1+1/2)/6 and(az2+z1/4)/5. The Wronskian change is(2t)^6=64t^6, without the common factor t proper to odd functions. The sign of Dmix will only be the origin of W4, not its global control.

The authorized recovery087 must keep its hash, parameters and complete tail. The four moments103 will be used as outward rational intervals, not as floating centres. The evaluation accepts both signs, without campaign or adjustment.

## Analytic exterior

Reviewed the reuse of the holomorphic strip095 with all modes. Two horizontal IBPs give T1=1/p²−integral R[2p'/p³+rp'/p²], with exponentially dominated boundary terms. Rep>=Y and|p'|<=5Y pay|T1−1/p²|<=15/Y³. The direct representation of J pays|J/Phi|<=|z|/Y+1/Y²; integrating rJ, the error of K is less than(16+|z|)/Y³. No real O is differentiated.

Cauchy at radius1/32 controls the column errors up to order3. The model[a/P²,t/P,1,tP] has W=128a(6t²+4t−1)/P². Verified the maxima of entries and the sum of the seven multilinear errors:61440H+6144H²+192H³. With Cstar<2^98,y(64)>2^128 and growth of y/t, the margin Wmixed/Phi⁴>6t²/y² holds for ALLt>=64. It is an analytic proof, without theta samples.

A negative Dmix, together with the positive tail, would discard only global Chebyshev4 of THIS family by opposite orientations of determinants near confluence. A positive Dmix would only verify a neighbourhood of the origin without radius. Neither case decides the crossing of the particular forcing U nor its primitive, kernel, W or all orders. The first three global prefixes103 remain proved.

## Literal before execution

Read in full `tools/power_mixed_four_origin_104_verify.py`. It checks the hash087 BEFORE runpy; it extracts Phi0 and the normalized coefficients z1,z2,z3 from a[1:4], according to the literal087. The four moments103 and radii are exact Fractions before their outward conversion to I70. It keeps the denominator checks and1/25<a<1, matrix of lambda derivatives and24 permutations with correct sign. The assert admits either sign and does not adjust parameters. It prints recovered rational endpoints for later persistence. The recovery and the single gate were authorized; no data had been run in the audit and its sign was not anticipated.

## Result and reproduction

The fixed gate ended **POSITIVE**, both in the run and in the independent reproduction. Identical hash104:`063ce9ba28dc9b0e3cca245018a968794b5b28c7a57df5da7a5c70d008b95105`. Exact endpoints copied from `tools/power_mixed_four_origin_104_verify.log`:

- lower: `20910875038731301173957476100644455719909401587771537215845430471153/5000000000000000000000000000000000000000000000000000000000000000000000`;
- upper: `41821750077462602464978622735022256356361140514400545338810504099651/10000000000000000000000000000000000000000000000000000000000000000000000`.

The same log keeps the complete recovery087 and the rational endpoints Phi0,z1,z2,z3. Quadrature103 was not repeated and the design was not adjusted. Dmix>0 and ORIGIN prove mixed W4 positive on an existing neighbourhood of the origin, WITHOUT explicit radius. Together with the exterior analytic proof one has positivity for ALLt>=64. The intermediate compact remains OPEN; there is no falsifier, global Chebyshev4, finite U crossing, finite Xi positivity nor new W/T/allorders coverage. No other test is authorized by this conclusion.

## Audit of the analytic extension: keeping powers of the remainder reduces the tail to t>=16

**PROVED / independent review, without new theta data.** In the seven multilinear terms of§5 it is not necessary to discard all additional powers of y. Keeping them one obtains

`error <=61440 Hstar t³/y³+6144 Hstar² t³/y⁴+192 Hstar³ t³/y⁵`.

The three simple terms have y^-3; the three double ones have y^-4 and the triple y^-5. The same entry majorants and1+t<=2t are kept. For y>=Hstar, the error is less than2^17 Hstar t³/y³, since61440+6144+192=67776<2^17.

With Hstar=39321600, positive Taylor up to degree5 proves exp2>7; the exact integer computation gives

`3*7^16=99698791708803 >16*2^17*Hstar=82463372083200`.

Hence y(16)=pi exp32>3*7^16 and, since y/t grows for t>1/2, for ALLt>=16 one has y>=Hstar anderror<t²/y². The previous model is larger than7t²/y², so that

`Wmixed(t)/Phi(t)^4>6t²/y²>0 for ALLt>=16`.

It is an improvement of the remainder of104, not a new evaluation of theta nor a change of parameters of110. Run110 is kept intact. No sign of the compact nor global coverage is inferred without the corresponding proofs and reproduction.
