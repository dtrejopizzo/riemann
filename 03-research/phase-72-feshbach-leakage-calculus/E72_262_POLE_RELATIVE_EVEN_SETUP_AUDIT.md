# E72.262 -- Pole-relative even setup audit

**Purpose.** Repair the model complement geometry after E72.261.

The pole-relative route should not use the pure even ground as the energy base. It should subtract the
global pole energy, which in the model is an odd vector, while keeping the full physical even sector.

Thus the corrected construction is:

```text
e_pole  = lambda_0(H_model)          # odd pole mode
B_even  = orthonormal even Fourier basis
C_model = B_even^T (H_model  - e_pole I) B_even
C_actual= B_even^T (H_actual - e_pole I) B_even
```

No symmetrized near-zero vector is normalized, and no arbitrary even line is removed.

## Diagnostic

The pole is odd to numerical precision:

```text
poleOdd = 1.000e+00,
poleEvenLeak = 2e-16 -- 6e-16.
```

The corrected pole-even model complement has the desired `L^2` scale:

```text
lam  L       oldMinC      poleEvenMinC  minC/L^2
  6  3.5835  2.614634e+00 2.503992e+00 1.949905e-01
  8  4.1589  4.124950e+00 3.912816e+00 2.262226e-01
 12  4.9698  7.526496e+00 7.024137e+00 2.843890e-01
 16  5.5452  1.060517e+01 1.036559e+01 3.371033e-01
 20  5.9915  1.419980e+01 1.384117e+01 3.855733e-01
 24  6.3561  1.775109e+01 1.740525e+01 4.308218e-01
```

So the `L^2` coercivity was not imaginary; it belongs to the pole-relative even sector.

## LM8 impact

The old LM8 rational majorant was fitted in the accidental complement. In the corrected pole-even
geometry, the exact BSE and old rational envelope become:

```text
lam  exactBSE      old rational LM8 envelope
  6  1.376502e+00  1.398716e+03
  8  1.354176e+00  1.258908e+02
 12  1.067327e+00  6.597546e+00
 16  9.235401e-01  1.114324e+00
 20  8.277297e-01  9.214678e-01
 24  7.748451e-01  8.760991e-01
```

Interpretation:

* The corrected geometry has finite low-window failures (`lambda=6,8,12`) for exact BSE.
* Starting at `lambda=16`, exact BSE is below the target `0.9409`.
* The old rational LM8 envelope is too loose at `lambda=16` but passes again by `lambda=20`.

Thus the architecture is not dead, but the LM8 polynomial certificate must be refit/certified in the
corrected pole-even geometry, with low finite windows handled separately.

## Corrected target

Replace old uses of `setup_pair` in proof-facing RFBD/LM8 statements by the pole-relative even setup:

```text
MCOER2-pole-even:
lambda_min(B_even^T(H_model-e_pole I)B_even) >= c_C L^2.
```

Then redo:

```text
LM8-pole-even,
HOC3-pole-even,
K1-pole-even,
RFBD-pole-even.
```

## Status

This repairs the parity/gauge bug without abandoning the pole-relative route. The next task is to
construct a homogeneous rational LM8 majorant for the corrected pole-even spectra, starting from
`lambda>=16` or `lambda>=20`, and classify the smaller windows as finite exceptions.
