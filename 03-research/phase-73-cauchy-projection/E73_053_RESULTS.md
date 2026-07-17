# E73.053 results - FAR quotient tail audit

## 1. Purpose

E73.053 tests whether the FAR3 tail can be bounded by writing

```text
T_k = F_k Q_k,
Q_k := |C_x(i gamma_k)| / dist(-gamma_k,Div(P_x)),
```

and then using a global tail bound

```text
sum_tail T_k <= (sum_tail F_k) max_tail Q_k.
```

## 2. Result

This global quotient bound fails badly.

Representative output:

```text
E73.053 FAR quotient tail probe
 lam     L sigma     tau nK        WCS     tail3    sumFtail  maxQtail  qBoundTail/tail
  16   5.545  0.20   14.13 12  2.848e-05  1.534e-08  1.261e+03  7.520e-01       6.180e+10
  18   5.781  0.20   21.02 12  7.160e-06  1.576e-09  5.934e+01  4.641e+01       1.747e+12
  20   5.991  0.20   14.13 12  1.304e-05  8.883e-12  2.602e+02  5.095e-01       1.493e+13
  24   6.356  0.20   14.13 12  1.590e-05  2.772e-13  3.077e-13 1.442e+284      1.601e+284
```

## 3. Diagnosis

The quotient

```text
Q_k=|C_x|/dist(-gamma,Div(P_x))
```

can become enormous near a finite Cauchy root.  But those same nodes have tiny FAR score and tiny
actual WCS contribution.  Taking `max Q_k` across the tail destroys the mechanism.

This is the same old lesson in a new coordinate: a global max replaces a structured product by an
incoherent ceiling.

## 4. Consequence

Reject:

```text
FAR3-tail <= sumFtail * maxQtail.
```

Keep:

```text
FAR3-tail = sum_tail W_k |P_x(-gamma_k)/D_x(-gamma_k)|
```

as a nodewise finite rational certificate.

## 5. Status

```text
rejected: global Q-tail bound;
remaining: FAR3-nodewise rational certificate.
```
