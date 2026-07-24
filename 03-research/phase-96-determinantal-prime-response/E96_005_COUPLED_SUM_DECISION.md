# E96.005 - Coupled-sum decision

## 1. Termwise matching is not required

The sufficient but much stronger assertion

```text
integral_0^1 BR_t(s;s_*;y)dt
 =E(s;s_*;y)+small                                   (1.1)
```

for every individual shift `y` is not implied by the determinant identity and
is not required by E96.004.  The finite CCM numerator is a nonlinear response
to the complete prime matrix; its one-cell derivative depends on all other
cells through `P` and `chi`.

## 2. Admissible target

The primary quantity is the complete signed sum

```text
SUMDEF_(L,N)(s;s_*)
 =sum_n Lambda(n)n^(-1/2)
  integral_0^1[BR_t-E](s;s_*;log n)dt.               (2.1)
```

It must be combined with `BASE` before estimation.  Taking absolute values
over `n` before the determinant cancellation would reproduce the finite
truncation wall.

## 3. Exact force location

The force-bearing theorem is now

```text
DETERMINANTAL-PRIME-RESPONSE:
BASE_(L,N)+SUMDEF_(L,N)->0                            (3.1)
```

locally uniformly along one resolved directed family.

This is not a new weakening of the direct anchor.  It is its exact expansion
in finite prime-cell directions.

## 4. Status

```text
rejected as unnecessary and over-strong:
  termwise prime-cell matching;

open:
  DETERMINANTAL-PRIME-RESPONSE.
```

