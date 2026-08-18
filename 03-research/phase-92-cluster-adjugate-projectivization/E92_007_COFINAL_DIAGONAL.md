# E92.007 - Cofinal projective diagonal

## 1. Setup

Let `D={s:Re s>1}` and let

```text
K_1 subset K_2 subset ...                            (1.1)
```

be a compact exhaustion of `D`.  Let `L_m->infinity`.  Suppose normalized
holomorphic profiles satisfy

```text
F_(m,N)->F_m locally uniformly as N->infinity        (1.2)
```

for every fixed `m`, and

```text
F_m->F locally uniformly as m->infinity.             (1.3)
```

### Theorem 1.1

There is a strictly increasing sequence `N_m` such that

```text
F_(m,N_m)->F locally uniformly on D.                  (1.4)
```

### Proof

For each `m`, use (1.2) to choose `N_m>N_(m-1)` with

```text
sup_(s in K_m)|F_(m,N_m)(s)-F_m(s)|<1/m.             (1.5)
```

Fix `r`.  For `m>=r`, `K_r` is contained in `K_m`, so

```text
sup_(K_r)|F_(m,N_m)-F|
 <=1/m+sup_(K_r)|F_m-F|.                             (1.6)
```

The right side tends to zero by (1.3). `QED`

## 2. Projective charts

Apply the theorem after normalizing the bordered numerator in any nonzero
safe chart.  On overlaps, two normalizations differ by a scalar independent
of `s`, so the diagonal is chart-independent.  A finite change of chart does
not affect local convergence.

## 3. Consequence

Cofinal compatibility is automatic once the two iterated local convergence
statements have been proved.  It requires no quantitative rate connecting
`N` and `L`.

For the endpoint program, (1.2) is fixed-`L` projective convergence and (1.3)
contains the outer arithmetic anchor.  The diagonal theorem combines them but
does not prove either one.

## 4. Status

```text
proved:
  cofinal projective diagonal without a uniform rate;

closed as an independent obligation:
  cofinal compatibility;

open:
  fixed-L projective convergence;
  outer arithmetic identification.
```

