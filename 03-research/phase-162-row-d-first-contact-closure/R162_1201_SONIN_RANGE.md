# R162_1201 — The Sonin range question as operator theory — **NO-GO (PROVED)**, four exact structures

Note. Inputs: README (F1–F4, rounds 1–11), R162_590, R162_1101 (Thm 5.1
Riesz collapse, Thm 2.1), R161_011 §4 ((4.2)), R162_402 (Thm 1.3, Lemma 1.2), R162_801 (L2), Paper 47 eq:symbol,
eq:form, lem:firstcontact, eq:Gammaenergy, subsec:collars.

**Question.** H = H_{T_*} = Π A_T Π on P_T (Π = projection onto the primitive space), N = ker H finite-dimensional,
H ≥ 0. Is Π e^{a_m t} ∈ closure(ran H) = N^⊥, i.e. x_m(F) := ∫_I F(u)e^{a_m u}du = 0 for F ∈ N (a_m = 2m+½, m ≥ 1)?
(x_m = K_F(−a_m) = εK_F(a_m).)

**Labels.**
- Lemma 1.1 (Gamma lattice = exponent spectrum of the archimedean kernel; m=0 is the Tate pair) PROVED.
- Thm 1.2 (exterior Gamma field: (𝒦F)(t) = Σ_{m≥1} x_m e^{−a_m t} for t > T, F ∈ P_T) PROVED.
- Thm 2.1 (exact lattice system (S_m); Jordan/secular term x'_m) PROVED. **New.**
- Thm 2.2 (completeness: {(S_m)}_{m≥1} ⟺ HF = 0; hence "(S) forces x = 0" ⟺ N = {0}) PROVED. **Restatement, E1.**
- Thm 3.1 (Euler regime = comb sampling of the exterior field: Σ_{m≥1}Λ(n)n^{−2m−1}x_m = w_n G(log n), log n > T) PROVED. **New.**
- Thm 4.1 (Müntz–Szász sharpening: Gate 1 ⟺ x_m = 0 on N for m in any S with Σ_S 1/m = ∞) PROVED.
- Prop 4.2 (Stieltjes form: g_F(q) = Σ x_m q^m is the Cauchy transform of F on the cut [e^{−2T},e^{2T}]; comb = q-dilations) PROVED.
- Thm 5.1 (NO-GO: λ-shift and falsifier transport) PROVED.
Gate 1 OPEN. No label moves.

## 0. Corpus check

Grep "secular", "Jordan", "Stieltjes", "Müntz", "exterior field", "e^{a_m t}", "d_{m,N}" in phases 150–162: the
exterior Hankel form is Paper 47 eq:Gammaenergy (its L²-norm on (T+δ,∞)); d_{m,N} and D_N are Paper 47
subsec:collars (collar balance); the FP value μ_m^reg is R162_402 Lemma 1.2; Müntz faithfulness is the proof below
eq:Gammaenergy (all m). New here: the lattice-by-lattice system with the secular term (Thm 2.1), its completeness
(Thm 2.2), the Gamma resummation of the Euler channel (Thm 3.1), the divergent-harmonic sharpening (Thm 4.1), the
Stieltjes/q-dilation dictionary (Prop 4.2). None is a closing identity.

## 1. The archimedean operator and the Gamma lattice (answer to (a))

κ(u) := e^{−|u|/2}/(1 − e^{−2|u|}) = Σ_{k≥0} e^{−a_k|u|}, a_0 = ½.

**Lemma 1.1.** From ψ(z) = −γ + ∫_0^∞ (e^{−x} − e^{−zx})/(1−e^{−x})dx at z = ¼ + iτ/2, x = 2u:
m(τ) = c_0 − κ̂(τ), i.e. the Gamma multiplier is M = c_0 − 𝒦, 𝒦 = convolution by κ(|·|) (Hadamard finite part at
u = 0, absorbed with c_0). The continued symbol μ(a) := m(−ia) = ½[ψ(¼+a/2)+ψ(¼−a/2)] − log π has simple poles
exactly at a = ±a_k (k ≥ 0); near a_k (from ½ψ(−k+w) = −1/(2w) + O(1), w = −(a−a_k)/2), μ(a) = 1/(a−a_k) + μ_k^reg + O(a−a_k),
μ_k^reg = ½[ψ(k+½)+ψ(k+1)] − log π (= FP d_Γ of R162_402 Lemma 1.2).

So (a) answered: **e^{at} is a generalized eigenfunction of the full-line M with eigenvalue μ(a) only for |Re a| < ½**;
the Gamma lattice {a_m} is exactly the set of *singular points* of the eigenvalue function (the exponent spectrum of
κ), not a set of eigenvalues. The point a_0 = ½ is the Tate pair; primitivity is x_0^± = A(F), B(F) = 0.

**Thm 1.2 (exterior Gamma field).** For F ∈ P_T and t > T, (𝒦F)(t) = Σ_{k≥0} e^{−a_k t}∫F e^{a_k u} = G(t) :=
Σ_{m≥1} x_m e^{−a_m t} (k = 0 killed by B/A-moment), absolutely convergent since |x_m| ≤ (2T)^{1/2}e^{a_mT}‖F‖. For
t < −T symmetrically with εx_m. Hence for the uncompressed A = M − C (C = Σ_{n∈N_T} w_n(S_{ℓ_n}+S_{−ℓ_n}),
ℓ_n = log n), (AF)(t) = −G(t) − (CF)(t) on t > T, and = −G(t) exactly for t > 3T.
*Proof.* For u ∈ I, t > T: κ(t−u) = Σ e^{−a_k t}e^{a_k u}; Fubini (geometric convergence). ∎

Gate 1 (all m) ⟺ G ≡ 0 ⟺ F = 0 (Müntz, eq:Gammaenergy). The data sit in the *exterior far field* of the archimedean
potential of F; HF = 0 is an *interior* equation. That is the whole difficulty, and §2 makes it exact.

## 2. The exact lattice system (derived from HF = 0)

HF = 0 with F ∈ P_T means A_T F = r := αe^{t/2} + βe^{−t/2} on I (Tate space). Pair with e^{a t}1_I (form domain:
ĝ = O(1/τ)). Direct integration of κ on I gives, for t ∈ I,

  M(e^{a·}1_I)(t) = μ(a)e^{at} + Σ_{k≥0}[ e^{−(a+a_k)T}e^{−a_k t}/(a+a_k) − e^{(a−a_k)T}e^{a_k t}/(a−a_k) ].     (2.1)

At a = a_m the pole of μ cancels against the k = m term of the second sum, leaving the **secular term**
(T − t)e^{a_m t}: on I, e^{a_m t} is a rank-two (Jordan) resonance of M_I, not an eigenvector.
The comb on I: ⟨F, C_I e^{a}⟩ = Σ_n w_n[n^{a}(x(a) − ρ^+_n(a)) + n^{−a}(x(a) − ρ^−_n(a))], with collar moments
ρ^+_n = ∫_{T−ℓ_n}^T F e^{au}, ρ^−_n = ∫_{−T}^{−T+ℓ_n} F e^{au}, and w_n n^{a_m} = Λ(n)n^{2m}, w_n n^{−a_m} = Λ(n)n^{−2m−1}.

**Thm 2.1 (lattice system).** Put x'_m := ∫_I uF(u)e^{a_m u}du, J_m^± := ∫_I e^{(a_m±½)t}dt. For every F ∈ N and m ≥ 1:

 (μ_m^reg − T − Σ_{n∈N_T}Λ(n)[n^{2m} + n^{−2m−1}]) x_m + x'_m
   + Σ_{n∈N_T}Λ(n)[n^{2m}ρ^+_{n,m} + n^{−2m−1}ρ^−_{n,m}]
   − Σ_{k≥1,k≠m} e^{(a_m−a_k)T} x_k/(a_m−a_k) + ε Σ_{k≥1} e^{−(a_m+a_k)T} x_k/(a_m+a_k)
 = α J_m^+ + β J_m^−.                                                                                   (S_m)

*Proof.* ⟨A_TF, e^{a_m}1_I⟩ = ⟨F, A_T e^{a_m}1_I⟩ (self-adjointness on the form domain) and (2.1), comb formula; the
limit a → a_m of μ(a)x(a) − e^{(a−a_m)T}x(a_m)/(a−a_m) is μ_m^reg x_m + x'_m − T x_m. k = 0 terms vanish (x(±½) = 0). ∎

The coefficient of x_m is the lattice value of the *window symbol* 𝔰_T continued to a_m (Euler part Σ Λ(n)n^{−2m−1} =
d_{m,N_T}, anti-Euler part Σ Λ(n)n^{2m}), minus T. Every other term is a *compression defect*: the secular moment
x'_m (Gamma pole), the collar moments ρ^± (comb truncation), and the Hankel couplings x_k (edges ±T).

**Thm 2.2 (completeness = restatement).** The family {(S_m)}_{m≥1}, read as linear conditions on F ∈ P_T with (α,β)
free, is equivalent to HF = 0. Hence (S) forces x ≡ 0 on N iff N = {0}.
*Proof.* (S_m) is ⟨HF, Πe^{a_m}⟩ = 0. {Π e^{a_m}}_{m≥1} is total in P_T (Müntz in x = e^{2t} on [e^{−2T},e^{2T}],
0 ∉ interval, plus Π a finite-rank correction killing only the Tate span). So HF ⊥ total set ⟺ HF = 0. ∎

**Exact obstruction.** Each (S_m) introduces at least one new unknown (x'_m; also ρ^±_{n,m}) beyond x_m: the system is
underdetermined lattice-by-lattice by the order of the Gamma pole (one), and it closes only as a whole, where it is
HF = 0 itself. No finite subsystem forces anything (a finite set of pairings has codimension ≤ L on P_T, and N is
already inside it only if the conclusion holds).

## 3. The Euler regime (answer to (b))

**Thm 3.1 (Gamma resummation of the Euler channel).** For every n with ℓ_n = log n > T and F ∈ P_T,

  Σ_{m≥1} Λ(n) n^{−2m−1} x_m = w_n G(ℓ_n) = w_n (𝒦F)(log n).                                              (3.1)

Summing over n > e^T: Σ_{m≥1} (Σ_{n>e^T}Λ(n)n^{−2m−1}) x_m = Σ_{n>e^T} w_n G(log n), absolutely convergent; in
particular the complete values −ζ'/ζ(2m+1) enter Gamma data only through the sampled exterior field
Σ_{n>e^T} w_n G(log n) plus the finitely many n ≤ e^T (partial, collar-truncated, as in (S_m)).
*Proof.* Σ_{m≥0} n^{−a_m}e^{a_m u} = κ(ℓ_n − u) for u < ℓ_n; m = 0 vanishes by primitivity; Thm 1.2. ∎

So the absolutely convergent Euler-product regime is **the comb applied to the archimedean potential, evaluated
outside the window**: it is the MC cross term of A, not new arithmetic. For n > e^{2T} (all but finitely many of the
terms that make the partial sums into −ζ'/ζ(2m+1)) the points log n lie beyond 2T, where HF = 0 says nothing about
G (Thm 1.2: exterior AF is free). Inside N_T the Euler sums are partial sums of a finite nonnegative weight vector,
and Λ*1 = log restricted to N_T is the statement "w = w^Λ" (R162_801 L2): a weight value, not a relation (S) can use.
Euler multiplicativity would act on G through q-dilations (Prop 4.2), and the window only sees the dilations with
n < e^{2T}.

## 4. Two sharpenings (true, not closing)

**Thm 4.1 (Müntz–Szász).** Let S ⊂ ℕ with Σ_{m∈S} 1/m = ∞. If x_m(F) = 0 for all F ∈ N and m ∈ S, then N = {0}.
Conversely for each F ∈ N∖0, Σ_{m: x_m(F)=0} 1/m < ∞.
*Proof.* x_m(F) = ½∫ y^{m} y^{1/4}F(½log y) y^{−1}dy on [e^{−2T},e^{2T}]; on an interval [a,b], a > 0, {y^m}_{m∈S} is
dense iff Σ_S 1/m = ∞ (Müntz–Szász for [a,b], a>0; CITED: Borwein–Erdélyi, *Polynomials and Polynomial
Inequalities*, §4.2). ∎
Consequence: Gate 1 cannot be won "for finitely many m", nor lost only on a sparse set; it is all-or-nothing up to
harmonic-convergent sets, so any proof must control a divergent-density family of lattice points uniformly.

**Prop 4.2 (Stieltjes/q-dilation form).** g_F(q) := Σ_{m≥1} x_m q^m = ∫_I F(u)e^{u/2} qe^{2u}/(1 − qe^{2u}) du is
analytic on ℂ ∖ [e^{−2T},e^{2T}] and its jump across the cut is a nonzero multiple of y^{1/4}F(−½log y)·(Jacobian).
Shifts act by dilation: g_{S_{±ℓ_n}F}(q) = n^{±1/2} g_F(n^{±2}q) (exact on ℝ; on I up to the collar moments). The
q^m are joint eigenfunctions of all dilations q ↦ n²q with eigenvalues n^{2m}, which is why the comb on the
lattice produces Dirichlet sums. HF = 0 becomes a finite-part singular integral equation on the cut (kernel
(py)^{1/4}max(p,y)^{1/2}/|p−y|, p = e^{−2t}, y = e^{−2u}) with dilations n^{±2}, n ∈ N_T; Gate 1 ⟺ g_F ≡ 0.
*Proof.* Geometric series (|qe^{2u}| < 1 near 0), analytic continuation, Sokhotski–Plemelj; the kernel from §1. ∎
This is a q-difference Riemann–Hilbert problem with finitely many incommensurable dilations; its exterior solution
is again the whole of F. Recorded as a dictionary; no Λ-dependent Liouville argument is available (§5).

## 5. The NO-GO and the falsifiers

**Thm 5.1.** (i) (F1) For an eigenvector H F_λ = λF_λ, the same derivation gives (S_m) with μ_m^reg replaced by
μ_m^reg − λ; the pole/secular structure, collar defects and Hankel couplings are λ-independent, and x(F_λ) ≠ 0 by
Müntz. So λ = 0 enters (S) only as one value of a diagonal shift; its distinguishing property (bottom of spectrum,
H ≥ 0, minimality of T_*) is an inequality and is not expressible in (S). Any argument from (S) plus linear
consequences proves x = 0 for λ > 0 eigenvectors too — false.
(ii) (F3) (S), Thm 3.1, Prop 4.2 hold verbatim with Λ replaced by any finite weight vector a on N_T (deletion/κ,
Λχ₂: same Gamma factor, same lattice) and with Beurling ℓ_n (same M; Thm 3.1 with Beurling n). For DH (Gamma factor
of an odd character, lattice a_m = 2m + 3/2) the analogous system holds with its coefficients, and DH has first
contacts with nonzero Gamma data (R162_102). So no property of (S) that is shared by these systems closes Gate 1.
(iii) The only arithmetic input of (S) at fixed T_* is the vector (Λ(n))_{n∈N_T}; by Thm 2.2 the question is whether
one explicit self-adjoint operator H(w^Λ) has kernel orthogonal to a Müntz system. That is Gate 1.

- **F1.** Used λ = 0 (the Tate right side r; Thm 2.2). Passed only by restatement; (i) shows a linear use cannot pass.
- **F2.** (S) is linear in F; the (PC) orientation does not appear. Not passed.
- **F3.** Failed at the use (ii).
- **F4 (why this is not a linear graph limit).** Every identity is exact at finite T_*: finite comb N_T, finitely many
  collar moments, Gamma sums geometric (convergent for |t| > T, not a truncation limit), and the Euler completion
  n > e^{2T} in Thm 3.1 is an *evaluation* of the exterior field G at points log n, not a limit of window graphs
  (PC-ren)_N as N → ∞. R161_018 does not apply; the proof dies at Thm 2.2 (completeness) and 5.1(i), not at F4.

## 6. Verdict and residual

**NO-GO (PROVED).** The range question is answered structurally: the lattice exponentials are not eigenfunctions of the
archimedean operator but its singular exponents; compressed to I they are Jordan resonances (secular term), so
HF = 0 gives, lattice point by lattice point, the exact system (S_m) with one extra unknown per point, which closes
only as HF = 0 itself (Thm 2.2). The Euler-regime Dirichlet sums enter as the comb-sampled exterior Gamma field
(Thm 3.1), invisible to the window beyond e^{2T}. The system is λ-shift covariant (F1) and holds for every falsifier.

**Residual (sharp).** A closing argument must use the *inequality* H ≥ 0 together with (S): e.g. a Kreĭn-type
statement that the Jordan chain {e^{a_m t}, (T−t)e^{a_m t}} of M_I, perturbed by the comb, cannot become neutral
(H-isotropic) at the bottom. By Thm 4.1 it must hold on a harmonic-divergent family of m uniformly. Candidate
input: the Stieltjes positivity of κ (κ is completely monotone: 𝒦 on I is a positive Stieltjes-kernel operator,
Kreĭn string theory) against the comb — not attempted here; check R160 survey (Kreĭn strings, de Branges) first.

Add to R162_590 §1c: "Sonin range as operator theory (lattice system, secular term, Euler resummation, Müntz–Szász,
q-dilation RH problem) — R162_1201 — completeness = HF=0; λ-shift covariant; falsifier-transported | F1, F3, E1".

Files edited: this file only.
