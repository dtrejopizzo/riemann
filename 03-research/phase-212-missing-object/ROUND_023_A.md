# Round 23, memo A: reflection positivity through log m = log(kn)

Selection gate. Nothing is derived, nothing is computed, papers and the index are not touched.

Operation examined: take the near-coincidences m ≈ kn (h = m − kn ≠ 0) as reflected pairs
h ↔ −h about the exact coincidence h = 0 (Div), in order to write Div_M + Near_M = ⟨θF, F⟩ with a
reflection θ, and let Arch_M supply the reflection-positive measure.

Cross-check done: `ROUTES-MASTER-INDEX.md` (grep «reflexi», «reflection», «Osterwalder», «INV_V_002»: l.1918,
2087, 3016–3020, 4804–4820, 5041, 5828, 5875, 6050), `RULES_AVOID.md` §Z (Z3), `NEAR_DOSSIER.md` l.205,
`phase-200-sign-object/LEDGER_L1_RH1-9_PH000-099.md` l.95–102 and l.140–146, `AUDIT_200_SPEC_002.md`
(end of §5), `phase-193-creation-campaign/CA_A_007_SEED_TRIAGE_HOMOTOPY_TRIPLES_RP.md` (Lemma 1,
Theorem 2, l.36–62), `phase-200-sign-object/K1_OSG_001.md`, `phase-196-global-object/INV_V_002_*.md`
(V2.2, V2.4), `ROUND_016_C.md` §§0–3, `phase-6-osterwalder-schrader-reflection/` (M-OS-2, Prop. S2.1).

## (1) Closest antecedent

- **CA_A_007 §3** (phase 193). Lemma 1: for F = f + Θf with f supported on a half-line,
  𝔞(F) = 2𝔞(f) + 2H_K(f), with H_K(f) = ∬ f(t)f(s)K(t+s); «RP is the Hankel half of the
  Toeplitz form». **Theorem 2 (PROVED):** if K = K_c − Σ_n (v_n/2)δ_{±log n} has a single atom in the range,
  H_K is not ≥ 0 (f_ε concentrated at ½ log n_0 gives H_K → −v_{n_0}/2). Line 62 of the same memo explicitly
  closes the «cross-place» version of NG-E1, which is the one proposed by LEDGER_L1 S1.
- **K1_OSG_001** (phase 200): reflection at the edge; Theorem 2 conjugated by translation; R-K1 «do not
  retry edge reflections or CM kernels».
- **ROUND_016_C** (phase 212, RULES_AVOID Z3): the three variants of the choice of θ (translation of the centre,
  n ↦ 1/n, per-prime reflections θ_p = chessboard of CA_J_001) already discarded; «Arch is completely
  monotone» (K(u) = 2Σ_j e^{−(2j+½)u}) proved and blind.
- **INV_V_002** (phase 196): affine form of near-coincidences 𝔄ff_T; Thm V2.4 (Chebyshev rigidity, PROVED).

## (2) New object or operation

The nominally new candidate would be: θ acting on the near-coincidence index h = m − kn,
θ: h ↦ −h, with Div on the «hyperplane» h = 0. Written in the real variables of the form it does not exist:
𝔸_M is a form on vectors x = (x_m)_{m≤M}; h is a summation index internal to the kernel
Near_M(m,k) = ½ Σ_{n≥2, kn≠m} v_n c_0(log(kn/m)), not a coordinate of the Hilbert space. For
«Div + Near = ⟨θF,F⟩» to make sense h must be carried to the logarithmic variable t = log(kn/m), and then
θ is t ↦ −t, which is (i) the parity of c_0 (identity, blind to the weight) or (ii) the reflection of the Hankel half
of CA_A_007 translated to the point log m (K1_OSG_001). The version «pairs (p^a, q^b) with θ at
log p^a − log q^b» of LEDGER_L1 S1 is exactly the cross-place one that CA_A_007 l.62 closed.
**No formula for θ different from those two can be written.** Moreover, in the variable h the reflection is not
exact: log((m+h)/m) ≠ −log((m−h)/m) at order h²/m², so not even the parity identity survives
in h; the «asymmetry test 𝔖_2(h) vs 𝔖_2(−h)» of AUDIT_200_SPEC_002 was described there as a datum, not a route,
and moreover 𝔖_n does not depend on the weight (falsifier cΛ, c>1, in the same memo).

## (3) Does it avoid the exact reason for failure?

No. The exact reason is Theorem 2: in the OS scheme the reflected part R = 2H_K(f) receives the comb with
negative sign, and a Hankel kernel h(t+s) is ≥ 0 on a half-line only if h is the Laplace transform of
a positive measure (Widom–Bernstein, CITED); a comb of negative atoms is not. Putting Div on the
hyperplane changes nothing: Div are the atoms at t = 0 (the diagonal of θ), Near the atoms at t ≠ 0, and both
enter with sign −. «Arch supplies the reflection-positive measure» is Observation 1 of ROUND_016_C (blind).
The difference from INV_V_002 that LEDGER_L1 left pending («RP is not a Hermitian lift but
half-space positivity») is real as a statement, but the half-space then falls under Theorem 2: one
avoids V2.4 only to enter CA_A_007 §3.

## (4) Link with 𝔸_M ⪰ 0 and controls

The only writable link is OS Cauchy–Schwarz: 𝔞(f) ≥ |H_K(f)| in both parity sectors, which is the
positivity of the form restricted to evens and odds (J3, thm:parityschur): reformulation, not mechanism.
Under the three controls (weight cΛ with c≠2; deletion of a prime power; Beurling-type weight) the named
step that should break does not exist: RP fails in all four cases by the same Theorem 2 (any atom
suffices), and the part that is positive (Arch, CM) holds in all four cases. It violates (F1) and (F3) (parity /
change of reference operator); Arch and the weight do not enter the same step (F2).

## Verdict

**DOES NOT PASS (repetition).** It is the cross-place reflection of NG-E1 / LEDGER_L1 S1, closed by CA_A_007
Theorem 2 (PROVED) and l.62; the variants of θ are in K1_OSG_001 and ROUND_016_C (RULES_AVOID Z3). The
pending «difference from INV_V_002» is resolved: it exists, but leads into Theorem 2. Reopening
would require a θ not expressible as parity of c_0 nor as a half-line reflection in t, with explicit formula and
with the comb entering with positive sign in the reflected part; none was identified.
