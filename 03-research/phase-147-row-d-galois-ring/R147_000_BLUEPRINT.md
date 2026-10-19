# R147.000 — Blueprint, phase 147: the Galois group ring as the missing `+`

and then this phase. Inputs of record: `R145_005` (the frame has `⋆` and no `+`; missing effective classes
are graphs of sums; for `g = 1` bigness = PSD of `deg(m+nπ)` on `Z[π]`, a count), `R146_005` (Weil's ring has
no analogue over `Spec Z`: `Hom(Spec Z, Spec Z) = {id}`, the arithmetic Frobenius is a translation of the
class group, not a homomorphism; the formal Hecke sums are zero-blind; the computed diagonal `P(m) = P(n) ⟹
δ_m = δ_n`), `CORPUS_CHECK_R147.md` (pure-magnitude single-prime forms are no-go), `CORPUS_CHECK_R147b.md`
(the Galois reading is NEW in all four components; Warning: positing a positive trace form on an endomorphism
ring = assuming RH — R145_004 Warning 1; Paper 44 Thm 8bis.4a: Frobenius Gram unsigned at every finite
chart), phase 139 D.20 (base change of `I_∞` over conjugate packets, abelian unconditional; `K_K`), phase 140
D.22 (`Frob_𝔫`, `Sh_{O_K}` for every number field), Paper 44 §8bis (coset indicators, shifted-coset Gram),
phase 139 D.19 (Epstein as a class-group-character combination).*

Standing rules as before. **Binding warnings:** (W-a) deliver **counts** and **effective realizations**, never
positivity of a trace form (that is RH); the deliverable is a cone of effective classes and the theorem of
what it contains. (W-c) every statement must be run for the falsifiers **by structure**: `Ξ_a` has no Galois
structure (it is not a Dedekind zeta) — say exactly which construction fails to exist for it; `Ξ_Q` (Epstein)
is `(1/h)Σ_χ \overline{χ}(𝔄)L(s,χ)`, a **signed** combination of Hecke L-functions — show it is not in the
effective cone; `ζ_K`: everything must be uniform in `K` (T1 is now the reason the ring exists at all).

## The idea (to be built or refuted)
Weil's `+` is `End(J) ⊇ Z[π]`, available because Frobenius is a morphism of the curve. `Spec Z` has no
morphisms, so no ring. But `Spec O_K` for `K/Q` Galois has genuine automorphisms `σ ∈ G := Gal(K/Q)`: their
graphs `Γ_σ ⊂ Spec O_K ×_{Spec Z} Spec O_K` are honest effective "curves" on the arithmetic square, the group
ring `Z[G]` is a ring of effective correspondences with composition `Γ_σ ∘ Γ_τ = Γ_{στ}`, and the Frobenius
elements `Frob_𝔭 ∈ G` (for unramified `𝔭`) sit **inside** the ring. Over `Q` the ring is `Z`: this is why
row D over `Q` alone looks rigid, and why T1 demanded field-uniformity. The question is whether
`Z[G]`-effective classes, together with the Frobenius correspondences `Frob_𝔫` of phase 140 and the rulings,
generate a cone that **fills the positive cone** of the square of `Spec O_K` — the bigness the frame lacked —
or at least strictly enlarges `𝓔` in the direction the cosh witness needs.

## D.50 — The Galois correspondences on the arithmetic square (construction)
1. **Objects.** For `K/Q` finite Galois with group `G`, `S ⊇ S_∞ ∪ {ramified}`, the carrier `C_{K,S}`
   (phase 139/140), the Weil class `D^W_K`, `I_∞^{(K)}`, `K_K`, `Frob_𝔫` (phase 140 D.22). Define the
   **Galois correspondence** `Γ_σ` on `C_{K,S}` (σ acts on ideles of `K`; on `C_{K,S}` as a group
   automorphism commuting with the norm to `C_{Q,S}`). Prove: `Γ_σ` is an effective class (a positive
   measure on the square / a nonnegative kernel), `Γ_σ ⋆ Γ_τ = Γ_{στ}`, `Γ_σ^† = Γ_{σ^{−1}}`, `Γ_1 = Δ`;
   bidegree `(1,1)`; and the interaction with Frobenius: `Γ_σ ⋆ Frob_𝔫 ⋆ Γ_σ^{−1} = Frob_{σ𝔫}`. Label.
2. **Pairings.** Compute `I_∞^{(K)}(Γ_σ, Γ_τ)`, `I_∞^{(K)}(Γ_σ, Frob_𝔫)`, `I_∞^{(K)}(Γ_σ, K_K)` from the
   explicit formula for `ζ_K` decomposed by Artin characters (phase 139 D.20 machinery): the Galois
   action on the zero space is the decomposition `ζ_K = ∏_χ L(s,χ)^{χ(1)}`, so `Γ_σ` acts on the `χ`-isotypic
   part by `χ(σ)`. Expected: `I_∞^{(K)}(Γ_σ,Γ_τ) = (polar) − Σ_χ χ(1)χ(σ^{−1}τ)·(zero sum of L(s,χ))` — the
   **character table enters the intersection numbers**. Prove exactly; state the degree `deg Γ_σ` and the
   fixed-point count (`Γ_σ · Δ` = measure of the fixed locus of `σ` on `C_{K,S}`) — this is where the "count"
   lives: the fixed points of `σ` are the ideles fixed by `σ`, i.e. those coming from the fixed field `K^σ`:
   `Γ_σ · Δ = ?` (compute; compare with the geometric `#Fix(σ)` on a curve with automorphisms).
3. **The ring.** `𝓡 := Z[G]` acting on `D^W_K` by `Γ_σ`; the effective cone `𝓔_G := {Σ_σ a_σ Γ_σ ⋆ E : a_σ ≥ 0,
   E ∈ 𝓔}` and its enlargement by Frobenius `𝓔_{G,Frob}`. Prove the analogue of the model's formula
   `[Γ_{φ+ψ}] = [Γ_φ]+[Γ_ψ] − F_2 + 2⟨φ,ψ⟩F_1` — here `Γ_σ + Γ_τ` is a **union** (effective, both
   coefficients nonnegative), so the new content is NOT sums of two elements but the **relations** in the
   character table: `Σ_σ χ(σ)Γ_σ` (the isotypic projectors, rational multiples) — which classes with
   negative coefficients are effective? E.g. is `|G|·Δ − Σ_{σ≠1}Γ_σ`-type (the augmentation) effective?
   In geometry, for a curve with automorphism group `G`, the classes `Γ_σ` and their combinations with
   the fibres fill part of `NS(C×C)`; compute in the model first (D.53).
4. **Effectivity of Galois-twisted Frobenius.** The classes `Frob_𝔫 ⋆ Γ_σ` are effective (composition of
   effective correspondences). Their span mod `𝓝_∞^{(K)}` and the cone they generate: does it contain classes
   with `Φ(0)Φ(1)`-data and zero-data that the radial cone `𝓔` cannot reach? Test: the cosh witness of R142
   (transported to `K`: R142 D.31.12 holds for `ξ_K` given a simple on-line zero of `ζ_K`) — is the witness
   class `E = tF_0 + dK_K` equivalent mod `𝓝_∞^{(K)}` to a class in `𝓔_{G,Frob}`? Compute the cosh-lemma
   constant for `𝓔_{G,Frob}` (the analogue of `s`: `σ(𝓔_{G,Frob}) := sup |Re e^{iθ}Φ_{E'}(ρ)|/(½deg E')`
   over the new cone): does it exceed `s_1`? (W-a: this is a computation of a support function of a cone,
   not a positivity claim.) If it reaches `1`, the defect theorem's obstruction is lifted for `ξ_K` — say so
   and immediately check what the transfer theorem would then give and whether it is RH-strength (FATAL
   rule: flag, run the falsifiers).

## D.51 — Falsifiers by structure
* `Ξ_a`: no field `K`, no `G`; the construction does not exist. Record where each statement of D.50 uses `G`.
* `Ξ_Q` (Epstein, `K = Q(√−D)`, `G = Z/2`, `h > 1`): the class-group characters are **not** Galois characters
  of `K/Q` (they are characters of `Cl(K)` = Galois group of the Hilbert class field `H/K`). Work over `H/Q`
  (Galois? `H/Q` is Galois with group `Cl(K) ⋊ Z/2` — check) and show: `ζ_H = ∏_χ L(s,χ)` (all class-group
  characters, product), while `Z_Q ∝ Σ_χ \overline{χ}(𝔄)L(s,χ)` is a **signed sum** — the class realizing `Z_Q`
  in the `Z[Gal(H/Q)]`-module is not in the effective cone. Prove it (the coefficients `\overline{χ}(𝔄)` are
  not all nonnegative unless `𝔄` is principal, i.e. `Z_Q = Z_{Q_0}` the principal form — and even then it is
  `(1/h)Σ_χ L(s,χ)`, not a product: check whether the principal Epstein zeta IS in the cone (it is a
  nonnegative combination!) — if it is, and it has off-line zeros (Davenport–Heilbronn for the principal
  form with `h > 1`, R139), then **effectivity in `𝓔_G` does not imply Hodge index**, and the cone is too
  big; resolve this carefully: the principal Epstein zeta is the zeta function of the *set* of principal
  ideals, a sub-object, not a Galois-invariant one — determine whether it corresponds to an effective class
  on the square of `Spec O_H` or of `Spec O_K` and what its degree/self-intersection is. This is the sharpest
  test of the whole idea.)
* `ζ_K`: uniformity — every construction must be for all `K/Q` Galois; towers `L/K/Q` and the compatibility
  of `𝓔_G` with induction/restriction (Artin formalism at the level of cones).

## D.52 — What bigness would require, stated without RH
From R145 Prop D.42.5: a closed `𝓝_∞`-saturated cone with the degree gate satisfies bigness iff RH. So the
target is **not** "𝓔_{G,Frob} is big" (that would be RH for `ζ_K`) but the **mechanism**: does `Z[G]` provide
(4a) of (P145′) — a sections functor `E ↦ H⁰(E)` with a divisor map into `𝓔_{G,Frob} ⊗ Q` — via the
regular representation (the `|G|` copies of the identity in `Z[G]`, `H⁰(E) := (Z[G]-module generated by
E)^{G-invariants}`, dimension counting by Frobenius reciprocity)? Analyse: what is `dim H⁰` for `E = mK_K`?
Does it grow like `m²`? (In the model with automorphisms: `H⁰(C×C, O(D))^G`.) State honestly what is
computable and what is (4a) itself.

## D.53 — The model: a curve with automorphisms over `F_q`
Take a Galois cover `C → P¹` or a curve with `G = Aut(C)` nontrivial over `F_q` (e.g. an elliptic curve
with CM by `Z[i]` over `F_p`, `p ≡ 1 mod 4`, `G ⊇ Z/4`; or a hyperelliptic curve with its involution). Compute
`NS(C×C)`, the classes `Γ_σ`, `Γ_{π^n}`, `Γ_{σπ^n}`, their intersection numbers (`Γ_σ·Γ_τ = #Fix(σ^{−1}τ)`,
`Γ_σ·Γ_π = #{x : σx = πx}`), and the cone they generate vs `Eff(C×C)` vs `Pos`. Decide: does adding the
automorphism graphs (and their Frobenius composites) enlarge the frame's cone `𝓔_C` toward `Eff`? By how
much (the model's `s`)? This is the control experiment; the arithmetic construction is judged against it.

## D.54 — Synthesis input
One page: does `Z[G]` supply a genuine `+` (effective classes with negative coefficients in the Frobenius
basis) — yes/no with the model's numbers and the arithmetic cosh constant; the Epstein resolution; what
remains for (4a); recommendation.

## Deliverables and rounds
`R147_001_ROUND1.md` (D.50 items 1–4; D.51 complete, especially the Epstein resolution; D.52; D.53
with an explicit curve; D.54; corpus check per idea; paper-facing; open list; label), README; audit
`R147_002`, repairs, confirmation, `R147_005`. Scripts only for the model's intersection numbers and
the cosh constant (`--fast`, margin).

## Warnings
* No positivity claims about trace forms on `Z[G]` (W-a). A support-function computation is allowed; a
  "therefore PSD" is not.
* The Epstein test (D.51) can kill the idea in one line if the principal Epstein zeta is an effective class
  with off-line zeros; do it early and report it plainly if so.
* Do not reuse the collapsed Pólya realization for zero data (R140); use the Artin decomposition.
