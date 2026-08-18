# E77.7h - WFE cyclic tail profile

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced `RITZ-BRACKET` to a weighted Feshbach envelope for the
coupling spectral measure

```text
alpha_R=sum_l |<w_l,h_R>|^2 delta_{omega_l}.
```

This note probes the next live object:

```text
WFE-CYCLIC-TAIL:
construct a certified cyclic majorant for alpha_R that makes the
self-energy fixed point eta_R -> 0 and is small enough for
BRACKETED-LOW-MODE-BTG.
```

The result is a sharper reduced target, not a closure.

## 2. Windowed cyclic envelope

Write

```text
kappa_l=omega_l-mu_R,
Sigma_R(eta)=sum_l |c_l|^2/(kappa_l+eta).
```

The Feshbach bracket follows if one proves, for a cofinal `R=R(N)`, an
`eta_R -> 0` such that

```text
Sigma_R(eta_R) <= eta_R,
K_R-(mu_R-eta_R) positive on the h_R-cyclic support.        (W-1)
```

The admissible proof-facing majorant is windowed:

```text
CYCLIC-WINDOW-ENVELOPE:
partition the kappa-axis into windows I_q(R), certify masses

A_q(R) >= alpha_R(I_q(R)),
d_q(eta_R) <= inf_{kappa in I_q(R)} (kappa+eta_R),

with d_q(eta_R)>0 and

sum_q A_q(R)/d_q(eta_R) <= eta_R.             (W-2)
```

Then `(W-2)` implies `(W-1)`, hence

```text
CYCLIC-WINDOW-ENVELOPE
=> WEIGHTED-FESHBACH-ENVELOPE
=> RITZ-BRACKET
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> fixed-mu block growth
=> corrected Weyl-disk contraction.           (W-3)
```

This is still a convergence/identity statement.  It does not use Weil
positivity, a zero filter, a pseudoinverse, or an ambient bordered inverse.

## 3. Why the windowing is necessary

Two crude routes are now ruled out:

```text
1. min spec(K_R)-mu_R > 0;
2. ||h_R||^2 / dist(mu_R-eta,spec K_R).
```

In zeta finite sections, `min spec(K_R)-mu_R` is negative at the Ritz-shift
scale.  Yet the negative spectral mass of the actual coupling vector is
tiny.  Therefore the correct object is not complement positivity, but
negative-window mass suppression plus positive-window mass bounds.

In planted sections, after the small `R=8` resonance, the negative window is
empty but the same weighted fixed-point algebra holds.  Thus this front
remains falsifier-neutral.

## 4. Probe

Companion:

```text
E77_7h_wfe_cyclic_tail_probe.py
E77_7h_wfe_cyclic_tail_results.json
```

Command:

```bash
python3 E77_7h_wfe_cyclic_tail_probe.py \
  --lambda 6 --max-modes 18 --refs 8,10,12,14,16 --dps 70
```

The probe diagonalizes the finite complement, computes the cyclic spectral
measure, and reports:

```text
negative mass fraction;
negative self-energy fraction at eta=delta;
number of top contributors needed for 50/90/99/99.9 percent;
window mass/self-energy fractions for kappa <= delta, sqrt(delta),
delta^(1/4), 1;
Sigma(2 delta)/(2 delta), Sigma(4 delta)/(4 delta), Sigma(10 delta)/(10 delta).
```

### Zeta

| R | delta | negative self frac | contributors for 90% | Sigma(2d)/(2d) |
|---:|---:|---:|---:|---:|
| 8  | 3.6786e-28 | 4.78e-8  | 6 | 0.500000 |
| 10 | 8.9295e-33 | 3.76e-7  | 5 | 0.500000 |
| 12 | 2.4032e-37 | 3.76e-6  | 4 | 0.499998 |
| 14 | 1.7090e-41 | 2.96e-5  | 3 | 0.499985 |
| 16 | 1.5411e-45 | 4.18e-64 | 2 | 0.499847 |

The negative spectral window is harmless in the measured zeta runs, despite
the minimum complement eigenvalue lying below `mu_R`.  The self-energy is
strongly cyclic: by `R=16`, two complement modes give 90 percent and four
give 99.9 percent.

The positive-window profile is also sharp.  At `R=16`,

```text
kappa <= sqrt(delta): mass fraction ~4.38e-14,
self-energy fraction ~0.999998.
```

So mass is tiny but placed at the exact denominators that matter.  Total
mass estimates discard this structure.

### Planted build

| R | delta | negative self frac | contributors for 90% | Sigma(2d)/(2d) |
|---:|---:|---:|---:|---:|
| 8  | 1.0243    | 0.8467 | 2 | 0.269840 |
| 10 | 1.0071e-1 | 0      | 3 | 0.477151 |
| 12 | 3.5234e-2 | 0      | 4 | 0.491667 |
| 14 | 2.0548e-2 | 0      | 3 | 0.495415 |
| 16 | 4.6750e-3 | 0      | 2 | 0.498920 |

The plant has the expected early resonance at `R=8`; after that the algebra
looks just as benign.  This confirms the intended audit: `A` does not
separate the builds.

## 5. Autopsy

`WFE-CYCLIC-TAIL` is not closed here.  The finite profile identifies the
missing theorem:

```text
NEG-WINDOW:
alpha_R({kappa<0}) is small enough relative to eta_R-rho_R.

POS-WINDOW:
for positive windows I_q(R), alpha_R(I_q(R)) is bounded at the scale needed
by A_q/d_q, not merely by total ||h_R||^2.
```

The finite data suggest that only a few cyclic modes dominate, but a proof
cannot name finite eigenmodes of the truncation as the mechanism.  The
proof-facing object must be stated in terms of certified windows or moments
of the cyclic measure, constructed from `D+B` and the exact Hilbert/cell
entries.

The next strictly smaller object is:

```text
CYCLIC-WINDOW-MASS:
Build explicit windows I_q(R) and certified mass bounds A_q(R) for the
h_R-cyclic spectral measure of K_R such that the inequality (W-2) has a
solution eta_R -> 0 and the E77.7h bracketed low-mode denominator still
diverges.
```

Then

```text
CYCLIC-WINDOW-MASS
=> CYCLIC-WINDOW-ENVELOPE
=> WFE-CYCLIC-TAIL
=> BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> corrected LP.
```

## 6. Status

```text
proved:    CYCLIC-WINDOW-ENVELOPE implies WFE and RITZ-BRACKET;
proved:    WFE plus bracketed low-mode divergence implies BTG-DIV-L
           and corrected Weyl-disk contraction;
observed:  zeta negative-window self-energy fraction is tiny in the run;
observed:  zeta self-energy is concentrated in very few cyclic modes;
observed:  Sigma(2 delta)/(2 delta) is ~1/2 for both builds after resonance;
observed:  planted remains A-neutral except for expected finite resonance;
refuted:   total mass/gap and positive complement gap as sufficient proof
           mechanisms;
open:      certified infinite cyclic window mass bounds;
open:      WFE-CYCLIC-TAIL, RITZ-BRACKET, BRACKETED-LOW-MODE-BTG,
           BTG-DIV-L, corrected LP;
live:      CYCLIC-WINDOW-MASS.
```

