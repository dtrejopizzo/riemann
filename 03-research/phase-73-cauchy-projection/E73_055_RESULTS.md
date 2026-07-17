# E73.055 results - FAR3 nodewise rational verifier

## 1. Purpose

E73.055 implements the finite `FAR3-nodewise` certificate:

```text
1. select top three FAR nodes;
2. evaluate each WCS term using C_x=P_x/D_x;
3. split the total into main and tail;
4. verify the rational product evaluation against the direct Cauchy sum.
```

## 2. Computed output

```text
E73.055 FAR3 nodewise rational verifier
Verifies T_k via finite rational C_x=P_x/D_x and FAR3 selection.
 lam     L sigma     tau nK    mainSum    tailSum     total    maxRelRat  mainGammas
  16   5.545  0.20   14.13 12  2.846e-05  1.534e-08 2.848e-05    3.130e-87 30.4,32.9,37.6
  16   5.545  0.20   21.02 12  2.857e-05  4.612e-09 2.858e-05    3.130e-87 30.4,32.9,37.6
  18   5.781  0.20   14.13 12  9.010e-06  5.239e-09 9.016e-06    1.911e-87 30.4,32.9,37.6
  18   5.781  0.20   21.02 12  7.158e-06  1.576e-09 7.160e-06    1.911e-87 30.4,32.9,37.6
  20   5.991  0.20   14.13 12  1.304e-05  8.879e-12 1.304e-05    3.309e-87 30.4,32.9,37.6
  20   5.991  0.20   21.02 12  1.236e-05  7.436e-12 1.236e-05    3.309e-87 30.4,32.9,37.6
  24   6.356  0.20   14.13 12  1.590e-05  2.905e-13 1.590e-05    1.985e-85 30.4,32.9,37.6
  24   6.356  0.20   21.02 12  1.726e-05  1.105e-11 1.726e-05    1.985e-85 30.4,32.9,37.6
```

Reproduce with:

```text
python3 03-research/phase-73-cauchy-projection/E73_055_far3_nodewise_verifier.py
```

## 3. Diagnosis

The rational identity is numerically certified at very high precision:

```text
maxRelRat about 1e-85.
```

The FAR3 main set is stable across the tested windows:

```text
gamma approximately 30.4, 32.9, 37.6.
```

The tail is tiny:

```text
tail/main ranges from about 5e-4 down to about 1e-8.
```

## 4. Status

```text
validated: finite rational FAR3-nodewise certificate in tested windows;
remaining: prove the uniform budget rules for all natural heights.
```
