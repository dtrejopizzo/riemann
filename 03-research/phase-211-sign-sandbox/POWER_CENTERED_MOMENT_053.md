# POWER_CENTERED_MOMENT_053 — An exact matrix moment reduces the cutoff to96

Status: **PROVED with rational certificate; independent audit approved in POWER_CENTERED_MOMENT_AUDIT_053.md.** Only dimension13, ALL numerators and ALL j>=96. Papers untouched.

## 1. Corpus, prior choice and difference

Consulted ROUTES-TRIED-INDEX/README, the master grid, CROSSWORD-TO-D, HIGHPASS015, CENTERED_CUTOFF049 and DIMENSIONAL_CUTOFF051 with its audited correction. The uniform bound051 allows paying two contacts via a larger cutoff (for example128). The difference here is to certify the EXACT inverse moment of a whole block of dimension13, instead of reusing the IBP majorant051 as new.

J=96 and b=1/5 were fixed BEFORE the computation: a single rational trial to reduce that cutoff128 by a quarter and obtain ARCH>12/5. This choice was recorded beforehand. No other J, no numerator and no parameter grid was tried. The matrix has dimension13, although the highpass order is96. The script `tools/power_centered_moment_053_verify.py` executes only that certificate and rational constants.

## 2. Exact binomial Gram and positivity of the moment

On the circle z=exp(i theta), q=(2+z+zbar)/4=|1+z|²/4. If A(z)=sum_(a=0)^12 A_a z^a, the orthonormal Laguerre correspondence gives exactly the spectral probability of Q^j F0 as q^j|A(z)|² dtheta, normalized. Here F0 ranges over ALL of V13.

The matrix of the integral against dtheta/(2pi) is

    (T_j)_(a,b)=4^(-j) binom(2j,j+a-b), 0<=a,b<=12,

understood as zero if the index lies outside0,...,2j. Proof: expand

    q^j=4^(-j)z^(-j)(1+z)^(2j)

and take the constant coefficient after multiplying by z^(a-b). Binomial symmetry makes swapping a-b with b-a irrelevant. T_j is positive definite: q^j>0 except at one point of the circle and a nonzero polynomial has only finitely many roots.

The ratio r_j=E[(1-q)/q] satisfies

    r_j = A* (T_(j-1)-T_j) A / (A*T_j A).

Hence r_96<1/5 for ALL A!=0 is equivalent to (6/5)T_96-T_95 being positive definite. Multiplying by4^96 gives the FINITE rational matrix

    M_(a,b)=(6/5)binom(192,96+a-b)
                         -4binom(190,95+a-b).

The verifier checks the THIRTEEN LDL pivots are strictly positive in Fraction arithmetic, without floating eigenvalues. The certificate is also valid for complex coefficients because the matrix is real symmetric.

## 3. All later j, without other certificates

For each fixed A, passing from j to j+1 reweights by q. Since (1-q)/q decreases in q, the covariance is nonpositive. Hence r_(j+1)<=r_j. All integrals are finite for j>=1. One obtains simultaneously for ALL j>=96 and ALL F0!=0 in V13,

    r_j<1/5,
    E_(Q^jF0)[tau^-2] < 1/(5u²)=4/19845, u=63/2.       (MOMENT)

It is not required that the same A minimize each index; monotonicity holds for EACH A and the initial certificate covers ALL A.

## 4. ARCH and two contacts with exact constants

By Jensen, Cauchy and the digamma bound of017/051,

    ARCH/||G||²
      > log[u sqrt5/(2pi)] - 2/sqrt19845 - 2/19845.

One has sqrt5>559/250 and pi<22/7, whence u sqrt5/(2pi)>56/5. Moreover2/sqrt19845<1/70 and2/19845<1/9800. Finally

    log(56/5)>12/5+1/70+1/9800

is verified with the first32 POSITIVE terms of the atanh series, of argument51/61. Neither a remainder nor a decimal evaluation is needed: a lower positive prefix already exceeds the indicated rational. Consequently

    ARCH[Q^jF0] > (12/5)||Q^jF0||², j>=96.             (ARCH)

The real coefficients of the contacts satisfy v2=sqrt2 log2<1 and v3=2log3/sqrt3<77/60<13/10. One uses log2<7/10, sqrt2<10/7, log3<11/10 and sqrt3>12/7. The absolute value of each correlation is bounded by the squared norm, so

    (ARCH+contact2+contact3)[G] > (7/60)||G||².

No favorable sign of the contacts is presumed.

## 5. Polar and scope of E23

In V13, the exact polar bands are

    p_k=(63/992)(-1)^k[(32/31)^k+(31/32)^k], 0<=k<=12.

The verifier checks |p_k|<1/5. The norm of the polar matrix is less than13/5<3 by row sums. The elementary proof of ENDPOINT048 for dimension13 gives <qF,F>>=||F||²/(4·13²)=||F||²/676. Log-convexity of the moments q^j implies ||Q^jF||²>=676^(-j)||F||². Hence

    |Polar[Q^jF]|/||Q^jF||²
       <3(676/3968)^j=3(169/992)^j<3·5^(-j)<1/1000

for all j>=96. Defining E23=ARCH+POLAR+contacts2,3, one gets

    E23[Q^jF]>(1/10)||Q^jF||²,
    ALL j>=96, ALL F!=0 inV13.                      (TAIL-E23)

The bound uses7/60-1/1000>1/10. It does not contain the contacts n>=4. For a claim about complete W one still has to pay that tail and treat the segment j=1,...,95; positivity of base V13 and any later transport are separate obligations. That segment has not been certified here, and no global sign is concluded.
