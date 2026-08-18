# E98.005 - Corrected direct boundary target

## 1. Exact theorem

The direct anchor is equivalent to

```text
SENSITIVITY-BOUNDARY-SHELL:
BASE_(L,N)(s;s_*)
 +integral_0^1 {
    INT_(L,N,t)(s;s_*)
   +SHELL_(L,N,t)(s;s_*)
   -[J_L(s)-J_L(s_*)]
  }dt
 ->0.                                                (1.1)
```

## 2. Relation with inherited modules

The decomposition explains the exact role of two inherited targets:

```text
SAFE-BOUNDARY-PAIRING
  controls the internal commutator after the actual determinant sensitivity
  has been inserted;

RDP-SHELL
  controls the two incoming and two outgoing Fourier crossings only after
  the same safe sensitivity pairing.                 (2.1)
```

Neither module is logically required as a separate norm theorem.  Their
coupled scalar sum in (1.1) is the direct object.

## 3. Allocation

The next calculation must insert the explicit incomplete-divisor kernel of
E83.006 into `INT` and preserve `SHELL` until the bilateral base-point
subtraction has been carried out.  Any estimate of the four shell operators
before this pairing loses the determinant cancellation.

## 4. Status

```text
closed:
  exact identification of internal boundary and compression-shell roles;

open:
  SENSITIVITY-BOUNDARY-SHELL.
```

