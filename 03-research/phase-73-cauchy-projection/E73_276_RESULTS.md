# E73.276 results - curvature source adjoint probe

Command:

```text
python3 E73_276_curvature_source_adjoint_probe.py
```

## 1. Purpose

E73.275 showed that adding action-generated primitive rows does not close
APR-COB.  The next proposed move was to build the source in balanced
second-Abel curvature coordinates.  This probe checks what that source is.

For a row `q_a`, form the coefficient maps

```text
B_a(y)=q_aQ_y eta
     =sum c_omega(eta)e^(iomega y)
      +y sum l_omega(eta)e^(iomega y).
```

The adjoint source row of the coefficient/weight functional is

```text
Src_a=sum W_omega u_omega+sum V_omega v_omega,
```

where `c_omega=u_omega eta` and `l_omega=v_omega eta`.

## 2. Result

The source row reconstructed from coefficient weights agrees with `q_aH_L`:

```text
Src_a = q_aH_L
```

at numerical floor.

Representative output:

```text
lam=8, gamma=14.13, row=0:
  srcErrB=-24.63, centerB=-21.68, srcEtaB=-21.68

lam=10, gamma=21.02, row=0:
  srcErrB=-22.45, centerB=-14.98, srcEtaB=-14.98

lam=12, gamma=21.02, row=1:
  srcErrB=-21.14, centerB=-16.84, srcEtaB=-16.84
```

The balanced version gives the same source, because the neutral ramp has
`F_L[r_*]=0`.

## 3. Consequence

The balanced second-Abel curvature source is not a new row:

```text
curvature source row = q_aH_L.
```

After Cauchy principal subtraction, it is exactly the APR row:

```text
q_aH_LR_w = q_aH_L-A_aQ_w.
```

Therefore a source-coordinate construction that merely rewrites the curvature
weights cannot prove APR-U4.  It only reproduces the same principal residual.

The missing proof must do more:

```text
1. split q_aH_LR_w into a fixed symbolic left-coborder plus explicitly named
   residual slots;
2. prove those residual slots pair small with xi_L.
```

## 4. Verdict

```text
proved numerically/algebraically: coefficient curvature adjoint = q_aH_L;
rejected: source-coordinate curvature rewrite as an independent mechanism;
survives: symbolic coborder plus nontrivial residual-slot separation.
```

