# E73.275 results - APR coupled-Loewner coborder smoke test

Command:

```text
python3 E73_275_apr_cl_coborder_probe.py
```

## 1. Purpose

Test the first finite proxy for the E73.274 coupled Loewner-principal
primitive module.  The tested modules are:

```text
poly    : span{D^k q_j^*}
dd      : first DD-local module from E73.244
cl      : q_j^*, D^2q_j^*, D^4q_j^*, Hq_j^*, H0q_j^*, Prime q_j^*,
          and D^2 times those action vectors
dd+cl   : combined DD-local plus CL-action proxy
```

For each module the script projects

```text
rho_a=q_aH_L(I-P_w)
```

onto the generated left-coborder rowspace `{Y^*E_L}` and records the residual
geometry.

## 2. Main observation

The scalar pairing is invariant under exact left-coborders:

```text
(rho_a-Proj_Mrho_a)xi_L = rho_axi_L.
```

The output confirms this in the stable windows: `resPairB` remains essentially
equal to `centerB`.  Thus, as expected from E73.256/E73.272/E73.273, adding
the CL-action rows cannot by itself create scalar cancellation.

## 3. Geometry signal

Representative rows:

```text
lam=10, gamma=14.13, row=0
  poly: resNormB=-9.22, cauchyLeakB=-17.85
  dd  : resNormB=-8.32, cauchyLeakB=-15.00
  cl  : resNormB=-9.18, cauchyLeakB=-17.77
  dd+cl: same scale as cl

lam=12, gamma=21.02, row=0
  poly: resNormB=-6.29, cauchyLeakB=-11.93
  dd  : resNormB=-5.61, cauchyLeakB=-9.86
  cl  : resNormB=-6.30, cauchyLeakB=-11.96
  dd+cl: same scale as cl
```

The CL-action proxy is comparable to the polynomial Cauchy module and usually
better than the raw DD-local module on residual norm and Cauchy leakage.  But
it does not turn the residual into an obviously negligible endpoint/Loewner
slot.  The residual row remains much larger than the scalar center.

For `lambda=16`, some `resPairB` values move above `centerB`; this is
consistent with the conditioning warnings from E73.245/E73.256.  Those rows
are diagnostic only.

## 4. Verdict

This first CL-action proxy does not close APR-COB:

```text
rejected: CL-action rows alone as an APR symbolic coborder closure;
kept:     coupled Loewner-principal source-coordinate architecture from E73.274.
```

The next module must encode the balanced second-Abel functional at the
coefficient/source level, not merely add `Hq_j`, `H0q_j`, or prime-action
vectors as primitive columns.

