# Construction 083 — Moment transport between the sign zones

Status: identities, polynomial profile, coverage and cross-indefiniteness test checked independently. There is no proof of the sign of the form. The extraction of a square that only annihilates approximate profiles is abandoned.

## Profile and two balanced measures

Choose a real profile g∈C_c∞(I)∩P_T, nonzero, by means of an even smooth cutoff and an even smooth central corrector normalized in cosh(t/2), as in the final modification of BUILD080 (not by Q applied to the hard cutoff). It is not assumed that g is an eigenvector nor that A g=0. Write g=g+−g−, with both parts non-negative and disjoint supports.

For σ=±1 set

    mσ=∫e^(σt/2)g+(t)dt=∫e^(σt/2)g−(t)dt>0,
    dμσ,±(t)=e^(σt/2)g±(t)dt/mσ.

They are probabilities. For F=g h with h smooth bounded and F∈P_T,

    ∫h dμσ,+=∫h dμσ,−=:cσ(h).                           (1)

The whole domain is not yet considered: this carrier of products may fail to be dense if g vanishes on an interval. This coverage problem is not omitted.

## Exact transport identity for a difference

If x is in {g>0}, y in {g<0}, define

    Aσ(x;h)=∫[h(x)−h(z)]dμσ,+(z),
    Bσ(y;h)=∫[h(w)−h(y)]dμσ,−(w).

By (1), h(x)−h(y)=Aσ(x;h)+Bσ(y;h). Hence

    |h(x)−h(y)|²=|Aσ|²+|Bσ|²+2Re(Aσ conjugado(Bσ)).       (2)

The interaction between signs is expressed in differences internal to each zone, but the mixed term is kept and has no sign. Jensen is not applied and that term is not discarded.

Both identities can be combined: for any real θ(x,y),

    h(x)−h(y)=θ(A++B+)+(1−θ)(A−+B−).                    (3)

This is a concrete design freedom based on BOTH constraints. Choosing θ does not by itself produce positivity; its possible role would be to cancel cross terms with the full archimedean and arithmetic interaction.

## Energy form without assuming a ground state

For smooth profiles and tests, the product identity for the form a_T gives

    a_T(g h)=∫g(t)(H_T g)(t)|h(t)|²dt
       +(1/4)∬ K(|t−s|)g(t)g(s)|h(t)−h(s)|²dt ds
       +Σ_n [Λ(n)/sqrt(n)]∫g(t)g(t−log n)|h(t)−h(t−log n)|²dt. (4)

Functions are extended by zero. H_T g denotes the operator of the full form on L²(I), WITHOUT primitive compression; it does not vanish and is not assumed to have a sign. The contact coefficient is v_n/2=Λ(n)/sqrt(n). The identity is justified first with cutoffs of the continuous singularity and then by convergence of the smooth differences.

In (4), the interactions internal to each sign are positive and those crossing signs are negative. The proposal is to insert (3) into ALL the negative interactions, keeping the same functions θ and both averaging terms, and to compare the resulting coefficients with the internal interactions. The potential g H_T g remains in the computation: omitting it would amount to assuming a ground state that does not exist in the window.

## First result and remaining obligation

Equations (1)-(3) give an exact transport, not a bound. The sign requires constructing θ and a joint identity where the potential and the mixed terms are controlled. θ with that property has not yet been chosen.

Moment transport works for any weight and does not separate falsifiers. Any selection of θ based only on g and the moments, without using H_Tg and the exact contacts in the same cancellation, would not explain the arithmetic sign. The design must also solve the coverage of the carrier, not only a subclass of products.


## Simplification of the mixing parameter

The check verifies Aσ(x;h)=h(x)−cσ(h) and Bσ(y;h)=cσ(h)−h(y). In (3), θ only replaces the center by cθ=θc++(1−θ)c−. The mixed term remains. It is not claimed that this freedom already constitutes a sign operation.

## Polynomial profile with dense coverage

The initial interior compact profile is replaced by the following explicit profile on the whole window:

    ψ_T(t)=(T²−t²)² for |t|<T, zero outside,
    g_T=(1/4−∂²)ψ_T,
    g_T(t)=(T²−t²)²/4+4T²−12t² for |t|<T, zero outside.  (5)

Since ψ_T and ψ_T′ vanish at both endpoints, the distributional second derivative adds no masses. Integrating by parts twice one obtains ∫g_T e^(±t/2)=0 exactly.

On (0,T), g_T′(t)=−t(T²−t²+24)<0; g_T(0)>0 and g_T(T−)=−8T²<0. Hence it has exactly two simple interior zeros ±r_T, where

    r_T²=T²+24−sqrt(32T²+576),  0<r_T<T.                 (6)

The positive sign is on (-r_T,r_T); the negative one on the two exterior strips. The measures μσ,± are thus completely specified by polynomials and exponentials. g_T is compact BV; its transform is O((1+|τ|)^(-1)), and therefore log(2+|τ|)·ĝ_T∈L². In particular the full operator H_Tg_T is defined in L²(I). That operator is not compressed before forming the potential of (4).

To justify coverage, take F smooth primitive and interior compact. Neighborhoods of radius ε of ±r_T are removed by smooth cutoffs. The error is a sum of two functions F(t)η((t−r)/ε), whose H^s norm is O(ε^(1/2−s)) for any 0<s<1/2 (rescaling and uniform bounds of the smooth envelopes). Hence it also converges to zero in the logarithmic norm of the form. Correct the two moments by means of two fixed bumps supported far from the zeros, with invertible moment matrix. Their coefficients tend to zero. The corrected tests F_ε are primitive, vanish near the zeros and the boundary, and converge to F in form norm.

Now h_ε=F_ε/g_T is smooth compact, since the division only occurs far from the two zeros. Thus the class of products g_T h that are primitive contains a dense core of the form. This is a justification of coverage, NOT of positivity of (4). On that class the product identity is obtained by truncation of the continuous kernel and convergence of the forms; the potential H_Tg_T is kept intact.

The independent verification confirms (5)-(6), the operator domain and the coverage: PROVED as an auxiliary result, without global sign. The polynomial profile is not chosen by similarity with an eigenvector nor by optimization of a_T.


On the subspace where the four averages of h against μσ,± are zero, both centers cσ are zero. There Aσ=h(x), Bσ=−h(y) for both signs and θ does not modify the mixed term. This subspace must be treated directly with the potential and the interactions of (4); no choice of center solves it automatically.


## Effective cancellation of the first archimedean mode between zones

Checked computation: PROVED as an auxiliary decomposition. Use tests of the constructed core that vanish on neighborhoods of ±r_T. Write F=F_L+F_C+F_R according to the three regions (-T,-r_T),(-r_T,r_T),(r_T,T). The supports of the three pieces are separated. Set a_j=2j+1/2 and

    A_j^D=∫_D e^(a_j t)F(t)dt,
    B_j^D=∫_D e^(-a_j t)F(t)dt, D=L,C,R.

The part of the form pairing the center with the two exterior regions is exactly

    Cross(F)=−2 Re Σ_{j≥0}[A_j^L conjugado(B_j^C)
                                +A_j^C conjugado(B_j^R)]
       −2Σ_n Λ(n)/sqrt(n) Re ∫[F_C(t)conjugado(F_L(t−log n))
                              +F_R(t)conjugado(F_C(t−log n))]dt. (7)

It is a decomposition of the pairing of F, not only of the signed energy of h; the potential of (4) is not discarded. The continuous series converges absolutely by separation of supports and K(u)=2Σ_j e^(-a_j u). The L–R interactions, which belong to the two zones of equal sign of g, are not included in Cross.

On the already identified subspace where the four averages of h against μσ,± are zero, F_C has both moments zero: A_0^C=B_0^C=0. Hence the j=0 term of (7) VANISHES exactly. This uses both moments of the center, not only the two global moments of F. That vanishing is not claimed for every primitive F.

The written remainder is

    Cross(F)=−2 Re Σ_{j≥1}[A_j^L conjugado(B_j^C)
                                +A_j^C conjugado(B_j^R)]
              − contacts between center and exteriors.                 (8)

The higher moments do not vanish under the given constraints. Neither do the contacts. Equation (8) locates which interaction remains to be compensated; it constitutes neither a bound nor a positive identity.

For the general carrier the j=0 term of (7) must also be kept. A future construction cannot promote the cancellation of this subspace to the full carrier without supplying its corresponding correction.

## Analytic test of the cross remainder after cancelling j=0

Equations (7)-(8), their convergence and scope were checked independently: PROVED as an auxiliary decomposition, without global sign.

Checked test: PROVED as indefiniteness of the cross remainder. Choose two small intervals J_L⊂L and J_C⊂C, separated from the zeros and the boundary. They can be chosen so that all differences t−s with t∈J_C,s∈J_L avoid the finitely many log n<2T: it suffices to pick two centers whose difference is not a contact and shrink the intervals.

Let η_L,η_C be smooth non-negative nonzero bumps supported in those intervals. Define

    F_D=(1/4−∂²)η_D, D=L,C, and F_R=0.

Each F_D is primitive by integration by parts. The four averages of h=(F_L+F_C)/g_T vanish: those of the center because F_C is primitive, those of the exterior because F_L is primitive. h is smooth compact away from the zeros of g_T.

For a_j=2j+1/2,

    A_j^L=(1/4−a_j²)∫e^(a_jt)η_L(t)dt,
    B_j^C=(1/4−a_j²)∫e^(-a_jt)η_C(t)dt.

The product A_j^L B_j^C is strictly positive for all j≥1. The cross contacts are zero by construction. Hence

    Cross(F_L+F_C)=−2Σ_{j≥1}A_j^L B_j^C<0.

Replacing F_C by −F_C preserves all moments, supports and individual energies, and changes the sign of Cross. The cross remainder is therefore indefinite even on the subspace where θ does not act and the j=0 mode has already disappeared.

This does NOT refute a_T≥0: the contributions a_T(F_L) and a_T(F_C) remain. It does prevent completing the design by claiming that the cross remainder of (8) by itself has favorable sign. A repair must keep and use those individual energies in the same identity, with the relevant contacts inside each piece. That identity has not yet been obtained.


## Constructive status after the check

Neither a choice of θ nor another operator compensating the cross remainder with the self-energies has been constructed. Coverage and the partial cancellation are proved; global domination is not. The indefiniteness test only rules out signing Cross separately. It does not exclude a joint identity and does not establish that such an identity exists in this class.

No new design is proposed until a concrete additional operation on the self-energies and the cross pairing is written. Reformulating its domination as another norm, discriminant or Schur complement would not solve that step.

## Controlled truncation of the separated archimedean couplings

Status: PROVED as an auxiliary estimate; equations (9)-(14), constants, range and density scope checked independently. It is not a new sign mechanism. Under the later authorization to solve subproblems, the infinite computation of (7) is addressed, keeping the exact contacts. Immediate antecedent: (7)-(8) and their convergence proof; difference: an operator-norm bound is now provided, uniform in the tests for fixed gaps, and a sufficient criterion with an explicit error budget. No novelty is attributed to the geometric estimate.

Fix three ordered subintervals I_L,I_C,I_R inside the respective zones, with distances δ_L=inf I_C−sup I_L>0 and δ_R=inf I_R−sup I_C>0. Work with F_D supported in I_D and F=F_L+F_C+F_R primitive. Each piece is not required to be primitive. Set a_j=2j+1/2. For integer J≥0, keep the terms 0≤j<J in the archimedean part of (7). The remainder is

    R_J(F)=−2 Re Σ_{j≥J}(A_j^L conjugado(B_j^C)
                                   +A_j^C conjugado(B_j^R)).          (9)

For two ordered intervals I_D,I_E at distance δ and a>0, the rank-one operator with kernel exp(−a(t−s)), s∈I_D,t∈I_E, has norm

    ||exp(a·)||_{L²(I_D)} ||exp(−a·)||_{L²(I_E)}
          ≤ exp(−aδ)/(2a).                                         (10)

Proof: if b=sup I_D and c=inf I_E, the two integrals of squares are bounded by exp(2ab)/(2a) and exp(−2ac)/(2a). This does not depend on the lengths nor on the size of T.

Accordingly define

    h_J(δ)=exp(−a_J δ)/[2 a_J(1−exp(−2δ))],
    ε_J=sqrt(h_J(δ_L)²+h_J(δ_R)²).

Summing (10), using a_j≥a_J, one obtains

    |R_J(F)| ≤ 2h_J(δ_L)||F_L||||F_C||
                     +2h_J(δ_R)||F_C||||F_R||
              ≤ ε_J ||F||².                                       (11)

The last inequality follows from Cauchy–Schwarz on the two exterior components and 2xy≤x²+y². The sum of operators converges absolutely in norm. Its Hermitian form has, by (11), norm at most ε_J; no pointwise or operator sign of the remainder is inferred.

Let a_T^[J] be the full form a_T on this carrier, replacing ONLY the archimedean coupling L–C and C–R by its first J modes. The following remain intact: the three self-energies, the full L–R coupling, all contacts (including those crossing zones), and the two global moments. Then

    a_T^[J](F)−ε_J||F||² ≤ a_T(F)
                             ≤ a_T^[J](F)+ε_J||F||².                (12)

The retained archimedean block L–C/C–R has rank at most 4J. This does NOT make a_T^[J] finite-dimensional: the contacts and the self-energies still act on infinite spaces.

For δ=min(δ_L,δ_R) and any η>0, an explicit sufficient choice for ε_J≤η is

    J ≥ max(0, ceil(log(sqrt(2)/(η(1−exp(−2δ))))/(2δ))). (13)

Indeed 2a_J≥1 and exp(−a_Jδ)≤exp(−2Jδ). (13) is a conservative choice, not an optimal one.

Reduced obligation and scope: an independent proof of a_T^[J](F)≥ε_J||F||² on the considered carrier would certify a_T≥0 there. That inequality has not been proved. The error can be made as small as prescribed with fixed gaps; it is not assumed that a positive margin exists to absorb it. When the gaps tend to zero, J must grow: no uniform truncation is established. The density already proved allows passing to the original carrier IF the sign is obtained on the whole family of separated carriers; density alone does not produce those proofs.

This estimate only uses K, so it also holds for the falsifiers. Its usefulness is to control a tail when checking future compensations, not to distinguish the true weight nor to solve the global sign by itself.

Splitting the same penalty ε_J among the three regions can be avoided. For any p_L,p_R>0, (11) and two scalar squares give

    |R_J(F)| ≤ p_L||F_L||²+p_R||F_R||²
            +(h_J(δ_L)²/p_L+h_J(δ_R)²/p_R)||F_C||².                 (14)

This yields another explicit lower bound by subtracting the three penalties of (14) from a_T^[J]. The parameters p_L,p_R allow assigning the tail cost to the regions where a future proof has reserve; no such reserve is presupposed. It is an exact application of Young, not a new arithmetic inequality. All retained terms remain unestimated.

## Closing the gaps: control relative to the logarithmic norm

Status: PROVED as an auxiliary estimate, with independent check of (15)-(22), constants, convergence and moment repair. Next subproblem of (9)-(14): remove the positive separation between regions. Antecedents: (10)-(12) only give a bound for fixed gaps; the corpus on logarithmic transmission (phase 121, cited in P124_008 §1) already contains Carleman operators. No novelty of the ingredient is claimed. Here a quantitative estimate of THIS modal tail is given on the full carrier, without gaps and without requiring positive Sobolev regularity.

At a boundary b between two adjacent intervals write x=b−s>0, y=t−b>0. The exact kernel of the tail operator is, for J≥1,

    H_J(x,y)=Σ_{j≥J}exp(−a_j(x+y))
      =exp(−a_J(x+y))/(1−exp(−2(x+y)))
      =exp(−b_J(x+y))/(2sinh(x+y)), b_J=2J−1/2>0.       (15)

Since sinh u≥u,

    0≤H_J(x,y)≤exp(−b_Jx)exp(−b_Jy)/(2(x+y)).           (16)

The operator with kernel 1/(x+y) on the half-line has norm ≤π: the Schur test with weight x^(−1/2) uses the integral ∫_0^∞ y^(−1/2)/(x+y)dy=π x^(−1/2), obtained by y=xz². This bound suffices; norm equality is not used. From (16), for the cross term of one boundary,

    |Cross_J,b(F)|≤π||exp(−b_Jx)F_left|| ||exp(−b_Jy)F_right||
                ≤(π/2)∫exp(−2b_J|t−b|)|F(t)|²dt.      (17)

The integral can be extended to all of R. This proof works with complex functions by taking moduli. It also justifies convergence of the modal pairing by domination, even though the sum of norms of the rank-one pieces no longer converges. For the two boundaries their two bounds (17) are added.

Define the positive logarithmic energy, with F extended by zero,

    L(F)=(1/(2π))∫log(2+|τ|)|Fhat(τ)|²dτ,
    Fhat(τ)=∫F(t)exp(iτt)dt.

It is finite on the declared form domain, without assuming a sign of a_T. For any measurable set E of length |E| and any R>0, split frequencies |τ|≤R and |τ|>R. Plancherel and Cauchy–Schwarz give

    ∫_E|F|² ≤ (2|E|R/π)||F||²+2L(F)/log(2+R).         (18)

Indeed, the low-frequency piece satisfies ||F_low||∞≤sqrt(R/π)||F||; the high-frequency one has squared norm ≤L(F)/log(2+R). One uses |u+v|²≤2|u|²+2|v|². This estimate is not applied to cut pieces; it is applied to the original F.

For r>0, split the integral of (17) into |t−b|<r and its complement. The first set has length 2r; on the second the weight is ≤exp(−2b_Jr). Summing both boundaries,

    |R_J(F)|≤[4rR+πexp(−2b_Jr)]||F||²
                         +[2π/log(2+R)]L(F).           (19)

Choose r=J^(−1/2), R=J^(1/4). One obtains, uniformly in T and in the position of the boundaries,

    |R_J(F)|≤d_J||F||²+e_J L(F),                       (20)
    d_J=4J^(−1/4)+πexp(−(4J−1)/sqrt(J)),
    e_J=2π/log(2+J^(1/4)).

Both constants tend to zero. This is convergence in the form norm relative to ||F||²+L(F), WITHOUT gaps. For every F∈P_T in the form domain, define a_T^[J]=a_T−R_J, where the cross remainder is the bounded operator of (15). Then the explicit lower bound

    a_T(F)≥a_T^[J](F)−d_J||F||²−e_J L(F)               (21)

holds on the full carrier. It is defined by subtraction of a bounded form; no additional regularity of the three cut pieces needs to be assumed. On the smooth core it coincides with replacing the adjacent archimedean links by the first J modes. Contacts, two moments, self-energies and L–R link remain intact.

### Why gap closing does not converge to zero in L² norm

For fixed J, at a single boundary take F_ε equal to ε^(−1/2) on both intervals of length ε adjacent to b, and zero outside. It has squared norm 2. Rescaling x=εu,y=εv in (15) and using (16),

    <F_right,H_J F_left> → ∫_0^1∫_0^1[2(u+v)]^(−1)dudv=log 2.

Hence Cross_J,b(F_ε)→−2log 2. To impose both moments, subtract two fixed bumps with invertible moment matrix and supports away from the boundaries. The moments of F_ε are O(sqrt(ε)), so the corrector has norm O(sqrt(ε)). Since the total tail is bounded in L² by (17), correcting changes its value by o(1). The other boundary contributes nothing before the correction if ε is small. The corrected tests belong to the logarithmic domain (they are compact BV) and are primitive. Thus, for each J,

    sup_{F∈P_T, F≠0}|R_J(F)|/||F||² ≥ log 2.           (22)

The uniform bound |R_J(F)|≤π||F||² exists by (17), but not a bound c_J||F||² with c_J→0. There is no uniform convergence to zero in L² norm, not even after the two moments. This does not refute the full form: it only explains why the correct control when closing gaps is (20), with logarithmic energy.

### Obligation that remains

(21) removes the gap requirement and quantifies the error on the whole domain; it does not prove that the lower bound is positive. It still remains to compensate the contacts and the retained modes with enough reserve for the cost d_J||F||²+e_J L(F), or to find an identity avoiding that cost. Convergence of (20) is not enough to infer a sign: a limit is not interchanged with a supposed positive lower bound. The estimate also holds for the falsifiers, and constitutes neither an arithmetic separation nor a global proof.

## Exact gluing at one boundary, without truncation cost

Status: PROVED as an auxiliary decomposition; (23)-(29), factors, domains and passage to the limit checked independently. Antecedents: (15)-(21), the positive decomposition of the kernel K of P46 and 212-78. It is not presented as a new sign source nor as a reflection proof for the arithmetic form. The additional operation consists of keeping the square of moment difference at one boundary and absorbing exactly its two diagonal terms into reflected energies. Unlike (21), it leaves no truncation penalty. The complete regional residue is written, without assuming it positive.

Fix b∈(−T,T) and define on x>0, with extension by zero,

    f_−(x)=F(b−x), f_+(x)=F(b+x),
    α_j(f)=∫_0^∞ exp(−a_jx)f(x)dx, a_j=2j+1/2.

For a>0 set

    k_a^N(x,y)=exp(−a|x−y|)+exp(−a(x+y)),
    N_a(f)=(1/2)∫_0^∞∫_0^∞ k_a^N(x,y)|f(x)−f(y)|²dxdy≥0. (23)

The row sum of k_a^N is exactly 2/a. Hence

    N_a(f)=(2/a)||f||²−∫∫exp(−a|x−y|)f(x)conjugado(f(y))dxdy
                                      −|α_a(f)|².

The j-th summand of Arch−C0||F||² is

    E_j(F)=(2/a_j)||F||²−∫_R∫_R exp(−a_j|t−s|)F(t)conjugado(F(s))dtds.

Separating the two half-lines, the cross term is −2 Re α_j(f_−)conjugado(α_j(f_+)). Completing the square one obtains the EXACT identity

    E_j(F)=N_{a_j}(f_−)+N_{a_j}(f_+)
                                 +|α_j(f_−)−α_j(f_+)|².              (24)

All terms of (24) are non-negative. The identity for finite sums passes to the limit by monotonicity of the three terms. Since Σ_jE_j(F)=Arch(F)−C0||F||² is finite on the form domain,

    Arch(F)=C0||F||²+N(f_−)+N(f_+)+||V_b^arch F||²,                 (25)
    N(f)=Σ_{j≥0}N_{a_j}(f),
    V_b^arch F=(α_j(f_−)−α_j(f_+))_{j≥0}.

Divergent diagonals are not separated when summing. The proof holds first for any F∈L² in each mode and then for every F in the logarithmic domain. In particular (25) proves finiteness of the energies N of the pieces, without requiring the cut of F to have additional regularity.

### Contacts in the same gluing

Write w_n=Λ(n)/sqrt(n), l_n=log n, n<exp(2T). For f on the half-line define c_f(l)=∫_R f(x)conjugado(f(x−l))dx, with zero extension. The real part of the contact splits as

    Re c_F(l)=Re c_{f_−}(l)+Re c_{f_+}(l)
                    +Re ∫_0^l f_−(x)conjugado(f_+(l−x))dx.          (26)

The last term is included in the explicit gluing operator

    (V_b^prime F)_n(x)=sqrt(w_n)[f_−(x)−f_+(l_n−x)], 0<x<l_n.

Its square is exactly the cross contribution of the comb PLUS the penalties w_n∫_0^{l_n}(|f_−|²+|f_+|²). Define the regional form

    q_T(f)=C0||f||²+N(f)−2Σ_n w_n Re c_f(l_n)
                                     −Σ_n w_n∫_0^{l_n}|f(x)|²dx.   (27)

Then the FULL form satisfies

    a_T(F)=q_T(f_−)+q_T(f_+)
                     +||V_b^arch F||²+||V_b^prime F||².             (28)

There is no omitted remainder nor numerical error: all active contacts and all archimedean contributions are present. The contact sums are finite. N(f_±) is finite by (25), so (27)-(28) are defined on the original domain.

### The two moments and the pending residue

The primitive conditions are equivalent, regardless of b, to

    ∫_0^∞ cosh(x/2)(f_−(x)+f_+(x))dx=0,
    ∫_0^∞ sinh(x/2)(f_+(x)−f_−(x))dx=0.                             (29)

(29) is obtained by multiplying the original moments by exp(∓b/2) and adding/subtracting. The pieces have finite support. It is not imposed that each piece satisfy the two moments separately.

The candidate V_b=(V_b^arch,V_b^prime) has, by (28), EXACT residue q_T(f_−)+q_T(f_+). It is not known that this residue is non-negative, nor does it follow from N≥0: C0<0 and the arithmetic terms of (27) remain. If the residue turns out negative, the gluing squares could compensate it; its positivity is not required as a necessary condition for the goal.

This design solves only the archimedean gluing and writes the contacts with their exact penalties. It is generic for non-negative weights and positive delays, also for the falsifiers. It does not yet satisfy the final requirement of a nonlinear arithmetic mechanism giving the sign. The next concrete obligation is to control (27) under the two coupled conditions (29), keeping the squares of (28); that obligation is not declared solved and the residue is not called a positive energy.


### Diagnosis of the gluing square

NUMERICAL, not certified: `build_079_data/check_gluing.py` evaluates the arithmetic channel with b=0 on the saved even vector T=0.8, reconstructed in its piecewise basis and corrected in both moments. Gauss quadratures of orders 64 and 96, split at all original and reflected breakpoints, give norm 1 (error <4e−15), moments <3e−17 and

    ||V_b^prime F||² ≈ 1.40645379239075,
    channels n=2,3,4: 0.45288941915506, 0.60700843323509, 0.34655594000061.

The saved energy is 5.29432592315062e−12; it was not recomputed or recertified here. The values are numerical evidence that the candidate V_b extracts too much energy in this window. One should not propose q_T(f_−)+q_T(f_+)≥0 as a mechanism based on this decomposition. The exact identity remains valid, but in this diagnosis the positive squares need an order-one cancellation with the regional residue. The auxiliary progress is writing the gluing without truncation error, not having gained a positive reserve for the global sign.

### Diagnosis of the regional negative sector, T=0.8

NUMERICAL, without continuous index certification. `build_079_data/check_regional.py` builds matrices of q_T in orthonormal Legendre polynomials on (0,T), eliminates the cosh moment by QR and adds the gluing square. The isometric even embedding is F(t)=f(|t|)/sqrt(2); in these coordinates V_arch=0 and

    A_even=q_T+B,
    B(f)=(1/2)Σ_n w_n∫_0^{l_n}|f(x)−f(l_n−x)|²dx.

The factors and formulas of the script were checked independently. The energy N is integrated using H0(u)=exp(−u/2)/(1−exp(−2u)) and the exact tail ∫_u^∞H0=atanh(exp(−u/2))+atan(exp(−u/2)). The inner quadrature removes the diagonal value (its contribution to the differences is zero), but keeps error near that diagonal and near the logarithmic endpoint. It is not interval arithmetic.

| Degree | Gauss order | Negatives of the q matrix | Seventh eigenvalue of q | Computed minimum A_even |
|---|---|---|---|---|
| 16 | 128 | 6 | 0.00300021 | −4.37846e−4 |
| 24 | 256 | 7 | −8.31625e−5 | −1.04833e−4 |
| 24 | 512 | 6 | 0.000233080 | −2.56044e−5 |
| 32 | 512 | 7 | −0.00101102 | −2.56078e−5 |

Comparing the two degree-24 rows isolates the quadrature variation; the two order-512 rows isolate the degree variation. The seventh sign is NOT resolved. The first six eigenvalues are approximately −1.637, −1.235, −0.632, −0.507, −0.182, −0.070: they constitute a negative signal robust to these variations, not a rigorous proof of six continuous directions. It is not concluded that the continuous index is six or seven. The minima of A_even are errors/approximations without certified sign and are far larger than the scale of the saved ground value; they do not refute positivity.

In each matrix the negative directions of q and their complement were separated. Writing A=q+B in blocks gives the exact Schur complement of that matrix

    S=A_--−B_-+ A_++^(-1) B_+-.

The computed minima of A_++ were between 0.855 and 0.969; solve residuals <2.1e−16. The block A_-- alone had positive minimum between 2.87e−4 and 8.48e−4, while the Schur correction had norm between 0.224 and 0.245. Hence checking only the original negative block after adding B does NOT justify the sign of the full matrix. This coupling is not discarded and the Schur subtraction is not interpreted as an additional positive energy.

This computation contributes no new mechanism: it makes concrete that the regional compensation involves several directions and their coupling to the complement. To turn the diagnosis into a result one needs to certify a matrix of negative tests and control the remainder; that task is not replaced by the floating-point count. The global sign and an independent arithmetic formula for the transfer remain open.

## Three negative regional directions with analytic bound and intervals

Status: PROVED by an analytic majorant and an interval certificate PASS, checked and reproduced independently; constant 1/600 also checked. The computational certification depends on the implementation of mpmath.iv. Regional result, not negativity of a_T. Immediate antecedent: previous diagnosis of q_T at T=0.8. The change consists of replacing all singular quadrature by an explicit majorant with elementary integrals and fixing the tests rationally before certifying. Knowing eigenvectors of the target form is not needed.

Fix T=4/5. For f(x)=p(x/T) on (0,T), zero outside, define on the unit square

    I_−(p)=∫∫|p(z)−p(v)|²/|z−v| dzdv,
    I_+(p)=∫∫|p(z)−p(v)|²/(z+v) dzdv.

With H0(u)=Σ_j exp(−a_j u), for u>0,

    H0(u)=1/(4sinh(u/2))+1/(4cosh(u/2))≤1/(2u)+1/4,
    ∫_u^∞H0(v)dv=atanh(exp(−u/2))+atan(exp(−u/2))
                  ≤(1/2)log(4/u)+u/8+π/4.                         (30)

The second bound uses coth(u/4)≤1+4/u and log(1+u/4)≤u/4. Separating the interior (0,T) from its exterior in N, and using C0=−γ−π/2−3log2−logπ, one obtains the quadratic majorant

    q_T(f)≤U(p),
    U(p)=T cbar∫|p|²−(T/2)∫|p|²log(1−z²)
         +(T/4)(I_−(p)+I_+(p))
         +(T²/2)(∫|p|²−|∫p|²)
         −2Σ_n w_n Re c_f(log n)−Σ_n w_n∫_0^{log n}|f(x)|²dx,
    cbar=−γ−log(2π)+T/4−log T.                                    (31)

All integrals without limits in z are taken over (0,1). In the last two terms f is extended by zero. Active contacts: n=2,3,4; only log2<T produces an internal contact. The contacts and penalties of q are kept exactly; only N is bounded from above, in the direction needed to certify regional negativity.

### Explicit tests, with exact moment

Let P_n be the Legendre polynomials and

    p_n(z)=P_n(2z−1)−[∫_0^1P_n(2u−1)cosh(Tu/2)du]/[∫_0^1cosh(Tu/2)du],
    f_k(x)=Σ_{n=1}^8 V_nk p_n(x/T), k=1,2,3, 0<x<T,
    V=(1/10000) *
      [[−8787, 2039, 1009],
       [ 3613, 8461,  −87],
       [ 3082,−4155, 3429],
       [  −35,−2573,−6207],
       [ −179,  212,−3361],
       [ −294, −504, 5728],
       [ −340,  163, 1716],
       [  −50, −214,−1281]].                                     (32)

Each f_k has exactly zero cosh moment. F_k(t)=f_k(|t|)/sqrt2 belongs to P_T: the second moment reduces to the same one by parity. The tests are compact BV, hence belong to the logarithmic domain. The minor of the first three rows of 10000V equals −319025298190≠0; together with the independence by degrees of p_1,...,p_8, it proves independence of f_1,f_2,f_3.

### Evaluation without quadrature

`build_079_data/regional_upper.py` evaluates the polarization of (31) by means of integrals of monomials. For I_− one divides p(z)−p(v) by z−v and integrates over triangles. For I_+ one uses

    ∫_0^1∫_0^1 z^u v^vexp/(z+v) dzdv
        =(A_u+A_vexp)/(u+vexp+1),
    A_0=log2, A_k=1/k−A_(k−1).

Here vexp denotes an integer exponent, not the integration variable. The logarithmic moments are

    ∫_0^1z^(2m)log(1−z²)dz
       =[2log2−2H_(2m+2)+H_(m+1)]/(2m+1),
    ∫_0^1z^(2m+1)log(1−z²)dz=−H_(m+1)/(2m+2).

The cosh moments are enclosed by their positive series with 32 terms and a geometric bound for the tail; the moment correction of the test is defined by the EXACT quotient, not by the midpoint of an interval.

`regional_seed.json` fixes (32). `certify_regional.py` evaluates the restricted 3×3 matrix of U using mpmath.iv at 70 digits; it uses neither diagonalization nor quadrature. The intervals of the LDL pivots of its opposite lie strictly inside

    (0.22998,0.23000), (0.09419,0.09421), (0.00182,0.00183).

It also checks by intervals that each diagonal dominance margin of that opposite is >1/600. The full output is `regional_certificate.json`. This gives, for all c∈C³,

    q_T(Σ_k c_k f_k)≤U(Σ_k c_k p[f_k])
                                  ≤−(1/600)Σ_k|c_k|²,             (33)

where p[f_k](z)=f_k(Tz). The constant refers to the coordinates (32), not to an L² normalization. It is an interval-arithmetic-assisted proof that the regional negative index is ≥3; it does NOT establish that it is six or seven nor compute the exact index.

### Consequence for the design

A positive repair of rank r<3 of q_T on the subspace of zero cosh moment cannot make it non-negative: its kernel intersects the three-dimensional space of (32) nontrivially, and (33) remains strictly negative on that intersection.                                             (34)

The scope is this regional form and this carrier. It does not exclude every construction with rank-two corrections in other objects. Nor does it refute a_T≥0: the gluing squares of (28) are kept and can compensate q_T. The proof only turns part of the diagnosis into a rigorous restriction on finite-rank regional repairs; the sufficient arithmetic compensation still has to be built.

## Explicit rank-three repair on the certified subspace

Status: PROVED as a repair on E, by an interval certificate PASS checked and reproduced independently (128 modes). Computational dependency: mpmath.iv. T=4/5 and E=span{f_1,f_2,f_3} of (32), with zero cosh moment, are kept. Antecedent: (33)-(34) proves that a positive repair of rank<3 does not suffice even on E. The Gram projection is a standard ingredient already considered in the corpus (RULES_AVOID W2); it is not presented as a new global sign mechanism. Here a concrete repair of this subproblem is constructed and verified, without inverting the target form.

In the even sector, the embedding F(t)=f(|t|)/sqrt2 gives

    a_T(F)=q_T(f)+B(f),
    B(f)=||Lf||²,
    (Lf)_n(x)=sqrt(w_n/2)[f(x)−f(l_n−x)], 0<x<l_n, n=2,3,4.

Define g_k=Lf_k and its matrix G_ij=<g_i,g_j>. The g_k are piecewise polynomial functions with coefficients defined exactly in (32). For G>0, set

    s_k(f)=<g_k,Lf>,
    C_3(f)=s(f)*G^(-1)s(f),
    P_G=orthogonal projection onto span{g_1,g_2,g_3},
    W_3f=(I−P_G)Lf.                                                (35)

The inner product convention is conjugate-linear in the first entry. The functionals are also written without abstract operators:

    r_k(x)=Σ_n w_n 1_(0,l_n)(x)[f_k(x)−f_k(l_n−x)], 0<x<T,
    s_k(f)=∫_0^T conjugado(r_k(x))f(x)dx.                           (36)

The zero extension of f_k is used. The formula comes from (I−R_l)^2=2(I−R_l) for the unitary reflection R_l on L²(0,l). The only inverse in (35) is that of the 3×3 Gram matrix of the gluing, not an inverse or root of a_T.

By orthogonal projection,

    0≤C_3≤B,
    B(f)=C_3(f)+||W_3f||²,
    a_T(F)=q_T(f)+C_3(f)+||W_3f||².                               (37)

If f∈E, then W_3f=0 and C_3(f)=B(f). Moreover, B−C_3 has zero pairing with E against any test. G>0 implies that C_3 has rank exactly 3 because s(Σc_kf_k)=Gc. Positivity of q_T+C_3 outside E is not claimed.

### Certification by a lower bound, without quadrature

`build_079_data/compensate_regional.py` computes G and the restriction to E of the lower bound

    A_128(f)=C0||f||²+Σ_{j=0}^{127}N_{a_j}(f)
             −2Σ_n w_n Re c_f(l_n)−Σ_n w_n∫_0^{l_n}|f|²+B(f).

Each omitted mode N_{a_j}≥0, so A_128≤q_T+B exactly. There is no need to estimate a small tail nor to assume a reserve to absorb it.

The exponential integrals of each mode are computed exactly for polynomials by recurrences. For β=aT and p in the variable z=x/T,

    h_p(z)=Σ_{r=0}^{deg p}(−1)^r p^(r)(z)/β^(r+1),
    ∫_0^z exp(−β(z−v))p(v)dv=h_p(z)−h_p(0)exp(−βz),
    I_0=(1−exp(−β))/β, I_k=(k I_(k−1)−exp(−β))/β.

These identities evaluate Toeplitz, the reflected term and all the contacts, with the exact moments enclosed as in the previous certificate. The code uses mpmath.iv at 70dps and verifies LDL of both matrices, without diagonalization or quadrature in the interval run.

The certified intervals of the pivots of A_128 are positive and close to .00750177, .00354991, .02166562; those of G are positive and close to .38126223, .19452065, .17273963. The interval run was reproduced independently.

### Scope and next residue

The certificate proves that (q_T+C_3)|_E=(q_T+B)|_E>0 and explicitly repairs the three directions previously certified negative, with minimal rank 3 for that task. This conclusion is not extended to the complement nor to T other than 4/5. The new residue on the whole even sector is q_T+C_3; the square W_3 vanishes exactly on E. The sign of that residue and the control of its coupling with the complement are missing. The previous diagnosis already warns that checking only the E block is not enough.

The projection construction is generic and can be repeated for falsifiers; the local result does not establish a global arithmetic separation. This step performs a concrete compensation where before there was only a rank obstruction; it does not complete the global proof.

### Certificate result and diagnosis outside E

The run `python3 compensate_regional.py --interval --modes 128` gave PASS. The six interval pivots of A_128 and G are strictly positive; full output in `regional_compensation_certificate.json`. The proof uses only the positive lower bound and the exact contacts, not the floating-point eigenvalues of the previous diagnosis.

NUMERICAL, not certified: `check_gluing.py` was extended to evaluate the correction C_3 and the new square W_3 on the saved even vector T=.8. Quadratures 64/96 split at breakpoints give

    B(f)≈1.40645379239075,
    C_3(f)≈1.38089100495599,
    ||W_3f||²≈0.025562787434764.

The saved energy is still 5.29432592315062e−12, not recertified. The repair reduces the extraction in that test, but the remaining square is still excessive according to this diagnosis. The local repair is not promoted to positivity of q_T+C_3 on the whole carrier. The solution of the subproblem is strictly the compensation of E; the other directions and their coupling are still missing, with enough precision for the global sign.

## Positivity of the infinite regional complement

Status: PROVED as a regional bound and control of the infinite complement; analytic proof, interval constant and passage to both parities checked and reproduced independently. Computational dependency of the constant at T=4/5: mpmath.iv. Antecedents: (27), (35)-(37), finite reduction L2 already existing in P46. No new global equivalence is claimed, nor that the remaining finite block is positive. An explicit lower bound for the infinite complement of THIS regional form is provided here, instead of inferring its sign from finite matrices.

Work with f supported in (0,T), with N(f)<∞. No moment restrictions are needed for the following bound. Define

    I(u)=∫_u^∞H0(v)dv=atanh(exp(−u/2))+atan(exp(−u/2)),
    s_in(T)=Σ_{log n<T}Λ(n)/sqrt(n),
    s_all(T)=Σ_{log n<2T}Λ(n)/sqrt(n),
    c_T=C0+2I(T)−2s_in(T)−s_all(T),
    κ_T=1 if 0<T≤2; κ_T=exp(−T/2) if T>2.                       (38)

For 0<u≤T, H0(u)≥κ_T/(2u). The bound exp(−T/2) follows from 1−exp(−2u)≤2u. For the improvement κ_T=1 when T≤2, set a=u/2≤1: sinh a≤a cosh a and cosh a≤1+a give

    H0(u)=1/(4sinh a)+1/(4cosh a)≥(1+a)/(4a cosh a)≥1/(4a).

The bound cosh a≤1+a can be verified via cosh a≤Σ(a²/2)^k=1/(1−a²/2)≤1+a for 0≤a≤1. On the other hand I''=−H0'>0. Separating the energy N into the square (0,T)² and its exterior, omitting only the positive internal reflected kernel and using convexity on the tail, one obtains

    N(f)≥(κ_T/4)∫_0^T∫_0^T |f(x)−f(y)|²/|x−y| dxdy
                                          +2I(T)||f||².

The internal contacts with log n≥T are zero; the others satisfy |c_f(log n)|≤||f||². Each penalty ∫_0^{log n}|f|²≤||f||². Hence

    q_T(f)≥(κ_T/4)∫∫ |f(x)−f(y)|²/|x−y| dxdy+c_T||f||².         (39)

### Elementary diagonalization of the comparison

Let p_n(x)=sqrt((2n+1)/T)P_n(2x/T−1), orthonormal Legendre basis, and H_n=Σ_{k=1}^n1/k (H_0=0). On the unit interval set

    (Dp)(z)=∫_0^1[p(z)−p(v)]/|z−v|dv.
For monomials, division of z^n−v^n and integration over v<z and v>z gives

    D(z^n)=2H_n z^n−Σ_{k=0}^{n−1} z^(n−1−k)/(k+1).

Thus D preserves degrees and is symmetric on polynomials. Legendre orthogonality implies D(P_n(2z−1))=2H_nP_n(2z−1). This proves the eigenvalue without an imported spectral identity.

The form d(f)=(1/2)∫∫|f(x)−f(y)|²/|x−y| has pairing d(f,p_n)=2H_n<f,p_n>, with the conjugation convention adjusted to the linear argument. For f of finite energy, the identity is justified by Cauchy–Schwarz in the energy and by the divided kernel of p_n, which is bounded. Subtracting any finite sum of its coefficients and using d≥0 gives

    d(f)≥2Σ_{n=1}^M H_n|<p_n,f>|².

There is no need to claim that polynomials are a form core for this inequality. Letting M→∞ and using Parseval, (39) implies

    f⊥span{p_0,...,p_(N−1)} ⇒
    q_T(f)≥(κ_T H_N+c_T)||f||².                                  (40)

The scale T cancels between the norm and the comparison energy; no factor 1/T appears in (40).

### Explicit bound and scope for both parities

For every fixed T, H_N→∞. For example, for any γ>0 choosing

    N=ceil(exp(max(0,(γ−c_T)/κ_T)))

guarantees κ_T H_N+c_T>γ, since H_N≥log(N+1). It is a conservative and explicit bound, not an estimate of the exact index.

At T=4/5, the interval evaluation of (38) gives

    c_T≈−5.01972493487543,
    H_96+c_T≈0.127038212680009>1/8.

Thus, with the certified and checked constant,

    f⊥p_0,...,p_95 ⇒ q_(4/5)(f)≥(1/8)||f||².                   (41)

Code `build_079_data/certify_regional_bulk.py`, output `regional_bulk_certificate.json`; it only verifies constants, while (39)-(40) are the proof of the infinite statement.

For the even sector, a_T=q_T+B with B≥0. For the odd one, the same gluing gives

    a_T(sign(t)f(|t|)/sqrt2)=q_T(f)+2Σ_j|α_j(f)|²
                          +(1/2)Σ_n w_n∫_0^{l_n}|f(x)+f(l_n−x)|²dx.

Therefore (40)-(41) also bound both full forms on their respective high subspaces, when additionally imposing the cosh moment (even) or sinh moment (odd). This does NOT claim the sign of their low blocks.

To keep each moment exactly, let Q_h be the orthogonal projection onto the complement of h=cosh(x/2) or h=sinh(x/2), and E_low=span{Q_h p_0,...,Q_h p_95} inside h^⊥. It has dimension 96: h is not a polynomial and the projection annihilates no nonzero polynomial combination. Its complement in h^⊥ is orthogonal to the 96 polynomials, so it satisfies (41). Hence there remains a low block of dimension 96 per parity, with a coercive infinite complement.                                      (42)

The mixed terms between that block and its complement remain. A positivity proof for the isolated low block is not enough; nor does (42) produce an arithmetic formula for its Schur complement. The estimate uses only absolute bounds of the contacts and holds with adapted constants for falsifiers. Its contribution is to control the infinite sector rigorously, not to solve or replace the global sign obligation.

Regional index corollary: at T=4/5, (33) and (41) give 3≤n_−(q_T|cosh^⊥)≤96. The upper bound is obtained by dimension: a negative subspace of dimension 97 would intersect the coercive complement, contradiction. The exact index is not identified and the 6/7 diagnosis is not turned into a theorem.

## Computable correction of the coupling and a posteriori residue

Status: PROVED as an identity and sufficient criterion, checked independently; the final matrix has not been evaluated or certified. Explicit antecedents: Feshbach/layer formulas of phase 77 and 114_d_207_SCALAR_GAP_SPLIT_INVARIANCE_AND_GREEN_PIVOT, which prevents obtaining a sign simply by dividing a scalar gap. No novelty of Schur or of the residual identity is claimed. The development here specifies a finite correction operator inside the coercive complement of (42); it uses its form matrix, not only the scalar constant. The scalar bound is applied only to the residue left after that resolution.

Fix T=4/5 and a parity. On the primitive Hilbert space h^⊥ of (42), A is the operator of the full form of that parity. Let E:C^96→E_low be the column map e_i=Q_h p_i (i=0,...,95), Π_H the projection onto the high complement, and

    P=E*AE, C=Π_H AE,
    H=compression of A to the high complement, H≥γI, γ=1/8.

The basis e_i is not assumed orthonormal: P is the matrix of the form in those coordinates, not a matrix of eigenvalues in Euclidean norm. The e_i are polynomials plus multiples of h, with piecewise smooth compact extension. Their transform is O(1/|τ|); the archimedean symbol grows logarithmically and the contacts are bounded. Hence the e_i belong to the operator domain and C has columns in L². The primitive compression does not invalidate this conclusion because the moment representatives have the same regularity.

### A finite corrector with its own formula

For any integer M>96, set N=96 and

    w_k=p_k−[<h,p_k>/<h,p_N>]p_N, k=N+1,...,M,
    W:C^(M−N)→L²(0,T), columns w_k.

The w_k are in the high complement and are independent. The denominator is not zero: by Rodrigues and integration by parts, <h,p_n> is a positive constant times ∫_0^T h^(n)(x)x^n(T−x)^n dx; the derivatives of cosh(x/2) and sinh(x/2) are strictly positive on (0,T). This also specifies exactly the moments of the high tests. A small moment is not replaced by zero.

Define the matrices and the operator

    K=W*HW, D=W*C,
    Z=WK^(-1)D, R=C−HZ,
    S_Z=P−D*K^(-1)D.                                             (43)

K≥γW*W>0, so the finite inverse is justified without assuming the sign of A. The w_k are in the operator domain by the same argument as the e_i. H is the self-adjoint compression defined by the form; on these columns HW=Π_H AW and HZ=Π_H AZ. Hence R has columns in L² of the high space. The operator Z takes low coordinates and returns an explicit high correction via a coercive matrix. Galerkin gives W*R=0, but this alone does not give a small bound on R.

### Identity and bound for the mixed terms

The exact Schur complement is S=P−C*H^(-1)C. Expanding R and using Z*HZ=D*K^(-1)D, one obtains

    S=S_Z−R*H^(-1)R,
    S_Z−8R*R ≤ S ≤ S_Z.                                         (44)

For F=Ec+y, y in the high form domain, one also has the exact identity

    a_T(F)=c*S c+||H^(1/2)(y+Zc+H^(-1)Rc)||².                   (45)

Here a_T is read in the corresponding parity embedding. The root of H is legitimate by (42); no root of the target form is taken without knowing its sign. The formula does not suggest that H^(-1) has been computed: it disappears from the verifiable sufficient condition

    S_Z−8R*R ≥0.                                                (46)

The matrix R*R is the L² Gram of the residues of the high equation, not a quadrature residue nor a coefficient norm. Replacing it by a floating-point solve error does not verify (46). If R=0, (43) reproduces the exact Schur complement; it is not claimed that some finite M has R=0 nor that the sequence of these residues converges in L².

### What is solved and what is not

The formulas specify which operator to correct and how to convert a rigorous control of its residue into a control of ALL high couplings. The factor 8 is established by (41), not adjusted numerically. No matrix of (46) with certified sign has been computed, nor is it assumed that the gap 1/8 suffices to do so. The computation requires P,K,D and the L² products of R with enough precision; the isolated low block is not enough, nor is increasing M without controlling that residue.

This is an application of the known residual method to the concrete complement built here, not a new sign proof nor a global solution. A certification at T=4/5 would not replace a construction valid for all T either. The global arithmetic obligation remains open.

## Well-conditioned primitive bases to run the corrector

Status: PROVED as a basis arrangement and coercivity, with formulas, interval implementation and constants checked and reproduced independently. Computational dependency: mpmath.iv. Concrete antecedent: (42)-(43). Although those bases are exact, the low basis Q_h p_0,...,Q_h p_95 almost loses a dimension, and the high one divides by the tiny moment <h,p_96>. Both are replaced to avoid these problems, without rounding moments to zero. No new sign source is claimed; the already defined corrector is made executable with well-conditioned bases.

Set N=95, α_n=<p_n,h> (positive reals),

    h_low=Σ_{n=0}^N α_n p_n, h_tail=h−h_low,
    ε=||h_tail||²/||h||²,
    e_n=p_n−(α_n/α_0)p_0, n=1,...,N.                              (47)

The low basis now has dimension 95, belongs to h^⊥ and consists only of polynomials. Its Gram is I+ββ*, β_n=α_n/α_0; hence its spectral condition number is at most ||h||²/α_0².

In contrast, the Gram of the previous basis Q_h p_0,...,Q_h p_95 is I−aa*/||h||², a=(α_0,...,α_95), with minimal eigenvalue ε and condition number 1/ε. The bound below shows that this representation required keeping a difference of more than 374 decimal orders, even though the geometric space was well defined.

### Coercivity of the new complement

If f∈h^⊥ is orthogonal to the e_n of (47), its low coefficients are proportional to those of h: f_low=t h_low. The moment gives t||h_low||²=−<h_tail,f_tail>, and by Cauchy–Schwarz,

    ||f_low||²≤[ε/(1−ε)]||f_tail||²,
    ||f_tail||²≥(1−ε)||f||².

Applying (39) and Bessel to the coefficients of degrees≥96,

    q_T(f)≥[κ_T H_96(1−ε)+c_T]||f||².                            (48)

For T=4/5, ε is enclosed by the Taylor remainder of h of degree 95:

    ε≤δ_h:=T exp(T)(T/2)^192/[(96!)²||h||²],
    ||cosh(x/2)||²=(sinh T+T)/2,
    ||sinh(x/2)||²=(sinh T−T)/2.                                 (49)

The orthogonal projection onto polynomials approximates at least as well as that Taylor polynomial. The uniform bound of the remainder is exp(T/2)(T/2)^96/96!, valid for both h; integrating its square proves (49).

The certificate verifies δ_h<10^(−374) for both parities and

    H_96(1−δ_h)+c_T>1/8.

Thus the new complement is still coercive with 1/8. The two moments are imposed exactly by parity, not by a tolerance. The bound on the regional index inside cosh^⊥ improves to 3≤n_−≤95; no exact index is claimed.

### High basis without small denominators

Define for k≥96

    w_k=p_k−[α_k/||h_low||²]h_low.                               (50)

Each w_k is in h^⊥ and is orthogonal to the e_n. They are independent by their coefficients in p_k. For any finite collection its Gram is

    G_high=I+vv*/||h_low||², v=(α_k),
    cond(G_high)≤1/(1−ε).

There is no division by α_96. In L², the whole new complement is parametrized this way: choose an arbitrary f_tail and correct its moment with −<h_tail,f_tail>h_low/||h_low||². This does not by itself claim convergence in graph norm of a Galerkin algorithm.

The moments are computed without subtracting nearly equal integrals. Rodrigues and the beta integral give the positive series

    α_n=sqrt(T(2n+1))(T/2)^n
        ×Σ_{r≥0, r≡n+σ (mod2)} (T/2)^r (n+r)!/[r!(2n+r+1)!],    (51)

with σ=0 for h=cosh and σ=1 for h=sinh. The ratio between successive terms of that parity is ≤(T/2)²/[(r+1)(r+2)], which allows enclosing the tail after any prescribed number of terms.

`build_079_data/regional_bases.py` implements (47),(50),(51) in Legendre coordinates and returns intervals for their coefficients. The certification uses 32 positive terms per moment, not quadrature. It verifies by intervals that the low Gram has condition<27/20 and that the excess of the high condition bound over 1 is<10^(−370), besides keeping the coercivity 1/8. The explicit orthogonality checks in the script verify the 95 low columns and four high ones; the result for the whole family is proved algebraically above, not inferred from that sample.

Formulas (43)-(46) are now used with E:C^95→span{e_1,...,e_95} and W with columns w_96,...,w_M. The factor 8 remains valid. This solves the conditioning of the Grams and the imposition of moments; it does not evaluate P,K,D or R*R, does not guarantee the conditioning of the sign block and does not prove (46). In particular, it does not justify converting high-degree polynomials to monomials in ordinary precision nor discarding the pending coupling.

## Evaluation of the block and the corrector after extracting the singularities

Status: formulas checked; NUMERICAL evaluation, without interval bounds on the matrices or on the functional residue. Antecedents: (43)-(51) and the quadrature error detected in check_regional.py. evaluate_blocks.py is implemented in Legendre coordinates, avoiding direct quadrature of the singularities and the conversion of high-degree polynomials to monomials.

Write

    H0(u)=1/(2u)+r(u),
    I(u)=(1/2)log(4/u)+π/4+s(u),
    s(u)=(1/2)log[(u/4)/tanh(u/4)]−atan(tanh(u/4)).                (52)

r is regular at 0, with r(0)=1/4; it is evaluated by series near 0 to avoid numerical cancellation. The singular direct term contributes the already proved diagonal H_n. In the tail the matrix of log(1−z) is extracted exactly, with φ_n(z)=sqrt(2n+1)P_n(2z−1):

    L_nn=2H_n−2H_(2n+1)+1/(2n+1),
    L_nm=−sqrt((2n+1)(2m+1))/(|n−m|(n+m+1)), n≠m.              (53)

An algebraic verification of (53) uses the recurrence of multiplication by 2z−1 and the symmetry of the integral: row 0 is ∫P_m(2z−1)log(1−z)=−1/[m(m+1)] for m≥1, by Rodrigues, and equals −1 for m=0. The recurrence determines the remaining rows; the displayed formulas satisfy it. As an additional implementation check it was compared exactly with fractions against integration of polynomials of degrees 0..4.

The rest of the internal energy is integrated over the triangle x=Tu,y=Tuv, without |x−y| or singular denominators in the final weights. The regular direct weight is Tu r(Tu(1−v)), applied to differences of φ. The reflected one is 1/[2(1+v)]+Tu r(Tu(1+v)), applied to differences in even parity and to sums in odd parity. The remaining smooth tail is

    −(1/2)log(1+z)+s(T(1−z))+s(T(1+z)),

and the joint diagonal constant is −γ−log(2πT). The internal contacts carry −w(C+C*), and the reflection between half-lines −wR for even, +wR for odd. The independent check confirmed these factors and the normalized embedding.

### Computed matrices

At T=.8 degrees 0..111 were used: 95 low columns of (47) and 16 high ones of (50). P,K,D and the coefficient matrix Z_coeff=K^(-1)D are computed; the physical operator is W Z_coeff. The finite result S_Z=P−D*Z_coeff was evaluated with Gauss orders 128 and 160.

| Parity | Order | Minimum of P | Minimum of S_Z | Minimum of K |
|---|---|---|---|---|
| even |128|5.32560e−12|5.31894e−12|3.25285|
| even |160|5.32231e−12|5.31490e−12|3.25285|
| odd |128|1.130410e−9|1.129509e−9|3.28857|
| odd |160|1.130400e−9|1.129498e−9|3.28857|

These are eigenvalues of matrices in the coordinates of the bases, NOT eigenvalues normalized by their Grams nor certified bounds of λ_A. The agreement between quadratures is a diagnostic. It does not enclose the errors of the series of r, quadrature, floating-point arithmetic or conversion of moments to float.

The order-160 matrices and bases are preserved in blocks_even_160.npz and blocks_odd_160.npz, together with blocks_diagnostic.json. In those files the key Z contains Z_coeff; W@Z gives its coefficients in the original Legendre basis. The code explicitly restricts T to .8 because its contact list is 2,3,4.

The exact S_Z is an upper bound of the Schur complement, but the floating-point matrix does not constitute a certified upper bound. The solve residuals were <7e−16: they only verify the matrix equation K Z_coeff≈D and NOT the residue R=C−HZ in L² of the infinite complement. Neither R*R nor a certified lower bound S_Z−8R*R has been computed. Hence, the positive minima of the table do not prove (46), nor the full sign in this window nor for all T.

## Evaluation of the residue as a function

Status: operator formula and projection checked; NUMERICAL results without enclosure. `build_079_data/evaluate_residual.py` evaluates the action of the full operator on the corrected polynomial columns U=E−WZ_coeff, and then projects onto the high space. It does not identify the solve residual with R.

Besides the extraction (52), the singular reflected term is computed via

    ∫_0^T p_n(y)/(x+y)dy
       =2(−1)^n sqrt((2n+1)/T) Q_n(1+2x/T),                     (54)

where Q_n(s)=(1/2)∫_(−1)^1P_n(t)/(s−t)dt, s>1. Change of variable and parity prove (54). scipy.special.lqmn is used for the numerical evaluation. The singular direct term contributes H_n p_n; the regular terms are integrated by separating y<x and y>x. For σ=+1 even, −1 odd, the contact operator is

    −Σ_n w_n[f(x+l_n)+f(x−l_n)+σf(l_n−x)],

with zero extension. The reflected formulas change from difference to sum in the odd sector, as in (25).

If A_0 denotes the parity operator without moment compression, the exact projection is

    R= A_0 U−h <h,A_0U>/||h||²
                  −E(E*E)^(-1)E*A_0U.                           (55)

It is valid because E⊥h and the high complement is orthogonal to both. The script approximates the moment of the first subtraction by the finite expansion of h up to the degree of U; that tail is not declared enclosed. The product E*A_0U is obtained from the previously evaluated matrices. The residues are evaluated pointwise before forming their Gram, to avoid subtracting two large nearly equal Grams.

The exterior quadrature is split at all contact changes: 0,T−log2,log3−T,log4−T,log2,T. It still includes squared logarithmic singularities at the endpoints, so its error must be certified or removed before any sign conclusion.

### Diagnosis of the corrector with 16 high modes

With order-160 matrices and degree 111, the inner quadrature of the operator uses 160 nodes. Results:

| Parity | Exterior order | Approximate norm of R*R | Approximate minimum of S_Z−8R*R | Sampled low orthogonality error |
|---|---|---|---|---|
| even |128|0.94378|−1.56429|0.02275|
| even |256|0.98984|−1.56877|0.00558|
| odd |128|0.94248|−1.55377|0.04954|
| odd |256|1.06575|−1.56246|0.01227|

The orthogonality errors are numerical integrals of the residue against E, not solve errors; their variation evidences the cost of the logarithmic endpoints. The order-one negative minima are an unfavorable diagnosis of the sufficient criterion for this corrector, not a refutation of a_T≥0 nor an interval certificate of failure. The norm of the Gram still varies noticeably with the quadrature.

On the lowest coordinate eigenvector of S_Z, the penalty 8v*R*Rv is approximately 8.15e−13 in even parity and 1.21e−10 in odd, below the respective positive values of S_Z. This does not prove a sign either: the couplings with other directions remain, and the full matrix of the criterion has the negative diagnosis shown.

The baseline data are kept in residual_diagnostic.json. The later runs parametrize the order of the saved matrices and use separate names so as not to confuse correctors of different dimension. No floating-point error is interpreted as a bound on R*R.

The corrector was enlarged to 64 high modes (degree 159, matrices at order 192). With exterior quadrature 128, the minima of the scalar criterion S_Z−8R*R were approximately −1.14604 and −1.14524 (even/odd), still unfavorable. These data are in residual_diagnostic_192.json. Increasing the size does not by itself remove the cost of applying the minimal gap to the whole residue.

## Modal improvement of the residual control

Status: PROVED as an auxiliary inequality; argument and interval constants checked and reproduced independently. It is not a certificate of the sign of the computed matrices. The change with respect to (44) consists of keeping the full modal comparison of (39), instead of replacing it by its minimum 1/8. Therefore it is not a mere redistribution of the scalar gap excluded in 114_d_207: it uses additional information on the operator and the orthogonality of the residue to the resolved modes.

Work at T=4/5 with the new bases (47),(50). Let W_∞:ℓ²({96,97,...})→H_high be the exact parametrization by tail coefficients. With η=||h_tail||²/||h_low||², (49) establishes η≤ηbar=10^(−370). One has

    ||W_∞||²=1+η≤1+ηbar,
    a_T(W_∞z)≥q_T(W_∞z)≥Σ_{k≥96}d_k|z_k|²,
    d_k=H_k+c_T−|c_T|ηbar.                                      (56)

Indeed, in (39) the energy of all the high coefficients is kept, only the non-negative low energy is omitted and the term c_T||f_low||² is bounded by −|c_T|ηbar||z||². Here c_T<0 and d_96>1/8. It is not claimed that H≥d_(M+1)I on the whole high space.

For any source r∈H_high, the variational characterization of the inverse gives

    <r,H^(-1)r>
      =sup_y[2 Re<r,y>−a_T(y)]
      ≤Σ_{k≥96}|(W_∞*r)_k|²/d_k.                               (57)

The inequality is obtained by applying (56) on the whole high domain and then enlarging the supremum to the coefficient space with finite diagonal energy. It requires no additional form-core claim for the Galerkin approximations.

For an arbitrary corrector Z=W_M X, where W_M contains w_96,...,w_M, define

    Δ=D−KX=W_M*R,
    R=C−HZ,
    S_X=P−D*X−X*D+X*KX.

Separating in (57) the indices 96..M from the later ones, using growth of d_k and ||W_∞*r||²≤(1+ηbar)||r||², and polarizing, yields

    R*H^(-1)R ≤[(1+ηbar)/d_(M+1)]R*R
                 +(1/d_96−1/d_(M+1))Δ*Δ,
    S_exact=S_X−R*H^(-1)R.                                     (58)

In exact Galerkin Δ=0. The general formula includes the defect of the system, so a computed X need not be treated as an exact inverse. All products are in the low coordinates; the non-orthonormal high basis is already accounted for by ||W_∞||².

`build_079_data/certify_residual_weights.py` encloses the constants with mpmath.iv and establishes

    M=111: (1+ηbar)/d_112<1783/500=3.566,
    M=159: (1+ηbar)/d_160<1573/1000=1.573,
    0≤1/d_96−1/d_(M+1)<8.

Hence a rigorous sufficient condition, for each of those sizes, is

    S_X−ρ_M R*R−8Δ*Δ≥0,                                       (59)

with the respective rational ρ_M. The file residual_weights_certificate.json certifies the constants of this inequality, NOT its matrices.

### Diagnostic application of the improvement

`check_weighted_residual.py` applies the certified weights to the still floating-point matrices and Grams. Approximate results:

| High modes | Parity | Minimum of the diagnostic of (59) |
|---|---|---|
|16 (M111), exterior256|even|4.80e−12|
|16 (M111), exterior256|odd|1.057e−9|
|64 (M159), exterior128|even|5.19e−12|
|64 (M159), exterior128|odd|1.111e−9|

In the four diagnostics all computed eigenvalues were positive. This shows that the modal improvement changes the NUMERICAL viability of the sufficient condition; it does not yet verify (59). The Grams of the residue keep errors from logarithmic endpoints, truncated projection and floating-point arithmetic. The output weighted_residual_diagnostic.json expressly declares NUMERICAL_ONLY.

The next obligation is defined: enclose P,K,D, the corrected action and R*R with error small enough to prove (59), or modify the corrector again if a reliable enclosure fails. That task is not replaced by numerical stability, nor is T=.8 extrapolated to all windows. The global goal remains open.

## Rational approximation with exact cancellation of the tail

Status: PROVED as an auxiliary control of the operator error; argument, signs and transfer checked independently, rational certificate reproduced with result PASS. It does not yet certify (59). Immediate antecedent: (52)-(55) extract the singularity, but evaluate the remainder without enclosure. This step completes that concrete obligation: it keeps kernel and tail jointly and delivers an operator-norm bound, valid for all functions of the domain, not only for the tested polynomials. No new sign source is claimed nor priority over the Taylor approximation.

At T=4/5 set r(u)=H0(u)−1/(2u) and s(u)=−∫_0^u r(v)dv. This normalization coincides with (52): s(0)=0. The function r is holomorphic in |u|<π, including its removable singularity at zero. On |z|=2, write w=z/2=x+iy. Since |w|=1,

    |sinh w|²=sinh²x+sin²y≥(5/6)²(x²+y²),
    |cosh w|²=sinh²x+cos²y≥1/4.

One used |sinh x|≥|x|, |sin y|≥(5/6)|y| and cos y≥1/2 for |y|≤1; the last two follow from the elementary alternating expansions. From H0(z)=1/(4sinh(z/2))+1/(4cosh(z/2)) one obtains |r(z)|≤3/10+1/2+1/4=21/20. Cauchy gives, for r_K(u)=Σ_{k=0}^K c_k u^k,

    |c_k|≤(21/20)2^(−k),
    sup_[0,8/5]|r−r_K|≤δ_K=(21/4)(4/5)^(K+1),
    s_K(u)=−Σ_{k=0}^K c_k u^(k+1)/(k+1).                     (60)

All c_k are rational. An exact recurrence, without evaluating transcendental numbers, is

    b_j=(−1)^j 2^(j+1)/(j+1)!,
    c_k=[(−1/2)^(k+1)/(k+1)!−b_(k+1)/2
                  −Σ_{j=1}^k b_j c_(k−j)]/2.                 (61)

It comes from B(u)r(u)=[exp(−u/2)−B(u)/2]/u, with B(u)=(1−exp(−2u))/u. The first coefficients are 1/4,−1/48,−1/32,7/11520.

Define A_K by the same action as (54), keeping the singular terms, the logarithms and the contacts, and jointly replacing r,s by r_K,s_K. Let e=r−r_K, J(u)=∫_0^u e(v)dv and σ=+1 for even parity, −1 for odd. The diagonal rows of the direct and reflected error sum to

    J(x)+J(T−x)+J(T+x)−J(x)=J(T−x)+J(T+x).

The tail error is exactly the opposite. Hence, on the space L²(0,T) before imposing the moment,

    ((A−A_K)f)(x)=−∫_0^T[e(|x−y|)+σe(x+y)]f(y)dy,
    ||A−A_K||≤2Tδ_K=ξ_K=(42/5)(4/5)^(K+1).                   (62)

The bound follows from the Schur test, since absolute rows and columns are ≤2Tδ_K. The difference extends to a bounded self-adjoint operator; A_K can be defined as A minus that operator on the same domain. Orthogonal compressions do not increase the bound. Approximating s independently would lose this cancellation.

### Transfer to the finite criterion without inverting another matrix

Freeze one X, without requiring it to be an exact solution of any system, and set U=E−WX, G_U=U*U. The symbols A,A_K in the following expressions can be interpreted as the full operators before compression; the columns of U are primitive. Define

    S_X,K=U*A_K U,
    R_K=Π_high A_K U,
    Δ_K=W*A_K U,
    Γ_K=R_K*R_K.

The bases E,W and the projections are the exact ones of (47)-(51), not their floating-point approximations. Then (62) implies

    S_X≥S_X,K−ξ_K G_U,
    (R−R_K)*(R−R_K)≤ξ_K²G_U,
    (Δ−Δ_K)*(Δ−Δ_K)≤ξ_K²||W||²G_U.

Applying Young with any θ>0 and using ||W||²≤1+ηbar, (59) is guaranteed if

    S_X,K−ρ_M(1+θ)Γ_K−8(1+θ)Δ_K*Δ_K−β_K G_U≥0,
    β_K=ξ_K+(1+1/θ)ξ_K²[ρ_M+8(1+ηbar)].                      (63)

It is a sufficient condition; it is not claimed that its matrix is positive. The script certify_kernel_polynomial.py builds the 385 rational coefficients with K=384 and verifies with exact fractions ξ_K<10^(−35). With θ=10^(−20), ηbar=10^(−370) and the largest weight ρ=1783/500 it also verifies β_K<10^(−35), valid therefore for both sizes of (59). The file kernel_polynomial_certificate.json keeps coefficients, exact rational bound and scope of the certificate.

The uncertainty of the regular kernel is thus controlled uniformly, including all non-computed modes. The integrals and arithmetic of S_X,K, Γ_K, Δ_K and G_U, with exact moments, remain pending. Their integrands now contain polynomials, logarithms and the moment-correction functions; they are not considered rational nor automatically certified. In particular, the exterior quadrature and projection error of (55) is not solved by (62). The global sign remains OPEN.

## Polynomial source with explicit singularities

Status: PROVED as an auxiliary identity, checked independently. It completes the analytic preparation of (63), not its matrix inequality. Antecedent (54)-(55): evaluation of Q_n and quadrature of squared logarithms without certified error. Change: express the source before projection by means of polynomials and three logarithms, preserving its singularities exactly. It is not presented as a new arithmetic sign mechanism.

Let f be a polynomial, z=x/T, σ=±1, and define

    D_T f(x)=∫_0^T(f(x)−f(y))/|x−y|dy,
    Q_f(x)=∫_0^T[f(y)−f(−x)]/(x+y)dy,
    C_T=−γ−log(2πT).

Here f(−x) means continuation of the polynomial, NOT zero extension. The division in Q_f is exact: for f(y)=y^m,

    Q_f(x)=Σ_{j=0}^{m−1}(−x)^j T^(m−j)/(m−j).

The operator D_T also preserves polynomials; for m≥0,

    D_T x^m=2H_m x^m−Σ_{j=0}^{m−1}T^(j+1)x^(m−1−j)/(j+1).

With C_prime the contact action (positive in the notation A=Arch−C_prime), the source of the approximating operator (62) is exactly

    A_K f(x)=.5D_T f(x)+C_T f(x)−.5σQ_f(x)
       +.5[σf(−x)−f(x)]log z
       −.5f(x)log(1−z)−.5σf(−x)log(1+z)
       −∫_0^T[r_K(|x−y|)+σr_K(x+y)]f(y)dy
       −C_prime f(x).                                         (64)

To prove it, split f(y)=f(−x)+(x+y)q(x,y) in the singular reflected integral. Its constant part produces f(−x)log((1+z)/z). The reflected diagonal row, combined with −.5f log(1−z²), produces −.5f[log z+log(1−z)]. The regular rows cancel the tail s_K exactly as in (62). This gives (64), including all signs. The contacts keep the zero extension and are polynomial on each interval delimited by their support changes. The regular integral is a polynomial, separating y<x from y>x. The identity holds almost everywhere; all its terms are in L².

The primitive/high projection is applied AFTER (64); it adds the function h of (55). That function is not replaced by a polynomial without an error bound.

### Exact moments for the endpoints

On an affine interval x=a+(b−a)t, the singularities present at its endpoints are kept as log t and log(1−t). For n≥0, k=n+1, H_k=Σ_{j=1}^k1/j and H_k^(2)=Σ_{j=1}^k1/j²,

    ∫_0^1 t^n dt=1/k,
    ∫_0^1 t^n log t dt=−1/k²,
    ∫_0^1 t^n log(1−t)dt=−H_k/k,
    ∫_0^1 t^n log²t dt=2/k³,
    ∫_0^1 t^n log²(1−t)dt=[H_k²+H_k^(2)]/k,
    ∫_0^1 t^n log t log(1−t)dt
        =H_k/k²+H_k^(2)/k−π²/(6k).                            (65)

The first formulas follow by integration or differentiation of ∫t^n; the remaining ones are obtained by differentiating the beta integral in its two exponents at (k,1), with the finite identities of the harmonic numbers. The derivatives under the integral are justified by integrability of squared logarithms in neighborhoods of those exponents. Hence the Gram of functions p(t)+q(t)log t+r(t)log(1−t), with rational coefficients, is computed exactly in Q+π²Q, without exterior quadrature. The module log_polynomial_moments.py implements these six moments and the contraction of coefficients; it checks, among other identities, ||log t−log(1−t)||²=π²/3.

The other logarithms of (64) are smooth on each piece where they were not kept as a singularity. For u∈[a,b] with a>0, c=(a+b)/2, v=(u−c)/c and q=(b−a)/(b+a)<1,

    log u=log c+Σ_{j=1}^L(−1)^(j+1)v^j/j+E_L(u),
    |E_L(u)|≤q^(L+1)/[(L+1)(1−q)].                            (66)

This follows from the integrated geometric series. The endpoint u=0 is never treated with (66): it is kept exactly by (65). The contact points are not rational and must be enclosed; nor is log c rational. The implementation of (65) is the algebraic core, not an automatic enclosure of those coefficients.

With (64)-(66) an integration path without hidden singularities is defined: keep the endpoint logarithms, approximate only the smooth factors with explicit remainder and evaluate their products by (65). The full interval assembly of (63), including the projection h, remains to be executed. The availability of formulas is not interpreted as a certificate of the matrix nor of its sign.

## Controlled replacement of the hyperbolic projection

Status: PROVED as a comparison of projectors, checked independently. Antecedent (55): the evaluator approximated the moment of the source by a truncated expansion of h without enclosing the error. Now the full projectors are compared using the tail bound already proved in (49); the primitive basis is not modified and no small moment is declared zero. This removes a pending non-polynomial integration in (63), without by itself providing the sign.

Let V_95=span{p_0,...,p_95}, h_low=P_95h and h_tail=h−h_low. The low space E of (47) is exactly V_95∩h_low^⊥. The orthogonal projectors onto the primitive high complement and onto the polynomial tail satisfy

    Π_high=I−P_E−P_h,
    Π_tail=I−P_95=I−P_E−P_hlow,
    ||Π_high−Π_tail||=sqrt ε<10^(−187),
    ε=||h_tail||²/||h||².                                    (67)

Indeed, both projections coincide outside the plane generated by h_low,h_tail. In the orthonormal basis of that plane, P_hlow−P_h has matrix

    [ ε                  −sqrt(ε(1−ε)) ]
    [ −sqrt(ε(1−ε))      −ε             ],

whose square is εI. If the tail were zero, the projectors would coincide. The bound ε<10^(−374) comes from (49) for both parities.

For the source V=A_KU and its Grams define

    G_V=V*V,
    B_n=<p_n,V>,
    Γ_tail=G_V−Σ_{n=0}^{95}B_n*B_n.

Then Γ_K=V*Π_high V and

    −δG_V≤Γ_K−Γ_tail≤δG_V,  δ=10^(−187).                     (68)

It is a matrix inequality in low coordinates; δ is NOT an absolute error bound of each entry nor of the norm of the Gram without accounting for G_V. The substitution into (63) produces the following sufficient criterion, with K=384, θ=10^(−20) and either of the two certified weights ρ_M:

    S_X,K−ρ_M(1+θ)Γ_tail−8(1+θ)Δ_K*Δ_K
            −10^(−35)G_U−4·10^(−187)G_V ≥0.                  (69)

β_K<10^(−35) and ρ_M(1+θ)<4 were used. All matrices of (69) are defined with the exact bases E,W; their moment coefficients are enclosed by (51). No integral of h against the source appears: G_V, B_n, S_X,K and Δ_K require only integrals of the sources of (64) against themselves or against polynomials. The hyperbolic coefficients of the bases do not disappear, but they already have a positive series and a tail bound.

certify_projection_transfer.py reproduces with mpmath.iv70 the Taylor bound

    ||h_tail||²≤T exp(T)(T/2)^192/(96!)²

and encloses the norm of the projector difference by 9.20e−189 (even) and 4.03e−188 (odd), both smaller than δ. It saves projection_transfer_certificate.json. The certificate establishes only transfer constants, not matrices nor positivity. The subtraction in Γ_tail still requires sufficient interval precision; performing it in double precision or replacing it by stability between quadratures is not justified.

## Assembler of the source by moments and contacts

Status: auxiliary identity PROVED and checked; implementation checked and numerical verification reproduced independently with PASS_IMPLEMENTATION_CHECK. This step implements (64), without introducing a new candidate or an additional sign mechanism. For non-negative integers k,m and σ=±1,

    J_(k,m)^σ(x)=∫_0^T[|x−y|^k+σ(x+y)^k]y^m dy
      =(1−(−1)^k) m!k!/(m+k+1)! x^(m+k+1)
       +Σ_{j=0}^k[(−1)^(k−j)+σ] binom(k,j)
                        T^(m+j+1)/(m+j+1) x^(k−j).            (70)

Proof: replace |x−y|^k by (y−x)^k on the whole interval and add (1−(−1)^k)(x−y)^k on y<x. The integrated correction is the beta term of (70). Expanding the two remaining polynomials gives the sum. There is no numerical integration nor singularity in this step.

For f=Σa_m x^m and r_K=Σc_k u^k, precompute μ_j(f)=Σ_m a_m T^(m+j+1)/(m+j+1). The sum of (70) is contracted with these moments, plus the beta terms for odd k, in O(K²+K·degree(f)) operations per column. The module polynomial_source.py implements that contraction, D_T, Q_f, the three logarithmic coefficients of (64) and the contacts. It works both with mpmath.mp and with mpmath.iv; only the latter mode encloses the coefficients and roundings.

At T=4/5 the full contact partition is

    0, T−log2, log3−T, log4−T, log2, T.

The program verifies the strict separation of the intervals enclosing those points. On each piece it determines the active contacts by their midpoint; the list contains all support changes, so activity is constant in the interior. Composing the polynomial with x+log n, x−log n or log n−x implements each active term. The endpoints, of measure zero, do not affect the L² source. If the precision does not allow deciding order or activity, the assembly fails explicitly.

check_polynomial_source.py compares the assembly against the original action, integrating separately direct, reflected and tail increments, for a polynomial of degree 4 and r_K of degree 8. It covers both parities and the five pieces, with numerical reference at 100dps and interval coefficients at 60dps. This check is an independent implementation diagnostic, not a proof by quadrature nor a sign certificate. Degree 8 serves to test the operations; it does NOT replace degree 384 of (69).

The assembler keeps the physical variables x; it does not evaluate the Gram nor resolve its possible cancellations. The pending work is to transform each piece to (0,1), apply (65)-(66) with remainder bounds and assemble the matrices of (69) with enough precision.

## Interval integration of products of sources

Status: analytic control and implementation checked independently; test of three identities and two scalar integrals PASS. The full matrices of (69) are still pending. The immediate antecedent is the assembler (70): integrating its sources with an explicit remainder was missing. The new module interval_source_integrals.py connects both steps, without replacing any sign test by numerical agreement.

On each piece x=a+d t, d=b−a>0, transform the four polynomials of (64) by affine composition. If a=0, log(x/T)=log(d/T)+log t is kept; if b=T, log(1−x/T)=log(d/T)+log(1−t) is kept. The presence of these endpoints is determined by the exact partition, not by numerical proximity. For the other factors log(α+βt), the center c=α+β/2 and q=|β|/(2c)<1 allow (66). c>0 and q<1 are required by strict interval comparison.

Let F be the exact source A_Kf on the piece and Ftilde=p+q_0 log t+r_0 log(1−t) its approximant, after replacing only the smooth logarithms. For a polynomial v define C(v)=Σ|coefficients(v)|. If v_j multiplies an approximated logarithm with uniform remainder ε_j, then

    ||F−Ftilde||_(L²(a,b))≤e_F=sqrt(d)Σ_j ε_j C(v_j),
    ||Ftilde||_(L²(a,b))≤n_F
       =sqrt(d)[C(p)+sqrt(2)(C(q_0)+C(r_0))].                 (71)

The first bound uses |v_j(t)|≤C(v_j) on [0,1]; the second uses ||1||_2=1 and ||log t||_2=||log(1−t)||_2=sqrt2. For two sources one obtains by Cauchy–Schwarz

    |<F,G>−<Ftilde,Gtilde>|
       ≤e_F n_G+e_G n_F+e_F e_G.                             (72)

The product of the approximants is integrated with (65), including the factor d of the change of variable. All constants, coefficients, endpoints, logarithms, π² and roundings are computed with mpmath.iv. The program adds the symmetric interval of the budget (72). Although it represents that budget as a non-negative interval, multiplying it by [−1,1] uses its upper endpoint and keeps the required bound.

The function source_inner requires a shared partition of the full interval (0,T). Coinciding endpoints must represent the same exact points, such as those built by polynomial_source.pieces; equality of intervals does not authorize identifying two distinct unknown exact parameters. The module does not use decimal approximation of the contact points to choose the integration domain.

The resulting certification corresponds to A_K and to the exact coefficients enclosed by their intervals. The error A−A_K remains covered separately by (69). Nor does it turn an enclosed entry into positivity of the matrix: all relevant entries must be assembled and a rigorous matrix criterion verified.

check_interval_source_integrals.py checks three integrals with known value (log²t, logt·log(1−t), log²(1+t)) and two norms of the source A_8f of degree 4, one per parity. In the norms, the enclosure comes from (71)-(72) and interval arithmetic; the reference by quadrature at 130dps is only an independent implementation check. The 95×95 Gram is not run in this test, nor is K384 replaced by K8 in the final criterion.

Result of the test: the intervals of the squared norms have widths smaller than 1.946e−39 (even) and 2.154e−38 (odd), with values approximately 1.77351234335 and 0.102218493217. The intervals and references are kept in interval_source_integrals_check.json. They are integrals of the test sources A_8f, not energies of the ground vector nor certified entries of the full Gram of (69).

## Joint contraction of columns

Status: algebraic reorganization and code checked independently; tests of known Grams PASS. It is not a certificate of the matrix of (69). Antecedent (71)-(72): pair-by-pair integration that repeated preparations. The module interval_source_gram.py prepares each column once per piece and shares the smooth expansions, their remainders and the interval moments at fixed precision.

With local components φ_(s,k)(t)=t^k L_s(t), L_0=1, L_1=log t, L_2=log(1−t), and coefficients C_(s,k),i of each approximated source, define

    M_(s,k),(r,l)=∫_0^1 t^(k+l)L_s(t)L_r(t)dt,
    Gtilde=d C^t M C,
    E_ij=e_i n_j+n_i e_j+e_i e_j.                             (73)

The six types of blocks M are Hankel and are computed by (65). The program applies M to each column and then contracts with C^t: O(nD²+n²D) operations if there are n columns and D total coefficients per source, versus O(n²D²) for repeating the contractions pairwise. The intervals of Gtilde_ij are widened by [−E_ij,E_ij] and summed over pieces. Symmetry is imposed by copying each upper entry to its transpose, since both enclose the same exact real number; this does not claim positivity of any matrix selected from the intervals.

The logarithm cache checks context, precision, degree and interval parameters before reusing an expansion. The moment cache belongs to a single context at fixed precision. Reassociating the products may change the interval width, but not its validity. The bound (72) was not changed and no error term was omitted.

check_interval_source_gram.py verifies all entries of the Grams of {1,log t,log(1−t)} and {1,log(1+t),1+log(1+t)}, against analytic formulas, with iv80 and degree 64 for the smooth logarithm. The second test exercises the reuse of one expansion across columns. These tests include neither the 95 columns of the corrector nor the kernel K384; they only verify the joint contraction and the smooth errors, without repeating the reference quadrature at 130dps.

It remains to measure and run the assembly with the real columns of U=E−WX. The small tests do not establish the cost nor the width of the intervals at that scale, and the global sign remains OPEN.

## Frozen corrector and real primitive columns

Status: algebraic procedure and code checked independently; interval reconstruction of 95 columns per parity PASS. Antecedent (73): test Grams, still without the real columns of the corrector. frozen_corrector.py takes exclusively the matrix Z from the files blocks_even_160.npz and blocks_odd_160.npz, interpreting it as the matrix X of (58), with 16 rows and 95 columns. Each finite binary value is converted via as_integer_ratio into an exact rational. The files frozen_corrector_even_160.json and frozen_corrector_odd_160.json keep those rationals and the SHA256 of their source. The hash provides traceability, not a mathematical proof.

T is reconstructed as 4/5, not as the rational corresponding to the saved float 0.8. The bases E,W are reconstructed from (47)-(51), without importing the floating-point matrices A,P,K,D,S. For the fixed rational X,

    U_i=e_i−Σ_{k=96}^{111}X_(k−96),(i−1) w_k,  i=1,...,95.       (74)

The row and column notation of X here starts at 0; the mathematical columns i correspond to code index i−1. To avoid operational ambiguity, the program traverses the list e_1,...,e_95 and the list w_96,...,w_111 in that order. D=KX is not required and the defect term of (69) remains intact. Exact primitivity of U_i follows from the identities of the bases; that a computed interval of the moment contains zero is only an implementation check.

To pass to physical powers the exact formula is used

    p_n(x)=sqrt((2n+1)/T)
             Σ_{j=0}^n(−1)^(n+j)binom(n,j)binom(n+j,j)(x/T)^j. (75)

The reconstruction uses iv400 and 160 terms in the positive moment series of (51), keeping its explicit tail bound. Increasing only dps would have left the 32-term remainder untouched; that is why stable_split now accepts the parameter terms, whose default value is still 32 for the previous certificates.

The frozen data define an exact reproducible corrector even though its choice comes from a floating-point computation. They do not certify that this corrector is sufficient, nor do they transfer to the new computations the signs of earlier numerical matrices. The sources A_384U_i, their Grams, the defect Δ and the sign of (69) remain pending.

Result saved in frozen_corrector_check.json: the 190 reconstructed columns passed the checks. Maximal width of moments: <2.887e−400 (even), <1.071e−399 (odd). Maximal width of physical coefficients: <1.652e−309 (even), <2.347e−309 (odd). These bounds correspond to the reconstruction of U, not to A_384U nor to the Gram. The exact rational provenance is kept in the two JSON files of frozen correctors.

## Refined norm and first source of the real corrector

Status: refinement of the error bound PROVED and code checked independently; first real source assembled with PASS. The antecedent (71) bounds the norm of the approximant by absolute values of coefficients. At high degree that bound may lose the cancellations of the polynomial; there is no need to keep it if the Gram of the approximant is already available.

First compute Gtilde=d C^tMC, WITHOUT adding Taylor remainders. Since its diagonal encloses exactly the squared norm of the approximating source on that piece,

    n_i,new=min(n_i, sqrt(upper(Gtilde_ii))),                  (76)

where both arguments of the minimum are upper bounds and the root is rounded upward, is still a bound on ||Ftilde_i||_2. The budget (72) is kept by replacing n_i with n_i,new. There is no circularity: Gtilde corresponds to explicit functions already integrable by (65), while the remainder added afterwards corresponds to replacing the smooth logarithms by their polynomials. upper(Gtilde_ii)≥0 is required; a wide interval may give a poor bound, but not an invalid one.

interval_source_gram.py implements this order and keeps the previous bound if it were smaller. The two analytic 3-column Grams passed again; in the smooth logarithm test the maximal width dropped from 3.83e−32 to 1.004e−32. That comparison only describes the test, not an improvement already measured on the 95 columns.

build_real_source.py reconstructs the column of index 0 of the even parity of the rational corrector (74), applies the kernel of degree 384 and assembles the five pieces of A_384U_0 with iv400. It is a column of the fixed real object, not a new corrector nor a reduced-degree test. The polynomial source has maximal degree 496, together with the three logarithmic multipliers of (64).

To preserve the computation, the program saves each interval endpoint as its exact dyadic tuple from mpmath (sign, integer mantissa, exponent, bit length), in compressed JSON. The coefficients are not converted to lower-precision decimals. The format records the mpmath version and the fingerprint of the corrector JSON. The pack/unpack check compares all tuples before writing them; reading the persisted file is checked separately.

The point values at the midpoints of the five pieces serve to measure widths and to check that the evaluation is finite. They constitute neither a sign proof of the form nor a replacement for the integration of the Gram. The next obligation is still to form the real integrated entries of (69).

Result of build_real_source.py: PASS for even A_384U_0, five pieces, maximal coefficient width <2.954e−277; time 162.31s including reconstruction, assembly and writing. Artifact real_source_even_0.json.gz, report real_source_check.json. A later reading checked its 4175 intervals at 50dps: each dyadic tuple matched exactly, with the file fingerprint verified. This certifies the persistence of those enclosures, not the integral of the Gram. The observed time corresponds to this column; the joint computation of 95 columns has not yet been measured.

## First integrated entry of the real-source Gram

Status: enclosure obtained with code and formulas checked and reproduced independently with the same result and input fingerprint. Antecedent (76): real source persisted but without integral. arb_source_integral.py runs the same formulas (65),(66),(71),(76) with python-flint 0.9.0, using arb and arb_poly at 500 DECIMAL digits. Composition and multiplication of polynomials are done in native code; the operator is not changed and the bounds are not replaced by quadrature.

To transfer an interval with dyadic endpoints to Arb, align their exponents: endpoints L·2^e and H·2^e, integers L≤H. Use center (L+H)·2^(e−1) and radius (H−L)·2^(e−1). The ball constructor covers its roundings; it is also checked that the ball contains both exact endpoints, whose bit length is required not to exceed the working precision. The precision of the Arb radii may widen the interval and is included in the validated operations.

The integral is computed by pieces, with degree 512 for the smooth logarithms. The moments are evaluated by harmonic recurrences in balls. First the squared norm of the approximant is computed; then the radius 2e nsharp+e² is added. The exact partition of (0,T) comes from the generator of the file, with fingerprint checked; the reader also verifies that shared endpoints have identical dyadic representations. Mere containment of T in an interval is not presented as proof of identity of endpoints.

Result for the even column of index 0 of the real corrector:

    (G_V)_(0,0)=||A_384 U_0||²
       ∈ [0.443886963801320938000048529800836280833610634739973860113084376990299605579014185905735369725002044460152144474905033 ±3.97e−118]. (77)

The decimal representation shown is conservative; the computed internal radius is smaller than 2.548e−118. The five radii per piece are, respectively, smaller than 3.476e−288, 2.548e−118, 9.207e−177, 6.725e−238 and 2.254e−251. The endpoints, remainders and metadata are kept in real_source_integral.json. The computation took 40.51s after loading the source and first passed two checks of integrals with known analytic value.

This value is an entry of G_V of (69), NOT the value of the form a_T(U_0), nor an entry of the Schur complement, nor an eigenvalue. Its positive sign, being a squared norm, does not solve the problem. The progress consists of having the first real integrated product with controlled error at the planned degrees. B_n, the other entries of G_V, S_X,K and Δ_K, and the final verification of (69) are missing. Nor is the result at T=.8 extrapolated to other windows.

## First complete diagonal of the residual criterion

Status: enclosed interval computation; code, formulas and consequence on the infinite subspace checked, enclosure reproduced independently with the same result. Antecedent (77): only G_V,00. arb_residual_diagonal.py now computes B_n=<p_n,A_384U_0> for n=0,...,111 and completes the terms of diagonal 0 of (69).

For the disjoint pieces and the errors e_j of (71), the global source error satisfies ||V−Vtilde||²≤Σ_j e_j². Since ||p_n||_(L²(0,T))=1, the error of each moment satisfies

    |B_n−Btilde_n|≤sqrt(Σ_j e_j²).                            (78)

The program integrates the products of the approximants with the normalized polynomials, includes the coefficient intervals and adds the global remainder of (78). The sum of absolute values of the coefficients of p_n is not used for this bound. With the same source and the same corrector, verified by their fingerprints, it reconstructs

    Γ_tail,00=G_V,00−Σ_{n=0}^{95}B_n²,
    S_X,K,00=Σ_{n=0}^{111}U_(n,0)B_n,
    Δ_(k,0)=Σ_{n=0}^{111}W_(n,k)B_n,
    G_U,00=Σ_{n=0}^{111}U_(n,0)².
The dimensions are fixed explicitly to N95, M111, 112 coefficients and 16 high columns to prevent silent zip truncations or use of a wrong weight. The coefficients U,W are reconstructed with the exact enclosed moments; no floating-point values of S or Δ are imported.

The file real_residual_diagonal.json encloses:

- G_V,00≈0.443886963801320938;
- Γ_tail,00≈0.0028131096599416285;
- S_X,K,00≈0.261998862294024588;
- ||Δ_(·,0)||²≈2.21470841823e−26;
- G_U,00≈1.00054172185354570.

Including all terms of (69), its diagonal 0 is enclosed in

    M_00∈[0.2519673132466727407969558456690957078273489705956560402666800294610096850934486402921789940958736086707056292619032 ±1.87e−116]
        >1/4.                                                (79)

M here designates only the matrix of the sufficient criterion (69). It is not the full matrix of the operator and M≥0 is not claimed from a diagonal.

### Consequence on an infinite subspace

The transfer already proved gives S_exact,00≥M_00>1/4 for the true operator A, not only for A_384. Let e_1 be the first low column, H the true high compression and c_1=Π_high A e_1. For any complex α and v in the high form domain,

    a_T(αe_1+v)
      =a_T(v+αH^(−1)c_1)+S_exact,00|α|²
      ≥(1/8)||v+αH^(−1)c_1||²+(1/4)|α|².                    (80)

The source c_1 belongs to L²; by coercivity, H^(−1)c_1 belongs to the operator domain and therefore to the form domain. The inequality establishes strict positivity on span{e_1}⊕H_high, a subspace of codimension 94 inside the primitive even sector. 1/8 is not interpreted as a bound in the original norm of αe_1+v: the triangular change of (80) must be accounted for that.

This result validates an infinite part of the construction at T=4/5, a window whose positivity was already known from other certificates. It does not enlarge the proved interval nor solve the sign of the other 94 low directions and their couplings. The full matrix of (69) and the global goal remain OPEN.

## Principal block with full couplings

Status: formulation and code checked; 8×8 block enclosed and certified positive by interval LDL. Independent verification of the eight leading principal minors by arb_mat.det: PASS_SYLVESTER, without reusing the LDL recurrence. Antecedent (79)-(80): a single low direction. arb_residual_block.py selects the first eight columns of the SAME frozen corrector, keeps the 16 high columns and the complement H_high defined by the 95 low directions. It does not solve another system nor modify the carrier when reducing the verified block.

The generation of sources reuses polynomial_source.pieces and formula (70) through an Arb context adapter. The intervals U,W reconstructed with iv400 are transferred by endpoint containment to Arb500dps. The constants are evaluated in the current context and the contact branches still use certified comparisons. All coefficients of the native source 0 are checked against the previously archived intervals; the overlap is an implementation check, not the basis of the bound.

For each piece all sources are prepared. Their cross products and the 112 moments of each column are integrated. With global errors e_i=sqrt(Σ_pieces e_(i,piece)²) and norms of the approximants computed before the remainders, each Gram entry is widened by e_i n_j+n_i e_j+e_i e_j. Each B_(n,i) is widened by e_i, using ||p_n||=1. For I={0,...,7},

    Γ_I=G_V,I−B_(0:95,I)^t B_(0:95,I),
    S_I=(U_I^t B_I+B_I^t U_I)/2,
    Δ_I=W^t B_I,  G_U,I=U_I^t U_I.                           (81)

The average of the two contractions of S is valid because A_384 is self-adjoint and both enclose the same exact entry. ALL entries of (69) in I are formed, including the mixed terms of Γ,Δ^tΔ,G_U,G_V.

The LDL factorization is carried out with balls and without pivoting. Each pivot must have a strictly positive lower endpoint before being used as a denominator. If this cannot be established, the output is LDL_INDETERMINATE and no negativity is inferred. The positive certification of the block M_I gives, for C_Iα=Π_high AΣ_i α_i e_(i+1),

    a_T(Σ_{i∈I}α_i e_(i+1)+v)
      ≥(1/8)||v+H^(−1)C_Iα||²+α* M_I α.                     (82)

Strict positivity is obtained on span{e_1,...,e_8}⊕H_high, of codimension 87 inside the primitive even sector. The LDL pivots are not interpreted as eigenvalues nor as L²-norm bounds on that subspace. The run is parametrized in the number of columns up to 95, but running a block of 8 does not certify the other sizes.

For the following runs arb_moment_convolution.py was added: if f_s has degree d, the convolution of its reversed coefficients with the table μ_(s,0),...,μ_(s,d+111) has at position d+k the value Σ_j f_(s,j)μ_(s,j+k). Summing the three components gives g_k=∫t^k Ftilde; then <p_n,Ftilde> is the contraction of g_k with the coefficients of the local p_n. The Jacobian and the remainders are kept. The identity was checked and passed 17 analytic moments, including both logarithms, and the null case. The 8×8 run already started continues with the previous direct contraction; it was not restarted to apply this optimization. Both associations enclose the same integral, although their widths may vary.

Result of the direct run: POSITIVE_PRINCIPAL_BLOCK, 451.30s. The eight interval pivots are approximately 0.2519673132, 0.0934374943, 0.0447207476, 0.00776144705, 0.1100067499, 0.0667125756, 0.0177444232, 0.1495851184; all their lower endpoints are positive. The radii of the pivots are smaller than 8e−108. real_residual_block_even_8.json keeps the full enclosed matrix, the moments, Gram, errors and corrector fingerprint. This run used direct polynomial products for the moments, before the optimization by reversed convolution. The block of 8 does not change the situation of the other 87 even low directions nor of the 95 odd ones, and does not enlarge the window T=4/5.

The independent check saved real_residual_block_even_8_minors.json with matrix and corrector fingerprints, verified symmetry and eight positive minors. The determinant of order 8 is 1.59182184006199695...e−10, with radius<1.74e−117. This second verification certifies positivity of the enclosed matrix; it was not an independent reintegration of the eight sources.

## Native matrix contraction and run of the full even sector

Status: algebraic reorganization and code checked; analytic test reproduced independently. 95×95 run started, no sign result yet. arb_native_gram.py extends the reversed convolution to the three test types t^k L_s. For each source j it prepares

    Y_(s,k),j=∫_0^1 t^k L_s(t) Ftilde_j(t)dt,
    Gtilde=d C^tY,
    Btilde=P_local Y_(s=0,k≤111).                            (83)

In the last expression the program also includes the physical factor d=b−a. The coefficients P_local are those of the normalized polynomials composed with the affine transformation of the piece. The moments of Y require only the six products of logarithms already treated in (65). The number of polynomial rows is enlarged when needed to cover both sources and tests, including empty components.

The two matrix products are run with arb_mat; then exactly the same error budgets and refined norm are applied. The mathematical matrix that must satisfy (69) is not changed. The module test verifies a 3×3 Gram of logarithms and a 2×3 matrix of polynomial moments against known values, with independent reproduction.

arb_residual_block.py --columns95 was started for the 95 even low directions of the same corrector. The run keeps all 16 high corrector directions, the 112 moments and the infinite complement. If all pivots of the criterion turn out positive, it will cover the full primitive even sector at T=4/5; until that result is obtained it is not taken as proved. The odd sector and positivity for all T are separate obligations.

The program checks the 64 entries of the principal block 8 against the previously certified intervals and preserves that file when writing new results. That overlap verifies consistency between implementations; it does not replace the LDL proof in 95 dimensions. The 95 run is still active when recording this step.

### Conditional audit of the closure of the even sector

The independent check verified that, IF the block M95 of (69) is positive definite, no other density hypothesis remains to conclude positivity on the full primitive even sector. The decomposition E⊕H_high preserves the form domain because the 95 columns of E belong to the operator domain. The high form is closed and H≥1/8; C=Π_high AE has L² columns, and L=H^(−1)C is bounded from the finite space of low coordinates.

Besides pointwise positivity, a uniform ground value would be obtained. With s=λ_min(M95)>0, F=Ex+v and w=v+Lx,

    a_T(F)≥(1/8)||w||²+s||x||²,
    ||F||²≤2||w||²+(||E||²+2||L||²)||x||²,
    λ_par≥min{1/16,s/(||E||²+2||L||²)}>0.                    (84)

This consequence remains CONDITIONAL until test 95 finishes. It does not yet provide a numerical value of λ_par, since it requires enclosing s and the indicated norms. It proves neither the odd sector nor positivity for other windows.

### Preparation of the odd sector during the even run

The verifier now accepts --parity even/odd, with even as the default value. The routing of corrector, fingerprints, antecedents and reports by parity was checked independently. The even run already active was neither restarted nor changed in in-memory code; the full odd run has not yet been launched.

For the odd sector, the embedding F(t)=sgn(t)f(|t|)/sqrt2 is isometric and primitivity is equivalent to the moment with sinh(x/2). stable_split reconstructs those bases via the certified series and frozen_corrector_odd_160.json is used exclusively. The assembler receives σ=−1: the archimedean reflection has f(x)+f(y) and the reflected contact enters with positive sign. The term 2Σ_j|α_j(f)|² of (29) is already incorporated in that reflected action; adding it separately would count it twice.

The constants of (49),(56),(67),(69) cover both parities. The residual weight is not changed and integrated data of the even sector are not reused for the odd one. The comparison with real_source_even_0.json.gz is run only in even parity. This preparation is not an odd numerical certificate: it remains to run it and verify its pivots.

## Verification by congruence and quantitative uniform bound

While the 95 run continues, an independent verification of the LDL was prepared. verify_residual_congruence.py proposes a preconditioner P via Cholesky at 80dps of the midpoint, but that stage is only heuristic. It freezes each stored entry of P as an exact dyadic, checks zero radius in Arb500 and computes B=PMP^t with intervals. If

    δ=min_i{lower(B_ii)−Σ_(j≠i)upper|B_ij|}>0,

Gershgorin establishes B>0. This forces P to be invertible and by congruence establishes M>0, without requiring the approximate Cholesky or its inverse to be exact. A heuristic or dominance failure is recorded as indeterminate. The report keeps P, margins and hash of M. The file 8 passed this verification and it was reproduced independently; it has not yet been run on 95.

The same congruence gives s=δ/||P||_F²≤λ_min(M). For a block of r certified directions, write X_r for its columns, g=tr G_V,r and y=||X_r||_F. Using E⊥W, ||E||²≤27/20, ||W||²≤1+ηbar, ηbar=10^(−370), and ξ≤10^(−35),

    ||U_r||²≤27/20+(1+ηbar)y²,
    ||H^(−1)C_r||≤ell
      =sqrt(1+ηbar)y
         +8[sqrt(g)+ξ sqrt(27/20+(1+ηbar)y²)],
    a_T(F)≥c_r||F||² on span(e_1,...,e_r)⊕H_high,
    c_r=min{1/16,s/(27/20+2ell²)}>0.                         (85)

The bound on ell comes from H^(−1)C_r=WX_r+H^(−1)R_res, with R_res=Π_high A U_r, and ||R_res||≤sqrt(g)+ξ||U_r||. It requires neither computing AW nor building the infinite inverse. For r95 it would cover the full even sector; for r8 it only covers the already certified subspace of codimension 87.

certify_uniform_subspace_bound.py reproduces the congruence using the saved P and computes (85) with conservative endpoints, verifying hashes, symmetry, sizes, T4/5 and K384. On the block of 8 it obtained s>6.42687939e−7, ell<36.086398365 and c_8>2.46636882e−10. It is a bound in the ORIGINAL L² norm on that restricted subspace; it is not a bound of λ_A on the whole carrier and must not be compared as such with the ground value of the full form. The reports are real_residual_block_even_8_congruence.json and real_residual_block_even_8_uniform_bound.json.

certify_uniform_subspace_bound.py was also reproduced independently: PASS_UNIFORM_BOUND, with the same bound c8 and restricted scope. The active 95 computation was neither repeated nor restarted.

### Active full runs

The even run finished assembling its 95 sources and continues integrating the full block; it has not yet produced an LDL95 result. After checking resource availability, the odd 95 run was started in parallel with --parity odd and reduced CPU priority via nice. It uses distinct files and the already frozen odd corrector; it neither modifies nor restarts the even run. Neither of the two full blocks is declared certified while their results do not exist and are not verified.

### Correspondence with the current definitions of Paper 46

eq:symbol, eq:form, the definition of lamA and item (o) of thm:parityschur in the current main.tex file were cross-checked, without modifying it. The contact coefficient is v_n=2Λ(n)/sqrt(n), the two constraints are ∫F exp(±t/2)=0 and the norm of λ_A is the L² norm used here. The embeddings with factor 1/sqrt2 preserve that norm.

In (84)-(85), λ_par means the ground value of the PRIMITIVE sector with the primes included, i.e. λ_A^par of the paper, not the archimedean ground value without primes that uses a similar notation in another section. If both full certificates give constants c_even,c_odd>0, the orthogonal decomposition for the norm and the form gives λ_A(4/5)≥min(c_even,c_odd). It remains a conditional conclusion while either of the two certificates is missing; it does not claim positivity of the full form W_T outside the primitive carrier nor for larger windows.


## Simultaneous assembly of the polynomial sources

Status: identity and code checked independently; implementation checks PASS. It is a reorganization of (70), not a new sign mechanism. For f(x)=Σ_m F_m x^m and r_K(u)=Σ_k c_k u^k, define

    H_(j,m)=T^(m+j+1)/(m+j+1),
    L_(l,j)=[(-1)^l+σ] c_(l+j) binom(l+j,l), l+j≤K,
    Q_(n,m)=2 c_k m! k!/(m+k+1)!, k=n−m−1 odd, 1≤k≤K.

The other entries are zero. The regular action of (70) is

    integral_regular(f)=[embed(LH)+Q] F.                    (86)

In the source A_K f it enters with negative sign. The exact matrices of D_T, of the reflected division and of the constant of (64) are added. Each shift uses S_(j,m)=binom(m,j) b^(m−j) a^j for f(b+ax), with certified activity per piece and zero extension in contacts. The three logarithmic multipliers are kept separate. Thus all columns share the archimedean matrix and the shift matrices.

arb_source_batch.py implements this association with Arb. check_arb_source_batch.py compares the real even column 0, of degree 111 and kernel 384, with the preserved file: 4160 compatible coefficients, maximal radius<9.1e−278, 17.67s of assembly. arb_source_batch_check.json keeps fingerprints and scope. The formulas were audited and a two-column test, degree 4/kernel 8, both parities and five pieces, was reproduced independently: 580 comparisons PASS, radii<1e−65. The overlap is an implementation control; it does not by itself prove equality nor certify a new Gram.

The 95 runs already active continue with their original assembler; they were not restarted. The new module remains available for later runs and has not yet been connected to the main verifier. At the time of recording, the even run had integrated pieces 0,1,2 and the odd one had assembled its 95 sources and integrated piece 0. There is still no complete sign result.

The global obligation does not reduce to the cost of the assembly: one needs to build correctors and prove, for each T, the matrix domination of the residue in (69), with constants adapted to that window. The constants 1/8, 1783/500 and the degrees of this certificate belong to T=4/5; they are not transferred to other windows without proof. This optimization does not fulfill that obligation nor does it yet identify the required arithmetic cancellation.


## Approximation of the kernel in any finite window

Status: PROVED as an auxiliary lemma, identity and bounds checked independently. Antecedent: (60)-(63) uses a local Taylor expansion for T=4/5. This extension removes the restriction of the radius of that expansion; it does not constitute a new sign source. No novelty of the Bernstein procedure is claimed.

For u≥0 define, including the continuations at zero,

    B(u)=2∫_0^1 exp(−2ut)dt,
    N(u)=∫_0^1∫_(1/2)^(2t) exp(−us)ds dt,
    r(u)=N(u)/B(u).                                         (87)

The inner integral is oriented when 2t<1/2. For u>0, N=(exp(−u/2)−B/2)/u, so (87) is exactly H0(u)−1/(2u). At zero, B(0)=2,N(0)=1/2 and r(0)=1/4.

On 0≤u≤2T, the parameters s of the integral lie in [0,2], the length of each interval is ≤3/2 and

    B≥2exp(−4T), |B'|≤2, |N|≤3/2, |N'|≤3,
    |r'|≤L_T:=(3/2)exp(4T)+(3/4)exp(8T).                    (88)

The first four bounds come directly from the integrals; the last applies the quotient rule. Let n≥1 and q_j approximations to r(2Tj/n) with |q_j−r(2Tj/n)|≤ε. Set x=u/(2T) and

    r_n(u)=Σ_(j=0)^n q_j binom(n,j)x^j(1−x)^(n−j).

If J has binomial(n,x) distribution, positivity and unit sum of the weights, Cauchy–Schwarz and Var(J/n)=x(1−x)/n give

    |r_n(u)−r(u)|≤ε+L_T·2T E|J/n−x|
                  ≤ε+L_T T/√n=:δ_n.                        (89)

This is a proof of the bound, not a numerical convergence hypothesis. The nodes can be enclosed via exponentials, using the exact value at zero. If T is rational and the q_j rational, r_n has rational coefficients in u. For arbitrary real T a rational R larger than T can be chosen, the polynomial built on [0,2R] and restricted; it is not claimed that a normalization by an irrational T preserves rational physical coefficients.

Define s_n(u)=−∫_0^u r_n(v)dv and replace kernel and tail jointly as in (62). The difference between the exact and approximate operator has exclusively the kernel

    −[(r−r_n)(|x−y|)+σ(r−r_n)(x+y)],
    ||A_T−A_(T,n)||≤2Tδ_n.                                 (90)

The bound holds in both parities by Schur, since x,y∈[0,T]. The difference is bounded and symmetric and does not change the domain of the original singular operator. The arithmetic contacts and the two moments are not approximated in this step.

To obtain an operator error ≤ζ>0 it suffices to choose ε≤ζ/(4T) and n≥(4L_T T²/ζ)². For rational coefficients in a real window use R>T and those same choices with R, which gives a bound valid also at T. The cost can be enormous: it is an explicit existence construction with controlled error, not an implementation recommendation against piecewise Taylor or other more efficient approximations.

Limited consequence: the radius of convergence of the local Taylor expansion does not prevent defining residual certificates of arbitrary precision in other windows. A corrector still has to be built and the sign of the corresponding matrix criterion proved. Making δ_n small does not prove that inequality, nor guarantees that a given corrector satisfies it; the falsifiers also admit this approximation. No new positive window nor a global proof has been obtained.


### Optional integration of the shared assembler

The verifier now accepts --source-method batch; direct remains the default value. Both branches use the same columns and lead to the same integration and criterion. The routing was checked independently. The reports identify source_method, batch files have a separate name and new runs preserve existing files by means of runN suffixes. The 95 processes already active did not change. A full check of one even column with batch was started, still without result at the time of recording; no new certificate is attributed to this preparation.


The batch full check of one column finished in 83.06s: POSITIVE_PRINCIPAL_BLOCK, criterion00=0.2519673132466727407969... with radius<1.91e−116 and lower endpoint>1/4. real_residual_block_even_1_batch.json keeps the result. 114 overlaps with the previous certificate 8 were checked: 112 moments, Gram00 and criterion00, with equality of the corrector fingerprint. real_residual_block_even_1_batch_crosscheck.json records PASS_END_TO_END_CROSSCHECK and both fingerprints. It is an implementation validation of the same already certified direction, not a new subspace or positivity window.


## Coercive complement and residual weights for every fixed T

Status: PROVED as an auxiliary extension of (38)-(58), checked independently. It is not a new sign mechanism. Fix T>0, γ>0 and a parity, with h=cosh(x/2) or sinh(x/2). Keep κ_T,c_T of (38), including all contacts of that window. Choose an integer N≥1 satisfying

    δ_N=T exp(T)(T/2)^(2N+2)/[((N+1)!)²||h||²]≤1/2,
    κ_T H_(N+1)≥2|c_T|+2γ.                                (91)

The selection terminates: for fixed T, δ_N→0 by the factorial and H_(N+1)→∞, while κ_T>0 and c_T is finite. N can be increased until both inequalities are verified with conservative bounds; the sign of the form is not used to choose it. The norms of h are those of (49) and are strictly positive for T>0.

Generalize (47),(50) to this N: E=span(e_1,...,e_N), h_low=Σ_(0≤n≤N)α_n p_n and w_k=p_k−α_k h_low/||h_low||² for k≥N+1. Since α_0>0 and the Taylor approximation gives ε≤δ_N, set eta_bar=δ_N/(1−δ_N)≤1. Then

    ||W∞||²≤1+eta_bar≤2,
    a_T(W∞z)≥Σ_(k≥N+1)d_k|z_k|²,
    d_k=κ_T H_k+c_T−|c_T|eta_bar,
    d_(N+1)≥2γ.                                           (92)

The modal comparison comes from (39); the low norm term only costs |c_T|eta_bar. The last inequality uses (91) and |c_T|+c_T≥0. Hence the operator H of the form restricted to the exact high complement satisfies H≥γ in the physical norm. This preserves exactly the moment of the parity and, through the corresponding embedding, the two original moments.

For any M≥N+1 and any finite corrector Z=W_M X, define C=Π_high AE, R=C−HZ, Δ=W_M*R and S_X=P−D*X−X*D+X*KX as before. The same variational proof of (57)-(58) gives

    S_exact=S_X−R*H^(-1)R,
    R*H^(-1)R≤rho R*R+tau Δ*Δ,
    rho=(1+eta_bar)/d_(M+1),
    tau=1/d_(N+1)−1/d_(M+1)≥0.                            (93)

The primitive polynomial columns are in the operator domain by the same action with logarithmic endpoints and finitely many contacts; no new spectral condition appears. The denominator in (93) is positive by (92). It is not presupposed that X is an exact solution of the finite system.

Thus the sufficient criterion S_X−rho R*R−tau Δ*Δ≥0 is available in each finite window. Together with (87)-(90), the existence of a coercive tail and of an arbitrarily precise approximation of the kernel at any T is settled. Finding X and proving the sign of that criterion for each T is not settled. Nor is convergence of the residue as M increases, termination of the positivity test or a global positive identity claimed. These reduction tools remain applicable to falsifier forms with finitely many contacts; they do not by themselves provide the missing arithmetic distinction.


## Full certificate of the even sector at T=4/5

Status: interval computation 95 finished, verified by congruence and reproduced independently at the stage of matrix certification and uniform bound. real_residual_block_even_95.json finished in 3666.00s with 95 strictly positive LDL pivots and overlap of the 64 entries of the previous block 8. Its SHA256 is 91bc989abd773bdb6b61f8a23ec30730650e2b3e2d938a59d8ed43c87174a7ab. The run started before the parity field was added to the report; the even parity is identified by the frozen corrector and its fingerprint, not by an inference from the name alone.

verify_residual_congruence.py produced PASS_CONGRUENCE in dimension 95. The exact dyadic preconditioner and the dominance margins are in real_residual_block_even_95_congruence.json. certify_uniform_subspace_bound.py reproduced the congruence and applied (85), giving PASS_UNIFORM_BOUND, scope full parity:

    s>4.79542948e−12,
    ell<284.400740,
    a_(4/5)(F)≥2.96437025e−17 ||F||²
      for every F in the primitive even sector.                 (94)

The last inequality includes all 95 low directions and the infinite complement, via (84)-(85); it does not interpret the pivots as eigenvalues. real_residual_block_even_95_uniform_bound.json keeps the bounds and fingerprints. The rounding of (94) is downward with respect to the enclosure obtained.

This result completes the even residual certificate in a window already known to be positive by other means. It does not enlarge the proved window nor yet establish the odd sector, whose 95 run is still active. It does not prove global positivity nor provide the arithmetic construction rule for all T.

PASS_CONGRUENCE and PASS_UNIFORM_BOUND on the file 95 were reproduced independently, fingerprints/dimensions were verified and the scope of (94) on the whole primitive even form domain was confirmed. The 95 sources were not reintegrated and neither reports nor the odd process were modified.


## Closure of the local certificate over both parities

Status: both 95 blocks positive, verified by congruence; independent check of both sectors and their combination completed. The odd run finished in 3661.78s with 95 positive LDL pivots. real_residual_block_odd_95.json has SHA256 288085f3be1a57c3b496a5cb27416fb8102b2f101418a61ba32427d9becd0fd7 and odd corrector fingerprint 130a68519fe65899ab5da92d2817de538d8b068ab908a23f25145d63ed1a9d80.

The congruence and the uniform bound (85) gave PASS_CONGRUENCE and PASS_UNIFORM_BOUND:

    s_odd>1.05649760e−9, ell_odd<288.587238,
    a_(4/5)(F_odd)≥6.34279623e−15 ||F_odd||².                (95)

For primitive F, F_even and F_odd satisfy their respective hyperbolic moments; the reflection commutes with the form. By orthogonality of norm and form, (94)-(95) imply

    a_(4/5)(F)≥2.96437025e−17 ||F||²,
    λ_A(4/5)≥2.96437025e−17>0.                              (96)

Both congruences and bounds were reproduced before saving real_residual_full_T4_5_certificate.json, PASS_BOTH_PARITIES. The report includes the two fingerprint chains, the full parity scope of each and the joint bound rounded downward. The combination uses the previous analytic decomposition, not an additional test on isolated vectors.

The residual certificate of BUILD083 on the WHOLE primitive domain at T=4/5 is closed. No new window was obtained and the known ground value was not improved: the bound is conservative. There are no pending 95 computations. Positivity for all T and the arithmetic design that forces (93) remain OPEN; (96) does not authorize extrapolating the corrector or its constants to larger windows.

The odd congruence and bound were reproduced independently, dimension/parity/fingerprints were verified and (96) was confirmed by orthogonality of the reflection. The check was not an independent reintegration of sources.


## Minimal-residual corrector and exact update

Status: PROVED as an auxiliary design lemma, checked independently. Antecedents: correctors (43)-(46),(93), without monotonicity of the L² residue, and RAT-DD least squares recorded in the master index (lines 25754-55 at the time of consultation). No novelty is attributed to least squares, nor is it presented as a new route to the sign. No other numerical campaign was run.

With H≥γ>0 on the high complement, W_M the independent high columns and C=Π_high AE, define

    Y_M=H W_M, G_M=Y_M*Y_M,
    X_M=G_M^(-1)Y_M*C, Z_M=W_M X_M,
    R_M=C−H Z_M=(I−P_range(Y_M))C.                         (97)

The columns of W_M are in Dom(H), so Y_M belongs to L². Moreover G_M≥γ²W_M*W_M>0, justifying the finite inverse without using positivity of the full form. The ranges are nested and their orthogonal projectors satisfy P_(M+1)≥P_M. It follows that

    R_(M+1)*R_(M+1)≤R_M*R_M.                              (98)

The inequality holds simultaneously in all low directions, not only for the trace. There is also an explicit update. Set w=w_(M+1), y=Hw,

    a=G_M^(-1)Y_M*y, q=y−Y_M a,
    Z_(M+1)=Z_M+(w−W_M a)(q*C)/||q||²,
    R_(M+1)=R_M−q(q*R_M)/||q||²,
    R_M*R_M−R_(M+1)*R_(M+1)
       =R_M*q q*R_M/||q||²≥0.                            (99)

Since H is injective and w does not belong to span(W_M), q≠0. The orthogonality q⊥range(Y_M) gives q*C=q*R_M and proves the formulas by orthogonal projection. The choice uses the images of the high operator and a finite Gram; it does not invert the full form nor assume the sign of the Schur complement.

What is solved: when enlarging the corrector space, the L² residue of THIS choice does not grow. What is not solved: there is no proof here of density of the union range(Y_M), nor convergence R_M→0, nor control of the conditioning of G_M. Moreover Y_M*R_M=0 is not equivalent to W_M*R_M=0: the defect Δ of (93) does not vanish as in energetic Galerkin. S_X also changes, so (98) does NOT imply monotonicity or positivity of the full criterion. The global arithmetic inequality is still missing. The frozen correctors of the local certificate were neither replaced nor reinterpreted as solutions of (97).


## Joint optimization of the scalar certificate

Status: PROVED as an auxiliary repair of design (97)-(99), checked independently. Antecedent: there only the residual Gram decreases, without monotonicity of the full criterion. The scalar criterion of (46) is now optimized; no novelty is attributed to completing squares and no new arithmetic sign source is claimed.

Fix the low carrier E, its complement H≥γ>0 and a number r>1/γ. For Z=WX, Y=HW, K=W*HW, D=W*C, set

    R=C−HZ,
    J(X)=S_X−rR*R,
    G=rY*Y−K, B=rY*C−D.                                  (100)

One has Y*Y≥γK and K>0, hence G≥(rγ−1)K>0. This inequality only requires W⊂Dom(H); Y*Y is an L² Gram and does not require the columns to be in Dom(H²). The exact expansion is

    J(X)=P−rC*C+B*X+X*B−X*GX,
    X_opt=G^(-1)B,
    J_opt=P−rC*C+B*G^(-1)B,
    J_opt−J(X)=(X−X_opt)*G(X−X_opt)≥0.                    (101)

The optimum is simultaneous in Loewner order for all low coordinates, not only a trace maximum. If W_M⊂W_(M+1), keeping THE SAME E,H and r, the previous corrector is included among the new admissible ones and (101) implies

    J_opt,M≤J_opt,M+1≤S_Schur,
    S_Schur−J(X)=R*(rI−H^(-1))R≥0.                        (102)

The last identity comes from S_Schur=S_X−R*H^(-1)R. H^(-1) appears only in the proof of the error; the constructive formula (101) uses images HW and finite matrices, without inverting the full form nor assuming its sign.

This solves the lack of joint monotonicity of the SCALAR certificate: enlarging the optimized corrector does not worsen its lower bound. It does not prove that J_opt reaches zero, that R tends to zero nor that the limit is S_Schur. Nor does it allow changing N,E or r between steps while keeping monotonicity without a new proof. It is not compared as superior to the MODAL criterion (69), which has additional information and was the one used in the local certificates. Frozen correctors were not replaced and no other computational campaign was launched.

Explicit remaining obligation: obtain an arithmetic bound forcing P−rC*C+B*G^(-1)B≥0 for a constructive choice of corrector space at each T, or control its limit and its sign by another identity. Monotonicity alone admits negative limits and also holds for the falsifiers; it does not close the global goal.


## Exact gain per corrector direction

Status: PROVED, checked independently, as an update of (101)-(102). Keep H,C,P,r and the low carrier fixed. Use the inner product conjugate-linear in the first entry and the positive metric

    g(u,v)=r<Hu,Hv>−<u,Hv>, u,v∈Dom(H).

Let Z_old be the optimum over span(W), G=g(W,W), and choose w∈Dom(H) outside span(W). Define

    a=G^(-1)g(W,w), q=w−Wa, d=g(q,q)>0,
    b=r(Hq)*C−q*C,
    Z_new=Z_old+q b/d,
    J_new=J_old+b*b/d.                                    (103)

The orthogonalization gives g(W,q)=0 and q≠0. Writing a corrector in span(W,q), the quadratic term of (101) separates between both components; completing the square in the new row gives (103). The new choice is the joint optimum, not a heuristic that keeps the old coefficients for convenience.

Moreover, R_old=C−HZ_old satisfies exactly

    b=(rHq−q)*R_old,
    x*(J_new−J_old)x=|bx|²/d.                              (104)

The first identity uses g(q,Z_old)=0. This identifies the concrete detector of a useful direction: bx≠0 produces strict improvement of the criterion at x. It does not imply that all low directions improve strictly with a single q; the gain has rank at most one.

Starting from Z_0=0 and successively orthogonalizing independent candidates in g, one obtains the finite identity

    J_m=P−rC*C+Σ_(j=1)^m b_j*b_j/d_j.                     (105)

The procedure uses Hq, without applying H² to q. Convergence of the infinite sum is not assumed. The arithmetic design task is expressed as choosing candidates whose joint contributions dominate rC*C−P. Writing that obligation does not prove it: the initial term may be indefinite, the increments may leave directions uncompensated and the falsifiers admit the same identities. No arithmetic rule ensuring that domination for all T has yet been found. The local certificates are not altered and no novelty of the Gram algebra is claimed.


## Arithmetic seeds with jumps for the corrector

Status: INCOMPLETE CANDIDATE; domain and development gate checked independently. Antecedents: BUILD079, which discards extracting directly the square of the causal Möbius operator, and (103)-(105), which allow enriching an optimized corrector. The concrete change is to use that operator to produce trial directions, without requiring domination of the discarded square. It is presented neither as a sign mechanism nor as a proof of a Möbius advantage.

Work on I=(-T,T), with extension by zero. Let p_j be the normalized Legendre polynomial on I, U_l f=1_I f(·−l), and define exactly as in BUILD079

    E_T=Σ_(2≤n<exp(2T)) Λ(n)/(√n log n) U_log n,
    R_T=exp(−E_T)=Σ_(1≤n<exp(2T)) μ(n)/√n U_log n.          (106)

The exponential is a finite polynomial by nilpotency of the delays. The equality of coefficients comes from the formal Euler product and does not require convergence of an infinite series. R_T is not confused with the residue R of (100).

For σ=±1, Π_σ f(t)=[f(t)+σf(−t)]/2; take h_+=cosh(t/2), h_−=sinh(t/2) on I. Let E_σ be the isometric embedding of the previously constructed primitive low space in that parity. The exact high projector, written on the full space, is

    Q_high,σ=Π_σ−h_σ(h_σ*·)/||h_σ||²
                   −E_σ(E_σ*E_σ)^(-1)E_σ*,
    w_j=Q_high,σ R_T p_j.                                 (107)

The two subtracted terms are orthogonal because E_σ is primitive. The first subtraction removes the moment of the parity; the other preserves it. The condition of the other moment holds automatically by parity. All entries of the projectors are explicit integrals of polynomials, exponentials and piecewise functions.

Each R_T p_j is a finite sum of translated polynomials with jumps at the points −T+log n. It is BV and its archimedean action has logarithmic singularities at finitely many points, which belong to L². The projections of (107) only add piecewise smooth functions, with possible irregularities at zero due to the parity embedding and cuts at the endpoints. Hence w_j belongs to Dom(H) of the corresponding high complement; applying H² is not needed.

The constructive rule is to run through j=0,1,..., orthogonalize w_j against the accepted directions in the metric g of (103) and accept only if d_j=g(q_j,q_j)>0. A null or dependent seed is discarded without dividing by zero. With each accepted seed one computes

    b_j=(rHq_j−q_j)*R_old,
    Z_new=Z_old+q_j b_j/d_j,
    J_new=J_old+b_j*b_j/d_j.                              (108)

If starting from a nonempty optimized corrector, that space is kept and enriched; if starting from zero, the telescoping (105) applies. The interior jumps may enlarge the previous finite polynomial space, but independence of all seeds and density in graph norm are not claimed.

The identification of coefficients with μ is lost for generic weights; this only distinguishes an arithmetic identity, it does NOT prove that the remainder has sign exclusively for Λ. The gain (108) remains non-negative for any admissible direction and any falsifier with coercive complement. It remains to prove that these seeds produce a total compensation of rC*C−P for all T, or to find a modification that does. b_j has not yet been evaluated for this family nor claimed to be nonzero. The correctors of the local certificates were not replaced.

## L² density and first genuinely new direction

Status: PROVED as auxiliary properties of (106)-(108), checked independently. They are not proofs of the sign nor of convergence in graph norm. The compressed positive shifts satisfy U_l U_s=U_(l+s), and U_l=0 almost everywhere if l≥2T. By μ*1=δ, the explicit finite inverse is

    D_T^arith=Σ_(1≤n<exp(2T))n^(-1/2)U_log n,
    R_T D_T^arith=D_T^arith R_T=I.                         (109)

Let P_m be the L² projection onto the first m+1 Legendre polynomials on ALL of I. For f in the high complement of parity σ, the finite combination of seeds

    f_m=Q_high,σ R_T P_m D_T^arith f

satisfies

    ||f_m−f||≤||R_T|| ||(I−P_m)D_T^arith f||→0,
    ||R_T||≤Σ_(n<exp(2T))|μ(n)|/√n.                       (110)

The bound follows from the contraction of the high projector and identity (109); convergence uses the L² completeness of Legendre. Thus the seeds densely cover the high complement in L². This topology is not exchanged for the graph norm of H: (110) does not control Hf_m nor prove that the residue of (108) tends to zero.

There is moreover an explicit new direction in the already certified window. For T=4/5 and p_0=1/√(2T), the only nontrivial arithmetic jumps of R_Tp_0 are those of n=2,3, since μ(4)=0. At t_2=log2−T the jump before separating parity is −1/(2√T). No reflected jump coincides with it: such a coincidence would require nm=exp(2T), impossible because

    4 < 609427507/123046875 < exp(8/5)
      < 115187041703/23255859375 < 5.

These rational bounds come from truncating the exponential series at degree 8 and bounding the tail by its first term divided by 1−(8/5)/10. Hence, in both parities, the seed w_0 of (107) keeps the jump

    jump_(t_2)(w_0)=−1/(4√T)=−√5/8.                      (111)

The functions subtracted by the high projection are smooth NEAR t_2≠0; global smoothness of their extensions at zero is not assumed. No combination of the previous finite polynomial high space has that interior jump. Consequently w_0 does not belong to that space and its orthogonalization in g has d>0. This establishes that the enrichment adds an admissible direction, not that the corresponding row b is nonzero nor that its gain is sufficient. The computation or sign of that gain and the control in graph norm remain open.


## Operator core of the seeds and convergence of the corrector

Status: PROVED as an auxiliary result, with independent check of commutator, domains, operator core and convergence. Antecedents: logarithmic transmission by Carleman in P121_DYADIC_RADICAL_BOOTSTRAP, Lemma 2.2 (master index), estimates (15)-(22) and L² density (110). No novelty of the Carleman ingredient is claimed. The topology required by the corrector is settled here, without using or concluding the global sign.

Let A0 be the self-adjoint archimedean operator on the line. By its explicit symbol, its graph norm is equivalent to

    ||f||_log²=∫[1+log²(2+|ξ|)]|fhat(ξ)|²dξ.              (112)

For χ=1_I, the cross block of the operator has kernel −H0(|x−y|). One verifies for u>0

    uH0(u)≤(1/2+u)exp(−u/2)≤1/2+2/e<2.

Each endpoint of the interval reduces by translation/reflection to an operator dominated by 2/(s+t), s,t>0. Schur with weight s^(−1/2), using ∫_0^∞t^(−1/2)/(s+t)dt=πs^(−1/2), bounds its norm by 2π. Summing the two endpoints, the cross block and the commutator are bounded by 4π.

For f Schwartz, χf is compact BV and belongs to H^s for 0<s<1/2, hence to Dom(A0). The commutator identity computed through the kernel gives

    ||[A0,χ]f||≤4π||f||.                                 (113)

Extending from the Schwartz core in graph norm and using that A0 is closed proves χDom(A0)⊂Dom(A0) and the same identity on the whole domain. To identify the compression, subtract from A0 the bounded self-adjoint operator formed by its two cross blocks. The result is self-adjoint on Dom(A0), commutes with χ and decomposes as a direct sum. Its interior block coincides with the compression of the archimedean form. Hence the domain of that block is exactly the functions of Dom(A0) supported in I, with graph norm equivalent to (112) applied to the extension by zero. The contacts are a finite sum of bounded operators for each T and do not change that domain.

Polynomials on I, extended by zero, constitute an operator core of this compression. To prove it, first contract the support of f∈Dom(A0) toward the interior by unitary dilations. These converge strongly in (112): their norms are uniformly bounded for factors close to 1, and convergence is checked first on Schwartz and extended by density. Then mollifying with support smaller than the available margin approximates in (112) by compactly supported C∞ functions in I. Each function so obtained is approximated in C¹ of the closed interval by polynomials (approximate its derivative uniformly and integrate). The extension by zero of the error has H^s norm, s<1/2, controlled by its C¹ norm; this is obtained by separating the fractional seminorm inside I and the boundary term, whose integral d(x,∂I)^(−2s) is finite. Finally H^s controls (112). This is existence of polynomial approximants; convergence in graph norm of the orthogonal projections P_m used in (110) is NOT claimed.

Translations of the line commute with A0, so U_l=χτ_lχ is bounded in graph norm by (113). The finite sums R_T and D_T^arith are then bounded mutually inverse operators in that norm. Transporting the polynomial core through R_T gives an operator core formed by span{R_Tp_j}.

Reflection preserves Dom(A0). The finite projections onto h_σ and E_σ also preserve the domain, and their commutators with the compressed operator are bounded: for a column v∈Dom(A), the coefficients of the cross terms are written via Av∈L². The same block argument identifies the domain of the high operator H with the intersection of the compressed domain and the high complement. Applying Q_high,σ to the previous approximants proves

    span{w_j:j≥0} is an operator core of H.            (114)

Thus (110) is improved to density in graph norm for finite combinations of seeds, without claiming rates or good numerical conditioning. Discarding exact dependencies via (108) does not change their span.

For fixed r>1/γ, the metric used by the corrector satisfies

    (r−1/γ)||Hu||²≤g(u,u)≤r||Hu||².                       (115)

One uses <u,Hu>≤||Hu||²/γ. Since H≥γ, this metric is equivalent to the graph norm. The columns Z_*=H^(-1)C belong to Dom(H), and (114) allows approximating them in g by combinations of the seeds. The identity (101)-(102) identifies the finite optimum as the projection of Z_* in that metric; hence

    ||H(Z_opt,m−Z_*)||→0, ||R_m||→0,
    J_opt,m increases toward S_Schur in matrix norm.      (116)

The number of low columns is finite for each T, so convergence by columns implies that of the Grams and matrices. No rate uniform in T is obtained. In particular, IF S_Schur>0 in a window, there is a finite step with J_opt,m>0. That premise is still the sign to be proved; (116) does NOT allow deducing it. If the limit has a negative direction, monotonicity does not repair it; if it is only semidefinite, positivity at any finite step is not guaranteed. The global design is still pending, now without the analytic density gap of the corrector.

The check confirmed the chain (112)-(116). The conditional existence of a positive finite size does not by itself establish termination of a concrete interval implementation: one would also need to specify verified approximation and integration of these piecewise sources and precision refinement. No new computations were run and the OPEN status of the global sign was not changed.


## Audit of the role of Euler in completeness

Status: identity PROVED and diagnosis checked independently. Keep P,C,H,r fixed. For any operator core of H, orthogonalized in g, (105)-(116) or Parseval in g applied to Z_*=H^(-1)C give

    Σ_j b_j*b_j/d_j = g(Z_*,Z_*)
                    =rC*C−C*H^(-1)C.                    (117)

The convergence is in matrix norm, since the number of low columns is finite. The right-hand side does not depend on the chosen operator core. Hence, replacing the Möbius seeds by another complete core changes the partial sums and their speed of convergence, but not the total contribution. It is not claimed that this total stays the same when changing Λ or a falsifier: those changes alter P,C,H.

This locates a concrete limit of candidate (106): using the Euler product only to establish invertibility and completeness of the seeds does not provide the sign. The positive sum of (117) also exists with bases lacking that arithmetic datum; combining it with P−rC*C one recovers exactly the Schur complement whose sign remains open. Therefore arithmetic completeness alone does not satisfy clauses O3/O4 of OBJECT_SPEC.

It is not a NO-GO for all Möbius seeds nor a discard of their possible finite efficacy. An additional identity on P,C,H, or an arithmetic control of partial sums sufficient to dominate rC*C−P, could provide new information. That piece is not built. The candidate is kept as an explicit approximation tool with proved convergence, without presenting it as a global positivity mechanism.


## Explicit action on the steps of the first seed

Status: formula PROVED and checked; implementation verified numerically, not interval. For f=1_[a,b] extended by zero, define I(d)=atanh(exp(−d/2))+atan(exp(−d/2)), d>0. The exact archimedean action, away from the two endpoints, is

    Arch f(x)=C0+I(x−a)+I(b−x),       a<x<b,
             =−I(a−x)+I(b−x),         x<a,
             =−I(x−b)+I(x−a),         x>b.                (118)

Inside the step, the difference term reduces to the two exterior tails. Outside, the negative integral of H0 over [a,b] remains. In both cases I(d)=∫_d^∞H0(u)du gives (118). The singularities at the endpoints are logarithmic, L²; point values play no role. For x∈(-T,T), the full physical action adds exactly

    −Σ_(log n<2T)Λ(n)/√n
           [1_[a,b](x+log n)+1_[a,b](x−log n)].           (119)

The linear combination of (118)-(119) evaluates A R_Tp_0, since R_Tp_0 is a finite sum of steps. The parity reflection commutes with A. On the other hand, to apply the high projection of (107) one must keep A(P_hg) and A(P_Eg):

    H w_0=Q_high A[g−P_hg−P_Eg], g=Π_σR_Tp_0.            (120)

This expression is not replaced by Q_high Ag, which would omit the couplings. Those terms and the Gram of the source are necessary before claiming that b_0 or its gain has been computed.

step_source.py implements (118)-(119) in mpmath and refuses to evaluate the archimedean part exactly at the singular endpoints. An independent comparison by direct integration of H0 at four interior/exterior points, plus reflection, passed at 70 digits with maximal discrepancy<3.7e−71; step_source_check.json records PASS_NUMERICAL_FORMULA_CHECK. It is an implementation control without interval enclosure, not a numerical sign proof. The mathematical formula was checked independently. The full projected source (120) and the gain of the candidate have not yet been evaluated.


## Action on the hyperbolic moment corrections

Status: formula PROVED/checked; NUMERICAL implementation control. For f_a(x)=exp(ax)1_(-T,T), a=±1/2, and −T<x<T, separating the increments to the left and right gives

    Arch f_a(x)=exp(ax)[C0+I(x+T)+I(T−x)
                         +F_(-a)(x+T)+F_a(T−x)],
    F_a(d)=∫_0^d H0(u)(1−exp(au))du.                      (121)

The integrand has removable value −a/2 at zero. For q=exp(−d/2), write

    A_+(q)=2log q−log(1+q)−(1/2)log(1+q²)−atan q,
    A_−(q)=−log(1+q)+(1/2)log(1+q²)−atan q,
    F_(±1/2)(d)=A_±(q)−A_±(1).                           (122)

The substitution t=exp(−u/2) reduces the integrands to 2/[t(1+t)(1+t²)] and −2/[(1+t)(1+t²)], respectively. The above primitives satisfy those derivatives. Their constants are A_+(1)=−(3/2)log2−π/4 and A_−(1)=−(1/2)log2−π/4. In particular F_+(0)=F_−(0)=0, F_+(d)≤0 and F_−(d)≥0.

The full action subtracts the contacts of (119) with f_a extended by zero. The combinations (f_++f_−)/2 and (f_+−f_−)/2 give cosh and sinh; the normalization factors of the embedding are not omitted when passing to the half-interval. With (118),(121) and the polynomial action already available, the pieces needed to write the source of (120) are at hand, keeping all corrections. Its assembly and Gram are still pending.

step_source.py incorporates exponential_increment, arch_exponential and physical_exponential. Six independent integrals at 70 digits, the signs of F and the reflection were checked: maximal error<4.6e−71, exponential_source_check.json PASS_NUMERICAL_FORMULA_CHECK. It is neither an interval enclosure nor an evaluation of the gain of the corrector.


## Coefficients of the first projected seed

Status: projection identity and normalization checked; coefficients computed NUMERICALLY at 100 digits, without enclosure. On the isometric half-interval, the first unprojected seed is

    g(x)=Σ_(n<exp(2T)) μ(n)/(2√(Tn))
       [1_[max(0,log n−T),T](x)
           +σ1_[0,min(T,T−log n)](x)],                    (123)

omitting empty intervals. The term n=1 equals 1/√T for σ=+1 and zero for σ=−1. Let v_k=<p_k,g>, α_k=<p_k,h>, h_low=Σ_(0≤k≤N)α_kp_k. Then

    t=Σ_(0≤k≤N)α_kv_k/Σ_(0≤k≤N)α_k²,
    c_k=−v_k+tα_k, κ_h=−<h,g>/||h||²,
    w_0=g+Σ_(0≤k≤N)c_kp_k+κ_h h.                         (124)

The formula uses Q_high=I−P_V+P_hlow−P_h; it does not invert another ill-conditioned system. The v_k are integrated via the exact Legendre primitive, and <h,g> by primitives of cosh/sinh on each step. For each term c1_[a,b] of (123), the parity source is c[A1_[a,b](x)+σA1_[−b,−a](x)], without another factor √2. Adding Σc_kA_σp_k+κ_hA_σh and projecting the output gives Hw_0.

projected_mobius_seed.py saves the two representations in projected_mobius_seed.json for T4/5, N95. The numerical residuals of the moment and of the 95 low orthogonalities are<2.7e−102. The first four moments v_k were also checked by independent piecewise quadrature, with discrepancy<9e−103. The coefficients κ_h are approximately −0.4538580045 in even and 2.4536035273 in odd. These residuals are implementation controls, not proofs by tolerance: the exact projection is (124), and the saved values are not intervals. Assembling the full action and measuring the gain remain; no new sign has been certified.


## First diagnosis of the full source and gain

Status: NUMERICAL, without intervals or sign certificate. evaluate_mobius_gain.py assembles the source of (124), including the polynomial and hyperbolic actions, and also applies Q_high on the output using integrated moments of h, without truncating h by its expansion. It uses the 16 previous high directions, N95 and r=16 in the metric of (103). The partition contains six pieces with all singularities and boundaries of the contacts of the steps. The polynomial action reuses operator_basis with inner order 160.

C=Q_high AE, Y=Q_high AW, y=Q_high Aw_0 were computed by quadrature, K=W*Y symmetrized, G=16Y*Y−K and a=G^(-1)(16Y*y−W*y). With q=w_0−Wa, Hq=y−Ya, d=16||Hq||²−<q,Hq>, b=16(Hq)*C−q*C and gain trace ||b||²/d were evaluated. A floating-point residual is not assumed to be a rigorous bound.

| Parity | Order per piece | ||Hw_0||² | d | ||b|| | gain trace |
|---|---:|---:|---:|---:|---:|
| even |96|0.00672301415|0.0982195543|0.645151965|4.23765981|
| even |128|0.00673407369|0.0983963592|0.645526034|4.23495203|
| odd |96|0.00685998560|0.0973321791|0.653330066|4.38539628|
| odd |128|0.00687106697|0.0975084935|0.653543089|4.38032169|

The gain changes approximately 0.064% in even and 0.116% in odd between these orders; it is declared neither converged nor enclosed. The low input/output orthogonalities are smaller than 1.4e−14, and the moments smaller than 2e−16. mobius_gain_diagnostic.json keeps all values and sizes. The gain has rank at most one in low COORDINATES, not an improvement of λ_A nor an L² eigenvalue.

The test gives numerical evidence of a nonzero row b for the first seed, whose exact positive denominator was already proved by (111). It does not establish b≠0 by intervals, nor that the gain benefits the decisive direction or makes the full scalar criterion positive. That criterion was not evaluated here. The Möbius selection still lacks a global arithmetic comparison; this trace is not interpreted as such.


## Directional gain against the full scalar criterion

Status: NUMERICAL diagnosis, full code audited independently; not a certificate of inertia or sign. evaluate_mobius_gain.py was extended to form the previous scalar optimum J_before=P−16C*C+B*G^(-1)B, B=16Y*C−W*C, and J_after=J_before+b*b/d. Both matrices and the gain are saved in mobius_directional_{parity}_{order}.npz; mobius_directional_diagnostic.json preserves the controls. The first trace report was not overwritten.

| Parity | Order | minimum before | minimum after | gain on the previous minimal vector |
|---|---:|---:|---:|---:|
| even |96|−7.7778123|−7.7213228|0.2152956|
| even |128|−8.2139169|−8.1227793|0.2354798|
| odd |96|−7.7996978|−7.7538301|0.1536406|
| odd |128|−8.2248839|−8.1625782|0.1624179|

In the four computations, the floating-point number of negative eigenvalues goes from 23 to 22. It is not a certified index. The gain on the previous minimal vector does not coincide with the change of the minimum, since the vector may change when adding the rank-one matrix.

The minimum changes by about 0.44 when varying the quadrature; these values are NOT declared converged. The metric orthogonality g(W,q) shows residuals between 4.8e−9 and 7.1e−8, larger than the moment residuals: the assembly of actions and the symmetrization of K are still subject to quadrature errors. Negativity of the form A is not deduced, nor even a rigorous bound of the criterion J from these floating-point matrices.

Limited conclusion: the test detects a contribution in a low direction, but does not observe that a single seed closes the scalar criterion. The positive trace of the previous test did not justify that conclusion. A certified estimate of the gain and, above all, an arithmetic compensation rule sufficient for all T are still pending. No campaign of mechanical increase of seeds is opened on the basis of these data.

The code audit found no normalization or sign errors nor omitted terms. It identified that using symmetrized K in G but unsymmetrized W*Y in the control contributes to the metric defect; both coincide exactly, not in quadrature. It confirmed that the floating-point increment, positive by construction, certifies neither its exact value nor the sign of J or A.


## Optimization with modal weights and monotone refinement

Status: PROVED as an auxiliary development, checked independently. Antecedents: modal control (57)-(59), scalar optimization (100)-(102) and the recent unfavorable diagnosis of the scalar criterion. The change consists of keeping per-mode weights inside the optimization, not of mechanically increasing the number of seeds. It provides no new arithmetic sign identity.

Fix T, the low carrier and its high complement, with the bases and numbers d_k>0 of (92), k>N. Set c=1+eta_bar and distinguish the modal columns w_k from the directions chosen for the corrector. The dual inequality gives

    H^(-1)≤V:=Σ_(k>N)d_k^(-1)w_kw_k*.

For L≥N+1, define the explicit finite-rank-plus-identity operator

    U_L=c/d_(L+1) I
          +Σ_(N<k≤L)(1/d_k−1/d_(L+1))w_kw_k*.             (125)

The control W∞W∞*≤cI and the growth of d_k imply

    V≤U_L,
    U_L−U_(L+1)=(1/d_(L+1)−1/d_(L+2))
                    [cI−Σ_(N<k≤L+1)w_kw_k*]≥0,
    ||U_L−V||≤c/d_(L+1)→0.                              (126)

For the first inequality, separate the tail of V and bound it by 1/d_(L+1) times the sum of its rank-one projectors. For the norm bound, U_L−V is positive and bounded by (c/d_(L+1))I. The w_k are not assumed orthonormal.

Choose fixed ε>0 and V_L=U_L+εI. Let F be a finite independent family of corrector directions in Dom(H), Y=HF, K=F*HF, D=F*C. Then

    G_L=Y*V_LY−K≥εY*Y>0,
    B_L=Y*V_LC−D,
    X_opt=G_L^(-1)B_L,
    J_opt=P−C*V_LC+B_L*G_L^(-1)B_L.                      (127)

The expansion of J_L(X)=S_X−R*V_LR reproduces the completion of squares of (101). In particular J_opt−J_L(X)=(X−X_opt)*G_L(X−X_opt)≥0. H² is not applied to the columns: only Grams of Y and their modal moments are formed. The exact remainder is

    S_Schur−J_L(X)=R*(V_L−H^(-1))R≥0.                    (128)

With the low carrier and ε fixed, enlarging the corrector space does not worsen the optimum. Increasing L does not worsen it either, since V_L decreases and therefore J_L(X) increases for each fixed corrector. The regularization ε is not free: it is included exactly as εR*R and is not omitted in a certificate.

The metric g_L(u,u)=<Hu,V_LHu>−<u,Hu> satisfies ε||Hu||²≤g_L(u,u)≤||V_L||||Hu||². By the operator core proved in (114), exhausting the corrector directions makes J_opt→S_Schur for fixed L; it also holds when increasing L jointly, by monotone comparison with any fixed L. Increasing L ONLY with a fixed corrector space does not prove that convergence: V+εI may strictly exceed H^(-1).

This construction avoids replacing the whole modal distribution by the scalar penalty r=16 of the previous test. It is not claimed that it numerically beats (69) with any ε nor that the new criterion is positive without evaluating it. The global arithmetic compensation remains pending. No new computation was launched and the local certificates were not altered.


## Diagnosis of the modal optimization with the same seed

Status: NUMERICAL, code audited independently, without enclosures. evaluate_mobius_gain.py --metric modal keeps the seed, corrector space and orders 96/128, but uses (125) with L111 and ε=1e−12. It includes all individual weights 1/d_k−1/d_112, not a single scalar bound. The computed matrix G has minimum≈43.79 in even and 44.95 in odd, with condition≈4.8; the solve would stop if that floating-point minimum were not positive.

| Parity | Order | minimum before | minimum after | gain on the previous minimum |
|---|---:|---:|---:|---:|
| even |96|−1.76608e−10|−1.76444e−10|2.46576e−13|
| even |128|−1.36001e−11|−1.33763e−11|3.37375e−13|
| odd |96|1.05704e−9|1.09263e−9|5.30744e−11|
| odd |128|1.05693e−9|1.09256e−9|5.31591e−11|

The trace of the gain goes from 0.902918 to 0.902353 in even and from 0.933455 to 0.932368 in odd. Reports and matrices are kept in mobius_modal_directional_diagnostic.json and the modal NPZ files, without overwriting the scalar test.

The diagnostic improvement with respect to the scalar criterion is clear, but the even ground value is not resolved by this quadrature: it changes at a scale larger than the previously certified local positive ground value. Nor are the positive odd minima certified. The exactness of the local sign still rests on (96), not on these figures. No improved bound of λ_A nor a new window is obtained.

The audit confirmed c_T, indices 96..112, all products of the metric and separate names. The floating-point diagnosis does not represent eta_bar=1e−370; an interval version must restore c=1+eta_bar and its contribution to d_k. The test G_min>0 is only a numerical safeguard. The campaign of sizes or quadratures was not mechanically enlarged. The global arithmetic proof of compensation remains open.


## Algebraic proof against the rescaling 1.1Λ

Status: PROVED and checked as a scope audit, not as a new sign mechanism. Replacing Λ by cΛ gives E_c=cE and R_c=exp(−cE), with inverse exp(cE). The finite expansion of the formal Euler product produces

    R_c=Σ_(n<exp(2T)) d_c(n)/√n U_log n,
    d_c(n)=∏_(p^k||n)(−1)^k binom(c,k).                   (129)

For T=4/5 only 1,2,3,4 enter, and

    R_c=I−c/√2 U_log2−c/√3 U_log3
                       +c(c−1)/4 U_log4.                (130)

At c=1 the last coefficient is zero; at c=11/10 it equals 11/400. The identification with μ breaks, but not invertibility nor continuity in graph norm: the exponentials are still finite polynomials of shift operators by nilpotency. Hence the operator core property of the transported seeds survives the rescaling.

For the modified form the cutoff N, the coercivity γ and the weights d_k must be recomputed. In particular the values N95 and γ1/8 of the real certificate are NOT transferred to 1.1Λ. Once an appropriate coercive complement is built, the optimization and convergence lemmas keep their proof; they do not use c=1 for the sign of their increments.

Conclusion of the audit: the change of coefficients in (130) is not the positivity breakdown required by O4 of OBJECT_SPEC. The auxiliary positive mechanisms survive; what is still missing is to prove the domination of the initial term of (105), or its modal version, by an identity that specifically uses the true data. Invariance of the Schur complement when changing c is not claimed, nor are possible additional uses of the arithmetic identity discarded. This proof does not modify the local certificate for Λ nor provide a global sign.


## Exact candidate identity without inverse of the high operator

Status: PROVED as an identity and positivity of the high remainder, checked independently. Antecedents: completion (84) uses H^(-1)C; modal criterion (125)-(128) uses an explicit majorant V=V_L. It is not a proof of the sign of the low matrix.

Fix V=U_L+εI, ε>0, and a finite corrector Z. For F=Ex+v in the primitive form domain, set

    w=v+Zx, R=C−HZ, J=S_Z−R*VR,
    mathcal V(F)=V^(1/2)Rx+V^(-1/2)w.

Then the exact identity on that WHOLE domain is

    a_T(F)=||mathcal V(F)||²+x*Jx
                       +h(w)−<w,V^(-1)w>.                (131)

Here h is the form restricted to the high complement. The expansion of the square contributes R*VR, 2Re<w,Rx> and <w,V^(-1)w>; the two added diagonal terms cancel exactly with J and the last term. There is no inequality nor loss of margin in this identity.

Since H^(-1)≤V, the inverse order gives V^(-1)≤H in the sense of forms, hence

    h(w)−<w,V^(-1)w>≥0.                                  (132)

The domain of h is preserved when adding Zx, whose columns belong to Dom(H). V is bounded and uniformly positive, so both roots are bounded and do not restrict the domain. The justification of (132) uses the already proved modal majorant; the operator mathcal V does not require computing H^(-1).

Indeed, V=αI+Σβ_kw_kw_k*, α>0, β_k≥0. On S=span{w_k:N<k≤L}, a finite orthonormalization and the positive matrix of V give its roots; on S^⊥ they are the scalars α^(±1/2). The whole candidate operator is specified by these finite operations, the corrector Z and its source R.

The remaining obligation is exactly J≥0. If it is proved, (131)-(132) provide the square and a non-negative remainder of the sought form. As long as it is not proved for all T, the term x*Jx remains signed and the identity does NOT by itself satisfy OBJECT_SPEC. Nor has an arithmetic breakdown for the falsifiers been built here. The result turns the certificate into a usable exact identity; it changes neither the global OPEN status nor the already established local window.

## Local positive realization of identity (131)

Status: PROVED locally, code audited and replay reproduced independently. It is a closure of the previous construction, not a new global route. Fix T=4/5, L=111 and ε=10^(-20), with the frozen rational correctors of the certificates (94)-(96). The already proved modal comparison gives U_111≤(1783/500)I+8WW*. By the transfer of criterion (69), its certified matrix M satisfies

    J=S_Z−R*(U_111+εI)R ≥ M−εR*R
                            ≥ (s−ε B_R)I,                 (133)

where s is the COORDINATE lower bound of M, not the L² bound of the form, and

    B_R=[sqrt(tr G_V)+10^(-35)
                sqrt(27/20+(1+10^(-370))||X||_F²)]².

The bound comes from the norm of the approximate source, from the contraction by the high projection and from the operator error; the exact residue is not assumed small. certify_regularized_identity.py reproduces both congruences with Arb at 500 digits, verifies the fingerprints and subtracts ε B_R. Result in regularized_identity_T4_5.json:

| Sector | Conservative upper bound of B_R | Lower bound of J in coordinates |
|---|---:|---:|
| even | 1260 | 4.79541688e−12 |
| odd | 1297 | 1.05649759e−9 |

Consequently, for these concrete data ALL terms on the right-hand side of (131) are non-negative on the full carrier of each parity. The finite term can be written ||J^(1/2)x||², with J defined by the exact sources, not by their floating-point approximations. The orthogonal sum of parities gives the local identity on P_(4/5).

Scope: the verification reuses the already certified sources and their bounds; it is not an independent reintegration. It neither enlarges the known window nor improves the bound (96). It does remove the open question of whether the regularization needed to define V^(-1/2) could consume the local margin. For all T, building correctors and an arithmetic domination S_Z≥R*V R remains OPEN; neither (133) nor the convergence of correctors proves that global domination.

## Mandatory interpolation if the ground value is exactly zero

Status: PROVED as a design corollary, checked independently. Antecedents: (116) warns that convergence does not guarantee a finite semidefinite certificate; (128) already gives the loss identity. It is not a new identity, an arithmetic route nor a sign result for additional T. The addition specifies what the corrector must do in the limit case that the goal ≥0 allows.

Write S=P−C*H^(-1)C, B=V−H^(-1), with V=U_L+εI and ε>0. By (128), J=S−R*BR and B≥εI. Then

    J≥0 implies S≥0 and R ker(S)={0}.                       (134)

Indeed S=J+R*BR≥0. If x belongs to ker(S),
0≤x*Jx=−<Rx,BRx>≤−ε||Rx||²; hence Rx=0. In terms of the corrector, this condition is HZx=Cx exactly in each null direction. A small positive error is not enough.

Conversely, assuming S≥0, set K=ker(S). Since the low space is finite, S_perp=S|_(K^perp)>0 when K^perp is nontrivial. One has the exact criterion

    J≥0 if and only if R|_K=0 and
                  R_perp* B R_perp ≤ S_perp.              (135)

The proof is the orthogonal decomposition K⊕K^perp: the first condition annihilates the cross rows and columns of R*BR, and S already has those rows and columns zero. If S=0, the criterion reduces to R=0. For a sufficient bound on the complement one can use ||B|| ||R_perp||²≤lambda_min(S_perp); this is only a conditional tool, not an available bound of the true margin.

The hypothesis B≥εI is relevant. If only B≥0, what is needed is B^(1/2)R|_K=0, not necessarily R|_K=0. The present corollary does not force every possible positive identity to use interpolation: it refers to the regularized class (131).

Operational consequence: a design that aims to cover the non-strict goal via (131) needs to reproduce exactly the possible null directions, or prove that they do not exist, or change the penalty and justify its new remainder. The corollary does not determine K nor prove that a null direction exists for the real form. It does not authorize using H^(-1)C as a computable construction nor assuming S≥0 in the global proof. The arithmetic domination remains OPEN.

## Strict monotonicity of the ground value of the full form

Status: PROVED, argument and gate checked independently. Antecedents: P46 lem:compact proves compactness of the resolvent and existence of a minimizer for the FULL form on P_T; lem:strict of the paper refers to the archimedean ground value. Here compactness is combined with interior translations that preserve both moments. It is an auxiliary lemma, not an arithmetic sign mechanism nor a priority claim.

For 0<T_1<T_2 one has

    lambda_A(T_2)<lambda_A(T_1).                           (136)

Proof. Extension by zero preserves norm, moments and autocorrelation, so it gives the non-strict inequality. Suppose equality with value lambda. Let F be a unit minimizer in P_(T_1), which exists by lem:compact. For |s|<T_2−T_1, define F_s(t)=F(t−s). Its support remains in I_(T_2) and

    ∫F_s(t)e^(±t/2)dt=e^(±s/2)∫F(t)e^(±t/2)dt=0.

Translation preserves the archimedean form norm and all autocorrelations; the additional contacts of the larger window vanish when their shift exceeds the width of the support. Hence F_s is admissible and a_(T_2)(F_s)=lambda. Since a_(T_2)−lambda||·||² is a non-negative form, polarization implies that each F_s belongs to the eigenspace of H_(T_2) with eigenvalue lambda. That eigenspace is finite-dimensional by compactness of the resolvent.

However, any finitely many distinct translations of F are linearly independent. To see this, order s_1<…<s_k and set alpha=inf ess supp F. On the interval (alpha+s_1,alpha+s_2) all translations except the first are zero almost everywhere; the first is not identically zero there, by the definition of alpha. Every null combination forces its first coefficient to be zero. Repeat with the remaining translations; for the last one use F≠0. Thus independent families of arbitrary size are obtained inside a finite eigenspace, a contradiction. This proves (136). Strict monotonicity of each parity sector is not claimed by this argument: translations do not preserve parity.

In particular,

    [lambda_A(T)≥0 for all T]
        implies [lambda_A(T)>0 for every finite T].         (137)

It suffices to choose T_2>T_1 in (136). More locally, non-negativity at T_2 implies strict positivity in every smaller window. If lambda_A(T_0)=0, then lambda_A(T)<0 for all T>T_0. These consequences neither prove the global premise nor give a quantitative bound of the margin.

Application to the design: under the global goal, the Schur matrices of each finite window are positive definite; hence the null case of (134) does not require a separate construction within an eventual global proof. This does not allow assuming the sign when building the correctors. The convergence of (116)/(128) only gives existence of a positive finite step CONDITIONAL on that positivity, without rate or arithmetic mechanism. The lemma survives any locally finite comb with the same compactness and translation properties; it does not distinguish falsifiers and does not by itself satisfy O3/O4.
