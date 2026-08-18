# E79.94 - A mild upper regularity of the numerator is not enough to force strong escape

**Scope:** `DISCRIMINANT`, autopsy inside the denominator-driven escape route.  
**Class:** AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the naive next
target

```text
CLOSE + (numerator is merely small / bounded in mesh units)
  => STRONG_ESCAPE                                                      (94-1)
```

is too weak as stated. An upper bound on the numerator alone cannot force large
escape; the mechanism needs some form of non-collapse or lower floor relative to
`|c|`.

## 0. Why this autopsy is necessary

E79.91 showed that the zeta-side escape mechanism is denominator-driven:

```text
escape_ratio = |q^T x| / (|c| mesh_radius),                            (94-2)
```

with `|c|` collapsing while the numerator stays tiny in mesh units.

That naturally tempts the weaker slogan:

```text
"small denominator + tame numerator should force strong escape".        (94-3)
```

But this is not logically sharp enough. The exact identity already reveals the
problem: a small **upper** bound on the numerator says nothing about whether the
quotient is large or tiny.

## 1. Exact obstruction

Write

```text
N_N := |q^T x| / mesh_radius.                                           (94-4)
```

Then the escape ratio is exactly

```text
escape_ratio = N_N / |c_N|.                                             (94-5)
```

So:

```text
- an upper bound N_N <= C does not force escape_ratio to be large;
- to force escape_ratio >> 1 from |c_N| << 1, one still needs N_N to stay
  away from zero at an appropriate relative scale.                      (94-6)
```

In other words, the live content is not just "numerator tame", but

```text
numerator non-collapse relative to the denominator collapse.            (94-7)
```

## 2. Why the zeta data already show this

From E79.91, on the audited zeta ladder:

```text
N=8:  N_N ~ 5.28e-5,   |c| ~ 3.93e-7,  escape ~ 134.5,
N=10: N_N ~ 5.25e-7,   |c| ~ 4.56e-9,  escape ~ 115.0,
N=16: N_N ~ 2.50e-8,   |c| ~ 2.04e-10, escape ~ 122.5.                 (94-8)
```

So the numerator does **not** stay fixed. It shrinks by several orders of
magnitude along the ladder.

What survives is more specific:

```text
it shrinks much more slowly than |c| does.                              (94-9)
```

That is the real mechanism compatible with the data.

## 3. Consequence for the live target

The next useful target is therefore **not**

```text
CLOSE + (N_N <= constant) => STRONG_ESCAPE.                             (94-10)
```

That target is too weak and should not be pursued.

The candid replacement is something of the form

```text
CLOSE + (N_N does not collapse as fast as |c_N|) => STRONG_ESCAPE,      (94-11)
```

or more concretely:

```text
N_N / |c_N| >= A                                                        (94-12)
```

for an audited lower scale `A`, which is exactly the escape ratio itself.

So the problem has sharpened once more:

```text
the missing content is a lower-scale statement on the numerator side,
not an upper regularity statement.                                      (94-13)
```

## 4. Reading

This is a useful autopsy because it prevents the next false simplification.

After E79.91, it was tempting to say:

```text
the numerator is harmless, only the denominator matters.                (94-14)
```

That is too loose. The correct version is:

```text
the denominator is the active lever,
but the numerator still needs a non-collapse statement strong enough
to keep the quotient large.                                             (94-15)
```

So the numerator is not the main source of difficulty, but neither can it be
replaced by a vacuous upper bound.

## 5. Status

```text
proved by exact identity:
  a mere upper bound on the numerator cannot force strong escape;

proved by audit:
  on the zeta ladder the numerator itself still shrinks substantially, so the
  real mechanism is slower numerator collapse relative to denominator collapse,
  not numerator constancy;

corrected:
  the next target is not "mild numerator regularity" in the sense of an upper
  ceiling, but a genuine lower-scale or relative non-collapse statement;

reduced:
  the live front inside CLOSE => STRONG_ESCAPE to finding the right
  relative-scale statement for N_N = |q^T x|/mesh_radius.
```
