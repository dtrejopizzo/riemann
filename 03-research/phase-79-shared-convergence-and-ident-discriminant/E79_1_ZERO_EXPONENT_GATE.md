# E79.1 - ZERO exponent gate: precision floor first, asymptotic verdict still open

**Scope:** `GAP-Z` only, first milestone of Phase 79.  
**Class:** AUTOPSIA + GATE NUMERICO FRANCO.  
**What we know after this document that we did not know before:** the extended
ZERO-side exponent probe is numerically trustworthy at `dps=60` through
`N=24`, but not at `dps=50`; the low-precision run develops a fake blow-up
starting at `N=20`. Once the precision floor is lifted, the extended data
reproduces the Phase-78 anchor exactly and still looks consistent with a
borderline but summable law `ZERO ~ N^{-p}` with `p` only slightly above `1`
on the zeta side. So `E79.1` has not yet reached the promised `N=40+`, but it
has already closed the first numerical gate: any candid continuation must run
at `dps >= 60`, and raw `build_mp` cost is the mechanical bottleneck.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This stays entirely on the fixed-L / Re(s)>1 side.
MW-3:  respected. No per-prime local/global assembly.
MW-4:  respected. No wrong-sign lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No spectral-gap assumption.
K1-K5: respected. This is a direct measurement of the independent K_N spectral
       object from E78.152/E78.157, before any endpoint identification.
E72.16/E77.7az: respected. This is a convergence gate, so only build-neutral
       conclusions count. Any zeta/plant difference below is reported only as
       observed regularity, not as a forcing step.
Circularity: respected. ZERO is computed from spec(K_N), not from the target
       Gamma/cell derivative.
```

## 1. The target under test

Phase 78 reduced the shared convergence lemma to:

```text
GAP-Z:
ZERO_N(sigma)
  = sum_{kappa in spec K_{N+2}} 2 sigma/(kappa^2+sigma^2)
  - sum_{kappa in spec K_N}     2 sigma/(kappa^2+sigma^2),          (Z-1)
```

with `MESH = O(sigma/N^2)` and `BND = O(sigma/N^3)` already proved
build-neutrally in E78.157. The only open numerical question for the first
gate is the effective exponent of `ZERO_N`:

```text
ZERO_N(sigma) ?~ C_sigma N^{-p_sigma}.                              (Z-2)
```

If `p_sigma > 1` on safe compacta, the evidence points toward summability;
if `p_sigma ~ 1` or below, `GAP-Z` becomes marginal or false.

## 2. Probe

Companion file:

```text
E79_1_zero_exponent_probe.py
```

The probe reuses the verified machinery:

```text
- build_mp from P76.002,
- right_transfer_data from E77.3c,
- the section cutter from E78.9,
- the exact K_N builder from E78.152/E78.157.
```

For each section depth `N`, it computes `spec(K_N)`, evaluates `(Z-1)` at
`sigma in {0.55, 1, 2, 3}`, and records:

```text
- ZERO_N(sigma),
- N^2 ZERO_N(sigma),
- local ratio exponent p_local,
- sliding-window log-log fit p_window.
```

## 3. First finding: `dps=50` is not admissible for the extended run

Running zeta only with

```text
maxN=26, dps=50
```

reproduces the established Phase-78 values up to `N=18`, but then develops a
catastrophic fake blow-up:

```text
sigma = 1
N=18: ZERO = 0.001620319...,   N^2 ZERO = 0.524983...
N=20: ZERO = 0.021084899...,   N^2 ZERO = 8.433959...
N=22: ZERO = 0.308140915...,   N^2 ZERO = 149.140...
N=24: ZERO = 1.696259789...,   N^2 ZERO = 977.045...
```

This is incompatible with the already-certified Phase-78 anchor E78.157b at the
same `maxN=26`, and therefore cannot be read as a genuine asymptotic signal.

So:

```text
dps=50 is below the numerical stability floor for extended ZERO-side runs.     (Z-3)
```

This is the first decisive outcome of E79.1.

## 4. Stable run at `dps=60`: exact agreement with the Phase-78 anchor

Repeating the same ladder with

```text
maxN=26, dps=60
```

restores stability and matches E78.157b exactly on the common range.

### Zeta, `sigma = 1`

```text
N= 8: ZERO = 0.00441146161408,  N^2 ZERO = 0.282333543301
N=10: ZERO = 0.00311967333856,  N^2 ZERO = 0.311967333856
N=12: ZERO = 0.00266839222435,  N^2 ZERO = 0.384248480306
N=14: ZERO = 0.00209014597783,  N^2 ZERO = 0.409668611655
N=16: ZERO = 0.00191375639527,  N^2 ZERO = 0.489921637188
N=18: ZERO = 0.00162059139824,  N^2 ZERO = 0.525071613030
N=20: ZERO = 0.00128806245044,  N^2 ZERO = 0.515224980175
N=22: ZERO = 0.00136705197055,  N^2 ZERO = 0.661653153746
N=24: ZERO = 0.00114056098219,  N^2 ZERO = 0.656963125740
```

### Plant, `sigma = 1`

```text
N= 8: ZERO = -0.187814467254,   N^2 ZERO = -12.0201259043
N=10: ZERO =  0.0087314478509,  N^2 ZERO =  0.87314478509
N=12: ZERO =  0.0120726608506,  N^2 ZERO =  1.73846316248
N=14: ZERO =  0.00736404224019, N^2 ZERO =  1.44335227908
N=16: ZERO =  0.00774455723221, N^2 ZERO =  1.98260665145
N=18: ZERO =  0.00580243905844, N^2 ZERO =  1.87999025494
N=20: ZERO =  0.00534961440599, N^2 ZERO =  2.13984576240
N=22: ZERO =  0.00465050081642, N^2 ZERO =  2.25084239515
N=24: ZERO =  0.00359681159533, N^2 ZERO =  2.07176347891
```

These are exactly the Phase-78 patterns, extended only in bookkeeping, not in
qualitative behavior:

```text
- zeta: N^2 ZERO drifts upward mildly (~0.28 -> ~0.66);
- plant: after the N=8 transient, N^2 ZERO wanders in a band of order 1-2.
```

## 5. What exponent the stable data actually supports

On the stable `dps=60` run, the sliding 4-step log-log fits for zeta give:

```text
sigma = 1
N=14 window fit: p_window = 1.29026
N=16 window fit: p_window = 1.09407
N=18 window fit: p_window = 1.17768
N=20 window fit: p_window = 1.34469
N=22 window fit: p_window = 1.18710
N=24 window fit: p_window = 1.04144
```

and similarly for `sigma = 2, 3`:

```text
sigma = 2: p_window ranges 1.04 .. 1.34
sigma = 3: p_window ranges 1.04 .. 1.34
```

So the stable data does **not** support any clean `N^{-2}` law for ZERO, but it
also does **not** support a non-summable growth. The candid reading is:

```text
on the current stable range, zeta is consistent with a borderline summable law
ZERO ~ N^{-p} with p just above 1.                                   (Z-4)
```

For the plant the same window fits, after the initial sign-changing transient,
sit roughly in the `p ~ 1.0 .. 1.8` band depending on `sigma`, again far from a
clean `2`, but not obviously non-summable on the audited range.

## 6. What E79.1 still has not settled

E79.1 asked for `N=40+`. This document does **not** reach that range.

The reason is mechanical, not conceptual: the cost sits in `build_mp`, which
rebuilds the full CCM matrix entry-by-entry via the `WR` quadratures before any
K_N diagonalization happens. The extended raw runs showed:

```text
- the mathematics side (K_N and ZERO) is stable at dps=60 through N=24;
- the engineering bottleneck is the matrix builder, not the exponent fitter.
```

So the next admissible move is no longer "interpret dps=50" or "guess from the
current tail", but:

```text
either
  (a) push the same probe to N=40+ with a cached / staged build_mp workflow, or
  (b) bypass the brute-force extension and move directly to E79.2 / E79.3,
      where the secular equation controls near-origin root displacement.
```

## 7. Consequence for the phase

This closes one real gate and sharpens the next one:

```text
E79.1 so far proves:
  any trustworthy extended ZERO exponent audit must run at dps >= 60;        (Z-5)

E79.1 so far observes:
  on the stable range N <= 24, both builds remain compatible with the
  Phase-78 picture; zeta stays in the borderline-summable p > 1 regime,
  with no evidence yet for a clean asymptotic constant and no evidence yet
  for genuine non-summability.                                               (Z-6)
```

So the question "is GAP-Z even plausible?" remains alive, but with a much
tighter reading:

```text
plausible, yes;
proved, no;
numerically settled to N=40+, not yet.
```

## 8. Status

```text
proved:
  dps=50 is numerically inadmissible for the extended ZERO-side run; it creates
  a fake blow-up starting at N=20 on the zeta side, contradicting the certified
  Phase-78 anchor;

proved:
  dps=60 restores stability and reproduces the Phase-78 anchor exactly on the
  full audited range N=8..24 for both builds;

observed:
  on the stable range, zeta remains compatible with a borderline summable
  exponent p just above 1, not with a clean N^-2 law;

observed:
  the plant, after the initial transient, remains in the order-one N^2 ZERO band
  already seen in Phase 78;

open:
  extend the stable audit to N=40+, or replace the brute-force extension by the
  near-origin root-displacement route of E79.2/E79.3;

next:
  either add a cached/staged build path for build_mp and rerun E79.1 to N=40+,
  or begin E79.2 by isolating the near-origin part of ZERO exactly.
```
