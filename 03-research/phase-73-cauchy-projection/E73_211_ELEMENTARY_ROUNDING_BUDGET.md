# E73.211 - Elementary rounding budget

Date: 2026-07-14.

## 1. Purpose

E73.210 shows that the special-function tail can be enclosed well below the
per-entry target.  The remaining entry-radius work is finite elementary
rounding:

```text
R_elem + R_WR_head + R_prime.
```

This note estimates how many decimal digits are needed for those finite sums.

## 2. Audit model

For each matrix entry, compute an absolute work size:

```text
W_entry = sum absolute values of all finite elementary summands
```

over:

```text
1. the two elementary archimedean integrals;
2. the finite WR head up to R=80;
3. the finite prime-power samples.
```

If arithmetic is performed with `p` decimal digits, the audit radius is modeled
as:

```text
R_round <= 10 * (#ops) * W_entry * 10^(-p).
```

The factor `10` is a crude inflation.  The final proof must replace it by
actual outward-rounded ball arithmetic, but this gives a precision target.

## 3. Status

```text
diagnostic: decimal precision budget for finite elementary parts;
not yet: outward-rounded implementation.
```
