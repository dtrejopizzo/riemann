# R147.003 — Builder round 2, phase 147: repairs, and the χ-graded carrier

*Builder: Opus 5. Date 2026-09-14. Read in full before writing: `R147_002_HOSTILE_AUDIT.md`
(verdict **ACCEPT WITH REPAIRS**; 0 FATAL, 6 MAJOR, 11 MINOR, 5 NOTES), `R147_001_BUILDER_ROUND1.md`,
`R147_000_LEAD_BLUEPRINT.md`, `CORPUS_CHECK_R147b.md`. Re-read for the repairs: Paper 46
**Definition–Theorem 11.7** (`main.md:2164`), **Theorem 14.3** (`:3732`), **Lemma 19.17** (`:6167`),
**Theorem 19.23** (`:6292`), §12.2 RECORD NOTE and §20; Paper 44 §3bis; phase 139 `R139_001` D.19.4a,
**D.20.2/(D.20.3)**, `R139_004` **H4 (CLOSED)**; `R140_001` D.22; `R145_001` (145.8)–(145.10).
**`R147_001` is not overwritten**; its corrections are appended there as a dated *Corrections of record*
block. All six MAJORs and all eleven MINORs are discharged in Part A; Part B is the construction the
audit says the round owed (MAJOR 5). Scripts: `scripts/graded_support.py` (new), and the two of round 1.*

---

## §0 — Round 2 in one page

**Part A (repairs).** Three of round 1's four advertised results do not survive, and they are withdrawn:
`K ∈ 𝓔` is Paper 46 Theorem 11.7(i) (not new, and *proved* there, strictly, term by term); the
"`𝓔` contains a class with zeros right of `1`" is a two-line triviality that needed no Epstein and no
Davenport–Heilbronn; and "this kills the horn *enlarge the effective cone*" is a non sequitur that
contradicts round 1's own D.51.5(c). The `\cos(π/m)` lemma was proved wrongly and is corrected
(`\cos(π/m)` for `m` even, `\cos(π/(2m))` for `m` odd, argmin `π/m` resp. `π/(2m)`). The two carriers
are separated throughout: the collapse is a statement about the **radial realization map**
`R : \mathrm{Corr}(C_{K,S}) → \mathrm{End}(D^W)`, not about "the carrier". What survives, and is the
round's durable contribution, is exactly that: **`R(Γ_σ) = \mathrm{id}`.**

**Part B (the χ-graded carrier — the construction round 1 declared nonexistent).** Phase 139 Theorem
D.20.2 already supplies a χ-graded Weil form. On
`𝒟_K := ⊕_{χ ∈ \widehat G} D^W` with `I^{(K)} = Σ_χ I^{(χ)}` (the `χ`-slot carrying the zeros of
`Λ(s,χ)`), the group ring acts by `χ(σ)` on the `χ`-slot — **not** by the augmentation — and the
blueprint's formula is **CONFIRMED, not refuted**:

    I^{(K)}(Γ_σ E, Γ_τ F) \;=\; Σ_{χ ∈ \widehat G} χ(στ^{-1})\; I^{(χ)}(E_χ, F_χ) ,

unconditional for abelian `K/Q`. The character table does enter the intersection numbers. The
realizable effective cone there is the isotypic image of the **non-radial** nonnegative tests on
`C_{Q,S}` (class field theory: `C_{Q,S} ↠ G`), whose extreme rays are the point masses
`δ_{(u,g)}`, `u ∈ R`, `g ∈ G`; the Galois correspondences are the **translations** by norm-one ideles
(R146_005's "the arithmetic Frobenius is a translation of the class group" — here a positive), and the
support function at a zero `ρ = ½+iγ` of `Λ(s,χ_0)` is

    S(γ,θ,m) \;=\; \max_{0 ≤ k < m}\, s\!\left(γ,\ θ - \tfrac{2πk}{m}\right),\qquad m := \mathrm{ord}\,χ_0 .

**Three numbers decide the phase** (`scripts/graded_support.py`, `--fast`, margins printed):

| | value | meaning |
|---|---|---|
| `S(γ,θ,1) = s(γ,θ)` | `s(γ_1,π/2) = 0.998456` (corpus `s_1 = 0.99846016`, grid margin `3.7×10^{−6}`) | **at every zero of `ζ` the constant is unchanged, for every `K`** |
| `S(γ_1,π/2,m) = 1` **exactly** iff `4 ∣ m` | `1.000000000` for `m = 4,8,12` | the fixed-direction bound **is** lifted — but only at zeros of `L(s,χ)` with `4 ∣ \mathrm{ord}\,χ`. **FLAGGED**; falsifiers run in §D.55.7 |
| `σ(γ,m) := \min_θ S(γ,θ,m) < 1` for every finite `m` | `γ_1`: `0.998456 (m{=}1,2)`, `0.999613 (m{=}4)`, `0.999956 (m{=}12)`; `d_0 = 324 → 1294 → 11313` | **the defect theorem still runs**, in a direction `θ` outside the finite bad set `πZ + (2π/m)Z` |

**Answer to B6.** `Z[G]` **does** supply a genuine `+` on the graded carrier — the classes
`Γ_g δ_{(u,1)} = δ_{(u,g)}` have coefficient `χ(g) ∈ μ_m` in the `χ`-slot, negative or complex, exactly
the analogue of the model's `[Γ_i] = ½[Γ_π] − ½[Δ] − F_1 + F_2` — and it is **useless for `ζ`**, by a
theorem:

> **Theorem D.55.9.** In `𝒟_K` the `G`-invariant sector is exactly the `χ = 1` component, i.e. exactly
> the zeros of `ζ`. `Z[G]` acts nontrivially only on the `χ ≠ 1` components. Hence the Galois `+` is
> real, and lives entirely in the part of the spectrum that `ζ` does not occupy.

Recommendation unchanged, and now with a proof: close the Galois-ring thread.

---

# PART A — Repairs

## A.1 (MAJOR 1) `K ∈ 𝓔` is Paper 46 Theorem 11.7(i)

**WITHDRAWN as a result of this phase.** The correct statement, cited:

> **Paper 46, Definition–Theorem 11.7(i) (`CLASSICAL` + `PROVED`).** `K` is real, **even**, and
> `K(t) > 0` for every `t`. Import **(X12)** (Pólya, *Acta Math.* **48** (1926); Titchmarsh §10.1,
> (10.1.4) and the two following displays). Elementary proof inserted at phase 135 round 2 (finding LF6
> of `R135_003`): each term of (11.7) is `2πn²e^{5u/2}e^{−πn²e^{2u}}(2πn²e^{2u} − 3)` and
> `2πn² ≥ 2π > 3`, so `K > 0` for `u ≥ 0` and by evenness everywhere. Corpus numerical check
> (`scripts/polya_class.py --check`): `\min K = 1.0204×10^{−69}` on `t = −2.0(0.05)2.0`.

Round 1's `K(t) = e^{t/2}Σ_{n≥1}(4y²−6y)e^{−y}`, `y = πn²e^{2t}`, **is** (11.7) after substitution
(`4y²−6y = 2y(2y−3)` and `y = πn²e^{2t}` give the displayed term). Round 1's evidence
`\min_t K = −1.47×10^{−15}` is **round-off**, not a minimum: the script's `YMAX` truncation makes
`K(±4.5)` identically `0`, so its "minimum" and its "evenness residual" are the same cancellation
artefact. Against a **proved strict positivity** this is worthless as evidence and is retracted as such.

**Label:** `RESTATEMENT` of Paper 46 Thm 11.7(i)/(X12). **Corpus-check §5 row 4 of round 1: `NOT NEW`.**
The §6 proposal to add "Remark 11.13b" to Paper 46 is **deleted**. Section [A] of
`scripts/epstein_cone_test.py` is retained **only** as the normalization check
`\deg K = 1.000000000` (Paper 46 Theorem 11.8(v)), which it does pass exactly.

## A.2 (MAJOR 2) The off-line-zeros statement, re-proved in two lines

**Theorem A.2 (`PROVED`, elementary, no numerics, no Epstein, no Davenport–Heilbronn).** Put
`φ(t) := e^{−t²}` and

    E := 3φ + τ_{\log 2}φ \; ∈ D^W ,\qquad E > 0\ \text{pointwise},\qquad \deg E > 0 .

Then `Φ_E(s) = Φ_φ(s)\,(3 + 2^{\,s−½})`, with `Φ_φ(s) = \sqrt π\,e^{(s−½)²/4}` entire and **zero-free**.
Hence `Φ_E(s) = 0` exactly when `2^{s−½} = −3`, i.e. on the vertical line

    \mathrm{Re}\,s = ½ + \frac{\log 3}{\log 2} = 2.0849625007…,\qquad
    \mathrm{Im}\,s ∈ \frac{π + 2πZ}{\log 2} ,

infinitely many zeros, **all** with `\mathrm{Re}\,s > 1`.

*Proof.* `Φ_{τ_aφ}(s) = e^{(s−½)a}Φ_φ(s)` (Paper 46 Lemma 11.2(iii)); `E > 0` since both summands are;
`\deg E = ∫E·2\cosh(t/2)dt > 0` by Theorem 11.13(i). The Gaussian transform is
`∫e^{−t²}e^{(s−½)t}dt = \sqrt π e^{(s−½)²/4}`, nowhere zero. ∎ `PROVED`

**Structural reason (already in the corpus):** pointwise nonnegativity constrains `Φ_E` **only on the
real axis** — `E ≥ 0, E ≢ 0 ⟹ Φ_E(s) > 0` for real `s` — and says nothing off it. Paper 46 §19.9: "the
image of the nonnegative cone … is a **moment cone**".

**Consequences for round 1.** D.51.6(ii) `STANDS`, now by Theorem A.2; its dependence on `D = 15`, on
`h > 1` and on **O-47.2 is deleted**, and O-47.2 itself is **WITHDRAWN** (closed at `R139_004` H4,
verified there: for the principal class `\overlineχ(𝔄_0) = 1`, so `Z_{Q_0} = \frac1hΣ_χL(s,χ)` is a
non-degenerate combination of `h ≥ 2` distinct Euler products and Davenport–Heilbronn applies). The
"round's sharpest general finding" framing is **deleted**. The Epstein membership table (D.51.5) is
kept, as a table about `K_Q`, with the label and citation of A.5 below.

## A.3 (MAJOR 3) What the horn actually is, and what round 1 may say about it

**WITHDRAWN:** "effectivity is zero-blind, therefore the repair horn *enlarge the effective cone* is
closed / killed" (round 1 §0 item 3, the blockquote after D.51.6, D.51.6(iii), D.54, README, §6).

**The horn, as Paper 46 states it** (§12.2 RECORD NOTE, pursued in §19.9 and §20 as `B4`): *"weaken (c)
by a defect vanishing at the degrees Theorem 12.3 actually uses, or **enlarge the effective cone**
(nonnegative Frobenius traces)"*. Its mechanism is the **support function**: Theorem 12.3 consumes the
cone through (b′), through Theorem 11.13(i) (`effective ⟹ \deg > 0`) and through Theorem 11.14(ii)
(`|I_∞(E,F)| ≤ C_F\deg E`), and the obstruction is exactly **Lemma 19.17** (`= D.31.4`) with
`s(γ,θ) < 1` (**Proposition 19.18** `= D.31.5`), feeding **Theorem 19.23** (`= D.31.10`). A cone
`𝓒 ⊇ 𝓔` with `s(𝓒;γ,θ) = 1` would lift that obstruction **whether or not `𝓒` contains classes with
off-line zeros** — indeed `\overline{\mathrm{Eff}}(E×E)` in the model has `s = 1` and is full of them.
(`B4`'s own fate is Remark 20.12: "`B4` is not an enlargement of the effective cone".)

**What round 1 is entitled to say, and no more:**

> **Proposition A.3 (`PROVED`).** For **no** cone `𝓒 ⊇ 𝓔` is there an implication
> "`E ∈ 𝓒 ⟹` every zero of `Φ_E` lies on `\mathrm{Re}\,s = ½`" — by Theorem A.2, already for `𝓒 = 𝓔`.

This is a proposition nobody in the corpus advanced; it is a clarification, not a closure. **To speak to
the actual horn one must compute `s` of the candidate enlargement** — which round 1 did not do, and
which **Part B does** (§D.55.5–D.55.7).

## A.4 (MAJOR 4) Two carriers, and the three ill-typed claims

**Definition A.4 (the radial realization map).** Let `\mathrm{Corr}(C_{K,S})` denote the `⋆`-algebra of
correspondences of Papers 43–44 (measures on `C_{K,S}×C_{K,S}`; carrier `D_A = C_c^∞(C_S)`), and
`D^W` Paper 46 Definition 11.1 (real functions **on `R`**). These are **different spaces**: Paper 46
**Theorem 14.3(i)** — "`D_A^∞` contains non-radial tests, **which `D^W` does not model**"; Paper 44
§3bis — "the **Frobenius family** … is **not** radial"; `R140_001:374` — "What exists is the **action**:
`\mathrm{Frob}_n` acts on radial classes by the modulus". Write

    R : \mathrm{Corr}(C_{K,S}) \longrightarrow \mathrm{End}(D^W)

for the **radial realization**: `R(𝔠)E := ` the modulus-pushforward of `𝔠 ⋆ \tilde E`, `\tilde E` the
radial lift of `E`.

**Theorem D.50.2′ (the collapse, correctly typed; `PROVED`; replaces round 1's D.50.2).**
For every `σ ∈ G`, `R(Γ_σ) = \mathrm{id}_{D^W}`. Equivalently, the composite
`Z[G] → \mathrm{Corr}(C_{K,S}) \xrightarrow{R} \mathrm{End}(D^W)` is the **augmentation** `Z[G] → Z`.

*Proof.* `|σ(x)|_{A_K} = |x|_{A_K}` (A1: `σ` permutes the places over each place of `Q` and
`|σx|_{σv} = |x|_v`; Neukirch II.§8, III.§1), so `σ` preserves every level set of the modulus and the
modulus-pushforward of `σ_*μ` equals that of `μ`. ∎ `PROVED`

**Upstairs, nothing collapses:** as correspondences `Γ_σ ≠ Δ` for `σ ≠ 1`,
`\mathrm{Frob}_{σ𝔫} ≠ \mathrm{Frob}_𝔫` when `σ𝔫 ≠ 𝔫`, and
`𝓔_{G,\mathrm{Frob}} ⊋ 𝓔_{\mathrm{Frob}}`. Round 1's D.50.1 is a theorem **about
`\mathrm{Corr}(C_{K,S})`** and `STANDS` there; every "= in the frame" in round 1 must be read "= after
`R`". The three ill-typed claims are retyped:

 (a) **D.50.3(ii) WITHDRAWN as stated.** `Δ ∉ D^W` (it is not a function), so `I_∞(Γ_σ,Γ_τ)` was not
   defined and "`= Δ·Δ = −∞`" was not a licensed evaluation. The licensed statement is
   **`I_∞^{(K)}(R(Γ_σ)E, F) = I_∞^{(K)}(E,F)` for all `E,F ∈ D^W`** — `σ`-independent. (The divergence
   `Δ·Δ = −∞` of Paper 44 Thm 8bis.2 / Paper 46 Prop. 14.2 remains true of its own object and is not
   used here.)
 (b) **D.50.9(i) DOWNGRADED.** "`𝓔_{\mathrm{Frob}} ⊆ 𝓔`" is false as typed: `R(\mathrm{Frob}_𝔫)` is a
   **point mass** at `u = \log N𝔫`, not an element of `D^W`. The conclusion survives by the point-mass
   computation: the ratio of `δ_{\log N𝔫}` is `|\cos(γ\log N𝔫 + θ)|/\cosh(\tfrac12\log N𝔫)`, hence

       s(𝓔_{\mathrm{Frob}};γ,θ) \;≤\; \sup_{u∈R}\frac{|\cos(γu+θ)|}{\cosh(u/2)} \;=\; s(γ,θ) ,

   which is all D.50.9(iv) and D.50.10 use. **`PROVED` in this form.**
 (c) **D.50.1(iv) vs D.50.3(iii).** `Γ_σ ⋆ \mathrm{Frob}_𝔫 ⋆ Γ_σ^{-1} = \mathrm{Frob}_{σ𝔫}` is a
   genuine identity **in `\mathrm{Corr}(C_{K,S})`**. The frame statement is the strictly weaker
   `R(\mathrm{Frob}_{σ𝔫}) = R(\mathrm{Frob}_𝔫)`, which holds because `N(σ𝔫) = N𝔫` and `R` retains only
   `N𝔫` (D.22.5(v)). Round 1's §6 Paper-44 bullet is corrected accordingly.

**Headline, rewritten.** Not "the frame's carrier is radial" but: **`Z[G]` collapses under the radial
realization.** (§0 of round 1, D.54 bullet 2 and the README are corrected; see A.9 and the new README.)

**MINOR 13.** §0 and the README must state `s(𝓔_{G,\mathrm{Frob}};γ_1,π/2) ≤ s_1`, not `=`. Done
throughout round 2. (The direction is the safe one for the FATAL rule.)

## A.5 (MINOR 7, 8, 9, 11, 12, 14, 15, 16, 17; NOTE 20, 21, 22) — the remaining repairs

**(MINOR 7) D.50.6 relabelled.** `(Γ_σ·Δ)_{\mathrm{Arak}}` was **defined** to be `\log N(𝔞_σ)` and no
intersection theory, and no archimedean Green's contribution (the infinite places, which `σ` permutes,
are absent), entered the proof. The name "Arakelov" is **withdrawn**. Restated:

> **Theorem D.50.6′ (the Hurwitz/different identity; `CLASSICAL-RESTATEMENT`).** For `σ ≠ 1` let
> `𝔞_σ ⊆ O_K` be the ideal generated by `\{σ(x)−x\}`. Then
> `Σ_{σ≠1}\log N(𝔞_σ) = \log N(𝔇_{K/Q}) = \log|d_K| = Σ_χ χ(1)\log 𝔣(χ)`.
> *Inputs, verbatim:* Hilbert's different formula `v_𝔓(𝔇) = Σ_{σ≠1}i_𝔓(σ)` (Serre, `Corps Locaux`
> IV §1 Prop. 4; Neukirch III.2.6), `N(𝔇) = |d_K|` (Neukirch III.2.9), conductor–discriminant
> (Neukirch VII.11.9). **No sign datum is produced**; this and phase 139 D.20.2 are the same theorem
> read twice (round 1's own Remark D.50.7, promoted into the statement).

**(MINOR 8) the ramification sentence, corrected.** *As printed in round 1:* "`v_𝔓(𝔞_σ) = 0` unless
`σ ∉ D_𝔓`" — **false**. *Correct:* `v_𝔓(𝔞_σ) = 0` **unless `σ ∈ I_𝔓`**. (For `σ ∉ D_𝔓` pick
`x ∈ 𝔓 ∖ σ^{-1}𝔓`, so `v_𝔓(σx−x) = 0`; for `σ ∈ D_𝔓 ∖ I_𝔓` the residue action is nontrivial, again
`0`.) Two missing steps supplied: (a) `v_𝔓(𝔞_σ) = i_𝔓(σ)` uses the **density of `O_K` in `O_𝔓`**,
since Hilbert's formula is stated for a *local* generator and `O_K` need not be monogenic; (b) the model
check `Σ_{σ≠1}\#\mathrm{Fix}(σ) = 8` is the **tame** Riemann–Hurwitz identity, applicable here because
`p = 5 ∤ |G| = 4` (Hartshorne IV.2.4 with the tameness hypothesis).

**(MINOR 9) D.51.7 relabelled `RESTATEMENT`, clause (iii) deleted.** `D^W` is defined (Paper 46
Definition 11.1) as a space of functions on `R` with a decay bound and **no reference to any field**, so
`𝓔 = \{E ≥ 0\}` is the same set for every `K` **by inspection**; Lemma D.50.2 is not needed and its
citation is removed. Clause (iii) ("induction and restriction of cones are the identity") is **deleted**:
no induction or restriction map on `D^W` is defined anywhere in the corpus. Clause (ii) carries
D.20.2's conditionality: `PROVED` for abelian `L/K`, `PROVED-CONDITIONAL` on Artin holomorphy otherwise.

**(MINOR 12) the blueprint's `χ(σ^{-1}τ)` formula: `REFUTED` → `NOT-APPLICABLE`, then CONFIRMED.**
Round 1 refuted it in the single-copy radial realization, where the left side is `σ`-independent
*because* `R(Γ_σ) = \mathrm{id}` — a reading the blueprint did not impose (it directed the computation
"*from the explicit formula for `ζ_K` decomposed by Artin characters (phase 139 D.20 machinery)*").
Relabelled **`NOT-APPLICABLE` (to the radial realization)**, and **proved on the graded carrier** in
§D.55.3 below.

**(MINOR 14) D.53.5(v) hypothesis corrected.** R145 Theorem D.41.13's hypothesis is
`d²(1−s²) > d − 4χ`, which reduces to `d > (1−s²)^{-1} = 5` **only for `χ ≥ 0`**. Restated: *"for every
`χ ≥ 0` and every `d > 5`; in general for every `d` with `d²(1−s²) > d − 4χ`."*

**(MINOR 15) D.53.4 typed, script docstring fixed.** The integral identity is
`2[Γ_i] = [Γ_π] − [Δ] − 2F_1 + 2F_2` in `\mathrm{NS}(E×E)`; equivalently
`[Γ_i] = ½[Γ_π] − ½[Δ] − F_1 + F_2` in `\mathrm{NS}(E×E) ⊗ Q`. The docstring of
`scripts/model_intersections.py` (which printed `+F_1 − F_2`, against its own code) is **corrected**.

**(MINOR 16) citation fixed.** Paper 46 open item (21) is the **kernel representation of `ω_∞` on
`D^W`** (entered with finding M9 of `R135_002`) and has nothing to do with non-radial tests. All three
occurrences (round 1 Remark D.50.4, O-47.1, D.54) now cite **Theorem 14.3(i)** and Paper 44 §3bis.

**(MINOR 17) the `θ^*` degeneracy.** `Z[i]` is `i`-stable, so the generator ratios are `π/2`-periodic in
`θ` and the minimiser is a **coset of four**: `θ^* ∈ \{\arctan½,\ \arctan½ + π/2,\ …\} =
\{0.463648, 2.034444, …\}`. The table now reads `θ^* = \arctan\tfrac12` (one of four).

**(NOTE 20) the model's two roles, moved into §0.** In `E/F_5` the group `μ_4` is **both** the deck
group of `E → E/μ_4 = P¹` (the analogue of `\mathrm{Gal}(K/Q)` for
`\mathrm{Spec}\,O_K → \mathrm{Spec}\,Z`) **and** a subring of `\mathrm{End}(E)` acting on the Tate module
by a primitive 4th root of unity. **Only the first role has an arithmetic counterpart.** Round 1 said
this in D.54 and not in §0; it is now said first. `R145_004` **Warning 1** binds any attempt to carry
D.53.1's trace form `\tildeγ_α·\tildeγ_β = −\mathrm{Tr}(α\barβ)` across: positing positivity of a trace
form on an endomorphism ring **is** RH. Nothing is carried across here.

**(NOTE 21) the `Ξ_a` verdict, reworded.** Theorem D.51.1 `STANDS` and is a tautology: once
`R(Γ_σ) = \mathrm{id}` collapses everything to `\mathrm{id}`, every conclusion is a statement about
`\mathrm{id}`, which exists for `Ξ_a` with `G = 1`. It is evidence about the **radial realization**, not
about the Galois idea; §D.55.7 runs `Ξ_a` against the graded carrier instead.

**(NOTE 22, MINOR 10) the Epstein table: label and provenance.** Phase 139 **Theorem D.19.4a**
(`PROVED`) already proves `K_Q > 0` **false** for the family `Q_k = x²+ky²`, `k` large (via a real zero
of `Λ_{Q_k}` in `(σ_0,1)`; `R139_005` line 14). So `K_Q ∉ 𝓔` for infinitely many principal forms is a
**theorem of the corpus**, and round 1's table **extends** it rather than discovering it. The two are
complementary: D.19.4a detects non-membership through a **real zero**; the table detects it by direct
pointwise evaluation in cases where no real zero is visible at the sampled points (`Ξ_Q > 0` at
`0,¼,½,¾,1` in all eleven cases). §5 row 5 of round 1 is corrected from "NEW" to
**"extends D.19.4a"**. **Label of D.51.5: `CERTIFIED` (numerically), not `PROVED`** — grid
`t ∈ [−4.5,4.5]` step `0.05`, adaptive lattice radius, evenness residual `≤ 3.1×10^{−16}`, sign changes
at `0.24`–`0.74` of the class maximum, i.e. eleven orders of magnitude over the noise.

## A.6 (MAJOR 6) The `\cos(π/m)` lemma, corrected and proved

**Lemma A.6 (`PROVED`; replaces round 1's D.53.5(ii) proof).** For `m ≥ 1`,

    L(m) \;:=\; \min_θ \max_{0 ≤ k < m} \left|\cos\!\left(θ + \tfrac{2πk}{m}\right)\right|
    \;=\; \begin{cases} 0 & m ≤ 2,\\[2pt] \cos(π/m) & m\ \text{even},\ m ≥ 4,\\[2pt]
                        \cos\!\big(π/(2m)\big) & m\ \text{odd},\ m ≥ 3,\end{cases}

attained at `θ^* = π/m` (`m` even) resp. `θ^* = π/(2m)` (`m` odd), modulo the symmetry group of the
configuration.

*Proof.* `|\cos|` has period `π`, so the relevant data is the multiset `\{θ + 2πk/m \bmod π\}`. If `m`
is even, `\{2πk/m \bmod π\} = \{2πj/m : 0 ≤ j < m/2\}`: `m/2` points of `[0,π)` equally spaced with gap
`2π/m`. If `m` is odd, `\gcd(2,m) = 1` and `\{2πk/m \bmod π\} = \{πk/m : 0 ≤ k < m\}`: `m` points with
gap `π/m`. In either case write `d` for the gap (`2π/m` resp. `π/m`). `\max_k|\cos|` is attained at the
point of the configuration **farthest from `π/2`**, i.e. nearest to `0` or `π`; translating `θ` so that
the gap straddling `0 ≡ π` is centred puts that nearest point at distance `d/2`, giving
`\max_k|\cos| = \cos(d/2)`, and any other translation moves a point strictly nearer to `0` or `π`,
strictly increasing the max. So `L(m) = \cos(d/2)`, which is `\cos(π/m)` resp. `\cos(π/(2m))`, at
`θ^* = d/2`. For `m ≤ 2` the configuration is a single point, which can be placed at `π/2`. ∎ `PROVED`

*Certified independently,* `scripts/graded_support.py` §[1], `m = 1,…,12`: every numeric value agrees
with the closed form to `≤ 1.1×10^{−16}`, and every argmin agrees with `θ^* = d/2`. Table:

| `m` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `L(m)` | 0 | 0 | `0.866025` | `0.707107` | `0.951057` | `0.866025` | `0.974928` | `0.923880` | `0.984808` | `0.951057` | `0.989821` | `0.965926` |
| round 1's `\cos(π/m)` | — | 0 | `0.5` ✗ | `0.707107` ✓ | `0.809017` ✗ | `0.866025` ✓ | ✗ | ✓ | ✗ | ✓ | ✗ | ✓ |

**Propagation.** Round 1's D.53.5(ii) **inequality** `s(𝓔_{\mathrm{Aut,Frob}}) ≥ L(|G|)` `STANDS`; the
**equality** `L(m) = \cos(π/m)` is corrected; D.53.5(iii) `STANDS with corrected constants` — the gain
is still bounded away from `1` for every finite `m` (`L(m) < 1` always), but for odd `m` it approaches
`1` twice as fast (`\cos(π/(2m)) = 1 − π²/(8m²) + O(m^{-4})`), and `L(m) = 0` for `m ≤ 2` (an
automorphism group `\{±1\}` gives **no** gain — round 1's qualitative claim, now with the right reason:
the single point mod `π`). §5 row 8 corrected.

## A.7 (MINOR 10) The two grid-only equalities, now proved

**Proposition A.7a (`PROVED`; round 1's `s_{\mathrm{End}} = 2/\sqrt5`).** On `E/F_5` with
`\mathrm{End}(E) = Z[i]`,

    s_{\mathrm{End}} = \min_θ \sup_{α ∈ Z[i]∖0} \frac{2|\mathrm{Re}(e^{iθ}α)|}{1+N(α)} = \frac2{\sqrt5},
    \qquad θ^* = \arctan\tfrac12\ (\text{one of four}).

*Proof.* The generator's ratio is `≤ 2\sqrt{N(α)}/(1+N(α))`, which is `≤ 2\sqrt5/6 = 0.745356` for
`N(α) ≥ 5` and `= 4/5` for `N(α) = 4`; both are `< 2/\sqrt5 = 0.894427`. So only `N(α) ∈ \{1,2\}`
matters: the units `\{±1,±i\}` give `u(θ) := \max(|\cosθ|,|\sinθ|)`, and `\{±1±i\}` give
`\tfrac{2\sqrt2}3 u(θ−π/4)`. Both are `π/2`-periodic and the pair is symmetric about `θ = π/4`, so
minimise on `[0,π/4]`, where `u(θ) = \cosθ` decreases and `\tfrac{2\sqrt2}3\cos(π/4−θ)` increases. They
tie when `\cosθ = \tfrac23(\cosθ+\sinθ)`, i.e. `\tanθ = ½`, giving `\cosθ = 2/\sqrt5`. ∎ `PROVED`

**Proposition A.7b (`PROVED`; round 1's `s_{\mathrm{Aut,Frob}} = 1/\sqrt2`).** With generators
`α = σπ^n`, `σ ∈ μ_4`, `n ∈ Z` (`π = 1+2i`, `θ_u = \arctan 2`):
 (`≥`) the `n = 0` generators give `\max_k|\cos(θ+kπ/2)| = u(θ) ≥ 1/\sqrt2`, so `s ≥ 1/\sqrt2`;
 (`≤`) at `θ = π/4` the `n = 0` entry is `1/\sqrt2`; the `|n| = 1` entries are
   `\max_k|\cos(π/4 ± θ_u + kπ/2)|/\cosh(\tfrac12\log5) = |\sin(π/4+θ_u)| \cdot \tfrac{\sqrt5}3
   = \tfrac3{\sqrt{10}}\cdot\tfrac{\sqrt5}3 = \tfrac1{\sqrt2}` — an **exact three-way tie**; and every
   `|n| ≥ 2` entry is `≤ 1/\cosh(\log 5) = 5/13 = 0.384615 < 1/\sqrt2`. ∎ `PROVED`

**Remaining `CERTIFIED`:** `s_{\mathrm{Frob}} = 2/3`. The `≤` is proved (at `θ = π/2` the `n = 0` entry
vanishes, the `n = ±1` entries tie at `\sinθ_u\cdot\tfrac{\sqrt5}3 = \tfrac23`, and `|n| ≥ 2` entries
are `≤ 5/13`); the `≥` (i.e. that `θ = π/2` is the minimiser) is a grid search,
`\min_θ` over `2×10^5` points, margin to the closed form `\sqrt{4q−a²}/(q+1)` **exactly `0.0`**.
Labelled **`CERTIFIED`**. *(F-147-1 is unaffected and is `CONFIRMED` by the auditor, NOTE 18; the
sharper form recommended there — "run the finite check over `n ∈ Z`, not `|n| ≥ 2`" — is adopted.)*

---

# PART B — The χ-graded carrier (D.55)

*This is the construction the blueprint ordered (D.50 item 2, "from the explicit formula for `ζ_K`
decomposed by Artin characters"), which round 1 wrongly declared nonexistent (MAJOR 5). Its source is
phase 139 **Theorem D.20.2**, `PROVED` unconditionally for abelian `L/K`.*

## D.55.1 The carrier, the action, the form

**Standing hypothesis for §D.55:** `K/Q` **abelian** Galois, `G = \mathrm{Gal}(K/Q)`,
`\widehat G = \mathrm{Hom}(G,C^×)`; by class field theory `\widehat G` is a group of primitive Dirichlet
characters and `ζ_K = ∏_{χ∈\widehat G}L(s,χ)`, `ξ_K = ∏_χ Λ(s,χ)` with `Λ(s,1) = ξ` (phase 139
(D.20.2)). **Everything in §D.55 is unconditional in this case**; for non-abelian `K/Q` every statement
holds with `χ(σ)` replaced by `ρ_χ(σ)` and multiplicities `χ(1)`, conditionally on Artin holomorphy
(D.20.2's own label).

**Definition D.55.1.** `𝒟_K := ⊕_{χ ∈ \widehat G} D^W ⊗_R C`, with the real structure
`\overline{E_χ} = E_{\barχ}`. Write `E = (E_χ)_χ`.
 (i) **The action.** `Γ_σ · E := (χ(σ)E_χ)_χ` for `σ ∈ G`, extended `Z`-linearly to `Z[G]`. This is a
   faithful `Z[G]`-module structure; on a real packet `\{χ,\barχ\}` it is the real rotation by
   `\argχ(σ)`, so `𝒟_K` is a real `Z[G]`-module.
 (ii) **The form.** `I^{(K)}(E,F) := Σ_{χ ∈ \widehat G} I^{(χ)}(E_χ,F_χ)`, where

       I^{(1)}(E,F) := Φ_E(0)Φ_F(1)+Φ_E(1)Φ_F(0) − Σ_{ρ ∈ Z(ξ)}Φ_E(ρ)Φ_F(1−ρ)   (Paper 46 (11.6)),
       I^{(χ)}(E,F) := −Σ_{ρ ∈ Z(Λ(·,χ))}Φ_E(ρ)Φ_F(1−ρ)                 (χ ≠ 1; no polar block).

 (iii) **The diagonal embedding** `ι : D^W → 𝒟_K`, `E ↦ (E)_χ`.

**Theorem D.55.2 (`PROVED`; the form is phase 139's, and `ι` is an isometry).**
 (i) For `χ ≠ 1`, `Λ(·,χ)` is **entire** (Hecke, primitive non-trivial character), so
   `I^{(χ)}` carries no polar block and `Φ_{K_χ}(0) = Φ_{K_χ}(1) = 0`;
 (ii) `I^{(K)}(ιE, ιF) = I_∞^{(K)}(E,F)`, the Weil form of `ξ_K` on the radial carrier — this is
   **exactly (D.20.4)** of phase 139 Theorem D.20.2, `PROVED` unconditionally here;
 (iii) `𝓝^{(K)} := \mathrm{rad}\,I^{(K)} = ⊕_χ 𝓝^{(χ)}`, and `ι^{-1}(𝓝^{(K)}) = 𝓝_∞^{(K)}`.

*Proof.* (i) is round 1's Lemma D.51.3 (entirety of `Λ(\cdot,χ)`, so `Ξ_χ(0) = Ξ_χ(1) = 0`). (ii) The
zero multiset of `ξ_K` is the disjoint union of those of the `Λ(\cdot,χ)` (D.20.2's proof), the polar
blocks of `ξ_K` and `ξ` are equal (weight one, `P = \{0,1\}`, D.20.2's repair H5(c)), and
`Φ_{ιE}(ρ) = Φ_E(ρ)` in every slot. (iii) Componentwise. ∎ `PROVED`

**Definition–Theorem D.55.3 (the canonical class, degrees, rulings; `PROVED`).**
`K_K := (K_χ)_χ` with `Φ_{K_χ} = Ξ_χ := ½s(s−1)Λ(s,χ)` (the Pólya kernel of `Λ(\cdot,χ)`; real for real
`χ`, and `K_{\barχ} = \overline{K_χ}`, so each packet contributes a real class). Then:
 (i) `\deg E := I^{(K)}(E, 2K_K) = \deg E_1` — **the degree sees only the trivial component**, because
   `I^{(χ)}(E_χ,K_χ) = −Σ_ρ Φ_{E_χ}(ρ)Ξ_χ(1−ρ) = 0` for `χ ≠ 1` (the `ρ` are zeros of `Λ(\cdot,χ)` and
   the zero multiset is `ρ ↦ 1−ρ` stable, Lemma D.20.2a₀);
 (ii) `\deg K_K = \deg K = 1`; `\deg K_χ = 0` for `χ ≠ 1`, i.e. **every `χ ≠ 1` component is
   primitive**;
 (iii) the **rulings** (the functionals `Φ(0)`, `Φ(1)`, hence the bidegree) live **only in the `χ = 1`
   component**;
 (iv) **`Γ_σ` preserves the degree**: `\deg(Γ_σE) = 1(σ)\deg E_1 = \deg E`; and
   `Γ_σ` is an **isometry** of `I^{(K)}`: `I^{(K)}(Γ_σE,Γ_σF) = Σ_χ|χ(σ)|²I^{(χ)} = I^{(K)}(E,F)`.

*Proof.* As indicated; (iv) uses `|χ(σ)| = 1` and, for the adjoint, `Γ_σ^† = Γ_{σ^{-1}}` acting by
`\overline{χ(σ)}`. ∎ `PROVED`

## D.55.3 The blueprint's formula, confirmed

**Theorem D.55.4 (the character table enters the intersection numbers; `PROVED`, unconditional for
abelian `K/Q`).** For all `E,F ∈ 𝒟_K` and all `σ,τ ∈ G`,

    I^{(K)}(Γ_σ E,\ Γ_τ F) \;=\; Σ_{χ ∈ \widehat G} χ(στ^{-1})\; I^{(χ)}(E_χ, F_χ) ,

and in particular, on the diagonal image (`E = ιE_0`, `F = ιF_0`, `E_0,F_0 ∈ D^W`),

    I^{(K)}(Γ_σ ιE_0,\ Γ_τ ιF_0)
      \;=\; χ_1(στ^{-1})\Big[\,\underbrace{Φ_{E_0}(0)Φ_{F_0}(1)+Φ_{E_0}(1)Φ_{F_0}(0)}_{\text{polar}}
            - \!\!\sum_{ρ∈Z(ξ)}\!\!Φ_{E_0}(ρ)Φ_{F_0}(1−ρ)\Big]
            \;-\; \sum_{χ≠1} χ(στ^{-1})\!\!\sum_{ρ∈Z(Λ(·,χ))}\!\!Φ_{E_0}(ρ)Φ_{F_0}(1−ρ) .

For general (non-abelian) `K/Q` the same holds with `Σ_χ χ(1)χ(στ^{-1})`, `PROVED-CONDITIONAL` on Artin
holomorphy (the label of D.20.2).

*Proof.* `Γ_τ^† = Γ_{τ^{-1}}` acts on the `χ`-slot by `\overline{χ(τ)} = χ(τ^{-1})`, so
`I^{(K)}(Γ_σE,Γ_τF) = Σ_χ χ(σ)χ(τ^{-1})I^{(χ)}(E_χ,F_χ)` and `χ(σ)χ(τ^{-1}) = χ(στ^{-1})`. The
displayed specialisation is Definition D.55.1(ii) with `Φ_{ιE_0}(ρ) = Φ_{E_0}(ρ)` in every slot. ∎
`PROVED`

> **This is the blueprint's D.50 item 2, correct.** Its expected shape —
> `(\text{polar}) − Σ_χ χ(1)χ(σ^{-1}τ)\cdot(\text{zero sum of } L(s,χ))` — is reproduced exactly, with
> `στ^{-1}` in place of `σ^{-1}τ` (an inessential convention: `G` is abelian here, and `χ(στ^{-1}) =
> \overline{χ(σ^{-1}τ)}`, equal on real packets). Round 1's `REFUTED as stated` is **withdrawn** and
> replaced by `NOT-APPLICABLE (to the radial realization)` + this theorem (MINOR 12).
>
> **Consistency with the collapse (no contradiction).** `R(Γ_σ) = \mathrm{id}` (A.4) and Theorem D.55.4
> are both true, of different objects. `ι` is an isometry of forms but is **not** `Z[G]`-equivariant:
> `Γ_σ ιE_0 = (χ(σ)E_0)_χ ∉ ι(D^W)` for `σ ≠ 1`. The radial sector `ι(D^W)` is not a `Z[G]`-submodule
> of `𝒟_K`, and that — not any error — is why the same group acts by the augmentation downstairs and by
> the character table upstairs.

## D.55.4 The effective cone: three candidates, and which one is right

**(i) Componentwise nonnegativity.** `𝓔^{(i)} := \{E : E_χ ≥ 0\ \text{pointwise},\ ∀χ\}`.
**Rejected.** It is **not `Z[G]`-stable** (`χ(σ)E_χ` is not nonnegative once `χ(σ) ∉ R_{≥0}`; already
for a real `χ` with `χ(σ) = −1`), so it is not a cone of correspondence-images; and its support function
is `s(γ,θ)` componentwise, i.e. **no gain**. It has no arithmetic source.

**(ii) The realizable cone.** By class field theory `C_{Q,S} ↠ G` (the Artin map), so write a test on
`C_{Q,S}`, modulo the part the frame does not see, in the coordinates `(u,g)`, `u = \log|x|`, `g ∈ G`.
Define the **isotypic transform** `f ↦ (f_χ)_χ`, `f_χ(u) := Σ_{g∈G}χ(g)f(u,g)`, and

    𝓒 \;:=\; \big\{ (f_χ)_χ \;:\; f ≥ 0\ \text{on}\ R×G,\ f ≢ 0 \big\} \subset 𝒟_K .

**Accepted.** This is the right analogue of "effective on the square of `\mathrm{Spec}\,O_K`":

> **Theorem D.55.5 (`PROVED`).**
>  (a) `𝓒` is a convex cone, `Z[G]`-stable, with extreme rays the **point masses** `δ_{(u,g)}`, whose
>    image is `(χ(g)δ_u)_χ`;
>  (b) the Galois correspondences act on `𝓒` as the **translations** of `C_{Q,S}` by norm-one ideles:
>    `Γ_g δ_{(u,h)} = δ_{(u,gh)}` — this is `R146_005`'s *"the arithmetic Frobenius is a translation of
>    the class group, not a homomorphism"*, here a **positive**: translations are effective
>    correspondences of bidegree `(1,1)` (graphs of measure-preserving bijections);
>  (c) `ι(𝓔) ⊂ 𝓒`: `ιE` is the image of `f = E ⊗ δ_{g=1}`, the test concentrated on the identity coset.
>    Hence `𝓒 ⊇ ι(𝓔)` and `𝓒 ⊇ Z[G]·ι(𝓔)`, so `𝓒` contains the blueprint's `𝓔_G`;
>  (d) **the degree gate (4b) holds**: `\deg (f_χ)_χ = \deg f_1 = ∫\big(Σ_g f(u,g)\big)2\cosh(u/2)du > 0`
>    for `f ≥ 0`, `f ≢ 0` — the analogue of Paper 46 Theorem 11.13(i);
>  (e) **the `G`-invariants of `𝓒` are exactly the `χ = 1` sector**: `f` uniform in `g` iff `f_χ = 0`
>    for all `χ ≠ 1`.
>
> *Proof.* (a) Linearity of `f ↦ (f_χ)` and extremality of point masses in the cone of nonnegative
> measures. (b) `Γ_g` acts by `f ↦ f(·,g^{-1}\cdot)`, whence `f_χ ↦ χ(g)f_χ` — Definition D.55.1(i) —
> and on `C_{Q,S}` this is translation by any idele with Artin symbol `g`, which has `|a| = 1` (it may be
> taken in `\widehat{Z}^×`), so it preserves the modulus and has bidegree `(1,1)` by the computation of
> round 1 D.50.1(iii). (c) `f = E⊗δ_{g=1}` gives `f_χ = χ(1)E = E` for every `χ`. (d) `f_1 = Σ_gf ≥ 0`
> and Theorem 11.13(i). (e) Fourier inversion on the finite group `G`. ∎ `PROVED`

**(iii) The induced cone** `ι(𝓔)` — the image of the radial effective cone. It is the sub-cone of `𝓒`
on the identity coset (D.55.5(c)); its support function is `s(γ,θ)`, **no gain**; it is `Z[G]`-stable
only under the augmentation. So `ι(𝓔) ⊊ Z[G]·ι(𝓔) ⊆ 𝓒`, and **(ii) is the object to compute with**.

## D.55.5 The support function of `𝓒`

**Theorem D.55.6 (`PROVED`).** Let `ρ = ½+iγ` be a zero of `Λ(s,χ_0)`, `m := \mathrm{ord}(χ_0)` in
`\widehat G` (so `χ_0(G) = μ_m`). Then, with `s(γ,θ) := \sup_{u∈R}|\cos(γu+θ)|/\cosh(u/2)`
(Definition D.31.3 `=` Paper 46 Lemma 19.17's constant),

    S(γ,θ,m)\;:=\;\sup_{E' ∈ 𝓒}\frac{\big|\mathrm{Re}\big(e^{iθ}Φ_{E'_{χ_0}}(ρ)\big)\big|}{\tfrac12\deg E'}
    \;=\; \max_{0 ≤ k < m}\ s\!\left(γ,\ θ-\tfrac{2πk}{m}\right) .

*Proof.* By D.55.5(a) it suffices to evaluate on the extreme rays `δ_{(u,g)}`, for which
`Φ_{(δ_{(u,g)})_{χ_0}}(ρ) = χ_0(g)e^{iγu}` and `\tfrac12\deg δ_{(u,g)} = \cosh(u/2)`; so the ratio is
`|\cos(γu + θ + \arg χ_0(g))|/\cosh(u/2)`, and `\argχ_0(g)` runs over `\{2πk/m\}` as `g` runs over `G`.
Take the sup over `u ∈ R` at each `k`. ∎ `PROVED`

**Numerics of record** (`scripts/graded_support.py --fast`; `γ_1 = 14.134725141734693790` is (X19)'s
first zero; the `u`-grid is `[−8,8]` at `4×10^4` points and the `θ`-grid `[0,π)` at `2520` points, with
`2·2520` divisible by every `m` used, so the rotations are exact index shifts):

| | `m=1` | `m=2` | `m=3` | `m=4` | `m=5` | `m=6` | `m=8` | `m=12` |
|---|---|---|---|---|---|---|---|---|
| **`S(γ_1,π/2,m)`** (fixed direction) | `0.998456` | `0.998456` | `0.999825` | **`1.000000`** | `0.999934` | `0.999825` | **`1.000000`** | **`1.000000`** |
| **`σ(γ_1,m) := \min_θ S`** | `0.998456` | `0.998456` | `0.999825` | `0.999613` | `0.999934` | `0.999825` | `0.999901` | `0.999956` |
| `θ^*` | `π/2` | `π/2` | `0.523599` | `0.784151` | `0.314159` | `0.523599` | `0.392699` | `0.258059` |
| `1−σ` | `1.54e−3` | `1.54e−3` | `1.75e−4` | `3.87e−4` | `6.56e−5` | `1.75e−4` | `9.85e−5` | `4.42e−5` |
| `d_0 = (1−σ²)^{-1}` | `324.2` | `324.2` | `2854.5` | `1293.6` | `7622.0` | `2854.5` | `5074.2` | `11313.2` |

*(Grid margin: the script's `s(γ_1,π/2) = 0.998456498` against the corpus's 40-digit
`s_1 = 0.998460157…` (Prop. D.31.5, `scripts/certify_sF.py`) is `3.66×10^{−6}`, the `u`-grid resolution;
the corpus value is authoritative and all conclusions use `≤`.) A second ordinate `γ = 6.0` is tabulated
in the script with the same qualitative pattern and larger margins (`1−σ` from `8.4×10^{−3}` to
`2.4×10^{−4}`).*

**Theorem D.55.7 (`PROVED`).**
 (i) `S(γ,π/2,m) = 1` **exactly when `4 ∣ m`**: take `k` with `2πk/m = π/2`, i.e. `k = m/4`; then
   `s(γ, π/2 − π/2) = s(γ,0) = \sup_u|\cos(γu)|/\cosh(u/2) = 1`, attained at `u = 0`. Conversely if
   `4 ∤ m` then `π/2 − 2πk/m ∉ πZ` for every `k`, and `s(γ,θ') < 1` for `θ' ∉ πZ`, `γ ≠ 0`
   (Proposition D.31.5 `=` Paper 46 Proposition 19.18), so the max of finitely many numbers `< 1` is
   `< 1`.
 (ii) **`σ(γ,m) = \min_θ S(γ,θ,m) < 1` for every finite `m` and every `γ ≠ 0`**, because
   `S(γ,θ,m) = 1` forces `θ ∈ πZ + (2π/m)Z`, a **finite** set modulo `π`; choose `θ` outside it.
 (iii) `σ(γ,m) ≥ L(m)` of Lemma A.6 (the `u = 0` entries alone). **Arithmetically this bound is not
   binding** — `L(4) = 0.7071` against `σ(γ_1,4) = 0.99961` — because `u` ranges over all of `R` and
   `s(γ,θ)` is already within `1.6×10^{−3}` of `1`. **`MISMATCH 12` (new):** in the model the carrier is
   the lattice `(\log q)Z`, `u = 0` is isolated, and `L(m)` **is** the binding entry
   (`s_{\mathrm{Aut,Frob}} = L(4) = 1/\sqrt2` exactly, Prop. A.7b); in the arithmetic the lattice is
   replaced by `R` and the `u = 0` entry is dominated. The model's gain is therefore **not** a guide to
   the arithmetic gain.

*Proof.* As indicated; (iii) is the table. ∎ `PROVED`

**Theorem D.55.9 (where the `+` lives; `PROVED`).** Let `ρ` be a zero of `ξ_K` and `χ_ρ` the unique
character with `ρ ∈ Z(Λ(\cdot,χ_ρ))`. Then:
 (i) if `ρ` is a zero of `ζ` then `χ_ρ = 1`, `m = 1`, and `S(γ,θ,1) = s(γ,θ)` — **the support function
   at every zero of `ζ` is unchanged, for every abelian `K/Q`**;
 (ii) the `G`-invariant sector of `𝓒` is exactly the `χ = 1` component (D.55.5(e)), i.e. exactly the
   spectrum of `ζ`; `Z[G]` acts nontrivially only on the `χ ≠ 1` components;
 (iii) hence **the Galois `+` is real and lives entirely in the part of the spectrum that `ζ` does not
   occupy.**

*Proof.* (i) `Z(ξ) = Z(Λ(\cdot,1))` and the decomposition is a disjoint union (D.20.2). (ii) is
D.55.5(e). (iii) is (i)+(ii). ∎ `PROVED`

## D.55.6 The `+`, exhibited

**Proposition D.55.8 (`PROVED`).** Let `g ∈ G` and `χ` with `χ(g) = −1` (such a pair exists iff `|G|` is
even). Then the class `δ_{(0,g)} ∈ 𝓒` is **effective** (a point mass on `C_{Q,S}`, an extreme ray) and
its `χ`-coordinate is `−δ_0`: a **negative** coefficient in the basis in which `ι(𝓔)` has only
nonnegative ones. More generally `δ_{(u,g)}` has coordinates `(χ(g))_χ ∈ μ_m^{\widehat G}`, complex of
modulus one. This is the arithmetic analogue of the model's
`[Γ_i] = ½[Γ_π] − ½[Δ] − F_1 + F_2` (round 1 Theorem D.53.4), with `μ_m` in place of
`\mathrm{Aut}(E) = μ_4` and with the same mechanism: **a root of unity multiplying the zero datum.**

*Proof.* D.55.5(a) and `Φ_{(δ_{(u,g)})_χ}(ρ) = χ(g)e^{iγu}`. ∎ `PROVED`

> **So the answer to the phase's question is "yes, and it does not reach `ζ`".** The `+` exists
> (D.55.8), the character table enters the intersection numbers (D.55.4), the cone is genuinely enlarged
> and its support function genuinely rises (D.55.6) — and by D.55.9 none of it touches the zeros of `ζ`,
> while by D.55.7(ii) even on the `χ ≠ 1` sectors the constant stays `< 1` in a free direction.

## D.55.7 Falsifiers and the FATAL rule, on the graded carrier (W-c)

**FATAL-RULE FLAG (raised, examined, cleared).** `S(γ,π/2,m) = 1` **is** reached, for `4 ∣ m`
(D.55.7(i)) — the first time in row D that any support function reaches `1`. Required actions taken:

 1. **Where.** Only at zeros of `L(s,χ)` with `4 ∣ \mathrm{ord}\,χ`, and only in the **fixed** direction
   `θ = π/2`. **Never at a zero of `ζ`** (D.55.9(i)), for any `K`.
 2. **Does a transfer theorem run?** **No.** Paper 46 Theorem 12.3 / D.31.12 consumes a function `h⁰`
   with (a), (b′), (c); lifting the Lemma-19.17 bound removes **one known proof** that (b′)⁺ fails
   (Theorem 19.23's witness) and supplies **no `h⁰`**. Nothing becomes provable.
 3. **Does bigness follow?** **No**, and it must not: by `R145` Proposition D.42.5, for a closed
   `𝓝`-saturated cone with the degree gate, bigness **is** RH. `𝓒` satisfies the gate (D.55.5(d)); its
   bigness clause is therefore exactly GRH for the `L(s,χ)` and is **not asserted**.
 4. **Free direction.** `σ(γ,m) < 1` for every finite `m` (D.55.7(ii)), so Theorem 19.23/D.41.13 — which
   may choose `θ` — **still runs**, with threshold `d_0(m)` growing from `324` (`m = 1`) to `11313`
   (`m = 12`). The obstruction is weakened quantitatively, not removed.
 5. **W-a.** Every statement above is a support function of a convex cone. **No positivity of `I^{(χ)}`,
   of any trace form on `Z[G]`, or of anything else is claimed.** The statement
   "`I^{(χ)} ≤ 0` on the `χ`-effective cone" **is GRH for `L(s,χ)` restated** and is never made.

**`Ξ_a`.** No field, no characters: `\widehat G = \{1\}`, `𝒟 = D^W`, `m ≡ 1`, `𝓒 = 𝓔`, `Γ_σ = \mathrm{id}`
— **everything collapses to round 1**, and the graded construction does not exist. `PROVED`. *(Note the
asymmetry with round 1: there, D.50 was `Ξ_a`-uniform because everything collapsed for `ξ` too; here the
construction genuinely separates `ξ_K` from `Ξ_a` — but by D.55.9 the separation is invisible at the
zeros of `ζ`, so it buys nothing for the target.)*

**`Ξ_Q` (Epstein) — where the Epstein test belongs (B3).** Let `K = Q(\sqrt{−D})`, `h = h(−D)`,
`H` the Hilbert class field, `\mathrm{Gal}(H/K) ≅ \mathrm{Cl}(K)` (round 1 Lemma D.51.2). Apply §D.55 to
the **abelian** extension `H/K` with group `\mathrm{Cl}(K)`: `ζ_H = ∏_{χ∈\widehat{\mathrm{Cl}(K)}}L(s,χ)`
and `𝒟_{H/K} = ⊕_χ D^W`, `K_{H/K} = (K_χ)_χ`. Then, precisely:

> **Theorem D.55.10 (`PROVED`).** Let `t : 𝒟_{H/K} → D^W`, `t((E_χ)_χ) := \tfrac1hΣ_χ E_χ`, be the
> **averaging (trace) map**, and let `Γ_𝔄` denote the action of the class `𝔄 ∈ \mathrm{Cl}(K)`. Then
>
>     K_{Q_𝔄} \;=\; t\big(Γ_{𝔄^{-1}}\,K_{H/K}\big),\qquad\text{in particular}\qquad
>     K_{Q_0} \;=\; t\big(K_{H/K}\big) \;=\; \tfrac1hΣ_χ K_χ ,
>
> i.e. the **principal** Epstein class is the image of the canonical class under the **augmentation
> idempotent followed by the averaging map**, and a general Epstein class is the image of its
> `Γ_{𝔄^{-1}}`-translate. Moreover `t` is **not** an isometry and does **not** map `𝓒` into `𝓔`: the
> zero set of `Φ_{t(E)}` is not the union of the zero sets of the `Φ_{E_χ}` (a **sum** of `L`-functions,
> not a product), which is exactly why `Z_{Q_0}` has zeros in `\mathrm{Re}\,s > 1` while no `L(s,χ)`
> does.
>
> *Proof.* `Γ_{𝔄^{-1}}K_{H/K} = (χ(𝔄^{-1})K_χ)_χ = (\overlineχ(𝔄)K_χ)_χ`, and applying `t` gives
> `\tfrac1hΣ_χ\overlineχ(𝔄)K_χ`, which is `K_{Q_𝔄}` by round 1 Lemma D.51.3 (all class-group characters
> unramified ⟹ one common `Γ`-factor ⟹ `Λ_{Q_𝔄} = \tfrac1hΣ_χ\overlineχ(𝔄)Λ(s,χ)`, and `Ξ` is
> `R`-linear in `Λ`). Non-isometry: `I^{(K)}` on `𝒟` is a **sum over the disjoint union** of zero sets,
> whereas the Weil form attached to `Z_{Q_𝔄}` is a sum over `Z(Z_{Q_𝔄})`, and these multisets differ
> (Davenport–Heilbronn, `R139_004` H4: for `h > 1`, `Z_{Q_𝔄}` has infinitely many zeros in
> `\mathrm{Re}\,s > 1`, and no `L(s,χ)` has any). ∎ `PROVED`

**Verdict on `Ξ_Q`.** The graded construction **exists for `ζ_H` and not for `Z_{Q_𝔄}`**: the Epstein
zeta is the image of a graded class under a projection that destroys the grading, and it is not a class
of `𝒟` at all. So the falsifier is passed **by structure** (the construction does not apply), and — new
— the corpus now has the exact place where Epstein sits relative to the Galois grading: it is the trace,
not a component. This also re-explains round 1's D.51.5 table without numerics: membership of
`K_{Q_𝔄}` in `𝓔` is a property of an **average** of `h` classes, and nothing in the grading controls it.

**`ζ_K` (uniformity).** The construction exists for every abelian `K/Q` and is compatible with towers:
for `Q ⊆ K ⊆ L` abelian, `\widehat{\mathrm{Gal}(K/Q)} ⊆ \widehat{\mathrm{Gal}(L/Q)}` and `𝒟_K ⊆ 𝒟_L` as
a sum of slots, with `Γ` restricting correctly — **Artin formalism at the level of cones, now
non-tautologically** (contrast round 1 D.51.7, where the cone did not depend on `K` at all):
`𝓒_K ⊆ 𝓒_L` via `f ↦ f∘(\text{projection } G_L ↠ G_K)`, and the support function is **monotone
increasing in the tower** because `m` can only grow. But by D.55.9(i) the constant **at the zeros of
`ζ`** is `s(γ,θ)` for every `K` in every tower. Uniform, and uniformly useless for the target.

## D.55.8 Bigness and (4a) on the graded carrier (re-opening D.52)

Round 1's Theorem D.52.2 (`\dim H^0 = 1`) `STANDS on the radial realization` and **must not** be stated
for `𝒟_K` (MAJOR 5). On `𝒟_K` the `G`-action is faithful, so the regular-representation proposal is not
degenerate — and it still fails, for a different and sharper reason:

**Theorem D.55.11 (`PROVED`).** Define `H^0(E) := (Z[G]\cdot E)^G` for `E ∈ 𝒟_K`. Then
`Z[G]\cdot E = ⊕_χ C·E_χ` (each slot is an eigenline), so
`\dim_C Z[G]\cdot E = \#\{χ : E_χ ≠ 0\} ≤ |G|`, and

    \dim_C H^0(E) \;=\; \dim_C (Z[G]E)^G \;=\; \mathbf{1}_{\{E_1 ≠ 0\}} \;≤\; 1 ,

because the `G`-invariants of `⊕_χ C·E_χ` are the `χ = 1` slot. In particular `\dim H^0(mK_K) ≤ 1` for
every `m`: **no `m²` growth, and (4a) fails on the graded carrier too.**

*Proof.* `Γ_σ` acts on `C·E_χ` by the scalar `χ(σ)`; a vector is `G`-invariant iff every slot with
`χ ≠ 1` vanishes. ∎ `PROVED`

> **Diagnosis.** Passing to `𝒟_K` buys a faithful action (dimension `|G|` instead of `1`) but the
> invariants — which is what a sections functor must count — are still one-dimensional, because the
> module is a sum of **eigenlines**, not of copies of the regular representation. To get
> `\dim H^0 ≍ m²` one needs a module whose `G`-decomposition has multiplicities growing with `m`; the
> graded carrier has multiplicity `1` in every character by construction. **This is the same wall as
> (4a) itself, now stated exactly:** the missing object is multiplicity, and neither `Z[G]` nor its
> graded carrier supplies it. `O-47.3` is re-based here and remains `OPEN`.

## D.55.9 Model check (B4)

On `E/F_q` with `G = \mathrm{Aut}(E) = μ_m ⊂ \mathrm{End}(E)`, round 1's dictionary gives
`Φ_{Γ_α}(ρ_1) = α` and `\tfrac12\deg Γ_α = \tfrac12(1+N(α))`, so `Γ_σ` for `σ ∈ μ_m` acts on the zero
datum by **multiplication by a primitive `m`-th root of unity** — the same mechanism as D.55.6.
`\mathrm{NS}(E×E)⊗C` decomposes under `G` with `Γ_σ` acting as the diagonal operator `(σ^j)_j` on the
`\mathrm{End}(E)⊗C`-part, and the support-function gain is `\max_k` over the rotations, exactly
`S(γ,θ,m)` with the carrier `R` replaced by the lattice `(\log q)Z`. Confirmed, with the corrected
constants of Lemma A.6:

| | model (`E/F_5`, `m = 4`) | arithmetic (`γ_1`, `m = 4`) |
|---|---|---|
| carrier of `u` | lattice `(\log 5)Z` | `R` |
| `u = 0` entry | **binding**: `L(4) = 1/\sqrt2` | dominated: `L(4) = 0.7071` vs `σ = 0.99961` |
| constant without `G` | `2/3` | `s_1 = 0.99846` |
| constant with `G` | `1/\sqrt2 = 0.70711` (gain `+0.0404`) | `0.99961` (gain `+1.16×10^{−3}`) |
| `d_0` | `5` (with `\mathrm{End}`), `2` (`\mathrm{Aut}`) | `324 → 1294` |
| reaches `1`? | no, ever (`L(m) < 1`) | only at `θ = π/2` with `4∣m`, never in a free direction |

**`MISMATCH 12`** (D.55.7(iii)) is the content of this table: the model's gain comes from the
**discreteness** of its carrier, which the arithmetic frame does not have. Round 1's §0 bullet 2 and
README are corrected accordingly (NOTE 20).

## D.55.10 Corpus check for B1–B4 (B5)

*Greps run over `03-research` (and `04-papers` for the paper-facing rows): `graded`, `character packet`,
`Λ_{[χ]}`, `packet`, `D.20.2`, `twisted explicit formula`, `Hecke`, `isotypic`, `Artin formalism`,
`regular representation`, `translation of the class group`.*

| # | object | corpus status | source / verdict |
|---|---|---|---|
| B1a | the packet-graded **form** `Σ_{[χ]}χ(1)Ŵ^{(Λ_{[χ]})}` | **TRIED–PROVED**, reused verbatim | phase 139 **Theorem D.20.2**, (D.20.3)/(D.20.4), Lemma D.20.2a₀ (`R139_001:844`+, `R139_003:32`, `R139_005:20`); `PROVED` abelian, `PROVED-CONDITIONAL` otherwise |
| B1b | the packet-graded **carrier** `⊕_{[χ]}D^W` as a space, with `ι` an isometry | **NEW** (the corpus decomposes the form, never the carrier) | Theorem D.55.2 |
| B1c | `Z[G]` acting by `χ(σ)` on the graded carrier; `I(Γ_σE,Γ_τF) = Σχ(στ^{-1})I^{(χ)}` | **NEW** | Theorem D.55.4; `CORPUS_CHECK_R147b` §2 records "no twist of `Frob_n` by any character anywhere" |
| B1d | degrees/rulings confined to the `χ = 1` slot | **NEW** | Theorem D.55.3; consistent with round 1 Lemma D.51.3 (`K_χ` primitive) |
| B2a | the realizable cone `𝓒` = isotypic image of nonnegative **non-radial** tests | **NEW**; its raw material (coset indicators, level structure on `C_S`) is **TRIED–PARTIAL** | Paper 44 §8bis Thm 8bis.1b/1b′ (`main.md:3348-3390`); `CORPUS_CHECK_R147b` §2 |
| B2b | Galois correspondences as **translations** by norm-one ideles | **TRIED–PARTIAL, sign reversed**: `R146_005` §1 records "the arithmetic Frobenius is a **translation** of the class group, **not a homomorphism**" as a *negative*; here the same fact is the mechanism | `R146_005`; new use |
| B2c | the support function `S(γ,θ,m) = \max_k s(γ,θ−2πk/m)` | **NEW** | Theorem D.55.6; built on Lemma 19.17/D.31.4 and Prop. 19.18/D.31.5, both `PROVED` |
| B3a | Epstein `= t(Γ_{𝔄^{-1}}K_{H/K})`, the trace of a graded class | **NEW** | Theorem D.55.10; uses phase 139 D.19.1 (C3) and `R139_004` H4 |
| B4 | `\mathrm{NS}(E×E)⊗C` graded by `\mathrm{Aut}(E)`; graphs as diagonal operators | **NEW** (`CORPUS_CHECK_R147b` §4: no curve-with-automorphisms model anywhere) | D.55.9 |
| — | positivity of `I^{(χ)}` / of a trace form on `Z[G]` | **BARRED** (`R145_004` Warning 1; W-a; = GRH) | **never claimed** |

**What is reused:** the graded form (D.20.2) entire, the cosh lemma and its constant (Lemma 19.17 /
D.31.4, Prop. D.31.5), the degree/effectivity theorem (11.13), Prop. D.42.5 as the RH-equivalence guard,
and round 1 Lemma D.51.3. **What is new:** the graded **carrier** and the `Z[G]`-action on it, the
realizable cone `𝓒`, its support function, and the placement of Epstein as a trace (rows B1b–B4).

## D.55.11 Synthesis (B6)

**Does the graded carrier supply the `+`?** **Yes** — Proposition D.55.8 exhibits effective classes
(point masses `δ_{(u,g)}`) whose coordinates in the character basis are roots of unity, negative for
`χ(g) = −1`: the exact analogue of `[Γ_i]` in the model. The character table enters the intersection
numbers (Theorem D.55.4), the blueprint's formula is confirmed, the cone `𝓒` is `Z[G]`-stable, satisfies
the degree gate, and contains `ι(𝓔)` strictly.

**And it does not help, by a theorem.** Three independent reasons, in increasing order of force:

 1. **Quantitative.** `σ(γ,m) < 1` for every finite `m` (D.55.7(ii)), so Theorem 19.23 / D.41.13 still
   builds its witness — in a direction `θ` outside the finite bad set `πZ + (2π/m)Z`. The threshold
   `d_0` grows (`324 → 11313` for `m = 1 → 12`) but never becomes infinite.
 2. **Structural.** The gain is concentrated at zeros of `L(s,χ)`, `χ ≠ 1`. **At every zero of `ζ` the
   constant is exactly `s(γ,θ)`, unchanged, for every abelian `K/Q`** (Theorem D.55.9(i)), because the
   `G`-invariant sector of `𝓒` **is** the `χ = 1` sector (D.55.5(e)) — the group ring acts trivially
   precisely where `ζ` lives. This is the same phenomenon as round 1's collapse, seen one level up:
   there the invariance was of the modulus under `σ`, here it is the invariance of the trivial
   character.
 3. **Mechanistic.** (4a) fails again, and now for an exactly stateable reason: `𝒟_K` is a sum of
   **eigenlines**, so `\dim H^0 ≤ 1` (Theorem D.55.11). A sections functor needs **multiplicity**
   growing with the degree, and no group ring — graded or not — supplies it.

**Recommendation: close the Galois-ring thread, on the negative, with the graded carrier recorded as
built and measured.** Phase 147 now has (i) a correct one-lemma no-go for the radial realization
(`R(Γ_σ) = \mathrm{id}`, A.4), (ii) the graded carrier actually constructed, the blueprint's formula
proved on it, its cone and support function computed, and its failure localized to a theorem
(D.55.9, D.55.11), (iii) a function-field control with exact numbers and corrected constants, and (iv)
one confirmed repair to R145. The next genuine move is **multiplicity**, not more correspondences — and
the corpus has no candidate for it. Options for the lead: (a) close row D at the map, as `R146_005` §4
option (ii) proposed, with §D.55 as the final entry; (b) open a phase on multiplicity (`O-47.3′`), which
is (4a) itself and therefore of unknown difficulty.

---

## §6 — Paper-facing (round 1's list, corrected)

* **Paper 46 §11.** *(round 1's bullet 1 is **deleted**: `K ∈ 𝓔` is Theorem 11.7(i).)* Add after
  **Theorem 11.14** a one-line remark: *"Theorem A.2 (phase 147): `𝓔` contains classes of positive
  degree whose `Φ` has infinitely many zeros in `\mathrm{Re}\,s > 2`, e.g. `3φ + τ_{\log2}φ`,
  `φ = e^{−t²}` — pointwise nonnegativity constrains `Φ_E` only on `R` (the moment-cone diagnosis of
  §19.9)."* **No claim about the §12.2 horn.**
* **Paper 46 §14.3 / §19.9.** New subsection candidate: *the radial realization kills correspondence
  rings.* `R(Γ_σ) = \mathrm{id}` (A.4), with the consequence that the Connes–Consani / Borger / `F_1` /
  `K/Q` family of "more endomorphisms" escapes cannot reach `D^W`; and the graded carrier `𝒟_K` of
  §D.55 as the place where they can, together with Theorem D.55.9 saying what that buys at the zeros of
  `ζ` (nothing).
* **Phase 139 / Paper 45.** D.20.2 gains a corollary: the graded **carrier** `⊕_{[χ]}D^W`, on which
  D.20.3 is the pairing and `Z[G]` acts by the character table (D.55.2, D.55.4). Add the Epstein
  placement D.55.10 (`K_{Q_𝔄} = t(Γ_{𝔄^{-1}}K_{H/K})`) next to D.19.1, and cite `R139_004` H4 there.
* **Paper 44 §8bis.** Corrected cross-reference: `R(\mathrm{Frob}_{σ𝔫}) = R(\mathrm{Frob}_𝔫)` because
  `N(σ𝔫) = N𝔫` — a statement about the **realization**, not about `\mathrm{Frob}_{σ𝔫}` itself (A.4(c)).
* **R145 Prop. D.41.12′.** Repair F-147-1 stands (`CONFIRMED`, NOTE 18), in the auditor's sharper form:
  run the finite check over `n ∈ Z`, not `|n| ≥ 2`.
* **No label anywhere in the corpus is changed.**

## §7 — Open list (round 1's, corrected)

| id | statement | status |
|---|---|---|
| **O-47.1′** | *(re-worded per MAJOR 5; the round-1 wording is withdrawn)* Extend `I_∞` from `D^W` to the non-radial sector of `D_A^∞` (Paper 46 Thm 14.3(i), Paper 44 §3bis) so that `𝒟_K` and `𝓒` of §D.55 are realizations of genuine correspondence classes rather than a model. §D.55 builds the model and computes in it; the identification with `\mathrm{Corr}(C_{Q,S})` uses Weil's explicit formula for Hecke characters (Weil 1952; Bombieri, *Remarks on Weil's quadratic functional*) and is **not** built in the corpus | **OPEN** |
| **O-47.2** | *(Davenport–Heilbronn class-uniformity)* | **WITHDRAWN** — closed at `R139_004` H4 |
| **O-47.3′** | **multiplicity**: a carrier whose `G`-decomposition (or whose sections module) has multiplicities growing with the degree, so that `\dim H^0 ≍ m²`. This is (4a) itself, now stated exactly (D.55.11) | **OPEN** — the only live opening |
| **O-47.4** | closed form for `\min_θ s(𝓔_{\mathrm{End}})` on a general CM curve, and whether `\sup < 1` uniformly | **OPEN** |
| **O-47.5** | a closed criterion for `K_Q ∈ 𝓔` (the data suggest the second successive minimum of `Q`); note phase 139 D.19.4a settles the asymptotic direction | **OPEN**, low priority |
| **O-47.6** | *(new)* is `σ(γ,m) \to 1` as `m \to ∞` for fixed `γ`, and at what rate? The table gives `1−σ` from `1.5×10^{−3}` (`m=1`) to `4.4×10^{−5}` (`m=12`). Relevant only to the `χ ≠ 1` sectors | **OPEN**, low priority |
| O-36–O-39, O-46.6 | carried from R145/R146 | unchanged |

---

## §Label — round 2

*(Round 1's labels are superseded where marked; `R147_001` carries the same corrections in its appended
`Corrections of record`.)*

| item | label |
|---|---|
| **A.2** (`E = 3φ + τ_{\log2}φ`, zeros on `\mathrm{Re}\,s = ½+\log3/\log2`) | **`PROVED`** — replaces round 1 D.51.6(ii)'s proof |
| **A.3** (no `𝓒 ⊇ 𝓔` certifies zero location) | **`PROVED`**; the inference to the §12.2 horn is **WITHDRAWN** |
| **D.50.2′** (`R(Γ_σ) = \mathrm{id}`) | **`PROVED`** — round 1's D.50.2, correctly typed |
| **D.50.1** | **`PROVED`**, as a statement about `\mathrm{Corr}(C_{K,S})` |
| **D.50.3(ii)** | **WITHDRAWN as stated**; replaced by `I_∞(R(Γ_σ)E,F) = I_∞(E,F)`, **`PROVED`** |
| **D.50.3, blueprint's formula** | `REFUTED` → **`NOT-APPLICABLE`** (radial realization); **CONFIRMED** on the graded carrier (D.55.4) |
| **D.50.6′** (Hurwitz/different identity) | **`CLASSICAL-RESTATEMENT`**; "Arakelov" withdrawn; ramification sentence corrected (`unless σ ∈ I_𝔓`) |
| **D.50.9(i)** | **DOWNGRADED**; the `s ≤ s(γ,θ)` conclusion **`PROVED`** by the point-mass argument |
| **D.50.9(ii)–(iv), D.50.10** | **`PROVED`** (with `≤`, per MINOR 13) |
| **D.51.1** (`Ξ_a`-uniformity of the radial realization) | **`PROVED`**, reworded per NOTE 21 |
| **D.51.5** (Epstein membership table) | **`CERTIFIED`** (grid + margins), **not** `PROVED`; extends phase 139 D.19.4a |
| **D.51.6(i)** (`K ∈ 𝓔`) | **`RESTATEMENT`** of Paper 46 Thm 11.7(i)/(X12); "NEW" **withdrawn** |
| **D.51.6(ii)** | **`PROVED`** by A.2; O-47.2 dependence deleted |
| **D.51.6(iii)** | **WITHDRAWN** |
| **D.51.7** | **`RESTATEMENT`** of Paper 46 Def. 11.1; clause (iii) **deleted**; (ii) carries D.20.2's conditionality |
| **D.52.2** (`\dim H^0 = 1`) | **`PROVED` on the radial realization only** |
| **A.6** (corrected `L(m)` lemma) | **`PROVED`** + `CERTIFIED` to `1.1×10^{−16}` |
| **A.7a** (`s_{\mathrm{End}} = 2/\sqrt5`), **A.7b** (`s_{\mathrm{Aut,Frob}} = 1/\sqrt2`) | **`PROVED`** (round 1's grid labels upgraded) |
| **D.53.5(i)** (`2/3 → 1/\sqrt2`) | `s_{\mathrm{Frob}} = 2/3`: `≤` **`PROVED`**, `≥` **`CERTIFIED`** (margin `0.0` to the closed form) |
| **D.53.5(ii)** | inequality **`PROVED`** with the corrected `L(m)`; round 1's equality **corrected** |
| **D.53.5(iii)** | **`PROVED` with corrected constants** |
| **D.53.5(v)** | **`PROVED` for `χ ≥ 0`, `d > 5`**; general hypothesis `d²(1−s²) > d−4χ` |
| **D.55.2** (graded carrier; `ι` isometry; `= (D.20.4)`) | **`PROVED`** (abelian, unconditional) |
| **D.55.3** (canonical class, degree `= \deg E_1`, rulings in `χ=1`, `Γ_σ` isometry) | **`PROVED`** |
| **D.55.4** (`I(Γ_σE,Γ_τF) = Σ_χ χ(στ^{-1})I^{(χ)}`) | **`PROVED`** abelian / **`PROVED-CONDITIONAL`** on Artin holomorphy in general |
| **D.55.5** (`𝓒`: cone, extreme rays, translations, `ι(𝓔) ⊂ 𝓒`, degree gate, invariants) | **`PROVED`** |
| **D.55.6** (`S(γ,θ,m) = \max_k s(γ,θ−2πk/m)`) | **`PROVED`**; the numeric table **`CERTIFIED`** (grid margin `3.7×10^{−6}` against the corpus's `s_1`) |
| **D.55.7** (`S(γ,π/2,m) = 1 ⟺ 4∣m`; `σ(γ,m) < 1` always; `MISMATCH 12`) | **`PROVED`** — **FATAL-rule flag raised and cleared in §D.55.7** |
| **D.55.8** (the `+` exhibited) | **`PROVED`** |
| **D.55.9** (the constant at the zeros of `ζ` is unchanged; invariants `=` `χ=1` sector) | **`PROVED`** |
| **D.55.10** (`K_{Q_𝔄} = t(Γ_{𝔄^{-1}}K_{H/K})`; `t` not an isometry) | **`PROVED`** |
| **D.55.11** (`\dim H^0 ≤ 1` on `𝒟_K`; multiplicity is the wall) | **`PROVED`** |
| **F-147-1** | **`CONFIRMED`** (auditor, NOTE 18), in the sharper form |
| corpus rows | round 1 §5 rows **4 WITHDRAWN** ("NOT NEW"), **5 → "extends D.19.4a"**, **6 → `RESTATEMENT`**; new rows B1b–B4 in D.55.10 |

**No label anywhere else in the corpus is changed by round 2.** Row D remains where `R146_005` left it.

---

## Corrections of record (2026-09-14, round 3)

*Entered after `R147_004_HOSTILE_AUDIT_R2.md` (0 FATAL; 7 MAJOR, 9 MINOR, 4 NOTE; verdict **ACCEPT PART
A; PART B REQUIRES MAJOR REPAIRS BEFORE ANY LABEL**). The text above is **not** rewritten. **Part A
above is accepted in full by the auditor** and stands as written, with one label upgrade (D14). **Part B
(§D.55) must be read through the repairs below**, which are carried out in
`R147_003b_BUILDER_ROUND3.md`, the document of record for Part B.*

| # | location above | correction | where repaired |
|---|---|---|---|
| **D1** | **D.55.1(ii)**; D.55.2(i),(ii); D.55.3(i),(ii); D.55.4; §0 table; README | **The grading must be by conjugate PACKETS, not by characters** — exactly the error `R139_001` §D.20.2 was rebuilt in round 2 to repair (its finding H5): for complex `χ`, `1−ρ ∈ Z(Λ(\cdot,\barχ))` and **not** `Z(Λ(\cdot,χ))`, so the per-`χ` form `I^{(χ)}` is neither symmetric nor real and is not one of the forms of (D.20.3). Forced repair: pair the `χ`-slot with the `\barχ`-slot, `I^{(K)}(E,F) := Σ_χ I^{[χ]}(E_χ,F_{\barχ})`. The **total** form still equals (D.20.4); every **slot-wise** claim of round 2 was unlicensed as written | `R147_003b` §R3.1, Def. D.55.1′, Thm D.55.2′ |
| **D2** | **D.55.4** and its proof; **D.55.3(iv)**; §0 display; README | **`χ(στ⁻¹)` does not follow from the stated (bilinear, per-`χ`) form** — bilinearity gives `χ(στ)` — and the proof silently replaced `I(\cdot,Γ_τ\cdot)` by `I(\cdot,Γ_τ^†\cdot)`; the same smuggled adjoint is what made D.55.3(iv)'s isometry come out right. Under the packet pairing the second argument sits in the `\barχ`-slot, so `Γ_τ` contributes `\barχ(τ) = χ(τ^{-1})` **by bilinearity alone, with no adjoint**, and both statements become true | `R147_003b` §R3.1–§R3.2, Thm D.55.3′(iv), Thm D.55.4′ |
| **D3** | **D.55.5(a)**; **D.55.6** and its proof; **Prop. D.55.8**; §0; README | **`δ_u ∉ D^W`** (Paper 46 Def. 11.1 is a space of *functions* on `R`), so `𝓒` was not a subset of the carrier it was declared a subset of, "extreme rays are the point masses" is false of the object as typed, and "it suffices to evaluate on the extreme rays" is not an argument (no compactness). This is verbatim the defect repaired one section earlier for `𝓔_{\mathrm{Frob}}` (§A.4(b)). Repair: take `f ∈ C_c^∞(R×G)`, `f ≥ 0`, and prove `S = \max_ks` **in two halves** — Lemma D.31.4 per coset for `≤`, concentration of `f` on one coset near the optimal `u` for `≥`. `Prop. D.55.8` restated with a bump; the strictness `ι(𝓔) ⊊ 𝓒` now **proved**, not exemplified | `R147_003b` §R3.3, Def. D.55.5′, Thms D.55.5″, D.55.6′, Prop. D.55.8′ |
| **D4** | **D.55.7(i)** framing; the FATAL-RULE FLAG block; §0 table row 2; README | **"the first time in row D that any support function reaches `1`" is WITHDRAWN.** `s(γ,0) = 1` for every `γ`, attained at `u = 0` (Paper 46 Prop. 19.18's proof), and `\max_θ s(γ,θ) = 1` is displayed at Paper 46 **(19.2)**. Correct statement: for `4 ∣ m` the `μ_m`-orbit of `π/2` meets `πZ`, the direction in which the support function was always `1`; **no support function reaches a value it did not already have**, and nothing ever binding is lifted (the direction `θ = 0` was never usable — which is why Thm 19.23 is built at `θ = π/2`). The **arithmetic** `S(γ,π/2,m) = 1 ⟺ 4∣m` stands; the flag stays raised-and-cleared, on the correct ground | `R147_003b` §R3.4, Thm D.55.7′(i) |
| **D5** | §D.55.7 item 4; §0 table row 3; §D.55.11 point 1; README; the `d_0` row; `O-47.6` | **"the defect theorem — which may choose `θ` — still runs" is WITHDRAWN, twice over.** (a) Paper 46 Thm 19.23 runs on the **specific** witness `F_0` of Def. 19.19: real, **odd**, `\deg F_0 = 0` *because the integrand is odd*, `|η| < 10^{−390}`, `L ≤ 5.46×10^{−91}`, `W_{F_0} = 2G²`, `C_{F_0} ≤ G·s_1` — all tied to `θ = π/2`; a `\cos(γ_1u+θ)` witness is not odd and **no such family exists in the corpus**. (b) **There is no defect theorem for `L(s,χ)` at all**: §§19.5–19.7 are built on `ξ`, on (X19) and on `D^W`'s archimedean factor. Replaced by a **`CANDIDATE`** conditional statement; new **O-47.7** | `R147_003b` §R3.5 |
| **D6** | **D.55.10**, "Moreover `t` … does **not** map `𝓒` into `𝓔`"; §D.55.7 "Verdict on `Ξ_Q`" | **FALSE, refuted by round 2's own definitions.** Character orthogonality gives `t((f_χ)_χ) = \tfrac1hΣ_gf(u,g)Σ_χχ(g) = f(u,1) ≥ 0`, so `t(𝓒) ⊆ 𝓔` and `t∘ι = \mathrm{id}` (`t` is evaluation at the identity coset). Only the **non-isometry** half is needed for the Epstein verdict and it stands, as a theorem (the zero multiset of `Z_{Q_𝔄}` is not `⊔_χZ(Λ(\cdot,χ))`); `K_{Q_𝔄} ∉ 𝓔` is consistent because **`K_H ∉ 𝓒`** | `R147_003b` §R3.6, Thm D.55.10′ |
| **D7** | **D.55.11**, its Diagnosis blockquote, §D.55.11 point 3, `O-47.3′`, README | **WITHDRAWN as a load-bearing negative.** (a) *Vacuous in `m`*: `Z[G]\cdot(mK_K) = Z[G]\cdot K_K` for every `m ≠ 0`, so the parameter (4a) is about is not modelled, and `(Z[G]E)^G` is **not** (4a)'s sections functor. (b) *Abelian-only*: `Z[G]E = ⊕_χC·E_χ` uses `\dimχ = 1`. **"Multiplicity is the missing object" is withdrawn as a slogan.** Downgraded to Remark D.55.11′; `O-47.3′` re-worded as a mathematical question ((4a) on `𝒟_L`). **The phase's negative does not depend on it** — D.55.9 carries it alone | `R147_003b` §R3.7 |
| **d8** | §D.55.10's use of "§D.55" for `H/K` | Standing hypothesis silently changed: base `K` (not `Q`), **Hecke/class-group** characters, `χ = 1` slot `ξ_K` (not `ξ`). §D.55 is restated for a general abelian `L/F`; the Γ-factor claim is correct (all class-group characters unramified, `K` imaginary quadratic with one complex place) and the unit factor `w = \#O_K^×` is the one absorbed in round 1 Lemma D.51.3, now **cited** rather than silently re-derived | `R147_003b` §R3.1 (standing hypothesis), §R3.6 |
| **d9** | D.55.3, `K_K := (K_χ)_χ` | `K_χ ∈ D^W` was **asserted**. Proved: for base `K` imaginary quadratic, `K_χ = Σ_𝔄χ(𝔄)K_{Q_𝔄}` and each `K_{Q_𝔄} ∈ D^W(α)` for every `α > 0` by phase 139 **Thm D.19.2(iii)**; for base `Q`, from the theta series `θ_χ(u) = Σ_nχ(n)n^δe^{−πn²u/q}` and its transformation, giving `K_χ(t) = O(e^{Ct}e^{−ce^{2|t|}})` | `R147_003b` §R3.1, Thm D.55.3′(v) |
| **d10** | §Label, `s_{\mathrm{Frob}} = 2/3` | "`CERTIFIED`, margin exactly `0.0`" certified the wrong direction (a grid minimum bounds the true minimum from **above**, which is the half already proved). Now **PROVED** in both directions: if all three binding entries were `< 2/3` then `|\cosθ| + 2|\sinθ| < 2` with `|\cosθ| ≤ 2/3`, impossible since `g(c) = |c|+2\sqrt{1−c²} ≥ 2` there with equality only at `c = 0` | `R147_003b` §R3.8, Prop. A.7c |
| **d11** | the `σ`/`d_0` table; §0 | A grid **under**estimates a supremum, so every `σ(γ,m)` and every `d_0(m)` printed is a **LOWER BOUND**. The `m = 1` cell must carry the corpus's certified `s_1 = 0.99846016271880910923…`, `d_0 = (1−s_1²)^{-1} = 324.9598266…` (Paper 46 Thm 19.23), not the grid's `324.1889`; at `m = 12` the grid margin `3.66×10^{−6}` is `8\%` of `1−σ`, so `d_0 ≳ 11313` carries `≈ +9\%`, not four decimals | `R147_003b` §R3.5 |
| **d12** | §D.55.7, "`ζ_K` (uniformity)" | "monotone increasing in the tower because `m` can only grow" is **wrong twice**: `σ(γ_1,3) = 0.999825 > σ(γ_1,4) = 0.999613`, so `σ` is monotone in the **divisibility** order (`m ∣ m' ⟹ σ(γ,m) ≤ σ(γ,m')`), not in `m`; and `m = \mathrm{ord}χ_ρ` is attached to the **zero**, a character inflating with the same order, so **at a fixed zero the constant is unchanged in the tower** — what grows is the set of zeros | `R147_003b` §R3.5 |
| **d13** | D.55.6 table `θ^*` column; `scripts/graded_support.py` docstring | The **exact** argmin is `θ^* = d/2` (`d = 2π/m` for `m` even, `π/m` odd); the printed `0.784151` (`m = 4`) and `0.258059` (`m = 12`) are one and three grid steps off a **flat** minimum. Docstring corrected (`χ(g)` not `\overline{χ(g)}`; `C_{F,S}` not `C_{K,S}`; packet pairing; no point masses) | done in the script; `R147_003b` §R3.5 |
| **d14** | D.55.5(b); corpus row **B2b** | The quotation *"the arithmetic Frobenius is a translation of the class group, not a homomorphism"* is **not in `R146_005`** — it is the **lead's**, `R147_000:7`. Attribution corrected. Also the two translation families must be distinguished: phase 146's (`R146_001` D.45.8, itself downgraded to `CLAIM`) act by `x ↦ ℓx` and **shift** `u`; the round's `Γ_g` are **norm-one** and **fix** `u`. That distinction is the round's own point and the reason for D.55.9 | `R147_003b` §R3.9 |
| **d15** | D.55.5(ii), "by class field theory `C_{Q,S} ↠ G`" | Asserted, not derived. `\mathrm{Art} : C_F ↠ G` is correct and norm-one representatives exist (`\widehat Z^× ↠ G` by **Kronecker–Weber**, uncited), but for a **finite** `S` the truncated group surjects onto `G` only if `S` generates `G`; and `(u,g)` is a **projection**, so `𝓒` is a sub-cone of a projected **model** and D.55.6 is an equality for the model, at most `≤` for a realizable cone. Carries **O-47.1′**'s qualifier explicitly | `R147_003b` §R3.3 (standing qualifier) |
| **d16** | §D.55.7 item 3 | "`𝓒` satisfies the gate; its bigness clause is therefore exactly GRH" — Prop. D.42.5 is proved for a **closed**, `𝓝_∞`-saturated cone in `D^W` with `I_∞` for `ξ`, and `𝓒` is not closed as defined. Correct wording: *"would be GRH, by the analogue of D.42.5, which is not built."* (Conservative direction; W-a unaffected) | `R147_003b` §R3.5 |
| **d17** | D.55.7(iii) / `MISMATCH 12`; the D.55.9 table row "`u = 0` entry: dominated" | Reworded: `u = 0` is **not** a weak contributor — it is exactly where `s(γ,0) = 1` is attained and exactly what makes `S(γ,π/2,4) = 1`. `L(m)` is a weak lower bound for `σ` because `σ` is driven by the **full `u`-supremum** at each rotated direction. The model's gain does come from the discreteness of `(\log q)Z` (where `u = 0` is isolated and binding); the two sentences are now consistent | `R147_003b` §R3.4 |
| **d18** | corpus rows B1b, B1c, B1d ("NEW") | `NEW` **only after the packet repair** — B1a's own source already grades by packets, so round 2's per-character carrier was not a new object but the one phase 139 discarded | `R147_003b` §R3.9 |
| **d19** | §D.55.11 "Recommendation"; README | Closing is justified by **D.55.9 alone**, not by D.55.11 (withdrawn), not by the `d_0` table (thresholds of a theorem not stated for `L(s,χ)`), not by any `S = 1` claim. **Two things must not be read as closed:** the **non-abelian** case (`O-47.8`) and the **`χ ≠ 1` sectors** — a `ζ_F`-frame theorem consumes *all* zeros of `ξ_L = ∏_χΛ(s,χ)`, so the enlarged constants at `L`-zeros **would** matter to it (`O-47.7`) | `R147_003b` §R3.10 |
| **d20** | Part A of this document | **No correction.** The auditor checked all six MAJORs and eleven MINORs of `R147_002` line by line and found Part A complete; A.6 is recorded as correcting the **previous auditor**'s own argmin error; A.7a and A.7b are re-derived and the upgrades to `PROVED` are "earned". Only `s_{\mathrm{Frob}}`'s `≥` half moves — from `CERTIFIED` to `PROVED` (d10) | `R147_003b` §R3.8 |

**Net effect on Part B.** After the one forced change (packets + `C_c^∞`), D.55.2–D.55.6, D.55.8 and
D.55.9 **stand and are `PROVED`**, as the auditor predicted. Four claims are **withdrawn**: the "first to
reach `1`" framing, the `θ`-freedom clearing argument, "`t` does not map `𝓒` into `𝓔`", and
`\dim H^0 ≤ 1` as a negative about (4a). **Theorem D.55.9 is the phase's result and the sole basis for
closing the thread.** No label anywhere else in the corpus is changed.
