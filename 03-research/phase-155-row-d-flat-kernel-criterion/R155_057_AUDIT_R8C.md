# R155_057 — Audit of R155_054 (round 8c, P7: the D-HS kill)

Object: `R155_054_ROUND8C_P7_DHS_KILL.md`.
No compute. Every citation below was opened at the stated line; `P46` = `04-papers/46-intersection-frame-defect/archive/main.md`,
`P44` = `04-papers/44-row-b-arithmetic-family/main.md`, `LN` = `03-research/phase-136-row-d-map/NOTE_OFF_THE_PAGE_CANDIDATES.md`,
`R140` = `03-research/phase-140-row-d-frobenius-square/R140_001_ROUND1.md`, `PTD` = `05-meta-and-planning/ABCD-CLOSURE-PLAN/PATH-TO-D.md`.

Verdict scale: PASS (correct and correctly cited), AMEND (conclusion stands, statement or proof needs the listed repair),
FAIL (statement false or unproved as labelled).

## 0. Citation check (all cited theorems opened)

| memo cites | found at | matches memo's use? |
|---|---|---|
| Thm 12.3 uses `h⁰` only at `nF`, `K−nF` | P46:2744-2797, Steps 2–3 | yes (Step 2: `h⁰(K−nF)`, Step 3: `h⁰(nF)`; (c) invoked at `E = nF` only) |
| Thm 12.4 | P46:3006-3017 | yes |
| Thm 13.6(i),(ii) | P46:3511-3521 | yes |
| CC formula `⌈(deg D+log2)/log3⌉ − 1_L` | P46:3353-3360 | yes |
| Thm 19.2 (Serre symmetry, bilinearity only) | P46:5930-5943 | yes; `R(E) = ½I_∞(E,E) − ½I_∞(E,K) + χ` at P46:5917-5920 |
| Lemma 19.20 (`F_0` odd, `deg F_0 = 0`) | P46:6205-6213 | yes |
| Thm 19.23 statement | P46:6292-6300 | yes, `t > 0` is in the statement; conclusion is "no `E' ≥ 0`, `E' ≢ 0`, `E − E' ∈ 𝓝_∞`" |
| Thm 19.25 proof, Steps 1–3 | P46:6332-6351 | yes |
| Remark 19.26 bullets 2–4 | P46:6353-6367 | yes, quoted accurately |
| Thm 19.30 + table | P46:6463-6489 | yes |
| Def 19bis.14 / Thm 19bis.15 | P46:6972-6996 | yes |
| Thm 19bis.17, 19bis.19, Lemma 19bis.18, Thm 19bis.22 | P46:7068, 7112, 7122, 7185 | yes |
| Thm 20.19, Thm 20.23 | P46:7719, 7866 | yes; **20.23 is about `B4^{g,0}` specifically** (see Ev-4) |
| Thm 21.15, 21.16, Remark 21.16a | P46:8796-8850 | yes |
| §28.4 six clauses | P46:11956-11973 | yes |
| Thm 11.13, 11.14(ii) | P46:2542-2552, 2560-2578 | yes; **11.14(ii) is two-sided: `|I_∞(E,F)| ≤ C_F deg E`** |
| Thm 11.7(i) `K` even, `> 0` | P46 (Def–Thm 11.7) | yes |
| Thm 11.8(iii) "Frob_n acts as `τ_{log n}`" (memo §1.1) | P46:2247-2250 | **loose**: 11.8(iii) is the bidegree identity `M(τ_aK) = ½(e^{a/2},e^{−a/2})` matching `M(Frob_n)`; the identification of the action is the text at P46:3350-3351 and Thm 14.3(ii). Minor AMEND. |
| P44 Def 3ter.1–3ter.2, Prop 3ter.5, Thm 3ter.6(ii),(iii),(iv) | P44:1440-1470, 1541-1551, 1554-1580 | yes |
| R140 Prop D.24.10 | R140:1121-1136 | yes: "(b′) refuted, RH at (c)" via D.24.5/D.24.7 |
| phase-140 README:58 | README:58 | yes: "D.24.10 … refuted, PROVED" |
| PTD `:189`, `:328` | PTD:189 (row (vi)), PTD:324-333 (P7) | **partly**: see §6 |

## 1. Corollary 1 (the primary kill by Theorem 19.25) — AMEND

**What passes.** Theorem 19.25 quantifies over every `h⁰ : D^W → R_{≥0}` (P46:6332-6334) and its proof uses (b′), (c), `deg`,
`K`, `𝓝_∞`, and the witness of Theorem 19.23, nothing about how `h⁰` is built (P46:6337-6351). For an `h⁰` defined on `D^W`
and asked to satisfy (a),(b′),(c) with the nonnegative cone, Corollary 1 is a one-line specialisation and is `PROVED`
given (X19). D-HS as written (LN:44 "T3. Prove (b′): `h⁰(E) > 0 ⇒ E ≡ E' ≥ 0 mod 𝓝_∞`"; LN:45 T4 = (c) on `mK`, `K−nF`)
asks for exactly these clauses. **PASS on this reading.**

Detail: Step 2 of Theorem 19.25 does not actually need Serre symmetry — (c) at `E` with `h⁰(K−E) = 0` gives `h⁰(E) ≥ R(E)`
directly. Harmless; the memo repeats P46's decoration.

**Attack (domain).** The memo's §1.1 proves "a larger domain is irrelevant" (PASS: Theorem 12.3 reads `h⁰` only at `nF`
and `K−nF`, P46:2777-2797) but then concludes "the domain of D-HS … is `D^W`" (memo:44). That is too strong in the other
direction. The **minimal** domain on which Theorem 12.3 can be run is `𝒢_min := {nF, K−nF : F ∈ C_c^∞ primitive}`, contained
in `C_c^∞ ⊕ RK`. The witness of Theorem 19.25 Step 3 is `E = tF_0 + dK` with `F_0(u) = e^{−u²/18}sin(γ_1u)` (P46:6203),
which is **not compactly supported**, so `E ∉ C_c^∞ ⊕ RK`. An `h⁰` defined only on `C_c^∞ ⊕ RK` (which does contain `K`,
so the memo's dismissal "a smaller one does not contain `K`", memo:45, does not cover it) satisfies the hypotheses of
Theorem 12.3 and is **not literally** in the range of Theorem 19.25. P46 has a compactly supported witness only for `Ξ_a`
(Theorem 19.15, P46:6134-6136, `F_+` of Prop 12.4B); for `ξ` no compactly supported witness is on record (grep of P46 for
truncation of `F_0`: none).

Repair (not in the memo, not in P46): a truncation lemma — `F_R := F_0·χ_R` with a smooth cutoff at `|u| ≤ R`; `C_{F}` is
controlled by (11.17), `Σ_ρ|Φ_F(1−ρ)|`, which by (11.2)+(E3d) is continuous in the `C²`-weighted norm of `D^W`, and
`F_0 − F_R` and its two derivatives are `O(e^{−R²/18}·poly(R))`; the margin `G(1−s_1) = 5.79×10^{−3}` (P46:6288) is fixed,
so some finite `R` gives `C_{F_R} < \sqrt{W_{F_R}/2}` and Theorem 19.23 runs with `F_R ∈ C_c^∞ ⊂ 𝒢_min ⊕ RK`. Elementary but
**must be written**, and it re-enters the computer-assisted layer through the constants (`s_1`, `L`). Alternatively the memo's
Lemma 3 (§2.3) closes the small domain without (X19) — but Lemma 3 is **reading-dependent** (it needs the fibrewise factoring
(2.1)), so the "definition-free" kill (memo:227) is definition-free only on `D^W`.

**Verdict: AMEND.** Corollary 1 `PROVED` for `h⁰` on `D^W`; for `h⁰` on `C_c^∞ ⊕ RK` it needs the truncation lemma
(one paragraph, to be added) or falls back on the reading-dependent Lemma 3.

## 2. Evasion clauses

### (Ev-1) domain — AMEND
Same as §1: "larger domain irrelevant" PASS; "smaller domain impossible" not shown for `C_c^∞ ⊕ RK`.

### (Ev-2) different degree `deg'` — AMEND (conclusion holds, hypothesis list incomplete)
(i) *Is Theorem 19.23's conclusion degree-free?* **Yes.** The statement at P46:6294-6296 is "there is no `E' ∈ D^W` with
`E' ≥ 0`, `E' ≢ 0`, `E − E' ∈ 𝓝_∞`": it mentions the nonnegative cone and `𝓝_∞` only. `deg` enters the *proof*
(`deg E' = d` via Theorem 11.13(ii),(iv), then Theorem 11.14(ii)) as a tool, as the memo says (memo:83-85). PASS.

(ii) *Sign of `t`.* Theorem 19.23 is stated for `t > 0` (P46:6294). Its proof uses Theorem 11.14(ii), which is the two-sided
bound `|I_∞(E,F)| ≤ C_F deg E` (P46:2576-2578), so the proof is symmetric under `t ↦ −t` (`|t|W_{F_0} ≤ C_{F_0}d`). The memo's
symmetry claim (memo:82-83) is correct, though its stated reason ("bounds `|Im Φ_E(ρ_1)|`") is a paraphrase; the actual
mechanism is the absolute value in 11.14(ii). PASS.

(iii) *Missing property.* The memo says Theorem 12.3 "needs of a degree only" positivity on nonzero nonnegative classes and
constancy on `𝓝_∞`-cosets (memo:79-80). **False as a list**: Step 4 of Theorem 12.3 (P46:2793-2797) also needs
`deg'(nF) = 0` for primitive `F`, i.e. **`deg'` vanishes on the primitive space `P^W`** (Theorem 11.13(iii) for the frame's
`deg`). Without it the transfer theorem D-HS wants to feed has no Step 4, and there is no RH to obtain. With it,
`deg'` factors through `D^W/P^W ≅ R²`, i.e. `deg' = αa + βb` with `(a,b) = M(E)`, and positivity on the nonnegative cone
(where `a,b > 0`, Lemma 19bis.18) forces `α,β ≥ 0`, not both `0`. Then `deg' K = (α+β)/2 > 0` and
`deg' F_0 = (α−β)η`, `|η| < 10^{−390}` (Lemma 19.20(ii), P46:6206), so Step 2's requirement `deg'(K−E) < 0` on the witness
holds for `d ≥ 2` with **no** sign choice and **no** parity argument. The memo's fallback "`F_0` odd ⇒ `deg' F_0 = 0` for even
weight" (memo:83) is correct but unnecessary once the third property is recorded; and the memo's general "linear `deg'`"
(memo:77-78) without the third property does not evade *because it does not run Theorem 12.3 at all*.
**Verdict: AMEND** — add the third property; conclusion (no evasion) holds and becomes cleaner.

### (Ev-3) different canonical class `K'` — AMEND (sign and witness correct; one inequality mis-stated)
Linearity: `R'(E) − R(E) = −½I_∞(E,K'−K)` from `R(E) = ½I_∞(E,E) − ½I_∞(E,K) + χ` (P46:5917-5920). Correct, linear in `E`.
Sign: irrelevant, since only `|R'−R| = O(d)` is used. `t = O(d)`: from `t²W_{F_0} < d²/2 − d/2 + 2χ` (P46:6294),
`t < d/\sqrt{2W_{F_0}}(1+o(1))`. Correct.

**Error.** The memo writes `R(E) − 0 ≥ ¼d²(1−s_1²) − O(d)` for "the witness family" (memo:92). Theorem 19.23 admits **any**
`t` in the open window `s_1²d²/2 < t²W_{F_0} < d²/2 − d/2 + 2χ`; `R(E) = ½(d²/2 − t²W_{F_0}) − d/4 + χ` (Thm 19.21(i),
P46:6262) ranges over `(0, ¼d²(1−s_1²) − d/4 + χ)`, and at the top of the window `R(E) → 0⁺`, where an `O(d)` shift can kill
`R'(E) > 0`. The inequality holds only for `t` chosen near the **bottom** of the window, `t²W_{F_0} = s_1²d²/2·(1+ε)` — which is
available, so the argument closes, but the choice must be stated. Remark 19.26 last bullet (P46:6363-6367) says "the gap grows
like `d²(1−s_1²)`", also at optimal `t`.

Step 2 with `K'`: `h⁰(K'−E) = 0` by Step 1 needs `deg(K'−E) = deg K' − d ≤ 0`, i.e. `d ≥ deg K'`; memo has it (memo:93).
Step 3: `R'(E) > 0` at the chosen `t` for `d` large. Serre symmetry for `R'` (memo:89-90): true by Theorem 19.2's proof
(P46:5932-5934), and not needed (see §1). **Verdict: AMEND** (specify `t`); no `K'` evades.

### (Ev-4) different cone in (b′) — FAIL as `PROVED`; AMEND to the honest statement
The memo's two cases (memo:101-109) are **not exhaustive** and case (ii) mis-cites §20.

* Case (i) — `𝓔_HS ⊆ {E ≥ 0} + 𝓝_∞` — is labelled `DIAGNOSTIC` (memo:105) and rightly so: the divisor of a nonzero section is
 `div(σ) + D|_{y_0}`, which is *linearly equivalent* to `D|_{y_0}`, not equal (cf. Theorem 21.16(b′), P46:8818-8820); the
 memo's positive-operator averaging (P44 Prop 3ter.5, P44:1541-1551, correctly cited) shows an average of effective fibre
 divisors is a nonnegative radial density, but the step "fibrewise linear equivalence assembles to `𝓝_∞`-equivalence on the
 square" is not argued. Under this inclusion the B3 row of Theorem 19.30's table (P46:6489) refutes at once. PASS as
 `DIAGNOSTIC`, not as `PROVED`.
* Case (ii) — the memo says "B4 or something containing extreme classes: §20 applies … `(b′)_{B4}` ⟺ RH (Theorem 20.23)".
 Theorem 20.23 (P46:7866-7876) is an equivalence for **`B4^{g,0}`** specifically, and Theorem 20.19 (P46:7719) is (T2_cone)
 failure for **`B4^g`** specifically. Theorem 19.30 (P46:6465-6475) for an *arbitrary* cone with (T1_cone),(T2_cone) gives
 only the **necessary** condition `C'_{F_0} ≥ G`; it refutes cones with `C'_{F_0} < G` and says nothing about cones with
 `C'_{F_0} ≥ G` other than B4. A hypothetical `𝓔_HS` with `C'_{F_0} ≥ G`, (T2_cone), and `𝓔_HS ≠ B4` is a third case the
 memo does not treat, and "evasion by cone enlargement costs RH as input" (memo:109) is proved only for B4.
* Missing evasions, for the record: (Ev-5) a different pairing `I'` in (c) — then Theorem 12.3's conclusion is not
 `I_∞(F,F) ≤ 0` and Paper 45 Theorem 10.4 does not deliver RH: not an evasion but an abandonment of the target;
 (Ev-6) a larger equivalence `𝓝' ⊋ 𝓝_∞` in (b′) — Theorem 12.3 Step 2 needs `I_∞(·,H')` constant on `𝓝'`-cosets, i.e.
 `𝓝' ⊆ rad I_∞ = 𝓝_∞` (Theorem 11.11, P46 (11.14)): impossible; a smaller `𝓝'` makes (b′) stronger and Theorem 19.25 applies
 verbatim. One line each; both close.

**Why this does not save D-HS.** LN §1 T3 (LN:44) states (b′) with the **nonnegative** cone; D-HS as proposed has no other
cone, and the memo says so (memo:110). So D-HS is killed by Corollary 1. But the sentence "the only open-ended one, the cone,
is Horn B, where enlargement either fails Theorem 19.30 or is RH" (memo:234-235) is **not proved** and is not what P46 says:
P46 §19.9 records B4 as the one survivor of Theorem 19.30's test (P46:6491) and §20 as the transport of the sign problem onto
`(b′)_{B4}` (P46:7878-7880). Horn B is a residual of the **frame**, open before this memo and open after it; D-HS neither
supplies nor closes it. **Verdict: FAIL as `PROVED`; AMEND to: "(Ev-4) is Horn B; D-HS proposes no cone beyond the nonnegative
one; Horn B remains as recorded in P46 §19.9/§20."**

### §28.4 check of the evasion clauses — PASS
Correct: (Ev-1)–(Ev-4) modify the frame; §28.4 (P46:11956-11967) asks for a new object with six properties.

## 3. Radial collapse (T1, T2) — AMEND

**(2.1) `E|_{y_0} = y_0·E|_1`.** The fibre over `y_0` of the graph of a group homomorphism `x ↦ nx` is the preimage
`{x : nx = y_0}`, a translate of the fibre over `1`. PASS as stated, with two corrections of notation: (α) in the class space
the multiplier is the **integral idele class** `c_n`, `|c_n|_S = 1/n` (P44 Def 3ter.2, P44:1462-1466), not `n ∈ Q^×`
(principal, trivial on the class space); LN's "`ny_0`" (LN:36-37) and the memo's `(x,nx)` inherit the same looseness;
(β) `Frob_n` is the **Haar measure of the coset** `c_nK_{P(n)}` (P44:1466), so "graph of `Frob_n`" is a graph only after
`K_{P(n)}`-averaging — the memo's Lemma 2(iii) handles exactly this.

**Lemma 2(ii): "the base `Γ_S ≅ R` is a single orbit".** **Wrong base.** The fibration of LN §1 is over the second factor of the
`S`-square, whose points are classes `y_0 ∈ C_S`, and `C_S ≅ R_{>0} × K^♮` with `K^♮ = {±1}×∏_{p∈S_f}Z_p^× = ker|·|_S`
(P44 Prop 3ter.5 proof, P44:1548-1549, citing Lemma 3bis.3b). `τ_a` moves only the modulus; `Frob_n`-transport translates by
`c_n` and averages over `K_{P(n)}`. So the joint action of `{τ_a} ∪ {Frob_n}` is transitive on `R_{>0}`, and compatibility
with all `Frob_n` forces `∏_pZ_p^×`-invariance (Lemma 2(iii), correct: `Δ^{(n)}` is an idempotent by Thm 3ter.6(ii)), but
**nothing acts on `{±1}`**. The base modulo compatibility is `R_{>0} × {±1}`: **two orbits, not one**, unless the classes are
declared even in the sign coordinate. The memo's `Γ_S ≅ R` is the *modulus quotient* of the base, not the base. Consequence:
`h⁰_HS(E) ≤ 2·dim_S H⁰(E|_1)`, still `O(m)`. The "two-factor with archimedean place" question of the task: the archimedean
factor of `C_S` is exactly the `R_{>0}` on which `τ_a` is transitive; the finite places supply the compact `K^♮`; the
collapse is real, off by a factor `≤ 2`. **Verdict: AMEND** (state the base as `C_S`, the orbit count as `≤ 2`).

**T2, fibre dimension.** The memo applies CC's `dim_S H⁰(D) = ⌈(deg D + log 2)/log 3⌉ − 1_L` (P46:3358-3359) to `E|_1 = Σ_n h_n
[c_n^{−1}K_{P(n)}]`, a Haar-smeared measure, as if it were a CC Arakelov divisor on `\overline{Spec Z}`. D-HS never defines
this identification (LN:20-24 says "an Arakelov divisor `E|_{y_0}`" without saying how a smeared coset is one). The memo
flags this in its own item 4 (memo:268-270) and covers it by §2.3 ("any linear functional"). Acceptable **as conditional**:
"whatever fibre degree D-HS assigns, if CC's count is a function of that degree alone and the degree is linear in `E`, the
fibre dimension is `O(m)` at `E = mK`". Note also `K` is even (Thm 11.7(i)), so with the memo's own `w = t` weight
`deg(mK|_1) = m∫K(t)t\,dt = 0` and the fibre dimension at `mK` is `O(1)`, not merely `O(m)`. AMEND (label conditional).

**T2, fibre count.** The degree-shift formula `deg(y_0·D) = deg D + (∫E)log|y_0|` is asserted, not derived from any corpus
definition. The **load-bearing** fact is weaker and immediate: for `E = mK` both `deg(mK|_1)` and `∫mK` scale by `m`, so the set
`{y_0 : deg(mK|_{y_0}) > 0}` is **independent of `m`** for every linear fibre degree; hence the "count of fibres" cannot supply
a factor of `m`. The memo should say this (it is what (2.2) uses) instead of "a half-line whose length is fixed by the
truncation" (memo:156-158). **Verdict on T2: PASS on the conclusion `h⁰_HS(mK) = O(m)`, AMEND on the argument's phrasing.**

**"Tensor square is the only way to get `m²`" (memo:169-176).** The claim that `(a,b) = M(E)` are the only two frame-invariant
independent linear "fibre degrees" is unproved as a uniqueness statement (any linear functional of `E` is a candidate); but the
memo's actual use is only that the tensor-square reading is D.24.10's, which is PROVED (R140:1121-1136). AMEND: drop "only".

## 4. Lemma 3 (moment-functional `h⁰` fails (b′)) — AMEND; general form FAIL as stated

**Special case `w ∈ {1, t}` (what D-HS needs).** The functions `1, t, e^{t/2}, e^{−t/2}, cos γ_1t, sin γ_1t` are exponential
polynomials with distinct exponents `0` (multiplicity 2), `±½`, `±iγ_1`, hence linearly independent on any interval; the six
functionals `F ↦ ∫Fφ_j` are therefore linearly independent on `C_c^∞(I)` (density of `C_c^∞(I)` in `L²(I)`), so a real
`F ∈ C_c^∞` with `∫F = ∫Ft = Φ_F(0) = Φ_F(1) = 0` and `Φ_F(ρ_1) = ∫F e^{iγ_1t} ≠ 0` exists. Then `M(E_0+tF) = M(E_0)`,
`ℓ_i(E_0+tF) = ℓ_i(E_0)`, `|Φ_{E_0+tF}(ρ_1)| → ∞`, and Theorem 11.11 + Lemma 19bis.18 (P46:7112-7120) forbid a nonnegative
`𝓝_∞`-representative, exactly as in Theorem 19bis.19 (P46:7128-7149). Also `E_0 + tF` stays in any domain containing `E_0`
and `C_c^∞`, so this route does close the small-domain gap of §1 **for the fibrewise reading**. **PASS.**

**General statement (memo:183-185).** The hypothesis "`w_i` continuous of at most exponential growth `< e^{|t|/2}`" does **not**
exclude `w_1 = cos γ_1t`, `w_2 = sin γ_1t` (bounded). For those weights `V ∋ cos γ_1t, sin γ_1t` and no `F ∈ V^⊥` has
`Φ_F(ρ_1) ≠ 0`: the proof's separation step fails, and the prose "V contains no function with the oscillatory Fourier support…
a finite set of functions of distinct exponential types is linearly independent" (memo:190-194) is not an argument for
arbitrary continuous `w_i`. **The lemma as stated is FALSE-by-proof** (the conclusion may still be true; it is not proved).
Repair: since `V` is finite-dimensional and `ξ` has infinitely many zeros `ρ_j = β_j + iγ_j` with distinct `γ_j`, pick `j` with
`e^{(ρ_j−½)t} ∉ V_C`; Theorem 11.11 gives `Φ_{E'}(ρ) = Φ_E(ρ)` at **every** zero and Lemma 19bis.18 bounds `|Φ_{E'}(s)|` for
**every** `s` with `Re s ∈ [0,1]`, so the argument runs at `ρ_j`. With this repair no growth condition on `w_i` is needed at
all. The memo calls the general form "not load-bearing" (memo:273): agreed. **Verdict: AMEND** (restate with the zero chosen
off `V`; drop the growth clause).

**Independence of `ℓ_1, ℓ_2` from `M`.** `deg(E|_1)` with weight `t` and `∫E` with weight `1` versus `Φ_E(0), Φ_E(1)` with weights
`e^{∓t/2}`: independent. PASS.

## 5. T5 and the §28.4 table — PASS

§3: Theorem 12.4 (P46:3006-3017) and Theorem 19.25 give that the clause set (a),(b′),(c) is jointly unsatisfiable for both
`ξ` and `Ξ_a`, so no definition can pass LN T5's pattern (hold for `ξ`, fail for `Ξ_a`). Remark 19.26 bullets quoted
verbatim (P46:6357-6362). PASS. The scaling `((n^a+n^{−a})/2)²` of `ab` under the `Ξ_a`-transport is `DIAGNOSTIC` and
unverified here; not load-bearing.

§4 table against §28.4 (P46:11956-11967): (1) D-HS is a dimension count, not a square — PASS; (2) no local-data polar divisor;
the pole enters only through `K` in (c) — PASS; (3) no object — PASS; (4) reads `λ_−λ_+ = 1` (P44 Thm 3ter.6(iii)), a
magnitude; cannot separate `ξ` from `Ξ_a` by §3 — PASS; (5) carrier is `C_S` (P44 Def 3ter.1), multiplicative only — PASS;
(6) vacuous — PASS. **No clause of §28.4 survives; D-HS is not a reopening.**

## 6. Corpus correction — AMEND (half right)

* R140 Prop D.24.10 (R140:1121-1136): "(i) `ab` invariant = unimodularity of Thm 3ter.6(iii); (ii) transport-invariant tensor
 square factors through `ab`; (iv) Theorems D.24.7 and D.24.5 apply … refuted at (b′) and is RH at (c)". Cited accurately.
 README:58 "D.24.10 … refuted, PROVED" — accurate. P46 §19bis.17/19/22 transcriptions — verified (P46:7068, 7122, 7185;
 the transport-invariant remark follows 19bis.22 at P46:7196-7200).
* **PTD:189 is quoted inaccurately.** Row (vi) says "*One residue survives*: the never-run kill tests T1–T5 of candidate
 D-HS … but it must first clear the frame defect theorem W5, which post-dates that note". That sentence is **accurate**: the
 LN tests T1–T5 were never run, and D.24.10 ran none of them (it works in the frame, on `τ_{log n}`, not on fibre modules).
 Only **P7 at PTD:328** ("the one arithmetic-geometry candidate in the corpus never killed and never built") is inaccurate,
 and only in "never killed". The memo's item 6 (memo:274-275) should correct `:328` alone, and should note that D.24.10
 kills D-HS **only in the frame's reading** (transport = `τ_{log n}` on `D^W`, R140:1118-1119), which is what the memo calls
 the tensor-square reading.

## 7. Final verdict

| claim | verdict |
|---|---|
| §0 corpus correction | AMEND (fix `:328` only; `:189` is accurate) |
| §1.1 domain = `D^W` | AMEND (minimal domain `C_c^∞ ⊕ RK` excludes the Gaussian witness; needs a truncation lemma or Lemma 3) |
| §1.2 Corollary 1 on `D^W` | PASS (`PROVED` given (X19)) |
| Thm 21.15 confirmation | PASS |
| (Ev-1) | AMEND (as §1.1) |
| (Ev-2) degree-free conclusion / sign flip | PASS / PASS; AMEND: add "`deg' = 0` on `P^W`" (Thm 12.3 Step 4), which makes the parity argument unnecessary |
| (Ev-3) linear `O(d)` gap, witness | AMEND (choose `t` at the bottom of the window; `R(E)` is not bounded below by `¼d²(1−s_1²)−O(d)` for all admissible `t`) |
| (Ev-4) cone dichotomy `PROVED` | FAIL as `PROVED`; AMEND to "Horn B, unchanged, D-HS supplies no cone" — case (ii) mis-cites Thm 20.23 (B4 only); case (i) is `DIAGNOSTIC` |
| (Ev-5),(Ev-6) pairing / radical | missing; each closes in one line — AMEND (add) |
| (2.1) translate | PASS (with `c_n` for `n`) |
| Lemma 2(ii) single orbit | AMEND (base is `C_S = R_{>0}×K^♮`; `{±1}` unacted on; `≤ 2` orbits; bound `O(m)` survives) |
| T2 linear growth | PASS on conclusion; AMEND (state the `m`-independence of the positive-degree set; CC formula applied conditionally) |
| "tensor square is the only way to get `m²`" | AMEND (drop "only") |
| Lemma 3, `w ∈ {1,t}` | PASS |
| Lemma 3, general form | FAIL as stated (growth clause does not exclude `w_i ∈ span{cos γ_1t, sin γ_1t}`); repair by choosing a zero off `V` |
| §3 T5 | PASS |
| §4 §28.4 table | PASS — no clause survives |

**"D-HS KILLED": PASS.** D-HS as proposed in LN §1 — nonnegative cone in (b′), domain containing `K` — is excluded by
Theorem 19.25 on `D^W` (`PROVED` given (X19)), independently has linear growth `h⁰_HS(mK) = O(m)` under the fibrewise reading
(fails LN T2), and independently fails (b′) by Lemma 3 with `w ∈ {1,t}` (no (X19)); its tensor-square reading was already
killed in phase 140 (D.24.10). No clause of §28.4 is met.

**"No residual": AMEND, not PASS.** Two residuals, neither created by D-HS and neither favourable to it, must be named
rather than denied: (R1) the small-domain case `h⁰` on `C_c^∞ ⊕ RK` is killed only by the reading-dependent Lemma 3 until a
one-paragraph truncation of `F_0` is written into P46 §19.6; (R2) the cone in (b′) is Horn B, where P46 itself records B4 as
passing Theorem 19.30's test and `(b′)_{B4} ⟺ RH` — the memo's "either fails Theorem 19.30 or is RH" is proved for B4 only.
Recommended wording for the record: "D-HS KILLED (three independent routes); residual = Horn B and the frame's own open
items, unchanged by this memo; PATH-TO-D `:328` corrected." Labels to change in R155_054: (Ev-4) `PROVED` → `PROVED` for
case (i) under the `DIAGNOSTIC` inclusion, otherwise Horn B open; Lemma 3 general → restate; §1.1 "domain is `D^W`" →
"domain contains `𝒢_min`; `D^W` case PROVED, `C_c^∞ ⊕ RK` case by Lemma 3 or truncation".
