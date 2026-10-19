# R137.001b — Paper 46 Part III (§§17–19), **draft, round 2**; not appended, and not appendable this round

Proofs and
repairs: `R137_001_ROUND1.md` (round 1) as corrected by `R137_003_ROUND2.md` (round 2).

## 0. Status: NOT to be appended in this round, and why

The audit's ruling is explicit ("Do not append"), the coordinator has confirmed it, and I
agree. Round 1's reasons stand and two more have been added:

1. **Protocol.** Parts I and II entered Paper 46 only after report → audit → repair → confirmation.
   Round 2 is the repair; the confirmation round has not happened. Phase 135's own ledgers (§§9.2a,
   9.2b, 14.4a, 14.4b) record what round-1 material looked like before audit, on this very object.
2. **An undeclared zero-location import.** §17.4 rests on `|ζ(1+iτ)|^{−1} ≪ \log^{7}(2+|τ|)`, a
   quantitative form of `ζ(1+iτ) ≠ 0`. Paper 46 §1.13 lists every zero-location fact the paper uses;
   the *qualitative* fact is already there (via (E2), Proposition 11.11a), the quantitative one is not.
   Appending §17.4 requires adding the §1.13 row and the §15 import tag (X19). The
   zero-free-region-free alternative was worked out in round 2 (`R137_003` §2.4b) and **fails**: the
   degree ceiling `Φ_E(σ) ≤ m` holds only on `σ ∈ [0,1]`, inside which `ξ` may vanish, so the method is
   forced onto `\mathrm{Re}\,s = 1`.
3. **One statement is `CANDIDATE`, not `PROVED`** (§17.6(ii), hypothesis `(H_a)`), and one is now a
   `HEURISTIC` question rather than a statement (§19.2).
4. **§19 is a comparison, not a theorem.** Its placement — Part III, a subsection of §14, or outside the
   paper — is a decision.

**Recommendation unchanged.** Append §§17–18 after a confirmation round and after §1.13 is amended;
place §19 in §14 (connections) or leave it in the phase directory.

---

## 1. Draft §17 — D.11: growth of `h⁰_Z(mK)` on the full lattice

**Lemma 17.0a** (`PROVED`). `ΠK(t) ≤ 0` for `|t| ≥ u_0 := \tfrac12\log(5.1/π) = 0.2422553…`; hence
`\{ΠK > 0\} ⊂ (−u_0,u_0)`. *Proof: term by term, `f_n'' ≥ f_n/4` whenever `x := πn²e^{2t} ≥ 5.1`, which
reduces to `8x³−56x²+82x−18 ≥ 0`.* (`R137_003` Lemma 2.1.)

**Lemma 17.0b** (`PROVED`). `K(t) ≥ 2π²e^{9t/2}e^{−πe^{2t}}` for `t ≥ 0`; hence
`κ_q := \min_{|t−\log q|≤u_0}K(t) ≥ e^{−βq²}` with `β := πe^{2u_0} = 5.1`. (`R137_003` Lemma 2.2,
Corollary 2.3.)

**Theorem 17.1** (`PROVED`). For `λ ∈ H⁰_Z(mK)`, `E := mK+λ`: `\deg E = m`; `0 ≤ Φ_E(σ) ≤ m` on `[0,1]`;
`|Φ_E(σ+iτ)| ≤ Φ_E(σ)`; and for `σ ∈ (0,1)`,
`−m/(σ(1−σ)) ≤ A(σ) ≤ m(1−ξ(σ))/(ξ(σ)σ(1−σ))`, `A(s) = Σ_qa_qΛ(q)q^{s−1}`. *(The upper bound is new;
Lemma 13.5b gives only the lower one. Both bounds control only the **signed** sum; cancellation between
coefficients of opposite sign is untouched — Remark 13.6b's obstruction, unchanged.)*

**Theorem 17.2** (`PROVED`). With `M_+ := \sup ΠK ≤ 17` (certified numerically, upper bound only): for
`m ≥ M_+w_q/κ_q` the class `−w_qτ_{\log q}(ΠK)` lies in `H⁰_Z(mK)`. For `q = 2` the value `m = 4\,538\,961`
suffices, so `h⁰_Z(mK) > 0` from there on. **No threshold here is sharp.**

**Remark 17.2a** (`PROVED`). Theorem 17.2 proves the **sufficiency** direction of Remark 13.6a's
heuristic (`m ≥ ce^{βq²}` suffices for one generator at `q`, `β = 5.1`), and the **necessity** direction
holds too: feasibility forces `mK(\log q) ≥ w_qΠK(0)` and `K(t) ≤ Ce^{9t/2}e^{−πe^{2t}}` for `t ≥ 0`, so
`m ≥ cq^{−5}e^{πq²}`. Together: the single-generator threshold lies between `e^{πq²}` and `e^{5.1q²}`,
i.e. `\log q = \tfrac12\log\log m + O(1)` — **Remark 13.6a's heuristic, now a theorem in both
directions** — and the count exceeds `1` from `m ≈ 4.5·10^6`. §13.2's numerical count `1` reflects the
range `m ≤ 8`. *This is a confirmation of Remark 13.6a, not a correction of it.*

**Theorem 17.3** (`PROVED`). `h⁰_Z(mK) ≥ c\,(\log m)^{3/2}/\log\log m` for `m ≥ m_1`, `c, m_1` absolute.
*So the full lattice strictly beats every finite truncation of Lemma 13.5a, by a power of `\log m`.*

**Theorem 17.4** (`PROVED`; imports: Montgomery–Vaughan (`CLASSICAL`), Stirling (E4), and **(X19)**
`|ζ(1+iτ)|^{−1} ≪ \log^{7}(2+|τ|)` — *a zero-location input, see §0.2*). If all indices of
`λ ∈ H⁰_Z(mK)` are `≤ Q` then `Σ_q|a_qΛ(q)|² ≤ Cm²e^{CQ}` and
`h⁰_{Z,≤Q}(mK) ≤ Cπ_*(Q)(\log m + Q)`. In particular Lemma 13.5a's uncontrolled radius satisfies
`ρ_Q ≤ Ce^{CQ}/\min_{q≤Q}Λ(q)` — the first explicit bound on it, and **not** the uniformity item (23)
asks for.

**Corollary 17.5** (`PROVED`). Let `Q(m)` be the largest index occurring in `H⁰_Z(mK)`. (i)
`Q(m) ≥ c\sqrt{\log m}`. (ii) If `Q(m) < ∞` then `h⁰_Z(mK) ≤ Cπ_*(Q(m))(\log m + Q(m))`. (iii) There is
an absolute `ε_0 > 0` with: `Q(m) ≤ ε_0m\sqrt{\log m}` `⟹` (c) fails for `h⁰_Z`; equivalently
**(c) `⟹` `Q(m) > ε_0m\sqrt{\log m}`**. (iv) **There is no converse**, since (ii) is an upper bound only;
so `Q(m) = o(m\sqrt{\log m})` is *sufficient*, not necessary, for item (23). (v) `Q(m) < ∞` and
`h⁰_Z(mK) < ∞` are **not proved**. `OPEN`.

**Theorem 17.6** (`CANDIDATE`). (i) Theorems 17.1 and 17.4 transfer to `Ξ_a` verbatim by Proposition 12.6
(`PROVED`). (ii) Theorem 17.3 transfers **under the hypothesis `(H_a)`**: one of `\{Π_PK_a > 0\}`,
`\{Π_PK_a < 0\}` has bounded complement. `(H_a)` needs a Laplace analysis of
`K_a = (e^{at}K)⋆(e^{−at}K)` that is not carried out. `CANDIDATE`.

**Remark 17.7** (`RESTATEMENT`). The construction of Theorem 17.3 is **model-uniform** in the sense of
(12.3), so by **Restatement 12.4a** no derivation of (a)+(b′)+(c) can rest on it alone. Both `ξ` and
(under `(H_a)`) `Ξ_a` receive **lower** bounds from it; **nothing is claimed about which count is
larger** — that would need an upper bound on the full lattice, which is item (23) itself — and nothing
about any sign. *(Round 1's "`Ξ_a` has strictly more sections" and the disqualification criterion built
on it are withdrawn; see `R137_003` §2.5.)*

## 2. Draft §18 — D.12: the semilocal object with the polar block

**Definition 18.1.** `W_S(F) := 2Φ_F(0)Φ_F(1) − Σ_{v∈S}⟨F⋆F^∨,W_v⟩`, so that
`W_{\text{all}}(F) = Σ_ρΦ_F(ρ)Φ_F(1−ρ)`, the Weil quantity. *(The blueprint's opposite sign would state
the anti-Weil inequality; see `R137_001` §3.1.)*

**Normalization check** (`PROVED`). CC define `W_∞ := −W_R` with an explicit note of the sign change
`[cc:88–90]`; on primitive `F` with `\mathrm{supp}(F⋆F^∨) ⊂ (−\log2,\log2)` their `W_∞(g⋆g^*)` is the
corpus's `W_{\{∞\}}(F)`. Conventions agree.

**Theorem 18.2** (`PROVED`). If `\mathrm{supp}F ⊆ [−T,T]` with `2T < \log2`, then
`W_S(F) = W_{\{∞\}}(F) = W_{\text{all}}(F)` for every finite `S ∋ ∞`. *Inside the Connes–Consani window
the `S`-dependence is vacuous.*

**Corollary 18.3** (`IMPORTED`; CC Thms 1 `[cc:109–111]`, 6.11 `[cc:3108]`, `13 < c < 17` `[cc:3163]`).
On that window `W_S(F) ≥ 0` for real `F` satisfying CC's conditions; imposing primitivity **and**
`Φ_F(½) = 0` is more than CC need, so the conclusion holds a fortiori. Without `Φ_F(½) = 0`, the deficit
is at most `c|Φ_F(½)|²`.

**Remark 18.3a** (`PROVED`; corrects round 1). CC's conditions are on `g`, and on `f = F⋆F^∨` the pair
(11) `[cc:236–239]` collapses to the **single** equation `Φ_F(0)Φ_F(1) = 0` — strictly **weaker** than
primitivity. For real **even** `F`, `Φ_F(0) = Φ_F(1)` and CC's single condition *is* primitivity; on odd
tests it is weaker. The corpus's third condition `Φ_F(½) = 0` (`= \hat g(0) = 0`) has never been imposed
in Papers 43–46.

**Remark 18.4** (`PROVED`; demoted from a theorem). For `2T > \log2` the first term that enters is
`2(\log2)2^{−1/2}(F⋆F^∨)(\log2) = 0.98026…·(F⋆F^∨)(\log2)`, and `F ↦ −⟨F⋆F^∨,W_2⟩` is not nonnegative
(`W_2` is a positive atomic measure; `F⋆F^∨` can be made positive at `\pm\log2`). Consequently
**`W_{\{∞\}} ≥ 0` carries no information about `W_{\text{all}} ≥ 0`**: `W_S` decreases as `S` grows, and
the target sits at the bottom of the chain.

**Remark 18.5** (`RESTATEMENT` + `NOT-APPLICABLE`). Doc 135's Theorems A/A′ are theorems of the
**constructive** regime; the object here is the **destructive** regime (`a = Λ ≥ 0`, polar block). Doc
135 says so itself (§7.2 B3) and files this object as its own open problem `[GAP-135.B]`. So the route
"purity for the prime part + `∆ → Σ` for the archimedean part" does not apply. *(Round 1's use of Paper
44 Thm 8bis.4a here is **withdrawn**: its witness has uncontrolled support, and Remark 8bis.4b declares
the colimit statement `OPEN`. Whether the pure Frobenius form fails positivity under D.12's support
restriction is `OPEN`.)*

**Remark 18.6** (`IMPORTED`). D.12(ii) is Connes–Consani's own stated next step `[cc:82–84]`: "implement
this fundamental positivity in the semi-local framework applied to the finite set of places
`\{∞,2,3,…,p\}` … for functions `f` fulfilling `\mathrm{Support}(f) ⊂ (p^{−1},p)`".

**Open items (24)–(26)** (`OPEN`, new): (24) a finite `(S,T)` with `W_S ≥ 0` for `ξ` and `W^{(a)}_S < 0`
for `Ξ_a` on the same support class — the acceptance test for any sign-carrying semilocal theorem;
(25) `W_{\{∞,2\}} ≥ 0` for some `T > ½\log2`; (26) the narrow-support version of Thm 8bis.4a.

## 3. Draft §19 — D.13: the Connes–Consani dictionary

Split into three columns, as the audit requires; the round-1 single `RESTATEMENT` label was wrong.

**Exact identity, with the computation** (`PROVED`): CC's `Q = −(ρ∂_ρ)²+¼` `[cc:243]`, `[cc:1445]` **is**
`Π = −∂_t²+¼` of (1.11): `ρ∂_ρ = ∂_t` at `t = \logρ`, and the symbol `z²+¼` of CC's footnote is `s(1−s)`
at `s = ½+iz`. *This is the section's one genuine identity.*

**Exact, after correction** (`PROVED`): the vanishing conditions, as in Remark 18.3a.

**Analogies** (`HEURISTIC`; no map constructed in either direction): scaling kernel `δ(λx−y)`
`[cc:145–148]` ↔ `Frob_n`; trace ↔ `T_∞`, `I_∞`, diagonal ↔ `Δ`; `∆` `[cc:588]` ↔ the polar packet `K`;
`Σ` ↔ `Λ_W ⊂ 𝓝_∞`; `δ(ρ)` (8) `[cc:193–202]` ↔ the Tate block `𝔅_T` / `Σ(T)`; the jump of `δ'`
`[cc:226–232]` ↔ the diagonal divergence (8bis.4a).

**Statement 19.1** (`RESTATEMENT`). CC pay the archimedean obstruction and only it; by their own sentence
`[cc:139–141]` the approach is "not yet in shape to handle the delicate principal values involved in the
Riemann–Weil explicit formula". In this paper's terms those are the diagonal divergence of Paper 44
Thm 8bis.2 / (8bis.4a), taken at `ρ = p^{\pm k}` instead of at `ρ = 1`.

**Statement 19.2** (`HEURISTIC`; open item (27)). Two sourced facts and **no inference**: (a) CC's `Σ`
carries a positive functional (Thm 4.7, `[cc:289–296]`); (b) `Λ_W ⊂ 𝓝_∞`, and `𝓝_∞` is the **radical**
of `I_∞` (Thm 11.11). No construction identifies the two objects, so nothing follows about transferring
`∆ → Σ`. The question — *is there a completion in which `𝓝_∞` carries a positive functional as CC's `Σ`
does?* — is `OPEN`.

## 4. Ledger rows to add at Paper 46 §14.4 / §14.5, **if and when** Part III is accepted

| statement | label | what it changes |
|---|---|---|
| Lem. 17.0a, 17.0b | `PROVED` | two explicit constants for `K`, `ΠK`, proved analytically |
| Thm 17.1 | `PROVED` | adds the upper half of Lemma 13.5b |
| Thm 17.2, Rem. 17.2a | `PROVED` | **confirms** Remark 13.6a's single-generator heuristic and gives its threshold |
| Thm 17.3 | `PROVED` | full lattice `≫` every finite truncation; refines item (23) |
| Thm 17.4 | `PROVED` **with (X19)** | first explicit bound on `ρ_Q`; **requires §1.13 and §15 amendments** |
| Cor. 17.5 | `PROVED` | (c) `⟹` `Q(m) ≫ m\sqrt{\log m}`; no converse |
| Thm 17.6 | `CANDIDATE` | `Ξ_a` transfer, under `(H_a)` |
| Rem. 17.7 | `RESTATEMENT` | Restatement 12.4a applied to the growth mechanism |
| Def. 18.1–Rem. 18.6 | mixed | the semilocal object, its exact scope, the first term, CC's programme |
| §19 | `PROVED` (one row) + `HEURISTIC` (the rest) | `Q = Π`; the vanishing conditions corrected |
| **Obs. 2.1** (`R137_005` §2, N4) | `PROVED` | **corrects §14.5 item (23)**: the word "equivalently" is wrong — uniform `ρ_Q` alone leaves `h⁰ ≤ π_*(Q)\log(2mρ+1)`, still divergent in the rank; it must be combined with a bound on `Q(m)`, whereas `Q(m) = o(m\sqrt{\log m})` alone **does** suffice |
| items (24)–(27) | `OPEN` | new open items for §14.5 |

**No sign is claimed, asserted or suggested in this draft.**
