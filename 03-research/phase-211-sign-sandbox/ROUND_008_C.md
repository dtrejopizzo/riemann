# Round 8 C: the one-sided variation of λ_A in the window variable, its two brackets, and what a Grönwall inequality in T contains

Object: λ_A(T) = inf{a_T(F) : F ∈ P_T, ‖F‖ = 1} (STATEMENT_001 §1). Target (★): λ_A(T) ≥ 0 for every T. Labels:
PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. No equivalence of (★) with any other statement is
used, named or invoked. Inputs: Paper 47 lem:monoT (monotonicity across contacts), lem:contA (continuity), lem:firstcontact
(first-contact reduction and the weak equation eq:localweak with a Tate multiplier), lem:compact (compact resolvent);
ROUND_007_B §2, ROUND_007_D (rate-2 law, λ_A^ev = μ₁ to five digits); tools/galerkin_mp.py.

## 0. Corpus check

Searched: ROUTES-TRIED-INDEX README (PROOF_L_SHARP_H_001 at the entry "strategy H", PROOF_L_SHARP_KK_001, restriction 11,
class 𝒦_H), 04_PHASES_100-189 (R186-S2seeds, R186-PNTcone, R186-D_B, R186-bilateral); phase 186 R186_038 (Lemmas α.1–α.4),
R186_111 (audit of R186_038), R186_004 (§2 "Grönwall … the same problem with one fewer scalar", "Hadamard formula OPEN");
phase 165 R165_202 (1.4 virial derivative, 1.5 formal Hadamard principle); index grep "Grönwall", "Danskin", "Hadamard",
"edge strip", "virial".

What is recorded.
- R186-S2seeds / R186_038 α.3 (NO-GO, "vacuous"): Grönwall in T at the minimiser: λ_A′ ≥ −cλ_A ⟺ 𝒱_T(h*_T) ≤ Tc(T)λ_A(T),
  c superexponential; the audit R186_111 §3.1 relabels it CONDITIONAL because the passage to the integrated bound needs λ_A
  absolutely continuous, which is not in the record. **This is the same differential inequality in the window variable T
  that the present task asks about.** It is not retried as a route; it is re-examined only for the two technical gaps the
  audit left (absolute continuity; non-simple bottoms) and for the size of its constant, which the record never measured.
- PROOF_L_SHARP_H_001 (class 𝒦_H, NO-GO ARGUED, restriction 11): Grönwall in the frequency variable c = 2πμ, μ = e^{2T}, on
  the complete form W_T in the dilated frame (window fixed, band edge moving), for the bundle 𝔐 − κμ^{−A}D with Slepian
  rate 2 in c; identity dN/dT = −2(band-edge alias)(odd Weil pairing); closes ⟺ a virial bound of relative precision O(1/c)
  at the minimiser.
- R165_202 1.4 (PROVED under (REG)): D⁺λ ≤ −𝒱_T(F_T)/T ≤ D₋λ for the single minimiser; 1.5 (ARGUED): 𝒱 = 0 if the dilation
  generator keeps F_T in the form domain. R186_004: Hadamard formula OPEN (edge singularity).

How a differential inequality in T differs from the frequency-variable one of H_001, and how it does not.
(i) Object: here the primitive form a_T on P_T with its two Tate multipliers, not the complete form W_T with its polar
term; the window moves and the frequency band is not cut. (ii) Variable: with c = 2πe^{2T}, dc/dT = 2c, so a rate C_c in c is
the rate C_T = 2c·C_c in T. The law of ROUND_007_D, −log λ_A = 4πe^{2T} + O(T), has C_T = 8πe^{2T}(1 + o(1)) = 4c, i.e. C_c = 2:
**the constant 2 in c of H_001 (Slepian rate) and the constant 8πe^{2T} in T are the same number under the change of
variable.** So in content the two inequalities are the same statement on two different (sandwiching, ROUND_007_D Prop. 4.1)
bottoms; H_001's NO-GO class 𝒦_H ("differential inequalities in T or c with coefficients evaluated at the minimiser")
covers the T-form. (iii) What is new below and is not in the record: (a) an exact, regularity-free inequality in the
opposite direction to the virial one (Proposition 3: the decrement λ_A(T) − λ_A(T+h) is bounded by the edge-strip energy of
the minimiser at T+h, Tate repair included) — this is the "Hadamard direction" that R186_004 lists as OPEN, in an
integrated, not differential, form; (b) a discrete Grönwall lemma (Proposition 4) that needs no absolute continuity,
closing the gap of R186_111 §3.1; (c) the eigenspace (Danskin) form for non-simple bottoms, with the Tate multipliers
written out (Theorem 1); (d) the first multiprecision measurement of the derivative and of the cancellation inside the
virial (§5). None of (a)–(d) is a sign mechanism, and the memo does not claim one.

## 1. Notation

U_r F(t) = r^{−1/2}F(t/r) (r > 0): unitary L²(I_T) → L²(I_{rT}); F̂ ↦ r^{1/2}F̂(r·), c_{U_rF}(u) = c_F(u/r). 
For T fixed, E_T is the bottom eigenspace of a_T on P_T (finite-dimensional, lem:compact; both parities allowed). For
F ∈ E_T there is a unique ρ_F in the Tate space 𝒯_T = span{e^{t/2}, e^{−t/2}}|_{I_T} with
  a_T(F, X) = λ_A(T)⟨F, X⟩ + ⟨ρ_F, X⟩  for every X in the form domain of L²(I_T)            (1.1)
(PROVED: for X ∈ P_T this is the Euler–Lagrange equation; for X ∈ 𝒯_T, which lies in the form domain since an exponential
with two jumps is in H^s for s < ½, define ρ_F by Riesz on the two-dimensional space 𝒯_T: ⟨ρ_F, X⟩ := a_T(F, X), using
F ⊥ 𝒯_T; this is eq:localweak of Paper 47.) ρ_F is linear in F.
Tate first moments: A₁(F) = ∫ F(t)(t/2)e^{t/2}dt, B₁(F) = −∫ F(t)(t/2)e^{−t/2}dt. Dual Tate basis p_A, p_B ∈ 𝒯_T:
A(p_A) = B(p_B) = 1, A(p_B) = B(p_A) = 0. Contacts: N_T = {n ≥ 2 : Λ(n) ≠ 0, log n < 2T}.
Virial (archimedean): 𝒱_∞(F) = (1/2π)∫ τ m′(τ)|F̂(τ)|² dτ.

Lemma 1.2 (PROVED). m′(τ) ≥ 0 for τ ≥ 0, and M₁ := sup|τm′(τ)| < ∞, M₂ := sup|τ(τm′)′(τ)| < ∞. Hence 0 ≤ 𝒱_∞(F) ≤ M₁‖F‖².
Proof. Re ψ(x + iy) − ψ(x) = Σ_{k≥0} y²/((k+x)((k+x)² + y²)) (from ψ(z) = −γ + Σ(1/(k+1) − 1/(k+z))), increasing in y² for
x > 0; take x = ¼, y = τ/2. τm′ and τ(τm′)′ are bounded because ψ′(z) = 1/z + O(1/z²) and ψ″(z) = O(1/z²) on Re z = ¼. ∎

## 2. The dilation bracket: a one-sided variation formula with Tate multipliers (Theorem 1)

Hypothesis (R_F) for a real F ∈ P_T: c_F is differentiable at every log n, n ∈ N_T, and, if 2T = log n₀ for a prime power n₀
(T a contact threshold), F has one-sided limits F(T⁻), F(−T⁺). (Under the latter, c_F(2T − ε) = εF(T⁻)F(−T⁺) + o(ε),
R186_038 α.2, so c_F′(2T⁻) = −F(T⁻)F(−T⁺).) (R_E) means (R_F) for every F ∈ E_T. Neither is known for the true minimiser
(R186_036 §4: the form domain is H^{log}, without boundary trace); both are statements about finitely many points.

Definitions (F real, unit, in P_T):
  𝒱(F) := 𝒱_∞(F) − Σ_{n∈N_T} v_n log n · c_F′(log n)                         (dilation virial; = R165_202 (1.4) without Tate term)
  τ(F) := 2[A₁(F)·a_T(F, p_A) + B₁(F)·a_T(F, p_B)]                          (Tate virial: first moments × multipliers)
  𝒱^♯(F) := 𝒱(F) + τ(F),   φ(F) := 2v_{n₀}F(T⁻)F(−T⁺) if 2T = log n₀, φ := 0 otherwise   (entry fold).
For F ∈ E_T, a_T(F, p_A) = ⟨ρ_F, p_A⟩ and a_T(F, p_B) = ⟨ρ_F, p_B⟩ by (1.1): τ is "first Tate moment times Lagrange
multiplier". All four are quadratic forms in F on E_T (ρ_F is linear in F).

**Theorem 1 (one-sided variation; PROVED under (R_E), the equality part CONDITIONAL on (U)).** Let T > 0.
(a) For every unit F ∈ E_T satisfying (R_F), as h → 0 (either sign),
    λ_A(T + h) ≤ λ_A(T) − (h/T)·𝒱^♯(F) − h⁺·φ(F) + o(h),   h⁺ = max(h, 0).                       (2.1)
(b) Hence, with S(E_T) the unit sphere of E_T,
    D⁺λ_A(T) ≤ −max_{F∈S(E_T)} [𝒱^♯(F)/T + φ(F)],      D₋λ_A(T) ≥ −min_{F∈S(E_T)} 𝒱^♯(F)/T,
and 𝒱^♯ ≥ 0 on E_T (Corollary 2.2).
(c) (Danskin.) Assume (U): for every sequence T_k → T and unit minimisers F_k ∈ E_{T_k}, the expansion (2.1), written at T_k
with h = T − T_k, holds with o(h) uniform in k, and 𝒱^♯, φ are continuous along every subsequence F_k → F ∈ E_T. Then
    λ_A′(T⁺) = −max_{S(E_T)} [𝒱^♯/T + φ],      λ_A′(T⁻) = −min_{S(E_T)} 𝒱^♯/T.
In particular λ_A is differentiable at T iff 𝒱^♯ is constant on S(E_T) and φ ≡ 0 there; if dim E_T ≥ 2 and 𝒱^♯|_{E_T}
is not scalar, λ_A has a concave corner at T (λ′(T⁺) < λ′(T⁻)).

Proof. Write r = 1 + s, s = h/T, and let F ∈ E_T be real (E_T is invariant under conjugation; a complex eigenvector is a
combination of two real ones and the forms are real), unit, with (R_F).
Step 1 (archimedean, uniform on L²). Arch(U_rF) = (1/2π)∫ m(τ/r)|F̂(τ)|²dτ. With g(σ) = m(τe^{−σ}): g′(σ) = −(xm′)(x),
g″(σ) = x(xm′)′(x), x = τe^{−σ}. Lemma 1.2 gives |m(τ/r) − m(τ) + (log r)τm′(τ)| ≤ ½M₂(log r)², hence
Arch(U_rF) = Arch(F) − (log r)𝒱_∞(F) + O(s²)‖F‖², uniformly in F.
Step 2 (comb). Π_{rT}(U_rF) = Σ_{Λ(n)≠0} v_n c_F(log n/r) (c_F vanishes on |u| ≥ 2T, so the sum over N_{rT} may be
replaced by the sum over all prime powers). For |s| small only n with log n ≤ 2T contribute: if log n > 2T then
log n/r > 2T. For n ∈ N_T, c_F(log n/r) = c_F(log n) − s log n·c_F′(log n) + o(s) by (R_F). For 2T = log n₀: if s < 0 the
argument exceeds 2T and the term is 0; if s > 0, c_F(2T/r) = 2Ts·F(T⁻)F(−T⁺) + o(s). So
Π_{rT}(U_rF) = Π_T(F) − sΣ_{N_T} v_n log n c_F′(log n) + s⁺·2T v_{n₀}F(T⁻)F(−T⁺) + o(s), and with Step 1 (log r = s + O(s²))
    a_{rT}(U_rF) = λ − s𝒱(F) − s⁺·Tφ(F) + o(s).
Step 3 (Tate repair). For F ∈ P_T, A(U_rF) = r^{1/2}∫F(t)(e^{rt/2} − e^{t/2})dt = sA₁(F) + O(s²) and B(U_rF) = sB₁(F) + O(s²)
(Taylor on the compact I_T). Let p_A^{(rT)}, p_B^{(rT)} be the dual Tate basis on I_{rT} and W_r := U_rF − A(U_rF)p_A^{(rT)} −
B(U_rF)p_B^{(rT)} ∈ P_{rT}. U_r^{−1}p_A^{(rT)} → p_A^{(T)} in the form norm of a_T (exponentials e^{±rt/2} restricted to I_T, whose
difference from r = 1 is O(s) in sup norm and in jump size), so by Step 1 of the proof of lem:contA,
a_{rT}(U_rF, p_A^{(rT)}) = a_T(F, p_A) + o(1), and likewise for B; also ⟨U_rF, p_A^{(rT)}⟩ → ⟨F, p_A⟩ = 0. Expanding,
    a_{rT}(W_r) = a_{rT}(U_rF) − sτ(F) + o(s),     ‖W_r‖² = 1 + o(s).
Hence λ_A(rT) ≤ a_{rT}(W_r)/‖W_r‖² = λ − s𝒱^♯(F) − s⁺Tφ(F) + o(s), which is (2.1) with s = h/T.
(b) Take h ↓ 0 in (2.1) for each F: D⁺λ ≤ −𝒱^♯(F)/T − φ(F); take the infimum of the right side over S(E_T) (a compact set,
dim E_T < ∞, lem:compact). Take h ↑ 0: (λ(T) − λ(T − |h|))/|h| ≥ −𝒱^♯(F)/T + o(1), for every F; take the maximum of the
right side.
(c) Apply (2.1) at T_k with the repaired dilate of F_k, U_{T/T_k}: λ(T) ≤ λ(T_k) + ((T_k − T)/T_k)𝒱^♯(F_k) + [fold] + o(|T − T_k|)
uniformly. For T_k ↓ T this gives (λ(T) − λ(T_k))/(T_k − T) ≤ 𝒱^♯(F_k)/T_k + o(1); by lem:contA and compactness (the proof of
lem:contA, Step 4–5, shows minimisers at T_k are near-minimisers at T after dilation, hence precompact in L² by the compact
resolvent) a subsequence F_k → F ∈ S(E_T), so the lower right Dini derivative is ≥ −max 𝒱^♯/T − max φ; with (b), equality.
The left side is symmetric (no fold, since the left dilation never meets an entering contact). The corner statement is the
inequality max > min of a non-scalar quadratic form on a sphere. ∎

**Corollary 2.2 (PROVED under (R_E)).** 𝒱^♯(F) ≥ 0 for every F ∈ E_T; and if T is a contact threshold and F ∈ E_T is even
with F(T⁻) ≠ 0, the fold φ(F) = 2v_{n₀}F(T⁻)² > 0 (cost), for F odd φ(F) = −2v_{n₀}F(T⁻)² < 0 (payment).
Proof. λ_A is non-increasing (lem:monoT), so the upper left Dini derivative is ≤ 0 and therefore D₋λ ≤ 0; by (b),
−𝒱^♯(F)/T ≤ D₋λ ≤ 0. The fold: F(−T⁺) = ±F(T⁻) by parity. ∎

**Proposition 2.3 (the two frames for an entering contact; PROVED).** (i) Zero-extension frame: for F ∈ P_T extended by zero
and every h ≥ 0, a_{T+h}(F) = a_T(F) exactly; the contacts n with 2T ≤ log n < 2T + 2h contribute 0 to all orders (lem:monoT),
and this frame yields only D⁺λ_A ≤ 0. (ii) Dilation frame: an entering contact contributes at first order exactly the fold
−h·φ(F), which is 0 iff F(T⁻)F(−T⁺) = 0. (iii) In the truncation frame of §3 there is no contact term at all: an entering
contact acts on λ_A only through the minimiser at T + h, i.e. through its edge strip.
Proof. (i) is the proof of lem:monoT; (ii) is Step 2 above; (iii) is (3.1) below, which involves only a_{T+h}. ∎

Reading. "Entering contacts contribute 0 at first order" is true in frame (i) and in frame (iii), and false in frame (ii)
unless the edge product vanishes. The three frames are compatible: the fold of (ii) is paid in (iii) by the edge-strip
energy. In the even sector (the bottom sector at every resolved window, ROUND_007_D §1(c)) an entry can only steepen the
descent (Cor. 2.2), as R186_038 α.2 already says for simple bottoms.

## 3. The truncation bracket: an exact, regularity-free bound of the decrement by the edge-strip energy (Proposition 3)

Fix T and h > 0, T′ = T + h, λ′ = λ_A(T′). Let F be a real unit minimiser at T′ (exists, lem:compact) with multiplier ρ ∈ 𝒯_{T′}
as in (1.1). Split F = G + R, R := F·1_{T≤|t|<T′} (the two edge strips of width h), G := F·1_{I_T}. Let q ∈ 𝒯_T be the unique
element with A(q) = A(R), B(q) = B(R) (Tate repair on the smaller window), and G♯ := G + q.

**Proposition 3 (PROVED; no regularity of F, no simplicity).** G♯ ∈ P_T, and
    (λ_A(T) − λ_A(T + h))·‖G♯‖² ≤ 𝔈_h,                                                               (3.1)
    𝔈_h := (a_{T′} − λ′)(R) − 2⟨ρ, R⟩ + [ 2⟨ρ, q⟩ − 2a_{T′}(R, q) + (a_T − λ′)(q) ],
with ‖G♯‖² = 1 − ‖R‖² + 2⟨G, q⟩ + ‖q‖², ‖q‖ ≤ γ_T(|A(R)| + |B(R)|) ≤ 2γ_T e^{T′/2}(2h)^{1/2}‖R‖ (γ_T = norm of the inverse
Tate Gram map on I_T). The bracket is the Tate repair; it is quadratic in (R, q) and O(h^{1/2}‖R‖·(1 + ‖R‖_{form})).
Proof. A(G♯) = A(F) − A(R) + A(q) = 0, likewise B. Since G and q are supported in I_T, a_T(G) = a_{T′}(G), a_T(G, q) = a_{T′}(G, q),
a_T(q) = a_{T′}(q) (zero extension; contacts with 2T ≤ log n < 2T′ see autocorrelations that vanish, lem:monoT). By (1.1) at T′,
a_{T′}(F, X) = λ′⟨F, X⟩ + ⟨ρ, X⟩ for every X in the form domain; R and q are admissible (R = F·indicator of two intervals is
in the form domain because the form is ≥ the Lévy form minus bounded terms and the Lévy energy of a restriction is bounded by
that of F plus the killing term ∫|F|²(∫_{ℝ∖J}K), which is finite for F in the form domain of a_{T′} on I_{T′}: the killing
weight of the strip boundary at ±T is dominated by the double-integral energy of F across ±T; this is the standard
restriction property of Lévy forms with kernel ≍ 1/u, which in the log-order case holds with a log loss that is integrable
— ARGUED here, PROVED for F with a_{T′}-finite energy across ±T, which is the case for every F with F ∈ L^∞ near ±T).
Then a(G) = a(F) − 2a(F, R) + a(R) = λ′ − 2λ′‖R‖² − 2⟨ρ, R⟩ + a(R), and a(G, q) = a(F, q) − a(R, q) = λ′⟨G, q⟩ + ⟨ρ, q⟩ − a(R, q)
(⟨F, q⟩ = ⟨G, q⟩). Therefore
  a_T(G♯) = λ′ − 2λ′‖R‖² − 2⟨ρ, R⟩ + a(R) + 2λ′⟨G, q⟩ + 2⟨ρ, q⟩ − 2a(R, q) + a(q).
Subtract λ′‖G♯‖² = λ′(1 − ‖R‖² + 2⟨G, q⟩ + ‖q‖²) and use λ_A(T)‖G♯‖² ≤ a_T(G♯). The norm bound for q: |A(R)| ≤ e^{T′/2}‖R‖_{L¹}
and ‖R‖_{L¹} ≤ (2h)^{1/2}‖R‖. ∎
(Label precision: (3.1) is PROVED for every T at which the minimiser F at T′ is bounded near ±T; for a general form-domain F
the admissibility of R as a test vector is the restriction property flagged above, ARGUED. Nothing below depends on more.)

**Corollary 3.1 (the derivative is squeezed between a virial and an edge budget; PROVED under (R_E) and the hypothesis of
Proposition 3).** For every unit F ∈ E_T,
    𝒱^♯(F)/T ≤ liminf_{h↓0} (λ_A(T) − λ_A(T+h))/h ≤ limsup_{h↓0} (λ_A(T) − λ_A(T+h))/h ≤ limsup_{h↓0} 𝔈_h/h,
the left inequality from (2.1) (at a contact threshold add φ(F)), the right one from (3.1) and ‖G♯‖ → 1 (‖R‖ → 0 along any
precompact family of minimisers).

Reading (edge trace vs energy). The upper bracket is the energy of the two edge strips of the later minimiser measured
above its eigenvalue, (a − λ′)(R), minus the flux of the Tate multiplier through the strips, 2⟨ρ, R⟩, plus a repair of order
h^{1/2}‖R‖. If F behaves at the edge like the log-order Dirichlet problem suggests, F(±(T′−δ)) ≍ θ_±(log 1/δ)^{−1/2} (ARGUED by
the analogy K(u) = 1/u + O(1), i.e. the archimedean form is ½ the logarithmic Laplacian plus a bounded form; the boundary
decay of eigenfunctions of that operator is quoted from memory and is not CITED here), then ‖R‖² ≍ (θ₊² + θ₋²)h/log(1/h),
⟨ρ, R⟩ = o(h), and the log-order energy of a strip of width h is ≍ log(1/h)·‖R‖², so 𝔈_h ≍ (θ₊² + θ₋²)h: a Hadamard formula
with the edge traces θ_± in place of normal derivatives (ARGUED, constant not derived). The derivative of λ_A is an edge
quantity of the minimiser; it is never an interior quantity.

## 4. Grönwall in T: what it would give, and what it is

**Proposition 4 (discrete Grönwall; PROVED, no absolute continuity needed).** Let T₀ > 0 with λ_A(T₀) > 0 and let
C : [T₀, ∞) → [0, ∞) be continuous. Suppose that for every T ≥ T₀ there are arbitrarily small h > 0 with
    λ_A(T) − λ_A(T + h) ≤ C(T)·h·λ_A(T + h) + o(h)·λ_A(T + h)                                     (EB_C)
(for instance: 𝔈_h ≤ C(T)h λ_A(T+h)‖G♯‖² + o(h)λ_A(T+h), by (3.1)). Then λ_A(T) ≥ λ_A(T₀)exp(−∫_{T₀}^T C) > 0 for all T ≥ T₀.
Proof. Let T₁ = sup{T ≥ T₀ : λ_A(S) ≥ λ_A(T₀)exp(−∫_{T₀}^S C) − ε(S − T₀) for S ∈ [T₀, T]} for fixed ε > 0, and suppose T₁ < ∞.
By continuity (lem:contA) the inequality holds at T₁, so λ_A(T₁) > 0 for ε small. (EB_C) at T₁ gives h arbitrarily small with
λ_A(T₁ + h) ≥ λ_A(T₁)/(1 + C(T₁)h + o(h)) ≥ λ_A(T₁)(1 − C(T₁)h) − o(h); since λ_A is non-increasing, the inequality holds on
[T₁, T₁ + h] up to o(h) — and the −ε(S − T₀) slack absorbs the o(h) for h small — contradicting the definition of T₁ (the
standard continuous-induction argument; continuity of λ_A replaces absolute continuity because the hypothesis is on
increments, not on a derivative). Let ε → 0. ∎
This closes the gap of R186_111 §3.1 (absolute continuity) for the integrated form; (EB_C) is a statement on increments.

**Proposition 5 ((EB_C) and its differential form are restatements of (★) plus a rate; PROVED).**
(i) If (★) holds strictly on [T₀, ∞) and λ_A is locally Lipschitz there, then (EB_C) holds with the continuous majorant of
C(T) := limsup_{h↓0} (λ_A(T) − λ_A(T+h))/(hλ_A(T+h)) = −D_-log λ_A(T) (upper right logarithmic Dini rate), which is finite.
So "there exists a continuous C with (EB_C)" is (★) on [T₀, ∞) together with local Lipschitz continuity of λ_A.
(ii) For any weights w (cΛ with c ≠ 1, a_P, a Beurling system, a finite modification of v_n) whose bottom λ_w has a first zero
T_c and is negative on (T_c, T_c + δ): (EB_C) fails at T_c for every finite C, because its right side is ≤ 0 for h small
(λ_w(T_c + h) < 0) while its left side is ≥ 0 (monotonicity) and > 0 for some arbitrarily small h (λ_w is not constant on
[T_c, T_c+h]). The same holds for the differential form D ≤ Cλ (D := −λ′ ≥ 0) and for the minimiser forms 𝒱^♯ ≤ TCλ and
𝔈_h ≤ Chλ. The failure is automatic and is caused only by the sign of λ_w itself.
(iii) A uniform (form) version — "𝒱^♯(F) ≤ T·C·a_T(F) for every F ∈ P_T" or "a_T − (1/(TC))𝒱^♯ ⪰ 0 on P_T" — implies (★) at T
directly (apply it on E_T, where 𝒱^♯ ≥ 0 by Cor. 2.2 and a_T = λ_A). By (2.1), a_T(F) − s𝒱^♯(F) = a_{(1+s)T}(W_{1+s}F) + o(s)
for each fixed F, so the uniform version with s = 1/(TC) is, to first order in s, the statement λ_A((1 + s)T) ≥ 0: an Euler step
of (★) of length T·s = 1/C ≈ e^{−2T}/(8π) (ARGUED: the o(s) is not uniform on P_T without a second-variation bound).
Proof. (i) Local Lipschitz gives (λ(T) − λ(T+h))/h bounded, and λ(T+h) ≥ λ(T)/2 > 0 for small h; take a continuous majorant.
(ii) and (iii) as stated. ∎

Answer to task (2). The Grönwall inequality D ≤ Cλ_A (or (EB_C)) is a **restatement**: with an unspecified finite C it is (★) plus
local Lipschitz continuity (Prop. 5(i)); every falsifier fails it automatically at its first zero and only through its own sign
(Prop. 5(ii)), which is exactly the signature that rule 4 of the brief flags as carrying no mechanism; a uniform form version is
(★) at the next Euler step (Prop. 5(iii)). With the constant the law demands, C = 8πe^{2T}(1 + o(1)) (ROUND_007_D §2; §5 below
measures it), the inequality is strictly stronger than (★): it is the lower half of the rate-2 law in differential form, i.e.
R186-bilateral (OPEN residue) written as an increment inequality. No structured weaker statement was found: every weakening
that keeps a finite explicit C is still a lower bound of relative precision C·λ_A on a difference of two O(1) quantities (§5),
and every weakening that drops C is Prop. 5(i).

## 5. NUMERICAL: d log λ_A/dT on 0.7 ≤ T ≤ 1.2 and the minimiser formula

Method (tools/galerkin_mp.py, Dirichlet sines, even sector = bottom sector at every T). The dilated sine basis on I_{rT} is
U_r applied to the sine basis on I_T, so in fixed coordinates v the Galerkin form is v ↦ vᵀM_{T}v with M_T = Arch_T − Π_T
and the Tate rows A_T, B_T depending smoothly on T between contacts. Then (i) λ_A^N(T) is differentiated by a central
difference with relative step δ; (ii) the minimiser formula of Theorem 1 is evaluated as the constrained Hellmann–Feynman
expression λ′ = vᵀArch′v − vᵀΠ′v − 2μᵀ(C′ᵀv), where v is the unit minimiser, μ the two multipliers (Mv = λv + Cμ, residual
≤ 10⁻⁶⁰), C = [A_T B_T]; vᵀArch′v = −𝒱_∞(F*)/T, vᵀΠ′v = −(comb virial)/T, −2μᵀC′ᵀv = −τ(F*)/T. N = 90, dps 40 (δ = 10⁻¹⁴),
checked at dps 60/80 with δ = 10⁻²⁰/10⁻²⁵ at T = 1.0, 1.1, 1.2. "law" = 2c₁e^{2T} + c₂ with the ROUND_007_D whole-range fit
(c₁ = 12.59, c₂ = −20.6).

| T | λ_A^N | −λ′ (fd) | HF vs fd (rel.) | −d log λ/dT | 8πe^{2T} | law | 𝒱_∞(F*) = T·|Arch′| | |λ′|/|Arch′| | τ-part / λ′ | |μ|/λ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.7 | 6.343·10⁻⁸ | 5.402·10⁻⁶ | 3·10⁻²² | 85.2 | 101.9 | 81 | 1.0030 | 3.8·10⁻⁶ | 4.6·10⁻⁴ | 0.36 |
| 0.8 | 5.974·10⁻¹² | 6.471·10⁻¹⁰ | 2·10⁻¹⁸ | 108.3 | 124.5 | 104 | 1.0032 | 5.2·10⁻¹⁰ | 3.3·10⁻⁴ | 0.36 |
| 0.9 | 5.726·10⁻¹⁷ | 7.935·10⁻¹⁵ | 1·10⁻¹³ | 138.6 | 152.0 | 131 | 1.0034 | 7.1·10⁻¹⁵ | 2.4·10⁻⁴ | 0.35 |
| 1.0 | 1.963·10⁻²³ | 3.456·10⁻²¹ | 2·10⁻¹⁹ (dps 60) | 176.1 | 185.7 | 166 | 1.0035 | 3.4·10⁻²¹ | 1.7·10⁻⁴ | 0.35 |
| 1.1 | 1.510·10⁻³¹ | 2.836·10⁻²⁹ | 2·10⁻¹¹ (dps 60) | 187.9 | 226.8 | 207 | 1.0036 | 3.1·10⁻²⁹ | 1.5·10⁻⁴ | 0.35 |
| 1.2 | 2.611·10⁻⁴¹ | 6.908·10⁻³⁹ | 7·10⁻¹² (dps 80) | 264.5 | 277.0 | 257 | 1.0037 | 8.3·10⁻³⁹ | 1.0·10⁻⁴ | 0.35 |
Secondary: N = 60 gives −d log λ/dT = 84.0, 110.1, 140.3, 168.5 at T = 0.7–1.0 (stable to ≈ 5 %) and 127, 92 at 1.1, 1.2 (not
converged); N = 120 at T = 1.2 gives 223.3 (λ = 1.264·10⁻⁴¹). At dps 40 with δ = 10⁻¹⁴ the matrix difference quotients have a
floor ≈ 10⁻²⁸ (visible at T ≥ 1.1), removed at dps 60–80.

Readings (NUMERICAL).
(a) The Hellmann–Feynman formula of Theorem 1 reproduces the derivative of the Galerkin bottom to 11–22 digits at every T:
within the Galerkin model the variation formula, with the Tate term, is exact. (In the sine model (R_E) holds trivially; the
model's minimiser vanishes at the edge, so the fold is invisible and the edge behaviour is that of the basis, which is the
known source of its slow N-convergence, TOOL_001 §2.)
(b) −d log λ_A/dT = 85 → 265 on 0.7 → 1.2, between 0.83 and 0.96 of 8πe^{2T} and within ±7 % of the law's 2c₁e^{2T} + c₂, except
T = 1.1 (−9 %, just after the contact ½log 9 = 1.0986, and N = 90 is not converged there: λ^N(1.1) = 1.51·10⁻³¹ against
1.08·10⁻³¹ at N = 180). The Grönwall constant demanded by the data is C(T) ≈ 8πe^{2T} − 21 on the whole resolved range.
(c) The archimedean virial of the minimiser is 𝒱_∞(F*) = 1.003–1.004 at every T (the minimiser lives where τm′(τ) ≈ 1), the
comb virial equals it, and their difference 𝒱(F*) = T·D is 3.8·10⁻⁶ (T = 0.7) … 8.3·10⁻³⁹ (T = 1.2) of either. The Tate virial
is 10⁻⁴ of D and the multipliers are ≈ 0.35λ: the constraint is invisible at the scale of the derivative, as it is at the
scale of λ (ROUND_007_D §3(a)).
(d) Hence D/λ_A = 𝒱^♯(F*)/(T·a_T(F*)) is a ratio of two cancellations: numerator 𝒱_∞ − 𝒱_Π (each ≈ 1.00), denominator
Arch − Π (each ≈ 0.087 → 0.015). The inequality D ≤ Cλ with C ≈ 8πe^{2T} asks that the virial cancellation be at most C·T times
the energy cancellation; at T = 1 this is a statement at relative precision 3.4·10⁻²¹ on the virial pair.

## 6. Pure mathematics: D/λ through the minimiser

Proposition 6 (PROVED under (R_E), simple bottom with minimiser F*). 
    D(T)/λ_A(T) = 𝒱^♯(F*)/(T·a_T(F*)) = [𝒱_∞(F*) − 𝒱_Π(F*) + τ(F*)] / [T(Arch(F*) − Π_T(F*))],   𝒱_Π(F) := Σ_{N_T} v_n log n·c_F′(log n),
and, by Theorem 1 and Corollary 3.1, T·D ∈ [𝒱^♯(F*), T·limsup 𝔈_h/h]. In the edge form: D ≤ limsup_h 𝔈_h/h, so the
Grönwall inequality is implied by the edge-budget inequality
    (EB_C)   𝔈_h(F*_{T+h}) ≤ C(T)·h·λ_A(T + h)·(1 + o(1))      (edge-strip energy above the bottom, minus multiplier flux, plus repair),
and it implies the virial–energy inequality
    (VE_C)   𝒱^♯(F*_T) ≤ T·C(T)·a_T(F*_T)     (the virial cancellation is at most TC times the energy cancellation).
Proof. Theorem 1(c) for a simple bottom (E_T one-dimensional, (U) reduces to continuity of F* in T, which is what (R_E) and the
proof of (c) use), Proposition 3 and Corollary 3.1. ∎

What follows, and what does not. (i) Under (EB_C) with any continuous C, (★) holds on [T₀, ∞) from any certified base T₀
(Prop. 4; base ½log5, P47 thm:log5A; floors to ½log15 transferred in ROUND_007_D Cor. 4.3). (ii) Under (VE_C) alone, (★) follows
only with absolute continuity of λ_A (R186_111 §3.1) — Proposition 4 does not apply to the virial direction, because (2.1) is an
upper bound on λ_A(T+h), not a lower one. So the right inequality to aim at is the edge one, (EB_C), not the virial one: the
edge budget majorises the decrement, the virial minorises it. (iii) Neither inequality is proved, and §5(d) gives their size.

**The remaining inequality (named).** (EB_C) with C(T) = 8πe^{2T}(1 + o(1)): for every T ≥ ½log5 and small h, the energy of the
two edge strips of width h of the minimiser at T + h, measured above its eigenvalue and corrected by the Tate multiplier flux
and repair, is at most C(T)·h·λ_A(T+h). OPEN. It is the lower half of the rate-2 law (R186-bilateral) written on increments,
and it belongs to class 𝒦_H (H_001: differential inequalities with coefficients at the minimiser).

## 7. Falsifier test (rule 4)

Theorem 1, Corollary 2.2, Propositions 2.3, 3, 4 and 6 are structural: they hold verbatim for cΛ, a_P, every Beurling system and
every finite modification of v_n (only finiteness of the comb on bounded windows and the Lévy form are used). They are not sign
steps and are not required to fail. The only sign-bearing statements are the hypotheses (EB_C), (VE_C), D ≤ Cλ; by Prop. 5(ii)
each fails for every falsifier with a first zero (certified for a_3, the Beurling 3→3.2 system and 1.1Λ, ROUND_007_C), at its
first zero, for every finite C — and fails only through the sign of the falsifier's own λ. Before the first zero T_c of a
falsifier, its λ_w and Λ's λ_A coincide on every window where the weights agree (the Beurling system and a finite
modification agree with Λ below the first modified point; cΛ and a_P differ from the start but enter the hypothesis only
through λ_w), so (EB_C) uses no information that distinguishes them until λ_w itself turns: rule 4 is satisfied only in the
trivial way that flags a restatement.

## Result

PROVED pieces + NO-GO (restatement) for the Grönwall route in the window variable.

## What was proved

1. Theorem 1 (PROVED under (R_E); Danskin equality CONDITIONAL on (U)): the one-sided variation λ_A(T+h) ≤ λ_A(T) − (h/T)𝒱^♯(F)
   − h⁺φ(F) + o(h) for every F in the bottom eigenspace, with 𝒱^♯ = archimedean virial − comb virial + Tate virial (first Tate
   moments × Lagrange multipliers) and φ the entry fold; D⁺/D₋ as max/min over the eigenspace; concave corners at non-scalar
   degenerate bottoms; Corollary 2.2: 𝒱^♯ ≥ 0 on E_T.
2. Lemma 1.2: m′ ≥ 0 on [0, ∞), so the archimedean virial is a nonnegative bounded form.
3. Proposition 2.3: entering contacts contribute 0 at every order in the zero-extension frame, the fold −hφ in the dilation
   frame, and nothing explicit in the truncation frame.
4. Proposition 3 (PROVED for minimisers bounded near ±T; ARGUED in general): the exact, simplicity-free inequality
   (λ_A(T) − λ_A(T+h))‖G♯‖² ≤ 𝔈_h (edge-strip energy above the bottom − multiplier flux + Tate repair) — the Hadamard direction
   that R186_004 listed as OPEN, in integrated form. Corollary 3.1: the decrement is squeezed between virial and edge budget.
5. Proposition 4: a discrete Grönwall lemma on increments that needs only continuity of λ_A (closes R186_111 §3.1 for (EB_C)).
6. Proposition 5: D ≤ Cλ / (EB_C) / (VE_C) with unspecified C are (★) plus local Lipschitz continuity; every falsifier fails them
   automatically at its first zero; the uniform form version is (★) at the next Euler step (ARGUED).

## What failed and why

- The Grönwall inequality is a restatement (Prop. 5); with the explicit constant the data demand (C ≈ 8πe^{2T} − 21, §5) it is
  the lower half of the rate-2 law on increments, OPEN, and in class 𝒦_H (H_001; under c = 2πe^{2T} the constant 8πe^{2T} is the
  Slepian constant 2 of H_001).
- No structured weaker statement exists in this frame: D/λ is a ratio of two cancellations, 𝒱_∞(F*) − 𝒱_Π(F*) with each term
  ≈ 1.003 and Arch(F*) − Π(F*) with each term ≈ 0.02–0.09; any finite explicit C asks for the first at relative precision C·T·λ
  (3.4·10⁻²¹ at T = 1, 8.3·10⁻³⁹ at T = 1.2). The edge-trace reading (§3) relocates this cancellation to the edge strips of the
  minimiser but does not reduce its precision.
- The edge Hadamard constant (§3 reading) is ARGUED by analogy with the log-order Dirichlet problem; the boundary decay of the
  true minimiser is not known (R186_036 §4).

## Next concrete step

Measure the edge budget 𝔈_h/h directly on a basis that resolves the edge (sines plus the two functions (log 1/(T∓t))^{−1/2}
near ±T, or a Jacobi-weighted basis), to test the ARGUED Hadamard form 𝔈_h ≍ (θ₊² + θ₋²)h and to see whether the edge traces
θ_±(F*) themselves follow 8πe^{2T}·λ_A — i.e. whether λ_A ≍ θ² e^{−2T}/(8π) holds as an identity of sizes. That would turn
(EB_C) into a pointwise statement about two numbers per window (the edge traces), the smallest object the derivative depends on.
Do not retry Grönwall with another denominator (restriction 11 of the index).
