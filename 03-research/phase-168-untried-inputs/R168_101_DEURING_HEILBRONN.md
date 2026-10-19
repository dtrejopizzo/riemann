# R168_101 — Deuring–Heilbronn / Turán repulsion as a zero-side input (phase 168)

**Status: WALL MET (slack type; the identity-level version is the explicit formula, already in the corpus). No theorem toward (★_cell). No label change.**

## 0. Corpus check
`grep -rn "Deuring\|Heilbronn\|repuls"`: the input is **NOT new**. `NO-GO-LIST.md` [NG-B3] "Deuring–Heilbronn repulsion"
(phase-25-lower-bounds-bj-audit/01-audit-classical.md §Mechanism 4): "D-H operates near Re s = 1 … no anti-Siegel repulsion away from the critical
line is known." Also NO-GO line 63 lists "Deuring–Heilbronn repulsion, Turán powers" as attempted. This round is a re-test
against the *new* walls (M_m, f_t, identification, W2/M), not a new input. Davenport–Heilbronn hits are unrelated.

## 1. Classical statements (literature from memory — FLAG: constants and exact forms to be checked)
- **D-H for ζ-type/Dirichlet L (Linnik 1944; Bombieri, *Le grand crible* 1974/87; Jutila 1977; Heath-Brown, Proc. LMS 1992).**
  If χ₁ (real, mod q) has a real zero β₁ = 1 − λ₁/log q with λ₁ small, then every other zero β+iγ of ∏_{χ mod q} L(s,χ) satisfies
  β ≤ 1 − c·log(1/λ₁)/log(q(|γ|+2)) (c absolute; Heath-Brown gives explicit c, valid for λ₁ ≤ some λ₀). PROVED-CITED [flag].
  Mechanism: positivity of ∑Λ(n)(1+χ₁(n))(1+Re χ(n)n^{-iγ})… ≥ 0 at σ>1 (or Turán's power-sum lower bound for ∑(s−ρ)^{-k}),
  where the exceptional zero contributes −1/(σ−β₁) comparable to the pole 1/(σ−1).
- **Turán power-sum method (Turán 1953; Knapowski; Montgomery, *Topics*, LNM 227, 1971, Ch. 11–12).** Gives zero-density
  N(σ,T) ≪ T^{A(1−σ)} log^B T and D-H as above. All statements are either near σ=1 or averaged (density). PROVED-CITED [flag].
- **Near the critical line.** To my knowledge (FLAG) **no** unconditional result says that an individual zero ½+δ+iγ* forces a
  zero-free or zero-sparse region around itself, or constrains the on-line zeros near γ*. Montgomery's pair correlation (1973) is
  statistical and on-line. The nearest phenomenon: a Siegel zero of L(s,χ_D) forces near-arithmetic-progression spacing of
  ζ's on-line zeros in a range (Montgomery–Weinberger 1974; Conrey–Iwaniec, Duke 2002) — repulsion caused by an exceptional
  zero of *another* L-function near 1, not by an off-line zero of ζ. PROVED-CITED [flag].

## 2. What Turán / Λ ≥ 0 gives at an off-line zero (PROVED)
Let s = σ₀+iγ*, σ₀ = 1+η, η∈(0,1], γ* large, ρ* = ½+δ+iγ*, D_k(σ₀) := ∑Λ(n)(log n)^{k−1}n^{−σ₀}/(k−1)!.
Hadamard + Stirling: for k ≥ 2, Z_k(s) := ∑_ρ (s−ρ)^{−k} = (−1)^{k}(d/ds)^{k−1}(ζ′/ζ)(s)/(k−1)! + O(γ*^{−k}) + O_k(γ*^{−k+1})
(pole and Γ-terms), and the Dirichlet side is bounded, by Λ ≥ 0, by D_k(σ₀) ≥ η^{−k} (pole at 1; D_k(σ₀)=η^{−k}+O(1)·… ).

**Prop 2.1 (Λ ≥ 0 inequalities are non-binding off σ≈1).** For each k ≥ 2: |Z_k(s)| ≤ D_k(σ₀) + O(γ*^{−k+1}). The off-line term
satisfies |s−ρ*|^{−k} = (½+η−δ)^{−k} ≤ 2^k, versus the bound ≥ η^{−k}. Every zero has |s−ρ| ≥ ½+η−δ_max ≥ η, and
∑_ρ |s−ρ|^{−2} ≪ log γ*, so the zero-side admits, for **every** configuration (on-line zeros and quartets with δ ≤ ½−c), the
estimate |Z_k| ≤ C log γ*·c^{−(k−2)}, which is < η^{−k} once k ≥ k₀(η,c,γ*) ≍ log log γ*/log(c/η). Hence for k ≥ k₀ the Λ-positivity
inequality is satisfied by every admissible zero set: **no repulsion**. For k < k₀ it is the O(log γ*) local count. PROVED.
- Equivalently, the classical D-H bound at β* = ½+δ: λ* = (½−δ)log(q γ*) ≫ 1, so log(1/λ*) < 0 and the D-H region is vacuous.
  (Rewritten formula; PROVED given the cited form.)
- The 3–4–1 / Turán lower bound loses (cK/(N+K))^{K} with N ≍ log γ* zeros in the disc, while the off-line zero's advantage over
  an on-line zero at the same height is ((σ₀−½)/(σ₀−½−δ))^k = (1+O(δ))^k: to win needs k ≫ log log γ*/δ, where the Dirichlet bound
  η^{−k} dominates. This is NG-B3's "Paley–Wiener barrier" made quantitative. PROVED (elementary; constants not optimized).

**Prop 2.2 (what survives: a slack inequality).** At heights where −ζ′/ζ is nearly Kronecker-aligned (|ζ′/ζ(s)| close to D₁(σ₀),
which occurs for a set of γ by Kronecker/Bohr — PROVED-CITED), Re Z₁(s) ≤ D₁(σ₀) + ½log γ* + O(1) is near-tight, so a zero
configuration near γ* cannot add arbitrary positive Re(s−ρ)^{−1}-mass there. This is a **local upper count with positive kernel
(σ₀−β)/|s−ρ|²**, in which a quartet with δ→0 contributes like two double on-line zeros (difference O(δ²)). PROVED.

## 3. Falsifier table
| test | result | label |
|---|---|---|
| **M_m** (ζ × rational quartets) | M_m has no Dirichlet series, so the inequality is not a statement about M_m; read as "zero sum ≤ ζ's Dirichlet bound", M_m violates it only where ζ's slack < quartet mass ≈ 4(σ₀−½)^{−1}·(1+O(δ²)); but ζ with a hypothetical quartet at γ* obeys it equally by moving on-line zeros (R163_801 §6 real-weight compensation), and the kernel sees the quartet only at O(δ²) beyond two on-line zeros. Hence the inequality constrains *counts*, not the *sign* variable. Does not separate at the witness. | PROVED (2.2) + ARGUED (compensation, as in R163_801 §6) |
| **Beurling zetas (Diamond–Montgomery–Vorhauer, Math. Ann. 2006; 00-references/beurling-dmv)** | Euler product, Λ ≥ 0, continuation, zeros arbitrarily close to σ=1: every repulsion law derived only from "Euler product + Λ≥0" holds for them, so it cannot exclude off-line zeros; it is a class property of {Euler products}, i.e. slack, not identification. | PROVED-CITED [flag] |
| **f_t** | no Euler product, no law; same window prime side. Irrelevant as falsifier; consistent with R163_901. | PROVED (logic) |
| **identification** | class {Euler product, Λ≥0, FE, q=1} = {ζ} (R164_190). The repulsion inequality is not identification; it is the Λ≥0 shadow of the explicit formula. Its identity-level strengthening (equality, all k, all heights) **is** the explicit formula = atomic exchange (R163_114, ⟺ RH): already the corpus' single own datum. | PROVED (R164_190) / ARGUED (reduction) |
| **W2/M (Theorem M)** | the only δ-dependence is (1+O(δ))^k in 2.1 and O(δ²) in 2.2: any repulsion radius r(δ) obtained this way → 0 as δ→0; at the zero-margin witness it is vacuous. | PROVED (from 2.1/2.2) |

## 4. Connection to (★_cell) and ω(E) (R165_201 Cor 2.2)
The sign variable ω(E) is a signed offset of witness nodes relative to on-line zeros of the cell. Repulsion as obtained in §2
gives at most an upper bound on the positive-kernel mass of zeros near γ* (a count), symmetric under on-line moves; it carries
no orientation, so it cannot push ω(E) into the positive region. Exact stop: **repulsion is a SLACK estimate** (Prop 2.1: vacuous
for k ≥ k₀; Prop 2.2: count with O(δ²) quartet visibility), not identity-level; W2/M kills it at the witness. It also does not
touch O167.101.2 (small-y on-line count): Prop 2.2 is a count of the same strength as S(t) = O(log t), not sharper.

## 5. Ledger
| # | item | label |
|---|---|---|
| 0 | input already in corpus (NG-B3) | PROVED (grep) |
| 1 | D-H near 1 (Linnik/Bombieri/Jutila/Heath-Brown), Turán density | PROVED-CITED [flag] |
| 1′ | no known individual repulsion near σ=½ from an off-line ζ-zero | literature claim [flag] |
| 2.1 | Λ≥0/Turán inequalities non-binding for β ≤ 1−c; D-H vacuous at ½+δ | PROVED |
| 2.2 | surviving local count, quartet visible only at O(δ²) | PROVED |
| 3 | M_m not separated; Beurling falsifier; identity-level = explicit formula | PROVED / PROVED-CITED / ARGUED |
| 4 | no effect on ω(E); stop = slack (W2/M) | PROVED (from 2.1–2.2) for the class of §2 inequalities; ARGUED for "any Euler-product repulsion law" |
| O168.101.1 | an identity-level, non-linear (Euler-product) zero-side law near σ=½ not reducible to the explicit formula | OPEN (no candidate) |
