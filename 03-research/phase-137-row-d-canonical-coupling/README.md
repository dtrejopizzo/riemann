# Phase 137 — the coupling of the canonical class with the Frobenius lattice (row D)

Report + audit rounds, following phase 136's map and plan. Rules: no sign claimed or assumed;
nothing defined through the location of the zeros; `ξ` admissible as data; every statement labelled;
every theorem run against `Ξ_a`; numerics only where a constant must be certified, and then with a
stated robustness margin (never called interval-safe: the Lipschitz constant is sampled).

| file | round | content | status |
|---|---|---|---|
| `R137_000_BLUEPRINT.md` | 0 (blueprint) | tasks D.0, D.11–D.14 | issued |
| `R137_001_ROUND1.md` | 1 (report) | D.0 audit; D.11–D.13; blueprint refutations | delivered; **superseded in part** — see its header banner and `R137_003` |
| `R137_002_AUDIT.md` | 2 (audit) | H1–H20; two `FATAL`, thirteen `MAJOR`; verdict CONFIRMED WITH REPAIRS; ruling: do not append Part III | delivered |
| `R137_003_ROUND2.md` | 2 (report) | all twenty findings **accepted**; H1 repaired analytically (`u_0 ≤ 0.2422553` proved, `β = 5.1`, threshold `4 538 961`); H2 repaired by **withdrawal** of the `Ξ_a` comparison and everything on it; the R3 text of phase 65 read and the `REFUTED` verdict re-run against it; the zero-free-region-free route worked out and shown to **fail**; four downgrades; D.14 gate reassessed | delivered |
| `R137_004_CONFIRMATION.md` | 3 (audit) | D.11, D.12, D.13 and the pre-R3 half of D.0 **CONFIRMED**; one `MAJOR` residue `N1` (the R3 reading), minors `N2`–`N7` | delivered |
| `R137_005_ROUND3.md` | 3 (report) | **`N1` decided: outcome (A)**. R3 point 4 *does* supply L1 for the sourced matrix `G_P^∘` (verified from source) and the shorting preserves it — but R3 point 1 withdraws the limit identification for that very object, and R3 point 3 applies Vitali to the renormalized **trace** `M_P`, whose Nevanlinna mass no source-frame bound bounds. **Neither object carries both premises** (Prop. 1.1, the fork). `Ξ_a` run on point 4: transfers, so point 4 is not load-bearing; `Ξ_a` fails **G4** (four polar points, not rank one), and the falsifier family of G4's shape is **not empty** (every Dedekind zeta `ζ_K` has it: simple pole, positive atoms, functional equation) but contains **no member with proven off-line zeros** — so the test cannot adjudicate; corrected in `R137_006` (N9). `N2`–`N7` repaired, `N4`/`N5` by proving the missing statement | delivered |
| `R137_001b_PART_III_DRAFT.md` | 1–2 (report) | Paper 47 Part III (§§17–19) as a **draft**; **not appendable this round** (protocol; the (X19) zero-location import would need Paper 47 §1.13 amended; one `CANDIDATE`) | draft |
| `cc_2006.13771_text.txt` | — | Connes–Consani, *Weil positivity and trace formula: the archimedean place*; all `[cc:NNN]` citations are line numbers of this file | source |
| `scripts/d137_lattice.py` | 2 | rewritten: `u_0` and the kernel bound are now **theorems** (`R137_003` Lemmas 2.1–2.2) and the script only verifies them; `C2` now probes `[0.235, u_0)`, the interval round 1's check was blind to; `M_+ ≤ 17` certified by grid + Lipschitz margin over the whole interval. `--fast` ≈ 32 s; run of record ≈ 3 m 42 s, exit `0`, all checks pass; `--fast` and the full run report the **same** constants. `M_+ ≤ 17` is robust: it holds for any `L ≤ 460` against a sampled `L ≈ 101.5` | passing |

**Surviving results of the phase so far.** `RH-PROOF.md` localized and `REFUTED` in both its versions — the
pre-R3 half at `L1`, the R3 half at the **fork** between the sourced matrix (bound, no identification) and
the renormalized trace (identification, no bound);
the two-sided Mellin bound (Thm D.11.1); non-vacuity of `H⁰_Z(mK)` with a certified threshold (Thm
D.11.2′); `h⁰_Z(mK) ≥ c(\log m)^{3/2}/\log\log m` (Thm D.11.3); a coefficient bound and the first explicit
bound on Lemma 13.5a's `ρ_Q` (Thm D.11.4′); (c) `⟹` `Q(m) ≫ m\sqrt{\log m}` (Cor. D.11.5′); the sign
correction of the blueprint's `W_S` and the support decoupling (D.12); the exact identity `Q = Π` (D.13).

Cross-file effects: a header note in `03-research/phase-65-signature-continuity/RH-PROOF.md` (placed
**after** its R3 banner, auditing both versions), and an entry in `NO-GO-LIST.md` under
"[phase 137] audit of phase-65 RH-PROOF.md" (both rewritten in round 2).

## Record note (from the audit review of LaTeX Paper 43)

Paper 43 `main.md` sourced the *continuity* of the crossed-product Hochschild
decomposition (label-γ Koszul collapse; Thm 7.1(a) in the md numbering) to
P123.121 and P123.123. The audit checked both notes: P123.121 contains no
Hochschild computation (it supplies the coefficient algebra and the
temperedness of the actions, i.e. hypotheses); P123.123's result (11) is the
derived monoidal transport of crossed products along a tensor product, a
different statement. The algebraic decomposition is classical (Nistor,
Getzler–Jones, Brylinski); its continuous form for the rapid crossed product is
**not proved anywhere in the corpus**. In the LaTeX Paper 43 it is stated as
Hypothesis 5.9; dependents are exactly Theorem 5.10(a) (Hochschild shadow),
Corollary 5.12 (blindness) and Proposition 13.10; the trace, symbol, numerical
theory, Banach algebra, charts, effectivity, Riemann–Roch, classical model and
signature are independent of it. Consequence for the row-A record: clause A.5's
"blindness of the Hochschild shadow" is CONDITIONAL on this continuity until it
is proved; the clauses actually load-bearing for rows B–D (trace, symbol, `c=0`,
Tate sequence, rulings, `𝓐_tr`) are unaffected. To be reflected in Paper 43
`main.md` and in the row-A label line at the next record pass.

**Update :** the continuity is now proved (LaTeX Paper 43,
Proposition `prop:crossed`, Koszul bimodule resolution with height-weighted
contractions), so A.5 is no longer CONDITIONAL; the Hom transfer `Tr` is also
proved (Proposition `prop:hom`, with `E_R` on `R^×`). Reflected in Paper 43
`main.md` and README.

## Other files in this folder

- `R137_007_CLOSING_DECISION.md` — Closing decision, phase 137 (row D, canonical coupling).
