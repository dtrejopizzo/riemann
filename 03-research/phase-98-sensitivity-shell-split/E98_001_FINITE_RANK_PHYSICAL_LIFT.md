# E98.001 - Finite-rank physical lift

## 1. Fourier projection

Let `P_N` be the Fourier projection onto the finite CCM modes in
`L^2(0,L)` and set

```text
Q_N=I-P_N.                                           (1.1)
```

The finite bilateral sensitivity of E97.001 is lifted to the physical module
by

```text
K_N=P_NK_NP_N.                                       (1.2)
```

It is finite rank.

## 2. Trace compatibility

Let `A=Z^{-1}[X,Z]` be the uncompressed Euler connection.  The finite prime
matrix is the Fourier compression

```text
H_(P,N)=P_N(A+A^*)P_N.                               (2.1)
```

Since `K_N=P_NK_NP_N`,

```text
Tr_N[K_N H_(P,N)]
 =Tr_[L2][K_N(A+A^*)].                               (2.2)
```

The physical trace is well defined because `K_N` is finite rank and all other
operators in (2.2) are bounded at fixed `L`.

## 3. Consequence

The Euler trace identity of E97.002 applies before Fourier compression.  No
inverse of the compressed Euler unit and no false compressed semigroup law is
introduced.

## 4. Status

```text
proved:
  exact compatibility of finite and physical trace pairings;
  admissibility of applying the Euler identity before compression.
```

