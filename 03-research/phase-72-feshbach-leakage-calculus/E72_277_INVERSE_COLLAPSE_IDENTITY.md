# E72.277 -- Inverse-collapse identity

**Purpose.** Remove the opaque Feshbach inverse from the gauged compact-root target as far as possible.

After E72.275--E72.276 the compact-root residual is

```text
R_x(s,tau_j)
= i alpha(tau_j)<a_s^perp,C_E^(-1)S_tau_j xi_x>,
```

where

```text
S_tau=2tau(tau^2I-D^2)^(-1).
```

Let

```text
C_E xi_x = mu_x xi_x.
```

Since `xi_x` is the actual even ground vector in the corrected pole-even complement, this is exact.

## Exact identity

For any operator `S`,

```text
C_E S xi_x = mu_x S xi_x + [C_E,S]xi_x.
```

Thus

```text
S xi_x = mu_x^(-1) C_E S xi_x - mu_x^(-1)[C_E,S]xi_x.
```

Applying `C_E^(-1)` and pairing with `a_s^perp` gives the exact identity

```text
<a_s^perp,C_E^(-1)S xi_x>
= mu_x^(-1)<a_s^perp,S xi_x>
 - mu_x^(-1)<a_s^perp,C_E^(-1)[C_E,S]xi_x>.                  (IC)
```

For `S=S_tau_j`, the HPAC residual splits into:

```text
R_x(s,tau_j)
= D_x(s,tau_j) + K_x(s,tau_j),
```

with

```text
D_x = i alpha(tau_j)mu_x^(-1)<a_s^perp,S_tau_j xi_x>,
K_x = -i alpha(tau_j)mu_x^(-1)
      <a_s^perp,C_E^(-1)[C_E,S_tau_j]xi_x>.
```

This is an exact algebraic identity.  No root tracking or zero input is used.

## Probe

Run:

```text
python3 E72_277_inverse_collapse_probe.py
```

Output:

```text
E72.277 inverse-collapse probe
Exact identity: <a,C^-1 Sxi> = mu^-1<a,Sxi> - mu^-1<a,C^-1[C,S]xi>.
Residual includes the factor i alpha(tau).
lam L roots mu maxR maxDiag maxComm maxRel
 16 5.545177     7 1.232544e+01 2.571511e-02 2.571511e-02 4.979407e-14 4.124e-15
 20 5.991465     7 1.596102e+01 1.494883e-02 1.494883e-02 2.298793e-15 3.997e-15
 24 6.356108     5 1.965549e+01 6.308598e-03 6.308598e-03 9.857540e-18 2.527e-15
 28 6.664409     6 2.339219e+01 4.104033e-03 4.104033e-03 8.302836e-17 1.383e-09
 32 6.931472     8 2.716069e+01 2.102367e-03 2.102367e-03 1.824160e-15 4.281e-04
```

## Reading

The compact-root residual is, in the tested windows, completely carried by the diagonal term

```text
i alpha(tau_j)mu_x^(-1)<a_s^perp,S_tau_j xi_x>.
```

The commutator correction is numerically invisible.  Therefore the proof-facing target should be
split as:

```text
1. Diagonal Cauchy-resolvent orthogonality:
   sup |mu_x^(-1)<a_s^perp,S_tau_j xi_x>| -> 0.

2. Commutator invisibility:
   sup |mu_x^(-1)<a_s^perp,C_E^(-1)[C_E,S_tau_j]xi_x>| -> 0.
```

This is strictly sharper than trying to control `C_E^(-1)S_tau_jxi_x` by a crude gap bound.  The crude
bound is too large; the actual mechanism is an explicit diagonal resolvent pairing plus an invisible
commutator channel.
