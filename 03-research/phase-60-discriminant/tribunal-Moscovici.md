# Tribunal — Audit (SEVERE referee)
## CCM zeta spectral triples program — chain E0→E4 **Lens:** complex analysis / entire
functions (Laguerre–Pólya, Hermite–Biehler, de Branges, Boas, Phragmén–Lindelöf).
**Documents read:** `RH-PROOF-FULL.md`, `AUDIT-repairs-E1-III.md`, `E2-nucleo-proof.md`,
`N5-subpieces-proved.md`.
**Rule:** cold. A forced proof is worse than an admitted gap. RH is NOT claimed. --- ## 0. Executive summary (per piece) | Piece | Verdict | One line |
|---|---|---|
| E0 | **SOLID** | Definition + identity `QW=`Weil; correct as a definition. |
| E1 (real-rootedness) | **GAP** | Own proof open. **I close half** (HB for pure positive envelope); the half with boundary carrier remains open. See §2. |
| H1 | **SOLID** (structure) | PF gives simple bottom + positive envelope. Does NOT give PSD. Correct after correction. |
| H1′ (QW PSD) | **GAP = RH** | `ε_0≥0 ⟺` Weil-pos `⟺` RH-up-to-T*. Not unconditional. Correctly labeled. |
| N0 | **SOLID** | Double-exp Φ + incomplete Γ: the proof is correct and robust. See §3.1. |
| N1 | **SOLID*** | Subharmonicity + two constants + harmonic measure correct; Boas well invoked. One constant imprecision, harmless. See §3.2. |
| N2 (Γ=O(1)/O(logλ)) | **SOLID** | Plancherel–Pólya + Nikolskii correct. The `O(1)` with normalization is stronger than what is proved (proved: `O(logλ)`); harmless. See §3.3. |
| N3 | **SOLID** | Boas/Phragmén–Lindelöf correct. See §3.4. |
| Reduction (Thm 2) | **SOLID*** (modulo E1) | The Hurwitz step is valid; the bound `λ^{1/2}ε_loc` correct. See §4. |
| III | **GAP (conditional)** | (H-gap)+(H-lim)+(H-pos) only numerical; (H-pos)=RH. Implication correct. |
| N5b | **SOLID** | Boundary benign; reduction valid. |
| N5c | **SOLID*** (modulo E1) | Real-rooted monotonicity correct; DH side proved. See §5. |
| IV.1 | **GAP (analysis)** | Limit operator not identified; not RH-hard. |
| IV.2 ≡ §V | **GAP = RH-equivalent** | The core. Correctly labeled RH-hard. |
| E3 (Hurwitz) | **SOLID** (modulo E1) | Classical, well applied. See §4. |
| E4 | **SOLID** | `Ξ∈LP ⟺ RH`, classical. | **Referee's statement:** The analytic scaffolding (N0–N3, Reduction, Hurwitz) **withstands
severe audit** — it is correct, reusable mathematics. The document is **candid** in
its labels: there is no self-deception in the localization. The three live points are (i) E1 with no
proof of its own, (ii) III conditional with (H-pos)=RH, (iii) the IV.2 RH-equivalent core.
**RH is not proved.** Below I partially close E1 and delimit *exactly* what is missing. --- ## 1. Audit of the scaffolding — detailed verdicts ### 1.0 E0 — SOLID (as a definition)
The form `QW=A_λ^N` is well defined; the identity `⟨ξ,QWξ⟩ = Σ_ρ g(γ_ρ)·conj(g(conj γ_ρ))`
with `g=ξ̂` is Weil's explicit formula restricted to `PW_Ω`, and the claim "`QW` IS the
Weil form of the zero-side" is **structurally correct** and central. It is not a piece that
"proves" anything; it is the setting. SOLID, no objection. --- ## 2. THE CLOSABLE GAP IN MY LENS — E1 real-rootedness ### 2.1 Exact statement and refutation of the old proof
The claim is: for all `λ,N`, `ξ̂_{λ,N}(s) = sin(Ls/2)·Σ_{|k|≤N} ξ_k/(s−d_k)` has **only
real zeros**. The recorded proof (interlacing with `ξ_k>0`) is **correctly refuted**
by `ξ=(−1,2,−1)`, `d=(−1,0,1)`: `f(s)=−2/(s³−s)`, constant numerator, **zero roots**.
The counterexample is valid and devastating for the old proof. I accept the refutation. Furthermore the document observes that real-rootedness also holds empirically for
Davenport–Heilbronn (where `Λ≥0` fails), so **it cannot come from Perron–Frobenius**.
This is a correct and candid argument: it rules out the coefficient-positivity route. ### 2.2 The real structure of the problem (Hermite–Biehler)
Let me rewrite it. Let `f(s)=Σ_k ξ_k/(s−d_k)` be the secular function. The zeros of `ξ̂` (aside from cancelling the
poles `d_k`) are the zeros of `f`. The claim "`ξ̂∈LP`" is equivalent to "**`f` has only
real zeros**", because `sin(Ls/2)` is already LP and entire of type `L/2`, and the product of two functions
with only real zeros and order ≤1 (with correct pole pairing) remains entire.
Precisely: `ξ̂` is entire (the poles of `f` at `d_k` are cancelled by the zeros of
`sin(Ls/2)`), of exponential type `L/2`, **real on ℝ** (coefficients `ξ_k`, `d_k` real). **Key HB criterion (real Hermite–Biehler).** A real entire function `g` of exponential
type, real on ℝ and in the closed Pólya–Laguerre class, has **only real zeros**
if and only if there exists `E` (a de Branges function, `E=A−iB` with `A,B` real on ℝ) such that
`g=B` (or `g=A`), `E` of HB type (`|E(z̄)|<|E(z)|` for `Im z>0`), **and `A,B` have
interlacing real zeros**. Equivalently, via the classical Hermite–Biehler
theorem: a function `A+iB` with `A,B` real polynomials/entire functions is Hurwitz-stable (zeros in
a half-plane) ⟺ the zeros of `A` and `B` are real, simple and **interlace**, with the
Wronskian `A'B−AB'` of constant sign. **The decisive technical point:** the real-rootedness of `f` **does NOT** follow from any sign
property of `ξ_k` alone; it follows **if and only if** the rational function `f(s)=Σ ξ_k/(s−d_k)`
is a **Nevanlinna/Herglotz function with constant-sign residues**, or more
generally if `f` is the **m-function of a self-adjoint Jacobi/Sturm–Liouville operator**. ### 2.3 What I CAN close rigorously (half the gap) **Lemma M1 (positive residues ⟹ real-rootedness, Herglotz).**
Let `f(s)=Σ_{k} r_k/(s−d_k)` with distinct `d_k∈ℝ` and **all residues `r_k>0`**.
Then `f` is a Herglotz–Nevanlinna function (it maps the upper half-plane `H` into the
lower half-plane): for `Im s>0`,
``` Im f(s) = Σ_k r_k · Im(1/(s−d_k)) = Σ_k r_k · (−Im s)/|s−d_k|² < 0.
```
Hence `f(s)≠0` for `Im s≠0` (its imaginary part is nonzero), i.e. **all the zeros of `f`
are real**. Moreover, between two consecutive poles `f` decreases from `+∞` to `−∞`, giving
exactly one zero per gap: **strict interlacing**. ∎ This is the correct classical result (it is exactly the case of the m-function of a Jacobi
operator with positive weights). Now the connection to `ξ̂`: **Lemma M2 (residue↔band-edge value translation).** By the residue formula,
`ξ̂(d_k)=lim_{s→d_k}sin(Ls/2)·ξ_k/(s−d_k)`. Since `sin(Ls/2)` has a simple zero at `d_k`
with derivative `(L/2)cos(Ld_k/2)=(L/2)cos(πk)=(L/2)(−1)^k`, we get
``` ξ̂(d_k) = ξ_k·(L/2)·(−1)^k. (correct, matches the document's)
```
The **residue** of `f` at `d_k` is exactly `ξ_k`. Hence Lemma M1 gives real-rootedness
**if and only if all the `ξ_k` share the same sign** (WLOG `ξ_k>0`). **Partial conclusion [CLOSED]:** If the fundamental eigenvector had a **constant-sign
envelope in the raw sinc basis** (`ξ_k>0` ∀k), real-rootedness would be an **elementary
theorem** (Herglotz, Lemma M1), self-contained, with no citation to CCM. This is clean mathematics and
I consider it closed for that case. ### 2.4 Why the real case is NOT covered — and exactly what hypothesis is missing
The obstruction, correctly identified by the document, is that the **real** ground state
has `ξ_k ≈ u_k cos(ω*k+φ)` with boundary carrier `ω*≈0.966π` (near-Nyquist), so `ξ_k`
**changes sign ~N times**. Lemma M1 **does not apply**, and in fact the counterexample
`(−1,2,−1)` shows that with alternating signs real-rootedness **can fail**. So why is it empirically true? The correct answer is de-modulation. Define
the change `ξ_k = (−1)^k η_k` (modulation by the Nyquist carrier `ω=π`). The band-edge
value becomes `ξ̂(d_k)=η_k(L/2)`, **without the `(−1)^k`**. But this does NOT change the residues of `f`:
`f(s)=Σ(−1)^kη_k/(s−d_k)` — the alternating sign reappears in the residues. The de-modulation
that makes `η_k>0` (positive envelope, **what H1/PF does give**) is **not** what controls the
residues of `f`. There is a structural **phase mismatch**: the positivity PF delivers lives
in the de-modulated envelope (`η_k>0`), while real-rootedness via Herglotz requires
positivity of the raw residues `ξ_k`. With carrier `ω*` near π (but **not** exactly
π), neither `ξ_k>0` nor `(−1)^kξ_k>0` holds. **Precise verdict on E1:** Real-rootedness is **NOT self-contained at the Herglotz level**.
It requires one of: - **(A)** a **de Branges interlacing** property: that `ξ̂` be the `B` component of an `E=A−iB` of HB type, which is *equivalent* to the secular zeros being the **spectrum of a self-adjoint operator** (CCM's spectral realization). This is **exactly CCM Thm 1.1(iii)**: the secular roots = real spectrum of the self-adjoint realization. It is not derivable from M1; it is the spectral claim itself.
- **(B)** a hypothesis on the fundamental eigenvector: that the operator `QW` (real symmetric) be such that its ground state generates a **Chebyshev system / totally positive kernel** in the sinc basis. The document reports that this was **refuted** numerically (Gantmacher–Krein, totally non-negative, does not fit). I accept that finding: the TP/TN route is closed. **Hence my verdict on E1 is (c) of the task's statement, refined:**
> Real-rootedness is true as **CCM Thm 1.1(iii)** (real spectrum of the self-adjoint
> realization = secular roots). **It does not admit a self-contained proof at the level of elementary
> entire functions** (Herglotz/HB) with the information the program has in isolation
> (de-modulated positive envelope), because of the carrier phase mismatch ω*≠π. The only
> own route would be to **reconstruct the self-adjoint realization** (that `ξ̂` ∈ a de Branges space
> `H(E)` with explicit HB `E`), which is **re-proving CCM 1.1(iii)**, not a shortcut. This **closes question 2**: I produce (a) a rigorous elementary proof for the sub-case `ξ_k>0`
(Herglotz, Lemma M1), and I identify (c) that the real case *must* be cited from
CCM 1.1(iii). The precise extra hypothesis the ground state must satisfy is **membership in a
de Branges space `H(E)` with `E` of HB type** (equivalently: interlacing `A`/`B` of its structure
function), which is the self-adjoint realization — not a combinatorial sign property. ### 2.5 Candor about severity
E1 feeds Hurwitz (E3) and N5c. Both inherit "modulo E1". The document's **🔧/GAP label
is correct and does not overstate**. My only refinement: the document suggests that the
own HB proof "remains open as a repair"; I am harsher: **at the level of the isolated
information, the own proof is essentially CCM 1.1(iii)** and not a pending sugar lemma.
Citing it as a black box is **legitimate**; presenting it as "closable with more work in
entire functions" would be **unjustified optimism**. Downgrade to: *mandatory citation of CCM*. --- ## 3. Rigorous verification of the analytic lemmas ### 3.1 N0 (double-exp Φ + incomplete Γ) — SOLID
The bound `Φ(u)≤Ce^{9u/2}e^{−πe^{2u}}` for `u≥0` is correct: the dominant term of `Φ` is
`2π²n⁴e^{9u/2}e^{−πn²e^{2u}}`, and `Σ_n n⁴ e^{−π(n²−1)e^{2u}} = O(1)` uniformly for `u≥0`
(the tail converges, dominated by `n=1`). Correct. The change `v=e^{2u}`, `du=dv/(2v)`, gives
`∫_T^∞ e^{(9/2+δ)u}e^{−πe^{2u}}du = ½∫_{e^{2T}}^∞ v^{(9/2+δ)/2−1}e^{−πv}dv
= ½∫ v^{5/4+δ/2}e^{−πv}dv = ½Γ(7/4+δ/2, πe^{2T})`. **Exponent verified:** `(9/2+δ)/2−1
= 9/4+δ/2−1 = 5/4+δ/2`. Correct.
The incomplete Gamma bound `∫_X^∞ v^a e^{−πv}dv ≤ C X^a e^{−πX}` for large `X` is standard
(integration by parts, the boundary term dominates when `a/(πX)→0`). With `X=e^{2T}=λ²`:
`(λ²)^{5/4+δ/2}e^{−πλ²}=λ^{5/2+δ}e^{−πλ²}`. **The proof of N0 is correct and robust.** SOLID. Minor remark (does not affect anything): the corollary "the strip grows up to `λ²/logλ`" is correct and in
fact underscores that Fourier truncation is **not** the obstruction. Fine. ### 3.2 N1 (off-axis transfer) — SOLID*, with a constant-level nuance
The construction `w(z)=log|F(z)|−τ·Im z` subharmonic on `H` is correct (`log|F|` subharmonic,
`τ Im z` harmonic). The invocation of **Boas Thm 6.2.4** (`|F(z)|≤Γ e^{τ|Im z|}` for `F` of
type `τ` bounded on ℝ) is **correct and is exactly the growth condition that makes
`w` bounded above**, enabling Phragmén–Lindelöf / harmonic majorant. Well invoked.
The harmonic measure bound of the segment from `iy₀`:
`ω_{[−R,R]}(iy₀)=(2/π)arctan(R/y₀)`, and `(2/π)arctan(R/y₀)≥1−(2/π)(y₀/R)` for `y₀≪R`
(because `arctan(R/y₀)=π/2−arctan(y₀/R)≥π/2−y₀/R`). **Verified.** SOLID*. **Nuance (harmless):** the bound `1−ω≤(2/π)(y₀/R)` is for the point `x₀=0`. For `|x₀|≤R/2` the
harmonic measure of the segment only **increases** (the point still "sees" the segment at
comparable angle), so `1−ω` remains `O(y₀/R)=O(λ^{−2})`. The document uses this
implicitly; it is correct but deserves a line. It changes nothing: `Γ^{1−ω}→1`. ### 3.3 N2 (amplitude) — SOLID, with a harmless overstatement
The Parseval identity `‖ξ̂‖²_{L²}=(πL/2)‖ξ‖²_{ℓ²}=πlogλ` (with `‖ξ‖_{ℓ²}=1`) is correct
via orthogonality of the `sinc_k`. Nikolskii/Plancherel–Pólya `‖g‖_∞≤C√τ‖g‖_{L²}` for
`g∈PW_τ`, `τ=logλ`, gives `‖ξ̂‖_∞≤C√(logλ)·√(πlogλ)=O(logλ)`. **This is proved and is SOLID.** **Discrepancy I flag:** the box in `RH-PROOF-FULL.md` and the Reduction sometimes claim
`Γ=O(1)` "with the normalization `ξ̂(0)=Ξ(0)`". What is **proved** is `Γ=O(logλ)`. The jump to
`O(1)` requires that the normalization at one point control the global sup, which **is not
proved** (plausible but not trivial: `Ξ(0)` is a fixed constant, but `‖ξ̂‖_∞`
could exceed `|ξ̂(0)|`). **It does not matter for the chain**, because the Reduction only needs
`Γ=poly(λ)` (so that `Γ^{1−ω}→1`), which `O(logλ)` gives with room to spare. I recommend **withdrawing
the claim `Γ=O(1)`** and keeping the proved `O(logλ)`. Correct label: SOLID for
what the chain needs. ### 3.4 N3 (amplification, Boas/PL) — SOLID
`g(z)=F(z)e^{iτz}` on `H`: `|g(x)|=|F(x)|≤M` on ℝ; `|g(z)|=|F(z)|e^{−τ Im z}` bounded on
sectors by the growth of type `τ`; Phragmén–Lindelöf on `H` (finite order, bounded on
the boundary) ⟹ `|g|≤M` on `H` ⟹ `|F(x+iy)|≤Me^{τy}` for `y≥0`; reflection for `y<0`.
**Correct, it is Boas 6.2.4.** Gives the factor `e^{τy}=λ^y≤λ^{1/2}`. SOLID. --- ## 4. Reduction + Hurwitz (E3) — SOLID (modulo E1). Validity of the Hurwitz step. **The Reduction's bound** `sup_{|Im z|≤½}|ξ̂_λ−Ξ|≤Cλ^{1/2}ε_loc+Cλ³e^{−πλ²}` is the sum
of N0 (`δ=½`: `λ^{5/2+½}=λ³`) and of N1/N3 (`e^{τ·½}ε_loc^ω Γ^{1−ω}=λ^{1/2}ε_loc·(1+o(1))`).
**Arithmetically and analytically correct.** Verified `5/2+δ=3` with `δ=½`. SOLID. **The Hurwitz step (E3), audited with severity:**
> If `ξ̂_λ→Ξ` **uniformly on compacta** of the open strip `|Im z|<½` (indeed
> `≤½+`), and each `ξ̂_λ` has **only real zeros**, then `Ξ` has no zeros in
> `0<|Im z|<½`. This is Hurwitz's theorem correctly applied: if `Ξ(z_0)=0` with `0<Im z_0<½`,
then by locally uniform convergence (and `Ξ≢0`), for large `λ` `ξ̂_λ` has a zero
in any neighborhood of `z_0` — but the zeros of `ξ̂_λ` are **real**, a contradiction.
**Valid.** Three conditions I verify are met:
1. **Locally uniform convergence** on the strip: given by the Reduction **if** `ε_loc=o(λ^{−½})` (that is the core hypothesis, unproved). Correct that it is conditional.
2. **`Ξ≢0`** (limit not identically zero): yes, `Ξ` is Riemann's xi. Correct.
3. **Real-rootedness of the `ξ̂_λ`**: **is E1**, the gap. Hurwitz **inherits modulo E1**. **Normalization/convergence-mode subtlety (question 3):** The document claims that the
normalization is "free" by Hurwitz invariance: if `c_λ ξ̂_λ→Ξ` with `c_λ≠0` and `ξ̂_λ`
real-rooted, then `Ξ` is real-rooted. **This is correct** — multiplying by `c_λ≠0` neither creates
nor destroys zeros, and Hurwitz only looks at zeros. **BUT** there is a real subtlety that the document
touches on but does not emphasize: applying Hurwitz requires **locally uniform convergence with
limit ≢0**, and the bound `λ^{1/2}ε_loc` controls the difference `ξ̂_λ−Ξ` **already normalized**
(same scale as `Ξ`). If one changed the normalization to `‖ξ̂_λ‖_{L²}=1` (as in III), the
limit would be `Ξ/‖Ξ_T‖_{L²}` and `‖Ξ_T‖_{L²}~√(logλ)→∞`, so `c_λ→0` and the "limit"
degenerates to 0 — **Hurwitz would not apply** under that normalization without renormalizing back. The
document is **consistent** (it uses `ξ̂_λ(0)=Ξ(0)`, fixed scale) but the claim "the
normalization is free" is **too loose**: it is free *modulo keeping the limit ≢0 and
finite*. I recommend specifying: the normalization must be such that `c_λ ξ̂_λ` converges to a
**finite, nonzero** limit (i.e. `c_λ` bounded away from 0 and ∞ over the family). With
`ξ̂_λ(0)=Ξ(0)` this is guaranteed. **Verdict: the Hurwitz step is valid; the "freedom of
normalization" should be stated as freedom modulo a non-degenerate limit.** SOLID modulo E1. **E4** (`Ξ∈LP ⟺ RH`): classical (de Branges / Pólya). SOLID, no objection. --- ## 5. N5c (converse discriminant) — SOLID* modulo E1
**Lemma N5c.1 (real-rooted monotonicity `|g(x+iy)|≥|g(x)|`):** the proof via the
Hadamard product is **correct**: `g(z)=ce^{az+b}z^m∏(1−z/r_n)e^{z/r_n}` with `r_n,a∈ℝ`, and
`|1−(x+iy)/r_n|²=(1−x/r_n)²+(y/r_n)²≥(1−x/r_n)²`. The factor `e^{a(x+iy)}` has modulus `e^{ax}`
independent of `y`. **Verified.** (Requires `g∈LP`, i.e. real-rooted, genus ≤1 — this is
E1 again.) Prop N5c.2 (DH does not converge off-axis) follows: at the off-line zero `z_0` of
`Ξ_f`, `|ξ̂_λ(z_0)−Ξ_f(z_0)|=|ξ̂_λ(z_0)|≥|ξ̂_λ(x_0)|→|Ξ_f(x_0)|>0`. The only fine hypothesis
is `Ξ_f(x_0)≠0`, which the document justifies (the real projection of an off-line zero is not an on-line
zero). **Correct, though it is worth noting:** there could in principle exist an on-line zero of
`Ξ_f` coinciding with `x_0`; for DH this is generically false and the argument holds,
but it is a generic hypothesis, not 100% unconditional. Harmless. **SOLID* modulo E1.** A good
result: it certifies that `ε_loc` separates true-RH from false-RH, with the false side proved. --- ## 6. RH-hard / conditional pieces — confirmation of labels - **H1′ (QW PSD ⟺ RH-up-to-T*):** correctly identified as RH-equivalent. PF gives structure (simple bottom, positive envelope), **not** spectral positivity `ε_0≥0`. The "PF≠PSD" correction is **correct and candid**. GAP=RH.
- **III:** correct conditional theorem given (H-gap)+(H-lim). The observation that **(H-pos) `ε_0>0` ≈ Weil-pos ≈ RH-up-to-T*** ("the renormalization bakes in RH") is **sharp and correct** — Davis–Kahan on `Â=A/ε_0` presupposes `ε_0>0` with relative gap, which is precisely what is to be shown. It is not an unconditional theorem. Conditional GAP.
- **IV.1:** identification of the limit operator — the constant-coefficient identifications are refuted; the reading "2nd-order SL with variable coefficients / compact Loewner kernel" is reasonable but **not proved**. It is **analysis (Landau–Widom/de Branges), not RH-hard**. I agree. GAP.
- **IV.2 ≡ §V:** the variational characterization ("Weil ground state = `Ξ_T` ⟺ all the `γ_ρ` real ⟺ RH") is **correct as an equivalence** and is **the RH core**. Under RH, the form `Σ_ρ|g(γ_ρ)|²≥0` is a sum of squares and its band-limited minimizer vanishes at the `γ_ρ≤T*` (modulo the rigor of the Landau–Beurling frame deficit). Without RH it is indefinite. **The 🟥 RH-equivalent label is correct and candid.** What is missing —the rate `o(λ^{−½})`— **is** RH. No objection to the label; the "rigor of the frame deficit" (`g_0=Ξ_T+O(ε_0)`) is a real sub-gap in Beurling–Landau theory, but it lives *under* the RH hypothesis, so it rescues nothing unconditionally. --- ## 7. Closable vs RH-hard (question 4) **Closable (genuine analysis, not RH):**
- **IV.1** — identifying the boundary operator (Landau–Widom / de Branges). Hard analysis but not RH. Closable in principle.
- **The "frame deficit"** `g_0→Ξ_T` under RH (Beurling–Landau at critical density). Closable, but it only refines the RH-side of the core; it does not advance unconditionally.
- **N1 nuance `x₀≠0`** and **withdrawing `Γ=O(1)`** → use `O(logλ)`: trivial expository corrections, already closable. **Essentially a mandatory citation (not closable as an own proof at this level):**
- **E1 real-rootedness** — at the level of the isolated information (de-modulated positive envelope), the carrier phase mismatch `ω*≠π` blocks the elementary Herglotz/HB route. It is **CCM Thm 1.1(iii)** (real spectrum of the self-adjoint realization). My sub-case `ξ_k>0` (Lemma M1) is closed but **does not cover the real ground state**. Mandatory citation, not repairable with entire-function sugar. **RH-hard (the wall, not closable without proving RH):**
- **IV.2 ≡ §V** — `ξ̂_∞=Ξ` / `ε_loc=o(λ^{−½})` / "Weil ground state = `Ξ_T`". **It is RH.**
- **H1′ (`ε_0≥0`)** and **(H-pos) in III** — Weil positivity = RH-up-to-T*. **It is RH.** --- ## 8. Conclusion of the tribunal (cold) The CCM program, audited through the lens of complex analysis, is a **correct and
elegant reduction of RH to a single RH-equivalent core** (IV.2≡§V: the Weil ground state is `Ξ_T`),
**surrounded by a genuinely proved approximation scaffolding** (N0, N1, N2, N3, Reduction,
Hurwitz). That scaffolding **withstands severe audit**: the proofs of N0 (incomplete Γ),
N1 (harmonic measure + Boas), N2 (Nikolskii) and N3 (Phragmén–Lindelöf) are **correct**, and the
Hurwitz step is **valid** modulo E1, with a necessary precision about the "freedom of
normalization" (it must preserve a non-degenerate limit). **What I close in my lens (E1):** a rigorous elementary proof (Herglotz, Lemma M1) of the sub-case
`ξ_k>0`, and a **precise identification** of why the real ground state (carrier `ω*≈0.966π`)
**does not** fall into that case nor into its de-modulation, so that real-rootedness **must** be cited
from CCM Thm 1.1(iii) (self-adjoint realization / de Branges space `H(E)`), not from a
pending entire-function lemma. I am harsher than the document here: **it is not "closable with
more work"; it is a mandatory citation.** **What remains open:** (i) E1 with no proof of its own (mandatory citation CCM 1.1(iii)); (ii) III
conditional with (H-pos)=RH; (iii) the IV.2≡§V core which **is** RH. **RH is not proved.** The
document is **candid**: I detect no self-deception in the localization. The corrections I request
(withdraw `Γ=O(1)`, specify the freedom of normalization, harden the status of E1 to "mandatory
citation", flag the generic hypothesis in N5c) are **expository, not structural.** *— H., referee.*
