# E72.163 -- Fixed-weight two-block PSD certificate

**Date:** 2026-07-09.
**Role:** remove window-dependent weights from `2B-PSD`.

## 0. Fixed certificate

Let:

```text
K_rel=K_0+K_1
```

be the two-block relative arithmetic perturbation with cut:

```text
I_0=[0,0.60L],
I_1=(0.60L,L],
```

and set:

```text
P_0=(K_0)^+,
P_1=(K_1)^+.
```

The fixed-weight certificate is:

```text
||K_rel-0.70P_0-0.60P_1||_HS <= eta < 1.                   (F2B-PSD)
```

Since:

```text
0.70P_0+0.60P_1 >= 0,
```

`(F2B-PSD)` implies `PSD-DIST`.

## 1. Consequence

The current route may be stated as:

```text
GCOER + F2B-PSD + B-scale + Y-scale + OPM + UKERN + ROP + CGE-K
=> scalar WRL resonance annihilation.
```

## 2. Numerical evidence

E72.162 reports that fixed weights work for the midpoint cut.  E72.164 improves the cut and reports:

```text
a=0.70, b=0.60, cut=0.60, maxDist=0.967, margin=0.065
```

over the tested windows `lambda=6,8,10,12,14`.

## 3. Status

```text
proved: F2B-PSD implies PSD-DIST;
observed: fixed weights certify the tested windows;
open:   prove F2B-PSD uniformly.
```
