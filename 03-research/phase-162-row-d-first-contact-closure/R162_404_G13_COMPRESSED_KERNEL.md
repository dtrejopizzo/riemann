# R162_404 — G1.3: the compressed kernel equation tested on smooth-comb images

Round 4, mechanism G1.3.

Status: **NO-GO (PROVED), with four PROVED STEPS.** Gate 1 is not closed.

- PROVED STEP 1 (§2, compressed Dirichlet algebra). Take P ≥ e^{2T}. Then P_T Z_P P_T = Z_T, the
  compressed *integer* comb Σ_{n<e^{2T}} n^{−1/2} P τ_{log n} P. It does not depend on P. The compressed
  left shifts form a semigroup, so Z_T = I + N with N nilpotent. The inverse is exactly the compressed
  Möbius comb Σ_{n<e^{2T}} μ(n)n^{−1/2}Pτ_{log n}P. The compressed Chebyshev identity B^*Z_T = K_T is
  exact.
- PROVED STEP 2 (§3, reparametrization). The tests G = P_T Z_P^*ψ (ψ ∈ form domain of L²(I_T)) run
  over the **whole** form domain. The tested family is therefore *equivalent* to eq:localweak, and the
  tests P_T Z_P ψ give its J-image.
- PROVED STEP 3 (§4, exact Brown–Halmos identity). For H_TF = λF,
  𝔞_T(Z_TF, ψ) = λ⟨Z_TF, ψ⟩ + ⟨Z_T r, ψ⟩ − 𝔡(F, ψ). Here 𝔡 = 𝔟_M − 𝔟_Λ is the commutator
  defect. Its Gamma part 𝔟_M carries **all** Gamma coordinates μ_F(a_j) = εK_F(a_j), j ≥ 0, with the
  weights Σ_{n<e^{2T}} n^{−s_j} (truncated ζ(s_j)). Its prime part 𝔟_Λ carries only right and left
  collar products (Hankel–Hankel, H^*H).
- PROVED STEP 4 (§5, polar layer = exterior Hankel). For exterior tests φ, P_T Z_P^*φ = Γ_P^*φ with
  Γ_P = (I−P_T)Z_PP_T. On (−∞,−T), Γ_PF has Laplace transform ζ_P(½+a)μ_F(a) − (entire). The principal
  part at a = −½ is a **nonsingular triangular** image of the Tate jets μ_F^{(i)}(−½) = ∫tⁱe^{−t/2}F,
  1 ≤ i ≤ π(P)−1.
- NO-GO (§6). In the tested equation the polar layer and the Tate jets enter **only through the term
  λ⟨Γ_PF, φ⟩**. At λ = 0 (first contact) they drop out identically. For λ > 0 they are determined by
  the Brown–Halmos data. The mechanism is F1-inverted: it constrains the jets exactly when no
  constraint is wanted. Every consequence of the family is a consequence of H_TF = 0 alone. Such a
  consequence can force R_LF = 0 only by proving ker H_T = {0}, which does not use minimality. The Gamma
  residues are tied to finite truncated collar data and not to the jets. No Vandermonde/Hankel system
  links (i) and (ii).

Notation follows Paper 46 §sec:firstcontact, R162_401 and R162_403. I = I_T = (−T,T). P = P_T is
restriction to I followed by extension by zero. Π is the projection of L²(I) onto 𝒫_T. τ_c F(t) =
F(t+c) (left shift) and V_c F(t) = F(t−c) (right shift). μ_F(a) = ∫e^{at}F and K_F(a) = ∫e^{−at}F, so
μ_F = εK_F when JF = εF. a_j = 2j+½, s_j = 2j+1. The real pairing is used throughout. The form is
𝔞_T = 𝔪_T − ⟨(B+B^*)·,·⟩, with B = P Σ_{d<e^{2T}} ℓ_d V_{log d} P, ℓ_d = Λ(d)d^{−1/2} (right shifts), so
that B^* consists of left shifts. For F in dom H_T, r ∈ span{e^{±t/2}} is defined by
𝔞_T(F, G) = ⟨H_TF + r, G⟩ for all G in the form domain 𝒬 of L²(I).

## 0. Corpus check (before building)

- **R162_301 Thm 1.1** (global Brown–Halmos, T_f^*T_f − T_fT_f^* = H_f^*H_f on H_T). That result is
  an identity for **every** g, with no kernel equation, and it concerns the Euler history A_P. Here
  the Hankel enters through the commutator of Z_T with the *form* 𝔞_T, evaluated on a kernel vector
  (§4). This is the case R162_403 §7 asked to be checked. It is **not** closed by R162_301. The mixed
  defect of §4 has the same algebraic origin, (3.2) of R162_301 (compressed τ_a vs V_b), but R162_301
  never pairs it against 𝔞_T or H_TF = 0.
- **R162_403 §4.2(ii), §7.** The polar layer Pol_P at a = −½, of order π(P)+1. Here it is located
  exactly: it is the exterior Hankel image Γ_PF (§5). Its order in the pairing drops by one because
  μ_F(−½) = B(F) = 0.
- **R162_101 / P124_001.** Joint variation at a fixed window returns the radical equation
  tautologically. §3 is the operator form of this fact for comb tests.
- **R160 survey F21** ("finite-S scalar Euler/Tate colligation … poles/zeros"). These are the same
  poles a = −½ + 2πik/log p (§5). **NG-F1** (smoothness controls the localized sign, not
  multiplicativity) is consistent with Prop. 2.3: the only Λ-specific identity is a semigroup identity.
- R160 survey, "compression" entries (0A2 faithfulness ≠ positivity; the CC Sonin compression). No
  entry treats comb-conjugation of the local kernel equation. The construction is new, and so is the
  negative result.

## 1. Two preliminary lemmas (PROVED)

**Lemma 1.1 (compressed shift semigroups).** For a, b ≥ 0:
(a) Pτ_aPτ_bP = Pτ_{a+b}P and PV_aPV_bP = PV_{a+b}P. Also Pτ_aP = 0 = PV_aP when a ≥ 2T.
(b) Put H^L_a := (I−P)τ_aP : L²(I) → L²(−∞,−T) and H^R_b := (I−P)V_bP : L²(I) → L²(T,∞). Then

    Pτ_aP·PV_bP − PV_bP·Pτ_aP = −(H^R_a)^* H^R_b + (H^L_b)^* H^L_a.            (1.1)

*Proof.* (a) (Pτ_aPτ_bPg)(t) = 1_I(t)1_I(t+a)1_I(t+a+b)g(t+a+b). If t ∈ I and t+a+b ∈ I, then
t+a ∈ I by convexity. The same argument works for V. If a ≥ 2T, then t and t+a cannot both lie in I.
(b) On the line, τ_aV_b = V_bτ_a. Insert I = P + (I−P) between the factors. This gives
Pτ_aPV_bP − PV_bPτ_aP = −Pτ_a(I−P)V_bP + PV_b(I−P)τ_aP. The adjoint of H^R_a is Pτ_a(I−P), and the
adjoint of H^L_b is PV_b(I−P). ∎

(1.1) is the Brown–Halmos formula T_{fg} − T_fT_g = H^*H in the interval setting.

**Lemma 1.2 (indicators act on the form domain).** Multiplication by 1_{(c,∞)} is bounded on
𝒬(ℝ) = {g : ∫log(2+|τ|)|ĝ|² < ∞}. So Pτ_aP, PV_aP, H^L_a, H^R_a are bounded on 𝒬.

*Proof.* On the Fourier side, 1_{(c,∞)} = ½(1 + sgn(x−c)) acts by modulation and the Hilbert
transform. The Hilbert transform is bounded on L²(w dτ) for w ∈ A_2 (Hunt–Muckenhoupt–Wheeden). Also
w(τ) = log(2+|τ|) ∈ A_2: w is even and increasing in |τ|, and for an interval J of length R containing
0 (the worst case), avg_J w ≍ log(2+R) and avg_J w^{−1} ≍ 1/log(2+R). Translations are unitary on
𝒬. ∎

## 2. The compressed Dirichlet algebra (PROVED STEP 1)

Let 𝒟_T be the set of operators D(a) := Σ_{n<e^{2T}} a(n)n^{−1/2}Pτ_{log n}P, a: ℕ → ℂ.

**Proposition 2.1.** D(a)D(b) = D(a*b), where * is Dirichlet convolution truncated at n < e^{2T}.
Hence 𝒟_T is commutative, and D is a homomorphism from Dirichlet series modulo the ideal
{n ≥ e^{2T}} onto 𝒟_T.

*Proof.* By Lemma 1.1(a), (dm)^{−1/2}Pτ_{log d}Pτ_{log m}P = (dm)^{−1/2}Pτ_{log dm}P. This vanishes
when dm ≥ e^{2T}. ∎

**Corollary 2.2.** Let P ≥ e^{2T}. Then P Z_P P = Z_T := D(1), independently of P. The operator Z_T
is invertible on L²(I) and on 𝒬∩L²(I), with Z_T^{−1} = D(μ), where μ is the Möbius function. Also
Z_T − I = D(1 − δ_1) is nilpotent: (Z_T − I)^k = 0 for k ≥ 2T/log 2.

*Proof.* Every n < e^{2T} is P-smooth. By Lemma 1.1(a) the smooth n ≥ e^{2T} contribute 0. Then
1*μ = δ_1, and D(δ_1) = P. For nilpotency, (1−δ_1)^{*k} is supported on n ≥ 2^k. Boundedness on 𝒬
follows from Lemma 1.2. ∎

**Proposition 2.3 (compressed Chebyshev, exact).** B^*Z_T = K_T := D(log). The identity holds with Λ
replaced by a iff a*1 = log on n < e^{2T}.

*Proof.* B^* = D(Λ). Apply Prop. 2.1: Λ*1 = log. ∎

This is the compressed version of R162_403 Lemma 1.2. It is a coefficient identity in 𝒟_T, valid for
every F. The G1.3 identity below never uses it: no K_T and no X occur. If X is inserted, the relation
PX = XP gives [X, Z_T] = −K_T exactly, and Prop. 2.3 then reproduces the tautology of R162_403 §5
inside 𝒟_T.

## 3. Reparametrization of the kernel equation (PROVED STEP 2)

**Theorem 3.1.** Let F ∈ 𝒫_T ∩ 𝒬, let r ∈ span{e^{±t/2}}, let λ ∈ ℝ and P ≥ e^{2T}. The following
are equivalent:
(a) 𝔞_T(F, G) = λ⟨F, G⟩ + ⟨r, G⟩ for all G ∈ 𝒬∩L²(I);
(b) 𝔞_T(F, P Z_P^*ψ) = λ⟨F, P Z_P^*ψ⟩ + ⟨r, P Z_P^*ψ⟩ for all ψ ∈ 𝒬∩L²(I);
(c) the same with P Z_P ψ in place of P Z_P^*ψ.
If JF = εF, then (b) and (c) are exchanged by ψ ↦ Jψ.

*Proof.* P Z_P^*ψ = Z_T^*ψ, and Z_T^* = D(1)^* is invertible on 𝒬∩L²(I) by Cor. 2.2 applied to the
adjoint algebra (compressed right shifts). So {Z_T^*ψ} = 𝒬∩L²(I), which proves (a)⇔(b). For (c),
note JPτ_cPJ = PV_cP, so JZ_TJ = Z_T^*. Now 𝔞_T is J-invariant and Jr = εr, and a second
application of the same argument gives (a)⇔(c). ∎

So interior comb tests contain exactly the information in eq:localweak, whatever P is. For
P ≥ e^{2T} they are even independent of P. The data of order π(P) (Tate jets, Pol_P) cannot appear in
them.

## 4. The exact Brown–Halmos identity (PROVED STEP 3)

**Theorem 4.1.** Let F ∈ dom H_T, H_TF = λF, with r as above, and let ψ ∈ 𝒬∩L²(I). Then

    𝔞_T(Z_TF, ψ) = λ⟨Z_TF, ψ⟩ + ⟨Z_T r, ψ⟩ − 𝔡(F, ψ),    𝔡 = 𝔟_M − 𝔟_Λ,              (4.1)

with, writing Σ_n = Σ_{n<e^{2T}} and truncated moments μ^{[α,β]}, K^{[α,β]},

    𝔟_M(F,ψ) = Σ_{j≥0} Σ_n n^{−s_j} [ μ_F(a_j) K_ψ^{[T−log n, T]}(a_j) − μ_F^{[−T, −T+log n]}(a_j) K_ψ(a_j) ],   (4.2)
    𝔟_Λ(F,ψ) = Σ_{n,d<e^{2T}} n^{−1/2} ℓ_d [ ⟨H^R_{log d}F, H^R_{log n}ψ⟩ − ⟨H^L_{log n}F, H^L_{log d}ψ⟩ ].       (4.3)

The j-series in (4.2) converges absolutely after the n-sum is taken inside the integral (see the
proof). The j = 0 term of the first bracket vanishes because μ_F(½) = A(F) = 0.

*Proof.* By definition of r and because Z_T^*ψ ∈ 𝒬 (Lemma 1.2),
𝔞_T(F, Z_T^*ψ) = ⟨λF + r, Z_T^*ψ⟩ = λ⟨Z_TF, ψ⟩ + ⟨Z_Tr, ψ⟩. Put
𝔡 := 𝔞_T(F, Z_T^*ψ) − 𝔞_T(Z_TF, ψ). We compute 𝔡 separately for the Gamma part and for the prime
part.

*Prime part.* We have Z_T^* = Σ_n n^{−1/2}PV_{log n}P, and B^* ∈ 𝒟_T commutes with Z_T (Prop. 2.1).
So the prime contribution to 𝔡 is −⟨[Z_T, B]F, ψ⟩. Apply (1.1) with a = log n and b = log d. This
gives −[Z_T, B] = Σ n^{−1/2}ℓ_d[(H^R_{log n})^*H^R_{log d} − (H^L_{log d})^*H^L_{log n}], which is
(4.3).

*Gamma part.* On the line M commutes with translations, and ⟨MF, g⟩ = 𝔪(F, g) for F, g ∈ 𝒬(ℝ).
Write PV_bPψ = V_bψ − H^R_bψ and Pτ_aPF = τ_aF − H^L_aF, with a = b = log n. Then
𝔪_T(F, PV_bPψ) − 𝔪_T(Pτ_aPF, ψ) = −⟨MF, H^R_bψ⟩ + ⟨MH^L_aF, ψ⟩, because the terms ⟨MF, V_bψ⟩ and
⟨Mτ_aF, ψ⟩ are equal. In each remaining pairing the two supports are disjoint (I against (T,∞), and
(−∞,−T) against I). So only the off-diagonal kernel of M enters. With m(τ) = −log π + Re ψ(¼+iτ/2)
and ψ(z) = −γ + Σ_{j≥0}((j+1)^{−1} − (j+z)^{−1}), one term is −(j+¼+iτ/2)^{−1} = −2/(a_j+iτ). Its
real part has kernel −e^{−a_j|x|}. So

    κ(x) = −Σ_{j≥0} e^{−a_j|x|} = −e^{−|x|/2}/(1−e^{−2|x|})    (x ≠ 0).

For t > T this gives MF(t) = −Σ_j e^{−a_jt}μ_F(a_j). Hence
−⟨MF, H^R_bψ⟩ = Σ_j μ_F(a_j)∫_T^{T+b}e^{−a_jt}ψ(t−b)dt = Σ_j n^{−a_j}μ_F(a_j)K_ψ^{[T−b,T]}(a_j).
Similarly, ⟨MH^L_aF, ψ⟩ = −Σ_j μ_{H^L_aF}(a_j)K_ψ(a_j) with
μ_{H^L_aF}(a_j) = n^{−a_j}μ_F^{[−T,−T+a]}(a_j). Multiplying by n^{−1/2} gives n^{−s_j} and hence (4.2).
Convergence: the nonnegative kernel Σ_j e^{−a_jx} ≤ C/x, and ∫∫_{u<T<t}|f(u)||g(t)|/(t−u) ≤ π‖f‖‖g‖
by Hilbert's inequality. Tonelli–Fubini then allows termwise summation. ∎

**Remarks.** (i) (4.1) says that Z_TF satisfies the perturbed equation "H̃(Z_TF) = λZ_TF + Z_Tr − 𝔡".
The whole kernel information is carried by the commutator [Z_T, H̃], which is a sum of Hankel–Hankel
products. This is the only non-symbol object (R162_403 §7).
(ii) The Gamma residues enter through 𝔟_M alone. Their weights are the partial sums
ζ_{<e^{2T}}(s_j) := Σ_{n<e^{2T}} n^{−s_j}, one for each n, paired with *truncated* moments of ψ on the
collar [T−log n, T]. Taking ψ = (Z_T^*)^{−1}ΠS_LF in (a) of Thm 3.1 simply returns eq:Qbalance.
(iii) Every quantity in (4.1)–(4.3) is finite and independent of P ≥ e^{2T}.

## 5. The polar layer is the exterior Hankel (PROVED STEP 4)

Let φ ∈ C_c^∞((−∞,−T)). Then P Z_P^*φ = P Z_P^*(I−P)φ = Γ_P^*φ, where Γ_P := (I−P)Z_PP. This is a
finite sum of compressed right shifts of φ, so it lies in 𝒬∩L²(I).

**Proposition 5.1.** For F ∈ L²(I) ∩ 𝒫_T:
(a) Γ_PF = Z_PF on (−∞,−T). Its two-sided Laplace transform is
μ_{Γ_PF}(a) = ζ_P(½+a)μ_F(a) − μ_{Z_TF}(a) for Re a > −½, and the last term is entire.
(b) The poles on Re a = −½ are: a = −½ + 2πik/log p (k ≠ 0, p ≤ P), which are simple and distinct;
and a = −½, of order ≤ π(P) − 1.
(c) Put w = a + ½. The principal part at a = −½ is Σ_{k=1}^{π(P)−1} c_k w^{−k} with
c = 𝐔 𝐉. Here 𝐉 = (μ_F^{(i)}(−½))_{1≤i≤π(P)−1}, where μ_F^{(i)}(−½) = ∫tⁱe^{−t/2}F are the Tate jets,
and 𝐔 is triangular with diagonal entries (Π_{p≤P}log p)^{−1}/i! ≠ 0. So the map 𝐉 ↦ c is
nonsingular.
(d) For t < −T the expansion of Γ_PF by the residues on Re a = −½ is exact, as a limit of symmetric
partial sums.

*Proof.* (a) Z_PF is supported in (−∞,T] and Z_TF = PZ_PF, so (I−P)Z_PF = Z_PF on (−∞,−T). The
Laplace transform of τ_cF is e^{−ac}μ_F(a), so μ_{Z_PF} = Σ_{smooth} m^{−½−a}μ_F(a). The function
Z_TF has compact support, so its transform is entire. (b) ζ_P(w) = Π(1−p^{−w})^{−1}. Its poles are
w = 2πik/log p; they are distinct because log p/log q ∉ ℚ. At w = 0 the order is π(P), and it drops by
one because μ_F(−½) = B(F) = 0. (c) 1 − p^{−w} = w log p(1 − ½w log p + …), so
ζ_P = (Π log p)^{−1}w^{−π(P)}(1 + O(w)). Also μ_F(a) = Σ_{i≥1}𝐉_i w^i/i!. Multiply and read off the
coefficients of w^{−k}. (d) Inverse Laplace: shift the contour from Re a = c > −½ to Re a = −σ. The
integrand is bounded by |ζ_P(½−σ+iy)||μ_F||e^{−at}| ≤ Π(p^{σ−½}−1)^{−1}e^{σ(T+t)}. For t < −T this
tends to 0 as σ → ∞. The horizontal segments are handled as in R162_403 Thm 4.2. ∎

**Corollary 5.2 (exterior-tested equation).** Let H_TF = λF. Then for all φ ∈ C_c^∞((−∞,−T)),

    λ ⟨Γ_PF, φ⟩ = 𝔞_T(F, Γ_P^*φ) − ⟨Γ_P r, φ⟩.                                  (5.1)

Also Γ_P is injective on L²(I) for P ≥ e^{2T}.

*Proof.* (5.1) is the definition of r with G = Γ_P^*φ. For injectivity, suppose Γ_PF = 0. Then
Z_PF = Z_TF =: G has compact support in Ī, and F = A_P G with A_P = Π_{p≤P}(1 − p^{−1/2}τ_{log p}).
Let [α,β] be the convex hull of supp G. The shift by log N_P, N_P = Π_{p≤P} p ≥ 2P > e^{2T}, occurs in
exactly one term of A_P. So A_PG ≠ 0 near α − log N_P < −T. This contradicts supp F ⊂ Ī, unless
G = 0, in which case F = 0. ∎

## 6. Decision (NO-GO, PROVED)

**Theorem 6.1.** Let F be a first-contact vector at T = T_*, so λ = 0. Take any P ≥ e^{2T}, and form
any combination of the tested equations with interior tests P Z_P^{(*)}ψ (§3–§4) and exterior tests
Γ_P^*φ (§5).
(a) Every identity so obtained is a consequence of eq:localweak (Thm 3.1; Cor. 5.2 is an instance of
eq:localweak). It holds for every F ∈ ker H_T at every window, whether or not H_T ≥ 0 and whether or
not T is minimal.
(b) The Tate jets 𝐉 and the whole polar layer occur only in the term λ⟨Γ_PF, φ⟩ of (5.1). At λ = 0
their coefficient is zero. So no relation between (i) the jets and (ii) the Gamma residues arises at
first contact.
(c) The Gamma residues μ_F(a_j) occur only in 𝔟_M (4.2), paired with truncated moments of ψ with
weights n^{−s_j}, n < e^{2T}. These data do not depend on P, so no system indexed by π(P) can bind
them.
(d) So the family forces R_LF = 0 at first contact iff it forces ker H_T = {0}. This is not a
conclusion that uses minimality (condition (i) of prob:annihilate), so the route cannot close Gate 1
as posed.

*Proof.* (a) Thm 3.1 and Cor. 5.2. (b) Cor. 5.2 together with Prop. 5.1(a): the polar data of Γ_PF
belong to the left side of (5.1) only. The right side is an evaluation of eq:localweak at an interior
test. (c) Thm 4.1, Remark (iii). (d) By (a), whatever follows from the family holds on ker H_T. The
map R is faithful and ker H_T is finite-dimensional (paper, after prob:annihilate), so "R_LF = 0 for
some L, for all F ∈ ker H_T" ⟺ ker H_T = {0}. ∎

**Exact obstruction.** The only non-symbol input, the compression, enters the kernel equation through
the invertible Möbius-conjugation Z_T (§3) and the Hankel commutator 𝔡 (§4). Both are linear in F and
independent of λ. The single place where π(P)-order data (the Tate jets) would be bound, (5.1), carries
them with coefficient λ. A nonsingular jet system (Prop. 5.1c) does exist, but it is multiplied by the
eigenvalue.

## 7. Falsifiers

- **F1 (λ > 0, explicit).** For an eigenvector H_TF = λF with λ > 0, (4.1) acquires λ⟨Z_TF, ψ⟩, and
  (5.1) reads λ⟨Γ_PF, φ⟩ = RHS. Since Γ_P is injective and 𝐉 ↦ c is nonsingular, (5.1) then
  **determines** the polar layer, and hence the Tate jets, from Brown–Halmos/interior data. At λ = 0
  this determination disappears. The mechanism acts where it is not wanted (λ > 0 vectors, for which
  R_LF ≠ 0 is allowed; eq:Qspectral) and is void where it is wanted. That is the NO-GO in F1 form. The
  family does use λ = 0, but only by *deleting* the jet channel.
- **F2.** Everything is linear in F. Replacing 𝔞 by −𝔞 (Weil sign reversal) preserves (a)–(d)
  verbatim.
- **F3 (finite modifications).** Replace Λ by a = Λ + η_0. Thm 3.1, Thm 4.1 (with ℓ_d → a(d)d^{−1/2})
  and Prop. 5.1 hold unchanged, because Z_T, Γ_P and M do not involve Λ. Only Prop. 2.3 fails:
  B_a^*Z_T = K_T + D(η_0*1). But Prop. 2.3 is never used in (4.1) or (5.1). **Davenport–Heilbronn /
  Epstein**: the forms have the same Gamma part, and their Dirichlet coefficients enter only through
  ℓ_d in 𝔟_Λ. Z_T is the integer comb and stays unipotent. So §§3–6 hold verbatim. The G1.3 family has
  no Λ-specific step, and therefore no step that could fail for these data. This agrees with the NO-GO:
  a closing step would have to be Λ-specific.
- **F4.** No limit is taken; all identities are finite at fixed T and P.

## 8. Next sub-lemma

By R162_101 Lemma 1, left minimality is equivalent to H_{T_*} ≥ 0. By Thm 6.1(a), the kernel equation
plus that positivity (Cauchy–Schwarz in the nonnegative form only returns 𝔞(F, ·) = 0) contains
nothing beyond ker. The unused hypothesis is **right minimality (R): λ_A(T) < 0 for T > T_*.**

**G1.4 (window-enlarged Brown–Halmos defect).** Let T' = T_* + δ and zero-extend F. The compressed
algebra 𝒟_{T'} gains the integers n ∈ [e^{2T_*}, e^{2T'}), and the defect 𝔡_{T'}(F, ·) of (4.1) gains
the corresponding collar terms, including the new Gamma weights n^{−s_j} in (4.2). Determine whether
negativity of H_{T'} on span{F, ΠZ_{T'}F, Π(Z_{T'})^{−1}F}, as δ ↓ 0, gives a sign on the new
Gamma-residue collar terms Σ_{e^{2T_*} ≤ n < e^{2T'}} n^{−s_j}μ_F(a_j)K^{[·]}(a_j). Such a sign would be
a genuinely nonlinear use of the compression together with minimality. Mandatory corpus check first:
P124_004 (window variation, one-sided crossing quotient, no sign) and R162_101 §§2–4. G1.4 must show
that it differs from both through the Möbius-conjugated test Π(Z_{T'})^{−1}F.

GATE 1: OPEN. Row D: OPEN.

Files edited: this file only.
