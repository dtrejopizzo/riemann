# R162_501 — V: the sign of the virial form on the first-contact kernel

Round 6, mechanism V. Follows R162_407 (Thm 3.2, Cor 3.3), R162_408, R162_102.

**Status: NO-GO for the sign. PROVED: a Selberg–virial identity (Thm 2.2) in which Λ*1=log enters
the value of 𝒱|_N through W = μ*log² = Λlog + Λ*Λ, combined with the kernel equation.**
DH filter: passed at a single line (coefficient sign of W). F3 is only partly passed: the argument does
not break for finite modifications a = Λ+η with η ≥ 0. No sign of 𝒱 on N follows.
Gate 1: OPEN. Row D: OPEN.

Notation is that of R162_407. X := e^{2T_*}, I := I_{T_*}, and G ∈ N = ker H_{T_*} (primitive parity)
is real, with ‖G‖ = 1.
- z_c(τ) := Σ_{n<X} Λ(n) n^{−1/2−iτ}, and z := 2 Re z_c = Σ v_n cos(τ log n) (the comb symbol).
- s = m − z, with m(τ) = Re ψ(¼+iτ/2) − log π.
- Kernel equation in full-line form: (M − Z)G = r_G + h_G, where r_G ∈ span{e^{±t/2}}·1_I (Tate vector)
  and h_G := 1_{ℝ∖I}(M−Z)G (exterior leakage). Paper 47 eq:localweak gives exactly this.
- (REG) as in R162_407 §3. We assume it throughout, as Thm 3.2 there does.

## 0. Corpus check

- R162_407 (3.1): 𝒱 = arch − Σ v_n log n c_G'(log n) + 2⟨G, t r_G'⟩. Cor 3.3: (LB) at o(δ) ⟺ 𝒱|_N ≤ 0.
  Thm 3.2 already gives 𝒱(G) = max_N 𝒱 ≥ 0. So what is needed is 𝒱 ≡ 0 on the top eigenvector.
- R162_205 (four-block Green law) and R162_206 (antisymmetric exterior correlation): the leakage term
  in Thm 2.2 below is of that type. This is not new. What is new is how it is reached.
- R162_401 ([X,S_N] = −K_N, log channel) is the closest earlier item: it used the log weight as a
  commutator. It did not use Selberg's identity Λlog + Λ*Λ = μ*log², which converts the log weight
  into a *square of the comb*. The kernel equation can then absorb that square. I found no corpus
  entry using μ*log² (grep over phases 150–162 and Paper 47: none).
- R160 NG-F1 (smoothness, not multiplicativity, decides localized signs) is confirmed again in §3.

## 1. The virial as a symbol derivative (PROVED)

**Lemma 1.1.** Under (REG), for G ∈ N,

    𝒱(G) = (1/2π)∫ τ s'(τ)|Ĝ(τ)|² dτ + 2⟨G, t r_G'⟩
         = (1/2π)∫ τ m'(τ)|Ĝ|² − (1/2π)∫ τ z'(τ)|Ĝ|² + 2⟨G, t r_G'⟩.                          (1.1)

*Proof.* We have c_G'(u) = −(1/2π)∫ τ sin(τu)|Ĝ|², and z'(τ) = −Σ v_n log n sin(τ log n). Hence
−Σ v_n log n c_G'(log n) = −(1/2π)∫ τ z'|Ĝ|². This is the comb term of R162_407 (3.1). ∎

**Lemma 1.2 (archimedean virial).**

    τ m'(τ) = Σ_{k≥0} 2y²(k+¼)/((k+¼)²+y²)²,  with y = τ/2.

Consequently τm' > 0 for τ ≠ 0, τm'(0) = 0, τm' → 1 as |τ| → ∞, and τm' is bounded. So the
archimedean virial lies in (0, C_m], and it tends to ‖G‖² when G has high-frequency mass.

*Proof.* Differentiate the series in the proof of lem:mbounds(i) term by term. The limit is the
Riemann sum of ∫_0^∞ 2y²x/(x²+y²)² dx = 1. ∎

So the sign problem is entirely in the comb term and the Tate term. (1.1) alone is weight-blind.

## 2. Selberg–virial identity: Λ*1 = log enters the value (PROVED)

**Lemma 2.1 (Selberg identity, from Λ*1 = log).** Put W := μ*log². Then

    Λ·log + Λ*Λ = W.

*Proof.* log is a derivation for Dirichlet convolution: (f*g)log = (f log)*g + f*(g log).
Multiply Λ*1 = log by log. This gives (Λlog)*1 + Λ*log = log². Now Λ*log = Λ*Λ*1, again by
Λ*1 = log. Möbius inversion finishes the proof. ∎

For a general weight a (a(1) = 0) the same computation gives a·log + a*a = μ*((a*1)·log) + E_a, with
an error E_a that vanishes iff a*1 = log on the relevant range. For the DH coefficients c (defined
by −L'/L = Σc n^{−s}, with L = Σ α(n)n^{−s}) the analogue is c·log + c*c = α^{−1}*(α log²) =: W_DH.
The facts that distinguish W from every other W_a are:
- (W1) W ≥ 0;
- (W2) supp W ⊂ {n : ω(n) ≤ 2};
- (W3) W(p^k) = (2k−1)log²p, and W(p^i q^j) = 2 log p log q.

**Theorem 2.2 (Selberg–virial identity on N).** Assume (REG), and put Y(τ) := Σ_{n<X} W(n)n^{−1/2−iτ}.
Then, for every G ∈ N,

    𝒱(G) = (1/2π)∫ τ m'|Ĝ|²                                     (archimedean, > 0)
          − (1/π)∫ τ Im Y(τ)|Ĝ|²                                 (Selberg term, see (2.3))
          + (1/π)∫ τ m(τ) Im z_c(τ)|Ĝ|²                           (arch × odd comb)
          − (1/π) Re∫ τ Im z_c(τ) Ĝ(τ)‾ (r̂_G + ĥ_G)(τ) dτ          (Tate + exterior leakage)
          + 2⟨G, t r_G'⟩.                                                                   (2.1)

In the (2.1) Selberg term:

    −(1/π)∫ τ Im Y |Ĝ|² = −2 Σ_{n<X} W(n) n^{−1/2} c_G'(log n).                              (2.3)

*Proof.*
1. Differentiate: dz_c/dτ = −i Σ Λ(n)log n · n^{−1/2−iτ}.
2. By Lemma 2.1 restricted to n < X, Σ_{n<X}Λ log n · n^{−1/2−iτ} = Y − (z_c² − R_X). Here
   R_X := Σ_{m,k<X, mk≥X} Λ(m)Λ(k)(mk)^{−1/2−iτ} collects the product terms with n ≥ X. The divisors
   of n < X are < X, so the truncated Λ*Λ is exactly z_c² − R_X.
3. So z' = 2Re(dz_c/dτ) = 2 Im Y − 2 Im(z_c²) + 2 Im R_X, and Im(z_c²) = z·Im z_c.
4. The R_X term only contains frequencies log n ≥ 2T_*. Against |Ĝ|² these give c_G'(log n), which
   is 0 for log n > 2T_* because supp c_G ⊂ [−2T_*, 2T_*]. At log n = 2T_* (regime II) we get
   c_G'(2T_*) = ∓G(T_*−)G(−T_*+). This is 0 by R162_408 Prop 4.1 under its regularity hypothesis;
   under (REG) alone the term is kept inside ĥ_G below. So −(1/2π)∫τ z'|Ĝ|² = −(1/π)∫τ Im Y|Ĝ|² +
   (1/π)∫ τ Im z_c · z|Ĝ|².
5. Kernel substitution: zĜ = mĜ − r̂_G − ĥ_G (Fourier transform of the full-line kernel equation).
   The symbols τ Im z_c and z are real, so ∫τ Im z_c z|Ĝ|² = Re∫ τ Im z_c Ĝ‾(zĜ). Substituting and
   inserting into (1.1) gives (2.1).
6. (2.3): the same computation as Lemma 1.1, with v_n log n replaced by 2W(n)n^{−1/2}. ∎

**What is new.** In (1.1) the comb virial carries the weight Λ(n)log n, which is weight-blind: it is
defined for every a. In (2.1) half of that weight, Λ*Λ, is a square of the comb. The kernel equation
turns the square into archimedean data plus Tate/leakage. What remains is W = μ*log², which is where
Λ*1 = log enters the value. For eigenvectors with λ ≠ 0 the substitution in step 5 produces an extra
term +(λ/π)∫τ Im z_c|Ĝ|². So (2.1) is λ=0-specific in the F1 sense. It is only additively so, though
(compare R162_407 Prop 4.2).

## 3. The sign: NO-GO

**DH-FILTER LINE (mandatory).** The formal identity (2.1) holds for every weight a, with W replaced
by W_a := a·log + a*a (this is the defining equation of W_a, so steps 1–5 go through verbatim). Hence:
- for DH, the argument breaks **only** at a line that uses (W1), (W2) or (W3) of W. For example
  "W ≥ 0" fails for W_DH, since W_DH(p) = c(p)log p and DH has c(p) < 0 for some p;
- for a = Λ + η with η ≥ 0 supported below X, W_a = W + η log + 2Λ*η + η*η ≥ 0. So (W1) survives,
  and **a (W1)-based argument does not break. It fails F3.**
Only (W2) or (W3) (support on ω ≤ 2 with exact values) is broken by all finite modifications. But
at a fixed T_* those are finitely many numbers, and they are equivalent to knowing Λ|_{n<X}.

**Proposition 3.1 (no sign from (2.1)).** None of the four non-archimedean terms of (2.1) has a
determined sign on N, and neither does their sum, from (W1)–(W3) alone:
- (a) The Selberg term is −2Σ W(n)n^{−1/2}c_G'(log n). By (W1) its sign is that of −c_G' on the comb.
  The autocorrelation c_G of a real function is even, and c_G(0) = 1 is its maximum. So c_G' ≤ 0 is
  forced only near 0⁺. At u = log n ≥ log 2, c_G' is unconstrained for real G ∈ L²(I). More precisely,
  the map G ↦ (c_G'(log n))_{n<X} restricted to any subspace of codimension < #{n<X} is onto an open
  cone containing vectors of both signs (Müntz/Kronecker argument as in R162_408 Prop 5.1: the log n
  are ℚ-independent over primes). Since N is an arbitrary finite-dimensional space from the viewpoint
  of these inequalities, W ≥ 0 gives nothing.
- (b) The arch × odd-comb term ∫τ m Im z_c|Ĝ|² = −Σ Λ(n)n^{−1/2}·(1/2π)∫τ m sin(τ log n)|Ĝ|² is again
  a comb of derivatives, now of the m-weighted autocorrelation. There is no sign, for the same reason.
- (c) The leakage term is the antisymmetric exterior correlation of R162_205/206: it changes sign
  under G ↦ −G on one half of the exterior pairing. R162_205 showed that sign cannot be
  manufactured by substitution. (2.1) is one more substitution.
- (d) Iterating: one can apply Lemma 2.1 again to the log-weight hidden in m (the Gamma analogue
  ψ' of Λ log). This reproduces the Hadamard/Pohozaev form of the virial, 𝒱(G) = edge flux of G,
  which is ≥ 0 and weight-blind (the log-Laplacian Pohozaev identity has boundary term ∝ ∫_{∂I}(edge
  germ)²; this matches R162_408 κ'). The second substitution therefore undoes the arithmetic. It is
  the continuum cancellation of R162_305 once more.

*Proof of the shape of (d) (sketch, NOT fully checked).* By Lemma 1.2, τm' = 1 − ρ(τ) with
ρ ∈ L¹ ∩ L^∞. The log-part (symbol log|τ|) has dilation commutator exactly the identity, and the
compression to I produces the Chen–Weth-type boundary term. The ρ-part and the comb are bounded
perturbations whose commutators are integral operators. None of this sees W. ∎

**Verdict.**
- Theorem 2.2 is the requested identity: Λ*1 = log enters the value of 𝒱|_N through W = μ*log² after
  the kernel equation eats the Λ*Λ square.
- Deciding the sign needs a positivity statement about Σ_{n<X} W(n)n^{−1/2}c_G'(log n) on N. By
  Prop 3.1(a) such a statement cannot follow from W ≥ 0. Any version using (W2)/(W3) is a statement
  about finitely many numbers at each T_*, and it would have to be uniform in T_* (Thm finZ: row D is
  intrinsically infinite).
- The only surviving formulation, stated for the record:

  **(S-W)** For G ∈ N_{T_*}: Σ_{n<X} W(n)n^{−1/2}c_G'(log n) ≥ ½·[arch + arch×odd + leakage + Tate]
  of (2.1).

  (S-W) is equivalent to 𝒱|_N ≤ 0, i.e. to Cor 3.3 of R162_407. It is a reformulation, not progress.

Falsifiers:
- F1: (2.1) differs from the positive-window identity only by λ∫τ Im z_c|Ĝ|². Additive, so no
  separation (NO-GO consistent with R162_407 Prop 4.1–4.2).
- F2: (2.1) is quadratic in G, and orientation-blind.
- F3: DH breaks only at (W1). Finite η ≥ 0 modifications do not break it. **FAIL** for any (W1)-based
  sign.
- F4: not applicable (no graph limit).

GATE 1: OPEN. Row D: OPEN. Numerics: none used. Files edited: this file only.
