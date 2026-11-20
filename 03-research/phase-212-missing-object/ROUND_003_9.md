# ROUND_003_9 — Selection: non-local metric of the theta realization

Selection memo, not a construction memo. Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`;
N = e^{2T}. Sources from 211 cited as HY (`POWER_HYPERBOLIC_MODEL_GRAM.md`), GS
(`POWER_GRAM_SLICES_OBSTRUCTION.md`), CONE001 (`POWER_CONE_001.md`), BRIDGE002 (`POWER_BRIDGE_002.md`).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

### Search performed

- Full primary reading: HY §§1–5 and §§12.2–12.7; CONE001 §§1–2; BRIDGE002 §6;
  `ROUND_001_L.md` §§1–4 (by cited lines), `ROUND_003_4.md`, `OBJECT_SPEC.md`, `RULES_AVOID.md`,
  `LEDGER.md`, `README.md`; README of phase 209; `ANNEX_211_GRAM_HYPERBOLIC.md` §§0–1;
  `phase-114-closing-the-four-rows/114_d_139_THETA_PAIR_METRIC_NO_GO.md` §0 and initial §1.
- grep in `03-research/` (all phases), `04-papers/47*`, `04-papers/48*`,
  `05-meta-and-planning/` for: «Kontorovich», «Lebedev», «métrica no local», «metrica no local»,
  «nonlocal metric», «entrelaz», «intertwin», «Stieltjes», «Herglotz», «traza que represente»,
  «Green positivo». No hits for Kontorovich/Lebedev nor for «métrica no local» as a phrase.
  «nonlocal metric» only in D.139 (phases 114/116, same file). «Green positivo» only in HY, in
  its echoes in the grid/crossword/index and in `POWER_GREEN_PAIR_TP2_SCOPE_111.md` (not opened in full).
  «Stieltjes» in phase 206 (NODE_001: Stieltjes integral against d(ψ − t), another sense).
  «Herglotz» in phases 136–137 (matrix-Herglotz of a compressed resolvent, another object).
- GS §§17–19 I know only through the annex `ANNEX_211_GRAM_HYPERBOLIC.md` §0 and through `RULES_AVOID.md`
  D9, D14, D16; I did not reread them in primary. LINK_014 of 209 only through its statement (Theorem 3 and
  status, l. 151–173). The absence of hits does not prove novelty; §2 moreover shows that there is
  none in the class examined.

### (1) Closest antecedent

- HY §§4–5 (PROVED for the model φ_a = e^{−a cosh 2t}): M_a(u)/u = ½Tr(H + u²/4)^{−1} with
  H = −D_r² + a²e^{2r} positive and independent of u (REP); hence the resolvent identity
  (uR_u + vR_v)/(u+v) = (H + uv/4)R_uR_v and the sum of squares GRAM for all sizes.
- HY §12.6 (PROVED as a realization): space ℋ = L²((0,∞), sech(πω/2)dω) ⊕ ℝ³, Q(v), C, D, B̄, h,
  with ⟨Y_ν(2π), h⟩ = Z(2ν) and the strong equation Y_rr = (b² + ν²)Y + 2DY_r + (−C + 2bB̄)Y.
- HY §12.7 (NO-GO with class PROVED): there is no local, bounded, strictly positive metric M(r) with
  M′ = −DM − MD and −C + D² + 2bB̄ symmetric in M(r).
- `ROUND_001_L.md` Theorem 2.1, Cor. 2.2, Prop. 4.2 (PROVED relative to Herglotz–Riesz, Pick and
  Blaschke, CITED): the ladder K_ij = (L(32+i)+L(32+j))/(63+i+j) is PSD in all sizes if and
  only if M is real-positive on Π = {Re u > 0}, and then M = Σ_k r_k·2u/(u² + τ_k²), r_k ≥ 0. The
  index (README l. 1791, «real kernel of Pick type») and the memo itself record this
  Herglotz-type positivity as a **reformulation of the goal**.
- D.139 (phase 114): for the theta pair (LD, L) in logarithmic coordinate, every positive
  translation-invariant metric defined on the whole domain is zero (the theta vector is in the kernel
  of C = ∂_x + φ′ and its transform does not vanish almost everywhere). It excludes global
  convolution metrics before cutting the Tate moments; it does not exclude non-invariant metrics.
- Phase 209: CONSTRUCTOR_001 (NO-GO of J + compact C), 005 (SPD kernel −R_α), 011 (continuous
  Mellin–Gauss map to a positive kernel; the induced form does not coincide with Q_T: the corrected high
  frequency separates), 012–014 (uniform dominations; LINK_014: every fixed non-negative
  combination AκG + Bκvv* + CΠ with the same a_d has |Q|/E → 0), 016 (positivity only on the image does not
  enlarge the cone). None is a metric of the theta realization; all fail at the link with the
  form, not at the positivity of the auxiliary kernel.

### (2) The object, written

The realization (HY §12.6) and what the metric should give are written in §1. The «metric 𝒢» that the
project rule asks to make explicit is formalized in §2 as the class 𝒞_G of Green identities of
REP type (the only ones that, in the antecedent HY §§4–5, produce GRAM). Lemma 2 proves that in that class
the observable data of 𝒢 (the spectral measure of H seen from the observation) are
**determined** by M and are exactly its Herglotz data; their positivity is the complete
ladder. There are no new ℋ_T, V_T or ρ_T to write: the canonical solution is the space of the boundary
measure of M, whose sign is the goal.

### (3) Does it evade the difficulty of the antecedent?

No. The difficulty of HY §12.7 is local (the metric equation forces incompatible exponents). Passing
to non-local or unbounded metrics avoids that concrete proof, but Lemma 2 shows that any
metric, local or not, that produces an identity of REP type has its observable data fixed and its
positivity is equivalent to the real-positivity of M, already recorded as a reformulation. Non-locality does not
change what has to be signed.

### (4) Connection with global positivity

Exact chain (without margin): REP identity with 𝒢 ⪰ 0 ⟹ K_M PSD in all sizes (Lemma 2(a),
PROVED) ⟹ ladder of BRIDGE002 §6 PSD ⟹ non-negativity of the form on all smooth compact
tests, in particular on P_T for every T (BRIDGE002 §6, PROVED there). The converse up to
«there exists 𝒢 ⪰ 0 in 𝒞_G» also holds (Lemma 2(b)). The connection exists, but it is an equivalence with the
ladder: it is not an intermediate inequality.

### (5) Breaking lines for cΛ and a_P

Λ enters 𝒢 only through M, linearly (§3): L_c(a) = L(a) − (c − 1)Σ_n Λ(n)n^{−a} and
L_P(a) = L(a) + Σ_{p<P}Σ_{k≥1}(log p)p^{−ka}. The line that breaks is r_k ≥ 0 in the
Herglotz representation of M_c or M_P, that is, the positivity of the boundary measure: the same
statement one wants to prove (211 LEDGER C43: the window in c closes at c = 1 from both sides).
There is no intermediate sign step that fails: point (5) without answer. The candidate is not ready for
construction.

## 1. The theta realization and the equation of the metric

**1.1 Objects (HY §12.6, PROVED there).** ℋ = L²((0,∞), ρ(ω)dω) ⊕ ℝ³, ρ(ω) = sech(πω/2),
λ_j = j + ¼; Q(v) = (cos ωv, cosh λ_0v, cosh λ_1v, cosh λ_2v); C multiplication by −ω² and λ_j²;
D multiplication by d(ω) = 1 + ω coth(πω/2) + (15/2)cosh(πω/2)/cosh(2πω) and masses (−29/4, −23/4, −9/4);
B̄ the closure of BQ(v) = sinh v Q′(v) + cosh v DQ(v) on S = span{Q(v)}; h ∈ ℋ with
⟨Q(v), h⟩ = q_θ(v) = Φ(v/2)e^{2π cosh v}. For b = e^r > 0,

    Y_ν(b) = ∫_0^∞ e^{−b cosh v} cosh(νv) Q(v) dv,
    Y_rr = (b² + ν²)Y + 2D Y_r + (−C + 2bB̄)Y,
    ⟨Y_ν(2π), h⟩ = ∫_0^∞ Φ(v/2)cosh(νv)dv = Z(2ν).

**Remark 1.2 (PROVED, one line).** The observation reads only the slice b = 2π: the factor
e^{2π cosh v} of q_θ cancels exactly the kernel e^{−2π cosh v}. The scale variable r and its
equation are scaffolding; the observation of any other slice b ≠ 2π is not Z. A metric in r
is useful only if its Green identity, evaluated at b = 2π, reproduces M = Z′/Z.

**1.3 What the metric should satisfy (translation of the antecedent).** In the model, the identity that
gives GRAM is REP: M(u)/u = ½Tr(H + u²/4)^{−1} with H ⪰ 0 independent of u, obtained from the
Wronskian equation (y_x² z_x′)′ = y_x² and from the symmetry of −D² + a²e^{2r} in L²(dr). For the theta
realization the local necessary condition is that of HY §12.7 (M′ = −DM − MD and symmetry of E in M(r)), excluded
there for local bounded M. A non-local metric is a form 𝒢 ⪰ 0 on functions of r with values
in ℋ (kernel 𝒢(r, s)) in which L = −∂_r² + 2D∂_r + b²I + E(b) is symmetric with boundary conditions
compatible with h; its Green function G_ν would give, by the Wronskian argument, an identity of
the form

    (REP-𝒢)   M(u) = βu + u⟨g, (H + u²)^{−1} g⟩_𝒦,   H ⪰ 0 independent of u, β ≥ 0,

with 𝒦 the completion of (functions, 𝒢), H the operator associated with L and g the boundary vector given by h
(rescaling u ↦ u/2 if the normalization of HY is wanted). That the symmetry of L in 𝒢 implies
(REP-𝒢) is ARGUED (it is the computation of HY §§3–4 with ⟨·,·⟩ replaced by 𝒢; I do not write it because
Lemma 2 makes its exact form unnecessary). What follows classifies (REP-𝒢) directly, without going through
L or r.

## 2. The metric is determined and its positivity is the goal

**Class 𝒞_G.** Triples (𝒦, H, g) and β ≥ 0, with 𝒦 any real Hilbert space (any dimension,
any origin: local, non-local, unbounded), H self-adjoint ⪰ 0 on 𝒦, g ∈ 𝒦, such that
(REP-𝒢) holds for u in a set X ⊂ (0,∞) of uniqueness for holomorphic functions on Π (for
example the ladder 31.5 + ℕ of BRIDGE002 §6, which is of uniqueness by ROUND_001_L Lemma 1.3, or an
interval). Here M(u) = L(u + ½) with L from CONE001 §1:

    L(a) = 1/a + 1/(a−1) − (log π)/2 + ψ(a/2)/2 + ζ′(a)/ζ(a),   ζ′/ζ(a) = −Σ_n Λ(n)n^{−a}.

M is meromorphic on ℂ and odd (Z(u) = C∫Φ(t)cosh(ut)dt is even and entire, CONE001 §2).

**Lemma 2 (circularity in 𝒞_G).**

(a) (PROVED) If (𝒦, H, g, β) ∈ 𝒞_G, then K_M(u,v) = [M(u)+M(v)]/(u+v) is PSD on every finite subset
of X, with the explicit sum of squares

    Σ_ij c_i c_j K_M(u_i,u_j) = β(Σc_i)² + ‖H^{1/2}Σ_i c_iR_ig‖² + ‖Σ_i c_iu_iR_ig‖²,
    R_i = (H + u_i²)^{−1}.

(b) (PROVED relative to `ROUND_001_L.md` Theorem 2.1 and Prop. 4.2, which in turn are PROVED relative to
the classical C1–C3 cited there) Conversely, if K_M is PSD on every finite subset of X,
there exists (𝒦, H, g) ∈ 𝒞_G with β = 0: 𝒦 = ℓ², H = diag(τ_k²), g_k = (2r_k)^{1/2}.

(c) (PROVED relative to the uniqueness of the measure in the Herglotz–Riesz representation and to
Stieltjes inversion, CITED) For every (𝒦, H, g, β) ∈ 𝒞_G, β = lim_{u→∞} M(u)/u and the
spectral measure μ_g of H at g (μ_g(E) = ⟨g, 1_E(H)g⟩) are determined by M. The only freedom is
unitary equivalence on the cyclic subspace of g and the orthogonal complement, which plays no role.

(d) (PROVED, from (a)–(c)) Consequently, for the theta realization, there exists a metric 𝒢 —local or
not, bounded or not— whose Green identity is of type (REP-𝒢), if and only if the ladder of BRIDGE002
§6 is PSD in all sizes; and then the observable part of 𝒢 is canonical: the measure μ_g is the
boundary measure of M, atomic, with masses r_k and positions τ_k² (ROUND_001_L Prop. 4.2). The
positivity of 𝒢 in 𝒞_G is literally the positivity of that ladder.

*Proof.* (a) For u, v > 0 the resolvents commute and
uR_u + vR_v = R_uR_v[u(H + v²) + v(H + u²)] = (u + v)R_uR_v(H + uv). Hence
K_M(u,v) = β + ⟨g, (H + uv)R_uR_vg⟩ = β + ⟨H^{1/2}R_ug, H^{1/2}R_vg⟩ + uv⟨R_ug, R_vg⟩, using that
R_u, R_v, H^{1/2} are self-adjoint and commute and that R_ug ∈ Dom(H) (H^{1/2}R_u bounded). Each summand
is a Gram kernel; the quadratic form is the one written.

(b) By ROUND_001_L Theorem 2.1 there is a real-positive F on Π with F = M on X. M is meromorphic on ℂ and F
holomorphic on Π; X has an accumulation point in Π or is of uniqueness, so M = F on Π (in the
case of the ladder, uniqueness is that of ROUND_001_L Lemma 1.3 applied to M − F, which is meromorphic of
controlled growth on Π: it is exactly the step used there in Cor. 2.2). By Prop. 4.2,
M(u) = Σ_k r_k·2u/(u² + τ_k²), r_k ≥ 0, without linear term. With H = diag(τ_k²) and g_k = (2r_k)^{1/2},
u⟨g, (H + u²)^{−1}g⟩ = Σ_k 2r_ku/(τ_k² + u²) = M(u); g ∈ ℓ² because Σ r_k/(1 + τ_k²) < ∞ (finiteness of
M(1)).

(c) From (REP-𝒢), M(u)/u = β + ∫ dμ_g(λ)/(λ + u²) on X, and both sides are meromorphic/holomorphic on
Π; hence the equality holds on Π, and in particular s ↦ ∫dμ_g(λ)/(λ + s) is determined for s > 0,
with β = lim M(u)/u (dominated convergence: ∫dμ_g/(λ+u²) → 0 if μ_g is finite, which it is because
g ∈ 𝒦). The Stieltjes transform of a finite positive measure on [0,∞) determines the measure
(Stieltjes inversion, CITED). The spectral measure determines H|_{cyclic of g} up to unitary
equivalence (spectral theorem, CITED).

(d) Combine (a), (b), (c) with BRIDGE002 §6 (the ladder is K_M on X = 31.5 + ℕ, shifting
a = u + ½). ∎

**Class and scope of the lemma (circularity NO-GO with class, PROVED in the above terms).**
Class: every Green identity representing M in the form (REP-𝒢), with positive operator
independent of u, on any Hilbert space. In this class the «non-local metric» is not a free
object: it is the Herglotz representation of M, whose positivity is recorded as a reformulation of the
goal (IDX README l. 1791; ROUND_001_L l. 27). Solving the intertwining equation by Mellin or
by any other transform produces, if it produces anything, that same measure.

**Corollary 2.1 (variant with remainder, PROVED relative to ROUND_001_L Theorem 3.1).** If one asks only
M = M_𝒢 + F with M_𝒢 of type (REP-𝒢) non-zero and F real-positive (a positive «controlled remainder»), the
measure of M_𝒢 is dominated by that of M, which under that hypothesis is atomic (it is literally the
rigidity R-comp of `OBJECT_SPEC.md` §3 with M0 = M_𝒢/ε). There is no metric of 𝒞_G that pays part of the
sign and leaves an independent positive remainder: its measure has to be inside that of M.

**Remark 2.2 (modular involution; ARGUED).** The symmetry θ(1/t) = √t θ(t) gives Φ even, Z even and M
odd. In Lemma 2 that parity is already consumed: it is what makes the Herglotz measure
symmetric and (REP-𝒢) depend on u². A factorization 𝒢 = 𝒥*𝒥 with 𝒥 the involution contributes no sign:
every 𝒢 ⪰ 0 is a square, and the parity is shared by any even Φ (any datum with a functional
equation of the same type, for example Davenport–Heilbronn in the corresponding normalization), so
that an argument using only the involution has no line that breaks at that falsifier.
I do not develop it as a lemma.

**Remark 2.3 (explicit kernel of Kontorovich–Lebedev type; PROVED as a computation, without sign).** In the
model, y_x(r) = K_{√x}(ae^r) with K_ν the Macdonald function (∫_0^∞e^{−b cosh v}cosh(νv)dv = K_ν(b),
CITED), and the operator H is diagonalizable by a transform of that family with positive Plancherel
density. That positivity is universal (it does not depend on Φ) and by Lemma 2(c) cannot be
the metric: the metric is fixed by M. An «explicit function» (quotient of Gammas, theta, its
transform) whose positivity were that of 𝒢 would have to encode μ_g, that is the ladder.

## 3. Where Λ enters

Integrality: Φ = Σ_n n^{−1/2}h(t + log n) has coefficient 1 at each n (in the modal form, 1 on
the squares of the theta). Euler product: Σ_{d|n}Λ(d) = log n is exactly the identity that
converts the logarithmic derivative of Σn^{−a} into −ΣΛ(n)n^{−a}. Thus Λ appears in M, linearly and
explicitly, through ζ′/ζ in L (CONE001 §1, PROVED there). In 𝒞_G, by Lemma 2(c), μ_g is the boundary
measure of M, which depends linearly on M; the only non-linearity is g_k = (2r_k)^{1/2}, which adds no
information. Clause O10 is satisfied formally (one works on the Λ side), but without mechanism:
the crossing of the logarithmic derivative is in the definition of M, not in a sign step.

For cΛ: M_c(u) = M(u) − (c − 1)Σ_nΛ(n)n^{−(u+½)} (ARGUED that BRIDGE002 §6 transports with the
Dirichlet inverse of the coefficients of cΛ instead of μ; CONE001 §1 gives the comb term
proportional to c). For a_P: M_P(u) = M(u) + Σ_{p<P}Σ_k (log p)p^{−k(u+½)}. In both cases the line
of Lemma 2 that fails is the existence of (𝒦, H, g) with μ_g ≥ 0, that is (b): exactly the
positivity of the ladder of the altered model. There is no other line.

## 4. Inventory of non-local kernels already proved (only what is pertinent)

- 211, hyperbolic model (HY §§4–5): positive Green of all orders, PROVED; without transfer
  (§6–7: positive mixtures and convolutions do not transfer; §§9–12.4: scale flow, prefactors,
  scalar drifts, excluded in their classes).
- 211, HY §12.7: local bounded metric, NO-GO. GS §2.3: translational Hankel factorization of A
  excluded. GS §4.3: references G0, H0 not PSD. GS §§17–19 (via the annex): resonant sum of squares
  with margin, comparison Off against E_y refuted (pairs k, k+1), thermal graph and Q_B; no
  kernel that represents A with controlled remainder.
- 114 D.139: global translational metric of the theta pair, zero.
- 209: auxiliary positive kernels (005, 011) without link to the form; fixed dominations (012–014)
  fail with |Q|/E → 0; 016 does not enlarge the cone. Common failure: the positive kernel does not see the sign of the
  form; the identification with the form loses the part that carries the sign.

## Result

No new mechanism, with one circularity NO-GO piece with class (PROVED in the terms of
Lemma 2, relative to ROUND_001_L and to CITED classics). The «non-local metric» of the theta realization,
within the class of Green identities of REP type (positive operator independent of u, any
Hilbert space, local or not), is determined by M in its observable part, and its positivity is the ladder
of BRIDGE002 §6, already recorded as a reformulation. The candidate does not pass the selection gate.

## What was proved

- Lemma 2(a): REP-𝒢 ⟹ K_M PSD with explicit sum of squares (PROVED).
- Lemma 2(b)–(d): converse, uniqueness of the observable data and equivalence with the ladder (PROVED
  relative to ROUND_001_L Theorem 2.1, Prop. 4.2 and to Herglotz–Riesz/Stieltjes CITED).
- Corollary 2.1: a metric of 𝒞_G with real-positive remainder falls into the rigidity R-comp (PROVED relative
  to ROUND_001_L Theorem 3.1).
- Remark 1.2: the realization §12.6 observes only the slice b = 2π (PROVED, direct computation).

## What failed and why

- The metric does not appear as a free object: in 𝒞_G its data are the Herglotz data of M; solving the
  intertwining (by Mellin or by another route) cannot give anything else. Circularity, not impossibility
  of the sign.
- The modular involution and the explicit Plancherel densities are universal or shared by
  falsifiers with functional equation; they do not carry the breaking line (ARGUED).
- Point (5): for cΛ and a_P the only thing that fails is the positivity of the boundary measure, which is the
  altered goal.

Remaining NOT excluded:
1. Green identities not of REP type: operator depending on u in a non-resolvent way,
   indefinite (Kreĭn) forms with a non-radical neutral vector (`ROUND_003_4.md` §3, point 1), or
   identities on A(t,s) that do not pass through M and use a structure that Lemma 2 does not see (for
   example, building the Gram vectors of A from arithmetic operations with algebraic
   verification, as HY §5 in the model). The latter is (G) itself on the ladder, without object.
2. Non-local metrics that give (REP-𝒢) only for a part of M with a remainder that is not
   real-positive (outside Corollary 2.1).
3. Realizations different from §12.6 (other Q, other non-continuous observations).

## Concrete next step

Do not relaunch the «non-local metric of the theta realization» in the REP class: record Lemma 2 next to
the reserve entry for non-local metrics (memory of selections and `RULES_AVOID.md` D15) as
circularity with class. A reopening would have to leave the class 𝒞_G: write an identity that
represents A or K_M with an operator depending on u in a non-resolvent way, or with an indefinite metric,
and point out the line that breaks for cΛ and a_P before any derivation.
