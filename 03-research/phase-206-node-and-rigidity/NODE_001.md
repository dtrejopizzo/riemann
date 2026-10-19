# NODE_001 — Track A (phase 206): the node, exact statement, inventory, nonlinear candidates and the first 2×2 case

Files written: this memo and `NODE_001_data/node2x2.py`, which contains the only numerical computation: two 2×2 blocks with mpmath at 30 digits.

## Summary (≤250 words)

**(1) Statement.** I verified that the compressed main term is exactly 𝔢 − 2ccᵀ in convention (R1), with c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²)) for k odd (PROVED). The README needs a correction at one point: Φ_N is not Σ(Λ(n)−1)·…, but a Stieltjes integral against d(ψ(t) − t). The difference between the two forms is an Euler–Maclaurin term that does not vanish. The counting version is a consequence of the node, not its equivalent: node ⇒ n₊(Φ_N|_{c^⊥}) ≥ n₋((𝔪+𝔢)|_{c^⊥}) ≥ N′ − 1.

**(2)–(3) Inventory and candidates.** I examined the four nonlinear candidates in Λ:
- (a) Λ∗1 = log is the E.2 collapse, already recorded: retried.
- (b) Selberg's identity holds for every Dirichlet series (Prop N.2, PROVED). That is why a_P, cΛ, Beurling and DH all pass it; it does not contain the FE, so it chains. Already in the index (DMV 7.7, TB-3).
- (c) |P_X(½+iτ)|² ≥ 0: a Gram square only yields a bound for a linear functional of Λ if Λ(m)Λ(n) is linearized, and that goes through (b) or J1. Its version with the FE (the AFE) is in the index as L2_012 and R163_603.
- (d) The Loewner/Pick matrix of the Toeplitz part falls on the zero side: thm:Z.

No candidate survives. **Class NO-GO (ARGUED):** the available nonlinear operations on (ℕ,+,·) are polynomial identities of Dirichlet series or Gram squares, and neither contains Γ_ℝ.

**(4) 2×2 case (NUMERICAL).** At ½log3, the even block {1,3} raises no question at all: N′ = 1 and the prime 2 *subtracts*. The first nontrivial case is **T = ½log5**, block {1,3}:
- (𝔪+𝔢)(F) = −0.18913 and Φ_N(F) = +0.19098 for F ⊥ c, with margin 0.00185;
- the prime 2 contributes +0.5103 while 3 and 4 subtract;
- a_P fails (−0.477) and cΛ fails for c < 0.9924.

Why the 2 pays: ω₃ log 2 ≈ 1.29π. There is no identity behind it; it is an inequality between transcendental constants.

---

## 0. Corpus check (mandatory)

I grepped `05-meta-and-planning/ROUTES-TRIED-INDEX/` (README, 01–06, audits, SURVEY) and phases 199–205.
- **"Selberg"**: appears in three places.
  - NG-A4 (Selberg/Bombieri sieve, parity): NO-GO.
  - AUDIT_B 7.7 ("Selberg identity is blind", Prop, CITED DMV): duplicate of the Beurling-DMV falsifier.
  - 06_OPEN_RESIDUES l.117, TB-3 (R186_005 Thm TB3-neg: "generalized Selberg holds ∀b, Λ*Λ ≥ 0 is trivial"): closed negative in every degree.
  - The corpus also has R186_005_DEGREE_TWO_SELBERG, 104_35/104_37 (Selberg gates), R162_501, R11_2_ORIGIN and MAP_200.
- **"Λ∗Λ", "Λ*Λ"**: TB-3 (trivial), INV_J_001 (new reason "Λ(n)Λ(n+h), not Λ⋆Λ"; J1–J3; Thm J3 NO-GO by H_sparse).
- **"sieve", "criba"**: README ("Sieves, progressions…: W-sieve, phase 167"), R167_102 W-sieve, J2 ("MV/large sieve/Selberg only give the trivial bound").
- **"log²"**: SYNTHESIS M3 ("the log² terms cancel"), E.5 (H ~ log X versus G ~ log²X), X_001 ("log² cancellation"). No entry uses μ∗log² as the right-hand side of a window bound.
- **"Λ∗1 = log", "collapse"**: PROOF_L_SHARP_E_001 Thm E.2 (PROVED: on Z-images the full comb is Z_log Z^{−1}, the exterior form is free of Λ). Thm E.5 gives NO-GO for "sum of squares over ratios".
- **"approximate functional", "Riemann–Siegel", "AFE"**: L2_012 ("|ζ|²-positivity; AFE as class", NO-GO), G3C-R163_603 (DEAD: "Riemann–Siegel/AFE is FE-only data, shared by f_χ"), INV_K_001 ("AFE/Euler–Maclaurin: reformulation"), Z_CARRIER_001, and the README "symbol rigidity theorem" ("no exact identity on σ_T built with FE, Euler, Mellin, Poisson or Riemann–Siegel…").
- **"Loewner", "Pick", "Nevanlinna"**: phases 0–99 ("Loewner matrix + prolate", "core rate lemma RH-hard"), 100–189 ("Loewner transfer, planted falsifiers"). In the README, "Pick on σ>1 (Hadamard) is the zero side; its transport = thm:Z".
- **"semiring"**: principle (README), PROOF_L_SHARP_E_001 (exact form of the principle for 𝒲_ext: harmonic cut), class H (p-derivations, carrying).
- **"node", "Φ_N", "2×2 block ½log5"**: 0 hits as a statement. The explicit 2×2 with the decomposition 𝔪 + 𝔢 − 2ccᵀ + Φ and per-prime contribution does not appear. CALIB_R5 gives only eigenvalues; LL_001 has a 2×2 in another form (block (1,1) of the exterior form).

**Conclusion of the check.**
- Candidates (a), (b) and (c) of the target **are in the index**. Below I test each one for a new reason; none exists, and I declare them retries with the concrete reason.
- What is new in this memo:
  - the exact statement of the node with the Stieltjes correction;
  - Prop N.2 (universality of Selberg-type identities) as a one-line proof of why (b) chains;
  - Prop N.3, which reduces Gram squares to (b) or J1;
  - the explicit 2×2 at ½log5 with its per-prime bookkeeping.

---

## 1. Exact statement of the node

### 1.1 Data from P47 (verified against the text)
- **Window form** (eq:Aform):
  𝔞_T(F) = 𝔪_T(F) − Σ_{n∈N_T} v_n c_F(log n),  with v_n = 2Λ(n)n^{−½}, c_F(u) = ∫F(t)F(t+u)dt, N_T = {n : log n < 2T}.
  By support, c_F(log n) = 0 if n ≥ e^{2T} (H1PLUS §1.2).
- **Archimedean term:** 𝔪_T(F) = (1/2π)∫ m(τ)|F̂(τ)|²dτ, of conductor 1. The Lévy form, used in the script, is
  𝔪 = (C₀ + κ_T)c(0) + ∫₀^{2T}(c(0) − c(u))K(u)du,
  with C₀ = ψ(¼) − log π, K(u) = 1/(2sinh(u/2)) + 1/(2cosh(u/2)) and κ_T = log coth(T/2) + 2arctan e^{−T}.
- **Basis** (lem:combsine): e_k(t) = T^{−½}sin(ω_k(t+T)), ω_k = πk/2T. It is even if k is odd. E_N^ev = span{e_k : k odd ≤ N}.
- **Even sector:** 𝔄_ev = 𝔞_T|_{even} and W^ev = 𝔄_ev + 2ℓ², with ℓ(F) = ⟨F, χ_ev⟩ and χ_ev = cosh(t/2)1_{I_T} (prop:WT, cor:H1minus).

### 1.2 The compressed main term (PROVED; verification requested)
I call the main term the integral corresponding to the weight v_n with Λ replaced by the density 1:
  M(F) := −∫_1^{X} 2t^{−½}c_F(log t)dt = −2∫_0^{2T}e^{u/2}c_F(u)du = −∫∫F(x)F(y)e^{|x−y|/2}dxdy,  X = e^{2T}.
The last equality uses that c_F is even in u and that its support is [−2T, 2T].

We write e^{|s|/2} = 2cosh(s/2) − e^{−|s|/2} and cosh((x−y)/2) = ch(x)ch(y) − sh(x)sh(y), with ch = cosh(·/2) and sh = sinh(·/2). Thus:
  M(F) = 𝔢(F) − 2(⟨F,ch⟩² − ⟨F,sh⟩²),  𝔢(F) = ∫∫F(x)F(y)e^{−|x−y|/2} = (1/2π)∫|F̂|²/(¼+τ²) ≻ 0.   (R1)
In the even sector ⟨F,sh⟩ = 0, so **M = 𝔢 − 2ℓ²**. Compressing to E_N^ev, M_N = 𝔢_N − 2ccᵀ with c_k = ⟨χ_ev, e_k⟩. Two things need checking.

- **Closed formula for c_k** (PROVED). Integrating by parts twice:
  ∫_{−T}^{T}cosh(x/2)sin(ω(x+T))dx = [ω(cosh(T/2) − cosh(T/2)cos 2ωT) + ½sinh(T/2)sin 2ωT]/(¼+ω²).
  For k odd, 2ω_kT = πk, so cos = −1 and sin = 0. This gives
  **c_k = 2ω_k cosh(T/2)/(√T(¼+ω_k²))**, which matches the README.
  - NUMERICAL check: at T = ½log3, c₁ = 0.950424 by the formula and 0.9504238 by quadrature (script).
- **Agreement with the script's decomposition** (NUMERICAL). With 𝔢 := M + 2ccᵀ, this 𝔢 is positive definite:
  - at ½log3, eigenvalues 0.0233 and 0.848;
  - at ½log5, 0.0488 and 1.161.
  Moreover, 𝔄 = 𝔪 + comb reproduces the minimal eigenvalues of CALIB_R5: −2.0165 at ½log3 with block {1,3}, versus the 2N value, −2.02; and −3.0238 at ½log5, versus −3.02.

**Verdict:** the README is correct on the main term.

### 1.3 Correction to the README: Φ_N is Stieltjes, not Σ(Λ−1)
By definition, Φ_N := comb − M, that is
  **Φ_N(F) = −∫_{1^−}^{X} 2t^{−½} c_F(log t) d(ψ(t) − t)**   (Stieltjes; E(t) = ψ(t) − t),
and equivalently
  Φ_N(F) = −Σ_{n<X} 2Λ(n)n^{−½}c_F(log n) + 2∫_0^{2T}e^{u/2}c_F(u)du.

The README's wording, "Σ_{n≤e^{2T}}(Λ(n)−1)·(2/√n)·𝓕_F(log n) + boundary", is correct only if the "boundary" is exactly
  B_N(F) := Σ_{n<X}2n^{−½}c_F(log n) − ∫_1^X 2t^{−½}c_F(log t)dt.
That term is neither small nor of fixed sign (ARGUED).
- It is the Euler–Maclaurin formula for the function t^{−½}c_F(log t), which does not vanish at the boundary t = 1, where it equals c_F(0) = ‖F‖².
- It contains a term of ζ(½)·c_F(0) type plus the derivative jumps.
- The n = 1 term of the sum, with Λ(1) − 1 = −1, already contributes +2‖F‖².

**Recommendation.** Use the Stieltjes form or the second line. This is the script's convention, and it is the one under which the 2×2 of §4 reproduces CALIB_R5.

### 1.4 The node in terms of primes (PROVED, exact rewriting)
Write F = Σ_{k odd ≤ N} x_k e_k with ⟨F, c⟩ = Σx_k c_k = 0. The node says:

  **Σ_{n<e^{2T}} 2Λ(n)n^{−½}·(−c_F(log n))  ≥  −𝔪_T(F) − 𝔢(F) − 2∫_0^{2T}e^{u/2}c_F(u)du.**   (N)

The right-hand side has no primes: it depends on Γ_ℝ (through 𝔪), on the pole (through 𝔢 and the main term), and on F. In lem:combsine coordinates, the left-hand side is xᵀΠx, with Π_{kk} = C_T(ω_k) + D_T(ω_k)/(2Tω_k) and Π_{kl} the difference quotient of D_T(ω) = Σ v_n sin(ω log n). That is exactly how the phases sin(ω_k log n) enter.

**Context identity (H1PLUS (1.4), PROVED).** For F ⊥ c, the left side minus the right side equals exactly W^ev_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ). That is, (N) is the positivity of the Weil form restricted to c^⊥ ∩ E_N^ev. This is not used for anything; it only fixes requirement (iv) of the README: a proof of (N) cannot consist of evaluating that sum.

### 1.5 Counting version (PROVED, correct direction)
Let V = c^⊥ ∩ E_N^ev, of dimension N_ev − 1. If 𝔪 + 𝔢 + Φ_N ≽ 0 on V, then by min–max (Weyl) n₊(Φ_N|_V) ≥ n₋((𝔪+𝔢)|_V). By Cauchy interlacing, n₋((𝔪+𝔢)|_V) ≥ N′ − 1, with N′ := n₋((𝔪+𝔢)_N^{ev}). Hence
  **node ⇒ n₊(Φ_N|_{c^⊥}) ≥ N′ − 1.**
- The converse is false in general: the count only requires that Φ have enough positive directions, not that they be aligned with the negative directions of 𝔪 + 𝔢 nor that they have the required size.
- The count is necessary, not sufficient. The README needs correcting where it says "n₊ ≥ N′ − 1 is required": it should say that it is necessary.
- Remark: N′ ≤ n₋(𝔪_N^{ev}), because 𝔢 ≻ 0. In the two computed cases equality holds (§4).

---

## 2. Inventory: what Φ_N has and what 𝔪 + 𝔢 has

| | Φ_N | 𝔪 + 𝔢 |
|---|---|---|
| dependence on Λ | linear, coefficients Λ(n)n^{−½}, n < e^{2T} | none |
| phases | sin(ω_k log n), cos(ω_k log n), exact | none; smooth symbol m(τ) + 1/(¼+τ²) |
| structure | Toeplitz (difference quotient of D_T) + Hankel (lem:combsine) | Toeplitz with smooth symbol + Lévy |
| FE | does not see it (a_P preserves the comb except for one prime) | encodes it: m = −2θ′ (Riemann–Siegel phase), conductor 1 |
| pole | only through the subtracted main term | 𝔢 (Green's kernel of ¼ − ∂²) |
| size | O(e^T) coefficients individually; internal Chebyshev cancellation | O(log T) per mode |

**Identities linking Λ with Γ_ℝ without zeros.** The index has two families.
- **Explicit formula.** It is linear; in the window it is thm:Z or lem:roughEF and leads to the sum over zeros (§1.4).
- **Hamburger rigidity.** It is linear; BARRIER_D1 Thm 4 says it is blind to w_T.

A third one is needed. **Poisson/Mellin applied to the truncated comb** with a test in the window is not it.
- The functional equation of theta, seen through Λ = μ∗log, is the Mellin transform of θ(x) = Σe^{−πn²x}. Applying it to Σ(Λ−1)(n)n^{−½}c_F(log n) requires going from θ to ζ and from ζ to ζ′/ζ.
- The log-derivative introduces the zeros as poles, and the result is lem:roughEF. On the critical line the identity is pointwise: Re(ζ′/ζ)(½+iτ) = −θ′(τ) away from the zeros, and its distributional boundary value adds π Σ_γ δ(τ−γ).
- That is: **the FE is exactly the archimedean term of the node, and what is left over is the zero measure.** It is an identity, not a sign (PROVED as a classical computation; it is the "symbol rigidity theorem" of the index README).
- Therefore the sign step has to be nonlinear in Λ, or nonlinear in ζ before taking the log-derivative.

---

## 3. Nonlinear candidates, one by one

### 3.0 Preliminary lemma: how a nonlinear step gives a linear bound (PROVED, logic)
The node bounds below a linear functional L(Λ) = Σ Λ(n)k_F(n), with k_F(n) = −2n^{−½}c_F(log n). A nonlinear step only helps in the form
  Q(Λ) ≥ 0  and  Q(Λ) = R − L(Λ)  ⟹  L(Λ) ≤ R
(or with the signs flipped), where Q is nonlinear and R does not contain Λ, or contains it in a controlled way. So each candidate must exhibit:
(i) the identity Q = R ∓ L;
(ii) the positivity of Q;
(iii) the correct sign and size of R against 𝔪 + 𝔢.
I use this template for all of them.

### 3.1 Candidate (a): Λ∗1 = log as a quadratic identity
- **Form.** ⟨Λ∗1, g⟩ = ⟨log, g⟩ for every g. As a form in F: Σ_{m,j}Λ(m)k_F(mj) = Σ_n log n·k_F(n).
- **Not quadratic.** It is bilinear in (Λ, 1), with the factor 1 fixed, so it is linear in Λ. To use it one must solve for L(Λ) in terms of a sum with k_F evaluated at multiples mj. That is a Möbius inversion, and requirement (v) of the README rules it out.
- **Index.** E.2 (PROOF_L_SHARP_E_001) carries out exactly that collapse on Z-images: the form becomes free of Λ and the ratio classes are indefinite one by one (E.5).
- **New reason?** None. On E_N the Z-images do not apply, but the only variant on E_N is the compression of the same collapse. **Retry: discarded.**

### 3.2 Candidate (b): Selberg's identity
- **Form.** Λ·log + Λ∗Λ = μ∗log², which coefficient by coefficient is the identity (ζ′/ζ)′ + (ζ′/ζ)² = ζ″/ζ.
- **Template 3.0.** For a pointwise weight g ≥ 0, Σ Λ(n)log n·g(n) = Σ(μ∗log²)(n)g(n) − Σ(Λ∗Λ)(n)g(n) ≤ Σ(μ∗log²)(n)g(n). This is an upper bound for a linear functional of Λ obtained from quadratic positivity. It is exactly the mechanism of the elementary Selberg–Erdős proof, and it is a genuine nonlinear step in the template's form.

**Proposition N.2 (PROVED, universality).** Let D(s) = Σ a_n n^{−s} be a formal Dirichlet series with a_1 = 1, and let Λ_D be the coefficient of −D′/D. Then Λ_D·log + Λ_D∗Λ_D = (D^{−1})∗(a·log²), where D^{−1} is the Dirichlet inverse of a.
- *Proof.* (D′/D)′ + (D′/D)² = D″/D holds in the ring of formal series. Read off the coefficients. ∎
- **Consequences.**
  - It is passed by a_P (D = ζ·(1 − 2^{−s}), a = 1_{odd}), cΛ (D = ζ^c), Beurling-DMV and DH (D = combination of L-series, which is a Dirichlet series).
  - The right-hand side of Selberg is elementary only if a is known.
  - For a_P, a = 1_{odd} is just as elementary. Therefore the positivity Λ∗Λ ≥ 0 plus the elementary right-hand side **does not distinguish ζ from a_P**: requirement (i) fails.
  - The FE does not appear: (ii) fails. By Def. O1.2, the sign step uses a single channel (E), i.e. **it chains**.

**Three more failures in the window form**, all PROVED as observations:
1. **The window weight is not positive.** k_F(n) = −2n^{−½}c_F(log n) has indefinite sign in n: in §4, c_F(log 2) < 0 and c_F(log 3) > 0. Λ∗Λ ≥ 0 only helps against g ≥ 0.
2. **One must divide by log n.** To isolate Λ one must divide by log n, which gives a weight g/log, and the resulting bound applies to Λ log, not to Λ.
3. **Weight gap.** The elementary error of Σ_{n≤x}(μ∗log²)(n) is O(x), with weight 1. At weight n^{−½} and scale X = e^{2T} it gives O(e^T)‖F‖². That is e^T times the budget 𝔪 + 𝔢 = O(log T)‖F‖². This is the weight gap from SYNTHESIS §4: every built-in positivity reads the primes at weight ≤ n^{−1}.

**Index.** Covered by AUDIT_B 7.7 ("Selberg identity is blind", DMV) and TB-3 / R186_005 ("generalized Selberg holds ∀b; Λ*Λ ≥ 0 is trivial").
**New reason?** The proposal was the window form. Failures 1–3 show that the window form does not evade either of the two recorded reasons (universality and triviality) and adds the weight gap. **Retry: discarded. NO-GO (PROVED as far as falsifiers are concerned, by N.2).**

### 3.3 Candidate (c): |Σ_{n≤X}Λ(n)n^{−½−iτ}|² ≥ 0, with the FE in the same step
- **Form.** Q(Λ) := (1/2π)∫|P_X(½+iτ)|²|F̂(τ)|²dτ = Σ_{m,n<X}Λ(m)Λ(n)(mn)^{−½}c_F(log m − log n) ≥ 0, which is Gram.

**Proposition N.3 (PROVED, structure of Q).**
- *Diagonal.* m = n gives Σ Λ(n)²n^{−1}·‖F‖²: weight n^{−1}.
- *Off-diagonal.* m ≠ n with Λ(m)Λ(n) ≠ 0. If m/n is a power of the same prime, one gets the local square Σ_p log²p·∫|Σ_a p^{−a(½+iτ)}|²|F̂|², positive term by term, of weight p^{−1}, and **growing as primes are added**. If m = p^a and n = q^b with p ≠ q, the terms carry c_F(log(p^a/q^b)), of indefinite sign.
- *Linearization.* To relate Q to the linear functional L(Λ) of template 3.0, Λ(m)Λ(n) must be linearized. The only exact linearizations available are Λ² = log·Λ on the diagonal (J1 of INV_J_001) and Λ∗Λ = μ∗log² − Λlog in the product mn, which is (b). The ratio m/n has no linearization: the pairs (p, q) are multiplicative correlations of primes (P36-4 / Doc 108, closed).
- *Proof.* Direct expansion and classification of the pairs (m, n). ∎ The claim "only ones available" is ARGUED: it is the index's inventory, not a classification theorem.

**Requirement (i) via B_P.** Removing the prime 2, Q loses a positive local square, so Q^{a_P} ≤ Q^ζ. A proof that uses only Q ≥ 0 is passed by a_P if the rest of the chain is comb-generic. It does not falsify by itself, but it does not supply the specificity of ℕ either.

**FE in the same step.** The only way for Γ_ℝ to enter |P_X|² is via the AFE: ζ = P_X + χ·P̃_Y + error, with χ = Γ_ℝ(1−s)/Γ_ℝ(s). That is the object of L2_012 ("|ζ|²-positivity; AFE as class", NO-GO) and of R163_603 (DEAD: "Riemann–Siegel/AFE is FE-only data, shared by f_χ"). INV_K_001 classifies it as a reformulation. The falsifier f_χ = αL(s,χ) + ᾱL(s,χ̄) shares the AFE.

**New reason?** That the weight n^{−½} lies in the "empty cell" of SYNTHESIS §4 is not a new reason: L2_012 already worked at weight ½ with the FE. **Retry: discarded.**

### 3.4 Candidate (d): others that pass (i)–(v)
**(d1) Loewner/Pick of the Toeplitz part.**
- The Toeplitz part of lem:combsine is the Loewner matrix [(D_T(ω_k) − D_T(ω_l))/(ω_k − ω_l)]. By Loewner's theorem (CITED), it is ≽ 0 on every node set iff D_T is an operator-monotone function (Pick).
- Pick positivity for a finite partial sum: D_T is almost periodic and bounded, so it is not Pick (a nonconstant Pick function on ℝ grows). The matrix is not ≽ 0 in general, and the positivity that would be needed is that of the sum 𝔪 + 𝔢 + Φ, not that of Π alone.
- If D_T is replaced by −ζ′/ζ, the Pick version for σ > 1 is the zero side (index README: "Pick on σ>1 (Hadamard) is the zero side; its transport = thm:Z"). Loewner also appears in phases 0–99 and 100–189.
- **Retry: discarded.**

**(d2) What the 2×2 shows (§4).**
- At ½log5 the direction F ⊥ c is paid for by the prime 2 only because ω₃·log 2 = 4.059 ≈ 1.29π, so cos(ω₃ log 2) < 0. It is a **resonance of the local Euler factor at 2** with the Dirichlet frequency ω₃ = 3π/log 5.
- The object expressing this is the local multiplier g_{2}(τ) = 2log 2·Re[2^{−½−iτ}/(1 − 2^{−½−iτ})] from B_P (TOOLS_204U), which is linear in the set of primes.
- The correct nonlinear question would be why the window's Dirichlet frequencies (ω_k = πk/log X) fall in the negative bands of the local factors of small primes. That is a relation between log 5 (the edge X) and log 2, log 3: **semiring arithmetic at the edge**, because X = 5 = 2² + 1 and the window opens at an integer. It is an idea, not a candidate with a sign step, and it remains OPEN as a question (§4.3).

**Proposition N.4 (class NO-GO, ARGUED).** Let 𝒦_NL be the class of sign steps of the form Q ≥ 0, Q = R − L(Λ), where:
- Q is a polynomial in the coefficients of −D′/D of a Dirichlet series D over ℕ, positive as a sum of Gram squares or as Λ∗Λ ≥ 0;
- R is computed from the coefficients of D and of Γ_ℝ only via identities.

Every step in 𝒦_NL chains:
- the D part is universal (N.2);
- Γ_ℝ can only enter via the AFE or the explicit formula, which are linear identities in ζ.

It either falsifies a_P or reproduces thm:Z. *Argument:* N.2 and N.3 plus the inventory of identities in §2. A classification theorem for "zero-free" identities between Λ and Γ_ℝ is missing; hence the state is ARGUED.

---

## 4. First finite lemma: the 2×2

### 4.1 ½log3: raises no question at all (NUMERICAL)
- At N(T) = 2 the even block is {k = 1}, of dimension 1. Since c^⊥ = 0, the node is empty.
- **Correction to the statement:** at ½log3 the even space of E_{N(T)} is not of dimension 2. N′ = n₋(𝔪^{ev}) = 1 (CALIB_R5: even/odd 1/1).
- Enlarging to {1, 3} (2N, with ω₃ = 8.58 > t₀), the script gives:

| | eigenvalues |
|---|---|
| 𝔪 | −1.7419, +0.1775 |
| 𝔪 + 𝔢 | −0.9055, +0.2121 (N′ = 1) |
| Φ_N | −0.2075, +0.9064 |
| 𝔄 | −2.0165, +0.0037 |

- For F ⊥ c: (𝔪+𝔢)(F) = +0.17070 and Φ_N(F) = −0.16700, of which the comb (prime 2) contributes −0.14243 and the main term −0.02457. Z(F) = +0.00370.
- **The only prime, 2, hurts.** The node holds because 𝔪 + 𝔢 is already positive on c^⊥.
- **Reading of falsifiers at ½log3:** a_P (without the 2) gives Z = +0.146, so it *passes*; cΛ with c = 1.2 gives Z = −0.025, so it *fails*. That is, the node at ½log3 is an **upper bound** for log 2 (c ≤ ≈1.15), not a statement of arithmetic sign. It does not work as a model case.

### 4.2 ½log5, block {1,3}: the smallest nontrivial question (NUMERICAL, 30 digits)
Data: T = ½log5 = 0.804719, ω₁ = 1.95199, ω₃ = 5.85597 < t₀ = 6.2898. Comb terms: n ∈ {2, 3, 4}.

| matrix (basis e₁, e₃) | entries | eigenvalues |
|---|---|---|
| 𝔪 | [[−2.13814, −0.40163], [−0.40163, −0.28960]] | −2.22163, −0.20611 |
| 𝔢 | [[1.07761, 0.29315], [0.29315, 0.13233]] | 0.04879, 1.16114 |
| 𝔪 + 𝔢 | — | −1.07338, −0.14443 (**N′ = 2**) |
| Φ_N | [[1.06076, 0.10924], [0.10924, 0.15987]] | 0.14681, 1.07382 |
| 𝔄 | [[−2.68998, −0.94789], [−0.94789, −0.33193]] | −3.02377, +0.00185 |

- c = (1.159786, 0.408979), with polar eigenvector cos ≈ 1.
- Node direction: F = −0.332562 e₁ + 0.943081 e₃, unit, ⊥ c.

**Node bookkeeping (N):**
- (𝔪+𝔢)(F) = **−0.189129**. The budget is met exactly: N′ − 1 = 1 direction that Φ must pay for.
- Φ_N(F) = **+0.190981** = comb **+0.243969** − main term **0.052988**. What is left is Z(F) = 𝔄(F) = **+0.001852**.
- Comb by term: −2Λ(n)n^{−½}c_F(log n), with c_F(0) = 1.

| n | c_F(log n) | contribution |
|---|---|---|
| 2 | −0.520595 | **+0.510318** |
| 3 | +0.185447 | −0.235252 |
| 4 | +0.044864 | −0.031097 |

**Falsifiers in this 2×2** (NUMERICAL):
- **a_P, P = {2}:** Z(F) = −0.47737 and 𝔄 has n₋ = 2. **Falsifies.** Confirms property (i) in the smallest question.
- **cΛ:** the threshold is c* ≈ 0.9924, where the eigenvalue of 𝔄 crosses 0 (+1.97e−6 at 0.9924). c < c* falsifies (c = 0.8: −0.0459) and c > c* passes (c = 1.2: +0.0506; c = 3: +0.543). At ½log5 the node is a lower bound for Λ, the opposite direction from ½log3.
- **Per-coefficient tolerance**, with the rest fixed:
  - the node holds if Λ(2) ≥ (1 − 0.00363)·log 2;
  - it holds if Λ(3) ≤ (1 + 0.00787)·log 3;
  - the n = 4 term enters with Λ(4) = log 2.
- **Quartets, Epstein x² + 5y², DH:** not computed in this 2×2. Epstein at T = ½log5 has n₋(𝔄_ev) = 1 (CALIB_R5), so it does not falsify at this T. This is consistent with its hyperbolic pairs living above t₀. A quartet or DH should falsify starting from its critical T (≥ 9/5 for DH), not at ½log5. **The ½log5 2×2 only discriminates a_P and cΛ.**

**Lemma N.5 (NUMERICAL; provable via interval arithmetic, not done).** At T = ½log5, for F ∈ span{e₁, e₃} with ⟨F, c⟩ = 0:
  Σ_{n∈{2,3,4}}2Λ(n)n^{−½}(−c_F(log n)) = 0.243969‖F‖² > 0.242117‖F‖² = −(𝔪+𝔢)(F) + 0.052988‖F‖².
Equivalently, the node (N) holds with margin 0.001852‖F‖² (0.76% of the left-hand side).
- Alternative route to PROVED: the P47 certificates at ½log5 (CITED) give W^ev ≽ 0 in the window. By RFIN_TRACT 1.1(b), that implies Z_N ≽ 0 on all of E_N^ev and hence the node on this block.
- That route is CONDITIONAL on the certificate covering the whole even sector and not only λ_A in its class of tests. Not verified against the text in this memo.

### 4.3 What arithmetic identity makes that direction positive? (honest answer)
**None identified.** In coordinates, the 2×2 is an inequality between explicit constants:
- log 2 and log 3, entering through Λ;
- √2 and √3, entering through n^{−½};
- log 5, entering through T;
- ψ(¼), log π, coth, arctan e^{−T} and the Lévy integral, entering through 𝔪;
- cosh(T/2) = (5^{¼} + 5^{−¼})/2, entering through c and 𝔢;
- the sin and cos phases of (3π/log 5)·log 2 and (3π/log 5)·log 3.

**What makes the direction positive.** It is paid for by the prime 2, because the frequency ω₃ falls in the negative band of the local factor 2^{−iω}:
- (3/log 5)·log 2 = 1.292, that is ω₃ log 2 ≡ 1.29π;
- the 3 pays off because ω₃ log 3 = 6.43 ≡ 0.05π, where the cosine is positive.

**What kind of statement this is.** A "near-commensurability" relation among log 2, log 3 and log 5 at resolution π/T. It is the semiring at its barest: 5 = 4 + 1 (the additive edge X = 5) versus 4 = 2·2 (the power n = 4 that also enters). But the margin is 0.76%, and positivity is closed by the rest of the explicit formula: Σ_ρ|Φ_F(ρ)|² = 0.00185, which is small because F̂ decays before γ₁ = 14.13.

**The smallest case already shows the node's three features:**
1. exact cancellation in the count (N′ − 1 = 1 direction);
2. margin at the floor of the sum over zeros;
3. dependence on a specific prime via phase resonance.

**What is missing for a lemma** (OPEN), named: **(N5-uniform).** For the family of windows T = ½log(2^a + 1), give a lower bound for −c_F(log 2) in the node direction that does not go through the sum over zeros.
- The arithmetic 2^a + 1 = X fixes the phase ω_k log 2 = πk·log 2/log(2^a + 1) ≈ πk/a.
- This is the first question in which (ℕ,+,·) enters through the *edge* of the window and not through the comb.
- Not clear whether it has content: it might be the same family of boundary tests as the "boundary channel" of SYNTHESIS_MECHANISM_001, and a grep for "boundary channel" is needed before taking it on.

---

## 5. Entry for the index

- **NODE_001 (phase 206, track A).** Node stated exactly:
  - (R1) is verified in the even sector, with c_k in closed form;
  - Φ_N is Stieltjes against d(ψ − t); the README's "Σ(Λ−1)" form is incorrect except for the Euler–Maclaurin term;
  - the count is necessary, not equivalent.
- **Candidates (a) Λ∗1 = log (= E.2), (b) Selberg's identity and (c) |P_X|² ± AFE (= L2_012/R163_603):** all retries without a new reason.
  - Prop N.2 (PROVED): Selberg-type identities hold for every Dirichlet series ⇒ a_P/cΛ/DMV/DH pass them; it chains.
  - N.3: Gram squares linearize only via J1 or (b).
  - N.4: class NO-GO of 𝒦_NL (ARGUED).
  - (d1) Loewner/Pick = zero side.
- **2×2 at ½log5, {e₁, e₃} (NUMERICAL):** (𝔪+𝔢) = −0.18913, Φ = +0.19098, margin 0.00185 = sum over zeros. The prime 2 pays +0.510 (ω₃ log 2 ≈ 1.29π); a_P falsifies (−0.477); cΛ threshold c* = 0.9924. ½log3 is either empty or in the wrong direction.
- OPEN: N5-uniform (windows X = 2^a + 1). Row D OPEN.

## 6. What was not proved (explicit)
- The node for general T: OPEN.
- N.4 as a classification theorem: ARGUED.
- Lemma N.5: NUMERICAL, not certified by intervals. The CITED route depends on the P47 certificate covering the whole even sector, which is not verified.
- Quartets, Epstein and DH in the 2×2: not computed.
