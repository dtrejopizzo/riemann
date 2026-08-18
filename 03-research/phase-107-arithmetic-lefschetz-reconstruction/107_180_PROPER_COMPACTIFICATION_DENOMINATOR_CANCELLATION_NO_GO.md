# 107.180 -- Proper coherent compactification cancels the required local pole

## 1. Minimal compactification

Compactify the transverse scaling line to

\[
 \mathbb P^1,qquad [X:Y]\longmapsto[tX:Y].
\]

The two fixed points are \(0=[0:1]\) and
\(\infty=[1:0]\), with normal characters \(t\) and \(t^{-1}\).
Equivariant localization for the structure sheaf gives

\[
 {1\over1-t}+{1\over1-t^{-1}}=1.
 \tag{1.1}
\]

Thus the proper boundary point at infinity cancels the localization
denominator exactly.

More generally, with the standard linearization of
\(\mathcal O_{\mathbb P^1}(n)\), \(n\ge0\),

\[
 {1\over1-t}+{t^n\over1-t^{-1}}
 =1+t+\cdots+t^n.
 \tag{1.2}
\]

The right side is the ordinary finite-dimensional character of
\(H^0(\mathbb P^1,\mathcal O(n))\).  It has no pole at \(t=1\).

## 2. General properness principle

For a proper scheme with a torus action and a bounded equivariant
coherent complex, the global equivariant Euler characteristic lies in
the unlocalized representation ring \(R(T)\).  Fixed-point formulas may
express it as a sum of fractions in localized \(R(T)\), but all Euler
denominators cancel in the global sum.

This is precisely why the ordinary forgetful map is defined on the
global coherent Euler characteristic even though it is not defined on
an individual local term, as proved in `107_179`.

## 3. Conflict with the explicit local term

The geometric side required by the explicit formula retains the
individual factor

\[
 {1\over|1-u|_v}
\]

as a distribution at each place.  Replacing the transverse affine field
by an ordinary proper coherent compactification performs the
cancellation (1.1) and turns that factor into a regular finite character.
It therefore destroys, rather than geometrizes, the required local
distribution.

Consequently the **global cancellation** fork of `107_179` cannot work
inside finite-type proper coherent geometry while preserving the local
explicit formula term-by-term.  A finite-type compactification can map
to ordinary Arakelov theory only after the information carried by the
uncancelled denominator has disappeared.

## 4. No-go and surviving architecture

Rows (c) and (d) cannot both be obtained by the following chain:

\[
 \text{local inverse Euler class}
 \longrightarrow
 \text{proper finite-type coherent compactification}
 \longrightarrow
 \text{ordinary arithmetic Hodge index}.
\]

The first arrow cancels the local pole before the second arrow becomes
available.

The surviving route must keep a distributional or relative boundary
term outside ordinary coherent Euler characteristic and prove an index
theorem that includes it.  Equivalently, it needs an equivariant,
renormalized arithmetic Hodge theory for the pair
\((\widetilde{\mathrm{Spec}\,\mathbb Z},\widetilde\eta)\), not just
a proper compactification of the transverse line.

This no-go is restricted to finite-type proper coherent
compactifications.  It does not rule out infinite-dimensional,
noncommutative, relative, or renormalized theories.

## 5. Falsifier

The verifier checks (1.1)--(1.2) exactly for \(0\le n\le16\), confirms
that every localized summand has an Euler denominator, and that every
proper global sum is a Laurent polynomial regular at \(t=1\).  It also
evaluates the identities at real prime-derived rational parameters.
Any uncancelled pole in the proper character returns `VERDICT: NO`.
