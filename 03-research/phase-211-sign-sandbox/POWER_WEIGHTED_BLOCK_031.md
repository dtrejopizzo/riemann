# POWER_WEIGHTED_BLOCK_031 — Adverse weighted prefix and real recovery at 4

Status: **PROVED**, independent review approved and verifier PASS reproduced. FIXED rate u=63/2. With X0=225/64=(15/8)²:

    int_1^X0 G_N H<−3/1000       for ALL N>=2^24,
    int_1^4 G_N H>3/200          for ALL N>=2^22,
    int_X0^4 G_N H>9/500         for ALL N>=2^24.        (REAL)

These are not total values of W. Rest of the balance and global sign OPEN. Papers untouched. No campaign over contacts is continued.

## 1. Corpus and new reason

Read the project rules, INTERIOR_SCALE030 and its audit; identity JOINT-G, weighted primitive I_* and local gamma error. Consulted the index ROUTES-TRIED-INDEX, master grid and CROSSWORD-TO-D.md on weighted means, primitives, Euler/Möbius and blocks 030. The primitives of H and x²H refuted in 030 are NOT the object here.

The difference is to incorporate the NEXT contact, q=3, into the primitive weighted by G_*=(3/2)x^(-1/2), and check whether its sign can serve the real pairing. The universal premise I_*>=0 already fails after that contact. But, before pivoting, a QUANTITATIVE recovery of the real gamma block is extracted, uniform in N and at fixed rate. No isolated dimensions are certified and no other model is used in place of G_N.

Only an adverse prefix motivated inside (3,4), with rational square endpoint X0, and the endpoint 4 completing the cell of contact 3 are evaluated. Contact 4 is at the endpoint and its integral contribution is exactly 0. No list of signs for more contacts is generated.

## 2. Real weight and correct primitive

Keep 030:

    G_N(x)=x^(-1/2)[(3/2)rho_N(logx)−rho_N'(logx)]>0,
    H(x)=1+[log((x+1)/(x−1))+c−1−2Psi_1(x)]/x²,
    c=−gamma−log(4pi), Psi_1(x)=sum_(q<=x)qLambda(q),
    W[g_N]/norm²=int_1^infty G_N(x)H(x)dx.

The primitive under study is

    I_*(X)=int_1^X G_*(x)H(x)dx, G_*=(3/2)x^(-1/2).

Integrating each arithmetic step, with EVERY contact q<=X,

    I_*(X)=3(sqrtX−1)+(c−1)(1−X^(-3/2))+(3/2)J(X)
       −2sum_(q<=X)Lambda(q)/sqrtq
       +2X^(-3/2)sum_(q<=X)qLambda(q),                  (I)
    J(X)=int_1^X x^(-5/2)log((x+1)/(x−1))dx.

Each endpoint contact q=X cancels exactly between the two sums. No jump with favorable or adverse value is omitted.

For z=sqrtX>1, the integration by parts of 030 gives the closed form

    J(X)=(8/3)(1−1/z)−[2/(3z³)]log((X+1)/(X−1))
        +(2/3)log((z+1)/(2(z−1)))
        −(4/3)arctan((z−1)/(z+1)).                       (J)

At X0, z=15/8 and the arctan argument is 7/23. At X=4, z=2 and the argument is 1/3. The two formulas contain only constants with explicit rational intervals, not a numerical quadrature.

## 3. What happens after contact 3

At both endpoints only q=2 and q=3 contribute (q=4 has coefficient 0 at X=4). Their real values are Lambda(2)=log2, Lambda(3)=log3. The exact certificate proves

    I_*(225/64)<−1/250,
    I_*(4)>1/50.                                        (WEIGHTED)

Used: 140/99<sqrt2<99/70 and 265/153<sqrt3<97/56, checked by squaring. The negative bounds are obtained with the smaller reciprocals; the positive ones with the larger reciprocals, keeping the correct direction of each term −2Lambda(q)/sqrtq.

For orientation, without using them in the proof, the values are approximately −.0047659 and +.0251073. WEIGHTED refutes exactly the premise «the weighted primitive I_* is nonnegative for all X». It does not refute the sign of W nor authorize ignoring the subsequent recovery interval.

## 4. Uniform transfer to the REAL G_N, without another certified N

By 030, for real y,

    |rho_N(y)−1|<=M2_N y²/2,
    |rho_N'(y)|<=M2_N |y|,
    M2_N=u²/(2N−3).

On 1<=x<=4 one has logx<=log4<7/5. Hence

    |G_N(x)−G_*(x)|
      <=M2_N[(3/4)(logx)²+logx]<3M2_N.                  (G-ERROR)

Also

    int_1^4 |H(x)|dx<10.                               (H-NORM)

To prove it, the length is bounded by 3, the constant part by (23/5)(3/4), the logarithmic kernel by 2log2<7/5, contact 2 by 4log2 int_2^4 x^(-2)dx<7/10 and contact 3 by 6log3 int_3^4 x^(-2)dx<11/20. Their sum is 9.1<10. The value of contact 4 at the endpoint does not alter the integral.

Thus for ANY X<=4,

    |int_1^X(G_N−G_*)H|<30u²/(2N−3).                    (ERROR)

At FIXED rate u=63/2, the majorant is <1/200 for ALL N>=2^22 and <1/1000 for ALL N>=2^24. There is no sweep or individual certificate per N: an explicit decreasing function of N is used.

Combining ERROR and WEIGHTED gives the first two REAL bounds. For N>=2^24, subtracting them on the SAME real gamma function proves the recovery

    int_X0^4 G_NH>3/200+3/1000=9/500.

In particular the adverse real prefix does not disappear when incorporating the gamma datum: for every N in the declared range a negative contribution persists. The extended block compensates it quantitatively before reaching 4.

## 5. Relation to the real factor and global obligation

Write R_N=G_N/G_*=rho_N−(2/3)rho_N', with rho evaluated at logx. On finite intervals,

    int_1^X G_NH=R_N(X)I_*(X)−int_1^X I_*(x)dR_N(x).

On the whole half-line the boundary term vanishes, by the gamma decay and the at most polynomial growth of I_*, and one gets W/norm²=−int I_*dR_N. This identity is not a new sign inequality. The shape and variation of the real factor R_N are analyzed in parallel in POWER_GAMMA_WEIGHT_031.md; it is not assumed monotone from 1.

WEIGHTED shows why even a favorable property of R_N needs to compare intervals: I_* has a real adverse region. REAL supplies a concrete compensation, but does not say that all blocks admit the same pattern nor that adding positive blocks closes the form.

The list of contacts is not extended here. The next requirement is a pairing inequality that uses the gamma factor and controls the adverse contributions of ALL contacts against the favorable ones, keeping the full weight. Only the block up to 4 is resolved. The rest int_4^infty G_NH remains open, and cannot automatically be replaced by a positive tail of another representation without accounting for the truncation changes.

## 6. Evidence

Verifier: tools/power_weighted_block_031_verify.py, Fraction and exact intervals; PASS. It checks the two inequalities of WEIGHTED, the coefficients of G-ERROR/H-NORM and the analytic thresholds. The uniformity in ALL N of REAL is proved above. Not claimed: total W negative or positive, a new window T, or global closure. Papers untouched.
