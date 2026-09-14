# Panel 1 — Mathematical correctness of the proofs (Papers 43, 44, 45)

Reviewer 1 of the three-member independent review panel, phase 133.
Date: 2026-09-12.  Mandate: **mathematical correctness**.  Method: read the
lead's decisions of record (`R130_005`, `R131_019`, `R132_007`), select the
load-bearing theorems, and **re-derive each from its stated hypotheses**
without reading the supplied proof as authority; run every script in
`phase-130/131/132/scripts/`.  No paper was edited.

**Headline.  No FATAL finding.  Every load-bearing theorem re-derives.
Four MAJOR findings, all of exposition or bookkeeping rather than of
mathematical content: one symbol collision in Paper 43 that makes one remark
false as written, one false supporting assertion inside an otherwise correct
proof (Thm 14.1), one unlabelled algebra transfer under two `PROVED` clauses of
row A, and one false "no external inputs" claim in Paper 44 §11.  All four have
local repairs that change no verdict.  Papers 44 and 45 depend on no
unlabelled import beyond what row A carries; Paper 43 does (finding A3).**

---

## 1. Scripts

| script | result |
|---|---|
| `130/contour_check2.py` | runs; residue + contour = axis integral to `1e−27` ✓ |
| `130/mertens_check.py` | runs; mesh sum `1.0000` at three windows ✓ |
| `130/ml_check.py` | **crashes** (`TypeError`, `np.exp` applied to an `mpf` inside `mp.quad`). Superseded by `R130_ml_check.py`, which does the same job and passes; but a broken script sits in the record. **MINOR (A8)** |
| `130/R130_ml_check.py` | runs; Mittag–Leffler form agrees with the closed form to `≤5e−5` at `p=2,3,7,∞`; residues at `±i/2` are `∓i` at every place ✓ — this is Thm 9.7b(a),(b),(c) numerically |
| `131/verify_131_contacts.py` | runs; ALL CHECKS PASS + ROUND-4/5/6 PASS ✓ (incl. the two *negative* blocks (F) "no rate is convention-free" and (H) "(Wgr) is FALSE") |
| `132/verify_132_explicit_formula.py` | 26/26 ✓ |
| `132/lead_explicit_formula_check.py` | explicit formula to 20 digits; `A(s)+A(1−s) = 0` to 25 digits ✓ |

The numerics are honest: two of the blocks exist to *refute* the authors' own
earlier claims, and they do.

---

## 2. Findings

Graded FATAL (kills a label) / MAJOR (kills or rewrites a statement, not a
label) / MINOR (local).

### Paper 43 (row A)

**A1 — MAJOR — `D_A^0` denotes two different spaces.**
*Location:* line 1072 (`D_A^0 := {F : F ≡ 0 on a neighbourhood of the identity
class}`) versus **Definition 9.10**, line 2865 (`D_A^0 := ker λ_− ∩ ker λ_+`,
the primitive sector).  These are incompatible: a primitive `F` generally has
`F(1) ≠ 0` (indeed Paper 45 Cor 9.6a proves `c‖F‖² ≠ 0` on exactly that
sector).  The collision is **load-bearing in one place that is false as
written**: **Remark 8.6b**, line 1146 — *"Every result in §§9–10 is either
proved on `D_A^0`, where `F(1)=0`, or invariant under changing `c`"*.  Under
Definition 9.10's reading that sentence is **false**, and it is precisely the
sentence Paper 45 Cor 9.6a had to overturn ("the correction `c‖F‖²` does not
vanish on the primitive sector").  Theorem 8.8, Theorem 8.9 and Theorem 9.5
all use the §8 meaning and are correct; Theorem 9.12(iii)'s phrase "a
regularization-free computation on `D_A^0`" survives only by the accident that
the witness `Φ = F − F′` of Theorem 9.5 lies in **both** spaces.
*Repair:* rename the §8 set `D_A^{off}` (three occurrences in §8, plus 1398,
1412, 1482, 1511, 1932, 4675) and rewrite Remark 8.6b as: *"every result in
§§9–10 is either proved on `D_A^{off}`, where `F(1)=0`, or invariant under
changing `c` (Theorem 9.8 explicitly so); on the primitive sector `D_A^0` the
constant does **not** drop out — see Paper 45 Cor 9.6a."*  No theorem changes.

**A2 — MAJOR — Theorem 14.1(a),(b): the stated reason is false.**
*Location:* proof of Thm 14.1, line ~5018: *"using that `D_A`'s Fourier images
contain all Schwartz functions in `τ` on each component"*, and the preceding
"choosing `F̂` supported in disjoint such sets".  `D_A = C_c^∞(C_S)` is
compactly supported in the `R^×` coordinate, so every `F̂(𝔠,·)` is **entire of
exponential type** (Paley–Wiener) and is **never** compactly supported in `τ`;
the Fourier image is not all of `S(R)` and the disjoint-support orthogonality
construction does not exist.
*Status of the conclusion:* **true**, and re-derived here by the correct
argument.  *Repair:* replace "supported in" by "concentrated in".  Since
`T̂+c ≤ m+c` everywhere and `T̂+c → −∞`, pick windows `I_1, I_2, …` on one
component with `T̂+c ≤ −K_j` on `I_j`, `K_j ↑ ∞`, and `F_j` with
`∫_{I_j}|F̂_j|² ≥ (1−η_j)∫_R|F̂_j|²`, `η_j → 0` (possible: translate and dilate
a fixed Paley–Wiener bump).  Then `I_A(F_j,F_j) ≤ (−K_j(1−η_j)+(m+c)η_j)
∫|F̂_j|² < 0`, and near-orthogonality of the `F̂_j` gives an
infinite-dimensional negative-definite subspace by Gram-matrix
diagonal-dominance.  Same for (b) on `{T̂+c > 0}` when `c > −m`.  (c) and (d)
are untouched; (14.2)'s numeric `5.372` re-derived and confirmed by
`R130_ml_check.py`.

**A3 — MAJOR — a `PROVED` clause rests on an unlabelled transfer.**
*Location:* **Remark 3.6** (lines 402–415).  The morphism classification
`(3.3)`, `Hom_{U-U}(E_a,E_b) = C·U_γ`, is proved in P123.082 **for a different
algebra**; the paper says so honestly — *"I use (3.3) for `U` and record this
as a transfer, not as a citation of an identical statement"* — but the transfer
carries **no status label** and does **not** appear in §12's import table.
`(3.3)` is used in Proposition 3.2(iv) (infinitely many objects, clause **A.2**)
and in the proof of Theorem 5.3 (the dagger, clause **A.4**), both graded
`PROVED`.  *Repair:* add a row to §12, id `Tr`, statement "P123.082 (3.3) for
the algebra `U` of (2.4)", label `CONDITIONAL` or `IMPORTED (transfer)`, with
the hypotheses-checked column pointing to Remark 3.6; and mark A.2, A.4
`PROVED modulo (Tr)` in §14.0b, or prove freeness of the lattice action on the
open stratum for `U`.  This is the **only** answer "yes" to the panel's
unlabelled-import question in row A.

**A4 — MINOR — Theorem 9.12, nondegeneracy step: the exponents are swapped.**
The display reads `a·conj λ_−(G_w) + b·conj λ_+(G_w) = a|w|^{1/2}conj λ_−(G) +
b|w|^{−1/2}conj λ_+(G)` "using `λ_∓(G_w)=|w|^{∓1/2}λ_∓(G)`" — internally
inconsistent: the stated rule gives `a|w|^{−1/2}…+b|w|^{+1/2}…`.  (The
`[REBUILT … finding F8: the exponents were swapped]` note fixed the wrong one.)
*Harmless:* the conclusion only needs unboundedness at **one** end per
coefficient; with the correct exponents `a = 0` is forced as `|w|_S → 0` and
`b = 0` as `|w|_S → ∞`, the two limits merely exchanged.  *Repair:* swap the
two exponents and the two limit clauses.

**A5 — MINOR — Theorem 9.8:** "*By Theorem 9.7(c) the zeros of `T̂(𝔠,·)` are
isolated*" should read `T̂(𝔠,·)+c`; the correct object is named two sentences
earlier.  No consequence.

**A6 — MINOR — Theorem 9.14a(a):** "`0 < λ_−(F_n)`" and "`0 < λ_+(G_n)`" need
`ψ ≥ 0`; the hypothesis says only "real `ψ` with `∫ψ = 1`".  Nothing uses the
strict positivity (only the upper bound `‖ψ‖_{L¹}e^{−na}` is used), but
Theorem 10.8b *does* assume `ψ ≥ 0` and should not have to re-assume it.
*Repair:* add `ψ ≥ 0` to Theorem 9.14a.

**A7 — MINOR — Theorem 9.7(b):** the parity term is
`½·π/cosh(πτ)`, bounded by `π/2`, not `π`; the bound "`max Ŵ_∞(0,·) + π`" is
true but loose by a factor 2.  Cosmetic.

**A8 — MINOR —** `scripts/ml_check.py` does not run (see §1).  *Repair:* delete
it or fix the `numpy`/`mpmath` mix (`mp.exp` inside `mp.quad`).

### Paper 44 (row B)

**B1 — MAJOR — §11's external-input claim is false for clause B.4.**
§11 states *"**In clauses B.1–B.9: none.**  Row B's contract is discharged with
no external citation"*.  But **Theorem 6bis.4**, which is the whole of the
amended clause **B.4** (`PROVED AS AMENDED`, and the clause the owner had to
amend), is proved from two elementary but genuinely external facts:
`\log|Φ_n(1)| = Λ(n)` (via Thm 6bis.3(v)) and `\log n = Σ_{d|n}Λ(d)` (Cor
5.3a, itself carrying only "`PROVED` (Möbius …)").  Both are `CLASSICAL`
number theory, neither is proved in the repository, neither is in any import
table.  They are elementary and no verdict is at risk, but the sentence as
written is not true.  *Repair:* add to §11 a third bullet, "**In clause B.4:
two elementary `CLASSICAL` facts — `Φ_n(1) = p^{[n=p^k]}` and `Λ = μ * \log` —
used in Thm 6bis.3(v) and Cor 5.3a**", and delete "none" from the B.1–B.9
bullet.  This is the answer "yes, mildly" to the panel's unlabelled-import
question in row B.

**B2 — MINOR — §11's parenthetical misstates Paper 43.**  "*adds none to the
one import (`W`, Wodzicki excision) recorded in Paper 43 §12*": Paper 43 §12
records **four** rows (`M`, `W`, `C`, `RR`) and says in terms "**Count.  Three,
not one**".  *Repair:* "…to the imports recorded in Paper 43 §12".

**B3 — MINOR — Theorem 6bis.3(v), "the divisor cube `d ↦ Sh_Z(Frob_d)`,
`d | n`".**  For non-squarefree `n` the divisor poset is **not** a cube (for
`n = p^k` it is a chain of length `k`).  The identity `Σ_{d|n}μ(n/d)\log d =
Λ(n)` is of course correct, and for `n = p^k` it is the 1-cube
`{p^{k−1}, p^k}`.  *Repair:* say "the total cofiber of the cube indexed by the
radical divisors of `n`, taken over the top layer", or replace "cube" by
"Möbius total cofiber over the divisor poset".

*(No finding against Thm 3bis.7, 3ter.4, 3ter.10, 3ter.12, 8bis.1b, 8bis.1e,
8bis.2, 8bis.4a, 8bis.6/6a/6b, 8bis.8 — all re-derived clean; see §3.)*

### Paper 45 (row C)

**C1 — MINOR — Lemma 5.1a's subtraction step is one citation short.**  The
proof computes `Σ_pW_p(Γ_h)` directly, then invokes the global Plancherel form
(Paper 43 Thm 9.7(d)) and says "subtracting the finite-place terms just
computed leaves the archimedean term".  That step needs the **place-wise**
identity `W_p(H) = ∫Ĥ·Ŵ_p\,dχ`, which is established inside the proof of Thm
9.7 but is nowhere stated as a numbered assertion.  *Repair:* state it as Thm
9.7(d′) in Paper 43, or cite "the termwise interchange in the proof of Thm
9.7(d)".  The lemma is true; this is a citation gap, not a hole.

**C2 — MINOR (disclosure, not error) — Theorem 10.4 is the one theorem of
Paper 45 not re-derivable from Paper 45.**  Steps (i),(ii) and the `C10` fix
(the real-linear surjectivity of `(a,b) ↦ Z_R(s_0)Φ(s_0)^N(a+bs_0^2)`, which is
an isomorphism iff `s_0^2 ∉ R`, i.e. iff `x_0y_0 ≠ 0`) re-derive **cleanly** and
the use of (E2)'s "no real nontrivial zeros" clause is exactly right.  Step
(iii), tail domination, is a *transfer* of `106_11` (27)–(30) with `D ↦ D+2`;
its correctness cannot be checked inside Paper 45.  It is labelled — (R1),
`PROVED-IN-REPOSITORY` — so this is **not** an unlabelled import, but the panel
should note that C.6's discharge rests on an estimate proved elsewhere.

**No unlabelled import in Paper 45.**  §11's table is complete, every row is
labelled, and the quarantine of (E8) survives the deletion test I re-ran by
inspection: removing Thm 9bis.4(ii),(iii) removes nothing else.

---

## 3. Table of re-derived theorems

Verdict key: **RE-DERIVED** = I obtained the statement from the stated
hypotheses independently; **RE-DERIVED (repair)** = ditto, but the written
justification contains a false or missing step, repaired above;
**TRANSFER** = correct modulo an external result I did not re-derive.

| # | theorem | what I re-derived | verdict |
|---|---|---|---|
| 43 Lem 3.3 | valuation splitting | `φ` a continuous hom retracting onto the free group `Γ_S`; abelian retraction ⇒ `A_S^× = Γ_S × ker φ`; `ker φ = R^××∏Z_p^×`; `\|x\|_S = \|x_∞\|` | **RE-DERIVED** |
| 43 Thm 8.8 | absolute convergence off the identity | all four counterterms vanish; shell sum finite, `≤ \sup\|a\|p^{−\|k\|/2}\mathrm{vol}`; unit packet bounded by `p^{j_0}` | **RE-DERIVED** (uses `D_A^0` in the §8 sense — finding A1) |
| 43 Thm 9.7(a) | finite symbol | `χ(j_p(p^kw)) = η_p^k κ_p(w)`; shell sum `= (\log p)2Re(ζ/(1−ζ))`, `\|ζ\|=p^{−1/2}`; unit packet `= −c(κ_p)\log p`.  Checked (9.14) independently at `p=3`, quadratic `κ`: integral `= −1 = −c(κ)` ✓ | **RE-DERIVED** |
| 43 Thm 9.7(b) | archimedean symbol | `Ŵ_∞ = ½∫'e^{iτt}dt/(2\|\sinh(t/2)\|) + (−1)^ε½·π/\cosh(πτ)`; `Cin` gives `−\log\|τ\|+O(1)`; closed form `\logπ − Reψ(¼+iτ/2)`; `\max = \logπ+γ+3\log2+π/2 = 5.372` | **RE-DERIVED** (A7 slack) |
| 43 Thm 9.7(c),(d) | real, bounded above, `→−∞`; Plancherel | ✓; interchange dominated termwise | **RE-DERIVED** |
| 43 Thm 9.7b | Mittag–Leffler, universal Tate residue | `Ŵ_p = L[1/(1−e^{−w})+1/(1−e^{−w̃})−2]`, `½\coth(z/2)` expansion, poles `τ_k^± = ±i/2+(2πk−θ_p)/\log p` with residues `∓i` — **recomputed the change of variable and the residues independently**; `Ŵ_∞` from `ψ`'s Mittag–Leffler, poles `±i(2n+½)`, residues `∓i`; hence `Res_{i/2}T̂ = −i(\|S_f\|+1)`.  Contour identity (d),(e): shifting `R → \{Im τ = h\}` picks up `+ΣF̂(τ_k^+)` with the right sign and orientation ✓ | **RE-DERIVED** |
| 43 Thm 9.8 | `𝓝 = 0` | `(F⋆G^†)^\wedge = F̂\overline{Ĝ}`; `G = χ_𝔠·g` legitimate (every character of `Z_q^×` is locally constant); density of `\{ĝ\}` in `S`; `T̂+c` real-analytic `≢0` ⇒ `F̂ ≡ 0` | **RE-DERIVED** (A5 typo) |
| 43 Thm 9.12 | Tate sequence, primitive sector nonzero + nondegenerate | exactness, `†`, module structure ✓; nondegeneracy via boundedness of the inverse Fourier transform against unbounded `\|w\|^{±1/2}` | **RE-DERIVED (repair A4)** |
| 43 Lem 9.14a0 | uniform trace seminorm | bounded set ⊂ one Fréchet step ⇒ finitely many components + `\|Ĝ\| ≤ C\min(1,τ^{−2})`; `\|T̂\| ≤ A_S+B_S\log(2+\|τ\|)` | **RE-DERIVED** |
| 43 Thm 9.14a | rulings are limits | `λ_+(F_n)=1` exactly, `λ_−(F_n)=∫e^{−ns}ψ ≤ ‖ψ‖_1e^{−na}`; `\sup\|F̂_n\| ≤ ‖ψ‖_1e^{−na/2}`; (c) from 9.14a0; (e) diagonal action on `B_T` | **RE-DERIVED** (A6) |
| 43 Thm 9.14b | canonical splitting | `σ` module map, `M̄σ=id`, both summands closed, projections continuous | **RE-DERIVED** |
| 43 Thm 9.14c | rulings are the scalar radical | `Ĝ_m(τ)=∫ψ(s)e^{−ms(½−iτ)}ds`, two parts ⇒ `N(G_m) = O(m^{−1}\log m)`; `β_T(MF_n,MG_m) → 1` | **RE-DERIVED** |
| 43 Thm 9.14c′ | `I_A`-null along **every** admissible pair | `\sup\|F̂_α\| ≤ ‖F_α‖_1`; AM–GM shows (ii) is strictly stronger than (i), so "spread" is a real restriction; (9.21) admissible and `N`-bounded | **RE-DERIVED** |
| 43 Thm 10.8b | Mertens; hyperbolic in the colimit | Step 0 profiles `h_{n,m}=e^{−t/2}(ψ_n*ψ_m)`; Step 1 `Σ_pW_p = Σ_NΛ(N)N^{−1}φ(\log N)`; Step 2 partial summation against `A(x)=\log x+O(1)` ⇒ `1+O(\max(n,m)^{−1})`; Step 3 `\|W_∞\| ≤ (1−e^{−2a})^{−1}e^{−(n+m)a}`; Step 4 both bounds of (10.19) re-derived | **RE-DERIVED** |
| 43 Thm 14.1 | no Hodge-index shape | (14.1) from (9.13); (c) `m ≥ 5.372` ✓; (a),(b) true, argument false | **RE-DERIVED (repair A2)** |
| 44 Thm 3bis.7 | radial trace = shell volumes + `K` | unit packet vanishes pointwise by radiality; `Λ(p^k)=\log p = \mathrm{vol}(p^kZ_p^×)`; archimedean branch-sum `= ∫K(\|t\|)h`; `K(t)=(1/4)[1/\sinh(t/2)+1/\cosh(t/2)] = e^{−t/2}/(1−e^{−2t})`, and `K(\log n) = n^{3/2}/(n^2−1)` — checked by hand and by script (5c),(5d) | **RE-DERIVED** |
| 44 Thm 3ter.4 | strong monoidal, true unit | Haar⋆Haar on cosets of compact subgroups; `K_{P(m)}K_{P(n)}=K_{P(mn)}`, `c_mc_n=c_{mn}`; `Frob_1=δ_1`; `\|c_n\|_S = 1/n` and the `r`-coordinate `n^{−1}` for `r∤n` recover `(n,P(n))` | **RE-DERIVED** |
| 44 Thm 3ter.10 | finite contact exact at every level | shells: only `n=q^m` survives, indicator at `r≠p` is `1` because the `r`-coordinate is the coset centre; unit packets vanish because `1 ∉ supp h`; archimedean `= (∫K h)·∏1[r^N \mid n−1]` | **RE-DERIVED** |
| 44 Thm 3ter.12 | support meets no stratum for composite `n` | archimedean coordinate `1/n` vs `q^{−m}` | **RE-DERIVED** |
| 44 Thm 6bis.4 | amended B.4 on objects | `\log\#(Z/Φ_n(1)) = Λ(n)`; `\log n = Σ_{d\|n}Λ(d)` | **RE-DERIVED** (external facts — finding B1) |
| 44 Thm 8bis.1b | Gram diagonal | stratification of `Z_r^×` by `v_r(1−u)`: `\mathrm{vol}\{v=j\}=r^{−j}` (`j≥1`), `=(r−2)/(r−1)` (`j=0`), summing to 1; integral `= (r−2)/(r−1)+(N−1)`; archimedean `−\log(1/ε)+O(1)` with the `(γ+\log4π)` counterterm — every constant recomputed | **RE-DERIVED** |
| 44 Thm 8bis.1e | Weil kernel = Gram form of `Frob⋆Δ^{rad}` | corollary of 3bis.7 once the indicators become `1` by `K^♮`-invariance; both hypotheses (width, chart) now explicit | **RE-DERIVED** |
| 44 Thm 8bis.2 | `Δ·Δ = −∞` | `F̂_ε(τ)=φ̂(ετ)`; `σ=ετ` scaling; `‖φ‖²/ε(\logε+O(1))`; bounded region handled separately, `A_S = ω̂_{fin}(0)` exactly | **RE-DERIVED** |
| 44 Thm 8bis.4a | positivity FAILS on the pure Frobenius form | `ω̂_{fin}(0) = Σ(\log p)2p^{−1/2}/(1−p^{−1/2}) > 0`; `Π` primitivises; `M_{bulk} ≍ T`, `M_{tail} = o(T^{−k})T`; majorant `(σ^2+1)^2` correct.  Script (E) values match by hand (chart `[2]`: `3.3468`) | **RE-DERIVED** |
| 44 Lem 8bis.6/6a | Riemann sums on a moving window | `(t−\log n)/gap_n = (x−n)(1+O(1/n))`, `≤5` terms, partition of unity ⇒ `1+O(e^{−L/2})`; `Σρ'(x−n) ≡ 0` is the cancellation that makes `‖(g_D)'‖_∞ = O(1)` | **RE-DERIVED** |
| 44 Lem 8bis.6b | single-frequency test cannot witness | `ĝ_L(ρ_0)=∫ψ(t/L)e^{δt}dt > 0` and `ĝ_L(1−\barρ_0)=∫ψ(t/L)e^{−δt}dt > 0`: **both positive reals**, so the resonant pair contributes `+`.  `(Wgr)` is false | **RE-DERIVED** |
| 44 Thm 8bis.8 | `\mathrm{vol}(Z_p^×)=\log p` unique | `ζ_p = c_p/(1−p^{−s})`, residue `c_p/\log p`; `ζ_∞ = 1/s`, residue 1; scale quotient checked (rescaling by `λ` preserves the agreement) | **RE-DERIVED** |
| 45 Lem 9.1 | entirety, reflection, bounds | `N`-fold integration by parts; `Φ_F(½+iτ)=\hat F(−τ)`; `Φ_h = Φ_FΦ_F(1−·)` | **RE-DERIVED** |
| 45 Lem 9.2 | zero sum as contour integral | argument principle; horizontals `O(X_j^{−4}\log^2X_j)` by (9.2) with `N=2` and (E3c); lines absolutely convergent | **RE-DERIVED** |
| 45 Lem 9.3 | reflection | `s=1−u` reverses orientation **and** sign of `ds`; `g(1−u)=g(u)` | **RE-DERIVED** |
| 45 Thm 9.4 | **Weil's explicit formula, proved** | `ξ'/ξ = A_0+A_Γ+ζ'/ζ`; (a) `A_0(1−s)=−A_0(s)`, rectangle residues `g(0)+g(1)=2Φ(0)Φ(1)`; (b) shift to `L_{1/2}`, `(1/πi)(i\,dτ) = 2·dτ/2π`, evenness kills `Im ψ`; (c) `g·n^{−s}` entire, shift, Fourier inversion gives `2n^{−1/2}h(−\log n) = n^{−1/2}[h(\log n)+h(−\log n)]`.  **Every constant recomputed; script agrees to 20 digits** | **RE-DERIVED** |
| 45 Lem 5.1a | radial trace, no support hypothesis | finite places by radiality (packet vanishes pointwise); archimedean via Thm 9.7(d), not via (8.5∞) | **RE-DERIVED (repair C1)** |
| 45 Thm 9.6 | the comparison theorem | `T_∞(Γ_h)` = minus the (gamma + prime) groups of (9.6) exactly; adding `2Φ(0)Φ(1)` gives (9.9); primitivity gives (9.10).  Script (5i),(5j): `I_A = −q = −Σ_ρ`, error `1.4e−9` at `N=200` | **RE-DERIVED** |
| 45 Cor 9.6a | `c=0` unique | `(Γ_F⋆Γ_F^†)(1) = ‖Γ_F‖² = ‖F‖²` by `d^*w = dt⊗μ`, `μ` a probability; Plancherel route agrees; `M(Γ_F)=0` does not kill `‖F‖²`.  Script (6a)–(6c) ✓.  The deleted "equivalently … is Weil's criterion" was correctly deleted | **RE-DERIVED** |
| 45 Thm 9bis.2′ | Tate residues | `A = −ξ'/ξ + 1/s + 1/(s−1)`; `ξ(0)=ξ(1)=½≠0`; residue 1 at each, cross-checked from `−½ψ(s/2) ∼ 1/s` and `−ζ'/ζ ∼ 1/(s−1)`; chart `f_p ∼ 1/s` gives `\|S_f\|+1` at `s=0`, `f_p(1)=\log p/(p−1)` finite gives `0` at `s=1`.  **Cross-consistent with Paper 43 Thm 9.7b(c)** under `s=½+iτ` (`Res_s = i·Res_τ`) — I checked this independently | **RE-DERIVED** |
| 45 Thm 10.4 | sufficiency (`¬RH ⇒` negative primitive tests) | `Π` primitivises (`Φ_{ΠG}=s(1−s)Φ_G`); the `C10` fix: `(a,b)↦Z_R(s_0)Φ(s_0)^N(a+bs_0^2)` is an `R`-iso iff `s_0^2∉R` iff `x_0y_0≠0`, `x_0≠0` being (E2)'s last clause — correct, and the only use of that clause | **TRANSFER** (tail step (iii) rests on `106_11`; finding C2) |
| 45 Thm 12.2 | `𝓝_∩ = 0` at every chart | Thm 9.7(d) on all of `D_A`; evenness of `T̂_S` on `𝔠_0` (`θ_p=0`); density of `\{ĝ\}`; `T̂_S` real-analytic, `≢0`, discrete zeros.  Correctly **not** a corollary of `𝓝=0` | **RE-DERIVED** |

---

## 4. Does any theorem labelled `PROVED` depend on an unlabelled import?

* **Paper 43: YES — one.**  Finding **A3**: the transfer of P123.082 (3.3) to
  the algebra `U`, under clauses **A.2** and **A.4**.  It is *disclosed* in
  Remark 3.6 but carries no status label and is absent from §12.  Everything
  else in row A traces to `PROVED-IN-REPOSITORY` notes or to the four declared
  imports; in particular **Theorem 9.8 (`𝓝=0`) is import-free**, as claimed,
  and I confirm that §§9–10 nowhere touch import `C`.
* **Paper 44: YES, mildly — two elementary facts.**  Finding **B1**:
  `Φ_n(1) = p^{[n=p^k]}` and `Λ = μ*\log` under clause **B.4**
  (`PROVED AS AMENDED`).  They are labelled `CLASSICAL` *locally* but §11
  asserts "none".  No other unlabelled dependency: the two quarantined
  `CLASSICAL` imports of §8bis.3–4 are used by no clause, and I verified by
  re-derivation that Thms 8bis.1b, 8bis.1e, 8bis.2, 8bis.4a, 8bis.8 and Lemmas
  8bis.6/6a/6b use none of them.
* **Paper 45: NO.**  §11's table is complete and every entry labelled; (E3)
  was correctly split into (E3a)–(E3d) in round 2, which is exactly the
  distinction Lemma 9.2 needs; (E2)'s "no real nontrivial zero" clause is used
  in exactly one place and said so; (E8) is quarantined and the deletion test
  holds.  The only caveat is C2 (a labelled transfer, not an unlabelled import).

---

## 5. Overall assessment, one paragraph per paper

**Paper 43 (row A).**  The mathematics is sound and, in the places that matter
most, better than the surrounding prose.  The two computational hearts —
Theorem 9.7's symbol (with the `−\log\|τ\|` archimedean divergence and the exact
ramified unit packet `−c(κ_p)\log p`) and Theorem 9.7b's Mittag–Leffler form
with the universal residue `∓i` at every place — I re-derived line-independently
and they are correct to the constant; the numerics in `R130_ml_check.py`
confirm them to `5e−5`.  `𝓝 = 0` (Thm 9.8) is a clean, import-free theorem and
deserves the weight placed on it.  The `9.14a–c′` package is the most careful
writing in the three papers: the `[REBUILT, round 2]` repair that replaced a
single family by the *class* of admissible approximations, and Remark 9.14c″'s
explicit refusal to claim a continuous extension of `I_A` to
`N_A^{dist}×N_A^{dist}`, are exactly the right moves.  Theorem 10.8b is a
correct and rather pretty computation and is correctly quarantined.  Against
that: one symbol collision (`D_A^0`) that makes Remark 8.6b false as written
(A1); one false supporting sentence inside Theorem 14.1's otherwise-true proof
(A2); one unlabelled algebra transfer under two `PROVED` clauses (A3).  None
touches a verdict.  My reading of the label: **sustained**, with A3 recorded
beside it.

**Paper 44 (row B).**  Row B is the most *self-critical* of the three and the
one whose negative theorems I trust most.  Theorem 8bis.4a is a genuine,
unconditional refutation of positivity on the pure-Frobenius form at every
finite chart, and I re-derived it completely (the `Π`-primitivised
concentration argument is correct, including the round-6 correction of the
majorant).  Lemma 8bis.6b's refutation of the withdrawn import `(Wgr)` is
right for the simplest possible reason — both Mellin factors at a resonant
off-line quartet are *positive reals* — and the script's block (H) is an
honest confirmation of a negative.  Theorem 3ter.4's inverse-semigroup
structure with a true unit, Theorem 3ter.10's exactness at every level, and
Theorem 8bis.8's uniqueness of `\mathrm{vol}(Z_p^×) = \log p` all re-derive
cleanly, and the last is a real theorem, not a stipulation.  Theorem 8bis.1b's
`(r−2)/(r−1) + (N−1)` and Theorem 8bis.2's `−‖φ‖^2ε^{−1}\log(1/ε)` I recomputed
from scratch and confirm.  The one defect is bookkeeping: §11's "no external
citation in B.1–B.9" is false for the amended B.4 (B1), and its description of
Paper 43's import count is wrong (B2).  My reading of the label:
**sustained**, with B1 corrected in §11.

**Paper 45 (row C).**  This is the strongest paper of the three, and the reason
is Theorem 9.4: the Weil explicit formula is *proved*, from (E1)–(E5), by a
contour argument every step of which I re-derived and every constant of which I
recomputed — and the derivation is then confirmed to twenty digits by the
lead's own script.  The step D128 `C4` had broken (term-by-term integration of
`ζ'/ζ` followed by a contour shift) is now legitimate for the stated reason:
after the expansion, `g(s)n^{−s}` is entire, so no zero is crossed.  Lemma 5.1a
is a model repair — it identifies that every application has `0 ∈ supp h`, that
the naive archimedean integral therefore diverges, and that the correct route
is the Plancherel form, which carries no support hypothesis.  Theorem 9.6's
sign bookkeeping (`T_∞(Γ_h)` is *minus* the gamma-plus-prime groups of (9.6))
is correct and is independently confirmed by check (5i)/(5j).  Corollary 9.6a
genuinely derives `c = 0` at the identity level, and the round-3 deletion of the
over-claimed "equivalently … is Weil's criterion" was the right call — I agree
with the reasoning that for `c < 0` the sign condition is plausibly still
RH-equivalent, so the biconditional was unearned.  Theorem 9bis.2′'s residues
are correct and, pleasingly, cross-check exactly against Paper 43 Theorem
9.7b(c) under `s = ½+iτ`.  Only two minor observations (C1, C2), neither
affecting a statement.  My reading of the label: **sustained**.

---

*No paper was edited by this reviewer.  All line references are to the files as
of 2026-09-12.*
