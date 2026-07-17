# E72.289 -- APCB band exclusion

**Purpose.** Locate why compressed APCB is much smaller than the full-line Dirichlet-symbol floor.

E72.287 showed that APCB follows from the full-line scalar floor

```text
-2 inf_omega Re P_L(omega)=O(L^2),
```

but E72.288 flagged this as likely RH-strength.  The compressed operator is much smaller.  This note
tests where its top positive eigenvector lives in the Fourier mesh.

## Probe

Run:

```text
python3 E72_289_apcb_band_exclusion_probe.py
```

Output:

```text
E72.289 APCB band-exclusion probe
Top positive Delta_arith eigenvector mass in mesh frequency d=2pi n/L.
badArg is the low-frequency minimizer of the full-line Dirichlet symbol on [0,4].
lam L pos/L2 badArg mean|d| rmsD mass|d|<2 mass2<=|d|<8 mass|d|>=8
 16 5.545177 1.617975e-01 7.020000e-01 2.263994e+01 2.427396e+01 2.919130e-03 1.606084e-02 9.810200e-01
 20 5.991465 1.530683e-01 6.440000e-01 3.019511e+01 3.090288e+01 2.608950e-05 2.522864e-04 9.997216e-01
 24 6.356108 1.428683e-01 6.040000e-01 3.172632e+01 3.246001e+01 3.523355e-04 1.225729e-03 9.984219e-01
 28 6.664409 1.406409e-01 5.730000e-01 1.925971e+01 2.064233e+01 1.491140e-03 4.281407e-03 9.942275e-01
 32 6.931472 1.327397e-01 5.480000e-01 1.971723e+01 2.046029e+01 5.030315e-07 5.269743e-05 9.999468e-01
```

## Reading

The full-line symbol is worst at low frequency:

```text
omega_bad ~= 0.5--0.7.
```

But the top positive compressed eigenvector has almost all its Fourier-mesh mass in high frequency:

```text
mass(|d|>=8) >= 0.98
```

in the tested windows, and often above `0.999`.

Therefore the gap between DSF and APCB is not accidental.  The compressed even finite operator excludes
the low-frequency directions responsible for the worst full-line symbol floor.

## Proof-facing target

A sharper APCB route is:

```text
APCB-band:
decompose u = u_low + u_high in mesh frequency.

1. Low band:
   prove the positive Delta_arith form is small on |d|<8 after even finite compression.

2. High band:
   prove a direct O(L^2) ceiling for the compressed autocorrelation on |d|>=8.

3. Cross terms:
   control by Cauchy-Schwarz or a finite off-band kernel estimate.
```

This route uses the compression that DSF discards.  It is not a full-line `-zeta'/zeta` floor.
