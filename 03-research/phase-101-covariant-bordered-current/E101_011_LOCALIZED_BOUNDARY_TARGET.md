# E101.011 - Localized boundary target

## 1. Projective defect

Let

```text
DEF_alpha(s;s_*)
 =BASE_alpha(s;s_*)
  +integral_0^1 RES_(alpha,t)(s;s_*)dt,              (1.1)
```

where `RES` is the complete covariant boundary residual of E101.009.  The
finite deformation identity gives

```text
exp(DEF_alpha(s;s_*))=R_alpha(s;s_*),                (1.2)
```

the direct bordered ratio divided by the independent Euler--Gamma ratio.

## 2. Local identification target

Fix one open interval

```text
I compactly contained in (1,infinity)                (2.1)
```

on the real `s` axis.  The arithmetic identification hypothesis can be
reduced to

```text
LOCAL-COVARIANT-IDENT:
DEF_alpha(s;s_*)->0                                  (2.2)
```

locally uniformly for `s in I`, with `s_* in I`.

No assertion about the current outside `I` is part of (2.2).

## 3. Compactness recovered from the same interval

Earlier coordinates separated the auxiliary condition

```text
SAFE-COFINAL-BOUND:
sup_alpha Theta_alpha(s)<infinity
for every s in U.                                    (3.1)
```

E101.018--E101.019 make this separate hypothesis unnecessary.  Choose two
points inside `I`.  Local identification bounds the ratio at the second point,
which bounds the complete Stieltjes mass and hence the family on every compact
set.  Therefore

```text
LOCAL-COVARIANT-IDENT
 => SR-SAFE
 => Omega7.                                          (3.2)
```

## 4. Allocation of difficulty

The exact finite identities of E101.001--E101.009 reduce (2.2) to the signed
boundary evaluation

```text
BASE_alpha
 +integral_0^1 {
    COVBOUND_(alpha,t)
   +SHELL_(alpha,t)
   -EULER_alpha
  }dt
 ->0                                                 (4.1)
```

only on `I`.  In contrast, (3.1) is a one-sided magnitude bound at an
unbounded collection of points and does not identify the limit.

This proves the precise version of the infrastructure/discriminant split:

```text
compactness is automatic from two points in I;
the new arithmetic identity is needed only on I.     (4.2)
```

## 5. Warning

The reduction of the domain does not weaken the logical force of (2.2).
Together with (3.1), it still implies `Omega7`.  Consequently any proof of
`LOCAL-COVARIANT-IDENT` under the compactness input must contain the
RH-strength step or an error.

## 6. Status

```text
closed:
  localization of the arithmetic boundary target to one safe interval;
  recovery of compactness from the same interval;

open:
  LOCAL-COVARIANT-IDENT;
  Omega7.
```
