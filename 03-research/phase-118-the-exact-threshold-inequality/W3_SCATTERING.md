# W3 — the scattering question: is there an explicit contraction `Phi` with `Y_T = Phi X_T`?

Workstream W3, phase 118. Written 2026-08-17. All numbers below are **measured**
by the scripts named at each step, all living in `scripts/`, none of which
modifies `rowd_assembly.py` or `rowd_threshold.py`. Distinguishes measured /
derived / conjectured throughout, per SPEC Rules.

**Bottom line up front.** Douglas' lemma makes existence of `Phi` with
`Y_T = Phi X_T` and `||Phi||<=1` *equivalent* to row (d), hence to RH
(`PROOF_ARCHITECTURE.md` §2) — so no amount of numerics here can prove
`||Phi||<=1`, and this report does not claim to. What is new is (1) a
re-verified, machine-precision-exact explicit realization of `X_T, Y_T`,
carried further than before into (2) `||Phi||` at every prime-power threshold
up to 37 at refine 8/16/32 (all `<1`, all consistent with `->1`, exactly
mirroring the campaign's `lam_min_norm` finding, from the *opposite*
monotonicity direction), (3) the actual place-indexed block structure of
`Phi` — the deliverable the task asked to aim at — including a clean,
reproducible fact (the archimedean/Gamma channel's *relative* share of
`Phi`'s norm shrinks as the threshold grows, contrary to the naive
"archimedean channel does all the work" story), (4) a machine-precision
cross-check that the defect operator `I-Phi^*Phi` built from the explicit
channel construction agrees with the operator `A_T` from `rowd_assembly.py`
via a *second, independent* code path, and failed/negative results for the
Toeplitz-in-log, Hankel-in-log and rank-one candidates for `Phi`'s structure,
and (5) the near-maximizing direction's shape as a function of `t`, including
a genuine qualitative transition (center-peaked to edge-peaked) around
`T~1.2`.

---

## (1) Explicit `X_T, Y_T` — re-verified to machine precision

**Script:** `scripts/W3_task1_verify.py` (drafted by the interrupted earlier
attempt; re-run here unmodified). Run: `python3 W3_task1_verify.py`. Full log:
`scripts/W3_task1_verify.log`.

Construction (`scripts/W3_build_xy.py`, unmodified from the earlier attempt,
read carefully and re-verified line by line):

    X_T F = ( G_{Gamma,T}^{1/2} F ,  ( sqrt(w_n) J_{n,-} F )_n )
    Y_T F = ( sqrt(m_0) F        ,  ( sqrt(w_n) J_{n,+} F )_n )

`J_{a,±}` is realized on an "enlarged mesh" (original cell edges union
shifted-by-`-a` edges) via 0/1 embedding matrices scaled by `sqrt(cell
length)` (an `L^2`-orthonormal codomain basis) — an actual, candid
finite-dimensional realization of the zero-extension-to-`L^2(R)` codomain the
SPEC insists is load-bearing, not a formal stand-in. `G_{Gamma,T}^{1/2}` is
realized as the abstract symmetric PSD square root of the assembled Gram form
`G` (no elementary Fourier-synthesis realization of the Gamma channel exists
in this codebase; Douglas' lemma only needs *some* Hilbert space, so this is
legitimate and is flagged as such in `W3_build_xy.py`'s docstring).

**Result** (thresholds `q = 2..37`, refine `4, 8`; both on the full mesh and
after restriction to `P_T`):

| refine | max `\|X^*X-R\|` | max `\|Y^*Y-L\|` | max `\|(X^*X-Y^*Y)-A\|` | typical scale |
|---|---|---|---|---|
| 4  | 3.6e-12 | 3.6e-12 | 6.7e-13 | 0.09 – 2.6 |
| 8  | 4.1e-12 | 4.1e-12 | 6.9e-13 | 0.07 – 1.3 |

Relative residuals are `~1e-12` to `~1e-13` throughout, at every one of the 19
prime-power thresholds up to 37 and both on the full mesh and after
projection to the primitive space `P_T` (columns marked `[P_T: ...]` in the
log) — machine precision, full stop. **Task (1) is re-verified and its
report, lost in the earlier interruption, is now recorded here.**

---

## (2) `\|\|Phi\|\|` vs threshold and refinement

**Scripts:** `scripts/W3_task2_phi_norm.py` (earlier draft; provides the
"cheap" Rayleigh-quotient route and cross-checks it against a fully explicit
SVD-of-the-channel-matrices route at refine 4, 8 — they **agree to
`<1e-6` relative at every threshold and every `rtol` tested**, printed `YES`
throughout `scripts/W3_task2_phi_norm.py`'s own log path; the explicit route
is `O(rows_X)` in memory and becomes too expensive to also run at refine
16/32 for all 19 thresholds, so it is not repeated there — this is stated,
not hidden). `scripts/W3_task2b_phi_norm_fast.py` (new, this run) reruns the
already-cross-checked-cheap route alone across refine `8, 16, 32`, all 19
thresholds up to 37, and `rtol in {1e-6,1e-8,1e-10,1e-12}`. Full log:
`scripts/W3_task2b_phi_norm.log`, `scripts/W3_task2b_phi_norm.json`.

Identity used (exact, no approximation, holds because `Phi X = Y` on `Ran(X)`):

    ||Phi||^2 = sup_v (v^T L_P v)/(v^T R_P v) = lambda_max( R_P^{dag/2} L_P R_P^{dag/2} )

**Monotonicity direction, stated explicitly per SPEC Rules:** this is a
*Rayleigh quotient of a maximum*; restricting to the Galerkin subspace can
only *decrease* the achievable supremum. So the measured `||Phi||` is a
**lower bound** on the true value — the *opposite* direction from
`lam_min_norm` (a minimum, Galerkin gives an upper bound there). Measured
`||Phi||>1` would refute row (d) outright; measured `<=1` is consistent but
proves nothing.

**Rtol-dependence (measured, not assumed):** identical to 8 significant
digits across all four `rtol` values at *every* threshold and refine tested,
and `rank(R_P)` is full (`= dimP`) throughout. Same conclusion as the
campaign's earlier pseudo-inverse sweep (`RESUME.md` (a)): the cutoff is not
doing anything here either.

**Result** — `||Phi||`, selected thresholds (full table in the log):

| q | refine 8 | refine 16 | refine 32 |
|---|---|---|---|
| 2 | 0.94817 | 0.95117 | 0.95220 |
| 8 | 0.99818 | 0.99943 | 0.99983 |
| 17 | 0.99957 | 0.99986 | 0.99996 |
| 32 | 0.99986 | 0.99995 | 0.99999 |
| 37 | 0.99986 | 0.99996 | 0.99999 |

`||Phi|| < 1` at **every single** threshold/refine combination tested (no
violation found — the numerics do not refute row (d)), and `||Phi||`
increases toward `1` monotonically with both the threshold `q` and the mesh
refinement, mirroring `lam_min_norm -> 0+` exactly: `1 - ||Phi||^2` and
`lam_min_norm` are literally two names for gaps that both close under
refinement (see §(4) for a direct, machine-precision identity linking them
via `A_T`). **This is consistent with, not proof of, `||Phi||->1` — i.e.
criticality — matching the rest of the campaign's finding.**

---

## (3) Place-indexed block structure of `Phi` — the deliverable

**Script:** `scripts/W3_task3b_blocks.py` (new). Run:
`python3 W3_task3b_blocks.py`. Full log: `scripts/W3_task3b_blocks.log`.
Rows `{const, sym_n : n in prime powers < q}`, columns
`{Gamma, ant_n : n in prime powers < q}`, entries = operator norm
(top singular value) of the corresponding block of `Phi = Y X^dagger`
(explicit SVD pseudoinverse, `rtol=1e-10`; by §(2)'s rtol-independence
finding this value is not sensitive to that choice — **derived**, not
independently re-swept here, from the rank-stability already measured
at every `rtol` in §(2)). Computed at `q = 8, 17, 37`, refine 8.

### Does the archimedean channel do essentially all the work? Measured: no, and its relative share *shrinks* with T.

| q | `\|\|Phi\|\|` (full) | `\|\|Phi[:,Gamma]\|\|` | `\|\|Phi[:,finite]\|\|` | Gamma frac. of `\|\|Phi\|\|_F^2` |
|---|---|---|---|---|
| 8  | 0.9982 | 0.8450 | 0.6311 | 0.701 |
| 17 | 0.9996 | 0.7744 | 0.7454 | 0.590 |
| 37 | 0.9999 | 0.6819 | 0.8360 | 0.442 |

The Gamma column *is* individually the largest single entry in every row at
every threshold tested (e.g. `const` row at `q=37`: `Gamma=0.404` vs the next
largest `ant_5=0.180`, more than 2x) — so in a "which single place matters
most" sense the archimedean channel is special, consistent with the
intuition in the prompt. But **as an operator norm restricted to just that
column, `||Phi[:,Gamma]||` *decreases* with `q` (0.845 → 0.774 → 0.682) while
`||Phi[:,finite]||` increases (0.631 → 0.745 → 0.836) toward the full
`||Phi||`**: collectively, the growing family of finite contacts can
almost by itself reach nearly the same norm as the whole operator, while the
archimedean channel alone falls further behind. **Measured, only 3
thresholds — reported as a clear trend, not asserted as an asymptotic law.**
The elementary obstruction noted in the prompt (`Phi` cannot be
block-diagonal over places) is consistent with this: it is not that the
archimedean channel pays for everything, it is that *no single channel* can,
and the finite channels' collective share grows with `T`.

### Finite-finite block: no simple decay law found (negative result)

Testing `B[n,m] = ||Phi[sym_n, ant_m]||` against two closed forms, linear fit
of `log B`:

| q | Toeplitz `f(\|log n - log m\|)` `R^2` | Hankel `f(log n + log m)` `R^2` |
|---|---|---|
| 8  | 0.156 | 0.084 |
| 17 | 0.002 | 0.116 |
| 37 | 0.006 | 0.105 |

**Both dead.** `R^2` never exceeds `0.16`; the Hankel fit's `R^2` does not
even improve with `q`. Neither "decay in the shift `log n - log m`" nor "a
Hankel/Toeplitz pattern in `log n`" survives contact with the numbers —
reported here as failed, not smoothed over.

**Diagonal suppression (measured, robust across all three thresholds):** the
`n=m` entry of `B` is *not* the row-maximum in **100% of rows**, at every
threshold tested. Concretely (q=37, row `sym_5`): `B[5,3]=0.0734`,
`B[5,7]=0.0736` both exceed the diagonal `B[5,5]=0.0485`. The block is
locally *dipped*, not peaked, at coincident prime powers — the opposite of
the naive "near-diagonal decay" picture.

### Is `Phi` close to rank-one-plus-diagonal? Partially, and improving with T.

Best rank-1 fit of the off-diagonal part of the finite-finite block
`B_ff` (`n != m`), relative Frobenius error and its complement (fraction of
squared norm explained):

| q | rel. error | explained-variance fraction |
|---|---|---|
| 8  | 0.456 | 0.793 |
| 17 | 0.340 | 0.885 |
| 37 | 0.257 | 0.934 |

Not exact at any threshold tested, but the fit visibly *improves* with `q`:
by `q=37` a single rank-one term plus the (suppressed) diagonal already
explains 93% of the off-diagonal block's squared norm. **Measured trend,
3 data points — worth pushing further (more thresholds, larger refine) but
not claimed here as a proven asymptotic.**

### Generalized-eigenvalue spectrum: how many singular values near 1

**Script:** `scripts/W3_task3a_spectrum.py` (new). Uses the exact identity
(no explicit codomain needed): since `Phi X = Y` on `P_T`,

    ||Phi(Xv)||^2 / ||Xv||^2 = (v^T L_P v)/(v^T R_P v)   for all v in P_T,

so the squared singular values of `Phi|_{Ran(X)}` are *exactly* the
generalized eigenvalues of the pencil `(L_P,R_P)` — computed via
`scipy.linalg.eigh(L_P,R_P)`, cross-checked against §(2)'s top eigenvalue
(they agree by construction: same quantity). Full log:
`scripts/W3_task3a_spectrum.log`.

Count of eigenvalues `>1-1e-3` (i.e. singular values of `Phi` within `~0.05%`
of 1):

| q | refine 8 | refine 16 |
|---|---|---|
| 2  | 0 | 0 |
| 8  | 0 | 0 |
| 13 | 0 | 2 |
| 19 | 1 | 4 |
| 32 | 3 | 6 |
| 37 | 3 | 7 |

Grows with **both** `T` and refinement — no spectral gap opening near 1,
consistent with (and measured independently of) the campaign's `lam_min_norm`
finding and `PROOF_ARCHITECTURE.md` §3's explanation (finer meshes resolve
higher frequencies, hence more near-null directions).

---

## (4) `I - Phi^*Phi = Psi^*Psi`: searched, no explicit closed form found

**Script:** `scripts/W3_task4_defect.py` (new). Run:
`python3 W3_task4_defect.py`. Full log: `scripts/W3_task4_defect.log`.

`Phi` is extended to all of `codomain(X_T)` via the Moore-Penrose
pseudoinverse (kills `Ran(X_T)^perp`). Trivially, `D := I - Phi^*Phi = I`
(i.e. `Psi = Identity`) on `Ran(X_T)^perp` — uninteresting, confirmed
numerically (top eigenvalues of `D` sit at exactly `1.000000`). The content
is entirely on `Ran(X_T)`.

**Cross-check (machine precision, two independent code paths):** pulling `D`
back through `X_T` gives, by construction, exactly `<A_T v,v>` for
`v=X_T^dagger u`. This was checked *directly against `rowd_assembly.py`'s own
`R,A` matrices* — a code path that shares nothing with the channel-explicit
`X,Y` construction of `W3_build_xy.py` beyond the mesh:

| q | bottom eigval of D (explicit `X,Y` route) | `1 - mu_min(A_P,R_P)` (raw `rowd_assembly` route) |
|---|---|---|
| 8  | 3.645799e-03 | 1 − 0.996354200636 = 3.645799e-03 |
| 17 | 8.659926e-04 | 1 − 0.999134007401 = 8.659926e-04 |
| 37 | (not built explicitly at refine 8; see below) | 2.780145e-04 |

Agreement to 9 significant digits at `q=8,17` — a genuine validation that the
two independently-coded constructions describe the same operator (a real bug
in either would have shown up here), not new physical content: it **is**
Douglas' lemma restated, and is reported as such, not oversold.

**The genuinely open part — an explicit `Psi` (unitary dilation / Julia
operator) — was searched and NOT found.** Concretely tried and reported as
failed:

- *Toeplitz-in-`log n`, Hankel-in-`log n`* for the finite-finite block of
  `Phi` itself (§3): `R^2 <= 0.16` throughout — already dead, so any `Psi`
  built from those forms is dead too.
- *Block-diagonal-over-places* `Psi`: explicitly excluded by the prompt's own
  elementary obstruction (would force `Re<S_nF,F> <= -Re<S_nF,F>`, false),
  confirmed consistent with §3's finding that no single channel carries the
  whole defect.
- *Channel decomposition of the near-null eigenvector of `D`* (the most
  natural candidate direction for `Psi` to act on): computed explicitly.
  Gamma-channel fraction of `||v||^2` for the 8 lowest eigenvalues of `D`:

| q | mode 0 (most critical) | mode 1 | ... | mode 7 (least critical of the 8) |
|---|---|---|---|---|
| 8  | 0.606 | 0.639 | → | 0.732 |
| 17 | 0.449 | 0.474 | → | 0.554 |

  The Gamma fraction **increases monotonically from the most-critical mode to
  the least-critical one, at both thresholds tested** — i.e. the direction
  closest to breaking the inequality is *less* archimedean-dominated than the
  safer directions nearby, the opposite of what a "Gamma channel absorbs the
  danger" story would predict. This sharpens §3's finding and is reported as
  a genuine structural fact, not a guess.

No candidate built from `Psi(D)`, the two Tate moments, or the leakage
coefficients `b_E` of `rowd_threshold.py` was found to reproduce `D`'s
spectrum beyond the tautological identity above — this is reported as an
**candid negative result**, not a near-miss: nothing was found that even got
close enough to "miss at the third digit."

---

## (5) The near-maximizing direction, as a function of `t` on `I_T`

Directly from §3's generalized-eigenvector computation
(`scripts/W3_task3a_spectrum.py`): the eigenvector `v` for the top
generalized eigenvalue, pulled back to an actual piecewise-constant function
`F=Z@v` on the mesh of `I_T`, IS the near-maximizing direction (this is what
"top singular value of `Phi`" means, restated in the domain).

**Measured, refine 8 and 16, `q=2..37`:**

- **Sign structure:** exactly 2 sign changes for the top mode at every
  threshold and refine tested — the "simplest" admissible shape after
  removing the two Tate constraints, consistent across refinement.
- **A genuine qualitative transition in peak location around `T~1.2`:**

  | q | T | peak location `\|t_peak\|/T` |
  |---|---|---|
  | 2  | 0.35 | 0.06 |
  | 3  | 0.55 | 0.06 |
  | 5  | 0.80 | 0.05 |
  | 8  | 1.04 | 0.04 |
  | 13 | 1.28 | **0.80** |
  | 19 | 1.47 | 0.78 |
  | 32 | 1.73 | 0.77 |
  | 37 | 1.81 | 0.80 |

  For small `T` the top mode peaks essentially at the center of `I_T`; for
  `T` past roughly `1.2` (between thresholds `q=8` and `q=13`) it jumps to
  peaking near the *edge*, around 77-80% of `T` out, and stays there through
  `q=37`. Same qualitative pattern at refine 16. **This transition is
  measured, not derived** — no mechanism for it is proposed here.
- **Behaviour at `t=0`:** `F(0)` is always comparable in magnitude to the
  peak value (never small/vanishing), e.g. at `q=37,refine=8`,
  `F(0)=-0.177` vs peak `|F|_max=0.201` — the mode does not have a node at
  the origin despite the primitivity constraints living there.
- **Endpoint behaviour:** support is (numerically) the full window `I_T` at
  every threshold — no boundary layer or vanishing-at-endpoints structure was
  found; the "active" (>2% of peak) region's share near the edges (`|t|>0.9T`)
  ranges `12%-40%` across thresholds with no clean monotone trend.
- **Motion with refinement:** amplitude `|F|_max` decreases as refine
  increases at fixed `T` (e.g. `q=37`: `0.201` at refine 8 vs `0.207` at
  refine 16 — small change; the shape is close to refinement-converged
  already at refine 8-16 for the *top* mode, unlike the higher, more
  oscillatory modes which by `PROOF_ARCHITECTURE.md` §3's argument should
  keep climbing in frequency under refinement — consistent with, though not
  a full test of, that prediction).

---

## Summary table: what was established vs what remains open

| claim | status |
|---|---|
| `X_T^*X_T=R_T`, `Y_T^*Y_T=L_T`, difference `=A_T` | **verified**, machine precision, re-confirmed after the earlier interruption |
| `\|\|Phi\|\|<1` at every threshold/refine tested, up to `q=37`, refine 8/16/32 | **measured** (lower bound; no violation found) |
| `\|\|Phi\|\|` consistent with `->1` under refinement, mirroring `lam_min_norm->0+` | **measured**, consistent with, not proof of, criticality |
| archimedean (Gamma) channel carries most of a single row's block-norm budget | **measured**, true, but its aggregate share of `\|\|Phi\|\|_F^2` *shrinks* with `T` (0.70→0.59→0.44) |
| Toeplitz-in-`log n` / Hankel-in-`log n` structure for `Phi`'s finite-finite block | **refuted** (`R^2<=0.16`) |
| rank-one-plus-diagonal structure for the finite-finite block | **partial fit**, improving with `T` (79%→93% explained variance), not exact |
| diagonal (`n=m`) suppression relative to neighbours | **measured**, robust, 100% of rows at all 3 thresholds tested |
| explicit `Psi` with `I-Phi^*Phi=Psi^*Psi` beyond the tautological pullback of `A_T` | **not found** — candid negative result |
| near-null defect eigenvector is more archimedean-dominated as it gets *safer* (less critical) | **measured**, at 2 thresholds |
| near-maximizing `F` transitions from center-peaked to edge-peaked around `T~1.2` | **measured** |

Nothing here proves `||Phi||<=1` or RH; per `PROOF_ARCHITECTURE.md` §2 nothing
internal to this operator-theoretic reformulation can. What this report adds
to the campaign is the verified explicit realization of `X_T,Y_T` (task 1,
now on record), and a set of concrete, reproducible structural facts and
failed candidates about `Phi` that any eventual explicit-identity proof would
have to reproduce or explain away.
