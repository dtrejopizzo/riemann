# R148.002 — Hostile audit of round 1, phase 148

*Auditor: Opus 5 (1M), adversarial role. Date 2026-09-14. Inputs read in full:
`R148_000_LEAD_BLUEPRINT.md`, `R148_001_BUILDER_ROUND1.md` (592 lines), `README.md`,
`scripts/certify_mixed_support.py` (re-run `--fast`, output reproduced below),
Paper 46 `04-papers/46-row-d-the-sign/main.md` §11 (Def. 11.1 / (11.1), Lemma 11.2, `I_∞`, `𝓔`) and §19
(Def. 19.16, Lemma 19.17, Prop. 19.18, Thm 19.22, Thm 19.23, Remark 19.27),
`03-research/phase-41-build-G2/125-forma-interseccion-cuadrado.md`.
A negative closing is audited exactly as hard as a positive one: a false negative closes a row.*

---

## VERDICT

**ACCEPT WITH REPAIRS.**

The kill test's outcome (i) **stands**, and the central mechanism is not only correct but **weaker than it
needs to be** — the audit supplies a strictly stronger replacement for Lemma D.56.3 (§1.3 below) that
closes the exact loophole the hostile brief asks about and, as a bonus, closes **O-148.3**, which the
builder left open and mislabelled. Seven repairs are required. Two labels **DOWNGRADE**, one headline is
**WITHDRAWN as stated**, one corpus row is **WRONG** and must be rewritten. No claim in the phase is
**REFUTED**, and no FATAL flag is warranted.

---

## §1 — Item 1: is the collapse really forced? (the hardest attack; the builder's proof is the weak point
## of an otherwise correct conclusion)

### 1.1 The builder's argument, restated at its exact strength

Thm D.56.2 (characterisation) is correct and is a triviality of order of quantifiers: `k_Φ − φ⊗ψ ≥ 0`
on `X` `⟺` `Φ(w) ≥ (φ⊛ψ)(w) := sup_u φ(u)ψ(u+w)` for all `w`. `PROVED`, no attack available.

Lemma D.56.3 asserts `φ⊛ψ ≥ 0` and proves it from **`φ(u), ψ(u) → 0` as `|u| → ∞`**, via
`sup ≥ limsup_{u→+∞} = 0`. The builder then adds the load-bearing clause *"and more generally for every
pair for which the `(R)×(R)` block of `B` is finite"*, and builds the whole closing narrative on it
(D.56.4's remark; §D.58 *"the additional sector is Hilbert–Schmidt, hence vanishing at infinity"*; the
Recommendation *"the obstruction is a consequence of finiteness of the `(R)×(R)` block, so every variant
within the form's domain inherits it"*).

### 1.2 **FINDING A-1 (an error). `L²` does NOT imply vanishing at infinity, so the clause as written is
### false and the narrative built on it is unsupported.**

`φ ∈ L²(R)` with `φ(u_n) = n` on intervals of width `n^{−3}` about `u_n = n` is Hilbert–Schmidt-admissible
and does not vanish at infinity. So *"Hilbert–Schmidt `⟹` vanishing at infinity"* — used verbatim three
times, in D.56.4's remark, in §D.58 and in the Recommendation — is **false**. Inside `D^W` (Def. 11.1,
decay (11.1)) the hypothesis of Lemma D.56.3 does hold, so **Theorem D.56.4 is not damaged**; what is
damaged is every sentence claiming the collapse is *structural for the whole domain of `B`*. That is
precisely the sentence the phase closes on.

### 1.3 **REPAIR R-1 (the correct lemma, strictly stronger, and it answers the brief's question).**

Replace Lemma D.56.3 by the following, which needs **no decay at all** and which converts the collapse
from a statement about `(R)×(R)` into a statement about the **`(T)×(R)` block** — the block the brief
suspected could stay finite while `(R)×(R)` blows up.

> **Lemma D.56.3′ (audit; `PROVED`, unconditional).** Let `φ, ψ : R → R` be measurable.
> (i) If `φ ≥ 0` and `ψ ≥ 0` then `(φ⊛ψ)(w) ≥ 0` for every `w`, with **no hypothesis whatsoever** — a
> supremum of nonnegative numbers.
> (ii) In general, `(φ⊛ψ)(w) < 0` for a given `w` holds **iff** there is `ε > 0` with
> `φ(u)ψ(u+w) ≤ −ε` for **every** `u ∈ R` (this is the definition of a strictly negative supremum).
> In that case `|φ(u)ψ(u+w)| ≥ ε` for all `u`, hence `∫_R|φ(u)ψ(u+w)|du = +∞` and the cross-correlation
> of Lemma D.55.4 satisfies `χ_{φ,ψ}(w) = −∞`.
> (iii) If in addition `φ, ψ` are continuous and `p_w(u) := φ(u)ψ(u+w) → 0` along any sequence
> `|u| → ∞`, then `(φ⊛ψ)(w) ≥ 0`; and if merely `p_w ∈ L¹(R)` then `(φ⊛ψ)(w) ≥ 0`, since an `L¹`
> function cannot satisfy `p_w ≤ −ε < 0` everywhere. *In particular `φ, ψ ∈ L²` suffices, by
> Cauchy–Schwarz — which is the statement the builder wanted and did not prove.*

Now run the brief's three escape attempts against D.56.3′:

* **`φ, ψ ≥ 0` with non-decaying tails, e.g. `ψ(w) ≍ e^{|w|/2}` mimicking the Weil density
  `w_{2K} = 2\cosh(w/2)`.** Dead on arrival by (i): sign, not decay, is what makes `φ⊛ψ ≥ 0`. The
  builder's decay hypothesis was never needed in the nonnegative case, and the `w_{2K}`-growth idea
  cannot help because growth does not produce a negative supremum. Note the brief's own arithmetic is
  right and is worth recording: the `(T)×(R)` block **can** stay finite with a growing `ψ`
  (`χ_{φ,ψ}(w) = ∫φ(u)ψ(u+w)du` finite if `φ` decays faster than `e^{−|u|/2}`, and then
  `χ_{φ,ψ}(w) = O(e^{|w|/2})`, integrable against `Φ = O(e^{−(1+ε)|w|})` by (11.1)) while `(R)×(R)` is
  `+∞`. **So the loophole the brief names is real as a statement about the two blocks — and it buys
  nothing, because the collapse never depended on either block for nonnegative data.**
* **Signed `φ` or `ψ`.** By (ii), enlarging the shadow at a single `w` forces `χ_{φ,ψ}(w) = −∞`, i.e.
  it destroys the **`(T)×(R)`** block, not merely `(R)×(R)`. This is the strengthening: the escape is
  coextensive with the collapse of the *weaker* of the two blocks, so **no intermediate carrier exists**
  between "shadow `= 𝓔`" and "`B` undefined against every `(T)` test".
* **Does a null set of bad `w` help?** No, and this is the clean plug. `D^W ⊂ C²(R)`, so `Φ` is
  continuous. If `Φ ≥ φ⊛ψ` and `{w : (φ⊛ψ)(w) < 0}` has empty interior, then `Φ ≥ 0` off a set with
  empty interior, hence `Φ ≥ 0` everywhere by continuity. So an enlargement of the shadow requires
  `(φ⊛ψ) < 0` on a **nonempty open set `W⁻`**, hence `χ_{φ,ψ} ≡ −∞` on `W⁻`, hence
  `B(k_Φ, φ⊗ψ) = −∞` for every `Φ` that is `> 0` somewhere on `W⁻`. `PROVED`.

> **Corollary (audit, R-1a; `PROVED`).** `𝓣(M) ⊋ 𝓔 ∪ \{0\}` is possible **only** for pairs `(φ,ψ)`
> for which the `(T)×(R)` block of `B` is `−∞` against a nonempty open set of translation tests.
> Theorem D.56.4's conclusion therefore holds on the **entire domain of definition of `B`**, and not
> merely on `D^W × D^W` — which is what the builder asserted and did not have.

### 1.4 **FINDING A-2 (a real gap in coverage). D.56.2–D.56.4 are stated for a single rank-one kernel,
### but `(R)` is defined (D.55.1) as the finite real span.**

For `k = k_Φ − Σ_{i=1}^n φ_i⊗ψ_i ≥ 0` the condition is `Φ(w) ≥ sup_u Σ_i φ_i(u)ψ_i(u+w)`, and the
nonnegativity of that supremum is **not** an instance of anything proved: the summands may have mixed
signs, so (i) of D.56.3′ does not apply. The conclusion survives — under (11.1) the sum tends to `0`, so
the sup is `≥ 0`; and under `L²` factors, `Σ_i p_i^{(w)} ∈ L¹` and (iii) applies — but **the finite-rank
case is nowhere stated or proved in round 1**, while D.55.1 explicitly admits it and D.55.2's proof is
written for `n` summands. **REPAIR R-2: state and prove D.56.2/D.56.3/D.56.4 for finite rank.** Without
it, Thm D.56.4's `𝓣(M) = 𝓔 ∪ {0}` is proved for a proper subfamily of the cone the phase declares.

### 1.5 The `k_Φ + φ⊗ψ ≥ 0` quadrant (O-148.3): the builder is wrong twice, and the audit closes it

The brief is right that this is the direction that would *enlarge* the shadow, and right about the
formula. `k_Φ + φ⊗ψ ≥ 0 ⟺ Φ(w) ≥ −inf_u φ(u)ψ(u+w) = −(φ ⊛_{\min} ψ)(w)`. The builder recorded
O-148.3 as *"the one direction Theorem D.56.4 does not close … probably ill-posed"*. Two objections:

* **it is not a separate direction.** `k_Φ + φ⊗ψ = k_Φ − φ⊗(−ψ)`, so the `+` quadrant is exactly the
  `−` quadrant with **signed** data. It is therefore governed by D.56.3′(ii), not unexamined;
* **it closes, by the same lemma.** `inf_u φ(u)ψ(u+w) > 0` for a given `w` requires
  `φ(u)ψ(u+w) ≥ ε > 0` for **all** `u` (this is what "bounded below by positive constants, not decaying"
  means), hence `χ_{φ,ψ}(w) = +∞` and `B(k_Φ, φ⊗ψ) = +∞`. With `φ, ψ > 0` decaying, `inf = 0` and
  `Φ ≥ 0` again — exactly as the brief computes. So:

> **Theorem D.56.4′ (audit; `PROVED`).** For either sign, `k_Φ ∓ φ⊗ψ ≥ 0` with the `(T)×(R)` block of
> `B` finite (i.e. `χ_{φ,ψ}(w) ∈ R` for a.e. `w`, the minimum for `B` to exist) implies `Φ ≥ 0`. The
> translation shadow of the **full** quadrant, both signs, is `𝓔 ∪ {0}`.

**REPAIR R-3: O-148.3 must be moved from `OPEN` to `CLOSED (audit D.56.4′)`, and the builder's reason
for leaving it open — "the enlarged `Φ` would fail Thm 11.13(i) `\deg Φ > 0`, so the normalisation in
Def. D.56.5 breaks and there is no support function to compare" — must be withdrawn.** That reason is a
non-argument: a cone whose elements have `deg ≤ 0` is not "ill-posed", it is a cone one restricts to
`deg > 0`, and Def. D.56.5 already carries `deg Φ > 0` as a side condition. The real reason is
D.56.4′. Leaving a closed quadrant flagged as "the one direction the collapse does not close" in a
closing document is the single most dangerous sentence in round 1: it is an invitation to reopen the
square on a false premise.

### 1.6 Is the negative *forced*? Yes, on the declared carrier — with one honest caveat

Collecting §§1.3–1.5: on `𝒦 = (T) ⊕ (R)` with `B` defined (finite `(T)×(R)` block), the shadow is `𝓔`,
for either sign, for finite rank, for signed factors, for non-decaying factors, and for factors mimicking
`2\cosh(w/2)`. **The kill is forced and is now proved at full strength.** The caveat is §5 below: the
classes that classical and tropical intersection theory actually uses on a square are `f_1 = C×\{pt\}`
and `f_2 = \{pt\}×C`, which are *not* in `(T) ⊕ (R)` at all. That is O-148.2, and it is not idle.

---

## §2 — Item 2: the form `B`, and the three consistency findings

### 2.1 (a) Two representing densities — **proved, and not a contradiction; the write-up invites one**

Thm D.55.6 is correct and its proof is complete: `B(k_Ψ,k_Φ) = ∫Ψ w_Φ` is Paper 46 Thm 11.14(i);
`B(φ⊗ψ,k_Φ) = ∫χ_{φ,ψ}Φ` is Lemma D.55.4; and at `Φ = 2K` the two densities `2\cosh(w/2)` and `2K` are
verified distinct from Thm 11.7(ii) plus `Φ_{2K}(0) = Φ_{2K}(1) = 1`, `Φ_{2K}(1−ρ) = 2ξ(1−ρ) = 0`.
`PROVED`, unconditional. **Reconciliation the brief asks for:** there is **no** inconsistency, and `B`
**is** a single well-defined bilinear form. The two displays in (148.1) pair *different arguments*
(`Ψ ∈ D^W` in the first, `χ_{φ,ψ} ∈ D^W` in the second) through *different representations*; they would
conflict only if some `k` admitted both readings, and Thm D.55.2 (`(T) ∩ (R) = 0`) says none does. What
Thm D.55.6 actually proves is the **non-existence of a common radial coordinate**: there is no linear
`R : 𝒦 → D^W` with `B(k, k_Φ) = ∫R(k)·w_Φ` for all `k`. That is Cor. D.55.7 and it is correctly proved.
**REPAIR R-4: rename "density anomaly" and state it as the non-existence of a common radial
representation; delete the implication that `B` is in any tension with itself.** As written ("well
defined AND a density anomaly") the round-1 text reads as a self-contradiction and will be quoted as one.

### 2.2 (b) No radial projection / no degree — **proved, but D.55.7(i)'s last clause is over-strong**

`R_{mean}(k_Φ) = Φ`, `R_{mean}(φ⊗ψ) = 0`, `R_{int}(φ⊗ψ) = χ_{φ,ψ}`, `R_{int}(k_Φ) ≡ +∞`: all four are
one-line computations and all four are right. The **no-degree** claim (ii) is right and its positivity
step is right (`2\cosh(w/2) − 2K(w) > 0` outside a compact set by Thm 11.7(ii), `χ_{φ,ψ} ≥ 0` continuous
and `≢ 0`). But the clause *"and **no** linear map `𝒦 → D^W` restricting to the identity on `(T)` and to
`φ⊗ψ ↦ χ_{φ,ψ}` on `(R)` is a limit of diagonal averages"* is **asserted, not proved**: nothing in the
proof paragraph addresses maps that are not `R_{mean}` or `R_{int}`. In fact, by directness (D.55.2),
such a linear map **trivially exists** — define it blockwise. What is true is that it is not a limit of
diagonal averages and not continuous along Thm D.55.8's limit. **REPAIR R-5: replace "no linear map
exists" with "the blockwise map exists but is not a limit of diagonal averages (Thm D.55.8)".** As
stated, D.55.7(i)'s last clause is **false**.

### 2.3 (c) Linear divergence in the cutoff — **proved, trivially; the CC identification is rhetoric**

Thm D.55.8 is correct: `B` is `T_a`-invariant, `T_a k_Φ = k_Φ`, so the integrand is constant in `a` and
`B(2Λ·A_Λ(φ⊗ψ), k_Φ) = 2Λ∫Φχ_{φ,ψ}`. **But this is not a discovery about `B`; it is the observation
that a quantity rescaled by `2Λ` diverges when the unrescaled quantity has a nonzero limit-free constant
value.** `B(A_Λ(φ⊗ψ), k_Φ) = ∫Φχ_{φ,ψ}` is *constant* in `Λ`; the divergence is inserted by hand through
the normalisation chosen in (i) to make the pointwise limit land on `k_{χ}`. The finding that survives is
real and worth one sentence — *the normalisation that makes `(R)` converge to `(T)` pointwise is not the
normalisation under which `B` converges* — but:

**DOWNGRADE 1.** The label *"`RESTATEMENT` of the known obstruction [CC's delicate principal values],
with a new and elementary witness"*, and README's *"exhibits, in two lines, the 'delicate principal
values' that Connes–Consani themselves name"*, must be downgraded to **`ANALOGY`, not `RESTATEMENT`**.
CC's obstruction concerns the principal-value regularisation of a trace on the square of the scaling
site; Thm D.55.8 exhibits a scale-linear normalisation mismatch between two elementary blocks of a form
the phase itself defined. Nothing connects them beyond both involving a divergence. Per the blueprint's
own warning (*"Do not import Connes–Consani theorems as if they were about the square"*) this is the one
place round 1 comes close to violating its orders. Finding **F-148-1**'s substance stands; its CC gloss
does not.

### 2.4 **FINDING A-3 (a headline that must be WITHDRAWN as stated).**

Thm D.55.5 is titled *"the three blocks are the three restrictions of one composition trace"*. Items
(i)–(iv) are each correct. The **title is not**: (i) is a **regularised** trace (Paper 46 Def. 11.4,
`⟨(Φ⋆Φ'^∨)_{ev}, W_{fin}+ω_∞⟩`), (ii)–(iii) are **honest** traces of trace-class operators, and the
builder's own Thm D.55.8 is the proof that **no single trace functional restricts to both** — that is
exactly what the linear divergence says. So the phase asserts a unification in D.55.5 and refutes it in
D.55.8, three pages apart. **REPAIR R-6 / WITHDRAW the title:** the three blocks are three traces
computed by **two inequivalent prescriptions**, glued by fiat along the direct-sum decomposition
D.55.2. The gluing is legitimate (directness makes it well defined) and should be stated as a *choice*,
which is what the blueprint asked to be recorded (*"the first thing that can fail: record it"*). The
content (i)–(iv) of D.55.5 stands unchanged; only the unification claim goes.

---

## §3 — Item 3: D.56.4's proof, D.56.6–D.56.11, the zero-blind block, `Ξ_a`

* **Thm D.56.4** — proof complete given Lemma D.56.3, with the coverage gap A-2 (finite rank) and the
  hypothesis error A-1 repaired by R-1/R-2. The `⊇` direction takes `φ = ψ = 0`, i.e. it does not use the
  square at all; that is correct but should be said, since it means `𝓣(M) ⊇ 𝓔` is content-free.
  **STANDS after repair.**
* **Thm D.56.6** (`s^{(M)} = s`) — the `≤` step is Lemma 19.17 verbatim (verified in `main.md:6167–6177`,
  `E' ≥ 0 ⟹ |Re(e^{iθ}Φ_{E'}(ρ))| ≤ ½s(γ,θ)\deg E'`), applicable because the shadow is `𝓔`; the `≥`
  step is the bump argument of D.31.2(i), and `E'_δ ∈ 𝓔 ⊆ 𝓣(M)` is legitimate. Normalisation matches
  Def. 19.16/Prop. 19.18. **STANDS.** Note it is a **corollary of D.56.4 and nothing else** — the square
  contributes zero to it.
* **Cor. D.56.7** ((b′)⁺_X ⟺ (b′)⁺) — immediate from D.56.4; Thm 19.23 (`main.md:6292–6306`) then applies
  at the same witness `tF_0 + dK` and the same threshold `d²(1−s_1²) > d − 4χ`. **STANDS.**
* **Thm D.56.8, the "zero-blind `(T)×(R)` block"** — (148.2) is correct. Part (i) (*"numerically
  identical for `ξ`, `Ξ_a`, `Ξ_Q`, every `ζ_K`"*) is true **pointwise in `(Φ,φ,ψ,X)`** and is quietly
  false for any *optimised* quantity: the admissibility constraint `Ψ ≥ φ⊛ψ` couples the sectors, and
  nothing forbids choosing `φ,ψ` as functions of `ξ`-data. **DOWNGRADE 2: restrict (i) to "the
  integrand contains no zeta data", and drop the word "numerically identical" for suprema.** The
  disqualifier that actually carries the argument is (ii), **non-`𝓝_∞`-invariance**, which is proved and
  is the correct instrument (D.31.2(iii)). **STANDS as repaired.**
* **Cor. D.56.9** — (i),(ii),(iii) correct; (ii)'s variation argument (fix `Ψ`, move `(φ,ψ)` inside
  `Ψ ≥ φ⊛ψ`, `I_∞(Ψ,X)` fixed and `∫Xχ` moves) is a genuine proof that the extra term is a
  representative-level quantity. **STANDS.** O-148.5 correctly declared idle.
* **D.56.10/D.56.11, the `Ξ_a` check** — correct and correctly used. Every new object is `Ξ_a`-blind;
  the only `ξ`-dependent ingredients are `I_∞` and `s(γ_1,π/2)`. The builder also gets the epistemology
  right, which auditors of this corpus usually have to supply: `Ξ_a`-blindness *condemns a positive* and
  is *neutral for a negative*. Since the conclusion is a negative, the blindness is the **proof that no
  A3 step was smuggled in**, not a defect. **STANDS.**
* **Prop. D.56.12** (ceiling) — an honest `RESTATEMENT` of R140_001 D.23.13, correctly flagged as such,
  and correctly conditioned on D.23.13(iv)'s finiteness hypothesis. **STANDS.**

---

## §4 — Item 4: labels, and the grid-based claims

Script re-run (`--fast`, `mp.dps = 25`) reproduces round 1 exactly:
`s_1 = 0.9984601627188091092345474`, `u^* = −0.1109915633705136940835335`,
`1−s_1 = 1.539837281190890765×10^{−3}`, `1−s_1² = 3.077303463529236×10^{−3}`,
`d_0 = 324.9598266311831410805725`; part (b) worst ratio `0.697289926730959`, margin `+0.30117024`;
(c) `δ = 0.002 → 0.998060777767119`, margin `+3.9938495×10^{−4}`; (d) `t = 10^8 → 0.998050575243726`,
margin `+4.0958748×10^{−4}`; (e) `∫Φχ = 0.810907325613`, `2Λ∫Φχ` linear in `Λ`. Every margin `≥ 0`.

Two audit checks on the certificate itself:

* **the scan window is legitimate but unjustified in the script.** `s_of` scans only `|u| ≤ 1.6`. That is
  rigorous — for `|u| > 1.6`, `|\cos(γu+θ)|/\cosh(u/2) ≤ 1/\cosh(0.8) = 0.74810… < s_1` — and it is the
  same a-priori enclosure Prop. 19.18 states at `|u| ≥ 0.2`. **REPAIR R-7: put the enclosure bound in
  the script as an assertion, not in the auditor's head.** Uncommented, a `4000`-point scan on a hard
  interval is exactly the kind of step that has to be re-derived by every later reader.
* **parts (b), (c), (d) certify nothing about the theorem.** Every `Φ` sampled is nonnegative by
  construction, so Lemma 19.17 bounds it by `s_1` *a priori*; the margins cannot be negative whatever the
  grid does. They are consistency checks on the code, not evidence for D.56.6. Part (e) prints
  `2Λ × 0.8109…` for four values of `Λ`, which is multiplication. **README's "Every margin is ≥ 0" must
  not be read as support for the kill**, and the label `CERTIFIED` is appropriate **only** for the
  constants of part (a) (`s_1`, `u^*`, `1−s_1²`, `d_0`), which are a scan-plus-Newton evaluation of an
  explicit elementary function inside a proved enclosure, with margins.

### Label disposition

| statement | round-1 label | audit |
|---|---|---|
| D.55.2 `(T) ∩ (R) = 0` | `PROVED` | **STANDS** (exponential-polynomial argument correct; (11.1) two-sided decay kills every `p_j`) |
| D.55.4 `(T)×(R)` block finite, `= ∫Φχ_{φ,ψ}` | `PROVED` | **STANDS** |
| D.55.5 items (i)–(iv) | `PROVED` | **STANDS** |
| D.55.5 **title**, "three restrictions of one composition trace" | `PROVED` | **WITHDRAW as stated** (A-3; regularised vs honest trace; contradicted by D.55.8) |
| D.55.6 density anomaly | `PROVED` | **STANDS**, rename per R-4 (it is non-existence of a common radial representation, not a defect of `B`) |
| D.55.7(i) two candidate projections | `PROVED` | **STANDS except the last clause**, which is false as written → R-5 |
| D.55.7(ii) no degree | `PROVED` | **STANDS** |
| D.55.8 block divergence | `PROVED` | **STANDS** (trivial: `T_a`-invariance) |
| F-148-1 as CC's "delicate principal values" | `RESTATEMENT` + `IMPORTED` | **DOWNGRADE → `ANALOGY`** (DOWNGRADE 1) |
| D.56.1 `(max,+)` structure | `IMPORTED` | **STANDS** |
| D.56.2 tropical characterisation | `PROVED`, NEW as a condition | **STANDS**; "NEW" survives the corpus check in §5 **only** as *"as a condition on a kernel"* |
| D.56.3 `φ⊛ψ ≥ 0` | `PROVED` | **DOWNGRADE → `PROVED` only on `D^W`; the "more generally, `(R)×(R)` finite" clause is REFUTED** (A-1). Replaced and strengthened by **D.56.3′** (R-1) |
| D.56.4 the kill, `𝓣(M) = 𝓔 ∪ {0}` | `PROVED` | **STANDS for rank one; EXTEND to finite rank** (A-2, R-2); strengthened to both signs by **D.56.4′** (R-3) |
| D.56.6 `s^{(M)} = s`, `s_1` unchanged | `PROVED` | **STANDS** |
| `s_1`, `u^*`, `d_0` numerics | `CERTIFIED` | **STANDS** for part (a) only; parts (b)–(e) are **not** certification of anything (R-7 + §4) |
| D.56.7 (b′)⁺_X ⟺ (b′)⁺ | `PROVED` | **STANDS** |
| D.56.8(i) "numerically identical for `ξ`, `Ξ_a`, …" | `PROVED` | **DOWNGRADE 2**: true pointwise, not for suprema; (ii) is the load-bearing part and **STANDS** |
| D.56.9 no member of (★) | `PROVED` | **STANDS** |
| D.56.10/11 `Ξ_a`-uniform, no A3 step | `PROVED` | **STANDS** |
| D.56.12 ceiling | `RESTATEMENT`+`PROVED` | **STANDS** |
| O-148.3 `k_Φ + φ⊗ψ` quadrant | `OPEN`, "probably ill-posed" | **WITHDRAW the status: CLOSED** by D.56.4′ (R-3); the stated reason (degree normalisation) is a non-argument |
| O-148.2 larger kernel class with a degree | `OPEN`, outside `B`'s domain | **STANDS, and must be UPGRADED to the phase's principal residue** (§5) |
| corpus row "phase-41 doc 125 … not used below" | — | **WRONG** (§5) — the row must be rewritten |
| row D | no label, no sign | **STANDS** |
| positivity of `B` anywhere outside the HS block | NOT ASSERTED | **CONFIRMED.** W-a is respected throughout; I found no covert positivity assertion |

---

## §5 — Item 5: phase-41 Doc 125, and the corpus row that is wrong

`03-research/phase-41-build-G2/125-forma-interseccion-cuadrado.md` (Trejo Pizzo, June 2026) is *"la forma
de intersección sobre el cuadrado del sitio de escala"*. Round 1's corpus table lists it as the "tropical
toy Hodge index" file, verdict "TRIED–NO-GO, **not used below**". **That row is wrong: doc 125 is the
same construction as §D.55, one level up, and it both anticipates and cuts against round 1.**

**Anticipation (three exact hits).**
1. Doc 125 §2.4 defines on `C_p × C_p = (R/(\log p)Z)²` the correspondences
   `F_μ : Δ_μ = \{v = u + \logμ\}` — *"una **traslación de la diagonal**"*. Phase 148's `(T)` kernel
   `k_Φ(u,v) = Φ(v−u)` is **exactly a superposition of doc 125's `Δ_μ` with density `Φ`**. The builder's
   `(T)` sector is doc 125's flow-correspondence family, smeared. §0's "not used below" is therefore
   false at the level of the object, not merely of the technique.
2. Doc 125 §2.4 defines `f_1 = C_p × \{v_0\}` and `f_2 = \{u_0\} × C_p`. These are the degenerate
   rank-one classes `δ_{v_0}` in one variable and `1` in the other — **precisely the `(R)`-type kernels
   phase 148 excludes**, being neither `L²` nor decaying.
3. Doc 125 §1.3 and §5.3 compute the Gram matrix on `⟨f_1,f_2,Δ⟩` with `f_1·f_2 = 1`, `Δ·f_1 = Δ·f_2 = 1`,
   `Δ² = 0` (`g = 1`), signature `(1,2) = (1,ρ_{toy}−1)`, **negative definite on the primitive part** —
   the Hodge-index signature, in the finite toy.

**Contradiction, and it is the interesting one.** Doc 125's pairing gives `f_1 · f_2 = 1`: a **finite,
nonzero** intersection number between exactly the two classes on which phase 148's `B` is undefined
(`R_{int}(k_Φ) ≡ +∞`, Cor. D.55.7(i); and `f_1, f_2` are not Hilbert–Schmidt, so the `(R)×(R)` block does
not see them either). So the intersection theory that *does* produce the Hodge signature on the square
pairs precisely the classes phase 148's form cannot pair, and produces **integers** where phase 148
produces divergences. Phase 148 has not shown that no intersection theory exists on the square; it has
shown that **the one form it wrote down, on the one domain it chose, is trivial and blind**.

**But doc 125 also bounds the prize, and here it supports the negative.** Doc 125's own result 4/§5.5 is
that the toy's signature *does not survive the passage to infinite rank* (slopes dense in `R`,
tension T2 of Doc 119, and the Babaee–Huh example of a tropical surface whose intersection form **lacks**
the Hodge-index signature); its §6 leaves two gaps (G-125.A integrality of the intersection number on the
flow correspondences — generically **real, not integer**; G-125.B persistence of the signature), and its
R-NC test verdict is that eventual positivity reduces to the Lefschetz formula, i.e. **circular (fails
NC3)**. The standing verdict TRIED–NO-GO is confirmed and phase 148 does not disturb it.

**REPAIR R-8 (supersedes the §0 row): rewrite the doc-125 corpus row to read "same object — the `(T)`
sector is doc 125's translation correspondences `Δ_μ` smeared by `Φ`; doc 125's `f_1, f_2` lie outside
`(T) ⊕ (R)` and are paired finitely there, which is O-148.2 made concrete; doc 125's independent
obstructions (real-not-integer intersection numbers; Babaee–Huh non-persistence of signature; NC3
circularity) bound what any square can deliver and are not repaired by phase 148."**

---

## §6 — Required repairs, in order

* **R-1 (blocking).** Replace Lemma D.56.3 by D.56.3′; delete "Hilbert–Schmidt ⟹ vanishing at infinity"
  from D.56.4's remark, §D.58 and the Recommendation; state Cor. R-1a (escape `⟺` `(T)×(R)` block is
  `−∞` on an open set) and the continuity plug (`Φ ∈ C²` ⟹ a null set of bad `w` cannot help).
* **R-2 (blocking).** Prove D.56.2/D.56.3/D.56.4 for **finite rank**, matching D.55.1's own definition.
* **R-3 (blocking).** O-148.3 → **CLOSED** by D.56.4′; withdraw the degree-normalisation excuse.
* **R-4.** Rename the "density anomaly"; state explicitly that `B` is well defined and that the anomaly
  is the non-existence of a common radial representation.
* **R-5.** Fix D.55.7(i)'s last clause (a blockwise linear map exists; it is not an averaging limit).
* **R-6.** Withdraw D.55.5's title; record the gluing of a regularised with an honest trace as a
  **choice**, per the blueprint's "record it".
* **R-7.** Put the `|u| ≤ 1.6` enclosure into the script as an assertion; restrict `CERTIFIED` to
  part (a); relabel (b)–(e) as consistency prints in the README.
* **R-8.** Rewrite the doc-125 corpus row; upgrade **O-148.2** from a footnote to the phase's principal
  open residue, with doc 125's `f_1·f_2 = 1` as its concrete instance.
* **DOWNGRADE 1** (CC "delicate principal values" → `ANALOGY`) and **DOWNGRADE 2** (D.56.8(i) pointwise
  only) applied in the labels table and in the README headline.

Nothing above changes the phase's outcome, the constant `s_1`, the threshold `d_0`, or any label in
Paper 46. **No FATAL flag. Theorems 19.21–19.25 untouched. Row D: no label, no sign — confirmed.**

---

## §7 — The closing paragraph the brief asks for

**The negative closing is justified, and item 1 does not leave a live direction inside the declared
carrier — but the builder proved it for the wrong reason, and the right reason is stronger.** The
collapse does not depend on Hilbert–Schmidt finiteness, does not depend on decay, and does not depend on
the sign convention: for nonnegative factors `φ⊛ψ ≥ 0` is a supremum of nonnegative numbers and no
growth condition can touch it, so the brief's `ψ ≍ e^{|w|/2}` Weil-density escape is closed before it
starts; for signed factors, and for the `+` quadrant the builder left open, a strictly negative
(resp. strictly positive) tropical bound at a single `w` forces the product `φ(·)ψ(·+w)` to be bounded
away from zero on **all** of `R`, hence `χ_{φ,ψ}(w) = ∓∞`, hence the **`(T)×(R)`** block — not merely the
`(R)×(R)` block — is undefined there; and since `D^W ⊂ C²`, an enlargement of the shadow needs a
*nonempty open* set of such `w`, so `B` fails against an open set of translation tests. The loophole the
brief identified is real as a statement about the two blocks (a growing `ψ` genuinely can keep `(T)×(R)`
finite while `(R)×(R)` diverges), and it is empty as a route, because the collapse was never a fact about
either block for the data that could have used it. So `𝓣(M) = 𝓔`, `s^{(M)}(γ_1,π/2) = s_1`, (b′)⁺_X ⟺
(b′)⁺, outcome (i). **The live direction that does remain is not item 1 but O-148.2, and phase-41 doc 125
names it concretely:** the classes that carry the Hodge signature on a square — `f_1 = C×\{pt\}`,
`f_2 = \{pt\}×C`, with `f_1·f_2 = 1` — are exactly the classes outside `(T) ⊕ (R)`, paired finitely by a
tropical stable intersection and infinitely by `B`. Phase 148 has proved that *its* form on *its* domain
is trivial and zero-blind; it has not proved that the square admits no intersection theory, and it should
not be written as though it had. Doc 125 already bounds that residue from the other side (intersection
numbers generically real not integer; Babaee–Huh non-persistence of the signature at infinite rank; NC3
circularity), which is why the recommendation to close the square is still the right one — but the
closing document must close it on doc 125's obstructions plus D.56.4′, not on the false premise that
Hilbert–Schmidt finiteness forces the collapse.
