# E78.134 - `SAFE-F-NONVANISHING` is not a new derivative burden

**Scope:** front B only, current exact triple burden for `DMU-COUPLED-GENERATOR`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the denominator
clause in the derivative package,
`SAFE-F-NONVANISHING: |F_b(i sigma;mu)| >= m > 0`,
does not define a new front below `MU-DIR`; it is exactly the same zero-free
denominator condition already required on the fixed-`L` IDENT side for the
two-generator quotient `W'/(1+W)`.  So, relative to the standing front-B work,
the derivative-specific residual burden is only `SAFE-H-BOUND + SAFE-Y-BOUND`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity/Weil-form target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No wrong-sign lower-bound mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral-gap hypothesis.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       and no ambient inverse norm is promoted.
P76.061: respected. The reduction is purely inside the paired two-generator
         algebra before any inversion estimate.
E72.16/E77.7az: respected. This is front B; planted separation is admissible.
```

## 1. The two appearances of the same denominator

On the fixed-`L` IDENT side, E78.6 and E78.7 reduced the finite arithmetic
object to the coupled quotient

```text
W'_{L,N}(z) / (1 + W_{L,N}(z)),                                             (D-1)
```

with the explicit side condition

```text
inf_{z in K_i} |1 + W_L(z)| > 0,                                            (D-2)
```

and the finite denominators eventually nonvanishing on the same safe compact.

On the derivative side, E78.103-E78.104 write

```text
T_b(z) = F_b(z)/(z-d_b),
F_b(z) = 1 + H_b(z) + H_b^bd,                                               (D-3)
```

and then require

```text
SAFE-F-NONVANISHING:
  |F_b(i sigma;mu)| >= m_{L,K,eta} > 0.                                     (D-4)
```

But by the exact two-generator identity of P76.041 / E78.6,

```text
F_b(z) = F_{L,N}(z) = 1 + W_{L,N}(z).                                       (D-5)
```

So `(D-4)` is not a new object. It is the same denominator clause already
present in `(D-1)`--`(D-2)`.

## 2. Exact consequence for the DMU burden

E78.104 proved the exact implication

```text
SAFE-F-NONVANISHING
+ SAFE-H-BOUND
+ SAFE-Y-BOUND
=> DMU-COUPLED-GENERATOR.                                                    (D-6)
```

Substituting `(D-5)` shows that the first clause of `(D-6)` is exactly the
front-B denominator condition already inherited from the fixed-`L`
two-generator package.

Hence the derivative route does **not** introduce three independent new burdens.
It introduces only two derivative-specific ones, relative to the standing
fixed-`L` arithmetic front:

```text
existing shared clause:
  zero-free denominator for 1 + W_{L,N};                                    (D-7)

new derivative-specific clauses:
  SAFE-H-BOUND + SAFE-Y-BOUND.                                               (D-8)
```

Therefore:

```text
[shared denominator clause from E78.6-E78.8]
+ SAFE-H-BOUND
+ SAFE-Y-BOUND
=> DMU-COUPLED-GENERATOR.                                                    (D-9)
```

This is strictly less new information than carrying the whole triple burden as
if all three clauses were born inside the derivative package.

## 3. Why this is a genuine reduction

The predecessor burden treated

```text
SAFE-F-NONVANISHING + SAFE-H-BOUND + SAFE-Y-BOUND                           (D-10)
```

as a fresh three-part load below `MU-DIR`.

After `(D-5)`--`(D-9)`, one part of `(D-10)` is recognized as already shared
with the standing fixed-`L` IDENT front.  So the residual derivative-specific
work shrinks to the pair

```text
SAFE-H-BOUND + SAFE-Y-BOUND,                                                (D-11)
```

modulo the pre-existing denominator clause.

That is a genuine reduction in the derivative burden. It removes one whole
clause from the set of *new* obligations introduced by the `DMU` package.

## 4. What this does not prove

This note does **not** prove the denominator clause itself.  E78.8 only audited
it on the tested safe ladder and explicitly left theorem-grade nonvanishing
open.

So the right reading is:

```text
SAFE-F-NONVANISHING remains open theorem-grade,
but it is not a new open object created by DMU.                               (D-12)
```

The live derivative-specific burden is smaller than it looked, but not yet
closed.

## 5. Consequence

The honest derivative-side return point is now:

```text
shared front-B denominator clause for 1+W
+ new derivative-specific burden SAFE-H-BOUND + SAFE-Y-BOUND.               (D-13)
```

So the next admissible step is not to reopen a separate denominator front under
`MU-DIR`, but to attack:

```text
1. theorem-grade inheritance of the shared denominator clause, if needed;
2. SAFE-H-BOUND and SAFE-Y-BOUND as the only genuinely new derivative burdens. (D-14)
```

## 6. Status

```text
candidate closure - pending review

proved:
  SAFE-F-NONVANISHING is exactly the same denominator condition
  F_b = 1 + W_{L,N} already present in the fixed-L IDENT package;

reduced:
  the derivative-specific burden below DMU-COUPLED-GENERATOR from a fresh
  three-part load to the pair SAFE-H-BOUND + SAFE-Y-BOUND, modulo the
  pre-existing shared denominator clause;

clarified:
  SAFE-F remains theorem-grade open, but not as a new front created by MU-DIR;

next:
  attack SAFE-H-BOUND / SAFE-Y-BOUND directly, while treating denominator
  nonvanishing as a shared front-B clause rather than a separate DMU burden.
```
