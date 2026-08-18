# 107.219 -- Componentwise cyclotomic descent of finite-support H1

## 1. Replace subdivision by normalized components

The no-go of 107_218 concerns the power-map subdivision of the group
ring \(\mathbb Z[\mu_L^2]\).  It does not apply to the normalized rooted
scheme

\[
 \mathcal R_L=\coprod_{n\mid L}\mathrm{Spec}\,\mathbb Z[\zeta_n]
\]

of 107_160.  If \(L\mid L'\), every old component occurs unchanged as an
open-and-closed component of \(\mathcal R_{L'}\).

For two rooted labels \((n,u)\) and \((m,v)\), put

\[
 \ell=\mathrm{lcm}(n,m),\qquad O_\ell=\mathbb Z[\zeta_\ell],
\]

\[
 a=\zeta_\ell^{u\ell/n}-1,
 \qquad b=\zeta_\ell^{v\ell/m}-1.
 \tag{1.1}
\]

Both roots live in the actual cyclotomic compositum
\(\mathbb Q(\zeta_\ell)\).  Define the component complex

\[
 K_{n,u;m,v}:
 0\to O_\ell\xrightarrow{(-b,a)}O_\ell^2
 \xrightarrow{(a,b)}O_\ell\to0.
 \tag{1.2}
\]

## 2. Strict finite-support descent

Let \(S\) be a finite set of label pairs and set

\[
 K_S=\bigoplus_{((n,u),(m,v))\in S}K_{n,u;m,v}.
 \tag{2.1}
\]

Once every \(n,m\) in \(S\) divides \(L\), the complex (2.1) is supported
on open-and-closed components of \(\mathcal R_L^2\).  For every larger
\(L'\), extension by zero along
\(\mathcal R_L^2\hookrightarrow\mathcal R_{L'}^2\) carries each summand
to the identical complex over the identical ring \(O_\ell\).  Therefore

\[
 K_S(L')=K_S(L),
 \qquad H^i(K_S(L'))=H^i(K_S(L))
 \tag{2.2}
\]

canonically for \(i=0,1,2\).

This is strict stabilization, not stabilization of dimensions only.

## 3. Cohomology on mixed components

For \(I=(a,b)\subset O_\ell\), the Dedekind-domain calculation of
107_217 applies without requiring \(n=m\):

\[
 H^0(K_{n,u;m,v})=O_\ell/I,
 \qquad
 H^1(K_{n,u;m,v})=I^{-1}/O_\ell,
 \qquad
 H^2=0
 \tag{3.1}
\]

unless both characters are trivial.  In particular,

\[
 |H^0|=|H^1|=N_{O_\ell}(I).
 \tag{3.2}
\]

Mixed-primary components can be acyclic because their two augmentation
ideals are coprime.  Components sharing a ramified prime can retain
torsion.  Both outcomes are detected rather than imposed.

## 4. Exact gain and remaining gap

This constructs a directed, finite-support integral \(H^1\) system on
the normalized rooted square.  It repairs the transition failure of
107_218 by changing the geometric carrier, not by changing the power
map after seeing the data.

It does not yet make \(\mathcal R_L^2\) the Phase 107 surface: its
components are finite over \(\mathrm{Spec}\,\mathbb Z\), and the
complexes (1.2) are character local systems rather than the divisor
modules \(O(D)\).  The next required comparison is a morphism from the
finite-support divisor modules to these component complexes, compatible
with the Frobenius graph ideals and integer dimension.

## 5. Falsifier

`107_219_componentwise_cyclotomic_h1_descent.sage` uses mixed actual
cyclotomic composita, computes the integral homology and ideal norms, and
checks identity of every old differential after two fixed level
enlargements.  A power-subdivision negative control must move at least
one old label and is rejected.

