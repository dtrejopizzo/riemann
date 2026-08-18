# E77.5o - Profile Drift Diagnostics

## Objective

E77.5n reduced the residual to the drift of the leading coefficient profile:

```text
C_N(sigma)=N(Delta external_N-Delta logT_N).
```

E77.5o measures

```text
D_N(sigma)=C_N(sigma)-C_{N+2}(sigma)
```

to see whether the profile drift is already summable or whether another
coefficient must be isolated.

## Probe

Artifacts:

```text
E77_5o_profile_drift_probe.py
E77_5o_profile_drift_results.json
```

Command:

```bash
python3 E77_5o_profile_drift_probe.py
```

The probe reads `E77_5n_lead_1_over_n_cancel_results.json` and reports
`D_N`, `N D_N`, and `N^2 D_N` by sigma.

## Last-Window Drift

The table shows the final measured drift `N=18 -> 20` in the coefficient
profile.

| build | sigma | abs D | N D | N^2 D |
|---|---:|---:|---:|---:|
| zeta | 0.55 | 0.00188123 | 0.0338621 | 0.609519 |
| zeta | 0.60 | 0.00205321 | 0.0369578 | 0.665241 |
| zeta | 0.75 | 0.00257075 | 0.0462735 | 0.832924 |
| zeta | 1.00 | 0.00343986 | 0.0619175 | 1.11451 |
| zeta | 1.50 | 0.00521190 | 0.0938142 | 1.68865 |
| zeta | 2.00 | 0.00704603 | 0.126829 | 2.28292 |
| zeta | 3.00 | 0.01097995 | 0.197639 | 3.55750 |
| planted | 0.55 | 0.00778202 | -0.140076 | -2.52138 |
| planted | 0.60 | 0.00741420 | -0.133456 | -2.40220 |
| planted | 0.75 | 0.00581579 | -0.104684 | -1.88432 |
| planted | 1.00 | 0.00251792 | -0.0453226 | -0.815807 |
| planted | 1.50 | 0.00367844 | 0.0662119 | 1.19181 |
| planted | 2.00 | 0.00903530 | 0.162635 | 2.92744 |
| planted | 3.00 | 0.01894357 | 0.340984 | 6.13772 |

## Reading

The zeta drift is smaller and sign-coherent, but not yet eliminated.  The
scaled quantity `N^2 D_N` is still substantial and grows with sigma across
the tested compact:

```text
0.61, 0.67, 0.83, 1.11, 1.69, 2.28, 3.56.
```

Thus `PROFILE-DRIFT-CANCEL` is not closed by the raw drift measurement.

The planted falsifier has a different anatomy: the final drift changes sign
between small and larger sigma, consistent with the failure of coherent
log/external coupling already seen in E77.5l-m.

## Reduced Target

`PROFILE-DRIFT-CANCEL` is reduced to:

```text
SECOND-COEFF-CANCEL:
  identify the next coefficient in

    C_N(sigma)-C_{N+2}(sigma)

  and prove the signed cancellation that removes the observed N^-2 drift.
```

The next step should derive this second coefficient from the
moving-boundary cell expansion instead of extrapolating from N<=22.

## Status

```text
proved:    no delta-envelope theorem yet;
refuted:   raw profile drift as already negligible;
observed:  zeta drift is coherent but still has a visible N^-2-scale
           coefficient;
observed:  planted drift changes sign and fails the zeta profile;
reduced:   PROFILE-DRIFT-CANCEL -> SECOND-COEFF-CANCEL;
next:      E77.5p should isolate the second coefficient from the
           moving-boundary/four-node expansion.
```
