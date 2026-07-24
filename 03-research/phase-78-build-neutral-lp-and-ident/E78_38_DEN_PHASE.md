# E78.38 - `DIRDEF_b,N` is exactly a denominator phase defect

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.37 reduced the denominator correction to

```text
DIRDEF_b,N := (1/2) ||b_hat_N+2 - b_hat_N||^2,           (DPH-1)
```

where

```text
b_hat_N := (1-theta_N)/|1-theta_N|.                       (DPH-2)
```

This note shows that `DIRDEF_b,N` is exactly a one-dimensional phase defect.

## 2. Exact phase identity

Because `b_hat_N` lies on the unit circle, the step ratio

```text
rho_b,N := b_hat_N+2 / b_hat_N                            (DPH-3)
```

has modulus `1`.  Write

```text
rho_b,N = exp(i Delta phi_b,N),                           (DPH-4)
```

with `Delta phi_b,N := arg(rho_b,N)`.

Then

```text
<b_hat_N+2, b_hat_N> = cos(Delta phi_b,N),               (DPH-5)
```

so

```text
DEN-PHASE:
DIRDEF_b,N
 = 1 - cos(Delta phi_b,N)
 = 2 sin^2(Delta phi_b,N / 2).                            (DPH-6)
```

Thus the denominator-direction correction from E78.37 is controlled exactly by
the phase increment of the normalized denominator direction.

## 3. Probe audit

Companion:

```text
E78_38_den_phase_probe.py
E78_38_den_phase_results.json
```

The probe reconstructs `(DPH-6)` directly from the certified `E77.5ac` points.

### Exactness

For both builds:

```text
max reconstruction error < 1e-15.                         (DPH-7)
```

So the phase formula is exact to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0:
  N=10->12  |Delta phi_b| = 0.00197085894960783
  N=12->14  |Delta phi_b| = 0.0024900808541071374

sigma=3.0:
  N=10->12  |Delta phi_b| = 0.005924045792726611
  N=12->14  |Delta phi_b| = 0.007445162316356419.        (DPH-8)
```

So the audited zeta denominator direction moves by tiny angular increments.

### Planted build

The planted build fails exactly by large early phase steps:

```text
sigma=1.0:
  N=10->12  |Delta phi_b| = 0.2991643218040757
  N=12->14  |Delta phi_b| = 0.3757554599459294

sigma=3.0:
  N=10->12  |Delta phi_b| = 0.30536133033987906
  N=12->14  |Delta phi_b| = 0.46522075079285974.         (DPH-9)
```

That is the direct phase version of the large `DIRDEF_b,N` seen in E78.37.

## 4. Consequence

This gives the cleanest denominator reduced target so far:

```text
DEN-PHASE-RIGIDITY:
prove that |Delta phi_b,N| stays small cofinally on zeta. (DPH-10)
```

Indeed, by `(DPH-6)`,

```text
small phase step
=> tiny DIRDEF_b,N
=> small DENDIR_N.                                        (DPH-11)
```

So the denominator front becomes

```text
DEN-PHASE-RIGIDITY
=> DIRDEF-B-SMALLNESS
=> denominator-direction control.                         (DPH-12)
```

This is a genuine reduction: the live denominator object is now a single phase
increment on the unit circle.

## 5. Honest reading

This note does not yet prove phase rigidity cofinally. What it does prove is
that the denominator-direction scalar from E78.37 is exactly equivalent to a
one-dimensional phase-step target.

That is the smallest honest denominator object named so far.

## 6. Status

```text
proved:
  DIRDEF_b,N is exactly 1-cos(Delta phi_b,N), equivalently
  2 sin^2(Delta phi_b,N/2);

proved:
  the reconstruction holds to roundoff for both builds;

observed:
  zeta has tiny denominator phase steps on the audited ladder;

observed:
  the planted build has order-10^-1 early denominator phase steps and fails
  phase rigidity;

reduced:
  DIRDEF-B-SMALLNESS to DEN-PHASE-RIGIDITY;

next:
  express Delta phi_b,N directly from the shell update of 1-theta_N and test
  whether it inherits a simpler finite quotient law.
```
