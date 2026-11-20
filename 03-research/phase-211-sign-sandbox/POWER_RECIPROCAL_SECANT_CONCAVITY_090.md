# POWER_RECIPROCAL_SECANT_CONCAVITY_090 — Concavity of a reciprocal secant

**Update099:** the REAL global obligation T_h>0 was closed in `POWER_EXACT_H_GLOBAL_DESIGN_099.md`, audited in `POWER_EXACT_H_GLOBAL_AUDIT_099.md` and summarized in `POWER_STATE_099.md`. Both curvatures and all triples of the remainder G_p are proved; the auxiliary five-node block is anchored at0 and they are NOT five admissible W generators. The mentions of a pending compact/hypothesis below keep the historical status of this round; inheritance to the next level remains open.

Status: **PROVED the elementary lemma and its theta application via the global datum T_R>0 proved in089, with derivation and independent reproduction FULL PASS.** Independent audit passed; see `POWER_RECIPROCAL_SECANT_CONCAVITY_AUDIT_090.md`. No claim is made that the remainders inherit new Turán inequalities, nor of a global sign of W. Papers untouched.

## 1. Consultation and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked078,081–089.078 left open a second concavity to control the pairs of the remainder G_p;079/082 avoided needing it for three original generators.084 introduced T_f=2f'f'''−3f''² for four nodes.081 prevents naively inheriting monotonicity and concavity of the original function in all the remainders.

The new step relative to the corpus is an integral inequality: T_f>0 implies strict concavity of the reciprocal of the secant from0. It is proved under hypotheses that do not require f to be increasing and concave at once: f'>0 and T_f>0 suffice. This connects the global T_R datum sought in089 with the h obligation of078. No worldwide priority of the lemma is claimed and the missing theta hypothesis is not presumed.

## 2. Lemma and removable endpoint

Let 0<L<=infinity and f∈C³([0,L)), with f'(x)>0 on ALL of [0,L). Suppose

    T_f(x)=2f'(x)f'''(x)−3f''(x)²>0, 0<x<L.

Define, for x>0,

    g(x)=f(x)−f(0)>0,
    h_0(x)=x/g(x).

Then h_0 extends as a C² function to the endpoint0, with

    h_0(0)=1/f'(0),
    h_0''(x)<0, ALL0<x<L.                         (SECANT-CONCAVITY)

Neither f>0 nor f''<0 is required. At0 only h_0''(0)<=0 follows; the strict inequality there needs T_f(0)>0.

The C² extension follows from

    g(x)/x=int_0^1 f'(sx)ds,

whose right-hand side is C² and positive up to0. Moreover

    h_0''(0)=[3f''(0)²−2f'(0)f'''(0)]/[6f'(0)³]
             =−T_f(0)/[6f'(0)³]<=0.

## 3. Proof by integrating the tangent

Set w=(f')^(-1/2)>0. Differentiating twice gives

    w''=[3f''²−2f'f''']/(4f'^(5/2))
        =−T_f/(4f'^(5/2))<0, 0<x<L.

Thus w is strictly concave on each interval [0,x], and w(0)>0. Fix x>0 and its tangent

    ell_x(s)=w(x)+w'(x)(s−x), 0<=s<=x.

Strict concavity implies w(s)<ell_x(s) for0<=s<x. In particular

    d_x=w(x)−xw'(x)>=w(0)>0.

Since ell_x is linear and its two endpoint values are positive, there is no hidden pole when integrating its reciprocal square. One obtains the strict inequality

    g(x)=int_0^x ds/w(s)²
         >int_0^x ds/ell_x(s)²
         =x/[w(x)(w(x)−xw'(x))].                   (TANGENT-INTEGRAL)

The integral equality also holds if w'(x)=0, by direct computation or continuity; one does not divide by w' without treating that boundary. Nor is a sign of w' used.

Write d=f'=1/w² and e=f''=−2w'/w³. The exact computation of the second quotient is

    h_0''=[2xd²−2gd−xge]/g³
          =2[x−g w(w−xw')]/(w⁴g³).

TANGENT-INTEGRAL proves that the numerator is strictly negative, while the denominator is positive. This proves SECANT-CONCAVITY. The sign gain comes from the integrated tangent inequality, not from an identity of the quotient by itself.

## 4. Theta application, global input proved in089

Use the real coordinates073/077/078/086:

    a=M'(0)>0,
    R(x)=u/M(u), x=u²,
    b(x)=[au/M(u)−1]/u²=a[R(x)−R(0)]/x,
    h(x)=1/b(x).

The analytic parity of Z and M(u)/u→a show that R is analytic at0 and R(0)=1/a.073 gives R'>0 for x>0, and086 proves R''<0 for ALL x>0. Hence R' decreases strictly, and its finite limit at0 satisfies R'(0)>R'(x)>0. This verifies the nondegenerate endpoint required by the lemma, without assuming an unproved sign for a cumulant at0.

089, its four-density transport and the independent reproduction 87911 FULL PASS prove

    T_R=2R'R'''−3R''²>0, ALL x>0.                 (THETA-INPUT-PROVED)

Hence SECANT-CONCAVITY applies to f=R and gives

    h(x)=[x/(R(x)−R(0))]/a,
    h''(x)<0, ALL x>0.                            (THETA-PROVED)

The global datum comes from the transport proved in089, not from extending085 beyond its domain:085 by itself, from a positive endpoint, did not replace the hypothesis on all of0..x. The proof089 includes both compact enclosures and the tail088 with independent reproduction FULL PASS.

## 5. Proved consequence for the pairs of G_p

The other datum of078 is already discharged in086: g_*(x)=xb(x)=aR(x)−1 satisfies g_*''<0. By THETA-INPUT-PROVED and§4, h''<0 globally. Hence, for each P=p², set

    C_P(x)=[b(P)−b(x)]/[xb(x)−Pb(P)].

The formulas of078 are

    C_P'(x)=−b(P)b(x)²
        ·[h(x)−h(P)−(x−P)h'(x)]/[xb(x)−Pb(P)]²,
    [xC_P(x)]'=b(P)
        ·[g_*(x)−g_*(P)−(x−P)g_*'(x)]/[xb(x)−Pb(P)]².

The strict concavities give C_P'<0 and(xC_P)'>0 for x≠P. At x=P their limits are also strict: the numerators of the tangent errors are respectively −h''(P)(x−P)²/2 and−g_*''(P)(x−P)²/2, while the denominator has leading term g_*'(P)²(x−P)² and g_*'(P)>0. The singularities are removable, as in077.

Since G_p(z)=[a/B(p)]zC_P(z²)>0,

    −1<zG_p'(z)/G_p(z)<1, ALL p,z>0.

The pair criterion CONE001 then proves all pairs of the kernel G_p positive definite for distinct nodes. G_p'>0 is not required; hence the result is compatible with the obstruction081.

This application is now proved by089. It does not claim T_(R_G)>0, nor concavity of both reciprocal data of G_p, nor preservation of the hypotheses when iterating Schur. One obtains a possible concrete step on the crossings of the remainder, not a closure of all orders or of the global target.

## 6. Extension to an interior anchor: proof with both orientations

Let f∈C³(I), I an interval, f'>0 and T_f>0 on I. For P∈I define

    H_P(x)=(x−P)/[f(x)−f(P)], x≠P,
    H_P(P)=1/f'(P).

Then H_P is C² and H_P''<0 on ALL of I, including x=P. It is not required that P be an endpoint of the interval nor that f be concave.

The C² extension follows from [f(x)−f(P)]/(x−P)=int_0^1 f'(P+s(x−P))ds>0. Set y=x−P, G=f(x)−f(P), w=(f')^(-1/2), and fix the tangent ell_x(s)=w(x)+w'(x)(s−x). Since w''<0, this tangent is strictly greater than w(s) for s≠x on the segment with endpoints P,x. In particular d=w(x)−yw'(x)=ell_x(P)>w(P)>0, and the tangent is positive on that whole segment.

If x>P, integrating in the positive orientation gives

    G=int_P^x ds/w(s)²
      >int_P^x ds/ell_x(s)²=y/[w(x)d].

If x<P, both integrals are oriented the other way and give

    G=−int_x^P ds/w(s)²
      <−int_x^P ds/ell_x(s)²=y/[w(x)d].

The evaluation of the linear integral also holds if w'(x)=0. The derivative formula is

    H_P''(x)=2[y−G w(x)d]/[w(x)^4 G³].

For x>P the numerator is negative and G³>0. For x<P the numerator is positive and G³<0. In both cases H_P''<0. At the removable point,

    H_P''(P)=−T_f(P)/[6f'(P)³]<0.

Thus both orientations and the anchor itself are checked explicitly.

## 7. One curvature of the remainder is discharged with the same datum T_R

Keep x=z², P=p², b_P=b(P), g(x)=xb(x)=aR(x)−1 and h(x)=1/b(x). In this section R_G,S_G are the reciprocal data of the REMAINDER, not those of M:

    R_G(x)=z/G_p(z), S_G(x)=zG_p(z).

The exact expression077 of G_p gives

    R_G(x)=(1/a){(x−P)/[h(x)−h(P)]−P b_P},
    S_G(x)=a{(x−P)/[g(x)−g(P)]−h(P)}.             (REST-SECANTS)

To verify the first, use h−h(P)=(b_P−b)/(bb_P); for the second, use g(P)=Pb_P. They are algebraic equalities that extend to x=P by their removable values.

By THETA-INPUT-PROVED of089, g'>0 and T_g=a²T_R>0 on the whole half-line. The interior-anchor lemma applies to f=g and proves

    S_G''(x)<0, ALL p>0,x>0.                     (ONE-REST-CURVATURE)

Hence this curvature requires no new hypothesis beyond the global T_R datum: it uses the same datum for ALL pivots. It is an effective shape inequality, not simply the REST-SECANTS identity. The input089 already has a mathematical/code audit and independent reproduction 87911 exit0/FULL PASS, so ONE-REST-CURVATURE is PROVED for the real Phi.

By contrast R_G''<0 would be proved by the same lemma IF T_h>0 were proved globally, since h'>0 is already known from077. It is not claimed that T_h is inherited. In fact, the removable formula of§6 shows that R_G''(P)<0 for ALL pivots would necessarily require T_h(P)>0. Thus the family of these curvatures has as exact additional obligation T_h>0, not the monotonicity of G_p refuted in081.

If that additional datum were proved,082 applied to G_p, whose pairs are PD by§5 under the input089, would give all its triples positive definite. This still does not prove that the same conditions are preserved to the next remainder.

## 8. The T_h obligation is a next anchored minor, not automatic inheritance

Additional consultation:083 identifies the bordered Pfaffian of size five with the interpolation determinant of the columns

    (1,x,x²,R,xR).

Its specialization with one node at0 clarifies exactly which new datum is requested. Write R0=R(0), G=R−R0>0 and H=x/G=ah. Subtract R0 times the first column from the fourth and R0 times the second from the fifth. Expanding along the row corresponding to0, the four-node determinant of (x,x²,G,xG) remains.

Dividing each remaining row by its G_i>0 gives (H,xH,1,x). Moving the two blocks of two columns to (1,x,H,xH) uses four transpositions and has positive sign. Consequently, for four distinct positive nodes,

    det[1,x,x²,R,xR]_(nodes 0,x1,x2,x3,x4)
        =(product_(i=1)^4G(xi))
             ·det[1,x,H,xH]_(nodes x1,x2,x3,x4).    (ANCHORED-FIVE)

The version with the four positive nodes confluent is exactly

    W(x,x²,G,xG)=G⁴ W(1,x,H,xH)
                 =−G⁴T_H=−a²G⁴T_h.              (ANCHORED-JET)

The same column orientation as in084 is used. The node0 here is an algebraic auxiliary and is not turned into an admissible exponent for W.

Thus T_h>0 is the local condition of the next five-column determinant, with one node anchored at0 and the other four confluent. The sign of the four-column T_R does not supply it. The identity shows the real additional obligation without declaring it resolved, nor claiming positivity for all arbitrary five nodes or preservation of all orders.

## 9. NO-GO for generic inheritance: explicit global counterexample

Status of this section: **PROVED, independent audits passed.** Automatically preserving T_f>0 under H=x/(f−f0) is refuted, even for f positive, increasing and strictly concave on the WHOLE half-line. The difference from084 is that the initial datum here DOES have T_f>0 globally. No theta datum is modified and T_h of the real Phi is not refuted.

Define for ALL x>=0

    w(x)=(5−exp(−x))/4,
    f(x)=1+(16/25){log[(5exp(x)−1)/4]
                          −1/[5exp(x)−1]+1/4}.

Then f(0)=1 and

    f'(x)=1/w(x)²>0,
    f''(x)=−2w'(x)/w(x)³<0,
    T_f(x)=−4w''(x)/w(x)^5=exp(−x)/w(x)^5>0.

Here w>0,w'=exp(−x)/4>0,w''=−exp(−x)/4<0 globally. f is positive because it starts at1 and increases. The explicit formula for f is verified by differentiating, without quadrature or gluing.

However H(x)=x/[f(x)−f(0)] does NOT preserve T_H>0. The regular extension at0 has exact series

    f(x)−f(0)=x−x²/4+7x³/48−x⁴/12+O(x^5),
    H(x)=1+x/4−x²/12+5x³/192+O(x^4).

Hence

    H'(0)=1/4, H''(0)=−1/6, H'''(0)=5/32,
    T_H(0)=2H'(0)H'''(0)−3H''(0)²
           =5/64−1/12=−1/192<0.

The functions are analytic in a neighbourhood of0. By continuity, T_H<0 on some positive interval: it is not just a failure at an excluded endpoint. No attempt is made to quantify that interval, because the sign already decides the universal inheritance claim.

A general jet check locates the additional datum. If w(0)=1, b=w'(0), c=−w''(0), d=w'''(0), then

    H'(0)=b, H''(0)=−2c/3, H'''(0)=(bc+d)/2,
    T_H(0)=b²c+bd−4c²/3.

The example fixes b=c=d=1/4. Parameters were not varied in a numerical campaign. Although H''<0 is guaranteed by the lemma of this source, its new Turán inequality fails.

Scope: only that generic inheritance is refuted. The REAL curvature S_G''<0 of§7 remains proved. T_h of the real Phi remains OPEN and would require specific information, for example the anchored five-column minor of§8. W, the coverages085, other invariants and the general Schur recursion are not refuted. No positivity is claimed for all triples of G_p, of five original generators or of all orders.
