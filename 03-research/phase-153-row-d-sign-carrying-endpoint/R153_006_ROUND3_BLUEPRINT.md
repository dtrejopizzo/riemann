# R153.006 — Lead blueprint, round 3 (owner: same phase, two tracks). Date 2026-09-19.

Corpus check (lead, Explore sweep): no file treats a single off-line pair `½ ± a + iγ` with `γ ≠ 0`; all off-line studies
use `Ξ_a(s) = ξ(s+a)ξ(s−a)` (phases 119–124, 137–138, 153). DH retired (no pole). The bound
"`λ_min(A_T) ≥ −Ce^{aT} ⟺ β ≤ (1+a)/2`" is NOT in the corpus in this form: prove or cite before use.

## Track 1 — (P153.5): the rank-two (single-pair) detection law for ζ itself

**Model (exact, no approximation).** Let `γ_0` be an actual ordinate of a zero of ζ (e.g. `γ_1 = 14.1347…`). Let `ζ̃_{a,γ_0}`
denote the "zero configuration of ζ with the pair `½ ± iγ_0` replaced by the four points `½ ± a ± iγ_0`" (as a divisor,
not as a function). Its Weil form on real `F ∈ P_T` is, by the explicit formula written as a sum over the divisor,
`B_T(a,γ_0) = A_T + R_T(a,γ_0)`, with the finite-rank correction
`⟨R_T F,F⟩ = −2|F̂(½+iγ_0)|² + 2 Re[ F̂(½+a+iγ_0) · conj F̂(½−a+iγ_0) ]` (symmetrised over `±γ_0`; state the exact
normalisation of `F̂` used in main.tex and the factor from real `F`). Everything else (archimedean, primes, poles) is
unchanged, because `A_T` on `P_T` IS the divisor sum. Define `T*(a,γ_0) := inf{T : B_T(a,γ_0) ≱ 0 on P_T}`.

Questions. (1) Prove the model statement: on `P_T`, `⟨A_T F,F⟩ = Σ_ρ F̂(ρ) conj F̂(1−ρ̄)` with the corpus's normalisation
(RESTATEMENT of Weil/Paper 42 — cite the exact line), hence `B_T` is the Weil form of the modified divisor (PROVED, trivial
but must be written). (2) Prove the two-sided a-priori bounds: for `supp F ⊂ [−T,T]`, `|F̂(½±a+iγ)| ≤ e^{aT}‖F‖_1`, and
derive the classical growth dichotomy "if `B_T ≥ −Ce^{2a'T}‖F‖²` for all `T` then no zero has `|β−½| > a'`" and its
converse — label RESTATEMENT if you find it in Weil/Bombieri/Iwaniec–Kowalski §5, PROVED otherwise; keep the proof short.
(3) Compute `T*(a,γ_0)` (DIAGNOSTIC-NUMERIC, mesh-free spectral assembly from `scripts/audit/`, refinement check) for
`γ_0 = γ_1` and `a ∈ {0.05,0.1,0.2,0.3,0.45}`, and for `a = 0.3` with `γ_0 ∈ {γ_1, γ_2, γ_5, γ_10}` (real ordinates from
mpmath.zetazero). Does the law separate into an `a`-part (like `T*(a)` of round 2) and a `log γ_0`-part (resolution
needed to isolate one zero among density `(log γ)/2π`)? Fit only if the data force it; label DIAGNOSTIC. (4) The
conditional exclusion: since `A_T ≥ 0` is certified for `T ≤ log 2`, any `(a,γ_0)` with `T*(a,γ_0) < log 2` is excluded
**under the hypothesis that all other zeros are on the line**. State it exactly as a conditional theorem and then
apply the FATAL rule: the excluded set must lie strictly inside what is already known (all zeros with `|γ| ≤ 3·10¹²`
are on the line, Platt–Trudgian 2021) — check whether any `(a,γ_0)` with `γ_0 > 3·10¹²` could be excluded by the
`log 2` window alone; if the answer is yes, PRESUME ERROR and find it. Report the honest outcome either way. (5) State
plainly what this does and does not say about ζ.

## Track 2 — (P153.4): the needle at b = log 3

Operator `A_{T}(b) := G_{Γ,T} − m_0 − w_2(S_{log 2}+S_{−log 2}) − w_3(S_b + S_{−b})` on `P_T`, `T = log 2`,
`w_n = Λ(n)n^{−1/2}`, `b ∈ (log 2, 2T)`. Round 2 found `λ_min(b)` positive (`≈ 1.1·10⁻⁷`) only in a needle of width
`~10⁻⁷` around `b = log 3`. Questions. (1) Explain the needle analytically: the form is `⟨(G−m_0−w_2(…))F,F⟩ − 2w_3 c_F(b)`
where `c_F(b)` is the autocorrelation of `F` at `b`; positivity for all `F ∈ P_T` at `b` means the maximum over `F`
of a ratio; write the variational problem and show why its solution can be sharply peaked in `b` (is it because the
near-minimiser of `A_{log2}` has an autocorrelation with a local minimum exactly at `log 3`? compute `c_{F_min}(b)`).
(2) Is the needle a property of the pair `(log 2, log 3)` or of `(2T, b)` — repeat at `T = 0.68, 0.70, 0.72` with the
same `w_2,w_3`: does the needle follow `b = log 3` (arithmetic) or `b = f(T)` (analytic)? DIAGNOSTIC-NUMERIC.
(3) If a clean statement emerges ("at `T = log 2` the two-contact Weil form is nonnegative iff `b = log 3`, up to
width `ε`"), formulate it as a theorem candidate with exactly what would be needed to prove it, label OPEN. Corpus
check first: grep `needle`, `unique contact`, `b = log 3`, `contact uniqueness`.

## Rules (both tracks)
Labels PROVED / RESTATEMENT / DIAGNOSTIC-NUMERIC / OPEN / WITHDRAWN; FATAL rule; no sign claimed for ζ beyond
`T ≤ log 2` except as the explicit conditional of Track 1 (4); corpus-check lines; scripts in `scripts/round3/`.
Deliverables: `R153_007_TRACK1_SINGLE_PAIR.md` and `R153_008_TRACK2_NEEDLE.md` (≤ 3500 words each).
