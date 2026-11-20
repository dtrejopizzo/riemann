# Brief for phase 210

Goal of the phase: a rigorous proof that finite-order Hecke L-functions over Q(√−3), Dirichlet
L-functions and ζ have no zeros in Re s > 4/5, by extending the method of the archived
preprints. Row D is not involved; no statement about the window form or its sign belongs here.

## Sources (read them; do not paraphrase from memory)

- `00-references/qrh-preprints/openai-qrh-seven-eighths.txt` — 199 pages, text extraction of
  the 7/8 manuscript. Part I = Sections 3–11 (11/12 by probe and continuation). Part II =
  Sections 12–20 (7/8). The final combination is Section 20: Lemma 20.1 gives the row-bin
  exponent E(d) in formula (20.4); Lemma 20.2 is the endpoint certificate; Proposition 20.3
  orders the choices. The two moments are Lemma 17.1 (inverse polynomial, marked) and
  Lemma 18.1 (plain polynomials, κ ∈ [3/4, 1]). Row counts: Proposition 19.2. Low estimate:
  Proposition 15.3. Local compensation: Proposition 16.1. Continuation principle: Prop. 2.1.
- `00-references/qrh-preprints/openai-qrh-eleven-twelfths.txt` — 49 pages, the short 11/12
  proof: Proposition 3.1 (mean square over H = D^{1+ϑ} rows), (2.4)–(2.5) and (3.2) (the p⁶
  transfer), Section 4 (Poisson), Section 5 (iteration), Proposition 5.2 (completed mean
  square, bound 𝓗 + 𝓗² N(f)/X), Proposition 5.4 (transfer by two Poisson summations).
- Phase 209 notes: `03-research/phase-209-nonlocal-kernel/QRH_*.md` (in Spanish; read
  QRH_EXPONENT_MAP, QRH_FOUR_FIFTHS_ATTEMPT, QRH_HIGH_CANDIDATE_AUDIT, QRH_REPLICA_COHERENCE).
  Do not repeat what they prove; cite them.

## Rules

1. Pen and paper. Every exponent computation written out so that a reader can check it.
2. Labels on every claim: PROVED (here, in full) / CITED (from a source, with the exact
   statement number) / CONDITIONAL (on what) / ARGUED / OPEN / NO-GO. Never upgrade a CITED
   statement to PROVED. The preprints are unrefereed: when a lemma is used, quote its
   hypotheses, including the ranges of parameters, and check that they are met.
3. Never change a published statement's range silently. If a lemma is stated for κ ≥ 3/4 and
   you need κ = 3/5, say so and classify the need as "extension of Lemma X" with a note on
   where its proof uses the range.
4. English, mathematical register, written as a research note by a person. No dates, no
   author lines, no names of AI models or companies in the body, no process words (builder,
   reviewer, session, prompt, owner, user). The preprint authors are cited as
   "the 7/8 manuscript" / "the short preprint".
5. Do not edit files outside this phase folder. Do not touch
   phase 209.
6. Before proposing an estimate, check the index `05-meta-and-planning/ROUTES-TRIED-INDEX/`
   (entries L74 and the phase 209 section) and the phase 209 notes.
7. Memo format: title; one paragraph stating the result and its label; numbered sections;
   a final section "What this does and does not give" with the honest status of 4/5.
   Length as needed, no padding.
