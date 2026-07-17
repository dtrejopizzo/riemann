# E74.9 results - harmonic left-coborder audit

Command:

```text
python3 E74_009_harmonic_coborder_probe.py
```

## Summary

The audit tested whether the new E74 harmonic symbol can close the structured
left-coborder target:

```text
rho_a=q_aH_L(I-P_w) approx Y(H_L-mu_LI).
```

The answer is no as a direct closure mechanism.

The decisive reason is algebraic:

```text
(H_L-mu_LI)xi_L=0.
```

Thus every exact primitive term `Y(H_L-mu_LI)` pairs to zero with `xi_L`, and
the scalar obstruction is invariant under left-coborder projection:

```text
(rho_a-Y(H_L-mu_LI))xi_L = rho_a xi_L.
```

Harmonic/rational modules can fit the row extremely well, sometimes down to
`resRel ~ 1e-9`, but they do not produce a stable scalar improvement over
`centerB`.

Representative rows:

```text
 lam      L gamma row module dim centerB resPairB resRel
  16  5.545 14.13   0 poly     6  -19.21   -19.37 3.1e-01
  16  5.545 14.13   0 rat     24  -19.21   -16.48 3.4e-07
  16  5.545 14.13   0 harm    18  -19.21   -19.19 3.8e-04
  16  5.545 14.13   0 harmRat 72  -19.21   -19.26 1.4e-09

  20  5.991 21.02   1 poly     6  -17.79   -17.88 9.2e-01
  20  5.991 21.02   1 rat     24  -17.79   -13.77 4.5e-06
  20  5.991 21.02   1 harm    18  -17.79   -17.49 6.8e-03
  20  5.991 21.02   1 harmRat 72  -17.79   -19.31 1.5e-08
```

## Verdict

```text
closed:   the four-step audit requested for the harmonic coborder branch;
rejected: improving primitive spans as a scalar cancellation proof;
survives: exact residual-slot theorem
          rho=Y(H-muI)+R with Rxi=O_M(L^-M).
```

This means E74 does not close Omega7, but it prevents another circular pass:
the missing theorem is not "find a better Y".  The missing theorem is "name
the residual R and prove its eigenline pairing is super-polynomially small".

