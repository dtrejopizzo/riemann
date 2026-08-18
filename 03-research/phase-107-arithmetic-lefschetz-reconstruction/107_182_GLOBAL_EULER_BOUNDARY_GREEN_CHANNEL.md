# 107.182 -- The localized boundary classes assemble to the Euler Green channel

## 1. Reduced local class

For a prime \(p\) and \(\Re(s)>1\), evaluate the normal character at

\[
 t_p(s)=p^{-s}.
\]

The local inverse-Euler class of `107_178` is

\[
 \mathscr L_p(s)={1\over1-t_p(s)}.
\]

Its identity contribution is the \(k=0\) term.  Removing it gives the
reduced boundary class

\[
 \mathscr B_p(s)=\mathscr L_p(s)-1
 ={p^{-s}\over1-p^{-s}}
 =\sum_{k\ge1}p^{-ks}.
 \tag{1.1}
\]

This subtraction is forced by the Euler expansion: closed prime orbits
begin at the first positive iterate, while the identity/generic term is
handled separately by the white-light renormalization.

## 2. Global assembly

Weight (1.1) by the orbit length \(\log p\).  For \(\Re(s)>1\), the
series

\[
 \mathscr G_{\rm fin}(s)
 =\sum_p\log p\,\mathscr B_p(s)
 =\sum_p\sum_{k\ge1}\log p\,p^{-ks}
 \tag{2.1}
\]

converges absolutely.  By the Euler product,

\[
 \boxed{
 \mathscr G_{\rm fin}(s)=-{\zeta'(s)\over\zeta(s)}.}
 \tag{2.2}
\]

Thus the local equivariant boundary class is not merely numerically
compatible with the prime source.  After the canonical reduction and
orbit-length weighting, its global sum is exactly the logarithmic
derivative of the finite Euler factor.

## 3. Geometric interpretation

Equation (2.1) gives the first global convergent realization map for the
new boundary route:

\[
 (p,k)\longmapsto
 \log p\,t_p(s)^k.
\]

The denominator \((1-t_p)^{-1}\) is the localized normal Euler class;
the power \(t_p^k\) is the \(k\)-fold closed-orbit iterate; and
\(\log p\) is its geometric period.  These are precisely the three
pieces already present in the Deninger and Connes--Consani systems.

The Davenport--Heilbronn falsifier is respected: a Dirichlet series
without an Euler product has no canonical prime-indexed family
\(\mathscr B_p\), so (2.1) is unavailable.  The construction therefore
does not promote generic functional-equation data to geometry.

## 4. Result and remaining extension

The finite-prime Green channel is constructed and source-derived in the
half-plane of absolute convergence.  It still does not provide:

1. meromorphic/distributional continuation of the boundary class to the
   critical strip;
2. the archimedean Gamma and pole classes;
3. a divisor-valued rather than scalar-valued global realization;
4. a bilinear self-intersection whose value is Weil's quadratic form.

The next forced operation is to add the archimedean logarithmic
derivative and then Mellin-invert the completed channel on compactly
supported Weil tests.  Only that test-function-valued distribution can
be compared with a Green current and a primitive Hodge class.

## 5. Falsifier

The verifier checks the exact prime-power coefficient dictionary and
compares prime truncations of (2.1) with
\(-\zeta'/\zeta\) at several real and complex points.  The truncation
cutoff is fixed before evaluation, errors must decrease on the real
axis, and the final numerical tolerance is fixed.  Any mismatch returns
`VERDICT: NO`.
