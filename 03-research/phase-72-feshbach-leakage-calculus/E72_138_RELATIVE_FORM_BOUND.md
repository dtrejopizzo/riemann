# E72.138 -- Relative arithmetic form bound

**Date:** 2026-07-09.
**Role:** express `RCOER` as the exact arithmetic form inequality that must be proved.

## 0. Split

Write:

```text
C_actual = C_model + Delta_arith.
```

The desired relative coercivity is:

```text
C_actual >= theta_H C_model,        theta_H>0.                (RCOER)
```

This is equivalent to:

```text
<v,Delta_arith v> >= -(1-theta_H)<v,C_model v>
```

for all vectors `v` in the even Feshbach complement.

## 1. Relative form bound

Define the negative relative form constant:

```text
eta_H(x)
 := sup_{v!=0} (-<v,Delta_arith v>)_+ / <v,C_model v>.
```

Then:

```text
eta_H(x) <= eta_H < 1                                      (RFBD)
```

implies:

```text
C_actual >= (1-eta_H)C_model.
```

Thus `(RFBD)` is exactly `(RCOER)`.

### Proof

For every `v`,

```text
<v,Delta_arith v> >= -eta_H<v,C_model v>.
```

Therefore:

```text
<v,C_actual v>
 = <v,C_model v>+<v,Delta_arith v>
 >= (1-eta_H)<v,C_model v>.
```

`QED`

## 2. Why this is weaker than the failed Weyl bound

E72.133 tried to control:

```text
||Delta_arith||.
```

That sees positive and harmless high-energy directions.  `(RFBD)` only controls the negative part of
the arithmetic perturbation in the model energy norm, which is exactly what coercivity needs.

Numerically, E72.134 measures:

```text
theta_H(x)=lambda_min(C_model^(-1/2)C_actual C_model^(-1/2)),
```

so:

```text
eta_H(x)=1-theta_H(x).
```

The observed `theta_H(x)>=0.42` gives `eta_H(x)<=0.58` in the tested windows.

## 3. Updated finite route

Combining E72.137 and this note:

```text
GCOER + RFBD => COER.
```

Therefore:

```text
CGE-K + ROP + GCOER + RFBD + MSB
=> scalar WRL resonance annihilation.
```

## 4. Status

```text
proved: RFBD is equivalent to RCOER;
proved: CGE-K + ROP + GCOER + RFBD + MSB imply scalar WRL;
open:   prove RFBD as an arithmetic form bound relative to the model complement energy.
```
