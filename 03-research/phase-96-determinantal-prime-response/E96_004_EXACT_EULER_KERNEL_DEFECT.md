# E96.004 - Exact Euler-kernel defect

## 1. Euler current in the same weights

Let `y=log n` and `u=s-1/2`.  Since

```text
n^(-s)=n^(-1/2)exp(-uy),                              (1.1)
```

the projective Euler current is

```text
J_L(s)-J_L(s_*)
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)E(s;s_*;log n),                  (1.2)

E(s;s_*;y)
 =(2/y)[exp(-uy)-exp(-u_*y)].                         (1.3)
```

## 2. Exact deformation defect

Subtract (1.2) from E96.003(2.2):

```text
AJ_t(s;s_*)
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)
   [BR_t(s;s_*;log n)-E(s;s_*;log n)].               (2.1)
```

This is an identity before any limit.

## 3. Integrated kernel target

Including the archimedean base term, the direct anchor is equivalent to

```text
BASE_(L,N)(s;s_*)
 +sum_(2<=n<=exp L)Lambda(n)n^(-1/2)
  integral_0^1
   [BR_t(s;s_*;log n)-E(s;s_*;log n)]dt
 ->0.                                                 (3.1)
```

The integral of `E` is itself because it is independent of `t`.

## 4. Status

```text
proved:
  exact Euler kernel in CCM prime weights;
  exact global arithmetic kernel defect;

open:
  signed cofinal cancellation in (3.1).
```

