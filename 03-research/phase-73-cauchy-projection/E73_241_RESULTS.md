# E73.241 results - curvature source row audit

Command:

```text
python3 E73_241_curvature_source_row_audit.py
```

## 1. Output

```text
E73.241 curvature source row audit
Compares coefficient/weight source row with qH, and residual modulo Cauchy plane.
 lam      L gamma row srcEtaB qHEtaB src-qHB rhoEtaB trivialCobB
   8    4.159  14.13   0   -21.68  -21.68   -26.41   -21.68      -28.21
   8    4.159  14.13   1   -21.46  -21.46   -26.37   -21.46      -28.29
   8    4.159  21.02   0   -15.76  -15.76   -27.04   -15.76      -28.54
   8    4.159  21.02   1   -15.79  -15.79   -27.10   -15.79      -28.55
  10    4.605  14.13   0   -18.50  -18.50   -23.41   -18.50      -25.66
  10    4.605  14.13   1   -18.51  -18.51   -23.42   -18.51      -26.37
  10    4.605  21.02   0   -14.98  -14.98   -23.96   -14.98      -26.87
  10    4.605  21.02   1   -14.98  -14.98   -23.96   -14.98      -27.55
  12    4.970  14.13   0   -20.62  -20.64   -22.81   -20.64      -24.62
  12    4.970  14.13   1   -20.34  -20.35   -22.90   -20.34      -24.42
  12    4.970  21.02   0   -16.61  -16.61   -24.26   -16.61      -25.16
  12    4.970  21.02   1   -16.84  -16.84   -24.17   -16.84      -25.03
  16    5.545  14.13   0   -18.90  -19.11   -19.38   -19.21      -20.53
  16    5.545  14.13   1   -19.82  -19.84   -19.46   -20.02      -20.71
  16    5.545  21.02   0   -18.20  -18.18   -20.30   -18.18      -21.72
  16    5.545  21.02   1   -19.10  -19.04   -20.40   -19.04      -21.78
```

## 2. Interpretation

The coefficient/weight source row satisfies, on `eta`,

```text
Src_{a,w} eta = q_aH_L eta
```

to the finite assembly precision already seen in E73.220/E73.235.

Since `eta=(I-P)xi`,

```text
q_aH_L eta = q_aH_L(I-P)xi = rho_a xi.
```

So the curvature source is not a new independent source.  It is `q_aH_L`
modulo the Cauchy plane.

The trivial identity

```text
q_aH_L eta = q_aE eta
```

also holds because `q_a eta=0`, but it is not a proof-facing coborder:
`E` acts on `eta`, not on the eigenline `xi`.  Using it returns to the
circular branch `E eta=-EPxi`.

## 3. Consequence

`CURV-COB` must target the transverse residual row:

```text
rho_a=q_aH_L(I-P_w),
```

not the full row `q_aH_L` and not the trivial primitive `q_a^*`.

The valid theorem is:

```text
rho_a = Y_{a,w}^*E + endpoint residual
```

with `Y_{a,w}` in a fixed symbolic primitive module and the endpoint residual
pairing rapidly small.

