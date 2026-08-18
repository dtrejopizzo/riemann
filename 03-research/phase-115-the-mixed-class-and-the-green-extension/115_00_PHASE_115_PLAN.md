# Phase 115 — The mixed class and the Green extension

**Opened:** 2026-08-08, from `phase-114/PHASE_114_CLOSURE.md`.

Row (d) is not missing an inequality.  It is missing an **object**.  This phase
builds it, or proves it cannot exist.

## The target

For each \(f\in\mathcal T^0\), a perfect object
\(\mathbf M_f\in\mathrm{Perf}_{IDN}(\mathscr Y_{\mathbb S})\) with:

1. reduced derived contact with \(\Delta\) reproducing the row-(b) family with
   weights \(\Lambda(n)/\sqrt n\), **in the cross form \(C_\Lambda\), not the
   self form \(K_S\)** (`115_01` §3);
2. intrinsic periodic cohomology with
   \(\dim\mathbf H^{\rm int}_t(\mathbf M_f)\sim t^2\cdot\frac12B_{\rm nuc}(f,f)\);
3. normalized determinant with metric exponent \(B_{\rm nuc}(f,f)\);
4. effectivity = the cone of `prop:externaleffectivity`.

Then `thm:mixedsectionforcing` gives row (d).

Axiom 4 of that theorem is **already proved** on the ruled cone:
`cor:cotangentRRdimension` gives \(t^2ab=\frac12t^2q(D,D)\).

## Why this is allowed

* `main.tex` §1 requires it: *"Row (d) must come from a Riemann–Roch theorem on
  the square, or not at all."*  Every other import route is closed
  (`phase-5/B3.2`, `main.tex` §1, `113_11`).
* `113_11`'s obstruction O1 does **not** apply: it is a category error *inside*
  \(\mathcal D\), where divisors and sections are the same type.  In row (a)
  they are not — \(\mathcal L(D,E)\) and \(\mathbf H^{\rm int}\) are different
  objects, and the divisor map is invariant under scaling the section.
  `113_11` says so itself (condition R10, and "it does not prove that no
  \(h^0\) exists anywhere").
* `113_11` §5's own redirection points here: the section functor should live on
  *a module of integral divisors on prime powers*, not a subspace of
  \(\mathcal D\) — which is \(\mathcal N_{DN}\) over \(\mathcal C_{\mathbb R}\).

## What `115_01` already established

\[
 M(C_\Lambda)=\mathrm{diag}(\ell),\quad
 M(B_{\rm int})=\ell\ell^{\!\top},\quad
 M(G)=\ell\ell^{\!\top}-\mathrm{diag}(\ell),
 \qquad \ell_p=\log p,
\]

so row (a)'s Green term is a **rank cut \(r\to1\)** — literally "couples
distinct primes while preserving their local contact".  And on its primitive
space row (a) attains \(B=0\) exactly.  **Row (a) is row (d)'s equality case.**

Working hypothesis: \(d\Psi-dx\) is the *centred degree vector* of the mixed
classes, and the row-(d) Green term is its outer square minus the local
contact.

## Execution

### Step 1 — the centred degree vector

Make the hypothesis precise.  Row (a): \(d_i(x)=\ell^{\!\top}x_i\), and
\(M(B_{\rm int})=\ell\ell^{\!\top}\).  On prime powers \(v_n=\Lambda(n)/\sqrt n\)
is not summable; the two Tate conditions remove the divergence and leave
\(dA=d\Psi-dx\).

Deliverable: the exact statement of \(v\) on mixed classes, with the
regularization carried explicitly, and the outer square \(vv^{\!\top}\) written
as an operator on \(\mathcal T^0\).

**Falsifier.** The resulting Green term must reproduce `thm:forcedgreen`'s
\(G_\infty\) — which row (c) pins *exactly*, with no freedom
(`eq:archmultiplier`, \(m_\infty(\tau)=\log\pi-\mathrm{Re}\,\psi(\frac14+i\frac\tau2)\)).
If the outer square does not give that multiplier, the hypothesis is dead and
the phase says so.

This is the sharpest possible test: one side is forced by row (c), the other is
constructed from row (a), and they were built independently.

### Step 2 — the object

Only if Step 1 survives.  Build \(\mathbf M_f\) in
\(\mathrm{Perf}_{IDN}\) with clauses 1–4.  Clause 2 is where
`thm:infiniterankcontact` is waiting.

### Step 3 — where it is allowed to live

`thm:infiniterankcontact` forbids \(\mathbf M_f\) factoring through
\(N^1_{\rm rul}\).  It does not forbid the object.  Read positively: the
mixed classes must land where \(B_{\rm int}\)'s radical (dimension \(2r-2\),
and it grows with \(r\)) becomes **genuine negative directions**.

The naive contact opens that radical into \(r\) **positive** directions
(`thm:finitecontactobstruction`).  The cross form opens it into hyperbolic
pairs.  The requirement is that the deformation opens it **downwards**.

That is the precise form of the bet, and the precise place it can break.

## Standing rules

**Method rule (D.263).** Before building any candidate, state which theorem of
`main.tex` §`sec:rowdgate` forbids its naive version and what feature escapes
it.  **Check the ledger first.**

**No local constructions.** No finite-rank, per-prime, or separately-budgeted
candidate.  `thm:infiniterankcontact` forbids the whole family, and phase 114
spent seventy notes rediscovering that.

**F2 — arithmetic discrimination.** Any mechanism that also works on the
off-line Beurling surrogate cannot close row D.

**Numerics are diagnostic only.** D.198 records a spurious negative eigenvalue
produced by floating point. Anything rigorous is redone in interval arithmetic.

## What ends this phase

* Step 1's falsifier fires → the hypothesis is dead, recorded, phase closes
  with a sharper no-go than it opened with;
* Step 1 survives and \(\mathbf M_f\) is built → row (d) reduces to the
  remaining clauses of `thm:mixedsectionforcing`;
* Step 1 survives and the object provably cannot exist in
  \(\mathrm{Perf}_{IDN}\) → the Riemann–Roch route named in `main.tex` §1
  is closed, which is a result about the whole programme.

## Index of notes, and where the phase actually went

| note | content | verdict |
|---|---|---|
| `115_01` | Green term is a rank cut \(r\to1\); \(M(G)=\ell\ell^\top-\mathrm{diag}\,\ell\) | proved |
| `115_02` | architecture of row (d), 7 design decisions | — |
| `115_03` | literature against the blueprint | — |
| `115_04` | theta construction on row (a)'s lattices; two-term RR exact | proved |
| `115_05` | closed form \(\widehat h^0=c\,d_{1+}d_{2+}\); axioms 1, 2 | proved |
| `115_06` | \(h^2=0\), \(h^1=h^\vee\); axioms 3, 4 on the ruling sector | proved |
| `115_07` | the mixed lattice cannot come from the code | proved (no-go) |
| `115_08` | sign dictionary; **slack lemma**; two lossless identities; window \(=\{K=0\}\); **archimedean no-go** | proved |
| `115_09` | semi-local reduction to \(E_S\le0\); shell decomposition | reduction proved, (H) open |
| `115_10` | literature: window unmoved 6 years; three independent confirmations | — |

Scripts in `scripts/`, all reproducible:
`115_08_explicit_formula_sign_fit.py` (fits the explicit-formula coefficients to
\((+1,-1,+1,-1)\) exactly), `115_08_cc_unconditional_positivity.py`,
`115_08_prime_free_window_crosscheck.py` (+ `.out`).

**The phase did not go where this plan expected.**  Step 1's falsifier was never
reached, because `115_08` proved something that makes the whole family of
approaches — including this plan's Step 1 — inadmissible:

> **Slack lemma.**  If \(-G_\infty\ge\mathcal A\) with slack
> \(\sigma=-G_\infty-\mathcal A\ge0\), then
> \(\mathcal A-K=-B_{\rm nuc}-\sigma\).  So "\(\mathcal A\ge K\)" is row (d)
> *plus* \(\sigma\), never a reduction of it.

Since every functional built from the scaling action and the \(\Lambda=1\)
cutoff — \(\mathcal S\), \(E\), \(L\), \(D\), and any nonnegative combination —
is such an \(\mathcal A\), **no single-place construction proves row (d)**
(`115_08` Corollary 7).  The one escape is a cutoff that itself sees the primes,
i.e. the semi-local Sonin projection \(\mathbf S_S\) (`115_09`).  That space
exists in the literature (CCM arXiv:2310.18423 Theorem 4.6); the positivity does
not, and its authors call it a strategy rather than a theorem.

Recorded in Connes' own words (arXiv:2602.04022, Feb 2026, verified locally):
the window *"is the simple case when no primes are involved"*, and the
compression result still holds only on \([2^{-1/2},2^{1/2}]\).

## Off the critical path

The \(T=\frac12\log5\) / \(\frac12\log6\) certificate mismatch, and the interval
track paused at D.227 (both `phase-114/PHASE_114_CLOSURE.md`).

Not to be modified without an explicit decision:
`04-papers/42-arithmetic-lefschetz-programme`.

Row D: **OPEN**.
