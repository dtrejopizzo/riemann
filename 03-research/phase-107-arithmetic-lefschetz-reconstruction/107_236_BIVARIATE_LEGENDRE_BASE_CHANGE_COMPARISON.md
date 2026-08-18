# 107.236 -- Bivariate Legendre base change closes external H0 comparison

## 1. Correct source category

The comparison left open by 107_235 does not start from the countable
Gamma-module \(\mathcal O(\mathcal D)\) of arXiv:2602.15941.  The published
Scaling-Site construction starts from the characteristic-one arithmetic
structure semiring and forms

\[
 \mathcal R(\mathbb Z)
 =\mathbb Z_{\max}\widehat\otimes_{\mathbb B}\mathbb R_{\max},
 \tag{1.1}
\]

where the hat denotes multiplicatively cancellative reduction.  The Legendre
theorem of *Geometry of the Scaling Site* identifies (1.1) with finite convex
piecewise-affine functions on \(\mathbb R_+\), with integral slopes and real
coefficients.  At a point represented by an ordered rank-one group
\(H\subset\mathbb R\), its stalk is the analogous semiring

\[
 \mathcal R(H)=
 \left\{\max_i(h_i x+c_i):h_i\in H, c_i\in\mathbb R\right\}.
 \tag{1.2}
\]

For \(H=H_p=\mathbb Z[1/p]\), restriction to the periodic orbit gives the
published sheaf \(\mathcal O_p\), and passage to fractions and Cartier
divisors gives the published modules \(H^0(C_p,D)\).

Thus 107_235 rejects only the unextended Gamma-module arrow.  It does not
reject (1.1), which inserts the real coefficients before functional
reduction.

## 2. Two-dimensional Legendre theorem

Let \(H,K\subset\mathbb R\) be ordered rank-one groups.  Define

\[
 \mathcal R(H,K)=
 \left\{
 F(x,y)=\max_{1\leq i\leq r}(h_i x+k_i y+c_i):
 h_i\in H, k_i\in K, c_i\in\mathbb R
 \right\},
 \tag{2.1}
\]

with pointwise maximum and addition.  The zero is the function \(-\infty\).

### Theorem 2.1 (bivariate Legendre base change)

External addition of functions induces a canonical isomorphism

\[
 \boxed{
 \left(
 \mathcal R(H)\otimes_{\mathbb R_{\max}}\mathcal R(K)
 \right)_{\mathrm{fun.red}}
 \xrightarrow{\ \sim\ }
 \mathcal R(H,K),}
 \tag{2.2}
\]

where \(f\otimes g\mapsto((x,y)\mapsto f(x)+g(y))\), and
`fun.red` identifies tensors inducing the same function.

### Proof

An element of the algebraic tensor semiring is a finite tropical sum of pure
tensors.  Write

\[
 f_r(x)=\max_a(h_{ra}x+u_{ra}),\qquad
 g_r(y)=\max_b(k_{rb}y+v_{rb}).
\]

Distributivity gives

\[
 \max_r(f_r(x)+g_r(y))
 =\max_{r,a,b}
 \bigl(h_{ra}x+k_{rb}y+u_{ra}+v_{rb}\bigr),
 \tag{2.3}
\]

so the map lands in \(\mathcal R(H,K)\).  Conversely every affine term
\(hx+ky+c\) is the image of
\((hx+c)\otimes(ky)\), and finite maxima lift term by term.  Hence the map is
surjective.  Its kernel congruence is, by definition, equality of the induced
functions; quotienting by functional reduction makes it injective.
\(\square\)

Geometrically, (2.2) is the support-function description of finite convex
polyhedra in \(H\times K\times\mathbb R\).  Tropical addition is convex hull
of unions and multiplication is Minkowski sum.  It is the exact
two-dimensional analogue of the published one-dimensional Legendre theorem,
not a Cartesian product of section spaces.

## 3. Frobenius and sheaf descent

For positive integers \(m,n\), define

\[
 (\operatorname{Fr}_{m,n}F)(x,y)=F(mx,ny).
 \tag{3.1}
\]

In (2.1) this replaces each slope pair \((h_i,k_i)\) by
\((mh_i,nk_i)\).  Therefore (2.2) intertwines the two absolute Frobenius
actions.  Restriction to open rectangles also commutes with (2.2), so the
construction sheafifies on the product Scaling topos.  Put

\[
 \mathcal O_{\mathscr S^2}
 :=\left(
 \operatorname{pr}_1^{-1}\mathcal O_{\mathscr S}
 \otimes_{\mathbb R_{\max}}
 \operatorname{pr}_2^{-1}\mathcal O_{\mathscr S}
 \right)_{\mathrm{fun.red}}.
 \tag{3.2}
\]

Then \((\mathscr S^2,\mathcal O_{\mathscr S^2})\) is a canonical
semiringed product-topos carrier.  Its stalk at a pair of periodic points
\((\lambda H_p,\mu H_q)\) is \(\mathcal R(\lambda H_p,\mu H_q)\).

This constructs a genuine global cross-prime sheaf.  It does not assert that
the resulting ringed topos is a proper arithmetic surface in the hypotheses
of an existing Hodge theorem.

## 4. Identification of external divisor H0

For special divisors \(N\{1\}\) on \(C_p\) and \(M\{1\}\) on \(C_q\), the
published one-dimensional modules have extremal generators \(\phi_a\) and
\(\psi_b\).  Under (2.2), their external tensor image is exactly

\[
 \left\{
 \max_{a,b}\bigl(\phi_a(x)+\psi_b(y)+c_{ab}\bigr)
 \right\}.
 \tag{4.1}
\]

This is precisely the intrinsic module \(\mathcal T_{N,M}^{p,q}\) defined in
107_232.  Therefore the earlier dimension computation is now a computation
inside the base-changed global square sheaf, rather than an unattached local
model.

The effective-inclusion and principal-translation squeeze of 107_233 takes
place inside the same sheaf.  Consequently, for arbitrary external divisors
\(D\) and \(E\),

\[
 \boxed{
 \operatorname{cdim}^{(2)}
 H^0_{\mathrm{ext}}(D\boxtimes E)
 =\max(\deg D,0)\max(\deg E,0).}
 \tag{4.2}
\]

The direct comparison rejected in 107_235 is replaced by the exact chain

\[
 \mathbb Z_{\max}
 \longrightarrow
 \mathbb Z_{\max}\widehat\otimes_{\mathbb B}\mathbb R_{\max}
 \xrightarrow{\mathrm{Legendre}}
 \mathcal O_{\mathscr S}
 \xrightarrow{\boxtimes}
 \mathcal O_{\mathscr S^2}.
 \tag{4.3}
\]

## 5. Status change and hard boundary

The following package is now closed:

\[
 \boxed{\texttt{SCALING\_SQUARE\_EXTERNAL\_H0: CONSTRUCTED}.}
\]

This is a construction, not an audit: it defines the semiringed product
topos, its bivariate stalks, its Frobenius action, and its external divisor
modules, and identifies their continuous dimension.

Row (a) nevertheless remains `partial`.  Exactly three items remain:

1. extend from external divisors to the intrinsically mixed correspondence
   divisors \(D(f)=\int f(\lambda)\Psi_\lambda d^*\lambda\);
2. construct the intermediate \(H^1\) or prove a replacement existence
   theorem not requiring it;
3. prove RR/intersection theory strong enough to imply effectivity from a
   positive self-intersection.

The 2018 Connes--Consani paper identifies the same boundary: \(H^0\) on the
square is straightforward, \(H^2\) may be defined by duality, and \(H^1\) is
the open obstruction.  No status is promoted beyond the external \(H^0\)
package.

## 6. Machine certificate

Run

```bash
/home/trabajo/miniforge3/bin/python \
  107_236_bivariate_legendre_base_change_comparison.py
```

The program reads the published Legendre, periodic-stalk, divisor-module and
2018 boundary statements, then checks exact two-variable distributivity,
surjectivity on a fixed real prime atlas, Frobenius covariance, and a mutated
non-external map which must fail.
