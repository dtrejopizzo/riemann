# Program Map — From the Survey to the Reduction

A single picture of where the program has been and where it stands now. Read top to bottom.
This map trades the day-by-day working log for the logical structure: what was tried, what
survived, what failed and why, and where the difficulty currently lives. For phase-by-phase
detail, see [`03-research/README.md`](03-research/README.md) and
[`COMPLETE-PROGRAM-SUMMARY.md`](COMPLETE-PROGRAM-SUMMARY.md); for every dead end by name, see
[`NO-GO-LIST.md`](NO-GO-LIST.md).

**If you read nothing else, read Part 12.** It states the program's current final result: a
fifteen-step reduction of RH to one classical, named inequality (Li–Keiper positivity), with
fourteen of the fifteen steps proved.

---

## Part 1 — The road traveled: from the survey to the named wall

```
                          +-----------------------------------------------+
                          |  01 - SURVEY "The Critical Line"               |
                          |  Thesis: every front reduces to POSITIVITY     |
                          +----------------------+--------------------------+
                                                 |
                  +-------------------------------+-------------------------------+
                  |   ARC A -- the omega-class / resonance program                |
                  |                                                               |
                  |   02 -- omega-class reduction:  B(N) <= N^eps => Lindelof     |
                  |   |      (sufficient, plausibly stronger than LH)            |
                  |   v                                                          |
                  |   04 -- DH null result:  no power-law growth                 |
                  |   |      => onset bound  N* >~ 10^14                         |
                  |   v                                                          |
                  |   (folded into 02) -- phenomenology: coefficient             |
                  |   |   architecture is the discriminant; Liouville parity     |
                  |   v                                                          |
                  |   (folded into 02) -- omega-geometry at peaks                |
                  |            |                                                 |
                  |   pre-canonical SIGN artifacts found -------------------+    |
                  +----------------------------------------------------------+    |
                                                 |                              |
                                                 v                              |
                          +-----------------------------------------------+    |
                          |  03 - SIGN RECONCILIATION                      |<---+
                          |  r is conditioning-dependent (peaks positive,  |
                          |  troughs negative, mean zero). Cleans 02, 04.  |
                          +----------------------+--------------------------+
                                                 |  (02's "phase transition" refuted,
                                                 |   reframed honestly)
                                                 v
                  +---------------------------------------------------------+
                  |   ARC B -- inverse operator, the localized Weil form     |
                  |                                                          |
                  |   localized Weil quadratic form  Q = M_zeros - M_arith  |
                  |   |      (Hermite-Gauss basis at T0, width sigma, dim J) |
                  |   v                                                     |
                  |   07 - RIGOROUS DETECTOR                                |
                  |     - Front A: off-line zero => lambda_min(Q) < 0       |
                  |                (explicit constants)          PROVED    |
                  |     - Front B: truncation floor decays like            |
                  |                exp(-alpha (log X)^2), PNT only         PROVED    |
                  |     - Front C: the detector is technical; the          |
                  |                UNIFORM limit is RH-equivalent          |
                  +----------------------+-----------------------------------+
                                         |
                                         v
        +---------------------------------------------------------------------+
        |   0A2 - THE COMPRESSION QUESTION (the program's central question)    |
        |   Is  Q = P_J . T . P_J  a FAITHFUL compression of the Weil          |
        |   operator T?                                                       |
        |     - Part I  (algebraic): the compression identity                 |
        |     - Part II (spectral): no spectral pollution                     |
        |   0A2 implies H1 (uniform-in-T0 stability); H1 does NOT imply 0A2.  |
        +----------------------+-----------------------------------------------+
                               |  (only if 0A2 holds does the next box equal RH)
                               v
        +=======================================================================+
        |   THE WALL, NAMED                                                    |
        |   (LB):  inf spec(T) >= 0   <=>   lambda_min(Q_infinity(f)) >= 0      |
        |          for every f  =  Weil positivity  =  RIEMANN HYPOTHESIS       |
        |          (conditional on 0A2)                                        |
        |                                                                       |
        |   Finite-X is controlled (Front B). What remains open is the         |
        |   UNIFORM passage to the limit.                                      |
        +======================================+================================+
                                               |
                                               v
                          +-----------------------------------------------+
                          |   A stability probe (see Part 2) tested        |
                          |   whether Q is a faithful compression.         |
                          |   Verdict: BOTH tested hypotheses supported    |
                          |     (H1) uniformity-in-T0 falsifier did not    |
                          |          fire -- faithfulness survived         |
                          |     (H2) monotone, no Conrey-Li obstruction    |
                          |   A weak confirmer: GRH controls only, the     |
                          |   entanglement question stays untouched.       |
                          +----------------------+--------------------------+
                                                 |
                                                 v
                          +-----------------------------------------------+
                          |   Phase 4 -- pure-math attack on the wall      |
                          |   collapses the problem to CLASSICAL           |
                          |   structure: explicit formula -> off-axis      |
                          |   evaluations -> closability. See Part 4.      |
                          +-----------------------------------------------+
```

---

## Part 2 — What the stability probe could have bought

The stability probe returns a verdict on two hypotheses about the compression question 0A2.
Each verdict opens, narrows, or closes a road. No road is short, and every road ends at a
positivity that no finite computation can supply — the last step is always pure mathematics.

**The probe landed on the "both supported" branch** (the best of the four possible outcomes).
H1 (uniformity in $T_0$) and H2 (monotonicity) were both supported on the GRH controls, and the
Conrey–Li obstruction was specifically absent. This is the strongest empirical position — and,
by the one-way logic of 0A2, still only a weak confirmer: it keeps the "faithful compression"
scenario alive without settling the deeper entanglement question, which is a matter of theory,
not computation.

| Probe outcome | What it buys | Realistic next step | Chance of *proving RH* from here |
|---|---|---|---|
| (H1) supported alone | (LB) reduces to one operator positivity, $\inf\mathrm{spec}(\mathcal T)\ge0$ | hand Connes-trace positivity to an expert | very low, but the cleanest reduction |
| (H2) supported alone | (LB) reduces to a de Branges chain condition | check Conrey–Li, then expert | very low (de Branges has known gaps) |
| **both supported (what happened)** | two cross-checking ladders to (LB) | strongest position; still needs the proof | very low, best odds of the four |
| both refuted | the structural routes via $Q$ are dead | pivot to Nyman–Beurling/Li, or stop at paper 07 | effectively zero from this instrument |

---

## Part 3 — Where the program stood after the first two arcs

A survey whose thesis was positivity (paper 01). Arc A built descriptive machinery
(ω-classes), calibrated it (the DH null result), found a parity theorem, and had to correct
itself (paper 03 — sign artifacts that even refuted paper 02's original headline claim). Arc B
then gave the program its first rigorous result: paper 07, the localized Weil detector, which
turns the "Weil signal" into theorems with explicit constants and names a uniform-positivity
inequality that equals RH *provided* the localized form $Q$ is a faithful compression of the
Weil operator (the 0A2 question). That faithfulness — not RH itself — was, at this stage, the
program's central open problem: if $Q=P_J\mathcal T P_J$ holds spectrally, the wall is the
genuine Weil wall; if it fails subtly, the wall belongs to the localized scheme instead. The
stability probe does not climb that wall; it is a falsifier of faithfulness, and it survived.
Climbing the wall — proving the structural positivity — is pure mathematics beyond any closed
computational loop. *(This is where the deeper phases, Part 4 onward, took over. The program's
current final state is Part 12.)*

---

## Part 4 — Inside the Weil-operator program: the collapse to classical structure

This phase changed the shape of the problem. The program **stopped looking for a new
geometry** (Connes' noncommutative framework, the de Branges chain, and a Fock-space pivot were
each tried and each found unnecessary) and the question **collapsed back to classical
objects**: the explicit formula, off-axis evaluations, and closability. Fewer new
constructions, more classical structure, is the pattern that persisted for the rest of the
program.

**The chain of reductions, in order:**

1. **The compression identity holds** (Problem A, essentially settled: a Gram-matrix tautology
   plus the Front-B truncation bound from paper 07 together identify $\mathcal T$ as a
   legitimate object).
2. **A self-adjoint realization of $\mathcal T$ exists**, unconditionally, by a standard von
   Neumann deficiency-index argument (the operator admits the natural conjugation
   $f\mapsto\tilde f$, so its deficiency indices are equal).
3. **The explicit-formula identity (EF-id) holds on the operator's dense core**, unconditionally:
   $$\mathfrak t(g,g)=\sum_{\text{on-line}}|\hat g(\gamma)|^2+\sum_{\text{off-line}}4\,\mathrm{Re}[\hat g(t-ib)^2].$$
   The right-hand side is manifestly indefinite in general; its positivity is exactly RH.
4. **Two invariants separate the relevant function spaces**: $R=K\rho$ governs trace-class
   membership (trivial), and $P=\rho\ell$ governs the Carleson condition. A short computation
   shows that any admissible evaluation window forces $P\to\infty$, so the natural home for this
   problem is an *over-sampling* Hardy space, where both $\mathfrak t_+$ and $\mathfrak t_-$ are
   unbounded but coercivity ($\mathfrak t_+\ge c>0$) is easy (a Beurling over-density argument).
5. **The relative form bound (RFB), $\mathfrak t_-\lesssim\mathfrak t_+$, is the residual
   target.** Every *pointwise* route to it (Schur test, Gram-matrix comparison, Jaffard's
   interpolation technique) fails, because each one pays the same divergent price $P\to\infty$.
   Only a *statistical* route — where that divergent quantity cancels between $\mathfrak t_-$
   and $\mathfrak t_+$ rather than being bounded separately — survives.
6. **A statistical proof of RFB via band-fixed quadrature of the zeros.** In the classical
   Paley–Wiener class $PW_d$, the excess energy $E_g=\sum_\gamma|F(\gamma)|^2-\rho\int|F|^2$
   is exactly a Parseval pairing $\int_{-2d}^{2d}\hat g(\alpha)D_T(\alpha)\,d\alpha$. The naive
   global bound on $D_T$ is vacuous (it loses all localization); the correct object is a *local*
   bound obtained by integration by parts against an unconditional density estimate
   ($S(t)=O(\log t)$), giving $E_g=O(\mathfrak t_+)$ — the right order of magnitude, not a
   smaller one, but exactly what the target needs.
7. **The off-line sum closes unconditionally** via a Plancherel–Pólya argument (clustering of
   zeros is not an obstruction; only the local zero *count*, which is unconditionally $O(\rho)$,
   matters).
8. **What remains is coercivity of $\mathfrak t_+$ itself**, and here the news is mixed: a naive
   "infinitely many zeros off the critical line still leaves a Nyquist gap" argument does *not*
   suffice (a theorem of Beurling blocks it). But coercivity is only needed *near* off-line
   zeros, and a depth split shows shallow off-line zeros are harmless while deep off-line zeros
   are locally rare — controllable, in principle, by a uniform short-interval zero-density
   estimate strictly weaker than RH.

**Where this reduction lands.** Everything up to this point is unconditional. The single
remaining input is: **a uniform short-interval zero-density bound**, strictly between "no gaps
at all" and RH itself. If it holds, the localized Weil form is a genuine unconditional theorem
(a faithful, semibounded realization). This is a real, if narrow, achievement — but it does not
touch the *sign* of the bottom of the spectrum, which is RH itself. The magnitude bound gives
$|\mathfrak t_-|\le C\mathfrak t_+$ with $C\ge e^d>1$; RH needs $C\le1$ — positivity, not just a
finite bound. No density or sampling estimate lowers $C$ below $1$ without assuming RH.

**The resulting theorem (Kreĭn structure).** With the semibounded realization in hand,
$\mathfrak t=E^*JE$ with $J=J^*$, $J^2=I$ (a Kreĭn-space involution), and the whole problem
becomes the sign of one angular operator: $\mathfrak t=\|P_+EF\|^2-\|P_-EF\|^2$, so RH is
$\|K\|\le1$ for the associated contraction $K$. A companion **no-go theorem** proves that this
sign is *not reachable from the zero side alone*: the off-line depths enter $\mathfrak t$ only
through the quantity whose sign is exactly Weil positivity, so bounding $\|K\|\le1$ using
zero-side data is circular — it *is* Weil positivity, restated. This closes what became **paper
08** (a faithful Kreĭn-space realization of the Weil form, with the zero-side no-go).

**Route B — the only route left: is $\mathcal T$ a square, $A^*A$, for an $A$ built
independently of the zeros?** This was pursued through several fronts:

- **Comparing the Kreĭn structure of paper 08 to Connes' noncommutative-geometry framework**
  showed both share a common template — $\mathrm{RH}\iff\|K\|\le1$ for *any* metric
  decomposition of this shape — so matching the shape is not yet a bridge. But a real
  distinction survives: paper 08's operator $K$ is zero-dependent (it literally vanishes on
  RH), while the analogous Connes operator is a fixed, zero-*independent* compact operator.
  There is no natural zero-independent identification between the two, so paper 08's no-go
  does **not** transport to the Connes side — the Connes residual remains a genuinely
  unobstructed attack surface.
- **Comparing to the de Branges canonical-system structure** showed the same template again
  (a Hermite–Biehler / kernel-positivity certificate equals RH), but the specific de Branges
  positivity hypotheses proposed in the literature had already been refuted (Conrey–Li, 2000).
  A durable observation survived: under RH, the de Branges chain and paper 07's sampling
  ladder coincide.
- **The semi-local Connes residual** — positivity of $\mathrm{Id}-K_{CC}$ on a semi-local
  window — is the sharpest open frontier this comparison produced. It connects to a genuine
  finite-window analogue of the Connes program, built on paper 07's computable machinery.

**A creative-frontier program** then combined the Connes residual with the program's unique
computational assets — paper 07's engine and an explicit RH-violating control object, the
Davenport–Heilbronn function $L_{DH}$ (paper 04) — around one organizing question: *which
arithmetic invariant forces $\|K\|\le1$ for $\zeta$ but forces $\|K\|>1$ for a
non-Euler-product control?* This produced a genuine, if partial, positive research program:

- **A pure-theory classification program** proved that the natural "tautology test" for any
  candidate invariant is passed *by theorem*, not just by experiment: the zero-side operator
  from paper 08 literally *is* the tautology (it vanishes exactly on RH), while the arithmetic
  Connes-side invariant is provably distinct and real-analytic in the Euler factors.
- A forced spectral-transition theorem was lifted from paper 07's detector: the localized
  eigenvalue crosses zero exactly at a computable threshold, with rate confirmed numerically
  to high precision.
- The per-prime "anatomy" $R_p$ of the localized Weil form was characterized exactly:
  $\lambda_{\min}=R_\infty(u)-\sum_pR_p(u)$, an archimedean-versus-prime-mass competition, with
  a proved mass-form, a proved concavity/extremal reduction, and a proved exponential-stability
  theorem (paper 09) — all unconditional, all RH-*independent*, all durable mathematics.
- This anatomy program matured into two publishable results: **paper 09** (the exponential
  stability theorem, autonomous) and **paper 10** (the anatomy itself, the Carleson
  reformulation, and the resulting Conjecture B2 — factorizability of the anatomy implies an
  Euler product — later proved as a genuine converse theorem and folded into paper 10).
- A validated numerical engine confirmed every gate: $\zeta$ sits at the positivity floor,
  the forced-negativity exponent matches prediction, and the $L_{DH}$ control is correctly
  flagged as violating positivity.

**A separate, more ambitious attempt — Osterwalder–Schrader reflection positivity.** The
insight: the Kreĭn involution $J$ (complex conjugation composed with $\rho\mapsto1-\rho$) is
exactly the functional-equation reflection, so Weil positivity should be OS reflection
positivity for a lattice built from the Euler product, one factor per prime. If each local
factor were reflection-positive and the tensor gluing worked, OS reconstruction would deliver a
self-adjoint Hamiltonian — Hilbert–Pólya, for free. **This mechanism was computed and refuted:**
the exact local prime kernel $G_p$ is indefinite (verified for $p=2,3,5,7$ to full numerical
precision), so per-place reflection positivity fails outright, and the Euler-lattice mechanism
collapses. The refutation is itself informative: it shows RH is equivalent to the archimedean
envelope pointwise dominating the sum of these indefinite local kernels — and that comb, once
regularized, is essentially $\zeta'/\zeta$ on the critical line, i.e. **large values of $\zeta$**
(a genuine, hard, open frontier, closely related to the program's own ω-class machinery, but not
an obvious crossing). A careful audit of every follow-up attempt to exploit this observation
found each one flawed on inspection — the comb is a distribution, not a function, and the
naive pointwise-domination argument does not survive taking limits.

**What this phase established, in one sentence.** Before this collapse the picture was "RH
follows from some new geometry (Connes / de Branges / Fock)"; after it, the picture is "RH
follows from Weil positivity, which follows from the explicit formula, which follows from
off-axis evaluations and closability" — all classical objects, with the entire remaining
difficulty concentrated in one zero-density inequality (the RFB) and, beyond that, in the sign
of the Kreĭn operator $K$, which two independent no-go arguments show cannot be reached from the
zero side alone.

---

## Part 5 — The eight-language wall and the wrong-sign capstone

With Route B's honest conclusion in hand, the program engaged every modern reformulation of RH
it could identify. Each one reduced to the same statement, via the same underlying principle.

- **The band-limited Weil–Carleson form** (paper 12): a saturated positivity constant
  $C(d,T_0)=\lambda_{\max}$, with $\mathrm{RH}\iff C\le1$. Three findings: $C\equiv1$ for
  $\zeta$ in the natural regime, with prime incoherence buying zero margin; the detector's
  second-order statistic *is* the Montgomery–Dyson pair correlation; and $C(d,T_0)$ is exactly
  the Connes–Consani prolate compression constant — the same wall, reached from a third
  direction.
- **The de Bruijn–Newman heat flow** (paper 13): $\mathrm{RH}\iff\Lambda=0$. A Lyapunov theorem
  proves the critical line is the flow's attractor; a dynamical no-go shows the flow itself is
  arithmetic-blind (it cannot distinguish $\zeta$ from any other GRH-respecting control), so no
  purely dynamical argument can supply RH — the target becomes an unconditional gap
  universality statement.
- **A search for an arithmetic-aware monotone quantity along the heat flow** found none: every
  candidate is either generic (arithmetic-blind) or reduces, via the explicit formula, to the
  same wall. This produced the **wrong-sign capstone**: every unconditional tool available
  (sieves, density estimates, positivity of variance) supplies a *lower*-bound positivity, while
  RH is an *upper*-bound constraint. The available machinery has the wrong sign.
- **The cohomological/Hodge-index route** (paper 14, attempted specifically to escape the
  capstone, in analogy with the Weil-conjectures proof over function fields): a candidate
  intersection form was shown to degenerate exactly at the point where four different framings
  coincide ($C\equiv1$, $\Lambda=0$, a vanishing Hodge gap); the regularized form survives as
  definite, giving the identity $\lambda_{\min}(G)=\frac{\pi^2}{6}\beta_{\min}^2$ — but this
  reprices to exactly the same target as before (uniform short-interval regularity). The
  capstone holds even here.
- **The hyperbolicity / stable-polynomial route** (paper 14): real-rootedness of the Jensen
  polynomials of $\Xi$, via interlacing rather than positivity directly — the most promising
  *structurally different* mechanism considered. It reduces to a moment identity
  $b(k)=m_{2k}/(2k)!$, and the decisive fact (via Borcea–Brändén) is that real-rootedness of
  this kind **is itself** a positive-semidefinite Hermite-form condition. The capstone holds
  even in the richest available positivity language.

**The headline of this phase.** Eight independent paradigms — the explicit-formula/Kreĭn
approach, per-place analysis, the Carleson form, pair correlation, the Connes prolate operator,
the heat flow, the cohomological/Hodge route, and hyperbolicity — all reduce to a positivity
statement and to the same cornered target, and the deepest single finding is the wrong-sign
capstone: every unconditional handle available in current analytic number theory is a
lower-bound positivity, while RH demands an upper-bound one. This was confirmed across all
eight paradigms, including the two (Hodge, hyperbolicity) specifically built to escape it. This
is a chart of the wall of unusual completeness — not a passage through it.

---

## Part 6 — The first mechanism-correct path

The capstone itself pointed to the next move: find a mechanism whose *native* output is an
unconditional upper bound rather than a positivity. The one branch of mathematics tied to
$\zeta$ with that property is **log-correlated fields and multiplicative chaos**.

- $S(t)=\arg\zeta(\tfrac12+it)$ is log-correlated (the measured covariance slope matches the
  theoretical value); tight zero-pairs correspond to its steepest rises.
- The natural upper bound on this field is a first-moment (union/Markov) bound — **not a
  positivity statement**, and so, for the first time in the program, a genuine escape from the
  capstone.
- This immediately meets a second, independent obstruction: a probabilistic/deterministic
  barrier. The log-correlated-field machinery describes the *statistics* of an ensemble; RH is
  a statement about one *deterministic* configuration (the actual off-line zero count, which
  must be exactly zero). Two fundamentally different obstructions now co-exist: the capstone
  (deterministic tools have the wrong sign) and this new barrier (the right-signed tools are
  the wrong *kind* of object).
- The barrier is bridged, partially: $S(t)$ can be derandomized as an explicit prime sum
  (verified), turning the union-bound count into a large-value count for that prime sum,
  controllable by the large sieve — the first tool in the program that is simultaneously
  deterministic, upper-bound, and not a positivity statement.
- The resulting moment computation is sharp in its low-order reach (the relevant sum is
  Gaussian, by the $\mathbb Q$-linear independence of $\{\log p\}$), but its extreme values are
  governed by near-resonances among the $\log p$ — precisely the **additive energy of the
  primes**, the object already studied in paper 02's ω-class machinery. Baker's theorem on
  linear forms in logarithms is qualitatively the right tool but exponentially too weak
  quantitatively; a sharp high-order bound on this additive energy is exactly the
  moment-conjecture frontier (Conrey–Farmer–Keating–Rubinstein–Snaith).

**The headline of this phase.** This is the program's first mechanism-correct chain, start to
finish: it escapes the wrong-sign capstone and bridges the probabilistic/deterministic barrier,
reaching the extreme values of $\zeta$ by a route that is deterministic, upper-bound, and
non-positivity throughout. What remains is a genuine, sharply stated open problem — a
high-order additive-energy bound for $\{\log p\}$ — and, remarkably, this is exactly the problem
the program's very first arc (the ω-class program) had already been built to study. For the
first time, the obstruction found is the *right* one, not a restatement of positivity.

---

## Part 7 — Closing the strategy map: the discriminator and the unconditional finite bottom

After reaching the ω-class frontier again from a completely different direction, the program
turned from attacking individual routes to building an *instrument* for classifying every
future one, and closing the strategic map as a whole.

- **The ω-hierarchy** (paper 05, RH-independent): the moment exponent, multiplicative-chaos
  freezing, and a branching-random-walk picture of the maximum of $\log|\zeta|$ are shown to be
  one and the same structure, viewed three ways. Genuinely new mathematics, but it does not
  face the zeros.
- **The ω-to-zeros direction was closed.** A Motohashi-type factorization shows the relevant
  generating function is self-referentially built from $\zeta$ itself in a way that makes any
  ω-based route back to the zeros circular, because $\omega(n)$ is prime-blind by construction.
- **A discriminator, D0**, was built and calibrated: an operational filter deciding whether a
  proposed new mathematical object can, even in principle, escape the walls already found. It
  is a four-clause test (does the object distinguish primes; does it supply genuinely
  independent input via a decisive existing theorem; does it resolve individual zeros, not just
  averages; is it arithmetic-aware) calibrated against roughly thirty historical RH programs and
  four positive controls, including the two genuinely *proved* analogues of RH (the function-field
  case, twice). Every attempted ζ-side route is blocked either by a missing-geometry obstruction
  or by an "object-special" trap (the candidate secretly re-encodes $\zeta$ rather than
  supplying independent structure).
- **The finitization obstruction.** The only remaining kind of new object that could work is a
  *finite-dimensional model* of ζ's positivity — formally, a Frobenius periodicity, in analogy
  with the function-field case (where the zeros repeat with a finite period). Under the standard
  linear-independence hypothesis for the ordinates $\{\gamma_n\}$, **no such periodicity can
  exist** (paper 06). This closes off finite-dimensional model-building as a route, and applies
  uniformly across several concrete finite-order-positivity families (Hodge-theoretic, Hankel,
  total-positivity, combinatorial-Hodge) — every finite order is unconditional; the full order is
  RH.
- **The Pontryagin-index route was closed by direct computation** (paper 11): the index
  $\kappa=\#\{\text{off-line zeros}\}$ is finite only if a tail relative-form-bound holds, and
  two independent computations show it does not — a subordination cutoff diverges, and the
  near-critical multiplicity of the relevant operator grows without bound.
- **The localized Weil form was made unconditionally semibounded, modulo a logarithmic loss**
  (paper 16): a verified identity for the second moment, combined with the large sieve, gives an
  unconditional lower bound on $\mathfrak t$ up to a $(\log T)^c$ factor; a Goldston–Montgomery
  equivalence reduces closing that gap to a *uniform short-interval prime variance* estimate —
  strictly weaker than RH and strictly stronger than anything currently known, but genuinely
  non-circular. A three-level hierarchy separates the target cleanly: semibounded (achieved) <
  finite index (refuted) < RH.

**The headline of this phase.** The program closed its own strategy map: every RH-directed
branch collapses either to the wrong-sign capstone or to the missing-geometry wall, unified as
the absence of a finite-dimensional, Frobenius-periodic model of ζ's positivity — an absence
that is *proved*, not merely observed, under linear independence of the zero ordinates. The
discriminator gives future ideas a fast, calibrated classification. The one genuinely new
RH-directed gain from this phase is paper 16: the localized Weil form is unconditionally
semibounded modulo a logarithmic loss, with the residual difficulty identified precisely as a
recognized sub-RH frontier. Everything else new and durable that this phase produced (papers 05,
09, and Conjecture B2) is RH-independent.

---

## Part 8 — The Lefschetz dichotomy and the SURF specification

The program then built the full Weil scaffold for an arithmetic intersection theory over
$\mathrm{Spec}\,\mathbb Z$, reducing RH to the existence of one missing object — an independent
hard-Lefschetz $\mathfrak{sl}_2$ triple, or equivalently an ample (Kähler-type) class $\omega$ —
and then proved why the spectral routes available cannot supply it.

- The arithmetic intersection pairing, its trace identity, effectivity, and the ample cone were
  all built and verified to high numerical precision.
- $\mathrm{RH}\iff\omega\succ0$ on the relevant orthogonal complement; the missing class
  $\omega$ must satisfy an **independence filter** ($\omega$ cannot lie in the operator algebra
  generated by the Weil form itself) — any spectrally derived candidate for $\omega$ only
  restates RH.
- An explicit, $\mathcal T$-independent hard-Lefschetz $\mathfrak{sl}_2$ triple **was**
  constructed on the archimedean continuum, verified to high precision — the first such
  explicit object in the program. Its transport to the arithmetic side is exactly the explicit
  formula, and the resulting positivity is a near-cancellation residual — the wall named
  earlier as the capstone, reached again.
- **The Lefschetz dichotomy** (paper 17): an integer (lowest-weight) hard-Lefschetz grading and
  the linearly-independent arithmetic zero spectrum are structurally incompatible. In the
  discrete picture there is no Tate-twist operator available on the zeros; in the continuum
  picture the relevant representation is a principal series, which does not carry a
  hard-Lefschetz structure at all. This sharpens the finitization obstruction (paper 06) to a
  precise representation-theoretic statement.
- A prismatic-cohomology route was traced and found to relocate the same obstruction: the
  relevant Frobenius structure exists *locally* (at each prime, as local Satake data) but the
  obstruction is *global* gluing — exactly the missing object again, now in a third language.
- A submitted third-party "proof" invoking Connes' framework was checked and refuted, with six
  independent fatal flaws identified.
- A literature program returned three honest negative results — matching, independently, the
  three-route obstruction already found — plus one new RH-independent constraint (a rigidity
  bound on the third moment of prime gaps, tied to a prime-power design constraint).
- An "Arakelov–RH equivalence" claim from the literature was checked and clarified: its honest
  content is a one-directional theorem (existence of a suitable witness variety implies RH, via
  the Yuan–Zhang arithmetic Hodge index theorem); the converse (RH implies such a variety
  exists) is the open Hilbert–Pólya dream, and may simply be false if the zeros are not
  geometric in the required sense.

**The SURF specification.** This phase closed by fixing precise acceptance criteria for any
future construction of the missing witness variety: four pillars (spectrum, pairing, Lefschetz
structure, positivity) and four rejection filters, with the correction that the required
positivity theorem for the zero-carrying cohomology is *not* available from the Yuan–Zhang
theorem (which controls a different, related object) — it is a genuinely new theorem that would
need to be proved, not cited.

---

## Part 9 — The forward ω-flow and the zero–ω bridge

In parallel with the Weil/SURF program, an independent arc traced the direct flow from primes,
through the ω-class statistics, to multiplicative chaos and moments — deliberately without
reference to the zeros of $\zeta$, to see how far arithmetic statistics alone could reach.

**An unconditional, RH-independent chain** (five steps, no zeros involved):

```
   primes -> omega(n) ~ Poisson(log log n)        [Erdos-Kac / Turan-Kubilius]
          -> E[q^omega] ~ (log n)^(q-1)            [Poisson moment-generating function, q = k^2]
          -> M_k(N) ~ C_k (log N)^(k^2)            [elementary integral; the exponent k^2 is forced]
          -> large-deviation saturation             [the same phenomenon at each step]
          -> B-smooth condensation                  [weight shifts toward large omega]
          -> the random maximum grows with sum(1/p) [a log-correlated branching-random-walk field]
```

The exponent $k^2$ and its constant are both prime-theoretic and provably convergent without
reference to any zero of $\zeta$. This is durable, RH-independent mathematics.

**Does ω-statistics see the zeros at all?** A Selberg–Delange factorization answers this
directly: the generating function for $q^{\omega(n)}$ factors as $\zeta(s)^q\cdot G_q(s)$ with
$G_q$ holomorphic and non-vanishing where it matters — so the zeros of $\zeta$ appear as *zeros*
of this generating function, not poles, and Perron's formula for the relevant moments picks up
no residue at them. The moments are monotonically increasing; they never oscillate. The zeros
are, to first order, invisible to this statistic.

**Where the zeros do enter.** The only channel through which the zeros affect the ω-class
statistics in a non-trivial way — one that does not simply reduce to the prime-counting function
$\psi$ itself — is the *rate of convergence* of the cross-correlation
$C_k(h,N)/M_k(N)^2\to r_q(h)$. An explicit error formula was derived for this rate,
$$\frac{C_k(h,N)}{M_k(N)^2}-r_q(h)=-\frac{A_q(h)}{C_q^2}\sum_\rho\frac{N^{\rho-1}}{\rho}+O(\text{smaller}),$$
with an explicit, strictly positive coefficient $A_q(h)$. This gives an unconditional
**equivalence**: this convergence rate is $O(N^{-1/2+\varepsilon})$ if and only if RH holds. And
a structural theorem closes off any hope of an alternative route: because $A_q(h)>0$ at every
multi-point correlation, the positivity of $q^{\omega(n)}$ **prevents any algebraic cancellation**
of the zero terms — there is no "arithmetic resonance" internal to the ω-class construction that
could eliminate the zeros' contribution without already assuming RH.

**Conclusion of this arc.** The ω-class family contains enough information to reconstruct
$\zeta$'s bulk statistics (moments, multifractal structure) but not the fine geometry of its
zeros. The zeros surface only in the error term of one specific cross-correlation, and that
error term is provably equivalent to RH via the same classical mechanism (the prime number
theorem in arithmetic progressions) found by every other route in this program. There is no
zero-free direction inside the ω class.

---

## Part 10 — Phases 21–61: the wall mapped from every side

*Full phase-by-phase detail lives in [`COMPLETE-PROGRAM-SUMMARY.md`](COMPLETE-PROGRAM-SUMMARY.md).
This is the one-paragraph map of a long stretch of the program.*

After the ω-class branch reached the same classical wall, the program ran the **Arc-B closure**
(the Pontryagin/Kreĭn realization pushed to its Paley–Wiener barrier, a fifteen-mechanism audit,
four parallel fronts all reducing to the statement "$\Xi\in$ Laguerre–Pólya"), then the **CCM
framework** (the Connes–Consani–Moscovici trace criterion, $T_\lambda=0\iff\mathrm{RH}$, and its
Hadamard barrier), then a long sequence of new-direction attempts: the amplification functor,
a Hodge/$\mathrm{Spec}\,\mathbb Z$ construction, the Deninger leafwise-Hodge route (found
non-circular as a *framework* but later shown to be indeterminate/circular as an actual proof
route), and a series of new-mathematics constructions interleaved with adversarial audits (one
audit refuted an incorrectly claimed kernel positivity and the trace criterion was repaired via
moment rigidity).

A later stretch attacked **the wall as an object in its own right**: it was characterized as the
kernel of an averaging operator; the five classical crossing mechanisms known to number theory
(Tauberian theorems, positivity arguments, functional equations, group/dynamical arguments, and
index/K-theoretic arguments) were shown to provably collapse for the Weil form specifically; and
every canonical inertia metric on the relevant crossed-product construction was shown to carry
$\zeta$ by modular structure (the Bost–Connes system) rather than by anything specific to RH.
This stretch closed with a precise decomposition $\mathrm{RH}=A\wedge\mathrm{Dic}$ (each half
independently calibrated), roughly eighteen new unconditional theorems, the accumulated no-go
results organized axiomatically, and a precise interface specification for any future external
attack.

One further phase refuted a proposed "multiplicativity discriminant" (a new variant of the
arithmetic-propagation wall), and the phase that followed took inventory of what remained
genuinely open within this framework.

**The state at the end of this stretch.** RH lived in the sign of one global scalar $\kappa$.
Every front reached it; none crossed it. The crossing appeared to require a cohomology over
$\mathrm{Spec}\,\mathbb Z$ that reads inertia rather than value — the still-unbuilt
Connes–Consani arithmetic site — which is RH-equivalent by construction and therefore no easier
to build than to prove RH directly. *(Part 11, next, sharpens this into a single named classical
criterion.)*

---

## Part 11 — Phases 62–76: the pivot to $\Omega_7$

```
                          +-------------------------------------------------+
                          |  PHASE 62 - Cesaro-in-lambda / quaternionic HR   |
                          |  Averaging relocates the arithmetic-propagation  |
                          |  wall; it does not cross it (off-line growth is  |
                          |  secular). A real quaternionic Hodge-Riemann     |
                          |  polarization was found on the Weil window --    |
                          |  but it is GAPLESS: zeta sits at the marginal    |
                          |  threshold, mu_max = 1.                          |
                          +----------------------+----------------------------+
                                                 |
                          +----------------------v----------------------------+
                          |  PHASE 63 - Lefschetz realization frontier        |
                          |  The function-field analogue has a J-linear      |
                          |  Frobenius isometry of a GAPPED polarization;    |
                          |  the zeta window has neither property (its       |
                          |  scaling is antilinear, its polarization         |
                          |  gapless). This makes the missing-object wall    |
                          |  precise by direct contrast with the one proved  |
                          |  case of RH.                                     |
                          +----------------------+----------------------------+
                                                 |
                                sharpest statement of the wall reached so far
```

**The pivot off Weil positivity, onto $\Omega_7$:**

```
   PHASE 64 (Connes' route)              PHASE 65 (signature continuity)
   L1 reclassified as an RH criterion    Constructs an index-graded
   in its own right; the live target     determinant and topology;
   becomes REGULARIZED positivity,       isolates the decisive burden
   not a finite spectral gap             (a Feshbach-shorting argument)
             |                                       |
             +--------------------+------------------+
                                  v
   PHASE 66 (rank-one escape)            PHASE 67 (quantum q-index)
   The candidate operators are           A free-product Haar-orthogonality
   self-adjoint BY CONSTRUCTION, so      argument kills the arithmetic
   there is no positivity left to        interference this route needs
   prove; the open question becomes
   boundedness -- a different kind
   of question than Weil positivity
             |                                       |
             +--------------------+------------------+
                                  v
   PHASE 68 (GLT/Toeplitz symbol)        PHASE 69 (exact signed index)
   Symbol positivity turns out to be     A signed-index identity,
   GAUGE-FRAGILE -- it fails the         ind_-(A_N - P_lambda) = 0 <=> RH,
   generalized-locally-Toeplitz          is made gauge-robust and exact.
   distribution law numerically          Solid as a detector; the forcing
                                          mechanism is still open
             |                                       |
             +--------------------+------------------+
                                  v
                  +-------------------------------------------+
                  |  PHASE 70 - Lee-Yang / de Bruijn-Newman     |
                  |  RH <=> Lambda = 0 (Rodgers-Tao: Lambda>=0) |
                  |  The open content is localized to the      |
                  |  arithmetic direction Lambda <= 0 -- a      |
                  |  genuine forcing mechanism, the first       |
                  |  clearly positive turn of this arc.         |
                  +----------------------+-----------------------+
```

**A finite architecture, closing into paper 36:**

```
                  +-----------------------v-----------------------+
                  |  PHASE 71 - CAND-1 / CCM finite convergence     |
                  |  The spectrum is real BY ALGEBRA (this route    |
                  |  never touches Weil positivity at all). The RH  |
                  |  content is now entirely a question of stable-  |
                  |  divisor OPERATOR CONVERGENCE.                   |
                  +----------------------+-----------------------+
                                         |
                  +----------------------v-----------------------+
                  |  PHASE 72 - Feshbach leakage calculus           |
                  |  Converts the global convergence question into  |
                  |  a pole-relative leakage estimate -- a strictly |
                  |  smaller, more tractable target.                |
                  +----------------------+-----------------------+
                                         |
                  +----------------------v-----------------------+
                  |  PHASE 73 - Cauchy projection gate              |
                  |  Reduces the leakage estimate to ONE finite      |
                  |  Cauchy-Schur nodal identity, named NAT-PROJ.    |
                  +----------------------+-----------------------+
                                         |
                  +----------------------v-----------------------+
                  |  PHASE 74 - Hilbert eigenline cancellation      |
                  |  NAT-PROJ is rewritten as an exact Hilbert       |
                  |  product-rule identity, named HPR-DIV.           |
                  +----------------------+-----------------------+
                                         |
                  +----------------------v-----------------------+
                  |  PHASE 75 - Arithmetic numerator divisibility   |
                  |  Attacks HPR-DIV via a chain of finite           |
                  |  arithmetic-divisibility statements:             |
                  |  ARITH-LOCK => CCM-ROOT-LOCK => CRIT-NUM-DIV     |
                  |  => CAUCHY-EIG-LOC => HPR-DIV.                   |
                  +----------------------+-----------------------+
                                         |
                  +----------------------v-----------------------+
                  |  PHASE 76 - Normalized adjugate arithmetic lock |
                  |  Corrects the endpoint identity to A_L = |C_L|^2;|
                  |  roughly sixty-five audited sub-steps close it   |
                  |  down to one remaining limit-point uniqueness    |
                  |  statement.                                      |
                  +----------------------+-----------------------+
                                         |
                                         v   feeds directly into Part 12
```

---

## Part 12 — The current final state: paper 36, the fifteen-step architecture, and $\Omega_7=$ Li–Keiper

This is the program's current endpoint. It is published as **paper 36**,
["The Riemann Hypothesis: An Obstruction Ledger and the Arithmetic Pick Architecture It
Shaped"](04-papers/36-obstruction-ledger/), already posted to arXiv.

The paper has two parts. **Part I** is the obstruction ledger: every structural wall found by
this program (MW-1 through MW-6, catalogued in [`NO-GO-LIST.md`](NO-GO-LIST.md)) is stated
precisely and assigned an exact logical status. **Part II** is a new, independently constructed
fifteen-step architecture — the **Arithmetic Pick/Nevanlinna Program**, ARP-P — proving

$$\text{ARP-P}\iff\text{RH}.$$

### The fifteen steps

Fourteen of the fifteen steps below are fully proved (two of those fourteen, Steps 9 and 11, as
proved *conditional* consequences of Step 5). **Step 5 is the sole open input.** Every other
step is a classical or complex-analytic implication with no remaining gap.

| Step | What it establishes | Status |
|---|---|---|
| 1 | Sets up the variables, the completed zeta function $\Xi$, and translates RH into a statement about zero locations in a shifted coordinate. | Closed |
| 2 | Defines finite evaluation channels and the target function $G_\Xi^F$. | Closed |
| 3 | Proves meromorphy of $G_\Xi^F$ with no holomorphic ambiguity. | Closed |
| 4 | Establishes the Weil explicit formula on the relevant half-plane. | Closed |
| **5** | **ARP-P**: a finite-node arithmetic Pick-positivity condition. | **Open — the single input** |
| 6 | Positive Cauchy transforms have positive Pick kernels (a classical fact from Nevanlinna–Pick theory). | Closed |
| 7 | A "tower" version of ARP-P implies ARP-P itself. | Closed |
| 8 | ARP-P produces genuine Nevanlinna–Pick interpolants. | Closed |
| 9 | Normality of the interpolant family and a Montel extension argument. | Closed, conditional on Step 5 |
| 10 | Detects residues channel by channel. | Closed |
| 11 | ARP-P removes any off-line poles in the relevant domain. | Closed, conditional on Step 5 |
| 12 | The resulting symmetries cover all of $\mathbb C\setminus\mathbb R$. | Closed |
| 13 | Real zeros of $\Xi$, in this coordinate system, are exactly RH. | Closed |
| 14 | RH implies ARP-P (the converse direction). | Closed |
| 15 | ARP-P $\iff$ RH (assembling Steps 1–14). | Closed |

Steps 1–4 build the classical setup; Steps 6–15 are a closed analytic bridge showing that *once*
Step 5 is supplied, RH follows (Steps 1–13), and that RH conversely implies Step 5 (Step 14) —
so the equivalence in Step 15 is exact, not one-directional. All of the architecture's difficulty
is concentrated in Step 5.

### Developing Step 5: the $\Omega$-chain down to $\Omega_7$

Step 5 (ARP-P) does not reduce to RH all at once. It factors through a chain of six further
proved equivalences, $\Omega_1$ through $\Omega_6$, terminating at $\Omega_7$ — the one
statement in the entire architecture that is not closed.

| Link | Statement | Status |
|---|---|---|
| $\Omega_1$ | $\mathrm{RH}\iff$ every zero of $\Xi$ is real. | Closed |
| $\Omega_2$ | Real zeros $\iff$ ARP-P (this is exactly Steps 1–15 above). | Closed |
| $\Omega_3$ | ARP-P $\iff$ a terminal positivity condition, $\delta_N(z_0)\ge0$ for all $N$, in a specific reference-whitened form. | Closed, in that whitened form |
| $\Omega_4$ | $\delta_N\ge0$ for all $N$ $\iff$ a one-sided whitened spectral-radius domination condition. | Closed |
| $\Omega_5$ | Interior positivity has a positive, regular limit as the boundary is approached. | Closed, for each $N$ |
| $\Omega_6$ | Boundary positivity $\iff$ the classical **Li–Keiper criterion**, $\lambda_n\ge0$ for all $n$. | Closed |
| $\Omega_7$ | $\lambda_n\ge0$ for all $n$: an archimedean ceiling term must dominate an oscillating prime-side term, uniformly in $n$. | **Open — the terminal residue; equivalent to RH** |

Every link $\Omega_1$ through $\Omega_6$ is a proved equivalence. $\Omega_7$ is not a link — it
is the statement the entire chain isolates. It is not a new discovery: it is the classical
**Li–Keiper positivity criterion** for RH, known since 1997. The contribution of this program is
that an independently constructed fifteen-step architecture, built from an entirely different
starting point (Pick/Nevanlinna interpolation theory rather than the Li–Keiper coefficients
themselves), **terminates at exactly the same classical statement.**

Two proved facts sharpen what any attempted closure of $\Omega_7$ must look like:

- **No finite prime truncation gives a positive operator to perturb from.** The full sum over
  all primes is positive (this is exactly RH), but the same sum truncated at any finite cutoff
  $X$ is *negative*, verified computationally at multiple truncation depths. Positivity is
  restored only by summing the entire, infinite prime tail — it is a genuine global
  cancellation, not a small correction to an already-positive quantity.
- **This defeats the two natural perturbative attempts to close it.** Mollifying the evaluation
  symbol is equivalent, in the relevant limit, to the same truncation and inherits the same
  indefiniteness. Running the de Bruijn–Newman backward heat flow (starting from a height where
  the zeros are known to be real, by the proof that $\Lambda\ge0$) propagates a margin that
  shrinks factorially in the window size against a merely polynomial error drift, so it closes
  only a bounded range of the index $n$, not all of it.

Every attempted route through phases 64–76 to close $\Omega_7$ — the rank-one/self-adjoint
route, the quantum q-index route, the GLT/Toeplitz-symbol route, the exact signed-index route,
the Lee–Yang/de Bruijn–Newman route, and the finite CAND-1/Feshbach/Cauchy–Hilbert architecture
that produced this very reduction — returned, on inspection, to one of the six structural walls
(MW-1 through MW-6) catalogued in [`NO-GO-LIST.md`](NO-GO-LIST.md).

### What changed, honestly

$\Omega_7$ is exactly as hard as RH — being equivalent to it, it carries the Hypothesis's full
difficulty, and this reduction does not lower that difficulty by one degree. What changed across
phases 62–76 is the *resolution* of the map. Before this arc, the program's honest final
statement was that RH requires "an unbuilt cohomology over $\mathrm{Spec}\,\mathbb Z$" — real,
but abstract, and not stated as a checkable inequality. After this arc, the program's honest
final statement is that RH requires one classical, precisely stated inequality — Li–Keiper
positivity — reached independently through an arithmetic Pick/Nevanlinna architecture, with
fourteen of its fifteen supporting steps fully proved and a falsification harness available for
outside attack.

**No proof of RH is claimed.** This is a reduction, not a resolution — but it is the sharpest,
most concrete statement this program has produced of exactly where RH lives and exactly what a
proof would need to supply.
