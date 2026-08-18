# Phase 96 closure - Global von Mangoldt response

## 1. Closed mathematics

The characteristic Jacobian has the exact expansion

```text
Jac(P,chi)
 =-sum_n Lambda(n)n^(-1/2)J_(log n)(P,chi).          (1.1)
```

After bilateral base-point subtraction, the bordered deformation current is

```text
BJ_t(s;s_*)
 =sum_n Lambda(n)n^(-1/2)BR_t(s;s_*;log n).          (1.2)
```

The independent Euler current uses the same weights with kernel

```text
E(s;s_*;y)
 =(2/y)[exp(-(s-1/2)y)-exp(-(s_*-1/2)y)].            (1.3)
```

## 2. Exact remaining scalar

The direct anchor is the signed cancellation

```text
BASE
 +sum_n Lambda(n)n^(-1/2)
  integral_0^1(BR_t-E)dt
 ->0.                                                 (2.1)
```

No inverse, eigenvector, zero list or moving-level derivative occurs.

## 3. Closure grade

```text
closed:
  polarized determinant derivative;
  cellwise Jacobian expansion;
  bilateral response kernel;
  exact Euler-kernel defect;
  termwise-matching autopsy;

open and transferred:
  DETERMINANTAL-PRIME-RESPONSE;
  DIRECT-BORDERED-ANCHOR and Omega7.
```

