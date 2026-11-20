# POWER_THREE_SECANTS_079 — Three generators from ONE additional concavity

**Update 080:** the admissible compact range of g was certified in `POWER_THETA_G_COMPACT_080.md`, audited in `POWER_THETA_G_COMPACT_AUDIT_080.md` and summarized in `POWER_STATE_080.md`: ALL triples of powers ai>1 have full positive sign. The mentions below of a pending compact range describe the historical state of this round; h and the higher orders are not discharged by 080.

Status: **PROVED as implication and converse under BASE, independent audit approved (three independent checks).** See `POWER_THREE_SECANTS_AUDIT_079.md`. For the real Phi, the 073 hypotheses are proved; it remains to verify g concave on the interval where one wants to apply it. The pending real compact range and global three generators are not claimed here. Papers untouched; no campaigns, new grids or numerical matrices.

## 1. Antecedents and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread POWER_SCHUR_003, the jet and the class falsifier 074, and 073–078. 003 refutes inferring order three from M increasing, M/u decreasing and even M concave. 074 keeps the potential hypothesis of 073 and again refutes that promotion. None is withdrawn.

The new concrete hypothesis is the concavity of

    g(x)=x b(x)=a sqrt(x)/M(sqrt(x))−1,
    b(x)=[a sqrt(x)/M(sqrt(x))−1]/x, a=M'(0)>0.

The jet 074 identified g''<=0 as a LOCAL necessary condition for three generators. Here it is proved that, TOGETHER with the real properties 073, this same concavity suffices for ALL triples of nodes of the interval, not only a confluent jet. The proof is an algebraic comparison of two bounds on a difference of secants. It does not require the additional concavity of 1/b proposed in 078, nor does it invoke a principle for matrices of arbitrary order.

## 2. Minimal hypotheses and statement

Keep the real M of 073. Use the already proved properties

    M>0, M'>0, M''<0, M(0)=0,
    M/u strictly decreasing.                    (BASE)

The last property also follows from M strictly concave and M(0)=0. In particular g=a u/M−1 is positive and strictly increasing in x=u². The additional property b decreasing of 077 is not needed. Let I be an interval of positive nodes. Assume moreover that g is concave on the interval of squares {u²:u∈I}. There is no need to assume that concavity between 0 and the first node.

Then, for any three nodes u1,u2,u3 in I, the kernel

    K_ij=[M(ui)+M(uj)]/(ui+uj)

is positive semidefinite. If the nodes are distinct and the secant difference of g defined below is strictly positive, K is positive definite. In particular, if g is strictly concave on the interval, all its distinct triples are positive definite.

The CONVERSE also holds within BASE: all three-node blocks of I are positive semidefinite IF AND ONLY IF g is concave on the interval of squares. It is proved directly in §7, without a limiting jet step. This equivalence between a scalar criterion and the 3-blocks under the declared hypotheses does not claim the sign of that curvature for the real Phi where it remains pending.

For original exponents ai=ui+1/2>1, this K is exactly the full form of the three exponentials, including ARCH, polar and ALL contacts, according to CONE001. The exterior map only introduces a positive diagonal congruence. The form is not replaced by an isolated component.

## 3. Secants and exact congruence

First order 0<u<v<w, and write g1=g(u²),g2=g(v²),g3=g(w²). Define

    beta=(g2−g1)/(v²−u²)>0,
    delta=beta−(g3−g2)/(w²−v²)>=0,
    alpha=1+g1−beta u².

Positivity of beta comes from g increasing; delta>=0 is exactly concavity between these three squares. The weak case beta=0 is treated separately at the end.

alpha>=1 is not assumed here. Although 077 would allow proving it, it is unnecessary: M increasing will directly give alpha>beta uv>0 in §4. This care allows using only the concavity of g on the interval of the three squares, without extending it to 0 or introducing an additional hypothesis from 077.

The values are

    g1=alpha−1+beta u²,
    g2=alpha−1+beta v²,
    g3=alpha−1+beta w²−delta(w²−v²).

Set Hi=1+gi>0 and S=diag(H1,H2,H3)/sqrt(a). The congruence T=SKS has entries

    T_ij=1+[ui gj+uj gi]/(ui+uj).                      (CONGRUENCE)

A direct expansion of its determinant gives the exact identity

    det T=delta (u−v)²(v−w)²/(u+w)²
       ·{alpha beta(w²−u²)
                     −delta[alpha w²+beta u²v²]}.       (DET)

Its sign is not concluded from delta>=0 alone: the second factor is the competition that must be controlled.

## 4. Concavity of M controls the same difference

M(v)>M(u), using M(ui)=a ui/Hi, implies

    alpha>beta uv.                                    (INC)

Indeed vH1−uH2=(v−u)(alpha−beta uv)>0. Therefore

    D2=alpha w+beta uv(u+v−w)
      =w(alpha−beta uv)+beta uv(u+v)>0.                 (DEN)

Concavity of M at the nodes gives

    (w−v)M(u)−(w−u)M(v)+(v−u)M(w)<=0.

After multiplying by the positive denominators H1H2H3/a, the left side is exactly

    (u−v)(v−w)
      ·{delta(v+w)D2
        −beta(w−u)[alpha(u+v+w)−beta uvw]}.

The prefactor (u−v)(v−w) is positive. Hence

    delta<=delta_conc
      =beta(w−u)[alpha(u+v+w)−beta uvw]/[(v+w)D2].      (CONC)

Its numerator is also positive, since

    alpha(u+v+w)−beta uvw
      =alpha(u+v)+w(alpha−beta uv)>0.

The orientation of the inequality is not changed when solving for delta; DEN checks the sign that could have been lost if w>u+v.

## 5. Exact comparison with the determinant threshold

The braced factor in DET is positive if

    delta<delta_crit
      =alpha beta(w²−u²)/[alpha w²+beta u²v²].          (CRIT)

The difference of the two thresholds admits the factorization

    delta_crit−delta_conc
      = beta(w−u)uvw(alpha+beta u²)(alpha+beta v²)
        /{[alpha w²+beta u²v²](v+w)D2}>0.              (GAP)

To verify GAP it suffices to multiply by the positive denominators: the remaining polynomial identity is

    alpha(w+u)(v+w)[alpha w+beta uv(u+v−w)]
      −[alpha(u+v+w)−beta uvw][alpha w²+beta u²v²]
       =uvw(alpha+beta u²)(alpha+beta v²).

Thus CONC implies delta<delta_crit. The competing factor of DET is strictly positive. If delta>0, det T>0 and by congruence det K>0. The diagonals and the two-point minors are positive by 073. The Schur complement of the first entry has positive diagonal and positive determinant; hence it is positive definite and so is K. This last step is algebra of a 2x2 matrix, not a positivity hypothesis on the full kernel.

## 6. Degenerations and coincident nodes

If beta>0 but delta=0, the data g are affine in x on the three nodes. CONGRUENCE reduces exactly to

    T=alpha·11^t+beta·(u,v,w)^t(u,v,w),

which is positive semidefinite and has rank 2 for distinct nodes. It is not declared positive definite in this case.

If the non-strict versions of BASE are allowed and beta=0, g increasing and concave forces g1=g2=g3 and delta=0. Then T=(1+g1)11^t is positive semidefinite of rank 1. In the real application BASE is strict and beta=0 does not occur, but there is no division by beta to hide that edge.

If two or three nodes coincide, their coefficients are combined and one is left with a block of one or two generators already positive by 073. The matrix with repeated columns is positive semidefinite. Strict energy corresponds to the nonzero represented FUNCTION, not to any nonzero coefficient vector that may represent zero.

## 7. Converse: the sign of the secant difference is necessary

Keep BASE and three distinct nodes, but do not assume delta>=0. Positivity of beta and the inequality alpha>beta uv>0 still hold: they only use g increasing and M increasing at the first two nodes. If delta<0, the braced factor of DET is strictly positive,

    alpha beta(w²−u²)−delta[alpha w²+beta u²v²]>0.

Therefore det T<0 and det K<0. It cannot be a positive semidefinite block. Thus positivity of ALL triples forces delta>=0 for all u<v<w, which is exactly concavity of g on the squares. Together with the implication already proved, the equivalence within BASE follows. More precisely, for each triple the sign of the determinant coincides with that of delta; delta=0 is the rank-2 case described above.

No higher-order conclusion is used, and concavity is not deduced from positive pairs: the new obligation is precisely the sign of these secants of g.

## 8. Current application and reduced obligation

For the real Phi, 073 supplies all the properties of BASE. 077 motivated the quotient coordinates and supplies additional valid results, but its property b decreasing is NOT necessary in the minimal proof of 079. Therefore the ONLY additional obligation of this criterion for three generators is g''<=0 on the desired interval. Concavity of 1/b is not needed for this proof and remains a separate property, not a pending requirement of the criterion.

078 already proves g''<0 for u>=63/2 via the full arithmetic and an explicit algebraic margin. This yields an analytic proof of the triples with ui>=63/2. That region is NOT new coverage: 053 already proved thirteen arbitrary poles in that range. The new result of 079 is to reduce the GLOBAL three-generator obligation to a bounded interval of ONE real curvature. For admissible exponents ai>1 only 1/2<u<63/2 is needed, without needing the second concavity or a sequence of finite matrices.

Not claimed here: g''<=0 on that pending interval, three generators for all ai>1, positivity of four or all orders, or a new time window. The identities were verified symbolically as an auxiliary check; the proof is given entirely by the exact factorizations above, without numerical matrices or parameter campaigns.
