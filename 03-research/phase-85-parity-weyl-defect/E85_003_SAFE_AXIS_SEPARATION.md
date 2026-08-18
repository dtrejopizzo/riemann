# E85.003 - Separation of parity responses on the safe axis

## 1. Cauchy transforms of real parity vectors

For a real mesh vector `x`, define

```text
ell_z(x)=sum_j x_j/(z-d_j).                            (1.1)
```

### Lemma 1.1

For `sigma>0`,

```text
ell_{i sigma}(x) is purely imaginary if x is even,
ell_{i sigma}(x) is real if x is odd.                  (1.2)
```

### Proof

Pair the nodes `d` and `-d`.  For an even vector the paired kernel is

```text
1/(i sigma-d)+1/(i sigma+d)
 =-2 i sigma/(sigma^2+d^2),                            (1.3)
```

which is purely imaginary.  For an odd vector it is

```text
1/(i sigma-d)-1/(i sigma+d)
 =-2d/(sigma^2+d^2),                                  (1.4)
```

which is real.  The zero node contributes only in the even case and is also
purely imaginary. `QED`

## 2. No cross-parity cancellation

Write

```text
r_P=r_P^O+r_P^E                                      (2.1)
```

according to (2.2)--(2.3) of E85.002.  Then

```text
ell_{i sigma}(r_P^O) is real,
ell_{i sigma}(r_P^E) is purely imaginary.              (2.2)
```

Consequently

```text
|ell_{i sigma}(r_P)|^2
 =|ell_{i sigma}(r_P^O)|^2
  +|ell_{i sigma}(r_P^E)|^2.                          (2.3)
```

### Corollary 2.1

The safe response tends to zero on an imaginary-axis interval if and only if
both parity responses tend to zero there separately.

There is therefore no admissible proof based on cancellation between the
`alpha` and `beta` terms on the safe axis.

## 3. The two scalar targets

The surviving theorem splits exactly into

```text
PW-E:
alpha sum_{q in Q_odd}L_{i sigma}(q)S_q
      Delta_P^E(lambda_q) -> 0,                       (3.1)

PW-O:
beta sum_{q in Q_even}L_{i sigma}(q)A_q
      Delta_P^O(lambda_q) -> 0,                       (3.2)
```

locally uniformly in safe `sigma`, with their safe derivatives.  Each clause
must retain the signed sum over complementary eigenvalues.

## 4. Status

```text
proved:
  real-imaginary separation of parity Cauchy transforms;
  Pythagorean identity for the full safe response;

closed:
  cross-parity cancellation as a possible mechanism;

open:
  PW-E and PW-O along a cofinal cluster schedule.
```

