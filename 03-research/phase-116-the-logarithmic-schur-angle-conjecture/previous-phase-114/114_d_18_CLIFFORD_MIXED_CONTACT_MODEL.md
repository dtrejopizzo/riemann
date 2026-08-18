# Row (d): Clifford mixed-contact model

## Status

The ordinary divisor Koszul complex cancels mixed prime channels but also
makes the arithmetic current null-homotopic.  This note constructs the
minimal finite algebraic alternative: a Clifford module cancels cross-prime
terms without declaring the prime operators exact.  It preserves the local
contact, but does not yet produce the global Green curvature or the Hodge
inequality.

## 1. The Koszul collision

On a finite squarefree divisor cube let `N_p` remove the factor `p`.  The
standard differential

\[
 d_K=\sum_pN_p\otimes\varepsilon_p
\]

satisfies

\[
 d_K\iota_p+\iota_pd_K=N_p.                          \tag{1}
\]

Therefore the current

\[
 J=\sum_p(\log p)N_p                                \tag{2}
\]

is null-homotopic.  This is incompatible with the contact determinant,
which requires (2) to survive.  Thus mixed cancellation cannot be obtained
by making every `N_p` exact.

## 2. Clifford replacement

Let `P` be a finite set of primes and let `Cl(P)` be the real Clifford
module with self-adjoint generators `gamma_p` satisfying

\[
 \gamma_p^2=1,\qquad
 \gamma_p\gamma_q+\gamma_q\gamma_p=0\quad(p\ne q).   \tag{3}
\]

On the squarefree divisor Hilbert space the lowering operators satisfy the
double-commutation relations

\[
 N_pN_q=N_qN_p,\qquad N_p^*N_q=N_qN_p^*\quad(p\ne q).
                                                                    \tag{4}
\]

Put

\[
 A_p=N_p+N_p^*,\qquad
 \mathscr D_P=\sum_{p\in P}\sqrt{\log p}\,
                   A_p\otimes\gamma_p.               \tag{5}
\]

### Proposition 2.1

The operator (5) is self-adjoint and

\[
 \mathscr D_P^2
 =\sum_{p\in P}(\log p)A_p^2\otimes1.                \tag{6}
\]

In particular all cross-prime terms cancel, while no `N_p` is declared
null-homotopic.

### Proof

Self-adjointness is immediate.  Expanding the square, the coefficient for
an unordered pair `p != q` is

\[
 \sqrt{\log p\log q}\,A_pA_q\otimes
 (\gamma_p\gamma_q+\gamma_q\gamma_p)=0,
\]

because (4) implies `A_pA_q=A_qA_p`.  The diagonal terms give (6).

### Proposition 2.2 (the current survives)

Let `tau_Cl` be the normalized Clifford trace.  Then each prime operator is
recovered from the first Clifford coefficient:

\[
 (\mathrm{id}\,\otimes\tau_{\rm Cl})
 \bigl((1\otimes\gamma_p)\mathscr D_P\bigr)
 =\sqrt{\log p}\,A_p.                                \tag{7}
\]

Consequently the hermitized current
`J+J*` is a fixed linear contraction of `D_P`; it does not vanish as it
does in Koszul cohomology.

### Proof

The Clifford trace of `gamma_p gamma_q` is `delta_pq`.  Apply it to (5)
and then multiply the result by `sqrt(log p)` before summing over `p`.

## 3. Prime-power towers

The correct local label is the prime, not each individual prime power,
because `Lambda(p^k)=log p`.  For a truncated tower choose commuting normal
operators `A_{p,k}` and form

\[
 \mathscr D_{P,K}
 =\sum_{p\in P}\left(\sum_{k\le K_p}c_{p,k}A_{p,k}\right)
       \otimes\gamma_p.                               \tag{8}
\]

Cross terms between distinct primes still cancel.  Terms within the same
prime tower remain and are encoded in the square of the parenthesis.  This
is the algebraic distinction required by the reduced contact: different
primes are orthogonal, while powers of one prime occupy the same contact
direction.

## 4. What the model does and does not prove

The Clifford construction supplies a non-Koszul mixed coefficient object
with three useful properties:

1. genuine signed cancellation happens before a norm is taken;
2. the prime current remains observable;
3. all finite truncations carry a positive Hilbert metric.

However (6) contains only the finite contact curvature.  It does not
produce the archimedean oscillator module of
`114_d_17_ARCHIMEDEAN_OSCILLATOR_BOUNDARY_MODULE.md`, nor the scalar
counterterm whose exact value is `2A_X+m_0`.  Tensoring the oscillator with
the Clifford module merely adds positive squares and leaves the sharp
coercivity theorem unchanged.

A successful continuation must therefore construct a **superconnection**

\[
 \mathbb A_X=\mathscr D_{P,K}+\nabla_\infty+\mathcal B_X              \tag{9}
\]

whose curvature has a Lichnerowicz identity

\[
 \mathbb A_X^2=
 \text{positive connection Laplacian}
 -B_{\rm nuc}                                                        \tag{10}
\]

on the two-trace kernel.  The boundary term `B_X` must be constructed from
section restriction/duality.  Choosing it by a Schur complement of
`B_nuc`, or by the sign of the finite-window Weyl determinant, would be
circular.

Thus the Clifford model solves the algebraic mixed-prime cancellation
problem but isolates, rather than assumes, the remaining geometric
superconnection problem.

