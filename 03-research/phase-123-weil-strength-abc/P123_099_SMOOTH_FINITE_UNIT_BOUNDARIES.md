# P123.099 — Smooth tangential diagonals on the actual finite-unit boundaries

Date: 2026-09-06. Status: PROVED-IN-REPOSITORY at finite unit levels,
including the transition on tangential homology. A completed limit and
its comparison with the full source are not assumed.

## 1. The finite-level arithmetic mapping tori

For the q-zero boundary put a=log q, U=Z_p^*, and choose an open
subgroup N of U. Let F_N=U/N. Its finite-level quotient is

    Y_N=(R times F_N)/((t,u)~(t+a,q u)).                     (1)

This comes from the actual Gamma quotient of Z_q by first normalizing
the p valuation; it is not a replacement circle unrelated to the source.
Write d_N for the order of q in F_N. Its q-orbits all have length d_N,
so Y_N has |F_N|/d_N circle components, each of circumference d_N a
in the physical real coordinate t. Give it the quotient of dt times
probability counting measure on F_N. Each circle consequently has
measure d_N a/|F_N|, and the total measure is a, as in P123.041.

Set B_N=C^infinity(Y_N), with the finitely many circle derivative
seminorms in t. Pullback embeds this as a dense-in-its-own-level smooth
subalgebra of C(Y_N), and then as a subalgebra of C(B_q).
It is the smooth, N-invariant tangential coefficient domain.

## 2. A finite free diagonal resolution

Let R_N=C^infinity(Y_N times Y_N)=B_N tensorhat_pi B_N. The tensor
identity follows componentwise by the Fourier-series argument of
P123.098. On a pair of equal circle components choose their angular
coordinate z=exp(2pi i t/(d_N a)), using the same origin in both factors,
and put g_N(y,z')=z(y)-z(z'). On pairs of distinct components put g_N=1.
These pieces are smooth because component pairs are open and closed.

Exactly as in P123.098, restriction to the diagonal gives the finite
free, underlying continuously split resolution

    0 -> R_N --g_N--> R_N -> B_N ->0.                       (2)

Division on equal component pairs uses a first-order real transverse
coordinate and costs at most one derivative; on distinct pairs it is
the identity. This proves both exactness and continuity, including the
closed image of multiplication by g_N.

Derived diagonal pullback of (2) is a two-term complex with zero
differential. Its degree-one term identifies canonically with the
conormal line of the diagonal, namely the complexified cotangent line
Omega_N=B_N dt. Although g_N depends on angular origins, its class
modulo the square of the diagonal ideal maps to its differential in
the transverse direction; rescaling g_N changes the basis of that line,
not the line itself. Thus the smooth completed diagonal has

    H_0=B_N,    H_1=Omega_N=B_N dt,    H_j=0 for j>=2.       (3)

This is a finite free derived-intersection calculation over R_N.
Equivalently it computes the continuous Hochschild bar via the usual
resolution comparison: both the completed bar and (2) are resolutions
by relatively projective R_N-modules in the underlying linearly split
exact structure. Free modules lift generators through a split surjection;
inductive lifting constructs the comparison maps and their homotopies.
Their terms are continuous at every step. Thus no algebraic tensor
resolution is substituted for the completed smooth one.

## 3. Refining a unit level preserves the tangential line

If M is an open subgroup contained in N, the map pi:Y_M->Y_N induced
by U/M->U/N is a finite covering and a local diffeomorphism in t.
Consequently pullback B_N->B_M is continuous in all derivative
seminorms and

    pi^*(h dt)=(h compose pi) dt.                            (4)

Formula (4) is the actual degree-one diagonal map. To check it without
depending on a chosen g_N, use the degree-one bar map
b_0 tensor b_1 -> b_0 db_1: its boundary identities follow from the
Leibniz rule, it identifies (3) with the conormal line, and it commutes
with smooth pullback. On a circle covering of degree r, an angular
coordinate would give dtheta_N=r dtheta_M; expressing both in the
physical t coordinate cancels that scale. Thus (4) contains no spurious
circle-length factor. Degree zero is ordinary pullback. These maps
compose exactly on triples of unit levels.

One must distinguish this homology map from pulling back the entire
diagonal support in Y_N times Y_N: that inverse image in Y_M times Y_M
contains every deck graph, not just the diagonal. Equation (4) is
induced by the algebra/bar pullback; it does not discard those extra
components by claiming they never existed.

Normalized quotient measures satisfy

    integral_(Y_M) h compose pi=integral_(Y_N) h.            (5)

This follows directly by averaging over the finite unit fibers in (1).
Hence the original Haar trace on degree zero and the tangential
transition (4) retain their separate, explicit normalizations.

## 4. The moving-graph family at each finite level

Real translation by s preserves each circle component. Pulling (2)
to its graph gives on each component, up to the invertible angular
factor, the two-term complex

    [B_N --(1-exp(2pi i s/(d_N a)))--> B_N].                 (6)

For 0<|s|<d_N a it is acyclic, and at zero it has the two groups (3).
It is a finite free family with constant virtual rank zero. This places
the smooth excess model of P123.098 on the actual arithmetic finite-level
mapping tori. Compatibility of the entire moving families under changes
of level requires accounting for their additional deck graphs; (4)
alone is not that stronger assertion.

## 5. Remaining scope for A

This supplies the tangential smooth domain, its diagonal and its fixed
homology transitions at every finite unit level. The normal induced
action of P123.043 already uses this real-smooth/unit-finite regularity,
but that fact alone does not identify its regularized trace with a
determinant of (2) or (6). In particular the tangential virtual-rank
cancellation is not a proof of vanishing or positivity of the Weil form.

A common completed smooth source, full derived transition maps,
orbit-decay tensor comparisons in that topology, normal determinant
and mixed RR remain to be constructed before closing row A.
