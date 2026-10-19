# R157_004 — Audit of R157_002 (the mechanism search under F1–F5)

Object: `R157_002_MECHANISM_SEARCH.md`, against the blueprint
`R157_000_BLUEPRINT.md` (F1–F5) and R157_003 (T3 = `METHOD-CONSTRAINT` modulo the `CITED (secondary source)`
import (H-DMV′)). Pure mathematics; the only computations are two scalar evaluations of closed-form bounds
(§1.1, §1.2), done in the scratchpad, not archived. `P47` = `04-papers/47-row-d-dual-certificates/main.tex`,
`P46` = `04-papers/46-intersection-frame-defect/archive/main.md`. I opened every label I cite at the line given. Amendments are applied
in place in R157_002, each marked "[amended per R157_004, Ak]". No paper, README or blueprint was edited.

Verdict scale: PROVED (correct as labelled, possibly after a stated repair), AMEND (conclusion stands, statement or
basis needs the repair listed), FAIL (false or unproved as labelled).

**Bottom line.** O3 is PROVED after four repairs (notation, "≍" → "≤", sign restriction, vacuity range); its
hypothesis cannot be proved here, but its failure has a clean characterisation (Lemma D). O4 is PROVED after I
supply the continuity proof (Lemma C) and an elementary small-window bound (Lemma E). Its "determinate" clause
FAILS as stated. Its content is Bombieri 2000 Thms 1, 3 and 5 plus P45 Thm 10.4, so it is a RESTATEMENT. In the
table, row 37 (Deninger) is not excluded: the exclusion inverts P46 T1, and the blueprint's F4 shares that
misreading. Rows 35 and 36 exclude only their `h⁰` readings. That leaves a second non-excluded entry, the unbuilt
"MW-5 cluster". Clause (b) of Lemma P157.S1 is not an exclusion criterion, and clauses (a) and (c) repeat the
non-sequitur that P46 Restatement 12.4a corrected. Five candidates are missing. **Row D: no label. No sign.**

---

## 1. The new observations

### 1.1 O3 (margin resolution) — **PROVED after repairs A1–A4**

**Derivation.** Checked against P47 eq:A (l.~170: `𝔞_T(F) = C₀‖F‖² + ∫(‖F‖² − c_F(u))K(u)du − Σ_{n∈N_T} v_n c_F(log n)`,
`v_n = 2Λ(n)/√n`), §subsec:finite (l.3273–3292: `v_n(a) = 2a(n)/√n`, `𝔞^{(v)}_T`, `RD_T(a)`, `W_T(a)`), and the proof of
`thm:finmod`(ii) (l.3368–3370: the same one-line computation with `F = F_+` of `lem:cpos` and
`c_* = √n₀ max(𝔞_T(F),0)/(2c_F(log n₀))`). With `a = Λ + sε1_{n₀}`, `v_{n₀}(a) − v_{n₀}(Λ) = 2sε/√n₀`, so for the
minimiser `F*`: `𝔞^{(v(a))}_T(F*) = λ^A_T − (2sε/√n₀) c_{F*}(log n₀) = λ^A_T − (2ε/√n₀)|c_{F*}(log n₀)|` when
`s = sgn c_{F*}(log n₀)`. Then `λ_min(A_T(a)|P_T) ≤ ` that value by the variational definition. Correct.

**Minimiser.** It exists: the proof of `thm:O` (l.614–620) proves compactness of sublevel sets on the unit sphere of
`L²(I_T)`, and `P_T` is closed; `cor:RH` proof (l.1269–1271) gives a real minimiser by `W(u+iv) = W(u) + W(v)`, and the
same splitting holds for `𝔞_T` on `P_T` (`prop:finite`(ii) proof, l.3308–3312). For the complete form, take the real
minimiser of `W_T` on `L²(I_T)` (Bombieri 2000 Thm 3, read in R154_031:328–331). The perturbation touches only the
comb, so `λ^W_T(a) ≤ λ^W_T − (2ε/√n₀)|c_{F^W}(log n₀)|`, where `F^W` is **the `W_T`-minimiser** (not `F*`), and
`λ^W_T ≤ λ^A_T` (`thm:margin`). PROVED.

**Repairs.**
* **A1 (notation).** `Φ* = Φ_{F*}` clashes with P47 l.136, where `Φ_F(s) = ∫F(t)e^{(s−½)t}dt` is the Mellin-type
  transform. The quantity in the computation is the autocorrelation `c_{F*}(log n₀)`. "Φ*(log n₀)" read literally
  is a different number.
* **A2 ("≍" → "≤").** `cor:margin1` gives an **upper** bound on `λ^A_T`, so O3 gives an upper bound on the threshold:
  `ε_*(T,n₀) := √n₀ λ^A_T/(2|c_{F*}(log n₀)|) ≤ 2·10⁹ T e^{−14.449T}/|c_{F*}(log n₀)|` for `T ≥ 1`. The true threshold
  may be far smaller (Zhu's conjectural law). The exponent is right: `15.449 − 1` comes from `√n₀ < e^T`. For
  `n₀ = 2` one keeps `15.449`, with prefactor `2√2·10⁹`. "≍" asserts a two-sided rate that nothing proves.
* **A3 (1/|c| and vacuity).** `|c_{F*}(u)| ≤ ‖F*‖² = 1`, so the factor `1/|c|` only **enlarges** the bound, and no
  lower bound on `max_{n∈N_T}|c_{F*}(log n)|` is known. So "exponentially small" holds only on the unproved
  proviso `|c_{F*}(log n₀)| ≥ e^{−(14.449−δ)T}` for some contact. Also, the closed form `2·10⁹Te^{−14.449T}` is
  `≥ 1` for `T ≤ 1.51` (it is 1061 at `T = 1` and 1.16 at `T = 1.5`), so O3 says nothing at `T ∈ [1, 1.5]` even with
  `|c| = 1`. This matches `rem:margin` (l.3261–3271: "an asymptotic statement … vacuous at the windows where signs
  are known"). §0 and §6's "about `e^{−14T}`" dropped both the prefactor and `1/|c|`.
* **A4 (sign restriction).** For `s = −1` one needs `Λ(n₀) ≥ ε_*`. At a contact that is not a prime power
  (`Λ(n₀) = 0`), only `s = +1` is available. For the class `C_BT` (`a ≤ Λ`) only `s = −1` is available.

**Is the hypothesis provable? Can it fail?** Not proved here. What its failure means is clean:

> **Lemma D (degenerate case; PROVED).** Fix `T`. For `v ∈ ℝ^{N_T}` put `V(v) = inf{𝔞^{(v)}_T(F) : F ∈ P_T, ‖F‖ = 1}`.
> Then `V` is finite and concave. If `F*` is a real unit minimiser at `v⁰ = v_T(Λ)`, then
> `V(v) ≤ V(v⁰) − Σ_n (v_n − v⁰_n) c_{F*}(log n)` for all `v`. Hence, **if some minimiser has `c_{F*}(log n) = 0` for
> every `n ∈ N_T`, then `v_T(Λ)` is a global maximiser of `V` on `ℝ^{N_T}`**, and in particular
> `λ^A_T ≥ λ^{∞,P}_{min}(T)` (take `v = 0`).
>
> *Proof.* `V` is an infimum of affine functions of `v`, so it is concave. It is bounded above by `𝔞^∞(G)` for any
> unit `G ∈ P_T` supported in an interval of length `< log 2`: such `G` exist, since the constraint has codimension
> `≤ 2` in an infinite-dimensional space, and their autocorrelation vanishes at every `log n`, `n ≥ 2`. It is
> bounded below by `λ^{∞,P} − Σ|v_n|`. The displayed inequality is `V(v) ≤ 𝔞^{(v)}_T(F*)` expanded with eq:A. ∎

So O3's degenerate case is not structural noise. It would mean that the actual comb is the **optimal** comb for
`λ_min` at that window, among all real weight vectors. Nothing in the record excludes this, and nothing makes it
plausible. Record it as open. If the minimiser is non-unique and **some** minimiser has `c ≠ 0` at a contact, O3
applies with that one. **Label: O3 = COROLLARY (PROVED) of the proof of `thm:finmod`(ii) + `cor:margin1`,
conditional on the stated non-degeneracy, which is OPEN; Lemma D PROVED.**

**Scope of the "Reading" (A5).** For `C_PNT(ε)` and `C_zeros`, `cor:void` already excludes every derivation with
**no** size restriction (`thm:finmod`(iii): closed under arbitrary one-term changes). O3 adds content only for
classes closed under **small** one-weight changes, for instance inputs known to width `δ` (enclosures). Even there
it restates `cor:margin2`(i) in weight coordinates: margin in weights = margin in `λ` × `√n₀/(2|c|)`. "Every
estimate … fails this" is replaced by "every input whose class is closed under a change of one weight by
`ε_*(T,n₀)`".

### 1.2 O4 (clopen reformulation) — **PROVED after Lemmas C and E; "determinate" clause FAIL; content = RESTATEMENT**

**(⇒).** RH ⟹ `λ^W_T > 0` for every `T`: this is in P47 already, in the proof of `cor:RH` (l.1266–1279, the
Jensen/exponential-type argument) and restated in the proof of `thm:KEP3`(b) (l.1689–1691: "gives `λ^W > 0` — not
merely `λ^W ≥ 0` — for every `T ≥ ½log2`"). It is also Bombieri 2000 Thm 1 (strict positivity; R154_031:314–315)
with his Thm 3 (attainment). PROVED, not new.

**(⇐).** Assume ¬RH. P45 Thm 10.4, used in the proof of `cor:margin2`(iii) (l.3253–3256), gives `T₀` with
`λ^A_{T₀} < 0`, hence `λ^W_{T₀} ≤ λ^A_{T₀} < 0`. We need `λ^W ≥ 0` somewhere, and continuity.

> **Lemma E (small windows, elementary; PROVED).** For `2T < log 2`,
> `λ^W_T ≥ C₀ + log coth(T/2) − 4 sinh T`. In particular `λ^W_T > 0` for `T ≤ 0.005` (the right side is `0.599`).
>
> *Proof.* There are no contacts. For real unit `F` (the form splits), eq:A with `‖F‖² − c_F(u) ≥ 0` and
> `c_F = 0` on `u ≥ 2T` gives `Lev(c_F) ≥ ∫_{2T}^∞ K ≥ ∫_{2T}^∞ ½/sinh(u/2)du = log coth(T/2)`, and
> `2|A||B| ≤ 2(∫_{I_T}e^t)^{1/2}(∫_{I_T}e^{−t})^{1/2} = 4 sinh T`. Also `C₀ = ψ(¼) − log π = −5.3722`. ∎

This removes O4's dependence on Zhu (`cor:KEP08`) or Yoshida/Bombieri Thm 12. Only `λ^W ≥ 0` at one point is
needed.

> **Lemma C (continuity of `T ↦ λ^W_T`; PROVED).** `λ^W_T` is continuous on `(0,∞)`.
>
> *Proof.* For `r ∈ [½,2]` let `U_r F(t) = r^{−1/2}F(t/r)`, unitary `L²(I_T) → L²(I_{rT})`, preserving form
> domains; `\widehat{U_rF}(τ) = r^{1/2}F̂(rτ)`, `c_{U_rF}(u) = c_F(u/r)`. Then `λ^W_{rT} = inf_{‖F‖=1} W(U_rF)`, and
> `W(U_rF) − W_T(F)` is the sum of three terms.
> (i) Archimedean: `(1/2π)∫(m(s/r) − m(s))|F̂(s)|²ds`, with `|m(s/r) − m(s)| ≤ sup_x|x m′(x)|·|log r|`. This is finite,
> since `m′(x) = −½ Im ψ′(¼ + ix/2)` and `ψ′(z) = O(1/|z|)` on `Re z = ¼`.
> (ii) Comb: `Σ_{n<e^{4T}} v_n|c_F(log n/r) − c_F(log n)|`. Here `|c_F(u) − c_F(u′)| ≤ (1/2π)∫|F̂|²min(2,|τ||u−u′|)
> ≤ η‖F‖² + (2/log(2+η/|u−u′|))‖F‖²_Q`, with `‖F‖²_Q := ‖F‖² + (1/2π)∫log(2+|τ|)|F̂|²`. Terms with
> `log n/r ≥ 2T` vanish, which handles contacts entering or leaving.
> (iii) Polar: `A(U_rF) = r^{1/2}∫F(t)e^{rt/2}dt`, so `|A(U_rF) − A(F)| ≤ ‖F‖·‖r^{1/2}e^{rt/2} − e^{t/2}‖_{L²(I_T)}`,
> and the same for `B`.
> Since `log(2+|τ|) ≤ m(τ) + C`, one has `‖F‖²_Q ≤ W_T(F) + C′‖F‖²` with `C′` uniform for `r ∈ [½,2]`. So
> `|W(U_rF) − W_T(F)| ≤ η(r)(W_T(F) + C′‖F‖²)` with `η(r) → 0` as `r → 1`, uniformly in `F`. Taking infima,
> `|λ^W_{rT} − λ^W_T| ≤ η(r)(|λ^W_T| + C′)`. ∎
>
> *Independent citation:* Bombieri 2000 Thm 5 (R154_031:335–337, primary text read): the even and odd minima
> `μ_±(M)` of the complete functional on `L²([M^{−1},M])` are continuous and decreasing. Since `W_T` splits into even
> and odd parts (`Re(A B̄) = |A_e|² − |A_o|²`, and the symbol is even), `λ^W_T = min(μ_+, μ_−)` at `M = e^T`.
> **Caution for Paper 47:** P47 itself says "no continuity in `T` is claimed" for the class value `= λ^W`
> (l.3103), and "no continuity being asserted" for the archimedean thresholds (`prop:arch` proof, l.2409).
> O4 therefore imports something that P47 deliberately does not assert. That is legitimate by Lemma C, but it
> must be said.

With Lemmas C and E, (⇐) is the IVT. Moreover, if RH fails then `Z_W = [T_c, T_c′]` is a **nonempty compact
interval**, possibly a point (`λ^W` is nonincreasing by `lem:monoT` and continuous). **O4 as an equivalence: PROVED.**

**The "determinate" clause — FAIL as stated (A6).** At `T_c`, `W_{T_c} ⪰ 0` has a real kernel vector `F*`
(attainment). What is proved: *if* `𝔖(T_c) ≠ ∅`, every `ν ∈ 𝔖(T_c)` satisfies `∫|F̂*|²dν = 0`. This uses the core
approximation in the proof of `thm:KEP2` (l.1663–1676), `F̂_k → F̂*` locally uniformly, and Fatou. So `ν` is purely
atomic on the real zeros of `F̂*`, and no absolutely continuous solution exists. By `thm:Al`(b) (l.3606–3608) no
`w ∈ 𝒲_T` satisfies `Al_T(w)` there. **Not proved:** (a) that `𝔖(T_c) ≠ ∅`, since `thm:KEP3`(a) is silent at
`λ^W = 0` and P47 l.3915 says so explicitly ("Indeterminacy of KEP(T) is not known to be equivalent to either λ^W > 0 or λ^W ≥ 0"); (b) that `#𝔖(T_c) = 1`. The classical Kreĭn theorem
(degenerate datum ⟹ unique extension) is for continuous positive-definite data, and P47 §subsec:KEP (l.1578–1582)
imports nothing from it. `thm:finDet` is for **finite** zero sets, and the real zero set of `F̂*` is infinite. So
the clause should read "every solution, if any, is atomic and carried by `F̂*^{−1}(0) ∩ ℝ`".

**"Not structural" (A7).** The witness in `cor:convfail`(ii) (l.3842–3846) crosses **in the weight parameter `θ`
at fixed `T = ½log3`**, not in `T`. It shows that degeneracy is not excluded by comb-class structure. It is not an
instance of a `T`-crossing. The conclusion stands; the wording is corrected.

**Is O4 already in P47 or in the literature?** The strict half is in P47 (`cor:RH`, `thm:KEP3`(b)) and in Bombieri
Thm 1. The continuity is Bombieri Thm 5. `thm:KEP3`(a) and `thm:Al`(c) already name `{T : λ^W = 0}` as the
exceptional set. The reformulation "never exactly 0", equivalently "`W_T` has trivial radical at every `T`", is
not stated in P47 (grep "clopen", "first crossing": 0). It is in the genus of Suzuki Thm 1.3/1.4 (R154_031:232–237,
"nondegenerate on `L²(−a,a)`"). The conditional status of Suzuki's Thm 1.4 is not recorded in R154_031. By O4 it
cannot be an unconditional statement at every `a` unless it proves RH, so it must be read in the primary text
before any novelty sentence. **Label: O4 = RESTATEMENT (Bombieri 2000 Thms 1, 3, 5 + P45 Thm 10.4), with Lemmas C,
E PROVED.**

### 1.3 O1, O2

O1: PASS (RESTATEMENT). The Weil functional is translation-invariant on `f ⋆ f̃`: `A B̄` is invariant under
`F(· − c)`. So nestedness plus `lem:monoT` gives exactly Weil positivity on `C_c^∞`.

O2: **AMEND (A8)**. "If `H` is consistent with one off-line zero then `H` does not imply …" is, read literally, false
or empty. If RH is true, every true `H` implies it (P47 l.3416). The operative form is a schema in the sense of
P46 Thm 18.1/Rem 18.1a: a derivation from `H` that is valid in a structure satisfying `H` with an off-line zero is
unsound. The use of O2 inside O4's (⇐) is the unconditional part (P45 Thm 10.4), and it is correct.

---

## 2. Sample audit of the table (17 rows; every cited label opened)

| # | row | cited basis, as found | exclusion valid? | verdict |
|---|---|---|---|---|
| 26b | P152.2 | R152_005:34–36; R152_002:196–235 (formulation, gates g1–g3; auditor's estimate "(g1) fails") | not excluded: Prop B.3 is scoped to trees (R152_005:21) | **SURV confirmed**; see §3 for the test |
| 37 | Deninger | P46 Thm 18.1 (main.md:4787–4822); §18.1 title (l.4785) "**the proof must be uniform in the number field**"; l.5295; MAP_1:73 NG-62b = `EQUIVALENT-TO-RH` (a finite-window diagnostic) | **FAIL.** T1 is a method constraint with a disjunction: name a separating property **or** prove GRH for all `K`. A field-uniform programme is what T1 *prescribes*, not what it excludes (Rem 18.1a: "does not say that GRH is out of reach"). NG-62b concerns a finite-window model, not Deninger's (unbuilt) cohomology | **NOT EXCLUDED (unbuilt programme, MW-5 cluster)** (A9) |
| 35 | F₁ / scaling site | P46 Thm 19.25 (main.md:6358–6361): no `h⁰ : D^W → ℝ_{≥0}` with (a), (b′), (c); MAP_1:59 MW-5 "genuinely UNBUILT (not proved impossible)" | valid for **`h⁰`/Riemann–Roch-growth readings** only. A Hodge-index theorem on a square not routed through an `h⁰` on `D^W` is outside Thm 19.25. "Category-independent" is true for functions on `D^W`, not for the programme | **AMEND**: EXCL for `h⁰` variants; residual → MW-5 cluster (A10) |
| 36 | Arakelov | P122_007:3–8 ("do not apply … cannot be imported"); phase-15-arithmetic-hodge-index M3-attempt6, M10 | valid for **importing** Faltings–Hriljac–Moriwaki / Yuan–Zhang (hypothesis mismatch: no surface over `Spec Z`); not for building the square | **AMEND**: EXCL (import); residual → MW-5 cluster (A10) |
| 34 | CC prolate / archimedean | P47 `prop:archneg` (l.2573), `cor:Tarch` (l.2543), `thm:index`, `thm:J` | valid: the archimedean form is indefinite on `P_T` from `0.60` and complete-negative from `0.4608` (PROVED, interval-arithmetic / machine-verified). F4's "shared Γ-data" is not needed; F1 suffices | EXCL (as a uniformity mechanism) confirmed; F4 wording dropped |
| 18 | CC semilocal / finite `S` | P47 `thm:SC` (l.2098), `prop:finsupp` (l.3374–3392) | valid. The "(arg.)" for infinite-support finite-mass `S` is a proof. `σ_T` now depends on `T`, but `|Σ_{n∈S∩N_T}v_n cos(s log n/T) − A_S| ≤ Σ_{n≤N}v_n|1 − cos(s log n/T)| + 2Σ_{n>N, n∈S}v_n → 0` pointwise with the bound `A_S`, and dominated convergence runs as in `prop:finsupp` | EXCL; **arg. → PROVED** (A11) |
| 41 | dBN / Rodgers–Tao | Paper 13 `thm:nogo` (13/main.tex:150; N5 "arithmetic-blind", l.45–46) | valid as EQUIV plus F1 for the flow | EQUIV confirmed |
| 7 | Li / Keiper | P47 `cor:Li` (l.4707–4730), `rem:LiSC` (l.4754) | valid. `rem:LiSC` carries computed values (DIAGNOSTIC-type) and says its reading is "an interpretation, not a theorem" | EQUIV confirmed; note `rem:LiSC` label |
| 43 | Nyman–Beurling / Báez-Duarte | MAP_1:36 NG-B4 (`EQUIVALENT-TO-RH / CIRCULAR`), :64 CIR-3; R155_038:22 (`HEURISTIC`, P4 closed) | valid as EQUIV. The "rhyme" with `thm:margin` is interpretation | EQUIV confirmed |
| 38 | Suzuki | R154_031:232–240 (Thms 1.2–1.7 as read) | valid as EQUIV. **"Its proof of `⇐` is a partial-sum bound (W4)" is not in R154_031 or any file I found: UNVERIFIED** | EQUIV; A12 strikes the unverified sentence |
| 32 | Hilbert–Pólya | MAP_1:52 NG-E5, :58 MW-4, :43 NG-C3; R151_005:19 | EQUIV verdict fine. **Basis wrong:** O-151.4 is an **OPEN** item (R151_005:19, 52), not a proved restatement, and T6 concerns moment families, not operators with spectrum `{γ}` | EQUIV; basis amended (A13) |
| 40 | Jensen / Turán / GORZ | Paper 15 `thm:hr` (15/main.tex:203–213) | **overstated.** `thm:hr`(2) says `δ_∞ = 0 ⟹ inf_m δ_m = 0`: no uniform *gap*. It does not say "uniform positivity cannot come from a stability argument". It is `thm:margin` again. Finite order is excluded by O2 (unconditional, consistent with off-line zeros; arg.) | EQUIV/EXCL kept; wording amended (A14) |
| 42 | Lee–Yang / Kurasov–Sarnak | E70_1_RESULTS:30–33 | valid | EQUIV confirmed |
| 28 | model theory | argument in the memo | valid **scoped to o-minimal expansions of ℝ** (definable subsets of ℝ are finite unions of points and intervals; the primes are not). Λ is definable in `(ℤ,+,·)`, so "Λ enters only as parameters" holds only inside o-minimal structures. The ACFA sentence uses Thm 22.17, which R152_002 flagged as a category error when applied off schemes (R152_005:22) | EXCL (arg.), scope stated (A15) |
| 27 | `×p` rigidity | P47 `cor:void` (l.3394–3412) with `C_supp` | valid, PROVED: `C_supp` contains Λ and is closed under amplification at `2` and under deletion | EXCL confirmed for positions-only inputs |
| 46 | Selberg-trace analogues | R152_005:10 (Prop A.1 PROVED); closure plan:151–153; MAP_1:56 MW-2 | Prop A.1 valid for Maass–Selberg. **MW-2 is a pattern, "not itself a single closed theorem" (MAP_1:56)**; the Ramanujan-graph / 3/16 discard is a closure-plan judgement | EXCL for the listed instances, basis labelled (A16) |
| 19 | local–global | MAP_1:41 NG-C1, **:48** NG-E1, **:57** MW-3 (memo says "l.41, 48, 59"; l.59 is MW-5) | NG-E1 is a *computed* refutation at `p ≤ 7` (DIAGNOSTIC-type); MW-3 is "absence of a known theorem" (MAP_1:57). The exclusion stands on `thm:SC`/`prop:finsupp` (PROVED), and only for arguments that infer the sign from local or finite-`S` positivity | EXCL, basis amended (A17) |

**Rows resting partly on non-theorem items without saying so:** 19 (NG-E1 computed; MW-3 absence), 32 (O-151.4
OPEN), 33, 46 and 53 (MW-2 pattern-level), 37 (NG-62b diagnostic; T1 misread), 38 (unverified proof claim),
6 and 7 (`rem:LiSC` computed values, supplementary only). **Exclusions that are really equivalences:** none of the
EXCL rows sampled collapses to an equivalence, except that row 40's finite-order part is excluded by O2 as a
quasi-RH statement, which is a method constraint, not a theorem. **T3 wording:** rows 26b and §5(a) said
"conditional on H-DMV"; replaced by "METHOD-CONSTRAINT modulo the CITED (secondary source) import (H-DMV′)"
(R157_003 §3) (A18).

**The blueprint's F4 itself** reads "names a property separating ξ from all ξ_K (P46 T1)". That inverts P46 §18.1
("the proof must be uniform in the number field") and Rem 18.1a. F4 should read "names, at a
load-bearing step, a property not shared by every `ξ_K`, **or** proves GRH for every `K` (T1); invokes A3 and one of
A7/A8/A9 (T2, `Ξ_a`)". Rows 12, 45 and 48 also cite T1 as if it excluded something. All three keep their verdicts
on independent PROVED grounds (F1; NG-B8/`cor:infinite`; F1).

---

## 3. P152.2 and Lemma P157.S1

**Never run: confirmed.** `grep -rn -i 'poineau|beurling blind|P152|A^{1,an}|Berkovich line'` over
`03-research/phase-15-arithmetic-hodge-index[3-6]*`, `04-papers/4[4-7]*/main.*` and `05-meta-and-planning/`: the only hits are
R155_031:67 and PATH-TO-D:67 (a summary row of phase 152) and ROW-D-CLOSURE-PLAN:320–342 (the recommendation). No
round ran the test. P46 does not record (P152.2) (grep 0), and neither does Paper 44 (the recommended remark on
Dictionary B.1 is also absent).

**Clause validity.**

* **(a) Definability ⟹ excluded by T3 + `thm:finmod`: AMEND (A19).**
  - *Non-sequitur.* "Defined by the same formulas" transfers a **proof**, not a **truth**. This is exactly the
    error P46 Restatement 12.4a corrected in phase 135 (main.md:3020–3040, "uniformity of a *definition* transfers a
    *proof*, not the *truth* of a conclusion"). A uniformly defined `𝓔` can be `⪰ 0` for ζ and indefinite for other
    members. The valid criterion is about **derivations**: if `𝓔 ⪰ 0` is derived using only data and properties
    common to a class `𝒞` of weight functions that contains Λ, is closed under one-term amplification, and on which
    the identity `𝓔_a = W_T(a)` holds, then by `cor:void` + `thm:finmod`(ii) the derivation proves a false statement.
    That is PROVED and unconditional.
  - *T3 needs a bridge.* T3 (P46 Rem 27.16, l.11881 ff.) forbids deriving (ZFS_δ) from BE1–BE8. To use it, one
    needs "`𝓔_𝒫 ⪰ 0 ⟹ ζ_𝒫` has no zeros with `β > 1 − δ`" for Beurling `𝒫`. A Weil-type criterion is not available
    for the DMV system, which continues only to `Re s > θ` and has no functional equation. Without the bridge, T3
    does not apply. With it, T3 is `METHOD-CONSTRAINT` modulo the `CITED (secondary source)` import. So `cor:void`
    is the primary exclusion and T3 is supplementary.
* **(b) Per-place splitting ⟹ excluded by NG-E1 + `thm:SC`: FAIL as a criterion (A20).** Weil's explicit formula
  already writes `W(g) = W_∞(g) + Σ_p W_p(g) +` polar terms. So **every** construction that satisfies the identity
  `𝓔(f) = W(f ⋆ f̃)` decomposes as `Σ_v 𝓔_v` at the level of values, and (b) would fire on Weil's form itself.
  Indefinite summands do not forbid a positive sum: `W_T = 𝒜_∞ + Π_T` with both indefinite (`prop:archneg`,
  `lem:cpos`). Valid replacement **(b′)**: *if the positivity of `𝓔` is inferred from positivity of the `𝓔_v`, or of
  `𝓔_∞ + Σ_{v∈S}𝓔_v` for a finite `S`, it is excluded by `prop:finsupp`/`thm:SC` (PROVED), with NG-E1 as
  corroboration (computed at `p ≤ 7`).* This is R152_002's gate (g3): the construction must name what supplies the
  assembly.
* **(c) Defined and `⪰ 0` for `Ξ_a` ⟹ excluded by P46 Thm 12.4: AMEND (A21).** Thm 12.4 (main.md:3006–3017) is
  about `h⁰_a` satisfying (a), (b′), (c) in the intersection frame, not about energies. The fact needed is that
  `Ξ_a`'s Weil-type form is negative on some primitive test: P46 Prop 12.4B (main.md:2899) with Hardy (X16), i.e.
  Thm 12.4's argument. The criterion is again a schema (Restatement 12.4a). If `𝓔_Z ⪰ 0` **and** the identity
  `𝓔_Z = W_Z` are both derived model-uniformly over a class containing `Ξ_a`, contradiction. An unconditional
  `𝓔_{Ξ_a} ⪰ 0` (for instance a tree energy of negative type, R152_002:189–191) only shows that the identity fails
  for `Ξ_a`. That kills the candidate only if the identity for ζ is proved model-uniformly.
* **Missing clause (d) (A22).** The lemma lists `𝒫` of type (iv) (number fields) but tests nothing for it, and it
  omits R152_002's gate (g2) (Epstein, `Ξ_Q`). Add: **(d)** if the positivity derivation uses only A1–A6, A2⁺ and the
  data `𝔇`, it is excluded by P46 Thm 18.16 (T2, falsifier `Ξ_Q` PROVED). If it is field-uniform over
  `M(O_K)`, T1 requires it to prove GRH for all `K`, which is a standard to meet, not an exclusion. The **Pass**
  clause must also require that A3 and one of A7/A8/A9 be invoked (T2).
* **Expected outcome (A23).** The memo expects (a) to pass because "a Beurling system has no such ring". This
  conflicts with the record's own estimate (R152_002:232–233, "the auditor's estimate is that (g1) fails") and with
  R152_001:407 ("Dictionary B.1 applies verbatim to a Beurling generalized-prime system"). The test must decide
  whether `μ_f` and `k` factor through the **atom list** `{(q, k log q)}` with weights. If they do, the geometry of
  `A^{1,an}_Z` is decorative and (a) fires via `cor:void`, whatever ring Beurling systems lack.

---

## 4. Candidates missed

| candidate | filter verdict |
|---|---|
| **M1. Zagier / Sarnak / Verjovsky horocycle equidistribution** (RH ⟺ the long closed horocycles of `SL₂(ℤ)\ℍ` equidistribute at rate `O(y^{3/4−ε})`) | a rate criterion. Per window, an estimate: excluded by `cor:void` (F1). Weaker rates are quasi-RH (O2, F2). Globally **EQUIV**. Same family as row 25 (the resonances `ρ/2`) |
| **M2. Balazard–Saias–Yor** (`(1/2π)∫_{Re s=½} log|ζ(s)| |s|^{−2}|ds| = Σ_{Re ρ>½} log|ρ/(1−ρ)| ≥ 0`, with RH ⟺ equality) | **EQUIV.** It is a one-sided identity whose RH case is the boundary, the exact rhyme of `cor:margin2`(iii) (`L^W ≤ 0`, RH ⟺ `L^W = 0`), and it belongs in §4's "no-margin laws" list. No mechanism |
| **M3. Lax–Phillips / Pavlov–Faddeev scattering** (the zeros of `ζ(2s)` as scattering resonances of the modular surface) | the same object as row 25. R152 Prop A.2: `β = ¼` *is* RH. **EQUIV**, or excluded below RH strength by O2. A naming gap only |
| **M4. Selberg-class axiomatics** (Dirichlet series, continuation, functional equation, Ramanujan, Euler product) | **not excluded, no mechanism.** None of the record's falsifiers lies in the class: DMV has no functional equation (T3), `Ξ_a` violates Ramanujan (the A3 analogue), Epstein and Davenport–Heilbronn have no Euler product (T2), and `ξ_K ∈ S` puts the class under T1 (GRH for all `K`). The axiom list is a hypothesis set that no record statement refutes. That is worth recording, but it names no step. **EQUIV (framework)** |
| **M5. Connes–Consani ζ-cycles / Sonin spaces** (finite-`L` scaling spectra approximating low zeros; literature description not re-verified) | per `L`, a finite approximation: **F3** (`thm:finZ`, `thm:arena`). In the limit, a spectral realisation: row 32, **EQUIV** |
| **M6. The MW-5 cluster** (Deninger's foliated cohomology with a Hodge–Riemann form; a CC Hodge index on the square of the scaling site; an arithmetic surface "`Spec ℤ ×_{F₁} Spec ℤ`" with a Hodge index not routed through `h⁰` on `D^W`) | **NOT EXCLUDED by any proved statement** (MAP_1:59: "UNBUILT (not proved impossible)"). It passes F5 (not an `h⁰` on `D^W`), and F4 once T1 is read correctly. No object, no one-round test. Formed from rows 37, 35(residual), 36(residual) |

---

## 5. Verdicts

| item | verdict |
|---|---|
| O1 | PROVED (RESTATEMENT) |
| O2 | AMEND (A8): a derivation schema, not an implication |
| O3 | PROVED after A1–A5; non-degeneracy hypothesis OPEN; Lemma D PROVED |
| O4 | equivalence PROVED with Lemmas C, E (new here, PROVED); "determinate" FAIL → "atomic, if solvable" (A6); crossing wording (A7); content RESTATEMENT of Bombieri Thms 1, 3, 5 |
| table, 17 rows sampled | 9 confirmed (26b, 34, 18, 41, 7, 43, 42, 28, 27); 6 AMEND on basis or scope (19, 32, 35, 36, 40, 46); 1 FAIL (37); 1 verdict confirmed with an unverified sentence struck (38) |
| row 18 "(arg.)" | upgraded to PROVED (A11) |
| P152.2 never run | confirmed |
| Lemma P157.S1 | (a) AMEND, (b) FAIL → (b′), (c) AMEND, (d) missing; Pass clause amended |
| missed candidates | M1–M6 |
| counts | 56 rows → 61 (M1–M5 added as rows 56–60; M6 is row 37 re-scoped, not a new row): EXCL 39 (38 old + M5), EQUIV 20 (16 old + M1–M4), SURV 1 (P152.2), NOT EXCLUDED 1 (row 37 = MW-5 cluster) |

**Final survivor list.** (1) **(P152.2)**, formulated, with the amended one-round Lemma P157.S1. (2) **The MW-5
cluster (M6)**, not excluded, unbuilt, with no formulated object and no one-round test. The record's rule ("do not
invent the candidate") applies to it as it does to rows 27 and 30. The honest §6 sentence is: "one formulated
candidate and one unbuilt programme cluster are not excluded". It is not "exactly one".

**Cleared for Paper 47 (not applied; decision pending; checked against P47's own definitions per the
rule).**

(i) *Optional remark after `cor:margin2`, cleared:*

> **Remark (resolution in the weights).** Fix $T\ge1$ and let $F_\star$ be a real unit minimiser of $\mathfrak a_T$
> on $\PT$. If $c_{F_\star}(\log n_0)\ne0$ for some $n_0\in\NT$, the proof of Theorem~\ref{thm:finmod}(ii) applied
> to $F_\star$, with the sign of the change chosen as that of $c_{F_\star}(\log n_0)$ (a decrease requires
> $\Lambda(n_0)$ at least the change), shows that $\mathrm{RD}_T(a)$ fails for some $a\ge0$ differing from $\Lambda$
> at $n_0$ alone, by at most $\sqrt{n_0}\,\lamA/(2|c_{F_\star}(\log n_0)|)\le2\cdot10^9\,T e^{-14.449T}/|c_{F_\star}(\log n_0)|$
> (Corollary~\ref{cor:margin1}, $n_0<e^{2T}$); the same holds for $\lambda^{\mathrm W}_T(a)$ with the minimiser of
> $W_T$. The bound exceeds $1$ for $T\le1.51$ even when $|c_{F_\star}(\log n_0)|=1$, and no lower bound on
> $\max_{n\in\NT}|c_{F_\star}(\log n)|$ is known; if every minimiser has $c_{F_\star}\equiv0$ on $\log\NT$, then
> $v_T(\Lambda)$ maximises $v\mapsto\lambda_{\min}(A^{(v)}_T|\PT)$ over $\R^{\NT}$. It gives no sign.

(ii) *Optional, one sentence, as a RESTATEMENT, in §subsec:related or after `thm:KEP3`:*

> By \cite[Thms.~1, 3, 5]{Bombieri2000} and \cite[Thm.~10.4]{Paper45}, RH holds if and only if $\lamW\ne0$ for
> every $T$; if RH fails, $\{T:\lamW=0\}$ is a nonempty compact interval, at which every solution of
> $\mathrm{KEP}(T)$, if one exists, is atomic and carried by the real zeros of a minimiser's transform.

Adding (ii) requires reconciling it with P47 l.3103 ("no continuity in $T$ is claimed"), for instance "no continuity
is claimed for the sub-classes; for $\lamW$ itself it is \cite[Thm.~5]{Bombieri2000}". Lemma C may be added as a
proof if a citation is not preferred.

**Not cleared:** O3's "≍" form; "`e^{−14T}`" without prefactor and `1/|c|`; O4's "determinate"; any claim that O4
is new; the table and §6 as written ("exactly one candidate"); Lemma P157.S1 clause (b) as stated.

**Row D: no label. No sign is claimed for ζ at any window, in either form. Nothing moves any row's status.**
