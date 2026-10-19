# EI_002 — Review

prop:wit-cheb, prop:sharp, prop:boundary, subsec:band, thm:kappa, thm:sos, def:PD, lem:shape-lin, lem:shape-restate, prob:region),
SHAPE_THEOREM, SPEC_B, index 06_ R9. Pen and paper.

## Verdict
**EXCLUDED (O1–O5, O7, O11, O15: every identity survives every modification; "fails by identification" is not a property of the deduction); identities Thm 1, Thm 2 (split), Thm 3(i) bulk, Thm 3(iii), Thm 4 CONFIRMED PROVED; FIX on three points (§2), one of them a false PROVED upgrade (Fact N2); sign content REF-D (T*₃(η) = (S), SPEC_B §1.4).** No SI-column property moves; the README's "ℤ-integrality as mechanism: YES" for this object is rejected.

## 1. Line-by-line check
| claim | check | label |
|---|---|---|
| Thm 1 | prop:AM(ii) + m = −2Re ζ′/ζ(½+iτ) (prop:boundary, off ordinates; Re of the simple-pole term i m_ρ/(τ−γ) is continuous) + Σv_n cos = 2Re P_{X′}; |P_s|² = |ζ_w(½−iτ)|² = |ζ_w(½+iτ)|² (w real). | CONFIRMED (one-line rewriting, as the memo says) |
| (2.1) polar-free | 𝓕_T = 2∫y^{−½}c_F(log y)d(ψ−y) (prop:wit-cheb) and 𝔞_T = 𝔞^♯ − 𝓕_T with m^♯ = m + (¼+τ²)^{−1} (lem:polarelim); comb of G_M sees only n < X′. | CONFIRMED |
| Thm 2, (3.1) | Mellin inversion with c₀ > ½, Σ_n n^{−s}(n/M)^{−z} = M^zζ(s+z); shift to Re z = −A crossing z = 0 (res. w(0)ζ(s)) and z = 1−s (res. M^{1−s}W(1−s)); W(z) = −(1/z)∫w′x^z, w′ ∈ C_c^∞(η,1) ⇒ single pole, rapid vertical decay; ζ polynomial growth (CITED). Condition "A ∉ {½, 3/2, …}" is unnecessary (no further poles) — harmless. | CONFIRMED PROVED (standard smoothed AFE/Perron; cf. L2_012 §2 "coefficient-1 AFE = Poisson on ℤ") |
| size |ρ_M| ≪ M^{−A}(1+|τ|)^A | convexity on Re = ½ − A. | CONFIRMED (CITED) |
| **Corollary (Fact N2 → PROVED)** | at a low ordinate γ: ζ_w(½+iγ) = M^{½−iγ}W(½−iγ) + ρ_M. The bound "≪ M^{½}(1+|γ|)^{−k}" is **large**, of size M^{½}·|W(½−iγ)|, for bounded γ (γ₁ ≈ 14.13): (1+|γ|)^{−k} is decay in γ, not in M. The family does **not** annihilate the low zeros; it takes the value of the polar (ℓ = 0 Poisson) term there, which is the dominant term of the test at every bounded τ (the length-M partial sum of ζ(½+iτ) at bounded height is ≍ M^{½}, not ≍ |ζ|). Annihilation of a low ordinate on the family ⟺ W(½−iγ) ≈ 0, a condition on w, not a theorem. | **FIX — false as stated; Fact N2 stays NUMÉRICO**. If phase 190's observation is right, Thm 2 turns it into: the A_M-minimizer's cutoff w_M has Mellin transform ≈ 0 at the low ordinates on Re z = ½ (zero-side, descriptive) |
| Thm 3 framework (ℤ²-Poisson) | g_n(x,y) = (xy)^{−½}w(x/M)w(y/M)c₀(log x − log y − log n): support is the wedge ny e^{−2T₀} < x < ny e^{2T₀}, 0 < y < M, whose closure **contains the origin**; g_n ~ c²(xy)^{−½} there (integrable, not smooth, not compactly supported in (0,∞)²). "Support touches neither axis" is wrong. The lattice sum is over m, k ≥ 1, i.e. y ≥ 1, and the memo itself needs the cut y ≥ 1 in (iii); with the cut, g_n1_{y≥1} has a jump at y = 1, so ĝ_n decays only like 1/|ℓ₂| in that direction and Poisson holds only as Euler–Maclaurin with boundary terms (conditional convergence), not "with absolute convergence". | **FIX** (bookkeeping; the regrouping is correct once the boundary terms are kept, as (iii) partly does) |
| Thm 3(i), (0,0) term | ĝ_n(0,0) = n^{½}∫dy w(y/M)∫dv e^{v/2}c₀(v)w(nye^v/M) (re-derived: (xy)^{−½}dx = n^{½}e^{v/2}dv). Bulk: w(nye^v/M) ≡ c ⇒ c∫e^{v/2}c₀ = 0 (first Tate condition). Edge: Taylor in v; constant and linear terms vanish by ∫e^{v/2}c₀ = 0 and ∫v e^{v/2}c₀ = 0 — the latter is the second-order vanishing of ĉ₀ = F̂₀² at −i/2 (rem:Kprim / lem:transl(iii)): correct. Remainder is a genuine quadratic term ½(a²w″ + aw′)κ₂, nonzero at the edge. | CONFIRMED PROVED (bulk and edge expansion). **Note**: it uses only the two Tate conditions, i.e. the polar/archimedean structure of F₀; the ℤ-lattice plays no role in the vanishing |
| Thm 3(ii) self-duality | phase e^{−2πiy(ℓ₁ne^v+ℓ₂)}; |Ŵ_v(ξ)| ≪ M(1+M|ξ|)^{−k} (smooth in y, scale M — again only without the cut); dual support −ℓ₂ ≈ ℓ₁n. | CONFIRMED (structural; = N_BUILD_009 §1 self-duality on ℤ², as the memo says) |
| Thm 3(iii) | Σv_nĝ_n(0,0) = 2ΣΛ(n)Ψ(n); ∫₀^∞Ψ = M∫w·∫_{y≥1}w(y/M)dy/y·∫e^{−v/2}c₀ = 0 with the cut (without it, ∞·0); Ψ = 0 for u ≥ X′; ∫Ψdψ = ∫_{[2,X′)}Ψd(ψ−u) − ∫₀²Ψdu. | CONFIRMED PROVED as identity |
| Thm 5(a) | U_{T′} ≠ ∅ (subsec:band; thm:kappa(iv) g₁(0) = C₀+4 < 0) ⇒ no termwise sign. | CONFIRMED |
| Thm 5(b),(c) | record (thm:sos, def:PD, thm:Z; L2_012 §2(a)). | CONFIRMED (CITED internal) |
| Thm 5(d) "not estimable below M^{−3}" | shows that the single bound M^{−A}(1+|τ|)^A against F̂₀²|ζ|m^♯ integrates only for A < 3 − 1/6. That excludes one estimate, not all; the memo's own (e) shows why: for |τ| ≳ M the remainder is O(1) and the τ^{−4} profile tail gives ∫_M^∞τ^{−4} ≍ M^{−3} — the family's M^{−3} law is the profile's beyond-Nyquist tail. | **downgrade PROVED → ARGUED** |

## 2. FIXes
1. Corollary of §3 (Fact N2 upgrade): withdraw; see table. The README line "Fact N2 (phase 190) upgraded NUMÉRICO → PROVED" must be removed.
2. Thm 3 framework: support/corner singularity and the y ≥ 1 cut (boundary terms, decay 1/ℓ₂); state Poisson as Euler–Maclaurin with explicit boundary terms or restrict to k ≥ 2 and treat k = 1 separately.
3. Thm 5(d): ARGUED.

## 3. MUST-NOT clauses, tested
Property set: "Theorems 1–5 hold for the form q tested on s_w". Apply the modification to the comb/form and ask whether the identities survive.
| clause | survives? |
|---|---|
| O1–O5 (comb modifications) | Thm 1: yes with R^{(a)}_X := −ζ_a′/ζ_a − P^{(a)}_X; (2.1): yes with ψ_a; Thm 2: yes (a statement about the test only); Thm 3: yes (Tate conditions only); Thm 5(a): yes (U_T′ ≠ ∅ for the modified symbol at the relevant windows, or negative bottom outright). **EXCLUDED by O1** |
| O6/O11 Beurling | Thm 1, 3: yes (any positive atoms at positions e^{u_j}); Thm 2: yes (test unchanged); Λ∗1 = log in D_X: holds formally (SHAPE table, O6 "keeps Λ*1 = log formally") |
| O7 a_P | all yes: ζ_{a_P} = ζΠ_{p<P}(1−p^{−s}); D^{(a_P)}_X = ζ_{a_P}R^{(a_P)}_X has coefficients a_P∗(coeff of ζ_{a_P}) ≥ 0 |
| O8a quartets, O8b f_t, O9 ζ̃, O10 Epstein | Thm 1 with the model's own symbol: yes; Thm 2: yes; Thm 3: yes; D_X ≥ 0 fails for Epstein (no Euler product) — but Thm 5 is a NO-GO, not a deduction, so nothing is lost |
| O12 ζ_K | all yes with ψ_K, Γ_K; the "naming" (Poisson on 𝒪_K differs) is not used at any line |
| O13, O14 | yes / n.a. |
| O15 Poisson positions | all yes (positions enter Thm 3 only through c₀(log x − log y − u_j)); the ℤ²-lattice is the **test** lattice (m, k), a choice of the prover, not a property of the comb |
| B4 | the collapse Λ∗1 = log is linear (W7) — memo concedes |
| B8 | T*₃(η) ⟺ D for η ≤ η₀ (SPEC_B §1.4, CONDITIONAL on NUMÉRICO) — REF-D, memo concedes |
Conclusion: invariant under every modification; the memo's "✓ by identification" is precisely what thm:shape(C) excludes (W-identification).

## 4. MUST clauses
| clause | verdict |
|---|---|
| exact identity on the family | met |
| non-linear in Λ | **not met**: the symbol Re R_X is affine (memo concedes); the test |ζ_w|² is a choice of vector, non-linear in nothing the comb varies with; "coefficients 1 encode Λ∗1 = log" is identification |
| Euler × FE × ℤ jointly as one mechanism | **not met** ("factors in one integrand", memo concedes) |
| ℤ-integrality as mechanism | **not met** (README says YES — rejected): the Mellin polar term/dual modes are properties of the test lattice; the (0,0) vanishing is Tate, not ℤ; everything survives O15 on the comb |
| margin from the identity | **not met** (memo concedes; and the M^{−3} on the family is the profile tail) |
| fluctuation not density | met as structure (Thm 3(i),(iii)): the continuous main term cancels exactly by Tate — B2d made exact on the family; endorsed as a PROVED correction to SPEC_B §4 Line 2 (bulk) |
| 10⁻⁵-sensitive | vacuous (no sign decided) |
| separates ζ from ζ_K | named, **not used** at any load-bearing line ⇒ (R)(10) not met |

## 5. Retry check
Thm 2 overlaps L2_012 §2 (coefficient-1 AFE = Poisson on ℤ) and the standard smoothed Perron formula; Thm 4 = N_BUILD_009 §1 restated on ℤ²; Thm 1/(2.1) = prop:AM + prop:wit-cheb; the sign content = SPEC_B T*₃/C*₃ = index 06_ R9. No dead sub-route of R1/R9 is reused. Not a retry, but the only new PROVED content is Thm 3(i)/(iii) (exact second-order cancellation of the continuous atom sum on the family, with the edge term identified).

## 6. REF-D scepticism
The sign content is (S) on the family = T*₃(η), already REF-D for η ≤ η₀ (SPEC_B). The Mellin/Poisson rewritings are coordinate changes on the test; none is weaker than, or independent of, D. Thm 5(b) correctly notes that any square representation would be class (D) (thm:sos/def:PD, REF-D). Nothing new is D in disguise beyond what SPEC_B already recorded.
