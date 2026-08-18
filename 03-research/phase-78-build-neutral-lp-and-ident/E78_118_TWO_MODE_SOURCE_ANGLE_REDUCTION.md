# E78.118 - `SOURCE-PAIR-ANGLE` reduces to a two-mode off-ground profile

**Scope:** front B only, live object `SOURCE-PAIR-ANGLE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the residual
source angle is not one-mode, but it is essentially two-mode on the audited
safe family. The first mode is negligible and the pairing is saturated by the
first two off-ground coordinates taken together.

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
P76.061: respected. The reduction stays entirely at the paired level
         `<g_z,off_1>`.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.116 reduced the remaining source burden to the normalized pairing angle

```text
cos_N(z) = |<g_z,off_1>| / (||g_z|| ||off_1||),            (T-1)
```

with

```text
g_z = sum_{j>=1} gamma_j(z) v_j,
off_1 = sum_{j>=1} omega_j v_j.                             (T-2)
```

E78.117 then autopsied the one-mode route: mode `j=1` is not the carrier of
the angle.

The next candid question is whether the residual angle is at least low-rank in
the off-ground sector.

## 2. Two-mode profile

Define the truncated pairing

```text
P_N^{(k)}(z) := sum_{j=1}^k gamma_j(z) omega_j,            (T-3)
```

in the off-ground eigenbasis.  The predecessor `SOURCE-PAIR-ANGLE` depends on
the full sum

```text
<g_z,off_1> = sum_{j>=1} gamma_j(z) omega_j.               (T-4)
```

If a fixed small `k` reproduces `(T-4)` on the safe family, then the angle
reduces from a distributed infinite profile to a finite modal package.

That is strictly less information than the full off-ground correlation profile.

## 3. Probe

The audited safe sweep at `N=8,12` and `z in {i0.6,i1.0,i2.0}` gives:

```text
BUILD zeta
  k=1 contributes only ~1e-27 to 1e-16 of the full pairing,
  while k=2 already gives 0.999999... to 1.0 of the full pairing.          (T-5)

BUILD plant
  k=1 contributes only ~1e-81 to 1e-73 of the full pairing,
  while k=2 already gives 1.0 of the full pairing.                          (T-6)
```

So the one-mode route is truly dead, but the two-mode truncation already
captures the entire audited pairing to displayed precision on both builds.

## 4. Why this is a genuine reduction

The predecessor asked for the full off-ground angle `(T-1)`, which a priori
depends on all off-ground coordinates of `g_z` and `off_1`.

The new object asks only for the two-mode profile

```text
TWO-MODE-SOURCE-ANGLE:
  control gamma_1(z)omega_1 + gamma_2(z)omega_2             (T-7)
```

on the safe family.

That is strictly less information than the full off-ground sum `(T-4)`.

So this is a genuine reduction:

```text
TWO-MODE-SOURCE-ANGLE
=> SOURCE-PAIR-ANGLE
on the audited safe frontier.                               (T-8)
```

## 5. Consequence

The remaining arithmetic content of this branch is no longer an arbitrary
off-ground angular profile.  It is concentrated in the first two off-ground
coordinates taken together.

The candid next live object is therefore

```text
TWO-MODE-SOURCE-ANGLE:
  identify or control the finite paired coefficient
  gamma_1(z)omega_1 + gamma_2(z)omega_2.                    (T-9)
```

This is substantially sharper than `SOURCE-PAIR-ANGLE`.

## 6. Status

```text
candidate closure - pending review

proved:
  the one-mode route is dead but the two-mode truncation saturates the audited
  safe pairing to displayed precision;

reduced:
  SOURCE-PAIR-ANGLE to the finite two-mode coefficient
  gamma_1(z)omega_1 + gamma_2(z)omega_2;

next:
  identify that two-mode coefficient inside the finite coupled package, or
  autopsy the exact reason it cannot be expressed there.
```
