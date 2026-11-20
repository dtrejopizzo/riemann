# REVIEW_001_LC — Critical review of ROUND_001_L and ROUND_001_C

Scope: line-by-line reading of the two memos, independent derivation of each step, cross-check of the citations
against `../phase-211-sign-sandbox/` (STATEMENT_001, POWER_CONE_001, POWER_BRIDGE_002,
POWER_GRAM_SLICES_OBSTRUCTION §§17.2–17.5, 18.1–18.4, 18.7; POWER_GLOBAL_ROUTE_REVIEW "asinh
comparator", "Primitive comparisons", "Small hyperbolic comparison", "Closure…", "Reusable general
filter", "Factorial extension…", "Squarefree scales…"; POWER_HYPERBOLIC_MODEL_GRAM §4),
search in the routes index, the grid and `RULES_AVOID.md`, and a hunt for counterexamples. No
existing file was modified. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

Summary of verdicts.

| Memo | Verdict | Mathematical error in the core | Correction needed |
|---|---|---|---|
| ROUND_001_L | ACCEPT with corrections | none found | labels of §6.3(a) and §9; actual scope of the asinh corollary; non-effectiveness; sandbox wording |
| ROUND_001_C | ACCEPT with corrections | none in Lemma 1, (R0), (R1), (R2) nodes | gap in the modes version; three overstatements; novelty smaller than declared |

---

## Part I — ROUND_001_L

### I.1 Step-by-step verification (independent derivations)

- **F2.** H even and real on ℝ ⟹ H(iτ) real ⟹ H′(iτ) ∈ iℝ ⟹ Re M(iτ) = 0 away from the poles. Correct.
- **F4.** Redone: for Re z ≥ 1, |k+z| ≥ k+1 gives |ψ(z)+γ| ≤ (π²/6)|z−1|; with Re a ≥ 2,
  |1/a|+|1/(a−1)| ≤ 3/2. (b) correct; (a) correct.
- **C1.** Normalization checked: Re 1/(σ+i(τ−s)) = σ/(σ²+(τ−s)²), integral π; an atom of mass m at
  τ gives m/(u−iτ), i.e. residue = mass. Consistent with Step 2 (mass r_k) and with 2u/(u²+τ²) per pair.
- **C2.** Pick's theorem on Π, arbitrary nodes of Π (real ones included). The transport identity
  to the disc was recomputed:
  1 − S(u)conj S(v) = 2(F(u)+conj F(v))/[(F(u)+1)conj(F(v)+1)] and analogously for z; the quotient is the one
  written. Re w_i ≥ 0 guarantees w_i ≠ −1. The case of constant unimodular S (F constant imaginary) does not
  break anything. Correct.
- **C3 and Lemma 1.2.** Blaschke condition on Π for zeros of a function of bounded type:
  Σ Re u_n/(1+|u_n|²) < ∞. For the ladder, Σ (31.5+n)/(1+(31.5+n)²) = ∞; transported to the half-plane
  Re u > 3/2 it still diverges. Correct. The class at stake is the right one: F and M0 are positive-real
  (hence of bounded type), and M is of bounded type on Re u > 3/2 because M = [M/(u+1)]/[1/(u+1)] with
  both factors bounded (F4(b)). M need not be positive-real for uniqueness: good.
- **Lemma 1.3.** Montel + C2; the limit S satisfies S(x_j) ≠ 1. Correct. Uncountable case: correct.
- **Theorem 2.1.** Correct (requires only that M be finite on X; it is, F1).
- **Theorem 3.1, Step 1.** G = M − εM0 − F is of bounded type on Re u > 3/2 and vanishes on a set
  violating Blaschke ⟹ G ≡ 0 there ⟹ meromorphic identity on Π. Correct. **Step 2.** Stieltjes
  inversion with F2: away from the poles the limit density is 0; at a pole
  (1/π)∫φ·r_kσ/(σ²+(τ−τ_k)²)dτ → r_kφ(τ_k). Correct; c_M = 0 by F4(a). **Step 3.** Uniqueness of the
  Herglotz triple ⟹ c_0 = c_F = 0, εμ_0 ≤ μ_M. Correct.
- **Corollary 4.1.** Exact contrapositive of Theorem 3.1; logically unconditional. Correct.
- **Proposition 4.2.** Correct; CONDITIONAL properly placed.
- **§6.2.** REP of 211/HYP §4 says exactly M_a(u)/u = ½Tr(H_a+u²/4)^{-1}, with Tr R_x ≤ 1/(2a);
  hence M_a = Σ_k 2u/(u²+ω_k²), ω_k = 2√λ_k. Correct.
- **§6.3.** The real Gram of the resolvents (u − 2i√H)^{-1} is Σ_k[1/((u−iω_k)(v+iω_k)) + c.c.], which is
  Lemma 1.1 for μ_a; U_Phi = Σ_k G(ω_k)·(projector k). The condition "U_Phi = 0" and "every iω_k is a pole
  of M" coincide. Correct. **NUMERICAL** (spot check, mpmath 30 digits): first zero in ν
  of K_{iν}(2π) at ν₁ = 9.768770…, ω₁ = 19.53754… ∈ [17, 41/2], consistent with the localization of 211.
- **§6.4.** sinh maps {Re w > 0, |Im w| < π/2} bijectively onto Π; M_0 = ½asinh(u/4π) is
  positive-real, c_0 = 0, and on the boundary Re M_0(iτ) = ½arccosh(|τ|/4π) > 0 for |τ| > 4π: density
  (1/2π)arccosh. (E2) holds. Correct.
- **§7.1.** Schur complement: K − g⊗g/K(w,w) ⪰ 0 if K ⪰ 0. Correct.
- **Circularity.** None: neither Theorem 3.1 nor Cor. 4.1 assumes the sign of K_M. What does happen
  (and the memo says so) is that the hypothesis of Theorem 3.1 contains that sign.

### I.2 Counterexample hunt (NUMERICAL, toy)

Toy: M_toy(u) = π coth(πu) − 1/u = Σ_{k≥1} 2u/(u²+k²) (atomic boundary measure, masses 1 at ±k),
nodes 1.5 + n, n < N, smallest eigenvalue of K_{M_toy − εM0}, arithmetic with 150–260 digits.

| comparator M0 | ε | N = 4 | 8 | 16 | 32 | 48 |
|---|---|---|---|---|---|---|
| 1/(u+1) (continuous boundary) | 0.9 | 2.6e−5 | 1.9e−11 | −2.8e−16 | −1.0e−15 | −1.2e−15 |
| 1/(u+1) | 0.3 | 3.1e−5 | 2.5e−11 | 1.5e−23 | −6.6e−30 | −2.3e−29 |
| 2u/(u²+1.5²) (foreign atom) | 0.5 | 2.9e−5 | 2.5e−11 | 1.6e−23 | −2.0e−36 | −2.3e−35 |
| u (linear term) | 0.05 | 3.0e−5 | 2.1e−11 | −2.3e−9 | −2.3e−4 | −1.1e−2 |
| 2u/(u²+1) (own atom), sizes 3–24 | 0.5 | positive in all | | | | |
| 2u/(u²+1) (own atom), sizes 3–24 | 1.2 | negative from N = 6 on (≈ −7e−6) | | | | |
| none (control) | — | 3.2e−5 | 2.6e−11 | 1.8e−23 | 7.0e−48 | 2.5e−72 |

No counterexample was found; all cases behave as predicted by (E1)–(E4) and Prop. 4.2. A fact
the memo does not state: the violation appears late and with size 10⁻¹⁶–10⁻³⁶ (with ε = 0.05 it does not appear
until N = 24). Cor. 4.1 **is not effective**: it is useless as a numerical filter in double precision and does not give
the block size.

### I.3 Errors and gaps (with location)

L-1. **§6.3, point (a) — inflated label.** "Holds for every a > 0 and for the Robin variants and the
sums w·b·M_{a,β}(bu)" appears under a PROVED heading without the memo proving that each variant
is positive-real on Π with atomic boundary measure (for Robin one needs the REP with a positive operator
with trace-class resolvent; for the sums, convergence in the sense of C1). Correct label:
**ARGUED** for Robin and sums; **PROVED** only for Dirichlet and every a > 0 (REP holds for all a).

L-2. **§9, first point, and "What was proved" 7 — certificate dependence omitted.** "No exterior
model… with an atom outside the poles of M (hyperbolic a = 2π) works, for any ε" is PROVED
only relative to the interval certificate of 211 (G < −10⁻⁸ on [17, 41/2]). The memo acknowledges it in
§6.3 but omits it in §9. Correct label: **assisted PROVED (rel. certificate of 211, CITED)**.

L-3. **Cross-check (2) and §6.4 — actual scope of the novelty of the asinh corollary.** For ε > 1 the exclusion
is trivial and does not need the memo: M(u) − (ε/2)asinh(u/4π) ~ ((1−ε)/2)·log u → −∞, so that already a
1×1 block of the ladder is negative. For ε = 1 it was already in the corpus (jet certificate).
The new content is exactly **0 < ε < 1**. Cross-checked: `RULES_AVOID.md` B4, README index
(entries "asinh comparator") and grid record only ε = 1; the "Reusable general filter" does not apply
(D is not o(1/u)); non-positivity with ε = 1 does not imply that for ε < 1. The novelty holds in that
range.

L-4. **Cor. 4.1 — non-effectiveness must be declared** (I.2), as well as the fact that, as a tool, it only informs in
the branch where K_M is PSD (in the other branch the statement is true for trivial reasons:
K_M − εK_{M0} ⪯ K_M). It is logically unconditional; it is not information independent of the target.
It is not an error; it is scope that must appear in the record.

L-5. **Summary of §4, second point.** "One exists if and only if M is positive-real on Π and has at
least one pole on the axis": the second clause is redundant. If M is positive-real, c_M = 0 and
M ≢ 0 force μ_M ≠ 0. Correct statement: there exists an admissible nonzero positive-real comparator
⟺ M is positive-real on Π. Minor.

L-6. **Lemma 1.2, final sentence** ("the condition is also necessary"). (i)/(ii) are not necessary:
an X accumulating only at 0 with Σu = ∞ also violates Blaschke on Π and gives uniqueness of the interpolant
F (both functions are of bounded type on Π). The only thing missing in that case is identifying M with F
(§7.5). The sentence should say: the exact condition for uniqueness of the interpolant is
Σ_{u∈X} u/(1+u²) = ∞. Minor.

L-7. **Sandbox wording (Theorem 3.1 point 1, Cor. 2.2, F3).** Point 1 and Cor. 2.2 are
reformulations of the target in terms of the localization of the poles of M; rule 1 of the brief
forbids reasoning by reduction of that type and B3 forbids recording reformulations as a result. The
proof does not need it: "M − εM0 extends to a positive-real function" and the boundary measure suffice.
Cor. 2.2 must not be recorded in the index or the grid; in the record, the conclusion is stated through
the boundary measure, not through pole localization.

L-8. **§7.4.** Depends on the "Primitive comparisons" lemma of 211 (CITED); cross-checked: the lemma requires D
odd and real-analytic on all of ℝ and all primitive blocks of an open interval of (c,∞),
c = ½, and concludes full PSD. The memo uses it within that scope (M0 with a gap of the measure
around 0). Correct; label CITED + PROVED appropriate.

No error was found in Theorem 2.1, Theorem 3.1 or Cor. 4.1. The
unconditional/conditional split is correct with precision L-4 and correction L-5.

### I.4 Corrected statement, label and scope

**Rigidity lemma (PROVED relative to C1–C3, CITED).** Let X ⊂ (0,∞) have an accumulation point in
(0,∞) or satisfy Σ_{u∈X,u≥2} 1/u = ∞ (e.g. the ladder 31.5 + n), ε > 0, and M0 positive-real on Π, real
on (0,∞), with Herglotz data (c_0, μ_0). If K_M − εK_{M0} is PSD on every finite subset of X,
then M − εM0 extends to a positive-real function on Π, the boundary measure of M is
Σ_k r_k(δ_{τ_k}+δ_{−τ_k}), c_0 = 0 and εμ_0 ≤ μ_M. Contrapositive (logically unconditional, not
effective): if c_0 > 0, or μ_0 has a continuous part, or an atom outside {±τ_k}, or μ_0({τ_k}) > r_k/ε,
there exists a finite block of X with negative energy for K_M − εK_{M0}; neither the size nor the
vector is given.

**asinh corollary (PROVED rel. C1–C3).** K_M − ε·K_{½asinh(u/4π)} is not PSD on the ladder for
any ε > 0. New content: 0 < ε < 1 (ε = 1 already certified in 211; ε > 1 trivial by 1×1 blocks).

**Hyperbolic instance (assisted PROVED, rel. certificate of 211).** For a = 2π Dirichlet, the
necessary condition of the lemma coincides with U_Phi = 0; the closure of 211 is the verification of a foreign
atom. For other a > 0 Dirichlet the lemma gives the necessary condition (PROVED) but not the exclusion without
a per-atom certificate. Robin and sums: ARGUED.

Scope: only positive-real comparators on the same carrier (or after a common congruence), domination
at all sizes. It does not cover general PSD kernels, non-common congruences, joint
compensations, blocks of bounded size, a fixed window, or the primitive discrete ladder (OPEN, §7.4).
It is not a sign step.

### I.5 What may be recorded in the index and the grid

It may be recorded, with this text:

> **Phase 212, positive-real comparators on the power ladder — NO-GO with class, PROVED
> relative to three cited classical theorems (integral representation of positive-real functions,
> Pick interpolation, Blaschke condition).** `ROUND_001_L.md`, Theorem 3.1 and Cor. 4.1; review
> `REVIEW_001_LC.md`. Class: kernels [M0(u)+M0(v)]/(u+v) with M0 positive-real on Re u > 0 and real on
> (0,∞), compared with the ladder kernel on the same carrier or after a common congruence, with
> domination K_M − εK_{M0} ⪰ 0 at all sizes on the ladder 31.5 + n (or any set
> of nodes with Σ1/u = ∞ or with interior accumulation). Conclusion: M0 has no linear term and its
> boundary measure is dominated by (1/ε) times that of M, which under that hypothesis is purely atomic;
> excluded, for the corresponding ε, are every linear term, every continuous part, every foreign
> atom and every mass larger than r_k/ε. New consequence: ½asinh(u/4π) is excluded for every
> 0 < ε < 1 without a certificate (ε = 1 already recorded; ε > 1 trivial). The small hyperbolic comparison
> a = 2π of 211 is an instance (same necessary condition; its closure still depends on the
> interval certificate). Non-effective exclusion: gives no block or vector. It does not cover general PSD
> kernels, non-common congruences, joint compensations, bounded sizes, a fixed window, or the
> primitive discrete ladder. It contributes no sign.

It may not be recorded: (a) Cor. 2.2 or point 1 of Theorem 3.1 as a result (reformulation, B3;
and wording outside the sandbox); (b) "the boundary measure of M is purely atomic" without the hypothesis;
(c) the Robin and sum variants as PROVED; (d) the exclusion of a = 2π as "without certificate";
(e) any reading of the memo as a restriction on spaces ℋ that do not come from a comparator
of this class (§7.1 of the memo proves that outside the class there is no restriction).

---

## Part II — ROUND_001_C

### II.1 Cross-check of (M1)–(M5) against phase 211

- **(M1)** GRAM §18.1: (GRAPH) and (A-GRAPH) agree with what is cited (T, Lg, C, F, G). Correct.
- **(M2)** GRAM §18.2: the text fixes a finite list of κ_i, 0 < a < π·min(1, min κ_i), 0 < γ < 2a, and
  proves continuity B_a² → H_γ × H_γ of P ↦ (F,G) and of the form of (A-GRAPH), "without presupposing PSD".
  For integer scales the condition is 0 < a < π, as the memo says. The constant depends on (a,γ).
  Redone here, the only ingredient deferred to §17.7: ‖F(m²·)‖_{H_γ} ≤ e^{−γ(m²−1)/2}‖F‖_{H_γ}, hence C
  is bounded on H_γ for every γ > 0. (M2) says exactly what the memo uses. Correct.
- **(M3)** GLOBAL, "Squarefree scales": holomorphy of z ↦ P_z on Re z > a/π with values in
  B_a² and bound C_δ(1+|z|)^{13/4} on Re z ≥ δ: literal. The claim about E_z is added by the memo;
  verified: sup_{t≥1} e^{at}|∂_t^j e^{−πzt}| ≤ (π|z|)^j e^{a−π Re z}.
- **(M4)** (MOB-P) literal in GRAM §18.3, absolute in B_a²; the modal expansion and b_λ = q^{−1/2}f_{d,q}
  recomputed (λ = kn², k^{5/4}n² = λ^{5/4}n^{−1/2}). Correct.
- **(M5)** GRAM §17.2–17.3: (RES-SOS) and D_q > 0 literal, valid at y = 0. The bound D_q ≥ c_*I_q
  (§17.5) is stated there for a family with parameter 0 < ε ≤ 1; it was not checked here whether it covers
  y = 0. It does not matter: the memo only uses D_q > 0.

### II.2 Verification of the steps

- **Lemma 1.** ‖Vc‖² = A_0 − ρ ≤ A_0 ≤ |A_0| ≤ C_a‖P(c)‖². Correct; does not assume a sign. A square
  bounded by a form continuous in a norm is continuous in that norm: immediate, no gap.
- **(R0).** The functional is well defined on the quotient (it vanishes where P(c) = 0), Hahn–Banach on
  the complex Banach space B_a², composition with a holomorphic map: correct. The values
  N_g(k) do not depend on the chosen extension.
- **(R1), growth class.** H = N/(z+1)⁴ is holomorphic and bounded on Re z ≥ δ; the quotient by
  finite Blaschke factors of the half-plane Re z > δ is bounded and continuous up to the boundary, with
  modulus ≤ ‖H‖_∞ on the boundary; the Phragmén–Lindelöf principle for bounded functions gives the
  interior bound. Product: Π(1 − 2(z₀−δ)/(k+z₀−2δ)) → 0 ⟺ Σ1/k = ∞. Correct. Polynomial growth
  on a half-plane **is sufficient** (after dividing by a polynomial the function is bounded; the
  Blaschke condition of the bounded class applies). No exponential-type theorem is needed.
- **(R2), nodes.** Correct: N_g − αN′_g vanishes on {θ = α}, hence N_g = αN′_g; then N′_g
  vanishes on {θ ≠ α}.
- **Proposition 3.** Correct; does not assume a sign. For RES-SOS it coincides with (TAIL-ZERO) +
  (NO-FIN-MARGIN) of GRAM §18.7 (f_{d,q} has finite support): not new.
- **Proposition 4.** Trivial and correct.
- **Observation 5.** Recomputed against STATEMENT_001 §2: x = δ_m − δ_k gives x*𝔸x = 2B(0) − 2B(log(m/k));
  for |d| < log 2 − 2T_0 the arithmetic part of B(d) is zero; F̂_0 = (τ²+¼)|ĝ|⁴ = O(τ^{−2}), so
  that τ²m(τ)F̂_0² is integrable and B is C² and even near 0. Correct relative to STATEMENT_001 §2 (not
  cross-checked against the text of the paper, as the memo itself warns).
- **Circularity.** None.

### II.3 Counterexample hunt

Exact toy of the same structure: A_toy[c] = ∫_1^∞ |Σ_k c_k e^{−πkt}|² dt (form continuous in the
graph norm, PSD, with exact system V c = Σ c_k e^{−πk·} and ρ = 0). Does it admit a square
depending only on the coefficient c_1? The relative distance of e^{−πt} to the span of {e^{−πkt}}_{2≤k≤K}
in L² is exactly Π_{k=2}^K (k−1)/(k+1) = 2/(K(K+1)) → 0 (Müntz formula, which is the same
Blaschke product as in (R1)). Hence inf{A_toy[c] : c_1 = 1} = 0 and no square w|c_1|², w > 0,
fits in an exact identity: the toy confirms the theorem and does not refute it. With lacunary nodes
(k = 2^j) the product does not tend to 0 and the square does fit: the divergence hypothesis is necessary.
**PROVED** (closed computation). No counterexample to Lemma 1, (R0), (R1) or (R2) was found.

What does exist, and limits the title of the memo: continuous functionals whose INDEX or WEIGHTS are
arithmetic, for example ℓ_{m,t₀}(c) = (TP(c))(t₀) − m^{−1/2}(TP(c))(m²t₀) with weight Λ(m). Their
coefficients in k are values of a holomorphic function of k, as (R0) requires, and do not fall into class 𝒜.
The memo acknowledges it in §7(i); the title and §4 must be consistent with it (C-2).

### II.4 Errors and gaps (with location)

C-1. **Modes version of (R1), (R2), class 𝒜 "in the mode index", instance 5 — gap.**
The "mode coefficients" of a functional are not uniquely defined on finite vectors c:
no finite c isolates a mode (b = δ_λ requires c_{λn²} = μ(n)n^{−1/2}, of infinite support). The memo
applies (R1) to an operator given as a "selection 1_S(λ) of a continuous operator", identifying its
formal coefficients x_λ with n_g(λ) without proving it. Missing lemma (PROVED here): if
ℓ(c) = Σ_λ b_λ(c)x_λ for every finite c, ℓ is continuous in the graph norm and
Σ_N d(N)N^{−1/2}|x_{λN²}| < ∞ for each λ, then n_g(λ) = x_λ. Proof: by (MOB-P) and continuity,
ℓ̃(E_λ) = λ^{−5/4}Σ_n μ(n)n^{−1/2}ℓ(δ_{λn²}) = λ^{−5/4}Σ_{n,n′} μ(n)(nn′)^{−1/2}x_{λn²n′²}
= λ^{−5/4}Σ_N N^{−1/2}x_{λN²}Σ_{n|N}μ(n) = λ^{−5/4}x_λ, with the reordering justified by
absolute convergence. In instance 5, x_λ = 1_{m²|λ}⟨h_λ, g⟩ decays exponentially and the
hypothesis holds. With this lemma the modes version and instance 5 become PROVED; without it they are
ARGUED.

C-2. **§4, instance 2, last sentence — false as written.** "The index 'squarefree class' cannot be
part of the index of any exact system." What is proved is that no square
can DEPEND only on coefficients of a set of nodes with divergent complement (in particular
on finitely many classes). An exact system may be indexed by d, by m or by any
arithmetic label, provided each functional is continuous in the graph (example of II.3). It should
be replaced by: "no square of an exact system can depend only on the coefficients of
a family of classes whose complement is divergent".

C-3. **§4, final paragraph — unproved claim, false in its literal form.** "The only classical
arithmetic function passing filter (R0) as a twist is log k." Every restriction to the integers of
a holomorphic function of polynomial growth on the half-plane passes the necessary condition (k^s,
k^{it}, polynomials in log k); and (R2) says nothing about twists without a divergent level set
(φ(k)/k, σ(k)/k, e(αk) with α irrational): neither excluded nor admitted. It must be removed or left as an
unlabelled observation. For irrational e(αk) an exclusion by an exponential-type argument
plus logarithmic integrability on the boundary is plausible (ARGUED, not written in the memo).

C-4. **Short answer, §9 and title — scope of "arithmetic twist".** (R2) covers only twists θ
with a value α such that {θ = α} and {θ ≠ α} are both divergent (characters of modulus q ≥ 2, non-constant
Ramanujan sums, μ, μ², Λ, indicators). The sentence "no square can depend on arithmetic
indices" is not proved and is not true (C-2, II.3). The statement must carry the exact class.

C-5. **Novelty overstated in the cross-check.** The argument of (R1) (holomorphy of z ↦ ℓ(P_z), division
by (z+1)⁴, finite product of half-plane Schwarz factors, divergence of Σ1/d) is literally
that of GLOBAL "Squarefree scales" with "squarefree" replaced by "set of divergent reciprocal
sum"; instances 1, 2 and 6 are GRAM §18.7; instance 5 is the "Consequence
for the joint remainder" of GLOBAL. What is new with respect to the corpus is: Lemma 1 as a statement
(exactness with non-negative remainder ⟹ continuity of each square), (R2), and instances 3–4
(residue classes, characters, Ramanujan, μ, Λ, gcd). The memo half-says it ("common
generalization"); the record must say it unambiguously. There is no new tool.

C-6. **§8 — label.** "(M2) holds for the analogous form of any comb with C_a bounded on H_γ,
in particular cΛ, a_P…" is not proved in the memo or in the citation (the identity (GRAPH) uses
Σ_{m|n}Λ(m) = log n; for another comb the analogous form is not written). Label: **ARGUED**.

C-7. **Proposition 3, "Reading".** "Off cancels R_res completely" is (TAIL-ZERO) rewritten:
A_0 → 0 along the sequence with R_res ≥ √d·D_q. It adds nothing to GRAM §18.7 and must not appear
as a new result.

C-8. **Scope with respect to the identity (G) of OBJECT_SPEC.** The theorem restricts a SINGLE
identity on the integer-scale carrier at y = 0, in the coordinates c. It does not restrict objects
written per window (a_T, P_T) nor on 𝔸_M (the memo says so in §7(ii)); point (4) of the cross-check
("necessary condition on the operator V of (G)") must carry that restriction.

### II.5 Corrected statement, label and scope

**Theorem R (PROVED, relative to (M2)–(M4) of phase 211, CITED and rechecked here).** Let
0 < a < π. If a system of squares (ℋ, V) on finite coefficients at integer scales satisfies
‖Vc‖² ≤ M·A_0[c] for every c (in particular if A_0 = ‖Vc‖² + ρ with ρ ≥ 0 for every c), then for
each g ∈ ℋ:
(i) c ↦ ⟨Vc, g⟩ is continuous in the norm ‖P(c)‖_{a,2};
(ii) ⟨Vδ_k, g⟩ = N_g(k) with N_g holomorphic on Re z > a/π and |N_g(z)| ≤ C(1+|z|)^{13/4} on Re z ≥ δ;
(iii) if ⟨Vδ_k, g⟩ = 0 for every k in a set with Σ1/k = ∞, then ⟨Vc, g⟩ = 0 for every c;
(iv) if V′ satisfies the same bound and Vδ_k = θ(k)V′δ_k with {θ = α} and {θ ≠ α} both of divergent
reciprocal sum for some α, then V = V′ = 0;
(v) the same in the mode index for functionals ℓ(c) = Σ_λ b_λ(c)x_λ with
Σ_N d(N)N^{−1/2}|x_{λN²}| < ∞ (lemma of C-1).

**Corollary (NO-GO with class, PROVED).** In a single identity A_0 = Σ squares + ρ, ρ ≥ 0, on
the whole integer-scale carrier at y = 0, no nonzero square can: depend only on a
set of nodes with divergent complement (finite support, finitely many squarefree
classes, a residue class, multiples of g ≥ 2, fixed gcd(k,q)); be the twist of a continuous
functional by an additive or multiplicative character of modulus q ≥ 2, a non-constant
Ramanujan sum, μ, μ² or Λ; be the selection of a set of modes with divergent complement applied to
a continuous operator, alone or added to a continuous term. The same holds with "‖Vc‖² ≤ M·A_0" instead
of the identity.

Not excluded: squares continuous in the graph with arithmetic labels or weights (dilation
index m, weights Λ(m)); twists without a divergent level set; identities with a remainder without manifest
sign or non-negative only on a subspace; any object written per window or on 𝔸_M
(there only Observation 5, PROVED relative to STATEMENT_001 §2). It is not a sign step.

### II.6 What may be recorded in the index and the grid

It may be recorded (index 06, residue R9, dead subroutes; grid), with this text:

> **Phase 212, extended system of squares with arithmetic selection or twist at nodes or modes —
> NO-GO with class, PROVED (relative to GRAM §18.2 and to the holomorphy of z ↦ P_z of GLOBAL "Squarefree
> scales").** `ROUND_001_C.md`, Lemma 1, Theorem R, Corollary 2; review
> `REVIEW_001_LC.md` (lemma on uniqueness of modal coefficients included there). In a single identity
> A_0 = Σ squares + non-negative remainder on the integer-scale carrier (y = 0), each square
> is continuous in the graph norm and its coefficients in k are the integer values of a holomorphic
> function of polynomial growth on a half-plane; hence no nonzero square can
> vanish on a set of nodes or modes of divergent reciprocal sum, nor be the twist of
> a continuous functional by a function with a divergent level set of divergent complement
> (characters of modulus q ≥ 2, non-constant Ramanujan sums, μ, μ², Λ, indicators of residue
> classes, of multiples or of fixed gcd). It generalizes with the same instrument GRAM §18.7 (finite
> support) and GLOBAL "Squarefree scales" (squarefree tail, discontinuity of S_sq); what is
> new is the class, not the tool. It does not exclude continuous squares with arithmetic index or weights
> in the dilation, twists without a divergent level set, remainders without manifest sign, or
> per-window objects or objects on 𝔸_M. It contributes no sign. The direction of R9 in formulation (S) remains
> open with a single modulus-of-continuity restriction (Observation 5).

It may not be recorded: (a) "no square can depend on arithmetic indices" or "the squarefree class
index cannot be part of an exact system" (C-2, C-4); (b) "log k is the only
admissible arithmetic twist" (C-3); (c) the genericity in the comb of §8 as PROVED (C-6);
(d) Proposition 3 as a new result (C-7); (e) the closure of R9: the memo does not close it.

---

## Part III — Verdict

- **ROUND_001_L: ACCEPT with corrections.** Mathematical core correct and complete relative to three
  well-stated classical theorems with hypotheses satisfied. Corrections: L-1, L-2 (labels),
  L-3 (new range 0 < ε < 1), L-4 (non-effectiveness), L-5, L-6 (minor), L-7 (sandbox wording and
  non-recording of Cor. 2.2).
- **ROUND_001_C: ACCEPT with corrections.** Lemma 1 and Theorem R (nodes) correct. Corrections: C-1
  (missing lemma in the modes version; supplied above), C-2 to C-4 (overstatements that must be
  withdrawn), C-5 and C-7 (novelty), C-6 (label), C-8 (scope).

Neither memo contributes positivity of the form; both are discard tools and must
appear as such.
