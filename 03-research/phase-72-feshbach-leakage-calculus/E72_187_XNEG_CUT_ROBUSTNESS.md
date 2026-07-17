# E72.187 -- XNEG cut robustness

**Date:** 2026-07-09.
**Role:** test whether the mixed sign `Tr(G_0G_1)<=0` is specific to the cut `0.60L`.

## 0. Question

E72.186 suggests the decomposition:

```text
Tr(G^2)=Tr(G_0^2)+Tr(G_1^2)+2Tr(G_0G_1)
```

with:

```text
XNEG: Tr(G_0G_1)<=0.
```

If `XNEG` only holds for one tuned cut, it is probably a calibration artifact. If it persists across
nearby cuts, it is a better candidate for a structural block-ordering lemma.

## 1. Output

The companion script:

```text
E72_187_xneg_cut_robustness_probe.py
```

reports:

```text
E72.187 XNEG cut-robustness probe
reports cross=2Tr(G0G1); negative supports XNEG
cut  maxCross  worstFinal  per-window
prepared lambda=12
prepared lambda=16
prepared lambda=20
prepared lambda=24
prepared lambda=28
prepared lambda=32
0.55   -0.002      0.980 12:-0.026 16:-0.023 20:-0.017 24:-0.019 28:-0.070 32:-0.002
0.60   -0.007      0.970 12:-0.048 16:-0.047 20:-0.022 24:-0.024 28:-0.082 32:-0.007
0.65   -0.024      0.969 12:-0.065 16:-0.055 20:-0.043 24:-0.047 28:-0.099 32:-0.024
```

## 2. Reading

`XNEG` persists for cuts:

```text
0.55, 0.60, 0.65.
```

The mixed term is not just negative at the optimized cut; it remains negative in a neighborhood. This
supports treating it as a structural early/late block interaction.

The worst final certificate remains near the initial stable window:

```text
lambda=12.
```

## 3. Updated proof route

With the original `m_*=0.05` margin, the stable arithmetic theorem can be targeted as:

```text
NTC-8:
Tr((K_0/0.90)^16)<1,
Tr((K_1/0.60)^16)<1.

D-ASRP:
Tr(G_0^2)+Tr(G_1^2)<0.9025.

XNEG:
Tr(G_0G_1)<=0.
```

Then:

```text
NTC-8 + D-ASRP + XNEG => ASRP-0.05.
```

All three are finite cycle inequalities. `XNEG` is now isolated as a sign/ordering lemma for the
two prime-position blocks.

E72.188 recommends the same decomposition with `m_*=0.03`, replacing `0.9025` by `0.9409`.
