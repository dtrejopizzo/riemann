# CA_F_SYNTHESIS — Front F (topology and geometry), phase 193

 Pen and paper; no numerics. **No sign contact. No negative value for ζ. No clause of (R) moved.**
Seeds and screens: CA_F_000_SEEDS.md (15 seeds, two batches). No survivor ⇒ no development memos; area exhausted per protocol.

| subarea | seed | killing clause | label |
|---|---|---|---|
| Floer beyond Maslov | F1 | Lemma F1: spectral invariants = eigenvalues; continuation = no crossing (CA_A_008 L1) | PROVED (lemma); REF-D |
| Symplectic capacities | F12 | capacities of ellipsoids are spectral ⇒ F1 | REF-D |
| Bridgeland / mirror | F2 | Lemma F2: support property on ker Z = P_T is the target; no category (ES-20); Gamma conj. archimedean + (B′) | PROVED (formal); REF-D |
| Condensed / liquid (MW-3 variant) | F3 → CA_F_001 | condensed restatement adds nothing (L1–2); bare local pieces ∉ 𝒦*_T at every finite p (Prop 3, via prop:cone(ii)); allotted local positivity = convex split (Prop 4, REF-D); O6 | NO-GO (PROVED, three classes) |
| A¹-homotopy / motivic / RO(G) | F4 | signature = n₊−n₋ of target (REF-D); GW(ℚ) needs rational form (thm:sos); RO(C₂) = parity Schur | REF-D |
| Hodge–Riemann / Lorentzian | F5 | Lemma F5 (Haynsworth) = thm:parityschur; Theorem P: full-space n₋ > 2 at large T | PROVED (lemma); retry |
| Spectral geometry (Weyl, heat) | F6 | R164_502; (B′); (R)(5); (B″) | DEAD |
| Hyperbolic / Selberg / Arthur TF exact; horocycles, Heegner | F7/F14 → CA_F_002 | Lemma 1: ξ on any vertical translate of the critical line enters tr(M⁻¹M′) only as 0 or πΣ_γ ĥ(γ−θ) (zero side); other factors at abscissa 0,1,≥3/2 (MW-2); Heegner = norm class, O12/T1 | NO-GO (PROVED for TF⁺ class) |
| GMT calibrations | F8 | calibration = dual certificate, class (D) | NO-GO (class) |
| DAG / ∞-traces; perfectoid; nef cones | F9/F13/F15 → CA_F_003 | Lemma 1: on test classes any Lefschetz pairing IS 𝔞_T; content only in proving Hodge index; gap G-F = (a) ample surface over ℤ + (b) quadratic-growth h⁰ + (c) trace; literature 2024–26 (CC 2602.15941, 2606.06604, 2609.00299, 2205.01391) has none | OPEN (object unbuilt), not impossible; W10 for declared carriers |
| Cluster algebras | F11 | coefficient positivity is comb-type, kept by O2/O6 | NO-GO |
| Perfectoid tilting | F13 | local at one p, no global surface | DEAD |
| Homogeneous dynamics (exact) | F14 | Bochner class (N_018); σ_T(0) < 0; (B″) | NO-GO |
| Nef/ample cones | F15 | ES-20; P41-1; Nakai = dual cone (D) | DEAD |
| Tropical, Deninger, prismatic, AHK | F10 | excluded by brief (L10/L29, P42-2, RH9, P41-2) | — |

## Structural observation (CA_F_003 §3: Prop 2 PROVED for unitary-invariant invariants; trichotomy outside ARGUED)
Every topological/geometric invariant available here is of one of three kinds, each already excluded:
(i) **spectral** (Floer, capacities, signatures, degrees): functions of the eigen-data of 𝔞_T ⇒ REF-D/(R)(3);
(ii) **dual/cone** (calibrations, nef cones, support properties): certificates ⇒ class (D);
(iii) **local/asymptotic** (heat, Weyl, equidistribution rates, condensed local data): (B′), (R)(5), or unordered ℚ_p.
A geometric route would need a *polarized global object* producing positivity by a Hodge-index mechanism whose input is not the
signature of 𝔞_T itself (F5 shows the input signature is false on the full space by Theorem P). Building such an object is the
ES-20 / T1 problem and is not in reach of existing mathematics in this area.

## Proposed index updates (pending review)
- "MW-3 condensed variant untried" → NO-GO (PROVED for three classes; CA_F_001).
- "Selberg/Arthur trace formula used exactly" → NO-GO (PROVED for class TF⁺; CA_F_002).
- Polarized object over ℤ: OPEN gap G-F, no 2024–26 candidate (CA_F_003); residual: direct read of 2609.00299 (low).
- "Floer beyond Maslov untried", "RO(G) untried", "A¹-homotopy untried", "cluster categories untried" → covered by F1/F4/F11 (REF-D or O2/O6).
**Status (round 2, deepened):** front F stops. Area exhausted except the OPEN gap G-F (MW-5), which is a missing construction, not something existing mathematics in this area supplies.
