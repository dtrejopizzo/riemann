# R153.000 — Blueprint, phase 153 (row D): does the certified endpoint carry sign?


## 0. Why this phase, in one paragraph

The corpus's only unconditional Weil-positivity theorem with primes coupled is Paper 42 Thm `thm:certifiedendpoints`
(`main.tex:4164`): `A_T ≥ 0` on the primitive space `P_T` for all `0 < T ≤ log 2` (contacts `{2,3}`), by the
Directed Feshbach lemma plus the exact capacity identity D.76 for one near-null direction `v1` (Rayleigh value
`±1.7·10⁻⁶`, margin `8.63·10⁻⁸`; phase 118 `W4_CERTIFIED_RANGE.md` §2(e)). Connes–Consani's positivity
(2006.13771 Thm 1) is archimedean only, support `[2^{-1/2},2^{1/2}]`, i.e. `T = ½ log 2`, where **no prime enters**.
Phase 137 (R137_001 §3, R137_007) wrote the dictionary and left the acceptance test open:

> **D.12-α (OPEN).** Exhibit finite `(S,T)` with `W_S ≥ 0` for `ξ` and `W_S^{(a)} < 0` for the falsifier `Ξ_a`
> on the same support class. Any sign-carrying semilocal theorem must exhibit such a pair.

Nobody has run D.12-α on the certified endpoint itself. If `(S,T) = ({∞,2,3}, log 2)` satisfies it, the log 2
certificate is the first theorem of the programme that **carries sign** (distinguishes `ζ` from a function with
off-line zeros at finite `T`), and the corpus is ahead of CC in substance, not only in range. If it does not,
the certificate is archimedean domination (Yoshida Lemma 2 quantified) and the honest map says so.

## 1. Corpus facts the construction must not rebuild (read them)

- Setup of `A_T`, `P_T`, `m_0`, `G_{Γ,T}`, Directed Feshbach lemma, Thm certifiedendpoints, Remark yoshidacalibration:
  `04-papers/42-arithmetic-lefschetz-programme/main.tex:4072-4230`. Certificate notes and scripts:
  `04-papers/42-arithmetic-lefschetz-programme/certificates/row_d_log2/` and
  `03-research/phase-114-closing-the-four-rows/114_d_77_*`, `114_d_58_YOSHIDA_ENDPOINT_KERNEL_AUDIT*`.
- Margin decomposition, near-null `v1` (even, boundary-concentrated), failed `½ log 5` extension (two cross terms
  never computed): `03-research/phase-118-the-exact-threshold-inequality/W4_CERTIFIED_RANGE.md` §§2–5.
- Phase 119 README: `A_T ≥ 0 ∀T ⟺ RH` (Weil/Yoshida/Bombieri); no extra arithmetic input claimed.
- `Ξ_a` falsifier and its four substitutions (Prop. 12.6 of Paper 47 `04-papers/47-intersection-frame-defect/archive/main.md`; grep
  `Ξ_a`, `Proposition 12.6`): coefficients `Λ(n)(n^a+n^{-a})`, doubled archimedean block, four polar points
  `0,1,±a`-shifted; zeros at `Re s = ½ ± a`. Also Epstein `Ξ_Q` (T2, phase 150 R150_003) and Beurling (T3).
- Phase 137: `R137_001_ROUND1.md` §3 (D.12: first unpaid term at `2T = log 2` is
  `2(log2)2^{-1/2}(F⋆F^∨)(log 2)`; Doc 135 purity NOT APPLICABLE; D.12-α, D.12-β), §4 (D.13 dictionary: CC pay only
  the archimedean obstruction; CC's vanishing condition vs primitivity), `R137_007` §1. Phase 138 audit H7 (CC
  Thm 1 needs `ĝ(i/2)=ĝ(0)=0`; Thm 6.11 removes the latter at cost `−c|ĝ(0)|²`, `13<c<17`).
- Phase 46 Doc 142 (`03-research/phase-46-audit-and-attacks/142-attack-on-gap-135-b-the-semilocal.md`): archimedean
  domination threshold is absolute `O(1)`, does not scale with the conductor; `X_S^{ar}` violates positivity for
  long support for every finite `S` (deficit `Ω(0) − B_S ≈ −11.72` for `S={2,3}` in that normalization);
  GAP-142.A. Phase 106_10: absolute prime control is only `O(1)`.
- Paper 42 `main.tex:6330-6360`: deficit window `Ω_Γ = (−τ_Γ, τ_Γ)`, `g_Γ(τ_Γ)=1`, `τ_Γ = 0.2860886…`, and
  band-coherence corollary with the sharp first-band width `log(3/2)`.

## 2. The three questions (all new after the grep of §1)

**Q1 — D.12-α on the certified endpoint (the sign test).** Define `A_T^{(a)}` = the `Ξ_a` analogue of `A_T` exactly
by Prop. 12.6's substitutions (state it with the four-moment primitive space `P_T^{(a)}` and the doubled
archimedean block; check the normalisation against `a → 0`, where it must equal `2A_T` on the ξ²-primitive space —
note the ξ² space has doubled polar order; say precisely what `P_T^{(a)}` is as `a→0`). Determine, for `T = log 2`
and `T = ½ log 3`: is there `a ∈ (0, ½]` with `A_T^{(a)} ≱ 0` on `P_T^{(a)}`? Method: exhibit a single explicit
test function `F_a` with negative Rayleigh quotient and certify the sign of the quotient (interval arithmetic
on one number; `mpmath.iv` or `python-flint` acceptable). If found: `PROVED`, D.12-α answered with
`(S,T) = ({∞,2,3}, log 2)` (or `{∞,2}`, `½ log 3`), and the certificate carries sign. If, for every `a`, Galerkin
diagnostics show `A_T^{(a)} > 0` with clear margin: state `OPEN` with the diagnostic table and explain the
mechanism (the four-moment constraint shrinks the space; the weight growth `(n^a+n^{-a})` is only `≤ 2.12`).
Also run the same test for `T` slightly above `log 2` where nothing is certified, purely as diagnostic, to locate
`a*(T)`: the first `a` at which `Ξ_a` negativity appears, as a function of `T`. Every number labelled
`DIAGNOSTIC-NUMERIC` unless certified by interval arithmetic on a single vector (`PROVED`).

**Q2 — Is the endpoint prime-blind? (the mechanism test).** (i) `A_T^{abs} := G_{Γ,T} − m_0 − 2Σ_{n<e^{2T}}Λ(n)n^{-1/2}·I`
satisfies `A_T ≥ A_T^{abs}`. Is `A_T^{abs} > 0` on `P_T` at `T = ½ log 3` and at `T = log 2`? (ii) Sign-flip:
replace `Λ(3)` by `−Λ(3)`, and separately replace the shift `log 3` by a generic `b ∈ (log 2, 2T)`; does positivity
at `log 2` survive (Galerkin diagnostic, then, if a clear negative appears, one certified vector)? (iii) Identify
which operator the near-null direction `v1` is nearly annihilated by: compute `⟨(G_{Γ,T}−m_0)v1,v1⟩` and the
prime contributions `⟨S_{±log 2}v1,v1⟩`, `⟨S_{±log 3}v1,v1⟩` separately (the certificate scripts contain `v1`;
reconstruct it if necessary). Outcome A: `A^{abs}_{log2} > 0` ⇒ archimedean domination; the certificate is Yoshida's
lemma with constants and the map must say "not ahead of CC in substance". Outcome B: `A^{abs} ≱ 0` and sign flips
destroy positivity ⇒ the certificate uses the arithmetic relation between `log 2` and `log 3` (identify the term:
`S_{log(3/2)}` cross term or the `2·3` structure), which is new and must be stated as a theorem about the
endpoint, `PROVED` only to the extent certified.

**Q3 — The delicate direction and the CC dictionary (the theorem in T).** (i) Prove `T ↦ λ_min(A_T|P_T)` is
non-increasing (zero extension preserves primitivity) and continuous (Suzuki Thm 1.4 — cite, do not reprove).
(ii) Give an analytic description of `v1`: is it (to within the observed accuracy) the primitive function of
minimal archimedean energy on `[−T,T]`, i.e. the first eigenfunction of the compression of `g_Γ − m_0` to `P_T`
(a prolate-type object: CC's Sonin space/Δ→Σ live exactly here)? Compute the overlap of `v1` with that eigenfunction
(`DIAGNOSTIC-NUMERIC`). (iii) Write the capacity identity D.76 as a statement in `T` on `(0, log 2]`: "high-frequency
Gamma capacity `≥ (B/4)E_B`" — is the constant `T`-independent? If yes, state and prove the `T`-uniform version
(`PROVED`); if it degrades at `½ log 5` say exactly how (the two uncomputed cross terms of W4 §3).

## 3. Rules

- Labels: `PROVED` / `RESTATEMENT` (cite where) / `DIAGNOSTIC-NUMERIC` / `OPEN` / `REFUTED`. Never `CONJECTURE` as a result.
- No sign is claimed for `ζ` beyond `T ≤ log 2`. FATAL rule: any new zero-free region, moment bound, or cancellation
  derived from known theorems ⇒ presume error and stop.
- Before each new idea: `grep -rIn` the corpus (03-research, 04-papers) and record the hits in a `Corpus check` line.
- Numerics are diagnostics or single-vector certificates only; every script goes to `scripts/` with the exact
  command line; every printed number carries its label.
- Kill criteria: Q1 negative for all `a` at `log 2` AND Q2 Outcome A ⇒ the phase's conclusion is "the endpoint is
  archimedean domination; the corpus is not ahead of CC in substance" — write it plainly.
- Deliverable: `R153_001_ROUND1.md` (≤ 5000 words + scripts). Then audit `R153_002`.

## 4. Why this is not a restatement

Yoshida 1992 Lemma 2 / Suzuki 2025 Thm 1.4 give positivity for some small window with no arithmetic content.
D.12-α asks whether the certified window already distinguishes `ζ` from `Ξ_a`; that is a question about the
endpoint, not about small windows, and it is open in the corpus (R137_007 §1). Q2 asks which mechanism the
certificate uses; the corpus records the mechanism (Feshbach + D.76) but never asked whether it is prime-blind.
