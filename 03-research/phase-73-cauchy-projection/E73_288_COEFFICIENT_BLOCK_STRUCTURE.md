# E73.288 - Coefficient block structure

Date: 2026-07-14.

## 1. Purpose

E73.287 gives closed weights for `BLOCK-FREQ-DIV`.  E73.288 derives the exact
structure of the coefficient blocks coming from the finite CCM cells.

The key question is whether `c` and `l` are independent.  They are not.

## 2. Diagonal/off-diagonal split

For

```text
B(y)=q_aQ_yeta
=sum_omega c_omega e^(iomega y)
 +y sum_omega l_omega e^(iomega y),
```

split:

```text
c=c^diag+c^off.
```

The diagonal cells are:

```text
q_nn(y)=2(1-y/L)cos(d_ny).
```

Thus each diagonal contribution gives:

```text
c^diag_{d_n}      += row_n eta_n,
c^diag_{-d_n}     += row_n eta_n,
l_{d_n}           += -row_n eta_n/L,
l_{-d_n}          += -row_n eta_n/L.
```

Therefore the exact identity is:

```text
l_omega = -c^diag_omega/L.                       (DIAG-L)
```

The probe verifies this at roundoff:

```text
diagRel ~ 1e-16.
```

Off-diagonal cells contribute only to `c^off`, not to `l`.

## 3. Refined frequency identity

Starting from:

```text
sum c_omega W'_omega + sum l_omega V'_omega,
```

use `c=c^diag+c^off` and `(DIAG-L)`:

```text
sum c^off_omega W'_omega
+sum c^diag_omega (W'_omega - V'_omega/L).
```

Thus `BLOCK-FREQ-DIV` is equivalent to:

```text
DIAG-OFF-FREQ-DIV:
sum c^off_omega W'_omega
+sum c^diag_omega U'_omega
=O_M(L^(-M)),
```

where

```text
U'_omega := W'_omega - V'_omega/L.
```

This removes the artificial independence of `c` and `l`.  The real
cancellation is between:

```text
1. the off-diagonal sine-difference coefficients paired with W';
2. the diagonal coefficients paired with U'=W'-V'/L.
```

## 4. Numerical diagnostic

The probe reports:

```text
pairDiag = sum c^diag W',
pairOff  = sum c^off W',
pairV    = sum l V',
total    = pairDiag+pairOff+pairV.
```

The total is APR-small while the individual pieces are much larger.  The
exact algebraic compression is:

```text
pairDiag+pairV = sum c^diag(W'-V'/L).
```

This is the next expression to attack with closed weights.

## 5. Updated theorem target

The proof target is now:

```text
DIAG-OFF-FREQ-DIV:
sum_omega c^off_omega W'_omega
= -sum_omega c^diag_omega (W'_omega - V'_omega/L)
   + O_M(L^(-M)).
```

All weights are closed from E73.287.  All coefficient blocks are exact from
the cell formulas.

## 6. Status

```text
proved: l=-c^diag/L exactly;
identified: linear block is diagonal-cell bookkeeping, not an independent
            coefficient source;
refined: BLOCK-FREQ-DIV -> DIAG-OFF-FREQ-DIV;
open: prove the diagonal/off-diagonal closed-weight cancellation.
```
