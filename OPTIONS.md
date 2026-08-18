# Options — where to push next

**Written:** 2026-08-18. **Status:** none of these is executed. This is the
decision document, not a plan for any one of them.

The corpus does **not** reduce entirely to RH. It contains genuinely weaker,
open, non-RH-equivalent targets that were never closed — that correction
matters enough to state before anything else here.

---

## 0. The correction this document exists to record

I had been saying, in different forms, that every live thread in this corpus
terminates at a statement equivalent to RH. That is the dominant pattern, but
it is **not universal**. The audit of phases 34–118 turned up a real exception:
a decomposition of RH into two strictly weaker pieces, neither closed, neither
proved equivalent to RH.

    RH  =  (m < infinity)  AND  (m < infinity  =>  m = 0)

where `m` is the number of off-critical-line zero quadruples. Two independent
pieces, and the corpus never closed either one, and never proved either one is
secretly as hard as RH.

| target | file | why it is strictly weaker | status |
|---|---|---|---|
| **Diana L8** — any unconditional bound `m <= C` | `phase-37-physics/111` | bounds the off-line quadruples without killing them | **OPEN**, verdict "INALCANZABLE" with cataloged techniques — every known zero-density mechanism is *binary* (gives 0 or `T^theta`, never a finite nonzero count) — but **not proved impossible** |
| **"Lemma 108"** — `kappa_W(Q_2) <= C * n_W` for any absolute `C` | `phase-36-ABC-forms/108` §8.1 | **explicitly not RH-equivalent**: allows `m > 0` up to `C/2` | OPEN, tied to conjectural pair-correlation lower-order terms |
| **Conjecture C_B** — finitely many off-line zeros implies none | `phase-34-new-directions/94` §11 | the second half of the decomposition | OPEN, no known bridge from finitude to nullity |
| **C5 ⟹ κ<∞** | `phase-34/91`, `94` | the tail bound is already achievable for large X | OPEN — only the deduction step (an unclosed Krein–Langer argument) is missing |
| **LP-112** — sequential self-approximation of zeta on a fixed compact disc | `phase-37-physics/112`, `113` | would give `m ∈ {0, infinity}`, one of the two pieces above | OPEN, verdict **"SIN PRECEDENTE"** after an exhaustive literature check (Montel, Stepanov, Weyl, Birkhoff — nothing like it exists for any L-function). Its non-equivalence to RH is *asserted, not proved* — downgraded by a later audit (`phase-38/115`) |
| **GAP-157.A** — quantitative discrepancy/irrationality-measure bound on the Kronecker flow `tau -> (p^{i tau})_p` | `phase-49/157`, `158`, `159` | a diophantine input strictly weaker than full recurrence | OPEN, two of three attack routes killed, the core implication neither affirmed nor refuted |
| **Boundary triples for `W_lambda`** | `phase-60/RH-PROOF-PAPER.md` §4.B | classifying self-adjoint extensions at the endpoints | OPEN, **self-labelled "RH-neutral, doable now"**, never attempted |

Every one of these is decidable without deciding RH. None is guaranteed to go
anywhere. That is the candid state of "weaker than RH" in this corpus.

---

## 1. Options that attack row (d) / the missing object directly

### 1a. G-4 — Deninger's rational Witt vectors, the norm and the pairing

**File:** `phase-114-closing-the-four-rows/114_a_03_THE_CANDIDATE_LEDGER.md`.

Deninger, *Rational Witt vectors and associated sheaves* (arXiv 2508.05329),
**Theorem 5.1**: `W_rat(O(X)) ≅ Corr(X,A)` — rational Witt vectors identified
with a ring of **finite algebraic cycles**. Recorded in the corpus as
*BUILT-MODULO-GAP*, the best row-(a) candidate in the whole ledger, with one
named open gap: **G-4, the missing norm and pairing.**

Why it matters: it attacks row (b) — "the `Gamma_n` as cycles, not functionals"
— which `THE_BACKWARD_MAP.md` §3 lists as blocked precisely because nothing
attaches the shell functionals `Gamma_{p,k}` to elements of a divisor group.
This is the one place in the corpus where that attachment is *almost* built by
someone else's theorem, with the missing piece named precisely.

Risk: `107_242` Thm 4.1 already shows the Deninger–Morishita bridge annihilates
the p-adic transverse direction (residue field `F_p-bar` with `mu_(p)` of order
prime to `p`). G-4 needs checking against that obstruction before investing —
it may already be closed by it, or it may survive because 2508.05329 is a
different, newer construction than the one 107_242 tested.

### 1b. Condensed mathematics (Clausen–Scholze) against O1

O1 (`113_10` §5): the divisor group inside `𝒟` is a plain complex vector space,
so the effective cone is scaling-stable and `h^0(nD) = h^0(D)` — no growth,
which kills the classical Riemann–Roch engine.

Condensed abelian groups carry continuous and discrete structure natively —
`Z` is genuinely discrete inside a category that also holds `R`. This is the
most direct candidate for dissolving O1 specifically (as opposed to routing
around it), and it does not appear anywhere in the corpus's 118 phases.

Risk: O1, O2 (infinite mutual intersection of correspondences — the `1/2`
exponent that IS the critical line), and O3 (no spectral gap) were all proved
*inside* `𝒟`. Moving category is not excluded by them, but nothing guarantees
condensed mathematics evades O2 and O3 as well as O1 — they would need
independent checking, not just O1.

### 1c. Quillen K-theory of Spec Z directly

`K_n(Z)` is genuinely discrete with no continuous parameter to begin with — it
might sidestep the "orientation" node of `phase-51/161` Teorema 161.9 (the
canonical orientation of a KK-fundamental class is a Tomita–Takesaki modular
weight whose partition function is literally `zeta(beta)`), since there is no
modular weight to canonically choose. Nothing in the corpus connects `K_*(Z)`
or higher regulators to the inertia invariant `m`. Untried.

### 1d. R16 — does a quadratic Riemann–Roch exist over Spec Z at all?

`THE_BACKWARD_MAP.md` §7 item 3: *"Every Riemann–Roch actually available there
is one-dimensional with a linear `chi`. If none can be quadratic, Ansatz A is
dead and this route with it. A negative answer is as valuable as a positive
one."*

Partial answer already in hand from the audit: Connes–Consani's proved
Riemann–Roch on the scaling site has **real-valued** dimensions,
`chi(D) = deg(D) in R` — not merely non-quadratic, **not even integral**. That
answers R16 negatively *for that specific object*. It does not settle R16 in
general — no scan of the wider arithmetic-geometry literature (arithmetic
surfaces, Arakelov theory over number fields, other F1 candidates) has been
done from inside this corpus. This is a literature question, cheap to attack,
and a clean negative answer would kill Ansatz A permanently and redirect
everything currently aimed at row (d) through Riemann–Roch.

---

## 2. The non-RH-equivalent open sub-targets (§0's table)

Six items, tabulated above. Two look most tractable on their own terms:

- **Boundary triples for `W_lambda`** — the corpus's own self-assessment is
  "doable now," and it has literally never been attempted. Lowest-risk,
  fastest to a decisive answer in either direction, and RH-neutral either way
  — a genuine, if modest, unconditional result either closes or narrows this.
- **LP-112** — highest ceiling (it is half of the `RH = (m<infinity) AND (...)`
  decomposition) but "SIN PRECEDENTE" is a real warning: an exhaustive
  literature search found nothing like it for any L-function, including
  non-arithmetic ones. This is a genuine research problem, not a known
  technique waiting to be applied.

---

## 3. What NOT to do without rework

- **The Davenport–Heilbronn multiplicativity wedge**, as originally proposed
  for phase 119: the underlying thesis — that multiplicativity (the Euler
  product) controls the sign of the localized Weil residual — was **tested
  with reproducible code and refuted** (`phase-60`, no-go **NG-F1**).
  Non-multiplicative smooth controls (`flat`, `loglin`) matched or beat zeta's
  discriminant score. Any DH-wedge argument must be rebuilt on a different
  distinguishing property (row a–c's `deg_det` provenance, not multiplicativity
  per se) or dropped.
- **Any further work on Weil positivity as stated** — proved equivalent to RH
  twice, independently: algebraically (`phase-113`, `(E°) <=> RH`) and
  analytically, verified against real zeta zeros to 10 digits (`phase-118`,
  `<A_T F,F> = sum_rho h(gamma_rho)`). Not a route to RH; it **is** RH.
- **The Gamma–Tate source model** (`phase-117`): `c_N < 1` at every threshold
  tested, decaying, Galerkin-bounded from above — one-sided-robust dead end.

---

## 4. A methodological note, not an option

The discreteness-mechanism hypothesis — every route needs a discrete invariant,
every construction tried is C-linear, zeta re-enters exactly where discreteness
is imposed — is **confirmed as the dominant pattern, not a universal law**
(`AUDIT_A_CATEGORY_CHANGES.md` §2). Real counterexamples exist: `phase-52/163`
Hallazgo 163.2 dies by parity (`2m` is even, its image in `Q/Z` is trivially 0)
*before* zeta ever enters; `107_166` and `114_a_38` die by pure dimension
counting. Whatever gets attempted next, check which failure mode applies before
assuming it is the discreteness one — the corpus has both kinds on record.

---

## Data-quality items found during the audit, worth a cheap pass

- Corrupted publication years in `01-context/RH9/task*` citation blocks (arXiv
  IDs misread as years, e.g. "Jan 2401").
- `phase-29/52` labels a conjectural, unconstructed object "Teorema 2.1
  (Deninger, 1991)" against the corpus's own tagging discipline.
- `phase-60/RH-PROOF-PAPER.md`'s Doob-transform identification claim postdates
  every tribunal verdict in that phase and was never itself reviewed.

---

## Status

None of the above is a proof of RH, a route guaranteed to work, or a claim of
progress. This is an options list, dated 2026-08-18, for deciding where to
spend the next unit of effort. Nothing here has been promoted to any research
phase yet.
