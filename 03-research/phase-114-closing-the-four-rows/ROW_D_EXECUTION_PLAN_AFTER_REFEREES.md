# Row D — execution plan after the full-paper and referee audit

## Goal

Prove, without zeros or a positivity projection as input,

\[
 B_{\rm nuc}(f,f)\le 0\qquad(f\in\mathcal T^0),
\]

including domains, all prime powers, the full Gamma term, propagation over
all support windows and the equality case.

Row D remains open until every item in the final acceptance test below is
proved.  Numerical calculations are used to discover and certify finite
remainders, never to replace the uniform theorem.

## What the five reports change

The reports agree on the exact analytic bottleneck even when they disagree
about the categorical status of rows A--C.  Their useful common content is:

1. the corrected three-block/Feshbach cross is essential;
2. convergence of the return expansion is weaker than the unit budget;
3. the two Tate moments cannot carry an infinite-rank boundary block;
4. a capacity-defined section functor is circular;
5. a mixed Riemann--Roch theorem whose proof uses row-D propagation is
   circular;
6. finite endpoint certificates do not replace a cofinal uniform theorem;
7. the sought constant is exactly one, so a proof should look for a
   conservation/defect identity rather than a lossy estimate.

Claims in the reports that the first unfinished endpoint would by itself
complete propagation are rejected: it is one finite birth, not a uniform
large-birth theorem.

## Authoritative reduction

At a prime-power birth, assume the transported old core is positive and
use the complete reference Cholesky variables of D.170:

\[
 A_N=Y_0R_0^{\dagger/2},\qquad
 y_N=(Y_E-Y_0R_0^\dagger X_0^*X_E)S_E^{\dagger/2},
\]

\[
 D_{{\rm out},N}=I-A_NA_N^*.
\]

The single carrying theorem is

\[
 \boxed{
 y_N=D_{{\rm out},N}^{1/2}v_N,\qquad \|v_N\|\le1.
 }
\tag{G}
\]

The operator \(v_N\) must be source-defined before the enlarged sign is
known.  By D.170, D.190 and Douglas, (G) is equivalent to the exact Schur
capacity and, over an exhaustive family of births, to row D.

## Completed reductions

* The operator map, types and domains are recorded in
  `ROW_D_OPERATOR_MAP.md`.
* The sharp gate and acceptance test are recorded in
  `ROW_D_SHARP_DOUGLAS.md`.
* The direct two-projection route is impossible; its exact residual is in
  `ROW_D_TWO_PROJECTION_AUDIT.md`.
* D.242--D.247 construct the local Fourier-tangent Hodge form, its strict
  primitive contraction and its conservative degree/contact completion.
* D.245--D.246 identify the complete first-order prime and Gamma scores.
* D.248--D.249 construct the positive local Blaschke-delay components.
* D.250 proves that tangent contractions cannot be transported to the
  balanced features through bounded inverses.
* D.251 proves the abstract unitary transfer-defect theorem, but not the
  required wiring.
* D.252 proves that the relative prime score is not a local causal Schur
  defect; the naive local cascade is impossible.
* D.260--D.261 identify the unpaid coherent channel with the centered
  measure \(d\Psi-dx\) and write its complete old-defect cost as one
  operator-valued Green energy, retaining the archimedean cross.
* D.262 inserts the paired Gamma-delay expansion into that cross and proves
  that the assembled archimedean score changes sign.  Thus the individual
  Blaschke colligations cannot be assigned independent positive Douglas
  budgets; only the joint adelic residual is admissible.

## Selected route

The selected route is now the **global four-port feedback route**.  No
other route will be developed in parallel unless this one is eliminated by
an exact obstruction.

### Phase 1 — Explicit feedback equations

For a finite prime-power set and a finite paired Gamma truncation, write one
block system whose ports are:

* odd prime tangents and the global degree input;
* even prime tangents and reduced contacts;
* paired Gamma free-delay/delay states;
* the two Tate ports;
* old and born position-support ports.

Deliverable: an explicit system matrix \(\mathcal U_{N,M}\), with every
source and target space stated, and a direct proof of
\(\mathcal U_{N,M}^*\mathcal U_{N,M}=I\).  Equality of phase derivatives
is not a substitute.

### Phase 2 — Redheffer well-posedness

Specify the internal feedback matrix \(F_{N,M}\).  Prove that
\(I-F_{N,M}\) is invertible on a common compact form core without using
row-D positivity.  Compute the Redheffer transfer operator explicitly.

Failure criterion: if invertibility is equivalent to the enlarged Schur
sign, the proposed feedback is circular and is discarded.

### Phase 3 — Exact state elimination

Eliminate in this fixed order:

1. paired Gamma internal states;
2. degree/contact internal ports;
3. the two Tate ports;
4. old reference states.

Compare the resulting born defect with

\[
 \mathscr R_{E,N}^{\rm D190}
 =I-y_N^*D_{{\rm out},N}^\dagger y_N.
\]

Deliverable: either the exact equality

\[
 \mathscr R_{E,N}^{\rm D190}
 =P_E\Pi_TK_{N,M}^{\rm tr}\Pi_TP_E,
\tag{C}
\]

or a formula for the exact residual \(\mathscr E_{N,M}\).  A norm estimate
is forbidden before \(\mathscr E_{N,M}\) is known.

### Phase 4 — Falsification

Test every algebraic lemma, not merely the final numerical sign, on the
existing off-line Beurling surrogate.  A lemma that survives is retained
as algebra but is not credited with the arithmetic discrimination needed
for D.  The comparison (C), or the sign of its residual, must be the first
place where the actual Euler--Gamma source is used beyond PNT-strength
data.

### Phase 5 — Limits and domains

If (C) holds at finite \(M\), pass in this order:

1. monotone paired-Gamma form limit \(M\to\infty\);
2. \(D_{{\rm out},N}+\varepsilon I\), then
   \(\varepsilon\downarrow0\);
3. closure of the compact smooth primitive core;
4. directed support-window limit.

This order must produce the supported-range inclusion rather than assume
it.

### Phase 6 — Uniform large births

Use the source formula obtained in Phase 3 to prove (G) for every
sufficiently large prime-power birth.  Reparametrize births by the ordered
sequence \(q_j=p^k\), \(\tau_j=\frac12\log q_j\); steps with
\(\Lambda(N)=0\) are omitted only after proving that the operator has no
new contact there.

No uniform strict gap is required.  The target is the sharp inequality
\(\|v_N\|\le1\).

### Phase 7 — Finite remainder

Certify every birth below the asymptotic threshold with reproducible
interval arithmetic, including originating enclosures, cross blocks,
tails and hashes.  The pending \(T=\frac12\log5\) corrected joint Schur
certificate belongs here; it is not the global theorem.

### Phase 8 — Propagation and equality

Combine the certified initial interval, birth continuity, (G) at every
birth, the large-birth theorem and the finite certificates.  Classify
equality from the kernel of the exact transfer defect.  Only the known
polar/radical modes may survive; they must vanish in \(\mathcal T^0\).

## Current exact residual and immediate next calculation

The feedback programme has now eliminated all scalar and separately
positive local realizations.  In the notation of D.261--D.262 the object
to be factored is

\[
 \mathscr R_{N,\varepsilon}
 =\mathcal M_N-\mathfrak q_N^*(D_N+\varepsilon I)^{-1}\mathfrak q_N,
\]

where \(\mathfrak q_N\) is the joint column formed from the centered
Chebyshev measure \(d\Psi-dx\) and the paired Gamma-delay measure.  The
immediate target is an explicit adelic Fourier--Poisson map
\(\mathscr Z_{N,\varepsilon}\), defined without the inverse above, for
which

\[
 \mathscr R_{N,\varepsilon}
 =\mathscr Z_{N,\varepsilon}^*\mathscr Z_{N,\varepsilon}.
\]

The first audit is to transport the finite paired-Gamma truncation and the
finite prime-power measure through the same support/old-short state
equations, calculate the residual symbolically, and test whether it is a
Gram before any limit or norm estimate.  If the residual is not a Gram,
its exact negative-square index and support must be recorded; no local
channel may be reoriented independently.

Historical port reductions leading to this target follow.

Write the finite-dimensional state equations of the D.247 four-port
partial isometry and the Julia prime colligation in a common port order.
Do **not** divide by the tangent filters of D.250.  Connect the global
degree output to the free-delay inputs only after adjoining the contact
output, and retain the Tate ports externally.  Compute the resulting
Redheffer Schur complement symbolically.  The first target is the exact
prime-only residual; Gamma is adjoined only after the prime port algebra is
fixed.

D.253 sharpens this calculation: each meromorphic relative Euler factor
has the exact kernel

\[
 K_{b_r/z}(w,z)=u_r(w)^*u_r(z)-z^{-1}\bar w^{-1},
\]

with exactly one negative square.  Therefore the prime-only port algebra
must first be written as a Pontryagin/J-inner system and converted by the
Potapov--Ginzburg transform after the D.247 degree/contact port change.
An ordinary Schur cascade is not an admissible starting point.

D.254 supplies the explicit non-singular prime port rotation.  With
\(B=(I-rU)^{-1}\) and the even tangent
\(D=\frac{Lr}{2}(I-rU)^{-1}(U+U^*-2r)\), one has

\[
 D^*B+B^*D=L(P_r-I),
\]

and the fixed Hadamard rotation \((B,D)\mapsto((B+D)/\sqrt2,
(B-D)/\sqrt2)\) gives the exact signed balanced prime multiplier.  The
next calculation must compose this rotation with D.247 while leaving the
global degree/contact ports external.

D.255 rules out replacing that matrix problem by a scalar Euler-product
cascade.  The product \(\prod_{p\in S}b_p(z)/z\) has generalized-Schur
index \(|S|\); a fixed Tate correction cannot remove its growing negative
index.  The Potapov--Ginzburg calculation must therefore use the full
matrix-valued D.247 contact output.

D.256 fixes the matrix pivot.  The scalar degree equals the coherent
functional of the contact vector.  Only that rank-one contact component
can be exchanged with degree; the orthogonal \((|S|-1)\)-dimensional
contact block must remain as a positive defect output.  The finite port
calculation must use this coherent/primitive split before adjoining Gamma
or Tate.

D.257 proves the finite tensor coherence behind that split.  Pairing the
tensor Euler derivative with the single dual central tensor cancels all
spectator factors and yields the sum of the local scores with no
cross-prime remainder.  After torsion normalization this central covector
is exactly the coherent degree/contact port.  D.240 already transports the
resulting scalar score through semilocal assembly, Gamma and Tate.  The
remaining comparison is specifically the transport of the conservative
port/defect factorization through support and old-core shorting.

D.258 fixes the functional-analytic type of the coherent port.  It is
rank one only in prime-index space; after Fourier realization and
two-Tate compression it remains an injective infinite-rank \(L^2\) port.
The feedback pivot must therefore be operator-valued and must transport
the complete support commutator.  A scalar degree short is inadmissible.

D.259 prevents a second false closure: the D.244 primitive condition is
pointwise in prime-index fibres, whereas row-D primitivity consists of two
global Tate moments.  The latter does not kill the coherent \(L^2\) port.
The remaining theorem is exactly its sharp capacity estimate after Gamma
and old-core shorting; the orthogonal contact component is already paid.

D.260 gives the source formula for that coherent remainder.  It is the
Mellin--Stieltjes transform of \(d\Psi-dx\), equivalently of
\(A(x)=\Psi(x)-x+1\), with the exact endpoint term.  The next comparison
must factor this measure channel through the old Green defect; PNT-size
bounds are explicitly insufficient.

D.261 inserts this measure into the exact old Green inverse.  The unpaid
capacity is now an explicit double Stieltjes energy with kernel
\(\mathcal K_N(x)^*D_N^\dagger\mathcal K_N(y)\), plus the unseparated
Gamma/endpoint cross.  The next algebraic target is to combine the paired
Gamma-delay representation with this three-term energy and the born budget
before applying any norm estimate.

## Final acceptance test

Row D is complete only when:

1. the contraction in (G) is explicitly constructed from source data;
2. its factorization and norm-one bound are proved on the correct domains;
3. all prime powers and the full Gamma term occur with exact weights;
4. the construction is independent of zeros and of the desired sign;
5. a uniform theorem covers all sufficiently large births;
6. all remaining births have reproducible interval certificates;
7. propagation covers every compact window;
8. the equality case is proved;
9. the primitive inequality follows as a theorem.

Until then the correct status is: **row D open, with a single sharp gate
and one selected source-defined feedback programme**.
