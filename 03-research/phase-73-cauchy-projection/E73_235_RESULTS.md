# E73.235 results - APR coefficient collapse

Command:

```text
python3 E73_235_apr_coefficient_collapse_probe.py
```

## 1. Output

```text
E73.235 APR coefficient collapse
Compares principal residual, eta-matrix residual, and coefficient/weight closed center.
 lam      L gamma row aprB etaB coeffB apr-etaB eta-coeffB ||Qeta||B
   8    4.159  14.13   0  -21.68  -21.68   -21.68    -27.40     -26.35    -26.80
   8    4.159  14.13   1  -21.46  -21.46   -21.46    -27.88     -26.31    -26.80
   8    4.159  21.02   0  -15.76  -15.76   -15.76    -28.24     -27.02    -27.38
   8    4.159  21.02   1  -15.79  -15.79   -15.79    -30.10     -27.06    -27.38
  10    4.605  14.13   0  -18.50  -18.50   -18.50    -25.42     -23.41    -26.01
  10    4.605  14.13   1  -18.51  -18.51   -18.51    -25.46     -23.43    -26.01
  10    4.605  21.02   0  -14.98  -14.98   -14.98    -25.64     -23.90    -25.20
  10    4.605  21.02   1  -14.98  -14.98   -14.98    -26.22     -23.86    -25.20
  12    4.970  14.13   0  -20.64  -20.64   -20.62    -24.31     -22.93    -23.58
  12    4.970  14.13   1  -20.35  -20.35   -20.34    -24.55     -23.05    -23.58
  12    4.970  21.02   0  -16.61  -16.61   -16.61    -24.63     -24.25    -24.34
  12    4.970  21.02   1  -16.84  -16.84   -16.84    -24.78     -23.94    -24.34
```

## 2. Interpretation

The three centers agree:

```text
APR principal residual:
qHxi - A(w)Qxi

eta-matrix residual:
qH(I-P)xi

coefficient/weight center:
sum c_omega W_omega + sum l_omega V_omega.
```

The principal-to-eta equality is at the finite rounding level.  The
eta-to-coefficient equality has the same closed-series discrepancy already
measured in E73.220, and remains far below the scalar size in the tested
windows.

The Cauchy annihilation constraint is also visible:

```text
||Qeta|| = L^-23.58 ... L^-27.38.
```

This is the finite numerical version of the exact relation `Q(I-P)xi=0`.

## 3. Consequence

The remaining U4 theorem is now one finite coefficient divisibility statement:

```text
ETA-DIV:
if eta=(I-P_w)xi_L and Q_w eta=0, then

sum_omega c_omega(eta) W_omega
+sum_omega l_omega(eta) V_omega
= O_M(L^-M).
```

No rowspace, pseudoinverse, Cauchy-plane eigen branch, or commutator-norm
statement remains as a separate endpoint.

