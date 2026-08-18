# E101.035 - Planted heat falsifier

## 1. Off-line squared pole

Let a planted off-line zero have centered coordinate

```text
z=a+i gamma,
a!=0,                                                (1.1)
```

and put

```text
alpha=z^2.                                           (1.2)
```

The conjugate pair of squared poles contributes, up to its positive
multiplicity,

```text
q_alpha(x)
 =1/(x-alpha)+1/(x-conjugate(alpha)).                (1.3)
```

For the numerical plant `z=0.4+3i`,

```text
alpha=-8.84+2.4i.                                    (1.4)
```

## 2. Integer generating signal

For `n_0>=1`, define

```text
Q_alpha(q)
 =sum_(k>=0)q^k q_alpha(n_0+k).                      (2.1)
```

Since `Re(n_0-alpha)>0`, direct integration gives

```text
Q_alpha(q)
 =2Re integral_0^1
    y^(n_0-alpha-1)/(1-qy)dy.                        (2.2)
```

The corresponding real Hausdorff density is

```text
2y^(n_0-Re(alpha)-1)
 cos(Im(alpha)log y).                                (2.3)
```

For (1.4), the cosine factor is

```text
cos(2.4log y),                                       (2.4)
```

which changes sign infinitely often as `y` approaches zero.  A positive
beta mixture cannot create a nonreal exponent or this logarithmic
oscillation.

## 3. Structural exclusion

Every positive beta mixture has, in the heat coordinate `v=-log y`, the form

```text
p(v)=integral_[0,infinity)
      (n_0+t)exp(-(n_0+t)v)d nu(t),                  (3.1)
```

with real rates.  Its Mellin transform can have singularities only on

```text
x=-t,
t>=0.                                                (3.2)
```

The planted term has singularities at `alpha` and its conjugate, outside the
negative real axis.  No positive real-rate mixture can reproduce these poles.
Hence the beta-mixture discriminant rejects the plant for the same structural
reason that the Stieltjes discriminant rejects an off-line zero.

## 4. Fixed tests versus drifting tests

At a drifting integer `n->infinity`,

```text
q_alpha(n)
 =2/n+2Re(alpha)/n^2+O(n^(-3)),                     (4.1)
```

so the nonreal displacement is progressively hidden.  In contrast, the full
function `Q_alpha(q)` contains every fixed coefficient and retains the two
nonreal poles through (2.2).

This verifies the quantifier distinction:

```text
all fixed integer coefficients:  plant-sensitive;
one drifting integer:             plant-insensitive. (4.2)
```

At `n_0=1` and `q=0.4`, direct summation of (2.1) and quadrature of (2.2)
both give

```text
0.303533595491473453311678107612,                   (4.3)
```

with residual below `1e-59`.

## 5. Audit consequence

Any proposed estimate for E101.034 must fail when the arithmetic target is
modified by (1.3).  An estimate based only on decay as `k->infinity`, on
Hausdorff finite-difference signs, or on positivity of the kernel in (3.6)
does not meet this requirement.  The proof must retain the real-rate
beta-mixture structure or the complete coupled cofactor defect.

## 6. Status

```text
proved:
  exact disk signal of one planted off-line quartet;
  oscillatory Hausdorff density of the planted contribution;
  incompatibility with positive real-rate beta mixtures;
  preservation of the plant signal by fixed integer coefficients;

open:
  arithmetic vanishing of the unmodified cofactor generating current.
```
