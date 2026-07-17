# E73.050 results - FAR-DNS window stress

## 1. Purpose

E73.050 tests whether the `FAR-DNS` selector remains stable when the critical window grows.

The tested selector is:

```text
F_k(A,L)=
e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|
dist(-gamma_k,Div(P_x)).
```

The dominant set is the top `r` nodes by `F_k`.

## 2. Result

For the tested high windows and `ncrit=6,8,10,12`, the top three FAR nodes capture essentially all
of the WCS mass.

Representative output:

```text
E73.050 FAR-DNS window stress
 lam     L sigma     tau  m nK      WCS  far3 far5 far8 post3 r90 r95 r99
  16   5.545  0.20   14.13  3 12 2.85e-05  1.00  1.00  1.00  1.00   3   3   3
  18   5.781  0.20   21.02  3 12 7.16e-06  1.00  1.00  1.00  1.00   3   3   3
  20   5.991  0.20   14.13  3 12 1.30e-05  1.00  1.00  1.00  1.00   3   3   3
  24   6.356  0.20   21.02  3 12 1.73e-05  1.00  1.00  1.00  1.00   3   3   3
```

## 3. Diagnosis

The evidence supports:

```text
r=3 for the tested natural-height windows.
```

Unlike geometry-only DNS, FAR-DNS does not degrade when the critical window is enlarged from six to
twelve nodes.

## 4. Status

```text
supported: top-3 FAR selector;
remaining: quantify the actual FAR-tail and turn it into a finite certificate.
```
