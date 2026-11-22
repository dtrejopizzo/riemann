# R157_006 — Audit of R157_005 (the one-round test Lemma P157.S1 on (P152.2), the Berkovich-line kernel)

Object: `R157_005_BERKOVICH_TEST.md`. Pure mathematics; no computation
was run. No sign is claimed for ζ at any window, in either form. Row D has no label, and nothing here changes one.
Papers and READMEs were not edited. Amendments are applied in place in R157_005, each marked
"[amended per R157_006, Bk]".

Criteria. R157_005 was written (08:12) against the **unamended** Lemma P157.S1. The parallel audit R157_004 §3
(final 08:17) amended it: (a) → a statement about derivations (A19), (b) → (b′) (A20), (c) → P47 Prop 12.4B + Hardy
(X16) as a schema (A21), and a new (d) (A22), with the Pass clause requiring A3 and one of A7/A8/A9. This audit grades
R157_005 against the **amended** lemma, as specified.

Scale: PASS (correct, correctly cited), AMEND (conclusion stands after the listed repair), FAIL (false, or unproved
as labelled).

## 0. Sources opened this round (open access only)

arXiv PDFs, read as text in the scratchpad and not stored in the repository (copyright):

| source | what was read | used for |
|---|---|---|
| Morrow, *Global pluripotential theory for adelic line bundles*, arXiv 2507.10410v1 | whole paper by grep; §1, §2.4, §3.1–3.3 (Defs 3.1.2, 3.1.3, 3.3.1), §7.1, §8 (eq. (8.1.0.1), Def. 8.2.1) | doubt 1 |
| Poineau, *Dynamique analytique sur Z. I*, arXiv 2201.08480v5 | §1 (Thms A, B, Prop. C, Cor. D, Thm E), §3.3 (Defs 3.16, 3.17) | doubt 1 |
| Poineau, *La droite de Berkovich sur Z*, arXiv 0809.2880 (= Astérisque 334) | introduction, "Description des espaces en jeu" | doubt 6, Lemma 2.1 |
| Lemanissier–Poineau, *Espaces de Berkovich globaux*, arXiv 2010.08858 | table of contents; §4.3 (Thm 4.3.8); grep for "potentiel/énergie/energy" (0 hits) | doubt 1, Lemma 2.1 |
| Chambert-Loir, *Heights and measures on analytic spaces*, arXiv 1001.2517v2 | §1 overview; §3 (global heights, product formula); §3.4.1 (arithmetic Hodge index) | doubt 1 |
| Favre–Rivera-Letelier, arXiv math/0407471 | eqs. (1)–(4), Defs 1.1–1.2, §2.4 eq. (7), Prop. 2.6 eq. (9), Lemma 4.4 eq. (22), Prop. 4.5 eq. (23), Lemma 4.8 | citation check |
| Gubler–Rabinoff, arXiv 2506.13548 (abstract) | fixed non-archimedean field; not over Z | ruled out of scope |

Corpus files opened: Paper 46 `main.tex` l.115–160 (`eq:W`, `P_T`), l.495–520 (`def:PD`), l.1160–1215 (`def:W`,
`eq:nuw`, `thm:Z`, `eq:fw`), l.2098–2140 (`thm:SC`, `cor:SC1`), l.3300–3420 (`lem:cpos`, `thm:finmod`,
`prop:finsupp`, `cor:void`). Paper 47 `main.md` l.2899–3070 (Prop 12.4B, Thm 12.4, Restatement 12.4a, Remark 12.4a′).
`114_d_195_CONTACT_GNS_POISSON_CP_AND_TATE_JET_DEFECT.md` (whole). `MAP_1_WALLS_AND_MASTER_DOCS.md:48`.
`R152_001` l.16, 266, 303, 407. `R157_002` §5 (amended). `R157_004` §3.

## 1. Citation check

| R157_005 cites | found | verdict |
|---|---|---|
| FRL "Def. 1.2 and eq. (3)", height `½Σ_v(([F]−ρ_v,[F]−ρ_v))_v` | Def 1.2 is **eq. (4)**. Eq. (3) is the same identity for the naive height with `ρ_v = λ_v`, and the product formula is used just before (3) (`Σ_v(([F],[F]))_v = 0`) | AMEND (B2): cite "eq. (3) (naive height) and Def. 1.2, eq. (4)" |
| FRL eq. (7), mutual energy `−∬_{z≠w} log|z−w| dρ dρ′` | §2.4, eq. (7), archimedean | PASS |
| FRL Prop 2.6, archimedean positivity on mass zero, `= ∫dg∧d^cg ≥ 0`, `= 0 ⟺ ρ = 0` | Prop 2.6, eq. (9) | PASS |
| FRL **Lemma 4.8**, non-archimedean positivity | Lemma 4.8 is the **regularization** lemma (`ρ_ε → ρ`; `[F]_ε` has continuous potential). Positivity is **Prop. 4.5**, eq. (23): `(ρ,ρ) = ∫_{H_p} f_ρ² dλ ≥ 0`, `= 0 ⟺ ρ = 0`. The non-archimedean kernel is the Hsia kernel `log sup{S,S′}` (Lemma 4.4, eq. (22)), not `log|x−y|` of a difference | AMEND (B2): replace "Lemma 4.8" by "Prop. 4.5, eq. (23)" everywhere (§0 table row (c), §2.1, §4.2, §6, source list) |
| Poineau Dyn-I, "continuity of the fibrewise family" | Thm A; also Prop. C (global continuous potential `λ_φ` with `Δ(λ_φ|X_y) = χ_y − μ_{φ_y}`) and Cor. D (`y ↦ ⟨μ_{φ_y},μ_{ψ_y}⟩` continuous, the FRL pairing **fibre by fibre**) | PASS, strengthened (§2) |
| `cor:SC1` "∼ 4e^T" | the corollary gives the ten-prime bound. `𝒜_T ∼ 4e^T` is in the text right after it (main.tex l.2135–2137) | AMEND (B13): "the text after `cor:SC1`" |
| P47 Prop 12.4B, Thm 12.4, Restatement 12.4a/12.4a′ | l.2899, 3006, 3020, 3058 | PASS as locations. The use is graded in §6 |
| NG-E1 = MAP_1 l.48 | MAP_1:48: "computed: G_p(0)>0, G_p(π/log p)<0 for p = 2,3,5,7, indefinite" | PASS |
| "Paper 44 … next to Dictionary B.1" | Dictionary B.1 is `R152_001:266`, a phase-152 **proposal** for Paper 44. It is **not** in Paper 44 (grep 0; R157_004 §3 confirms) | AMEND (B11) |

## 2. Doubt 1 — exhaustion of 𝔄: **FAIL as stated; AMEND to 𝔄⁺, and the conclusion survives**

### 2.1 What the literature builds (read this round)

* **Morrow 2507.10410.** It contains **no energy and no quadratic pairing**. The objects are metrics `φ` on line
  bundles over `U^an` (Def 3.1.2), required to be continuous and **norm-equivariant** (Def 3.1.3(2): if
  `|·|_x = |·|_{x_1}^t` then `φ(s(x))_x = t·φ(s(x_1))_{x_1}`), built as limits of **tropical Fubini–Study metrics**
  `m^{-1} max_j(log|s_j| + λ_j)` from global sections `s_j` of `mL` (Def 3.3.1). The measures are Monge–Ampère
  measures defined **fibrewise** (§7.1: "Our goal is to define the Monge–Ampère measure fiberwise": Bedford–Taylor
  at archimedean points, Chambert-Loir–Ducros at non-archimedean ones). The "global Monge–Ampère measure"
  (Def. 8.2.1) is the disintegration `∫_{M(Z)} (∫_{fibre} f · MA_x) dμ(x)` against a probability measure `μ` on
  `M(Z)` **chosen by hand**: arc length on each branch with weight `1/(p log p)` (and `1/e` at ∞), eq. (8.1.0.1),
  chosen only to make the total mass finite. So: fibrewise measures, a base measure with hand weights, and cross-fibre
  data only through (i) continuity in the base, (ii) norm-equivariance along a branch, (iii) global sections `s_j`.
  Nothing couples places beyond the product formula (which enters only through the models). **The energy question
  does not arise, and its measures are in the (a)-by-hand branch.**
* **Poineau Dyn-I 2201.08480.** Energies occur only as the FRL pairing on a single fibre, `⟨μ_{φ_y},μ_{ψ_y}⟩`
  (Cor. D), whose dependence on `y` is continuous. The global objects are a continuous potential `λ_φ` on the whole
  relative line (Prop. C) and continuity of families of fibrewise measures (Def. 3.16), plus "flottant" families
  with `(Φ_ε)_*μ_y = μ_{y^ε}` (Def. 3.17). Poineau notes (§1.1) that the ultrametric analogues of the tools needed in
  higher dimension (Bedford–Taylor, Chern–Levine–Nirenberg) are "largely conjectural". **Fibrewise energy only.**
* **Lemanissier–Poineau 2010.08858.** Foundations: category, topology, cohomology. Fibre products exist in the
  category of `A`-analytic spaces (Thm 4.3.8). No potential theory (grep "potentiel", "énergie", "energy": 0 hits).
* **Chambert-Loir 1001.2517.** Global heights are sums of local heights, and the product formula kills the
  dependence on the chosen section (§3: "since, by the product formula, the second term vanishes"). The one
  **non-local** term in the whole survey is in the arithmetic Hodge index theorem for a curve `X` (§3.4.1,
  Faltings–Hriljac): `(ĉ_1(L)²|X) = −2ĥ_NT([L]) + Σ_v D(f_v)`, with `D(f_v)` local Dirichlet energies (each `≤ 0`)
  and `ĥ_NT` the Néron–Tate height of the Jacobian class. **For genus 0 the global term is 0** (CL's own
  parenthesis), so on `P^1`/`A^1` the energy is a sum of local terms. The global term exists only on curves of
  genus `≥ 1`. That is outside (P152.2), and it is the Hodge-index shape the corpus treated already (P47 Part II,
  the Hodge-index transfer theorem of phase 135).
* **FRL math/0407471.** As R157_005 says, after the citation repairs of §1.

Conclusion from the reading: **no construction in the sources read couples places in an energy beyond the product
formula.** The survey claim (R157_005) is confirmed for Morrow, Poineau Dyn-I, Lemanissier–Poineau, FRL and
Chambert-Loir. Baker–Rumely, Thuillier, Rumely LNM 1378 and Chinburg–Rumely (*The capacity pairing*, Crelle 434)
were **not** read. They remain CITED from standard knowledge. Chinburg–Rumely is the one residual title whose
pairing is, by its name, a global object.

### 2.2 But Lemma 2.2's list is incomplete, so 𝔄 is not exhaustive even canonically

Lemma 2.2 says two points over different base points are related canonically only through the base or through
global sections `σ_α`. **False.** Two further kinds of canonical cross-fibre data exist, and R157_005's own text
uses the first.

1. **Global functions.** Every `P ∈ Z[T]` is evaluated at every point: `x ↦ |P|_x` is a continuous function on all
   of `A^{1,an}_Z`. The simplest case is `ℓ := −log|T|` on `A^{1,an}_Z ∖ {T=0}`. It restricts to R157_005's `ℓ_v` on
   each fibre, and it is what identifies all the local value lines with one line (Lemma 3.2). Then `ℓ(x) − ℓ(y)` is
   defined for **every** pair `(x,y)`, over the same place or not. Kernels `G(x,y) = H(|P_1|_x,…;|P_1|_y,…)`, in
   particular the **norm-line kernels** `H(ℓ(x) − ℓ(y))`, are canonical, compare different fibres, and are not of
   shape (2.1): not supported on the fibre diagonal, not a function of `(π(x),π(y))`, not supported on `Σ × Σ`.
   Morrow's tropical Fubini–Study metrics are built from exactly these evaluations.
2. **The scaling flow along a branch.** `x ↦ x^ε` (the seminorm `|·|_x^ε`) maps the fibre over `|·|_v^{ε′}` to the
   fibre over `|·|_v^{εε′}` (Poineau's `Φ_ε`, Dyn-I Def. 3.17; Morrow's norm-equivariance, Def 3.1.3(2)). It relates
   different base points **on the same branch**. Lemma 6.1's "slice move" `½ → ½ ± a` is this flow.

Also R157_005 calls `M(Z)` "a tree". Poineau (0809.2880, intro) says the topology near the central point is
"strictly coarser than the tree topology". Prop B.3's meet kernel is a function on the tree, so the conclusion is
unaffected, but the word should be "a tree as a set, with a coarser topology at the root" (B4).

### 2.3 The enlarged class 𝔄⁺ is still closed

Let 𝔄⁺ be 𝔄 plus kernels `G_Φ(x,y) = H(Φ(x),Φ(y))`, with `Φ = (|P_j|)_{j∈J}` for finitely many `P_j ∈ Z[T]`, plus
kernels using the flow `Φ_ε` along one branch.

**Lemma B.1 (flow kernels are branch-local; PROVED).** A kernel built from `Φ_ε` couples only points over one
branch, so it keeps the energy a sum over branches (places). It is a per-place term of (4.1), with `𝓔_v` now allowed
to read several slices of branch `v`. *Proof:* `Φ_ε` preserves each branch of `M(Z)`. ∎ (The root is shared, but
it is one base point, which the base term `h` already covers.)

**Lemma B.2 (finitely many global functions see finitely many primes on the skeleton; PROVED, elementary).** Let
`η_{p,ε,r}` be the point of the fibre over `|·|_p^ε` with `|Σ a_iT^i| = max_i |a_i|_p^ε r^i` (Gauss point of radius
`r`, the `G_m`-skeleton point with `ℓ = −log r`). If `p` divides no nonzero coefficient of `P_1,…,P_J`, then
`Φ(η_{p,ε,r}) = (max_{i:a_i^{(j)}≠0} r^i)_j` does not depend on `p` or on `ε`.
*Proof:* `|a|_p = 1` for `p ∤ a`. ∎
So on skeleton-supported measures (the ones R157_005 §4.2 uses), a kernel in `G_Φ` treats all but finitely many
primes identically. Any dependence on `p` at infinitely many primes must enter through the measures `μ_{f,p}` (their
weights: the (a) branch) or through atoms at sections (the `𝓖` term of Thm 4.1, where FRL's only canonical choice
is the product-formula kernel). Finitely many distinguished primes cannot carry the sign (`thm:SC`,
`prop:finsupp`: this is (b′)).

**Lemma B.3 (norm-line kernels are Paper 46's dual problem; RESTATEMENT, one direction PROVED).** Take
`G = H(ℓ(x) − ℓ(y))` and `μ_f` with `ℓ_*μ_f = ν_f`, so that `𝓣(f) = ∬ H(u−u′) dν_f(u) dν̄_f(u′)`. Take `ν_f = f du`
(the only linear choice that does not reintroduce weights by hand). If `𝓣(f) = W_T(f)` on `C_c^∞(I_T)`, then `H`
agrees with the Weil kernel on `|u| < 2T` and is arbitrary on `|u| ≥ 2T`. So `𝓣 ⪰ 0` "by construction" means that
`H` is positive definite, i.e. `Ĥ ≥ 0`, and such an `H` is a certificate of value `≥ 0` in the sense of P46
`def:PD` (with the polar term as in `thm:Z`, `β = (2,0)`). ⟸: weak duality (`prop:weak`), PROVED. ⟹: P46's strong
duality, CITED from P46, with non-attainment allowed, so only in `ε`-form. **This is P46's dual problem (D) written
on `A^{1,an}_Z`. It is not a new object.** The kernel reads only the line `R` with its atoms and weights, so the (a)
schema applies to every derivation of `Ĥ ≥ 0` (`cor:void`, `thm:finmod`(ii)): R157_005's Lemma 5.1 proof covers it
word for word.

**Verdict on doubt 1: FAIL (Lemma 2.2 and "𝔄 exhausts the canonical data") → AMEND.** With 𝔄⁺ the conclusion of
R157_005 stands: every cross-fibre coupling is branch-local (flow), finite-prime (global functions on the skeleton),
the product formula at sections, or a kernel on the norm line, and the last is P46 (D). The literature survey is
confirmed for the five sources read, with the residual Chinburg–Rumely flagged.

## 3. Doubt 6 and Lemma 2.1 — the fibre product: **AMEND (the needed content is correct)**

The open question: "`A^{2,an}_Z` is the fibre product over `M(Z)` since the restriction to `Z` of a multiplicative
seminorm on `Z[T_1,T_2]` is a point of `M(Z)`". That argument proves less than it claims.

* **What it proves.** For every point `z` of `A^{2,an}_Z`, the two projections `pr_1(z), pr_2(z)` (restrictions of
  `|·|_z` to `Z[T_1]`, `Z[T_2]`) have the same restriction to `Z`. So they lie over one point of `M(Z)`. The
  addition `m^*: T ↦ T_1 + T_2` is a `Z`-algebra map, so `m` commutes with `π`. **Correct, and it is all that
  R157_005 uses.**
* **What it does not prove.** `A^{2,an}_Z = A^{1,an}_Z ×_{M(Z)} A^{1,an}_Z` holds in the **category** of `Z`-analytic
  spaces (the affine case by definition; in general Lemanissier–Poineau Thm 4.3.8). It is **false as sets**: the map
  `|A^{2,an}_Z| → |A^{1,an}_Z| ×_{|M(Z)|} |A^{1,an}_Z|` is surjective and not injective.
  - Archimedean fibre: over `|·|_∞` the fibre of `A^{2,an}_Z` is `C²/conj` (Poineau 0809.2880, intro: "`C^n`
    quotienté par l'action de la conjugaison complexe"), while `(C/conj) × (C/conj)` has the two points `(z,w)`,
    `(z,w̄)` of `C²/conj` over each generic pair.
  - p-adic fibre: over (Gauss point, Gauss point) lie both the Gauss norm of the bidisc (`|T_1 − T_2| = 1`) and the
    seminorm `P ↦ |P(T,T)|_{Gauss}` (`|T_1 − T_2| = 0`).
* **Consequence for "a translation-invariant kernel only compares points over the same place": TRUE, with a
  repair.** The difference `x − y` is a map on `A^{2,an}_Z`, not on pairs of points. Even over one fibre it is
  multivalued on pairs: two values on `C/conj`, and a whole segment of values over a pair of type-II points. A
  "difference kernel `k_s(x−y)`" on pairs therefore has to be a symmetrization or a choice: the sum over the two
  lifts on `C/conj`, the Hsia kernel `sup{S,S′}` of FRL Lemma 4.4 in the non-archimedean fibres, or `k(ℓ(x)−ℓ(y))`
  through the multiplicative skeleton, which is well defined because `|T_1T_2|_z = |T|_{pr_1 z}|T|_{pr_2 z}`. Every
  such choice is supported on `{π(x) = π(y)}` **except** the last. The last is the norm-line kernel of §2.3, and it
  comes from the multiplicative law read through the global function `ℓ`, not from the additive law.

Verdict: Lemma 2.1 **AMEND (B3)**. State it as: "every point of `A^{2,an}_Z` lies over a single point of `M(Z)`, and
`m` is a morphism over `M(Z)`; the fibre product is categorical, not set-theoretic". The fibre description of (2.0)
is confirmed from Poineau 0809.2880 (archimedean fibres `C^n/conj`, `p`-adic fibres Berkovich spaces, branches meeting
at the trivial norm). Doubt 6: PASS after (B3).

## 4. Doubt 2 — Lemma 3.3: **PASS (with a simplification)**

Checked against P46 conventions. `eq:A`: `𝔞_T(F) = C_0‖F‖² + ∫(‖F‖² − c_F(u))K du − Σ_{n∈N_T} v_n c_F(log n)`,
`v_n = 2Λ(n)/√n`. So the prime-`p` part is `Q_p(F) = −Σ_{k: k log p < 2T} v_{p^k} c_F(k log p)`. This is the same
sign as `thm:finmod`(ii)'s `−(2c/√n_0)c_F(log n_0)`, with `v_{p^k} = 2 log p·p^{−k/2}` and the symbol
`σ_p = −Σ_k v_{p^k} cos(kτ log p)`. The truncation is automatic: `c_F(u) = 0` for `|u| ≥ 2T` when `supp F ⊂ I_T`.
`W_T = 𝔞_T + 2Re(A B̄)`, and the polar term is assigned to `Q_∞`, which is consistent with `eq:W`.

The construction: `J = (−T,−T+ℓ)`, `ℓ < min(u_0, 2T−u_0)`, `u_0 = log p`. Then `J + u_0 ⊂ I_T` because
`−T + ℓ + u_0 < T`. For `F_φ = φ + φ(·−u_0)` the translate `F_φ(·−ku_0)` is supported in
`(J+ku_0) ∪ (J+(k+1)u_0)`, which misses `J ∪ (J+u_0)` for `k ≥ 2` because `(k−1)u_0 ≥ u_0 > ℓ`. So
`c_{F_φ}(ku_0) = 0` for `k ≥ 2`, and `c_{F_φ}(u_0) = ⟨φ(·−u_0), φ(·−u_0)⟩ = ‖φ‖²`. Signs verified:
`Q_p(F_φ) = −v_p‖φ‖² < 0`.

Two simplifications (not errors):
1. The fourth translate `J + 3u_0` is unnecessary: `ℓ < u_0` already makes all translates `J + ku_0` pairwise
   disjoint.
2. The disjoint-support family is unnecessary. `φ ↦ F_φ` is linear and injective, and `Q_p(F_φ) = −v_p‖φ‖²` for
   **every** `φ ∈ C_c^∞(J)`. So `Q_p` is negative definite on the **infinite-dimensional** subspace
   `{F_φ : φ ∈ C_c^∞(J)}`. Its intersection with `P_T` has codimension `≤ 2`, so it is still infinite-dimensional
   (exactly as in `lem:cpos`'s last sentence).

So Lemma 3.3 holds in the stronger form "negative definite on an infinite-dimensional subspace of
`P_T ∩ C_c^∞(I_T)`, for every `p` and every `T > ½ log p`". This turns NG-E1 (computed at `p ≤ 7`, MAP_1:48) into a
PROVED statement for all `p` in the window setting. (On `L²(R)`, indefiniteness is immediate from `σ_p(0) < 0 <
σ_p(π/log p)`. The window version is the new content.) Label PROVED. Amendment (B5) records the simplification.

Under (b′) (R157_004 A20) Lemma 3.3 is **corroboration**, not the exclusion: indefinite summands do not forbid a
positive sum (`W_T = 𝒜_∞ + Π_T` with both indefinite). It shows that no argument can infer the sign from a single
`Q_p`. The finite-`S` version is `thm:SC`/`prop:finsupp`.

## 5. Lemma 3.1 and Lemma 3.2: **PASS** (3.2: AMEND, normalization)

* **3.1(i)** `−log|m|_p = ord_p(m) log p = Σ_{k≥1} log p·1[p^k|m]`: correct.
* **3.1(ii)** Summing (i) over `p` gives `Σ_{d|m} Λ(d) = −Σ_p log|m|_p`. The product formula
  `log|m|_∞ = −Σ_p log|m|_p` then gives `log|m| = Σ_{d|m}Λ(d)`. Both are consequences of unique factorization, and
  given (i) each is equivalent to the other. "Is the identity" should be read as "is equivalent to, given (i)".
  PASS.
* **3.1(iii)** For additive `φ` (`φ(1) = 0`), `(μ∗φ)(n) = φ(q^j) − φ(q^{j−1})` if `n = q^j`, and `0` otherwise.
  For `φ = log p·ord_p` this gives `log p·1[n` a power of `p]`. So `Λ = Σ_p μ∗(−log|·|_p)`, and this also follows
  from `μ∗log = Λ` and (ii). Correct. It is **classical** (`Λ = μ∗log` split by primes) and must be labelled
  RESTATEMENT, classical, with no novelty claim.
* **3.2** Correct at the points `ε = 1` (`|·|_v` unrescaled). On the fibre over `|·|_v^ε`, `ℓ_v` scales by `ε`, and
  the product formula holds only for the normalized absolute values. Say "at `ε_v = 1` for every `v`" (B6). "Both
  equal `k log p`" means in absolute value. PASS after (B6).

## 6. Clause-by-clause re-grading under the amended lemma

### 6.1 (b′): do Theorem 4.1's two cases establish exclusion? **No. They establish that the construction
reproduces `W` without an independent positivity input. That is a RESTATEMENT, not an exclusion.**

* **Case 1** ("`𝓔_{s_v}(μ_{f,v}) = Q_v(f)`": the explicit formula written on the skeleta). By R157_004 A20, a
  per-place decomposition is not an exclusion criterion, because `W` itself is `Σ_v Q_v`. Case 1 infers no sign. It
  is the identity `W = Σ_v Q_v` transported to `A^{1,an}_Z`. (b′) does not fire (nothing is inferred), and nothing
  needs to fire: the case contains no positivity mechanism, and its positivity question is `λ^W_T ≥ 0` itself. So
  R157_005's "**Excluded** (NG-E1; `thm:SC` …)" in §4.2 case 1 is **FAIL as a reason**. The correct label is
  RESTATEMENT (identity), and it is not a survivor because it supplies no sign input. (B7)
* **Case 2** (termwise-positive local energies with a redistribution). Here `𝓔 ⪰ 0` **is** inferred place by place
  (FRL Prop 2.6 / Prop 4.5, tree kernels). But `𝓔 ≠ W`: `W = 𝓔_P − A_P` with a nonnegative scalar load. So the
  positivity of `W` is **not** inferred from local positivity. (b′) fires only on the inference "`𝓔_v ⪰ 0 ∀v ⟹ W ⪰ 0`",
  which would be the false step. What remains is the global inequality `𝓔_P ≥ A_P` on the primitive space (D.195
  (3.5)), which is `RD_T` (§7). So case 2 is **excluded as a mechanism by (b′)** in the precise sense "local
  positivity does not give the sign". As a construction it reduces to a **RESTATEMENT of `RD_T`**, not to an
  impossibility. (B7)
* **The new 𝔄⁺ branches** (§2.3): flow kernels are per-branch (case 1 or 2 again); finite global functions are
  finite-`S` (b′, `thm:SC`); norm-line kernels are P46 (D), a RESTATEMENT, whose "positive by construction" variant
  falls to the (a) schema.

### 6.2 (a) amended (derivations): **PASS after rewording**

Lemma 5.1 is the factorization through the atom list `{(q, k log q)}` with weights that R157_004 A23 asked the test
to decide. It **is** decided: in the weights-by-hand branch the geometry of `A^{1,an}_Z` is decorative, and every
derivation of `𝓔 ⪰ 0` from data common to an amplification-closed class is excluded by `cor:void` +
`thm:finmod`(ii) (PROVED, unconditional). The sentence after Lemma 5.1 is already phrased as a statement about
derivations. T3 must be demoted: by A19 it needs a bridge "`𝓔_𝒫 ⪰ 0 ⟹ (ZFS_δ)`" that does not exist for DMV, so
"T3 modulo (H-DMV)" should read "T3 supplementary, and inapplicable without the bridge" (B8).

**Doubt 4 (exhaustiveness of the §5 split).** "By hand" versus "produced by the fibre geometry" is a dichotomy only
once "geometric" is defined: weights that are values of canonical functions on `A^{1,an}_Z` (Green kernels,
evaluations at points of `M(Z)` or of fibres). With that definition it is exhaustive by construction. Two remarks.
(i) R157_005's "a construction placing mass elsewhere and recovering `W` by a non-local identity is covered by (b)"
relied on the old (b). Under (b′) such a construction is either an identity (RESTATEMENT) or infers the sign
locally or from finite `S` (excluded). (ii) The geometric branch analysed only Green levels and the slice. A
derivation that uses the **single** slice `{½}` (not model-uniform over `Ξ_a`, whose slice is `{½ − a, ½ + a}`)
escapes (c). It does not escape Theorem 4.1: its energy is still in case 1 or case 2, so it reduces to the same
restatement. **Exhaustive after (B9), with the escape named and closed by Thm 4.1, not by (c).**

### 6.3 (c) amended (Prop 12.4B + Hardy, schema): **AMEND. One sentence uses (c) on a function (doubt 5)**

* The main use (R157_005) is correct as a schema: "if the identity `𝓔 = W` were **derived** from the explicit formula
  and the geometry, the derivation would read verbatim for `Ξ_a` …". This excludes derivations and matches
  Restatement 12.4a and A21. Two repairs. (1) The contradiction is with **Prop 12.4B** (negativity on a
  `Ξ_a`-primitive test) together with Hardy (X16), not with Thm 12.4, which is about `h⁰_a` in the intersection frame
  (A21). (2) `Ξ_a`-primitivity is **four** conditions (P47 Lemma 12.4A, rank-4 `Π_P`), not `P_T`. The transferred
  positivity must hold on a class containing the `Ξ_a`-primitive tests. It does whenever it holds on a
  mass-zero/degree-zero class cut by the polar data of `Ξ_a`, but this must be said. (B10)
* "`𝓔_{Ξ_a} ⪰ 0` PROVED for this branch". The function statement is true, but by A21 it shows only that **the
  identity fails for `Ξ_a`**. It kills the candidate only in conjunction with a model-uniform derivation of the
  identity for ζ. The §0 table's "⇒ excluded" must read "⇒ model-uniform derivations excluded". (B10)
* **The slip (doubt 5, FAIL).** §6 first bullet: "A function `𝓔` that equals `W_ζ` by an argument inspecting `ζ`
  beyond the space is not excluded by (c), but then its positivity is not structural, and it falls under §4.2
  case 1." This is wrong. Such an `𝓔` is termwise positive **by hypothesis** (it is in the structural branch). What
  is non-uniform is the **identity** `𝓔 = W_ζ`. It falls under **case 2**, where it is not excluded: the identity plus
  termwise positivity would prove `RD_T`, i.e. it is exactly D.195 (3.5) with the gap closed. Filing it under case 1
  (no sign) disposes of a function by reclassification. That is the use of (c) against a function that Remark
  12.4a′ forbids. (B10)
* Lemma 6.1: PASS. `−Ξ_a′/Ξ_a = −ξ′/ξ(s+a) − ξ′/ξ(s−a)`, whose prime part is `Σ Λ(n)(n^{−a} + n^{a})n^{−s}`. At
  `s = ½ + iτ` the weight is `Λ(p^k)(p^{−k(½−a)} + p^{−k(½+a)}) = log p(|p^k|_p^{½−a} + |p^k|_p^{½+a})`. The
  "evaluation at `ε`" reading is a tautological rewriting of `p^{−kε}`. So the identity is PROVED, and "the space
  cannot distinguish ζ from `Ξ_a`" is a dictionary sentence (RESTATEMENT). Note also that the `Ξ_a` comb weights
  `∼ n^{a−½}Λ(n)` grow relative to ζ's, so "the same branches" does not mean "the same measure".

### 6.4 (d), missing from R157_005: **added (B12)**

Poineau Dyn-I and Lemanissier–Poineau work over rings of integers `O_K` (Dyn-I abstract; LP scope). Lemma 2.1,
Theorem 4.1 (in 𝔄⁺) and Lemmas B.1–B.3 hold verbatim over `M(O_K)`, with one branch per place of `K`. So any
positivity derivation on `A^{1,an}_{O_K}` is field-uniform, and by T1 it would have to prove GRH for every `ζ_K`.
That is a standard, not an exclusion. For Epstein (`Ξ_Q`, T2) the question is whether a derivation uses only A1–A6,
A2⁺ and `𝔇`. **No positivity derivation is proposed**, so (d) has nothing to act on. The Pass clause (A3 plus one of
A7/A8/A9 invoked) is not met, trivially, because no derivation exists.

## 7. Doubt 3 — D.195 (3.5) against Paper 46 definitions: **PASS as a restatement, with two conventions fixed**

Re-derivation. P46: the operator of `𝔞_T` is `G_Γ − m_0 − Σ_{n∈N_T} w_n(S_{log n} + S_{−log n})`,
`w_n = Λ(n)/√n`, with `m_0 = −C_0 = log π − ψ(¼) > 0`, and `G_Γ − m_0` has multiplier `m(τ) = C_0 + Lev`. D.195
(2.3): `log p·(A_p^*A_p − I) = log p Σ_{k≠0} p^{−|k|/2} S_{k log p}`, i.e. the full `p`-part `Σ_k w_{p^k}(S + S^{−1})`.
With (3.1), `A_p^*A_p − I = (c_p − 1)I − c_p(I − M_p)`, the Weil operator is

    G_Γ − m_0 − Σ_p log p[(c_p−1) − c_p(I − M_p)] = 𝓔_P − A_P·I ,

with `𝓔_P = L_∞ + Σ_p log p·c_p(I − M_p)` and `A_P = m_0 + Σ_p log p(c_p − 1)`. So:

1. **Sign convention.** D.195's `B_P = A_P I − 𝓔_P` is **minus** the Weil form, and (3.5) `𝓔_P ≥ A_P` on
   `ker M_+ ∩ ker M_−` says `𝔞_T ≥ 0` on the primitive space. Consistent. (`M_±` are the two Tate moments, P46's
   `A, B`.)
2. **Window convention.** (3.5) is a window statement only after compression to `L²(I_T)`. D.195 §3 says so ("primes
   whose displacement exceeds the window cancel internally between the two terms of (3.1)"). Indeed, for
   `log p ≥ 2T`, `P_T[(c_p − 1) − c_p(I − P_TM_pP_T)]P_T = P_T(c_pM_p − I)P_T = 0` on `L²(I_T)`. With
   `P ⊇ {p < e^{2T}}`, the compressed (3.5) on `P_T` **is** `RD_T` (`λ^A_T ≥ 0`), and "∀T" is RH by P46 l.141–144.
   D.195 §5 records that the compression breaks the Markov/CP structure. That does not affect the identity. So
   "(3.5) equivalent to row D" is **correct as a restatement** under P46's definitions (primitive form).

**The scale match (R157_005's doubt 3, "heuristic").** It can be sharpened to an identity:

    A_P − m_0 = Σ_{p∈P} log p·2r_p/(1−r_p) = Σ_{p∈P} Σ_{k≥1} 2 log p·p^{−k/2} = Σ_{p∈P, k≥1} v_{p^k}     (PROVED)

So `A_P + C_0` is the **untruncated** comb mass over `P`. With `P = {p < e^{2T}}`,
`A_P + C_0 − 𝒜_T = Σ_{p<e^{2T}, p^k ≥ e^{2T}} v_{p^k} = O(T)` (Chebyshev bounds: the `k = 2` terms with
`e^T < p < e^{2T}` give `Σ 2 log p/p ∼ 2T`, and the rest is `O(1)`). So `A_P = 𝒜_T + O(T) ∼ 4e^T`
(PROVED, modulo Chebyshev/PNT for the asymptotic). What stays **HEURISTIC** is the *interpretation*: that this
constant plays the role of a capacity threshold in the sense of `thm:SC`'s mass condition `A < −C_0`. The
labelling is right in spirit. (B7)

## 8. §4.3 (the global constraint): **AMEND labels**

(i) and (ii) are identities: RESTATEMENT, as labelled. (iii): `P_T = {A = B = 0}` is cut out by the moments against
`e^{±t/2}`, i.e. by the **polar** data (the pole of ζ), not by "archimedean data alone". It is independent of the
prime weights, which is what the argument needs. `thm:SC` is stated on `P_T` (checked), so the PROVED claim "the
restriction to `P_T` does not by itself produce positivity" stands. The paragraph "on `f` the product formula has no
content beyond (i)" is an argument about what a test function is, not a theorem: HEURISTIC. For `Ξ_a` the constraint
has four conditions (Lemma 12.4A). (B8)

## 9. Theorem 4.1: **AMEND (B6)**

* "absolutely continuous in the fibres (as they must be for `f ∈ C_c^∞`)". Nothing forces this, and the measures
  §4.2 actually uses are on the `G_m`-skeleton (type II/III points), which is not absolute continuity for any
  natural fibre measure. The hypothesis needed is **no atoms on `Σ`** (`Σ` is countable, and section values are type
  I points, so skeleton measures qualify). Replace, and drop "as they must be".
* Add the fourth term `𝓣` of §2.3 (global-function and norm-line kernels) and the flow kernels. The theorem is then
  stated for 𝔄⁺, with Lemmas B.1–B.3.
* The "difference kernel `k_s(x−y)`" in (2.1) must be read with the repair of §3 (symmetrization on `C/conj`, the Hsia
  kernel non-archimedean).

With these, Theorem 4.1 is PROVED within 𝔄⁺. Its content is: **every energy in 𝔄⁺ that reproduces `W` is the
explicit formula (case 1), a termwise-positive energy minus the load `A_P` (case 2, = D.195 (3.5) = `RD_T`), a
finite-prime form (`thm:SC`), or a norm-line kernel (P46 (D)).** That is a classification by restatement.

## 10. Verdict table

| item | verdict | label after audit |
|---|---|---|
| §1 corpus grep | PASS | — |
| (2.0) fibre description | PASS (verified from Poineau 0809.2880) | CITED |
| §2.1 FRL citations | AMEND (B2): Def 1.2 = eq. (4); non-arch positivity = Prop 4.5 eq. (23), not Lemma 4.8 | CITED (checked) |
| §2.1 Morrow, Poineau Dyn-I | AMEND (B2): read beyond abstract; fibrewise measures, hand base measure, no energy | CITED (checked) |
| Lemma 2.1 | AMEND (B3): categorical, not set-theoretic, fibre product; the needed content is correct | PROVED |
| Lemma 2.2 | **FAIL** as stated (B4): global functions and the scaling flow are omitted | replaced by §2.2 list; exhaustion over 𝔄⁺ = CITED/HEURISTIC (Chinburg–Rumely unread) |
| Lemma 3.1 (i)–(iii) | PASS; (iii) classical | PROVED (elementary); RESTATEMENT |
| Lemma 3.2 | AMEND (B6): `ε_v = 1` normalization | PROVED |
| Lemma 3.3 | PASS; stronger form (infinite-dim subspace of `P_T`), `J+3u_0` superfluous (B5) | PROVED; NG-E1 now PROVED for all `p` |
| Theorem 4.1 | AMEND (B6): no atoms on `Σ`; add 𝔄⁺ terms | PROVED within 𝔄⁺ |
| §4.2 case 1 "Excluded" | **FAIL as a reason** (B7): identity, no sign inferred | RESTATEMENT |
| §4.2 case 2 | AMEND (B7): (b′) excludes the local inference; the construction reduces to `RD_T` | RESTATEMENT (D.195 (3.5) ≡ `RD_T`, re-audited PASS) |
| `A_P ∼ 4e^T` | upgraded (B7): `A_P + C_0 = Σ_{p∈P,k≥1} v_{p^k}` exactly; `= 𝒜_T + O(T)` | PROVED; capacity reading HEURISTIC |
| §4.3 | AMEND (B8): (iii) is polar, not archimedean; last paragraph HEURISTIC | PROVED for (iii) |
| Lemma 5.1 and (a) | PASS in derivation form; T3 demoted (B8) | PROVED (factorization); exclusion of derivations PROVED via `cor:void` |
| §5 case split (doubt 4) | AMEND (B9): exhaustive once "geometric" is defined; single-slice escape closed by Thm 4.1 | — |
| Lemma 6.1 | PASS | PROVED (identity); "cannot distinguish" = RESTATEMENT |
| §6 (c) use | AMEND (B10): Prop 12.4B + Hardy, four-condition primitivity; **FAIL** of the "falls under case 1" sentence (function excluded by reclassification) | RESTATEMENT (schema) |
| (d) | added (B12): field-uniform ⇒ T1 standard; no derivation, so no pass | — |
| §0/§7 final verdict "EXCLUDED, by clause (b)" | **FAIL as worded** (B1) | see §11 |

## 11. Final verdict on (P152.2)

**(P152.2) is CLOSED: no survivor. Its category is EQUIV (restatement), not EXCL-by-(b).** Under the amended Lemma
P157.S1:

* no realization in 𝔄⁺ supplies an independent positivity input. Every realization that reproduces `W` is the
  explicit formula on the skeleta, D.195 (3.5) (≡ `RD_T`, re-audited against P46), a finite-prime form, or P46's dual
  problem (D) on the norm line (Theorem 4.1 amended, Lemmas B.1–B.3);
* the positivity **mechanisms** it could offer are each excluded: local or finite-`S` inference by (b′)
  (`thm:SC`, `prop:finsupp`, with Lemma 3.3 now PROVED as corroboration); "positive by construction" with
  weights on the atom list by the (a) schema (`cor:void` + `thm:finmod`(ii), PROVED); model-uniform structural
  derivations by the (c) schema (Prop 12.4B + Hardy);
* (d) is not reached, because no derivation exists; the Pass clause fails trivially.

The survival condition's naming requirement was met: the coupling is the global function `ℓ = −log|T|` together
with the product formula at sections. What it produces is `W`'s own place decomposition, or `W` on the norm line.
Neither is a sign. **The bibliographic residual is narrower than R157_005 said.** Morrow, Poineau Dyn-I and
Lemanissier–Poineau were read and contain no cross-place energy. The one unread title with a global pairing is
Chinburg–Rumely, *The capacity pairing* (Crelle 434, 1993). The known genuinely global energy term (Néron–Tate, CL
§3.4.1) vanishes in genus 0 and lives outside (P152.2).

Consistent with option (A) of the reduced statement: the phase-157 search has no formulated survivor. The MW-5
cluster (#37) remains "not excluded, no object" per R157_004.

## 12. Clearance

| item | cleared? | where | condition |
|---|---|---|---|
| Lemma 2.1 (amended B3) | **yes** | Paper 47 Part IV, one remark in the (P152.2) closing paragraph (why Prop B.3's conclusion extends from `M(Z)` to `A^{1,an}_Z`) | state the categorical fibre product, and that `x − y` is a map on `A^{2,an}_Z` |
| Lemma 3.1(iii) | **conditional** | Paper 44, but only **together with** Dictionary B.1 (R152_001:266), which is itself not in Paper 44 | decide on Dictionary B.1 first. Label: classical (`Λ = μ∗log` split by primes), RESTATEMENT, no novelty |
| Lemma 3.3 (stronger form) | **yes** (not proposed in R157_005) | Paper 46 as a one-line corollary of `lem:cpos`, or P47 as the proved form of NG-E1 | P46 is in R2 revision: to be decided. Label PROVED |
| Theorem 4.1 (amended B6, with Lemmas B.1–B.3) | **yes, as a restatement** | Paper 47 Part IV, the (P152.2) paragraph | label "PROVED within 𝔄⁺; exhaustion of the literature CITED (five sources read; Chinburg–Rumely unread)"; must not be phrased as an impossibility theorem |
| Lemma 6.1 | **yes** | Paper 47, next to Thm 12.4 / Prop 12.4B, as a dictionary remark | label: identity PROVED, reading RESTATEMENT |
| D.195 (3.5) ≡ `RD_T` (re-audit, §7) | **yes, as a record note** | Paper 47 (where phase-114 material is cited), with the two conventions of §7 | — |
| Lemma B.3 (norm-line kernels = P46 (D)) | optional | Paper 46 remark after `thm:Z` | to be decided; P46 under revision |

## 13. Closing paragraph

The test of the Berkovich line over Z (R157_005) holds up in substance, but its headline was wrong. The energy does
split into per-place pieces. Weil's own formula also splits that way, so splitting by itself proves nothing, and
the parallel audit had already ruled so. What the round actually shows is that every energy one can build on this
space either rewrites the explicit formula, or rewrites Paper 46's dual problem, or moves the whole question into a
capacity inequality that is exactly row D at each window. None of these supplies a sign from outside. The positivity
arguments one might try on top of them (place by place, from a few primes, from weights put in by hand, or by a
construction that works equally for the falsifier `Ξ_a`) are each ruled out by theorems already proved.
I read the recent global Berkovich papers (Morrow; Poineau; Lemanissier–Poineau; Chambert-Loir's survey). They
build measures fibre by fibre and never couple places in an energy, so the survey claim holds for them.
There is one gap in the list (R157_005) of how two different places can be related: through global polynomial
functions, including the logarithm of the norm, which is what puts all primes on one line. Closing it leads back to
Paper 46's dual problem. The candidate is closed, as a restatement rather than an exclusion. One per-prime lemma
comes out stronger than stated: each prime's local piece of the Weil form is negative on an infinite-dimensional
space of admissible tests, at every window. That turns an old computed no-go into a theorem. No sign is claimed or
suggested for ζ at any window, in either form.
