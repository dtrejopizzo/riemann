# R183.029 — (Λ) proved; global (E′) is the wrong target; the correct estimate is local and microlocal

Phase 183.
Neither RH nor the closure of row D is claimed.

Inputs: R183_025 (Thm 1, Thm 2, identity (3.1), definition of r_p, §4), R183_027 (§"is the
half-line model faithful?": the model discards the overlap PP̂P), R183_028 §3.1, R183_018 §3–4,
R183_020. Source: CC 2006.13771 (local text phase-137): Prop 2.2 (42)–(43), Def 4.4 (72),
Prop 4.5 (74)–(82), Thm 4.7 (83)–(90). Nothing from R183_025 is duplicated: its notation is used
(S = {∞,p}, a = log p, ε = p^{−1/2}, τ, m(s) = 1 − εe^{−isa}, K = S(1,1), K' = S(1,1/p), E, D,
R_edge, ⟨X⟩_h = Tr(ϑ(f)X) with f = g∗g^*, f(1) ↔ c_h(0)).

---

## 0. Verdict

1. **(Λ) PROVED (Theorem A).** For every b ∈ (0,1],
   Tr ϑ(f)(Π_{S(1,b)} − Π_{S(1,1)}) = log(1/b)·f(1) + ∫ f(ρ) ε'_b(ρ) d^*ρ. Here ε'_b is continuous and
   bounded, has an explicit formula, and its Mellin density is in L¹(ds) with norm
   ≤ 3C₀ + 4b + 4. The operator ϑ(f)(Π_{S(1,b)} − Π_{S(1,1)}) is trace class, with no need for
   CC's individual finiteness results. With b = 1/p one obtains exactly the term a·c_h(0) that
   R183_025 assumed. Window T only enters via f's support; p only enters via the prolates'
   time-frequency product b.
2. **Exact structure of r_p (PROVED).** r_p = ρ_E − μ_D, where μ_D ≥ 0 is a tempered measure
   and ρ_E(s) = a(1−ε²)/|m(s)|². Hence **r_p ≤ a(1+ε)/(1−ε)** for all s, and identity (3.1)
   makes sense for every h with no hypothesis at all. The lower bound (equivalent to μ_D ≤ C) remains
   OPEN.
3. **The prolates are not the obstacle (PROVED).** Y = Y_0 + Y_pro exactly. Y_pro is trace class,
   with ‖Y_pro‖₁ ≤ 2·4b, and is the part carrying the prolates (R183_027's overlap PP̂P). Y_0 =
   P_E Q P_E, with Q = F P_1 F^{−1} the Paley–Wiener projection, **contains no prolates** and is not
   trace class. Every linear contribution of the prolates to r_p has density in L¹ ∩ L^∞. **The
   n = 0 term contributes O(|s|^{−2}), not 1/|s|.** The strategy "expand in ξ_n with summable
   weights" controls Y_pro and does not touch Y_0.
4. **The heuristic r_p ≍ 1/|s| is incomplete (PROVED in the two-edge model with fixed L;
   transfer to L(s) is heuristic).** The model's exact density (Prop 3.3, with numerical
   control) has a **first-order** term 2ε^{N+1}cos((N+1)sa), N ≈ L/a. With
   L = L(s) = log(|s|/2π), that term has amplitude ≍ |s|^{−1/2}, **which is not in L²(ds)**, and
   phase with "position" t ≈ L(s) → ∞. The non-oscillating part is ≍ e^{−L(s)} ≍ 1/|s|. Hence
   **(E′) as formulated (r_p ∈ L²(R,ds) global) is expected FALSE**, and moreover it is unnecessary.
5. **What is needed is local (PROVED as a reduction).** L1′ and the Hilbert–Schmidt
   conclusion are equivalent to κ_p := F^{−1}r_p ∈ L²(−2T,2T), which I call (E′_loc). I reduce it
   (Theorem C) to a microlocal hypothesis (M) about the shape of r_p at high frequency. If (M)
   holds, the first-order oscillating term is C^0 on (−2T,2T) by non-stationary phase,
   and the monotone 1/|s| term gives a logarithmic singularity in L².
6. **Corollary (CONDITIONAL on (M)).** For S = {∞,p} and T < ½ log(next prime), R'_S = E_S −
   Son_S is Hilbert–Schmidt on L²(I_T). δε_p is **not** continuous in general: the 1/|s| part
   produces a log singularity at t = 0. L1 in the strong form is expected false; L1′ is expected
   true. **Everything beyond the reduction is proved only in the two-edge model with fixed
   L.** (M) is the only missing estimate and it contains no primes.
7. R183_021's (CF-S) (R183_025's Cor 3.2) in measure language: (CF-S) ⟺ μ_D → a (flat
   density). What the model predicts is μ_D = ρ_E + O(1/|s|) + (position oscillation L(s)), i.e.
   the Szegő density a(1−ε²)/|m|². There is no atom at ±ka with fixed k. This is OPEN in the
   true Sonin space, and, in the model, PROVED-in-model.

---

## 1. Conventions and two general lemmas

L²(R)^{ev} ≅ L²(R_+^*, d^*x), t = log x. ϑ(ρ) is the regular representation, ϑ(f) = ∫f(ρ)ϑ(ρ)d^*ρ.
In t, ϑ(f) is convolution with kernel f(e^{t−t'}) dt', and its diagonal equals f(1). F is the even unitary
Fourier transform, with Fϑ(ρ)F^{−1} = ϑ(ρ^{−1}) (CC, proof of (77)). P_1 = 1_{|x|≤1}, P := 1 − P_1,
1_{|y|<b} on the Fourier side, P̂_b := F^{−1}(1 − 1_{|y|<b})F, so that S(1,b) = ran P ∩ ran P̂_b
(Def 4.4, (72), CITED).

**Lemma 1.1 (density of a positive form; PROVED from Bochner–Schwartz, CITED).** Let X ≥ 0
be bounded such that ϑ(g)Xϑ(g)^* is trace class for every g ∈ C_c^∞. Then there exists a unique
positive tempered measure μ_X on R_s with ⟨X⟩_h = (1/2π)∫|φ|² dμ_X. For X = X_1 − X_2 of this class,
μ_X := μ_{X_1} − μ_{X_2} is a tempered distribution.
*Proof.* f ↦ Tr(ϑ(f)X) is linear and continuous on C_c^∞, and is ≥ 0 at f = g∗g^*, i.e. of positive
type. Apply Bochner–Schwartz. ∎

**Lemma 1.2 (trace part = L¹ density; PROVED).** If A is trace class, then
κ_A(ρ) := Tr(ϑ(ρ)A) is continuous and bounded by ‖A‖₁, Tr(ϑ(f)A) = ∫ f κ_A d^*ρ, and the Mellin
transform of κ_A is a function r_A ∈ L¹(ds) ∩ C_0 with ‖r_A‖_{L¹} ≤ 2π‖A‖₁.
*Proof.* A = Σ σ_j |u_j⟩⟨v_j| with Σσ_j = ‖A‖₁. Then κ_A = Σσ_j⟨v_j|ϑ(ρ)u_j⟩, which converges
uniformly. The transform of each term is (up to 2π) \overline{v̂_j}û_j, with
‖v̂_j û_j‖_{L¹} ≤ ‖v_j‖‖u_j‖ = 1 by Cauchy–Schwarz and Plancherel. ∎

This lemma is the rigorous form of the strategy "r = Σ w_n a_n b_n with summable weights": it works
**exactly on the trace part**. Correction to the formulation: the ξ_n are supported on
|x| ≤ 1, i.e. on the half-line t ≤ 0. Their Mellin transform is holomorphic on a half-plane and
**not** entire of exponential type. Since ξ_n is smooth up to the boundary, ξ̂_n(s) = ξ_n(1)/(½+is) + O(|s|^{−2}), and
this suffices.

---

## 2. Theorem A: the scaling law (Λ) (PROVED)

**Theorem A.** Let 0 < b ≤ 1, L_b := {b ≤ |y| < 1} and X_b := F^{−1}1_{L_b}F. For
f ∈ C_c^∞(R_+^*), the operator ϑ(f)(Π_{S(1,b)} − Π_{S(1,1)}) is trace class and

    Tr ϑ(f)(Π_{S(1,b)} − Π_{S(1,1)}) = log(1/b)·f(1) + ∫ f(ρ) ε'_b(ρ) d^*ρ,

where

    ε'_b(ρ) = −Tr(ϑ(ρ)[P_1X_b + X_bP_1 − P_1X_bP_1])
              − Σ_n μ_n^{(b)} ⟨ζ_n^{(b)}|ϑ(ρ)ζ_n^{(b)}⟩ + Σ_n μ_n^{(1)} ⟨ζ_n|ϑ(ρ)ζ_n⟩.

Here μ_n^{(b)} = λ_b(n)² are the eigenvalues of the time-frequency concentration operator
P_1 F^{−1}1_{|y|<b}F P_1 on L²(R)^{ev} (product-b prolates). The ζ_n^{(b)} are CC's (76)
eigenvectors for the pair (P, P̂_b), and μ^{(1)}, ζ_n are CC's. ε'_b is continuous,
|ε'_b| ≤ 3C₀ + 4b + 4 with C₀ := 2cosh(2π), and its Mellin density is in L¹(ds) with the same
bound (multiplied by 2π). With b = 1/p, log(1/b) = a: it is R183_025's (3.1) term a·c_h(0).

*Proof.*
(i) *Two-projection decomposition.* For the pair (P_1, Q_b), with Q_b := 1 − P̂_b, the
non-generic intersections are trivial except ker ∩ ker. ran P_1 ∩ ran Q_b = 0, because a
function supported on |x| ≤ 1 with Fourier transform on |y| ≤ b is zero (Paley–Wiener).
ran P_1 ∩ ker Q_b = 0, because Ff is entire and vanishes on an interval. ker P_1 ∩ ran Q_b = 0,
because f is entire and vanishes on |x| < 1. ker P_1 ∩ ker Q_b = S(1,b). On the generic part, Halmos's
normal form P_1 = diag(1,0), Q_b = [[c²,cs],[cs,s²]] gives P = diag(0,1), P̂_b = [[s²,−cs],[−cs,c²]], hence
PP̂_bP = diag(0,c²) and P_1Q_bP_1 = diag(c²,0). Hence PP̂_bP and P_1Q_bP_1 have the same
eigenvalues μ_n^{(b)} ∈ (0,1) on the generic part, and

    PP̂_bP = Π_{S(1,b)} + Σ_n μ_n^{(b)} |ζ_n^{(b)}⟩⟨ζ_n^{(b)}|.

This is CC (81)/(90) with general b; CC's Prop 4.5 proof does not use b = 1. Also
Σμ_n^{(b)} = Tr(P_1Q_bP_1) ≤ ∫_{−1}^{1}∫_{−b}^{b}dy dx = 4b. For b = 1 this recovers CC's footnote 7:
the sum, including odd ones, is 4.

(ii) *The difference.* P̂_b − P̂_1 = X_b ≥ 0. Subtracting (i) for b and for 1:

    Π_{S(1,b)} − Π_{S(1,1)} = P X_b P − Σμ^{(b)}|ζ^{(b)}⟩⟨ζ^{(b)}| + Σμ^{(1)}|ζ⟩⟨ζ|.

The two sums are trace class, with norm ≤ 4b and ≤ 4, and Lemma 1.2 turns them into the two
last pieces of ε'_b.

(iii) *P X_b P.* Write P X_b P = X_b − P_1X_b − X_bP_1 + P_1X_bP_1.
* The operator B := P_1F^{−1}1_{L_b} has kernel 2cos(2πxy) on the compact rectangle
  [−1,1] × L_b. Expanding cos in a Taylor series gives a sum of rank-one operators
  x^{2j} ⊗ y^{2j} with norms ≤ (2π)^{2j}·2/(2j)!. Hence ‖B‖₁ ≤ C₀, uniformly in b. Thus
  P_1X_b = B(1_{L_b}F), X_bP_1 = (F^{−1}1_{L_b})B^* and P_1X_bP_1 = BB^* are trace class, and
  Lemma 1.2 turns them into the first piece of ε'_b.
* ϑ(f)X_b = F^{−1}ϑ(f̃)1_{L_b}F, with f̃(ρ) = f(ρ^{−1}). In t, ϑ(f̃)1_{L_b} is convolution by a
  compactly supported kernel, followed by restriction to an interval of length log(1/b). By
  Dixmier–Malliavin, f̃ = Σ_i f_i ∗ g_i with f_i, g_i ∈ C_c^∞, and each term factors as a
  product of two compactly-kerneled Hilbert–Schmidt operators. Hence it is trace class, and its trace is the
  integral of the diagonal: f̃(1)·log(1/b) = f(1)·log(1/b).

(iv) Continuity of ε'_b and the L¹ bound follow from Lemma 1.2. The total bound is
3C₀ + 4b + 4. ∎

**Scaling law.** Dilation δ_c f(x) = c^{−1/2}f(x/c) commutes with ϑ(f). It satisfies
δ_c P_α δ_c^{−1} = P_{cα} and δ_c P̂_β δ_c^{−1} = P̂_{β/c}. Hence S(α,β) ≅ S(cα, β/c) via
a unitary commuting with ϑ, and all weighted traces depend only on the product αβ. Thus
S(1,1/p) ≅ S(p^{−1/2},p^{−1/2}), which is R183_025's S(λ,λ) form, λ = p^{−1/2}. It **cannot** be
reduced to λ = 1: the invariant is b = λ², and the prolates involved are those of time-frequency
product b = 1/p. Window T enters only through supp f ⊂ [e^{−2T},e^{2T}].
Consistency with (43): the term 2log(1/λ)f(1) with λ = b^{1/2} is log(1/b)f(1) = a f(1). (PROVED)

With this, R183_025's identity (3.1) is **PROVED** without hypothesis (Λ): (3.1) is
unconditional as an identity of distributions.

---

## 3. (E′): what is proved, what fails, and what is actually needed

### 3.1 Exact structure of r_p (PROVED)

R_edge = F^{−1}Π_EF − Π_D is a difference of two projections. ⟨F^{−1}Π_EF⟩_h is finite
(R183_025 §3), and ⟨Π_D⟩_h is finite because (1.1) is a difference of finite quantities, by
Theorem A and the finiteness of Son_S − Son_∞. By Lemma 1.1:

    r_p = ρ_E − μ_D,   ρ_E(s) = a(1 + 2Σ_{k≥1}ε^k cos(ksa)) = a(1−ε²)/|m(s)|²,   μ_D ≥ 0.

**Proposition 3.1 (PROVED).**
(a) r_p is a tempered distribution, and identity (3.1) holds for every h ∈ C_c^∞(I_T) with no
hypothesis on r_p. **Neither L^∞ nor polynomial growth is needed for the identity.**
(b) r_p ≤ a(1+ε)/(1−ε) as measures.
(c) r_p ≥ ρ_E − μ_{K'} + |m|²μ_K/(1+ε)² as measures.
*Proof of (c).* B := 1 − ετ is ϑ-equivariant, with ‖B‖ ≤ 1+ε. BΠ_KB^* has range BK and norm
≤ (1+ε)², so BΠ_KB^* ≤ (1+ε)²Π_{BK}. Since CB = ϑ(g') with Mellin transform φ·m, one has
μ_{BΠ_KB^*} = |m|²μ_K. Hence μ_{BK} ≥ |m|²μ_K/(1+ε)² and μ_D = μ_{K'} − μ_{BK}. ∎

(c) only gives a lower bound of logarithmic size on average, because μ_K and μ_{K'} ~ θ'(s)/π (CC
(83)). **The bound r_p ≥ −C, i.e. μ_D ≤ C, remains OPEN.** It is the half of L^∞ that is missing.

### 3.2 Exact decomposition of the overlap: the prolates are harmless (PROVED)

Γ := P_EFΠ_{K'}F^{−1}P_E = 1 − Y on E (R183_025 §4). Let v ∈ V := F^{−1}E. Since E lives on
|y| ≥ 1/p, one has P̂_bv = v with b = 1/p. From Theorem A(i), Π_{K'} = PP̂_bP − Σμ^{(b)}|ζ^{(b)}⟩⟨ζ^{(b)}|,
and a direct computation gives ‖v‖² − ⟨v,PP̂_bPv⟩ = ‖P_1v‖² + ‖Q_bP_1v‖². Hence, exactly,

    Y = Y_0 + Y_pro,
    Y_0   := P_E Q P_E,   Q := F P_1 F^{−1}   (Paley–Wiener projection PW_1 in the variable y),
    Y_pro := P_E F [ Σ_n μ_n^{(b)} ( |ξ_n^{(b)}⟩⟨ξ_n^{(b)}| + |ζ_n^{(b)}⟩⟨ζ_n^{(b)}| ) ] F^{−1} P_E,

where P_1Q_bP_1 = Σμ^{(b)}|ξ^{(b)}⟩⟨ξ^{(b)}|.

**Proposition 3.2 (PROVED).** ‖Y_pro‖₁ ≤ 2Σμ_n^{(b)} ≤ 8/p. Every contribution of Y_pro to r_p
that is linear in Y is, by Lemma 1.2, a density in L¹ ∩ C_0. The n = 0 contribution is
μ_0^{(b)} times a combination of |ξ̂_0^{(b)}(s)|² and |ζ̂_0^{(b)}(s)|² (weighted by ρ_E). Since
ξ̂_0(s) = ξ_0(1)/(½+is) + O(s^{−2}), that contribution is **O(|s|^{−2})**.

**Consequence.** The overlap PP̂P that R183_027 flags, i.e. the prolate structure, is **not** the
origin of r_p's tail. Y_0 contains no prolates: it measures how much of the geometric layer
e_u = Σε^kτ^ku is band-limited on |x| ≤ 1. It is not trace class, because each layer k contributes O(1) in
HS (R183_025 §4). The layers k with p^k ≳ |s|/2π are almost entirely within PW_1. In Mellin, Q is the
Hardy projection conjugated by the gamma phase e^{2iθ(s)} and reflected. If θ is linearized at a
frequency S, Q becomes the hard cutoff at t = L(S) = 2θ'(S). That is the two-edge model
with L = L(S). (The reduction to Y_0 of Γ^{−1}'s nonlinear terms further requires that Γ be
boundedly invertible at high frequency; see (M).)

### 3.3 Exact density of the two-edge model with fixed L (PROVED + control)

**Proposition 3.3.** In R183_025 Thm 2's model (K = L²[0,L], K' = L²[0,L+a]), let
N(y) := ⌊y/a⌋ for y in the layer [L,L+a), z := εe^{isa}, and q_y := ε^{N(y)+1}. D_L's spectral
density is

    ρ_{D_L}(s) = ∫_L^{L+a} (1−ε²) |1 − z^{N(y)+1}|² / ( |m(s)|² (1 − q_y²) ) dy,

and, with ψ_y := (N(y)+1)sa,

    r^{mod}(s) = ρ_E − ρ_{D_L} = ((1−ε²)/|m|²) ∫_L^{L+a} (2q_y cos ψ_y − 2q_y²)/(1 − q_y²) dy.

*Proof.* By R183_025 Thm 2, D_L is formed by the truncated geometric series
v = Σ_{k≤N(y)} ε^kτ^{−k}u, with u on the layer. Its norm has weight w(y) = (1−q_y²)/(1−ε²). The trace
against c = e^{isx} is ∫|Σ_{k≤N}z^k|²/w dy. The N = ∞ case is subtracted. ∎
Control (statement quadrature only, scratchpad): grid, L = 37, a = 5, ε = 2^{−1/2},
s = 0.83. Direct trace 1.096816442512135 versus formula 1.09681644251214.

**Reading.** r^{mod} has two parts:
* **first-order oscillating:** ≈ 2(1−ε²)|m|^{−2} q cos((N+1)sa), with amplitude ε^{L/a} = e^{−L/2}
  and position t = (N+1)a ∈ (L, L+2a];
* **monotone:** −2q² + …, of size e^{−L}.

Against c_h with supp c_h ⊂ (−2T,2T) and L > 2T, the oscillating part vanishes identically, because
c_h((N+1)a) = 0. That is why R183_025 Thm 2's error is O(ε^{2⌊L/a⌋}): it is correct **for c of
support < L**. As a density in s, however, the first order dominates.

### 3.4 Transfer to L(s) and verdict on (E′) (heuristic, labeled)

If L is replaced by L(s) = log(|s|/2π) (R183_025 §4), one obtains:
* oscillating amplitude ≍ e^{−L(s)/2} = (2π/|s|)^{1/2}, whose square ≍ 1/|s| **is not integrable**;
* monotone part ≍ 2π/|s|, which is in L² but not L¹.

Hence, **the heuristic r_p ≍ 1/|s| is correct only for the monotone part.** r_p ∈ L²(R,ds)
global (R183_025's (E′)) **is expected to be FALSE**, by a logarithmic margin. The heuristic is not
a proof, so the label is "expected false", not NO-GO. But global (E′) was never
necessary: only κ_p = F^{−1}r_p on (−2T,2T) is used.

### 3.5 What is needed for each consequence (PROVED as equivalences)

| Consequence | Necessary and sufficient condition | r_p ∈ ? |
|---|---|---|
| Identity (3.1) | none (tempered, Prop 3.1a) | nothing needed |
| R'_S Hilbert–Schmidt on L²(I_T) (L1′) | κ_p ∈ L²(−2T,2T) = **(E′_loc)** | global L² is enough, but not needed |
| δε_p continuous on [−2T,2T] (L1) | κ_p ∈ C[−2T,2T] | global L¹ is enough; expected false |

The HS ⟺ κ ∈ L²(−2T,2T) equivalence holds because R'_S's kernel on I_T × I_T is
ε_S(t−t'), and ∫∫_{I_T²}|ε_S(t−t')|² is comparable to ‖ε_S‖²_{L²(−2T,2T)}, with constants
depending on T.

**Hypothesis (M) (OPEN, with no primes).** There exist S_0 with L(S_0) > 2T + 3a and a decomposition
r_p = r_low + r_mono + r_osc such that:
(M1) r_low is a finite measure supported on |s| ≤ S_0;
(M2) |r_mono(s)| ≤ C(1+|s|)^{−1/2−δ} for some δ > 0 (the model gives exponent 1);
(M3) r_osc = Re(A(s)e^{iΦ(s)}) for |s| > S_0, with |A| ≤ C|s|^{−δ}, |A'| ≤ C|s|^{−1−δ},
     Φ' ≥ L(s) − 2a and |Φ''| ≤ C/|s| (the model gives δ = ½ and Φ ≈ sL(s)).

**Theorem C (PROVED, reduction).** (M) ⟹ (E′_loc). More precisely, κ_p = κ_low + κ_mono + κ_osc,
with κ_low continuous, κ_mono ∈ L²(R), and κ_osc continuous on [−2T,2T].
*Proof.* κ_low is the transform of a finite measure, hence continuous. κ_mono ∈ L² by
Plancherel, since (1+|s|)^{−1/2−δ} ∈ L². For κ_osc(t) = ∫_{|s|>S_0} A e^{i(Φ−st)}ds with
|t| ≤ 2T, one has Φ' − t ≥ L(s) − 2a − 2T ≥ a > 0. Integration by parts gives a boundary
term at S_0 plus ∫[A'/(Φ'−t) − AΦ''/(Φ'−t)²]e^{i(…)}ds. The integrand is bounded by
C|s|^{−1−δ}, uniformly in t, so the integral converges absolutely and uniformly. Hence
κ_osc is continuous (the conjugate is treated the same way with −Φ). ∎

**Corollary C′ (CONDITIONAL on (M)).** For S = {∞,p} and T < ½ log(the prime after p) (so that
Son_S and E_S see only prime p in the window):
(i) L1′: Son_S − Son_∞ = −2log p Σ_k p^{−k/2}Re c_h(k log p) + ∫c_h δε_p, with
    δε_p = ε'_{1/p} + κ_p ∈ L²(−2T,2T), where ε'_{1/p} is continuous by Theorem A;
(ii) R'_S = E_S − Son_S = −∫c_h ε_S is Hilbert–Schmidt on L²(I_T). R183_025's Cor 3.1 applies:
    R183_018 Thm 5.1's NO-GO does not reach the partition Son_S + R'_S, and n₋ below −δ is
    finite;
(iii) if r_mono ≍ 1/|s| as in the model, κ_mono has a logarithmic singularity at t = 0,
    δε_p is not continuous and L1 (strong form) fails. L1′ is the correct form.

If (M) holds, (CF-S) is false: r_p has no non-decaying part at frequencies ka, fixed k.
Then R183_021 Thm 3.4 becomes vacuous and there is no atom −log 2/√2 at ±log 2 (the question of
R183_028 §3.1). This is CONDITIONAL on (M).

**What is needed to prove (M).** A microlocal comparison is needed, with trace-norm remainders in
frequency windows |s| ∼ S, between Π_D (or Γ^{−1} restricted to those frequencies) and the
two-edge model with L = L(S). The linearization error of the gamma phase is θ''(S) ≍ 1/S on
windows of width ≍ 1/a. Also needed is that Γ be bounded below at high frequency;
at low frequency (|s| ≲ 2π/p) Γ is not bounded below, but that falls into r_low. It is a
pseudodifferential computation standard in spirit, not yet carried out. It contains no primes: p only
appears via a and ε.

---

## Status

| Statement | Label |
|---|---|
| Theorem A: (Λ), Tr ϑ(f)(Π_{S(1,b)}−Π_{S(1,1)}) = log(1/b)f(1)+∫fε'_b, ε'_b continuous, L¹ density | PROVED |
| Scaling law S(α,β) ≅ S(cα,β/c); invariant = product; window only via supp f | PROVED |
| R183_025's identity (3.1) | PROVED (now without (Λ) as hypothesis) |
| r_p = ρ_E − μ_D, ρ_E = a(1−ε²)/\|m\|², μ_D ≥ 0 tempered | PROVED |
| r_p ≤ a(1+ε)/(1−ε); identity valid without hypothesis | PROVED |
| r_p ≥ −C (μ_D ≤ C) | OPEN |
| Y = Y_0 + Y_pro exact; ‖Y_pro‖₁ ≤ 8/p; n=0 term is O(\|s\|^{−2}) | PROVED |
| Exact density of the two-edge model with fixed L (Prop 3.3) | PROVED (+ numerical control) |
| r_p ≍ 1/\|s\| | only the monotone part; heuristic |
| (E′): global r_p ∈ L²(R,ds) | expected FALSE (oscillating amplitude \|s\|^{−1/2}, heuristic); unnecessary |
| (E′_loc) ⟺ Hilbert–Schmidt R'_S | PROVED (equivalence) |
| Theorem C: (M) ⟹ (E′_loc) | PROVED |
| (M) | OPEN (the only missing estimate; no primes) |
| L1′ and R'_S HS for S={∞,p}, T<½log(next prime) | CONDITIONAL on (M) |
| strong L1 (continuous δε) | expected false (log singularity at t=0); CONDITIONAL |
| (CF-S) / atom at ±log 2 | expected false; CONDITIONAL on (M) |
| Positivity / N_T / row D | OPEN; not claimed |

## Review points

1. **Normalization of f(1) against c_h(0), and of d^*ρ against ds/2π.** R183_025's has been
   followed. The term log(1/b)f(1) is the trace of ϑ(f̃)1_{L_b}, with diagonal f(1) and length
   log(1/b) (Theorem A(iii)). It must be checked that CC's convention for ϑ(ρ) (ρ^{±1/2}) introduces
   no factor of 2 on L²(R)^{ev}.
2. **Theorem A(i).** Check the three trivial intersections and Halmos's form with P = 1−P_1,
   P̂_b = 1−Q_b. Also check that CC (81) uses the generic part of the pair (P_1,Q) and not of the
   pair (P_1,P̂).
3. **Proposition 3.2.** It is the identity ‖v‖² − ⟨v,PP̂_bPv⟩ = ‖P_1v‖² + ‖Q_bP_1v‖² for
   P̂_bv = v. It should be redone: P̂_bPv = v − P̂_bP_1v.
4. **The central point: the first order.** In Prop 3.3, the term 2q cos ψ is first order in
   q and, for c with no compact support, dominates over q². If one believes that
   R183_025's Thm 2 gives error ε^{2N} for every bounded c, note that bound uses c((N+1)a) = 0. This
   contradicts R183_025 §4's heuristic "r_p ≍ 1/|s|" on the oscillating part.
5. **Transfer L → L(s).** It is heuristic. The floor ⌊y/a⌋ makes the model's phase
   stepwise. In the true Sonin space a smoothed version is expected, which is (M3). If the real
   phase had stationary points with Φ' ∈ (−2T,2T) at high frequency, (M) would fail and content
   would appear within (−2T,2T): that is this route's falsifier.
6. **Γ at low frequency.** Γ is not bounded below when |s| ≲ 2π/p. It has been relegated to
   r_low (M1), which only requires that r_p be a finite measure on compacts, which holds by
   Lemma 1.1.
7. **No circularity.** Neither ζ nor zeros enter. Primes ≠ p are excluded by
   T < ½ log(next prime).

## Note (R183_032)

§3.5 and the corresponding row of Status reverse (Δ): under (M), (CF-S)
is false and F^{-1}[ρ_S − ρ_∞] **does** have the atom −log2·2^{-1/2} at
±log 2 (it is the exact prime term of R183_025's Thm 2; the atom-free
object is r_p/μ_D). Corrected reading: under (M), Son_S − Son_∞ = full
prime term + ∫c_h δε_p with δε_p ∈ L²_loc. MINOR: C₀ = 4cosh(2π);
1_{L'} is missing in Dixmier–Malliavin; Prop 3.2 only to first order.
