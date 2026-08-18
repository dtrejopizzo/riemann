# 114.a.50 — H7: a compatible cofinal finite-moment system

```
+--------------------------------------------------------------------------+
| PROBLEM     a_33 changes the residue characteristic with the degree.     |
| SCALE       Use T_j=2^j and one new separating prime ell_j at each scale.|
| MODULUS     M_j=product_{i<=j} ell_i, hence M_j divides M_{j+1}.         |
| TRANSITION  Reduce mod M_j and truncate moments: exact compatibility.     |
| SEPARATE    The newest factor ell_j separates every code at t<=T_j.     |
| SIZE        log M_j=O(T_j), so 2r_j moments still have O(T_j^2) size.    |
| GAIN        Degree functoriality is closed on each fixed effective ray.  |
| OPEN        All-tree cofinality, arbitrary divisors and RR promotion.    |
+--------------------------------------------------------------------------+
```

## 1. Why a single moving prime is not functorial

Fix a two-prime effective ray and write its second denominator as `q^t`.
Let `B` be the maximum of `3` and the finite set of primes occurring in the
fixed ray and its chosen fixed arities.
The construction of `a_33` chooses a prime depending on `(r_t,q^t)`. Distinct
finite fields have no unital transition maps, so those individual quotients
do not form a degree-directed system.

The repair is to retain old residue factors instead of replacing them.

## 2. Cofinal moduli

Put

\[
 T_j=2^j,qquad
 r_j=\left\lfloor\log_3(2^{T_j+1}+1)\right\rfloor,                       \tag{2.1}
\]

and choose the least prime

\[
 \ell_j>H_j:=\max(B^{T_j},3^{r_j}).                                      \tag{2.2}
\]

The sequence is strictly increasing, and no `ell_j` equals any fixed prime
entering a denominator. Define

\[
 M_j=\prod_{i=0}^j\ell_i.                                                \tag{2.3}
\]

Then `M_j|M_{j+1}`. Every denominator formed from the two fixed ray primes
and the bounded tree arities is a unit modulo every `M_j`.

For `0<=s<2r_j`, let

\[
 \chi_{s,j}([x])=x^s\pmod {M_j},qquad
 \mathcal E_j=(\chi_{0,j},\ldots,\chi_{2r_j-1,j}).                       \tag{2.4}
\]

The zeroth moment replaces the moments `1,...,2r` of `a_33`; its Vandermonde
determinant is the standard product of differences.

### Theorem 2.1 (exact transition compatibility)

For `i<=j`, reduction `Z/M_j -> Z/M_i` followed by truncation to the first
`2r_i` coordinates gives

\[
 \pi_{j,i}\circ\mathcal E_j=\mathcal E_i.                               \tag{2.5}
\]

Each component is a ring homomorphism, so (2.5) is compatible with products
of sections as well as degree inclusions.

### Proof

Divisibility `M_i|M_j` makes reduction a unital ring map. Formula (2.4) is
the same integral Laurent evaluation before reduction at every level.
Reducing and truncating therefore commute literally with evaluation. QED.

## 3. Uniform separation below a cofinal scale

### Theorem 3.1

For every `t<=T_j`, the first `2r_t` coordinates of `E_j` separate the
complete balanced code of rank `r_t` and denominator `q^t`.

### Proof

Project (2.4) to its factor modulo `ell_j`. By (2.2),

\[
 \ell_j>q^{T_j}\ge q^t,qquad
 \ell_j>3^{r_j}\ge3^{r_t}.                                                \tag{3.1}
\]

After grouping equal nonzero labels, a difference of two codes has at most
`2r_t` distinct labels and coefficients of absolute value `<3^{r_t}`. The
moment equations for exponents `0,...,v-1` have Vandermonde determinant

\[
 \prod_{a<b}(x_b-x_a),                                                    \tag{3.2}
\]

which is nonzero modulo `ell_j` because all distinct numerator labels lie
between `1` and `q^t<ell_j`, and the denominator is invertible. Thus every
grouped coefficient is zero modulo `ell_j`, hence zero as an integer by
(3.1). Balanced ternary uniqueness then recovers the code. QED.

## 4. Quadratic target size survives compatibility

Bertrand's postulate gives `ell_i<2H_i`. Along the fixed ray,

\[
 \log H_i=O(T_i),qquad
 \log M_j=\sum_{i=0}^j\log\ell_i
          =O\left(\sum_{i=0}^j2^i\right)=O(T_j).                         \tag{4.1}
\]

Since `r_j=Theta(T_j)`, the target obeys

\[
 \log\#(\mathbb Z/M_j\mathbb Z)^{2r_j}
 =2r_j\log M_j=O(T_j^2).                                                  \tag{4.2}
\]

The balanced code at `t=T_j` retains the `Omega(T_j^2)` lower bound from
`a_33`. Hence the compatible system has matching quadratic logarithmic size
on the cofinal sequence. For arbitrary `t`, choose the least `j` with
`t<=T_j<2t`; (4.2) remains `O(t^2)`.

## 5. Exact remaining scope

This closes the **changing-characteristic/degree-transition obstruction** on
every fixed effective two-prime ray. Together with `a_49`, it supplies a
compatible normalized lower/upper package on `A_12`.

`a_51` later replaces the Laurent-only residue maps by finite twisted-bio
evaluations, extending the compatible package to all scalar trees.

It does not yet prove:

1. that `A_12` is dimension-cofinal among every bounded alternating scalar
   tree (H7-FMD-ALL);
2. compatibility when arbitrary divisor presentations introduce one of the
   accumulated residue primes into a denominator;
3. principal-divisor invariance, sheaf exactness or the RR comparison
   H7-RR0.

## 6. Verification scope

`114_a_50_h7_cofinal_moment_verify.py` checks nested moduli, exact transition
maps, exhaustive code separation at small levels and the quadratic target
bound. The asymptotic estimates are proved above.
