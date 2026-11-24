# Review of STATEMENT_001 and DOSSIER_001 against Paper 46

References P46:n are to lines of 04-papers/46-row-d-sign-radial-intersection-form/main.tex; P48:n to 04-papers/48-routes-to-weil-positivity/main.tex.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Part 1. STATEMENT_001

### 1.1 Section 1 (definitions)
s_T, a_T, P_T, K, C_0 and the Lévy form agree with Lemma lem:K (P46:395–410, eq:m) and Theorem thm:A (eq:Aform, P46:444–452).
No discrepancy.

### 1.2 Section 2 (profile)
Definitions agree with P46:7760–7771 (T_0 = 2a, supp G_0 ⊂ [−T_0,T_0], supp c_0 ⊂ [−2T_0,2T_0]). F_0 is not normalised there.
The decomposition A_M = Arch_M − Div_M − Near_M carries over the normalisation gap of prop:AM (see 2.(b)). It is correct only with
Div_M multiplied by c_0(0) = ‖F_0‖², or with ‖F_0‖ = 1.

### 1.3 Section 3 (archimedean term as an exponential sum): CONFIRMED, with three corrections
Archimedean term. From eq:m and Plancherel (ĉ_0 = F̂_0², because F̂_0 is real and positive),
(1/2π)∫ m F̂_0² cos(τd) dτ = C_0 c_0(d) + ∫_0^∞ K(u)[c_0(d) − ½c_0(d−u) − ½c_0(d+u)] du.
For d > 2T_0 one has c_0(d) = c_0(d+u) = 0, so the term equals −½∫_0^∞ K(u) c_0(d−u) du = −½∫ K(d−v) c_0(v) dv.
The equality is valid because d − v > 0 on supp c_0. The expansion K = 2Σ_j e^{−(2j+½)u} gives the stated sum with constant 1.
The j = 0 term is ∫e^{v/2}c_0 = A(F_0)B(F_0) = 0. The constants agree with lem:transl(iv) (P46:7690–7693) and with the
cross term in the proof of thm:band (P46:7716–7718), where B(D) = −X_ν(D)/2.

Prime term. For d ≥ 0 and n ≥ 2: log n + d ≥ log 2 > 2T_0, so c_0(log n + d) = 0. This claim is CONFIRMED (it needs 2T_0 < log 2).
Then −½Σ v_n c_0(log n − d) = −x^{−1/2} Σ Λ(n) φ(n/x) with φ(y) = y^{−1/2}c_0(log y).

Moments. ∫φ dy = ∫e^{u/2}c_0 = AB = 0 and ∫φ dy/y = ∫e^{−u/2}c_0 = 0. CONFIRMED.

Corrections:
(i) The support claim [e^{−2T_0}, e^{2T_0}] ⊂ (½, 2) needs 2T_0 < log 2. Section 3 does not restate this hypothesis.
(ii) Section 3 is not new. It is lem:transl(iv) together with thm:band (P46:7699–7728), up to normalisation. In that notation
Ξ_{F_0}(log x) = 2x^{−1/2}Σ Λ(n)φ(n/x). The label "PROVED here" should be "PROVED (P46 lem:transl(iv), thm:band)".
(iii) The tail Σ_{j≥1} γ_j x^{−(2j+½)} is O(x^{−5/2}) with the explicit bound of lem:transl(iv) times ‖F_0‖². CONFIRMED.

Bochner consequence. If (★) holds then thm:oneprofile gives that B is positive definite, hence |B(d)| ≤ B(0) = a(F_0, F_0)
(PROVED, standard). This yields |Σ Λ(n) φ(n/x)| ≤ a(F_0)√x + O(x^{−2}). It is exactly the band of thm:band, the 2×2 case.
Three errors:
- "for all x" must read "for x > e^{2T_0}". For smaller x the formula of Section 3 does not apply.
- "square-root cancellation with sign" is wrong. The bound is two-sided in absolute value and carries no sign.
- "This is Problem (N) of Paper 46 in its sharpest form; it is not a detour, it is the content" is unsupported. Problem (N)
  (P46:10695–10707) is a signed Nyquist coherence bound correlated with the admissible samples of P_T. The band is only a
  necessary 2×2 condition, as P46:7748 states. The sentence must be deleted or labelled ARGUED and weakened to "necessary".

NUMERICAL paragraph: acceptable as labelled.

## Part 2. DOSSIER_001 §6

### (a) eq:coer-sandwich and lem:wh-schurabs(ii) when λ_S < 0 — CONFIRMED, with one refinement
The proof was checked. Take F = v + e, with v and e orthogonal, and a_T(v+Ke) ≥ c‖v+Ke‖² ≥ 0.
- Lower bound. a_T(F) ≥ s(e) ≥ λ_S‖e‖² ≥ λ_S‖F‖² when λ_S < 0. So λ_A ≥ λ_S.
- Upper bound. Take v = −Ke_S. Then a_T(F) = λ_S and ‖F‖² = 1 + ‖Ke_S‖², so λ_A ≤ λ_S/(1+‖Ke_S‖²).

Consequences:
- The upper bound λ_A ≤ λ_S printed at P46:5257 is false whenever Ke_S ≠ 0. A minimising sequence would need ‖e‖ → ‖F‖,
  which forces Ke → 0.
- The lower bound λ_S/(1+‖K‖)² ≤ λ_A is false whenever K ≠ 0, because λ_S/(1+‖K‖)² > λ_S/(1+‖Ke_S‖²) ≥ λ_A.
  Refinement: the lower bound fails even if Ke_S = 0 but K ≠ 0. The dossier's "unless Ke_S = 0" applies to the upper bound only.
- The faulty steps are at P46:5274–5278 ("‖F‖² ≥ ‖e‖², so λ_A ≤ λ_S", and "if λ_S ≤ 0 the lower bound is implied") and
  P46:5701–5703. At P46:5703 the bound min{c,λ_S}(a²+‖e‖²) ≥ min{c,λ_S}‖F‖²/(1+k)² is used, which multiplies by a negative
  number. The "moreover" clauses of lem:wh-schurabs (P46:5690–5692) are correct.
- The same unqualified "λ_A ≤ λ_S" is repeated at P46:5303 (rem:coer-honest(2), restricted only to λ_S ≤ c) and at
  P46:10687–10688 ((L2)). Both need the qualifier λ_S ≥ 0.
- Uses at P46:5727–5732, 8940–8962 and 9146 assume λ_A ≥ 0 or λ_A > 0 and are unaffected. The same holds for thm:coer-schur(iii).
  Its "if" direction for λ_S < 0 follows from the corrected upper bound.

### (b) Normalisation of F_0 — CONFIRMED
P46:7762–7769 defines F_0 without a norm. P46:7835 uses c_0(0) = 1, but c_0(0) = ‖F_0‖². lem:transl and thm:band
(P46:7683, 7700) assume ‖F_0‖ = 1. As printed, (Div_M + Near_M)_{mk} = ½Ξ_{F_0}(log m/k) is consistent with Ξ only if the
Div entries are v_{m/k}‖F_0‖²/2. Positive definiteness is scale-invariant, so thm:oneprofile and prop:AM(i),(ii) are unaffected.
Fix: impose ‖F_0‖ = 1, or write c_0(0) in Div_M.

### (c) "exactly one negative eigenvalue for every window" — CONFIRMED
The dossier's proof was checked. For F ∈ L²(I_T), |F̂(τ)|² ≤ ‖F‖_1² ≤ 2T‖F‖², so (1/2π)∫_{|τ|<R}|F̂|² ≤ (2TR/π)‖F‖².
With 2T < log 2 there is no comb, m ≥ C_0, and m is increasing in |τ|. This gives
a_T(F) ≥ [m(R)(1 − 2TR/π) + C_0·2TR/π]‖F‖², which is positive for suitable R once T is small.
So n_−(A_ev(T)) = 0 for small T. The final sentence of prop:H (P46:6567–6569) and P48 thm:eveninertia(iii) (P48:207) are false
as printed. The correct statements are "≤ 1 for all T", or "= 1 for all T ≥ 0.12" (cor:H1minus, P46:6546).
P48 (ii) (P48:205–206) omits the alternative "n_− = 0 and q > −½" of prop:WT (P46:6511–6512). It also omits T ≥ 0.12.

### (d) Comb-genericity of the half-line identity — CONFIRMED as a defect of P46; the dossier's stronger conclusion is ARGUED
P46:10654–10657 asserts that the half-line identity holds for cΛ, for prime deletions and for Beurling systems. No proof is given.
The proof of thm:ext-half (P46:9921–9932) rests on Guo's radical lemma, i.e. Φ_f lying in the radical of the full Weil
distribution. That is specific to the summation map with coefficients 1 and to ζ. No analogue for cΛ or for Beurling systems
is proved anywhere in the paper.
Mis-citation: the dossier quotes P46:10146 as concerning the half-line identity. That sentence concerns the mirror and EM
identity that precedes it, not thm:ext-half. The conclusion survives on the ground stated above.
The conclusion "the exterior form is not comb-generic" is ARGUED, not PROVED. Showing it would require that no radical identity
exists for cΛ, and that is not shown. Item 2 of §ext-constraints should be restricted to the algebraic identities, or proved.

### (e) Arithmetic squares on (½log2, ½log3) — CONFIRMED for the reduction; NUMERICAL and undetermined for the value
- N_T = {2}. The first condition of thm:sos (P46:8441–8444) forces μ_0 ≥ v_2. The second is λ^{∞,P}_min(T) ≥ μ_0.
- Conversely, with μ_0 = v_2: v_2(1 − cos θ) = |x_1 + x_2 e^{iθ}|² with x_1 = −x_2 = (v_2/2)^{1/2}, a Dirichlet polynomial on {1, 2}.
- So a decomposition exists iff λ^{∞,P}_min(T) ≥ v_2 = √2 log 2 = 0.98026. PROVED.
- Misreading: rem:directbound (P46:7909–7914) does not give "λ^{∞,P}_min ≈ 0.49 at T ≈ 0.367". It says the bound of
  cor:directbound is positive only where λ^{∞,P}_min > 0.49, and that this holds numerically up to T ≈ 0.367. The value at that
  T is consistent with 0.49, but no value at T = ½log2⁺ is given.
- Whether λ^{∞,P}_min(½log2⁺) ≥ v_2 is therefore OPEN (NUMERICAL). The claim at §6(i) that the clause "becomes vacuous"
  is CONDITIONAL on that number.

### (f) Monotonicity of n_−(A_ev(T)) — CONFIRMED for monotonicity; UNDECIDED for the "birth window"
Monotonicity. Extension by zero keeps parity and the form domain. Comb terms with log n ≥ 2T see c_F(log n) = 0. So values are
preserved (lem:monoT), and min–max gives that n_− is nondecreasing. PROVED.
Birth window. The existence at T_2 of a nonzero kernel vector needs continuity, from both sides, of the second eigenvalue of
A_ev(T) in T. That is an analogue of lem:contA for the unconstrained even form, and it is not proved. The phrase
"orthogonal (in A_ev) to χ_ev" is vacuous for a kernel vector and must be made precise. The restatement of prop:H is correct
once (c) is applied.

### (g) Fixed-window content of Problem ext-L and leakage prediction — CONFIRMED with qualifiers
- If λ^W_T > 0, then W_T(g) ≥ λ^W_T‖g‖² ≥ (λ^W_T/(C_1N²)) ℓ(g) by lem:ext-ellbound (P46:9959–9961). So eq:ext-L holds at that T
  with A_0 = 2. The only open part is uniformity, as for prop:ext-base. PROVED.
  This is CONDITIONAL on λ^W_T > 0, which is itself unknown beyond the certified range.
- Prediction. Since λ^W ≤ λ_A ≤ 4·10⁹ T N^{−7.7245} (cor:margin1, P46:3561–3565; e^{−15.449T} = N^{−7.7245}), eq:ext-L gives
  ℓ(g) ≤ (4·10⁹T/κ) N^{A_0−7.72} for unit g with W_T(g) ≤ λ^W + o. This requires T ≥ 1, g in the core, and near-minimisers
  of W_T (not of a_T). The dossier writes λ_A and does not specify the form; correct this.
- 1 − χ_0(2πN) ~ e^{−4πN} = e^{−4πe^{2T}}: doubly exponential in T. CONFIRMED.
- "almost band-limited" is interpretive (ARGUED).

### (h) Two-sector reduction with η ↓ 0 — partly REFUTED
- thm:nyq-schur(ii) holds for every η > 0 as stated (P46:6355, 6367–6375). CONFIRMED.
- Correction: for η below the least positive sample, d_η counts samples with s_T(ω_k) ≤ 0, not < 0. Also dim N'_η ≤ d_η.
  Positive samples have no accumulation at 0 because s_T → ∞.
- Count. With ω_k = πk/(2T), the samples in [0, τ_last] number at most (2T/π)τ_last + 1 over both sectors. The dossier's
  (4T/π)τ_last + 1 is a valid but loose bound.
- REFUTED: the claim that this is "a smaller exact finite reduction than (L2) [...] already proved". By prop:band(v)
  (P46:2878), τ_last ≤ τ^lo with τ^lo > 2πe^{A_T}. So the proved bound is about 4T e^{A_T}, against 2k − 2 ≈ 2T e^{A_T + 1.64}
  for (L2): the same order. A smaller dimension holds only if the Nyquist non-positive set is sparse, which is OPEN, as the
  dossier itself says.
- As η ↓ 0, c_η falls to half the least positive sample, which may be arbitrarily small. The entries of S_η are, like those
  of S_{T,k}, infima over an infinite-dimensional complement, not closed forms.
- The reading of rem:nyq-schur-num (large d_η driven by S^low) is CONFIRMED.
- Proposing (L2′) is premature until the sparsity is settled.

### Further remark on §6(j)
The statement "No step labelled PROVED was found to rely on an unproved claim beyond (a)" is incorrect. Item (c) is a false
sentence inside a proposition labelled "proved", and item (b) is a constant error inside a PROVED proposition.

## Part 3. Sandbox-rule check
Strict reading of the rule (no equivalence of window positivity with any other statement):
- STATEMENT_001 lines 35–36 state two equivalences: (★) ⇔ B positive definite, and (★) ⇔ A_M ⪰ 0 for all M.
- DOSSIER_001 states equivalences at lines 31–32, 46, 58, 71, 73, 79–87 (including Kreĭn indeterminacy at 87), 115, 117, 122,
  124, 330, 365, 380 and 472.
- All of these are internal reformulations of the window form taken from P46. None is an equivalence with a statement about
  zeros. If the sandbox admits internal reformulations, they are permitted; if not, every one is a violation.
- No line in either document invokes an equivalence with a statement about zeros of ζ.
- Zero-side material appears only as tools: DOSSIER lines 158, 170, 235, 254, 472–474. Lines 472–474 (the zero-side reading
  and the zero sum in prop:H) are the closest to the boundary. They use identities, not equivalences, and are admissible as tool use.
- STATEMENT line 75 and DOSSIER lines 230–241 (the factor ζ(½+iτ)) describe a route and invoke no equivalence.
