# 107.196 -- Canonical relative Fock determinant cancels the eta tail

## 1. Number-operator filtration

Let

\[
 \mathcal F_{\ge r}=\bigoplus_{n\ge r}\mathbb C e_n,
 \qquad Ne_n=ne_n.
\]

For \(|q|<1\), the operator \(q^N\) is trace class on every
\(\mathcal F_{\ge r}\), so the Fredholm determinant

\[
 D_r(q)=\det_{\mathrm F}(1-q^N\mid\mathcal F_{\ge r})
       =\prod_{n\ge r}(1-q^n)
 \tag{1.1}
\]

is defined without regularization.

The number grading gives the canonical exact sequence

\[
 0\longrightarrow\mathcal F_{\ge2}
 \longrightarrow\mathcal F_{\ge1}
 \longrightarrow\mathbb C_{(1)}
 \longrightarrow0,
 \tag{1.2}
\]

where \(q^N\) acts by \(q\) on \(\mathbb C_{(1)}\).

## 2. Relative determinant theorem

Multiplicativity of Fredholm determinants in (1.2) gives

\[
 \boxed{
 {D_1(q)\over D_2(q)}=1-q.
 }
 \tag{2.1}
\]

This is not a truncation of the eta product.  Both infinite tails are
retained, and their cancellation is induced by an equivariant exact
sequence fixed before \(q\) is evaluated.

More generally,

\[
 {D_r(q)\over D_{r+1}(q)}=1-q^r,
 \tag{2.2}
\]

so every individual return weight is the determinant of the graded
quotient \(\mathcal F_{\ge r}/\mathcal F_{\ge r+1}\).

## 3. Prime-orbit specialization

For a real prime orbit and \(s\in\mathcal H\), put \(q=p^{-s}\).
Then (2.1) becomes

\[
 {D_1(p^{-s})\over D_2(p^{-s})}=1-p^{-s},
 \tag{3.1}
\]

exactly the twisted determinant of 107_185.  The inverse determinant
is the local Euler factor; its Green connection can equivalently be
written using the determinant as

\[
 d\log {D_1(p^{-s})\over D_2(p^{-s})}
 =\log p\,{p^{-s}\over1-p^{-s}}\,ds,
 \tag{3.2}
\]

which is the local finite Green channel.

Thus the virtual class

\[
 [\mathcal F_{\ge1}]-[\mathcal F_{\ge2}]
 =[\mathbb C_{(1)}]
 \tag{3.3}
\]

provides the canonical cancellation demanded by 107_195.

## 4. Relation to the flat-torus eta tower

The holomorphic eta tail is

\[
 (q;q)_\infty=D_1(q).
\]

The denominator in (2.1) is not an arbitrary correction:

\[
 D_2(q)=(q^2;q)_\infty
\]

is the determinant on the invariant codimension-one tail of the same
number operator.  Therefore (2.1) is a relative determinant in a
single filtered spectral object.

## 5. Exact scope

This closes the local **virtual cancellation** problem left by
107_195.  It constructs a source-defined relative determinant and
recovers both the orbit determinant and its Green one-form.

It does not yet construct:

1. a finite-dimensional compact Kahler manifold realizing the virtual
   Fock difference;
2. an arithmetic K-theory pushforward or Quillen metric for (3.3);
3. a Bott--Chern current comparing the two infinite tails;
4. a global square-level Deligne pairing;
5. a primitive Hodge form.

The next required bridge is therefore not another determinant identity.
It is a geometric or noncommutative realization of the exact sequence
(1.2) in a category with a secondary characteristic class and an index
theorem.

## 6. Falsifier

The verifier uses primes \(2,3,5,7,11\), real and complex spectral
parameters, and several finite cutoffs.  At every cutoff the paired
tails must cancel exactly to \(1-q\), and the infinite-product tail is
bounded independently.  It also checks (3.2).  A mutated shift
\(\mathcal F_{\ge1}/\mathcal F_{\ge3}\), which would introduce the
extra factor \(1-q^2\), must be rejected.
