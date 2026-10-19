# R162_903 — Round 9: a nonlinear exact use of Λ*1=log (Möbius/Gram/lattice) — **NO-GO (PROVED), five structural theorems**

Round 9. Inputs: README (F1–F4, rounds 1–8), R162_590, R162_801 (L1–L5, residual),
R162_502 B1, R162_701 (Lemma 1.1, 2.1, 2.2), R162_504 (Perron), R162_703 (deletion model).
Conventions as in R162_502: X=e^{2T}, M_T(α)=P_TΣα(m)m^{-1/2}τ_{log m}P_T, Z=M_T(1), Z^{-1}=M_T(μ), X̂ = position
operator (written X̂ to avoid a clash with X=e^{2T}), ψ_T Perron ground state, F ∈ N = ker H_{T_*}.

**Status.** The candidate (integer-structured Gram matrix of Möbius images of ψ_T and F across T_n=½log n, with a
rank/determinant contradiction) is **built and refuted**. Five PROVED statements:
- Prop 2.1: floors do not survive an L² pairing; Gram entries across windows are hyperbola sums = sawtooth (linear).
- Thm 3.2 (terminating BCH): log Z = M_T(Λ/log) exactly (finite sum), and B2.1 is e^{ad log Z}X̂ truncated at order 1
  by commutativity of 𝒜_T. New as a derivation of B2.1; it shows every nonlinear-in-Λ identity (Selberg, Λ^{*k}) is a
  consequence of one exponential relation valid for any unipotent coefficient system.
- Thm 4.1 (Cauchy–Binet/Sylvester collapse) and Thm 4.2 (Moore collapse): every continuous GL_N(ℤ)-congruence
  invariant of an indefinite real form is a function of det; integrality of the Möbius/floor matrices is invisible to
  continuous data. The definite case (Gram at first contact) has lattice invariants, but they are a-independent.
- Thm 5.1 (tensor lift): any exact use of degree 2d in F is a degree-2 use for the tensor Weil operator on
  ℕ^d-indexed data, with weights Σ_i 1⊗…⊗a⊗…⊗1; the same walls apply. "Nonlinear in F" adds no arithmetic.
- Prop 6.1: Perron positivity + |μ|≤1 gives only pointwise domination |Z^{-1}F| ≤ Z|F|, valid for Beurling and Λχ₂.
Gate 1 stays OPEN. The residual of R162_801 is sharpened (§8).

## 0. Corpus check

- R162_701 Lemma 2.1: ZZ^{-1}=I uses 1*μ=δ_1 only; Lemma 2.2: floor remainders = ψ-sawtooth = (PC) comb, linear.
- R162_801 L2 (Möbius ledger per window), L4 (concavity in weights), L5 (Theorem M kill of asymptotic ledger use).
- R162_502 B1 (exact compressed semigroup), B3 (inputs (i)–(iv) and their kills).
- R162_504 / 702: Perron–Frobenius for A_T; support class 𝒞 contains κ-models with first contacts.
- R162_802: conserved Haynsworth index (inertia) across T.
- R160_D4 Thm 5.1: dilations/translations of tests are window shifts.
None of these contains Thm 3.2, Thm 4.2 or Thm 5.1. Grep for "Moore", "Sylvester", "Cauchy–Binet", "BCH", "tensor
lift" in phases 150–162: no hits on these mechanisms (Haynsworth inertia in R162_802 is the T-flow version of 4.1).

## 1. The candidate, stated sharply

Family: u_{n,k}^± = M_{T_n}(μ)^{k}ψ_{T_n}, v_{n,k} = M_{T_n}(μ)^kF (zero-extended), T_n=½log n. Gram
𝔊 = [⟨u,u'⟩]. Hoped-for mechanism: (a) 𝔊 = A^T K A with A an integer matrix built from ⌊x/n⌋ and μ; (b) at a first
contact a rank drop or a determinant identity for 𝔊; (c) incompatibility with integrality of A, with |μ|≤1, or with
ψ>0. We compute each piece exactly.

## 2. Where the floors actually live (PROVED)

**Prop 2.1.** Let h_x(t)=e^{t/2}1_{[0,log x]}(t) (the half-density indicator; the only vectors on which Z produces
floors: (Zh_y)(t) = e^{t/2}⌊y e^{-t}⌋ on t≥0). Then
  ⟨h_x, Z h_y⟩ = ∫_1^x ⌊y/u⌋du = Σ_{m≤y}(min(x, y/m) − 1)_+ =: D(x,y),
a piecewise-linear function of (x,y) with breakpoints on xm=y. For the Gram of ψ_{T_n}, F or their M_T(μ)-images
no floor appears at all: entries are Σ α(m)β(k)(mk)^{-1/2}⟨Pτ_{log m}G, Pτ_{log k}G'⟩, real-analytic in the
autocorrelation data.

*Proof.* Fubini, u=e^t, then Σ_{m≤y/u}1 = ⌊y/u⌋ and ∫_1^x⌊y/u⌋du summed termwise. The second claim is B1(d). ∎

So the "integer structure ⌊x/n⌋" of the candidate is present only pointwise. Every L² pairing replaces ⌊y/u⌋ by
u + ½ + sawtooth (R162_701 Lemma 2.2); the sawtooth part is linear in the (PC) comb. **Failing line for (a):** the
integer matrix A exists only as the coefficient matrix α(m)β(k) ∈ ℤ, not as ⌊·⌋-entries of 𝔊.

## 3. The algebra 𝒜_T and the terminating BCH (PROVED)

𝒜_T := {M_T(α)} is a commutative algebra (B1(a)) and M_T: (arith. functions, *) → 𝒜_T is a ring homomorphism
whose kernel contains all α supported on n ≥ X.

**Lemma 3.1 (nilpotency).** (Z−I)^K = 0 for K > 2T/log 2. More precisely (Z−I)^k = M_T(d_k^≥2), with d_k^≥2(n) the
number of ordered factorizations of n into k factors ≥2; it vanishes on n<2^k. In the lattice basis
e_n := n^{-1/2}P_Tτ_{log n}G (any G ∈ L²(I_T)), Z e_n = Σ_m e_{mn} is integral unipotent, Z^{-1}e_n = Σ μ(m)e_{mn}.
*Proof.* (1−δ_1)^{*k} is supported on n ≥ 2^k; apply the homomorphism. B1(a) for the basis action. ∎

**Theorem 3.2 (terminating BCH).** log Z := Σ_{k=1}^{K}(−1)^{k+1}(Z−I)^k/k = M_T(Λ/log), and
  Z X̂ Z^{-1} = e^{ad_{log Z}} X̂ = X̂ + [log Z, X̂] = X̂ + M_T(Λ),
the series terminating after one commutator. Consequently B2.1 of R162_502, and every polynomial identity among
Z, Z^{-1}, M_T(Λ), M_T(Λ^{*k}), M_T(Λ·log), X̂ (Selberg's Λlog+Λ*Λ=μ*log², R162_501; Λ^{*k}) follows from the
single relation Z = exp M_T(Λ/log) together with [X̂, M_T(α)] = −M_T(α·log).

*Proof.* In the ring of arithmetic functions, log(δ_1+(1−δ_1)) = Σ(−1)^{k+1}(1−δ_1)^{*k}/k is the coefficient
sequence of log ζ(s) = ΣΛ(n)/log n·n^{-s} (formal identity, n ≥ 2). Apply M_T (finite by 3.1). Then
[log Z, X̂] = −[X̂, M_T(Λ/log)] = M_T(Λ). Next [log Z, M_T(Λ)] = 0 because 𝒜_T is commutative, so ad^2=0 and the
exponential series stops. For the second claim: [X̂,·] maps 𝒜_T into itself by the log-multiplier rule, so the
subalgebra generated is 𝒜_T[X̂] with the stated relations; any element of 𝒜_T built from 1, μ, Λ is expressed
through exp/log of M_T(Λ/log) and multipliers. ∎

**Reading.** "Λ*1 = log", in operator form, is "Λ/log = log 1" in the arithmetic ring, i.e. the Euler exponential.
For any coefficient system a with a(1)=1 (DH, Λχ₂, Beurling on 𝒩_B) the same holds with Λ_a := log-derivative
coefficients. The Λ-specific content is therefore exactly one linear datum per n: **the weight in the Weil form equals
the log-derivative coefficient of Z, and Z has coefficients 1.** Deletion and κ-models keep Z and violate the first
clause; DH violates the second; Λχ₂ and Beurling satisfy both for their own Z. Nonlinear-in-Λ identities add nothing
beyond this list (they are consequences of 3.2).

## 4. Integrality under congruence (PROVED)

Every Gram construction of §1 has the form 𝔊 = A^T K A where A is the (integer) coefficient matrix of the
M_T(α_k), α_k ∈ ℤ[1, μ, compositions] in the basis e_n, and K = [⟨e_m, e_n⟩] (or K^H = [⟨e_m,He_n⟩] for Weil-form
Grams).

**Theorem 4.1 (Cauchy–Binet/Sylvester collapse).** (a) Every minor of 𝔊 is Σ_{S,S'} det A_{S,I} det K_{S,S'} det A_{S',J}
with integer coefficients det A_{·,·}. (b) If the α_k are M_T-unipotent products (as all Z^{±k} are), A is
unitriangular in the order of n and det 𝔊 = det K on the corresponding square block; inertia(𝔊) = inertia(K) whenever
A is square invertible. (c) (a)–(b) hold verbatim for Λχ₂ (A ∈ ℤ, entries 0,±1), Beurling (A ∈ {0,1} on 𝒩_B) and for
deletion/κ-models (A identical to ζ's). For DH they hold with A real.
*Proof.* Cauchy–Binet; unitriangularity from Lemma 3.1; Sylvester's law of inertia. ∎

So a rank drop of 𝔊 is a rank drop of K (a property of F alone), and determinants carry no trace of A. The
candidate's step (b) is a property of the autocorrelation data of F, not of μ.

**Theorem 4.2 (Moore collapse).** Let N ≥ 2, p,q ≥ 1, c ≠ 0, and Q_c = {K ∈ Sym_N(ℝ): sig K = (p,q), det K = c}.
If f: Q_c → ℝ is continuous and f(A^TKA) = f(K) for all A ∈ SL_N(ℤ), then f is constant.
*Proof.* Q_c is one orbit of G = SL_N(ℝ) under K ↦ g^TKg; fix K_0 and put f̃(g) = f(g^TK_0g). f̃ is left-invariant
under H = SO(K_0) ≅ SO(p,q) and right-invariant under Γ = SL_N(ℤ), hence a continuous H-invariant function on G/Γ.
H is closed and non-compact (p,q ≥ 1) and G is simple with Γ a lattice, so by Moore's ergodicity theorem H acts
ergodically on G/Γ. A continuous H-invariant function is then a.e. constant, hence constant (Haar has full support). ∎

**Consequence.** For indefinite Weil-form Grams (windows T > T_*, or K^H on non-primitive spans), integrality of A is
invisible to every continuous invariant: only (sig, det) remain, and these are real-congruence invariants (4.1), so
the same for DH with A real. Integrality can matter only through **discontinuous** invariants (e.g. exact
representation numbers of values), which are then subject to L5/Theorem M: the defect to be seen is
≤ exp(−exp((2−ε)T)) in relative size (R162_801 L5), and any discontinuous invariant at that scale is a statement about
exact coincidences of real numbers c_F(log m), which the first-contact equations do not produce.

**Prop 4.3 (definite case).** At the first contact the relevant Gram K = [⟨e_m,e_n⟩] is positive semidefinite; its
GL_N(ℤ)-invariants (successive minima, Voronoi cell of the lattice L_F = ℤ-span{e_n}) exist and are continuous, but
they depend on F only, not on the weights a. The weights enter the first-contact problem only through the linear
functional G ↦ Σ_n a(n)(K_{1n}+K_{n1}) (B1(d)). **Failing line:** for the deletion model Λ1_{n≥5} (first contacts at
T_W ≤ 0.4608, R162_703) and κ-models (R162_702 Thm 2), L_F, Z, Z^{-1} and every lattice invariant are literally the same
functions of F as for ζ; the model differs only in that linear functional, i.e. in L2 of R162_801.

## 5. Nonlinear in F reduces to quadratic in a tensor model (PROVED)

**Theorem 5.1 (tensor lift).** Let Φ be a polynomial functional of F of degree 2d built from 𝒜_T, X̂, the
archimedean operator A^∞, polar/Tate functionals and floor data. Then Φ(F) = ⟨F^{⊗d}, 𝐇 F^{⊗d}⟩ for an operator 𝐇 in
the algebra generated by 𝒜_T^{⊗d} = M_T^{(d)}(arith. functions on ℕ^d) (the compressed multiplicative semigroup on
I_T^d, B1(a) holding coordinatewise), X̂_i and A^∞_i. At a first contact, F^{⊗d} ∈ ker 𝐇_{T_*} with
𝐇_T = Σ_i I⊗…⊗H_T⊗…⊗I ≥ 0, whose weights are Σ_i 1⊗…⊗Λ⊗…⊗1, and ker 𝐇_{T_*} = N^{⊗d}.
The analogues of Thm 3.2 (log Z^{⊗} = Σ_i log Z_i), 4.1, 4.2, 4.3 hold for 𝐇.
*Proof.* Polarization writes Φ as a d-linear form in F⊗F; tensor products of compressed shifts compose coordinatewise.
H_T ≥ 0 on P_T at T_* gives 𝐇 ≥ 0 on P_T^{⊗d} with kernel N^{⊗d}. The algebraic statements are coordinatewise. ∎

**Reading.** Any exact nonlinear use of the ground state/first-contact vector is a quadratic use at a tensor first
contact, whose arithmetic is the diagonal Dirichlet ring on ℕ^d, again weight-linear. Symmetric mixed tensors
ψ_T ⊗ F are included (ψ_T ⊗ F is not in the kernel; its pairing with 𝐇 is λ_0(T)⟨…⟩, a spectral statement on
ψ_T, weight-blind by R162_702). The tensor model has first contacts exactly when the base model has; so F3 models pass
through the lift unchanged. F1: an eigenvector with λ>0 lifts to one with eigenvalue dλ, same identities.

## 6. Perron positivity and |μ| ≤ 1 (PROVED; weight-blind)

**Prop 6.1.** Since Z is positivity-preserving and ψ_T > 0: |M_T(β)G| ≤ M_T(|β|)|G| pointwise for all β, G; in
particular |Z^{-1}F| ≤ Z|F|, |Z^{-1}ψ_T| ≤ Zψ_T, and ⟨|F|, M_T(Λ)|F|⟩ ≥ |⟨F, M_T(Λ)F⟩|.
*Proof.* Triangle inequality in the kernel representation; |μ| ≤ 1; Λ ≥ 0. ∎
These are the only nonlinear (non-polynomial) relations the candidate supplies. **Failing lines:** Beurling
(Z_B ≥ 0, |μ_B| ≤ 1, Λ_B ≥ 0, Λ_B*1 = log, off-line zeros) satisfies all three; Λχ₂ satisfies the first two with
Z_{χ₂} dominated by Z. F is sign-changing (ε = −1 sector), so the Kato-type inequality replaces F by |F|, which is not
in P_T and not in N; this is input (iii) of R162_502 B3.

## 7. Falsifier table

| model | Thm 3.2 | Thm 4.1 (A ∈ ℤ, unipotent) | Prop 6.1 | declared failing line | has first contacts |
|---|---|---|---|---|---|
| DH | holds with Λ_DH | A real, not integral | fails (a^{-1} large) | "Z has coefficients 1" | yes |
| deletion Λ1_{n≥5} | Z unchanged | identical to ζ | holds | "Weil weight = log-coeff. of Z" at n=2,3,4 (linear) | yes, T_W ≤ 0.4608 |
| κ-models | Z unchanged | identical to ζ | holds | same, linear | yes (R162_702) |
| Λχ₂ (ζ arch. data) | holds for Z_χ | A ∈ {0,±1} | holds (|μχ₂| ≤ 1) | none of §§2–6 | yes (B3) |
| Beurling DMV | holds on 𝒩_B | A ∈ {0,1} | holds | only "⌊·⌋ = integer counting", which enters pointwise only (Prop 2.1) | yes (off-line zeros) |

Λχ₂ and Beurling pass every line: any closure from §§2–6 proves a falsehood. Deletion/κ fail only at a linear line.

**F1.** Every statement in §§2–6 is an identity in F or holds for all F; λ = 0 enters only as ⟨F,HF⟩ = 0, linear in
K (or in 𝐇 after the lift). On λ > 0 eigenvectors the same identities hold. F1 not passed.
**F2.** All Gram/minor/inertia data are even in F and quadratic in c_F; the determinant/rank data of 4.1 are
invariants of the (PC)-square class, invariant under A_M → −A_M. F2 not passed.

## 8. Verdict and sharpened residual

NO-GO (PROVED). The integer-structured Gram mechanism fails at (a) (Prop 2.1: floors integrate to hyperbola/sawtooth),
(b) (Thm 4.1: rank/det of 𝔊 are those of K_F), (c) (Thm 4.2: continuous integrality invariants collapse; Prop 4.3:
definite-case lattice invariants are weight-independent; Prop 6.1: |μ| ≤ 1 + ψ > 0 is Beurling/Λχ₂-valid). Raising the
degree in F does not help (Thm 5.1), and raising the degree in Λ does not help (Thm 3.2).

Sharpened residual (replaces R162_801's): an exact step must use a **discontinuous** functional of F that distinguishes
integer from generalized-integer support (to kill Beurling) and 1 from χ₂ (to kill Λχ₂), and it must not be invariant
under unipotent integral congruence. By 4.1–4.2 and 5.1 no functional built from 𝒜_T, Gram data, floors, positivity and
tensor powers has these properties. Add to R162_590 §1c:
"nonlinear Möbius Gram / lattice / tensor lift — R162_903 — BCH terminates (Thm 3.2), Sylvester/Moore collapse
(4.1–4.2), tensor lift (5.1); Λχ₂ and Beurling pass every line — F1, F2, Φ".

Labels: Prop 2.1, Lemma 3.1, Thm 3.2, Thm 4.1, Thm 4.2, Prop 4.3, Thm 5.1, Prop 6.1 PROVED. Route: NO-GO.
