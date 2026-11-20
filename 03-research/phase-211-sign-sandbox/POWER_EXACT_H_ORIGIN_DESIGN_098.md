# POWER_EXACT_H_ORIGIN_DESIGN_098 — Prior design and decision of the exact jet of T_h

**Update099:** the REAL obligation T_h>0 globally was closed in `POWER_EXACT_H_GLOBAL_DESIGN_099.md`, audited in `POWER_EXACT_H_GLOBAL_AUDIT_099.md` and summarized in `POWER_STATE_099.md`. Both curvatures and all triples of the remainder G_p are proved; the auxiliary block of five nodes is anchored at0 and they are NOT five admissible W generators. The mentions of compact set/pending hypothesis below keep the historical status of this round; inheritance to the next level remains open.

**Independent audit:** `POWER_EXACT_H_ORIGIN_AUDIT_098.md` approved; run19778 exit0/FULL PASS, independent reproduction run57072 exit0/FULL PASS128 and matching hash.

Status: **PROVED POINTWISE by the main run exit0/FULL PASS; design and literal text independently approved BEFORE the run.** Final reading and independent reproduction pending. The previous design is kept; result in§6. Papers untouched.

## 1. Difference, antecedents and object

Consulted the project rules, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D, and073/077/078/087/090/092/093/095. The abstract Hankel/Schur identities are already registered; they do not by themselves prove a sign.093 verified a jet of a stronger density condition. Here the EXACT condition T_h(0) is decided, using only six moments of the SAME real Phi. No new pivots or samples; no global sign is inferred from the origin.

With Z(u)=integral_R exp(ut)Phi(t)dt, M=Z'/Z, x=u² and

    N(x)=M(u)/u=a+b x+c x²+d x³+e x^4+O(x^5),
    h(x)=xN(x)/(a−N(x)),
    T_h=2h'h'''−3(h'')²,

the exact algebraic regularization gives

    T_h(0)=12a H3/b^4,
    H3=det[[a,b,c],[b,c,d],[c,d,e]].

Here a=κ2,b=κ4/6,c=κ6/120,d=κ8/5040,e=κ10/362880, with κ the cumulants of the probability Phi/Z(0).The variance073 gives a>0;086/097 give R'(0)>0 for R=1/N, and from R'(0)=−b/a² one obtains b<0. That strict inequality is not deduced only from M''<0 for u>0. The script will also check that its intervals verify those inequalities before the comparison. H3 is not treated as a determinant of generic positive moments: they are cumulant coefficients and their sign is the requested test.

Define Ir=integral_0^infinito t^rPhi(t)dt for r=0,2,4,6,8,10. The normalized moments are mr=Ir/I0. The even series Z(u)/Z(0)=sum_(k=0)^5 m_(2k)u^(2k)/(2k)!+O(u^12) is formed, with m0=1 exactly. Differentiating its logarithm up to degree9 produces a,b,c,d,e without requiring moments of order greater than10. The implementation must respect the known formal precision: Z.prec>=11 and M.prec>=10, without filling in unknown coefficients.

## 2. Prior parameters, identical to093

On[0,2],128panels, centres(2j+1)/128,j=0,...,127, h=1/128. Cauchy radius r=1/32, ratio1/4. Taylor degree64, cap65, precision512bits, theta modes1,...,16. No tuning after observing the sign.

The already audited design093 proves on the complex discs

    −1/32<=Re t<=65/32, |Im t|<=1/32,
    |Phi(t)|<2^22, |t|<3,
    EPS=2^25*17^4/8^289

for the COMPLETE tail of modes m>=17. The only new complex majorization needed is

    |t^(2k)Phi(t)|<3^10*2^22<10^12, k=0,...,5.

EPS*32^j is added to ALL coefficients Phi[j],j=0,...,64, before multiplying by each t^(2k). No previous mesh is imported or executed to compute these moments.

## 3. Fixed integration error

Each Taylor polynomial of degree64 of t^(2k)Phi is integrated exactly on the symmetric panel: even terms2coef[j]h^(j+1)/(j+1), odd terms0. Roundings are outward interval.

With the new bound10^12 and total length2, the TOTAL error of the complete expansion is

    REM=2*10^12*4^(−65)/(1−1/4)<10^(−24).

It is added symmetrically to each moment. This Cauchy remainder is added to the theta errors already propagated in the coefficients; it does not replace the theta tail nor is it estimated from observed values.

## 4. New temporal tail, valid up to order10

093 already proved, keeping all modes,

    0<Phi(2+s)<2^(−140)exp(−300s), s>=0.

For all orders r=0,2,4,6,8,10,

    (2+s)^r<=2^10 exp(5s),

by log(1+s/2)<=s/2. Hence

    0<integral_2^infinito t^rPhi(t)dt
       <(1024/295)*2^(−140)<2^(−138).

TAIL=2^(−138) is fixed for ALL six moments and the positive interval[0,TAIL] is added. Do not use the tail2^(−140) of093, which was fixed only for orders0,1,2.

## 5. Prior test and scope

The implementation will verify the positivity and finiteness of the six moments, the finiteness of the series and the formal precisions above. H3 will be evaluated by the exact polynomial formula

    H3=a*c*e−a*d²−b²*e+2b*c*d−c³.

The decision assert accepts H3>0 OR H3<0. If the intervals do not separate0, it is reported inconclusive without modifying parameters to force an answer. Positivity is not predetermined.

A positive sign only proves T_h>0 near the origin on an unquantified neighbourhood; a negative sign would refute the sought global property for the real Phi, but would not be a counterexample to W. Neither decides the whole remaining interval nor all orders. No new window T.


## 6. Main run result and exact scope

After mathematical and literal approval, the SINGLE run19778 ended exit0/FULL PASS128panels, without changes of code, precision, parameters, modes or remainders during the run. The test that accepted either sign obtained

    PASS098: exact T_h(0) sign POSITIVE.

Outward interval output of Arb:

    I0 [0.12428019454707852747819343 +/- 6.89e-27]
    I2 [0.00574298607878635938381247 +/- 2.84e-27]
    I4 [0.00074071210842190804134207 +/- 6.71e-27]
    I6 [0.00014982398664939487296086 +/- 5.39e-27]
    I8 [4.024164363754890272123e-5 +/- 2.69e-27]
    I10 [1.325965856957266369438e-5 +/- 2.26e-27]
    a [0.0462099862308379415778676 +/- 3.74e-26]
    b [-7.434519857053937232973e-5 +/- 5.94e-27]
    c [2.88347862801946559391e-7 +/- 4.83e-28]
    d [-1.3260633605059817397e-9 +/- 5.73e-29]
    e [6.427328301233202432e-12 +/- 4.61e-31]
    H3 [1.73824840842099742e-21 +/- 6.84e-39]
    Th0 [3.1551297417482263e-5 +/- 5.03e-22].

The proof of the sign is the strict interval comparison of the script, not the substitution of the centres of these intervals. a>0 and b<0 are also verified before the quotient. All moments include the complete mode tails, the quadrature remainder and the temporal tail up to order10. No abstract positivity of Hankel matrices is used to replace that signed computation.

Thus **T_h(0)>0 for the REAL Phi**. The regularization of§1 is analytic near0 because b!=0, and by continuity T_h(x)>0 on an existing neighbourhood of x=0, without certified radius. This exact local premise is verified; it is not refuted nor is its sign inferred on the whole intermediate interval. The node0 is auxiliary for the anchored criterion, not a new admissible exponent of W. No new number of generators, global sign, all orders or window T.

Command from the repository root:

    python3 03-research/phase-211-sign-sandbox/tools/power_exact_h_origin_098_verify.py

SHA256 of the fixed script:

    bebcca70c5dd54ba53841e77542aa3e3e2ea059306061dc676e24f88ee5117c9.

The script is self-contained: it does not import or execute the runs087/093, although it keeps their already audited analytic bounds and quadrature scheme. The audit098 is approved and run57072 reproduced exit0/FULL PASS128 with the same hash.
