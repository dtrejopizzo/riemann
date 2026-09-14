# R131.011 — Hostile audit of Paper 44, round 4

Auditor: Claude (Opus 5, 1M), adversarial auditor of record for phase 131.
Date: 2026-09-12.
Scope: every `[REBUILT, phase 131, round 4]` passage of
`04-papers/44-row-b-arithmetic-family/main.md` (18 marks), `README.md`, and
`03-research/phase-131-row-b-closure/scripts/verify_131_contacts.py`.
Method: re-derivation from the declared formulas of Paper 43 ((8.5), (8.5∞),
Rem. 8.6a, (8.5a)/(8.5b), Lemma 8.2, Thm. 8.8, (9.5b), (9.11), Thm. 9.7(b),
Thm. 9.7b(a)–(c), Thm. 8A.7c, Thm. 14.1, (14.2)) and of Paper 44 §3bis/§3ter,
not re-reading of the round-4 proofs.  Inputs: `R131_008`, `R131_009`,
`R131_010`.

**Headline.**  `F1` is **fully repaired**, and repaired in the right
direction: there is no residual claim anywhere in §0, the banner, §8bis, §9,
§10 or `README.md` that the Frobenius Gram form is the Weil kernel, and the
replacement — **Thm 8bis.1e**, the Weil kernel is the Gram form of
`Frob ⋆ Δ^{rad}` — is **correct**, as is the diagonal computation
**Thm 8bis.1b** (I re-derived the unit-packet value, the `p | n` vanishing and
the archimedean `−log(1/ε)` independently; all three check out to the letter,
and the numerics reproduce them).  **Thm 8bis.8** (the shell normalization) is
correct and its scope is stated honestly; the builder's refutation of the
chart-invariance route is **right**.  What does **not** survive the round is
smaller but real: **six `MAJOR` findings**, of which the two that matter
mathematically are that **Thm 8bis.4(iv)'s proof is a non-sequitur** (the
conclusion is true and provable in a *stronger* form, one line from a display
already in the paper), and that **Thm 8bis.7 does not close as proved** — its
primitivization step is wrong by a factor `≍ e^{5L/4}`, and the import `(W)`
as stated is false for `h_L = g_L ⋆ g_L^†`.  Neither touches B.1–B.9.
**The label is EARNED**, conditional on `M1`–`M6`.

---

## 1. Findings

### M1 `MAJOR` — Theorem 8bis.4(iv): the proof is a non-sequitur, and the true statement is stronger

*Location.* `main.md` Thm 8bis.4(iv) and its proof ("two quadratic forms whose
symbols differ by an indefinite function are not equivalent for definiteness
on an infinite-dimensional space"); repeated as a headline in §0, the banner,
§10's round-4 block, `README.md` and `R131.010` §2 (R3).

*Error.*  "`I_∂^{Frob} ≤ 0` ⟺ RH" is a biconditional between two propositions
each of which has a **fixed truth value**.  No argument about how two fixed
quadratic forms differ can refute such a biconditional: a difference of forms
is not a difference of truth values.  The displayed argument ("choose `ĥ`
where the difference is positive, resp. negative") shows only that the two
*forms* are distinct, which nobody disputed.  As written, the `PROVED` label
on (iv) is not earned.

*Repair (available, one line, and it gives more).*  Decide the sign of the
Frobenius form **unconditionally**.  By the paper's own (8bis.7),
`ω̂_{fin}(τ) = Σ_{p∈S_f}(\log p)\,2\,\mathrm{Re}(ζ_p/(1−ζ_p))` with
`ζ_p = p^{−1/2−iτ}`; at `τ = 0` every term is
`(\log p)\,2p^{−1/2}/(1−p^{−1/2}) > 0`, so `ω̂_{fin}(0) > 0` strictly, and
`ω̂_{fin}` is continuous and bounded (`|ω̂_{fin}| ≤ A_S`).  Take `ĝ`
concentrated in a window around `τ = 0` where `ω̂_{fin} ≥ c > 0`; the tail
contributes `O(A_S·δ)`.  Hence `I_A(Γ_g,Γ_g) > 0` for such `g`, and the two
primitivity conditions (codimension 2) do not obstruct.  **Conclusion:
positivity fails on the pure Frobenius family, unconditionally** — so the
equivalence with RH is refuted outright unless RH is false.  That is a genuine
`PROVED` negative theorem; the present one is not.

### M2 `MAJOR` — Theorem 8bis.7 does not close: the primitivization estimate is wrong, and `(W)` as stated is false

*Location.* Thm 8bis.7, proof, first paragraph; and the statement of the
import `(W)`.

*Error 1 (the estimate).*  The proof says primitivity "can be enforced by
altering two coefficients `c_n` with `\log n` near `L/2` by `O(e^{−L})`".
Re-derive: by the paper's own bound in the same sentence,
`|λ_∓(Γ_{g_L})| ≤ ‖g_L‖_1 e^{L/2} ≍ L e^{L/2}`.  Altering one coefficient
`c_n` by `δ` at `\log n ≈ L/2` changes `λ_−` by `δ·n^{1/2} ≍ δ e^{L/4}`.  So
the required `δ` is `≍ L e^{L/4}`, **not** `O(e^{−L})` — the claim is off by a
factor `≍ e^{5L/4}`.  A perturbation of that size is not controlled by
Lemma 8bis.5 against a main term `≍ L^2e^{2|β−1/2|L}` with `2|β−1/2| < 1`.

*Error 2 (the import).*  `(W)` asserts that "the contribution of ... the Tate
terms is `O(L^2e^{|β−1/2|L})`".  For `h_L = g_L⋆g_L^†` the Tate/polar
contribution is `ĥ_L(±i/2) = |ĝ_L(±i/2)|^2 ≍ e^{L}/(1+|γ_0|)^2`, while the
main term is `L^2e^{2|β−1/2|L}` with `2|β−1/2|L < L`.  The polar packet
therefore **dominates** the term it is supposed to be negligible against.
`(W)` as displayed is not a true classical statement.

*Repair.*  Impose the two Tate conditions **on the profile directly**:
`∫ψ(t/L)e^{iγ_0t}e^{±t/2}dt = 0` is a codimension-2 linear condition on
`ψ ∈ C_c^∞([1/2,1])`, costing nothing, and it makes the primitivization step
vacuous.  Then verify that the main term `ĝ_L(ρ_0) ≍ Le^{(β−1/2)L}` survives
the two conditions (it does, generically; say so), and restate `(W)` without
the false Tate clause.  Everything else in the proof is **correct**: I checked
Young (`‖e⋆g_L^†‖_∞ ≤ ‖e‖_∞‖g_L‖_1 ≍ Le^{−L/2}`), the support
`[−L/2−2,L/2+2]`, Lemma 8bis.5 at `R = L/2+1` giving `e^{L/4}`, and the
resulting cross terms `O(Le^{−L/4})` against `L^2e^{2|β−1/2|L}`.

### M3 `MAJOR` — Lemma 8bis.6: the proof proves a weak estimate (off by `L`) and asserts a pointwise one

*Location.* Lemma 8bis.6, proof: "that measure differs from Lebesgue measure
on `[L/2,L]` by `O(e^{−L/2})` when tested against `C^1` functions."

*Error.*  (a) The **tested** error is `Σ_n gap_n^2 ≤ (\max gap)(Σ gap_n)
≍ e^{−L/2}·(L/2)`, i.e. `O(Le^{−L/2})`, not `O(e^{−L/2})`.  (b) What the
lemma actually needs is the **pointwise** statement
`Σ_n gap_n ρ_{ε_n}(t−\log n) = 1 + O(e^{−L/2})`, which does **not** follow
from a tested estimate.  The pointwise statement is true (the mesh function
`gap(t) ≍ e^{−t}` has derivative `O(gap)`, so the mollified mesh density is
`1 + O(gap)`), but it is not proved here; the two estimates are conflated.
This is the builder's own press point (1) of `R131.010` §5, and it is
warranted.

*Consequence.* None fatal: even `‖g−g_D‖_∞ = O(Le^{−L/2})` leaves the cross
terms at `O(L^2e^{−L/4})`, negligible.  *Repair:* prove the pointwise version
(three lines: local Taylor expansion of `t ↦ gap(t)`), or weaken (8bis.13) to
`O(Le^{−L/2})` and propagate.

### M4 `MAJOR` — the chart quantifier: §8bis uses `T` where only `T_∞` will do; (8bis.10) is false at a finite chart

*Location.* Cor 8bis.1d's definition of `W_{fin}` ("`Σ_{q\ \text{prime}}`",
**all** primes); (8bis.6) in Thm 8bis.1e; Thm 8bis.4(i)–(iii) and (8bis.10);
Lemma 8bis.5's finite part ("a sum over `k ≤ e^{R}`"); Thm 8bis.7.

*Error.*  Paper 44's trace is Paper 43's `T` at a **fixed finite chart** `S`,
whose finite part runs over `p ∈ S_f` only (Thm 3bis.7, and §9.1 says so
explicitly: "on the colimit `D_A^∞` with `T_∞` the restriction `p ∈ S_f`
disappears").  §8bis never passes to the colimit — the words `T_∞`, `D_A^∞`
occur **nowhere** in §8bis.  Consequences: (a) (8bis.6) as displayed is
**false** for profiles wide enough to see a prime `ℓ ∉ S_f` (its left side
omits `(\log ℓ)ℓ^{−1/2}(h⋆g^†)(\log ℓ)`); (b) worse, (8bis.10) —
"`I_∂ ≤ 0` on primitive radial classes ⟺ RH" — is **false as stated** for a
finite chart: positivity of a kernel carrying only finitely many primes is not
Weil's criterion; (c) Lemma 8bis.5 and Thm 8bis.7 use windows `[L/2,L]` with
`L → ∞` and therefore *require* all primes up to `e^L`, i.e. `T_∞`.

*Repair.*  One sentence at the head of §8bis: work on `D_A^∞` with `T_∞`
(Paper 43 Thm 8A.7c), where for each fixed support radius the prime sum is
complete.  Every value computed in §8bis is unchanged (for the entries, `m/n =
q^{±k}` forces `q | mn`, hence `q ∈ S_f`); only the quantifier moves.  This is
the one place where a round-4 `PROVED`/`CLASSICAL` display is literally wrong
as written, and it must be fixed.

### M5 `MAJOR` — the `N`-linear divergence of the diagonal is normalization-dependent, and in the paper's own declared convention it is false

*Location.* Thm 8bis.1b, last sentence ("Consequently the diagonal entries of
the **Frobenius Gram matrix** … have no limit as `ε → 0` or `N → ∞`");
Thm 8bis.1′(i); Rem 8bis.1c; §0; the banner; §10 round-4 block; `README`.

*Error.*  Thm 8bis.1b computes `T` of the object `Δ^{(n),[φ_ε,N]}` with a
**unit-height** archimedean bump and **bare** coset indicators.  The actual
Gram diagonal is `T(Frob_n^{sm}⋆(Frob_n^{sm})^†)`, whose finite factors carry
exactly the convolution constants that Thm 8bis.1 declares it is now carrying
(`F3`): `∏_{s∈S_f∖P}vol(1+s^NZ_s) = ∏_s ((s−1)s^{N−1})^{−1}`.  Multiplying
(8bis.3′) — which grows **linearly** in `N` — by that constant, which decays
**geometrically** in `N`, gives a diagonal that tends to **`0`**, not to
`−∞`.  So "no limit as `N → ∞`" holds in the `♭` (normalized) convention and
**fails** in the convention Thm 8bis.1 explicitly adopts.  The two theorems
sit three paragraphs apart and use opposite conventions without saying so.

*Repair.*  State the convention in Thm 8bis.1b ("in the `♭` normalization of
Def 3ter.8, in which the convolution constants of Thm 8bis.1 are divided
out"), and add one clause to Thm 8bis.1′(i) and to the banner/§0/§10/README
headlines.  The archimedean `−\log(1/ε)` divergence is convention-robust; the
`N`-linear one is not.

### M6 `MAJOR` — ledger and dependency regressions

(a) *The P123.038 §5 row was not re-graded.*  `R131.010` §3 states "The ledger
row for that item is re-graded accordingly", and §6bis.1's Rem 6bis.3d ends
"§10's ledger row is graded accordingly".  It is **not**: the row in §10 still
reads `PARTIAL` with "*Open:* **the cyclic extension to mixed
correspondences**; …", which Thm 6bis.3c(ii) now supplies (trivially, and the
paper says so), and it cites neither Thm 6bis.3c nor L2 nor `R131.005` §2.
Two documents and two sections of one paper disagree.  *Repair:* re-grade the
row, or delete the two sentences claiming it was re-graded.

(b) *"External inputs: **none**" is now false, and the import symbol
collides.*  §11 reads: "External inputs: **none**.  Row B adds no citation to
the one import (`W`, Wodzicki excision) recorded in Paper 43 §12."  Round 4
adds **two** external inputs: the named import **`(W)`** of Thm 8bis.7
(Weil's growth estimate) and **Chebyshev's bound** inside Lemma 8bis.5 — and
the new import is given the **same symbol `W`** as Paper 43's Wodzicki
excision, in a paper that names its kernel `W_{fin}` and its local terms
`W_p`, `W_∞`.  *Repair:* rename the import (e.g. `(Wgr)`), and amend §11 to:
"External inputs: none in B.1–B.9; two in the quarantined §8bis.4 — `(Wgr)`
and Chebyshev — used by no clause."

(c) *Theorem 8.2 (clause B.9) is now literally contradicted by §8bis.*
Thm 8.2 asserts "**No** construction, statement or proof in this paper uses a
zero of `ζ`, the Riemann Hypothesis …" and "**two things are not claimed
anywhere in this paper**: any statement about zeros …".  Thm 8bis.4(ii)–(iii)
and Thm 8bis.7 are statements about zeros and about RH.  The **substance** of
B.9 is intact (no clause depends on them), but the sentence must carry the
carve-out that §10's round-4 block already carries.

### m1 `MINOR` — Theorem 8bis.1e inherits the very hypothesis `F3` forced on Theorem 8bis.1

(8bis.6) is stated for "`h_m,h_n` supported near `\log m, \log n`" with no
`ε_0(A,S)`, and — see `M4` — with `W_{fin}` over all primes.  Both are
repaired by "for profiles of width `< ε_0(A,S)`" plus the colimit sentence.

### m2 `MINOR` — (8bis.5) drops the profile value and the convolution constants

Cor 8bis.1d writes `I_A(G,G) = Σ_{m≠n}c_mc_n W_{fin}(\{\log m − \log n\}) + …`
as an **equality**.  By Thm 3ter.10/Cor 3ter.11 the entry is the atom mass
times `(h_m⋆h_n^†)(n/m)` times `∏_s vol(1+s^NZ_s)`; (8bis.2) is a statement
about `contact_{fin}` (the atom), not about the entry.  Say "with unit-height
profiles in the `♭` normalization", or carry the two factors.

### m3 `MINOR` — equation-number collisions and one stale cross-reference

`(8bis.5)` is assigned twice (Cor 8bis.1d's Gram decomposition; Thm 8bis.2's
`L^2`-normalized form), `(8bis.6)` twice (Thm 8bis.1e's radial Gram identity;
and referred to in Cor 8bis.2a as "the archimedean symbol", which is now
`(8bis.8)`), `(8bis.7)` twice (Thm 8bis.1e's kernel value; Thm 8bis.2's `A_S`
bound — and Cor 8bis.2a's "the finite-place symbol being bounded by (8bis.7)"
now points at the wrong display).  Renumber.

### m4 `MINOR` — Lemma 8bis.5: an unlabelled import and an unjustified constant

The proof uses "Chebyshev's bound `Σ_{k≤X}Λ(k) ≤ cX`" — an external
arithmetic input — inside a lemma labelled `PROVED`; and the displayed
constant `4` requires `c ≤ 1`, i.e. `ψ(X) ≤ X`, which is **false** for
infinitely many `X` (Littlewood).  Write `C‖h‖_∞e^{R/2}` with `C` absolute,
and label the lemma `CLASSICAL` or flag the import.

### m5 `MINOR` — real versus complex profiles

Def 8bis.3 and Thm 8bis.4 quantify over **real** `g` and **integer/real**
`c_n`; Thm 8bis.7 applies the hypothesis to `g_L = ψ(t/L)e^{iγ_0t}` and to
`g_D` with complex coefficients.  The passage is legitimate (the kernel is
real and even, so `I(g,g) = I(\mathrm{Re}\,g,\mathrm{Re}\,g) +
I(\mathrm{Im}\,g,\mathrm{Im}\,g)`) but is nowhere stated.  One sentence.

### m6 `MINOR` — `README.md`'s round-3 block carries the retracted sentence unmarked

`README.md` line 43 still reads "The Gram matrix of the smeared Frobenii
**is** the Weil kernel `W(\log m − \log n)`" and line 47 "Weil positivity
**implies** the Hodge index on this class (proved, one direction)".  The
round-4 block below retracts both, but the round-3 block carries **no**
inline superseded marker, unlike every superseded block in `main.md` (§10,
§8bis, the banner).  A reader who stops at line 43 reads the refuted claim.
Add `[SUPERSEDED IN ROUND 4 — see below]`.

### m7 `MINOR` — §11's phase-131 record is stale

"Phase 131 record: … (lead blueprint `R131_000`, builder report `R131_001`,
numerical checks in `scripts/`)" — rounds 2–4 (`R131_002`–`R131_011`) are not
listed, though §9bis and §10 cite them throughout.

### n1 `NOTE` — Theorem 8bis.8 fixes `c_p` only relative to the declared archimedean measure

The theorem holds `d^*x_∞ = dx/(2|x|)` fixed while letting `c_p` vary, so what
is proved is "`c_p = \log p` **given** (8.5b)".  Cor 8bis.8a's last sentence
("the only remaining freedom is an overall positive scale") covers this
correctly — rescaling all places by `λ` gives `c_p = λ\log p` and `λ` at `∞` —
but the theorem's statement would read better with the scale quotient in it.

### n2 `NOTE` — Theorem 8bis.1's proof phrases the shell criterion imprecisely

"a shell `q^{m'}Z_q^×` meets [the support] in a set of positive Haar measure
**iff** … and `q ∈ F`".  For the **smeared** class the level-`N` coset at
`s ∉ F` is open, so a shell at `s ∉ F` *can* meet it in positive measure; what
actually kills it is the archimedean coordinate together with the `ε < ε_0`
hypothesis (`s^{−m'}` must lie within `2ε` of `n/m`, forcing `s^{−m'} = n/m`
and hence `s ∈ P(r) ⊆ F`).  The conclusion is right; the stated reason is not
the operative one.

### n3 `NOTE` — numerics block (D) is a tautology

`assert abs(c_p/log p − 1) < TOL` for `c_p := log p` verifies nothing about
Thm 8bis.8; it restates the definition.  Blocks (A), (B), (C) are real checks
and I reproduced (C) by hand (slope `−Σ_{r∤n}\log r = −4.653960` for
`n = 2,4` and `−4.248495` for `n = 3`; `N = 1` value `−3.377976 =
−[\tfrac12\log3+\tfrac34\log5+\tfrac56\log7]`).  Script runs: **ALL CHECKS
PASS**, **ROUND-4 CHECKS PASS**.

---

## 2. What survives — re-derived independently

* **`F1` is fully repaired.**  I grepped and read every occurrence of "Weil
  kernel" in `main.md` and `README.md`.  There is **no** residual assertion
  that the Frobenius Gram form is the Weil kernel in §0, the banner, §2, §8bis,
  §9, §9bis, §10 or `README`'s round-4 block; the only survivals are inside
  explicitly-marked withdrawn/superseded text (W16, the round-3 §10 block) and
  the unmarked `README` round-3 block (`m6`).  The withdrawal is recorded
  where a withdrawal belongs (§9bis W16–W18) and is not softened.

* **Theorem 8bis.1b is correct, in full.**  With `du` the probability Haar
  measure of `Z_r^×` (which is the normalization of Paper 43 (8.5), whose unit
  packet already carries `\log p` out front): `vol(1+r^jZ_r) =
  ((r−1)r^{j−1})^{−1}` for `j ≥ 1`, so `vol\{v_r(1−u)=j\} = r^{−j}` (`j ≥ 1`)
  and `(r−2)/(r−1)` (`j = 0`), summing to `1`; the integrand `|1−u|_r^{−1}`
  is `r^{j}` on the `j`-stratum; hence
  `∫_{Z_r^×∖(1+r^NZ_r)}|1−u|_r^{−1}du = (r−2)/(r−1) + (N−1)` **exactly**, and
  the packet is `−(\log r)[(r−2)/(r−1)+(N−1)]`.  The `r = 2` degeneration
  (`Z_2^× = 1+2Z_2`, first term `0`) is right.  The vanishing at `p | n` is
  right and for the right reason (no condition at `p` ⇒ `a_p` constant ⇒ the
  packet's integrand is identically zero).  The shell vanishing is right
  (`|\log q^{−k}| ≥ \log 2 > 2ε`).  The archimedean term is right: with
  `K(t) = e^{−t/2}/(1−e^{−2t})` (Paper 43 (8.5∞)), `K(t)e^{−t/2} = 1/(2t)+O(1)`
  near `0` and `= O(e^{−t})` at `∞`, so `−2∫_ε^∞K(t)e^{−t/2}dt =
  −\log(1/ε)+O(1)`, and the `(0,ε)` piece is `O(1)` by the stated splitting —
  I checked both halves of that splitting (`∫_0^ε t^{−1}O(t^2/ε^2)dt = O(1)`,
  `∫_0^ε t^{−1}O(t)dt = O(ε)`), which is the builder's press point (2), and it
  is **sound**.  Subject to `M5` (which convention the statement is in), this
  is the strongest new computation of round 4.

* **Theorem 8bis.1e is correct.**  `Γ_m^{rad}⋆(Γ_n^{rad})^† =
  Γ^{rad}_{(\log m)}⋆Γ^{rad}_{(−\log n)} = Γ^{rad}_{(\log m − \log n)} =
  Γ^{rad}_{m/n}` by Thm 3bis.5(i)–(ii), and on profiles `Γ_h⋆Γ_g^† =
  Γ_{h∗g^∨}` by Lemma 3bis.6a (I re-checked the convolution computation in
  Lemma 3bis.6a: it is the disintegration `d^*w = dt⊗du`, correct).  Then
  Thm 3bis.7 gives `∫(h⋆g^†)d(ω_{fin}+ω_∞)` with `ω_{fin}` atomic on
  `±\log p^k` and `ω_∞ = K(|t|)dt` — the **full** kernel, with no indicator,
  for the stated reason: a radial section is `K^♮`-invariant, so the
  level-`N` conditions of (3ter.7) are absent and (3ter.9)'s arithmetic
  indicator is identically `1`.  The diagonal `m = n` is indeed Thm 8bis.2
  (`Γ_{h⋆h^†}` is centred at `0`), and that pairing **also** diverges
  (`−\log(1/ε)`), a fact 8bis.1e states but Thm 8bis.1′(ii) omits — see `M5`
  for the parallel omission on the other side.  Subject to `M4` and `m1`.

* **The two-Gram-form dichotomy (Thm 8bis.1′) is the right statement and it is
  proved.**  (i) = Cor 8bis.1d + Thm 8bis.1b; (ii) = Thm 8bis.1e; (iii) =
  Cor 3ter.10b + Prop 3ter.5.  The mechanism sentence — `Δ^{rad}` converts the
  finite half into the whole, at the cost of forgetting the factorization
  (Lemma 3bis.3b) — is exactly the repair `R131.008` §1 `F1` prescribed, and
  it is a better theorem than the false one it replaces.  The indicator
  `∏_{s∉F}\mathbf 1[s^N|(n−m)]` is re-derived correctly from (3ter.9) with
  `r = m/n`, `r−1 = (m−n)/n`, `v_s(r−1) = v_s(m−n)` for `s ∤ n`.

* **Theorem 8bis.8 is correct.**  `ζ_p(s) = c_pΣ_{k≥0}p^{−ks} =
  c_p/(1−p^{−s})`, residue `c_p/\log p` at `s = 0`; `ζ_∞(s) =
  ∫_{|x|≤1}|x|^s dx/(2|x|) = 1/s`, residue `1`; equality iff `c_p = \log p`.
  Part (iv) checks against Paper 43 Thm 9.7b(a): there the residue at
  `τ_k^+` is `−i` for **every** `p` precisely because the factor `L = \log p`
  in (9.11) cancels the `1/(iL)` of the partial-fraction expansion — replacing
  `\log p` by `c_p` multiplies the whole symbol by `c_p/\log p`, hence every
  residue, giving `−i(c_p/\log p)` against the archimedean `−i`.  Correct.

* **The builder's refutation of the chart-invariance route is correct.**
  Paper 43 Thm 9.7b(c) reads the total residue as `∓i(|S_f|+1)`, manifestly
  chart-dependent; Thm 8A.7c(e)'s chart-invariance is about values on windows
  of bounded radius, not about a symbol's residues.  I add an independent
  reason: inflation along `S ⊆ T` makes the new coordinate constant, so the
  new place's **unit packet vanishes** and its shell terms vanish below the
  radius `\log ℓ` — chart-invariance imposes **no** condition on `c_ℓ` at all.
  Rem 8bis.8b's "uniqueness theorem given a named requirement, **not** a
  derivation from chart-invariance" is exactly the honest statement, and
  Rem 8bis.8c removes the probability-vs-`d^*x` equivocation of `F7` cleanly.

* **`F4`, `F5`, `F6`, `F8` are repaired correctly.**  `F4`: the bracket is now
  `b(t)+b(−t)` in the logarithmic variable, matching Paper 43 (8.5∞)/Rem 8.6a,
  and the reason the reflected term drops (`e^{t} > 1 > n^{−1}e^{ε}`) is
  stated.  `F5`: (8bis.8a) handles `|τ| ≤ R_0` by continuity and the value
  `\logπ − ψ(1/4)` of Paper 43 (14.2), contributing `ε^{−1}O(ε) = O(1)`; the
  citation is corrected to Thm 9.7(b).  `F6`: `C_Bε R^2\log R + η(R)` with the
  derivation shown; the `R`-then-`ε` order is unaffected.  `F8`: Lemma 6bis.3a
  proves `i_{e,f}∘i_{d,e} = i_{d,f}` degreewise (`id∘id`, `(f/e)(e/d)=f/d`)
  and `i_{d,d} = id`, with the correct wording "functor on the divisor poset,
  function on the monoid".  All four verified.

* **§6bis.1 (L2) is honest and correct** as far as it goes: `Z[𝔉^+]` is the
  monoid ring of a commutative monoid, `deg_det` is additive by the cone law,
  cyclicity is trivial **and is said to be trivial**, (6bis.5) is the linear
  extension of Thm 6bis.4, and part (a) is `REFUTED` (P123.022), not open.
  Rem 6bis.3d measures it clause by clause against the quoted note.  The only
  defect is `M6`(a), a ledger regression, not a mathematical one.

* **Independence (attack 8/9).**  Zeros and RH occur **only** in
  Thm 8bis.4(ii),(iii) (`CLASSICAL`), Thm 8bis.4(iv)/(vi) (as the *name* of a
  statement not asserted), and §8bis.4 (`CLASSICAL`, import `(Wgr)` named).
  None is used by B.1–B.9; deleting §8bis.3–§8bis.4 changes no clause verdict.
  No sign, no positivity, no `𝓝_∞ = 0`, no von Mangoldt input (`Λ` is still
  derived as a shell volume, and now with a uniqueness theorem behind the
  normalization).  Independence **holds in substance**; `M6`(b),(c) are the
  bookkeeping that must catch up with it.

* **Consistency of the apparatus.**  §0 (lines 255–300), the banner (25–48),
  §9bis W16–W18, §10's round-4 block and `README`'s round-4 block say the same
  thing in the same words, and that thing is the corrected one.  §2's contract
  table is unchanged and remains accurate.  The single inconsistency is
  `m6` (`README`'s unmarked round-3 block) plus `M6`.

---

## 3. Renaming test on the round-4 material

* **Thm 8bis.1b, Cor 8bis.1d, Thm 8bis.1′(i),(iii)**: `PASS`, decisively.  The
  `p`-adic unit-packet value `−(\log r)[(r−2)/(r−1)+(N−1)]`, the vanishing at
  `p|n`, and the disjointness of `supp\,Frob_n` from `Im\,j_∞` are **invisible**
  to the scalar explicit formula: they are statements about supports and about
  local integrals over `Z_r^×`, at a level of resolution the explicit formula
  does not have.
* **Thm 8bis.1e**: `PASS, WEAKLY`.  Stripped of prose it says: the radial
  family is the translation group `(R,+)`, and row A's trace on it is the
  geometric side of the explicit formula (Thm 3bis.7, round 2).  "Gram form"
  is then the group law.  Its honest weight is carried entirely by the
  **contrast** with (i) — which is new — and the paper should keep saying so
  as plainly as Thm 8bis.4(iii) does.
* **Thm 8bis.4(iii)**: the paper **itself** says, in bold, "this is Weil's
  criterion carried by row A's declared trace, and it is **NOT** new".  That is
  precisely the honesty the lead asked for and it is granted in full.
* **Thm 8bis.8, Lemma 6bis.3a, Thm 6bis.3c**: `PASS`.  A local-zeta residue
  computation, a composition check in a divisor poset, and an additive
  extension — none is a statement of the explicit formula.
* **Thm 8bis.7**: not a renaming, but not a theorem either as proved (`M2`);
  and correctly quarantined.

---

## 4. Verdict per clause

| clause | round-4 verdict |
|---|---|
| **B.1** | `PROVED` (unchanged; `𝔉_S` and its grading re-verified in round 3). |
| **B.2** | `PROVED`, non-vacuous (Thm 3ter.4(iv), Rem 3ter.4a). |
| **B.3** | `PROVED`, with a true unit. |
| **B.4** | `REFUTED AS STATED`; `PROVED AS AMENDED` (owner-accepted), proved on objects in degree (Thm 6bis.4), now with the composition law of `Sh_Z` actually proved (Lemma 6bis.3a, `F8` closed) and extended additively (Thm 6bis.3c). |
| **B.5** | `PROVED` (unchanged), and `Λ(p^k) = \log p` is no longer merely declared (Thm 8bis.8). |
| **B.6** | `PROVED`, both halves non-vacuous (Thm 3ter.12; Thm 3ter.14 with `F6` repaired). |
| **B.7** | `PROVED` as a test; I **maintain** my dissent on the mechanism (`PARTIAL`, Rem 6.5a′).  The round-4 procedure — adopt the lead's ruling, record the dissent **verbatim** beside it, leave Rem 6.5a′ unchanged — is the correct resolution of `F10` and I accept it as such: the disagreement is now visible to the reader, which is all an auditor can ask. |
| **B.8** | `PROVED`; script re-run by me, all blocks pass, block (C) re-derived by hand; block (D) is vacuous (`n3`). |
| **B.9** | `PROVED` **in substance**, but the *text* of Thm 8.2 and of §11 must be amended (`M6`(b),(c)): they assert blanket independence and "external inputs: none" while §8bis.4 names an import and Lemma 8bis.5 uses Chebyshev. |

§8bis remains outside the contract; `M1`–`M5` therefore flip no clause.

---

## 5. Reservations R1–R6

* **R1 `DISSOLVED`** (Thm 3ter.4(iv), Rem 3ter.4a).  Unchanged.
* **R2 `DISSOLVED IN DEGREE, ON THE MONOID`** — the most P123.022 permits;
  round 4 adds the poset functoriality and the additive extension.  An
  object-level identification in `G` is **refuted**, not open.
* **R3 `DISSOLVED`** (true unit, dagger, inverse semigroup).
* **R4 `DISSOLVED`, in the only form available.**  Upgraded from round 3's
  `PARTLY`.  Thm 8bis.8 is correct and Rem 8bis.8b states exactly what cannot
  do the job.  Residual: the requirement (universal per-place Tate residue) is
  **named, not derived** — the paper says this in bold — and the normalization
  is fixed only up to a global scale (`n1`).
* **R5 `ANSWERED IN THE FORM THAT IS TRUE`.**  The false answer of round 3 is
  withdrawn; the true one (Thm 8bis.1e + Thm 8bis.1′) is proved; the
  equivalence with RH is labelled `CLASSICAL` and disclaimed as not new; the
  negative statement about the Frobenius form is the right statement but
  wrongly proved (`M1`), and the converse attempt is quarantined and does not
  close (`M2`,`M3`).  **R5 is not "dissolved" — it cannot be, because it asks
  for a sign, and row B's own summary (8bis.4(vi)) says the sign is row D's.**
  What R5 *can* ask of row B — name the object, factor it, and say honestly
  what is classical — is delivered.
* **R6 `DISSOLVED`** (Thm 3ter.12).

---

## 6. Grade

**Row B earns `WEIL-STRENGTH-COMPLETE` on Paper 43's declared carrier**
(B.4 amendment accepted by the owner), **conditional on the six `MAJOR`
repairs**, none of which is a clause of the contract and none of which
requires new mathematics:

* `M4` is **mandatory before the label is written down**: it is the one place
  where a round-4 display labelled `PROVED`/`CLASSICAL` is literally false as
  written, and the fix is a single sentence (`T_∞` on `D_A^∞`).
* `M1` and `M5` are mandatory because they are **repeated in §0, the banner,
  §10 and the README** — the same failure mode as `F1`, at one-tenth the
  amplitude.  `M1`'s repair strengthens the paper.
* `M2`, `M3`, `M6` are confined to quarantined or bookkeeping material.

Round 4 did what round 3 refused to do: it accepted a refutation of its own
central claim, withdrew it in the ledger rather than softening it, and proved
the correct statement instead — which turned out to be more interesting than
the false one.  The remaining defects are of a different order from `F1`:
none is a claim the paper makes and cannot support at all; all six are claims
stated with the wrong quantifier, the wrong convention, or the wrong proof of
a true conclusion.  That is a paper at the end of its audit, not in the middle
of one.

**One standing warning.**  Three of the six `MAJOR`s (`M4`, `M5`, `m1`,
`m2`) are *the same error as `F3`* — a hypothesis or normalization proved in
one theorem and silently dropped in the next.  Round 5, if there is one,
should press there first, and on `M1`'s replacement argument.
