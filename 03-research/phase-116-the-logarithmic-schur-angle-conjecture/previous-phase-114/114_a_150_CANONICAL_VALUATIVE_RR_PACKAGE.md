# 114.a.150 — Canonical valuative RR package on the prime-generated square

## 1. Canonical all-prime finite-place valuation

Let

\[
 \mathbb T_{\rm fin}=\mathbb N^{(\mathcal P)}\cup\{\infty\}
\]

with coordinatewise tropical addition `a oplus b=min(a,b)` and tropical
multiplication `a odot b=a+b`.  The absorbing element is `infinity` and the
multiplicative unit is the zero vector.  Equivalently, this is the semiring
of nonzero integral ideals of `Z`, with ideal sum and ideal product, together
with the zero ideal.

The map

\[
 \nu_{\rm fin}:\mathbb Z\longrightarrow\mathbb T_{\rm fin},\qquad
 n\longmapsto(v_p(n))_p
\]

is multiplicative and satisfies

\[
 \nu_{\rm fin}(a+b)\ge
 \nu_{\rm fin}(a)\oplus\nu_{\rm fin}(b)
\]

coordinatewise.  It is therefore a valuation in the ordered-blueprint (or
tropical-hyperfield) sense, not a semiring homomorphism.  It retains every
prime separately.

Its canonical mass is

\[
 \ell((n))=\log\#(\mathbb Z/(n))
 =\sum_pv_p(n)\log p=\log|n|,\qquad n\ne0.
\]

No interpolation base or auxiliary prime occurs.

## 2. Arakelov completion and principal descent

Put

\[
 \widehat{\operatorname{Div}}(\overline{\operatorname{Spec}\mathbb Z})
 =\bigoplus_p\mathbb Z[p]\oplus\mathbb R[\infty]
\]

and

\[
 \widehat\deg\left(\sum_pa_p[p]+a_\infty[\infty]\right)
 =\sum_pa_p\log p+a_\infty.
\]

For `r in Q^times`, define

\[
 \widehat{\operatorname{div}}(r)
 =\sum_pv_p(r)[p]-\log|r|[\infty].
\]

The product formula gives degree zero.  Conversely, every divisor of degree
zero is principal: for its finite part take `r=product p^(a_p)`; subtracting
`div(r)` kills the finite coordinates and the degree-zero condition kills
the infinity coordinate.  Hence

\[
 \widehat{\operatorname{Div}}/widehat{\operatorname{Prin}}
 \xrightarrow[\widehat\deg]{\sim}\mathbb R.
\]

This is the missing numerical collapse of the infinite prime lattice.  It is
a real Picard/degree line, not a finitely generated integral lattice.

On the square used in the paper, boundary faithfulness gives the internal
direct sum

Div_A = Prin_A direct-sum D_pr.

Hence projection to the prime coordinate is well-defined on the full
displayed divisor group.  Extending d_i by zero on Prin_A annihilates every
actual principal divisor, including a principal fraction which does not
split between the rulings.  On ruling fractions this agrees with the
Arakelov product formula above.

## 3. Canonical periodic-orbit section functor

The absolute-curve/Arithmetic-Site morphism sends a prime `p` canonically to
the periodic orbit

\[
 C_p=\mathbb R_+^\times/p^\mathbb Z
\]

of length `log p`.  On `C_p`, Connes--Consani prove

\[
 \operatorname{Div}(C_p)/\operatorname{Prin}(C_p)
 \simeq\mathbb R\times\mathbb Z/(p-1)\mathbb Z
\]

and

\[
 \operatorname{cdim}H^0(C_p,D)=\max(\deg D,0).
\]

For delta in R, let [D_p(delta)] be the unique divisor class with
(deg,chi)=(delta,0).  The class is canonical.  Different representatives
are related by a principal tropical function g, which translates H^0
homeomorphically.  The ultrametric slope norm satisfies
||f-g||_p <= max(||f||_p,||g||_p), and the inverse has the same bound.
Consequently the filtered pieces agree after the depth exceeds the fixed
norm of g, so continuous dimension is representative-independent.

For `delta,eta>=0`, let

\[
 \mathcal T_{p,q}(\delta,\eta)
 =H^0(C_p,D_p(\delta))\widehat\boxtimes
  H^0(C_q,D_q(\eta))
\]

be the functionally reduced external tropical tensor module.  The exact
external-dimension theorem gives

\[
 \operatorname{cdim}^{(2)}\mathcal T_{p,q}(\delta,\eta)=\delta\eta.
\]

Let PerExt be the category of finite-support families of filtered external
periodic tropical modules.  Componentwise principal translations are
isomorphisms and effective inclusions are morphisms.  There is a unique
dimension functional on PerExt which is additive on finite products and
restricts on each prime-pair component to the published normalized external
continuous dimension: these two requirements force it to be the unweighted
sum of the component dimensions.

For an effective prime divisor

\[
 x=\sum_pa_{p,1}e_{p,1}+\sum_qb_{q,2}e_{q,2},
\]

define the finite-support valuative section packet

\[
 \mathcal H_{\rm val}(x)=
 \prod_{a_{p,1}b_{q,2}\ne0}
 \mathcal T_{p,q}(a_{p,1}\log p,b_{q,2}\log q)
\]

and its multi-trace continuous dimension by this unique functional.  Since
the support is finite, all cofinal limits may be taken independently and
commute with the finite sum.  Therefore

\[
 h_{\rm val}(x)
 =\sum_{p,q}a_{p,1}b_{q,2}\log p\log q
 =d_1(x)d_2(x).
\]

In particular

\[
 h_{\rm val}(t x)=t^2d_1(x)d_2(x)
\]

exactly.  This is an intrinsic dimension functor on the prime-generated
effective sector, unlike raw bounded cardinality and unlike a selected
finite-field image.

Pointwise tropical multiplication, with the degree-zero module inserted on
an absent component, gives associative maps from the packets for x and y to
the packet for x+y.  Thus H_val is a lax symmetric monoidal functor under
divisor addition.  Principal translations commute with these maps.

## 4. Canonical RR, contact and Green lines

Define on the group completion

\[
 F_{RR}^{\rm val}(x)=d_1(x)d_2(x)
\]

and the normed line with distinguished generator

\[
 \|1_x\|=\exp(-F_{RR}^{\rm val}(x)).
\]

Its polarization is

\[
 B_{RR}^{\rm val}(x,y)
 =d_1(x)d_2(y)+d_2(x)d_1(y).
\]

The degree maps extend to the full Arakelov divisor group and annihilate
principal divisors, so this line and its biextension descend genuinely; no
representative is chosen.

Retain the canonical reduced contact line

\[
 C_\Lambda(x,y)=\sum_p
 (x_{p,1}y_{p,2}+x_{p,2}y_{p,1})\log p.
\]

Then

\[
 G_A^{\rm val}=B_{RR}^{\rm val}-C_\Lambda,
 \qquad
 \lambda_G^{\rm val}=\delta\lambda_{RR}^{\rm val}\otimes\lambda_C^{-1}
\]

is canonical.  The former interpolation modulus has disappeared: the
coefficient `1` is the product normalization of two published continuous
dimensions.

## 5. Numerical Neron--Severi and Hodge signature

On the real finite-support prime space `V`, the radical of
`B_RR^val` is `ker(d_1,d_2)`.  Consequently

\[
 N^1_{\rm val}=V/\ker(d_1,d_2)\simeq\mathbb R^2,
 \qquad
 [B_{RR}^{\rm val}]=
 \begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For `H=(1,1)`, `H^2=2` and `H^perp={(a,-a)}` is negative definite.
Thus the numerical Hodge index statement is exact and canonical.

The integral finite-support quotient is still infinite rank.  The valid
reformulation is to use the real numerical Neron--Severi space, which is the
object on which intersection numbers and the Hodge index theorem are
actually formulated.  No claim of a finitely generated integral lattice is
made.

## 6. Exact status

The canonical package

\[
 \mathscr A_{\rm val}=
 (\mathscr Y_A,\operatorname{Div}_A,\operatorname{Prin}_A,
  \mathcal H_{\rm val},\lambda_{RR}^{\rm val},\lambda_C,
  \lambda_G^{\rm val},N^1_{\rm val})
\]

closes normalization and numerical signature on the prime-generated
external sector without a calibration choice.

It does not yet identify `H_val` with the full bounded-section object of
Haran's square; `114_a_147` proves that such an identification is impossible.
It is instead a canonical valuative/tropical replacement functor, justified
by the all-prime ideal valuation and the canonical prime-to-periodic-orbit
map.
