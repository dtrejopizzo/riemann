# E77.5g - Schur Phase Increment Audit

## Objective

E77.5f closed the exact 2x2 shell-resolvent identity

```text
T_N(z)=t0_N(z)-tau_N(z) Sigma_N^{-1} kappa_N
      =t0_N(z)(1-theta_N(z)),

theta_N(z)=tau_N(z) Sigma_N^{-1} kappa_N/t0_N(z).
```

E77.5g asks whether the remaining shell regularity can be placed directly
on `theta_N`.  The measured quantities are:

```text
log(1-theta_N(i sigma)),
2 Re(i d_z log(1-theta_N(i sigma))),
Delta_N theta_N,
Delta_N log(1-theta_N),
Delta_N 2 Re(i d_z log(1-theta_N)).
```

The derivative quantity is the shell component that enters the safe
logarithmic derivative.  The raw phase is recorded modulo `2*pi`, so
principal-branch jumps are not mistaken for mathematical discontinuities.

## Probe

Artifacts:

```text
E77_5g_schur_phase_increment_probe.py
E77_5g_schur_phase_increment_results.json
E77_5g_smoke_results.json
```

Main command:

```bash
python3 E77_5g_schur_phase_increment_probe.py --lambda 6 --max-modes 22 --dps 100 --output E77_5g_schur_phase_increment_results.json
```

Falsifier:

```text
gamma=14.134725141734693790, beta=0.30, strength=5.0
```

No zero locations are used except this declared planted falsifier.  The
probe uses finite Schur solves and paired Cauchy quantities only; no
pseudoinverse, ambient inverse norm, Weil positivity, or absolute
pre-cancellation estimate is invoked.

## Increment Table

Max over `sigma in {0.55,0.6,0.75,1,1.5,2,3}`.

| build | step | max abs Delta safe deriv | max abs Delta theta | max wrapped phase |
|---|---:|---:|---:|---:|
| zeta | 8 -> 10 | 0.028139077 | 0.068445728 | 0.002837678 |
| zeta | 10 -> 12 | 0.012798196 | 0.053619596 | 0.001553755 |
| zeta | 12 -> 14 | 0.0086700075 | 0.023515542 | 0.00014575867 |
| zeta | 14 -> 16 | 0.0045648659 | 0.022835206 | 0.0034168284 |
| zeta | 16 -> 18 | 0.0036380721 | 0.017264103 | 0.0032474275 |
| zeta | 18 -> 20 | 0.0022451578 | 0.015438585 | 0.00069777947 |
| zeta | 20 -> 22 | 0.0013905120 | 0.0067492443 | 0.0053686272 |
| planted | 8 -> 10 | 0.35272356 | 2.8023251 | 0.091512764 |
| planted | 10 -> 12 | 0.056742761 | 1.8421061 | 0.16197231 |
| planted | 12 -> 14 | 0.0029845392 | 3.6679515 | 0.012561442 |
| planted | 14 -> 16 | 0.00075684366 | 7.2624973 | 0.013857324 |
| planted | 16 -> 18 | 0.00083830139 | 1.8386094 | 0.011477036 |
| planted | 18 -> 20 | 0.00065764176 | 1.9241482 | 0.0097090455 |
| planted | 20 -> 22 | 0.00056728562 | 1.9757430 | 0.010241891 |

## Section Table

| build | N | max abs theta | min abs one-minus-theta | max safe shell deriv |
|---|---:|---:|---:|---:|
| zeta | 8 | 1.3437864 | 0.32669749 | 0.068252524 |
| zeta | 10 | 1.2753408 | 0.26729995 | 0.040113447 |
| zeta | 12 | 1.2217213 | 0.21731894 | 0.027315251 |
| zeta | 14 | 1.1982058 | 0.19551977 | 0.018645243 |
| zeta | 16 | 1.1753709 | 0.17357737 | 0.014080377 |
| zeta | 18 | 1.1581070 | 0.15690802 | 0.010442305 |
| zeta | 20 | 1.1426685 | 0.14181940 | 0.0081971472 |
| zeta | 22 | 1.1359206 | 0.13524917 | 0.0068066353 |
| planted | 8 | 1.3217474 | 2.0263367 | 0.41021980 |
| planted | 10 | 4.0009250 | 4.8140579 | 0.057496232 |
| planted | 12 | 5.5388467 | 6.5239242 | 0.0025192588 |
| planted | 14 | 9.1905982 | 10.181219 | 0.0013894518 |
| planted | 16 | 1.9281952 | 2.9272727 | 0.00063260819 |
| planted | 18 | 0.089759551 | 1.0895715 | 0.00020569320 |
| planted | 20 | 2.0137199 | 3.0128006 | 0.00045194856 |
| planted | 22 | 0.038081819 | 1.0379767 | 0.00011533706 |

## Reading

The first candidate criterion,

```text
small Delta of the safe shell derivative,
```

is not an arithmetic discriminator.  The planted build also makes this
quantity small in late windows.  Therefore E77.5g autopsies that criterion:
derivative smallness is a quotient-level cancellation that can occur after
the off-line plant has already destroyed the Schur geometry.

The stricter finite object survives:

```text
THETA-REG:
  theta_N(i sigma) is Cauchy with a summable envelope on sigma-compacts.
```

On the tested window, zeta has coherent decreasing increments:

```text
max |Delta theta|: 0.0684, 0.0536, 0.0235, 0.0228,
                   0.0173, 0.0154, 0.00675.
```

The planted falsifier fails this object decisively:

```text
max |Delta theta|: 2.80, 1.84, 3.67, 7.26, 1.84, 1.92, 1.98.
```

The wrapped phase gives a secondary check: zeta stays below `0.0054`, while
planted initially jumps by `0.09` and `0.16`, then remains about
`0.01`.  Phase alone is not enough, but it is consistent with the
`theta_N` instability verdict.

## Status

```text
proved:    no IDENT theorem and no Omega7 closure;
proved:    derivative-smallness is not an admissible discriminant, because
           the planted build can satisfy it in late finite windows;
observed:  zeta theta_N increments decrease to 0.00675 by N=22;
observed:  planted theta_N increments remain O(1) and oscillatory;
reduced:   SHELL-REG -> THETA-REG;
next:      E77.5h factor decomposition of Delta theta into tau, Sigma,
           kappa, and t0.
```

## Next Theorem Target

E77.5h should identify which finite factor carries `THETA-REG`:

```text
Delta theta
= Delta( tau Sigma^{-1} kappa / t0 )
```

The desired output is a factor-level theorem:

```text
FACTOR-REG:
  one of tau, Sigma^{-1}kappa, or t0 has the signed/coherent zeta
  regularity that planted lacks.
```

Then:

```text
FACTOR-REG => THETA-REG => SHELL-REG => DELTA-ENVELOPE
=> SR-LOG-2SCALE => IDENT.
```
