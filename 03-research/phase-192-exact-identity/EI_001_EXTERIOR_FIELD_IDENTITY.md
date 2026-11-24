# EI_001 — The exterior field of the window minimizer: an exact three-term identity, and what it does to C*_A

Construction round (phase 192). Pen and paper; no numerics.
P46 = 04-papers/46-row-d-sign-radial-intersection-form/main.tex. SPEC_A = phase-191/SPEC_A_EXACT_INDUCTION.md.
**No sign is certified here; no negative value of 𝔞_T for ζ is found or claimed.**

## 0. Corpus check — why this is not a retry
grep over ROUTES-TRIED-INDEX (README, 03_, 04_, 06_), phase-186/188/190/191: "exterior field" appears only in 04_ line 888 (R163_1001 angle (C):
window Hamburger theorem *against* the exterior field — NO-GO/REF-D: the exterior samples are free, Thm C.3) and in SPEC_A §3–5 (C*_A stated,
no identity written). R186_048 Lemma 3.2 bounds the visibility of an atom through the collar (an estimate, W-cont). L2_BUILD_008 §4 writes the
prime pairing of the *clamped ground mode* as (¼−∂²)² acting on dψ̃ with the main term annihilated. Nobody has written the exterior field of the
*minimizer* as a closed identity in which the polar main term, the Chebyshev fluctuation and the archimedean tail are separated exactly, nor
the Fourier-side identity Ê = (σ_T − λ)ĥ* − Tate with its pole structure. Not a retry: the object is the one SPEC_A §5 named as the only line
where an input could enter ("the evaluation of the exterior field g*_j = 𝒯_jh*_j on the collars"), and it had not been evaluated.

## 1. Setting (P46)
I_T = (−T,T), X := e^{2T}, v_n = 2Λ(n)n^{−½}, 𝒩_T = {n ≥ 2 : n < X}; m(τ) = Re ψ(¼+iτ/2) − log π = C₀ + ∫₀^∞(1−cos τu)K(u)du with
K(u) = 2e^{−u/2} + K₁(u), K₁(u) := 2Σ_{k≥1}e^{−(2k+½)u} (lem:K); σ_T(τ) = m(τ) − Σ_{n∈𝒩_T}v_n cos(τ log n); 𝔞_T(F) = (1/2π)∫σ_T|F̂|², F̂(τ) = ∫F(t)e^{itτ}dt;
A(F) = ∫Fe^{t/2}, B(F) = ∫Fe^{−t/2}, P_T = {A = B = 0}; 𝒟_T the form domain; h* a real unit minimizer of 𝔞_T on P_T ∩ 𝒟_T (exists, lem:compact);
λ := λ_A(T) = 𝔞_T(h*). All functions on I_T are extended by zero to ℝ. For t ∈ ℝ define the (compressed-to-nothing) field
  (σ_T(D)h*)(t) := C₀h*(t) + ∫₀^∞K(u)[h*(t) − ½h*(t−u) − ½h*(t+u)]du − ½Σ_{n∈𝒩_T}v_n[h*(t−log n) + h*(t+log n)],
whose Fourier transform is σ_T(τ)ĥ*(τ) (tempered distribution; σ_T has logarithmic growth and ∫log(2+|τ|)|ĥ*|² < ∞ since h* ∈ 𝒟_T).

**Lemma 1 (Euler–Lagrange with Tate multipliers; PROVED, routine).** There are β₀, β₁ ∈ ℝ such that, as distributions on I_T,
  σ_T(D)h* = λh* + β₀e^{t/2} + β₁e^{−t/2}.
*Proof.* h* minimizes the Rayleigh quotient of the closed semibounded form 𝔞_T on P_T ∩ 𝒟_T (lem:compact), so 𝔞_T(h*,G) = λ⟨h*,G⟩ for every
G ∈ P_T ∩ 𝒟_T. The functional G ↦ 𝔞_T(h*,G) − λ⟨h*,G⟩ on 𝒟_T is continuous in the form norm and vanishes on P_T ∩ 𝒟_T = ker A ∩ ker B ∩ 𝒟_T, which has
codimension exactly 2 in 𝒟_T (A, B are bounded on L², linearly independent, and 𝒟_T is dense); hence it equals β₀A(G) + β₁B(G). Since
𝔞_T(h*,G) = ⟨σ_T(D)h*, G⟩ for G ∈ C_c^∞(I_T), this is the displayed identity. ∎

**Definition (exterior field).** E(t) := (σ_T(D)h*)(t) for |t| > T, E := 0 on I_T. (SPEC_A's 𝒯_jh*_j is −E restricted to the collars, up to the
sign convention; here the sign is the one of the operator.) For |t| > T the local terms vanish and
  E(t) = −½∫_{I_T}K(|t−s|)h*(s)ds − ½Σ_{n∈𝒩_T}v_n[h*(t−log n) + h*(t+log n)].                                                  (1.1)

## 2. Theorem 1 — the exterior field is (polar edge moment) − (Chebyshev fluctuation at the scale e^{|t|}) − (archimedean tail)

Put H̃(x) := x^{½}h*(log x) for x > 0 (supported in (e^{−T}, e^T)). For t > T:
  **E(t) = e^{t/2}∫_{−T}^{t−2T}h*(s)e^{−s/2}ds − e^{−t/2}∫_{[1,X)}H̃(e^t/u) d(ψ(u) − u) − ½∫_{I_T}K₁(t−s)h*(s)ds,**                    (2.1)
with the convention ∫_{−T}^{a} = 0 for a < −T (so the first term starts at t = T and is identically 0 for t ≥ 3T), and the symmetric
formula for t < −T (replace h*(s) by h*(−s)). **PROVED.**

*Proof.* In (1.1), for t > T the terms h*(t+log n) vanish (t + log n > T). Archimedean part: K = 2e^{−u/2} + K₁ and
½∫2e^{−(t−s)/2}h*(s)ds = e^{−t/2}A(h*) = 0 by the Tate condition; the K₁ part is the third term. Comb part:
−Σ_{n<X}Λ(n)n^{−½}h*(t − log n) = −∫_{[1,X)}u^{−½}h*(t − log u)dψ(u) = −∫_{[1,X)}u^{−½}h*(t−log u)d(ψ(u)−u) − ∫₁^X u^{−½}h*(t−log u)du.
In the first integral u^{−½}h*(t−log u) = e^{−t/2}(e^t/u)^{½}h*(log(e^t/u)) = e^{−t/2}H̃(e^t/u). In the second, u = e^r:
∫₀^{2T}e^{r/2}h*(t−r)dr = e^{t/2}∫_{t−2T}^{t}e^{−s/2}h*(s)ds = e^{t/2}∫_{t−2T}^{T}e^{−s/2}h*(s)ds = e^{t/2}[B(h*) − ∫_{−T}^{t−2T}e^{−s/2}h*] = −e^{t/2}∫_{−T}^{t−2T}h*e^{−s/2},
using B(h*) = 0 (and h* = 0 outside I_T). Collecting signs gives (2.1). For t ≥ 3T all three prime-side pieces vanish identically
(t − log u > T for u < X) and the first term is e^{t/2}B(h*) = 0. ∎

**Reading of the three terms (PROVED facts, not estimates).**
(a) *Polar edge moment* p(t) := e^{t/2}∫_{−T}^{t−2T}h*(s)e^{−s/2}ds, T < t < 3T. It is the exterior field that the **main-term comb**
    ρ₁ = e^{u/2}du (density κ = 1, truncated at X) produces; p(T⁺) = 0 and p(3T) = e^{3T/2}B(h*) = 0: a bump supported on (T,3T) whose value
    at t = T + ε is e^{T/2}× the Tate moment of h* on the **opposite** collar [−T, −T+ε]. This is the polar/contact coupling of SPEC_A §2(d)
    written out: the right collar sees the left collar through the pole of ζ, at lag 2T.
(b) *Chebyshev term* q(t) := e^{−t/2}∫_{[1,X)}H̃(e^t/u)d(ψ(u)−u): the fluctuation of ψ − u on the multiplicative window
    u ∈ (e^{t−T}, min(X, e^{t+T})), tested against the minimizer read backwards (H̃(e^t/u)), truncated at the window edge X. For t = T + ε the
    test covers all scales u ∈ (e^ε, X): the whole window comb; the truncation at X cuts the test support, which is why (a) is not zero.
(c) *Archimedean tail* r(t) := ½∫K₁(t−s)h*(s)ds = Σ_{k≥1}e^{−(2k+½)t}μ_k⁺, μ_k⁺ := ∫h*(s)e^{(2k+½)s}ds: a finite-type exponential sum with
    exponents 5/2, 9/2, …, with no Tate cancellation (the k = 0 term is the one Tate killed).
So E = p − q − r exactly. The density ceiling (thm:ceiling, thm:kappa: κ = 1 < κ⋆) says that p alone never pays; B2d is visible in the identity.

## 3. Theorem 2 — Fourier side: Ê = (σ_T − λ)ĥ* − Tate, the symbol is the boundary value of the Euler tail, and no zero appears

Let R_X(s) := −ζ'/ζ(s) − P_X(s), P_X(s) := Σ_{n<X}Λ(n)n^{−s} (so R_X(s) = Σ_{n≥X}Λ(n)n^{−s} for Re s > 1, meromorphic on ℂ).
(i) **PROVED.** As functions on ℝ, Ê(τ) = (σ_T(τ) − λ)ĥ*(τ) − β₀ê₊(τ) − β₁ê₋(τ), e_± := e^{±t/2}𝟙_{I_T}.
(ii) **PROVED (CITED: FE of ζ, prop:boundary).** σ_T is the restriction to ℝ of the meromorphic function
      Σ(τ) := R_X(½+iτ) + R_X(½−iτ) = ½[ψ(¼+iτ/2) + ψ(¼−iτ/2)] − log π − P_X(½+iτ) − P_X(½−iτ),
    whose only poles are at τ = ±i(2k+½), k ≥ 0 (simple). **The zeros of ζ do not appear**: the poles of −ζ'/ζ(½+iτ) and of −ζ'/ζ(½−iτ) at an
    off-line zero cancel pairwise, because ζ'/ζ(s) + ζ'/ζ(1−s) = log π − ½ψ(s/2) − ½ψ((1−s)/2) exactly (logarithmic derivative of ξ(s) = ξ(1−s)).
    Equivalently σ_T(τ) = 2Θ_X'(τ) with Θ_X(τ) := θ(τ) − Σ_{n<X}Λ(n)n^{−½}sin(τ log n)/log n, θ the Riemann–Siegel theta (θ' = ½m; see EI_003).
(iii) **PROVED.** Ê is holomorphic in |Im τ| < 5/2 (E = p − q − r with p, q compactly supported in T < |t| < 3T and r = O(e^{−5|t|/2}));
    the poles of Σ at ±i/2 are removed by the Tate zeros ĥ*(±i/2) = 0; the first singularities of Ê are simple poles at τ = ∓5i/2 with residues
    proportional to μ₁^± = ∫h*(s)e^{±5s/2}ds, matching Res_{τ=∓5i/2}Σ·ĥ*(∓5i/2). The identity (i) is therefore consistent pole by pole and
    contains no information beyond (Λ(n))_{n<X}, m, λ, β₀, β₁ — prop:finite(iv).

*Proof.* (i) Fourier transform of Lemma 1 extended by E. (ii) prop:boundary gives m(τ) = −2Re ζ'/ζ(½+iτ) off the ordinates; the displayed
meromorphic identity is the FE differentiated; on ℝ both sides are continuous (at a critical-line zero the two simple poles have opposite
residues ∓im_ρ and cancel; at an off-line zero ρ the pole of ζ'/ζ(s) at s = ρ and the pole of ζ'/ζ(1−s) at s = ρ cancel in the sum, as the
right side has no pole there). Σ − P-terms = ½[ψ(¼+iτ/2) + ψ(¼−iτ/2)] − log π has poles at ¼ ± iτ/2 ∈ −ℕ₀, i.e. τ = ±i(2k+½). (iii) is the
support/decay of (2.1) and the Laplace transform of e^{−5t/2}𝟙_{t>3T}. ∎

**Corollary (answer to SPEC_A's question (i)).** "Is 𝒯h* determined by an exact functional equation of ζ applied to the Dirichlet polynomial of
h*?" — Yes and trivially: the only functional equation of ζ that acts is m = −2Re ζ'/ζ = 2θ' on the line, which identifies the boundary value
of the infinite Euler tail with the Γ-factor and is already inside σ_T. By prop:finite(iv) and R163_1001 Thm C.3 (exterior samples are free),
no further relation exists: the exterior field is the inverse transform of the **Euler tail beyond the window**, R_X(½+iτ) + R_X(½−iτ), times
ĥ*, minus the Tate exponentials. **PROVED (by the record).**

## 4. Where the sign of C*_A sits in the identity
SPEC_A's residual conjecture C*_A needs, for every collar function G (supported in T < |t| < T + ε, after the Tate correction),
|⟨G, E⟩|² ≤ μ_j(edge energy of G − ν_j‖G‖²)-type control (rank-one necessary form, SPEC_A §3). By (2.1),
  ⟨G, E⟩ = ⟨G, p⟩ − ⟨G, q⟩ − ⟨G, r⟩,
with ⟨G,p⟩ = ∫_{T}^{T+ε}G(t)e^{t/2}∫_{−T}^{t−2T}h*e^{−s/2}ds dt (the two collars coupled through the pole; a bounded explicit bilinear form in
(G, h*|_{left collar}), of size ‖G‖·‖h*‖_{L¹(left collar)}e^{T/2}·e^{−T}), ⟨G,r⟩ explicit and exponentially small in T (e^{−5T/2}·μ₁⁺-type, up to
the collar width), and
  ⟨G, q⟩ = ∫_{[1,X)} [∫_{T}^{T+ε}G(t)e^{−t/2}H̃(e^t/u)dt] d(ψ(u) − u)  — a **twisted Chebyshev sum over the whole window, tested by the product of the
  collar function with the minimizer**.
The margin that C*_A must deliver is ν_j ≍ λ_A(T_{j+1}) (SPEC_A Lemma S(iv)); the three terms are each exact. Two ways to decide the sign:
(α) bound ⟨G,q⟩ — any such bound is an estimate on primes with a remainder (MUST-NOT 1), of strength exp(−cT) at best against a margin
exp(−e^{2T}) (SPEC_A (γ)); (β) keep ⟨G,q⟩ exact — then C*_A is the Schur complement identity of Lemma S, i.e. the target at T_{j+1} given the
target at T_j (R186_029 Lemma H(ii), REF-D). The identity (2.1) does not open a third way: it is linear in Λ at fixed h*, and the only
non-linearity in Λ is the dependence of h* on Λ through the resolvent (the "functional of h*, not of σ" of phases 183–186).

**What the identity does prove (new, PROVED).** (P1) The exterior field of ζ's minimizer at a window is the exterior field of the density-1
main-term comb (truncated at X), minus the Chebyshev fluctuation at the scale of the collar tested by the minimizer, minus an archimedean
tail of exponent 5/2; the Tate conditions annihilate exactly the e^{−|t|/2} archimedean term and the full-range polar term, and nothing else.
(P2) Across the window edge, the polar coupling is the partial Tate moment of the *opposite* collar; the first atom to couple the two collars
at the same lag 2T is n_j with log n_j ≈ 2T (through q, in the term u ≈ e^{2T}); the archimedean coupling at that lag is K₁(2T) = O(e^{−5T}),
not 2e^{−T} (the latter is Tate-killed) — this corrects SPEC_A §2(d), which paired v_{n_j} with the polar coupling 2n_j^{−½}: in the exterior
field of a *primitive* h* the polar partner of the atom n_j is p(t), i.e. the opposite-collar Tate moment, not 2n_j^{−½}.
(P3) Ê is holomorphic in |Im τ| < 5/2; the zeros of ζ are invisible in the exterior-field identity (Theorem 2(ii)).

## 5. Review (self)
1. Lemma 1 needs 𝔞_T(h*,G) = ⟨σ_T(D)h*,G⟩ for test functions G: true as distributions since σ_Tĥ* is tempered and Ĝ Schwartz. The multiplier
   argument needs P_T ∩ 𝒟_T of codimension exactly 2 in 𝒟_T: A, B restricted to 𝒟_T are independent since 𝒟_T ⊃ C_c^∞(I_T) and e^{t/2}, e^{−t/2}
   are independent on I_T. ✓
2. (2.1): the Stieltjes integral against d(ψ − u) with the integrand e^{−t/2}H̃(e^t/u): H̃ is as regular as h* (form domain, so at least L²
   with log-weighted transform); the Stieltjes integral is a finite sum minus a Riemann integral; no regularity issue. The boundary u = 1:
   H̃(e^t) = e^{t/2}h*(t) = 0 for t > T. ✓ Signs re-derived twice. ✓
3. Theorem 2(ii): the cancellation of the off-line-zero poles is the FE; this is NOT a statement about zeros being on the line and uses no
   zero information: it says the symbol never sees zeros, which is prop:finite(iv) in meromorphic dress. ✓ Nothing zero-side is used anywhere.
4. Theorem 2(iii) pole matching: Res_{τ=−5i/2} of ½ψ(¼+iτ/2) = ½·(residue of ψ at −1 is −1)·(dτ/dz = 2/i) → −i; times ĥ*(−5i/2) = μ₁⁺; on the
   E side, ∫_{3T}^∞e^{−5t/2}e^{itτ}dt·(−μ₁⁺) = −μ₁⁺e^{3T(iτ−5/2)}/(5/2 − iτ) has residue at τ = −5i/2 equal to −μ₁⁺e^{…}/(−i) = −iμ₁⁺e^{0}… the
   constants agree up to the entire part contributed by (T,3T); consistency is as stated, not a new relation. ✓ (ARGUED for the constant; the
   structural claim — first singularity at Im τ = ±5/2 unless μ₁^± = 0 — is PROVED.)
5. P2 "corrects SPEC_A": SPEC_A's pairing v_{n_j} ↔ 2n_j^{−½} was for the kernel K acting on the frozen-window function x, where x is
   primitive on I_{T_j}: there too ∫2e^{−(t−s)/2}x(s)ds = 2e^{−t/2}A(x) = 0, so the polar archimedean partner is absent for the same reason. The
   correction stands. ✓
6. Non-linearity: the identity is affine in the weights v at fixed h*; ∂_{v_n}λ = −c_{h*}(log n) (lem:degen) is its first variation. No
   non-linear use of Λ is made. ✗ (recorded in §6).
7. No numerics; no estimate used; no sign claimed. ✓

## 6. Compliance table (mandate + Thm 20.28 / Problem (R))
| clause | status | note |
|---|---|---|
| MUST-NOT: estimate on primes with remainder | ✓ avoided | (2.1) is exact; q is kept as a Stieltjes integral |
| MUST-NOT: invariant under O1–O15 | ✓/✗ | identity holds verbatim for every comb (O1–O5, O7, O11, O15): it is *invariant as an identity*; only its value changes. As a mechanism it carries no ζ-specific property |
| MUST-NOT: class argument / functional of symbol statistics / shift-multiplier calculus | ✓ | the identity is not in prop:opcalc's class (it is a statement about the exterior of the window, not a measure identity on (−2T,2T)); but any *use* of it to bound ⟨G,q⟩ falls into B4/B6 |
| MUST-NOT: dual/lattice/SOS certificate; zero information; σ-transport; perturbative induction; REF-D restatement | ✓ for the identity; ✗ for its sign content | the sign content is C*_A = Lemma S = Schur = REF-D (SPEC_A §6) |
| MUST: exact identity on h*_T | ✓ | Theorems 1–2 |
| MUST: full vector (Λ(n))_{n<X} enters non-linearly | ✗ | enters linearly (through dψ on [1,X)); non-linear only via h* = h*(Λ) |
| MUST: Euler × FE(q=1) × ℤ jointly as mechanism | ✗ | Euler: linearly (ψ); FE: only as m = 2θ' (Theorem 2(ii)); ℤ: not used (any positive measure dψ gives (2.1)) |
| MUST: doubly-exponential margin from the identity | ✗ | no margin is produced; the identity relocates it into ⟨G,q⟩ |
| MUST: wins by fluctuation, Λ at the ceiling r = 1 < κ⋆ | ✓ (structure) | p is the density-1 field and cannot pay (thm:kappa); the fluctuation q is the carrier — exhibited, not decided |
| MUST: sensitive to 10⁻⁵ weight changes | ✓ (inherited) | through h* and λ (prop:wit-sens) |
| MUST: names what separates ζ from ζ_K | ✗ | nothing in (2.1) is field-specific; for ζ_K the same identity holds with ψ_K and Γ_K |
| (R)(1) exact values at every T | ✓ | |
| (R)(2) Euler + FE jointly | ✗ | FE enters only through m |
| (R)(3) non-linear in Λ | ✗ | |
| (R)(4) no zeros | ✓ | Theorem 2(ii) |
| (R)(5)–(8) | ✓ formally (no bounded functional; all frequencies; exact at centre/resolution) | the identity decides nothing, so (6)'s precision is not tested |
| (R)(9), (10) | ✓ / ✗ | not a D_σ symmetrization; no property beyond A1–A6 is named |

## 7. Column bookkeeping (what had to be given up)
To keep **exact identity** and **no estimate**, the following moved from the MUST (yes) column to the NO column for this object:
- "Λ enters non-linearly" → NO: at fixed h* the exterior field is linear in Λ; the only non-linearity is h*(Λ) (resolvent), which is the
  REF-D channel (Lemma S). 
- "ℤ-integrality as mechanism" → NO: (2.1) uses Λ only as a positive measure dψ on [1,X); O11 (Beurling) leaves the identity unchanged.
- "doubly-exponential margin out of the identity" → NO: the margin is relocated into the twisted sum ⟨G,q⟩ and not produced.
- "names ζ vs ζ_K" → NO.
Kept in the YES column: exact; no remainder; no zeros; no class; no certificate; fluctuation (not density) is the carrier; sensitivity inherited.
Status of C*_A after EI_001: unchanged (OPEN, REF-D as content); the object of SPEC_A §5 is now explicit: ⟨G,q⟩ = whole-window twisted
Chebyshev sum tested by (collar function × minimizer), to be controlled at precision ≍ λ_A(T_{j+1}).
