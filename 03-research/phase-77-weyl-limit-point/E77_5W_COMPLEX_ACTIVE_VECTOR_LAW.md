# E77.5w - Complex Active Vector Law

## Statement

This test keeps the full six-node complex active contribution vector from the
common-core Schur update

```text
[-N-1, -N, -N+1, N-1, N, N+1],
```

with entries

```text
c_j = tau_j (S^{-1}k)_j.
```

The vector is phase-aligned by the inserted four-node anchor

```text
c_{-N-1}+c_{-N}+c_N+c_{N+1}
```

and normalized in complex l2.  This is not an absolute pre-cancellation
estimate: the retained object is the signed complex vector, including phase
gaps and inter-branch distances.

Target tested:

```text
COMPLEX-ACTIVE-VECTOR-LAW:
  the mod2 spike in Q_N is detected by the phase-aligned active vector itself.
```

## Probe

File:

```text
E77_5w_complex_active_vector_probe.py
```

Runs:

```text
python3 E77_5w_complex_active_vector_probe.py \
  --case zeta --max-modes 20 --dps 60 \
  --output E77_5w_complex_active_vector_zeta.json

python3 E77_5w_complex_active_vector_probe.py \
  --case plant --max-modes 18 --dps 50 \
  --output E77_5w_complex_active_vector_plant_n18.json
```

The plant is the mandatory falsifier:

```text
gamma = 14.134725141734693790
beta = 0.30
strength = 5.0
```

## Zeta Window

For `sigma=3.0`:

| N | mod4 | Q_N | left/right phase gap | boundary phase gap | inserted abs |
|---:|---:|---:|---:|---:|---:|
| 8 | 0 | 1.5828711783824705 | 0.538722449103895842 | 0.395038303832125964 | 1160198.15030925528 |
| 10 | 2 | 0.3604516822205389 | 0.412005459426397666 | 0.306229834347575009 | 9227968849.55392521 |
| 12 | 0 | 1.6582690853478144 | 0.342787376679962705 | 0.258823934607338454 | 21575329662.634019 |
| 14 | 2 | -0.41566848456466 | 0.286589965114190235 | 0.215051068515013576 | 261568701458.238432 |
| 16 | 0 | 1.4170355051596246 | 0.251893290546237616 | 0.192162943106738941 | 42275251255078.9744 |
| 18 | 2 | 3.557502428022666 | 0.217994501380878764 | 0.164536071862978498 | 653713667706497.118 |

Vector distances at `sigma=3.0`:

| comparison | distance |
|---|---:|
| mod0 8 -> 12 | 0.0790850058082026054 |
| mod0 12 -> 16 | 0.0360500026500093487 |
| mod2 10 -> 14 | 0.0499055646910633561 |
| mod2 14 -> 18 | 0.0271830094401027095 |
| cross 16 -> 18 | 0.0134723416328398399 |
| cross 16 -> 14 | 0.0139047077614944928 |

At `sigma=1.0` the same pattern appears:

| comparison | distance |
|---|---:|
| mod0 8 -> 12 | 0.077494490943680608 |
| mod0 12 -> 16 | 0.0354551777019858179 |
| mod2 10 -> 14 | 0.049368678946348602 |
| mod2 14 -> 18 | 0.026761823088371046 |
| cross 16 -> 18 | 0.0130051329292981256 |

## Plant Falsifier

For `sigma=3.0`:

| N | mod4 | Q_N | left/right phase gap | boundary phase gap | inserted abs |
|---:|---:|---:|---:|---:|---:|
| 8 | 0 | -6.218859619965421 | -0.910692186414754901 | -0.594420706269396768 | 0.24692399532631076 |
| 10 | 2 | 4.902664972580595 | -0.181197387064174096 | 0.306514435186748333 | 0.67910893341317327 |
| 12 | 0 | 12.368355307534316 | 0.018756987927862674 | 0.0458645180081895022 | 2.68429472584406667 |
| 14 | 2 | 4.283370277730909 | 0.0491251502169052007 | -0.000493593145355541645 | 0.948794999435129433 |
| 16 | 0 | 13.544748846546014 | 0.0520384089546014143 | 0.0544837030196709797 | 0.883022337270505902 |

Plant vector distances at `sigma=3.0`:

| comparison | distance |
|---|---:|
| mod0 8 -> 12 | 1.03994531577724999 |
| mod0 12 -> 16 | 0.371728912417873908 |
| mod2 10 -> 14 | 0.496243224967881326 |
| cross 12 -> 14 | 0.306201118288803519 |
| cross 16 -> 14 | 0.469839924031812825 |

## Proof-Or-Falsifier

The direct law is refuted.  In zeta, the normalized active vectors become
closer as `N` grows, including across the mod0/mod2 split.  The largest known
`Q_N` spike in this window occurs at `N=18`, `sigma=3`, but the adjacent
cross-mod vector distance

```text
dist(16,18) = 0.0134723416328398399
```

is the smallest cross distance in the table.  Therefore the mod2 spike is not
encoded in the location of the phase-aligned active vector alone.

The plant falsifier does not follow the same regular transport.  Its distances
remain one to two orders larger on the same reduced window.  Thus active-vector
regularity is a zeta discriminator, but not the missing scalar law for `Q_N`.

## Status

```text
proved:
  the full complex active vector is computable from the finite Schur cell
  without pseudoinverse or zero filtering;
  zeta active vectors show Cauchy-like transport;
  the planted falsifier breaks this transport.

refuted:
  COMPLEX-ACTIVE-VECTOR-LAW as a direct state law for the mod2 Q spike.

open:
  identify the derivative/curvature functional of the active-vector path
  that carries Q_N.
```

Reduced target:

```text
ACTIVE-VECTOR-CURVATURE:
  measure first and second differences of the phase-aligned active vectors
  and test whether Q_N is controlled by signed curvature rather than state.
```
