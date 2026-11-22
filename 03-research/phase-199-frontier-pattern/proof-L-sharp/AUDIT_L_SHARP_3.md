# AUDIT_L_SHARP_3 — audit of K_001 and P_001 (+ P_001_numerics.py) against AUDIT_L_SHARP_2 (★★)

Phase 199, ,
and
Sources checked: AUDIT_L_SHARP_2 §7 ((★★_u), (★★_EM), (★★_St), constraints 1–11); F_001 (Thm F.2); J_001 (Thm J.3, §4.1);
A_001 (Thm 1.1); PATTERN_001 §2 (Mori V κ table); ROUTES-TRIED-INDEX/AUDIT_ZENODO_FRONTIER §B1 (Mori VIII margin);
Paper 46 (no statement of P46 is touched by K or P, so there is nothing to integrate). Prolate facts (CITED): Slepian–Pollak 1961,
Slepian 1965 (Hermite limit), Fuchs 1964 (1−λ_n(c) ≈ √π 2^{3n+2}c^{n+½}e^{−2c}/n!), and Slepian's identity
∂_cλ_n = (2/c)λ_nψ_n(1)² (normalisation ∫_{−1}^{1}ψ_n² = 1). Recomputations were done in a scratchpad and are not stored in the repo.

**Verdict in one line.** K.1b, K.3, P.1 and P.2 survive. K.1a is weaker than stated. K.4's "index 4" reading is a fitted
exponent, not a mechanism, and contradicts K's own constraint count. P.4 is reproduced at μ = 5 only after a hidden quadrature
parameter is fixed, and it is NOT converged at μ = 15. Nothing here is a sign. (★★) OPEN; row D OPEN.

## 1. K.1a / K.1b (priority 1)
- **f(0) = 0 is free: PROVED, with one caveat.** The claim g = Ef|_I depends only on f|_{|x|>1/λ} is correct, so a zero-mass bump in
  (−1/λ,1/λ) changes neither g nor f̂(0) nor W_T. The bump does, however, have an O(1) out-of-band tail. Its Fourier scale is λ,
  and its amplitude must be ψ₀(0) ≍ c^{1/4}λ^{−1/2}. Leakage 1−λ is therefore **not invariant** under moves that leave the form
  unchanged. Any "W ≍ κ·(leakage)" law is a statement about a proxy, and the honest denominator is dist²(ρ,𝒢̄₁) as in (★★).
  This caveat applies to every prolate law below.
- **The cost of f(λ) = 0 is understated.** Slepian's identity combined with Fuchs gives ψ_n(1)² ≈ c(1−λ_n), so |ψ₀(1)| ≍ c^{3/4}e^{−c}.
  This part is correct. But a C² cutoff of width 1/c has energy ≍ ψ(1)²/c ≍ (1−λ_n), and it lives at frequency ≍ c, so it leaks
  at O(1) relative rate. The repair cost is therefore **of the same order as the vector's own defect**, not negligible against
  1−λ₀ in any sense. It is negligible only after K.1b, against 1−λ₂ (the gain is the factor c^{−2}). K.1a(f(λ)) is downgraded
  to ARGUED, valid at the 1−λ₂ scale.
- **K.1b: PROVED, given the CITED Hermite limit.** h₀(0) = π^{−1/4} and h₂(0) = H₂(0)/√(8√π) = −π^{−1/4}/√2. With
  ψ̂_n(0) ∝ i^nψ_n(0), we get ψ̂₂(0)/ψ̂₀(0) → +1/√2, so α = −√2(1+O(1/c)) ✓. Double orthogonality gives
  leak = (1−λ₀) + 2(1−λ₂). With ‖f‖² = 3, this is (2/3)(1−λ₂), and Fuchs gives (1−λ₂)/(1−λ₀) = (8²/2!)c² = 32c², hence
  (64/3)c²(1−λ₀) ✓.
  Stronger form (new, PROVED modulo Fuchs): the minimum of the leakage Rayleigh quotient over even admissible vectors
  (f̂(0) = 0) is (2/3)(1−λ₂)(1+O(c^{−2})). Lagrange gives a_n ∝ ψ̂_n(0)/(1−λ_n), and adding ψ₄ costs (1−λ₄)/(1−λ₂) ≍ c².

## 2. K.3: circularity of J.3's Poisson step on PW data (priority 2). PROVED.
Poisson summation in n of Σ_n r(nu) returns u^{−1}Σ_k f(k/u). The dual frequencies k/u with k < λu lie inside supp f, so they
are O(1). They are the window samples, i.e. A Thm 1.1 read backwards (Ψ_f = Zr_f). Smooth deep data (J.3) have these terms
superpolynomially small. PW data do not, because the scale-1/μ oscillation is exactly the aliasing scale (constraint 5,
AUDIT_2 §3.5). The "O(c^{−2})·0.046" ranking of the J.3 anatomy is ARGUED: it uses |B| ≲ C_c/c from one integration by parts
on the Langer tail (K.2, CITED). The NO-GO is for the technique, as stated. It is not a class NO-GO.

## 3. Numerical comparison (priority 3). Recomputed.
Fuchs at c = 30π gives the following values (n = 0…6): 9.4447e−81, 7.1212e−78, 2.6846e−75, 6.7472e−73, **1.2718e−70**,
1.9178e−68, 2.41e−66. The ratio (1−λ₄)/(1−λ₀) = (8⁴/4!)c⁴ = 1.3466e10 ✓. Mori VIII's certified margin is
2.40e−70 = **1.887**·(1−λ₄) ✓ and 5.02e5·μ⁴(1−λ₀) ✓.
**What "1.89" is.** It is the ratio of two different objects:
- the numerator is the bottom eigenvalue of a compressed Schur complement in Mori's certificate. That is a quantity of the
  full constrained form λ^W, attached to no vector;
- the denominator is the leading Fuchs asymptotic (the O(1/c) correction is not included) for the unrepaired ψ₄.
So the comparison is **not apples-to-apples**, and 1.89 has no structural meaning. The apples-to-apples datum is Mori V's
Galerkin λ_min (NUMÉRICO, CITED via PATTERN_001). At μ = 15 its ratio to (1−λ₄) is 4.63, not 1.89.
**Is "κ-band index 4, κ ≈ 1.9" fair?** No, on two counts.
(i) Mori V's ratios are λ_min/(1−λ₄) ∈ [4.11, 5.34] for μ ∈ {7, 11, …, 20}. Refitting λ_min/(1−λ_n) against log μ gives
slopes 2.14 / 1.14 / **0.14** / −0.86 / −1.86 for n = 2…6. The data fix only the exponent of c in
λ_min ≈ C·c^{β}e^{−2c}, with β ≈ 4.64. The "index" n and a polynomial prefactor μ^{a} are **not separately identifiable**:
index 4 with κ ∝ μ^{0.14} is the same fit as index 2 with κ ∝ μ^{2.14}.
(ii) Fair wording: "λ_min ≈ (4–5)·(1−λ₄(2πμ)) on 7 ≤ μ ≤ 20 (Galerkin, NUMÉRICO); the certified margin at μ = 15 is
1.9× the same scale".
The certified margins at μ = 10 and μ = 12 (Mori VI/VII) are **not in hand** (PATTERN_001 table: "not in hand"), so the
stability of the certified ratio cannot be tested. The Galerkin ratio at μ = 12 is 4.11.

## 4. "ψ₄ is the natural extremal vector" (priority 4). Downgraded: the honest count says 2, not 4.
For even f there are three conditions.
- f(0) = 0 is free (§1).
- f̂(0) = 0 is one effective linear constraint, of cost ≍ 1−λ₂.
- f(λ) = 0 is cheap at the scale of the vector's own defect (§1).
The admissible set is therefore codimension 1 in the even prolate span for any leakage-type quotient. By interlacing, the
extremal vector is ψ₀ − √2ψ₂ at scale (2/3)(1−λ₂), i.e. **index 2**. If f(λ) = 0 is counted as a hard constraint, the
admissible set has codimension 2 and the generic solution in span{ψ₀,ψ₂,ψ₄} has a nonzero ψ₄ component. Interlacing then
only bounds the minimum above by ≍ 1−λ₄; it does not say the minimum equals 1−λ₄.
K's sentence "ψ₂ repairs along ψ₀/ψ₄ with defect 1−λ₄ when ψ₀ is excluded" assumes ψ₀ is excluded, and nothing in the
constraint list excludes it. If the empirical exponent β ≈ 4.6 is real, it therefore needs **two more effective null
directions** than the listed constraints provide. A candidate (ARGUED only) is the two pole functionals A = F(1) and
B = F(0) of 2AB. Mechanism OPEN. K.4's "consistent with K.1b" is RETRACTED.

## 5. P.1 / P.2 / P.3 (priority 5)
- **P.1: PROVED.** This is two lines of algebra from Q(F₀,F₀) = 0 and Q(F,G) = Q(F₀,G) + Q(G,G). It is a rewriting, not information.
- **P.2: PROVED, with a gap closed here.** As written, the integrand contains (ζ′/ζ)(1−s). That factor alone has poles at
  s = 1−ρ inside 0 < Re s < ½, which the left shift crosses. The correct justification is
  −ζ(s)(ζ′/ζ)(1−s) = −χ(s)ζ′(1−s) (functional equation). That function is meromorphic, with poles only at s = 0 (from ζ′ at 1)
  and at odd s ≥ 1 (from Γ(1−s)). It uses no zero information.
  - At s = 0: χ(s) ≈ s/2 and ζ′(1−s) ≈ −1/s², so the residue is ½·R(1)F(0) = −ζ(0)R(1)B ✓.
  - Shifting right past s = 1: χ ≈ −2/(s−1) and ζ′(0) = −½log 2π. The residue is −R(0)[log 2π·A + F_log(1)], so
    Q(F₀,F) = I_c + R(0)[log 2π·A + F_log(1)] ✓.
  - Growth on Re s = c′: |χ| ≍ |τ|^{½−c′} ✓.
  The memo's parenthetical "(equivalently the Γ_ℝ pole of Θ_∞)" is loose but harmless. No numerical check of P.2 exists: the
  script prints the residue terms but never evaluates J_{c′} or I_c. Recommended: compute J_{c′} at c′ = −¼ in
  the same basis.
- **P.3: PROVED as a statement about this split.** After P.1, every determinant reduction needs −Q(G,G) ≥ 0, which is
  (★★) up to the cross term. The argument is circular, as stated.

## 6. P.4 numerics (priority 6). Spot-checked; partially reproduced.
- **F/G split in the script: correct.** I_n(s) = ∫_n^{n+1}ρX^{−s}. The cumulative sums give ζ_X(1−s), so F = ∫ρX^{−s}ζ_X(1−s)dX.
  F₀ = ζ(1−s)R, G = F − F₀, and Θ_∞ = Re ψ(¼+iτ/2) − log π ✓. Q(F,G) = C + Q_G ✓.
- Stale comment: the comment says the basis is t^{2k}, but the code uses cos(kπt/μ), and the memo is right.
- **Hidden parameter.** The Gauss–Legendre node count per unit interval (argv[5]) is not reported. With 16 nodes at τ ≤ 800
  (μ = 5), the top eigenvalue is 354.7 (garbage), because X^{−iτ} makes ≈ 127 oscillations per unit at X ≈ 1. With 120 / 250
  / 450 nodes at τ ≤ 200 / 400 / 800, the results are:
  - top eig 𝔔: 12.09 / 12.39 / 12.57;
  - ‖Q(F,G)‖/‖Q(F)‖: 0.061 / 0.059 / 0.058;
  - Q(G,G) all ≤ 0 (bottom eigenvalues ~1e−15, i.e. noise);
  - the dt-halving check is stable.
  So μ = 5 reproduces the memo, but the top eigenvalue is still drifting by ≈ 1.5% per doubling of τ.
- **μ = 15 is NOT converged.** With N = 60:
  - τ ≤ 600 (350 nodes): spectrum top 2.97, with two negative 𝔔 eigenvalues (−1.2e−3, −3.7e−4);
  - τ ≤ 1000 (550 nodes): top 7.30, min 1.0e−7 (matches the memo).
  That is a factor 2.5 between cutoffs. The Mellin bandwidth of ρ is ≈ 2πμX (≈ 94X at μ = 15), so τ ≤ 1000 cannot be
  adequate. The memo's "consistent at τ ≤ 1000" is unsupported, and every μ = 15 number in P.4 (0.0011, 0.22, 0.55) is
  NUMÉRICO-unconverged.
- **New finding (NUMÉRICO, μ = 5 only).** 2symQ(F,G) is effectively low-rank and pole-controlled at μ = 5.
  - Its eigenvalues are −1.45, +0.06, −7e−3, then below 4e−4.
  - ‖P⊥Q(F,G)P⊥‖/‖Q(F,G)‖ = 0.036 / 6e−6 / 5e−9 with 2 / 4 / 6 pole functionals.
  - 𝔔 and −Q(G,G) agree eigenvalue by eigenvalue down to 1.6e−12 (relative differences 0.1–0.5%).
  This is **more** than the memo claims for μ = 5, and it contradicts "not finite-rank". The only counter-evidence is the
  unconverged μ = 15 run.
- **Structural or artefact?** Undecided.
  - The 10-dimensional smooth basis is not constrained: the radical and ĝ(0) = 0 are not imposed.
  - The bottom of the true spectrum, ≍ e^{−4πμ}, is invisible at μ = 15: min 1e−7 against ~1e−70.
  - The operator-norm ratios are dominated by the top of the spectrum.
  Precise statement for testing:
  **Conjecture (C_G) (OPEN; NUMÉRICO support only at μ = 5).** There are θ < 1, κ > 0 and A such that for every μ ≥ 5
  and every ρ ∈ PW_μ with ĝ(0) = 0 and ρ ⊥ 𝒢̄₁ (radical removed):
  (a) |2Q(F,G) + 2A(ρ)B(ρ)| ≤ θ·(−Q(G,G));
  (b) −Q(G(ρ),G(ρ)) ≥ κμ^{−A}dist²(ρ,𝒢̄₁).
  (a) and (b) together imply (★★_P) = L′♯. Part (b) is a sign statement of the same type as (★★), so (C_G) is a
  re-localisation onto the Euler–Maclaurin defect, not a reduction. Its value is that (a) is a *comparison* and could be
  attacked by the pole structure of P.2. Required test before any use: a converged μ = 15 run (τ ≳ 2πμ·X_eff with
  X_eff ≈ 10, nodes ≳ τ/2), with the constraints imposed and a prolate-adapted basis.

## 7. Updated (★★) and constraints
**(★★) unchanged:** (★★_u) = (★★_EM) = (★★_St) = L′♯, base case μ ≤ 15 (H.1). P adds one more PROVED-equivalent spelling:
  (★★_P)  −Q(G,G) + 2Q(F,G) + 2AB ≥ κμ^{−A}dist²(ρ,𝒢̄₁)
This is a rewriting by P.1. Conjecture (C_G) is a sufficient split, OPEN.
Constraints 1–11 stand. Added:
**12. No E-image of a single prolate with small repair.** Admissibility (f̂(0) = 0) costs an O(1) component along ψ₂ (K.1b). The
leakage-minimal admissible even vector has defect (2/3)(1−λ₂). Leakage is not invariant under radical moves (§1), so prolate
laws are proxies and the denominator must be dist²(ρ,𝒢̄₁). The empirical scale c^{4.6}e^{−2c} of λ_min is not explained by
the listed constraints (§4).
**13. The pole couples only through residues of rank one.** The F₀-piece of 2AB is exactly the s = 0 residue
½R(1)F(0) (left shift), or R(0)[log 2π·A + F_log(1)] (right shift). Both are computed through −χ(s)ζ′(1−s) with no zero
information. The remaining couplings J_{c′} and I_c are full bilinear forms with no sign and no proved finite rank. The μ = 5
low-rank observation (§6) is NUMÉRICO only.
**Do not retry:** J.3-type Poisson-in-m evaluation on PW tails; "Eψ₀ + small correction"; "κ-band index" readings that are
built from the ratio of a certificate margin to the leakage of a single unrepaired prolate; Mellin-side numerics of 𝔔
without a reported quadrature and a cutoff ≳ 2πμX_eff.

## 8. Label table
| item | memo | audit |
|---|---|---|
| K.1a f(0) = 0 free | PROVED | PROVED (form level); leakage not invariant |
| K.1a f(λ) = 0 cost | ARGUED, negligible | ARGUED; same order as the own defect, negligible only against 1−λ₂ |
| K.1b α = −√2, leak (64/3)c²(1−λ₀) | PROVED given CITED | PROVED given CITED; minimality over the admissible span PROVED mod Fuchs |
| K.2 Langer tail | CITED/ARGUED | unchanged |
| K.3 circularity | PROVED, technique NO-GO | PROVED; O(c^{−2})·0.046 ranking ARGUED |
| K.4 a = 4, κ₀ ≈ 5e5, 1.89 | NUMÉRICO | numbers ✓; "1.89" not apples-to-apples; index not identifiable (exponent β ≈ 4.64 only); "consistent with K.1b" RETRACTED |
| K "ψ₄ natural extremal" | ARGUED | downgraded: the honest count gives index 2; index 4 needs two unexplained null directions |
| P.1 | PROVED | PROVED (rewriting) |
| P.2 | PROVED | PROVED after the χ-rewriting (gap closed here); not checked numerically |
| P.3 | PROVED | PROVED for this split |
| P.4 μ = 5 | NUMÉRICO | reproduced (quadrature parameter required); Q(F,G) low-rank NUMÉRICO |
| P.4 μ = 15 | NUMÉRICO | NOT converged (factor 2.5 between τ ≤ 600 and τ ≤ 1000; negative eigenvalues at 600) |
| conjecture (P) NO-GO | NO-GO | "Q(G,G) ≤ 0" stands at μ = 5; "not finite-rank" UNSUPPORTED (μ = 5 contradicts, μ = 15 unconverged) → downgraded to OPEN |
| (C_G) | — | OPEN (stated here) |

No sign is claimed. (★★) OPEN. Row D OPEN.
