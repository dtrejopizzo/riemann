# E77.7y - Intrinsic Schur regularization audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7x reduced the singular-section problem to the intrinsic Schur package

```text
Sigma, kappa, tau, t0,
v = Sigma^{-1}kappa,
theta = tau v / t0.
```

The next admissible question is whether singular regularization stabilizes
when it is performed directly on this package rather than on external inner
coordinates.

This note audits two intrinsic candidates:

```text
1. shifted Schur solve:   v_eta = (Sigma - i eta I)^(-1) kappa;
2. weak-mode deflation:   kappa -> kappa - <u0,kappa> u0,
   where u0 is the eigenvector of Sigma with smallest |lambda|.
```

Both are tested only through the paired factor

```text
1 - theta_eta
```

and its projective normalization at a safe anchor `sigma0=1`.

## 2. Probe

Companion:

```text
E77_7y_intrinsic_schur_regularization_probe.py
E77_7y_intrinsic_schur_regularization_results.json
```

Command:

```bash
python3 E77_7y_intrinsic_schur_regularization_probe.py \
  --lambda 6 --max-modes 18 --dps 80
```

For each finite section and each build, the probe records:

```text
1. the smallest Schur eigenvalue |lambda0(Sigma)|;
2. the overlap |<u0,kappa>| with the weak Schur direction;
3. the final eta-step of the shifted projective profile on
   eta = 1e-2,1e-4,1e-6,1e-8;
4. the projective difference between the raw profile and the weak-mode
   deflated profile.
```

The profile itself is

```text
Pi_eta(i sigma)
= (1-theta_eta(i sigma)) / (1-theta_eta(i sigma0)).
```

As in E77.7m--p, the reference `mu` is the largest finite-section surrogate,
not the abstract `mu_L`.

## 3. Result

### Shifted Schur regularization

The shifted intrinsic solve is highly stable as `eta -> 0` in both builds.

For zeta:

```text
final eta-step
= 1.87e-6 at N=9,
  1.74e-9 at N=10,
  5.66e-11 at N=12,
  9.93e-14 at N=17.
```

For the planted build:

```text
final eta-step
= 2.44e-7 at N=6,
  8.55e-8 at N=10,
  3.74e-9 at N=14,
  2.73e-10 at N=18.
```

So the intrinsic Schur profile is already essentially `eta`-stable on the
tested ladder, including the zeta sections where E77.7p failed badly at the
full-coordinate resolvent level.

### Weak-mode deflation

Deflating the weakest Schur mode changes the projective profile by a real but
bounded amount.

For zeta:

```text
max deflated/raw projective relative difference
= 0.234 at N=6,
  0.131 at N=10,
  0.065 at N=18.
```

For the planted build:

```text
max deflated/raw projective relative difference
= 0.175 at N=10,
  0.015 at N=16,
  9.19e-4 at N=18.
```

So weak-mode subtraction is not innocuous normalization drift.  It alters the
profile itself.  That means the admissible object is the shifted intrinsic
limit, not a deflated replacement profile.

## 4. Reading

This is the first singular regularization that behaves correctly in the exact
coordinates isolated by the autopsies.

```text
E77.7p: naive full resolvent regularization failed in the zeta near-null regime;
E77.7u: every spectral Feshbach variant is equivalent to mode subtraction;
E77.7q--w: external one-mode / block / Krylov regularizations never closed;
E77.7x: the true unstable object is the intrinsic Schur package.
```

E77.7y shows that once the regularization is performed directly on

```text
Sigma^{-1}kappa
```

the `eta`-instability practically disappears.

This does **not** yet prove the theorem-grade singular-section bridge,
because the probe is still finite, grid-based, and uses a finite surrogate
for `mu_L`.  But it changes the live object sharply:

```text
the correct singular bridge is a limit theorem for the intrinsic Schur
profile Pi_eta, not a subtraction theorem for external resonant modes.
```

## 5. What is refuted and what survives

Refuted:

```text
WEAK-MODE-DEFLECT-THEN-CLOSE:
replace the raw Schur profile by the profile with the weakest Sigma mode
removed.
```

The deflated profile differs nontrivially from the raw one, especially in the
zeta build, so this is not a harmless canonical replacement.

Supported:

```text
INTRINSIC-SCHUR-ETA-STABILITY:
for safe compact K, the projective family built from
v_eta = (Sigma - i eta I)^(-1)kappa
has a local-uniform eta -> 0 limit.
```

This target is falsifier-neutral in the observed sense: both builds stabilize
under the same intrinsic procedure.

## 6. Smaller live object

The next admissible theorem target is:

```text
INTRINSIC-SCHUR-ETA-LIMIT:
for each fixed finite section and safe compact K,
Pi_{N,eta}(z)
= (1-theta_{N,eta}(z)) / (1-theta_{N,eta}(z0))
converges locally uniformly as eta -> 0,
with the limit compatible with the singular section required in
PROJECTIVE-MU-TRANSFER.
```

Then:

```text
INTRINSIC-SCHUR-ETA-LIMIT
+ PROJECTIVE-MU-TRANSFER away from singular sections
=> singular-section clause for the LP interface bridge.
```

This is strictly smaller and sharper than `RESONANT-MODE-REGULARIZATION`.

## 7. Status

```text
observed:  intrinsic Schur shift regularization is eta-stable for both zeta
           and plant on the tested ladder;
observed:  weak-mode deflation changes the profile nontrivially and is not a
           canonical replacement;
refined:   the live singular target is INTRINSIC-SCHUR-ETA-LIMIT;
next:      prove eta-limit at fixed section and then transport it into the
           theorem-grade projective mu-transfer bridge.
```
