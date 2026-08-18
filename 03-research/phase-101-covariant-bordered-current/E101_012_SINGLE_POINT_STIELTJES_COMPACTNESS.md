# E101.012 - Single-point Stieltjes compactness

## 1. Canonical products

Let

```text
F_alpha(z)=c_alpha product_j(1-z^2/r_(alpha,j)^2)    (1.1)
```

be even real entire functions of order at most one whose nonzero zeros are
real.  Fix `sigma_0>0` and normalize by

```text
Theta_alpha(z)=F_alpha(z)/F_alpha(i sigma_0).         (1.2)
```

Define the safe Stieltjes mass

```text
M_alpha(sigma_0)
 =sum_j 1/[r_(alpha,j)^2+sigma_0^2].                 (1.3)
```

Repeated zeros are counted with multiplicity.

## 2. One-point compactness theorem

### Theorem 2.1

The family `Theta_alpha` is locally bounded on the plane if and only if

```text
sup_alpha M_alpha(sigma_0)<infinity.                 (2.1)
```

### Proof: mass bound implies local boundedness

For `R>=sigma_0`, the canonical product and
`log(1+x)<=x` give

```text
log[F_alpha(iR)/F_alpha(i sigma_0)]
 =sum_j log{1+(R^2-sigma_0^2)
                 /[r_(alpha,j)^2+sigma_0^2]}
 <=(R^2-sigma_0^2)M_alpha(sigma_0).                 (2.2)
```

For `R<sigma_0`, the same ratio is at most one.  Real-rooted domination gives

```text
sup_(|z|<=R)|Theta_alpha(z)|
 <=max{1,exp[(R^2-sigma_0^2)M_alpha(sigma_0)]}.       (2.3)
```

Thus (2.1) bounds the family on every disk.

### Proof: local boundedness implies mass bound

Differentiate the product on the safe axis.  Since
`Theta_alpha(i sigma_0)=1`,

```text
d/d sigma Theta_alpha(i sigma)|_(sigma=sigma_0)
 =2 sigma_0 M_alpha(sigma_0).                        (2.4)
```

Local boundedness near `i sigma_0` bounds the complex derivatives there by
Cauchy's estimate.  Equation (2.4) then proves (2.1). `QED`

## 3. Exact logarithmic form

Equation (2.4) is equivalently

```text
M_alpha(sigma_0)
 ={1/[2 sigma_0]}
  d/d sigma log Theta_alpha(i sigma)|_(sigma=sigma_0).
                                                               (3.1)
```

For the bordered characteristic, the right side is an explicit safe cofactor
ratio of Phase 94.  Hence compactness is reduced to one scalar upper bound at
the normalization point; no zero locations are required as input.

## 4. Status

```text
proved:
  equivalence of global local boundedness and one safe Stieltjes-mass bound;
  exact safe logarithmic-derivative formula;
  reduction of compactness to one finite cofactor scalar.
```

