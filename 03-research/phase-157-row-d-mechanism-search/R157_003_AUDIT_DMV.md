# R157_003 — Audit of R157_001 (O-150.1: importing (H-DMV) from the open secondary literature)

Object: `R157_001_DMV_IMPORT.md`. Pure mathematics; no numerics. `P46` =
`04-papers/46-intersection-frame-defect/archive/main.md`; `S1…S5` as in R157_001 §1.1 (`00-references/beurling-dmv/*.txt`). I opened every
quotation at the line stated. Web use: WebSearch; the zbMATH Open API (open access); arXiv PDFs 2110.11463, 2209.01689,
2202.01837 (Révész; read in the scratchpad, not stored). Springer pages redirect to an authentication page, and I did not
follow them. One new reference file was saved so that the new quotation can be checked by file and line:
`00-references/beurling-dmv/zbMATH-records.txt` (the zbMATH Open records of DMV 2006 and Zhang 2007; the
folder README was **not** edited, and a row for this file should be added). Amendments are applied in place in
R157_001, each marked "[amended per R157_003, Ak]". Nothing in P46 or any README was edited.

Verdict scale: PASS (correct and correctly cited), AMEND (the conclusion stands, but the statement or proof needs the listed
repair), FAIL (false, or unproved as labelled).

## 0. Citation check (every quotation of R157_001 §1.1, §2, §6)

| memo cites | found at | matches? |
|---|---|---|
| S1 l.15–53 (DMV: `N = ρx + O(x^θ)`, `π = Li + Ω±(x e^{−c√log x})`, dlVP region realised, RH fails) | 2004.11501.txt:15–53 | yes, verbatim up to PDF mangling; the "[…]" elides only the definition of `Ω±` (l.29–31) |
| S1 l.70–76 (Landau: (1.1) ⟹ dlVP PNT) | :70–76 | yes |
| S1 l.80–83 | :80–83 | yes |
| S1 l.89–95 (definition, multiplicities) | :89–95 | yes |
| S1 l.216–218 (DMV probabilistic discretisation) | :215–218 | yes |
| S1 l.268 (thanks to H. G. Diamond) | :268 | yes |
| S2 l.2687–2692 | 2409.10051.txt:2687–2694 | yes. The curve is `σ = 1 − a/log(|t|+2)` (the fraction is split across l.2690–2691) |
| S2 l.2695–2708 (`N(ζ_DMV;α,T) = Ω(T^{2λ(1−α)})`, fixed `α > θ`) | :2694–2708 | yes. **The memo under-uses it**: it proves the zero clause outright (§1 D3) |
| S2 l.2713–2718 (`ζ_DMV = ζ_c e^{Z}`) | :2713–2718 | yes, **but** the source gives only the bound `Z(σ+it) ≪_σ √log(|t|+2)` for `σ > 1/2`. The memo's "`Z` analytic" (§1.2 table, §6 doubt 2) is not in the source. It is derivable (§1 D2) (A2) |
| S2 l.2733–2742 (Ω-bound; convexity bound) | :2728–2742 | yes; "routine calculations which we omit" is at l.2730 |
| S2 l.44–47 (continuation to `Re s > θ`) | :43–47 | yes |
| S3 l.94–95 | 2211.08716.txt:93–95 | yes |
| S3 l.100–111 (Landau region; DMV zeros on a curve `σ = 1 − d/log|t|`) | :97–111 | yes |
| S3 l.113–118 (Lemma 1.1, `O_α(log T)` zeros per unit height) | :112–118 | yes |
| S3 l.1180, 1203–1209 (truncated explicit formula, Révész) | :1165–1180, 1203–1209 | yes. S3 l.1165–1167 itself calls it an "explicit Riemann–von Mangoldt-type formula" (Theorem 4.1, Révész); it is a truncated explicit formula for `ψ`. Not used after Z2/Z3 (§1 D3) |
| S3 l.1413–1458 (continuous model; `ℓ_k = 4^k`, `β_k = 1 − 1/ℓ_k`, `γ_k = e^{ℓ_k}`; holomorphic on `σ > 1/2`) | :1413–1458 | yes. Also l.1431–1436: "the actual discrete example … `ψ_P(x) = ψ_C(x) + O(x^{1/2} log x)`", which the memo did not use (§1 D2) |
| S4 l.189–210 | 2207.00665.txt:189–210 | yes |
| S4 footnote l.763–766 | :763–767 | yes (footnote 11) |
| S5 l.43–50 | 2012.06220.txt:43–50 | yes; note it gives `Ω`, not `Ω±` (l.49–50), as the memo says |
| S5 l.8–9, 106–108 (DMV = "case β = 1") | :8–15, 106–108 | yes |
| S5 l.125–140 (Euler/exp identity) | :124–140 | yes |
| S5 l.164 (discretisation lemma) | :164–170 | yes |
| R150_001 l.~175 "(DMV-a)" | R150_001:167–171 | **line wrong**: (DMV-a) is at l.167–171. L.173–177 is (DMV-b), which puts the `x e^{−c√log x}` term on the **prime** side, where it belongs (A1) |
| P46 locations l.11842–11861, 11863–11881, 11925, 12016–12017, 12087–12090 | P46 at those lines | yes, all five |

## 1. Doubts from R157_001, resolved

**D1. Source independence. — PASS after new evidence.** R157_001 is right that S1, S2, S3 and S5 share F. Broucke, and
S4 states the result in words only. I found three further open statements.

(i) **W.-B. Zhang, Math. Ann. 337 (2007) 671–704**, author's abstract as reproduced by zbMATH Open (Zbl 1121.11061,
reviewer H. Müller), `zbMATH-records.txt:19–23`, verbatim: *"Two Beurling generalized number systems, both
with N(x)=kx+O(x^{1/2}exp{c(log x)^{2/3}}) and k>0 are constructed. … The associated zeta function of the second has
infinitely many zeros on the curve σ=1−1/log t and no zeros to the right of the curve and the Chebyshev function ψ(x) of
its primes satisfies limsup(ψ(x)−x)/(x exp{−2√log x})=2 and liminf(ψ(x)−x)/(x exp{−2√log x})=−2. A sharpened form of
the Diamond-Montgomery-Vorhauer random approximation … [is] used in the construction."* Zhang is not a Ghent author. This
is the author's own abstract of a second model, not a restatement of DMV. It supports (H-DMV′) by itself (route Z3 below),
since `x^{1/2}exp{c(log x)^{2/3}} = O(x^θ)` for every `θ > 1/2`. The zbMATH record of DMV itself (same file, l.5–11) has
no review text ("contents unavailable due to conflicting licenses").

(ii) **Révész, three further arXiv papers**, independent of Broucke but not of S4, since they repeat S4's sentence:
2110.11463 (Mathematica Pannonica) l.129–131: "a construction of Diamond, Montgomery and Vorhauer [6]. They basically
showed that under Axiom A the Riemann hypothesis may still fail: moreover, nothing better than the most classical
zero-free region and error term …"; 2209.01689 l.171–186, the same; 2202.01837 l.1756–1758, which names the discretisation
theorem "Theorem 6 (Diamond–Montgomery–Vorhauer–Zhang)".

(iii) **Révész, S4 Theorem 5**, 2207.00665.txt:375–377. This is Révész's own theorem, read in its own (open) source,
statement only: *"Let the arithmetical semigroup G satisfy Axiom A. Assume that η(t) : [0,∞) → [0, 1−θ] is an arbitrary
real function such that D(η) is free of zeroes of the Beurling zeta function ζ_P. Then for arbitrary ε > 0 we have
∆_P(x) = O(x exp(−(1 − ε)ω_η(x)))"*, where `D(η) = {σ > 1 − η(|t|)}` (l.240) and `ω_η(x) = min_{t≥1}(η(t)log x + log t)`
(l.249). For `η ≡ δ ∈ (0, 1−θ]` the minimum is at `t = 1`, so `ω_η(x) = δ log x`. This turns the sketched
"independent route" into a cited theorem.

So (H-DMV′) now rests on **two author-independent chains**: Ghent (S1, S2, S3, S5) for DMV's system, and Zhang (via
zbMATH) plus Révész for Zhang's system. T3 needs one model (R150_003 Thm 2.8′ proof, l.141–142), so either chain suffices.
The primary texts (DMV 2006, Zhang 2007) remain unread. The label stays `CITED (secondary source)`, and **not** `IMPORTED`.

**D2. Discrete versus continuous. — PASS, and T3 does not depend on it.** Clause (c) is stated **for the discrete
`ζ_DMV`** in S2 l.2688–2691 ("a Beurling number system (P_DMV, N_DMV) … ζ_DMV(s) has infinitely many zeros"), and for "a
Beurling system" in S3 l.110–111. No transfer from `ζ_C` is needed for T3. As corroboration, the transfer is valid by two
routes:
* *From S2 l.2714–2718.* Let `h = ζ_DMV/ζ_c` on a domain where both are meromorphic. If `h = e^{Z}` with `Z` finite at
  every point (the stated bound gives this), then `h` has neither zeros nor poles. So `h` is holomorphic and zero-free,
  and the zeros of `ζ_DMV` and `ζ_c` coincide **with multiplicity**. Growth also transfers:
  `|e^{Z}| ≤ exp(C_σ√log(|t|+2)) ≪_{σ,ε} |t|^ε`. Holomorphy of `Z` is not stated in the source, and is not needed.
* *From S3 l.1431–1436 (`PROVED` here).* `ψ_P − ψ_C = O(x^{1/2}log x)` gives, by partial integration, that
  `D(s) := ∫_1^∞ x^{−s}d(ψ_P − ψ_C)` is holomorphic on `σ > 1/2`. On `σ > 1`, `D = −ζ_P'/ζ_P + ζ_C'/ζ_C`. `ζ_C` is
  holomorphic on `σ > 1/2` except for the pole (S3 l.1454). So `ζ_P'/ζ_P` continues meromorphically to `σ > 1/2`, and its
  residues equal those of `ζ_C'/ζ_C`. Hence `ζ_P = ζ_C·exp(holomorphic)` on `σ > 1/2`, and the zeros coincide with
  multiplicity, the `ρ_k` of S3 l.1443 included. This reproduces S2's `e^{Z}` from S3's data.

The growth that BE7 needs comes from Lemma 2.1 applied to the discrete system directly, not from `ζ_c`.

**D3. Lemma 2.2 and zeros near `σ = θ` at bounded height. — Lemma 2.2 FAIL as proved; the zero clause PASS by other
routes; T3 needs nothing about such zeros.**
* *T3 needs nothing about them.* (H-DMV)'s zero clause asks for zeros with `β > 1 − δ` for every `δ`. Zeros elsewhere
  in the strip violate no BE axiom: BE3 allows zeros, BE7 bounds `|ζ|` from above, and BE6 concerns only `σ > 1`.
* *The gap.* Lemma 2.2's step "Fix `ε > 0` with the infinitely many zeros not all in `θ < σ < θ + ε`. Then infinitely many
  lie on `C_a ∩ {σ ≥ θ+ε}`" is a non sequitur. "Not all" in a set does not give "infinitely many" outside it. If
  `a/log 2 > 1 − θ`, the curve `C_a` meets `σ = θ` at a finite height `t_0`, and the infinitely many zeros could accumulate
  at `(θ, ±t_0)`. The original caveat names exactly this. S3 Lemma 1.1 does not repair it, since it counts only zeros
  with `β ≥ α > θ`. So **Lemma 2.2 is proved only when `a/log 2 < 1 − θ`** (the curve then stays in `σ ≥ 1 − a/log 2 > θ`,
  and each bounded arc is compact), or when `|γ_n| → ∞` is assumed (A4).
* *Three routes that close the zero clause without Lemma 2.2:*
  **Z1** (`CITED`, S2 l.2694–2696): for fixed `α > θ`, `N(ζ_DMV; α, T) = Ω(T^{2λ(1−α)})` with `λ > 0`. So the count is
  unbounded for every `α ∈ (θ,1)`, and there are infinitely many zeros with `β ≥ α`. Taking `α_n ↑ 1` gives `β_n → 1`.
  **Z2** (`CITED` + `PROVED`): Theorem DMV(b) plus Révész Thm 5 (D1(iii)). If no zero lay in `σ > 1 − δ` (take
  `δ ≤ 1−θ`), then `ψ(x) − x = O(x^{1−δ/2})`. Partial summation, with the prime-power correction `≪ x^{1/2}log²x` from
  `N(x) ≪ x`, gives `π(x) − Li(x) = O(x^{1−δ/3})`. That contradicts `Ω±(x e^{−c√log x})`.
  **Z3** (`CITED` + `PROVED`, independent of Broucke): Zhang's second system plus Révész Thm 5. As in Z2, a zero-free
  `σ > 1−δ` would give `ψ(x) − x = O(x^{1−δ/2})`, which contradicts `limsup(ψ−x)/(x e^{−2√log x}) = 2`.
  Z2 and Z3 need Révész's semigroup setting: free generation and a locally finite norm (S4 l.38–50). Counting integers with
  multiplicity, as in BE1, gives exactly that. Axiom A (S4 l.62–69) is `N = κx + O(x^θ)` up to a bounded shift of `R`.

**D4. The misquotation. — PASS (confirmed independently).** R150_001:167–168 reads "`N_𝒫(x) = a x + O(x·exp(−c(log x)^{1/2}))`".
Every source gives DMV's integer law as `O(x^θ)`, `θ ∈ (1/2,1)`: S1:19, S2:2689, S5:49. S3 (l.110) and S4 (l.190, "under
Axiom A", with Axiom A = `O(x^θ)` at S4:62–69) say the same in words. The `x exp(−c√log x)` term is the size of the
**prime** oscillation in every source (S1:28, S2:2693–2694, S5:49; Zhang's `x e^{−2√log x}` for `ψ`). The misquotation
moved the prime-side term to the integer side, and R150_001's own (DMV-b), l.173–177, has it correctly on the prime side.
The "β = 1" point also checks: S1 l.236 and S5 l.8–9 give `(N_β)` with `O(x exp(−c′ log^β x))`, which at
`β = 1` is `O(x^{1−c′})`. The audit R150_002 §1.1 (l.36–50) and R150_003 §2.1 (l.66–73) were correct **about the quoted
hypothesis**: their divergence computation stands.

**D5. Scope. — PASS.** Nothing in R157_001 bears on the sign, on Weil positivity, or on any row's status. T3 is a
statement about derivations from BE1–BE8. Row D keeps no label.

## 2. Mathematical checks

**Lemma 2.1 (Mellin). — AMEND (A3).** The identity `ζ(s) = ρs/(s−1) + s∫_1^∞R(x)x^{−s−1}dx` is correct under
`N(1^−) = 0`: the boundary term is `0 − N(1^−) = 0`, and `x^{−σ}N(x) → 0` for `σ > 1`. So is the absolute and locally
uniform convergence on `σ > θ`, hence holomorphy of the integral, and the simple pole at `1` with residue `ρ`.
`|R| ≤ Cx^θ` for all `x ≥ 1` follows from `O(x^θ)` at infinity and boundedness on compacts, after enlarging `C`. The growth
claim "uniformly for `σ ≥ θ+ε`" is too quick: the bound `C|s|/(σ−θ)` grows with `σ`. Repair: on `θ+ε ≤ σ ≤ 2`, `|t| ≥ 2`,
use `|s| ≤ 2 + |t|` and `|s|/|s−1| ≤ 3/2`. On `σ ≥ 2`, use `|ζ(s)| ≤ ζ(2)`, from `dN ≥ 0`. Then
`|ζ(σ+it)| ≪_ε |t|` holds uniformly.

**Choice of `η`. — AMEND (A5).** With `η ≡ 1−θ`, BE3's region is `Re s > θ`. Lemma 2.1 gives `≪ |t|` only on
`σ ≥ θ+ε`, which suffices for R150_001's BE7 ("uniformly for `σ ≥ 1 − η/2`"). But P46's (H-DMV) (l.11846–11847) says
"polynomial growth … **in that region**", and on all of `Re s > θ` the constant blows up as `σ → θ`. Take
**`η ≡ (1−θ)/2`**. BE3's region is then `Re s > (1+θ)/2`, where Lemma 2.1 gives `≪_θ |t|` uniformly (with
`ε = (1−θ)/2`). The zeros with `β_n → 1` eventually lie in it. Both readings of BE7 are then met.

**BE1–BE8, item by item.**

| item | memo | audit |
|---|---|---|
| BE1 | `CITED` (discreteness) + `PROVED` | PASS. `N ≪ x` gives absolute convergence on `σ > 1`; multiplicities as in S1:91–93, S2:21–22 |
| BE2 | `PROVED` | PASS. `π ≤ N ≪ x` gives `Σp_j^{−σ} < ∞`, so the Euler product converges absolutely, `dΛ ≥ 0`, and `log Z` has coefficients `1/m ≥ 0`. Discreteness is `CITED` (S2:2688 "Beurling number system (P_DMV, N_DMV)", S3:1431) |
| BE3 | `PROVED` from (a) | PASS with A5 (`η ≡ (1−θ)/2`) |
| BE4 | `PROVED` | PASS. Real `p_j`, and reflection persists to the continuation by the identity theorem |
| BE5 | `CITED`/`CLASSICAL` | PASS as `CLASSICAL` (Landau), also stated verbatim at S5:32–35 ("Suppose that N(x) = ax + O(x^θ) holds for some a > 0 and θ < 1. Then … π(x) = Li(x) + O(x exp(−c√log x))"), a better cite than S1:70–76, which is phrased for (1.1). `ψ ≍ x` for `x ≥ x_0` |
| BE6 | from BE2 | PASS |
| BE7 | `PROVED`, `A = 1` | PASS with A3, A5 |
| BE8 | `CLASSICAL` | PASS |
| zeros | Lemma 2.2 (+ caveat) | **Lemma 2.2 FAIL as proved (D3)**; clause PASS via Z1, Z2 or Z3 |

**Proposition 3.1 ((H-DMV′) ⟹ (H-DMV)). — PASS after A5.** The derivation is complete. It uses discreteness (BE1, BE2,
BE4, BE6), Lemma 2.1 (BE3, BE7), Landau's PNT (BE5, `CLASSICAL`), Landau's theorem (BE8, `CLASSICAL`), and (H-DMV′)'s
zero clause. That clause gives, for every `δ`, a zero with `β > 1−δ` that lies in the BE3 region once `β_n > (1+θ)/2`. No
use of Lemma 2.2 is needed, because `β_n → 1` is **part of** (H-DMV′) and is supported by Z1, Z2 or Z3. The existential
`η` of BE3 is chosen per model, which matches R150_003 l.141–142.

**Theorem DMV(c), wording. — AMEND (A2).** "Equivalently it 'realizes the classical dlVP zero-free region'" should read
"consistently". The two statements are not formally equivalent as quoted.

## 3. Labels

| item | R157_001 proposes | audit |
|---|---|---|
| (H-DMV) | `CITED (secondary source)` via (H-DMV′) + Prop 3.1 | **CONFIRMED.** Support: DMV via S1, S2, S3, S5 (Ghent); Zhang via zbMATH (independent); zero clause Z1/Z2/Z3 |
| (H-DMV′) | `CITED (secondary source)` | **CONFIRMED.** "Support: … `β_n → 1` by Lemma 2.2" is replaced by Z1–Z3 (A4) |
| Lemma 2.1 | `PROVED` | `PROVED` (A3) |
| Lemma 2.2 | `PROVED` | **`PROVED` only if `a/log 2 < 1−θ` or `|γ_n| → ∞`; not used** (A4) |
| Prop 3.1 | `PROVED` | `PROVED` (A5) |
| T3 = R150_003 Thm 2.8′ = P46 Rem 27.16 | `METHOD-CONSTRAINT (meta-theorem); PROVED modulo one CITED import` | **`METHOD-CONSTRAINT` (meta-theorem), PROVED modulo the `CITED (secondary source)` import (H-DMV′); content = RESTATEMENT of DMV/Zhang + axiom list** (R150_002 §1.2 l.64–69; R150_003 l.671). **Stays a Remark in P46** (R150_005 l.43: "add T3 only as 'Remark …' until O-150.1 is read"; R150_002 l.448). The recommendation to promote it to a theorem is **not cleared** (A8) |
| Cor 2.9′ | `PROVED` from T3, inherits import | **CONFIRMED** |
| P46 Prop 27.17 item 3 | `PROVED` mod `CITED` (H-DMV′) | **CONFIRMED** |
| O-150.1 / P46 item (41) | `CLOSED at the secondary-source level` | **AMEND**: "**discharged at the `CITED (secondary source)` level; no longer blocking; residual OPEN: read DMV 2006 (and Zhang 2007) in the primary text.**" O-150.1 as written (R150_003 l.711–712, "Record their main theorem verbatim") asks for the primary read, which has not been done, so "CLOSED" overstates (A8) |
| Misquotation record | `PROVED` (bookkeeping) | **CONFIRMED**, line R150_001:167–168 (A1) |

## 4. Amendments applied in R157_001

* **A1**: (DMV-a) is at R150_001 l.167–171, not "l.~175". L.173–177 ((DMV-b)) had the prime-side term correctly.
* **A2**: §1.2 (c) "Equivalently" → "Consistently". Table: S2 states a bound on `Z`, not holomorphy; the zero and growth
  transfer holds anyway (R157_003 D2), and T3 does not use it.
* **A3**: Lemma 2.1: the uniform growth needs `σ ≥ 2` handled by `|ζ(s)| ≤ ζ(2)`.
* **A4**: Lemma 2.2: the proof has a gap at bounded height. It is valid only for `a/log 2 < 1−θ` or under `|γ_n| → ∞`.
  The zero clause of (H-DMV′) is supported by Z1 (S2 l.2694–2696), Z2 (DMV(b) + Révész Thm 5) and Z3 (Zhang + Révész
  Thm 5).
* **A5**: `η ≡ (1−θ)/2` throughout (BE3, BE7, Prop 3.1, §5), so BE7 holds uniformly on the whole BE3 region.
* **A6**: BE5 cite: S5 l.32–35.
* **A7**: §3 and §6 doubt 1: the independence gap is closed by Zhang (zbMATH, Zbl 1121.11061) and Révész.
* **A8**: §4: T3 stays a Remark, with its content recorded as a restatement. O-150.1 / (41) is "discharged at the CITED
  level, residual OPEN", not "CLOSED". §5's texts are superseded by R157_003 §5, which fixes over-attribution, `η` and
  sources.

## 5. Replacement texts cleared for Paper 46 (not applied)

**(a) Hypothesis (H-DMV), P46 l.11847 from "**Label:" through l.11854 "**blocking**.", replace by:**

> **Label: `CITED (secondary source)`** (phase 157). It follows from the reduced statement
> **(H-DMV′)**: *there are `θ < 1` and a discrete Beurling system `𝒫` with `N_𝒫(x) = ρx + O(x^θ)`, `ρ > 0`, whose zeta
> function has zeros `β_n + iγ_n` with `β_n → 1`.* Indeed, partial integration gives
> `ζ_𝒫(s) = ρs/(s−1) + s∫_1^∞(N_𝒫(x) − ρx)x^{−s−1}dx`, hence meromorphic continuation to `\mathrm{Re}\,s > θ` with a
> single simple pole at `s = 1` of residue `ρ`, and `ζ_𝒫(σ+it) ≪_θ |t|` uniformly on `σ ≥ (1+θ)/2`, `|t| ≥ 2`. So BE3
> and BE7 hold with `η ≡ (1−θ)/2`. BE5 is Landau's prime number theorem for such systems, BE8 is Landau's theorem on
> nonnegative Dirichlet integrals, and BE1, BE2, BE4, BE6 hold for every discrete Beurling system. (H-DMV′) is stated in
> the open literature for the system of Diamond–Montgomery–Vorhauer, *Beurling primes with large oscillation*,
> Math. Ann. **334** (2006), 1–36. For every `θ ∈ (½,1)`: `N(x) = ρx + O(x^θ)` (Broucke–Debruyne–Vindas, Adv. Math.
> **370** (2020), §1; Broucke, arXiv 2409.10051, §6.2); infinitely many zeros on a curve `σ = 1 − a/\log(|t|+2)`
> (ibid. §6.2; Broucke–Debruyne, arXiv 2211.08716, §1); and, for each fixed `α > θ`, infinitely many zeros with `β ≥ α`
> (arXiv 2409.10051, §6.2). Independently of these sources, W.-B. Zhang, Math. Ann. **337** (2007), 671–704 (author's
> abstract, zbMATH Open Zbl 1121.11061), constructs a Beurling system with
> `N(x) = kx + O(x^{1/2}\exp\{c(\log x)^{2/3}\})` and `\limsup(ψ(x)−x)/(x e^{−2\sqrt{\log x}}) = 2`. By Révész's
> theorem (arXiv 2207.00665, Theorem 5: under `N(x) = κx + O(x^θ)`, a zero-free half-plane `σ > 1−δ` with
> `0 < δ ≤ 1−θ` forces `ψ(x) − x = O(x^{1−(1−ε)δ})`), this system also satisfies (H-DMV′). **The primary texts have not
> been read**. The check against them is open item (41), which no longer blocks at the `CITED` level.

**(b) Remark 27.16.** Heading (l.11863): "(T3, as a conditional meta-theorem)" → "**(T3, a meta-theorem modulo a cited
import)**". L.11868: "Hence, conditionally," → "Hence, modulo that import,". Label sentence (l.11876–11878), replace from
"**Label of the remark:" through "unresolved.**" by:

> **Label of the remark: `METHOD-CONSTRAINT` (meta-theorem), proved modulo the `CITED (secondary source)` import
> (H-DMV); its content is a restatement of the Diamond–Montgomery–Vorhauer and Zhang constructions with the axiom list
> BE1–BE8 attached. It is recorded as a remark and not as a theorem of this paper because the primary sources have not
> been read (open item (41)).**

**(c) Proposition 27.17 heading (l.11897–11898):**

> **Proposition 27.17 (three falsifiers, three different conclusions; `PROVED`, item 3 modulo the `CITED (secondary
> source)` import (H-DMV)).**

**(d) Withdrawn-table row (l.11925), third column, replace by:**

> `WITHDRAWN`; replaced by (H-DMV) and Remark 27.16. The quoted hypothesis misquoted Diamond–Montgomery–Vorhauer: their
> integer law is `N_𝒫(x) = ρx + O(x^θ)`, `θ ∈ (½,1)`, and with it continuation to `\mathrm{Re}\,s > θ` holds (phase 157).
> The term `x\exp(−c\sqrt{\log x})` is the size of their **prime** oscillation. The divergence statement in the second
> column remains correct for the misquoted hypothesis.

**(e) Summary (l.12016–12017):** "Conditionally on (H-DMV), the axioms" → "**Modulo the cited import (H-DMV), the
axioms**".

**(f) Open item (41) (l.12087–12090), replace by:**

> * **(41)** *Discharged at the `CITED (secondary source)` level (phase 157); no longer blocking.* (H-DMV) follows from
>   (H-DMV′), which the open literature states for the Diamond–Montgomery–Vorhauer system, Math. Ann. **334** (2006)
>   (Broucke–Debruyne–Vindas, Adv. Math. **370** (2020), §1; Broucke, arXiv 2409.10051, §6.2; Broucke–Debruyne, arXiv
>   2211.08716, §1), and, independently, for Zhang's system, Math. Ann. **337** (2007) (author's abstract, zbMATH Open
>   Zbl 1121.11061, with Révész, arXiv 2207.00665, Theorem 5). *Residual, `OPEN`:* confirm against the primary texts.

The section title "27.4 T3, conditional, and three falsifiers with three conclusions" may become "27.4 T3, modulo a cited
import, and three falsifiers with three conclusions". That is optional and cleared.

**Not cleared:** R157_001's original §5 texts. Its (41) text attributes the full theorem (Ω±, zeros on the curve) to all
five sources, which S4 and S5 do not state, and uses `η ≡ 1−θ`. Also not cleared: any promotion of Remark 27.16 to a
theorem; the word "CLOSED" for (41); and Lemma 2.2 as a proof of the zero clause.

## 6. Overall verdict

**R157_001: PASS with amendments.** The main claim, (H-DMV) → `CITED (secondary source)` via (H-DMV′) and Prop 3.1,
**stands**. It is now supported by two author-independent chains, and the zero clause by three routes, none of which needs
Lemma 2.2. The misquotation finding is **confirmed**. One proof fails as written (Lemma 2.2, bounded-height gap), but it is
not load-bearing after A4. There are two label overstatements: promotion of T3, and "CLOSED" for O-150.1 (A8). There is
one uniformity slip (Lemma 2.1 at large `σ`, A3), one choice of `η` that fails P46's reading of BE7 (A5), and one source
over-read ("`Z` analytic", A2). **Row D: no label. No sign is claimed. Nothing moves any row's status.**
