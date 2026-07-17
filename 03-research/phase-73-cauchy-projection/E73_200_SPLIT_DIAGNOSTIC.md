# E73.200 - Archimedean/prime split diagnostic

Date: 2026-07-14.

## 1. Purpose

E73.199 validates the digamma finite-frequency certificate at the final residual
scale, but several rows have relative errors of order one because the target
itself is extremely small.  This diagnostic splits the certificate before the
final cancellation:

```text
F_L[B_a]=A_L[B_a]-P_L[B_a].
```

The goal is to identify whether the discrepancy comes from:

```text
1. the archimedean digamma evaluation;
2. the finite prime-power frequency evaluation;
3. final cancellation between two much larger validated terms.
```

## 2. Tested quantities

For each row, the script compares:

```text
arch_matrix = row H_model eta,
arch_digamma = A_L^digamma[B_a],
prime_matrix = row Prime eta,
prime_freq = P_L[B_a],
final_matrix = row(H_model-Prime)eta,
final_cert = arch_digamma-prime_freq.
```

It also reports the older accelerated WR evaluation error `accelE` from
E73.182/E73.195.

## 3. Status

```text
diagnostic: separates formula error from cancellation floor;
load-bearing: no, this is an audit of E73.199 before intervalization.
```
