# PROOF_L_SHARP_H_001 — Strategy H: a differential (Grönwall) argument in c = 2πμ from the certified base μ ≤ 15

Phase 199, prover memo (pen and paper; no numerics). Target: **Lemma L′♯ / (★★)** (AUDIT_L_SHARP_1 §6.3): ∃κ > 0, A ≥ 0:
∀μ ≥ 5, ∀g ∈ E(core): W_T(g) ≥ κμ^{−A}ℓ(g). no equivalence of
any kind is invoked;
Notation: T = ½log μ, λ = √μ = e^T, c = 2πμ, I = (−T,T), W_T the complete form (Mori's Q), E the summation map,
ℓ(g) the gauge-minimised leakage (AUDIT_199), 𝔐, D, 𝒦 as in memo A §3.4, G_φ, k, W^− defined in §1.

**Outcome in one line.** L′♯ is NOT proved. What is obtained: (1) the base case is PROVED with explicit constants
(§2: L′♯ holds for 5 ≤ μ ≤ 15 with A = 2, κ = 2^{−2905}/C₀, from Mori ½log15 CITED + memo A Lemma 4.2); (2) a dilated
frame in which the summation image of a test is a **fixed** function G_φ truncated to the growing interval (−2T, 0),
the admissibility constraints are c-independent and only the band edge and the gauge move (§1, PROVED); (3) exact
rate identities (§3, PROVED): the leakage rate is the band-edge Fourier value, d/dc leak_c(φ) = −(1/π)|φ̂(c/2π)|²
(rank one; Slepian's identity is the prolate case), and the window-form rate is a boundary pairing,
dN/dT = −2G_φ(−2T)·(W^−G_φ)(−2T), with W^− the *odd* (Hilbert-type) Weil distribution; N is C¹ across contact
crossings for every fixed test, and the crossing of q enters only at second order with coefficient
c_q·G_φ(−2T)·φ′(1); (4) the exact closure condition of the Grönwall scheme (§4, Theorem H.5, PROVED as an
equivalence): the scheme closes if and only if, at the minimiser of the pencil, the decay rate of the window form
does not exceed the decay rate of its own leakage by more than A/c — a virial-type inequality of relative precision
O(1/c) at the minimiser. The Slepian input fixes the *target* rate exactly (2 − (k+½)/c, so the quantitative
obstruction "c superexponential" of R186_038 α.3(b) disappears in the variable c), but the virial side is a
functional of the minimiser with no independent bound, which is the recorded wall (lem:flowdet, W-lin, R186_038
α.3, INV_U §3). The crossing positions (the only ℤ-specific, non-TV-robust input listed in the brief) enter the
derivative with a sign-indefinite coefficient and at second order only, so they cannot drive the inequality.
**Strategy H is NO-GO as a class** (𝒦_H: differential inequalities in T or c whose coefficients are evaluated at
the minimiser); its identities are recorded as objects. No sign is claimed. Row D OPEN.

## 0. Corpus check (rule ) and why this is not a bare retry
- **Index read.** 04_PHASES l.67 (lem:flowdet / β,T-flow: NO-GO, "coefficient dominated by h*(T)²/λ_A"), l.139
  (R186-S2seeds: Fold/Grönwall NO-GO, "vacuous/closed/pole-dominated"), l.401 (G8F-157 lem:monoT: REF-D), l.412
  (G3E-159: bootstrap in T, DEAD), l.431 (G8E-159 bootstrap: flow on orbit is identity), l.635 (G7E-R160 flow-monotone
  functional: every monotone functional is generic/archimedean/explicit-formula), l.975 (R170_888 Hellmann–Feynman in
  Z_N: tool PROVED, no sign), l.1033 (P47 D.1–D.3: monotonicity in T fails for the state reformulation); README
  l.423 (BARRIER_D2_001: continuation in comb space transfers only λ_A(a₀) − d_v; segments give only upper bounds),
  l.450–455 (MECH_001, PROOF_L_SHARP_A–E, AUDIT_L_SHARP_1); SURVEY l.116 (flows in T closed, monotonicity = SPEC_A).
- **Corpus read.** R186_038 §2 and Lemma α.3 (Grönwall on the minimiser ⟺ virial bound 𝒱_T(h*) ≤ Tc(T)λ_A(T),
  c superexponential in T, vacuous without an independent virial bound: "la misma cancelación de la forma, en su
  derivada"); R186_045 Lemma 1.1 (log det flow, Hellmann–Feynman); INV_U_001 (U0 entry invisibility PROVED, U2 modulus
  1/log(1/η) PROVED, U3 edge law ARGUED, U4 onset η/log(1/η) ARGUED, U5b C¹ across crossings ARGUED, §3 drift formula
  dλ/dT = −𝒱/T, "a quantity λ·w(T) nondecreasing between crossings is a restatement"); SIGN-REAUDIT I16 (no Grönwall
  by dilation at fixed F: PROVED negative); Paper 46 lem:monoT, lem:contT, lem:flowdet, rem:bar-loc, rem:moriceiling;
  memo A (Thm 1.1, Prop 2.1, Thm 3.1, §3.4, Lemma 4.2), memo D (Thm 2.1), memo E (Thm E.2, Lemma E.4),
  AUDIT_L_SHARP_1 §3 (Slepian identity, ε′(1⁺) = −cΣ(d/dc)log(1−λ_n)), §6.3 ((★★) and the constraint list);
  PATTERN_001 (κ-band, sawtooth), MECH_001 Prop 3.2; AUDIT_ZENODO_FRONTIER B1 (Mori ½log15, CITED, L104).
- **Reason given for looking again (and what it buys).** Every recorded flow attempt differentiates the *bottom* λ
  of a form and compares it with an abstract rate c(T); R186_038 α.3(b) shows that c must be superexponential in T
  because λ decays like exp(−4πe^{2T}), and that the needed virial bound has relative precision λ. Strategy H
  differentiates the **pencil** 𝔐 − κμ^{−A}D, whose subtracted term has an *exactly known* rate (Slepian/band edge),
  in the variable c where that rate is the constant 2 + O(1/c). This removes the quantitative obstruction (b) of
  α.3 — in c, polynomial losses are affordable and the comparison rate is explicit — and leaves only the
  qualitative one. The memo establishes that the qualitative obstruction is intact and is the whole content of
  L′♯ (Theorem H.5). Nothing below is a retry of a sign source; §4–§5 close the class with a written reason.

## 1. The dilated frame (PROVED, elementary)

**1.1 Fixed data, moving band.** For admissible f (even, C², supp ⊂ [−λ,λ], f(0) = f̂(0) = 0, and f(λ) = 0 as in
(★★)) put f(x) = λ^{−1/2}φ(x/λ), i.e. φ(x) := λ^{1/2}f(λx): φ is even, C², supp φ ⊂ [−1,1], φ(0) = φ̂(0) = φ(1) = 0,
‖φ‖ = ‖f‖, and with f̂(ξ) = ∫f e^{−2πixξ} one has f̂(ξ) = λ^{1/2}φ̂(λξ). Substituting η = λξ, the out-of-band set
|ξ| > λ of f is |η| > λ² = μ = c/2π for φ̂, and
  **leak_c(φ) := leak(f) = 2∫_λ^∞|f̂(ξ)|²dξ = 2∫_μ^∞|φ̂(η)|²dη = 2∫_{c/2π}^∞|φ̂(η)|²dη.**
The constraints φ(0) = φ̂(0) = φ(1) = 0 do not involve c. The gauge 𝒢₀ (supp ⊂ [−1/λ,1/λ]) becomes
  𝒢_c := {χ even C², supp χ ⊂ [−1/μ,1/μ], χ(0) = χ̂(0) = 0},  nested: c′ > c ⇒ 𝒢_{c′} ⊂ 𝒢_c,
and ℓ(g) = L_c(φ) := inf_{χ∈𝒢_c} leak_c(φ+χ) (memo A Prop 2.1(c)).

**1.2 The summation image is a fixed function.** With u = e^x, x ∈ I, and y := x − T ∈ (−2T, 0):
  g(x) = (Ef)(e^x) = e^{x/2}Σ_n f(ne^x) = e^{x/2}λ^{−1/2}Σ_n φ(ne^{x−T}) = G_φ(x−T),
  **G_φ(y) := e^{y/2}Σ_{n≥1}φ(ne^y)  (y ∈ ℝ),**
which does not depend on T. G_φ = 0 on [0,∞) (ne^y ≥ 1 and φ(1) = 0 with supp φ ⊂ [−1,1]), G_φ is locally
Lipschitz, G_φ(y) = O(e^{3y/2}) at −∞ (Guo Lemma 4.3, CITED), and by Poisson (φ(0) = φ̂(0) = 0, φ even)
  G_φ(y) = e^{−y/2}Σ_{k≥1}φ̂(ke^{−y}).
In particular the **left-edge value** is the band-edge aliasing sum
  G_φ(−2T) = μ^{1/2}Σ_{k≥1}φ̂(kμ) = μ^{1/2}[φ̂(c/2π) + Σ_{k≥2}φ̂(kc/2π)],
a functional of φ̂ on [c/2π, ∞) (edge included); the tail G_φ|_{(−∞,−2T)} is Z r with r = φ̂·1_{|η|>c/2π}
(memo A Rem (ii)); and the right edge satisfies G_φ(0⁻) = φ(1) = 0, G_φ′(0⁻) = φ′(1).

**1.3 The window form is translation invariant.** W_T(g) = (1/2π)∫Θ|ĝ|² + 2Re(A(g)B̄(g)) − Σ_{n<μ}v_n c_g(log n) on
L²(I) (Paper 46 def:W, Mori's Q). Under g ↦ g(·+T): the archimedean term and the autocorrelations are invariant;
A ↦ e^{T/2}A, B ↦ e^{−T/2}B, so AB̄ is invariant. Hence, writing J_T := (−2T, 0),
  **W_T(Ef) = 𝒲[G_φ·1_{J_T}] =: N(T;φ),**
where 𝒲 is the full-line Weil form of memo A §1 (the comb may be taken complete: c_{G1_J}(log q) = 0 for log q ≥ 2T).
So, for fixed data φ, the window value is the Weil form of a fixed function G_φ truncated to an interval that grows
to the left, and the whole T-dependence of L′♯ sits in (i) the truncation point −2T of N, (ii) the band edge c/2π
of leak_c, (iii) the shrinking gauge 𝒢_c. □

**Definition (pencil bottom).** For κ > 0, A ≥ 0 fixed,
  Q_c(φ) := N(T;φ) − κμ^{−A}L_c(φ),   Δ(c) := inf{Q_c(φ)/‖G_φ1_{J_T}‖² : φ admissible, φ ≠ 0}.
Then L′♯ with (κ, A) ⟺ Δ(c) ≥ 0 for all c ≥ 10π (μ ≥ 5). (The normalisation by ‖g‖² = ‖G_φ1_{J_T}‖² makes
Δ ≤ λ^W_T; by memo A Lemma 4.2, ℓ(g) ≤ C₀μ²‖g‖², so Δ ≥ λ^W_T − κC₀μ^{2−A}.) Δ(c) = inf over the constraint
space 𝒦 of the bottom of 𝔐 − κμ^{−A}D_B relative to the Gram matrix of the E-images, memo A §3.4.

## 2. The base case (PROVED; Mori ½log15 CITED)

**Proposition H.1.** For 5 ≤ μ ≤ 15 and every g ∈ E(core): W_T(g) ≥ 2^{−2904}C₀^{−1}μ^{−2}ℓ(g), C₀ = 4(1/5+4c_B)
the constant of memo A Lemma 4.2. Consequently L′♯ holds on 5 ≤ μ ≤ 15 with A = 2 and any κ ≤ 2^{−2904}/C₀,
and with κ := 2^{−2905}/C₀, A := 2 one has Δ(c) ≥ 2^{−2905} on 10π ≤ c ≤ 30π.
*Proof.* Mori (Zenodo 23281236, Theorem O; AUDIT_ZENODO_FRONTIER B1, index L104, CITED): W_T(g) ≥
2^{−2904}‖g‖² for all C² g supported in I_{½log15}; by lem:monoT this holds for all T ≤ ½log15, i.e. μ ≤ 15. Memo A
Lemma 4.2 (PROVED): ℓ(g) ≤ C₀μ²‖g‖² on the core. Combine. For Δ: Q_c(φ)/‖g‖² ≥ 2^{−2904} − κμ^{−2}C₀μ² = 2^{−2905}. □
This is the initial condition c₀ = 30π of the scheme. It is a trivial consequence of the certificate and records
nothing about uniformity; it is the first explicit instance of L′♯ at any window and is new only as a record.

## 3. Exact rate identities (PROVED)

**Lemma H.2 (leakage rate = band-edge value; rank one).** For fixed admissible φ and c > 0,
  d/dc leak_c(φ) = −(1/π)|φ̂(c/2π)|² ≤ 0.
For χ ∈ 𝒢_c fixed the same holds for leak_c(φ+χ). *Proof.* Differentiate 2∫_{c/2π}^∞|φ̂|²; φ̂ is entire. □
*Check against Slepian (CITED).* For φ = ψ_n(c;·) (prolate on [−1,1], bandwidth c), leak_c(ψ_n) = 1 − λ_n(c) and the
prolate relation ∫_{−1}^1ψ_n(x)e^{−icx}dx = μ_nψ_n(1), |μ_n|² = 2πλ_n/c, give (1−λ_n)′ = −(2/c)λ_nψ_n(1)²: Slepian's
identity (AUDIT_L_SHARP_1 §3) is Lemma H.2 on the prolate basis. The rate −(d/dc)log(1−λ_n) = (2/c)λ_nψ_n(1)²/(1−λ_n)
equals 2 − (n+½)/c + O(c^{−2}) for n ≪ c (from 1−λ_n ≈ K_nc^{n+½}e^{−2c}). **So in the variable c the leakage decays
at the constant rate 2 with a 1/c correction; the polynomial factor c^{n+½} is exactly the kind of loss that the
right-hand side κμ^{−A} of L′♯ absorbs.** (AUDIT_L_SHARP_1 §3 objects reused, not retried.)

**Lemma H.3 (gauge-minimised leakage: one-sided rates).** Let χ*_c ∈ 𝒢̄_c attain L_c(φ) (it exists: closed convex set,
coercive quadratic functional). Then for h > 0:
  L_{c+h}(φ) ≥ inf_{χ∈𝒢̄_c}leak_{c+h}(φ+χ) ≥ L_c(φ) − (2/2π)∫_{c/2π}^{(c+h)/2π}sup_{χ∈𝒢̄_c, leak_c(φ+χ)≤L_c+1}|(φ+χ)^(η)|²dη,
  L_{c−h}(φ) ≤ leak_{c−h}(φ+χ*_c) = L_c(φ) + 2∫_{(c−h)/2π}^{c/2π}|(φ+χ*_c)^|².
Hence D₊L_c ≥ −(1/π)sup|(φ+χ)^(c/2π)|² and D^−L_c ≥ −(1/π)|(φ+χ*_c)^(c/2π)|² (lower Dini bounds), while the
gauge shrink gives no upper bound on D⁺L_c beyond continuity. *Proof.* Nesting 𝒢_{c+h} ⊂ 𝒢_c and monotonicity of
leak in the cutoff. □ *Reading.* For the Grönwall scheme (a lower bound on Δ′) one needs an **upper** bound on the
derivative of the subtracted term κμ^{−A}L_c; the band edge helps (L decreases) and the gauge shrink hurts (L
increases); only the band-edge part is explicit. In the prolate matrix picture this is the statement that D′ is
known (Slepian) while the motion of the gauge subspace B̄ inside the prolate basis is not.

**Theorem H.4 (window-form rate = edge value × odd Weil pairing).** Let φ be admissible and G = G_φ. Put
k(t) := ν(t) − 2cosh(t/2) (ν(t) = e^{−t/2}/(1−e^{−2t}), memo A §1) and define the **odd Weil distribution**
  (W^−G)(b) := ∫_0^∞[G(b−t) − G(b+t)]k(t)dt + Σ_{q≥2}c_q[G(b−log q) − G(b+log q)],  c_q = Λ(q)q^{−1/2},
with G := 0 on [0,∞). Then N(T;φ) is C¹ in T on (½log5, ∞), including at the contact points T = ½log q, and
  **dN/dT = −2·G(−2T)·(W^−G)(−2T).**
*Proof.* By memo A Thm 1.1(c)–(e) applied to Φ = G(·−T) (WG = 0 a.e. by Guo Lemma 4.4, CITED, and W commutes with
translations), N(T) = −𝒲(G1_{J_T}, G1_{(−∞,−2T)}). Writing out 𝒲 (memo A §1) with the two supports disjoint:
  N(T) = ∫∫_{y<−2T<x<0}G(x)G(y)k(x−y)dxdy + Σ_q c_q∫_{−2T}^{min(0,−2T+log q)}G(x)G(x−log q)dx
(the term Φ₂(x+log q) vanishes for x > −2T; the sign conventions are those of memo A: the Lévy cross term enters
with −ν and the pole term with +2cosh, and N = −𝒲(g,Ψ)). Absolute convergence: |G(x)G(y)k(x−y)| ≤ C e^{3y/2}e^{|x−y|/2}
near −∞ and ν(x−y) ≤ 1/|x−y| with G Lipschitz near the diagonal; the q-sum converges by Σc_qq^{−3/2}·sup|G| < ∞ for
the terms with −2T−log q far in the tail. Leibniz in the moving lower limit b = −2T (db/dT = −2) gives
  dN/dT = −2G(b)·{∫_{−∞}^bG(y)k(b−y)dy − ∫_b^0G(x)k(x−b)dx + Σ_q c_q[G(b−log q) − G(b+log q)·1_{log q<2T}]}.
The two integrals are separately log-divergent at the diagonal (k(t) ~ 1/(2t)) but their difference is
∫_0^∞[G(b−t)−G(b+t)]k(t)dt, convergent since G is Lipschitz; the convergence of each ∫_ε and the limit ε → 0 are
justified by dominated convergence, and the Leibniz step is applied to the regularised region |x−y| > ε first. For
log q ≥ 2T the upper limit of the q-term is 0 and does not move, so only the lower limit contributes, which is the
same formula because G(b+log q) = G(−2T+log q) = 0 when −2T+log q ≥ 0. Continuity of the right-hand side in T,
including at 2T = log q (where G(b+log q) → G(0⁻) = 0 from both sides), gives C¹. □

**Corollary H.4′ (how a crossing enters, for fixed data).** At 2T = log q the second derivative jumps:
  [d²N/dT²]_{T=½log q⁺} − [d²N/dT²]_{T=½log q⁻} = 4c_q·G(−log q)·G′(0⁻) = 4c_q·G_φ(−log q)·φ′(1).
*Proof.* The only non-smooth piece is −2c_qG(b)[−G(b+log q)]·1_{log q<2T} whose T-derivative at the crossing is
−2c_qG(b)·(−2)G′(b+log q) → 4c_qG(b)φ′(1) from the right and 0 from the left (b+log q → 0⁻, G′(0⁻) = φ′(1)). □
So, for a fixed test, a crossing is invisible at first order (U0, U5b made PROVED for fixed data) and enters at
second order with the coefficient c_q × (band-edge aliasing value) × φ′(1), whose sign depends on φ, not on q.

**Lemma H.5 (residue-1 cancellation in the derivative; classical, = memo E Lemma E.4 on W^−).** With ψ(t) the
Chebyshev function, Σ_q c_qG(b−log q) = ∫_0^∞G(b−t)e^{−t/2}dψ(e^t) and ∫_0^∞G(b−t)·2cosh(t/2)dt = ∫_0^∞G(b−t)(e^{t/2}+e^{−t/2})dt,
so the main term ∫G(b−t)e^{t/2}dt of the comb (dψ(e^t) ≈ e^tdt) cancels against the pole part of k exactly when the
residue is 1, leaving
  (W^−G)(b) = ∫_0^∞[G(b−t)−G(b+t)]ν(t)dt − ∫_0^∞G(b−t)e^{−t/2}dt + ∫_0^∞G(b+t)·2cosh(t/2)dt + ∫_0^∞G(b−t)e^{−t/2}d(ψ(e^t)−e^t) − G_log(b),
with G_log(b) := Σ_qc_qG(b+log q) = e^{b/2}Σ_{m≥2}(log m)φ(me^b) (memo E Thm E.2, Λ∗1 = log). *Proof.* Rearrangement
of absolutely convergent integrals. □ The derivative therefore has the same architecture as the form itself (memo
B Lemma 3.1 / memo E Lemma E.4): archimedean odd pairing + Chebyshev remainder + collapsed prime term; the pole
and the residue act only through this cancellation. Input (c) of the brief enters here and nowhere else.

**Remark H.6 (symbol of W^−; identity, classical).** On the full line the multiplier of W^− is the odd partner of
the Weil symbol: −2i·Im-part, formally 2Σ_ρ p.v. 1/(τ−γ_ρ) — the Hilbert transform of the zero point masses, which
is a global function, not supported on the zeros. Hence WG = 0 does **not** imply W^−G = 0: the radical of W is not
the radical of W^−, and dN/dT is in general nonzero even though 𝒲(G) = 0. (Consistent with memo A Rem 3.3: no symbol
calculus sees the sign of N, and none sees the sign of N′ either.)

## 4. The Grönwall scheme and its exact closure condition

**4.1 Set-up.** Let φ*_c be a minimiser of Q_c(φ)/‖G_φ1_{J_T}‖² (existence: the pencil is bounded below on the
unit sphere of the window norm and Q_c is weakly lsc on the finite block of memo A §4.4 plus the coercive tail
of Cor 4.3; CONDITIONAL on that compactness argument, not written here). Where Δ is differentiable and the
minimiser is simple, Hellmann–Feynman (lem:flowdet, Paper 46; R186_045 Lemma 1.1) gives
  Δ′(c) = [∂_cQ_c(φ*) − Δ(c)·∂_c‖G_{φ*}1_{J_T}‖²]/‖G_{φ*}1_{J_T}‖²,  ∂_c‖G1_{J_T}‖² = (dT/dc)·2G(−2T)² ≥ 0.
Unconditionally (Danskin), D⁺Δ(c) ≤ that expression evaluated at any minimiser at c: the **easy** direction gives
upper bounds on Δ, in line with lem:monoT and BARRIER_D2 Thm 2 ("segments give only upper bounds"). The Grönwall
direction needs the lower Dini derivative, i.e. continuity of minimisers in c (ARGUED; lem:contT gives it for λ^W).

**4.2 The differential inequality.** Write ρ_N(c) := −∂_c log N(T;φ*) and ρ_L(c) := −∂_c log L_c(φ*) (rates at the
minimiser; by Lemma H.2 and the prolate expansion, ρ_L = 2 − (k+½)/c + (gauge/mixing corrections) when φ* sits on
the k-th prolate, and by Theorem H.4, ρ_N = 2G(−2T)(W^−G)(−2T)·(dT/dc)/N). Using (κμ^{−A})′/(κμ^{−A}) = −A/c:
  ∂_cQ_c(φ*) = −ρ_N N + (ρ_L + A/c)κμ^{−A}L  (all at φ*).
With Q = N − κμ^{−A}L this is
  **∂_cQ_c(φ*) = −ρ_N·Q + (ρ_L − ρ_N + A/c)·κμ^{−A}L(φ*).**   (H-ODE)
So the scheme Δ′ ≥ −Φ(c)Δ − Ψ(c) holds with Φ = ρ_N + 2G(−2T)²(dT/dc)/‖g*‖² and Ψ = 0 **if and only if**
  **(H)   ρ_N(c) ≤ ρ_L(c) + A/c   at the minimiser φ*_c,**
and then Δ(c) ≥ Δ(c₀)exp(−∫_{c₀}^cΦ). Positivity for all c follows if additionally ∫Φ < ∞ on every finite range,
i.e. ρ_N locally integrable — which (H) itself guarantees whenever ρ_L is (it is, between contacts, Lemma H.2).

**Theorem H.5 (closure ⟺ restatement; PROVED).** Under the standing regularity (4.1):
(i) If (H) holds on [c₀, ∞) with c₀ = 30π, then Δ > 0 on [c₀, ∞), hence L′♯ (with the same κ, A as in Prop H.1).
(ii) (H) is not necessary: L′♯ with (κ, A) does not force (H) pointwise. Indeed (H-ODE) only says that where (H)
fails, Q decreases faster than the rate ρ_N allows, which is compatible with Q > 0 as long as the failure set is
short; and L′♯ with (κ,A) implies Q^{(κ′,A′)} ≥ (κμ^{−A} − κ′μ^{−A′})L > 0 for κ′ < κ, A′ > A without any
derivative information. So **(H) ⇒ L′♯ (PROVED, modulo 4.1); L′♯ ⇏ (H).** What is equivalent to L′♯ is the
integrated form of (H-ODE), Q_c(φ*_c) ≥ 0 for all c, i.e. a restatement with no gain.
*Proof.* (i): (H) and (H-ODE) give ∂_cQ(φ*) ≥ −ρ_N Q, i.e. Δ′ ≥ −ΦΔ, and Grönwall from Δ(c₀) ≥ 2^{−2905} (Prop H.1).
(ii): as stated. □

**4.3 What (H) says, and why it is the recorded wall.** By Theorem H.4 and Lemma H.2 at the minimiser,
  ρ_N = 2G*(−2T)·(W^−G*)(−2T)·(dT/dc)/N(φ*),   ρ_L = (1/π)|(φ*+χ*)^(c/2π)|²/L(φ*) − (gauge-shrink rate ≥ 0 in the
  worst case; Lemma H.3).
Three observations, each PROVED from the identities above:
(a) **Both sides are functionals of the minimiser.** ρ_L is explicit once φ* is known (band-edge value over leakage);
   ρ_N is the odd Weil pairing at the edge, normalised by the form value. (H) is an inequality between two
   numbers attached to φ*_c; there is no term in it that is a property of the comb or of the archimedean kernel
   alone. This is the W-lin / lem:flowdet wall: "every first-order discriminant is a functional of h*, not of σ".
(b) **The target rate is pinned by Slepian, the virial is not.** ρ_L = 2 − (k+½)/c + O(c^{−2}) if the gauge-optimal
   representative is a single prolate of index k (NUMÉRICO: k = 4 at the bottom, PATTERN_001; the gauge mixing is
   not controlled). So (H) reads: the window form at its own minimiser must decay in c **no faster than**
   e^{−2c}c^{k+½+A}. Compare R186_038 Lemma α.3: Grönwall on λ_A ⟺ 𝒱_T(h*) ≤ Tc(T)λ_A(T); there c(T) had to be
   superexponential in T and the statement was "the same cancellation of the form, in its derivative". Here the
   change of variable T ↦ c and the subtraction of the leakage make the required c(T) explicit and tame
   (ρ_N ≤ 2 + O(1/c)), so α.3(b) no longer bites. But α.3(a)/(d) do: ρ_N ≤ 2 + B/c is a statement about the virial
   of the minimiser, 𝒱(h*) = −T dλ/dT = T·ρ_N·λ·(dc/dT), with **relative precision O(1/c)**, since ρ_N and ρ_L
   both equal 2 to leading order and the inequality lives in the 1/c term. The archimedean part of the virial is
   O(1) positive (R186_038 α.3(d)) and the comb part must cancel it to the margin — the cancellation of the form
   reappears in its derivative, now at relative order 1/c of the rate rather than at absolute order λ. No input
   in (a) Slepian, (b) crossing law, (c) residue cancellation bounds ρ_N: (a) is on the other side of (H), (c) is
   an identity inside W^− (Lemma H.5), (b) is examined next.
(c) **Crossings cannot drive (H).** Between contacts the comb is frozen (PATTERN_001 §1, PROVED) and (H) is a
   statement about a C¹ function. At a contact 2T = log q: Δ is continuous (U0: the new term −v_qc_g(log q) vanishes
   at entry, PROVED); for fixed data N is C¹ and the crossing is a second-order event with coefficient
   c_q·G_φ(−log q)·φ′(1) (Cor H.4′), whose sign is that of G_φ(−log q)φ′(1) — a property of the test, the same for
   Λ, cΛ, deleted primes, and for a Beurling crossing at its own position; at the minimiser the germ is
   −v_q·a₊a₋·2η/log(κ/2η) (U4, ARGUED), again a functional of h*. The ℤ-specific content of the crossings is their
   *position*; (H) uses positions only as the set where the C¹ function ρ_N may have a 1/log singularity in its
   derivative. **An inequality on ρ_N that holds between contacts for one comb holds verbatim for a comb with the
   same frozen part and different future contacts** (the derivative identity of Thm H.4 is pointwise in T and sees
   only q with log q ≤ 2T through G(b+log q), and all q through G(b−log q) in the tail — the tail term
   Σ_qc_qG(b−log q) is the only place where future primes appear, through Z r on (−∞,−2T): it is TV-continuous in
   the comb with modulus ‖Zr‖_∞Σ|δc_q|q^{−3/2}·… = polynomial in μ, not e^{−2c}). So any proof of (H) must
   produce the 1/c precision from the tail pairing, with an input that is not TV-robust at scale e^{−2c}
   (B Lemma 4.1 transported to the derivative: the δ_{u₀}-perturbation of the comb changes ρ_N by
   m·|c′_{g*}(u₀)|/N ≍ m·e^{+2c}·poly, so (H) for Λ is at distance m ≍ e^{−2c} from failure in TV). The crossing
   *positions* are therefore not the lever: the lever would be the tail pairing at the e^{−2c} scale, which is
   (★★) again.

**The inequality needed at the crossings, exactly (answer to (iii)).** Let T_q = ½log q, η ∈ (0, gap). Then
  Δ(T_q+η) − Δ(T_q) = ∫_{T_q}^{T_q+η}[frozen-comb drift](T)dT − v_q·c_{g*_T}(log q)|_{T=T_q+η} + o(·),
and Grönwall with the polynomial budget μ^{−A} over the ≈ μ/log μ contacts below μ allows a *relative* loss per
contact of at most O(A log²μ/μ) on average. Hence what is needed at each contact is
  **(H_q)   v_q·sup_{0<η<gap} |c_{g*_{T_q+η}}(log q)| ≤ C·(log²μ/μ)·λ^W_{T_q}·(1+o(1)),**
i.e. the autocorrelation of the minimiser at the new lag must be of the size of the bottom itself times
log²μ/μ (equivalently, by INV_U U2, the product of the edge masses of g* on [−T,−T+2η] and [T−2η,T] must be
≲ λ^W·log²μ/(μ v_q·log(1/η))). Since the left-edge value of any E-image is the band-edge aliasing
G(−2T) = μ^{1/2}Σ_kφ̂(kμ) (§1.2) — of the size √(leakage)·poly for a prolate — while the right-edge slope is
φ′(1) = O(1), (H_q) demands either that the right edge of the minimiser also carries e^{−c}-small mass at
resolution η, or an internal cancellation in c_{g*}(log q). Neither is implied by any PROVED statement in the
corpus; the numerically observed sawtooth (κ drops 8–15% at each contact, PATTERN_001 §2, NUMÉRICO) says the
loss per contact is O(1) relative, *not* O(log²μ/μ), and is compensated by the between-contact drift (κ rising).
**So the Grönwall scheme with Ψ ≡ 0 is falsified at the level of the available data** unless the between-contact
gain is included — and that gain is −(ρ_N − ρ_L) < 0 between contacts, again a virial statement at the minimiser.

## 5. Falsifier test (constraint (iv)) and class verdict

| step | cΛ (c>1) | a_P | Beurling | F-DH | verdict |
|---|---|---|---|---|---|
| §1 dilated frame, G_φ fixed, N translation invariant | YES (E_c, d_c) | YES | YES (E_B) | YES (conductor-rescaled) | generic |
| Prop H.1 base case | holds only where the comb is certified positive (T ≤ ½log2 for every comb; cΛ negative at T = 1, certified) | — | — | — | base is a certificate, comb-specific by data |
| Lemma H.2 band-edge rate | YES | YES | YES | YES | archimedean, generic |
| Thm H.4 derivative identity | YES (comb c·c_q) | YES | YES (comb of B-primes) | YES | generic (uses only WG = 0, which holds for every Dirichlet series with its own E) |
| Lemma H.5 residue cancellation | leftover (1−c)-term | leftover | leftover | no pole: no cancellation | selects residue 1, in the derivative as in the form |
| (H) at the minimiser | FALSE on some interval in (½log2, 1): Δ_{cΛ} passes from ≥ 0 to < 0 (CERT_FALSIFIERS, PROVED), so ρ_N must exceed any integrable bound there | FALSE likewise | FALSE (NUMÉRICO) | FALSE (Ziad, UNVERIFIED) | the Λ-step |

Conclusion (PROVED by the table): every identity of this memo is generic; (H) is the Λ-step and is exactly as
non-robust as (★★) (its TV-distance to failure is e^{−2c}, §4.3(c)). The differential formulation does not change
which object carries the sign; it changes the variable in which the margin is measured (relative rate instead of
absolute value) and shows that the margin there is O(1/c) in the rate — a polynomial, not doubly-exponential,
margin, which is the correct quantitative shape (AUDIT_L_SHARP_1 §4.3(b): the exterior carrier has only a
polynomial relative margin) — without providing it.

**Class NO-GO (𝒦_H).** Differential inequalities in T or c for the bottom of the window form, of the pencil
𝔐 − κμ^{−A}D, or of any ratio Δ/‖D‖, whose coefficients are evaluated at the minimiser and whose inputs are
(a) Slepian/band-edge rates, (b) crossing positions and the onset law, (c) residue cancellation, (d) TV-robust
bounds on the tail pairing. Reason: by Theorem H.5 and §4.3, closure ⟺ (H), a virial inequality at the minimiser
with relative precision O(1/c), which is a functional of h* (W-lin/flowdet), is not implied by (a)–(c), and is
excluded from (d) by the transported barrier. This subsumes R186_038 α.3 (same wall, there in the variable T with
an abstract comparison), SIGN-REAUDIT I16 (fixed-test Grönwall: here Theorem H.4 shows the fixed-test derivative
is −2G(−2T)(W^−G)(−2T), of size √(leakage)·√μ, i.e. no Grönwall at fixed test at scale e^{−2c}), and INV_U §3
("λ·w(T) nondecreasing is a restatement"). What is **new** in the record: the dilated frame (§1), the band-edge
rank-one rate (Lemma H.2), the odd Weil distribution W^− and the derivative identity (Thm H.4), the second-order
crossing law for fixed data (Cor H.4′), the exact closure condition (H) with its O(1/c) relative precision, and
the explicit crossing requirement (H_q). None is a sign source.

## 6. Labels and verdict
- **PROVED:** §1 (dilated frame, G_φ fixed, N translation invariant, left-edge value = band-edge aliasing), Prop
  H.1 (base case, given Mori CITED), Lemma H.2 (and its agreement with Slepian), Lemma H.3 (Dini bounds), Theorem
  H.4 (derivative identity, C¹ across crossings for fixed data), Cor H.4′, Lemma H.5 (classical), Rem H.6
  (identity), (H-ODE), Theorem H.5(i) (modulo 4.1), the correction in H.5(ii) that (H) is sufficient and not
  equivalent, §4.3(a)–(c) as stated, the table of §5.
- **CITED:** Mori ½log15 (L104), Guo Lemmas 4.3–4.4, Slepian's identity, Paper 46 lem:monoT, lem:contT,
  lem:flowdet, memo A Thm 1.1 / Lemma 4.2 / Prop 2.1, memo E Thm E.2 / Lemma E.4, INV_U U0/U2, CERT_FALSIFIERS_001.
- **CONDITIONAL:** existence/simplicity/continuity of the pencil minimiser (4.1); Hellmann–Feynman for Δ.
- **ARGUED:** ρ_L = 2 − (k+½)/c at the bottom (gauge mixing uncontrolled); the edge germ at the minimiser (U4);
  the reading of the sawtooth as an O(1) relative loss per contact (NUMÉRICO source).
- **OPEN:** (H); (H_q); L′♯ / (★★). No sign is claimed. Row D OPEN.
- **NO-GO (class 𝒦_H):** Strategy H as a Grönwall/continuation argument in T or c. Do not retry with another
  comparison functional (any D-like or ‖D‖-like denominator) unless an independent bound on the virial of the
  minimiser at relative precision O(1/c), or on the edge autocorrelation c_{g*}(log q) at scale λ^W·log²μ/μ, is
  first proved; that bound is the Λ-step itself.

**Verdict.** In the variable c the window form and the leakage both decay at rate 2, so the pencil's ratio to the
leakage satisfies a tame ODE whose forcing is the mismatch ρ_N − ρ_L of the two rates at the minimiser; Slepian
fixes ρ_L to O(c^{−2}), the odd Weil pairing gives ρ_N exactly, and L′♯ would follow from ρ_N ≤ ρ_L + A/c. That
inequality is a virial bound of relative precision 1/c on the minimiser, carried by the tail pairing at the
e^{−2c} scale; the crossings enter at second order with sign-indefinite coefficients and cannot supply it.
Strategy H is closed as a class with the objects above recorded for REF-D. Row D OPEN.
