# R162_403 — G1.2: the Poisson–Chebyshev identity for the smooth-number comb

Round 4, mechanism G1.2.

Status: **NO-GO (PROVED), with three PROVED STEPS.** Gate 1 is not closed.

- PROVED STEP 1 (§2). With S_N replaced by the smooth comb Z_P, the exact identity is
  Z_P A_P 𝓕 = {X, E^{(P)}} − L_P^* E^{(P)}, where L_P runs over all prime powers of p ≤ P.
  **The divisor-hyperbola term vanishes identically.** H^{(P)} := L_P Z_P − K_P = 0, because
  Λ*1 = log holds exactly on the divisor-closed set of P-smooth integers. This step is Euler-specific.
- PROVED STEP 2 (§3). The exact defect. E^{(P)} = 𝓕Z_P^* − JZ_P = J·Δ_P(D), where Δ_P is the
  functional-equation defect of ζ_P. On P_T × L²(I_T) with P ≥ e^{2T}, its compression is
  **−P_T R_P 𝓕**, where R_P = Σ_{n not P-smooth} n^{−1/2}τ_{log n} is the rough comb (exact, by
  Poisson summation on the primitive class). It tends to 0 as P → ∞.
- PROVED STEP 3 (§4). The exact Gamma-coordinate expansion of ⟨Z_P𝓕F, g⟩ (§4.2). It has a polar
  layer on Re a = −½, of order π(P)+1 at a = −½, which carries the higher Tate moments
  ∫tᵏe^{t/2}F, k ≤ π(P). It also has a convergent Gamma series with multipliers γ_jζ_P(−2j).
  **Correction to the brief:** ζ_P(−2j) → 0 as P → ∞, super-exponentially, with sign (−1)^{π(P)}.
  This happens with no trivial zero: |ζ_P(−2j)| ≤ ζ(2j)e^{−2jθ(P)}. The quantity that does *not*
  converge to its ζ-value is the log channel: ζ_P'(−2j) → 0, whereas ζ'(−2j) ≠ 0.
- NO-GO (§5). The paired identity splits into an 𝓕-block and a J-block. **Each block is the single
  identity H^{(P)} = 0**, i.e. the logarithmic derivative ζ_P' = (ζ_P'/ζ_P)·ζ_P. Every channel cancels
  identically for every F and g: the value channel ζ_P(−2j), the log channel ζ_P'(−2j), the jet
  channel ζ_P(−2j)d_j^{(P)}, and the polar layer. No uncancelled term remains, with either
  coefficient ζ_P(−2j) or ζ_P'(−2j). Even taken separately, each of these channels has a P → ∞
  coefficient that is o(e^{−jθ(P)}). So none of them is comparable with c_{N,L}, which is fixed.

Notation follows Paper 46 §sec:firstcontact and R162_401. Write μ_F(a) = ∫e^{at}F and
K_F(a) = ∫e^{−at}F, so K_F(−a) = μ_F(a). Also a_j = 2j+½, s_j = 2j+1, γ_j = 2(−1)^j(2π)^{2j}/(2j)!,
and χ(s) = π^{s−½}Γ((1−s)/2)/Γ(s/2). Pairings are the real pairing ⟨h,g⟩ = ∫hg. 𝒮 = 𝒮(ℝ) is the
Schwartz core.

## 0. Corpus check (before building)

- **R162_202 / R162_301.** Z_P is the full-line inverse A_P(τ)^{−1} of the finite Euler history of
  R162_202 (2.1), written with left shifts. On the full line it is a bounded normal multiplier with
  symbol ζ_P(½ − iτ) and norm ζ_P(½). On H_T or I_T its compression is *not* the inverse of the
  compressed history. The discrepancy is the Brown–Halmos Hankel term of R162_301 Thm 1.1. This note
  works on the full line, before any compression except the final pairing, so it is disjoint from
  R162_301 §§3–5. The compressed object is not reopened.
- **R160 survey F21** (phase-64 E105/E109: "finite-S scalar Euler/Tate colligation … poles/zeros").
  This is the same polar line Re w = 0 of ζ_P that appears here as Re a = −½ (§4). **NG-F1**
  (smoothness, not multiplicativity, controls the localized sign) is consistent with §5: the only
  Euler-specific fact, H^{(P)} = 0, carries no F-information.
- **R162_401 §5 / R162_305 §4.** The jet channel ζ_P(−2j)d_j^{(P)} and the value channel are
  reproduced here with ζ_P in place of the renormalized ζ. They cancel exactly as there (§5).

## 1. The operators (PROVED)

For a finite prime bound P, put

    Z_P = Σ_{n P-smooth} n^{−1/2}τ_{log n},   K_P = Σ_{n P-smooth} (log n)n^{−1/2}τ_{log n},
    L_P = Σ_{p ≤ P, k ≥ 1} (log p) p^{−k/2}τ_{k log p},   A_P = 𝓜 − L_P − L_P^*,
    R_P = Σ_{n not P-smooth} n^{−1/2}τ_{log n}  (formal; used only on 𝓕 of primitive tests).

**Lemma 1.1.** (a) Z_P, K_P, L_P, L_P^*, Z_P^* are bounded on L²(ℝ) and map 𝒮 to 𝒮. Their norms
are ζ_P(½), −ζ_P'(½), −(ζ_P'/ζ_P)(½) and ζ_P(½) respectively.
(b) On e_a(t) = e^{at}, Re a < ½: Z_P e_a = ζ_P(½ − a)e_a, K_P e_a = −ζ_P'(½ − a)e_a,
L_P e_a = −(ζ_P'/ζ_P)(½ − a)e_a, and L_P^* e_a = −(ζ_P'/ζ_P)(½ + a)e_a (the last for Re a > −½).
(c) [X, Z_P] = −K_P on 𝒮.

*Proof.* (a) The coefficient sums Σ_{smooth} n^{−1/2} = Π_{p≤P}(1 − p^{−1/2})^{−1} and its log-weighted
version are finite, because only finitely many primes occur. Schwartz preservation: for g ∈ 𝒮 and
t → −∞, split the n-sum at n = e^{|t|/2}. The first part is ≤ ζ_P(½) sup_{u ≥ t/2}|g(u)| up to
polynomial weights, which is rapidly decreasing. The second is ≤ ‖g‖_∞ times the tail of a convergent
series in n^{−1/2} over smooth n > e^{|t|/2}. That tail is ≤ C_ε e^{−(¼−ε)|t|}(1+|t|)^{π(P)}. For
t → +∞ every argument t + log n → +∞. Derivatives commute with the shifts. L_P^* is handled the same
way, with the roles of ±∞ exchanged. (b) τ_{log n}e_a = n^a e_a. (c)
[X, τ_c]h(t) = t h(t+c) − (t+c)h(t+c) = −cτ_c h. The series converge in 𝒮. ∎

**Lemma 1.2 (exact Chebyshev identity on smooth numbers).** K_P = L_P Z_P = Z_P L_P. Equivalently,
H^{(P)} := L_P Z_P − K_P = 0.

*Proof.* The coefficient of k^{−1/2}τ_{log k} in L_PZ_P is Σ_{dm=k, d a power of p≤P, m P-smooth} Λ(d).
It is nonzero only for P-smooth k. Every divisor of a P-smooth k is P-smooth, so the sum equals
Σ_{d|k} Λ(d) = log k. Everything commutes. (Symbol form: −ζ_P' = (−ζ_P'/ζ_P)·ζ_P.) ∎

This is the exact content of "Λ*1_P = log on P-smooth numbers". In thm:PCfinite the corresponding
H_{M,N} is a nonzero remainder supported at k > N. Here it is zero.

## 2. The exact smooth-comb PC identity (PROVED)

Put E^{(P)} := Z_P𝓕 − JZ_P.

**Theorem 2.1.** On 𝒮,

    Z_P A_P 𝓕 = {X, E^{(P)}} − L_P^* E^{(P)}.                                        (PC_P)

More precisely, for every P and without using Lemma 1.2,

    Z_P A_P 𝓕 = {X, E^{(P)}} − L_P^* E^{(P)} − J H^{(P)} − H^{(P)} 𝓕,                  (2.1)

and Lemma 1.2 removes the last two terms.

*Proof.* The proof of thm:PCfinite uses only [X, S] = −K, M = X + 𝓕X𝓕, 𝓕² = 1, JX = −XJ and
JL = L^*J, and it applies verbatim with S = Z_P. Explicitly:
Z_PM𝓕 = Z_PX𝓕 + Z_P𝓕X = XZ_P𝓕 + K_P𝓕 + Z_P𝓕X. Substituting Z_P𝓕 = E^{(P)} + JZ_P gives
{X, E^{(P)}} + XJZ_P + JZ_PX + K_P𝓕, and XJZ_P + JZ_PX = J[Z_P, X] = JK_P. So
Z_PM𝓕 = JK_P + K_P𝓕 + {X, E^{(P)}}. Insert K_P = L_PZ_P − H^{(P)}, use JL_PZ_P = L_P^*JZ_P
= L_P^*(Z_P𝓕 − E^{(P)}), and subtract Z_P(L_P + L_P^*)𝓕 = L_PZ_P𝓕 + L_P^*Z_P𝓕. All operators
map 𝒮 → 𝒮 (Lemma 1.1a, and 𝓕𝒮 = 𝒮). ∎

**Remark 2.2 (the two blocks).** Group (2.1) by orientation. The J-block of RHS − LHS is
J(XZ_P − Z_PX) + JL_PZ_P = J(L_PZ_P − K_P) = JH^{(P)}. The 𝓕-block is
[Z_P, X]𝓕 − Z_PL_P𝓕 + (terms cancelling pairwise) = −H^{(P)}𝓕. So (PC_P) is **equivalent** to the
pair of identities JH^{(P)} = 0 and H^{(P)}𝓕 = 0, both of which are Lemma 1.2. In R162_401 there were
two cancellations: the commutator, and the Λ-channel together with the hyperbola remainder. Here they
coincide in one scalar identity of meromorphic functions, ζ_P' = (ζ_P'/ζ_P)ζ_P.

## 3. The exact defect (PROVED)

**Proposition 3.1.** (a) As operators on 𝒮, Z_P𝓕 = 𝓕Z_P^*, hence E^{(P)} = 𝓕Z_P^* − JZ_P = JΔ_P(D),
with

    Δ_P(τ) = u_∞(−τ) ζ_P(½ + iτ) − ζ_P(½ − iτ),

a bounded continuous multiplier. It is the functional-equation defect of ζ_P on the critical line,
and it would vanish identically for ζ, since u_∞ is χ on the line.
(b) Let h ∈ C_c^∞(I_T) and N ≥ e^{2T}. Then, pointwise,

    S_∞𝓕h − JS_∞h = −μ_h(½) e_{½}      (Poisson summation; the series converge absolutely).

(c) Let F ∈ C_c^∞(I_T) with μ_F(½) = 0, let g ∈ L²(I_T), and let P ≥ e^{2T}. Then

    ⟨E^{(P)}F, g⟩ = −⟨R_P𝓕F, g⟩ = −Σ_{n not P-smooth} n^{−1/2} ∫ 𝓕F(t + log n) g(t) dt,

and |⟨E^{(P)}F, g⟩| ≤ C_k(F)‖g‖_1 Σ_{n>P} n^{−1/2}(ne^{−T})^{½−k} → 0 as P → ∞, for every k.
The same holds with F replaced by XF when μ_g(½) = 0. In general the Tate term −μ_h(½)μ_g(½)
appears, and it vanishes on primitive pairs.

*Proof.* (a) Jz(D)J = z(−D), and Z_P^* has symbol z(−τ) because the coefficients are real. Hence
𝓕Z_P^* = u_∞(D)Jz(−D) = u_∞(D)z(D)J = Z_P𝓕. Next, E^{(P)} = J[Jz(D)u_∞(D)J − z(D)] =
J[z(−D)u_∞(−D) − z(D)], and z(τ) = ζ_P(½ − iτ). (b) Write h(t) = e^{t/2}f(e^t) with f even,
Schwartz and vanishing on |y| < e^{−T}. Then S_∞𝓕h(t) = e^{t/2}Σ_{n≥1} f̂(ne^t) and
JS_∞h(t) = e^{−t/2}Σ_{n≥1} f(ne^{−t}). Poisson summation Σ_ℤ f̂(nx) = x^{−1}Σ_ℤ f(n/x), with
x = e^t, f(0) = 0 and f̂(0) = 2∫_0^∞ f = 2μ_h(½), gives the claim. (c) Put Z_P = S_∞ − R_P. Then
E^{(P)} = (S_∞𝓕 − JS_∞) − R_P𝓕 + JR_P. The first term vanishes by (b). The last pairs to 0,
because every non-P-smooth n exceeds P ≥ e^{2T}, so JR_PF is supported in [log n − T, ∞) ⊂ [T, ∞).
For the bound, 𝓕F(u) = e^{u/2}f̂(e^u) with f̂ Schwartz. When t ∈ I_T we have u = t + log n ≥ log n − T,
so |𝓕F(u)| ≤ C_k e^{u(½−k)}. ∎

So the correct exact replacement for E_N is the rough comb applied to 𝓕F. It samples only the
**Schwartz (right) tail** of 𝓕F, at arguments ≥ log P − T. It has no additive Poisson partner. Its
compressed pairing vanishes as P → ∞, just as ⟨E_NF, g⟩ = −⟨S_{>N}𝓕F, g⟩ does as N → ∞ (the same
proof with R_P replaced by S_{>N}).

## 4. Gamma coordinates of the smooth comb (PROVED)

**Lemma 4.1 (Tate).** For F ∈ C_c^∞(ℝ), the two-sided Laplace transform
L_{𝓕F}(a) := ∫e^{at}𝓕F(t)dt equals χ(½ − a)K_F(a), meromorphically in a. Its poles are at
a = −a_j (j ≥ 0), with residue γ_jμ_F(a_j).

*Proof.* L_{𝓕F}(a) = ∫_0^∞ y^{a−½}f̂(y)dy. Tate's local functional equation for even f
(0 < Re u < 1, u = a + ½) gives π^{−a}Γ((½+a)/2)/Γ((½−a)/2)·∫_0^∞ y^{−a−½}f(y)dy =
χ(½ − a)K_F(a). Continue meromorphically. Residue: Res_{w=−j}Γ(w) = (−1)^j/j! with w = (½+a)/2,
and Γ(j+½) = (2j)!√π/(4^j j!), so the residue is 2(−1)^jπ^{2j+½}/(j!Γ(j+½)) = γ_j. The value is
μ_F(a_j) = K_F(−a_j). (Check at a = 0: χ(½) = 1, which is self-duality.) ∎

**Theorem 4.2 (exact expansion).** Let F, g ∈ C_c^∞(I_T). Then

    ⟨Z_P𝓕F, g⟩ = Pol_P(F, g) + Σ_{j≥1} γ_j ζ_P(−2j) μ_F(a_j) μ_g(a_j)          (4.1)

with the following ingredients.
(i) The Gamma series converges absolutely: |ζ_P(−2j)| = Π_{p≤P}(p^{2j} − 1)^{−1} and
|μ(a_j)| ≤ √(2T)e^{a_jT}‖·‖.
(ii) Pol_P is the sum of the residues of ζ_P(½+a)χ(½−a)K_F(a)K_g(a) on the line Re a = −½. It is
taken as the limit of symmetric partial sums over heights τ_n → ∞ chosen at distance ≥ c_P from the
pole ordinates. The poles are:
  - a pole of order π(P) + 1 at a = −½ (π(P) from ζ_P, one from Γ). It pairs the jets
    ∂^k_a[K_F K_g](−½), which are the higher Tate moments ∫tᵏe^{t/2}F and ∫tᵏe^{t/2}g for
    k ≤ π(P). Only k = 0 vanishes on P_T.
  - simple poles at a = −½ + 2πik/log p, for p ≤ P and k ≠ 0. They are simple and distinct, because
    log p/log q ∉ ℚ.
(iii) The same expansion holds for K_P𝓕, L_PZ_P𝓕 and L_P^*Z_P𝓕, with ζ_P(½+a) replaced by
−ζ_P'(½+a), (−ζ_P'/ζ_P)(½+a)ζ_P(½+a) and (−ζ_P'/ζ_P)(½−a)ζ_P(½+a) respectively. At a = −a_j these
are −ζ_P'(−2j), the same number, and ζ_P(−2j)d_j^{(P)}, where d_j^{(P)} = −(ζ_P'/ζ_P)(s_j)
= Σ_{p≤P,k} log p·p^{−ks_j} is the smooth collar weight.

*Proof.* L_{Z_P𝓕F}(a) = Σ_{smooth} n^{−½−a}L_{𝓕F}(a) = ζ_P(½+a)χ(½−a)K_F(a) for Re a > −½, where
Z_P𝓕F is O(e^{t/2}|t|^{π(P)}) at −∞. Parseval for the two-sided Laplace transform gives
⟨Z_P𝓕F, g⟩ = (2πi)^{−1}∫_{(c)} ζ_P(½+a)χ(½−a)K_F(a)K_g(a)da for any c ∈ (−½, ½). Now shift to
Re a = −σ_J, σ_J = a_J + 1. The horizontal segments at the heights τ_n tend to 0: on them |ζ_P| is
bounded (finitely many arithmetic progressions of poles, and a lower bound for |1 − p^{−w}| at
distance ≥ c_P from them); χ grows polynomially; and K_FK_g = O_k(|a|^{−k}) by integrating by parts
over I_T. For the remainder on Re a = −σ_J, use |ζ_P(½−σ+iτ)| ≤ Π(p^{σ−½} − 1)^{−1}, Stirling at
distance 1 from the Γ-poles (|χ(½+σ+iτ)| ≍ (|a|/2π)^{−σ}, uniformly), and
|K_F(a)K_g(a)| ≤ C e^{2σT}|a|^{−2}. The remainder is then
≤ C′(2πe^{2T}/σ_J)^{σ_J}Π(p^{σ_J−½} − 1)^{−1} → 0 as J → ∞. The residues at −a_j come from Lemma 4.1,
since ζ_P is holomorphic there with value ζ_P(½ − a_j) = ζ_P(−2j). (iii) is the same computation with
the symbols of Lemma 1.1(b). ∎

**Proposition 4.3 (the P → ∞ behaviour; this corrects the brief).** For each j ≥ 1:

    ζ_P(−2j) = (−1)^{π(P)} Π_{p≤P}(p^{2j} − 1)^{−1},     0 < |ζ_P(−2j)| ≤ ζ(2j) e^{−2jθ(P)},
    ζ_P'(−2j) = ζ_P(−2j)·Σ_{p≤P} log p·p^{2j}/(p^{2j} − 1),   |ζ_P'(−2j)| ≤ 2ζ(2j) θ(P) e^{−2jθ(P)}.

Hence ζ_P(−2j) → 0 = ζ(−2j), but not through a zero: it is a product of factors each of modulus
≤ 1/3, and the sign oscillates. Moreover ζ_P'(−2j) → 0 ≠ ζ'(−2j) = (−1)^j(2j)!ζ(s_j)/(2(2π)^{2j}),
and ζ_P(−2j)d_j^{(P)} → 0 ≠ ζ'(s_j)γ_j^{−1}. So

    γ_j ζ_P'(−2j) → 0,  whereas  γ_j ζ'(−2j) = ζ(s_j)   (R162_401 (2.1)).

*Proof.* The product formula is immediate, and |1 − p^{2j}|^{−1} = p^{−2j}(1 − p^{−2j})^{−1}. The
log-derivative formula is Lemma 1.1(b). Finally θ(P) = Σ_{p≤P} log p → ∞. ∎

Interpretation (remark, not used). ζ_P(w) → ζ(w) only for Re w > 1. The smooth comb carries no
trivial zeros, and for that reason it also carries no functional equation. The residue data
ζ(s_m)K_F(a_m), which R162_401 found in the renormalized log channel, arises there *only* through the
functional equation, γ_jζ'(−2j) = ζ(s_j). For Z_P the Gamma lattice sees super-exponentially small
numbers, and all the mass migrates into the polar layer Pol_P on Re a = −½. There the poles become
dense as P → ∞: this is the natural-boundary behaviour of F21 in the R160 survey.

## 5. Pairing at first contact: NO-GO (PROVED)

**Theorem 5.1.** Let P ≥ e^{2T}, F ∈ P_T ∩ C_c^∞(I_T) and g ∈ L²(I_T) (in particular g = ΠS_LF,
by density and continuity of every term in g). Pair (PC_P) with F ⊗ g. Then:
(a) The paired identity is equivalent to the pair ⟨JH^{(P)}F, g⟩ = 0 = ⟨H^{(P)}𝓕F, g⟩ (Remark 2.2).
Both hold because H^{(P)} = 0, for **every** F and g, with no use of H_TF = 0, λ = 0 or the
minimality of T_*.
(b) In the expansion of Theorem 4.2, each channel cancels separately:
  - the value channel γ_jζ_P(−2j)μ_Fμ_g, between XZ_P𝓕 ⊂ Z_PX𝓕 and {X, E^{(P)}};
  - the log channel −γ_jζ_P'(−2j)μ_Fμ_g, between K_P𝓕 (from Z_PX𝓕 = XZ_P𝓕 + K_P𝓕) and L_PZ_P𝓕,
    by Lemma 1.2 at a = −a_j, i.e. −ζ_P'(−2j) = (−ζ_P'/ζ_P)(−2j)ζ_P(−2j);
  - the jet channel γ_jζ_P(−2j)d_j^{(P)}μ_Fμ_g, between Z_PL_P^*𝓕 and L_P^*Z_P𝓕 (translations commute);
  - the polar layer Pol_P, term by term, since it is built from the same symbols at a different set
    of residues.
(c) No term Σ_j c_j(P)K_F(a_j)K_g(a_j) with c_j(P) ∈ span{ζ_P(−2j), ζ_P'(−2j), ζ_P(−2j)d_j^{(P)}}
survives. Taken separately, before cancellation, every such coefficient is O(θ(P)e^{−2jθ(P)}) by
Prop. 4.3. Meanwhile c_{N,L} = ⟨R_LF, D_{N,L}R_LF⟩ does not depend on P, and so neither does
d^{(P)}_m → d_m ≤ q_0. So no P-dependent term of the pairing can be comparable with c_{N,L}, and none
can force R_LF = 0 as P → ∞.
(d) By Prop. 3.1(c) the defect pairing ⟨E^{(P)}F, ·⟩ tends to 0 as P → ∞. So (PC_P) degenerates, in
compressed form, to 0 = 0 plus the Tate endpoints. Those vanish on primitive pairs, or contribute
μ_{XF}(½)μ_g(½) = 0 when g ∈ P_T.

*Proof.* (a) Remark 2.2. (b) Pair each block of Remark 2.2 with F ⊗ g through Parseval (Theorem 4.2
proof). Each block is an integral over Re a = c of [symbol identity]·χ(½−a)K_F(a)K_g(a) whose
bracket is identically zero. So its residues at every pole are zero, channel by channel. (c) is
Prop. 4.3. For (d) use Prop. 3.1(c) for E^{(P)}F, E^{(P)}XF and ⟨XE^{(P)}F, g⟩ = ⟨E^{(P)}F, Xg⟩; and
Xg ∈ L²(I_T). ∎

**Theorem 5.2 (answer to G1.2).** The truncated Euler comb removes the trivial zeros from the value
multiplier, so ζ_P(−2j) ≠ 0. It also makes the Chebyshev step exact, so H^{(P)} = 0. For exactly
this reason the PC identity becomes the scalar tautology ζ_P' = (ζ_P'/ζ_P)ζ_P, tensored with the two
orientations 𝓕 and J. The first-contact pairing adds nothing: the combined system {(PC_P) paired with
F ⊗ ΠS_LF, eq:Qbalance} is eq:Qbalance alone. As in R162_401 §6, forcing R_LF = 0 from it is
equivalent to the conclusion (eq:equivgate). There is also no P → ∞ route: the Gamma-channel
coefficients vanish super-exponentially, the defect vanishes, and ζ(s_m) cannot be recovered on the
lattice, since the functional equation is absent.

## 6. Falsifiers

- **F1 (λ = 0).** Theorem 5.1(a) holds for every F, including eigenvectors with λ > 0 and R_LF ≠ 0.
  An identity valid for all sources cannot force R_LF = 0. This is the NO-GO in falsifier form.
- **F2.** (PC_P) is linear. Its square is invariant under A_P ↦ −A_P, and it orients nothing.
- **F3 (finite modifications).** Replace Λ by a = Λ + η_0. Then H^{(P),a} = Σ_{k smooth}
  (η_0*1_P)(k)k^{−1/2}τ_{log k} ≠ 0, so the exact identity (PC_P) is Λ-specific. This is the only
  Euler-specific fact produced. It is a coefficient identity, though, and never an F-constraint: the
  modified identity acquires the Ward defect −JH^{a} − H^{a}𝓕, which is linear in η_0 and changes
  sign under η_0 → −η_0 (R162_205, R162_305 Thm 3.1). **Davenport–Heilbronn.** DH has no Euler
  factorization, and its coefficients restricted to smooth numbers give no product. The analogue of
  Lemma 1.2 therefore fails: H^{DH,P} ≠ 0 for every P. The smooth-comb construction does not exist
  for DH. It passes F3 as a construction, but it carries no closing step that could fail.
- **F4.** No linear limit is used for the conclusion. The P → ∞ limit kills every channel (Prop. 4.3,
  Prop. 3.1c) and leaves 0 = 0, consistent with F4.

## 7. Consequences and next sub-lemma

- The smooth comb breaks the trivial-zero (value) cancellation of E1 at finite P. It breaks it only
  by also making the Chebyshev hyperbola exact, which merges the two cancellations of R162_401 into
  one symbol identity. **Structural lesson (PROVED in the form of Remark 2.2 and Thm 5.1b):** any
  identity in the commutative algebra generated by X, J and Dirichlet-series multipliers z(D)
  (𝓕 = u_∞(D)J included) is equivalent to identities between meromorphic symbols. Such identities
  hold for every source, so they cannot pass F1. Neither the integer comb, nor the renormalized comb,
  nor the smooth comb escapes this.
- The only F-dependent data exposed by Z_P that is *not* killed on P_T is the order-(π(P)+1) polar
  layer at a = −½, which pairs the higher Tate moments ∫tᵏe^{t/2}F, 1 ≤ k ≤ π(P). This data is
  outside the Gamma lattice, and it is invisible to eq:Qbalance.

**Next sub-lemma G1.3 (non-commutative input: compression against the polar layer).** The closing
identity must contain an operator outside the multiplier algebra. The only one available is the
compression P_T entering through H_TF = 0 (eq:localweak). G1.3: form the compressed first-contact
equation 𝔞_T(F, P_T Z_P^* φ) = ⟨r, P_T Z_P^* φ⟩ for exterior test directions φ, and determine whether
it expresses the higher Tate jets ∂^k_a[K_F](−½) (k ≤ π(P)) of §4(ii) in terms of the Gamma residues
K_F(a_m). Such a relation would be non-tautological, because it uses H_TF = 0. Before building,
check whether this is the Brown–Halmos Hankel term of R162_301 Thm 1.1 (the compression defect of
Z_P = A_P^{−1}), in which case it is closed there. Filter F1 first: the relation must fail for
λ > 0 eigenvectors.

GATE 1: OPEN. Row D: OPEN.

Files edited: this file only.
