# 114.a.149 — The canonical Scaling-Site dimension and the bridge gate

## 1. The intrinsic coefficient exists on a different carrier

On the product Scaling topos, functional reduction of the external tropical
tensor gives the bivariate Legendre sheaf

\[
 \mathcal R(H,K)=\{\max_i(h_i x+k_i y+c_i)\}.
\]

For external divisors `D` on the periodic orbit `C_p` and `E` on `C_q`, the
finite-depth tensor section module has intrinsic covering dimension.  The
special-divisor extremal-generator theorem and the squeeze by principal
translations give

\[
 \operatorname{cdim}^{(2)}H^0(D\boxtimes E)
 =\max(\deg D,0)\max(\deg E,0).
\]

Thus this carrier has the desired coefficient `1`, independent of an
interpolation base or a retained-coordinate convention.  This is the
genuine intrinsic candidate that the calibrated Haran quotient was missing.

## 2. A direct homomorphic bridge is impossible

### Proposition 2.1

Let `T` be any idempotent semiring and let `phi: Z -> T` preserve zero, one,
addition and multiplication.  Then

\[
 \phi(n)=1_T\qquad(n\ge1).
\]

In particular no such map remembers a prime `p`, its valuation, or `log p`.

### Proof

Because tropical addition is idempotent,

\[
 \phi(n)=\underbrace{1_T\oplus\cdots\oplus1_T}_{n\text{ times}}=1_T.
\]

Therefore every positive integer, and hence every prime, has the same image.
QED.

The same argument applies to a morphism from the ordinary-ring bio inside
Haran's square to an idempotent target: its unary integer `n`, obtained by
the `n`-fold ordinary sum of the unit, becomes the tropical unit.  Pulling a
prime Cartier multiplier through this map makes it trivial.  Consequently a
direct F-ring/semiring morphism cannot transport simultaneously:

* the actual prime divisors `e_{p,i}`;
* their torsion contact norm `p^{-1}`;
* the canonical Scaling-Site continuous dimension.

## 3. Exact remaining construction

The viable bridge cannot be an ordinary homomorphism.  It must be a valued,
hyperfield, bend-congruence, or dequantization construction in which the
inequality

\[
 v(a+b)\ge\min(v(a),v(b))
\]

replaces preservation of addition and the prime value `v(p)=log p` survives.
It must then prove all of:

1. a functor from the supportwise regular Cartier sector to the bivariate
   Legendre sheaf;
2. transport of completed divisor torsors and their principal isometries;
3. identification of its external bounded sections with the tropical tensor
   modules;
4. equality of normalized dimension with the coefficient-one formula;
5. compatibility of the reduced prime contact determinant.

Until this valued comparison is constructed, the Scaling-Site theorem does
not canonically normalize the Haran determinant line.  The two results are
compatible numerical shadows on different carriers, not yet one row-A
object.

## 4. Verdict

`SCALING_EXTERNAL_DIMENSION: CLOSED`.

`DIRECT_HARAN_TO_IDEMPOTENT_BRIDGE: CLOSED_NO_GO`.

`VALUED_CARTIER_TROPICALIZATION: OPEN`.

This is now the unique constructive normalization gate if the unpolarized
row A is required while retaining Haran's prime/contact geometry.
