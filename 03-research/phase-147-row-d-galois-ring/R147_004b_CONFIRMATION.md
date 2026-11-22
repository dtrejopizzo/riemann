# R147.004b — Confirmation of `R147_003b_ROUND3.md` (phase 147, row D)

`Corrections of record` **D1–D20** appended to `R147_003_ROUND2.md`, `README.md` (rewritten), and
my own `R147_004_AUDIT_R2.md`. `scripts/graded_support.py` **re-run with `--fast`**, full output
compared line by line against the round-3 tables; docstring re-read after the claimed fix.
Re-checked in the corpus: `R139_001` §D.20.2 (H1–H3 as used), `R147_001` D.51.3 and its
`\deg K_{Q_𝔄} = ½`, Paper 47 (19.2)/Prop. 19.18/Def. 19.19/Thm 19.23, Paper 47 Thm 11.8(v).*

**Method.** Every repair was re-derived from scratch rather than read: symmetry and reality of the packet
form were recomputed from (H2)/(H3) by substitution; `χ(στ^{-1})` was recomputed from bilinearity alone;
`D.55.3′(i)` was checked against `Ξ_{\barχ}(1−ρ)`; both halves of `D.55.6′` were re-proved; `A.7c` was
re-derived including the endpoint analysis of `g(x) = x+2\sqrt{1−x²}`; the `θ^*` column was checked cell
by cell against the script's new exact column; the degree normalisation was cross-checked against round
1's `\deg K_{Q_𝔄} = ½`.

---

## Status of my 7 MAJOR / 9 MINOR / 4 NOTE

| finding | correction of record | verdict |
|---|---|---|
| **MAJOR 1** (per-`χ` grading = phase 139's discarded object) | D1 | **DISCHARGED** — see (i) below; re-derived, correct |
| **MAJOR 2** (`χ(στ)` vs `χ(στ^{-1})`; smuggled adjoint) | D2 | **DISCHARGED** — the adjoint is gone, not hidden; it is now a corollary |
| **MAJOR 3** (`δ_u ∉ D^W`; extremality not a proof) | D3 | **DISCHARGED** — two-halves proof verified; one scope slip, MINOR C4 |
| **MAJOR 4** (`S = 1` framing) | D4 | **DISCHARGED** — withdrawn in text, README and the script's verdict block |
| **MAJOR 5** (`θ`-freedom; no `L`-analogue of Thm 19.23) | D5 | **DISCHARGED in the documents**; **NOT in the script docstring** (MINOR C6) |
| **MAJOR 6** (`t(𝓒) ⊆ 𝓔`) | D6 | **DISCHARGED** — the false clause deleted, orthogonality computation correct; `K_H ∉ 𝓒` still unproved (MINOR C5) |
| **MAJOR 7** (`\dim H^0` vacuous/abelian-only) | D7 | **DISCHARGED** — downgraded to Remark D.55.11′, `O-47.3′` re-worded as a question |
| **MINOR 8** (base change of hypothesis) | d8 | **DISCHARGED** — §R3.1 now runs over a general abelian `L/F`; **but** the degree normalisation broke (MAJOR C2) |
| **MINOR 9** (`K_χ ∈ D^W`) | d9 | **DISCHARGED** — D.55.3′(v); the `F = K` half is clean (finite combination of `K_{Q_𝔄}`, phase 139 D.19.2(iii)); the `F = Q` half is a sketch, acceptable with its citations |
| **MINOR 10** (`s_{\mathrm{Frob}}` `≥`) | d10 | **DISCHARGED** — A.7c re-derived, complete (see (v)) |
| **MINOR 11** (`d_0` lower bounds; certified `m=1` cell) | d11 | **DISCHARGED** — table and script both corrected; one sign-of-error slip (MINOR C7) |
| **MINOR 12** (monotonicity in the tower) | d12 | **DISCHARGED** — divisibility order, constant at a fixed zero; `m ∣ m' ⟹ \{2πk/m\} ⊆ \{2πk'/m'\}` is correct |
| **MINOR 13** (`θ^*` exact `= d/2`; docstring) | d13 | **PARTLY** — the script gained an exact column ✓, but one table cell is wrong (MINOR C3) and the docstring fix is incomplete (MINOR C6) |
| **MINOR 14** (mis-attributed quotation) | d14 | **DISCHARGED** — attribution moved to `R147_000:7`, and the two translation families are tabulated; the distinction is correct and is the right one |
| **MINOR 15** (`C_{Q,S} ↠ G`; projection) | d15 | **DISCHARGED** — standing qualifier states both defects and routes them to O-47.1′ |
| **MINOR 16** (Prop. D.42.5 transfer) | d16 | **DISCHARGED** — "would be GRH, by an analogue that is not built" |
| **NOTE 17** (`u = 0` / `MISMATCH 12`) | d17 | **DISCHARGED** — the two sentences are now reconciled, in my words, correctly |
| NOTES 1–4 (Part A) | d20 | **CONFIRMED** — Part A unchanged except the `s_{\mathrm{Frob}}` upgrade |

**D1–D20 cover my findings exactly, with no silent omission and no claim withdrawn in one place and kept
in another** (see (vii)).

---

## (i) The packet-graded form — re-derived, and it holds

I did not read the proofs; I recomputed them.

* **Bilinear.** `I^{[χ]}` is a zero sum of products `Φ_A(ρ)Φ_B(1−ρ)`: bilinear by inspection, and the
  assembly `Σ_χI^{[χ]}(E_χ,F_{\barχ})` is bilinear in `(E,F)`. ✓
* **Symmetric.** Re-indexing `χ ↦ \barχ` and substituting `ρ = 1−ρ'` with `ρ' ∈ Z(Λ(\cdot,χ))`:
  `I^{[\barχ]}(F_{\barχ},E_χ) = −Σ_{ρ'}Φ_{F_{\barχ}}(1−ρ')Φ_{E_χ}(ρ') = I^{[χ]}(E_χ,F_{\barχ})`. The
  substitution is a multiplicity-preserving bijection `Z(Λ(\cdot,\barχ)) → Z(Λ(\cdot,χ))` **by (H2)**,
  which is exactly the property the per-`χ` form lacked. ✓ The `χ = 1` term is symmetric by (11.6). ✓
* **Real on `\overline{E_χ} = E_{\barχ}`.** `\overline{Φ_A(ρ)} = Φ_{\bar A}(\barρ)`, and by (H3)
  `ρ ∈ Z(Λ(\cdot,χ)) ⟺ \barρ ∈ Z(Λ(\cdot,\barχ))`, so
  `\overline{I^{[χ]}(E_χ,F_{\barχ})} = I^{[\barχ]}(E_{\barχ},F_χ)`; summing and re-indexing gives
  `\overline{I^{(K)}} = I^{(K)}`. ✓ **I verified that both (H2) and (H3) are genuinely needed and are
  used in the right places** — (H2) for symmetry, (H3) for reality. Round 2 had neither available.
* **`χ(στ^{-1})` with no adjoint.** `(Γ_σE)_χ = χ(σ)E_χ`, `(Γ_τF)_{\barχ} = \barχ(τ)F_{\barχ}`, and
  bilinearity pulls out `χ(σ)\barχ(τ) = χ(στ^{-1})`. ✓ **This is the honest fix**: the scalar
  `\barχ(τ)` arrives because the second argument is drawn from the conjugate slot, not because an
  adjoint was applied. The blockquote "*Where the adjoint enters — it does not*" is accurate, and the
  adjoint identity is correctly demoted to a corollary. The isometry `χ(σ)\barχ(σ) = |χ(σ)|² = 1` is now
  legitimate.
* **D.55.3′(i).** `I^{[χ]}(E_χ,K_{\barχ}) = −Σ_{ρ∈Z(Λ(·,χ))}Φ_{E_χ}(ρ)Ξ_{\barχ}(1−ρ)` and
  `Ξ_{\barχ}(1−ρ) = ½(1−ρ)(−ρ)Λ(1−ρ,\barχ) = 0` since `1−ρ ∈ Z(Λ(\cdot,\barχ))` by (H2). ✓ **The
  statement round 2 proved by a false reason is now proved by the true one**, and the round says so in
  its own text.
* **Total form `= (D.20.4)`.** `⊔_χZ(Λ(\cdot,χ)) = Z(ξ_L)` with multiplicity (H1 + D.20.2), polar block
  in the `χ = 1` slot only; the round is explicit that **only** the total identification is claimed. ✓

**Verdict on (i): MAJOR 1 and MAJOR 2 are discharged by one change, exactly as predicted. D.55.2′,
D.55.3′(i),(iii),(iv), D.55.4′ are `PROVED`.**

## (ii) The support function, and strictness

* **(`≤`)** `\mathrm{Re}(e^{iθ}Φ_{f_{χ_0}}(ρ)) = Σ_g∫f(u,g)\cos(γu+θ+\argχ_0(g))du`; each
  `f(\cdot,g) ≥ 0` lies in `D^W` (`C_c^∞` trivially satisfies Def. 11.1), so Lemma D.31.4 applies **per
  coset**, and `\argχ_0(g)` runs over all of `\{2πk/m\}` because `χ_0(G) = μ_m`. Summing gives
  `≤ ½(\max_k s)Σ_g\deg f(\cdot,g) = ½(\max_k s)\deg E'`. ✓ **No extremality, no compactness, no point
  masses.**
* **(`≥`)** With `f = φ_δ⊗1_{g^*}`, `∫φ_δ = 1`: numerator `→ |\cos(γu^*+θ_{g^*})|` and
  `½\deg E' = ∫φ_δ\cosh(u/2) → \cosh(u^*/2)`; the sup over `u` is attained (Prop. 19.18), so the limit is
  `s(γ,θ_{g^*})` exactly. ✓
* `\{2πk/m\} = \{−2πk/m\}` via `k ↦ m−k` ✓, so the two displayed forms agree.
* **Strictness.** `𝓒 ∌ ι` of anything non-constant across slots; the witness `f = φ⊗1_g` gives
  `(χ(g)φ)_χ`, which is not constant in `χ` whenever `χ(g) ≠ 1`, and `\widehat G` separates points ✓.
  Strictness is an existential statement, so exhibiting this class **is** a proof, and it is now derived
  rather than asserted. ✓ (Wording slip: MINOR C4.)

**Verdict on (ii): MAJOR 3 discharged. D.55.6′ and D.55.8′ are `PROVED`.**

## (iii) MAJOR 6 / Epstein

`t((f_χ)_χ) = \tfrac1hΣ_gf(u,g)Σ_χχ(g) = f(u,1) ≥ 0` — I recomputed the orthogonality; correct, and
`t∘ι = \mathrm{id}` follows since `ι(E)` is the image of `E⊗δ_{g=1}`. The false clause is deleted, the
non-isometry half is kept, and it is correctly identified as the only half the Epstein verdict needs.
**But `K_H ∉ 𝓒` is asserted, not proved** — see MINOR C5, where I give the two available proofs and note
that the non-trivial one rests on a `CERTIFIED` table.

## (iv) Theorem D.55.9′ — read critically

This is the theorem the closing rests on, and it is the weakest-presented object in the round.

**It has no numbered statement and no proof in the document of record.** `R147_003b` states it in the §0
blockquote, restates it in §R3.10's blockquote, and lists it in the label table as "**PROVED** — the
phase's result, and the sole basis for closing" — but §§R3.1–R3.9 never state it as a theorem and never
prove it. Its only proof in the corpus is round 2's D.55.9, whose proof cites D.55.5(e) and a
**superseded** definition (D.55.1, withdrawn by D1). *A phase may not close on a theorem whose proof
lives only in the withdrawn version of its own construction.* That is MAJOR C1, and it is repairable in
three lines — because the mathematics is right:

* **The content is true, and simpler than advertised.** For `E' = (f_χ)_χ ∈ 𝓒`, the `χ = 1` slot is
  `f_1 = Σ_{g}f(u,g) ≥ 0`, and every nonnegative `C_c^∞` test arises this way. **The `χ = 1` slot of `𝓒`
  is exactly `𝓔^∞`** — no more and no less. Hence
  `\sup_{E'∈𝓒}|\mathrm{Re}(e^{iθ}Φ_{E'_1}(ρ))|/(\tfrac12\deg E') = S(γ,θ,1) = s(γ,θ)`, since
  `\mathrm{ord}(1) = 1` and every rotation in D.55.6′ is trivial. That is the whole proof.
* **The stated reason is a non sequitur.** §0 and §R3.10 argue: "the `G`-invariant sector is exactly the
  `χ = 1` slot. **Hence** the support function at every zero of `ζ_F` is unchanged." It does not follow.
  D.55.5″(e) is a statement about `G`-**invariant elements** of `𝓒`; the support function at a zero of
  `ζ_F` is a statement about the `χ = 1` **component of every element** of `𝓒`, invariant or not. Both
  are true; only the second is what closes the phase, and it is proved by `f_1 = Σ_gf ≥ 0`, not by
  Fourier inversion on `G`. **Repair:** state the theorem in the `f_1` form; keep (e) as a separate,
  compatible remark.
* **"the unique character `χ_ρ` with `ρ ∈ Z(Λ(\cdot,χ_ρ))`" (round 2's wording) is not well defined.**
  `Z(ξ_L) = ⊔_χZ(Λ(\cdot,χ))` is a **multiset** union; nothing known excludes a zero of `ζ_F` from also
  being a zero of some `Λ(\cdot,χ)`, `χ ≠ 1` (that is an open problem, not a lemma). So "if `ρ` is a zero
  of `ζ_F` then `m = 1`" is not a licensed deduction about `ρ`. **The conclusion survives**, because
  D.55.6′ is correctly typed on the **pair** `(ρ,χ_0)` — the `ζ_F`-relevant datum is `Φ_{E'_1}(ρ)`,
  whose support function is `S(γ,θ,1) = s(γ,θ)` regardless of what other slots that complex number
  inhabits. **Repair:** say "at the `χ = 1` slot", never "at a zero of `ζ_F`, `m = 1`".
* **What is genuinely strong about it.** The mechanism is the right one and is not circular: norm-one
  ideles fix `u = \log|x|`, so they commute with the radial projection and act only on the coset; the
  `χ = 1` slot *is* the coset-average, i.e. the trace `t`; so the enlargement is invisible exactly where
  `ζ_F` lives. It is the round-1 lemma one level up, and the identification of `f_1` with `h·t` makes
  that literal. **I could not break it**, and I tried: the only routes are the multiset overlap (handled
  above), the `𝓔` vs `𝓔^∞` gap (MINOR C4 — harmless, `s(𝓔) = s(𝓔^∞)` by density), and the possibility
  that a genuinely realizable cone is larger than the projected model `𝓒` (O-47.1′, honestly open — and
  note this cuts **against** the closing, not for it: a larger realizable cone could have a larger
  `χ = 1` slot).

## (v) Proposition A.7c

Re-derived independently. `\cosh(\tfrac12\log5) = 3/\sqrt5`, `\cosh(\log5) = 13/5`; the `n = ±1` entries
are `\tfrac{\sqrt5}3|\cos(θ±θ_u)| = \tfrac13|c∓2s|` using `\cosθ_u = 1/\sqrt5`, `\sinθ_u = 2/\sqrt5` ✓;
`|n| ≥ 2` gives `≤ 5/13 < 2/3` ✓. **(`≤`)** at `θ = π/2` both `n = ±1` entries equal `2/3` and the
`n = 0` entry vanishes ✓. **(`≥`)** if all three bind below `2/3` then `|c| < 2/3` and
`\max(|c−2s|,|c+2s|) = |c|+2|s| < 2`; on `[0,2/3]`, `g(x) = x+2\sqrt{1−x²}` has
`g'(x) = 1−2x/\sqrt{1−x²} > 0` for `x < 1/\sqrt5 = 0.4472` and `< 0` after, so `g` is unimodal there and
`\min_{[0,2/3]}g = \min(g(0),g(2/3)) = \min(2,\,2.1573) = 2`, with equality only at `x = 0` —
contradiction with the strict `< 2` ✓. Using only `n ∈ \{0,±1\}` is legitimate for the `≥` half. **The
proof is complete; `PROVED` in both directions is earned, and the round correctly records that the
`CERTIFIED` label had bounded the wrong direction.**

## (vi) The `d_0` table and the lower-bound flags

Re-ran `graded_support.py --fast`. Every number in §R3.5's table reproduces: `S(γ_1,π/2,m)` =
`0.998456498, 0.998456498, 0.999824825, 1.000000000, 0.999934398, 0.999824825, 1.000000000,
1.000000000`; `σ ≥ 0.999613420 (m=4)`, `0.999955803 (m=12)`; `1−σ = 3.866e−4`, `4.420e−5`; `γ = 6.0`
row unchanged. The script now prints "`sigma is a LOWER bound (grid underestimates a sup); so is d_0.
Exact argmin = d/2`", carries an **exact `d/2` column**, and its verdict block has been rewritten to the
round-3 framing (including "they belong to a theorem that has NOT been stated for `L(s,χ)` and whose
witness `F_0` is odd and tied to `θ = π/2`. See O-47.7"). The `m = 1` cell of the document's table now
carries the corpus's certified `s_1 = 0.99846016271880910923…` and `d_0 = 324.9598266…` ✓. **MINOR 11 and
the `d_0` half of MINOR 13 are discharged**, subject to C3 and C7.

## (vii) Withdrawn phrases

`grep` over `R147_003b`, `README.md` and `scripts/` for `may choose theta`, `still runs`, `first support
function`, `first time in row D`, `does not map`, `extreme ray`, `point mass`, `multiplicity is the
missing`: in the **documents**, every hit is inside the sentence that withdraws it (`R147_003b:38–41`,
`:247`, `:278`, `:505`, `:510`, `:511`; `README:81`) or inside an assertion that the object is *absent*
(`:180`, `:204`). ✓ **One exception, in the script** — MINOR C6.

## (viii) Label table

Checked row by row against the text. **All round-3 labels are supported** with these exceptions:
`D.55.9′`'s "`PROVED`" has no proof in the document of record (MAJOR C1); `D.55.3′`'s "`PROVED`" carries
the degree-normalisation error (MAJOR C2); `D.55.5″`'s "`PROVED`" should read `ι(𝓔^∞) ⊊ 𝓒`, not
`ι(𝓔) ⊊ 𝓒` (MINOR C4). The `CANDIDATE` for the conditional defect-theorem statement, the
`CERTIFIED`-as-lower-bounds for the table, and the demotion of D.55.11′ to a remark are all correct and
conservative. The claim "no label anywhere else in the corpus is changed" I re-verified: phase 139's
D.20.2 labels are untouched and are now **used as they were repaired**, which is the point of D1.

---

## Remaining defects

### MAJOR C1 — the closing theorem is not stated or proved in the document of record
**Location:** §0 blockquote; §R3.10 blockquote; §Label row `D.55.9′`; README.
**Defect.** No `Theorem D.55.9′` appears in §§R3.1–R3.9; the only proof is round 2's D.55.9, which cites
the withdrawn D.55.1/D.55.5(e). Additionally the stated reason is a non sequitur (invariant *sector* vs
`χ = 1` *component*), and round 2's "unique `χ_ρ`" is not well defined (a zero of `ζ_F` may also lie in
`Z(Λ(\cdot,χ))`; nothing excludes it).
**Repair.** Insert, as a numbered theorem in §R3:
> **Theorem D.55.9′ (`PROVED`).** For `E' = (f_χ)_χ ∈ 𝓒`, `f_1 = Σ_{g∈G}f(\cdot,g) ≥ 0`, and every
> `0 ≤ φ ∈ C_c^∞(R)` arises as some `f_1`. Hence the `χ = 1` slot of `𝓒` is exactly `𝓔^∞`, and for every
> `ρ = ½+iγ ∈ Z(ξ_F)` and every `θ`,
> `\sup_{E'∈𝓒}|\mathrm{Re}(e^{iθ}Φ_{E'_1}(ρ))|/(\tfrac12\deg E') = S(γ,θ,1) = s(γ,θ)` — unchanged, for
> every abelian `L/F`, every tower and every `m`. Equivalently: `f_1 = h·t(E')` and norm-one translations
> fix `u`, so the coset-average cannot see them. *(D.55.5″(e) — the `G`-invariant sector is the `χ = 1`
> slot — is a compatible but distinct statement and is not what is used here.)*
**This is the only defect that touches the recommendation.**

### MAJOR C2 — `\deg K_L = 1` "valid over any base `F`" contradicts round 1's `\deg K_{Q_𝔄} = ½`
**Location:** **D.55.3′(ii)**; the parenthetical "(H4 with H5(c), valid over any base `F`)".
**Defect.** Paper 47 Thm 11.8(v) (`\deg K = 1`) is a statement about `ξ`. Take `F = K = Q(\sqrt{−3})`,
`h = 1`: then `H = K`, `G = 1`, `\widehat G = \{1\}`, `𝒟_H = D^W`, `t = \mathrm{id}`, and D.55.10′(i)
gives `K_{Q_0} = K_1 = K_{ξ_K}`. Round 1 **D.51.3 (`PROVED`)** gives `\deg K_{Q_𝔄} = ½` for every `𝔄`
(`R147_001:291`, `:713`, matching phase 139 D.19.2(vi)). So `\deg K_{ξ_K} = ½ ≠ 1`, and the
generalisation of (H4) to an arbitrary base is false as printed.
**Repair.** Write `\deg_F E := I^{[1]}(E_1,2K_{ξ_F})` and record that the normalising constant
`\deg K_{ξ_F}` is **base-dependent** (`1` for `F = Q`; `½` for `F` imaginary quadratic in round 1's
convention). **Nothing downstream breaks:** D.55.5″(d) computes the gate directly as
`∫(Σ_gf)·2\cosh(u/2)du > 0`, so only the **sign** is used, and every support-function ratio is
homogeneous of degree `0` in the normalisation — but the constant `1` must not be asserted, and the
`\deg K_L = \deg K_1 = 1` clause must be restricted to `F = Q`.

### MINOR C3 — one cell of the `θ^*` row is wrong, and contradicts the script
§R3.5's table gives `θ^* = π/12` at **`m = 6`**. The rule is `θ^* = d/2` with `d = 2π/m` for `m` even, so
`θ^*(6) = π/6`; the script's new exact column prints `0.523599 = π/6` ✓ (and `π/12` correctly at
`m = 12`). Typo, but it is in the corrected table. Fix to `π/6`.

### MINOR C4 — the cone contains `ι(𝓔^∞)`, not `ι(𝓔)`; the strictness sentence names the wrong element
Taking tests in `C_c^∞(R×G)` (the MAJOR 3 repair) means `𝓒 ⊉ ι(𝓔)`: Gaussians are not compactly
supported, and the round's own Theorem A.2 witness `3φ+τ_{\log2}φ` is **not** in `𝓔^∞`. D.55.5″(c) says
`ι(𝓔^∞) ⊂ 𝓒` correctly, but the label row and §0 still say `ι(𝓔) ⊊ 𝓒`. Harmless for every number in the
round (`s(𝓔) = s(𝓔^∞)` by density, and support functions are what is computed), but the statement
"the cone is genuinely enlarged" should be made against `ι(𝓔^∞)` or the closure taken. Also (c)'s
strictness sentence says "then `(χ(g)f_χ)_χ` is not constant in `χ`" without naming `f = φ⊗1_g`; as
written `f_χ` is a generic slot and the sentence does not parse. Name the witness (it is D.55.8′'s).

### MINOR C5 — `K_H ∉ 𝓒` is asserted without proof
**Location:** §R3.6, the WITHDRAWN blockquote ("`K_{Q_𝔄} ∉ 𝓔` … is consistent because **`K_H ∉ 𝓒`**").
Two proofs exist and neither is given. (a) *Trivial:* `𝓒` is defined with `f ∈ C_c^∞`, and `K_χ` is not
compactly supported — but this is an artefact of the typing and would evaporate on any completion.
(b) *Substantive:* `t` is continuous and `t(𝓒) ⊆ 𝓔`, with `𝓔` closed under pointwise limits, so
`K_{Q_0} = t(K_H) ∉ 𝓔` forces `K_H ∉ \overline{𝓒}` — for exactly those discriminants where round 1's
table shows `K_{Q_0} ∉ 𝓔`, i.e. resting on a **`CERTIFIED`** table (and, asymptotically, on phase 139
D.19.4a, which is `PROVED`). Give (b), and say which discriminants it covers.

### MINOR C6 — the script docstring still carries two withdrawn claims
`scripts/graded_support.py` is the file of record for the numbers. d13 states the docstring was corrected
for "packet pairing"; it was not. Lines 2–7 still read "`the form is I^{(K)} = sum_chi I^{(chi)}`, with
`I^{(chi)}` carrying the zeros of `Lambda(s,chi)`" — the per-`χ` form withdrawn by **D1** — and still
cite the superseded `D.55.1`/`D.55.4`. Line 24 still reads "`the constant the defect theorem actually
uses (Thm 19.23 / D.41.13 may choose theta)`" — the clearing argument withdrawn by **D5** (the printed
`[4]` verdict block *was* correctly rewritten, so the file contradicts itself). **Repair:** update lines
2–7 to the packet pairing `I^{(K)}(E,F) = Σ_χ I^{[χ]}(E_χ,F_{\barχ})` and line 24 to "the constant a
`θ`-adjustable defect theorem *would* use; no such theorem is stated for `L(s,χ)` — O-47.7".

### MINOR C7 — the error direction is written both ways
§R3.5 says `d_0 ≳ 11313` carries "roughly `+9\%`" (correct: a lower bound, so the true threshold is
larger), the table cell says "`11313` (`+9\%`)" ✓, but the §Label row says "`±9\%`". Make it `+`.

### NOTE C8 — absolute convergence is used without citation
The re-indexings `ρ ↦ 1−ρ` and `ρ ↦ \barρ` in D.55.2′(ii),(iii) rearrange the zero sums. On `D^W(α)` this
is licensed (absolute convergence, phase 139 Lemma D.19.3a, cited in D.55.2′(iv) for a different purpose)
but it is not invoked where it is used. One clause.

### NOTE C9 — what the round got right that it could have got wrong
The round did **not** take the easy exits: it did not quietly keep `χ(στ^{-1})` by redefining the form as
sesquilinear (which would have re-imported an adjoint), it did not retain the `S = 1` headline in weaker
words, it did not keep `\dim H^0 ≤ 1` as a hedge, and it opened **two** new items (O-47.7, O-47.8)
against its own conclusion, including the one that cuts hardest — that a `ζ_L`-frame theorem would in
fact consume the `L`-zeros where the constants rise. It also corrected the previous auditor twice (the
`\cos(π/m)` argmin in round 2, and the redundancy of the Lipschitz margin here). That is the correct
disposition and it should be on the record.

---

## Verdict

**ACCEPT, with two required repairs (MAJOR C1, MAJOR C2) and five editorial ones (C3–C7).** All seven
MAJORs, all nine MINORs and the NOTE of `R147_004` are discharged in substance; D1–D20 record them
accurately and against this round's own interest; the numbers reproduce exactly; the script's verdict
block has been reframed correctly; and the two repairs I predicted would be forced (packet pairing,
`C_c^∞` tests) do what I predicted — they turn every round-2 `CANDIDATE` into a theorem, with no residue.
**No FATAL.** Nothing in rounds 1–3 proves RH, `¬`RH or GRH; no `h⁰` is produced; Theorem 12.3 / D.31.12
is never made to run; the bigness clause is named as GRH and declined; W-a is honoured in the documents
and in the script. The two remaining MAJORs are not obstructions to the phase's conclusion but to its
bookkeeping: **C1** is that the theorem the phase closes on is stated in three blockquotes and proved in
none of them (and proved, in the superseded round, from a withdrawn definition and by a non sequitur) —
three lines fix it; **C2** is a normalisation constant asserted over a base where the round's own round-1
theorem gives a different value — it touches no sign and no support function. With C1 written as a
numbered theorem in the `f_1 = Σ_gf` form, phase 147 may close.

## What Theorem D.55.9′ does and does not establish for row D

**Does.** On the χ-graded carrier of an abelian `L/F` — the one carrier in the corpus on which the Galois
group ring acts non-trivially, where the character table genuinely enters the intersection numbers
(D.55.4′) and where effective classes with negative character coordinates genuinely exist (D.55.8′) — the
`χ = 1` slot of the enlarged cone `𝓒` is **exactly** the old cone of nonnegative radial tests, because
the Galois action is by norm-one ideles, which fix the modulus and therefore commute with the coset
average. Consequently the support function at the zeros of `ζ_F` is `s(γ,θ)`, **identically unchanged**,
for every abelian `L/F`, every tower, and every order `m` — so the entire gain of the construction,
including the `S = 1` phenomenon at `4 ∣ m`, is confined to the `L(s,χ)`, `χ ≠ 1` sectors. This closes,
on the negative and by a theorem rather than by a failed search, the "more correspondences from a Galois
group" family of escapes for `ζ`: it is the round-1 lemma `R(Γ_σ) = \mathrm{id}` seen one level up, and
it is the same mechanism (`σ` preserves the modulus) in both places. **Does not.** It says nothing about
whether the enlarged constants matter to a frame theorem for `ζ_L` or `ζ_K` itself, which would consume
*all* the zeros of `ξ_L = ∏_χΛ(s,χ)` — that is O-47.7, and it is the round's own honest opening; nothing
about non-abelian `L/F`, where `Γ_σ` acts by matrices and D.20.2 is only conditional (O-47.8); nothing
about whether a genuinely **realizable** cone — `𝓒` is a projected model, O-47.1′ — has a larger `χ = 1`
slot than the model's, which is the one direction in which the theorem could still be wrong-sized;
nothing about (4a), multiplicity, or bigness, all of which the round has now correctly disowned; and,
emphatically, nothing about the sign. It is a **no-go of exactly one escape route**, sharply proved, and
that is the whole of what phase 147 is entitled to claim.
