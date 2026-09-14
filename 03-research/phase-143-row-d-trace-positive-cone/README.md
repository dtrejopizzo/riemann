# Phase 143 — Row D: `s_*`, the trace-positive cone B4, and a repaired transfer theorem

Row D of the ABCD programme (the sign). This phase opens on the two repair horns left by phase 142,
in the blueprint's order: **(0)** the constant `s_*` (O-19), **(1)** Horn B / the trace-positive cone
B4, **(2)** Horn A as a secondary line.

## Files

| file | content | status |
|---|---|---|
| `R143_000_LEAD_BLUEPRINT.md` | Lead's blueprint: D.33 (`s_*`), D.34 (B4: definition, (T1), (T2), the transfer theorem, falsifiers, A8), D.35 (Horn A), D.36 (synthesis); standing rules; FATAL rule | input of record |
| `R143_002_HOSTILE_AUDIT.md` | Hostile audit of round 1: **no FATAL**; MAJOR H1–H4; MINOR H5–H11; item-5 verdict *"RESTATEMENT, not reduction — but a well-chosen one"* | input of record |
| `R143_003_BUILDER_ROUND2.md` | **Builder, round 2** — per-finding repair ledger (H1–H11), the new **Proposition D.34.16**, and the new **Lemma D.34.9′** (`(G⁺)` unconditionally, O-25 closed) | **this round** |
| `R143_001_BUILDER_ROUND1.md` | **Builder, rounds 1–2 (repaired in place, bracketed round-2 notes)** — D.33 (`s_* = m(γ₁) ∈ [0.99845824, 0.99846016]` PROVED, attained at `ρ₁`; `= s_1` to 18 decimals CERTIFIED); D.34.1–4 (the cone; **(T1) decided NO, unconditionally**; **(T2) false**; **Theorem D.34.8, the transfer theorem 12.3-B4**; **Theorem D.34.10, `(b′)_{B4}` under RH**; **Corollary D.34.12, `(b′)_{B4} ⟺ RH`**); D.34.5–6 (falsifiers, A8); D.35; D.36; corpus check; paper-facing (P46-34…P46-42); open list (O-24…O-27); §Label | **this round** |
| `scripts/certify_s_star.py` | certifies `s(γ,θ)`, `m(γ) = inf_θ s(γ,θ)`, the elementary bound `L(γ) = 1/cosh(π/4γ)`, and the decision `s_* = s_1` with its margins. `--fast` = `mp.dps 20` (default `40`). Per-period Newton solves with an explicit truncation bound — **not** a blind scan | `CERTIFIED` |

Pending for the phase: hostile confirmation of round 2, and `R143_005` (lead decision).

## Headline results of round 1

* **`s_* = m(γ₁) ∈ [0.99845824, 0.99846016]` (PROVED), `= s_1 = 0.998460162718809109…` (CERTIFIED)**, attained at the lowest zero `ρ_1` and `θ = ±π/2`; margin
  `L(γ_2) − s_1 = 8.42×10^{−4}`. O-19 is closed in its **zero-indexed** form; the **cone** constant
  `s_*^{\mathrm{cone}}` of `R142_001` Definition D.31.13 is a different number and stays `OPEN`
  (`= 0` not excluded) — so Horn A's defect `Δ` is still undetermined.
* **(T1) is decided, NO, unconditionally** (Theorem D.34.5): no primitive class outside the radical
  has all Frobenius traces `≥ 0`. Mechanism: the traces generate a Dirichlet series whose only real
  poles are the two polar ones; Landau's theorem does the rest. No RH, no zero list, no
  equidistribution. The corpus precedent for the mechanism is `R138_001` Theorem D.17.2.
* The **literal (T1)** of Theorem D.32.4 is **false** on `B4` as defined (explicit degree-`0`
  witness) and true once `t_0 ≥ 0` is added; **(T2) is false** on `B4` — `C'_X = +∞`, proved in round 2
  by letting the Gaussian width grow (Theorem D.34.7, Lemma D.34.6a). Hence Theorem D.32.4's
  `(T1)+(T2)` format does not apply to B4, and J3's "B4 passes the test" is vacuous.
* **Theorem D.34.8 (12.3-B4)**: `(a) + (b′)_{B4} + (c) ⟹ RH`, proved using **only** (T1′) — no ample
  class, no bounded-density constant, no (T2). It stands **beside** Paper 46 Theorem 12.3 with an
  **incomparable** clause (`𝓔` and `B4` are not comparable): fewer and cheaper inputs about the cone,
  and a clause that is **not refuted** by Theorem D.31.10, whereas 12.3's is unsatisfiable.
* **Theorem D.34.10 / Corollary D.34.12**: `h⁰_{RR}^{+}` satisfies `(b′)_{B4}` **under RH**, so
  `RH ⟺ ∃` admissible `g` `∃h⁰` with `(a),(b′)_{B4^{g,0}},(c)` (an equivalence, hence also
  `RESTATEMENT`). The auxiliary condition `(G⁺)` on the test class is **unconditional**
  (Lemma D.34.9′: `g = K + λh`; `K` itself is inadmissible, and with `g = K` even (T1′) would fail). The clause that phase 142 proved **false** for the effective
  cone is **true** for the trace cone. Horn B is alive; the single remaining question is **O-24**
  (prove the clause unconditionally), which is RH.
* **Falsifiers.** `Ξ_a`: the transfer theorem transports verbatim, so `(b′)_{B4_a}` is **false** for
  `Ξ_a` (Corollary D.34.13) — the A3-line is located **inside the clause**, at `|n^{½−ρ}| = 1`.
  `Ξ_Q`: frame broken (A7), the traces are not definable. `ζ_K`: everything transports **conditionally
  on `ξ_K` having no real zero** (Theorem D.34.14) — the mechanism's only zero-location input.
* **Proposition D.34.16** (round 2): if `Φ_E(0) > 0` the traces are positive for all `n ≥ N(E)`,
  **unconditionally** — so `(b′)_{B4}` is a **finite** condition per class (`n < N(E)`; `N ≤ 16` for
  the phase-142 witness, `N ≤ 64d²` uniformly on `{deg ≤ d}` under RH). For `Ξ_a` the same eventual
  half holds and the violation sits at a fixed finite index: **the A3-line is in the head, not the
  tail.**
* **A8** enters through (α) the **semigroup** structure of the test translations plus the meromorphic
  continuation of their generating function and (β) `ξ`'s two **real** polar exponents — **not**
  through the weights `Λ(n)n^{−½}`, and not specifically through `N` (the sparse semigroup `{2^k}`
  works too). O-20 is answered affirmatively in that weaker sense (round-2 restatement, H6).

**Row D label: unchanged.** Nothing with a sign is proved.

## Reproduction

```
python3 scripts/certify_s_star.py --fast     # ~2 min, mp.dps = 20
python3 scripts/certify_s_star.py            # mp.dps = 40 (slower)
```
