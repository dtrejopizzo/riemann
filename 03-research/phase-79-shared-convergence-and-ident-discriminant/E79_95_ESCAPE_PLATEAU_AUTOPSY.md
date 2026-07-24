# E79.95 - The right numerator-side object is not a slower collapse rate, but a stable large escape plateau

**Scope:** `DISCRIMINANT`, correction of the first post-E79.94 reading.  
**Class:** AUTOPSIA HONESTA + sharper replacement target.  
**What we know after this document that we did not know before:** the audited
zeta data do **not** support the loose slogan

```text
the numerator collapses much more slowly than |c|.                      (95-1)
```

What they support instead is sharper and more concrete:

```text
the quotient
  escape_ratio = (|q^T x|/mesh_radius)/|c|
stays on a large, stable plateau on the zeta ladder.                    (95-2)
```

## 0. Why this correction is necessary

E79.94 correctly ruled out a mere upper bound on the numerator as too weak.
But its replacement wording

```text
the numerator shrinks much more slowly than |c| does                    (95-3)
```

was still too loose.

A direct step-to-step ratio audit on the certified E79.91 data shows that on
the zeta ladder the numerator and `|c|` often collapse at **comparable**
multiplicative rates from one audited section to the next.

So the true object is not a one-sided rate separation. It is the stability of
their quotient.

## 1. Stepwise ratio audit

Let

```text
N_N := |q^T x| / mesh_radius,
C_N := |c_N|.                                                            (95-4)
```

From the audited zeta rows in E79.91:

```text
N=10 / N=8:   N-ratio ~ 9.93e-3,   C-ratio ~ 1.16e-2,   gap ~ 0.855,
N=12 / N=10:  N-ratio ~ 32.10,     C-ratio ~ 28.35,     gap ~ 1.132,
N=14 / N=12:  N-ratio ~ 1.60e-2,   C-ratio ~ 1.73e-2,   gap ~ 0.923,
N=16 / N=14:  N-ratio ~ 9.29e-2,   C-ratio ~ 9.11e-2,   gap ~ 1.019,
N=18 / N=16:  N-ratio ~ 1.755,     C-ratio ~ 1.760,     gap ~ 0.997.  (95-5)
```

The key fact is not "numerator decays much slower". The key fact is:

```text
the stepwise collapse factors track each other closely.                 (95-6)
```

That is exactly why the quotient remains stable.

## 2. The actual stable object

The quantity that stays sharply organized on the zeta ladder is simply

```text
escape_ratio = N_N / C_N.                                               (95-7)
```

Numerically, from E79.91:

```text
zeta:
  134.5, 115.0, 130.3, 120.2, 122.5, 122.1,                            (95-8)
```

which is a clear large plateau.

By contrast, on the planted main control:

```text
0.77, 1.65, 1.28, 1.09, 1.32, 1.43.                                    (95-9)
```

So the honest replacement for the vague "slower collapse" story is:

```text
zeta:   large stable quotient plateau,
plant:  order-one quotient plateau.                                     (95-10)
```

## 3. Reading

This correction matters because it changes the shape of the next target.

The old, too-loose phrasing would have pushed toward a statement about relative
exponents or asymmetric rates:

```text
N_N decays slower than C_N.                                             (95-11)
```

But the audited evidence points somewhere cleaner:

```text
N_N and C_N co-move, and the true discriminating content is the
plateau value of N_N / C_N.                                             (95-12)
```

That is a much more concrete finite object.

## 4. Consequence

After E79.95, the live target inside the escape branch is no longer

```text
"find a slower-collapse theorem for the numerator".                     (95-13)
```

It is:

```text
explain why the quotient
  (|q^T x|/mesh_radius)/|c|
locks onto a large zeta-side plateau, while the planted build remains
order-one.                                                              (95-14)
```

That is strictly stronger and more faithful to the audited data.

## 5. Status

```text
corrected:
  the audited data do not support the loose slogan "numerator collapses much
  more slowly than c";

proved by audit:
  what is actually stable on the zeta ladder is the large plateau of the
  quotient escape_ratio = (|q^T x|/mesh_radius)/|c|;

reduced:
  the escape branch to explaining a large quotient plateau rather than a
  vague rate separation;

next:
  search for the finite package identity or normalization that pins this
  plateau at the zeta-side scale and keeps the planted build order-one.
```
