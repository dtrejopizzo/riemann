# E78.114 - `SOURCE-FIRST-RESOLVENT` reduces to the safe source-pairing functional

**Scope:** front B only, live object `SOURCE-FIRST-RESOLVENT`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** once the Cauchy
side has been reduced, the source side is no longer needed as a full vector.
Only the scalar functional `z -> <(I-P0)A^-1 r_z, A^-1 1>` survives.

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
P76.061: respected. The reduction keeps only the pairings with the selected
         safe Cauchy responses.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.111 gave the exact identity

```text
<r_z,(I-P0)A^-2 1> = <(I-P0)A^-1 r_z, (I-P0)A^-1 1>.       (F-1)
```

E78.112 reduced the first factor `(I-P0)A^-1 r_z` to the raw Cauchy geometry of
`r_z`.  E78.113 then closed the direct raw-geometric route for the second
factor `(I-P0)A^-1 1`.

So the candid question is: after those two steps, what part of the source side
still actually matters?

## 2. Exact reduction

Define

```text
g_z := (I-P0)A^-1 r_z.                                       (F-2)
```

Then `(F-1)` becomes

```text
<r_z,(I-P0)A^-2 1> = <g_z, A^-1 1>,                         (F-3)
```

because `g_z ⟂ v_0`, so pairing against `A^-1 1` is the same as pairing against
`(I-P0)A^-1 1`.

Therefore the derivative-relevant tail never uses the full vector
`(I-P0)A^-1 1` by itself. It uses only the scalar holomorphic family

```text
SOURCE-PAIR-FUNCTIONAL:
  S_N(z) := <(I-P0)A^-1 r_z, A^-1 1>.                       (F-4)
```

This is strictly less information than `SOURCE-FIRST-RESOLVENT`: instead of
controlling the entire vector `(I-P0)A^-1 1`, it asks only for its values under
the safe linear functionals `g_z`.

So

```text
control of S_N(z) on the safe family
=> control of the source side in every derivative-relevant tail pairing.    (F-5)
```

## 3. Why this is a genuine reduction

The predecessor asked for vector control:

```text
SOURCE-FIRST-RESOLVENT:
  control (I-P0)A^-1 1.                                     (F-6)
```

The new object asks only for the scalar family `(F-4)` indexed by safe `z`.
That removes almost all coordinates of the source vector and retains only the
part seen by the selected Cauchy responses.

So this is not a reparametrization. It is a strict reduction in information.

## 4. Probe

Companion files:

```text
E78_114_source_pair_functional_probe.py
E78_114_source_pair_functional_results.json
```

The audited data confirm the exact surviving quantity:

```text
zeta:
  N=6,8,10,12 and z in {i0.6,i1.0,i2.0}
  produce the scalar family S_N(z) directly.                (F-7)

plant:
  the same functional is well-defined and large on the
  falsifier, which is admissible in front B.                (F-8)
```

The point of the probe is not smallness; it is that after E78.112/E78.113,
these are exactly the scalar observables still carrying the source burden.

## 5. Consequence

The live source object is now no longer vectorial. It is the safe scalar family

```text
SAFE-SOURCE-PAIR:
  for safe z, control S_N(z)=<(I-P0)A^-1 r_z, A^-1 1>.      (F-9)
```

Together with E78.112:

```text
SAFE-SOURCE-PAIR + CAUCHY-GEOMETRIC-RATIO
=> derivative-relevant tail control.                        (F-10)
```

This is the sharpest candid frontier reached so far on this branch.

## 6. Status

```text
candidate closure - pending review

proved:
  the exact reduction from SOURCE-FIRST-RESOLVENT to the safe scalar family
  S_N(z)=<(I-P0)A^-1 r_z, A^-1 1>;

reduced:
  the source side from a full off-ground vector to the safe source-pairing
  functional;

verified:
  the scalar family is computed directly on the audited safe rows for both zeta
  and the falsifier;

next:
  attack SAFE-SOURCE-PAIR directly from the coupled-generator package, or
  autopsy the exact coefficient that prevents a cofinal proof for this smaller
  scalar family.
```
