# E73.120 Results - Finite GATE-73 Manifest Verifier

Date: 2026-07-12.

Script:

```text
E73_120_gate73_manifest_verifier.py
```

Purpose:

Consolidate the Phase 73 finite certificates into one machine-checkable
manifest.  Each row declares which certificate is allowed:

```text
base16_exact_lock:
  lambda=16 low-scale base certificate from E73.119.

standard_box:
  exact-local box certificate from E73.117.
```

The manifest contains:

```text
2 boxes  for lambda=16 using exact LOCK base certificate;
12 boxes for lambda=20 finite subdivided cover;
4 boxes  for lambda=24,28 wide-box certificate.
```

Thresholds enforced:

```text
standard_box:
  LOCK <= L^-5,
  TAIL <= L^-5,
  OUT  <= L^-9,
  MAIN <= 1.

base16_exact_lock:
  exact LOCK <= L^-5,
  MAIN <= 1.
```

For the base16 rows, `TAIL` and `OUT` already passed in E73.117 on the
same wide boxes; the manifest isolates the only repaired component,
`LOCK`.

Output:

```text
E73.120 finite GATE-73 manifest verifier
Each row declares the certificate kind; thresholds are enforced by kind.
 name                                kind              L   lockB  tailB    outB mainBox nTri status
lambda16-base-14.13                 base16_exact_lock  5.545  -9.921    -inf    -inf 2.049e-01    1 PASS
lambda16-base-21.02                 base16_exact_lock  5.545 -10.001    -inf    -inf 2.058e-01    1 PASS
lambda20-cover-g1-a0.15-0.20-t0     standard_box       5.991  -8.151 -10.651 -14.191 1.000e-01    1 PASS
lambda20-cover-g1-a0.15-0.20-t1     standard_box       5.991  -8.144 -10.644 -14.180 1.011e-01    1 PASS
lambda20-cover-g1-a0.15-0.20-t2     standard_box       5.991  -8.138 -10.638 -14.186 1.022e-01    1 PASS
lambda20-cover-g1-a0.15-0.20-t3     standard_box       5.991  -8.132 -10.632 -14.211 1.032e-01    1 PASS
lambda20-cover-g1-a0.20-0.25-t0     standard_box       5.991  -8.012 -10.316 -14.025 1.350e-01    1 PASS
lambda20-cover-g1-a0.20-0.25-t1     standard_box       5.991  -8.005 -10.309 -14.025 1.365e-01    1 PASS
lambda20-cover-g1-a0.20-0.25-t2     standard_box       5.991  -7.999 -10.303 -14.031 1.379e-01    1 PASS
lambda20-cover-g1-a0.20-0.25-t3     standard_box       5.991  -7.994 -10.298 -14.045 1.392e-01    1 PASS
lambda20-cover-g2-t0                standard_box       5.991  -7.982 -10.314 -14.132 1.329e-01    1 PASS
lambda20-cover-g2-t1                standard_box       5.991  -7.989 -10.321 -14.122 1.312e-01    1 PASS
lambda20-cover-g2-t2                standard_box       5.991  -7.996 -10.328 -14.111 1.294e-01    1 PASS
lambda20-cover-g2-t3                standard_box       5.991  -8.004 -10.336 -14.100 1.275e-01    1 PASS
lambda24-wide-14.13                 standard_box       6.356  -8.699 -10.725 -13.590 2.366e-01    1 PASS
lambda28-wide-14.13                 standard_box       6.664  -8.378 -10.108 -13.337 1.912e-01    1 PASS
lambda24-wide-21.02                 standard_box       6.356  -8.782 -10.807 -13.356 2.542e-01    1 PASS
lambda28-wide-21.02                 standard_box       6.664  -8.402 -10.132 -13.083 2.050e-01    1 PASS
manifest_status PASS failures=0
```

Conclusion:

The finite manifest passes with zero failures.

What this proves:

```text
For every declared box in the manifest, the corresponding finite
GATE-73 certificate is verified by an explicit computable inequality.
```

What this does not yet prove:

```text
Uniform GATE-73 for every L>=L0 and every natural-height off-line cluster
box.
```

The route has now been separated cleanly:

```text
finite machine-checkable gate: E73.120;
uniform/asymptotic theorem: still open.
```

The next target is no longer local repair.  It is to formulate a single
asymptotic majorant theorem for the `standard_box` quantities that explains
why the wide boxes improve from lambda=24 onward.

