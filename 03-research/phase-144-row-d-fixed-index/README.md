# Phase 144 — Row D: the fixed-index inequality

*Target (adopted from `R143_004` §6 and `R143_005` §3): identify the smallest index `m` at which the
trace clause `(b′)_{B4_a}` fails for the falsifier `Ξ_a`, write the corresponding `ξ`-inequality
`(P_m)` at that index, and decide whether it is unconditional for `ξ` while false for `Ξ_a`.*

## Headline results of round 1

* **The smallest failing index for `Ξ_a` is `m = m_*(g_a) = \min\{n : t^{(a)}_n(F_+) ≠ 0\}`**, finite
  by (T1′)_a, with an explicit threshold in `r` whose numerator is minimal at `n = 1`; and
  **`m_* = 1` for a non-empty open set of admissible test classes** (the cosh family `g^{(T)}_a`).
  *This is an existence statement over `g_a`, not a genericity statement* — round 1's "outside a
  discrete exceptional set, for every admissible `g_a`" is withdrawn (`R144_002` M1).
* **The blueprint's proposed A3-line is REFUTED.** Every symmetric polar set `P = 1−P` has a uniform
  AM–GM floor, and for pair-symmetric coefficients the floor is attained at `n = 1`; the four-point
  two-modulus set of `Ξ_a` is no worse than `ξ`'s two-point set (Lemma D.37.2). The argument survives
  verbatim for `Ξ_a`, so by the FATAL rule it is wrong, and the round stops and says so
  (Remark D.37.5).
* **`(P_m)` for `ξ` is equivalent to RH at every fixed index `m ≥ 1`**, in particular at `m = 1`
  (Theorem D.38.3) — blueprint outcome (ii). The clause does not decompose by index. Shortest form:
  **RH ⟺ `I_∞(E,g_λ) ≥ 0` for every `E` with `\deg E > 0`, `½I_∞(E,E) > ¼\deg E`**
  (Restatement D.38.3a, `RESTATEMENT`).
* **Bounded density on `S_0` ⟺ RH** (Theorem D.38.5); no finite constant makes `(P_1)` unconditional,
  which answers the phase-142 `(★)`-question in the direction that was still open
  (Corollary D.38.5a).
* **O-29 and O-30 both closed negatively:** the sparse cone `\{t_{2^k} ≥ 0\}` is not a weakening (the
  single index `k = 0` is already RH); and there is **no** unconditional lower bound
  `W(E) ≥ −Ψ(a,b,\deg E)` on `S_0` — `O-30 ⟺ RH` (Corollary D.38.5c).
* **§D.40 — the trace-cone route is closed.** The single ray `E_t = tF + K`, with
  `(a,b,\deg) = (½,½,1)` frozen, `R(E_t) = ½t²q > 0`, and `W(E_t) = −t²q → −∞`, refutes **every**
  weakening tried in phases 143–144 (fixed index, sparse cone, head stratification, bounded density,
  large constant, O-30). What the frame cannot see: `W` is a norm iff RH, and `|n^{½−ρ}| = 1` iff RH —
  both zero-location facts. The parting point with `Ξ_a`: a primitive `F` with `I_∞(F,F) > 0` is a
  **theorem** for `Ξ_a` (Prop. 12.4B) and is literally `¬RH` for `ξ` (Paper 45 Thm 10.4).
  **No new positivity target inside the frame is proposed.**
* **Row D label: unchanged.**

## Files

| file | content |
|---|---|
| `R144_000_BLUEPRINT.md` | Blueprint: the object `(P_m)`, D.37, D.38 items 1–3, D.39, the FATAL rule, the `λ`-warning |
| `R144_002_AUDIT.md` | Audit of round 1: ACCEPT WITH REPAIRS, no FATAL; M1–M3 MAJOR, m1–m9 MINOR; programme-level assessment (§9) |
| `R144_003_ROUND2.md` | **Round-2 ledger (final round).** Per-finding status for M1–M3 and m1–m9; what each repair changed; §D.40 |
| `R144_001_ROUND1.md` | **Round 1 (this round).** D.37 (Lemma D.37.1 polar block; Lemma D.37.2 the polar floor and the refutation; Theorem D.37.3 the failing index; Theorem D.37.4 the true separating step; Remark D.37.5 the FATAL-rule report). D.38 (Prop. D.38.1 the unconditional inventory of `R > 0`; Lemma D.38.2 + D.38.2a the one-index witness; **Theorem D.38.3 `(P_m) ⟺ RH`**; Restatement D.38.3a; Cor. D.38.3b the `λ`-dependence; Prop. D.38.4 the `d = 1` head — `≤ 64` inequalities, **the count `64 = 64d²` itself RH-conditional**, none of them unconditional; **Theorem D.38.5 bounded density on `S_0` ⟺ RH**; Cor. D.38.5c **O-30 closed negatively**). **§D.40 closure of the trace-cone route.** D.39 synthesis. Round-2 repairs (M1–M3, m1–m9) applied in place with bracketed notes. Corpus check, paper-facing list (P47-43…P47-49), open list (O-30, O-31 new; O-29 closed), §Label |
| `scripts/certify_failing_index.py` | Certifies the `Ξ_a` polar block and the floor: `--a` (default `0.25`), `--fast` (dps 25 instead of 40), `--margin` (default `1e-6`). Exits `0` on PASS. Certifies (C1) the four polar values `Ξ_a(p) > 0`, pair-equal, `= ξ(1±2a)/2`; (C2) `\deg_aK_a = Σ_pΞ_a(p)² = I^{(a)}_∞(K_a,K_a) > 0`, hence `R_a(rF_+ + K_a) > 0` for every `r`; (C3) the polar part is `2A\cosh((½+a)L) + 2B\cosh((½−a)L)`, whose infimum is attained at `n = 1` and is **positive** — the numerical half of the refutation of the blueprint's lemma; (D) the failing-index threshold formula. **It certifies no sign statement about `ξ`.** |

Run: `python3 scripts/certify_failing_index.py --fast` → `RESULT: PASS`, exit `0` (≈1 s). Also
`PASS` at `--a 0.1` and `--a 0.45`. At `a = ¼`, `mp.dps = 25`: `α = 0.25436551936316197901`,
`β = 0.24856038909415705496`, `\deg_aK_a = 0.2529681689350597622`, floor `= 1.0058518169146380679` and four-term AM–GM bound
`1.0057848077201793325` — **both under the normalisation `Φ_{g_a}(1+a) = Φ_{g_a}(1−a) = 1`, which is
two independent normalisations of the (Baire-chosen, non-explicit) `g_a`: the floor value is therefore
not an `a`-invariant. The normalisation-free content is `A,B > 0` and the `\cosh` shape.** `α` and `β`
are `a`-invariants; `\deg_aK_a` is too.

## State of the phase

Round 1 (`R144_001`) and the audit (`R144_002`) are in place; **round 2 is the final round
round** — repairs applied in place in `R144_001` with bracketed round-2 notes, ledger in
`R144_003_ROUND2.md`. Remaining: `R144_004` confirmation, `R144_005` closing decision.
