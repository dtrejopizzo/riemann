# 107.164 -- No additive lift descends through Newton reduction

## 1. Question forced by 107_163

The integral monoid algebra in 107_163 gives exact abelian equations for
the rational Frobenius congruences.  To use them as a Cech differential
for the reduced square of the Arithmetic Site, they would have to depend
only on the reduced Newton polygon, not on the chosen monomial support.
This note proves that such an additive descent is impossible.

## 2. Idempotent obstruction

**Lemma.**  Let \(M\) be an idempotent commutative monoid and \(A\) an
abelian group.  Every monoid homomorphism \(f:M\to A\) is zero.

**Proof.**  For every \(x\in M\),

\[
 f(x)=f(x+x)=f(x)+f(x),
\]

so \(f(x)=0\). \(\square\)

Both the unreduced Boolean tensor square (addition by union) and the
reduced Newton semiring (addition by convex hull of union) are
idempotent.  Therefore neither admits a nonzero additive homomorphism
to the additive group underlying an Eilenberg--MacLane module.

## 3. Stronger support-level collapse

The obstruction persists even if one first replaces a finite support
by its formal integral sum.  Let

\[
 L(S)=\sum_{u\in S}e_u
\]

for finite \(S\subset\mathbb Z^2\), and suppose that \(L(S)=L(S')\)
whenever the upper Newton polygons agree:

\[
 \mathrm{conv}(S)+\mathbb R_+^2
 =\mathrm{conv}(S')+\mathbb R_+^2.
 \tag{3.1}
\]

**Theorem.**  Relations (3.1) kill every basis vector \(e_w\).

**Proof.**  Fix \(w=(a,b)\), and set

\[
 u=(a-1,b+1),\qquad v=(a+1,b-1).
\]

The points \(u,v\) are incomparable for the product order and \(w\) is
their midpoint.  Consequently

\[
 \mathrm{conv}\,\{u,v\}+\mathbb R_+^2
 =\mathrm{conv}\,\{u,w,v\}+\mathbb R_+^2.
\]

The required additive identification gives

\[
 e_u+e_v=e_u+e_w+e_v,
\]

and cancellation in an abelian group yields \(e_w=0\).  Since \(w\)
was arbitrary, the quotient is zero. \(\square\)

This argument uses actual two-dimensional Newton geometry; it is not
the general idempotence lemma in disguise.

## 4. Consequence for the Phase 107 lift

The map \(\Lambda_{n,m}\) of 107_163 is canonical on the **enriched
unreduced monomial support**.  It is not a functor of the reduced Newton
polygon alone and must not be described as an additive linearization of
\(\mathrm{Conv}(\mathbb Z^2)\).

Thus the proposed route

\[
 \text{reduced Newton square}
 \longrightarrow
 \text{abelian Cech complex}
\]

is closed.  A viable route must instead keep a support/phase enhancement
\(\widetilde{\mathcal O}\) above the reduced square:

\[
 \widetilde{\mathcal O}
 \xrightarrow{\mathrm{Newt}}
 \mathcal O_{\rm red},
\]

where `Newt` is a non-additive tropical shadow after passing to signed
abelian coefficients.  The kernels of 107_163 live upstairs.  The
downstairs Newton polygon may control convex geometry, but it cannot
determine the abelian cohomology object.

This does not invalidate the local kernel theorem of 107_163.  It fixes
its exact categorical level and prevents a false claim that the 2022
integer dimension applies directly to the reduced characteristic-one
structure sheaf.

## 5. Falsifier

The verifier uses finite windows in \(\mathbb Z^2\).  For every interior
test point it constructs the incomparable endpoints above, verifies
equality of the upper Newton polygons exactly by linear inequalities,
and checks that the induced abelian relation kills that point.  A free
support lift without Newton reduction is retained as a negative control.
