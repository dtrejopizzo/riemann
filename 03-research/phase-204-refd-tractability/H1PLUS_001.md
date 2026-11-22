# H1PLUS_001 — (phase 204t): H1⁺ = n₋(𝔄_ev(T)) ≤ 1 ∀T, EXACT inertia accounting via the comb structure

OPEN / NO-GO / NUMERICAL. Single file written.

## Summary (≤250 words)

On Paper 46's own definitions (eq:W, lem:roughEF, prop:WT), for F real even on 𝒟_T:
**𝔄_ev(F) = Z_T(F) − 2⟨F,χ_ev⟩²**, Z_T(F) := Σ_ρ Φ_F(ρ)² = W^ev_T(F) (PROVED, it is lem:roughEF read on the even sector).
The truncated comb leaves no "tail": c_F(log n) = 0 for n ≥ e^{2T} (support), so "window comb" = "full comb", and no
boundary term appears: the killing κ of rem:ext-killing(i)/thm:A is an internal rewriting of the archimedean term, not an
extra summand (PROVED). Exact accounting: n₋(Z_T) ≤ n₋(𝔄_ev) ≤ n₋(Z_T) + 1 (PROVED). In Z_T each quadruple of
off-line zeros contributes 4[(Re Φ_F(ρ))² − (Im Φ_F(ρ))²], signature (1,1); on-line zeros contribute |F̂(γ)|² ≥ 0
(PROVED). CALIB's "1" (n₋(𝔄_ev) = 1 for ζ) is exactly the subtracted polar direction (−2χχᵀ); Epstein's "2" at T = 2 is
pole + one hyperbolic pair (consistent, NUMERICAL). With a boundary-concentration lemma (ARGUED) n₋(𝔄_ev(T)) →
1 + #hyperbolic pairs, hence **H1⁺ ∀T ≡ W^ev ⪰ 0 ∀T = D^ev** (⇐ PROVED; ⇒ ARGUED). H1⁺ is not a "half" of D^ev: ∀T it is
the whole D^ev read via P4. The cancellation of ≈4T archimedean directions by the comb IS the explicit formula; no
distinct exact mechanism exists. The frequency reading (partial sum of the comb ≈ m) requires ψ(x) − x at scale x^{1/2}:
zero-side data; Chebyshev/dlVP give neither size nor sign.
**Verdict: NO-GO (REF-D by P4) for H1⁺ as an independent route.** OPEN with name: Lemma LCB (boundary), prediction a_P.

## 0. Corpus check (mandatory)

grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` and in phase 204:
- «H1⁺»: WT_HALVES_001 (204n: H1⁺ OPEN, necessary, class (L2)); H1_TRACT_001 (204r: Lemma A∞, NO-GO 𝒦_PF, TRANSFER to
  (N_loc)/K34). «n₋ ≤ 1», «inertia», «second eigenvalue», «Weyl»: H1_TRACT §2–§4 (Weyl useless in the direction asked;
  λ₂ ∈ 𝒦_W CITED, 𝒦_H ARGUED). «(L2)», «N_loc», «K34»: L2_INTERLACE_001 (Lemma T3, Haynsworth), WEAKEN_001 K34
  («equivalent to the datum»). «𝒦_W», «BARRIER_W»: phase 197, continuation in T. «truncated translation», «comb rank»,
  «prolate», «low frequency»: no own entry for the identity 𝔄 = Z − 2ℓ² on the even sector. «LEDGER_L2 nodes»,
  «large entries»: reading of LEDGER_L2 (archimedean nodes predict the sign of large entries; arithmetic in the small
  ones) — compatible with §3 below. «zero-side», «thm:Z», «REF-D»: INV_F_001, INV_S_001, thm:Z (flat-top certificate
  = smoothing of the zero side, REF-D).
- **New reason, written out** against (L2)/𝒦_W/H1_TRACT: the second eigenvalue is not estimated, there is no continuation
  in T, and Weyl/norms are not used. An EXACT mechanism is used: the comb as a finite sum of symmetrized translations
  τ_{±log n}, whose action on the window is identical to that of the full comb (support), plus the explicit formula for
  rough tests (lem:roughEF), to write 𝔄_ev as (zero-side form) − (rank-one polar term) **as an identity of forms**, and to
  count the exact inertia. None of this appears in the index as an accounting of n₋(𝔄_ev). If the result is REF-D, it is
  declared NO-GO (it is: §4).

## 1. Exact structure of 𝔄_ev on the window

### 1.1 Definitions (P46, verified against the text)
- eq:Aform / l.118–135: 𝔞_T(F) = (1/2π)∫ m|F̂|² − Σ_{n∈N_T} v_n c_F(log n), c_F(u) = ∫F(t)F(t+u)dt (autocorrelation
  form), 𝒟_T = {F ∈ L²(I_T): ∫log(2+|τ|)|F̂|² < ∞}.
- eq:W: W_T(F) = 𝔞_T(F) + 2Re(A(F)\overline{B(F)}), A(F) = ∫F e^{t/2}, B(F) = ∫F e^{−t/2}.
- lem:roughEF: if in addition Σ_ρ|Φ_F(ρ)Φ_F(1−ρ)| < ∞, W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ), Φ_F(s) = ∫F(t)e^{(s−½)t}dt.
- prop:WT: 𝔄 = 𝔞_T|𝒟^par, W^par = 𝔄 + 2ε_par χχᵀ, χ_ev = cosh(t/2)1_{I_T}, ε_ev = +1.
Coherence: for F even, A(F) = B(F) = ⟨F,χ_ev⟩, so 2Re(AB̄) = 2⟨F,χ_ev⟩²; for F odd, B = −A = −⟨F,χ_odd⟩,
2Re(AB̄) = −2⟨F,χ_odd⟩². Matches ε_ev = +1, ε_odd = −1 (PROVED, one line).

### 1.2 The comb as a sum of translations and the "tail" (PROVED)
c_F(log n) = ⟨F, τ_{log n}F⟩ with (τ_uF)(t) = F(t+u). As a quadratic form,
−Σ_n v_n c_F(log n) = ⟨F, C F⟩, C = −Σ_n (v_n/2)(τ_{log n} + τ_{−log n}).
On L²(ℝ), τ_u is the Fourier multiplier e^{iτu}, so (formally) C = −c(D) with c(τ) = Σ_n v_n cos(τ log n).
But (i) Σ_n v_n cos(τ log n) does NOT converge at any real τ (v_n = Λ(n)n^{−1/2}: Σ v_n diverges like 2X^{1/2});
(ii) for F ∈ L²(I_T), supp(F) ∩ supp(τ_{±log n}F) has measure zero if log n ≥ 2T, so c_F(log n) = 0 for n ≥ e^{2T}.
Exact consequence: **on the window the "prime tail" does not exist**: P_T C_{≤e^{2T}} P_T = P_T C P_T as forms over
L²(I_T), where C is the full sum (each summand is a well-defined form and only finitely many are nonzero). Nothing
needs truncating: the truncation n ≤ e^{2T} is automatic.

### 1.3 "σ ≡ 0" is not a multiplier identity (PROVED)
The objective proposes 𝔄_ev = P_T σ(D) P_T with σ(τ) = m(τ) − c(τ). The correct statement: σ is not a function. As a
distribution (on tests whose F̂ is entire of exponential type, i.e. Paley–Wiener of the window) the explicit formula says
  (1/2π)∫ m|F̂|² − Σ_n v_n c_F(log n) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ) − 2Re(A\bar B),
that is, "σ = 2π Σ_γ δ_γ (plus masses at complex γ, read by continuation of F̂) − (evaluation at ±i/2)". The two pieces
on the right-hand side are NOT measures on ℝ except for the on-line zero part: the off-line zeros and the pole are read
by evaluating F̂ at complex points (γ − iβ, ±i/2). That is why 𝔄_ev is not a Fourier multiplier and the truncation P_T
"breaks" nothing: the identity lives in Paley–Wiener, where evaluation at complex points is a continuous functional.

### 1.4 Form identity on the even sector (PROVED, given lem:roughEF)
For F real and even, Φ_F(1−s) = ∫F(t)e^{−(s−½)t}dt = Φ_F(s). Hence, on the dense kernel 𝒞 = C_c^∞(I_T)^{ev} (where
hypothesis (b) of lem:roughEF holds: Φ_F decays rapidly in the strip and Σ_ρ 1/(1+|γ|²) < ∞):
  **𝔄_ev(F) = Z_T(F) − 2⟨F,χ_ev⟩²,  Z_T(F) := Σ_ρ Φ_F(ρ)²  (= W^ev_T(F)).**   (1.4)
Closure: 𝔄_ev and ⟨·,χ⟩² are closed/bounded in the form norm of 𝒟_T; Z_T := 𝔄_ev + 2⟨·,χ⟩² is defined by that
equality on 𝒟^ev_T and coincides with the sum over zeros where the latter converges absolutely (lem:roughEF). Inertias
are computed on the kernel (n₋ of a closed semibounded form = n₋ on any kernel, by min–max). PROVED.

### 1.5 Boundary terms: there are none (PROVED)
The killing κ(x) = ∫_{|y|>T}K(|x−y|)dy of thm:A/prop:wh-index(i), and its analogue κ(y) ~ ½log(1/(y−T)) in
rem:ext-killing(i), appear when the archimedean term (1/2π)∫m|F̂|² is written as a Dirichlet form over I_T × I_T. It is a
rewriting of the SAME number, not an additional summand: (1.4) uses (1/2π)∫m|F̂|² over the extension by zero, which
already includes the killing. lem:roughEF covers rough tests (jump at ±T) by mollification, with explicit control of the
n in [e^{2T}, e^{2T+2ε}) (where c_F = 0). Hence **H1⁺ is not a statement about a boundary term**: the boundary is
absorbed into an exact identity. (The killing does carry useful information — it is positive and pushes n₋ downward —
but that information is already inside Z_T.)

## 2. EXACT accounting of the inertia

### 2.1 Rank-one sandwich (PROVED)
From (1.4): Z_T = 𝔄_ev + 2ℓℓᵀ, ℓ = ⟨·,χ_ev⟩. For closed semibounded forms and a fixed-sign rank-one perturbation:
  n₋(Z_T) ≤ n₋(𝔄_ev) ≤ n₋(Z_T) + 1.   (2.1)
(min–max; on ker ℓ both forms coincide, codimension 1.) Moreover n₋(𝔄_ev) = n₋(Z_T) + 1 ⟺ there exists F with
Z_T(F) < 2ℓ(F)² in the Z_T-orthogonal complement of the negative part of Z_T; if Z_T ⪰ 0, this is exactly H1⁻ (n₋ ≥ 1),
which AUDIT_204_H1MINUS_001 proves (PROVED) and CALIB certifies at ½log3 (𝔪_{T₀}(χ_ev) < 0, intervals).

### 2.2 Structure of Z_T by zero type (PROVED)
- On-line zero, ρ = ½ + iγ: for F real even F̂ is real and even, Φ_F(ρ) = F̂(γ), contribution |F̂(γ)|² ≥ 0 (lem:roughEF
  last sentence).
- Quadruple {ρ, ρ̄, 1−ρ, 1−ρ̄} with ρ = ½ + β + iγ, β ≠ 0: Φ_F(ρ̄) = \overline{Φ_F(ρ)}, Φ_F(1−ρ) = Φ_F(ρ), so the
  quadruple contributes 2Φ(ρ)² + 2\overline{Φ(ρ)}² = 4[(Re Φ_F(ρ))² − (Im Φ_F(ρ))²]: a form of signature (1,1) on the
  two functionals x_ρ = Re Φ_F(ρ), y_ρ = Im Φ_F(ρ). A **hyperbolic pair** per quadruple.
- Real off-line zeros (γ = 0, pair {ρ, 1−ρ}): contribute 2Φ_F(ρ)², ≥ 0 on the even sector (and ≤ 0 on the odd one).
Hence Z_T = P_T + Σ_{q} 4(x_q² − y_q²), P_T ⪰ 0, and **n₋(Z_T) ≤ N_hip** := #hyperbolic quadruples (PROVED), and by (2.1)
  n₋(𝔄_ev(T)) ≤ 1 + N_hip.   (2.2)

### 2.3 Lower bound: Lemma LCB (boundary concentration) — ARGUED
**Lemma LCB.** If there exists a hyperbolic quadruple with β > 0, then n₋(𝔄_ev(T)) ≥ 2 for T large enough;
more generally n₋(𝔄_ev(T)) → 1 + N_hip (∞ if N_hip = ∞).
*Sketch.* (a) The functionals ℓ, x_q, y_q (q = 1..k) are linearly independent over 𝒟^ev_T for every T > 0 (distinct
exponentials cosh((β_q + iγ_q)t); PROVED). (b) Boundary test: F_T(t) = ψ(t−T+L) + ψ(−t−T+L), ψ ∈ C_c^∞(0,L) modulated at
frequency γ_q and with phase chosen so that x_q(F_T) = 0, |y_q(F_T)| ≍ e^{β_qT}‖F_T‖, while P_T(F_T) ≤
C·log(2+γ_q)·(1+L^{−1})‖F_T‖² with C independent of T (density of on-line zeros; the mass of |F̂_T|² for |τ| ≤ R is
uniform in T because F_T is a translate of a fixed profile). Then Z_T(F_T) ≤ (C′ − 4c e^{2β_qT})‖F_T‖² < 0. (c) The k
boundary tests for distinct quadruples are nearly orthogonal for large T (distinct frequencies, independence of (a))
and orthogonal to the polar direction modulo O(e^{−(½−β)T}) — care is needed here, because ℓ(F_T) ≍ e^{T/2} also grows;
hence ℓ(F_T) = 0 is imposed by combining two profiles (one extra codimension, admissible by (a)). With that, Z_T restricted
to span{F_T^{(q)}} ⊕ (H1⁻ direction) is ≺ 0 of dimension k + 1 and 𝔄_ev ≤ Z_T there. ∎ (ARGUED: (b) needs writing out
with constants and the near-orthogonality in (c); it uses neither continuation in T nor Weyl on 𝔄: it is a direct
construction of a negative subspace of dimension k + 1.)

### 2.4 What CALIB's "1" and Epstein's "2" are
- ζ, 8 windows, n₋(𝔄_ev) = 1 (CALIB_R4_001, NUMERICAL/certified): with Z_T ⪰ 0 on those windows (D^ev there,
  PROVED/CITED up to ½log15), (2.1) gives n₋ ∈ {0,1}; H1⁻ gives 1. **The "1" is exactly the subtracted polar direction
  −2χχᵀ.** There is no contradiction with "zero-side form ≥ 0": 𝔄 is NOT the zero-side form, it is the zero-side form
  minus the pole.
- Epstein x² + 5y² (CALIB §3): n₋(𝔄_ev(2)) = 2. By (2.2) that requires n₋(Z_T) ≥ 1, i.e. W^ev_T not semidefinite at
  T = 2, consistent with the model having hyperbolic quadruples realized at that scale (the row "fails by inertia").
  NUMERICAL, consistent with 2.2–2.3; the CALIB table (1.59: fails by q, 2: fails by inertia) is the transition "the
  hyperbolic pair is first seen through the polar direction (q_ev > −½), then separates as a second negative direction."
- DH (no pole, CALIB §3): ℓ ≡ 0 ⇒ 𝔄 = Z, n₋(𝔄) = n₋(Z) — CALIB's "the only way to fail is n₋(𝔄_odd) ≥ 1" is (2.2)
  with the "+1" absent. Consistent.
- a_P (deletion of 2) at ½log3: n₋(𝔄_ev) = 1 (H1⁺ holds) and D fails via q_ev ≈ −0.408 (NUMERICAL). The model has
  "zeros" on Re s = 0 (factor 1 − 2^{−s}: s = 2πik/log 2), quadruples with β = ½: they grow like e^{T/2}, at the same
  rate as the polar direction. **Prediction (ARGUED by LCB):** n₋(𝔄_ev^{a_P}(T)) → ∞; H1⁺ fails for a_P at large T.
  This corrects the reading of H1_TRACT §1 ("H1⁺ necessary not sufficient" by a_P): it is correct PER WINDOW, not for "∀T".

### 2.5 Odd sector (for completeness; identity PROVED, lower bound ARGUED)
For F odd, Φ_F(1−s) = −Φ_F(s): Z^odd_T = −Σ_ρ Φ_F(ρ)², the line contributes |F̂(γ)|², each quadruple −4Re Φ² (signature
(1,1)), and 𝔄_odd = Z^odd_T + 2⟨·,χ_odd⟩². Then n₋(Z^odd) − 1 ≤ n₋(𝔄_odd) ≤ n₋(Z^odd) ≤ N_hip. B = "𝔄_odd ≻ 0 ∀T"
with LCB forces N_hip ≤ 1 and, combined with the even sector, N_hip = 0. ARGUED.

## 3. H1⁺ ∀T versus D^ev: equivalence (P4 reading)

**Proposition H (⇐ PROVED; ⇒ ARGUED via LCB).** H1⁺ (n₋(𝔄_ev(T)) ≤ 1 ∀T) ⟺ W^ev_T ⪰ 0 ∀T (= D^ev).
- ⇐: W^ev = Z_T ⪰ 0 ⇒ (2.1) n₋(𝔄_ev) ≤ 1. (Already in H1_TRACT §1.)
- ⇒: if W^ev_{T₀} is not ⪰ 0, Z_{T₀} has a negative direction; by (2.2) N_hip ≥ 1 in the sense of (2.2) (P_T ⪰ 0
  produces no negatives); by LCB n₋(𝔄_ev(T)) ≥ 2 for large T: H1⁺ fails. ∎
Reading: "the comb cancels all but one of the ≈ 4T negative archimedean directions" is, word for word, the explicit
formula (1.4) plus "Z_T ⪰ 0": the ≈ 4T directions of Lemma A∞ are those with m < 0 in |τ| < 6.29; the comb compensates
them exactly except for what remains in Z_T (zeros) and in −2ℓ² (pole). The one that survives is the polar one. There is
no "inertia" remainder separable from the sign of the zero-side form: H1⁺ ∀T **is not a half** of D^ev; it is the whole
D^ev expressed in inertia terms. The "half" q_ev (H2) is the one that, at each T, measures whether the polar direction
separates or not — redundant ∀T given H1⁺.

Correction to H1_TRACT_001 / WT_HALVES_001: "H1⁺ necessary not sufficient" holds as a per-window statement; as an ∀T
statement, H1⁺ ⟹ D^ev (ARGUED, LCB). The two "halves" of the WT lemma are not independent in the limit: H2 ∀T follows
from H1⁺ ∀T. (This changes the status of nothing: both were OPEN and remain so; it changes the classification: H1⁺ moves
from "class (L2)" to "REF-D".)

## 4. Is there an exact zero-free mechanism? (point 3 of the objective)

### 4.1 The frequency reading
For F concentrated at frequency a (|a| < 6.29), (1/2π)∫m|F̂|² ≈ m(a)‖F‖² and −Σ_{n≤e^{2T}} v_n c_F(log n) ≈
−‖F‖²·S_T(a) with S_T(a) = Σ_{n≤e^{2T}} v_n w_F(log n) cos(a log n) (w_F = normalized autocorrelation, supported on
[0,2T]). Neutralizing m(a) < 0 requires S_T(a) ≲ m(a). But by partial summation with ψ(x) = x + E(x):
  Σ_{n≤X} Λ(n)n^{−½−ia} w(log n) = ∫_1^X x^{−½−ia}w(log x)dx + ∫_1^X x^{−½−ia}w(log x)dE(x).
The first term is the polar contribution (exactly what produces −2ℓ²; it has size X^{1/2}, not small, and is the reason
why 𝔄 has the χ direction). The second is the contribution of E: after integration by parts, ≍ ∫ x^{−3/2}|E(x)|dx
weighted by w′, w. For it to be O(1) uniformly on the window one needs E(x) = O(x^{1/2}·(log x)^{O(1)}) in weighted
average — and the SIGN of that residual, not just its size.

### 4.2 What zero-free methods give (PROVED/CITED)
- Chebyshev (x ≪ ψ(x) ≪ x, elementary): |E(x)| ≤ cx, residual ≍ X^{1/2}: wrong size by a factor X^{1/2} = e^T, no sign.
- PNT with classical zero-free region (dlVP, CITED): E(x) ≪ x·e^{−c√(log x)}: residual ≍ e^{T−c√(2T)} → ∞. Wrong size
  and no sign. (Consistent with the phase-151 record: "dlVP capped by archimedean density".)
- Any bound E(x) ≪ x^{θ+ε} translates, via the explicit formula, into information about the location of the zeros, and
  conversely (CITED, Landau/Ingham, classical form of the error ↔ zero-free-region correspondence). The scale required
  here is that of the window itself: it is zero-side data, in the very same form as Z_T.
- The identity of §1.2 (the comb on the window = the full comb) removes the "tail" from the objective: there is no tail
  to bound. The only place where the information lives is E(x) restricted to x ≤ e^{2T}, which is exactly the part of
  the comb that enters.
Conclusion: **there is no zero-free mechanism** in this reading. "Approximating m by the partial sum of the comb in the
low band" is the explicit formula written in frequency; its error is Z_T. NO-GO (PROVED as an identity; ARGUED as a
class: every method whose only arithmetic input is a bound on E(x) falls here).

### 4.3 Compatibility with LEDGER_L2
LEDGER_L2: "the archimedean nodes predict the sign of the large entries of the prime matrix; the arithmetic lies only
in the small entries." In (1.4): the large entries are those of the polar piece (x^{1/2}, the main term of ψ) and those
of m (nodes of the low-band prolates); the small ones are those of Z_T in the prolate basis. It is the same partition
seen from the explicit formula: the sign of the small entries is the sign of the zero-side form. Consistent (ARGUED).

## 5. Death criterion (applied)
- Was Weyl/norms used? No (the LCB lower bound is a direct construction; the upper bound is rank one).
- Hellmann–Feynman on the second eigenvector? No.
- Continuation in T? No (monotonicity of n₋ is used only as an already-proved datum, not for the conclusion).
- But the exact mechanism found (explicit formula on the even sector) reduces H1⁺ ∀T to W^ev ⪰ 0 ∀T: REF-D by P4.
  **By the objective's own rule ("if H1⁺ ≡ positivity of the truncated zero-side form modulo the pole: NO-GO"): NO-GO.**

## 6. Verdict

- (1.4) 𝔄_ev = Z_T − 2χχᵀ with Z_T = W^ev_T = zero-side form: **PROVED** (lem:roughEF, even sector; no boundary term).
- (2.1) sandwich n₋(Z_T) ≤ n₋(𝔄_ev) ≤ n₋(Z_T)+1; (2.2) n₋(𝔄_ev) ≤ 1 + N_hip; hyperbolic pair (1,1) per quadruple: **PROVED**.
- CALIB's "1" = polar direction; Epstein's "2" = pole + hyperbolic pair: **NUMERICAL, consistent**.
- Lemma LCB and the direction H1⁺ ⇒ D^ev: **ARGUED**.
- Proposition H: H1⁺ ∀T ≡ D^ev: **⇐ PROVED, ⇒ ARGUED**.
- Zero-free mechanism in frequency: **NO-GO** (Chebyshev/dlVP: size e^{T}·, no sign; bound on E = zero-side data).
- **H1⁺ as an independent route: NO-GO (REF-D by P4).** Label of the H1⁺ statement: OPEN (it is D^ev).

## 7. OPEN with name
- **LCB** (boundary concentration): write out (b)–(c) of §2.3 with constants ⇒ Proposition H ⇒ PROVED. Closable without D.
- **PRED-aP**: prediction n₋(𝔄_ev^{a_P}(T)) ≥ 2 for moderate T (quadruples β = ½ on Re s = 0); verifiable on the
  CALIB_R4 / rem:polarcapdiag pipeline (NUMERICAL, no new background code). If it fails, LCB is wrong and the
  classification reverts to "class (L2)".
- **Classification correction** in WT_HALVES/H1_TRACT: H1⁺ and H2 are not independent ∀T.

## 8. Entry for the index

- **H1PLUS_001 (phase 204t, H1⁺ by exact comb structure): NO-GO (REF-D by P4).** On the window the truncated comb
  = the full comb (c_F(log n) = 0, n ≥ e^{2T}); lem:roughEF on the even sector gives 𝔄_ev = Z_T − 2χχᵀ, Z_T = W^ev =
  Σ_ρΦ_F(ρ)², with no boundary term (killing = internal rewriting) — PROVED. Inertia: n₋(Z) ≤ n₋(𝔄_ev) ≤ n₋(Z)+1, each
  hyperbolic quadruple = pair (1,1) (PROVED); CALIB's "1" is the polar direction; Epstein n₋ = 2 at T = 2 = pole + pair.
  LCB (ARGUED) ⇒ H1⁺ ∀T ≡ D^ev; it is not a "half". Frequency: residual = E(x) at scale x^{1/2}, Chebyshev/dlVP give
  neither sign nor size. Do not retry inertia of 𝔄 "via the comb" without an object that bypasses (1.4). OPEN: LCB with
  constants; PRED-aP.
