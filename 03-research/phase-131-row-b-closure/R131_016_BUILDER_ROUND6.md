# R131.016 — Builder, round 6: a false import withdrawn, and the converse made conditional

Builder: Claude (Opus 5, 1M). Date: 2026-09-12.
Inputs: `R131_014_AUDIT_ROUND5.md` (hostile: N1–N5, m1′–m7′, n1′–n2′),
`R131_015_LEAD_AUDIT_ROUND5.md` (lead: LF5, LF6), coordinator's round-6
instruction.
Output: Paper 44 `main.md` (§8bis.1–§8bis.4 rewritten in parts; §9bis W23 and
the round-6 block; §10 round-6 block; §0, banner, §11), `README.md`,
`scripts/verify_131_contacts.py` (+2 blocks, one replaced). Numerics: **ALL
CHECKS PASS**, **ROUND-4**, **ROUND-5**, **ROUND-6 CHECKS PASS**.

**Everything mandatory is done.** No clause verdict moves. One `CLASSICAL`
import is withdrawn as **false** (W23) and the theorem that used it is restated
as a conditional transfer theorem whose machinery is proved and whose
arithmetic input is isolated and `OPEN`.

---

## 1. LF5 — the false import (item 1, the most serious)

**Accepted in full, and turned into a proved lemma rather than a retraction
note.** I re-derived the lead's computation before writing anything.

With `ĝ(s) := ∫g(t)e^{(s−1/2)t}dt` and `Q(g) = Σ_ρ ĝ(ρ)conj(ĝ(1−ρ̄))`:

* on-line `ρ = ½+iγ` has `1−ρ̄ = ρ`, contributing `|ĝ(ρ)|² ≥ 0`;
* for `g_L(t) = ψ(t/L)e^{−iγ_0t}` with `ψ ≥ 0`, at `s = ρ_0 = ½+δ+iγ_0` the
  oscillation cancels and `ĝ_L(ρ_0) = ∫ψ(t/L)e^{δt}dt > 0`; at
  `s = 1−ρ̄_0 = ½−δ+iγ_0`, `ĝ_L(1−ρ̄_0) = ∫ψ(t/L)e^{−δt}dt > 0`. **Both are
  positive reals**, so the pair contributes `2ĝ_L(ρ_0)ĝ_L(1−ρ̄_0) > 0`, of size
  `≍ e^{δL}·e^{−δL/2} = e^{δL/2}`;
* **and the failure is structural**: for *any* amplitude `w ≥ 0`,
  `ĝ(ρ_0) = ∫we^{δt} ≥ ∫we^{−δt} = ĝ(1−ρ̄_0) > 0`; for any real tilt
  `w = ψ(t/L)e^{αt}` the two exponents are `α+δ` and `α−δ`, and `α+δ > α−δ`
  always. **No non-negative amplitude and no real tilt can peak the transform
  at `1−ρ̄_0`.** Peaking requires *cancellation*, which is exactly what destroys
  the sup-norm control Step 3 needs.

This is now **Lemma 8bis.6b**, `PROVED` (given only the classical zero-sum
framework already imported as Thm 8bis.4(ii)). `(Wgr)` is **withdrawn**
(§9bis **W23**), removed from §11's import list, and cited nowhere.

**Repair (a)+(b) of the instruction, outcome: the third of the three permitted
outcomes.** Theorem 8bis.7 is restated as a **conditional transfer theorem**:

* **(a) `PROVED`** — if the explicit hypothesis
  **(H_L)**: *a primitive `g_* ∈ C_c^∞([L/2,L];C)` with `Q(g_*) < 0` and
  `R(L) := L e^{−L/4}‖g_*‖_∞‖g_*‖_{C¹}/|Q(g_*)| → 0`*
  holds for arbitrarily large `L`, then positivity **fails** on the
  primitive Dirichlet-polynomial class with per-`n` widths.
* **(b) `CLASSICAL`** — if RH fails, `Q(g) < 0` for some primitive `g`
  (Weil's criterion; Paper 45 Thm 10.4 for the primitive class). *This is the
  true classical statement, and it is all that is classical.*
* **(c) `OPEN`** — whether such a `g` can be taken in a **moving window**
  `[L/2,L]` with `R(L) → 0`. **Not supplied by any classical statement known
  to this paper, and not asserted.**

Hence "positivity on Dirichlet profiles ⟹ RH" is **`OPEN`** and is not
claimed. I attempted the two-frequency route the lead described and record the
obstruction quantitatively in **Rem 8bis.7a(2)**:

* *(α)* the single-frequency route is **provably dead** (Lemma 8bis.6b);
* *(β)* the two-frequency route needs `|B(g_1,g_2)|² > Q(g_1)Q(g_2)` for the
  `2×2` Hermitian block. Two obstacles, both quantified: by 8bis.6b(iv) the
  peaking of `ĝ_2` at `1−ρ̄_0` needs cancellation of order `e^{δL}`, so
  `‖g_2‖_∞` exceeds `|ĝ_2(1−ρ̄_0)|` by a factor no classical statement bounds;
  and `R(L)` is **quadratic** in `g_*`, so a witness carrying a weight `e^{αt}`
  has `‖g_*‖_∞‖g_*‖_{C¹} ≳ e^{2αL}` while the available lower bound on `|Q|`
  is polynomial times `e^{δL}`-type factors — `R(L) → 0` then requires
  `2α < δ + ¼`, which the construction does not deliver. **If a witness with
  `R(L) → 0` is exhibited for all `β`, (a) upgrades the implication to a
  theorem; if only for `|β−½| < θ`, for that range. Neither is claimed.**

Numerics block **(H)** illustrates both halves with a *synthetic* zero
(`β = 0.8`, `γ_0 = 20`, no real zero of `ζ` used): the single-frequency pair
term is **positive** at `L = 20, 40, 60` with log-slope `0.0797 ≤ δ/2 = 0.15`,
nowhere near `2δ = 0.6`; and the two-frequency block on the same quadruple has
`det = Q_1Q_2 − |B|² < 0`, so an optimal `c` makes it negative — with the
printed caveat that the **full** `Q` adds a large positive on-line sum, which
is precisely `(H_L)`.

---

## 2. N3/LF6(b) — the `C¹` gap (item 2)

Accepted: the sentence "the derivative always falls on the smooth factor" is
true of `I(ẽ,g̃)` and **false** of the other cross term, and the naive bounds
`‖ẽ′‖_∞ ≍ e^{L}` would give `O(Le^{L/2})`, **dominating** the main term for
`|β−½| < ¼`.

Repaired by the instruction's two-part route, both parts proved:

* **New Lemma 8bis.6a**: `‖(g_D)′‖_∞ = O(‖g‖_{C¹})`, hence
  `‖(g−g_D)′‖_∞ = O(‖g‖_{C¹})`. Proof: split `g(log n) = g(t) + [g(log n)−g(t)]`;
  the coefficient-variation part is `O(‖g′‖_∞)` (five terms, each
  `≤ ‖g′‖_∞‖ρ′‖_∞`); the mesh part is `g(t)S(t)` with
  `S(t) = Σ_nρ′(a_n)/gap_n`, and **the cancellation `Σ_kρ′(x−k) ≡ 0`** in the
  partition of unity gives `Σ_nρ′(a_n) = O(1/x)` by Taylor, while
  `1/gap_n = x+O(1)`, so `S(t) = O(1)`. Without that cancellation the bound
  would be `e^{L}`; the paper now says so explicitly.
* **Step 3 rewritten** with the expansion
  `I(g̃,g̃) − I(g_D′,g_D′) = I(ẽ,g̃) + I(g̃,ẽ) − I(ẽ,ẽ)` (8bis.13h), in which
  **only `g̃` and `ẽ` occur**; the rough–rough term is bounded with
  `‖ẽ⋆ẽ^†‖_{C¹} ≤ ‖ẽ′‖_∞‖ẽ‖_1 ≤ 2L‖ẽ′‖_∞‖ẽ‖_∞ = O(Le^{−L/2}‖g̃‖²_{C¹})`.
  The total error is (8bis.13i), `O(Le^{−L/4}‖g̃‖_∞‖g̃‖_{C¹}) +
  O(Le^{−L/2}‖g̃‖²_{C¹})` — exactly the ratio `R(L)` of `(H_L)`, so the final
  comparison is now a hypothesis rather than an unverified estimate, and holds
  **for every `β`** for which `(H_L)` holds.

---

## 3. The remaining findings

| finding | disposition |
|---|---|
| **LF6(a)/m1′** | `b = O(e^{−L/4})` (the Cramer term `λ_+(e)λ_−(w_1)/det ≍ e^{−3L/4}e^{L}/e^{L/2}` dominates `Le^{−L/2}`); corrected in (8bis.13e′), and the sup norm `‖bw_2‖_∞ ≍ e^{−L/2}` is **unchanged**, so (8bis.13f) stands |
| **N1** | Thm 8bis.2 now **explicitly exempted** from (C1), in the statement; and the addendum: under `T_∞` the conclusion is *easier* — for `ε < ½log2` the profile meets no atom of `W_fin^∞`, the finite part is **identically zero**, the divergence is purely archimedean and (8bis.8b) is not needed |
| **N2** | the three **displays** are renumbered `(8bis.4b)`, `(8bis.4c)`, `(8bis.8b)`; the double assignments of `(8bis.5)`/`(8bis.7)` are resolved; the six dangling pointers — including Thm 8bis.4a's only quantitative hypothesis — now resolve |
| **N4** | §0's sentence "since the latter's kernel lacks the indefinite `ω̂_∞`" **deleted** (it *is* the withdrawn argument) and the conclusion re-attributed to Thm 8bis.4(iii); the grammatical break fixed; the banner now cites (iii) and Thm 8bis.1e, not (iv) |
| **N5** | README's **round-4** block marked `[SUPERSEDED IN ROUNDS 5–6]` with both retracted sentences named; the two banner rate lines marked `[rate superseded, round 5]` and `[round 6, N1]` |
| **m2′** | (8bis.8c)'s cross term is `2 Im` (**odd**), not `2 Re` (even); proof rewritten with `A(−τ) = conj A(τ)` spelled out |
| **m3′** | majorant `(σ²+1)²`, valid for all `σ` and `T ≥ 1`; the round-5 `σ⁴+1` fails for `|σ| ≳ 1.4` |
| **m4′** | complex→real reduction **carried out**: `λ_∓` have real kernels so primitivity passes to `Re g_D′` and `Im g_D′`; both are Dirichlet-polynomial profiles with the same widths; (8bis.8c) then forces one real summand `> 0`, which is what contradicts a hypothesis quantified over real profiles |
| **m5′** | §9bis `W17`'s live assertion of the withdrawn claim is marked `[SUPERSEDED BY W19; CORRECTED IN ROUND 6]` with the round-6 reading spelled out |
| **m6′** | `Q_fin` is named at its definition (Thm 8bis.4(iv)) and every headline use in §0 now carries that definition |
| **m7′** | Thm 8.2's carve-out sentence de-garbled |
| **n1′** | numerics block (D) replaced: the two local Tate residues are now **computed** from `ζ_p(s) = c_p/(1−p^{−s})` and `ζ_∞(s) = 1/s`, for `c_p = log p` **and** for `c_p = 1`, showing agreement iff `c_p = log p` |
| **n2′** | `A_S = ω̂_fin(0)` **exactly** — recorded where the bound is stated and where Thm 8bis.4a uses it; it explains why the concentration point is the symbol's maximum |

---

## 4. Claims of the round-6 instruction that I refuted or corrected

1. **"the off-line quadruple gives … of sizes `L e^{(β−1/2)L}` and
   `L e^{−(β−1/2)L/2}`" (item 1, and the same in LF5).** The **signs, the
   dominant ends and the exponents are right**; the **polynomial** prefactor is
   **not**. *Counterexample, found by my own numerics (block (H)):* for a
   `C_c^∞` bump `ψ` vanishing to infinite order at the endpoints, Laplace's
   method has a saddle at distance `≍ (δL)^{−1/2}` from the endpoint and
   contributes `e^{−c√(δL)}` — **sub-exponential, not polynomial**. With
   `β = 0.8`, `L = 40 → 60`, the measured log-slope of the pair term is
   `0.0797`, not `δ/2 = 0.15`, precisely because of that factor; it converges to
   `δ/2` only as `L → ∞`. Corrected in Lemma 8bis.6b(ii), where the statement
   now reads "up to sub-exponential factors depending on `ψ`". **Nothing in
   (i)–(iv) depends on it**: the refutation of `(Wgr)` rests on the **sign**
   and on `δ/2` versus `2δ`.

2. **"prove `‖(g − g_D)′‖_∞ = O(e^{−L/2}‖g‖_{C²})` (or at least
   `‖(g_D)′‖_∞ = O(‖g‖_{C¹})`)" (item 2).** The first form is **not what the
   argument gives and is not needed**. The mesh part of `(g_D)′` is
   `g(t)·S(t)` with `S(t) = O(1)` — **not** `O(e^{−L/2})` — because
   `Σ_nρ′(a_n) = O(1/x)` and `1/gap_n ≍ x`, and those two cancel to `O(1)`
   exactly, not better. So `‖(g−g_D)′‖_∞ = O(‖g‖_{C¹})` is the true statement,
   it needs only `C¹` (not `C²`), and it is enough: Step 3 uses `‖ẽ′‖_∞` only
   against the small factor `‖ẽ‖_∞ = O(e^{−L/2}‖g‖_{C¹})`. I proved the second
   (parenthetical) form, which is the correct one.

3. **"`b = O(e^{−L/4})`, not `O(Le^{−L/2})`; sup norm of correction unchanged"
   (item 3).** Accepted and applied — with one addition the instruction omits:
   the **`C¹`** size of the correction also has to be recorded now that Step 3
   uses `‖ẽ′‖_∞`, and it is `O(‖g̃‖_{C¹})` by Lemma 8bis.6a applied to `u_1,u_2`
   with `|a|‖u_1‖_{C¹} ≍ e^{−L/2}` and `|b|‖u_2‖_{C¹} ≍ e^{−L/2}`. Round 5
   would have had a second `C¹` gap here; it is closed in (8bis.13f).

4. **"restate the import as Weil's theorem in its true form — '… there exist,
   for arbitrarily large `L`, primitive complex `g_* ∈ C_c^∞([L/2,L])` with
   `Q(g_*) < 0`' — and give the witness explicitly" (item 1(a)).** The
   **restatement is not classical as displayed**, and I did not import it. What
   *is* classical is Weil's criterion: `¬RH ⟹ ∃g` with `Q(g) < 0`. The
   additional requirements — support in a **moving** window `[L/2,L]` with
   `L → ∞`, and the norm control — are **not** part of any classical statement I
   can name, and supplying "the witness explicitly" is exactly the step that
   does not close (item 1's own third permitted outcome). So (b) imports only
   the true classical statement and (c) records the rest as `OPEN` with the
   obstruction quantified. A weaker import is better than a false one.

---

## 5. The hypothesis-carrying audit, repeated

As in round 5, before reporting I re-read §8bis for the standing failure mode.
New entries this round:

| carried hypothesis | established | now carried into |
|---|---|---|
| fixed chart, `A_S` bounded | (C1) exemption | **Thm 8bis.2 statement** (was missing — `N1`), Cor 8bis.2a, Thm 8bis.4a, Rem 8bis.4b(1) |
| `‖ẽ′‖_∞ = O(‖g̃‖_{C¹})` | Lemma 8bis.6a | Thm 8bis.7 Step 2 (the correction's `C¹` size) and Step 3 (the rough–rough term) |
| `λ_∓` real ⟹ `Re`, `Im` primitive | (8bis.8c), `m4′` | Thm 8bis.7 Step 4 |
| `A_S = ω̂_fin(0)` | (8bis.8b), `n2′` | Thm 8bis.2, Thm 8bis.4a Steps 1 and 4 |

---

## 6. Status

No clause verdict moves; B.1–B.9 stand as in round 4. §8bis is not a clause.
What changed: a **false `CLASSICAL` import is gone**, the theorem that used it
is honest, and the two remaining imports (Weil's criterion, Chebyshev) are both
genuinely classical, both named in §11, both **used by no clause of B.1–B.9**,
and both deletable without changing a verdict.

**The label is not granted and not claimed.** No sign, no positivity, no
`𝓝_∞ = 0`, and no statement about zeros outside the clauses labelled
`CLASSICAL`.

**Where a round 7, if any, should press.** (1) Lemma 8bis.6a's mesh estimate
`S(t) = O(1)` — the cancellation is the whole argument and it is new.
(2) Lemma 8bis.6b(iv): is "no real tilt can peak at `1−ρ̄_0`" stated at the
right generality, i.e. does it cover every amplitude of the form
`w(t) = |w(t)|e^{iθ(t)}` with slowly varying `θ`? (3) Whether `(H_L)`'s ratio
is the *sharp* requirement or an artifact of routing everything through
Lemma 8bis.5's `e^{R/2}`. (4) Whether the numerics' synthetic-zero illustration
in block (H′) could mislead — it is labelled, but it is the one place where a
reader might read a witness into an illustration.
