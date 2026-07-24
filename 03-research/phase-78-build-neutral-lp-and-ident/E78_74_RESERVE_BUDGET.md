# E78.74 - The quadratic shell margin is exactly a basepoint reserve budget

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.72 split the radial part of the shell sign into a basepoint reserve minus a
tail loss, and E78.73 identified that reserve as an exact old-old contraction
law for `|1-theta_old|`.

This note combines those two reductions with the quadratic barrier of E78.70
into a single operational budget identity.

## 2. Exact reserve decomposition

Fix the left endpoint

```text
sigma_0 := 0.55.                                         (RBG-1)
```

E78.72 gives

```text
Re Delta ell_N(i sigma)
 = BASE_N(sigma_0) - TAIL_N(sigma_0,sigma),             (RBG-2)
```

where

```text
BASE_N(sigma_0) := Re Delta ell_N(i sigma_0),           (RBG-3)
TAIL_N(sigma_0,sigma)
 := -(1/2) ∫_{sigma_0}^{sigma} SAFEDELTA_N(t) dt.       (RBG-4)
```

E78.73 identifies the basepoint term exactly as

```text
BASE_N(sigma_0)
 = log( |1-theta_old(N;i sigma_0)|
      / |1-theta_old(N+2;i sigma_0)| ).                 (RBG-5)
```

Subtracting the quadratic phase penalty from both sides of `(RBG-2)` yields

```text
Re Delta ell_N(i sigma) - |wrap Im Delta ell_N(i sigma)|^2
 = BASE_N(sigma_0)
   - TAIL_N(sigma_0,sigma)
   - |wrap Im Delta ell_N(i sigma)|^2.                  (RBG-6)
```

So the quadratic shell barrier from E78.70 is equivalent to the explicit budget
inequality

```text
BASE_N(sigma_0)
>
TAIL_N(sigma_0,sigma) + |wrap Im Delta ell_N(i sigma)|^2. (RBG-7)
```

This is the exact finite content of the zeta shell margin.

## 3. Explicit implication

By E78.70,

```text
Re Delta ell_N(i sigma) > |wrap Im Delta ell_N(i sigma)|^2
=> LOGQ-QUADRATIC-BARRIER
=> LOGQ-BARRIER
=> LOGQ-GAIN-SIGN.                                       (RBG-8)
```

Combining `(RBG-6)` with `(RBG-8)` gives the proved reduction

```text
RESERVE-BUDGET:
  BASE_N(0.55)
  >
  TAIL_N(0.55,sigma) + |wrap Im Delta ell_N(i sigma)|^2

=> LOGQ-QUADRATIC-BARRIER
=> LOGQ-GAIN-SIGN.                                       (RBG-9)
```

Hence the live shell target sharpens again:

```text
LOGQ-QUADRATIC-BARRIER
<=
RESERVE-BUDGET
<=
OLD-OLD-RADIAL-STEP + signed tail control + phase-square control. (RBG-10)
```

## 4. Probe audit

Companion:

```text
E78_74_reserve_budget_probe.py
E78_74_reserve_budget_results.json
```

The probe reconstructs `(RBG-6)` directly from the certified `E77.5g` rows.

```text
zeta:   max reconstruction error = 0,
plant:  max reconstruction error = 0.                   (RBG-11)
```

So the reserve identity is exact to roundoff in both builds.

### Zeta

Across the full audited ladder

```text
N = 8,10,12,14,16,18,20
sigma in {0.55,0.6,0.75,1,1.5,2,3},                     (RBG-12)
```

the reserve margin stays strictly positive:

```text
margin = BASE - TAIL - phase^2
      = Re Delta ell_N - |wrap Im Delta ell_N|^2

min    = 4.845e-2,
median = 1.116e-1,
max    = 2.220e-1.                                      (RBG-13)
```

Moreover the phase-square term is negligible relative to the reserve:

```text
max phase^2 <= 2.883e-5,                                (RBG-14)
```

while the tail loss from `sigma_0=0.55` to `sigma=3` remains well below the
basepoint reserve on every audited zeta step; in fact

```text
max tail/base <= 9.62e-2,
max phase^2/base <= 5.95e-4.                            (RBG-14a)
```

### Planted build

The plant does not preserve that budget regime:

```text
margin min    = -1.017,
margin median = -3.137e-1,
margin max    =  1.247.                                 (RBG-15)
```

So the falsifier already loses the exact reserve budget on the audited ladder.

## 5. Consequence

This note turns the shell-sign burden into a single concrete inequality with
three named pieces:

```text
prove:
  (i) old-old radial contraction at sigma_0=0.55,
  (ii) signed tail loss control from SAFEDELTA,
  (iii) wrapped-phase square below the remaining reserve. (RBG-16)
```

Nothing hidden remains in the radial factor. Every part is now an explicit
finite object already present in the certified front.

## 6. Honest reading

This note does not prove the reserve budget cofinally. It proves that the
quadratic shell barrier is exactly this budget, no more and no less.

That matters because it removes the last unnamed scalar from the reduction: the
live target is now a three-term inequality involving only old-old contraction,
safe-derivative tail loss, and wrapped phase.

## 7. Status

```text
proved:
  the quadratic shell margin equals BASE - TAIL - phase^2 exactly;

proved:
  therefore RESERVE-BUDGET implies LOGQ-QUADRATIC-BARRIER and hence
  LOGQ-GAIN-SIGN;

observed:
  on the audited zeta ladder the reserve budget margin is uniformly positive,
  while the planted build does not preserve that regime;

reduced:
  LOGQ-QUADRATIC-BARRIER to the explicit three-piece inequality
  RESERVE-BUDGET.
```
