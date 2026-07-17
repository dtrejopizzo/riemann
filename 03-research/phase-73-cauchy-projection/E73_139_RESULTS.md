# E73.139 Results - Prime-Orbit Cancellation Probe

Date: 2026-07-12.

Script:

```text
E73_139_prime_orbit_cancellation_probe.py
```

Purpose:

Inspect the dominant critical-cell cancellation from E73.137:

```text
<e,W02 xi> ~= <e,Prime xi>.
```

The prime term is expanded by prime-power orbits

```text
y = k log p,
weight = (log p) p^{-k/2}.
```

The script tracks the residual

```text
<e,W02 xi> - partial_sum_{k log p <= y} <e,Prime_{p^k} xi>.
```

Output:

```text
E73.139 prime-orbit cancellation probe
Tracks residual <e,W02 xi> - partial_sum <e,Prime_orbit xi>.
 lam     L gamma  targetB totalPrimeB  bestResB best_u  finalResB
  20   5.991   14.13   -1.549      -1.584    -3.814  0.809    -3.108
  20   5.991   21.02   -2.777      -2.795    -4.710  0.988    -4.710
  24   6.356   14.13   -2.242      -2.293    -8.747  0.816    -3.551
  24   6.356   21.02   -2.502      -2.555    -3.785  0.999    -3.785
```

Sparse traces:

```text
lambda=20, gamma=14.13:
u=0.663 residualB=-0.669
u=0.835 residualB=-1.576
u=0.930 residualB=-2.902
u=0.999 residualB=-3.108

lambda=24, gamma=14.13:
u=0.687 residualB=-2.423
u=0.854 residualB=-1.559
u=0.934 residualB=-1.934
u=0.999 residualB=-3.551
```

## Reading

The cancellation is not a simple monotone local-in-length cancellation.
Some partial sums come very close to the W02 target, especially near

```text
u = y/L ~= 0.8,
```

but the final residual after all prime powers is on the `WR` scale:

```text
finalResB ~= WRB.
```

This is consistent with the exact cell equation:

```text
W02 - Prime = WR + mu*eval.
```

The prime orbit sum first approaches or overshoots the W02 channel and the
full Euler-truncated sum lands at the archimedean correction `WR`.

## Consequence

The next theorem should not attempt to prove binwise positivity or local
length cancellation.  The correct identity is global over the finite
Euler-truncated orbit sum:

```text
sum_{p^k <= lambda^2}
(log p) p^{-k/2} <e,Q_{k log p} xi>

=
<e,W02 xi> - <e,WR xi> + O(L^{-17-p_gamma}).
```

This is a finite explicit formula.  It is the concrete version of Critical
Cell Cancellation.

