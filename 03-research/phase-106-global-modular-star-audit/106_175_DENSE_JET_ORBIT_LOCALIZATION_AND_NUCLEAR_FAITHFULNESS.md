# 106.175 — Dense jet-orbit localization and nuclear faithfulness

## 1. Purpose

The remaining comparison after 106.174 has two logically distinct parts:

1. fixed-orbit localization must be faithful in the nuclear topology of
   the CCM cokernel;
2. the positive Tate middle metric must equal the CCM Rosati trace
   pairing.

The first part can be proved without the second.  Raw values at prime
return lengths are not topologically faithful on a Schwartz space.  The
scaling action, however, supplies every translate by
\(\log\mathbb Q_+^\times\), and its infinitesimal generator supplies all
jets.  Because that translation group is dense, the resulting jet-orbit
observation reproduces the exact Schwartz seminorms.

This note proves the corresponding topological embedding and its quotient
consequence.  It closes nuclear faithfulness on the scalar diagonal
Morita component of the CCM target.  The metric identity remains.

## 2. The scalar CCM target in logarithmic coordinates

For \(\mathbb Q\), the idele class exact sequence has the canonical
fundamental domain

\[
 \Delta_{\mathbb Q}=\widehat{\mathbb Z}^{\times}
                    \times\mathbb R_+^\times.                \tag{1}
\]

After a compact-character decomposition in the first factor and the
coordinate \(t=\log|x|\) in the second, the strong scalar Schwartz target
of CCM is a direct sum of copies of \(\mathcal S(\mathbb R)\).  It is
therefore enough to prove the assertion in one compact-character sector.

Put

\[
 G=\log\mathbb Q_+^\times
   =\operatorname {span}_{\mathbb Z}\{\log p:p\text{ prime}\}.
                                                                    \tag{2}
\]

The group \(G\) is countable and dense in \(\mathbb R\).

## 3. The complete jet-orbit observation

For \(f\in\mathcal S(\mathbb R)\), define

\[
 \boxed{
 \mathcal O_\infty f
 =\bigl(f^{(n)}(g)\bigr)_{g\in G,\ n\ge0}.}                  \tag{3}
\]

Let \(\mathscr J_G\) be the vector space of arrays
\(a=(a_{g,n})\) for which

\[
 q_{m,n}(a)=\sup_{g\in G}(1+|g|)^m|a_{g,n}|<\infty
 \qquad(m,n\ge0).                                           \tag{4}
\]

On \(\mathcal S(\mathbb R)\), use the equivalent standard seminorms

\[
 p_{m,n}(f)=\sup_{t\in\mathbb R}(1+|t|)^m|f^{(n)}(t)|.        \tag{5}
\]

### Theorem 3.1 — Exact recovery of the Schwartz topology

For every \(f\in\mathcal S(\mathbb R)\) and every \(m,n\ge0\),

\[
 \boxed{q_{m,n}(\mathcal O_\infty f)=p_{m,n}(f).}             \tag{6}
\]

Consequently \(\mathcal O_\infty\) is injective and is a topological
isomorphism from \(\mathcal S(\mathbb R)\) onto its image.

#### Proof

For fixed \(m,n\), the function

\[
 t\longmapsto(1+|t|)^m|f^{(n)}(t)|                           \tag{7}
\]

is continuous.  Since \(G\) is dense, its supremum over \(G\) equals its
supremum over \(\mathbb R\).  This is (6).  If all zeroth jets vanish,
continuity and density give \(f=0\); hence the map is injective.  Equality
of every defining seminorm proves the topological assertion. \(\square\)

The derivatives in (3) are not extra arithmetic data.  If \(D=d/dt\) is
the infinitesimal generator of scaling and \(T_gf(t)=f(t-g)\), then

\[
 f^{(n)}(g)=(-1)^n(D^nT_{-g}f)(0).                            \tag{8}
\]

Thus (3) consists precisely of translated fixed-orbit observations and
their scaling-generator descendants.

## 4. Closed-range consequence

Let \(V\subset\mathcal S(\mathbb R)\) be any linear subspace, and let
closures be taken in the Schwartz topology and in the transported
topology of \(\operatorname {Ran}\mathcal O_\infty\), respectively.

### Theorem 4.1 — Nuclear quotient faithfulness

\[
 \boxed{
 \mathcal O_\infty^{-1}
 \left(\overline{\mathcal O_\infty(V)}\right)=\overline V.}  \tag{9}
\]

Therefore \(\mathcal O_\infty\) induces an injective topological map

\[
 \boxed{
 \mathcal S(\mathbb R)/\overline V
 \longrightarrow
 \operatorname {Ran}\mathcal O_\infty/
 \overline{\mathcal O_\infty(V)}.}                          \tag{10}
\]

It is an isomorphism onto the displayed quotient.

#### Proof

Theorem 3.1 makes \(\mathcal O_\infty\) a homeomorphism onto its image.
Homeomorphisms preserve closure, which proves (9).  The universal property
of the quotient gives (10), and (9) gives injectivity. \(\square\)

This is the step that fails for an \(L^2\) observation: point evaluation
and its jets are not continuous there, and a dense multiplier range has
zero reduced cokernel.  No Hilbert completion is used in (9)--(10).

## 5. Compact-character sectors and Morita trace

Let \(K=\widehat{\mathbb Z}^{\times}\).  The strong CCM scalar target is
nuclear in the compact variable and Schwartz in \(t\).  Peter--Weyl
decomposition gives rapidly decreasing compact-character coefficients
\(f_\chi(t)\).  Define

\[
 \mathcal O_{\rm CCM}f
 =\left((f_\chi)^{(n)}(g)\right)_{\chi,,g\in G,,n\ge0},     \tag{11}
\]

with the usual rapid seminorms in \(\chi\) and the seminorms (4) in
\((g,n)\).  Applying Theorem 3.1 sector by sector gives:

### Corollary 5.1 — Faithful scalar orbit localization

The map (11) is a topological embedding of the complete strong scalar CCM
target.  If \(\mathcal V\) is the closed range of the scalar diagonal
restriction map \(\operatorname {Tr}\circ\rho\), then

\[
 \boxed{
 \mathbf S(C_{\mathbb Q})/\mathcal V
 \hookrightarrow
 \mathcal O_{\rm CCM}\mathbf S(C_{\mathbb Q})/
 \overline{\mathcal O_{\rm CCM}\mathcal V}}                 \tag{12}
\]

is injective and is an isomorphism onto its image quotient.

For \(\mathbb Q\), CCM's splitting identifies the trace-class matrix
field target with its scalar diagonal target by cyclic Morita equivalence.
The matrix trace is the forward morphism; a fixed rank-one matrix unit is
a chain section, with the standard matrix contraction providing the
cyclic homotopy.  Hence (12) proves faithfulness on the scalar diagonal
Morita component, rather than merely on degree-zero functions.

## 6. Relation with the prime coefficient construction

The observation group in (2) is exactly the group generated by the prime
times of 106.154.  Theorem 5.2 there proves that the translated prime
increments generate the full increment sigma-algebra of the common
Cauchy dilation.  The present theorem is the nuclear deterministic
counterpart:

\[
 \boxed{
 \text{prime times + all scaling translates + jets}
 \quad\Longrightarrow\quad
 \text{faithful Schwartz observation}.}                     \tag{13}
\]

Raw prime-power values alone do not give (6).  The translates and jets
are indispensable, and both are already supplied by the equivariant CCM
action.  No Paley--Wiener zero-counting or sampling inequality is used.

The local maps of 106.173 and the primitive projector of 106.174 may now
be applied coefficientwise to (11).  The two conclusions must not be
conflated: 106.173 proves surjectivity onto local middle coefficients,
whereas the present theorem proves injectivity only while the full jet
array (11) is retained.  Proving that passage from that faithful jet array
to the Tate middle target loses no CCM class remains part of the global
chain comparison.

## 7. What remains after nuclear faithfulness

The result does not yet prove that the positive Tate middle metric is the
CCM trace pairing.  A topological embedding can carry many inequivalent
quadratic forms.  The outstanding identity is

\[
 \boxed{
 \mathfrak h_{\rm Ros}(u,v)
 =\left\langle
   \operatorname {Loc}^{\rm mid}u,
   \operatorname {Loc}^{\rm mid}v
  \right\rangle_{\rm Tate+\Gamma+polar}.}                   \tag{14}
\]

The prime coefficient, parity, scalar finite part, local surjectivity, and
faithful nuclear observation entering (14) have now been constructed.
The remaining work is a chain-level Green identity which both identifies
the kernel lost in passing from the jet array to the middle target and
couples the
archimedean/polar boundary to the two Tate balance maps.  Positivity would
then follow from the already positive target metric, rather than from an
estimate of the Weil form.

## 8. Falsification controls

1. A non-Euler Dirichlet series has no prime-time group generated by local
   factors together with the coefficient descent of 106.173--106.174.
2. Density of \(G\) proves only topological faithfulness; it proves no sign
   and cannot by itself imply RH.
3. The topology in (4) deliberately retains all Schwartz seminorms.  If it
   is replaced by an \(\ell^2\) sample norm, Theorem 4.1 need not hold.
4. Equation (14), not (12), is the remaining force-bearing assertion.

## 9. Status

Proved without RH or zero input:

* exact recovery of every Schwartz seminorm from dense translated jets;
* a topological embedding of every compact-character sector;
* preservation of closed restriction ranges and injectivity on their
  quotients;
* compatibility with the prime-generated time group;
* nuclear scalar-diagonal faithfulness of the complete jet observation
  after cyclic Morita reduction.

Still required:

* the complete Gamma/polar Green identity;
* proof that the jet-to-middle kernel is exactly the CCM restriction
  range;
* the Rosati/Tate metric equality (14);
* verification that the resulting polarized comparison intertwines the
  full degree-one scaling trace.

## 10. Primary input

The restriction morphism, strong scalar Schwartz target, closure of its
range, cyclic Morita trace, and resulting degree-one cokernel are from
A. Connes, C. Consani, and M. Marcolli,
*The Weil proof and the geometry of the adeles class space*, 2007.
The dense-jet topological embedding (3)--(10) is proved directly here.
