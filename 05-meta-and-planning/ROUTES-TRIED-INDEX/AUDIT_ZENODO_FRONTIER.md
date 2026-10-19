# Audit : Zenodo frontier items (survey S1 B1, B2, B3, B5, B8)

Read-only, adversarial audit. Paper 47 not edited. Sources were downloaded to a scratch directory, not the repo.

## 0. Common conventions
Every item writes Weil's form in the logarithmic variable as Q(f) = 2|∫f cosh(x/2)|² − 2|∫f sinh(x/2)|² + (1/2π)∫a(t)|F_f(t)|²dt − 2Σ_{n<e^{2L}} Λ(n)n^{-1/2} Re∫f·conj f(x−log n), with a(t) = Re ψ(1/4+it/2) − log π. Note that 2|c|² − 2|s|² = 2Re(F(i/2)·conj F(−i/2)) = 2Re(A B̄). So Q = W_T = 𝔞_T + 2Re(AB̄), the complete form with the pole term kept, on L²(I_T), with **L = T** (the support half-width). This is the same matching as Liu (AUDIT_LIU §2).
- "Width log μ" (Mori) means e^{2L} = μ, that is **T = ½ log μ**. So "width log 15" is **T = ½log15 = 1.354025** (prime powers 2,3,4,5,7,8,9,11,13). The answer to the question in the brief is yes.
- Mori V and Guo use the multiplicative window [λ⁻¹,λ] on L²(du/u). This is unitarily equivalent to L²([−log λ, log λ]), so T = log λ and μ = λ² = e^{2T}.
- Ziad uses odd functions with ∫u sinh(x/2) = 0. On odd functions ∫u cosh = 0 holds automatically, so this is exactly **the odd sector of Paper 47's primitive space P_T** (both Tate moments vanish), and λ₁ is the odd-sector primitive bottom.
- Domain: C² or C_c^∞ functions are a form core of the closed form (same remark as in the Liu audit), so the bounds pass to λ^W_T.

## B1. Mori, "Weil positivity on the window of width log 15" (zenodo 23281236; code 23092422 v1.6.2 = github moriryota/prolate-weil-bounds certificate-VIII; data 23281176)
(a) Theorem O: Q(f) ≥ 2^{-2904}‖f‖² for every complex C² function f with supp f ⊂ [−½log15, ½log15]. In our notation: **λ^W_T ≥ 2^{-2904} at T = ½log15**. By lem:monoT this holds for all T ≤ ½log15. Since λ^W ≤ λ^P ≤ λ_A, it also gives λ_A > 0 there.
Proof chain:
- bounded comparison (Liu framework plus Mori papers VII/IX, i.e. the log 10 and log 12 papers, which were not audited here);
- weighted Schur bound ‖C_p‖ ≤ 66/16;
- out-of-band tail with C = log(Ω/2π) − 1/Ω − γ and Ω = 736;
- Legendre projection with N = 1664 (832 modes per parity);
- block elimination;
- the finite matrix inequality (2.2) certified in Arb by a congruence test.
(b) Rigor and reproducibility:
- The code and 1.8 GB of data are public (Apache/CC-BY), with SHA-pinned sources.
- Checker and proposer are separate programs, and there is an independent re-check. Seven mutation tests were rejected.
- AI-generated (Claude/GPT), not refereed, not formalized.

**My independent recomputation (mpmath, no shared code):**
- c = ΩL = 996.5625
- −log₂ d(c) = 2900.286
- C = 0.1369944
- u₀E₀ = 0.136844 < C and u₁E₁ = 0.136341 < C
- Cδ ≥ 2^{-2904} holds
- max R_w on a 2·10⁵-point grid = 4.09133 ≤ 66/16 = 4.125 (paper: 4.0915 on 2304 Arb cells)

The author's scalars.py also passes (log₂(α+βb²) = −697.74 < −697).

Gap: the shipped independent_scalars.py fails because notes/0792_claude_lowmem_generator/scalar_mu15.json is missing from the release. This is minor.

**§B1-run (done , scratchpad).**
- Code: github v1.6.2 certificate-VIII.
- Data: 46 files fetched from github raw; all SHA-256 sums match; restore.py reports "all 24 data files restored and verified".
- Ran `check_certificate.py --bits 1280` (python-flint 0.9.0) in 283 s, 3.5 GB. Result: **PASS_EXTERNAL_CERTIFICATE**.
- λ_min(T) ≥ 2.3979369226737e−70 (even) and 3.9458005898258e−66 (odd), with ε_T = 4.79e−94. These are exactly the paper's Table 2.
- Independent entry check: A₀₀ (even) = γ − ⟨v₀, C_p v₀⟩ = 37/8 − Σ_{n<15} Λ(n)n^{-1/2}·2(2L−log n)/(2L) = 1.3127070815421376549595321292 by my own mpmath. It agrees with the packet's dyadic centre to 40 digits. This confirms the prime set (including 13) and the normalization.
- Not done: regenerating J (7800 s/parity); the analytic lemmas of papers VII/IX.

(c) Consistency with our data:
- Fuchs: 1−λ₄(c) ≈ (4√π 8⁴/4!) c^{9/2} e^{-2c}, with c = 2πμ.
- At μ = 15 this gives about 1.5e−70. Times Mori's Galerkin ratio of 4–5, that is about 7e−70.
- The certified finite margin is 2.40e−70 (even), the lowest eigenvalue of a Schur complement of M+V, which must be ≥ λ_min of the compressed form. **The orders of magnitude match.**
- The certificate does resolve levels about 10⁻⁷⁰. It does so with 3328-bit arithmetic, and all paid errors are < 2^{-300} ≈ 5e−91.
- The final constant 2^{-2904} ≈ 10^{-874} is the out-of-band δ ~ e^{-2ΩL}. It sits far below the true bottom, so there is no tension.
- Our NUMÉRICO μ_even ≤ 2.5e−22 at T = 1 (BARRIER_Z_001, M = 64, not converged and still decreasing with M) is an upper bound. It is consistent with the Fuchs-model value of about 9e−30 at μ = e². Our Galerkin data simply do not resolve the bottom at T ≥ 1. This needs no correction, but it should be recorded: **the true bottom at T = 1 is plausibly ~1e−29**.
- **Margin plausible.**

Verdict: **VERIFIED (computational part)**. The certificate was reproduced, and the scalars and the A entry were checked independently. The analytic reduction of papers VII/IX (Prop 3.1, Lemma 3.2, block elimination) was not re-proved here. Label for Paper 47/index: **CITED** (unrefereed, AI-generated, but externally reproducible). λ^W_T ≥ 2^{-2904} for T ≤ ½log15.

## B2. Mori, "Improved upper bounds for windowed Weil forms with exponential factor e^{-4πμ}" (zenodo 23363767, v3; concept 23175060)
(a) Theorem K, unconditional. With λ_min = λ^W_T and T = ½log μ:
- λ_min ≤ 3.50e24 μ^{9/2} log μ e^{-4πμ} for 50 ≤ μ ≤ 10⁴;
- λ_min ≤ 7.58e24 μ⁵(log μ)³ e^{-4πμ} for all μ ≥ 50.
Method: an explicit smoothed prolate test vector, with the zero sum bounded using RH verified up to 3·10¹² and a zero-free region. These are upper bounds only. Conjecture 1.2 is λ_min ≍ μ^{9/2}e^{-4πμ}. The earlier bound from the same series is 1.362e9 λ^{46} e^{-4πλ²} for μ ≥ 5 (cited by Guo).

(d) Comparison with ours. cor:margin1 is λ_A ≤ 4e9·T·e^{-15.449T}, which is **singly** exponential in T. Mori's bound is **doubly** exponential: exp(−4πe^{2T}).

| T | cor:margin1 | Mori 1.362e9 μ^{23}e^{-4πμ} (μ ≥ 5) | Mori Thm K value (proved only for μ ≥ 50) |
|---|---|---|---|
| 1.0 | 781 (vacuous) | 6e−12 | (2.7e−12) |
| ½log15 | 4.5 (vacuous) | 2e−46 | (2.6e−52) |
| 1.956 (μ = 50) | 5.9e−4 | 2e−225 | 8e−241 |
| 2.5 | 1.7e−7 | 1e−751 | 1e−775 |

cor:margin1 bounds λ_A, while Mori bounds λ^W ≤ λ_A, so the two are not directly comparable. Mori uses zero data (verified RH up to a height and a zero-free region); Paper 47 cor:margin1 removes one zero via the testfam family. Even so, as a ceiling on certificate methods **Mori's bound is overwhelmingly stronger** for λ^W, and it supersedes the "e^{-15.449T}" scale as the quantitative barrier for any complete-form certificate. prop:env (τ_env doubly exponential in T) is consistent with this: both say the resolution needed grows like exp(e^{2T}).

Verdict: **PLAUSIBLE-UNVERIFIED**. The proof was not checked line by line; the bound is consistent with the B1 margin and with the Fuchs asymptotics. Recommended label: CITED.

## B3. Guo Chen, "Prolate leakage and near-zero spectral clusters…" (zenodo 23297284)
(a) Theorem 1.1: for λ ≥ Λ_m, A_λ has ≥ m eigenvalues in [−δ_m, δ_m], δ_m ≲ λ^{4m+17/2}e^{-πλ²}, via the summation map E applied to prolates with f(0) = f̂(0) = 0. This is an exact residual identity (Thm 4.5) plus transfer and nondegeneracy.
The constants are astronomical: log Λ_m ≤ 700(4m+5)⁴. Theorem 1.8 (m = 1) needs λ ≥ 2^{15}/√(2π) for part (b), and λ ≥ 232 (T ≥ 5.4) for parts (d) and (e).
**This is vacuous at every window we work at (T ≤ 2).** Its value is structural: an unconditional NO-GO quantifier saying the near-kernel has growing multiplicity. Any lower-bound method must separate m clustered eigenvalues at scale e^{-πμ}. It is the multiplicity version of the CCM mechanism (L06/L39).

Verdict: **PLAUSIBLE-UNVERIFIED** (classical ingredients; not checked line by line). Record in the index as a NO-GO quantifier, not as a route.

## B5. Senke, window (−77/64, 77/64) (zenodo 22871384, v0.3)
The record is **Restricted**: no files are public. Only the description is available. It describes a cellwise Schur certificate plus a Binet tail plus a dyadic transfer, with prime powers 2,3,4,5,7,8,9,11 and T = 1.203125.
Nothing can be checked. The window is also superseded in range by Mori ½log12 = 1.242 and ½log15 = 1.354.

Verdict: **UNVERIFIABLE (restricted)**. This is treated as PLAUSIBLE-UNVERIFIED at most. Do not cite.

## B8. Ziad, "Localized constrained Weil forms: near-degeneracy and a Davenport–Heilbronn first kernel" (zenodo 23145455)
(a) Zeta, odd primitive sector at T = ½log7: 0 < λ₁ < 5.0023e−19.
- The upper bound comes from an 80-mode Legendre witness: archimedean 0.2157094617577142245 against prime −0.2157094617577142240. Arb, ±3.8e−51.
- The lower bound comes from a 431-mode head plus an analytic tail (Schur).
- The coefficients are not published; the record contains only the PDF, and "no separate Git repository".
- The result is consistent with our μ_odd (3.8e−18 to 5.3e−20 at T = 1, not converged).

(e) DH witness: the form for F = Σa_n n^{-s} with a_n periodic mod 5 (0, 1, κ, −κ, −1), gamma factor Γ((s+1)/2)(5/π)^{(s+1)/2}, α = 3/4, coefficients b_n/√n from −F′/F. These coefficients are real but **not supported on prime powers** (for example b₆ = (1+κ²)log6 ≠ 0), and **there is no Euler product and no pole**.
- The constraint ⊥ sinh(x/2) is imposed artificially.
- Positivity holds for a ≤ ½log2: no shifts, and an analytic floor of 0.4289.
- The negative witness at a = 9/5: 140 sine modes, Rayleigh quotient −6.1690e−9 ± 4e−23 (archimedean 2.38352025058 against arithmetic up to n ≤ 36, −2.38352025675).
- **Admissibility:** the witness is exactly constrained, odd and supported in (−9/5, 9/5), so as a test function it lies in the odd part of our P_T with T = 9/5. But the form is **not** our W_T: archimedean kernel K_{3/4}, conductor 5, and non-prime-power coefficients. It is therefore a falsifier only for method classes that use nothing beyond the functional equation, a gamma factor and a Dirichlet series (no multiplicativity of the coefficients, no Euler product). It is not a datum about W_T.
- Its window 9/5 = 1.8 lies well beyond our working windows. The first-loss scale is bracketed only loosely: (½log2, 9/5).
- Plausibility: DH's first off-line zero is near 0.808 + 85.7i. The witness bandwidth is 140π/1.8 ≈ 244, enough to reach it. A 9-digit cancellation is of the kind expected near a first crossing. The result is plausible.

Verdict: **PLAUSIBLE-UNVERIFIED** (not reproducible: coefficients and code are absent). Use: add to the index as falsifier test **F-DH**: "any proposed carrier/certificate method that does not use the Euler product must fail for DH at some a < 9/5". This complements the Beurling and cΛ falsifiers. This is consistent with the semiring principle (the sign must come from the (ℕ,+,·) structure).

## Index actions
- B1: record the frontier datum (CITED pending human review). The certified first-contact lower bound moves from 17/16 (Liu) to ½log15 = 1.354. Route class: dual certificate / bounded comparison (KNOWN; no new mechanism for all T).
- B2: record the doubly exponential ceiling exp(−4πe^{2T}) as the quantitative barrier for complete-form certificates.
- B3: record as a NO-GO quantifier (multiplicity of the near-kernel).
- B5: UNVERIFIABLE, superseded.
- B8: record falsifier F-DH, with the caveat that its form is not W_T.
