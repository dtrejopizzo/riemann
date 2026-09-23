# Hostile referee report R1 — `main.tex` (Paper 47)

Reviewed: `main.tex` (1293 lines) in full, against the compiled `main.pdf` and the
source record `03-research/phase-154-row-d-law-of-the-body/` (R154_007, 010, 011,
015, 016, 025, 028). Every displayed identity, constant and asymptotic in §§2–7 was
re-derived by hand; the numerical constants were recomputed independently in `mpmath`
(C₀, the tail integral of Theorem 2.2(iii), the two bounds of Corollary 2.6, `2πe^{A_T}`
at both windows, the last sign change of σ_T at both windows, D(0.3), D(0.69)).
`main.log` shows no undefined citation or reference. No edit was made to `main.tex`.

**Verdict: ACCEPT WITH REPAIRS.**

The architecture is sound and, as far as I can check, new: the Lévy–Khintchine reading
of the archimedean multiplier, the semi-infinite LP dual with outside-window measures,
strong duality by finite relaxation + biconjugation + weak-\* limit, the non-attainment
theorem, and the identification of the dual variable with the explicit formula on
modulated flat-top weights. I found no error that destroys a main theorem. I found one
false assertion inside a theorem statement (Finding 3), one false clause in a
proposition (Finding 4), one proposition that is wrong as stated and carries a
`PROVED` label with no proof at all (Findings 5, 6), and a rigour gap in the
machine-verified certificate that the programme's own auditor already raised (R154_016
repair R3) and that this paper does not implement (Finding 1). All are repairable
without touching the results.

Severity scale: FATAL (a stated result is false or unprovable as claimed) / MAJOR
(a proof is incomplete, a label is unearned, or a statement overclaims) / MINOR /
COSMETIC.

---

## 1. Label discipline and the two programme rules

**Rule (1) — no zero-location statement, no sign beyond T ≤ log 2: CLEAN.** The only
certified constant is at `T = ½log3 = 0.5493 < log 2` (Theorem 5.1). §6.4 states
explicitly that "nothing is certified at any `T > ½log3` by the methods of this paper,
and the sign there rests on [Paper42, Zhu2026]", and records the negative value
`−3.1964·10⁻³` at `T = 0.58`. §1.4 is correct. Corollaries 7.4 and 7.5 are
equivalences/identities, not location claims; Corollary 7.5's final sentence is
explicitly conditional ("Under RH:"). No violation.

**Rule (4) — priority consistency with §1.3: CLEAN.** Zhu's window (autocorrelation
support 1.6) is said to be larger than this paper's (log 3 = 1.0986) at four places
(§1.2, §1.3, §1.4, §5.2); Bombieri's primal attainment is cited as
[Bombieri2000, Thm. 3] in §1.2, §1.3, Theorem 3.8's proof, Remark 3.9 and
Corollary 7.4; Yoshida is credited with the prime-free window `a = ½log2`, consistent
with §1.1's "autocorrelation support log 2". No overstatement of priority; the
Cohn–Elkies analogy is acknowledged and hedged ("we have not found it transported to
the Weil symbol before").

**Rule (3) — numerics labelled DIAGNOSTIC: CLEAN except Finding 8.** The Galerkin
bounds, the M-sweep, the contact-set description, the two-prime values and the
resolution-scale paragraph all carry `DIAGNOSTIC`; the Galerkin numbers are correctly
described as variational *upper* bounds throughout.

**Rule (2) — every `PROVED` has a proof or a citation: VIOLATED twice.** See
Findings 6 (Prop. 8.1 has no proof) and 15 (Cor. 7.5 has no proof).

---

## 2. Findings

### Finding 1 — MAJOR. The `PROVED (machine-verified)` label of Theorem 5.1 rests on a *sampled* floating-point allowance, and the round-4 margin argument no longer covers it
*Location:* lines 793–812 (proof of Theorem 5.1), in particular lines 802–805; and
line 197 of §1.2.

*Quote (lines 802–805):* "The target used in the cover is `8.8578·10⁻⁵` minus a
floating-point allowance `10⁻⁹`, which is justified by comparing the double-precision
evaluator with the interval evaluator at the four fine-grid minima and `60` random
points (maximal discrepancy `5.4·10⁻¹³`)."

*What is wrong:* the 2 378 593 cell evaluations of the second-order cover are performed
in float64. Only the *constants* (`H₀, H₁, ψ'(¼), k₀, k₁`, and `m` at four argmins) are
interval-enclosed. The uniform float error of the evaluator is therefore bounded by a
calibration at 64 points, which is not a bound. At round 4 this was defensible because
the cover closed at `4.43·10⁻⁵` against a true infimum of `8.87·10⁻⁵`, leaving a margin
of `4.4·10⁻⁵` (R154_011, row 16). **That margin is gone at round 5:** the cover closes at
target `8.8578·10⁻⁵` against a binding minimum `h₀(37.8153) = 8.8578564·10⁻⁵`, i.e.
a slack of `5.6·10⁻¹⁰`, of the same order as the unproved `ε_fp = 10⁻⁹`. The paper's
own source record flags exactly this: R154_016 §E3 and repair **R3** ("state `ε_fp` as
an a priori bound, e.g. `2Σ|a_j|u_max τ_max ε_mach + M₂w_min²/8 + (437+8)ε_mach‖·‖`, or
re-run surviving cells in `mpmath.iv`"). The repair was never carried out, and the paper
presents the result as `PROVED (machine-verified)`.
Line 197 compounds this: "an exhaustive second-order cover with **all constants enclosed
in interval arithmetic**" reads, in the abstract-adjacent introduction, as if the whole
cover were interval arithmetic.

*Repair (concrete, and it works):* the a-priori bound is easy and comfortably below
`10⁻⁹`. The dominant term is argument rounding in `cos(u_jτ)`:
`2Σ|a_j|·u_max·τ_max·ε_mach = 90.754 × 21.0567 × 442.5 × 2⁻⁵³ ≈ 9.4·10⁻¹¹`;
the Taylor-remainder term is `M₂w_min²/8 = 6264.92 × 10⁻¹⁸/8 ≈ 7.8·10⁻¹⁶`; the
accumulation over the 445 summands is `≈ 445·ε_mach·max|term| ≈ 10⁻¹³`; `scipy.digamma`
contributes a few ulp of `O(5)`, `≈ 10⁻¹⁵`. Total `< 10⁻¹⁰ < ε_fp = 10⁻⁹`.
Replace lines 802–805 by: *"The target used in the cover is `8.8578·10⁻⁵` minus a
floating-point allowance `ε_fp = 10⁻⁹`, which exceeds the a priori error of the
double-precision evaluator: argument rounding in the `437` cosines contributes at most
`2Σ_j|a_j|·u_{460}·(\tau_1+NP)·2^{-53} < 10^{-10}`, the Taylor remainder at the minimal
width `M₂w_min²/8 < 10^{-15}`, and summation and `\psi` evaluation together less than
`10^{-12}`; the measured float-versus-interval discrepancy at the four fine-grid minima
and `60` random points, `5.4\cdot10^{-13}`, is consistent with this bound."* And on
line 197 write "with the constants of the cover enclosed in interval arithmetic and an
a priori bound for the floating-point evaluator".

### Finding 2 — MAJOR. The abstract asserts that λ_min(A_T|P_T) *is* the value of the linear programme; the paper only proves it for the relaxation λ^prim, and says so
*Location:* lines 75–78 (abstract).

*Quote:* "we prove that **the bottom of the spectrum of `A_T` on the primitive class is
the value** of a semi-infinite linear programme".

*What is wrong:* Theorem 3.6 proves `D_T = λ^prim`, and `λ^prim ≤ λ^A` with equality
**explicitly not asserted** (Remark 2.5, line 373: "the equality `λ^prim = λ^A` is not
needed anywhere and is not asserted"; §10.1 open problem (2) asks whether it holds).
The abstract therefore claims more than the body proves, and contradicts Remark 2.5.

*Repair:* "we prove that a semi-infinite linear relaxation of the bottom of the spectrum
of `A_T` on the primitive class — the infimum over the primitive autocorrelation class
`K^prim`, a lower bound for `λ_min(A_T|P_T)` — is the value of a linear programme whose
dual variables are …".

### Finding 3 — MAJOR. A false parenthetical inside Theorem 2.4's proof: the two moment conditions do **not** say that Φ̂ vanishes to order ≥ 2 at ±i/2
*Location:* lines 364–367.

*Quote:* "In terms of `Φ̂ = |F̂|²`, an entire function of exponential type `2T`, the two
conditions say that `Φ̂` vanishes to order `≥2` at `±i/2` (indeed
`Φ̂(±i/2) = F̂(±i/2)F̂(∓i/2) = A B̄` up to conjugation and its derivative there is the
second integral)."

*What is wrong:* the two conditions are `Re(A B̄) = 0` and `Re(A'B̄ − A B̄') = 0` — two
**real** conditions. Since `Φ = c_F` is Hermitian, `Φ̂(i/2) = \overline{Φ̂(−i/2)}`, so
`∫Φ cosh(u/2)du = Re Φ̂(i/2)` and `∫Φ u sinh(u/2)du = \frac i2(Φ̂'(i/2) − Φ̂'(−i/2))`.
Vanishing of these two real numbers is strictly weaker than `Φ̂(±i/2) = Φ̂'(±i/2) = 0`
(four real conditions), which is exactly the point of Remark 2.5 (lines 370–376): `K^prim`
is *larger* than the primitive autocorrelation class. As written, Theorem 2.4's proof
asserts the equality that Remark 2.5 denies. (I verified the two moment formulas
themselves by hand — expanding `cosh((t−s)/2)` and `(t−s)sinh((t−s)/2)` in exponentials
gives `Re(A B̄)` and `Re(A'B̄ − A\overline{B'})` exactly as stated; only the entire-function
gloss is wrong.)

*Repair:* replace the parenthetical by: *"In terms of `Φ̂`, an entire function of
exponential type `2T` with `Φ̂(i/2) = \overline{Φ̂(−i/2)}`, the two conditions say that
`Re Φ̂(i/2) = 0` and `Re[i(Φ̂'(i/2) − Φ̂'(−i/2))] = 0`; when `F ∈ P_T` one has the stronger
`Φ̂(±i/2) = Φ̂'(±i/2) = 0`, i.e. `Φ̂` vanishes to order `≥2` at `±i/2` (Remark 2.5)."*

### Finding 4 — MAJOR. Proposition 4.11 calls an unbounded function bounded
*Location:* lines 732–751, specifically line 738; and the paragraph at lines 745–751.

*Quote (line 738):* "`σ_T(τ) + ν̂_K(τ) = (C₀+c_K) + ∫₀^{2T}(1−cos τu)K(u)du − Σ v_n cos(τ log n)`,
**a bounded function** all of whose frequencies lie in `[0,2T]`."

*What is wrong:* `∫₀^{2T}(1−cos τu)K(u)du = log|τ| + O(1)` as `|τ| → ∞` (this is exactly
the estimate the paper itself uses in the proof of Theorem 2.4, line 359, and `K(u) ~ 1/u`
at the origin makes `∫₀^{2T}K = ∞`). Hence `σ_T + ν̂_K → +∞`; it is band-limited but
**not** bounded. The identity itself is correct (I re-derived it); only the adjective and
the sentence at lines 746–747 ("the outside-window Lévy tail converts the unbounded symbol
into a band-limited one … the residual positivity problem is then a finite-dimensional one
on the band") are wrong — and the second half of that sentence is a non sequitur even after
the repair, since a band-limited function of unbounded growth is not a finite-dimensional
object.

*Repair:* line 738, "a function whose distributional Fourier transform is supported in
`[−2T,2T]` (it still grows like `log|τ|`, the logarithmic singularity of `K` at the origin
being inside the window)". Lines 745–747: "Its content is that the outside-window Lévy tail
removes every `T`-independent frequency from the symbol; what remains, apart from the
`log|τ|` growth generated by `K` near `u = 0`, is carried by frequencies in `[0,2T]`."

### Finding 5 — MAJOR. Proposition 8.1's negative branch is false as stated
*Location:* lines 1109–1116, specifically lines 1112–1113.

*Quote:* "if `λ^prim < 0`, some `F ∈ P_T` in a finite-dimensional trial space has
`𝔞_T(F) < 0`".

*What is wrong:* `λ^prim` is the infimum over `K^prim`, which by Remark 2.5 is strictly
larger than `{c_F : F ∈ P_T}`. `λ^prim < 0` therefore produces `Φ ∈ K^prim` with negative
value, i.e. (by Boas–Kac) some `F ∈ L²(I_T)` with `c_F ∈ K^prim` — which need not lie in
`P_T`. Deducing `𝔞_T(F) < 0` for an `F ∈ P_T` would prove `λ^A < 0`, i.e. would settle the
*other* direction of the inequality the paper carefully never asserts. The proposition as
written decides the sign of `λ^A`, not of `λ^prim`.

*Repair:* "if `λ^prim < 0`, some `Φ` in a finite-dimensional trial family inside `K^prim`
has `C₀ + 𝔈(Φ) − Σ v_nΦ(\log n) < 0`, which is a finite computation with certified
quadrature." And add, after "decidable": "(the sign of `λ^A` is decided only in the
positive branch, since `λ^prim ≤ λ^A`)".

### Finding 6 — MAJOR (rule 2). Proposition 8.1 carries the label `PROVED` and has no `proof` environment
*Location:* lines 1109–1116 (no `\begin{proof}`); label table, line 1234.

Two further clauses are asserted without argument: (a) that the search terminates — this
needs the remark that, `λ^prim ≠ 0` being assumed, Theorem 3.6 gives a certificate with a
*strict* margin, so a dovetailed enumeration over *rational* atoms and multipliers finds
one in finite time, and (b) what "certified quadrature" means for `𝔞_T` (the Lévy integral
`𝔈(Φ)` is a convergent integral of an explicit completely monotone density, so it is
enclosable — say so). Also, the proposition is only meaningful for computable `T`.

*Repair:* add a five-line proof containing (a), (b), the computability hypothesis on `T`,
and the corrected negative branch of Finding 5.

### Finding 7 — MAJOR. The verification threshold is quoted with and without ‖ν‖_TV, and the two are not the same object
*Location:* Proposition 6.3(i), line 920 (`τ_env := 2πe^{A_T+‖ν‖_TV+o(1)}`) against (iii),
lines 925–928 ("at `T = ½log3` and `log2` the values `2πe^{A_T}` are `16.7` and `59.5`");
then §8.2 line 1122 (with `‖ν‖_TV`), §9 item (3) line 1160 (`[0,2πe^{A_T}]`), and the
verdict §8.4 line 1215 (`[0,2πe^{A_T}]`); abstract line 91.

*What is wrong:* for the certificate actually produced, `‖ν‖_TV = 90.75`, so
`2πe^{A_T+‖ν‖_TV} ≈ 10⁴⁰` — which is why Lemma 5.3 (periodicity), not Proposition 6.3, is
what closes the tail at `τ_1 + NP ≈ 442` (Corollary 4.6 says exactly this). Quoting `16.7`
and `59.5` as *the* verification threshold, and then asserting in §9(3) and §8.4 that "the
obstruction is located on `[0,2πe^{A_T}]`" and that this interval "cannot be shortened",
silently drops the `‖ν‖_TV` in the exponent and converts a *sufficient stopping point* into
a claimed *necessary* amount of work. Proposition 6.3 proves neither: it proves that beyond
`τ_env` nothing needs to be checked, not that everything below it must be.

*Repair:* (iii) should read "`2πe^{A_T}` is the threshold for the multiplier-free part
alone (`16.7` and `59.5` at the two windows); for a certificate of total variation
`‖ν‖_TV` the threshold is `2πe^{A_T+‖ν‖_TV}`, e.g. `≈10⁴⁰` for the certificate of §5, which
is why the periodic Lemma 5.3 and not this bound is used there". §9(3) and §8.4 should say
"`[0, 2πe^{A_T}]` is the shortest interval a *pointwise-envelope* argument can reach, and no
envelope shortens it" — the claim about where the obstruction *is* is not proved and should
be labelled `DIAGNOSTIC` or deleted.

### Finding 8 — MAJOR (rule 3). The "factor 5–10 per contact" is an unlabelled numeric claim and is not supported by the paper's own data
*Location:* line 1165.

*Quote:* "`λ^A` drops by a factor `5`–`10` per contact."

*What is wrong:* the table of §6.4 (lines 940–943) gives, at the *fixed* contact set
`{2,3}`, `2.16·10⁻⁴ → 1.09·10⁻⁷` between `T = 0.58` and `T = log 2` — a factor `2·10³`
with no new contact at all; and `9.89·10⁻⁴ (½log3, one contact) → 2.16·10⁻⁴ (0.58, two
contacts)` is a factor `4.6` that mixes the new contact with the change of `T`. The data do
not isolate a per-contact factor, and the sentence sits inside a list of things a closing
argument "cannot be" — i.e. it is doing argumentative work while unlabelled.

*Repair:* delete the clause, or replace by "and, by the `DIAGNOSTIC` data of §6.4, `λ^A`
falls by three orders of magnitude between `T = 0.58` and `T = log 2`".

### Finding 9 — MINOR. Theorem 3.8: the existence of the primal minimiser is justified by the wrong citation
*Location:* lines 524–528.

*Quote:* "A minimiser `Φ_⋆ = c_{F_⋆} ∈ K^prim` of the primal exists: the sublevel sets of
`𝔞_T` on the unit sphere of `L²(I_T)` are compact … (this is also
[Bombieri2000, Thm. 3])."

*What is wrong:* Bombieri's Theorem 3 gives attainment of the infimum on the unit sphere of
`L²(E)` (and the paper uses it correctly elsewhere), not attainment over the strictly larger
class `K^prim`. The correct argument is already in this paper: the feasible set of (P) is
tight (because `σ_T → +∞`, bounded below) and weak-\* closed, and `μ ↦ ∫σ_T dμ` is weak-\*
lower semicontinuous — exactly step (iii) of Theorem 3.6 — so a minimising measure `μ_⋆`
exists, and Boas–Kac (Proposition 3.2) writes it as `|F̂_⋆|²dτ/2π`.

*Repair:* replace the parenthetical by "by the tightness and lower semicontinuity of step
(iii) in the proof of Theorem 3.6, applied with `⋃U_n` dense in `[2T,∞)`; on `P_T` itself
this is [Bombieri2000, Thm. 3]".

### Finding 10 — MINOR. Theorem 3.9: the Lagrange multipliers must be complex
*Location:* line 561.

*Quote:* "there are `α,β ∈ ℝ` with `(𝒜−λ)F = α cosh(t/2) + β sinh(t/2)`".

*What is wrong:* `P_T` is defined by two **complex** linear conditions `A(F) = B(F) = 0` on
`L²(I_T)`; the annihilator of their common kernel is the complex span of `e^{±t/2}`. Unless
`F` is restricted to be real, `α,β ∈ ℂ`.
*Repair:* `α,β ∈ ℂ` (or add "for real `F`" to the hypothesis).

### Finding 11 — MINOR. Proposition 3.5: the uniqueness argument is garbled
*Location:* lines 589–591.

*Quote:* "Uniqueness: two values of `β₀` would make `ĝ₀` a certificate term for a constant,
i.e. `ĝ₀ ≥` const, which fails since `ĝ₀` changes sign."

*What is wrong:* the sentence does not parse as an argument, and `ĝ₀ ≥ const` is true for
*any* bounded `ĝ₀`. The one-line correct proof is: if `β₀ ≠ 2` then
`\frac1{2\pi}\int(σ_T+β₀ĝ₀)|F̂|² = W_T(F) + (β₀−2)Re(A\bar B)`, and `Re(A\bar B)` takes both
signs on `L²(I_T)` (Lemma 6.1 with witnesses `(1,±1,0,0)`), so no bound of the left side
bounds `W_T`. The statement should also record that `β₁ = 0` is forced by the same argument
with `Re(A'\bar B − A\bar B')`.

### Finding 12 — MINOR. Theorem 6.2(ii): the radius `R − π/T` is unjustified
*Location:* line 882.

`μ'_{ε,R}(\{|τ| ≥ R−π/T\}) ≥ ε(1−o(1))` is asserted, but `μ_0 = |F̂_0|²dτ/2π` with
`F_0 ∈ C_c^∞(I_T)` has mass on all of `ℝ`; nothing in the construction confines `1−o(1)` of
its mass to `|τ| ≤ π/T`. What *is* true is that for any `ρ(R) → ∞` with `ρ(R) = o(R)`,
`μ'(\{|τ| ≥ R−ρ(R)\}) ≥ ε(1−o(1))`, since `μ_0` has a rapidly decaying density.
*Repair:* state it with `R − \sqrt R` (or any such `ρ(R)`), which is all part (iii) uses.

### Finding 13 — MINOR. Remark 7.6: the limit `ν_w → −Σ_{n∉N_T}\frac{v_n}2 δ_{±\log n}` is false; the limit statement is heuristic and should be labelled so
*Location:* lines 1076–1082.

*What is wrong:* by (7.2), `dν_w = [\frac12(1−w)K + 2w\cosh\frac u2]\mathbf 1_{|u|≥2T}du −
Σ_{n∉N_T}\frac{v_n}2 w(\log n)(δ_{±\log n})`. As `w → 1` the first bracket tends to
`2\cosh\frac u2\mathbf 1_{|u|≥2T}`, which is **not** zero and is not even a finite measure —
that is precisely why `w ≡ 1 ∉ W_T` (the class imposes `|w| ≤ Ce^{-(1/2+δ)|u|}`). The
remark drops it. The companion claim `f_w → 2π\sum_ρ δ_{γ_ρ}` is correctly normalised
(`\int ŵ = 2πw(0) = 2π`, so `ŵ → 2πδ₀` weakly), but it is a statement about a limit taken
outside the class, i.e. a heuristic.

*Repair:* "as `w ↑ 1` pointwise, the atomic part of `ν_w` tends to
`−Σ_{n∉N_T}\frac{v_n}2(δ_{±\log n})`, the primes outside the window, while its absolutely
continuous part tends to the non-finite measure `2\cosh\frac u2\mathbf 1_{|u|≥2T}du` —
the limit leaves the class `W_T`, which is another face of Theorem 3.8 — and, since
`\int ŵ = 2π w(0) = 2π`, formally `f_w → 2π\sum_ρ δ_{γ_ρ}`. This paragraph is heuristic."
Then §9 item (1) (line 1156, "the only exact certificate is the zero measure itself
(Remark 7.6)") must be softened accordingly, since it currently leans on this heuristic as
if it were Theorem 3.8's content.

### Finding 14 — MINOR. Theorem 7.3: modification (b) needs the cut-off (c) to come first
*Location:* lines 1037–1044.

*Quote:* "(b) replace `h` by `\frac12K` on intervals of length `η_n` around each `\log n`,
`n ∉ N_T`, with `Ση_n` small (so that `w_h` vanishes there and the atoms disappear)".

*What is wrong:* there are infinitely many `n ∉ N_T`, and `\log(n+1) − \log n → 0`, so
"intervals around each `\log n`" eventually overlap and `Ση_n` small is not enough to keep
them disjoint; moreover for `\log n` outside `\supp h` one has `w_h = −\frac12K/D ≠ 0`, so
the atoms there do not disappear at all. The argument is repaired by doing (c) first: after
cutting `w_h` off beyond `U_1`, only the finitely many `n ≤ e^{U_1}` carry atoms, and their
removal by (b) costs an arbitrarily small total variation; the atoms beyond `U_1` are gone
because `w = 0` there.
*Repair:* reorder to (a), (c), (b), and say "the finitely many `\log n ≤ U_1`".

### Finding 15 — MINOR (rule 2). Corollary 7.5 has no proof
*Location:* lines 1065–1071.

It is an immediate consequence of Theorem 7.2(ii) (`f_w = Σ_ρ ŵ(τ−γ_ρ)` with the sum
absolutely convergent), but the paper's own convention requires the one line. Add
`\begin{proof} Immediate from Theorem~\ref{thm:Z}(ii). \end{proof}`.

### Finding 16 — MINOR. `𝔈(Φ) ∈ [0,∞]` and the prime term are stated for complex-valued Φ, where they are complex
*Location:* line 339 (definition of `𝔈`), line 341 (equation (2.7)), line 347 (definition
of `K^prim` uses `Φ` directly).

For complex `F`, `c_F` is Hermitian, not even, and Plancherel gives
`\frac1{2\pi}\int\cos(τu)|F̂|²dτ = \Rel c_F(u)`. So the correct statements are
`𝔈(Φ) = \int_0^\infty(Φ(0) − \Rel Φ(u))K(u)du` and `−Σ v_n \Rel c_F(\log n)`. (No numeric
consequence: the two integrals defining `K^prim` are already automatically real, and the
whole of §3 onwards works with even measures, where the issue does not arise.)
*Repair:* insert `\Rel` in the two places, or add "all autocorrelations below are
identified with their even parts".

### Finding 17 — MINOR. Lemma 5.6 (hybrid tail) uses `k` as both the row index and the column index
*Location:* lines 696–701.

`H_k(x) = \widehat ν_{\mathrm{lat}}(x) + W_k(x) + \sum_k c_k \widehat ν_{s_k,p_k}(x+kP)`:
the `k` of the sum and the `k` of the row are different variables. The displayed formula is
unreadable as printed.
*Repair:* rename the column index to `\ell`:
`H_k(x) = \widehat ν_{\mathrm{lat}}(x) + W_k(x) + \sum_{\ell} c_\ell \widehat ν_{s_\ell,p_\ell}(x+kP)`,
`H_N(x) = \widehat ν_{\mathrm{lat}}(x) + W_N(x) − \sum_\ell |c_\ell|\operatorname{cap}_{s_\ell,p_\ell}(x+NP)`.

### Finding 18 — MINOR (citations to verify). Three references I cannot confirm at the stated precision
*Locations:* line 327 (`\cite[Thm.~13.10, Cor.~13.12]{SSV2012}`), line 390
(`\cite[Prop.~2.3]{SongVondracek2003}`), line 615 (`\cite[5.9.13]{DLMF}`).

- **SSV2012, Thm. 13.10 / Cor. 13.12** for "subordinate Brownian motion with a *special*
  subordinator". The mathematical content used — a Lévy measure that is completely monotone
  on each half-line, `φ(x)/x → 0` hence no Gaussian part — is correct and is verified in the
  paper itself. The chapter/number should be checked against the 2nd edition; the adjacent
  citation `[Ch. 6–7]{SSV2012}` for "complete Bernstein functions form a convex cone closed
  under pointwise limits" is right.
- **SongVondracek2003, Prop. 2.3** for `λ_n ≤ φ((nπ/2T)²)`. The direction is correct (the
  Dirichlet form of the subordinate killed process dominates that of the killed subordinate
  process, so the killed-subordinate eigenvalues are the smaller ones) and the Dirichlet
  Laplacian eigenvalues of `(−T,T)` are `(nπ/2T)²`, but the proposition number should be
  checked. Note also that the Brownian motion must be normalised with symbol `ξ²` (generator
  `Δ`), not `\tfrac12Δ`, for `φ(μ_n)` to be the right comparison; the paper never says which.
  *Repair:* add "with `B` normalised so that its characteristic exponent is `ξ²`".
- **DLMF 5.9.13** for `ψ(z) = \log z − \frac1{2z} − \int_0^\infty g(t)e^{-zt}dt`. The
  identity is correct — I re-derived it from `ψ(z) = \int_0^\infty(e^{-t}/t −
  e^{-zt}/(1−e^{-t}))dt` and `\log z = \int_0^\infty(e^{-t}−e^{-zt})dt/t`, using
  `1/(1−e^{-t}) = g(t) + 1/t + 1/2` — but §5.9 of DLMF contains several Binet-type formulas
  and the equation number should be verified (5.9.12 is the arctan/`e^{2πt}−1` form).
  All other citations I checked are correctly attributed: Boas–Kac 1945 (positive-definite
  functions vanishing outside an interval are autocorrelations), Rockafellar Thm 7.4 +
  Cor. 12.1.1 (`f** = \mathrm{cl}\,f`, and `\mathrm{cl}\,f = f` on the relative interior of
  the domain) — exactly what the biconjugate step needs, IK Thm 5.12 (the explicit formula,
  in the normalisation used), Bombieri Thms 3, 5, 8, 12, Weil 1952, Cohn–Elkies 2003.

### Finding 19 — MINOR (register). Internal phase references are used as load-bearing citations
*Locations:* lines 63–66 (footnote: "phases 153–154 of the author's programme, in
collaboration with AI systems (Claude, Anthropic) used as builders and hostile auditors"),
lines 256–260 (§1.3: "stated in phase 153 … in phase 114 … in phase 64"), lines 331–335
(Remark 2.3: "phase 114 (D.69, D.182) … (D.98) … phase 64"), line 1134 ("phase 138 of the
author's programme, `H_⋆ ≈ 2πe^{2T+1}`"), line 1229 (label table).

A referee cannot verify any of these, and at lines 256–260 and 331–335 they are doing
priority work ("what is added here is (ii)"). Line 1134 uses one as evidence for a
`DIAGNOSTIC` scale. This is the register that papers 43–45 were cleaned of (see their
`TEX_HOSTILE_REVIEW_R1.md` §1).
*Repair:* replace the phase references by "in earlier work of the author" with a citation to
a numbered paper of the programme where one exists, and delete the D-numbers; delete the
"builders and hostile auditors" clause from the footnote or reduce it to "the computations
were independently replicated".

### Finding 20 — COSMETIC. `for $v$ with $\lamP>0$`
*Location:* line 79. Read "for `T` with `λ^prim > 0`".

### Finding 21 — COSMETIC. `M₂ = 6264.92` is quoted for all four covered functions
*Location:* line 799. It is `M₂` for `f`; the three tail rows have
`M₂ = 6262.99` (the `β`-terms `|β₀|H₀+|β₁|H₁` are excluded there and carried by the monotone
`−|β_i|k_i`). Using the larger constant on all four is conservative and therefore harmless,
but say so: "`M₂ = 6264.92` for `f`, and the same (conservative) value for the three tail
rows, whose own constant is `6262.99`".

### Finding 22 — COSMETIC. Lemma 2.1's tail asymptotic is weaker than the truth
*Location:* line 289: `K(u) = 2e^{-u/2}(1+O(e^{-u}))`. From
`K = 2e^{-u/2}/(1−e^{-2u})` the error is `O(e^{-2u})`.

### Finding 23 — COSMETIC. Problem 8.2's norm drops the `1/2π`
*Location:* line 1180. The identity `λ^prim − c = ∫(f−c)dμ_⋆` (which I verified: the `ν̂`
and `ĝ_j` integrals against `μ_⋆` vanish, so `∫f dμ_⋆ = λ^prim`) has
`dμ_⋆ = |F̂_⋆|²dτ/2π`, so the norm is `L¹(|F̂_⋆|²dτ/2π)`. The word "one-sided" **is**
correct: a certificate satisfies `f − c ≥ 0` on all of `ℝ`, so the required approximation is
genuinely from one side.

---

## 3. Re-derivations that came out clean

These are recorded so that the repairs above are not mistaken for a general verdict on the
computations.

- **Lemma 2.1.** The three forms of `K` agree
  (`\frac1{2\sinh(u/2)}+\frac1{2\cosh(u/2)} = \frac{e^{u/2}}{\sinh u} = \frac{2e^{3u/2}}{e^{2u}−1}`);
  the series `2\sum_{k≥0}e^{-(2k+1/2)u}` is right; the Lévy representation follows from
  `ψ(z) = −γ + \int_0^\infty\frac{e^{-t}−e^{-zt}}{1−e^{-t}}dt` with the substitution `t = 2u`,
  and `\frac{2e^{-u/2}}{1−e^{-2u}} = K(u)` exactly. `C₀ = ψ(¼) − \log π = −5.3721834192…`
  (recomputed).
- **Theorem 2.2.** (i) `\Rel[\frac1{a_k} − \frac1{a_k+iτ/2}] = \frac{τ²}{a_k(4a_k²+τ²)}` ✓;
  each summand `x/(a_k(x+4a_k²))` is CBF ✓. (ii) the Lévy measure `\frac12K(|u|)du` ✓.
  (iii) `\int_{2T}^\infty K = \log\coth\frac T2 + π − 2\arctan e^T`: I verified the two
  antiderivatives and checked the identity numerically at `T = ½\log3`
  (`2.36415544812141445478` both ways, 20 digits).
- **Theorem 2.4.** Both moment formulas `\Rel(A\bar B)` and `\Rel(A'\bar B − A\overline{B'})`
  re-derived (see Finding 3 for the one wrong gloss).
- **Remark 2.5.** The trichotomy is correct: for real `F`, `AB = 0` and `A'B − AB' = 0` iff
  `F ∈ P_T` or `A = A' = 0` or `B = B' = 0`. The final claim `λ^W ≤ λ^prim` is also correct:
  the first condition of `K^prim` is `\Rel(A\bar B) = 0`, so `W_T = 𝔞_T` at any `F` realising
  a `Φ ∈ K^prim` via Boas–Kac.
- **Corollary 2.6.** `C₀+A_T+φ((3π/2T)²) = 1.29110791…` at `T = ½\log3` and `2.32675226…`
  at `T = \log2` — both agree with the printed `1.291` and `2.327`. `A_T = 0.98025814`
  and `2.24882634`, `B = A_T − C₀ = 7.62100976` at `T = \log 2` ✓.
- **Lemma 3.3.** The two integrations by parts, the relation
  `ĝ₀(1+\frac1{4τ²}) = \frac{2\cosh T\sin 2Tτ}{τ} + \frac{\sinh T\cos 2Tτ}{τ²}`, the bound
  `k₀`, and `|ĝ₁| ≤ 8T\sinh T/τ` (using `\int_0^{2T}(u\sinh\frac u2)' du = 2T\sinh T` and
  the one-signed integrand) are all correct, as is the two-term expansion (which needs
  `g'(0) = 0`, true for both `g₀` and `g₁`).
- **Theorem 3.6.** The LP-duality bookkeeping (`a_i = −y_i/2`, `β_j = −y_{N+1+j}`,
  `w^{**}(b) = \sup\{y_0 : σ_T − \sum y_kf_k ≥ 0\}`) is correct; `w` is proper convex and
  `> −\infty` for the stated reason; the separation, the Cesàro means (all `u_i > 0` and
  distinct, `ĝ_j → 0`), the forced vanishing of `g(2T^-)` then `g'(2T^-)` from the
  oscillating expansion, and the determinant
  `\cosh T(\sinh T + T\cosh T) − T\sinh²T = \sinh T\cosh T + T > 0` all check. The weak-\*
  step (tightness from `σ_T → ∞` bounded below, density of `⋃U_n`, continuity of `\check μ`,
  lower semicontinuity) is correct.
- **Theorem 3.8.** Given Finding 9, the rest is right: `\check m = −\frac12K(|u|)` on
  `0<|u|<2T`, the prime part `−Σ\frac{v_n}2δ_{±\log n}`, and the contradiction between a
  bounded continuous left side and a right side with a `1/u` singularity and atoms. The proof
  in fact uses only that `Σβ_jh_j` is locally bounded and atom-free near the origin, so the
  hypothesis "continuous on the closed window" is stronger than needed — no repair required,
  but the theorem could be stated for `h_j ∈ L^1 ∩ L^\infty_{loc}(0,2T)`.
- **Lemma 4.1.** The Binet representation, `g(0^+) = 0`, `g'(t) = t^{-2} − \frac14\sinh^{-2}(t/2) > 0`,
  `g(∞) = \frac12`, the integration by parts giving `|\int g e^{-zt}dt| ≤ \frac1{2|z|}`, and
  the substitution `y = τ/2` producing exactly `\log\frac{τ}{2π} − \frac1τ − \frac1{2τ²}` and
  `\log\frac{τ}{2π} + \frac1τ + \frac12\log(1+\frac1{4τ²})` — all correct, including the
  monotonicity of the lower bound (`τ^{-1}+τ^{-2}+τ^{-3} > 0`). Part (iii) is correct: the
  `\log p` are `ℚ`-independent, the one-parameter Kronecker theorem applies to them directly,
  and prime powers are handled by `|\cos(kθ_p) − 1| ≤ k²θ_p²/2` with `k ≤ 2T/\log p` bounded;
  composite `n` never appear because `Λ(n) = 0`. The supremum is not attained, and the paper
  writes `\sup`.
- **Lemmas 5.3, 4.5, 5.6, Cor. 4.6, Prop. 4.9, Prop. 4.10.** The periodicity `u_jP = 2πj`, the
  row construction (exact prime term on the first `N` copies, `−A_T` beyond, `m` increasing,
  `k_i` decreasing), the exponential-column transform
  `\Rel[e^{2iTτ}p!/(s−iτ)^{p+1}]` with cap `p!/(s²+τ²)^{(p+1)/2}` decreasing, the mass
  `p!/s^{p+1}`, the linear/exponential cost dichotomy of Corollary 4.6
  (`τ_1 ≥ \max\{A+A'+2, 2πe^{c+A_T+1}\}`), and the second-order cell bound with
  `M₂ = Σv_n\log²n + 2Σ|a_j|u_j² + |β₀|H₀ + |β₁|H₁` are all correct as stated.
- **Theorem 4.8.** The totality argument is correct: if `g ∈ L^\infty` annihilates all
  `t^pe^{-t}` then its Laplace transform, holomorphic on `\Rel z > 0`, has all derivatives
  zero at `z = 1`, hence vanishes, hence `g = 0`. The `ε`-bookkeeping (`ε/2` from
  Theorem 3.6, `ε/8` twice from smoothing, `ε/8` from the `L¹` approximation, with
  `\|\hatν_2−\hatν_1\|_\infty ≤ \|ν_2−ν_1\|_{TV}`) closes.
- **Theorem 5.1, numbers.** Against R154_010 §4 and R154_015 §3: `437` atoms, `j = 24..460`,
  `d = \log3/24`, `u_{460} = 21.0567`, `β₀ = 2.00256170925026…`, `β₁ = −0.00965443404485…`,
  `‖a‖₁ = 45.377` hence `‖ν‖_{TV} = 2Σ|a_j| = 90.754` (paper: `90.75` ✓), `\hatν(0) = 1.7337`,
  `M₂ = 6264.92`, `τ_1 = 30`, `N = 2`, `P = 2π·24/\log3 = 137.2608` (so the period is
  `[30, 167.2608]` ✓), `2 378 593` evaluations, `0` unresolved, `20` segments, initial width
  `0.02`, minimal width `10⁻⁹`, discrepancy `5.4·10⁻¹³`, binding minimum
  `h₀(37.8153) = 8.85786·10⁻⁵`, the other three argmins `f(17.645)` and `h₂(58.817)` — every
  figure matches the archive. `c = 8.8578·10⁻⁵ − 10⁻⁹ = 8.8577·10⁻⁵` is arithmetically
  consistent. The M-sweep `−7.1·10⁻³, −4.4·10⁻³, +2.2·10⁻⁴, +3.4·10⁻⁴, +1.7·10⁻⁴` matches
  R154_007 §3.2 and R154_010; the `+1.7·10⁻⁴ → −2.1·10⁻²` honesty note matches R154_010 §4;
  `9%` of the Galerkin bound `9.89·10⁻⁴` matches (`8.95%`). The `T = 0.58` row (414 atoms,
  `−3.1964·10⁻³`, `β = (2.0400, −0.1478)`) matches R154_015 §5.
- **Lemma 6.1.** The four witnesses do what is claimed: `(1,0,0,∓1)` gives `(Q₀,Q₁) = (0,±1)`
  and `(1,±1,0,0)` gives `(±1,0)`; surjectivity of `F \mapsto (A,B,A',B')` on
  `C_c^\infty(I_T)` follows from real-analyticity; the moment image of the *measure* feasible
  set is convex because the moment map is linear, which is what makes the separation step
  legitimate.
- **Theorem 6.2.** (i) is exactly `−B + ε(m(R) − m(0))` after the split. (ii) the mixture
  `\check μ_{ε,R} = [(1−ε)+ε\cos Ru]\check μ_0` is supported in the window ✓; the choice
  `λ = ε|d|/(r_0+ε|d|)` does give `|w| = r_0` and moment `0` ✓; the correction costs
  `λ(B+V^*) = o(ε)` ✓. Only the radius of Finding 12 is wrong.
- **Proposition 6.3(iii).** `A_T = \sum_{n<X}2Λ(n)/\sqrt n \sim 4\sqrt X = 4e^T` by PNT and
  partial summation ✓. `2πe^{A_T} = 16.7456` and `59.5433` ✓ (recomputed). The last sign
  changes of `σ_T` are at `τ = 10.532` and `46.13` ✓ (recomputed by a `10⁻³` scan).
- **Theorem 7.2(i).** The identity `σ_T + \hatν_w + 2ĝ₀ = f_w` checks term by term: the
  archimedean parts combine to `C₀ + \int_0^\infty(1 − w\cos τu)K` using `w ≡ 1` on `[0,2T]`;
  the two prime sums combine into `−\sum_{n≥2}v_nw(\log n)\cos(τ\log n)`; and
  `2ĝ₀ + 2\int_{|u|≥2T}w\cosh\frac u2\cos τu = 2\int_ℝ w\cosh\frac u2\cos τu`. Finiteness of
  `ν_w` is correctly justified by the `e^{-(1/2+δ)|u|}` decay.
- **Theorem 7.2(ii).** The explicit-formula normalisation is right:
  `\hat h(i/2) + \hat h(−i/2) = 2\int h\cosh\frac u2`, the prime term is
  `−\sum 2Λ(n)n^{-1/2}h(\log n)` for even `h`, and the archimedean term is
  `\frac1{2π}\int m\hat h`. The transform of `h_τ = w\cos(τ·)` is
  `\frac12[\hat w(t−τ)+\hat w(t+τ)]`; the symmetry `γ_ρ \mapsto −γ_ρ` (from `ρ \mapsto 1−ρ`)
  together with `\hat w` even collapses the two halves to `\sum_ρ\hat w(τ−γ_ρ)`; and Fourier
  inversion gives `\frac1{2π}\int\hat w(t∓τ)dt = 1` and
  `\frac1{2π}\int\hat w(t∓τ)\cos(tu)dt = w(u)\cos(τu)` (the sine part drops by evenness).
- **Theorem 7.3, the denominator.** `D(u) = 2\cosh\frac u2 − \frac12K(u)` satisfies
  `D' = \sinh\frac u2 − \frac12K' > 0` for all `u>0` because `K` is completely monotone, and
  `D(0.3) = 0.1149 > 0`, `D(0.69) = 1.1734 > 0` (recomputed); with `2T ≥ \log 2 > 0.3` the
  claim holds. `w_h = (h − \frac12K)/D` is the unique solution of
  `\frac12K + wD = h` ✓, and `|w_h| \ll e^{-|u|}` off `\supp h` ✓, which sits inside the
  class's `e^{-(1/2+δ)|u|}`.
- **Corollary 7.4.** Both directions are correct, including the Jensen step: `F̂_⋆` is entire
  of exponential type `T` and in `L²`, so it has `O(R)` zeros in `|z| ≤ R`, against
  `N(R) \sim \frac R{2π}\log R` zeros of `ζ`; hence `W_T(F_⋆) = 0` is impossible and
  `λ^W > 0`.
- **§8.2, the reformulation.** `λ^{prim} − c = \int(f−c)dμ_⋆` holds because
  `\int\hatν dμ_⋆ = \int\check μ_⋆ dν = 0` and `\int ĝ_j dμ_⋆ = 0`; "one-sided" is the right
  word.
- **§9 items.** (2) is Theorem 6.2 ✓, (3) is Proposition 6.3(ii) ✓ modulo Finding 7, (5) is
  Theorem 7.2(ii) ✓ — `f_w ≥ 0` *is* literally the inequality `\sum_ρ\hat w(τ−γ_ρ) ≥ 0`.
  (1) leans on the heuristic Remark 7.6 (Finding 13) and (4)'s numeric clause is Finding 8.

---

## 4. What is correct and new

1. **The archimedean multiplier as a Lévy exponent** (Lemma 2.1, Theorem 2.2). `m(τ) = C₀ +
   \int_0^\infty(1−\cos τu)K(u)du` with `K = \frac1{2\sinh(u/2)}+\frac1{2\cosh(u/2)} =
   2\sum_{k≥0}e^{-(2k+1/2)u}` completely monotone; `\Rel ψ(¼+iτ/2) − ψ(¼) = φ(τ²)` with `φ`
   complete Bernstein; the process is pure-jump, with no Gaussian part; and the entire
   `T`-dependence of the archimedean side is the closed-form tail
   `\log\coth\frac T2 + π − 2\arctan e^T`. Verified in full.
2. **The form as a Lévy energy** (Theorem 2.4): `𝔞_T(F) = C₀\|F\|² + 𝔈(c_F) − \sum v_nc_F(\log n)`,
   turning the eigenvalue problem into `C₀` minus a Legendre transform over the
   autocorrelation class. Clean modulo Findings 3 and 16.
3. **The dual programme and strong duality** (Definition 3.1, Proposition 3.2, Theorem 3.6).
   The identification of the dual variables as finite signed measures *outside* the window
   plus two polar multipliers, with `D_T = λ^{prim}` and finitely atomic dual sequences, is
   the paper's structural contribution and its proof is correct: finite relaxation, Legendre
   biconjugation with a genuine interiority proof (the Cesàro argument and the determinant
   `\sinh T\cosh T + T`), and a weak-\* limit. I found no gap.
4. **Non-attainment** (Theorem 3.8). The mechanism — the `1/u` singularity of the Lévy
   density and the prime atoms live *inside* the window, where the dual variable may not —
   is both correct and, as far as I can see, new; the pairing with Bombieri's primal
   attainment is a genuine and quotable structural statement.
5. **Exhaustion by exponential columns** (Theorem 4.8) and the tail calculus
   (Lemmas 5.3, 4.5, 5.6, Cor. 4.6, Prop. 4.10), including the `\Theta(c^{-1/2})` cost of the
   second-order cover against `\Theta(c^{-1})` for a Lipschitz cover. All correct.
6. **The explicit certificate at `T = ½\log3`** (Theorem 5.1). Every archived number is
   consistent with the source record, `M₂` is a correct second-derivative bound, the tail is
   correctly reduced to three rows on one period, and the arithmetic
   `c = 8.8578\cdot10^{-5} − ε_{fp}` is consistent. Subject only to Finding 1 (make `ε_{fp}`
   a priori — the bound exists and is `< 10^{-10}`), this stands as a proof of positivity by
   an explicit dual feasible point rather than by matrix compression.
7. **The negative theorems.** The `\Theta(\log R)` exchange law (Theorem 6.2) and the exact
   supremum `A_T` of the prime comb by Kronecker (Lemma 4.1(iii), Proposition 6.3(ii)) are
   correct and are real obstructions, not rhetoric.
8. **Section 7 — the strongest part of the paper.** The algebraic identity
   `σ_T + \hatν_w + 2ĝ₀ = f_w` (Theorem 7.2(i)) and its identification with the Weil explicit
   formula on `u \mapsto w(u)\cos(τu)` (Theorem 7.2(ii)) are exactly right, in a correct
   normalisation, and the exhaustion Theorem 7.3 — every certificate of the complete form is
   a flat-top explicit-formula certificate up to arbitrarily small uniform correction —
   converts the optimiser's `β₀ ≈ 2.0026` from a numerical curiosity into the polar term of
   the explicit formula. Corollary 7.4 (RH ⟺ for every window a flat-top weight whose
   smoothing of the zero measure is nonnegative) is a correct, quotable equivalence, and
   Corollary 7.5 makes every certificate an unconditional inequality about the zeros. Modulo
   Findings 13–15, this section is sound and is what the paper should be read for.
