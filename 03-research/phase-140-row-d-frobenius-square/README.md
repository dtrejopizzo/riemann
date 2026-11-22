# Phase 140 — Row D: the Frobenius side of (P139); the square as a tensor structure

the construction problem (P139) and tests (AT-1)–(AT-3)). Plan:
`05-meta-and-planning/ABCD-CLOSURE-PLAN/ROW-D-COMPLETION-PLAN.md` §1.*

**Question of the phase.** In Weil's proof, quadratic growth `h⁰(m(F_1+F_2)) ≍ m²` on `C×C` is
automatic from the product structure. Do the two arithmetic ingredients — the inverse-semigroup law
`Frob_m ⋆ Frob_n = Frob_{mn}` (Paper 44 Thm 3ter.4(i)) and a curve-level `h⁰` of linear growth
(Connes–Consani, arXiv:2205.01391) — assemble into an `h⁰_□` on the square meeting (a), (b′), (c) of
(P139)? If not, **which clause absorbs the zero information**?

**Answer after round 2, in one line.** The tensor structure supplies the growth exactly
(`h⁰_□(mK_K) = (r²/4)m²`, the constant (P139) demands, for every number field) and Weil's steps W3–W4
over every number field; but the candidate reads only bidegrees, so **(b′) fails for every
bidegree-function** (Thm D.24.7, extended in round 2 to every `h⁰` reading the Pólya-Frobenius Gram
data, Thm D.24.11) and **(c) implies RH** (Thm D.24.5(i)).

> **Round 1's stated *reason* was withdrawn in round 2** (audit finding H3). The collapse
> `Div_□/𝓝_∞ = NS(P¹×P¹)` is a property of the **Pólya realization** `r(Frob_n) := τ_{log n}(2K)`, a
> construction of this phase which deletes the arithmetic weights `Λ_K(𝔫)N𝔫^{−½}` — not a theorem
> about the Frobenius family, which Papers 44/46 never realize in `D^W`. Paper 44's **actual**
> Frobenius Gram form behaves in the opposite way: it is sparse and arithmetic (nonzero exactly when
> `m/n` is a prime power, weights `Λ(q^k)q^{−k/2}`) and **unsigned at every finite chart** — positivity
> on it fails on an explicit primitive class, unconditionally (Paper 44 **Thm 8bis.4a**). See
> §D.23.3bis / Theorem D.23.12, new in round 2.

## Files

| file | what it is | status |
|---|---|---|
| `R140_000_BLUEPRINT.md` | Blueprint: the idea to test, D.22–D.25, warnings, rounds | input of record |
| `R140_001_ROUND1.md` | **Round 1–2** (round-2 repairs are in place, each with a bracketed note). D.22 (`Frob_𝔫`, `Sh_{O_K}` over any number field — closes O-9); D.23 complete (`Div_□`, bidegree, the multiplicative semigroup, the full intersection matrix with the named regularization, the Weil comparison table, the Epstein failure line, the `Ξ_a` asymmetry, and Thm D.23.10 — the Weil bound shape on a translate family); D.24.1–D.24.4 (the exact clause-by-clause analysis of the tensor-square candidates); D.25 synthesis (**rewritten in full in round 2**); corpus check per idea; paper-facing list; open list; §Label | delivered; **round-2 repairs applied** |
| `R140_002_AUDIT.md` | **Audit of round 1**: 1 FATAL, 7 MAJOR, 6 MINOR; verdict *NOT CONFIRMABLE as round 1* | input of record |
| `R140_003_ROUND2.md` | **Round 2 — repair ledger.** All 14 findings accepted, none contested; per-finding disposition, new material, labels that moved | delivered |
| `scripts/certify_chi.py` | **illustrates** `inf g = c²/2` (so `χ = 1/8` for `ξ`) on a grid, and prints `1 − 1/log 3 = 0.08976…`. **Not a certificate** (no Lipschitz/interval bound; the minimizer is not a grid node — finding H13). `--fast` ≈0.13 s, full run ≈41 s. Exit `0`. | `COMPUTATIONAL-ILLUSTRATION`, load-bearing nowhere |
| `README.md` | this file | — |
| *(pending)* `R140_004_CONFIRMATION.md` | confirmation | not written |
| *(pending)* `R140_005_CLOSING_DECISION.md` | decision | not written |

## Results of record (after round 2)

| item | statement | label |
|---|---|---|
| D.22 | `Frob_𝔫` for ideals of `O_K`: the law `Frob_𝔪⋆Frob_𝔫 = Frob_{𝔪𝔫}`, `Frob_𝔫⋆Frob_𝔫^† = Δ^{(𝔫)}`, bidegree `(N𝔫^{½},N𝔫^{−½})`; `Sh_{O_K}(Frob_𝔫) = Cone(𝔫L_S ↪ L_S)` with **`L_S = ∏_{𝔓∈S_f}O_𝔓`**, `H⁰ ≅ O_K/𝔫`, `deg_{det} = \log N𝔫`, non-monoidal by `Tor`. Ideal-indexed: the class group never appears | **PROVED** — **O-9 closed** *(round 1 used `L_S = O_{K,S}` and proved `H⁰ = 0`; FATAL H1, repaired)* |
| **D.23.12** | **the three Gram forms**: (A) pure Frobenius — `W_fin` only, sparse on the prime-power-ratio graph, weights `Λ(q^k)q^{−k/2}`, **unsigned at every finite chart** (Paper 44 Thm 8bis.4a); (B) unit-averaged — full Weil kernel, sign `⟺` RH, forgets factorization; (C) Pólya realization — **rank 2**, reads neither | **PROVED** (C) / **PROVED-IN-REPOSITORY** (A),(B); new in round 2 |
| D.23.7 | `F_1 = K+K_odd`, `F_2 = K−K_odd` as `a_0`-dependent lifts canonical mod `𝓝_∞` (**not** the rulings `e_∓`, which are not in `D^W`), `K = ½(F_1+F_2)`, full intersection matrix, `r(Frob_n) ≡ n^{½}F_1+n^{−½}F_2 (mod 𝓝_∞)` | **PROVED** |
| D.23.8–9 | Castelnuovo with equality on `r(Div_□)`; the lattice is that of `NS(P¹×P¹)` (canonical class does **not** match) | **RESTATEMENT** of `R138_001` Cor. D.15.4c on a sub-cone (H4) + **PROVED** |
| D.23.10 + **D.23.13** | translate family: constant genus `W(E_0)`, Lefschetz datum (D.23.5a), Castelnuovo `⟺ |T_n| ≤ 2W(E_0)`; **over the whole orbit this is Bochner positive-definiteness of the Toeplitz kernel `κ_{E_0}`, i.e. RH for the zeros `E_0` sees** | **RESTATEMENT**; carries no sign. *Round 1's target O-16 is **withdrawn** on this ground (H8)* |
| D.23.4 | `r_Q` is not multiplicative — stated for the **order** `O_{−D}` and its ring class group, with the explicit witness `x²+5y²`: `r_Q(3) = r_Q(7) = 0 < r_Q(21)` | **PROVED** (H9 repair) |
| D.24.3a | `h⁰_□(mK_K) = (r²/4)m²` — the growth (P139) forces, on the nose, for every `K` | **PROVED** |
| D.24.2 | `λ_CC = 1/\log 3 < 1` **in CC's own units**; the `λ_CC²` deficit is **conditional** on `\deg_{CC} = \deg`, which Finding 13.8 declines; two unit problems named | **PROVED** (i) / **PROVED-CONDITIONAL** (ii) / **OPEN** (iii) — candidate (β) is **not refuted** (H6) |
| D.24.4 | `\inf g = c²/2`; `χ = 1/8` for `ξ`, `r²/8` for `ξ_K`; the blueprint's `χ = ¼` **corrected**, witness `½F_1` | **PROVED** |
| D.24.5 | (i) `(⇒)` for every bidegree-function: (c) **implies RH**. (ii) `(⇐)` for `ψ` satisfying (D.24.5a). (iii) biconditional for `h⁰_□` | **PROVED**; round 1's general biconditional **false and withdrawn** (H2, witness `ψ ≡ 0`) |
| **D.24.7** | (b′) **fails** for every nonzero `h⁰` factoring through the bidegree, with an explicit witness | **PROVED** — the round's strongest result; survived independent re-derivation intact |
| **D.24.11–12** | any `h⁰` reading the pairings against `r(Div_□)` factors through `M`, hence is refuted too; an admissible `h⁰` must read `Z(E)` **through the arithmetic side** | **PROVED**, new in round 2 |
| D.24.9 | (b′) is exactly a **moment problem** on `\{e^{(s−½)t}\}_{s∈\{0,1\}∪Z(ξ)}` with a nonnegativity constraint; necessary condition `|Φ_E(ρ)| ≤ b^{1−β}a^{β}` | **PROVED**; the moment cone `𝔐` is **OPEN** (O-15) |
| D.24.10 | D-HS (phase 136 S4): isometric Frobenius transport forces `h⁰ = ψ(ab)` — refuted | **PROVED** |
| (AT-1),(AT-2),(AT-3) | (AT-1) passes on the non-multiplicativity of `r_Q`; its second half is **weakened** (H7: no `Ξ_Q`-primitive witness — O-17). (AT-2) passes, and more strongly (the primitive bridge exists: Paper 47 Lemma 12.4A). (AT-3) passes. Clause (N) is **moot** for `h⁰_□` | **PROVED** / **WEAKENED** as marked |
| row D label | **no change**: no sign, no `h⁰` | — |

## Open items (after round 2)

`O-13` injectivity of `𝔫 ↦ Frob_𝔫` for general `K` (used nowhere). **`O-14′`** can an `h⁰` reading
family (A)'s *arithmetic* Gram entries `Λ(q^k)q^{−k/2}` satisfy (b′)? — forced, not optional, by
D.24.7 + D.24.11 + D.24.12. **`O-15`** describe the moment cone
`𝔐 = \{(M(E'),Z(E')) : E' ≥ 0, E' ≢ 0\}` — the whole content of (b′), with no zero named;
**recommended phase-141 target**. `O-15′` the general-necessity half of Thm D.23.13(iv).
**`O-17`** a `Ξ_Q`-**primitive** compactly supported witness with `W_Q < 0`, needed to upgrade
(AT-1)(ii). **~~`O-16`~~ withdrawn** (Thm D.23.13: it is Weil positivity on an orbit).

## Reproduction

    python3 scripts/certify_chi.py --fast     # ~0.13 s, exit 0
    python3 scripts/certify_chi.py            # ~41 s, exit 0
