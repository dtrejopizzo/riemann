# E72.276 -- Gauged root-window profile

**Purpose.** Test the corrected pole-even HPAC residual on all finite Weyl roots in a fixed compact
height window.

After E72.275, the resonant residual is

```text
R_x(s,tau_j)
= <a_s^perp,C_E^(-1)i alpha(tau_j)S_tau_j xi_x>,
```

where

```text
a_s^perp = a_s - xi_x<xi_x,a_s>/<xi_x,xi_x>.
```

This is the first version of the HPAC root target that is both:

```text
1. in the corrected full pole-even sector;
2. free of the old invalid Q=I-kk^* line removal;
3. free of the harmless constant 2xi_x channel.
```

## Fixed-height probe

Run:

```text
python3 E72_276_gauged_root_window_profile.py
```

Output:

```text
E72.276 gauged root-window profile
Residual: <a_s^perp,C_E^(-1)i alpha(tau_j)S_tau_j xi_x>.
Fixed compact height H=8; higher-height tails are a separate theorem.
lam L roots max mean
 16 5.545177     7 2.571511e-02 7.211859e-03
 20 5.991465     7 1.494883e-02 4.471099e-03
 24 6.356108     5 6.308598e-03 2.660988e-03
 28 6.664409     6 4.104033e-03 1.152259e-03
 32 6.931472     8 2.102367e-03 6.118181e-04
```

## Reading

This is a positive compact-height signal: for fixed `H=8`, the maximum corrected HPAC root residual
decreases by more than one order of magnitude from `lambda=16` to `lambda=32`.

The result should be stated with the correct quantifier order:

```text
for each fixed compact height H and Cauchy compact K,
max_{0<tau_j<=H, s in K} |R_x(s,tau_j)| -> 0.
```

It does **not** yet prove a growing-height statement.  A quick exploratory run at `H=12` already shows a
larger finite-window spike at `lambda=16`, so the high-root tail must remain a separate estimate.

## Next theorem

The next load-bearing statement is:

```text
Pole-even gauged HPAC compact-root decay:
for every fixed H and compact Cauchy set K,
sup_{s in K} max_{0<tau_j<=H}
|<a_s^perp,C_E^(-1)i alpha(tau_j)S_tau_j xi_x>| -> 0.
```

Together with a high-root tail estimate, this is the corrected finite-root side of Mellin spectral
divisibility.
