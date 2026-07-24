# E78.116 - The `SOURCE-OFFGROUND-NORM` route is dead; it loses the off-ground correlation angle

**Scope:** front B only, live object `SOURCE-OFFGROUND-NORM`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** controlling the
source norm `||(I-P0)A^-1 1||` cannot force the safe source pairings. The exact
missing quantity is the normalized off-ground correlation
`|<g_z,off_1>| / (||g_z|| ||off_1||)`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as a theorem of closure.
P76.061: respected. The autopsy is phrased entirely at the paired level
         `S_N(z)=<g_z,off_1>`.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.115 reduced the live source object to the single scalar sequence

```text
SOURCE-OFFGROUND-NORM(N) := ||off_1||,
off_1 := (I-P0)A^-1 1,                                      (A-1)
```

through the exact bound

```text
|S_N(z)| <= ||g_z|| ||off_1||,
g_z := (I-P0)A^-1 r_z.                                      (A-2)
```

The question is whether that route can ever be sharp enough to prove the safe
source pairings.

## 2. Exact missing coefficient

The pairing factors exactly as

```text
|S_N(z)| = ||g_z|| ||off_1|| cos_N(z),                      (A-3)
```

where

```text
cos_N(z) := |<g_z,off_1>| / (||g_z|| ||off_1||).            (A-4)
```

So the route of E78.115 forgets precisely the factor `cos_N(z)`.

## 3. Probe

Companion files:

```text
E78_116_source_angle_autopsy_probe.py
E78_116_source_angle_autopsy_results.json
```

The audited values are:

```text
BUILD zeta
N=6,8,10,12 and z in {i0.6,i1.0,i2.0}:
  cos_N(z) lies between 2.95e-3 and 8.54e-3.                (A-5)

BUILD plant
N=6,8,10,12 and z in {i0.6,i1.0,i2.0}:
  cos_N(z) lies between 0.999993 and 0.999999.              (A-6)
```

So on the zeta ladder the safe source pairing is smaller than the norm product
by roughly two and a half orders of magnitude, while on the planted falsifier
the norm bound is essentially saturated.

## 4. Autopsy

This closes the `SOURCE-OFFGROUND-NORM` route.

The route fails for an exact reason:

```text
the norm reduction throws away the off-ground correlation angle cos_N(z).    (A-7)
```

That angle is tiny on zeta and essentially `1` on the planted falsifier. So
the arithmetic content of the safe source pairings is not in the source norm by
itself; it is in the signed alignment between `g_z` and `off_1`.

Therefore

```text
SOURCE-OFFGROUND-NORM  is not an admissible forcing object for SAFE-SOURCE-PAIR. (A-8)
```

## 5. Consequence

The honest next live object is the angular factor itself:

```text
SOURCE-PAIR-ANGLE:
  control cos_N(z)=|<g_z,off_1>| / (||g_z|| ||off_1||)
  on the safe row family.                                   (A-9)
```

That is the exact quantity lost by the dead source-norm route, and it is where
the zeta/plant separation actually lives.

## 6. Status

```text
candidate closure - pending review

proved:
  the exact factorization |S_N(z)| = ||g_z|| ||off_1|| cos_N(z);

autopsied:
  the route through SOURCE-OFFGROUND-NORM loses the decisive factor cos_N(z);

closed:
  SOURCE-OFFGROUND-NORM as a forcing object for SAFE-SOURCE-PAIR;

next:
  attack SOURCE-PAIR-ANGLE directly, or identify an equivalent finite coupled
  coefficient carrying that same angular cancellation.
```
