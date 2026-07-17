# E73.189 results - Cauchy-Dirichlet packet

Command:

```text
python3 E73_189_cauchy_dirichlet_packet_probe.py
```

Output:

```text
E73.189 Cauchy-Dirichlet packet
Checks B_perp(0)=B_perp(L)=0 and the simplified archimedean cell.
 lam     L gamma row qetaB B0B BLB archB matB errB primeB signedB
  12   4.970   14.13   0 -23.41 -22.98 -21.48   -1.51  -1.51 -21.40   -1.51   -20.81
  12   4.970   14.13   1 -24.52 -24.09 -22.05   -2.11  -2.11 -21.16   -2.11   -21.09
  12   4.970   21.02   0 -24.21 -23.77 -22.91   -1.88  -1.88 -22.01   -1.88   -20.40
  12   4.970   21.02   1 -24.86 -24.43 -23.19   -2.72  -2.72 -22.20   -2.72   -19.87
  16   5.545   14.13   0 -21.51 -21.11 -19.72   -4.02  -4.02 -19.62   -4.02   -19.17
  16   5.545   14.13   1 -22.08 -21.68 -20.08   -0.88  -0.88 -20.29   -0.88   -19.91
  16   5.545   21.02   0 -21.87 -21.47 -20.75   -1.91  -1.91 -20.35   -1.91   -18.18
  16   5.545   21.02   1 -22.67 -22.27 -20.37   -0.97  -0.97 -20.31   -0.97   -19.03
  20   5.991   14.13   0 -20.35 -19.96 -19.76   -1.52  -1.52 -17.98   -1.52   -19.16
  20   5.991   14.13   1 -20.30 -19.91 -19.27   -2.05  -2.05 -17.94   -2.05   -18.58
  20   5.991   21.02   0 -21.87 -21.48 -18.91   -0.74  -0.74 -18.28   -0.74   -17.66
  20   5.991   21.02   1 -23.49 -23.10 -19.50   -0.92  -0.92 -18.22   -0.92   -17.78
```

Column meanings:

```text
qetaB   = log_L |q_j eta|
B0B     = log_L |B_j^perp(0)|
BLB     = log_L |B_j^perp(L)|
archB   = simplified Dirichlet archimedean functional
matB    = matrix value q_j H_model eta
errB    = quadrature/matrix error
primeB  = q_j Prime eta
signedB = q_j(H_model-Prime)eta
```

Reading:

```text
q_j eta is zero to numerical precision.
B^perp(0)=2q_j eta is zero to the same scale.
B^perp(L)=0 is also at endpoint floating precision.
The simplified archimedean functional matches q_jH_model eta.
The archimedean and prime transverse cells are still individually ordinary
size; the small signed value is the remaining matching theorem.
```

Conclusion:

```text
TRANS-CELL is now a Dirichlet explicit-formula matching problem:

A_L[B^perp]-P_L[B^perp]=O_R(L^-R),

where B^perp is a finite Weyl packet with B^perp(0)=B^perp(L)=0 and two
Cauchy moment constraints.
```
