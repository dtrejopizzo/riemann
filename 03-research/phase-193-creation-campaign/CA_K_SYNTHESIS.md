# CA_K_SYNTHESIS — Front K (theory of frustrated quadratic forms), phase 193

 Pen and paper; no numerics. **No sign contact. No certified negative value for ζ. No clause of (R) moved.**
Memos: CA_K_000 (13 seeds, full screens, corpus check), CA_K_001 (diamagnetism, holonomy, signed Laplacian), CA_K_002 (interpolation,
disorder, heat flow on Ĝ, site independence). Corpus: 0 prior hits for Guerra/Parisi/spin glass/Aizenman/Goemans/Harary/diamagnetic;
Doob transform = Paper 41 (retry).

## Answer to the front's key question
*Can the frustration structure (cycles m → … → 2m, weights from Γ and log) be used exactly to lower-bound the bottom by a diamagnetic or
interpolation mechanism that is ζ-specific?* **No, within the declared classes (PROVED):**
1. Diamagnetism points the right way (frustrated ≥ unfrustrated) but the unfrustrated comparison is void in the integer picture
   (bottom ≤ 𝖡(0)(1 − ½N_δ(M)) → −∞, CA_K_001 Thm 1.2), and in the t-picture the unfrustrated member *is ζ* (Λ is the diamagnetic extremum
   among |a| ≤ Λ, Thm 2.1), with negative unconstrained bottom (Thm 2.2(i)); on 𝒫_T the order **reverses** (λ_A(0.7;0) < 0 < λ_A(0.7;Λ), Thm 2.2(ii)).
   The archimedean Markov part is not the "|couplings|" version in the integer picture: Arch_M is indefinite (Prop 1.3(a), from C₀ < 0).
2. The gauge-invariant content of the frustration (ℤ/2 holonomy) is exactly sgn 𝖡 on log G (Prop 3.1: the +/· cycle C_m has flux
   sgn 𝖡(log 2)); switching-class data cannot decide positive definiteness (Prop 3.2); no U(1) flux exists inside the ratio class (Prop 3.3).
3. Every deterministic interpolation has concave bottom: its sign hypothesis is a minimizer statement (CA_K_002 Thm 1.2, REF-D); averaging over
   the only symmetry group (Ĝ-twists) is a gauge and gives upper bounds (Prop 2.1); Gaussian representations are G0. Both solvable endpoints
   (archimedean; Euler-decoupled/Haar) are indefinite (CA_K_001 Prop 1.3(a); CA_K_002 Cor 3.3(ii)).
4. ζ-specificity: none of the mechanisms separates ζ from a_P, Beurling, quartets or Epstein — each statement holds with any comb / any
   continuous 𝖡 in place of ζ's (B″-type), except the reversal Thm 2.2(ii), which is a certified ζ fact (Zhu, P47 cor:Tarch) and is an obstruction.

## Verdicts
| seed | verdict | killing clause |
|---|---|---|
| K1 Guerra interpolation | NO-GO (PROVED) | 002 Thm 1.2 (concavity ⇒ sign = minimizer statement); endpoints indefinite |
| K2 Talagrand/GG/ultrametricity | DISCARD | 002 Prop 2.1: no disorder; twists are gauges |
| K3 ASS cavity | DISCARD (retry) | Schur reductions (P47), CA_E_001 Thm 1 induction |
| K4 Grothendieck/GW/2/π | DISCARD | bottom = exact SDP; dual = class (D)/G0 |
| K5 Lasserre/SOS | DISCARD | thm:sos; CA_E_001 Cor 1.2 |
| K6 balance/holonomy/elliptope | NO-GO as sign step (PROVED) | 001 Props 3.1–3.4 |
| K7 signed Laplacian/Cheeger | NO-GO (PROVED + CITED constants) | 001 Thm 4.2 (target = near-maximal frustration), Cor 4.3 (Cheeger ≤ ½) |
| K8 diamagnetic (Kato/Simon) | NO-GO (PROVED) both pictures | 001 Thm 1.2, Thm 2.1–2.2 |
| K9 Lieb flux phase / paramagnetic | DISCARD | needs RP (CA_J_001); reversal = 001 Thm 2.2(ii) |
| K10 heat flow on Ĝ | developed; NO-GO | 002 Prop 3.1 (H-anat, linear in Λ), Cor 3.3(ii) (Haar endpoint negative) |
| K11 Doob/ground-state transform | DISCARD (retry) | Paper 41 |
| K12 frustration-free decompositions | DISCARD | thm:sos; CA_F_001 Prop 3 |
| K13 TAP/Plefka | DISCARD | perturbative, [crit] |

## PROVED facts (usable elsewhere)
K-D1. Λ is the diamagnetic extremum: λ₀(T;a) ≥ λ₀(T;Λ) for every comb with |a| ≤ Λ (signed, complex twists included).
K-D2. On 𝒫_T the order reverses: λ_A(0.7;0) < 0 < λ_A(0.7;Λ) (CITED inputs). Row D is anti-diamagnetic.
K-A. Arch_M is indefinite for M large (α is not PD: its Bochner density m ĉ₀/2π is negative near 0); under the premise Comb_M < 0 at
     Arch_M's bottom eigenvectors.
K-H. ℤ/2 holonomy of 𝔸_M on [m₀, M] ≡ sgn 𝖡(log(m/k)) on fundamental cycles of the additive path; switching data cannot decide PD.
K-L. 𝔸 = L_σ − (D_d − 𝖡(0)I) exactly; the target on (M/2, M] forces λ_min(normalized signed Laplacian) ≥ 1 − O(1/M) (near-maximal frustration).
K-S. **Site independence:** (eq:target) ⟺ 𝖡-matrices on any asymptotically dense site set (e.g. primes) are ⪰ 0. On prime sites Div ≡ 0, so the
     target is Arch ≥ Near on prime-sited tests, Arch is indefinite there, and the Haar (Euler-decoupled) endpoint Arch − Div is indefinite.

## Proposed YES→NO moves
- "diamagnetic / Kato–Simon comparison of the frustrated window matrix with its |couplings| version gives the sign" → NO (PROVED, both pictures).
- "the flux / holonomy of the +/· frustrated cycle carries the sign" → NO (flux = sgn 𝖡; switching class insufficient, PROVED).
- "Guerra/ASS interpolation from the archimedean or the Euler-decoupled endpoint" → NO (concavity; endpoints indefinite, PROVED).
- "signed-graph Cheeger inequalities" → NO (need 1 − O(1/M), Cheeger ≤ ½).

## +/· reading (PRINCIPIO RECTOR)
The front's +/· object, the frustrated cycle closed by (m, 2m), turns out to be (a) gauge-equivalent to the sign function of 𝖡 (a
conjunction of "𝖡 > 0 near 0" and "𝖡(log 2) < 0") and (b) a site artifact: prime-sited tests are decisive and have no exact multiplicative
edges at all (K-S). Exact multiplicative relations (Div, Haar) are therefore not needed by any proof; what any proof must handle is 𝖡 at log q
for rationals q near integers — the near-coincidence locus R9/(S), now isolated on a test class where it is the *only* comb contribution
(Arch ≥ Near on prime sites). Area exhausted for frustration theory; front K stops.
