# E73.221 - Closed-center stability audit

Date: 2026-07-14.

## 1. Purpose

E73.220 identified that the proof-facing scalar center must be

```text
C_a=A_L^digamma[B_a]-P_L[B_a],
```

not the legacy matrix product `q_aHeta`.  E73.221 checks whether the closed
center itself has a numerical stability problem.

## 2. Test

For every tested window, row, and Cauchy height, compute the same closed center
at

```text
dps=80, 100, 140
```

and compare the lower-precision values to the `dps=140` value.

## 3. Result

The worst observed relative differences are:

```text
dps=80  : 1.4e-67
dps=100 : 1.6e-87
```

In logarithmic `L`-exponents, the `dps=80` center displacement lies around

```text
L^-116 ... L^-132.
```

This is far below the scalar radius budget of E73.219, whose dominant
inflated-sector radii are around

```text
L^-42 ... L^-48.
```

## 4. Consequence

The finite-center computation is numerically stable by an enormous margin.
The proof-facing task is therefore not higher precision; it is an outward
rounding wrapper for the same closed operations:

```text
finite exponentials,
finite prime samples,
digamma/polygamma tail,
coefficient assembly.
```

## 5. Status

```text
verified: closed-center numerical stability is not the bottleneck;
open: replace mp stability by formal outward complex-ball center arithmetic.
```

## 6. Prior-audit distinction

E73.201 showed that double precision can change the finite certificate at the
residual scale.  That was a warning against using the double assembled scalar
as a proof-facing value.

E73.221 asks a different question: once the proof-facing closed formula
`A_L^digamma-P_L` is assembled in multiprecision, is further precision a
limiting issue?  The answer is no in the tested windows.  Thus E73.201 forces
us away from double precision, while E73.221 says the multiprecision closed
center is stable enough to wrap by outward balls.
