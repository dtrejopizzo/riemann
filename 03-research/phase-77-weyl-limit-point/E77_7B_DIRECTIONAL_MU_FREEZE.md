# E77.7b - Directional Mu-Freezing Gate

**Run:** 2026-07-18.

## 1. Why This Gate Is Necessary

Weyl LP is a statement for one fixed operator at one fixed real spectral
point `mu_L`.  The existing section energies were computed instead at the
moving finite ground points `mu_{L,N}`:

```text
S_N^mov=||x_N(mu_{L,N})||^2.
```

Therefore the observed growth of `S_N^mov` implies LP only after proving that
moving `mu_{L,N}` to a common `mu_L` preserves the canonical energies and the
selected safe Cauchy responses.  Pointwise convergence `mu_{L,N}->mu_L` alone
does not provide this, because the response may be resonant.

## 2. Exact Directional Identity

For

```text
A_N(mu)=H_{L,N}^{inner}-mu I,
A_N(mu)x_N(mu)=b_N,
```

the resolvent identity gives

```text
x_N(mu_N)-x_N(mu_L)
=(mu_N-mu_L) A_N(mu_N)^(-1)x_N(mu_L).          (MF-1)
```

The admissible target is not an ambient inverse norm.  Pair `(MF-1)` with
the selected Cauchy row before estimating:

```text
DIR-MU-FREEZE:
sup_{z in K}
 |r_z[x_N(mu_N)-x_N(mu_L)]|/|r_z x_N(mu_N)| -> 0,
```

together with block comparability

```text
c S_N(mu_N) <= S_N(mu_L) <= C S_N(mu_N)
```

on the parity/block subsequences used by R3.  `MU-LIMIT` without these
directional statements is insufficient.

## 3. Probe

Companion:

```text
E77_7b_mu_limit_probe.py
```

The probe uses the largest measured ground point `mu_{L,18}` only as a
numerical freezing reference.  It is not claimed to be the infinite-volume
limit.

Command:

```bash
python3 E77_7b_mu_limit_probe.py \
  --lambda 6 --max-modes 18 --dps 60
```

### Zeta

```text
mu_6  = 5.68e-23,
mu_12 = 2.40e-37,
mu_18 = 2.53e-49.
```

Across `N=6--17`, freezing at `mu_18` gives

```text
S_N(frozen)/S_N(moving) = 0.970--0.996,
max safe-transfer difference = 0.0021--0.0153.
```

This is compatible with directional freezing but is not a proof.

### Planted falsifier

The planted ground points drift toward the largest-section reference:

```text
mu_12=-1.70946,
mu_16=-1.74002,
mu_17=-1.74014,
mu_18=-1.74469.
```

Nevertheless freezing is strongly resonance-sensitive:

| N | `|mu_N-mu_18|` | frozen/moving energy | safe-transfer difference |
|---:|---:|---:|---:|
| 12 | 3.52e-2 | 4.95e-2 | 0.782 |
| 14 | 2.05e-2 | 1.16e-3 | 0.961 |
| 16 | 4.68e-3 | 2.42e-1 | 0.506 |
| 17 | 4.55e-3 | 6.84e-4 | 0.972 |

Thus numerical convergence of the points does not imply convergence of the
selected responses on the measured sections.

## 4. Consequence for the LP Ledger

The quantities in E77.1/E77.1b are moving-point diagnostics.  Until
`DIR-MU-FREEZE` is proved, they cannot be identified with Weyl-disk radii of
one fixed semi-infinite operator.  This does not invalidate their empirical
zeta/plant separation; it corrects their theorem-level attribution.

The R3 implication is now:

```text
MU-LIMIT
+ DIR-MU-FREEZE
+ FIXED-MU-BLOCK-GROWTH
=> fixed-L Weyl-disk contraction
=> LP.
```

For the radical interface one must additionally prove

```text
SHELL-CAUCHY-GROWTH.
```

## 5. Falsifier Reading

E77.6 predicted that the plant should ultimately pass qualitative fixed-L LP
and fail arithmetic identification.  The present finite resonance does not
refute that prediction.  It shows only that the existing moving-point probe
does not yet test fixed-point LP for the plant.  The E77.8 location rule must
be applied after directional freezing, not before it.

## 6. Status

```text
proved:    exact paired mu-shift identity (MF-1);
observed:  zeta moving/frozen responses differ by at most 1.53% in the run;
observed:  planted responses remain highly resonance-sensitive;
refuted:   bare mu_N convergence as sufficient for transferring S_N growth;
open:      existence of mu_L and DIR-MU-FREEZE;
open:      FIXED-MU-BLOCK-GROWTH and SHELL-CAUCHY-GROWTH;
next:      derive DIR-MU-FREEZE from a selected Cauchy pairing, never from
           an ambient inverse norm.
```

