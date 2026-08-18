# 114.a.136 — H7 no-go: the rational sphere has no base retraction

~~~
+------------------------------------------------------------------------+
| BASE        S=F{+-1} embeds in the rational sphere residue kappa_inf.   |
| ASSUME      An S-algebra retraction kappa_inf -> S exists.              |
| VECTOR      v=(3/5,4/5) has unit norm and survives in kappa_inf.        |
| CONTACT     v is residue-orthogonal to both signed coordinate axes.      |
| CONFLICT    Every nonzero element of S_[2] lies on one of those axes.    |
| RESULT      The mixed projection has no section induced from the base.   |
+------------------------------------------------------------------------+
~~~

## 1. The three-vector calculation

Work in the CGR model; the same argument is visible after forgetting a
CFR^t object to CGR. Put

\[
 S=\mathbb F\{\pm1\},\qquad
 v=(3/5,4/5)\in(\kappa_\infty)_{[2]}.                                \tag{1.1}
\]

The vector survives the real residue because

\[
 (3/5)^2+(4/5)^2=1.                                                  \tag{1.2}
\]

Let \(e_1,e_2\) be the two coordinate vectors. In the valuation object,
contraction is the Euclidean scalar product. Hence

\[
 v\sslash e_1=3/5,\qquad v\sslash e_2=4/5.                           \tag{1.3}
\]

Both scalars have norm strictly less than one, so both become zero in the
residue \(\kappa_\infty\). On the other hand

\[
 v\sslash v=1.                                                       \tag{1.4}
\]

## 2. No-retraction theorem

### Theorem 2.1

There is no \(S\)-algebra morphism

\[
 r:\kappa_\infty\longrightarrow S.                                  \tag{2.1}
\]

In particular, \(S\to\kappa_\infty\) has no retraction.

### Proof

Because \(r\) is over \(S\), it fixes \(e_1,e_2,0,1\). If \(r(v)=0\),
applying \(r\) to (1.4) gives \(0=1\), impossible. Thus \(r(v)\) is a
nonzero element of \(S_{[2]}\). By the definition of the monoid generalized
ring \(\mathbb F\{\pm1\}\), those elements are exactly

\[
 \{\pm e_1,\pm e_2\}.                                                 \tag{2.2}
\]

If \(r(v)=\pm e_i\), its contraction with \(e_i\) is \(\pm1\), whereas
applying \(r\) to the corresponding equality in (1.3) gives zero. This
contradicts preservation of contraction. QED.

The proof uses no topology, cardinality extrapolation or assumption about
all of \(\mathbb F_{\mathbb R}\); the single rational Pythagorean vector
already suffices.

## 3. Geometric consequence

A retraction \(\kappa_\infty\to S\) would give a section

\[
 X\longrightarrow X\times_Sx_\infty
\]

of the mixed projection, and such a section would make pullback injective
on every Picard theory with functorial pullback. Theorem 2.1 proves that
this standard section argument is unavailable.

This does **not** prove that mixed pullback is noninjective. Faithfully-flat
descent can be conservative without a section, and a norm can split Picard
pullback without splitting the base algebra. The live gate from a135
therefore sharpens to:

> **H7-RSPH-DESC/NORM.** Prove conservativity on the prime torsor lattice by
> genuine descent or construct a Picard norm; a base retraction cannot do
> it.

## 4. Status

The easiest proposed proof of H7-RSPH-CONS is closed negatively.
H7-RSPH-DESC/NORM, H7-ARCH-BDRY, row A and RH remain open.

The verifier 114_a_136_h7_rational_sphere_no_retraction_verify.py checks the
exact Pythagorean and contraction contradiction and the primary-source
operations.
