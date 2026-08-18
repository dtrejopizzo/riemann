# D.41 — Two-strip Gamma line and the Meyer cokernel

## 1. The correct topological replacement for `E/Xi E`

Let `E` be the Mellin transform of `H_-`.  Thus `E` consists of entire
functions which are Schwartz on every vertical line.  Introduce the two
half-strip spaces.  Here ``meromorphic'' means meromorphic on the whole
plane; the displayed half-plane specifies where Schwartz estimates are
imposed, while the allowed pole divisor lies in the opposite half-plane:

\[
 \mathcal U_+=\{u_+:\ u_+\text{ is meromorphic, vertically Schwartz for }
     \operatorname{Re}s\ge1/2,\text{ with poles only at }-2\mathbb N_0\},
                                                               \tag{1.1}
\]

\[
 \mathcal U_-=\{u_-:\ u_-\text{ is meromorphic, vertically Schwartz for }
     \operatorname{Re}s\le1/2,\text{ with poles only at }1+2\mathbb N_0\}.
                                                               \tag{1.2}
\]

The topology is intended to be given by Schwartz seminorms on compact
closed vertical substrips, together with a topology on the locally finite
residue coordinates.  D.40 proves the finite-level/pro residue statement,
but does not identify the inverse limit with a particular Frechet sequence
space.  Until that topology is constructed, `U_+` and `U_-` are
meromorphic section spaces and pro-Frechet objects, not yet audited Frechet
spaces to which the open-mapping theorem may be applied.  Put

\[
 \gamma(s)=\pi^{1/2-s}
 \frac{\Gamma(s/2)}{\Gamma((1-s)/2)}.                \tag{1.3}
\]

Define the Gamma line of two-strip sections by

\[
 \mathcal L_\gamma=
 \{(u_+,u_-)\in\mathcal U_+\times\mathcal U_-:
   u_-=\gamma^{-1}u_+\text{ meromorphically}\}.      \tag{1.4}
\]

The allowed poles in (1.1)--(1.2) are forced by the divisor of `gamma`.
They are exactly the residue objects constructed in D.40.

The primitive line is the algebraically defined subspace

\[
 \mathcal L_\gamma^0=
 \{(u_+,u_-)\in\mathcal L_\gamma:
             u_+(1)=0,\ u_-(0)=0\}.                 \tag{1.5}
\]

At each finite residue level it is closed.  Calling it closed in a single
infinite Frechet topology depends on the topology theorem stated above.
These are the two polar/ruling conditions.  Without (1.5), multiplication
by zeta lands in Meyer's pole extension `H_cup`, not necessarily in the
entire numerator `H_-`.

## 2. Characteristic section

For `(u_+,u_-) in L_gamma^0`, set

\[
 \sigma_\zeta(u_+,u_-)
 :=\zeta(s)u_+(s)=\zeta(1-s)u_-(s).                 \tag{2.1}
\]

The equality follows from
`zeta(1-s)=gamma(s)zeta(s)`.  Here is the complete local order check.

* At `s=-2n`, `n>=1`, the trivial zero of `zeta(s)` cancels the allowed
  simple pole of `u_+`.
* At `s=1+2n`, `n>=1`, the trivial zero of `zeta(1-s)` cancels the allowed
  simple pole of `u_-`.
* At `s=0`, `zeta(s)` is regular and nonzero.  Since `gamma^{-1}` has a
  simple zero there, the condition `u_-(0)=0` forces the possible residue
  of `u_+` at zero to vanish.  Simultaneously it cancels the pole of
  `zeta(1-s)` in the reflected expression.
* At `s=1`, the symmetric argument with `u_+(1)=0` removes a possible pole
  of `u_-` and cancels the pole of `zeta(s)`.

Thus the common function in (2.1) is entire.
Polynomial vertical bounds for zeta
on fixed strips show that it belongs to `E`.

Conversely, let `h in E`.  Meyer's range theorem says that

\[
 h\in Z\mathcal H_\cap                              \tag{2.2}
\]

if and only if

\[
 u_+=h/\zeta(s)\in\mathcal U_+,qquad
 u_-=h/\zeta(1-s)\in\mathcal U_-.                  \tag{2.3}
\]

The functional equation gives the gluing relation (1.4).  Hence (2.1)
induces an algebraic isomorphism onto the Poisson relation space, compatible
with every finite residue level:

\[
 \boxed{
 \sigma_\zeta:\mathcal L_\gamma^0
   \xrightarrow{\sim}_{\mathrm{alg}}Z\mathcal H_\cap.}            \tag{2.4}
\]

Meyer's closed-range theorem proves that the image on the right is closed
and gives it the quotient topology transported from `H_cap`.  His
set-theoretic divisibility characterization does not, by itself, prove
that this topology equals the independently proposed residue/strip
topology on the left.  To upgrade (2.4) to a topological isomorphism one
must prove:

1. that the infinite residue section spaces are Frechet, or work entirely
   in an exact pro-category;
2. continuity of division by zeta from the Meyer range topology to both
   strip topologies, uniformly across cancelled zeros;
3. continuity of inverse multiplication with the chosen residue
   seminorms.

These estimates are not contained in D.40--D.41.  Thus (2.4) proves the
algebraic/pro presentation and formulates, rather than completes, the
independent topological comparison.

Algebraically, and topologically after transporting the Meyer range
topology to the source, the odd row-C object has the presentation

\[
 \boxed{
 0\longrightarrow\mathcal L_\gamma^0
 \xrightarrow{\ \sigma_\zeta\ }E
 \longrightarrow V\longrightarrow0,
 \qquad V=\mathcal H_-^0.}                          \tag{2.5}
\]

This is the correctly weighted replacement for the naive quotient
`E/Xi E`.  With the independently proposed strip/residue topology, the
comparison left open in D.40 remains a theorem to prove.

## 3. Scaling and reflection

Scaling acts by `(lambda_t h)(s)=t^s h(s)` on every term of (2.5).
It preserves the residue divisors and commutes with `sigma_zeta`.
Reflection exchanges the two charts:

\[
 (u_+,u_-)(s)\longmapsto(u_-(1-s),u_+(1-s)).         \tag{3.1}
\]

Together with complex conjugation this is the source-defined Tate real
duality.  Reflection does not commute literally with scaling.  Direct
substitution gives the weight-one Tate-similitude law

\[
 \mathfrak r\lambda_t
 =t\,\lambda_{t^{-1}}\mathfrak r.                  \tag{3.2}
\]

Thus (2.5) is a scaling-equivariant range--cokernel triangle, and
reflection is equivariant after the weight-one Tate twist.  It is built
without the nontrivial zero divisor.

Taking the transpose after the construction recovers generalized
evaluation at the zeros, as in Meyer; those evaluations are not used to
define (2.5).

## 4. The canonical boundary metric and its exact limitation

On the critical boundary, (1.3) satisfies

\[
 |\gamma(1/2+i\tau)|=1.                              \tag{4.1}
\]

Hence the two charts have the common positive boundary norm

\[
 \|(u_+,u_-)\|_\partial^2
 =\frac1{2\pi}\int_{\mathbb R}
   |u_+(1/2+i\tau)|^2d\tau
 =\frac1{2\pi}\int_{\mathbb R}
   |u_-(1/2+i\tau)|^2d\tau.                         \tag{4.2}
\]

This norm is scaling invariant after central normalization and contains
the Gamma scattering exactly.  It is a genuine positive metric on the
source line `L_gamma^0`.

It does not give a faithful metric on `V`.  Equip the target `E` with its
ordinary critical-boundary `L^2` norm.  The required density can be proved
without assuming that the two-strip source is already a graph core for the
unbounded multiplier `zeta`.

For every `phi in E`, put

\[
 h(s)=\Xi(s)\phi(s).                                  \tag{4.3}
\]

Then `h in Z H_cap`.  Indeed, on the right strip, `h/zeta(s)` is
`s(s-1)/2` times the completed Gamma factor and `phi`; on the left strip
the analogous assertion follows from `Xi(s)=Xi(1-s)`.  Both quotients are
vertically Schwartz by Stirling estimates.

The critical-line traces of `E` are dense in `L^2(R)`.  For example, the
functions

\[
 s\longmapsto\exp((s-1/2-ia)^2),\qquad a\in\mathbb R,              \tag{4.4}
\]

belong to `E` and restrict to translates of a Gaussian; their linear span
is dense in `L^2`.  Moreover `Xi(1/2+i tau)` is a bounded measurable
multiplier and is nonzero almost everywhere.  The multiplication-range
lemma therefore gives dense range for `M_Xi` on `L^2`.  Since `M_Xi` is
bounded and the boundary traces of `E` are dense,

\[
 \overline{\Xi E}^{L^2}=L^2.
\]

Finally `Xi E subset Z H_cap=ran(sigma_zeta)`.  Thus the target Hilbert
cokernel is zero:

\[
 \overline{\operatorname{ran}\sigma_\zeta}^{\,L^2}=L^2,
 \qquad
 L^2/\overline{\operatorname{ran}\sigma_\zeta}=0.   \tag{4.5}
\]

This recovers D.26 inside the algebraically correctly typed Gamma line and
proves the ordinary-boundary Hilbert collapse.  It does not repair the
missing equivalence between the independent two-strip residue topology and
the Meyer quotient topology.

## 5. Remaining Hodge datum

The exact remaining datum is a positive completion of the **cokernel
topology** in (2.5), not of its almost-everywhere boundary values.  It must
retain the generalized evaluation classes, make centrally normalized
scaling unitary, and identify Hilbert traces with the nuclear trace of row
C.  Any norm obtained only from (4.2) kills the entire cokernel; any norm
obtained by summing evaluations at the nontrivial zeros is spectral and
circular.

Thus D.41 completes the algebraic/pro Gamma-line comparison and proves the
ordinary `L^2` collapse.  Two row-D obligations remain, in order:

1. prove that the independent two-strip residue topology agrees with
   Meyer's closed-range quotient topology, or formulate and prove the
   entire comparison in an exact pro-category;
2. construct a source-defined reproducing or graph norm on the cokernel of
   (2.5) that is faithful, scaling invariant and trace compatible, then
   prove that its Tate form is the pullback already identified with
   `B_nuc` in D.32.
