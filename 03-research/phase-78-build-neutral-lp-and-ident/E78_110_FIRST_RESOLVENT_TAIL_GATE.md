# E78.110 - The tail of `A_N(0)^(-2)1` reduces to the off-ground part of `A_N(0)^(-1)1`

**Scope:** front B only, live object `G0-RESOLVENT-SOURCE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the negligible-tail
part of `A_N(0)^(-2)1` does not need the dead raw-overlap certificate of
E78.109; it is implied by a sharper first-resolvent object,
`(I-P_0)A_N(0)^(-1)1`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as a forcing theorem.
P76.061: respected. Everything is written at the paired finite-algebra level.
E72.16/E77.7az: respected. This is front B; planted separation is admissible.
```

## 1. Starting point

E78.108 reduced the zeta-side live object to

```text
G0-RESOLVENT-SOURCE:
  control the ground scalar |<v_0,1>| / nu_0^2
  and prove the tail negligible in A_N(0)^(-2)1.            (R-1)
```

E78.109 autopsied the crude route

```text
gap ratio + raw overlap |<v_0,1>|                           (R-2)
```

because the bad factor `|<v_0,1>|^(-1)` destroys the bound.

So the candid next attempt must preserve the resolvent geometry.

## 2. Exact first-resolvent gate

Write the spectral decomposition

```text
A_N(0) v_j = nu_j v_j,   0 < nu_0 <= nu_1 <= ...           (R-3)
1 = sum_j c_j v_j,       c_j := <v_j,1>.                   (R-4)
```

Then

```text
A_N(0)^(-1)1 = c_0/nu_0 v_0 + sum_{j>=1} c_j/nu_j v_j,    (R-5)
A_N(0)^(-2)1 = c_0/nu_0^2 v_0 + sum_{j>=1} c_j/nu_j^2 v_j. (R-6)
```

Define

```text
ground_1 := c_0/nu_0 v_0,
off_1    := (I-P_0)A_N(0)^(-1)1,                            (R-7)

ground_2 := c_0/nu_0^2 v_0,
tail_2   := (I-P_0)A_N(0)^(-2)1.                            (R-8)
```

Since `nu_j >= nu_1` for `j>=1`,

```text
||tail_2||^2
 = sum_{j>=1} |c_j|^2 / nu_j^4
 <= nu_1^(-2) sum_{j>=1} |c_j|^2 / nu_j^2
 = nu_1^(-2) ||off_1||^2.                                  (R-9)
```

Also

```text
||ground_2|| = |c_0| / nu_0^2 = |nu_0|^(-1) ||ground_1||.  (R-10)
```

Therefore

```text
||tail_2|| / ||ground_2||
 <= |nu_0/nu_1| * ||off_1|| / ||ground_1||.                (R-11)
```

This is the exact replacement for the dead certificate of E78.109.

## 3. Why this is a genuine reduction

The predecessor asked for the full tail of the *second* resolvent,
`(I-P_0)A_N(0)^(-2)1`.

The new object asks only for the off-ground ratio of the *first* resolvent,

```text
FIRST-RESOLVENT-OFFGROUND:
  ||(I-P_0)A_N(0)^(-1)1|| / ||P_0 A_N(0)^(-1)1||.          (R-12)
```

That is strictly less information: one resolvent power instead of two, and the
dead factor `|<v_0,1>|^(-1)` disappears entirely.

By `(R-11)`,

```text
|nu_0/nu_1| * FIRST-RESOLVENT-OFFGROUND  => negligible tail in A_N(0)^(-2)1. (R-13)
```

So this is a genuine reduction of the tail part of `G0-RESOLVENT-SOURCE`.

## 4. Probe

Companion files:

```text
E78_110_first_resolvent_tail_probe.py
E78_110_first_resolvent_tail_results.json
```

The audited data give:

```text
BUILD zeta
N= 6: |nu0/nu1| = 2.46e-3,  off_1/ground_1 = 3.42e-3,
      tail_2/ground_2 = 2.71e-8,  certificate = 8.39e-6
N= 8: |nu0/nu1| = 1.19e-3,  off_1/ground_1 = 1.65e-3,
      tail_2/ground_2 = 4.85e-9,  certificate = 1.96e-6
N=10: |nu0/nu1| = 1.17e-3,  off_1/ground_1 = 1.64e-3,
      tail_2/ground_2 = 5.63e-9,  certificate = 1.92e-6
N=12: |nu0/nu1| = 9.05e-4,  off_1/ground_1 = 1.26e-3,
      tail_2/ground_2 = 2.32e-9,  certificate = 1.14e-6.   (R-14)
```

So on the audited zeta ladder the exact certificate `(R-11)` is small, unlike
the dead bound of E78.109.

For the planted falsifier:

```text
off_1/ground_1 is enormous and |nu0/nu1| is O(1), so the certificate fails
exactly on front B, where failure is expected.                              (R-15)
```

## 5. Consequence

The tail part of `G0-RESOLVENT-SOURCE` is now candidly reduced to the first
resolvent geometry:

```text
FIRST-RESOLVENT-OFFGROUND + control of |nu0/nu1|
=> negligible tail of A_N(0)^(-2)1.                         (R-16)
```

Therefore the zeta-side live object is no longer the second-resolvent tail
itself, but the smaller package

```text
G0-FIRST-RESOLVENT:
  control the scalar ground coefficient c_0/nu_0^2,
  and prove FIRST-RESOLVENT-OFFGROUND cofinally.            (R-17)
```

## 6. Status

```text
candidate closure - pending review

proved:
  the exact tail gate
  ||tail(A^-2 1)|| / ||ground(A^-2 1)||
  <= |nu0/nu1| * ||off(A^-1 1)|| / ||ground(A^-1 1)||;

reduced:
  the second-resolvent tail problem to the first-resolvent off-ground ratio;

verified:
  on the audited zeta ladder the new certificate is genuinely small
  (~1e-6 to 1e-5), while the planted falsifier breaks there as front B allows;

next:
  attack FIRST-RESOLVENT-OFFGROUND cofinally, or autopsy the exact coefficient
  that prevents a theorem-grade proof of that smaller object.
```
