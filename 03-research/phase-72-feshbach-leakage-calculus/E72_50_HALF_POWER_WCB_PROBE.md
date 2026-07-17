# E72.50 -- Half-power weighted channel probe

**Date:** 2026-07-08.
**Role:** measure the actual weighted endpoint scalar channel and identify the sharp quantitative target.

## 0. Quantity measured

For:

```text
S_x(z)=sum_{n<=x}(n/x)^zT_{x,n},
v_{x,s}=C_x^(-1)Q_x(sI-D_x)^(-1)1_x,
```

measure:

```text
N_x(s;z)=<v_{x,s},S_x(z)k_x>.
```

The scalar WRL route needs:

```text
N_x(s;z)->0.
```

The half-power scale from E72.49 asks whether:

```text
sqrt(x) |N_x(s;z)|
```

remains bounded or tends to zero.

## 1. Numerical signal

Representative values:

```text
z=6:
  x=64    |N_x|=1.75e-3, sqrt(x)|N_x|=1.40e-2
  x=100   |N_x|=1.73e-3, sqrt(x)|N_x|=1.73e-2
  x=144   |N_x|=5.40e-4, sqrt(x)|N_x|=6.48e-3
  x=256   |N_x|=2.60e-4, sqrt(x)|N_x|=4.15e-3

z=10:
  x=64    |N_x|=8.36e-4, sqrt(x)|N_x|=6.69e-3
  x=100   |N_x|=8.51e-4, sqrt(x)|N_x|=8.51e-3
  x=144   |N_x|=1.91e-4, sqrt(x)|N_x|=2.29e-3
  x=256   |N_x|=2.46e-4, sqrt(x)|N_x|=3.93e-3

z=14:
  x=64    |N_x|=4.99e-4, sqrt(x)|N_x|=3.99e-3
  x=100   |N_x|=4.90e-4, sqrt(x)|N_x|=4.90e-3
  x=144   |N_x|=8.39e-5, sqrt(x)|N_x|=1.01e-3
  x=256   |N_x|=2.16e-4, sqrt(x)|N_x|=3.45e-3
```

The raw compressed vector is not itself half-power small:

```text
||v_{x,s}|| ~ 1e-1 to 1
```

on these tests. The smallness is in the scalar endpoint channel.

## 2. Correct theorem target

### Half-Power Weighted Channel Bound

For fixed compact height windows and two Cauchy heights:

```text
sup_{z in K} sqrt(x)
|<C_x^(-1)Q_x(sI-D_x)^(-1)1_x, S_x(z)k_x>|
 -> 0
```

or at least remains bounded with an additional PNT decay factor in the discrepancy formulation.

This is stronger than WCB and exactly supplies the missing half-power from E72.49.

## 3. Mechanism indicated by data

The half-power is not coming from:

```text
||v_{x,s}|| -> 0.
```

It must come from:

```text
endpoint taper + finite Fourier overlap + scalar phase cancellation
```

inside the matrix element.

Thus the proof should work directly with the scalar function:

```text
a_{x,s}(y)=<v_{x,s},Q_x(y)k_x>,
```

not with operator norms.

## 4. Status

```text
observed: half-power smallness in the weighted scalar endpoint channel;
open: prove Half-Power WCB from the finite Fourier-prime scalar transform.
```

The next proof step is to express `a_{x,s}(y)` as a finite trigonometric polynomial and apply explicit
prime exponential-sum estimates at its finite frequency set.
