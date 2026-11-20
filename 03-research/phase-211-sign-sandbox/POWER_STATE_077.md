# POWER_STATE_077 — Uniform real sign of the regularized Schur remainder

**Update 080:** the admissible compact range of g was certified in `POWER_THETA_G_COMPACT_080.md`, audited in `POWER_THETA_G_COMPACT_AUDIT_080.md` and summarized in `POWER_STATE_080.md`: ALL power triples ai>1 have full positive sign. The later mentions of a pending compact range describe the historical state of this round; h and the higher orders are not discharged by 080.

Status: **PROVED/APPROVED** by analytic proof and complete compact certificate, with code audit. Independent compact reproduction 36038 finished exit0/FULL PASS; matching hash. Papers untouched; global sign OPEN.

## Result

Sources: POWER_THETA_REMAINDER_077.md, POWER_THETA_RATIO_OUTER_077.md and POWER_THETA_RATIO_COMPACT_077.md. Integrated audit: POWER_THETA_REMAINDER_AUDIT_077.md.

Keep Phi, Z, M, Phi_u, H_u from 073/075. For ALL u>0, c=M(u), a=M′(0), beta=u²a/(ua−c), define

    J(x)=integral_|x|∞ yPhi(y)dy,
    F_u(x)=J(x)−betaPhi_u(x).

Then F_u has exactly ONE positive zero, SIMPLE, is negative before it and positive after it. Its total mass is 0. For ALL u,z>0,

    T_u(z)=Z(z)−[Z(0)/H_u(0)+z²/c]H_u(z)>0,
    G_u(z)=c²T_u(z)/(uzH_u(z))>0.

G_u is the exact remainder F1−R_u/z of 075, with R_u=uc²/(ua−c)>0. The statement is uniform in both positive parameters; it is not a finite selection of pivots or nodes.

## New local inequality and proof of the sign

For p=V′, q=V″, r=V‴, V=−logPhi, it was proved on ALL x>0 that

    C=p³+xp²q−pq−xpr+xq²>0,
    N=(xq−p)C′−xrC>0.

Thus L=(xq−p)/C decreases strictly to 0. Integration by parts and the real boundary wPhi->0 express R(x)^−1 as a tail average of L against −(wPhi)′>0, w=1+xq/p. This proves that R=(p+xq)/(x−pJ/Phi) increases strictly to infinity, discharging the hypothesis of the conditional proof.

The forcing of F has two vanishing moments and pattern +−+. Convex interpolation between its two crossings gives F(0)<0 through the Green function with negative sign; the anticausal representation gives a positive tail. Rolle counting with multiplicities limits to four global zeros and forces the single simple positive crossing. Zero mass and the growth of cosh prove T and G positive.

## Reproducible evidence

Exterior x>=1: analytic proof with first-mode margin and the WHOLE theta tail. Fraction verifier power_theta_ratio_outer_077_verify.py, three PASS reproduced independently. It is a certificate for a whole quadrant, not a point mesh.

Compact: origin 0..1/16 via V6<0 and REG on 1024 panels; remainder 1/16..1 with Taylor2 models of C,N on 8192 fixed panels. Run 1589 finished exit0/PASS. Script power_theta_local_077_verify.py fully audited; SHA256

    896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee.

Run 36038 finished its independent reproduction exit0/FULL PASS on the origin and the remaining 8192 panels, with matching hash. The first, insufficient direct interval evaluation failed because of dependency; the Taylor version keeps domains/meshes and adds the needed derivatives and remainders, without changing the hypothesis to force the sign.

## Difference and pending obligation

075 only constructed a positive Phi_u; 076 formulated the defect and left its crossing open. 077 proves a specific differential property of the SAME Phi that controls the remainder, not a generic iteration of 073. The auxiliary 074 does not, of course, satisfy these new local inequalities and does not contradict the result.

G_u(z)>0 on the line does NOT imply that [G_u(z_i)+G_u(z_j)]/(z_i+z_j) is PSD. Positivity of three generators, of all orders, a complete table or a new time window has not yet been obtained. The crossings of the remainder kernel remain the next concrete obligation; global sign OPEN.

## Auxiliary anchored corollary

With N(u)=M(u)/u and B(u)=[a/N(u)−1]/u², one has B>0, B′<0 and 2B+uB′>0. The last inequality comes from N′<0; B′<0 follows from the removable value

    G_u(u)=−aB′(u)/[B(u)(2B(u)+uB′(u))]>0.

Hence F=uB has |uF′/F|<1 and all its kernel pairs are positive definite. The exact Schur complement

    K_M(u,v)−N(u)N(v)/a=[uN(u)vN(v)/a]K_F(u,v)

proves the anchored matrix {0,u,v}, for distinct u,v>0. The node 0 is only the auxiliary extension: it corresponds to a_orig=1/2, outside the admissible power data a_orig>1. There are no three admissible W tests in that corollary. Neither positivity of the kernel G nor of three arbitrary positive nodes is proved.

## Appendix 078 — Two sufficient curvatures and analytic exterior ranges

Case derivation and insight 048, **APPROVED** by independent review in POWER_THETA_CURVATURE_AUDIT_078.md. No other source of reformulations is created. The following exterior estimates are not a new W sign region; the initial compact range remains pending.

Set x=u² and, using primes for derivatives with respect to x only in this appendix,

    b(x)=B(sqrt x), h(x)=1/b(x), g(x)=x b(x).

A sufficient condition for ALL pairs of the remainder kernel G_p, at any positive pivot p, is the double concavity

    h''(x)<=0, g''(x)<=0, ALL x>0.                    (CURVATURE-OPEN)

This is more than the values G_p(z)>0 already proved in 077. Indeed, with P=p², define

    C_P(x)=[b(P)-b(x)]/[x b(x)-P b(P)].

077 proves b decreasing and xb increasing, so C_P>0 and its singularity at x=P is removable. Exact algebra gives

    G_p(z)=[a/B(p)]z C_P(z²),
    C_P'(x)=-b(P)b(x)²
       ·[h(x)-h(P)-(x-P)h'(x)]/[x b(x)-P b(P)]²,
    [xC_P(x)]'=b(P)
       ·[g(x)-g(P)-(x-P)g'(x)]/[x b(x)-P b(P)]².

The tangent-line inequalities of CURVATURE-OPEN would imply C_P'<=0 and (xC_P)'>=0, including the removable values by continuity. Then |zG_p'/G_p|<=1, exactly the mixed condition of CONE001 for all positive pairs of the kernel G_p. To pass from there to a Schur step one also keeps the positive residue R_p/z; its kernel is R_p/(zw), positive of rank one. It is not claimed that the two concavities are automatically preserved under iteration.

### Identification of the already known obligation and of the second curvature

With v=a u/M(u), r=uM'(u)/M(u), t=-u²M''(u)/M(u), the results 073/077 give v>1, 0<r<1, t>0. The exact derivatives are

    g''(x)=v[2r²-r+t-1]/(4u^4),
    h''(x)=v[(r-1)(2r+v-3)-(v-1)t]
                         /[4u²(v-1)^3].

Therefore g''<=0 is PRECISELY the jet obligation already recorded in STATE074,

    t<=(1-r)(1+2r),

and it is not presented as a newly discovered inequality. The second concavity requires

    t>=(1-r)(3-v-2r)/(v-1).

The latter is automatic and strict if v+2r>=3, for example if v>=3. There is no proof here of that comparison on the whole initial compact range.

### First curvature: g''<0 for all u>=63/2

Write A=u+1/2>=32, c=M(u), d=M'(u), e=M''(u) and

    P_j(A)=sum_(n>=2)Lambda(n)(log n)^j n^(-A).

The real absolute series of CONE001 give

    c=1/A+1/(A-1)-logpi/2+psi(A/2)/2-P_0,
    d=-1/A²-1/(A-1)²+psi_1(A/2)/4+P_1,
    e=2/A³+2/(A-1)³+psi_2(A/2)/8-P_2.

Comparing the polygamma series with integrals proves psi_1(y)>=1/y, psi_1(y)<=1/y+1/y² and psi_2(y)>=-1/y²-2/y³. Keeping their cancellations in d+ue gives

    d+ue>=-3/(4A²)+A/(A-1)³+P_1-uP_2
          >1/(4A²)-uP_2.

Lambda(n)(log n)^j<=(log n)^(j+1)<=n^(j+1) allows the complete majorant

    P_j(A)<=2^(j+1-A)[1+2/(A-j-2)], j=0,1,2.

The bounds of P_0, AP_1 and A³P_2 decrease from A=32: the logarithmic derivative of the power A^m times 2^(-A) is at most 3/A-log2<0, and that of the bracket is negative. At 32,

    P_0<=2^(-31)·16/15<1/100,
    AP_1<=32·2^(-30)·31/29<1/100,
    A³P_2<=32³·2^(-29)·15/14=15/229376<1/4.

Thus d+ue>0. The upper bound of psi_1 also gives d<1/(2A)+P_1 and hence ud<51/100. From psi(y)>=log y-1/y,

    c>=log[A/(2pi)]/2+1/(A-1)-P_0
      >log5/2-1/100>3/4.

Here A/(2pi)>=56/11>5 by pi<22/7, and log5>124/81>38/25 by two positive atanh terms with argument 2/3. One obtains

    Delta=c²+ucd+u²ce-2u²d²
          =c²+cu(d+ue)-2(ud)²
          >9/16-2(51/100)²=423/10000>0.

Finally the exact derivative is

    g''(x)=-a Delta/(4u³c³)<0, ALL u>=63/2.

The sign of components is not separated to conclude W: only this concrete auxiliary curvature is proved. No matrix was certified and no new gamma orders were chosen.

### Second curvature: h''<0 for all u>=128

First one obtains the bound of the REAL datum a=M'(0)>1/25, without integrating theta moments. CONE001 fixes M(15/2)=L(8). The audited bounds gamma<3/5, logpi<23/20 and psi(4)=11/6-gamma give

    L(8)>13/42-P_0(8).

Explicit source of those constants: POWER_FOUR_GLOBAL_009§4 and its rational verification. Gamma<H32-log32<3/5 uses log2>693/1000, obtained from three positive atanh terms with argument 1/3. The bound logpi<23/20 uses pi<22/7 and the positive sum sum_(k=0)^6(23/20)^k/k!>22/7. These are already audited rational inequalities, not new parameter evaluations.

For n>=1, log n<=sqrt n: the maximum of (log x)/sqrt x is 2/exp1<1. Thus Lambda(n)<=sqrt n and the sum-integral comparison, keeping all terms, proves

    P_0(8)<=sum_(n>=2)n^(-15/2)
       <=2^(-15/2)(1+4/13)<85/11648<1/105.

1/sqrt2<5/7 was used. Therefore L(8)>3/10. The strict concavity of 073 and M(0)=0 imply

    a>M(15/2)/(15/2)>1/25.

For u>=128, the real formula for M, psi(y)<=log y, P_0>=0 and pi>3 give

    M(u)<log(u/5)/2+2/(u-1/2).

Indeed (u+1/2)/(2pi)<u/5 for u>5/2. At u=128,

    (3/2)log(128/5)+6/(128-1/2)
       <99/20+4/85<128/25,

because 128/5<27 and log3<11/10. The difference

    u/25-(3/2)log(u/5)-6/(u-1/2)

is strictly increasing for u>=128: its derivative is greater than 1/25-3/256>0. Hence 3M(u)<u/25<a u for ALL u>=128, that is v>3. The exact formula for h'' then proves

    h''(x)<0, ALL u>=128.

This range improves the more conservative preliminary bound u>=1024, which is not presented as another construction. All thresholds come from explicit analytic inequalities, without mesh or additional certificate.

### Initial compact range and scope

What remains is g'' on 0<u<63/2 and h'' on 0<u<128. Before any certificate the origin would have to be regularized: b(0)=-kappa4/(6a), b'(0)=kappa4²/(36a²)-kappa6/(120a), while h''(0) also depends on kappa8. Individual positivity of cumulants or the concavity of M does not supply those mixed comparisons.

An exact coordinate for seeking a new proof uses J from 076 and

    K(x)=int_|x|^infinity (y-|x|)[aPhi(y)-J(y)]dy>0.

Positivity follows from the single negative/positive crossing and zero mass of aPhi-J: the tail integral of that weight is positive for all x>0, so K'<0 and K(infinity)=0. If Z_J,Z_K are their bilateral transforms, then Z_J=Z'/u and u²Z_K=aZ-Z_J, so that b(u²)=Z_K(u)/Z_J(u). The required concavities are comparisons between TWO distinct tilted laws; 073 does not prove them separately for each law. No new bound for those compact comparisons, closure of the kernel G or new coverage of W is declared here.
