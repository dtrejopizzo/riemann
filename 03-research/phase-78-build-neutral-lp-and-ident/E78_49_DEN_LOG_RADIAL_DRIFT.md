# E78.49 - The radial contraction law is equivalently a logarithmic drift

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

After E78.47-E78.48, the modulus front is already one-dimensional:

```text
|d_N+2| / |d_N| < 1,                                      (DLR-1)
```

with

```text
d_N := 1-theta_N.                                         (DLR-2)
```

Because this is a multiplicative contraction, the natural alternative language
is logarithmic drift. This note records that equivalence and audits whether it
creates a genuinely smaller target.

## 2. Exact logarithmic identity

From E78.47,

```text
|q_N| = |d_N+2| / |d_N|.                                  (DLR-3)
```

Taking negative logarithms gives

```text
LOG-RADIAL-DRIFT_N
 := -log(|d_N+2| / |d_N|)
  = -log|q_N|.                                            (DLR-4)
```

Since the radial deficit is

```text
delta_N := 1 - |q_N|,                                     (DLR-5)
```

we also have the exact scalar identity

```text
LOG-RADIAL-DRIFT_N = -log(1-delta_N).                     (DLR-6)
```

Therefore

```text
DEN-RADIAL-CONTRACTION
<=> LOG-RADIAL-DRIFT_N > 0.                               (DLR-7)
```

## 3. What this does and does not buy

The logarithmic form is useful because it turns multiplicative contraction into
an additive shell drift:

```text
log|d_N| - log|d_N+2| = LOG-RADIAL-DRIFT_N.               (DLR-8)
```

But it does **not** create a smaller theorem-grade target. Positivity of the
log drift is exactly the same burden as positivity of the radial deficit, since
`-log(x)` is strictly decreasing on `(0,+infinity)`.

So this note is primarily an algebraic re-expression, not a further reduction.

## 4. Probe audit

Companion:

```text
E78_49_DEN_LOG_RADIAL_DRIFT_probe.py
E78_49_den_log_radial_drift_results.json
```

The probe imports the certified E78.47 rows and reconstructs `(DLR-6)` exactly.

### Exactness

For both builds:

```text
max reconstruction error < 1e-15.                         (DLR-9)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  |d_N+2|/|d_N|      = 0.4942238447
  log drift          = 0.7047667376
  radial deficit     = 0.5057761553

sigma=3.0, N=12->14:
  ratio              = 0.6180913415
  log drift          = 0.4811190306
  radial deficit     = 0.3819086585.                     (DLR-10)
```

So the audited zeta branch has a clean positive additive drift in `log|1-theta|`.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  ratio              = 7.7999254111
  log drift          = -2.0541141710

sigma=3.0, N=12->14:
  ratio              = 0.5804033349
  log drift          = 0.5440320122.                     (DLR-11)
```

So the plant shows the exact same success/failure pattern as the radial ratio:
early expansion gives negative log drift.

## 5. Candid reading

This note is another theorem-plus-autopsy step.

Theorem:
the denominator modulus law can be written as an additive drift for `log|1-theta|`.

Autopsy:
this additive drift is equivalent to the same contraction target from E78.47,
not a stricter endpoint.

That said, the log form may still be the right language for a future shell
recurrence or telescoping argument, so it is worth keeping in the ledger.

## 6. Status

```text
proved:
  -log(|1-theta_N+2|/|1-theta_N|) = -log|q_N| exactly;

proved:
  positivity of the log drift is equivalent to DEN-RADIAL-CONTRACTION;

observed:
  the audited zeta ladder has robust positive log drift, while the planted
  build fails exactly where the radial ratio exceeds 1;

autopsied:
  the logarithmic rewrite does not produce a smaller theorem-grade target;

next:
  search for a genuine recurrence, drift inequality, or telescoping law for
  log|1-theta_N| itself, rather than further equivalent rewritings.
```
