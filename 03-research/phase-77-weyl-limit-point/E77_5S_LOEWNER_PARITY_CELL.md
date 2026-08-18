# E77.5s - Loewner Parity Cell Audit

## Objective

E77.5r reduced the live obstruction to:

```text
LOEWNER-PARITY-CELL:
  explain the branch difference between N=0 mod 4 and N=2 mod 4 from the
  finite moving-boundary Loewner cell.
```

E77.5s tests the first candidate: raw parity of the inserted four-node
cell

```text
{-N-1,-N,N,N+1}.
```

## Probe

Artifacts:

```text
E77_5s_loewner_parity_cell_probe.py
E77_5s_loewner_parity_cell_results.json
```

Command:

```bash
python3 E77_5s_loewner_parity_cell_probe.py
```

The probe records the sine-symbol packages of the inserted four nodes and
compares them against the second coefficient `Q_N` at `sigma=1` and
`sigma=3`.

## Results

For zeta:

| N | mod4 | abs odd package | Q(sigma=1) | Q(sigma=3) |
|---:|---:|---:|---:|---:|
| 8 | 0 | 3.628621 | 0.293624 | 1.582871 |
| 10 | 2 | 3.172437 | -0.058858 | 0.360452 |
| 12 | 0 | 4.676992 | 0.415485 | 1.658269 |
| 14 | 2 | 7.769841 | -0.251635 | -0.415668 |
| 16 | 0 | 10.097603 | 0.382931 | 1.417036 |
| 18 | 2 | 2.130976 | 1.114514 | 3.557502 |

For planted:

| N | mod4 | abs odd package | Q(sigma=1) | Q(sigma=3) |
|---:|---:|---:|---:|---:|
| 8 | 0 | 16.471337 | -101.717588 | -6.218860 |
| 10 | 2 | 6.166854 | -5.732206 | 4.902665 |
| 12 | 0 | 6.349194 | 6.033886 | 12.368355 |
| 14 | 2 | 8.969127 | -4.065455 | 4.283370 |
| 16 | 0 | 11.047127 | 4.995937 | 13.544749 |
| 18 | 2 | 1.338367 | -0.815807 | 6.137718 |

The even left/right package is zero by symmetry in these central sections.

## Autopsy

Raw inserted-node parity does not explain the spike.

The decisive zeta counterexample is:

```text
N=18, mod2:
abs odd package = 2.130976,
Q(sigma=3) = 3.557502.
```

The spike is large when the raw odd package is small.  Conversely, `N=14`
has a larger raw odd package but negative/smaller Q values.  Therefore the
branch obstruction is not carried by unweighted sine-symbol parity.

This refines the target: the missing parity object must include the
Loewner/Cauchy weights produced by elimination and boundary movement.

## Reduced Target

`LOEWNER-PARITY-CELL` is reduced to:

```text
WEIGHTED-PARITY-CELL:
  derive the mod0/mod2 branch difference using the inserted-node parity
  after weighting by the common-core resolvent and safe Cauchy row.
```

The next probe should measure the weighted active-block vectors from the
common-core identity of E77.5k, not just the raw sine symbols.

## Status

```text
proved:    no parity-cell theorem yet;
refuted:   raw four-node sine-symbol parity as the spike source;
observed:  zeta spike survives when the raw odd package is small;
observed:  planted has different raw parity/transient anatomy;
reduced:   LOEWNER-PARITY-CELL -> WEIGHTED-PARITY-CELL;
next:      E77.5t should compute the Cauchy/resolvent-weighted parity
           packages in the active 2-node/6-node common-core block.
```
