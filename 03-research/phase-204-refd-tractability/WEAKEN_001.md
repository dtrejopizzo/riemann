# WEAKEN_001 — Phase 204o: can the hypothesis consumed by the 22 TRANSFER entries be weakened to something PROVED?

Every statement is D-only
(𝔞_T ≥ 0 on P_T, λ_A(T) ≥ 0, W_T ⪰ 0).
**Sources read:** FINAL_204_001 (table of 43), AUDIT_204_CLOSURES_001 (Lemma WT, PC-2), Paper 47 (lem:monoT l.502,
prop:polarcap l.4316, prop:WT l.4358, rem:polarcapdiag), MAP_200_001 §2 (W2 / Cor 2′). **Corpus check:** the question
«hypothesis consumed → PROVED weakening» does not appear in ROUTES-TRIED-INDEX nor in FINAL_204 §6 (which only
records TRAT). New explicit reason versus the recorded attempts: no reformulation is retried as a route to D; the
general theory's *hypothesis* is swapped for one already PROVED and we ask what follows. Every row that dies here is
recorded as an «empty weakening».

## Summary (≤300 words) — revised after AUDIT_204_W1_001

The 22 TRANSFER entries consume four hypotheses: (H-PD) 𝔞_T ⪰ 0 on P_T ∀T; (H-inv) 0 ∉ spec in a sector/block;
(H-unif) uniform control in T; (H-tail) control of the prime tail > e^{2T}. The strongest partial datum is D0:
λ^W(T) > 0 for T ≤ T₀ = ½log15 (Mori, λ^W(T₀) ≥ 2^{−2904}, CITED; extended downward by lem:monoT). Weakening (H-PD) to
«T ≤ T₀» gives, in 11 rows, something equivalent to the datum (Lemma W0, PROVED), in 6 nothing (D8), and in 5
structural content (Kreĭn, de Branges/Douglas, affinity in t, and K11) confined to (0,T₀]. K11/prop:WT: Lemma W1
(q_odd nondecreasing) is PROVED but is **lem:gmono rewritten in the variable q = 1/(𝔤+2)**; Corollary W1′ (𝔄_odd ≻ 0,
q_odd < ½ on (0,T₀]) is PROVED using the Mori bound. **No amplification:** ½ − q_odd ≍ ‖h_odd‖²λ^W_odd
(thm:parityschur (a3)–(a4)); the 2.5·10⁻⁴ is an UPPER Galerkin bound measured at T = ½log3, not at ½log15, where it
is predicted to be ≲ 10⁻⁶⁵/ℓ(e)². (L-b) is NO-GO (TRANSFER, restriction 11: the R6/T6.2 route). No row produces a
polynomial-scale signed quantity. Answer to «closer to the sign?»: **no**; this pass only records, with proof (Lemma
W0), why the finite-T weakenings are sterile, and leaves a measurement (L-a) to pin down the odd channel's constants
at ½log15.

## 0. Available partial data (closed list of PROVED/CITED inputs)

| Id | Statement | Label |
|---|---|---|
| D0 | λ^W(T) > 0 (hence W_T ≻ 0, λ_A(T) > 0) for T ≤ T₀ = ½log15; λ^W(T₀) ≥ 2^{−2904} | CITED (Mori; verified phases 194–198) + lem:monoT |
| D1 | lem:monoT: λ_A, λ_P, λ^W nonincreasing in T, even at contact thresholds | PROVED (P47 l.502) |
| D2 | lem:contT: λ^W continuous | PROVED |
| D3 | prop:WT: inertia per sector via q_par, requiring only 0 ∉ spec(𝔄_par), q ≠ 0 | PROVED (P47 l.4358) |
| D4 | PC-2: 𝔤_par(T) ≤ W_{T₁}(F)/ℓ(F)² for T ≥ T₁ if λ^par_A(T) > 0 | PROVED |
| D5 | Lemma T3 (Haynsworth ×2) | PROVED |
| D6 | n_−(𝔄_ev) = 1, q_ev + ½ ≈ −2·10⁻⁸; n_−(𝔄_odd) = 0, q_odd ≈ ½ − 2.5·10⁻⁴ (at ½log3) | NUMERICAL |
| D7 | Inertia (10,0,1) in the cited block; Theorems B/B′/C; Φ.12 | PROVED (per sources 186/200) |
| D8 | W2 / Cor 2′: every perturbative step in T requires doubly exponential cancellation | PROVED (MAP_200 §2) |

General remark (PROVED, immediate from D1): **every hypothesis of the form «positivity up to T₁» with T₁ ≤ T₀ comes
for free**, and every hypothesis «positivity at T₁ > T₀» is D_{T₁}, unavailable. No «up to finite T» weakening can,
by itself, conclude anything at T > T₀ without a continuation step; and continuation steps fall under D8. This
fixes the ceiling of this pass: what can be gained are **structures valid on (0, T₀]** and **signed quantities whose
scale decides whether continuation is even conceivable**.

---

## 1. Table of the 22 TRANSFER entries

Columns: (b) general theorem; (c) exact hypothesis consumed; (d) PROVED weakening and what the theory concludes; (e)
verdict and scale of the signed quantity. «Equiv. to the datum» = the conclusion is a rewriting of D0 with no
additional content.

| # | (a) D-only reformulation | (b) General theorem | (c) Exact hypothesis consumed | (d) PROVED weakening → conclusion | (e) Verdict / scale |
|---|---|---|---|---|---|
| K1 | Weyl function m_T of the window formula is Nevanlinna (Herglotz) | Nevanlinna–Herglotz; de Branges (space H(E) with E Hermite–Biehler) | (H-PD) on P_T, ∀T | With D0: m_T is Herglotz for T ≤ T₀, there exists E_{T₀} Hermite–Biehler and H(E_{T₀}) isometric to (P_{T₀}, W) | **Structural content CITED/PROVED on (0,T₀]**: increasing de Branges chain {H(E_T)}_{T≤T₀} (lem:monoT ⇒ isometric inclusion). No sign beyond that. Scale: none new. |
| K2 | Kreĭn indeterminacy of the extension problem for g_T | Kreĭn (extension of PD functions on [−2T,2T]); Nevanlinna parametrization of extensions | strict (H-PD) on [−2T,2T] ∀T | With D0: g restricted to [−2T₀,2T₀] is strictly PD ⇒ the problem is **indeterminate**, set of extensions = {measures σ ≥ 0} parametrized by Schur functions | **Non-trivial (CITED Kreĭn + D0):** there exists an infinite family of positive measures σ with σ̂ = explicit data on |u| < 2T₀. See Lemma W3. Does it get closer? It converts D_{T₁} (T₁>T₀) into «some extension of T₀ is compatible with the primes in (15, e^{2T₁}]»: that test is K8 ⇒ D8. No new scale. |
| K3 | Li/Keiper/Jensen–Hankel uniform in order | Hamburger/Hankel; GORZ (fixed order) | (H-PD) of the moment functional at every order (≡ ∀T by cor:Li outside 𝒲_T) | Window T₀: positivity of the Hankel matrices *of the window form* up to T₀ (equiv. to the datum). The Li kernel is outside 𝒲_T (cor:Li) | **Empty**: what is concluded for T ≤ T₀ is D0 rewritten; the Li coefficients λ_n are not functionals of 𝒲_{T₀}. |
| K4 | W_T = A*A with A causal (Douglas / Wiener–Hopf / Sz.-Nagy) | Douglas's lemma; Wiener–Hopf factorization of a ≥ 0 symbol | (H-PD) of the symbol on P_T | With D0: there exists a causal A_{T₀} (Douglas, CITED). P1.A forbids convolutive A for T ≥ ½log3 | **Non-trivial structure but no use found:** A_{T₀} exists, non-convolutive (P1.A), not explicit. No scale. |
| K5 | Archimedean Schur complement Σ(T) ⪰ 0 | Szegő / Schur–Haynsworth | ≥ 0 symbol of the complementary block (≈ (H-PD)) | Weakening to (H-inv): only 0 ∉ spec(𝔞_T|𝒱) ⇒ Haynsworth gives In(W) = In(block)+In(Σ) (= Lemma T3) | **Equiv. to the datum** as a sign; the inertia bookkeeping is already there (T3). |
| K7 | Flat-top certificate ν̂ ≥ 0 (thm:Z) | Hahn–Banach / cone duality | separation of the admissible cone (≈ D_T) | With D0: certificates exist for T ≤ T₀ (½log5, ½log15 explicit) | **Equiv. to the datum** (it is D0 by thm:Z). finZ: no finite certificate exists ∀T. |
| K7b | Problem B (primes > e^{2T}) | Hahn–Banach with restricted support | (H-tail) | No PROVED version of (H-tail) | **Empty.** Thms L, Σ are negative. |
| K8 | Gradual law λ_T ≥ −Ce^{κT} | Phragmén–Lindelöf / convexity in T | (H-unif) at κ = 0 | With D0 + D1: λ_T ≥ 0 on (0,T₀]; for T>T₀ only the trivial bound λ_A(T) ≥ −‖comb‖ | **Empty**; the missing hypothesis is a zero-free band (D8). |
| K9 | Sonin ρ*(T) < 1 | Müntz–Szász (all-or-nothing) | angle < 1 for all T | With D0: ρ*(T) < 1 for T ≤ T₀ (equiv.) | **Equiv. to the datum**; Müntz gives no gradation. |
| K10 | (L2) S_{T,k} ⪰ 0 | Haynsworth + Fredholm (Cor L1) | 0 ∉ spec(𝔞_T|P_T) (invertibility only, not sign) for the *equivalence*; positivity for the conclusion | (H-inv) on T ≤ T₀ is PROVED (from D0) ⇒ S_{T,k} nonsingular and ⪰ 0 on (0,T₀] | **Equiv. to the datum**. Note: invertibility alone IS PROVED on (0,T₀] but gives no sign (crossings possible at T>T₀; lem:monoT). |
| K11 | Polar capacity 𝔤_par(T) ≥ 0 | prop:polarcap / prop:WT (Weyl–Tate, rank one) | λ^par_A(T) > 0 (old version); in prop:WT only 0 ∉ spec(𝔄_par), q ≠ 0 | **Already weakened** (D3). With D0 on (0,T₀]: n_−(𝔄_odd)=0, q_odd < ½; n_−(𝔄_ev)=1, q_ev < −½ | **Reformulation of lem:gmono in the variable q = 1/(𝔤+2)** (Lemma W1); margins ≍ background per sector (not amplified); 2.5·10⁻⁴ and 2·10⁻⁸ are Galerkin upper bounds at ½log3. |
| K12 | (Ω_{t₀}) damped comb | convex interpolation in t | positivity ∀T at fixed t₀ | Weakening to T ≤ T₀: trivial (t=1 is D0, does convexity in t of the form give every t ∈ [t*,1]?) — the form is *affine* in t ⇒ positivity at t=1 and at t=0 (pure archimedean, PROVED) ⇒ ∀t ∈ [0,1], T ≤ T₀ | **PROVED but trivial** (affinity). K12's Lemma 2.1 blocks the extension. |
| K28 | Theorem A at large T | Prop 5 (phase 153): odd box | extension of the odd box beyond log 2 | D0 gives the odd box up to T₀ indirectly (odd ⪰ 0) | **Equiv. to the datum**; but points to the same odd channel as K11 (same margin ≍ odd background). |
| K31 | R-C.a given R-C.b | logic | R-C.a ⟺ D given R-C.b | — | **Empty** (logical). |
| K32 | Bagchi recurrence | Voronin universality | the strong version uses the full datum | Window recurrence T ≤ T₀: not written D-only | **Empty / OPEN** (no D-only form exists). |
| K34 | (N)/(N_loc) Σ v_n Re c_F(log n) ≤ 𝔞_∞(F) | Cauchy–Schwarz / large sieve | signed cancellation at scale e^{2T} (H-tail+H-unif) | With D0: (N_loc) true for T ≤ T₀ (equiv.) | **Equiv. to the datum**; no weakening of the cancellation is PROVED. |
| K35 | (Ω₀) bending mode Σ2Λ(n)n^{−½}h_T(log n) < 0 | finite computation per T | ∀T > ½log5 | For T ≤ T₀ it's a finite count with primes ≤ 15 | **PROVED-trivial on (½log5, T₀]** (finite, NUMERICALLY certifiable); its magnitude is O(1), not amplified; but it is *necessary*, not sufficient. |
| K36 | (Ω_Φ) Poisson–Euler fixed point | contraction (Banach) | |Φ′| < 1 on the orbit of λ (consumes the sign of λ) | Linear branch: tautological | **Empty**. |
| K37 | (E_γ) twisted Chebyshev | Bohr/Landau per frequency | criticality at each γ | For T ≤ T₀ (finite packet): equiv. to the datum | **Empty** (the limit m♯(γ) = the target). |
| K38 | λ_A ≥ −ε(T), ε → 0 | lem:monoT | ε ≡ 0 | D1 ⇒ ε(T)=0 on (0,T₀] | **Equiv. to the datum.** |
| G3 | Coercive gauge-minimized L′♯ | Fredholm + relative compactness (S5) | coercivity = (L2) | With D0: coercivity for T ≤ T₀ | **Equiv. to the datum** (current target). |
| G8 | Arch ≥ Near (near-coincidences) | term-by-term domination | positivity of the Near-arch block | Residues l.391/415 attackable without a sign | **OPEN with no sign** (not weakened, just separated). |

Count: **non-trivial content** in 5 (K1, K2, K4, K11, K12-trivial-affine); **signed quantity at non-doubly-exponential
scale**: none (K11 dismissed after AUDIT_204_W1_001); **equivalent to the datum** in 11; **empty** in 6.

---

## 2. Why almost every weakening is «equivalent to the datum»

**Lemma W0 (PROVED, formal).** Let 𝒯 be a general theorem whose hypothesis is «𝔞_T ⪰ 0 on P_T» for a fixed T and
whose conclusion 𝒞(T) is a property of the form on window T (not on window T′ > T). Then, for T ≤ T₀, 𝒞(T) is
PROVED, and no 𝒞(T) with T ≤ T₀ implies 𝔞_{T₁} ⪰ 0 for T₁ > T₀ unless 𝒞 contains data about the contacts
n ∈ (e^{2T₀}, e^{2T₁}).

*Proof.* By lem:monoT the zero extension identifies P_T ⊂ P_{T₁} with the same form; the form on P_{T₁} differs from
that on P_T only by the functions whose support reaches |t| > T and by the contacts n with log n ∈ [2T,2T₁). 𝒞(T)
sees neither. ∎

Consequence: weakening «∀T» to «T ≤ T₀» always yields something PROVED but *confined* to (0,T₀]. The only rows that
escape this confinement are those that produce an object with **monotonicity in T** (K1, K2, K11): there what is
gained is a *direction* of variation whose sign and scale are measurable. None gives a scalar quantity with a margin
larger than the background (AUDIT_204_W1_001).

---

## 3. The three rows with content

### 3.1 K11 / prop:WT — the odd channel in the variable q (no amplification)

Reminder (D3): in the odd sector, W_odd = 𝔄_odd − 2ℓ_odd² with ℓ_odd(F) = S(F) = ∫F sinh(t/2) (χ_odd = Riesz
representative, unnormalized), and W_odd ≻ 0 ⟺ 𝔄_odd ≻ 0 ∧ q_odd < ½, q_odd = ⟨𝔄_odd⁻¹χ_odd, χ_odd⟩, 𝔤_odd = 1/q_odd − 2.

**Lemma W1 (monotonicity of q_odd; PROVED — not new).** Let J ⊂ (0,∞) be an interval on which 𝔄_odd(T) ≻ 0. Then
q_odd(T) = sup_{F ∈ 𝒟^odd_T, F≠0} ℓ_odd(F)² / 𝔞_T(F) and T ↦ q_odd(T) is nondecreasing on J.

*Proof.* Cauchy–Schwarz in the inner product 𝔞_T (equality at F = 𝔄⁻¹χ). For T < T′ the zero extension E preserves
parity, ℓ_odd (a T-independent formula), and 𝔞 (lem:monoT's proof). ∎

*Novelty: none.* Since 𝔤_odd = 1/q_odd − 2 and x ↦ 1/(x+2) is decreasing, Lemma W1 ⟺ lem:gmono (P47 l.4760) in the
odd sector. It is a **reformulation of lem:gmono in the variable q = 1/(𝔤+2)** (AUDIT_204_W1_001 §1(c)).

**Corollary W1′ (PROVED given D0 + D3, proof redone).** For every T ≤ T₀: 𝔄_odd(T) ≻ 0 and q_odd(T) < ½;
μ_odd(T) := ½ − q_odd(T) is positive and nonincreasing on (0,T₀].

*Proof.* W_T ⪰ 0 alone would only give q_odd ≤ ½ and 𝔄_odd ⪰ 0. The Mori bound is used: λ^W(T₀) ≥ 2^{−2904} > 0
(CITED) and, by lem:monoT, λ^W(T) ≥ λ^W(T₀) > 0 for T ≤ T₀. Thus W_odd(T) has a positive background, n_−(W_odd) = 0
and a trivial radical. Since W_odd = 𝔄_odd − 2ℓ_odd² ≤ 𝔄_odd, 𝔄_odd has background ≥ λ^W > 0, hence 𝔄_odd ≻ 0 and
0 ∉ spec; q_odd > 0 (𝔄_odd ≻ 0, χ ≠ 0). By prop:WT(ii) and (iii), n_−(W_odd)=0 and non-degeneracy ⇒ strict q_odd < ½.
Monotonicity: Lemma W1 on J = (0,T₀]. ∎

**Why there is no amplification (CITED from AUDIT_204_W1_001 §2–3; PROVED by thm:parityschur(a3)–(a4)).**
- ½ − q_odd = 𝔤_odd·q_odd/2 ≈ 𝔤_odd/4, and λ^W_odd ≤ 𝔤_odd/‖h_odd‖² ≤ 2λ^W_odd (when 2λ^W_odd < λ_A^odd); also
  𝔤_odd ≤ λ^W_odd/ℓ(e_odd)² for the background vector e_odd. Hence **½ − q_odd ≍ ‖h_odd‖²λ^W_odd**: the odd margin
  is the odd background in different units.
- The value 2.5·10⁻⁴ is measured at **T = ½log3** (as prop:WT states) and is an **UPPER** Galerkin bound on the
  margin, not a lower one.
- At ½log15 the prediction is ½ − q_odd ≲ 10⁻⁶⁵/ℓ(e_odd)². The smallness of the background passes through to q
  unchanged; the change of variable does not reduce it.

What remains is the equivalence (PROVED, with no sign content): «W_odd(T) ≻ 0 ∀T» ⟺ [𝔄_odd ≻ 0 ∀T] ∧
[q_odd(T) < ½ ∀T], with q_odd monotone. It is prop:WT + lem:gmono; **the «amplified sign» label is withdrawn**.

**Lemma W2 (even channel; PROVED given D0+D3).** For T ≤ T₀: n_−(𝔄_ev(T)) = 1 and q_ev(T) < −½; and if moreover
n_−(𝔄_ev) remains 1 on an interval, is q_ev **nonincreasing**? — **It cannot be shown**: with n_−(𝔄_ev)=1 the
variational characterization is a min-max (Courant minimax over an indefinite space), not a sup; the monotonicity of
q_ev in T does not follow from the zero-extension argument. Label: **OPEN**; the margin is 2·10⁻⁸ (not amplified).
The even channel remains the bottleneck.

### 3.2 K2 — Kreĭn extensions up to T₀

**Lemma W3 (CITED Kreĭn + D0).** Let g be the distribution of the explicit formula (prime side + archimedean). For
T ≤ T₀, the restriction g|(−2T,2T) is strictly positive definite; the set ℰ_T of positive measures σ on ℝ with
σ̂ = g on (−2T,2T) is nonempty, convex, weak-* compact, and parametrized by the Schur function of a
Nevanlinna–Pick problem (indeterminate case). By lem:monoT, ℰ_{T} ⊇ ℰ_{T′} for T < T′ ≤ T₀.

Non-trivial conclusion: up to T₀ a «positive spectral measure» exists compatible with every prime ≤ 15 on the
logarithmic scale. But (honestly): the chain ℰ_T is decreasing, and «ℰ_{T₁} ≠ ∅» is exactly D_{T₁}. The question
«how much does ℰ_T shrink?» is measured by the Weyl radius (Weyl disc of the Schur parameter) r_W(T), whose scale
is — via the de Branges reproduction formula — of order λ^W(T) (a doubly-exponentially small quantity).
**Weakening with content, but no amplification.** NO-GO as an amplifier (ARGUED, the Weyl radius is comparable to
the background by the reproducing-kernel formula).

### 3.3 K1/K4 — de Branges chain and causal factorization up to T₀

With D0, {H(E_T)}_{T≤T₀} is an increasing de Branges chain (CITED de Branges, Thm 40 + lem:monoT), and
W_T = A_T*A_T with A_T causal (Douglas, CITED). Content: the canonical Hamiltonian H(t) of the chain exists for
t ≤ T₀ and is ⪰ 0 (trace 1). Positivity for T > T₀ ⟺ the Hamiltonian extends ⪰ 0. This is a reformulation (already
in K1), not a signed weakening; the size of det H(t) near T₀ would be the interesting quantity, and it is tied to
λ^W ⇒ no amplification (ARGUED).

---

## 4. Weakenings of (H-unif) and (H-tail): empty by D8

Rows K7b, K8, K34, K36, K37, K38. The hypothesis consumed is not a positivity but a *uniform control* (in T or in
the prime tail). No PROVED weakening exists: the strongest available is the trivial bound
|comb| ≤ Σ_{n≤e^{2T}} Λ(n)n^{−½}‖c_F‖_∞, which is ≫ 𝔞_∞ and concludes nothing. W2/Cor 2′ (D8) states that any
sufficient control requires cancellation to precision exp(−e^{cT}). **NO-GO for the weakening (PROVED as a
consequence of D8 for the class «uniform tail weakening»).**

---

## 5. Systematic search for polynomial-scale signed quantities

| Quantity | Sign forced by | Measured scale | Monotone in T? | Amplified? |
|---|---|---|---|---|
| ½ − q_odd(T) | D0 + D3 (T ≤ T₀) | ≤ 2.5·10⁻⁴ (Galerkin upper bound, at ½log3); ≲ 10⁻⁶⁵/ℓ(e)² predicted at ½log15 | yes, nonincreasing (Lemma W1 = lem:gmono) | **No** (≍ ‖h_odd‖²λ^W_odd) |
| 𝔤_odd(T) = (1−2q_odd)/q_odd | same | ≈ 4(½ − q_odd) | yes (lem:gmono) | **No** |
| −½ − q_ev(T) | D0 + D3 | 2·10⁻⁸ | OPEN | partial (10⁻⁸ ≫ 10⁻⁷⁰ but infimum) |
| 𝔤_ev(T) | PC-2 upper bound | ≲ 9·10⁻⁸ | monotone upper bound (PC-2) | no (upper bound) |
| background of 𝔄_odd | D0 + D3 | **not measured** | yes, nonincreasing (lem:monoT applies to 𝔞 without Tate) | **unknown — measure it** |
| (Ω₀) bending sum | finite | O(1) | no | no (necessary, not sufficient) |
| Weyl radius r_W(T) | D0 | ~λ^W | yes, decreasing | no (ARGUED) |
| λ^W(T) | D0 | ≪ 10⁻⁷⁰ (per MAP_200) | yes (D1) | — |

Reading (revised): the scalar capacities q_par do **not** separate out a smaller scale: ½ − q_odd ≍ ‖h_odd‖²λ^W_odd
and the values 10⁻⁴ / 10⁻⁸ are Galerkin upper bounds at ½log3. The smallness of the background passes through to q
unchanged. No row in this table is amplified.

---

## 6. Ranking of the weakenings with content (revised)

None amplifies the scale of the sign. Order by usable structural content:

1. **K2 (Lemma W3, Kreĭn up to T₀)** — existing positive object ℰ_T, decreasing chain; no new scale.
2. **K1/K4 (de Branges/Douglas up to T₀)** — canonical Hamiltonian ⪰ 0 for t ≤ T₀; no scale.
3. **K11 (Lemma W1, Cor W1′)** — reformulation of lem:gmono in q; useful only as a change of variable. **Not the
   best row by scale:** its margin is the per-sector background.
4. K12 (affinity in t up to T₀) — trivially PROVED.

### First exact lemmas

**(L-a) Measurement at ½log15 of the odd channel's constants.** Compute ℓ(e_odd), ‖h_odd‖ and q_odd at T = ½log15
(e_odd background vector of W_odd; h_odd = 𝔄_odd⁻¹χ_odd/q_odd). Goal: fix the constant in
½ − q_odd ≍ ‖h_odd‖²λ^W_odd and verify the prediction ≲ 10⁻⁶⁵/ℓ(e)². NUMERICALLY strictly necessary: decides
whether any large ‖h_odd‖² factor remains (the only place an amplification could hide) or whether the question is
closed. Label: OPEN.

**(L-b) Consumption rate of q_odd via Schur on the annulus T<|t|<T′.** **NO-GO (TRANSFER, restriction 11 of
SYNTHESIS_MECHANISM_001):** this is the R6/T6.2 route from POLAR_CAP (variation of the polar capacity) with q
instead of 𝔤; r contains 𝔄_{11}⁻¹χ_T, a functional of the window resolvent (𝒦_H). Do not retry.

**(L-c) Monotonicity of the even channel via fixed inertia.** OPEN; likely NO-GO due to the negative eigenvector
crossing (lem:monoT does not control v_−).

---

## 7. Does this bring us closer to the sign? (honest answer)

**No.** What is PROVED in this pass is: (i) Lemma W0 — formally explains why the «up to finite T» weakenings of the
22 TRANSFER entries are equivalent to the datum or empty (it was not an error of phase 204 to dismiss them); (ii)
Lemma W1 / Cor W1′ — PROVED, but they are lem:gmono rewritten in q, and the odd margin ½ − q_odd is ≍
‖h_odd‖²λ^W_odd, not an amplified quantity; (iii) Lemma W3 — up to T₀ positive Kreĭn extensions exist (CITED), with
no amplification. No row produces a polynomial-scale signed quantity at ½log15, nor a lower bound beyond T₀; every
continuation in T remains under W2/Cor 2′. The only thing left open is (L-a), a measurement that can only confirm
or close off the absence of amplification in the odd channel.

## 8. For the index (ROUTES-TRIED-INDEX)

- «Weakening the hypothesis of the 22 TRANSFER entries to positivity up to ½log15»: 11 equivalent to the datum, 6
  empty (Lemma W0, D8), 5 with structural content; **none amplified** (odd channel of prop:WT: ½ − q_odd ≍
  ‖h_odd‖²λ^W_odd; Lemma W1 = lem:gmono in q). Do not retry by weakening K3, K5, K7, K7b, K8, K9, K10, K31–K38, G3;
  (L-b) NO-GO (TRANSFER, restriction 11). Alive: (L-a) (measurement); (L-c) likely NO-GO.
