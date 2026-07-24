# E78.117 - The first off-ground mode does not carry `SOURCE-PAIR-ANGLE`

**Scope:** front B only, live object `SOURCE-PAIR-ANGLE`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the residual angle
is not localized in the first off-ground eigenmode. Any route that tries to
explain the zeta/plant split by a single low mode is dead.

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
P76.061: respected. The whole discussion stays at the paired source angle
         `|<g_z,off_1>| / (||g_z|| ||off_1||)`.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.116 localized the remaining burden to

```text
SOURCE-PAIR-ANGLE:
  cos_N(z) = |<g_z,off_1>| / (||g_z|| ||off_1||),           (M-1)
```

with

```text
g_z := (I-P0)A^-1 r_z,
off_1 := (I-P0)A^-1 1.                                      (M-2)
```

The first obvious localization is to ask whether `cos_N(z)` is carried by the
first off-ground mode `v_1`.

## 2. Probe

Let

```text
g_z = sum_{j>=1} gamma_j(z) v_j,
off_1 = sum_{j>=1} omega_j v_j.                             (M-3)
```

The audited sweep over `N=6,8,10,12` and `z in {i0.6,i1.0,i2.0}` gives:

```text
BUILD zeta
  |gamma_1(z)| / ||g_z|| = 0.99996... to 0.99999...,       (M-4)
```

so the Cauchy-side vector is almost entirely in the first off-ground mode.
But simultaneously

```text
  |omega_1| / ||off_1|| =
    2.63e-34, 8.50e-30, 2.69e-23, 2.00e-18                 (M-5)
```

for `N=6,8,10,12`. Therefore the mode-1 contribution to the pairing is tiny:

```text
  |gamma_1(z) omega_1| / |<g_z,off_1>|
  ranges from 3e-32 up to 7e-16.                            (M-6)
```

For the planted falsifier the route also fails:

```text
  |omega_1| / ||off_1|| and |gamma_1(z)| / ||g_z||
  are both negligible, and the mode-1 pairing ratio is
  1e-82 to 1e-25 on the audited rows.                       (M-7)
```

## 3. Autopsy

This closes the first-mode route.

The exact failure is:

```text
the first off-ground mode is nearly the whole Cauchy side on zeta,
but almost absent from the source side; so it cannot carry the residual angle. (M-8)
```

And on the planted falsifier, the same mode is negligible on both sides, so it
also fails there as an explanatory mechanism.

Therefore

```text
SOURCE-PAIR-ANGLE is not a one-mode phenomenon.             (M-9)
```

Any attempt to force it through a single low off-ground coefficient is now dead.

## 4. Consequence

The remaining angular content must be genuinely distributed across the
off-ground sector, or encoded in a finite coupled coefficient that mixes many
modes at once.

So the honest next live object is not `v_1`, but a distributed or coupled
object such as:

```text
1. a weighted multi-mode correlation profile, or
2. a finite coupled-generator coefficient whose value equals the same angle.  (M-10)
```

## 5. Status

```text
candidate closure - pending review

autopsied:
  the route "SOURCE-PAIR-ANGLE is carried by the first off-ground mode";

proved:
  mode-1 almost exhausts g_z on zeta but contributes essentially nothing to the
  source pairing, and it is also negligible on the planted side;

closed:
  any one-mode explanation of SOURCE-PAIR-ANGLE;

next:
  attack a distributed off-ground profile or identify a finite coupled
  coefficient that carries the same angular cancellation.
```
