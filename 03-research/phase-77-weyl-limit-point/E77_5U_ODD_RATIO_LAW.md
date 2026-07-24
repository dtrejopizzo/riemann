# E77.5u - Odd Ratio Law

## Objective

E77.5t reduced the weighted parity obstruction to the normalized ratio:

```text
odd_ratio = |weighted odd package| / |weighted inserted package|.
```

E77.5u tests whether this ratio models the second coefficient `Q_N`.

## Probe

Artifacts:

```text
E77_5u_odd_ratio_law_probe.py
E77_5u_odd_ratio_law_results.json
```

Command:

```bash
python3 E77_5u_odd_ratio_law_probe.py
```

The probe fits `Q = a odd_ratio + b` by sigma on the zeta data from
E77.5t, then applies the same fit to the planted rows.

## Results

Global zeta fit by sigma:

| sigma | slope | intercept | zeta max residual | planted max residual |
|---:|---:|---:|---:|---:|
| 1.0 | 1.32865 | -0.537538 | 0.651475 | 102.345 |
| 3.0 | 3.01861 | -0.599781 | 1.96194 | 12.8181 |

The global ratio law is therefore too coarse.

Splitting the zeta fit by mod class:

```text
sigma=1.0, N=0 mod 4: max residual 0.04798
sigma=3.0, N=0 mod 4: max residual 0.11095

sigma=1.0, N=2 mod 4: max residual 0.56040
sigma=3.0, N=2 mod 4: max residual 1.69131
```

## Autopsy

`ODD-RATIO-LAW` is not a full closure.  It captures the stable zeta
`N=0 mod 4` branch well, but it does not explain the `N=2 mod 4` spike.
The planted falsifier fails the global zeta fit by large margins, so the
ratio remains useful as an arithmetic-sensitive diagnostic, but it is not
the final cell law.

## Reduced Target

`ODD-RATIO-LAW` is reduced to:

```text
MOD2-MISSING-WEIGHT:
  find the additional weighted active-block observable that distinguishes
  the N=2 mod 4 branch from the stable N=0 mod 4 branch.
```

Candidates already available in E77.5t:

```text
old-boundary-pair / inserted,
outer-pair / inserted,
old-shell-pair / inserted,
complex phase of weighted odd package.
```

## Status

```text
proved:    no delta-envelope theorem yet;
refuted:   global odd-ratio law as a complete Q_N model;
observed:  odd-ratio law models zeta N=0 mod 4 branch well;
observed:  zeta N=2 mod 4 branch still carries the spike;
observed:  planted fails the zeta fit;
reduced:   ODD-RATIO-LAW -> MOD2-MISSING-WEIGHT;
next:      E77.5v should test the remaining weighted ratios/phases for
           the N=2 mod 4 branch.
```
