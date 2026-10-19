# Phase 141 — Row D: an `h⁰` that reads the Frobenius traces

Target of the phase: **O-14′** (well-posed per `R140_004` residue R11), with **O-15** (the moment
cone) as a tool and **O-17** (the `Ξ_Q`-primitive bridge, residue R8) as the falsifier-side
prerequisite.

**Where the phase stands after round 2.** Clauses (a) and (c) of Theorem 12.3 are now **theorems**,
unconditional and model-uniform, for the Riemann–Roch-defined candidate
`h⁰_{RR}^{+}(E) = \max(R(E),0)\cdot\mathbf 1_{\deg E>0}` with `R` the right-hand side of (c) itself
(§D.30). Row D therefore reduces to a **single clause**: *every class of positive degree and positive
self-intersection is `𝓝_∞`-equivalent to a nonzero effective class.* It implies RH, it is false for
the falsifier `Ξ_a`, it is proved on the zero-free locus, and its converse (RH ⟹ the clause) is the
new open item **O-18**. **No sign is proved and none is claimed; row D keeps its label.**

## Files

| file | contents | status |
|---|---|---|
| `R141_000_BLUEPRINT.md` | the blueprint (R141_000): the object (R11 made well-posed), D.26–D.29; three falsifiers, corpus-grep instruction, FATAL-flag convention, the 8bis.4a warning | input of record |
| `R141_001_ROUND1.md` | **the mathematics of record, rounds 1 and 2.** D.26 (the Frobenius traces; `\ker T = 𝓝_∞`; the moment cone `𝔐`; (b′) as a containment; necessary conditions; transport to the falsifiers). D.27 (the quadratic ansatz: (c) as an inequality between quadratic forms; the case (A)/(B) analysis; `h⁰_{\deg}`; the Paper-44 Gram kernel `C^{Frob}` with residue R2 and Thm 8bis.4a). D.28 (**O-17 closed**). **§D.30 (new in round 2): the Riemann–Roch candidate, (a) and (c) unconditional, the clause (b′)⁺, the stable form, the falsifiers, O-18.** D.29 (synthesis, rewritten). Corpus check per idea, paper-facing list, open list, `§ Label`. Round-2 repairs are in place with bracketed notes | delivered (round 2) |
| `R141_002_AUDIT.md` | audit of round 1: 0 FATAL, 7 MAJOR (H1–H7), 7 MINOR (H8–H14); verdict **REVISE**; the D.29 recommendation rejected and the missing candidate supplied (H6) | delivered |
| `R141_003_ROUND2.md` | **repair ledger**: per-finding status (all 14 CLOSED, none contested), the new §D.30 result table, and the exact status of `RH ⟹ (b′)⁺` | delivered |
| `R141_004_CONFIRMATION.md` | confirmation | pending |
| `R141_005_CLOSING_DECISION.md` | closing decision (R141_005) | pending |

No `scripts/` directory: every constant of the phase (`γ_C`, `χ = 3/16` and its optimality at `E = ½K`,
`−1/16`) is an exact closed form.

## Results of record

| item | statement | label |
|---|---|---|
| D.26.1–D.26.5 | the Frobenius traces `t_n(E) = I_∞(E,τ_{\log n}g)` (zero-free), and **`\ker T = 𝓝_∞`**: the traces determine `E` mod `𝓝_∞`; separation of `n^{½−ρ}` by a `ζ`-transform (not by Bohr). *The round's one clean new theorem.* | PROVED |
| D.26.6 | every finite window of traces is surjective, on `D^W` and on the primitive `C_c^∞` subspace (Langer + Riemann–von Mangoldt) | PROVED |
| D.26.8 | **(b′) ⟺ `{Ψ>0} ∩ T(D^W) ⊆ 𝔐`** — a zero-free containment, with `E' ≢ 0` absorbed into `𝔐` | PROVED |
| D.26.9(i)–(iii) | `𝔐` is a convex, **pointed** cone inside the positive-degree half-space | PROVED |
| D.26.9(iv),(v) | barycentric and dual descriptions | RESTATEMENT ((iv)); PROVED `⊆` / OPEN `⊇` ((v)) — O-15′′ |
| D.26.10 | zero-free necessary conditions, incl. the one-sided A4/A8 bound `PRIME ≥ 0` | PROVED |
| D.26.11 | every theorem of D.26 transports to `Ξ_a`, `Ξ_Q`, `ξ_K` — hence **no proof carried out inside D.26 can establish a sign** (a statement about proofs, not objects) | PROVED |
| D.27.3 | clause (c) written exactly as an inequality between quadratic forms; the necessary part (Q1), **not decided** | PROVED |
| D.27.4 | `h⁰` satisfying (b′) vanishes in degree `≤ 0` — the classical sanity check | RESTATEMENT (Thm 12.3 Steps 2,4) |
| D.27.5 | on the positively 2-homogeneous ray-continuous ansatz: in case (A) (b′) fails; in case (B) **(c) alone implies RH, without (b′)** | PROVED |
| D.27.6 + D.27.6a | `h⁰_{\deg} = ¼(\deg)²`: growth `¼m²` exactly, (c) ⟺ RH, `χ = 3/16` **optimal** (extremal `½K`), and it **fails (b′)**; `3/16` vs `1/8` explained (different candidates; D.24.4 not contradicted) | PROVED |
| D.27.7–D.27.8 | the Paper-44 Gram kernel `C^{Frob}` (a NAMED CHOICE: the diagonal does not exist, Rem. 8bis.1c): `γ_C > 0` clears `¼m²`; `C^{Frob}` indefinite (zero trace); trace-level unsignedness on primitive classes; residue R2 and Thm 8bis.4a carried | PROVED |
| **D.28.1** | **O-17**: a `Ξ_Q`-primitive compactly supported witness with `I_∞^{(Q)}(F,F) > 0` — Prop. 12.4B with `P = {0,1}`, a non-real Davenport–Heilbronn zero, the widened strip, and Paper 46 **Lemma 3.1** for the operator inverse | PROVED modulo the `106_11` import (the standing of Prop. 12.4B) |
| **D.30.1** | **`R(K−E) = R(E)`** identically, from bilinearity and symmetry of `I_∞` alone | PROVED |
| **D.30.5** | **`h⁰_{RR}^{+}`: (a) and (c) hold unconditionally, for every `χ`** (the two degree gates cannot both be off, since `\deg K = 1 > 0`); growth `¼m² − ¼m + χ`; vanishes in degree `≤ 0`; not 2-homogeneous; not a bidegree-function; defeats D.24.7's witness | PROVED |
| **D.30.7–D.30.8** | `χ > 0` **refuted** unconditionally; `χ ≤ 0` forced; at `χ = 0` the gate is calibrated **exactly** to Lemma D.24.6's necessary bound | PROVED |
| **D.30.9–D.30.10** | **THE CLAUSE (b′)⁺**, and **(b′)⁺ ⟹ RH**, by two independent proofs (one direct, via the bounded-density bound) | statement / PROVED |
| **D.30.11–D.30.12** | Theorem 12.3 survives the **stable** weakening (b′)_{st}; hence the weakest target is the arithmetic *"`D²>0`, `D·H>0` ⟹ `D` big"* | PROVED (an extension of Thm 12.3; 12.3 untouched) |
| **D.30.13** | RH ⟹ (b′)⁺ **on the zero-free locus**, with the explicit effective family `2\sqrt{ab}\,τ_{\log(a/b)}K` | PROVED, unconditional |
| **O-18** | **RH ⟹ (b′)⁺ in general?** No counterexample available from the known necessary conditions; the perturbative route blocked by `R138_001` D.15.2b(ii) | **OPEN — the phase's principal open item** |
| D.30.14 | (b′)⁺ as the containment `T(S_0) ⊆ 𝔐`; under RH `S_0` is already **convex** (forward Lorentzian cone), so convexity of `𝔐` adds nothing | PROVED |
| D.30.15–D.30.16 | (a),(c) model-uniform (the gate needs only `\deg_Z K_Z > 0`, any polar rank — checked for `Ξ_a`'s rank 4); **`Ξ_a`: (b′)⁺ is false**, explicit witness `rF_+ + K_a`; for **`Ξ_Q`** the finding is that **Theorem 11.14, hence Theorem 12.3, does not transport** — axiom **A7** | PROVED / NOT DECIDED (with the obstruction named) |
| D.29 | synthesis, rewritten: which clause forces RH, where A3/A7/A8 enter, recommendation for phase 142 | synthesis |

**Row D: no label change.** Nothing in the corpus is relabelled.
