# Round 4, zone 1 — Quadratic divisor defect entering additively (selection memo)

Selection memo, not a construction memo. Target (★): λ_A(T) ≥ 0 for all T, with the definitions of
`../phase-211-sign-sandbox/STATEMENT_001.md`. N = e^{2T}, 𝒩 = {n : 2 ≤ n < N}. Labels: PROVED /
CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

Notation. For a weight a ∈ ℝ^𝒩: γ_n(F) = 2n^{−1/2} Re c_F(log n); a_T^{(a)}(F) = Arch(F) − Σ_n a(n)γ_n(F);
b_T(F) = Σ_n Λ(n)γ_n(F), so that a_T = Arch − b_T. Atoms ℓ_k(a) = Σ_{d|k, d≥2} a(d) − log k, k ∈ 𝒩.
U is the incidence matrix (Ue)_k = Σ_{d|k} e_d (unitriangular; U^{−1} is the truncated Möbius
convolution), and ℓ(a) = U(a − Λ) because UΛ = log.

Format examined (𝔉): for each F ∈ P_T ∩ 𝒟_T a symmetric matrix K(F) ⪰ 0 indexed by 𝒩 (entries
quadratic in F) and, for every weight a of a class 𝒜 ∋ Λ,

    a_T^{(a)}(F) + 𝔇_a(F) = ‖V_T(a)F‖² + ρ(a; F),   𝔇_a(F) = ⟨ℓ(a), K(F) ℓ(a)⟩,   ρ ≥ 0 manifest.   (𝔉)

## Cross-check

### What was searched and where

Grep in `03-research/` (all phases), `04-papers/47` and `48`, `05-meta-and-planning/` (index and
crossword) and the grid for: "defecto de divisores", "divisor defect", "δ_a(", "penalt", "penaliz",
"Lagrang", "augmented", "aumentad", "joint positivity", "positividad conjunta", "window in c",
"(c − 1)²", "inf over a", "stability", "Moreau", "𝒦_D2", "BARRIER_D2". Opened as primary sources:
phase 197 `BARRIER_D2_001_DEFECT_STABILITY_SPLITTING_AND_CONTINUATION_NO_GO.md` (in full) and
`AUDIT_197_HOSTILE.md` §(f) (the gate (D2)); phase 170 `R170_866` §§0–3, `R170_868` §§0–3 and §7; phase
211 `LEDGER.md` C35, C39, C43, `ROUND_021_A.md` Lemma 3.3 and §3.4, `ROUND_017_A.md` table and readings
(l. 135–163), and from `ROUND_002_E.md` and `ROUND_003_A.md` the statements (Lemmas 1–3, Cor. 4; Lemmas 3–4);
from this phase `ROUND_003_6.md` and `ROUND_003_2.md` in full, `ROUND_003_4.md` Lemma 4, `REVIEW_003.md`,
`LEDGER.md`, `RULES_AVOID.md`, `OBJECT_SPEC.md`, `README.md`, `BRIEF_CONSTRUCTOR.md`; the entries of the
index README l.422 and 06 l.89–90. The matches for "penalt/Lagrang/augmented" (≈ 400 files) were not
opened one by one: from context they are unrelated uses (Lagrangians of Tate constraints, augmented
certificate matrices). Not opened as primary sources: `R161_030` (its summary in `RULES_AVOID.md`
K2 and `ANNEX_161_FILES_1.md` is used), `R170_869` (its status in `RULES_AVOID.md` I2 is used), the INV_P/INV_Q memos
of phase 193 that BARRIER_D2_001 declares subsumed, and the P48 chapter on stability (the grep only
returned "sparse stability", unrelated). A search without matches does not prove novelty.

### (1) Closest antecedent

**Phase 197, `BARRIER_D2_001`, Theorem 1 (PROVED there; audited in `AUDIT_197_2.md`; index README
l.422, NO-GO of class 𝒦_D2).** For any class of combs 𝓔 ∋ Λ and any defect Δ ≥ 0 with
Δ(Λ) = 0, the stability inequality (I_T; C): λ_A(T; a) ≥ −CΔ(a) on 𝓔 is equivalent to positivity at
Λ conjugated with an unsigned rigidity of Δ; the necessary condition (Rig^w) is
Δ(a) ≥ C^{−1}(⟨a − Λ, w_T⟩ − μ), with w_T the correlation vector of the minimizer. The format (𝔉)
implies, taking the infimum over F, an inequality of this type with Δ(a) = sup_{‖F‖=1} 𝔇_a(F). The difference
in form is that here the defect depends on F, is quadratic in the atoms, and the manifest identity is
required for each F, not the inequality between infima.

Antecedents of the pieces: `R170_866` (the form ℒ_N = 𝒟_N*𝒟_N with kernel exactly ℝ(Λ,1), which is
𝔇 with K = diag(1/k) without F); `R170_868` §3 (every positive linear extension preserving the null line
is 𝒟_N*(I + ΣQ_j*Q_j)𝒟_N, a change of metric); `ROUND_003_6.md` Lemma 3 and (4.4) (the only written
quantity that distinguishes c = 1 is (c − 1)b_T); `ROUND_003_2.md` Lemmas 1 and 3; `R161_030` (oriented variance,
of degree two and generic); 211 C43 and `ROUND_021_A` Lemma 3.3 (window J_R ≍ λ₀/K₀).

### (2) Genuinely new object

There is no object (ℋ_T, V_T, ρ_T) that passes. What is new is a lemma that decides the whole format (§1):
(𝔉) for all weights is equivalent, pointwise in F, to the inequality with margin

    a_T(F) ≥ ¼ ⟨η(F), K(F)^+ η(F)⟩,   η(F) := U^{−T}γ(F),   η_d(F) = Σ_{m: dm<N} μ(m) γ_{dm}(F),     (M_K)

plus η(F) ∈ ran K(F). It is a pointwise, quadratic version of BARRIER_D2_001 Theorem 1(c), with the
linear term written out (the "first jet" of `R170_868`) and with the quantitative consequence along
cΛ (Lemma 2). It is not a sign object: it is the exact description of what (𝔉) requires.

### (3) Does it avoid the antecedent's difficulty?

No. The difficulty of BARRIER_D2_001 is that the whole sign stays at the point Λ. Passing to a
quadratic defect depending on F does not change this: a term that vanishes to second order at Λ cannot pay
the first-order term −⟨ℓ, η(F)⟩, so (𝔉) forces a_T(F) to have margin (M_K) at each
F. It is stronger than (★), not weaker. The case of `R170_868` repeats literally: 𝔇 is a change of
metric (F-dependent) on the image of 𝒟_N and loses the first jet (Lemma 0 and Lemma 1).

### (4) Identity connecting to the complete form on P_T

At a = Λ, (𝔉) is exactly (G): 𝔇_Λ = 0. Away from Λ, by Lemma 1, (𝔉) can always be written as:

    a_T^{(a)}(F) + 𝔇_a(F) = [a_T(F) − ¼⟨η, K^+η⟩] + ⟨ℓ(a) − ½K^+η, K(F)(ℓ(a) − ½K^+η)⟩,

so the only signed statement is (M_K), at Λ. The connection with global positivity exists
and is trivial (evaluate at Λ); the format contributes no mechanism.

### (5) cΛ and a_P: why the remainder stops being ≥ 0

In (𝔉) the remainder does not stop being ≥ 0 for cΛ nor for a_P: the identity remains valid and what breaks is
the conclusion, because 𝔇 > 0 absorbs the negativity (a_T^{(cΛ)} ≥ −(c − 1)²Q; a_T^{(a_P)} ≥ −Q for
P > N, since a_P vanishes in the window and ℓ(a_P) = −log). This satisfies R3-i to the letter, but Lemma 1
shows that this breaking is automatic for any K satisfying (M_K) and contains no sign. Quartets
and f_t have the same Λ(n), n < N: (𝔉) at their weight is (𝔉) at Λ, it does not separate them (RULES_AVOID §E).

## 1. Lemmas

### Lemma 0 (every semidefinite quadratic defect vanishing on the line is of this format; PROVED)

Let q be a positive semidefinite quadratic form in (a, c) ∈ ℝ^𝒩 ⊕ ℝ with q(Λ, 1) = 0. Then there exists
K̃ ⪰ 0 with q(x) = ⟨𝒟_N x, K̃ 𝒟_N x⟩, 𝒟_N(a,c)_k = k^{−1/2}((a∗1)(k) − c log k).

*Proof.* For q ⪰ 0, q(v) = 0 implies that v is in the radical (Cauchy–Schwarz:
|q(v,x)|² ≤ q(v)q(x) = 0). Hence q vanishes on ℝ(Λ,1) = ker 𝒟_N (`R170_866` Thm. 2.1) and descends to the
quotient, which 𝒟_N identifies with ℝ^𝒩 by surjectivity (`R170_868` §1). ∎

Reading: (𝔉) with c = 1 fixed is the most general semidefinite quadratic defect vanishing at Λ; K(F)
is a metric on the image of 𝒟_N, as in `R170_868` (3.3), now F-dependent.

### Lemma 1 (Legendre equivalence; PROVED)

Let 𝒜 = ℝ^𝒩 (all real weights). For each fixed F the following are equivalent:
(i) a_T^{(a)}(F) + 𝔇_a(F) ≥ 0 for all a ∈ 𝒜;
(ii) η(F) ∈ ran K(F) and a_T(F) ≥ ¼⟨η(F), K(F)^+ η(F)⟩.
In particular (𝔉) on 𝒜 implies (★) with the margin (M_K), and if (ii) holds the identity of §(4)
gives the right-hand side as a number ≥ 0 plus a square.

*Proof.* With e = a − Λ, Σ a(n)γ_n = b_T + ⟨e, γ⟩ and e = U^{−1}ℓ, hence ⟨e, γ⟩ = ⟨ℓ, U^{−T}γ⟩ = ⟨ℓ, η⟩;
(U^{−T}γ)_d = Σ_{k: d|k} μ(k/d)γ_k. Thus a_T^{(a)}(F) + 𝔇_a(F) = Φ_F(ℓ) := a_T(F) − ⟨ℓ, η⟩ + ⟨ℓ, Kℓ⟩, and
ℓ = ℓ(a) ranges over all of ℝ^𝒩 as a does (U invertible). If η ∉ ran K = (ker K)^⊥, there is v ∈ ker K with
⟨v, η⟩ > 0 and Φ_F(tv) = a_T − t⟨v, η⟩ → −∞: (i) fails. If η ∈ ran K, completing the square
Φ_F(ℓ) = a_T − ¼⟨η, K^+η⟩ + ⟨ℓ − ½K^+η, K(ℓ − ½K^+η)⟩, whose minimum is a_T − ¼⟨η, K^+η⟩. ∎

Answer to (iii) of the task, a = 0 and a large: a = 0 gives Arch(F) + Q(F) ≥ 0 with Q(F) := ⟨log, K(F) log⟩;
the leading coefficient for large a is ⟨·, K·⟩ ≥ 0. Neither extreme is false for large
K: the effective constraint is in the neighbourhood of Λ (first jet), and it is (M_K).

### Lemma 2 (along cΛ; PROVED)

Assume (𝔉) for all cΛ, c ≥ 0 (every class containing the weights ≥ 0 satisfies this). Since
ℓ(cΛ) = (c − 1) log and ⟨log, η⟩ = ⟨U^{−1}log, γ⟩ = ⟨Λ, γ⟩ = b_T,

    a_T(F) − (c − 1) b_T(F) + (c − 1)² Q(F) ≥ 0   for all c ≥ 0 and all F.

(a) λ_A(T; cΛ) ≥ −(c − 1)² Q_T, with Q_T := sup_{‖F‖=1} Q(F).
(b) If b_T(F) ≥ 0, or |b_T(F)| ≤ 2Q(F): a_T(F) ≥ b_T(F)² / (4Q(F)).
(c) If u ∈ P_T is an exact null vector of a_T with Q(u) < ∞, then b_T(u) = 0 and Arch(u) = 0.

*Proof.* a_T^{(cΛ)} = a_T − (c − 1)b_T gives (a). (b): c − 1 = b/(2Q) ≥ −1 in both cases. (c): if
b(u) > 0, (b) gives 0 ≥ b²/(4Q) > 0; if b(u) < 0 and |b| ≤ 2Q, likewise; if b(u) < −2Q(u), c = 0 gives
0 + b + Q ≥ 0, contradiction; if Q(u) = 0, c → ∞ gives b ≤ 0 and c = 0 gives b ≥ 0. Hence b(u) = 0 and
Arch(u) = a_T(u) + b_T(u) = 0. ∎

Answer to (i), a checkable necessary condition against C43. Over all F: the discriminant
b_T(F)² ≤ 4a_T(F)Q(F) (with b ≥ 0); at the near-minimizers u (a_T(u) ≈ λ_A): Q(u) ≥ b_T(u)²/(4λ_A); and at
each c outside the window J_T: Q_T ≥ −λ_A(T; cΛ)/(c − 1)². The window that closes at first order
(c_+ − 1 ≍ λ_A/b_T(u), 211 C43, `ROUND_021_A` Lemma 3.3, `ROUND_017_A` reading (i)) is compatible with (𝔉)
only if Q is of order b_T(u)²/λ_A on the minimizer. In an exact-contact window, (c) requires
b_T ≡ 0 at the null vector, i.e. exact tangency with zero slope, which 211 `ROUND_003_A` Prop. 2
describes as a codimension-one coincidence (there the computed background has Π > 0: NUMERICAL).

### Corollary 3 (bounded kernels; CONDITIONAL and NUMERICAL)

Class 𝒦_b: K(F) ⪯ κ_T‖F‖² I with κ_T fixed. It includes the two natural kernels of the task:
- K_{kk'}(F) = (kk')^{−1/2}⟨S_{log k}F, S_{log k'}F⟩ (compressed translations, ‖S‖ ≤ 1): it is the Gram of
  w_k = k^{−1/2}S_{log k}F, hence κ_T ≤ Σ_{k<N} 1/k ≤ 2T, and Q(F) ≤ (Σ_{k<N} log k/√k)²‖F‖²;
- that of `R170_866` tensorized, K = diag(1/k)‖F‖²: Q(F) = (Σ_{k<N} log²k/k)‖F‖².

(PROVED) In 𝒦_b, (𝔉) over all weights implies a_T(F) ≥ |η(F)|²/(4κ_T) for ‖F‖ = 1, and therefore every
unit near-minimizer u (a_T(u) ≤ λ_A + ε) satisfies |η(u)|² ≤ 4κ_T(λ_A + ε). With P47 cor:margin1
(CITED: λ_A(T) ≤ 4·10⁹ T e^{−15.449T} for T ≥ 1): |η(u)| ≤ 4·10^{4.8} T e^{−7.72T}, and by Lemma 2(b)
|b_T(u)| ≤ 2(Q_T λ_A)^{1/2} with Q_T polynomial in N.
(CONDITIONAL) If b_T(u_T) does not decay faster than a power of N on the near-minimizers, no
kernel of 𝒦_b with κ_T, Q_T polynomial in N realizes (𝔉) for large T. There is no PROVED lower bound for
|b_T(u)|: the degenerate case w_T = 0 is not excluded in phase 197 either (`AUDIT_197_HOSTILE` §(e)).
(NUMERICAL, values recorded in 211 `ROUND_017_A`, not recomputed here) At T = 1, even Galerkin:
λ_A(1; (1 + 10^{−20})Λ) ≈ −3.2·10^{−22}, hence Lemma 2(a) requires Q_1 ≥ 3.2·10^{18}; at T = 0.8,
λ_A(0.8; (1 + 10^{−10})Λ) ≈ −3.8·10^{−13} requires Q_{0.8} ≥ 3.8·10^7. For the two natural kernels at
T = 1 (n ≤ 7): Q_1 ≤ (Σ_{k=2}^{7} log k/√k)² ≈ 4.004² ≈ 16.0 and Q_1 = Σ_{k=2}^{7} log²k/k ≈ 2.72. Both
violate the necessary condition by ≥ 17 orders of magnitude. A K satisfying it has to be
≳ b_T(u)²/λ_A precisely on the bottom of a_T, i.e. be a functional tuned to the minimizer
(pattern B9; ARGUED).

### Answer to (iv): `R170_868`/`869` on this format

`R170_868` closes the linear rows that annihilate the null line: they factor through 𝒟_N and every positive
extension is a change of metric that loses the first jet. The format (𝔉) is quadratic, not linear, in
𝒟_N, but by Lemma 0 it is exactly a change of metric (F-dependent) of ℒ_N, and Lemma 1 makes
the loss of the first jet precise: the derivative of 𝔇_a at Λ is zero, the first-order term
−⟨ℓ, η(F)⟩ is paid only by a_T(F), and that is why the margin (M_K) is needed. That K depends on F does not escape: the
argument is pointwise in F. Escaping requires one of the three exits of `R170_868` §0: leaving the coefficient
space (boundary coordinate β_T), a term non-polynomial in ℓ that does not vanish to second order
(which then stops being ≥ 0 near Λ in the direction of η, by the same computation), or not annihilating the line
(so that 𝔇_Λ ≠ 0 and (𝔉) at Λ is no longer (G)). `R170_869` (every linear use falls in the ideal Q𝒟_N) does not
apply to the letter to a quadratic term, but by Lemma 1 the only use of the format at Λ is linear:
evaluation.

## Result

Essentially a repetition, plus a short PROVED lemma that closes the format as stated. The format
(𝔉) is the pointwise, quadratic version of gate (D2) of phase 197 (`BARRIER_D2_001`
Theorem 1, NO-GO of class 𝒦_D2) and a change of metric in the sense of `R170_868`. Lemma 1: over all
weights, (𝔉) is equivalent to the inequality with margin (M_K) at Λ, stronger than (★); the defect contributes no
sign. For the natural kernels the margin is incompatible with what is recorded (NUMERICAL at T = 0.8, 1;
CONDITIONAL in general). No candidate ready for construction.

## What was proved

1. Lemma 0 (PROVED): every semidefinite quadratic defect in (a, c) vanishing at (Λ, 1) is ⟨𝒟_N·, K̃𝒟_N·⟩.
2. Lemma 1 (PROVED): (𝔉) over all weights ⟺ η(F) ∈ ran K(F) and a_T(F) ≥ ¼⟨η, K^+η⟩ for each F, with
   η = U^{−T}γ the vector of correlations with Möbius weights. The extremes a = 0 and large a do not constrain.
3. Lemma 2 (PROVED): along cΛ, λ_A(T; cΛ) ≥ −(c − 1)²Q_T; a_T ≥ b_T²/(4Q) when b_T ≥ 0; at an
   exact null vector, b_T = Arch = 0. A checkable necessary condition against C43.
4. Corollary 3: in the class of bounded kernels, |η(u)|² ≤ 4κ_T(λ_A + ε) at near-minimizers (PROVED);
   impossibility for large T CONDITIONAL on a polynomial lower bound for |b_T(u)|; violation by
   ≥ 17 orders at T = 1 for the two natural kernels (NUMERICAL, with values recorded in 211).

## What failed and why

- A term vanishing to second order at Λ does not pay the first-order term in the weight; that term
  is linear and falls on a_T(F), which must have margin. It is the first-jet loss of
  `R170_868`, now in the quadratic version.
- The "breaking under cΛ by a written term" that the format satisfies is automatic for any K
  satisfying (M_K): the conclusion about a_T^{(c)} fails because 𝔇 > 0, but that contributes no sign at Λ.
- The sign lives in (M_K) at Λ, just as in phase 197 it lives in WP_T(Λ).

NOT excluded (delimitation; none of this has a written object):
1. kernels K(F) unbounded in L² and not tuned to the minimizer: Lemma 1 only says they must satisfy
   (M_K), and Corollary 3 only covers the bounded class; with K relatively bounded by the norm N_T of
   R3-h the conclusion is the same (ARGUED: near-minimizers have bounded N_T norm);
2. classes 𝒜 containing neither a neighbourhood of Λ nor the line cΛ (for example, only Euler combs with
   integer exponents): Lemma 1 uses all directions, Lemma 2 the line; on discrete classes
   around Λ the linear term is not forced;
3. defects that neither vanish to second order at Λ nor are polynomial in ℓ, and the boundary coordinate β_T
   of `R170_868` §5;
4. the lack of a PROVED lower bound for |b_T| on the near-minimizers, which would turn
   Corollary 3 into an unconditional NO-GO for the bounded class.

## Concrete next step

Do not build on this format. Record in the index (row of phase 197, BARRIER_D2_001), in the grid and in
the ledger: "Phase 212, additive quadratic divisor defect (format a_T^{(a)} + ⟨ℓ(a), K(F)ℓ(a)⟩ =
‖V(a)F‖² + ρ): repetition of BARRIER_D2_001 Thm. 1 and of `R170_868` §3 in pointwise version; Lemma 1
PROVED: equivalent to a_T(F) ≥ ¼⟨η, K^+η⟩ with η = U^{−T}γ (target plus margin); Lemma 2 PROVED: λ_A(T; cΛ)
≥ −(c − 1)²Q_T; bounded kernels incompatible with the recorded window (NUMERICAL T = 0.8, 1;
CONDITIONAL in general). Global sign OPEN." Before recording it, a second reading should verify the
change of variables ⟨e, γ⟩ = ⟨ℓ, U^{−T}γ⟩ and the case Q(u) = 0 of Lemma 2(c). The piece that would turn
Corollary 3 into an unconditional NO-GO is a lower bound for |b_T| (or for |η|) on the near-minimizers;
it is the same gap w_T ≠ 0 of phase 197 and is not proposed as a route.
