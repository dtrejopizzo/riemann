# Phase 114 — Closure

**Closed:** 2026-08-08.  No successor phase opened.

## What this phase set out to do

Close the four rows of the arithmetic Lefschetz programme (paper 42).  Rows
(a), (b) and (c) were completed and written up.  The phase then concentrated
entirely on row (d): prove, without zeros, RH, or the sign of the Weil form
as input,

```text
B_nuc(f,f) <= 0    for all f in T^0.
```

## What it achieved

**Rows (a)--(c): complete and published**, in the stated categories, in
`04-papers/42-arithmetic-lefschetz-programme`.  Each follows the same
method — prove a no-go about the naive object, then build the forced
replacement once, in an infinite but tame category, on an imported engine
(Connes--Consani, Haran, Meyer).

**Row (d): reduced, not closed.**  The genuine reductions, in order:

1. **Sharp Douglas gate** (D.170, `ROW_D_SHARP_DOUGLAS.md`): row D is
   equivalent, over an exhaustive family of prime-power births, to
   \(y_N=D_{{\rm out},N}^{1/2}v_N\) with \(\|v_N\|\le1\).
2. **Exact operator Green identity and defect-difference identity**
   (D.210, D.211, D.214).
3. **The D.172 correction** (D.200): a real gap in the three-block Feshbach
   endpoint template — a dropped safe-block/tail coupling — found, proved
   non-cosmetic by scalar counterexample, and fixed.  The paper's
   \(T=\frac12\log5\) certificate was correspondingly demoted in
   `row-d-local-analysis.tex` to separate rigorous statements which "do not
   yet prove positivity of the complete primitive space at this endpoint".
4. **Identification of the unpaid channel** (D.260): it is the
   Mellin--Stieltjes transform of \(d\Psi-dx\), equivalently of
   \(A(x)=\Psi(x)-x+1\).  This is the first time the residual object has a
   name outside this programme.
5. **The joint regularized residual** (D.261, D.262):
   \[
    \mathscr R_{N,\varepsilon}
    =\mathcal M_N-\mathfrak q_N^*(D_N+\varepsilon I)^{-1}\mathfrak q_N,
   \]
   an exact identity with a monotone \(\varepsilon\downarrow0\) limit, where
   \(\mathfrak q_N\) jointly carries every prime power via \(d\Psi-dx\), the
   complete Gamma term, support compression and the two Tate jets.
6. **One unconditional side result** (D.244): exact inertia \((1,|S|-1)\)
   for the finite prime tangent Hodge form.  Proved; not usable for row D
   (D.258--D.259); worth extracting separately.

## Candid self-assessment (why the phase closes here)

D.263 audits the terminal state and finds that the campaign D.191--D.262
ended on **two obstructions already proved in the paper before the campaign
began**:

* **A.** Infinite rank is not removed by two Tate equations.  Paper:
  `thm:infiniterankcontact` + `cor:primitiveinfiniterank`.  Campaign:
  D.195--D.197, D.258, D.259.  The paper's version is strictly stronger (it
  uses the prime atoms); the campaign's are softer instances applied one per
  candidate port.
* **B.** The archimedean multiplier is indefinite.  Paper: the text
  following `eq:archenergy` — \(m_\infty(0)=\log\pi-\psi(1/4)>0\),
  \(m_\infty(\tau)\to-\infty\), "\(G_\infty\) is indefinite", "the local
  energy does not close row (d)".  Campaign: D.262 §3, same function, same
  values, same conclusion, two days later.  This correspondence is verbatim,
  not merely structural.

The cause is the unit of work.  The campaign's unit was a candidate *local*
construction, so a verdict that `thm:infiniterankcontact` had already
delivered for the whole family had to be re-derived once per candidate.
Roughly seventy notes recovered it candidate by candidate.  From D.214 and
D.260 the terminal object was reachable directly; D.241--D.259 lie off that
path.

Per the reduce-don't-rewrite rule, the phase closes at its sharpest
formulation, and — more importantly — the **method** changes: rows (a)--(c)
never enumerated finite local candidates, and row (d) will not either.

## Loose ends carried forward

* **The log5/log6 mismatch.**  `ROW_D_EXECUTION_PLAN_AFTER_REFEREES.md`
  Phase 7 lists "the pending \(T=\frac12\log5\) corrected joint Schur
  certificate", but essentially all deep interval work in this phase
  (D.198--D.227) targets \(T=\frac12\log6\), and no note back-ports the
  corrected Feshbach machinery to log5.  Two unfinished finite certificates
  now exist — log5 in the paper, log6 in phase 114 — with no documented
  plan to reconcile them.  This must be settled explicitly before any
  finite-remainder work resumes.  It is not on the critical path.
* **The interval track paused, it did not fail.**  D.227 stopped the log6
  campaign by methodological decision (FFT band calibration), not by a hard
  obstruction.  D.222's exact-Green calculation worked and reached within
  0.09 of the budget; the natural resumption is that calculation at a larger
  native-Arb band.  Resumable, not on the critical path.
* **D.244 extraction.**  Unconditional, self-contained, dead-ended for row D
  for a subtle reason (finite rank in prime-index space is not finite rank
  as a Hilbert operator after Fourier realization).

## Method rule adopted

> Before constructing any candidate for row D, state which theorem of
> `main.tex` §`sec:rowdgate` forbids the naive version of that candidate,
> and what feature of the candidate escapes it.  A candidate that cannot
> answer this is not built.

Corollary: no finite-rank, per-prime, or separately-budgeted local
construction will be attempted again.

## Endpoint as it stands

```text
PROVED:   row D  <=>  sharp Douglas gate (G)  [D.170]
IDENTITY: R_{N,eps} = M_N - q_N* (D_N + eps I)^{-1} q_N,
          exact, monotone as eps -> 0            [D.262 (4.2)-(4.4)]
          q_N carries: dPsi - dx, the full Gamma term,
          support compression, the two Tate jets [D.260, D.261]

OPEN (the minimal load-bearing theorem):
          construct Z_{N,eps}, without pseudoinverses and without
          assuming RH, such that R_{N,eps} = Z_{N,eps}* Z_{N,eps}.
```

No successor phase is opened here.  Note for whoever picks this up: the
de Branges / canonical-systems route was already audited and deprioritized in
`phase-5-structural/B3.2-de-branges-comparison.md` (certificate \(\iff\) RH;
Conrey--Li), `main.tex` §1 excludes explicit-formula equivalences by design,
and `phase-113/113_11` closed the imported-\(h^0\) route in both directions.
Check those three before proposing an import.

Row D: **OPEN**.
