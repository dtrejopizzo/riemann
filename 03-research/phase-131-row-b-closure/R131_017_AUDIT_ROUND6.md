# R131.017 — Audit of Paper 44, round 6 (final confirmation pass)

Scope: `R131_014` (N1–N5, m1′–m7′, n1′–n3′), `R131_015` (LF5, LF6),
`R131_016` (round 6); every `[REBUILT, phase 131, round 6]` passage of
`04-papers/44-row-b-arithmetic-family/main.md` (**12 marks**, all located),
`README.md`, and `scripts/verify_131_contacts.py` (re-run: **ALL CHECKS PASS**,
**ROUND-4**, **ROUND-5**, **ROUND-6 CHECKS PASS**).
Method: independent re-derivation of every round-6 estimate from the declared
formulas, plus a **mechanical** pass (script) resolving every `(8bis.*)`
reference in the file — the check my own round-5 report demanded.

**Headline.**  Round 6 is the best round of the phase *in the mathematics*.  A
`CLASSICAL` import was withdrawn **as false**, and not by retraction note but by
a proved lemma; the theorem that used it is now an honest conditional transfer
theorem with its arithmetic input isolated, named and `OPEN`; and the `C¹` gap
`N3` is closed by a genuinely new estimate whose proof turns on a cancellation
the paper states explicitly.  I re-derived Lemma 8bis.6a, Lemma 8bis.6b, the
Cramer orders, the expansion (8bis.13h) and the error total (8bis.13i)
independently; **all are correct**.  What does not survive is the *apparatus*,
for the third round running, and this time in its worst form: **three repairs
reported as executed were not executed** (`N4`'s §0 sentence, `N4`/`N5`'s
banner, `m7′`), the round-6 ledger and the README **assert** that they were,
**two new dangling equation references** were created in the very passage
rewritten to repair the dangling-reference finding, and the new hypothesis
`(H_L)` does not cover one of the two error terms its own proof produces.
Five `MAJOR`, nine `MINOR`, no `FATAL`.  **None touches B.1–B.9.**
**The label is EARNED**, conditional on `A1`–`A5`, none of which is new
mathematics and none of which is a clause.

---

## 1. Findings

### `A1` `MAJOR` — the withdrawn symbol-comparison reason is **still in §0**, verbatim, and three documents say it was deleted

*Location.* `main.md` lines 312–314 (§0, end of the round-5 paragraph).

*Text as it stands:* "… so **positivity fails on the pure Frobenius form,
unconditionally** — whose object is the Gram form of `Frob ⋆ Δ^{rad}` and
**not** the Frobenius Gram form, **since the latter's kernel lacks the
indefinite `ω̂_∞`**."

*Error.*  This is the sentence `N4` named, character for character, including
the grammatical break ("unconditionally — whose object is").  `R131_016` §3
states it was "**deleted**"; §10's round-6 block states the argument is "purged
from section 0, the banner, README's round-4 block and section 9bis W17";
README's round-6 block repeats it.  §0 was **not** touched.  The withdrawn
argument (`W19`) therefore still stands as the *stated reason* in the paper's
summary, and three status blocks now certify a repair that did not happen.
That second half is worse than the first: `N1` was exactly this failure
(round 5's report claimed an exemption that was not in the paper), and it has
recurred at larger amplitude.

*Repair (unchanged from `N4`).*  Replace the clause after "unconditionally"
with: "The object whose Hodge index is at issue is, **by Theorem 8bis.4(iii)**
— the colimit statement — the Gram form of `Frob ⋆ Δ^{rad}`."  Delete the
`ω̂_∞` reason.

### `A2` `MAJOR` — the `main.md` banner's round-4 bullet is untouched: it still cites the withdrawn clause and still headlines the retracted rate

*Location.* `main.md` lines 43–56 (the round-4 bullet of the status banner).

*Text as it stands:* "with a diagonal that diverges **LINEARLY in N** and like
log(1/eps)"; "Delta . Delta = -infinity (infinite genus), **rate computed**";
"The object whose Hodge index is RH is the Gram form of Frob * Delta^rad, NOT
the Frobenius Gram form **(Thm 8bis.4(iv))**."

*Error.*  `N5` required the two rate lines to be marked `[rate superseded,
round 5]` / `[round 6, N1]`, and `N4` required the attribution to move from
(iv) to (iii).  `grep` for `rate superseded` in `main.md` returns **nothing**.
The banner therefore contradicts §0's own "**no rate is headlined**" (line 307)
and Cor 8bis.1b′ / (C2), and attributes a live conclusion to the clause whose
round-4 form `W19` withdraws.  `README.md`'s round-4 block **is** correctly
marked `[SUPERSEDED IN ROUNDS 5–6]` with both retracted sentences named
(`N5`, README half: **REPAIRED**) — so the two documents disagree in the
opposite direction from round 5.

*Repair.*  Mark the banner's round-4 bullet exactly as README's round-4 block
is marked; change "(Thm 8bis.4(iv))" to "(Thm 8bis.4(iii); Thm 8bis.1e)".

### `A3` `MAJOR` — §8bis.4's own header and Theorem 8bis.4(v) still say the converse "closes modulo one named classical import"

*Location.* `main.md` line 3884 (the `[REBUILT …]` header of §8bis.4): "The
attempt now closes **modulo one named classical import**, and everything else
is proved here."  And Thm 8bis.4(v), line 3742: "§8bis.4 **settles** the variant
with per-`n` widths, **modulo one named classical import**."

*Error.*  After `W23` there is **no** classical import behind Thm 8bis.7; the
missing ingredient is the hypothesis `(H_L)`, which the paper itself grades
`OPEN` (8bis.7(c)) and explicitly declines to import ("not supplied by any
classical statement known to this paper").  So the subsection's own header and
a clause of the `PROVED` Theorem 8bis.4 both assert a settlement that
Theorem 8bis.7 retracts twelve pages later.  This is the `M1`/`N4` failure mode
— the headline outliving the theorem — and it is inside a `PROVED` theorem's
statement, not in prose.

*Repair.*  Both places: "…closes **modulo one explicit hypothesis `(H_L)`,
which is `OPEN`** (Theorem 8bis.7(c)); the analytic machinery is proved here."

### `A4` `MAJOR` — `N2` regressed: `(8bis.13d)` and `(8bis.13e)` no longer exist, and Step 2 of Theorem 8bis.7 rests on both

*Location.* Thm 8bis.7 Step 2 (lines 4147, 4149); `W21` (line 4737).

*Error.*  I ran the mechanical check my round-5 report asked for: every
`(8bis.*)` token in `main.md`, definitions versus references.  The three
displays `N2` named are now correctly defined — `(8bis.4b)` line 3521,
`(8bis.4c)` line 3528, `(8bis.8b)` line 3571 — and the double assignments of
`(8bis.5)` and `(8bis.7)` are resolved (`N2`: **REPAIRED**).  But round 6's
condensation of Step 2 ("Exactly as before: … (8bis.13d) gives …") **deleted the
displays** `(8bis.13c)`, `(8bis.13d)`, `(8bis.13e)` while keeping the pointers.
`(8bis.13d)` is the four `λ`-asymptotics and `(8bis.13e)` the two mismatch
estimates — i.e. the entire quantitative input of Step 2, and of the corrected
`(8bis.13e′)` that round 6 was written to install.  `W21` also cites
`(8bis.13d)–(8bis.13f)`.  Numbering now jumps `13b → 13e′`.

*Repair.*  Restore the two displays (the values are all correct and I verified
them — see §3), or inline them and delete the pointers.  Mechanical.

### `A5` `MAJOR` — Theorem 8bis.7(a) is labelled `PROVED`, but `(H_L)` as stated does not control the second error term of (8bis.13i)

*Location.* `(H_L)` / (8bis.14d) (line 4117); Step 4 (line 4211).

*Error.*  (8bis.13i) has **two** terms,
`O(L e^{−L/4}‖g̃‖_∞‖g̃‖_{C¹})` **and** `O(L e^{−L/2}‖g̃‖²_{C¹})`, and
`R(L)` of (8bis.14d) is built from the **first only**.  The second is dominated
by the first exactly when `‖g̃‖_{C¹} ≤ e^{L/4}‖g̃‖_∞` (I re-derived: the ratio
is `e^{−L/4}‖g̃‖_{C¹}/‖g̃‖_∞`).  Step 4 says this "holds for every profile of
bounded frequency and tilt, **and is assumed in `(H_L)` otherwise**".  It is
**not** assumed in `(H_L)`: `(H_L)` contains `Q(g_*) < 0` and the ratio, and
nothing else.  So the displayed hypothesis does not imply the displayed
conclusion, and part (a) is not proved *as stated* — the one substantive
mathematical defect of round 6.  The failure mode is the phase's standing one:
a condition established in one display and silently assumed in the next.

*Repair (one line, and it costs nothing).*  Define
`R(L) := [L e^{−L/4}‖g_*‖_∞‖g_*‖_{C¹} + L e^{−L/2}‖g_*‖²_{C¹}] / |Q(g_*)|`
and delete the "bounded frequency and tilt" sentence.  Everything downstream —
including Rem 8bis.7a(2)(β)'s threshold, which is driven by the first term —
is unchanged.

### `p1` `MINOR` — Lemma 8bis.6b(ii)–(iii): what is estimated is the **pair**, not the **quadruple**, and "false" is stronger than what is proved

(ii) estimates `{ρ_0, 1−\bar ρ_0}` and is correct.  (iii) then says "the
resonant **quadruple** produces `+e^{δL/2}`".  The quadruple also contains
`{\bar ρ_0, 1−ρ_0}`, and for `g_L = ψ(t/L)e^{−iγ_0t}` those give
`∫ψ e^{δt}e^{−2iγ_0t}` and `∫ψ e^{−δt}e^{−2iγ_0t}`: non-stationary phase with a
**fixed** `γ_0` gains only a constant factor `≍(δ/2γ_0)^k` per integration by
parts, **not** a power of `L`.  So the mismatched pair is of the **same
exponential order** `e^{δL/2}`, with **unknown sign**, and the lemma neither
estimates it nor mentions it (the review's `LF5` at least called it "negligible",
which is also unproved).  Consequently what the lemma proves is: *the
single-frequency test does not produce `(Wgr)`'s mechanism, and its resonant
pair has the opposite sign and half the exponent*.  That is decisive for
withdrawing an import — the burden is on the claimant — but the flat "**`(Wgr)`
is false**" of (iii), `W23` and §10 is one notch stronger than the proof.

*Repair.*  Either estimate the conjugate pair (a bound `O(e^{δL/2})` suffices to
kill the `e^{2δL}` claim), or say "`(Wgr)` is **unsupported**, and its stated
mechanism is refuted: the term it relied on is positive and of half its
exponent."  Nothing downstream changes: Rem 8bis.7a(2)(α) rests on (iv).

### `p2` `MINOR` — Lemma 8bis.6b is stated for the **non-primitive** test, while the ambient class is primitive

`(H_L)` and Thm 8bis.7 quantify over **primitive** `g`; Lemma 8bis.6b's `g_L`
is not primitive, and §8bis.4's whole point is that tests are primitivized by
`Π = −∂_t²+¼`.  Under `Π`, `\widehat{Πg}(s) = [¼−(s−½)²]\hat g(s)`; at the two
resonant points the factors are `A := ¼−(δ+iγ_0)²` and `\bar A`, so the pair
term is multiplied by `\mathrm{Re}(A²)` — positive for every `|γ_0| ≥ 1` (and
for all `γ_0` unless `δ` is near `½`), so the lemma's conclusion survives
primitivization.  But the paper does not say this, and a reader may object that
the refuted route is not the route the section uses.  One sentence.

### `p3` `MINOR` — Rem 8bis.7a(2)(β): the threshold `2α < δ + ¼` is **indicative**, not quantified

The arithmetic is internally consistent and I checked it:
`R(L) ≍ L e^{−L/4}·e^{2αL}/e^{δL} = L e^{(2α−δ−¼)L} → 0 ⟺ 2α < δ + ¼`.  But the
denominator is introduced as "polynomial in `L` times `e^{δL}`-**type**
factors" — an unproved order of magnitude for a witness that does not exist yet.
So the inequality records *where the natural candidates miss*, which is useful
and honest; calling it "quantified" (twice, plus §10 and `R131_016`) overstates
it.  Write "indicative threshold, on the natural sizes; not a theorem".

### `p4` `MINOR` — `m7′` **NOT REPAIRED**, and §10 says it was

Thm 8.2, line 3079, still reads: "Deleting §8bis.3–§8bis.4 changes no clause
verdict.  With that carve-out:  The objects used are: rational integers…" —
the colon, the double space and the capital, verbatim as in `m7′`.  §10's
round-6 block lists "`m7′` (garbled carve-out)" among the repairs.

### `p5` `MINOR` — §11 still says the quarantined imports are "**three**"

§11's *External inputs* bullet: "In the quarantined §8bis.3–§8bis.4: **three**,
all `CLASSICAL`…", with the list still numbered (i),(ii),(iii) and slot (ii)
occupied by the round-6 withdrawal note.  §10, README and `R131_016` all say
**two**.  The withdrawal is spelled out in place, so no reader is misled about
`(Wgr)` being live — but §11 is the import list that must be recorded beside the
label (condition 2 below), and it must say *two*, listing *Weil's criterion /
explicit formula* and *Chebyshev*, with `(Wgr)` moved to a "withdrawn" line.

### `p6` `MINOR` — `W21` still prints the superseded Cramer order

`W21` (line 4735): "Cramer gives `a = O(e^{−L})`, `b = O(Le^{−L/2})`".
`m1′`/`LF6`(a) asked for the exponent in **five** places; `(8bis.13e′)` and
`W23`'s closing paragraph are correct, `W21` is not.

### `p7` `MINOR` — a sign convention left open in the step that concludes a sign

Step 4: "`I_∂(Γ_u,Γ_u) = −Q(u)` **up to the fixed sign convention** of
Theorem 8bis.4(ii)".  The entire conclusion is the sign of `I_∂`; "up to the
sign convention" is the one phrase a sign-producing step may not contain.  Fix
the convention in 8bis.4(ii) and cite it without hedge.

### `p8` `MINOR` — frequency-sign mismatch between §8bis.3 and §8bis.4

The note after (8bis.8c) says "§8bis.4's complex `g_L = ψ(t/L)e^{iγ_0t}`";
Lemma 8bis.6b uses `e^{−iγ_0t}` (necessarily, for the resonance at `ρ_0` to
cancel the oscillation).  Harmless, symmetric under `γ_0 ↦ −γ_0`; cosmetic.

### `p9` `MINOR` — `(8bis.13c)` is skipped

With `(8bis.13d)`/`(8bis.13e)` gone (`A4`), the numbering runs
`13b → 13e′ → 13f`.  Fix with `A4`.

### `n1″` `NOTE` — the numerics are the strongest they have been

Block (D) is no longer tautological (`n1′` **REPAIRED**): it computes both local
residues from `ζ_p(s) = c_p/(1−p^{−s})` and `ζ_∞(s) = 1/s` for `c_p = log p`
**and** for `c_p = 1`, and agreement holds only for the former.  Blocks (E),(F),
(G) re-verified by hand in round 5.  New block (H): I reproduced the arithmetic
— `2·6.891984·8.505384e−4 = 1.172379e−2` ✓, and the `L: 40→60` log-slope
`log(3.7936e−1/7.7056e−2)/20 = 0.0797` ✓ — and the **analytic** claim behind it:
for `ψ` flat at the endpoint, `max_v exp(−1/v − δLv)` is attained at
`v = (δL)^{−1/2}` with value `e^{−2√(δL)}`, so the prefactor is
sub-exponential, the slope approaches `δ/2` **from below**, and the construction's
refutation of the "polynomial prefactor" (his §4.1, and of my own instruction)
is **right**.  Block (H′) is labelled "RESONANT QUADRUPLE ONLY", "SYNTHETIC
zero", "Numerics illustrate, not prove", and names the missing on-line sum as
`(H_L)` — the construction's own round-7 worry (4) is adequately handled.

### `n2″` `NOTE` — Lemma 8bis.6a is correct and is round 6's best step

Re-derived independently.  `(g_D)' = Σ_n g(\log n)ρ'(a_n)/gap_n`; the
coefficient-variation part is `O(‖g'‖_∞)` over at most five `n`; the mesh part
is `g(t)S(t)` with `S = Σ_nρ'(a_n)/gap_n`, and `Σ_nρ'(x−n) ≡ 0` (derivative of
the partition of unity) leaves `Σ_nρ'(a_n) = O(‖ρ''‖_∞/n) = O(1/x)` by Taylor
on `a_n = (x−n)(1+O(1/n))`, against `1/gap_n = x+O(1)`: `S = O(1)` **exactly**,
not better.  The construction's refutation of my `O(e^{−L/2}‖g‖_{C²})` prescription
(his §4.2) is **right**, and `O(1)` with only `C¹` is precisely what Step 3
needs, since `‖ẽ'‖_∞` is only ever paired against `‖ẽ‖_∞ = O(e^{−L/2})`.
The paper states the cancellation as load-bearing ("without it the naive bound
would be `e^{L}`"), which is the right way to write it.

---

## 2. Disposition of round-5 findings

| id | disposition |
|---|---|
| `N1` | **REPAIRED**, and well.  Thm 8bis.2 and Cor 8bis.2a are exempted from (C1) **in the statement**, in bold; and the `T_∞` addendum is correct and I checked it: `supp(F_ε⋆F_ε^†) ⊆ {|t| ≤ 2ε}`, `2ε < \log 2 ≤ \min|±k\log q|`, so the finite part vanishes identically and (8bis.8b) is not needed on the colimit.  The conclusion is genuinely *easier* there. |
| `N2` | **REPAIRED for the three displays named** (`(8bis.4b)`, `(8bis.4c)`, `(8bis.8b)` now exist; `(8bis.5)`/`(8bis.7)` singly assigned — verified mechanically over the whole file).  **REGRESSED elsewhere**: two new dangling pointers in the rewritten Step 2 (`A4`).  Net: the *specific* finding is closed, the *failure mode* is not. |
| `N3` | **REPAIRED, in full and correctly.**  Lemma 8bis.6a supplies `‖ẽ'‖_∞ = O(‖g̃‖_{C¹})`; the expansion (8bis.13h) removes `g_D'` from every pairing; the rough–rough term is bounded by `2L‖ẽ'‖_∞‖ẽ‖_∞`; and (8bis.13i) is exactly what I get by hand.  Both hypotheses of Lemma 8bis.5 are now verified at **both** applications — the standing warning of `R131.014` §5 is discharged. |
| `N4` | **NOT REPAIRED.**  §0 (`A1`) and the banner (`A2`) both still carry the withdrawn reason; §9bis `W17` (`m5′`) and README **are** repaired. |
| `N5` | **REPAIRED in `README.md`** (round-4 block marked `[SUPERSEDED IN ROUNDS 5–6]`, both retracted sentences named); **NOT REPAIRED in the `main.md` banner** (`A2`). |
| `LF5` | **ACCEPTED AND EXCEEDED.**  The review asked for a restatement; the construction proved a lemma, withdrew the import as false, and rebuilt the theorem as a conditional.  This is the correct response and the correct outcome (the third of the three permitted ones).  Residual: `p1` (pair vs quadruple), `p2` (primitivization). |
| `LF6`(a) | **REPAIRED** in `(8bis.13e′)` — `b = O(e^{−L/4}‖g̃‖_{C¹})`, which I re-derived from `λ_+(e)λ_−(w_1)/\det ≍ e^{−3L/4}e^{L}/e^{L/2}` — and the sup norm `‖bw_2‖_∞ ≍ e^{−L/2}` is indeed unchanged, so `(8bis.13f)` stands.  Residual: `W21` (`p6`). |
| `LF6`(b) | **REPAIRED** = `N3`. |
| `m1′` | REPAIRED in the theorem, not in `W21` (`p6`). |
| `m2′` | **REPAIRED.**  `|A+iB|² = |A|²+|B|²+2\,\mathrm{Im}(A\bar B)`, `A(−τ)=\overline{A(τ)}` spelled out, `\mathrm{Im}(A\bar B)` odd, integrates to `0` against the even symbol.  Correct. |
| `m3′` | **REPAIRED** — `(σ²+1)²`, valid for all `σ` and `T ≥ 1`, with the failure of `σ⁴+1` at `|σ| ≳ 1.4` recorded. |
| `m4′` | **REPAIRED and carried out.**  `λ_∓` have real kernels ⟹ `Re g_D'`, `Im g_D'` primitive; both are Dirichlet-polynomial profiles with the same widths and real coefficients; (8bis.8c) splits the form; one real summand is `> 0`.  This is the argument, and it is now written. |
| `m5′` | **REPAIRED** — `W17` carries `[SUPERSEDED BY W19; CORRECTED IN ROUND 6]` with the round-6 reading and the sentence "a withdrawals section may not carry an unmarked live assertion of a withdrawn claim".  Exactly right. |
| `m6′` | REPAIRED (`Q_{fin}` named at Thm 8bis.4(iv) and beside the §0 headline). |
| `m7′` | **NOT REPAIRED** (`p4`), and reported as repaired. |
| `n1′` | **REPAIRED** — block (D) now computes both residues, both `c_p` conventions. |
| `n2′` | **REPAIRED** — `A_S = ω̂_{fin}(0)` **exactly**, recorded at (8bis.8b) and used in Thm 8bis.4a. |
| `n3′` | **DISSOLVED** by `W23`: the import that carried the analytic content no longer exists. |

---

## 3. The new mathematics of round 6, re-derived

* **Lemma 8bis.6b (i),(ii),(iv) — correct.**  (i) is `1−\bar ρ = ρ`.  (ii): at
  `s = ρ_0` the phase cancels and `\hat g_L(ρ_0) = ∫ψ(t/L)e^{δt}dt > 0`; at
  `s = 1−\bar ρ_0` it is `∫ψ(t/L)e^{−δt}dt > 0`; the pair contributes
  `2\mathrm{Re}[\hat g(ρ_0)\overline{\hat g(1−\bar ρ_0)}] = 2\hat g(ρ_0)\hat
  g(1−\bar ρ_0) > 0`, of size `e^{δL}·e^{−δL/2} = e^{δL/2}` — **exponent `δ/2`,
  positive sign**, against `(Wgr)`'s `−L²e^{2δL}`.  Both the sign and the
  exponent fail, by a factor `e^{3δL/2}`.  The sub-exponential prefactor is
  right (see `n1″`).  (iv) is the decisive clause and is correct as stated:
  `∫we^{δt} ≥ ∫we^{−δt}` for `w ≥ 0`, `t > 0`, and `α+δ > α−δ` for any real
  tilt — so **peaking at `1−\bar ρ_0` requires cancellation**, which is both
  why Weil's real argument is two-frequency and why it destroys the sup-norm
  control.  That link between the two halves of the section is the genuinely
  new observation of round 6.  (Its proof line "(iv) is the monotonicity of
  `α ↦ α`" is garbled; the content is the displayed inequality.)
* **Step 2 — arithmetic re-derived, all correct.**  `λ_−(e) = O(‖g̃‖_{C¹})`
  (`‖e‖_∞ e^{L/2}`), `λ_+(e) = O(e^{−3L/4}‖g̃‖_{C¹})` (`‖e‖_∞e^{−L/4}`),
  `\det ≍ e^{L}e^{−L/2} − L² ≍ e^{L/2}`, `a ≍ e^{−L/2}/e^{L/2} = e^{−L}`,
  `b ≍ e^{L/4}/e^{L/2} = e^{−L/4}`; `‖aw_1‖_∞ ≍ e^{−L}e^{L/2} = e^{−L/2}`,
  `‖bw_2‖_∞ ≍ e^{−L/2}`.  The new `C¹` line of (8bis.13f) is right and was
  **not** requested by either auditor: `|a|‖u_1‖_{C¹} ≍ e^{−L}e^{L/2}`,
  `|b|‖u_2‖_{C¹} ≍ e^{−L/4}e^{−L/4}`, both `e^{−L/2}`, so the correction is
  `C¹`-small.  Round 5 would have had a second `C¹` gap here; the construction found
  it himself.
* **Step 3 — correct.**  (8bis.13h) is the right expansion (`g_D' = g̃ − ẽ`
  gives `I(g̃,g̃) − I(g̃−ẽ,g̃−ẽ) = I(ẽ,g̃)+I(g̃,ẽ)−I(ẽ,ẽ)`), and no pairing
  involves the mesh comb.  With `R = L/2+2`, Lemma 8bis.5 gives
  `C_0e^{L/4}·e^{−L/2}‖g̃‖_{C¹}L‖g̃‖_∞ + C_1e^{−L/2}L‖g̃‖²_{C¹}` for the mixed
  terms and `C_0e^{L/4}Le^{−L}‖g̃‖²_{C¹} + C_1Le^{−L/2}‖g̃‖²_{C¹}` for the
  rough–rough term; absorbing, exactly (8bis.13i).  The first term **is** the
  numerator of `R(L)`, so the theorem's hypothesis is the theorem's error —
  which is the honest way to write a conditional.  Defect: the second term
  (`A5`).
* **Theorem 8bis.7 as a conditional — the right shape.**  (a) is a transfer
  statement about Riemann sums and contains no arithmetic; (b) imports only
  Weil's criterion, which is genuinely classical; (c) is `OPEN` and says so
  three times, including "not asserted".  The construction's refutation of the
  instruction's item 1(a) (§4.4 of `R131_016`) is **correct**: "there exist
  primitive `g_*` in a **moving** window `[L/2,L]` with norm control" is *not*
  a classical statement, and importing it would have replaced a false import by
  an unnamed one.  A weaker import is better than a false one; this is the
  right call and it is the reason the label survives round 6.

## 4. Renaming test on round-6 material

* **Lemma 8bis.6a** — `PASS`.  Stripped of prose: *a Riemann sum built from a
  smooth partition of unity on a slowly varying mesh has derivative `O(‖g‖_{C¹})`,
  because `Σ_kρ'(x−k) ≡ 0`.*  Honest analysis; no arithmetic hides in it.
* **Lemma 8bis.6b** — `PASS`.  Stripped: *the Laplace transform of a
  non-negative function is bigger at the bigger exponent.*  It is elementary and
  the paper presents it as elementary; and it is used only **destructively**,
  to kill an import, which is the direction in which a triviality is allowed to
  be decisive.
* **Theorem 8bis.7** — `PASS AS A CONDITIONAL`, which it did not do in rounds
  4–5.  Stripped: *if a small-norm negative witness exists in a moving window,
  the Dirichlet mesh sees it.*  No statement about zeros survives the stripping;
  the arithmetic is entirely inside `(H_L)`, which is `OPEN`.
* **`W23`** — `PASS`.  A withdrawal that names what was claimed, why it is
  false, and what replaces it, without softening.

## 5. Independence and the hypothesis-carrying check on §8bis, final pass

Zeros and RH occur **only** in Thm 8bis.4(ii),(iii) (`CLASSICAL`),
Thm 8bis.4(iv)/8bis.4a/Rem 8bis.4b (which assert nothing about zeros), and
§8bis.4 (Lemmas 8bis.5, 8bis.6, 8bis.6a, 8bis.6b, Thm 8bis.7, Rem 8bis.7a) —
all inside the carve-out `§8bis.3–§8bis.4` of Thm 8.2.  Deleting those two
subsections changes no clause verdict.  **Independence holds.**

Hypothesis-carrying, item by item: `ε<ε_0` ✓; bare/`♭` ✓; profile value ✓;
`c_p = \log p` ✓; real-vs-complex ✓ (now *carried out*, `m4′`); colimit `T_∞` ✓
with Thm 8bis.2/Cor 8bis.2a **explicitly exempted** in the statement (`N1`
closed); Lemma 8bis.5's **two** hypotheses (`supp ⊆ [−R,R]` and `‖h‖_{C¹}`)
verified at **every** application, which is the check I demanded for round 6 —
`PASS`, via Lemma 8bis.6a; `A_S` as a **chart** constant carried into
Thm 8bis.2, Cor 8bis.2a, Thm 8bis.4a, Rem 8bis.4b(1) ✓.  The one failure is
`A5`: a side condition (`‖g̃‖_{C¹} ≤ e^{L/4}‖g̃‖_∞`) established in Step 4 and
attributed to a hypothesis that does not contain it.  Same failure mode, now
down to a single inequality.

## 6. Verdict per clause

| clause | round-6 verdict |
|---|---|
| **B.1** | `PROVED` (unchanged). |
| **B.2** | `PROVED`, non-vacuous. |
| **B.3** | `PROVED`, true unit. |
| **B.4** | `REFUTED AS STATED`; `PROVED AS AMENDED` (accepted ), on objects in degree (Thm 6bis.4), composition law proved (Lemma 6bis.3a), extended additively (Thm 6bis.3c); ledger row matches the text. |
| **B.5** | `PROVED`; `Λ(p^k) = \log p` with a uniqueness theorem (Thm 8bis.8), up to one global scale. |
| **B.6** | `PROVED`, both halves non-vacuous. |
| **B.7** | `PROVED` as a test, by the review's ruling; my dissent (`PARTIAL`, as a mechanism, Rem 6.5a′) stands and is recorded verbatim beside it.  I accept that procedure as the resolution. |
| **B.8** | `PROVED`; script re-run, four banners pass; (D) now non-vacuous, (E),(F),(G),(H),(H′) re-derived or reproduced by hand. |
| **B.9** | `PROVED` in substance and in the text (Thm 8.2's carve-out, §11's list, "used by no clause"), subject to the two text corrections `A3` and `p5`, neither of which is a mathematical defect. |

§8bis is outside the contract; `A1`–`A5` and every minor flip **no clause**.

## 7. Reservations

* **R1 `DISSOLVED`.**
* **R2 `DISSOLVED IN DEGREE, ON THE MONOID`**; object level `REFUTED`, not open;
  the ledger agrees with the text.
* **R3 `DISSOLVED`.**
* **R4 `DISSOLVED`, in the only form available** — uniqueness given a named
  requirement, up to one global scale.
* **R5 `ANSWERED IN THE FORM THAT IS TRUE`, and round 6 improves the answer
  once more.**  The false import is gone; the converse no longer pretends to be
  classical; what is proved (the transfer machinery) and what is missing
  (`(H_L)`) are separated by a line.  R5 still cannot be *dissolved*: it asks
  for a sign, and the sign is row D's.
* **R6 `DISSOLVED`.**

## 8. Grade

**Row B earns `WEIL-STRENGTH-COMPLETE` on Paper 43's declared carrier**, the
B.4 amendment having been accepted by the repository record .

What must be recorded **beside the label**, in the paper and in the ledger:

1. **The carrier and the clauses.**  "On Paper 43's declared carrier
   (§14.0a–b), as a theorem about row A's declared trace.  **B.4 is `REFUTED AS
   STATED` and `PROVED AS AMENDED`**, the amendment accepted by the repository record
**B.7 `PROVED` by the review's ruling, with the audit's dissent
   (`PARTIAL`, as a mechanism) recorded verbatim beside it.**"
2. **What row B does not deliver.**  "No sign, no positivity, no `𝓝_∞ = 0`, and
   no statement about zeros outside Thm 8bis.4(ii)–(iii) and §8bis.3–§8bis.4.
   The quarantined imports are **two**, both `CLASSICAL` — Weil's
   criterion/explicit formula, and Chebyshev's `ψ(X) ≤ cX` — each used by no
   clause of B.1–B.9 and deletable without changing a verdict.  The sign is
   row D's."
3. **The three quantifiers.**  "The interface with Weil's criterion is a
   **colimit** statement (`T_∞` on `D_A^∞`); at a finite chart it is **false**.
   No divergence **rate** is convention-free; what is stated is that
   `I_A(Frob_n,Frob_n)` does not exist.  Thm 8bis.4a is a **fixed-chart**
   statement; its colimit version is `OPEN`.  Thm 8bis.2 is a **fixed-chart**
   theorem, exempted from (C1), and holds a fortiori on the colimit."
4. **The withdrawal of record.**  "`(Wgr)`, a `CLASSICAL` import carried by
   rounds 4–5, is **withdrawn as false** (§9bis `W23`, Lemma 8bis.6b).  The
   implication *positivity on Dirichlet-polynomial profiles ⟹ RH* is **`OPEN`**
   and is not claimed: Thm 8bis.7 is a **conditional** transfer theorem, (a)
   `PROVED`, (b) `CLASSICAL`, (c) `OPEN` under the explicit hypothesis
   `(H_L)`."
5. **§8bis.4 is quarantined**, and as of this audit its part (a) is
   `PROVED MODULO A5` (one inequality in the statement of `(H_L)`).

**Conditions on the label** (none is new mathematics; none is a clause):

* **Mandatory before the label is written down:** `A1` (§0), `A2` (banner),
  `A3` (§8bis.4's header and Thm 8bis.4(v) still promising a classical
  settlement the paper has retracted), `A4` (two dangling pointers carrying all
  of Step 2's arithmetic), and `p5` (§11 must say **two**).
* **Mandatory before Thm 8bis.7(a) keeps the label `PROVED`:** `A5` — put both
  error terms of (8bis.13i) into `R(L)`, or demote (a) to `PROVED for profiles
  with ‖g‖_{C¹} ≤ e^{L/4}‖g‖_∞`.
* **Corrections of record:** `p1`–`p4`, `p6`–`p9`.

**The procedural finding, and it is the one I want on the record.**  Round 6's
mathematics is the strongest of the six: an import was withdrawn *as false*
rather than softened, on a lemma the construction proved himself; the `C¹` gap was
closed by an estimate neither auditor had correctly prescribed (both of us asked
for the wrong bound, and he said so and proved the right one); and a theorem
that could have been kept by importing an unnamed hypothesis was instead reduced
to a conditional.  That is the behaviour a label is for.  **Against it:** three
items were reported as repaired and are not in the paper (`A1`, `A2`, `p4`), and
two status blocks and a README now certify those repairs.  Round 5 had one such
item (`N1`); round 6 has three.  Prose reports of prose repairs are no longer
reliable in this phase, and the remedy is not a seventh round of reading.
**Before the label is written down, `A1`–`A5` and `p5` must be verified by
`grep`, not by report** — the reference-resolution check that found `A4` took
one script and ten seconds, and it is the check that should have been run in
round 5, in round 6, and now.
