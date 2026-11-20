# Re-audit of phases 161-210 (window positivity, standalone problem)

Scope read: Paper 47 main.tex lines 90-160 (definitions of a_T, lambda_A, W_T) and
10650-10800 (open problems (L2)/(N)/(S)/(R)); 05-meta-and-planning/ROUTES-TRIED-INDEX/README.md;
06_OPEN_RESIDUES_DEAD_SUBROUTES.md (full, 229 lines); phase READMEs/WORK_STATE/REVIEW_STATE for
phase-202 (exterior plank), phase-205 (composing object), phase-209 (nonlocal kernel,
GOAL_D_STATUS.md + SYNTHESIS.md), phase-210 (QRH 4/5).

## Per-phase summaries (161-210)

Given the budget, I did not re-open every single phase folder at full depth (162-201 are already
summarized, cross-indexed, and curated into the ROUTES-TRIED-INDEX files 04_PHASES_100-189.md and the
06_OPEN_RESIDUES file, which post-date and subsume the individual phase READMEs). What follows is
based on the 06_OPEN_RESIDUES ledger — which is the authoritative, current-as-of-2026-10-14 status
file explicitly designed to answer "what is the exact current status of every live residue" — plus
direct re-reading of the three phases the task calls out specifically (202, 205, 209) and 210.

- **Phase 162 (first-contact closure) / master grid**: λ_A continuity proved; Gate-1 after 3 NO-GOs;
  rounds 6-18 all NO-GO. Feeds directly into R1-R10 residues below. No new finding beyond index.
- **Phase 163 (★_cell) / 164 (tail theorem)**: (★_cell)⇒(TC) proved; L1 hybrid split, L2 Beurling <1/3
  bound. Indexed, closed as tool, not as sign source.
- **Phases 165-182**: a long sequence of named objects/attempts (critical interlacing, Ω-closure,
  witness-weighted sieve, input architecture, global prime inequality, discrete Beurling frontier,
  object-01, total exclusion, third coordinate, Euler-Poisson transversality/Petz, fermionic/oriented/
  Kadison interference, complex polarization, rectangular tunnel) — all fully absorbed into the
  ROUTES-TRIED-INDEX "Closed families" list (Sonin/Connes/prolate/semilocal; coercivity/Schur/Wiener-
  Hopf/Nyquist/witnesses; Euler/Möbius algebra; transport/reflection/Frobenius dilation). No
  unrecognized partial result surfaced on re-check.
- **Phases 183-186 (Sonin chain, residues, crossword, toolbox)**: per MEMORY and index — semilocal
  Sonin chain PROVED ∀S finite with no sign; Theorem X (new primes must cancel σ on U at resolution
  π/T) — listed under "dead: thm:X converse" in 06_OPEN_RESIDUES ("NO-GO: M₁ satisfies X and is
  negative"). Correctly labeled dead, not stopped-by-fatigue.
- **Phases 187-193**: pattern/closing-D/new-theory/near-coincidence experiment/design-T-star/exact-
  identity/creation campaign — feed Problem (S) and the "Admissible directions" of R9. No live
  unflagged thread found.
- **Phase 194 (invention, INV_A...INV_K)**: all eleven threads (Lévy/Hamburger rigidity, pair surface
  Hodge/CS/nef, Farey/Möbius pair counts, Mp₂ Weil character, Kronecker-Hurwitz/Eichler-Selberg, cones
  across ∂log, min/hyperbola balance, additive ℕ/Ramanujan/Vaughan, integrality, additive prime
  correlations) are recorded NO-GO/ARGUED in the index's "Closed families" paragraph, with a precise
  joint specification of what any sign-carrying object must satisfy (clauses 1-6) and one explicitly
  flagged open clause: **clause (5), "couple Λ at n<e^{2T} to the functional equation through a route
  other than the factor ζ(½+iτ)" — labeled OPEN, no known object.** This is a genuinely open, correctly
  labeled gap, not a mislabel.
- **Phases 195-201**: modern tools / global object / barrier theorem / parity split / frontier pattern
  / sign object / untried families — feed into phase 204's tractability review and into the
  specification of the "admissible region" (R) of Paper 47. No hidden partial proof found.

## Detailed audit: phase 202, exterior plank (★★)

File: 03-research/phase-202-exterior-plank/README.md, WORK_STATE.md, REVIEW_STATE.md.

Status: **phase explicitly closed by its own pre-declared death criterion (a), in round 2** — not
stopped by fatigue. Quote (README): "Closure — phase dead by criterion (a) in round 2... No
sign. (★★), L′♯, row D OPEN." The death criterion was fixed *before* starting (three rounds of a
fixed team); it triggered in round 2, i.e. inside budget, not because of an external stop.

Last mathematical obstacle, precisely: Lemma M (R2, PROVED) shows the archimedean weight 𝔅_n is never
multiplicative (by Riemann-Lebesgue, the only continuous multiplicative function on dense log ℚ is a
character, and the Euler product does not converge at ½); the sum Σμ(n)n^{-½}𝔅_n collapses to
∫m|r̂̃|²D_N(½-iτ)dτ, i.e. a "1/ζ channel" (already closed as route C6). So the one candidate way to use
the exact values of Λ in the exterior region produces no new inequality — it is an identity, not a
sign source. The remaining unaddressed residue is the "layer edges κ_{T+log n}" size bound, explicitly
flagged as "Residue without a proposal" — nobody has attempted this.

## Detailed audit: phase 205, composing object

Files: README.md, RFIN_TRACT_001.md, REVIEW_STATE.md.

This is the Toeplitz-Hankel-type finite reformulation "n₋(𝔄_N(T)) = 1 ∀T" in a basis of Dirichlet
sines (dimension N(T) ≈ 4T, polynomial — contrasted with (L2)'s exponential k(T)). **Status: TRACT = NO
(does not escape the N3 NO-GO), closed as REF-D "in block form."** Not stopped by budget: §3 of
RFIN_TRACT_001 walks five candidate proof strategies (finite Toeplitz inequality from an arithmetic
identity; rank argument; Szegő/Widom/Avram-Parter/GLT; interlacing-in-T/block continuation; monotone
n₋ in N) and kills each one with a specific reason (the only exact arithmetic identity routes back to
the explicit formula's zero side; no bounded rank beyond the main term; critical sampling defeats
Szegő-type asymptotics (same as W-det/R164_502c); continuation is "Hellmann-Feynman at the crossing,"
i.e. a functional of the minimizer (forbidden by Theorem X); monotonicity runs the wrong direction).

What changed relative to the frontier before 205, honestly stated in §3.2: only the **size** (dim ≈2T
vs exponential) is a genuine computational improvement; canonicity and cancellation-within-the-block
make tractability *worse*, not better — the near-zero margin (~1e-15 to 1e-17) is "the exact analogue
of (L2)'s 10⁻⁷⁰ margin." This is an honest self-report of non-progress disguised as progress, caught
by the phase's own audit — a good example of disciplined labeling, not a mislabel.

One real byproduct: **Lemma RF.1, labeled PROVED-elementary (to be written up)** — a genuine lower
bound n₊(Φ_N) ≥ 1.95T − 2 on the number of directions in which the compressed Chebyshev remainder must
be positive. This is a small proved fact sitting unintegrated (not in Paper 47, not cross-referenced
elsewhere); it is a legitimate, currently-true partial statement, but it is explicitly scoped as giving
"no sign" — so it is not an unrecognized route to λ_A ≥ 0, just an uncatalogued auxiliary lemma. Worth
flagging as a minor index gap: it is not yet in 06_OPEN_RESIDUES (the phase-205 index entry at the
bottom of RFIN_TRACT_001 records it informally but 06_ file's table for (L2) does not cite RF.1
explicitly, though it does cite the companion facts).

## Detailed audit: phase 209, nonlocal kernel

File: GOAL_D_STATUS.md (full log of ~20 continuations, 2026-10-18 to 2026-10-19) and SYNTHESIS.md.

**This is the strongest candidate for "stopped-not-dead," but the log itself argues against that
framing with unusual rigor.** The explicit goal-tracking tool was set to status `blocked` after three
consecutive continuations (post-016) produced no new step toward the sign of the auxiliary kernel Q.
The log is explicit that this is *not* a budget/patience stop: "A usage limit is NOT the reason for the block" and reiterates at each
step that blocked ≠ a mathematical NO-GO ("this is not a proof that [the object] doesn't exist: it is this investigation's
dead end"). So by the standing project rule (only NO-GO-by-proof or falsifier closes a route), this
residue should be read as: **genuinely stuck for lack of a new idea, explicitly not closed, explicitly
not a mathematical impossibility** — which is precisely the "stopped but not dead" category the task
asks to flag, except that the phase file is unusually careful to say so itself.

Chain of auxiliary results inside 209 (all PROVED/CITED but all explicitly scoped as "no sign for Q"):
- CONSTRUCTOR_005/AUDIT_005 (PROVED): the kernel −Rα is SPD via an identity
  −Rα(A) = κ E_{P_s}|A−μ₁(A)|² + ∫ y^{α−1} τ(y) |E_yA−μ₁(A)|² dy, κ = −2π^{−α}Γ(α)ζ(2α) > 0, s=2α∈(0,1).
  Survives deletion of any finite set of primes (explicitly checked) — this is flagged by the authors
  themselves as *not specific enough* ("Es PSD con radical en indicadores borrados... Así, su
  positividad SOLA no implica Q_T por transferencia").
- LINK_009 through LINK_016: a sequence of increasingly careful negative results about possible maps
  linking this auxiliary kernel to Q_T — non-interpolability by C0 semigroups (LINK_009), a spectral
  moment restriction (LINK_010), an explicit compact Mellin-Gauss map whose domination fails at high
  frequency (LINK_011), an explicit falsifier of that exact-scale domination via an Arb-certified
  numerical test (LINK_012: Q<0.002351 vs E>0.26134, i.e. a NUMERIC falsifier of one specific proposed
  inequality, not of the problem), a proof that **no** fixed constant c>0 independent of T repairs the
  domination (LINK_013, using the CITED rate from Paper 47's thm:margin proof), a proof that dropping
  the rank-one term (κvv*) and reweighting positively still fails uniform domination for the same
  coefficients (LINK_014), resolution of a closability question with an explicit vertical vector
  (LINK_015), and finally a proof that the map U_T has dense range on the whole polar-free carrier for
  every T (LINK_016) — which closes off the possibility that positivity need only be checked on the
  map's image rather than globally.
- Also inside 209: QRH_REPLICA_COHERENCE, QRH_HYPERBOLIC_PROJECTION, QRH_FOUR_FIFTHS_ATTEMPT — these
  are a different side investigation (an attempted adaptation of a "Sept-30" proof toward an exponent
  4/5, feeding directly into phase 210) which gets to a formal minimum exponent 13/15 under one ansatz,
  short of the 4/5 target by 1/15 in a low-exponent parameter; explicitly labeled "no teorema 13/15, no
  barrera universal, no cierre D."
- One housekeeping finding worth noting precisely: the 209 log records a **correction to
  06_OPEN_RESIDUES' own [margin] annotation** — three references had wrongly attributed a *double*-
  exponential ceiling to λ_A, when Paper 47's cor:margin1 only proves a *single*-exponential ceiling for
  λ_A (the double-exponential figure, unverified, is cited only for λ_W, and λ_W ≤ λ_A has the wrong
  direction to transfer it). This was fixed in the index (visible already in the version of
  06_OPEN_RESIDUES I read: the [margin] bullet and the R6 entry both now state this correctly). This
  was a real, consequential mislabel that existed in the record and has since been caught and repaired
  — I did not find it still present, so it is resolved, but worth recording as a documented near-miss:
  had it persisted, it would have let someone wrongly treat an unverified double-exponential bound on
  λ_W as a proved ceiling on λ_A (the actual sign target).

No LINK_* file in 209 leaves a genuinely promising *open* thread beyond LINK_016's observation that
non-continuous forms, other maps, and other T-factors remain "outside" the examined family — stated
explicitly as un-excluded but also as having no next concrete proposal. SYNTHESIS.md's rounds 005-007
describe a parallel, slightly more developed thread (functional equation of Π, contractive module,
explicit sign facts: strict concavity of log τ(e^x), strict anticorrelation Cov_y(1_{d|N},1_{e|N})<0
for coprime d,e>1, negative pairwise prime-factor covariance) that is explicitly flagged "resultado
positivo parcial real" but with the same verdict: positivity of matrix entries is not positivity of the
form, diagonal/same-prime blocks and the exact Q_T link are still missing.

## Hits

(Ranked; "hit" = unrecognized progress toward λ_A(T) ≥ 0 beyond ½log5, or a once-open hypothesis later
proved elsewhere without being connected.)

1. **None found.** No phase among 161-210 contains a result that proves or nearly proves window
   positivity beyond ½log5 without the record already noting it. The ROUTES-TRIED-INDEX's "Live
   residues" list (R1-R10 plus the "Other open items" table) is, on this re-check, internally
   consistent with the phase-level memos: every PROVED sub-result is already scoped by its own memo as
   insufficient (necessary-only, an identity rather than an inequality, scoped to a sub-family, etc.),
   and every such scoping was independently re-derived by an independent audit in the same phase.
2. One housekeeping item that functioned as a near-hit of the "mislabel" type rather than the
   "unrecognized progress" type: the λ_A/λ_W double-exponential ceiling confusion in 06_OPEN_RESIDUES,
   caught and fixed during phase 209 (see above) — not a live issue now, but worth knowing it
   existed, since it is exactly the kind of silent mislabel that could propagate into Paper 47 if a
   future round re-derives it from an un-audited citation.

## Stopped-not-dead

- **Phase 209 (nonlocal kernel), overall goal:** explicitly `blocked` by the goal-tracking tool after
  three unproductive continuations (rounds "after 016"), and the phase's own log insists, repeatedly
  and in writing, that this is not a mathematical NO-GO — only the absence of a next idea. What remains
  to be done, verbatim from the final log entry: "to continue with concrete mathematical work a new
  ingredient is needed (an operator candidate, identity or sign lemma)"; none of the auxiliary PROVED facts (005, 015, 016) supply it.
  This is squarely in the "time/patience" category the task asks about, except here it is the
  investigation's own idea-exhaustion (no more candidates to try), not an externally imposed stop; no
  external stop order is recorded in this file.
- **Phase 202 (exterior plank), residue "layer edges κ_{T+log n}":** flagged "Residue without a
  proposal" at closure — nobody has attempted a bound here; it was noted in passing rather than
  pursued, because the phase's death criterion (a) triggered on a different question first.
- **Phase 205, Lemma RF.1** (n₊(Φ_N) ≥ 1.95T − 2, PROVED-elementary): a true, standing partial result
  that is marked "to be written up" and is not yet cross-indexed in 06_OPEN_RESIDUES' (L2) row by name;
  low priority (gives no sign) but technically an unintegrated proved lemma.
- **Phase 210 / QRH_FOUR_FIFTHS_ATTEMPT candidate scalars** (ℓ=1/5, b=1/10, l_x=7/20, l_y=9/20,
  h=17/20): explicitly marked "pendiente validación global" (pending global validation) — the
  formal minimum 13/15 computation stopped at an ansatz boundary, not at a proof of impossibility;
  this is a live, resumable sub-thread of phase 210, separate from the window-positivity problem
  proper (QRH exponent is a distinct target per MEMORY, not window positivity itself).

## Mislabels

None found that are currently live in the index as read. The one identified instance (λ_A/λ_W
double-exponential ceiling in 06_OPEN_RESIDUES' [margin] note and the R6 table row) was already
corrected by the time of this audit, per phase-209's own log ("Continuation audit after
a015... An obsolete reference in residue file 06 was corrected") — confirmed fixed by re-reading
the current 06_OPEN_RESIDUES_DEAD_SUBROUTES.md, whose [margin] bullet and R6 entry both now state the
correct single-exponential ceiling for λ_A and flag the λ_W figure as unverified-and-non-transferable.
No other mislabel surfaced in the phases inspected (161-210): labels (PROVED/CITED/ARGUED/OPEN/NO-GO)
in 202, 205, 209, 210 match the content of their own proofs/disproofs on inspection.
