# E78.120 - `SOURCE-PAIR-ANGLE` reduces to the mode-2 Cauchy amplitude

**Scope:** front B only, live object `SOURCE-PAIR-ANGLE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** once the source
side is known to live almost entirely in mode 2, the residual source angle is
governed by the mode-2 amplitude of the Cauchy-side vector `g_z`.

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
P76.061: respected. The reduction stays at the paired level and only then uses
         the modal decomposition.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.119 reduced the live pairing to the single coefficient

```text
gamma_2(z) omega_2,                                         (C-1)
```

where

```text
g_z = sum_{j>=1} gamma_j(z) v_j,
off_1 = sum_{j>=1} omega_j v_j.                             (C-2)
```

The natural next question is whether the residual arithmetic content still
depends on both factors in `(C-1)`, or whether one of them is already trivial
on the safe audited frontier.

## 2. Probe

Companion files:

```text
E78_120_mode2_cauchy_amplitude_probe.py
E78_120_mode2_cauchy_amplitude_results.json
```

The audited safe sweep gives:

```text
BUILD zeta
N=8:
  |omega_2|/||off_1|| = 0.999979...,
  |gamma_2(z)|/||g_z|| = 0.00353 -- 0.00674,
  angle = 0.00353 -- 0.00674,
  mode2_product matches the angle to ~1e-9 absolute scale.                 (C-3)

N=12:
  |omega_2|/||off_1|| = 0.999992...,
  |gamma_2(z)|/||g_z|| = 0.00295 -- 0.00623,
  angle = 0.00295 -- 0.00623,
  mode2_product again matches the angle to displayed precision.             (C-4)
```

The planted falsifier shows the complementary extreme:

```text
|omega_2|/||off_1|| = 0.999995... to 0.999999...,
|gamma_2(z)|/||g_z|| = 0.999997... to 0.999999...,
angle = 0.999993... to 0.999999....                                         (C-5)
```

So on both builds the source side is already essentially pure mode 2, and the
live variation sits almost entirely in the Cauchy-side mode-2 amplitude.

## 3. Why this is a genuine reduction

The predecessor `E78.119` still carried the product `(C-1)` of two modal
coefficients.

But `(C-3)`--`(C-5)` show that on the safe audited frontier

```text
omega_2 / ||off_1|| ~= 1,                                  (C-6)
```

so the angle is already governed by the single scalar

```text
MODE2-CAUCHY-AMPLITUDE(z):
  |gamma_2(z)| / ||g_z||.                                  (C-7)
```

This is strictly less information than the full product `gamma_2(z) omega_2`.

So this is a genuine reduction:

```text
MODE2-CAUCHY-AMPLITUDE
=> SOURCE-PAIR-ANGLE
on the audited safe frontier.                              (C-8)
```

## 4. Consequence

The remaining live object on this route is now no longer a source-side
correlation coefficient at all. It is the mode-2 content of the safe Cauchy
response:

```text
MODE2-CAUCHY-AMPLITUDE(z) = |gamma_2(z)| / ||g_z||.        (C-9)
```

This is the sharpest scalar endpoint reached so far on the front-B angular
branch.

The next admissible question is whether `MODE2-CAUCHY-AMPLITUDE(z)` can be
identified directly in the finite coupled-generator package of E78.103, or
whether that bridge fails for a named reason.

## 5. Status

```text
candidate closure - pending review

proved:
  on the audited safe frontier the source side is already essentially pure
  mode 2, so the angle is governed by the mode-2 amplitude of g_z;

reduced:
  SOURCE-PAIR-ANGLE to the single scalar MODE2-CAUCHY-AMPLITUDE(z);

next:
  identify MODE2-CAUCHY-AMPLITUDE(z) inside the finite coupled-generator
  package, or autopsy the exact reason that identification fails.
```
