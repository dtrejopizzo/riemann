# E77.7h - Cyclic pole-capture audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced the zeta difficulty to:

```text
CYCLIC-POLE-CAPTURE:
Lanczos/Ritz poles in the h_R-cyclic Krylov subspace capture the
Stieltjes-dominant windows of alpha_R, with a certified residual tail.
```

This note tests whether the capture seen in E77.7h can be certified by
posteriori Ritz residuals.

The finite answer is yes at the measured depth.  The infinite theorem is
still open: one must control the cofinal cyclic tail.

## 2. Posteriori certificate

For an `m`-step Lanczos tridiagonal `T_m`, a Ritz pair `(theta_j,s_j)` has
residual in the original complement bounded by

```text
res_j = beta_m |s_j(m)|.
```

Thus there is spectrum of `K_R` in

```text
[theta_j-res_j, theta_j+res_j].
```

If such intervals are separated and the corresponding cyclic weights are
controlled, their Stieltjes contributions can be bracketed by

```text
weight_j / (theta_j-mu_R+eta-res_j).
```

This gives the admissible finite mechanism:

```text
POSTERIORI-POLE-CAPTURE:
dominant Ritz poles have small residual intervals, separated clusters, and
the unclustered cyclic tail has a certified Stieltjes upper bound.
```

Then

```text
POSTERIORI-POLE-CAPTURE
=> CYCLIC-POLE-CAPTURE
=> KRYLOV-WINDOW-RESOLUTION
=> LANCZOS-RESOLUTION-ENVELOPE
=> CYCLIC-WINDOW-MASS
=> WFE-CYCLIC-TAIL
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.                              (P-1)
```

The missing item in `(P-1)` is the cyclic weight/tail certificate, not pole
location in the finite run.

## 3. Probe

Companion:

```text
E77_7h_cyclic_pole_capture_probe.py
E77_7h_cyclic_pole_capture_results.json
```

Command:

```bash
python3 E77_7h_cyclic_pole_capture_probe.py \
  --lambda 6 --max-modes 18 --refs 14,16 \
  --lanczos-steps 32 --dps 70
```

The probe computes:

```text
Ritz pole locations and cyclic weights;
residual widths beta_m |s_j(m)|;
nearest Ritz gaps;
angle proxy res_j/gap_j;
captured contribution counts;
partial interval upper sums for top captured poles.
```

### Zeta

| R | dim | rel error Sigma(delta) | beta_out | poles for 90% | max angle proxy |
|---:|---:|---:|---:|---:|---:|
| 14 | 32 | 1.03e-24 | 0 | 3 | 0 |
| 16 | 32 | 5.94e-18 | 0 | 2 | 0 |

At `R=16`, the two leading Ritz poles are:

```text
kappa ~= 4.9846781244e-38, fraction .88168;
kappa ~= 3.2190017703e-43, fraction .06444.
```

The residual interval width is zero at the working precision because the
32-step cyclic subspace closes for this finite section.  The top-eight
captured interval contribution accounts for

```text
R=14: 0.9999928233 of exact Sigma(delta);
R=16: 0.999999999897 of exact Sigma(delta).
```

### Planted build

| R | dim | rel error Sigma(delta) | beta_out | poles for 90% | max angle proxy |
|---:|---:|---:|---:|---:|---:|
| 14 | 32 | 1.38e-71 | 0 | 3 | 0 |
| 16 | 32 | 2.72e-70 | 0 | 2 | 0 |

The plant again passes the finite algebraic capture audit.  This is
consistent with the front-A rule: no proof step here should filter the
planted build by sign or by its off-line divisor.

## 4. Autopsy

The finite posteriori pole-capture mechanism works in the measured sections,
but it does not close the infinite theorem.

The exact remaining obstruction is:

```text
COFINAL-CYCLIC-TAIL:
after capturing the dominant Ritz/Lanczos clusters at depth m_R, prove that
the remaining h_R-cyclic spectral measure contributes o(eta_R), uniformly
en the cofinal relation R=R(N).
```

This is stricter than observing finite `beta_out=0`.  In finite sections the
cyclic subspace can close because the matrix is finite and the vector may
generate only a finite-dimensional invariant subspace to working precision.
The proof must show that the uncaptured infinite cyclic tail remains harmless
in the Stieltjes bracket used by WFE.

The next live object is therefore:

```text
COFINAL-CYCLIC-TAIL:
certify the residual h_R-cyclic spectral tail beyond the captured
Lanczos/Ritz clusters, in the Stieltjes norm at eta_R.
```

Then

```text
COFINAL-CYCLIC-TAIL
=> POSTERIORI-POLE-CAPTURE
=> CYCLIC-POLE-CAPTURE
=> ... => BTG-DIV-L => corrected LP.
```

This remains safely on the convergence/identity side of the architecture.
No ambient inverse norm, pseudoinverse, zero filter, or Weil positivity is
used.

## 5. Status

```text
proved:    POSTERIORI-POLE-CAPTURE implies the chain to BTG-DIV-L;
observed:  finite zeta pole capture at R=14,16 is exact to working
           precision at Lanczos depth 32;
observed:  finite plant pole capture is also exact to working precision;
observed:  top captured poles account for essentially all measured
           Sigma(delta);
refuted:   pole-location residuals as the only missing ingredient;
open:      cofinal infinite h_R-cyclic tail after captured clusters;
open:      CYCLIC-POLE-CAPTURE, KRYLOV-WINDOW-RESOLUTION,
           CYCLIC-WINDOW-MASS, WFE-CYCLIC-TAIL, RITZ-BRACKET,
           BRACKETED-LOW-MODE-BTG, BTG-DIV-L, corrected LP;
live:      COFINAL-CYCLIC-TAIL.
```

