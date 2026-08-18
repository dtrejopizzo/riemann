# 107.218 -- Rooted inclusion and cellular subdivision do not define one descent map

## 1. The two existing transitions

Let \(L' = dL\).  Phase 107 currently has two canonical transition
rules.

The rooted transition of 107_159--107_160 retains every old root with
its value unchanged:

\[
 \iota_{L,L'}:\mu_L\hookrightarrow\mu_{L'},
 \qquad \zeta\longmapsto\zeta.
 \tag{1.1}
\]

The cellular subdivision of 107_169 is induced by

\[
 \phi_{L,L'}:
 \mathbb Z[x]/(x^L-1)\longrightarrow
 \mathbb Z[x']/(x'^{L'}-1),
 \qquad x\longmapsto x'^d.
 \tag{1.2}
\]

On character points, the contravariant map of (1.2) is

\[
 \phi_{L,L'}^*:\mu_{L'}\longrightarrow\mu_L,
 \qquad \zeta'\longmapsto(\zeta')^d.
 \tag{1.3}
\]

## 2. Compatibility criterion

Restrict (1.3) to the old rooted labels through (1.1).  For
\(\zeta\in\mu_L\),

\[
 \phi_{L,L'}^*\iota_{L,L'}(\zeta)=\zeta^d.
\]

Therefore the old label is preserved if and only if

\[
 \zeta^{d-1}=1.
 \tag{2.1}
\]

For a primitive label of order \(n\mid L\), this is equivalent to
\(n\mid d-1\).  It fails for generic level enlargements; for example,

\[
 L=3,quad L'=6,quad d=2,quad
 \zeta_3\longmapsto\zeta_3^2\ne\zeta_3.
 \tag{2.2}
\]

### Theorem 2.1 (transition no-go)

The rooted open-and-closed inclusions of 107_160 and the cellular
subdivision maps of 107_169 do not form one compatible directed system
on nontrivial character summands.

Moreover, replacing (1.2) by \(x\mapsto x'\) cannot repair the problem:
that assignment does not descend to the quotient when \(L<L'\), since
\(x'^L-1\ne0\) in \(\mathbb Z[x']/(x'^{L'}-1)\).

The obstruction already occurs in one ruling and therefore persists on
the square.

## 3. Effect on the twisted H1

The cohomology groups of 107_217 are indexed by the character pair
\((\zeta^u,\zeta^v)\).  Under cellular subdivision they are pulled to
\((\zeta^{du},\zeta^{dv})\), while rooted descent retains
\((\zeta^u,\zeta^v)\).  Their effective character orders, and hence the
torsion norm

\[
 \Phi_m(1)^{\varphi(n)/\varphi(m)},
\]

can differ.  Thus the finite-level groups of 107_217 do not yet define a
directed divisor cohomology theory via the transitions of 107_169.

This does not invalidate either finite-level construction.  It rejects
their naive identification.  A surviving globalization must use one of:

1. restriction/transfer correspondences retaining both maps;
2. a pro-system indexed contravariantly by the power maps;
3. a cellular model built directly on the disjoint cyclotomic
   normalization rather than on \(\mu_L\).

Choosing one of these is new structure and must include a proof that the
resulting \(H^1\) stabilizes for each divisor.

## 4. Falsifier

`107_218_rooted_inclusion_vs_cellular_subdivision_no_go.sage` uses actual
cyclotomic fields for fixed divisibilities.  It checks the power-map
criterion, exhibits moved primitive labels, verifies the exceptional
fixed labels, and rejects the attempted map \(x\mapsto x'\) by evaluating
the source relation in the target quotient.

