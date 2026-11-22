# Phase 142 — Row D: the clause (b′)⁺

*Opened by `R142_000` to decide the clause to which `R141_005` reduced row D.
Rounds 1–2 complete: report `R142_001`, audit `R142_002` (0 FATAL, 5 MAJOR, 5 MINOR;
Theorem D.31.12 **STANDS**), repairs and §D.32 in `R142_003`.*

## What the phase proved

> **Theorem 12.3's hypothesis is unsatisfiable for `ξ` — and for every admissible `Z` with a simple
> isolated on-line zero, `ξ_K` verbatim.** There is no `h⁰ : D^W → R_{≥0}` with (a), (b′), (c), for any
> `χ`. (Theorem D.31.12; `PROVED` given the verified-zero import (X19); audited.)

**This is a statement about the frame, not about `ζ`.** The cause is that the effective cone of `D^W`
is strictly thinner than the Riemann–Roch gate `{R > 0}` *transversally to the canonical ray* — in
geometry the effective cone **fills** the positive cone (`D² > 0`, `D·H > 0` ⟹ `D` big), here it does
not. The deficit is an explicit constant: `s_1 = sup_u |sin(γ_1u)|/cosh(u/2) = 0.998460162718809…`,
where geometry has `1`. **The frame retains the intersection theory of `C × C` and discards its linear
systems**, and Theorem D.31.12 says one cannot keep the first without the second. The same obstruction
kills the clause for `Ξ_a` too (for a cruder reason), so it separates nothing: it is a frame defect.

Consequences, in order:

* **(C4.1) is FALSE** (residue R12, discharged). The exact constant of Theorem 11.14(ii) — not its
  upper bound (11.17), which is vacuous here — is the support function of the effective cone, and
  Lemma D.24.6's constant `√(ab)` is **not sharp** at an on-line zero. The `χ = 0` calibration of
  Cor. D.30.8 was made against the non-sharp constant.
* **(b′)⁺ and (b′)⁺_st are false for `ξ`**, for every `χ`, with a certified witness
  `E = 53.11911·F_0 + 400·K`, `F_0(u) = e^{−u²/18}\sin(γ_1u)` — a class that passes **every** necessary
  condition the corpus knew and fails exactly the new one.
* **Row D loses its reduction.** `R141_005`'s "row D reduces RH to constructing an `h⁰`" is
  **withdrawn**, not relabelled; Theorem 12.3 keeps its label as a vacuous implication. O-18 is closed
  negatively.
* **Row D: no label change.** Nothing with a sign is proved, and nothing above is evidence about the
  zeros of `ζ`.

**Epistemic type.** Unconditional **but computer-assisted**: the results rest on (X19) — `ρ_1` is a
**simple** zero of `ξ` on the line, and `ξ` has no other zero with `|Im ρ| ≤ 21`. Simplicity is
load-bearing: at multiplicity `2` the refutation fails. Same type as (X16)/(X18); *not* the type of
Theorem 11.14.

## Where phase 143 goes (§D.32.3, two horns, each with its exact test)

* **HORN A — weaken (c)** by a defect `Δ` supported above `d_*`. Theorem 12.3 applies (c) **only** at
  degree `0`, so any `Δ` with `Δ(0) = 0` leaves its proof intact (verified). Binding tests: prove
  (c′) for the (★)-gated candidate **unconditionally** (it currently holds only under RH — O-22), and
  decide the successor clause `S_0^{(★)} ⊆ 𝔐` (O-18′).
* **HORN B — enlarge effectivity.** Theorem D.32.4 reduces this to **one inequality**: any cone `𝓔'`
  with `deg > 0` and a finite bounded-density constant must have `C'_{F_0} ≥ G`, i.e. must raise the
  support function at `F_0` by the factor `1/s_1`. Of five candidates, B1 (`G ⋆ G^∨`) and B2
  (`Φ ≥ 0` on the critical line) are refuted, B3 (hull of translates of `K`) gains nothing, B5
  (completions) is refuted for closures; **B4 (non-negative Frobenius traces) is the only survivor —
  and the only candidate that reads A8.**

## Files

| file | content |
|---|---|
| `R142_000_BLUEPRINT.md` | the blueprint's blueprint: Q-A (1–3), Q-B (1–4), falsifier protocol, FATAL rule |
| `R142_001_ROUND1.md` | **report round 1, repaired in place for round 2** — §D.31: D.31.2 (the exact constant as a support function); D.31.4–5 (the sharp modulus bound, `s(γ,θ) < 1`, `s_1`); D.31.7 (`F_0`); D.31.8 (exact (C4.1)); **D.31.9 (decision: FALSE)**; **D.31.10–11**; **D.31.12 (obstruction)**; D.31.14 (ray-restricted); the table of eight necessary conditions × `ξ`/`ξ_K`/`Ξ_a`; falsifier runs; Q-B.1–4; corpus check; paper-facing list P47-26…P47-33; open list; §Label. Round-2 repairs carry bracketed `[…, round 2, finding H…]` notes |
| `R142_002_AUDIT.md` | audit: verdict on D.31.12 (**STANDS**), findings H1–H10, independent recomputation of every constant, the geometric diagnosis, required actions |
| `R142_003_ROUND2.md` | **round 2** — per-finding ledger (all ten accepted) and **§D.32**: what is vacuous / what survives; the geometric diagnosis as Restatement D.32.1; **Prop. D.32.3 (HORN A)**; **Thm D.32.4 (the HORN B test)** with the five-candidate table; O-18′, O-19, O-22, O-22′, O-23 |
| `scripts/certify_sF.py` | certifies `s_1 = 0.9984601627188091092345474…`, `u^* = 0.11099156…`, `d_0 = 324.9598…`, and the nonempty witness windows (mpmath, 40 digits) |
| `scripts/certify_leakage.py` | proof-of-record leakage bound `L ≤ 5.46×10^{−91}` from (E2)+(V2)+Riemann–von Mangoldt, **no zero list**, against the margin `G(1−s_1) = 5.79×10^{−3}`; the zero-list sum is kept as an illustration only |

Scripts certify constants only; no claim rests on unverified numerics.

## Imports

**(X19)** (new to Paper 47 / row D; Platt–Trudgian is already cited in papers 01, 36, 37) = (V1) `ρ_1`
is a simple on-line zero of `ξ`; (V2) no other zero has `|Im ρ| ≤ 21`. Rosser–Yohe–Schoenfeld (IFIP
1968); Platt–Trudgian, Bull. LMS **53** (2021), 792–797. *A cheaper form is available:* `ξ'(ρ_1) ≠ 0`
by interval arithmetic plus an argument-principle count. Q-B literature: Kreĭn–Nudel'man (AMS TMM 50,
1977); Rudin, Illinois J. Math. **7** (1963); Akhiezer (1965); Hartshorne GTM **52** Ch. V; Lazarsfeld
Ergebnisse **48** §2.2. **Beurling–Malliavin is a corpus cross-reference, not a new import**
(`03-research/phase-33-dbn/85-completeness-of-exponential-systems.md`, `82-variational-reformulation-and-the-connection.md` §5.2 — and it needs no RH).

## Next

Closing decision `R142_005`. Phase 143 opens on the two horns: **O-22 / O-18′** (Horn A) and
**O-22′** (Horn B, i.e. (T1),(T2) and the `C'_{F_0} ≥ G` test for the trace-positive cone).
