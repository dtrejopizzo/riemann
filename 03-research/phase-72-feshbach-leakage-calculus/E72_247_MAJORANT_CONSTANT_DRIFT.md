# E72.247 - Majorant constant drift

## Purpose

This note audits the fixed-degree LM8/PTC majorants for dimensional drift.

The concern is:

```text
P_j(0)>0  =>  Tr P_j(K_j/M_j) contains dim * P_j(0).
```

Even a small constant buffer becomes an `O(dim)` contribution.

## Diagnostic

Script:

```text
E72_247_majorant_constant_drift_probe.py
```

Output:

```text
E72.247 majorant constant drift probe
LM8 uses scaled P_j(u) with contribution M_j^2 Tr P_j(K_j/M_j).
Polynomial endpoint data:
  LM8 P0(0)=+3.700346580000e-04 P0'(0)=-2.171401110000e-02
  LM8 P1(0)=+4.227792450000e-04 P1'(0)=-2.423772450000e-02
  PTC P0(0)=+2.322000310000e-04 P0'(0)=-1.873153280000e-02
  PTC P1(0)=+1.969030190000e-04 P1'(0)=-1.493881030000e-02
lam dim exact LM8 slack constCost const/slack linearTerm envNoConst
 12  32 8.980903e-01 9.374141e-01 +3.485920e-03 1.446172e-02 4.149 +2.076168e-03 9.229524e-01
 16  40 7.937823e-01 8.168950e-01 +1.240050e-01 1.807714e-02 0.146 +2.166017e-03 7.988179e-01
 20  48 7.348533e-01 7.540282e-01 +1.868718e-01 2.169257e-02 0.116 +3.373452e-03 7.323357e-01
 24  56 7.403769e-01 7.636295e-01 +1.772705e-01 2.530800e-02 0.143 +7.233055e-03 7.383215e-01
 28  64 6.359406e-01 6.629692e-01 +2.779308e-01 2.892343e-02 0.104 +4.154416e-03 6.340458e-01
 32  72 4.921427e-01 5.263644e-01 +4.145356e-01 3.253886e-02 0.078 +5.924157e-03 4.938255e-01
 36  80 6.476415e-01 6.839368e-01 +2.569632e-01 3.615429e-02 0.141 +4.664467e-03 6.477825e-01
```

## Verdict

The audit confirms the dimensional-drift objection.

At `lambda=12`, the LM8 constant term alone costs:

```text
constCost = 1.446e-2,
LM8 slack = 3.486e-3.
```

Thus the constant term is more than four times the reported margin. More importantly, the constant
cost grows linearly with dimension, so the current fixed-degree LM8 envelope cannot be the final
uniform theorem target.

## Consequence

LM8 remains a useful diagnostic, but the proof-facing majorant must be homogeneous at the origin:

```text
P_j(0)=P_j'(0)=0.
```

The natural replacement is:

```text
P_j(t)=t^2 R_j(t).
```

The next certificate should majorize the split energy using such homogeneous polynomials, preferably
with rational/SOS certificates on the relevant intervals.
