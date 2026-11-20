# POWER_EXACT_H_GLOBAL_DESIGN_099 — Fixed design and global proof of the exact obligation T_h

**Independent audit:** final source, design and literal text approved in `POWER_EXACT_H_GLOBAL_AUDIT_099.md`; run98529 FULL PASS2048, independent reproduction run8310 exit0/FULL PASS2048 and matching hash. Exact application: `POWER_SCHUR_TRIPLES_APPLICATION_099.md`; status: `POWER_STATE_099.md`.

Status: **PROVED by the main run and independent reproduction run8310 exit0/FULL PASS2048; final reading and audit approved, matching hash.** Design and literal text were independently approved BEFORE the single run. The previous design and its analytic history are kept; the result is in§8. Papers untouched.

## 1. Object, antecedents and change of representation

Consulted the project rules, README ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D, and073/077/078/080/085/089/090/092/093/095/097/098.097 proved the EXACT obligation T_h>0 for u>=512;098 decided T_h(0)>0 by six complete moments. The pointwise density conditions093/095 are stronger and are not presupposed global.090 refutes a generic Turán inheritance; it is not retried.

This design addresses directly the remaining compact set using a regularized ENTIRE function. No new matrix, sufficient density condition or mere samples of T_h are certified. The mechanism of central jets and Cauchy080/085 is reused, but the denominators and the algebraic zero u^15 are eliminated BEFORE fixing the test. The difference is essential to prevent a triangular variation bound from losing the sign only because of that known factor.

Let E be a positive constant multiple of the transform Z of Phi, M=E'/E,a=M'(0)>0,x=u² and

    N(x)=M(u)/u,
    h(x)=xN(x)/(a−N(x)),
    T_h=2h'h'''−3(h'')²,

with derivatives of h with respect to x. Define the entire functions in x

    U(x)=E'(u)/u,
    V(x)=[aE(u)−U(x)]/u².

Their entireness comes from the parity of E and from aE(0)=E''(0): U=2dE(sqrt x)/dx; the numerator of V has zero constant term. It is not presupposed that h=U/V is entire nor that V lacks complex zeros.

With derivatives with respect to x, put Wij=V^(i)U^(j)−V^(j)U^(i). The exact polynomial identity is

    NUM_x=−W_x(V,xV,U,xU)
         =2W01W03+6W01W12−3W02².

It is entire without denominators. On reals x>0, V>0 by073 and NUM_x=V^4 T_h.

## 2. Integer polynomials in E and regularization of the zero15

Put ej=E^(j)(u),j=0,...,4, derivatives NOT normalized by factorial. Define

    PS=u^4(2e0²e2e4−3e0²e3²−2e0e1²e4+10e0e1e2e3
             −6e0e2³−4e1³e3+3e1²e2²)
       +u³(2e0²e1e4−6e0²e2e3−2e0e1²e3+12e0e1e2²−6e1³e2)
       +u²(6e0²e1e3−9e0²e2²+3e1^4)
       +u(6e0²e1e2−6e0e1³)+3e0²e1²,

    PC=u³(e0e1²e4−6e0e1e2e3+6e0e2³+2e1³e3−3e1²e2²)
       +u²(6e0e1²e3−12e0e1e2²+6e1³e2)
       +u(3e0e1²e2−3e1^4)+3e0e1³,

    Ntilde=a u PS−4PC.

PS=E^4 N_S and PC=E^4 C_h, with N_S,C_h defined and audited097. PS has18monomials, absolute sum of coefficients91 and degree in u<=4; PC has11monomials, sum51 and degree<=3. All are homogeneous quartic in e0,...,e4.

The formula DIRECT097 and NUM_x=V^4T_h, first for u>0 and then by identity of entire functions, give

    Ntilde(u)=(16/a)u^15 NUM_x(u²),
    S(u)=Ntilde(u)/u^15=(16/a)NUM_x(u²).          (ENTIRE-S)

Hence S is ENTIRE and EVEN, with the removable division already justified. Its value at0 is S(0)=192E(0)^4H3>0 by098. Entireness rests on U,V and ENTIRE-S, **not** on assuming that the meromorphic T_h lacks complex singularities.

On reals u>0, S>0 is exactly equivalent to T_h>0. The implementation will evaluate the quotient at strictly positive centres; 0/0 is not evaluated. The following Cauchy bound is applied to the real entire S, not to an arbitrary family where a is varied breaking aE0=E''0.

## 3. Complete growth bound, without zero-free discs

Positivity of Phi and parity of E give, for each real centre c>=0,|z−c|<=r and each j>=0,

    |E^(j)(z)|<=2j! E(c+r+1).

One uses |t|^j<=j!exp(|t|) under the integral; all tails are kept. For c<=512,r=1, the real monotonicity073 and the complete gamma/arithmetic anchor guarantee M(t)<3 up to514. An elementary check can use the anchor A=516: psi(A/2)<=log(A/2), the favourable prime term and pi>3 give M(515.5)<log86/2+1/516+1/515<3, since86<(8/3)^5<exp5. Monotonicity extends the upper bound to the whole required interval.

The audited elementary bound exp1<87/32 and(87/32)^6<512 give exp6<512. Thus E(c+2)/E(c)<exp6<512 and on the disc of radius1,

    |ej|/E(c)<1024j!<2^15, j<=4,
    |u|<513<2^10, a<8.

The bound a<8 is amply contained in the certified interval098, and will also be checked for its pointwise refinement. By the coefficient sums of§2,

    |PS|/E(c)^4<2^107,
    |PC|/E(c)^4<2^96,
    |Ntilde|/E(c)^4<2^121.                       (RAW-BOUND)

It is not required that E(z) be non-zero on the disc: its complex quotients and logarithms do not appear in these polynomials.

## 4. Uniform bound on S through the removable origin

If |z|>=1/4 inside a previous disc, RAW-BOUND implies

    |S(z)|/E(c)^4<2^121*4^15=2^151.

For |z|<=1/4 use a circle centred at0. Since E(c)>=E(0), the same derivative inequality and M<3 give on |z|=1/4

    |ej|/E(c)<=2j! E(5/4)/E(0)
               <128j!<2^12, j<=4.

Here exp(15/4)<64, by log2>56/81. Moreover |z|<=1 and a|z|<2. By the sums91 and51 one obtains |Ntilde|/E(c)^4<2^57 on that circle. ENTIRE-S and the maximum principle, applied to the already removed function, give on ALL of |z|<=1/4

    |S(z)|/E(c)^4<2^57*4^15=2^87.

Both cases prove on each disc |z−c|<=1,c in[0,512], the single fixed bound

    |S(z)|/E(c)^4<2^151.                         (CAUCHY-S)

A remainder of u^15 is not blindly subtracted on a panel touching0: the factor was eliminated algebraically in the function being certified.

## 5. Parameters fixed before executing

ONE branch, domain[0,512],2048panels, half-width h=1/8, centres

    c_j=(2j+1)/8, j=0,...,2047.

Precision1024bits, cap of E109, Taylor degree104. All centres are positive. Cauchy radius r=1 and ratio h/r=1/8. Normalize the entire series E by its positive real value E(c_j), CONSTANT with respect to the formal variable; thus S/E(c_j)^4 is certified. The uncertainty of the normalizing value is kept outward.

Before evaluating centres, the independent review detected another structural loss of the triangular lower bound: S keeps the factor E(u)^4. In the tail, its linear growth over a panel could consume the sign even if S were positive. There was NO run nor observed sign. Hence the ENTIRE per-panel gauge is fixed

    G_c(u)=exp[−4M(c)(u−c)]S(u)/E(c)^4,
    M(c)=E'(c)/E(c).

The EXPONENTIAL FACTOR is positive on the reals; the sign of G_c is not presumed. There is no division by the variable E(u). On the disc of radius1, |M(c)|<3 gives a maximal factor exp12<2^18. By CAUCHY-S,

    |G_c|<2^169,
    REM=2^169*(1/8)^105/(1−1/8)<2^(−145).

The effectiveness of removing that growth has a prior analytic reason:073 gives0<M'(u)<=a<1 for u>=0. For |s|<=h,c+s>=0,

    0<=logE(c+s)−logE(c)−M(c)s<=a s²/2.

Thus the factor E(c+s)^4 exp(−4M(c)s)/E(c)^4 belongs to[1,exp(2ah²)] and is less than exp(1/32). This does not guarantee the sign of the rest of the function; it eliminates a known loss before asking the certificate to decide it. The adjustments Taylor96→104 and cap101→109 pay exactly the gauge bound; they do not change mesh, precision or centres, and were fixed BEFORE evaluating.

For each centre, require G.prec>=105 and coefficients0,...,104 finite. The continuous positivity test is

    G[0]−sum_(k=1)^104 abs(G[k])*h^k−REM>0.

The test verifies the WHOLE closed panel. It does not take samples as a substitute for a continuous lower bound. If an enclosure fails, that is not by itself a negative sign and does not authorize tuning the parameters to force PASS.

## 6. Precise datum a and proposed reproducible evaluation

The wide interval of a098 is not used as the main datum for the divisions by u^15. Before going through the panels, enclose the SAME a again by the exact identity

    a=E''(0)/E(0),

in a single central jet of order2 and1024bits. It is checked that the new interval is contained in the certified interval098

    0.0462099862308379415778676 +/- 3.74e−26.

The new narrow enclosure is kept, without replacing it by the wider old interval. It is not a new free datum; both enclose the same constant and their consistency is verified.

To evaluate E one uses the already audited entire formula080/085 with A=u+1/2,

    E(u)=A[1+(A−1)zeta_deflated(A)]Gamma(A/2)pi^(−A/2).

zeta_deflated(A)=zeta(A)−1/(A−1), NOT(A−1)zeta(A). Official API definition: https://flintlib.org/doc/arb_poly/_arb_poly_zeta_series.html . The evaluations are only jets at exact centres, not zeta parameter balls. The identity with the even theta transform comes from the audited definitions of CONE001/073; the global positive constants do not affect M,a or the sign.

E.prec109 leaves E^(4).prec105; the products PS,PC,Ntilde and the formal division by u^15 keep known coefficients0,...,104 at each non-zero centre. Unknown derivatives are not filled with zeros. The ej are FUNCTIONAL derivatives obtained by derivative(), not Taylor coefficients without their factorials. They are computed from the original series E normalized by the CONSTANT E(c), NOT from a series already modified by the gauge. First PS,PC,Ntilde/u^15 are evaluated; only afterwards is it multiplied by exp[−4M(c)(u−c)]. M(c) is enclosed from the same pointwise jet, without evaluating M on complex discs.

Substituting a narrow ball for a in the operations encloses the selected real value. The Cauchy proof is applied to that exact real value, whose moment relation ensures ENTIRE-S; it is not required that all foreign constants contained in the ball define removable functions.

## 7. Conclusion foreseen by the design and limits

If all panels verify the lower bound, the positive real gauge implies S>0 on[0,512], and by ENTIRE-S T_h>0 is proved on0<u<=512. Splicing with097 discharges T_h>0 for ALLu>0.098 also gives the positive value at0. This is the exact obligation, weaker than the temporal sign of particular densities.

The design did not claim the result before the run;§8 records its decision. Even after a PASS, no Turán inheritance of the next remainder, iteration to all orders or global sign of W is inferred. The applications will be formulated and audited separately; the parameter u is not a new window T. No new implementation until this design is independently approved.


## 8. Main run: global exact obligation discharged

After the independent mathematical and literal approvals, ONE fixed run was executed, owning handle98529. It ended exit0, without changes of parameters, code or representation during execution:

    PASS all predeclared Cauchy, Schwarz and gauge bounds
    PASS precise a, certificate098 containment and entire representation
    PASS exact T_h panels128 of2048
    ...
    PASS exact T_h panels2048 of2048
    PASS ALL099: exact T_h positive throughout[0,512].

The pointwise refinement of a was enclosed with radius less than5.69e−306 and was contained in the complete interval098. No previous moment run was imported or re-executed for the proof099. The continuous decision uses each lower bound of§5, all coefficients up to104 and the EXACT remainder

    REM=1/78052608194857180995375013954269265270931456.

The proved sign is that of the positive entire per-panel gauge, so S>0 on ALL of[0,512]. The identity ENTIRE-S and V>0 on positive reals prove

    T_h(u²)>0 for ALL0<u<=512.

Splicing with the complete analytic tail097 discharges the EXACT obligation

    T_h(x)=2h'(x)h'''(x)−3h''(x)²>0
    for ALL x>0.

098 also gives T_h(0)>0 in its removable extension. This result refers to the SAME real Phi and keeps the complete arithmetic through the entire representation E; it is not a generic inheritance from T_R. Nor does it prove that the particular temporal Wronskian093/095 has a sign on its whole intermediate interval: that condition was stronger and was not used.

SHA256 of the fixed script, unmodified during the run:

    6712eb8542b4d8b7e0836260fba831cd44ccaffb7f1ea321df0a0a32668d51d7.

Reproducible command from the root:

    python3 03-research/phase-211-sign-sandbox/tools/power_exact_h_global_099_verify.py

No new Turán inheritance for the next remainder, iteration to all orders, global sign of W nor a new window T is inferred from this step. Additional applications must be formulated and audited separately. The source keeps the difference between the tilt variable u and the time variable t of095. The audit099 is approved and the independent reproduction run8310 ended exit0/FULL PASS2048 with matching hash and exact remainder.
