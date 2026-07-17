# E73.264 - Paired alignment audit for Schur residuals

Date: 2026-07-14.

## 1. Purpose

E73.263 proves that the current center is the paired Schur residual

```text
rho^A_{a,w}xi_L-rho^P_{a,w}xi_L,
rho^A_{a,w}=q_aH_L^A(I-P_w),
rho^P_{a,w}=q_aH_L^P(I-P_w).
```

This note asks whether the rapid smallness can be reduced to a row-level
alignment:

```text
rho^A_{a,w} ~= rho^P_{a,w},
```

or whether the cancellation exists only after pairing with the special
eigenline `xi_L`.

## 2. Quantities

The companion script reports:

```text
centerB    = log_L |(rho^A-rho^P)xi_L|;
archB      = log_L |rho^A xi_L|;
primeB     = log_L |rho^P xi_L|;
pairRel    = |(rho^A-rho^P)xi_L| / |rho^A xi_L|;
rowDiffRel = ||rho^A-rho^P|| / max(||rho^A||,||rho^P||);
rowCos     = |<rho^A,rho^P>|/(||rho^A||||rho^P||).
```

If `rowDiffRel` were tiny, the remaining theorem would be a row approximation
problem.  If only `pairRel` is tiny, the theorem must use the eigenline itself.

## 3. Expected reading

The prior E73.263 output already suggested:

```text
rhoNormB is not rapidly small.
```

Thus the likely outcome is:

```text
pairRel tiny,
rowDiffRel not tiny.
```

That would rule out one more easy closure:

```text
prove rho^A ~= rho^P in norm.
```

and retain the sharper eigenline-paired cancellation:

```text
<rho^A-rho^P,xi_L>=O_M(L^-M).
```

## 4. Consequence

If the audit confirms paired-only cancellation, the next theorem cannot be a
Schur row convergence theorem.  It must be an eigenline transport theorem:

```text
xi_L weights the archimedean and prime Schur rows so their pairings agree
to rapid order.
```

This is precisely the `EIG-COEFF` content left by E73.262, now in Schur form.

## 5. Result

The probe confirms the paired-only case:

```text
pairRel    tiny, often 1e-14--1e-10;
rowDiffRel not tiny, reaching 0.605 in the tested range.
```

Therefore the route cannot close through a row approximation
`rho^A ~= rho^P`.  The next theorem must be an eigenline-paired transport
identity:

```text
<rho^A-rho^P,xi_L>=O_M(L^-M).
```

## 6. Status

```text
rejected: row-level arch-prime residual convergence;
confirmed: EIG-COEFF must be genuinely paired with xi_L.
```

