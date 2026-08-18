# 107.174 -- No-go for descending the oriented CM Frobenius graph

## 1. Descent datum

Let

\[
 K=\mathbb Q(\alpha),\qquad \alpha^2+3\alpha+5=0,
\]

and let \(c\) be complex conjugation.  Then

\[
 c(\alpha)=\bar\alpha=-3-\alpha.
\]

The rational curve \(E_{\rm CM}/\mathbb Q\) has all its CM
endomorphisms over \(K\), but Galois acts on their graphs by

\[
 c(\Gamma_\alpha)=\Gamma_{\bar\alpha}.
 \tag{1.1}
\]

Consequently an individual oriented graph can descend to \(\mathbb Q\)
only if these two graphs agree.

## 2. The conjugate graphs are distinct

On \(E_{\rm CM}\times E_{\rm CM}\),

\[
 \Gamma_\alpha^2=0,
\]

whereas

\[
 \Gamma_\alpha\cdot\Gamma_{\bar\alpha}
 =\deg(\alpha-\bar\alpha)
 =N_{K/\mathbb Q}(\sqrt{-11})=11.
 \tag{2.1}
\]

Thus \(\Gamma_\alpha\neq\Gamma_{\bar\alpha}\), even numerically.  The
same conclusion follows from endomorphisms: an endomorphism defined over
\(\mathbb Q\) must be fixed by conjugation, whereas \(\alpha\) is not.
In particular there is no degree-5 endomorphism over \(\mathbb Q\)
whose base change is \(\alpha\).

## 3. Orbit averaging does not preserve composition

The invariant integral orbit cycle is

\[
 C_n=\Gamma_{\alpha^n}+\Gamma_{\bar\alpha^n}.
\]

It descends as a correspondence, but

\[
 C_n\cdot\Delta=2N_n.
\]

Dividing by two repairs this single intersection identity.  Set

\[
 A_n={1\over2}C_n.
\]

Composition gives

\[
 A_m\circ A_n={1\over4}\left(
 \Gamma_{\alpha^{m+n}}
 +\Gamma_{\alpha^m\bar\alpha^n}
 +\Gamma_{\bar\alpha^m\alpha^n}
 +\Gamma_{\bar\alpha^{m+n}}
 \right).
 \tag{3.1}
\]

The two mixed graphs in (3.1) are absent from \(A_{m+n}\).  Already for
\(m=n=1\), both mixed terms are \(\Gamma_{[5]}\), while the outer terms
are \(\Gamma_{\alpha^2}\) and \(\Gamma_{\bar\alpha^2}\).  Hence

\[
 A_1\circ A_1\neq A_2.
\]

Orbit averaging therefore preserves the scalar point-count
intersection only by sacrificing the Frobenius semigroup law.

## 4. Consequence for Phase 107

The everywhere-good surface of `107_173` cannot be descended to the
requested rational base together with its oriented Frobenius graph
package.  This is a no-go for the **CM graph descent route**, not for the
existence of a different absolute correspondence.

This conclusion agrees with the architecture of Connes--Consani's 2026
arithmetic Jacobian: in characteristic zero the explicit formula is
modeled by idele-class translations on an adelic Picard monoid, not by a
single algebraic Frobenius endomorphism.  The rooted and arithmetic-linking
data in that construction are therefore a genuinely different source
channel and must be tested directly rather than identified with the CM
graph.

## 5. Falsifier

The verifier uses the actual CM number field and curve.  It computes the
conjugate, the graph intersection in (2.1), the doubled diagonal
intersection through \(n=16\), and the support of the averaged
composition (3.1).  It returns `VERDICT: NO` if the oriented graph
descends or if averaging unexpectedly preserves composition.
