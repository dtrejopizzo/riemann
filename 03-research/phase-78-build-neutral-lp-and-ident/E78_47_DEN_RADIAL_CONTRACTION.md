# E78.47 - The denominator modulus deficit is exactly a radial contraction law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.46 reduced the denominator front to the modulus-side target

```text
1 - |q_N|,                                                (DRC-1)
```

where

```text
q_N := (1-theta_N+2)/(1-theta_N).                         (DRC-2)
```

This note removes the remaining quotient opacity from the modulus side.

## 2. Exact radial identity

Set

```text
d_N := 1-theta_N.                                         (DRC-3)
```

Then

```text
q_N = d_N+2 / d_N,                                        (DRC-4)
```

so taking moduli gives the exact identity

```text
|q_N|
 = |d_N+2| / |d_N|
 = |1-theta_N+2| / |1-theta_N|.                           (DRC-5)
```

Therefore

```text
1 - |q_N|
 = 1 - |1-theta_N+2| / |1-theta_N|.                       (DRC-6)
```

So the modulus deficit from E78.46 is not a free complex-modulus condition at
all: it is exactly a radial shell-contraction law for the denominator norm.

## 3. Consequence

The post-E78.46 denominator burden reduces to

```text
DEN-RADIAL-CONTRACTION:
  prove cofinally that
  |1-theta_N+2| <= (1-c_*) |1-theta_N|                    (DRC-7)
```

for some safe-ladder margin `c_*>0`.

Together with the already isolated small angular penalty from E78.46, this gives

```text
radial contraction of |1-theta_N|
+ negligible phase penalty
=> subunit gap 1-Re(q_N)
=> denominator direction control.                         (DRC-8)
```

This is a genuine reduction: the modulus side is now a one-dimensional shell
law on the denominator radius.

## 4. Probe audit

Companion:

```text
E78_47_den_radial_contraction_probe.py
E78_47_den_radial_contraction_results.json
```

The probe reconstructs `(DRC-5)` directly from the certified Phase-77
`one_minus_theta` rows.

### Exactness

For both builds:

```text
max ||q_N| - |d_N+2|/|d_N|| < 1e-15.                      (DRC-9)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  |q_N| = 0.4942238447
  |d_N+2|/|d_N| = 0.4942238447
  1-|q_N| = 0.5057761553

sigma=3.0, N=12->14:
  |q_N| = 0.6180913415
  |d_N+2|/|d_N| = 0.6180913415
  1-|q_N| = 0.3819086585.                               (DRC-10)
```

Across the audited zeta ladder:

```text
median radial deficit = 0.30723431628410935
min    radial deficit = 0.2617331140726784
max    radial deficit = 0.505776155332037.               (DRC-11)
```

So the audited zeta denominator norm contracts strongly from one shell step to
the next.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  |q_N| = 7.7999254111
  |d_N+2|/|d_N| = 7.7999254111
  1-|q_N| = -6.7999254111

sigma=3.0, N=12->14:
  |q_N| = 0.5804033349
  |d_N+2|/|d_N| = 0.5804033349
  1-|q_N| = 0.4195966651.                               (DRC-12)
```

The planted build fails already because the denominator norm can expand
violently (`|q_N|>1`) at the early breaking steps.

## 5. Candid reading

This note does not yet prove the cofinal contraction law. What it does prove is
that the live denominator modulus target is now as simple as it can be:

```text
successive safe-shell denominator norms must contract.    (DRC-13)
```

No hidden complex geometry remains on the modulus side.

## 6. Status

```text
proved:
  |q_N| is exactly the radial ratio |1-theta_N+2| / |1-theta_N|;

proved:
  the modulus deficit 1-|q_N| is exactly a shell contraction deficit for the
  denominator norm;

observed:
  zeta shows strong audited radial contraction, with median deficit about
  0.3072;

observed:
  the planted build fails already by radial expansion at the early breaking
  steps;

reduced:
  DEN-SUBUNIT-POLAR to DEN-RADIAL-CONTRACTION plus the already isolated
  angular penalty;

next:
  derive a finite shell law forcing the contraction of |1-theta_N|, or autopsy
  that radial deficit into an even smaller exact recurrence target.
```
