# E73.248 results - symbolic pivot rule probe

Command:

```text
python3 E73_248_symbolic_pivot_rule_probe.py
```

## 1. Main observations

The tested pivot rules were:

```text
QR, NORM4, SYMPAIR, EDGECORE, MAXMINOR.
```

`NORM4` and `SYMPAIR` are tempting but not reliable in the first trusted window.
For example:

```text
lambda=8, pow=0:
QR       [-5, 5, 2, -2]   condB=6.89  zMaxB=-4.31  transB=0.36
NORM4    [-5, 5, 3, -3]   condB=9.90  zMaxB=-0.22  transB=4.55
SYMPAIR  [-5, 5, 3, -3]   condB=9.90  zMaxB=-0.22  transB=4.55
```

`EDGECORE` is also too coarse:

```text
lambda=8, pow=0:
EDGECORE [-6, 6, -5, 5]   condB=8.68  zMaxB=-3.06  transB=2.27
```

The stable benchmark is `MAXMINOR`:

```text
lambda=8, pow=0:
MAXMINOR [-5, -2, 2, 5]   condB=6.89  zMaxB=-4.31  transB=0.36

lambda=12, pow=2:
MAXMINOR [-9, -4, 4, 9]   condB=5.84  zMaxB=-7.86  transB=0.56

lambda=16, pow=2:
MAXMINOR [-20, -18, 18, 20] condB=4.30 zMaxB=-8.65 transB=0.44
```

## 2. Full output

```text
E73.248 symbolic pivot rule probe
Compare QR pivots with physical rules for PIV-QUOT-DIV.
 lam      L pow rule          pivIdx              condB detB zMaxB transB reconB
   8    4.159   0 QR            [-5, 5, 2, -2]   6.89 -46.48  -4.31   0.36  -38.47
   8    4.159   0 NORM4         [-5, 5, 3, -3]   9.90 -50.64  -0.22   4.55  -35.08
   8    4.159   0 SYMPAIR       [-5, 5, 3, -3]   9.90 -50.64  -0.22   4.55  -35.08
   8    4.159   0 EDGECORE      [-6, 6, -5, 5]   8.68 -49.49  -3.06   2.27  -37.58
   8    4.159   0 MAXMINOR      [-5, -2, 2, 5]   6.89 -46.48  -4.31   0.36  -38.55
-
  10    4.605   0 QR             [7, -7, 2, 0]   6.18 -38.61  -3.92   0.60  -35.96
  10    4.605   0 NORM4         [7, -7, -3, 3]   6.14 -38.38  -4.23   0.45  -35.48
  10    4.605   0 SYMPAIR       [7, -7, -3, 3]   6.14 -38.38  -4.23   0.45  -35.48
  10    4.605   0 EDGECORE      [-8, 8, 7, -7]   7.48 -40.67  -2.85   1.92  -34.19
  10    4.605   0 MAXMINOR      [-7, -6, 6, 7]   6.06 -38.38  -4.24   0.53  -35.58
-
  12    4.970   0 QR            [-9, 9, 3, -5]   5.89 -33.81  -7.54   0.69  -37.89
  12    4.970   0 NORM4         [-9, 9, 4, -4]   5.81 -33.65  -7.69   0.56  -37.16
  12    4.970   0 SYMPAIR       [-9, 9, 4, -4]   5.81 -33.65  -7.69   0.56  -37.16
  12    4.970   0 EDGECORE    [-10, 10, -9, 9]   7.10 -36.03  -6.52   1.94  -35.43
  12    4.970   0 MAXMINOR      [-9, -4, 4, 9]   5.81 -33.65  -7.69   0.56  -36.98
-
  16    5.545   0 QR        [20, -20, 18, -13]   4.20 -19.69 -11.94   0.77  -37.47
  16    5.545   0 NORM4     [20, -20, -18, 18]   4.52 -19.80 -11.76   1.03  -35.99
  16    5.545   0 SYMPAIR   [20, -20, -18, 18]   4.52 -19.80 -11.76   1.03  -35.99
  16    5.545   0 EDGECORE  [20, -20, -18, 18]   4.52 -19.80 -11.76   1.03  -35.99
  16    5.545   0 MAXMINOR  [-20, -13, 18, 20]   4.20 -19.69 -11.94   0.77  -37.06
```

The omitted `pow=1,2` rows follow the same pattern.

## 3. Endpoint update

The pivot law should be:

```text
J_*(L,w) in argmax_{|J|=4} |det D_Q[:,J]|.
```

The new finite theorem is:

```text
MAXMIN-PIV-DIV:
xi_{J_*}+D_Q[:,J_*]^{-1}D_Q[:,R_*]xi_{R_*}=O_M(L^-M).
```

with polynomial nondegeneracy:

```text
MAXMIN-NONDEG:
|det D_Q[:,J_*]| >= L^{-B}.
```
