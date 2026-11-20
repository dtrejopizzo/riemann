# POWER_RECIPROCAL_SECANTS_082 — Two reciprocal concavities for order three

Status: **PROVED as an algebraic criterion, final audit passed.** See `POWER_RECIPROCAL_SECANTS_AUDIT_082.md`. Identities and signs checked independently twice. No claim is made of its discharge for all remainders G_p, preservation under Schur, or positivity of all orders. Papers untouched.

## 1. Consultation and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked POWER_SCHUR_003, POWER_TWO_COPY_SCOPE_074, POWER_THREE_SECANTS_079 and POWER_SCHUR_BASE_OBSTRUCTION_081.003/074 refute inferences from pairs or from generic concavity hypotheses.079 proves order three under BASE073 plus an additional concavity;081 proves that the REAL remainder G_p does not inherit that BASE, because its derivative can be negative.

The new object is a criterion symmetric under F↔1/F that does NOT require F increasing or concave. Within the class of strictly positive pairs, two concavities in x=u² are necessary and sufficient for all triples. The criterion allows the negative derivatives of081. It is not presented as a solution of the obligation to prove those concavities for the real remainders.

## 2. Definitions and statement

Let I be an interval of positive numbers, and F:I→(0,infinity) continuous. Define

    K_F(u,v)=[F(u)+F(v)]/(u+v),
    x=u², R(x)=u/F(u), S(x)=uF(u)=x/R(x).

For distinct nodes x_i, the notation R[x1,x2] and R[x1,x2,x3] denotes the usual divided differences, without an additional factorial. Suppose ALL blocks of two distinct nodes of K_F are positive definite. Then the following are equivalent:

1. All blocks of three nodes of K_F are positive semidefinite.
2. R and S are concave on the interval of squares I².

For a distinct triple, positive definiteness is equivalent to BOTH second-order divided differences being strictly negative. Strict concavity of both functions is sufficient for all distinct triples to be positive definite; it is not replaced by a claim about their strict second derivatives if there is only continuous regularity.

## 3. Normalized identity of order two

For 0<u<v in I, set x1=u²,x2=v² and Ri=R(xi). A direct expansion gives

    det K_F(u,v)
       =(u−v)²/(R1R2) · R[x1,x2] S[x1,x2].          (DET2)

Indeed, performing the congruence diag(R1,R2), the numerator of its determinant is

    (R2−R1)(v²R1−u²R2)/(u+v)².

The two factors R2−R1 and v²R1−u²R2 cannot both be negative: that would require R2<R1 and R2/R1>v²/u²>1. Hence the hypothesis of strictly positive pairs is equivalent to

    R[x1,x2]>0, S[x1,x2]>0, ALL x1<x2.             (PAIR)

In particular R and S are strictly increasing. It does not follow that F is increasing.

## 4. Secants of a triple

Fix 0<u<v<w in I and write Hi=R(ui²), (u1,u2,u3)=(u,v,w). Define

    beta=(H2−H1)/(v²−u²)>0,
    delta_R=beta−(H3−H2)/(w²−v²),
    alpha=H1−beta u².

PAIR for S gives

    alpha=[v²H1−u²H2]/(v²−u²)>0.

The inequality alpha>beta uv of079 is not needed: it expressed that F was increasing. The data are parametrized exactly as

    H1=alpha+beta u²,
    H2=alpha+beta v²,
    H3=alpha+beta w²−delta_R(w²−v²).

Define also

    delta_S=(S(v²)−S(u²))/(v²−u²)
             −(S(w²)−S(v²))/(w²−v²).

S(x)=x/R(x) and denominators Hi>0 give the identity

    delta_S={alpha beta(w²−u²)
                −delta_R[alpha w²+beta u²v²]}/(H1H2H3). (RECIPROCAL)

This identity is verified by multiplying by H1H2H3 and substituting the three values Hi; only polynomial products remain.

In particular, if delta_R<=0, RECIPROCAL gives delta_S>0. Both defects are never nonpositive at the same time. This is the additional sign point that a factorization of the determinant does not contain by itself.

## 5. Normalized identity of order three

Set D=diag(H1,H2,H3) and T=DK_FD. Then

    T_ij=[ui Hj+uj Hi]/(ui+uj), T_ii=Hi.

The polynomial expansion of079, now without its BASE hypothesis, gives

    det T=delta_R (u−v)²(v−w)²/(u+w)²
       ·{alpha beta(w²−u²)
                  −delta_R[alpha w²+beta u²v²]}.

Using RECIPROCAL and det T=(H1H2H3)² det K_F,

    det K_F=delta_R delta_S/(H1H2H3)
                        ·(u−v)²(v−w)²/(u+w)².       (SECANTS)

Since

    delta_R=−(w²−u²)R[u²,v²,w²],
    delta_S=−(w²−u²)S[u²,v²,w²],

one obtains the symmetric form

    det K_F(u,v,w)
       =Vandermonde(u,v,w)²/(H1H2H3)
          ·R[u²,v²,w²] S[u²,v²,w²],                (DET3)

where Vandermonde(u,v,w)=(v−u)(w−u)(w−v). No factor (u+w) remains in DET3: it cancels exactly with (w²−u²)².

## 6. Proof of the criterion and boundaries

By PAIR all principal minors of order one and two are positive. By the Schur complement of a diagonal entry, the order-three block is PSD if and only if its determinant is nonnegative, and it is PD if and only if its determinant is positive.

SECANTS requires delta_R delta_S>=0. RECIPROCAL excludes both being negative and also excludes one being negative and the other zero. Consequently

    det K_F>=0  iff delta_R>=0 and delta_S>=0;
    det K_F>0   iff delta_R>0 and delta_S>0.

In terms of divided differences, these are exactly the two concavities, or the two strict inequalities for that triple. Imposing them for all triples of an interval is equivalent to the concavity of R and S; continuity allows the usual formulation without additional differential regularity.

If delta_R=0, RECIPROCAL gives delta_S>0 and the determinant is zero. The congruence reduces to T=alpha·11^t+beta·(u,v,w)^t(u,v,w), of rank two. If delta_S=0, the case is its image under F↔1/F and also has rank two. Under strict PAIR both defects do not vanish simultaneously. The argument alpha beta>0 is not extended to classes of merely PSD pairs without separating their degeneracies.

Repeated nodes produce repeated columns and PSD matrices whenever the block of distinct nodes is. The coefficients are combined: a represented function that is zero can correspond to a nonzero coefficient vector.

## 7. Symmetry, relation with079 and real scope

The exact identity

    K_(1/F)(u,v)=K_F(u,v)/[F(u)F(v)]

is a positive diagonal congruence. Inversion swaps R and S, so PAIR and the two-concavity criterion are invariant. The differential pair criterion |uF'/F|<=1 also admits negative derivatives;081 does not refute it.

For F=M real, R=u/M=(1+g(x))/a. Hence R''=g''/a. Moreover

    S''(x)=[u²M''(u)+uM'(u)−M(u)]/(4u³)<0

by073. Thus DET3 recovers079: within BASE073 only the concavity of g is missing. The pending real compact of080 is kept and its result is not claimed here.

For F=G_p, the criterion would apply IF its strictly positive pairs and the two new concavities R_p(x)=sqrt(x)/G_p(sqrt x), S_p(x)=sqrt(x)G_p(sqrt x) are proved.077 only proves positive values;078 offers another conditional sufficient criterion for pairs.081 discards requiring monotonicity of G_p, but not the current two concavities. Neither their discharge nor their preservation under repeated Schur has been proved here.

DET2 and DET3 suggest asking about identities of higher order, but no general pattern, positivity of four generators or global closure is declared. The result of082 is the exact order-three criterion for a class that admits non-monotone functions F.
