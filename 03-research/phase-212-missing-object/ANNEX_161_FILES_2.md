# Annex: file-by-file reading of phase 161, part R161_028 – R161_055

Complete reading of the 28 files of the part, in order. Notation of the memos: τ_a f(t) = f(t+a);
J f(t) = f(−t); 𝓕 (Fcal) the additive logarithmic Fourier transform, which in Mellin acts as
reflection with unimodular multiplier u = u_∞; X = M_t (multiplication by t); M = X + 𝓕X𝓕 (Gamma
multiplier); S_N = Σ_{n≤N} n^{−1/2}τ_{log n}; C_N the continuous (polar) Euler–Maclaurin counterpart;
S_N^ren = Z_N = S_N − C_N; L_M = Σ_{d≤M} Λ(d)d^{−1/2}τ_{log d}; K_N = Σ_{k≤N}(log k)k^{−1/2}τ_{log k}
= −[X, S_N]; H_{M,N} the hyperbola tail (K_N = L_M S_N − H_{M,N} for M ≥ N); E_N = S_N𝓕 − JS_N
(Poisson defect); (PC) / (PC-ren) the finite Poisson–Chebyshev identity and its renormalized version;
P = P_T projection onto the window [−T, T]; Π_T primitive projection; Tate: φ_± = e^{±t/2}.
«First contact» = hypothetical primitive radical vector F ≠ 0 of parity ε (JF = εF) in the critical window.
Labels: the one the memo gives itself is recorded; when the reading does not uphold it, this is said separately.

Several memos (036, 037) work with the zeta function, its functional equation and, in 036, with the evaluation
at its zeros; this is recorded neutrally as «uses the complete function and its functional equation / uses an
evaluation at zeros» without developing it. Several memos (039, 051) state that their terminal target «has the
logical strength of closing row D» relative to the imported first-contact reduction: it is an
internal equivalence of the architecture of row D, not with any external statement.

---

## R161_028 — The Euler–Maclaurin polar layer is exactly the exterior image

Object. N = e^a; C_a(s) = e^{a(1−s)}/(1−s); in physical space (C_aF)(t) = e^{−t/2}∫_{−∞}^{t+a} e^{y/2}F(y)dy;
with (VF)(t) = e^{−t/2}∫_{−∞}^t e^{y/2}F, C_a = e^{a/2}τ_aV and (1.5) ∂_aC_a = e^{a/2}τ_a.
If supp F ⊂ [−T,T] and the positive Tate moment ∫e^{y/2}F = 0, then supp C_aF ⊂ [−T−a, T−a]; with
a = 2(T+δ), supp ⊂ [−3T−2δ, −T−2δ] (image interval of R161_027). Image operator M_{T,δ} = τ_aJ.
Theorem 3.1: if JF = εF, ∂_a(C_aF) = ε e^{a/2} M_{T,δ}F. Gamma energy (4.1)–(4.2):
B^Γ = ⟨F, K_Γ^+ M_{T,δ}F⟩ = ε e^{−a/2}⟨F, K_Γ^+ ∂_a(C_aF)⟩; D^Γ_{T,δ} = −½∂_δ{…}.
Comb with continuous cutoff S_a = Σ_{n≤e^a} n^{−1/2}τ_{log n}, discrepancy Z_a = S_a − C_a: continuous velocity
−e^{a/2}τ_a between births, jumps n^{−1/2}τ_{log n} at a = log n.
Statements. PROVED: (1.5), support (2.2)–(2.4), Theorem 3.1, (4.2) as a rewriting, velocities and jumps of
Z_a. Upheld (elementary computations checked). OPEN: L161.11, identity «0 = 2D^Γ + D^Poisson_a,
D^Poisson_a ≥ 0» (6.1) at a = 2(T+δ) or after positive averaging in δ.
Stop. The ordinary derivative of ‖S_a − C_a‖² contains an uncontrolled cross term; the orientation
would have to come from (PC-ren) and from the terminal jumps of the hyperbola. Corrected/sharpened in R161_029.
Cross-check. U1 no. U2 yes, partially: uses the support of the window and the Tate law (vanishing moment) to locate
the polar layer outside the window; it builds no leakage ‖(I−P)·‖². U3 no. U4 no. U5 no.

## R161_029 — Sign audit of the moving discrepancy

Object. N_f(a) = ‖Z_a f‖². Between births (2.2) N_f′(a) = −2e^{a/2}Re⟨Z_a f, τ_a f⟩. Jump at a = log n:
(3.2) N_f(a_n+) − N_f(a_n−) = 2n^{−1/2}Re⟨Z_− f, τ_{log n}f⟩ + n^{−1}‖f‖². Primitive family
H_a = Π P Z_a^*Z_a P Π ⪰ 0; if F is radical, a_T(F, H_aF) = 0 for all a.
Statements. PROVED / INDEFINITE: (2.2) and (3.2). FALSE: monotonicity of the ordinary discrepancy (NUMERICAL
falsifier: oscillation in `161_02_poisson_defect_probe.py`). REJECTED AS TAUTOLOGICAL: deriving (4.2).
IDENTIFIED: L161.11 = inverted Tate-centred Markov pullback of R161_016. OPEN/TERMINAL: two-orientation
quadratic form defined by the source that replaces the cross terms by
2D^Γ + D^Poisson_a, D^Poisson ≥ 0, and vanishes at first contact.
Stop. The cross terms Re⟨Z_a f, τ_a f⟩ have no sign; weighting them with positive Chebyshev coefficients
does not resolve it. Radicality against H_aF is the tautology of R161_023.
Cross-check. U1 no. U2 yes: H_a uses the compression P and Π (words of type Q V Q), declared tautological; expanding
the projection reintroduces the moving Tate and exterior boundary terms (phase 121). U3 no. U4 no. U5 no.

## R161_030 — Oriented divisor variance (the algebraic gate)

Object. Hilbert H; k ≥ 2; w_d = Λ(d) for d | k; W_k = Σ_{d|k} w_d = log k. Two vectors x_d^± per path;
m_d = (x_d^+ + x_d^−)/2, r_d = (x_d^+ − x_d^−)/2.
Theorem 1.1 (PROVED):
  (W_k/2)Σ_d w_d(‖x_d^+‖² + ‖x_d^−‖²) − ‖Σ_d w_d m_d‖²
    = W_k Σ_d w_d‖r_d‖² + ½Σ_{d,e} w_d w_e‖m_d − m_e‖²,              (1.1)
with equality ⟺ x_d^+ = x_d^− and m_d = m_e for all active d, e. Proof: parallelogram
(‖x^+‖² + ‖x^−‖²)/2 = ‖m‖² + ‖r‖² and weighted variance W Σw‖m‖² − ‖Σwm‖² = ½ΣΣw_dw_e‖m_d − m_e‖².
Checked line by line: correct. Reading remark: the identity is generic in the weights
(it holds for any w ≥ 0 with W_k := Σw_d); Λ enters only when writing W_k = log k.
Prime k = p: left side = (log p)²‖x_p^+ − x_p^−‖²/4 (2.1): the fibre of a single divisor keeps the
difference of orientations; it is declared that this avoids the root-diagonal obstruction of
P121_CMO_SOURCE_MATRIX_NO_GO. Interpretation as total variance Var X = E_D Var(X|D) + Var_D E[X|D] with
P(D = d | k) = Λ(d)/log k.
Gate (4.2) (OPEN/TERMINAL): build source-defined x_{k,d}^±(F), whose difference is the projected Poisson
defect and whose weighted mean is the coherent Chebyshev port, and prove the saturation
Σ_k[(log k)/2 Σ_dΛ(d)(‖x^+‖² + ‖x^−‖²) − ‖Σ_dΛ(d)m_{k,d}‖²] = 0 at first contact.
Statements. PROVED: (1.1), equality kernel, survival on prime fibres. «PROVED ALGEBRAICALLY»: escape
from the root diagonal (upheld only as algebra; there is no realization). OPEN: realization by vectors of
(PC-ren) and saturation (4.2).
Stop. §5: (4.2) does not follow from (1.1); claiming that radicality annuls it would repeat R161_023 (the
radicality annuls a linear primitive test, not an arbitrary second moment of the source).
Corrected by. R161_031 (realization by paths), R161_033 (withdraws the realization of the direct-sum norm),
R161_035 (replaces it with the coherent version).
Cross-check. U1 yes in form, not in mechanism: the term ½ΣΣ w_dw_e‖m_d − m_e‖² is of degree 2 in the weight and
enters ADDITIVELY; but it vanishes (R161_031) by coherence of the translations τ_{log d}τ_{log e} = τ_{log k}, for
any weight, not by Σ_{d|n}Λ(d) = log n. Identity (1.1) is valid for every weight vector (it carries no
sign specific to Λ). U2 no. U3 no. U4 no. U5 no (precedes U5).

## R161_031 — Realization by paths: the divisor seam collapses and the Poisson seam survives

Object. For de = k and f in the common core: x_{k,d}^−(f) = k^{−1/2}Jτ_{log k}f, x_{k,d}^+(f) = k^{−1/2}τ_{log k}𝓕f
(outputs of the two non-recombined terms J L_M S_N and L_M S_N 𝓕 of (PC), by
Jτ_{log d}τ_{log e} = Jτ_{log k}). On complete fibres k ≤ N ≤ M, Σ_{d|k}Λ(d) = log k gives
Σ_dΛ(d)x^∓ = k^{−1/2}(log k)·(Jτ_{log k}f, τ_{log k}𝓕f); summing: JK_Nf and K_N𝓕f.
Since x^± do not depend on d, m_{k,d} − m_{k,e} = 0 and (1.1) of 030 gives (3.2):
  (log k)/2 Σ_dΛ(d)(‖x^+‖² + ‖x^−‖²) − ‖Σ_dΛ(d)m_{k,d}‖² = (log k)²/(4k)‖τ_{log k}𝓕f − Jτ_{log k}f‖².
Checked: correct (W_kΣΛ(d)‖r‖² with ‖r‖² = ‖Δ_kf‖²/(4k)). Δ_k = τ_{log k}𝓕 − Jτ_{log k};
D^orient_{M,N}(f) = ¼Σ_{2≤k≤N}(log k)²/k ‖Δ_kf‖² ≥ 0 (4.2) — direct sum, NOT ‖K_N𝓕 − JK_N‖².
Expected form of the closure (5.2): 0 = 2D^Γ_{T,δ}(F) + D^orient_{M,N}(F) + boundary_{M,N,T,δ}(F), with
boundary = 0 at first contact (5.3) (OPEN).
Statements. BUILT: x^±. PROVED: use of Λ∗1 = log on complete fibres; collapse of the seam.
«DEFINED AND POSITIVE; REALIZATION OF THE SOURCE NORM OPEN»: (4.2). PROVED by 026–028: continuous component.
OPEN/TERMINAL: crossed Tate saturation.
Reading: the initial verdict («the required vectors are identified») is correct; the sentence of §0
about complete realization is withdrawn by R161_033 (the memo itself already refers to 033).
Stop. (PC-ren) contains the coherent synthesis Σ_k, not the direct-sum norm; the
boundary identity (5.3) is missing.
Cross-check. U1: the use of Λ∗1 = log is linear (synthesis of K_N); the quadratic term in the weight disappears by
coherence, for every weight. It is not U1. U2 no (still without compression). U3 no. U4 no: it says explicitly
«no Möbius elimination is used». U5: it states the need (the direct-sum norm).

## R161_032 — Parity makes the crossed Tate block positive

Object. Tate basis (φ_−, φ_+) = (e^{−t/2}, e^{t/2}) in L²(−T,T):
G_T = 2[[sinh T, T],[T, sinh T]] (Gram), C = [[0,1],[1,0]] (exchange),
A_T^cross = G_TC = 2[[T, sinh T],[sinh T, T]]; G_T and C commute. First-contact forcing
r = αφ_− + βφ_+, v = (α, β)ᵗ, Cv = εv (parity PROVED in phase 121).
Theorem 2.1 (PROVED): ε⟨v, G_TCv⟩ = ⟨v, G_Tv⟩ = ‖r‖²_{L²(−T,T)}; for v = c(1, ε)ᵗ, ‖r‖² = 4|c|²(sinh T + εT) > 0.
Checked (∫_{−T}^T e^{∓t} = 2 sinh T, ∫1 = 2T). Collar current (phase 121) j = (J_+, J_−)ᵗ = G_TCv;
(3.2) ε⟨v, j⟩ = ‖r‖². Scattering defect (R161_021) X_T(F) = ‖g‖² + ε⟨g, C_log g⟩ = ½‖(I + εC_log)g‖².
Candidate identity (4.2):
  0 = X_T(F) + ‖r‖² + D_T^orient(F) + 2D^Γ_{T,δ}(F),
a sum of nonnegatives that would force X_T = 0, r = 0, D^orient = 0, D^Γ = 0.
Statements. PROVED: (2.2), (3.2), «conditional compatibility with the scattering sign». OPEN/TERMINAL:
the finite Green accounting identity (4.2).
Stop. It remains to derive that the Green expansion of (PC-ren) produces the concomitant with the sign
+ε⟨v, j⟩ (and not another order/sign) and the crossed completion in k. §5 forbids inserting X_T by definition or
inferring (4.2) from radicality. R161_033 adds that D^orient (direct sum) is not realized; R161_043
shows that at the «derived source» order (Xf) the Tate term has opposite parity and gives 0, not ‖r‖².
Cross-check. U1 no. U2 yes: it is exactly the «joint accounting with the Tate block (4.2)» that REVIEW_003
leaves open; the memo leaves it as OPEN/TERMINAL without derivation; the recorded obstacles are: sign of
appearance not derived (033 §6), D^orient not realized (033), opposite parity at the order Xf (043). U3 yes,
partially: G_TC is indefinite on the complete Tate plane (R161_023) and becomes positive on the
parity line; it is not a Kreĭn form with a neutral vector, it is a restriction to an invariant
subspace. U4 no. U5 no.

## R161_033 — Coherent gap / direct sum; exits A and B

Object. Y_N(f) = Σ_{2≤k≤N}(log k)k^{−1/2}Δ_kf (coherent difference of JK_Nf and K_N𝓕f);
‖Y_N‖² = Σ_{k,l}(log k)(log l)(kl)^{−1/2}⟨Δ_kf, Δ_lf⟩ (1.3); D^orient_N = ¼Σ(log k)²/k‖Δ_kf‖² (1.4) is its
diagonal (up to the factor ¼). H_N^src = ⊕_{2≤k≤N}H; analysis Af = ((log k)k^{−1/2}Δ_kf)_k; synthesis
S((u_k)) = Σu_k; Y_N = SAf; ‖SAf‖² = ‖Af‖² ⟺ vanishing of the total cross Gram.
Finite counterexample (§3, PROVED): u_2 = u_3 = u gives 4‖u‖² versus 2‖u‖²; u_2 = −u_3 gives coherent norm 0
and positive direct sum: no identity between the two follows from the coherent vector equation.
Exits (§5):
 A. Source dilation: build explicitly V_N : H → H_N^src from additive Poisson/Fourier data
    with synthesis S V_N = coherent port of (PC-ren) and ‖V_Nf‖² = D^orient_N(f) (theorem of
    Naimark/Parseval type). Target «‖V_NF‖² = D_N^orient(F)».
 B. Exact compensation of the cross Gram: with I_N(f) = Σ_{k≠l}(log k)(log l)(kl)^{−1/2}Re⟨Δ_kf, Δ_lf⟩,
    prove I_N + B_N^polar + B_T^Tate = 2D^Γ_{T,δ} + D_N^boundary, D_N^boundary ≥ 0 (7.1), with the
    first-contact equation annulling the coherent left side. The memo judges B closer to (PC-ren).
Statements. PROVED: factorization by paths; variance identity as abstract algebra; parity
Gram. OPEN / PRIOR CLAIM WITHDRAWN: second moment from (PC-ren). OPEN: appearance of the Tate Gram
with the required sign.
Stop. The synthesis S is not an isometry; the additive Fourier translation does not make log-translated copies
of a compactly supported source orthogonal; a Parseval/Naimark identity or a compensating boundary
Gram is needed.
Reading (minor inconsistency): exit A asks for «an isometry V_N : H → H_N^src» with ‖V_Nf‖² = D^orient(f);
the two things are not literally compatible (an isometry gives ‖V_Nf‖² = ‖f‖²). The real content is: a
map V_N with squared norm equal to D^orient and whose synthesis coincides with the coherent port, that
is, a dilation in which the labels are orthogonal.
Cross-check. U1 no. U2 yes in B: the cross Gram would be compensated with polar and Tate blocks (boundary
concomitants); it remains OPEN. U3 no. U4 no. U5 yes: it is the definition of exit A. Follow-up: R161_034 computes the
exact cross Gram (ratio/product channels) and discards the cancellation on the full line; R161_035 declares
the direct sum «unnecessary» and replaces it with the coherent version; R161_052–053 build a unitary
colligation (another dilation, not that of A); the synthesis (R161_099, in its lines on 033 and 035)
confirms that 035 «eliminates the need for a labelled dilation». In this part nobody built V_N
nor proved that exit A is impossible.

## R161_034 — Exact Mellin Gram: the missing interference is the product–ratio channel

Object. s = ½ + iτ; (𝓕f)^ = u_∞(τ)f̂(−τ), (Jf)^ = f̂(−τ), |u_∞| = 1. Atom d_k = k^{−1/2}(τ_{log k}𝓕 − Jτ_{log k}),
(d_kf)^ = q_k(τ)f̂(−τ), q_k = k^{−s}u_∞ − k^{−(1−s)} (summand of one atom of the multiplier D_N(s)u_∞ − D_N(1−s)).
With a_k = log k: I_N(f) = ∫Σ_{k≠l}a_ka_l q_k conj(q_l)|f̂(−τ)|²dτ (2.3).
(3.1) q_k conj(q_l) = (kl)^{−1/2}[e^{−iτ log(k/l)} + e^{iτ log(k/l)} − u_∞e^{−iτ log(kl)} − conj(u_∞)e^{iτ log(kl)}];
(3.2) Re(q_k conj q_l) = 2(kl)^{−1/2}[cos(τ log(k/l)) − Re{u_∞e^{−iτ log(kl)}}].
Checked: correct. Ratio channel (equal orientations, k/l) and product channel (opposite orientations, kl);
it coincides with 106_50_TRIANGLE_VARIANCE_AND_PRODUCT_RATIO_SPLIT. The sum–product construction controls the
product coefficient by Dirichlet convolution but does not group the ratio term through Λ∗1 = log.
§4: the polar counterterm is a continuous one-parameter family and the Tate block has rank two after
compression; there is no coefficient-by-coefficient identity converting all the frequencies log(k/l) into a
rank-two boundary term (ARGUED as «cannot be claimed on the full line»; it is a counting
argument, not a theorem with a written class).
Candidate (5.2): compressed coherent leakage L_{N,T}(F) = ‖(I−P)Σ_{k≤N}(log k)d_kPF‖² ≥ 0; the object that may
be new is the commutator [P, d_k].
Statements. PROVED: symbol, exact coherent/direct-sum difference, product–ratio decomposition.
IDENTIFIED: collision with phase 106. CANONICAL POSITIVE CANDIDATE: (5.2). OPEN: identification with the
physical scattering leakage of R161_020 and saturation at first contact.
Stop. Without the compression [P, d_k] one returns to the star/triangle variance of phase 106 (wrong coherence
direction). The leakage (5.2) remains without identification.
Cross-check. U1 no. U2 yes, fully: the leakage ‖(I−P)·PF‖² of the coherent operator is the candidate; it remains OPEN, without
computation of its renormalized limit or its saturation. U3 no. U4 no. U5 yes: shows that the condition of A
(vanishing cross Gram) is false on the full line — the cross Gram is the sum of the ratio and product channels,
which do not vanish.

## R161_035 — Coherent two-orientation gate (parallelogram)

Object. U_N = K_N𝓕, V_N = JK_N; from R161_001 (3.1) S_NM𝓕 = JK_N + K_N𝓕 + {X, E_N}, hence
U_N + V_N = S_NM𝓕 − {X, E_N} (2.2), and in renormalized version (2.3) with K_N^ren = −[X, S_N^ren].
Theorem 3.1 (PROVED):
  D_N^coh(f) := ½(‖K_N^ren𝓕f‖² + ‖JK_N^ren f‖²) − ¼‖[S_N^renM𝓕 − {X, E_N^ren}]f‖² = ¼‖(K_N^ren𝓕 − JK_N^ren)f‖² ≥ 0,
equality ⟺ K_N^ren𝓕f = JK_N^ren f. No cross term in k is eliminated. Order: synthesis by Λ∗1 = log
(K_N = L_MS_N − H_{M,N}) → retain the two orientations → coherent two-state variance.
Exterior component (5.1): D^ext_{N,T} = ¼‖(I−P)(U_N^ren − V_N^ren)f‖².
Terminal target (5.2): ½(‖U f‖² + ‖V f‖²) = ¼‖(U+V)f‖² + o(1) in the first-contact graph limit,
equivalent to (U_N^ren − V_N^ren)f → 0 (5.3).
Statements. PROVED: coherent vectors, sum formula, (3.2), retention of the product–ratio Gram.
OPEN/TERMINAL: (5.2); OPEN: identification of (5.3) with the physical scattering.
Reading: (3.1) is the parallelogram identity, generic; all the content is in (5.2). The identity
does not depend on the weight except through the definition of K_N.
Stop. §7: (5.2) is an equality of second moments; radicality gives only a vanishing linear pairing
after primitive projection. Defining the Green identity as D^coh or using the scattering law would be
circular. R161_038 proves that (5.2) does not follow from (PC) + radicality + parity.
Cross-check. U1 no. U2 yes: (5.1) is a compressed leakage and the memo requires applying the same orthogonal decomposition
to the three norms; it does not compute it. U3 no. U4 no. U5 yes: abandons exit A («unnecessary»).

## R161_036 — The coherent difference is the Gamma-covariant critical jet

Object. Z_N(s) = D_N(s) − N^{1−s}/(1−s), e_N(s) = Z_N(s)u(s) − Z_N(1−s), K_N^ren(s) = −Z_N′(s);
U_N(s) = −Z_N′(s)u(s), V_N(s) = −Z_N′(1−s). (2.2) U_N + V_N = −e_N′(s) + Z_N(s)u′(s) (connection m = u′/u);
(3.1) U_N − V_N = −Z_N′(s)u(s) + Z_N′(1−s). Using the limit Z_N → ζ and the derived functional equation
ζ′(s)u(s) + ζ(s)u′(s) + ζ′(1−s) = 0: (3.4) U_∞ − V_∞ = −2ζ′(s)u(s) − ζ(s)u′(s).
§4 evaluates at zeros of ζ and uses ζ′(ρ) ≠ 0 (uses an evaluation at zeros and a simplicity hypothesis; this is
recorded without development).
Statements. PROVED: (2.2), (3.1). PROVED CONDITIONAL on differentiated convergence of the graph: (3.4), (4.1).
OPEN/TERMINAL: saturation and differentiated convergence.
Reading: §4 rests the conclusion on simplicity (ζ′(ρ) ≠ 0) without proof; R161_037 removes that dependence.
Corrected by. R161_037 (replaces §4–6 by an almost-everywhere argument; removes the requirement of strong
differentiated convergence).
Cross-check. U1 no. U2 no (only mentions the boundary layer). U3 no. U4 no. U5 no.

## R161_037 — Saturation alone forces F = 0

Object. B_N = U_N^ren − V_N^ren, multiplier b_N(τ) = −Z_N′(s)u(s) + Z_N′(1−s); by pointwise differentiated
Euler–Maclaurin, b_N → b_∞ = −ζ′(s)u(s) + ζ′(1−s) = −2ζ′(s)u(s) − ζ(s)u′(s).
If D_N^coh(F) = ¼‖B_NF‖² → 0, an a.e. subsequence ⇒ b_∞(τ)F̂(−τ) = 0 a.e. (2.3). b_∞ ≢ 0 because
b_∞ ≡ 0 would imply (ζ²u)′ = ζ[2ζ′u + ζu′] = 0, ζ²u constant, contradiction with the pole at s = 1. Discrete
zeros on the line ⇒ F̂ = 0 a.e. ⇒ F = 0.
Statements. PROVED: pointwise differentiated convergence, subsequence argument, a.e. non-vanishing,
«D_N^coh(F) → 0 ⇒ F = 0». REMOVED: requirement of strong differentiated convergence. OPEN/ONLY GATE: (5.1)
coherent saturation at first contact.
Reading: the argument is correct (it uses the complete function and its functional equation, and the meromorphic
continuation; it does not use zeros). Note: in (3.2) the contradiction also «with any nontrivial zero» is
superfluous.
Stop. The saturation (5.1) must come out of the finite Green pairing; radicality does not suffice.
Cross-check. U1 no. U2 no. U3 no. U4 no. U5 no.

## R161_038 — Finite matrix countermodel to automatic saturation

Object. H = ℂ²; X = diag(1, −1); J = 𝓕 = [[0,1],[1,0]]; S = [[0,1],[0,0]]; L = 0. Then JXJ = −X,
M = X + 𝓕X𝓕 = 0, A = M − (L + L*) = 0 (every vector is radical). K = −[X,S] = −2S, E = S𝓕 − JS = X, H = LS − K = 2S,
{X, E} = 2I, JH + H𝓕 = 2I: (PC) holds exactly; also SM𝓕 = 0 = JK + K𝓕 + {X, E}.
U = K𝓕 = −2SJ = −2 diag(1,0), V = JK = −2 diag(0,1), U − V = −2X, D^coh(f) = ¼‖(U−V)f‖² = ‖f‖² for every f,
also on both parity lines.
Statements. PROVED (direct multiplication; checked): exact realization, A = 0, failure of saturation in
both parities. REFUTED: automatic algebraic saturation.
Closed class: every proof whose only inputs are (1) involutions J, 𝓕; (2) X + 𝓕X𝓕 = M; (3) definitions
of K, E, H, A; (4) linear (PC); (5) radicality Af = 0 and linear polarized consequences; (6) parity.
Falsifier: the 2×2 model. It does not model: logarithmic cosine kernel, support in a physical interval, semigroup of
integer translations and its Euler–Maclaurin continuum, crossed Tate collar law, Gamma pole lattice.
Reading: the countermodel has no Λ, no Euler product, no arithmetic relation; it closes a class
of formal manipulations, not a class with physical data (the memo itself says so and R161_046 reinforces it).
Cross-check. U1 no. U2 yes as a frontier: the model lacks compression to a window; the memo deduces that the
physical compression must enter essentially. U3 yes, indirectly: A = 0 is the zero form (everything radical);
it is not a non-radical neutral vector of an indefinite form. U4 no. U5 no.

## R161_039 — Terminal equivalence and blocked ledger

Object. Summary: B_N = K_N^ren𝓕 − JK_N^ren; D_N^coh = ¼‖B_NF‖² ≥ 0; D_N^coh → 0 ⇒ F = 0 (037). Missing (2.1):
«F primitive of first contact ⇒ D_N^coh(F) → 0». Not proved by: linear (PC-ren), radical polarization,
parity, abstract parallelogram, source labels/divisor variance, crossed Tate matrix without
derivation of its appearance and sign, E_N^ren → 0, completed scalar commutator.
Required identity (3.1): lim ¼‖B_NF‖² = −lim Green^{PC}_{N,T}(F), with Green^{PC} = 0 by radicality applied to a
source-defined primitive test, retaining both causal orientations, with polar term = image
layer of 028 and literal endpoint term +ε⟨v, G_TCv⟩ = ‖r‖², without using inverses of the primitive compression
nor the scattering law nor the desired norm.
Statements. PROVED: joint PC identity, polar/Tate coordinates and parity sign, positive gate,
«saturation ⇒ F = 0». «NOT PROVED / LOGICALLY INDEPENDENT OF THE FORMAL ALGEBRA»: saturation from what
exists. MISSING: physical boundary Green identity. Phase: BLOCKED.
Blocked ledger: (1) scattering/leakage 017–020; (2) inverted Gamma–Hankel shift 026–029;
(3) divisor-variance saturation 030–033; (4) coherent saturation 035–038.
Reading: §0 claims «the corpus contains no additional physical identity that provides it» and suggests
independence; R161_046 withdraws the stronger claim (independence only of the listed abstract identities, not of the
physical hypotheses). §4 (equivalence «relative to the first-contact reduction») is
an internal equivalence of the architecture; it is not developed.
Cross-check. U1 no. U2 yes: requires the literal Tate term (joint accounting) as clause 4 of (3.1). U3 no.
U4 no. U5 no (exit A does not appear in the list of requirements).

## R161_040 — Poisson identifies the two exterior histories

Object. Z_N = S_N^ren, E_N = Z_N𝓕 − JZ_N; JZ_NJ = Z_N* (real coefficients, reflection inverts orientation;
also checked for the polar part C_N, whose Volterra kernel satisfies JVJ = V*); (1.3) Z_N𝓕 = Z_N*J + E_N.
Theorem 2.1 (PROVED): with Jf = εf, f = Pf, (I−P)Z_N𝓕f − ε(I−P)Z_N*f = (I−P)E_Nf (2.2); interior analogue (2.3).
Histories H_N^+ = (I−P)Z_N𝓕P, H_N^− = (I−P)Z_N*P; ‖H_N^+f − εH_N^−f‖² = ‖(I−P)E_Nf‖² (3.3).
Compressed self-commutator: for normal Z, T = PZP, ⟨f, (T*T − TT*)f⟩ = ‖(I−P)Z*f‖² − ‖(I−P)Zf‖² (4.2).
Proposal (6.1): boundary derivative of ‖(I−P)E_N^ren f‖² = ‖(I−P)(K_N^ren𝓕 − JK_N^ren)f‖² + 2D^Γ + ε⟨v, G_TCv⟩.
Statements. PROVED: JZ_NJ = Z_N*, (2.2), (3.3), identification of the annular transport of phase 121 with the
Poisson defect. WITHDRAWN (by 041, wrong orientation): (6.1).
Stop. Differentiating the difference E_N produces the mean U + V, not the critical difference U − V.
Cross-check. U1 no. U2 yes: exterior leakage ‖(I−P)E_Nf‖², words (I−P)Z P, compression self-commutator; X = M_t
commutes with P (used to differentiate without differentiating the window). Reason for failure: orientation (041). U3 no.
U4 no. U5 no.

## R161_041 — Orientation audit: sum and difference

Object. Z, K = −[X,Z], E = Z𝓕 − JZ, C = Z𝓕 + JZ; U = K𝓕, V = JK; X𝓕 + 𝓕X = M𝓕.
(2.2) U + V = ZM𝓕 − {X, E}. Theorem 3.1 (PROVED): {X, JZ} = −J[X,Z] = JK, hence U − V = ZM𝓕 − {X, C} (3.3);
D_N^coh = ¼‖[Z_NM𝓕 − {X, C_N}]f‖² (3.4). Mellin: c_N = Z_Nu + Z_N(1−s), −c_N′ + Z_Nu′ = U − V (4.3).
Proposed object (5.2): Re⟨exterior Ef, exterior [ZM𝓕 − {X, C}]f⟩ with polar and Tate corrections.
Statements. PROVED: (2.2), (3.3), Mellin check. WITHDRAWN: 040 (6.1). OPEN: compressed mixed E–C Green
completion.
Reading: checked {X, JZ} = XJZ + JZX = −JXZ + JZX = −J[X, Z] = JK. Correct.
Cross-check. U1 no. U2 yes: the compressed mixed pairing is of type compression + M_t. U3 no. U4 no. U5 no.

## R161_042 — Mixed Green Wronskian and Tate defect

Object. Lemma 1.1 (PROVED): X = X*, e = a − d, c = a + d ⇒ Re⟨e, Xc⟩ = ⟨a, Xa⟩ − ⟨d, Xd⟩. With a_N = Z_N𝓕f,
d_N = JZ_Nf: Re⟨E_Nf, XC_Nf⟩ = ⟨Z_N𝓕f, XZ_N𝓕f⟩ + ⟨Z_Nf, XZ_Nf⟩ (2.2)–(2.3) (by JXJ = −X).
Exterior: P_+ = 1_{[T,∞)}, P_− = 1_{(−∞,−T]}, a_+ = P_+a_N, d_− = P_−d_N;
⟨a_+, Xa_+⟩ − ⟨d_−, Xd_−⟩ − T(‖a_+‖² + ‖d_−‖²) = ‖(X−T)^{1/2}a_+‖² + ‖(−X−T)^{1/2}d_−‖² ≥ 0 (3.4).
With B_N = Z_NM𝓕 − {X, C_N}: Re⟨E_Nf, B_Nf⟩ = Re⟨E_Nf, Z_NM𝓕f⟩ − Re⟨E_Nf, XC_Nf⟩ − Re⟨E_Nf, C_NXf⟩ (4.2);
the last term forces PXf = Π_TPXf + Tau_TPXf (primitive + Tate).
Acceptance identity (6.2): 0 = ‖(X−T)^{1/2}a_+‖² + ‖(−X−T)^{1/2}d_−‖² + D_N^boundary(f).
Statements. PROVED: Lemma 1.1, (2.2), (3.4), decomposition. REJECTED (horizontal modulation tautology,
by 044): primitive component as a new law. OPEN: reduction of the Tate component to a vanishing
pairing; sign of the residual boundary pieces.
Reading: the original text anticipated a positive Tate square; the memo itself already incorporates the correction
of 043. The retention of the «interior and exterior pieces on the wrong side» of (2.2) is not computed.
Cross-check. U1 no. U2 yes, fully: uses M_t (X) and the compression to exterior half-lines, with the decomposition
primitive + Tate; the sign of the residual pieces remains open. U3 no (Lemma 1.1 is the indefinite Wronskian form
⟨a,Xa⟩ − ⟨d,Xd⟩, but it is not treated as a Kreĭn form with a neutral vector). U4 no. U5 no.

## R161_043 — Opposite parity annuls the Tate term of the source derivative

Object. JX = −XJ ⇒ if Jf = εf, J(Xf) = −εXf. Tau_T commutes with J ⇒ the coefficient w_X of Tau_TPXf satisfies
Cw_X = −εw_X. With r (Cv = εv) and j = G_TCv (parity ε): ⟨r, Tau_TPXf⟩ = 0 (3.3), ⟨w_X, j⟩ = 0 (3.5).
Statements. PROVED: all three. REJECTED / WRONG PARITY: positive Tate square at this order. OPEN:
conversion of the complete finite pairing into the literal orthogonal terms; remaining primitive/exterior Green
identity.
Stop. ε⟨v, G_TCv⟩ = ‖r‖² (032) applies only to endpoint vectors of the same parity as the forcing.
Cross-check. U1 no. U2 yes: closes the joint accounting with the Tate block at the order «Xf» (gives 0, not
‖r‖²); it does not close other orderings. U3 no. U4 no. U5 no.

## R161_044 — The primitive term Xf is the horizontal modulation tautology

Object. G_σ = Π_T(e^{σX}f), G_0′ = Π_TP_TXf; P121_HORIZONTAL_MODULATION_RADICAL_NO_GO Thm. 3.1: a_T(f, G_σ) = 0 and
its derivatives only repeat a_T(f, h) = 0, h ∈ P_T. All new information would be a defect of exterior order:
with g_N the right product port and w_N the scattering defect, ⟨g_N, S_N^ren w_N⟩ and ⟨(S_N^ren)*g_N, w_N⟩ are
equal before cutting the support; their difference after projecting is a sum of Hankel terms
PS^ren(I−P), (I−P)S^ren P. Minimal scalar gate (4.1): Re⟨g, e⟩ = 0, e = P_+C_log g + εg, since
½‖(I + εC_log)g‖² = Re⟨g, e⟩ (R161_021).
Statements. PROVED: G_0′ = Π_TP_TXf. KNOWN TAUTOLOGY: primitive pairing. ZERO (043): Tate.
PROVED STRUCTURALLY: reduction to exterior Hankel commutators. OPEN/TERMINAL: antisymmetric exterior
reciprocity (L161.6 of R161_023).
Reading: R161_046 adds that two orders coinciding by adjunction on their common domain do not generate a
boundary term by themselves; an explicit projection or distinct domain is needed.
Cross-check. U1 no. U2 yes: modulation e^{σX} (M_t), primitive projection, compression Hankel; the interior part is
tautological, the exterior reciprocity remains OPEN. U3 no. U4 no. U5 no.

## R161_045 — Toeplitz–Hankel: the local square does not globalize the gate

Object. For a prime p, r = p^{−1/2}, S the unilateral shift, A_r = rS(1 − rS)^{−1}.
(1.2) (from P122_013_LOCAL_EULER_DETERMINANT_LINE): A_r*A_r − A_rA_r* = H_{φ̄_r}*H_{φ̄_r} = (1 − r²)^{−1}ℓ_r*ℓ_r ⪰ 0
(rank-one self-commutator, exact «root observation», correct orientation under port inversion).
Local determinant cocycle (P122_015_EULER_CONTOU_CARRERE_DETERMINANT_BRIDGE): ⟨1 − rz, 1 − rz^{−1}⟩_Hdet = 1 − r²;
its grading derivative is the connection (1.1) and its curvature is (1.2).
Why it does not close (§2): the first-contact equations give two histories h_{p,+}, h_{p,−}, not one and the same
vector in both entries of (1.2); they give a norm relation between crossed ports, not
‖A_rh‖ = ‖A_r*h‖ (2.1) (the «annular transport» missing since phase 121). Phase 161 gives the non-differentiated
transport H_N^+f − εH_N^−f = (I−P)E_N^ren f (2.2), but the logarithmic derivative required by (1.2) changes the
orientation: derivative of the difference E_N → K_N𝓕 + JK_N; derivative of the sum C_N → K_N𝓕 − JK_N (2.3). Hence
(2.2) cannot be differentiated into the single-history hypothesis (2.1).
Global obstruction (§3, cited from P122_015): multiplying the local lines does not build (1) the archimedean
quarter-Gamma line, (2) the two Tate boundary factors, (3) a convergent extension of the
critical boundary determinant, (4) a metric anomaly/trivialization identifying the two physical
histories, (5) first-contact flatness.
Statements. PROVED (CITED from phase 122): local Toeplitz–Hankel square; local cocycle and normalization.
PROVED (040): Poisson identification of non-differentiated histories. FALSE / WRONG ORIENTATION: differentiation
to the critical orientation. MISSING: global Gamma–Tate determinant anomaly/trivialization. OPEN/TERMINAL:
antisymmetric exterior reciprocity.
Exact reason for the stop: (i) orientation mismatch (2.3) between the Poisson transport and the
derivative required by the self-commutator; (ii) absence of a global trivialization of the product of local lines
(the five items of §3). Reading: item (ii) is CITED from phase 122 and is not re-derived here; item (i) is
PROVED by 041. The memo gives no explicit falsifier; the class countermodel for the algebraic part is
that of R161_038.
Cross-check. U1 no (each local factor is linear in Λ via Euler; there is no additive term of degree ≥ 2). U2 yes:
Toeplitz operators (compression to Hardy), self-commutator = ‖Hankel‖² of finite rank (one) per prime;
globalization fails by orientation and by lack of trivialization. U3 no. U4 no. U5 no.

## R161_046 — Backward chain and finite detection on the radical

Object. Scope correction: 038 refutes saturation from the listed abstract identities, not the
independence with respect to the physical hypotheses; the previous claim that the exterior reciprocity is a
new axiom is withdrawn (status: not proved). The two orders of R161_023 (5.3) coincide by adjunction on the
common domain: inverting the order generates no boundary; an explicit projection/distinct domain is needed.
Finite detection lemma (PROVED, using compactness of the resolvent imported from phase 121 and completeness of
moments from R161_019): N ⊂ L²(−T,T) finite-dimensional, a_m = 2m + ½, ℓ_m(F) = ∫F(t)e^{−a_mt}dt,
N_M = N ∩ ker ℓ_1 ∩ … ∩ ker ℓ_M; there exists finite M with N_M = {0}; with weights b_m > 0,
Σ_{m≤M} b_m|ℓ_m(F)|² ≥ c_N‖F‖² on N. It does not bound M by dim N nor uniformly in T.
Certificate criterion: primitive tests H_{m,n}F from finite PC data with
|ℓ_m(F)|² ≤ Re a_T(F, H_{m,n}F) + e_{m,n}(F), limsup_n e_{m,n} ≤ 0 (acceptance criterion, not built).
Blocks: ⟨g, Sw⟩ = ⟨PS*g, Pw⟩ + ⟨QS*g, Qw⟩, Q = I−P; if Pw = r (Tate), the first term is ⟨Tau PS*g, r⟩.
Statements. PROVED: reduction to finite detection (with imports). Not established: independence of the
physical hypotheses (withdraws 039). OPEN: finite PC certificate. Next: projected pairing of the
Laurent coefficient at a fixed positive odd Gamma pole.
Cross-check. U1 no. U2 yes: finite rank (detection on finite-dimensional N_T, finitely many moments) and P/Q
decomposition of the pairing; no term with a sign. U3 no. U4 no. U5 no.

## R161_047 — Compression at a fixed pole and exact exponential collar

Object. z = s − ½, a_m = 2m + ½; Res_{z=a_m}W^0(½+z) = K_F(a_m) (R161_025). v = w − E_Tr (exterior remainder);
Res_{z=a_m}Mv(z) = K_F(a_m) (1); every compactly supported distribution has an entire transform (interior
primitive tests, interior Tate corrections, endpoint distributions and prehistories Q_± contribute
no residue). Model: h(t) = −ke^{at}1_{t<−T} has transform ke^{(z−a)T}/(z−a), residue k.
Collar (2): ℓ_a(Pτ_hF) = e^{ah}[ℓ_a(F) − L_{a,h}(F)], L_{a,h}(F) = ∫_{−T}^{−T+h}F(u)e^{−au}du, 0 ≤ h ≤ 2T.
(3): ℓ_a(PS_NF) = Σ_{n≤min(N, e^{2T})} n^{a−1/2}[ℓ_a(F) − L_{a,log n}(F)] (analogues with log n or Λ(n)).
Statements. PROVED: (1)–(3). OPEN: annihilation at a fixed pole from PC-ren.
Stop. The large factor n^{a−1/2} also multiplies the collar; there is no small remainder; it coincides with the
large-moment obstruction of R161_024 §5.
Cross-check. U1 no. U2 yes: compression by finite translation, exact collars; no sign. U3 no. U4 no. U5 no.

## R161_048 — Exact stabilization of the interior cut and retry ledger

Object. If supp F ⊂ [−T,T] and vanishing positive Tate moment: supp C_NF ⊂ [−T − log N, T − log N]; for
log N ≥ 2T, P_TC_NF = 0 (1); P_Tτ_{log n}F = 0 if log n ≥ 2T; hence, for N ≥ e^{2T},
P_TZ_NF = P_TS_NF = Σ_{n<e^{2T}} n^{−1/2}P_Tτ_{log n}F (2). Increasing the cut only changes the exterior; there is no
new interior equation as N → ∞. The relation Z_N𝓕F − εZ_N*F = E_NF retains the noncompact source 𝓕F,
to which (2) does not apply.
Statements. PROVED: (1)–(2). Status: missing step defined — control the exterior Fourier block together
with the renormalized translated collars. D OPEN; no closure is declared.
Cross-check. U1 no. U2 yes: compression to the window and exact finite truncation; no sign. U3 no. U4 no. U5 no.

## R161_049 — Three-block scattering audit

Object. P_L = 1_{(−∞,−T]}, P_0 = 1_{(−T,T)}, P_R = 1_{[T,∞)}; C logarithmic cosine; g = P_Rg corrected right product
port; h = g + εCg. Desired gate P_Rh = 0 (1.2) (⇔ P_RCg = −εg; by R161_020 it implies h = 0).
What the completed incoming current theorem (P121_GRAPH_RENORMALIZED_INCOMING_CURRENT) proves is
P_0h = 0 (1.3), the central block. With a = P_RCg, b = P_0Cg = 0, c = P_LCg: ‖a‖² + ‖c‖² = ‖g‖² (2.1);
e_R = g + εa, e_L = εc; ‖e_R‖² − ‖e_L‖² = 2‖a‖² + 2εRe⟨g, a⟩ (2.3); ‖h‖² = 2‖g‖² + 2εRe⟨g, Cg⟩ (2.4).
Missing scalar condition: Re⟨g, e_R⟩ = 0 (2.5). In the first chamber 0.8 < T < ½log5, the initial right
collar is the field Y_3 (2, 3, 4) and the nonlocal Gamma row Y_3(F) − tF + r_ε = CQCF.
Statements. PROVED: three-block identities. Rejected: identifying P_0 with P_R. OPEN: exterior
transfer. Generic Sonin functions show (ARGUED, without an example written here) that central cancellation
+ cosine symmetry do not transfer.
Cross-check. U1 no. U2 yes: compression into three blocks; none with a sign. U3 yes, in germ: C self-adjoint unitary
(indefinite form ⟨g, Cg⟩); no neutral vector is built. U4 no. U5 no.

## R161_050 — Three-block unitary countermodel

Object. H = ℂ³, basis e_L, e_0, e_R; C e_L = e_R, C e_R = e_L, C e_0 = e_0; g = e_R; h_ε = e_R + εe_L.
Then g = P_Rg, C = C* = C^{−1}, P_0h_ε = 0, Ch_ε = εh_ε, but P_Rh_ε = e_R ≠ 0 and P_RCg = 0 ≠ −εg.
Closed class (PROVED by multiplication): «central cancellation + self-adjoint unitarity + scattering
parity ⇒ right compressed scattering» is false. Falsifier: the 3×3 model. Available arithmetic properties
that would exclude it (each implies the exclusion of first contact): membership in the
co-Poisson range (R161_012), removability at positive odd Gamma poles (024), vanishing Gamma residue energy
(025–026), preservation of active Euler ideals (P121_ACTIVE_EULER_IDEAL_OVERDENSITY), exterior PC
Green/reciprocity identity (021–023).
Cross-check. U1 no. U2 yes (frontier: shows that compression into three blocks without arithmetic does not suffice). U3 yes,
in germ: h_ε is an eigenvector of the indefinite form ⟨·, C·⟩ with ⟨h_ε, Ch_ε⟩ = ε‖h_ε‖², not neutral; no
Kreĭn form is studied. U4 no. U5 no.

## R161_051 — Terminal equivalence after the three-block audit

Object. List of seven equality-state properties (right compressed scattering; X_T(F) = 0;
removability of W_ε^0 at positive odd Gamma poles; vanishing pole energy; co-Poisson range; preservation
of active Euler ideals for p < e^{2T}; coherent PC saturation of 037), each with an implication towards
F = 0 PROVED in phases 161/121; equivalence of strength relative to the imported first-contact reduction.
Statements. PROVED: downstream closure and equivalence of strength (trivial: vacuity in the reverse
direction). Not proved: derivation of any of them from PC-ren + first contact. Explicitly «it is not a
claim that no proof exists».
Cross-check. U1 no. U2 no (inventory). U3 no. U4 no. U5 no.

## R161_052 — Finite unitary Poisson colligation

Object. A_N(τ) = Z_N(s), B_N = Z_N(1−s) = conj(A_N); e_N = A_Nu − B_N; θ_N = A_Nu/B_N, |θ_N| = 1 a.e.;
e_N = B_N(θ_N − 1). P Hardy/support projection, Q = I−P, U_N = M_{θ_N}, T_N = PU_NP:
I − T_N*T_N = (QU_NP)*(QU_NP) ⪰ 0, I − T_NT_N* = (QU_N*P)*(QU_N*P) ⪰ 0; ‖x‖² − ‖T_Nx‖² = ‖QU_Nx‖² (2.3);
if T_Nx = λx, |λ| = 1, then U_Nx = λx. Phase current without division:
|A_N|²θ_N′/θ_N = conj(A_N)A_N′ + |A_N|²u′/u − A_N conj(A_N′) (3.2). Remaining proposition (5.1): for the source
vector x_{M,N,T}(F), ‖T_Nx‖² − ‖x‖² → 0 and the limit of QU_Nx is the physical left leakage.
Statements. PROVED: unimodular multiplier, Toeplitz–Hankel leakage square, phase current.
WITHDRAWN by R161_056 (outside the part; note in the header): that the unitary tangent is the closure jet (it is
the mean U + V). OPEN: (5.1).
Cross-check. U1 no. U2 yes: it is a compression of a unitary with defect ‖QU_NPx‖² (exact leakage, without a chosen square
root); extremality remains open and the tangent has the wrong orientation. U3 no. U4 no.
U5: related but distinct — it is a unitary dilation (conservative colligation) of the quotient of the
two histories, not the source dilation with orthogonal labels k of exit A.

## R161_053 — Canonical lifting of the source and covariant tangent

Object. (E_N^ren F)^ = [A_Nu − B_N]F̂(−τ); x_N(F) = B_NF̂(−τ); U_Nx_N = A_NuF̂(−τ), (U_N − I)x_N = (E_N^renF)^ (1.3).
D_τ = (1/i)∂_τ, [D_τ, U]x = (1/i)U′x; U_N*[D_τ, U_N]x_N = q_Nx_N, q_N = (1/i)θ_N′/θ_N real;
|B_N|²q_N = (1/i)[conj(A_N)A_N′ + |A_N|²u′/u − A_N conj(A_N′)]. ‖PU_Nx‖² + ‖QU_Nx‖² = ‖x‖²; x_N is not in PH.
Acceptance (5.1): ‖QU_Nx_N^Tate(F)‖² + E_N^Γ(F) + E_N^Tate(F) = o(1).
Statements. PROVED: lifting, (1.3), covariant tangent. WITHDRAWN by 056: closure orientation
(the tangent is the mean). OPEN: balance (5.1).
Cross-check. U1 no. U2 yes (Hardy compression and Tate endpoint). U3 no. U4 no. U5: the lifting x_N is a
dilation of the source to the boundary space, but without labels k or norm D^orient: it is not exit A.

## R161_054 — Two causal orientations: squeeze lemma

Object. H = H_L ⊕ H_0 ⊕ H_R, U unitary, y = Ux: ‖y_R‖² − ‖x_R‖² = ‖x_L‖² − ‖y_L‖² + ‖x_0‖² − ‖y_0‖² (1.1).
With ‖x_0‖ = ‖y_0‖: one orientation with x_L = 0 gives ≤ 0 (1.4); the reflected orientation gives ≥ 0 (1.5); if it is the
same scalar, both vanish (1.6). Δ_0 = ‖x_0‖² − ‖y_0‖² uncontrolled (2.2); assigning it 0 from the
completed commutator is invalid (central amplitude ≠ difference of metrics). Acceptance (4.1)–(4):
Δ^+_{0,N} − Δ^−_{0,N} = 2Re⟨C_N^Tate(F), endpoint_N(F)⟩, common exterior norms N_T(0), N_T(δ) in inverted
order, uniform o(δ) remainders; then E_T^PC(F) = 0 (R161_015).
Statements. PROVED: (1.1), abstract squeeze. OPEN: central metric equality (4.1), identification of the
common port and uniformity. Note 056: the application to the tangent of θ_N does not reach the critical jet.
Cross-check. U1 no. U2 yes: balance of compression blocks with Tate term; open. U3 yes, in the
mechanism: two inequalities of opposite sign on the same scalar (squeeze), not a Kreĭn form; there is no
neutral vector. U4 no. U5 no.

## R161_055 — Central metric equality via a diagonal graph limit

Object. Diagonal lemma (PROVED): E_N = Y_N − X_N, E_Nf → 0 and X_Nf → Xf on a dense core in the graph; there exist
f_j → F and N_j with E_{N_j}f_j → 0, X_{N_j}f_j → XF, Y_{N_j}f_j → XF; for every projection P,
‖PY_{N_j}f_j‖² − ‖PX_{N_j}f_j‖² → 0. Application: X_N = Z_N*J, Y_N = Z_N𝓕, E_N = E_N^ren; stable under a
finite-rank correction T_j common to both histories.
Statements. PROVED: diagonal; non-differentiated central metric equality along it; stability under the
Tate correction. OPEN: differentiated tangent and identification of the common port norm; o(δ) remainders.
Reading: the equality is of order zero; the memo itself warns that both projected differences may
tend to zero without informing about the derived boundary layer. Applicability uses the common graph of phase
121 (imported).
Cross-check. U1 no. U2 yes (projections and finite-rank correction); no sign. U3 no. U4 no. U5 no.

---

## Synthesis

### (a) Reusable PROVED pieces

- Polar layer = exterior image: ∂_aC_a = e^{a/2}τ_a; support of C_aF in [−T−a, T−a] under vanishing Tate moment;
  ∂_a(C_aF) = εe^{a/2}τ_aJF (R161_028 §§1–3). Interior stabilization P_TZ_NF = Σ_{n<e^{2T}} n^{−1/2}P_Tτ_{log n}F
  for N ≥ e^{2T} (R161_048 (1)–(2)).
- Derivative and jumps of ‖Z_af‖² (R161_029 (2.2), (3.2)): indefinite, useful as falsifiers of monotonicity.
- Oriented divisor variance (R161_030 Thm. 1.1) and its realization by paths with collapse of the
  seam (R161_031 (3.2)): D^orient = ¼Σ(log k)²/k‖Δ_kf‖² as a direct sum.
- Tate parity Gram: ε⟨v, G_TCv⟩ = ‖r‖² = 4|c|²(sinh T + εT) (R161_032 Thm. 2.1, (3.2)).
- Exact cross Gram in Mellin, ratio and product channels (R161_034 (2.3), (3.1)–(3.2)).
- Coherent parallelogram D_N^coh = ¼‖(K_N^ren𝓕 − JK_N^ren)f‖² with U + V = S^renM𝓕 − {X, E^ren} (R161_035 Thm. 3.1)
  and U − V = ZM𝓕 − {X, C} (R161_041 Thm. 3.1).
- D_N^coh(F) → 0 ⇒ F = 0 (R161_037 §§2–3), using the complete function and its functional equation.
- JZ_NJ = Z_N*, exterior Poisson transport (I−P)Z_N𝓕f − ε(I−P)Z_N*f = (I−P)E_Nf (R161_040 Thm. 2.1, (3.3));
  compressed self-commutator as a difference of two leakages (R161_040 (4.2)).
- Sum–difference Green lemma Re⟨a−d, X(a+d)⟩ = ⟨a,Xa⟩ − ⟨d,Xd⟩ and exterior excess (3.4) (R161_042).
- Parity: J(Xf) = −εXf; the Tate term of Xf is orthogonal to r and to j (R161_043).
- Π_TP_TXf = G_0′ of the horizontal modulation (R161_044 §1).
- Local Toeplitz–Hankel square A_r*A_r − A_rA_r* = (1 − r²)^{−1}ℓ_r*ℓ_r (R161_045 §1, CITED from P122_013) and
  cocycle 1 − r² (CITED from P122_015).
- Finite detection on a finite-dimensional radical (R161_046), exact exponential collar (R161_047 (2)–(3)),
  exterior Gamma residues (R161_047 (1)).
- Three-block identities (R161_049 (2.1)–(2.4)); unitary colligation θ_N and exact leakage (R161_052 §2);
  lifting x_N and covariant tangent (R161_053 §§1–2); three-block flow and squeeze (R161_054 §1);
  diagonal lemma (R161_055 §1).

### (b) Closures with class and falsifier

- R161_038: class = proofs using only the involutions J, 𝓕, X + 𝓕X𝓕 = M, definitions of K, E, H, A, linear
  (PC), radicality (and linear polarizations) and parity. Falsifier: 2×2 model with A = 0 and
  D^coh = ‖f‖². Conclusion: coherent saturation does not follow from that class.
- R161_050: class = central cancellation + self-adjoint unitary C + scattering parity. Falsifier:
  3×3 model. Conclusion: there is no transfer P_0 → P_R.
- R161_033 §3: class = deducing the direct-sum norm from the coherent equation. Falsifier: u_2 = ±u_3.
- R161_029: monotonicity of the ordinary discrepancy FALSE (NUMERICAL falsifier).
- R161_040 (6.1), R161_052–054 (unitary tangent): withdrawn for wrong orientation (041, 056), with an algebraic
  proof that the derivative of the difference is the mean.
- R161_043: positive Tate square at the order Xf: rejected by opposite parity (PROVED).
- R161_044: primitive component of Xf: tautology (phase 121).
- R161_034 §4: polar/Tate cancellation of the cross Gram on the full line: ARGUED impossible (rank-two
  count versus infinitely many frequencies), not a theorem with a class.

### (c) Explicitly open, with exact obstacle

- L161.11 (028 (6.1)) / two-orientation form of 029 §6: cross term Re⟨Z_af, τ_af⟩ without sign.
- Divisor-variance saturation (030 (4.2)) and boundary (031 (5.3)): the direct-sum norm is not
  realized by (PC-ren) (033).
- Finite Green accounting (032 (4.2)) 0 = X_T + ‖r‖² + D^orient + 2D^Γ: it was not derived that the concomitant
  appears as +ε⟨v, j⟩; D^orient not realized; at the order Xf it gives 0 (043).
- Exits A and B of 033 (7.1).
- Compressed coherent leakage L_{N,T} = ‖(I−P)Σ(log k)d_kPF‖² (034 (5.2)): without identification with the physical leakage nor
  saturation.
- Coherent saturation (035 (5.2), 037 (5.1), 039 (2.1)): «first contact ⇒ D_N^coh → 0»; requires a physical
  boundary Green identity (039 (3.1)) that does not exist in the corpus.
- Compressed mixed E–C Green completion (041 (5.2), 042 (6.2)): sign of the residual boundary pieces.
- Antisymmetric exterior reciprocity (044 §§3–4; 045): Re⟨g, e⟩ = 0; requires a global Gamma–Tate
  trivialization (045 §3) or an exterior-order identity with a distinct projection/domain (046).
- Finite PC certificate for detection (046); annihilation at a fixed pole (047): the factor n^{a−1/2} multiplies
  the collar.
- Exterior transfer P_0 → P_R (049–051): requires an arithmetic property that excludes the 3×3 model.
- Extremality of the colligation (052 (5.1)), PC–Γ–Tate balance (053 (5.1)), differentiated central metric
  equality (054 (4.1), 055 §4).

### (d) What already covers U1–U5, with the recorded reason for failure

- U1 (term of degree ≥ 2 in the weight that adds and vanishes at Λ). Only R161_030–031 have a term
  quadratic in the weight that enters additively: ½ΣΣ_{d,e|k}Λ(d)Λ(e)‖m_d − m_e‖². It vanishes, but by coherence of the
  translations (m_{k,d} does not depend on d) and for any weight, not by Σ_{d|n}Λ(d) = log n; identity (1.1)
  is generic in the weight. The recorded failure is not one of U1 but of realization (033). U1 remains untouched in its
  sense of REVIEW_003.
- U2 (compression, M_t, finite rank; Tate block). Covered extensively: compressed coherent leakage
  (034 (5.2), unidentified); exterior Poisson leakage (040 (3.3), its derivative gives the mean orientation: 041);
  mixed Green with M_t and exterior half-lines (042, residual pieces without sign); Tate term at order Xf
  = 0 by parity (043); primitive term = tautology (044); local rank-one Toeplitz–Hankel self-commutator
  (045: does not globalize by orientation and lack of Gamma–Tate trivialization); finite rank / detection (046);
  collars (047–048); three blocks (049–050: countermodel); unitary colligation and squeeze (052–055: tangent
  with mean orientation, central equality only of order zero). The joint accounting with the Tate block
  (032 (4.2)) remained OPEN without derivation; the three recorded reasons are: appearance/sign not derived (033 §6),
  direct-sum second moment not realized (033), and vanishing by parity in the ordering Xf (043).
  There is no complete computation of (4.2) in another ordering in this part.
- U3 (indefinite forms with non-radical neutral vector). None is built. The closest: G_TC indefinite
  on the Tate plane and positive on the parity line (032); form ⟨g, Cg⟩ with self-adjoint unitary C
  (049–050, the vector h_ε is an eigenvector, not neutral); squeeze of two opposite inequalities (054); Wronskian
  ⟨a,Xa⟩ − ⟨d,Xd⟩ (042). None is treated as a Kreĭn space.
- U4 (truncated Möbius remainder). It does not appear in the part; 031 declares that it uses no Möbius elimination. The tail
  H_{M,N} enters only as K_N = L_MS_N − H_{M,N}.
- U5 (exit A of 033). Definition: map V_N : H → ⊕_{2≤k≤N}H built from additive Poisson/Fourier data,
  with S V_N = coherent port of (PC-ren) and ‖V_Nf‖² = D^orient_N(f) = ¼Σ_{k≤N}(log k)²/k‖Δ_kf‖² (theorem of
  Naimark/Parseval type making the labels k orthogonal). It would require: compensating or annulling the cross Gram
  I_N = Σ_{k≠l}(log k)(log l)(kl)^{−1/2}Re⟨Δ_kf, Δ_lf⟩, which by 034 is exactly the sum of the ratio
  (cos(τ log(k/l))) and product (−Re u_∞e^{−iτ log kl}) channels, nonzero (collision with phase 106). Nobody took it up: 035
  declares it unnecessary and moves to the coherent version; 052–053 build another dilation (unitary colligation
  M_{θ_N} with lifting x_N = B_NF̂(−τ)), without labels k, whose tangent turned out to have mean orientation
  (056); the synthesis R161_099 confirms the abandonment. There is no proof of impossibility of A in this part.

### (e) Inconsistencies between memos

1. 031 §0 says the vectors of 030 (4.1) are identified and suggests realization; 033 withdraws the
   realization of the direct-sum norm (031 already refers to 033 in its text).
2. 033 §5.A asks for an «isometry» with ‖V_Nf‖² = D^orient(f): literally incompatible; the real meaning is a
   dilation with orthogonal labels. 033 (1.4) calls «diagonal of (1.3)» a quantity that differs by the
   factor ¼.
3. 032 anticipates the term +ε⟨v, j⟩ = ‖r‖² in the accounting; 042 expected it at the order Xf; 043 proves that at
   that order it is 0.
4. 039 §0 suggests logical independence of the saturation from the corpus; 046 withdraws it (only with respect to the
   abstract identities of 038).
5. 040 (6.1) proposed and withdrawn by 041; 052–054 propose the tangent of θ_N as closure jet, withdrawn by
   056 (outside the part), with notes in the header.
6. 036 §4 uses simplicity (ζ′(ρ) ≠ 0) and differentiated convergence; 037 removes both dependencies.
7. 029 identifies L161.11 with the inverted Markov gate of 016; 031 and 035 change the target to the
   direct-sum version and then the coherent one; 039 declares them the same blocked gate.
8. 049 claims that generic Sonin functions prevent the transfer, without an example written in the memo (050
   writes it in matrix form).

### (f) Files read (complete reading with Read, from beginning to end)

R161_028 (198 l.), R161_029 (132), R161_030 (143), R161_031 (162), R161_032 (147), R161_033 (175), R161_034 (152),
R161_035 (158), R161_036 (149), R161_037 (151), R161_038 (171), R161_039 (111), R161_040 (160), R161_041 (151),
R161_042 (179), R161_043 (120), R161_044 (116), R161_045 (93), R161_046 (75), R161_047 (66), R161_048 (39),
R161_049 (70), R161_050 (53), R161_051 (44), R161_052 (99), R161_053 (97), R161_054 (99), R161_055 (69).
28 of 28, all complete. In addition, from phase 212: README.md, OBJECT_SPEC.md, LEDGER.md, BRIEF_CONSTRUCTOR.md,
REVIEW_003.md (complete). For the follow-up of U5, «dilation/Naimark/direct-sum» was searched in R161_056–099
(auxiliary search, not a complete reading of those files).
