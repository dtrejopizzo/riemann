# CA_R2_002 — SPEC_A clause (γ) redone with the PROVED margin (phase 193, round R2)

Pen and paper; no numerics.
Object: 03-research/phase-191-design-T-star/SPEC_A_EXACT_INDUCTION.md (exact Schur induction through contacts n_j, T_j = ½log n_j).
Audit entry #1 (AUDIT_PHASE193_CERTAINTY): (γ) kill is **CIRC** — it used ν_j ≈ exp(−13e^{2T_{j+1}}) (pattern law,
NUMÉRICO / NOT PROVED). Proved input: thm:margin / cor:margin1, λ_A(T) ≤ 4·10⁹·T·e^{−15.449T} (T ≥ 1), an **upper** bound.
**No negative value of 𝔞_T for ζ is produced or claimed.**

## 1. The step's slack, from proved facts only (PROVED)
Lemma S(iv) of SPEC_A: for the minimizer h* = ιx + e_min at T_{j+1},
  λ_A(T_{j+1}) = 𝔞(ιx + 𝖪_j e_min) + 𝔰_j(e_min),   and 𝔞(ιx + 𝖪_j e_min) ≥ μ_j‖ιx+𝖪_je_min‖² ≥ 0 (frozen block coercive under H_j).
Hence, with ‖e_min‖ ≤ 1 and **without** the NUMÉRICO edge-mass exponent,
  (1.1)  𝔰_j(e_min) ≤ λ_A(T_{j+1}) ≤ 4·10⁹·T_{j+1}·e^{−15.449 T_{j+1}} = 4·10⁹·T_{j+1}·n_{j+1}^{−7.7245}.
So the absolute slack of (L*) in the direction e_min is at most X^{−7.72}·O(log X), X = n_{j+1} = e^{2T_{j+1}}. (SPEC_A's ε_j^{−1.5}
factor concerned the *normalized* λ_𝔰 and needed the edge-mass exponent; (1.1) avoids it.)
Loss budget (SPEC_A §3, an identity-level computation, PROVED): an error η in the exterior-field functional ℓ_e moves the Schur
term by up to (2‖ℓ_e‖‖η‖ + ‖η‖²)/μ_j; to stay inside the slack one needs ‖η‖ ≲ μ_j·𝔰_j(e_min)/‖ℓ_{e_min}‖ ≤ μ_j·λ_A(T_{j+1})/‖ℓ‖.
With μ_j ≤ λ_A(T_j) and cor:margin1 at both ends (T_j ≥ 1):
  (1.2)  ‖η‖ ≲ 1.6·10^{19} T_jT_{j+1} e^{−15.449(T_j+T_{j+1})}/‖ℓ‖ ≈ X^{−15.45}·polylog   (n_j ≍ n_{j+1}).
Caveat: (1.1)–(1.2) are *upper* bounds on the tolerance. The true tolerance is λ_A-sized and may be much smaller (pattern law
suggests doubly-exponential). Proved data can only *tighten* the requirement, never relax it below (1.2).

## 2. (γ) with the proved margin: exponent vs exponent
A power-saving input at a selected frequency has error e^{−2δT} = X^{−δ} relative to the scale of the sum. Admissibility on (γ)
needs X^{−δ}·(scale) ≤ (1.2):
- single-margin form (only the slack (1.1) counted, ‖ℓ‖, μ_j treated as O(1)):  δ > 7.72;
- full budget (1.2):  δ > 15.45.
The input's scale: the exterior field 𝒯_j h* on the collars contains the contact atom v_{n_j} h*(t − log n_j), v_{n_j} = 2Λ(n_j)n_j^{−½}.
An *estimate* (as opposed to an exact evaluation) of a sum of Λ(n)n^{−½−iγ} over n ≤ X whose individual terms are of size X^{−½}log X
cannot have error below the size of one term unless it is an identity; all inputs listed in SPEC_A §5 (VK, BV/large sieve, MR,
Selberg CLT, Weil-over-𝔽_q as a bound) have savings δ ≤ ½ in this normalization (ARGUED from their published forms; CITED inputs
unchanged). Hence **2δ ≤ 1 < 15.449**: mismatch by a factor ≥ 15 in the exponent (≥ 30 in the full budget).
**Corrected (γ) verdict: FAIL for the mandated power source; strength upgraded CIRC → ARG(+PROVED margin)**:
- the mismatch is now *exponential vs exponential with a finite exponent gap*, not "doubly-exponential vs exponential";
- (1.1) is PROVED, so the failure no longer depends on the pattern law; the only ARGUED link is "estimates have δ ≤ ½".
- It is *not* a structural impossibility: a hypothetical input with saving δ > 7.72 (resp. 15.45) at the minimizer's frequencies
  would pass. No such input exists in the crossword table; an error of size < X^{−7.7} on a sum of X^{−½}-sized terms is an exact
  identity in disguise — which is SPEC_A's own requirement ("the exterior field must enter through identities only").
Therefore: **SPEC_A does not become admissible on (γ) as mandated.** If the power source is dropped (exact induction, identities
only, prop:finite makes the tail half of (γ) void), (γ) is vacuous — PASS — and the specification is judged by the other clauses.

## 3. The remaining clauses (re-graded)
| clause | SPEC_A verdict | corrected grade |
|---|---|---|
| (γ) | FAIL (doubly-exp, CIRC) | FAIL as mandated, exponent gap 15.449 vs 2δ ≤ 1 (PROVED margin + ARGUED δ ≤ ½); PASS (vacuous) in the identity-only version |
| B8 / (δ) | FAIL — L*_j restates positivity at T_{j+1} | **REF-D, not a closure** (audit §0: an RD discard means "no progress by itself"). L*_j is a valid objective; Lemma S(i) PROVED |
| (θ) / O6 | FAIL — ℤ-integrality unused | FAIL **as written** (S, not I): the spec names no line using log ℕ / near-coincidences; a version specifying such a line is not excluded. O6 itself is ARGUED → CIRC on the falsifier half |
| A15 / (ζ) | FAIL if powered by BV/sieve | FAIL if powered as mandated (cor:void at T > 0.74921, PROVED); PASS in the identity-only version |

## 4. Corrected verdict
**NOT ADMISSIBLE as mandated** (power-saving source): (γ) fails by an exponent gap (≥ 7.72 vs ≤ ½ in X-units), now resting on the
PROVED margin; A15/(ζ) fails as before.
**Identity-only exact induction:** (γ) and A15 PASS (vacuously); what remains is (θ) — unspecified, FAIL as written — and B8, which
this is REF-D (a reformulation), not a kill. Status of that version: **OPEN, admissible pending a (θ)-line**: it must
specify where the lag set log ℕ (the contact-block coincidence v_{n_j} vs 2n_j^{−½} at lag 2T_j, ratio Λ(n_j) = log p) enters the
computation of ‖ℓ_e‖_{𝔄_j^{−1}} exactly. That is the actionable item for any reopening of SPEC_A.
Ledger change proposed: audit row 1, (γ) strength CIRC → ARG (margin PROVED); "doubly-exponential" wording withdrawn; B8 relabelled RD.

## 5. Self-review
1. *Upper bound used as precision requirement — sign of logic?* The requirement is tolerance ≤ slack; slack ≤ λ_A ≤ bound. An upper bound
   on slack yields a *necessary* precision, which is what a kill needs. ✓ It does not give a sufficient precision (λ_A could be smaller). ✓
2. *Lemma S(iv) nonnegativity of 𝔞(ιx + 𝖪e):* the Schur decomposition puts ιx + 𝖪_j e in the frozen-block direction where 𝔞 = 𝔄_j ≥ μ_j > 0
   under H_j.1 — valid only inside the inductive step (assumes H_j), which is the setting of (γ). ✓
3. *cor:margin1 needs T ≥ 1:* contacts with T_j ≥ 1 are n_j ≥ 8; below, the base case (thm:log5A, Liu) covers. ✓
4. *"δ ≤ ½" is the weak point:* it is ARGUED; a smoothed-sum identity can have tiny error for smooth weights, but the error is governed
   by the spectral data of Λ at the test's frequencies — it is not a power saving of the mandated type. Kept ARGUED. ✓
5. *No use of zero information, no equivalence with other statements, no numerics run; no negative value for ζ certified.* ✓
