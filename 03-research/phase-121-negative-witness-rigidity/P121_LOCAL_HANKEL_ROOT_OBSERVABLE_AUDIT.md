# Phase 121 -- local Hankel root observable audit

## Status

The rank-one contact law of a degree-one Euler factor has an exact
non-positive-lift consequence: the self-commutator of its causal history
operator is a rank-one observation of the divisor root.  A shifted
degree-two factor has generically rank two, so this is a genuine
`zeta/Xi_a` discriminator.

The observable does not yet close a first-contact state.  The physical Real
involution supplies two causal history vectors, one for each time
orientation; it does not identify them as the same vector in one unilateral
tower.  Making that identification is exactly equality-state annular
transport.  Thus the calculation sharpens the terminal target but does not
prove the global square.

## 1. Exact rank-one root commutator

Let `S` be the unilateral shift on `ell2(N_0)`, let `0<r<1`, and define

\[
 A_r=rS(I-rS)^{-1}=\sum_{j\geq1}r^jS^j.             \tag{1.1}
\]

For the degree-one Euler factor at `p`, `r=p^{-1/2}` and the logarithmic
connection is `(log p)A_r`.

### Theorem 1.1

Put

\[
 v_r={1\over\sqrt{1-r^2}}(r,r^2,r^3,\ldots).
\]

Then

\[
 \boxed{A_r^*A_r-A_rA_r^*=v_r\otimes v_r.}          \tag{1.2}
\]

In particular

\[
 \|A_rh\|^2-\|A_r^*h\|^2
 ={1\over1-r^2}\left|\sum_{j\geq0}r^{j+1}h_j\right|^2. \tag{1.3}
\]

#### Proof

For `i<=j`, direct summation gives

\[
 \langle A_re_i,A_re_j\rangle={r^{j-i+2}\over1-r^2},
\]

whereas

\[
 \langle A_r^*e_i,A_r^*e_j\rangle
 ={r^{j-i+2}(1-r^{2i})\over1-r^2}.
\]

Their difference is `r^(i+j+2)/(1-r^2)`, the `(i,j)` entry of
`v_r tensor v_r`.  Symmetry handles `j<i`.  QED.

This is the operator form of the vanishing of every `2 x 2` Hankel minor
of the geometric prime-power sequence.  Unlike the causal Moebius
connection, whose diagonal is zero, (1.2) really creates a root
observation by running once down and once up the unilateral tower.

## 2. It separates a degree-two shifted Euler factor

For two distinct radii `r_1,r_2 in (0,1)`, put

\[
 A=A_{r_1}+A_{r_2}.                                  \tag{2.1}
\]

The same matrix calculation, polarized in `r_1,r_2`, shows that
`A^*A-AA^*` has range contained in

\[
                         \operatorname {span}\{v_{r_1},v_{r_2}\}. \tag{2.2}
\]

Its two-by-two principal determinant is nonzero whenever `r_1 ne r_2`;
hence the range is generically two-dimensional.  For

\[
 \Xi_a(s)=\xi(s+a)\xi(s-a),
\]

the two local radii are `p^(-1/2-a)` and `p^(-1/2+a)`.  Thus the rank-one
root observable is special to a degree-one local Euler factor and fails
for every `a ne 0`.  This passes the phase-121 synthetic firewall.

## 3. Why the root observable does not yet annihilate a zero mode

Identity (1.3) would kill the root history if the equality-state equations
gave one vector `h` satisfying

\[
                         \|A_rh\|=\|A_r^*h\|.        \tag{3.1}
\]

The physical equations do not give (3.1).  The right-oriented Euler
resolvent creates a causal history `h_+` based at the left edge of the
window.  Real reflection creates a second causal history `h_-` based at
the right edge and gives only

\[
                         \|A_rh_+\|=\|A_r^*h_-\|.    \tag{3.2}
\]

There is no source-level identity `h_+=h_-`.  Their difference is the
incoming exterior history in v94 (451)--(455), equivalently the annular
amplitude in (441)/(446).  Substituting `h_-` for `h_+` in the second norm
of (1.3) deletes precisely that amplitude.

The same fact appears in finite depth.  Reversing a truncated unilateral
tower exchanges its two endpoints, so its self-commutator contains a
positive root term and a negative terminal term.  Cancellation of the
terminal term in the cofinal tower is not a formal consequence of Real
symmetry; it is the missing boundary transport.

Consequently the implication

\[
 \text{first contact}\Longrightarrow
 \langle[A_r^*,A_r]h_+,h_+\rangle=0                \tag{3.3}
\]

is not available.  If it were, Theorem 1.1 would force the rank-one root
coordinate to vanish prime by prime and the causal recursion would kill
the source.  Equation (3.3), however, is exactly the sought identification
of the two oriented histories, not a consequence of their separate
equations.

## 4. Corpus comparison and verdict

The phase-120 Fock/CAR route constructs positive free-vacuum carriers and
stops at arithmetic descent/reflection.  The phase-121 CMO audit proves
that a one-sided logarithmic connection has no root diagonal.  Theorem 1.1
is the exact bridge between those observations: adding the adjoint creates
the missing root, but only after the two physical histories have been
identified.

No phase-1--120 occurrence of the explicit formula (1.2) as an
equality-state root observable was found.  Its local rank is a genuine
Euler-degree discriminator.  Its terminal identification is nevertheless
the already isolated annular transport theorem, so it does not close F2 or
the global square.

