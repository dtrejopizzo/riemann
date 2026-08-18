# E101.018 - Two-point mass equivalence

## 1. Safe ratio at two points

Let `Theta_alpha` be the normalized canonical products of E101.012.  Fix

```text
0<sigma_0<tau,
c=tau^2-sigma_0^2.                                  (1.1)
```

Then

```text
log Theta_alpha(i tau)
 =sum_j log{1+c/[r_(alpha,j)^2+sigma_0^2]}.           (1.2)
```

## 2. Quantitative equivalence

### Theorem 2.1

For every member of the family,

```text
{1/c}log Theta_alpha(i tau)
 <=M_alpha(sigma_0)
 <={tau^2/(sigma_0^2 c)}log Theta_alpha(i tau).       (2.1)
```

### Proof

For

```text
x_j=c/[r_(alpha,j)^2+sigma_0^2],                     (2.2)
```

one has

```text
0<=x_j<=c/sigma_0^2,
x_j/(1+x_j)<=log(1+x_j)<=x_j.                        (2.3)
```

Since

```text
1+x_j<=1+c/sigma_0^2=tau^2/sigma_0^2,               (2.4)
```

the lower inequality in (2.3) gives

```text
log(1+x_j)>=
 (sigma_0^2/tau^2)c/[r_(alpha,j)^2+sigma_0^2].       (2.5)
```

Sum (2.3) and (2.5) over `j`. `QED`

## 3. Consequences

For any fixed `tau>sigma_0`, the following statements are equivalent:

```text
sup_alpha Theta_alpha(i tau)<infinity;
sup_alpha M_alpha(sigma_0)<infinity;
local boundedness of Theta_alpha on the plane.       (3.1)
```

The last equivalence is E101.012.  Thus one additional safe value already
contains all compactness information for an even real-rooted normalized
family.

## 4. Status

```text
proved:
  quantitative two-point Stieltjes inequalities;
  equivalence of one safe-value bound, mass bound and global local
  boundedness.
```

