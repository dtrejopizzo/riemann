# E78.30 - `SAFE-U-CONTRACTION` reduces to a raw delta ratio

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.27-E78.28 reduced the sign-side target to the geometric envelope for

```text
A_N := N Delta safe_u_N.                                   (DR-1)
```

This note isolates the only nontrivial part of the contraction ratio.

## 2. Exact factorization

By definition,

```text
rho_N := A_{N+2}/A_N
      = ((N+2) Delta safe_u_{N+2}) / (N Delta safe_u_N).  (DR-2)
```

Therefore

```text
rho_N
 = ((N+2)/N) * (Delta safe_u_{N+2} / Delta safe_u_N).     (DR-3)
```

This is exact.

So the arithmetic content of `SAFE-U-CONTRACTION` is not the prefactor
`(N+2)/N`; that part is explicit and harmless. The live content is the raw
ratio

```text
RAW-DELTA-RATIO_N
 := Delta safe_u_{N+2} / Delta safe_u_N.                  (DR-4)
```

Indeed,

```text
rho_N < 1
<=> RAW-DELTA-RATIO_N < N/(N+2).                          (DR-5)
```

And the stronger geometric envelope from E78.28 becomes

```text
0 < RAW-DELTA-RATIO_N <= rho_* N/(N+2).                   (DR-6)
```

## 3. Consequence

The current sign-side target reduces one more step to

```text
DELTA-SAFEU-RATIO-CONTROL:
  prove a cofinal bound on the raw ratio

    0 < Delta safe_u_{N+2} / Delta safe_u_N <= c_N

  with c_N <= rho_* N/(N+2) < 1.                          (DR-7)
```

This is the cleanest one-step form available so far.

## 4. Probe audit

Companion:

```text
E78_30_delta_safeu_ratio_probe.py
E78_30_delta_safeu_ratio_results.json
```

### Zeta

At `sigma=1.0`, the raw ratios are

```text
0.64719, 0.68161, 0.73543, 0.74234, 0.78295.              (DR-8)
```

At `sigma=3.0`,

```text
0.65612, 0.68665, 0.73899, 0.74457, 0.78470.              (DR-9)
```

These are all positive and comfortably below `1`, and after multiplication by
the weight factor `(N+2)/N` they reproduce the contraction ratios from E78.27.

### Planted build

The planted raw ratios are unstable:

```text
sigma=1.0:  0.31561, 0.03598, -0.58779, 0.45706, -0.40695
sigma=3.0:  0.72576, 0.21511, -0.11996, 0.53670, -3.25725. (DR-10)
```

So the plant fails already at the raw delta-ratio level: positivity is lost
before the benign weight factor enters.

## 5. Candid reading

This is a real reduction, not just notation.

It says the live sign-side question is now:

```text
why do consecutive safe_u updates contract by a positive raw ratio?
```

That is more primitive than the weighted ratio `rho_N`, and therefore a better
candidate for a theorem-grade shell-update argument.

## 6. Status

```text
proved:
  SAFE-U-CONTRACTION factors exactly into the trivial weight (N+2)/N times the
  raw ratio Delta safe_u_{N+2}/Delta safe_u_N;

observed:
  zeta raw ratios are positive and stable on the audited ladder;

observed:
  the planted build fails already at the raw-ratio level via sign changes and
  large negative excursions;

reduced:
  the sign-side target from SAFE-U-CONTRACTION to
  DELTA-SAFEU-RATIO-CONTROL;

next:
  derive the raw delta-ratio control from the exact u-sector and shell-update
  formulas, which now carry the entire nontrivial burden.
```
