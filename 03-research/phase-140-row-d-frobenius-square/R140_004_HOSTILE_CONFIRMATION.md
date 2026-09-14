# R140.004 — Hostile confirmation, phase 140 (round 2)

*Hostile auditor: Claude Opus 5. Date 2026-09-13. Objects: `R140_003_BUILDER_ROUND2.md` (ledger),
`R140_001_BUILDER_ROUND1.md` with round-2 repairs in place (1388 lines, 43 bracketed notes),
`README.md`, `scripts/certify_chi.py`. Method: each of H1–H15 checked against the **current** text and
against the cited source lines; the two new theorems (D.23.12, D.23.13) and the two new corollaries
(D.24.11, D.24.12) re-derived from scratch; no builder file edited.*

**Verdict: CONFIRMED, with residue.** All 15 findings are accepted and repaired; none is contested;
two (H3, H8) are repaired by *reversing* the round's headline rather than by rewording it, which is the
honest disposition and the harder one. The FATAL is genuinely closed. I record **11 residues** (R1–R11),
none fatal, one of which (R11) bears directly on the phase-141 recommendation and should be settled
before the lead adopts it.

**Correction of my own record.** `R140_002`'s summary line said "1 FATAL, 7 MAJOR, 6 MINOR" while its
body lists H2–H9 as MAJOR, i.e. **eight**. The correct count is **15 findings = 1 FATAL + 8 MAJOR +
6 MINOR**. `R140_003` §0 inherited the wrong total ("14 findings", "7/7"); the dispositions are all
present and correct, only the arithmetic of the header is off. No mathematical consequence.

---

## 1. Per-finding status

| # | sev | status | verification performed |
|---|---|---|---|
| **H1** | FATAL | **CLOSED** | Definition D.22.4 now reads `L_S := ∏_{𝔓∈S_f}O_𝔓`, `𝔫L_S := ∏_𝔓 𝔓^{v_𝔓(𝔫)}O_𝔓` — the literal transport of `44/main.md:2668–2672`, which the repaired corpus-check quotes verbatim. "Projective `O_K`-module" deleted and replaced by the correct statement (a topological ring, an `O_K`-module through the diagonal). D.22.5 is re-proved **place by place**, and I checked each clause: (i) at `𝔓`, `π_𝔓^{v}` is injective on `O_𝔓`, cone ≃ `O_𝔓/𝔓^{v}` in degree 0, product over the finitely many `𝔓 | 𝔫` is `≅ O_K/𝔫` by approximation, order `∏N𝔓^{v_𝔓} = N𝔫` — **the hedge is gone and is no longer needed**; (ii) the local quotient `π_𝔪O_𝔓/π_𝔪π_𝔫O_𝔓 ≅ O_𝔓/π_𝔫` by division by `π_𝔪`, a non-zero-divisor — correct, and genuinely cheaper than round 1's Dedekind argument; (iii) follows; (iv) `\mathrm{Tor}_1^{O_𝔓}(O_𝔓/π^a,O_𝔓/π^b) ≅ O_𝔓/π^{\min(a,b)} ≠ 0` for `a,b ≥ 1` — correct (resolve `0→O_𝔓 →^{π^a} O_𝔓 → O_𝔓/π^a → 0` and tensor), and it specializes to Paper 44's `m=n=2` witness; (v) unchanged. **O-9 is genuinely closed.** |
| **H2** | MAJOR | **CLOSED** | Theorem D.24.5 is split exactly as prescribed: (i) `(⇒)` general `PROVED`; (ii) `(⇐)` under the displayed (D.24.5a) — which is precisely the inequality the proof delivers; (iii) the biconditional for `h⁰_□`, `χ ≤ 1/8`. The `ψ ≡ 0` counterexample is quoted in the note. I re-checked that (D.24.5a) at `ψ(a,b)=a⁺b⁺` is Theorem D.24.4's `g ≥ χ`, and that (AT-1)(ii), D.24.10(iv), D.24.11 and D.25 §3 now cite **(i)** only. |
| **H3** | MAJOR | **CLOSED, and exceeded** | Definition D.23.6 is rebuilt with `r` declared a *choice* that deletes `Λ_K(𝔫)N𝔫^{−½}`. New §D.23.3bis executes the blueprint's instruction. **Definition D.23.11 checked against Paper 44 line by line**: the entry `c_N(m,n)·W_{fin}(\{\log m−\log n\})·(h_m⋆h_n^†)(n/m)` is exactly the off-diagonal summand of (8bis.5)/Cor. 8bis.1d; `W_{fin}` on prime-power ratios with weight `(\log q)q^{−k/2}` is (8bis.2); the constant is (8bis.2b) with **§12 correction K1 carried correctly** (complement of the **intersection** `P(m)∩P(n)`, not of the union — I re-read K1 at `44/main.md:5829–5866`); "the diagonal does not exist" is Rem. 8bis.1c + Cor. 8bis.1b′. Theorem D.23.12's (A)/(B) rows are faithful to Cor. 8bis.1d, Thm 8bis.1e, Thm 8bis.1′ and Thm 8bis.4a; the FATAL screen and the closing blockquote carry **Remark 8bis.4b(3)** verbatim and correctly. (C)(i)'s rank-2 factorization `u⊗v+v⊗u` is correct. See residues **R2–R6**. |
| **H4** | MAJOR | **CLOSED** | D.23.8 is relabelled `RESTATEMENT` of `R138_001` Cor. D.15.4c on a sub-cone; the "central structural finding" blockquote is withdrawn; D.23.9's novelty is narrowed to the rank count and the phase-41 comparison; the W5 row of the Weil table now says "a property of the realization `r`". |
| **H5** | MAJOR | **CLOSED** | Recorded as the third correction of the blueprint (§0.3.3) with the `e_± ∉ D^W` citations; `F_1,F_2` declared `a_0`-dependent lifts, canonical mod `𝓝_∞`, with a one-line proof (two choices of `a_0` have the same `M` and the same vanishing zero data, so Theorem 11.11 puts the difference in `𝓝_∞` — correct). P46-10 now **extends** Prop. 14.1 and carries clause (iv). Residue **R7** (wording). |
| **H6** | MAJOR | **CLOSED, and correctly** | Lemma D.24.2 → Observation D.24.2: (i) `λ_{CC} < 1` in CC's units `PROVED`; (ii) the deficit stated as an explicit conditional on `\deg_{CC} = \deg`; (iii) **(U1)** the degree dictionary and **(U2)** `\dim_{\mathbb S}` vs a real functional, both `OPEN` and tied to Finding 13.8's own refusal. P46-14 withdrawn. Definition D.24.1 widened to `h_c(x) = 0` for `x ≤ −c''`, so (β) is now inside the class it is tested in. The added parenthetical — that (β) still fails **(b′)** by D.24.7 **independently of every unit convention** — is correct and is the right way to keep the withdrawal from over-rehabilitating (β). |
| **H7** | MAJOR | **CLOSED** | (AT-1)(ii) now concludes only "(c) implies a `Ξ_Q`-primitive-cone statement the corpus has not proved and that D.19.5 makes implausible"; the reason is stated in my own terms (non-primitive witness; `Π_P` multiplies each zero term by a non-sign-preserving complex factor; Paper 45 Thm 10.4 is a `ξ`-theorem); **(AT-1) now rests on (i)**, which is a theorem. O-17 opened. The added asymmetry with (AT-2) is **verified and true**: Paper 46 **Proposition 12.4B** is exactly the `Ξ_a`-primitive bridge (`46/main.md`, proof transports Paper 45 Thm 10.4 with `Π_P` of Lemma 12.4A), and Theorem 12.4 uses it. See residues **R8** (O-17 has a nearer template than the one recorded) and **R9** (a stale citation inside (AT-2)(iii)). |
| **H8** | MAJOR | **CLOSED IN FULL** | (1) Clause (ii) replaced by (D.23.5a); I re-derived it: (11.6) on `(E_0,τE_0)` and its transpose, summed, gives `I+I^{t} = 2(n^{½}+n^{−½})Φ_{E_0}(0)Φ_{E_0}(1) − T_n` — the displayed identity is exactly right. (2) The Euler-product sentence is **deleted**, with my reason (the translate law is the group law of `R`, which `Ξ_a` shares) stated as the reason; only a labelled `HEURISTIC` residue remains, and it says no identity is in hand. (3) **Theorem D.23.13 re-derived in full** — see §2. **O-16 withdrawn** everywhere (D.25 §5, open list, README, P46-15 now ships D.23.10 and D.23.13 as a pair "or the first reads as a target"). This is the strongest repair of the round. |
| **H9** | MAJOR | **CLOSED** | The proof of Theorem D.23.4 is restated for the order `O_{−D}`, proper ideals, `Cl(O_{−D})`, Chebotarev in the ring class field (Cox 7.7, 9.12), primes prime to the conductor; the explicit witness `Q = x²+5y²`, `r_Q(3) = r_Q(7) = 0 < r_Q(21) ≥ 1` (`21 = 1²+5·2²`) is adopted, so the existence claim is now checkable without Chebotarev. Statement unchanged, as it should be. |
| **H10** | MINOR | **CLOSED** | Cor. D.23.3 asserts a **surjective** monoid homomorphism, iso iff O-13; `Div_□^{(K)}` defined on the generators so nothing depends on O-13. |
| **H11** | MINOR | **CLOSED** | `Div_□ := Z·F_1 ⊕ Z·F_2 ⊕ ⊕_{n≥1}Z·Frob_n`, `Δ := Frob_1` a name. |
| **H12** | MINOR | **CLOSED** | The hedge is deleted (not patched) and its status as the symptom of H1 is recorded. |
| **H13** | MINOR | **CLOSED** | §0.4 and README say "illustrates"; the absence of a Lipschitz/interval bound, the minimizer not being a grid node, and the 0.13 s timing are all stated. Script unchanged and still exits `0` (re-run: grid min `0.127500`, `g(½,0) = g(0,½) = 0.125`). |
| **H14** | MINOR | **CLOSED** | Cor. D.23.9 now matches only **the lattice with its form**, lists the canonical-class mismatch, and carries Finding 13.8's refusal; P46-11 carries it verbatim. |
| **H15** | MINOR | **CLOSED** | (AT-1)(iii) reads "moot, and *a fortiori* unsatisfiable", and names Paper 46 §12.5's four substitutions as the step carrying Thm 12.3 across `𝒵`. |

**Contested: none. Reopened: none. Relabelled without warrant: none.** Every label that moved
(§4 of the ledger) is a *weakening* or a withdrawal, which is the direction an audit can confirm
cheaply; I checked each against its statement and found no upgrade smuggled in. Row D: **no label
change**, correct.

---

## 2. The four new results, re-derived

**Theorem D.23.12 (three Gram forms).** Rows (A), (B) verified against Paper 44 as above. (C)(i)
`I_∞(r(Frob_n),r(Frob_m)) = n^{−½}m^{½}+n^{½}m^{−½} = u_nv_m+v_nu_m` — rank ≤ 2, signature `(1,1)`
where `u,v` independent: correct. (iii)'s "complementary slices of one projector" is Theorem 8bis.1′,
correctly used. (iv) is the right disclaimer. **The reversal is warranted**: Paper 44 does prove,
unconditionally and at every finite chart, that positivity fails on the `W_{fin}`-form, and round 1's
message was the opposite. Residues R2–R6 concern precision, not direction.

**Theorem D.23.13 (orbit = Bochner = RH for the zeros `E_0` sees).** Re-derived:
* (i) `W(τ_uE_0,τ_vE_0) = Σ_ρ e^{(ρ−½)(u−v)}A_ρ = κ_{E_0}(u−v)` termwise, `A_ρ := Φ_{E_0}(ρ)Φ_{E_0}(1−ρ)`. **Correct**, and the termwise cancellation genuinely removes any rearrangement question.
* (ii) Castelnuovo on finite spans `⟺` `W(D) ≥ 0` for all **real** `(a_j)` `⟺` positive-definiteness. **Correct, but it needs one unstated step** — see residue **R9**: positive-definiteness in Bochner's sense quantifies over *complex* coefficients. It is true here because `κ_{E_0}` is **real and even** (`A_{\barρ} = \overline{A_ρ}` and `A_{1−ρ} = A_ρ`, `E_0` real, so `κ` is real; reindexing `ρ ↦ 1−ρ` gives `κ(−c) = κ(c)`), and a real symmetric matrix PSD over `R` is PSD over `C`. The two lines are missing from the proof.
* (iii) Sufficiency: `A_ρ = |Φ_{E_0}(½+iγ)|² ≥ 0` and `κ = \hat{}` of a positive discrete measure; `|κ| ≤ κ(0)` gives `|T_n| ≤ 2W(E_0)`. **Correct and unconditional.**
* (iv) Necessity. The step the coordinator asked about **holds**: `f_j(c) = Σ_{\mathrm{Re}ρ=β_j}A_ρe^{iγ_ρc}` converges **absolutely** (`Σ_ρ|A_ρ| < ∞` by Paper 46 (11.2)+(E3d), Theorem 11.3), hence **uniformly** on `R`, hence each `f_j` is Bohr almost periodic and bounded — this is the right class and it is the class `E_0 ∈ D^W` real automatically gives; no extra hypothesis on `E_0` is needed. Positive-definite `⟹` bounded by `κ(0)`; dividing by `e^{(β_1−½)c}` with `β_1 > ½` sends the `j ≥ 2` terms to `0` uniformly and forces `f_1(c) → 0` as `c → +∞`; a nonzero Bohr a.p. function cannot tend to `0` (its sup on every `[T,∞)` equals its sup on `R`); uniqueness of a.p. Fourier coefficients then gives `A_ρ = 0` on `\mathrm{Re}ρ = β_1`; downward induction, and `c → −∞` for `β < ½`. **Correct.** The hypothesis actually used is only that **finitely many distinct real parts occur among `\{ρ : A_ρ ≠ 0\}`**, which is exactly what is declared; the general case is honestly parked at O-15′ and is *not* needed for the withdrawal of O-16.
* **"RH for the zeros `E_0` sees" is stated precisely** — as `A_ρ = Φ_{E_0}(ρ)Φ_{E_0}(1−ρ) = 0` for every `ρ` with `\mathrm{Re}ρ ≠ ½`, not as "the zeros are on the line". That is the correct formulation and it is the one used.

**Theorem D.24.11.** `Φ_{r(D)}(ρ) = 0` for all `ρ` ⟹ `I_∞(E,r(D)) = Φ_E(0)Φ_{r(D)}(1)+Φ_E(1)Φ_{r(D)}(0)`,
a function of `M(E)` with `D`-dependent coefficients ⟹ the whole pairing family, hence `Ψ` of it,
factors through `M`. **Correct, and non-vacuous** (it covers `h⁰ = ψ(\deg E)`, `ψ(I_∞(E,K))`, and every
"Frobenius-Gram-aware" candidate built on `r`). It is the right generalization of D.24.7 and it closes
the obvious escape route.

**Corollary D.24.12.** First sentence — an `h⁰` satisfying (b′), `≢ 0`, cannot be constant on cosets
`E + (P^W ∩ C_c^∞)` — is exactly D.24.7's construction and is **correct** (the witness `F = Πg` lies in
`P^W ∩ C_c^∞`, so constancy on those cosets is all the argument consumes). Second sentence — "must read
`Z(E)` **through** the pairings `I_∞(E,X)` with `Z(X) ≠ 0`" — is **guidance, not a theorem**: see
residue **R10**.

---

## 3. Residues (none fatal; R11 is the one that gates phase 141)

| # | where | what | severity |
|---|---|---|---|
| **R1** | corpus check (D.22), last lines | Still says the new mathematics is *"(β) Theorem D.22.5(ii), whose proof needs invertibility of `𝔪` where `K = Q` needed nothing"* — but the repaired proof explicitly **does not** use invertibility (it divides by `π_𝔪` in a local ring). Stale sentence, contradicts the repair it accompanies. | MINOR |
| **R2** | Thm D.23.12 row (A); README; D.25 §2 | The unsignedness is Paper 44's `Q_{fin}(g) = ∫(g⋆g^†)dW^S_{fin}` on **real radial profiles** (8bis.10a); the object tabulated in the same row is the **discrete Gram matrix** `G^{Frob}_{mn}` of `\{Frob_n^{sm}\}`, whose diagonal does not even exist. They share the kernel `W_{fin}` but are not the same form, and the witness of 8bis.4a is not exhibited inside `span\{Frob_n^{sm}\}`. One clarifying sentence is needed, or the row should say "the `W_{fin}`-form" rather than "the Gram form of the family". | MAJOR (precision; the direction of the reversal is unaffected) |
| **R3** | §0.2, Thm D.23.12, D.25 §2, README | Remark 8bis.4b(**3**) is carried; **8bis.4b(1)** is not: 8bis.4a is a *fixed-chart* theorem and *"the colimit version is therefore `OPEN`, and is not asserted"*. Since the sign question lives in the colimit (convention (C1), Thm 8bis.4(iii)), every occurrence of "unsigned" should carry "(at every finite chart; the colimit statement is `OPEN`)". The text does say "at every finite chart" consistently — what is missing is that the colimit is open, not merely unaddressed. | MINOR |
| **R4** | Thm D.23.12(ii) | *"(A) has infinite rank and is sparse"* — only sparsity is argued. Infinite rank is plausible but unproved, inside a `PROVED` theorem. Prove it or delete the clause (D.25 §2 repeats it). | MINOR |
| **R5** | Thm D.23.12(iii) | Phase 136's triple is misquoted: the source (`PHASE_136_MAP_SYNTHESIS_AND_PLAN.md:64–66`) says an `h⁰` must couple through an object that *(i) is not model-uniform, (ii) grows quadratically, (iii) reads unimodularity* — not "support growth, bigrading, unimodularity". | MINOR |
| **R6** | Def. D.23.11 | Omits Cor. 8bis.1d's hypothesis on the level: the off-diagonal archimedean block vanishes only for `N` large enough that `s^N ∤ (n−m)` for some `s ∈ S_f∖(P(m)∪P(n))`, which needs `S_f ⊋ ⋃P(n)`. Without it, (8bis.2a) does not vanish and the entry is not (D.23.7). | MINOR |
| **R7** | Def. D.23.6, the `a_0` blockquote | *"the two `K_{odd}` differ by a class of `𝓝_∞`? — **no**: they differ by … hence … exactly by an element of `𝓝_∞`"* — the rhetorical "no" contradicts the sentence it introduces. Content is right; wording inverts it. | MINOR |
| **R8** | O-17 | The route recorded ("Landau on `Π_P`-images") is mine and is the longer one. The **nearest template is Paper 46 Proposition 12.4B**, which already transports Paper 45 Theorem 10.4 to a non-`ξ` member of `𝒵`; for `Ξ_Q` one takes `P = \{0,1\}`, `Π_P = Π` (rank 2, Paper 45's own operator), and the two checks to make are named there: (a) the quartet representative needs `x_0 = γ_0 ≠ 0`, i.e. **choose a non-real Davenport–Heilbronn zero** — available, and `Ξ_Q`'s *real* zeros in `(0,1)` (R139 D.19.4a) are then irrelevant, though they are exactly why Lemma 12.4A(v)'s argument cannot be copied verbatim; (b) the strip on which `106_11`'s estimates (15),(16),(27),(29) are read must be widened to `\max_ρ|\mathrm{Re}ρ−½|` for `Ξ_Q`, as §12.4B does for `½+a`. Recording this makes O-17 a two-check task rather than an open-ended one — and if it closes, (AT-1)(ii) returns to a **refutation**. | MAJOR (constructive; not an error) |
| **R9** | Thm D.23.13(ii); (AT-2)(iii) | (a) The Bochner step needs the unstated lemma "`κ_{E_0}` is real and even" (two lines, proved above). (b) (AT-2)(iii) still says (c) is *"equivalent to"* `W_a ≥ 0` — after H2's split it is *implies* — and still cites `R138_001` Thm D.15.4, whose witness `F_u = τ_uK_a+τ_{−u}K_a` is **effective and not `Ξ_a`-primitive**, i.e. the same defect H7 removed from (AT-1)(ii). The claim survives because Prop. 12.4B + Thm 12.4 **do** supply the primitive statement; the citation should be to those alone. | MINOR |
| **R10** | Cor. D.24.12, second sentence | *"must read `Z(E)` through the pairings `I_∞(E,X)` with `Z(X) ≠ 0`"* does not follow from the proof: what is proved is that `h⁰` must separate equal-bidegree classes with different zero data. That it must do so *through `I_∞`-pairings* is a design choice (an `h⁰` could read `Z(E)` through any zero-free functional of `E⋆X^∨`, or through a nonlinear explicit-formula expression). Label the second sentence `HEURISTIC`/guidance; the first is `PROVED`. | MINOR |
| **R11** | O-14′ and D.25 §7 | **O-14′ is not yet well-posed.** "An `h⁰` reading family (A)'s arithmetic Gram entries" cannot be taken literally: `G^{Frob}_{mn}` are **constants** depending on `(m,n)`, not functions of `E`, so no `h⁰` can be a function of them. The intended object must be `h⁰(E) = Ψ\big((I_A(E,\,Frob_n^{sm}))_n\big)` — pairings of the **class** against the arithmetic family — and that formulation carries quantifiers the round has not fixed: the chart `S`, the level `N`, the smearing `ε` (Paper 44's entries depend on all three, and `I_A(Frob_n,Frob_n)` does not exist at all), and the colimit convention (C1). Until O-14′ names those, it is a slogan. Pair it with Cor. D.24.12's *proved* half, which is the real statement of what is needed. | MAJOR (blocks adoption of the phase-141 target as written) |

---

## 4. Assessment of D.25 and of the phase-141 recommendation

**D.25 as rewritten is accurate.** §1 (what the tensor idea buys) now carries H5's correction and H6's
withdrawal; §2 is the new three-Gram-form picture and is the honest replacement of round 1's headline;
§3 is unchanged and is the durable part; §4 states D.24.11/D.24.12 correctly modulo R10; §5 withdraws
O-16 with the reason proved rather than asserted; §6 ("what must not be repeated") is the best page of
the phase and its last bullet — *"do not set a phase-141 target whose statement is Weil positivity
restricted to a subspace or an orbit; Theorem D.23.13 is the test to run"* — is exactly the right
protocol to hand forward.

**On the recommendation itself I dissent in emphasis, on T2 grounds.** D.25 §7 recommends **O-15** (the
moment cone `𝔐`) as the phase-141 target, with O-14′ second and O-17 as prerequisite. But:

1. **O-15 is model-uniform.** `𝔐 = \{(M(E'),Z(E')) : E' ≥ 0, E' ≢ 0\}` is defined from `D^W`, `M`,
   `\{·≥0\}` and the zero set — every item of the data list `𝔇` of Transfer Lemma D.19.7c. By **T2**
   (`R139_001` §D.19.7), a description of `𝔐` that is uniform over `𝒵` cannot by itself yield (b′) for
   `ξ`, because it would yield it for `Ξ_Q` too, where Theorem 12.3 would then give a positivity that
   R139 D.19.5 contradicts. So O-15 can be a **tool** — a good one, and genuinely classical-looking —
   but it cannot be the step that carries the sign, and D.25 §7 should say so. (The round's own
   §6 rule and Cor. D.19.7d both point this way; the recommendation does not draw the inference.)
   Minor related overstatement: O-15 is described as "with no zero named", but `𝔐`'s second coordinate
   is *indexed by* `Z(ξ)`. It does not *use* the location of the zeros, which is the defensible claim.
2. **O-14′ is the one that can satisfy clause (N)**, because family (A)'s entries are `Λ(q^k)q^{−k/2}`
   — that is A8, read directly — and it is the only surviving candidate not excluded by D.24.7 or
   D.24.11. It should be **first**, not second. It is also the one blocked by **R11**: it must first be
   stated as a functional of `(I_A(E,Frob_n^{sm}))_n` with its chart/level/colimit quantifiers fixed.
3. **The 8bis.4a warning is correctly respected.** D.25 §4's last sentence — *"Theorem 8bis.4a says
   positivity fails on (A)'s own form at every chart, so an `h⁰` built on (A) cannot inherit a sign
   from it"* — is the right and non-optimistic reading, and it should travel with O-14′ verbatim, now
   also carrying R3 (the colimit statement is `OPEN`, so the warning is a chart warning).

**Recommended order for the lead:** O-14′ (restated per R11, carrying the 8bis.4a warning and T2's
requirement that the definition read A8 essentially) → O-17 (per R8, a two-check transport of
Prop. 12.4B, which would restore (AT-1)(ii) to a refutation and give the falsifier side its teeth) →
O-15 as a tool, explicitly *not* as the sign-carrying step.

---

## 5. Per-item verdicts (round 2)

| item | verdict |
|---|---|
| **D.22** | **CONFIRMED.** The FATAL is closed by the correct definition and a correct place-by-place proof; O-9 is genuinely closed. Residue R1 (stale sentence in the corpus check). |
| **D.23** | **CONFIRMED.** D.23.1–D.23.10 stand as re-derived in round 1's audit, now with the right labels (D.23.8 `RESTATEMENT`, D.23.6 a declared choice, `F_1,F_2` mod `𝓝_∞`, H9's ring-class-group proof, H14's qualifications). §D.23.3bis and Theorem D.23.12 are new, faithful to Paper 44, and reverse the round's headline in the direction the sources require. Theorem D.23.13 is correct and is the decisive result of round 2. Residues R2–R7, R9(a). |
| **D.24** | **CONFIRMED.** D.24.5's split is correct; the CC withdrawal is correct and correctly scoped (β still fails (b′) unconditionally); (AT-1)(ii) is honestly weakened; D.24.4, D.24.6, D.24.7, D.24.9, D.24.10 unchanged and intact; D.24.11 is a genuine strengthening of D.24.7 and closes the obvious escape. Residues R8, R9(b), R10. |
| **D.25** | **CONFIRMED as synthesis; the *recommendation* needs one edit** — the T2 status of O-15 and the precedence and restatement of O-14′ (R11 and §4 above). |
| **labels / FATAL screen / corpus check / paper-facing list / README** | **CONFIRMED.** Screen clean and now also carries 8bis.4b(3). Every moved label is a weakening or withdrawal and each matches its statement. The corpus check is extended to the four Paper 44 theorems it had skipped. The paper-facing list is consistent with the repairs (P44-4 unblocked, P46-10 extends rather than replaces, P46-11 carries Finding 13.8, P46-13 carries the split, P46-14 withdrawn, P46-15 ships the D.23.10/D.23.13 pair, P46-17 new, P44/46-16 carries H9). README's one-line answer is now accurate and the withdrawal blockquote is prominent. |

## 6. Overall

**CONFIRMED, with residue.** Round 2 accepts every finding, contests nothing, repairs the FATAL
correctly, and — in the two places where the audit struck at the round's message rather than its
wording (H3, H8) — reverses the message and proves the reversal (Theorem D.23.12) or proves the
withdrawal (Theorem D.23.13) instead of hedging. That is the disposition an audit can confirm.

The phase's durable output is now: **Theorem D.24.7 + Theorem D.24.11** (no `h⁰` reading only
bidegrees, or only the Pólya-Frobenius pairings, satisfies (b′)); **Theorem D.24.4**
(`χ = 1/8`); **Proposition D.24.3a** (growth `(r²/4)m²`, every number field); **D.22** (the ideal-indexed
Frobenius family and its shadow over every `K`, O-9 closed); **Theorem D.23.12** (the three Gram forms,
and that the Euler product's own form is arithmetic and unsigned at every chart); and **Theorem D.23.13**
(the orbit test that disqualifies Weil-positivity-in-disguise targets). Row D: **no label change**,
and none is warranted.

**Residue to carry into the lead's decision:** R1–R10 as editorial/precision items (R2 and R8 worth a
paragraph each), and **R11 as a gate**: O-14′ must be restated as a functional of
`(I_A(E,Frob_n^{sm}))_n` with its chart, level and colimit quantifiers fixed before it can be adopted
as the phase-141 target, and D.25 §7 should record that O-15, being model-uniform, cannot by T2 be the
step that carries the sign.
