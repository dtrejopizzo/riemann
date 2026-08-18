# 106.210 — The cyclotomic diagonal stop test

## 1. Purpose

For distinct cyclotomic divisors, the arithmetic intersection multiplicity
is detected by the resultant:

\[
 \frac{1}{\varphi(n)}
 \log\left|\operatorname {Res}(\Phi_m,\Phi_n)\right|
 =\begin{cases}
 \log p,&m/n=p^a,\\
 0,&m/n\text{ is not a prime power},
 \end{cases}
 \tag{1}
\]

for \(m>n>1\).  This supplies the exact prime-power support that the
set-theoretic \(\gcd\) overlap lacks.

Before using (1) in a Gram matrix, the same intersection theory must
define the diagonal \(Z_n^2\), where

\[
 Z_n=V(\Phi_n)\subset\operatorname {Spec}\mathbb Z[x].
 \tag{2}
\]

The precommitted fifth stop test is:

> Construct a finite, source-defined self-intersection of (Z_n) in the
> same category that gives (1), without importing an unrelated diagonal
> form or choosing its sign.

The finite resultant theory does not pass this test.  It gives the
off-diagonal local intersections but no finite diagonal.  The missing
datum is precisely an archimedean Green metric after proper
compactification.

## 2. Why the ordinary resultant has no diagonal

For any nonconstant polynomial \(f\),

\[
 \operatorname {Res}(f,f)=0.
 \tag{3}
\]

Hence

\[
 \boxed{\operatorname {Res}(\Phi_n,\Phi_n)=0.}
 \tag{4}
\]

This is not a removable normalization singularity.  Distinct divisors
meet in a finite zero-dimensional scheme, whereas a divisor intersected
with itself has excess dimension and requires a normal bundle or a
moving lemma.

## 3. Derived self-intersection on the affine surface

Let

\[
 A=\mathbb Z[x],
 \qquad
 B_n=A/(\Phi_n).
 \tag{5}
\]

The standard free resolution of \(B_n\) is

\[
 0\longrightarrow A
 \xrightarrow{\ \Phi_n\ }A
 \longrightarrow B_n\longrightarrow0.
 \tag{6}
\]

Tensoring (6) with \(B_n\) makes the differential zero.  Therefore

\[
 B_n\otimes_A^{\mathbf L}B_n
 \simeq[B_n\xrightarrow{0}B_n],
 \tag{7}
\]

and

\[
 \operatorname {Tor}_0^A(B_n,B_n)\cong B_n,
 \qquad
 \operatorname {Tor}_1^A(B_n,B_n)\cong B_n.
 \tag{8}
\]

Both modules are horizontal and infinite as abelian groups.  Their
lengths are not finite, so the usual local Euler characteristic

\[
 \sum_i(-1)^i\operatorname {length}
 \operatorname {Tor}_i^A(B_n,B_n)
 \tag{9}
\]

is not a number.  Formally the two identical classes cancel in \(K_0\),
but this zero does not provide the required metric self-intersection.

There is a second affine obstruction.  The ring \(\mathbb Z[x]\) is a
UFD, and \(Z_n=\operatorname {div}(\Phi_n)\) is principal.  Its class in
\(\operatorname {CH}^1(\operatorname {Spec}\mathbb Z[x])\) is zero.
Thus the nonzero logarithmic resultants are local intersection
contributions; they are not the values of a complete numerical
intersection pairing on the affine surface.

## 4. Compactification moves the missing term to infinity

Let \(\overline Z_n\) be the closure of \(Z_n\) in
\(\mathbb P^1_{\mathbb Z}\), and let \(D_\infty\) be the divisor at
infinity.  Homogenizing \(\Phi_n\) gives the divisor relation

\[
 \operatorname {div}(\Phi_n(x))
 =\overline Z_n-\varphi(n)D_\infty.
 \tag{10}
\]

Consequently

\[
 \overline Z_n\sim\varphi(n)D_\infty.
 \tag{11}
\]

The local finite intersections measured by resultants must be completed
by contributions at \(D_\infty\).  A numerical arithmetic
self-intersection additionally requires a Green function, equivalently a
Hermitian metric on the associated line bundle.  Changing that metric
changes the archimedean self-intersection.  The finite cyclotomic divisor
does not determine it.

Thus \(\operatorname {Spec}\mathbb Z[x]\) supplies a genuine arithmetic
surface and genuine local intersections, but not a canonical global
diagonal by itself.

## 5. The discriminant is canonical but is not the missing diagonal

One may move one copy infinitesimally by replacing \(\Phi_n\) with its
derivative.  This gives

\[
 \left|\operatorname {Res}(\Phi_n,\Phi_n')\right|
 =\left|\operatorname {Disc}(\Phi_n)\right|.
 \tag{12}
\]

The cyclotomic discriminant is

\[
 \boxed{
 \left|\operatorname {Disc}(\Phi_n)\right|
 =\frac{n^{\varphi(n)}}
 {\displaystyle\prod_{p\mid n}
  p^{\varphi(n)/(p-1)}}.}
 \tag{13}
\]

Hence its normalized logarithm is

\[
 \frac{1}{\varphi(n)}
 \log\left|\operatorname {Disc}(\Phi_n)\right|
 =\log n-\sum_{p\mid n}\frac{\log p}{p-1}.
 \tag{14}
\]

This is a valid finite arithmetic invariant: it measures the different
and ramification of the cyclotomic order.  It is not a bilinear
self-intersection compatible with (1): it uses a derivative, is a normal
torsion rather than a diagonal product, and does not determine the
archimedean metric in (10).  Treating (14) as \(Z_n^2\) would therefore
mix two different constructions in exactly the way forbidden by the
stop test.

## 6. Why automatic Arakelov negativity would not solve the problem

After choosing a regular proper arithmetic surface and Green metrics,
the arithmetic Hodge-index theorem gives a negative semidefinite pairing
on the degree-zero part.  That sign is structural and unconditional.

For the present compactification there is an additional degeneracy:
\(\mathbb P^1_{\mathbb Z}\) has genus zero and trivial Jacobian.  Its
degree-zero horizontal divisor classes carry no nontrivial arithmetic
\(H^1\) capable of holding the CCM resonant divisor.  The local
resultants remember prime-power ramification, but the ambient surface has
no degree-one geometry whose signature could encode the zeros of
\(\xi\).

Therefore importing an arbitrary Arakelov metric would give either an
automatic sign or a metric-dependent finite part.  Neither identifies
the required CCM/Weil diagonal.

## 7. Consequence of the fifth stop test

The cyclotomic resultant construction makes a genuine advance over
set-theoretic root overlap:

* it lives on the classical arithmetic surface
  \(\operatorname {Spec}\mathbb Z[x]\);
* its local intersections are scheme-theoretic;
* it vanishes on mixed ratios;
* it gives exactly \(\log p\) on prime-power transitions.

But it does not by itself define the diagonal, and the genus-zero
compactification cannot supply the missing resonant degree one.  Under
the stop rule, the resultant matrix is not assembled by borrowing the
diagonal \(\Gamma_n^2=n\) from cardinality counting.

The only coherent continuation would require a richer ambient arithmetic
object carrying all three structures simultaneously:

1. cyclotomic derived intersections at finite places;
2. the Gamma--polar Green metric at infinity;
3. a nontrivial degree-one/diagonal trace identified with the CCM
   resonant degree one.

Constructing item 2 on \(\mathbb P^1_{\mathbb Z}\) is not enough; item 3
is absent there.  Thus the classical cyclotomic surface is a correct
local model, not the global polarized object sought by the program.

## 8. Status

Proved:

* the ordinary cyclotomic resultant has no diagonal;
* the affine derived self-intersection has non-finite horizontal Tor
  modules and no numerical Euler characteristic;
* the affine divisor is principal;
* proper compactification exposes the missing infinity/metric term;
* the discriminant gives a canonical normal torsion but not the required
  self-intersection;
* the genus-zero ambient has no nontrivial Jacobian degree one.

Verdict:

> Cyclotomic resultants provide the correct finite local intersection
> support, but they do not close the diagonal.  The standalone
> \(\operatorname {Spec}\mathbb Z[x]\) route stops at the fifth test.  Its
> resultant identities remain valid local input for any future, richer
> arithmetic intersection theory.
