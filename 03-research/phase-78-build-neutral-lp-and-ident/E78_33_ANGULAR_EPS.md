# E78.33 - The angular correction is exactly an `eps_N` drift

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.32 split the raw safe-u increment into

```text
Delta safe_u_N
 = modulus_term_N + angular_term_N.                      (AE-1)
```

The angular piece was still written in terms of the normalized imaginary share

```text
s_N := Im(u_N)/|u_N|.                                    (AE-2)
```

This note rewrites it in the cleanest possible real form.

## 2. Exact epsilon-drift identity

Define the vertical defect

```text
eps_N := 1 - Im(u_N)/|u_N| = 1 - s_N.                    (AE-3)
```

Then the angular correction from E78.32,

```text
angular_term_N = 2 |u_N| (s_N+2 - s_N),                  (AE-4)
```

becomes exactly

```text
ANGULAR-EPS:
angular_term_N = 2 |u_N| (eps_N - eps_N+2).              (AE-5)
```

So the angular part of `Delta safe_u` is nothing but the drift of the single
real sequence `eps_N`, weighted by `2|u_N|`.

Combining E78.32 and `(AE-5)` gives the exact update law

```text
Delta safe_u_N
 = 2 (|u_N+2| - |u_N|) s_N+2
   + 2 |u_N| (eps_N - eps_N+2).                          (AE-6)
```

This is the cleanest current form of the sign-side shell update.

## 3. Probe audit

Companion:

```text
E78_33_angular_eps_probe.py
E78_33_angular_eps_results.json
```

The probe reconstructs `(AE-5)` from the certified E78.32 shell rows.

### Exactness

For both builds, the reconstruction is exact to roundoff:

```text
max angular-eps reconstruction error < 1e-18.            (AE-7)
```

So the angular term has now been reduced to a one-dimensional real drift with
no residual geometric ambiguity.

### Zeta

Representative rows:

```text
sigma=1.0:
  N= 8  eps_drift=-9.73e-04  angular=-2.34e-05
  N=14  eps_drift= 1.87e-02  angular= 1.24e-04
  N=20  eps_drift= 2.03e-01  angular= 7.28e-04

sigma=3.0:
  N= 8  eps_drift=-1.17e-04  angular=-7.96e-06
  N=14  eps_drift= 2.34e-03  angular= 4.38e-05
  N=20  eps_drift= 3.36e-02  angular= 2.86e-04.          (AE-8)
```

Compared against the modulus term from E78.32:

```text
max |angular_term|/|modulus_term| = 0.17364139886984334. (AE-9)
```

So on the audited zeta ladder, the `eps_N` drift remains a secondary
correction to the modulus gain.

### Planted build

The planted build fails at exactly this point: the `eps_N` drift is often of
the same size as, or much larger than, the modulus term.

Representative rows:

```text
sigma=1.0:
  N= 8  eps_drift= 1.03962   angular/modulus = 17.94
  N=10  eps_drift= 0.45279   angular/modulus =  6.51

sigma=3.0:
  N=10  eps_drift= 0.366998  angular/modulus = 17.23
  N=20  eps_drift=-0.033136  angular/modulus =  2.90.    (AE-10)
```

So the plant does not merely have a bad angle in some vague sense: its vertical
defect sequence `eps_N` fluctuates strongly enough to overpower the modulus
mechanism.

## 4. Consequence

This yields a sharper reduced target than E78.32:

```text
ANGULAR-DRIFT-SMALLNESS
can be pursued as a theorem-grade control of

  eps_N - eps_N+2,                                       (AE-11)
```

where

```text
eps_N = 1 - Im(u_N)/|u_N|.                               (AE-12)
```

So the sign-side branch now splits as

```text
MODULUS-GAIN-DOMINANCE
+ EPS-DRIFT-SMALLNESS
=> DELTA-SAFEU-GEOMETRIC-ENVELOPE
=> SAFE-U-GEOMETRIC-ENVELOPE
=> SAFE-U-GEOMETRIC-TAIL.                                (AE-13)
```

This is a real reduction: `eps_N` is simpler than either the raw angle or the
original `Q_theta`.

## 5. Honest reading

This note does not yet prove `EPS-DRIFT-SMALLNESS`. What it proves is that the
open angular mechanism has been localized exactly to the drift of a single real
sequence.

That is precisely the kind of reduced object the ledger wants.

## 6. Status

```text
proved:
  the angular correction in Delta safe_u is exactly
  2|u_N|(eps_N-eps_N+2) with eps_N = 1-Im(u_N)/|u_N|;

proved:
  the reconstruction is exact to roundoff for both builds;

observed:
  on the audited zeta ladder the angular piece stays below about 17.4% of the
  modulus term;

observed:
  on the planted ladder the eps-drift often dominates the modulus term by large
  factors;

reduced:
  ANGULAR-DRIFT-SMALLNESS to EPS-DRIFT-SMALLNESS;

next:
  seek a finite theorem-grade control on the shell drift of eps_N from the
  exact theta-logderivative / denominator update formulas.
```
