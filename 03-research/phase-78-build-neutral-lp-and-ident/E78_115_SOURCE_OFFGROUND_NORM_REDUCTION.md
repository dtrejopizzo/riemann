# E78.115 - `SAFE-SOURCE-PAIR` reduces to the single scalar `||(I-P0)A^-1 1||`

**Scope:** front B only, live object `SAFE-SOURCE-PAIR`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** once the safe
Cauchy side has been reduced, the entire source burden is carried by a single
scalar sequence, the off-ground norm of `A^-1 1`.

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
P76.061: respected. The selected Cauchy response is paired first; only then is
         Cauchy-Schwarz applied to the paired source term.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.114 reduced the source side to the safe scalar family

```text
S_N(z) := <(I-P0)A^-1 r_z, A^-1 1>.                         (N-1)
```

E78.112 had already reduced the Cauchy-side factor `(I-P0)A^-1 r_z`.

So the question is whether `(N-1)` still requires a whole scalar family on the
source side, or whether the source contribution can be collapsed further.

## 2. Exact scalar reduction

Write

```text
g_z := (I-P0)A^-1 r_z,
off_1 := (I-P0)A^-1 1.                                      (N-2)
```

Then

```text
S_N(z) = <g_z, off_1>,                                      (N-3)
```

because `g_z ⟂ v_0`.

By Cauchy-Schwarz,

```text
|S_N(z)| <= ||g_z|| * ||off_1||.                            (N-4)
```

This is exact and immediately shows that the entire source dependence of the
safe family enters through the single scalar

```text
SOURCE-OFFGROUND-NORM(N):
  ||(I-P0)A^-1 1||.                                         (N-5)
```

Together with E78.112,

```text
CAUCHY-GEOMETRIC-RATIO(z) + SOURCE-OFFGROUND-NORM
=> SAFE-SOURCE-PAIR.                                        (N-6)
```

## 3. Why this is a genuine reduction

The predecessor `SAFE-SOURCE-PAIR` asked for a scalar family indexed by safe
`z`.

The new object asks only for one scalar per section:

```text
SOURCE-OFFGROUND-NORM(N).                                   (N-7)
```

That is strictly less information: it removes the `z` dependence from the
source side entirely.

So this is not a rephrasing. It is a real shrink of the live object.

## 4. Probe

Using the audited safe family `z in {i0.6,i1.0,i2.0}`:

```text
BUILD zeta
N= 6: ||off_1|| = 1.87e8
       pair = 1.35e23, 7.27e22, 2.37e22
       bound = 1.68e25, 1.30e25, 5.13e24
N= 8: ||off_1|| = 3.16e10
       pair = 5.05e29, 2.62e29, 7.71e28
       bound = 7.50e31, 5.74e31, 2.19e31
N=10: ||off_1|| = 8.27e12
       pair = 9.02e36, 4.59e36, 1.26e36
       bound = 1.06e39, 8.04e38, 2.99e38
N=12: ||off_1|| = 1.42e15
       pair = 3.44e43, 1.72e43, 4.52e42
       bound = 5.52e45, 4.19e45, 1.53e45.                  (N-8)
```

For the planted falsifier the same bound is essentially saturated on the
audited rows, which is admissible in front B:

```text
pair ~= bound on the tested safe family.                    (N-9)
```

The purpose of the probe is not smallness. It is to verify that the exact bound
really does collapse all source dependence to `||(I-P0)A^-1 1||`.

## 5. Consequence

The only surviving source datum on this branch is no longer a vector and no
longer a scalar family. It is the single sequence

```text
SOURCE-OFFGROUND-NORM(N) = ||(I-P0)A^-1 1||.                (N-10)
```

This is the sharpest source-side reduction reached so far:

```text
SOURCE-OFFGROUND-NORM + CAUCHY-GEOMETRIC-RATIO
=> SAFE-SOURCE-PAIR
=> derivative-relevant tail control.                        (N-11)
```

## 6. Status

```text
candidate closure - pending review

proved:
  the exact bound |S_N(z)| <= ||(I-P0)A^-1 r_z|| * ||(I-P0)A^-1 1||;

reduced:
  SAFE-SOURCE-PAIR to the single scalar sequence
  SOURCE-OFFGROUND-NORM(N);

verified:
  the reduction on the audited zeta ladder and on the planted falsifier;

next:
  attack SOURCE-OFFGROUND-NORM directly, or autopsy the exact coefficient that
  prevents a cofinal proof for this one remaining scalar sequence.
```
