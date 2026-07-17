# E73.033 results - DATA-HERM decomposition

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_033_data_herm_decomposition_probe.py
```

Summary:

```text
tested lam: 8,10,12,14,16,18,20
tested nK: 3,4,5,6
tested Hermite orders: m=1,2,3
```

Columns:

```text
maxData   = max_k |g_cancelled(k)|
l1Data    = sum_k |g_cancelled(k)|
outNorm   = ||sum_k h(k)g_cancelled(k)||_Herm
l1Ratio   = outNorm / sum_k ||h(k)||_Herm |g_cancelled(k)|
maxRatio  = outNorm / (maxData sum_k ||h(k)||_Herm)
```

Reading:

```text
l1Ratio is often close to 1.
```

This means the Hermite-projected output is usually controlled by the individual smallness of the
critical data, not by a strong universal cancellation among the Hermite weights.

There are isolated windows with real cancellation, for example:

```text
lam=12, nK=5, m=1: l1Ratio=2.00e-2
lam=16, nK=6, m=1: l1Ratio=2.22e-1
lam=20, nK=6, m=1: l1Ratio=1.78e-1
```

but this is not uniform enough to replace the theorem by a generic moment identity.

Conclusion:

```text
DATA-HERM must be proved as critical-data divisibility/smallness of g_cancelled,
not as a universal Hermite moment cancellation.
```
