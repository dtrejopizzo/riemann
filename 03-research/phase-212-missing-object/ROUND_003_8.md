# Round 3, option 8 — the object quadratic in the weight and the Riccati-type factorization

Selection memo, not a construction memo. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}; S_a F(t) = F(t − a); e_n = n^{−1/2} S_{log n}. Labels: PROVED / CITED / CONDITIONAL /
ARGUED / OPEN / NO-GO / NUMERICAL.

Result stated in advance: **the cross-check identifies repetition.** The requested factorization (first-order
operator whose superpotential is the comb with weights Λ, with Λ·log coming from the derivative and Λ∗Λ from the
square, closed by μ∗log²) is constructed in phase 70 (E70_10–E70_12) and analysed in phase 166
(R166_502 §5), with the SUSY reading in phase 193 (CA_G_001 §2). The memo ends at the cross-check except for two
short PROVED lemmas that delimit where the degree-two relation could still enter (§2) and the
answer to the four difficulties (§3).

## 0. Cross-check

**What was searched.** Grep in `03-research/` (all phases), `04-papers/47*`, `04-papers/48*`,
`05-meta-and-planning/` (index and crossword) and the annexes of this folder for: Riccati, Darboux,
Miura, Schwarzian, superpotencial/superpotential, SUSY/Witten, A*A, Λ₂/Lambda_2, Selberg, Bombieri,
Diamond, Leibniz, «grado dos»/degree two. Hits: Riccati in phases 29, 70, 104, 120, 122,
166, 168, 184, 193, 211; Λ₂ in 156 files, Bombieri in 341, Diamond in 95, Leibniz in 93, «degree
two» in 75 (not all were opened; the primaries cited below were opened). No hits:
Schwarzian, Miura. A search without hits does not prove novelty: a Miura transformation is
here the same substitution V = Z⁻¹δZ already recorded, under another name.

**(1) Closest antecedent, read in primary.**
- `phase-70-lee-yang-dbn/E70_12_RICCATI_CURVATURE_TEST.md` (complete): in the semigroup algebra
  {e_n}, with Z = Σ e_n, δe_n = (log n)e_n, the Euler operator A_Euler = Z⁻¹δZ = Σ Λ(n)e_n satisfies
  δ(A_Euler) + A_Euler² = Z⁻¹δ²Z, whose coefficients are exactly Λ·log + Λ∗Λ = μ∗log². Diagnosis
  of the source: «entirely on the Euler side»; it does not produce the archimedean form; a
  connection–archimedean energy comparison is requested, without its own sign.
- `phase-70-lee-yang-dbn/E70_10_DIRICHLET_SQUARE_OBSTRUCTION.md` (via R166_502 §1, checked):
  (I − V)*(I − V) = I − T_Λ + V*V with V = Σ Λ(n)e_n; the square contains V*V, whose comb of ratios
  log(p^k/q^l) has coefficients ≥ 0 and does not cancel.
- `phase-166-omega-closure/R166_502_P7_Q25_PRECHECK.md` §§5.1–5.3 (PROVED there): the Hermitian square
  V*V lives in the group algebra of ℚ₊^× (ratios), the Selberg relation in the convolution algebra of
  ℕ (products, V²); neither Selberg, nor log ζ, nor complete Z, nor the Möbius factor, nor the
  connection ∇ = δ + V eliminate the cross comb of ratios; the only declared exit is a second
  sector with sign (graded cancellation), never constructed.
- `phase-193-*/CA_G_001_MONOID_SUSY_EW_LADDER.md` §2 (PROVED, standard): a factorization
  H = A*A + E₀ with A = d/du − (log ψ₀)′ exists if and only if H ≥ 0, and the superpotential is that of the
  ground state, that is the minimizer (pattern B9); the Witten identity H = {Q,Q*} holds for every
  superpotential, hence for every comb (pattern B1). Labelled REF-D.
- Concurrent: `phase-104-*/104_13_M5_SELBERG_RICCATI_GATE.md` (exact Selberg–Riccati recurrence,
  without one-sided inequality; scale ceiling); `phase-170-*/R170_850–851` (γ = Λ·log − Λ∗Λ clashes with
  W = μ∗log²; γ + W = 2Λ·log); `phase-168-*/R168_203` (Riccati = Selberg, the non-linearity remains in a
  factor ≥ 0 whose sign is linear); IDX README NODE_001 Prop N.2 (Selberg-type identities hold
  for every Dirichlet series, each with its own system); R11_2_ORIGIN_001 («Selberg Λ∗Λ order 2
  NO-GO»); R166_502 §4 (variant «Λ₂ = μ∗log² ≥ 0 with Möbius as positive adjoint», EXCL [F3]);
  this phase: `ROUND_001_A.md` Lemma B, `ROUND_001_D.md` Lemma A and Prop. D, `ROUND_002_C.md`,
  `REVIEW_002_BC.md` C.1 and C.5; `phase-194-*/INV_F_001_DLOG_WALL_CONES.md` Theorems F1–F3.

**(2) Genuinely new object.** None. The requested factorization is, term by term, that of E70_12:
superpotential V = Z⁻¹δZ (the comb with weights Λ), «derivative» δ = logarithmic degree (which in the space
of F is ad M_t: [M_t, S_a] = a S_a, PROVED by direct computation), square V², closure Z⁻¹δ²Z = μ∗log².
It was not possible to write ℋ_T, V_T, ρ_T: what remains to be written is an operator whose Hermitian square
contains products m·n (not ratios m/n) with the weights Λ(m)Λ(n), and a manifestly ≥ 0 remainder;
Lemma 1 of §2 proves that no translation-invariant operator does so.

**(3) Why the change would avoid the difficulty of the antecedent.** It does not avoid it. The recorded difficulty
(R166_502 §5.2) is that the Riccati identity lives in V² and a Hermitian square produces V*V. The
«truly quadratic» object a·log − a∗a, or a·log + a∗a − μ∗log², does not change that: it is the same
convolution relation, written for a general weight. The only thing the task adds relative to γ
(round 2) is the non-homogeneity in c, and that non-homogeneity is a property of the relation between
weights, invisible to the form (Lemma A of ROUND_001_D; §3(i) below).

**(4) Identity that would connect with global positivity.** There is none. The only exact identity
available is (I − V)*(I − V) = I − T_Λ + V*V (E70_10), which would require the archimedean part of a_T
to be I + V*V plus something ≥ 0; the archimedean part has no atoms at log(p/q) and V*V does, with positive
sign (R166_502 §5.2, Lemma (i)). No version with Riccati repairs it (E70_12, «no-free-lunch»).

**(5) Line that breaks for cΛ and a_P.** In the Riccati identity with Z = Σ_{n≥1} e_n fixed:
for cΛ, δ(cV) + (cV)² = Z⁻¹δ²Z is false at every n with (Λ∗Λ)(n) ≠ 0 (difference (c² − c)Λ∗Λ); but
the identity holds for cΛ with Z_c = Σ d_c(n)e_n (series ζ^c) instead of Z. For a_P it holds with
Z_P = Σ_{(n,∏_{p<P}p)=1} e_n. That is, the line that breaks is «Z has all coefficients 1»,
which by Lemma A of ROUND_001_D is a consequence of the linear atoms Σ_{d|n}a(d) = log n: the breaking
is that of the linear separator, not a degree-two one, and in any case it does not occur in a sign step, because
there is no sign step.

The cross-check identifies repetition. What follows only delimits.

## 1. Where F would enter and where the quadratic form

- **F (vector).** In E70_10–12 F enters only through ‖(I − V)F‖² and ⟨G_Γ F, F⟩; the Riccati
  relation is an equality between operators that does not contain F. With rule O2 of `OBJECT_SPEC.md`,
  that is exactly the wrong location: the non-linearity is in the product of weights, not in
  how V_T acts on F.
- **Functional equation.** On the Euler side it does not enter (diagnosis of E70_12). In the space of F the
  functional equation is the reflection J F(t) = F(−t) (exchange s ↔ 1 − s on the line). Lemma 2
  shows that J is precisely what converts ratios into products; it is the only place where the
  convolution relation could touch a form in F.

## 2. Two short lemmas

**Lemma 1 (translation-invariant squares see ratios). PROVED.** Let A_x be an operator on
L²(ℝ) commuting with all translations, with symbol α_x(τ) = α_0(τ) + Σ_{2≤n<N} x_n n^{−1/2}
n^{−iτ}, α_0 measurable, x real. For F ∈ L²(I_T) with F̂ in the domain,
‖A_x F‖² = (1/2π)∫|α_x|²|F̂|², and the part of |α_x(τ)|² quadratic in x is
Σ_{m,n} x_m x_n (mn)^{−1/2} cos(τ log(m/n)). In particular no term indexed by a product mn
with m, n ≥ 2 appears with a coefficient quadratic in x, and the convolution x∗x does not figure in ‖A_xF‖².

*Proof.* |α_x|² = α_x·conj α_x; conj(n^{−iτ}) = n^{iτ}, hence the product of the terms m and n
is (mn)^{−1/2}(n/m)^{iτ}; add (m,n) and (n,m). ∎

Consequence. Any identity a_T = ‖A_xF‖² + ρ with A_x translation invariant and ρ translation
invariant has, in the part quadratic in the weights, only frequencies log(m/n): the relation
Λ·log + Λ∗Λ = μ∗log² (frequencies log(mn)) cannot be used to cancel it. It is R166_502 §5.2 written
as a symbol lemma; it is not new.

**Lemma 2 (the reflection converts ratios into products). PROVED.** Let J F(t) = F(−t). For real F and
real a, b, ⟨S_a F, J S_b F⟩ = (F∗F)(−a − b), where F∗F is the convolution, whereas
⟨S_a F, S_b F⟩ = c_F(a − b). If F is even, (F∗F)(u) = c_F(u) for every u.

*Proof.* J S_b F(t) = F(−t − b), hence ⟨S_aF, JS_bF⟩ = ∫F(t − a)F(−t − b)dt; with s = t − a,
= ∫F(s)F(−s − a − b)ds = (F∗F)(−a − b). The second is the definition of c_F. If F is even,
F(−s − u) = F(s + u) and ∫F(s)F(s + u)ds = c_F(−u) = c_F(u) (F real). ∎

Reading. An operator with two sectors, B_m = S_{log m} in one and B_n = J S_{log n} in the other, gives in
⟨B_mF, B_nF⟩ the convolution of F at log(mn): there, and only with J, the convolution relation could
speak with a form in F. On the even part of F this coincides with the autocorrelation (it adds
nothing); the difference is in the odd part, where F∗F = −c_F in the sense F∗F(u) = −c_F(u) for odd
F (same computation). This is the «graded cancellation / second sector with sign» of E70_10 option 1
and of `REVIEW_002_BC.md` C.5, already recorded as not constructed; the lemma only specifies that the second
sector is that of J and that its effect reduces to a parity sign. It is not claimed that it gives an identity
(G); the parity of the boundary class (R170_870, `RULES_AVOID.md` I3) is the antecedent that would have to be
evaded.

## 3. The four difficulties of the task

(i) **Invisible degree.** Conceded. The form is affine in the comb; by Lemma A of ROUND_001_D every
polynomial relation on Λ in [2,N), including μ∗log², is a consequence of the linear atoms, and by
Lemma B of ROUND_001_A every consequence of «Poisson + archimedean + Selberg» is one of
«Poisson + archimedean + Λ∗1 = log + Leibniz». The only thing that does not become trivial is the **locus**
Z_T = {x : a_T^x = ‖V^xF‖² + ρ^x ∀F}: if V^x is quadratic in x, Z_T can be a quadric that cuts
the line {cΛ} only at c = 1 (version (P1) of ROUND_001_D §7). That is a property of the object that
would have to be constructed, not of the Selberg relation; Lemma 1 proves that with V^x translation
invariant the quadratic part does not contain x∗x, so the quadric cannot be Selberg's.
(ii) **Selberg discard** (R170_850–851; ANNEX_INDEX_README, SELBERG_DROP and R11_2_ORIGIN; R166_502):
in force; the task contributes no operation that evades it.
(iii) **∂log wall and H_cone** (INV_F_001): the Riccati relation is the definition of δ log applied twice;
it crosses ∂log, but generically: it holds for ζ^c with its own series Z_c (§0 point 5). It is not
conic, and even so it does not break H_cone in the form, because what distinguishes c = 1 is «coefficients of Z
equal to 1», the integrality datum, which enters linearly.
(iv) **a_P.** a_P satisfies Λ_P·log + Λ_P∗Λ_P = μ_P∗(1_P·log²) with 1_P the indicator of the integers
without primes < P (NODE_001 Prop N.2; R186_005 Lemma S0). What distinguishes it from Λ is only that Z_P ≠ Z,
again a linear datum (erased in the separator Σ_{d|n}a(d) = log n at n = 2). Nothing in the factorization
uses the functional equation, which is what a_P breaks: by `RULES_AVOID.md` G1, a construction that only
fails for cΛ by integrality and never uses J has not certified the functional-equation channel.

## 4. What remains not excluded

- Non-translation-invariant operators: truncated to the window, with M_t (whose commutator with S_a
  gives a S_a, the Riccati «derivative» in the space of F), or with J (Lemma 2). None has a written
  object; that of J coincides with the graded option of E70_10 and with residue C.5 of REVIEW_002_BC.
- The residue of ROUND_002_C (X_p that see the window with diagonal paid by the archimedean form).
- Uses of the degree-two relation that do not pass through a Hermitian square of weights (for example, the
  relation entering ρ and not V). Not examined here.
None of the above is a NO-GO of the «Riccati» class: Lemmas 1–2 exclude only the use of the
convolution relation inside a translation-invariant Hermitian square.

## Result

No new mechanism; repetition of E70_10–12, R166_502 §5 and CA_G_001 §2. Two PROVED
delimitation lemmas. Not ready for construction.

## What was proved

Lemma 1 (the part quadratic in the weights of a translation-invariant square has only
frequencies log(m/n); the convolution x∗x does not appear) — reformulation of R166_502 §5.2. Lemma 2 (the
reflection J converts autocorrelation into convolution; for even F they coincide, for odd F they differ by a
sign). Identity [M_t, S_a] = a S_a (the Riccati logarithmic degree δ is ad M_t).

## What failed and why

The requested factorization is that of phase 70: its Riccati identity is in the convolution algebra
(products), the Hermitian square in that of ratios (Lemma 1), and the superpotential that would make it exact
is that of the minimizer (CA_G_001 §2). The quadratic object a·log − a∗a changes none of that: its non-
homogeneity in c is a relation between weights, which the affine form does not see and which follows from the linear
atoms. It was not possible to write ℋ_T, V_T, ρ_T nor a sign step.

## Concrete next step

If one wants to continue in this zone, the only operation with different content is that of Lemma 2: write
explicitly, for F ∈ P_T decomposed into even and odd parts, the form
Σ_{m,n<N} Λ(m)Λ(n)(mn)^{−1/2}[(F∗F)(log mn) − c_F(log mn)] and decide whether the relation
Λ·log + Λ∗Λ = μ∗log² rewrites it in terms that the archimedean form can pay in the odd sector;
first, cross-check it against R170_870 (parity) and E70_10 option 1. Without that written object it is not relaunched.
