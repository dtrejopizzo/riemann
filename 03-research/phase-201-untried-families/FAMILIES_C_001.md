# FAMILIES_C_001 — Inventory C (phase 201): infinite-dimensional nonlinear invariants of the test, with S7 and S8 by construction

CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. This memo retries nothing from the ROUTES-TRIED index without
a written reason. P47 notation (def:W/def:PD/eq:nuw), as in SPEC_201 §C.1: g = f∗f̃ ∈ P_T, f ∈ C_c^∞[−T,T],
v_n^X = 2X(n)/√n, 𝒲_T^X = truncation to L²(I_T) of the single symbol
θ_T^X(s) = m(s) − Σ_{n ≤ N_T} v_n^X cos(s log n) (R186_004, PROVED), 𝔞_T^X(f) = ⟨f, 𝒲_T^X f⟩.
Falsifiers: Epstein 11, DH 12, a_P, cΛ, Beurling.

## Summary (≤300 words)

14 families with a nonlinear invariant in the test (S7) and infinite structure from the window (S8) were
inventoried: bound-state counting, Lieb–Thirring/Bargmann/Calogero, Sturm oscillation, Faddeev–Zakharov
trace identities, Gelfand–Levitan/Marchenko, KdV/Toda, nonlinear Fourier transform, Ruelle–Bowen pressure,
Gibbs/KMS, Hamilton–Jacobi viscosity, renormalization, Monge–Ampère/Brenier, Berezin–Li–Yau for the
truncated symbol, and Thouless/logarithmic energy. Results:

- **Lemma S-0 (PROVED).** If the potential V_F is 2-homogeneous in F, then "−∂² + V_{tF} ≥ 0 for all t" is
  equivalent to V_F ≥ 0 almost everywhere. Bound-state counting adds nothing to the pointwise positivity of a
  density.
- **Lemma S-1 (CITED, Simon 1976).** In weak coupling, N(tV_F) → 1{∫V_F ≤ 0}. The count is exactly the sign
  of a linear functional (branch 5).
- **Trace identity I1 (CITED, verified with δ):** −∫V = 4Σκ_j − (1/π)∫log(1/(1−|R|²))dk. The ≥ 0 term enters
  with the wrong sign for any choice ∫V_F = ±𝔞_T. What remains is "H_F has no bound states", which is
  SUSY/Riccati (index #96, NOT VIRGIN).
- **Lemma L-loc (PROVED).** Every local-density invariant has a second variation that does not see the
  log n atoms. This kills Hamilton–Jacobi, Monge–Ampère, and Schrödinger with a local potential.
- **Lemma P-fin (PROVED).** The pressure on the shift of primes with F of compact support is an analytic
  function of finitely many values F(log n): it does not satisfy S7(ii) and falls under Thm 3′.
- **Lemma C-pos (PROVED in the identity version).** An invariant with intrinsic positivity for every comb
  cannot equal 𝔞_T^X, because 𝔞^{Epstein} < 0. The Λ channel can only enter through a hypothesis of the
  positivity theorem, and those hypotheses are always operator positivities (branch 2).

Verdict: **0 viable families.** None remains as "virgin and viable". The ranking retains two finite and
cheap falsification lemmas (Berezin–Li–Yau bathtub on θ_T; second-order Neumann–Schrödinger) and one closure
lemma (general Lemma C-pos). I do not recommend launching any as a long construction.

---

## 0. Method

1. Grep of the index `05-meta-and-planning/ROUTES-TRIED-INDEX/` (all files) with the requested terms. Count
   of lines with real hits:
   - Schrödinger: 1 (L17 Lagarias, reformulation).
   - Terms with no hits: "bound states", Bargmann, "inverse scattering", Marchenko, KdV, "nonlinear
     Fourier", Monge, "free energy", "fixed point", viscosity, Ruelle, Bowen, Kolmogorov, Calogero, Jost,
     Brenier, Berezin, Li–Yau, Frostman, Thouless, Voiculescu, Avila.
   - Lieb: 3, all Brascamp–Lieb or Lieb flux, none Lieb–Thirring.
   - scattering: 12 (L59, L89 Faddeev–Pavlov NO-GO ARGUED, D6 causality, G8A-118/W3, R161_011-021).
   - Gelfand: 2 (R186 TB-1).
   - Gibbs/KMS: 3/5 (AUDIT_193 rows 12 and 15, L29).
   - renormaliz: 8 (G3F-102/167/170/171, R161, GG).
   - Perron: 12.
   - Mayer: 5 (CA_A_002 Lewis–Zagier NO-GO ARGUED; P152).
   - Lyapunov: 2 (dBN heat flow, R166_201E).
   - Sturm: 8 (DEAD G8D-155, R160_S4).
   - SUSY/Riccati: #96.
   - Bochner: 21.
   - Szegő: W-det.
   - "Toda": only false positives ("todas" [Spanish "all"]).
2. Corpus: FAMILIES_B F6, F7 and F9 (NOT VIRGIN), R186_000/004 (TB-1), CS0_COMMUTE_001, AUDIT_200_DCONS
   (Thm 3′), V1_1_NONNEG, V2_RECURRENCE (Thm V2-0, S7, S8), MAP_200 §2 (Φ200, C-emb).
3. Web: search "Weil positivity / explicit formula / Riemann zeta" combined with each family. Sources are in
   §7.
4. For each family, points (a)–(g) are given:
   - (a) positivity theorem;
   - (b) index;
   - (c) web;
   - (d) exact instantiation in the window: V or F, where v_n enters, Λ channel;
   - (e) filters S1–S8, Φ200 branches, Thm 3′, C-emb, G1;
   - (f) verdict;
   - (g) what would enter the index.

## 1. Four transversal lemmas (used throughout the inventory)

**Lemma L-loc (PROVED).** Let 𝒥(f) = ∫_{I_T} Φ(x, f(x), f′(x), …, f^{(k)}(x)) dx with Φ of class C², or any
functional whose second variation at 0 is a local differential quadratic form
Q(f) = Σ ∫ a_{ij}(x) f^{(i)} f̄^{(j)}. Then there is no c ≠ 0 such that Q = c·𝔞_T^X on P_T, for any T > ½log 2
and any comb with v_2^X ≠ 0.

*Proof.* Take f₁ and f₂ with disjoint supports at positive distance within I_T, both with zero moments
A = B = 0 (finite codimension, so they can be chosen). Also require f₂ to be a log-2 translate of a multiple
of f₁, restricted so that ∫ f₁(x) f̄₂(x + log 2) dx ≠ 0. By locality, Q(f₁ + f₂) − Q(f₁) − Q(f₂) = 0. The
cross term of 𝔞_T^X contains −v_2^X · 2Re ∫ f₁(x) f̄₂(x + log 2) dx. This term does not cancel against the
archimedean part, because K_∞ is smooth at log 2 and the fine separation of f₁, f₂ can be scaled so that
K_∞'s contribution is o(1) relative to the atom. Concretely, replace f₂ by f₂ modulated by e^{iξx} with
ξ → ∞: the atom gives −v_2^X · e^{iξ log 2}·c, and the smooth part decays by Riemann–Lebesgue. Hence the
cross term is nonzero. ∎

Consequence: every family whose invariant is an integral of a local density in the test (local
Hamilton–Jacobi, Monge–Ampère in the potential, Schrödinger with pointwise V_F = Φ(F), Fisher/entropy of F)
is ruled out for representing 𝔞_T, and also for bounding it in either direction. S8 is violated in the
strongest form: the window enters, but the log n shifts do not.

**Lemma C-pos (PROVED in the identity version; ARGUED in the inequality version).**
- (i) Let Ψ(f, X) ≥ 0 for every test f and every comb X of the battery, via an intrinsic positivity theorem
  (whose hypothesis does not depend on X). Then there is no identity 𝔞_T^X(f) = Ψ(f, X) valid for all X in
  the battery. *Proof:* 𝔞_T^{Ep}(f) < 0 for some (T, f) (Epstein 11 battery, CITED in P47/AUDIT_200_EPSTEIN).
  ∎
- (ii) In the inequality version, "𝔞_T^X ≥ Ψ − E(X)", the Λ channel enters through the error E. E is either
  linear in the comb (branch 1) or an operator positivity on the window (branch 2).

Moral: a family's intrinsic positivity is useful only if the Λ channel enters **in the hypothesis** of the
theorem (e.g. "no bound states", "reflectionless potential", "positive spectral measure"). The hypotheses of
the classical theorems in this class are operator positivities.

**Lemma S-0 (PROVED).** Let F ↦ V_F ∈ C(I_T) with V_{tF} = t^α V_F, α > 0. Let H_F = −∂² + V_F on I_T, with
Dirichlet or Neumann condition, or on ℝ if V_F is extended by 0. Then:
(H_{tF} ≥ 0 for all t > 0) ⟺ V_F ≥ 0 almost everywhere.

*Proof.*
- (⇐) Immediate.
- (⇒) If V_F < −δ on an interval J of length ℓ, take ψ = sin(π(x − x₀)/ℓ) on J. Then
  ⟨ψ, H_{tF}ψ⟩ ≤ (π²/ℓ² − t^α δ)‖ψ‖² < 0 for large t. ∎

Since P_T is a cone, tF ∈ P_T. Any "bound-state count = 0 for all F ∈ P_T" with a homogeneous potential then
reduces to the pointwise positivity of a density of 𝔞 (∫V_F = 𝔞, V_F ≥ 0). That is an SOS/local decomposition
of the form: branch 2. It is also false for any local density, by L-loc.

**Lemma S-1 (CITED: B. Simon, Ann. Phys. 97 (1976) 279–288).** Let V ∈ L¹((1+x²)dx) on ℝ, V ≢ 0. As λ → 0⁺,
−∂² + λV has a bound state if and only if ∫V ≤ 0. In that case
√(−E(λ)) = −(λ/2)∫V − (λ²/4)∬V(x)|x−y|V(y) + O(λ³).

Corollary (PROVED from the CITED fact): lim_{λ→0} N(λV_F) = 1{∫V_F ≤ 0}. If ∫V_F = 𝔞_T(F), the weak-coupling
count **is** the sign (branch 5, tautology). The second-order term −∬V|x−y|V is ≥ 0 when ∫V = 0, because |x|
is conditionally negative definite. But the kernel |x−y| is fixed and independent of the comb, so it falls
into branch 1.

## 2. Family by family

### C1. Bound-state count N(V) of −∂² + V_{F,Λ} in the window; Bargmann, Calogero, Lieb–Thirring

- (a) CITED theorems:
  - Bargmann: N ≤ ∫|x||V₋|.
  - Calogero: N ≤ (2/π)∫√V₋ for monotone V.
  - Lieb–Thirring 1D, γ = 3/2 optimal: Σ|E_j|^{3/2} ≤ (3/16)∫V₋².
  - Sturm: N = number of zeros of the zero-energy solution.
- (b) Index: 0 hits for bound states, Bargmann, Calogero and Lieb–Thirring. Birman–Schwinger is in R186-D_B
  (INV_D_001, discarded). Sturm/nodal is DEAD (G8D-155, R160_S4) and CS0_COMMUTE (NO-GO PROVED). It is
  **virgin as a bound-state count**, but adjoins Birman–Schwinger.
- (c) Web: no use for Weil positivity. There are Hamiltonians with spectrum at the zeros (Wu–Sprung 1993,
  PRE 48, 2595; Sierra 1404.4252), all on the zero side.
- (d) Possible instantiations:
  - (d1) V = −c_F weighted by the comb: V_F(x) = −Σ_n v_n (f∗f̃)(x − log n). It is linear in g, so S7(i)
    fails except via N. By S-0 (α = 1), "N = 0 for all F" ⟺ V_F ≥ 0 ⟺ Σ v_n g(x − log n) ≤ 0 everywhere.
    This is false: g(0) = ‖f‖² > 0 and n = 1 has v_1 = 0, but at x = log n the term v_n g(0) > 0 dominates.
    Dies.
  - (d2) V_F = f̄·(𝒲_T f) (non-local density, ∫V_F = 𝔞_T). It is 2-homogeneous and S-0 reduces it to
    f̄·𝒲_T f ≥ 0 pointwise. This is false for almost every f, because 𝒲_T f changes sign where f does not.
  - (d3) Normalized potential V̂_F = V_F/‖f‖², with fixed coupling c:
    - as c → 0 (S-1), N = 1{𝔞 ≤ 0}: branch 5;
    - as c → ∞ (Weyl, N ~ (√c/π)∫√(V̂₋)), it only counts the pointwise negative part: local in V̂, blind to
      the cancellation that decides 𝔞;
    - at intermediate c, N is an integer and locally constant in F outside a hypersurface (zero-energy
      resonance thresholds). By Thm 3′ it cannot equal 𝔞 nor be a continuous function of it; it can only give
      "N = 0 ⇒ 𝔞 > 0" (Simon/Neumann, see C2), and N = 0 is an operator positivity (branch 2).
  - Channel: v_n^X enters linearly in V. The change Λ → Epstein changes V, and the Bargmann, Calogero and
    Lieb–Thirring inequalities hold for every V. Generic-comb (branch 1) except in the hypothesis N = 0.
- (e) S7: (i) ✓, (ii) ✓, (iii) ✗ (S-1: the first order is linear). S8 ✓ in (d2) and ✗ in local densities
  (L-loc). Branches: 5 (weak), 1 (bounds), 2 (hypothesis N = 0). Thm 3′ applies to N.
- (f) **VIRGIN-DEAD: NO-GO PROVED** for homogeneous potentials (S-0) and in weak coupling (S-1). **ARGUED**
  at intermediate c (Thm 3′ + branch 2).
- (g) Index: "C1 bound-state count/Bargmann/Calogero/Lieb–Thirring with V_F: NO-GO. S-0 (homogeneous ⇒
  pointwise positivity), S-1 Simon (weak = sign of ∫V, branch 5), Thm 3′ at intermediate c".

### C2. Faddeev–Zakharov trace identities / scattering of −∂² + V (requested detailed treatment)

- (a) CITED identities (Faddeev–Zakharov 1971, Funct. Anal. Appl. 5; Deift–Trubowitz CPAM 1979), with
  V ∈ L¹((1+|x|)), κ_j = √(−E_j), R the reflection coefficient and ϱ(k) := log(1/(1−|R(k)|²)) ≥ 0:

  **(I1)**  −∫V dx = 4 Σ_j κ_j − (1/π) ∫_ℝ ϱ(k) dk,

  **(I3)**  ∫V² dx = (16/3) Σ_j κ_j³ + (4/π) ∫_ℝ k² ϱ(k) dk.

  Verification of I1 with V = αδ, from which I obtained the sign and constant (PROVED, own computation):
  - T(k) = 2ik/(2ik − α) and 1 − |R|² = |T|² = 4k²/(4k² + α²).
  - ∫_ℝ log(1 + α²/4k²) dk = π|α|.
  - Case α = −c < 0: κ = c/2, and the right side equals 2c − c = c = −∫V ✓.
  - Case α > 0: no bound states, the right side equals −α ✓.

  I3's constant 4/π comes from the Born limit, |R|² ≈ |V̂(2k)|²/4k² (ARGUED; the constant matches
  Lieb–Thirring's 3/16, CITED). The Lieb–Thirring inequality with γ = 3/2 is exactly I3 without the ϱ ≥ 0
  term, and equality holds only for reflectionless potentials.

- (b) Index:
  - Faddeev–Pavlov/Lax–Phillips is L89 (NO-GO ARGUED, a different object: wave group on Γ\H).
  - R186_008 states that the scattering phase φ_S of U = F_∞⁻¹F_S has derivative equal to the prime comb,
    with an exact trace identity (PROVED, no sign).
  - TB-1 (R186_000, R186_004) asks for the global existence of Gelfand–Levitan/Kreĭn with arithmetic data.
  - **Schrödinger trace identities (I1, I3) with V built from the test: 0 hits. Virgin as an identity.**

- (c) Web. Wu–Sprung (PRE 48, 2595, 1993) build a 1D potential whose WKB spectrum reproduces ~500 zeros. The
  input data is the smoothed counting function of the zeros, and the resulting potential is fractal.
  hep-th/0111067 (Khuri 2001, "Inverse scattering, the coupling constant spectrum and the Riemann
  hypothesis") translates the problem to the zero-energy coupling-constant spectrum: a repulsive V whose
  coupling spectrum is {ρ} would be needed. What remains as residue: **both use the zeros (or their count)
  as inverse data**, and the property that the spectrum is real is assumed in the construction
  (self-adjointness of a problem whose data is ζ). It is branch 3 (functional of the zero side) and also
  circular. Neither uses a trace identity with the Weil test.

- (d) **Can 𝔞_T be the left-hand side with ϱ ≥ 0 on the right?** There are three ways to wire it:
  - **(W−) ∫V_F = −𝔞_T(F).** I1 gives 𝔞_T = 4Σκ_j − (1/π)∫ϱ. Positivity would require a lower bound
    Σκ ≥ (1/4π)∫ϱ. No theorems go in that direction: Lieb–Thirring, Bargmann and Calogero are upper bounds.
    Moreover, I1 is an identity, so the lower bound **is** 𝔞 ≥ 0 rewritten (branch 5).
  - **(W+) ∫V_F = +𝔞_T(F).** I1 gives 𝔞_T = (1/π)∫ϱ − 4Σκ_j. The term ϱ ≥ 0 plays the role of the sign
    **if and only if Σκ_j is bounded by it**, in particular whenever H_F has no bound states. That is:
    𝔞_T(F) ≥ 0 ⟸ −∂² + V_F ≥ 0.

    This implication was already known without I1: it is Simon's theorem "∫V < 0 ⇒ bound state" in 1D. I1
    only quantifies the excess. There are three obstacles:
    - V_F is 2-homogeneous if quadratic in f. By S-0, the hypothesis "H_F ≥ 0 for all F" ⟺ V_F ≥ 0
      pointwise, which is false (C1 d2) or local (L-loc).
    - With fixed coupling and normalization, the hypothesis is the positivity of the form
      ψ ↦ ∫|ψ′|² + c∫V̂_F|ψ|². It is an operator positivity **stronger** than 𝔞 ≥ 0. In 1D it is equivalent
      to the Riccati factorization V = W′ + W² (Jacobi/Sturm), which is SUSY, index #96, NOT VIRGIN (G1).
    - The identity holds for every V. For Epstein, I1 holds just the same, with more bound states. The
      identity is generic-comb (branch 1) and the whole Λ channel is in Σκ (C-pos ii).
  - **(W3) Wiring with I3:** set ∫V_F² = 𝔞_T(F)·(something ≥ 0) or seek 𝔞 as a difference of the two sides.
    I3 has both right-hand terms ≥ 0 and the left side ≥ 0. There is no indefinite term, so by C-pos (i) it
    cannot contain 𝔞^X for the whole battery. Dies.

  **Falsifier that kills the identity.** Epstein 11 (or DH 12), in the (W+) version. Take (T, f) with
  𝔞^{Ep}_T(f) < 0 (P47 battery). I1 gives (1/π)∫ϱ^{Ep} < 4Σκ^{Ep}, so H_F^{Ep} has a bound state. Consistent,
  nothing is contradicted. But for Λ at T > T_known there is no structural reason why Σκ^Λ = 0: the class of
  V_F^X does not distinguish Λ from Epstein in any property used by I1. The falsifier lies **inside** the
  admissible class of potentials of I1. That is the exact diagnosis: the reflection term is positive for
  every comb; the sign lives in the bound states, and not seeing bound states is the positivity of an
  operator (branch 2).

  **Neumann variant in the window (literal S8), Lemma S-2 (PROVED).** With H_F^N = −∂² + V_F on I_T with
  Neumann condition and ∫_{I_T}V_F = 𝔞_T(F), the test ψ ≡ 1 gives E_0(H_F^N) ≤ 𝔞_T(F)/(2T). Hence
  𝔞_T < 0 ⇒ there is a negative eigenvalue. The converse fails: if V_F has a deep well, E_0 < 0 with 𝔞 > 0.
  Perturbation theory in c: E_0(cV_F) = c𝔞/(2T) − c²‖V_F − mean‖²_{Ḣ^{-1}_N} + O(c³). The first order is the
  sign (branch 5). The second is an Ḣ^{-1} ≥ 0 norm, local in the primitive of V_F, which is fixed and
  generic-comb.

- (e) S7 ✓ in ϱ and κ (nonlinear map of V). S7(iii) ✗: the linearization of I1 is ∫V. S8 ✓ (Neumann in the
  window). Branches 1, 2 and 5. G1 (SUSY #96).
- (f) **VIRGIN as an identity, DEAD: NO-GO ARGUED (class of wirings W−, W+, W3), with S-0, S-2 and C-pos
  PROVED.** The ϱ ≥ 0 term cannot carry the sign because it is positive for every comb. The Wu–Sprung and
  Khuri residue is a different object (zero side) and is left untouched.
- (g) Index: "C2 Faddeev–Zakharov trace identities (I1/I3) with V_F, ∫V_F = ±𝔞_T: NO-GO. ϱ ≥ 0 generic-comb
  (C-pos); sign = absence of bound states = Riccati/SUSY #96; Neumann S-2: first order = sign (branch 5).
  Wu–Sprung/Khuri: zero side (branch 3)".

### C3. Gelfand–Levitan / Marchenko / Kreĭn (inverse)

- (a) CITED: the Gelfand–Levitan equation K(x,y) + Ω(x,y) + ∫K Ω = 0 is solvable on [0, 2T] ⟺ I + Ω_T > 0
  (Kreĭn).
- (b) Index: TB-1 (R186), D-canon, Kreĭn REF-D (:58/:393/:622/:1035), FAMILIES_B F7 NOT VIRGIN.
- (d) The data Ω_T is the Toeplitz truncation of the form (R186_004: single symbol). Solvability is
  literally 𝒲_T > 0.
- (f) **NOT VIRGIN (branch 2).** Not retried. No new reason.

### C4. KdV / Toda / Fredholm determinants

- (a) CITED: conserved KdV invariants I_1 = ∫V, I_2 = ∫V², I_3 = ∫(V³ + ½V′²), …, equal to the moments of
  the trace identities; τ = det(1 + K_V) > 0 for reflectionless potentials (Kay–Moses, Dyson).
- (b) "KdV": 0 hits. "Toda": false positives. W-det is NO-GO (R186_034 Thm 3.1); FAMILIES_B F6 NOT VIRGIN.
- (d) The I_k are local densities in V: by L-loc, if V is local in the test, they do not see the log n
  atoms. If V_F is non-local (C2), the I_k are the same sides of the trace identities as in C2. The KdV flow
  conserves the I_k and N, so it does not transport the sign: it is isospectral, and transports the same
  question.
- (f) **NOT VIRGIN/DEAD:** τ = W-det; I_k = C2; the flow adds nothing (isospectral, PROVED).

### C5. Nonlinear SU(1,1) Fourier transform (Tao–Thiele; Verblunsky)

- (a) CITED (Tao–Thiele, NLFT notes, arXiv 1201.5129): the nonlinear Plancherel identity
  ∫_𝕋 log|a(z)| = −½ Σ_n log(1 − |F_n|²) ≥ 0. On the OPUC side, Szegő/Verblunsky gives
  Σ log(1 − |α_n|²) = ∫ log w.
- (b) "nonlinear Fourier": 0 hits. OPUC/Verblunsky are in MOM (RH2021, L44–L47: inverse Jacobi DEAD).
- (d) There are two readings:
  - with the F_n as test coefficients, both sides are ≥ 0 for every test and no comb appears: C-pos (i)
    kills the identity;
  - with the F_n as Verblunsky coefficients of the form's measure, |α_n| < 1 is needed, which is exactly
    the positivity of the measure (branch 2, MOM).
- (f) **VIRGIN (NLFT) in the first reading, DEAD by C-pos (PROVED). NOT VIRGIN in the second.**

### C6. Ruelle–Bowen topological pressure (and Gibbs/KMS)

- (a) CITED (Ruelle 1978; Bowen LNM 470): P(φ) = sup_μ(h_μ + ∫φ dμ) is convex; dP = μ_φ and
  d²P[ψ,ψ] = σ²_{μ_φ}(ψ) = Σ_k Cov(ψ, ψ∘σ^k) ≥ 0 (Green–Kubo).
- (b) Ruelle, Bowen, pressure: 0 hits as pressure. Perron/PF is NOT VIRGIN (P60-1, CA_I_001). Mayer/Lewis–
  Zagier is CA_A_002 (NO-GO ARGUED). Gauss map is P152 (DEAD). KMS/Gibbs: AUDIT_193 rows 12 and 15 (CIRC,
  "real β only").
- (c) Web: no use for Weil positivity. Mayer relates det(1 − L_s²) to the Selberg zeta of PSL₂(ℤ), not
  directly to ζ.
- (d) **Is the pressure (not the trace) an object distinct from X3c/CA_F_002's?** As an object, yes: the
  pressure is log λ_max(L_φ), a single dominant eigenvalue, not a determinant or a trace. But there are
  three instantiations, and all three die for reasons distinct from the trace's:
  - **(d1) Shift on the alphabet of primes or integers** (primon gas), with φ(n) = −β log n + F(log n). The
    pressure is P(β, F) = log Σ_n n^{−β} e^{F(log n)}. For f ∈ C_c^∞[−T,T] only the values F(log n) with
    n ≤ e^{T} are involved. **Lemma P-fin (PROVED):** P(β, F) − P(β, 0) is a real analytic function of
    finitely many linear functionals L_n(F) = F(log n). Hence it does not satisfy S7(ii). By Thm 3′ and
    Corollary V2-0.b, there is no continuous identity with 𝔞_T, because 𝔞_T is not constant on any open
    set, since its archimedean part is free outside the log n.
    (Proof: the sum over n > e^T does not depend on F, and the finite sum is exp-polynomial in the L_n.) ∎
    Also β is real ("real β only", row 12).
  - **(d2) Gauss map with potential −s log|T′| + εF**, at real s. d²P is the variance under the Gauss
    measure, which is a PSD form with the correlation kernel of the Gauss map. It is blind to ζ (branch 4)
    unless that kernel is made equal to Weil's (branch 5). The connection with ζ only exists through the
    Selberg zeta and the scattering phase of Γ\H (L89).
  - **(d3) Inverse design: a system with correlations = Weil's kernel.** By Green–Kubo,
    σ²(ψ) = 𝔞(ψ) ⟺ Weil's kernel is the covariance function of a stationary process. By Bochner, that is
    exactly the positivity being sought (branch 2, Bochner: 21 hits in the index).
- (e) S7(iii) ✗ by construction: the request itself notes that dP is linear. The positivity is in d²P, which
  is a quadratic form and returns to the original form. S8 ✗ in (d1).
- (f) **VIRGIN as pressure, DEAD:** (d1) NO-GO PROVED by P-fin + Thm 3′; (d2) branch 4; (d3) branch 2
  (Bochner). Answer to the question: the pressure is an object distinct from CA_F_002's trace, but it does
  not survive, for three reasons independent of CA_F_002's.
- (g) Index: "C6 Ruelle–Bowen pressure: prime shift = analytic function of finitely many F(log n) (Lemma
  P-fin, PROVED, Thm 3′); Gauss map blind (branch 4); d²P = variance ⇒ Bochner (branch 2)".

### C7. Viscosity solutions of Hamilton–Jacobi with data F

- (a) CITED: Crandall–Lions comparison principle (1983) and Hopf–Lax formula for convex H.
- (b) Viscosity: 0 hits. Hamilton: 3 hits, unrelated. Legendre/tropical: L29 (Connes–Consani tropical) and
  R166_601.
- (d) There are two versions:
  - **Local:** u_t + H(u_x) = 0, u(0) = F, with the comb in H. Natural: H = θ_T, the symbol, as a
    Hamiltonian. θ_T is not convex, so there is no Hopf–Lax. The amplitude expansion is
    u = εF − tθ_T(εF′) = … and is local. L-loc kills it. Also, comparison gives monotonicity in F, but 𝔞 is
    not monotone in F.
  - **Non-local:** u_t + Σ_n v_n (2u(x) − u(x+log n) − u(x−log n)) + … = 0. Comparison holds because the
    weight is ≥ 0, but the operator is a Lévy generator: Dirichlet form/Beurling–Deny (106_17, CA_I_001,
    INV_D_001 D1), NOT VIRGIN. And the comb enters 𝔞 with the opposite sign of a generator.
- (f) **VIRGIN-DEAD:** the local version dies by L-loc (PROVED); the non-local version is NOT VIRGIN
  (Lévy/Dirichlet).

### C8. Monge–Ampère / Brenier

- (a) CITED (Brenier 1991; Villani): the Brenier potential is convex and det D²u = ρ₀/ρ₁∘∇u. The
  linearization of W₂² around ρ₀ is ‖h‖²_{Ḣ^{-1}(ρ₀)} ≥ 0.
- (b) Monge, Brenier: 0 hits. FAMILIES_B F11 (optimal transport) NOT VIRGIN. L5 listed it with no object.
- (d) There are two options:
  - ρ_F = normalized |f|² and ρ₁ = the comb Σ v_n δ_{log n} restricted. In 1D, W₂ has an explicit formula in
    quantiles: nonlinear ✓, but its second variation is Ḣ^{-1}(ρ₀), local in the primitive, and L-loc kills
    it.
  - With a non-local cost c(x,y) containing the atoms, Monge–Ampère is lost and Kantorovich remains: an LP,
    which is P47's LP/dual certificate family, branch 2.
- (f) **VIRGIN-DEAD** (L-loc PROVED; Kantorovich = LP NOT VIRGIN).

### C9. Renormalization fixed points

- (b) Index: renormaliz 8 hits (G3F-102/167/170/171 DEAD; GG self-similarity of FF.1; R161
  renormalizations).
- (d) The natural candidate is R: T ↦ T + ½log 2 with the comb rescaling n ↦ 2n. The comb is not
  self-similar (Λ(2n) ≠ Λ(n)), so there is no fixed point. Also the monotonicity in T (R186_004) makes λ(T)
  non-increasing: the flow adds nothing.
- (f) **NOT VIRGIN.**

### C10. Berezin–Li–Yau / Laptev for the truncated symbol (new; literal S8: the window as a hard wall)

- (a) CITED (Berezin 1972; Li–Yau 1983; Laptev JFA 151 (1997) 531–545). For P_Ω a(D) P_Ω, with a a real
  measurable symbol, the sum of the first k eigenvalues satisfies
  Σ_{j≤k} λ_j ≥ inf{∫ a(s)ρ(s)ds : 0 ≤ ρ ≤ |Ω|/2π, ∫ρ = k} (bathtub).
  It is nonlinear in the symbol (concave, infimum of linear functionals), S7 ✓ in the symbol. The window
  enters as the domain Ω, so S8 ✓.
- (b) Berezin, Li–Yau: 0 hits. Szegő/Toeplitz λ_min ≥ ess inf of the symbol is implicit in W-det/Wiener–Hopf.
- (d) Ω = I_T (|Ω| = 2T), a = θ_T^X (genuine function, by R186_004's boundary lemma), k = 1:
  λ_1(𝒲_T^X) ≥ B_T^X := average of θ_T^X over its sublevel set of measure π/T.
  The Λ channel enters the formula: θ_T^X depends on v_n^X, so B_T changes with Epstein, DH, etc. But it
  enters as an infimum of linear functionals in the comb: it is branch 1 (generic-comb in the Φ200 sense).
  Restriction to P_T: the moments A = B = 0 are codimension 2. The bathtub applies to all of L²(I_T), so it
  is weaker than λ_A.
- (e) Prediction (ARGUED): θ_T(0) = m(0) − Σ_{n≤N_T} v_n ≈ −4e^{T}, and the valley has width ≍ 1/log N_T ≍
  1/T. The sublevel set of measure π/T includes it, so B_T < 0 from moderate T onward, while λ_A(T) > 0 is
  known up to ½log 15. The bound loses.
- (f) **VIRGIN, almost certainly DEAD (branch 1, ARGUED).** It is the only case with a finite and cheap
  falsification lemma. It stays in the ranking as a discard proof, not as a candidate.

### C11. Thouless / logarithmic energy (Frostman) / Lyapunov exponent

- (a) CITED: −∬log|x−y| dν dν ≥ 0 for ν of total mass 0 with compact support (Frostman/potential theory).
  Thouless's formula gives γ(E) = ∫log|E−x| dN(x) ≥ 0.
- (b) Frostman, Thouless, Avila: 0 hits.
- (d) The archimedean part of 𝔞 contains a log|x|-type kernel (digamma ~ log). Its positivity at zero mass
  is known and is not the problem (the archimedean piece is the one that "helps"). If a discrete Schrödinger
  operator is used with V(n) = comb weights, Thouless's formula sees the density of states of a finite
  sequence in the window, a finite datum (V2-0). If the sequence is infinite (all n), S8 ✗: the structure
  enters outside the window.
- (f) **VIRGIN-DEAD** (the archimedean part is already positive: branch 1; discrete version: finite datum,
  C-emb (a)).

### C12. Voiculescu free entropy/information (χ, Φ*)

- (a) CITED: Φ*(μ) ≥ 0, free Stam inequalities and subordination.
- (b) Voiculescu: 0 hits. Its classical neighbor, entropy/Fisher, is FAMILIES_B F19/F20.
- (d) The only natural μ carrying window information is the spectral measure of 𝒲_T: branch 2. A μ_F built
  from the test (distribution of f) does not see the comb (branch 4).
- (f) **VIRGIN-DEAD** (branches 2 and 4).

### C13. Nonlinear Nevanlinna–Pick problem / Maslov index of the family in T

- (b) Pick: 3 hits (Pick cone/LP in INV_F_001). Maslov: IDX (index/Maslov, phases 0–99).
- (f) **NOT VIRGIN.**

### C14. Sturm oscillation for the nonlinear operator in V (explicit request)

- (a) CITED: N(V) = number of zeros on (0, ∞) of the zero-energy Jost solution (Sturm, Calogero).
- (b) Sturm/nodal: DEAD (G8D-155, R160_S4, SPEC_011). CS0_COMMUTE: no operator of order ≤ 2 commutes
  (PROVED).
- (d) The new reason versus CS0 is that here the operator does not commute with 𝒲_T: it is −∂² + V_F, built
  from the test. But then N(V_F) is C1's count, which dies by S-0, S-1 and Thm 3′.
- (f) **DEAD by C1.** The new reason exists, but does not dodge the reason for failure: integer, locally
  constant in F.

## 3. Filter table

| # | Family | Virgin | S7 (i/ii/iii) | S8 | Φ200 branch / C-emb / Thm 3′ / G1 | Verdict |
|---|---|---|---|---|---|---|
| C1 | bound states, Bargmann/Calogero/LT | yes | ✓/✓/✗ | depends | 5 (weak), 1, 2; Thm 3′ | NO-GO PROVED (S-0, S-1) / ARGUED |
| C2 | Faddeev–Zakharov trace | yes (identity) | ✓/✓/✗ | ✓ (Neumann) | 1, 2, 5; G1 SUSY | NO-GO ARGUED (C-pos, S-0, S-2 PROVED) |
| C3 | Gelfand–Levitan/Kreĭn | no (TB-1) | — | — | 2 | NOT VIRGIN |
| C4 | KdV/Toda/Fredholm | partial | ✓/✓/✗ | — | W-det, C2 | NOT VIRGIN/DEAD |
| C5 | NLFT SU(1,1) | yes | ✓/✓/✓ | ✗ | C-pos (i), 2 | DEAD (PROVED) |
| C6 | Ruelle–Bowen pressure | yes (pressure) | ✓/✗/✗ | ✗ (d1) | Thm 3′, 4, 2 | NO-GO PROVED (P-fin) / branches |
| C7 | HJ viscosity | yes | ✓/✓/✗ | ✗ | L-loc; Lévy NOT VIRGIN | DEAD (PROVED) |
| C8 | Monge–Ampère/Brenier | partial (F11) | ✓/✓/✗ | ✗ | L-loc; LP | DEAD (PROVED) |
| C9 | renormalization | no | — | — | — | NOT VIRGIN |
| C10 | Berezin–Li–Yau on θ_T | yes | ✓ (in symbol) | ✓ | 1 | DEAD ARGUED; discard lemma |
| C11 | Thouless/Frostman | yes | ✓/✓/✗ | ✗ | 1, C-emb (a) | DEAD |
| C12 | Voiculescu | yes | ✓ | ✗ | 2, 4 | DEAD |
| C13 | Pick/Maslov | no | — | — | 2 | NOT VIRGIN |
| C14 | Sturm on V_F | new reason | = C1 | | Thm 3′ | DEAD |

## 4. Class diagnosis (ARGUED)

S7 + S8 + "intrinsic positivity" form a combination that is self-contradictory, except for one case that is
exactly REF-D:

1. If the classical theorem's positivity is intrinsic (holds for every input), C-pos (i) prevents the
   invariant from coinciding with 𝔞^X on the battery. The Λ channel has to enter through a hypothesis.
2. The hypotheses of the theorems in this class are: no bound states (Schrödinger), GL solvability (Kreĭn),
   |α_n| < 1 (Verblunsky), covariance (Bochner), Lévy generator (non-local comparison). All of them are
   positivities of a quadratic operator built from the window and the comb, and in every case that
   positivity is equal to or stronger than 𝔞 ≥ 0. It is branch 2.
3. If the invariant is nonlinear but local in the test, L-loc disconnects it from the log n atoms.
4. If it is nonlinear and non-local but from a finite discrete datum (pressure on primes, discrete
   Thouless), P-fin / V2-0 make it analytic in finitely many functionals: Thm 3′.
5. The "useful" nonlinearity (S7 iii) of spectral families always has a linear functional as its first order
   (Simon, Born, dP = μ_φ). The sign of that first order is either 𝔞's or that of a generic-comb functional.

This is **not** a class-impossibility theorem. It is the pattern observed across 14 families, covered
piecewise by 6 PROVED lemmas (L-loc, C-pos i, S-0, S-1 CITED, S-2, P-fin). It can go into the index as
"Pattern C201" (ARGUED).

## 5. Ranking (≤3) with a finite and decidable first lemma

None is viable in the FAMILIES_A/B sense. The following three are cheap proofs that close or reopen with a
concrete datum. They are not long constructions.

**R1. C10 Berezin–Li–Yau/bathtub on θ_T^Λ (discard).**
- Lemma C10.1 (decidable, NUMERICAL with interval arithmetic): compute B_T^Λ = average of θ_T^Λ over its
  sublevel set of measure π/T, for T ∈ {½log2, ½log3, ½log5}, with m(s) from lem:K and exact finite sums.
- Death criterion: B_T^Λ < 0 at T = ½log 3, where λ_A > 0 is PROVED (Theorem C). In that case the bound is
  strictly weaker than what is already proved: NO-GO.
- Survival only if B_T^Λ > 0 and B_T^{Ep} < 0 at the same T, which the linear channel makes nearly
  impossible (ARGUED). Cost: a script.

**R2. C2-Neumann second order (discard of C2's last crack).**
- Lemma C2.1 (finite, PROVED or disproved by hand): for V_F = f̄·𝒲_T f on I_T with Neumann, decide whether
  there exists c* > 0 uniform in F ∈ P_T with E_0(c*V̂_F) ≥ 0 ⇒ 𝔞 ≥ 0 and, conversely,
  𝔞 ≥ η‖f‖² ⇒ E_0(c*V̂_F) ≥ 0.
- Death criterion: a single pair (T < ½log 2, f) with 𝔞 > 0 but E_0(cV̂_F) < 0 for every c > 0 (a deep local
  well of V̂_F with positive mean) kills the converse. Then the family is not a tool: it only implies
  𝔞 ≥ 0 from something stronger. Forecast: dies (S-0 scaled to the norm).

**R3. Lemma C-pos in the inequality version (class closure).**
- Lemma C-pos.2 (finite statement): let Ψ(f, X) ≥ 0 be an intrinsic positivity and E(f, X) the error. If
  𝔞_T^X ≥ Ψ − E(X) for the whole battery and E is a continuous function of finitely many functionals of the
  comb, then E^Λ ≥ Ψ at some (T, f) with T ≤ ½log 2.
- Death criterion of the lemma (and of its usefulness as a closure): an explicit counterexample with E not
  continuous in the comb. If proved, it closes C1–C12 as a class at once.

Recommendation: run R1 (a script) and write up R3. Do not launch a long construction on any family C.

## 6. Entries for the index (written by whoever synthesizes)

- C1/C14 bound states/Sturm on V_F: NO-GO (S-0 PROVED, S-1 Simon CITED, Thm 3′).
- C2 trace identities I1/I3: NO-GO ARGUED (C-pos, S-2 PROVED; sign = Riccati/SUSY #96). Wu–Sprung and Khuri:
  zero side (branch 3).
- C5 NLFT: C-pos (i) PROVED. C6 pressure: P-fin PROVED + branches 4 and 2. C7/C8 HJ and Monge–Ampère:
  L-loc PROVED.
- C10 Berezin–Li–Yau on θ_T: branch 1 ARGUED; discard lemma R1 pending. C11, C12: dead.
- C3, C4, C9, C13: NOT VIRGIN.
- Pattern C201 (ARGUED): intrinsic positivity + channel in the hypothesis = branch 2.

## 7. Sources

- Wu, Sprung, "Riemann zeros and a fractal potential", Phys. Rev. E 48 (1993) 2595.
  https://journals.aps.org/pre/abstract/10.1103/PhysRevE.48.2595
- Khuri, "Inverse scattering, the coupling constant spectrum, and the Riemann hypothesis", hep-th/0111067.
  https://arxiv.org/html/hep-th/0111067
- Sierra, Dirac/Rindler with prime potential, arXiv 1404.4252. https://arxiv.org/pdf/1404.4252
- B. Simon, "The bound state of weakly coupled Schrödinger operators in one and two dimensions", Ann. Phys.
  97 (1976) 279–288. http://www.math.caltech.edu/simon/biblio.html
- Laptev, "Dirichlet and Neumann eigenvalue problems on domains in Euclidean spaces", JFA 151 (1997)
  531–545. On Berezin–Li–Yau: https://arxiv.org/html/0711.4925
- Faddeev–Zakharov (1971), Lieb–Thirring (1976), Deift–Trubowitz (1979), Ruelle (1978), Bowen (LNM 470),
  Brenier (1991), Crandall–Lions (1983), Tao–Thiele (arXiv 1201.5129): CITED from standard memory, not
  verified on the web in this session.
</content>
