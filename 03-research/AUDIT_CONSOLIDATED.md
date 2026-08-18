# Consolidated audit — what 118 phases say is closed, open, and untried

Written 2026-08-18. Consolidates the surviving probe reports. Companion to
`THE_BACKWARD_MAP.md` (which covers rows a–d and requirements d0–d5) and
`AUDIT_A_CATEGORY_CHANGES.md` (category-change attempts, on disk in full).

Several probes were killed by a session limit before writing their files; their
findings are recorded here from their returned summaries and are marked
**[from probe summary, file not written]**. Those need re-verification against
source before being relied on.

---

## 1. The discreteness hypothesis: confirmed as dominant, NOT universal

The hypothesis — *every route needs a discrete invariant; the constructions are
C-linear; zeta re-enters exactly where discreteness is imposed* — was tested
against the inventory.

**Confirmed, with two near-formal proofs:**

- **Doc 132, Prop. A.4** — in the Grothendieck ring of the category `Pol_delta`,
  the *only* character-valued invariants are dimension and reduced signature.
  The defect `delta` is provably **not a character**, i.e. not obtainable from
  any C-linear multiplicative structure. This is close to a formal proof of the
  hypothesis for a whole family.
- **Doc 161, Teorema 161.9** — the cleanest instance. The KK-theoretic
  fundamental class is RH-free and topological. The only canonical way to turn it
  into a *signed* invariant is to orient it, and the canonical orientation is a
  Tomita–Takesaki modular weight whose partition function is literally
  `zeta(beta)`. Discreteness is imposed exactly at the orientation step, and zeta
  is exactly what supplies it.
- **Doc 156** — the index does not exist as an object until Fredholmness is
  granted, and Fredholmness **is** `m < infinity`. Gated from the start.

**Genuine counterexamples — failures with nothing to do with zeta:**

- **Doc 163, Hallazgo 163.2 (parity).** `2m` is an even integer, so its image in
  the secondary receptor `Q/Z` is trivially `0`. The construction dies from group
  theory *before* any zeta-dependent step. Discreteness was achieved; the
  receiving structure could not represent it.
- **`107_166`** (topos amplitude) and **`114_a_38`** (diagonal collapse) — pure
  dimension-counting and universal-property failures. The category is the wrong
  shape before any invariant-reading step exists.
- **Phase 15 (prismatic)** — computes the wrong side of the explicit-formula
  duality: local Satake data, not the global zeros.

**Net.** The mechanism is real and dominant for routes that reach the
invariant-reading stage, and it is not universal. Some routes die earlier, on
category-shape grounds.

## 2. Open items that are NOT RH-equivalent

This is the most decision-relevant section, and it corrects the impression that
everything reduces to RH. **[from probe summaries, files not written]**

| item | statement | source | status |
|---|---|---|---|
| **Diana L8** | any unconditional bound `m <= C` on off-critical quadruples | `phase-37-physics/111` | OPEN, genuinely intermediate. Verdict "DIANA INALCANZABLE" with catalogued techniques, but **not proved impossible**. Known zero-density mechanisms are shown *binary* — they give 0 or `T^theta`, never a finite nonzero uniform count |
| **"Lema 108"** | `kappa_W(Q_2) <= C n_W` for any absolute `C` | `phase-36-ABC-forms/108` §8.1 | OPEN, **explicitly not RH-equivalent** (allows `m>0` up to `C/2`). Tied to conjectural pair-correlation lower-order terms |
| **Conjecture C_B** | finitely many off-critical zeros implies none | `phase-34-new-directions/94` §11 | OPEN, genuine. No argument in the literature bridges finitude to nullity |
| **C5 ⟹ κ<∞** | `a_tail(X) < 1` giving `kappa(Q) < infinity` | `phase-34-new-directions/91`, `94` | OPEN. Tail bound achievable for large `X`; the *deduction* step needs an unclosed Krein–Langer argument |
| **LP-112** | sequential self-approximation of zeta on a fixed compact disc | `phase-37-physics/112`, `113` | OPEN, verdict **SIN PRECEDENTE** after an exhaustive literature survey. Non-RH-equivalence is *asserted, not proved* (downgraded by the `115` audit) |
| **GAP-157.A** | quantitative discrepancy / irrationality-measure bound on the Kronecker flow `tau -> (p^{i tau})_p` | `phase-49/157`, `158`, `159` | OPEN. Two of three attack routes killed; the core implication is undecided, neither affirmed nor refuted |
| **boundary triples for `W_lambda`** | classify Fourier-invariant self-adjoint extensions; is `B_CCM` unique? | `phase-60/RH-PROOF-PAPER.md` §4.B | OPEN, self-labelled **"RH-neutral, doable now"**, never attempted |

`RH = (m < infinity) AND (m < infinity => m = 0)` is a decomposition into two
strictly weaker pieces. The corpus has closed neither, and has proved neither
equivalent to RH.

## 3. What the two rival programmes actually have

**[from probe summaries, files not written — re-verify before relying]**

**Connes–Consani.**
- The scaling site's proved Riemann–Roch has **real-valued** dimensions:
  `chi(D) = deg(D)` in `R`, not `Z`. So it is not merely non-quadratic — it is
  not integral either. *(This is the corpus's own inference from CC's theorem,
  not a CC claim; flagged for checking.)* It answers requirement **R16**
  negatively for this object.
- CC state themselves that no good `H^j` (`j != 0`) exists on the scaling site,
  and that the **self-intersection of the diagonal is unsolved**.
- CC's positivity in *The Weil proof and the geometry of the adèles class space*
  is explicitly **RH-equivalent**, not an independent Hodge index — the same wall.
- Genuine success: CC's archimedean distribution reproduces the `Psi(r)`/Gamma
  term of Weil's formula **exactly**.
- No CC or Borger construction supplies `H*(Spec Z x_{F1} Spec Z)`, a diagonal
  class, or a Hodge–Riemann form.

**Deninger.**
- Deninger–Singhof needs a **Kähler–Riemann foliation**; the space `X_K` as
  actually built has leaves of complex dimension **0**, so the hypothesis "fails
  literally" (`phase-43/129`). Double mismatch: dimension and nature.
- `phase-51/160`: the foliated cohomology of the Kronecker foliation computes the
  spectrum of the **integers** `{log k}`, not the zeros. Recorded there as the
  reason the programme has been open ~30 years.
- **The best row-(a) candidate in the whole ledger** is Deninger's *Rational Witt
  vectors and associated sheaves* (arXiv 2508.05329), **Theorem 5.1**:
  `W_rat(O(X)) ~= Corr(X,A)` — rational Witt vectors identified with a ring of
  **finite algebraic cycles**. Recorded as *BUILT-MODULO-GAP* in
  `phase-114/114_a_03`, open gap **G-4: missing norm and pairing**. This bears
  directly on row (b)'s "`Gamma_n` as cycles".

## 4. Two results that cut against previously-favoured ideas

- **The multiplicativity thesis was tested and refuted.** `phase-60/RESULTS.md`
  no-go **NG-F1**: the hypothesis that the sign of the localized Weil residual is
  controlled by the Euler product was tested with reproducible code, and
  non-multiplicative smooth controls (`flat`, `loglin`) **matched or beat** zeta's
  discriminant score. This is a direct hit on any plan resting on "multiplicativity
  distinguishes zeta", including the Davenport–Heilbronn wedge proposed for
  phase 119.
- **`W_lambda >= 0` was refuted.** `phase-38/114`: `int W_lambda dm_inf = 0`
  exactly, so the claimed non-negativity (used as proven across phases 34–37) is
  false, traced to a sign flip, a missing Abel boundary term, and a wrong
  arithmetic identity. Downstream citations in 34–37 rest on a retracted result.

## 5. The strongest positive result in the corpus, and what blocks it

`phase-61`/`62`/`63` (scripts `E48`, `E51`, `E93`, `E94`, `E99`), built on
Deninger arXiv 2204.02714 Props 2.5/2.7/2.13 (quaternionic `*` with `*^2 = -1`,
pairing `<h,h'> = tr(h u *h')`):

**Positive.** The finite-window Weil matrix `A_lambda` is genuinely positive
semidefinite on the `+i`-eigenspace of `J` for real zeta zeros, while random and
planted-falsifier controls come out indefinite. The corpus calls this *"the
clearest intrinsic appearance of Weil/Hodge–Riemann positivity we have
produced."*

**Blocked, and the reason is sharp (MW-5, `R3-VERDICT`, `E99`).** No `J`-linear
Frobenius isometry of a **gapped** polarization exists on any finite window,
because zeta has infinitely many zeros — *infinite genus*. Closing it needs an
candidly infinite-dimensional realization with **regularized** positivity, which
the corpus states is a theory problem beyond numerics.

## 6. Category changes never attempted

From `AUDIT_A_CATEGORY_CHANGES.md` §3. Ranked by how directly each attacks O1
(`D` is a plain C-vector space with no compatible discrete structure).

1. **Condensed mathematics (Clausen–Scholze).** O1 is *precisely* a statement
   about `D` being a plain C-vector space. Condensed abelian groups carry
   continuous and discrete structure natively — `Z` is genuinely discrete inside
   a category that also holds `R`. The most direct candidate for dissolving O1,
   and untried anywhere in the corpus.
2. **Quillen K-theory of `Spec Z` directly** (`K_n(Z)`), as opposed to Connes'
   analytic KK-theory of a crossed product. Genuinely discrete with no continuous
   parameter, so it may sidestep the orientation node of Teorema 161.9 — there is
   no modular weight to choose. Nothing in the corpus connects `K_*(Z)` or higher
   regulators to `m`.
3. **The named central gap**: a triple spectral object whose Chern character gives
   `kappa` **without its zeta spectral function being zeta** (`156` §4.5, `161`
   §5.3). The sharpest named-but-unattempted target in the corpus.
4. Equivariant `RO(G)`-graded stable homotopy for the Klein-four symmetry;
   Berkovich geometry over `Spec Z`; motivic `A^1`-homotopy; cluster categories;
   Floer refinements beyond the bare Maslov index.

## 7. Data-quality flags found during the audit

- Citation blocks across `01-context/RH9/task*` show **corrupted years** — arXiv
  IDs misread as publication years ("Jan 2401", "Jun 2501", "Sep 2504").
  Metadata bug, not mathematics, but it misleads.
- `phase-29/52` labels a box **"Teorema 2.1 (Deninger, 1991)"** for what the
  surrounding prose correctly calls conjectural and unconstructed. Mislabelled
  against the corpus's own tagging discipline.
- `phase-60`'s `RH-PROOF-PAPER.md` (2026-07-17) claims the limit operator is
  "now identified (Doob transform)". It postdates every tribunal verdict in the
  phase and **was never itself submitted to review** — unaudited.
- `task63`'s "Type-II dimension obstruction theorem" is the probe's own inference
  layered on CC's real theorem, not a CC quotation. Check its premises.

## 8. Status

RH is not proved. Row (d) is not closed. Nothing here promotes any status. The
strongest unconditional theorem in the corpus remains `A_T >= 0` for
`0 < T <= log 2`.
