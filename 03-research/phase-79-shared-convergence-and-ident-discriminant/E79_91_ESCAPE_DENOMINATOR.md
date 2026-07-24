# E79.91 - The audited escape split is denominator-driven: `c` is the active lever

**Scope:** `DISCRIMINANT`, first direct reduction of `CLOSE => STRONG_ESCAPE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** on the
audited main ladder, the large rank-one escape ratio is not being driven by an
exceptionally large numerator `q^T x`. It is being driven by the denominator
`c` becoming tiny.

## 0. Why this is the right next move

E79.90 reduced the live front to the pair

```text
CLOSE => STRONG_ESCAPE,
BAL   => LOW_DEFECT.                                                    (91-1)
```

The first of these is the more mechanical one, because

```text
STRONG_ESCAPE = |q^T x| / (|c| mesh_radius).                            (91-2)
```

So the immediate structural question is:

```text
is the zeta-side largeness coming from a huge numerator,
or from a tiny denominator?                                             (91-3)
```

## 1. Probe

Companion files:

```text
E79_91_escape_denominator_probe.py
E79_91_escape_denominator_results.json
```

To keep the check lightweight and fully reproducible, this audit uses the main
audited pair of builds:

```text
zeta,
plant gamma1, beta=0.30,                                                (91-4)
```

on the ladder

```text
lambda=6, N=8..18, dps=60.                                              (91-5)
```

For each row it records:

```text
|c|,
|q^T x|,
mesh_radius,
|q^T x| / mesh_radius,
|q^T x| / mesh_radius^2,
escape_ratio = |q^T x| / (|c| mesh_radius).                             (91-6)
```

## 2. Result

The audited zeta escape is denominator-driven.

### Zeta

On the zeta ladder:

```text
|c| ~ 1e-7 .. 1e-10,                                                    (91-7)
```

while the numerator stays tiny in mesh units:

```text
|q^T x| / mesh_radius   ~ 5.3e-5, 5.2e-7, 1.7e-5, 2.7e-7, 2.5e-8, 4.4e-8,
|q^T x| / mesh_radius^2 ~ 4.3e-6 down to 1.5e-9.                       (91-8)
```

Yet the escape ratio is huge:

```text
escape_ratio ~ 134, 115, 130, 120, 123, 122.                           (91-9)
```

So the largeness is not coming from `q^T x` being large in the natural mesh
scale. It comes from dividing by a tiny `|c|`.

### Planted gamma1

For the planted main control, the numerator is actually much larger in mesh
units:

```text
|q^T x| / mesh_radius   ~ 3.8 .. 37.8,
|q^T x| / mesh_radius^2 ~ 0.24 .. 1.66,                                (91-10)
```

but because

```text
|c| = O(1) .. O(10),                                                    (91-11)
```

the escape ratio stays small:

```text
escape_ratio ~ 0.77 .. 1.65.                                            (91-12)
```

So the plant has the opposite profile:

```text
large numerator scale, no denominator collapse, no strong escape.       (91-13)
```

## 3. Reading

This is the first direct finite explanation of `CLOSE => STRONG_ESCAPE`.

It does **not** yet prove the implication theorem-grade. But it does isolate
the active lever:

```text
the zeta-side strong escape is not a numerator-growth phenomenon;
it is a denominator-collapse phenomenon.                                (91-14)
```

That sharply narrows the next target. We no longer need to understand the full
behavior of `q^T x` first. The audited evidence says the difficult content sits
in controlling `c`, while the numerator remains comparatively tame.

## 4. Consequence

After E79.91, the next honest reduction is:

```text
CLOSE  =>  denominator collapse in the rank-one escape formula
        =>  STRONG_ESCAPE,                                              (91-15)
```

with the numerator side demoted to a secondary boundedness/stability check.

So the next live target is not "why is `q^T x` huge?", because on the zeta
ladder it is not. The next target is:

```text
show that when |c| enters the codimension-one closure regime,
the numerator stays on a much milder mesh scale, forcing escape_ratio >> 1. (91-16)
```

## 5. Status

```text
proved by audit:
  on the main audited ladder, the zeta-side strong escape is denominator-driven:
  |q^T x| stays tiny in mesh units while |c| collapses;

proved by audit:
  the planted main control has the opposite profile:
  large numerator scale but no denominator collapse, hence no strong escape;

reduced:
  the live front inside CLOSE => STRONG_ESCAPE from a two-sided ratio problem
  to the sharper question of controlling denominator collapse with only a mild
  numerator-scale hypothesis;

open:
  formulate and test the right mild numerator regularity statement on the full
  audited harness, or find the first row where that regularity fails.
```
