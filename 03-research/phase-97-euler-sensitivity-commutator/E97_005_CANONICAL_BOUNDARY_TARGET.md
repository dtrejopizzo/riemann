# E97.005 - Canonical determinant boundary target

## 1. Identification of the missing vector

E83.007 reduced the Gamma--Euler route to a safe boundary pairing on an
unspecified actual model vector.  The determinant route now specifies the
canonical object: it is the bilateral characteristic-constrained sensitivity

```text
S_t^bil(s;s_*).                                       (1.1)
```

It is constructed from the bordered and full characteristic cofactors and is
therefore independent of any chosen eigenvector normalization.

## 2. Exact target

Define

```text
COMM_t(s;s_*)
 =-Tr([Z,S_t^bil]Z^(-1)X)
  -Tr((Z^*)^(-1)[S_t^bil,Z^*]X).                     (2.1)
```

The remaining theorem is

```text
SAFE-DETERMINANT-BOUNDARY:
BASE_(L,N)(s;s_*)
 +integral_0^1
   {COMM_t(s;s_*)-[J_L(s)-J_L(s_*)]}dt
 ->0                                                  (2.2)
```

locally uniformly along one resolved directed family.

## 3. Relation with earlier boundary kernels

Using E97.004 and the exact shift commutators of E83.005--E83.006, every term
in the bordered part of `COMM_t` can be written as

```text
an incomplete-divisor boundary kernel;
a bordered Cauchy-row correction;
a finite Fourier shell correction.                   (3.1)
```

The characteristic constraint contributes in addition

```text
[Z,adj(H_t-mu_tI)/partial_mu chi].                    (3.2)
```

with its bilateral scalar coefficient.  This term is finite on a simple
branch and may not be replaced by a characteristic inverse.

Unlike the earlier abstract target, (2.2) fixes the sensitivity on which
those operators act.  No global operator-norm estimate is required or
admissible.

## 4. Force-bearing clause

Equation (2.2) is exactly `DIRECT-BORDERED-ANCHOR` in Euler-commutator
coordinates.  The unresolved mathematics is the signed safe pairing of the
explicit boundary kernels with (1.1).

## 5. Status

```text
closed:
  construction of the canonical determinant sensitivity;
  summation of the prime response into an Euler commutator;

open:
  SAFE-DETERMINANT-BOUNDARY, including the normalized characteristic-adjugate
  commutator.
```
