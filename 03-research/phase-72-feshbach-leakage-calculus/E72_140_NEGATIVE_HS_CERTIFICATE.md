# E72.140 -- Negative Hilbert-Schmidt certificate for RFBD

**Date:** 2026-07-09.
**Role:** replace the relative arithmetic form bound by one scalar finite spectral inequality.

## 0. Relative perturbation

As in E72.139, define:

```text
K_rel := C_model^(-1/2)(C_actual-C_model)C_model^(-1/2).
```

Let:

```text
K_rel^- := negative spectral part of K_rel.
```

## 1. Certificate

Assume:

```text
||K_rel^-||_HS <= eta_H < 1.                                (NHS)
```

Then `RFBD` holds with the same `eta_H`:

```text
(-<v,Delta_arith v>)_+ <= eta_H <v,C_model v>.
```

### Proof

Let:

```text
w=C_model^(1/2)v.
```

Then:

```text
<v,Delta_arith v> = <w,K_rel w>.
```

The negative part satisfies:

```text
-(<w,K_rel w>) <= <w,K_rel^- w>
                <= ||K_rel^-||_op ||w||^2
                <= ||K_rel^-||_HS ||w||^2.
```

By `(NHS)`:

```text
-(<v,Delta_arith v>) <= eta_H <v,C_model v>.
```

Thus `RFBD` holds. `QED`

## 2. Why this is a better finite gate

E72.139 shows the negative relative perturbation is not low rank.  However its total negative
Hilbert-Schmidt energy is small.  The new finite gate is therefore scalar:

```text
sum_{lambda_a(K_rel)<0} lambda_a(K_rel)^2 <= eta_H^2 < 1.
```

This controls all negative arithmetic modes at once and does not see harmless positive directions.

## 3. Consequence

Combining E72.137, E72.138, and this note:

```text
GCOER + NHS => COER.
```

Therefore the sharp route becomes:

```text
CGE-K + ROP + GCOER + NHS + MSB
=> scalar WRL resonance annihilation.
```

## 4. Diagnostic

The companion script:

```text
E72_140_negative_hs_certificate_probe.py
```

reports:

```text
etaOp=-lambda_min(K_rel),
negHS=||K_rel^-||_HS,
negHS2,
margin=1-negHS2,
thetaHS=1-negHS.
```

Representative output:

```text
E72.140 negative-HS certificate probe
 lam   L  dim  etaOp  negHS  negHS2  margin  thetaHS  negTrace
   6  3.58   18  0.425  0.764   0.584   0.416    0.236 2.305e+00
   8  4.16   24  0.489  0.800   0.641   0.359    0.200 2.712e+00
  10  4.61   28  0.377  0.692   0.478   0.522    0.308 2.613e+00
  12  4.97   32  0.574  0.782   0.612   0.388    0.218 2.756e+00
  14  5.28   36  0.565  0.747   0.559   0.441    0.253 2.699e+00
  16  5.55   40  0.542  0.724   0.525   0.475    0.276 2.808e+00
  18  5.78   44  0.554  0.728   0.530   0.470    0.272 2.940e+00
```

## 5. Status

```text
proved: NHS implies RFBD;
proved: CGE-K + ROP + GCOER + NHS + MSB imply scalar WRL;
observed: NHS holds with `negHS^2<0.65` in the tested windows;
open:   prove NHS uniformly as a finite relative arithmetic energy inequality.
```
