# E74.7 - Cell divisibility probe target

Date: 2026-07-16.

## Question

Does the constraint

```text
Q_w eta=0
```

force the cell packet

```text
B(y)=qQ_yeta
```

to carry a visible finite divisibility factor before applying the Gamma-prime
functional?

The desired proof shape would be:

```text
B(y)=D_w[y] C(y),
```

where `D_w` is an explicit factor coming from the two vanished Cauchy
functionals and `F_L[D_w C]` gains rapid decay by finite integration by parts
or by the already closed critical-line polynomial bounds.

## Probe to run next

For the real harness:

1. build `eta=(I-P_w)xi_L`;
2. sample `B(y)=qQ_yeta` on the interval `0<=y<=L`;
3. test endpoint and rational-factor consequences of `Q_weta=0`:

```text
B(0), B(L), B'(0), B'(L),
int_0^L e^{-wy}B(y)dy,
int_0^L e^{wy}B(y)dy.
```

The integrals are the important tests: the Cauchy constraints are Laplace-type
constraints on the Fourier packet.  If they vanish, E74 has a genuine
divisibility handle.  If only point endpoints vanish, the route likely returns
to the already insufficient Loewner endpoint calculus.

## Result

```text
tested: endpoint values and basic Laplace/Fourier moments;
rejected: simple divisibility of B(y) from Q_weta=0 alone;
kept: Gamma-prime directional cancellation with arch/prime pieces coupled.
```
