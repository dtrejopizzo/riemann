# E77.5d - Section-lag consecutive deltas

**Run:** 2026-07-18.

## 1. Statement

E77.5c named `SECTION-LAG` as the dominant finite obstruction in
`SR-LOG-2SCALE`.  E77.5d measures consecutive section differences at fixed
`lambda=6`:

```text
Delta_N(sigma)=E_{L,N}(sigma)-E_{L,N+2}(sigma).
```

If these deltas have a theorem-grade summable envelope, then
`SECTION-LAG` reduces to a tail estimate.

## 2. Probe

Probe:

```text
E77_5d_section_lag_probe.py
```

Command:

```bash
python3 E77_5d_section_lag_probe.py
```

Output:

```text
E77_5d_section_lag_results.json
```

The probe reads the certified `E77_5c_n22_core_results.json` artifact.

## 3. Results

For zeta at `lambda=6`:

| step | max error delta | error ratio |
|---|---:|---:|
| 8 -> 10 | 0.06116 | 0.8899 |
| 10 -> 12 | 0.03988 | 0.9193 |
| 12 -> 14 | 0.03213 | 0.9293 |
| 14 -> 16 | 0.02453 | 0.9419 |
| 16 -> 18 | 0.02195 | 0.9448 |
| 18 -> 20 | 0.01839 | 0.9511 |
| 20 -> 22 | 0.01454 | 0.9593 |

Tail delta ratios:

```text
0.8948, 0.8376, 0.7908
```

The deltas are positive throughout the safe sigma window.  The largest
delta occurs at the largest tested sigma `3.0`, but all sigma deltas move
in the same direction.

## 4. Reading

The data support monotone improvement of the coupled zeta
`SR-LOG-ERR` as N increases at fixed L.  This strengthens the
`SECTION-LAG` interpretation.

But the measured deltas do not themselves prove summability.  The error
ratios remain close to one, and the available N range is too short to infer
an asymptotic envelope.  A proof still needs an external bound derived from
the two-generator Schur/cell equation.

## 5. Reduced Target

`SECTION-LAG` is reduced to:

```text
DELTA-ENVELOPE:
Find an explicit summable upper envelope for

    |E_{L,N+2}(sigma)-E_{L,N}(sigma)|

uniformly on compact safe sigma intervals, in the cofinal regime
N(L)/L -> infinity.
```

The envelope must be proved before splitting prime and archimedean tails.
Otherwise it risks becoming the hard-prime-trace route already autopsied in
Phase 76.

## 6. Next Step

E77.5e:

```text
derive Delta_N directly from the Schur complement update between N and
N+2, expressing the difference as a finite shell update of F_b'/F_b;
measure whether the named shell-update terms match the observed deltas.
```

If the shell update is summable, it closes `SECTION-LAG`.  If not, its
dominant nonsummable component becomes the next finite object.

## 7. Status

```text
proved:    no IDENT theorem;
observed:  consecutive zeta section deltas are positive for N=8..22;
observed:  tail deltas decrease from 0.0245 to 0.0145;
open:      summable DELTA-ENVELOPE theorem;
next:      E77.5e Schur shell-update formula for Delta_N.
```
