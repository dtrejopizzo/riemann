# Round 4, zone 3: the remainder R(F) of the truncated Möbius test (selection memo)

Selection memo, not a construction memo. Target (★): λ_A(T) ≥ 0 for all T, with the definitions of
`../phase-211-sign-sandbox/STATEMENT_001.md`. Notation from P46 §sec:firstcontact
(`04-papers/46-row-d-sign-radial-intersection-form/main.tex`, l. 6625–6700): V_{−log n}F(t) = F(t + log n), S_N, S′_N,
L_M = Σ_{d≤M}Λ(d)d^{−1/2}V_{−log d}, A_M = 𝓜 − L_M − L_M*, 𝓜 = m(D). Object examined: the remainder R(F) of
`ROUND_003_6.md` (4.2). Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## Cross-check

Searches (grep over all of `03-research/`, P46, P48, the routes index, grid, crossword): "c_N(k)",
"truncated Möbius", "Möbius truncad", "M_N S_N / M_NS_N", "mollifi", "Levinson", "Barban", "Vehov",
"Selberg mollifier". Read as primary sources: P46 l. 6625–6700 (operators, thm:PCfinite) and l. 6760–6790
(subsec:collars), cor:shape (l. 9167–9190); `ROUND_003_6.md` in full; `R170_853` §§0–2, `R170_878` §§0–2,
`R170_879` §§0–2, `R170_880` §§0–2, `R170_881` §§0–2, `R170_882` §§0–2, `R170_883` §§0–2, `R170_896` §§0–3;
`phase-200-sign-object/A_MU_FACTORIZATION_001.md` (d)–(e) and table; `phase-200-sign-object/Z_CARRIER_001.md`
§3.2; `phase-199-frontier-pattern/proof-L-sharp/PROOF_L_SHARP_FF_001_EDGE_RECOMBINATION.md` §§1–3;
`phase-204-refd-tractability/AUDIT_204_TRACT_F_001.md` §3.3; `phase-188-closing-D/L2_BUILD_017` §§1–3;
`N_BUILD_003` (Theorem 1); grid `R162_2300_part6.jsonl` row "Proportion-of-zeros inputs" (mollification =
widening the window, DEAD). Not opened as primary sources: the ≈ 280 files of phases 101–159 where
"mollif" appears in other senses (only seen by grep line), `R170_884`, `N_BUILD_002`, `N_BUILD_005`,
`N_BUILD_006`, `D_CONSTRUCTION_001` (Prop. M), phases 106, 121, 162 and 186–187 beyond grep (no
matches of c_N(k) or truncated Möbius in them). A search without matches does not prove novelty.

**(1) Closest antecedent.** Three, as primary sources:
- `phase-200-sign-object/A_MU_FACTORIZATION_001.md` (d): the multiplier A_μ = 1 − ζM_μ (truncated Möbius)
  as a factor of a square identity; NO-GO there: it is "pure Möbius, exists for every falsifier", the
  positivity of the remainder reduces to that of the target.
- `PROOF_L_SHARP_FF_001` Thm. FF.1 and `Z_CARRIER_001` §3.2: the tail c_N of truncated Möbius acting on
  translates of the window function; the quotient block Σ_N c_N c_{kN} remained OPEN, with its own warning of
  being generic in the comb.
- `R170_878`–`R170_883`: the **compressed** causal inverse (PS_N*P)^{−1} = PM*P and its Möbius incidences
  with boundary; `L2_BUILD_017` Lemma 1: a_T = a_∞ − 2Re⟨U_μF, U_logF⟩ with truncated Möbius.

**(2) New object.** There is no (ℋ_T, V_T, ρ_T). What is new is structural and without sign: the verification of
(4.2), the closed formula for the archimedean part R_0 (Lemma 2), the exact symbol identity for
any translation-invariant approximate inverse (Lemma 3), and a NO-GO with class: in that class the
remainder and the "mollified" form are linear functionals of c_F and any manifest writing of both
adds up to a certificate of the form without the inverse (Lemma 4). Moreover R ≤ 0 is false on P_T (Lemma 5).

**(3) Does it avoid the antecedent's difficulty?** No. The difficulty of A_MU (d) is that the Möbius
multiplier does not depend on the weight; that of this zone is the same, plus one more: (4.2) does not use at all Σ_{d|n}Λ(d) =
log n, only μ ∗ 1 = δ on the integer comb (Lemma 1). The identity holds word for word for every weight,
hence it is of the type of P46 lem:shape-ident.

**(4) Connection with global positivity.** a_T = (a_T + R) − R on P_T (Lemma 1). If R ≤ 0 and a_T + R ≥ 0
on P_T, then (★). But the first is false (Lemma 5) and, in the translation-invariant class, the
pair only redistributes the symbol (Lemma 4).

**(5) Falsifiers.** (4.2) is generic in the weight: it holds for cΛ, a_P, deletions, amplifications and every
weight, because it does not use the value of the weight. No line breaks; the sign would have to come entirely
from the remainder, which is a form with explicit symbol of the same type as a_T. For cΛ, R^{(c)} = R_0 − cR_1 and,
on needles (Lemma 5), R^{(c)} = c·R + O(ε⁵): every sign detected by needles is the same for all c > 0.

**Verdict of the cross-check: essentially a repetition** (A_MU (d); the linear use of Möbius is a certificate,
P46 cor:shape (a)), plus three short lemmas that close the zone in the translation-invariant class. They
are written below because they are complete.

## 1. Verification of (4.2) against P46

**Lemma 1 (PROVED).** Let F be smooth with support in I_T, M ≥ N ≥ e^{2T}, M_N = Σ_{n≤N}μ(n)n^{−1/2}V_{−log n}.
Then M_NS_N = I + U_N, U_N = Σ_{N<k≤N²}c_N(k)k^{−1/2}V_{−log k}, c_N(k) = Σ_{d|k, k/N≤d≤N}μ(d), and

  Re⟨S_NA_MF, M_N*F⟩ = a_T(F) + R(F),
  R(F) = R_0(F) − R_1(F),  R_0 = Σ_k c_N(k)k^{−1/2} Re⟨𝓜V_{−log k}F, F⟩,
  R_1 = Σ_{N<k≤N²} Σ_{d≤M} c_N(k)Λ(d)(kd)^{−1/2} Re c_F(log(k/d)).

*Proof.* Translations, 𝓜 = m(D) and L_M, L_M* are Fourier multipliers: they commute. The coefficient
of k^{−1/2}V_{−log k} in M_NS_N is Σ_{dm=k, d≤N, m≤N}μ(d): it equals Σ_{d|k}μ(d) = [k = 1] if k ≤ N and 0 if
k > N². a_T(F) = Re⟨A_MF, F⟩ by P46 subsec:collars (the d with log d ≥ 2T translate the support out of
I_T). For k > N: ⟨L_MV_{−log k}F, F⟩ = 0 (disjoint supports, shift log(kd) > 2T);
⟨L_M*V_{−log k}F, F⟩ = Σ_{d≤M}Λ(d)d^{−1/2}⟨V_{log d−log k}F, F⟩ and ⟨V_aF, F⟩ = conj c_F(a). ∎

Check against `ROUND_003_6.md`: sign, range (N, N²] and support correct. Two clarifications,
neither is an error: (a) the restriction |log(k/d)| < 2T is automatic (c_F has support in [−2T, 2T]); (b) R
**depends on M** unless M ≥ N²e^{2T}: with M < N² near-coincidences d > M are lost and, if M = N, there is
no diagonal term k = d. In what follows M ≥ N²e^{2T} unless stated otherwise.

c_N(k) at prime powers (PROVED, direct count): c_N(p) = 0 for p ∈ (N, N²]; for a ≥ 2,
c_N(p^a) = −1 if p^{a−1} ≤ N < p^a and 0 otherwise. Hence the diagonal of R_1 is −κ_N‖F‖² with

  κ_N = Σ_{p^a ∈ (N,N²], a≥2, p^{a−1}≤N} (log p)/p^a > 0   (N ≥ 4, by Bertrand: there is p ∈ (√N, N]).

## 2. Structure of R_0 and R_1

**Lemma 2 (closed form of R_0, PROVED).** On P_T, with 𝔸_j(F) = ∫F e^{(2j+½)t}, 𝔹_j(F) = ∫F e^{−(2j+½)t},

  R_0(F) = −Σ_{j≥1} C_j(N) Re[𝔸_j(F) conj 𝔹_j(F)],   C_j(N) = M_N(2j+1)S_N(2j+1) − 1,

with M_N(s) = Σ_{n≤N}μ(n)n^{−s}, S_N(s) = Σ_{n≤N}n^{−s}.

*Proof.* By the Lévy form (STATEMENT §1), for G, F with disjoint supports
⟨𝓜G, F⟩ = −½∫K(|u|)c_{G,F}(u)du; with G = V_{−log k}F the argument runs over |u| = log k − v, |v| < 2T,
where K(|u|) = 2Σ_{j≥0}k^{−(2j+½)}e^{(2j+½)v}. Since Re c_F is even, ∫e^{av}Re c_F(v)dv =
∫cosh(av)Re c_F(v)dv = Re[𝔸 conj 𝔹] (a = 2j+½). The term j = 0 is Re[A(F) conj B(F)] = 0 on P_T.
The factor k^{−1/2}·k^{−(2j+½)} = k^{−2j−1}, and Σ_{N<k≤N²}c_N(k)k^{−s} = M_N(s)S_N(s) − 1. ∎
(NUMERICAL, only validation of the Dirichlet identity: C_1(8) = −0.0060125… from both sides.)

R_0 is thus a sum of hyperbolic forms of rank ≤ 2 with coefficients of size O(N^{−2j}) and unfixed
sign: the "nonlocal part of 𝓜 between I_T and its translate" contains nothing but the moment conditions
of orders 2j+½, j ≥ 1, and the one of order ½ vanishes exactly by the Tate conditions.

**Lemma 3 (symbol identity, PROVED).** Let b be finitely supported with b(1) = 1 and
P_b = Σ b(n)n^{−1/2}V_{−log n}, P̂_b(τ) = Σ b(n)n^{−1/2−iτ}; let s_M(τ) = m(τ) − 2Re L_M(½ + iτ) be the symbol of
A_M. For F smooth with support in I_T,

  Re⟨P_bA_MF, F⟩ = (1/2π)∫ Re P̂_b(τ) · s_M(τ) |F̂(τ)|² dτ.

If moreover b(k) = 0 for 1 < k ≤ e^{2T}, the left-hand side is a_T + R_b with
R_b = (1/2π)∫Re(P̂_b − 1)s_M|F̂|². For truncated Möbius, P̂ = M_N(½+iτ)S_N(½+iτ) and

  a_T + R = (1/2π)∫ Re[M_N S_N(½+iτ)] s_M |F̂|²,   R_1 = (1/2π)∫ Re[U_N(½+iτ) conj L_M(½+iτ)] |F̂|²,

with U_N = M_NS_N − 1; the other half, Re[U_N L_M], has frequencies log(kd) > 2T and integrates to zero against
|F̂|² for an F in the window.

*Proof.* P_bA_M is a multiplier with symbol P̂_b s_M; s_M is real and Re P̂_b is even (b real), hence
Re⟨P_bA_MF, F⟩ = (1/2π)∫Re(P̂_b)s_M|F̂|². ∎

## 3. What the window sees and the NO-GO with class

The window enters only through the support of F. Every operator in (4.2) is a Fourier multiplier: there is no
compression Q_T, nor M_t, nor finite rank. For such operators ⟨XF, YF⟩ = (1/2π)∫conj(Ŷ)X̂|F̂|²,
a linear functional of c_F, and the symbol is determined modulo functions whose spectrum does not touch (−2T, 2T)
(plus forms vanishing on P_T). That is exactly the degree of freedom of the measure
certificates of P46. The restriction to the window introduces nothing the symbol does not see.

**Lemma 4 (NO-GO with class 𝒯_inv, PROVED).** Class 𝒯_inv: identities on P_T ∩ C_c^∞(I_T) of the form
a_T = Q_1 − Q_2, with Q_1 = Re⟨P_bA_MF, F⟩ and Q_2 = R_b for any translation-invariant approximate inverse
P_b (truncated Möbius, smoothed Möbius, Selberg or Barban–Vehov weights,
b independent of the weight or not), and sign statements for each Q_i proved by a manifest writing:
Q_i = (1/2π)∫σ_i|F̂|² + τ_i(F) with σ_i ≥ 0 almost everywhere and τ_i ≡ 0 on P_T (the window is used only
to change σ_i within its class modulo the annihilator). Then:
(a) Q_1 ≥ 0 and −Q_2 ≥ 0 manifest give a_T = (1/2π)∫(σ_1 + σ_2)|F̂|² + τ_1 + τ_2: a certificate of class (D)
    of P46 for a_T, in which b does not appear. The same certificate is obtained with b = δ_1.
(b) In particular, the pair "a_T + R manifestly ≥ 0 and R manifestly ≤ 0" is impossible
    pointwise (σ_i ≡ literal symbols): adding, s_M ≥ 0 almost everywhere, false because
    s_M(0) = m(0) − 2Σ_{d≤M}Λ(d)d^{−1/2} < 0 for M ≥ N ≥ e^{2T} ≥ 2 (m(0) = C_0 < 0).
(c) Every (G) with V_T in the multiplier algebra is a partition of the symbol (R3-a without J).
*Proof.* (a) Q_1 − Q_2 = a_T and the sum of manifest writings is manifest; the σ_i depend on b
but their sum is a symbol of a_T modulo the annihilator. (b) It is (a) with τ_i = 0 and without annihilator.
(c) ‖V_TF‖² = (1/2π)∫|v̂|²|F̂|²; ρ_T = a_T − ‖V_TF‖² has symbol s_T − |v̂|². ∎

What Lemma 4 does not say: it does not prove that certificates of a_T do not exist (that is the content of λ^prim, P46
cor:shape (a)); it says that the approximate inverse adds nothing to that route, already recorded.

**Lemma 5 (R ≤ 0 is false on P_T, PROVED).** For M ≥ N² and N ≥ 4 there exists F ∈ P_T ∩ C_c^∞(I_T) with R(F) > 0.
*Proof.* Let ψ_ε ≥ 0 be a bump of width ε centred in the interior of I_T and φ = (¼ − ∂²)ψ_ε: by parts
∫φe^{±t/2} = 0, hence φ ∈ P_T, and likewise its translates inside I_T. The atoms of R_1 form a finite
set {u_i} ⊂ (−2T, 2T); take ε less than half the minimal distance between distinct atoms. Then
c_φ has support in |u| < 2ε and R_1(φ) = −κ_N‖φ‖². For R_0: |𝔸_j(φ)|, |𝔹_j(φ)| ≤ C_j‖ψ_ε‖_1 = O(hε) if ψ_ε
has height h, while ‖φ‖² ≍ h²ε^{−3}; and Σ_j|C_j(N)| < ∞, hence R_0(φ) = O(ε⁵)‖φ‖². Thus
R(φ) = κ_N‖φ‖²(1 + O(ε⁵)) > 0. ∎

With F = φ + sV_uφ (u an atom, s real) one gets R(F) = ‖φ‖²[κ_N(1 + s²) − w̃_u s] + O(ε⁵), with w̃_u the
coefficient of Re c_F(u) in R_1 summed over ±u. If |w̃_u| > 2κ_N for some atom, R also takes
negative values and is indefinite. NUMERICAL (validation of one point): T = 1, N = 8, M = N²e²: κ_8 = 0.2695,
max|w̃_u| = 1.175 at u = log 5 > 2κ_8; T = 1.5, N = 21: κ = 0.219, max|w̃_u| = 1.304. R is indefinite in
those cases.

**Corollary 6 (blindness to the weight on needles, PROVED).** For the weight cΛ, R^{(c)} = R_0 − cR_1 (R_0 and c_N do not
see the weight), and on the needle tests of Lemma 5, R^{(c)}(F) = c·R(F) + O(ε⁵)‖φ‖². The sign of R
detected by needles is the same for all c > 0. For a_P (P > e^{2T}) the atoms with
d < P disappear from R_1 and the others stay the same: the remainder changes its distribution, not through a property of Λ.

## 4. Answer to selection question (v)

- Dependence on the weight: R_0 does not depend on the weight; R_1 is linear in it (proportional to c under cΛ);
  a_T + R = Re⟨S_NA_MF, M_N*F⟩ is affine in c. Correct as stated.
- Choice of inverse with R ≤ 0 on P_T? For truncated Möbius with M ≥ N², no (Lemma 5). For a general b
  the diagonal of R_b is −Σ_{k prime power}b(k)Λ(k)/k: it can be made negative by loading b on
  prime powers, but then a_T + R_b ≤ a_T and the pair only moves the problem; in the class
  𝒯_inv with manifest writings the pair adds up to a certificate independent of b (Lemma 4).
- The zone does not die only because of "affine in the weight" (the set of c where an affine pair holds is an interval and
  could end at 1): it dies because it is linear in c_F within the multiplier algebra (Lemma 4) and because
  (4.2) is generic in the weight (Lemma 1). Affinity enters only in Corollary 6.

## Result

NO-GO with class 𝒯_inv (Lemma 4) plus repetition (A_MU_FACTORIZATION_001 (d); P46 cor:shape (a)). No new
mechanism; no candidate ready for construction. Global sign OPEN.

## What was proved

1. Lemma 1: (4.2) correct against P46 (sign, range (N, N²], support); R depends on M unless M ≥ N²e^{2T};
   c_N at prime powers and the diagonal −κ_N of R_1.
2. Lemma 2: R_0 = −Σ_{j≥1}(M_NS_N(2j+1) − 1)Re[𝔸_j conj 𝔹_j]; the order ½ vanishes by Tate.
3. Lemma 3: symbol identity a_T + R_b = (1/2π)∫Re P̂_b s_M|F̂|² for every invariant inverse.
4. Lemma 4: NO-GO with class 𝒯_inv; the pointwise version is impossible because s_M(0) < 0.
5. Lemma 5: R ≤ 0 is false on P_T (M ≥ N², N ≥ 4); indefinite at T = 1 and 1.5 (NUMERICAL).
6. Corollary 6: sign of R on needles blind to c > 0.

## What failed and why

The identity (4.2) only uses μ ∗ 1 = δ on the integer comb; it does not touch the weight and therefore does not break under
any weight falsifier. All its operators are multipliers, so that a_T + R and R are
linear functionals of c_F: choosing the approximate inverse only redistributes the symbol, and the remainder R has
positive diagonal κ_N, which prevents R ≤ 0.

NOT excluded (no object written):
1. inverses **compressed** to the window (Q_TM_NQ_T, the causal inverse (PS_N*P)^{−1} = PM*P of R170_878–883):
   they are not translation-invariant and fall outside Lemma 4; already traversed in phase 170 (RULES_AVOID
   §I2), reopening requires a new reason;
2. uses nonlinear in c_F (products of two functionals of the family, Gram determinants of
   (S_NA_MF, M_N*F)) that are identities and not bounds;
3. the quotient block Σ_N c_N c_{kN} of `Z_CARRIER_001` §3.2 (Lemma Z.2, OPEN), which lives in the other
   orientation (Möbius tail acting on the window function, not on the remainder of the form);
4. inverses with b depending non-affinely on the values of the weight.

## Concrete next step

Do not build on R(F) with translation-invariant inverses. Record in the index and in the grid:
"Phase 212, round 4, zone 3: remainder R(F) of truncated Möbius. (4.2) verified, generic in the weight; R_0 in
closed form via moments 2j+½; NO-GO with class 𝒯_inv (invariant inverse + manifest writings = a
certificate independent of the inverse); R ≤ 0 false (diagonal κ_N > 0). Global sign OPEN." A second
reading should redo Lemma 2 (factor −½·2 and the vanishing of j = 0) and Lemma 5 (order O(ε⁵) of R_0).
