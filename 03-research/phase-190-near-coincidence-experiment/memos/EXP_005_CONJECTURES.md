# EXP_005 — Candidate ζ-specific facts, stated as conjectures, tested, and checked against the index

Rule applied (task brief, W-pat): a regularity shared with any control is NOT ζ-specific. Controls = a₃, a₅, amp2(c), pert_n(±10⁻⁵, ±10⁻²),
Beurling (2 seeds, two lattices), Poisson (5 seeds), M₁ (δ = 0.1, 0.3). Index barriers named as in `06_OPEN_RESIDUES_DEAD_SUBROUTES.md`.

## 0. Headline
**No prime-side structural fact about Near was found that holds for Λ and fails for every control.** Every regularity of Near that is
visible at the resolution of the experiment falls into one of three classes: (a) shared with at least one control (not ζ-specific);
(b) an exact identity that is already indexed as wall W7 (linear use of Λ*1 = log) and carries no sign; (c) ζ-specific but a zero-side
observation (the minimizer encodes the zeros), hence in class C_zeros of cor:void — admissible as an observed mechanism, not as a prime-side
input. The table in §1 records each regularity with its class; §2 states the three ζ-specific statements as precise conjectures, with
their status and the honest assessment of a proof route; §3 records the non-ζ-specific regularities so that they are not retried.

## 1. Regularity table
| # | regularity | Λ | fails for which controls | shared with | class |
|---|---|---|---|---|---|
| R1 | A_M ⪰ 0 for all M computed, λ_min = M^{−3+o(1)} > 0 | yes (3 T₀, 2 b) | ALL (every control indefinite at M ≤ 400) | none | the target itself (R9) |
| R2 | amplification threshold c*(M) ≍ λ_min/0.18 ≍ M^{−3}; ∂λ_min/∂v₂ = O(1) | yes | — (it is a property of Λ's criticality) | — | prop:wit-sens, [sens] |
| R3 | bottom eigenvector entrywise positive, ≈ m^{−½} (overlap 0.993), global | yes | all (controls' bottom vectors are localized packets at the top scale) | none | (c) zero-side: P_v vanishes at γ_j |
| R4 | P_v(γ_j) → 0 for the minimizer, ratio to generic M^{−1.5…−2} | yes | all | none | (c) C_zeros |
| R5 | Near_n(v) + Div_n(v) = 0 to 3 decimals for every atom n ≥ 5 on the minimizer | yes | holds for any comb on smooth vectors (Tate + Riemann sum) | all | (a) analytic |
| R6 | the comb balance Σ_n δ_n(v) = Arch(v) − λ is carried by n = 2, 3, 4 only | yes | the controls' negative vectors also load n = 2, 3 (and 5) | partly | (a)+(target) |
| R7 | exact identity s^T(Div+Near)s = 2Σ_N N^{−½}log N·E_M(N) for s = m^{−½} | yes (12 digits) | a_P, amp2, pert (Σ_{n\|N}a(n) ≠ log N), Beurling on ℤ, Poisson; NOT M₁ (same Div/Near) | M₁ | (b) W7 |
| R8 | Div(v) ≈ log M + O(1), Near(v) ≈ −Div(v) + O(1) on the minimizer / on m^{−½} | yes | holds for a_P (density 1), Poisson (density 1), M₁ | all density-1 combs | (a) PNT-level (C_PNT) |
| R9 | 2×2 band: sup_{d≤15}|B(d)| ≤ a₀ with sup/a₀ = 0.942 (T₀ = 0.3) | yes | Poisson, Beurling (T₀ = 0.3), a₅ | a₃, amp2(0.05), pert₂(1.01) pass to d = 15 | (a); necessary only (L2_023) |
| R10 | near-saturation of the band without violation (sup/a₀ → 1 along d, recurrence) | yes (0.74, 0.94, 0.86… per unit range) | a₃ also 0.99 | a₃ | (a) and zero-side (Bohr recurrence of a discrete spectral measure) |
| R11 | Near matrix statistics: ‖Near‖ ≈ 0.17M, full rank, 56 % positive entries, mass ∝ Λ(n)n^{−3/2}, ⟂ Arch⁻ | yes | identical to 5 digits for pert(10⁻⁵) | all ε-perturbations | (a) by construction ([sens]) |
| R12 | Near mass by additive shift h flat in h | yes | all | all | (a) (L2_030 §1(c)) |
| R13 | (Ω₀): S_T(Λ) < 0 on [0.55, 1.10], margin 𝔞_T(φ₀) ≥ 0.016 | yes | a₃, a₅ (T ≥ 0.6), Poisson, amp2(0.5) at T ≤ 0.5 | amp2(0.05), pert₂(±10⁻²) pass at every T | (a); R2 necessary only |

## 2. The ζ-specific statements as conjectures
**Conjecture C1 (criticality law).** For every profile F₀ of Theorem S with 2T₀ < log 2: λ_min(A_M(Λ)) > 0 for all M and
λ_min(A_M(Λ)) = M^{−3+o(1)}. Equivalently, the amplification threshold c*(M) at n = 2 is ≍ M^{−3}.
Status: NUMÉRICO (M ≤ 2000, three T₀, two b; exponent 2.89 → 2.98 monotonically approaching 3). The first half is problem (S) = R9 verbatim
(no progress on it here). The exponent is a new quantitative statement. Proof route: the only mechanism identified is zero-side (EXP_003 §2,
Fact N2): with the spectral measure of B written as a positive measure μ (which exists exactly when the first half holds), the minimizer
annihilates P_v on the support of μ up to height ≍ M and the remainder is the F̂₀²-tail ∫_{≳M}τ^{−4}dN(τ) ≍ M^{−3}log M. That route assumes
the first half and uses the location of supp μ: it is C_zeros information and does not escape [zeros]. No prime-side route is visible.
Test harder: the exponent could be sharpened by computing λ_min with 30-digit arithmetic at M ≤ 300 (feasible: the kernels are
one-dimensional integrals; the matrix eigenproblem at 30 digits and M = 300 costs minutes); not done here because it cannot change the class.

**Conjecture C2 (minimizer law).** The bottom eigenvector v_M of A_M(Λ) is entrywise positive for all M, ⟨v_M, m^{−½}/‖m^{−½}‖⟩ ≥ 0.99, and
its Dirichlet polynomial satisfies P_{v_M}(γ) → 0 for every zero ordinate γ with F̂₀(γ) ≠ 0.
Status: NUMÉRICO (M ≤ 1200, T₀ = 0.3, 0.15; overlaps 0.9932–0.9937; |P_v(γ_j)|/generic = 10⁻³ → 7·10⁻⁷). Entrywise positivity is not
Perron–Frobenius (A_M is not a Z-matrix, EXP_003 §5). Proof route: zero-side only (same as C1). Index: C_zeros; also consistent with
thm:finZ (no finite set of zeros suffices: the minimizer must annihilate ≍ M zeros, growing with M). Not a prime-side fact.
Value for the programme: it identifies the sign-carrying vector of (S) concretely — m^{−½} with a 0.7 % correction — which no previous memo had
(L2_028 §3 analysed m^{−½} on Near-free resonators only). The corresponding test function is G = Σ_m m^{−½}(1+ε_m)V_{log m}F₀, i.e. the profile
convolved with the (corrected) Dirichlet series of ζ at ½ truncated at M.

**Conjecture C3 (lattice balance identity, PROVED-elementary, W7 class).** For s = m^{−½} on {1, …, M} and every comb a on ℕ with
Σ_{n|N}a(n) = ℓ(N): s^T(Div_a + Near_a)s = 2Σ_N N^{−½}ℓ(N)E_M(N), E_M(N) = Σ_{m≤M}m^{−½}c₀(log(N/m)); for Λ, ℓ = log. E_M(N) is the Riemann-sum
defect of a Tate-annihilated integral and satisfies E_M(N) → 0 as N → ∞ with N ≪ M (observed |E_M(N)| ≤ 2·10⁻⁶ for 50 ≤ N ≤ 400 at M = 800),
with E_M(2), E_M(3), E_M(4) = 0.78, 0.64, 0.29 (T₀ = 0.3).
Status: identity PROVED (one line: regroup the triple sum by N = kn and use Σ_{n|N}v_n n^{½}·(kn)^{−½}k^{−½}… — precisely
Σ_n v_n Σ_k k^{−½}Σ_m m^{−½}c₀(log(kn/m)) = Σ_N E_M(N)N^{−½}Σ_{n|N}2Λ(n)); decay of E_M(N): ARGUED (Euler–Maclaurin for the C² function c₀ at
spacing 1/N). Checked to 12 digits. ζ-specific in the weak sense that ℓ = log characterises combs with Σ_{n|N}a(n) = log N, which M₁ also has.
Index: W7 (linear use of Λ*1 = log) — "equals a window shift or cancels in thresholds"; here it gives the exact value of the comb part on
one vector where A_M is positive with margin (2.58/7.26). Not a sign source; recorded so that it is not rediscovered.

## 3. Regularities that are NOT ζ-specific (do not retry)
* R5/R8: per-atom Tate cancellation and the log M growth of Div(v) with Near(v) ≈ −Div(v): analytic/PNT-level; shared by all density-1 combs.
* R9/R10: the 2×2 band and its near-saturation: passed by a₃ to d = 15 at T₀ = 0.3 and by every arithmetic control at T₀ ≤ 0.15.
* R11/R12: every matrix statistic of Near (norms, singular values, sign fractions, atom and shift mass, alignments) — identical for the
  10⁻⁵ perturbations, which are indefinite from M = 200–400. By [sens] no such statistic can be ζ-specific.
* Packet-family margins (EXP_003 §6): separate a₃/Poisson from Λ, not the ε-perturbations nor M₁; [crit].

## 4. What the experiment does establish about problem (S) (for the record; proposed index rows)
Proposed rows for `04_PHASES_100-189.md` Part I (phase 190) — NOT written to the index:
| ID | Route | Tool family | Where | Outcome | Why |
|---|---|---|---|---|---|
| P190-N1 | λ_min(A_M(Λ)) = M^{−3+o(1)} > 0, c*(M) ≍ M^{−3}; every control indefinite at M ≤ 400 | numerics/discovery | phase-190 EXP_002/003 | NUMÉRICO (no sign contact; M ≤ 3000 at double precision) | criticality of A_M(Λ): any Near-statistic route dies by [sens] |
| P190-N2 | minimizer of A_M(Λ) ≈ m^{−½} with P_v(γ_j) → 0; controls fail on top-scale packets | numerics/discovery | EXP_003 §2, EXP_002 §3 | NUMÉRICO, zero-side (C_zeros) | identifies the sign-carrying vector; mechanism is zero-side |
| P190-C3 | lattice balance identity on m^{−½} (Div+Near = 2Σ N^{−½}log N E_M(N)); defect at N = 2, 3, 4 only | Euler/Möbius algebra | EXP_003 §4 | PROVED (identity), W7 class, no sign | positive with margin on m^{−½}; sign is in the 0.7 % correction |
| P190-band | 2×2 band to d = 15 for 12 combs; a₃ passes, indefinite at M = 50 | numerics | EXP_002 §5 | NUMÉRICO; confirms L2_023 | band necessary only |
| P190-Ω₀ | (Ω₀) on [0.40, 1.10] with controls | numerics | EXP_004 | NUMÉRICO | see EXP_004 |
Proposed note for `06_` R9: "Discovery run (phase 190): the sign of A_M(Λ) is decided on v ≈ m^{−½}(1 + ε), ε = 0.7 %, with Div ≈ log M,
Near ≈ −Div, Arch ≈ 0.3; per-atom defects only at n = 2, 3, 4; λ_min ≍ M^{−3}. No prime-side Near structure separates Λ from the 10⁻⁵
perturbations (which are indefinite from M ≈ 200). Admissible direction unchanged (joint control of Near with Arch); the vector on which it
must act is now explicit."

## 5. The correction ε is a cutoff, not an arithmetic function (done in this phase; scripts/epsilon.py, data/epsilon_T0*.json)
r_m := v_m√m/v_1 (r ≡ 1 for pure m^{−½}). At fixed m, r_m → 1 as M grows: max_{m≤30}|r_m − 1| = 0.058 (M = 100), 0.051 (200), 0.010 (400),
0.007 (800), 0.0035 (1200) at T₀ = 0.3 (T₀ = 0.15: 0.022 at M = 200, 0.005 at 800); the multiplicativity test r_{ab}/(r_a r_b) = 1 ± 0.003
for coprime a, b ≤ 11 is consistent with r ≡ 1, not with a nontrivial multiplicative correction. At fixed m/M the correction is stable:
r(0.5M) = 0.89–0.95, r(0.8M) = 0.84–0.85, r(M) = 0.19 (M = 400…1200). So **the minimizer is m^{−½}·w_M(m/M) with a smooth cutoff w (≈ 1 on
[0, 0.4M], decreasing to ≈ 0.2 at M) plus noise ≤ 0.4 % at small m.** Consequences: (i) Conjecture C2 has no arithmetic content beyond
m^{−½}: P_v(τ) = Σ m^{−½+iτ}w(m/M) is a smoothed partial sum of the Dirichlet series of ζ(½ + iτ), and its vanishing at the ordinates
γ_j (R4) is the statement that smoothed partial sums approximate ζ(½ + iτ) = 0 there — a classical fact about ζ's Dirichlet series
(zero-side, as classified). (ii) The sign-carrying family of problem (S) is explicit and one-dimensional in shape:
  s_w = (m^{−½}w(m/M))_{m≤M},  Q_M(w) := s_w^T A_M s_w = (1/2π)∫F̂₀(τ)²|Σ_{m≤M}m^{−½+iτ}w(m/M)|²[m(τ) − Σ_{n<Me^{2T₀}}v_n cos(τ log n)]dτ,
the twisted second moment of a smoothed partial sum of ζ(½+iτ) against the profile and the truncated comb density. Q_M(1) = 2.58 (M = 800,
‖s‖² = 7.26), Q_M(cos²) = 2·10⁻⁴, Q_M(w_opt) = λ_min‖s‖²-scale ≈ 10⁻⁸: positive with margin for flat cutoffs (provable at PNT level, as in
L2_028 §3), critical for the optimal cutoff.

## 6. Exact next step
Not another statistic of Near, and not larger M. The object is Q_M(w) of §5 on the explicit family s_w. Two concrete steps, both prime-side
in formulation, both checkable against [void] before any investment:
1. Write Q_M(w) = 𝒜_M(w) − 𝒟_M(w) − 𝒩_M(w) by hand with the C3-type regrouping: 𝒟 + 𝒩 = Σ_N N^{−½}Σ_{n|N}2Λ(n)w((N/n)/M)·E^w_M(N), E^w_M(N) =
   Σ_m m^{−½}w(m/M)c₀(log(N/m)); determine for which w the Λ*1 = log collapse of C3 survives (w flat on the support of E^w_M(N) for N ≤ M e^{−2T₀},
   i.e. the bulk) and isolate the edge terms N ≈ M, where w is not flat and the comb is sampled at scale M with weight w(k/M) — that edge is where
   the controls' negative packets sit (EXP_002 §3) and where the ε-sensitivity enters. This gives an explicit decomposition of Q_M(w) into
   (bulk: defects at N = 2, 3, 4 against archimedean energy, PNT-free) + (edge: a shifted-convolution sum of Λ at scale M against w). It is
   a pen-and-paper computation of a few pages; its value is to state the (S) problem as "edge term ≤ bulk margin for every w", with both sides
   explicit. The admissible direction of R9 (joint control of Near with Arch on vectors that see near-coincidences) then has a named vector
   and a named edge.
2. Test by hand whether the edge term for w_opt is of the size of a PNT error at scale M (then [void] applies and the route is a
   reformulation: REF-D) or of the size of the bulk margin M^{−3} (then the balance is a genuinely new inequality on Λ at scale M, to be compared
   with the twisted-sum formulations (E_γ)/(N_loc) of R1/R5). The numbers of this phase predict the second: the margin is M^{−3} while the
   edge packets of the ε-perturbations change the form by ε·M (EXP_002), so the edge term is O(M)·(comb fluctuation at scale M) and the
   inequality it must satisfy is sharp to M^{−3} — the same exponent-½-at-resolution-e^{2T} requirement recorded for (N_loc). This is
   recorded as the expected outcome, not as a result.
Everything else in this phase (bigger M, more controls, higher precision, more Near statistics) cannot change the classification of §1.
