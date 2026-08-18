# E97.003 - Bilateral commutator current

## 1. Exact substitution

The prime matrix is

```text
H_P=A+A^*.                                            (1.1)
```

Insert `K=S_t^bil(s;s_*)` into E97.002(2.3) and use
E97.001(3.2).  One obtains

```text
BJ_t(s;s_*)
 =-Tr([Z,S_t^bil]Z^(-1)X)
  -Tr((Z^*)^(-1)[S_t^bil,Z^*]X).                     (1.2)
```

Equation (1.2) sums the complete finite von Mangoldt response of Phase 96
before any estimate.

## 2. Projective cancellation

If `S_t^bil` is changed by a matrix commuting with both `Z` and `Z^*`, the
right side of (1.2) is unchanged.  This is the matrix form of the scalar
projective cancellation already seen for determinant factors independent of
the safe variable.

## 3. Euler comparison

The arithmetic defect is now

```text
AJ_t(s;s_*)
 =-Tr([Z,S_t^bil]Z^(-1)X)
  -Tr((Z^*)^(-1)[S_t^bil,Z^*]X)
  -[J_L(s)-J_L(s_*)].                                (3.1)
```

Thus the direct anchor is reduced from a prime sum to one sensitivity
commutator paired with the position derivation.

## 4. Status

```text
proved:
  exact summation of the determinantal prime response;
  exact bilateral sensitivity commutator;

open:
  Gamma--Euler evaluation of (3.1).
```

