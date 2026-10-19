# PROOF_L_SHARP_Q_001 — Strategy Q: Toeplitz-plus-Hankel structure of 𝔔 in the log variable on the half-line

Phase 199, prover memo (pen and paper; NUMÉRICO only to check one constant). Target: Lemma L′♯ = (★★_u) (AUDIT_L_SHARP_2 §7,
constraints 1–11).
Notation: memo F (Prop F.0, Thm F.1, F.2), J (Prop J.1),
P (P.1, P.2). λ = 1, a = 0 (Prop F.0). Log variable x = log X ∈ (0,∞), ρ̃(x) := e^{x/2}ρ(e^x), R(s) = ∫_1^∞ρX^{−s}dX = (Fρ̃)(τ), s = ½+iτ.

**Outcome in one line.** L′♯ is NOT proved. The premise "𝔔 = T_a − H_b + P₂ with H_b the log(mn) prime part" is corrected.
(Q.1) The prime part is NOT a Hankel form. It is a lattice of Toeplitz diagonals log(p/q), (p,q) = 1, and each diagonal carries
a *monotone increasing* step weight of the Hankel variable. Such a weight is never completely monotone, so Widom/Bernstein–Widder
cannot be applied piece by piece.
(Q.2) The genuine Toeplitz+Hankel decomposition is exact and has a different shape: 𝔔_c = T_{a_c} + 𝐇_c, with Toeplitz symbol
a_c(τ) = (1−c)Θ_∞(τ)|ζ(½+iτ)|². So **a_1 ≡ 0**. At c = 1 the whole form is built from ONE Hankel operator, H_ζ := P_−M_ζP_+
(symbol ζ(½−iτ), pole-regularised). The Euler–Maclaurin defect G of memo F is G = −H_ζ^♮ρ̃ (+ polar mode).
(Q.3) Hence, by Hartman–Wintner, the Toeplitz part has essential spectrum {0}. There is no coercive Toeplitz term to dominate
the Hankel part, and strategy (iii) (Toeplitz coercivity + Nehari/AAK smallness of the Hankel part) is NO-GO.
(Q.4) cΛ check: the decisive ingredient is the FE identity a_1 ≡ 0. It kills c > 1 at high frequency (ARGUED; the deep-mode case
is PROVED in J Cor J.4(c)). For c < 1 the Toeplitz part is coercive at high frequency, so the split does not see c < 1.
Residual (★★_Q): a statement about the single Hankel operator H_ζ. No sign. Row D OPEN.

## 0. Corpus / index check and the new reason
Index searched (ROUTES-TRIED-INDEX README, 03, 04, 05, 06) for Hankel / Toeplitz / Widom / Nehari / moment / completely
monotone. Entries found: G8A-118/W3 (scattering Toeplitz/Hankel in log n, heuristic, measured refutation); G4C-R161_039-045
(Toeplitz–Hankel local square, Brown–Halmos, does not globalise); G8D-R164_502c and G8D-R160_S2 F24 (Szegő–Widom/GLT symbol
of the *window* operator σ_T, symbol never positive); P45-1 (Weil–Toeplitz C*-algebra); W-det (Widom determinants);
R186-bilateral (Landau–Widom); A14a-1/L49 (PF₅ Toeplitz minor falsifier); G3D-159 (Nehari norms of the Suzuki kernel, a
mollifier/canonical-system route); G8A-R160_S1 (finite-order Hankel positivity); G2B-phase-119 (PSD Hankel of Ξ_a, falsifier).
**New reason (why this is not a retry).** Every previous Toeplitz/Hankel entry treats the *window* compression (Toeplitz of −θ′
or σ_T on [−T,T]), whose symbol is nonzero and indefinite. Here the object is the *exterior* form 𝔔 on L²(1,∞) of Prop F.0
(fixed, μ-free), and the question is the exact T+H anatomy of 𝔔 itself on the multiplicative half-line. The new fact (Q.2) is
that its Toeplitz symbol is *identically zero* (not indefinite). This turns the question into one about a single Hankel
operator with symbol ζ. G3D-159 Nehari is a mollifier norm, a different object. The constructive outcome is again negative and
is recorded as a NO-GO for the class 𝒦_{T+H} below.

## 1. (i) Exact kernel of the prime part in log coordinates (Q.1, PROVED)
By J Prop J.1(a),(b), with φ := ρ̃ on (0,∞) (zero on (−∞,0)), J(m,n) = (mn)^{−1/2}∫_0^∞φ(x+log m)φ(x+log n)dx and
  Π[φ] := Σ_{m,n}log(mn)J(m,n) = Σ_{(p,q)=1}(pq)^{−1/2}∫_ℝ φ(t+log p)φ(t+log q)·W_{pq}(t)dt,
  W_N(t) := Σ_{1≤j≤e^t} j^{−1}log(j²N)  (t ≥ 0; W_N = 0 for t < 0).
(Put m = jp, n = jq, t = x + log j. Absolute convergence holds since φ = O(e^{−3x/2}); exchange by Tonelli on |·|.) Likewise
‖Zr‖² = Σ_{(p,q)=1}(pq)^{−1/2}∫φ(t+log p)φ(t+log q)W⁰(t)dt with W⁰(t) = Σ_{j≤e^t}1/j.
**Reading.** In the variables (u,v) = (t+log p, t+log q) the kernel is Σ_{(p,q)=1}δ(u−v−log(p/q))·h_{pq}(u+v), with
h_N(w) := N^{−1/2}W_N((w−log N)/2). This is a *product* of two structures, not a sum T + H:
- a lattice Toeplitz structure (diagonals u−v ∈ log ℚ_{>0}, the near-coincidence direction);
- a Hankel-variable weight (the multiplication direction).
∂_t W_N = Σ_j(2log j + log N)j^{−1}δ(t−log j) ≥ 0, and W_N(t) = t² + (log N)(t+γ) + 2γ₁ + o(1) (Euler–Maclaurin; γ₁ the
first Stieltjes constant). So each weight is **increasing and unbounded**. A completely monotone function is non-increasing.
Hence no diagonal weight is a Laplace transform of a positive measure, and Widom's Hankel-positivity criterion (CITED: Widom
1966, a Hankel form on the half-line is PSD ⟺ its kernel is CM) has no object on any piece. **PROVED.**
**Moment form.** Π[φ] = −N′(0), where N(σ) := ‖Σ_m m^{−1/2−σ}φ(·+log m)‖²_{L²(0,∞)} = Σ(mn)^{−σ}J(m,n) ≥ 0 for all σ (Gram).
N(σ) = ∫e^{−σs}dν(s) with ν = Σ_K(Σ_{mn=K}J(m,n))δ_{log K}. ν is signed in general: ν({log 2}) = 2J(1,2) < 0 for any φ with
∫_0^∞φ(x)φ(x+log 2)dx < 0. So N is not CM (Bernstein, CITED). The Hankel weight log(mn) = −∂_σ(mn)^{−σ}|₀ is the boundary
derivative of rank-one positive Hankel weights; the matrix (log m + log n) has rank 2 and signature (1,1). **PROVED.** No sign.

## 2. (ii) The exact Toeplitz+Hankel decomposition (Q.2)
Let M = M_ζ be the Fourier multiplier ζ(½−iτ) = ζ(1−s) on L²(ℝ) (log variable), and P_± the projections onto y ≷ 0. With the
weights cΛ (prime part multiplied by c), write Q_c(U) = (1/2π)∫[Θ_∞|U|² − 2c Re(Ū U_log)]dτ (memo F Thm F.2 notation).
**Theorem Q.2.**
(a) F₀ = Mρ̃ (F Thm F.2). F is the transform of Ψ̌ (the P_+ part). G = F − F₀ is the Fourier transform of
  ρ₀e^{−y/2}1_{y>0} − (Zρ − ρ₀e^{−y/2})1_{y<0}  (AUDIT_2 §3.2), i.e. G = −H_ζ^♮ρ̃ + ρ₀·(polar mode),
where H_ζ^♮ρ̃ := P_−(Mρ̃ − ρ₀e^{−y/2}) is the Hankel operator of symbol ζ(1−s), regularised by subtracting the polar mode. The
polar mode comes from the pole of ζ(1−s) at s = 0, with coefficient ρ₀ = R(1) times the residue 1 of ζ.
(b) Q_c(F₀) = (1/2π)∫a_c(τ)|R(τ)|²dτ =: T_{a_c}[ρ̃], with **a_c(τ) = (1−c)Θ_∞(τ)|ζ(½+iτ)|²**. This is a Toeplitz form on
L²(0,∞), because R is the Fourier transform of a half-line function.
(c) Consequently 𝔔_c = T_{a_c}[ρ̃] + 𝐇_c[ρ̃], where 𝐇_c := 2Q_c(F₀,G) + Q_c(G,G) + 2AB. At c = 1,
  **𝔔 = 𝐇_1 = −Q(G,G) + 2Q(F,G) + 2AB,  G = −H_ζ^♮ρ̃ + polar,**
and every term is a bilinear expression in H_ζ^♮ρ̃, P_+Mρ̃ and the two pole functionals.
*Proof.* (a) is F Thm F.2 together with AUDIT_2 §3.2 (G = F₁+F₂ is the displayed Fourier transform); Zρ − ρ₀e^{−y/2} lies in
L²(y<0) by Euler–Maclaurin (F Lemma 3.1). (b) F₀^{log} = −ζ′(1−s)R, so Re(F̄₀F₀^{log}) = −|ζR|²Re(ζ′/ζ)(1−s). On the line
1−s = s̄, and F Thm F.1 gives 2Re(ζ′/ζ)(s̄) = −Θ_∞. Hence Θ_∞|F₀|² − 2cRe(F̄₀F₀^{log}) = (1−c)Θ_∞|ζR|². (c) follows from
bilinearity and from P.1 at c = 1. □ **PROVED.** Each piece has its L² meaning as in F Thm F.2(i). The identification of G with
a Hankel image is the AUDIT §3.2 identity rewritten; no new analysis is involved.
**Correction to the premise.** The log(mn) prime part and the Lévy/Γ_ℝ part do not separate into H and T. They are the two
halves of Q, and on the Q-null image Mρ̃ they cancel *pointwise in τ* (a_1 ≡ 0). What survives is Q evaluated on the Hankel
image of ζ. The lattice ℕ (a_n ≡ 1) enters only through M = ζ, that is, through H_ζ.
**Consistency (ARGUED).** For y < −log μ, Poisson summation in the dilate index gives (Zρ − ρ₀e^{−y/2})(y) =
e^{−y/2}Σ_{k≠0}(ρ1_{X>1})^(k e^{−y}). Since ρ = ĝ|_{(1,∞)} with supp g ⊂ [−μ,μ], the g-part vanishes for k e^{−y} > μ. So far
out, the Hankel image is determined by the in-band piece ĝ1_{|X|<1} alone. This is K Thm K.3's circularity seen in T+H language.

## 3. (iii) The strategy "Toeplitz coercivity + Nehari/AAK" is NO-GO (Q.3, PROVED)
(a) By Q.2(b), the Toeplitz part of 𝔔 has symbol a_1 ≡ 0. By Hartman–Wintner (CITED: the essential spectrum of T_a is the
essential range of a, for real a ∈ L^∞; here trivially T_0 = 0) there is no Toeplitz margin at all.
(b) Take any other split 𝔔 = T_{a′} + (𝐇_1 − T_{a′}) with a′ ≥ 0, a′ ≢ 0. It puts the Toeplitz symbol −a′ into the remainder.
Nehari's theorem and AAK (CITED, Peller 2003 ch. 1, 4) bound ‖P_−M_bP_+‖ and its s-numbers by dist(b,H^∞) and by rational
approximation of b. They bound *Hankel* operators only and give no control of T_{−a′}, whose spectrum on L²(0,∞) fills
[−sup a′, 0]. So in every split the "small" part contains a Toeplitz piece as large as the "coercive" one. The scheme
T ≥ κ₁·leak, ‖H|_{PW_μ∩𝒢⊥}‖ ≤ small cannot be run.
(c) Restricting to PW_μ does not rescue it, because T_{a′} − T_{a′} = 0 identically on every subspace. The margin must come from
𝐇_1 restricted to PW_μ ∩ 𝒢̄₁^⊥, i.e. from a *lower* bound on a form built from H_ζ. AAK and geometric s-number decay for
analytic symbols give *upper* bounds.
**NO-GO (PROVED) for the class 𝒦_{T+H}:** "a coercive Toeplitz part (any symbol a′ ≥ 0) dominating a Hankel part estimated by
Nehari/AAK/Widom s-number decay", on the exterior carrier.

## 4. The cΛ test and the Λ-ingredient (Q.4)
a_c = (1−c)Θ_∞|ζ|². Θ_∞(0) = ψ(¼) − log π = −5.37218; Θ_∞(τ₀) = 0 at τ₀ = 6.28984 (NUMÉRICO, mpmath); Θ_∞ ~ log(|τ|/2π) → +∞.
(a) c > 1: a_c → −∞ at high frequency. On ρ whose R is concentrated at |τ| ≫ 1, the Toeplitz term is about
−(c−1)log|τ|·‖ζR‖², while 𝐇_c involves H_ζ, which is small on high-frequency smooth data. So 𝔔_c < 0 (ARGUED; the deep-mode
instance 0.046 − 2(c−1)(D+O(1)) is PROVED in J Cor J.4(c)). The decisive step does fail for c > 1. The ingredient is exactly
the FE identity Θ_∞ = −2Re ζ′/ζ on the line, where Γ_ℝ (conductor 1) and Λ with a_n ≡ 1 are matched.
(b) c < 1: a_c ≥ 0 for |τ| > τ₀ and grows. The Toeplitz part is coercive at high frequency and negative only on the band
|τ| < τ₀. So the T+H split does not detect c < 1 by itself. For c < 1 falsifiers, any proof via Q.2 must use the low band
|τ| < 6.29 together with 𝐇_c.
(c) The three Λ-ingredients localise as follows:
- a_n ≡ 1 → the symbol ζ of H_ζ (Poisson/Euler–Maclaurin lattice);
- residue 1 → the polar mode ρ₀e^{−y/2} subtracted in H_ζ^♮, and the rank-2 term 2AB;
- conductor 1 → a_1 ≡ 0 (Γ_ℝ in Θ_∞).

## 5. (iv) Residual (OPEN)
  **(★★_Q)**  −Q(G,G) + 2Q(P_+Mρ̃, G) + 2AB ≥ κμ^{−A}dist²(ρ,𝒢̄₁)  on PW_μ,  G = −H_ζ^♮ρ̃ + ρ₀·polar.
Since P_+Mρ̃ = F, this is a statement about the single Hankel operator H_ζ of symbol ζ(½−iτ) acting on out-of-band tails,
through the line form Q (symbol Θ_∞ on |·|², log-weight pairing). By Q.2 it is (★★_P) of memo P rewritten: a restatement,
not a reduction.
Widom's moment criterion would apply only if 𝔔 were a single Hankel *quadratic* form in ρ̃, and it is not. The coupling Q(F,G)
pairs the P_+ image with the P_− image through a convolution, i.e. through a Hankel operator H_Θ composed with H_ζ, so 𝔔
contains products of type H_Θ^*H_ζ. Hence (★★_Q) is not a moment problem.
Open question recorded: restricted to the range of H_ζ^♮, is −𝐇_1 a negative CM (Laplace-type) form? The only hint is
NUMÉRICO (P.4: Q(G,G) ⪯ 0, 𝔔 ≈ −Q(G,G)). It is plausible and unproved, and it would itself be of (★★) strength.

## 6. Labels
PROVED: Q.1 (lattice-diagonal kernel, monotone weights, non-CM; moment form, ν signed); Q.2 (a)–(c) (a_c = (1−c)Θ_∞|ζ|²,
a_1 ≡ 0, G = Hankel image of ζ); Q.3 NO-GO for 𝒦_{T+H}. ARGUED: Q.4(a) beyond deep modes; the §2 consistency remark.
NUMÉRICO: τ₀ = 6.28984. CITED: Widom 1966, Bernstein–Widder, Hartman–Wintner, Nehari, AAK/Peller. OPEN: (★★_Q) = L′♯.
**Do not retry:**
- Widom/Bernstein CM tests on the log(mn) weight or on single ratio diagonals;
- Toeplitz-symbol coercivity of any part of 𝔔 on the exterior carrier (the symbol is ≡ 0);
- Nehari/AAK upper bounds as a sign source.
No sign is claimed. Row D OPEN.
