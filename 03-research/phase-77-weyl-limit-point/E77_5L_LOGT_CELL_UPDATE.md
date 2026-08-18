# E77.5l - Safe Log-Transfer Cell Update

## Objective

E77.5k autopsied `theta_common`: the common-core Schur identity is exact,
but the coordinate `theta=correction/t0` depends on the chosen eliminated
core.  The invariant quantity in `SR-LOG-ERR` is instead

```text
2 Re(i T_N'(i sigma)/T_N(i sigma)).
```

E77.5l measures the moving-boundary/four-node update directly at this
partition-invariant level.

## Identity

For each consecutive step, use the common core

```text
{-N+2,...,N-2}
```

and the exact active-block transfer identity from E77.5k:

```text
T_N(z)=t0_N(z)-tau_N(z)S_N^{-1}k_N.
```

Then the section-error delta decomposes exactly as:

```text
E_N(sigma)-E_{N+2}(sigma)
 = Delta base
 + Delta 2 Re(i T'/T)
 - Delta external_tail.
```

For fixed `lambda`, `Delta base=0`, so the obstruction is the signed
difference:

```text
Delta external_tail - Delta logT.
```

This is the partition-invariant form of the E77.5e shell/external coupling.

## Probe

Artifacts:

```text
E77_5l_logt_cell_update_probe.py
E77_5l_logt_cell_update_results.json
E77_5l_smoke_results.json
```

Main command:

```bash
python3 E77_5l_logt_cell_update_probe.py --lambda 6 --max-modes 22 --dps 100 --output E77_5l_logt_cell_update_results.json
```

The probe verifies:

```text
common-core transfer identity;
error-delta reconstruction;
zeta/planted falsifier contrast.
```

No zero locations are used except the declared planted falsifier; no
positivity, pseudoinverse, ambient inverse norm, or absolute pre-cancellation
bound is used.

## Certification Table

Max over `sigma in {0.55,0.6,0.75,1,1.5,2,3}`.

| build | step | max Delta logT | max Delta external | max Delta error | log/ext | max transfer id |
|---|---:|---:|---:|---:|---:|---:|
| zeta | 8 -> 10 | 0.081483062 | 0.098201952 | 0.016718890 | 0.82974992 | 1.35e-77 |
| zeta | 10 -> 12 | 0.054427779 | 0.065329654 | 0.010901876 | 0.83312516 | 3.00e-72 |
| zeta | 12 -> 14 | 0.037823417 | 0.046607937 | 0.0087845201 | 0.81152309 | 3.01e-68 |
| zeta | 14 -> 16 | 0.028222719 | 0.034929753 | 0.0067070345 | 0.80798506 | 7.68e-64 |
| zeta | 16 -> 18 | 0.021152832 | 0.027154034 | 0.0060012026 | 0.77899407 | 4.65e-60 |
| zeta | 18 -> 20 | 0.016688765 | 0.021715651 | 0.0050268859 | 0.76851323 | 2.06e-56 |
| zeta | 20 -> 22 | 0.013787648 | 0.017762848 | 0.0039752000 | 0.77620705 | 4.26e-53 |
| planted | 8 -> 10 | 0.79060918 | 0.098201952 | 0.77260549 | 8.0508500 | 2.15e-101 |
| planted | 10 -> 12 | 0.031686732 | 0.065329654 | 0.057585672 | 0.48502831 | 2.01e-100 |
| planted | 12 -> 14 | 0.0038378826 | 0.046607937 | 0.043902506 | 0.082343972 | 6.23e-101 |
| planted | 14 -> 16 | 0.0045702951 | 0.034929753 | 0.031495622 | 0.13084247 | 2.08e-101 |
| planted | 16 -> 18 | 0.0014177834 | 0.027154034 | 0.026192799 | 0.052212627 | 1.74e-101 |
| planted | 18 -> 20 | 0.0015000270 | 0.021715651 | 0.020343089 | 0.069075850 | 5.55e-101 |
| planted | 20 -> 22 | 0.00062194380 | 0.017762848 | 0.017361602 | 0.035013744 | 2.23e-101 |

The error reconstruction is exact to roundoff:

```text
zeta:    0 in the stored precision;
planted: <= 3.48e-101.
```

## Reading

`LOGT-CELL` is the correct invariant formulation of the finite-section lag.
It reproduces the E77.5e shell/external anatomy without relying on a
partition-dependent theta coordinate.

For zeta, the safe log-transfer update tracks the explicit external tail:

```text
Delta logT / Delta external = 0.77--0.83.
```

The uncancelled error delta decreases:

```text
0.0167, 0.0109, 0.00878, 0.00671, 0.00600, 0.00503, 0.00398.
```

For the planted falsifier, the coupling fails.  It first overshoots
(`8.05`) and then collapses to ratios as small as `0.035`, leaving nearly
the whole external-tail delta uncancelled in late windows.

## Reduced Target

`LOGT-CELL` is reduced to:

```text
LOG-EXT-RATIO:
  prove, for zeta and uniformly on safe sigma-compacts, that

    Delta logT_N / Delta external_N

  has a signed expansion 1 - epsilon_N with an explicit summable residual
  after the moving-boundary/four-node cell cancellation.
```

The planted build must fail the same expansion.  The proof cannot estimate
`Delta logT` and `Delta external` separately; their signed difference is the
object.

## Status

```text
proved:    partition-invariant log-transfer error reconstruction;
observed:  zeta logT/external coupling is stable around 0.8;
observed:  planted fails the coupling and keeps a large uncancelled tail;
reduced:   LOGT-CELL -> LOG-EXT-RATIO;
next:      E77.5m should fit and derive the signed residual
           Delta external - Delta logT as a cell/Gamma-prime remainder.
```
