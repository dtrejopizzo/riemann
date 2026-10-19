# AUDIT_L_SHARP_7 — audit of PROOF_L_SHARP_W_001 and SYNTHESIS_MECHANISM_001

Phase 199. ,
no zero location is used as input (zeros appear only as evaluation points in shipped data),
Checked against AUDIT_L_SHARP_6 (constraints 1–18),
MORI15_EXTREMAL_001 (+ shipped `MORI15_EXTREMAL_001_data/`), A_001 (Thm 1.1), C_001 (Prop 1.1–1.2), E_001 (Thm E.5),
V_001, S_001 (S.4–S.5), Guo 4.3–4.5 (as quoted in A_001/C_001). Independent recomputations: scratchpad scripts (double
precision, shipped 120-digit eigenvector, shipped prolate eigenvalues; not stored in the repo).

**Verdict in one line.** W.1–W.4 stand (W.1 needs a ¼-margin fix in M); the caustic formula is a correct WKB computation
and the shipped zero data do peak at n = 71–72 (ARGUED + NUMÉRICO). In the synthesis, **N1 is a tautology** (the unique
element of span{h₀,h₄} with f(0) = 0 *is* Pólya's f_P; the overlap only measures prolate vs Hermite at c = 30π), **M1 is I1
renamed** (no variation is performed), and **"min 𝔴 at the caustic" is built in** (on (1,2) 𝔴 is Θ_∞ of the stationary
frequency, whose minimum is t_c by definition). M3 is not falsified by MORI15 (g* is off-core) but its leading lower bound
½log 2μ = 1.70 already exceeds the data ratio 1.23, so the edge channel must carry ≥ 50 % of the chirp value with the
opposite sign: it is leading order, not a correction. (★★)/L′♯ OPEN. Row D OPEN.

## 1. PROOF_L_SHARP_W_001

**1.1 WKB phase and caustic.** The prolate ODE ((1−x²)ψ′)′ + (χ − c²x²)ψ = 0 gives, for x > 1, ψ″ ≈ −[(c²x²−χ)/(x²−1)]ψ:
local wavenumber κ = √((c²ω²−χ)/(ω²−1)) ✓. Against ξ^{−it}: phase cS(ω) − t log ω, stationary at t = ωκ(ω) ✓. With
x = ω², d/dx[x(c²x−χ)/(x−1)] = (c²x² − 2c²x + χ)/(x−1)², single critical point x* = 1 + √(1−χ/c²) (a minimum) ✓; χ = 0 gives
x* = 2, t = 2c ✓; expansion t_c = 2c − χ/(2c) + O(χ²/c³) ✓. Recomputed: χ = 9c ⇒ t_c = 183.883 (ω* = 1.3968, not √2);
with the true χ₄ = 837.338 (shipped `prolate_eigs`) ⇒ **t_c = 183.943**. **ARGUED** (WKB; the identification of the
dominant exterior wave as the ψ₄ continuation is MORI15's, NUMÉRICO). Not a proof that Φ_ℓ is "smaller than any power" below
t_c: Airy-dark decay is in (t_c − t)/c^{1/3} and the n ≥ 2 and gauge components are not controlled — ARGUED.

**1.2 Peak in the data (NUMÉRICO, shipped logs re-read).** Even: |Fg*(γ_n)| = 9.3, 9.2, 8.4·10⁻³⁷ (n = 68–70), **3.63·10⁻³⁶,
4.64·10⁻³⁶ (n = 71, 72; γ = 184.874, 185.599)**, 2.23, 1.35, 2.41, 2.65·10⁻³⁶ (73–76). Odd: 1.41, 1.36, 1.18·10⁻³⁴ (68–70),
**4.78, 5.99·10⁻³⁴ (71, 72)**, 2.74, 1.53·10⁻³⁴. Confirmed: same zeros, both sectors, on the bright side of t_c. Caveats:
(a) zero spacing ≈ 1.5 is the resolution, so t_c = 183.9 and 2c = 188.5 are only marginally distinguished (peak lies between);
(b) the "dark side" is only a factor 4–5 below the peak at n = 68–70; SYNTHESIS §1.3's "≤ 10⁻³⁸ below t*" is **wrong**
(data: up to 9.3·10⁻³⁷ at n = 68); MORI15's "10⁻⁶⁸…10⁻³⁸" refers to n ≲ 60. Label: t* = caustic **ARGUED, NUMÉRICO-
consistent** (one μ, one peak). The NO-GO for counting identities is correct (elementary).

**1.3 Thm W.1.** Steps checked: discs of radius ¼ about ρ (0 < Re ρ < 1, CITED classical) lie in −¼ < σ < 5/4 ✓ (band is
right; it is the minimal symmetric band for radius ¼); sub-mean-value |F(ρ)|² ≤ (16/π)∫_{D_ρ}|F|² ✓; ∫_strip|F|² =
2π∫‖F‖²_σdσ ≤ 3π sup_σ‖F‖²_σ ✓ (definition, Plancherel not needed); 16/π·3π = 48 ✓. **Fix:** a point s with Im s = t lies
in D_ρ only if |γ − t| < ¼, and for |γ| ≤ t* one has |t| ≤ t* + ¼; M must be max over |t| ≤ t* + ¼ (immaterial for
O(log t*)). Multiplicity is consistent on both sides. M(t*) ≤ N(t+¼) − N(t−¼) + (boundary) = O(log t*) by Riemann–von
Mangoldt with an explicit S(T) bound (Trudgian 2014) — **unconditional, uses only zero counting and 0 < Re ρ < 1**. No
separation, no location. **PROVED** (with the margin fix).

**1.4 Cor W.2.** Convention check (C_001 (b)–(c)): Φ_ℓ(s) = ∫_{−∞}^{−T}H(e^y)e^{sy}dy with H(e^y) = e^{−y/2}Ψ_f(y) = O(e^{y})
(A_001 (a): Ψ_f = O(e^{3y/2})), so Φ_ℓ is holomorphic on Re s > −1 and (1/2π)∫|Φ_ℓ(σ+it)|²dt = ∫|H|²e^{2σy}dy, decreasing
in σ on y < 0; sup = value at σ = −¼ = ‖ℓ‖²_* < ∞ ✓. Gauge infimum legitimate (Φ_ℓ(ρ) = −Φ_g(ρ) depends on g only) ✓.
**PROVED.** The link ‖Zr‖_* ≲_μ ‖r‖ to ℓ(g) is OPEN (C_001 only has the reverse comparison) — agreed. It is a *weak*
inequality: on g* both sides are O(10⁻⁷⁰) and it carries no sign.

**1.5 Cor W.3.** ρ ↦ 1−ρ preserves multiplicity; |ab| ≤ ½(|a|²+|b|²) gives |Σ m Φ(ρ)Φ(1−ρ)| ≤ Σ m|Φ_ℓ(ρ)|² ✓. The log-weighted
version needs W.1 *localised* to unit blocks (same proof, local M) — stated loosely but correct. **PROVED** (upper side,
no sign).

**1.6 Prop W.4.** f admissible supported in (−1/λ,1/λ): Σf(ne^x) = 0 for e^x > 1/λ ⊃ window, so g = 0, Φ_ℓ = ζf̃ vanishes
at every zero, ℓ ≠ 0 ✓. **PROVED.** (It is the AUDIT_199 gauge falsifier read on the Mellin side.)

**1.7 REF-D stop (iii).** For real g, Φ(s̄) = conj Φ(s); for Re ρ = ½, Φ(ρ)Φ(1−ρ) = |Φ(ρ)|². Hence pair form − Σ w_ρ|Φ(ρ)|²
(any diagonal Gram weights with w_ρ = 1 on the line) is supported on off-line pairs. This is pure algebra, holds whatever
the zero set is, and assumes nothing about locations ✓. The conclusion "a Gram comparison is the target restated" is a
correct REF-D classification of *this* route (not a statement about the target's truth). **PROVED algebra; stop justified.**
The BRS "not a Riesz basis / log-n part = comb" is CITED/ARGUED as labelled (W.4 does prove zeros alone are not sampling).

## 2. SYNTHESIS N1 / N2

**2.1 Definition.** Φ(u) = 2Σ(2π²n⁴e^{9u/2} − 3πn²e^{5u/2})e^{−πn²e^{2u}} is the classical Riemann–Pólya kernel (Titchmarsh
§2.16; Ξ(t) = ∫Φ(u)cos(ut)du, Φ even) ✓, and e^{u/2}Σf_P(ne^u) with f_P = (2π²v⁴ − 3πv²)e^{−πv²} reproduces it ✓, so
Φ = 2Ef_P. f_P is *not* "the E-image of the Gaussian": it is the Hermite combination ½(x⁴ − 3x²)e^{−x²/2}, x = √(2π)v,
= (H₄ − 12H₀)/32 · e^{−x²/2}; f_P = f̂_P, f_P(0) = 0, ∫f_P = 3/2 − 3/2 = 0 ✓ (radical).

**2.2 Recomputed (NUMÉRICO).** 3000-node GL on I, shipped vector: ‖g*‖² = 1 − 10⁻¹³; ⟨g*, Φ/‖Φ‖_I⟩ = **−0.999812**;
‖g* + Φ̂‖² = **3.752·10⁻⁴**; pointwise (x = 0, 0.2, 0.5): −1.5985/1.5799, −1.0696/1.0762, −0.0890/0.1068 ✓;
c_Φ(log 2) = **0.07555**, c_Φ(log 3) = **8.92·10⁻⁴** ✓; mass of Φ outside I = 2 × 5.78·10⁻³⁵ = 1.16·10⁻³⁴ ✓;
a₄/a₀ (Hermite) = −√384/12 = **−1.63299** ✓ vs −1.822/1.106 = −1.647 ✓.

**2.3 Reading: N1 is forced, not discovered.** At c = 2πλ² the prolates on [−λ,λ] satisfy ψ_k(v) ≈ h_k(√(2π)v)
(μ-independent scale, Slepian) — so span{ψ₀,ψ₄} ≈ span{h₀,h₄}. MORI15 already established f* ∈ span{ψ₀,ψ₄} + O(10⁻⁵),
and admissibility imposes f(0) = 0. **In span{h₀,h₄} the condition f(0) = 0 has a one-dimensional solution, and it is
exactly f_P**: a₄/a₀ = −h₀(0)/h₄(0) = −√384/12. Hence "Mori's vector is Pólya's kernel" = (MORI15 span) + (f(0) = 0) +
(prolate ≈ Hermite); the overlap defect 3.75·10⁻⁴ and the a₄/a₀ shift 0.8 % measure only ψ_k − h_k at c = 94. **NUMÉRICO
reproduced; structural content: none beyond MORI15** (a convenient closed form for the bulk). Not new structure; "not
tested by MORI15" is true but the identification was implicit.
Also: "Fg* ≈ −Ξ/‖Φ‖ explains the killed zeros" is **misleading**: Ξ vanishes at zeros, but g* differs from Φ̂ by 2 % in L²,
while Fg*(γ) ≤ 10⁻³⁶. The vanishing at zeros comes from Φ_g(ρ) = −Φ_ℓ(ρ) (C_001), which holds for *every* E-image; Pólya
plays no role in it. Downgrade to: Ξ is the Fourier transform of the bulk to 2 %.

**2.4 N2 ladder.** Recomputed from shipped eigenvalues and shipped 1−λ_k: even 4.7635e−70/1.16682e−70 = 4.082,
3.5915e−62/1.80665e−62 = 1.988, 6.1427e−55/3.42572e−55 = 1.793; odd 6.1090e−66/2.01858e−66 = 3.026,
1.52845e−58/9.70583e−59 = 1.575 ✓ (arithmetic NUMÉRICO). The reading "N2 is L′♯ with A = 0 on the first three rungs" is
**ARGUED and overstated**: L′♯ is W/ℓ with ℓ = dist² to the gauge closure, and ℓ of the higher eigenvectors was not
computed (1−λ_{4j} is neither ℓ nor a bound on it without the gauge computation, cf. AUDIT_6 on κ_emp). Valid content: the
low spectrum of W_T at μ = 15 is ordered like the parity-matched prolate defects, ratios 1.6–4.1.

## 3. M1 — "Hessian at a radical point"
Exactly what is varied: nothing. With Φ := Ef in the radical of the full-line form 𝒲 (Guo 4.4: WΦ = 0 a.e.), for *any*
quadratic form and any Ψ in its domain, 𝒲(Φ − Ψ) = 𝒲(Ψ) − 2𝒲(Φ,Ψ) + 𝒲(Φ) = 𝒲(Ψ). "Hessian" is the form itself (a quadratic
form equals its own Hessian at every point); "first variation zero" is "Φ ∈ rad 𝒲". This is A_001 Thm 1.1
(W_T(g) = 𝒲_ext[Ψ_f] = −𝒲(g,Ψ_f)) word for word, i.e. I1. **PROVED = I1 restated; no new content.** The explanatory remark
(O(1) pieces cancel because Ef is radical) is AUDIT_6 §3 verbatim. M1 does not escape constraint 2. The comb-weight
concavity remark (BB_001) is correct and correctly labelled a barrier.

## 4. M3 — the weight 𝔴_μ

**4.1 Derivation.** Θ_∞(τ) = Re ψ(¼+iτ/2) − log π = log(τ/2π) + O(τ⁻²); at τ = cω²/√(ω²−1) (the χ = 0 stationary
frequency) this is log(μω²/√(ω²−1)) ✓. Dilate n energy weight n⁻¹ and collapsed prime weight 2 log n per dilate n
(I9, Λ∗1 = log) ✓ ⇒ 𝔴_μ(ω) = Σ_{n≤ω} n⁻¹[log(μω²/√(ω²−1)) − 2log n] = H log(μω²/√(ω²−1)) − 2H₁ ✓ (algebra). The *diagonal
truncation* (pairs (m,n), m ≠ n, negligible except (1,n)) is the ARGUED input. log² cancellation: H log(μω) − 2H₁ =
log μ log ω + γ log(μω) − 2γ₁ + o(1) ✓.

**4.2 Minimum.** Recomputed (dense grid to ω = 10⁵): μ = 15: min = 3.4011974 = log 30 at ω = 1.41423 ✓; μ = 1: 0.56234 at
ω = 2 ✓. Analytic: on (1,2) 𝔴 = log μ + log(ω²/√(ω²−1)), minimised at ω² = 2 with value log 2μ (PROVED, elementary); at
ω = 2 the excess is log(2/√3) + ½log(μ/√3) > 0 for μ ≥ 2; beyond, dilates only add (NUMÉRICO for ω ≥ 2, elementary
proof not written). **Point:** "the minimum is attained exactly at the caustic" is **tautological**: on (1,2)
𝔴 = Θ_∞(τ(ω)) and min_ω τ(ω) = 2c = t_c(χ=0) by definition, so min 𝔴 = Θ_∞(t_c) = log(2c/2π) = log 2μ. It is not
independent evidence that the caustic is the "bottleneck of the sign". D(μ) recomputed: 3.491, 3.969, 5.051, 5.460, 6.761
(μ = 5, 7, 15, 20, 50) ✓; ½D(15) = 2.526 ✓; n = 1 term = log 4μ exactly (θ-substitution ω = sec θ) ✓.

**4.3 Tension with constraint 7 / E.5 — resolution.** E.5's Q_{1/1} = Σ_j j⁻¹[𝒜_a + 2AB] − 2∫r̃²H₁ is the same diagonal
object as 𝔴 (all (n,n) dilate terms are class 1/1). The two statements differ by *data*: E.5 uses fixed-shape bumps
translated to depth D (log-frequency fixed ⇒ archimedean term translation-invariant, linear H·c_φ ~ D against prime D² ⇒
negative); M3 uses chirps whose log-frequency grows like cω (archimedean term grows like log ω and cancels the log²).
No contradiction. **But**: E.5-type data are slowly varying in ξ, i.e. gauge-like (f̂ of f supported in |x| < 1/λ is of type
1/λ), and 𝒲_ext is gauge-invariant as a function while the diagonal truncation ∫𝔴|r|² is not (it assigns +∫𝔴|r_gauge|² ≥ 0
to pure gauge, whose true value is 0; E.5 shows the (1,1) class is off by −D² there, compensated by cross classes).
Therefore M3 is only meaningful **after the canonical projection Π (U.2)** and on Πr whose Mellin spectrum sits above ~c —
which is S1 (OPEN). **Constraint 7 is restricted, not removed:** cross-class cancellation is forced on any datum with a
gauge-like (low Mellin frequency) component; it is *not* proved forced on gauge-projected chirps (ARGUED both ways).
**S.4:** the near-bottom datum has an endpoint component f̂*(λ) ≈ f*(λ) ≈ 7·10⁻³⁵ ~ √ℓ (MORI15 jump), i.e. exactly S.4's
regime (decoupling scale log(l/k), μ-free, cross terms of diagonal size). So the edge channel is where S.4 lives; the
"(1,n) resonances only" claim applies at most to the core chirp. M3's decoupling at 1/c on chirps: ARGUED, untested.

**4.4 The mismatch, quantified.** Leading lower bound on core chirps: W ≥ ½(log 2μ − o(1))·leak = 1.70·leak; leading value
½D(15)·leak = 2.53·leak. Data: W/(a₄²(1−λ₄)) = 1.23, W/ℓ ∈ [0.56, ≤1.09]. If g* were a core datum, 1.23 < 1.70 would
falsify M3's lower bound at the 28 % level beyond any O(c^{−½}) ≈ 10 % correction. g* is **not** core (J = g*(T) =
−1.42·10⁻³⁴, f(λ) ≠ 0), so **MORI15 does not falsify M3**. Required edge contribution: W_chirp ≈ 2.53 × 3.87·10⁻⁷⁰ =
9.8·10⁻⁷⁰ (up to 2.1·10⁻⁶⁹ if leak ≈ ℓ_M28), observed 4.76·10⁻⁷⁰ ⇒ the (chirp, edge) block must contribute
**−5.0·10⁻⁷⁰ to −1.7·10⁻⁶⁹, i.e. 51–78 % of the chirp value**. Scale available: jump 7.2·10⁻³⁵, ‖Ψ‖ ~ 2·10⁻³⁵ ⇒ the cross
term 2f(λ)⟨h_p,XΨ_v⟩ reaches −5·10⁻⁷⁰ with an O(1) (≈ 1.7) normalised overlap, and J²Σ|ρ|⁻² = 4.66·10⁻⁷⁰ is of that order.
**Plausible in magnitude; not demonstrated.** Consequence: in the extremal the edge channel is leading order, not a
"rank-one correction", and the sign question is the 2×2 determinant W_chirp·W_edge − cross², which M3 does not touch.
Growth check (Mori V +16 % vs D +38 %, μ = 7→20) is quoted, not recomputed here (Mori V ratio not in the shipped data).

## 5. T1 and the pre-check
T1 as stated is **not well-posed yet**: (a) "span{ψ₀,ψ₄,ψ₈} with f(0) = f̂(0) = 0 and f(λ) = 0" — three linear conditions
on three coefficients leave only f = 0 generically; f̂(0) = 0 is only approximately implied by f(0) = 0 in the self-dual
span (O(1−λ)), so the conditions are (near-)dependent and the solution set depends on how ψ₈'s O(10⁻⁵) role is fixed —
must be restated (e.g. span{ψ₀,ψ₄,ψ₈,ψ₁₂}, or drop f(λ) = 0 and use the core closure); (b) "leak(f_μ)" must be ℓ = λ‖Πρ‖²
(U.2), not ∫|r|² — on gauge-projected data, otherwise the gauge term in ∫𝔴|r|² is spurious (§4.3); (c) Corollary (i) is an
upper bound that adds nothing to the sign; Corollary (ii) would be one direction of one family. The **pre-check** is
well-posed and cheap *provided* r is replaced by Πr (projection onto the Sonin annulus) and 𝒲_ext is evaluated by the exact
Λ-free expression (E.3), not by the diagonal truncation: it then tests M3's leading order on a core chirp. As written
(r = ψ̂₄|_{(λ,∞)} unprojected) it can fail for the gauge reason and would not decide M3. Recommend: run it with and without Π.

## 6. Labels
| item | memo | audit |
|---|---|---|
| W §2.1 counting identities for t* | NO-GO | NO-GO ✓ |
| W caustic t_c = min ωκ ≈ 4πμ − (2k+1)/2 | ARGUED | WKB computation correct; t_c = 183.94 (true χ₄); ARGUED |
| W peak n = 71–72 both sectors | NUMÉRICO | NUMÉRICO ✓ (resolution ≈ 1.5; dark side only ×4–5 lower) |
| W §3 pair − Gram = off-line sum; REF-D stop | PROVED algebra | PROVED; stop justified, location-free |
| Thm W.1 | PROVED | PROVED with M over |t| ≤ t* + ¼; unconditional (counting + 0<Re ρ<1) |
| Cor W.2 / W.3 / Prop W.4 | PROVED | PROVED; link to ℓ OPEN; no sign |
| N1 Pólya identification | NUMÉRICO, new | NUMÉRICO reproduced (−0.999812, 3.752e−4); **forced** by f(0)=0 in span{h₀,h₄}; no new structure |
| "Fg* ≈ −Ξ explains killed zeros" | ARGUED | misleading; killing is C_001's identity for every E-image |
| N2 ladder ratios | NUMÉRICO | NUMÉRICO ✓; "L′♯ on rungs" ARGUED/overstated (ℓ not computed) |
| M1 Hessian | PROVED | PROVED = I1 renamed; nothing varied; no new content |
| M2 | ARGUED | ARGUED |
| M3 weight algebra, min = log 2μ at √2 | ARGUED / NUMÉRICO | algebra ✓; min on (1,2) PROVED elementary; "min at caustic" tautological; diagonal truncation ARGUED |
| M3 vs constraint 7 / E.5 | tension | no contradiction (different data); meaningful only on Π-projected chirps (S1 OPEN) |
| M3 vs MORI15 mismatch | unexplained | not falsified (g* off-core); edge must supply −51…−78 % ⇒ leading order |
| T1 | theorem target | ill-posed as stated (constraint count, ℓ vs ∫|r|²); pre-check valid only with Π |
| L′♯ / (★★) | OPEN | OPEN |

## 7. Constraint 19 (what survives)
**19 (chirp/edge/gauge).** Any semiclassical (large-c) evaluation of 𝒲_ext must (a) be applied to the Π-projected datum
(U.2), never to raw r — the diagonal truncation is not gauge-invariant and E.5 shows its error on gauge-like data is
quadratic in depth; (b) treat the edge channel f(λ) ≠ 0 at leading order (at μ = 15 it must carry 51–78 % of the chirp
value with negative sign); (c) not count "minimum at the caustic" or "bulk = Pólya" as evidence — both are built in
(Θ_∞ of the stationary frequency; f(0) = 0 in span{h₀,h₄}). Constraint 7 is restricted: forced on data with gauge-like
components, open on Π-projected chirps.

**Do not retry:** "Mori's bottom = Pólya's kernel" as structural evidence; "W_T is a Hessian at a radical point" as a new
mechanism (it is I1); "the caustic minimises the sign weight" as evidence; M3 checks on unprojected r. No sign is claimed.
Row D OPEN.
