# E73.035 results - cancelled factor split

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_035_cancelled_factor_split_probe.py
```

Identity tested:

```text
g_cancelled(i gamma)
= (1-exp(i gamma L)) C_raw(gamma),
```

where

```text
C_raw(gamma)=sum_n xi_n/(-gamma-d_n).
```

Reading:

The smallness of `g_cancelled` has two sources:

```text
1. C_raw(gamma) small, often because gamma is close to a finite Cauchy root;
2. |1-exp(i gamma L)| small, a mesh-resonance cancellation.
```

Examples of multiplier-driven smallness:

```text
lam=14, gamma_3:
|1-exp|=6.33e-2, |C_raw|=2.30e-8, |g|=1.45e-9

lam=18, gamma_4:
|1-exp|=5.08e-2, |C_raw|=1.19e-7, |g|=6.07e-9

lam=20, gamma_4:
|1-exp|=7.72e-2, |C_raw|=4.80e-8, |g|=3.70e-9
```

Examples of raw Cauchy/root-driven smallness:

```text
lam=24, gamma_2:
|1-exp|=1.48, |C_raw|=2.17e-18

lam=24, gamma_3:
|1-exp|=1.62, |C_raw|=1.44e-16
```

Conclusion:

```text
CRIT-DIV is a two-factor divisibility statement:
finite-root alignment of C_x plus mesh-resonance cancellation.
```
