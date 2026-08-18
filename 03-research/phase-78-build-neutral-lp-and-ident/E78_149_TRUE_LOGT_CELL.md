# E78.149 - TRUE LOGT-CELL with the moving boundary pole (correction of E78.147)

**Run:** 2026-07-21.
**Scope:** IDENT, fixed-L. Corrects E78.147/E78.7 after the `d_{b,N}` audit.
**Class:** REDUCCION GENUINA (corrected numerics).

## 1. What changed

Audit finding: boundary index `= idx[-1] = n_modes = N`, so `d_{b,N} = 2 pi N/L`
depends on N; the boundary pole does not cancel. The object that feeds the WL-10
chain is the TRUE

```text
(log tau_N)'(z) = LOGT-CELL(z) = Delta[T'/T]
   = Delta[F'/F] - [ 1/(z-d_{b,N+2}) - 1/(z-d_{b,N}) ],   T = F/(z-d_{b,N}).
```

E78.147's probe computed only `Delta[F'/F]` (= W-QUOTIENT-DELTA). This note
recomputes the true `Delta[T'/T]` (probe `E78_149_true_logt_cell_probe.py`,
lambda=6, dps=60, N=8..20, both builds).

## 2. Result (per-step, A=|Delta[F'/F]|, B=|boundary inc|, C=|true Delta[T'/T]|)

### Zeta -- clean, still summable

```text
N->N+2   env|true|   N^2*C (sigma=1)   N^2*C (sigma=2)
 8->10   4.273e-2    1.280             1.983
10->12   2.836e-2    1.264             2.022
12->14   2.017e-2    1.403             2.109
14->16   1.491e-2    1.354             2.096
16->18   1.112e-2    1.288             2.027
18->20   8.822e-3    1.314             2.042
```

`N^2 C` is stable: `C(sigma=1) ~ 1.32`, `C(sigma=2) ~ 2.04`. So the TRUE object
obeys `|(log tau_N)'(i sigma)| = C(sigma)/N^2` with a stable constant, summable,
locally uniform. At sigma=1, `A ~ B` (0.0159 vs 0.0142 at N=8): the omitted
boundary term was the SAME order as the rest -- the correction was necessary --
but `C` (their signed combination) is again a clean `O(1/N^2)`.

### Plant -- still erratic

```text
N^2*C (sigma=1): 7.41, 0.66, 0.47, 0.75, 0.36, 0.98    (no clean law)
```

## 3. Reading

The bookkeeping correction changes the constant `C(sigma)` (from ~1.0 to ~1.32 at
sigma=1) but NOT the qualitative result: the true LOGT-CELL is `O(1/N^2)`
summable for zeta with a stable per-sigma constant, erratic-but-convergent for
the plant. All conclusions of E78.147 about flattening and fixed-L convergence
survive; only the object name (LOGT-CELL = Delta[T'/T], not Delta[F'/F]) and the
constant are corrected. The `C(sigma) ~ sigma` reading of E78.147 becomes
`C(sigma)` mildly super-linear (~1.32, 2.04 at sigma=1,2); exact identification
of `C(sigma)` remains open.

## 4. Status

```text
proved (exact): (log tau_N)' = Delta[F'/F] - Delta[1/(z-d_{b,N})], d_{b,N}=2piN/L;
observed:       zeta true LOGT-CELL = C(sigma)/N^2, C(1)~1.32 C(2)~2.04, summable;
observed:       plant erratic but convergent (Outcome A, build-neutral convergence);
corrected:      E78.147 mislabeled Delta[F'/F] as (log tau_N)'; E78.7 WL-7 not exact;
open:           exact C(sigma); the ZERO-SIDE-BOUNDEDNESS proof (E78.147 Sec 6);
next:           the point-6 DISCRIMINANT needs the RELATIVE residual F/A^Gamma
                (E78.150), since raw flattening is build-neutral here.
```
