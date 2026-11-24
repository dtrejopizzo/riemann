# Review 004 — independent check of ROUND_005_C, ROUND_005_A, ROUND_005_E, ROUND_006_A

Reference objects: STATEMENT_001.md (window form a_T, P_T, Lévy form), OBJECT_SPEC_001.md (R1–R5), Paper 46
(04-papers/46-row-d-sign-radial-intersection-form/main.tex). No equivalence of (★) with any other statement is used.
Verdicts: CONFIRMED (key step) / REFUTED / DOWNGRADE. Line numbers refer to the memo under review.

---------------------------------------------------------------------------------------------------
## 1. ROUND_005_C (the comb-response family E_T)

**Prop. 2 (l. 60–78). CONFIRMED.** Key step: for F = φ_q, φ_q(t ∓ log n) = n^{±iω_q}φ_q(t) on the overlap
t ≷ ∓(T − log n), giving ψ_q = ½[Ψ_q(T+t) + conj Ψ_q(T−t)]. Sector form: for F supported in I_T and log n < 2T the
circular translate on (−2T, 2T) agrees with the plain translate on I_T (the wrapped part lands in (−2T, −T)), so
Π = ½Σ_q C_q|φ_q⟩⟨φ_q| on L²(I_T), with ⟨ε_{q′}, 1_{I_T}ε_q⟩ = sin(π(q′−q)/2)/(π(q′−q)). Checked.

**Prop. 2′ (l. 84–94). CONFIRMED.** Key step: 1/(½+iω) + 1/(½−iω) = 1/(¼+ω²), and
e^{−iωt}e^{(T−t)(½−iω)} = e^{T(½−iω)}e^{−t/2}; the e^{±t/2} terms are in 𝒯, φ_q ∈ 𝒩_η, both killed by P_𝒞 because
L²(I_T) = 𝒯 ⊕ N′ ⊕ 𝒞 with 𝒯 + N′ = 𝒯 + 𝒩_η (pr_T is the orthogonal projection onto P_T = 𝒯^⊥).

**Lemma 1 (l. 108–123). CONFIRMED.** (i) ∫_ℝ e^{u/2}c_F = A(F)·conj B(F) = 0. (ii) Recomputed:
2∫_0^{2T}(e^{u/2} + e^{−u/2})cos(ω_q u)du = ½(¼+ω_q²)^{−1}·2[(−1)^q(e^T − e^{−T})] = (−1)^q·2 sinh T/(¼+ω_q²). (iii) is
inherited from ROUND_001_C Theorem 1 because the gauge is a form identically zero on P_T; note that the λ-gauge (unlike
the alternating c-gauge, which is null on all of L²(I_T) since Re c_F(2T) = 0) is null ONLY on P_T, so every operator
statement must be compressed by P_T. The memo respects this (l. 152–154, residual 3·10⁻¹⁰).

**Prop. 3, the sign budget (l. 133–150). CONFIRMED as an exact identity on P_T, with one REFUTED side claim.**
Recomputation. In the Lévy form split K = 2e^{−u/2} + K_1 and write the comb as ∫Re c_F dR + 2∫_0^{2T}e^{u/2}Re c_F du
(dR = Σ v_nδ_{log n} − 2e^{u/2}du, consistent with R(u) = Σ_{log n≤u}v_n − 4(e^{u/2}−1)). The j = 0 kernel term over
(0, ∞) is 4‖F‖² − 2∫_0^{2T}e^{−u/2}Re c_F (c_F vanishes beyond 2T); subtracting the comb density 2∫e^{u/2}Re c_F and
using Lemma 1(i) the two Re c_F integrals cancel exactly, leaving 4‖F‖². The K_1 part over (2T, ∞) leaves
‖F‖²∫_{2T}^∞K_1 = ‖F‖²Σ_{j≥1}2e^{−(4j+1)T}/(2j+½). Hence σ_T = C_0 + 4 + Σ_{j≥1}2e^{−(4j+1)T}/(2j+½), which equals the
other form C_0 + 4 − 4e^{−T} + ε_T because the j = 0 summand of ε_T = ∫_{2T}^∞K is 4e^{−T}. The split is EXACT on P_T
(the only non-identity used is Lemma 1(i), which is exactly the Tate pair). Evaluated: σ_{½log5+10⁻⁴} = −1.357553,
σ_1 = −1.366738, matching l. 291–292. Mesh form (b): recomputed m_q − C_q = σ_T + κ_q − R̂_q − g_q, so s′_q = s_q + g_q
(c = 0). CONFIRMED.
REFUTED (side claim, l. 138): "σ_T < 0 for every T". The j ≥ 1 sum diverges like log(1/T) as T → 0; σ_T = 0 at
T ≈ 0.05195 and σ_T > 0 below. The claim holds for T > 0.0520, which covers every window used, so the consequence
"(★)_T ⟺ ℛ ≤ κ − |σ_T|" (l. 145) must be restricted to T > 0.0520 (for smaller T it reads ℛ ≤ κ + σ_T). Repair: replace
|σ_T| by −σ_T throughout; nothing downstream changes.

**Theorem 2 (l. 164–178). CONFIRMED, including (iii).** Key step for (iii): x = pr_Tφ_p = φ_p − τ, τ ∈ 𝒯, and with
A = Arch − Π, Ax = Arch x − Πφ_p + Πτ; each of Πφ_p, Πτ decomposes along 𝒯 ⊕ N′ ⊕ 𝒞 into a part in 𝒩_η + 𝒯 (orthogonal
to E^c ⊂ 𝒞) and a part P_𝒞Π(·) ∈ V_T ⊂ E (orthogonal to E^c). So P_{E^c}Πφ_p = P_{E^c}Πτ = 0 and Bx = P_{E^c}Arch x
EXACTLY. This is exact precisely because V_T contains P_𝒞Π𝒯 as well as P_𝒞Π𝒩_η: dropping the two Tate responses
(the 22-dimensional family of l. 259) breaks (iii). Two precisions the memo should state: (a) "Arch" here contains the
gauge terms, which are null only after compression by P_T; in an untruncated statement this is harmless since
E^c ⊂ P_T, and the model residual 1.5·10⁻³ / 8.75·10⁻⁴ (l. 283–286) is exactly the truncation defect of HᵀH = I;
(b) the statement is an identity of structure, not a smallness statement: ‖P_{E^c}Arch|_{N′}‖ = 0.14 is not small
relative to the margin, and (iii) gives no bound. (ii): 𝒞 = V_T ⊕ E^c orthogonally (E^c = 𝒞 ∩ V_T^⊥), so the iterated
Schur complement is the (L2′) form; CONFIRMED given ROUND_001_C coercivity on 𝒞. (i), (iv) CONFIRMED (min–max, Prop. S).
Comparison with R4 (l. 180–186): honest; the dimension bound is of arena order, the escape is NUMERICAL only.

**Prop. 4 (l. 197–209). CONFIRMED with a notational repair.** x(Πφ_p) = ½G𝒞G_{·p} from Π = ½Σ C_q|φ_q⟩⟨φ_q|.
𝔐 = ½𝔛^T S 𝔛 must read ½𝔛^* S 𝔛 (x(τ_±) and the phases of φ_q are complex). Degrees 1/2/3 in v correct (S affine,
𝒞 linear). On the unprojected family the formula is the form only with the λ = 0 gauge (the λ-gauge is not null
off P_T); with c-gauge only, as written, it is valid on all of L²(I_T).

**Prop. 5 (l. 211–225). CONFIRMED.** Recomputed (i): ∫_{I_T}1_{t>log max(m,n)−T} = 2T − log max(m,n), cross terms
∫1_{log m−T<t<T−log n} = (2T − log mn)_+, factor (1/2T)·¼·2 = 1/4T. (ii) is a correct description of the support
weights; not checked term by term (no claim depends on the explicit W).

**§5.3(i) Selberg rewriting (l. 427–444). DOWNGRADE (partial error).** The Prop. 5(i) product part is a genuine
Dirichlet convolution because N = mn < e^{2T} forces m, n < e^{2T}: CONFIRMED. The companion claim for the mesh
squares, C_q² = 2Σ_N(Λ∗Λ)(N)N^{−1/2}cos(ω_q log N) + … "(no cutoff; N up to e^{4T})" (l. 437–438), is FALSE as written:
for e^{2T} ≤ N < e^{4T} the sum runs only over factorisations with m, n < e^{2T}, which is a truncated convolution,
not Λ∗Λ(N). Correct statement: Σ_{mn=N, m,n∈N_T}Λ(m)Λ(n). The NO-GO conclusion of §5.3 is unaffected.

**§5.3(ii) local Euler factors (l. 446–455). CONFIRMED.** Re z/(1−z), |z| = r, is increasing in cos θ (derivative
∝ r(1−r²) > 0), so the extremes are r/(1−r) and −r/(1+r).

**Lemma 6 (l. 229–242). (a) DOWNGRADE to CONDITIONAL, trivially repairable.** δ_T > 0 needs s_q ≠ 0 for all q, which
is asserted, not proved. For fixed T it fails for at most one value of c per q, so it holds for all c outside a
countable set; the memo should choose c generically and say so. With that, (a) is CONFIRMED (s_q(ϑ) = s_q − (ϑ−1)C_q).
(b), (e) CONFIRMED (structural).

**(SL_T)/(SL′_T) (l. 381–395).** CONFIRMED as NECESSARY for (★)_T (restriction of a_T to E_T ⊂ P_T). The two
constraints are correctly listed. Its "equivalence" with (★)_T only holds together with the Schur correction
(Theorem 2(ii)); the memo says so. The per-mode minors (l. 397–402) are necessary consequences: CONFIRMED.
(SL′_T) carries the sign repair above (−σ_T for |σ_T|).

**NO-GO (identity-based mechanisms on E_T), l. 464–470.** Class: sign mechanisms for (SL_T) built from identities
valid for every Beurling system and for a_P (Λ∗1 = log, Selberg, generalised Selberg, local Euler bounds, the Lévy
identity of Prop. 3). Logic CONFIRMED (an identity holding for a system w for which (SL_{T₁}) fails cannot imply
(SL_{T₁})). Falsifier status: NUMERICAL instances (Beurling 3 → 3.2: −0.2398; a_3: −0.5074; l. 362–365). For the
NO-GO to be PROVED rather than NUMERICAL-instanced, one falsifier value must be certified (interval arithmetic) —
the a_3 margin 0.51 is large enough to make that easy. Status: NO-GO (PROVED logic, NUMERICAL falsifier).
**NO-GO (floor-only Schur class on response enlargements), l. 268–276.** Class: sufficient inequalities
λ_min(A_EE) − ‖B‖²/c ≥ 0 with scalar c. Falsifier status: NUMERICAL (c_need vs λ_min(C)). CONFIRMED as recorded.

Numerical capture (l. 278–282) is labelled NUMERICAL, correctly; its reconciliation with ROUND_005_A Prop. 4.2 is in §5.

---------------------------------------------------------------------------------------------------
## 2. ROUND_005_A (the comb-first Krylov family K_j)

**Lemma 2.1 (l. 56–60). CONFIRMED.** Key step: concavity of φ gives m(τ) ≤ m(t_1) + φ′(t_1²)(τ² − t_1²) ≤ B(τ² − t_1²);
the Dirichlet sines vanish at ±T so the zero extension is in H¹ and (1/2π)∫τ²|F̂|² = ‖F′‖² ≤ (πN_T/2T)²‖F‖²;
N_T < 2Tt_1/π gives strict negativity; codimension ≤ 2. The hypothesis m(3) < 0 is a single-point evaluation,
certifiable; label it as such.

**Lemma 3.2 (l. 123–132). CONFIRMED.** (i) convexity of I; (ii) recomputed: (QV_aRV_{−b}QF)(t) =
1_I(t)1_{t−a∉I}F(t−a+b)1_I(t−a+b), and t − a < T forces t ≤ a − T, while t − a + b > −T forces t > a − b − T.
(iii) follows by inserting Q = 1 − R. The phrase "= 2S_{a+b}-part" in (i) is garbled (QV_{a+b}Q is not 2S_{a+b});
delete it.

**Prop. 3.3 (l. 137–151). CONFIRMED.** Π² = Qσ_v(1 − R)σ_vQ = Qσ_v²Q − 𝔏*𝔏 (R = R* = R²); c_ac_b = ½(c_{a+b} + c_{a−b});
S_{log N} = 0 for N ≥ e^{2T}, so the product sum is a genuine (untruncated) Dirichlet convolution for every surviving
N (both factors are automatically < e^{2T}); the ratio part is ½(1/2π)∫|F̂|²|Σv_nn^{iτ}|². Leak formula: for t > T only
F(t − x_n) with x_n > t − T survives. All checked.

**Prop. 3.4 (l. 160–173). Identity CONFIRMED; sign claim DOWNGRADE to ARGUED.** The four-word expansion of Π³ and the
product-to-sum formula (one pure term, three equal mixed terms) are correct, as is "r = 1 ⟺ prime-power towers".
The claim "near-coincidences ... work against the sign on K_2 (PROVED as a statement about the sign of the
contribution)" (l. 168–170) is not proved: the contribution of class r to ⟨f, Π_P f⟩ is ¾W_3(r)Re c_f(log r) PLUS
polar (Γ) terms, and Re c_f(log r) > 0 is only asserted for "low-frequency vectors" (l. 166), with edge terms not
controlled; moreover Prop. 3.4 is for the uncompressed Π³ whereas Π_ff uses Π_P, and the polar part is 19–48 % of
‖Πe‖² (l. 93–95). Label: ARGUED.

**Prop. 3.5 (l. 176–183). CONFIRMED.** The seed 𝒩_T is Λ-free, so span{(cΠ_P)^ie} = span{Π_P^ie}; a_T^{cΛ} = a_T −
(c−1)Π on the fixed subspace; λ_min of an affine matrix pencil is concave.

**Thm 4.1 (l. 210–219). CONFIRMED** (standard form-level Schur complement; only K ⊂ 𝒟_T is used).

**Prop. 4.2 (l. 223–247). CONFIRMED (i)–(iv) under (H_b) or in the Galerkin model; (v) CONFIRMED as an operator
identity with a constant error in the halo formula.** (ii): a_T(e_α, y) = ⟨Me_α, y⟩ − ⟨Π_Pe_α, y⟩ with e_α ∈ dom M,
y ⊥ e_α. (iii): Gram of the residuals. (iv) recomputed: ⟨f_α, Mf_β⟩ = (Π_PMΠ_P)_ee − Π_eeDΠ_ee (the two cross terms
and the double term combine to one −Π_eeDΠ_ee), and the Π_ff expansion is correct. (v): [M_0, S_x] =
Qc_xR𝔪Q − Q𝔪Rc_xQ from [𝔪, c_x] = 0. ERROR: the off-window kernel of 𝔪 is −½K(|t−s|), not −K(|t−s|): polarising the
Lévy form ¼∬|F(t)−F(s)|²K for F, G of disjoint supports gives Arch(F, G) = −½∬F(t)conj G(s)K(|t−s|). So
(R𝔪QF)(t) = −½∫_I K(|t−s|)F(s)ds (l. 239 and l. 320). The structural statement is unaffected; every Δ-term of §5.3
that contains R𝔪e must be re-evaluated with the factor ½ before any numerical use.

**Cor. 4.3 (l. 249–255). CONFIRMED** (Thm 4.1 with K = K_1 and 4.2(ii); penalty bound by the frame bound λ_max(G)).
Conditional on (H_b) for the spectral cone, as the memo says.

**§5.3 identities (l. 312–329).** α − μ_1 = (1/2π)∫s_T|ê|² CONFIRMED (e ∈ P_T). The others are stated with polar terms
"suppressed in the display"; they are therefore identities for the uncompressed Π only. DOWNGRADE of "(SL_2^{sc}) ⟺
H_2 + Δ ⪰ 0" from PROVED to CONDITIONAL on writing the omitted rank-2 polar terms (which are 19–48 % in size) and on
the halo constant above.

**Internal inconsistency (l. 379–383, 503).** The memo states that the A-generated family "reaches λ_A at the same
dimension" (l. 503) and that "the archimedean steps ... are what reaches the bottom" (l. 382). Its own numbers
(l. 379–380) are 1e−7, 2e−7, 8e−8, 5e−7 at dimension 20, against λ_A = 1.1e−7 (log 2), 3e−12 (½log5), ≲ 1e−14
(0.9, 1.0). Only at log 2 is the Lanczos value at the level of λ_A; elsewhere it is 4–7 orders above. REFUTED as
written; the correct reading is "the A-generated family converges 3–4 orders faster than the Π-generated one".

**NO-GO (l. 460–465).** Class: Π-Krylov family from the Λ-free archimedean negative cone, bounded j, as sign
carrier. PROVED piece: scale invariance (Prop. 3.5(ii)) — so on this family cΛ is a pencil test only. The decisive
part ("the pencil at c > 1 is decided by a near-null pair the comb steps do not generate") is NUMERICAL (j ≤ 6 for the
c = 1.1 test, j ≤ 20 for capture, T ≤ 1.2) and relies on ROUND_003_A Lemma 4 for λ_A(T; 1.1Λ) < 0. Falsifier status:
c = 1.1 at T ≤ 1.0 NUMERICAL (not certified). Label: NO-GO (NUMERICAL evidence, ARGUED for all bounded j); "PROVED
mechanism" overstates.

---------------------------------------------------------------------------------------------------
## 3. ROUND_005_E (the arena band; two-sided Weyl count)

**Lemma 3.0 (l. 146–148). CONFIRMED** (|c_F(u)| ≤ ‖F‖², v_n > 0; it is Paper 46 prop:coer-prime(i)).

**Theorem 3.1 (l. 150–159). CONFIRMED.** Key step: Arch_T − π_+ ≤ a_T ≤ Arch_T + π_− as forms on P_T ∩ 𝒟_T, so
Courant–Fischer gives λ_k ∈ [α_k − π_+, α_k + π_−] index by index; both counts follow. Valid verbatim on every Galerkin
compression with the compressed π_±. Caveat (not an error of the theorem, an error of its use): the numerical "sharp"
band sizes n_P(T) of l. 40–48 and l. 162 were computed with the Galerkin π_+, which is NOT the π_+ of the operator
statement; by ROUND_006_A Theorem 1 the operator value is larger (1.554 vs 1.516 at 0.9; 2.695 vs 2.057 at 1.2).
The reading "single exponential ≈ e^{4T}" (l. 130–138, 222–225) is therefore a truncation artefact and is
withdrawn by ROUND_006_A §5; the memo's own OPEN flag (l. 137–138) was the correct label.

**Prop. 3.2 (l. 169–174). CONFIRMED, with a title correction.** a_T ≤ Arch_T + θ on P_T ⟺ −Π ≤ θ ⟺ θ ≥ π_−, and
δ − θ < α_1 gives a zero count. This is a NO-GO only for the class "lower counts by pointwise comparison"; the title
"no archimedean lower count" overstates it (the test-space remark at l. 171–172 is NUMERICAL and concerns single
eigenvectors only).

---------------------------------------------------------------------------------------------------
## 4. ROUND_006_A (size of the comb form)

**Lemma 1.0 (l. 34–35). CONFIRMED** (real F; Π is a real operator, so the sup over complex F equals the sup over real F).

**Theorem 1 (l. 37–47). CONFIRMED — the modulation argument is complete on P_T.** Key steps checked:
c_{F_τ}(u) = c_{F_0}(u)cos τu + ∫F_0(t)F_0(t−u)cos(τ(2t−u))dt (product-to-sum, exact); Riemann–Lebesgue is needed only at
the finitely many u_n and at u = 0 (norm). The Tate constraints: A(F_τ), B(F_τ) → 0 by Riemann–Lebesgue; P^⊥ has
dimension 2, so ‖F_τ − PF_τ‖ ≤ C(|A(F_τ)| + |B(F_τ)|) → 0 (C depends only on the Gram matrix of e^{±t/2}1_{I_T}); with
‖Π_T‖ ≤ A_T the quadratic form moves by o(1) and ‖PF_τ‖ → 1. Dirichlet's simultaneous approximation gives τ_k = 2πq_k
→ ∞ with cos(τ_ku_n) → 1 for all n ∈ N_T (finite set), and the bounded-q case is handled. The same sequence gives
Π_T(PF_{τ_k}) → Π_T(F_0) for every F_0, hence both π_+ and π_−. Nothing in P_T beyond its codimension 2 is used; the
argument does not need F_0 ∈ P_T. One clarification to add: for the later use in Theorem 6 (a form inequality on
the form domain), choose F_0 ∈ 𝒟_T (e.g. smooth), which costs nothing since the supremum is approached by such F_0.

**Theorem 2 (l. 63–71). CONFIRMED.** For F ≥ 0, AM–GM on the Cauchy–Schwarz product and summation give
½∫F²[V(T+t) + V(T−t)]; Lemma 1.0 transfers to all F and to π_−, ‖Π_T‖. The (HT_T) reformulation (l. 87–90) is
correct (V(s) + V(2T−s) ≤ A_T ⟺ Σ_{n≤a}v_n ≤ Σ_{X/a<n<X}v_n, a = e^s). Cor. 2.1 CONFIRMED (Chebyshev suffices for
V(T)/A_T ≪ e^{−T/2}).

**Theorem 3 (l. 94–101). CONFIRMED.** Recomputed: for F = cosh(t/2)1_{I_T}, c_F(u) = ½∫_{−T+u}^{T}[cosh(t − u/2) +
cosh(u/2)]dt = sinh(T − u/2) + (T − u/2)cosh(u/2); v_n sinh(T − u_n/2) = Λ(n)(e^T/n − e^{−T}); v_n(T − u_n/2)cosh(u_n/2) =
½Λ(n)log(X/n)(1 + 1/n). Transport to P_T by Theorem 1 (F ∉ P_T is irrelevant). Cor. 3.1 (PNT CITED): ½∫_1^Xψ(t)dt/t =
(X/2)(1+o(1)), remaining terms O(Te^T + T²), so π_+(P_T) ≥ e^T(1+o(1)) and liminf ≥ ¼: CONFIRMED.

**Theorem 4 (l. 118–125). CONFIRMED.** e^{|s|/2} = cosh(s/2) + sinh(|s|/2); the cosh part is A(F)B(F) = 0; G = sinh(|s|/2)
has G″ − G/4 = δ; for x ≥ T, u_F(x) = ½e^{x/2}B(F) − ½e^{−x/2}A(F) = 0 (and symmetrically), so u_F, u_F′ vanish at ±T and
integration by parts gives −∫(u_F′² + u_F²/4). Cross-check with ROUND_005_C Prop. 3: on P_T, 2∫_0^{2T}e^{u/2}Re c_F =
−2∫_0^{2T}e^{−u/2}Re c_F, and the right side is ≤ 0 by positive definiteness of e^{−|u|/2} (Fourier transform
1/(¼+τ²) > 0) — consistent. The "Reading" (l. 127–131: the top is reached ONLY by high-frequency packets) is not
implied by Theorem 4, because the fluctuation part ρ_T is not shown to be o(e^T) on low-frequency vectors of P_T:
DOWNGRADE that sentence to ARGUED.

**Lemma 5.1 (l. 135–146). CONFIRMED.** On the span E, Arch(F) < s‖F‖²; with m ≥ C_0 on Ω = {m < s+1} and ≥ s+1 off Ω,
q > 1/(s + 1 − C_0) (s ≥ −1 ensures s + 1 − C_0 > 0); min–max for the time–frequency limiting operator B gives
dim E ≤ (s + 1 − C_0)tr B, tr B = 2T·2τ′/2π. Paper 46 lem:mbounds(ii) (main.tex l. 505–509) gives, for τ ≥ 2π,
m(τ) ≥ log(τ/2π) − 1/τ − 1/(2τ²) ≥ log(τ/2π) − 0.1718 (since lem:mbounds(i) makes m increasing, Ω is an interval),
hence τ′ ≤ 2πe^{s+1.172}; 4e^{1.172} = 12.91. Constants CONFIRMED.

**Theorem 5 (l. 148–154). CONFIRMED with a citation correction.** Chain: 005_E Thm 3.1, Thm 2, Lemma 5.1 (monotone in
s for s ≥ −1). The asymptotic exp(2e^T(1+o(1))) needs A_T = 4e^T(1+o(1)), which is the prime number theorem, not
Chebyshev (Chebyshev gives only exp(O(e^T))). Change "(Chebyshev, CITED)" to "(PNT, CITED)"; the explicit finite
bound is unaffected.

**Theorem 6 (l. 156–161). CONFIRMED (given PNT and the threshold-free form of thm:arena).** θ ≥ π_+ by the packets of
Theorem 1 (with F_0 ∈ 𝒟_T). The lower count: Paper 46 thm:arena (main.tex l. 2786–2808) bounds λ^{ev}_{k+1} ≤
m((2k+3)π/2T) and its proof uses no particular threshold, so N_Arch(s) ≥ #{k ≥ 0 : m((2k+3)π/2T) < s} ≈ Tm^{−1}(s)/π −
3/2; the memo's "⌊Tm^{−1}(δ+θ)/π − ½⌋" is off by one in the additive constant (should be ⌈Tm^{−1}/π − 3/2⌉ with strict
inequality handled), immaterial for the asymptotics 2T exp(e^T(1+o(1))).

---------------------------------------------------------------------------------------------------
## 5. Reconciliation: capture by comb responses (ROUND_005_C §4.2) versus ROUND_005_A Prop. 4.2

Claimed tension: ROUND_005_C (l. 270–272, 278–282) finds that ONE comb step from the Nyquist block captures the
minimiser to 5·10⁻¹⁰ (better than one A-step, 8·10⁻⁹, and one Arch-step, 2·10⁻⁷); ROUND_005_A (l. 376–383, 502–505)
finds that comb steps do NOT reach the near-null pair, which is "reached through the archimedean commutator terms
[M, Π_P]K_1".

Verdict: NO CONTRADICTION between PROVED statements; one overstatement in ROUND_005_A must be corrected.
(a) What Prop. 4.2 PROVES is only: with an M-invariant seed, the Krylov spaces of A and Π_P agree at j = 2, and differ
from j = 3 on by [M, Π_P]K_1 (an identity), and the seed couples to its complement only through the comb (4.2(ii)).
The sentence "the near-null pair is generated by the archimedean commutator terms" is a NUMERICAL reading of §6.1,
not a consequence of Prop. 4.2. Label it NUMERICAL.
(b) The two memos use different seeds. ROUND_005_A seeds with the Λ-free negative spectral subspace of M on P_T
(n_T = 1–2 per sector), which by its own Prop. 4.2(ii) is M-invariant and couples through Π only. ROUND_005_C seeds
with the Nyquist block 𝒩_η (11 resp. 41 modes), defined by s_q ≤ 0 for the FULL symbol m − C (Λ-dependent, already
containing the comb resonances), which is not M-invariant. Theorem 2(iii) of ROUND_005_C is the exact dual of
Prop. 4.2(ii): an M-invariant seed couples through Π; a seed closed under one Π-step (plus Tate responses) couples
through Arch. After one comb step, the residual coupling of E_T is P_{E^c}Arch N′ — precisely the archimedean
direction ROUND_005_A says is needed next. The two pictures are the same picture at different stages.
(c) ROUND_005_C's own table shows that at T₁ the A-step (8·10⁻⁹) and the Π-step (1.9·10⁻⁹) from the block are within
a factor 4 and both are 3 orders below the block alone; the comb's advantage is seed-specific and NUMERICAL.
(d) The genuine inconsistency is inside ROUND_005_A (see §2): "A-generated reaches λ_A at the same dimension" is
refuted by its own table (1e−7 to 5e−7 at dimension 20 against λ_A ≤ 3·10⁻¹² for T ≥ ½log5). Neither family, nor
E_T, reaches λ_A; E_T is closest (5·10⁻¹⁰ vs 3·10⁻¹² at T₁). Also note: ROUND_005_E Table 1.2 shows plain archimedean
planes E_k reach 4.7·10⁻¹² at dimension 28, T = 0.9 — the archimedean ordering alone is competitive with both.

---------------------------------------------------------------------------------------------------
## 6. NO-GO register (class; falsifier status)

1. ROUND_005_C §4.1: floor-only (scalar-coercivity) Schur certificates on response enlargements of the Nyquist block.
   Class: λ_min(A_EE) − ‖B‖²/c ≥ 0, c scalar. Falsifier: none needed (it is a failure of sufficiency), evidence
   NUMERICAL (c_need 2.5–8.9 vs λ_min(C) ≈ 1.3). Label NO-GO (NUMERICAL).
2. ROUND_005_C §5.3(iv): identity-based sign mechanisms on E_T (Selberg, Λ∗1 = log, Euler-factor bounds, Lévy identity).
   PROVED logic; falsifiers a_3 (−0.507) and Beurling 3 → 3.2 (−0.240) NUMERICAL, not certified. Label NO-GO
   (PROVED logic, NUMERICAL falsifier); certifying the a_3 value would make it fully PROVED.
3. ROUND_005_A §7: Π-Krylov family from the Λ-free archimedean negative cone, bounded j. PROVED part: scale
   invariance. Falsifier c = 1.1 not rejected at T ≤ 1.0, j ≤ 6: NUMERICAL. Label NO-GO (NUMERICAL; ARGUED for all
   bounded j). "PROVED mechanism" overstated.
4. ROUND_005_E Prop. 3.2: lower cluster counts by pointwise archimedean comparison. PROVED (trivial); falsifier n/a.
5. ROUND_005_E Result: arena band at threshold A_T as starting block (saturates the Galerkin space) and sharp band as
   sign carrier (Λ-dependent through one scalar, killed by ROUND_004_A Prop. B). NUMERICAL + cited logic.
6. ROUND_006_A Theorem 6: Weyl caps on the cluster from a_T ≥ Arch_T − θ. PROVED given PNT and thm:arena; no
   falsifier needed (impossibility within the declared class).
7. ROUND_006_A §6: "λ_max(Π_T)/A_T → 0" REFUTED (PROVED, Cor. 3.1, PNT); Gram/Toeplitz bound on shifted copies:
   circular (ARGUED; one-line, acceptable).

---------------------------------------------------------------------------------------------------
## 7. Corrections required (summary)

- 005_C l. 138: σ_T < 0 only for T > 0.0520; replace |σ_T| by −σ_T in Prop. 3 and (SL′_T).
- 005_C l. 437–438: the mesh-square identity C_q² is a TRUNCATED convolution for N ≥ e^{2T}.
- 005_C l. 201: 𝔛^T → 𝔛^*; Lemma 6(a): choose the gauge c off a countable set so that s_q ≠ 0.
- 005_A l. 239, 320: halo kernel −½K, not −K; re-evaluate Δ in §5.3.
- 005_A l. 168–170: near-coincidence sign claim PROVED → ARGUED; §5.3 equivalence PROVED → CONDITIONAL (polar terms).
- 005_A l. 382, 503: A-family does not reach λ_A at dimension 20 for T ≥ ½log5; and "generated by commutator terms"
  is NUMERICAL.
- 005_A l. 124 "= 2S_{a+b}-part": delete.
- 005_E l. 40–48, 130–138, 222–225: Galerkin π_+; single-exponential reading withdrawn (006_A).
- 006_A l. 153: Chebyshev → PNT; l. 158: additive constant in the arena count; l. 127–131 reading → ARGUED.
Everything else checked is CONFIRMED.
