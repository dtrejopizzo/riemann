# POWER_SCHUR_PRIOR_AUDIT_003 — Antecedents and first arithmetic step

Status: PROVED (algebra and first real step); OPEN (iterated preservation). Does not modify papers.

## 1. Novelty restriction

Consulted the project rules, index ROUTES-TRIED-INDEX, grid R162_2300_part3/part5, CROSSWORD-TO-D and a search for Schur algorithm, Cayley, Nevanlinna and recursion in the corpus. Concrete antecedents:

* 04-papers/36-obstruction-ledger/main.tex:3753–3765: cor:schur-coords and scalar Schur–Nevanlinna algorithm on nested Pick data. The general algorithm is not new.
* 03-research/phase-61-open-problems/respuestas3.md:110–134: Krein–Langer/Schur recursion for transfer matrices ordered by primes. It is another object.
* 03-research/phase-104-unconditional-a1-closure/104_16_JORDAN_COCYCLE_ATTACK.md and its README: shifted completed quotient and Cayley jets. Another input datum and another parametrization.
* 03-research/phase-120-global-polarization/P3_EFFECTIVE_HERGLOTZ_GAMMA_GATE.md:36: Cayley and contractivity of an effective object.

Those searches did not find the exact step for F(z)=L(z+1/2) at the nodes z=31.5+k. The authorized difference is to compute the first transforms from the arithmetic series, prove a preserved inequality and identify an explicit falsifier that fails that inequality. It does not consist in announcing the known algorithm nor in using it as a proof without sign.

## 2. Exact first transform

Fix u>=31.5, c=F(u)>0, and define

    b_u(z)=(z-u)/(z+u),
    r(z)=(F(z)-c)/(F(z)+c),
    q(z)=r(z)/b_u(z),
    F_1(z)=c(1+q(z))/(1-q(z)).

Direct algebra gives

    F_1(z)=c [z F(z)-u c]/[z c-u F(z)].

No contractivity is assumed to obtain this formula. The inequality already proved in POWER_CONE, F'>=0 and F-zF'>0 for z>=31.5, implies 0<=q(z)<1 for all real z>=31.5, z different from u. Indeed r and b have the same sign since F is increasing; q<1 is exactly the inequality of quotients between u/z and z/u, proved for all pairs of that interval. The removable value is

    q(u)=uF'(u)/c <1,
    F_1(u)=c[c+uF'(u)]/[c-uF'(u)]>0.

Hence F_1 is real and strictly positive on that whole interval. This result verifies a first real step; it does not imply positivity of the full kernel of F_1.

## 3. Rational falsifier of the same step

For H(z)=3+cosh z and F=H'/H, take u=log2,v=2log2. Then c=3/17, F(v)=15/41,

    r(v)=22/63, b_u(v)=1/3,
    q(v)=22/21>1,
    F_1(v)=-43c=-129/17<0.

Thus the first real step distinguishes a property proved for the arithmetic datum from the mere assumption of a positive cosh representation. It does not yet prove preservation of that property after the step.

## 4. The next concrete inequality and a warning

Set d=F'(u), e=F''(u). Differentiating the removable fraction at u gives

    F_1'(u)=c[d(c-ud)+uc e]/(c-ud)^2.

The necessary local condition for a next step is

    |u(cd-u d²+uc e)| <= c²-u²d².

This inequality uses only the explicit jets of L, and can be attacked with the absolutely convergent series of psi and zeta'/zeta in the range a>=32. It has not yet been proved here, and global preservation would require the corresponding control for all pairs of the first transform and its iterations.

Do not require F_1'>=0 as an invariant: not even the model F(z)=c+(1/2)log(z/u), locally with c>0, preserves it, since d=1/(2u),e=-1/(2u²) give F_1'(u)<0 when c>1/2. The appropriate invariant must allow both signs of the derivative and control |zF_j'/F_j|, or directly the two-point inequality of each transform. The real positivity of the first transform by itself is not that invariant.

## 5. False lemma: all positive pairs do not preserve the next step

Falsifier verified with rational arithmetic:

    F(z)=(z²-z+10)/10, 1<=z<=3.

One has F>0, F'=(2z-1)/10>0 and

    d/dz[F(z)/z]=1/10-1/z²<0

on the whole interval. By the exact two-point criterion, ALL 2x2 blocks of the kernel [F(x)+F(y)]/(x+y) are positive definite for x different from y in [1,3]. However for the nodes 1,2,3,

    K=[[1,11/15,13/20],[11/15,3/5,14/25],[13/20,14/25,8/15]],
    det K=-13/270000,
    LDL pivots=(1,14/225,-13/16800),
    (93,-375,280)K(93,-375,280)^t=-182/3.

The first transform, with pivot u=1 and c=1, simplifies exactly to

    F_1(z)=(z²+10)/(10-z),
    F_1(2)=7/4, F_1(3)=19/7.

It is positive on [1,3] and increasing, but

    F_1(3)/F_1(2)=76/49>3/2,

so it loses the band of quotients required for the next step. Even the local control of §4 at the initial pivot passes: its left-hand side is 29/100 and the right-hand side 99/100. Hence checking only that jet at the first pivot would not suffice to control the other nodes either.

**Conclusion of exact scope:** the claim of preservation of the Schur step based exclusively on F'>=0 and F/z decreasing is refuted, even though both properties hold at all points of the interval. This does not refute the arithmetic kernel nor the algorithm as a constructive instrument. It forces proving an additional property of the arithmetic series and checking its preservation by the transforms. No NO-GO is claimed outside that explicit class of hypotheses.

## 6. Review and status at recording

The matrix, determinant, pivots and negative vector of §5 were recomputed with exact rational fractions; the formula for F_1 was verified by algebraic simplification. The scalar proofs of §§2–4 use no assumed sign of the full kernel. The first real step for the arithmetic datum remains PROVED by POWER_CONE; iterated preservation remains OPEN, with the false lemma of §5 explicitly withdrawn from the possible justifications.

## 7. Adding concavity does not suffice either: piecewise continuous falsifier

Datum verified exactly:

    F(z)=min((2+3z)/5,(14+z)/10), z>=1.

The two lines cross at z=2. The slope goes from 3/5 to 1/10, so F is positive, increasing and concave. On each branch F(z)/z is decreasing because of its positive intercept, and it is continuous on the union; hence it decreases on all of [1,infinity). All pairs pass the criterion. However F(1)=1,F(2)=8/5,F(3)=17/10 give det K=-53/270000<0.

This refutes, for the class of piecewise continuous functions, that adding concavity to the two monotonicities guarantees the sign of order three. No analytic falsifier is claimed here nor is such a claim needed for the declared scope. Nor is impossibility claimed of obtaining an additional inequality specific to the arithmetic datum.
