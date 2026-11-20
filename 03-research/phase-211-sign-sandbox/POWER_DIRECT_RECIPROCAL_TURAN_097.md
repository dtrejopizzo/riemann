# POWER_DIRECT_RECIPROCAL_TURAN_097 — Direct T_h and real tail from512

**Update099:** the REAL obligation T_h>0 globally was closed in `POWER_EXACT_H_GLOBAL_DESIGN_099.md`, audited in `POWER_EXACT_H_GLOBAL_AUDIT_099.md` and summarized in `POWER_STATE_099.md`. Both curvatures and all triples of the remainder G_p are proved; the auxiliary block of five nodes is anchored at0 and they are NOT five admissible W generators. The mentions of compact set/pending hypothesis below keep the historical status of this round; inheritance to the next level remains open.

Status: **PROVED the formula, the regularization and T_h>0 for ALL u>=512; independent audits approved.** See `POWER_DIRECT_RECIPROCAL_TURAN_AUDIT_097.md`. The compact set0<u<512 remains OPEN. The pointwise sign of the particular densities K is not required. No preservation of Turán, sign of all orders nor new W coverage is claimed. Papers untouched; no new numerical certificates.

## 1. Consultation and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked078,083–085,089–090,092–093 and095.090 identifies T_h>0 as an exact obligation for the curvatures R_G at all pivots and refutes its generic inheritance from T_R>0. The sign of the Wronskian of particular densities investigated093/095 is a STRONGER sufficient condition, still without global proof.

Here one works directly with the SAME h on real data M,Z. Its algebraic cancellation is kept and a new tail inequality is obtained via the complete series already audited084. No other dimension is re-certified, nor is the anchored five-column identity promoted as a sign gain.

## 2. Explicit formula in M and three derivatives

Put x=u², a=M'(0)>0 and

    c=M(u), d=M'(u), e=M''(u), f=M'''(u),
    D=ud, E=u²e, F=u³f,
    h(x)=u²M(u)/[au−M(u)].

The derivatives of h are with respect to x; d,e,f are with respect to u.073 gives au−c>0 for u>0. Define the polynomial N_S already used084 and a new polynomial C_h:

    N_S=3c²+c(6D+6E+2F)−9D²−6DE+2DF−3E²,
    C_h=3c³+c²(3D+6E+F)+c(−12D²−6DE)+6D³.

Then exactly

    T_h=2h'h'''−3h''²
        =a[au N_S−4C_h]/[16u³(au−c)^4].           (DIRECT)

These are explicit coefficients: N_S and C_h only contain a,u,M,M',M'',M'''. No asymptotic remainder needs to be derived. A check by differentiation uses

    h'=[acu+adu²−2c²]/[2(au−c)²],
    h''=a[−acu+adu²+aeu³+3c²−5cdu−ceu²+2d²u²]
                                      /[4u(au−c)³].

Differentiating h'' by(2u)^(-1)d/du and combining2h'h'''−3h''² gives DIRECT. The numerator is not replaced by independent absolute errors before carrying out that cancellation.

As a structural check, S(x)=uM(u) satisfies T_S=N_S/(16u^6), and

    T_h={a²u⁴T_S+2ac⁴(d/dx)^3[u³/M(u)]}/(au−c)^4.

The second summand may be negative; that is why T_S>0 alone does not resolve the sign. The following proof pays its cost via C_h.

## 3. Complete arithmetic input and audited exterior box

Write A=u+1/2.084 proves via complete real series

    c=1/A+1/(A−1)−logpi/2+psi(A/2)/2−P_0,
    d=−1/A²−1/(A−1)²+psi_1(A/2)/4+P_1,
    e=2/A³+2/(A−1)³+psi_2(A/2)/8−P_2,
    f=−6/A⁴−6/(A−1)⁴+psi_3(A/2)/16+P_3,
    P_j(A)=sum_(n>=2)Lambda(n)(log n)^j n^(−A).

All these sums are absolute in the region used. No primes are truncated. The complete remainders are paid via

    P_j(A)<=2^(j+1−A)[1+2/(A−j−2)], j=0,1,2,3,

and integral comparisons of the polygamma series, detailed084. Its audited consequence for A>=128 is

    c>3/2,
    9/20<D<51/100,
    −51/100<E<−2/5,
    4/5<F<101/100,
    N_S>3c²−2>2c².                                (INPUT-084)

The last comparison uses c²>9/4>2. A c-dependent bound from084 is reused, not only the constant margin N_S>19/4.

The same box allows a joint upper bound on C_h. Indeed,

    3D+6E+F<3(51/100)+6(−2/5)+101/100=7/50,
    −12D²−6DE<−12(9/20)²+6(51/100)²
                  =−4347/5000<0,
    6D³<6(51/100)³<4/5.

Hence

    C_h<3c³+(7/50)c²+4/5<4c³, c>3/2.             (COST)

The last inequality is elementary: c³−(7/50)c²−4/5 is increasing for c>=3/2 and at3/2 equals113/50>0. If C_h were negative, the cost would be even smaller; its sign is not presumed.

INPUT-084 and COST give

    au N_S−4C_h>2c²(au−8c).

Thus it suffices to prove au>8M(u) in the tail.

## 4. Scalar comparison that pays ALL u>=512

078 proves the REAL datum a>1/25, using the anchor L(8)>3/10 and073. Also, for u>=128,

    M(u)<log(u/5)/2+2/(u−1/2).                    (UPPER-M)

At u=512, 512/5<128 and log2<7/10 imply

    M(512)<(7/2)log2+2/(512−1/2)
           <49/20+1/100=123/50.

The bound log2<7/10 is proved, for example, with the positive sum of the series of exp(7/10) up to degree4, which is greater than2. Thus

    8M(512)<492/25<512/25<a·512.

To extend the comparison without a mesh, consider

    H(u)=u/25−4log(u/5)−16/(u−1/2).

The previous computation gives H(512)>0, and for ALL u>=512,

    H'(u)=1/25−4/u+16/(u−1/2)²
           >1/25−4/512>0.

UPPER-M then implies au>u/25>8M(u) for all those u. DIRECT is strictly positive:

    T_h>a c²(au−8c)/[8u³(au−c)^4]>0,
    ALL u>=512.                                (DIRECT-TAIL)

The threshold was fixed by these loose analytic inequalities. No favourable endpoint was searched for and T_h was not evaluated numerically. The domain is that of the tilt parameter u; it is not the time domain t of095.

## 5. Exact regularization of the origin

The parity of Z and its positivity near the origin make N(x)=M(u)/u analytic in x=u². Write

    N(x)=a+b_1x+b_2x²+b_3x³+b_4x^4+O(x^5),
    b_1=kappa4/6, b_2=kappa6/120,
    b_3=kappa8/5040, b_4=kappa10/362880,

where kappa_(2j) are the cumulants of the real law Phi without tilt. Their sign is not claimed separately.086 gives R'(0)>0, so b_1<0, since R=1/N. The regular expression is

    h(x)=N(x)/B_0(x),
    B_0(x)=[a−N(x)]/x,
    B_0(0)=−b_1>0.

Hence h and its derivatives are analytic in a neighbourhood of0; the apparently singular denominator of DIRECT does not imply a real singularity. The small numerator and denominator are not used separately to decide a sign.

The explicit values are

    h(0)=−a/b_1,
    h'(0)=a b_2/b_1²−1,
    h''(0)=2a(b_1b_3−b_2²)/b_1³,
    h'''(0)=6a(b_1²b_4−2b_1b_2b_3+b_2³)/b_1^4.

Combining these derivatives cancels terms and gives

    T_h(0)=(12a/b_1^4)
       ·det[[a,b_1,b_2],[b_1,b_2,b_3],[b_2,b_3,b_4]]. (ORIGIN-HANKEL)

Thus the origin datum is a Hankel3 of the NORMALIZED cumulant coefficients. Its sign is not inferred from positivity of a different measure nor from the individual positivity of some cumulants. In this source no new moments are computed and the sign of ORIGIN-HANKEL is not certified.

## 6. Remaining obligation and scope

DIRECT-TAIL discharges the EXACT obligation T_h on a tail of u. On0<u<512 a joint bound for auN_S−4C_h is still missing, or an equivalent comparison that keeps its cancellation. To decide the origin itself one can use ORIGIN-HANKEL with a previously designed moment enclosure; that computation was not started here.

The datum is weaker than requiring a signed temporal Wronskian at each point: it does not need that sufficient hypothesis nor derive its real remainders. Global T_h, R_G'' for all pivots, all triples of the kernel G_p, five original generators or all orders have not been proved. The new tail does not by itself modify the W coverage already proved085. The inheritance counterexample090 remains valid and does not refute this REAL inequality. Global objective OPEN.
