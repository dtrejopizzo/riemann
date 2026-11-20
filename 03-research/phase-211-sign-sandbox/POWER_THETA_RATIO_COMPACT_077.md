# POWER_THETA_RATIO_COMPACT_077 — Two local signs on the remaining interval

Status: **PROVED/APPROVED**, run 1589 exit0/PASS and mathematical/code audit in POWER_THETA_REMAINDER_AUDIT_077.md. Independent reproduction 36038 finished exit0/FULL PASS; script hash matching. The sign of the quotient additionally uses the separate proof of the assembly. Papers and phase 103 untouched.

## 1. Specific residue and signs that are checked

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread 073–076 and the limits of the generic class 074. The object is the SAME real Phi, V=−logPhi. For x>0 set

    p=V', q=V'', r=V''', s=V'''',
    C=p³+xp²q−pq−xpr+xq²,
    N=(xq−p)C'−xrC,
    C'=4p²q+2xpq²+xp²r−2pr+xqr−xps.

The obligations of this source are

    C(x)>0, N(x)>0 for ALL 0<x<=1.                  (COMPACT)

Thus L=(xq−p)/C>0 and L'=−N/C²<0 on that interval. The numerator xq−p is positive by V'''>0 of 073. The separate source POWER_THETA_RATIO_OUTER_077.md treats x>=1 analytically.

The difference relative to 075/076 is to check TWO specific local inequalities of Phi, not to assume the monotonicity of an integral quotient nor to present the ODE again as a proof. A generic class condition that sufficed for two generators does not control these combinations, as 074 already showed.

## 2. Analytic desingularization at the origin

At 0, p and r vanish and the numerators have high-order cancellations. For x>0 define

    P=p/x, Q=q, R=r/x,
    D=(Q−P)/x²,
    E=C/x³=QD+P³+P²Q−PR,
    U=D'/x, T=R'/x.

These functions admit smooth even extensions to 0. One has the identities

    P'=xD, Q'=xR,
    D=∫_0^1 t²R(tx)dt,
    (E²/x)L'=P{U(P²+PQ−R)−D[3PD+2DQ+PR−T]}.        (REG)

They are algebraic identities, reviewed independently. Let a=V''(0)>0 and b=V''''(0)>0. If on 0<=x<=1/16 one certifies

    V^(6)(x)<0, b<2a²,                              (ORIGIN-DATA)

then parity implies V^(5)(0)=0 and hence V^(5)(x)<0 for x>0. Then V'''' decreases and R=∫_0^1V''''(tx)dt also decreases, giving T<0. The integral formula for D gives U<0. 073 and log-concavity 10334 give P,Q>=a>0 and R,D>0. Moreover R<=b<2a²<=P²+PQ. Therefore E=QD+P(P²+PQ−R)>0 and REG is strictly negative. This proves COMPACT on 0<x<=1/16 from data with NONZERO margin, without dividing intervals by x³ or x⁷.

## 3. Rational models of the theta sum and its complete tail

Write, as in 073,

    Phi(x)=pi exp(5x/2) S(x),
    S=Σ_(m>=1)m²(2y−3)exp(−y), y=pi m²exp(2x).

With Q0(y)=2y−3 and Q_(j+1)=2y(Q_j'−Q_j), one has S^(j)=Σm²Q_j(y)exp(−y). The verifier generates Q0,...,Q8 with exact integer coefficients. Let A=max_(j<=8)Σ|coef Q_j|. Each degree is <=9 and, for y>=1, |Q_j(y)|<=A y⁹.

Modes m=1,...,6 are retained. For ALL 0<=x<=1 and m>=7, y>=3m²>=147>9. The function y⁹exp(−y) decreases there, and exp(3)>16 by a rational Taylor sum. Thus

    m²|Q_j(y)|exp(−y)<=A·3⁹m²⁰2^(−4m²).

The consecutive ratio is <=(8/7)²⁰2^(−60)<1/2. Therefore the COMPLETE tail of each S^(j), j<=8, is enclosed in [−epsilon,epsilon], with

    epsilon=2A·3⁹·7²⁰·2^(−196).                     (TAIL)

Six modes and this tail were chosen BEFORE running so that division by S near x=1 would not amplify an overly coarse uniform bound. The tail is not modified according to the result.

The logarithmic derivatives are reconstructed by the exact recurrence

    ell_j=[S^(j)−Σ_(k=1)^(j−1)binom(j−1,k−1)ell_k S^(j−k)]/S,
    ell_j=(logS)^(j).

Then p=−ell_1−5/2 and V^(j)=−ell_j for j>=2. At each evaluation S.lower>0 is certified before dividing.

## 4. Elementary enclosures and the TWO fixed meshes

The script tools/power_theta_local_077_verify.py uses outward intervals with integer endpoints over 10^70. Pi is enclosed with Machin and 128 alternating terms per arctangent, with explicit remainder, as in 073.

For exp(z), 0<=z<=2048, Taylor up to degree 128 is evaluated at z/2048<=1 with remainder [0,2/129!]; eleven outward squarings recover exp(z). The range includes all arguments of the six modes on [0,1]. No floating-point value is used as proof datum.

The first mesh consists of 1024 uniform intervals of [0,1/16]. If m is the centre of a panel of radius h, V^(6) is enclosed by

    V6(m)+[-h,h]V7(m)+[0,h²/2]V8(panel).              (TAYLOR-V6)

The strictly negative upper sign on all panels, together with the rational asserts a,b>0 and 2a²>b at 0, certifies ORIGIN-DATA.

The second mesh consists of 8192 uniform intervals of [1/16,1]. On each panel C, N and their first derivatives are evaluated at the point CENTRE; cancellations are not ignored by treating the final value as a sum of absolute terms. The simplified identities are

    N'=(xq−p)C''−(r+xV4)C,
    N''=xrC''+(xq−p)C'''−(2V4+xV5)C−(r+xV4)C'.

C, C', C'', C''' are computed by jets of derivatives up to order 3, with the binomial product rule; they only require V up to order 6. On the whole panel one encloses

    Cwhole=C(m)+[-h,h]C'(m)+[0,h²/2]C''(panel),
    Nwhole=N(m)+[-h,h]N'(m)+[0,h²/2]N''(panel).        (TAYLOR-CN)

The asserts are Cwhole.lower>0 and Nwhole.lower>0. The meshes and the strict signs are fixed, not chosen by a parameter sweep.

## 5. History of the enclosure and reproducibility

The first implementation tried to enclose V6 by direct evaluation of the log-jet on the first panel. It produced an interval with positive upper endpoint, although the pointwise diagnostic was negative. That FAIL was lack of dependency, not a counterexample to ORIGIN-DATA; it was not promoted as a sign change. Exactly 1024/8192 panels, domains and margins are kept, but the direct enclosure is replaced by the second-order Taylor models above, with their justified additional derivatives and tails. An editing error accidentally relaunched that same old assert and repeated the immediate FAIL before the file was corrected; it was not another selection of parameters.

The run of the corrected certificate is

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_local_077_verify.py

The corrected run 1589 finished exit0 and produced PASS for ORIGIN-DATA and for C>0, N>0 on the remaining 8192 panels. This proves COMPACT completely, without samples or floats. The printed rational tail was

    epsilon=42965568563849534658039831/98079714615416886934934209737619787751599303819750539264.

The SHA256 of the exact reproducible verifier is

    896902cf8ac1f504eb1357b6edc3048a9316094afd9b8ac5597aaff4a81a70ee.

The script was not modified during its run; the hash fixes the version that finished PASS.

## 6. Scope and connection

COMPACT and OUTER, both audited, provide C>0, L'<0, L(infinity)=0 for the REAL Phi. The separate proof POWER_THETA_REMAINDER_077 and its audit integrate the quotient of tails and conclude G_u(z)>0 for u,z>0; this local certificate does not obtain it by itself. Neither a positive second-order Schur kernel, three generators, all orders nor a new time window is inferred. No auxiliary constant is optimized nor are matrices of growing dimensions evaluated.
