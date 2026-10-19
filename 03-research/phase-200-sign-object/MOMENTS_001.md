# MOMENTS_001 — Phase 200, round 25: moments (mollified, fourth moment, Motohashi) as a source of sign

Goal: row D / L′♯.
Single file for the round. Not written to the index; the proposed entry is in §8.

---

## 0. Index and corpus check (mandatory)

`grep` on `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` (564 lines) for "moment", "Ingham", "fourth moment",
"|ζ|^4", "|ζ|^{2k}", "Conrey", "Keating", "Heath-Brown", "Motohashi", "EI_002", "R162_1102", "D_μ", "1/ζ", "mollifier",
"channel (iv)", "DH_TRANSFER", "T.1", "Kuznetsov", "Katok", "H_j", "Levinson".

| term | index lines | content |
|---|---|---|
| R162_1102 | l.46 | family of Dirichlet characters, Thm O (average over family); l.553 V3 = retry |
| EI_002 | l.160, l.175 | Q = (1/π)∫F̂₀²|ζ_w|²Re R_{X′}; Poisson over ℤ, ℤ²; sign content = T*₃(η) = (S), REF-D |
| EI_003 / "second twisted moment" | l.162–165 | Symbol rigidity theorem: no exact identity on σ_T is nonlinear in Λ; nonlinearity only enters via h* (REF-D) or via tests built from ζ's coefficients (second twisted moment = mollifier) |
| T.1, D_μ | l.515 | T.1 PROVED; NO-GO "discrete archimedean part": null symbol, mass at zeros, D_μ(ρ) = −1 |
| mollifier / SQ.0 | l.516 | AUDIT_200_SPEC_002: every mollified exterior is −g mod radical at any level Y; Q1 tautological (yᵀ𝔅y = 𝒲[g]); Q2 ladder NO-GO (difference of mollifiers radical, 𝒲 = 0) |
| Ingham | l.527 | Z_CARRIER_001: "Ingham/Estermann/Re ζ′/ζ duplicate EI_002, J.3, AUDIT_16"; R-Z1 |
| DH_TRANSFER | l.550 | channel (i) PROVED; order-≥2 S4 residue (arithmetic constants of moments) ARGUED → OPEN candidate |
| Kuznetsov | l.337 | only as a residue of front A (Salié/Kuznetsov), never developed |
| Motohashi, fourth moment, |ζ|^4, |ζ|^{2k}, Conrey, Keating, Heath-Brown, Katok, H_j, Levinson | **no appearance in the index** | Levinson/Conrey appears in AUDIT_200_SPEC_003 (l.519, zero-coordinate injectivity, as a citation) and in DH_TRANSFER §S3–S4 (table S4, row "mollifiers with μ") |

In the phase 200 corpus: Z_CARRIER_001 §2.2 (Ingham moments, comb-generic diagonal, duplicate of EI_002);
DH_TRANSFER_001 §S2.3–S2.5, table S4, §6 (OPEN candidate); SPEC_SIGN_OBJECT_009 X3b (Selberg, NO-GO via TF⁺, l.42);
LEDGER_L3 l.125 (Kuznetsov never developed).

**New reason, written out.** The DH_TRANSFER §6 candidate was never evaluated. The difference from what is already
on record is concrete:

- Z_CARRIER §2.2 treated the **unmollified second moment** and its diagonal.
- EI_003 ruled out tests built from ζ's coefficients as an *identity on the symbol*.

What changes here is the class of methods: **asymptotic and exact formulas for mollified moments (Conrey 1989) and
the exact spectral formula for the fourth moment (Motohashi), used to evaluate the T.1 form with its weight |ĝ|²**.
Neither Motohashi nor Conrey 1989 appears in the index. The difference in principle evades the reason behind earlier
failures, because the arithmetic constant a_k is nonlinear in Λ (order-2 Euler product). If it survived, it would
escape EI_003's rigidity. §2–§4 decide whether it survives.

---

## 1. Objects (verified against SPEC_SIGN_OBJECT_002, l.29–48)

- μ ≥ 5, a = T = ½ log μ, g even in the core on (−a, a), A(g) = ∫ g e^{x/2} = 0.
- M_μ(s) = Σ_{d<μ} μ(d) d^{−s}, D_μ = ζ M_μ − 1 = Σ_{N≥μ} c_N N^{−s}.
- m(t) = Re ψ(¼ + it/2) − log π, v_n = 2Λ(n) n^{−½}.
- **T.1** (PROVED given Guo L4.3–4.4): W_T(g) = (1/2π)∫|ĝ|²|D_μ(½+it)|² [m(t) − Σ v_n cos(t log n)] dt. The
  archimedean term converges absolutely, and the sum over n is taken term by term.
- **F4** (CA_M, PROVED; DH_TRANSFER Prop 5.1 for the DH analogue): σ(t) := m(t) − Σ v_n cos(t log n) is, as a
  boundary value from Re s > ½, equal to m + 2Re ζ′/ζ(½+it). It is null pointwise away from the ordinates, and its
  distributional boundary value is 2π Σ_{Re ρ=½} δ(t − γ).

Notation: 𝒲[h] is the window Weil form applied directly to the test h, and w(t) := |ĝ(t)|².

---

## 2. Decision (a): is W_T a "moment integral" in Conrey's sense?

### 2.1 Effective length of the weight

**Lemma 2.1 (PROVED).** If g ∈ C_c^k(−a, a), then ĝ is entire of exponential type a and

  |ĝ(t)| ≤ ‖g^{(k)}‖_{L¹} |t|^{−k}.

Hence w(t) = |ĝ(t)|² ≤ C_k |t|^{−2k}. If g ∈ C_c^∞, w decays faster than any power, but never exponentially on ℝ,
unless g ≡ 0 (if |ĝ(t)| ≤ Ce^{−δ|t|}, g would be real-analytic on ℝ, which is impossible for compactly supported
g ≠ 0).

*Proof.* Integration by parts k times. The negative claim is standard (CITED, Paley–Wiener–Schwartz). ∎

The "moment" then has **infinite** length, with a polynomially or superpolynomially decreasing weight. The mass is
concentrated at |t| ≲ t₀(g). For Mori's minimizer g* (μ = 15), F0_TEST_001 l.31–39 localizes the pieces at
|t| = O(1)–O(10²).

### 2.2 What moment theorems say in this regime

The mollified asymptotics (Levinson; Conrey 1989, CITED: ∫_0^X |ζM|² dt = c(θ, P)·X + O(X^{1−ε}) with
θ = log(length)/log X < 4/7) have three features that prevent applying them here:

1. They need X → ∞.
2. They need a mollifier length X^θ tied to X.
3. They have an error term O(X^{1−ε}), generally without an explicit constant.

Decompose W_T dyadically: W_T = Σ_j ∫_{2^j ≤ |t| < 2^{j+1}} (…) + ∫_{|t|<1}.

**Lemma 2.2 (PROVED, regime).** With μ fixed, each dyadic block [X, 2X] with X ≤ μ^{7/4} has θ_X = log μ/log X ≥ 4/7,
and falls outside Conrey's proven range. For X ≤ μ, the polynomial M_μ is longer than the height, and the
Montgomery–Vaughan mean-value theorem (CITED),

  ∫_0^X |Σ a_n n^{−it}|² = Σ |a_n|²(X + O(n)),

has an error O(n) that dominates the main term. The blocks where some mollified asymptotic applies
(X > μ^{7/4} ≈ 114 for μ = 15) are tails, of weight ≤ C_k X^{1−2k}·(log X)^{O(1)}.

*Proof.* It is exponent arithmetic, plus Lemma 2.1's bound and the convexity bound for |ζM_μ|² on the block. ∎

**Corollary 2.3 (PROVED).** For fixed μ, the region where w's mass lies is the "short" region (length O(1) in t, or
X ≤ μ^{7/4}), where no moment theorem produces a main term with an exact arithmetic constant. Where the asymptotics
do apply, only a tail bound is obtained, which is comb-generic (DH_TRANSFER's S2: transfers to DH). The objection
raised in the brief ("short moment") is correct in its precise form: **the moment is not short in length, but in
mass**. The length is infinite, but the useful mass lives where the asymptotics say nothing.

### 2.3 The limit μ → ∞ does not help

If μ → ∞ is taken with g a fixed shape rescaled to the interval (−a, a), a = ½ log μ, then ĝ(t) = a·ĝ₁(at). The
weight concentrates at |t| ≲ 1/a → 0, even closer to t = 0, where |ζ(½+it)| ≈ ½ has no asymptotic behavior at all.
Not even a two-parameter regime (height × length) enters Conrey's range, because the effective height does not grow.
**(a) is decided: NO, in the operative sense.** The form is not a Conrey moment in any available parameter regime
(PROVED in the regime sense: Lemmas 2.1–2.2).

### 2.4 Scale: quantitative impossibility (ARGUED → PROVED in the weak form)

W_T(g*) = 4.978·10⁻⁷⁰ (F0_TEST_001 l.39), and the O(1) pieces cancel to 74 digits (l.33). Any evaluation of the
pieces with relative error ≥ 10⁻⁷⁰ is blind to the sign. Moment errors are O(X^{1−ε}) or, in the best exact case
(Motohashi with fixed w), a spectral sum that must be bounded. **Weak form (PROVED):** no bound whose relative error
is not ≤ 10⁻⁷⁰ decides the sign of W_T(g*). This is trivial, but it rules out the whole "asymptotic + error" class.

However, the decisive point is not the scale. It is the identity of §3.

---

## 3. The decisive fact: T.1's moment part is identically null

### 3.1 Algebraic decomposition on the line

On the line, by the FE: ζ(½−it) = conj ζ(½+it) and ζ(½+it) = e^{−iθ(t)} Z(t) with Z real. Hence conj ζ / ζ = e^{2iθ(t)}
away from the zeros. Write σ = m + 2Re(ζ′/ζ) (boundary value, F4) and |D_μ|² = |ζM|² − 2Re(ζM) + 1. Then, pointwise
away from the ordinates:

  |D_μ|²σ = σ + (|ζM|² − 2Re ζM)·σ.

For the second summand, (|ζM|² − 2Re ζM)·2Re(ζ′/ζ) expands into terms of the form

  ζ′ conj(ζ) |M|²,  ζ′ M,  conj(ζ) conj(M) ζ′/ζ = e^{2iθ} ζ′ conj(M)

and their conjugates. **None of them contain 1/ζ.** The apparent singularity conj(ζ)ζ′/ζ is regular on the line,
because conj(ζ)/ζ is unimodular and real-analytic.

**Lemma 3.1 (PROVED, pointwise identity on the line).** Define

  𝔐_μ(t) := (|ζM_μ|² − 2Re ζM_μ)(½+it)·σ(t),

expanded as above. It is a real-analytic function on ℝ of polynomial growth, with no mass at the ordinates, and is a
combination of "mixed moments" of ζ, ζ′, M_μ and the phase e^{2iθ}. The T.1 form thus splits as:

  W_T(g) = (1/2π)∫ w·σ  +  (1/2π)∫ w·𝔐_μ.

The first term is the Weil form applied to g directly, 𝒲[g], in the sense of the explicit formula: its mass is at
the zeros. The second is a genuine moment integral: an entire integrand in t, a mixture of mollified second moments
and derivatives. This is the Levinson–Conrey class, which in Levinson's method uses V = (ζ + ζ′/L)M.

*Proof.* The algebra is as above. On regularity: at a zero on the line, σ has mass 2πδ, but
|ζM|² − 2Re ζM vanishes there (ζ(ρ) = 0), so the mass of its product with σ is 0·δ = 0. The regular part of σ (F4)
is null away from the zeros, but 𝔐_μ was defined with σ = m + 2Re ζ′/ζ expanded, which is regular in the product. At
an off-line zero there is no mass at the boundary (DH_TRANSFER Prop 5.1(c), identical argument for ζ). ∎

**Remark.** By F4, 𝔐_μ(t) = (|ζM|² − 2Re ζM)·σ(t) = 0 pointwise away from the ordinates, since σ = 0 there. Since the
product has no mass at the ordinates, **𝔐_μ ≡ 0 as a distribution.** This must be read carefully: Lemma 3.1's
expansion into "mixed moments" is a sum of *individually nonzero* pieces (each is ζ′conj(ζ)|M|², etc.) whose sum is
null. The identity is verified without F4, by an independent route:

### 3.2 Verification on the zero side (independent)

**Proposition 3.2 (PROVED given Guo L4.3–4.4, already implicit in SQ.0 / AUDIT_200_SPEC_002).** For all μ ≥ 5 and
every g in the core with A(g) = 0:

  W_T(g) = 𝒲[g],  equivalently  (1/2π)∫ |ĝ|²(|D_μ|² − 1)σ dt = 0.

*Proof.* By the explicit formula in zero form (rem:ext-killing(iii), cited in DH_TRANSFER §S3), the evaluated T.1
form is Σ_ρ Φ(ρ)Φ(1−ρ) with Φ(s) = ĝ(s)·D_μ(s) in T.1's normalization. At every nontrivial zero, D_μ(ρ) = −1 and
D_μ(1−ρ) = −1, because 1−ρ is also a zero. So Φ(ρ)Φ(1−ρ) = ĝ(ρ)ĝ(1−ρ): the sum is that of 𝒲[g]. The polar and Tate
terms vanish in both forms by A(g) = 0 (T.1, step 3: A(Ψ̌_c) = D_μ(0)A(g) = 0). The trivial zeros and the
archimedean part are absorbed into m the same way in both. This is exactly the statement "every mollified exterior
is −g mod radical" (AUDIT_200_SPEC_002, index l.516). ∎

**Corollary 3.3 (NO-GO, PROVED given Guo L4.4).** Let ℳ be any procedure that evaluates (1/2π)∫ w·𝔐_μ, by Conrey's
asymptotics, by Motohashi's exact formulas, or by any other method. The correct result is **zero**, for every μ and
every admissible g. The arithmetic constant that ℳ produces in each piece (c(θ, P), a_2 = ∏_p(…), Estermann d∗d
terms) cancels between the pieces, exactly. **The mollifier is invisible modulo the radical; T.1's moment part
carries no information about the sign, because it equals 0.** What remains is 𝒲[g], which is the original form with
mass at zeros (REF-D by P4).

This closes the question: the "method of moments" applied to T.1 can only reproduce 0 + 𝒲[g]. The difference of two
moment integrals the brief proposed (∫ w|ζM|²w₁ − ∫ w|ζM|²w₂) is, with w₁ − w₂ = σ, the piece 𝔐_μ + (REF-D term).
There is no choice of (w₁, w₂) turning σ into a moment weight with a nontrivial arithmetic constant, because any
"function" weight representing σ away from the zeros is 0 (F4). The only alternative is boundary weights from
Re s > ½. There σ is −2Re Σ Λ(n)n^{−s}+m, a form linear in Λ (EI_003: rigidity). The nonlinear arithmetic constant
would only appear in the products |ζM|²·σ, which sum to 0 by Prop 3.2.

**Relation to objection (a) of the brief.** The length objection (§2) is correct but secondary. The fatal objection
is structural: **even if an exact formula with an arithmetic constant existed for each piece, the sum of the pieces
is 0.**

### 3.3 Does this contradict the pieces having different arithmetic constants for ζ and DH?

No. For DH, D^{DH}_μ is the truncation of 1/F_DH, and D^{DH}_μ(ρ_DH) = −1 also, by definition: F_DH(ρ) = 0 ⇒ D = −1.
Prop 3.2 holds equally for DH in the radical version of GUO_QUANT Prop 1.3 (DH_TRANSFER §S1.4). In DH the pieces have
other constants (without a_2), but they also sum to 0. The difference between ζ and DH then lies in 𝒲[g], i.e. in
the zeros, and that is CERT_DH_001's. **The non-transfer of the moment constants is real piece by piece and null in
the sum.** This proves, in a strong form, DH_TRANSFER §6's last row ("(P-mult) of order ≥ 2 … ARGUED"), for the
concrete case it left open: "the arithmetic constant enters as a coefficient of a moment inequality weighted with
test-dependent weight |ĝ|²|D_μ|²". **That case moves from ARGUED to PROVED (NO-GO)**: the constant enters with total
coefficient zero.

---

## 4. Decision (b): exact Motohashi as a source of ℰ_μ ≥ 0

### 4.1 The formula (CITED)

Motohashi (Acta Math. 1993; 1997 book) gives, for a smooth, rapidly decaying weight w, an exact identity:

  ∫ |ζ(½+it)|⁴ w(t) dt = 𝒫[w] + Σ_j α_j H_j(½)³ Λ_w(κ_j) + (continuous: ∫ |ζ(½+ir)|⁶/|ζ(1+2ir)|² Λ_w(r) dr) + (holomorphic).

- 𝒫[w] is an explicit main term: a polynomial in log with constants that include an a_2-type one, plus the pole.
- α_j = |ρ_j(1)|²/cosh(πκ_j) ≥ 0.
- H_j(½) = L(½, u_j). Its non-negativity H_j(½) ≥ 0 is CITED: Katok–Sarnak, Kohnen–Zagier in the holomorphic case,
  and Guo for Maass forms.
- Λ_w(r) is an explicit integral transform of w (hypergeometric kernels).

### 4.2 Degree: Motohashi does not see the window form

**Proposition 4.1 (PROVED).** The T.1 form is, as a function of ζ, of degree ≤ 2 in (ζ, conj ζ), plus ζ′/ζ in σ.
Lemma 3.1's expansion only contains products with at most one ζ and one conj(ζ) (or one ζ′ and one conj(ζ)). **There
is no |ζ|⁴ term.** Producing |ζ|⁴ would require a test g whose ĝ contains ζ, e.g. ĝ = ζ·ĥ: a test built from ζ's
coefficients. That is EI_003's "second twisted moment" (l.165), which is the mollifier, DEAD (G3D-159 via
Z_CARRIER §2.2). Moreover, that ĝ is not entire of exponential type (ζ has a pole and is not of exponential type on
the line), so g ∉ P_T.

*Proof.* For the degree: T.1 is quadratic in Φ = ĝD_μ, and D_μ is linear in ζ. For P_T: Paley–Wiener, and
ζ(½+it) is not polynomially bounded by e^{a|Im|} in the strip in the required way, with the pole at s = 1 included. ∎

**Does this contradict C-hom/N5 ("there is no quadratic or 4-point identity in theta")?** No. That record says there
is no 4-point identity giving the form. Prop 4.1 says the same from the other side: the form has no fourth-degree
content in ζ. The two statements are consistent and nothing needs reconciling. The fourth moment would only appear
in ⟨Zr, Zr⟩² or in quartic forms in g. Those are not the window form: they are a degree-4 form in the test.

### 4.3 Does the spectral sum serve as the ℰ_μ ≥ 0 of AUDIT_200_SPEC_003?

AUDIT_200_SPEC_003 (l.198–204) asks for a decomposition 𝒲[r] = ‖A_μ r‖² − ℰ_μ[r] with explicit ℰ_μ ≥ 0 and A_μ given
by a formula. For Motohashi to provide it, one would need:

1. 𝒲 to be a combination of weighted fourth moments. This is false by Prop 4.1;
2. the spectral sum to be ≥ 0 for the weights that appear. This is false in general: α_jH_j(½)³ ≥ 0, but Λ_w(κ_j)
   has no fixed sign for arbitrary w ≥ 0. This is the same structure as X3b (SPEC_009 l.42: "destroys ĥ ≥ 0"), with
   the spectral side's positivity cancelled by a signless transform;
3. the explicit term 𝒫[w] not to contain a sum over zeros. This is indeed true for Motohashi: 𝒫 contains no Σ_ρ.
   There is no REF-D in that formula. But point 1 makes this virtue irrelevant.

**Proposition 4.2 (NO-GO, PROVED by 4.1 + 3.2; ARGUED only in sub-point 2).** Motohashi's spectral sum cannot be the
ℰ_μ ≥ 0 of AUDIT_200_SPEC_003 for the window form. The form has no quartic component (4.1), and its only moment
component is identically null (3.2). Sub-point 2 (signless Λ_w) is ARGUED with the standard kernel reference, and is
not needed for the NO-GO.

### 4.4 What remains as an independent object (record, no route)

The positivity α_jH_j(½)³ ≥ 0 is an exogenous positivity (spectrum of Δ on PSL₂(ℤ)\ℍ, Hecke arithmetic). The
falsifier battery sees it thus:

- Epstein: its fourth moment has a different spectral decomposition, with level/character forms of ℚ(√−D).
- DH: has no Hecke spectral decomposition (not Euler).

That is, **it is a Λ-sensitive property in C-τ's sense.** But it lives in a quartic form in g, which is not row D. To
connect it to D would require an inequality 𝒲[g]² ≤ (Motohashi quartic in g) or similar. No known mechanism exists,
and C-hom/N5 excludes it as an identity. It is recorded as **OPEN, no proposal**. Not launched.

---

## 5. Where Λ enters (constants a_k)

- a_2 = ∏_p (1 − p^{−1})⁴(1 + 4p^{−1} + p^{−2})·… (Ingham; Keating–Snaith a_k, CITED) is an invariant of the complete
  Euler product. It is discontinuous in the comb in C-τ's sense: perturbing Λ at one prime p changes the local
  factor. This holds ✓.
- **Does it live on P_T? Not as a net contribution.** By Cor 3.3, the pieces of T.1 carrying a_2 (or, in the
  mollified regime, c(θ, P) with its Euler product) enter with total coefficient 0. In the window form on P_T, Λ
  enters only linearly: v_n = 2Λ(n)n^{−½} in σ. This agrees with EI_003's rigidity.
- In terms of C-E′: Epstein has a different fourth-moment constant (without Euler), and DH has another one
  (DH_TRANSFER table S4). Both differences are real piece by piece and null in the sum: §3.3.

**New constraint (R-MOM, PROVED given Guo L4.4):** *every order-≥2 arithmetic constant in Λ that appears when
evaluating the mollified window form T.1 by moments (Ingham, Conrey, Keating–Snaith, Motohashi, Estermann) enters
with net coefficient zero, because (|D_μ|² − 1)σ annihilates |ĝ|² for A(g) = 0 (Prop 3.2). For such a constant to
affect the sign, the object must exit the degree-2 window form in the test, or exit SQ.0's radical.*

---

## 6. Test on the falsifiers and on Mori μ = 15

| case | what the analysis says | label |
|---|---|---|
| Mori μ = 15, g* | W_T(g*) = 4.978·10⁻⁷⁰ = 𝒲[g*] (Prop 3.2). The moment piece equals 0 exactly. F0_TEST's pieces (arch, band, pole, comb), O(1) and cancelling to 74 digits (l.33), are the expansion of 𝒲[g*], not of 𝔐_μ. No moment method with relative error > 10⁻⁷⁰ resolves them (§2.4) | PROVED (identity); NUMERICAL (value, F0_TEST) |
| Lemma E (Epstein) | Prop 3.2 holds with D^{Ep}_μ and Epstein's radical (Guo Prop 1.3 / GUO_QUANT). The pieces have other constants and sum to 0. The certified negative sign is in 𝒲^{Ep}[g], at the zeros | PROVED given the radical version for Epstein (CITED GUO_QUANT) |
| DH (CERT_DH_001) | Same: D^{DH}_μ(ρ) = −1. F_DH's fourth moment has a different constant (Σ with (1±iκ)/2 and cross terms; DH_TRANSFER S4, CITED via Bombieri–Hejhal for the order). No Motohashi decomposition (not Hecke). None of this enters the form | PROVED (cancellation); CITED (different constant) |
| cΛ, a_P | Combs linear in Λ: the mollifier (if defined) does not change the conclusion. The moment constants are either undefined or non-Euler, and in any case enter with coefficient 0 | ARGUED (cΛ's mollifier definition not fixed) |

No falsifier separates from ζ by this route. This is exactly what is expected of a quantity that is 0 for all of
them.

---

## 7. Labels

| statement | label |
|---|---|
| Lemma 2.1 (decay of |ĝ|², non-exponential) | PROVED (+ CITED Paley–Wiener) |
| Lemma 2.2 / Cor 2.3 (regime: mass outside the Conrey/MV range; comb-generic tails) | PROVED |
| §2.3 (μ → ∞ concentrates the weight at t → 0) | PROVED |
| §2.4 weak form (relative error > 10⁻⁷⁰ blind to the sign) | PROVED (trivial) |
| Lemma 3.1 (decomposition W_T = 𝒲[g] + ∫w𝔐_μ, pieces without 1/ζ on the line) | PROVED |
| Prop 3.2 (W_T(g) = 𝒲[g]; ∫w(|D_μ|²−1)σ = 0) | PROVED given Guo L4.3–4.4 (= SQ.0, AUDIT_200_SPEC_002) |
| Cor 3.3 (every moment evaluation of the mollified part gives 0) | NO-GO, PROVED given Guo L4.4 |
| DH_TRANSFER §6, row "(P-mult) order ≥ 2 with weight |ĝ|²|D_μ|²" | ARGUED → **PROVED (NO-GO)** |
| DH_TRANSFER §6 candidate (moments with arithmetic constant) | **closed: NO-GO** |
| Motohashi (formula, α_j ≥ 0, H_j(½) ≥ 0) | CITED |
| Prop 4.1 (the form has no quartic component in ζ; ĝ = ζĥ ∉ P_T) | PROVED |
| Prop 4.2 (Motohashi is not ℰ_μ) | NO-GO PROVED; sub-point signless Λ_w ARGUED |
| §4.4 (Motohashi quartic inequality → D) | OPEN, no proposal, not launched |
| R-MOM | PROVED given Guo L4.4 |
| L′♯ / row D | OPEN |

---

## 8. Proposed index entry (editor copies it)

> - **MOMENTS_001 (phase 200, round 25; new reason: Conrey 1989 mollified moments and the exact Motohashi formula,
>   never indexed): NO-GO.** DH_TRANSFER §6 residue closed. (a) Regime (PROVED): T.1's weight |ĝ|² has
>   infinite length but mass at |t| = O(1) (or X ≤ μ^{7/4}), outside Conrey's range (θ < 4/7) and MV's (O(n) dominates).
>   Comb-generic tails; μ → ∞ concentrates at t → 0. (Decisive, PROVED given Guo L4.4): W_T(g) = 𝒲[g] and
>   ∫|ĝ|²(|D_μ|²−1)σ = 0 (D_μ(ρ) = D_μ(1−ρ) = −1; = SQ.0). The moment part (pieces ζ′conj(ζ)|M|², ζ′M, e^{2iθ}ζ′conj(M),
>   without 1/ζ on the line) sums to 0 exactly: the arithmetic constants (a_2, c(θ,P), Estermann) enter with net
>   coefficient 0. **R-MOM.** DH_TRANSFER §6 last row ARGUED → PROVED. (b) Motohashi: the form has degree ≤ 2 in ζ,
>   no |ζ|⁴ term; ĝ = ζĥ ∉ P_T (= second twisted moment, EI_003). The spectral sum α_jH_j(½)³Λ_w (α_j, H_j(½) ≥ 0
>   CITED) is not the ℰ_μ of AUDIT_200_SPEC_003 (NO-GO PROVED). Signless Λ_w (ARGUED) = X3b pattern. Mori μ=15:
>   W_T(g*) = 𝒲[g*] = 4.978e−70. The moment piece is 0. OPEN residue with no proposal: quartic inequality (Motohashi)
>   ↔ 𝒲[g]², not indicated by C-hom/N5. **Do not retry: moments of ζ (mollified or not, asymptotic or exact) on the
>   degree-2 window form.**

---

## 9. Next lemma

The structural lesson is that **everything multiplied by |D_μ|² inside T.1 is gauge** (Prop 3.2). All it does is
reproduce 𝒲[g]. An object using nonlinear arithmetic in Λ must act **outside the radical**, i.e. change g's class
modulo 𝔑 (P9′/P10 of AUDIT_200_SPEC_002), not the integration weight.

**Proposed lemma (OPEN, for round 26; index check pending).** Characterize the set of real-analytic, polynomially
growing multipliers η(t) such that ∫|ĝ|²(η − 1)σ = 0 for every g in the core with A(g) = 0 (the form's "multiplicative
gauge group"). Working conjecture: it is exactly {η : η(γ) = 1 at every ordinate, with the right multiplicity}
∪ (the closure of |D_μ|²). If so, the lemma states: **no multiplicative weight, arithmetic or not, changes the
form's value except via its values at the zeros (REF-D)**. That would turn R-MOM into a class theorem, covering
every moment weight at once.

Before launching, search the index for "gauge", "radical", "𝔑", "P9′", "multiplier", "Lemma A.1", "Π_μ", because
PI_MU_001 (l.524) and SPEC_003 (l.518) may already contain it.
