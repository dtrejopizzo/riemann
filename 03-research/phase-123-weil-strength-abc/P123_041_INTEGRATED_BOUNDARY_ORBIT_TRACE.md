# P123.041 — integrated boundary-orbit representation and its trace

Date: 2026-09-05. Status: CONSTRUCTED and PROVED for the compact
single-zero boundary orbit. This resolves its tangential trace after
integration against scalar tests. The normal coefficient complex,
higher strata and the common global shadow remain OPEN.

## 1. Identify the orbit as an external homogeneous space

Use logarithmic real coordinates and the positive component

    H_S=R times product_(ell in S_f) Z_ell^*.

Let K_(S,p) be the image of Q_p^* under the local-idele class map.
For x=p^k u its image is

    (-k log p; u at p, p^-k at ell!=p).

It is a closed subgroup: the real coordinates lie in a discrete lattice,
and on each such coordinate its remaining variable is the compact group
Z_p^*. The map from Q_p^* to K_(S,p) is a topological group isomorphism.

The external action on the single-zero stratum of P123.040 is transitive,
and the stabilizer of the class (1;0 at p,1 elsewhere) is exactly
K_(S,p). To see the stabilizer assertion, a fixed class has an a with
 a_v=gamma for every v!=p; dividing by gamma leaves only a local
p-coordinate. Therefore its orbit is

    Y_(S,p)=H_S/K_(S,p).

The mapping-torus description of P123.040 proves that Y_(S,p) is compact.
Give H_S Haar measure dt times probability unit Haar, and K_(S,p)
counting measure in k times probability Haar in u. The quotient measure
on Y_(S,p) has total mass log p. These choices are kept throughout.

## 2. A representation preserving convolution and dagger

On the Hilbert space H_(S,p)=L^2(Y_(S,p)), let

    rho_(S,p)(g)v(y)=v(g^-1 y).

This is a strongly continuous unitary representation. For a scalar
Bruhat test f on H_S, smooth and compactly supported in t and locally
constant at a fixed unit level, define the Bochner integral

    R_(S,p)(f)=integral_(H_S) f(g)rho_(S,p)(g)dg.

It satisfies

    R(f*g)=R(f)R(g),
    R(f^*)=R(f)^*,   f^*(g)=conjugate(f(g^-1)).

These follow by Fubini, Haar invariance and the unitary representation;
||R(f)||<=||f||_1. Unlike the finite block assignment of P123.039,
this is an actual integrated convolution representation.

## 3. Trace class on the declared tests

Choose an open subgroup N of the compact unit factor leaving f
invariant. Integration over N makes R(f) zero on the orthogonal
complement of N-invariant vectors in L^2(Y_(S,p)). The quotient
Y_(S,p)/N is a finite union of circles: after passing to finite unit
quotients the mapping torus is the suspension of a permutation of a
finite abelian group.

Its characters have real frequencies in finitely many arithmetic
progressions. Repeated integration by parts in the compactly supported
real variable bounds the eigenvalue of R(f) at frequency tau by
C_M(1+|tau|)^(-M), uniformly over those finitely many progressions.
For M>1 the absolute eigenvalue sum is finite. Thus R(f) is trace class
on the full Hilbert space, not only on a finite Galerkin subspace.
No assertion that rho(g) itself is trace class is made.

## 4. Compute the trace from its smooth kernel

Periodize f along K_(S,p):

    P_p f(gK)=integral_(K_(S,p)) f(gk)dk.

Compact support in t restricts the sum over valuations to finitely
many terms locally, and unit averaging preserves the stated regularity.
The quotient integral formula shows that R(f) has convolution kernel

    K_f(y,z)=P_p f(y z^-1)

relative to the quotient Haar measure. On the finite-level compact
circle quotient this kernel is smooth, with an absolutely convergent
Fourier series, by the estimates of section 3. Its diagonal integral
therefore equals the trace. Consequently

    Tr R_(S,p)(f)
      =(log p) integral_(K_(S,p)) f(k)dk
      =(log p) sum_(j in Z) integral_(Z_p^*)
                          f(j_p(p^j u))d^*u.       (4.1)

Here d^*u is probability Haar. This proves the tangential orbit factor
as an operator trace. In particular it treats tangential identity
excess by integrating in the whole external group before taking the
trace; it does not restrict the kernel of the identity to its diagonal.

## 5. Coherent chart maps preserve this trace

For S contained in T and p in S, the normalized projection pi_TS
sends K_(T,p) isomorphically onto K_(S,p). Hence it induces a
surjection Y_(T,p) -> Y_(S,p), with kernel the new compact unit group.
Its probability Haar fibers preserve the quotient measure, whose total
mass on both sides is log p.

Pullback J_ST:L^2(Y_(S,p)) -> L^2(Y_(T,p)) is an isometry. For the
scalar pullback P_ST f=f compose pi_TS of P123.023, group integration
over the new units gives the exact operator identity

    R_(T,p)(P_ST f)=J_ST R_(S,p)(f) J_ST^*.

On the new-unit-invariant subspace this is the old representation;
on its orthogonal complement it is zero. Thus traces agree, and the
operators, isometries and trace equalities compose on chart triples.
This is a genuine trace-compatible boundary representation, distinct
from the incompatible internal Jacobian family of P123.031.

## 6. The normal factor is a further coefficient operation

Equation (4.1) has no factor p^(-|j|/2). It is the tangential character,
not yet the full local Weil packet. The normal coordinate of the
stratum carries multiplication by x in Q_p^*, whose Fourier-normalized
local distribution is the one constructed in P123.034.

The next construction must couple that normal coefficient operation to
this integrated representation and prove the resulting trace formula.
Multiplying the right side of (4.1) by a desired Jacobian weight is not
by itself a representation construction. The unit singularity also
requires its specified normal regularization.

Thus one missing piece is now supplied: an actual convolution-preserving,
trace-class tangential representation, with source orbit, kernel,
normalization and chart coherence all explicit. Extending it through
normal coefficients and the higher-zero strata, with the integral
contact determinant and mixed RR, remains necessary for full A/B/C.
No positivity conclusion for D follows from this tangential trace.
