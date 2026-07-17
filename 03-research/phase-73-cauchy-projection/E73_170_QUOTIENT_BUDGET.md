# E73.170 - Quotient budget

Date: 2026-07-14.

## 1. Purpose

E73.169 leaves the endpoint as a three-dimensional quotient pairing:

```text
QUOT-PAIR:
e^(alpha L)|<Pi_Q(A),G_Q>| <= L^B.
```

This note tests whether the stronger Cauchy-Schwarz sufficient condition is
reasonable:

```text
QUOT-NORM:
e^(alpha L)||Pi_Q(A)|| ||G_Q|| <= L^B.
```

If `QUOT-NORM` loses many powers of `L`, the exact pairing must be kept.  If
the loss is polynomial and modest, `QUOT-NORM` becomes a clean finite target.

## 2. Quantities

For each off-line row `A`:

```text
Pi_Q(A) = P_Q Pi_A,
G_Q     = P_Q G_K,
pair    = e^(alpha L)|<Pi_Q(A),G_Q>|,
norm    = e^(alpha L)||Pi_Q(A)|| ||G_Q||,
loss    = norm/pair.
```

The table reports logarithmic exponents in base `L`:

```text
piQB   = log_L ||Pi_Q(A)||,
gQB    = log_L ||G_Q||,
normB  = log_L norm,
pairB  = log_L pair,
lossB  = log_L loss.
```

## 3. Result

In trusted windows:

```text
lossB is typically between 0.1 and 1.6,
```

with no sign of exponential loss.

Thus Cauchy-Schwarz in the quotient loses only a modest polynomial factor in
the diagnostic rows.  This makes `QUOT-NORM` a reasonable sufficient theorem.

## 4. Where the budget lives

For the large rows, `||Pi_Q(A)||` is usually of polynomial size:

```text
piQB about -1 to 0.2
```

for the non-tiny off-line rows.

The decisive scale is therefore `||G_Q||`:

```text
gQB ranges roughly from -14 to -10 in the trusted rows.
```

The off-line exponential weight `e^(alpha L)` is already included in
`normB`.  The tested norm budget remains strongly negative:

```text
normB about -14 to -10
```

on the large rows in the trusted range.

## 5. Updated theorem

The current sufficient finite theorem is:

```text
QUOT-NORM:
There exist B,L0 such that for every L>=L0 and every natural-height off-line
Hermite cluster A,

e^(alpha L)||P_Q,L Pi_A|| ||P_Q,L G_K|| <= L^B.
```

This implies:

```text
QUOT-NORM
=> QUOT-PAIR
=> DATA-HERM / NAT-SRC
=> NAT-PROJ
=> scalar WRL
=> Omega7.
```

## 6. What remains

The quotient geometry has separated the remaining proof into two explicit
finite bounds:

```text
QPI:
e^(alpha L)||P_Q,L Pi_A|| <= L^B,

QG:
||P_Q,L G_K|| <= L^B e^(-alpha L).
```

The diagnostics suggest `QPI` is geometric and polynomial, while `QG` is the
true arithmetic/spectral divisibility statement.

This is the sharpest current split:

```text
finite quotient geometry + quotient spectral Cauchy smallness.
```

## 7. Status

```text
kept:      quotient dimension 3;
kept:      Cauchy-Schwarz quotient norm route;
open:      prove QPI and QG uniformly, or prove QUOT-PAIR directly.
```

