# R162_103 — B3: the first chamber 0.8 < T_* < ½ log 5

Round 1, mechanism B3. Pure mathematics; no numerics were run.

**Status: NO-GO (structural) for the chamber-local mechanism, with three proved lemmas and one
proved dichotomy theorem. No chamber exclusion is proved. Row D: OPEN.**

The question was whether (a) the Sonin range-intersection lemma, (b) the finite 2,3,4 collar
equations with the Gamma/Tate matrix, and (c) the proved index information of the archimedean form
(Paper 47 thm:index, cor:Tarch, cor:H1) together force R_L F = 0 for a first-contact vector in the
chamber, i.e. exclude first contact in (0.8, ½log5). Answer: (b) and (c), and the proved part of
(a) (Sonin–Gamma coercivity, R161_014 Thm 2.1), are satisfied verbatim by a one-parameter family of
finite-modification models that do have first-contact vectors in the chamber (or a plateau of
kernel vectors across it). The index information (c) is exactly what makes these models exist. The
only ingredient that separates ζ from the models is the typed Sonin identity (a) itself. That
identity is global (open boundary passage, R161_011 §6), and the chamber does not localize it.

Notation is that of Paper 47 §1 and §sec:firstcontact: Γ_T = archimedean form (A_∞ on P_T),
Π_T(F) = Σ_{n∈N_T} w_n · 2Re⟨V_{log n}F, F⟩ (the compressed prime comb, w_n = Λ(n)/√n), so
a_T = Γ_T − Π_T on P_T. P_T^par is the parity-par part of P_T. ½log5 = 0.80472, so the chamber
C := (0.8, ½log5) has length < 0.0048.

---

## 1. What the chamber contains (proved)

**Lemma 1.1 (chamber arithmetic).** For T ∈ C: (i) N_T = {2,3,4}; (ii) N_{T'} ⊂ {2,3,4} for every
T' ≤ T; (iii) the identity Λ∗1 = log restricted to k ≤ 4, i.e. Σ_{d|k} a(d) = log k for
k = 2,3,4 with a(1) = 0, holds if and only if (a(2), a(3), a(4)) = (log2, log3, log2).

*Proof.* (i),(ii): log 4 = 1.386 < 1.6 < 2T < log 5. (iii): k=2 gives a(2) = log2, k=3 gives
a(3) = log3, k=4 gives a(2)+a(4) = log4, so a(4) = log2. The system is unitriangular. ∎

So on every window up to ½log5, the form a_T depends on the arithmetic only through three numbers.
In the chamber, "use Λ∗1 = log in the step that forces vanishing" (F3, Problem prob:annihilate
(iii)) can only mean "use the exact numerical values of w_2, w_3, w_4". Every structural identity
with shifts log 2, log 3, log 4 and arbitrary positive weights is Λ-blind.

**Lemma 1.2 (width of the finite collar).** In R161_012 (3.1), δ_T = min(log2, log5 − 2T) =
log5 − 2T < log5 − 1.6 < 0.0095 for T ∈ C. The only interior points reached by the germ
Y_3(F)(t) = Σ_{n=2,3,4} w_n F(t − log n), for t ∈ (T − δ_T, T + δ_T), lie in
[T − log4 − δ_T, T − log2 + δ_T] ⊂ (−0.60, 0.12). This set is at distance > 0.2 from both endpoints
±T.

*Proof.* The arithmetic is direct: T − log4 − δ_T > 0.8 − 1.3863 − 0.0095 > −0.60, and
T − log2 + δ_T < 0.8047 − 0.6931 + 0.0095 < 0.13, so the distances to −T and T are > 0.2 and > 0.67. ∎

**Corollary 1.3 (the germ does not reach the phase-121 boundary germ).** Even complete vanishing of
the finite germ, Y_3(F) = 0 on (T − δ_T, T + δ_T), is a set of linear relations among the values of
F on the interior set of Lemma 1.2. It implies nothing about F on (−T, −T + η) ∪ (T − η, T) for
η < 0.2. So it cannot trigger P121 Theorem 3.1 (infinitesimal gap enlargement), which needs F = 0 on
a boundary subcollar. That theorem also assumes *strict* positivity below T_*, which R162_001 does
not provide (its closing remark). The only way the germ closes is through global vanishing of the
whole port (R161_012 Prop. 1.1). So the chamber-local germ is not a closing device by itself.

## 2. The weight-deformation family (proved)

For κ ≥ 0 and a parity par ∈ {ev, odd} put

  a_T^κ := Γ_T − κ Π_T  on P_T^par,   g_par(κ, T) := inf{a_T^κ(F) : F ∈ P_T^par ∩ D_T, ‖F‖ = 1}.

κ = 1 is ζ. For κ ≠ 1 the weights are a_κ = κΛ on {2,3,4}, and they are the Λ-weights for n ≥ 5
(inactive at T < ½log5). This is a finite modification in the sense of Paper 47 thm:finmod, and by
Lemma 1.1(iii) it violates Λ∗1 = log at k = 2,3,4. The associated
ζ_κ = ζ · exp((κ−1)(2^{−s} + 3^{−s} + ½·4^{−s})) has exactly the zeros and the pole of ζ
(thm:finmod(iii)). So the critical-jet detector G_+(iγ) = −ζ′(ρ)K_F(iγ) of R161_007 sees the same
zero set in every model.

**Lemma 2.1 (regularity in (κ, T)).** For T ≤ ½log5 and each parity:
(i) κ ↦ g_par(κ, T) is concave and Lipschitz, with constant A := Σ_{n≤4} v_n;
(ii) T ↦ g_par(κ, T) is non-increasing;
(iii) T ↦ g_par(κ, T) is continuous;
(iv) g_par is jointly continuous, and each value is attained by an eigenvector of the operator of
a_T^κ on P_T^par.

*Proof.* (i) g is an infimum of affine functions of κ, hence concave. Also |Π_T(F)| ≤ A‖F‖².
(ii) Zero extension embeds P_{T'}^par into P_T^par for T' < T and preserves a^κ, because a shift
that does not act on I_{T'} contributes nothing (proof of lem:monoT; weight-agnostic).
(iii) R162_001 Steps 1–6 use the comb only through the estimate of lem:contT(ii) for a finite sum of
shifts with nonnegative bounded weights, and J commutes with the dilations U_r and with the
correction space if φ_1, φ_2 are chosen of the given parity combination (take φ_2 = Jφ_1). So the
proof applies verbatim to κΠ in each parity. Its status is inherited from R162_001, which is still
pending check.
(iv) (i) and (iii) give joint continuity. Attainment holds by compact resolvent (proof of thm:O).
The form is Γ_T plus a bounded perturbation. ∎

**Lemma 2.2 (the comb has a positive direction in each parity).** For T ∈ C and each parity there
is F ∈ P_T^par ∩ D_T with Π_T(F) > 0. Hence g_par(κ, T) → −∞ as κ → ∞.

*Proof.* Let φ ∈ C_c^∞(−ε, ε) be real, with ∫φ = ∫tφ = 0 and ε small. Put
ψ = φ(· − u) + φ(· − u − log2) with u = 0.05, and F_0 = ψ ± Jψ. The supports of ψ and Jψ are near
{0.05, 0.743} and {−0.05, −0.743}. The pairwise differences between the two sets are near 0.1, 0.793
and 1.486, which are ≥ 4ε away from log2, log3 and log4 for small ε. Within each set the only
difference is exactly log2. Hence Π_T(F_0) = 2·2w_2‖φ‖² > 0. The Tate moments of F_0 are
O(ε²‖φ‖_{L¹}) = O(ε^{5/2}‖φ‖) because the first two moments of φ vanish. The parity-preserving
correction of R162_001 Step 3 changes Π_T by O(ε^{5/2})‖φ‖², which leaves Π_T > 0 for small ε. The
second claim follows from a^κ(F) = Γ_T(F) − κΠ_T(F). (For the even sector this is also Paper 47
Lemma cpos / thm:finmod(ii).) ∎

**Lemma 2.3 (the index anchors κ = 0).** For T ∈ C: g_ev(0, T) = λ_ev(T) < 0 (thm:index(ii),
cor:Tarch). g_odd(0, T) = λ_odd(T) is > 0 if T < T*_odd and < 0 if T > T*_odd (thm:index(iii),
lem:strict). The position of T*_odd ∈ [log2, 0.81] relative to C is undecided (cor:H1).

This is the entire content of (c) in the chamber. It fixes the sign of the κ = 0 end of each concave
curve and is independent of κ.

## 3. The dichotomy theorem (proved, modulo R162_001)

For s ∈ C and each parity, let I_s^par := {κ ≥ 0 : g_par(κ, s) ≥ 0}. This set is closed, and it is
an interval because it is a superlevel set of a concave function. It is bounded by Lemma 2.2, and
decreasing in s by Lemma 2.1(ii). Because g(·, s) is continuous and I_s = ∩_{s'<s} I_{s'} (joint
continuity), its endpoints κ_−^par(s) ≤ κ_+^par(s) are non-decreasing and non-increasing in s,
respectively, and both are left-continuous.

**Theorem 3.1 (first chamber: ζ or a model).** Fix a parity. Assume 1 ∈ I_s for every s ∈ C, i.e.
no true primitive violation of that parity occurs in C. (Otherwise the true first contact of that
parity already lies in [0.8, ½log5), and there is nothing to exclude.) Let κ_e be the endpoint of
I_s that is a zero of g(·, s). For the even sector this is κ_−(s) ∈ (0, 1], since g_ev(0, s) < 0.
For the odd sector with s < T*_odd it is κ_+(s) ∈ [1, ∞). Then exactly one of the following
holds.

(A) **Genuine model first contact in C.** There are s_0 ∈ C and κ_0 = κ_e(s_0) with
g(κ_0, s_0) = 0 and g(κ_0, s) < 0 for all s > s_0 (s < ½log5). The window s_0 is also a minimal
contact from below, since g(κ_0, s) ≥ 0 for s < s_0 by monotonicity. The kernel of the κ_0-model
operator at s_0 contains a nonzero parity vector F_0.

(B) **Plateau.** κ_e is constant on C, so g(κ_e, s) = 0 for every s ∈ C. The model has kernel
vectors at every chamber window, and zero-extended kernel vectors vanish on boundary collars.

In either case κ_0 = 1 (respectively κ_e = 1) means that ζ itself has zero bottom at that window,
i.e. a true first contact (A) or a true plateau (B) in C. If κ_0 ≠ 1, the model violates
Λ∗1 = log at k = 2,3,4 (Lemma 1.1).

*Proof.* Take the even case. κ_−(s) is non-decreasing and left-continuous on C. If it is constant
on C, we are in (B): g(κ_−, s) = 0 at the left endpoint, because g(·, s) is continuous and negative
just to its left (concavity and g(0) < 0). Otherwise there is s_0 ∈ C with κ_−(s) > κ_−(s_0) for
every s > s_0 in C. Indeed, if every point had a right neighbourhood of constancy, then
left-continuity and a sup argument (the set {s : κ_−(s) = κ_−(s_1)} is closed from the left and
open to the right) would make κ_− constant. Then κ_0 := κ_−(s_0) ∉ I_s for s > s_0, i.e.
g(κ_0, s) < 0. Also g(κ_0, s_0) = 0 by the endpoint property, and attainment (Lemma 2.1(iv)) gives
F_0. The odd case with s < T*_odd is the same with κ_+ non-increasing and g(0) > 0. Continuity and
concavity put g(κ_+, s) = 0, and Lemma 2.2 guarantees κ_+ < ∞. If T*_odd < ½log5, the odd sector on
(T*_odd, ½log5) behaves like the even one. ∎

## 4. The no-go

**Theorem 4.1 (chamber-local ingredients cannot force R_L F = 0).** In case (A) with κ_0 ≠ 1, the
κ_0-model at s_0 satisfies all of the following, with w_n replaced by κ_0 w_n throughout:

1. minimality from above and below and λ = 0 (Theorem 3.1(A)), so it passes the falsifier F1 test;
2. the index facts (c) (Lemma 2.3), which do not involve w;
3. the collar identity RB_N = D_N R − E_N (Paper 47 eq:collar, with d_m → κ_0 d_m on n ≤ 4), the
   balance eq:Qbalance, eq:Qspectral and the equivalences eq:equivgate. Each proof uses only
   local finiteness, parity and the weak equation, never the values of the weights;
4. the finite germ (R161_012 (3.2)) and the inner/outer transmission (R161_013 (2.2)–(2.4), (4.2)),
   with Y_3 → Y_3^{κ_0}. The proofs use local finiteness and D_Γ = Q + C_log Q C_log, which is
   arithmetic-free;
5. Sonin–Gamma coercivity (R161_014 Thm 2.1), a statement about every g ∈ Dom(Q) ∩ Son_T^σ;
6. the invertible Gamma/Tate crossed matrix of the primitive condition, which is arithmetic-free.

Yet F_0 ≠ 0. The map R is faithful (Paper 47, after eq:Gammaenergy, weight-free), so R_L F_0 ≠ 0 for
every L that is injective on the model radical. Therefore no argument that uses only items 1–6,
plus positivity and minimality, proves R_L F = 0 in the chamber. In case (B) the same holds with
item 1 weakened to "H ≥ 0 below and at the window", which is all that R162_001 supplies for ζ.

*Proof.* Items 1–6 were checked above against their source proofs. The conclusion follows from
faithfulness. ∎

**Where it fails, precisely.** The only discriminating ingredient in the chamber is (a): the typed
scattering identity g_+ + C_log R g_− = 0 of R161_011 (0.1). It descends from
Z_+(B_+ + B_−) = D_Γ Z_+ (phase 116 (1.2)), which is the logarithmic derivative of Poisson
summation for the integer comb together with K_N = L_M S_N (Λ∗1 = log for all k). In the
κ_0-model this identity acquires the interior divisor defect
(κ_0 − 1) Σ_k (Λ(2)[2|k] + Λ(3)[3|k] + Λ(4)[4|k]) k^{−1/2} τ_{log k}. That defect is supported on
all multiples of 2 or 3, so it is not a chamber-local object. The chamber localizes (b), not (a).

- The Sonin relation is nonlocal. C_log couples the germ on (T, T + δ_T), whose length is below
  0.0095, to the port on all of [T, ∞). On [T + log2, ∞) the port carries the outer ζ-shifts
  m ≥ 2, and on [log5 − T, ∞) the prime tails n ≥ 5 (R161_012 §3).
- Hence neither (4.2) nor the upper balance (5.2) E_T^PC(F) ≤ 0 reduces to finite 2,3,4 data.
  E_T^PC = 2∫_T^∞ (t−T)|g|² is dominated by the part of the port outside the collar.

The chamber therefore does not simplify the Sonin range-intersection lemma. It inherits it
unchanged, and that lemma is still OPEN.

## 5. What a chamber exclusion would have to be

**Proposition 5.1 (the chamber statement is a finite-window positivity).** "No first-contact vector
at any T_* ∈ C", with T_* = sup{T : λ_A(T) ≥ 0} as in R162_001, is equivalent to λ_A ≥ 0 on
(0, ½log5). This is the primitive-form positivity on windows up to ½log5 = 0.8047, only 0.0047
beyond Zhu's range. It is a consequence of RH, not equivalent to it.

*Proof.* Paper 47 gives λ_A ≥ λ_W ≥ 0 for T ≤ 0.8 (Zhu), monotonicity (lem:monoT) and continuity
(R162_001). ∎

By Theorem 3.1 and Lemma 1.1, any proof of Proposition 5.1's right side must separate κ = 1 from
the model endpoint κ_e(s) for s ∈ C. That is a quantitative margin statement about three specific
numbers (log2/√2, log3/√3, log2/2) against Γ_s. The known routes are a certified margin (a
Zhu-type computation extended by 0.0047, or an explicit modulus of continuity for λ_A applied to a
certified λ_W(0.8) > 0) or the global Sonin lemma (a). Neither is structural in the chamber. The
first is numerics, which the rule allows only when strictly necessary. It would yield only a
window statement, not Gate 1.

**Odd sector (the suggested chamber-restricted exclusion).** Suppose T*_odd > ½log5. Then on C the
odd archimedean form is positive definite, g_odd(0, s) > 0. One might hope this excludes an odd
first contact in C. It does not: an odd kernel vector only needs Π_s(F) = Γ_s(F) ≥ λ_odd(s)‖F‖² > 0,
and Lemma 2.2 shows the comb has such directions. Theorem 3.1 (odd, right endpoint κ_+ ≥ 1)
produces odd models with κ_+ > 1, in which the comb is amplified as in thm:finmod(ii), with odd
chamber first contact or plateau. Positivity of Γ in the odd sector gives only g_odd(κ, s) > 0 for
κ ∈ [0, κ_+(s)), which is consistent with both outcomes. **No odd-sector chamber exclusion is
proved.**

## 6. Falsifier tests

- **F1 (spectral).** This note claims no closure. The countermodels of Theorem 4.1 have λ = 0 and
  two-sided minimality, which is stronger than F1 requires. Any argument that used only items 1–6
  would be refuted by them non-perturbatively.
- **F2 (orientation).** No quadratic estimate of (PC) is used. The models change the weights,
  not the sign of A_M. The discriminating ingredient (a) is an oriented identity (cosine scattering
  with reflection R), consistent with F2.
- **F3 (arithmetic).** Theorem 4.1 is itself an F3 test. The κ-models are the finite modifications
  of thm:finmod, restricted to {2,3,4}. They share the zeros and the pole of ζ, and they violate
  Λ∗1 = log exactly at k = 2,3,4, which by Lemma 1.1 is all of Λ∗1 = log visible in the chamber.
  Epstein/Davenport–Heilbronn data carry a different Gamma factor or a different conductor, so they
  are not chamber models of this form. For ζ's own Gamma factor and conductor 1, Hamburger's theorem
  makes the Poisson structure (a) essentially characterize ζ. This is consistent with (a) being the
  sole discriminator.
- **F4 (linear limit).** Not used.

## 7. Summary of status

| item | status |
|---|---|
| Lemma 1.1 (chamber sees Λ∗1 = log only as three numbers) | PROVED |
| Lemma 1.2 / Cor. 1.3 (germ collar < 0.0095, never reaches ±T) | PROVED |
| Lemmas 2.1–2.3 (concave κ-family, index anchors κ = 0) | PROVED (2.1(iii) inherits R162_001) |
| Theorem 3.1 (dichotomy: ζ or chamber model with first contact / plateau) | PROVED modulo R162_001 |
| Theorem 4.1 (items 1–6 cannot force R_L F = 0 in C) | PROVED — NO-GO |
| Chamber exclusion (even or odd) | NOT PROVED; equivalent to a margin statement |
| Sonin range-intersection lemma (4.2) | OPEN, not localized by the chamber |
| Row D | OPEN |

Recommendation. Drop the first-chamber branch as a structural closing device. Its entire
arithmetic content is three numbers, and every chamber-local identity is blind to them. Any Gate 1
proof must act through the global typed Sonin identity (a), where Λ∗1 = log holds for all k and
the finite-modification defect is supported on all multiples of 2 and 3.
