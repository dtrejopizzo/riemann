# PANEL 2 — Consistency and connections between Papers 43, 44, 45

Reviewer 2 of the three-member independent review panel (phase 133).
Mandate: cross-paper citations in both directions, shared conventions,
contradictions and quantifier mismatches, respect for the withdrawal ledgers,
and the row-D handoff. Date: 2026-09-12. Sources read first: `R130.005`,
`R131.019`, `R132.007`; then the three `main.md` files in full at the cited
sections. **No paper was edited.**

Headline: **no FATAL finding; the three papers are one theory.** Two MAJOR
bookkeeping defects and eight MINOR ones, all in citation apparatus and status
labels, none touching a proof, a verdict or a carrier.

---

## 1. Citation verification, by theorem number, both directions

### 1.1 Paper 45 → Paper 43 (§14.3 "Used from Paper 43", §§1–12 in situ)

| cited as | exists? | what Paper 43 actually says | hypotheses the citing paper assumes | verdict |
|---|---|---|---|---|
| Lemma 3.3 | yes (l.342) | valuation splitting `A_S^× = Γ_S × ker φ`, `C_S ≅ R^××∏Z_p^×`, `\|x\|_S = \|x_∞\|` | fixed finite chart `S`, `S_f ≠ ∅` | ✅ |
| Corollary 3.4 | yes | `D_A = C_c^∞(C_S)` nuclear LF `†`-algebra | — | ✅ |
| Def. 8.5, 8.6, (8.4), (8.5), (8.5∞), (8.5b), Rem. 8.6a | yes | `T := Σ_{v∈S}W_v + c·F(1)`; `d^*x_∞ = dx/2\|x\|`; the declared `½` folding | `c := 0` supplied separately | ✅ |
| Theorem 8.8 | yes (l.1153) | absolute convergence off the identity, `F ∈ D_A^0`, no regularization | Paper 45 Lem. 5.1a deliberately does **not** use it (uses Thm 9.7(d)) | ✅ |
| Definition 8A.7d | yes (l.1853) | `c := 0` declared; four reasons | Paper 45 carries `c := 0` into §§1.2, 5.1, 9.5, 12 | ✅ (but see MINOR-5) |
| Theorem 8A.7b | yes (l.1633) | `𝓐_tr` Banach `†`-algebra, `Det_S^{rel}` | **declined** by Paper 45 with a reason | ✅ |
| Theorem 8A.7c, esp. (e) | yes (l.1800) | colimit trace `T_∞` on `D_A^∞`; window `R(F) < \log ℓ_next(S)` | used as (C1) and in Thms 9.6, 9.6′, §9.6 row 3 | ✅ |
| Theorem 9.1 | yes (l.2173) | `λ_∓(F) = ∫F\|u\|_S^{∓1/2}`, `M = (λ_−,λ_+)` surjective, `β_T = [[0,1],[1,0]]`, `λ_∓(F^†)=\overline{λ_±(F)}` | Paper 45 Thm 8.1 re-derives `M(Γ_F) = (Φ_F(1),Φ_F(0))` from it | ✅ |
| Theorem 9.12 (cited in §2 C.2 as "Thm 9.1, 9.12") | yes (l.2885) | exact Tate sequence (T2), primitive sector nonzero (T3) | — | ✅ |
| Definition 9.2 / Theorem 9.3 | yes | `I_A(F,G) := T(F⋆G^†)`, Hermitian, jointly continuous | — | ✅ |
| Theorem 9.7, 9.7(b),(c),(d), 9.7b, (9.11), (9.13) | yes | symbol real, bounded above, `\hat W_∞(0,τ)=\logπ−Reψ(¼+iτ/2)`; Plancherel on all of `D_A`; Mittag–Leffler with universal Tate residue `∓i`, total `∓i(\|S_f\|+1)` | Paper 45 Lem. 5.1a relies on 9.7(d) holding on **all** of `D_A` — confirmed | ✅ |
| (9.12b) | yes (l.2571) | `max_τ \hat W_∞(0,τ) = \logπ−ψ(¼) ≈ 5.372` | Paper 45 §1.5 cites it for the **archimedean** constant (round-3 correction `n7′`) | ✅ |
| (14.1), (14.2), Theorem 14.1 | yes (l.4990) | `I_A` indefinite, infinite index both sides, `(D_A^{prim})^{⊥}=0`; (14.2) bounds `m := \sup\hat T` **including finite places** | Paper 45 Warning 8.5, §14.4 item 2 | ✅ |
| Theorem 9.8, 9.13(a), 9.14, 9.14a–c′, Def. 9.14c0 | yes | `𝓝=0`, `N_A=D_A`; no `D_A`-module splitting; rulings as limits in the completion; `I_A`-null along every admissible pair | Paper 45 Prop. 8.3, Cor. 8.4, Thm 12.2 | ✅ |
| Theorem 10.8b | yes (l.4148) | `CLASSICAL`/Mertens; in the **colimit** chart the scalar form is hyperbolic on the rulings; counts toward no clause of A | Paper 45 uses it once, as (E8), quarantined, in Thm 9bis.4(ii) | ✅ |
| Theorem 8.10 / Rem. 8A.7e (`c_cut`) | yes | comparison with an imported regularization; "does not close"; no value claimed | **declined** by Paper 45 | ✅ |
| §14.0a (carrier), §14.1a (what row C may use) | yes | verbatim carrier; phase-132 block | — | ✅ |

**Handoff count.** Paper 45 §14.3 claims Paper 43 §14.1 hands row C three items:
Thm 10.8b (item 5), Thm 14.1 (item 1), window 8A.7c(e) (item 4). Verified: the
five numbered items of Paper 43 §14.1 are exactly as described, and the
round-3 correction of the "five bullets / three handoffs" confusion is right.

### 1.2 Paper 45 → Paper 44

| cited as | exists? | content | verdict |
|---|---|---|---|
| Def. 3bis.6, Lem. 3bis.6a | yes (l.1093/1097) | `Γ_h(w) = h(−\log\|w\|_S)`; `Γ_h ∈ D_A^{rad}`, `Γ_h⋆Γ_g = Γ_{h∗g}`, `Γ_h^† = Γ_{h^†}` | ✅ |
| Thm 3bis.7 (= Paper 45 Thm 5.1) | yes (l.1117) | the prime packet, hypothesis `0 ∉ supp h`, `c := 0` | ✅ — and Paper 45 correctly refuses to cite it where `0 ∈ supp h` (round-2 `M4`), using Lem. 5.1a instead |
| Def–Thm 3bis.8, (3bis.8), (3bis.11) | yes | `ω_fin` atomic, `ω_∞ = K(\|t\|)dt`, `Λ(p^k)=\log p = vol(p^kZ_p^×)`, `K(\log n)=n^{3/2}/(n²−1)` | ✅ |
| Thm 3bis.7′, Thm 3bis.10 | yes | contact locus; `Σ_{d\|n}Λ(d)=\log n=\log[L_S:nL_S]` | ✅ |
| Thm 3ter.10, Cor. 3ter.10b, Thm 3ter.12, Thm 3ter.14 | yes | exact finite contact; Frobenius off `Im j_∞`; composite support meets no stratum; `Frob_n ∈ N_A^{dist}`, `M(Frob_n)=(n^{1/2},n^{−1/2})`, **not primitive** | ✅ |
| Thm 8.3 | yes (l.3015) | `Γ_n^{rad} ∈ N_A^{dist}` | ✅ |
| Thm 8bis.1e, 8bis.1′, Cor. 8bis.1d | yes | Weil kernel = Gram form of `Frob ⋆ Δ^{rad}`; two-slice dichotomy; the Frobenius form carries only the finite half | ✅ |
| Thm 8bis.4 (i)–(vi), 8bis.4a, Rem. 8bis.4b | yes | interface; positivity fails on `Q_fin` at every chart, colimit version `OPEN`; `\hat W_fin^∞(0)=+∞` | ✅ content; ❌ label of (ii) — see MAJOR-2 |
| Thm 8bis.8, Cor. 8bis.8a, Rem. 8bis.8b | yes (l.4445) | `vol(Z_p^×)=\log p` unique **given a universal Tate residue**, up to one global scale; chart-invariance does **not** force it | ✅ — Paper 45 §1.6 and Cor. 9bis.3 reproduce the hypothesis faithfully |
| (8bis.9), (8bis.14a), (8bis.14e) | yes | Tate conditions `Φ_g(0)=Φ_g(1)=0`; `Q(g)=Σ_ρ\hat g(ρ)\overline{\hat g(1−\barρ)}`; `I_∂ = −Q` on primitive | ✅ |
| (C1), (C2) | yes (l.3180/3206) | colimit quantifier; bare level-`N` convention | ✅ — inherited verbatim in Paper 45 §1.2, including the explicit carve-out that (C1) does **not** govern the continued symbol `A` |
| "§9.1 the prime packet", §9.2, §9.3, §9.3a | yes, as **sections** | the four handoffs | ✅ (see MINOR-4 on "Theorem 9.1") |

### 1.3 Paper 44 → Paper 45 and Paper 44 → Paper 43

| cited as | exists? | verdict |
|---|---|---|
| Paper 45 Thm 9.4 (explicit formula), Thm 8.1 (polar packet), Thm 5.1, Lem. 5.1a, Thm 10.4 (`Π = −∂_t²+¼`, sufficiency) | all yes | ✅ — and Paper 45 Rem. 10.3 confirms it is literally the operator Paper 44 Thm 8bis.4a Step 2 uses |
| Paper 45 **§11, Theorem 11.1** (Paper 44 §9.4, §9bis W2, l.358) | **no** — withdrawn, Paper 45 §13 **W45.7** | ❌ MINOR-1 |
| Paper 45 **§12's `G_rad`** (Paper 44 §9.4 last sentence) | **no** — withdrawn, Paper 45 §13 **W45.8** | ❌ MINOR-1 |
| Paper 43 **Remark 9.5** (Paper 44 l.2973, 2979, 3009, 4675, 5454, 5558) | **does not exist**; Paper 43 has Theorem 9.5 and Remark 9.6, and neither poses the quoted question | ❌ **MAJOR-1** |
| Paper 43 Thms 9.1, 9.3, 9.4, Lemma 9.14a0, Thm 8A.7c, Def. 8A.7d, Thm 14.1, §14.0a–b, §14.1a, (9.5b), (9.11), (9.13) | all yes | ✅ |

### 1.4 Paper 43 → Paper 45 (the `[phase 132]` records)

| record | target exists? | verdict |
|---|---|---|
| Def. 8A.7d reason (iv) → Paper 45 Cor. 9.6a, Rem. 9.6b(3) | yes | ✅ — and non-circular: reasons (i)–(iii) stand independently and Cor. 9.6a's proof uses nothing from 8A.7d beyond the family (8.4) |
| §14.0 row `𝓝_∞^W = 0` → "declined by row C (Paper 45 §0.2, §14.3)" | yes | ✅ — but see MINOR-2, two other places in Paper 43 were not updated |
| §14.0 row `c_cut` → separated from the identity constant `c` | yes | ✅ |
| §14.1a `[phase 132]` block | yes, matches Paper 45 §14.3 item by item | ✅ |
| §13 W45.3 cited for the withdrawn `χ_A = Σ_pW_p+W_∞` assembly | W45.3 is the semilocal-assembly withdrawal; `χ_A` itself is named in W45.9 | ✅ (acceptable; both items withdraw the same construction) |

---

## 2. Conventions table

| convention | Paper 43 | Paper 44 | Paper 45 | agree? |
|---|---|---|---|---|
| carrier `C_S ≅ R^××∏_{p∈S_f}Z_p^×`, `\|x\|_S=\|x_∞\|` | Lemma 3.3, §14.0a | §1.2, Lem. 3bis.1 | (1.1), §1.2 verbatim | ✅ |
| `D_A = C_c^∞(C_S)`, `F^†(u)=\overline{F(u^{−1})}` | (3.6), (8.2) | §1.2 | §1.2 | ✅ |
| chart maps `j_p`, `j_∞` | (8.5) informal `(x at p, 1 elsewhere)`; (9.5b) normalized `j_p(p^kw)=(p^{−k}@∞, w@p, p^{−k}@rest)` | Prop. 3bis.2 uses the **(9.5b)** form | §5 uses the (9.5b) form | ✅ same class; ⚠ MINOR-8 (two formulas, reconciliation never stated) |
| `T = Σ_{v∈S}W_v + c·F(1)`, `c := 0` | (8.4) + Def. 8A.7d | §9.1 "Thm 3bis.7 with `c := 0`"; 8bis.4(i) | (1.2) `T(F)=Σ_vW_v`, `c:=0` | ✅ |
| `I_A(F,G) := T(F⋆G^†)` | Def. 9.2 | §8bis (C1) `I_A := T_∞(·⋆·^†)` | (1.3) | ✅ |
| radial class and profile sign `Γ_h(w)=h(−\log\|w\|_S)` | — | Def. 3bis.6 | Lemma 1.1: profile `t↦h(−t)`, `\widehat{Γ_h}(τ)=\hat h(−τ)`, supported on `𝔠_0` | ✅; the sign is harmless because every symbol is even in `τ` (Paper 43 Thm 9.7(a),(b)) |
| `M = (λ_−,λ_+)`, `λ_∓(F)=∫F\|u\|^{∓1/2}` | Thm 9.1 | (8bis.9): `M(Γ_g)=(∫ge^{s/2},∫ge^{−s/2})` | (1.6): `λ_−(Γ_F)=Φ_F(1)`, `λ_+(Γ_F)=Φ_F(0)` | ✅ **arithmetically checked**: `λ_−(Γ_F)=∫F(−t)e^{−t/2}dt=∫F(t)e^{t/2}dt=Φ_F(1)` |
| the swap | — | Thm 3ter.14(iii) `M(Frob_n)=(n^{1/2},n^{−1/2})` (mass at `\|w\|=1/n`) | Rem. 8.2: `M(Γ_F)=σ(z(F))`, old labelling refuted by counterexample; `β_T` is `σ`-invariant | ✅ **consistent**: 44's `M(Frob_n)` is exactly what 43's `λ_∓` gives on a mass at `1/n`; 45's correction is internal to 45 and contradicts no statement of 43 or 44 |
| `q = −B_nuc`, `I_∂ = −Q`, `(S2)` | (14.1) | (8bis.14a), (8bis.14e), no hedge | Lemma 1.3 (S1)(S2)(S3), all three reconciled, with the (C1) quantifier carried (round-3 `r7`) | ✅; the dependency chain `Lem 1.3(S3) → P44 (8bis.14e) → P44 8bis.4(ii) → P45 Thm 9.4 → (E1)–(E5)` terminates, and Thm 9.6 uses only leg (S1) |
| archimedean constants: `\hat W_∞(0,τ)=\logπ−Reψ(¼+iτ/2)`, `\hat W_∞(0,0)=\logπ−ψ(¼)≈5.372`, counterterm `γ+\log4π`, `K(t)=e^{−t/2}/(1−e^{−2t})`, `d^*x_∞=dx/2\|x\|` | (8.5∞), (8.5b), Rem. 8.6a, (9.12b), (14.2) | Thm 8bis.2, 8bis.4(iv)(a) | §1.5 table, Thm 7.4 (`γ+\log4π+ψ(½)=\logπ`) | ✅ numerically; ⚠ MINOR-3 (Paper 44 cites (14.2) where (9.12b) is meant) |
| `vol_{d^*x}(p^kZ_p^×) = \log p` | (8.5) declared | Thm 8bis.8: **unique given a universal Tate residue**, up to one global scale; Rem. 8bis.8b: chart-invariance does not force it | §1.6, §6: "not a stipulation of this paper"; Cor. 9bis.3 quotes 8bis.8b verbatim | ✅ — the hypothesis travels intact in all three |
| (C1) colimit quantifier | Thm 8A.7c is the mechanism | (C1) stated as a standing convention of §8bis | inherited verbatim, §1.2, with an explicit carve-out for `A` | ✅ |
| (C2) bare level-`N` convention | — | (8bis.0), no rate headlined | §1.2: no level-`N` normalization arises on radial classes; cites 44's Frobenius statements in the bare convention | ✅ |
| explicit formula | not used (A.10 forbids) | 8bis.4(ii): body says `PROVED-IN-REPOSITORY`, footer + §11 say `CLASSICAL` | Thm 9.4 `PROVED` here, Cor. 9.4a | ❌ **MAJOR-2** |
| Weil's criterion | — | 8bis.4(iii) / (8bis.10) `CLASSICAL`, colimit | Warning 8.5 cites it as (8bis.10), `CLASSICAL` | ✅ |
| Mertens | Thm 10.8b `CLASSICAL`, quarantined, counts toward no clause | cited nowhere (§11 says so) | (E8), `CLASSICAL`, quarantined, two uses, deletion test for both | ✅ |
| Chebyshev | — | Lem. 8bis.5 `CLASSICAL`, unspecified constant, used by no clause | not imported | ✅ |

---

## 3. Contradictions and quantifier mismatches

### FATAL
**None.** No statement of any paper is refuted by a theorem of another. In
particular the three places where a contradiction was plausible are clean:

* Paper 43 Thm 14.1 (`I_A` indefinite at every finite chart, `c=0`) versus
  row D's target (`I_∂ ≤ 0`): **no contradiction**, because the target is a
  colimit statement and all three papers say so at the point of use
  (Paper 44 (C1) and 8bis.4(iii); Paper 45 §14.4 item 1; Paper 43 §14.1 item 4).
* Paper 44 Thm 8bis.4a (positivity fails on `Q_fin` at every chart) versus
  Weil positivity: `Q_fin` is the **pure Frobenius** form, not the Weil kernel
  (Cor. 8bis.1d, Thm 8bis.1e). Paper 45 Warning 8.5 repeats the distinction
  correctly and never asserts the stronger reading.
* Paper 45 Rem. 8.2's ruling swap versus Paper 44 Thm 3ter.14: recomputed
  independently; the two are the same convention, and the swap corrects only
  Paper 45's own earlier text.

### MAJOR

**MAJOR-1 — a nonexistent citation carrying a `PROVED` ledger row.**
Paper 44 cites **"Paper 43 Remark 9.5"** six times (Thm 8.1(iv) at l.2973/2979,
§8 at l.3009, §9bis W3 at l.4675, the §10 clause ledger at l.5454, and §11 at
l.5558), attributing to it the question *"what the family's pairings equal in
terms of `Λ(n)`"*. **Paper 43 has no Remark 9.5.** It has Theorem 9.5
(`N_A ≠ 0`, `T` separates two sections of equal modulus) and Remark 9.6 (what
(9.5) does and does not establish) — and Remark 9.6 asks nothing about `Λ(n)`;
the quoted sentence appears nowhere in Paper 43. The `PROVED` row in Paper 44
§10 that reads *"'what the family's pairings equal in terms of `Λ(n)`' | Paper 43
Rem. 9.5 | `PROVED`: `contact_fin(Γ_n^{rad}) = Λ(n)n^{−1/2}`"* therefore
discharges an obligation attributed to a paper that does not state it. The
**mathematics is unaffected** (Thm 3bis.7 is true and is row B's own), but a
ledger row is anchored on a dangling reference, and W3 withdraws an answer to a
question that has no cited source. Either Paper 43 must be given the remark, or
Paper 44 must re-anchor the row on Thm 9.5/Rem. 9.6 or on row B's own framing.

**MAJOR-2 — the explicit-formula label is inconsistent in three places at once.**
The phase-132 cross-paper edit relabelled Paper 44 Thm 8bis.4(ii) from
`CLASSICAL` to `PROVED-IN-REPOSITORY (Paper 45 Thm 9.4)`. The relabel was
applied to the body of (ii), to §10.4 items 2 and 4a, to the §0 banner and to
one sentence of §11. It was **not** propagated to:

1. **Paper 44, Thm 8bis.4's own status footer** (l.3824): *"`PROVED` in (i),(iv);
   `CLASSICAL` in (ii),(iii); `OPEN` in (v)"* — still calls (ii) `CLASSICAL`;
2. **Paper 44 §11**, which still says the quarantined section has *"TWO, both
   `CLASSICAL`"* imports and lists them as *"(i) Weil's criterion **and the
   explicit formula**, Theorem 8bis.4(ii)–(iii)"*, immediately above the
   `[phase 132]` sentence that contradicts it;
3. **Paper 45 §14.3** itself, which describes what it imports from row B as
   *"Theorem 8bis.4 (the interface, (i) `PROVED`, **(ii)–(iii) `CLASSICAL`**)"* —
   i.e. Paper 45 records as `CLASSICAL` the very clause it relabelled in
   §14.5(a) and the very statement it proves in its own Thm 9.4.

This is a label contradiction in the strict sense of the mandate: one statement
carries two different labels in two papers and two different labels inside one
paper. No verdict moves either way (the clause is used by no clause of B, and C
proves it), but the import ledgers of both papers are currently wrong, and the
count "two classical imports" in Paper 44 §11 is stale.

### MINOR

**MINOR-1 — Paper 44 cites two withdrawn statements of Paper 45 as live.**
§9.4 and §9bis W2 discuss *"Paper 45 §11 (Theorem 11.1)"* in the present tense
and close with *"in particular Paper 45 §12's radial sector `G_rad` is exactly
the sector in which §3bis works."* Paper 45 §13 withdraws §11 in its entirety
(**W45.7**) and `G_rad` with Prop. 12.2 and Thm 12.3 (**W45.8**); Paper 43
§14.1a's `[phase 132]` block records both withdrawals. Paper 45 W45.7
acknowledges Paper 44 §9.4(a) as still correct *about the lift*, so the §11
discussion is defensible as history; the `G_rad` sentence is not — it asserts
a withdrawn object as the working sector of §3bis. Nothing rests on it.

**MINOR-2 — Paper 43 still assigns `𝓝_∞ = 0` to row C in two places.**
The phase-132 edit corrected the §14.0 obstacle row to *"declined by row C …
not claimed by any row."* But §13.8 (l.4816) still reads *"recorded here as
`CLASSICAL`, **belonging to row C**"*, and the §14.2 status blockquote (l.5211)
still reads *"`𝓝_∞ = 0` for the colimit (§13.8, `CLASSICAL`, row C)"*. Paper 45
§0.2 and §14.3 decline it explicitly. Internal contradiction in Paper 43,
contradicted by Paper 45; no clause depends on it.

**MINOR-3 — Paper 44 makes the exact mis-citation Paper 45 corrected in itself.**
Thm 8bis.4(iv)(a) and its proof cite *"Paper 43 (14.2)"* for the value
`\hat ω_∞(0) = \hat W_∞(0,0) ≈ 5.372`. (14.2) is a lower bound for
`m := \sup_{\hat C_S}\hat T` **including the finite places**; the exact
archimedean value is Paper 43 **(9.12b)**. The two numbers coincide only
because every finite-place term at `τ=0` is positive and (14.2) is written as
an inequality, so the argument survives; but the typing is wrong, and it is the
same error Paper 45 §1.5 records and repairs in round 3 (note `n7′` of
`R132.005`). Paper 44 was never corrected.

**MINOR-4 — "Paper 44 Theorem 9.1" does not exist.** Paper 44 §10.4 item 4a
(and `R131.019` §5) say *"Row C received **Thm 9.1** as its Thm 5.1."* Paper 44
has no Theorem 9.1; the prime packet is **§9.1**, whose content is Thm 3bis.7.
Paper 44 §9.1a itself and Paper 45 §14.3 both get this right ("§9.1").

**MINOR-5 — Paper 45 Cor. 9.6a quotes a sentence Paper 43 no longer contains.**
Cor. 9.6a's preamble says Paper 43 Def. 8A.7d *"says in terms that 'none of
[its four reasons] is a derivation'"*. After the phase-132 edit that Paper 45
itself authorized, Def. 8A.7d reads *"reasons (i)–(iii) are normalization
choices and are not derivations, and reason (iv) … **is** a derivation"*. The
quotation is stale (it was true of the phase-130 text). Harmless, but it is the
citing paper misquoting the cited one at the one joint where circularity would
matter; the non-circularity itself is fine, since Cor. 9.6a's proof uses only
Paper 43's family (8.4) and Paper 45 Thm 9.4.

**MINOR-6 — an over-conservative label in Paper 44.** Thm 8bis.7(b) is labelled
`CLASSICAL` (via 8bis.4(ii)–(iii)) for *"if RH fails then `Q(g) < 0` for some
primitive `g`"*, and cites Paper 45 Thm 10.4 in the same breath. Paper 45
Thm 10.4 **proves** exactly that statement in the repository (from `106_11`
Theorem 1 with the `C10` fix, plus imports (E2) last clause, (E3d), (E6)). So
(b) is `PROVED-IN-REPOSITORY`, not `CLASSICAL`. Errs on the safe side; noted
for completeness of the import ledger.

**MINOR-7 — Paper 44 §11 omits Paper 45 from its dependency list.** §11 lists
"Papers: Paper 43 … and its appendix" only, while §8bis.3–§8bis.4 substantively
cite Paper 45 Thm 8.1 (the polar packet drops on the primitive sector) and
Paper 45 Thm 10.4 (`Π`, sufficiency), and §10.4 now cites Paper 45 Thm 9.4.

**MINOR-8 — two formulas for `j_p`, never reconciled in print.** Paper 43 (8.5)
writes `j_p(x) :=` the class of `(x` at `p`, `1` elsewhere`)`; Paper 43 (9.5b)
and Paper 44 Prop. 3bis.2 write `j_p(p^kw) = (p^{−k}` at `∞`, `w` at `p`,
`p^{−k}` at every other place`)`. These are the same class — divide by the
`S`-unit `p^k ∈ Γ_S` and use the splitting of Lemma 3.3 — and every computation
in Papers 44 and 45 uses the normalized form. No paper states the reconciliation,
and a reader checking Paper 44 Prop. 3bis.2(ii) against Paper 43 (8.5) will
think the maps differ.

### Quantifier check (chart vs colimit) — clean

Every statement I could find that could be read at the wrong quantifier carries
its quantifier at the point of use:

* `I_∂ ≤ 0 ⟺ RH` is colimit in Paper 44 ((C1), 8bis.4(iii), *"at a fixed finite
  chart it is false"*) and colimit in Paper 45 (§14.4, Thm 9.6's chart clause
  with the explicit window and *"the identity is **false** at a chart"*).
* `𝓝 = 0` / `𝓝_∩ = 0` are fixed-chart in Paper 43 (Thm 9.8) and fixed-chart in
  Paper 45 (Thm 12.2, *"not claimed in the colimit"*).
* Thm 8bis.2 and 8bis.4a are fixed-chart, with the colimit version `OPEN` —
  stated identically in Paper 44 §10.4 item 3 and Paper 45 §14.4 item 2.
* (C1) is explicitly **not** carried into Paper 45 Def. 9bis.1a / Thm 9bis.2′
  (the continued Euler-product symbol `A`), and Cor. 9bis.3 proves the exchange
  fails. This is the subtlest quantifier in the corpus and it is handled
  correctly in both directions.

---

## 4. Withdrawal ledgers: are they respected?

| ledger | respected by the other papers? |
|---|---|
| **Paper 44 §9bis W1–W23** | **Yes.** W1–W3 (the `n−1` obligation) are honoured by Paper 45 W45.7, which deletes §11 rather than discharging it. W16 ("the Gram form of the Frobenius family is the Weil kernel") is honoured: Paper 45 §14.4 item 3 names the object as `Frob ⋆ Δ^{rad}` and says *"not the Frobenius Gram form"*. W19 is honoured: Paper 45 Warning 8.5 cites 8bis.4a (the proved chart failure), never the withdrawn symbol-comparison argument. W23 (`(Wgr)` false) is cited nowhere by 43 or 45. No paper cites W4–W15, W17, W18, W20–W22 as live. |
| **Paper 45 §13 W45.1–W45.16** | **Mostly.** W45.7 (§11/Thm 11.1) and W45.8 (`G_rad`) are still referenced by Paper 44 §9.4 — MINOR-1. W45.3 is correctly cited by Paper 43 Def. 8A.7d(iv) as the reason the former reason (iv) was replaced. W45.10 (the Hodge-index reading) is honoured everywhere: no paper reads row D's target as a Hodge index. W45.14 ("nothing in row C depends on `c`") is honoured — both Paper 43 §14.0 and Paper 45 §14.4 now treat `c` as load-bearing and derived. The withdrawn name `^{mer}` (W45.15) appears nowhere outside its ledger entry. |
| **Paper 43 §14.0 (the obstacle/not-claimed ledger)** | **Yes** by Paper 44 and Paper 45 — neither claims `𝓝_∞^W = 0`, a value for `c_cut`, non-invertible objects, net-independence of `I_A` on `N_A^{dist}×N_A^{dist}`, or effective descent along a stack covering. The only defect is **internal** to Paper 43 (MINOR-2). |

---

## 5. The handoff to row D: is the target stated identically?

**No — and one paper does not state it at all.** The three statements are
*compatible*, but they are not the same statement:

| paper | where | what it says |
|---|---|---|
| **43** | §14.1 items 1–5, Thm 14.1, §10 l.4550 | **states no target.** It hands row D three negatives (no Hodge-index shape; the chart/colimit window; the ruling plane is a quotient in `N_A` and a subobject only in `N_A^{dist}`) and the sentence *"the sign is row D's."* |
| **44** | 8bis.4(iii)+(vi), §10.4 | names the **object** — the Gram form of `Frob ⋆ Δ^{rad}`, i.e. the full Weil kernel `W_fin + ω_∞`, not the Frobenius form — and states the **biconditional** `I_∂ ≤ 0 on every primitive radial Γ_g ⟺ RH` as `CLASSICAL`, colimit, false at a chart. |
| **45** | §14.4 | states the **target** as the one-directional obligation `I_∂ ≤ 0` on every primitive radial class `Γ_g`, `g ∈ C_c^∞(R)`, **on the colimit `D_A^∞` with `T_∞`**, **on the trace with `c = 0`** (now a theorem, Cor. 9.6a), and proves *target ⟹ RH* in the repository (Thm 9.6 (9.10) + Thm 10.4), i.e. **without** using 44's `CLASSICAL` biconditional. |

So Papers 44 and 45 agree on the inequality, the sector, the quantifier and the
object; Paper 45 adds the normalization `c = 0` as a hypothesis that Paper 44's
(8bis.10) does not carry explicitly (8bis.4(i) does declare `c := 0`, so this is
a presentation gap, not a conflict), and Paper 45 replaces the `CLASSICAL`
biconditional by a proved implication in the direction row D needs. Paper 43 is
silent, by design. Recommendation to the panel: a single boxed statement of
row D's target, with `c = 0`, (C1) and the named object, should appear
identically in all three papers before row D opens; at present a reader of
Paper 43 alone would not know what row D is being asked to prove.

---

## 6. Assessment

The three papers do form **one consistent theory**. They share one carrier
(`C_S ≅ R^× × ∏_{p∈S_f}Z_p^×`, Paper 43 Lemma 3.3, §14.0a, quoted verbatim by
both others), one algebra and involution, one declared trace `T = Σ_vW_v` with
one normalization `c = 0` — declared in A, used in B, and *characterized* in C —
one intersection form `I_A(F,G) = T(F⋆G^†)`, one Tate pair `M = (λ_−,λ_+)` with
one hyperbolic `β_T`, one measure normalization `vol(Z_p^×) = \log p` carried
with its hypothesis (a universal Tate residue) intact through all three, one
kernel and one set of archimedean constants that I re-derived and found
numerically and structurally concordant, and one quantifier discipline: (C1) and
(C2) are stated once in Paper 44 and inherited verbatim by Paper 45, with the
chart/colimit distinction carried into the hypotheses of every theorem that
needs it — including the one place where it must *not* be carried (the continued
Euler-product symbol `A`). The sign conventions `q = −B_nuc`, `(S2)` and
`I_∂ = −Q` are reconciled explicitly in Paper 45 Lemma 1.3, whose dependency
chain I traced and found terminating. Every cross-paper citation I checked
resolves to a theorem that exists under that number, says what the citing paper
says it says, and is used within the hypotheses the citing paper assumes — with
the single exception of Paper 44's "Paper 43 Remark 9.5", which resolves to
nothing (MAJOR-1). No theorem of any paper refutes a statement of another; the
three places where a refutation looked possible (Thm 14.1 vs row D's target,
Thm 8bis.4a vs Weil positivity, the ruling swap) are each resolved by a
quantifier or a distinction that all three papers state at the point of use, and
the two withdrawal ledgers are honoured in substance, with two stale forward
references from Paper 44 into a version of Paper 45 that no longer exists
(MINOR-1). What is *not* yet one theory is the **import bookkeeping**: the
explicit formula currently carries the label `CLASSICAL` in three places and
`PROVED-IN-REPOSITORY` in five, across both Papers 44 and 45 (MAJOR-2), which is
precisely the kind of defect the closure protocol exists to prevent, even though
no verdict depends on it. My recommendation is that the label of Paper 44
Thm 8bis.4(ii) be propagated to its own footer, to Paper 44 §11, and to
Paper 45 §14.3; that "Remark 9.5" be resolved; that Paper 44 §9.4's `G_rad`
sentence be struck; and that row D's target be boxed identically in all three
papers. None of these is a mathematical repair, and I record no finding that
would withdraw or qualify any of the three `WEIL-STRENGTH-COMPLETE` labels.
