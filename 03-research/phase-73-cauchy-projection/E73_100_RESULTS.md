# E73.100 results - unified GATE-73 verifier

## 1. Purpose

E73.099 consolidates the scalar-WRL endpoint as:

```text
GATE-73
= LOCK-COMP-BUD
+ TAIL-LC-BUD
+ OUT-FAR
+ FAR3-MAIN-RAT.
```

E73.100 is the first unified finite verifier for all four gates.

## 2. Targets

The verifier checks:

```text
LOCK <= L^-5,
TAIL <= L^-5,
OUT  <= L^-9,
MAIN <= L^-5.
```

Here `OUT` is the finite FAR complement:

```text
OUT-FAR_fin.
```

The high zero tail `OUT-HIGH` is the analytic theorem E72.394 and is not recomputed numerically.

## 3. Output

```text
E73.100 unified GATE-73 verifier
Targets: LOCK<=L^-5, TAIL<=L^-5, OUT<=L^-9, MAIN<=L^-5.
OUT is the finite FAR complement; OUT-HIGH is the analytic E72.394 tail.
 lam     L tau    M    lockB  tailB    outB   mainB status tags
  16   5.545   14.13   20   -6.685  -8.245 -10.504  -6.111   PASS 14.13:L,21.02:L,25.01:C
  16   5.545   21.02   20   -6.732  -8.292 -11.206  -6.108   PASS 21.02:L,25.01:C,14.13:L
  18   5.781   14.13   22   -6.524  -8.728 -10.867  -6.621   PASS 14.13:L,21.02:L,25.01:C
  18   5.781   21.02   22   -6.531  -8.735 -11.552  -6.752   PASS 21.02:L,25.01:C,14.13:L
  20   5.991   14.13   24   -9.919 -12.449 -14.213  -6.282   PASS 14.13:L,21.02:L,25.01:L
  20   5.991   21.02   24   -9.955 -12.485 -14.314  -6.312   PASS 21.02:L,25.01:L,14.13:L
  24   6.356   14.13   28  -10.043 -12.204 -15.634  -5.974   PASS 14.13:L,21.02:C,25.01:L
  24   6.356   21.02   28  -10.155 -12.317 -13.630  -5.930   PASS 21.02:C,25.01:L,14.13:L
```

## 4. Reading

All four finite gates pass in the tested cases.

The limiting gate is `MAIN`, not the Mellin divisibility, local tail, or outside complement:

```text
worst MAIN = L^-5.930.
```

The local and tail gates have larger slack:

```text
worst LOCK = L^-6.524,
worst TAIL = L^-8.245,
worst OUT  = L^-10.504.
```

## 5. Consequence

The scalar WRL branch is now reduced to a single finite, machine-checkable certificate format:

```text
verify GATE-73(A,L) on each natural-height cluster box.
```

In the finite harness, the certificate is evaluated by:

```text
python3 03-research/phase-73-cauchy-projection/E73_100_gate73_verifier.py
```

## 6. Status

```text
verified: all four finite gates pass in the tested low natural-height boxes;
proved: GATE-73 => scalar WRL by E73.099;
remaining: prove Uniform GATE-73 over all natural-height cluster boxes.
```
