# POWER_THETA_G_COMPACT_080 — Remaining curvature and three generators on the WHOLE admissible range

Status: **PROVED, complete certificate exit0/PASS and reproduction 92790 exit0/FULL PASS, independent audit approved.** See `POWER_THETA_G_COMPACT_AUDIT_080.md`. Neither four generators, all orders nor a new time window are proved. Papers untouched.

## 1. Exact obligation and antecedents

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; read 073–079 and the corresponding audits. 073 proves M increasing, strictly concave and M(0)=0 for the mean of the real theta tilt. 079 proves, under those properties, that all three-node blocks of an interval are positive semidefinite IF AND ONLY IF

    g(x)=a sqrt(x)/M(sqrt(x))−1

is concave in their squares, with a=M'(0)>0. Its minimal proof requires neither concavity of 1/b nor the additional result 077. 078 already proves g''<0 for u=sqrt(x)>=63/2. For admissible exponents A=u+1/2>1, only 1/2<u<63/2 is missing, not the origin u=0.

Here that SINGLE compact obligation is proved, with all constants and the complete arithmetic function. No triples or eigenvalues are selected, no sequence of new dimensions is certified and the sign is not inferred from samples. The change relative to the previous enclosures is to use jets only at EXACT centres and a uniform analytic Cauchy remainder, derived from the positive theta density; not to evaluate jets of the deflated function on wide balls near its polar cancellation.

## 2. Scalar curvature and complete regularization at A=1

Let Z(u)=∫_R Phi(t)e^(ut)dt and M=Z'/Z, as in 073. With c=M(u), d=M'(u), e=M''(u), define

    Delta(u)=c²+ucd+u²ce−2u²d².

Exact differentiation gives

    g''(u²)=−a Delta(u)/(4u³c³).                     (CURVATURE)

For u>=1/2, c>0. Therefore it suffices to prove Delta>0. The arithmetic formula of CONE001 identifies Z, up to a positive constant irrelevant for M, with the real entire function

    E(A)=A[1+(A−1)zeta_deflate(A)]Gamma(A/2)exp(−A logpi/2),
    A=u+1/2,
    zeta_deflate(A)=zeta(A)−1/(A−1).

The deflation does NOT mean (A−1)zeta(A). The entire product Q=1+(A−1)zeta_deflate(A) is what avoids evaluating the pole at A=1. There Q=1 and E(1)=1. Using A=1 as a regular endpoint does not claim separate convergence of the polar and the comb of the boundary test: the original exponents of the conclusion are strictly greater than 1.

The meaning of deflate and the series were cross-checked against the installed API python-flint 0.9.0, the local FLINT headers and the official documentation:

- https://arblib.org/arb_poly.html
- https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html

The documentation specifies the function ζ(s,a)+1/(1−s) when deflate is nonzero. The self-tests E(1) and the agreement of regularized jets with the ordinary formula at A=2 only validate the implementation; the mathematical identity comes from the explicit deflation, not from those two tests.

## 3. A uniform real bound for the Cauchy discs

Fix r=1/16. For all centres c0 in [1/2,63/2], c0+r+1<=32+9/16<33+1/2. The monotonicity of M from 073 and the arithmetic formula at A=34 give

    M(t)<=M(33+1/2)
      <1/34+1/33+(1/2)log[34/(2pi)]
      <2/32+(1/2)log6 <1,

for 1/2<=t<=c0+r+1. Only the negative arithmetic term of M was discarded for this UPPER bound. We used pi>3, psi(y)<=log y and log6<9/5; the latter is verified with a positive Taylor sum of exp(9/5)>6. The rational term is not bounded by 2/32 pointwise at small rates: first the monotonicity up to the anchor 33+1/2 is used.

Hence

    Z(c0+r+1)/Z(c0)
      =exp[int_(c0)^(c0+r+1)M(t)dt]
      <exp(17/16)<3.                               (RATIO)

For the last constant e<11/4 and exp(1/16)<16/15 suffice, which give exp(17/16)<44/15<3. The bound e<11/4 is proved by summing up to degree 3 and paying from degree 4 on the geometric series of ratio 1/5: e<=8/3+5/96<11/4.

## 4. Complete complex bound of Delta, without interval jets

For |z−c0|<=r and k>=0, positivity of Phi and |t|^k<=k!exp(|t|) give

    |Z^(k)(z)|
      <=k![Z(Re z+1)+Z(Re z−1)]
      <=2k! Z(c0+r+1)<6k! Z(c0).

The last comparison uses the parity of Phi and the monotonicity of Z with respect to the modulus of its real argument. The segment between c0 and z remains in the disc, so

    |Z(z)−Z(c0)|<=2rZ(c0+r+1)<(3/8)Z(c0),
    |Z(z)|>(5/8)Z(c0).

Thus M=Z'/Z and its derivatives are analytic there and satisfy

    |Z^(k)(z)/Z(z)|<(48/5)k!, k=1,2,3,
    |M|<10,
    |M'|<120,
    |M''|<2700.

Indeed one uses M'=Z''/Z−(Z'/Z)² and M''=Z'''/Z−3Z'Z''/Z²+2(Z'/Z)³. The exact intermediate bounds are 48/5, 96/5, 288/5. Since |z|<32 on all these discs,

    |Delta(z)|
      <10²+32·10·120+32²·10·2700+2·32²·120²
      <60000000=:B.                                (CAUCHY-BOUND)

No sign of the form on complex data is invoked. Only an absolute analytic error is derived for the SAME entire arithmetic function that is evaluated on the real axis.

## 5. Fixed partition and exact remainder

The 4096 equal intervals cover [1/2,63/2]. They have radius h=31/8192 and exact centres

    c_j=[4096+(2j+1)31]/8192, j=0,...,4095.

For Delta(c_j+t)=ΣD_k(c_j)t^k, the coefficients D_k are normalized by k!. Cauchy and CAUCHY-BOUND give, uniformly in |t|<=h,

    |Σ_(k>=17)D_k t^k|
      <= B(h/r)^17/(1−h/r)=epsilon,
    h/r=31/512,
    epsilon=5285183618944392932503807265625/
            41901009533176678637026095660718210485846016
      <10^(−12).                                   (TAIL)

It is an error for the WHOLE Taylor tail, not only the next coefficient. The verifier uses the exact fraction TAIL, not the decimal upper bound 10^(−12), when checking the sign.

At each centre, ball arithmetic at 256 bits encloses D0,...,D16 of the complete function. The sufficient assert is

    D0.lower−Σ_(k=1)^16 |D_k|.upper h^k−epsilon>0.     (PANEL)

The function is not evaluated on a mesh and interpolated without remainder. PANEL proves the sign on each whole interval, including its endpoints.

## 6. Implementation, enclosure failures and reproduction

The code is tools/power_theta_g_compact_080_verify.py. It uses REAL arb_series, precision 256 bits and cap 20: logE has coefficients up to degree 19; M up to 18; M'' up to 16; Delta keeps the 17 necessary coefficients. Delta.prec>=17 and finiteness of ALL D0,...,D16 are required. Before logE, E0>0 is required. The real entire function is evaluated only at exact centres, with jets of special functions and complete FLINT errors; no sum over primes is truncated without tail.

The partition 4096, the domain, the precision 256 and the strict margin >0 were fixed before running and were not adjusted to results. The first enclosures tried to use coefficient 6 on a parameter ball. The direct enclosure and its Taylor2/Taylor4 corrections failed because of loss of dependency near the cancellation of the pole of ζ. The central values were positive, but those FAILs did NOT prove the sign on the panels nor constitute a counterexample to the curvature. History and scope were kept. Increasing only the jet order did not resolve that cause: the last interval failure was on panel 1, with an excessive remainder.

The final representation eliminates ALL evaluations of ζ on parameter balls and replaces them by the external remainder TAIL proved above. r=1/16, B=60000000, degree 16/cap 20 were fixed and their formulas audited BEFORE the run of that representation. It was a mathematical correction of the enclosure of the same objective, not a sweep of hypotheses or sign parameters.

Run

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_g_compact_080_verify.py

Run 43260 finished exit0, PASS of regularization and PASS of ALL 4096 panels. The SHA256 of the script that finished is

    640d8eb8ecf2bce7e782e08333a722171744af8fc0c9831582fcfcb796fb09bc.

Run 92790 independently reproduced the complete certificate: exit0/FULL PASS 4096 and the same hash. That script was not modified while it ran. The asserts are proofs with rigorous intervals and rational constants; no eigenvalue or floating-point number was used as a sign premise.

## 7. Splice and conclusion on three generators

PANEL proves Delta>0 on [1/2,63/2] and CURVATURE gives g''<0 there. 078 proves the same curvature for u>=63/2 via uniform arithmetic bounds. Therefore

    g''(x)<0 for ALL x>=1/4.                        (GLOBAL-ADMISSIBLE)

073 supplies all BASE properties of 079. For any three distinct exponents A1,A2,A3>1, their nodes ui=Ai−1/2 are >1/2 and g is strictly concave on their whole interval of squares. The secant theorem 079 proves that

    K_ij=[L(Ai)+L(Aj)]/(Ai+Aj−1), i,j=1,2,3,

is POSITIVE DEFINITE. It is the COMPLETE real form of the three exponentials, with ARCH, polar and ALL contacts. The diagonal congruence of the exterior map preserves the sign on any real combination of three powers with exponents >1.

If some exponents coincide, coefficients are combined and the case of one or two generators proved in 073 remains: the redundant matrix is positive semidefinite and the energy is positive for every nonzero represented FUNCTION. Positive energy is not attributed to a nonzero vector representing the zero function.

## 8. Exact limit of the advance

The result extends from ALL pairs 073 to ALL admissible triples, not only to large rates already covered by 053. It does not require concavity of 1/b. It does not prove four generators, all orders nor the complete linear span; nor does it modify a window T of the paper or close its global sign. The papers remain untouched.
