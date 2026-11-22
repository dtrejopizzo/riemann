# R162_803 — Round 8: a generating object for all windows at once

Labels: PROVED / PARTIAL / CITED / EQUIV / NO-GO.
**Verdict: NO-GO as a mechanism.** One new exact identity (Theorem G, PROVED); the positivity it carries
is **Lagarias's criterion** (RH ⟺ Re ξ′/ξ(u) > 0 on Re u > ½) and its domain of regularity is
**von Koch** (already G2_B7_R3 Theorem T). The first-contact structure is invisible to the object (Prop. 4).
No sign is claimed. Row D keeps no label.

## 0. Corpus check (rules )

- Dead-end map R162_590: "Kreĭn/de Branges, Li/Keiper, Nyman–Beurling, Herglotz, κ=0" are E1 (arcs II, IX);
  "every ∀T target = von Koch/KEP/κ=0/Weil" (159 G2).
- **G2_B7_R3 Theorem L/T (phase 159)**: Laplace transform in T of a *fixed-profile scalar certificate value*;
  poles of ζ′/ζ(½+s±iτ), growth exponent 2(Θ−½); EQUIV. This memo is the *operator-valued* version and must not
  re-derive Theorem T; it cites it.
- Paper 46 lem:monoT (zero-extension invariance), lem:mbounds (λ ≥ C_0 − A_{2T}).
New here: the Schur-product form of the window average, its exact factorisation, the identification of its diagonal
with Re ξ′/ξ, and the invisibility of first contact (§§2–4).

## 1. The naive generating objects are degenerate (PROVED)

**Prop 1.** For F ∈ L²(I_T) extended by zero, a_{T′}(F) = a_T(F) for all T′ ≥ T (lem:monoT: c_F vanishes on
|u| ≥ 2T, so the comb truncation n ∈ N_T is automatic). Hence {a_T} is one form a on C_c(ℝ) filtered by support,
and ∫e^{−sT}a_T(F)dT = a(F)e^{−sT_F}/s + (window-dependent nothing). A Laplace transform of the *forms* in T carries
no information beyond a itself unless the test is moved with T (dilation or truncation).

- Dilation frame U_T f: the comb term becomes Σ w_n c_f(log n/T); its Mellin transform in T is
  Σ Λ(n)n^{−1/2}(log n)^{−z}·∫c_f(u)u^{z−1}du — a series in (log n)^{−z}, **not** a Dirichlet series; no Euler
  factorisation exists. Discarded.
- Bottoms: λ_A is nonincreasing (lem:monoT), so −dλ_A = μ ≥ 0 and ∫e^{−sT}dμ is a Laplace–Stieltjes transform of a
  positive measure (Landau/Pringsheim: real singularity at the abscissa). The positivity is automatic; the content
  is the single inequality μ((T_0,∞)) ≤ λ_A(T_0) (T_0 = ½log5, R162_303), i.e. "λ_A(∞) ≥ 0" (EQUIV, Weil).
  λ_A is an infimum, so no exact computation in terms of ζ is available. Discarded.

The object that *is* exactly computable is the truncation average, §2.

## 2. The window average as a Schur product (PROVED)

Use the complete form W (eq:W). Its polar term 2Re(A(F)B̄(F)) has kernel e^{(t−t′)/2}+e^{−(t−t′)/2}, i.e. W is
(formally) convolution by one even distribution
  k_W(u) = k_∞(u) − Σ_n w_n(δ_{log n}+δ_{−log n})(u) + 2cosh(u/2),
compressed to the window. Define, for s > 0 and F ∈ C_c(ℝ),

  Φ(s)[F] := ∫_0^∞ 2e^{−2sT} W(1_{I_T}F) dT.

**Lemma 2.1.** Φ(s) = (1/s)·(W ∘ E_s), Schur (pointwise-kernel) product with
E_s(t,t′) = e^{−2s max(|t|,|t′|)} = ∫ 1_{T>|t|}1_{T>|t′|} 2s e^{−2sT}dT/s·s … precisely
∫_{max(|t|,|t′|)}^∞ 2e^{−2sT}dT = E_s(t,t′)/s. E_s is a positive mixture of rank-one projections, hence positive
definite, and E_s = M_s K_s M_s with M_s = multiplication by e^{−s|t|}, K_s(t,t′) = e^{−s||t|−|t′||} (PD).
So Φ(s) ≥ 0 ⟺ W∘K_s ≥ 0 on C_c. *Proof:* Fubini on compact support. ∎

**Theorem G (exact factorisation; PROVED for s > ½, analytic continuation below).** For exponentials
e_z(t) = e^{zt} and α = z + w̄, β = (z − w̄)/2, in the absolute-convergence region,
the translation L = log n contributes
  ∫ e^{αt} e^{zL} e^{−2s max(|t+L|,|t|)} dt = n^{β − s}·4s/(4s² − α²)
(split at t = −L/2). Summing over the whole kernel k_W:

  ⟨Φ(s)e_z, e_w⟩ = (4/(4s²−α²)) · [H(s−β) + H(s+β)],   H(u) = ∫_0^∞ k_W(L)e^{−uL}dL = ξ′/ξ(½+u) (normalised).

Indeed the comb gives Σ Λ(n)n^{−½−u} = −ζ′/ζ(½+u), the archimedean part gives ½ψ(¼+u/2) − ½log π, the polar
cosh gives 1/(u+½) + 1/(u−½); these are the four summands of ξ′/ξ(½+u). On the frequency side (z = iτ′, w = iτ):

  Φ(s)^(τ,τ′) = c · P_s(τ−τ′) · 2Re ξ′/ξ(½ + s + i(τ+τ′)/2),   P_s(x) = 4s/(4s²+x²)·(1/s),

a **product of a geometric Poisson factor in the difference frequency and a ξ′/ξ factor in the mean frequency.**
Equivalently: the mean-frequency factor is the Poisson extension to height s of the Weil symbol 𝔰 + polar,
using m(τ) = Re ψ(¼+iτ/2) − log π and v_n = 2Λ(n)/√n (exact bookkeeping: 2·½Reψ, 2·(−½log π), 2Re ζ′/ζ = −Σv_n n^{−s}cos).
The "multiplicative factorisation" requested is −ζ′/ζ = (−ζ′)·(1/ζ), i.e. Λ = μ*log, entering as the Dirichlet
series of the comb factor.

**Convergence (PROVED).** The comb factor converges absolutely iff s > ½, the polar factor iff s > ½; for
0 < s ≤ ½ both diverge and only their *sum* can converge — this is ψ(x) − x = O(x^{Θ+ε}), so the far-packet
kernel identity holds literally on s > Θ − ½ and not below (G2_B7_R3 Theorem T; von Koch). On C_c, Φ(s) itself is
defined for every s > 0 (Lemma 2.1).

## 3. The Herglotz property and its collapse (EQUIV)

**Theorem H.** (i) RH ⟹ W_T ≥ 0 ∀T ⟹ Φ(s) ≥ 0 ∀s > 0 (positive mixture; PROVED given Weil on the window class).
(ii) If Φ(s) ≥ 0 and the far-packet limit exists (s > Θ − ½), then Re ξ′/ξ(½+s+iσ) ≥ 0 for all σ (diagonal of a
continuous PD kernel: take F = M_s^{−1}g, g a wave packet at frequency σ, support → +∞, width → ∞, where
K_s(t,t′) = e^{−s|t−t′|} and W∘K_s is convolution by k_W e^{−s|u|}). PROVED for s > ½, PARTIAL for s ≤ ½.
(iii) Re ξ′/ξ(u) > 0 on Re u > ½ ⟺ RH (**Lagarias 1999**, Acta Arith. 89; CITED).
Hence "Φ(s) ≥ 0 ∀s" ⟺ RH, and the diagonal of the generating object is exactly Lagarias's Herglotz function
u ↦ ξ′/ξ(u) (Re > 0 on the half-plane = a Nevanlinna/Herglotz function after rotation). Under RH,
Re ξ′/ξ(½+s+iσ) = Σ_γ s/(s²+(σ−γ)²): the object is the Poisson-smoothed zero measure — which is also the
de Branges/Kreĭn reading already in the map (E1).

**Single s.** At a fixed s the diagonal condition only forbids quartets whose real part b = Re ρ − ½ is close to s
from above (their contribution at σ = γ is 2s/(s²−b²) → −∞ as b ↓ s); it gives no zero-free region by itself
(other zeros may compensate). Each off-line quartet contributes (1/s)·[2cosh(δ(t−t′))cos(γ_0(t−t′))]∘E_s, whose
window compressions have signature ≥ (1,1) at every T, so no s-threshold argument exists without the positive part:
unconditional positivity at large s is **not** derivable from λ_W ≥ 0 on (0,½log5] plus λ_W ≥ C_0 − A_{2T},
because tests supported at |t| > T_0 never see the small windows (Lemma 2.1: weight is 1_{T>|t|}).

## 4. First contact is invisible (PROVED)

**Prop 4.** (a) The primitive family has no Schur/generating form: 1_{I_T}F ∉ P for F ∈ P, so
∫e^{−2sT}a(1_{I_T}F)dT mixes primitive and polar directions; the primitive constraint A = B = 0 is T-independent
but truncation does not preserve it (the same obstruction as lem:contA Step 2).
(b) For a first-contact vector F (W(F) = a(F) = 0, supp F ⊂ Ī_{T_*}), Φ(s)[F] = ∫_0^{T_*}2e^{−2sT}W(1_{I_T}F)dT:
the contact itself contributes exactly 0 and the rest is the truncation history, with no sign (truncations carry
the polar term). (c) E_s has full support and strictly positive T-density, so Φ is a strictly positive average;
minimality of T_* (a statement at a boundary point of the T-axis) has no counterpart. The object fails F1 in the
sense that every step holds for λ > 0 eigenvectors as well.

## 5. Falsifiers

- F1: Theorem G/H are identities or positive averages; they hold on every eigenvector. Fails F1 as a Gate-1 tool.
- F2: Φ is linear in W; A_M → −A_M changes the comb sign in H(u) and the identity persists (for the modified ξ).
- F3: For Davenport–Heilbronn / Epstein data with functional equation, Theorem G holds verbatim with ξ_DH′/ξ_DH;
  Theorem H correctly fails for DH, **only because** ξ_DH′/ξ_DH has poles at off-line zeros. The Euler product enters
  only as −ζ′/ζ = Σ Λ n^{−s} (a symbol identity, R162_403 lesson); no positivity of the Dirichlet coefficients of
  1/ζ or of the factor (−ζ′)·(1/ζ) is available. For finite modifications a ≠ Λ, H changes by an entire Dirichlet
  polynomial and the Herglotz property fails or holds according to the zeros of the modified function — again zeros.
- F4: linear in (PC-ren)-type data; no graph limit involved, but no port vanishing either.

## 6. What survives

1. Theorem G (PROVED, s > ½; continuation below): the T-Laplace average of the windowed Weil forms is the Schur
   product W∘E_s, and in frequency it factorises as (Poisson in τ−τ′) × (2Re ξ′/ξ at ½+s+i·mean frequency).
   A clean record lemma linking Paper 46's windows to Lagarias's function; new to the corpus.
2. Theorem H: "all windows at once" = Lagarias's Herglotz criterion; the regular domain s > Θ−½ = von Koch
   (G2_B7_R3 Thm T). Both classical; EQUIV.
3. Prop 4: the generating object erases the first-contact datum; any Gate-1 use must break positivity of the
   T-average, i.e. work at a single window. Recommendation: do not pursue T-transforms further (angle closed on
   scalar (159 G2_B7) and operator levels).

Weakest step: the wave-packet diagonal limit in Theorem H(ii) for s ≤ ½ (conditionally convergent comb + polar);
the polar normalisation constant c in Theorem G should be checked once by a independent reader.
