# E73.261 - Reduced-adjugate certified budget

## 1. Purpose

E73.260 gives the determinant-only form of `ETA-ADJ`, but direct row
determinants become ill-conditioned.  This note connects `ETA-ADJ` to the
finite bordered-Krawczyk/eigenline certificate already built in E73.204--E73.217.

The normalized reduced-adjugate defect is:

```text
||rho Adj_red(E_L)|| / ||Adj_red(E_L)|| = |rho xi_L|.
```

Thus after the eigenline is certified, the radius required for normalized
`ETA-ADJ` is exactly the scalar radius for

```text
rho xi_L = q_aH_L(I-P_w)xi_L.
```

This radius is already computed in E73.219.

## 2. Certificate chain

For each finite window:

```text
BALL-ENTRY-CERT
=> bordered Krawczyk eigenline [xi_L]          (E73.217)
=> Cauchy projection [eta_w]=(I-P_w)[xi_L]    (E73.218)
=> scalar radius for q_aH_Leta_w              (E73.219)
=> normalized ETA-ADJ radius                  (this note).
```

No determinant of a nearly singular matrix has to be evaluated directly in
floating arithmetic.

## 3. Result

The companion script reports:

```text
etaAdjB = log_L |q_aH_Leta_w|,
radB    = certified radius from [H] and [eta_w],
certB   = log_L (|center|+radius).
```

Representative output:

```text
 lam     L    N  dim Csec gamma row etaAdjB radB certB ratio verdict
   8   4.159    6   13    1   14.13   0   -21.68 -57.20  -21.68  1.0e-22 radius-small
   8   4.159    6   13  1e6   21.02   0   -15.76 -47.89  -15.76  1.3e-20 radius-small
  10   4.605    8   17    1   21.02   0   -14.98 -53.49  -14.98  2.9e-26 radius-small
  12   4.970   10   21  1e6   14.13   0   -20.64 -41.92  -20.64  1.5e-15 radius-small
```

Even with the conservative Bernoulli-sector inflation `Csec=1e6`, the certified
radius is far below the center in the tested finite windows.

## 4. What is now closed finitely

For the tested windows and current entry-ball assumptions:

```text
1. the matrix entries are enclosed;
2. the ground eigenline is enclosed by bordered Krawczyk;
3. the Cauchy projection is enclosed;
4. the normalized ETA-ADJ scalar is enclosed with tiny radius.
```

Thus the computational certificate no longer fails at:

```text
eigenline certification,
Cauchy projection,
or adjugate normalization.
```

## 5. What remains mathematical

This does not prove `Omega7`.  It proves that, at finite tested scales, the
value being measured is certified.  The uniform theorem still needed is:

```text
UNIF-ETA:
|q_aH_L(I-P_w)xi_L| <= A_M L^-M
```

for every `M`, uniformly over admissible windows.

Equivalently:

```text
ETA-DIV / ETA-ADJ / ETA-DET
```

must be proved from the explicit Gamma-prime construction, not merely evaluated
with certified arithmetic.

## 6. Status

```text
proved finite certificate chain: BALL-ENTRY => Krawczyk => normalized ETA-ADJ interval;
verified: radius is negligible in tested windows;
open: uniform analytic decay of the certified center.
```

