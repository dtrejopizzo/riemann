# Requirement theorem for the Part II architecture: what 4/5 needs

**Result.** The certificate of Part II of the 7/8 manuscript is written out as a system of
scalar inequalities in the free quantities (ℓ, b, δ₀, z₀, κ, the row exponent R(δ, x), the slot mean
q = xδ), with the exponents of Lemma 15.1, Proposition 15.2, Proposition 16.1 and Lemma 20.1
as structural inputs. Two things are established. (a) With every published estimate unchanged,
the infimum σ_inf of the certifiable reference exponent satisfies

    365233/417462 = 0.87489… ≤ σ_inf ≤ 7/8,

the lower bound PROVED by exact arithmetic on the CITED inputs; numerically σ_inf = 0.87496
at ℓ = 0.1668, b = 0.1235, so the published geometry (1/6, 1/8) is within 4.3·10⁻⁵ of the optimum
of its own architecture. The figure 13/15 of the phase 209 notes and of LEDGER_001 is not the
infimum of the architecture: it is the infimum when the row counts of Proposition 19.2 are
replaced by the ideal count R = 1 − δ. The binding high constraint is not the floor bin but the
adaptive range δ ≈ 0.39 with full slot amplitude x = 1/2, where the actual count R* exceeds
1 − δ; the manuscript's own margin there is 2.3·10⁻⁴. The κ-extension of Lemma 18.1
(MOMENTS_001) changes σ_inf by less than 1.5·10⁻⁴ and buys nothing by itself. (b) At σ₀ = 4/5 the
deficits at the near-optimal geometry are 3/40 on the low side and 3/40 on the high side; the
admissible trades are tabulated, and the targets are three: a bilinear low bound beyond
Cauchy–Schwarz (T1), a signed row-sum bound on zero-selected bins at conductor Z^h beating
absolute values (T2), and, as a bounded auxiliary, counts reaching the density-hypothesis
exponent 1 − δ (T3). Each is stated as an explicit inequality with the required saving. (c) T1 and
T2 are both signed mean values whose unsigned versions are sharp; they are of a different type
from MS(18/25) of RECURSIVE_TRANSFER_001 and neither pair of routes implies the other. No
4/5 statement is made. Labels: the certificate system and the exact lower bound are PROVED
(arithmetic on CITED inputs); the numerical optimum and the frontier table are NUMÉRICO
(evaluations of closed forms); the typing of the targets is ARGUED; 4/5 is OPEN.

## 1. Index and corpus check

Index entry L74 and the phase 209 section (QRH_FOUR_FIFTHS_ATTEMPT, QRH_HIGH_CANDIDATE_AUDIT,
QRH_LOW_CANDIDATE_VALIDATION) contain the low template σ_low(ℓ) = 11/12 − ℓ/4 + (5ℓ − 1)₊/8,
the floor formula E(h) ≤ C_geom + (1/2 + 3ℓ/2)δ₀ and the joint infimum 167/192 (δ₀ = 1/50) or
13/15 (δ₀ → 0). LEDGER_001 rederived (20.4)–(20.11), proved (R*) (every branch of
Proposition 19.2 has R ≥ 1 − δ) and identified the low exponent (T1) and the floor constant (T2)
as the theorem-type inputs. MOMENTS_001 extended Lemma 18.1 to κ > 1/2 and gave the modified
constants D_x = 3 − 19x/9, P_x = (2 − 10x/9)(1 − x) at the 4/5 baseline. RECURSIVE_TRANSFER_001
reduced 4/5 in the short preprint's architecture to MS(18/25). None of these optimised the
adaptive certificate (Lemma 20.2) over the geometry; that is what is done here. Nothing below
reopens a route closed in the index.

## 2. The certificate as a system of inequalities

All statement numbers refer to the 7/8 manuscript; the quantities are those of LEDGER_001,
Section 1: ℓ, b > 0 free, l_x = (1 − b − ℓ)/2, l_y = (1 + b − ℓ)/2, h = (1 + 3ℓ + b)/2 by (G1)–(G3),
C(σ₀) = σ₀ − 1 + l_x/2 + h/6, δ = 2a − 1 the bin variable, δ₀ the floor, x = q/δ ∈ [0, 1/2],
α = 5/6, z₀ = 17/50, κ the parameter of Lemma 18.1 and c = 1/(3κ₀) the plain-capacity
constant (c = 4/9 published; c = 1/(3(2σ₀ − 1)) with the extension of MOMENTS_001). The
contradiction hypothesis at a reference exponent σ₀ < 7/8 is β* ∈ (σ₀, 7/8] (the 7/8 result
CITED as input), so the bins have δ ≤ κ_max = 3/4; with only the 11/12 input, κ_max = 5/6.

The endpoint exponent of a bin, from (10.15) at d = h (LEDGER_001, Section 3):

    E(h; δ, x, R) = C_geom + (1/2 + ℓ + ℓx)δ − h(1 − R),      C_geom = 2/3 + b/6 + ℓ − σ₀.   (2.1)

The count delivered by Proposition 19.2 for 0 < δ ≤ α, minimised over t ∈ [1, 3/2] (the balancing
point (20.8); LEDGER_001 Section 4), is

    R*(δ, x) = 1 − δ + (α − δ)δP_x/(2J),   J = (α − δ)D_x + δP_x,
    D_x = 3 − (1 + 2c)x,   P_x = (2 − 2cx)(1 − x),                                          (2.2)

plus a cost Δ/4 (Δ/3 with the extension) which is absorbed in the comparison with C(β*) since
h/4 < 1 (20.10); at the floor δ₀ no witness exists and R = 1. Writing

    G(δ, x) = C_geom + δ·K(δ, x),   K(δ, x) = (1/2 + ℓ + ℓx) − h·[1 − (α − δ)P_x/(2J)],       (2.3)

the certificate at σ₀ consists of

    (LOW)    11/12 − ℓ/4 + (5ℓ − 1)₊/8 ≤ σ₀                       [Lemma 15.1, Prop. 15.2, Prop. 15.3];
    (FLOOR)  C_geom + (1/2 + 3ℓ/2)δ₀ < 0                          [(20.5): R = 1, q ≤ δ₀/2];
    (ADAPT)  G(δ, x) < 0  for all δ₀ < δ ≤ κ_max, 0 ≤ x ≤ 1/2        [(20.8)–(20.10)];
    (INT)    E(d) < 0 for d_min ≤ d < h with the count used there    [(20.11)];
    (SIDE)   ℓ/h > 7/37 (supply; 13/70 with the extension), ℓ ≤ 1/3 − 8b/9 (absorption in
             Prop. 15.3), (13/75)h − l_y/2 < 0 (small rows, (20.6)), b > 0, δ₀ > 0.

Three remarks, each PROVED by the displayed algebra.

(i) (LOW) does not depend on b: the b/12 of the low exponent l_x/2 + b/12 is cancelled by the
b/12 inside h/6 in C(σ₀). LEDGER_001, Section 6, says that smaller b lowers (LOW); it does not.

(ii) (INT) is implied by (ADAPT) if the adaptive count is used on every d ∈ [d_min, h]: by
(10.15), E(d) = E(h) + (d − h)(R + δ/2 − z₀) and R* + δ/2 − z₀ ≥ 1 − δ/2 − 17/50 > 0. The
manuscript uses no slots for d ≤ 1/2 and the count 76/75 − 2δ/3; at σ₀ = 4/5 that choice fails
for δ > 0.506 (Section 5), so the adaptive count must be used down to d_min. This needs
supply ℓ/d ≥ ℓ/h (true for d ≤ h) and a mesh ℓ_i/d ≤ η_mesh, i.e. K ≥ 2ℓ/(d_min η_mesh): a
parameter choice.

(iii) At δ → 0, G → C_geom, and ∂G/∂δ at δ = 0 equals K(0, x) = 1/2 + ℓ + ℓx − h(1 − P_x/(2D_x)),
which at x = 0 is 1/6 − b/3 > 0 and at x = 1/2 is 7/74 + 21ℓ/74 − 15b/37 (published: 0.091).
So G rises above its floor value before the term (α − δ)P_x/(2J) decays, and (ADAPT) is not
implied by (FLOOR). This is the point missed by the phase 209 notes and by LEDGER_001,
Section 5: the sentence "(ADAPT) can never be satisfied where (FLOOR) fails" is true, but its
converse, implicitly used to call 13/15 the infimum, is false. In the published certificate the
maximum of G is at δ = 79/204 = 0.387, x = 1/2, with G = −2.28·10⁻⁴ (LEDGER_001, Section 4),
whereas the floor value is −7/1200 = −5.8·10⁻³: the adaptive range, not the floor, is binding.

## 3. Theorem A: the infimum with the existing estimates

Define Ψ(ℓ, b; c, κ_max) = max over δ ∈ [0, κ_max], x ∈ [0, 1/2] of δ·K(δ, x). Then (FLOOR) and
(ADAPT) together read σ₀ > 2/3 + b/6 + ℓ + max{Ψ, (1/2 + 3ℓ/2)δ₀} =: σ_high(ℓ, b), and the
certificate at σ₀ exists in the template if and only if σ₀ ≥ max{σ_low(ℓ), σ_high(ℓ, b)} with
strict inequality in the second and (SIDE).

**Theorem A.** (1) With R = R* (Proposition 19.2 as published, c = 4/9, any κ_max ≤ 5/6, any
δ₀ ≤ 1/50), for every admissible (ℓ, b),

    max{σ_low(ℓ), σ_high(ℓ, b)} ≥ 365233/417462 = 0.874889…,

and the published geometry gives 7/8. Hence 0.87489 ≤ σ_inf ≤ 0.875. (2) With the ideal count
R = 1 − δ for every δ > δ₀ (the (R*) ceiling of LEDGER_001), σ_inf = 13/15, attained in the limit
ℓ → 1/5, b → 0, δ₀ → 0. (3) With the κ-extension of Lemma 18.1 and nothing else (c = 1/(3(2σ₀ − 1)),
Δ/3 in place of Δ/4), the lower bound of (1) becomes 3304/3777 = 0.874768… (using the most
favourable c = 5/9, which is only legitimate at σ₀ = 4/5); self-consistently, c = 1/(3(2σ₀ − 1))
with σ₀ ≈ 0.875 is 0.4445, and σ_inf is unchanged to five decimals.

*Proof of (1).* Lower bound. For any (δ₁, x₁) in the range, Ψ ≥ δ₁K(δ₁, x₁), so σ_high(ℓ, b) ≥
2/3 + b/6 + ℓ + δ₁K(δ₁, x₁). Take δ₁ = 2/5, x₁ = 1/2, c = 4/9: D = 37/18, P = 7/9,
J = (13/30)(37/18) + (2/5)(7/9) = 649/540, (α − δ₁)P/(2J) = 91/649, so

    K(2/5, 1/2) = 1/2 + 3ℓ/2 − (558/649)h = 1/2 + 3ℓ/2 − (279/649)(1 + 3ℓ + b),
    σ_high ≥ 6763/9735 + (3518/3245)ℓ − (103/19470)b.                                       (3.1)

The coefficient of b is negative, and (SIDE) gives b ≤ 3(1 − 3ℓ)/8, hence
σ_high ≥ 6763/9735 − 309/155760 + ℓ(3518/3245 + 927/155760) =: A + Bℓ with B > 0. For ℓ ≤ 1/5,
σ_low(ℓ) = 11/12 − ℓ/4 is decreasing and A + Bℓ is increasing; they cross at

    ℓ_c = 11627/69577 = 0.16711,     σ_low(ℓ_c) = 365233/417462 = 0.874889,

so max{σ_low, σ_high} ≥ 365233/417462 for all ℓ ≤ 1/5; for ℓ ≥ 1/5, σ_low ≥ 13/15 > 0.8749.
Upper bound: Lemma 20.2 and Proposition 20.3 (CITED) at (ℓ, b) = (1/6, 1/8), σ₀ = 7/8. ∎

*Proof of (2).* With R = 1 − δ, K = 1/2 + ℓ + ℓx − h = −(ℓ + b − 2ℓx)/2 ≤ −b/2 < 0, so Ψ ≤ 0 and
σ_high = 2/3 + b/6 + ℓ + (1/2 + 3ℓ/2)δ₀; the crossing with σ_low at b, δ₀ → 0 is ℓ = 1/5, value
13/15 (QRH_FOUR_FIFTHS_ATTEMPT Section 4; LEDGER_001 Section 5). ∎

*Proof of (3).* Repeat (3.1) with c = 5/9: D = 3 − 19/18 = 35/18, P = (2 − 5/9)/2 = 13/18,
J = (13/30)(35/18) + (2/5)(13/18) = 611/540, (α − δ₁)P/(2J) = 169/1222; the crossing is at
ℓ = 0.16759 with value 3304/3777. Since the extension enlarges the plain capacity by the factor
κ_pub/κ (from 3/4 to 2σ₀ − 1), c > 4/9 only for σ₀ < 7/8; at the infimum the two values of c are
within 10⁻³ and the crossing moves by less than 10⁻⁵. ∎

Numerical complement (NUMÉRICO, evaluation of (2.1)–(2.3) on a grid in δ, x and a bracketing
of the crossing in ℓ with b optimised): with c = 4/9,

    ℓ* = 0.16684,  b* = 0.1235,  σ_inf = 0.874957,  maximiser δ* = 0.388, x* = 1/2, Ψ = 0.02087;

with c = 5/9 (the capacity of the extension at the 4/5 baseline, not legitimate at this σ₀),
σ_inf = 0.874840 at ℓ* = 0.16731; with the self-consistent c = 0.4446, σ_inf = 0.874957. The
κ_max and δ₀ choices do not affect the optimum, because the
maximiser is interior (δ* ≈ 0.39) and the floor value (1/2 + 3ℓ/2)δ₀ = 0.016 is below Ψ. The
worst amplitude is x = 1/2 for δ ≥ 0.25 and x = 0 for small δ.

Consequences. (a) The 7/8 of the manuscript is the infimum of its own architecture to within
4.3·10⁻⁵: no parameter choice in (ℓ, b, δ₀, z₀, κ, slot system) improves it. (b) The moments and
the detector are not inert: the gap Ψ ≈ 0.021–0.028 between R* and 1 − δ is the whole
difference between 7/8 and 13/15 at the template level. (c) The κ-extension alone is worth
< 1.5·10⁻⁴; the conservative choice κ = 3/4 of QRH_HIGH_CANDIDATE_AUDIT loses nothing
measurable.

## 4. Theorem B: requirements at σ₀ = 4/5

Let s_low ≥ 0 be a saving in the low exponent (Proposition 15.3 improved to Z^{l_x/2 + b/12 − s_low + ε},
with the loss (5ℓ − 1)₊/8 kept) and let s(δ, x) ≥ 0 be a saving, in base Z, in the row-sum bound
of Lemma 20.1 for the bin (δ, x) at U = Z^h. The certificate at 4/5 exists in the template if and
only if there is an admissible (ℓ, b) with

    s_low ≥ σ_low(ℓ) − 4/5 = 7/60 − ℓ/4 + (5ℓ − 1)₊/8,                                        (4.1)
    s(δ, x) > G(δ, x) = (ℓ − 2/15 + b/6) + δK(δ, x)   for all δ₀ ≤ δ ≤ 3/4, 0 ≤ x ≤ 1/2,        (4.2)

with G(δ₀, x) replaced by its floor form ℓ − 2/15 + b/6 + (1/2 + 3ℓ/2)δ₀ at the floor, plus (SIDE)
and (INT) handled as in Section 2 (ii). Write s_high = max_{δ,x} G(δ, x) = σ_high(ℓ, b) − 4/5 for a
saving uniform in the bin.

**Theorem B.** (1) (Frontier, NUMÉRICO on PROVED closed forms.) With the counts R* (c = 4/9,
or c = 5/9 with the extension), the minimal pairs (s_low, s_high) are, with b optimised:

    ℓ        s_low     s_high (c = 4/9)   s_high (c = 5/9)   b_opt   supply ℓ/h
    0.095    0.0929    0                  0                  0.05    0.14  (< 7/37: counts recomputed with capped capacity, Section 4.3)
    0.120    0.0867    0.0243             0.0238             0.097   0.16
    2/15     0.0833    0.0387             0.0381             0.115   0.19
    0.150    0.0792    0.0567             0.0561             0.120   0.20
    1/6      3/40      0.0748             0.0742             0.123   0.21
    0.180    0.0717    0.0892             0.0886             0.127   0.22
    1/5      1/15      0.1109             0.1102             0.132   0.24

Along the frontier 4s_low + s_high lies between 0.37 and 0.39. (2) With the ideal count R = 1 − δ,
s_high reduces to ℓ − 2/15 + b/6 + (1/2 + 3ℓ/2)δ₀ and the frontier is 4s_low + s_high = 1/3
(LEDGER_001 Section 6), e.g. (1/15, 1/15) at ℓ = 1/5 or (1/12, 0) at ℓ = 2/15, in the limit
b, δ₀ → 0. (3) Pure-high routes (s_low = 0) need ℓ ≥ 7/15, which violates ℓ ≤ 1/3 − 8b/9 and
activates the loss (5ℓ − 1)/8 = 1/6; they require three changed estimates (Lemma 15.1's second
branch, Proposition 15.2's absorption, and s_high ≥ 1/3) and are not minimal.

### 4.1 The target inequalities, with labels

(P1) Floor δ₀. Parameter choice. Lemma 8.1's grid may start at any a₀ > 1/2 (Proposition 16.1
needs 4 − 5x_r − 6z_r ≤ −51/100 at a = a₀, true for a₀ ≥ 1/2 with z_r = 17/50). Gain: at most
(1/2 + 3ℓ/2)δ₀ = 0.016 at ℓ = 1/5, and only at the floor, which is not binding. Not needed.

(P2) Adaptive count on d_min ≤ d ≤ h. Parameter choice (K ≥ 2ℓ/(d_min η_mesh)); replaces the
no-slot count of (20.11), which fails at 4/5 for δ > 0.506 (E(1/2) = −0.148 + 0.292δ at
ℓ = 1/5, b = 1/10, z₀ = 17/50). Needed, routine.

(P3) Lemma 18.1 at κ ∈ [3/5, 1]. Extension of Lemma 18.1, routine per MOMENTS_001 (one
numerical line and three uniformity sentences). Needed only if the dynamic κ is kept; the
conservative κ = 3/4 under the CITED 7/8 input is equivalent to within 7·10⁻⁴ of s_high.

(P4) Lemma 15.1 at ℓ ≤ 1/5. Extension of Lemma 15.1 (QRH_LOW_CANDIDATE_VALIDATION,
CONDITIONAL on Lemma 14.3): the second-branch loss (5ℓ − 1 + d)/4 is clipped for ℓ ≤ 1/5 and
the lemma transports. Needed for any ℓ ≠ 1/6; routine.

(T1) Low bound beyond Cauchy–Schwarz. New theorem. For every rescaled subset J of length d
and tuple p_J, with Q = q_{b*}X′Y′ ≍ Z^{M′}, M′ = 1 − ℓ − 2d, in the exact separation (6.2):

    | Σ_{σ∈T} ∫ Ŵ₀(iv) Σ_{0<q_m≪Q} Ω(q_m/Q) ξ(m)(q_m/Q)^{−iv} A_{m,σ,v}(Y′) B^J_{m,σ}(Z) dv |
        ≪ Z^{ε} (X′)^{1/2} P_a^{1/12} Z^{−s_low},                                                (T1)

with s_low from (4.1): s_low ≥ 1/15 at ℓ = 1/5 (together with T2 at s_high ≈ 0.111), s_low ≥ 3/40
at ℓ = 1/6 (with s_high ≈ 3/40), s_low ≥ 0.093 at ℓ ≈ 0.095 (alone). The factor (X′)^{1/2}P_a^{1/12}
is the Cauchy–Schwarz value (15.8); the saving must be uniform in the tuple and in the subset.

(T2) Signed row sums on a bin. New theorem. For the retained rows B(δ, x) of one dynamic and
amplitude bin at q_u ≍ U = Z^h, on the central contours ℜs = a + 16e, ℜw = 1 − a − 6e,
ℜz = 17/50, and for every error subset I,

    | Σ_{u∈B(δ,x)} L_S(w, χ•(u)) H^{(I)}_{η,u,Z}(s, w, z) |
        ≪ U^{R(δ,x) + δ/2 + ε} Z^{ℓ(17/50 − 1/2) + xδℓ − s(δ,x)} (1 + T₁)^{A},                     (T2)

with s(δ, x) > G(δ, x) of (4.2), R(δ, x) the count actually used. At ℓ = 1/5, b = 1/10, with
R = R* (c = 5/9): G(δ₀, ·) = 0.0859 (floor, δ₀ = 1/50), G(0.2, 0.4) = 0.102, G(0.42, 1/2) = 0.1105
(maximum), G(0.6, 1/2) = 0.102, G(3/4, 1/2) = 0.073; in base U these are 0.101, 0.120, 0.130,
0.120, 0.086. With R = 1 − δ (T3 solved): G = 1/12 − (3/10 − 2x/5)δ/2, maximum 1/12 at the floor.
A single bound (T2) with s ≥ 0.111 on every bin at ℓ = 1/5 (or s ≥ 3/40 at ℓ = 1/6 with T1 at
3/40) suffices. The bound cannot be replaced by a full-family mean value at one contour: the
contour depends on a, so each bin is summed on its own line, and the rows of a bin are selected
by the location of zeros (Lemma 8.1).

(T3) Counts at the density-hypothesis exponent. New theorem, bounded gain. For every bin,
#B(δ, x) ≪ U^{1 − δ + ε}(1 + T₁)^{A}, i.e. R = 1 − δ for all δ ∈ (δ₀, 3/4] and all x, instead of R*.
Gain in s_high: Ψ = 0.021–0.028 (c = 4/9 or 5/9, ℓ ∈ [1/6, 1/5]). By (R*) of LEDGER_001 this is
the ceiling of Proposition 19.2's branches; reaching it on every row requires the detector of
Proposition 8.3 to deliver a saturated witness (r = 1 or m = 1/2) on every row, which the
two-witness detector does not assert. Counts below 1 − δ at δ ≈ 0.4 (a ≈ 0.7) would be below
the density hypothesis for the sextic family at conductor U; the width-one moments cannot give
them (MOMENTS_001, Section 5). T3 never suffices alone: even with R = 1 − δ, s_high ≥ 1/15 at
ℓ = 1/5 remains.

### 4.2 Minimal sets

Two-estimate route: T1 with s_low ≥ 1/15 and T2 with s ≥ 0.111 (ℓ = 1/5), or T1 and T2 both at
3/40 (ℓ = 1/6, the published geometry, where (P4) is not needed), with (P2) and either (P3) or
κ = 3/4. One-estimate route: T1 alone with s_low ≥ 0.093 at ℓ ≈ 0.095, b ≈ 0.05, where the
supply ℓ/h = 0.14 is below 7/37 and the counts were recomputed with the capacities capped at
ℓ/h (Section 4.3); (P4) is needed there. T3 reduces the T2 requirement by Ψ but never removes it.

### 4.3 Counts under a supply cap (NUMÉRICO)

For ℓ/h < 7/37 the slot selection of Proposition 19.2 is capped at z ≤ S = ℓ/h. Recomputing the
count directly from the branches (inverse 1 − δr − 2q·min{(1 − r)/2, S} for r ≤ 1; 1 − α + (α − δ)r
for r ≥ 1; plain 1 − 2δm − 2q·min{c(1 − 2m)/2, S} for m < 1/2; worst r ∈ [t − 1/2, t], best
t ∈ [1, 3/2]) reproduces R* for S ≥ 7/37 to 10⁻⁴ and raises it by at most 0.008 at S = 0.10. The
resulting s_high at ℓ = 0.09, 0.10, 0.11 is 0 (with margin 0.006), 0.005, 0.015. This is why the
one-estimate route has s_low ≥ 0.093 rather than 1/12.

## 5. Checks

(i) Published certificate: Ψ(1/6, 1/8; 4/9, 5/6) = 0.02061 at δ = 0.388, x = 1/2;
C₀ + Ψ = −2.28·10⁻⁴, the margin of Lemma 20.2 (LEDGER_001, Section 4). (ii) (20.11) at the
published values with R = 76/75 − 2δ/3: E(1/2) = −529/2400 + 25δ/96, −3.4·10⁻³ at δ = 5/6,
reproduced. (iii) At ℓ = 1/5, b = 1/10, σ₀ = 4/5 and the no-slot count 1 − 2δ/3:
E(h) = 1/12 + 0.2333δ > 0 for all δ and E(1/2) = −0.1477 + 0.2917δ, positive for δ > 0.506;
with R* at d = 1/2 the slope argument of Section 2 (ii) gives E(1/2) < E(h; R*). (iv) (SIDE) at
ℓ = 1/5, b = 1/10: ℓ/h = 4/17 > 7/37; ℓ = 1/5 ≤ 1/3 − 4/45; small rows (13/75)(17/20) − 9/40 =
−0.078 < 0. (v) The b-independence of (LOW): l_x/2 + b/12 ≤ σ₀ − 1 + l_x/2 + (1 + 3ℓ + b)/12
⟺ σ₀ ≥ 11/12 − ℓ/4.

## 6. The type of cancellation each new target asserts, and the comparison with MS(18/25)

T1. In (6.2) the two factors are separately sharp up to the term P_a^{1/6}: the additive Gram
bound (15.4) contains the diagonal k = 0 of size Q/Y′ (proof of Proposition 15.2), and the
completed-row norm Z^{M′} of Lemma 15.1 is the row count for row polynomials whose marked
slot sum has square-root cancellation on average (Z^{ℓ′} tuples at normalisation Z^{−ℓ′/2}),
while the completed row itself, Σ_{q_A≍Z} α(A)χ_A(m)q_c^{−1}q_n^{−5/2}, is an L(1)-type object of
size O(1), not a quantity with further cancellation (ARGUED). Removing P_a^{1/6} entirely would
save only b/12 ≤ 1/120. Hence a saving s_low ≥ 1/15 cannot come from either factor: (T1) is a
bilinear statement, cancellation between the additive Gauss-sum factor A_{m,σ,v} (an additive
character sum in the frequency m) and the multiplicative completed-row factor B^J_{m,σ} (a
sextic-character object in m), summed over Z^{M′} rows with the sign ξ(m)(q_m/Q)^{−iv}. Under
the hypothesis it is meant to contradict, the probe has true size Z^{C(β*)} ≪ Z^{−1/6−b/6}
(C at β* = 1/2), so the Cauchy–Schwarz value Z^{l_x/2 + b/12} is far from sharp; the requested
saving 1/15 is a small part of that gap. Type: signed bilinear form, mixed additive–multiplicative,
at the diagonal of both factors.

T2. At the floor every pointwise factor is already of Lindelöf quality (U^{δ₀/2} from the zero-free
rectangle of Lemma 8.1 on the reflected line; P_i^{−1/2 + ϑ} for the slots from Lemma 19.1), so
the only loss is the count U^1 of rows times absolute values. (T2) asks for cancellation in the
signed sum over u of L_S(w, χ•(u)) times the slot and local products, i.e. a first moment of
reflected L-values twisted by a short sextic polynomial of length Z^{ℓ} = U^{ℓ/h}, over a subfamily
selected by the position of zeros (the bin), beating the trivial bound by U^{s/h} ≈ U^{0.13} at
ℓ = 1/5 (U^{0.09} at ℓ = 1/6). In the adaptive range the same cancellation is asked on the rows of
the bin, against the count R*; T3 would lower the requirement by at most Ψ. Type: signed first
moment on a zero-selected subfamily; unsigned, the bound is the row count and is sharp.

Comparison with MS(18/25). MS(α) (RECURSIVE_TRANSFER_001, Section 1) asks
Σ_{N(u)≤D^α}|A_u(D)|² ≪ D^{1+α+ε}: the row-count bound (square-root cancellation per row on
average) for Möbius sums of length D over D^α < D rows; it is unsigned in u and uses the sign
of μ. T1 and T2 are signed mean values whose unsigned versions are already proved and sharp;
their savings (1/15 and 0.11 in base Z) are small powers, whereas MS(18/25) asks a full
below-the-large-sieve-diagonal bound (saving D^{7/25} against the large sieve). Neither route
implies the other: MS(18/25) ⟹ 4/5 by Theorem R, and T1 + T2 (+ P2–P4) ⟹ 4/5 by the
certificate, but a zero-free half-plane does not give MS(18/25) (GRH gives MS(α) for all α; a
half-plane does not), and MS(18/25) says nothing about the probe of Part II. In strength per
statement: MS(18/25) is one estimate, stronger than any known unconditional mean square and,
by RECURSIVE_TRANSFER_001 Section 5(c), itself a new zero-free half-plane; T1 and T2 are two
estimates, each weaker than a zero-free half-plane in isolation (they are consistent with the
truth of RH by the size count above and do not individually imply a zero-free region), but each
requires a sign-sensitive treatment for which the manuscript has no tool, and T2 must hold on
zero-selected subfamilies, where mean-value technology does not apply directly. Honest
ranking: as a single target, MS(18/25) is cleaner and its obstacle is located (the dual below the
diagonal, Proposition 2 of RECURSIVE_TRANSFER_001); as an attack, T1 is the more tractable
first step because its unsigned inputs are in hand and the requested saving is small relative to
the gap between the Cauchy–Schwarz value and the true size of the probe, but T1 alone certifies
4/5 only at ℓ ≈ 0.095 with s_low ≥ 0.093, and any ℓ ≥ 0.1 brings T2 back.

## 7. What this does and does not give

Gives: the complete certificate system (2.1)–(2.3) with (LOW), (FLOOR), (ADAPT), (INT), (SIDE);
the proof that (LOW) is b-free and that (ADAPT) is not implied by (FLOOR); Theorem A, with the
exact lower bound 365233/417462 for the infimum of the architecture with unchanged estimates
and the conclusion that the manuscript's geometry is optimal to within 4.3·10⁻⁵, so that 13/15
is the infimum only under ideal counts; the value of the κ-extension alone (< 1.5·10⁻⁴); Theorem
B, the requirement frontier at 4/5 (deficits 3/40 and 3/40 at the published geometry, 1/15 and
0.111 at ℓ = 1/5, 0.093 and 0 at ℓ ≈ 0.095), the explicit target inequalities (T1), (T2), (T3) with
their savings, the parameter items (P1)–(P4), and the typing of T1 and T2 as signed mean
values whose unsigned versions are sharp.

Does not give: any estimate at σ₀ < 7/8; a proof of (T1), (T2) or (T3); an audit of the
manuscript (all its statements are CITED); a proof that the two factors of (6.2) are sharp
beyond the displayed diagonal terms (ARGUED); or any comparison of difficulty beyond the
structural one in Section 6. The numerical optimum σ_inf = 0.874957 and the frontier table are
evaluations of the closed forms (2.1)–(2.3) and are not theorems; the exact statements are the
bounds 0.87489 ≤ σ_inf ≤ 7/8 and the frontier under ideal counts, 4s_low + s_high = 1/3. Status of
4/5: OPEN. The architecture needs, at the published geometry, a saving of 3/40 on each side,
or, at ℓ = 1/5, 1/15 on the low side and 0.111 on the high side; both are signed estimates of a
kind not present in Part II.
