# E77.7h - Cyclic Lanczos mass audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced `CYCLIC-WINDOW-MASS` to controlling the Stieltjes transform
of the cyclic coupling measure

```text
Sigma_R(eta)=<h_R,(K_R-mu_R+eta)^(-1)h_R>.
```

This note tests whether low-order cyclic moments, via Lanczos, can certify
the required window masses without diagonalizing the complement spectrum.

The result is mixed:

```text
finite cyclic Lanczos exactly reconstructs the self-energy when enough
steps are used, but fixed low-order moments do not resolve the zeta
critical window.
```

## 2. Exact cyclic Lanczos formulation

Starting from `q_0=h_R/||h_R||`, Lanczos for the self-adjoint complement
`K_R` produces a Jacobi matrix `J_m`.  For every finite `m`,

```text
Sigma_R^(m)(eta)
= ||h_R||^2 e_0^T (J_m-mu_R+eta)^(-1)e_0.    (L-1)
```

This is the Stieltjes transform of the `m`-point Gaussian quadrature measure
for the cyclic moments

```text
<h_R,K_R^j h_R>,  j=0,...,2m-1.
```

At full cyclic dimension, `(L-1)` equals the finite Feshbach self-energy
from E77.7h.  Therefore the proof-facing admissible target is:

```text
LANCZOS-RESOLUTION-ENVELOPE:
Construct a cofinal depth m_R and certified upper Stieltjes bracket
U_R^(m_R)(eta) for the cyclic Lanczos measure such that

Sigma_R(eta_R) <= U_R^(m_R)(eta_R) <= eta_R,
eta_R -> 0,

and eta_R remains small in the E77.7h bracketed-low-mode denominator.
```

Then

```text
LANCZOS-RESOLUTION-ENVELOPE
=> CYCLIC-WINDOW-MASS
=> WFE-CYCLIC-TAIL
=> WEIGHTED-FESHBACH-ENVELOPE
=> RITZ-BRACKET
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.                              (L-2)
```

This stays within the allowed architecture: it is a cyclic Stieltjes
convergence theorem, not positivity of the Weil form, not a zero filter, and
not an ambient inverse estimate.

## 3. Probe

Companion:

```text
E77_7h_cyclic_lanczos_probe.py
E77_7h_cyclic_lanczos_results.json
E77_7h_cyclic_lanczos_deep_results.json
```

Commands:

```bash
python3 E77_7h_cyclic_lanczos_probe.py \
  --lambda 6 --max-modes 18 --refs 8,10,12,14,16 \
  --lanczos-steps 14 --dps 70

python3 E77_7h_cyclic_lanczos_probe.py \
  --lambda 6 --max-modes 18 --refs 14,16 \
  --lanczos-steps 36 --dps 70 \
  --output E77_7h_cyclic_lanczos_deep_results.json
```

The probe compares `Sigma_R^(m)(delta)` with the exact finite self-energy
and also solves the fixed point for the truncated Jacobi matrix.

### Zeta, 14 Lanczos steps

| R | rel error at step 14 | fixed point / delta | steps for 1e-8 |
|---:|---:|---:|---:|
| 8  | 2.08e-2 | 0.979164 | NA |
| 10 | 4.15e-1 | 0.584641 | NA |
| 12 | 9.06e-1 | 0.093878 | NA |
| 14 | 9.9999e-1 | 7.50e-6 | NA |
| 16 | 1.0000 | 1.10e-10 | NA |

Fixed low-order Lanczos does not see the critical zeta window as `R`
increases.  This refutes:

```text
LOW-ORDER-MOMENTS:
a bounded number of cyclic moments uniformly certifies WFE-CYCLIC-TAIL.
```

### Zeta, deep run

| R | depth | steps for 1e-2 | steps for 1e-8 | final rel error | final fp/delta |
|---:|---:|---:|---:|---:|---:|
| 14 | 32 | 27 | 32 | 1.03e-24 | 1.000000 |
| 16 | 32 | 32 | 32 | 5.94e-18 | 1.000000 |

The finite cyclic Lanczos route is not false: with enough depth it recovers
the exact self-energy and the correct fixed point.  But the needed depth is
itself the new resolution problem.

### Planted build

| R | 14-step rel error | steps for 1e-8 | final fp/delta |
|---:|---:|---:|---:|
| 8  | 3.54e-71 | 7 | 0.0 |
| 10 | 8.99e-71 | 6 | 1.0 |
| 12 | 9.64e-71 | 7 | 1.0 |
| 14 | 2.75e-71 | 7 | 1.0 |
| 16 | 1.82e-70 | 7 | 1.0 |

The planted build is easier for cyclic Lanczos after the finite resonance.
This is not a proof discriminator for `A`; it is a diagnostic of where the
zeta critical window is spectrally hidden.

## 4. Autopsy

`CYCLIC-WINDOW-MASS` is not closed by low-order moments.

The obstruction is now exact:

```text
MOMENT-RESOLUTION:
the cyclic measure has decisive mass in windows so narrow that a fixed
number of moments cannot resolve them; m_R must grow cofinally with the
Ritz/window scale.
```

The failure is not numerical roundoff.  In the deep zeta run, the same
finite matrix is recovered to `1e-18--1e-24` once the Lanczos depth reaches
the relevant cyclic dimension.

The next strictly smaller object is:

```text
KRYLOV-WINDOW-RESOLUTION:
prove a deterministic relation between the required window scale eta_R and
the Lanczos depth m_R, giving a certified Stieltjes upper bracket
U_R^(m_R)(eta_R) with m_R cofinal and eta_R small enough for
BRACKETED-LOW-MODE-BTG.
```

Then

```text
KRYLOV-WINDOW-RESOLUTION
=> LANCZOS-RESOLUTION-ENVELOPE
=> CYCLIC-WINDOW-MASS
=> WFE-CYCLIC-TAIL
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.
```

## 5. Status

```text
proved:    finite cyclic Lanczos/Stieltjes identity (L-1);
proved:    LANCZOS-RESOLUTION-ENVELOPE implies CYCLIC-WINDOW-MASS
           and the chain to BTG-DIV-L;
refuted:   fixed low-order cyclic moments as a uniform zeta proof;
observed:  zeta requires near-full cyclic resolution at R=14,16 in the run;
observed:  planted needs only 6--7 steps for 1e-8 in the measured windows;
open:      deterministic Krylov depth/window theorem;
open:      CYCLIC-WINDOW-MASS, WFE-CYCLIC-TAIL, RITZ-BRACKET,
           BRACKETED-LOW-MODE-BTG, BTG-DIV-L, corrected LP;
live:      KRYLOV-WINDOW-RESOLUTION.
```

