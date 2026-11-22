# R139.004 — Confirmation, phase 139

* Object: the **current** `R139_001_ROUND1.md`
(1371 lines, round-2 repairs applied in place) and `README.md`. `R139_003_ROUND2.md` was read
as a map only; **every finding below was checked against the repaired text, not against the ledger**.
The round-1 files are not edited.*

**Overall verdict: CONFIRMED, with one MAJOR residue (H17) that is a one-line repair.**
16/16 audit findings are genuinely closed in the files. Two repairs are new mathematics and both
survive an independent re-derivation: **H8**'s contour-shift construction of `K_K` (I verified the Stirling
exponent, the shift, and the evenness/reality argument) and **H5**'s conjugate-packet lemma. The
residue is that the repair of H7 introduced an inconsistency this round did not notice: the class
`𝒵` over which `(P139)` is now stated is defined by A1–A6 + A2⁺, which **excludes `Ξ_a`** — the very
function (AT-2) and the unsatisfiability argument need it to contain. No FATAL. No label change.

---

## 1. Per-finding status (checked against the repaired files)

| # | Sev. | Status | Verification |
|---|---|---|---|
| **H1** | MAJOR | **CLOSED** | (0.1) at `R139_001:24` now reads `Σ_{p∈P}Φ_F(p)Φ_G(1−p) − Σ_ρ…`, weight one, with the bracket correctly explaining that `Z(p)` enters only through `Φ_{K_Z}(1−p)`. `B_pol^{(Z)}` matches. I re-checked the four downstream constants against the new convention: D.19.2(vi) (`¼\deg F`, `⅛`), D.19.3(v) (`2z²AB`, `z²(A+B)`, `2z²`), D.20.1(iv) (`(r/2)\deg_KF`, `r²/2`) and the reduction "Hodge at even `F` ⟺ `Ŵ ≤ 0`" — all consistent now, none changed. |
| **H2** | MAJOR | **CLOSED (withdrawn correctly)** | Remark D.19.3b (`:343`) is rewritten as "`Ξ_Q` lies outside Proposition 12.6's class", lists exactly the four failed hypotheses, and quotes the paper's own `main.md:3083` note. §7's P47-5 (`:1254`) is downgraded to **EDITORIAL** with the withdrawn text quoted and the sentence "**That is a misreading and it must not reach Paper 47's Part III**" in place. The README row is corrected. The surviving editorial suggestion (two symbols; note that (12.4) is consumed only by Thm 11.14 → Thm 12.3) is accurate and is the right residue to carry to Part III. |
| **H3** | MAJOR | **CLOSED**, one cosmetic residue (H18) | New Definition D.19.3a′ (`:269`). I checked the expansion: `1/(1+W) = Σ_{k≥0}(−1)^kW^k` gives `−W'/(1+W) = Σ_{k≥1}(−1)^kW^{k−1}W'` — index correct; absolute convergence for `σ` large is correct; `σ_a ≥ σ_1` is correct; and the admission "**no theorem places `σ_a` at `σ_1`** for a series without an Euler product" is exactly the point. Theorem D.19.3's hypothesis is now `α > max\{θ_Z, σ_a−½\}` with `c ∈ (σ_a, ½+α)`; `D^W(α)` still contains `K_Q` and `C_c^∞`. |
| **H4** | MAJOR | **CLOSED** | Standing restriction at `:239`. I verified both halves. *Applicability of DH to the principal form:* for the principal class `𝔄_0`, `\overlineχ(𝔄_0) = 1`, so `Z_{Q_0} = \frac1hΣ_χL(s,χ)` is a combination of `h ≥ 2` **distinct** Euler products with all coefficients equal and non-zero — the non-degeneracy Davenport–Heilbronn require; the theorem applies. *Compatibility with D.19.4a:* `x²+ky²` **is** the principal (reduced, `a=1`) form of discriminant `−4k`, and `r_{Q_k}(1) = 1`, so `n_0 = 1` as the restriction demands. The two are compatible and the restriction costs nothing that the round uses. The generalized-Dirichlet-series diagnosis for `n_0 ≥ 2` is correct and is properly parked as O-10. |
| **H5** | MAJOR | **CLOSED**, two residues (H19, H20) | (a) Labels now read `PROVED` abelian / `PROVED-CONDITIONAL` on Artin holomorphy, with the correct reason (a pole of one factor would cancel a zero of another). (b) Conjugate packets: I re-derived Lemma D.20.2a₀ for `χ ≠ \barχ` — `Λ_{[χ]}(1−s) = W(\barχ)^{−1}Λ(s,χ̄)·W(χ)^{−1}Λ(s,χ)` and `W(χ)W(\barχ) = 1` (itself forced by applying the Artin equation twice) — **correct**. (c) The conductor–discriminant factorization `Λ_L = Λ_K∏Λ(s,χ)^{χ(1)}` is exact and the spurious `r_L/r_K`, `u(s)` are gone; with weight-one polar blocks `I_∞^{(L)} = I_∞^{(K)} + Σχ(1)Ŵ^{(Λ_{[χ]})}` is right. |
| **H6** | MAJOR | **CLOSED** | I recomputed clause (c) at `E = mK_K`: `½m²·(r²/2) − ½m·(r²/2) + χ_K = \tfrac{r²}4m² − \tfrac{r²}4m + χ_K`. The displayed line at `:1150` matches, `K_K − mK_K = (1−m)K_K` is right, and the `K = Q` check (`r = 1 ⟹ ¼m²`) now closes against `NOTE_OFF_THE_PAGE_CANDIDATES.md:5-8`. |
| **H7** | MAJOR | **PARTIALLY CLOSED → see H17** | The restatement over a class `𝒵` and the promotion of the naming clause **(N)** are the right repair in shape, and the further defect this round found (the naive "for every `Z ∈ 𝒵`" version is unsatisfiable) is **real**: I checked Paper 47 Theorem 12.4 (`main.md:2945`) and it does say "there **is no** `h⁰_a : D^W → R_{≥0}` satisfying (a), (b′) and (c)". The split — rule defined on `𝒵`, clauses demanded only at `ξ_K` — is correct and well-posed. But the membership condition chosen for `𝒵` is wrong (H17), which breaks both that argument and (AT-2). |
| **H8** | MAJOR | **CLOSED (new proof verified)** | See §2. |
| **H9** | MINOR | **CLOSED** | The "in particular" clause is deleted at `:532`; D.19.6(ii) now says "fails **in its absolute form**", and the bracket records that A8's failure rests on (i) alone. Correct. |
| **H10** | MINOR | **CLOSED** | `:153` now `O(e^{5t/2}e^{−ce^tm_Q})`. Correct (`y_v² ≍ e^{2t}` times `e^{t/2}`). |
| **H11** | MINOR | **CLOSED** | `:287` now `Σ_ρΦ_h(ρ) = Φ_h(0)+Φ_h(1) − ⟨h,W^{(Q)}⟩`. Correct — the polar packet of Thm 11.3 is a sum of residues. |
| **H12** | MINOR | **CLOSED** | `Theorem 3ter.4(i)`, `main.md:1489` at all three places carrying a number (`:563`, `:983`, ledger row W4a `:1043`); (AT-1) carries no theorem number. The two Thm 3ter.6 citations are kept and are correct. |
| **H13** | MINOR | **CLOSED** | A9 now reads "`Z(σ) > 0` for every `σ ∈ R`; equivalently `Z` has no real zero (given `Z(p)>0` on `P` and the functional equation)". I checked the equivalence: no real zero ⟹ constant sign on `R` ⟹ positive, by `Z(p) > 0` at any `p ∈ P ⊂ R`. Correct; `K_Z > 0 ⟹ A9` is recorded as sufficient only. |
| **H14** | MINOR | **CLOSED** | The classical no-real-zero theorem for real **primitive odd** characters is now cited directly (Landau; Davenport §14) and the round-1 justification is withdrawn with the reason. |
| **H15** | MINOR | **CLOSED (sharpened)** | A4 now names `E` (finite product of `Γ`-factors, exponentials `q^s`, and `½s(s−1)`) with `a_n ≥ 0`, `a_{n_0} > 0`; A5 is stated as a conclusion; A6 is the splitting only, the Hodge index on `Λ_Z^+` being derived. The concession that D.19.7c is then a soundness statement is recorded as O-12. This is the honest outcome; the `METHOD-CONSTRAINT` label continues to carry it. |
| **H16** | MINOR | **CLOSED** | `:465` asserts the failure "at `F_T^{(δ)}` **itself**"; the projection is gone. |

---

## 2. Priority 1 — H8: the contour-shift construction of `K_K`, checked in detail

**Verdict: PROVED. The exponent, the polynomial factor, the strip, the shift and the conclusion are
all correct, and the construction genuinely removes the obstruction the audit named.**

* **The Stirling exponent `πd/4` is right.** `|Γ(x+iy)| ≍ e^{−π|y|/2}|y|^{x−½}√{2π}`. The `r_1` real
  places contribute `Γ(s/2)`, i.e. `|Γ(σ/2+iτ/2)| ≍ e^{−π|τ|/4}·\text{poly}`, so `e^{−πr_1|τ|/4}`; the
  `r_2` complex places contribute `Γ(s)`, i.e. `e^{−π|τ|/2}` each, so
  `e^{−πr_2|τ|/2} = e^{−π(2r_2)|τ|/4}`. Product: `e^{−π(r_1+2r_2)|τ|/4} = e^{−πd|τ|/4}` with
  `d = [K:Q]`. **Exactly this round's constant.** The polynomial factor `(1+|τ|)^{M'_A}` absorbs the
  Stirling powers `|τ|^{σ/2−½}`, `|τ|^{σ−½}`, the factor `½s(s−1)`, and (X-a)'s `(1+|τ|)^{N_A}`;
  `|d_K|^{s/2}` is `τ`-independent in modulus. (D.20.0) is correct.
* **The strip.** (X-a) — `ζ_K` of finite order in vertical strips, by Phragmén–Lindelöf between the
  half-plane of absolute convergence and its reflection — is classical and is the right import. One
  wrinkle (H21): as **stated** for `ζ_K` "uniformly on `|σ−½| ≤ A`", the bound is false near the pole
  `s = 1`. The statement that is used and that is true is (D.20.0) for the **entire** function `ξ_K`,
  where `½s(s−1)` has removed the pole.
* **Convergence, smoothness, reality, evenness.** By (D.20.0) at `σ = ½` the defining integral and
  every `∫τ^jξ_K(½+iτ)e^{−iτt}dτ` converge absolutely, so `K_K ∈ C^∞`. Reality/evenness: from
  `ξ_K` real on `R` and `ξ_K(s) = ξ_K(1−s)` one gets `ξ_K(½+iτ) = \overline{ξ_K(½−iτ)} = ξ_K(½−iτ)`,
  so `τ ↦ ξ_K(½+iτ)` is real and even, hence `K_K` is real and even. **Correct** — and note this is
  *cleaner* than the theta route, which had to derive evenness from a functional equation of `Θ`.
* **The shift.** With `f(s) = ξ_K(s)e^{−(s−½)t}`, `K_K(t) = \frac1{2πi}∫_{(½)}f(s)\,ds`; the
  horizontal sides vanish by the exponential decay in `|τ|`; moving to `Re s = ½+A` multiplies the
  integrand's modulus by `e^{−At}`, giving `|K_K(t)| ≤ C_A''e^{−At}`, and moving to `½−A` gives the
  mirror bound. Hence `|K_K(t)| ≤ C_A''e^{−A|t|}` **for every `A`**, i.e. `K_K ∈ D^W(α)` for every
  `α`, with the same for derivatives (the factor `τ^j` is absorbed). `Φ_{K_K}` is then entire and
  equals `ξ_K` on `Re s = ½` by Fourier inversion, hence everywhere. **All steps check.**
* **What it buys.** No theta function, no fundamental domain for the units, no ideal-class
  decomposition — precisely the obstruction of the audit's H8. It also re-proves the *existence* of
  `K_Q` (the explicit form (0.3) is still the theta computation, unchanged and still correct), and it
  is genuinely reusable for any `Z` with polynomial growth in strips and exponential decay in `τ`.
* **Bonus, correctly noted:** Corollary D.19.7d never depended on (iii). That note is right and
  protects the round's sharpest statement.

---

## 3. Priority 2 — H5: the packet bookkeeping

**Verdict: CLOSED, content correct, with two residues.**

* **H19 (MINOR, new).** Lemma D.20.2a₀ as **stated** ("`Λ_{[χ]}(s) = Λ_{[χ]}(1−s)` for every packet")
  is **false for a real `χ` with root number `W(χ) = −1`**: there `Λ(s,χ) = −Λ(1−s,χ)`. The lemma's
  own proof admits this and retreats to "the zero multiset is still `ρ ↦ 1−ρ`-invariant, which is all
  Lemma D.19.5a's Hadamard step uses" — and that retreat is **correct**: from `Λ(1−s) = −Λ(s)` one
  gets `Λ'(1−s) = Λ'(s)` and hence `(Λ'/Λ)(½−z) = −(Λ'/Λ)(½+z)`, the only relation D.19.5a needs.
  But as written the lemma asserts something false and then claims "A1's functional equation holds
  for `Λ_{[χ]}`", which it does not in that case. **Minimal repair:** state the lemma as
  `Λ_{[χ]}(s) = ε_{[χ]}Λ_{[χ]}(1−s)` with `ε_{[χ]} = ±1`, `ε = +1` unless `χ` is real with root
  number `−1`; and record that D.19.5a needs only the zero symmetry and the oddness of `Λ'/Λ`, both
  of which hold for either sign. Nothing downstream changes.
* **H20 (MINOR, new).** Corollary D.20.2a(b)'s `⇒` says "apply the Landau criterion of Lemma D.19.5a
  to each packet … giving RH for each packet". One cannot apply it to a packet from the hypothesis,
  which is about `Ŵ^{(ξ_L)}`, not `Ŵ^{(Λ_{[χ]})}`. The correct route — and clearly the intended one —
  is: apply D.19.5a to **`ξ_L`** (this needs A9 for `ξ_L`), conclude RH for `ξ_L`, then RH for every
  factor because the zero multiset is the union, then `Ŵ ≤ 0` for each packet. **Minimal repair:**
  say so, and state the conditional clause (c) as "A9 for `ξ_L`" rather than "A9 for each packet".
* Theorem D.20.3 is correctly annotated as the unconditional case (`K/Q` abelian, `χ_{−D}` real).

---

## 4. Priority 3–4 — H4 and `(P139)`

H4 is closed (§1). `(P139)` carries one MAJOR residue.

### H17 (MAJOR, new, introduced by the round-2 repair of H7): `𝒵` as defined excludes `Ξ_a`
**Location:** D.21.4, the definition of `𝒵` (`:1115–1118`); the paragraph "Why the requirement is
split"; (AT-2); README row `D.21.4`.
**Exact claim.** "Let `𝔄₀ := ` A1–A6 + A2⁺, and let `𝒵` be the class of all `Z` satisfying `𝔄₀` (by
Theorem D.19.7a, `𝒵` contains `ξ`, every `ξ_K`, **every `Ξ_a` with `0 < a < ½`**, and `Ξ_Q` …)."
**Why wrong.** `𝔄₀` includes **A3 (equimodular polar block)**, and the round's own verification table
(Theorem D.19.7a, `:642`) marks the `Ξ_a` row **`A3 ✗`** — that is the entire point of the `Ξ_a`
falsifier (`p−½ ∈ \{±(½±a)\}` is not of constant modulus). So `Ξ_a ∉ 𝒵`, and the parenthetical
contradicts the table three sections earlier.
**Consequences.** (i) The unsatisfiability argument of the "Why the requirement is split" paragraph —
whose whole force is "`Ξ_a ∈ 𝒵`, and Paper 47 Theorem 12.4 forbids `h⁰_{Ξ_a}`" — does not go through
as stated; with `𝒵` as defined, the naive "(a),(b′),(c) for every `Z ∈ 𝒵`" is **not** shown vacuous,
and the split this round introduced would be unmotivated. (ii) **(AT-2) again denotes nothing**: "the
rule, evaluated at `Z = Ξ_a`" presupposes `Ξ_a ∈ 𝒵`. This is the exact defect H7 was raised to
remove, reintroduced at one remove.
**Minimal repair (one line).** Define `𝒵` by **A1, A2, A2⁺, A4, A5, A6 — A3 not required**. Then
`Ξ_a ∈ 𝒵` (its row is `✓` on all of those), `Ξ_Q` and every `ξ_K` remain in `𝒵`, both acceptance
tests denote something, and the unsatisfiability argument is restored verbatim. **T2 and Transfer
Lemma D.19.7c are untouched**: they quantify over derivations from A1–A6 + A2⁺, and `Ξ_Q` satisfies
A3, so the transfer to `Ξ_Q` is unaffected. Correct the parenthetical, (AT-2) and README row 40.

### Assessment of `(P139)` as the phase-140 deliverable
Once H17 is repaired, **`(P139)` is well-posed and non-vacuous**, and I judge it the right statement
to hand to phase 140:
* **Well-posed.** The rule is asked to be *defined* on `𝒵` and to satisfy (a),(b′),(c) only at
  `Z = ξ_K`; by Theorem 12.3 (available for every `K` by D.20.1(vi)) that is exactly GRH for `ζ_K`.
  The split is forced, not cosmetic: Paper 47 Theorem 12.4 makes the unsplit version unsatisfiable,
  and I verified that theorem's statement directly.
* **Non-vacuous.** Nothing in the round shows `(P139)` unsatisfiable: the obstruction theorems
  (D.19.5, Thm 12.4) bite at `Ξ_Q` and `Ξ_a`, where the clauses are **not** demanded.
* **The growth target is now right** (`r²/4·m²`, `¼m²` at `K = Q`), and it is the phase-136 wall
  verbatim, so `(P139)` is visibly the named single remaining difficulty.
* **One caveat to record for phase 140 (not a defect).** Clause **(N)** is a condition on the
  *proof*, not on the *object*: "names explicitly the line at which it uses A7, A8 or A9" is not a
  mathematical predicate of the rule `Z ↦ h⁰_Z`. That is defensible — it is what makes the acceptance
  tests do work, and this round says so ("the mathematical content of the acceptance tests is
  therefore (N)") — but it means "`(P139)` is solved" is a claim about a manuscript, not only about a
  function. Phase 140 should state (N) as an **audit protocol** attached to `(P139)`, so that the
  construction problem proper stays purely mathematical.
* **Gap to close first (carried from O-9).** (AT-3) requires the `K`-analogue of `Sh_Z` (`Frob_𝔞`,
  `deg_{det} = \log N𝔞`), which is not built. This is kept as O-9 and recommended as the
  first task of phase 140; I concur, and note that H8's contour construction now supplies the
  `K_K` half of the frame it needs.

---

## 5. Priority 5 — H1, H3, H2, H15 spot checks
All four verified in §1. The two things I re-derived rather than read: the weight-one Hodge reduction
(H1) and the Definition D.19.3a′ expansion (H3). Both correct.

## 6. Residue

| # | Sev. | Item |
|---|---|---|
| **H17** | **MAJOR** | `𝒵` defined with A3 excludes `Ξ_a`; breaks the unsatisfiability argument and (AT-2). One-line repair (drop A3 from the membership condition). Also in README row 40. |
| **H18** | MINOR | (D.19.5) and Theorem D.19.6's preamble still qualify the Dirichlet series with "`(Re s > σ_1)`"; after H3 the correct abscissa for that identity as an absolutely convergent series is `σ_a`. |
| **H19** | MINOR | Lemma D.20.2a₀ overstated for a real `χ` with root number `−1`; the content survives with `ε = ±1` (see §3). |
| **H20** | MINOR | Corollary D.20.2a(b)'s `⇒` should be routed through `ξ_L`, and (c)'s A9 clause stated for `ξ_L`. |
| **H21** | MINOR | Import (X-a) as phrased is false at `s = 1`; state it for the entire `ξ_K`, or exclude a disc around `s = 1`. |
| O-2, O-3 | — | Attribution of `K_Q` and of D.19.4a still `OPEN`; unchanged and correctly carried. |
| O-9 | — | `Sh_Z` for a general number field, needed by (AT-3). First task of phase 140. |
| O-10, O-11, O-12 | — | Correctly opened in round 2 (non-principal `Q`; Artin holomorphy; T2's strength = the table's strength). |

## 7. Per-item verdicts

| Item | Verdict |
|---|---|
| **D.19** | **CONFIRMED.** D.19.2, D.19.4a/4b/4a′, D.19.5, D.19.5b, D.19.6(i)/(iii), D.19.7a, D.19.7c, T2, D.19.7d all stand; the Prop-12.6 erratum is properly withdrawn; the principal-form restriction is honest and costs nothing the round uses. Residue: H18. |
| **D.20** | **CONFIRMED.** D.20.1(iii) is now a real proof and a good one (H8). D.20.2 is correctly split into an unconditional abelian case and an Artin-conditional general case, over self-dual packets. Residues: H19, H20, H21. |
| **D.21** | **CONFIRMED PENDING H17.** The ledger and its citations are unchanged and were verified in round 1; `(P139)` has the right growth constant and the right split, but its domain `𝒵` must be corrected before (AT-2) means anything. |
| **Labels** | **ACCEPT.** Two downward relabels (P47-5 → EDITORIAL; D.20.2 → abelian `PROVED` / general `PROVED-CONDITIONAL`) and one scope restriction (principal `Q`); nothing relabelled upward; `METHOD-CONSTRAINT` on T2 unchanged and right. |
| **RH-free definitions** | **ACCEPT.** No object is named by a zero location; `K_K` is now built from `ξ_K` by a transform, which is data, not a zero set. |
| **FATAL screen** | **CLEAN.** Re-run after the repairs. The two statements whose meaning moved — `(P139)` (a construction problem) and Theorem D.20.2 (weaker, conditional) — cannot combine with Paper 47 Theorem 3.7 to give RH or `¬RH`. |
| **README** | **REPAIR**: row 40 carries H17. Otherwise accurate, including the new D.20.1(iii) and D.20.2 rows. |

## 8. Overall

**CONFIRMED — one MAJOR residue (H17, one line) and four MINOR.** Row D: **no label change**; nothing
in this phase asserts a sign for `ξ`. Round 2 did what a repair round should: it retracted the one
claim that was wrong about someone else's text (P47-5), restricted the scope where the mathematics
demanded it (principal `Q`), replaced a sketch with a proof (`K_K` by contour shift), made a
conditional statement conditional (D.20.2), and — the one place it overreached — introduced H17 by
choosing the wrong axiom subset for `𝒵`. Repair H17, H18–H21, and phase 139 can close with `(P139)`
as the phase-140 deliverable.
