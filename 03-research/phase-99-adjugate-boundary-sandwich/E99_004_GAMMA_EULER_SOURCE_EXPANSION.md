# E99.004 - Gamma--Euler source expansion

## 1. Inner operator source

Before Fourier compression,

```text
H_t=H_A-t(A+A^*),
A=Z^(-1)[X,Z].                                       (1.1)
```

The one-sided shift algebra is commutative, so

```text
[Z,A]=0.                                             (1.2)
```

Hence

```text
[Z,H_t]=[Z,H_A]-t[Z,A^*].                            (1.3)
```

Both terms in (1.3) are boundary operators.  The first is the renormalized
archimedean boundary commutator of E83.005; the second is a finite sum of
one-sided/adjoint shift commutators of the form E83.005(2.3).

## 2. Mobius-gauged form

Multiplication of the archimedean part by the inverse Euler unit converts it
to the incomplete-divisor kernel

```text
R_y=M[S_y^*,Z]                                       (2.1)
```

computed exactly in E83.006.  Its left and right formulas contain only
truncated divisor sums and endpoint translations.

## 3. Border sources

The remaining blocks in E99.002,

```text
Zb-b,
h_z-h_zZ,                                            (3.1)
```

are finite Euler translations of the raw boundary column and the safe Cauchy
row.  They must be combined with the operator source before the bilateral
base-point subtraction.

## 4. Compression

Replacing the physical unit by its Fourier compression adds exactly the four
shell crossings of E98.002 and no other term.

## 5. Status

```text
proved or inherited exactly:
  decomposition into archimedean boundary, adjoint Euler boundary, bordered
  row/column and Fourier shell sources;
  normalized characteristic-adjugate commutator as a separate constraint
  term;

open:
  their signed cofactor-sandwich pairing.
```
