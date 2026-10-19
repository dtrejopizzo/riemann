# Phase 138 — Row D: the primitive radial sector and detecting cones


**Question of the phase (Q).** Is there a convex cone `C ⊂ D^W` that is (i) *detecting* (every off-line
zero is witnessed by a failure of `I_∞(F,F) ≤ ½(deg F)²` at some `F ∈ C`), (ii) defined without
reference to zeros, and (iii) such that the inequality on `C` follows from a structure of the carrier
(polar block, Frobenius lattice, positivity of kernels, convexity) rather than from the explicit
formula plus zero information?

**Answer after rounds 1–2 (audit: CONFIRMED WITH REPAIRS, no FATAL).** No such cone is
produced, and (i) and (iii) are proved to live on **complementary `I_∞`-orthogonal summands**:
`D^W = Λ ⊥ P^W` with `Λ = span(K,K_odd)` a hyperbolic plane reading only the ruling datum
`M(F) ∈ R²`, and `P^W` carrying the pure zero form. The polar block satisfies the Hodge-index
inequality identically (slack `½μ(F)²`), so no ruling-side structure can detect; detection is cheap
(`E` and `C_c^∞(R)` are detecting cones, witnessed by mollified triangles) but on the family where the
detection happens the sign is the PNT error term — a recorded route no-go. The invariant that
separates `ξ` from the falsifier `Ξ_a` before any zero is spoken of is **equimodularity of the polar
exponents** `|p−½|`, with the explicit ceiling that it cannot separate `ξ` from `ζ_K`.
**No label change for row D.**

## Files

| file | round | content |
|---|---|---|
| `R138_000_BLUEPRINT.md` | round 0 | the blueprint: setting, Definition 0.1 (detecting cone), Observation 0.2, items D.15–D.18, and warnings |
| `CORPUS_CHECK_R138.md` | corpus check | which of the nine candidate ideas were already attempted, with verdicts and paths (Pólya cone and support-growth NEW; Chebyshev/PNT a recorded no-go; Hilbert–Pólya and Laguerre–Pólya closed) |
| `R138_005_CLOSING_DECISION.md` | round 3 | closing decision: answer to Q (PROVED restricted / OPEN clause (iii) on `E`), corpus discipline, paper-facing list, phase-139 recommendation; residuals C1–C4 applied in place | delivered |
| `R138_001_ROUND1.md` | rounds 1+2 | the mathematics: D.15 complete (five items); D.16 items 1–3; D.17 items 1–4; §5 the answer to Q; §6 paper- and blueprint-facing corrections; §6bis corpus check; §7 open list; §7bis **the answer to Q after audit**; §8 label. **All round-2 repairs are applied in place, each marked with a bracketed `[…, round 2, finding H<n>]` note — no silent edits.** |
| `R138_002_AUDIT.md` | round 2 | verdict **CONFIRMED WITH REPAIRS**, no FATAL; 4 MAJOR (H1–H4), 9 MINOR (H5–H13); §0 lists what survived independent re-derivation |
| `R138_003_ROUND2.md` | round 2 | cover note: the repair ledger H1–H13 (what changed, where, and what it cost), and what survives unchanged |

*(Later: `R138_004` confirmation, `R138_005` closing decision. No `scripts/` directory: nothing in
rounds 1–2 requires a certified constant — every statement is symbolic.)*

## Main statements of round 1, with labels

| id | statement | label |
|---|---|---|
| Thm D.15.1 | `D^W = Λ ⊥ P^W`; `Λ = span(K,K_odd)` a hyperbolic plane of signature `(1,1)`; `P^W` = radical of the polar block | `PROVED` |
| Thm D.15.2 | Lorentzian criterion: `Q ≤ 0` on `K^⊥` ⟺ reverse Cauchy–Schwarz against `K` on any set absorbing at `K` | `PROVED`; blueprint clause (c) `REFUTED` |
| Thm D.15.2b | (i) `E` has empty `‖·‖₁`-interior; (ii) `E` is **not absorbing at `K`** — algebraic, topology-free, and this is what refutes the blueprint | `PROVED`; round-1's "every topology" claim `WITHDRAWN` (H2) |
| Thm D.15.2c | `RH ⟺ Hodge index on the ample cone`; but `A` is defined through `I_∞`, so it is **not zero-free** and fails clause (ii) of Q | `PROVED`, with the H10 caveat |
| Thm D.15.3 | polar slack `½μ(F)²`; `(★)` `PRIME ≤ ARCH + ½deg²`, zero-free | `PROVED` |
| Thm D.15.4 | `Ξ_a` fails Hodge index on the **effective** class `τ_uK_a + τ_{−u}K_a`, `u ≠ 0` | `PROVED` |
| Thm D.15.4b | equimodularity of `\|p−½\|` ⟺ Hodge index on the Frobenius translation cone | `PROVED` |
| Thm D.15.4c | `Λ_ξ^+` is effective, zero-free, structurally signed — and not detecting | `PROVED` |
| Thm D.16.1 | `{τ}`, `{δ}`, `{p(∂),⋆}` each make the closure detecting; `{p(∂)}` does not | `PROVED`; "translation is *the* operation" `REFUTED` |
| Thm D.16.1(d) | Theorem F's own witnesses are `q_±(∂)φ^{⋆N}` — no translation; `⋆` ranges over members of `C_W` (the fixed-kernel form is not provable, H4) | `PROVED` (repaired) |
| Thm D.16.2′ | Cartwright annihilation budget crosses the zero density at `R = 2πe·e^{2T}` | `PROVED` (density itself `PROVED-IN-REPOSITORY`, phase 122) |
| D.16.3′ | comparison with D.11 | `HEURISTIC` (relabelled, H3) |
| Thm D.16.2‴ | detection and polar structure live on complementary summands | `PROVED` |
| Thm D.17.1b | `C_Pó ∩ C¹(R) = {0}`: the Pólya cone meets the Weil class only in `0` | `PROVED`; blueprint cone `REFUTED`, repaired |
| Thm D.17.2 | the one-parameter **family** `{h_T}` detects: `RH ⟺ W(h_T) ≥ 0 ∀T > 0` | `PROVED` (Landau); **novelty `OPEN`** (H8) |
| Cor. D.17.2d | `E` and `C_c^∞(R)` are **detecting cones** (Definition 0.1), witnessed by mollified triangles. `C_Pó` is a cone of *kernels* and is **not** one (H1) | `PROVED` |
| D.17.3 | on the Pólya cone the sign is the PNT error term | `PROVED-IN-REPOSITORY` (route no-go, `phase-114/114_d_185`); the convexity remark downgraded (H6) |
| D.17.4 | falsifier on the triangle family: detection confirmed; the "growth match ⟺ unimodularity" prediction refuted | `PROVED` |

## Routes stopped in this phase

* the Pólya cone as a source of the sign (PNT error term; `phase-114/114_d_185`, `phase-72/E72_49`);
* deriving the sign from the polar block or the Frobenius lattice on any cone;
* the Khovanskii–Teissier criterion on the effective cone.

Not touched, per the standing no-go list: Hilbert–Pólya (MW-4, NG-E5); Laguerre–Pólya / Jensen /
Turán / Li / Keiper (phase 28, 103); extending the certified window past `T = log 2` (phase 118 W4).

## Status after round 2

Verdict **CONFIRMED WITH REPAIRS**, no FATAL. The two substantive contributions — the
`I_∞`-orthogonal splitting into a hyperbolic plane and the zero form (hence: no ruling-side structure
can detect), and the equimodularity criterion with its `ζ_K` ceiling — survived re-derivation
intact; the negative answer to **Q** (§7bis of `R138_001`, written after the audit) was confirmed in restricted form by `R138_004` and its label split (PROVED restricted / OPEN unrestricted, clause (iii) on `E`). No MAJOR finding touched a proof:
H1 and H4 are statement/quantifier repairs, H2 withdrew an overreaching claim of record whose
load-bearing half is proved, H3 was a mislabel.

Open after round 2: D.15-β (a zero-free description of the ample cone), D.15-γ (interior of `E` in
finer topologies — withdrawn claim, not needed), D.16-α, D.16-β, **D.16-γ** (a cone cut out by the zero
datum — the one unexplored quadrant), D.17-α (attribution of Theorem D.17.2), D.17-β (convexity of
`√C_Pó`).
