# Phase 210 — From 7/8 to 4/5: a zero-free half-plane Re s > 4/5

Target: prove that every finite-order Hecke L-function over Q(√−3), hence every Dirichlet
L-function and ζ, has no zero in Re s > 4/5. The starting point is the two OpenAI preprints
archived in `00-references/qrh-preprints/` (11/12 and 7/8; neither is refereed) and the
phase 209 notes on them. This phase is independent of row D: a zero-free half-plane gives no
sign for the window form, and nothing here is counted toward D.

## What phase 209 established

- The 11/12 proof of the short preprint rests on a mean square over H = D^{1+ϑ} rows of
  sextic-twisted Möbius sums and a transfer to the untwisted sum through the sixth-power rows
  p⁶. With that transfer the exponent is θ = ½ max{1 + 5h/6, 2 − h/3} for H = D^h; it is
  11/12 at h = 1 and would be 6/7 at h = 6/7 if the mean square held there, which is not
  proved (QRH_EXPONENT_MAP, QRH_REPLICA_COHERENCE).
- In the 7/8 manuscript, keeping the chain of low bounds of Section 15 and changing only the
  probe geometry (ℓ, b, l_x, l_y, h) cannot go below 13/15 (QRH_FOUR_FIFTHS_ATTEMPT). The
  candidate geometry ℓ = 1/5, b = 1/10, l_x = 7/20, l_y = 9/20, h = 17/20 passes the low
  estimate (11/60) but the high certificate fails by 49/1500, and the plain moment Lemma 18.1
  is stated only for κ ≥ 3/4 (QRH_HIGH_CANDIDATE_AUDIT).

So 4/5 requires at least one new estimate, not a new choice of parameters.

## Plan

1. **Ledger.** An exact exponent ledger of Part II of the 7/8 manuscript: every inequality
   that enters the low estimate (Prop. 15.3), the local compensation (Prop. 16.1), the two
   moments (Lemmas 17.1, 18.1), the row counts (Prop. 19.2) and the final certificate
   (Lemma 20.2, formula (20.4)), with the exponent it costs and the hypotheses it needs.
2. **Requirement theorem.** Treat the geometry and the moment exponents as free variables and
   determine which improvements of which estimates would certify 4/5 with the same
   architecture. The outcome is a short list of concrete target inequalities, each labelled
   parameter choice / extension of an existing lemma / new theorem.
3. **Alternative architecture.** In the short preprint, replace the trivial transfer error
   O(D/Y) by the Möbius sum of length D/q it actually is and bound it recursively. This
   removes the second branch of θ(h), so the exponent becomes ½(1 + 5h/6) and 4/5 corresponds
   to a mean square over H = D^{18/25} rows: below the diagonal. The obstacle there is
   located precisely (the term 𝓗²/X of the quadratic large sieve in the dual).
4. **Attack** the most tractable target inequality from steps 2–3, one estimate at a time,
   each with an independent hostile audit.

Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO. The preprints' results are
CITED, not PROVED here; nothing in them has been audited line by line.

## Results of the first round

- **Theorem R** (RECURSIVE_TRANSFER_001, PROVED conditional on MS(α), audited): in the
  11/12 architecture, replacing the trivial transfer error by the exact identity
  A_{p⁶}(D) = Σ_j ν(p)^j A_1(D/N(p)^j) and an induction gives θ = ½ + 5α/12 whenever the
  mean square holds over D^α rows. 4/5 corresponds to α = 18/25. But the proof of the mean
  square in the short preprint needs H > D (Proposition 2: the dual target is false below the
  diagonal), and the part of MS(α) that Theorem R uses is equivalent to its conclusion. So
  MS(α) for α < 1 is not an easier intermediate statement.
- **Ledger** (LEDGER_001, arithmetic verified): formula (20.4) and the certificate 49/440640
  reproduced. The load-bearing exponents are the low bound l_x/2 + b/12 (with the Lemma 15.1
  loss), the floor-bin constant 2/3 + b/6 + ℓ − σ₀ (rows at U = Z^h bounded by trivial count
  and absolute values) and the row exponent R ≥ 1 − δ.
- **Moments** (MOMENTS_001): both moments are diagonal bounds, sharp up to Z^ε; κ ≥ 3/4 in
  Lemma 18.1 is used in one line and the proof works for κ > 1/2 (extension routine,
  CONDITIONAL on the unaudited remainder); the extension does not touch the floor deficit.
- **Requirements** (REQUIREMENTS_001): with all estimates unchanged the infimum of the
  architecture is σ_inf ∈ [0.87489, 7/8], so the published geometry is optimal to 4·10⁻⁵;
  13/15 is the infimum only with ideal counts. For σ₀ = 4/5 the deficits are
  (s_low, s_high) = (3/40, 3/40) at ℓ = 1/6. Targets: (T1) a bilinear low bound beyond
  Cauchy–Schwarz in (6.2); (T2) a signed bound for the floor rows at U = Z^h; (T3) R = 1 − δ
  on all bins (never sufficient alone). T1 and T2 are signed mean values whose unsigned
  versions are sharp: new theorems, of a different type from MS(18/25).
- Audit AUDIT_210_001: all three memos confirmed, one base-case gap in Theorem R repaired,
  "equivalent to MS(18/25)" corrected to "implied by".

Status of 4/5: OPEN. No progress on a proof; the obstacles are now located.

## Documents

- `BRIEF.md` — working rules and sources for every memo of this phase.
- `LEDGER_001.md` — step 1.
- `REQUIREMENTS_001.md` — step 2.
- `RECURSIVE_TRANSFER_001.md` — step 3.
- `MOMENTS_001.md` — the two moment estimates: ranges, contraction, terminal bounds.
- `AUDIT_210_001.md` — hostile audit of the round.

## Suggested reading order

`README.md` → `LEDGER_001.md` → `REQUIREMENTS_001.md` → `RECURSIVE_TRANSFER_001.md` →
`MOMENTS_001.md` → `AUDIT_210_001.md`. All memos are in English; there are no scripts.

## Relation to other phases

Phase 209 holds the first reading of the preprints (QRH_* files). Rows A–D are untouched.
