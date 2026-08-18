# 114.a.115 — H7: local contact is not the Riemann--Roch intersection

```
+------------------------------------------------------------------------+
| LOCAL       a114 gives delta_(p,q) log p on the reduced contact block.  |
| RR          a34/a53 force c log p log q, c=1/(2 log 3), if H7-RR0 holds.|
| MISMATCH    The two values differ for every pair of rational primes.    |
| EXCESS      Full geometry must supply c log p log q-delta_(p,q) log p.  |
| MEANING     Lambda contact and global RR intersection are distinct maps.|
+------------------------------------------------------------------------+
```

## 1. The two independently forced quantities

For prime-axis generators, `a114` constructs the reduced contact pairing

\[
 C_{p,q}:=I_{12}^{\rm red}(D_{p,1},D_{q,2})
 =\delta_{p,q}\log p.                                                   \tag{1.1}
\]

Independently, the optimal bounded code of `a34`, extended continuously in
Picard degree by `a53`, has

\[
 h_{\rm code}(tD)
 =\frac{1}{2\log3}\deg_1(D_1)\deg_2(D_2)t^2+O(t\log t).                \tag{1.2}
\]

If H7-RR0 promotes this coefficient to

\[
 h^0_{\rm norm}(tD)=\frac12 I_{\rm RR}(D,D)t^2+o(t^2)                  \tag{1.3}
\]

with square-zero ruling axes, polarization forces

\[
 R_{p,q}:=I_{\rm RR}(D_{p,1},D_{q,2})
 =\frac{\log p\log q}{2\log3}.                                        \tag{1.4}
\]

Equation (1.1) is unconditional on the reduced contact quotient.  Equation
(1.4) is a forced target conditional on H7-RR0; it is not yet a constructed
intersection.

## 2. Exact mismatch theorem

### Theorem 2.1

For every pair of rational primes `p,q`,

\[
 C_{p,q}\ne R_{p,q}.                                                    \tag{2.1}
\]

### Proof

If `p!=q`, the left side is zero while the right side is positive.  If
`p=q`, equality would give

\[
 \log p=\frac{(\log p)^2}{2\log3}.
\]

Since `log p>0`, this implies `log p=2 log 3=log 9`, hence `p=9`, which is
not prime.  QED.

The mismatch persists under all positive multiplicities: both sides scale by
`mn`, so no Veronese regrading repairs it.

## 3. The forced complementary contribution

If a full intersection both projects to the local contact and satisfies the
RR coefficient, its complementary generalized/archimedean contribution on
prime generators is forced to be

\[
 E_{p,q}^{\rm forced}
 =\frac{\log p\log q}{2\log3}-\delta_{p,q}\log p.                       \tag{3.1}
\]

For distinct primes this entire positive RR intersection lies in the
complementary sector, consistent with `a114`: the cross quotient has no
nonzero finite scalar bio, so ordinary residue cardinality cannot see it.
For equal primes, (3.1) is the correction to the selected `F_p` contact; it
may have either sign and cannot be interpreted as the cardinality of one
finite set.

Formula (3.1) is a **required value**, not a construction of the excess.
The actual task is to produce a functorial complex/gauge whose Euler/Green
degree equals it and obeys the product formula.

## 4. Consequence for A

There must be two compatible but distinct outputs:

1. a local/reduced contact functor carrying `Lambda`;
2. a global principal-invariant RR intersection carrying the quadratic
   degree product.

Identifying them is impossible already on prime generators.  This is the
Haran-square analogue of the principal-invariance distinction in `a09`, where
finite resultants are local contributions rather than global intersections.

The remaining gate is sharpened to:

> **H7-REG-EXCESS-RR.** Construct the complementary intersection/Green
> complex on `Y^reg`, prove its prime-axis degree is (3.1), and prove that its
> sum with the reduced contact satisfies H7-RR0 and principal invariance.

This theorem prevents a false closure but does not prove H7-RR0,
H7-REG-INTER, row A or RH.

## 5. Verification scope

`114_a_115_h7_contact_vs_rr_verify.py` checks positivity off the diagonal,
the exact `p=9` contradiction on the diagonal, multiplicity scaling and the
forced excess identity over a prime grid.  It does not construct the excess.
