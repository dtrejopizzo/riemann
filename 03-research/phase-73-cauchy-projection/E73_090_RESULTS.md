# E73.090 results - LOCK/COMP budget

## 1. Purpose

E73.089 proves that `LOCAL-HWIN-5` follows from a root-locked nodal budget plus a fixed companion
residual budget.

E73.090 measures the actual sufficient quantity:

```text
4(1+e^(sigma L))/sigma
* (sum_{gamma_k in FAR3} W_k)
* (N_lock+N_comp),
```

and compares it with the exact local HWIN budget.

## 2. Output

```text
E73.090 LOCK/COMP budget probe
Compares exact LOCAL-HWIN with the Theorem 89.3 sufficient budget.
 lock cutoff: dist <= L^-8; paired +/- contribution included
 lam     L tau      SFARB   NlockB   NcompB  suffB  exactB  ratio tags
  16   5.545   14.13    4.629  -18.590  -13.876  -6.685 -10.557 7.60e+02 14.13:L,21.02:L,25.01:C
  16   5.545   21.02    4.581  -18.590  -13.876  -6.732 -10.640 8.07e+02 21.02:L,25.01:C,14.13:L
  18   5.781   14.13    4.823  -16.329  -13.877  -6.524 -11.027 2.70e+03 14.13:L,21.02:L,25.01:C
  18   5.781   21.02    4.816  -16.329  -13.877  -6.531 -11.037 2.71e+03 21.02:L,25.01:C,14.13:L
  20   5.991   14.13    4.618  -17.026     -inf  -9.919 -14.506 3.68e+03 14.13:L,21.02:L,25.01:L
  20   5.991   21.02    4.582  -17.026     -inf  -9.955 -14.551 3.75e+03 21.02:L,25.01:L,14.13:L
  24   6.356   14.13    4.491  -16.997  -18.705 -10.043 -13.962 1.41e+03 14.13:L,21.02:C,25.01:L
  24   6.356   21.02    4.378  -16.997  -18.705 -10.155 -14.076 1.41e+03 21.02:C,25.01:L,14.13:L
```

Exponents are powers of `L`.  Thus `suffB=-6.5` means the sufficient budget is `L^-6.5`.

## 3. Interpretation

Even with the crude universal coefficient bound:

```text
|A_L(z,w)|+|B_L(z,w)| <= 4(1+e^(sigma L))/sigma,
```

the sufficient LOCK/COMP budget is below `L^-5` in every tested case:

```text
worst tested suffB = -6.524.
```

The exact local HWIN is much smaller:

```text
exactB = -10.557 to -14.551.
```

The ratio between sufficient and exact budgets is large because the coefficient bound discards phase
and height separation.  This is acceptable for a sufficient theorem: no cancellation is being used in
the final inequality.

## 4. Structural split

The tags show the split:

```text
L = root-locked node;
C = companion residual node.
```

For low `L`, the third local node may be companion.  At larger tested `L`, it can become root-locked.
Thus the correct theorem is not "all nodes root-lock"; it is:

```text
root-lock where finite roots are close;
direct companion residual elsewhere.
```

## 5. Consequence

The local HWIN budget now has a finite sufficient certificate:

```text
LOCK-COMP-BUD:
4(1+e^(sigma L))/sigma
* S_FAR(A,L)
* (N_lock(A,L)+N_comp(A,L))
<= C L^-5.
```

Together with E73.089:

```text
LOCK-COMP-BUD => LOCAL-HWIN-5.
```

## 6. Status

```text
proved: LOCK/COMP budget is sufficient for LOCAL-HWIN-5;
verified: finite harness satisfies the budget with slack;
open: prove LOCK-COMP-BUD uniformly from the finite divisor geometry.
```
