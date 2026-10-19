# R162_2202 — Round 22: the node system of the witness under the Euler operator — **PARTIAL (node identity PROVED, new) + NO-GO (PROVED) for Euler self-similarity**

*Cell: 8B/6C boundary (object = the zero set X of F̂ of the witness, column B; arithmetic = exact values of Λ through
Z, row 6). Nearest record routes: R160_X_C1 Thm G (8B, "Blaschke-rigid witness", grid §7 rank 4), R162_1502 Prop 3,
R162_903 Thm 3.2, R162_1001 Thm 3.1. Walls named in advance: W3 (F3 class-blindness) and W1 (E1, Herglotz/de Branges).
Conventions: P47 `eq:symbol` (σ_T = m − Σ_{n∈N_T} v_n cos(τ log n), v_n = 2Λ(n)n^{−1/2}), R160_X_C1 §1, §5
(μ = σ_{T_c}dτ/2π + δ_{−i/2} + δ_{i/2}, Ĥ_x = F̂/(z−x)), R162_1502 (Z = M(1), a′ = exp_*(a/log)). [compl] unless
stated. Pure mathematics, no numerics. No sign for ζ is claimed. No label moves. Gate 1 stays OPEN.*

---

## 0. Corpus check

Grep over 03-research and 04-papers: "Christoffel" (hits only phase-78 LP autopsies, a different object),
"Hermite–Biehler" (phase-21-negative-directions-geometry exclusion principle, phase-136 maps: de Branges wall, not node weights), "node", "Gauss-node",
"quadrature" (R160_X_C1 Thm G only), "self-similar", "descent" (no node-level use). Not found: a closed formula for
the Gauss weights w_x, a prime-by-prime kernel for them, or any action of Z / Euler factors on the zero set of a
first-contact vector. §2 (Theorem NI) and §4 (Theorem ND) are new; §3 is transport of structure and is recorded only
so that it is not rebuilt.

## 1. Failing lines, stated first (rule §0.4 of the master grid)

The proposed forcing step is: "the Möbius/Euler conjugation of the node system satisfies the *same* quadrature, so the
node system is self-similar under the Euler operator, which forces an infinite descending tower incompatible with
type T_c and density T_c/π". It must fail for Λχ₂ and for the two-atom Type I curve. It does — but it fails for
**every** datum, including ζ:

| model | node identity (Thm NI) | ascent/transport (Prop T) | descent (Thm ND) | first contact with a Gauss-node witness |
|---|---|---|---|---|
| Λχ₂ | holds verbatim with v_n → 2Λ(n)χ₂(n)n^{−1/2}; in conjugated form a′ = χ₂, conjugator Z_χ | holds with D_χ | impossible (no Euler-factor divisor) | yes (R160_X_C1 χ) |
| two-atom s₂δ_{log2}+s₃δ_{log3} (R162_2001) | holds with the two atoms; a′ = exp_*(a/log) | holds | impossible | yes, including a Type I contact at s₂^c |
| deletion, κ, DH, Epstein, Ξ_a | holds with own symbol/polar set | holds | impossible | yes (where the form goes negative) |
| ζ | holds; a′ ≡ 1, conjugator Z | holds | impossible | hypothetical (¬RH) |

So the self-similarity step fails for Λχ₂ and for the Type I curve, as it must, **and it does not force anything for
ζ**. Theorem ND shows that Euler descent is excluded by the class-level Theorem R alone, and Prop T shows that ascent
is a tautology. Neither step reads a′ ≡ 1. This is W3 again, and Thm 6 of R162_1502 ("a′ is inert") now holds at node
level.

## 2. Theorem NI (exact node identity; Christoffel form). PROVED, [compl]

Setting: ¬RH, T_c < ∞, F ∈ E_c real and even (F̂ real and even on ℝ; the odd case only changes signs), x a simple
real zero of F̂. Put

  L(y) := ∫ Ĥ_y^#(p) dμ(p) = ∫ F̂^#(p)/(p−y) dμ(p)   (absolutely convergent at nodes y = x).

**Theorem NI.** (a) d_x = W(H_x) = F̂′(x)·L(x); hence w_x = d_x/F̂′(x)² = L(x)/F̂′(x).
(b) Explicitly, with k_F(x,u) := ∫_u^{T_c} F(s) sin(x(s−u)) ds,

  w_x F̂′(x) = 𝔄_F(x) + Σ_{n ≥ 2, log n < T_c} (2Λ(n)/√n) k_F(x, log n) − 2A(F) x/(x²+¼),
  𝔄_F(x) := (1/2π)∫ m(τ) F̂(τ)/(τ−x) dτ.

Only the prime powers n < e^{T_c} = X^{1/2} enter. The contacts in [T_c, 2T_c) do not appear at node level.
(c) For every y ∉ ℝ, Ψ(y) := ∫ F̂F̂^#/(p−y) dμ = F̂(y) L(y). The Hilbert law G(e) is Ψ(x) = 0, which is automatic.

*Proof.* (a) Write Ĥ_x(p) = F̂′(x) + (p−x)K(p) with K := (Ĥ_x − F̂′(x))/(z−x). K is entire and of type ≤ T_c. On ℝ,
K = O(|F̂|/τ² + 1/τ), so K ∈ PW_{T_c} ∩ 𝒟. Since (p−x)Ĥ_x^# = F̂^#,
W(H_x,H_x) = ∫Ĥ_xĤ_x^#dμ = F̂′(x)∫Ĥ_x^#dμ + ∫K F̂^#dμ = F̂′(x)L(x) + W(K,F), and W(K,F) = 0 because F is in the kernel.
The integral L(x) converges absolutely: Ĥ_x = O(|F̂|/|τ|) and ∫|F̂| log(2+|τ|)/(1+|τ|) < ∞ by Cauchy–Schwarz.
(b) Invert (z−x)Ĥ = F̂: F = iH′ − xH, so H_x(t) = −ie^{−ixt}∫_{−T_c}^t F(s)e^{ixs}ds. H_x vanishes at ±T_c because
F̂(x) = 0, and then H_x(u) = ie^{−ixu}∫_u^{T_c}F(s)e^{ixs}ds. For even F this gives (1/2π)∫Ĥ_x(τ)cos(τu)dτ =
½(H_x(u)+H_x(−u)) = −k_F(x,u), with k_F = 0 for u ≥ T_c since supp H_x ⊂ I_{T_c}. The comb term of σ enters with the
factor −v_n, which gives +v_n k_F. For the polar term, Ĥ_x^#(−i/2)+Ĥ_x^#(i/2) = −[A/(x−i/2)+B/(x+i/2)], which is
−2Ax/(x²+¼) when A = B.
(c) Split F̂(p)/(p−y) = F̂(y)/(p−y) + H⁰_y(p) with H⁰_y ∈ 𝒟, and use W(H⁰_y,F) = 0. ∎

**Reading.**
- NI is the Christoffel/Gauss formula (weight = second-kind function / derivative) for the indefinite measure μ, and it
  is exact at λ = 0. Against λ > 0 the extra term λ⟨K,F⟩ appears, so NI uses the kernel non-perturbatively (S1 holds).
- w_x is homogeneous of degree 0 and nonlinear in F (a ratio), so S2 holds at the level of the object.
- The arithmetic enters only linearly in Λ, through k_F(x, log n). In conjugated form (R162_1502 Lemma 1/Prop 3,
  Λ = log*μ): Σ_n v_n k_F(x,log n) = −(Z X Z⁻¹ g_x)(0)-type expressions with g_x the reflected H_x. The general datum
  gives the same expression with Z_{a′}. The conjugator is therefore the only place where a′ ≡ 1 appears, and the
  identity is an identity for every a′.

**Corollary NI.1 (interlacing; class-level).** Since w_x ≥ 0 and F̂′ alternates in sign on consecutive simple real
zeros, L alternates there too. L has a zero strictly between consecutive nodes x < x′ with w_x w_{x′} > 0. By
Thm G(c) this holds for all but ≤ 2(dim E_c − 1) gaps. PROVED. It is W1 if promoted to a criterion: interlacing of
(F̂, L) is the Hermite–Biehler/de Branges condition, which is E1.

## 3. Prop T (ascent is transport of structure). PROVED, class-level

Let D(z) = Σ_{n≤N} b_n n^{iz} (b_1 ≠ 0) have no real zero; untruncated M(b) is the Fourier multiplier D. Then
Ĝ ↦ DĜ maps PW_{T} isometrically, for the datum ν_D := ν/|D|² (with the same polar set, weights rescaled by
1/(D(a)D^#(a))), onto D·PW_T ⊂ PW_{T+log N}. The node system {x}, the weights w_x and the Hilbert law of F transport
to DF̂ with nodes X ∪ Z_ℝ(D) = X, **for every datum and every D**. For ζ the choice D = partial sums of Z = M(1) is
allowed, and so is D_χ for Λχ₂.
*Proof.* Translation-invariant multipliers commute; |D| ≠ 0 on ℝ. ∎

The image is a proper subspace of PW_{T+log N}, so it is not the first-contact space of ν_D. "The image satisfies the
same quadrature" is therefore true and empty. Ascent raises the type (T_c ↦ T_c + log N) and the density, so the tower
it builds ascends and conflicts with nothing. The compressed M_T(1) = P_T Z P_T does not preserve the zero set (it is
not a multiplier). R162_903 Thm 3.2 / 1502 Prop 3 give Z X Z⁻¹ = X − M(a) for every a, so compression gives no
datum-specific invariance either.

## 4. Theorem ND (no Euler descent). PROVED, class-level

**Theorem ND.** Let 𝔡 be any admissible window datum (R160_X_C1 §1.2) with a first contact, and let F ∈ E_c ∖ 0.
Suppose F̂ = Φ·Ĝ with Φ entire, Ĝ entire, and Φ having infinitely many non-real zeros. Then this is impossible. In
particular, no element of E_c is divisible by:
- any Dirichlet polynomial D(z) = Σ_{n≤N} b_n n^{iz} (b_1 ≠ 0) that has at least one non-real zero;
- any Euler factor 1 − a p^{−1/2}p^{iz} with 0 < |a| ≠ √p, whose zeros lie on Im z = (log|a| − ½log p)/log p ≠ 0;
- any finite Euler product of such factors.

*Proof.* The non-real zeros of Φ are non-real zeros of F̂, and Theorem R(a) of R160_X_C1 says there are finitely many.
For D, let z₀ ∉ ℝ be a zero. D is uniformly almost periodic in Re z on the horizontal strip through z₀ (Bohr). On a
disc B around z₀ with B ∩ ℝ = ∅ and D ≢ 0, take ε < min_{∂B'}|D| on a smaller circle ∂B'. For a relatively dense set
of real τ, |D(z+τ) − D(z)| < ε on B'. By Rouché, D has a zero in B' + τ, and these zeros are non-real. So there are
infinitely many. The Euler-factor case is the single-frequency instance, with zeros periodic in Re z. ∎

**Reading.** The requested contradiction ("self-similarity under the Euler operator forces an infinite descending
structure") is **automatic and class-level**. Divisibility by an Euler factor is already excluded for ζ, for Λχ₂, for
the two-atom curve and for DH, by the finiteness of non-real zeros of ground states. The only divisors left are
Dirichlet polynomials with purely real zeros; for single-frequency ones this means |b|-balanced factors
1 + e^{iθ}n^{iz}. These are compatible with type T_c and density T_c/π for every datum, and a′ does not select them.
So neither direction of the Euler action on X can separate ζ from the table of §4 of the grid.

## 5. Falsifiers, spec, walls

- **F1.** NI uses λ = 0 exactly (the W(K,F) = 0 step). ND and T use only Theorem R, which holds at every bottom
  eigenvalue λ, so they are F1-blind and cannot carry a sign. NI passes F1 as an identity but gives no inequality
  beyond w_x ≥ 0, which is W ≥ 0 again.
- **F2.** Prop T and Thm ND are invariant under comb → −comb (any datum). NI is linear in the comb, and its only sign
  input is w_x ≥ 0. F2 is **not passed** by any forcing use.
- **F3.** Failed by construction (§1): every statement holds for deletion, κ, DH, Λχ₂ and the Type I curve.
- **Theorem M.** Nothing here is quantitative: NI, T and ND are exact and margin-free (S12 holds), so M does not
  bite. It also means no margin could be recovered from them.
- **Spec S1–S12.** S1 ✓ (NI). S2 ✓ (w_x is a ratio). S5 ✓ (single T_c object). S12 ✓. Fails S4/S8/S9 (class-level,
  weight-blind), S3 (orientation-blind) and S7 (Euler enters only as a multiplier after regularisation).
- **Walls.** W3 (primary killer), W1 (Cor NI.1 as a criterion = Hermite–Biehler), W12 (NI is an exact identity
  without sign).

## 6. Verdict and residuals

**PARTIAL + NO-GO.** New PROVED tools: Theorem NI (closed Christoffel formula for the Gauss weights, with a prime-by-prime
kernel k_F(x, log n) seeing only n < e^{T_c}), Cor NI.1 (interlacing of F̂ and L), and Theorem ND (no element of any
first-contact space has a divisor with infinitely many non-real zeros, e.g. an Euler factor). The Euler
self-similarity route is **NO-GO (PROVED)**. Descent is excluded for every datum by Theorem R, ascent is transport of
structure, and a′ ≡ 1 is never read.

Residuals (open, not claimed):
- O2202.1: the [prim] version of NI. K ∉ P_T, and the required Lagrange correction in the two moments is not
  written out.
- O2202.2: NI states that the contacts n ∈ [e^{T_c}, e^{2T_c}) are invisible at node level. Does a node-level
  statement that uses only n < X^{1/2} evade Theorem M? (It must still pass F3; there is no candidate.)
- O2202.3: whether a witness can have a real-rooted Dirichlet-polynomial divisor 1 + e^{iθ}n^{iz}, which would make the
  node set contain an arithmetic progression 2π(k+θ′)/log n. This is class-level as posed, so it is recorded, not
  proposed.
