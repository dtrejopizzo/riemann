# Exponent ledger of Part II of the 7/8 manuscript

Result. Every inequality of Part II that enters the final certificate (Sections 12, 15, 16, 19,
20 and the statements of Lemmas 17.1, 18.1 and Proposition 19.2) is listed below with the
exponent it contributes, written as a function of the geometry (ℓ, b, l_x, l_y, h), the reference
exponent σ₀, the bin variable δ = 2a − 1, the slot mean q, the row exponent R and the row scale
d. From these inputs formula (20.4) for E(d), the floor bound (20.5), the endpoint bound (20.7),
the certificate of Lemma 20.2 (constant C₀ = −1/48, lower bound 49/440640), the intermediate
bound (20.11) and the small-row saving 63/800 are rederived and the arithmetic is verified
symbolically (PROVED, as arithmetic; the analytic statements themselves remain CITED). The
general endpoint exponent is

    E(h) = C_geom + (1/2 + ℓ)δ + ℓq − h(1 − R),      C_geom = 2/3 + b/6 + ℓ − σ₀,

in agreement with phase 209 (QRH_HIGH_CANDIDATE_AUDIT, Section 3). The decisive finding is
that the moment estimates (Lemmas 17.1, 18.1, 17.6) and the detector (Proposition 8.3) enter
E(h) only through the term −h(1 − R), and Proposition 19.2 never gives R < 1 − δ; hence the
best conceivable δ-dependence of the certificate is C_geom − bδ/2, and the certificate at any σ₀
requires C_geom ≤ 0, i.e. σ₀ ≥ 2/3 + ℓ + b/6, with no help from the moments. Combined with the
low template σ₀ ≥ 11/12 − ℓ/4 + (5ℓ − 1)₊/8 (phase 209, QRH_FOUR_FIFTHS_ATTEMPT), the two
constraints meet at ℓ = 1/5 with value 13/15. At σ₀ = 4/5 the published geometry is short by
3/40 on the low side and by 13/240 (δ → 0) on the high side; the ℓ = 1/5 geometry is short by
1/15 and 1/12 respectively. Label of the whole memo: PROVED (arithmetic and the reduction of
the certificate to the two scalar constraints) on top of CITED inputs; no 4/5 statement.

## 1. Conventions and the fixed relations of the geometry

All statement numbers refer to the 7/8 manuscript. Z is the probe scale; a physical row u has
q_u ≍ U = Z^d. The geometry of Part II is (12.4):

    b = 1/8,  h = 13/16,  ℓ = 1/6,  l_x = 1 + ℓ − h = 17/48,  l_y = l_x + b = 23/48,
    X = Z^{l_x},  Y = Z^{l_y},  M = l_x + l_y = 5/6,  M + ℓ = 1.

Three relations are structural and are used inside proofs, not only as numerical choices:

    (G1)  l_y = l_x + b          (definition of the additive length);
    (G2)  l_x + l_y + ℓ = 1      (the completed scale Z q_{p_J^c}·X′Y′ balance, used in Lemma 15.1
                                  through M′ + ℓ′ − 1 = −3d);
    (G3)  h = 1 + ℓ − l_x        (used in the proof of Lemma 10.4 to pass from the contour
                                  bookkeeping to (10.15)).

Hence l_x = (1 − b − ℓ)/2, l_y = (1 + b − ℓ)/2, h = (1 + 3ℓ + b)/2. The reference exponent is

    C(s) = C_II(s) = l_x/2 + s − 1 + h/6 = s − 11/16         ((12.3), (15.9)),

so the normalization itself depends on the geometry: C(σ₀) = σ₀ − 1 + l_x/2 + h/6.

Standing hypotheses of Part II (12.1)–(12.2), CITED:

    0 < Δ = β* − 7/8 ≤ 1/24,    κ = 2β* − 1 = 3/4 + 2Δ ≤ 5/6,    a ≤ β*,    δ = 2a − 1 ≤ κ ≤ 5/6.

The upper bound 1/24 comes from Part I (β* ≤ 11/12, Theorem 3.1). The bin grid of Lemma 8.1
starts at a = 51/100, so δ ≥ δ₀ = 1/50 and the floor bin a = 51/100 carries no zero witness.

## 2. The ledger

Each entry: statement; exponent contributed; hypotheses and ranges; where the range is used.

### 2.1 Low side

L1. Lemma 15.1 (compensated completed-row norm). For a rescaled subset J of total length
d ∈ [0, ℓ], with M′ = M − 2d, ℓ′ = ℓ − d:

    Σ_{0<q_m≪Q} |B^J_{m,σ}(Z)|² ≪ Z^{M′ + ((d − 1/6)/4)₊ + ε} = Z^{M′ + ε}.

Exponent: M′. Hypotheses: Lemma 14.3 (reflected energy), Lemma 4.5/4.6, the fixed slot system.
Range use: the proof has two branches; the second branch (15.3) gives the energy
M′ + (1 + 3ℓ′ − 2M′ − 2Δ_H + θ_N)/4, and the identity 1 + 3ℓ′ − 2M′ = d − 1/6 uses the
published values; in general the loss is (5ℓ − 1 + d)/4 (phase 209, QRH_FOUR_FIFTHS_ATTEMPT
Section 3, checked here against the displayed (15.3)). At ℓ = 1/6 the loss is clipped to zero for
every d. This is a theorem-type input: the loss is a property of the reflected energy, not a choice.

L2. Proposition 15.2 (additive Gram bound). For P_a = Y′²/Q ≥ 1,

    Σ_{q_m≪Q} |A_m|² ≪ (1 + |ν|)^{J_Gr} (Q/Y′)(1 + P_a^{1/6} + P_a²/Y′) Z^ε.

Exponent: (Q/Y′) P_a^{1/6}, provided P_a²/Y′ ≪ P_a^{1/6}. Hypotheses: P_a ≥ 1, Q, Y′ ≥ 1 in
polynomial ranges. Range use (proof of Proposition 15.3): P_a = q_{b*}^{-1} Z^b, so b > 0 is needed
for P_a ≥ 1 at large Z; and l_y − d − 11b/6 ≥ 1/12 > 0 for the absorption P_a²/Y′ ≪ P_a^{1/6}
(in general l_y − ℓ − 11b/6 ≥ 0, i.e. ℓ ≤ 1/3 − 8b/9; phase 209 Section 5).

L3. Proposition 15.3 (compensated low estimate). Cauchy–Schwarz of L1 and L2 with the tuple
count Z^{d+ε}, coefficient Z^{−3d/2} and (X′)^{1/2} ≍ X^{1/2} Z^{−d/2}:

    |I_{η,modified}(Z)| ≪ Z^{l_x/2 + b/12 + ε},   additional exponent per subset f(d) = −d ≤ 0.

Exponent: l_x/2 + b/12 = 3/16 = C(7/8). Hypotheses: those of L1, L2, plus M′ ≥ 1/2,
l_y − d ≥ 5/16 for the thresholds. Together with (15.9) this fixes the low-side equation

    σ_low:  l_x/2 + b/12 + (5ℓ − 1)₊/8 = C(σ_low)   ⟺   σ_low = 11/12 − ℓ/4 + (5ℓ − 1)₊/8,

where the clipped term is L1's second-branch loss halved by Cauchy–Schwarz (phase 209,
Section 4; the published case ℓ = 1/6 gives exactly 7/8). The low margin m_lo = Δ in Section 20.5
is the statement that σ_low = σ₀ with zero slack: the low exponent equals C(σ₀).

### 2.2 Local compensation (Section 16)

C1. Proposition 16.1 (dynamic local errors). Contours x_r = a + 16e, w_r = 1 − a − 6e,
z_r = 17/50, with 51/100 ≤ a ≤ 1, 0 < e ≤ 10⁻³. For any subset I of error slots,

    L_S(w, χ•(u)) Π_{i∈I} D_i(u) ≪ U^{a − 1/2 + O(e) + ε} (3 + T₁)^C Π_{i∈I} P_i^{z_r − 1/2 + O(e) + ε}.

Exponents: U^{δ/2} (the reflected numerator, from Lemma 8.1's functional-equation bound
U^{a−1/2+12e}) and P_i^{z_r − 1/2} per slot, with no positive amplitude for error slots.
Range use: the four local exponents −x_r + 2ϑ, −6z_r + 2ϑ, 4 − 5x_r − 6z_r + 2ϑ, 1 − w_r − 6z_r + ϑ
must be ≤ −51/100; at a = 51/100 the third is 49/25 − 5a − 68e = −59/100 − 68e, which is
where a ≥ 51/100 and z_r = 17/50 are used (z_r ≥ 49/150 would be the floor for the third exponent
at a = 51/100). The hypothesis |L(1 − w, ψ*_u)| ≪ U^ε is supplied by Lemma 8.1 on the bin.

C2. (16.13), principal multiplier B_p = −1 + O(q_p^{−7/8}) in the second Euler region. Exponent:
a subpower correction, through κ_P < (7/8) min ℓ_i, used only in the normalizer (Section 20.1).
Phase 209 (QRH_FOUR_FIFTHS_ATTEMPT Section 1) checked the enlarged box x ≥ 4/5, z ≥ 33/200,
w ≥ 19/20 gives B_p = −1 + O(Q^{−4/5}); this is not a blocking term.

C3. Lemma 16.2 / (16.15), absolute tuple bounds on the small-row lines (x_r = β* + e, w_r = 1/2,
z_r = 17/50) and the large-row lines (2, 2, z_∞): |H_{η,u,Z}| ≪ U^ε Z^{ℓ z_r}. Exponent: ℓ z_r, i.e.
the slots contribute only their trivial size there.

C4. (16.14), |H_{η,1,Z}| ≪ Z^{ℓ ℜz} on the second Euler region: the all-height majorant required by
Lemma 10.5 (hypothesis (10.17)).

### 2.3 Prime amplitudes and the two moments

P1. Lemma 19.1 (prime bound in a bin): |Q_i(u; z)| ≪ U^{ε₁} P_i^{a − 1/2 + O(e)}. Exponent: slot
amplitude g_i ≤ δ/2, hence the slot mean q ∈ [0, δ/2] in (19.1). Hypotheses: Lemma 8.2's loss
and height hypotheses; 51/100 ≤ a ≤ 1. The bound is the zero-free rectangle of the bin applied
to the logarithmic derivative; it is a theorem-type input (a zero-density/zero-free use), and its
value δ/2 is what makes q ≤ δ/2 vanish at the floor.

P2. Lemma 17.1 (marked inverse moment), statement. For an inverse polynomial M_u(Z^r; W) of
length r and prime slots of total length z over rows 0 < q_u ≪ Z^m,

    Σ_u |M_u Q_u|² ≪ Z^{m + ε}    provided   r + 2z ≤ m − c₁,   2r + 8z ≤ 3m − c₂.

Exponent: the mean square is of the size of the row count (width m), i.e. the marked inverse
spike |M_u|² ≈ U^{δr} costs nothing on average. Range: the two strict width conditions with fixed
margins c₁, c₂. Where used in the proof: they are the canonical margins of the induction,
F_init − M_init − Q_init − z₀ ≥ c₁ − 9η − τ and 4F_init − 3M_init − 6z₀ ≥ c₂ − 22η − 3τ
(Section 17.6, around (17.82)–(17.86)); the second one is the identity
4F − 3M − 6z₀ = 3m − 2r − 8z + 10G + 2P₁. In Proposition 19.2 they are met at row width m = 1 by
1 − r − 2z ≥ 2ν₀ and 3 − 2r − 8z ≥ 9/37 (from r ≥ 23/37). No mesh condition.

P3. Lemma 17.6 (sixth-power amplification), from (17.87) (Lemma 17.1 with m = 1, no slots,
H ≥ D^{1+c}):

    Σ_u |M_u(U^r; W)|² ≪ U^{e(r) + ε},    e(r) = max{1, (1 + 5r)/6}.

Exponent: the slope α = 5/6 for r > 1 is the transfer U^{1/6} H^{5/6} through the sixth powers
u a⁶ (the same mechanism as the p⁶ transfer of the short preprint, QRH_EXPONENT_MAP). Range:
r in a bounded range, c > 0 chosen small; valid for every bin with δ > 1/50 (Remark 19.3).

P4. Lemma 18.1 (fourth moment with short prime factors), statement. For 3/4 ≤ κ ≤ 1, two plain
polynomials of lengths n₁, n₂ and prime slots of total length z over rows of width M = m + q:

    Σ_{k∈R_z} |S(n₁) S(n₂) Q|² ≪ Z^{M + ε}

in case z = 0 (no restriction on n₁, n₂) and in case z > 0 under n₁ + n₂ + 6κz ≤ M, with the
zero-free hypothesis β* ≤ (1 + κ)/2 when κ < 1, and a slot mesh z_i ≤ η(ε) uniform in κ ∈ [3/4, 1].
Exponent: the plain spike |S_m|⁴ ≈ U^{2δm} costs nothing on average for 2m + 6κz ≤ 1 (two copies
of the witness at width one), giving the plain capacity (19.2)

    z_P(m) = (1 − 2m)/(6κ).

Where the range κ ≥ 3/4 is used in the proof (located): (a) Section 18.2, the prime estimate
(18.12) |Q_ω|² ≤ C Z^{κz+ε₁}, obtained by shifting the von Mangoldt contour to ℜs = s_κ + e with
s_κ = (1 + κ)/2, which needs the zero-free hypothesis β* ≤ s_κ (this is where κ = 2β* − 1 comes
from); (b) (18.13) z ≤ M/(6κ) ≤ 2M/9 and κz ≤ M/6 for the terminal widths; (c) the comparison
"6κ − 1 ≥ 7/2, hence z < M/21 < M/20" after (18.14) for A > 5M/6; (d) "0 ≤ 6κ − 1 ≤ 5" in
Section 18.8 and the uniform mesh choices (18.52). At κ = 3/5 item (c) fails (z < 5M/78, not
< M/20), so a literal κ = 3/5 use would be an extension of Lemma 18.1. Phase 209
(QRH_HIGH_CANDIDATE_AUDIT, Section 2) already notes that with the 7/8 result as CITED input one
may take κ = max{3/4, 2β* − 1} = 3/4 for every β* ≤ 7/8, which satisfies both the range and
β* ≤ (1 + κ)/2 = 7/8; checked here, and the consequence is that the (19.6) excess Δ/4 becomes
zero since z_P is then the baseline 2(1 − 2m)/9. The κ range is therefore not an obstacle at 4/5.

### 2.4 Row counts

R1. Proposition 8.3 (two saturated witnesses). For t ∈ [1, 3/2]: lengths r ≤ t, r + m ≥ t,
t − 1/2 ≤ r, 0 ≤ m ≤ 1/2, with |M_r|² ≫ U^{δr − ε}, |S_m|² ≫ U^{δm − ε}. Exponent: the spikes
δr, δm. Range: a > 51/100 (an actual zero in the bin), Lemma 8.2's hypotheses, e < e₀,
(1 + T₁)^{A_A} ≤ U^{ε/10}. Where used: the saturated inverse witness r ≈ t up to 3/2 is what
permits the no-slot count L(t); the plain witness m ≤ 1/2 bounds the plain gain by δ.

R2. Proposition 19.2 (row counts). For a bin with 0 < δ ≤ α = 5/6 and amplitude mean q = xδ,

    #B ≪ U^{max{R_short(t), L(t)} + Δ/4 + ε} (1 + T₁)^{A_A},
    R_short(t) = 1 − δ + (δP_x/D_x)(3/2 − t),    L(t) = 1 − δ + (α − δ)(t − 1),
    D_x = 3 − 17x/9,    P_x = (2 − 8x/9)(1 − x);

without selected primes, t = 1 gives 1 − 2δ/3; at δ = α, R = 1 − δ (19.3); at the floor R = 1.
Hypotheses: total available prime length ℓ/d > 7/37 by a fixed margin (the inverse capacity is at
most (1 − 23/37)/2 = 7/37, from r*(1) ≥ 23/37); the two strict conditions of Lemma 17.1 at width
one; the zero-free condition of Lemma 18.1 via κ = 2β* − 1. The branches, with their derivation:

    inverse witness with slots:  1 − δr − 2qz,  z ≤ z_M(r) = (1 − r)/2   (Lemma 17.1);
    plain witness with slots:    1 − 2δm − 2qz,  z ≤ z_P(m) = (1 − 2m)/(6κ)   (Lemma 18.1);
    no slots, r ≥ 1:             1 − α + (α − δ)r   (Lemma 17.6);
    no slots, m ≥ 1/2:           1 − 2δm ≤ 1 − δ    (Lemma 18.1, z = 0).

Every branch is ≥ 1 − δ: in the first, r + 2z ≤ 1 and 2q ≤ δ give 1 − δr − 2qz ≥ 1 − δ(r + z) ≥
1 − δ; in the second, 2m + 6κz ≤ 1 with 6κ ≥ 9/2 > 2 gives 2δm + 2qz ≤ δ(2m + z) ≤ δ; the third
and fourth are ≥ 1 − δ since α ≥ δ and m ≤ 1/2 respectively. Hence

    (R*)  R ≥ 1 − δ = 2(1 − a) in every branch of Proposition 19.2,

with equality only at δ = α (no slots, t = 3/2), at zero plain capacity (m = 1/2), or in the limit
of full selection. This is the density-hypothesis strength for the count of rows carrying a zero
of real part ≥ a at conductor U. The term Δ/4 is the (19.6) cost of using the dynamic capacity
instead of the baseline; it vanishes if κ = 3/4 is used.

### 2.5 The high exponent

H1. Lemma 10.4 / (10.15) with σ₀ = 7/8, z₀ = 17/50, g = qℓ, and the hypothesis (10.13)

    Σ_{u∈C} L_S(w, χ•(u)) H^{(I)}_{η,u,Z} ≪ U^{R + δ/2 + ε_c} Z^{ℓ(z₀ − 1/2) + qℓ + ε_c} (1 + T₁)^{A_η},

which Lemma 20.1 verifies from C1 (error slots), P1 (main slots, |Q_i| ≤ P_i^{g_i + ϑ}) and R2
(cardinality U^{R}). The exponent relative to C(σ₀):

    E_{σ₀}(d; R, q) = a − σ₀ + h(z₀ − 1/6) − a l_y − ℓ/2 + qℓ + d(R + δ/2 − z₀).      (10.15)

Term by term: a − σ₀ (the central contour ℜs = a + 16e against the reference scale), h(z₀ − 1/6)
(the ℜz contour z₀ against the pole at z = 1/6 of ζ^S_F(6z), scale Z^{h}), −a l_y (ℜw = 1 − a on
the Y-polynomial), −ℓ/2 + qℓ (central slot scale P_i^{−1/2} and amplitude), d(R + δ/2 − z₀) (row
count, reflected numerator, and q_u^{−z₀}). The 7/8-specific first line of (20.4) is exactly this
with the published geometry; substituting a = (1 + δ)/2, h = 13/16, ℓ = 1/6, l_y = 23/48:

    E(d) = −1/48 + 2δ/3 + q/6 − h(1 − R) + (d − h)(R + δ/2 − 17/50),    C₀ = −1/48.

Verified symbolically (the two lines agree identically; C₀ = E(h) at δ = q = 0, R = 1). Ranges of
Lemma 20.1: 0 < d_min ≤ d ≤ d_max, e < 10⁻³, T₁ = Z^τ with τ ≤ d_min/100, the cumulative height
allocation (10.14), q ∈ [0, δ/2].

H2. The coefficient of z₀ in E(d) is h − d: at d = h the contour choice z₀ = 17/50 does not enter
the endpoint exponent at all. It enters only the slope R + δ/2 − z₀ (positive, ≥ 4/25 in Section
20.5), which is what lets d = h bound all d ≤ h; and it enters (20.6) with the opposite sign for
the small rows.

H3. Small rows (Section 20.3, Lemma 10.6, C3): exponent h(z₀ − 1/6) − l_y/2 = −79/800, row
exponent 63/50 < 2, d_min = 1/100: saving m_small = 63/800. Large rows: B₀ = l_x/2 + 1 + l_y =
53/32 and the free parameter z_∞; no exponent constraint. Verified.

H4. Principal normalizer (Section 20.1, Lemma 13.1): A_T(Z) ≍ (log Z)^{−K}, subpower; margins
m_w = l_y/20 = 23/960, m_z = h/600 = 13/9600, m_P = κ_P = 7ℓ/(16K). Verified. These are
positive for any geometry and never bind.

## 3. The general endpoint exponent and its derivation

Put d = h in (10.15) and use (G1)–(G3) with a = (1 + δ)/2:

    E(h) = a − σ₀ − a l_y − ℓ/2 + qℓ + h(R + δ/2 − 1/6)
         = C_geom + (1/2 + ℓ)δ + ℓq − h(1 − R),      C_geom = l_x/2 − σ₀ + 5h/6 = 2/3 + b/6 + ℓ − σ₀.

Check of the constant: (1 − l_y)/2 − ℓ/2 + 5h/6 − σ₀ with (1 − l_y)/2 = (l_x + ℓ)/2 gives
l_x/2 + 5h/6 − σ₀; then l_x/2 + 5h/6 = (1 − b − ℓ)/4 + 5(1 + 3ℓ + b)/12 = 2/3 + b/6 + ℓ. Check of
the δ-coefficient: (1 − l_y)/2 + h/2 = (l_x + ℓ + 1 + ℓ − l_x)/2 = 1/2 + ℓ. At the published
geometry C_geom = 17/96 − 84/96 + 65/96 = −2/96 = −1/48 and 1/2 + ℓ = 2/3, as in (20.4). This is
the formula of phase 209 (QRH_HIGH_CANDIDATE_AUDIT, Section 3), confirmed.

Two specializations used by the manuscript:

  (i) Floor bin (20.5): δ₀ = 1/50, R = 1, q ≤ δ₀/2:
      E(h) ≤ C_geom + (1/2 + 3ℓ/2)δ₀ = −1/48 + (3/4)(1/50) = −7/1200.   Verified.

  (ii) Endpoint δ = α = 5/6 (20.7): R = 1 − δ (no slots, t = 3/2), q ≤ δ/2:
      E(h) ≤ C_geom + δ(1/2 + 3ℓ/2 − h) = −1/48 − δ/16.   Verified; in general
      1/2 + 3ℓ/2 − h = l_x + ℓ/2 − 1/2 = −b/2, so with the ideal count R = 1 − δ the
      δ-dependence of the certificate is exactly −bδ/2 for any geometry.

## 4. Lemma 20.2 rederived

For 1/50 < δ < α, x = q/δ ∈ [0, 1/2], J = (α − δ)D_x + δP_x, t = 1 + δP_x/(2J), R* = L(t) =
R_short(t) = 1 − δ + (α − δ)δP_x/(2J). Inserting R = R*, q = xδ into E(h) with the published
geometry, and y = 1/2 − x, p_y = 7 + 18y + 8y², j_y = 185 + 170y + (−138 + 12y + 96y²)δ,
v = 51 + 41y:

    D_x = (37 + 34y)/18,  P_x = p_y/9,  J = j_y/108   (verified);
    −E* = [1 + (3 + 8y)δ]/48 − (13/32)(5/6 − δ)δP_x/J   (verified);
    10368 J(−E*) = 10(37 + 34y) − 8(237 + 377y + 26y²)δ + 48(51 + 131y + 94y² + 32y³)δ²  (verified);
    10368 v J(−E*) = (3 + 5y)[(4vδ − 79)² + 49] + 4y{4vδ[(1 + 3y)(15 + 32y)δ + 9 − 13y] + 265 + 3485y}
                                                                                            (20.9) verified.

Every term on the right is ≥ 0 for y, δ ≥ 0 (9 − 13y ≥ 5/2), the first line is ≥ 49(3 + 5y), and
v ≤ 17(3 + 5y); with J ≤ 5/2 this gives −E* ≥ 49/(10368·17·5/2) = 49/440640 (and 10368·17 =
176256 as displayed). The bound is not sharp: on y = 0 the right side is minimal at δ = 79/204,
where −E* = 7/30672 ≈ 2.28·10⁻⁴, and a grid over the range gives the same minimum; so the true
margin of the certificate is about 2.3·10⁻⁴ (numerical check of a verified closed form).
The bounds 37/18 ≤ D_x ≤ 3, 7/9 ≤ P_x ≤ 2, 35/54 ≤ J ≤ 5/2 and D_x − P_x = 1 + x − 8x²/9 > 0 are
verified. (20.10): E_actual(h) − Δ ≤ −49/440640 − (1 − h/4)Δ + ε_total = −49/440640 − 51Δ/64 +
ε_total, with h/4 = 13/64 the cost of R ≤ R* + Δ/4. (20.11): with d = 1/2, R = 76/75 − 2δ/3,
q = δ/2, E(1/2) = −529/2400 + 25δ/96 ≤ −49/14400 at δ = 5/6; verified. All of these are
PROVED as arithmetic on CITED inputs.

The structure of the certificate is therefore: a negative constant C₀ = −1/48, the floor cost
(3/4)δ₀ at the floor bin, the endpoint slope −δ/16, and between them the adaptive count R*
whose only role is to keep −h(1 − R*) + (2/3)δ + δx/6 below 1/48 for 1/50 < δ < 5/6; this is the
content of Lemma 20.2, and it is comfortable (margin ≈ 2.3·10⁻⁴ before Δ).

## 5. What stops the certificate at 7/8

The certificate at a reference exponent σ₀ consists of the three scalar requirements

    (LOW)   l_x/2 + b/12 + (5ℓ − 1)₊/8 ≤ C(σ₀)      ⟺  σ₀ ≥ 11/12 − ℓ/4 + (5ℓ − 1)₊/8,
    (FLOOR) C_geom + (1/2 + 3ℓ/2)δ₀ ≤ 0            ⟺  σ₀ ≥ 2/3 + b/6 + ℓ + (1/2 + 3ℓ/2)δ₀,
    (ADAPT) C_geom + (1/2 + ℓ)δ + ℓq − h(1 − R) < 0 for δ₀ < δ ≤ κ, R from Proposition 19.2,

plus the side conditions ℓ/h > 7/37 (supply), ℓ ≤ 1/3 − 8b/9 and b > 0 (L2), and the
height/mesh/loss orders which cost only arbitrarily small powers. By (R*), the strongest row
count this detector and these moments can ever deliver is R = 1 − δ, for which (ADAPT) reads
C_geom − bδ/2 < 0; so (ADAPT) can never be satisfied where (FLOOR) fails, and no improvement of
the moment estimates, of the capacities z_M, z_P, of the amplification slope α, or of the Δ/4
loss can change the constant C_geom. The moments decide only whether the slope in δ is
achieved; they are not what stops the method.

The binding pair is (LOW) and (FLOOR). With δ₀ → 0 and b → 0 they read σ₀ ≥ 11/12 − ℓ/4 (for
ℓ ≤ 1/5) and σ₀ ≥ 2/3 + ℓ; the first decreases and the second increases in ℓ, they cross at ℓ = 1/5,
and the common value is 13/15. For ℓ > 1/5 both increase. This is phase 209's 13/15 (template
minimum, QRH_FOUR_FIFTHS_ATTEMPT Section 4, and the relaxed joint infimum of QRH_HIGH_CANDIDATE_
AUDIT Section 4, 167/192 with δ₀ = 1/50 and 13/15 with δ₀ → 0), re-obtained here from the
general E(h) rather than from the floor formula alone; the new point is that (R*) makes the same
13/15 the infimum over all row counts available to Proposition 19.2, not only over the floor.

At σ₀ = 4/5 the deficits are:

    published geometry (ℓ = 1/6, b = 1/8):  LOW deficit 3/16 − 9/80 = 3/40;
                                            C_geom = 13/240;  FLOOR value 13/240 + 3/200 = 83/1200;
    ℓ = 1/5, b = 1/10 (phase 209 candidate): LOW deficit 11/60 − 7/60 = 1/15;
                                            C_geom = 1/12;  FLOOR value 1/12 + 2/125 = 149/1500
                                            (phase 209's 49/1500 at σ₀ = 13/15: checked, 1/60 + 2/125).

The 7/8 geometry is exactly the point where (LOW) holds with equality at ℓ = 1/6 (σ_low = 7/8)
and (FLOOR) holds with the slack 7/1200 (C_geom = −1/48 against the floor cost 3/200): the
manuscript spent its whole high-side room on the floor bin and its whole low-side room on the
completed-row norm.

## 6. What would have to change for C_II(4/5)

Separated by type.

Pure parameter choices (existing lemmas, within their stated ranges):
  - The floor δ₀ = 1/50 (grid of Lemma 8.1, Proposition 16.1 needs a ≥ 51/100 only through the
    local exponent 4 − 5x_r − 6z_r ≤ −51/100, which holds for a ≥ 1/2 with z_r = 17/50). Lowering
    δ₀ removes (1/2 + 3ℓ/2)δ₀ from (FLOOR): at most 3/200 (published) or 2/125 (candidate).
  - z₀ = 17/50: absent from E(h); irrelevant to the endpoint.
  - κ: taking κ = 3/4 with β* ≤ 7/8 as CITED input removes the Δ/4 (= hΔ/4 in (20.10)) cost and
    keeps Lemma 18.1 inside its range; it does not touch C_geom.
  - b: smaller b lowers both (LOW) by b/12 and (FLOOR) by b/6 but b > 0 is required by L2.
  - ℓ, l_x, l_y, h: tied by (G1)–(G3); the trade-off is the 13/15 crossing.
  None of these reaches 4/5; the parameter infimum is 13/15 (phase 209, confirmed).

Ranges of existing lemmas (extension needed, not a new theorem):
  - Lemma 18.1 below κ = 3/4: needed only if the dynamic κ = 2β* − 1 is kept at σ₀ = 4/5; avoidable
    as above. Locations where the range is used: Section 2.3, item P4 (a)–(d).
  - Lemma 15.1 for ℓ ≠ 1/6: the loss (5ℓ − 1 + d)/4 of the second branch; for ℓ ≤ 1/5 it is clipped
    and the lemma's form transports (phase 209, QRH_LOW_CANDIDATE_VALIDATION, conditional on
    Lemma 14.3). Lemma 20.1 and Proposition 19.2 for ℓ/h > 7/37: satisfied by the candidate (4/17).

Terms whose exponent is a theorem (changing them needs a new estimate):
  - (T1) The low exponent l_x/2 + b/12 of Proposition 15.3: it is Cauchy–Schwarz of the completed
    norm Z^{M′} (Lemma 15.1, reflected energy Lemma 14.3) and the additive Gram bound
    (Q/Y′)P_a^{1/6} (Proposition 15.2, quadratic large sieve). To certify 4/5 at ℓ = 1/5 this
    exponent must fall by s_low ≥ 1/15 (by 3/40 at ℓ = 1/6).
  - (T2) The high constant C_geom = 2/3 + b/6 + ℓ − σ₀: it is the trivial row count R = 1 on the floor
    bin times the pointwise bounds U^{δ/2} (Lemma 8.1), P_i^{−1/2} (Proposition 16.1, Lemma 19.1),
    Z^{−h/6} (the residue normalization) and Y^{−a} on the central contour, i.e. absolute values
    taken row by row at U = Z^h. To certify 4/5 at ℓ = 1/5 it must fall by s_high ≥ 1/12 (by 13/240
    at ℓ = 1/6), and (R*) shows no zero-detection count can provide this since the rows in
    question carry no zero. What would provide it is a bound for the floor-bin row sum that beats
    trivial count × pointwise bound, for instance a mean value over rows u ≍ Z^h of
    L_S(w, χ•(u))Π_i Q_i(u; z) on the central contour; nothing of this kind is in Part II.
  - (T3) The row exponent R ≥ 1 − δ (Proposition 19.2; Lemmas 17.1, 18.1, 17.6, Proposition 8.3):
    density-hypothesis strength; it bounds the δ-slope by −b/2 and is already optimal for the
    certificate's shape. Beating 1 − δ would require counting rows below the density hypothesis,
    which these width-one moments cannot do (the inverse moment at width one, r + 2z ≤ 1, caps
    the spike at U^{δ}). This is not where 4/5 is lost.
  - (T4) The slot amplitude q ≤ δ/2 (Lemma 19.1): vanishes at the floor; not binding.

A split is possible in principle: with savings s_low on (T1) and s_high on (T2), the two
constraints become ℓ ≥ 7/15 − 4s_low and ℓ ≤ 2/15 + s_high (b, δ₀ → 0), so any s_high + 4s_low ≥ 1/3
certifies 4/5 at the template level, e.g. s_low = s_high = 1/15, or s_high = 1/3 alone at ℓ = 7/15
(but then L2 requires ℓ ≤ 1/3, so the high-only route also needs L2 changed), or s_low = 1/12
alone at ℓ = 2/15 (then (LOW) needs 11/12 − 1/30 − s_low ≤ 4/5, i.e. s_low ≥ 1/12). None of these
savings exists in the manuscript or in phase 209.

## 7. What this does and does not give

Given: a complete list of the exponents entering the Part II certificate with their sources and
ranges; symbolic verification of (20.4)–(20.11) and of Lemma 20.2 (C₀ = −1/48, 49/440640, true
margin ≈ 2.3·10⁻⁴); the general endpoint exponent E(h) = 2/3 + b/6 + ℓ − σ₀ + (1/2 + ℓ)δ + ℓq −
h(1 − R); the observation (R*) that every branch of Proposition 19.2 has R ≥ 1 − δ, so the
moments and the detector control only the δ-slope (−bδ/2 at best) and never the constant; the
identification of the two load-bearing theorem-type exponents, the low exponent l_x/2 + b/12
(T1) and the high constant from the floor-bin trivial count (T2), whose trade-off in ℓ gives the
13/15 infimum of phase 209; the exact deficits at σ₀ = 4/5 (3/40 and 13/240 at the published
geometry; 1/15 and 1/12 at ℓ = 1/5); and the location of the κ ≥ 3/4 uses inside the proof of
Lemma 18.1, with the conclusion that this range is avoidable at 4/5 by κ = 3/4 under the CITED
7/8 input.

Not given: any proof at σ₀ = 4/5, or at any σ₀ < 7/8. The manuscript's lemmas are CITED, not
audited; the ledger relies on their statements. The low template's loss (5ℓ − 1 + d)/4 is an upper
bound on the method's cost, not a lower bound on the truth. The statement (R*) is a property of
Proposition 19.2's branches, not an impossibility theorem for other detectors. The single biggest
obstacle is (T2): the floor-bin rows at conductor U = Z^h, bounded by trivial count times
pointwise absolute values, which forces σ₀ ≥ 2/3 + ℓ + b/6 while the low side forces
σ₀ ≥ 11/12 − ℓ/4; everything else in Part II (moments, capacities, κ, z₀, δ₀, Δ/4) is either
already optimal for the certificate or costs only arbitrarily small powers. Status of 4/5: OPEN;
it requires a new estimate of type (T1) or (T2) with total saving s_high + 4s_low ≥ 1/3.
