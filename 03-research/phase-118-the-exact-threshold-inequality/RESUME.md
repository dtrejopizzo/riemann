# Resume note — what already exists (read after SPEC.md)

A machine restart killed the first wave of workstreams before any of them wrote
its report. Their **scripts survived** in `scripts/`, and two result files
survived. Reuse them; do not redo this work.

## Already settled — do not recompute

**(a) The pseudo-inverse cutoff is NOT the explanation.** `W1_pinv_sweep.log`
sweeps `rtol` over `1e-14 ... 1e-6` at `refine = 8,16,32,64` for steps `(2,3)`
and `(5,7)`. At every single setting the retained rank is FULL
(`14/14, 30/30, 62/62, 126/126`) and `lam_min_norm` is identical to 9 digits.
So the decay of `lam_min_norm` under refinement is a genuine continuum effect,
not an artifact of near-null directions of `A_0` being included or dropped.

**(b) Convergence data to refine 128 exists** in `W1_convergence.json` for the
steps `(2,3),(3,4),(4,5),(5,7),(7,8)` at
`refine = 4,8,12,16,24,32,48,64,96,128`, with `lam_min_norm`, `minA0`, `minSE`,
`rank_SE`, range residuals and timings.

**(c-NEW, 2026-08-17, supersedes (c) below) — the deep run to refine 512 changed
the picture.** `W0_deep_refine.log` / `.json` push three steps to `refine=512`.
The three behave DIFFERENTLY, and the difference tracks the conditioning of `A_0`:

| step | `lam_min_norm` local slope `-dlog(lam)/dlog(r)`, coarse -> fine | `minA0` at r=512 | reading |
|---|---|---|---|
| (2,3) | 0.68 0.44 0.26 0.15 0.08 **0.04** | 3.703e-04 | flattens; converges to a POSITIVE limit ~3.65e-4 |
| (3,4) | 0.83 0.62 0.43 0.36 **1.45 1.71** | 1.063e-06 | was flattening, then broke at the last two points |
| (5,7) | 1.54 1.56 1.61 1.60 1.68 **1.73** | 5.415e-08 | steady power decay, no flattening |

The one step whose `A_0` stays well conditioned is the one that converges to a
positive limit. The steps that appear to decay to zero are exactly the ones
where `A_0` becomes near-singular — and the target contains `b_E^* A_0^dag b_E`,
which amplifies error by `1/lambda_min(A_0)`. At `minA0 = 5.4e-8` in float64
that is an amplification of `~2e7`.

**Leading hypothesis, NOT yet established: the apparent decay to zero is a
conditioning artifact, and the true behaviour is convergence to a positive
limit — i.e. the inequality is strict with margin, NOT critical.** Settling this
is the campaign's top priority and requires high-precision arithmetic.

Note the earlier ruling-out in (a) was scoped to `refine <= 64`; it does NOT
cover `refine = 512`, where the conditioning is many orders worse.

**(c-OLD) The fit is inconclusive at refine <= 128.** A three-parameter fit
`lam(r) = L + C r^-p`:
- on all ten points gives `L < 0` with residuals *larger than* `|L|` — the coarse
  meshes are simply not in the asymptotic regime, so this is meaningless;
- on the last five or six points gives small `L > 0` for four of the five steps
  and small `L < 0` for `(7,8)`, with `p ~ 1.65-1.80` fairly stable;
- but `L` moves by an order of magnitude between the last-6 and last-5 windows
  (e.g. step `(5,7)`: `2.96e-5` vs `2.27e-6`).

**`L` is therefore not determined by the data.** The candid statement is that
`lam_min_norm` is consistent with `0`, with small positive, and with small
negative. The coordinator is pushing refinement to settle it; **do not duplicate
that run.**

**(d) `lambda_min(A_0)` itself decays to 0** under refinement, fast — for step
`(7,8)`, `9.7e-3` at `refine 4` down to `9.4e-7` at `refine 128`, roughly
`r^-2.7`. The old block becomes singular in the continuum limit. This is the
corpus's O3 "no spectral gap", measured directly.

**(e) The linchpin of the Weil identity is verified to 30 digits.**
`psi(1/4) = -(gamma + pi/2 + 3 log 2)` exactly, hence
`Re psi(1/4 + i tau/2) - log pi == g_Gamma(tau) - m_0` identically. See
`PROOF_ARCHITECTURE.md` §2, which you should read — it changes what counts as a
useful result in every workstream.

## Environment after the restart

`python-flint` 0.9.0 now lives at
`03-research/phase-118-the-exact-threshold-inequality/vendor/rowd-flint`
(it was copied out of volatile `/tmp` before the reboot). Use
`PYTHONPATH=<abs path to>/vendor/rowd-flint`. Do not rely on `/tmp`.

`numpy` 1.26.4, `scipy` 1.11.4, `mpmath` 1.3.0 import directly.

## Surviving scripts

`W1_convergence_run.py`, `W1_convergence_fit.py`, `W1_pinv_sweep_run.py`,
`W2_common.py`, `W3_build_xy.py`, `W3_task1_verify.py`, `W3_task2_phi_norm.py`,
`W4_next_thresholds_probe.py`, `W4_near_null_structure.py`,
`W4_near_null_parity_scan.py`, `W4_capacity_precision_test.py`,
`W0_weil_identity.py` (coordinator's, incomplete and unverified).

None of these has been reviewed. Treat them as drafts by a previous author:
read before reusing, and re-verify anything you depend on.
