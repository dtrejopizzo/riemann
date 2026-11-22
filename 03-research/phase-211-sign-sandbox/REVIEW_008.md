# Review 008: round 009_B (Fourier-class selection rule, self-dual lower half) against Paper 46 §sec:ext, ROUND_008_E, ROUND_009_A, REVIEW_006/007 and V.1.4

Scope. ROUND_009_B read in full and checked against Paper 46 §sec:ext (def:ext, lem:ext-mob, thm:ext-half, the gauge 𝒢_T,
prop:ext-gauge, prob:ext-L, prop:ext-consol), the definition of P_T (Tate moments A(F) = ∫Fe^{t/2}, B(F) = ∫Fe^{−t/2}),
ROUND_008_E, ROUND_009_A, REVIEW_006/007, and V.1.4 of phase 199. Verdicts: CONFIRMED / REFUTED / DOWNGRADE, with the label
each claim keeps. Numerical tables were not rerun; they keep the label NUMERICAL. No equivalence of (★) with another
statement is used.

## 1. Poisson identity (1.0) and Theorem 1.1

Recomputation. For f even with absolutely convergent dual sum, Poisson over ℤ at spacing u = e^x reads
f(0) + 2Σ_{n≥1}f(nu) = u^{−1}(ℱf(0) + 2Σ_{k≥1}ℱf(k/u)), so
Σ_{n≥1}f(nu) = u^{−1}Σ_{k≥1}ℱf(k/u) + ℱf(0)/(2u) − f(0)/2. Multiplying by u^{1/2} = e^{x/2} and noting
(Eℱf)(−x) = e^{−x/2}Σ_{k≥1}ℱf(ke^{−x}) gives exactly (1.0), with boundary term τ = ½ℱf(0)e^{−x/2} − ½f(0)e^{x/2}. The
normalisation ℱf(ξ) = ∫f e^{−2πixξ} is the one fixed in §sec:ext (unitary, ℱ² = R, so ℱ has eigenvalues ±1 on even
functions and ε ∈ {±1} is the right label set). CONFIRMED.

R-invariance and exact removal. P_T = {A(F) = B(F) = 0} is by definition the orthogonal complement of 𝒯 = span{e^{x/2},
e^{−x/2}} in L²(I_T); R swaps the two generators, so 𝒯 and P_T are R-invariant, Π_T commutes with R and Π_Tτ = 0. With
ℱf = εf + h, linearity of E gives Ef = εREf + REh + τ; applying Π_T and P_{−ε} = (I − εR)/2 gives
P_{−ε}Π_TEf = ½(Π_TEf − εRΠ_TEf) = ½RΠ_TEh. Each step checked. CONFIRMED, PROVED.

Hypotheses (DOWNGRADE of the stated regularity, not of the theorem). The memo says "C¹ on ℝ, supp f ⊂ [−λ, λ], so ℱf =
O(ξ^{−2})". C¹ with compact support gives only ℱf = o(1/ξ) and ξℱf ∈ L²; that is enough for absolute convergence of
Σ_kℱf(k/u) (Cauchy–Schwarz against k^{−1}) and for pointwise Poisson, so the theorem holds as stated, but the parenthetical
O(ξ^{−2}) is false at that regularity (it holds for admissible f of def:ext, which are C² on [−λ, λ] with f(λ) = 0). More
important: the raw prolates ψ_k restricted to [−λ, λ] have a jump at ±λ (ψ_k(λ) ≠ 0), ℱψ_k ≍ 1/ξ, the dual sum is only
conditionally convergent, and Theorem 1.1 is not proved for them. Every numerical object of §§1.4–3 (g_k = Π_TEψ_k,
h_k = P_+Π_TEψ_k) is built from raw prolates, so the identity is used there outside its proved scope. An extension to data with an edge jump (symmetric Poisson with conditionally convergent dual sums, then an L²(I_T) limit) is plausible but is not written, and Lemma 1.3 cannot supply the limit since ∫u^{2s}|h|² = ∞ for |h| ≍ 1/u and every s > ½: ARGUED for raw prolates.

V.1.4 comparison. V.1.4 records Φ_{ℱf} = Φ_f∘R for admissible f (f(0) = ℱf(0) = 0, no boundary term). Theorem 1.1 is the
same Poisson identity, valid without the two vanishing conditions because Π_T kills τ; the "up to the tail r*" of V.1.4
is not literally removed (the remainder RΠ_TEh is the image of the Fourier defect, which includes the out-of-band part),
but it is now an identity with an explicit remainder. The novelty claim is CONFIRMED in that form.

## 2. Theorem 1.2 (diagonal Fourier defect)

Convention check. With x = λs, ξ = λt, ℱψ(λt) = λ∫_{−1}^{1}ψ(λs)e^{−2πiλ²st}ds, so the finite Fourier operator has
c = 2πλ² = 2πN and time and band intervals coincide; this is the c of ROUND_008_E and ROUND_009_A. The Slepian eigenvalue
of the kernel e^{+icst} is i^k|α_k|; the kernel here is e^{−icst}, whose eigenvalue is the conjugate (−i)^k|α_k|. For even
k, i^k = (−i)^k = (−1)^{k/2}, so the phase is convention-independent on the even sector, which is the only sector used
(def:ext data are even). Sanity check at k = 0: ψ_0 > 0, so ℱψ_0(0) = ∫ψ_0 > 0 and the eigenvalue is +√χ_0, class +1.
The modulus: ‖ℱψ_k1_band‖² = χ_k by definition of concentration in the unitary normalisation, and ℱψ_k1_band is a
multiple of ψ_k (finite-Fourier eigenfunction), hence equals ε_k√χ_kψ_k. CONFIRMED (CITED inputs used correctly).

Formula. ‖ℱf − εf‖² = ‖ℱf‖² + ‖f‖² − 2εRe⟨ℱf, f⟩ = 2Σa_k² − 2εΣε_k√χ_ka_k² (the pairing sees only the band part of ℱψ_j
because ψ_k vanishes off the band; ⟨ℱψ_j, ψ_k⟩ is real for even j). Eigenvalue 2(1 − εε_k√χ_k); on the own class
2(1 − √χ_k) = 2d_k/(1 + √χ_k) ∈ [d_k, 2d_k]; on the other class 2(1 + √χ_k) ∈ [2, 4]. Band part Σ(ε_k√χ_k − ε)²a_k²,
off-band part Σd_ka_k² by double orthogonality (⟨ℱψ_j1_off, ℱψ_k1_off⟩ = δ_{jk} − δ_{jk}χ_k). All CONFIRMED, PROVED,
for finite real combinations of raw prolates. Note: this is exact only for raw prolate spans; the mollified data of
ROUND_009_A that Corollary 1.4 and Lemma 1.6 need are not in those spans, so Theorem 1.2 transfers to them only up to the
mollification error (bounded in ROUND_009_A, not recomputed here).

## 3. Lemma 1.3 and Corollary 1.4

Lemma 1.3. v = e^x turns ‖Eh‖² into ∫_{1/λ}^{λ}|Σ_nh(nv)|²dv; weighted Cauchy–Schwarz with n^{∓s} gives the factor ζ(2s);
∫_{1/λ}^{λ}|h(nv)|²dv = n^{−1}∫_{n/λ}^{nλ}|h|²; interchanging, the n with n/λ ≤ u contribute Σ_{n≤uλ}n^{2s−1} ≤ (uλ)^{2s}
because 2s − 1 ∈ (0, 1]. Constant ζ(2s)λ^{2s} exact as stated. "h even" is unused. CONFIRMED, PROVED.

Corollary 1.4. ‖P_{−ε}Π_TEf‖ = ½‖RΠ_TEh‖ ≤ ½‖Eh‖; Lemma 1.3 with s = 1; split ∫_{1/λ}^{∞}u²|h|² at u = λ, using u ≤ λ on
the band and h = ℱf off the band (f vanishes there). The displayed bound follows (half-line norms ≤ full-line norms).
CONFIRMED, PROVED for C¹ data. The step "band term ≤ (Σd_k²a_k²)^{1/2}" uses 1 − √χ ≤ 1 − χ: correct. The application
to mollified prolate spans ("O(poly(N)√max d_k)") is CONDITIONAL on the weighted out-of-band bound of ROUND_009_A
(REVIEW_007 confirmed that memo's unweighted and first-moment bounds; the ξ-weighted L² norm needed here is the quantity
‖ξℱf1_off‖, which ROUND_009_A controls through ∫φ′² — acceptable, but the composite constant is not written) and on the
transfer remark at the end of §2. DOWNGRADE of the "in particular" clause to CONDITIONAL; the corollary proper stands.
The NUMERICAL ratios ρ_k ∈ [0.46, 0.90] refer to raw prolates, i.e. to a regime where neither Theorem 1.1 nor the
corollary is proved (§1 above); they are consistent with the identity but do not test it.

## 4. Theorem 1.5 and Lemma 1.6 (cross terms)

Identities. P_−Ef_+ = w_+ is Theorem 1.1 at ε = +1 (Π_TEf_+ = Ef_+ because A(Ef_+) = B(Ef_+) = 0); P_+Π_TEf_− = w_− is
Theorem 1.1 at ε = −1 with h_− = ℱf_− + f_−. Sign conventions h_± = ℱf_± ∓ f_± match. The bilinear half-line identity
W_T(Ef_+, G) = −𝒲(Ψ_{f_+}, G) for G ∈ P_T in the form domain follows from the radical relation in the proof of
thm:ext-half (𝒲(Φ_{f_+}, G) = 0, Φ = Ef + Ψ) and W_T = a_T on P_T. Hypothesis check: f_+ must be admissible in the sense of
def:ext (C² on [−λ, λ], f(0) = ℱf(0) = f(λ) = 0); a finite class-(+1) prolate combination can meet the three linear
conditions, so the hypothesis is not vacuous, but the class-(+1) span itself is not admissible and §2 works with raw
prolates. The displayed identities are CONFIRMED.

Correction (DOWNGRADE of the reading, not of the identity). w_+ = P_−Ef_+ is odd and w_− = P_+Π_TEf_− is even. a_T commutes
with R on P_T (P211-3A, PROVED; directly: W_T is invariant under t ↦ −t, which swaps A and B), so a_T(w_+, w_−) = 0
identically. Hence the cross term is exactly
    a_T(P_+Ef_+, P_+Π_TEf_−) = −𝒲(Ψ_{f_+}, w_−),
a single (exterior tail of f_+) × (Fourier defect of f_−) product. The advertised second product "defect(f_+) ×
defect(f_−)" is the zero term; the bound poly(N)[(L₁ + L₂)δ¹(f_−) + δ¹(f_+)δ¹(f_−)] is correct but its second summand is
spurious. Likewise, by parity, a_T(Ef_+, w_+) = a_T(P_−Ef_+, w_+) = a_T(w_+), so the diagonal block simplifies to
    a_T(P_+Ef_+) = 𝒲[Ψ_{f_+}] − a_T(w_+),
which the memo's two expressions do equal (checked: −2a_T(w_+) + a_T(w_+), and 2𝒲(Ψ, w_+) = −2a_T(w_+)). The simplified
form exposes what the memo's form hides: the correction to the exterior value has a definite structure, minus the
odd-sector form of the wrong-parity remnant, and with the NUMERICAL quotient a_T(w_+)/‖w_+‖² ≈ 1.7–2.5 it is a negative
correction of size ≍ ‖w_+‖² ≍ defect of f_+. The memo's sign-neutral phrase "O(defect products)" is not wrong in size but
should be replaced by this identity. Theorem 1.5: CONFIRMED with this simplification.

Lemma 1.6(a). The pole terms of the bilinear 𝒲 are A(Ψ)B(w) + A(w)B(Ψ) = 0 since A(w) = B(w) = 0; ⟨Ψ, w⟩ = 0 (disjoint
supports). Archimedean: with K(u) ≤ 1/u + ½ on (0, 1] and |c^{sym}(u)| ≤ ½u‖Ψ‖_∞‖w‖_∞ the near part is ≤ ½(1 + ¼)·
‖Ψ‖_∞‖w‖_∞ = (5/8)‖Ψ‖_∞‖w‖_∞, inside the stated ¾; the far part ½·Ktail(1) < 0.7. Comb: the shift by log n moves the
window to [−T − log n, T − log n]; for n > N its intersection with (−∞, −T] lies in (−∞, −T − (log n − 2T)], mass
≤ Me^{−(log n − 2T)} = MN/n; the opposite shift does not meet (−∞, −T]. Σ_{n≤N}v_n ≍ 4√N and NΣ_{n>N}v_n/n ≍ 4√N by
partial summation (Chebyshev bounds suffice, absolute C). CONFIRMED, PROVED, given the Lévy-kernel bounds K(u) ≤ 1/u + ½,
Ktail(1) < 1.4, which are cited from the paper's archimedean lemma and not rechecked here.

Lemma 1.6(b). The written statement contains an unfinished expression ("… + ∫_0^{2T}|c_u(0) − c^{sym}_{u,w}(u′)|…") and
the "clean statement" |a_T(u, w)| ≤ β_T‖u‖_{H¹}‖w‖_{H¹} is asserted with a one-line justification. The H¹ bound is
standard in shape, but the constant C(1 + T + √N) and the claim that Arch is dominated by "H^{1/2+} with log weight" are not
proved in the memo. DOWNGRADE to ARGUED. Since the parity correction above removes the only use of (b) in the cross term
(a_T(w_+, w_−) = 0), the cross-term bound of Theorem 1.5 does not need (b); (b) is still used for the diagonal correction
a_T(w_+), where a trivial bound a_T(w_+) ≤ ‖a_T‖_{form}‖w_+‖²_{H¹} of the same shape is needed.

The composite bound "of order poly(N)√(d_jd_k)" on mollified spans is CONDITIONAL on ROUND_009_A (weighted leakage) and on
the transfer of Theorem 1.2 to mollified data (§2 note). Label CONDITIONAL, not PROVED.

## 5. §1.7 (which class is near-null)

The qualitative reading is correct and consistent with V.1.4 and ROUND_008_E §2.2: in the even sector class +1 enters
with full norm, class −1 only through w_−; in the odd sector the roles swap and the odd class is {2, 6, 10} (k ≡ 2 mod 4),
matching the index 10 of ROUND_008_E. But the two load-bearing statements are not proved: "class −1 is not near-null
relative to its own norm" rests on the NUMERICAL quotient a_T(w_−)/‖w_−‖² ≈ 1.7–2.5 (raw prolates, outside the proved
scope of Theorem 1.1), and "class +1 is near-null" rests on 𝒲[Ψ_{f_+}] being small (ROUND_008_E Thm 3.1, upper bound,
CONDITIONAL there on Lemma 3.4, now ROUND_009_A) together with the diagonal identity of §4, whose correction −a_T(w_+) is
of the same order as the quantity being described. The statement "the sharp index is 8 because two constraints absorb
ψ_0, ψ_4 inside class +1" is the index count of ROUND_008_E Prop 3.3 restricted to a class; plausible, not proved here
for λ_A. DOWNGRADE from "PROVED reading" to ARGUED.

## 6. Lemma 2.1 (exact elimination)

With s*(r) the M-minimiser over S, the cross term ⟨r + s*(r), s − s*(r)⟩_M vanishes, so
M(r + s) = M̃(r) + M_SS[s − s*(r)] (Schur identity, requires M_SS > 0, true numerically by α_S ≥ 10¹³). Then
M̃(r) ≥ κ̃D(r + s*(r)) and M_SS[s − s*] ≥ α_SD(s − s*), and D(x) ≤ 2D(r + s*) + 2D(s − s*) (parallelogram). Conclusion
M ≥ ½min(κ̃, α_S)D. The phrase "with M_SS-orthogonality as above" is redundant (it is the definition of s*). CONFIRMED,
PROVED. The observation that D̂(e_k) = d_k "to all printed digits" for k ≥ 12 is NUMERICAL. Remark: the two stiff
directions are identified with "symmetric admissibility f(0) + ℱf(0) = 0 and the even Tate condition" by inspection of
their size only; that identification is ARGUED.

## 7. Proposition 2.2 and bound (2.1)

Proposition 2.2. In D̂-normalised coordinates, for a vector (t, y), t²α_b + 2t⟨x, y⟩ + ⟨Qy, y⟩ ≥ α_bt² − 2|t|Γ|y| +
α_H|y|², the quadratic form of [[α_b, Γ], [Γ, α_H]] at (|t|, |y|); its least eigenvalue is the smaller root κ, positive
iff Γ² < α_bα_H when α_b, α_H > 0. Block version identical with α_b → κ_LM. (For one-dimensional b the "P ≥ 0" is 0.)
CONFIRMED, PROVED, elementary.

Bound (2.1). The algebra is right: d_k increasing in k gives D ≥ d_8|a_{≥8}|² on class-(+1) indices; two linear
constraints solved for (a_0, a_4) give |a|² ≤ (1 + κ_C²)|a_{≥8}|²; ‖F‖² ≤ ‖Gram‖|a|². Three objections.
(i) The constant κ is not a structural quantity: it is the Schur root for a truncation k ≤ K, computed NUMERICALLY, and the
memo's own §2.4(ii)–(iii) shows it decreases with K (α_HI → 0.12–0.28) and argues inf M/D → 0 as K → ∞ with fixed
representatives. So (2.1) holds on each finite span with a K-dependent constant that is expected to degenerate; it is not
a bound with "three finite-dimensional constants" uniform in K, and κ_C, ‖Gram‖ are not measured at all.
(ii) "This is the shape λ_A ≥ κ(1 − χ_8)N^{−b} on that subspace" overstates: the subspace is the class-(+1) even image of
k ≤ K only, excluding class −1 remnants, the odd sector and the high range, and the constraint step requires the class-(+1)
data to satisfy the two constraints exactly, which is not the same as membership of F in P_T ∩ (even sector).
(iii) The "index improvement 6 → 8" compares a proved floor (ROUND_008_E Lemma 4.3, all even data) with a floor on a
smaller class-restricted subspace; it is not an improvement of the same statement.
Verdict: Proposition 2.2 CONFIRMED (PROVED); (2.1) DOWNGRADE from "PROVED as an implication" to CONDITIONAL on finite-K
constants (κ(K), κ_C, ‖Gram‖), with κ(K) NUMERICAL and expected to tend to 0; the "λ_A-shape" sentence is withdrawn.

§2.3, §2.5 tables: NUMERICAL, not rerun; the reading "M ≈ (1–2)·D on k ≤ 4N" is NUMERICAL. §2.4(iii) (gauge vectors in the
high prolate span force α_HI → 0): ARGUED, and it agrees with the remark after prob:ext-L that the inequality is false
without the gauge infimum (there for leak(f); here the analogous statement for D on fixed representatives). CONFIRMED as
ARGUED. (HR) is correctly stated as OPEN; (HR)(a) is prob:ext-L restricted to HI, so the reduction does not shrink the
open problem in kind, only localises it to the range 1 − χ_k ≈ 1. The memo says so. CONFIRMED.

## 8. Falsifier analysis (§3)

§3.1 (Λ-free). Theorems 1.1, 1.2, Lemma 1.3, Corollary 1.4 contain no weight: CONFIRMED. The weighted decoupling identity
a^w_T(P_+Ef_+, w_−) = −𝒲(Ψ_{f_+}, w_−) + 𝒫_{Λ−w}(·, w_−) (the a_T(w_+, w_−) term is zero by parity for every weight that
keeps the form R-invariant, which all listed comb weights do) keeps the small factor w_−: CONFIRMED. The conclusion "the
class–parity rule is not a sign step" is the correct use of the falsifier test. CONFIRMED.

§3.2(a),(b),(d). The identity a^w_T(Ef_+) = 𝒲[Ψ_{f_+}] + 𝒫_{Λ−w}[Ef_+] is ROUND_008_E (5.1), confirmed in REVIEW_006.
The table is NUMERICAL. The reading "near-nullity of class +1 is the Λ-specific part" is CONFIRMED as ARGUED: it is a
statement about where the falsifiers break the numerics, not a proof that the Λ-specific part carries a sign.

§3.2(c), a_P-adapted map. Recomputed: Σ_{(n,Q)=1}f(nu) = Σ_{d|Q}μ(d)Σ_{m≥1}f(dmu); Poisson for each d gives
(du)^{−1}Σ_{k≥1}ℱf(k/(du)) + ℱf(0)/(2du) − f(0)/2; the f(0) terms cancel (Σ_{d|Q}μ(d) = 0, Q > 1), the ℱf(0) term is
(φ(Q)/Q)ℱf(0)/(2u). The dual frequencies are j/(Qu), j ≥ 1, with weights c_j = Σ_{d|Q, (Q/d)|j}μ(d)/d (prefactor u^{−1}) depending on j,
whereas the adapted map applied to ℱf at −x evaluates ℱf at n/u with (n, Q) = 1 and weight 1. The two linear functionals
differ (different evaluation sets for generic ℱf), so the exact intertwining E_Qℱ = RE_Q + boundary fails. CONFIRMED,
PROVED. The stronger clause "no parity-class rule holds" is not proved: the failure of the exact identity does not exclude
an approximate rule with a different remainder. DOWNGRADE of that clause to ARGUED. Beurling: no Poisson formula, (1.0) has
no analogue; ARGUED, as stated. Overall falsifier verdict of §3: CONFIRMED in substance (Λ-free rule; Λ-specific
ingredient isolated in the class-(+1) block value), with the one wording downgrade.

## 9. Verdict table

| Claim | Verdict | Label after review |
|---|---|---|
| (1.0) Poisson in window coordinates | CONFIRMED | PROVED (C¹ data; "O(ξ^{−2})" holds only for C², kink-at-edge data) |
| Theorem 1.1 | CONFIRMED | PROVED for C¹ compactly supported even f; ARGUED for raw prolates (edge jump) |
| Theorem 1.2 | CONFIRMED | PROVED (CITED Slepian–Pollak, double orthogonality); phase i^k unambiguous on even k |
| Lemma 1.3 | CONFIRMED | PROVED |
| Corollary 1.4 | CONFIRMED / DOWNGRADE | bound PROVED; "O(poly(N)√max d_k) on mollified spans" CONDITIONAL on ROUND_009_A + transfer of Thm 1.2 |
| Theorem 1.5 | CONFIRMED with correction | PROVED; a_T(w_+, w_−) ≡ 0 by parity; cross term = −𝒲(Ψ_{f_+}, w_−); diagonal = 𝒲[Ψ_{f_+}] − a_T(w_+) |
| Lemma 1.6(a) | CONFIRMED | PROVED given the Lévy-kernel bounds |
| Lemma 1.6(b) | DOWNGRADE | ARGUED (statement unfinished, constant unproved) |
| defect-product bound poly(N)√(d_jd_k) | DOWNGRADE | CONDITIONAL |
| §1.7 near-null class | DOWNGRADE | ARGUED (rests on NUMERICAL quotients) |
| Lemma 2.1 | CONFIRMED | PROVED |
| Proposition 2.2 | CONFIRMED | PROVED |
| bound (2.1) | DOWNGRADE | CONDITIONAL on K-dependent constants κ(K) (NUMERICAL, expected → 0), κ_C, ‖Gram‖ (unmeasured); "λ_A-shape" withdrawn |
| §2.4(iii) gauge forcing | CONFIRMED | ARGUED |
| (HR) | CONFIRMED | OPEN (prob:ext-L localised to k > 4N) |
| §3.1 Λ-free rule, not a sign step | CONFIRMED | PROVED / NO-GO for sign from Poisson–ℱ-class symmetry |
| §3.2(c) a_P-adapted map | CONFIRMED / DOWNGRADE | exact intertwining fails PROVED; "no rule holds" ARGUED |
| Beurling | CONFIRMED | ARGUED |

Nothing REFUTED. No sign statement is made by the round and none is credited. Row D status unchanged: OPEN.
