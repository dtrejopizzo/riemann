# E72.191 -- Low-moment envelope search

**Date:** 2026-07-09.
**Role:** test whether D-ASRP can be reduced to low-degree moment inequalities.

## 0. Target

For:

```text
e_a(t)=t^2                  for t<0,
e_a(t)=(1-a)^2t^2           for t>=0,
```

search for scalar polynomial majorants on `[-1,1]`:

```text
P_j(u)>=e_{a_j}(u).
```

Then:

```text
M_j^2 Tr P_j(K_j/M_j)
```

majorizes the block sign energy.

## 1. Output

The companion script:

```text
E72_191_low_moment_envelope_probe.py
```

tests degrees `4,6,8`. The key result:

```text
-- degree=8
 lam  exactBSE  envSum  slack  pass09409
  12     0.898   0.937  0.039 YES
  16     0.794   0.816  0.022 YES
  20     0.735   0.753  0.018 YES
  24     0.740   0.762  0.022 YES
  28     0.636   0.661  0.026 YES
  32     0.492   0.525  0.033 YES
  36     0.648   0.682  0.034 YES
worst_env=0.937 at lambda=12
```

Degrees `4` and `6` fail at `lambda=12`; degree `8` succeeds.

## 2. Reading

D-ASRP-0.03 does not require the adaptive long polynomial for the diagonal energy. It can be replaced
by fixed low-moment envelopes of degree `8`.

The adaptive Chebyshev polynomial remains useful for removing sign projections conceptually, but the
diagonal energy itself admits a much shorter certificate:

```text
LM8-ASRP:
0.90^2 Tr P_0(K_0/0.90)+0.60^2 Tr P_1(K_1/0.60)<0.9409.
```

This is a fixed finite cycle inequality of length `8`, not `O(sqrt(d_x))`.
