# R164_502: Determinants, Szegő–Widom and spectral moments of the window operator A_T

*Phase 164, round 3. Memo, pure mathematics, no numerics. Labels: PROVED / PROVED-CITED / ARGUED / OPEN.*
*Read first: R164_190 (whole), R164_101 (Thm E1, Prop D, Prop EB), R164_401 (Thm R), R163_401 §1, §2, §4.6, §4.11(c) (Thm F),
R163_802 (Selberg fixed point), Paper 46 `eq:symbol`, `eq:form`, `def:W`, `thm:Z`, `thm:O`, and the compact-resolvent paragraph before `lem:contA`.*

## 0. Corpus check (rules: check the corpus first, master grid first)

grep over `03-research/phase-16-surf-witness-variety*` for "Fredholm | determinant | Szegő | Szego | Widom | Stieltjes | Hamburger | heat trace | spectral shift | Krylov":

| hit | content | bearing here |
|---|---|---|
| R162_2602 Prop 8(b), l.101 | Landau–Widom/Szegő count for truncated convolutions, N(T) ~ (T/π)\|{σ<0}\|. Also: "for ζ the symbol is a positive measure plus the rank-2 pole iff RH" | this is already the Szegő reading of §2 below. 8D was NO-GO (R162_2602) |
| R160_S1 #27 | Hamburger/Carleman trace criterion RH ⟺ ∫κ_n dν = 0 | a moment criterion on a different measure. Equivalence only, no sign |
| R160_S5 B3, R160_PD_R1 | Hamburger datum (E)+(P)+(FE) yields no inequality | same wall as §4 below |
| R160_001, R160_S4 | Zhu's Landau–Widom law −log λ ≍ e^{2T} (conjecture, cited) | asymptotics of λ_min, not its sign |
| R162_1001 | Krylov–Bogolyubov from a first-contact vector returns Lebesgue | a different Krylov (ergodic), not used |
| R163_802 Fact 3, §2 | Selberg's identity Λ·log + Λ∗Λ = μ∗log² ⟺ B″/B = ζ″/ζ ⟺ B = ζ | identification (wall W3′), see §5 |

No earlier memo studies spectral moments ⟨A_T^kF,F⟩ or tr φ(A_T), and none uses the Widom finite-section identity. Those are the new material here. Everything else turns out to be an existing wall.

## Status table

| # | statement | label |
|---|---|---|
| L0 | σ_T(0) ≤ m(0) = ψ(¼) − log π ≈ −5.372 < 0 for every T. The symbol is never positive, so the strong Szegő / Kac–Akhiezer theorem does not apply to σ_T | **PROVED** |
| L1 | (window locality) A_T = P_{I_T} σ_∞ P_{I_T}, where σ_∞ is the untruncated symbol. A_T depends only on σ̌ restricted to (−2T,2T), i.e. on m̌ and (Λ(n))_{n<e^{2T}}. Every spectral invariant of A_T is a function of the window | **PROVED** |
| L2 | The Szegő route is circular. A symbol on which Szegő is applicable (a positive density, or a positive measure plus the Tate rank 2) makes A_T ⪰ 0 trivially, and for ζ the effective symbol (Thm E1 / thm:Z: the zero measure) is a positive measure iff RH. Under RH it is singular (atoms), so log σ and Σk\|(log σ)^_k\|² are undefined | **PROVED** (reduction). Reading already in R162_2602 |
| L3 | Weyl law: λ_j(A_T) = log j + O_T(1). Hence tr A_T^k = ∞, the resolvent lies in no Schatten class S_p, and det, det_p and the ζ-regularised determinant of A_T are all undefined. The relative determinant against the archimedean part M_T is also undefined | **ARGUED** (Weyl law). The consequences are PROVED given it |
| L4 | Heat-trace criterion: Θ_T(s) := tr e^{−sA_T} < ∞ for s > s₀ = 1. Row D ⟺ ∀T: sup_{s≥2} Θ_T(s) < ∞ ⟺ ∀T: lim_{s→∞} e^{0·s}Θ_T(s) exists finite. First contact = first T at which Θ_T(s) stops being bounded as s → +∞ | **PROVED** given L3's lower bound λ_j ≥ log j − C_T (ARGUED) |
| L5 | Stieltjes = Krylov. For F ∈ dom A_T^{N}, the Stieltjes conditions (m_{i+j})⪰0 and (m_{i+j+1})⪰0 on m_k = ⟨A_T^kF,F⟩, k ≤ 2N, hold iff 𝔞_T ⪰ 0 on the Krylov space 𝒦_N(F) = span{F, A_TF, …, A_T^{N−1}F}. Quantified over F this is equivalent to row D, and adds nothing to k = 1 | **PROVED** |
| L6 | Widom finite-section identity: A_T² = P σ_T² P − P σ_T Q σ_T P (Q = 1 − P). Frequencies log(mn) ≥ 2T of σ_T² are annihilated by P·P. The Selberg convolution Λ∗Λ enters m₂ only at N < e^{2T}. More generally, in A_T^k every frequency outside (−2T,2T) is cancelled exactly | **PROVED** |
| L7 | Selberg is window data. For N < e^{2T}, (Λ∗Λ)(N), (μ∗log²)(N) and Λ(N)log N are all determined by (Λ(n))_{n<e^{2T}}. The generalised Selberg identity −A_f′ + A_f² = f″/f holds for every Dirichlet series f, including f_t | **PROVED** |
| L8 | No k separates ζ from f_t. For T ≤ ½log λ₁, A_T^{f_t} = A_T^ζ as operators (L1 + Thm F), so all moments, heat traces, spectral shifts and n₋ agree. For T > ½log λ₁ they already differ at k = 1. The separation is in T, never in k | **PROVED** (Thm F PROVED-CITED) |
| L9 | Kreĭn index form: row D ⟺ ∀T: ξ(0⁺; A_T, M_T) = −n₋(M_T), with n₋(M_T) ~ (T/π)\|{m<0}\| → ∞ | **PROVED** (equivalence). The asymptotic is PROVED-CITED (Landau–Widom). Sign: OPEN = RH |

## 1. Setup

As in R163_401 §1.1. On L²(ℝ) let 𝔐 be the Fourier multiplier by m, and S_a f(t) = f(t − a). Put P = P_{I_T} (multiplication by 1_{I_T}) and Q = 1 − P. Then 𝔞_T(F) = ⟨A_TF,F⟩ with

  A_T = P(𝔐 − Σ_{n∈𝒩_T} w_n(S_{log n} + S_{−log n}))P,  w_n = Λ(n)/√n,

which is the Paper 42/47 operator. It is self-adjoint and bounded below, with compact resolvent (Paper 46, paragraph before `lem:contA`, via Bombieri 2000 Thm 3). Write M_T := P𝔐P and Π_T := A_T − M_T (the prime part).

## 2. Szegő–Widom on σ_T: L0, L1, L2

**L0. PROVED.** m(0) = Re ψ(¼) − log π = (−γ − π/2 − 3log 2) − log π ≈ −4.2274 − 1.1447. Since v_n > 0, σ_T(0) = m(0) − Σ_{𝒩_T}v_n ≤ m(0) < 0. As σ_T is continuous, it is negative on a neighbourhood of 0. So log σ_T is not real, and neither the strong Szegő theorem nor the Kac–Akhiezer formula (which needs a symbol 1 + k̂ with k ∈ L¹, 1 + k̂ > 0 and a winding-free logarithm) applies. Moreover m(τ) ~ log(|τ|/2π) is unbounded, so even the bounded-symbol hypothesis fails. ∎

**L1 (window locality). PROVED.** For F ∈ L²(I_T), PS_aF = 0 when |a| ≥ 2T, because supp S_aF ⊂ I_T + a is disjoint from I_T. So adding the shifts with log n ≥ 2T does not change A_T, and A_T = P σ_∞ P. Here σ_∞ is the formal full symbol, i.e. any symbol in the flat-top class of `def:W` (w ≡ 1 on [−2T,2T]). In kernel form, A_T has the distributional kernel σ̌(t − s), |t − s| < 2T, which only involves σ̌|_{(−2T,2T)}. This is the operator version of the observation in Thm E1 (R164_101) that "M has Fourier support in u ≥ 2T, invisible". ∎

**L2 (circularity). PROVED.** Szegő-type asymptotics of log det P a P presuppose a ≥ 0, and then ⟨PaPF,F⟩ = (2π)^{−1}∫a|F̂|² ≥ 0 trivially, so they carry no information about the sign. The question is whether ζ admits some representative of its compressed symbol that is ≥ 0. By L1, any two symbols with the same Fourier restriction to (−2T,2T) for all T give the same A_T. By Thm E1 / `thm:Z`, the distinguished representative is the zero measure 2πΣ_ρ δ_{t_ρ} (plus the rank-2 Tate term), and it is a positive measure on ℝ iff all t_ρ are real, i.e. RH. Even under RH it is purely atomic, so log a, (log a)^_k and the Szegő constant Σk|(log a)^_k|² are undefined. **The Szegő/Kac–Akhiezer–Verblunsky positivity Σk|(log a)^_k|² ≥ 0 is a sign fact about log det, and log det requires positivity first.** ∎ (R162_2602 had already made the "positive measure iff RH" reading in the counting context.)

## 3. No determinant exists: L3, L4

**L3 (Weyl law). ARGUED.** Π_T is bounded: ‖Π_T‖ ≤ 2Σ_{𝒩_T}w_n = 𝒜_T. By min–max, |λ_j(A_T) − λ_j(M_T)| ≤ 𝒜_T. For M_T, the compression of a multiplier m ~ log|τ| to an interval of length 2T, the Landau–Widom count gives #{j : λ_j(M_T) < Λ} ~ (2T/2π)·|{m < Λ}| ~ (2T/π)·2π e^{Λ}. Hence λ_j(M_T) = log j + O_T(1). The upper bound follows from min–max on a span of j sine modes vanishing at ±T, whose Fourier transforms decay like τ^{−2}. The lower bound follows from the Landau–Widom count applied to the bounded multiplier min(m, Λ). This last step is cited but not written out here, hence ARGUED.

**Consequences. PROVED given L3.** Σ_j λ_j^k = ∞ for every k ≥ 1, so tr A_T^k = ∞. Σ_j |λ_j + c|^{−p} ≍ Σ (log j)^{−p} = ∞ for every p, so (A_T + c)^{−1} ∉ S_p for any p, and the Fredholm determinants det_p(1 − z(A_T + c)^{−1}) are undefined. The spectral zeta Σ λ_j^{−s} diverges for every s, so the ζ-regularised det A_T is undefined. For the relative determinant det(1 − (M_T + c)^{−½}Π_T(M_T + c)^{−½}): the middle operator has singular values bounded by 𝒜_T(log j)^{−1} only, so it is in no S_p unless Π_T itself is. Π_T is not compact: the compression of a single shift S_a, 0 < a < 2T, is a partial isometry from L²(−T, T − a) with infinite rank. So this determinant is undefined too. The literal programme "det(A_T) as a function of T" has no object.

**L4 (heat trace replaces the determinant). PROVED given L3.** Since λ_j ≥ log j − C_T, we get e^{−sλ_j} ≤ e^{sC_T} j^{−s}, so Θ_T(s) = Σ_j e^{−sλ_j} < ∞ for s > 1, and Θ_T is a "spectral Dirichlet series" with frequencies λ_j. As s → +∞, Θ_T(s) = mult(λ_min)·e^{−sλ_min}(1 + o(1)). Hence λ_min ≥ 0 ⟺ Θ_T is bounded on [2,∞). Row D ⟺ Θ_T is bounded on [2,∞) for every T. ∎ This is a correct and new criterion, but by L1 Θ_T is a function of the window, and it is equivalent to row D by a one-line Tauberian argument. It carries no new sign.

## 4. Moments: Stieltjes = Krylov (L5)

The spectral measure of A_T is not finite (tr = ∞). The meaningful moment sequences are the vector ones: μ_F := ⟨E(·)F,F⟩, with m_k(F) = ⟨A_T^kF,F⟩ for F ∈ dom(A_T^{k/2}).

**L5. PROVED.** Let G = Σ_{i<N} c_i A_T^iF ∈ 𝒦_N(F). Then ⟨G,G⟩ = Σ c_i c̄_j m_{i+j} and ⟨A_TG,G⟩ = Σ c_i c̄_j m_{i+j+1}. So (m_{i+j})_{i,j<N} ⪰ 0 always holds (it is a Gram matrix), and (m_{i+j+1})_{i,j<N} ⪰ 0 ⟺ 𝔞_T ≥ 0 on 𝒦_N(F). Since F ∈ 𝒦_N(F), the case N = 1 is m₁(F) ≥ 0. So:
- for a fixed F, the Stieltjes conditions are form positivity on a finite-dimensional subspace (linear in G, quadratic in the coefficients);
- ∀F: (Stieltjes at all orders) ⟺ ∀F: m₁(F) ≥ 0 ⟺ supp μ_F ⊂ [0,∞) ∀F ⟺ A_T ⪰ 0.

At k ≤ 2: m₀ = ‖F‖² ≥ 0 and m₀m₂ ≥ m₁² hold for every self-adjoint operator (Cauchy–Schwarz on F and A_TF), whatever the sign. Only m₁ ≥ 0 and det[[m₁,m₂],[m₂,m₃]] ≥ 0 carry the sign. The latter is 𝔞_T ⪰ 0 on span{F, A_TF}. ∎ So the move "non-linear in the test" (S2) is only apparent: Hankel positivity in the moments is form positivity on Krylov subspaces, i.e. row D restricted to a subspace.

## 5. Moments and the Selberg identity: L6, L7, L8

**L6 (Widom finite-section identity). PROVED.** Here σ_T acts as the bounded-below multiplier on L²(ℝ), and P is idempotent. Then P σ_T P σ_T P = P σ_T (1 − Q) σ_T P = P σ_T² P − P σ_T Q σ_T P. So

  m₂(F) = ‖A_TF‖² = ⟨σ_T²F,F⟩_{L²(ℝ)} − ‖Q σ_T F‖²,

which is Widom's T(ab) − T(a)T(b) = H(a)H(b̃) in its interval form. Expand the prime part of σ_T²:

  (Σ_{m}w_m(S_{log m}+S_{−log m}))² = Σ_{m,n}w_mw_n(S_{log mn} + S_{−log mn} + S_{log(m/n)} + S_{log(n/m)}),

with m, n ∈ 𝒩_T. The sum frequencies are grouped by N = mn with coefficient Σ_{mn=N}Λ(m)Λ(n)/√N = (Λ∗Λ)(N)/√N for N < e^{2T} (all divisors of such N lie in the window). In ⟨σ_T²F,F⟩ the term S_{±log N} contributes ⟨S_{log N}F,F⟩ = c_F(log N), which vanishes for log N ≥ 2T. So Selberg's convolution enters m₂ only through N < e^{2T}. There, (Λ∗Λ)(N) = (μ∗log²)(N) − Λ(N)log N. The large products e^{2T} ≤ mn < e^{4T} are present in σ_T², but they are killed on I_T, and the term ‖Qσ_TF‖² subtracts exactly the excursions of σ_TF outside I_T. Inductively, A_T^k = P(σ_TP)^{k−1}σ_TP, and each intermediate P truncates. A_T^k is therefore never the compression of σ_T^k. It is the compression of a word in which every partial sum of shifts is kept inside I_T. Frequencies of the k-fold convolution Λ^{∗k} at N ≥ e^{2T} never enter m_k. ∎

**L7. PROVED.** If N < e^{2T}, every divisor d | N satisfies d < e^{2T}, so (Λ∗Λ)(N) involves only window values. Also μ(d) for d < e^{2T} is a function of the window: μ is determined by the window values of Λ through the recursion ζ = exp(ΣΛ(n)n^{−s}/log n) truncated at N, since b = exp_∗(Λ/log) coefficient by coefficient (R163_802 §2). For a general Dirichlet series f with A_f = −f′/f, the identity −A_f′ + A_f² = f″/f is the logarithmic-derivative identity (R163_802 §2), with coefficients a_f·log + a_f∗a_f = (b_f^{−1})∗(b_f·log²). Selberg's identity for ζ is its instance with b = 1. Its content beyond this formal identity is "b ≡ 1", which is identification (R163_802: B″/B = ζ″/ζ ⟹ B = ζ; wall W3′, the same rigidity as Thm R of R164_401). ∎

**L8 (no k separates ζ from f_t). PROVED, with Thm F PROVED-CITED.** By Thm F (R163_401 §4.11(c)), f_t has the archimedean part m and the prime side of ζ on |u| < log λ₁. For T ≤ ½log λ₁, L1 gives A_T^{f_t} = A_T^ζ as operators on L²(I_T). So m_k(F), Θ_T(s), n₋, ξ and every other spectral invariant coincide, for every k and every F. Its generalised Selberg identity coincides with ζ's for every N < λ₁ (L7, same window). For T > ½log λ₁, σ̌^{f_t} − σ̌^ζ has an atom at ±log λ₁ ∈ (−2T,2T). Choose F with c_F(log λ₁) ≠ 0 (e.g. F = 1_{I_T}, for which c_F(u) = 2T − |u| > 0). Then m₁(F) already differs. So the moments separate the two exactly when the windows do, already at k = 1. Higher k does not shift the separation threshold. **The separation is in T, never in k.** ∎

The same argument applies to the deletion D of R164_101 Prop D. Its window differs from ζ's at n < 5, so it is separated already at k = 1, and correctly so. Its Selberg-type identity holds with its own b. Hence moments see only window differences, never "Euler product vs no Euler product" above the window.

## 6. Kreĭn spectral shift (L9)

**L9. PROVED (equivalence).** A_T − M_T = Π_T is bounded. Even when Π_T is not trace class, the integer-valued shift ξ(λ; A_T, M_T) := N_{A_T}(λ) − N_{M_T}(λ) is well defined via eigenvalue counts below λ, which are finite by compact resolvent. Row D at T ⟺ N_{A_T}(0) = 0 ⟺ ξ(0⁺) = −N_{M_T}(0) = −n₋(M_T). By Landau–Widom (PROVED-CITED, as used in R162_2602 Prop 8(b)), n₋(M_T) ~ (T/π)|{m < 0}| → ∞. So the prime comb must remove a negative space of dimension growing linearly in T, exactly. As an equivalence this is a counting form of row D (8D, wall W12/W6). It gives no inequality: the counting has no sign mechanism, and by L1 and L8 it is again window data shared with f_t.

## 7. Where it stops

$$\boxed{\begin{array}{c}
\text{Every spectral functional of the window operator }A_T\text{ (moments }\langle A_T^kF,F\rangle\text{, heat trace }\mathrm{tr}\,e^{-sA_T}\text{, Kreĭn shift, any regularised determinant)}\\
\text{is a function of }\check\sigma|_{(-2T,2T)}\text{ only, i.e. of the archimedean part and }(\Lambda(n))_{n<e^{2T}}\ \text{(L1). In }A_T^k\text{ the }k\text{-fold}\\
\text{convolutions }\Lambda^{*k}\text{ (hence Selberg's identity) enter only at }N<e^{2T}\text{: Widom's finite-section term cancels every frequency}\\
\text{outside the window exactly (L6). ``Uses }\zeta\text{ at all heights through the symbol'' (S7) is therefore false for the compressed operator.}\\
\text{Hankel/Stieltjes positivity of the moments is form positivity on Krylov subspaces (L5): S2 is met only formally.}\\
\text{Szegő/Kac–Akhiezer requires a positive symbol, and }\zeta\text{'s compressed symbol has a positive representative iff RH (L0, L2).}\\
\text{No determinant exists: }\lambda_j\sim\log j\text{ puts the resolvent in no Schatten class (L3); the heat trace is the substitute (L4).}\\
\text{Falsifier: }A_T^{f_t}=A_T^{\zeta}\text{ for }T\le\tfrac12\log\lambda_1\text{, so no }k\text{ separates; the separation is in }T\text{ (L8).}\\
\text{The route is DEAD by E1 + W3 (window locality), with W12 for the determinant/Kreĭn form. Residue: none new; it folds into O164.101 / O2601.1.}
\end{array}}$$

The positive outcome is that the moment/determinant programme has a precise formulation (L4, L5, L9), and each formulation is an equivalence with row D whose data are the window. Any separator must act on the tail above e^{2T}, which A_T never sees. That is again the question O164.101 ≡ O164.102.1 (R164_190 synthesis), now closed against the spectral-invariant route as well.

## 8. Ledger

| item | label | depends on |
|---|---|---|
| L0 σ_T(0) < 0 ∀T | PROVED | ψ(¼) = −γ − π/2 − 3log 2 |
| L1 window locality A_T = Pσ_∞P | PROVED | supports; Thm E1 (R164_101) |
| L2 Szegő circular / RH-equivalent | PROVED | L1, thm:Z, Thm E1 |
| L3 Weyl λ_j = log j + O_T(1); no S_p, no det | ARGUED (Weyl); PROVED given it | Landau–Widom (cited), min–max |
| L4 heat-trace criterion | PROVED given L3 lower bound | L3 |
| L5 Stieltjes ⟺ Krylov form positivity | PROVED | linear algebra |
| L6 Widom finite-section identity, frequencies outside the window cancelled | PROVED | P² = P |
| L7 Selberg = window data + identification | PROVED | R163_802 §2 |
| L8 no k separates ζ from f_t | PROVED (via Thm F, PROVED-CITED) | L1, R163_401 Thm F |
| L9 Kreĭn index equivalence | PROVED (equiv.); n₋(M_T) ~ cT PROVED-CITED | compact resolvent, Landau–Widom |
| sign of A_T | OPEN (= RH) | — |

New open items: none. O164.101 is unchanged.

## 9. Grid (append to R162_2300 per the master-grid rule)

- **4A** (Euler × one-window form): +1 DEAD route "R164_502 spectral moments / Selberg in m_k". Killer W3 + L1/L6: Selberg's identity enters only at N < e^{2T}, i.e. window data. Falsifier f_t (L8). The cell stays ◧ (its OPEN items are untouched).
- **4E** (Euler × flow/family in T): +1 DEAD route "R164_502 det/heat trace/Kreĭn shift as a function of T". Killers W12 (exact equivalence, no sign: L4, L9) and E1 (L2). There is no determinant object (L3). The cell stays ◧.
- **8D** (no arithmetic × spectrum): +3 PROVED-TOOL entries: L4 (heat-trace criterion), L5 (Stieltjes = Krylov), L6 (Widom identity for A_T^k). +1 DEAD route "Szegő–Widom strong limit for σ_T" (L0/L2, W4/W6: positive symbol iff RH). The cell stays ◧ (O2601.1, O2602.2 still live).
- Walls: W3 (class blindness through window locality), W12, E1. Falsifiers used: f_t (decisive), deletion (consistency check).
