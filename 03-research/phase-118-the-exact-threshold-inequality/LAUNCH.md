# Launch sheet — relaunch the phase-118 campaign

Stopped mid-flight on 2026-08-17 to stay inside a session limit. Everything
needed to resume is on disk. Nothing has been written to the paper, per
instruction.

## Round 2 outcome (2026-08-17, session limit reached)

**Landed.** W3 (`W3_SCATTERING.md`) and W4 (`W4_CERTIFIED_RANGE.md`) completed.
W5 verified the Weil identity against real zeta zeros to `5e-11`-`2e-9` before
dying — see `PROOF_ARCHITECTURE.md` §2, now upgraded to **verified**.

**Killed by the session limit, no report written:** W1, W2, W5. Their scripts and
result files survive in `scripts/` (`W1_hp_*` high-precision library,
`W2_sweep*.json`, `W2_coercivity_summary.json`, `W2_deep_check.*`,
`W2_tate_closedform.py`, `W5_highprec.log`, `W5_crossvalidate_assembly.log`,
`W5_zeros_cache.json` with 425 cached zeros, `W5_partB_bound.py`). Relaunch W1,
W2, W5 with the same briefs.

**FIRST TASK ON RESUME, before anything else:** resolve the two-route discrepancy
recorded in `PROOF_ARCHITECTURE.md` §2 ("UNRESOLVED"). Every fine numerical
conclusion in the campaign is suspended until it is settled.

**Do not relaunch W3 or W4** — they are done.

## Reading order for any agent

1. `SPEC.md` — the inequality, the code, the rules.
2. `RESUME.md` — what is already settled; do not redo it.
3. `PROOF_ARCHITECTURE.md` — the coordinator's derivation. **This changes what
   counts as a useful result in every workstream; nobody should start without it.**

## State

**Settled.**
- The pseudo-inverse cutoff is not the explanation for the decay of
  `lam_min_norm` (`W1_pinv_sweep.log`: full rank retained at every `rtol` from
  `1e-14` to `1e-6`, identical `lam` to 9 digits). Ruled out.
- `psi(1/4) = -(gamma + pi/2 + 3 log 2)` to 30 digits, hence
  `Re psi(1/4+i tau/2) - log pi == g_Gamma(tau) - m_0` identically. The paper's
  `m_0` **is** the archimedean constant of the explicit formula.
- `g_Gamma(tau) - m_0 = 2 pi *(zero density at tau) + o(1)`, checked numerically.
- W3 task (1) was verified to machine precision before the stop
  (`X^*X = R`, `Y^*Y = L`, `X^*X - Y^*Y = A`) — its script is in `scripts/`.

**Open, and the reason the campaign is not finished.**
- Whether `lam_min_norm -> 0`, or to a small positive limit, or crosses zero.
  Fits at `refine <= 128` are inconclusive: `L` moves by an order of magnitude
  between fitting windows. See `RESUME.md` (c).

**Running locally, no token cost, results land on disk.**
`scripts/W0_deep_refine.py` (nohup, writes `W0_deep_refine.json` and
`W0_deep_refine.log` incrementally) pushes steps `(2,3),(3,4),(5,7)` to
`refine = 512`. **Check this first on resume** — it may already have settled the
open question above. Refit with `L + C r^-p` on the last several points and
report `L` with an candid uncertainty.

## The five workstreams to relaunch

All five ran only minutes before the stop; none wrote its report. Relaunch as
`general-purpose` agents on Sonnet, in background, all five in parallel. Each
brief below is a summary — the full prompts are reconstructible from these plus
the three documents above.

| | file to write | question |
|---|---|---|
| **W1** | `W1_MINIMIZER.md` | Structure of the minimizing direction. Does it converge to a fixed continuum function or localize in frequency? `PROOF_ARCHITECTURE.md` §2 predicts the peak frequency climbs linearly in `refine` and there is no `L^2` convergence — test that explicitly. Decompose the minimizing *vector* (not the operator) against annulus ⊕ 2 Tate modes. Do **not** rerun the convergence sweep; the coordinator owns it. |
| **W2** | `W2_ANNULUS_TATE.md` | Block-decompose the target as `[[M_aa, M_at],[M_at^*, M_tt]]` with `M_tt` the 2x2 Tate block. Which of the three blocks carries the decay? Is `lambda_min(M_aa)` coercive, growing like `log(1/delta_j)`? If `M_tt` is critical, push for a closed form — the two vectors `e^{±t/2}|_{I_tau_old}` are explicit. |
| **W3** | `W3_SCATTERING.md` | The Douglas factor `Phi = Y X^dag` with `Y_T = Phi X_T`. Task (1) already verified. Remaining: `\|\|Phi\|\|` vs threshold and refinement (Galerkin gives a *lower* bound here — `>1` refutes); place-indexed block structure; whether `I - Phi^*Phi = Psi^*Psi` for an explicit `Psi`. Aim at the *structure* of `Phi`, not at bounding it — §2 says bounding it is RH. |
| **W4** | `W4_CERTIFIED_RANGE.md` | Extend the interval-certified endpoint past `T = log 2`. Reproduce the existing certificate, find what limits it (the margin is `8.6338e-8`), try `(1/2)log 5, 7, 8, 9, ...` using the exactness of the step. The assessment of *whether the mechanism can extend at all* matters as much as any extension. Uses `vendor/rowd-flint`. |
| **W5** | `W5_WEIL_IDENTITY.md` | **Highest value.** Verify `<A_T F,F> = sum_rho h(gamma_rho)` numerically to 8+ digits against real zeta zeros, at several `T`, and cross-validate `rowd_assembly.py` against it. Then Part B: how far does *verified* RH (`H = 3.0000175e12`) carry the inequality, and is the absorption of the high-frequency zero sum by the Gamma channel exact or only asymptotic? Also: check whether this line is already classical (Bombieri) rather than assuming novelty. Cache zeta zeros to disk; `mp.zetazero` is slow. |

## The one thing the coordinator should say on resume

`PROOF_ARCHITECTURE.md` §2 concludes that the row-(d) inequality **is** localized
Weil positivity on the primitive space, hence equivalent to RH — so no
reformulation internal to the operator theory closes it, and the campaign's
realistic outputs are (i) W5's identity as a validation and a clarification of
what remains, (ii) W4's certified range as an actual unconditional theorem, and
(iii) W1/W2/W3's structural results about where the criticality lives.

That conclusion rests on a derivation whose linchpin is verified but whose full
numerical check (W5 Part A) has **not yet been run**. Until it has, treat §2 as
derived-but-unverified and say so.
