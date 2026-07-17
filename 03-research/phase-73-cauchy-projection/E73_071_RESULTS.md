# E73.071 results - packet Mellin formula verifier

## 1. Purpose

E73.070 derives a closed formula for

```text
M_{B_z^infty}(w)=int_0^L e^(wy)B_z^infty(y)dy.
```

E73.071 verifies the formula numerically by comparing it with direct quadrature of the packet.

## 2. Formula tested

The closed formula is

```text
M_{B_z^infty}(w)
= i H_0(z)
  [ e^(zL)(e^((w-z)L)-1)/(w-z)
    - (e^((w+z)L)-1)/(w+z) ]

- i sum_n xi_n/(z+i d_n)
    (e^((w+i d_n)L)-1)/(w+i d_n)

+ i e^(zL) sum_n xi_n/(z+i d_n)
    (e^((w-i d_n)L)-1)/(w-i d_n).
```

Removable values use the limit

```text
(e^(aL)-1)/a -> L.
```

## 3. Output

```text
E73.071 packet Mellin formula verifier
Compares quadrature of M_B with the closed formula from E73.070.
 lam     L       z        w        absErr      relErr
  16   5.545   14.135 +0.10+3.00i   6.823e-16   6.574e-15
  16   5.545   21.022 -0.10+2.00i   1.686e-16   9.114e-15
  20   5.991   14.135 +0.00+4.00i   2.756e-15   6.557e-14
  24   6.356   21.022 +0.15+1.00i   6.229e-15   8.985e-14
```

## 4. Interpretation

The relative error is at quadrature precision:

```text
relErr <= 9e-14
```

in the tested cases.

Thus the packet Mellin formula in E73.070 is numerically certified in the finite harness.

## 5. Status

```text
verified: closed formula for M_{B_z^infty}(w);
next: use the formula to attack PACKET-ZERO-FAR3 without opening absolute L1 ceilings.
```
