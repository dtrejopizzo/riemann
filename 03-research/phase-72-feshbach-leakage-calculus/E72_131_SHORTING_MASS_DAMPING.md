# E72.131 -- Shorting mass damping

**Date:** 2026-07-09.
**Role:** turn the remaining mass gain into a spectral estimate for the shorted complement.

## 0. Mass functional

Let:

```text
b_{x,H}:=B_x^*W_H^T1_H.
```

Then the post-main mass is:

```text
Mass_x(H,tau_j)
 = b_{x,H}^*C_E^(-1)c_{x,H}^{pm}(tau_j).
```

E72.130 shows that the raw source mass and complement-projected source mass are only `O(1)`.  The
smallness is introduced by `C_E^(-1)`.

## 1. Damping theorem needed

The natural sufficient estimate is:

```text
||C_E^(-1)b_{x,H}|| <= C_H L^(-1)||b_{x,H}||.               (SMD)
```

If additionally:

```text
||c_{x,H}^{pm}(tau_j)|| <= C_H ||b_{x,H}||^(-1)
```

in the normalized post-main source scale already measured by E72.130, then:

```text
|Mass_x(H,tau_j)| <= C_H/L -> 0.
```

Thus `(SMD)` is a clean spectral form of the mass gain.

Equivalently, the mass vector must lie in a high-energy sector of the shorted complement:

```text
Ray_C(b_{x,H}) := ||b_{x,H}||^2 / <b_{x,H},C_E^(-1)b_{x,H}> >= c_H L.
```

## 2. Diagnostic

The companion script:

```text
E72_131_shorting_mass_damping_probe.py
```

reports:

```text
||C_E^(-1)b||/||b||,
L||C_E^(-1)b||/||b||,
Ray_C(b),
Ray_C(b)/L.
```

Representative output:

```text
E72.131 shorting mass damping probe
 lam   L    dim  ||C^-1b||/||b||  L*gain  rayEig  rayEig/L  minEig  maxEig
   6  3.58     18        2.552e-01 9.144e-01 3.934e+00 1.098e+00 3.76e+00 7.81e+00
   8  4.16     24        1.815e-01 7.548e-01 5.532e+00 1.330e+00 5.38e+00 1.03e+01
  10  4.61     28        1.376e-01 6.339e-01 7.308e+00 1.587e+00 7.05e+00 1.21e+01
  12  4.97     32        1.119e-01 5.562e-01 8.952e+00 1.801e+00 8.78e+00 1.45e+01
  14  5.28     36        9.332e-02 4.926e-01 1.073e+01 2.033e+00 1.05e+01 1.66e+01
  16  5.55     40        7.965e-02 4.417e-01 1.258e+01 2.269e+00 1.23e+01 1.87e+01
```

The damping is stronger than needed: the whole complement has `minEig` growing like `L`, so the mass
vector is not a special lucky direction in these windows.

## 3. Status

```text
reduced: MG to a shorting mass damping estimate SMD plus bounded post-main source size;
observed: Ray_C(b)>=c_HL and even minEig(C_E)>=c_HL in the tested windows;
open:   prove complement coercivity C_E>=c_HLI.
```
