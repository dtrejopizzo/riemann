# E77.7h - Shorted shell-energy anatomy

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced shell summability to the scalar shorted energy

```text
<r,S^{-1}r>,
r=g-C^*A^{-1}h.
```

This note audits whether the zeta smallness comes from a benign Schur
denominator, from small shell source norm, or from cancellation in the
shorted residual `r`.

The answer is:

```text
zeta smallness is residual cancellation:
g and C^*A^{-1}h nearly coincide in the shell coordinates.
```

## 2. Anatomy

Recall the shell decomposition

```text
K_{M+2}-z =
[[A, C],
 [C^*, D]],

h_{M+2}=(h,g),
S=D-C^*A^{-1}C,
r=g-C^*A^{-1}h.
```

The shell increment is exactly

```text
Delta_M Sigma(eta)=<r,S^{-1}r>.              (E-1)
```

Expanding the residual gives

```text
<r,S^{-1}r>
=<g,S^{-1}g>
 +<C^*A^{-1}h,S^{-1}C^*A^{-1}h>
 -2<g,S^{-1}C^*A^{-1}h>.                     (E-2)
```

Thus the proof-facing target is not separate control of `g`, `A^{-1}`, or
`S^{-1}`.  It is the cancellation in the shell residual before norms are
taken.

## 3. Probe

Companion:

```text
E77_7h_shorted_shell_energy_probe.py
E77_7h_shorted_shell_energy_results.json
```

Command:

```bash
python3 E77_7h_shorted_shell_energy_probe.py \
  --lambda 6 --max-modes 20 --pairs 16:18,18:20 \
  --ref-modes 14 --dps 60
```

The probe measures direct shell source `g`, mediated source `C^*A^{-1}h`,
residual `r`, angle/cosine, Schur condition, and the loss from the crude
bound

```text
||r||^2 / lambda_min(S).
```

### Zeta

| shell | energy/eta | ||r||/max(||g||,||med||) | cos(g,med) | crude/energy |
|---:|---:|---:|---:|---:|
| 16 -> 18 | 9.02e-5 | 1.95e-5 | 0.9999999999993 | 4.82e7 |
| 18 -> 20 | 1.48e-8 | 2.03e-9 | 0.999999999999999999 | 2.29e6 |

The direct and mediated shell vectors are almost identical:

```text
16 -> 18: ||g|| ~ 6.7344e-26, ||med|| ~ 6.7343e-26,
          ||r|| ~ 1.3103e-30.

18 -> 20: ||g|| ~ 1.5341e-24, ||med|| ~ 1.5341e-24,
          ||r|| ~ 3.1136e-33.
```

The crude residual norm over `lambda_min(S)` still loses millions, so even
after cancellation one should keep the scalar pairing intact.

### Planted build

| shell | energy/eta | ||r||/max(||g||,||med||) | cos(g,med) | crude/energy |
|---:|---:|---:|---:|---:|
| 16 -> 18 | 0.2292 | 0.8121 | 0.5838 | 1.22 |
| 18 -> 20 | 0.1874 | 1.4679 | -0.6679 | 2.46 |

The planted build lacks the zeta shell cancellation in this window.  This is
a detector of the arithmetic structure, not by itself a proof of the chain.

## 4. Reduced Target

The next admissible object is:

```text
SHELL-RESIDUAL-CANCELLATION:
prove directly, from the exact Hilbert/cell/Gamma-prime shell update, that

r_{R,M}=g_{R,M}-C_{R,M}^*A_{R,M}^{-1}h_{R,M}

is small in the shorted pairing:

sum_M <r_{R,M},S_{R,M}^{-1}r_{R,M}> = o(eta_R).
```

Then

```text
SHELL-RESIDUAL-CANCELLATION
=> SHORTED-SHELL-ENERGY
=> SHELL-RESIDUAL-SUM
=> SHELL-STIELTJES-INCREMENT
=> COFINAL-STIELTJES-TIGHTNESS
=> COFINAL-CYCLIC-TAIL
=> ... => BTG-DIV-L => corrected LP.          (E-3)
```

This is exactly the P76.061-safe shape: the source is paired with the
shorted response before an estimate is made.

## 5. Autopsy

`SHORTED-SHELL-ENERGY` is not closed here.  The probe identifies the
load-bearing cancellation, but no infinite theorem proves it yet.

The failed easy routes are:

```text
1. bound ||g|| alone;
2. bound ||C^*A^{-1}h|| alone;
3. use ||r||^2/lambda_min(S) as the final estimate.
```

All three lose the structure.  The theorem must prove cancellation in
`r=g-C^*A^{-1}h`, preferably using the shell Schur identity together with
the finite cell/Hilbert product rule already established in earlier phase
77 notes.

## 6. Status

```text
proved:    energy expansion (E-2) and implication (E-3);
observed:  zeta shell residual cancellation improves from ~1e-5 to ~1e-9
           over the two measured shells;
observed:  planted does not show this cancellation in the same window;
refuted:   separate source/mediated/vector-norm estimates as sufficient;
open:      theorem-grade shell residual cancellation;
open:      SHORTED-SHELL-ENERGY, SHELL-STIELTJES-INCREMENT,
           COFINAL-CYCLIC-TAIL, CYCLIC-POLE-CAPTURE,
           KRYLOV-WINDOW-RESOLUTION, CYCLIC-WINDOW-MASS,
           WFE-CYCLIC-TAIL, RITZ-BRACKET, BRACKETED-LOW-MODE-BTG,
           BTG-DIV-L, corrected LP;
live:      SHELL-RESIDUAL-CANCELLATION.
```

