# GUO_QUANT_001 — Is there a quantitative version of Guo L4.4 that separates Λ from the falsifiers? (phase 200, round 7)

CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. Script: `GUO_QUANT_001_data/guo_quant_test.py` (mpmath; §3 only).

**One-line result.** Guo L4.4 is a divisor identity ("the Mellin transform of the summation is L·f̃, and L·f̃ vanishes
where L vanishes") that holds for every Dirichlet series with an explicit formula: a_P and DH are in their own radical, cΛ
separates only linearly (defect (1−c)·arch, already recorded), Beurling stays conditional on the continuation. The three
candidate quantitative readings all die: the condition count (i) is falsified by Epstein; the conductor (ii) acts
with the sign that helps, not the one that separates; the Tate part (iii) is rank one and positive for **every** set of zeros
in the open strip. The μ = 15 test gives W*/(J²Σ|ρ|⁻²) = 1.02175 (even) and 1.1200 (odd): it is not an identity, and the pure jump
model predicts 2.78, not 1. Site (β) of Z_CARRIER is **closed as a separation site**. No sign.

## 0. Index and corpus check

Grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` ("Guo", "L4.4", "radical", "Poisson", "Φ_f", "quantitativ"):

| entry | what it closed | relation to this memo |
|---|---|---|
| l.447 (CCM connection candidate + Guo residual identity) | Guo used as **identity** (P2); falls on L81 | here we ask whether a **non**-identity version exists |
| l.452 PROOF_L_SHARP_A_001 Thm 1.1 | W_T(Ef) = 𝒲_ext[…] (Guo as identity) | used as is |
| l.454 PROOF_L_SHARP_C_001 | E = multiplication by ζ in Mellin (Guo CITED); the sum of zeros is transferred to the tail | this is §1.1 below; here the falsifier test is added |
| l.507 OO_001 (Kreĭn, Γ₀ = Tate functionals) | NO-GO retry; uses Guo 4.4 | the Tate part of §2.3 is not its triple; only the constant is evaluated |
| l.515–519 SPEC_002/003, Q2_LADDER | every exterior mollified ≡ −g mod radical (given L4.4); Q1/Q2 tautological | confirms that passing to the quotient by the radical gives no sign |
| l.415 INV_V_002 | V*Ш = 2log|x|·Ш separates Λ from a_P, cΛ, Beurling **quantitatively but linearly** | §1.3(b) reproduces that linear defect for cΛ; not retried |
| PI4_JUMPS_001 (Tate mode, residue −½f(0)); Z_CARRIER_001 §4 (W* ≈ J²·0.0231); MORI15 §5.5 ("coincidence, do not build on it") | | §2.3 and §3 decide the coincidence |

**New reason (in writing).** No entry (a) evaluates L4.4 **by falsifier** (is a_P/DH/Beurling in its own radical
or in that of ζ?), (b) counts the admissibility conditions as an integer invariant, or (c) computes the ratio
W*/(J²Σ|ρ|⁻²) with J recomputed from the eigenvector. MORI15 recorded (c) as a coincidence without computing it precisely. The memo does not
build any new object on closed routes: it decides whether site (β) of Z_CARRIER_001 has quantitative content.

## 1. What L4.4 exactly is, and what fails for each falsifier

### 1.1 Proof of "Φ_f ∈ rad 𝒲" from the explicit formula (PROVED, classical; reconstruction of the usage in Paper 47)

Conventions from Paper 47 §22: f even in C², compact support in [−λ, λ] (λ = e^T), admissible: f(0) = 0, ∫f = 0.
Summation (a_n ≡ 1): (E_1 f)(u) = Σ_{n≥1} f(nu). Mellin: f̃(s) = ∫_0^∞ f(u)u^{s−1}du (holomorphic for Re s > 0, and by the
Taylor expansion at 0 it continues to Re s > −2 except for a simple pole at s = 0 with residue f(0)).

**Lemma 1.1.** Φ_f(s) := ∫_0^∞ (E_1 f)(u) u^{s−1} du = ζ(s) f̃(s), for Re s > 1, and it continues to an entire function on
−2 < Re s, with rapid decay in |Im s| on vertical strips.

*Proof.* Fubini for Re s > 1: Σ_n ∫ f(nu)u^{s−1}du = Σ n^{−s} f̃(s). Continuation: ζ has a simple pole at 1 with residue
1, and f̃(1) = ∫_0^∞ f = ½∫_ℝ f = 0, so the pole cancels; f̃ has a simple pole at 0 with residue f(0) = 0, so it
disappears too (even though ζ(0) = −½ ≠ 0). Decay: f ∈ C² compact ⇒ |f̃(σ+it)| ≪ |t|^{−2}, and ζ grows polynomially. ∎

**Proposition 1.2 (L4.4 in the form used).** For every test Φ (Mellin transform of a function in Paper 47's class),
𝒲(Φ_f, Φ) = 0, where 𝒲 is the complete Weil distribution (archimedean − primes + poles).

*Proof.* Explicit formula (Weil; CITED) applied to the pair (Φ_f, Φ): archimedean − Σ Λ(n)n^{−½}(…) + [Φ_f(1)Φ(0) +
Φ_f(0)Φ(1)] = Σ_ρ Φ_f(ρ)Φ(1−ρ). Right-hand side: Φ_f(ρ) = ζ(ρ)f̃(ρ) = 0 for every nontrivial zero (Lemma 1.1, f̃ is
holomorphic at ρ). Polar terms: Φ_f(1) = Res_{s=1}ζ·f̃(1)… more precisely Φ_f(1) = lim (ζ f̃)(s) = f̃′(1)·1 + 0 is finite, and
the polar term of 𝒲 is the **evaluation of the pole of −ζ′/ζ**, which with Paper 47's normalization is written as the
pairing against Φ_f at 0 and 1; both values come from the same entire continuation and the explicit formula for Φ_f
accounts for it as a sum over the divisor of ζ (zeros − pole) of Φ_f(·)Φ(1−·). In the divisor of ζ·f̃ the zeros of ζ lie
inside the divisor of Φ_f, and the pole of ζ and that of f̃ cancel; so the sum over the divisor of ζ is zero. Equivalent
and shorter: 𝒲(Φ_f, Φ) = (1/2πi)∮ (ζ′/ζ)(s) Φ_f(s) Φ(1−s) ds (contour surrounding the strip, plus the archimedean part moved by the
functional equation), and (ζ′/ζ)Φ_f = ζ′f̃ is **holomorphic** on the closed strip except where f̃ might have poles (none, since f(0)=0) and at s = 1
(where ζ′ has a double pole but f̃ has a simple zero: what remains is a simple pole with residue −f̃′(1)… which is exactly the one that
compensates the polar term of 𝒲). Absolute convergence: decay of f̃ (CITED Guo; Paper 47 thm:ext-half). ∎

The structural form, which is what matters: **rad 𝒲 ⊇ {L·h : h holomorphic, admissible} with L the function whose logarithmic
derivative defines the comb**. The identity Λ∗1 = log (rem:ext-killing(ii)) is exactly the statement that
−ζ′/ζ · ζ = −ζ′, i.e. that the comb of the form (Λ) and the coefficients of the summation (1) are the coefficients of −L′/L and of L
**for the same L**. Nothing more.

### 1.2 The general principle (PROVED)

**Proposition 1.3 (L4.4 is comb-generic).** Let L(s) = Σ a_n n^{−s} with meromorphic continuation to a strip containing
[0,1] (or to ℂ), finitely many poles in the strip, and let 𝒲_L be the "zero-side" distribution Σ_{div L} Φ(·)Ψ(1−·) (signed
divisor: zeros +, poles −), written via L's explicit formula as archimedean_L − comb(−L′/L) + poles. Let
E_a f(u) = Σ a_n f(nu). If f̃ cancels every pole of L·f̃ in the strip (admissibility conditions ⟨L⟩), then
Φ^{a}_f = L·f̃ is in rad 𝒲_L.

*Proof.* Identical to 1.2: the Mellin transform of E_a f is L·f̃ (Fubini); the sum over div L of (L f̃)(ρ)Φ(1−ρ) vanishes at the
zeros via the factor L and at the poles via admissibility. ∎

### 1.3 By falsifier

**(a) a_P** (P finite; L_P(s) = ζ(s)Π_{p∈P}(1−p^{−s}), coefficients a_n = 1_{(n,P)=1}). Φ^P_f = ζ·Π(1−p^{−s})·f̃ vanishes
at the zeros of ζ **and** at the zeros s = 2πik/log p (Re s = 0) of the local factor. Poles: s = 1 cancelled by ∫f = 0; s = 0:
L_P(0) = 0 (each factor vanishes), so f(0) = 0 **is not needed**. By Prop. 1.3, **Φ^P_f ∈ rad 𝒲_{L_P}** (PROVED).
Moreover, Φ^P_f ∈ rad 𝒲_ζ as well (it vanishes at the zeros of ζ). **Decision: L4.4 does not separate a_P; site (β) is dead
for a_P** (PROVED). Note: the falsifier a_P lives in the form 𝒲_{L_P}, whose divisor includes the zeros on Re s = 0, and
the radical identity absorbs them the same way it absorbs the on-line ones.

**(b) cΛ** (comb ×c, summation a_n ≡ 1 unchanged). Writing 𝒲_c = arch − c·primes + poles_c and using 𝒲 = arch −
primes + poles:
 𝒲_c(Φ_f, Φ) = c·𝒲(Φ_f,Φ) + (1−c)·[arch(Φ_f,Φ) + poles(Φ_f,Φ)] + (poles_c − poles)(Φ_f,Φ)
 = (1−c)·arch(Φ_f,Φ) + O(polar), (PROVED, linear algebra)
and since f(0)=∫f=0 the polar terms with Φ_f vanish: **𝒲_c(Φ_f,Φ) = (1−c)·arch(Φ_f,Φ)**. Φ_f ∉ rad 𝒲_c, by a defect that is
**linear in (1−c)** and linear in Φ. This is exactly the linear defect of INV_V_002 (Λ∗1 = log as an operator identity);
class identification (I4/N_018). The "correct" summation for cΛ would be a_n = d_c(n) (coefficients of ζ^c), with which
there is once again a radical identity (Prop. 1.3 with L = ζ^c, divisor c·zeros − c·pole, multivalued but with −L′/L = cΛ-series).
Conclusion: cΛ separates only because a_n ≡ 1 was fixed with comb cΛ; there is no quadratic content. NO-GO (duplicate).

**(c) Beurling** (𝒫, generalized integers N_𝒫, ζ_𝒫). Mellin transform of Σ_{ν∈N_𝒫} f(νu) = ζ_𝒫(s)f̃(s) for Re s > 1. The radical of
𝒲_𝒫 (comb Λ_𝒫, archimedean Γ_ℝ) exists **only if** ζ_𝒫 continues to the strip with a functional equation of factor Γ_ℝ:
otherwise the explicit formula for 𝒲_𝒫 carries an extra term −(1/2πi)∫ Φ_f Φ(1−·)(H′/H) on the boundary of the continuation
region (ζ_𝒫 = ζ·H). There is an exact radical with respect to the "proper" distribution 𝒲_{ζ_𝒫} whenever ζ_𝒫 continues to the
[0,1]-strip (Prop. 1.3), but that distribution does not carry the Γ_ℝ archimedean term. CONDITIONAL (on the continuation); as a
separator, what separates is the **existence of continuation / functional equation**, not a quantity: not quadratic. NO-GO as a sign site.

**(d) DH** (a_n periodic mod 5, L_DH = combination of L(s,χ), L(s,χ̄), functional equation with conductor 5, no pole). Φ^{DH}_f = L_DH·f̃
vanishes on the whole divisor of L_DH, including zeros off the line. Poles: none at s = 1 (∫f = 0 is not needed);
at s = 0, f(0) = 0 is needed only if L_DH(0) ≠ 0 (generically yes). **Φ^{DH}_f ∈ rad 𝒲_{DH}** (PROVED by Prop. 1.3, which is
the explicit formula for L_DH; Euler is not used anywhere).

**Honest conclusion of §1 (PROVED).** L4.4 is an identity that holds for every L with an explicit formula (no Euler
product needed) provided the summation uses the coefficients of L and the comb uses those of −L′/L. As an identity it is
comb-generic; it separates only when coefficients and comb are decoupled (cΛ), and then only linearly. **Site (β) of
Z_CARRIER_001: dead as an identity.** The only thing that could separate is the form on the complement of the radical — which is (★★).

## 2. The form on the complement: three quantitative candidates

By §1, all information about L′♯ lives in 𝒲 restricted to a complement of rad 𝒲 in the class of tests, i.e. in the quotient
of the carrier by the gauge (prop:ext-gauge: ℓ(g) = 2dist²(r_f, 𝒢̄_T)). We look for **quantitative** properties of ζ's
explicit formula absent in the falsifiers.

### 2.1 (i) Count of admissibility conditions (counting output)

Define κ(L) := number of poles of L·f̃ in the closed strip 0 ≤ Re s ≤ 1 that admissibility must cancel = [L has a pole
at 1] + [L(0) ≠ 0]. This is the codimension of the admissible space (linear in f: f̃(1), f(0)).

| L | pole at 1 | L(0) | κ |
|---|---|---|---|
| ζ | yes (res. 1) | −½ | **2** |
| a_P: ζ·Π(1−p^{−s}) | yes (res. Π(1−1/p)) | 0 | 1 |
| DH (mod 5) | no | ≠ 0 (generic) | 1 |
| cΛ (ζ^c) | order-c singularity (branch) | (−½)^c | not an integer / not defined |
| Beurling ζ_𝒫 | yes (density) | no continuation in general | 1 or undefined |
| **Epstein ζ_Q, Q = x²+5y² (h = 2)** | yes | ζ_Q(0) = −1 ≠ 0 | **2** |
| Dedekind ζ_K, K imaginary quadratic | yes | −h/w·… ≠ 0 | 2 |

Among the five falsifiers of the panel, only ζ has κ = 2: the counting output **distinguishes** ζ from a_P, DH, cΛ, Beurling
(PROVED, elementary table). But **it is not a separator**: the Epstein zeta function of a class-number->1 form has
κ = 2, a functional equation, no Euler product, and zeros off the line (Davenport–Heilbronn 1936; CITED). Hence
no inequality whose only arithmetic input is "κ = 2" can be true (explicit falsifier: Epstein; NO-GO for the
counting output, conditional only on the target inequality being of the same form in Epstein's coordinates, with
Γ(s)(2π/√20)^{−s} instead of Γ_ℝ — see (ii)). Also, imaginary quadratic Dedekind also has κ = 2: κ does not see Euler.
The "one fewer condition for DH" is real but it is an invariant of the **existence of the pole**, not of positivity.

### 2.2 (ii) Conductor 1

In the explicit formula, a factor N^{s/2} adds to the archimedean term (log N)·Φ(½)… in the quadratic form of the
convolution this is (log N)·c_g(0) = (log N)‖g‖², **diagonal and positive** (PROVED, one line: d/ds log N^{s/2} = ½log N constant).
Thus DH (N = 5) receives +log 5·‖g‖² **in favor of** positivity and still violates it; conductor 1 is the **weakest** case of
the archimedean term, not a sign mechanism. As a separator it enters with the wrong sign: NO-GO (PROVED in the form "the
conductor term is a positive multiple of the identity, monotone in N"). What conductor 1 does distinguish is the
absence of a shift in the Poisson scale (ℤ vs ℤ/5): but that is the lattice, already closed (INV_V_002 V2.2(c): everything
holds for αℤ).

### 2.3 (iii) The Tate part: candidate "Tate Theorem" and its decision

**Exact computation (PROVED).** For the boundary mode 𝔪_T with Φ_𝔪(s) = e^{−sT}/s ·e^{T/2} (symmetrically normalized about ½), and
any set of zeros 𝒵 symmetric under ρ ↦ 1−ρ, ρ ↦ ρ̄ inside the open strip:
 Σ_{ρ∈𝒵} Φ_𝔪(ρ)Φ_𝔪(1−ρ) = Σ_ρ 1/(ρ(1−ρ)) =: S(𝒵).
For ζ, S = 2Σ_ρ Re(1/ρ) = 2 + γ − log 4π = 0.0461914… (Hadamard: B = −Σ Re 1/ρ; CITED Davenport ch. 12), and below the
critical line Σ_{γ>0}|ρ|^{−2} = S/2 = 0.0230957….

**Lemma 2.1 (universal positivity of the Tate part; PROVED).** For every ρ = β + iγ with 0 < β < 1,
Re[1/(ρ(1−ρ))] = (β(1−β) + γ²)/|ρ(1−ρ)|² > 0. Hence S(𝒵) > 0 for **any** 𝒵 in the open strip (in particular for
DH, Epstein, a_P except for the zeros on Re s = 0, cΛ with c·zeros).

*Proof.* ρ(1−ρ) = β(1−β) + γ² + iγ(1−2β); real part of the inverse = real part of the number / modulus². ∎

(For a_P, the zeros on Re s = 0 have β = 0: contribution (γ²)/(γ⁴+γ²)·… also > 0; the lemma holds on the closed strip
except for ρ = 0, 1.)

**Candidate "Tate" theorem (statement).** Let g be in the core with boundary value J = g(T), and decompose Ef = J·𝔪 + h
with h ⟂ 𝔪 in the sense of the zero-side form. Then
 W_T(g) = J²·S/2·c_T + 2J·𝒲⁰(𝔪, h) + 𝒲⁰[h]. (2.1)
The first piece is rank one, exists only if there is a boundary (and, via PI4, only if the pole/value ζ(0) creates the mode), and is positive
by Lemma 2.1. **But Lemma 2.1 makes this piece comb-generic:** it is positive for any divisor in the strip,
so it cannot carry the information that distinguishes ζ. All the separation is left in 2J𝒲⁰(𝔪,h) + 𝒲⁰[h], which is
(★★) on the complement of 𝔪. NO-GO for (iii) as a separator (PROVED: the candidate dominant term is positive for all the
falsifiers that have a Tate mode). What Λ does contribute: the **residue 1** fixes that the mode exists (κ = 2) and that the
constant is S(ζ) = 2+γ−log4π; for DH the constant would be S(DH) > 0 just the same.

And moreover the candidate theorem is **false as an approximation** at the extremal (§3): not even the form "W* ≈ J²·S/2" is
stable across sectors or compatible with the jump model.

## 3. Test μ = 15 (NUMERICAL)

Data: MORI15_EXTREMAL_001_data (Mori's bottom eigenvector, d = 832 Legendre modes per parity, L = T = ½log 15).
J recomputed as Σ_k v_k φ_{j_k}(L), φ_j(L) = √((2j+1)/2L), at 60 digits; matches `p0_prolate_M28.json` g(T) to
20 digits (and g(0) too), which fixes the normalization.

| sector | J = g*(T) | Q = W_T (compr.) | Q/(J²·Σ_{γ>0}|ρ|⁻²) |
|---|---|---|---|
| even | −1.42076774585075313667·10⁻³⁴ | 4.76346613556555724995·10⁻⁷⁰ | **1.02175225612** |
| even, + tail Ω (1–2)·10⁻⁷¹ | | | 1.043 – 1.065 |
| odd | −1.53677094978821·10⁻³² | 6.10904110103908·10⁻⁶⁶ | **1.12001403321** |

Pure jump model (F(t) ≈ 2J sin(Tt)/t, W ≈ Σ_{γ>0}2|F(γ)|²): with 300 exact zeros plus the tail via Riemann–von Mangoldt
density, Σ/Σ|ρ|⁻² = **2.7785** (≈ 4·Σγ⁻² /Σ|ρ|⁻² with the average ⟨sin²⟩ = ½ and the log t weighting), not 1.

**Reading (ARGUED on NUMERICAL).** (1) The ratio is not 1 to many digits: 1.0218 in the even sector, 1.12 in the odd one;
it is not an identity. (2) The "natural" value under the jump hypothesis is ≈ 2.78, not 1: the 2%-level even-sector coincidence does not come
from the boundary mechanism (MORI15 §5.5 already observed that the boundary is a boundary layer: |g*| ~ 10⁻³³ at T − 10⁻³, and the zeros with
γ ≤ 705 do not resolve a jump). (3) The sensitivity to the tail Ω (+2–6%) is of the same order as the discrepancy. Verdict:
**numerical coincidence**, with no identifiable remainder worth pursuing: the "remainder" in (2.1) is not small, it is everything. This
confirms MORI15's warning ("do not build on it"), now with the exact number.

## 4. Conclusion

### 4.1 Labels
- PROVED: Lemma 1.1, Prop. 1.2 (classical, reconstruction), Prop. 1.3 (L4.4 for every L with an explicit formula and admissibility
  ⟨L⟩); §1.3(a) a_P ∈ rad 𝒲_{L_P} and ∈ rad 𝒲_ζ, with one fewer condition; §1.3(b) 𝒲_c(Φ_f,Φ) = (1−c)·arch(Φ_f,Φ); §1.3(d) DH
  ∈ rad 𝒲_{DH}; κ table; conductor term = (log N)‖g‖² ≥ 0; Lemma 2.1 (S(𝒵) > 0 for every divisor in the strip).
- CITED: Weil's explicit formula; Hadamard (2+γ−log4π); Davenport–Heilbronn (Epstein h > 1 with zeros off the line);
  Guo L4.4 via Paper 47 thm:ext-half, prop:ext-gauge (Guo's paper is not in the repository).
- CONDITIONAL: (c) Beurling — radical only under continuation of ζ_𝒫 to the strip.
- NO-GO: site (β) as a separator (comb-generic identity); (i) κ count (Epstein falsifier); (ii) conductor 1 (wrong
  sign); (iii) Tate part as the dominant term (positive for every divisor).
- NUMERICAL: Q/(J²Σ|ρ|⁻²) = 1.02175 (even), 1.12001 (odd); jump model 2.78.
- OPEN: (★★) on the complement of rad 𝒲 ⊕ ℝ𝔪; L′♯; row D.

### 4.2 New constraint (for AUDIT_CONSTRAINTS)
**C-Guo.** Every argument that uses rad 𝒲 (Guo L4.4) or its consequences (gauge, Tate mode, condition count) as a
sign input must name which property of ζ **absent in Epstein (h = 2)** it uses: Epstein has a functional equation, a pole with residue,
ζ_Q(0) ≠ 0 (κ = 2), its own radical identity, and a positive Tate part, and it has no Euler product. The four sites
examined here fail this test. Corollary: Λ's input must be multiplicative (Euler) and must enter **quadratically** in the
complement of the radical; neither the divisor nor the poles suffice.

### 4.3 Index entry (paste into ROUTES-TRIED-INDEX)
- **GUO_QUANT_001 (phase 200, round 7; quantitative version of Guo L4.4 / site (β) of Z_CARRIER):** L4.4 = divisor
  identity (Mellin transform of the summation = L·f̃; PROVED for every L with an explicit formula, no Euler): a_P ∈ rad 𝒲_{L_P} (one
  fewer condition), DH ∈ rad 𝒲_{DH}, cΛ only a linear defect (1−c)·arch (= INV_V_002), Beurling CONDITIONAL on continuation.
  **Site (β) NO-GO.** Complement: κ count = 2 separates ζ from the panel but Epstein (h = 2) falsifies it; conductor enters as
  +(log N)‖g‖² (sign in favor, NO-GO); Tate part S(𝒵) = Σ1/(ρ(1−ρ)) > 0 for every divisor in the strip (PROVED, NO-GO).
  NUMERICAL: W*/(J²Σ|ρ|⁻²) = 1.0218 even, 1.1200 odd, jump model 2.78 ⇒ coincidence, not identity. New constraint
  C-Guo (Epstein test). Do not retry: radical/gauge/pole/Tate/conductor as a source of sign.

### 4.4 Next exact lemma
**Lemma E (Epstein test of the complement; OPEN).** Let 𝒲^Q be the Weil distribution of Epstein ζ_Q (Q = x²+5y²) in its own
explicit formula, with its summation Σ_{(m,n)} f(Q(m,n)u) and its gauge. Determine whether the analogue of L′♯ (lower bound κμ^{−A}
dist²(r_g, 𝒢̄_T)) **fails** for 𝒲^Q at some μ with an explicit vector. If it fails, any proof of L′♯ must use an
ingredient that distinguishes ζ from ζ_Q, and the only structural difference is the Euler product (Λ supported on prime
powers, i.e. −ζ′/ζ with multiplicatively generated coefficients ≥ 0); the next object is then the part of 𝒲 on the
complement of the radical where Λ(n) ≥ 0 enters quadratically (not linearly). If it does not fail, Epstein stops being a falsifier
of the L′♯ statement and the panel must be re-examined.

Script: `03-research/phase-200-sign-object/GUO_QUANT_001_data/guo_quant_test.py` (runs in ~3 min; argument = number of
zeros for the jump model).
