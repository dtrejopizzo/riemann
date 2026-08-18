# E101.033 - Beta-mixture discriminant

## 1. The explicit arithmetic sequence

Fix an integer `n_0>=1` and set

```text
a_k=g_Xi(n_0+k),
k>=0.                                                (1.1)
```

Every number in (1.1) is given in the absolute Euler region by
E101.020(2.4).  No zero list enters its definition.

## 2. Exact discrete criterion

### Theorem 2.1

`Omega7` is equivalent to the existence of a finite positive measure `nu`
on `[0,infinity)` such that

```text
a_k
 =integral_[0,infinity]
    (n_0+t)/(n_0+k+t)d nu(t)
for every k>=0.                                      (2.1)
```

### Proof

Suppose first that `Omega7` holds.  By E101.021,

```text
g_Xi(z)=integral_[0,infinity)d mu(t)/(z+t).          (2.2)
```

Set `d nu(t)=d mu(t)/(n_0+t)`.  Its total mass is `g_Xi(n_0)`, and evaluation
of (2.2) at `z=n_0+k` gives (2.1).

Conversely, assume (2.1) and define

```text
F(z)
 =integral_[0,infinity]
    (n_0+t)/(z+t)d nu(t).                            (2.3)
```

On every half-plane to the right of a positive vertical line, `F` is bounded
and analytic.  It agrees with the bounded analytic function `g_Xi` at all
integers `n_0+k`.  E101.031 implies `F=g_Xi` there.  With

```text
d mu(t)=(n_0+t)d nu(t),                              (2.4)
```

equation (2.3) is a positive Stieltjes representation of `g_Xi`.  The
Stieltjes discriminant E101.021 gives `Omega7`. `QED`

The representing Hausdorff measure of the sequence is, equivalently,

```text
lambda=integral_[0,infinity) beta_t d nu(t),         (2.5)
```

with the beta laws of E101.032.

## 3. Exponential-mixture form

Under `y=exp(-v)`, the beta law becomes

```text
d beta_t(v)
 =(n_0+t)exp(-(n_0+t)v)dv,
v>0.                                                 (3.1)
```

Therefore (2.1) says that the unique Hausdorff measure of `{a_k}` must become
a positive mixture of exponential laws whose rates lie in `[n_0,infinity)`.
Equivalently, away from `v=0` it must have a density

```text
p(v)=exp(-n_0v)h(v),                                 (3.2)
```

where

```text
h(v)=integral_[0,infinity)
       (n_0+t)exp(-tv)d nu(t)                        (3.3)
```

is completely monotone.  The target asymptotic excludes an atom at `v=0`.

Thus the force-bearing discrete assertion is not merely that `{a_k}` is a
Hausdorff moment sequence.  Its unique Hausdorff measure must lie in the
strict beta-mixture subcone (2.5).

## 4. Ordinary finite-difference positivity is insufficient

For every finite core approximant,

```text
(-1)^j Delta^j g_alpha(n_0+k)
 =j! sum_r
   1/prod_(ell=0)^j(n_0+k+r^2+ell)
 >=0.                                                (4.1)
```

These inequalities survive pointwise limits and characterize the larger
Hausdorff cone.  They do not characterize the beta-mixture cone.

To see the strict gap, choose `0<c<1` and put

```text
b_k=c^k.                                             (4.2)
```

This is the Hausdorff moment sequence of `delta_c`, and

```text
(-1)^j Delta^j b_k=c^k(1-c)^j>=0                    (4.3)
```

for all `j,k`.  It cannot have a representation (2.1).  Indeed, any nonzero
finite positive `nu` assigns positive mass to `[0,T]` for some finite `T`,
and then

```text
integral (n_0+t)/(n_0+k+t)d nu(t)
 >=C_T/(n_0+k+T),                                    (4.4)
```

which cannot decay geometrically.  An endpoint atom would instead have a
nonzero limit.

Equivalently, the bounded analytic interpolation

```text
B(z)=c^(z-n_0)                                       (4.5)
```

is completely monotone on the positive axis but is not Stieltjes.  For a
nonzero Stieltjes function without a constant term, `xB(x)` cannot eventually
decrease to zero.

## 5. Consequence for the proof search

Checking all signs in (4.1), even if achieved arithmetically, would not close
`Omega7`.  A valid discrete proof must establish the exponential-mixture
structure (3.1)--(3.3), or must obtain it as a limit of the finite secular
measures through `INTEGER-COFACTOR-IDENT`.

## 6. Status

```text
proved:
  an exact discrete beta-mixture criterion equivalent to Omega7;
  an exponential-mixture form of the same criterion;
  strict insufficiency of the complete Hausdorff finite-difference hierarchy;

open:
  arithmetic construction of the beta-mixture representation, equivalently
  INTEGER-COFACTOR-IDENT.
```
