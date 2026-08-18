# E78.46 - The subunit denominator gap is an exact modulus-plus-angle defect

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.45 isolated the genuinely new denominator scalar

```text
1 - Re(q_N),                                              (DSP-1)
```

with

```text
q_N := (1-theta_N+2)/(1-theta_N).                         (DSP-2)
```

This note shows that the subunit gap itself splits exactly into a modulus loss
plus an angular penalty.

## 2. Exact polar decomposition

Write

```text
q_N = |q_N| exp(i phi_N).                                 (DSP-3)
```

Then

```text
Re(q_N) = |q_N| cos(phi_N),                               (DSP-4)
```

so

```text
1 - Re(q_N)
 = 1 - |q_N| cos(phi_N)
 = (1-|q_N|) + |q_N| (1-cos(phi_N)).                     (DSP-5)
```

This is exact.

So the subunit barrier from E78.45 factors canonically into

```text
modulus gap      := 1 - |q_N|,
angular penalty  := |q_N|(1-cos(phi_N)).                 (DSP-6)
```

Equivalently,

```text
SUBUNIT-GAP
<=>
MODULUS-SUBUNIT + ANGULAR-PENALTY.                        (DSP-7)
```

## 3. Relation to the previous denominator chain

By E78.38, the same phase `phi_N = arg(q_N)` controls the denominator-direction
defect. So `(DSP-5)` shows:

```text
the new denominator scalar is not independent of the old phase front;
it is the sum of
  a genuinely new modulus-loss term 1-|q_N|,
  plus the old phase penalty, weighted by |q_N|.          (DSP-8)
```

This is the candid content of the reduction after E78.45.

## 4. Probe audit

Companion:

```text
E78_46_den_subunit_polar_probe.py
E78_46_den_subunit_polar_results.json
```

The probe reconstructs `(DSP-5)` directly from the certified denominator
quotient rows.

### Exactness

For both builds:

```text
max reconstruction error < 1e-16.                         (DSP-9)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  1-Re(q_N)   = 0.5057771152
  1-|q_N|     = 0.5057761553
  angular     = 9.5985e-07

sigma=3.0, N=12->14:
  1-Re(q_N)   = 0.3819257889
  1-|q_N|     = 0.3819086585
  angular     = 1.7130e-05.                              (DSP-10)
```

Across the audited zeta ladder:

```text
median modulus gap term   = 0.30723431628410924
median angular gap term   = 1.755794094499617e-06
max angular gap share     = 4.484098407624691e-05.       (DSP-11)
```

So on the audited zeta ladder the subunit gap is almost entirely a modulus-loss
effect; the angular penalty is tiny.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  1-Re(q_N)   = -6.4534770235
  1-|q_N|     = -6.7999254111
  angular     = 0.3464483876

sigma=3.0, N=12->14:
  1-Re(q_N)   = 0.4812804491
  1-|q_N|     = 0.4195966651
  angular     = 0.0616837840.                            (DSP-12)
```

Across the audited planted ladder:

```text
median modulus gap term   = 0.18909891122635974
median angular gap term   = 9.213684712089927e-05
max angular gap share     = 0.12815840767009428.         (DSP-13)
```

The plant can fail already because the modulus term itself becomes negative
(`|q_N|>1`), and where it does remain subunit its angular penalty is much less
benign than on zeta.

## 5. Consequence

This yields a sharper denominator endpoint:

```text
DEN-SUBUNIT-POLAR:
  prove that |q_N| stays below 1 by a cofinal margin,
  and that the phase penalty |q_N|(1-cos(arg q_N)) stays negligible. (DSP-14)
```

Then `(DSP-5)` gives the subunit gap from E78.45, which in turn gives
directional control.

This is a genuine reduction because the new proof burden splits cleanly into a
modulus-side clause and an already-recognized angular clause.

## 6. Candid reading

This note does not prove the cofinal modulus-subunit law. What it does prove is
that the post-E78.45 burden is mostly on the modulus side:

```text
for zeta on the audited ladder,
1-Re(q_N) is explained almost completely by 1-|q_N|.      (DSP-15)
```

So if the denominator front is to close, the likely next real target is a
theorem-grade `|q_N|<1` mechanism, not another phase renormalization.

## 7. Status

```text
proved:
  1-Re(q_N) = (1-|q_N|) + |q_N|(1-cos(arg q_N)) exactly;

proved:
  the subunit denominator gap splits into a modulus-loss term plus an angular
  penalty;

observed:
  on the audited zeta ladder the angular penalty is negligible compared to the
  modulus gap term;

observed:
  the planted build can fail already through |q_N|>1, before any subtle phase
  argument is needed;

reduced:
  DEN-SUBUNIT-HORIZONTALITY to DEN-SUBUNIT-POLAR;

next:
  isolate a finite shell law for the modulus-subunit term 1-|q_N|, or autopsy
  that modulus deficit into an even smaller exact update scalar.
```
