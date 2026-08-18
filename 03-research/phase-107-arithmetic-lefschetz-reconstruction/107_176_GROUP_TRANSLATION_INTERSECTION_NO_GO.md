# 107.176 -- Ordinary group translations cannot realize the local explicit term

## 1. Published local mechanism

The 2026 arithmetic-Jacobian construction interprets the local term in
the explicit formula as

\[
 \mathrm{Tr}_{\rm distr}(x\mapsto ux\text{ on }\mathbb Q_v)
 =\frac1{|1-u|_v}.
 \tag{1.1}
\]

The fixed point is the origin in the **transverse linear space** to an
idele-translation orbit in the adelic Picard monoid.  Formula (1.1) is
the inverse determinant of \(1-u\) on that normal direction.

The same paper explicitly warns that translations on a group have no
nontrivial fixed points.  The fixed strata needed by the trace formula
occur because the adelic target is a monoid with boundary.

## 2. Translation equalizers on group schemes

Let \(G\) be any separated group scheme over a field, let \(a\in G\),
and let \(\tau_a(x)=x+a\).  The graph--diagonal equalizer is

\[
 \Gamma_{\tau_a}\cap\Delta
 =\{x:x+a=x\}.
\]

Cancellation in the group law gives

\[
 \Gamma_{\tau_a}\cap\Delta=
 \begin{cases}
  \varnothing,&a\neq0,\\
  \Delta,&a=0.
 \end{cases}
 \tag{2.1}
\]

Thus the intersection is either empty or improper of positive
dimension.  It is never a proper zero-dimensional intersection carrying
the nonzero finite multiplicity \(1/|1-u|_v\) for \(u\neq1\).

This applies in particular to:

1. abelian varieties and their products;
2. Jacobians of curves of every genus;
3. the complex Tate curves
   \(E_p=\mathbb C^\times/p^\mathbb Z\) constructed in the 2026
   absolute-geometry paper;
4. the everywhere-good CM surface of `107_173`.

Passing from \(\mathbb C^\times\) to \(E_p\) makes multiplication by
the quotient generator \(p\) the identity.  Its graph is therefore the
diagonal itself, not a proper Frobenius graph.

## 3. Incompatibility with the explicit formula

For example, at \(v=5\) and \(u=2\),

\[
 {1\over|1-2|_5}=1,
\]

whereas every nonidentity translation on a smooth group has

\[
 \Gamma_{\tau_a}\cdot\Delta=0.
\]

At \(u=1\), the distributional expression is singular and the group
equalizer is the whole diagonal.  Neither side supplies an ordinary
proper intersection there.  The two failures have the same geometric
message: the relevant local term is an equivariant normal contribution,
not an ordinary fixed-point count on a smooth group object.

## 4. No-go and required replacement

Therefore no realization that replaces the adelic Picard **monoid** by
a smooth Picard group, abelian variety, or local Tate curve and then uses
ordinary graph--diagonal intersection can realize row (c).

This does not reject the published distributional trace formula.  It
fixes the interface a successful arithmetic surface must provide:

\[
 \boxed{
 \text{a boundary fixed stratum together with its transverse
 scaling representation and an equivariant local trace}.}
\]

Consequently the next admissible construction is not another smooth
group square.  It must compactify or geometrize the monoidal boundary,
retain the normal coordinate \(\mathbb Q_v\), and prove that its local
equivariant intersection is (1.1).  Only after that comparison may an
arithmetic Hodge pairing be attached.

## 5. Real-data falsifier

The Sage verifier uses five actual finite-field groups: four elliptic
curves, including the fixed Paper-0 control and a supersingular curve,
and the Jacobian of a genus-2 Artin--Schreier curve.  It enumerates every
rational point and checks (2.1) for every translation.  It separately
checks the nonzero local factor at \((v,u)=(5,2)\).  Any nonidentity
translation with a fixed point returns `VERDICT: NO`.
