# Phase 25 — lower bounds for b_j: full audit

A systematic survey of every classical and near-classical mechanism that
might force a nontrivial lower bound on the hypothetical off-line
displacement b_j = Re(ρ_j) - 1/2, plus two new structural connections (to
the de Bruijn-Newman constant and to the Laguerre-Pólya/Turán theory), done
without assuming RH or any equivalent.

## Results
- §25-A: fifteen classical mechanisms (Korobov-Vinogradov zero-free region,
  Selberg density theorems, Levinson-Conrey zero-proportion results,
  Deuring-Heilbronn repulsion, and others) are each audited; none produces
  a lower bound on b_j — ten are plain dead ends (wrong direction or
  statistical/proportion statements that say nothing about an individual
  zero), and five are reformulations of the same already-identified wall
  W4-RSRP in different language. **PROVED (negative survey)**.
- Theorem 25-B.4 (de Bruijn-Newman connection): under Hypothesis D (a
  finite off-line defect), the off-line zero ρ_j maps to a complex zero of
  the de Bruijn heat-flow function H₀(t) at γ_j - ib_j, and the
  Rodgers-Tao/Kim-Sirohi de Bruijn-Newman constant Λ satisfies Λ ≳ b_j²/2
  (new quantitative link between the Kreĭn index program, the de
  Bruijn-Newman constant, and b_j). **PROVED** (to leading order, isolated
  zero), noted to give only an *upper* bound on b_j from Λ, not the sought
  lower bound.
- Theorem 25-C.1/Proposition: the polynomial factor P_{4m}(1/2+it) is
  strictly positive on the whole critical line under Hypothesis D, so ξ and
  ξ₀ share the same on-line zeros, and ξ₀ itself lies in the
  Laguerre-Pólya class. **PROVED**.
- Theorem 25-C.6: Wall W4-RSRP is reformulated as a purely algebraic
  question about whether arithmetic constraints on the Taylor coefficients
  of ξ are incompatible with any Laguerre-Pólya × positive-polynomial
  factorization; this reformulation is shown to be circular as an attack
  route (LP membership of ξ itself is already equivalent to RH,
  Csordas-Norfolk-Varga 1988).
- Final wall map: W1 (Weil positivity), W2 (Hilbert-Pólya), W3 (trace
  formula), and the newly surveyed W4-RSRP / W4-LP / W4-dBN are all shown
  to reduce to the same fundamental obstruction — no known mechanism
  propagates arithmetic constraints from Re(s) > 1 into the critical strip.
  Two explicit routes that would break the wall are named: (A) an
  arithmetic-to-analytic propagation theorem, or (B) an unconditional upper
  bound Λ ≤ f(T) → 0. Both are **OPEN**.

## Documents
- `00-setup.md` — mission statement and document map.
- `01-audit-classical.md` — the fifteen-mechanism literature audit.
- `02-deBruijn-Newman.md` — the b_j ↔ de Bruijn-Newman constant Λ
  connection (Theorem 25-B.4).
- `03-krein-lp.md` — Kreĭn-Langer factorization and the Laguerre-Pólya/
  Turán-inequality reformulation (25-C.1–25-C.6).
- `04-verdict.md` — final wall map, the three genuinely new results, and
  the two named routes to break the wall.

## Relation to other phases
Completes the audit opened in phase 24; confirms and extends the Wall
W4-RSRP identified in phases 22-23 by unifying it with the de
Bruijn-Newman and Laguerre-Pólya programs; hands off the two named open
routes (A, B) for any later phase willing to attempt them.
