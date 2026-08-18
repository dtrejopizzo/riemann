# Phase 119 — plan (rev. 2)

Plan only. Nothing executed. Paper 42 untouched.

**Revision note.** Rev. 1 proposed rebuilding the signature decomposition of the
Weil form and combining it with prime-side moments. A corpus search found that
the first half is already done, and better, and that the second half runs into
one of our own recorded no-gos:

- **`04-papers/18-localized-weil-krein-index/`** already proves the signature
  reading — off-line zeros contribute a Lorentzian `u^2-v^2` through an off-axis
  evaluation functional, on-line zeros the nonnegative square `fhat(gamma)^2` —
  and goes further, to the **exact count** `kappa = 2m` via de Branges'
  Pontryagin index theorem, plus three obstruction theorems on what can carry
  `kappa`. It closes by locating the missing ingredient in the
  **pair-correlation regime**.
- **`04-papers/36-obstruction-ledger/main.tex:630`**, no-go
  *"pair correlation carries no off-line signal"*: pair correlation describes
  spacings between on-line zeros and is silent about off-line ones.

So a moment/compression argument can produce an unconditional **lower bound on
the proportion of zeros on the line**, and can say nothing whatever about the
zeros off it. That is a real theorem but it is not a step toward RH, and this
plan no longer pretends otherwise.

Rev. 2 therefore aims at the one input in this programme that is **not** shared
with objects whose RH-analogue is false.

---

## The gate that defines this phase

Any argument built only from a functional equation, an explicit formula, and mean
values of Dirichlet polynomials applies verbatim to the Davenport–Heilbronn
function, whose RH-analogue is **false**. Rows (a)–(c) supply something that is
not on that list:

    Lambda(n) = deg_det L_n

— the coefficients arise as **degrees of determinants of Witt contact complexes**,
not as postulated numbers. Two questions, both decidable:

> **(i)** What property of the coefficients follows from the `deg_det`
> provenance and does *not* follow from the mere existence of an explicit
> formula?
>
> **(ii)** Do the Davenport–Heilbronn coefficients violate it?

A third question, **(iii) does that property force `kappa = 0`?**, is RH. This
phase does not attempt it and will not claim progress on it. (i) and (ii) are
worth settling anyway: they decide whether this programme has a distinguishing
input at all, and that answer has been implicit for a decade without being
written down.

---

## Step 1 — inventory what is already proved (no new mathematics)

Before anything else, read and summarise in one document:
`04-papers/18-localized-weil-krein-index/` (the signature reading, `kappa = 2m`,
the three obstruction theorems), `phase-44/131,132` (the MW walls; `K_off`
Witt-trivial), `phase-51/160,161` (canonical metrics carry zeta),
`phase-52/162` (secondary homotopy inertia; zeta re-enters via the carrier
spectrum), `phase-47/146` (GAP-141.DH, the fat/sub-resolution trichotomy for
Davenport–Heilbronn), `04-papers/36-obstruction-ledger` (all no-gos).

Deliverable: a single page listing, for each recorded obstruction, whether the
`deg_det` input evades it. **Phase 118 spent five agents re-deriving MW-1 because
this step was skipped. Do not skip it.**

---

## Step 2 — question (i): isolate the content of `deg_det`

Make precise what `Lambda(n) = deg_det L_n` asserts beyond the numerical values.
Candidates to examine, in order of how load-bearing they look:

- **Integrality.** `deg_det` is a degree, hence an integer; `Lambda(p^k) = log p`
  says the *multiplicity* is an integer. In the function-field case integrality
  is load-bearing — Weil's proof uses that the trace of Frobenius is an integer,
  and Montgomery-type arguments use integrality of multiplicities (`m^2 >= 2m-1`).
  This is the leading candidate.
- **Support.** The coefficients are supported exactly on prime powers, with the
  support being the closed points of a scheme rather than an accident.
- **Functoriality.** `deg_det` is a degree of a determinant of a complex, so it
  is additive in distinguished triangles and multiplicative in composition. Are
  there relations among the `L_n` (composition, Künneth) that force relations
  among the `Lambda(n)` beyond `Lambda = -zeta'/zeta` coefficients?
- **Effectivity.** Contact complexes have effective classes; effectivity is an
  inequality, not an identity, and inequalities are what positivity arguments eat.

Deliverable: an explicit, checkable statement `P` — "the coefficient sequence
satisfies `P`" — that follows from the `deg_det` construction. State it as a
property of a *sequence*, so that it can be tested on other sequences.

---

## Step 3 — question (ii): test `P` against Davenport–Heilbronn

Build the Davenport–Heilbronn analogue of `A_T` and of the coefficient data, and
check whether `P` holds for it.

Note the identity of phase 118 will hold for DH too — same explicit-formula
structure — so the test is *not* about the identity. It is about `P`.

Three outcomes:

- **`P` fails for DH.** Then this programme has a genuine distinguishing input,
  and the whole corpus reorganises around making `P` load-bearing. This is the
  only outcome that bears on RH.
- **`P` holds for DH.** Then `P` is not a wedge; return to Step 2 with the next
  candidate. Record the failure in the obstruction ledger.
- **No `P` survives Step 2 at all.** Then the programme is subject to the DH
  ceiling permanently, and its candid scope is unconditional zero counting. That
  belongs in the ledger beside the scalar no-go, `c_N < 1`, and MW-1.

Existing starting points: `04-papers/04-davenport-heilbronn-null/` and
`phase-47/146` (which already asked whether DH's off-line zeros are fat or
sub-resolution).

---

## Step 4 — the counting result, as a by-product only

Independently of Steps 2–3, the compression machinery yields an unconditional
lower bound on the proportion of zeros on the critical line: signature reading
(already proved, paper 18) + prime-side moments `tr Gtilde`, `||Gtilde||_F^2`
(computable from the explicit formula, no knowledge of zero locations) +
rank/trace inequalities.

Do this **only after** Steps 2–3, and only if cheap. It is worth having as a
certified artifact produced by our own assembly, and worth nothing as an
argument about RH — by our own `ng:paircorr`, it is silent about off-line zeros.

Prerequisite if attempted: settle the two-route assembly discrepancy left open by
phase 118 (`phase-118/PROOF_ARCHITECTURE.md` §2, "UNRESOLVED"). If the bug is in
`rowd_assembly` rather than in the cross-validation script, phase 117's `c_N`
conclusions inherit it and must be re-audited.

Known ceiling, recorded so nobody spends against it: two-moment methods with
band-limit `<= 1` are bounded; passing them needs prime-pair information of
Hardy–Littlewood strength.

---

## Stop conditions

- Step 2 yields no candidate `P` → close the phase, record the DH ceiling.
- Step 3 shows every `P` holds for DH → same.
- Step 3 shows some `P` fails for DH → stop everything else and pursue it; that
  is the first genuinely new arithmetic input the programme has produced.

## What this phase will not do

Claim progress toward RH from moment or compression methods. Attempt (iii).
Promote any status. Modify paper 42.
