# E73.237 results - balanced coefficient second-Abel bridge

Command:

```text
python3 E73_237_balanced_coefficient_probe.py
```

## 1. Output

```text
E73.237 balanced coefficient second-Abel bridge
Checks derivative moment, rank-one source, and neutral balanced ramp.
 lam      L gamma row BpCoeffB BpRankB diffB FstarB FdiffB bal0B balp0B balLB
  12    4.970  14.13   0   -10.41  -10.41  -22.53 -430.82 -430.82  -22.88  -430.82  -21.50
  12    4.970  14.13   1   -10.41  -10.41  -23.52 -430.82 -430.82  -24.39  -430.82  -22.06
  12    4.970  21.02   0   -10.59  -10.59  -22.31 -430.82 -430.82  -23.56  -430.82  -22.85
  12    4.970  21.02   1   -10.59  -10.59  -21.85 -430.82 -430.82  -24.72  -430.82  -23.65
  16    5.545  14.13   0    -9.78   -9.78  -20.35 -403.27 -403.27  -21.11  -403.27  -19.75
  16    5.545  14.13   1    -9.78   -9.78  -20.47 -403.27 -403.27  -22.04  -403.27  -20.08
  16    5.545  21.02   0    -9.55   -9.55  -20.60 -403.27 -403.27  -21.60  -403.27  -20.85
  16    5.545  21.02   1    -9.55   -9.55  -20.62 -403.27 -403.27  -22.70  -403.27  -20.36
  20    5.991  14.13   0   -11.10  -11.10  -20.50 -385.84 -385.84  -20.68  -385.84  -19.87
  20    5.991  14.13   1   -11.10  -11.10  -18.49 -385.84 -385.84  -20.08  -385.84  -19.18
  20    5.991  21.02   0    -9.54   -9.54  -18.96 -385.84 -385.84  -21.12  -385.84  -18.91
  20    5.991  21.02   1    -9.54   -9.54  -18.90 -385.84 -385.84  -21.65  -385.84  -19.50
```

## 2. Interpretation

The derivative moment identity is verified:

```text
B'(0)=sum iomega c_omega+sum l_omega
     =-(2/L)(sum q_a)(sum eta).
```

The balanced ramp is neutral:

```text
F_L[r_*]=0
```

to the arithmetic floor of the computation.  Therefore subtracting
`B'(0)r_*` does not change the scalar center.

The balanced packet constraints are also certified:

```text
B^bal(0)=0,
(B^bal)'(0)=0,
B^bal(L)=0.
```

The derivative is symbolic in the probe, hence it lands at the exact zero
floor.

## 3. Consequence

ETA-DIV is now equivalent to the proof-facing finite identity:

```text
BSA-DIV:
int_0^L K_L(t)(B^bal)''(t)dt = O_M(L^-M),
```

with `(B^bal)''` given explicitly by finite coefficients and the balanced
ramp curvature.  This avoids the unstable nested quadrature of E73.194 as a
proof object; the quadrature identity is analytic, while the finite
certificate should use the coefficient curvature formula.

