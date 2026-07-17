# E72.164 -- Cut-weight audit for F2B-PSD

**Date:** 2026-07-09.
**Role:** test whether the two-block cut `L/2` is optimal for fixed weights.

## 0. Question

E72.163 uses the blocks:

```text
[0,L/2], (L/2,L].
```

with fixed weights:

```text
a=0.70, b=0.60.
```

The smallest margin occurs in the smallest window.  A different cut:

```text
[0,cL], (cL,L]
```

might give a more robust fixed certificate.

## 1. Diagnostic

The companion script:

```text
E72_164_cut_weight_probe.py
```

tests:

```text
c in [0.35,0.65]
```

with fixed weights `a=0.70,b=0.60`.

Representative output:

```text
E72.164 cut-weight probe fixed a=0.70, b=0.60
 cut   maxDist  margin  per-window
0.35    1.006  -0.011 6:0.990 8:1.006 10:0.904 12:0.945 14:0.902
0.45    1.001  -0.003 6:0.996 8:1.001 10:0.910 12:0.946 14:0.907
0.50    0.996   0.008 6:0.996 8:0.986 10:0.908 12:0.937 14:0.902
0.55    0.980   0.039 6:0.955 8:0.980 10:0.899 12:0.931 14:0.898
0.60    0.967   0.065 6:0.962 8:0.967 10:0.889 12:0.920 14:0.885
0.65    0.969   0.061 6:0.969 8:0.942 10:0.879 12:0.918 14:0.881
best_cut=0.60 maxDist=0.967 margin=0.065
```

The cut `c=0.60` improves the fixed-weight margin substantially.

## 2. Status

```text
observed: cut `0.60L` with fixed weights `(0.70,0.60)` gives a stronger certificate;
next:     update the fixed two-block certificate to use the improved cut.
```
