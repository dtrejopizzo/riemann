# E83.006 - Exact Mobius-weighted boundary kernel

## 1. Definitions

Put

```text
sigma=1/2+epsilon,
Z=sum_{n<=exp(L)} n^(-sigma)S_{log n},
M=sum_{d<=exp(L)} mu(d)d^(-sigma)S_{log d}.             (1.1)
```

For `0<=y<=L`, define the gauged boundary commutator

```text
R_y=M[S_y^*,Z].                                       (1.2)
```

For an integer `k`, introduce the truncated divisor sums

```text
D_k(t)=sum_{d|k, d<=exp(t)}mu(d),                      (1.3)

D_k(a,b)=sum_{d|k, exp(a)<=d<=exp(b)}mu(d).            (1.4)
```

The endpoint convention in (1.3)--(1.4) is inclusive.  It matters only on
the discrete set where an exponential endpoint is an integer.

## 2. Boundary formula before the gauge

### Lemma 2.1

For every bounded `f` and almost every `t in [0,L]`, one has

```text
([S_y^*,Z]f)(t)
 =sum_{exp(t)<n<=exp(t+y)}n^(-sigma)f(t+y-log n),
                                      0<=t<=L-y,       (2.1)

([S_y^*,Z]f)(t)
 =-sum_{exp(t+y-L)<=n<=exp(t)}n^(-sigma)f(t+y-log n),
                                      L-y<t<=L.        (2.2)
```

### Proof

The two products are

```text
(S_y^*Zf)(t)
 =1_[0,L-y](t)
  sum_{n<=exp(t+y)}n^(-sigma)f(t+y-log n),             (2.3)

(ZS_y^*f)(t)
 =sum_{exp(max(0,t+y-L))<=n<=exp(t)}
    n^(-sigma)f(t+y-log n).                            (2.4)
```

If `t<=L-y`, the second sum starts at `n=1` and subtracts the initial segment
of the first sum.  If `t>L-y`, the first expression vanishes and (2.4)
remains with a minus sign.  This proves (2.1)--(2.2). `QED`

Formula (2.1) samples `f` at the left endpoint interval `[0,y)`.  Formula
(2.2) is the corresponding right-end truncation.  Thus the boundary nature
is visible without estimating any individual shift.

## 3. Exact Mobius-gauged kernel

### Theorem 3.1

For every bounded `f` and almost every `t`, the operator (1.2) is given by

```text
(R_yf)(t)
 =sum_{exp(t)<k<=exp(t+y)}
    k^(-sigma)D_k(t)f(t+y-log k),
                                      0<=t<=L-y,       (3.1)

(R_yf)(t)
 =sum_{exp(t+y-L)<=k<=exp(t+y)}
    k^(-sigma)D_k(t+y-L,t)f(t+y-log k),
                                      L-y<t<=L.        (3.2)
```

### Proof

Use `MZ=I` to write

```text
R_y=MS_y^*Z-S_y^*.                                    (3.3)
```

Expanding the first term and grouping the pair `(d,n)` by `k=dn` gives

```text
(MS_y^*Zf)(t)
 =sum_k k^(-sigma)
   sum_{d|k,
       exp(max(0,t+y-L))<=d<=exp(t)}mu(d)
   f(t+y-log k),                                      (3.4)
```

where

```text
exp(max(0,t+y-L))<=k<=exp(t+y).                        (3.5)
```

Suppose first that `t<=L-y`.  For `k<=exp(t)`, every divisor of `k` occurs
in the inner sum, and hence

```text
sum_{d|k}mu(d)=1_[k=1].                               (3.6)
```

The `k=1` term cancels the last term of (3.3), every term with
`1<k<=exp(t)` vanishes, and (3.1) remains.  If `t>L-y`, the last term of
(3.3) is zero and the divisor band in (3.4) is exactly the one in (3.2).
This proves the theorem. `QED`

## 4. Consequence for the archimedean commutator

Let `a_L(y)` be the coefficient in E83.005.  On the common smooth core, in
the weak renormalized sense at `y=0`,

```text
M[H_L^A,Z]f=integral_0^L a_L(y)R_yf dy.                (4.1)
```

The full-divisor identity has therefore already been used in (3.1)--(3.2).
What survives is not another Euler product: it is a family of incomplete
divisor sums whose cutoff depends simultaneously on the output coordinate
`t` and the shift coordinate `y`.

## 5. Decision

The expected global Mobius telescope does not occur.  It closes only the
interior range `k<=exp(t)` in (3.4).  The multiplicative shell

```text
exp(t)<k<=exp(t+y)                                     (5.1)
```

and the right boundary divisor band survive exactly.  Consequently the
`BOUNDARY-GAMMA-EULER` target cannot be proved by invoking the untruncated
identity `sum_{d|k}mu(d)=0` after the boundary has been formed.

## 6. Status

```text
proved:
  exact boundary kernel before the Mobius gauge;
  exact incomplete-divisor kernel after the Mobius gauge;
  exact reduction of M[H_L^A,Z] to that kernel;

refuted:
  a complete Mobius telescope of the boundary commutator;

open:
  cancellation of (4.1) on the actual model vector after the safe pairing;
  joint treatment of the finite Fourier compression defect;

next:
  isolate an uncancelled endpoint wedge and decide whether any operator-norm
  version of the desired theorem remains possible.
```

