# E73.105 results - weighted FAR-SLOPE budgets

## 1. Purpose

E73.104 showed that the max-slope split is too crude.  The correct certificate is the weighted
three-row budget:

```text
sum_{gamma_k in D_3(A,L)} FAR_k Q_k <= C_main L^-5.
```

E73.105 measures the exact finite budgets:

```text
b_k:=L^5 FAR_k Q_k = L^5 T_k,
C_main:=sum_{D_3} b_k.
```

## 2. Output

```text
E73.105 weighted FAR-SLOPE budget probe
Reports node budgets b_k=L^5 FAR_k Q_k and total C_main=sum b_k.
 lam     L tau       Cmain   maxb  gamma:b list
  16   5.545   14.13   1.492e-01 9.438e-02 37.6:9.438e-02,30.4:3.586e-04,32.9:5.450e-02
  18   5.781   21.02   4.621e-02 2.974e-02 37.6:1.275e-02,32.9:3.719e-03,30.4:2.974e-02
  24   6.356   21.02   1.791e-01 1.769e-01 32.9:2.071e-03,30.4:1.335e-04,37.6:1.769e-01
  28   6.664   21.02   1.421e-01 1.385e-01 37.6:1.385e-01,30.4:1.866e-06,32.9:3.586e-03
  32   6.931   21.02   6.337e-03 6.337e-03 37.6:6.337e-03,32.9:7.304e-07,25.0:1.205e-08
```

## 3. Diagnosis

The measured constant:

```text
C_main=L^5 sum_{D_3}T_k
```

stays below:

```text
0.18
```

in the tested range.  A certificate with:

```text
C_main=1
```

has large finite slack.

The dominant budget is usually carried by:

```text
gamma ~= 37.6.
```

but the FAR selector can replace one weak row with `25.0` at `lambda=32`; the weighted budget remains
small.

## 4. Consequence

The interval certificate should not try to prove a universal bound on each individual row with a
tight fixed identity.  It should prove:

```text
sum_{selected rows} L^5 FAR_k Q_k <= 1
```

on each cluster box, with the selected FAR order fixed or certified by interval separation.

## 5. Status

```text
observed: C_main=1 is a plausible finite certificate constant;
observed: weighted budget survives selector changes;
next: formulate interval FAR-SLOPE box certificate.
```
