# Round 005 A — The comb-first Krylov family: structure, exact reduction, and the sign lemma on K_j

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Object specification: OBJECT_SPEC_001 (R1–R5). This memo
builds the comb-generated family of OBJECT_SPEC_001 and proves what can be proved about it. Labels:
PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. No equivalence of (★) with any other
statement is used.

## 0. Notation

I = I_T = (−T, T). On L²(ℝ): Q = multiplication by 1_I, R = 1 − Q; L²(I) is identified with QL²(ℝ). V_a is
the shift (V_aF)(t) = F(t − a), with F̂(τ) = ∫F e^{iτt}, so V_a is the Fourier multiplier e^{iaτ}. For x ∈ ℝ,
c_x := ½(V_x + V_{−x}) (multiplier cos(xτ)), and the **truncated shift** S_x := Q c_x Q on L²(I); S_x = S_{−x}
= S_x*, S_0 = Q, S_x = 0 for |x| ≥ 2T. Contacts N_T = {n ≥ 2 : log n < 2T}, x_n = log n, v_n = 2Λ(n)/√n,
𝒜 = Σ v_n. The **comb symbol** σ_v(τ) = Σ_{n∈N_T} v_n cos(τ x_n) is the multiplier σ_v = Σ v_n c_{x_n} on
L²(ℝ), and the **prime operator** is

    Π := Q σ_v Q = Σ_{n∈N_T} v_n S_{x_n}     on L²(I),     ⟨F, ΠF⟩ = Σ v_n Re c_F(log n)

(Paper 47 prop:shifts, CITED; the sign convention is that of ROUND_003_A: a_T = Arch − Π). 𝔪 is the
multiplier by m(τ) on L²(ℝ); Arch(F) = ⟨F, 𝔪F⟩ on the form domain 𝒟_T = {F ∈ L²(I): ∫log(2+|τ|)|F̂|² < ∞}.
Lévy form (CITED, Paper 47 lem:K, thm:A): Arch(F) = C_0‖F‖² + ¼∫∫_{ℝ²}|F(t) − F(s)|² K(|t−s|) dt ds, K(u) =
2Σ_{j≥0}e^{−(2j+½)u}, and 𝒟_T is exactly the set of F ∈ L²(I) with finite double integral (m − C_0 ≍
log(2+|τ|), Paper 47 lem:mbounds). χ_± = e^{±t/2}1_I, Γ = orthogonal projection of L²(I) onto span{χ_+, χ_−},
P = 1 − Γ (projection onto P_T). M is the self-adjoint operator of the closed form Arch|_{P_T ∩ 𝒟_T} (compact
resolvent, Paper 47 prop:nodes, CITED), Π_P := PΠP|_{P_T} (bounded, ‖Π_P‖ ≤ 𝒜), A := M − Π_P the operator of
a_T on P_T. Parity: J F(t) = F(−t) commutes with Q, c_x, 𝔪, Γ, hence with Π, Π_P, M, A (ROUND_003_A Prop. 1).

## 1. Corpus check

- Routes-tried index, grid and crossword searched for "Krylov", "prime operator", "truncated shift",
  "comb-generated", "iterated comb", "powers of the comb", "Π²", "Widom". Hits: (i) G8D-R164_502c, tool L5
  "Stieltjes on moments = positivity on Krylov space; only m₁ carries sign" and L6 "Widom identity
  A_T² = Pσ²P − PσQσP": both concern the Krylov space and the square of the **symbol operator** of a_T itself
  (generator A, or σ_T), for which Krylov positivity is tautologically the spectral measure of the cyclic vector
  — a restatement. Here the generator is the **comb operator Π_P**, not A, and the family is seeded on the
  archimedean negative cone; the Widom-type identity is used below for Π (its square), as a computation, not as a
  route. (ii) ROUND_004_A Prop. B (Λ-free finite planes, NO-GO) — the present family is Λ-dependent from j = 2 on;
  its behaviour under cΛ is analysed in §3.4 and is different from Prop. B in one respect (the subspace is
  scale-invariant) and identical in another (pencil). (iii) Paper 47 lem:archcount / lem:combsine / thm:arena
  (CITED as inputs). (iv) N_018 (identities + Bochner/Cauchy–Schwarz are comb-generic): every sign-definite piece
  found at degree 2 below is of this type and is labelled as such; no claim of a sign is made from it.
- Nothing in the index builds the Krylov family of Π_P from the archimedean negative subspace, writes the window
  form on it, or isolates its degree-3 near-coincidence content. No route is retried.

## 2. The object

### 2.1 The archimedean negative cone (two versions, both Λ-free)

(N1) **Spectral.** 𝒩_T := negative spectral subspace of M on P_T, n_T := dim 𝒩_T = n_−(M) < ∞ (compact
resolvent, semibounded). M-invariant by construction. Parity-split: 𝒩_T = 𝒩_T^ev ⊕ 𝒩_T^odd.

(N2) **Explicit (Dirichlet sines).** With e_k(t) = T^{−1/2} sin(πk(t+T)/2T) and t_1 = 3 (m(3) = −0.7442 < 0,
NUMERICAL evaluation of a proved inequality's hypothesis; any t_1 with m(t_1) ≤ 0 serves), N_T := ⌈2Tt_1/π⌉ − 1,
Σ_T := span{e_k : k ≤ N_T} ∩ P_T, dim Σ_T ≥ N_T − 2.

Lemma 2.1 (PROVED; Paper 47 lem:archcount restricted to P_T). Arch ≤ −B(t_1² − (πN_T/2T)²)‖F‖² on Σ_T with
B = φ′(t_1²) > 0, hence Σ_T ⊂ (a negative subspace of M) and n_T ≥ dim Σ_T ≥ ⌈2Tt_1/π⌉ − 3.
Proof. m(τ) = C_0 + φ(τ²) with φ concave (Paper 47 thm:S), so m(τ) ≤ m(t_1) + B(τ² − t_1²) ≤ B(τ² − t_1²).
Integrate against |F̂|² and use (1/2π)∫τ²|F̂|² = ‖F′‖² ≤ (πN_T/2T)²‖F‖² on the sine span; the two Tate conditions
cut codimension ≤ 2. Min–max gives n_−(M) ≥ dim Σ_T. ∎
Remark. At the windows used for validation (T ≤ 1.2) the explicit count gives nothing (N_T − 2 ≤ 0) while the
Galerkin negative count of M on P_T^ev is 1 (T = log 2, ½log5, 0.9, 1.0) and 2 (T = 1.2), with 0 on P_T^odd up
to T = 1.0 (NUMERICAL, §6). The spectral version (N1) is therefore the one with content at small T; (N2) is the
certified large-T floor, n_T ≳ 6T/π (or ≈ 4T with t_0 = 6.2898…, Paper 47).

### 2.2 The Krylov family

K_j(T) := span{ Π_P^i e : e ∈ 𝒩_T, 0 ≤ i < j } ⊂ P_T,   j ≥ 1;   K_1 = 𝒩_T,   Π_P K_j ⊂ K_{j+1},   dim K_j ≤ j·n_T.

The generating vectors are the **monomials** P(ΠP)^i e = Σ_{n_1,…,n_i} v_{n_1}⋯v_{n_i} P S_{x_{n_1}} P S_{x_{n_2}} ⋯ P S_{x_{n_i}} P e,
homogeneous of degree i in the weight vector v = (v_n)_{n∈N_T} with Λ-free vector coefficients (they depend on T
and on the positions log ℕ only).

Lemma 2.2 (form-domain invariance; PROVED). Let 𝔅 := 𝒟_T ∩ L^∞(I) ∩ P_T. Then S_x𝔅 ⊂ 𝒟_T ∩ L^∞ and Π_P𝔅 ⊂ 𝔅.
Proof. V_x preserves the Lévy double integral and L^∞. For F ∈ 𝒟_T ∩ L^∞ and an interval E,
|1_E(t)F(t) − 1_E(s)F(s)|² ≤ 2|F(t) − F(s)|² + 2|F(s)|²|1_E(t) − 1_E(s)|²; integrating against K(|t−s|), the
first term gives ≤ 2·(finite), the second ≤ 2‖F‖²_∞ ∫_{supp F} w_E(s) ds with w_E(s) = ∫_{1_E(t)≠1_E(s)} K(|t−s|) dt
≤ C(1 + log⁺(1/dist(s,∂E))), which is integrable over the bounded set supp F. So Q V_{±x} Q F ∈ 𝒟_T ∩ L^∞. P
subtracts multiples of χ_±, which are bounded and of bounded variation, hence in 𝒟_T. ∎
Consequence. If 𝒩_T ⊂ L^∞ (true for (N2); for (N1) it is the statement that the negative eigenfunctions of M
are bounded — CONDITIONAL, hypothesis (H_b) below; it is not needed for any of the finite identities, only for
placing K_j inside the form domain) then K_j ⊂ 𝔅 ⊂ 𝒟_T ∩ P_T for every j, and all form values a_T(x, y), x, y ∈ K_j,
are finite. For the explicit cone (N2) everything below is unconditional.

### 2.3 Polar corrections

Π_P^i e = PΠ^i e + (terms containing Γ). Since Γ has rank 2, the correction lies in 𝒳_j := Σ_{0≤i'<j−1} PΠ^{i'}
span{χ_+, χ_−}, dim 𝒳_j ≤ 2(j − 1). Hence K_j ⊂ P span{Π^i e} + 𝒳_j: the family built with the uncompressed Π and
projected afterwards differs from K_j by a Λ-dependent space of dimension ≤ 2(j−1) spanned by the comb orbits of
the two Tate exponentials. (PROVED; bookkeeping.) The monomial algebra of §3 is written for Π; for Π_P each word
P S P S ⋯ P expands into the Π-words plus words with Γ inserted, each of which is a rank-≤2 operator of the form
|PΠ^{a}χ_±⟩⟨Π^{b}χ_±|-type; the identities below are stated for Π and hold for Π_P with these rank-≤2 terms added.
They are not numerically small: on the negative even mode, ‖ΓΠe‖²/‖Πe‖² = 0.48, 0.23, 0.29, 0.19, 0.16 at
T = log 2, ½log5, 0.9, 1.0, 1.2 (NUMERICAL, §6.4) — the comb response of the negative mode has a large component
along cosh(t/2)1_I, which P removes. Every statement about the form a_T on K_j is made with Π_P.

## 3. Structure of the matrix of a_T on K_j

### 3.1 Degrees (PROVED)

Proposition 3.1. In the monomial generating system {Π_P^i e_α : α ≤ n_T, i < j} of K_j, with (e_α) an orthonormal
basis of 𝒩_T,
  (i) Gram entries ⟨Π_P^i e_α, Π_P^{i'} e_β⟩ = ⟨e_α, Π_P^{i+i'} e_β⟩ are homogeneous of degree i + i' in v;
  (ii) comb entries ⟨Π_P^i e_α, Π_P Π_P^{i'} e_β⟩ = ⟨e_α, Π_P^{i+i'+1} e_β⟩ are homogeneous of degree i + i' + 1
       ≤ 2j − 1, with Λ-free coefficients ⟨e_α, PS_{x_{n_1}}P ⋯ PS_{x_{n_{i+i'+1}}}P e_β⟩ (window overlaps of e_β
       dilated along a word of contacts, cut at every intermediate step, with e_α);
  (iii) archimedean entries Arch(Π_P^i e_α, Π_P^{i'} e_β) are homogeneous of degree i + i' ≤ 2j − 2, with Λ-free
       coefficients Arch(PS_w P e_α, PS_{w'} P e_β), words w, w'. By the Lévy form each such coefficient is
       C_0⟨S_w e_α, S_{w'} e_β⟩ + ∫_0^∞ K(u)[⟨S_w e_α, S_{w'}e_β⟩ − Re⟨S_w e_α, V_u S_{w'} e_β⟩] du, and
       ⟨S_w e_α, V_u S_{w'} e_β⟩ is a finite sum of overlaps ∫ e_α(t − a) e_β(t − a − u − b) 1_{polygon}(t) dt with
       a, b signed sums of logarithms of contacts: the archimedean kernel K is integrated against the overlap of
       the two words at total shift u + (a − b), a − b ∈ log ℚ_{>0} running over the products and quotients of
       contacts generated by the words.
Hence every entry of the matrix of a_T on K_j is a polynomial of degree ≤ 2j − 1 in v (degree ≤ 2j − 2 for the
archimedean part, exactly 2j − 1 for the top comb term), with coefficients that are archimedean kernels evaluated
at sums and differences of logarithms of contacts. (Polar corrections of §2.3 have the same degrees.)
Proof. Expand Π = Σ v_n S_{x_n} in each slot; self-adjointness of Π_P moves all comb factors to one side; the
Lévy form gives (iii); (S_w e)(t) is a sum over sign patterns of e(t − a)1_{polygon}(t) because (QV_aQ ⋯ QV_bQ F)(t)
= F(t − a − ⋯ − b)·Π(indicators of t minus the partial sums ∈ I). ∎

### 3.2 The word algebra: where (ℕ,·) enters (PROVED)

Lemma 3.2 (same-direction cuts are void; opposite-direction cuts are edge slabs). For a, b > 0:
  (i)  Q V_a Q V_b Q = Q V_{a+b} Q = 2S_{a+b}-part, i.e. the intermediate window is automatic;
  (ii) Q V_a Q V_{−b} Q = Q V_{a−b} Q − 𝒯_{a,b}, where (𝒯_{a,b}F)(t) = 1_{(a−b−T, a−T]}(t) F(t − (a − b)): the slab
       (−T, −T+b) of F, carried to position (a−b−T, a−T] — equivalently 𝒯_{a,b} = Q V_a R V_{−b} Q is the part of the
       left-shifted F that leaves the window and is brought back by the right shift;
  (iii) more generally, for any word, every maximal run of shifts in the same direction collapses to one truncated
       shift by the sum, and each change of direction inserts one factor R (a leak) or nothing.
Proof. (QV_aQV_bQF)(t) = 1_I(t)1_I(t−a)1_I(t−a−b)F(t−a−b); for a, b > 0 the point t − a lies between t and t − a − b,
both in I, so 1_I(t − a) = 1. For (ii), 1_I(t)1_I(t−a+b)[1 − 1_I(t−a)] = 1_I(t)1_I(t−a+b)1_{t ≤ a−T}, and
t − a + b > −T forces t > a − b − T. (iii): write Q = 1 − R between consecutive factors and use (i). ∎
NUMERICAL validation (T = 1, Dirichlet sines e_1, e_3, Gauss–Legendre 4000 nodes): (i), (ii) (both orders), the
three-step collapse Q V_{log2} Q V_{log3} Q V_{−log5} Q = Q V_{log6} Q V_{−log5} Q, and the Widom split of Prop. 3.3
below hold to 10^{−16}.

Proposition 3.3 (the square of the comb; PROVED). On L²(I), with the leak operator 𝔏 := R σ_v Q : L²(I) → L²(ℝ∖I),

    Π² = Q σ_v² Q − 𝔏*𝔏,
    Q σ_v² Q = ½ Σ_{N<e^{2T}} (v∗v)(N) S_{log N} + ½ Σ_{m,n∈N_T} v_m v_n S_{log(m/n)},   (v∗v)(N) = Σ_{mn=N} v_m v_n = 4(Λ∗Λ)(N)/√N,
    ‖𝔏F‖² = ¼ ∫_T^{T+x_max} |Σ_{n: x_n > t−T} v_n F(t − x_n)|² dt + ¼ ∫_{−T−x_max}^{−T} |Σ_{n: x_n > −T−t} v_n F(t + x_n)|² dt.

Consequently, for every F ∈ L²(I),

    ⟨F, Π²F⟩ = ½ Σ_{N<e^{2T}} (4(Λ∗Λ)(N)/√N) Re c_F(log N)  +  ½·(1/2π)∫|F̂(τ)|² |Σ_{n∈N_T} v_n n^{iτ}|² dτ  −  ‖𝔏F‖².
                 [product comb: Dirichlet convolution Λ∗Λ, indefinite]   [Dirichlet-polynomial mean value: ≥ 0]   [leak: ≤ 0]

Proof. Π² = Qσ_vQσ_vQ = Qσ_v(1 − R)σ_vQ and R² = R, σ_v* = σ_v. σ_v² = Σ v_mv_n cos(τx_m)cos(τx_n) =
½Σ v_mv_n[cos τ(x_m + x_n) + cos τ(x_m − x_n)], and Q cos(aτ) Q = S_a with S_a = 0 for |a| ≥ 2T, which removes all
products N = mn ≥ e^{2T}. Σ_{m,n} v_mv_n cos(τ(x_m − x_n)) = |Σ v_n e^{iτx_n}|². The leak formula is the
definition read on the two sides of the window (disjoint supports). ∎

Reading. (ℕ,·) enters the degree-2 entries exactly through (a) the Dirichlet convolution Λ∗Λ at the products N = mn
that still lie in the window, (b) the quotients m/n (a Toeplitz form in the comb, positive by Bochner), and (c) the
leaks, which are comb-weighted samples Σ v_n F(t − log n) of F at multiplicative distances from a point t just
outside the window. Λ∗Λ = Λ_2 − Λ·log (Selberg's identity, Λ_2 = μ∗log²) is the only arithmetic function of the
degree-2 term; it is the same for every Beurling system (products of generalized integers are generalized integers).
**No near-coincidence appears at degree 2**: all shifts are exact logarithms of products or quotients.

Proposition 3.4 (degree 3: the near-coincidences; PROVED). Π³ = Qσ_v³Q − Qσ_vRσ_v²Q − Qσ_v²Rσ_vQ + Qσ_vRσ_vRσ_vQ and

    Q σ_v³ Q = ¼ Σ_N (v∗v∗v)(N) S_{log N} + ¾ Σ_{r∈ℚ_{>0}} W_3(r) S_{log r},   W_3(r) := Σ_{m,n,k∈N_T: mn/k = r} v_m v_n v_k ≥ 0.

The ratio class r = 1 is the exact coincidences k = mn (prime-power towers only, since Λ(k) ≠ 0); the classes
r = mn/k with 0 < |log r| ≪ 1 (k = mn ± 1, …) are the near-coincidences, and for them S_{log r} is close to the
identity on low-frequency vectors: ⟨F, S_{log r}F⟩ = Re c_F(log r) = ‖F‖² − ½‖F − V_{log r}F‖² + (edge terms).
These are the first entries of the family in which the additive structure of ℕ (mn − k = ±1, ±2, …) appears,
with weight W_3(r) ≥ 0. Since Π_ff below enters a_T with a **minus** sign, near-coincidences strengthen the comb's
third moment on the responses and work **against** the sign on K_2 (PROVED as a statement about the sign of the
contribution; its size is not estimated here).
Proof. Expand cos³ by the product formula: cos a cos b cos c = ¼[cos(a+b+c) + cos(a+b−c) + cos(a−b+c) + cos(−a+b+c)];
symmetrise the three mixed terms. ∎

### 3.3 Scaling cΛ (PROVED)

Proposition 3.5. (i) In the monomial system of Prop. 3.1 every entry scales as c^{deg} under v ↦ cv: Gram and
archimedean entries of degree i + i', comb entries of degree i + i' + 1. (ii) As a **set**, K_j(T; cΛ) = K_j(T; Λ)
for every c ≠ 0 (a Krylov space is invariant under scaling its generator). (iii) Hence the condition
"a_T^{cΛ} ⪰ 0 on K_j(cΛ)" is the pencil condition M − cΠ_P ⪰ 0 on the fixed subspace K_j(Λ): if a_T ⪰ ε > 0 on
K_j(Λ) then a_T^{cΛ} ⪰ 0 on K_j(cΛ) for |c − 1| ≤ ε/‖Π_P|_{K_j}‖; and the function c ↦ λ_min(M − cΠ_P|_{K_j}) is
concave.
Proof. (i) is Prop. 3.1. (ii) span{(cΠ_P)^i e} = span{Π_P^i e}. (iii) is Weyl's inequality on the fixed subspace;
concavity: minimum of affine functions. ∎
Reading. Scale-sensitivity is **not** in the subspace but in the pencil, exactly as for the whole of P_T (c ↦
λ_A(T; cΛ) is concave, Paper 47 lem:degen, CITED). The family does not escape ROUND_004_A Prop. B for the falsifier
cΛ at a fixed window — nothing can, since λ_A(T; ·) is continuous in c at fixed T; the cΛ test is a test on the
family over all T (§7).

### 3.4 Deletions, finite modifications, Beurling systems (PROVED, structural)

(a) a_P (contacts below P deleted) and finite modifications w = v + δ change the generator: Π_P^{(w)} = Π_P + Π_{P,δ}
with Π_{P,δ} = P(Σ δ_n S_{x_n})P bounded by Σ|δ_n|. Then K_j(w) ≠ K_j(v) in general from j = 2 on: K_2(w) = 𝒩_T +
(Π_P + Π_{P,δ})𝒩_T. Unlike the cΛ case the subspace moves; the matrix of a_T^{w} on K_j(w) is obtained from that on
K_j(v) by the polynomial substitution v ↦ v + δ in every entry (Prop. 3.1) **and** a change of basis. The
sign-lemma conditions (§5) for v and for w are therefore different polynomial inequalities, not the same
inequality at a translated point.
(b) For a Beurling system (generalized primes p_i, generalized integers 𝒩 = the multiplicative semigroup, contacts
{log ν : ν ∈ 𝒩, log ν < 2T}, weights 2Λ_𝒩(ν)/√ν) every identity of §3.1–3.3 holds verbatim with Λ∗Λ replaced by
Λ_𝒩∗Λ_𝒩 (the semigroup is multiplicatively closed, so products of contacts are contacts); the degree-2 structure
is Beurling-generic. The degree-3 near-coincidence classes W_3(r), r ≈ 1, are the first place where the system's
additive structure (which rationals mn/k are close to 1, and how close) enters: for ℕ, |log(mn/k)| ≥ 1/(mn+1)
whenever mn ≠ k with the lattice of consecutive integers; for a generic Beurling system there is no such lattice.
(c) None of (a)–(b) is a sign statement. They locate where each falsifier acts on the object: cΛ through the
pencil only; a_P and δ through the subspace and the coefficients; Beurling through degree ≥ 3 only.

## 4. The exact reduction and the Schur coupling

### 4.1 Form-level Schur complement (PROVED)

Theorem 4.1. Let K ⊂ P_T ∩ 𝒟_T be finite-dimensional, K^⊥ its orthogonal complement in P_T, A_K the matrix of a_T on
K, and for y ∈ K^⊥ ∩ 𝒟_T let b_y ∈ K be the Riesz vector of x ↦ a_T(x, y) on K (finite-dimensional, always
defined). Then a_T ⪰ 0 on P_T ∩ 𝒟_T if and only if
  (i) A_K ⪰ 0, and
  (ii) for every y ∈ K^⊥ ∩ 𝒟_T: b_y ∈ range(A_K) and a_T(y) ≥ ⟨A_K^+ b_y, b_y⟩ (A_K^+ the pseudo-inverse); when
       A_K ≻ 0 this is the Schur form 𝔰_K(y) := a_T(y) − ⟨A_K^{−1} b_y, b_y⟩ ≥ 0 on K^⊥ ∩ 𝒟_T.
Proof. Every z ∈ P_T ∩ 𝒟_T is z = x + y with x ∈ K, y = z − P_K z ∈ K^⊥ ∩ 𝒟_T (K ⊂ 𝒟_T). a_T(x + y) = ⟨A_Kx, x⟩ +
2Re⟨b_y, x⟩ + a_T(y). For fixed y the infimum over x ∈ K is −∞ unless A_K ⪰ 0 and b_y ∈ range A_K, in which case it
is a_T(y) − ⟨A_K^+b_y, b_y⟩, attained at x = −A_K^+ b_y. ∎
No regularity beyond K ⊂ 𝒟_T is used: the coupling is a functional on the form domain, not a bounded operator.

### 4.2 The Krylov coupling algebra (PROVED)

Proposition 4.2 (K_1 = 𝒩_T, spectral version (N1) under (H_b), or the finite-dimensional Galerkin model). Let (e_α) be an
orthonormal eigenbasis of 𝒩_T, M e_α = α_α e_α, D = diag(α_α) ≺ 0, Π_ee = (⟨e_α, Π_P e_β⟩) and
f_α := P_{K_1^⊥} Π_P e_α = Π_P e_α − Σ_γ (Π_ee)_{γα} e_γ   (the comb responses of the negative modes).
  (i) A K_1 ⊂ K_2 = K_1 ⊕ span{f_α}: for the seed 𝒩_T the Krylov spaces of A = M − Π_P and of Π_P coincide at j = 2
      (M K_1 = K_1), and differ from j = 3 on by the commutator terms [M, Π_P] K_1 (see (v)).
  (ii) The coupling of K_1 to K_1^⊥ is carried by the comb alone: for y ∈ K_1^⊥ ∩ 𝒟_T, a_T(e_α, y) = −⟨f_α, y⟩, i.e.
      b_y = −Σ_α ⟨f_α, y⟩ e_α. (The archimedean part contributes nothing because M e_α = α_α e_α ⊥ y.)
  (iii) The Gram matrix of the responses is the variance of the comb on 𝒩_T:
      G := (⟨f_α, f_β⟩) = (Π_P²)_ee − Π_ee² ⪰ 0,  where (Π_P²)_ee = (⟨e_α, Π_P² e_β⟩) (degree 2 in v).
  (iv) The matrix of a_T on K_2 in the system (e_α; f_α) is
          [ D − Π_ee        −G                                    ]
          [ −G              (Π_P M Π_P)_ee − Π_ee D Π_ee − Π_ff    ],
      Π_ff := (⟨f_α, Π_P f_β⟩) = (Π_P³)_ee − Π_ee(Π_P²)_ee − (Π_P²)_ee Π_ee + Π_ee³   (degree 3),
      (Π_P M Π_P)_ee = (Arch(Π_P e_α, Π_P e_β))   (degree 2, archimedean coefficients).
      Degrees: block (1,1) ≤ 1, (1,2) = 2, (2,2) ≤ 3 = 2j − 1.
  (v) Commutator. On L²(I), with M_0 = Q𝔪Q and c_x = ½(V_x + V_{−x}): [M_0, S_x] = Q c_x R 𝔪 Q − Q 𝔪 R c_x Q. For
      F ∈ L²(I), (R𝔪QF)(t) = −∫_I K(|t − s|)F(s) ds for t ∉ I (the archimedean halo of F outside the window; C_0 does
      not contribute there), so the first term is the halo shifted back into the window by ±x and the second is the
      leak of F under the shift, read back through K. Hence [M, Π_P] 𝒩_T is spanned by Λ-weighted sums of these two
      halo/leak operators applied to the negative modes, plus rank-≤2 polar terms from Γ.
Proof. (i) A e_α = α_α e_α − Π_P e_α ∈ K_1 + Π_P K_1. (ii) a_T(e_α, y) = ⟨M e_α, y⟩ − ⟨Π_P e_α, y⟩ = 0 − ⟨f_α + P_{K_1}Π_P e_α, y⟩
= −⟨f_α, y⟩. (iii) ⟨f_α, f_β⟩ = ⟨Π_Pe_α, Π_Pe_β⟩ − Σ_γ(Π_ee)_{γα}(Π_ee)_{γβ}. (iv) a_T(e_α, f_β) = −⟨f_α, f_β⟩ by (ii);
a_T(f_α, f_β) = ⟨f_α, M f_β⟩ − ⟨f_α, Π_P f_β⟩, and ⟨f_α, M f_β⟩ = ⟨Π_Pe_α, MΠ_Pe_β⟩ − Σ_γ (Π_ee)_{αγ}α_γ(Π_ee)_{γβ} after
expanding f and using M e_γ = α_γ e_γ; the Π_ff expansion is the same bookkeeping. (v) M_0S_x − S_xM_0 =
Q𝔪Qc_xQ − Qc_xQ𝔪Q; insert Q = 1 − R in the middle of each term and use [𝔪, c_x] = 0 on L²(ℝ). ∎

Corollary 4.3 (exact reduction at j = 1; PROVED). Under (★) at T, or a priori: a_T ⪰ 0 on P_T ∩ 𝒟_T if and only if
  (SL_1)  D − Π_ee ⪰ 0 (with the range condition of Thm 4.1 if singular; ≻ 0 generically), and
  (SC_1)  a_T(y) ≥ Σ_{α,β} ⟨y, f_α⟩ ((D − Π_ee)^{−1})_{αβ} ⟨f_β, y⟩   for all y ∈ K_1^⊥ ∩ 𝒟_T.
The penalty on the right is a finite-rank form (rank ≤ n_T) supported on the span of the comb responses f_α, of
norm ≤ λ_max(G)/λ_min(D − Π_ee). Restricting (SC_1) to y ∈ span{f_α} gives exactly "a_T ⪰ 0 on K_2" (the Schur
complement of the block matrix in 4.2(iv)); restricting to y ∈ K_j ⊖ K_1 gives "a_T ⪰ 0 on K_j".
Proof. Theorem 4.1 with K = K_1 and 4.2(ii). ∎

### 4.3 What coercivity on K_j^⊥ would require (assessment)

(a) PROVED bound on the coupling: ‖b_y‖² = Σ_α⟨f_α, y⟩² ≤ λ_max(G)‖y‖² with λ_max(G) ≤ ‖Π_P‖² ≤ 𝒜², and λ_max(G) is
NUMERICALLY of order 10^{−2}–10^{−1} at T ≤ 1.2 (= ‖B‖² in §6). So the Krylov structure gives an explicit, Λ-polynomial
(degree 2) bound on the Schur coupling, with range confined to K_2 ⊖ K_1. This is the "exact algebra" asked for; it is
PROVED and comb-generic.
(b) What (SC_1) demands on K_1^⊥: a_T must dominate a finite-rank penalty of size λ_max(G)/λ_min(D − Π_ee). Under (★),
λ_min(D − Π_ee) ≥ λ_min(a_T|_{K_2}) ≥ λ_A(T), so the penalty can be as large as λ_max(G)/λ_A(T) only if the bottom of
a_T is nearly inside K_1 — which it is not (§6: the principal cosine between K_1 and the ground state is 0.56–0.79 at
T ≤ 1.0). NUMERICALLY λ_min(D − Π_ee) ≈ 2–5·10^{−2} and λ_max(G) ≈ 1–8·10^{−2}, so the penalty has norm of order 1 on
the responses: on K_1^⊥, (SC_1) asks a_T to beat a rank-n_T form of order one supported on explicit Λ-dependent vectors.
(c) No Λ-free coercivity exists on K_1^⊥: M ⪰ 0 there but its bottom α_+ is small (α_+ = 0.10–0.47 at the tested windows,
and ≤ log k + O(1) along the even tower, Paper 47 thm:arena, CITED) while ‖Π_P|_{K_1^⊥}‖ is of order 𝒜 ≍ e^T. So "Arch
dominates the comb on the complement" fails for every j with dim K_j fixed, by the arena count (ARGUED as the
quantitative reading, as in ROUND_004_A §5(b)). Coercivity on K_j^⊥ is therefore not a tool that the family supplies; it
is the statement (★) on the complement with a finite-rank handicap. The reduction is exact and the handicap is explicit,
but the complement carries the whole sign problem.
(d) Krylov structure for j ≥ 2: P_{K_j^⊥} Π_P P_{K_j} has range in K_{j+1} ⊖ K_j (PROVED, Π_P K_j ⊂ K_{j+1}), while
P_{K_j^⊥} M P_{K_j} ≠ 0 from j = 2 on and is given by the halo/leak commutators of 4.2(v) (not confined to K_{j+1}). So
the coupling of K_j to its complement is the comb step (finite rank, next block) plus an archimedean leak term with
explicit kernel K; both are PROVED formulas, neither is small.

## 5. The sign lemma on K_j

### 5.1 j = 1 (the known linear statement)

(SL_1): Σ_{n∈N_T} v_n R_n(𝒩_T) ⪯ D, with R_n(𝒩_T)_{αβ} = ½⟨e_α, (QV_{x_n}Q + QV_{−x_n}Q) e_β⟩ (ROUND_004_A notation).
Linear in v. Content: on the negative archimedean modes the comb must be at least as negative as the archimedean form
(|α_α| ≥ 0.15–0.73 at the tested windows). This is the statement of Paper 47 lem:archcount/lem:combsine written on the
spectral cone instead of the Dirichlet sines (CITED/PROVED), and ROUND_004_A (C_k) with E = 𝒩_T; by ROUND_004_A Prop. B
it cannot be a sign step (Λ-free subspace, positive margin). NUMERICALLY (§6) it holds with margin 1.7–4.9·10^{−2}
at the five windows, fails for deletions of 2 (at every window), for η = −0.1, −0.5, for the Beurling shift at T ≥ ½log5
(even), and for c = 0.9 at T ≥ 0.9; it does not reject c ∈ [0.99, 1.1], η = +0.1, +0.5, the swap, nor the deletion of
3 below T = 0.9.

### 5.2 j = 2 (new: quadratic and cubic in v)

(SL_2): the block matrix of 4.2(iv) is ⪰ 0; with (SL_1) strict, equivalently the Schur complement

    (Π_P M Π_P)_ee − Π_ee D Π_ee − Π_ff − G (D − Π_ee)^{−1} G ⪰ 0,   G = (Π_P²)_ee − Π_ee².

Scalar case n_T = 1 (the windows log 2 ≤ T ≤ 1.0 per sector, NUMERICAL count): with μ_k := ⟨e, Π_P^k e⟩ (k = 1, 2, 3),
m_2 := Arch(Π_P e, Π_P e), the 2×2 matrix of a_T on {e, Π_P e} is

    [ α − μ_1        αμ_1 − μ_2 ]
    [ αμ_1 − μ_2     m_2 − μ_3  ],       (SL_2^{sc}):  α − μ_1 ≥ 0  and  (α − μ_1)(m_2 − μ_3) ≥ (μ_2 − αμ_1)².

Reading: [deficit of the comb below the archimedean level on the negative mode] × [value of a_T on the comb response]
≥ [second comb moment minus α times the first]². The right side is of degree 4 in v, the left of degree ≤ 4; both
sides contain Λ∗Λ (through μ_2 and m_2, Prop. 3.3) and the left contains the near-coincidence classes W_3(r)
(through μ_3, Prop. 3.4). Under (★) it is a necessary condition (PROVED, min–max); NUMERICALLY it holds with
determinant 1.4–5.3·10^{−4} and smaller eigenvalue 1.9–5.8·10^{−3} at all seven (window, sector) pairs with n_T = 1.

### 5.3 The degree-2 structure, exactly, and the inequality the remainder needs

Write the degree-2 quantities on the negative mode e by Prop. 3.3 and its archimedean analogue. With Π_P e = Qσ_v e −
(polar), and 𝔏e the leak, one has exactly (polar terms suppressed in the display; they are the rank-2 corrections of §2.3):

    μ_2 = (1/2π)∫ σ_v² |ê|² − ‖𝔏e‖²,
    m_2 = (1/2π)∫ m σ_v² |ê|² − 2Re⟨𝔏e, 𝔪 σ_v e⟩ + ⟨𝔏e, 𝔪 𝔏e⟩,
    μ_3 = (1/2π)∫ σ_v³ |ê|² − ⟨e, Q σ_v R σ_v² Q e⟩ − ⟨e, Q σ_v² R σ_v Q e⟩ + ⟨e, Qσ_vRσ_vRσ_vQ e⟩,
    α − μ_1 = (1/2π)∫ s_T |ê|²   (exact, e ∈ P_T),    αμ_1 − μ_2 = (1/2π)∫ s_T σ_v |ê|² + ‖𝔏e‖² − ⟨R𝔪e, 𝔏e⟩ ,

where the last term is the pairing of the archimedean halo of e outside the window, (R𝔪e)(t) = −∫_I K(|t−s|)e(s)ds,
with its leak 𝔏e (both supported in ℝ∖I): it comes from αμ_1 = ⟨𝔪e, Πe⟩ = ⟨𝔪e, σ_ve⟩ − ⟨𝔪e, Rσ_ve⟩. Hence, with the
**moment matrix of the signed measure s_T(τ)|ê(τ)|²dτ/2π on polynomials of degree ≤ 1 in the comb symbol**,

    H_2 := [ ∫ s_T|ê|²        ∫ s_T σ_v|ê|²  ]
           [ ∫ s_T σ_v|ê|²    ∫ s_T σ_v²|ê|² ] / 2π ,

the scalar sign lemma reads (SL_2^{sc}) ⟺ H_2 + Δ ⪰ 0, where Δ collects the leak terms:
Δ_{11} = 0, Δ_{12} = ‖𝔏e‖² − ⟨R𝔪e, 𝔏e⟩, Δ_{22} = −2Re⟨𝔏e, 𝔪σ_ve⟩ + ⟨𝔏e, 𝔪𝔏e⟩ + ⟨e, Qσ_vRσ_v²Qe⟩ + ⟨e, Qσ_v²Rσ_vQe⟩ − ⟨e, Qσ_vRσ_vRσ_vQe⟩
(all PROVED identities; each term is an explicit integral of K or of overlaps against the halo/leak of e).

What H_2 ⪰ 0 says. H_2 ⪰ 0 ⟺ ∫ s_T (x + yσ_v)²|ê|² ≥ 0 for all real x, y: the negative set {s_T < 0} of the symbol,
weighted by |ê|², cannot be isolated by an affine function of the comb symbol σ_v. Since (x + yσ_v)² with y ≠ 0
concentrates on the level set {σ_v = −x/y}, this is a conditional statement: **on every level of the comb symbol the
symbol m must, on |ê|²-average, exceed that level**. It is non-linear in Λ (σ_v enters squared), it couples m and
σ_v pointwise in τ, and it is the first condition in the family that is not a bounded functional of the weights. Its
truth is not implied by anything proved: ∫ s_T|ê|² ≥ 0 is (SL_1), and ∫ s_T σ_v²|ê|² can be negative (NUMERICALLY m_2
< 0 at T = 0.9, 1.0 even and 1.2 odd: Arch(Π_Pe) < 0, the comb response is itself an archimedean-negative vector).
The inequality on Λ that the remainder needs: Δ_{22} ≥ ((1/2π)∫s_Tσ_v|ê|² + Δ_{12})²/((1/2π)∫s_T|ê|²) − (1/2π)∫s_Tσ_v²|ê|² — a lower
bound on the leak/halo terms by a polynomial of degree ≤ 4 in v. No mechanism for it is known; the leak terms are not
small (NUMERICAL: at T = 1.0 even, ‖𝔏e‖² is a substantial fraction of ∫σ_v²|ê|²/2π; table in §6.4), so the no-leak
model H_2 is not an approximation of (SL_2) but one of its two exact halves.

Mechanism attempted (products m·n, m/n): the degree-2 content splits exactly into (P) the product comb
½Σ_{N<e^{2T}}(4(Λ∗Λ)(N)/√N)Re c_e(log N), (R) the ratio form ½(1/2π)∫|ê|²|Σv_n n^{iτ}|² ≥ 0, and (L) −‖𝔏e‖² (Prop. 3.3).
(R) is positive by Bochner and (L) negative as a square: both comb-generic (index N_018 class), and both survive every
falsifier (they are identities). (P) carries Λ∗Λ — the only (ℕ,·)-specific content at degree 2 — and is sign-indefinite in general
(c_e(log N) has both signs, as R_n in ROUND_004_A). There is no decomposition of μ_2 or m_2 into "positive Dirichlet
convolution + small remainder": NUMERICALLY (§6.4) (P) is the smallest of the three parts (0 to 0.31, positive at the
tested windows because the only products in the window are 4, 6, 8, 9, 10), while (R) and (L) are each 3–8 times the
total and nearly cancel (0.73 − 0.61 at log 2, 4.03 − 3.62 at 1.2). The degree-2 value is a cancellation between the
Dirichlet-polynomial mean value and the leak, not a Dirichlet-convolution form plus a remainder. The near-coincidence remainder lives at degree 3 (Prop. 3.4), enters (SL_2) only through −μ_3, and with
weight W_3(r) ≥ 0 its exact part at r ≈ 1 makes μ_3 larger, i.e. works against the inequality. The mechanism therefore
does not close: the structure is PROVED, the inequality is OPEN, and the degree-2 positivity available is the trivial one.

## 6. Validation numerics (NUMERICAL; validates points, proves nothing)

Method of ROUND_003_A/004_A: Dirichlet sines, N = 80, Arch by quadrature on |τ| ≤ 6000, Π exact in t-space, sector by
sector, P_T imposed by the sector constraint. 𝒩_T is the span of the Galerkin eigenvectors of Arch with negative
eigenvalue on the sector; K_j is the block Krylov space of the sector-compressed Π_P from 𝒩_T (dim = j·n_T, no
rank loss observed). Galerkin values are upper bounds for the bottoms on the corresponding subspaces of P_T; values
below 10^{−14} are rounding. Windows: log 2, ½log5 ± 10^{−3}, 0.9, 1.0, 1.2.

6.1 Negative counts and the family's bottoms. n_−(Arch|P_T^ev) = 1, 1, 1, 1, 2 and n_−(Arch|P_T^odd) = 0, 0, 1, 1, 1 at
the five windows (odd negative mode appears between ½log5 and 0.9: α_1^odd = +0.0001 at ½log5+10^{−3}, −0.112 at 0.9).

λ_min(a_T|_{K_j}) (even sector; odd in brackets) against λ_A^{par}(T):

| T | j=1 | j=2 | j=3 | j=4 | j=6 | j=8 | j=12 | j=20 | λ_A^{par} (Galerkin) |
|---|---|---|---|---|---|---|---|---|---|
| log 2 | 3.4e−2 | 1.2e−2 | 5.2e−3 | 4.8e−3 | 4.6e−3 | 3.5e−3 | 2.4e−3 | 9.8e−4 | 1.1e−7 |
| ½log5 | 4.7e−2 | 4.1e−3 | 3.7e−3 | 3.3e−3 | 3.1e−3 | 2.4e−3 | 1.7e−3 | 8.0e−4 | 3e−12 |
| 0.9 | 1.7e−2 [4.9e−2] | 6.7e−3 [4.1e−3] | 3.0e−3 [4.1e−3] | 2.9e−3 [4.0e−3] | 2.3e−3 [3.6e−3] | 2.3e−3 [3.6e−3] | 1.9e−3 [3.4e−3] | 1.2e−3 [2.7e−3] | ≲1e−14 |
| 1.0 | 3.0e−2 [1.7e−2] | 3.5e−3 [4.0e−3] | 3.0e−3 [1.7e−3] | 3.0e−3 [1.6e−3] | 2.3e−3 [1.4e−3] | 2.2e−3 [1.3e−3] | 1.7e−3 [1.2e−3] | 1.2e−4 [9.8e−4] | ≲1e−15 |
| 1.2 | 6.1e−5 [1.8e−2] | 1.9e−6 [3.3e−3] | 9.0e−7 [2.7e−3] | 6.5e−7 [2.5e−3] | 4.9e−7 [2.4e−3] | 2.1e−7 [2.2e−3] | 6.9e−8 [2.2e−3] | 1e−14 [5.8e−5] | ≲1e−14 |

Reading. The comb-generated family converges very slowly: at dimension 20 it is still 3–4 orders of magnitude above
the bottom on the sector (except at T = 1.2 even, where it reaches rounding only at j = 20, dim 39 = half the section).
The principal cosine between K_j and the ground state is 0.56–0.79 at j = 1 and rises slowly (0.84–0.97 at j = 20, T ≤ 1).
For comparison the Krylov family of the **same seed under the generator A = M − Π_P** (Lanczos) reaches 1e−7 at
j = 20 for log 2, 2e−7 at ½log5, 8e−8 at 0.9, 5e−7 at 1.0 (dim 20): the two families coincide at j = 2 (Prop. 4.2(i))
and separate from j = 3 on by the halo/leak commutators of 4.2(v); the archimedean steps, not the comb steps, are what
reaches the bottom. The comb-first family therefore does **not** satisfy R3(i) in the tested range: it does not capture
the minimiser to precision λ_A at any dimension that is small compared with the section.

6.2 Coupling and penalty (§4.3). ‖B_Π‖ = ‖P_{K_j^⊥}Π_P P_{K_j}‖ = 0.12–0.31 at j = 1 (so λ_max(G) = 0.015–0.095), rising to
0.2–1.0 for j ≥ 2; ‖B_M‖ = 0 at j = 1 (to 10^{−14}: 𝒩_T is M-invariant) and 0.5–0.9 for j ≥ 2. λ_min(D − Π_ee) = 1.7–4.9·10^{−2}
(n_T = 1), 6.1·10^{−5} (T = 1.2 even, n_T = 2). The j = 1 penalty λ_max(G)/λ_min(D − Π_ee) is 0.9–4.4 at n_T = 1 and 1.6·10³ at
T = 1.2 even.

6.3 Falsifiers on K_j(w) (sign of λ_min(a_T^w|_{K_j(w)}); "+" = not rejected). Even sector; odd sector in brackets where
it exists.

| T | c=0.9 | c=0.99 | c=1.01 | c=1.1 | no 2 | no 3 | η=+0.1 | η=−0.1 | η=+0.5 | η=−0.5 | swap | 3→3.2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| log 2, j=1 | + | + | + | + | − | + | + | − | + | − | + | + |
| log 2, j≥2 | − | + | + | + | − | + | + | − | + | − | + | + |
| ½log5, j=1 | + | + | + | + | − | + | + | − | + | − | + | − |
| ½log5, j=2–3 | − | + | + | + | − | − | + | − | + | − | + | − |
| ½log5, j≥4 | − | + | + | + | − | − | + | − | − | − | + | − |
| 0.9, j=1 | − [+] | + | + | + | − | − [+] | + | − | + | − | + | − [+] |
| 0.9, j≥3 | − | − [+] | + | + | − | − | + | − | − [+] | − | − (j≥4) [+] | − |
| 1.0, j=1 | − | + | + | + | − | − [+] | + | − | + | − | + | − |
| 1.0, j≥2 | − | − (j≥2 ev, j≥3 odd) | + | + | − | − | + | − | + (ev) / + | − | − (j≥4 ev) [+] | − |
| 1.2, j=1 (ev) | − | − | + | + | − | − | + | − | + | − | − | − |
| 1.2, j≥3 (ev) | − | − | + | + (− at j=6) | − | − | − | − | − | − | − | − |

Reading. (a) cΛ: the family rejects c = 0.9 from j = 2 at every window and c = 0.99 from j = 2–3 at T ≥ 0.9, but it does
**not** reject c = 1.01 or 1.1 at T ≤ 1.0 for any j ≤ 6, although λ_A(T; 1.1Λ) < 0 there (ROUND_003_A Lemma 4 with the
Π-indefinite near-null pair gives λ_A(T; cΛ) ≤ λ_ev,2 − 0.1|μ_−| < 0 for T ≥ 0.7). This is the pencil reading of Prop. 3.5:
on K_j the pencil M − cΠ_P is still positive at c = 1.1 because K_j does not contain the near-null pair. Only at T = 1.2
even, j = 6 (dim 12) is c = 1.1 rejected. (b) Deletions, negative modifications and the Beurling shift are rejected
early (j ≤ 2); positive modifications (η = +0.1) are rejected only at T = 1.2 even, j ≥ 3; the swap needs j ≥ 4 and
T ≥ 0.9. The pattern is that of ROUND_004_A: the conditions reject what pushes the comb below Λ or moves a contact, and
are blind to what pushes it above, because the Π-indefinite near-kernel of a_T is not in the family.

6.4 The scalar j = 2 lemma and the degree-2 split (even sector unless stated).

| T | α | μ_1 | μ_2 | μ_3 | m_2 = Arch(Π_Pe) | eig of (SL_2^{sc}) | det | ‖Πe‖² = (P) + (R) − (L) | ‖ΓΠe‖²/‖Πe‖² |
|---|---|---|---|---|---|---|---|---|---|
| log 2 | −0.150 | −0.184 | 0.063 | −0.017 | +0.033 | 5.8e−3, 7.8e−2 | 4.5e−4 | 0.124 = 0 + 0.733 − 0.609 | 0.48 |
| ½log5 | −0.305 | −0.352 | 0.186 | −0.117 | +0.021 | 2.0e−3, 1.8e−1 | 3.8e−4 | 0.247 = 0.067 + 1.189 − 1.010 | 0.23 |
| 0.9 | −0.420 | −0.437 | 0.206 | −0.095 | −0.058 | 2.7e−3, 5.1e−2 | 1.4e−4 | 0.295 = 0.097 + 1.497 − 1.299 | 0.29 |
| 0.9 odd | −0.112 | −0.161 | 0.101 | −0.083 | +0.070 | 2.7e−3, 2.0e−1 | 5.3e−4 | — | — |
| 1.0 | −0.531 | −0.561 | 0.367 | −0.289 | −0.117 | 1.9e−3, 2.0e−1 | 3.7e−4 | 0.456 = 0.181 + 1.989 − 1.715 | 0.19 |
| 1.0 odd | −0.218 | −0.236 | 0.083 | −0.041 | +0.030 | 2.7e−3, 8.5e−2 | 2.3e−4 | — | — |
| 1.2 odd | −0.404 | −0.422 | 0.209 | −0.126 | −0.038 | 1.9e−3, 1.1e−1 | 2.0e−4 | — | — |

(μ_k, m_2 with Π_P in the Galerkin sector model; the split of ‖Πe‖² in t-space with the uncompressed Π, Gauss–Legendre
3000 nodes, the three parts summing to the direct value to 10^{−5}; ‖PΠe‖² agrees with the Galerkin μ_2 to 1–2 %.)
Reading. (SL_2^{sc}) holds at every tested pair with smaller eigenvalue ≈ 2–6·10^{−3}. The comb response Π_Pe is itself
archimedean-negative at T ≥ 0.9 (m_2 < 0): the sign of a_T on it comes from −μ_3 > 0, i.e. from the comb being negative
on its own response (μ_3/μ_2 = −0.28 … −0.82), which is the cubic term. In the degree-2 split, (P) = Λ∗Λ part is the
smallest term and positive; (R) and (L) are each several times ‖Πe‖² and cancel to 15–20 %.

## 7. Assessment against R1–R5, and the falsifier test

R1 (dim → ∞, Λ-dependent). Satisfied formally: dim K_j = j·n_T with n_T ≥ ⌈6T/π⌉ − 3 (Lemma 2.1), Λ-dependent from
j = 2. But the family is scale-invariant as a set (Prop. 3.5(ii)); its cΛ-dependence is the pencil's.
R2 (non-linear at the deciding step). Satisfied in form: entries of degree ≤ 2j − 1 with products v_mv_n, Λ∗Λ at
degree 2 (Prop. 3.3), near-coincidence classes W_3(r) at degree 3 (Prop. 3.4). Not satisfied in substance: the only
sign-definite degree-2 pieces are the Bochner form (R) and the leak square (L), both comb-generic; the Λ∗Λ part is
small; the near-coincidences enter with the wrong sign for the inequality (they enlarge μ_3).
R3 (exact reduction with controlled complement). (ii) holds: Thm 4.1 + Cor. 4.3 is an exact reduction with an explicit
finite-rank penalty on the comb responses, PROVED, and a PROVED degree-2 bound on the coupling (λ_max(G)). (i) fails:
NUMERICALLY the family does not capture the minimiser (3–4 orders above λ_A at dim 20, T ≤ 1), because the comb steps do
not generate the archimedean directions of the near-kernel; coercivity of a_T on K_j^⊥ minus the penalty is the whole
problem and no Λ-free coercivity exists (arena). The reduction organises the sign; it does not supply it.
R4 (joint archimedean/Euler entry; comb-first escapes the arena count). The entries do couple both (Prop. 3.1(iii): K
evaluated at u − log r, r ∈ ℚ_{>0}); the family escapes the arena count as a count (its dimension is j·n_T, not N*(T)),
but inherits the arena obstruction on the complement (§4.3(c)) and, numerically, needs a dimension comparable with the
section to reach the bottom (§6.1). So the gap named in OBJECT_SPEC R4 is not exploited by this generator.
R5 (falsifier test). The identities of §3–4 are identities and survive every falsifier (they must: they are
bookkeeping, not a sign step). The conditions (SL_j): (a) cΛ — rejected for c < 1 from j = 2, not rejected for
c ∈ (1, 1.1] at T ≤ 1.0 and j ≤ 6, although (★) fails there: **the family fails the test on the side c > 1**, because its
subspace is scale-invariant and misses the Π-indefinite near-kernel; (b) a_P — rejected at j = 1 (deletion of 2) and
j = 2 (deletion of 3); (c) Beurling 3 → 3.2 — rejected at T ≥ ½log5 even, j ≥ 1; (d) finite modifications — rejected for
η < 0 at j = 1, for η = +0.1 only at T = 1.2, j ≥ 3. Where an argument built on (SL_j) with j ≤ 6 would survive c = 1.1
at T = 1, it would be wrong; the memo makes no such argument.

NO-GO (class, NUMERICAL evidence, PROVED mechanism). Class: "the comb-generated Krylov family from the archimedean
negative cone, at dimension j·n_T with j bounded, as the carrier of the sign". Mechanism (PROVED pieces): the family is
scale-invariant as a set (Prop. 3.5(ii)), so on it the falsifier cΛ reduces to the pencil, and the pencil at c > 1 is
decided by the Π-indefinite near-null pair of a_T (ROUND_003_A Lemma 3–4), which the comb steps do not generate (the
A-steps do, by the commutators of 4.2(v)); NUMERICAL: K_20 is still 10^{3–4}λ-units above the bottom at T ≤ 1. The
label is NO-GO for bounded j; for j growing with the section it is a restatement.

## Result

PIVOT with reason. The comb-first Krylov family is built, its matrix structure, scaling and exact Schur reduction are
PROVED, and the sign lemma on K_2 is written explicitly (SL_2, scalar form (SL_2^{sc}), exact degree-2 split H_2 + Δ). The
family does not carry the sign: as a set it is invariant under cΛ, it misses the Π-indefinite near-kernel of a_T
(the comb does not generate it; the archimedean halo/leak commutators do), and it converges to the bottom 3–4 orders
of magnitude more slowly than the A-generated family at equal dimension. The generator must change: the next family
must include the archimedean steps that produce the near-null pair, i.e. be generated by both M and Π_P (or by the
halo/leak operators of 4.2(v)) from the same seed, while keeping the entries polynomial in v.

## What was proved

- Lemma 2.1: Λ-free negative cone Σ_T ⊂ P_T of dimension ≥ ⌈2Tt_1/π⌉ − 3, with Arch ≤ −B(t_1² − (πN_T/2T)²) on it;
  n_−(M) ≥ that. Lemma 2.2: 𝒟_T ∩ L^∞ ∩ P_T is Π_P-invariant (so K_j is in the form domain for the explicit cone;
  CONDITIONAL on boundedness of the negative eigenfunctions for the spectral cone).
- Prop. 3.1: entries of a_T on K_j are polynomials of degree ≤ 2j − 1 in v (≤ 2j − 2 archimedean, 2j − 1 comb) with
  coefficients = archimedean kernel K integrated against overlaps of dilated modes at shifts u − log r, r ∈ ℚ_{>0}.
- Lemma 3.2: same-direction truncated shifts compose exactly (QV_aQV_bQ = QV_{a+b}Q); opposite directions produce the
  edge-slab (leak) correction 𝒯_{a,b} = QV_aRV_{−b}Q. Prop. 3.3: Π² = Qσ_v²Q − 𝔏*𝔏 with Qσ_v²Q = ½Σ(v∗v)(N)S_{log N} +
  ½Σv_mv_nS_{log(m/n)}, i.e. ⟨F,Π²F⟩ = [Λ∗Λ comb] + [Dirichlet-polynomial mean value ≥ 0] − [leak square]. Prop. 3.4:
  Π³ = Qσ_v³Q − (three leak words), Qσ_v³Q = ¼Σ(v∗v∗v)(N)S_{log N} + ¾Σ_r W_3(r)S_{log r}, W_3(r) ≥ 0: near-coincidences
  mn ≈ k appear first at degree 3, and enlarge the comb's third moment on the responses.
- Prop. 3.5: monomial entries scale as c^{deg}; K_j(cΛ) = K_j(Λ) as sets; the K_j-condition under cΛ is the pencil.
- Thm 4.1: form-level Schur complement for finite K ⊂ 𝒟_T ∩ P_T (no operator domain needed). Prop. 4.2: with the
  spectral cone, A K_1 ⊂ K_2 (Krylov spaces of A and Π_P agree at j = 2), the coupling of K_1 to K_1^⊥ is carried by the
  comb responses f_α alone, G = (Π_P²)_ee − Π_ee² ⪰ 0 is its Gram matrix, the block matrix of a_T on K_2 is explicit
  (degrees 1 / 2 / 3), and [M_0, S_x] = Qc_xR𝔪Q − Q𝔪Rc_xQ (halo shifted back, leak read through K). Cor. 4.3: (★) at T
  ⟺ (SL_1) and a_T ≥ finite-rank penalty on K_1^⊥ supported on the responses, penalty norm ≤ λ_max(G)/λ_min(D − Π_ee).
- §5: (SL_1), (SL_2), (SL_2^{sc}) written out; exact identity (SL_2^{sc}) ⟺ H_2 + Δ ⪰ 0 with H_2 the moment matrix of
  s_T|ê|²dτ/2π on polynomials of degree ≤ 1 in σ_v and Δ the explicit leak/halo terms.
- NUMERICAL validations: all word identities to 10^{−16}; the degree-2 split to 10^{−5}; (SL_2^{sc}) holds with margin
  2–6·10^{−3}; Galerkin μ_2 vs t-space ‖PΠe‖² to 1–2 %.

## What failed and why

- Capture of the minimiser (R3(i)): the comb-generated family stalls 3–4 orders of magnitude above λ_A at dimension 20
  for T ≤ 1 (A-generated reaches λ_A at the same dimension). Reason (PROVED structure + NUMERICAL): the near-null pair of
  a_T is reached through the archimedean commutator terms [M, Π_P]K_1 (halo/leak), which the Π-Krylov recursion omits;
  the two families coincide only at j = 2.
- Falsifier c > 1: not rejected for j ≤ 6 at T ≤ 1.0. Reason (PROVED): K_j is scale-invariant as a set, and the pencil on
  K_j is positive at c = 1.1 because the Π-indefinite near-kernel is outside K_j.
- Sign mechanism at degree 2: the only sign-definite pieces are Bochner (R) and a square (L), comb-generic; the
  Λ∗Λ part is small; (R) and (L) cancel to 15–20 % of their size. No "Dirichlet-convolution positive form + small
  remainder" structure exists (NUMERICAL); the remainder inequality (end of §5.3) is OPEN with no mechanism.
- Near-coincidences (ℕ,+): located exactly (degree 3, classes W_3(r) ≥ 0), but they enter (SL_2) with the sign that
  strengthens the comb on the responses, i.e. against the inequality.
- The polar corrections (rank 2 per step) are 19–48 % of ‖Πe‖² at T ≤ 1.2: not a perturbation.

## Next concrete step

Replace the generator. Build K̃_j := span{ W e : e ∈ 𝒩_T, W a word of length < j in {Π_P, M} } — equivalently the
Krylov family of the pair (M, Π_P), or of A together with the halo/leak operators H_x := Qc_xR𝔪Q and L_x := Q𝔪Rc_xQ of
Prop. 4.2(v) — from the same Λ-free seed. Its entries are still polynomials in v (degree ≤ word length + 1) with
archimedean coefficients, it is not scale-invariant as a set (M-steps break Prop. 3.5(ii)), and at j = 2 it already
contains [M, Π_P]𝒩_T. First check (NUMERICAL, same scripts): whether K̃_3 captures the near-null even pair (principal
cosine > 0.99) and rejects c = 1.1 at T = 1.0; if yes, write the 3×3 (n_T = 1) sign lemma on {e, Π_Pe, [M,Π_P]e} with the
explicit halo/leak kernels and test whether its degree-2 archimedean block has a sign structure specific to the halo
kernel K (the one object here that is not comb-generic: K is the Lévy kernel of Γ(s/2) at conductor 1). If K̃_3 does
not capture the pair either, the seed is wrong (not the generator) and the next seed is the Λ-free archimedean
near-null candidate of ROUND_004_A E_k with k ≥ 6, under the mixed generator.
