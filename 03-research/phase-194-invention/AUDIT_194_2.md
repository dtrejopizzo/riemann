# AUDIT_194_2 — review of tracks D–J (phase 194)

Checked against Paper 46 (main.tex): eq:m, def:W/eq:nuw, lem:wit-conc (l.6980), thm:kappa (l.7256), prop:prog (l.8170),
def:shape-ops (l.8328), lem:shape-scale (l.8389: proved for c large ⇒ T>½log2 and c small ⇒ T≥0.60; O_4^ε CONDITIONAL on κ_T≠0),
prop:shape-eulerdel (l.8414: a_P fails WP_T on [0.60,½log P]), cor:Tarch (l.2516: 0.58≤T*≤0.60), thm:shape (l.8853).

## Verdicts per claim
| Memo / claim | Track label | Audit | Reason |
|---|---|---|---|
| D Thm 3 (𝔞_T as renormalised ω_+ character minus comb) | PROVED | **PROVED (bookkeeping)**, minor fix | Integrand (F(0)−F(u))·½K(|u|) from ‖Φ_g‖²=2F(0), Θ_+=K/2: correct = eq:m + Plancherel. For complex g the prime sum needs Re⟨ω_+(a_{log n})Φ_g,Φ_g⟩ (P46 uses Re c_F); add Re. Content = Connes local trace formula relabelled (CITED); no sign. Comb-generic (B″). |
| D Props 1,2,4; free HS positivity | PROVED/CITED | confirmed; REF-D for sign | Correctly self-labelled. |
| E Lemma E1 | PROVED | identity PROVED; **title overclaim** | σ^{*−1}*Lσ = Λ+Λ·id checked. "The only exact Λ-extraction is a log-derivative" is not proved by the lemma: uniqueness is the content of E2. Retitle. |
| E Thm E2 (hypertranscendence) | PROVED in 𝓒_0 | **downgrade to ARGUED for the family as stated** | Hölder–Hilbert–Ostrowski gives −ζ′/ζ ∉ ℂ(s)(ζ) (CITED, correct). But the Kronecker–Hurwitz/ES data are intrinsically ζ(s)ζ(s−1); "freezing the shifted factor as coefficient" leaves ℂ(s)-coefficients, and hypertranscendence over ℂ(s) says nothing over ℂ(s,ζ(s−1)). The PROVED part covers a subclass that does not contain the family's data; the NO-GO for the actual family is the ARGUED shifted case (difference-differential independence, citation unchecked). |
| F Lemma F0, Thm F1 (C2 ⇔ log-positivity ⇔ ID) | PROVED | PROVED | Trivial but correct (b_n = c_n log n). |
| F "11-cone classification: only ID and Pick cones cross ∂log" | PROVED | **ARGUED** | The table checks 11 listed cones; "only … up to equivalence" is not a theorem about all cones. Rows C1, C3, C6, C9, C11 individually PROVED. |
| F Thm F2 (cone premises O_4-closed ⇒ excluded) | PROVED | PROVED (instance of lem:shape-scale) | log ζ^c = c log ζ; comb of ζ^c is cΛ; arch untouched. Exclusion range exactly T>½log2 ∪ T≥0.60 as stated. Not new in kind: lem:shape-scale's hypothesis is "P preserved by a↦ca"; F2 only verifies cones satisfy it. |
| G 1.1–1.3 (D_M identities) | PROVED | PROVED | Hold at σ>3/2; also verbatim Beurling. |
| G Thm G1 | NO-GO PROVED mod B″ | **NO-GO, CONDITIONAL on the class description** | Valid as an instance of thm:shape(B″) once each class ingredient is Beurling-verbatim; that check is asserted, not itemised for (b) layer-cake. Acceptable as NO-GO in 𝓒_G; "positive part = Near ⇒ REF-D" ARGUED. |
| H §1 window-collapse | PROVED | PROVED | Re c_F supported in (−2T,2T). Trivial. |
| H Thm H1 divisor-gauge symbol | PROVED | PROVED; **H1(ii) trivial** | Correct (polar ρ_{Q(1)} cancels by lem:polarelim). By §1 every gauge gives the same number; the family λ_A ≥ sup_φ inf_τ s_φ is a pointwise-symbol bound only. H1(iii) ARGUED (correctly labelled) ⇒ family likely empty = mollifier (DEAD, G3D-159). |
| H Thm H3 integer comb ∉ 𝔠⁺ | "PROVED mod lem:wit-conc" | **PROVED** (one CITED value; NUMÉRICO for g(1),g(2)) | Value recomputed (mpmath): g_ℤ(0) = −5.3721834 + 2 + 2.9207090 = **−0.451474** ✓; g_ℤ(1)=−0.3130, g_ℤ(2)=−0.0426, zero crossing τ≈2.16, g_ℤ(3)=+0.190 ✓. lem:wit-conc hypotheses: p continuous, even (Re ζ(½+iτ) even), polynomial growth (convexity) — satisfied; use γ=1 (lemma needs γ>0, not γ=0). Packets must be in 𝒫_T as in thm:kappa(ii). Remaining caveat: the "q=1 piece of Λ" carries coefficient α_1(N)→1, not 1; H3 is about ν_ℤ itself, which is fine. |
| I Thm I1 | PROVED | PROVED | (ii) uses b_1=1; (iii) b_p=c ⇒ c∈{1} / ℕ. |
| I Thm I2 (a),(b),(c) | NO-GO PROVED | PROVED | (a) = lem:shape-scale c large restricted to c∈ℕ (valid, the proof uses one prime only); (b) a=0 and cor:Tarch; (c) = R163_1001 Thm O (identification, not new). |
| I Thm I4 degree obstruction | PROVED | **ARGUED** | "Degree-≤1 SOS identity in a" is ill-defined (squares are even degree); proof is a sketch of a homogeneity count. The "no further polynomial constraint between degree 1 and Selberg" is ARGUED (labelled). |
| I Prop I5 | PROVED given CITED | PROVED (in-paper inputs) | N_T={2} for T≤½log3; endpoints a=0 (cor:Tarch, interval arithmetic) and a=Λ (Thm A, T≤log2); concavity of μ_T. Correct but only short windows, below known range. |
| J Lemma J1, Prop J2 | PROVED | PROVED | Λ²=ℓΛ; direction argument correct. Comb-generic in K. |
| J Thm J3 sparse-stability NO-GO | PROVED | PROVED (instance of prop:shape-eulerdel) | Sparse-stability is defined relative to Λ, so "a_P has 𝖯" is by definition; the count only certifies the examples. HL/k-tuple enter as premises (not proved) — exclusion is of the deduction, valid. Zero-side: a_P shares the strip zeros (prop:shape-eulerdel) ✓. |
| J Cor J4 | PROVED | first half PROVED; "FE-coupling = Near ⇒ REF-D" **ARGUED** | |

No circular killing clause found: every NO-GO kills via lem:shape-scale (c large/small, PROVED parts only), cor:Tarch or prop:shape-eulerdel. None uses O_4^ε (CONDITIONAL). E2's killing clause for the real family is ARGUED (above).

## Retry check
- D: D1–D7 discarded against the index, D8 new language only; Thm 3 = Connes local trace (CITED) — not a retry, but no new content.
- E/G: closing the INV_D/INV_E residues; no index hit on Hurwitz class numbers. OK.
- F: Pick/LP/Kreĭn items only classified, not re-attacked. OK.
- H: A1/A5/A6/A7 classified, not retried. H1(iii) converges to mollifiers (DEAD) — flag: any continuation of the divisor gauge with infinite φ is a retry of G3D-159.
- I: I2(c) = R163_1001 Thm O (acknowledged).
- J: P36-4 reopened with written new reason (additive shift); acceptable. Overlap with NG-B8 (pair correlation) is subsumed, not retried.

## The H residue
Claim: "the pole-free q≥2 Ramanujan symbol must exceed ≈0.45 on |τ|≲2.1, Toeplitz sense on 𝒫_T."
**Verdict: REF-D restatement, not a new object.** By H1, g_ℤ-part + q≥2 part = s_{Q_N}, whose Toeplitz form on 𝒫_T *is* 𝔞_T.
"Toeplitz(q≥2) ≥ −Toeplitz(g_ℤ) on 𝒫_T" is 𝔞_T ≥ 0 verbatim. Further defects: (1) the split is gauge-dependent (α_1(N) ≠ 1,
and exterior φ moves mass between q=1 and q≥2 without changing 𝔞_T), so "0.45" is not an invariant; (2) "|τ|≲2.1" is a pointwise
region, meaningless for a Toeplitz statement at finite T (spectral resolution ~1/T); for T→∞ it becomes pointwise and H1(iii)
(ARGUED) says pointwise fails. What *is* genuine: H3 as a falsifier-type datum — the integer comb alone is negative, so any proof
must take positive mass from the Möbius-polynomial phase at small τ (consistent with the semiring principle).
**Compatibility with J (H_sparse):** yes, formally. By §1 the full gauge symbol depends on Λ exactly on N_T (pins small primes:
under O_6, a_P replaces ζ by ζ∏_{p<P}(1−p^{−s}), which changes Q_N and ζ(½+iτ) together) and ζ(½+iτ) carries the FE. So it is not
sparse-stable and escapes J3 — but only because it is the whole 𝔞_T. It does not supply a non-sparse-stable *pair* statement in J's sense.

## Label corrections to apply
E2 → ARGUED (family) / PROVED (same-argument toy subclass); E1 title overclaim; F "only ID+Pick" → ARGUED; G1 → NO-GO (class
description CONDITIONAL on itemised Beurling check of (b)); H3 → PROVED (γ=1); H residue → REF-D; I4 → ARGUED; J4 second half → ARGUED;
D Thm 3 needs Re. No sign obtained in D–J. Row D: OPEN.
