# E78.73 - The basepoint reserve is exactly an old-old radial contraction law

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.72 reduced the shell sign to a basepoint-plus-tail inequality. The first
term there was

```text
BASE_N(sigma_0) := Re Delta ell_N(i sigma_0).            (BPR-1)
```

This note identifies that basepoint exactly as a radial contraction law for the
old-old Schur anchor `1-theta_old`.

## 2. Exact basepoint identity

On the old-old chain from E78.66-E78.67,

```text
Delta ell_N
 = log q_old(N) - log q_old(N+2),                        (BPR-2)
q_old(N) := 1-theta_old(N).                              (BPR-3)
```

Taking real parts gives

```text
Re Delta ell_N
 = log|q_old(N)| - log|q_old(N+2)|
 = log( |1-theta_old(N)| / |1-theta_old(N+2)| ).        (BPR-4)
```

So the basepoint lower bound required by E78.72 is **exactly** a one-step radial
contraction statement for `|1-theta_old|`.

This is a genuine reduction:

```text
BASE_N(sigma_0) > 0
<=>
|1-theta_old(N+2)| < |1-theta_old(N)|                    (BPR-5)
```

at the chosen basepoint `sigma_0`.

## 3. Probe audit at `sigma_0 = 0.55`

Companion:

```text
E78_73_basepoint_radial_probe.py
E78_73_basepoint_radial_results.json
```

The identity `(BPR-4)` reconstructs the certified basepoint rows to roundoff:

```text
zeta:   max reconstruction error <= 9.23e-16,
plant:  max reconstruction error <= 2.23e-16.            (BPR-6)
```

### Zeta

At `sigma_0 = 0.55`, the first six audited steps give:

```text
N= 8:  ratio = |1-theta_8| / |1-theta_10|  ≈ 1.2486,  BASE ≈ 0.22201
N=10:  ratio = |1-theta_10| / |1-theta_12| ≈ 1.2418,  BASE ≈ 0.21659
N=12:  ratio = |1-theta_12| / |1-theta_14| ≈ 1.1186,  BASE ≈ 0.11212
N=14:  ratio = |1-theta_14| / |1-theta_16| ≈ 1.1302,  BASE ≈ 0.12240
N=16:  ratio = |1-theta_16| / |1-theta_18| ≈ 1.1092,  BASE ≈ 0.10363
N=18:  ratio = |1-theta_18| / |1-theta_20| ≈ 1.1082,  BASE ≈ 0.10275
N=20:  ratio = |1-theta_20| / |1-theta_22| ≈ 1.0496,  BASE ≈ 0.04845. (BPR-7)
```

So the zeta basepoint reserve is exactly a stable one-step radial contraction
regime, with contraction ratios bounded away from `1`.

### Planted build

At the same basepoint:

```text
N= 8:  ratio ≈ 0.4209,  BASE ≈ -0.86531
N=10:  ratio ≈ 0.7379,  BASE ≈ -0.30394
N=12:  ratio ≈ 0.6402,  BASE ≈ -0.44598
N=14:  ratio ≈ 3.4802,  BASE ≈  1.24708
N=16:  ratio ≈ 2.6874,  BASE ≈  0.98859
N=18:  ratio ≈ 0.3615,  BASE ≈ -1.01739
N=20:  ratio ≈ 2.9035,  BASE ≈  1.06590.                (BPR-8)
```

The plant therefore does **not** preserve a coherent radial contraction law at
the basepoint. It alternates between strong expansion and contraction.

## 4. Consequence

This sharpens the first ingredient of E78.72:

```text
BASEPOINT-TAIL
<=
OLD-OLD-RADIAL-STEP:
  prove a cofinal one-step contraction law for
  |1-theta_old(N+2)| / |1-theta_old(N)|                  (BPR-9)
```

at a chosen safe basepoint `sigma_0`, together with the tail and phase controls
already isolated.

So the radial part of the shell sign has been reduced from an abstract positive
constant to a concrete contraction ratio.

## 5. Honest reading

This note does not prove the contraction law. It proves that this is the exact
content of the basepoint reserve.

That matters because contraction of `|1-theta_old|` is a much more concrete
finite object than an unnamed lower bound for `Re Delta ell_N`.

## 6. Status

```text
proved:
  BASE_N(sigma_0) is exactly log(|1-theta_old(N)| / |1-theta_old(N+2)|);

observed:
  on the audited zeta ladder at sigma_0=0.55, this is a stable radial
  contraction regime with ratios |1-theta_old(N+2)|/|1-theta_old(N)| bounded
  above by about 0.953;

observed:
  the planted build does not preserve a coherent basepoint contraction regime;

reduced:
  the basepoint side of BASEPOINT-TAIL to OLD-OLD-RADIAL-STEP.
```
