# CORPUS_CHECK_R147 — the Frobenius diagonal, single-prime towers, and Frob ⋆ Δ^rad

dtrejo@biomakers.net
Purpose: pre-phase-147 corpus check for row D, item "single-prime tower / Frob ⋆ Δ^rad".

---

## 1. Paper 44 §8bis — the Frobenius diagonal, exact computation

File: `04-papers/44-row-b-arithmetic-family/main.md:3250-3900` (whole of §8bis).

**Theorem 8bis.1b** (`main.md:3416-3512`) computes, for the smeared idempotent
`Δ^{(n),[φ_ε,N]}` (unit archimedean height `φ_ε(0)=1`, bare level-`N` indicators,
`P := P(n)`):

  * (i) no shell (`q^k`, `k≠0`) contributes — killed by the archimedean window `ε<½log2`;
  * (ii) the unit packets at `p | n` vanish (no finite condition there — dependence on `n`
    is **only through `P(n)`**, exactly as the phase-147 charge supposes);
  * (iii) the finite part is **exact for every `N≥1`**:
    `Σ_{r∈S_f∖P}W_r = −Σ_{r∈S_f∖P(n)}(log r)[(r−2)/(r−1) + (N−1)]` (8bis.3′) — linear
    in `N`, slope `−Σ_{r∉P(n)}log r`, **negative**;
  * (iv) the archimedean part diverges logarithmically: `W_∞ = −log(1/ε) + O(1)` (8bis.4a).

Both quoted formulas in the phase-147 charge match verbatim: `−Σ_{r∉P(n)}(log r)[(r−2)/(r−1)+N−1]`
(8bis.3′) and `−log(1/ε)` (8bis.4a). `T_∞(Δ^{(n),[φ_ε,N]})` is finite for fixed `(ε,N)` and
**has no limit as `ε→0` or `N→∞`**; both divergences are negative.

**Corollary 8bis.1b′** (`:3514-3540`) converts this into the actual Gram diagonal `I_A(F,F)` in
both conventions via `F⋆F^† = V_N(n)·Δ^{(n),[h⋆h^†,N]}`, `V_N(n) := ∏_{r∈S_f∖P(n)}vol(1+r^NZ_r)`
(8bis.0), which **decays geometrically** in `N`. Consequence, stated as the point of the corollary:
**the sign/rate of the `N→∞` limit is convention-dependent** — bare convention → `I_A(F,F)→0`;
`♭` convention → `I_A(F^♭,F^♭)→−∞`. **No rate is headlined anywhere in the paper**, because no rate
is convention-free. The one convention-free fact is Remark 8bis.1c.

**Remark 8bis.1c** (`:3542-3555`): `I_A(Frob_n,Frob_n)` **does not exist** — Frobenius point classes
are multipliers, not elements of `D_A` (Rem 3bis.4b, Thm 3ter.14), so the diagonal pairing is not
merely divergent but structurally outside the space on which `I_A` is defined; `(ε,N)` cannot both
be removed. Consistent with Paper 43 Thm 14.1(a) (infinite negative index) and Rem 8.11
(`T(Δ)` undefined). This is the **only** convention-free statement about the diagonal: no rate, no
direction, is asserted independent of the (bare vs `♭`) normalization.

**Theorem 8bis.1e** (`:3598-3637`, "the Weil kernel IS the Gram form of the unit-averaged Frobenius
family"): for `Γ_n^{rad} := Frob_n ⋆ Δ^{rad}` (radial average), with **no indicators and no
arithmetic side conditions**, `I_A(Γ_m^{rad,sm},Γ_n^{rad,sm}) = T(Γ_{h_m⋆h_n^†}) = ∫(h_m⋆h_n^†)d(W_fin+ω_∞)`
— the **full** Weil kernel, both halves, for every `m≠n`; diagonal `m=n` is Thm 8bis.2. This is the
paper's name for what the phase-147 charge calls "the archimedean-bearing Frobenius object":
`Δ^rad` is exactly the averaging projector that **injects the archimedean block** that bare
`Frob_n^{sm}` alone lacks (Corollary 8bis.1d: the bare Frobenius family carries **only** `W_fin`,
**no archimedean off-diagonal block at all**). Mechanism (iii) of Thm 8bis.1′ (`:3639-3665`):
`supp Frob_n` is disjoint from `Im j_∞` (when `S_f⊋P(n)`), so bare Frobenius sees no archimedean
local term; convolving with `Δ^rad` spreads the support onto the whole modulus level set, which
meets `Im j_∞` at `j_∞(1/n)` — that is where `ω_∞` comes from.

**Theorem 8bis.2** (`:3667-3798`, "infinite genus"; **fixed-chart theorem, explicitly exempted from
the standing colimit convention (C1)**): for the radial approximate-identity family `F_ε` (profile
`ε^{-1}φ(t/ε)`), `I_A(F_ε,F_ε) → −∞` as `ε→0^+`, with exact rate `−(‖φ‖_2^2/ε)(log(1/ε)+O(1))` in
mass normalization, or `−log(1/ε)+C_φ+o(1)` in `L²` normalization (8bis.4b/4c). Interpreted
(Corollary 8bis.2a, labelled **an interpretation, used by no theorem**) as `Δ·Δ=−∞ ⟹ g=∞` under
Weil's curve/genus dictionary. Divergence is **entirely archimedean** (`Ŵ_∞(0,τ)~−log|τ|`), the
finite-place symbol being uniformly bounded at a fixed chart (8bis.8b).

**Standing conventions (C1)/(C2)** (`:3267-3314`) fix, once: (C1) `T` means the colimit trace `T_∞`
throughout §8bis except where a theorem is explicitly exempted (8bis.2, its corollary); (C2) the
**bare** convention (unnormalized level-`N` indicators) is used throughout, with `V_N(n)` (8bis.0)
the conversion factor to `♭`. Every displayed identity is chart-quantifier– and normalization–
labelled explicitly; this repairs earlier round-3/4 errors (`F1`, `M4`, `M5` findings) that had
conflated the two.

**Answer to charge item 1, precisely:**
  * Dependence on `n`: through `P(n)` only — confirmed in (ii)/(iii) of Thm 8bis.1b.
  * Dependence on chart level `N`: **exact and linear**, slope `−Σ_{r∉P(n)}log r`, in the bare
    convention; **geometric decay** if the `V_N(n)` conversion (8bis.0) is folded in (`♭` convention
    inverts the direction of the `N→∞` limit). No rate is convention-free (Cor 8bis.1b′).
  * Dependence on regularization `ε`: `−log(1/ε)+O(1)`, exact (8bis.4a); and in the radial/genus
    computation (Thm 8bis.2), rate `−log(1/ε)` (`L²`-normalized) or `−ε^{-1}log(1/ε)` (mass-normalized).
  * `♭` vs bare convention: defined in (C2)/(8bis.0); **the sign of the `N`-limit differs between
    them**, hence "no rate is headlined" is the paper's own verdict.
  * Differences `δ_m − δ_n`: **not** separately treated in §8bis.1b/8bis.1e; the closest object is
    the **off-diagonal** entry `I_A(Frob_m,Frob_n)` at `m≠n` (Thm 8bis.1, (8bis.1)-(8bis.2b)), which
    is a *different* computation (rational label `r=m/n`), not a diagonal difference. No theorem in
    the corpus computes `δ_m−δ_n` as such — **this would be new** (see §7 below).
  * Gram restricted to `{Frob_{p^k}}_k` for a single prime `p`: **not treated in Paper 44 §8bis** as
    a standalone sub-Gram; the single-prime object that **is** treated at length is Doc 131's
    `F_{p,α}` (Euler factor of one prime with a free weight `α`) — see §2 below, which is the
    genuinely relevant single-prime precedent, proved in a different (but directly transferable)
    framework.

---

## 2. Single-prime towers `{Frob_{p^k}}_k` — Doc 131 Thm 6.7, Doc 135 Thms A/A′/B

**The precedent is not inside Paper 44** but in the earlier "Arith" category documents:

**Doc 131** = `03-research/phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md`.
**[THEOREM 6.7]** (`:791-793`, "pureza local: H es decidible en la subcategoría de un primo"):
for the single-Euler-factor object `F_{p,α}` (weights `c_m = α^m + (p/ᾱ)^m`, i.e. exactly
`Λ(p^k)(p^{ka}+p^{-ka})`-type data with `α=p^a`, `1<|α|<p`):

    F_{p,α} satisfies H  ⟺  |α| = √p  ⟺  |c_m| ≤ 2p^{m/2}  ∀m≥1.

Proof (`:797-812`): forward direction is Prop 6.2 (divisor on `Re=½` ⟹ H); converse is an explicit
**two-bump Mertens-type test** `f = u + θu(·/p^M)` producing `Q_F(f,f) = L[2(1+|θ|²p^M) −
2Re(c̄_Mθ)](1+O(ε))`, minimized at `t*=|c_M|/(2p^M)` to value `2−|c_M|²/(2p^M)`, negative as soon as
`|c_M|>2p^{M/2}` — which occurs for `M` large whenever `δ'≠0` (`α=p^{1/2+δ'}`). **This is the
single-prime tower Gram form's positivity, decided exactly, and is manifestly `Ξ_a`-sensitive**: the
weight `|α|=p^a` is a free parameter, `a=1/2` is the unique positive point, and the mechanism is
literally "weights `Λ(p^k)(p^{ka}+p^{-ka})`" per the charge's own language. Commentary (`:830`):
"el producto de Euler no implica H" — a single pure Euler factor with `|α|=p^{0.6}` has Euler
product, functional equation, positive diagonal mass, **and violates H**; purity of the local weight,
not multiplicativity, is what decides the sign. The bound is **exactly** Ramanujan `|c_m|≤2p^{m/2}`,
and at the boundary positivity is "as tight as it can be" (exact Cauchy–Schwarz).

**Doc 135** = `03-research/phase-45-fredholm/135-two-prime-theorem-positivity-for-pure.md`. Extends Thm 6.7 to **two**
inconmensurable primes: **Teorema A (3.1)** = bilateral purity ⟹ H, exact spectral identity;
**Teorema B (4.1) + Corolario 4.2** (`:346-357`) = impurity of *either* factor ⟹ ¬H, with the
Ramanujan barrier of the two-bump test shifted from `2p^{M/2}` to `2p^{M/2}(1+L_q/L_p)` — a foreign
prime **protects additively** (its diagonal mass adds) but **cannot buy back** the impurity of
another factor, because the Ramanujan violation grows geometrically in `M` and the protection is
constant in `M`. Extrapolated to `ζ`, the total protection over all primes is `2θ(y)`, divergent
(Doc 135 §7). **Teorema A′ (7.1)** generalizes to `n` primes with a Mertens margin
`4Σ_{i<j}L_iL_j/Σ_iL_i` and kernel threshold `log(p_1⋯p_n)`. §7.2 finding B3 (quoted, `:453-461`):
Doc 135's pure objects have **local weight 1** (`|α_p|=√p`); the Euler factors of `ζ` have `α=1`,
weight 0 — a **maximal** Ramanujan violation — so "cada factor de ζ es σ-impuro y, aislado, viola H":
the regime relevant to `ζ` is **destructive** (`a=Λ≥0`), the opposite of Doc 131/135's
**constructive** pure objects (`a≤0`, unimodular-after-normalization). This is repeated verbatim in
phase-137 R137_001 §3.4 (`Doc 135's purity mechanism cannot supply the prime block` — see §5 below).

**Answer to charge item 2:** what is proved about a single prime's tower is a **sharp
iff**-classification of sign-definiteness by the local weight `a` (`α=p^a`): pure (`a=1/2`) ⟹ H
(exact Cauchy–Schwarz-tight positivity); impure (`a≠1/2`) ⟹ an explicit two-bump test forces
negativity, and the test is **manifestly `Ξ_a`-sensitive** — `a` is exactly the free parameter that
decides the sign. The two-prime and `n`-prime extensions (Doc 135) show that this local
positivity/purity **composes additively as protection but not as a cure**: no amount of well-behaved
primes rescues one impure factor, and (crucially for ζ, whose Euler weight is `a=0`, maximally
impure) the destructive `a=Λ≥0` regime of `ζ` is the mirror twin, not an instance, of Doc 131/135's
constructive positivity theorem (Doc 135's own §7.2 B3). **`TRIED–PROVED`** for the abstract
single-Euler-factor category object; **`TRIED–NO-GO`** (Doc 135 §3.4, imported into phase 137 §3.4)
as a *transfer route* to give positivity to any Weil-form's finite/prime block, including one built
from `{Frob_{p^k}}_k` alone, in the destructive regime relevant to ζ.

---

## 3. "Archimedean-bearing Frobenius object" / `Frob ⋆ Δ^rad` / diagonal renormalization attempts

Every attempt in the corpus to give the Frobenius diagonal a finite value lands on the **same**
conclusion: **any finite regularized value is not sign-relevant, because the sign question is
already answered by the full colimit statement (8bis.10), and the diagonal's finite/archimedean
split is itself convention-dependent (Cor 8bis.1b′)**. Specifically:

  * §8bis.1's own diagonal computation (Thm 8bis.1b) is presented **as** the regularized/finite
    value at fixed `(ε,N)` — it is not a failed attempt, it is the exact answer, and the point of
    Remark 8bis.1c is that **no further limit exists to take**: `(ε,N)→(0,∞)` is not a well-posed
    renormalization because Frobenius point classes are outside `D_A`.
  * The one place a genuine "regularized diagonal value" **does** exist and is used is
    `Frob ⋆ Δ^rad` (Thm 8bis.1e/8bis.2): averaging over the radial direction is what makes the
    diagonal self-pairing finite for each `ε>0` — but its `ε→0` limit is `−∞` (8bis.4b), **not** a
    finite renormalized value; this is Corollary 8bis.2a's "`Δ·Δ=−∞`", explicitly flagged as an
    interpretation used by no theorem. **This is the exact statement requested: any finite choice of
    the diagonal (any finite `ε`) makes the sign of the self-intersection negative (Remark 8bis.2b:
    the rate's coefficient is `1` in `L²`-normalization, not `2` as an earlier blueprint guessed) —
    and removing the regularization sends it to `−∞`, never to a finite sign-bearing constant.**
  * No document in the corpus attempts a **Tate-residue-style finite renormalization** (i.e., discard
    the `log(1/ε)` divergence and keep an `O(1)` constant, as one does for the self-intersection of
    the diagonal in Arakelov theory) as a *usable* invariant for row D's sign question. The `O(1)`
    constants in (8bis.4a) and (8bis.4c) are computed exactly (`γ+log4π` in 8bis.4a;
    `C_φ = log2π − ...` in 8bis.4c) but are **profile-dependent** (`φ`-dependent), so they are not
    canonical constants of the diagonal alone — this specific gap (a profile-independent finite part)
    is **not addressed** anywhere found in 03-research or 04-papers.

**Answer to charge item 3:** the exact statements are Thm 8bis.1b/Cor 8bis.1b′/Rem 8bis.1c (bare
diagonal, no limit, convention-dependent rate) and Thm 8bis.2/Cor 8bis.2a/Rem 8bis.2b (radial
self-pairing, exact rate to `−∞`, coefficient `1` not `2`). No attempt anywhere renormalizes the
diagonal to a finite, convention-free, sign-bearing number; the corpus's verdict is that this cannot
be done canonically (Rem 8bis.1c) and that the only unconditional theorem is negativity/divergence,
never a finite value.

---

## 4. Paper 47 open item (21) — the archimedean slot

File: `04-papers/47-intersection-frame-defect/archive/main.md:3809-3816` (§14.5, item 21; discussion at `:2612-2622`,
Remark 11.14a′).

Exact statement (quoted): the **kernel representation of `ω_∞` on `D^W`** — whether

    (1/2π)∫ĥ(τ)[Re ψ(¼+iτ/2) − log π]dτ = −f.p.∫h(t)K_∞(|t|)dt

for **every** real even `h∈D^W` (not just `C_c^∞` with `0∉supp h`), with the finite part in the
sense of Paper 44 (8.5∞). **Known** for `h∈C_c^∞` with `0∉supp h` (Paper 44 Theorem 3bis.7) and at
`t=0` by (8.5∞) directly; the extension to unbounded support via the decay estimate (11.1) is
"plausible" but **not proved**. Status: `OPEN`. Explicitly: "**Nothing in Part II depends on it**"
(Remark 11.14a′) — it is recorded as an open item, not a working hypothesis.

**Link to the Frobenius diagonal:** item (21) is the *archimedean symbol's* extension-to-unbounded-
support question, which is the natural companion of Paper 44's Thm 8bis.2 (archimedean divergence
`−log|τ|` of the same `Ŵ_∞(0,τ)` symbol, used at `τ=0`/bounded `τ` in 8bis.2's proof via (8bis.8)).
Both concern the same object `Ŵ_∞(0,τ) = logπ − Reψ(¼+iτ/2)`; item (21) asks whether its
finite-part/kernel identity extends past the `C_c^∞`, `0∉supp` regime that Paper 44 actually proves,
while Paper 44's own diagonal computation (Thm 8bis.1b/8bis.2) is precisely the `0∈supp` case,
handled by the counterterm `(γ+log4π)` in (8.5∞). **No document draws this connection explicitly**;
it is inferred here as a genuine open link a phase-147 note could name.

---

## 5. Phase 137 D.12 — semilocal `W_S`, `S={∞},{∞,2},{∞,2,3}`

Files: `03-research/phase-137-row-d-canonical-coupling/R137_000_BLUEPRINT.md:13-19`;
`R137_001_ROUND1.md:360-475`; `R137_002_AUDIT.md` (confirms with repairs);
`R137_007_CLOSING_DECISION.md:15`.

Definition: `W_S(F) := Σ_{v∈S}⟨F⋆F^∨,W_v⟩ − 2Φ_F(0)Φ_F(1)` (blueprint sign was refuted and
corrected in round 1/round-2 audit: the identity actually proved is
`Σ_v⟨F⋆F^∨,W_v⟩ − 2Φ_F(0)Φ_F(1) = −Σ_ρΦ_F(ρ)Φ_F(1−ρ)`, i.e. the blueprint's `W_S≥0` is the
**anti-Weil** inequality).

Answers (round-1 `§3.5`, closing decision table):
  * `S={∞}`: `W_{∞}≥0` exactly on the Connes–Consani window `supp F ⊆ [−½log2,½log2]`, primitive,
    with the extra condition `Φ_F(½)=0` (not the same as primitivity) — imported from CC 2006.13771
    Thm 1/Thm 6.11. **The polar term is zero on primitive tests inside the CC window; what costs is
    the third condition `Φ_F(½)=0`.**
  * `S={∞,2}`,`{∞,2,3}`, `T>½log2`: **`OPEN`, not provable by the named means** — Theorem D.12.4
    (`main.md`-analogue) shows added prime blocks **subtract** (adding a prime block always makes
    `W_S` harder to keep `≥0`, `main.md:R137_001:...`), and Theorem D.12.5 imports Paper 44 **Thm
    8bis.4a** verbatim: "at every finite chart there is an explicit primitive class with `Q_fin>0`"
    (i.e. positivity **fails** for the pure Frobenius/prime-only form, unconditionally, at every
    finite chart) — "**the finite half alone carries no positivity to donate**."
  * §3.4 (`REFUTED`): Doc 135's purity mechanism **cannot** be imported to supply the missing prime
    block, precisely because Doc 135's pure objects live in the *constructive* regime (`a≤0`) while
    the semilocal object needs the *destructive* regime (`a=Λ≥0`) — see §2 above, same B3 citation.
  * "First unpaid term at `2T=log2`" (closing table, `R137_007:15`): quoted exactly —
    "first unpaid term at `2T = log2` is `2(log2)2^{-1/2}(F⋆F^∨)(log2)`."

**Link to single-prime coupling with the archimedean block:** D.12 is the direct semilocal
analogue of what phase 147 is being asked to explore — coupling one or two primes' contribution to
`⟨F⋆F^∨,W_v⟩` against the archimedean block `ω_∞` — and its verdict is that **the pure-Frobenius
(prime-only) block is proved to carry no positivity to donate at any finite chart** (imports
Thm 8bis.4a), and Doc 135's single/two-prime purity mechanism is **proved inapplicable** to the
destructive regime ζ actually sits in. This is the single sharpest **prior negative result** directly
on the "single-prime tower coupled to the archimedean block" question phase 147 is chartered to
attack, and must be cited rather than re-derived.

---

## 6. Phase-60 "phase not magnitude" and P122.028 admissibility

  * **Phase 60** ("phase not magnitude"; cited at
    `03-research/phase-146-row-d-coupled-pairing/CORPUS_CHECK_R146.md:240-246`, and
    `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:57` and `:22`):
    "any bound using only `‖Λ(n)‖` cannot decide the sign, because Davenport–Heilbronn has the same
    magnitudes and the opposite sign; the sign lives in the *phase coherence* of `cos(t log n)`;
    off-line zeros give secular growth `λ^{2β−1}` no average removes." **A form depending only on one
    `p`, `log p`, `p^{−k/2}` (pure magnitude, no phase datum `e^{ikθ}` or comparable) is exactly the
    kind of object this theorem rules inadmissible as a sign-decider.** Doc 131 Thm 6.7's `F_{p,α}`
    avoids this only because `α` (hence the phase, via `α=p^{1/2}e^{iφ}` at the pure point) *is*
    present as data — the object is not pure-magnitude, it carries a phase `φ` even though the
    theorem's dichotomy collapses on `|α|` alone (the ⟹ H direction genuinely uses `Re=½`, a
    phase-position statement, not a magnitude statement).
  * **P122.028** (`03-research/phase-122-row-d-integrity-and-construction/P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md`,
    Gate S, `:168-186` per phase-146's citation): "Future work on `S` is admissible only if it
    introduces an independent input that proves the missing middle arrow. Relations derived solely
    from `log p`, `p^{-1/2}`, `N` and `Γ` cannot be cited as such an input: those data already define
    both sides of the scalar explicit formula." Recorded verdict: `PROVED-IMPOSSIBLE` for the cited
    relation classes.

**Answer to charge item 6:** a single-prime tower Gram form built only from `log p`, `p^{-k/2}` (no
phase, no cross-prime, no independent ingredient) is **provably inadmissible** as a sign-decider by
both phase-60's theorem and P122.028's Gate-S rule — this is confirmed, not merely suggested, by the
corpus. **Any phase-147 construction on `{Frob_{p^k}}_k` must carry an explicit phase/unimodularity
datum (as Doc 131's `α` does) or an independent non-magnitude ingredient (per P122.028), or it
reproduces an already-closed question.**

---

## Summary table

| # | Item | Status | Key files (path:line) |
|---|---|---|---|
| 1a | Frobenius diagonal, exact finite+archimedean value | `TRIED–PROVED` (exact, no limit exists) | `04-papers/44.../main.md:3416-3540` (Thm 8bis.1b, Cor 8bis.1b′, Rem 8bis.1c) |
| 1b | Dependence on `n` through `P(n)` only | `TRIED–PROVED` | `main.md:3436-3438` (Thm 8bis.1b(ii)) |
| 1c | Diagonal differences `δ_m−δ_n` | **NEW** — not computed anywhere found | closest is off-diagonal Thm 8bis.1 (`main.md:3317-3414`), a different quantity |
| 1d | Gram restricted to single prime `{Frob_{p^k}}_k` inside Paper 44 | not separately isolated in Paper 44 | precedent is Doc 131 instead (§2) |
| 2 | Single-prime tower positivity, `Ξ_a`-sensitivity | `TRIED–PROVED` (Thm 6.7, iff classification) + `TRIED–NO-GO` (transfer to ζ's destructive regime) | `03-research/phase-44-new-mathematics/131-algebra-of-arithmetic-correspondences-the-category.md:789-831`; two/n-prime extension `03-research/phase-45-fredholm/135-two-prime-theorem-positivity-for-pure.md:346-461,690-712` |
| 3 | Finite renormalization of the diagonal | `TRIED–NO-GO` (no canonical finite value exists; only divergence, both conventions) | `main.md:3514-3798` (Cor 8bis.1b′, Thm 8bis.2, Cor/Rem 8bis.2a/b) |
| 4 | Paper 47 open item (21), archimedean kernel slot | `OPEN`, unused, link to diagonal inferred not stated | `04-papers/47-intersection-frame-defect/archive/main.md:2612-2622,3809-3816` |
| 5 | Phase 137 D.12 semilocal `W_S` | `TRIED–PARTIAL/NO-GO` beyond `S={∞}`; imports Thm 8bis.4a as the operative obstruction | `03-research/phase-137-row-d-canonical-coupling/R137_001_ROUND1.md:360-475`; `R137_007_CLOSING_DECISION.md:15` |
| 6 | Phase-60 / P122.028 admissibility vs pure-magnitude single-prime forms | `TRIED–NO-GO` (both proved, both apply directly) | `03-research/phase-136-row-d-map/PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:22,57`; `P122_028_TWO_PRIME_FINITE_GREEN_COMPLEX.md:168-186` |

---

## What would be NEW in a phase-147 built on the single-prime tower and `Frob ⋆ Δ^rad`

1. **Diagonal *differences* `δ_m − δ_n`** (or, single-prime tower version, `δ_{p^k}−δ_{p^{k'}}`),
   as opposed to the off-diagonal Gram entry `I_A(Frob_m,Frob_n)` (Thm 8bis.1) or the diagonal itself
   (Thm 8bis.1b): **not computed anywhere in the corpus**. This is a genuinely open computation.
2. **A profile-independent (canonical) finite part of the regularized diagonal or of `Frob⋆Δ^rad`'s
   self-pairing** — the corpus computes exact `O(1)` constants (8bis.4a, 8bis.4c) but they are
   `φ`-dependent; a canonical (Arakelov/Tate-residue-style) finite value, if one could be
   characterized as convention- and profile-free, would be new. (Rem 8bis.1c currently forecloses
   this for the *bare* diagonal but the radial/`Δ^rad` self-pairing's finite part at fixed `ε` has not
   been asked to be made profile-free.)
3. **A single-prime-tower object `{Frob_{p^k}}_k` carrying an explicit phase/unimodularity datum**
   (à la Doc 131's `α=p^{1/2}e^{iφ}`) coupled to `Δ^rad`/the archimedean block, satisfying the
   phase-136 three-clause admissibility test (model-coupling, quadratic growth, unimodularity-
   reading) — this specific combination (single-prime Doc-131-style purity test **restated as a
   Gram sub-block of the Frobenius family and explicitly coupled to `ω_∞` via `Δ^rad`**) has not been
   built; phase 137's `W_S` couples primes+archimedean but never via `Δ^rad`, and never with the
   `Ξ_a`-sensitive per-prime weight of Doc 131 Thm 6.7.
4. **Extending Paper 47's open item (21)** (kernel representation of `ω_∞` on unbounded-support
   `D^W`) using the single-prime-tower/`Frob⋆Δ^rad` machinery, and explicitly linking it to Paper 44
   Thm 8bis.2's archimedean divergence mechanism — this connection is not drawn anywhere in the
   corpus.
5. Everything else asked by the charge (single-prime pure-magnitude Gram forms as sign-deciders;
   transfer of Doc 135's purity to the destructive/ζ regime; `W_S` positivity beyond `S={∞,2}`) is
   **already closed** as `TRIED–NO-GO` and must not be re-attempted without a materially new,
   independent, non-magnitude ingredient (per phase-60, P122.028, and phase-137 D.12's own verdicts).
