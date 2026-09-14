# R131.014 — Hostile audit of Paper 44, round 5 (confirmation pass)

Auditor: Claude (Opus 5, 1M), adversarial auditor of record for phase 131.
Date: 2026-09-12.
Scope: `R131_011` (M1–M6, m1–m7, n1–n3), `R131_012` (LF1–LF4), `R131_013`
(builder, round 5); every `[REBUILT, phase 131, round 5]` passage of
`04-papers/44-row-b-arithmetic-family/main.md` (17 marks), `README.md`, and
`scripts/verify_131_contacts.py` (re-run: **ALL CHECKS PASS**, **ROUND-4**,
**ROUND-5 CHECKS PASS**).
Method: independent re-derivation of every round-5 estimate from the declared
formulas, not re-reading of the builder's prose.

**Headline.**  The six `MAJOR`s are repaired **in the theorems**.  I verified
independently: the primitivity of `Π g` by two integrations by parts (no
boundary terms, sign convention of `λ_∓ = ∫g e^{±s/2}` correct); the strict
positivity `ω̂_fin(0) = Σ_{p∈S_f}(\log p)2p^{−1/2}/(1−p^{−1/2}) > 0` and its
bound `A_S` (which **equals** `ω̂_fin(0)`); the concentration/tail split of
Theorem 8bis.4a; the pointwise partition-of-unity estimate (8bis.13a)–(8bis.13b)
of the rebuilt Lemma 8bis.6, which is now correct and is the best repair of
`M3`/`LF1`; the four `λ`-asymptotics (8bis.13d), the determinant `≍ e^{L/2}`,
and the sup-norm size `O(Le^{−L/2})` of the correction; and the builder's
refutation of the lead's `C¹` prescription, which is **right**.  Withdrawals
`W19`–`W22` are recorded where withdrawals belong and are not softened.
What does not survive: **five `MAJOR` findings**, of which one is mathematical
(**`N3`**: Theorem 8bis.7 Step 3 has no control of `‖ẽ‖_{C^1}`, and the
`C_1‖h‖_{C^1}` term of Lemma 8bis.5 is therefore unbounded for the two
rough–rough pairings), one is the **same `M4` slip recurring** (**`N1`**:
Theorem 8bis.2 is a chart theorem left inside the standing convention `T = T_∞`,
and the exemption the builder's report says it inserted is **not in the
paper**), one is the **`m3` repair done backwards** (**`N2`**: the
cross-references were renumbered and the displays were not, leaving six
references to equations that do not exist — including Theorem 8bis.4a's own
bound), and two are the withdrawn `M1` argument surviving in the headlines
(**`N4`**, **`N5`**).  None touches B.1–B.9.  **The label is EARNED**,
conditional on `N1`, `N2`, `N4`, `N5`; `N3` is quarantined.

---

## 1. Findings

### `N1` `MAJOR` — Theorem 8bis.2 is a fixed-chart theorem left under convention (C1); the exemption the builder reports was not written

*Location.* Thm 8bis.2 (statement and proof), the display bounding
`|Σ_{p∈S_f}\hat W_p| ≤ A_S`; `R131_013` §1 and §6, which both assert that
"Thm 8bis.2 is now explicitly stated *at a fixed finite chart*".

*Error.*  It is not.  `grep "fixed chart\|fixed finite chart"` returns no hit
inside Thm 8bis.2; the only nod is a trailing clause of Cor 8bis.2a ("the
finite-place symbol being bounded by (8bis.8b) **at the fixed chart**"), which
is prose about a corollary and additionally cites a nonexistent display
(`N2`).  Meanwhile (C1) declares, in bold, that **throughout §8bis** `T` means
`T_∞` and `W_fin` is the kernel over **all** primes.  Under that convention the
proof's key uniform bound is **false**: the colimit symbol is unbounded, and
the paper says so itself three pages later (Rem 8bis.4b(1),
`ω̂_fin^∞(0) = +∞`, numerics block (E)).  So a `PROVED` theorem carries a proof
step that the section's own standing convention contradicts — precisely the
`M4` failure mode, one round later, and found by neither the builder's
line-by-line pass nor his own table in `R131_013` §6.

*Repair (one sentence, and the conclusion strengthens).*  State Thm 8bis.2 at a
fixed finite chart, exempted from (C1); and add that under `T_∞` the
conclusion is unchanged and easier, because for `ε < ½\log 2` the profile
`h` meets **no** atom of `W_fin^∞`, so the finite part is identically `0` and
the `−\log(1/ε)` divergence is purely archimedean.

### `N2` `MAJOR` — finding `m3` was repaired in the cross-references only: six references now point at equations that do not exist

*Location.* Cor 8bis.2a ("The theorem is **(8bis.4b)**", "(8bis.4b)–(8bis.4c)
supply the rate", "bounded by **(8bis.8b)**"); Thm 8bis.4a Step 1
("`|ω̂_fin| ≤ A_S` by **(8bis.8b)**"); Rem 8bis.4b(1) ("the bounded symbol
`ω̂_fin` of a finite chart **(8bis.8b)**").

*Error.*  No display in `main.md` is numbered `(8bis.4b)`, `(8bis.4c)` or
`(8bis.8b)`.  The displays are still `(8bis.4)` (the `−∞` rate), `(8bis.5)`
(the `L^2`-normalized form) and `(8bis.7)` (the `A_S` bound), and `(8bis.5)`
and `(8bis.7)` are **still doubly assigned** — `(8bis.5)` to Cor 8bis.1d's Gram
decomposition **and** to Thm 8bis.2's normalized form, `(8bis.7)` to
Thm 8bis.1e's kernel value **and** to the `A_S` bound.  The round-5 note inside
Cor 8bis.2a announces the renumbering ("the displays are renumbered and the
cross-references corrected"); only the second half was done.  The worst
instance is Thm 8bis.4a Step 1: the one quantitative hypothesis of the new
`PROVED` theorem (`|ω̂_fin| ≤ A_S`) is justified by a pointer to nothing.

*Repair.*  Renumber the three displays of Thm 8bis.2 to `(8bis.4b)`,
`(8bis.4c)`, `(8bis.8b)` as the cross-references already assume.  Purely
typographical; but `m3` must be graded `NOT REPAIRED` until it is done.

### `N3` `MAJOR` — Theorem 8bis.7, Step 3: `‖ẽ‖_{C^1}` is never controlled, and Lemma 8bis.5's second term needs it

*Location.* Thm 8bis.7 Step 3, "By Young, **with the derivative falling on the
smooth factor** … and the same with `g_D'` in place of `\tilde g_L` (whose
`L^1` norm is `O((1+|γ_0|)^2L)`)".

*Error.*  The identity used is
`I(\tilde g_L,\tilde g_L) − I(g_D',g_D') = I(ẽ,\tilde g_L) + I(g_D',ẽ)`
(correct: `I(ẽ,v)+I(v,ẽ)+I(ẽ,ẽ) = I(ẽ,u)+I(v,ẽ)`).  The **first** cross term
is fine and I verified it: `‖ẽ⋆\tilde g_L^†‖_{C^1} ≤ ‖ẽ‖_∞‖\tilde g_L'‖_1`,
the derivative genuinely falls on the smooth factor, and Lemma 8bis.5 at
`R = L/2+2` gives `O(Le^{−L/4})`.  The **second** term `I(g_D',ẽ)` has **no
smooth factor at all**: `g_D'` is a mesh comb and `ẽ = \tilde g_L − g_D'` is a
smooth function minus a mesh comb.  Lemma 8bis.5 reads
`|T_∞(Γ_h)| ≤ C_0‖h‖_∞e^{R/2} + C_1‖h‖_{C^1}`; the `‖h‖_∞` half is fine
(`‖ẽ‖_∞‖g_D'‖_1 = O(Le^{−L/2})`, which is what the paper checks), but the
`C_1‖h‖_{C^1}` half requires `‖ẽ'‖_∞` or `‖(g_D')'‖_1`, and the naive bounds
are `‖ẽ'‖_∞ ≍ ‖ρ'‖_∞/gap_n ≍ e^{L}` and `‖(g_D')'‖_1 ≍ e^{L}` (one `O(1)`
contribution per bump, `≍ e^L` bumps).  That gives
`|I(g_D',ẽ)| = O(Le^{L/2})`, which **dominates** the main term
`L^2e^{2|β−1/2|L}` whenever `|β−1/2| < 1/4`, i.e. for exactly the zeros the
theorem is about.  So Step 3, as written, does not close.  The builder's own
round-5 note ("only sup norms of the *error* enter Step 3, because the
derivative always falls on the smooth factor") is true of one of the two cross
terms and **false of the other**, and it is the sentence that hides the gap.

*Repair (available, and it is the same slow-variation computation twice).*
Add to Lemma 8bis.6 the `C^1` statement `‖(g−g_D)'‖_∞ = O(‖g‖_{C^2})`.  It is
true and is proved by differentiating (8bis.13b): with `x = e^t`,
`\tfrac{d}{dx}Σ_nρ(a_n(x)) = Σ_nρ'(x−n) + O(1/n) = O(1/n)` because
`Σ_nρ'(x−n) ≡ 0` (differentiate the partition of unity), so
`\tfrac{d}{dt} = x\tfrac{d}{dx}` is `O(1)`; and the coefficient variation
contributes `Σ_n|g(\log n)−g(t)|‖ρ'‖_∞/gap_n = O(‖g'‖_∞)`.  The **cancellation
in the partition of unity** is what kills the apparent `e^{L}`, and nothing in
the present text says so.  With `‖ẽ‖_{C^1} = O(1)` one gets
`‖g_D'⋆ẽ^†‖_{C^1} ≤ ‖ẽ'‖_∞‖g_D'‖_1 = O(L)`, and Step 3 survives — but the
estimate must be written, not assumed.  Until it is, Thm 8bis.7 is
`NOT PROVED AS WRITTEN`.  (It is quarantined; no clause moves.)

### `N4` `MAJOR` — §0 and the banner still justify the round-5 conclusion by the round-4 argument that `W19` withdraws

*Location.* §0, last sentence of the round-5 paragraph: "… so **positivity
fails on the pure Frobenius form, unconditionally** — whose object is the Gram
form of `Frob ⋆ Δ^{rad}` and **not** the Frobenius Gram form, **since the
latter's kernel lacks the indefinite `ω̂_∞`**."  Banner, round-4 bullet: "The
object whose Hodge index is RH is the Gram form of `Frob * Delta^rad`, NOT the
Frobenius Gram form **(Thm 8bis.4(iv))**."

*Error.*  "Since the latter's kernel lacks the indefinite `ω̂_∞`" **is** the
symbol-comparison argument.  It establishes only that the two forms are
distinct — Thm 8bis.4(iv)(a) — and the paper's own Thm 8bis.4(vi),
Rem 8bis.4b(3) and `W19` say three times that the conclusion rests on **(iii)**
and **not** on a comparison of symbols.  The banner still attributes the
conclusion to **(iv)**, the clause whose round-4 form is withdrawn.  §0's
sentence is also grammatically broken ("unconditionally — whose object is").
This is `F1`/`M1` at one further reduction of amplitude: the theorem is right,
the headline still carries the refuted reason.

*Repair.*  §0: "… positivity fails on the pure Frobenius form at every finite
chart (Thm 8bis.4a).  The object whose Hodge index is at issue is, by
Thm 8bis.4(iii) — the colimit statement — the Gram form of `Frob ⋆ Δ^{rad}`."
Banner: cite **(iii)** and Thm 8bis.1e, not (iv).

### `N5` `MAJOR` — `README.md`'s round-4 block is unmarked and still asserts the withdrawn claim and the retracted rate (finding `m6`, one round later)

*Location.* `README.md`, the round-4 status block: "and a new **negative**
theorem: the sign of the pure Frobenius Gram form is **not** RH
(Thm 8bis.4(iv))"; and "Its diagonal … **diverges** — linearly in `N` at each
`r ∤ n` … and like `−\log(1/ε)`".  Banner, round-4 bullet: "with a diagonal
that diverges LINEARLY in N", "Delta . Delta = -infinity (infinite genus),
**rate computed**".

*Error.*  Round 5 marked the README's **round-3** block `[SUPERSEDED IN
ROUNDS 4–5]` (`m6`, done) and left the **round-4** block unmarked, although it
now carries (a) the claim withdrawn by `W19` and (b) the `N`-linear rate that
`M5`/(C2) removed — while `main.md` §10's round-4 block **is** explicitly
marked "SUPERSEDED WHERE THE ROUND-5 BLOCK APPLIES (the divergence rate, the
chart quantifier, and Thm 8bis.4(iv))".  Two documents disagree, and the claim
"**No rate is headlined anywhere in this paper now**" (Cor 8bis.1b′,
`R131_013` §4) is false in `README.md` and in the banner.

*Repair.*  Mark the README round-4 block exactly as §10's is marked, naming the
two retracted sentences; and add `[rate superseded, round 5]` to the two banner
lines.

### `m1′` `MINOR` — Cramer: `b = O(e^{−L/4})`, not `O(Le^{−L/2})`

*Location.* Thm 8bis.7 (8bis.13e)→(8bis.13f); repeated in `W21`, §10's round-5
block, `README`, and `R131_013` §3.

*Error.*  `b = [λ_+(e)λ_−(w_1) − λ_−(e)λ_+(w_1)]/\det`; with
`λ_+(e) = O(e^{−3L/4})`, `λ_−(w_1) ≍ e^{L}`, `\det ≍ e^{L/2}`, the **first**
term is `O(e^{L/4}/e^{L/2}) = O(e^{−L/4})`, which **dominates** the second,
`O(L\cdot e^{−L/2})`.  The displayed formula is right; its evaluation drops the
larger term.  (The lead's `b ≍ Le^{−L/4}` was nearer.)

*Consequence: none.*  `‖bw_2‖_∞ = O(e^{−L/4}·e^{−L/4}) = O(e^{−L/2})`, so
(8bis.13f) — `‖aw_1+bw_2‖_∞ = O(e^{−L/2})`, the size of `‖e‖_∞` — **stands**,
and Step 3's input is unchanged.  Fix the exponent in five places.

### `m2′` `MINOR` — (8bis.8c): the cross term is `2\,\mathrm{Im}`, not `2\,\mathrm{Re}`, and as written the proof fails

*Location.* Def 8bis.3, proof of (8bis.8c).

*Error.*  For real `u,v` with `A = \hat u`, `B = \hat v`,
`|A+iB|^2 = |A|^2+|B|^2+2\,\mathrm{Im}(A\overline B)`.  The paper writes
`+2\mathrm{Re}(A\overline B)`.  The distinction is exactly the point: `A(−τ) =
\overline{A(τ)}` gives `A\overline B` at `−τ` equal to `\overline{A\overline
B}`, so `\mathrm{Im}(A\overline B)` is **odd** (and integrates to `0` against
the even symbol, as claimed) while `\mathrm{Re}(A\overline B)` is **even** and
would **not**.  Conclusion correct, proof as printed self-defeating; one symbol.

### `m3′` `MINOR` — Thm 8bis.4a Step 3: the majorant is false as displayed

`(σ^2/T^2+\tfrac14)^2 ≤ σ^4+1` for `T ≥ 1` fails once `σ^2/2 + 1/16 > 1`, i.e.
for `|σ| ≳ 1.4`.  Write `≤ 2(σ^4+1)` (or `(σ^2+1)^2`).  Schwartz decay makes
the conclusion untouched.

### `m4′` `MINOR` — Thm 8bis.7 Step 4: the complex→real reduction is invoked but not carried out

"Complex profiles are handled by (8bis.8c)" leaves two things unsaid, both
true and both needed: `λ_∓` are **real** functionals, so primitivity of `g_D'`
passes to `\mathrm{Re}\,g_D'` and `\mathrm{Im}\,g_D'`; and both are again
Dirichlet-polynomial profiles with per-`n` widths (real coefficients
`\mathrm{Re}\,c_n`, `\mathrm{Im}\,c_n`).  Only then does
`I(Γ_{g_D'},Γ_{g_D'}) > 0` contradict a hypothesis quantified over real
profiles.  Two sentences.

### `m5′` `MINOR` — §9bis `W17` still asserts what `W19` withdraws

`W17`'s *Replaced by* paragraph ends "plus the new **negative**
Theorem 8bis.4(iv): the sign of the pure Frobenius Gram form is **not** RH,
because `ω̂_∞` is indefinite.  The object whose Hodge index is RH is the Gram
form of `Frob ⋆ Δ^{rad}`."  `W19`, eight lines below, withdraws that sentence.
A withdrawals section that contains an unmarked live assertion of a withdrawn
claim is the one place where this cannot be tolerated.  Add
"[superseded by `W19`]".

### `m6′` `MINOR` — "the pure Frobenius form" names two different objects

`Q_{fin}` of Thm 8bis.4a is the form with kernel `W_{fin}^S` **on radial
profiles**.  The *Frobenius Gram form* of Cor 8bis.1d is the form on the family
`{Frob_n^{sm}}`, whose **diagonal** is the divergent negative
`I_A(Frob_n^{sm},Frob_n^{sm})` of Cor 8bis.1b′ and whose off-diagonal carries
the extra factors `V_N^{(m,n)}(h_m⋆h_n^†)(n/m)`.  They are not the same
quadratic form and their positivity properties are not the same question.
Thm 8bis.4(iv) does define `Q_{fin}` correctly ("the quadratic form with kernel
`W_{fin}` alone"), but the headline phrase "positivity fails on the **pure
Frobenius form**" is used in §0, the banner, §10, the README and `W19` without
that definition beside it.  Given `F1`'s history, define it once and use the
definition.  (No mathematical error; a naming risk of exactly the `F1` kind.)

### `m7′` `MINOR` — Thm 8.2's carve-out sentence is garbled

"Deleting §8bis.3–§8bis.4 changes no clause verdict.  With that carve-out:  The
objects used are: …" — a colon, a double space and a capital.  The carve-out
itself is correct and complete.

### `n1′` `NOTE` — numerics block (D) is still the tautology of `n3`

Blocks (E), (F), (G) are new and genuinely non-vacuous — I re-derived (E)
(`S_f = {2}`: `0.693147·2·2^{−1/2}/(1−2^{−1/2}) = 3.346811` ✓), (F)'s two
columns, and (G)'s ratio `≈1` against `e^{−L/2}` — but block (D) still asserts
`|c_p/\log p − 1| < TOL` for `c_p := \log p`, which `n3` named as verifying
nothing.  Delete it or make it compute the two residues from the two integrals.

### `n2′` `NOTE` — `A_S` is attained exactly where Thm 8bis.4a concentrates

`A_S = Σ_{p∈S_f}(\log p)2p^{−1/2}/(1−p^{−1/2})` is not merely a bound on
`ω̂_fin`: it **is** `ω̂_fin(0)`.  So Step 1's `c := ½ω̂_fin(0) = ½A_S`, and
Step 4's requirement is exactly `M_{tail}/M_{bulk} < 1/2`.  Worth one sentence:
it makes the theorem's mechanism transparent (the symbol's maximum is at the
concentration point) and explains why the numerics print one number for both.

### `n3′` `NOTE` — `(Wgr)` is very close to the conclusion it buys

As restated for primitive tests with no Tate clause, `(Wgr)` asserts that for
the concentrated family `\tilde g_L` the **whole** zero sum `Σ_ρ\hat h_L(ρ)`
has a fixed sign and modulus `≍ L^2e^{2|β−1/2|L}` — i.e. that the hypothetical
off-line pair dominates every other zero.  That domination *is* the substance
of the classical converse.  The restatement is correct and honest (and the
`Π`-repair of the Tate clause is right: `\widehat{Πg}(ρ) = ρ(1−ρ)\hat g(ρ)`
vanishes at `ρ = 0,1`, preserves support, and multiplies `\hat g(ρ_0)` by
`|ρ_0(1−ρ_0)|^2 ≠ 0`), but Rem 8bis.7a(1) should say that the import carries
the analytic content, not merely that it is classical.

---

## 2. Disposition of round-4 findings

| id | disposition |
|---|---|
| `M1` | **REPAIRED in the theorem; NOT repaired in the headlines.**  The withdrawal (`W19`) is exact and correctly reasoned, and Thm 8bis.4a is **correct** — I checked all four steps independently (see §3).  But the withdrawn argument survives as the *reason* in §0 and the banner (`N4`), in `README`'s round-4 block (`N5`) and in `W17` (`m5′`). |
| `M2` | **REPAIRED WITH A NEW ERROR.**  The `Π` route, the renaming to `(Wgr)`, the deletion of the Tate clause and the `w_1,w_2` correction are all correct; `(8bis.13d)` and the determinant check out.  New: `N3` (the `C^1` gap in Step 3) and `m1′` (the value of `b`). |
| `M3` | **REPAIRED.**  Lemma 8bis.6 is now a genuine partition of unity, the pointwise statement is proved by slow variation, the spurious `L` is gone, and the counterexample is in the script.  I re-derived (8bis.13a)–(8bis.13b) and Step 2 line by line; both are right. |
| `M4` | **REPAIRED WITH A NEW ERROR.**  (C1) is exactly the sentence I asked for and is carried into Thm 8bis.1e, Thm 8bis.4(iii),(vi), Lemma 8bis.5 and §8bis.4.  The builder's two **extra** slips: Thm 8bis.4a's fixed-chart scope is correctly written (with `W_{fin}^S` and Rem 8bis.4b(1)) — but Thm 8bis.2's is **not** (`N1`), contrary to `R131_013` §1 and §6. |
| `M5` | **REPAIRED.**  (C2), (8bis.0), Cor 8bis.1b′ and Rem 8bis.1c are correct; the convolution `\mathbf 1_{n^{−1}U_r}⋆\mathbf 1_{nU_r} = vol(U_r)\mathbf 1_{U_r}` is right, and both limits (bare `→0`, `♭ →−∞` geometrically) are right.  The builder's refutation of the instruction's framing — "linear divergence" is a statement about the **smeared idempotent**, not about the Gram diagonal in either convention — is **correct and is the better answer**.  Residual: the banner and README still headline the rate (`N5`). |
| `M6` | **(a) REPAIRED** (the P123.038 §5 row is genuinely re-graded, with the four open items and the object-level refutation separated).  **(b) REPAIRED** (`(Wgr)`; §11's three-item list, each "used by no clause").  **(c) REPAIRED** (Thm 8.2's carve-out; `m7′` is cosmetic). |
| `m1` | REPAIRED (Thm 8bis.1e now carries `ε<ε_0` and the chart clause). |
| `m2` | REPAIRED ((8bis.5) carries `V_N^{(m,n)}` and `(h_m⋆h_n^†)(n/m)`). |
| `m3` | **NOT REPAIRED** — see `N2`: renumbering announced, cross-references changed, displays not.  Worse than round 4, because the references now dangle. |
| `m4` | REPAIRED (Chebyshev named, lemma relabelled `CLASSICAL`, the constant `4` removed with Littlewood's reason given). |
| `m5` | **REPAIRED WITH A NEW ERROR** (`m2′`: `\mathrm{Re}` for `\mathrm{Im}`). |
| `m6` | **REPAIRED for the round-3 block; REGRESSED at the round-4 block** (`N5`). |
| `m7` | REPAIRED (all rounds listed). |
| `n1` | REPAIRED (Thm 8bis.8 "up to a global scale", quotient in the statement). |
| `n2` | REPAIRED, and correctly: the operative reason is the archimedean coordinate plus `ε<ε_0`, and the round-4 reason is named as not operative. |
| `n3` | **PARTIAL**: (E),(F),(G) added and non-vacuous; (D) still tautological (`n1′`). |

---

## 3. The new mathematics of round 5, re-derived

* **`Π` is automatically primitivizing — correct, and the right idea.**
  `λ_∓(Γ_{Πg}) = ∫(−g''+\tfrac14 g)e^{±s/2}ds`; two integrations by parts move
  `∂_s^2` onto `e^{±s/2}` with **no boundary terms** (`g ∈ C_c^∞`), and
  `∂_s^2e^{±s/2} = \tfrac14e^{±s/2}` gives `−\tfrac14∫ge^{±s/2}+\tfrac14∫ge^{±s/2}
  = 0`.  Sign convention of `λ_∓ = ∫g e^{±s/2}` matches (8bis.9) and Paper 43
  Thm 9.1.  In Fourier, `\hat g_T(τ) = (τ^2+\tfrac14)T\hatφ(Tτ)` with the zeros
  at `τ = ∓i/2` visible.  The builder's refutation of the instruction's
  "two linear conditions" route is **correct**: the Tate functionals are
  unbounded on a concentrating family, and perturbing to kill them destroys the
  concentration.  This is the best single step of round 5.
* **Thm 8bis.4a Steps 1,3,4 — correct.**  `ω̂_fin(0) > 0` strictly (on `𝔠_0`,
  `θ_p = 0`, so every summand is positive); `M_{bulk} ≍ T` by dominated
  convergence on `|σ| ≤ Tδ` (integrand between `(1/4)^2` and `(δ^2+1/4)^2`
  times `|\hatφ|^2`, `→ 1/16` pointwise); `M_{tail} = T·o(T^{−k})` by Schwartz
  decay (`m3′` corrects only the majorant's constant); Step 4 is then
  `c\,M_{bulk} − A_S M_{tail} > 0`.  The concern in my instruction — that
  `\hat h = |\hat g|^2` is not compactly supported, and that the symbol is only
  *bounded*, not decaying — is met by decay against a **bounded** symbol, which
  is legitimate **at a chart**, and the builder says so.
* **Rem 8bis.4b is the honest scope, and I endorse all three clauses.**  (1) is
  right and is the reason the colimit is `OPEN`: `ω̂_fin^∞` is unbounded (indeed
  `+∞` at `τ=0`) and the two scales collide.  (3) is airtight: what is proved is
  that the **left side** of the biconditional is false **at a chart**, while
  (iii) is a **colimit** statement, so no claim about RH follows.  This is the
  single place round 5 could have overreached and did not.
* **Lemma 8bis.6 — correct.**  Existence of `ρ ∈ C_c^∞([−1,1])` with
  `Σ_kρ(x−k) ≡ 1` is standard (normalize a bump by its own periodization);
  `∫ρ = 1` follows.  (8bis.13a) is right (`|x−n| ≤ 2` from `|t−\log n| ≤ gap_n`,
  then `\log(x/n) = \frac{x−n}{n}(1+O(|x−n|/n))` and `gap_n = \frac1n(1+O(1/n))`),
  and the comparison with the **uniform** grid costs
  `‖ρ'‖_∞Σ_{|x−n|≤2}|x−n|O(1/n) = O(e^{−L/2})` over at most five `n`.  Step 2's
  splitting is correct.  The lemma proves the **pointwise** statement it needs,
  and no tested estimate is used: `M3` is fully answered.
* **Thm 8bis.7 Step 2 — correct arithmetic except `m1′`.**  `‖w_1‖_∞ ≍ e^{L/2}`,
  `‖w_2‖_∞ ≍ e^{−L/4}`, `λ_−(w_1) ≍ e^{L}`, `λ_+(w_1) ≍ L`, `λ_−(w_2) ≍ L`,
  `λ_+(w_2) ≍ e^{−L/2}`, `\det ≍ e^{L/2}`, `λ_−(e) = O(1)`,
  `λ_+(e) = O(e^{−3L/4})`, `a = O(e^{−L})` — all re-derived and all right; the
  Lemma 8bis.6 errors `O(e^{−L/2}‖u_i‖_{C^1})` are genuinely of lower order in
  each of the four `λ`'s.  Sup-norm size of the correction: `O(e^{−L/2})` ✓.
* **Cor 8bis.1b′, (C1), (C2), §11, the ledger row, Thm 8.2** — checked above.
  (C1) does **not** change any computed value: for a Gram entry `m/n = q^{±k}`
  forces `q | mn`; and for Thm 8bis.1b the inflation of the smeared idempotent
  to a larger chart makes each new coordinate constant, so the new unit packets
  vanish and `T_∞ = T_S` there.  Both are stated and both are right.

## 4. Renaming test on round-5 material

* **Thm 8bis.4a:** `PASS, WEAKLY`.  Stripped of prose: *a finite sum of
  positive numbers is positive, and a test concentrated at the maximum of a
  continuous bounded symbol sees it; `Π` supplies the two linear constraints for
  free.*  That is a correct and useful negative statement, and it is a genuine
  improvement on the non-sequitur it replaces — but its weight is small, and the
  paper should not let "positivity fails on the pure Frobenius form,
  unconditionally" read as more than "at a finite chart, where the kernel is a
  finite sum of positive-at-zero atoms".  Rem 8bis.4b(1),(2) mostly does this.
* **Lemma 8bis.6:** `PASS`.  A non-uniform Riemann-sum lemma with a partition of
  unity and a slow-variation estimate is not a statement of the explicit
  formula; it is honest analysis and it is correct.
* **Thm 8bis.7:** not a renaming, and not a self-contained theorem either —
  `(Wgr)` carries the analytic content (`n3′`) and Step 3 has a gap (`N3`).
  Correctly quarantined and correctly labelled `CLASSICAL`.
* **Cor 8bis.1b′, (C1), (C2):** `PASS` — bookkeeping made honest, which is what
  they claim to be.

## 5. Independence and the hypothesis-carrying check

Zeros and RH occur only in Thm 8bis.4(ii),(iii) (`CLASSICAL`), Thm 8bis.4(iv),
Thm 8bis.4a/Rem 8bis.4b (which assert nothing about zeros), and §8bis.4
(`CLASSICAL`, imports named).  Deleting §8bis.3–§8bis.4 changes no clause
verdict; Thm 8.2 now says so with the carve-out and §11 lists the three
imports.  **Independence holds, and now the text says what the mathematics
does.**

Hypothesis-carrying (`F3`/`M4`/`M5` failure mode), my own pass over §8bis:
`ε<ε_0` ✓ carried (8bis.1, 8bis.1d, 8bis.1e, 8bis.4(i)); bare/`♭` ✓ carried
(8bis.1, 8bis.1b **in the statement**, 8bis.1b′, 8bis.1d); profile value ✓
carried into (8bis.5); `c_p = \log p` ✓; real-vs-complex ✓ (modulo `m2′`,
`m4′`); colimit `T_∞` ✓ except **Thm 8bis.2** (`N1`), and except that
Lemma 8bis.5's `C^1` hypothesis is stated in the lemma and **not verified at
its second application** (`N3`) — a hypothesis established in one statement and
silently assumed in the next, which is the same failure mode in its purest
form.  **The warning stands for round 6, if there is one: press on the
`C^1`-side of every application of Lemma 8bis.5.**

## 6. Verdict per clause

| clause | round-5 verdict |
|---|---|
| **B.1** | `PROVED` (unchanged). |
| **B.2** | `PROVED`, non-vacuous (Thm 3ter.4(iv), Rem 3ter.4a). |
| **B.3** | `PROVED`, true unit. |
| **B.4** | `REFUTED AS STATED`; `PROVED AS AMENDED` (owner-accepted), on objects in degree (Thm 6bis.4), with the composition law proved (Lemma 6bis.3a) and extended additively (Thm 6bis.3c); the ledger row now matches the text (`M6`(a)). |
| **B.5** | `PROVED`; `Λ(p^k) = \log p` has a uniqueness theorem behind it (Thm 8bis.8, now with the scale quotient). |
| **B.6** | `PROVED`, both halves non-vacuous. |
| **B.7** | `PROVED` as a test; my dissent on the mechanism (`PARTIAL`, Rem 6.5a′) stands and is recorded verbatim beside the lead's ruling.  I accept that procedure as the resolution. |
| **B.8** | `PROVED`; script re-run, all three banners pass; (E),(F),(G) re-derived by hand; (D) vacuous (`n1′`). |
| **B.9** | `PROVED` in substance **and now in the text**: Thm 8.2 carries the carve-out, §11 lists the three imports, and each is marked "used by no clause". |

§8bis is outside the contract; `N1`–`N5` and every minor flip no clause.

## 7. Reservations

* **R1 `DISSOLVED`.**  Unchanged.
* **R2 `DISSOLVED IN DEGREE, ON THE MONOID`** — and the ledger finally agrees
  with the text (`M6`(a)).  Object level `REFUTED`, not open.
* **R3 `DISSOLVED`.**
* **R4 `DISSOLVED`, in the only form available** — a uniqueness theorem given a
  named requirement, now explicitly up to one global scale (`n1`).
* **R5 `ANSWERED IN THE FORM THAT IS TRUE`, and round 5 improves the answer.**
  The false round-3 claim is withdrawn; the true one (Thm 8bis.1e + 8bis.1′) is
  proved; the RH equivalence is `CLASSICAL`, disclaimed as not new, and now
  correctly **quantified** (colimit, false at a chart); and the negative
  statement about the Frobenius form is at last *proved* rather than asserted
  (Thm 8bis.4a), with its scope — chart, not colimit — inside the statement.
  R5 still cannot be "dissolved": it asks for a sign, and the sign is row D's.
* **R6 `DISSOLVED`.**

## 8. Grade

**Row B earns `WEIL-STRENGTH-COMPLETE` on Paper 43's declared carrier**, the
B.4 amendment having been accepted by the owner.

What must be recorded **beside the label**, in the paper and in the ledger:

1. **The carrier and the clause.**  "On Paper 43's declared carrier (§14.0a–b),
   as a theorem about row A's declared trace; **B.4 is `REFUTED AS STATED` and
   `PROVED AS AMENDED`**, the amendment accepted by the owner 2026-09-12; **B.7
   `PROVED` by the lead's ruling, with the auditor's dissent (`PARTIAL`, as a
   mechanism) recorded verbatim beside it.**"
2. **What row B does not deliver.**  "No sign, no positivity, no `𝓝_∞ = 0`, no
   statement about zeros outside Thm 8bis.4(ii)–(iii) and §8bis.4, which are
   `CLASSICAL`, carry the named imports `(Wgr)` and Chebyshev, are used by no
   clause, and are deletable without changing a verdict.  The sign is row D's."
3. **The three quantifiers.**  "The interface with Weil's criterion is a
   **colimit** statement (`T_∞` on `D_A^∞`); at a finite chart it is **false**.
   No divergence **rate** is convention-free; what is stated is that
   `I_A(Frob_n,Frob_n)` does not exist.  Thm 8bis.4a is a **fixed-chart**
   statement; its colimit version is `OPEN`."
4. **§8bis.4 is quarantined and, as of this audit, `NOT PROVED AS WRITTEN`**
   (`N3`), independently of its imports.

**Conditions on the label** (none requires new mathematics; none is a clause):

* **Mandatory before the label is written down:** `N1` (Thm 8bis.2 exempted
  from (C1) — a `PROVED` theorem whose proof contradicts its own section's
  standing convention), `N2` (six dangling equation references, one of them the
  only quantitative hypothesis of Thm 8bis.4a), `N4` and `N5` (the withdrawn
  `M1` argument surviving as the stated reason in §0, the banner and the
  README, and the retracted rate still headlined there).
* **Mandatory before Thm 8bis.7 keeps any label:** `N3`.  Either write the
  `C^1` half of Lemma 8bis.6 (the repair is given above, and it works), or
  demote Thm 8bis.7 to `SKETCH`.
* The minors `m1′`–`m7′` and notes `n1′`–`n3′` are corrections of record.

Round 5 accepted every finding of round 4, including the withdrawal of a
`PROVED` claim it had headlined, and replaced the non-sequitur with a real
theorem; it refuted two of the coordinator's and the lead's own prescriptions
(the `C^1` size of the correction, and the "fix one convention" framing) and
was right both times; and it found two slips neither auditor had found.  The
five `MAJOR`s I record are of a lower order than round 4's: one true theorem
proved under the wrong standing convention, one half-done renumbering, one
missing estimate in a quarantined proof, and two headlines that have not caught
up with their own retraction.  That is a paper being closed, not a paper being
argued with.

**One standing warning for any round 6.**  Four of the five `MAJOR`s
(`N1`, `N2`, `N4`, `N5`) are *the apparatus failing to track the mathematics* —
a convention, a number, a reason and a status block.  Every round of this phase
has had exactly this residue, and each round it is smaller.  It is now small
enough that the next pass should be a **mechanical** one: check every equation
reference resolves, every status block carries its supersession marker, and
every application of Lemma 8bis.5 verifies both of its hypotheses.
