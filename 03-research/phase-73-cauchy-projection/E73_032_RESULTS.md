# E73.032 results - DATA-HERM probe

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_032_data_hermite_probe.py
```

Summary:

```text
tested lam: 8,10,12,14,16,18
tested sigma: 0.05,0.10,0.20
tested cluster heights: gamma_1, gamma_2
tested multiplicity m: 1,2,3
critical data: first six g_cancelled critical values
```

Observed weighted Hermite outputs:

```text
m=1: about 1e-9 to 1e-8
m=2: about 5e-8 to 2e-7
m=3: about 1.5e-7 to 1.5e-6
```

Observed cancellation gain against the absolute ceiling:

```text
gain = weighted / (geomAbs * max|g_cancelled|)
roughly 0.05 to 0.44
```

Reading:

```text
DATA-HERM shows real signed improvement, but not enough to be treated as solved.
```

The critical data are small in the tested finite CCM windows, and Hermite projection preserves that
smallness.  However the gain relative to the absolute ceiling is only a modest factor.  Therefore the
asymptotic theorem cannot be replaced by a generic Cauchy or Hermite estimate.

The remaining theorem is exactly:

```text
e^(alpha L)
||Pi_conf(A,K_L) g_cancelled(K_L)||_Herm <= L^B.
```

This is `NAT-PROJ` in its Hermite-normalized finite form.
