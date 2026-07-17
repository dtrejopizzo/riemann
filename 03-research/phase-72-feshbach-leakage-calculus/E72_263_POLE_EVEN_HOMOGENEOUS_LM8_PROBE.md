# E72.263 -- Pole-even homogeneous LM8 probe

**Purpose.** Refit the homogeneous LM8 envelope in the corrected pole-relative even geometry of
E72.262.

The polynomial architecture is unchanged:

```text
P_j(u)=u^2 R_j(u),
P_j(0)=P_j'(0)=0.
```

But the spectra are now those of the corrected operator:

```text
C_model = B_even^T(H_model-e_pole I)B_even,
```

with no accidental even line removed.

## Stable-window result

The low windows behave as follows in E72.262:

```text
lambda=6,8,12: exact BSE > 0.9409       finite failures for this threshold
lambda=16:     exact BSE = 0.9235401    passes exact BSE, but tight
lambda>=20:    exact BSE has comfortable margin in the tested range
```

E72.263 therefore refits LM8 on the stable windows:

```text
lambda = 16,20,24
```

and checks degrees `R=4,6,8,10,12`.

## Output

The best tested homogeneous envelopes still do not certify the delicate `lambda=16` window:

```text
R degree=8:
  lambda=16  env=9.978990e-01  FAIL
  lambda=20  env=9.124424e-01  PASS
  lambda=24  env=8.871077e-01  PASS

R degree=10:
  lambda=16  env=9.686461e-01  FAIL
  lambda=20  env=8.723770e-01  PASS
  lambda=24  env=8.325084e-01  PASS

R degree=12:
  lambda=16  env=9.554410e-01  FAIL
  lambda=20  env=8.693836e-01  PASS
  lambda=24  env=8.177026e-01  PASS
```

The exact BSE at `lambda=16` is below target, so this is not an RFBD failure. It is a polynomial
envelope failure in a tight finite window.

## Interpretation

The corrected pole-even route should split LM8 into:

```text
lambda >= 20: homogeneous LM8 envelope;
lambda = 16: finite sharp BSE or lower-dimensional certificate;
lambda < 16: below the stable threshold, handled separately or excluded by L0.
```

This is cleaner than forcing a single fixed polynomial to certify the transition window. The majorant
is meant for the uniform/asymptotic regime; the threshold window can be certified by direct interval
arithmetic on the finite matrices.

## Candidate stable coefficients

For the corrected stable regime, the `R degree=8` refit already certifies `lambda=20,24`:

```text
R0 =
  9.9902884873e-01
 -1.9514292338e+00
 -1.8253403605e+01
 -8.5297082916e+00
  2.6356605613e+02
  2.1058093811e+02
 -1.5488260398e+03
 -7.4663940140e+02
  3.2475435437e+03

R1 =
  9.9874673938e-01
 -2.5131201071e+00
 -1.3197719671e+01
  2.1797818446e+01
  1.2775742495e+02
 -1.3558570957e+02
 -3.4870221311e+02
  1.9700896920e+02
  3.2577191198e+02
```

These are not yet rational/interval certified. The next proof-facing step is:

```text
stable LM8-pole-even:
  rationalize/certify a homogeneous envelope for lambda>=20,
  and separately interval-certify lambda=16 by a sharp finite BSE certificate.
```

## Status

The pole-even correction preserves the RFBD architecture but changes the finite bookkeeping. The old
claim "one LM8 envelope from lambda=16" should be replaced by a thresholded statement:

```text
LM8 envelope for stable windows + sharp finite certificate for the transition window.
```
