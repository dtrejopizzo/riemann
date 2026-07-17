# E72.258 -- Rational strict LM8 probe

**Purpose.** Convert the strict homogeneous LM8 majorant of E72.256--E72.257 into explicit
decimal-rational coefficients. This removes the dimensional constant drift found in E72.247 and gives
a proof-facing object:

```text
P_j(u)=u^2 R_j(u),        P_j(0)=P_j'(0)=0.
```

The required univariate inequalities are checked at the `R` level, not at the `P` level:

```text
R_j(u) >= 1                 for -1 <= u <= 0,
R_j(u) >= (1-a_j)^2         for  0 <= u <= 1.
```

This is the correction to the near-zero double-root issue exposed in E72.254--E72.256.

## Rational coefficients

Rounding the strict buffered degree-8 `R` coefficients to six decimals still passes the interval and
stress checks. Thus the following coefficients may be read as rationals with denominator `10^6`:

```text
R0(u) =
  1.000199
 -2.612680 u
-19.804312 u^2
+12.299851 u^3
+299.698952 u^4
+14.347638 u^5
-1797.470005 u^6
-192.790165 u^7
+3715.980490 u^8

R1(u) =
  1.000732
 -1.539636 u
 -8.755675 u^2
 -5.533524 u^3
+46.182864 u^4
+84.054306 u^5
 +3.002174 u^6
-77.401146 u^7
-40.848595 u^8
```

Here `a_0=0.70`, `a_1=0.60`.

## Floating interval margins

The six-decimal rational grid reports:

```text
min R0(u)-1       on [-1,0] = +1.990000e-04
min R0(u)-0.09    on [ 0,1] = +1.496688e-03
min R1(u)-1       on [-1,0] = +7.320000e-04
min R1(u)-0.16    on [ 0,1] = +1.497781e-03
```

The interval margins are comfortably larger than the rounding scale. E72.259 replaces this floating
check by an exact rational Bernstein-subdivision certificate.

## Stress check

With the same rounded coefficients and no refit, the selected extended windows give:

```text
lambda=16  env=8.709152e-01  slack=+6.998482e-02
lambda=32  env=6.224936e-01  slack=+3.184064e-01
lambda=56  env=7.332795e-01  slack=+2.076205e-01
```

The worst selected value is still `lambda=16`, far below the target `0.9409`.

## Status

This does not prove the whole RFBD package. It proves that the LM8 envelope can be made homogeneous,
strict, and rational without losing the observed margin. The remaining proof-facing step for this
sublemma is exact interval certification of the four rational polynomial inequalities, followed by a
separate uniform argument that the model moments obey the required bounds.
