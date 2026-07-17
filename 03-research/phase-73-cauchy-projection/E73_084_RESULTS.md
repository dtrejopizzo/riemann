# E73.084 results - weighted HWIN probe

## 1. Purpose

E73.084 measures the exact weighted HWIN budget:

```text
Pref_k HWIN_k
```

and compares it with the direct row contribution

```text
Pref_k |H_0(z_k)|.
```

This checks whether `WEIGHTED-HWIN-5` is at the right scale.

## 2. Representative output

```text
E73.084 weighted HWIN probe
Compares Pref*HWIN with direct Pref*|H0(z)| on FAR3 rows.
 lam     L tau nwin   gamma   directB    hwinB  prefHwinB  ratio
  16   5.545   14.13    3   37.59    -7.174  -15.363    -11.146 1.110e-03
  16   5.545   14.13    5   32.94    -6.628   -9.383     -5.781 4.268e+00
  16   5.545   14.13    8   37.59    -7.174   -9.935     -5.718 1.212e+01
  18   5.781   14.13    3   30.42    -6.062  -15.975    -13.695 1.527e-06
  18   5.781   14.13    8   37.59    -6.113   -8.829     -4.322 2.313e+01
  20   5.991   14.13    3   37.59    -6.245  -19.236    -15.190 1.109e-07
  20   5.991   14.13    8   37.59    -6.245   -8.934     -4.888 1.136e+01
  24   6.356   14.13    3   37.59    -6.094  -18.513    -15.594 2.343e-08
  24   6.356   14.13    8   37.59    -6.094   -8.694     -5.774 1.805e+00
```

## 3. Diagnosis

For a local three-node window, the weighted HWIN budget is extremely small:

```text
Pref*HWIN = L^-11 to L^-16.
```

For larger windows, the budget can degrade:

```text
nwin=8 can approach or exceed the L^-5 target in finite data.
```

Thus `WEIGHTED-HWIN-5` is correct as a local finite-window theorem, but not as a blind statement for
arbitrary enlarged critical windows.

## 4. Consequence

The next target must specify the window:

```text
LOCAL-HWIN-5:
WEIGHTED-HWIN-5 on the minimal zero window used by the Cauchy projection block.
```

Large-window contributions should be handled by the already separate tail/outside-window mechanism,
not inserted into the local HWIN main budget.

## 5. Status

```text
observed: local three-node HWIN has large slack;
observed: enlarged windows can be too costly;
corrected target: local HWIN plus outside-window/tail machinery.
```
