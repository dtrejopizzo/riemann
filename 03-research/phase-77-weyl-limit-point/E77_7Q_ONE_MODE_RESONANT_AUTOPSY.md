# E77.7q - One-mode resonant autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7p refuted naive singular-section regularization and suggested the next
smaller object:

```text
RESONANT-MODE-REGULARIZATION:
separate the near-null inner mode from the regular remainder before forming
the projective quotient.
```

This note audits the simplest version of that idea: subtract the single
closest inner eigenmode to zero.

## 2. Probe

Companion:

```text
E77_7q_resonant_mode_probe.py
E77_7q_resonant_mode_results.json
```

Command:

```bash
python3 E77_7q_resonant_mode_probe.py \
  --lambda 6 --max-modes 18 --dps 60
```

For the frozen finite point `mu_ref`, write

```text
x_{N,eta} = (A_N(mu_ref)-i eta I)^(-1)b_N
          = coeff_0/(lambda_0-i eta) u_0 + x_{N,eta}^reg,
```

where `u_0` is the inner eigenvector whose eigenvalue `lambda_0` has minimum
absolute value.

The probe compares:

```text
raw projective profile from x_{N,eta},
regular projective profile from x_{N,eta}^reg,
```

using the same `eta` ladder as E77.7p.

## 3. Result

### Zeta

For every `N=6..18`, the final `eta`-step of the regularized profile after
one-mode subtraction is numerically identical to the raw one, up to roundoff:

```text
N=12: raw 0.06652413167093632907
      reg 0.06652413167093632904

N=18: raw 0.05266680150940462284
      reg 0.05266680150940462284.
```

So in the near-null zeta regime, removing the nearest single inner mode does
not stabilize the projective profile at all.

### Planted build

Away from singularity, one-mode subtraction is not the right correction
either.  The raw profile was already highly stable (`1e-8` to `1e-6` final
steps), while the one-mode-subtracted profile is often **less** stable:

```text
N=10: raw 1.76e-7,  reg 2.35e-6
N=12: raw 6.27e-7,  reg 1.20e-5
N=18: raw 1.87e-6,  reg 3.12e-5.
```

Only sporadically does the one-mode subtraction help.

## 4. Reading

This autopsy is decisive:

```text
1. the zeta instability of E77.7p is not carried by a single closest inner
   mode;
2. the relevant singular package is at least multi-mode / low-dimensional;
3. subtracting one mode can even spoil a stable regime away from singularity.
```

So the obstruction is not "one bad pole."  It is a structured resonant block
whose internal mixing survives the projective quotient.

## 5. What is refuted

The following reduced target is refuted:

```text
ONE-MODE-RESONANT-REGULARIZATION:
remove the nearest inner eigenmode and take the projective eta->0 limit of
the remainder.
```

It neither stabilizes zeta nor preserves the already stable planted regime.

## 6. Smaller live object

The next admissible object is:

```text
LOW-BLOCK-RESONANT-REGULARIZATION:
identify a finite resonant block E_N^res of all inner modes whose scale is
comparable to the eta-regularization window, split

  x_{N,eta} = x_{N,eta}^res + x_{N,eta}^far,

and prove projective stability only after treating the full block
E_N^res together with the safe Cauchy rows.
```

Concretely, the correct finite quantity is no longer

```text
coeff_0/(lambda_0-i eta),
```

but a low-rank matrix-valued self-energy built from the near-null cluster.

## 7. Status

```text
observed:  one-mode subtraction leaves zeta eta-instability unchanged;
observed:  one-mode subtraction often worsens the already stable planted
           regime;
refuted:   ONE-MODE-RESONANT-REGULARIZATION;
open:      LOW-BLOCK-RESONANT-REGULARIZATION;
next:      identify the minimal resonant cluster and treat its projective
           contribution as a finite matrix block before quotienting.
```
