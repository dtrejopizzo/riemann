# E73.113 results - possible-set box verifier

## 1. Purpose

E73.112 states the robust possible-set certificate:

```text
P_3(B,L)={rows that can be top-three by interval FAR scores},
sum of the three largest B_k^+ over P_3(B,L) <= 1.
```

E73.113 implements this certificate using the derivative Hermite enclosures from E73.111.

## 2. Output

```text
E73.113 possible-set box verifier
Uses FAR interval possible set P3 and sums the three largest B_k^+ budgets.
 lam     L box                         |P3| possible             worst3              budget status
  16   5.545 [0.15,0.25]x[13.63,14.63]    3 30.4,32.9,37.6       37.6,32.9,30.4       2.049e-01 PASS
  20   5.991 [0.15,0.25]x[13.63,14.63]    4 21.0,30.4,32.9,37.6  37.6,30.4,32.9       1.411e-01 PASS
  20   5.991 [0.15,0.25]x[20.52,21.52]    4 21.0,30.4,32.9,37.6  37.6,30.4,32.9       1.348e-01 PASS
  24   6.356 [0.15,0.25]x[20.52,21.52]    3 30.4,32.9,37.6       37.6,32.9,30.4       2.542e-01 PASS
  28   6.664 [0.15,0.25]x[20.52,21.52]    3 30.4,32.9,37.6       37.6,32.9,30.4       2.050e-01 PASS
```

## 3. Diagnosis

All tested boxes pass:

```text
budget <= 0.255 < 1.
```

In two boxes, the possible set has four rows:

```text
P_3={21.0,30.4,32.9,37.6}.
```

The certificate still passes because it sums the three largest `B_k^+` over the possible set.  Thus
the proof does not require artificial subdivision merely to force a stable selected set.

## 4. Consequence

The box-main gate now has a working verifier:

```text
E73.113:
HERM-BOX derivative enclosures
+ possible-set FAR selection
+ three-largest budget <= 1
=> FAR3-MAIN-RAT on tested boxes.
```

This is the first interval-style verification of the limiting main gate.

## 5. Status

```text
verified: possible-set box certificate passes tested natural boxes;
remaining: integrate this box-main certificate into the unified GATE-73 verifier.
```
