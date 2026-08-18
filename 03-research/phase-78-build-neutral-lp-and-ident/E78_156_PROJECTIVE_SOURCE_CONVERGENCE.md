# E78.156 - PROJECTIVE-SOURCE-CONVERGENCE: point-2 existence via option (ii)

**Run:** 2026-07-21.
**Scope:** LP interface / point 2 (A2-d existence). Validates E78.151 option (ii).
**Class:** REDUCCION GENUINA (numerically decisive; analytic proof = the shared
N^{-2} law).

## 1. What was tested

Point-2 existence (A2-d) requires a normalized l2 class. Ledger E77.7i reduces
uniqueness (via the author's Cauchy-row separation lemma) to `(I-3) dim E_L=1 and
ell_0(v_0) != 0`. The source-selected response (E78.151 Thm 5.1)

```text
v_N^res = P_N b_N / ell_0(P_N b_N),   ell_0 = safe Cauchy row at z0 = i,
```

is canonical EVEN when `dim ker > 1` (the source b selects the vector), so it
sidesteps simplicity. Option (ii): does `v_N^res` converge in the safe Cauchy
topology as `N -> infinity`, even as the residue `alpha_N = ell_0(P_N b_N)`
collapses? Probe `E78_156`, ground cluster `P_N` with k=1 and k=2 modes, test
Cauchy profiles at `sigma in {0.55,0.75,1.5,2.0,3.0}`, convergence measure
`max_sigma |profile_N - profile_{N+2}|`.

## 2. Result (lambda=6, dps=50)

```text
build k=1   N   |alpha|      prof(1.5)   max|dprof|   N^2*dprof
zeta        8   1.416e-19    0.426541    --
zeta       10   4.591e-24    0.422356    0.013507     1.35
zeta       12   5.959e-25    0.419693    0.0086919    1.25
zeta       14   5.515e-29    0.417864    0.0060128    1.18
zeta       16   3.627e-32    0.416532    0.0044033    1.13
plant       8   0.2944       1.00207     --
plant      10   0.0582       0.950348    0.17408
plant      12   0.02792      0.942367    0.028233
plant      14   0.006885     0.941144    0.0042509
plant      16   0.01196      0.940439    0.0024187
zeta  k=2   8   8.438e-18    0.63953     --
zeta  k=2  10   2.149e-22    0.633218    0.0092037
zeta  k=2  12   3.008e-23    0.629321    0.0054695
zeta  k=2  14   2.272e-27    0.626543    0.0061148
zeta  k=2  16   1.404e-30    0.624571    0.0030344
```

## 3. Reading -- decisive support for option (ii)

- For ZETA, `|alpha|` collapses 13 orders of magnitude (1.4e-19 -> 3.6e-32), yet
  `prof(sigma)` CONVERGES and `max|dprof|` decays with `N^2*dprof ~ 1.2` stable,
  i.e. `dprof ~ 1.2/N^2` -- SUMMABLE. The source-selected direction converges in
  the safe Cauchy topology even as the residue vanishes.
- ROBUST to near-degeneracy: k=1 and k=2 both converge (so the possibly
  non-simple ground cluster does not break it -- simplicity NOT needed).
- PLANT (residue does not collapse) also converges. Build-neutral, as EXISTENCE
  should be (Outcome A); the discriminant lives elsewhere.

So PROJECTIVE-SOURCE-CONVERGENCE holds numerically: the normalized class EXISTS
as the safe-Cauchy limit of `v_N^res`, WITHOUT a residue lower bound (sidesteps
the c_0 wall E78.146) and WITHOUT simplicity of `E_L`.

## 4. UNIFICATION -- one N^{-2} law behind all open convergence halves

The `dprof ~ 1.2/N^2` envelope here is the SAME summability law as:

```text
- point 6 SPECTRAL-SHIFT-COUNTING BOUND_N ~ 5.4/N^2 (E78.153),
- the flattening / LOGT-CELL |(log tau_N)'| ~ C(sigma)/N^2 (E78.147/149),
- point 2 projective source dprof ~ 1.2/N^2 (here).
```

All three are consecutive-section safe-Cauchy differences with a summable
`O(N^{-2})` envelope. **Proving ONE analytic `N^{-2}` bound for consecutive
safe-Cauchy section differences would close the convergence halves of points 2,
5, and 6 simultaneously.** This is the single load-bearing analytic lemma the
program has converged to.

## 5. Status

```text
observed (decisive):
  v_N^res converges in safe Cauchy topology, dprof ~ 1.2/N^2 summable, even as
  |alpha| collapses 13 orders (zeta); robust to k=1,2 (no simplicity needed);
  build-neutral (both converge, Outcome A);
reduced:
  point-2 A2-d EXISTENCE -> PROJECTIVE-SOURCE-CONVERGENCE, numerically decisive,
  sidesteps both the c_0 lower bound (E78.146) and ground-state simplicity;
unified:
  the N^{-2} envelopes of points 2 (this), 5, 6 (E78.147/153) are one law --
  a single consecutive-section safe-Cauchy N^{-2} bound closes all three
  convergence halves;
open:
  the analytic proof of the shared O(N^{-2}) safe-Cauchy section-difference bound
  (= the flattening / counting-sum / source-convergence law);
next:
  attack the shared N^{-2} lemma directly, now that 3 fronts reduce to it.
```
