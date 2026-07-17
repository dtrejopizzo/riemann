# E73.086 results - Zloc window-rule probe

## 1. Purpose

E73.084 used the first three critical heights as a proxy for the local zero window.  This can be
misleading because the FAR3 evaluation rows are not the same object as the zero nodes in the paired
packet identity.

E73.086 tests four non-optimized window rules:

```text
prefix    : first n zero nodes;
tau-near  : n zero nodes nearest the off-line cluster height tau;
eval-near : n zero nodes nearest the FAR evaluation row gamma;
far-set   : the FAR3 evaluation rows themselves.
```

The quantity measured is:

```text
sum_{gamma_k in FAR3} W_k(A,L) HWIN_k(window).
```

## 2. Representative output

```text
 lam     L tau rule      nwin     sumB     maxB   worst_gamma   window
  18   5.781   14.13 prefix       3  -11.027  -11.372        37.59 14.13,21.02,25.01
  18   5.781   14.13 tau-near     3  -11.027  -11.372        37.59 14.13,21.02,25.01
  18   5.781   14.13 eval-near    3   -4.135   -4.322        37.59 37.59,32.94,30.42
  18   5.781   14.13 far-set      3   -4.135   -4.322        37.59 37.59,32.94,30.42

  24   6.356   21.02 prefix       3  -14.076  -14.365        32.94 14.13,21.02,25.01
  24   6.356   21.02 tau-near     3  -14.076  -14.365        32.94 21.02,25.01,14.13
  24   6.356   21.02 eval-near    3   -5.452   -5.728        37.59 37.59,32.94,30.42
  24   6.356   21.02 far-set      3   -5.392   -5.728        37.59 32.94,30.42,37.59
```

The exponent `sumB` means `sum = L^sumB`.

## 3. Diagnosis

The local variable `w` in the exact paired divisor identity belongs to the Cauchy block attached to
the off-line cluster height `tau`, not to the FAR3 evaluation height `gamma_k`.

For the tested low clusters:

```text
tau-near, n=3:  L^-10 to L^-14;
eval-near/FAR3: around L^-4 to L^-5 in the worst finite cases.
```

Thus E73.084 was not showing that any small window works.  It was measuring the correct local
cluster window in the tested cases.  The wrong window rule is precisely the one that would identify
`Z_loc` with the dangerous WCS rows; that rule loses the budget.

## 4. Corrected meaning of Zloc

`Z_loc(A,L)` must be defined from the off-line cluster block:

```text
Z_loc(A,L) = the paired critical zero-node window nearest the cluster height interval I_A,
             with multiplicity/confluent data required by the maximal Cauchy block.
```

It is not:

```text
the critical rows selected by FAR3.
```

This matters because FAR3 and local projection solve different problems:

```text
Z_loc: local divisor cancellation in Pair_z(w);
FAR3 : dangerous evaluation rows in the WCS sum.
```

## 5. Consequence

The analytic target survives, but it must be stated in two-window form:

```text
LOCAL-HWIN-5 on Z_loc(A,L)
+ FAR3-WCS on D_3(A,L)
+ outside-window/tail control for critical nodes not in Z_loc
=> BUD-5/9.
```

This avoids the false claim that the FAR3 window itself has the local HWIN margin.

## 6. Status

```text
checked: prefix/tau-near local window has large finite slack;
checked: eval-near/FAR3 window is the wrong object and can lose the L^-5 target;
next: define Z_loc(A,L) canonically from the maximal Cauchy block and prove LOCAL-HWIN-5 for that window.
```
