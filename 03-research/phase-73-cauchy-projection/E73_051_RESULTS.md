# E73.051 results - FAR top-3 tail

## 1. Purpose

E73.050 rounded the capture as `1.00`.  E73.051 measures the actual WCS tail after selecting the top
three FAR nodes.

## 2. Representative output

```text
E73.051 FAR top-3 tail quantification
 lam     L sigma     tau nK        WCS       tail3     tailFrac  farGammas
  16   5.545  0.20   14.13 12  2.848e-05  1.534e-08  5.388e-04 37.6,30.4,32.9
  18   5.781  0.20   21.02 12  7.160e-06  1.576e-09  2.202e-04 37.6,32.9,30.4
  20   5.991  0.20   14.13 12  1.304e-05  8.883e-12  6.810e-07 32.9,37.6,30.4
  24   6.356  0.20   14.13 12  1.590e-05  2.772e-13  1.743e-08 32.9,30.4,37.6
  24   6.356  0.20   21.02 12  1.726e-05  1.128e-11  6.532e-07 32.9,30.4,37.6
```

## 3. Diagnosis

The FAR top-3 tail is tiny in the tested windows:

```text
tailFrac <= 5.4e-4
```

and improves sharply at larger `L` in the tested range:

```text
about 5e-4 at L=5.545;
about 1e-8 to 1e-6 at L=6.356.
```

The selected FAR nodes stabilize to the critical heights around:

```text
30.4, 32.9, 37.6.
```

## 4. Consequence

The next finite theorem target is:

```text
FAR3-tail:
For the top three FAR nodes D_3(A,L),

sum_{k notin D_3(A,L)}
W_k(A,L)|C_x(i gamma_k)|
<= epsilon_L
sum_k W_k(A,L)|C_x(i gamma_k)|,
```

with an explicit `epsilon_L`, empirically below `6e-4` in the tested windows and decreasing.

Combined with direct certification of the three main nodes, this gives `FAR-DNS`.
