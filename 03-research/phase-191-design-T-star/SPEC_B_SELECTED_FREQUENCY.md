# SPEC_B — Design direction B: "the missing estimate itself" at a selected frequency / at integer resolution e^{2T}

Design round, no construction. no
equivalence between row D and any other statement is used, invoked or mentioned.
NO-GO / NUMÉRICO. P46 = 04-papers/46-row-d-dual-certificates/main.tex; 188/ = phase-188-closing-D; 190/ = phase-190-near-coincidence-experiment;
SHAPE = 190/memos/SHAPE_THEOREM.md (operations O1–O15, clauses A1–A17, B1–B8, admissible region §3(e)); crossword = CROSSWORD-TO-D §3.2–3.3
((α)–(θ), (ι)–(μ)); index = ROUTES-TRIED-INDEX (README, 04_ Part I, 06_ R1/R5/R9/R10).

Corpus check: SHAPE §1–§5; crossword §3.1–3.3; index README, 04_ Part I-a/b/c, 06_ (R1, R2, R5, R7, R9, R10, "(E_θ) one-frequency
BV (968)"); P46 sec:combs (lem:polarelim, prop:sharp, prop:Egamma-exact, prop:boundary, rem:critical, thm:kappa, thm:ceiling, lem:reson, prop:nearfree,
rem:boxes, thm:band, thm:poisson, thm:oneprofile, prop:AM), sec:open (N), (S), prop:wit-coh, prop:wit-cheb, rem:wit-cheb, prop:wit-sens, thm:margin,
cor:margin1; 188/N_BUILD_013, N_BUILD_021, L2_BUILD_019, L2_BUILD_020, L2_BUILD_030; 190/EXP_002 §3, EXP_003 §2–§4 (Fact N2, identity C3), EXP_005 §5–§6.
**No sign is certified here; nothing below moves λ_A(T) for ζ.**

---

## 0. Verdict in one paragraph

**NOT ADMISSIBLE as specified.** An individual, signed, power-saving bound "at a selected frequency" admits exactly three consistent
formalizations, and each one fails a clause of the brief: (i) at one fixed frequency γ it is the exact limit statement (E_γ) of
prop:Egamma-exact, which has **no power-saving slack** (B2b: the packet limit equals m^♯(γ); the constant-weakened version collapses to it,
188/N_BUILD_013) and, by Hardy–Riesz (CITED), is a **half-plane summability statement** about −2ζ′/ζ − 2/(s−1), hence violates (λ) (it must hold on
all of Γ_S(F)) and (κ) in content; (ii) pointwise in ω on the Nyquist mesh with no correlation to P_T it is **false for ζ** (the symbol σ_T is negative on
U_T ≠ ∅, P46 subsec:band, thm:nolocal); (iii) correlated with the admissible samples |F̂(ω_k)|² on the whole mesh it is (N), an **exact restatement of
row D** (B8). The only object the direction genuinely produces is the fixed-family statement T*₃(η) of §1.3 (problem (S) on the phase-190 family
s_w = m^{−½}w(m/M)), for which the comb collapses exactly through Λ∗1 = log and the sign becomes a lattice (Poisson-on-ℤ) statement; it is admissible
as a *target* but it is REF-D whenever the family contains the A_M-minimizer (NUMÉRICO: it does, 190/EXP_005 §5), and it is not a "theorem between
Vinogradov–Korobov and Bombieri–Vinogradov": no twisted prime sum survives in it. Details, clause table and the honest accounting of where
ℤ-integrality, the Euler product and the functional equation would enter are below. The round stops here, as the mandate requires.

---

## 1. The statement T* — three nested forms

### 1.0 Objects (P46 notation)
X := e^{2T}; 𝒩_T = {n ≥ 2 : n < X}; v_n = 2Λ(n)n^{−½}; m(τ) = Re ψ(¼+iτ/2) − log π; m^♯ = m + (¼+τ²)^{−1};
𝔞_T(F) = (1/2π)∫[m − Σ_{𝒩_T} v_n cos(τ log n)]|F̂|²; P_T = {A(F) = B(F) = 0}; 𝔞^♯(F) = (1/2π)∫m^♯|F̂|²;
𝓕_T(F) = Σ_{𝒩_T} v_n Re c_F(log n) − 2∫_0^{2T}Re c_F(u)e^{u/2}du = 2∫_{[1,X)}y^{−½}c_F(log y) d(ψ(y)−y) (prop:wit-cheb).
Twisted sharp-cutoff fluctuation at frequency ω:
  E_X(ω) := Σ_{n<X} v_n cos(ω log n) − Re[2(X^{½+iω} − 1)/(½+iω)]  (= −4T·𝒞_T(ω), P46 prop:wit-coh).
Nyquist mesh ω_k = πk/(2T). Row D in mesh form (prop:wit-coh(i) + lem:polarelim), PROVED in P46:
  (N)  ∀T ∀F ∈ P_T:  (1/4T) Σ_k |F̂(ω_k)|² E_X(ω_k) ≤ 𝔟_T(F)  (= 𝔞^♯(F) on P_T).
Required strength: exponent ½ at resolution X, i.e. E_X(ω) = O(1)-size oscillation per unit log-interval with the sign fixed
against the archimedean level after correlation; margin: λ_A(T) ≤ 4·10⁹Te^{−15.449T} (cor:margin1), limsup λ_A ≤ 0 (thm:margin).

### 1.1 T*₁ — one selected frequency γ (packet form)
**Statement.** Fix γ ∈ ℝ. With F_T = F_T^γ the spectral-derivative packets (P46 §wit), 
  T*₁(γ):  limsup_{T→∞} 𝓕_T(F_T)/‖F_T‖² ≤ m^♯(γ).
This is (E_γ) in exact form (prop:Egamma-exact, PROVED equivalent to prop:wit-Egamma's (E_γ)). Its prime-side reading (rem:critical, N_BUILD_013 §1):
𝓕_T(F_T)/‖F_T‖² is a Riesz-type mean of Re Σ 2Λ(n)n^{−½−iγ} minus its polar part, and m^♯(γ) = Re[−2ζ′/ζ − 2/(s−1)](½+iγ) is the boundary value
(prop:boundary). **Required strength:** exactly exponent ½ with the exact constant: the one-sided inequality is, by N_BUILD_013 §3 (CONDITIONAL on
Hardy–Riesz CITED + ARGUED divergence alternative), equivalent to *convergence* of the means to m^♯(γ). So there is no "power saving" to prove: the
statement is an equality in the limit. **Compatibility with the margin:** none needed — T*₁ carries no margin at all; (E_γ,C) ⟺ (E_γ) ∀C ≥ 0.
**Uniformity in T:** T*₁ is a limit statement; by B2e no approximate version in T is weaker.
**Why it fails the brief:** B2b (no slack at any frequency: nothing between "exact" and "false"); (λ) (a single γ never decides a window: the witness
frequency is not determined by the window, R169_091); and, in content, summability at one point s₀ = ½+iγ is a half-plane statement about
−ζ′/ζ − 1/(s−1) (Hardy–Riesz, CITED; N_BUILD_013 §2), so T*₁ is of zero-free-half-plane type — the type that (κ) and R10's criterion exclude from the
*proof*, and that R186_050 §4.3 / N_013 Prop 3.3 classify as zero-side. Index: R5 (E_γ), admissible direction "exponent-½ signed twisted ψ bound at γ"
— T*₁ is that direction stated exactly; it is already recorded, OPEN, not a retry here. Dead sub-routes of R5 (constant weakening, large sieve, VK)
are not reused.

### 1.2 T*₂ — selected frequencies at integer resolution: the mesh
**Pointwise form (false).** ∀T ∀k: E_X(ω_k) ≤ 4T·m^♯(ω_k) + (aliasing) would be pointwise positivity of the polar-free symbol; it **fails for ζ**:
U_T ≠ ∅ (P46 subsec:band), κ = 1 < κ⋆ (thm:kappa(iv): g₁(0) = C₀+4 < 0), and thm:nolocal (W-loc). So no signed individual bound at a selected
mesh frequency, without correlation to P_T, is true. PROVED in the record.
**Correlated form.** Any signed bound of the shape E_X(ω_k) ≤ 4T·β_T(ω_k) with Σ_k|F̂(ω_k)|²β_T(ω_k) ≤ 𝔟_T(F) ∀F ∈ P_T is exactly (N): the family
of admissible sample sequences (|F̂(ω_k)|²)_k, F ∈ P_T, is what defines the sign (SHAPE Cor. (c): first variation = −c_{h*}(log n), R186_051 Thm 4.1).
Hence T*₂ := (N) ⟺ row D (B8, L2_BUILD_006). It is admissible as a target (index 06_ R1) and is the target. It is not an estimate that "existing
theorems partially give"; see §2.
**Selecting one mesh frequency** ω_{k₀} and letting T → ∞ with |F̂|² concentrating there gives the packets, i.e. T*₁. There is no fourth option:
frequency selection either concentrates (→ T*₁) or correlates over the mesh (→ T*₂). ARGUED (N_BUILD_013 §5: families with weakly convergent
spectral measures coincide with (N) or are critical; non-convergent families are R3, not a frequency selection).

### 1.3 T*₃(η) — selected vector at integer resolution M ≍ e^{2T}: problem (S) on the smooth-cutoff family
This is the formalization that the brief allows ("the explicit family s_w = m^{−½}w(m/M) from phase 190") and the only one in this direction that is
not already T*₁ or T*₂ by inspection.
**Setting** (P46 subsec:oneprofile, prop:AM; 190/EXP_005 §5). Profile F₀ with |b| > ½ and **2T₀ < ½log 2** (so that lags |d| ≤ 2T₀ carry no contact and
the main term of every Ξ(d), |d| > 2T₀, is removed exactly, lem:transl(iii)); c₀ = c_{F₀}; A_M = [B(log m − log k)]_{m,k≤M}; row D ⟺ A_M ⪰ 0 ∀M
(prop:AM(i), PROVED). Family: for η ∈ (0,1) let
  𝒲_η := { w ∈ C^∞[0,∞) : supp w ⊂ [0,1], w constant on [0,η], ‖w^{(j)}‖_∞ ≤ C_j η^{−j} (C_j independent of M) },
  s_w := (m^{−½}w(m/M))_{m≤M},  Q_M(w) := s_wᵀ A_M s_w = (1/2π)∫F̂₀(τ)²|Σ_{m≤M}m^{−½+iτ}w(m/M)|²[m(τ) − Σ_{n<Me^{2T₀}}v_n cos(τ log n)]dτ.
**Statement.**  T*₃(η):  ∀M ≥ 2 ∀w ∈ 𝒲_η:  Q_M(w) ≥ 0.
**Exact lattice form (PROVED, elementary regrouping; the case w ≡ 1 is identity C3 of 190/EXP_003 §4, and 188/N_BUILD_022 §3 / L2_BUILD_030 §1 in other coordinates).**
Writing N = kn in Σ_{m,k}s_m s_k Σ_n v_n c₀(log m − log k − log n):
  Q_M(w) = 𝒜_M(w) − Σ_{2≤N<Me^{2T₀}} N^{−½} D_w(N) E^w_M(N),
  𝒜_M(w) := Σ_{m,k≤M} s_m s_k Arch(log m/k),  Arch(d) := (1/2π)∫ m F̂₀² cos(τd) dτ,
  D_w(N) := Σ_{n|N, n≥2} 2Λ(n) w(N/(nM)),   E^w_M(N) := Σ_{m≤M} m^{−½} w(m/M) c₀(log(m/N)).
For w ∈ 𝒲_η with w ≡ c on [0,η]:
  D_w(N) = 2c·log N − Σ_{n|N, 2 ≤ n < N/(ηM)} 2Λ(n)[c − w(N/(nM))],   and  N/(ηM) < e^{2T₀}/η,
by Σ_{n|N}Λ(n) = log N (Euler product over ℕ, i.e. Λ∗1 = log). **So on 𝒲_η the comb enters only through (a) the exact divisor identity on every
N < Me^{2T₀}, used linearly, and (b) the finitely many values Λ(n), n < e^{2T₀}/η (for η = 0.4, T₀ = 0.15: n ∈ {2,3}; for T₀ = 0.3: n ∈ {2,3,4} — the
"defects at 2, 3, 4" of EXP_003 §3).** No twisted prime sum, no ψ(y) − y, no selected frequency remains in the statement.
**Farey form (PROVED, regrouping by gcd).** With m = ja, k = jb, (a,b) = 1, L_w(a,b) := Σ_{j ≤ M/max(a,b)} j^{−1} w(ja/M) w(jb/M):
  Q_M(w) = Arch(0)·Σ_{a≤M} a^{−1}L_w(a,a) + 2 Σ_{(a,b)=1, b<a≤M} (ab)^{−½} L_w(a,b) [Arch(log a/b) − ½ Ξ_{F₀}(log a/b)],
  Ξ_{F₀}(d) = Σ_n v_n c₀(log n − d) = 2∫y^{−½}c₀(log y − d) d(ψ(y) − y)  (thm:band; main term zero by Tate for d > 2T₀).
(Ξ(−d) = 0 for d > 0 since log n + d > 2T₀ for n ≥ 2.) Here the "selected frequencies" are the rationals a/b: the fluctuation of ψ in the multiplicative
window of relative width e^{±2T₀} around a/b, weighted (ab)^{−½}·log(M/max(a,b)) for flat w. The two forms are the same sum; the first exhibits the
collapse, the second exhibits what the collapse cancels (the Riemann sum over b of Ξ(log a − log b) against b^{−½} is annihilated by the Tate condition
∫c₀(v)e^{−v/2}dv = 0: the "per-atom Tate cancellation for n ≥ 5" observed in EXP_003 §3).
**Required strength.** For w flat on [0, e^{2T₀}/2] the comb is invisible (D_w ≡ 2log N) and Q_M(w) is an explicit lattice-vs-archimedean quantity,
positive with O(1) margin (NUMÉRICO Q_M(1) = 2.58 at M = 800; EXP_005 says provable at PNT level, L2_028 §3 — ARGUED, not re-derived here). For the
minimizing cutoff the margin is λ_min(A_M)‖s‖² ≍ M^{−3}log M (NUMÉRICO, EXP_002/003) while a single 10⁻⁵ change of v₂ moves Q by ≈ 10⁻⁵·O(1):
the inequality is sharp to relative precision M^{−3} in a quantity whose terms are O(log M). This is not "exponent ½": it is exact cancellation on the
extremal cutoff, consistent with B2c/(d) (criticality at integer resolution) and SHAPE Cor. (c) (sign = minimizer-dependent correlation).
**Compatibility with thm:margin.** A_M is the Galerkin section of the window form at T ≈ ½log M + T₀ on the span of translates V_{log m}F₀, m ≤ M;
its bottom M^{−3} (NUMÉRICO) is far above λ_A(T) ≤ exp(−e^{(2−ε)T}) because the P_T-minimizer at window T is not in that span. The doubly exponential
smallness is recovered only in the closure of prop:AM(i)(⇐): fixed lag configuration (a_j), m_j = ⌊e^{C+a_j}⌋, C → ∞ — i.e. spikes of relative width
→ 0, which lie in 𝒲_η only as η → 0. No contradiction; the two margins live on different test sets.
**Uniformity in T.** ∀M with M-independent constants C_j (declared); T*₃ restricted to M ≤ M₁ is a finite statement and decides nothing (A11 analogue).

### 1.4 The fixed-family dichotomy (what T*₃(η) is)
Let v_M be a minimizer of A_M(Λ) on the unit sphere.
(i) If v_M ∈ span-closure of {s_w : w ∈ 𝒲_η} for every M, then T*₃(η) ⟹ A_M ⪰ 0 ∀M ⟹ row D (prop:AM(i)); conversely row D ⟹ T*₃(η). **PROVED
modulo the hypothesis**; the hypothesis holds NUMÉRICO for η ≈ 0.3–0.4 (EXP_005 §5: v_M = m^{−½}w_M(m/M) + ≤ 0.4 % noise, w_M ≈ 1 on [0,0.4],
decreasing to ≈ 0.2 at 1, stable in m/M). In that case T*₃(η) is an **exact restatement of row D** (REF-D; B8).
(ii) If v_M ∉ that closure along a sequence of M, T*₃(η) is strictly weaker (necessary only). Whether it then still separates ζ from the falsifiers of
A1/A2/A5 depends on whether their negative directions lie in 𝒲_η: NUMÉRICO (EXP_002 §3) they are top-scale packets of relative width O(1), which
are in 𝒲_η for η ≲ 0.2; so for such η, T*₃(η) is false for Λ·1_{n≥3}, Λ·1_{n≥5}, Λ + cδ₂ (c large) and v₂ ± 10⁻⁵ (M ≥ 200–400) — a ζ-specific
necessary condition — but it is not a statement that closes row D.
There is no choice of η (or of any fixed family) that is simultaneously strictly weaker than D and sufficient for D. This is the structural reason the
direction cannot deliver "the missing estimate" as a theorem weaker than the target. ARGUED (the two halves are each PROVED or NUMÉRICO as marked).

---

## 2. Decomposition: what existing theorems give, and the residual C*

### 2.1 Existing inputs, each with its exact reach (all CITED unless marked)
| input | reach for T*₁ | reach for T*₂ = (N) | reach for T*₃(η) |
|---|---|---|---|
| Explicit formula (P46 lem:roughEF; thm:Z) | identity: 𝓕_T(F_T) = zero sum; sign in Σ_ρ (A17, zero-side) | identity only; = certificate content (B8) | identity Q_M(w) = Σ_ρ Φ(ρ)Φ(1−ρ)-type; no sign |
| Tate / polar elimination (lem:polarelim, lem:transl(iii), double zero of ĉ₀ at ±i/2) PROVED | removes polar part exactly; threshold m^♯ | 𝔟_T = 𝔞^♯ on P_T | main term of every Ξ(log a/b) and the first-order term of Σ_N D_w E^w_M vanish exactly; what is left is a Poisson-dual (lattice) sum |
| Λ∗1 = log (Euler product over ℕ) PROVED | nothing (single frequency) | nothing beyond identities (W7) | the collapse D_w(N) = 2c log N − small-divisor defects: the comb disappears except at n < e^{2T₀}/η (§1.3) |
| Euler–Maclaurin / Poisson summation on ℤ (standard) | — | — | E^w_M(N) = N^{½}Φ_w(N/M) + Σ_{ℓ≠0} f̂_N(ℓ), Φ_w(x) = ∫e^{v/2}c₀(v)[w(xe^v) − w(x)]dv; the main-term bookkeeping of Q_M(w) (not written out; ARGUED) |
| Ramanujan-sum / additive-character split (188/L2_BUILD_030 §3) PROVED identity | — | — | organizes the Poisson-dual tail by prime-power moduli; identity, no sign |
| PNT with VK error (rem:wit-cheb) | gives e^{T−c(2T)^{3/5}…}: useless | useless (R1 row 1) | not needed: no ψ−y remains on 𝒲_η; for η → 0 it re-enters through the divisor defects at scale M and is then useless at precision M^{−3} |
| Bombieri–Vinogradov / large sieve / Montgomery–Vaughan | mean in moduli / mean square in ω: no sign at one γ (W4, W-sieve) | no pointwise sign (rem:wit-cheb; I6) | class input only (N_BUILD_021 Thm 2 → cor:void); never enters the exact form |
| Matomäki–Radziwiłł | o(·) for bounded multiplicative functions; Λ unbounded; exact constant needed | same | not applicable (no short-interval prime sum remains) |
| Selberg's lemma for ζ′/ζ near the line (N_BUILD_013 §4c) | identity; sign carried by the zero term | same | — |
| twisted second moments of ζ with Dirichlet polynomials (literature; CITED-type, not in corpus) | — | — | wrong regime: Q_M(w) is a second moment of a length-M partial sum at height O(1) (F̂₀² ∼ τ^{−4}) twisted by a comb of length Me^{2T₀} > height; main terms cancel by Tate; error terms are relative power savings in height, not M^{−3} |
| prop:nearfree / rem:boxes PROVED | — | — | positivity with margin c₀ for all b on the resonator profile ε ≍ 1/M (near-coincidences invisible); T*₃ is the complementary case: fixed-width F₀, Near visible on every s_w |
| thm:band, Thm T (L2_023), Thm L (N_015) PROVED | — | — | each 2×2 section of A_M is the band |Ξ(d)| ≤ 2a₀ (necessary); Ξ oscillates about 0 unconditionally: no termwise sign |
| thm:ceiling, thm:kappa PROVED | — | — | density of Λ is 1 < κ⋆: the main term cannot pay; consistent with its exact cancellation here (B2d) |

### 2.2 The residual conjecture C*
For T*₁: C*₁(γ) = convergence of the Riesz means of Re[−2ζ′/ζ − 2/(s−1)] at ½+iγ to m^♯(γ). Supplies (γ) formally (exponent ½ with exact
constant) but is a half-plane statement in content (Hardy–Riesz): it does not supply (δ) and fails (λ), (κ). Not new: it is R5.
For T*₂: C*₂ = (N) itself. Not new: R1.
For T*₃(η): 
  **C*₃(η):  ∀M ≥ 2 ∀w ∈ 𝒲_η:   Σ_{N<Me^{2T₀}} N^{−½} D_w(N) E^w_M(N)  ≤  𝒜_M(w),**
with both sides explicit (§1.3). In Poisson-dual coordinates the left side is a two-dimensional lattice sum Σ_{m,N} m^{−½}N^{−½}w(m/M)D_w(N)c₀(log m/N)
whose continuous main term and first-order term vanish by the Tate conditions, so the inequality compares (dual terms (ℓ₁,ℓ₂) ≠ (0,0) of the
ℤ²-Poisson expansion of a degree-(−1) homogeneous kernel) − (small-divisor defects Σ_{n<e^{2T₀}/η} 2Λ(n)[c − w(·)]·1_{n|N}) against the archimedean
energy 𝒜_M(w). **What is new in it:** it supplies (δ) (primes, as divisibility of every N < Me^{2T₀}, coupled to the archimedean energy in one
inequality) and (θ) (ℤ-integrality enters as Poisson summation on ℤ² and as the divisor structure n | N); it does **not** supply (γ) as a twisted-sum
bound — no twisted prime sum remains; by I13 (N′ circularity, PROVED for single tests and power families, ARGUED in general) its content, if it is
REF-D, is still an O-bound of exact strength, now hidden in "∀w ∈ 𝒲_η, ∀M". **Not a retry:** R1's dead table (absolute ψ bounds, large sieve,
bounded functionals, sieve majorants, Möbius transport termwise (N_006), Euler cones, SOS, exterior certificates, 2×2 sections, Poisson comparison) —
none is used; N_021 Thm 2 (progression classes) — not used, and T*₃ as a statement is NUMÉRICO-false for the finite modifications, so no closed
class could prove it; W-sieve — no sieve; cor:void — the proof would use Λ∗1 = log on every N exactly, which every finite modification breaks;
R9 dead rows "exact matrix identity from 1∗Λ = log beyond divisors (N_022: Near is a discretization defect)" and "Near as a separate signed
operator (L2_030)" are the *inputs* of §1.3, not retried; EXP_005 §6 names the bulk/edge split of Q_M(w) as the next step and it has not been done.
**Status of C*₃:** OPEN. By §1.4, for η ≤ η₀ (NUMÉRICO η₀ ≈ 0.3–0.4) it is REF-D; for η > η₀ it is a necessary condition that does not close D.

---

## 3. Clause-by-clause compliance

Convention: the operations O_i act on deduction classes (SHAPE Thm S (A)); for a *statement* the question is whether a hypothetical proof of it can
lie in a class closed under O_i, and whether the statement itself is invariant under O_i (if it is, a class proof is not excluded by that O_i but the
statement then does not carry ζ's sign). "✓" = escapes / complies; "✗" = fails; "REF-D" = complies because it is D.

| clause | T*₁(γ) | T*₂ = (N) | T*₃(η), C*₃ |
|---|---|---|---|
| A1 (O1 finite deletion) | statement shifts by a bounded amount (N_013 §3): invariant up to O(1) but the limit is exact, so class proofs via PNT-type inputs are excluded (cor:void) ✓ | REF-D | identity Λ∗1 = log fails on the bulk ⇒ statement changes; NUMÉRICO false for Λ1_{n≥3}, Λ1_{n≥5} at M ≤ 400 (EXP_002) ✓ |
| A2 (O2 one-term amplification) | same ✓ | REF-D | D_w changes on every N with n₀ | N; NUMÉRICO false for Λ + cδ₂ ✓ |
| A3 (O3 tail deletion) | the tail is the whole content of a limit statement ✓ | REF-D | Λ∗1 = log fails for N with a divisor ≥ n₀ ✓ (sign of the change not located, as in A3) |
| A4 (O4 rescaling) | cΛ changes the limit by factor c: not invariant ✓ | REF-D | D_w ↦ cD_w ✓ |
| A4ε, A5 (O4ε, O5 ε-perturbations) | invariant to O(ε): a proof must be exact ✓ (B2b) | REF-D (CONDITIONAL κ_T ≠ 0) | NUMÉRICO: v₂ ± 10⁻⁵ makes A_M indefinite on packets ∈ 𝒲_η from M ≈ 200–400 ✓; CONDITIONAL in general (A5) |
| A6 (O6 Beurling) | Beurling systems have their own Riesz means; the statement is not ℕ-specific ✗ (statement is of class type unless the exact constant m^♯ is used) | REF-D | s_w, Poisson on ℤ and Λ∗1 = log on ℕ are not defined for a generalized-integer semigroup ✓ (the ℕ-lattice is the separating property) |
| A7 (O7 a_P) | a_P keeps Euler over ℕ; its Riesz means at ½+iγ differ by a finite Euler factor: statement not invariant ✓ | REF-D | Λ∗1 = log fails on every N with a prime factor < P ✓ (whether T*₃ is false for a_P at M e^{2T₀} < P is OPEN: the negative archimedean tests of cor:Tarch are not known to lie in 𝒲_η) |
| A8a (O8 quartets M_m, exact comb kept) | packets see the quartet term growing like e^{2δT}/T (prop:wit-Egamma): statement false for M_m ✓ | REF-D | the lattice matrix of M_m is A_M − k[Q_z(V_{log m}F₀, V_{log k}F₀)] ≠ A_M; a proof that computes with q = Arch − comb explicitly uses the absence of the quartet summand, i.e. ζ's own form, not a shared property ✓ ((e)1) |
| A8b (O8 f_t) | f_t's comb is not on log ℕ; its packet limit differs ✓ | REF-D | f_t has no Λ∗1 = log on ℕ ✓ |
| A8c (O8 ζ̃ = ζR) | the means at ½+iγ see the four off-line poles ✓ (ARGUED, as A8c) | REF-D | ζ̃ has no Euler product; the collapse fails ✓ |
| A9 (O9 Epstein/DH) | no Euler product: no Riesz-mean identity with m^♯ ✓ | REF-D | no Λ∗1 = log ✓ |
| A10 (O10 ξ_K) | — (OPEN falsifier) | REF-D | the separating property is named: comb on log ℕ, test lattice ℤ, Poisson on ℤ (for K ≠ ℚ the ideal lattice and Poisson on 𝒪_K differ) ✓ (names it; nothing more is claimed) |
| A11 (O12 bounded windows) | limit statement ✓ | REF-D | ∀M with M-uniform C_j declared ✓ |
| A12 (O13 symbol truncation) | not a criterion on U_T ✓ | REF-D | not a criterion on U_T ✓ |
| A13 (O14 bounded form perturbations) | exact limit, no O(1) tolerance ✓ | REF-D | exact at M^{−3} precision; not a moment/norm/determinant criterion ✓ |
| A14 (patterns) | not a pattern ✓ | REF-D | not a pattern ✓ |
| A15 (progression/sieve classes) | not used ✓ | REF-D | not used; N_021 Thm 2 respected ✓ |
| A16 (O15 Poisson randomization) | random positions have no Riesz means of a Dirichlet series with boundary value m^♯ ✓ | REF-D | Λ∗1 = log and the ℤ-lattice are destroyed ✓ |
| A17 (zero information) | **✗ in content**: summability at ½+iγ is a half-plane statement (Hardy–Riesz); the statement is of zero-side type (R186_050 §4.3) | REF-D | the statement is prime-side (comb, lattice, Arch); the zero-annihilation of P_w (Fact N2) is descriptive only ✓ |
| B1 (margin) | no margin exists (B2b) — consistent, but it means no "power saving" is available ✗ for the brief's framing | REF-D | polynomial margin M^{−3} on the lattice section (NUMÉRICO), doubly exponential only in the η → 0 closure (§1.3) ✓ |
| B2a (centre) | γ = 0 is L2_010: exact ✓ | REF-D | Arch(0) = 𝔞(F₀) enters the diagonal; polar main term removed by Tate ✓ |
| B2b (packets critical) | **✗: T*₁ is the critical equality itself; nothing to save** | REF-D | makes no packet statement; spectral weight F̂₀²|P_w|² covers all τ ✓ |
| B2c (integer resolution critical) | single frequency ✗ (discards all other bands) | REF-D | all frequencies up to M present (P_w has length M); F̂₀² ∼ τ^{−4} weights them; the M^{−3} law is attributed to the tail τ ≳ cM (Fact N2, NUMÉRICO) ✓ |
| B2d (density ceiling) | polar part removed exactly ✓ | REF-D | main term cancels exactly by Tate; sign in dual (fluctuation) terms ✓ |
| B2e (no asymptotic slack) | limit statement, no ε(T) ✓ | REF-D | ∀M ✓ |
| B3 (FE antisymmetry) | not a σ-transport ✓ | REF-D | not a σ-transport ✓ |
| B4 (operator calculus linear) | — | REF-D | the collapse is a linear identity in Λ (W7 class); the sign step is inf over w ∈ 𝒲_η of an explicit form: not identity + Cauchy–Schwarz ✓, but not shown non-linear in Λ either (see (β)) |
| B5 (no arithmetic SOS) | — | REF-D | no SOS proposed ✓ |
| B6, B7 | N/A ✓ | REF-D | N/A ✓ |
| B8 (no weaker substatement) | T*₁ is weaker than D (necessary) but is R5, already listed; not a new substatement | T*₂ ⟺ D | T*₃(η ≤ η₀) ⟺ D (§1.4(i), CONDITIONAL on NUMÉRICO N2′); T*₃(η > η₀) strictly weaker and not sufficient. Complies with B8 in the sense B8 predicts: nothing weaker that closes D ✓/REF-D |
| (α) individual property of Λ on ℕ | the boundary value m^♯(γ) is ζ's; distinguishes from M_m, f_t ✓ | REF-D | Λ∗1 = log on ℕ + ℤ-lattice ✓ |
| (β) non-linear in Λ, non-polynomial in the test | linear in Λ (a Dirichlet series) ✗ | REF-D | linear in Λ in the collapse (W7); the only non-linearity is the infimum over 𝒲_η ✗ as a statement about the *estimate* |
| (γ) upper bound on Σ_{n≥X}Λ(n)n^{−½−iγ_q}w beyond the window, exponent Θ−½ | supplied in form (exponent ½, exact constant) but with zero slack: it is the statement, not an estimate ✓/✗ | REF-D | **not supplied**: no twisted sum remains; absorbed into "∀w ∀M" ✗ |
| (δ) couples primes with ∞ without being D | couples via m^♯(γ) = boundary value: but is zero-side in content ✗ | ✗ (is D) | couples D_w with 𝒜_M(w) ✓; "without being D" ✗ for η ≤ η₀ (REF-D), ✓ for η > η₀ (then necessary only) |
| (ε) not a Sonin/Δ norm bound | ✓ | ✓ | ✓ |
| (ζ) not a sieve / measure-in-γ / uniform-in-γ bound | ✓ (one γ, exact) | ✓ | ✓ |
| (η) not inertia | ✓ | ✓ | ✓ |
| (θ) integrality of multiplicities and of ℤ | ✗ (not used) | REF-D | ✓ Poisson on ℤ², divisor structure n | N, exact small values Λ(2),Λ(3),Λ(4) |
| (ι) no margin | ✓ (none) | ✓ | ✓ (M^{−3} is the observed, not assumed, precision) |
| (κ) no zeros | ✗ in content (half-plane summability) | ✓ | ✓ |
| (λ) valid on all Γ_S(F) | ✗ (one γ) | ✓ | ✓ (∀w) |
| (μ) global in X | ✓ (limit) | ✓ | ✓ (∀M) |

**Failures admitted.** T*₁: B2b, B2c, A17/(κ) in content, (β), (θ), (λ). T*₂: none, because it is D (B8): it is not an estimate. T*₃: (γ) not supplied,
(β) not satisfied as an estimate, (δ) only as REF-D or as a non-closing necessary condition; A7-falsification of the statement OPEN.

---

## 4. Where ℤ-integrality, the Euler product and the functional equation would enter a hypothetical proof of C*₃ (no proof attempted)

Line 0 (definition of the object). The FE with Γ(s/2) at conductor 1 enters as m(τ) = Re ψ(¼+iτ/2) − log π in Arch(d) and in Arch(0) = 𝔞(F₀); the
pole enters as the polar density 2e^{u/2} and, through P_T, as the Tate conditions A(F₀) = B(F₀) = 0, i.e. the double zeros of ĉ₀ at ±i/2
(F₀ = (¼−∂²)G₀, G₀ ∈ H²₀). These are the only places the FE enters; they are structural (input, not estimate).
Line 1 (collapse). The Euler product over ℕ enters exactly once and linearly: Σ_{n|N}Λ(n) = log N for every N < Me^{2T₀}, giving D_w(N) = 2c log N −
small-divisor defects. This line is W7-class (Λ∗1 = log used linearly) and carries no sign by itself; it removes the large primes from the statement.
Line 2 (main-term cancellation). The Tate conditions kill ∫e^{±v/2}c₀ and ∫v e^{±v/2}c₀: the continuous (Riemann-integral) version of
Σ_N N^{−½}·2c log N·E^w_M(N) vanishes to second order (ARGUED, elementary Mellin computation; not written). This is B2d made exact: the density
pays nothing.
Line 3 (what remains, and the structural fact of ℤ that must carry the sign). After Lines 1–2 the left side of C*₃ is a sum of (a) ℤ²-Poisson-dual
terms of the degree-(−1) homogeneous kernel (m,N) ↦ m^{−½}N^{−½}c₀(log m/N)·w(m/M)·log N — in the Farey picture, the discretization defect of the
Riemann sum over denominators b of Ξ(log a − log b) against b^{−½}, which is exact for b ≥ e^{2T₀}/η and defective for small b — and (b) the
small-divisor defects Σ_{n<e^{2T₀}/η} 2Λ(n)[c − w(N/(nM))]1_{n|N}, i.e. the parity-type statistics of integers N ≍ M (how the multiples of 2, 3, 4 sit
under the smooth weight N^{−½}E^w_M(N)). The structural facts of ℤ that would carry the sign are therefore: **unique factorization in the form
Λ∗1 = log (Line 1); the lattice ℤ² and Poisson summation on it (the near-coincidences m ≈ kn, m ≠ kn, are exactly the nonzero dual frequencies of
the Dirichlet-convolution kernel, L2_BUILD_030 §2–3); and the divisibility pattern of integers near M by the finitely many n < e^{2T₀}/η.** No
near-coincidence enters through a prime fluctuation ψ(y) − y at scale y ≤ M: on 𝒲_η that fluctuation has been traded, by the identity, for the
divisibility pattern. (For η → 0 the trade reverses: D_w(N) then sees divisors n ≈ N/k with k bounded, i.e. primes near M/k, and the Chebyshev
fluctuation at scale M returns — this is EXP_005 §6's "edge", and the M^{−3} requirement makes every PNT exponent useless there, R1 row 1.)
Line 4 (the sign). The inequality "dual terms − defects ≤ 𝒜_M(w)" for all w ∈ 𝒲_η and all M. Nothing in the record gives its sign; its content for
η ≤ η₀ is row D (§1.4). A proof would be a computation with ζ's own data at every M (SHAPE §3(e)1), using Lines 0–3 jointly — the three inputs enter
jointly as the brief demands — but Line 1 is the only Euler-product line and it is linear, so the non-linearity required by (β)/B4 can only sit in
the quantifier over 𝒲_η. No candidate mechanism for Line 4 is proposed here.

---

## 5. Honest verdict

**NOT ADMISSIBLE** (as "the missing estimate itself", individual, at a selected frequency, closing row D).
- Frequency forms: T*₁ fails **B2b** (no slack: the statement is an exact limit, so there is no power saving to prove), **(λ)** and, in content,
  **A17/(κ)** (half-plane summability, Hardy–Riesz); pointwise mesh forms are **false for ζ** (thm:nolocal, U_T ≠ ∅); correlated mesh forms are (N) = D (**B8**).
- Fixed-vector form at integer resolution: T*₃(η) is admissible as a target and is the explicit lattice form of problem (S) on the phase-190 family;
  for η ≤ η₀ it is **REF-D** (CONDITIONAL on the NUMÉRICO fact that the A_M-minimizer is in 𝒲_η), for η > η₀ it is a necessary condition that does
  not close D (§1.4 dichotomy, ARGUED). It does not supply **(γ)**: on 𝒲_η no twisted prime sum survives; the primes act only through Λ∗1 = log
  (linear, W7) and the values Λ(2), Λ(3), Λ(4); the sign is a ℤ²-Poisson/divisibility statement against the archimedean energy. It is therefore not a
  theorem "between Vinogradov–Korobov and Bombieri–Vinogradov"; it is row D written on the integer lattice with the comb collapsed.
- What the direction leaves for the record (not a route, a statement of location): C*₃(η) in §2.2 with Lines 0–4 of §4; the open item is whether the
  A_M-minimizer lies in a fixed 𝒲_η for all M (NUMÉRICO yes; a proof would make T*₃(η₀) a PROVED exact restatement of D in which the only
  prime-side inputs are Λ∗1 = log on ℕ, Λ(2), Λ(3), Λ(4), and the archimedean symbol). No construction is proposed; the round stops.

---

## 6. Self-review
1. T*₁ = (E_γ) exact: prop:Egamma-exact PROVED; the collapse (E_γ,C) ⟺ (E_γ) is CONDITIONAL (N_013), stated so; "half-plane statement" is the
   record's own reading (N_013 §2, Hardy–Riesz CITED) and is used only to classify T*₁, never to say anything about row D's relation to any
   external statement. ✓
2. "Pointwise mesh form false": subsec:band (U_T ≠ ∅) and thm:kappa(iv) are PROVED in P46; thm:nolocal is the class statement. ✓
3. The lattice identity of §1.3: regrouping N = kn in prop:AM(ii)–(iii) with s_k = k^{−½}w(k/M); the N-range N < Me^{2T₀} follows from supp c₀ ⊂
   (−2T₀, 2T₀) and m ≤ M; D_w(1) = 0. The collapse for w ≡ c on [0,η] is Σ_{n|N}Λ(n) = log N split by whether N/(nM) ≤ η. The Farey form uses only
   gcd regrouping and Ξ(−d) = 0 for d > 0 (needs log 2 > 2T₀: declared 2T₀ < ½log2). PROVED, elementary. ✓
4. §1.4(i): if v_M ∈ family then family-positivity gives v_Mᵀ A_M v_M ≥ 0, i.e. λ_min(A_M) ≥ 0; prop:AM(i) closes. The hypothesis is NUMÉRICO
   (EXP_005 §5, double precision, M ≤ 1200); labelled CONDITIONAL. §1.4(ii)'s falsifier-detection is NUMÉRICO (EXP_002 §3). ✓
5. The claims "no twisted prime sum remains" and "primes enter only via Λ∗1 = log and Λ(n), n < e^{2T₀}/η" are exact consequences of item 3 for
   w ∈ 𝒲_η; they are statements about the *form* on that family, not about D's dependence on Λ (Λ = μ∗log, so every statement about Λ is a
   statement about Λ∗1 = log). ✓
6. Line 2 of §4 (second-order vanishing by the double zero of ĉ₀) is ARGUED, not computed; it is not load-bearing for the verdict. ✓
7. No numerics were produced; the NUMÉRICO constants quoted are the record's (190/EXP_002/003/005). No proof attempted. No equivalence with any
   external statement used; "half-plane summability of a Dirichlet series" is a statement about T*₁ itself. ✓
8. Not-a-retry check done against index 06_ R1, R2, R5, R9, R10 dead tables, 04_ Part I W7/W-sieve/cor:void/N_021, and the phase-190 proposed rows;
   the only overlap is intentional (EXP_003 C3 and EXP_005 §6 are the inputs). ✓
