# 107.172 -- A good-open arithmetic CM lift of the Paper-0 intersections

## 1. Fixed arithmetic model

Let

\[
 E_{\rm CM}/\mathbb Q:\qquad y^2+y=x^3-x^2-7x+10.
\]

Its global minimal discriminant and conductor are

\[
 \Delta_E=-11^3,\qquad N_E=11^2.
\]

It has CM by \(\mathcal O_K\), where

\[
 K=\mathbb Q(\sqrt{-11}),\qquad
 \alpha={-3+\sqrt{-11}\over2},\qquad
 \alpha^2+3\alpha+5=0.
\]

Put

\[
 U=\mathrm{Spec}\,\mathcal O_K[1/11].
\]

The base change of \(E_{\rm CM}\) extends to an abelian scheme
\(\mathcal E\to U\).  Every generic-fibre CM endomorphism extends
uniquely to \(\mathcal E\): this is the extension property for
homomorphisms of abelian schemes over a normal base.

Thus

\[
 \mathcal X_U=\mathcal E\times_U\mathcal E
\]

is a proper smooth relative surface carrying the two rulings, the
diagonal, and every graph \(\Gamma_{\alpha^n}\).  This is an actual
arithmetic model, but only over the good open \(U\), not over all of
\(\mathrm{Spec}\,\mathbb Z\).

## 2. The chosen prime above 5

The prime 5 splits as

\[
 (5)=(\alpha)(\bar\alpha)
\]

in \(\mathcal O_K\).  Fix \(\mathfrak p=(\alpha)\).  Its residue field
is \(\mathbb F_5\).  The action of \(\alpha\) on the tangent space of
the special fibre is its image modulo \(\mathfrak p\), hence zero.
Its reduction is therefore inseparable of degree
\(N(\alpha)=5\).

The special fibre has trace \(-3\).  Its Frobenius satisfies
\(T^2+3T+5\), while its Verschiebung is the conjugate root.  The
inseparable degree-5 reduction of \(\alpha\) is consequently the
Frobenius endomorphism.  At the conjugate prime, \(\alpha\) reduces to
the Verschiebung instead.  Choosing \(\mathfrak p\) before computing is
therefore essential.

The special fibre of \(\mathcal E\) at \(\mathfrak p\) is isomorphic
over \(\mathbb F_5\) to

\[
 y^2=x^3+x+1,
\]

the fixed Paper-0 control.

## 3. Scheme-theoretic graph intersections

For every \(n\geq1\), the equalizer square gives an identity of finite
flat \(U\)-schemes

\[
 \Gamma_{\alpha^n}\cap\Delta
 \simeq \ker(\alpha^n-1).
 \tag{3.1}
\]

The endomorphism \(\alpha^n-1\) is a nonzero isogeny.  Its kernel is
finite locally free, with constant rank

\[
 \deg(\alpha^n-1)=N_{K/\mathbb Q}(\alpha^n-1)
 =5^n+1-\mathrm{Tr}(\alpha^n)=N_n.
 \tag{3.2}
\]

Therefore the graph--diagonal intersection has degree \(N_n\) on every
geometric fibre of \(U\).  On the fibre at \(\mathfrak p\), (3.1) is
the fixed-point scheme of \(F^n\); on the complex fibre it is the graph
intersection of `107_171`.  The equality is not a numerical analogy:
both are fibres of the same finite flat kernel scheme.

The same fibrewise intersection calculation gives

\[
 \Gamma_{\alpha^n}\cdot F_1=5^n,\qquad
 \Gamma_{\alpha^n}\cdot F_2=1,\qquad
 \Gamma_{\alpha^n}^2=0.
\]

After centering, the relative numerical intersection matrix is

\[
 \begin{pmatrix}
 -2&-s_n\\
 -s_n&-2\cdot5^n
 \end{pmatrix},
 \qquad s_n=\mathrm{Tr}(\alpha^n),
\]

on every geometric fibre of \(U\).

## 4. What this proves

The complete Paper-0 correspondence and intersection package now lives
in one proper smooth arithmetic family over
\(\mathrm{Spec}\,\mathcal O_K[1/11]\).  In particular, the
finite-field and complex constructions of `107_02` and `107_171` are
connected by specialization inside a single model.

This does **not** finish row (a): the base is a CM number field with the
bad prime removed, not all of \(\mathrm{Spec}\,\mathbb Z\), and the
surface depends on the fixed elliptic control.  It does **not** finish
row (c): (3.2) packages one elliptic zeta function through a CM
endomorphism and does not construct Riemann zeta's prime/Gamma source
divisors.  No paper status is promoted.

## 5. Falsifier

The verifier uses the actual Sage curve and number field.  It checks the
minimal discriminant, conductor, bad locus, CM order, factorization of
5, the distinguished ideal \((\alpha)\), the fixed reduction, and the
kernel ranks/intersection degrees through \(n=16\).  Any failed
geometric prerequisite returns `VERDICT: NO`.
