# E77.7an - Vector connector reduction

**Run:** 2026-07-18.

## 1. Purpose

E77.7am autopsied the scalar shortcut

```text
anchor/drift functional  ~  shorted shell energy
```

and concluded that the missing connector must stay at vector level.

This note identifies that vector-level connector explicitly: the shell
residual of E77.7h is the same Schur residual source that already appears in
the common-core moving-boundary decomposition of E77.5k/5aa.

## 2. The two residuals

### Phase 77 shell residual

In E77.7h, after embedding the old complement into the new one,

```text
Delta_M Sigma = <r, S^{-1} r>,
r = h_s - K_{os}^* x_old,                        (AN-1)
```

where

```text
x_old = (K_oo-(mu-eta)I)^(-1) h_o.
```

### Phase 5 common-core Schur source

In E77.5k/5aa, for the common core / active split,

```text
k = g_a - A_ac A_cc^{-1} g_c.                    (AN-2)
```

This is the exact active Schur source driving the correction term

```text
corr = tau S^{-1} k.
```

## 3. Identification

Comparing the probe formulas line by line:

```text
old complement block          <=> common core block,
new shell coordinates         <=> active block,
h_o                           <=> g_c,
h_s                           <=> g_a,
K_{os}^*                      <=> A_ac,
x_old                         <=> A_cc^{-1} g_c.
```

Therefore the residual vector in `(AN-1)` is exactly the Schur source in
`(AN-2)` under this identification:

```text
r  <=>  k.                                        (AN-3)
```

This is not a heuristic similarity.  It is the same algebraic pattern under
the old/new common-core embedding used in the two probes.

## 4. Consequence

The missing shell connector

```text
ANCHOR-DRIFT-TO-SHELL
```

can be reformulated more sharply as:

```text
SCHUR-SOURCE-TO-SHORTED-ENERGY:
express the shorted shell energy through the exact Schur active source k
and prove cancellation/summability there.          (AN-4)
```

Then the shell chain becomes

```text
control of k in the common-core Schur decomposition
=> control of r in the shell Stieltjes increment
=> GEOMETRIC-SHELL-RESIDUAL
=> ... => BTG-DIV-L.                               (AN-5)
```

So the vector connector does not require inventing a third formalism.  It
already lives in the same Schur source `k` that Phase 5 isolated.

## 5. What is still open

This reduction does **not** yet prove the needed decay/summability.

It only says that the remaining shell theorem should be phrased directly in
terms of the exact Schur source vector `k`, not in terms of an unrelated new
shell object.

The live shell-facing pair from E77.7al therefore becomes:

```text
SECTOR-CERTIFICATE,
MOD4-DRIFT-SPLIT,
```

plus the connector now renamed as

```text
SCHUR-SOURCE-TO-SHORTED-ENERGY.                    (AN-6)
```

## 6. Status

```text
proved:    the E77.7h shell residual and the E77.5k Schur active source are
           the same vector object under the common-core identification;
refined:   ANCHOR-DRIFT-TO-SHELL -> SCHUR-SOURCE-TO-SHORTED-ENERGY;
clarified: the remaining shell theorem should be written directly at the
           level of the Schur source k;
next:      derive the shorted shell energy from k together with the exact
           Q_logT / u-phase identities, and test whether the mod4/sector
           laws already control k itself.
```
