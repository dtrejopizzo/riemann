# EI_003 — The beyond-window Euler product Z_X, the window Hardy function Z_T, the phase identity σ_T = 2Θ_X′, and the rigidity theorem: no exact identity makes the symbol non-linear in Λ

Construction round (phase 192), starting point (iii) of the mandate (minimizer ↔ partial sums of ζ, FE applied exactly). Pen and paper.

**No sign certified; no negative value of 𝔞_T for ζ.**

## 0. Corpus check — why not a retry
R163_603 (cell 3C): coupling of the first-contact witness with a mollified Hardy function via Riemann–Siegel/AFE — DEAD (F3: M_m; W3′: FE-only
data shared by f_χ). N_BUILD_005 / L2_011 row 8: partial Euler products and real powers in 𝔄_T — NO-GO (no sign). L2_012 §3: comb = −∂_s log(M+B).
None defines the beyond-window Euler product Z_X := ζ/Z_{<X} with Z_{<X} = exp(Σ_{n<X}Λ(n)n^{−s}/log n), states σ_T = −2Re(Z_X′/Z_X) on the line,
or proves the rigidity statement of §3. Not a retry: R163_603 coupled a *witness* to Z; here Z_T is a rewriting of the *symbol* and the
result is a NO-GO theorem for a class of constructions (the mandate's "non-linear in Λ" on the symbol side), plus the exact (iii) object.

## 1. Objects (all PROVED/elementary)
X = e^{2T}. Z_{<X}(s) := exp(Σ_{n<X}Λ(n)n^{−s}/log n): entire, zero-free, = Π_{p<X}(1−p^{−s})^{−1}·Π_{p<X}exp(−Σ_{k: p^k ≥ X}p^{−ks}/k) for Re s > 0.
Z_X(s) := ζ(s)/Z_{<X}(s) = exp(Σ_{n≥X}Λ(n)n^{−s}/log n) (Re s > 1) = 1 + Σ_{n≥X}z_X(n)n^{−s}, z_X ≥ 0: a Dirichlet series with nonnegative
coefficients, **no coefficient in 1 < n < X**, meromorphic on ℂ with exactly the zeros and the pole of ζ. −Z_X′/Z_X = R_X = −ζ′/ζ − P_X.
Θ_X(τ) := θ(τ) − Σ_{n<X}Λ(n)n^{−½}sin(τ log n)/log n, θ(τ) = Im log Γ(¼+iτ/2) − (τ/2)log π the Riemann–Siegel theta (CITED).
Z_T(τ) := e^{iΘ_X(τ)}Z_X(½+iτ) = Z(τ)·exp(−Σ_{n<X}Λ(n)n^{−½}cos(τ log n)/log n), Z the Hardy function.

**Theorem 1 (phase identity; PROVED).** (i) θ′ = ½m (differentiate Im log Γ(¼+iτ/2)); hence σ_T(τ) = 2Θ_X′(τ) and
  𝔞_T(F) = (1/π)∫Θ_X′(τ)|F̂(τ)|²dτ   for every F in the form domain.
(ii) Z_T is real and even on ℝ, vanishes exactly at the critical-line ordinates of ζ, and off them
  R_X(½+iτ) = Θ_X′(τ) + i·Z_T′(τ)/Z_T(τ):
the Euler tail beyond the window, on the line, has real part = half the window symbol and imaginary part = the logarithmic derivative of Z_T.
(iii) The window form at T is the comb-free form of the object Z_X with archimedean factor Γ_ℝ(s)·Z_{<X}(s): the whole window comb is absorbed
exactly into an entire zero-free change of Γ-factor, and the FE of Z_X reads Z_X(1−s) = Z_X(s)·[Γ-ratio]·Z_{<X}(s)/Z_{<X}(1−s).
*Proof.* (i) prop:boundary/lem:K. (ii) arg ζ(½+iτ) = −θ(τ) mod π, arg Z_{<X}(½+iτ) = Im Σ_{n<X}Λ(n)n^{−½−iτ}/log n = −Σ sin(τ log n)Λ(n)n^{−½}/log n, so
arg Z_X = −Θ_X mod π and e^{iΘ_X}Z_X is real; |Z_X| = |ζ|/|Z_{<X}| gives the second expression; d/dτ log Z_T = iΘ_X′ + i(Z_X′/Z_X)(½+iτ) is real,
so Re(Z_X′/Z_X) = −Θ_X′ and Z_T′/Z_T = −Im(Z_X′/Z_X) = Im R_X. (iii) is the definition. ∎

## 2. The (iii) object: 𝔞_T on the smoothed partial sum of ζ, exactly
With the family of EI_002 (G_M = Σ_m m^{−½}w(m/M)V_{log m}F₀, spectral density F̂₀²|ζ_w(½+iτ;M)|²) and EI_002 Theorem 2:
  𝔞_T(G_M) = (1/π)∫F̂₀(τ)²|c·ζ(½+iτ) + M^{½−iτ}W(½−iτ) + ρ_M(½+iτ)|²·Θ_{X′}′(τ)dτ,   X′ = Me^{2T₀},                                    (2.1)
and, writing ζ(½+iτ) = e^{−iθ(τ)}Z(τ) (FE, CITED) and M^{½−iτ} = M^{½}e^{−iτ log M}: the cross term c·ζ·M^{½+iτ}W̄ carries the phase e^{i(θ(τ) − τ log M)},
whose stationary point θ′(τ) = log M, i.e. ½m(τ) = log M, is at τ ≈ 2πM — the **integer resolution** of prop:shape-crit(c) (B2c), where
the comb RMS equals m. PROVED (identity) / the location of the stationary point is elementary. At that height M^{½}|W(½−iτ)| ≪ M^{½−k}
(w smooth), so the Riemann–Siegel saddle of the test contributes nothing of the size of the margin: the beyond-Nyquist tail of (2.1)
(|τ| > M^{1−ε}, where ρ_M is not small) is the only place the family's spectral density differs from c²F̂₀²|ζ|². ARGUED for the size, PROVED
for the identity.
**Exact AFE on the test (Riemann–Siegel with exact error as identity; CITED).** For |τ| ≤ M^{1−ε} the test is c·ζ(½+iτ) up to M^{−Aε}; applying
the Riemann–Siegel formula to ζ(½+iτ) at bounded height τ gives the two sums of length ≍ √(τ/2π) = O(1) plus the exact Riemann–Siegel integral:
nothing of the comb length X′ appears. The mandate's hope — "the ℤ-Poisson dual of the partial sum produces the comb term exactly" — fails
for a structural reason: the Poisson dual of the test is the polar term + ρ_M (EI_002 Thm 2), while the comb sits in the **symbol** Θ_{X′}′,
which is untouched by any transformation of the test. PROVED (by (2.1): test and symbol are separate factors).

## 3. Theorem 2 (symbol rigidity; PROVED)
Let 𝔖 be the set of expressions for σ_T obtained from the data of ζ by any finite chain of: the functional equation (Hamburger/Riemann),
the Euler product, Mellin inversion, Poisson summation on ℤ or ℤ², and Riemann–Siegel/AFE identities applied to ζ, ζ′/ζ or partial sums.
Then every member of 𝔖, as a function on ℝ, equals σ_T(τ) = 2Θ_X′(τ) = m(τ) − 2Re P_X(½+iτ), which is **affine in the vector (Λ(n))_{n<X}**;
and every identity in 𝔖 that introduces the zeros of ζ is the explicit formula (thm:Z / lem:roughEF).
*Proof.* σ_T depends on ζ only through the real function m on ℝ and the finite vector (Λ(n))_{n<X} (prop:finite(iv)); m is the boundary value
−2Re ζ′/ζ = 2θ′ (prop:boundary), i.e. the FE used once; the Euler product is log-linear in Λ (log Z_{<X} = Σ Λ(n)n^{−s}/log n is linear in Λ by
definition), so −∂_s log of any partial or complete Euler product is linear in Λ; Mellin, Poisson and AFE are linear operations on the
functions they act on and preserve the affine dependence on Λ of −ζ′/ζ − P_X; the only non-affine rewriting of the tail R_X is through
the zeros (Perron/explicit formula), which is the excluded class. ∎
**Corollary (the shape of the mandate).** The conjunction {exact identity on the window form, non-linear in Λ, not through h*(Λ), not REF-D}
is empty on the symbol side. Non-linearity in Λ can enter an exact identity only (a) through the minimizer h* = h*(Λ) (resolvent — EI_001,
Lemma S, REF-D by R186_029 Lemma H(ii)), or (b) through the **test** when the test is built from ζ's own coefficients (|ζ_w|², EI_002 /
(2.1) here), in which case the form is a twisted second moment of ζ against an affine symbol. PROVED (from Theorem 2 and EI_001–002).

## 4. What (2.1) and the phase identity do and do not give
- Θ_X is an exact "window-corrected" Riemann–Siegel phase; positivity of 𝔞_T on P_T says that the phase velocity Θ_X′ correlates positively
  with every primitive spectral density. Z_T′/Z_T = Im R_X is its Hilbert-transform partner only if R_X is holomorphic in Re s > ½ — a zero
  statement (κ), not used.
- Z_X = 1 + Σ_{n≥X}z_X(n)n^{−s} has nonnegative coefficients supported beyond the window: positivity of the *coefficients* gives nothing on
  the line (W-loc, thm:nolocal). Absorbing the comb into the Γ-factor (Theorem 1(iii)) is exact and sign-free (N_BUILD_005's NO-GO on partial
  products restated).
- On the family, (2.1) with Theorem 1(i): 𝔞_T(G_M) = (1/π)∫F̂₀²|ζ_w|²Θ_{X′}′ = (2/π)∫F̂₀²|ζ_w|² Re R_{X′}: the (iii) object is the twisted second
  moment of the smoothed partial sum against the beyond-window Euler tail; Theorem 2 says it cannot be made "manifestly positive" by any
  exact transformation that does not go through the zeros.

## 5. Review (self)
1. Theorem 1(i): θ′(τ) = ½Re ψ(¼+iτ/2) − ½log π = ½m. ✓ (ii): branch of arg handled mod π; Z_T real since e^{iΘ}Z_X has argument 0 mod π. ✓
   The identity R_X = Θ_X′ + iZ_T′/Z_T is valid off the ordinates; at ordinates Z_T′/Z_T has a simple pole, as R_X does. ✓
2. (2.1): product of EI_002 Theorem 2 and Theorem 1(i). ✓ The stationary-phase remark is heuristic (ARGUED) and is not used for any sign.
3. Theorem 2: the proof is prop:finite(iv) + the observation that log of an Euler product is linear in Λ; "any finite chain" is made precise
   as: operations that are linear on the function they act on, applied to −ζ′/ζ − P_X or to functions equal to it on ℝ. A reader may
   object that "exp" of the Euler product (ζ itself) is non-linear in Λ — correct, and that is exactly case (b) of the Corollary: it enters
   through the test, never through σ_T. ✓
4. Zero information: none used; the Hilbert-transform remark is explicitly excluded. ✓
5. R163_603 overlap: that memo used Z to couple to a witness and died by F3; here Z_T is a rewriting of σ_T and the output is a NO-GO
   theorem, not a route. ✓
6. No numerics; no estimate; no sign claimed. ✓

## 6. Compliance table
| clause | status | note |
|---|---|---|
| MUST-NOT: estimate with remainder | ✓ | all identities exact; the RS/AFE remainder is kept as an identity (CITED) |
| MUST-NOT: O1–O15 invariant | ✓ by identification | Z_X, Θ_X use ζ's exact comb and Γ_ℝ; a_P (no FE), E_Q (no Euler), Beurling (no ℤ) have no Z_T |
| MUST-NOT: class / statistic / opcalc / certificate / zeros / σ-transport / induction / REF-D | ✓ | Theorem 2 is a NO-GO for a class of constructions, not a deduction of the sign |
| MUST: exact identity on h*_T / s* | ✓ | Theorem 1 holds on every test; (2.1) on the family |
| MUST: Λ non-linear | ✗ on the symbol (Theorem 2: impossible); ✓ on the test (|ζ_w|²) | |
| MUST: Euler × FE × ℤ jointly as mechanism | partial | FE: θ and Z; Euler: Z_{<X}, Z_X; ℤ: coefficients 1 in the test — joint in (2.1) as factors |
| MUST: doubly-exponential margin from the identity | ✗ | none produced |
| MUST: fluctuation not density | ✓ structure | Θ_X′ = θ′ − comb: the density part of the comb is in θ′ via the FE |
| MUST: 10⁻⁵-sensitive | ✓ inherited | Z_{<X} changes with every weight |
| MUST: names ζ vs ζ_K | ✓ named | Z_T uses Γ_ℝ and the comb on log ℕ; for ζ_K the phase θ_K and the comb on log N(𝔞) differ |
| (R)(1)–(10) | as EI_002, with (3) ✗ on the symbol side (now a theorem) and (4) ✓ | |

## 7. Column bookkeeping
Moved from YES to NO, now as a PROVED statement rather than a failed attempt: "non-linear in Λ" on the symbol side (Theorem 2) — the
mandate's clause can only be met through h*(Λ) (REF-D channel) or through tests built from ζ's coefficients (twisted second moment).
Kept in YES: exact identity; no remainder; no zeros; FE enters beyond m (θ, Z); ℤ via coefficients 1; sensitivity; naming of ζ vs ζ_K.
Not obtained: any margin; any sign.
