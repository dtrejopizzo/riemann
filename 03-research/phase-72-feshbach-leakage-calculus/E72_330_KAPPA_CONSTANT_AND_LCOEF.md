# E72.330 -- Kappa is constant and the left coefficient is coercive

**Purpose.** Close the elementary endpoint-normalization gate left open in E72.328. The scalar
`kappa_L=Arch_0(1)` is independent of `L`, up to the fixed convention constant of the Hadamard finite
part. Therefore it cannot cancel the pole-even gap.

## 1. Recall the definitions

From E72.319 and E72.328,

```text
kappa_L=Arch_0(1),
```

where

```text
Arch_0(B)
:= Ren int_0^L e^(y/2)B(y)/(2sinh y)dy - WR(B).
```

The WR normalization is

```text
WR(B)=1/2(LOG4PI+gamma)B(0)
      + int_0^L (e^(y/2)B(y)-B(0))/(2sinh y)dy
      + 1/2 B(0)log(tanh(L/2)).
```

For `B=1`,

```text
WR(1)=1/2(LOG4PI+gamma)
      + int_0^L (e^(y/2)-1)/(2sinh y)dy
      + 1/2 log(tanh(L/2)).                            (1)
```

## 2. Finite-part split

Use the same finite-part convention in `Ren` as in the WR endpoint subtraction. Then

```text
Ren int_0^L e^(y/2)/(2sinh y)dy
= int_0^L (e^(y/2)-1)/(2sinh y)dy
   + FP int_0^L 1/(2sinh y)dy.                         (2)
```

Since

```text
int 1/(2sinh y)dy = 1/2 log(tanh(y/2)),
```

the finite part is

```text
FP int_0^L 1/(2sinh y)dy
= 1/2 log(tanh(L/2)) + c_FP,                           (3)
```

where `c_FP` is a constant depending only on the chosen finite-part convention at `0`.

Substituting (1)--(3),

```text
kappa_L
= c_FP - 1/2(LOG4PI+gamma).                            (4)
```

Thus

```text
kappa_L=kappa_* = O(1).                                (5)
```

No `L`-dependent term survives.

## 3. Left coefficient

The transformed packet equation uses

```text
Lambda_L:=mu+e_pole-2kappa_*.
```

In the pole-relative normalization, `mu` is the actual pole-even gap above the pole energy. Therefore
the proof-facing lower bound is:

```text
GAP:
mu+e_pole >= c L^2
```

or, equivalently in the convention where `e_pole` has already been absorbed into `mu`,

```text
mu >= cL^2.
```

Since `kappa_*` is constant, either version gives

```text
|Lambda_L| >= c' L^2
```

for all sufficiently large `L`, after adjusting finite low windows separately.

## 4. Status

```text
proved: kappa_L is an L-independent finite-part constant;
closed: GAP/LCOEF follows from the pole-even gap lower bound.
```

The transformed route now has only the two analytic tail gates:

```text
TAIL-POLY,
OUT-POLY.
```
