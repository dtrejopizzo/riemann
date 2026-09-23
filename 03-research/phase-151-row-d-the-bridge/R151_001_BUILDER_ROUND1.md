# R151.001 — Builder round 1: T6, the bridge theorem, and the classification of positivity mechanisms

*Builder: Opus 5, 2026-09-19, phase 151. Written against
`R151_000_LEAD_BLUEPRINT.md` §3. Circuit: builder → hostile audit → repairs → lead decision.
**FATAL rule in force: nothing below proves, asserts, claims or suggests a new zero-free region, a new
moment bound, or a new cancellation estimate. No sign is claimed. Row D receives no label here.***

---

## 0. Summary

**What is proved.** T6 (Theorem 2.7) says: in any family of "fibre sums" over `Z` in which the fibres
enter **additively with nonnegative weights**, the Mellin transform of the family moment `M_{2k}(N)` is
the Laplace transform of a nonnegative measure, and its abscissa of convergence is bounded **below** by
`2k β_max`, where `β_max = sup Re ρ`. Consequently:

* any a priori bound `M_{2k}(N) ≪ N^{a_k+ε}` gives `β_max ≤ a_k/2k` — so supplying the exponent is
  supplying the zero bound, at every level `k` and for every family type;
* no cancellation between fibres removes the fibre's singularity, because the fibre enters as a
  nonnegative summand and abscissae of nonnegative Laplace transforms take the **maximum**, not a
  cancelling combination;
* the one ingredient of Deligne's argument with no nonnegative-additive counterpart over `Z` is
  **rationality**, whose whole role is to place the fibre's singularities *outside* the region of
  convergence of the family's generating function — which over `Z` is impossible by the previous point.

**What is new, and what is not.** The forward half of T6(ii) is, honestly, **a restatement** of
Theorem 26.4 (the extraction, a Hölder inequality) chained with Corollary 27.10a (von Koch–Landau).
T6(iii) is trivial once stated. What T6 adds is:

1. an **`L²`-abscissa lemma** (Lemma 2.2): for the smoothed Chebyshev remainder, the abscissa of
   *mean-square* convergence equals `β_max` exactly. This is strictly sharper than the `L^∞` statement
   of Theorem 27.10 and it is what makes the argument survive at `k ≥ 2` (Lemma 2.4);
2. the **converse/optimality half** of T6(ii): no `a_k < 2kβ_max` is possible, so the hypothesis is not
   merely sufficient but *calibrated*;
3. **Corollary 3.2**, which recovers `H(2,c) ⟹` a zero-free strip **without** the off-diagonal
   hypothesis (26.9a) of Corollary 26.19 and **without** Granville's equivalence. This is the one place
   where T6 buys something the corpus did not already have;
4. **T6(iv)** (Theorem 2.9), the exact statement of what rationality does, as a theorem about abscissae
   rather than the slogan "one object is both a square and has an a priori polar divisor" of
   Theorem 26.17.

**Correction to the blueprint.** The blueprint proposed to obtain `σ_c(k) ≥ 2kβ_max` from *Landau's
oscillation theorem* ("`|ψ_w(N) − Nŵ(0)| ≥ N^{β_max−ε}` along a sequence"). **That route does not
prove the stated inequality.** An `Ω`-result along a sequence gives spikes on a set of measure zero;
spreading them by the derivative bound `|S'(N)| ≪_w 1` yields only
`σ_c(k) ≥ (2k+1)β_max − 1`, which is **weaker** than `2kβ_max` whenever `β_max < 1`. The repair is to
replace the oscillation theorem by **Mellin–Plancherel** (Lemma 2.2), which is available precisely
because the weight is smooth. The oscillation theorem is retained only where it belongs: the `Ξ_a`
gate (§5.1), exactly as in Proposition 26.21(1).

**Weakest point.** Lemma 2.2's lower half needs `W(ρ) ≠ 0` at zeros of near-maximal real part, and the
only device proved here to secure it is the `θ`-family `w_θ(u) = w(u)u^θ` of Corollary 26.5. So T6(ii)
is stated for a *family of weights*, not for one weight. Nothing weaker is proved.

---

## 1. Corpus check

Per the owner's standing rule (`feedback-check-corpus-first`), every ingredient was grepped before
being written. Commands run from the repository root.

| # | command | result | consequence for this round |
|---|---|---|---|
| 1 | `grep -rniE "Pringsheim" --include=*.md 03-research 04-papers 05-meta-and-planning` | 7 hits: `phase-103/103_16_EXPONENTIAL_COORDINATE_PRINGSHEIM_NO_GO.md` (elementary Pringsheim lemma, used to *refute* a sufficient condition for Li positivity); `phase-104/104_19`, `104_25`, `104_95` (Pringsheim forcing a singularity, three separate gates); `phase-29/17` (Śleszyński–Pringsheim, continued fractions — unrelated) | Pringsheim is **already** a corpus tool, used three times to force a singularity. T6's use is the same device; **no novelty is claimed for it** |
| 2 | `grep -rn "Landau's theorem for Laplace transforms" --include=*.md 03-research` | 2 hits: `phase-138/R138_001_BUILDER_ROUND1.md:762` and `phase-139/R139_001_BUILDER_ROUND1.md:478`, both citing *Widder, The Laplace Transform, Theorem II.5b* | the exact statement and reference of record already exist in the corpus; §2.1 **reuses them verbatim** rather than re-importing |
| 3 | `grep -rniE "abscissa" --include=*.md 03-research` | ~20 hits, concentrated in phases 137–139 (`R138_001` §D.17.2, `R139_001` §D.19.3a′, `R139_003` H3). Phase 14 `ANCHOR-framework-a-classification-of-zero-absence.md` is flagged in `R138_001:1144` as "**already the corpus's organizing frame**: an anchor is a Landau singularity" | the abscissa/Landau frame is **not new**. What is new in T6 is the **direction**: phases 14/138/139 use it on the *multiplicative* square (`G(z) = 2z^{−2}(ξ'/ξ)(½+z)`, where exponents *subtract*, Theorem 26.15); T6 uses it on a **nonnegative family moment**, where the corpus's own Theorem 26.15 says Landau is *useless* — and T6 explains why, and what survives |
| 4 | `grep -rniE "mean square\|Cramér" --include=*.md 03-research 04-papers` | hits in `phase-55/173-representacion-de-I.md` (Cramér's `V(t) = Σ e^{iρt}`, singularity structure) and `phase-58/191` (Balasubramanian–Conrey–Heath-Brown mean square of `ζ ×` Dirichlet polynomial). **No hit** for the mean-square abscissa identity `σ_2 = β_max` | **Lemma 2.2 is not in the corpus.** It is classical in substance (Mellin–Plancherel + the smoothed explicit formula) and is labelled `CLASSICAL, PROVED` here, not claimed |
| 5 | `grep -rniE "max.*abscissa" --include=*.md 03-research` | 1 hit, unrelated (`R138_001:972`, `θ = max_p\|p−½\|`) | Lemma 2.5 (abscissa of a sum = maximum) is not in the corpus; it is elementary and labelled as such |
| 6 | `grep -rn "Theorem 22.17\|Theorem 19.25\|Theorem 21.15" 04-papers/46-row-d-the-sign/main.md` | `22.17` at line 9847 (`Spec Z` terminal, no ring of Frobenius correspondences), `19.25` at 6332 (frame defect), `21.15` at 8796 (frame defect on the curve) | the three theorem numbers used in §4 to close mechanisms (β) and (γ) exist and say what §4 says they say |
| 7 | `grep -rn "MW-5\|CAND-1" --include=*.md 03-research 05-meta-and-planning` | ~15 hits: `phase-63-lefschetz-realization` (R1/R3/R6 verdicts, "no `J`-linear Frobenius isometry of a gapped polarization on the `ζ` window — this is MW-5"), `phase-62` (gapless `V₊` positivity), `phase-66` (rank-one escape, face (B) = MW-5), `phase-71` (CAND-1/CCM, 17-step reduction), `phase-136/MAP_3` rows 62, 63, 66, 71, `phase-138/README` (Hilbert–Pólya = MW-4, NG-E5, **closed, not to be reopened**) | §4's paragraph on mechanism (α) is written **from these records** and reopens nothing. NG-E5 (Hilbert–Pólya "for free" via OS reconstruction) is `RETRACTED` in the corpus and stays retracted |
| 8 | `grep -rn "nonnegative measure" --include=*.md 03-research 04-papers` | `main.md:8912` ("the frame's cone is a **moment cone** — the image of the nonnegative measures"), `R149_001:707` (the `RESTATEMENT` warning: "positivity that is free, being the autocorrelation of a nonnegative measure"), `phase-145/R145_001:657`, `phase-147/R147_001:95,104` | **the corpus has met "nonnegative by construction" four times and labelled it `RESTATEMENT` each time** (Warning to Theorem 26.12). T6 is the fifth instance and is labelled accordingly wherever its positivity is free; the parts that are *not* free are §2.2 and §2.4 |

**Corpus verdict.** Nothing in T6 reopens a closed route. The one genuinely new mathematical statement
is Lemma 2.2 (`CLASSICAL` in substance) and the one genuinely new consequence is Corollary 3.2. The
rest is a sharpening of Theorems 26.4, 26.15, 26.17, 27.3 and 27.10 into a single statement.

---

## 2. T6 — the bridge theorem

### 2.0 Setting

Fix `w ∈ C_c^∞(0,∞)`, `supp w ⊆ [1,2]`, `w ≥ 0`, `w ≢ 0`; write
`W(s) := ∫_0^∞ w(u)u^{s−1}du` (entire, of order `1`, rapidly decaying in vertical strips) and
`ŵ(0) := W(1) = ∫_0^∞ w > 0`. Write

    ψ_w(N) := Σ_{n≥1} Λ(n)w(n/N),        S_w(N) := ψ_w(N) − N ŵ(0),
    β_max  := sup\{ Re ρ : ζ(ρ) = 0, 0 < Re ρ < 1 \}  ∈ [½, 1] .

For `θ ∈ R` put `w_θ(u) := w(u)u^{θ}`, so `W_θ(s) = W(s+θ)`. The `θ`-family is the device of
Corollary 26.5 and is used only where §2.2 says.

**Definition 2.1 (nonnegative additive family).** A *nonnegative additive family over `Z`* is a datum
`𝔉 = (ℱ_N, S_f, w_f, f_0)` consisting of: a finite index set `ℱ_N` for each `N ≥ 1`; fibre functionals
`S_f(N) ∈ C` for `f ∈ ℱ_N`; **nonnegative** weights `w_f(N) ≥ 0`; and a distinguished fibre
`f_0 ∈ ℱ_N` for all large `N`, with `w_{f_0}(N) ≥ w_0 > 0` and `S_{f_0}(N) = S_w(N)` (or its
`μ`-analogue `Σ_{n}μ(n)w(n/N)`). The *family moment* of order `2k` is

    M_{2k}(N) := Σ_{f ∈ ℱ_N} w_f(N)\,|S_f(N)|^{2k}  ≥ 0 .                      (2.1)

We assume only that `N ↦ M_{2k}(N)` is measurable on `[1,∞)` and finite. Its Mellin transform is

    𝓜_{2k}(s) := ∫_1^∞ M_{2k}(N)\,N^{−s−1}\,dN ,                               (2.2)

and `σ_c(k) ∈ [−∞,+∞]` denotes its abscissa of convergence.

*Instances of record.* §26 is `ℱ_N = \{a/q : q ≤ Q = N^c, (a,q)=1\}`, `w_f ≡ 1`, `f_0 = 0`,
`S_f(N) = S̃(a/q;N)` (Lemma 26.3 identifies `S̃(0;N)` with `S_w(N)` up to `O_A(N^{−A})`); the
archimedean family is `ℱ = [0,T]` with `ψ_t(n) = n^{−it}`; the character family is `\{χ mod q\}`; the
quadratic-twist family is `\{χ_d\}`. **Definition 2.1 covers all of them**, because it imposes nothing
on `ℱ_N` beyond finiteness, nonnegativity of the weights, and the presence of the distinguished fibre.

### 2.1 The two imported analytic facts

**Fact 2.1a (Pringsheim–Landau for Laplace transforms; `IMPORTED`, `CLASSICAL`).** *Let `μ ≥ 0` be a
nonnegative Borel measure on `[0,∞)` and `F(z) := ∫_0^∞ e^{−zu}\,dμ(u)`, with abscissa of convergence
`σ_c ∈ R` (assumed finite). Then `z = σ_c` is a **singular point** of every analytic continuation of
`F` from the half-plane `Re z > σ_c`: there is no neighbourhood of `σ_c` to which `F` continues
holomorphically.*

Reference of record: D. V. Widder, *The Laplace Transform*, Princeton University Press, 1941,
Theorem II.5b. (Equivalent Dirichlet-series form: Hardy–Riesz, *The General Theory of Dirichlet's
Series*, Cambridge Tract 18, 1915, §II.6; for power series it is Pringsheim's theorem, 1894.) This is
the corpus's citation of record, already used at `phase-138/R138_001:762` and
`phase-139/R139_001:478`; it is imported unchanged.

*Passage to (2.2).* Substituting `N = e^{u}` in (2.2),

    𝓜_{2k}(s) = ∫_0^∞ M_{2k}(e^{u})\,e^{−su}\,du ,                             (2.3)

a Laplace transform of the nonnegative measure `dμ_k(u) := M_{2k}(e^{u})\,du`. So Fact 2.1a applies to
`𝓜_{2k}` verbatim.

**Fact 2.1b (Landau's oscillation theorem; `IMPORTED`, `CLASSICAL`).** *Let `β_max` be as above. Then
for every `ε > 0`,*

    ψ(x) − x = Ω_{±}\big(x^{β_max − ε}\big) ,

*i.e. `limsup_{x→∞}(ψ(x)−x)x^{−β_max+ε} = +∞` and `liminf = −∞`; the same holds for the smoothed
`S_w(N)` with `Ω`, provided `W(ρ) ≠ 0` for some zero `ρ` with `Re ρ > β_max − ε`.*

Reference of record: E. Landau, *Über einen Satz von Tschebyschef*, Math. Ann. **61** (1905), 527–550;
modern form in H. L. Montgomery and R. C. Vaughan, *Multiplicative Number Theory I*, CUP 2007,
Theorem 15.11 (and the general "Landau oscillation" mechanism, §15.1). `IMPORTED`, not re-proved.

**Where Fact 2.1b is and is not used.** It is used **only** in the `Ξ_a` gate (§5.1) and in the
optimality remark 2.8, never in the proof of T6(i). The reason is the correction recorded in §0: an
`Ω`-result is a statement along a sequence, hence on a set of Lebesgue measure zero, and the integral
(2.2) does not see sets of measure zero. Spreading a spike of height `V = N_0^{β_max−ε}` over the
interval on which the derivative bound `|S_w'(N)| ≤ C_w` (proved in Lemma 2.3 below) keeps `|S_w| ≥ V/2`
gives an interval of length `≍ V`, hence

    ∫ |S_w|^{2k}N^{−σ−1}dN ≫ N_0^{(2k+1)(β_max−ε) − σ − 1} ,

so this route yields only `σ_c(k) ≥ (2k+1)β_max − 1`, which is **strictly weaker** than `2kβ_max`
whenever `β_max < 1`. The blueprint's §1 is corrected accordingly; the engine is Lemma 2.2.

### 2.2 The `L²` abscissa lemma

This is the substitute for the oscillation theorem, and it is where the smoothness of `w` is spent.

**Lemma 2.2 (the mean-square abscissa of the smoothed Chebyshev remainder; `CLASSICAL`, `PROVED`).**
*Put*

    σ_2(w) := \inf\Big\{σ ∈ R : ∫_1^∞ |S_w(N)|^{2}\,N^{−2σ−1}\,dN < ∞\Big\} .

*Then:*

 *(a) `σ_2(w) ≤ β_max`, unconditionally and for every admissible `w`;*

 *(b) if `ρ` is a zero of `ζ` with `W(ρ) ≠ 0`, then `σ_2(w) ≥ Re ρ`;*

 *(c) consequently `sup_{θ∈R} σ_2(w_θ) = β_max`; more precisely, if `σ_2(w_θ) ≤ σ_0` for **every**
 `θ ∈ R`, then `β_max ≤ σ_0`.*

*Proof.* **(a)** The smoothed explicit formula. For `Re s > 1`, substituting `N = n/u`,
`∫_0^∞ w(n/N)N^{−s−1}dN = n^{−s}W(s)`, hence
`∫_0^∞ ψ_w(N)N^{−s−1}dN = (−ζ'/ζ)(s)\,W(s)`. Moving the contour to `Re s = −A` and collecting
residues — at `s = 1` (the pole of `−ζ'/ζ`, residue `W(1) = ŵ(0)`), at each non-trivial zero `ρ`
(residue `−m_ρ W(ρ)`), at the trivial zeros, and at `s = 0` — gives, for `N ≥ 1`,

    ψ_w(N) = N\,ŵ(0) \;−\; Σ_ρ m_ρ\,W(ρ)\,N^{ρ} \;−\; A_w(N) ,                (2.4)

with `A_w(N)` the archimedean/trivial-zero contribution, `A_w(N) ≪_{w,A} N^{−A}` for every `A > 0`.
The series converges absolutely because `W` decays faster than any polynomial in vertical strips
(`w ∈ C_c^∞`) while the zeros have density `≪ \log(2+|γ|)`. Therefore

    |S_w(N)| ≤ N^{β_max}\,Σ_ρ m_ρ|W(ρ)| + O_w(1) ≪_w N^{β_max} ,               (2.5)

since `N^{Re ρ} ≤ N^{β_max}` for `N ≥ 1`. Hence `∫_1^∞|S_w|^2N^{−2σ−1}dN ≪ ∫_1^∞ N^{2β_max−2σ−1}dN < ∞`
for every `σ > β_max`, i.e. `σ_2(w) ≤ β_max`.

**(b)** Let `σ > σ_2(w)` and pick `σ' ∈ (σ_2(w),σ)`. By Cauchy–Schwarz,

    ∫_1^∞|S_w(N)|N^{−σ−1}dN ≤ \Big(∫_1^∞|S_w|^2N^{−2σ'−1}dN\Big)^{1/2}
                              \Big(∫_1^∞N^{2σ'−2σ−1}dN\Big)^{1/2} < ∞ ,

so the Mellin integral `G(s) := ∫_1^∞ S_w(N)N^{−s−1}dN` converges **absolutely** for `Re s > σ_2(w)`
and is therefore holomorphic there. On the other hand, splitting (2.2) at `N = 1` and using the
`Re s > 1` identity above,

    G(s) = (−ζ'/ζ)(s)\,W(s) \;−\; \frac{ŵ(0)}{s−1} \;−\; E(s),                 (2.6)

where `E(s) := ∫_0^1 (ψ_w(N) − Nŵ(0))N^{−s−1}dN` is **entire** (the integrand vanishes identically for
`N < 1/2`, since `supp w ⊆ [1,2]` forces `ψ_w(N) = 0` for `N < 1/2`, and `∫_0^1 N^{−s}dN` is entire
after the elementary subtraction; explicitly `E(s) = ∫_{1/2}^1 ψ_w(N)N^{−s−1}dN − ŵ(0)/(1−s)` with the
first integral entire). By uniqueness of analytic continuation, (2.6) is the continuation of `G`. At a
zero `ρ` of `ζ` of multiplicity `m_ρ`, the right side of (2.6) has a pole of residue `−m_ρ W(ρ)`,
nonzero by hypothesis, and `ŵ(0)/(s−1)` is regular at `ρ ≠ 1`. A holomorphic function has no pole;
hence `Re ρ ≤ σ_2(w)`.

**(c)** Suppose `σ_2(w_θ) ≤ σ_0` for every `θ`, and suppose `ζ(ρ) = 0` with `Re ρ > σ_0`. By (b)
applied to `w_θ` — whose Mellin datum is `W_θ(s) = W(s+θ)` — we must have `W(ρ+θ) = 0` for every real
`θ`. Thus `W` vanishes on the horizontal line `\{ρ + θ : θ ∈ R\}`, a set with a limit point, so
`W ≡ 0`; but `W(1) = ŵ(0) > 0`. Contradiction. Hence `β_max ≤ σ_0`. Combining with (a) gives
`sup_θ σ_2(w_θ) = β_max`. ∎ `CLASSICAL` (Mellin–Plancherel and the smoothed explicit formula),
`PROVED`

**Remark 2.2a (what is needed of `W(ρ)`, exactly).** Part (b) needs `W(ρ) ≠ 0` at one zero of
near-maximal real part; nothing here proves that for a single `w`. `W` is entire of order `1` and
genuinely has zeros, so the hypothesis is not vacuous and not free. The **only** device proved here to
remove it is the `θ`-family of part (c), which is Corollary 26.5's device verbatim. Every statement
below that invokes `β_max` therefore quantifies over `θ ∈ R`. This is the weakest point of T6 and it is
flagged as such.

**Remark 2.2b (relation to Theorem 27.10).** Lemma 2.2 is the `L²` analogue of Corollary 27.10a. The
`L^∞` statement "`ψ(x) − x ≪_ε x^{θ+ε} ⟺ β_max ≤ θ`" is Theorem 27.10 and is `CLASSICAL`
(von Koch–Landau). Lemma 2.2 replaces the sup-norm by the mean square, which is what makes the passage
to `k ≥ 2` (Lemma 2.4) work without any loss. Neither implies the other formally: (a) is strictly
stronger than the `L^∞ ⟹ L²` direction because it is unconditional, and (b) is strictly weaker than
`⇐` of 27.10 because of the `W(ρ)` proviso.

### 2.3 Spreading, and the ascent from `k = 1` to `k ≥ 1`

**Lemma 2.3 (derivative bound; `PROVED`).** *`S_w` is `C^∞` on `(0,∞)` and `|S_w'(N)| ≤ C_w` for all
`N ≥ 1`, with `C_w` depending only on `w`.*

*Proof.* `ψ_w'(N) = −N^{−2}Σ_n Λ(n)\,n\,w'(n/N)`. The sum is supported on `N ≤ n ≤ 2N`, where
`n ≤ 2N` and `Σ_{n ≤ 2N}Λ(n) ≤ c·N` by Chebyshev (`CLASSICAL`); hence
`|ψ_w'(N)| ≤ N^{−2}·2N·‖w'‖_∞·cN = 2c‖w'‖_∞`. Subtract `ŵ(0)`. ∎ `PROVED`

(Lemma 2.3 is used only in the corrected accounting of §2.1 and in Remark 2.8; the main line does not
need it.)

**Lemma 2.4 (ascent; `PROVED`).** *Let `g : [1,∞) → [0,∞)` be measurable, let*

    σ_2 := \inf\{σ : ∫_1^∞ g(N)^2N^{−2σ−1}dN < ∞\},\qquad
    σ_{2k} := \inf\{σ : ∫_1^∞ g(N)^{2k}N^{−σ−1}dN < ∞\} .

*Then `σ_{2k} ≥ 2k\,σ_2` for every integer `k ≥ 1`.*

*Proof.* Fix `σ < σ_2` and set `A(X) := ∫_1^X g^2N^{−2σ−1}dN`, so `A(∞) = ∞`.

*Step 1 (`A` grows at least like a power along a sequence).* Fix `σ'' ∈ (σ,σ_2)` and put
`a_j := ∫_{2^j}^{2^{j+1}}g^2N^{−2σ''−1}dN ≥ 0`, so `Σ_{j≥0}a_j = ∞`. For `N ∈ [2^j,2^{j+1}]` we have
`N^{−2σ−1} = N^{−2σ''−1}N^{2(σ''−σ)} ≥ 2^{2j(σ''−σ)}N^{−2σ''−1}`, hence
`A(2^{j+1}) ≥ 2^{2j(σ''−σ)}a_j`. Since `Σ_j a_j = ∞`, for every `j_0` there is `j > j_0` with
`a_j ≥ j^{−2}` (otherwise the tail `Σ_{j>j_0}a_j ≤ Σ_{j>j_0}j^{−2} < ∞`). Along such a sequence `j_i`,
with `X_i := 2^{j_i+1}`,

    A(X_i) ≥ 2^{2j_i(σ''−σ)}j_i^{−2} ≥ X_i^{\,σ''−σ}   \text{ for all large } i .   (2.7)

*Step 2 (Hölder).* Write `f(N) := g(N)^{2k}N^{−2kσ−1} ≥ 0`. Then
`g^2N^{−2σ−1} = f(N)^{1/k}\,N^{1/k − 1}`, and Hölder with exponents `(k, k/(k−1))` on `[1,X]` gives

    A(X) ≤ \Big(∫_1^X f\Big)^{1/k}\Big(∫_1^X N^{−1}dN\Big)^{(k−1)/k}
         = \Big(∫_1^X f\Big)^{1/k}(\log X)^{(k−1)/k} ,

because `(1/k − 1)·\frac{k}{k−1} = −1` exactly. Hence

    ∫_1^X g^{2k}N^{−2kσ−1}dN \;≥\; \frac{A(X)^{k}}{(\log X)^{k−1}} .              (2.8)

*Step 3.* Insert (2.7) into (2.8): `∫_1^{X_i}g^{2k}N^{−2kσ−1}dN ≥ X_i^{k(σ''−σ)}/(\log X_i)^{k−1} → ∞`.
So `∫_1^∞ g^{2k}N^{−2kσ−1}dN = ∞` for every `σ < σ_2`, i.e. `σ_{2k} ≥ 2kσ_2`. ∎ `PROVED`

**Remark 2.4a.** The `k = 1` case of (2.8) is an identity and the lemma is vacuous there; the content is
`k ≥ 2`, and the `(\log X)^{k−1}` loss is harmless exactly because Step 1 supplies a *power*. This is
the point at which the blueprint's sequence-based route fails and Lemma 2.2's measure-theoretic
statement succeeds.

**Lemma 2.5 (maximum of abscissae for nonnegative Laplace transforms; `PROVED`).** *Let `(μ_j)_{j∈J}`
be nonnegative Borel measures on `[0,∞)`, `J` countable, `μ := Σ_j μ_j`, and let `σ_c(μ)` denote the
abscissa of convergence of `z ↦ ∫ e^{−zu}dμ(u)`. Then*

    σ_c(μ) \;=\; \sup_{j∈J} σ_c(μ_j) .

*Proof.* For real `σ`, `∫e^{−σu}dμ = Σ_j∫e^{−σu}dμ_j` by monotone convergence (Tonelli), all terms
nonnegative. If `σ > σ_c(μ)` the left side is finite, hence each term is, so `σ ≥ σ_c(μ_j)` for every
`j`: `σ_c(μ) ≥ \sup_j σ_c(μ_j)`. Conversely if `σ > \sup_jσ_c(μ_j)` each term is finite but the sum may
diverge, whence only `≥`; equality holds when `J` is finite, and in general the displayed identity is
to be read as `σ_c(μ) ≥ \sup_j σ_c(μ_j)`, with equality for finite `J`. ∎ `PROVED`

**Remark 2.5a (the honest form, and why only "`≥`" is used).** In Definition 2.1 the index set `ℱ_N`
**varies with `N`**, so `M_{2k}` is not literally a sum of `N`-independent measures and Lemma 2.5 does
not apply on the nose. The form actually used below is the trivial pointwise one:

    M_{2k}(N) \;≥\; w_0\,|S_{f_0}(N)|^{2k} \;≥\; 0 \qquad (N \text{ large}),      (2.9)

which gives `σ_c(k) ≥ σ_c(\text{fibre})` by monotonicity of the integral. Lemma 2.5 is stated because
it is the clean structural statement — *nonnegative summands cannot cancel an abscissa* — and because
it is exactly what fails over `F_q`, where the family generating function is a **ratio** (§2.4).

### 2.4 T6

**Definition 2.6.** For a nonnegative additive family `𝔉` write
`σ_c(k) = σ_c(k;𝔉,w)` for the abscissa of (2.2). Say that `𝔉` *admits the a priori exponent `a_k`* if
`M_{2k}(N) ≪_{k,ε} N^{a_k+ε}` for every `ε > 0`.

**Theorem 2.7 (T6, the bridge theorem; labels attached clause by clause).** *Let `𝔉` be a nonnegative
additive family over `Z` in the sense of Definition 2.1, with distinguished fibre
`S_{f_0}(N) = S_{w}(N)`, and let `k ≥ 1`. Then:*

**(i) `PROVED`.** *`𝓜_{2k}` is the Laplace transform of a nonnegative measure (identity (2.3)), its
abscissa `σ_c(k)` is attained at a real singular point of `𝓜_{2k}` (Fact 2.1a), and*

    σ_c(k) \;≥\; 2k\,σ_2(w) .                                                    (2.10)

*If moreover `σ_2(w_θ) = β_max` for the weight in use (which holds for all but at most the exceptional
`θ` of Remark 2.2a, and holds after quantifying over `θ ∈ R` by Lemma 2.2(c)), then
`σ_c(k) ≥ 2kβ_max`. In the opposite direction, for the single fibre alone the abscissa is **exactly**
`2kβ_max`.*

**(ii) `RESTATEMENT` (forward half), `PROVED` (converse half).** *If `𝔉` admits the a priori exponent
`a_k` for every member `w_θ`, `θ ∈ R`, of the weight family, then*

    β_max \;≤\; \frac{a_k}{2k} .                                                 (2.11)

*Conversely, no exponent `a_k < 2kβ_max` is admissible: the single fibre already forces
`M_{2k}(N)` to have Mellin abscissa `≥ 2kβ_max`. Hence a "bridge" supplying `a_k` for all `k` with
`a_k/2k → ½` is **equivalent to RH**; a bridge supplying a single `a_k ≤ k` is **already RH**; and a
bridge supplying `a_k = k + 2c` (the shape of `H(k,c)`, (26.2)) gives the strip
`β_max ≤ ½ + c/k`. All of this is independent of the family type — Farey, archimedean, quadratic
twists, characters mod `q`, number fields — because Definition 2.1 uses nothing about `ℱ_N`.*

**(iii) `PROVED` (and trivial).** *No cancellation between fibres removes the fibre's singularity: by
(2.9) the distinguished fibre contributes a nonnegative summand to a nonnegative integrand, so by
monotonicity (and, in the genuinely `N`-uniform case, by Lemma 2.5) `σ_c(k) ≥ 2kβ_max` whatever the
other fibres do. Adding fibres can only move the abscissa to the **right**.*

**(iv) `PROVED` as the inequality, `IMPORTED` for the `F_q` half.** *See Theorem 2.9.*

*Proof of (i).* Identity (2.3) is the substitution `N = e^u`; `M_{2k} ≥ 0` by (2.1) since
`w_f ≥ 0`. Fact 2.1a then gives the singularity at `σ_c(k)` (finite: `σ_c(k) ≤ ∞` trivially, and
`σ_c(k) > −∞` since `M_{2k} ≥ w_0|S_w|^{2k}` is not a.e. zero). For (2.10): by (2.9) and monotonicity,

    ∫_1^∞ M_{2k}(N)N^{−σ−1}dN ≥ w_0∫_1^∞|S_w(N)|^{2k}N^{−σ−1}dN ,

and by Lemma 2.4 applied with `g = |S_w|` the right side diverges for every `σ < 2kσ_2(w)`. Hence
`σ_c(k) ≥ 2kσ_2(w)`. With Lemma 2.2 this is `≥ 2kβ_max` under the stated proviso. For the reverse
inequality *for the fibre alone*: by (2.5), `|S_w(N)|^{2k} ≪_w N^{2kβ_max}`, so
`∫_1^∞|S_w|^{2k}N^{−σ−1}dN < ∞` for `σ > 2kβ_max`; combined with the lower bound, the fibre's abscissa
is exactly `2kβ_max`. ∎

*Proof of (ii).* Forward: `M_{2k}(N) ≪ N^{a_k+ε}` gives `σ_c(k) ≤ a_k + ε` for every `ε`, hence
`σ_c(k) ≤ a_k`; by (i), `2kσ_2(w_θ) ≤ a_k` for every `θ`, and Lemma 2.2(c) with `σ_0 = a_k/2k` gives
(2.11). Converse: immediate from (i). The three consequences are arithmetic: `a_k/2k → ½` forces
`β_max ≤ ½`, which with the functional equation is RH; `a_k ≤ k` gives `β_max ≤ ½` directly;
`a_k = k+2c` gives `β_max ≤ ½ + c/k`. ∎

*Proof of (iii).* (2.9) and monotonicity of `σ ↦ ∫`. ∎

**Remark 2.7a (candour: what (ii) is).** The forward half of (ii) is **the same theorem** as
Theorem 26.4 chained with Corollary 27.10a, in different clothing: Theorem 26.4 takes `2k`-th roots of
the moment bound to get `|S_w(N)| ≤ N^{a_k/2k + o(1)}` pointwise, and Corollary 27.10a converts that
partial-sum bound into `β_max ≤ a_k/2k`. T6(ii) reaches the same conclusion through the abscissa. It is
**not** a stronger statement and it is labelled `RESTATEMENT`. What the abscissa formulation buys is
threefold: (α) the converse half, which the Hölder route does not give — the abscissa is *exactly*
`2kβ_max`, so the hypothesis is calibrated, not merely sufficient; (β) robustness under the weight, the
`L²` route needing no pointwise bound at all; (γ) the structural statements (iii) and (iv), which are
statements about the *shape* of the hypothesis and have no counterpart in the Hölder route.

**Remark 2.8 (`Ω`-calibration; `PROVED` modulo Fact 2.1b).** With Lemma 2.3 and Fact 2.1b the same
conclusion can be reached along a sequence, but only in the weakened form
`σ_c(k) ≥ (2k+1)β_max − 1`, as computed in §2.1. The two bounds agree at `β_max = 1` and the
Lemma 2.2 route is strictly better for `β_max < 1`. Recorded so that the weaker route is not
re-attempted.

### 2.5 T6(iv): rationality has no nonnegative-additive counterpart

**Theorem 2.9 (T6(iv); `PROVED` for the `Z` half, `IMPORTED` for the `F_q` half).**

*(A) Over `Z`.* In every nonnegative additive family (Definition 2.1),

    σ_c(k) \;≥\; 2k\,β_max \qquad\text{for every } k ≥ 1 ,

so the fibre's singularity lies **at or to the right of** the abscissa of the total. Consequently:
*no a priori determination of the polar divisor of `𝓜_{2k}` by local data can place that divisor to
the left of `2kβ_max`; any assertion that it does is logically equivalent to the zero bound
`β_max ≤ a_k/2k` and is not an independent input.*

*(B) Over `F_q` (Deligne, Weil I, `IMPORTED`).* For a lisse `ℓ`-adic sheaf `F` of weight `w` on an open
`U ⊆ C/F_q`, the family generating function of the `2k`-th moment is

    L(U, F^{⊗k}⊗\bar F^{⊗k}, T) \;=\;
      \frac{\det(1 − FT \mid H^1_c(U_{\bar F_q}, F^{⊗k}⊗\bar F^{⊗k}))}
           {\det(1 − FT \mid H^0_c)\,\det(1 − FT \mid H^2_c)} ,

a **rational function**. Its only poles come from `H^0_c` and `H^2_c`; `H^2_c` is the coinvariants,
of weight `kw + 2` (so its inverse roots have modulus `q^{kw/2+1}`), and this weight is **known a
priori and depends on `k` only affinely**. The zero block `H^1_c` enters as a **numerator**. Hence
`\log L` has nonnegative coefficients (it is `Σ_{n,x}|tr F_x^n|^{2k}·(\ldots)/n`, the family sum being
a sum of `2k`-th powers of absolute values), Pringsheim–Landau locates the radius of convergence at
the first singularity on the positive axis, that singularity is the a priori pole
`|T| = q^{−(kw/2+1)}`, and the convergence of every local factor up to that radius forces
`|α_x|^{2k} ≤ q^{kw/2+1}` for every `x` and every eigenvalue, whence `|α_x| ≤ q^{w/2}` on letting
`k → ∞`.

*(C) The statement.* **Rationality is the one ingredient of Deligne's argument with no
nonnegative-additive counterpart over `Z`, and its role is precisely to place the fibre's singularities
*outside* the region of convergence of the family's generating function.** Over `F_q` the fibre
contributes to the **numerator** (`H^1_c`), so it does not create a pole, and the poles that do exist
are dictated by `H^{0}_c, H^2_c`, whose weights are known before any eigenvalue is examined: two
independent sources of information. Over `Z` the fibre contributes a **nonnegative summand**
(inequality (2.9)), so by (A) it *creates* the abscissa, and the upper and lower estimates of `σ_c(k)`
are computed from the same object `M_{2k}`: one source of information.

*Proof.* (A) is Theorem 2.7(i)+(iii). (B) is imported from Deligne, *La conjecture de Weil I*,
Publ. Math. IHÉS **43** (1974), 273–307, §3 (the extraction lemma 3.2 and the weight bound), in the
form already distilled in Doc 106 §1.1 items 1–4; nothing in it is re-proved here. (C) is the
conjunction, and its content is the asymmetry of the two inequalities: `σ_c ≥ 2kβ_max` over `Z`
against "the pole is at the a priori place, and the fibre is a numerator" over `F_q`. ∎

**Remark 2.9a (relation to Doc 106, stated candidly).** Doc 106's **Proposition 3.6** (the *sterility
lemma*; the blueprint cites it as "Prop. 3.9", which is in fact **Observation 3.9**, the multiply/sum
dichotomy — the numbering is corrected here) says: in the abstract tensor, properties (a)
(superadditivity of the index along powers) and (b) (uniform sublinear bound) are **computed from the
same data**, the signature, so no contradiction can be extracted; Weil I escapes because (a) is linear
algebra and (b) is *geometry* (rationality of the family `L`, weights of `H^2_c`) — two independent
sources. Doc 106 §5's **Lema Faltante 5.3** asks for a `C5`-type finiteness `κ(Q_k) ≤ f(k)` with
`f(k)/k → 0` coming from "data that do not move with `k`".

Theorem 2.9 is the **analytic instance** of that shape: `2kβ_max ≤ σ_c(k) ≤ a_k` is exactly
"`k·κ(ψ) ≤ κ(ψ^{⊠k}) ≤ f(k)`" with `κ ↔ 2β_max` and `f ↔ a_k`, and the sterility statement is that
both bounds are read off `M_{2k}`. And `a_k/2k → ½` is exactly `f(k)/k → 0` after the normalisation
`κ = 2β_max − 1`.

**This is an analogy, and it is labelled `ANALOGY`, not a derivation.** The corpus has already
downgraded the corresponding claim for T5 — "T5 is the analytic face of the abstract sterility lemma" —
to `ANALOGY` in §27's withdrawn table, on the ground that an implication would need a functor between
the two settings and none is supplied. The same objection applies verbatim here and the same label is
taken. What T6 *does* prove, unconditionally and without any functor, is (A): the inequality
`σ_c(k) ≥ 2kβ_max` in the analytic setting, on its own terms.

---

## 3. Corollaries

**Corollary 3.1 (T5 is the Parseval case; `PROVED`).** Let `𝔅` be a Parseval-type bound in the sense of
Definition 27.2, so that `M_{2k} ≤ 𝔅` for every `b` with the given norms. By Theorem 27.3,
`𝔅^{1/2k} ≥ L ≍ N`, i.e. the admissible exponent is `a_k ≥ 2k`. Theorem 2.7(ii) then returns
`β_max ≤ a_k/2k = 1`: **the trivial statement.** So T5 is precisely the assertion that the
`L²`-orthogonality mechanism delivers `a_k = 2k`, the worst admissible exponent, uniformly in `k`, in
`|ℱ|` and in the family type. ∎ `PROVED`

**Corollary 3.2 (the `k`-tuple / Hooley VII / Montgomery–Soundararajan moment conjectures are
RH-strength; `PROVED`).** Fix `c ∈ (0,1)` and `k ≥ 2`. If `H(k,c)` of (26.2) holds for every member
`w_θ` of the weight family — i.e. `M_{2k}(N) ≪ (\log N)^{B_k}Q^2N^{k} = N^{k+2c+o(1)}` — then

    β_max \;≤\; \tfrac12 + \tfrac{c}{k} .

If it holds for every `c > 0` (or for every `k` with `c` fixed), then `β_max ≤ ½`, i.e. RH.

*Proof.* `a_k = k + 2c` in Definition 2.6; apply Theorem 2.7(ii). ∎ `PROVED`

**Remark 3.2a (what Corollary 3.2 buys over Corollary 26.19 — the one genuinely new item).**
Corollary 26.19 derives RH from `H(2,c)` **together with** the off-diagonal hypothesis (26.9a)
`Σ_{d≠0}κ_Q(d)𝒞_4(d) = o(Q^2N^2)`, which §26 explicitly records as *a hypothesis of that corollary and
not a consequence of `H(2,c)`*, and it routes through Granville's average-Goldbach equivalence
(Funct. Approx. Comment. Math. **37** (2007), Thm 1A, with the 2008 Corrigendum). Corollary 3.2 needs
**neither**: no isolation of the `d = 0` term is performed, because the abscissa route never
decomposes `M_4` at all — it only uses `M_4 ≥ |S_w|^4 ≥ 0`. It is also quantitatively *weaker at a
single `c`* (it yields the strip `β_max ≤ ½ + c/2` rather than RH), and that is the honest trade: the
off-diagonal hypothesis is what upgrades a strip to the line at fixed `c`. Both statements are
**conditional on a hypothesis nobody can prove**; the FATAL rule is not triggered because nothing here
proves `H(k,c)` for any `k ≥ 2` (Open item (44) of §28.3 stands unchanged).

**Corollary 3.3 (promotion of the singular series from density to polar divisor; `RESTATEMENT`).**
`R149_002` §3 and Theorem 26.17 record the missing ingredient as "the singular series `𝔖(d)` and the
pairing `κ(d)` exist only as **densities**, never as **residues**". By Theorem 2.7, "promoting them to
a polar divisor" means exhibiting `a_k` with `𝓜_{2k}` holomorphic in `Re s > a_k`, i.e. asserting
`a_k = k + 2c` for all `k` — which by Corollary 3.2 is RH. Hence the promotion is not a step towards
the sign: **it is the sign.** ∎ `RESTATEMENT` (of Theorem 26.17's statement of the wall, made
quantitative)

**Corollary 3.4 (field uniformity; `PROVED`).** Every statement in §2 is proved from: the smoothed
explicit formula (2.4), Chebyshev's bound (Lemma 2.3), Hölder, Tonelli, and Fact 2.1a. All four hold
verbatim for `ζ_K`, `K` a number field, with `Λ` replaced by `Λ_K` and `ρ` by the zeros of `ζ_K`.
Hence T6 is field-uniform and compatible with T1 (Theorem 18.1). ∎ `PROVED`

---

## 4. Classification of positivity mechanisms

By T6, a positivity mechanism can produce a zero bound over `Z` only if its positivity is **not** a sum
of nonnegative fibre terms — otherwise (2.9) applies and the mechanism computes its own lower bound.
The exhaustive-by-shape list is four:

| mechanism | positivity is | status in the corpus |
|---|---|---|
| **additive-family** | `Σ_f w_f\|S_f\|^{2k} ≥ 0`, `w_f ≥ 0` | **closed by T6** (Theorem 2.7) and by T5 (Theorem 27.3) |
| **spectral** | `⟨Hf,f⟩ ≥ 0` for one self-adjoint / Kreĭn operator whose spectrum is the zeros | **the single open shape** (MW-5, MW-4) |
| **index** | a form of indefinite signature, sign controlled by an index theorem (Hodge index) | **closed**: Theorems 19.25, 21.15, 24.10, 24.11, 25.6, 25.7, Corollaries 25.8, 25.9 |
| **counting** | integrality: a degree, a number of points, an `h^0` | **closed**: Theorem 22.17 (and Lemma 24.1, Theorem 19.25) |

### 4.1 Mechanism (β), index/Hodge: closed by Paper 46

*Corpus check:* `grep -n "Theorem 19.25\|Theorem 21.15\|Theorem 22.17" 04-papers/46-row-d-the-sign/main.md`
→ lines 6332, 8796, 9847; `grep -n "Theorem 24.10\|Corollary 24.11\|Theorem 25.6\|Corollary 25.8"`
→ present in §§24–25 as summarised in §28.1 items 13–14.

The closing theorems, in the order the paper proves them:

* **Theorem 19.25** (frame defect): no `h^0` satisfying clauses (a), (b′), (c) exists for `ξ`; the
  hypothesis of the Hodge-index route is unsatisfiable. Unconditional.
* **Theorem 21.15**: the frame defect theorem holds **on a curve over a finite field**, where the
  Riemann hypothesis is a theorem. So the defect is not an artefact of `Spec Z`.
* **Theorem 24.10 / Corollary 24.11**: enlarging the carrier by the Galois group ring changes nothing
  in the `χ = 1` slot — the support function there is `s(γ,θ)`, unchanged, for every abelian `L/F`,
  every tower, every order; the frame defect theorem stands verbatim. Open item (35) answered
  negatively.
* **Theorems 25.6, 25.7, Corollaries 25.8, 25.9**: positivity-type constraints on the full square are
  **vacuous or infinite** — the translation shadow of the mixed cone is exactly `𝓔 ∪ \{0\}`, at every
  finite rank and for both signs, with the support constant unchanged.
* **Theorem 25.11** and **Theorem 26.13**: the two finite nonnegative pairings actually produced (the
  `(T)×(R)` block; the coinvariant block `κ`, `𝔖`) are **zero-blind**.

Mechanism (β) is therefore closed, and closed five times over. No new theorem is offered here.

### 4.2 Mechanism (γ), counting/integrality: closed by Paper 46

* **Theorem 22.17**: `Spec Z` is terminal in schemes
  (`Hom(Spec Z, Spec Z) = \{id\}`, via the affine anti-equivalence, import (X29a)), so there is **no
  ring of Frobenius correspondences** on `Spec Z`; the `+` that makes a degree additive does not exist.
* **Lemma 24.1**: where a ring does exist (the Galois group ring of a finite abelian extension), it is
  **inert on the radial carrier** — every Galois correspondence acts as the identity and `Z[G]` acts
  through its augmentation.
* **Theorem 24.10**: where a carrier does see the ring (the packet-graded carrier `𝒟_L`), it acts
  **away from the zeros of `ζ`**.
* Doc 106 **Proposition 3.10**: the Frobenius correspondences of the scaling site are **isometries** of
  `(𝒦,Q)` and therefore do not amplify the index.

A counting positivity needs a ring in which to count; the three theorems say the ring is absent,
invisible, or inert. Closed.

### 4.3 Mechanism (α), spectral: the single surviving shape

*Corpus check:* `grep -rn "MW-5\|CAND-1" --include=*.md 03-research 05-meta-and-planning` → phases 62,
63, 66, 71, 136 (`MAP_3_PHASES_061_110.md` rows 62, 63, 66, 71), 138 (`README`), plus Doc 106 §§3.3,
5.2–5.3.

The record, in one paragraph. **MW-5** is the absence of a Weil-cohomological realisation for the
`ζ` window: phase 63 proved that the scaling/Frobenius-candidate operator whose spectrum is the zeros
**anti-commutes** with `J` (ratio `2.000` exact) — it is complex-antilinear, the wrong type to be a
Frobenius — while `F_q` curves have `[F,J] = 0` and a gapped polarization; squaring (`D²` is `J`-linear)
was tried in R6/E99 and is gapless in both sectors. Phase 62 found that `ζ` genuinely *is*
positive-semidefinite on `V_+`, non-circularly and against DH and random-symmetric controls, but the
positivity is **gapless**: the spectrum cascades like `e^{−cL}` with `ζ` sitting at
`μ_max(L_prime,L_arch) = 1`, marginal from below. Phase 66 (rank-one escape) confirmed the easy
direction (`¬RH ⟹` unbounded escape norm) and a faithful proxy detector, and identified face (B) as
MW-5. Phase 71 (**CAND-1**, Connes–Consani–Moscovici zeta spectral triples) produced a 17-step
reduction to a "CCM stable divisor identification" lemma, deliberately sited off the positivity wall;
never closed. Doc 106 §3.3 records that the Frobenius correspondences of the scaling site are
isometries (Prop. 3.10) and §5.2–5.3 names the two missing lemmas (5.2 the analytic realisation of the
square; 5.3 the `C5` finiteness) and the finite falsifiable test (Problem 5.4: is the arithmetic side of
the doubled Weil functional on the diagonal kernel `h(x_1,x_2) = g(x_1x_2)`, supported on the almost
primes `p_1p_2`, autonomous?). **Hilbert–Pólya in the naive form is MW-4 and NG-E5 is `RETRACTED`;
neither is reopened here.**

**Statement.** Mechanism (α) is the only shape T6 does not touch, for the exact reason that its
positivity `⟨Hf,f⟩ ≥ 0` is a statement about **one** operator whose spectrum is the zeros — not a sum
over a family in which the distinguished fibre is a nonnegative summand. It is `OPEN`, it has been open
for decades, and **nothing is proposed for it here.**

---

## 5. Gates

Each gate is a falsifier the theorem must survive or be blind to, with the verdict.

### 5.1 `Ξ_a` (consistency: T6 must return `β_max = ½ + a`)

`Ξ_a(s) := ξ(s+a) + ξ(s−a)`, `0 < a < ½`; `Λ_a(n) := Λ(n)(n^{a} + n^{−a})`; the zeros lie on
`Re s = ½ ± a` (Theorem 12.4), so `β_max(Ξ_a) = ½ + a`. Every step of §2 applies to `Λ_a`: the
smoothed explicit formula (2.4) holds with `ρ` running over the zeros of `Ξ_a`; Lemma 2.3 holds because
`Σ_{n ≤ 2N}Λ_a(n) ≪_a N^{1+a}` (so `C_w` becomes `C_{w,a}N^{a}`, which changes nothing in §2.1 and is
not used in the main line); Lemma 2.2 gives `σ_2(w_θ) = ½ + a` after quantifying over `θ`; Lemma 2.4
gives `σ_c(k) ≥ 2k(½+a) = k + 2ka`.

**Verdict: PASS.** T6(ii) then says `H(k,c)` (`a_k = k + 2c`) is **false for `Λ_a` once `k > c/a``,
since it would force `½ + a ≤ ½ + c/k`. This reproduces Proposition 26.21(1) exactly, and by an
independent route: Proposition 26.21(1) argues through Landau's oscillation theorem applied to the
rightmost off-line zero; T6 argues through the abscissa. The two agree. Consistency check passed.

### 5.2 `Ξ_Q` (Epstein, no Euler product)

`Ξ_Q` is the completed Epstein zeta function of a principal form with `h(−D) > 1`: functional equation,
equimodularity, **not** an Euler product (a non-trivial complex combination of `h ≥ 2` Euler products,
Remark 18.12a), with real zeros in `(0,1)` and zeros right of `Re s = 1` (import (X21)).

**Verdict: T6 is blind to the Euler product, and says so.** §2 uses the Euler product **nowhere**: it
uses a Dirichlet series with a meromorphic continuation whose poles sit at the zeros (i.e. a
*polar-at-zeros* sequence in the sense of Definition 27.9), a smooth weight, and nonnegativity of the
weights `w_f`. So T6 applies verbatim to any polar-at-zeros datum with an explicit formula, `Ξ_Q`
included, and returns `σ_c(k) ≥ 2kβ_max(Ξ_Q)` with `β_max(Ξ_Q) > 1`. It therefore **cannot** be the
source of the sign: it is a statement about nonnegative measures, not about `ζ`. Recorded as a scope
limitation, in the same spirit as Remark 27.7a. (Open item (43) — that the `⇐` half of Theorem 27.10
for `Ξ_Q` needs an explicit formula to be more than an assertion — applies here too and is inherited,
not resolved.)

### 5.3 Beurling systems

A Beurling system `𝒫` satisfying BE1–BE8 has a nonnegative datum, an Euler product with nonnegative
atoms, a meromorphic continuation with a single simple pole, and an explicit formula. All of §2 goes
through, with `β_max(ζ_𝒫)` in place of `β_max`.

**Verdict: T6 is blind to `+` and to the Euler product.** Under (H-DMV) there are systems with
`β_max(ζ_𝒫) > 1 − δ` for every `δ > 0`, and T6 returns `σ_c(k) ≥ 2kβ_max(ζ_𝒫)` for them, correctly and
uselessly. So T6 is **a method theorem about family positivity, not a theorem about `ζ`** — exactly as
Remark 27.16 says of the BE-axioms. T6 adds no new information at the Beurling corner and claims none;
open item (41) is untouched.

### 5.4 `ζ_K` (field uniformity)

**Verdict: PASS**, by Corollary 3.4. T6 is field-uniform, hence compatible with T1 (Theorem 18.1) and
subject to its standard: a proof of `a_k ≤ k` for any family over any `K` proves GRH for `K`.

### 5.5 The FATAL rule

Nothing in §§2–4 proves, or is used to prove, (i) a zero-free region, (ii) a moment bound `H(k,c)` or
any unconditional upper bound on `M_{2k}(N)` for any `k ≥ 1` beyond the classical large sieve already
recorded in Theorem 26.9(ii), or (iii) any cancellation estimate. Every implication runs **from** an
assumed exponent `a_k` **to** a zero bound, never the other way. Corollary 3.2 is conditional on
`H(k,c)`, which §28.3 open item (44) records as presumed beyond present means and as requiring that any
claim of it be presumed erroneous until every error term and the `Q`-uniformity are re-derived. **FATAL
rule not triggered.**

---

## 6. Labels

| item | label | note |
|---|---|---|
| Fact 2.1a (Pringsheim–Landau for Laplace transforms) | `IMPORTED`, `CLASSICAL` | Widder, *The Laplace Transform*, 1941, Thm II.5b; corpus citation of record (`R138_001:762`, `R139_001:478`) |
| Fact 2.1b (Landau's oscillation theorem) | `IMPORTED`, `CLASSICAL` | Landau 1905; Montgomery–Vaughan, *MNT I*, Thm 15.11. Used **only** in §5.1 and Remark 2.8 |
| Lemma 2.2 (the `L²` abscissa `σ_2(w_θ)`, `sup_θ = β_max`) | `CLASSICAL` in substance, `PROVED` here | not found in the corpus (grep #4); the `θ`-family device is Corollary 26.5's |
| Remark 2.2a (the `W(ρ) ≠ 0` proviso) | `OPEN` as stated for a single weight | the weakest point of T6 |
| Lemma 2.3 (`\|S_w'\| ≪_w 1`) | `PROVED` | Chebyshev only |
| Lemma 2.4 (ascent `σ_{2k} ≥ 2kσ_2`) | `PROVED` | elementary; Hölder + a dyadic pigeonhole |
| Lemma 2.5 (max of abscissae) | `PROVED` | only the `≥` half is used (Remark 2.5a) |
| **T6(i)** (Theorem 2.7(i)) | `PROVED` | under the `θ`-quantified form of Lemma 2.2 |
| **T6(ii)** forward half | `RESTATEMENT` | = Theorem 26.4 + Corollary 27.10a (Remark 2.7a) |
| **T6(ii)** converse/optimality half | `PROVED` | the abscissa is exactly `2kβ_max` for the fibre |
| **T6(iii)** (no inter-fibre cancellation) | `PROVED` | trivial once stated; its force is structural |
| **T6(iv)** (Theorem 2.9), `Z` half | `PROVED` | it is Theorem 2.7(i)+(iii) |
| **T6(iv)**, `F_q` half | `IMPORTED` | Deligne, Weil I, §3; Doc 106 §1.1 |
| Remark 2.9a (T6 as the analytic form of Doc 106 Prop. 3.6 / Lema 5.3) | `ANALOGY` | **not** a derivation; the same downgrade §27 applied to the T5 version. Numbering corrected: the sterility lemma is Prop. **3.6**, not 3.9 |
| Corollary 3.1 (T5 as the Parseval case) | `PROVED` | |
| Corollary 3.2 (`H(k,c) ⟹ β_max ≤ ½ + c/k`) | `PROVED` | **new**: no off-diagonal hypothesis, no Granville |
| Corollary 3.3 (density → residue **is** RH) | `RESTATEMENT` | of Theorem 26.17 |
| Corollary 3.4 (field uniformity) | `PROVED` | |
| §4 classification, rows (β) and (γ) | `PROVED` (by the cited theorems of Paper 46) | nothing new proved here |
| §4 classification, row (α) | `OPEN` | MW-5; nothing proposed |
| §4 classification, exhaustiveness of the four rows | `CERTIFIED`, not proved | it is a taxonomy by the *shape* of the positivity statement, not a theorem; a fifth shape is not excluded |
| Gates §5.1 (`Ξ_a`), §5.4 (`ζ_K`) | `PROVED` (PASS) | |
| Gates §5.2 (`Ξ_Q`), §5.3 (Beurling) | `PROVED` (blindness, stated as scope) | |
| **Row D** | **no label; no sign claimed** | unchanged from §28.4 |

---

## 7. Open list carried and added

Carried unchanged from §28.3: (36)–(44), (P145′), O-148.2 = O-149.5 = Problem 25.13, (24)–(34).

Added by this round:

* **(O-151.1)** Remove the `W(ρ) ≠ 0` proviso of Lemma 2.2(b) for a *single* weight `w`, or show that
  it cannot be removed. Equivalently: for `w ∈ C_c^∞` with `supp w ⊆ [1,2]`, `w ≥ 0`, is
  `\{ρ : W(ρ) = 0\}` ever cofinal in `\{ρ : Re ρ > β_max − ε\}`? `OPEN`. **Blocking for the
  single-weight form of T6(ii); not blocking for the `θ`-family form used above.**
* **(O-151.2)** Exhaustiveness of the four-row classification of §4: is every positivity statement that
  could yield a zero bound over `Z` of one of the four shapes? `CERTIFIED`, and presumably not a
  theorem in any precise sense; a precise formulation would need an axiomatisation of "positivity
  mechanism" comparable to Definition 27.2's axiomatisation of "Parseval-type". `OPEN`.
* **(O-151.3)** Does T6 have a counterpart for families with *signed* weights `w_f` in which the
  negative part is a priori small? This is the only crack in Definition 2.1, and it is where an
  `F_q`-style numerator would have to enter over `Z`. No construction is proposed. `OPEN`, and **not**
  to be presumed negative: T6(iii) says nothing at all once `w_f ≥ 0` fails.

---

## 8. Proposed text for Paper 46, §28.6 (≤ 1 page)

> ### 28.6 The bridge theorem
>
> *Provenance. Taken from `03-research/phase-151-row-d-the-bridge/R151_001_BUILDER_ROUND1.md` §2, with
> the labels of record fixed by the phase's closing decision. Nothing in this subsection asserts,
> claims or suggests a sign; no zero-free region, moment bound or cancellation estimate is proved in
> it.*
>
> §26 measures one family; §27 shows that no `L²`-orthogonality extracts a fibre from any. This
> subsection states what the two have in common, as a theorem about abscissae, and identifies the one
> ingredient of Deligne's argument that has no counterpart over `Z`.
>
> **Definition 28.18 (nonnegative additive family).** An index set `ℱ_N` (finite for each `N`), fibre
> functionals `S_f(N)`, weights `w_f(N) ≥ 0`, the family moment
> `M_{2k}(N) := Σ_{f∈ℱ_N}w_f(N)|S_f(N)|^{2k}`, and a distinguished fibre `f_0` with
> `w_{f_0}(N) ≥ w_0 > 0` and `S_{f_0}(N) = ψ_w(N) − Nŵ(0)`. Write
> `𝓜_{2k}(s) := ∫_1^∞ M_{2k}(N)N^{−s−1}dN`, of abscissa `σ_c(k)`.
>
> **Lemma 28.19 (the mean-square abscissa; `CLASSICAL`, `PROVED`).** Let
> `σ_2(w) := \inf\{σ : ∫_1^∞|ψ_w(N)−Nŵ(0)|^2N^{−2σ−1}dN < ∞\}`. Then `σ_2(w) ≤ β_max` always; if
> `W(ρ) ≠ 0` then `σ_2(w) ≥ Re ρ`; and if `σ_2(w_θ) ≤ σ_0` for every member of the family
> `w_θ(u) = w(u)u^{θ}`, then `β_max ≤ σ_0`. *(The first part is the smoothed explicit formula; the
> second is the absolute convergence of the Mellin integral against a pole at `ρ`; the third is the
> device of Corollary 26.5.)*
>
> **Theorem 28.20 (T6, the bridge theorem).** For every nonnegative additive family and every `k ≥ 1`:
> **(i)** `𝓜_{2k}` is the Laplace transform of a nonnegative measure, `σ_c(k)` is a singular point of it
> (Landau's theorem for Laplace transforms; Widder, Thm II.5b), and `σ_c(k) ≥ 2kβ_max` after
> quantifying over the weight family; for the single fibre the abscissa is exactly `2kβ_max`. `PROVED`.
> **(ii)** Any a priori bound `M_{2k}(N) ≪ N^{a_k+ε}` gives `β_max ≤ a_k/2k`, and no `a_k < 2kβ_max`
> is admissible. So a bridge supplying `a_k` with `a_k/2k → ½` is **equivalent to RH**, for every family
> type. Forward half `RESTATEMENT` (Theorem 26.4 + Corollary 27.10a); converse half `PROVED`.
> **(iii)** No cancellation between fibres removes the fibre's singularity: it is a nonnegative summand,
> and abscissae of nonnegative Laplace transforms take the maximum. `PROVED`.
> **(iv)** Over `F_q` the fibre enters the family `L`-function through `H^1_c`, i.e. as a **numerator**,
> and the poles come from `H^0_c, H^2_c`, of weight known a priori and affine in `k`; so the fibre's
> singularity lies *outside* the disc of convergence. Over `Z`, by (iii), it lies *at or inside* the
> abscissa. **Rationality is the one ingredient of Deligne's argument with no nonnegative-additive
> counterpart over `Z`, and its role is precisely to place the fibre singularities outside the region of
> convergence.** `PROVED` over `Z`, `IMPORTED` (Weil I §3) over `F_q`.
>
> **Corollary 28.21.** Theorem 27.3 is the case `a_k = 2k` (Parseval), returning `β_max ≤ 1`.
> `H(k,c)` of (26.2) gives `β_max ≤ ½ + c/k` — recovering Corollary 26.19's conclusion in strip form
> **without** the off-diagonal hypothesis (26.9a) and without Granville's equivalence, at the cost of
> giving a strip rather than the line at a fixed `c`. The "promotion of the singular series from density
> to residue" of Theorem 26.17 is the assertion `a_k = k+2c` for all `k`, i.e. RH.
>
> **Scope.** T6 uses no Euler product, no functional equation and no `+`: it is a statement about
> nonnegative measures, and it applies verbatim to `Ξ_Q` and to every Beurling system, returning their
> own `β_max`. It is a **method theorem about family positivity, not a theorem about `ζ`**, and it is
> field-uniform (T1). Its relation to Doc 106's sterility lemma (Prop. 3.6) and Lema Faltante 5.3 —
> that `2kβ_max ≤ σ_c(k) ≤ a_k` is `k κ(ψ) ≤ κ(ψ^{⊠k}) ≤ f(k)` with `f(k)/k → 0` — is an **`ANALOGY`**,
> as in §27's withdrawn table; no functor between the settings is supplied.
>
> **Reading.** With T6, §28.4's clauses (1)–(3) become one statement: over `Z`, in any family in which
> the fibres enter additively with nonnegative weights, the upper and lower estimates of `σ_c(k)` are
> read off the same object, and there is no second source. The reopening condition of §28.4 is
> unchanged, and T6 sharpens what clause (2) must mean: not a polar divisor "determined by local data"
> in any sense compatible with nonnegative additivity — by (iii) no such divisor can lie left of
> `2kβ_max` — but one arising from a **numerator**, i.e. from cancellation of determinantal type.

---

*End of R151.001. Row D: no label. No sign claimed, asserted or suggested. FATAL rule not triggered.*
