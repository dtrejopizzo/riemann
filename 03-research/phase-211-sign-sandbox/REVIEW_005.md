# Review 005: rounds 005_D, 006_B, 006_C, 007_B, 007_C, 007_D, 008_D against Paper 46 and STATEMENT_001

Scope. ROUND_005_D, ROUND_006_B, ROUND_006_C, ROUND_007_B, ROUND_007_C, ROUND_007_D, ROUND_008_D, checked against Paper 46 (04-papers/46-row-d-dual-certificates/main.tex:
lem:K, thm:A, prop:nodes, lem:parity, prop:archneg, thm:parityschur, prop:polarcap, prop:sharp, lem:polarelim, lem:monoT) and STATEMENT_001. No equivalence of the
window statement (★) with any other statement is invoked. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO /
NUMERICAL. Verdicts on PROVED claims: CONFIRMED (key step named) / REFUTED / DOWNGRADE. "L.n" = line n of the memo under review.

Independent computations made for this review (scratch only, nothing added to the repository besides this file):
(a) a quadrature check of Proposition 4.2 of 005_D at T = 0.9 on F(t) = (1 − t²/T²)(1 + t + t³) (neither even nor odd, comb
{2,3,4,5}): a_T(F, χ_+) by the polarised Lévy form = −4.682612523688269, ⟨F, χ_+ω_+⟩ = −4.68261252368827 (difference 9·10⁻¹⁶);
the elementary identity ∫_0^{2T}(1 − cosh(u/2))K = −T − 2 log cosh(T/2) + arctan(sinh T) agrees to 30 digits at T = 0.3, log 2, 1;
(b) the polar quantities W_par(0) = ⟨χ_par, a_T^{−1}χ_par⟩ at T = 0.25, 0.30, 0.40, 0.45, 0.60 with tools/galerkin_mp.py
(N = 60 sines, dps 40, cached matrices); (c) a full re-run of tools/falsifier_cert_run.py for the three certificates of 007_C.


---------------------------------------------------------------------------------------------------------------------
## 1. ROUND_005_D

**Lemma 1.1 (L.74–80) and the jump/killing form (L.82–93).** CONFIRMED. Key step: c_F(0) − Re c_F(u) = ½∫|F̃(t) − F̃(t−u)|²dt
and −v_n Re c_F(u_n) = v_n(c_F(0) − Re c_F(u_n)) − v_n‖F‖², on top of thm:A. The killing κ is the mass of the even
extension of μ_T falling outside I_T; the edge asymptotics are those of thm:S(iii).

**Proposition 1.2 (L.95–109).** (i)–(iv) correctly labelled CITED. (v) CONFIRMED (simplicity plus positivity). (vi)
CONFIRMED (⟨h_T, χ_+⟩ > 0; codimension-two count). (vii) is a description, not a theorem; the "PROVED" tag should read
ARGUED/NUMERICAL (the overlap values are numerical).

**Theorem 2.1 (L.118–138).** CONFIRMED. Key step: the pointwise identity (hφ(x) − hφ(y))² = h(x)h(y)(φ(x) − φ(y))² +
(h(x) − h(y))(G(x) − G(y)) with G = hφ², integrated against ½J, plus the killing term, which is absorbed exactly into
𝔈_μ(h, G) = λ_0⟨h, G⟩. Membership of G in the form domain uses only that φ² is bounded Lipschitz and that ∫min(u², 1)dμ_T
< ∞. The extension to general φ is correctly marked CITED.

**Corollary 2.2 (L.147–158).** The equivalence with (2.1) is CONFIRMED (a rearrangement of Theorem 2.1; |μ_0| = A_T − C_0 −
λ_0 is the definition of λ_0). The parenthetical justification of μ_0 < 0 (L.155–156) is REFUTED as written: prop:archneg
(main.tex L.2587–2621) bounds the archimedean COMPLETE form 𝔄_∞(t·1_{I_T}) = Arch − 2s², whose negativity comes from the polar
square −2s²; the inequality "a_T ≤ 𝔄_∞ on the odd function" would need Π(F) ≥ 2s² for F = t, which is not shown and is not
implied by anything in the paper (c_F(u) = (4T³ − 6T²u + u³)/6 changes sign on (0, 2T), so even the sign of Π(F) is not
fixed). The conclusion μ_0 < 0 is true at every window computed (NUMERICAL: μ_0^{ev} = −0.908, −1.113, −1.529, −1.976, −2.399
at T = 0.25, 0.30, 0.40, 0.50, 0.60, review computation (b)) and nothing downstream depends on the citation; DOWNGRADE the
clause to NUMERICAL.

**Theorem 3.1 (L.171–187) against thm:parityschur.** CONFIRMED. Key step: a constrained critical value z off the spectrum
forces F = β(a_T − z)^{−1}χ and W(z) = 0; W is increasing between poles with W → −∞ at μ_0⁺ (τ_0 ≠ 0) and +∞ at μ_1⁻ (τ_1 ≠ 0),
and interlacing places λ_A^{par} in [μ_0, μ_1]. Comparison with the paper: Theorem 3.1 assumes 0 ∉ spec(a_T | L²_par) and
works with the resolvent on the whole sector; thm:parityschur(a) only needs 0 ∉ spec(a_T | 𝒬^{par}_T) (main.tex L.4222–4225)
and so is strictly more general. When both apply, h_par = a_T^{−1}χ_par / W_par(0), 𝔞_T(h_par) = 1/W_par(0) and

    𝔤_par = 2ε_par + 1/W_par(0) = (1 + 2ε_par W_par(0)) / W_par(0),

which is the identification used at L.385–392 (CONFIRMED). The statement "(★)_par ⟺ W_par(0) ≤ 0 when n₋ = 1" is internal to
the window form and invokes no outside equivalence.

**Corollary 3.2 (L.189–199).** CONFIRMED. Key step: W(λ_A) = 0 solved for the τ_1 term; the interlacing λ_A ≤ μ_1 ≤ λ_{A,2}
is the one-constraint Cauchy interlacing. Note: g_1 in (3.2) is the gap of the sector, not the global gap of Theorem 2.1
(the odd bottom can lie below μ_1^{ev}); L.407 says so, L.145 does not.

**Corollary 3.3 (L.201–208).** CONFIRMED. Key step: ⟨1, ψ⟩_{h²} = τ_0, ‖ψ‖²_{h²} = ‖χ‖², Cauchy–Schwarz on 1^⊥.

**Proposition 4.2 (L.239–262).** CONFIRMED, symbolically and numerically. Symbolic check: τ_uχ_+ = e^{−u/2}e^{t/2}1_{[−T+u, T+u]}
gives the indicator 1_{u<T+t}, τ_{−u} gives 1_{u<T−t}; with v_n = 2Λ(n)/√n, ½v_n e^{−u_n/2} = Λ(n)/n and ½v_n e^{u_n/2} = Λ(n),
so the comb contributes −ψ_1(e^{T+t}) − ψ(e^{T−t}); the second form follows from 1_{u<T±t} = 1 − 1_{T±t≤u<2T} on u < 2T and the
elementary integral, which the review checked to 30 digits at T = 0.3, log 2, 1. Domain: χ_+ has a jump at the edges, so
|χ̂_+|² ~ τ^{−2} and ∫m|χ̂_+|² < ∞ (m ~ log τ); χ_+ω_+ ∈ L² (logarithmic singularities). Numerical check (a) on a test that is
neither even nor odd and not supported in the interior: agreement to 9·10⁻¹⁶. Positivity of ω_+ − σ_T is termwise.

**The values W_ev(0) = −½, W_odd(0) = +½ (L.317–333, 355–361, 370–398): exact identity or near-degeneracy?** Near-degeneracy;
an exact identity is REFUTED. By the display above, W_ev(0) = −½ exactly is 𝔤_ev = 0, i.e. (thm:parityschur(a2)) a nonzero
radical of the complete form W_T in the even sector, and W_odd(0) = +½ exactly is 𝔤_odd = 0; under (a4) one has
𝔤_par/‖h_par‖² ∈ [λ^W_{T,par}, 2λ^W_{T,par}], so the deviation is controlled by the bottom of the complete form in that sector,
not by λ_A. Review computation (b), N = 60 sines per window, dps 40 (NUMERICAL):

| T | W_ev(0) | 1 + 2W_ev(0) | λ^W_{T,ev} | λ_A^{ev} | W_odd(0) | 1 − 2W_odd(0) | λ^W_{T,odd} | λ_A^{odd} |
|---|---|---|---|---|---|---|---|---|
| 0.25 | −0.519969 | −4.0·10⁻² | 3.4·10⁻² | 0.880 | +0.005446 | 0.989 | 0.414 | 1.18 |
| 0.30 | −0.503931 | −7.9·10⁻³ | 8.0·10⁻³ | 0.697 | +0.016466 | 0.967 | 0.228 | 0.993 |
| 0.35 | −0.500571 | −1.1·10⁻³ | 1.3·10⁻³ | 0.542 | +0.074463 | 0.851 | 0.069 | 0.840 |
| 0.40 | −0.500084 | −1.7·10⁻⁴ | 2.0·10⁻⁴ | 0.236 | +0.246851 | 0.506 | 0.016 | 0.783 |
| 0.45 | −0.500007 | −1.5·10⁻⁵ | 1.8·10⁻⁵ | 0.0705 | +0.436667 | 0.127 | 2.6·10⁻³ | 0.502 |
| 0.50 | −0.5000004 | −8.2·10⁻⁷ | 1.0·10⁻⁶ | 0.0132 | +0.494701 | 1.1·10⁻² | 2.2·10⁻⁴ | 0.201 |
| 0.60 | −0.50000000068 | −1.4·10⁻⁹ | 1.8·10⁻⁹ | 7.7·10⁻⁵ | +0.499986 | 2.8·10⁻⁵ | 6.8·10⁻⁷ | 3.8·10⁻³ |

So W_ev(0) + ½ and ½ − W_odd(0) are positive multiples of the sector bottoms of W_T (|1 + 2W_ev(0)| ≈ 0.8–1.2·λ^W_{T,ev}
throughout), they are visibly non-zero below T ≈ 0.5, and they fall below the five printed digits of ROUND_005_D exactly
when λ^W_T does. The "∓½ to all digits" of L.355, L.371–374, L.388 is the numerical shadow of the near-null vector of W_T
(𝔤_par ≈ 0⁺), the complete-form counterpart of the tangency already recorded for the primitive form. Two corrections to
the memo: (1) L.360 "the deviation 𝔊_T from 0 is of the order of λ_A" is wrong in the even sector (at T = 0.45 the
deviation is 1.5·10⁻⁵ against λ_A^{ev} = 0.07); it is of the order of λ^W_{T,par}; (2) L.522–523 should record the values as
NUMERICAL near-equalities with this mechanism, not as "W_ev(0) = −½, W_odd(0) = +½" without qualifier. The statement at
L.397–398 (an exact S^{Sch}_T = −D_pol would give λ_W ≤ 0 by (a4)) is correct and is the internal reason exactness cannot
hold at any window where λ_W > 0.

**Theorem 6.1, class 𝒦_gap (L.411–434).** DOWNGRADE to ARGUED. The core statement is a tautology once the slack is
identified: by Corollary 3.2, g_1 − |μ_0| − τ_1²/D = μ_1 − τ_1²/D = λ_A^{ev}, so s_T = λ_A^{ev}/|μ_0^{ev}|, and "a bound with
relative loss ε cannot prove a statement with relative slack < ε" is immediate. What is not proved is the membership of
each listed tool in the class with a comb-independent ε (Cheeger, Lyapunov, coupling, CD, supersolutions are asserted to
carry an intrinsic loss, L.417–432, without a quantitative statement). The NO-GO is also window-restricted: s_T is of size
1 at T = 0.25 (λ_A^{ev} = 0.88, |μ_0| = 0.91) and the class is excluded only where λ_A^{ev}/|μ_0| is small (T ≳ 0.6 on the
computed range). Register entry (ARGUED NO-GO): "lossy gap bounds for the h_T-transformed jump form, at windows with
λ_A^{ev}/|μ_0| below the method loss".

**Other points.** L.444–446: "Π is indefinite with at least two positive eigenvalues on L²_ev(I_T) for 2T > log 2, by
CA_I_001 Thm 2's construction (PROVED)" is a cross-reference not re-verified here; label CITED. §5 and §4.3 are NUMERICAL and
labelled so. Remark 3.4 correctly classifies Theorem 3.1 as a restatement of prop:polarcap / thm:parityschur.

---------------------------------------------------------------------------------------------------------------------
## 2. ROUND_006_B, Propositions 4.1–4.4

**Proposition 4.1 (L.203–216), set invariance.** The first assertion is CONFIRMED. Key step: a word in generators of
degrees d_i satisfies W(cv) = c^{Σd_i}W(v), so each generating vector is rescaled by a positive factor and the spans
coincide; concavity of c ↦ λ_min(M − cΠ_P | 𝒲_j) and the Danskin formula for its one-sided derivatives are standard. The
last clause (L.211–212, repeated L.366–367), "rejection of c = 1 + ε requires a minimiser u with ⟨Π_Pu, u⟩ ≥
λ_min(a_T|𝒲_j)/ε", is REFUTED as stated. Concavity gives f(1 + ε) ≤ f(1) + εf′_+(1), an upper bound; it does not prevent
f from dropping below its tangent, so f(1 + ε) < 0 can occur through a direction that does not minimise a_T on 𝒲_j. The
correct necessary condition needs no Danskin: if (M − (1 + ε)Π_P)(u) < 0 for a unit u ∈ 𝒲_j, then ε⟨Π_Pu, u⟩ > a_T(u) ≥
λ_min(a_T|𝒲_j), so SOME unit u ∈ 𝒲_j (the negative direction of the c-form, not a minimiser of a_T) has ⟨Π_Pu, u⟩ >
λ_min/ε. The uniqueness clause ("if the minimiser is unique and ⟨Π_Pu, u⟩ ≤ 0, no c ∈ (1, 1 + ε) is rejected") is true but
empty when λ_min(a_T|𝒲_j) > 0 (continuity alone gives it). DOWNGRADE the proposition to its first two sentences; the
reading at L.218–223 and the NO-GO of §5 use only set invariance and are unaffected.

**Proposition 4.2 (L.227–239).** (i) The inclusion of the word family of G = ΣG_d in that of {G_d} is CONFIRMED; the
sentence "the only way to obtain a subspace that depends on c is …" is a description, ARGUED. (ii) CONFIRMED. Key step:
P_U p(G)e = p(G|_U)P_Ue, and for u ⊥ P_Ue, ⟨u, p(G)e⟩ = ⟨u, (p(G|_U) − p(λ_1))P_Ue⟩ with ‖p(G|_U) − p(λ_1)‖ ≤ δ sup|p′|.
Caveat for the reading at L.241–247: C_j(G, e) is finite by compactness but is not controlled; it depends on δ (through
the supremum over the interval) and on how small ‖p(G)e‖ can be for polynomials concentrated near the cluster, so
"resolves the cluster at rate O(δ)" is a qualitative statement for fixed G, not a bound uniform in T.

**Proposition 4.3 (L.251–265).** CONFIRMED. Key steps: for F supported in I and t ∉ I, (𝔪F)(t) = ½∫(0 − F(s))K(|t − s|)ds,
with the ½ forced by m(τ) − C_0 = ∫_0^∞(1 − cos τu)K(u)du (lem:K); H_x* = L_x by self-adjointness of Q, R, 𝔪, c_x; [M_0, S_x] =
H_x − L_x by inserting Q = 1 − R and [𝔪, c_x] = 0 on L²(ℝ); the explicit kernels follow from (Rc_xQF)(s) = ½F(s − x) on (T,
T + x) and ½F(s + x) on (−T − x, −T) (x = log n < 2T); [M, Π_P] = P[M_0, Π]P − PM_0ΓΠP + PΠΓM_0P from P = 1 − Γ, with Γ of rank
two and Γ's range in the operator domain of M_0 (ROUND_005_D Prop. 4.2). The correction of the factor ½ in ROUND_005_A
Prop. 4.2(v) is right.

**Proposition 4.4 (L.282–302).** The matrix 𝔄_3 is CONFIRMED entry by entry. Key steps: ⟨e, g⟩ = αμ_1 − αμ_1 = 0, ⟨p, g⟩ = m_2 −
αμ_2, ⟨Mp, g⟩ = n_2 − αm_2, ⟨Π_Pp, g⟩ = q_1 − αμ_3, ⟨g, Mg⟩ = n_3 − 2αn_2 + α²m_2, ⟨g, Π_Pg⟩ = q_2 − 2αq_1 + α²μ_3. Two
corrections. (1) The "degrees in v" at L.284 are the top degrees; the entries are inhomogeneous (α − μ_1 has degrees 0 and 1,
αμ_1 − μ_2 degrees 1 and 2, and so on). (2) Sign error in the halo reading (L.288–290 and L.374): from [M, Π_P] = P(L* − L)P +
(rank ≤ 4), −⟨p, g⟩ = ⟨p, Le⟩ − ⟨Lp, e⟩ + polar, so αμ_2 − m_2 = ⟨Πe, Le⟩ − ⟨LΠe, e⟩ + polar is right, but the archimedean
excess Arch(Πe) − α‖Πe‖² = m_2 − αμ_2 is the NEGATIVE of that pairing, not the pairing itself as the sentence says.
DOWNGRADE the verbal identity; the matrix stands. "Why it cannot be a sign step" (L.295–302) is a NUMERICAL observation
(bottom increasing in c at the tested windows) combined with Prop. 4.1; the NO-GO of §5 is correctly labelled "PROVED
mechanism + NUMERICAL confirmation" and is registered as such (class: word families of v-homogeneous generators from a
Λ-free seed below the capture dimension; Lanczos families of A below cluster resolution).

---------------------------------------------------------------------------------------------------------------------
## 3. ROUND_006_C, Theorems A–B

**Lemma 1.1 (L.40–46).** CONFIRMED. Key step: |F̂|² is the transform of c_F, supported in [−2T, 2T], so convolution with an
even φ with φ̂ = 1 there leaves it unchanged; Fubini is licensed by |m(τ − x)| ≤ C + log(2 + |τ|) + log(2 + |x|) and the
log-moment of φ. (On L²(I_T), q_T coincides with the primitive form a_T itself, ROUND_005_D Lemma 1.1; the restriction to
P_T at L.9 is only needed to compare with λ_A.)

**Theorem A (L.56–67).** CONFIRMED. Key step: on the span E of eigenvectors with eigenvalue < δ, (1/2π)∫(δ + η − s_T)_+|F̂|²
> η‖F‖²; the operator Q_T h(D) Q_T ≥ 0 is trace class with trace (T/π)∫h (prop:negtrace(i)); min–max on the finite-
dimensional E (minimum attained, strict inequality kept) gives η·dim E < tr. The bound s_min ≥ C_0 − A_T and the
interlacing m_δ ≤ m_δ^{L²} are correct. Corollary A.2 (L.72–75): CONFIRMED (2τ′ ≤ 4πe^{A_T+δ+η+1.172}, A_T ~ 4e^T).

**Lemma B.0 (L.88–98).** CONFIRMED. Key steps: unique factorisation makes the characters e^{i⟨ε(m), θ⟩} distinct, so
E|𝒫^k|² = Σb_m²; Hoeffding's lemma for mean-zero variables in [−a_p, a_p] gives E e^{±λU}, E e^{±λV} ≤ e^{λ²S_T/2}; λ² = 2k/S_T
gives EU^{2k} ≤ (2k)!(eS_T/2k)^k; (U² + V²)^k ≤ 2^{k−1}(U^{2k} + V^{2k}); n! ≤ e·n^{n+1/2}e^{−n}. Each constant was rechecked.

**Theorem B (L.100–106).** CONFIRMED. Key step: Montgomery–Vaughan with λ_m = log m over integers m < X^k carrying b_m ≠ 0,
δ_m ≥ log(1 + 1/m) ≥ 1/(m + 1), hence 3π/δ_m ≤ 3π(X^k + 1); Chebyshev at level s^{2k}. Remark B.1 (Kronecker–Weyl,
portmanteau for the closed set, Hoeffding tail e^{−s²/(2S_T)}) and S_T = 8T²(1 + o(1)) (Mertens, partial summation; the
higher prime powers give a convergent O(1)) are CONFIRMED.

**Corollaries C and D (L.118–138).** CONFIRMED (conditional only on the CITED inputs lem:mbounds(ii), PNT, Mertens). The
block exponent is g(ℓ) = ℓ − (ℓ/2T)log(eℓ/16T) from 4kS_T/(eL²) = 16T/(eℓ) at k = ℓ/2T; g(4e^T) = 2e^T(1 + (log T + log 4 −
1)/T) was recomputed; the low blocks (eℓ ≤ 16T, or ℓ < 2T where k = 0 is inadmissible) are covered by the trivial measure
bound e^{O(T)}. The class limit of L.151–156 is correctly labelled ARGUED. The Beurling remark (L.163–167) is accurate:
Theorem B uses unique factorisation and integer spacing.

---------------------------------------------------------------------------------------------------------------------
## 4. ROUND_007_C, certified witnesses and the zero-extension lemma

**Re-run (review computation (c)).** `python3 tools/falsifier_cert_run.py a3 8 1e-6`, `beur 8 1e-6`, `1.1L 12 1e-6` (python-flint,
256 bits) reproduce every printed enclosure of L.62–89:

| case | T | solved coefficient | a_T^w(F) | a_T^w(F)/‖F‖² | upper end < 0 |
|---|---|---|---|---|---|
| a_3 | ½log5 + 10⁻⁴ | x_3 = 1.0000005632467671625 ± 4.3·10⁻²⁰ | −0.47918255366 ± 6.5·10⁻¹² | −0.5052870834 ± 1.4·10⁻¹¹ | yes |
| 3 → 3.2 | ½log5 + 10⁻⁴ | x_5 = 1.0000016578009623462 ± 4.0·10⁻²⁰ | −0.2220449629 ± 1.1·10⁻¹¹ | −0.2344823412 ± 4.4·10⁻¹¹ | yes |
| 1.1Λ | 1 | x_10 = −0.99999732355597536013 ± 9.0·10⁻²² | −0.1838889227 ± 8.2·10⁻¹¹ | −0.0782440084 ± 5.6·10⁻¹¹ | yes |

The rational coefficients printed by the script coincide with those of the memo; C_0, the tail, the integral over [δ, 2T],
the [0, δ] bound and the comb part coincide to all printed digits.

**Lemma 1 (L.28–29).** CONFIRMED (definition of the infimum).

**Lemma 2, zero extension (L.31–36).** CONFIRMED. Key step: A, B, ‖·‖, c_F and the Lévy integral do not depend on the
window once F is fixed; atoms in [2T, 2T′) meet c_F ≡ 0. One precision for the Beurling case (L.36): the extension holds for
every continuation of the atom set that has no atom in (log 5, 2T) = (log 5, log 5 + 2·10⁻⁴), i.e. no generalised integer in
(5, 5.0010); "any continuation beyond 5" should read "any continuation beyond e^{2T}". For a_3 and 1.1Λ the next contacts (7
resp. 8) lie beyond e^{2T}, so nothing changes.

**Lemma 3 (L.38–50).** CONFIRMED. Key steps: parity of sin(kπ/2 + ω_k t); for even F, A = B and for odd F, B = −A, so one
condition cuts out P_T in each sector (the script solves two coefficients; the second comes out as a ball of radius
≤ 2.4·10⁻⁷⁵ around 0 and is exactly 0 by parity, so the memo's one-coefficient description of the witness is the same
function); the antiderivatives log tanh(u/4) and 2arctan e^{u/2} for the tail; for (v), the zero extension of F ∈ H¹_0 is in
H¹(ℝ), c_F″ = −c_{F′}, |c_{F′}| ≤ ‖F′‖², c_F′(0) = 0, K(u) ≤ 1/u + 1/2.

**Rigour of the enclosure.** The integrand passed to acb.integral ignores the "analytic" flag. This is acceptable here: the
integrand is (c_F(0) − c_F(u))K(u) with c_F entire (sums of sin, cos and (L − u)cos) and K meromorphic, so ball evaluation on
a box meeting a pole returns a non-finite ball and no branch cut exists; the error bounds of the Gauss–Legendre scheme are
therefore valid. The exact witness has the exact solved coefficient, which lies in the printed ball, and the value is
enclosed by evaluating on that ball.

**Theorems 1–3 (L.62–90).** CONFIRMED as PROVED upper bounds: λ_A(½log5 + 10⁻⁴; a_3) ≤ −0.50528, λ_A(½log5 + 10⁻⁴; w_{3.2}) ≤
−0.23448, λ_A(1; 1.1Λ) ≤ −0.078244, and for every larger window by Lemma 2 (with the precision above for the Beurling
continuation). Typo at L.89: "a_1(F)" should be a_T(F) at T = 1. The register consequences of §3 (L.99–120) are correctly
scoped: the Θ_T falsifiers stay NUMERICAL, 1.1Λ below T = 1 stays NUMERICAL.

---------------------------------------------------------------------------------------------------------------------
## 5. ROUND_007_B: polar-free identification, Proposition 2.4, Proposition 3.1

**Lemma 1.1 (L.53–60).** CONFIRMED. Key step: ε_T = ∫_{2T}^∞K = ∫_{2T}^∞(2e^{−u/2} + K_1) = 4e^{−T} + ∫_{2T}^∞K_1, so the −4e^{−T}
cancels; near 0, K_1(u) = 2e^{−5u/2}/(1 − e^{−2u}) ~ 1/u gives the logarithm; tails of a positive decreasing kernel are
decreasing and convex. T_0 = 0.05199 is a numerical root, correctly labelled.

**Polar-free identification: Proposition 1.2 (L.67–75) and Proposition 1.4 (L.107–116).** CONFIRMED against prop:sharp and
lem:polarelim (main.tex L.7330–7378). Key steps: ∫_0^∞(1 − cos τu)2e^{−u/2}du = 4 − 1/(¼ + τ²), hence m^♯ = C_0 + 4 + ∫_0^∞(1 −
cos τu)K_1du, and Plancherel–Fubini with c_F = 0 beyond 2T gives σ_T‖F‖² + κ(F) = 𝔞^♯(F). Two precisions. (1) Proposition 1.2
holds on all of L²(I_T), not only on P_T: no Tate condition is used, and 𝔞^♯ = Arch + 𝔢 with 𝔢(F) = (1/2π)∫|F̂|²/(¼ + τ²) is the
symbol identity m^♯ − m = 1/(¼ + τ²), not lem:polarelim (which is the statement 2∫Re c_F e^{u/2} = −𝔢 and needs P_T). (2)
Proposition 1.4, ℛ = Π + 𝔢 = 𝓕_T, does need P_T (lem:polarelim; off P_T the paper's rem:polarelim-full adds −2Re(A B̄)). The
mesh symbol 𝒮_q = (1 − (−1)^q e^T)/(¼ + ω_q²) was recomputed from e^{2iTω_q} = (−1)^q. Corollary 1.5 (L.118–122) CONFIRMED,
including the H²_0 form (F̂ = (¼ + τ²)Ĝ gives c_F = (∂² − ¼)²c_G).

**Lemma 1.3 (L.82–96).** CONFIRMED. Key steps: span{e^{±t/2}} is a two-dimensional Haar space (a nonzero element has at most one
zero), so F ⊥ 𝒯 changes sign twice; the projection of e^{iτt} onto 𝒯 uses ‖cosh(t/2)‖² = T + sinh T, ‖sinh(t/2)‖² = sinh T − T.
The expansion d_T(0) = T⁵/360 + O(T⁷) was recomputed: 16 sinh²(T/2)/(T + sinh T) = 2T − T⁵/360 + O(T⁷).

**Lemma 2.1 (L.129–133).** CONFIRMED. **Lemma 2.2 (L.142–153).** CONFIRMED as a conditional statement (simplicity assumed).
The sentence at L.354–355, "the hypothesis holds in exact arithmetic", is not proved anywhere and contradicts the header of
§2.2 (L.140, "NUMERICALLY false at the precision of any model"); simplicity of λ_A(T) is OPEN and should be labelled so.

**Proposition 2.4 (L.214–223).** CONFIRMED. Key step: linearity of F ↦ ∫Re c_F dμ in μ. The proposition is a bookkeeping
identity and carries no sign; its use in the NO-GO of §4.3(a) (the crossing depends on the Λ-free density ν booked into ℛ)
is correct. Register: NO-GO "per-minimiser budget statements / crossing window" with reason (a) PROVED (bookkeeping) and
reason (b) NUMERICAL (near-null ladder).

**Proposition 3.1 (L.241–256).** CONFIRMED by recomputing the four interval lengths. With φ_q(t) = e^{−iω_qt}/√(2T) one has
Πφ_q = φ_qψ_q and c_F(u_k) = (1/2T)k^{−iω}∫ψ_q(t) conj ψ_q(t − u_k); on t ∈ (−T + u_k, T) the four products of step functions
have lengths (2T − max(u_m, u_n + u_k))_+ (phase (m/nk)^{iω}), (2T − max(u_m, u_k) + min(0, u_k − u_n))_+ ((mn/k)^{iω}),
(2T − u_m − u_n − u_k)_+ ((mnk)^{−iω}) and (2T − max(u_m + u_k, u_n))_+ ((n/mk)^{iω}); the last equals the first after m ↔ n,
giving the weight 2; the prefactor is (1/2T)·¼ = 1/8T. The display concerns Π(Πφ_q) before projection to P_T, as stated.

**Corollary 3.2 (L.262–271).** CONFIRMED with one numerical slip: at T = ½log5 + 10⁻⁴ the triple (5; 2, 2) has weight
2T − log 5 = 2·10⁻⁴, not 0 or 10⁻⁴ (L.265–266); (5; 2, 3) and (5; 3, 2) have weight 0 there. The T = 1 weights 0.391, 0.208,
0.054 and the entry thresholds ½log 8, ½log 9 were rechecked.

**NO-GO of §3.4 (L.298–307).** ARGUED with NUMERICAL support (the cancellation of three degree parts of size 1.4·10⁻³ to
3·10⁻¹² is a model computation); the logical core ("controlling a sub-part to precision ε proves only a_T ≥ −(rest)") is
immediate. Register as NO-GO (ARGUED): sub-part arguments on the response cubic with error above λ_A.

---------------------------------------------------------------------------------------------------------------------
## 6. ROUND_007_D: Proposition 4.1 and the floor transfer

**Proposition 4.1, λ_W^{par} ≤ λ_A^{par} ≤ λ_{W,2}^{par} (L.142–148).** CONFIRMED. Key steps: W_T = 𝔞_T on 𝒬^{par}_T because
ℓ_par = 0 there (thm:parityschur(o)), so the infimum over 𝒬 dominates the infimum over 𝒟; every two-dimensional S ⊂ 𝒟 meets
ker ℓ, so sup_S W_T/‖·‖² ≥ λ_A^{par} and min–max gives the upper half. The global λ_W ≤ λ_A follows by taking minima over
the parities and is already in Paper 46 (main.tex L.132, L.4330).

**Floor transfer, Corollary 4.3 and §1(a) (L.40–52, L.171–174).** CONFIRMED as a transfer of CITED inputs. Key steps:
λ_A(T) ≥ λ_W(T) ≥ λ_W(½log15) ≥ 2^{−2904} for T ≤ ½log15, using that λ_W is nonincreasing (lem:monoT, main.tex L.534–546,
which covers λ_W explicitly); the normalisation of the cited form is the paper's W_T = 𝔞_T + 2Re(AB̄) on L²(I_T) with T = ½log μ
(AUDIT_ZENODO_FRONTIER §0, checked). Three corrections. (1) The claim that this direction "was not used in the record"
(L.31–32) is inaccurate: AUDIT_ZENODO_FRONTIER B1(a), line 13, already states "Since λ^W ≤ λ^P ≤ λ_A, it also gives
λ_A > 0 there". The transfer is a re-statement, not new. (2) The ½log15 floor inherits the status of its source: the
computational certificate was reproduced (AUDIT_ZENODO_FRONTIER §B1-run), but the analytic lemmas imported from the
log 10 / log 12 papers were not audited (same file, B1(a) proof chain and "Not done"); the label is CITED with that
caveat, and the ½log12 floor is CITED, not audited. (3) The proposed correction of Paper 46's open-problem sentence
(main.tex L.10771–10772, "beyond ½log5 no lower bound better than the trivial … is known") is legitimate in substance: a
cited complete-form certificate does give λ_A floors up to ½log15. The paper's own text already records the inequality
λ_W ≤ λ_A next to the citation (L.3589); the open-problem item should be reconciled with it.

**Proposition 4.2 (L.150–165).** (i) CONFIRMED. Key step: the Euler–Lagrange system on F = G + xh gives (A_𝒬 − μ)G = μxPh
and 𝔤x = μ(⟨G, Ph⟩ + x‖h‖²), hence φ(μ) = 0 with R(μ) ≥ 0 below λ_A^{par}. (ii) The counterexample is correct in substance
but mislabelled: in the bordered model the matrix diag(α, w) must be that of W_T (so that 𝔤 = W_T(h) = w); with 𝔞_T =
diag(−1, −5) and ε = ±1 one gets 𝔤 = −5 + 2ε, and still λ_W − 𝔤/‖h‖² = 0 > λ_A = −1. Notational slip only.

**Lemma 4.6 and Corollary 4.7 (L.193–227).** CONFIRMED. Key steps: monotonicity of 𝒲 on (μ_0, μ_1); the bulk bound uses μ_k >
δ > L off the cluster; for 4.7, D is decreasing on (μ_0, μ_1), so 𝒲((1 − η)L) ≤ −D(L) + τ_1²/(ηL) ≤ 0. The proof text
contains an abandoned line (L.217–219, "fails to be the right comparison; argue instead") that should be removed. L.207–209
uses |σ_T|, which REVIEW_004 restricted to T > T_0 = 0.052; harmless on the windows considered.

**Proposition 4.4 (L.176–179).** CONDITIONAL, correctly labelled; the arithmetic −log(c^{9/2}e^{−2c}) at c = 2πe^{2T} gives
4πe^{2T} − 9T + O(1) and was rechecked.

**§2, §5, §6.** NUMERICAL, labelled so. Note for the record: §3(b) "λ_W^{ev} = 𝔤/‖h‖² to 7–8 digits" is consistent with the
review's finding in §1 above that W_ev(0) + ½ tracks λ^W_{T,ev}.

---------------------------------------------------------------------------------------------------------------------
## 7. ROUND_008_D

**Proposition 1, a_CE = Arch_CE − Π_CE P_V (L.30–37).** CONFIRMED relative to ROUND_005_C Theorem 2(iii) with the REVIEW_004
correction (Tate responses included in V_T): for x ∈ N′, Π_Px lies in V_T ⊂ E, so P_CΠx = 0 and the coupling from N′ is
archimedean; for y ∈ V_T, Π_Py has a component in C (the second responses). So "a_EC = Arch_EC" holds on N′ only, as the
memo says; the numerical check ‖Π_{C,N′}‖ ≤ 6.6·10⁻⁵⁰ is consistent. Label: PROVED given the cited structural theorem.

**Theorem 2, Neumann expansion with tail bounds (L.39–62).** CONFIRMED as CONDITIONAL on (H₋); (H₋) is correctly OPEN (L.65–67).
Key steps: (H₊) and (H₋) say ±Π_CC ≺ Arch_CC, i.e. |⟨Xu, u⟩| < ‖u‖²; X = Arch_CC^{−1/2}Π_CCArch_CC^{−1/2} is compact and self-
adjoint, so its eigenvalues lie strictly inside (−1, 1) and ‖X‖ = ρ(X) = r < 1; a_CC = Arch_CC^{1/2}(1 − X)Arch_CC^{1/2};
Arch_CC^{−1/2}X^kArch_CC^{−1/2} = Arch_CC^{−1}(Π_CCArch_CC^{−1})^k; S_E − S_E^{(K)} = −W*f_K(X)W; on [0, r_+], 0 ≤ f_K ≤
r_+^{K+1}/(1 − r_+), on [−r_−, 0], |f_K| ≤ r_−^{K+1}/(1 + r_−) (t^{K+1}/(1 + t) increasing), giving the two-sided bound; for odd K,
f_K ≥ 0 gives S_E ⪯ S_E^{(K)}; the weighted-norm statement in (i) is ‖Arch^{−1/2}YArch^{1/2}‖ = ‖X‖. The degree count (iv) is
correct with E and C frozen. Two precisions. (1) The separate hypothesis "Arch_CC ≻ 0" is redundant: adding (H₊) and (H₋)
gives 2Arch_CC ≻ 0. (2) (H₊) is attributed to ROUND_002_A Theorem F (L.64); that attribution was not re-verified in this
review (CITED, in-phase).

**Corollary 3 (L.71–76).** DOWNGRADE. The stated "only if" is too strong. The certificate 𝒫_K ⪰ 0 fails at the bottom vector u of
S_E exactly when ⟨(ε_K − f_K(X))Wu, Wu⟩ > λ_A, which involves ‖Wu‖² and the slack ε_K − f_K on the spectral measure of Wu, not
‖W*W‖; so ε_K‖W*W‖ < λ_A is sufficient for the tail term to be harmless, not necessary for 𝒫_K ⪰ 0. The displayed K is a
worst-case estimate (as §3(c) correctly calls it); the conclusion "degree grows like log(1/λ_A)" is ARGUED for this
certificate scheme, and is supported NUMERICALLY by the measured K* (§3 table).

**Falsifier reading (L.152–157).** REFUTED in its quantitative claim. By Theorem 2(iii), for odd K, S_E ⪯ S_E^{(K)}; hence a
negative eigenvalue of S_E^{(1)} already proves (under (H₋) for that comb) that S_E has a negative direction, with no tail
cost. Since S^{(K)} for 1.01Λ is "constant to 4 digits" at ≈ −0.0138 for K = 0 … 7, the rejection of 1.01Λ costs K = 1, not
"K ≈ 7"; the same holds for 1.1Λ and a_3. The degree gap stated at L.155 ("K ≈ 7 against K ≈ 84") should read "K = 1 against
K ≈ 84 (worst case) / 25–30 (measured)". The qualitative reading (rejecting falsifiers is cheap, certifying Λ is expensive)
is reinforced.

**Proposition 4 (L.161–167).** CONFIRMED as stated, i.e. CONDITIONAL on (H₋) on the frozen C, and only at the level of the
Galerkin space P_T^{(N)} with V, C frozen at their Λ-values. Key step: 𝒫_K = S_E^{(K)} − ε_KW*W ⪯ S_E, then the Schur lemma
(S_E ⪰ 0 and a_CC ≻ 0 give a_T ⪰ 0 on E ⊕ C). As the memo says (L.176–178), nonnegativity on a Galerkin subspace gives no
lower bound for λ_A (Galerkin minima are upper bounds), so the proposition is not a statement about a_T; ε_K(v) is not
polynomial in v. The falsifier test (c) Beurling was not run.

---------------------------------------------------------------------------------------------------------------------
## 8. Summary of verdicts on PROVED claims

| memo | claim | verdict |
|---|---|---|
| 005_D | Lemma 1.1, Prop. 1.2(v)(vi), Thm 2.1, Cor. 2.2 (equivalence), Thm 3.1, Cor. 3.2, Cor. 3.3, Prop. 4.2 | CONFIRMED |
| 005_D | Cor. 2.2, parenthetical "μ_0 < 0 by prop:archneg" (L.155–156) | REFUTED as cited; DOWNGRADE to NUMERICAL |
| 005_D | Prop. 1.2(vii) | DOWNGRADE to ARGUED/NUMERICAL |
| 005_D | W_ev(0) = −½, W_odd(0) = +½ | exact identity REFUTED; near-degeneracy tracking λ^W_{T,par} (NUMERICAL) |
| 005_D | Thm 6.1 (𝒦_gap) | DOWNGRADE to ARGUED; window-restricted |
| 006_B | Prop. 4.1 set invariance | CONFIRMED; Danskin "requires a minimiser" clause REFUTED |
| 006_B | Prop. 4.2(i)(ii), Prop. 4.3 | CONFIRMED (4.2(ii) constant uncontrolled) |
| 006_B | Prop. 4.4 matrix 𝔄_3 | CONFIRMED; verbal halo identity has a sign error (DOWNGRADE) |
| 006_C | Lemma 1.1, Thm A, Cor. A.1–A.2, Lemma B.0, Thm B, Remark B.1, Cor. C, Cor. D | CONFIRMED |
| 007_C | Lemmas 1–3, Thms 1–3 (re-run reproduced) | CONFIRMED; Beurling continuation must avoid (5, e^{2T}) |
| 007_B | Lemma 1.1, Prop. 1.2, Lemma 1.3, Prop. 1.4, Cor. 1.5, Lemma 2.1, Lemma 2.2 (conditional), Prop. 2.4, Prop. 3.1 | CONFIRMED |
| 007_B | "simplicity holds in exact arithmetic" (L.354) | unproved; OPEN |
| 007_B | Cor. 3.2(iii) weight of (5; 2, 2) at ½log5 + 10⁻⁴ | slip (2·10⁻⁴) |
| 007_D | Prop. 4.1, Cor. 4.3 transfer, Prop. 4.2(i), Lemma 4.6, Cor. 4.7 | CONFIRMED (transfer not new; ½log15 floor CITED with unaudited analytic lemmas) |
| 008_D | Prop. 1, Thm 2 (conditional on (H₋), OPEN), Prop. 4 (conditional, Galerkin level) | CONFIRMED |
| 008_D | Cor. 3 "only if" | DOWNGRADE (worst-case estimate) |
| 008_D | falsifier certificate cost "K ≈ 7" | REFUTED (odd K = 1 suffices) |

## 9. NO-GO register (as they should be entered)

| memo / place | class | status |
|---|---|---|
| 005_D Thm 6.1 | lower bounds on the spectral gap of the h_T-transformed jump form with a comb-independent loss, at windows where λ_A^{ev}/|μ_0| is below the loss | NO-GO (ARGUED; tautological core, membership of the listed tools asserted) |
| 006_B §5 | word families of v-homogeneous generators from a Λ-free seed below the capture dimension; Lanczos families of A below cluster resolution | NO-GO (PROVED mechanism: set invariance; NUMERICAL capture data) |
| 006_C §4 | Theorem A + moment/large-values bounds with off-diagonal error controlled by the integer spacing: cap stays exp(2e^T(1 + o(1))) | class limit ARGUED |
| 007_B §4.3 | per-minimiser budget statements, crossing window T_× | NO-GO (bookkeeping dependence PROVED; ladder NUMERICAL) |
| 007_B §3.4 | signing a proper sub-part of the response cubic with error above λ_A | NO-GO (ARGUED + NUMERICAL) |
| 007_D §6 | fitted laws as sign carriers; lower half not weaker than (★) at margin exp(−4πe^{2T}) | NUMERICAL |
| 008_D Result | finite-degree Neumann truncation of the Schur coupling on E_T with tail bounded by ρ(X) | NO-GO (ARGUED + NUMERICAL; Thm 2 conditional on (H₋), OPEN) |
