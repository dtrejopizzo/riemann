# 114.a.124 — H7: canonical metrized Green biextension on the prime presentation

```
+------------------------------------------------------------------------+
| LINE        E_G(x,y)=R with distinguished generator 1_(x,y).           |
| METRIC      ||1_(x,y)||=exp(-G_num(x,y)).                              |
| BIEXT       Addition in either variable gives isometric tensor laws.    |
| SPLIT       E_contact tensor E_Green = E_RR isometrically.              |
| GAUGE       q_G(x)=G_num(x,x)/2 polarizes back to G_num.                |
| DESCENT     Exists on Pic(Y^reg) iff the anti-diagonal is faithful.      |
| LIMIT       Metrized numerical biextension, not a sheaf-level Green     |
|             function or excess complex on Y^reg.                        |
+------------------------------------------------------------------------+
```

## 1. Metrized lines from a bilinear form

Let `D=mathfrak D_pr` be the all-prime presentation lattice.  For each
`x,y in D`, let

\[
 \mathcal E_G(x,y)=\mathbb R\,\mathbf1_{x,y}                           \tag{1.1}
\]

and give it the positive norm

\[
 \|\mathbf1_{x,y}\|_G=\exp\bigl(-G_{\rm num}(x,y)\bigr),              \tag{1.2}
\]

where `G_num` is the unique numerical Green correction of `a123`.

For addition in the first variable define

\[
 \mu_1:\mathcal E_G(x,y)\otimes\mathcal E_G(x',y)
 \xrightarrow{\sim}\mathcal E_G(x+x',y),
 \qquad \mathbf1_{x,y}\otimes\mathbf1_{x',y}\mapsto
 \mathbf1_{x+x',y},                                                    \tag{1.3}
\]

and analogously define `mu_2` in the second variable.

### Theorem 1.1

Equations (1.1)--(1.3) define a symmetric metrized biextension of
`D x D` by one-dimensional real normed lines.

### Proof

Bilinearity gives

\[
 G_{\rm num}(x+x',y)=G_{\rm num}(x,y)+G_{\rm num}(x',y).              \tag{1.4}
\]

Hence the tensor norm of the left generator in (1.3) is
`exp(-G(x,y)-G(x',y))`, exactly the norm of the right generator.  Thus
`mu_1` is an isometry; the same proof applies to `mu_2`.  Associativity,
units and the interchange square all send distinguished generators to the
same distinguished generator, so they commute.  Symmetry of `G_num` gives
the isometry `E_G(x,y)~=E_G(y,x)`.  QED.

No positivity of the bilinear form is required: (1.2) is a positive norm for
every real value of `G_num`.

## 2. Contact, Green and total RR biextensions

Apply the same construction to `C_Lambda` and `B_RR`, obtaining
`E_C` and `E_RR`.  Since `a123` proves

\[
 B_{\rm RR}=C_\Lambda+G_{\rm num},                                    \tag{2.1}
\]

the generator map

\[
 \mathcal E_C(x,y)\otimes\mathcal E_G(x,y)
 \longrightarrow\mathcal E_{\rm RR}(x,y),
 \qquad \mathbf1_C\otimes\mathbf1_G\longmapsto\mathbf1_{\rm RR}    \tag{2.2}
\]

is an isometry compatible with both biextension laws.

On prime generators, its logarithmic norm decomposition is

\[
 {\log p\log q\over2\log3}
 =\delta_{pq}\log p+
 \left({\log p\log q\over2\log3}-\delta_{pq}\log p\right).          \tag{2.3}
\]

Thus the literal finite contact and the archimedean/numerical correction are
realized as tensor factors of one metrized RR line, not merely as two numbers
whose sum was recorded.

## 3. The quadratic Green gauge

Define

\[
 q_G(x)={1\over2}G_{\rm num}(x,x),
 \qquad \|\mathbf1_x\|_{q_G}=e^{-q_G(x)}.                             \tag{3.1}
\]

Then

\[
 q_G(x+y)-q_G(x)-q_G(y)=G_{\rm num}(x,y),                              \tag{3.2}
\]

so the biextension metric is precisely the polarization of the quadratic
gauge.  Formula (2.5) of `a123` gives explicitly

\[
 q_G(x)={d_1(x)d_2(x)\over2\log3}
          -\sum_px_{p,1}x_{p,2}\log p.                                \tag{3.3}
\]

This is canonical on the decorated/presentation lattice and contains no
choice of prime, basis, tree or truncation.

## 4. Descent and exact remaining geometry

### Theorem 4.1

The metrized biextensions `E_C`, `E_G`, `E_RR` and the gauge `q_G` descend
through `rho:D->Pic_cmp(Y^reg)` if and only if the prime anti-diagonal is
faithful.

### Proof

If `rho` is injective, descent is tautological.  Conversely, a descended
biextension metric makes its logarithmic norm bilinear form vanish on
`ker rho` in either variable.  Theorem 3.1 of `a123` proves that none of the
three forms has a nonzero anti-kernel vector in its radical.  The quadratic
gauge polarizes to `G_num`, so its descent implies the same conclusion. QED.

This constructs an actual normed-line Green object at the numerical Picard
level.  It does not identify `E_C` with a determinant of the generalized
contact sheaf, construct `E_G` from a Green function on an archimedean fiber,
or identify `E_RR` with a Deligne pairing/excess determinant of completed
Cartier sheaves on `Y^reg`.  Those comparison theorems, together with
H7-RULING-PF, are the remaining geometric H7-REG-EXCESS-RR gate.  Dynamic
undecorated cycles, row A and RH remain open.

## 5. Verification scope

`114_a_124_h7_metrized_green_biextension_verify.py` checks the two tensor
isometries, associativity/interchange at logarithmic norm level, the
contact-Green-RR splitting, polarization and descent obstruction.  It does
not assert the missing sheaf-level comparison.

**Later boundary reduction (`a128`--`a129`).**  The global fraction
`p_2/p_1` cancels finite valuations but leaves nonunit real-boundary data, so
it does not prove failure of descent.  Descent is now exactly H7-ARCH-BDRY.
Using this numerical biextension itself to establish the missing geometric
boundary degree would be circular.
