# R155.015 — Hostile audit of R155_014 (Row D for Z_1000)

*Auditor, phase 155, round 2. Line-by-line audit of `R155_014_ROW_D_FOR_Z1000.md` against
Paper 47 §7 (`thm:Z`, `lem:Rrig`, `cor:nontermwise`, `lem:smooth`), `04-papers/README.md` (rows A/B/C).*

## Verdict table

| item | verdict |
|---|---|
| Lemma 2.1 (dictionary `f_{w,Z} ≥ 0 ⟺ w·g_Z` positive definite) | **PROVED** |
| Theorem 2.2 (no finite zero universe admits a flat-top certificate) | **PROVED WITH REPAIRS** (one real gap: multiplicities, Step 1; repair below) |
| Theorem 1.3(i), (iii) | **PROVED** (trivial; (iii) circular as stated — see G3) |
| Theorem 1.3(ii) uniqueness of the representing measure | **WRONG as stated** (see G2) |
| §1.2 rows A/B do not transfer; row C transfers as a definition | **PROVED / fair** |
| Corollary 2.3 (deletes the three hypotheses of `cor:nontermwise`(ii)) | **PROVED WITH REPAIRS** (overclaim: see G4) |
| Corollary 2.4 (row D is intrinsically infinite) | **PROVED** (first sentence of the second clause is a `DIAGNOSTIC` gloss, not proved) |
| Prop. 2.7 | **PROVED WITH REPAIRS** (phase `φ_k` wrong for odd `k`; missing IBP boundary hypothesis — G5) |
| Cor. 2.8 | **PROVED** |
| Remark 2.5 | mixed: the Toeplitz/recursion sentence is **PROVED** (it is §2); "`dim ℋ(E_N) = 2N`", the Carathéodory–Fejér/Kreĭn determinacy citation and "for ζ the obstruction disappears" are **HEURISTIC** — must be labelled as such |
| §3 (i)–(iv) | **PROVED as cited**, except (ii) "edge sits on the prime comb" — see G6 |
| §4 answer to the owner | fair, modulo the label corrections above |
| Consistency with Paper 47 | no contradiction with `thm:Z`/`cor:RH`/Thm C (ζ has infinitely many zeros) |

## Gaps

**G1 (Step 1, the only real gap).** Theorem 2.2 explicitly allows multiplicities, but Step 1 demands
`a` with `z_1,…,z_d` **pairwise distinct** — impossible whenever `Z` has a repeated ordinate.
*Repair (complete, no loss):* let `w_1,…,w_r` be the **distinct** values of `γ` in `Z` with
multiplicities `m_j`, choose `a ∈ (0, 2T/d]` with `e^{iw_ja}` pairwise distinct (all but countably
many `a`), and take `P(z) = Π_{j≤r}(z − e^{iw_ja})` of degree `r ≤ d`. Then `A = [c_{i−j}]_{0≤i,j≤r}`
has rank `r`, `ker A = ℂ·v`, `v` real (the node set is conjugation-closed since `Z` is symmetric with
multiplicity), `v_0 ≠ 0`, `r·a ≤ 2T`; Steps 3–4 are verbatim; in Step 5 the Cesàro mean of `|g_Z(ma)|²`
is `Σ_j m_j² ≥ r > 0`, so `limsup|g_Z(ma)| ≥ √(Σ m_j²) > 0`. With this substitution Theorem 2.2 is
**PROVED** as stated. Everything else in §2 verifies: Lemma 2.1(⇒) uses exactly the Gauss–Weierstrass
argument of `lem:Rrig` (correct: `φ ∈ L¹ ∩ C`, `φ̂ ≥ 0 ⇒ ∫φ̂ = 2πφ(0) < ∞ ⇒ φ̂ ∈ L¹ ⇒` Bochner);
`A = V^*V` with `(V^*V)_{ij} = Σ_l z_l^{j−i} = c_{i−j}` (real even) ✓; Step 3's
`x^*Mx = 2Re(t̄ b^*v) + |t|²c_0 ≥ 0 ∀t ⇒ b^*v = 0` ✓ and `b_i = φ(ia−ma) = c_{m−i}` ✓, so (★) reads
`Σ_i v_i c_{m−i} = 0` ✓; the reversed-polynomial argument `Σ_i v_i z^{m−i} = z^{m−d}·z^dP(1/z)`
vanishes at `z = z_l` because `1/z_l = z̄_l` is a root ✓ (uses symmetry of `Z`, as claimed); Step 4
solves for `c_m` using `v_0 ≠ 0` — the direction matches the initial data `c_0..c_d` ✓; Step 5's
Cesàro identity needs no Weyl equidistribution, only `z_lz̄_{l'} ≠ 1` ✓ (the name "Weyl" is decoration).

**G2 (Theorem 1.3(ii)).** Uniqueness is false for "any positive tempered `μ`": `μ = 2Σ_jδ_{γ_j}`
satisfies `∫ĥ dμ = W_N(h)` for every **even** `h`. Only the even part of `μ` is determined. Repair:
"unique among **symmetric** positive tempered measures".

**G3 (Theorem 1.3(iii)).** `Z_N ⊂ ℝ` is true by construction of the `γ_j` as real ordinates, so the
third equivalence is circular in the toy universe; keep it only as a slogan, not as a theorem clause.

**G4 (Corollary 2.3).** `cor:nontermwise`(ii) asserts negativity **for arbitrarily large τ**.
Theorem 2.2 gives only "takes negative values somewhere" — it is non-constructive (Step 5 contradicts
positive definiteness on a lattice in `u`, and says nothing about the location in `τ`). So Cor. 2.3 as
worded overclaims: the correct statement is that Theorem 2.2 implies the **conclusion "not
non-negative"** with all three hypotheses deleted, while the "arbitrarily large τ" refinement still
needs Prop. 2.7 and hence its hypotheses. Reword Cor. 2.3 accordingly (and §4's row for it).

**G5 (Prop. 2.7).** (a) `k+2`-fold integration by parts gives `(−1/(it))^{k+2}∫e^{itu}dw^{(k+1)}`; the
factor `(−1)^{k+2} = (−1)^k` is dropped, so `φ_k = arg i^{−(k+2)}` is off by `π` for **odd `k`**
(inherited verbatim from Paper 47 `cor:nontermwise`(ii) — fix in both places). Harmless to the sign
conclusion, wrong as a formula. (b) The IBP needs `w^{(j)}(u) → 0` at `±∞` for `j ≤ k`; true under
`w ∈ 𝒲_T` with `w^{(k+1)}` of bounded variation, but it is a hypothesis and must be stated (Prop. 2.7
is applied to non-compactly-supported `w`, where Paper 47 never argued it). (c) Zero mean of `Ψ` ✓
(all frequencies `s > 0`, `S` a set so no collisions); "non-zero zero-mean trig polynomial takes
negative values on a relatively dense set" ✓; hence `f_{w,Z}(τ) < 0` for arbitrarily large `τ` ✓.

**G6 (§3(ii)).** "The window edge sits on the prime comb exactly when `2T = log n`" is imprecise: in
the displayed `eq:fw` the comb is `Σ_n v_nδ_{log n}` evaluated at `u = log n`, and the window is
`|u| ≤ 2T`, so the coincidence is `log n = 2T`, i.e. `T = ½log n` — which is exactly what items (E)
and (C) then use (`T = ½log n`). The sentence's "`2T = log n`" and the subsequent "`T = ½log n`" agree;
but the earlier clause of the same paragraph attributes the tail frequency to `2T` (Prop. 2.7 with
`s = 2T`) — two different roles of `2T` (window half-width in `u` vs. tail frequency) are conflated in
one sentence. Split them. Items (E), (C), Thm SC, §3(iii), §3(iv) verify as cited.

## Missed implications (worth adding)

* Theorem 2.2 + `lem:smooth`(iii) forces a **location** statement the file does not draw: if a
  genuine certificate `f_w ≥ c > 0` exists for ζ, then for every `Γ` the truncation `f_{w,Γ}` is
  `≥ c/2` on `|τ| ≤ Γ/2` yet negative somewhere; hence **all** its negativity sits at
  `|τ| ≳ Γ/2`, and by §3(iv) the threshold is `Γ ≳ (‖x‖₁M³/c)^{1/3}`. This is the quantitative form
  of Corollary 2.4 and is stronger than the non-constructive proof suggests.
* No contradiction with Theorem C / `cor:RH`: the certificate at `½log3` is for the complete zero
  measure. But `cor:zeros` should carry an explicit remark that it is **not** verifiable on any finite
  zero list — that is precisely Theorem 2.2.

## Readiness for Paper 47 §7

**Ready, after G1 (mandatory), G4 and G5 (mandatory rewording).** With the multiplicity repair,
Theorem 2.2 is a correct, hypothesis-free strengthening and should replace `cor:nontermwise`(ii),
with the asymptotic statement kept as a separate clause (it alone gives "for arbitrarily large `τ`"),
and the status line 1807 of `main.tex` updated from "the general case OPEN" to PROVED.
