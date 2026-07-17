# E73.111 results - HERM-BOX derivative probe

## 1. Purpose

E73.111 replaces the finite-difference Lipschitz enclosure from E73.109 by the analytic derivative
envelope stated in E73.110.

The proof object is:

```text
G(a,k) <= G(center,k)+Lip_cell(G) radius_cell
```

with `Lip_cell(G)` computed from lower bounds for:

```text
|a|, |i gamma-a|, |1/(i gamma-a)+1/(2a)|.
```

## 2. Output

```text
E73.111 HERM-BOX derivative probe
Uses analytic derivative envelopes from E73.110 on subboxes.
 lam     L box                         selected        CmainUp  maxInfl status
  16   5.545 [0.15,0.25]x[13.63,14.63] 37.6,30.4,32.9    2.049e-01    1.026 PASS
  20   5.991 [0.15,0.25]x[20.52,21.52] 37.6,32.9,21.0    1.017e-01   99.728 PASS
  24   6.356 [0.15,0.25]x[20.52,21.52] 32.9,30.4,37.6    2.542e-01    1.040 PASS
  28   6.664 [0.15,0.25]x[20.52,21.52] 37.6,30.4,32.9    2.050e-01    1.040 PASS
```

## 3. Diagnosis

All tested boxes pass:

```text
CmainUp <= 0.255.
```

The analytic derivative envelope is only slightly more conservative than E73.109 on most boxes.

One useful warning appears:

```text
lambda=20, tau box around 21.0:
selected upper-FAR set includes 21.0 with maxInfl ~99.7.
```

This does not break the budget:

```text
CmainUp = 0.1017 < 1.
```

The correct interval certificate should therefore allow competing selected sets when the upper FAR
enclosure is loose.  E73.106 already permits this: certify every possible selected set or subdivide
the box.

## 4. Consequence

The rigorous HERM-BOX route is viable:

```text
analytic derivative HERM-BOX + possible-set certification
=> FAR3-MAIN-RAT on boxes.
```

No budget loss appears; the only issue is selection bookkeeping.

## 5. Status

```text
verified: derivative-envelope HERM-BOX passes tested boxes;
observed: conservative enclosures may add competing rows;
next: formulate possible-set FAR certificate instead of single-set stability.
```
