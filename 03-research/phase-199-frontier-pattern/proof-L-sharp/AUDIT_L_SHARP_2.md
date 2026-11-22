# AUDIT_L_SHARP_2 — audit of the proof attempts F, H, J of Lemma L′♯ (against AUDIT_L_SHARP_1 (★★))

Pen and paper, plus the numerical checks that were strictly necessary to decide labels
(§5: the constants of J Thm J.3 and the on-line symbol identity of F Thm F.1, mpmath 30 digits, NUMÉRICO).

Sources checked against the memos: AUDIT_L_SHARP_1 §1–§6 ((★★), constraints 1–7); memos A (Thm 1.1, Prop 2.1, §3.2,
Rem 3.3, Lemma 4.2), C (Prop 1.2, Prop 4.2), E (E.1, E.1′, E.2, Cor E.3, Lemma E.4, E.5, §7); Paper 46 (eq:symbol,
eq:form, eq:W, lem:K, def:W, lem:monoT, prop:archneg, sec:cert, and the two places where Zhu Thm 1.2 is cited for the
complete form at T ≤ 0.8, lines 143 and 1109); Mori L104 (index 05b l.56; AUDIT_ZENODO_FRONTIER B1:
computational part reproduced, label CITED); CERT_FALSIFIERS_001; Titchmarsh §3.5 (Euler–Maclaurin for ζ_X).

**Verdict in one line.** None of F, H, J proves L′♯, and all three say so. F: Prop F.0 and Thm F.1 are PROVED; Thm F.2
is PROVED as an identity but the "pointwise null vector" is a null vector of the *line form Q only* (the pole term 2AB is
not split and contains an F₀–F₀ piece), so Cor 3.2's block argument does not apply to 𝔔 verbatim; Thm F.3's displayed
kernel identity is DIVERGENT as written (same defect J finds in E.1′); Prop F.4(b) ("the O(1) remainder is the sawtooth
in the transition region") is FALSE — J Thm J.3 shows the sawtooth F₂ is superpolynomially small on smooth deep data and
the O(1)·e^D constant is a bulk quantity; Prop F.5 is a correct reduction with one factor-2 wording slip. J: Prop J.1,
Thm J.2 (literal statement), Rem 2.1 (correction to E.1′) and Thm J.3 are PROVED (J.3 given PNT, all constants verified);
Cor J.4(c) is overstated in its O(1) term; the class NO-GO of Thm J.2 is ARGUED, not PROVED (the object that *does* exist
is a Toeplitz-in-log matrix with a bounded positive-definite symbol peaked at scale 1/μ). H: the dilated frame, Lemma H.2,
Thm H.4, Lemma H.5, (H-ODE) and Thm H.5(i) are PROVED (H.5 modulo the compactness/HF assumptions 4.1, CONDITIONAL); Prop
H.1 is PROVED given Mori Theorem O (CITED, reproduced); Cor H.4′ has a sign error (the jump is −4c_qG_φ(−log q)φ′(1));
(H) ⇒ L′♯ is correct and (H) is a restatement-strength condition, so the class NO-GO 𝒦_H stands as ARGUED. The three
"mechanisms" (F: F₀–G coupling; J: Chebyshev remainder at the deep mode; E/AUDIT_1: cross-class interference) are not
mechanisms and not the same thing: they are three bookkeepings of one number, which on deep smooth data is
2(ξ′/ξ)(1)·B_φ²e^D, the Weil distribution at the pole — a global constant, not localised anywhere, and outside the
Paley–Wiener regime where (★★) lives. Nothing here is a sign. Row D OPEN.

## 1. F Prop F.0 — the universal form (PROVED, two caveats)

**1.1 Rescaling checked.** With ρ(X) = λr(λX): ‖ρ‖²_{L²(1,∞)} = λ²∫_1^∞r(λX)²dX = λ‖r‖²_{L²(λ,∞)} ✓.
Ψ̌(a+y) = e^{(a+y)/2}Σ_n r(nλe^y) = λ^{1/2}e^{y/2}·λ^{−1}Σ_nρ(ne^y) = λ^{−1/2}Ψ̌_ρ(y) ✓, and 𝒲 (archimedean form of the
zero-extended function, killing term included, comb, pole) is translation invariant on the full line, so 𝒲[Ψ̌] =
λ^{−1}𝒲[Ψ̌_ρ] ✓. g(t) = f(t/λ): supp g ⊂ [−λ²,λ²] = [−μ,μ], g(μ) = f(λ) = 0, ĝ(ξ) = λf̂(λξ) (convention e^{−2πixξ}), so the
band |ξ| < λ of f̂ is |X| < 1 for ĝ and ρ = ĝ|_{(1,∞)} ✓. Gauge: φ with supp ⊂ [−1/λ,1/λ], φ(0) = φ̂(0) = 0 ↦ χ(t) =
φ(t/λ) with supp ⊂ [−1,1], χ(0) = 0, χ̂(0) = λφ̂(0) = 0, and (1−P_λ)φ̂ ↦ (1−P_1)χ̂ up to the same λ-isometry ✓. Hence
dist²(r,𝒢̄) = λ^{−1}dist²(ρ,𝒢̄₁) and 𝒢̄₁ is μ-independent ✓. Both sides of (★★) scale by λ^{−1}: (★★) ⟺ (★★_u) with the
same (κ,A). **PROVED.** Consistent with H's dual rescaling (φ(x) = λ^{1/2}f(λx), band edge μ = c/2π; §4 below).

**1.2 Caveats.** (i) "𝒢̄₁ ⊂ ker 𝔔": the *generators* (1−P_1)χ̂ are radical vectors (memo A Prop 2.1(a)); 𝔔 is not
L²(1,∞)-continuous (Z is not L²-bounded, C Prop 4.2), so the closure is in ker 𝔔 only in the sense of the distance
functional — fine for (★★_u), but 𝔔 is a form on a domain (ρ Lipschitz on (1,∞), ρ = O(X^{−2})), not on L²(1,∞).
(ii) "PW_1 is the radical": Prop 2.1 gives gauge ⊂ radical, not equality; harmless. (iii) "PW_μ dense in L²(1,∞) as
μ → ∞": ARGUED (Hardy-space density, same status as J §4.1). **Label: PROVED; the reading paragraph ARGUED.**

## 2. F Thm F.1 — the critical-line formulation (PROVED; Rem 2.1 overstated)

**2.1 Derivation and convergence.** ∫_0^∞Ψ̌_ρ(y)e^{−(s−½)y}dy = Σ_n∫_0^∞ρ(ne^y)e^{(1−s)y}dy; X = ne^y gives
Σ_n n^{s−1}∫_n^∞ρ(X)X^{−s}dX = ∫_1^∞ρ(X)X^{−s}ζ_X(1−s)dX ✓; the exchange is absolute (Σ_n n^{−1/2}∫_n^∞|ρ|X^{−1/2} ≤
Σ_n n^{−1/2}·O(n^{−3/2}) for ρ = O(X^{−2})) ✓. The log version with −ζ_X′(1−s) = Σ_{n≤X}n^{s−1}log n ✓. A = F(1) =
∫ρ⌊X⌋/X, B = F(0) = ∫ρH(X) ✓ (A, B are Mellin values off the line; convergent since Ψ̌ = O(e^{−3y/2})). (F.1) is Cor E.3
in Plancherel form ✓ (F, F_log ∈ L²; Ψ̌_ρ Lipschitz with one jump ⇒ |F|² = O(τ^{−2}), log-integrable, so the Θ_∞-weighted
integral converges).
**2.2 Symbol identity.** From ξ(s) = ξ(1−s): (ζ′/ζ)(s) + ½ψ(s/2) − ½log π + 1/s + 1/(s−1) = −[same at 1−s]; on the line
1−s = s̄ and Re(1/s) + Re(1/(s−1)) = ½/(¼+τ²) − ½/(¼+τ²) = 0 ✓, so Θ_∞(τ) = −2Re(ζ′/ζ)(½+iτ). NUMÉRICO (§5): equality to
30 digits at τ = 5, 10, 14, 30. Re(ζ′/ζ) extends continuously across simple on-line zeros (1/(s−ρ) is purely imaginary
there) ✓. **PROVED** (it is memo A Rem 3.3 with the pole terms written out; F says so).
**2.3 Rem 2.1 "Im ζ′/ζ never enters; no zero data".** TRUE for (F.1) as displayed. NOT true for the split of Thm F.2:
the cross term 2Q(F₀,G) = −(1/π)∫Re[R̄(χζ′(1−s)G + ζ(s)G^{log})] contains χ(s)ζ′(1−s) = ζ(s)(ζ′/ζ)(1−s), the *full*
logarithmic derivative, and F₀ = ζ(1−s)R(s) vanishes at every on-line zero. The zeros are not used through bounds, but
they sit in F₀ (this is C Prop 1.2's zero sum reappearing: the exterior form is Σ_ρΦ_ℓ(ρ)Φ_ℓ(1−ρ)). **Rem 2.1: ARGUED,
overstated.**

## 3. F Thm F.2, Cor 3.2, Thm F.3, Prop F.4, Prop F.5

**3.1 Lemma 3.1 (Euler–Maclaurin), re-derived.** Σ_{n≤X}n^{−w} = ∫_{1^−}^X t^{−w}d⌊t⌋ = ⌊X⌋X^{−w} + w∫_1^X⌊t⌋t^{−w−1}dt;
with ⌊t⌋ = t − {t} and ζ(w) = w/(w−1) − w∫_1^∞{t}t^{−w−1}dt (Re w > 0) this gives ζ_X(w) = ζ(w) + X^{1−w}/(1−w) −
{X}X^{−w} + w∫_X^∞{t}t^{−w−1}dt ✓, |e_w(X)| ≤ (1+|w|/Re w)X^{−Re w} ✓, and e_w(X) = ∫_X^∞t^{−w}d{t} = −Σ_{k≠0}∫_X^∞
e^{2πikt}t^{−w}dt (Poisson, conditionally convergent) ✓. Note: replacing {t} by ½ + ({t}−½) the two ½-terms cancel
(−½X^{s−1} + ½X^{s−1}), so e_s is *purely oscillatory*: against smooth ρ it is superpolynomially small (used in §3.5).
**CITED/PROVED.**
**3.2 Thm F.2 (i)–(iv).** (i) ✓ (F₀ ∈ L² by |ζ(½−iτ)|² = O(τ^{1/2+ε}) and |R|² = O(τ^{−2}); the pieces are in the
Θ_∞-weighted L², so polarisation of Q is legitimate). (ii) Θ_∞|F₀|² − 2Re(F̄₀F₀^{log}) = |R|²|ζ(1−s)|²[Θ_∞ +
2Re(ζ′/ζ)(1−s)] = 0 pointwise ✓ (and = 0 at on-line zeros, both terms vanish). (iii) ✓. (iv) algebra re-done: Θ_∞F̄₀ −
\overline{F₀^{log}} = R̄ζ(s)[Θ_∞ + (ζ′/ζ)(s)] = −R̄ζ(s)\overline{(ζ′/ζ)(s)} = −R̄χ(s)ζ′(1−s) ✓, Q(G,G) display ✓.
**PROVED as identities.** Identification of the pieces (my computation, needed for §3.5): on the line F₀ + F₁ =
F[Ψ_full − ρ₀e^{−y/2}1_{y<0}] (two-sided Laplace transform of Ψ_full = Σ_n n^{−1/2}S_{−log n}ρ̃ is ζ(1−s)R(s) on Re s < 0,
memo A §3.2; subtracting the growth ρ₀e^{−y/2} at −∞ adds +ρ₀/s), hence F₀ = F[Ψ_full − ρ₀e^{−y/2}] (the untruncated
dilate sum minus the quasi-mode on the whole line) and F₂ = F[−(Ψ_full − ρ₀e^{−y/2})·1_{y<0}] (the Poisson/sawtooth
remainder *below* the window). So "F₀ is a null vector" is exactly memo A §3.2/Rem 3.3: the untruncated object has
vanishing symbol; the truncation at y = 0 is the whole form. Not new as content; new as a display.
**3.3 "Pointwise null vector" and the pole term.** Q is the *line* part (Θ_∞|F|² − 2Re F̄F_log) only; the pole term 2AB
is **not** split and is kept as 2A(ρ)B(ρ). A = F(1), B = F(0) are Mellin values at s = 1, 0, where F₀ contributes
F₀(1) = ζ(0)R(1) = −½∫ρ/X and (F₀+F₁)(0) = ρ₁ + γρ₀ = −R′(0) + γR(0). So 2AB contains the term 2ζ(0)R(1)(γR(0) − R′(0)),
a pure (F₀,F₀)-piece. **Hence F₀ is a null vector of Q, not of 𝔔**, and the premise of Cor 3.2 ("no (u,u)-term") fails
for 𝔔 once 2AB is included. Moreover Cor 3.2's abstract lemma needs a *product set* U × V; here F₀ and G are both
functions of one ρ (F says so), so the conclusion "the entire sign is in the coupling" is the tautology that the split
is not a direct sum. The sharpening of constraint 5 is therefore a restatement, not a theorem. **Thm F.2(ii): PROVED
(for Q). Cor 3.2: abstract lemma PROVED; application to 𝔔 ARGUED (premise false for the pole term; product-set premise
false by construction).** Also: the 2×2 block picture is for the pair (F₀,G) with G = F₁ + F₂; restricted to PW data
the map ρ ↦ (F₀,G) is injective-but-not-onto, so a "2×2 block ≥ 0" test is neither necessary nor sufficient for (★★_u).
**3.4 Thm F.3 (Hilbert-type kernel).** Pointwise kernel re-derived: for nξ > mη, ν(y−y′) = (mη/nξ)^{1/2}(nξ)²/
((nξ)²−(mη)²), Φ_m(y)dy = m^{−1/2}ξ^{−1/2}ρ(ξ)dξ, product = nξ/((nξ)²−(mη)²)·ρρdξdη ✓; (jα,jβ) ↦ j^{−1}max(βξ,αη)/
|β²ξ²−α²η²| with H(min(ξ/α,η/β)) ✓; prime part on the rational lines with G_{αβ} ✓. **But the display "regular part
of the Lévy energy = −∫∫ρ(ξ)ρ(η)𝒦(ξ,η)dξdη" is DIVERGENT as written:** 𝒦 ~ 1/|nξ−mη| is not integrable across any
rational line on which ρ(ξ)ρ(η) ≠ 0 (logarithmic divergence), and the sum over (m,n) adds every line. This is the same
defect J Rem 2.1 finds in E Thm E.1′ (literal reading of −ν class by class diverges). F acknowledges it in words ("the
Lévy regularisation … makes … finite") but the identity as displayed is not an identity; the finite object is the
polarised Lévy form Σ_{m,n}(mn)^{−1/2}𝓛(S_{−log m}r_m, S_{−log n}r_n) (J Prop J.1(e)/Thm J.2(b)), in which the kernel
1/|nξ−mη| never appears alone. **Label: kernel computation PROVED; the display and the "reading" paragraph RETRACTED as
identities (ARGUED as a description of where the singular set is); §4.2 bookkeeping PROVED in polarised reading;
§4.3 ARGUED as labelled.** Consequence for AUDIT_1 §1.1: E Thm E.1′ is PROVED only in the polarised reading (its proof
uses it; its statement sentence "to be read literally for the regular part −ν" is wrong). AUDIT_1 §5 (E.5) is unaffected
(diagonal class written polarised).
**3.5 Prop F.4 (deep data).** (i)–(iii) PROVED and consistent with J Thm J.3 (ρ₀ = e^{D/2}B(φ), Ψ̌ = ρ₀e^{−y/2} + tiny on
(0,D−C), 2AB and the prime part each 2Dρ₀² + O(ρ₀²), 𝒜 = O(ρ₀²)); J sharpens the O(ρ₀²) to (2+γ−log 4π)ρ₀² + o(ρ₀²).
**Consequence (a)** ("(1,1) carries the pole that cancels its own growth" is false class-wise) PROVED (= E.5 + J.4(d)).
**Consequence (b) is FALSE:** "the O(1) remainder is the transition region = the sawtooth F₂ evaluated where few dilates
contribute". By §3.1 and §3.2, on smooth deep data F₂ = F[−(Ψ_full − ρ₀e^{−y/2})1_{y<0}] is the Poisson remainder with
L = e^{D−y} ≥ e^D, superpolynomially small (J Thm J.3's bound |Ψ_1| ≤ C_Ne^{−(N−½)(c−x)} is the same estimate); and J
Thm J.3(iii) shows the whole transition region (Ψ_1 on (c−C, c+1)) contributes O(e^{D/2}) + O(1) = o(e^D). The O(1)·e^D
constant 0.046·B_φ²e^D is a *bulk* quantity: b_∞‖Ψ_0‖², the Lévy energy of the profile e^{−x/2} with its jump at the
window edge x = a, the pole/Chebyshev +2, and Mertens' −γ integrated against e^{−x} — all weighted towards x ≈ a, where
≈ e^D dilates contribute, the opposite of "few dilates". In F's own split the O(1) is 2Q(F₀,F₁) + Q(F₁,F₁) + 2AB with
F₀ ≈ F[−ρ₀e^{−y/2}1_{y>D} + Ψ_1] (the cut-off of the quasi-mode) and F₂ negligible — i.e. the "sign" is in the coupling
of the quasi-mode with its own cut-off at depth D through the Weil kernel at distance ≈ D, which is the explicit formula
at the pole (J.4(a)), not a sawtooth. **Consequence (b): RETRACTED. Consequence (c) (PW data superpose all depths;
E's classes are the Fourier-dual bookkeeping of the sawtooth): ARGUED.** The closing claim of F's verdict, "the sign is
decided in the Euler–Maclaurin transition region (few dilates), not class by class", is therefore half right (not class
by class) and half wrong (not the transition region, on the only data where anyone has computed it).
**3.6 Prop F.5 (shallow data = window form).** supp ρ ⊂ (1,X₀] ⇒ supp Ψ̌_ρ ⊂ (0,log X₀] ✓; on a compactly supported
function the full-line Weil form equals Paper 46's complete window form of its centred translate (Θ_∞ translation
invariant; A ↦ e^{∓T/2}A, B ↦ e^{±T/2}B, AB̄ invariant; autocorrelations invariant; pairs with log q ≥ log X₀ = 2T₀ do
not pair) ✓, with half-length T₀ = ½log X₀ and contacts log n < 2T₀ ✓. X₀ ≤ e^{1.6} = 4.953 ⟺ T₀ ≤ 0.8 ✓. Positivity:
Paper 46 l.143/1109 cite Zhu Thm 1.2 for the complete form at T ≤ 0.8 (CITED; also thm:log5W for T ≤ ½log5 = 0.8047,
unconditional in Paper 46). **Identification depth = half-window: the log-depth log X₀ is the *full* window length
2T₀; F's sentence "the depth of the data on the exterior carrier is the window half-length" is off by the factor 2
(its "depth ≤ 4.95" in X is right).** As F says, such ρ are not in PW_μ; this is E §7's "edge-localised data" remark
extended from X₀ = 2 to X₀ = e^{1.6}. **Label: reduction PROVED; positivity CITED; wording corrected.**
**3.7 F §6 "c(φ)" and §7 table.** The test object c(φ) that F "did not compute in closed form" is computed by J Thm J.3:
c(φ) = (2+γ−log 4π)·B_φ² ≥ 0, = 0 iff B_φ = ∫φe^{s/2} = 0 (then the next order is not computed by anyone). The table of
§7 is PROVED as labelled, with one correction: the row "Lemma 3.1 sawtooth … selects a_n ≡ 1" is a statement about the
*aliasing regime* only — on smooth deep data the sawtooth is negligible for ζ too (§3.5), so what the sawtooth selects is
the scale at which the PW oscillation (1/μ in X near X = 1) meets the integer mesh, i.e. constraint 5's "n ≈ λ/u".

## 4. H — dilated frame, base case, rate identities, (H-ODE), condition (H)

**4.1 Dilated frame (§1): PROVED.** φ(x) = λ^{1/2}f(λx): ‖φ‖ = ‖f‖, f̂(ξ) = λ^{1/2}φ̂(λξ), leak(f) = 2∫_μ^∞|φ̂|² ✓
(η = λξ, μ = λ²), gauge ↦ supp ⊂ [−1/μ,1/μ], nested ✓. g(x) = e^{(x−T)/2}Σφ(ne^{x−T}) = G_φ(x−T) ✓; Poisson with
φ(0) = φ̂(0) = 0, φ even: G_φ(y) = e^{−y/2}Σ_{k≥1}φ̂(ke^{−y}) ✓, G_φ(−2T) = μ^{1/2}Σ_kφ̂(kμ) ✓, G_φ(0⁻) = φ(1) = 0,
G_φ′(0⁻) = ½φ(1) + φ′(1) = φ′(1) ✓. W_T(Ef) = 𝒲[G_φ1_{(−2T,0)}] by translation invariance (checked as in §3.6) ✓.
This is F Prop F.0 in the dual rescaling (F fixes the band at 1 and lets the support grow; H fixes the support at
[−1,1] and lets the band grow): consistent.
**4.2 Prop H.1 (base case): PROVED given Mori Theorem O.** W_T(g) ≥ 2^{−2904}‖g‖² for C² g on I_{½log15} (L104; the
Zenodo frontier audit B1 reproduced the certificate and the scalars: label CITED, not UNVERIFIED as the 05b row still
says — that row should be updated); restriction to smaller windows is trivial (no lem:monoT needed). Memo A Lemma 4.2:
ℓ(g) ≤ C₀μ²‖g‖². Hence W_T ≥ 2^{−2904}C₀^{−1}μ^{−2}ℓ, A = 2, and with κ = 2^{−2905}/C₀: Δ ≥ 2^{−2904} − 2^{−2905} =
2^{−2905} ✓. Trivial, as H says; it is the first explicit (κ,A) at any window. Note the C²-vs-L² and primitive-vs-complete
conventions flagged in 05b l.56: H uses the complete form on C² g, which is Theorem O's statement ✓.
**4.3 Lemma H.2: PROVED.** d/dc 2∫_{c/2π}^∞|φ̂|² = −(1/π)|φ̂(c/2π)|² ✓. The Slepian check is right but uses one more
fact than stated: ψ_n(c;·) moves with c, and d/dc leak_c(ψ_n(c)) equals the fixed-φ derivative by Hellmann–Feynman (ψ_n
is the extremiser of λ_n); with |μ_n|² = 2πλ_n/c and |ψ̂_n(c/2π)|² = |μ_n|²ψ_n(1)² one gets (1−λ_n)′ = −(2/c)λ_nψ_n(1)²,
AUDIT_1 §3's identity ✓. Rate 2 − (n+½)/c from 1−λ_n ≈ K_nc^{n+½}e^{−2c} ✓. Lemma H.3 (Dini bounds): PROVED, and the
honest remark that the gauge shrink gives no upper bound on D⁺L_c is right — this is why ρ_L is only ARGUED at the bottom.
**4.4 Thm H.4 (dN/dT): PROVED.** N(T) = −𝒲(g,Ψ) with g = G1_{(−2T,0)}, Ψ = G1_{(−∞,−2T)} (memo A Thm 1.1(c)–(e), using
WG_φ(·−T) = WΦ_f = 0, Guo Lemma 4.4 CITED). Expanding −𝒲 with memo A's sign conventions: ∫∫g(x)Ψ(y)[ν−2cosh](x−y) +
Σc_q∫g(x)Ψ(x−log q) (Ψ(x+log q) = 0 on x > −2T) ✓, k = ν − 2cosh(t/2) ✓, q-integral over (−2T, min(0,−2T+log q)) ✓.
Leibniz in b = −2T, db/dT = −2: d/db[double integral] = G(b)[−∫_{y<b}G(y)k(b−y)dy + ∫_b^0G(x)k(x−b)dx], d/db[q-term] =
G(b)[−G(b−log q) + G(b+log q)1_{log q<2T}]; multiplying by −2 gives dN/dT = −2G(b)(W^−G)(b) with the odd distribution as
defined ✓ (G = 0 on [0,∞) absorbs the indicator). Convergence at t → 0: G Lipschitz (kinks only at y = −log n, the
contacts) ✓. C¹ across 2T = log q: G(b+log q) → G(0⁻) = 0 ✓. Lemma H.5 (residue-1 cancellation inside W^−): re-derived,
the +∫G(b−t)e^{t/2}dt of the comb's main term cancels the −∫G(b−t)e^{t/2}dt of the pole, leaving the display ✓
(convergence: G(b−t)e^{t/2} = O(e^{−t})) ✓. Rem H.6: identity-level, ARGUED ("formally").
**4.5 Cor H.4′: SIGN ERROR.** The non-smooth piece of dN/dT is −2c_qG(b)[−G(b+log q)]1 = +2c_qG(b)G(b+log q)1_{log q<2T}.
Its T-derivative is 2c_q(−2)[G′(b)G(b+log q) + G(b)G′(b+log q)] → −4c_qG(b)φ′(1) as T ↓ ½log q, and 0 from the left.
So [d²N/dT²]₊ − [·]₋ = **−4c_qG_φ(−log q)φ′(1)**, not +4 (H dropped the minus sign of −G(b+log q)). Harmless for every
conclusion drawn (the sign is that of G_φ(−log q)φ′(1), a property of the test; second order; indefinite). **Label:
PROVED with the sign corrected.**
**4.6 (H-ODE), Thm H.5, condition (H).** ∂_cQ = −ρ_NN + (ρ_L + A/c)κμ^{−A}L = −ρ_NQ + (ρ_L − ρ_N + A/c)κμ^{−A}L ✓
((μ^{−A})′/μ^{−A} = −A/c ✓). With L > 0: ∂_cQ(φ*) ≥ −ρ_NQ ⟺ (H) ✓; Hellmann–Feynman gives Δ′ ≥ −ΦΔ with Φ = ρ_N +
∂_c log‖g*‖², and Grönwall from Δ(c₀) = 2^{−2905} > 0 keeps Δ > 0 provided Φ is locally integrable (ρ_N bounded above by
(H) and ρ_L; large negative ρ_N only helps) ✓. **(H) ⇒ L′♯: PROVED modulo 4.1 (existence/simplicity/continuity of the
pencil minimiser and HF: CONDITIONAL, as H labels it; Danskin gives only the upper Dini derivative unconditionally, so
the Grönwall direction genuinely needs 4.1).** H.5(ii) "(H) not necessary": correct. **Is (H) ⇒ L′♯ correct? Yes, with
those provisos; and (H) is a condition at the minimiser with relative precision O(1/c) in the rate (both rates are
2 + O(1/c)), i.e. a virial inequality of the W-lin/lem:flowdet type.** The claim in §4.3(c) that (H) is at TV-distance
e^{−2c} from failure is ARGUED (δ_{u₀}-perturbation transported to the derivative; not written out). The crossing
requirement (H_q) is a correct necessary condition for the Ψ ≡ 0 scheme (ARGUED: the "≈ μ/log μ contacts, average loss
O(A log²μ/μ)" budget is a heuristic count), and the comparison with PATTERN_001's sawtooth (κ drops 8–15 % per contact)
is NUMÉRICO. Falsifier table: PROVED as labelled (the cΛ row rests on CERT_FALSIFIERS_001, CITED; the base case for cΛ
holds only for T ≤ ½log2 where every comb is empty ✓).
**4.7 Class NO-GO 𝒦_H.** H's reason — closure ⟺ (H), a functional of the minimiser, not implied by Slepian/crossings/
residue cancellation, and TV-fragile — is correct and is a *reduction*, not an impossibility proof: it shows that the
differential scheme adds nothing to (★★) (the integrated (H-ODE) is Q_c(φ*_c) ≥ 0, a restatement), and that the three
listed inputs cannot supply (H). **Label: NO-GO as ARGUED (class defined by its inputs), consistent with R186_038 α.3,
I16, INV_U §3; the identities (dilated frame, band-edge rate, W^−, dN/dT, Cor H.4′ corrected, (H), (H_q)) are PROVED
objects.** One further remark H does not make: in the dilated frame the left-edge value G_φ(−2T) = μ^{1/2}Σ_kφ̂(kμ) is
exactly the aliasing sum of the band edge (memo A Rem (ii)), so dN/dT = −2·(edge aliasing)·(odd Weil pairing at the
edge): the derivative identity says that the window form changes only through the band-edge alias, which is a one-line
proof that any T-flow argument is a statement about the out-of-band tail — i.e. about (★★). This is the cleanest
statement of the wall in the record and should be the one cited.

## 5. J — kernels, NO-GO J.2, deep quasi-mode J.3, Cor J.4 (NUMÉRICO where stated)

**5.1 Prop J.1 (a)–(f): PROVED.** (a) J(m,n) = m^{−1}C_{n/m}(mλ) ✓ (v = mu). (b) prime part = Σ log(mn)J(m,n): E.2 + sym-
metrisation ✓. (c) single-integral ratio classes ✓. (d) ✓. (e) FΨ̌ = ∫_λ^∞r(v)v^{−½−iτ}ζ_{≤v/λ}(½−iτ)dv: this is F Thm
F.1 in the variable v = λX (ζ_{≤X}(½−iτ) = ζ_X(1−s)) ✓ — F and J have the same partial-sum formula. (f) Stieltjes form
and 𝒞 = ∫D_t d(ψ(t)−t), 𝒲_ext = ã-form − 2⟨H,𝒞H⟩ = Lemma E.4 ✓. Note 𝒞 is not symmetric (S_u* = S_{−u} on the half
line), so the cross terms ⟨Ψ_0,𝒞Ψ_1⟩ and ⟨Ψ_1,𝒞Ψ_0⟩ are distinct — J correctly computes both in J.3(iii).
**5.2 Thm J.2 (no Hilbert kernel in the integer index).** (a) PROVED (= J.1(b)). (b) PROVED: for data beyond both
truncations 𝓛(s_m,s_n) = (mn)^{−1/2}c_{r̃}(log(n/m)), c_{r̃}(t) = (1/2π)∫(Θ_∞−b_∞)|Fr̃|²cos τt dτ, bounded by 𝓛[r̃]; with
active truncations the common jump at a gives ∫_0^1∫_0^1dsdt/(s+t) < ∞ ✓. (c) Riesz projection ✓. **Rem 2.1 (correction
to E.1′): PROVED and accepted; AUDIT_1 §1.1's "E.1′ PROVED" is amended to "PROVED in the polarised reading" (§3.4).**
**The class NO-GO is ARGUED, not PROVED:** the literal object the brief named (an antisymmetric 1/(log m − log n) matrix
against "the Lévy singularity ½") indeed does not exist, but the object that *does* exist is (mn)^{−1/2}c_{r̃}(log n/m):
a Toeplitz-in-log matrix whose symbol c_{r̃} is bounded, continuous and **positive-definite** (Fourier transform of the
nonnegative measure (Θ_∞−b_∞)|Fr̃|²dτ), hence a Bochner object — and for Paley–Wiener data, which oscillate at scale 1/μ
in y near a, c_{r̃}(t) is concentrated on |t| ≲ 1/μ: a kernel *peaked at m ≈ n at relative resolution 1/μ*, the "m ≈ kn"
of the semiring principle. Inequalities indexed by (m,n) do have that object (large-sieve/Toeplitz-type, not Hilbert's);
what excludes them as a sign source is A §5 + N_018 (Bochner on the Lévy block + bounds on the rest is comb-generic),
not the absence of a kernel. **Thm J.2 statement PROVED; "NO-GO for any (m,n)-indexed inequality" ARGUED and narrowed to
"no antisymmetric Hilbert/MV kernel".**
**5.3 Thm J.3 (deep quasi-mode): PROVED given PNT (Mertens with constant −γ), all constants verified (NUMÉRICO).**
Derivation re-done: F_x(m) = m^{−1/2}φ(x+log m−c) = L^{−1/2}g(m/L), L = e^{c−x}, g(ρ) = ρ^{−1/2}φ(log ρ) ∈ C_c^∞(1,e);
Poisson: Σ_mF_x(m) = L^{1/2}B_φ + Σ_{k≠0}L^{1/2}ĝ(kL) (∫g = ∫e^{s/2}φ = B_φ ✓; supp(L,eL) ⊂ (0,∞) for L > e^{−1}) ✓.
Ψ_0 = B_φe^{(c−x)/2}1_{(a,c)} = Be^{−x/2}1_{(a,c)}, B²e^{−a} = B_φ²e^D ✓; Ψ_1 superpolynomially small on (a,c−C), O(1) on
(c,c+1), zero beyond, one jump of size B_φ at c ✓. (i) |FΨ_0|² = B²e^{−a}|1−e^{−D(½+iτ)}|²/(¼+τ²) ✓; c₀ = (1/2π)∫ã/(¼+τ²):
via the Lévy representation c₀ = b_∞ + 2∫ν(1−e^{−u/2}) + 2 with 2∫_0^∞e^{−u/2}(1−e^{−u/2})/(1−e^{−2u})du = 4∫_0^1dw/
((1+w)(1+w²)) = log 2 + π/2 ✓. NUMÉRICO: ψ(¼) − log π = −5.372183419, log 2 + π/2 = 2.263943507, c₀ = −1.108239912 =
ψ(3/2) − log π to 30 digits, and the *direct* integral (1/2π)∫[Re ψ(5/4+iτ/2) − log π]/(¼+τ²)dτ = −1.108239912 agrees;
(1/2π)∫Θ_∞/(¼+τ²) = −3.108239912 = c₀ − 2 ✓. (ii) (𝒞Ψ_0)(x) = Be^{−x/2}[Σ_{q<Y}Λ(q)/q − log Y], Y = e^{c−x} ✓; Mertens
Σ_{n≤Y}Λ(n)/n = log Y − γ + o(1) (the o(1) is PNT-strength; CITED) ⇒ 2⟨Ψ_0,𝒞Ψ_0⟩ = −2γB_φ²e^D + o(e^D) by dominated
convergence of ∫_0^De^{−t}ε(e^{D−t})dt ✓. Separately 2A(Ψ_0)B(Ψ_0) = 2D(1−e^{−D})B_φ²e^D ✓ and Σc_q2⟨Ψ_0,S_{log q}Ψ_0⟩ =
2B_φ²e^D(D−1−γ+o(1)) ✓ (∫_0^∞te^{−t} = 1), difference 2+2γ ✓. (iii) ã-cross O(e^{D/2}) by Cauchy–Schwarz (∫|ã||FΨ_1|² =
O(1): Ψ_1 Lipschitz with one jump, bounds uniform in D) ✓; ⟨Ψ_1,𝒞Ψ_0⟩ = O(1) ✓; ⟨Ψ_0,𝒞Ψ_1⟩ re-derived: = B∫Ψ_1(y)e^{−y/2}
[(ψ(e^{y−a}) − e^{y−a}) − (ψ(e^{y−c}) − max(1,e^{y−c}))]dy, first bracket o(e^{y−a}) by PNT against ∫|Ψ_1|e^{(y−c)/2} =
O(1) ⇒ o(e^D), second bracket O(1) ⇒ O(1) ✓. Total (2+γ−log 4π)B_φ²e^D + o(e^D). NUMÉRICO: c₀ + 2γ = 0.04619141793 =
2 + γ − log 4π = 2(ξ′/ξ)(1) (numerically differentiated log ξ at 1: 0.04619141793) ✓. (J.3a) holds for the full Zr
(cross term O(e^{D/2})), hence (J.3b) for the full Zr by subtraction ✓. **Dependence on PNT:** only through the constant
−γ in Mertens' formula and ψ(Y) − Y = o(Y) in (iii); the zero-side check J.4(a) needs *no* PNT (dominated convergence
on Σ|ρ|^{−2}, 0 < Re ρ < 1), so the explicit formula route proves J.3 for Ψ_0 unconditionally and J's arithmetic route
is the one that needs PNT. Both give the same number: consistent.
**5.4 Cor J.4.** (a) PROVED/CITED: Φ_{Ψ_0}(s) = B(e^{(s−1)c} − e^{(s−1)a})/(s−1) ✓, product expands to e^{−a}/(ρ(1−ρ)) +
three terms bounded by e^{−a} and → 0 (Re ρ < 1) ✓; Σ_ρ1/(ρ(1−ρ)) = 2Σ_ρ1/ρ = 2(1 + γ/2 − ½log 4π) = 2 + γ − log 4π ✓;
ξ′/ξ(1) = 1 − ½log π + ½ψ(½) + γ ✓ (ψ(½) = −γ − 2log 2 gives 1 + γ/2 − ½log 4π ✓). The explicit formula for the rough
test Ψ_0 (jumps at a and c) is Paper 46 lem:roughEF, fine. **(b) PROVED:** c₀ = ψ(3/2) − log π = −1.108 < 0 (NUMÉRICO)
— the archimedean form with the pole, i.e. ã, is negative on the deep mode, and 2γ = 1.154 restores +0.046: a 4 %
margin. The "NO-GO for archimedean dominates primes" is the quantitative form of A §5's NO-GO ✓. **(c) OVERSTATED in
its O(1):** for the full Ψ̌ the prime part is D·B_φ²e^D + O(e^D) (J's own parenthesis), so form_c = [0.046 − 2(c−1)(D +
O(1))]B_φ²e^D, not 0.046 − 2(c−1)(D−1−γ) (that is the quasi-mode alone); the conclusions (negative for c > 1 at large
D, → −∞ without the pole, a_P undetected) survive. Also note these are *hybrids* (ζ's summation map Z with another
comb), not the index falsifiers E_c/a_P; J says so for cΛ. **(d) PROVED** (= E.5 with the value).
**5.5 J §4.1 (deep mode outside PW): PROVED, elementary** (a bump of relative width 1 at ξ ≈ λe^D is the restriction
of an f supported in length ≍ (λe^D)^{−1} < 1/λ: in the gauge); the density remark ARGUED and unused ✓. Constraint 9 as J
states it ("a mechanism that extends to C_c^∞ must reproduce 0.046") is a *consistency test*, not a constraint on
proofs of (★★): (★★) is quantified over PW_μ modulo the radical, and a proof need not extend; downgraded in §7.

## 6. Cross-check (priority 7): are F, J and E/AUDIT_1 the same mechanism?

No, and none is a mechanism. (1) On the only data where the value has been computed (smooth bump at depth D), all three
bookkeepings evaluate one number, 𝒲_ext[Zr] = 2(ξ′/ξ)(1)·B_φ²e^D + o(e^D) = (Σ_ρ 1/(ρ(1−ρ)))·B_φ²e^D: the Weil
distribution at the pole s = 1, a *global* constant of ζ. (2) It is not localised in the Euler–Maclaurin transition
region (F; falsified §3.5: the transition contributes o(e^D) and the sawtooth F₂ is negligible on smooth data), not in
any ratio class (E.5/J.4(d): every class is −log²·e^D), and "in the Chebyshev remainder" (J) only in the sense of J's
term-type anatomy, which is label-dependent: writing the same number as [ã-form −1.108] + [Mertens +1.154] or as
[Θ_∞-form −3.108] + [pole vs Chebyshev main +2] + [Mertens +1.154] moves the "carrier" of the sign between labels; what
is invariant is the 4 % excess 2γ − (log π − ψ(3/2)) = 0.046 > 0, equivalently ξ′(1) > 0, Hadamard. (3) The three are
*consistent*: F's split on deep data reduces to 2Q(F₀,F₁) + Q(F₁,F₁) + 2AB with F₀ the quasi-mode's cut-off, which is
J's Ψ_0 against its own truncation; E's cross-class cancellation is J.4(d) with its value. (4) None of them is in the
regime of (★★): the deep mode is a radical direction for PW data (J §4.1, F §5(c)); on PW data all depths D ≤ log μ are
superposed at the aliasing scale 1/μ and no one has evaluated anything. (5) The semiring reading
survives in two precise forms only: J.2(b)'s Toeplitz-in-log symbol c_{r̃} peaked at |log(n/m)| ≲ 1/μ (archimedean side)
against the diagonal weight log(mn) on the Gram matrix of dilates (prime side); and the deep-mode constant 2γ (Mertens:
Λ∗1 = log composed with H(Y) − log Y → γ) against ψ(3/2) − log π (Γ_ℝ + Lévy + pole). Neither is a sign on PW data.

## 7. Updated consolidated statement and constraint list

**(★★) unchanged** (AUDIT_1 §6.3), now with the three PROVED equivalent spellings added by F and J:
  (★★_u)  𝔔[ρ] ≥ κμ^{−A}dist²_{L²(1,∞)}(ρ,𝒢̄₁)  ∀μ ≥ 5, ∀ρ ∈ PW_μ  (F Prop F.0: one fixed form, fixed radical; all
  μ-dependence in the data class);
  (★★_EM)  2Q(F₀,G) + Q(G,G) + 2A(ρ)B(ρ) ≥ κμ^{−A}dist²(ρ,𝒢̄₁), F₀ = ζ(1−s)·Fρ̃ (Q-null, pointwise), G = ρ₀/s +
  ∫ρX^{−s}e_s(X)dX (F Thm F.2; the pole term unsplit);
  (★★_St)  (1/2π)∫ã|∫_λ^∞r(v)v^{−½−iτ}ζ_{≤v/λ}(½−iτ)dv|²dτ − 2⟨Zr,𝒞Zr⟩ ≥ κμ^{−A}dist²(r,𝒢̄), 𝒞 = ∫D_t d(ψ(t)−t) (J §4.2).
Base case (H Prop H.1, given Mori Theorem O CITED): (★★) holds for 5 ≤ μ ≤ 15 with A = 2, κ = 2^{−2905}/C₀. OPEN for
μ > 15.

**Constraints 1–7** (AUDIT_1) stand, with two amendments: in 3, "E Thm E.1′ ratio-class kernel" is to be read polarised
(J Rem 2.1; F Thm F.3's display likewise); in 5, "lattice aliasing" is now explicit: the ℤ-specific piece is the Poisson
remainder e_s(X) of ζ_X(1−s) (F Lemma 3.1), which is *negligible on smooth deep data* and matters only at the aliasing
scale 1/μ of PW data (§3.5) — the sawtooth selects a_n ≡ 1 only there.
**8. No antisymmetric Hilbert kernel in the integer index (J Thm J.2, PROVED as stated).** The prime pairing of dilates is
log(mn)·J(m,n) (diagonal weight on the Gram matrix); the archimedean pairing is (mn)^{−1/2}c_{r̃}(log n/m) with c_{r̃}
bounded, continuous and positive-definite, peaked at |log(n/m)| ≲ 1/μ on PW data. Hilbert/Montgomery–Vaughan bounds have
no object; Toeplitz/large-sieve-type bounds do, but are Bochner + C–S (constraint 2/4) and comb-generic. Do not retry
either on the exterior carrier.
**9. Deep-mode value (J Thm J.3, PROVED given PNT; test object, not a constraint on (★★)-proofs).** On smooth data at depth
D, 𝒲_ext[Zr] → (2+γ−log 4π)B_φ²e^D = 2(ξ′/ξ)(1)B_φ²e^D, anatomy ψ(¼)−log π (−5.372) + log 2 + π/2 (+2.264) + 2 (pole vs
Chebyshev main, residue 1) + 2γ (Mertens, a_n ≡ 1) = 0.046; archimedean-with-pole ã-value −1.108 < 0. Any argument that
is also valid on C_c^∞ data must reproduce this; "archimedean dominates primes" cannot (quantitative A §5). This closes
F §6's test object c(φ) = 0.046·B_φ². The deep mode is a radical direction for PW data, so this says nothing about (★★).
**10. The pole term couples the Q-null vector (F Thm F.2/§3.3 here).** In every split of F into a full-line (symbol-null)
part and a truncation defect, 2AB contains a product of the null part's Mellin values at s = 1 and s = 0; no block
argument that ignores 2AB (or that treats the null part and the defect as independent) applies; "the sign is in the
coupling" is a restatement of memo A §3.2 (all of W_T is the truncation at x = a).
**11. No differential/continuation argument closes without the virial bound (H Thm H.5, PROVED modulo 4.1; class 𝒦_H
NO-GO as ARGUED).** dN/dT = −2·(band-edge alias)·(odd Weil pairing at the edge), so every T- or c-flow of the window
form is a statement about the out-of-band tail; the Grönwall scheme for the pencil 𝔐 − κμ^{−A}D closes iff (H) ρ_N ≤
ρ_L + A/c at the minimiser, a relative-precision-O(1/c) virial inequality that is a functional of the minimiser and is
TV-fragile at scale e^{−2c} (ARGUED). Crossings enter at second order with coefficient −4c_qG_φ(−log q)φ′(1), sign of
the test. Do not retry with another denominator unless an independent virial bound at relative precision 1/c, or the
edge-autocorrelation bound (H_q), is first proved.

## 8. Label table and verdict

| item | memo label | audit label |
|---|---|---|
| F Prop F.0 (universal form, radical fixed) | PROVED | PROVED (closure ⊂ ker 𝔔 via dist only; density reading ARGUED) |
| F Thm F.1 (partial sums, Θ_∞ = −2Re ζ′/ζ) | PROVED | PROVED (NUMÉRICO check); Rem 2.1 "no zero data" ARGUED/overstated (zeros sit in F₀ and in χζ′(1−s)) |
| F Lemma 3.1, Thm F.2(i)–(iv) | CITED/PROVED | PROVED as identities; F₀ is Q-null, not 𝔔-null (2AB unsplit, contains an F₀–F₀ piece) |
| F Cor 3.2 | PROVED | abstract lemma PROVED; application to 𝔔 ARGUED (premises fail: pole term, non-product set); restatement of A §3.2 |
| F Thm F.3 (Hilbert-type kernel) | PROVED | kernel computation PROVED; display "regular part = −∫∫ρρ𝒦" RETRACTED (divergent on every rational line; polarised reading required, = J Rem 2.1) |
| F Prop F.4 (i)–(iii) | PROVED | PROVED (consistent with J.3) |
| F Prop F.4 consequence (b) (sign = sawtooth in transition region) | PROVED | FALSE / RETRACTED (F₂ superpolynomially small on smooth deep data; transition contributes o(e^D); value is bulk, = explicit formula at the pole) |
| F Prop F.5 (shallow = window, Zhu) | PROVED/CITED | PROVED reduction, CITED positivity; "depth = half-window" corrected to "log-depth = full window 2T₀" |
| F §7 table, NO-GOs | PROVED | PROVED as labelled; sawtooth row restricted to the aliasing regime |
| J Prop J.1 (a)–(f) | PROVED | PROVED |
| J Thm J.2 (no Hilbert kernel) | PROVED, class NO-GO | statement PROVED; class NO-GO ARGUED and narrowed (Toeplitz-in-log PD symbol peaked at 1/μ exists; excluded by A §5/N_018, not by absence) |
| J Rem 2.1 (E.1′ literal reading diverges) | PROVED | PROVED; AUDIT_1 §1.1 amended: E.1′ PROVED in polarised reading only; E.5 unaffected |
| J Thm J.3 (deep quasi-mode 0.046) | PROVED given PNT | PROVED given PNT (CITED); all constants NUMÉRICO-verified to 30 digits; zero-side route needs no PNT |
| J Cor J.4(a),(b),(d) | PROVED/CITED | PROVED/CITED (c₀ = −1.108 NUMÉRICO) |
| J Cor J.4(c) (pins c = 1) | PROVED | PROVED with O(1) corrected: 0.046 − 2(c−1)(D + O(1)); hybrids, not the index falsifiers |
| J constraints 8, 9 | — | 8 adopted (narrowed); 9 adopted as test object |
| H §1 dilated frame | PROVED | PROVED (= F Prop F.0 dual) |
| H Prop H.1 base case | PROVED, Mori CITED | PROVED given Mori Thm O (CITED; B1 reproduced; 05b row L104 to update from UNVERIFIED) |
| H Lemma H.2, H.3 | PROVED | PROVED (Slepian check needs HF, implicit) |
| H Thm H.4 (dN/dT), Lemma H.5 | PROVED | PROVED |
| H Cor H.4′ | PROVED | PROVED with sign corrected: jump = −4c_qG_φ(−log q)φ′(1) |
| H (H-ODE), Thm H.5(i) | PROVED modulo 4.1 | PROVED modulo 4.1 (CONDITIONAL); (H) ⇒ L′♯ correct |
| H §4.3(c) TV-distance e^{−2c}, (H_q), sawtooth reading | PROVED/ARGUED/NUMÉRICO | ARGUED / ARGUED / NUMÉRICO |
| H class NO-GO 𝒦_H | NO-GO | NO-GO as ARGUED (reduction to (H); subsumes R186_038 α.3, I16, INV_U §3) |

**Do not retry:** Hilbert/MV/Perfekt bounds in the integer index on the exterior carrier (J.2, F §4.3); Toeplitz/large-
sieve bounds on c_{r̃} as a sign source (Bochner + C–S); "(1,1) class bounded after the pole" (F.4/E.5); 2Q(F₀,F₂)+Q(F₂)
alone (F-DH, F §7); any block argument on (F₀,G) ignoring 2AB (§3.3); Grönwall/continuation in T or c without an
independent virial bound (H); "sign localised in the Euler–Maclaurin transition region" as a premise (§3.5).
**Objects for REF-D:** (★★_u), (★★_EM), (★★_St); the base case (κ,A) = (2^{−2905}/C₀, 2) on μ ≤ 15; F₀ = F[Ψ_full −
ρ₀e^{−y/2}] as the Q-null vector; the identity F₂ = F[−(Ψ_full − ρ₀e^{−y/2})1_{y<0}]; the deep-mode constant
2(ξ′/ξ)(1) = 0.0461914 with its anatomy; c_{r̃} as the archimedean dilate symbol; W^− and dN/dT = −2G_φ(−2T)(W^−G_φ)(−2T);
(H), (H_q). No sign is claimed. Row D OPEN.
