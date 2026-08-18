# E78.119 - `SOURCE-PAIR-ANGLE` reduces to the second off-ground coefficient

**Scope:** front B only, live object `SOURCE-PAIR-ANGLE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the residual
source angle is not merely low-rank; on the audited safe frontier it is carried
to displayed precision by the second off-ground mode alone.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as a theorem.
P76.061: respected. The reduction stays at the paired level
         `<g_z,off_1> = sum_j gamma_j(z) omega_j`.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.118 reduced the live object to the two-mode truncation

```text
gamma_1(z) omega_1 + gamma_2(z) omega_2,                   (S-1)
```

where

```text
g_z = sum_{j>=1} gamma_j(z) v_j,
off_1 = sum_{j>=1} omega_j v_j.                            (S-2)
```

E78.117 had already shown that the `j=1` term is negligible as an explanatory
mechanism. The remaining question is whether the full pairing really needs both
terms in `(S-1)`.

## 2. Probe

Companion files:

```text
E78_119_second_mode_source_angle_probe.py
E78_119_second_mode_source_angle_results.json
```

The audited safe sweep gives:

```text
BUILD zeta
N=8,12 and z in {i0.6,i1.0,i2.0}:
  |gamma_1 omega_1| / |<g_z,off_1>| = 1e-27 to 1e-16,
  |gamma_2 omega_2| / |<g_z,off_1>| = 0.99999928 to 0.99999995.   (S-3)

BUILD plant
N=8,12 and z in {i0.6,i1.0,i2.0}:
  |gamma_1 omega_1| / |<g_z,off_1>| = 1e-82 to 1e-73,
  |gamma_2 omega_2| / |<g_z,off_1>| = 0.99999997 to 0.999999997.  (S-4)
```

So on both builds, and across the audited safe frontier, the full pairing is
already exhausted by the single coefficient `gamma_2(z) omega_2` to displayed
precision.

## 3. Why this is a genuine reduction

The predecessor `E78.118` still carried a two-mode profile `(S-1)`.

The present step shows that, on the audited safe frontier, the live pairing
reduces further to

```text
SECOND-MODE-SOURCE-ANGLE:
  gamma_2(z) omega_2.                                       (S-5)
```

This is strictly less information than the two-mode package.

So this is a genuine reduction:

```text
SECOND-MODE-SOURCE-ANGLE
=> SOURCE-PAIR-ANGLE
on the audited safe frontier.                               (S-6)
```

## 4. Consequence

The remaining arithmetic content of this branch is no longer a diffuse angle,
nor a two-mode sum. It is the single finite coefficient

```text
gamma_2(z) omega_2.                                         (S-7)
```

This is now the sharpest candid finite object reached on this route.

The next admissible question is whether `gamma_2(z) omega_2` can be identified
inside the finite coupled-generator package of E78.103, or whether that bridge
fails for a named reason.

## 5. Status

```text
candidate closure - pending review

proved:
  on the audited safe frontier the full source pairing is saturated by the
  second off-ground mode to displayed precision;

reduced:
  SOURCE-PAIR-ANGLE to the single coefficient gamma_2(z) omega_2;

next:
  identify gamma_2(z) omega_2 inside the finite coupled-generator package, or
  autopsy the exact reason that identification cannot hold.
```
