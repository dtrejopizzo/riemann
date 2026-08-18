# E101.031 - Blaschke safe uniqueness

## 1. Half-plane uniqueness set

Fix `a>0` and let

```text
H_a={z:Re z>a}.                                      (1.1)
```

### Lemma 1.1

If a bounded analytic function on `H_a` vanishes at every integer
`n>=n_0>a`, then it vanishes identically.

### Proof

Translate by `a` and map the right half-plane to the unit disk by

```text
w=(z-a-1)/(z-a+1).                                  (1.2)
```

For all sufficiently large `n`, the integer zero maps to a real point `w_n`
with

```text
1-|w_n|=2/(n-a+1).                                   (1.3)
```

The zeros of a nonzero bounded analytic function in the disk satisfy the
Blaschke condition

```text
sum_n(1-|w_n|)<infinity.                             (1.4)
```

Equation (1.3) makes this sum divergent.  Hence the function is identically
zero. `QED`

## 2. Boundedness of the two candidate transforms

Let `g` be any subsequential limit of finite core Stieltjes transforms with

```text
sup_alpha g_alpha(x_0)<infinity                      (2.1)
```

at one positive point.  Its Stieltjes representation gives, for every
`a>0`,

```text
sup_(z in H_a)|g(z)|<infinity.                       (2.2)
```

Indeed `(t+x_0)/(t+z)` is uniformly bounded for `t>=0` and `Re z>a`.

For `a>1/4`, the principal square root satisfies

```text
Re sqrt(z)>sqrt(a),
z in H_a.                                            (2.3)
```

Thus `s=1/2+sqrt(z)` remains in a closed sub-half-plane of `Re s>1`.
The Euler--Gamma formula E101.020(2.4), Stirling's bound and absolute prime
convergence show

```text
sup_(z in H_a)|g_Xi(z)|<infinity.                    (2.4)
```

## 3. Integer-set closure theorem

### Theorem 3.1

Assume, along one directed family, that for some integer `n_0>1/4`,

```text
g_alpha(n)->g_Xi(n)
for every integer n>=n_0.                            (3.1)
```

Then `Omega7` holds.

### Proof

The case `n=n_0` bounds the Stieltjes masses at `n_0`, so the family has
locally convergent subnets on every `H_a`, `a>1/4`.  Let `g` be a sublimit.
The bounded analytic function `g-g_Xi` vanishes at all integers `n>=n_0` by
(3.1).  Lemma 1.1 gives `g=g_Xi` on `H_a`.  Hence `g_Xi` belongs to the
Stieltjes class, and E101.021 gives `Omega7`. `QED`

## 4. Cofactor version

By E101.022 and independent Euler convergence, it is enough to prove

```text
INTEGER-COFACTOR-IDENT:
D_(L_alpha,N_alpha)(1/2+sqrt(n))->0
for every integer n>=n_0                            (4.1)
```

along one directed family.

The order of quantifiers is essential:

```text
admissible:    for every fixed n, take alpha->infinity;
insufficient:  test only n=n_alpha->infinity.        (4.2)
```

The second line is the drifting regime rejected by E101.026.  The first line
is a Blaschke uniqueness set and retains the complete analytic information.

## 5. General uniqueness sequences

The integers may be replaced by any sequence `x_j in H_a` satisfying the
half-plane Blaschke divergence

```text
sum_j Re(x_j-a)/(1+|x_j-a|^2)=infinity.              (5.1)
```

This permits the determining set to be chosen for arithmetic convenience
without requiring an interior accumulation point.

## 6. Status

```text
proved:
  half-plane Blaschke uniqueness lemma;
  boundedness of the Stieltjes and Euler--Gamma candidates;
  integer-set closure theorem;
  INTEGER-COFACTOR-IDENT implies Omega7;

open:
  INTEGER-COFACTOR-IDENT.
```
