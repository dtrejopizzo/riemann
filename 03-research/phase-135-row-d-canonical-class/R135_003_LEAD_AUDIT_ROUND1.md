# R135.003 — Lead audit of round 1 (phase 135)

Author: session lead (Fable 5.1). Date: 2026-09-12.

## 0. Independent derivations, written BEFORE reading R135_001 (audit independence)

**0.1 Numerics** (`scripts/lead_polya_check.py`, exit 0, 30 digits): Pólya's kernel
`Φ(u) = Σ_n (4π²n⁴e^{9u/2} − 6πn²e^{5u/2})e^{−πn²e^{2u}}` satisfies, in the paper's
convention `Φ_g(s) = ∫g(t)e^{(s−½)t}dt`, `Φ_K(½) = ξ(½) = 0.497120778…`,
`Φ_K(0) = Φ_K(1) = ½`, `Φ_K(2) = ξ(2)`, `Φ_K(−3) = ξ(−3)`, `Φ_K(½+3i) = ξ(½+3i)`,
`|Φ_K(ρ_1)| < 10^{−32}`; `K > 0` on the grid; `I_∞(F,K) = ½ deg F` on a bump to 17
digits. The prime part of `T_∞(K) = 1` is `Σ_n Λ(n)n^{−½}·2K(log n) = 0.00269`; the
archimedean term carries `0.9973`. **The canonical class is almost entirely
archimedean** — consistent with the phase-118 / Connes–Consani fact that the first
cell `|t| ≤ log 2` is where everything unconditional lives.

**0.2 What the transfer theorem actually needs from the radical.** Only two facts:
(i) `N ∈ 𝓝_∞ ⇒ I_∞(N,F) = 0 ∀F` (definition); (ii) `N ∈ 𝓝_∞ ⇒ deg N = 0`. Proof of
(ii) without any independence argument: test against translates of `K`:
`Φ_{τ_uK}(s) = e^{(s−½)u}ξ(s)`, so `I_∞(τ_uK, N) = ½(e^{−u/2}Φ_N(1) + e^{u/2}Φ_N(0))`
(the zero sum vanishes termwise); vanishing for two values of `u` gives
`Φ_N(0) = Φ_N(1) = 0`. So the explicit characterization of `𝓝_∞` is a bonus, not a
load-bearing step. The builder should not make D.8 depend on D.7(i).

**0.3 A clean uniqueness theorem for the characterization** (`𝓝_∞ ⊆ {Φ_N(ρ)=0 ∀ρ}`),
avoiding distribution-theoretic independence of `e^{(ρ−½)t}`: for `N ∈ 𝓝_∞` real,
test against `τ_u N^†`: `I_∞(τ_uN^†, N) = −Σ_ρ e^{(ρ−½)u}Φ_N(1−ρ)² = 0` for all real
`u` (polar terms vanish by 0.2). Put `a_ρ := Φ_N(1−ρ)²`, `λ_ρ := ρ−½`, `|Re λ_ρ| ≤ ½`.
If `Σ_ρ|a_ρ| < ∞` (true when `Φ_N(s) = O(|s|^{−1})` in the strip, e.g. `N' ∈ L¹`
weighted), then for `Re w > ½`:
`∫_0^∞ (Σ a_ρ e^{λ_ρ u}) e^{−wu} du = Σ_ρ a_ρ/(w − λ_ρ) ≡ 0`.
The right side is meromorphic on `C` (zeros are discrete; `Σ|a_ρ| < ∞`) with residue
`a_ρ` at `λ_ρ` (distinct zeros, distinct exponents); vanishing on a half-plane forces
`≡ 0`, hence every `a_ρ = 0`, hence `Φ_N(1−ρ) = 0`. **Lemma (uniqueness of absolutely
convergent exponential sums with exponents in a vertical strip): `Σ a_n e^{λ_n u} = 0
∀u ∈ R`, `Σ|a_n| < ∞`, `λ_n` distinct in a strip ⇒ all `a_n = 0`.** `CLASSICAL`-level,
proof above. This also handles off-line zeros with no RH assumption.

**0.4 Openness of the ample cone (D.7(iv)).** `I_∞(E,F) = T_∞(E ⋆ F^†) =
∫E(t) w_F(t) dt` with `w_F(t) := T_∞(τ_t F^†)`. By the explicit formula,
`w_F(t) = Φ_F(1)e^{−t/2}·… + Φ_F(0)e^{t/2}·… − Σ_ρ e^{(ρ−½)t}Φ_F(1−ρ)` (signs per
convention), and `|Σ_ρ e^{(ρ−½)t}Φ_F(1−ρ)| ≤ e^{|t|/2}Σ_ρ|Φ_F(1−ρ)|` since `Re ρ ≤ 1`
— **Chebyshev-trivial**, no zero-free region. Hence `|w_F(t)| ≤ C_F cosh(t/2)` and
`|I_∞(E,F)| ≤ C_F deg E` for `E ≥ 0`. If the builder's `C_F` uses more than
`0 ≤ Re ρ ≤ 1`, it is wrong or wasteful. Caveat to check: the builder must not use
`Σ_ρ|Φ_F(1−ρ)| < ∞` unless `F` is smooth enough (true for `C_c^∞`).

**0.5 The transfer proof, checked step by step (Hartshorne V.1.9 transported).**
`F` primitive in `D_A^{rad}`, assume `I_∞(F,F) > 0`. (c) at `E = nF`:
`h^0(nF) + h^0(K−nF) ≥ ½n²I(F,F) − ½n·I(F,K) + χ = ½n²I(F,F) + χ` since
`I(F,K) = ½deg F = 0`. If `h^0(nF) > 0` then by (b′) `nF ≡ E' ≥ 0` mod `𝓝_∞`; `E' ≠ 0`
(else `nF ∈ 𝓝_∞`, so `I(F,F) = 0`), so `deg E' > 0 = deg(nF)`, contradicting 0.2(ii).
So `h^0(nF) = 0` for all `n`, and `h^0(K − nF) → ∞`, in particular `> 0` for large
`n`: `K − nF ≡ E'_n ≥ 0`, `E'_n ≠ 0`. Fix `m > C_F` (0.4). Then
`I(E'_n, F + mA) ≥ (m − C_F)deg E'_n ≥ 0`, while
`I(K − nF, F + mA) = I(K,F) + m·I(K,A) − nI(F,F) − nm·I(F,A) = 0 + m − nI(F,F) − 0 < 0`
for `n > m/I(F,F)`. Since `I(·, F+mA)` is `𝓝_∞`-invariant, contradiction. ∎
Needs: `I(K,A) = 1` (`= Φ_K(0)+Φ_K(1)`), `𝓝_∞`-invariance of `deg` and of `I(·,G)`,
`F + mA ∈` the class where `I` is defined (`A = e_+ + e_−` is a ruling *functional*,
not a function: `I(E, A) := deg E` must be **defined**, and `I(K − nF, F + mA)` expands
by bilinearity — the builder must make `A` an honest element or treat `deg` as a
functional throughout). **Potential gap to watch: `A` is not in `D^W`.** The fix is to
write everything with the functional `deg` and never form `F + mA` as a class:
`I(E'_n, F) + m·deg E'_n ≥ 0` vs `I(K−nF, F) + m·deg(K−nF) = −nI(F,F) + m`.

**0.6 The `Ξ_a` falsifier theorem (D.8).** For `Ξ_a` all of D.6–D.8 transport with
`K_a = (e^{at}K)⋆(e^{−at}K) > 0`, `Φ_{K_a} = ξ(s+a)ξ(s−a)`, four poles at
`{−a, 1−a, a, 1+a}` — so the ruling plane is **four-dimensional** for `Ξ_a`
(Paper 46 §7 / P124 lab already noted rank 4) and "primitive" means four conditions.
The transfer theorem then says: (a)+(b′)+(c) ⇒ `Σ_ρ Φ(ρ)Φ(1−ρ) ≥ 0` on that
sector ⇒ all zeros of `Ξ_a` on the line — false. So no `h^0` exists for `Ξ_a`. The
builder must state the rank-4 modification, not copy the rank-2 statement.

**0.7 On "using the answer".** `K` is defined from `ξ`, the same datum as Paper 43's
symbol. The location of zeros is never used in D.6–D.8; `𝓝_∞` is defined as a
radical. What *does* use zeros: the **characterization** of `𝓝_∞` and of `P^⊥`
(harmless: characterizations, not definitions) and every numerical *test* of (c) in
D.9(ii). The auditor should confirm the separation is kept in the paper's text.

**0.8 Expected refutations of the blueprint.** (i) `𝓝_∞ = ΠK⋆D^W` exactly is
probably false as stated: the Mellin quotient `Φ_N/(s(1−s)ξ(s))` is entire but need
not be the Mellin transform of an element of `D^W` (growth); expect
`𝓝_∞ = {N ∈ D^W : Φ_N ∈ s(1−s)ξ·𝒪(C)}` with `ΠK⋆D^W` a proper dense-ish subset.
(ii) `deg K_{CC} = −2log 2` vs `deg K = 1`: no reconciliation; the sign difference
must be recorded, not explained away. (iii) D.9(i)'s convex set may not have
`H^0(0) = {0}`: `E + ΠK⋆g ≥ 0` with `E = 0` means `K⋆Πg ≥ 0`, and `Φ_{K⋆Πg}(0) =
ξ(0)·0 = 0`, so a nonnegative function with vanishing `Φ(0)` must be `0` ✓ — fine, but
only after `Πg ∈ P` is checked for `g ∈ D^W` (not only `C_c^∞`): `Φ_{Πg}(0) =
0·Φ_g(0)` needs `Φ_g` finite at `0`, i.e. `g` in the strip class. OK.

## 1. Re-derived and found correct (after reading Part II §§11–16 of Paper 46, before R135_001)

| statement | check |
|---|---|
| Def 11.1 / Lemma 11.2 | decay `e^{−(1+ε)|t|}`, `C²`: holomorphy on `−½−ε < Re s < 3/2+ε` and the two-power bound (11.2) are exactly what the contour proof of Paper 45 Thm 9.4 needs ✓; the refutation of my `½+ε` class is right on both counts (contour line `c>1` unreachable; zero sum not absolutely convergent with one power) — a real correction of the blueprint |
| Thm 11.3 | every step checked against Cor 9.4a; the infinite prime sum converges by `Σ Λ(n) n^{−3/2−ε}` ✓ |
| Thm 11.7 | the cancellation `3/2·x^{−1/4} − 3/2·x^{−1/4}` at `t→−∞` via the theta functional equation is the point that settles decay of `K` on both sides ✓; `Φ_K = ξ` by agreement on a line ✓; my numerics agree to 17–27 digits |
| Thm 11.8 | `I_∞(F,K) = ½ deg F`, `I_∞(K,K) = ½`, `T_∞(K) = 1`, `Frob_n` weights `n^{±½}` ✓ (my §0.1) |
| Lemma 11.9 | identical to my §0.3 (Laplace transform + residue); the builder's version also handles the polar exponents `±½` and multiplicities ✓ |
| Thm 11.10 | (a)⇒(c) via `Π𝒮 = 0` in `D'` and hypoellipticity, then Lemma 11.9 ✓ |
| (11.13) refutation | correct and important: the perp is order-one vanishing; `Φ_G = ξ·e` needs multiplicities; equality ⟺ all zeros simple = `OPEN`. The blueprint's identification would have been an unproved statement about zeros; the builder refused it — right |
| Thm 11.11, Prop 11.11a | radical = `P^W ∩ (P^W)^⊥` ✓; `τ_a(ΠK) ∉ ΠK⋆D^W` by Riemann–Lebesgue against a unimodular symbol ✓ — my §0.8(i) expected exactly this |
| Thm 11.12 | Jensen `O(r)` vs `(r/π) log r` ✓; the refutation of "second proof of Paper 45 Thm 12.2" is a correct description: it is the colimit statement Remark 12.4 declined |
| Thm 11.13, 11.14 | Rosser–Schoenfeld constant used only as `ψ(x)=O(x)` ✓; the repair `A ↦ 2K` (degree form inside `D^W`) resolves my §0.5 gap ✓; `F + 2mK` ample for `m > C_F` ✓ |
| Thm 12.2, 12.2a | affine involution, (R5) satisfied ✓ |
| Thm 12.3 | Steps 1–4 match my §0.5; the improvement "no `χ ≥ 0` needed" is right (quadratic term dominates) ✓ |
| Thm 13.2, 13.3, 13.5, 13.7 | ✓; Thm 13.3/Cor 12.4a is the structural output: any model-uniform `h⁰` fails, so the Euler product must enter `h⁰` as **unimodularity**, not as weights |
| Prop 14.1–14.3 | ✓; `D^W` is not the colimit, the Hodge-index shape lives in the Weil completion — my §1 sentence was wrong as stated, repaired correctly |

## 2. Findings

**LF1 (MAJOR, hypothesis).** Proposition 12.6 assumes "all zeros of `Z` in `0 < Re s < 1`". For `Z = Ξ_a` the zeros are `ρ ± a`, with real parts in `(−a, 1+a)`; the hypothesis **fails for the very falsifier the proposition exists to cover**, unless one knows `a < Re ρ < 1−a`, which is a statement about the zeros. Repair: replace by "all zeros in `|Re s − ½| < θ`" (for `Ξ_a`, `θ = ½+a` gives `(−a, 1+a)` ✓), check that the Laplace transform of Lemma 11.9 is taken on `Re s > ½+θ` and that the poles `p ∈ P` are not zeros (`Z(p) > 0` since `Z > 0` on `R` ✓). Theorems 12.4 and 13.3 depend on Prop 12.6 and must be re-read after the repair.

**LF2 (MAJOR, proof).** Theorem 12.4 needs the `Ξ_a`-analogue of Paper 45 Thm 10.4 and gives it in a parenthetical ("that analogue is available: …"). That is the load-bearing step of the falsifier theorem and must be a labelled proposition with the hypotheses of Thm 10.4 (`106_11` (20)–(21) interpolation, (E6), (E3d)) verified for `Ξ_a` one by one — including the rank-4 primitive sector (four interpolation conditions instead of two) and the quartet structure of an off-line zero of `Ξ_a`.

**LF3 (MINOR, false sentence).** Definition 11.4 says `h = F⋆G^∨` is "real and even when `F,G` are real, by `h^∨ = h`". False for `F ≠ G`: `(F⋆G^∨)^∨ = F^∨⋆G`. Harmless because `W_{fin}+ω_∞` is even, so `⟨h,W⟩ = ⟨h_{even},W⟩`, and `Σ_ρ Φ_{h_{even}}(ρ) = Σ_ρ Φ_h(ρ)` by `ρ ↦ 1−ρ`; equivalently define `I_∞` by polarization of the quadratic form. State it.

**LF4 (MINOR, proof quality).** Theorem 13.6's proof of (13.4) is sketched ("one gets first `B = O(m)`… that forces…"). The label `PROVED` for the growth bound is not yet earned by the text; either write the two inequalities out (largest active index, maximizing index) or downgrade (13.4) to a lemma with a full proof. The **route closure** is safe regardless: Theorem 13.7 closes it independently via Cor 12.4a.

**LF5 (MINOR, label).** Corollary 12.4a is a schema over "definitions uniform in `Z`" and should be labelled `PROVED (schema)` or `RESTATEMENT`; its force is entirely in Theorem 12.4 + Prop 12.6.

**LF6 (NOTE).** Thm 11.7(i) imports positivity of `K` from Titchmarsh/Pólya; note that given evenness it is elementary: each term `4π²n⁴e^{9u/2} − 6πn²e^{5u/2} > 0` for `u ≥ 0` since `2πn²e^{2u} > 3`. One line, removes an import.

**LF7 (NOTE, for the next campaign, not a defect).** Remark 13.6a's mechanism — `mK` dominates `τ_{log n}(ΠK)` only for `n ≲ √(log m)` — says the integral sections were sought in a one-parameter family (translates). In `C×C`, `h⁰(nD) ~ n²D²/2` comes from a two-dimensional lattice of sections. The right `h⁰`, if it exists, must count objects indexed by **pairs** (the Frobenius bi-grading `(n^{½}, n^{−½})`, or `Frob_m ⋆ Frob_n^†`), and Corollary 12.4a says the count must see `Frob_n ⋆ Frob_n^† = Δ^{(n)}`. This is §14.5 item (18), and it is where phase 136 should start.

## 3. Interim ruling

Part II does what the blueprint asked and refuses what it should have refused: eight blueprint claims refuted or repaired (all accepted by the lead), the duality problem dissolved (affine `σ_K`), the transfer theorem proved conditionally with a weaker hypothesis list than Def 6.8, the Euler-product locus identified, two natural `h⁰` constructions closed. No sign; §10 unchanged. LF1–LF2 must be repaired before the lead's decision; LF3–LF5 in the same round. Pending: R135_001 (builder report), R135_002 (hostile audit), then one repair round.


## 4. Comparison with the hostile audit R135_002 (read after §§1–3 were written)

| hostile | lead | ruling |
|---|---|---|
| M1 FATAL (Cor 12.4a is a schema over *definitions*, invalid as stated; listing `Z` among the data makes it assert that no `h⁰` exists at all) | LF5 saw the label problem, **not** the vacuity | **accepted, upgraded**. Cor 12.4a must be recast: "if `h⁰` is defined uniformly in `Z` **and the proof of (a),(b′),(c) uses only the listed data**, then it transfers" — a heuristic principle, label `RESTATEMENT (schema)`, and Remark 12.4b's "main structural output" is demoted. Theorems 13.3 and 13.7 lose their proof and must be re-proved by the growth bound or withdrawn |
| M2 (parity in Def 11.4) | LF3 | accepted; polarization |
| M3 (Thm 11.12 counts multiplicity) | missed by lead | **accepted**. Repair: import Conrey (1989) / Levinson: a positive proportion `≥ 0.4` of zeros are simple, so distinct zeros in `\|s−½\| ≤ r` are `≥ c·r log r`, still `≫ O(r)`. `CLASSICAL` import (X18). Propagate to Paper 45 Rem 12.4a and Paper 43 Rem 14.1a |
| M4 (Prop 12.6 hypothesis excludes `Ξ_a`) | LF1 | accepted; strip `\|Re s − ½\| < θ` |
| M5, M6 (Prop 12.6 "line-by-line" label; Thm 10.4 analogue in a parenthesis) | LF2 | accepted: write the `Ξ_a` sufficiency proposition in full, including the rank-4 `Π_P` and (E2)'s last clause |
| M7 (`Λ(n) = 0` off prime powers ⇒ zero generators; Thm 13.5(i),(ii) false as stated) | missed by lead | **accepted**; index by prime powers |
| M8 (Thm 13.6 proof not a proof) | LF4 | accepted; full proof or downgrade |
| M9 (archimedean kernel form of `ω_∞` used beyond `C_c^∞`) | missed by lead | **accepted**: prove the kernel representation of `ω_∞` on `D^W` (equality of distributions on `C_c^∞`, then extension by the decay of `D^W`), or bound the digamma integral directly |
| M10–M15 minor | — | accepted as listed |
| M16 (reduction one-directional) | LF7 | agreed; it is the open problem, stated as such |
| M17 (normalization of (11.7) is twice the usual `Φ`, correct for `Ξ = ξ(½+iτ)`) | my §0.1 | consistent |

Lead-only items kept: LF6 (elementary positivity of `K`), LF7 (two-parameter sections for the next campaign).

**Ruling for round 2.** Repairs M1–M9 are mandatory; the honest expected outcome is that §13's route closures rest on Theorem 13.6 (repaired, with prime-power indexing) alone, and that "the Euler product must enter `h⁰` as unimodularity" becomes a **heuristic** (Remark), not a theorem. No new numerics beyond a fast mode for the two long scripts (owner's rule: pure mathematics first; computation only where strictly necessary).
