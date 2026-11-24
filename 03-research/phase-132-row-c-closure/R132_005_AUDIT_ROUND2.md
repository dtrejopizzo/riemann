# R132.005 — audit of record, row C, phase 132 **round 2** (confirmation pass)

Target:
[Paper 45](../../04-papers/45-row-c-explicit-formula/main.md) as rebuilt in
round 2 — all **25** `[REBUILT, phase 132, round 2]` passages read and
re-derived — plus [README.md](../../04-papers/45-row-c-explicit-formula/README.md),
`scripts/verify_132_explicit_formula.py` (**re-run: 26/26 pass**), and the
five `[phase 132]` cross-paper edits in
[Paper 43](../../04-papers/43-row-a-correspondence-algebra/main.md) and
[Paper 44](../../04-papers/44-row-b-arithmetic-family/main.md).
Inputs: my [R132.002](R132_002_AUDIT_ROUND1.md) (`M1`–`M4`, `m1`–`m7`,
`n1`–`n6`), [R132.003](R132_003_AUDIT_ROUND1.md) (`LF1`–`LF5`),
[R132.004](R132_004_ROUND2.md).

Method, as in round 1: every load-bearing round-2 statement **re-derived**, not
re-read; every cited theorem of Papers 43 and 44 opened and checked against its
own text and hypotheses (in particular Paper 43 Thm 9.7(c),(d) and its proof,
(8.5), (8.5∞), Def. 8A.7d, (14.1)–(14.2); Paper 44 Thm 3bis.7's proof steps,
(8bis.14a),(8bis.14e), Thm 8bis.4(ii)).

---

## Headline

**All four `MAJOR` findings of round 1 are genuinely repaired, and two of the
repairs are, as R132.004 claims, strengthenings.**  Corollary 9.6a is
correct and closes D128 `C9`; Lemma 5.1a is correct and closes the citation
defect that was the gravest item in round 1; (E3a)–(E3d) is an honest ledger;
Theorem 9bis.2′ is a real theorem and discharges clause C.4's polar half by a
residue computation.  R132.004's extension of 9bis.2′ to the **second** Tate
point (`Res_{s=1}A_S = 0`, `Res_{s=1}A = 1`) is correct, is new, and improves
the section; I verified both residues by hand and the script prints both.

**One new `MAJOR` remains**, and it sits on the label's headline sentence:
Corollary 9.6a(iii)'s **third** "equivalently" — *"equivalently for which
`I_∂ ≤ 0` on the primitive radial sector is Weil's criterion"* — and its two
echoes (§14.4 item 1's "the equivalence with Weil's criterion fails"; README
§5) assert a **biconditional that is nowhere proved and is probably false for
`c < 0`**.  What is proved, and what D128 `C9` needed, is uniqueness at the
level of the **identity** (9.9)/(9.10).  The repair is the deletion of one
clause in three places; no mathematics is lost.

Grade: **`WEIL-STRENGTH-COMPLETE` — GRANTED for row C on Paper 43's declared
carrier, conditional on the one-clause repair `R1` and the sweep `r1`–`r8`
(none of which requires new mathematics, and none of which touches a proof).**
§8 gives the exact list that must be recorded beside the label.

---

## 1. Re-derivations that stand (round-2 material only)

**(a) Lemma 5.1a — correct, and the proof is the right one.**  I checked both
legs against their sources.  *Finite places:* for a radial class,
`j_p(u) = (1 at ∞, u at p, 1 elsewhere)` gives `|j_p(u)|_S = 1`, so
`a(u) = h(0) = a(1)` and the regularized unit packet of (8.5) is **identically
zero pointwise**, with no support and no smallness hypothesis — this is
verbatim the radiality step of Paper 44 Thm 3bis.7's proof, and it is *not*
the step that uses `0 ∉ supp h`.  Confirmed in Paper 44.  *Archimedean:*
Paper 43 Theorem 9.7(d) is stated **"For every `H ∈ D_A`"** and its proof
(Fourier inversion into (8.4) plus a termwise domination: shell sums by
`Σ_kp^{−|k|/2}`, unit packets by `c(κ_p)\log p`, `Ŵ_∞` logarithmic against
Schwartz `Ĥ`) carries **no** support hypothesis.  Confirmed by opening the
proof.  So (5.1a) is legitimate exactly where round 1 was not.
I also verified the lemma **independently, by the other route**: from (9.13)
alone, with `dχ|_{𝔠_0} = dτ/2π`, `Ŵ_p(𝔠_0,τ) = Σ_{k≥1}2(\log p)p^{−k/2}\cos(kτ\log p)`
(Paper 43 (9.11)/(9.15) with `θ_p = 0`) and
`(1/2π)∫\hat h(−τ)e^{ikτ\log p}dτ = h(−k\log p)`, the finite part of (5.1a)
falls out with the stated coefficients.  The two routes agree; (5.1a) is right.
The **identity term when `h(0) ≠ 0` is handled correctly by being avoided**:
the paper does not attempt to evaluate (8.5∞)'s `(γ+\log4π)h(0)` counterterm and
`−2h(0)e^{−t/2}` subtraction in closed form — it uses the Plancherel form, of
which that regularization is precisely the reason (`W_∞` is a continuous
functional on all of `D_A` with symbol `Ŵ_∞`).  The consistency clause
(counterterm and subtraction vanish for `0 ∉ supp h`, recovering (5.1)) is
correct.  `M4` **closed.**

**(b) Theorem 9.6 is now correctly proved for `h = F⋆F^†`.**  The only defect
round 1 had at this theorem was the citation; it is now Lemma 5.1a, which
covers `h(0) = ‖F‖²_{L²} > 0`.  Everything else (the rearrangement of (9.6),
the polar-packet identification via Theorem 8.1(i), the window clause
8A.7c(e)) I re-derived in round 1 and it is unchanged.  `PROVED`.

**(c) Corollary 9.6a — the `c`-term is exactly `c‖F‖²_{L²}`, in Paper 43's
normalization.**  Two independent computations, both in the corollary, both
correct and both checked by me:
(1) `(Γ_F⋆Γ_F^†)(1) = ‖Γ_F‖²_{L²(C_S)}`, and with the disintegration
`d^*w = dt⊗μ`, `μ` a **probability** measure, `‖Γ_F‖²_{L²(C_S)} = ∫|F(−t)|²dt
= ‖F‖²_{L²(R)}`;
(2) via (14.1)/(9.13) on `𝔠_0` with `dχ|_{𝔠_0} = dτ/2π`:
`(c/2π)∫|\hat F|²dτ = c‖F‖²` by Plancherel.
The two agree **because** `μ` is a probability measure and `dχ|_{𝔠_0} = dτ/2π`
is the dual of `dt⊗μ` — i.e. the agreement is itself a check that the two
Paper 43 normalizations (Thm 9.14a's disintegration, Thm 9.7b(d)'s Plancherel
constant) are consistent.  They are.  Script (6a),(6b) confirm numerically
(`11.0473792243` both ways).
Part (ii) is right: `M(Γ_F) = (Φ_F(1),Φ_F(0)) = 0` constrains two Mellin
values, nothing else; `F = ΠG` is a primitive witness with `‖F‖² > 0`
(script: `Φ_F(0) = Φ_F(1) = −2.9·10^{−15}`, `‖F‖² = 11.047`).  Part (iii)'s
**first two** clauses — uniqueness for `I^{(c)} = B_nuc`, equivalently for
(9.9)–(9.10) — are immediate and correct.  The **third** clause is `R1` below.

**(d) `c_cut` is honestly separated.**  §14.4 now carries two numbered items:
the identity-class `c` of (8.4) (derived, load-bearing, inherited by row D as a
theorem) and Paper 43 Thm 8.10 / Rem 8A.7e's `c_cut` (a comparison with an
**imported** regularization whose coefficient P123.035 §6 forbids citing,
undetermined, not inherited).  Remark 9.6b(3) says the same in the text, and
Paper 43's obstacle row `c_{cut}` carries the matching `[phase 132]` clause.
The separation is correct and is stated in both papers.  The false sentence
"nothing in row C depends on it" survives **only** inside W45.14, quoting what
is withdrawn (grep: 1 hit).  **`W45.14` disposes of D128 `C9`** — not by
computing `c_cut`, which is not what `C9` asked, but by proving that the Weil
comparison pins the identity-class constant.  That is the disposal, and it is
the correct one.

**(e) Theorem 9bis.2′, both Tate points — verified by hand.**
`ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)`, so
`ξ'/ξ = 1/s + 1/(s−1) − ½\log π + ½ψ(s/2) + ζ'/ζ`, hence
`A = ½\log π − ½ψ(s/2) − ζ'/ζ = −ξ'/ξ + 1/s + 1/(s−1)` ✔, and
`ξ(0) = ξ(1) = ½ ≠ 0` ✔ (the zero of `s−1` kills `ζ`'s pole, the zero of `s`
kills `Γ(s/2)`'s), so `Res_{s=0}A = Res_{s=1}A = 1`, **chart-independently** ✔.
At a chart: `a(s) = ½\log π − ½ψ(s/2)` has **no** pole at `s = 1`
(`ψ(½) = −γ−2\log2`, finite) ✔, and `f_p(s) = (\log p)p^{−s}/(1−p^{−s})` has
poles only on `(2πi/\log p)Z`, which never meets `s = 1`, so
`f_p(1) = (\log p)/(p−1) < ∞` ✔ — a finite chart has **no pole at all** at
`s = 1`, hence `Res_{s=1}A_S = 0` ✔; while at `s = 0`, `−½ψ(s/2) = 1/s + O(1)`
and `f_p(s) = 1/s + O(1)` give `Res_{s=0}A_S = |S_f|+1` ✔ (Paper 43
Thm 9.7b(c)).  Script (3c′) prints `0` to `2·10^{−37}` and `1` to `2·10^{−33}`.
The reading is exactly right and the asymmetry is real: **at `s = 0` the chart
overcounts and the excess evaporates** (the tail supplies one `1/s` per omitted
prime while the continuation `−ζ'/ζ` is regular at `0`, `ζ(0) = −½`);
**at `s = 1` the chart undercounts and the pole is created in the limit** by
`ζ`'s pole.  Part (iv)'s identification of the pair with the polar packet is
Theorem 9.4(a)'s rectangle residues `g(0), g(1)` against the *same* `A_0`, so
the coefficient really is exactly `1` each; and the `s = 0 ↔ e_+`,
`s = 1 ↔ e_−` assignment agrees with Remark 8.2 (`λ_+(Γ_F) = Φ_F(0)`).
`M3` **closed, and improved beyond the brief.**

**(f) The Mertens clause is now used correctly, and it is still quarantined in
substance.**  Thm 9bis.4(iii)'s computation is right:
`Σ_{p≤x}\frac{\log p}{p−1} = Σ_{p≤x}Σ_{k≥1}\frac{\log p}{p^k}
= Σ_{N≤x}\frac{Λ(N)}{N} + O(1) = \log x + O(1)` — I checked the discarded
terms (`p ≤ x`, `p^k > x`) are `O(1)`, both for `p ≤ √x` (each `≤ 2\log p/x`,
summing to `O(θ(x)/x)`) and for `√x < p ≤ x` (`Σ\log p/p² < ∞`).  And
`−ζ'/ζ(σ) = 1/(σ−1)+O(1)` as `σ↓1`.  So the *rate* statement is a theorem, its
subject is `s = 1`, and Corollary 9bis.3's non-commutation at `s = 0` needs no
Mertens at all — round 1's blueprint refutation stands and is now sharper.  Two
book-keeping defects attach to it (`r5`, `r6` below), neither mathematical.

**(g) Corollary 9.4a — correct.**  `Φ_h(1−s) = ∫h(−u)e^{(s−½)u}du`, so
`g(1−s) = g(s)` **is** evenness of `h` ✔; `g(½+iτ) = \hat h(−τ) = \hat h(τ)`,
real but not `≥ 0` ✔; and no step of Theorem 9.4 uses positivity — (a) uses
`g(0), g(1)`, (b) uses evenness and reality of `g(½+i·)`, (c) uses Fourier
inversion and evenness of `h`.  I re-ran the proof with `|\hat F|²` replaced by
`\hat h` throughout and nothing breaks.  So `𝓔 = C_c^∞(R)^{even,real}` is a
genuine **vector space** and (9.11) a genuine **linear** functional; continuity
is explicitly disclaimed and "distribution" is flagged informal.  `m1` and
`LF3` **closed** (the mode of convergence — eventual exactness, pointwise in
`h` — is now in the *statement*, with the comparison to the two topologies it
is stronger/weaker than).

**(h) (E3a)–(E3d).**  The split is honest: (E3b) is the local count, (E3c) the
strip estimate, (E3d) the global count used **only** at Thm 10.4(iii) and
Rem 9.8; sources named (Davenport ch. 15–17, Titchmarsh §§3.1, 9.6); Lemma 9.2
now cites (E3b) for the height and (E3c) for the bound, with the words "an
import, **not** a consequence of (E3d)"; §9.6 row 7 likewise; §11's table has
four rows and the note.  `grep -c "(E3)"` = 1, inside the note that says (E3)
*was* one row.  `M2`/`LF2` **closed in main.md** — but not in the README
(`r2`).  One remark: (E3c) is presented as *"Consequently … from (E3a)+(E3b)"*
**and** carries a `CLASSICAL` label with a source.  That is acceptable
(the deduction is standard and the input is also named), and I record it as
belt-and-braces rather than as a defect.

**(i) `m2`, `m3`, `m4`, `m5`, `m6`, `m7`, `n1`, `n2`, `n3`, `LF1`, `LF4` — all
carried out, each verified at the point of edit.**  In particular: `m7` is
right and the diagnosis is right — Paper 43's (8.5∞) writes `b(1)` while
declaring `b := F∘j_∞` *"in the logarithmic coordinate"*, where the identity
class is `t = 0`; Paper 45's `2b(0)e^{−t/2}` is the correct reading and the
bracket really is `O(t)` (`b(t)+b(−t)−2b(0) = O(t²)` and
`2b(0)(1−e^{−t/2}) = b(0)t + O(t²)`), against `K(t) = O(1/t)`.  `LF1`/`n2`: the
`106_11` variable is `z = (ρ−½)/i`, so `ρ = ½ − y_0 + ix_0`; `y_0 ≠ 0` is
off-line and `x_0 ≠ 0` is "no real nontrivial zero"; (20) gives
`Im s_0² = 2x_0y_0 ≠ 0` and (21) the isomorphism — (10.1) is faithful, (E2)'s
new clause is used **only** there, and R132.003's reading and this one coincide.
`n3`: Theorem 12.2's proof now rests on Thm 9.7(c) ("vanishes identically on
**no** component", discrete zero set, **for every `c`**) and quotes (14.2) only
as a witness; the `c`-independence of `𝓝_∩ = 0` is stated and is correct (and
is a nice contrast with Cor. 9.6a, which the paper draws).

**(j) Script.**  26/26, re-run.  Checks (3c′), (3e), (6a)–(6c) are new, are
non-circular (each side computed independently), and (6b)'s two routes to
`c‖F‖²` are exactly the two normalizations I cross-checked by hand.  The
`ILLUSTRATION` labelling and the reported truncation errors remain honest.
One defect: the script's **section (2) banner and check (2b) still print the
withdrawn name and the withdrawn theorem number** (`r4`).

---

## 2. `FATAL`

**None.**

---

## 3. `MAJOR`

### `R1` — Corollary 9.6a(iii)'s third "equivalently" is an unproved biconditional, and it is the label's headline sentence

**Location.** main.md line ~1162, Cor. 9.6a(iii): *"… equivalently for which
(9.9) and (9.10) hold, **equivalently for which `I_∂ ≤ 0` on the primitive
radial sector is Weil's criterion**"*; echoed at §14.4 item 1 (*"the
equivalence with Weil's criterion fails"* for any other `c`) and at README §5
(*"equivalently for which `I_∂ ≤ 0` … is Weil's criterion"*).

**Error.**  The corollary proves — correctly, and this is all D128 `C9` needs —
that `c = 0` is the unique constant for which the **identity**
`I_∞^{(c)}(Γ_F,Γ_F) = B_nuc(F,F)` holds.  The third clause asserts something
strictly stronger: that for every `c ≠ 0` the **sign condition**
"`I_∞^{(c)} ≤ 0` on primitive radial classes" ceases to be equivalent to RH.
That is not proved anywhere, and for `c < 0` it is very likely **false**: the
condition becomes `Σ_ρΦ_F(ρ)Φ_F(1−ρ) ≥ c‖F‖²`, which is *weaker* than Weil
positivity pointwise but is plausibly still equivalent to RH, because under
`¬RH` the constructions of `106_11` (Theorem 10.4) produce negative tests whose
negativity is not bounded below by any fixed multiple of `‖F‖²` (the ratio is
not scale-limited: `F ↦ λF` scales both sides by `λ²`, and the target quartet's
contribution can be made to dominate `‖F‖²` by concentration).  Either way the
paper offers no argument, and a `PROVED` corollary may not carry an unproved
biconditional — this is the failure mode clause C.8 and D128 `C3` both exist to
catch, and it is sitting on the sentence that the label will travel with.

**Repair (deletion; nothing is lost).**  Strike the third "equivalently" in
Cor. 9.6a(iii) and replace §14.4 item 1's clause by: *"and the identification
of row D's target with Weil's criterion made in item 4 above — which goes
through the **identity** (9.10) — is available only for `c = 0`."*  Same edit
in README §5.  With that, Cor. 9.6a says exactly what it proves, D128 `C9` is
still closed, and Paper 43 Def. 8A.7d's new reason (iv) (which is phrased at
the identity level: *"the unique real constant for which the declared trace
satisfies the Weil comparison `I_∞(Γ_F,Γ_F) = B_nuc(F,F)`"*) is already
correct and needs no change.

---

## 4. `MINOR`

* **`r1` (main.md §14.3, line ~2093).**  *"conventions **(C1)** and **(C2)**
  (§1.2, carried into Theorems 9.6, 9.6′, **9bis.2**, 9bis.4 and §14.4)"*.
  Two defects in one line, and both bite on the `M3` repair.  (a) `9bis.2` is
  the **withdrawn** theorem number (W45.15); R132.004's grep
  `"Theorem 9bis.2[^′]"` missed it because the word "Theorem" is not repeated.
  (b) It asserts that (C1) is carried into a §9bis statement about `A` —
  the exact opposite of Definition 9bis.1a's box, which says in terms that
  *"(C1) … does **not** govern `A`"*, and which is the answer to round 1's
  "(C1) quantifier — one exception".  *Repair:* `9bis.2 → 9bis.2′` deleted from
  that list, leaving "Theorems 9.6, 9.6′, 9bis.4(ii),(iv)"; and add to §1.2's
  sentence *"carried … into §9.5, §9bis, §10"* the clause *"— in §9bis, into
  the statements about `T_∞` (Thm 9bis.4(ii),(iv)) and **not** into
  Definition 9bis.1a or Theorem 9bis.2′, which are about `A` and are
  chart-independent by construction"*.  No theorem statement is wrong (every
  §9bis theorem carries its own quantifier at the point of use); it is the
  ledger that lags.
* **`r2` (README §1).**  *"the argument principle on rectangles whose
  horizontal sides avoid the zeros (**using `N(T) = O(T log T)`**)"* — this is
  verbatim the `M2` error, repaired in main.md and left standing in the
  README.  *Repair:* "(using the **local** Riemann–von Mangoldt count
  `N(T+1)−N(T) = O(\log T)`, (E3b), and the strip estimate (E3c))".
* **`r3` (README, "What this paper does not claim").**  Omits §10: *"outside
  the comparison theorem and the clauses labelled `CLASSICAL`"*.  The banner
  and §0.2 were aligned by `m3` to name *"the contrapositive sufficiency
  argument of section 10"*; the README was not.  *Repair:* one clause.
* **`r4` (script, lines 247–248, 264).**  Section (2)'s banner prints
  *"Theorem 9bis.2: the meromorphic symbol of the colimit trace /
  `T-hat_infinity^mer(s) := A(s)+A(1-s) == 0`"* and check (2b) cites
  *"[Thm 9bis.2(i)]"*.  The name and the theorem are **withdrawn** (W45.15);
  the apparatus of record still prints them.  (The docstring at lines 13–18 is
  already correct, which makes the banner a pure oversight.)  *Repair:* banner
  → "(2) Remark 9bis.2b and Theorem 9bis.2′(i): the continued Euler-product
  symbol"; (2b)'s tag → `[Thm 9bis.2′(i)]`.
* **`r5` (§11, quarantine paragraph).**  The (E8) table row now reads *"Thm
  9bis.4(ii),(iii) **only**"*, but the paragraph below still says *"Mertens is
  used **once**, in Theorem 9bis.4(ii)"*, and the deletion test covers only
  (ii).  Round 2 added a second use (the rate at `s = 1`) and did not update
  the quarantine.  *Repair:* "used **twice**, in Thm 9bis.4(ii) and (iii);
  deleting both deletes no other statement — (iii) is a rate remark on which
  Theorem 9bis.2′, Corollary 9bis.3 and clause C.4 do not rest."
* **`r6` (§0.1 item (3) and README §3).**  Both fold the Mertens **rate** into
  the sentence that discharges clause C.4 (*"… the pole is created in the limit
  …, at the Mertens rate …"*).  Clause C.4's discharge is Theorem 9bis.2′,
  which uses no Mertens; a quarantined `CLASSICAL` import should not appear
  inside the summary of a clause it does not serve.  *Repair:* one parenthesis
  — "(the *rate* of that creation is Mertens, Thm 9bis.4(iii); clause C.4's
  discharge does not use it)".
* **`r7` (Lemma 1.3 / (1.5): the (C1) quantifier is not carried).**  (1.5)
  writes `T(Γ_{F⋆F^†})` and the proof's display sums `Σ_n` over **all** prime
  powers.  §1.2's convention says: *"Where this paper writes `T` with the prime
  sum running over all primes, it means `T_∞`, **and it says so**."*  Lemma 1.3
  does not say so — and round 2 touched Lemma 1.3 (the `m6` note) without
  adding it.  No theorem is wrong (Theorem 9.6, which uses leg (S1), carries
  (C1) itself), but this is the one place in the paper where the
  hypothesis-carrying rule is violated.  *Repair:* `T → T_∞` in (1.5) and one
  clause "(colimit, convention (C1); at a chart, inside the window of
  Thm 8A.7c(e))".
* **`r8` (cross-paper, Paper 44: edit (a) is incomplete).**  Relabelling
  Thm 8bis.4(ii) `CLASSICAL → PROVED-IN-REPOSITORY` leaves **three** statements
  of Paper 44 saying the opposite about the same object: Remark 8bis.7a item 1
  (*"Only two [imports] survive: Weil's criterion/explicit formula
  (Theorem 8bis.4(ii)–(iii)) … Both survivors are `CLASSICAL`"*), the round-7
  banner at ~line 5124 (*"Imports now: TWO, both `CLASSICAL` … Weil's
  criterion/explicit formula (Thm 8bis.4(ii)-(iii))"*), and §10.4 item 2
  (*"two quarantined `CLASSICAL` imports (Weil's criterion/explicit formula;
  Chebyshev)"*).  After edit (a) those sentences are inaccurate as written.
  *Repair:* one `[phase 132]` clause in each: *"the explicit-formula half of
  this import is `PROVED-IN-REPOSITORY` since phase 132 (Paper 45 Thm 9.4);
  what remains `CLASSICAL` here is Weil's **criterion**."*  This changes no
  clause of B and no count that matters (the import remains one object with a
  `CLASSICAL` half), but Paper 44 must not carry two labels for one theorem.
* **`r9` (cross-paper, Paper 43 Def. 8A.7d: the preamble now contradicts its
  own reason (iv)).**  The block still opens *"Four reasons are recorded, and
  **none of them is a derivation**"* — one line above the new reason (iv),
  which begins *"**It is derived:**"*.  *Repair:* "Four reasons are recorded;
  reasons (i)–(iii) are normalization choices and are not derivations, and
  reason (iv), added in phase 132, **is** a derivation relative to the Weil
  comparison (Paper 45 Cor. 9.6a)."  Also: the word "derived" is slightly
  stronger than the fact — `c = 0` is *characterized* as the unique value
  compatible with the comparison, which is what Paper 45 Rem. 9.6b(3) says
  carefully; the immediate gloss in the edit is correct, so only the headline
  word wants softening.
* **`r10` (three-way disagreement on which reasons survive).**  Paper 45
  Rem. 9.6b(2) says *"Reasons (i)–(iii) of 8A.7d are independent and stand"*;
  Paper 45 §14.5 row (d) and Paper 43's own edit both say *"(i)–(ii)"*.
  Reason (iii) (the intrinsic Mittag–Leffler constants) **is** independent and
  does stand; Rem. 9.6b is right and the other two are wrong.  *Repair:*
  `(i)–(ii) → (i)–(iii)` in both places.

---

## 5. `NOTE`

* **`n2′` (the citation chain now passes through Paper 44, and it still
  terminates).**  Edit (a) makes Paper 44 Thm 8bis.4(ii) depend on Paper 45
  Thm 9.4, and Paper 44 (8bis.14e) depends on 8bis.4(ii) ("the sign convention
  fixed once in Theorem 8bis.4(ii)"), and Paper 45 Lemma 1.3(S3) depends on
  (8bis.14a),(8bis.14e).  So the chain is
  `P45 Lem 1.3(S3) → P44 (8bis.14e) → P44 Thm 8bis.4(ii) → P45 Thm 9.4 →
  (E1)–(E5)`.  It **terminates** — Theorem 9.4 uses nothing from Paper 44 and
  nothing from §1 — so there is no circularity; but Lemma 1.3's `m6` note names
  only the direct hop and should name the Paper 44 hop too, since that is the
  one a reader will worry about after edit (a).
* **`n3′` (§2 lags §14.2).**  §2's clause table is round-1 text: row C.3 still
  cites only Thm 5.1 and (8.5∞) (not Lemma 5.1a), and row C.4 still says
  "§9bis is new" without naming Thm 9bis.2′.  §14.2 is correct and complete;
  §2 is a summary and no statement in it is false, but the two tables should
  agree.
* **`n4′` (§13 ordering).**  W45.14, W45.15, W45.16 are inserted **before**
  W45.13, which is now last.  Sixteen items confirmed by grep; only the order
  is odd.
* **`n5′` (§14.3's `m5` fix).**  The count is now right ("the five items") but
  the parenthetical pointer lists four locations for five bullets, and two of
  the five bullets (8A.7b, 8.10/`c_cut`) are **declines** rather than items
  handed over.  Cosmetic.
* **`n6′` (Paper 43 §14.1a).**  The section still ends *"this paper does not
  use anything from them [rows B and C]"*, while the `[phase 132]` records
  above it, the obstacle rows and Def. 8A.7d reason (iv) all now cite Paper 45.
  No clause of A rests on any of them, so nothing is wrong; add
  "(the phase-132 records cite Paper 45, but no clause of A rests on them)".
* **`n7′` (§1.5's citation of (14.2)).**  The dictionary row gives
  `\hat W_∞(0,0) = \log π − ψ(¼)` citing *Paper 43 (14.2)*; (14.2) is a lower
  bound for `m := \sup T̂` **including** the finite places.  The exact
  archimedean value is Paper 43 (9.12b).  Harmless, and `n3`'s repair already
  makes the typing distinction inside Theorem 12.2; the dictionary row should
  cite (9.12b).
* **`n8′`.**  The script's section (1) also verifies Theorem 9.4 for an *odd*
  and an *asymmetric* real `F` — correct (`h = F⋆F^†` is even regardless), and
  a fair illustration of Corollary 9.4a's generality.

---

## 6. Disposition of every round-1 finding

| id | disposition | verdict |
|---|---|---|
| `M1` | Cor. 9.6a + Rem. 9.6b + §14.4 rewritten + W45.14 + Paper 43 Def. 8A.7d reason (iv) + obstacle row `c_{cut}` | **CLOSED**, and it is a strengthening — **except** the over-claim `R1`, which is new and must be deleted |
| `M2` | (E3) → (E3a)–(E3d), sources named, Lem 9.2 and §9.6 row 7 and §11 rewritten | **CLOSED** in main.md; README lags (`r2`) |
| `M3` | name withdrawn (W45.15), Def. 9bis.1a with the (C1) box, **Thm 9bis.2′ at both Tate points**, Rem. 9bis.2a, `Ξ ≡ 0` demoted to Rem. 9bis.2b, §0.1/§14.2/§15 rewritten | **CLOSED, and exceeded** — the `s = 1` mirror is R132.004's own and it is correct.  Residue: `r1`, `r4` |
| `M4` | **Lemma 5.1a**, proved from the two hypothesis-free citations; Lem 1.3(S1), Thm 9.6, Thm 9.6′, Thm 12.2 all routed through it; W45.16 | **CLOSED.**  Both citations verified in their sources; the lemma re-derived independently by a second route |
| `m1` | Cor. 9.4a; `𝓔` a vector space; continuity disclaimed | **CLOSED** |
| `m2` | `D ↦ D+2`, not "enlarge `N`" | **CLOSED**, matches `106_11` (27)–(30) |
| `m3` | banner names §10 | **CLOSED** in main.md; README lags (`r3`) |
| `m4` | "`O(\log\|s\|)`" | **CLOSED** |
| `m5` | "five items", pointer corrected | **CLOSED** (`n5′` cosmetic) |
| `m6` | dependency stated at Lemma 1.3 | **CLOSED** (`n2′`: name the Paper 44 hop) |
| `m7` | `2b(0)e^{−t/2}` with the identity-class gloss | **CLOSED**, and the diagnosis of Paper 43's `b(1)` is right |
| `n1` | Remark 9.8 (absolute convergence) | **CLOSED** |
| `n2` | folded into (10.1) with `LF1` | **CLOSED** |
| `n3` | Thm 12.2 rests on Thm 9.7(c); (14.2) a witness only | **CLOSED** |
| `n4` | Paper 43 §14.1a replaced by a `[phase 132]` block | **CLOSED** (`n6′` cosmetic) |
| `n5` | Def. 8A.7d reason (iv) struck and replaced | **CLOSED** (`r9`, `r10`) |
| `n6` | no change needed | **CLOSED** |
| `LF1` | (E2)'s no-real-zeros clause, used only at (10.1) | **CLOSED** |
| `LF2` | = `M2` | **CLOSED** |
| `LF3` | eventual constancy in the statement, mode named | **CLOSED** |
| `LF4` | "continued Euler-product symbol" throughout; `T̂_∞` never bare | **CLOSED** in main.md (`r4`: the script) |
| `LF5` | all five cross-paper edits made | **CLOSED** for (b),(c),(d),(d′),(e); **(a) incomplete** (`r8`) |

**The cross-paper edits, checked one by one against the brief's test — does any
of them change a theorem, a label of row A or B, or a proof?**
(b),(c),(d),(d′) touch Paper 43's obstacle table, §14.1a and Def. 8A.7d's
*reasons*: **records only**, no statement, no proof, no clause of A.
(e) adds Paper 44 §9.1a and §10.4 item 4a: **records only**.
(a) changes the **status label of Thm 8bis.4(ii)'s import** from `CLASSICAL` to
`PROVED-IN-REPOSITORY`.  That is a label change — authorized here
(`LF5`(a)), *removing* an import rather than adding one, leaving the statement
and the proof untouched, leaving Weil's **criterion** (iii) `CLASSICAL`
(verified), and leaving Paper 44's own grade untouched.  I accept it, with
`r8`: Paper 44 must not go on saying elsewhere that the same object is
`CLASSICAL`.  **No label of row A or row B is affected.**

---

## 7. Per-clause verdict (round 2)

| clause | verdict |
|---|---|
| **C.1** | `PROVED` by citation to row B theorems.  **Clean**, unchanged |
| **C.2** | `PROVED` at the chart, rulings in the completion, labels corrected with a counterexample.  **Clean** |
| **C.3** | `PROVED` as a theorem about row A's **declared** trace, place-additivity disclosed as definitional **in the table itself**; the identity case `0 ∈ supp h` now covered by **Lemma 5.1a** with no support hypothesis.  **Clean** (round 1's condition discharged).  `n3′` cosmetic |
| **C.4** | `PROVED`, all three parts.  The polar half now rests on **Theorem 9bis.2′(ii),(iv)** — a positive residue statement at **both** Tate points, chart-independent, with coefficient exactly `1` each — and **not** on `Ξ ≡ 0` nor on any definition.  Round 1's `fail as written` is **lifted**.  `r1`, `r5`, `r6` book-keeping |
| **C.5** | `PROVED`.  Row 7's certificate is the **named** import (E3c); Rem. 9.8 adds absolute convergence for this test class |
| **C.6** | first half `PROVED` **for the trace with `c := 0`**, and `c = 0` is the unique constant for which the **identity** holds (Cor. 9.6a(i)–(iii) first two clauses) — subject to `R1`'s deletion of the third clause; second half `PROVED` (Thm 10.4, `C10` fix complete, (E2)'s last clause named and used once) |
| **C.7** | `PROVED`.  No sign is proved anywhere; the banner now names §10.  **Clean** (README `r3`) |
| **C.8** | `PROVED` in the **strong** form: Theorem 9.4 is proved in the repository, and the import ledger now names what it actually uses.  Round 1's condition discharged.  **This remains the paper's real achievement** |
| **C.9** | `PROVED`; handoffs by theorem number in both directions, each used or declined with a reason; `n−1` deleted not discharged; §14.5 records the cross-paper edits.  `r8` is a defect **in Paper 44**, not in C.9's discharge |
| **A.6 (radial)** | `PROVED` at every finite chart, and now for **every** `c` (Thm 9.7(c)); not claimed in the colimit.  **Clean** |

**Renaming/definition test on round-2 material.**  Every round-2 object is a
theorem or a citation, not a renaming: Lemma 5.1a is proved from two named
theorems of Papers 43 and 44 (and I re-derived it a second way);
Corollary 9.6a is a two-line computation with a numerical witness;
Corollary 9.4a is a re-run of an existing proof with positivity removed;
Theorem 9bis.2′ is a residue computation with four independent checks.
**Definition 9bis.1a is a definition, and it is correctly typed as one** — it
defines `A`, and every *claim* about `A` is a theorem about that function.  The
one place where a definition was doing a theorem's work in round 1 (`T̂_∞^{mer}
:=` plus `≡ 0`) is gone.  Test **passed**.

**Independence.**  Zeros of `ζ` occur in (E2)/(E3a)–(E3d) as a set, a density
and a product; in Lemma 9.2, Thm 9.4, Cor 9.4a, Thm 9.6, Thm 9.6′ (the
comparison); and in Thm 10.4 (a hypothetical off-line zero, contrapositive).
Nowhere else.  No sign, no positivity, no `𝓝_∞ = 0`.  Grep for the withdrawn
carrier objects (`Fell`, `E_u`, `E_{a_S`, `Z_J`, `χ_A`, `G_rad`, `K_h`,
corner strata) and for `T̂_∞^{mer}`: **every hit in main.md is inside a
withdrawal, a historical clause text, or the banner's description of what was
withdrawn.**  The one live residual anywhere is in the **script** (`r4`) and
the one live stale theorem number is §14.3's `9bis.2` (`r1`).

**Banner / §0 / §2 / §13 / §14.2 / §14.4 / §14.5 / README consistency.**
Banner ↔ §0.2 ✔ (aligned, §10 named).  §13 = sixteen items ✔ (order `n4′`).
§14.2 names every round-2 object ✔.  §14.4 separates the two constants ✔
(subject to `R1`).  §14.5's table matches the five edits actually present in
Papers 43 and 44 ✔ (one row's "(i)–(ii)", `r10`).  §2 lags §14.2 (`n3′`).
README lags on `M2` (`r2`), on `m3` (`r3`), and repeats `R1` (`r1`'s echo).

---

## 8. The answer on `Ξ ≡ 0`, and the grade

### 8.1 `Ξ ≡ 0`: **keep it as Remark 9bis.2b.  Do not delete it.**

R132.004 asked for a ruling and offered to delete.  The ruling is **keep**,
for three reasons, and R132.004's stated reason is the right one.
(1) The statement is **true**, is proved in four lines, and is now correctly
typed: a remark, named after what it actually is (the functional equation), with
the explicit sentence *"no clause of this paper rests on `Ξ ≡ 0`"*.  What
`M3` objected to was the **name** and the **rank** — "the meromorphic symbol of
the colimit trace", headlined as §0.1 item (3) and cited by §14.2's C.4 row.
Both are gone; `Ξ` is a local abbreviation inside one remark and is cited by no
clause.  (2) It carries genuine reader-facing information that nothing else in
the paper carries: Paper 43 Theorem 9.7b presents every local symbol in the
manifestly reflected form `(\cdot)(s) + (\cdot)(1−s)`, and a reader arriving
from there will ask what that reflection is on the continued symbol.  The
answer — it is `ξ(s) = ξ(1−s)` and nothing more — is worth four lines, and
*declining* to say it invites someone downstream to rediscover it and think it
means something.  (3) The remark now contains the sharpest available warning
against the round-1 error: it shows explicitly that the `+1` at `s = 0` is
cancelled **inside `Ξ`** by the `−1` coming from `ζ`'s pole at `s = 1` — i.e.
it demonstrates *why* a vanishing statement cannot reconcile the residues,
which is exactly the lesson `M3` was teaching.  Deleting it would remove the
paper's own explanation of its own withdrawn claim.
One condition: the sentence *"no clause of this paper rests on `Ξ ≡ 0`"* and
the §14.2 C.4 row's *"Rem. 9bis.2b (`Ξ ≡ 0`) is used by **no** clause"* must
both stay, and `r4` must remove the withdrawn name from the script so that the
apparatus stops printing the thing the paper withdrew.

### 8.2 Grade

    WEIL-STRENGTH-COMPLETE:  GRANTED for row C, on Paper 43's declared carrier
    (a fixed finite chart S with the chart system and its colimit as
    additional structure), conditional on the single one-clause repair R1
    and the sweep r1-r10, none of which requires new mathematics and none of
    which touches a proof.

Round 2 did what round 1 could not: the central theorem's citation is now
inside its source's hypotheses (Lemma 5.1a), the import ledger names what it
uses ((E3a)–(E3d)), clause C.4's polar half is a residue computation
(Theorem 9bis.2′), and the normalization that the whole chain to RH rests on is
**derived rather than declared** (Corollary 9.6a).  Paper 45 is the only one of
the three row papers whose central analytic input is proved in the repository
rather than imported, and I record that again.

### 8.3 What must be recorded beside the label

1. **The normalization is load-bearing, and it is now pinned.**  Every theorem
   of §§9, 9bis, 10, 12 — and therefore §14.4 item 4's "row D's target implies
   RH" — is a statement about row A's declared trace with `c := 0`
   (Paper 43 Def. 8A.7d).  By **Corollary 9.6a** that constant is no longer a
   declaration: `c = 0` is the **unique** real constant for which
   `I_∞^{(c)}(Γ_F,Γ_F) = B_nuc(F,F)`, the difference for any other `c` being
   `c‖F‖²_{L²}`, which does **not** vanish on the primitive sector.  This is
   the closure of D128 `C9`, and it travels with the label.  *It is a
   uniqueness statement about the **identity**, not about the sign condition
   (`R1`).*
2. **Paper 43's `c_cut` is a different and still open quantity** (Thm 8.10,
   Rem. 8A.7e); it is not inherited by rows C or D and must never be conflated
   with item 1.
3. **What is declined, not proved.**  Row C does not prove that `Σ_vW_v` is the
   relative character of a localization (D128 `C2`,`C3`); place-additivity
   remains **definitional** and the paper says so in §5.1 and in §14.2's table.
   Row C also **declines** `𝓝_∞^W = 0` and Paper 43 Thm 8A.7b.
4. **Quantifiers.**  The comparison theorem is a **colimit** statement ((C1));
   at a finite chart it holds exactly inside the window
   `R(Γ_h) < \log ℓ_{next}(S)` and is **false** outside it.  `𝓝_∩ = 0`
   (Thm 12.2) is a **fixed-chart** statement, true for every `c`; no colimit
   radical statement is made anywhere.  Convention (C1) governs the statements
   about `T_∞`; it does **not** govern the continued Euler-product symbol `A`
   (Definition 9bis.1a's box) — see `r1`.
5. **The poles.**  Clause C.4's polar half is **Theorem 9bis.2′**:
   `Res_{s=0}A_S = |S_f|+1`, `Res_{s=1}A_S = 0` at every finite chart, against
   `Res_{s=0}A = Res_{s=1}A = 1` in the continuation, chart-independently; the
   two poles are the poles of `ξ`'s trivial factor `½s(s−1)`, their residues
   against `g` are `g(0)` and `g(1)`, and that pair **is** the polar packet
   `2Φ_F(0)Φ_F(1) = β_T(M,M)`, coefficient exactly `1` each.  At `s = 0` the
   chart overcounts and the excess evaporates (summation and continuation do
   not commute, Cor. 9bis.3); at `s = 1` the chart has no pole and the pole is
   created in the limit by `ζ`'s pole.  `Ξ ≡ 0` is the functional equation, is
   a remark, and no clause rests on it.
6. **Imports.**  (E1), (E2), (E3a)–(E3d), (E4)–(E8), (R1) of §11, each with the
   clause it serves.  No spectral realization, no Meyer, no cutoff theorem `C`.
   Mertens (E8) is used in Thm 9bis.4(ii),(iii) only, quarantined, with a
   deletion test, and it serves **no** part of clause C.4's discharge (`r5`,
   `r6`).
7. **No sign.**  Row C proves no sign, no positivity, no `𝓝_∞ = 0`, and nothing
   about the location of any zero outside the comparison theorem (§9.5) and the
   contrapositive sufficiency argument (§10).
8. **Row D inherits** `I_∂ ≤ 0` on primitive radial classes of `D_A^∞` in the
   colimit, on the trace with `c := 0` — the latter now as a **theorem of
   row C** — and nothing else; plus Paper 43 Thm 14.1 and Paper 44
   Thm 8bis.4a as the two standing negatives (Warning 8.5).
9. **Cross-paper.**  Five `[phase 132]` edits: four are records in Paper 43
   (no theorem, no proof, no clause of A); one changes the **status label** of
   Paper 44 Thm 8bis.4(ii)'s explicit-formula import from `CLASSICAL` to
   `PROVED-IN-REPOSITORY (Paper 45 Thm 9.4)` — authorized, statement and proof
   untouched, Weil's **criterion** (iii) still `CLASSICAL`, no label of row A or
   row B affected.  Paper 44's three remaining "both imports are `CLASSICAL`"
   sentences must be brought into line (`r8`).  The citation chain
   `P45 Lem 1.3(S3) → P44 (8bis.14e) → P44 Thm 8bis.4(ii) → P45 Thm 9.4 →
   (E1)–(E5)` **terminates**; there is no circularity (`n2′`).
10. **Numerics.**  `verify_132_explicit_formula.py`, 26/26, re-run by the
    auditor; the zero-sum checks are labelled illustration and report their
    truncation error; no check is circular.  The script's section-(2) banner
    still prints the withdrawn name (`r4`) and must be corrected before the
    label is recorded.
