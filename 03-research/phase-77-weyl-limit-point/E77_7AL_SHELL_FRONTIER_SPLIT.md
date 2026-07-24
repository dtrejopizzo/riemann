# E77.7al - Shell frontier split

**Run:** 2026-07-18.

## 1. Purpose

E77.7ak reset the BTG side to the smallest live object

```text
SHELL-RESIDUAL-CANCELLATION.
```

Returning to the exact Phase-5 algebra shows that this shell front is not yet
one theorem.  It is presently split into two exact but still unassembled
subobjects.

## 2. What the exact Phase-5 chain already says

The exact finite log-transfer/cell identity gives

```text
Q_N = Q_ext,N - Q_logT,N.                            (AL-1)
```

E77.5l/5m/5n/5o/5p reduce the scalar residual hierarchy as follows:

```text
raw residual R_N
=> LEAD-1/N-CANCEL
=> PROFILE-DRIFT-CANCEL
=> SECOND-COEFF-CANCEL
=> MOD4-DRIFT-SPLIT.                                (AL-2)
```

Separately, E77.5aa/5ab/5ac/5ad reduce the active Schur anchor law:

```text
Tp/T = t0p/t0 - theta'/(1-theta),
u_N = -theta'_N/(1-theta_N),
```

with the current exact live target

```text
SECTOR-CERTIFICATE:
prove Im(u_N)-|Re(u_N)| > 0 on the zeta cofinal path. (AL-3)
```

The planted build fails this sector decisively.

## 3. What is missing

At present there is **no proved implication**

```text
MOD4-DRIFT-SPLIT + SECTOR-CERTIFICATE
=> GEOMETRIC-SHELL-RESIDUAL.                        (AL-4)
```

That implication is plausible, but it is not in the ledger yet.

The exact gap is:

```text
we do not yet have a theorem that converts the signed Schur-anchor control
on u_N together with the mod4 drift hierarchy of Q_N into the shell-distance
decay of the shorted residual pairing

  <r_{R,M},S_{R,M}^{-1}r_{R,M}>/eta_R.
```

So the shell frontier is still split into:

```text
1. an active-anchor signed sector problem;
2. a mod4 drift/cell-profile cancellation problem.
```

## 4. Honest reduced targets

Therefore the most accurate shell-facing live objects are not a single
theorem, but the pair

```text
ANCHOR side:  SECTOR-CERTIFICATE
DRIFT side:   MOD4-DRIFT-SPLIT
```

together with an explicit missing coupling lemma:

```text
ANCHOR-DRIFT-TO-SHELL:
show that the signed sector control on u_N and the mod4 drift decomposition
of Q_N imply the shell shorted-energy decay needed for
GEOMETRIC-SHELL-RESIDUAL.                           (AL-5)
```

This is smaller and more honest than pretending that `GEOMETRIC-SHELL-RESIDUAL`
is already directly accessible from any single currently proved Phase-5 law.

## 5. Consequence for the BTG chain

The BTG chain should now be read as

```text
SECTOR-CERTIFICATE
+ MOD4-DRIFT-SPLIT
+ ANCHOR-DRIFT-TO-SHELL
=> GEOMETRIC-SHELL-RESIDUAL
=> SHELL-RESIDUAL-CANCELLATION
=> ... => BTG-DIV-L.                                (AL-6)
```

This is the current minimum exact shell program supported by the ledger.

## 6. Status

```text
clarified: the shell front is presently split into anchor-sector and mod4
           drift subobjects;
refined:   the missing theorem-grade connector is ANCHOR-DRIFT-TO-SHELL;
not proved: no current file gives the implication (AL-4)/(AL-5);
live:      SECTOR-CERTIFICATE;
live:      MOD4-DRIFT-SPLIT;
live:      ANCHOR-DRIFT-TO-SHELL;
next:      derive the shell shorted residual directly from the exact Schur
           log-transfer decomposition and test whether the connector can be
           written as a finite identity before any asymptotic estimate.
```
