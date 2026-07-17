# E72.356 results - local divisor-ideal probe

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_356_divisor_ideal_probe.py
```

For simple nodes, local membership

```text
Delta(z,w) in (Z(z),Z(w))
```

is equivalent to

```text
Delta(a_i,a_j)=0
```

on every node pair.  The probe evaluates this nodal remainder for the partial CFIR compatibility
minor

```text
Delta(a_i,a_j)
=(S_{a_i}xi)(K_{a_j}xi)-(S_{a_j}xi)(K_{a_i}xi).
```

It also tests a control constructed explicitly as

```text
A(z,w)Z_W(z)+B(z,w)Z_W(w),
```

where `Z_W` is the finite node polynomial.  That control must vanish on the node product.

## Table

```text
lam   N roots node    maxDelta    relDelta    idealCtrlMax
 6.0  10     2 root   2.6209e-32  9.3014e-02   0.0000e+00
 6.0  10     2 shift  5.8818e-01  1.3370e-01   0.0000e+00

 8.0  12     3 root   5.7204e-24  1.3453e-01   0.0000e+00
 8.0  12     3 shift  1.6663e+01  1.4345e-01   0.0000e+00

10.0  14     3 root   4.1911e-24  1.0496e-01   0.0000e+00
10.0  14     3 shift  1.9137e+01  1.6339e-01   0.0000e+00

12.0  16     3 root   1.7934e-28  1.1092e-01   0.0000e+00
12.0  16     3 shift  3.4820e+01  3.8207e-01   0.0000e+00
```

## Reading

The local ideal test is calibrated: the explicitly ideal-generated control vanishes exactly on the
node product.

For finite Weyl-root windows, `maxDelta` is tiny because `K_a xi=G_x(a)` is tiny by construction.
The relative value is not meaningful there because both vectors are near zero.

For shifted controls, the partial residual has large ideal remainder:

```text
maxDelta ~= 5.9e-1, 1.7e1, 1.9e1, 3.5e1.
```

Thus the partial compatibility minor is not in the node-divisor ideal.  This confirms E72.355:
node-blind closure is false.

## Consequence

The next proof-facing object is not another shifted-node fit.  It is an explicit decomposition

```text
Delta_{c,d}^{Xi}(z,w)
= A_{c,d}(z,w)Z(z)+B_{c,d}(z,w)Z(w)+Err_{c,d}(z,w;L)
```

with polynomial `Err`.  That is the first statement which would use the Xi divisor without replacing
Xi-zero nodes by finite Weyl roots.
