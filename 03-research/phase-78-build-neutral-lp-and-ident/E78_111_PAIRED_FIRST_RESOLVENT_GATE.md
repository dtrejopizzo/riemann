# E78.111 - The second-resolvent tail enters only through a paired first-resolvent product

**Scope:** front B only, live object `G0-FIRST-RESOLVENT`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the only part of
the second-resolvent tail that matters for the derivative package is not the
vector tail itself, but the paired product of two off-ground first resolvents.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as the theorem.
P76.061: respected. The source is paired with the selected Cauchy response
         before any estimate.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.110 reduced the zeta-side tail problem to the first resolvent:

```text
||tail(A^-2 1)|| / ||ground(A^-2 1)||
 <= |nu0/nu1| * ||off(A^-1 1)|| / ||ground(A^-1 1)||.       (P-1)
```

But the derivative package from E78.103 never uses `A^-2 1` as a free vector.
It uses it only through Cauchy pairings of the form

```text
<r_z, (I-P0)A^-2 1>,                                        (P-2)
```

where `r_z` is the safe Cauchy row.

So the candid next question is whether `(P-2)` admits a smaller paired object
than the vector norm in `(P-1)`.

## 2. Exact paired gate

Let

```text
tail_2 := (I-P0)A^-2 1,
off_1  := (I-P0)A^-1 1.                                     (P-3)
```

Because `A` is selfadjoint and commutes with `P0`,

```text
tail_2 = A^-1 off_1.                                        (P-4)
```

Hence for every test row `r`,

```text
<r, tail_2>
 = <r, A^-1 off_1>
 = <A^-1 r, off_1>
 = <(I-P0)A^-1 r, off_1>.                                  (P-5)
```

The last step uses `off_1 ⟂ v_0`.

So the exact second-resolvent tail pairing is not a free norm quantity; it is
the bilinear first-resolvent product

```text
<r, (I-P0)A^-2 1>
 = <(I-P0)A^-1 r, (I-P0)A^-1 1>.                           (P-6)
```

Immediately,

```text
|<r, (I-P0)A^-2 1>|
 <= ||(I-P0)A^-1 r|| * ||(I-P0)A^-1 1||.                   (P-7)
```

This is the exact paired replacement for the ambient tail norm.

## 3. Why this is a genuine reduction

The predecessor `G0-FIRST-RESOLVENT` still carried the vector tail problem of
`A^-2 1` as an intermediate burden.

After `(P-6)`, the derivative-relevant quantity depends only on:

```text
PAIRED-FIRST-RESOLVENT:
  the off-ground first resolvent of the source 1,
  and the off-ground first resolvent of the selected Cauchy row r_z.         (P-8)
```

That is strictly less information than controlling the whole second-resolvent
tail vector.  It also obeys P76.061 in the strongest possible way: the source
is paired before any estimate.

Therefore

```text
PAIRED-FIRST-RESOLVENT  =>  the tail part of G0-FIRST-RESOLVENT
in every derivative pairing.                                             (P-9)
```

## 4. Probe

Companion files:

```text
E78_111_paired_first_resolvent_gate_probe.py
E78_111_paired_first_resolvent_gate_results.json
```

The identity `(P-6)` holds to roundoff:

```text
zeta:   relative error 2e-20 -- 4e-20
plant:  relative error 3e-39 -- 1e-38.                           (P-10)
```

On the audited `N=8` safe row family,

```text
BUILD zeta
z=i0.6: off-ground ratio of A^-1 r_z = 3.35e-4
z=i1.0: off-ground ratio of A^-1 r_z = 5.57e-4
z=i2.0: off-ground ratio of A^-1 r_z = 1.11e-3.                 (P-11)

BUILD plant
z=i0.6: 3.06e21
z=i1.0: 1.60e21
z=i2.0: 3.03e20.                                                (P-12)
```

So the Cauchy-side off-ground first resolvent is tiny on the zeta audited
ladder and fails exactly on the planted falsifier, which is the allowed break
location for front B.

## 5. Consequence

The derivative-relevant second-resolvent tail has now been reduced to the
paired first-resolvent package:

```text
control of (I-P0)A^-1 1
+ control of (I-P0)A^-1 r_z
=> control of <r_z,(I-P0)A^-2 1>.                             (P-13)
```

Hence the candid next live object is no longer a free vector tail, but

```text
PAIRED-FIRST-RESOLVENT:
  prove cofinally that the selected safe rows r_z and the source 1 both have
  negligible off-ground first-resolvent components in the zeta build.       (P-14)
```

## 6. Status

```text
candidate closure - pending review

proved:
  the exact identity
  <r,(I-P0)A^-2 1> = <(I-P0)A^-1 r, (I-P0)A^-1 1>;

reduced:
  the derivative-relevant second-resolvent tail to a paired first-resolvent
  object, eliminating the ambient tail norm from the front;

verified:
  the identity at roundoff and the expected zeta/plant separation on the
  audited safe row family;

next:
  attack the cofinal off-ground first-resolvent control for `1` and `r_z`, or
  autopsy the exact coefficient that prevents that paired statement.
```
