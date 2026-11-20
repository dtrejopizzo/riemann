# Audit: phases 100–160 re-read against today's finite reduction (L2)/(N)/(S)

Target recalled: window positivity on $\mathcal D_T$ (Paper 47 eq:symbol/eq:form/eq:W, lines 105–150); open
reduced forms (L2) $S_{T,k(T)}\succeq0$, (N) signed Nyquist Chebyshev coherence, (S) near-coincidence Toeplitz
matrix (lines 10677–10790). No RH-equivalence used anywhere below; phases are read strictly as statements about
the quadratic form $\mathfrak a_T$/$W_T$.

## Method
Read Paper 47 abstract/intro/open-problems (lines 90–160, 10660–10800) and
`05-meta-and-planning/ROUTES-TRIED-INDEX/04_PHASES_100-189.md` Part I (walls W1–W12, falsifiers, phases 185–189
and key 100–161 entries) before opening any phase folder, per the routes-tried rule. Then read phase 153, 155,
156, 160 primary memos (README/closure files already summarized in MEMORY.md) and the phase-160 builder/panel
corpus directly (20 memos C1–C8, M1–M12, plus panel PA–PE, plus round-2 D2/D4 and cycle X_C1).

## Phase-by-phase (100–133: rows A–C, not row-D content)
Phases 100–133 concern rows A/B/C (characteristic cofactor, Ω7 closure, A1 closure, row-A/B/C construction and
closure, ABC review panel) and are outside the window-positivity target; nothing in them states or bears on
$\mathfrak a_T\ge0$ or the finite matrix $S_{T,k}$. No hits.

## Phases 134–152 (row-D opening through method theorems)
- 134–146: canonical class (Pólya), affine duality $\sigma_K$, Hodge-index transfer (conditional on $h^0$),
  trace-cone restatement, function-field model, Frobenius diagonal. These build toward method theorems T1/T2/T5
  (walls W9 in the index) — all NO-GO for stated method classes (field-uniform proofs, axioms A1–A6, Deligne L²
  moments). None computes or bounds $S_{T,k}$ or the Nyquist coherence $\mathcal C_T$; they predate those objects
  by ~15 phases. No hit, no mislabel found on inspection: T5 is explicitly labeled "NO-GO (PROVED, trivial)" in
  the index, which is an honest label (it proves L² moments can't isolate one fibre, not that T5 fails to exist).
- 147–152 (Galois ring, single-prime tower, mixed effectivity, additive pencil, method theorems T3/T4/T5, the
  bridge, "new approach" survey of FUP/Berkovich–Poineau/Dolgopyat–Mayer): all DEAD/NO-GO per the index (P149
  "DEAD, inherits rationality wall"; P151 "DEAD, dlVP capped"; P152 "DEAD, both overstated"). These are generic
  qualitative/geometric routes, not finite-matrix computations; no connection to (L2)/(N)/(S) to re-examine.

## Phase 153: first sign-carrying theorem (D.12-α at log 2)
Closed with Theorem A (deformation calculus of the falsifier family $\Xi_a$) proving sign at
$T=\{\infty,2,3\},\log 2$; rounds on single-pair/needle leads closed negative (P153.2, P153.3 left open).
Phase-160 memo M3 revisits Theorem A "at large $T$" and finds it is EQUIV-tagged beyond the base case, i.e. the
deformation calculus does not transfer new sign information past log 2 without already assuming the target. No
unrecognised result found: the phase-153 record is consistent with the index's F-Ξ_a falsifier entry (falsifies
Hodge transfer/h⁰, not a positive route beyond log 2). Checked explicitly for a silent (S)-shaped near-coincidence
argument in R153_012; none present — the memo's matrix is on $\Xi_a$ test data, not the Toeplitz-in-$\log(m/k)$
matrix of (S).

## Phase 155: class-dependent value bounds / flat kernel criterion
This phase is the closest fit to (L2)/(N) read retrospectively, since it builds lattice certificates and
coercivity thresholds at the same windows ($\frac12\log3$, $\frac12\log5$) that (L2) parametrizes by contact
count $k(T)$.
- Theorem N/N′ (NO-GO, lattice certificates at $\frac12\log3$, $M\le8$, and two-prime windows $M\le24$): this is a
  **class impossibility** for lattice certificates, not for the Schur-complement object $S_{T,k}$ of (L2). (L2)
  is not a lattice certificate — thm:coer-schur produces $S_{T,k}$ from piecewise Tate exponentials on
  $\mathcal V_k$, a different (larger, non-lattice) test space. So thm:N/N′ does not bound or refute (L2); it was
  correctly scoped by Paper 47 as a separate problem (Problem~\ref{prob:A}), and the routes index correctly
  labels it "NO-GO (class impossibility)" rather than mislabeling it as bearing on (L2). No hit.
- Theorem AL (retracted) → AL′ (Θ(1/M)): same scoping — about lattice certificates, not $S_{T,k}$.
- round 5: "RH ⟺ Kreĭn indeterminacy" language appears in MEMORY.md's historical summary of phase 155 but is a
  restatement (thm:KEPdich, REF-D in the index), not a numerical result; it is not used here and carries no
  information toward (L2)/(N)/(S).
- Archimedean thresholds ($T^*_{\infty,P}\in[0.58,0.60]$, necessity at $\approx0.596$): these are bounds on the
  archimedean part $\lambda_{\infty,P}(T)$ alone (coercivity of Theorem thm:coer-B), i.e. exactly the ingredient
  that fixes $k_0(T)$ in (L2)'s statement ("$k(T)\ge k_0(T)$ ... archimedean form is coercive on $\mathcal V_k$").
  This is a genuine *tool* still load-bearing for (L2) (it is cited in Paper 47's own statement of (L2)), but it
  is already correctly folded into the current open-problem statement — not an unrecognised result, just the
  known input.

## Phase 156: per-window converse
MW-5 reduces to OT-5′; adèle class space shown to be a restatement, not a new object; no survivor "with an
object" found; converse (positivity $\Rightarrow$ no comb counterexample) is a 2×2 polar-capacity condition and
**fails in comb models** (F-comb falsifier, R156 "FALSIFIES per-window converse, (C2) from T≈0.38" per index).
This is a negative result about the converse direction, not about (L2)/(N)/(S) directly, and is correctly scoped
(T1 allows field-uniform proofs is the one surviving positive fragment, already carried forward). No hit.

## Phase 157–159 (mechanism search, MW-5 object, two-front construction)
Per the index (W10 MW-5/OT-5′: "every carrier postulates positivity; frame defect holds even over F_q" — NO-GO)
and R157/158/159 entries scattered through Part I-c (R158_001, R159 not separately tabled but feeding directly
into the phase-160 brief, which is the authoritative digest). Nothing here anticipates the Schur-complement
object of thm:coer-schur (that theorem postdates phase 160, cited in Paper 47 §on coer-Schur, built after R186 in
phase 162+); phases 157–159 could not have recognised (L2) in its current form since the finite reduction did not
exist yet. No hit.

## Phase 160: 20-builder survey + 5-panel audit, round 1 (complete) + round 2 (partial, then stopped)

### Builders stopped by the owner for lack of progress vs. for a mathematical reason
The historical record (MEMORY.md: "STOPPED 2026-09-26 by owner (no progress seen); last file R160_X_C1.md") is
accurate on inspection: round 1 (all 20 memos C1–C8, M1–M12) and its five panel reviews (PA–PE) **did complete**
and each panel scored every memo as RESTATEMENT or PARTIAL_NEW with scores 0.15–0.35 (0–1 scale, 1 = a proof of
G1/G2) — i.e., every memo received a *mathematical* verdict (restatement of Weil's criterion, EQUIV-tagged, or a
genuine but sign-free structural theorem), not a stopped-for-resource-limit verdict. Round 2 built only two of the
twenty slots (D2, D4), both closed by their own authors (R160_D2_R2 Thm Z; R160_D4_R2 Thm 5.1, per the index), and
a half-finished cycle (R160_X_C1, Route N: Carathéodory–Fejér/Connes–van Suijlekom rigidity on the first-contact
state) that reached a verdict section but was the last file before the stop. So:

- The **owner's stop was administrative** (quota/resource exhaustion risk per R160_HANDOFF.md: "running 20 memos
  at maximum effort exhausted the resource limit within the first round"), not a judgment that the surviving
  ideas were dead. Two threads were left genuinely open when the campaign paused:
  - **D2, D4** (round 2 slots): both already closed negatively by their own authors — not casualties of the stop.
  - **Route N / R160_X_C1** (Connes–van Suijlekom rigidity applied to the first-contact state, no limit taken):
    this memo's own §0 argues the route is structurally different from the Doc 99 (phase 35) use of the same
    rigidity tool (which "dies at the limit") because it is applied to a *finite-window* bottom-of-spectrum
    object via phase 121's first-contact-state result, so no limit is needed. The memo was mid-argument (through
    §0.1, listing why alternatives D1/D3/D5 are excluded) when the campaign stopped — this is the one idea in
    the 20-slot campaign whose closure is **not yet on record** one way or the other, administratively orphaned
    rather than mathematically resolved.

### Per-memo verdicts (two lines each), all PARTIAL_NEW/RESTATEMENT per panels PA–PE, none bearing a sign:
- **C1** (Connes profile, laminated carrier): object is $[other:\mathcal H^1]$, not $\mathfrak a_T$ or $W_T$ on
  any window; explicitly "no statement in this file is about $W_T$ or $\mathfrak a_T|P_T$." Not comparable to (L2)/(N)/(S).
- **C2** (Connes–Moscovici prolate boundary triples): no sign claimed; ties to the Sonin count, already folded
  into the semilocal Sonin chain (R186, phase 183-186) which proved PROVED-but-no-sign.
- **C3** (Meyer/Scholze nuclear carrier): escapes Hilbert-domain obstruction structurally, no positivity structure realized; no sign.
- **C4** (Borger Witt square): PB panel verdict RESTATEMENT (score 0.15) — Thm B is Weil's real-place density
  rewritten; Thm D is thm:A rewritten. Correctly scored low; not a hit.
- **C5** (Bost/Zhang extremal coupling): PARTIAL_NEW (0.30); every positivity statement is EQUIV or void by the
  memo's own admission; one real new result, Thm 5.2(c) $\lambda_{\min}(\mathfrak a_T|L^2(I_T))\le -4T+O(1)$ —
  an upper bound on the *negative* side, i.e. not usable toward (L2)/(N)/(S) positivity.
- **C6** (Consani $Sh_Z$ lattice): PARTIAL_NEW (0.35); sign step is von Koch's criterion in disguise (OT-5′
  failed by its own §8); genuinely new side-results (Thm Q+Lemma L on $B_\infty(T_0)$) do not touch the finite
  reduction.
- **C7** (Huh, Hodge–Riemann on intersection form): no sign for $\zeta$ claimed beyond record; pure structure.
- **C8** (Deligne/Tate phase datum, $\varepsilon$-factors): "no object that passes OT-5′ and no sign" — exact negative self-report.
- **M1** (Tao, Problem B as a family): two uncertified float sanity checks only; the canonical column $s=\tfrac12$
  tested as a family is new methodologically but delivers no bound on $S_{T,k}$ or $\mathcal C_T$.
- **M2** (Green, variational characterization of $\Lambda$): PROVED contact-cone lemma (0 interior to
  $\mathrm{conv}\,\kappa_T(\mathcal P_T)$) — a genuine [prim] theorem, but it is a convexity statement about the
  comb polytope, not a value of $S_{T,k}$ or the Nyquist coherence; already the right scope (G2 mechanism, not sign).
- **M3** (Bombieri, Theorem A at large $T$): EQUIV-tagged (flagged explicitly) — the one place in the 20 memos
  that is honestly marked as reducing to the target itself rather than proving anything toward it.
- **M4** (de Branges/Sarnak, polar capacity across $T$): structural identity for the Schur complement
  $\mathfrak G_T = S^{Sch}_T+J$ — this is the complete-form sibling object to (L2)'s $S_{T,k}$, built independently
  in the M4 memo before Paper 47's thm:coer-schur existed. **Worth flagging**: M4's $\mathfrak G_T$ identity and
  the later thm:coer-B/thm:coer-schur machinery (cited in Paper 47 (L2)) look like independent constructions of
  structurally the same Schur-complement object; no memo in phase 160 or later cross-references M4 against
  thm:coer-schur. This is not a proof gap closed, but it is a candidate for a genuine *tool* re-use that was not
  cross-checked — listed below as a Hit (weak).
- **M5** (Montgomery, Gaussian prime correlation heat flow): EQUIV on every statement — fully circular by its own labeling.
- **M6** (Maynard, self-scale evaluation): Theorem D states the "missing prime side" (Rigidity 153.M) is **false
  for $\zeta$ under RH** and its repair restates Conjecture 144.D — internally consistent negative result, not usable.
- **M7** (Iwaniec–Friedlander, bilinear cancellation): "the Friedlander–Iwaniec door is not inside any Weil form" — clean negative.
- **M8** (Schur square of the Weil distribution): finishes "Missing Lemma 5.2" as a theorem but the resulting
  object is "sign-faithful and sterile": positivity on every natural class is equivalent to the target itself (E1-shaped, i.e. REF-D).
- **M9** (Deligne/Katz amplification): no sign in either form; pure [meth]/[other] content.
- **M10** (Bakry–Ledoux Doob generator, $\Gamma_2$): PARTIAL_NEW; full-line Doob form only, window recovery "by
  restriction only... no window statement is made" — does not reach $\mathfrak a_T$ or $S_{T,k}$ despite superficially relevant curvature language.
- **M12** (Euler–Poisson–Harnack, entropy $\times p$): new coordinate system (Theorem 2.1, $\Lambda=\mu*\log$ as a
  harmonic-function value difference) but "not to a sign," per its own verdict.

## Hits (ranked)

1. **(weak) M4's $\mathfrak G_T=S^{Sch}_T+J$ identity vs. Paper 47's thm:coer-B/thm:coer-schur $S_{T,k}$.** Both
   are Schur-complement constructions on the same window object, built in different campaigns (phase 160 round 1
   vs. the machinery cited in the (L2) open problem), and no document cross-checks whether M4's structural
   identity for $\mathfrak G_T$ (complete form) gives any extra leverage on bounding the *least eigenvalue* of
   $S_{T,k}$ beyond what thm:coer-schur's own sandwich inequality $\lambda_A\le\lambda_S\le(1+\|\mathsf K\|)^2\lambda_A$
   already supplies. This is not a proof or near-proof of (L2); it is a candidate tool-reuse worth one
   verification pass (does $\mathfrak G_T$'s identity sharpen the uncontrolled $\|\mathsf K\|$ term in
   Corollary margin1?) before being filed as nothing.
2. **(administrative, not mathematical) R160_X_C1 / Route N** (Carathéodory–Fejér / Connes–van Suijlekom rigidity
   applied without a limit to the finite-window first-contact state of phase 121 / R157_004 O4) was mid-argument
   when phase 160 was stopped for resource reasons, not resolved negatively or positively. If the owner wants a
   genuinely unclosed 2026-09 thread reopened, this is the one candidate — note it is NOT yet in the routes-tried
   index as closed, so per the owner's rule it is **not barred from a fresh attempt**, provided a written reason
   is given for why finite-window rigidity escapes the "dies at the limit" failure mode of Doc 99's use of the
   same tool (the memo itself gestures at this reason in its §0.1 point 4, but never completes the rigidity argument).

No candidate was found in phases 100–160 that proves or comes close to proving $\lambda_A(T)\ge0$ beyond
$\frac12\log5$, or that materially pre-dates/duplicates the (S) near-coincidence matrix or the (N) Nyquist
coherence bound.

## Mislabels
None found. Every DEAD/NO-GO/RETRACTED/REF-D label checked above (T5, thm:N/N′, thm:AL→AL′, F-comb, M8's
sterility, C4–C9 panel scores) is backed by an explicit reason in the cited file that matches the outcome word
used, and no PROVED label was found attached to a claim that doesn't hold up (M2's contact-cone lemma is the only
PROVED in the sampled set and it is a true, narrowly-scoped convexity fact, correctly not oversold as bearing on sign).

## Phase-160 builder list (as requested), idea in two lines each
See full list under "Per-memo verdicts" above; repeated here compactly:
- C1 Connes: laminated/leafwise Hodge carrier, no compactness — object not a window form, no sign.
- C2 Connes–Moscovici: prolate boundary triples + Sonin count — no sign.
- C3 Meyer/Scholze: nuclear rigged carrier, positivity defined pre-spectrum — no sign.
- C4 Borger: Witt square archimedean correction = Coulomb kernel — RESTATEMENT (Weil's density rewritten).
- C5 Bost/Zhang: extremal archimedean coupling via Example E — PARTIAL_NEW but EQUIV/void; gives a negative lower bound only.
- C6 Consani: $Sh_Z$ lattice heat completion — sign step is von Koch's criterion in disguise.
- C7 Huh: Hodge–Riemann residue on arithmetic intersection form — pure structure, no sign.
- C8 Deligne/Tate: $\varepsilon$-factor phase datum — explicit self-report of no object, no sign.
- M1 Tao: Problem B as a family, canonical column $s=\tfrac12$ — two uncertified float checks only.
- M2 Green: variational/comb-polytope characterization of $\Lambda$ — PROVED contact-cone lemma, no sign.
- M3 Bombieri: Theorem A ($\Xi_a$ deformation) at large $T$ — one EQUIV statement, flagged as such.
- M4 de Branges/Sarnak: polar capacity $\mathfrak G_T$ across $T$, Kreĭn sets — structural identity, no sign (see Hit 1).
- M5 Montgomery: Gaussian prime correlation as heat flow — EQUIV on every statement.
- M6 Maynard: self-scale evaluation — one missing-prime-side claim proved FALSE under RH.
- M7 Iwaniec–Friedlander: bilinear cancellation against $W_T$ — explicitly not inside any Weil form.
- M8 Deligne/Tate (Schur square): finishes Doc 106 Missing Lemma 5.2 — resulting object sign-faithful and sterile.
- M9 Deligne/Katz: amplification over Spec Z — no sign in either form, pure method content.
- M10 Bakry–Ledoux: Doob generator / $\Gamma_2$ curvature — full-line only, no window statement.
- M12 Entropy $\times p$ / Euler–Poisson–Harnack: new coordinate system for $\Lambda$ — not to a sign.
- (round-2) D2, D4: closed negatively by their own authors.
- (cycle, unfinished) X_C1 Route N: Carathéodory–Fejér/Connes–van Suijlekom rigidity on the finite first-contact
  state, no limit — stopped mid-argument by the resource-exhaustion pause, not resolved (see Hit 2).
