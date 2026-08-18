# 114.a.148 — The current carrier cannot satisfy the unpolarized row-A specification

## Theorem (carrier trilemma)

Keep simultaneously:

1. the supportwise regular pro-square `Y^locreg`;
2. its actual prime-generated integral divisor sector
   `D_pr = direct_sum_p (Z e_{p,1} + Z e_{p,2})`;
3. raw bounded-section cardinality as `h^0`.

Then the unpolarized Weil-strength row A is impossible.  More precisely:

* raw `h^0` has no quadratic surface upper bound;
* the existing finite determinant quotients do not select a unique RR scale;
* the integral numerical divisor group is not finitely generated.

Consequently this is not a list of three proofs still to be supplied.  At
least one of the three retained structures must be changed.  The package
`A_kappa` is a complete polarized numerical reformulation; it is not the
unpolarized Weil analogue.

## Proof

### 1. Raw sections

For

`D_d = 2d e_{2,1} + d e_{q,2}`, `N=2^d`, `Q=q^d`,

the regular-reflection theorem of `114_a_147` gives

`#H^0_bd(Y^locreg,D_d) >= binomial(N+Q-1,N) >= 2^(2^d-1)`.

The divisor bidegree is linear in `d`, whereas the logarithm of this lower
bound is exponential in `d`.  Hence no estimate `log #H^0 = O(d^2)` can
hold.

### 2. RR scale

For every admissible calibration `kappa`, the normalized determinant line
has polarization

`B_kappa(x,y) = c_kappa(d_1(x)d_2(y)+d_2(x)d_1(y))`.

The constructions with exponent bases `3` and `3^j` give distinct positive
coefficients `1/(2 log 3)` and `1/(2j log 3)`.  A generator-preserving
isometry would preserve the norm on `(e_{p,1},e_{q,2})`, hence would force
the coefficients to be equal.  They are therefore inequivalent.  Neither
the carrier, the degree maps, nor the canonical contact determinant chooses
one of them.

### 3. Integral numerical rank

The radical of the total RR form on the real finite-support space is
`ker(d_1,d_2)`, so its real numerical quotient is `R^2`.  On the integral
prime lattice this radical is zero.  Indeed,

`sum_p a_p log p = 0`

implies `product_p p^(a_p)=1`, and unique factorization gives every
`a_p=0`.  Thus the integral numerical quotient is the original countably
infinite-rank prime lattice, not a finitely generated Neron--Severi group.

The three conclusions prove the theorem.  QED.

## Exact surviving closure

After an admissible calibration is declared as polarization data and
numerical equivalence is taken over the real vector space, `A_kappa` has:

* the regular noncollapsed carrier;
* actual Cartier and principal divisor data;
* principal-invariant determinant lines;
* canonical contact and calibrated Green lines;
* a two-dimensional numerical quotient with signature `(1,1)`.

Every assertion in this polarized package is a theorem.  Removing `kappa`
or demanding a finitely generated integral numerical lattice requires a new
construction, not another verification of the current one.
