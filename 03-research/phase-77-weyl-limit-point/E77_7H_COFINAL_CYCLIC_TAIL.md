# E77.7h - Cofinal cyclic-tail audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7h left the live object:

```text
COFINAL-CYCLIC-TAIL:
after capturing finite Lanczos/Ritz clusters, prove that the remaining
h_R-cyclic spectral tail is harmless in the Stieltjes norm at eta_R.
```

This note tests whether the finite pole-capture picture is stable as the
outer section `M` grows with fixed Ritz reference `R`.

The answer is:

```text
the Stieltjes value is stable for zeta, but the dominant pole labels are
not stable.  Therefore cofinal control must be stated at the level of the
total Stieltjes value or shell tail, not by tracking individual poles.
```

No closure of `BTG-DIV-L`, `LP`, or `Omega7` is claimed.

## 2. Cofinal tail formulation

For fixed `R`, let `K_{R,M}` and `h_{R,M}` be the complement and cyclic
coupling vector inside outer section `M`.  Define

```text
Sigma_{R,M}(eta)
= <h_{R,M},(K_{R,M}-mu_R+eta)^(-1)h_{R,M}>.
```

The proof-facing object should be:

```text
COFINAL-STIELTJES-TIGHTNESS:
construct eta_R -> 0 and M(R) cofinal such that

1. Sigma_{R,M}(eta_R) is Cauchy for M >= M(R);
2. the tail difference
   |Sigma_{R,M'}(eta_R)-Sigma_{R,M}(eta_R)|
   is o(eta_R) in the bracket relation;
3. the resulting eta_R remains small enough for
   BRACKETED-LOW-MODE-BTG.
```

Then

```text
COFINAL-STIELTJES-TIGHTNESS
=> COFINAL-CYCLIC-TAIL
=> POSTERIORI-POLE-CAPTURE
=> CYCLIC-POLE-CAPTURE
=> KRYLOV-WINDOW-RESOLUTION
=> LANCZOS-RESOLUTION-ENVELOPE
=> CYCLIC-WINDOW-MASS
=> WFE-CYCLIC-TAIL
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.                              (C-1)
```

This is a convergence statement for a cyclic Stieltjes transform.  It avoids
ambient inverse bounds, zero filters, pseudoinverses, and Weil positivity.

## 3. Probe

Companion:

```text
E77_7h_cofinal_cyclic_tail_probe.py
E77_7h_cofinal_cyclic_tail_results.json
E77_7h_cofinal_cyclic_tail_m20_results.json
```

Commands:

```bash
python3 E77_7h_cofinal_cyclic_tail_probe.py \
  --lambda 6 --max-list 16,18 --ref-modes 14 \
  --lanczos-steps 40 --top-k 6 --dps 60

python3 E77_7h_cofinal_cyclic_tail_probe.py \
  --lambda 6 --max-list 18,20 --ref-modes 14 \
  --lanczos-steps 44 --top-k 6 --dps 60 \
  --output E77_7h_cofinal_cyclic_tail_m20_results.json
```

The probe measures `Sigma` stability, `delta` stability, effective cyclic
dimension, top-pole drift, and top captured contribution.

### Zeta

| outer M | delta | Sigma ratio to previous M | top8/exact | poles for 99.9% |
|---:|---:|---:|---:|---:|
| 16 | 1.7089e-41 | NA | 0.958792 | 26 |
| 18 | 1.7090e-41 | 1.00009018 | 0.994800 | 28 |
| 20 | 1.7090e-41 | 1.000000015 | 0.998734 | 30 |

The value is stabilizing very quickly: from `M=18` to `M=20`, the measured
ratio is `1+1.48e-8`.  However the dominant pole identities drift strongly.
From `M=18` to `M=20`, the top zeta pole fraction moves from roughly
`.635` at `kappa~1.11e-28` to `.369` at `kappa~5.04e-28`, and another
large contribution appears near `kappa~2.38e-20`.

Thus tracking named finite poles is not cofinal proof data.  The stable
object is the total Stieltjes value.

### Planted build

| outer M | delta | Sigma ratio to previous M | top8/exact | poles for 99.9% |
|---:|---:|---:|---:|---:|
| 16 | 0.0158730 | NA | 0.99999989 | 6 |
| 18 | 0.0205480 | 1.2945247 | 0.99999791 | 6 |
| 20 | 0.0252342 | 1.2280587 | 0.99992958 | 8 |

The planted finite value still moves with `M` at this scale.  This does not
violate the front-A rule: the algebraic mechanism remains available to the
plant, but the cofinal behavior has not stabilized in this short window.

## 4. Autopsy

`COFINAL-CYCLIC-TAIL` is not closed by finite pole tracking.

The failed assumption is:

```text
dominant finite Ritz/Lanczos pole labels persist cofinally.
```

The zeta data refute that assumption as a proof mechanism: `Sigma` is stable
while the finite pole labels reorganize.  A proof must instead estimate the
shell change in the cyclic Stieltjes value directly:

```text
SHELL-STIELTJES-INCREMENT:
Delta_M Sigma_R(eta)
= Sigma_{R,M+2}(eta)-Sigma_{R,M}(eta)
```

in the paired/cyclic topology.  This is the exact analogue of the P76.061
lesson: control the paired scalar quantity before taking absolute ambient
norms.

The next strictly smaller live object is:

```text
SHELL-STIELTJES-INCREMENT:
derive a resolvent identity for Delta_M Sigma_R(eta_R) in terms of the new
outer shell rows/columns and prove its sum over M is o(eta_R) along a
cofinal M(R).
```

Then

```text
SHELL-STIELTJES-INCREMENT
=> COFINAL-STIELTJES-TIGHTNESS
=> COFINAL-CYCLIC-TAIL
=> ... => BTG-DIV-L => corrected LP.
```

## 5. Status

```text
proved:    COFINAL-STIELTJES-TIGHTNESS implies the chain to BTG-DIV-L;
observed:  zeta Sigma_{R,M} is very stable from M=18 to M=20 at R=14;
observed:  zeta finite pole labels are not stable cofinally;
observed:  planted remains algebraically admissible but not stabilized in
           this short M-window;
refuted:   tracking individual finite dominant poles as the cofinal proof;
open:      shell-level Stieltjes increment estimate;
open:      COFINAL-CYCLIC-TAIL, CYCLIC-POLE-CAPTURE,
           KRYLOV-WINDOW-RESOLUTION, CYCLIC-WINDOW-MASS,
           WFE-CYCLIC-TAIL, RITZ-BRACKET, BRACKETED-LOW-MODE-BTG,
           BTG-DIV-L, corrected LP;
live:      SHELL-STIELTJES-INCREMENT.
```

