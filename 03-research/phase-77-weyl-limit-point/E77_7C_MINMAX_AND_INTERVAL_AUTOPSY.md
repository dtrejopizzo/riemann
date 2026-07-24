# E77.7c - Min-Max Closure Gate and Real-Interval Autopsy

**Run:** 2026-07-18.

## 1. Finite Min-Max Theorem

Let `H_N=P_N H P_N` be nested Hermitian compressions and

```text
mu_N=lambda_min(H_N).
```

Cauchy interlacing, equivalently the Rayleigh--Ritz principle, gives

```text
mu_{N+1}<=mu_N.                                 (MM-1)
```

Hence `mu_N` always has a limit in the extended real line.  If `H` is a
lower-semibounded self-adjoint realization and the union of the finite
section spaces is a form core, then

```text
lim_N mu_N=inf spec(H).                         (MM-2)
```

Proof: `(MM-1)` gives a limit bounded below by `inf spec(H)`.  Density in the
form norm approximates every trial vector for the Rayleigh quotient by finite
vectors, giving the reverse inequality.  QED.

This proves the proposed min-max step once the common operator hypotheses are
available.  The current ledger states finite self-adjointness and quotes the
cell estimate `||Q_y||<=2(1-y/L)`, but it does not yet prove that the complete
fixed-L Gamma-prime matrix has a common lower-semibounded realization with
`c00` as a form core.  Therefore the honest status is

```text
proved:      finite monotonicity and the abstract min-max theorem;
remaining:   OP-REALIZATION, the fixed-L semibounded operator/form-core gate.
```

Without `OP-REALIZATION`, monotonicity permits `mu_N->-infinity`, so a finite
real `mu_L` cannot be declared solely from the finite matrices.

## 2. Corrected Quasiperiodic Operator Picture

E77.7 identifies

```text
H_L = long-range Hilbert/Loewner hopping
      + prime-frequency almost-periodic potential.
```

The base frequencies `{log p}` are rationally independent by unique
factorization.  The full set `{k log p}` is a finite integer module generated
by them, not a pairwise rationally independent set because powers of the same
prime are integer multiples.

This arithmetic is legitimate fixed-L input and does not propagate Euler data
into the critical strip.  It also does not imply LP.  Quasiperiodic potentials
can support point spectrum; the `1/(n-m)` long-range hopping and MR-1 must do
real work.  Pure-Hilbert absolutely continuous spectrum is not inherited for
free.

## 3. Proposed Uniform-Interval Shortcut

The proposed replacement for directional freezing was

```text
UNIFORM-INTERVAL-CONTRACTION:
inf_{mu in I} S_N(mu)->infinity
```

on a fixed real interval `I` around `mu_L`.  Together with `mu_N->mu_L`, this
would indeed absorb moving-point freezing.  E77.7c tests whether this is even
compatible with the finite real-resolvent geometry.

## 4. Probe

Companion:

```text
E77_7c_uniform_interval_probe.py
```

Command:

```bash
python3 E77_7c_uniform_interval_probe.py \
  --lambda 6 --max-modes 20 --dps 50 \
  --radius 0.05 --grid-size 21
```

The interval is centered at the largest-section reference.  The grid is a
falsifier, not a proof of any uniform statement.

### Zeta

The finite minima do not develop a growing lower envelope:

| N | minimum grid energy | maximum radius proxy |
|---:|---:|---:|
| 12 | 0.1567 | 6.380 |
| 14 | 9.0412 | 0.1106 |
| 16 | 0.6819 | 1.466 |
| 18 | 1.6898 | 0.5918 |
| 19 | 8.6587 | 0.1155 |
| 20 | 0.5589 | 1.789 |

### Planted build

The same resonance-and-valley behavior remains:

| N | minimum grid energy | maximum radius proxy |
|---:|---:|---:|
| 12 | 3.2457 | 0.3081 |
| 14 | 0.3975 | 2.516 |
| 16 | 1.3829 | 0.7231 |
| 17 | 0.2543 | 3.933 |
| 19 | 4.7966 | 0.2085 |
| 20 | 0.6140 | 1.629 |

The real resolvent has poles and intervening valleys.  Poles increase
canonical energy but do not force its infimum over a fixed real interval to
grow.  Thus the proposed shortcut is not supported even for zeta and cannot
replace `DIR-MU-FREEZE` as stated.

## 5. Falsifier-Location Tension

The `97%` planted discrepancy in E77.7b is not yet an A-link failure because
the freezing reference was finite and the asymptotic fixed-point problem has
not been constructed.  The present extension to `N=20` still shows strong
real-axis valleys, so transience is not established either.

The audit rule is therefore suspended at this sublink, not changed:

```text
if OP-REALIZATION + fixed-point LP hold for the plant,
the required first arithmetic break remains B;

if the plant persistently fails fixed-point LP/freezing,
Outcome A is false and the A-link must undergo the E72.16 zero-filter audit
before it can be used as an arithmetic discriminator.
```

No conclusion about the break location is licensed by the current finite
resonances.

## 6. Corrected R3 Chain

```text
OP-REALIZATION
=> MU-LIMIT by min-max

DIR-MU-FREEZE
+ FIXED-MU-BLOCK-GROWTH
=> LP

+ SHELL-CAUCHY-GROWTH
=> RDP-SHELL interface.
```

MR-1 is now the effective transfer recurrence for long-range hopping in the
prime almost-periodic potential.  The next proof must exploit that coupled
recurrence; it may not discard `(AT-1)` or replace it by a compact tail.

## 7. Status

```text
proved:    nested finite ground values are monotone by min-max;
proved:    conditional MM-2 under semibounded realization/form-core;
observed:  mu_N is monotone in both builds through N=20;
refuted:   fixed real-interval contraction as a supported freeze shortcut;
open:      OP-REALIZATION for the full fixed-L Gamma-prime matrix;
open:      DIR-MU-FREEZE and FIXED-MU-BLOCK-GROWTH;
next:      prove OP-REALIZATION from the Loewner commutator plus bounded
           sampled diagonal, then return to MR-1 block growth.
```

