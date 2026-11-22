# AUDIT_L_SHARP_1 — audit of the five proof attempts of Lemma L′♯ (A–E)

Pen and paper, plus one numerical check that was strictly necessary to decide a label
(§3: Slepian's derivative identity and the Connes–Consani kink value).

Sources checked against the memos: Paper 46 (eq:symbol, eq:form, eq:W, thm:A/eq:Aform, the "Dirichlet form with
killing" display in the proof after thm:A, def:PD, lem:roughEF, prop:archneg, prop:env, rem:moriceiling,
subsec:shape-geom thm:geo-tv and prop:geo-int); Guo (Zenodo 23297284) (2.4), (2.10), Lemmas 4.1–4.4, Thm 4.5,
Rem 4.6, (5.6); Connes–Consani 2006.13771 Def 4.4, Prop 4.5, Thm 4.7/(84), Lemma 5.4/(100); Mori VII §3
((3.1)–(3.4), Prop 3.1), Mori VIII §2 (margins); BARRIER_EST_001 Def 1 and Thm 4; AUDIT_199; MECH_001.

**Verdict in one line.** The five memos prove the same identity in three guises and reduce L′♯ to one inequality,
(★) = (L_ext) = (R_C) = (★E), which is OPEN. Two claimed theorems do not survive: D's Prop 2.3 size statement
("two e^{4πμ}-size terms cancel to e^{−4πμ}") is FALSE (the kink constant is polynomial), and C's Thm 6.1 (class
NO-GO for multiplier bounds) is NOT PROVED (the barrier does not transfer to the exterior carrier). E's correction
to A is right and harmless. Nothing here is a sign. Row D OPEN.

## 1. Consistency: A Thm 1.1 / C Prop 1.2 / E Thm E.1, and E's killing-term correction

**1.1 The three identities are one identity (PROVED).** With Φ_f(x) = e^{x/2}Σ_n f(ne^x), g = Φ_f|_I, Ψ = Φ_f|_{(−∞,−a)}
(f admissible, real, f(λ) = 0):
- A: W_T(g) = ∫Ψ̄·WΨ, W the full Weil distribution of Guo (4.7). Checked term by term: for x ∈ I,
  (WΨ)(x) = −(X_∞+X_≤+X_>+X_Π)Ψ(x) with Guo's (4.8) (the b_∞Ψ(x) and Ψ(x+t), Ψ(x+log q) terms vanish on I; the sign of
  X_Π = −∫2cosh(·)ℓ matches), so Guo Thm 4.5 reads Ãg = −(WΨ)|_I and W_T(g) = ⟨g,Ãg⟩ = −𝒲(g,Ψ). With WΦ_f = 0
  (Guo Lemma 4.4) one has 𝒲(g,g) + 𝒲(g,Ψ) = 0 and 𝒲(Ψ,g) + 𝒲(Ψ,Ψ) = 0, hence 𝒲(g,g) = 𝒲(Ψ,Ψ) = −𝒲(g,Ψ) and the
  total 𝒲(Φ_f) = 0. The truncated comb q < μ of W_T equals the full comb on g because c_g(log q) = 0 for q ≥ μ.
  PROVED (A's proof is correct; the only step it cites without proof is Q_{Wλ} = W_T, AUDIT_ZENODO §0).
- C: W_T(g) = Σ_ρ Φ_ℓ(ρ)Φ_ℓ(1−ρ). Uses lem:roughEF on g: (a) holds because g has a single jump at −a (f(λ) = 0 kills
  the jumps at x_n), so |ĝ|² = O(τ^{−2}); (b) holds because Φ_g(ρ) = −Φ_ℓ(ρ) (ζ(ρ)f̃(ρ) = 0, f̃ holomorphic on Re s > −2)
  and Φ_ℓ(σ+it) = O(1/|t|). PROVED. That this zero sum equals 𝒲_ext[ℓ] is C's Rem 2.1(i) (contour shift through the
  zeros, principal value on the line): the explicit formula for a test with e^{3y/2}-decay at −∞. I label it
  CITED/ARGUED (Guo proves it only for Φ_f, via cut-off; C's shift is standard but not written with the indentation at
  the zeros on Re s = ½). Not decisive.
- E: 𝒲[Ψ̌] expanded over the lattice sum Ψ̌ = Σ_n n^{−1/2}S_{−log n}r_n. The indicator bookkeeping (r_n(x+log n) ≠ 0 iff
  x > a) is right; absolute convergence by r̃ = O(e^{−3x/2}). PROVED.
So A (arithmetic side, quadratic form of W on the tail), C (zero side, zero sum of the tail) and E (lattice expansion
of A) are the same number. They are consistent, and all three use the full form of the zero-extended tail.

**1.2 E's correction (PROVED, and A's displayed formula is wrong as a display).** The archimedean part of ∫Ψ̄WΨ for
Ψ extended by zero is (1/2π)∫Θ_∞|FΨ|² = b_∞‖Ψ‖² + ½∫∫_{ℝ²}|Ψ(x)−Ψ(x′)|²ν(x−x′)dxdx′ (ν = K/2 of Paper 46 lem:K; the
factor ½ is checked: ∫∫_{ℝ²}|Ψ(x)−Ψ(x−u)|²ν(u) = 2∫_0^∞ν(u)(2‖Ψ‖²−2Re C_Ψ(u))du = 2·[Plancherel of
2∫_0^∞(1−cos τu)ν(u)du]). Splitting ℝ² into (−∞,−a)² and the two strips on which one factor vanishes gives the
**killing term** ∫_{y<−a}|Ψ(y)|²κ_a(y)dy, κ_a(y) = ∫_{|y+a|}^∞ν(t)dt ≈ ½log(1/|y+a|) + O(1) (ν(t) ~ 1/(2t)), integrable
against |Ψ|² although Ψ jumps at −a (Ψ(−a−) = Φ_f(−a) = λ^{−1/2}Σ_n f(n/λ) ≠ 0 in general). This is exactly Paper 46's
"Dirichlet form with killing" (Lev = ¼∫∫_{I×I}K|F(x)−F(y)|² + ½∫_Iκ|F|² with K = 2ν) transported to the half-line.
A's display of 𝒲_ext (half-line double integral only) omits it; A's Theorem 1.1 is unaffected because its proof
uses ∫Ψ̄WΨ, never the display. **Consequences:** A Prop 2.1, Thm 3.1, (★), Lemma 4.1, Cor 4.3 unchanged (none uses the
display). A §5 "Bochner" NO-GO unchanged (the killing term is ≥ 0 and comb-independent). A §1 convergence remark
"Ψ Lipschitz gives the Lévy term" is incomplete; E §1 supplies the strip estimate. Label of A's display:
CORRECTED (E §1). Label of E §1: PROVED.

## 2. E's Thm E.2 (prime collapse) and the Λ-ingredient

**2.1 The collapse is PROVED.** For x > a, Ψ̌(x+log q) = Σ_l l^{−1/2}r̃(x+log(lq)); with c_q = Λ(q)q^{−1/2} one has
c_q l^{−1/2} = Λ(q)(lq)^{−1/2}, so Σ_q c_q⟨Ψ̌,Ψ̌(·+log q)⟩_{(a,∞)} = Σ_{m,n}(mn)^{−1/2}(Σ_{q|n}Λ(q))I_a(m,n) =
Σ_{m,n}(mn)^{−1/2}(log n)I_a(m,n) = ⟨Ψ̌,Ψ̌_log⟩. Absolute convergence: Σ_n n^{−1/2}log n·n^{−3/2} < ∞. The full-line prime
term is −Σ_q c_q∫Ψ̌(x)(Ψ̌(x−log q)+Ψ̌(x+log q)) = −2Σ_q c_q∫_{x>a}Ψ̌(x)Ψ̌(x+log q) (the two correlations coincide; E's
"S_{log q}" should read S_{−log q} in its own convention — notational only). The consistency check with the ratio
bookkeeping (Σ_{q: q/gcd(q,α′)|j}Λ(q) = log(jα′)) is right. **Essential hypothesis:** the comb is complete (all prime
powers q, not only q < μ), which holds in 𝒲_ext because the tail has unbounded support (Guo Rem 4.6(iii)). On the
window carrier the comb is truncated and the collapse does NOT hold — this is why E's statement is specific to the
exterior carrier.

**2.2 Reconciliation with C §5 and D Thm 4.1 (no contradiction).**
- C §5 (Props 5.1–5.2): the *identity* W_T(Ef) = 𝒲_ext[ℓ] requires the Weil distribution (archimedean kernel, pole,
  comb) to belong to the same L whose coefficients a_n drive the summation map. E's Rem 3.2 says: granted that, the comb
  Λ_D contracts against a_n (Σ_{ql=n}Λ_D(q)a_l = a_n log n, i.e. −D′ = (−D′/D)·D). Both are correct and complementary:
  C says which comb must sit in the exterior form (−D′/D of the same D), E says that once it sits there it disappears
  into (a_n). For ζ: a_n ≡ 1, Λ∗1 = log.
- D Thm 4.1 is about the *window* carrier, where the comb is linear and truncated and Λ ↦ cΛ is a different form; the
  Sonin trace is comb-blind there. E's collapse is on the exterior carrier where the comb is not a free parameter. No
  overlap, no conflict. (For cΛ with the adapted map E_c the exterior form is again "Λ-free" by Rem 3.2, but the Poisson
  step fails, A §6; so no exterior inequality is even stated for cΛ.)

**2.3 What the Λ-ingredient is (corrected label).** E's list (Λ-E) = {a_n ≡ 1 on ℕ, residue 1, Γ_ℝ with conductor 1,
lattice aliasing} is PROVED as a *sufficient list of inputs*: (★E) is written with Z, Z_log, Θ_∞, 2AB and the
Paley–Wiener class, nothing else. E's further sentence "Λ ≥ 0 on prime powers is not available: it has been consumed by
the collapse" is OVERSTATED and I retract it as a constraint on proofs: by E's own Rem 3.1, Z_log Z^{−1} = Σ_{N≥2}c_N
S_{log N} with c_N = Λ(N)N^{−1/2} ≥ 0 (μ∗log = Λ). The information "Λ ≥ 0" is not consumed; it is *encoded* as the
statement that the commutator defect [M_log,Z]Z^{−1} is a nonnegative combination of shifts, and a proof of (★E) may
re-expand and use it. Correct reading: Λ ≥ 0 is not needed as a separate axiom — it is a theorem about (ℕ,·) that the
form carries through a_n ≡ 1. Label: (Λ-E) PROVED as sufficient inputs; "Λ ≥ 0 not available" RETRACTED (replaced by
"Λ ≥ 0 is equivalent to c_N ≥ 0 in Rem 3.1 and remains usable").

**2.4 One more PROVED structural fact in E worth keeping.** For arbitrary r ∈ L²(λ,∞) with compact support, Möbius
makes Z surjective onto C_c(a,∞) and 𝒲 is translation invariant, so "𝒲_ext[Zr] ≥ 0 for all half-line r" is the
positivity of the complete Weil form on every compactly supported test — i.e. row D on all windows, restated. Hence
the Paley–Wiener constraint on r (r = (1−P_λ)f̂, f̂ entire of exponential type λ) is the entire additive input of
(★E). PROVED (E §5), and consistent with A §6 (Poisson is the additive-specific step).

## 3. D's Prop 2.3 (weight inversion): the size claim is FALSE

**3.1 The formula is right, the size is wrong.** CC Lemma 5.4: ε′(1⁺) = Σ_n λ(n)²ξ_n(1)²/(1−λ(n)²) (even prolates,
CC normalisation ∫_0^∞|ξ|² = 1, so ξ_n(1)² = 2ψ_n(1)² in the standard normalisation on [−1,1]). D reads the weights
1/(1−χ_n) = D_n^{−1} and concludes 2ε_λ′(1⁺) ≥ 2χ_0ψ_0(λ)²/(1−χ_0) ≍ μ^{O(1)}e^{4πμ}. This ignores the numerator:
the edge value of a concentrated prolate is itself exponentially small. By Slepian's derivative identity
(classical, CITED; verified here numerically to 10^{−8} at c = 2π with a 400-point Gauss–Legendre discretisation of
the sinc kernel, NUMÉRICO),
  dλ_n/dc = (2/c)λ_n ψ_n(c,1)²,   hence   λ_nψ_n(1)²/(1−λ_n) = −(c/2)(d/dc)log(1−λ_n(c)),
and in CC's normalisation
  **ε′(1⁺) = −c Σ_{n even} (d/dc) log(1−λ_n(c)).**
Check against CC's own numbers at c = 2π: this formula gives t(0) = 11.9719, t(1) = 8.7757, t(2) = 2.2053,
t(3) = 0.0434, t(4) = 0.000125, total 22.9965 — CC's values to all printed digits. Since 1−λ_n(c) ≈ K_n c^{n+½}e^{−2c}
for n ≪ 2c/π, each term is ≈ 2c − n − ½ (polynomial), terms with n ≫ 2c/π are negligible, and ε′(1⁺) = O(c²).
At the level λ = e^T (c = 2πμ, prolates rescaled to [−λ,λ], ψ_n^{(λ)}(λ)² = ψ_n(c,1)²/λ) the same identity gives
ε_λ′(1⁺) = −(c/λ)Σ_n(d/dc)log(1−λ_n) = O(c²/λ) = O(μ^{3/2}). **So the kink constant is polynomial in μ, not e^{4πμ}.**

**3.2 Consequences.** (i) D's sentence "the decomposition is a cancellation of two terms of size e^{4πμ} down to the
margin e^{−4πμ}" and gap (G4) as phrased are RETRACTED; the correct statement is that all pieces of Cor 2.2 are of
polynomial size (Son ≥ 0, 2ε′𝔅 = O(μ^{3/2})‖G‖², K_s Hilbert–Schmidt, ℭ ~ √μ, 𝔓 ~ √μ) and must cancel to e^{−4πμ} —
the same situation as the window form itself (B §2: pole and prime blocks both ~√μ). (ii) "The leakage enters with
the weights D_n^{−1}" is literally true but has no content: the numerator ψ_n(λ)² cancels D_n^{−1} exactly up to the
factor −c(d/dc)log(1−λ_n) ≈ 2c. (iii) Nothing in D's §2.1 Thm 2.1 depends on this (it is at level (1,1), where the
kink is the fixed number 2·22.9965). (iv) The conclusion "Son ≥ 0 + TV-robust remainder bound is excluded" SURVIVES,
but through Prop 3.1 (window carrier, comb-linear, B Lemma 4.1), not through any size argument: qualitatively PROVED
(radius ≤ λ^W_T), quantitatively CONDITIONAL on rem:moriceiling (μ ≥ 50) — see §4. (v) The new identity
ε′(1⁺) = −cΣ(d/dc)log(1−λ_n) is PROVED (given Slepian, CITED) and is recorded as an object; it says the CC kink is the
logarithmic c-derivative of the total leakage Π_n(1−λ_n(c)) of the even prolate system.

## 4. B Thm 4.2 and C Thm 6.1: are the NO-GO classes correctly derived?

**4.1 B Lemma 4.1 (barrier for the complete form and for (B_μ)): PROVED, one normalisation remark.** The form
⟨f,(M+V)f⟩ = ⟨f,(γ+V)f⟩ − ⟨f,C_νf⟩ is of the shape 𝒜 − ∫c_f dν with 𝒜 comb-independent, so the δ_{u_0} perturbation
applies. With Paper 46's convention (ν = Σv_nδ_{log n} on u > 0, thm:geo-tv) the radius bound is r ≤ (1+ε)λ_min, not
½(1+ε)λ_min; B's ½ comes from a symmetrised measure. Harmless (both ≪ any estimate slack); to be normalised as in
AUDIT_197_2.

**4.2 B Thm 4.2: PROVED qualitatively, CONDITIONAL quantitatively, overstated at "any μ ≥ 5".** The chain
r(μ) ≤ λ_min(M+V) ≤ λ^W_T − Cδ is correct (Cor 1.2(b) uses Mori Prop 3.1, CITED). The next step λ^W_T ≤ κ₊μ^{9/2}e^{−4πμ}
is rem:moriceiling: CITED, PLAUSIBLE-UNVERIFIED, uses zero data, and stated for 50 ≤ μ ≤ 10⁴ (and a weaker form for
μ ≥ 50). So Thm 4.2 is CONDITIONAL for μ ≥ 50. At μ = 10, 12, 15 B substitutes the *certified finite margins*
(λ_min of Mori's test matrix T_N: 2.4·10^{−70} etc.) for λ^W: those are not proved upper bounds on λ^W (T_N is a
Schur-complement test, not the form), and "S7 resolves λ^W itself" rests on the slope check — ARGUED/NUMÉRICO. At
μ = 5 the table uses λ^W ≥ 10^{−18}, a lower bound, as if it were the required precision. For 5 ≤ μ < 50 only the
qualitative statement r ≤ λ^W_T(μ) is PROVED, with λ^W_T(μ) unknown. The floor r_E ≥ 10^{−10}μ is ARGUED, as labelled.
Corrected label: **Thm 4.2 PROVED as "r(μ) ≤ λ^W_T − Cδ"; CONDITIONAL (rem:moriceiling) for the e^{−4πμ} scale at
μ ≥ 50; ARGUED at μ = 10, 12, 15; the phrase "at any μ ≥ 5" is RETRACTED.** The class NO-GO "uniformise S7 by
TV-robust premises" stands with those qualifiers.

**4.3 C Thm 6.1: NOT PROVED (the barrier does not transfer to the exterior carrier).** C's class is: proofs of (R_C)
in which the comb enters only through bounds on the multiplier D_a(s) on lines Re s = σ > 1. C's proof: such bounds
hold on a (weighted) TV-ball around Λ, B Lemma 4.1 gives a comb ν′ in the ball with W^{(ν′)}_T negative at the bottom
vector, so "𝒫 would prove the sign for a comb for which it is false". Two gaps:
(a) What 𝒫 proves for ν′ is (R_C)^{(ν′)}, the *exterior* inequality with comb ν′. By C's own Prop 5.1 the identity
  W^{(ν′)}_T(Ef) = 𝒲^{(ν′)}_ext[ℓ] FAILS for ν′ ≠ Λ (the defect is O(‖g‖²), not of tail size). So (R_C)^{(ν′)} says
  nothing about W^{(ν′)}_T, and no contradiction with λ^W(ν′) < 0 follows. C §6 itself states that (R_C) for cΛ "is a
  different, false, statement" — its falsity is asserted, not proved.
(b) The barrier that *would* apply on the exterior carrier is the δ_{u_0}-perturbation of 𝒲^{(ν)}_ext[ℓ] =
  𝒜(ℓ) − ∫C_ℓ dν, with margin measured relative to ‖ℓ‖², not ‖g‖². At the bottom vector, 𝒲_ext[ℓ★] = λ^W‖g★‖² while
  ‖ℓ★‖² ≍ μ^{O(1)}ℓ(g★) ≍ μ^{O(1)}e^{−4πμ}‖g★‖² (AUDIT_199 (e); ARGUED), so the perturbation needed to break
  (R_C)^{(ν′)} is m ≳ λ^W‖g★‖²/‖ℓ★‖² = μ^{O(1)} — polynomial, not doubly exponential. The exterior inequality has, by
  construction, a polynomial relative margin; that is the whole point of L′♯. There is therefore **no
  doubly-exponential TV barrier on the exterior carrier** (ARGUED), and Thm 6.1 cannot be rescued by (b).
(c) Moreover, after E Thm E.2 the comb is not a parameter of the exterior form at all: "multiplier bounds on D_a"
  presuppose re-expanding Λ, and any such bound is an identity + C–S argument, i.e. N_018, and comb-generic by A §6.
Corrected label: **Thm 6.1 RETRACTED as PROVED; the class "Mellin multiplier bounds + Paley–Wiener loss" is NO-GO
only as ARGUED (N_018 + comb-genericity), not by the barrier.** C's Prop 1.1, 1.2, Thm 2.1, Thm 3.1, Props 4.1–4.2,
Cor 4.3, Props 5.1–5.2 are PROVED as labelled (Thm 3.1's dilation argument is correct: Ef_a = 0 for a > μ; Prop 4.1's
constant ζ(3/2) < 3 ✓; Prop 4.2's r_ε example ✓, the density sentence ARGUED as labelled).

**4.4 D Prop 3.1 (window carrier): PROVED qualitatively (radius ≤ λ^W_T), CONDITIONAL quantitatively.** Same status as
B Thm 4.2; the decomposition of Cor 2.2 is comb-linear on the window carrier, so the barrier applies verbatim.

## 5. E's Thm E.5 (ratio classes indefinite): PROVED on C_c^∞(a,∞), ARGUED on the Paley–Wiener class

Q_{1/1}(r̃) = Σ_j j^{−1}[𝒜_a[r_j] + 2A(r_j)B(r_j)] − 2∫r̃(y)²H₁(e^{y−a})dy with r_j = r̃·1_{(a+log j,∞)}: the first sum
is the archimedean + pole self-pairing of the pairs (j,j) (translation invariant, so each full term equals c_φ for
j ≤ e^D), the second is the prime part of the effective-shift-0 class in E.2's bookkeeping (G_{11} = 2H₁). With
r̃ = φ(·−a−D), φ ≥ 0 a unit bump of width 1: first sum = H(e^D)c_φ + O(1) = Dc_φ + O(1) (the O(1) is the finite Lévy
energy of the ≤ e^{D+1}−e^D truncated bumps, each with one jump, ν ~ 1/(2t) integrable against a jump: ✓); prime part
= −2∫φ²H₁(e^{D+s})ds = −D² + O(D) (H₁(X) = Σ_{j≤X}(log j)/j = ½log²X + γ₁ + O(log X/X) ✓). Hence Q_{1/1} < 0 for D
large: **H ~ log X versus G ~ log²X is correct**, and the linear-vs-quadratic depth comparison is PROVED. For
(α,β) ≠ (1,1) the same works with a bump of width > |log(β/α)| and φ ≥ 0 (positive overlap), as E says. Two caveats:
(i) the data in the proof are arbitrary deep bumps in C_c^∞(a,∞), not aliasing tails of admissible f; on the
Paley–Wiener class the no-SOS statement is ARGUED (approximation of a deep bump by (1−P_λ)f̂ is plausible but not
written); (ii) the ratio-class decomposition depends on E.2's effective-shift bookkeeping (E.1′ alone groups the prime
δ's differently), which E states. Labels: Thm E.5 PROVED (as stated, on C_c^∞); "no SOS over ratios on the data class"
ARGUED. NO-GO for classwise SOS stands.

## 6. Verdict: what is PROVED, and the one remaining inequality

**6.1 PROVED (surviving audit).** A: Thm 1.1 (half-line identity), Prop 2.1 (gauge = radical, ℓ = dist²), Thm 3.1
((L_ext) ⟺ L′♯), §3.2 Mellin truncation structure, Rem 3.3 (symbol identity, checked from ξ(s) = ξ(1−s)), Lemma 4.1,
Lemma 4.2 (ℓ(g) ≤ 4μ(1+4μc_B)‖g‖², checked), Cor 4.3 (trivial: the subspace 𝒯_* is where g sits at frequency
> e^{𝒜_T+λ}), §6 table. B: Lemma 1.1, Cor 1.2, Lemma 3.1 (checked: ψ(z)+1/z = ψ(z+1), F(e^{−|a|/2}) = (¼+t²)^{−1}),
Lemma 3.2, Prop 3.3, Prop 3.4 (identity), Lemma 4.1 (normalisation ½ → 1 in Paper 46's convention). C: Props 1.1–1.2,
Thm 2.1, Thm 3.1, Props 4.1–4.2, Cor 4.3, Props 5.1–5.2. D: Thm 2.1 (level (1,1), given CC Thm 4.7), Cor 2.2, the
formula of Prop 2.3 (not its size), "𝔐 ≠ function of W_λ", Prop 3.1 (qualitative), Thm 4.1, Cor 4.2 (given the
R186_014 structure, CITED). E: §1 correction, Thm E.1, E.1′, E.2, Cor E.3, Rems 3.1–3.2, Lemma E.4, Thm E.5 (on
C_c^∞), the "arbitrary r" remark, (Λ-E) as sufficient inputs.

**6.2 CONDITIONAL / ARGUED / RETRACTED.** B Thm 4.2 and D Prop 3.1 at the e^{−4πμ} scale: CONDITIONAL on
rem:moriceiling (μ ≥ 50), ARGUED at μ = 10, 12, 15; "any μ ≥ 5" RETRACTED. D Prop 2.3 "≍ e^{4πμ}" and gap (G4):
RETRACTED (polynomial kink, §3). C Thm 6.1: RETRACTED as PROVED, NO-GO class only ARGUED (§4.3). E "Λ ≥ 0 not
available": RETRACTED (§2.3). C Rem 2.1(i) (explicit formula for the tail by contour shift): CITED/ARGUED. E Thm E.5
on the Paley–Wiener class: ARGUED. A §4.4 dimension N_*: ARGUED.

**6.3 The remaining inequality — one statement, four spellings (PROVED equivalent, OPEN).** (★) [A, prolate matrix],
(L_ext) [A], (R_C) [C], (★E) [E] are the same statement with the same (κ,A): A Thm 3.1 gives L′♯ ⟺ (L_ext) (real
case; complex with κ/2); (★) is (L_ext) in the prolate basis; (R_C) is (L_ext) with 𝒲_ext written by Thm 2.1; (★E) is
(L_ext) with 𝒲_ext written by Cor E.3. The reduction to f(λ) = 0 is legitimate (g in the core vanishes at ±T, so
f(λ) = g(T−)λ^{−1/2} = 0). Not equivalent: (R_X) of C Cor 4.3 (X-norm, strictly stronger, sufficient) and B's
L_x(Ω)/(B_μ) (Mori's test; a different and stronger statement than λ^W > 0, related to L′♯ only by the ARGUED
comparison of B §5).

**Consolidated formulation (★★).** Fix μ ≥ 5, λ = √μ, a = ½log μ. Data: real r ∈ L²(λ,∞) of the form r = f̂|_{(λ,∞)}
with f even, C², supp f ⊂ [−λ,λ], f(0) = f̂(0) = f(λ) = 0 (Paley–Wiener: r is the restriction of an entire function of
exponential type λ, r = O(ξ^{−2})). Radical: 𝒢̄ = closure in L²(λ,∞) of {(1−P_λ)φ̂ : φ even C², supp φ ⊂ [−1/λ,1/λ],
φ(0) = φ̂(0) = 0}. Maps on (λ,∞): (Zr)(w) = w^{1/2}Σ_{n≥1}r(nw), (Z_log r)(w) = w^{1/2}Σ_{n≥2}(log n)r(nw);
Ψ̌(x) := (Zr)(e^x) for x > a, 0 for x ≤ a; A = ∫Ψ̌e^{−x/2}, B = ∫Ψ̌e^{x/2}. Archimedean form of the zero-extended
Ψ̌ (with killing): 𝒜[Ψ̌] = (1/2π)∫Θ_∞|FΨ̌|² = b_∞‖Ψ̌‖² + ½∫∫_{ℝ²}|Ψ̌(x)−Ψ̌(x′)|²ν(x−x′)dxdx′. Then L′♯ ⟺
  **(★★)  𝒜[Ψ̌] + 2AB − 2⟨Ψ̌, Z_log r(e^{·})⟩_{L²(a,∞)} ≥ κ μ^{−A} · dist²_{L²(λ,∞)}(r, 𝒢̄)**
for some κ > 0, A ≥ 0 and all μ ≥ 5 and all such r; equivalently (Lemma E.4)
(1/2π)∫ã|FΨ̌|² − R_Λ(Ψ̌) ≥ κμ^{−A}dist²(r,𝒢̄), ã(τ) = Re ψ(5/4+iτ/2) − log π, R_Λ(Ψ̌) = 2⟨Ψ̌,Ψ̌_log⟩ − 2∫_0^∞e^{u/2}C_Ψ̌(u)du.
The left side equals W_T(Ef) (A Thm 1.1 + E Cor E.3) and Σ_ρΦ_ℓ(ρ)Φ_ℓ(1−ρ) (C Prop 1.2). OPEN.

**Every known constraint on a proof of (★★).**
1. *Not TV-robust on the window carrier:* any comb premise about W_T must have TV-slack ≤ λ^W_T (PROVED, B Lemma 4.1 /
   thm:geo-tv; ≤ κ₊μ^{9/2}e^{−4πμ} CONDITIONAL on rem:moriceiling for μ ≥ 50). On the exterior carrier the comb is not a
   parameter (E.2) and the relative margin is polynomial (§4.3(b)); the barrier gives nothing there, but neither does
   any re-expansion of Λ (constraint 2).
2. *Not an identity + Bochner/Cauchy–Schwarz/Schur argument* (N_018): every identity in A–E (half-line identity, Möbius,
   Λ∗1 = log, pole–Chebyshev cancellation, Sonin decomposition) is multiplicative-generic or additive-generic and
   survives cΛ, a_P, Beurling, F-DH (A §6, E §6, D Thm 4.1).
3. *Not symbolic:* the on-line symbol of the full Weil distribution vanishes off the zeros (A Rem 3.3); there is no
   diagonal weight in the Mellin variable (C Thm 3.1); the off-line pairing Φ_ℓ(s)Φ_ℓ(1−s) is not a square (C Rem
   2.1(ii)); all of (★★) is the truncation defect at ξ = nλ (n ≈ λ/u), where Σ_n n^{s−1}R_{nλ}(s) differs from
   ζ(1−s)R_λ(s) (A §3.2, E §4(c)).
4. *Not multiplier bounds* (C, ARGUED via 2–3), *not classwise SOS over ratios* (E Thm E.5), *not Bochner on the Lévy
   part + C–S* (A §5), *not "Son ≥ 0 + remainder bound"* (D Prop 3.1), *not a uniformised certificate* (B Thm 4.2).
5. *Must use, together, at the boundary n ≈ λ/u:* a_n ≡ 1 on all of ℕ (Möbius inverse of Z; equivalently c_N =
   Λ(N)N^{−1/2} ≥ 0 in Z_log Z^{−1} = Σc_N S_{log N}); residue 1 (2AB cancels ∫e^{u/2}C exactly, E.4 — the only step that
   fails for cΛ, a_P, Beurling by residue and for F-DH by absence of the pole); Γ_ℝ with conductor 1 (Θ_∞ matched to the
   lattice band λ); lattice aliasing (r Paley–Wiener of type λ — without it (★★) with κ = 0 is row D on all windows,
   E §5). Must fail for cΛ (c > 1, certified), a_P (certified), Beurling (NUMÉRICO), F-DH (Ziad, UNVERIFIED).
6. *Scale:* the upper side is linear in the leakage amplitude (Guo Thm 1.6, square-root gap), so the quadratic RHS
   μ^{−A}·dist² is the only shape compatible with both sides, and κμ^{−A}(1−χ_k) is forced at the bottom (AUDIT_199 (e)).
   The remaining finite block has superpolynomial dimension (A §4.4, ARGUED) and contains the whole prolate tail
   k ≥ 4μ; nothing comb-generic covers it.
7. *Where the semiring sits:* the pairs (m,n) = (jα,jβ) beyond the window, Weil kernel at log(β/α) (·), harmonic cut
   H(min(ξ/αλ,η/βλ)) (+), with depth weights H ~ log X (archimedean/pole) against G ~ log²X (prime) that must cancel
   *across* ratio classes (E §5). Any proof must produce this cross-class cancellation; no single class carries it.

**6.4 What to record / not retry.** Do not retry: Bochner/Lévy + C–S on 𝒲_ext; Mellin multiplier bounds; classwise
SOS over ratios; Son ≥ 0 + remainder; uniformised Mori certificates; "Λ ≥ 0 inside the exterior form" as a *separate*
axiom (it is c_N ≥ 0 of Rem 3.1, usable but not decisive by itself). Objects for REF-D: (★★) with the constraint list
above; the identity ε′(1⁺) = −cΣ(d/dc)log(1−λ_n(c)) (§3); the observation that the exterior carrier has no
doubly-exponential TV barrier (§4.3(b), ARGUED). No sign is claimed. Row D OPEN.
