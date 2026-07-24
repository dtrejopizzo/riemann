# E78.62 - The real normalized ternary cocycle is a single coupled pairing over a positive denominator

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.61 localized the live scalar burden to

```text
REAL-NORMALIZED-TERNARY-CANCEL:
  Re(-(A_N+B_N+C_N)/(1-theta_N)).                        (RCP-1)
```

That object is still exact, but it is written as a complex quotient. This note
removes the quotient from the sign problem and rewrites the live scalar as a
single real coupled pairing over a manifestly positive denominator.

## 2. Exact coupled-pairing identity

Let

```text
T_N := A_N + B_N + C_N,
d_N := 1-theta_N.                                        (RCP-2)
```

Then E78.60-E78.61 say

```text
Re(w_N) = Re(-T_N/d_N).                                  (RCP-3)
```

Multiply numerator and denominator by `conj(d_N)`:

```text
-T_N/d_N = -(T_N conj(d_N)) / |d_N|^2.                  (RCP-4)
```

Taking real parts yields the exact identity

```text
Re(w_N)
 = -Re(T_N conj(d_N)) / |d_N|^2
 = -Re((A_N+B_N+C_N) conj(1-theta_N)) / |1-theta_N|^2.  (RCP-5)
```

Since `|1-theta_N|^2 > 0`, the sign of `Re(w_N)` is controlled exactly by the
single real numerator

```text
PAIRNUM_N := -Re((A_N+B_N+C_N) conj(1-theta_N)).         (RCP-6)
```

So the E78.50 core sign is equivalent to the sign of one coupled Hermitian
pairing numerator, not to the sign of a complex quotient.

## 3. Consequence for the denominator core

Substituting `(RCP-5)` into E78.50 gives

```text
2 PAIRNUM_N / |1-theta_N|^2 + |w_N|^2 < 0.               (RCP-7)
```

In particular, the inward branch from E78.57 becomes

```text
Re(w_N) < 0
<=> PAIRNUM_N < 0.                                       (RCP-8)
```

Thus the denominator fixed point from E78.58 and the real ternary target from
E78.61 both reduce to a single real coupled numerator over a positive scalar
denominator.

This is a legitimate reduction: it does not solve the ternary coupling, but it
does remove one layer of quotient geometry from the sign problem.

## 4. Audit

The identity

```text
Re(-(A_N+B_N+C_N)/(1-theta_N))
 = -Re((A_N+B_N+C_N) conj(1-theta_N)) / |1-theta_N|^2   (RCP-9)
```

was audited on the same common certified ladder as E78.61.

Max reconstruction errors:

```text
zeta:   1.57e-12,
plant:  2.22e-16.                                        (RCP-10)
```

So the reduction is exact to roundoff in both builds.

## 5. Honest reading

This note does not prove the required sign of `PAIRNUM_N`. The ternary burden is
still there, now concentrated in one real coupled functional.

But it is still a useful reduction:

```text
REAL-NORMALIZED-TERNARY-CANCEL
=> PAIRNUM-SIGN,
```

where

```text
PAIRNUM-SIGN:
  control the sign/cancellation of
  -Re((A_N+B_N+C_N) conj(1-theta_N)).                    (RCP-11)
```

That is a cleaner endpoint for any future finite cell/Loewner argument, because
the denominator is now harmless and positive.

## 6. Status

```text
proved:
  the live real scalar Re(-(A_N+B_N+C_N)/(1-theta_N)) equals a single coupled
  real pairing numerator divided by |1-theta_N|^2;

proved:
  the inward-branch sign Re(w_N)<0 is exactly the sign of
  PAIRNUM_N = -Re((A_N+B_N+C_N) conj(1-theta_N));

reduced:
  the denominator/IDENT sign burden from a complex normalized cocycle to the
  real coupled target PAIRNUM-SIGN;

next:
  expand or identify PAIRNUM_N as a single finite cell/Loewner pairing law
  without splitting it into absolute term bounds.
```
