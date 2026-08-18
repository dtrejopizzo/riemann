# E77.7r - Low-block resonant autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7q refuted one-mode subtraction and left the next reduced target:

```text
LOW-BLOCK-RESONANT-REGULARIZATION:
subtract a finite resonant cluster before forming the projective quotient.
```

This note audits the first nontrivial case: a resonant block of size `3`
consisting of the three inner eigenmodes closest to zero.

## 2. Probe

Companion:

```text
E77_7r_low_block_resonant_probe.py
E77_7r_low_block_resonant_results.json
```

Command:

```bash
python3 E77_7r_low_block_resonant_probe.py \
  --lambda 6 --max-modes 18 --dps 60 --block-size 3
```

The probe compares:

```text
raw regularized projective profile;
projective profile of the remainder after subtracting the 3-mode block.
```

As before, `mu_ref` is only the largest finite-section frozen surrogate.

## 3. Result

### Zeta

For every tested section `N=6..18`, the final `eta`-step after subtracting
the 3-mode block is numerically indistinguishable from the raw one:

```text
N=12: raw 0.06652413167093632907
      reg 0.06652413167093656268

N=18: raw 0.05266680150940462284
      reg 0.05266680150940462284.
```

So the zeta instability identified in E77.7p is **not** resolved by any
fixed low block of size `3`.

### Planted build

Here the picture is different.  The same 3-mode subtraction often reduces
the already tiny `eta`-steps by one or two orders:

```text
N=10: raw 1.76e-7   -> reg 4.00e-8
N=12: raw 6.27e-7   -> reg 3.96e-8
N=18: raw 1.87e-6   -> reg 5.34e-8.
```

For very small sections it can be slightly worse, but in the late planted
regime it captures most of the residual instability.

## 4. Reading

This gives a sharper structural picture.

```text
1. the planted near-resonance is genuinely low-rank: a small resonant block
   explains most of the eta-instability there;
2. the zeta near-null regime is not captured by any fixed tiny block;
3. therefore a size-3 resonant block is still too narrow for the theorem
   target.
```

So the next object is not "subtract a few lowest modes" in a fixed way.  The
right block must be **adaptive** to the regularization scale or to the
boundary-coupled self-energy.

## 5. What is refuted

The following target is now refuted for zeta:

```text
FIXED-3-BLOCK-RESONANT-REGULARIZATION.
```

It helps the planted build but leaves the zeta instability unchanged.

## 6. Smaller live object

The next admissible reduction is:

```text
ADAPTIVE-RESONANT-WINDOW:
define the resonant block E_N^res(eta) by a spectral window tied to the
regularization scale eta or to the paired boundary self-energy, rather than
by a fixed number of lowest modes.
```

Equivalently, one needs a theorem that separates:

```text
near modes with |lambda_j| <= W_N(eta)
far modes  with |lambda_j| >  W_N(eta),
```

with `W_N(eta)` chosen from the actual projective boundary coupling, not from
an a priori fixed dimension.

This is strictly smaller than full `PROJECTIVE-MU-TRANSFER` and strictly more
accurate than the failed one-mode and fixed-3-mode reductions.

## 7. Status

```text
observed:  fixed size-3 block subtraction captures much of the planted
           eta-instability;
observed:  the same subtraction leaves zeta unchanged to numerical
           precision;
refuted:   FIXED-3-BLOCK-RESONANT-REGULARIZATION as a zeta closure target;
open:      ADAPTIVE-RESONANT-WINDOW;
next:      tie the resonant block to the eta-scale or boundary-coupled
           self-energy instead of a fixed mode count.
```
