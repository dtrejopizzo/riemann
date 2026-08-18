# Phase 107 — Arithmetic Lefschetz reconstruction

## Mission

Phase 107 begins a new geometric program.  It does not extend the operator
polarization constructions of Phase 106 and it does not modify Paper 40.
Its objective is to reverse engineer, from source arithmetic data, a
finite-support Lefschetz divisor whose arithmetic self-intersection is the
Weil quadratic form.

The target is

\[
 f\longmapsto\overline D_f,
 \qquad
 D_f\cdot H_T=0,
 \qquad
 -\overline D_f^{\,2}\cdot\overline H_T=\mathcal Q_W(f),
\]

with \(\overline D_f\) constructed from prime powers, the Gamma factor,
the pole and geometric operations, never from zeta zeros or an assumed
sign of \(\mathcal Q_W\).

## Current Local Blocker

The current finite local source row of `107_03`--`107_04` is now
exact-checked as too coarse for the current target design.
On the real additive pair `20a1@2` / `36a4@2`, the present source row

\[
\bigl(Z_{2,1},(1,2),2^{-1/2},\log 2\bigr)
\]

is identical, while the current target state

\[
(\text{Kodaira},c_p,\text{reduction label})
\]

distinguishes the pair by \(c_p=3\) versus \(c_p=1\); see `107_123`,
`107_124`, and `107_125`.
So, if Phase 107 keeps \(c_p\) in the local target, the next viable
source upgrade must add a genuinely Galois-sensitive channel rather than
another valuative/Eulerian reparameterization.
The new `107_126` gate makes the design fork exact on the same pair:
`TARGET_WITH_CP: NO`, `TARGET_KODAIRA_ONLY: YES`.
The new `107_127` gate pushes that one step higher: with \(c_p\) kept in
the target, the current finite local source-rule vocabulary already
allowed in `107_00` is itself too coarse on the same real pair.
The new `107_128` witness shows that the pair is nevertheless
distinguishable by finer local arithmetic data: the residue class of the
local minimal model at \(p=2\) already separates `20a1@2` from
`36a4@2`.
The new `107_130` gate closes the next ambiguity: that mod-8 minimal
model residue channel is real and family-level, but still does not
determine \(c_p\) by itself inside the scanned \(IV^\ast\) additive
family at \(p=2\).
The new `107_131` gate adds a first quantitative threshold on that same
family: among the tested residue depths, mixed \(c_p\)-classes persist
through mod \(16\) and disappear first at mod \(32\).
The new `107_132` gate packages that obstruction in a tranche-compliant
fixed atlas of five real curves, including one supersingular elliptic
control and one genus-\(2\) hyperelliptic control.  On that fixed atlas
the current source-rule packet still collapses the forcing pair
`20a1@2` / `36a4@2` while the current target distinguishes them by
\(c_p\), so the verifier returns `VERDICT: NO`.
The new `107_133` gate turns that fixed-atlas failure into an explicit
state decision for the current finite local route: with the current
target still retaining \(c_p\), row (c) now returns
`ROW_C_STATUS: CLOSED_BY_NO_GO` on the same tranche-compliant atlas.
The new `107_134` gate then tests a genuinely different local grammar on
real data: valuative data plus minimal-model residue modulo \(32\).
On the same fixed-atlas regime it returns `VERDICT: YES`, so the current
route stays closed, but a new residue-sensitive route survives the
visible \(S_3\) atlas test.
The new `107_135` gate strengthens that further on family data: in the
real additive \(IV^\ast\) family at \(p=2\), the mod-\(32\) residue
subchannel stays free of mixed \(c_p\)-classes through conductor
\(2000\), with `ROWS: 285` and `VERDICT: YES`.
The new `107_136` gate closes the next loophole: that surviving mod-32
channel is **not** already hidden in the current finite source rule of
`107.00`.  On the same `ROWS: 285` family, the current source-rule
packet is constant while the mod-\(32\) channel splits into
`MOD32_CLASSES: 24`, so the verifier returns `VERDICT: NO` for
derivability from the present grammar.
The new `107_137` gate turns that into one operational decision:
`OPEN_A5_BRANCH: YES`.  The current row (c) remains closed, but the
mod-\(32\) route is now admitted as an explicit new live branch for the
local Paper A problem rather than an implicit variation inside the old
grammar.
The new `107_138` gate pushes that one step further into the planning
layer itself: `PAPER_A_LOCAL_BRANCH_STATE: BIFURCATED`.  So the main
Phase 107 plan and Paper A source note now need to be read with two
named local branches: legacy row (c), closed; `A5`, live.
The new `107_139` note then adds the first positive source-side object
for that live branch: the candidate extension
\(\mathcal S_{A5}=(\mathcal S_{\mathrm{legacy}},\rho_{32})\).  Its
verifier returns `VERDICT: YES` on the fixed atlas and on the enlarged
additive family, so `A5` now has more than a target-side separation
test; it has a first explicit source-extension candidate.
The new `107_140` note pushes that one step closer to `107_04`: it
attaches \(\rho_{32}\) directly to refined local generators and line
labels, while keeping the same underlying legacy support class.  Its
verifier returns `VERDICT: YES`, so the A5 branch now has a first
object-level local candidate, not just a packet-level one.
The new `107_141` note adds the first decorated determinant-line
candidate for that same branch:
\(\mathcal D_{A5}=(\mathcal D_{\mathrm{legacy}},\rho_{32})\).  Its
verifier returns `VERDICT: YES`, with the legacy scalar projection still
constant on the enlarged \(IV^\ast\) family and the \(\rho_{32}\)
decoration splitting that blind class.
The new `107_142` note adds the first algebraic compatibility law on top
of that decoration: the difference cocycle
\(\delta_{32}(row_1,row_2)=\rho_{32}(row_1)-\rho_{32}(row_2)\bmod 32\).
Its verifier returns `VERDICT: YES`, with transpose symmetry, cocycle
compatibility, and nontrivial separation on both the `c_p` pair and the
split/nonsplit pair.
The new `107_143` note pushes that one step further: the same
\(\delta_{32}\) now behaves like a first local transport/composition law
for `A5` arrows, with `TRANSPORT_OK: True` and `INVERSE_OK: True` on
the current real tests.

## Foundational distinction

A compactly supported test sees finitely many prime powers, but its
divisor must live on a regular proper model over the whole of
\(\operatorname{Spec}\mathbb Z\).  Deleting all places beyond a cutoff
produces a nonproper object and lies outside the scope of
Faltings--Hriljac.  The construction must prove the sign on each proper
global model before any pro-limit.

## Entry test

Before any construction over \(\mathbb Z\), the proposed operations must
recover the proved function-field chain on

\[
 E/\mathbb F_5:\quad y^2=x^3+x+1.
\]

This calibration tests correspondence composition, Lefschetz fixed-point
intersection, connected Euler extraction, critical balancing, primitive
projection and the Hodge-index estimate.  It does not test the new
finite-support-on-a-proper-global-model mechanism.

## Files

- `107_00_REVERSE_ENGINEERING_ARITHMETIC_LEFSCHETZ_PROGRAM.md` — complete
  program, work packages, stop rules and paper sequence.
- `107_01_PAPER_0_FUNCTION_FIELD_CALIBRATION_SPEC.md` — fixed positive
  control and proof obligations for Paper 0.
- `107_02_PAPER_0_FUNCTION_FIELD_CALIBRATION.md` — first formal
  deliverable: the fixed \(E/\mathbb F_5\) Frobenius--Lefschetz--Hodge
  calibration written out as a proof.
- `107_03_PAPER_A_FREE_ARITHMETIC_DIVISOR_MODULE.md` — Work Package I-A:
  raw decorated correspondences, Eulerian connected extraction and the
  finite-support source divisor module \(\operatorname{Div}_{\mathrm{EF}}\).
- `107_04_PAPER_A_LOCAL_DERIVED_INTERSECTION_LINES.md` — Work Package
  I-B: finite-place determinant lines, Apostol/resultant support and the
  excess-intersection status of the diagonal.
- `107_05_PAPER_A_ARCHIMEDEAN_GREEN_METRIC.md` — Work Package I-C:
  Gamma--polar metric, matched-cutoff normalization and coherent
  diagonal closure from the same metrized line.
- `107_06_PAPER_A_FINITE_SUPPORT_INTERSECTION_THEOREM.md` — Milestone I:
  theorem-level synthesis of Paper A and closure of the finite-support
  intersection package.
- `107_07_PAPER_B_DECORATED_ABSOLUTE_FROBENIUS_CATEGORY.md` — Work
  Package II-A: the decorated correspondence category
  \(\operatorname{Corr}_{\mathrm{EF}}\), with raw composition,
  transpose, degree and connected cyclic trace.
- `107_08_PAPER_B_SUSPENSION_TO_ARITHMETIC_FLOW.md` — Work Package
  II-B: suspension/groupoid with prime closed orbits of length \(\log p\)
  and return category \(\operatorname{Corr}_{\mathrm{EF}}\).
- `107_09_PAPER_B_ARITHMETIC_LEFSCHETZ_FORMULA.md` — Work Package II-C:
  fixed-point derivation of the complete prime--Gamma--polar arithmetic
  Lefschetz formula from the suspended correspondence flow.
- `107_10_PAPER_C_UNIVERSAL_FINITE_MODELS.md` — Work Package III-A:
  blueprint for regular proper global models \(\mathcal X_T\) carrying
  finite-support cycles over the full arithmetic base.
- `107_11_PAPER_C_PICARD_JACOBIAN_REALIZATION.md` — Work Package III-B:
  faithful Abel--Jacobi/Picard realization target with exact Weil
  radical kernel audit.
- `107_12_PAPER_D_HODGE_APPLICABILITY_AUDIT.md` — Work Package IV-A:
  hypothesis-by-hypothesis audit for applying Faltings--Hriljac or
  Yuan--Zhang to the realized Phase 107 objects.
- `107_13_PAPER_D_TERMINAL_IDENTITY_AND_RH_CLOSURE.md` — Work Package
  IV-B: the exact terminal identity
  \(-\widehat{\deg}(\overline M_f^{\,2})=\mathcal Q_W(f)\) and the
  resulting formal closure to RH once the earlier packages are proved.
- `107_14_PHASE_107_EXECUTION_LEDGER.md` — Part V execution ledger:
  paper-by-paper status, mandatory falsifier audit, and current closure
  state of the whole phase.
- `107_117_S3_ATTEMPT_A1_PRIME_GENUS_DISCRIMINANT_GATE.md` —
  first fixed-atlas \(S_3\) attempt; real `NO`.
- `107_118_S3_ATTEMPT_A2_ADD_TAMAGAWA_GATE.md` — second fixed-atlas
  \(S_3\) attempt adding \(c_p\); real `NO`.
- `107_119_S3_ATTEMPT_A3_ADD_SPLIT_FLAG_GATE.md` — third fixed-atlas
  \(S_3\) attempt adding split/nonsplit; real `YES`.
- `107_120_S3_ATTEMPT_A4_FROBENIUS_TRACE_GATE.md` — Frobenius-shaped
  replacement of the split flag by \(a_p^\flat\); real `YES`.
- `107_121_CURRENT_107_04_TO_A4_FROBENIUS_NO_GO.md` — exact no-go:
  the current `107_04` observable \(\log p\) does not recover
  \(a_p^\flat\).
- `107_122_CURRENT_107_03_107_04_SOURCE_PACKET_TO_A4_NO_GO.md` — exact
  no-go for the full current finite source packet
  \(\bigl(p,(1,p),p^{-1/2},\log p\bigr)\).
- `107_123_ADDITIVE_VALUATIVE_EULER_CP_NO_GO.md` — real additive
  no-go once \(c_p\) is retained in the target.
- `107_124_CURRENT_TARGET_NON_EULERIAN_SOURCE_NECESSITY_GATE.md` —
  governance gate forcing any future faithful local source upgrade to
  add a non-Eulerian, Galois-sensitive channel.
- `107_125_CURRENT_PHASE107_FINITE_SOURCE_ROW_CP_NO_GO.md` — the same
  obstruction stated in the exact language of the current finite Paper A
  source row.
- `107_126_TARGET_BIFURCATION_GATE_CP_VS_KODAIRA.md` — exact design
  fork on the real forcing pair: keeping \(c_p\) blocks the current
  source row, while reducing the target to Kodaira type removes that
  specific local obstruction.
- `107_127_CURRENT_SOURCE_RULE_LOCAL_CP_NO_GO.md` — exact no-go showing
  that, if \(c_p\) is retained, the current finite local source-rule
  vocabulary of `107_00` is already blocked on the same real forcing
  pair.
- `107_128_LOCAL_MINIMAL_MODEL_RESIDUE_CHANNEL_WITNESS.md` — first
  positive witness beyond the current source grammar: the residue class
  of the local minimal model already separates the forcing pair.
- `107_130_IVSTAR_MOD8_RESIDUE_CP_NO_GO.md` — exact family-level no-go:
  the mod-8 residue channel persists across many real \(IV^\ast\)
  additive curves at \(p=2\), but still does not determine \(c_p\) by
  itself.
- `107_131_IVSTAR_RESIDUE_THRESHOLD_GATE.md` — quantitative threshold
  gate on the same family: the first tested residue depth with no mixed
  \(c_p\)-classes is modulus \(32\).
- `107_132_FIXED_ATLAS_TARGET_CP_NO_GO.md` — tranche-compliant fixed
  atlas gate with five real curves, one supersingular elliptic control,
  one genus-\(2\) control, and a binary `NO` for the current target
  retaining \(c_p\).
- `107_133_CURRENT_ROW_C_CLOSURE_GATE.md` — explicit closure gate for
  the current row (c): on the same fixed atlas, the current target with
  \(c_p\) forces `ROW_C_STATUS: CLOSED_BY_NO_GO`.
- `107_134_S3_ATTEMPT_A5_LOCAL_MOD32_RESIDUE_GATE.md` — new fixed-atlas
  `S_3` attempt using valuative data plus local minimal-model residue
  modulo \(32\); returns `VERDICT: YES` on the current visible atlas.
- `107_135_IVSTAR_MOD32_RANGE_EXTENSION_GATE.md` — range-extension gate
  for the additive \(IV^\ast\) family at \(p=2\): mod-\(32\) residue
  remains clean through conductor \(2000\), with `ROWS: 285` and
  `VERDICT: YES`.
- `107_136_MOD32_NON_DERIVABILITY_FROM_CURRENT_SOURCE_RULE.md` —
  explicit no-go showing that the mod-\(32\) channel of `A5` does not
  factor through the current `107.00` finite source-rule vocabulary on
  the same `ROWS: 285` family.
- `107_137_A5_BRANCH_ADMISSION_GATE.md` — operational gate combining
  row-(c) closure, `A5` atlas survival, family robustness, and
  non-derivability from the current grammar; returns
  `OPEN_A5_BRANCH: YES`.
- `107_138_PAPER_A_LOCAL_BRANCH_FORMALIZATION.md` — planning-layer gate
  formalizing Paper A local state as bifurcated: legacy row (c) closed,
  `A5` live.
- `107_139_PAPER_A_A5_SOURCE_EXTENSION_CANDIDATE.md` — first positive
  Paper A source-extension candidate for the `A5` branch:
  \(\mathcal S_{A5}=(\mathcal S_{\mathrm{legacy}},\rho_{32})\), with
  `VERDICT: YES` on the current visible tests.
- `107_140_PAPER_A_A5_REFINED_LOCAL_LINE_CANDIDATE.md` — first
  object-level A5 refinement of the local Paper A picture: refined local
  generators and line labels carrying \(\rho_{32}\), with
  `VERDICT: YES`.
- `107_141_PAPER_A_A5_DECORATED_DETERMINANT_LINE_CANDIDATE.md` — first
  decorated determinant-line candidate for the A5 branch, preserving the
  legacy scalar projection while refining it by \(\rho_{32}\), with
  `VERDICT: YES`.
- `107_142_PAPER_A_A5_RHO32_TORSOR_CANDIDATE.md` — first torsor/cocycle
  candidate for the \(\rho_{32}\) decoration, with `VERDICT: YES` on
  the current real tests.
- `107_143_PAPER_A_A5_LOCAL_TRANSPORT_COMPOSITION_GATE.md` — first local
  transport/composition gate for the `A5` arrows, with `VERDICT: YES`
  on the current real tests.
- `107_15_PAPER_C_FIRST_CANDIDATE_MODEL_X_T.md` — Part III concrete
  advance: first explicit candidate model \(\mathcal X_T^{(1)}\) as a
  regularized closure of finite-support framed-divisor incidence loci.
- `107_16_PAPER_C_COMPACTIFIED_FRAMED_DIVISOR_SQUARE.md` — Part III
  compactification advance: candidate compactified square
  \(\overline{\mathfrak S}\), common corner \(C_\infty\), and boundary
  metric line \(\mathcal L_\infty\) for Gamma--polar descent.
- `107_17_PAPER_C_LOCAL_CHART_ATLAS_AND_FINITE_TYPE_CRITERION.md` —
  Part III local advance: chart atlas for
  \(\overline{\mathfrak P}_{\rm fr}\) and a first chartwise finite-type
  criterion for the closures \(\overline{\Gamma}_n^{\rm fr}\).
- `107_18_PAPER_C_FINITE_FRAMING_COORDINATE_FROM_ROOTED_CYCLOTOMIC_CHARTS.md`
  — Part III effective advance: finite framing coordinate
  \((n,\chi)\) extracted from visible rooted/cyclotomic packets.
- `107_19_PAPER_C_PACKETWISE_DETERMINANT_COMPARISON.md` — Part III
  comparison advance: packetwise bridge from finite rooted/cyclotomic
  charts to the determinant-line package of `107_04`.
- `107_20_PAPER_C_PACKET_INTERSECTION_LINE_CONSTRUCTION.md` — Part III
  local proof advance: explicit packet determinant line construction and
  off-diagonal norm comparison with `107_04`.
- `107_21_PAPER_C_GLOBAL_PACKET_DETERMINANT_DESCENT.md` — Part III
  globalization advance: descent of the local packet determinant package
  to a global line object on \(\mathcal X_T^{(1)}\).
- `107_22_PAPER_C_CANDIDATE_ADELIC_METRIZED_REALIZATION.md` — Part III
  realization advance: candidate integrable adelic metrized class
  attached to finite-support divisors on \(\mathcal X_T^{(1)}\).
- `107_23_PAPER_C_ADELIC_INTEGRABILITY_CRITERION.md` — Part III/IV
  interface advance: chartwise logarithmic criterion for the candidate
  adelic metric and partial closure of the finiteness audit.
- `107_24_PAPER_C_PRIMITIVE_DEGREE_ZERO_REDUCTION.md` — Part III/IV
  interface advance: explicit polarization candidate and finite
  reduction of the degree-zero audit.
- `107_25_PAPER_C_FIRST_POLARIZATION_INTERSECTION_IDENTITIES.md` —
  Part III geometric advance: first intersection identities for the
  candidate polarization and corner-driven nonvanishing criterion.
- `107_26_PAPER_C_EXCEPTIONAL_CORRECTION_CONTROL.md` — Part III
  geometric advance: finite control of exceptional correction terms and
  corner-preserving regularization criterion.
- `107_27_PAPER_C_LOCAL_EXCEPTIONAL_CENTER_AUDIT.md` — Part III
  geometric advance: explicit local list of polarization-active centers
  and corner-preserving audit in the chart atlas.
- `107_28_PAPER_0_GENUS_2_DIAGONAL_SENSITIVITY_AUDIT.md` — auxiliary
  Paper 0 audit: exact genus-2 controls for the primitive diagonal
  entries, now including one supersingular and one ordinary test.
- `107_28_genus2_diagonal_sensitivity.py` — exact verifier for the
  genus-2 diagonal-sensitivity audit.
- `107_29_PAPER_0_RECALIBRATION_AFTER_GENUS_AUDIT.md` — recalibration of
  Paper 0 after the genus-sensitivity falsifier audit.
- `107_30_PAPER_0_GENUS_UNIFORM_PRIMITIVE_INTERSECTION_FORM.md` —
  classical genus-uniform derivation by adjunction of the primitive Gram
  package on \(C\times C\).
- `107_31_PAPER_0_GENUS_UNIFORM_SOURCE_CHAIN.md` — source-level
  genus-uniform derivation of the Frobenius--Lefschetz--Euler--balance
  chain on \(C\times C\).
- `107_32_PAPER_0_GENUS_FREE_SOURCE_CALIBRATION.md` — integrated
  genus-free source calibration statement on \(C\times C\).
- `107_33_FOUNDATIONAL_STATUS_RECALIBRATION.md` — gate-audit
  recalibration of the foundational status of Papers 0, A, and B.
- `107_34_PAPER_A_PRIME_POWER_SUPPORT_AUDIT.md` — exact audit of the
  cyclotomic prime-power support law and diagonal resultant vanishing of
  `107_04`.
- `107_34_paper_a_prime_power_support_preflight.py` — exact verifier for
  that finite-place Paper A audit.
- `107_35_PAPER_A_CONNECTED_EXTRACTION_AUDIT.md` — exact audit of the
  Eulerian primitive extractor of `107_03` and its fixed-control
  function-field specialization.
- `107_35_paper_a_connected_extraction_preflight.py` — exact verifier
  for that connected-extraction audit.
- `107_36_PAPER_B_FUNCTION_FIELD_RETURN_LEFSCHETZ_AUDIT.md` — exact
  audit of the same-tower function-field return/composition/Lefschetz
  shadow of Part II on the fixed control.
- `107_36_paper_b_return_lefschetz_preflight.py` — exact verifier for
  that Paper B control audit.
- `107_37_PAPER_B_AUDIT_COVERAGE_MATRIX.md` — explicit coverage matrix
  separating the exact-audited and still-formalized parts of Part II.
- `107_38_PAPER_B_COMMON_PHASE_GLUING_AUDIT.md` — exact combinatorial
  audit of the load-bearing common-phase gluing shadow of `107_08`.
- `107_38_paper_b_common_phase_gluing_preflight.py` — exact verifier for
  that common-phase shadow audit.
- `107_39_PAPER_B_MIXED_TOWER_REFINEMENT_AUDIT.md` — exact combinatorial
  audit that mixed-tower composition does not collapse to primitive
  returns.
- `107_39_paper_b_mixed_tower_refinement_preflight.py` — exact verifier
  for that mixed-tower shadow audit.
- `107_40_PAPER_B_DAVENPORT_HEILBRONN_EXTERNAL_WITNESS.md` — exact
  external arithmetic witness that Davenport--Heilbronn is non-Eulerian
  already at the coefficient stage.
- `107_40_davenport_heilbronn_external_witness.py` — exact verifier for
  that external falsifier.
- `107_41_PAPER_B_JOINT_GAMMA_POLAR_FACTOR_AUDIT.md` — high-precision
  consistency audit for the explicit coupled Gamma--pole factor used by
  `107_05` and `107_09`.
- `107_41_joint_gamma_polar_factor_consistency.py` — exact verifier for
  that narrow archimedean factor audit.
- `107_42_PAPER_C_LOCAL_PACKET_UNIT_FACTOR_AUDIT.md` — exact local
  Paper C audit that the packet algebra of `107_20` preserves the
  cyclotomic resultant norm off the diagonal and does not repair the
  diagonal excess-intersection stop.
- `107_42_paper_c_packet_unit_factor_preflight.py` — exact verifier for
  that local packet unit-factor audit.
- `107_43_PAPER_C_AUDIT_COVERAGE_MATRIX.md` — explicit Part III
  coverage matrix separating exact local audits from still-globalized
  theorem targets.
- `107_44_PAPER_C_PACKET_DESCENT_COCYCLE_AUDIT.md` — exact Paper C
  audit of the finite rooted descent cocycle behind `107_21`, including
  route-independent descended sections and visible-action compatibility.
- `107_44_paper_c_packet_descent_cocycle_preflight.py` — exact verifier
  for that packet descent cocycle audit.
- `107_45_PAPER_C_LOGARITHMIC_CHART_AUDIT.md` — exact Paper C audit of
  the finite logarithmic chart shadow behind `107_23`.
- `107_45_paper_c_logarithmic_chart_audit.py` — exact verifier for that
  logarithmic chart audit.
- `107_46_PAPER_C_PRIMITIVE_DEGREE_ZERO_AUDIT.md` — exact Paper C audit
  of the finite primitive degree-zero shadow behind `107_24`.
- `107_46_paper_c_primitive_degree_zero_audit.py` — exact verifier for
  that primitive degree-zero audit.
- `107_47_PAPER_C_CORRECTION_SUM_AUDIT.md` — exact Paper C audit of the
  finite correction-sum shadow behind `107_25`--`107_27`.
- `107_47_paper_c_correction_sum_audit.py` — exact verifier for that
  correction-sum audit.
- `107_48_PAPER_C_EXACT_KERNEL_SHADOW_AUDIT.md` — exact Paper C audit
  of the finite equality-case/kernel shadow behind `107_11`.
- `107_48_paper_c_exact_kernel_shadow_audit.py` — exact verifier for
  that kernel-shadow audit.
- `107_49_PAPER_C_PAIRING_TRANSPORT_SHADOW_AUDIT.md` — exact Paper C
  audit of the finite bilinear pairing-transport shadow behind
  `107_11` and `107_13`.
- `107_49_paper_c_pairing_transport_shadow_audit.py` — exact verifier
  for that pairing-transport shadow audit.
- `107_50_PAPER_D_ROUTE_A_APPLICABILITY_COVERAGE_MATRIX.md` — explicit
  Route A coverage matrix separating exact finite shadows from still
  unproved target-side hypotheses in `107_12`.
- `107_51_PAPER_D_A6_FUNCTORIALITY_SHADOW_AUDIT.md` — exact Paper D
  audit of the finite A6 functoriality shadow behind `107_12`.
- `107_51_paper_d_a6_functoriality_shadow_audit.py` — exact verifier
  for that A6 functoriality shadow audit.
- `107_52_PAPER_D_A5_FINITENESS_SHADOW_AUDIT.md` — exact Paper D audit
  of the finite A5 finiteness shadow behind `107_12`.
- `107_52_paper_d_a5_finiteness_shadow_audit.py` — exact verifier for
  that A5 finiteness shadow audit.
- `107_53_PAPER_D_A1_REGULAR_PROPERNESS_BOUNDARY_AUDIT.md` — explicit
  Route A boundary audit showing that the candidate-model package of
  `107_10`, `107_15`--`107_17` supports A1 structurally but still does
  not close regular properness or exact adelic comparison.
- `107_54_PAPER_D_A4_LOG_EFFECTIVITY_SHADOW_AUDIT.md` — exact Paper D
  audit that the visible polarization-active blow-ups preserve the
  nonnegative local logarithmic support cone behind Route A item A4.
- `107_54_paper_d_a4_log_effectivity_shadow_audit.py` — exact verifier
  for that A4 log-effectivity shadow audit.
- `107_55_PAPER_D_A2_REMAINDER_COHERENCE_AUDIT.md` — exact Paper D
  audit that the visible regular remainder channel behind Route A item
  A2 is order-only and route-independent under descent and chart
  transport.
- `107_55_paper_d_a2_remainder_coherence_audit.py` — exact verifier for
  that A2 remainder-coherence shadow audit.
- `107_56_PAPER_D_TERMINAL_IDENTITY_PRIMITIVE_QUOTIENT_AUDIT.md` —
  exact Paper D audit that the finite shadow of `107_13` survives
  primitive projection and quotient by the explicit radical with the
  correct equality case.
- `107_56_paper_d_terminal_identity_primitive_quotient_audit.py` —
  exact verifier for that primitive-quotient terminal-identity audit.
- `107_57_PAPER_C_CANDIDATE_REALIZATION_PACKAGING_AUDIT.md` — exact
  Paper C audit that the finite packaging shadow of `107_22` is
  additive, single-receiver, rooted-refinement invariant, and primitive
  compatible.
- `107_57_paper_c_candidate_realization_packaging_audit.py` — exact
  verifier for that candidate-realization packaging audit.
- `107_58_PAPER_C_PACKET_CYCLOTOMIC_BRIDGE_AUDIT.md` — exact Paper C
  audit that the visible packet-to-cyclotomic bridge of `107_19`
  preserves support, norm, transpose symmetry, and diagonal caution.
- `107_58_paper_c_packet_cyclotomic_bridge_audit.py` — exact verifier
  for that packet-cyclotomic bridge audit.
- `107_59_PAPER_C_VISIBLE_FRAMING_COORDINATE_AUDIT.md` — exact Paper C
  audit that the visible rooted framing coordinate of `107_18` is a
  genuinely finite combinatorial packet system.
- `107_59_paper_c_visible_framing_coordinate_audit.py` — exact verifier
  for that visible framing-coordinate audit.
- `107_60_PAPER_C_LOCAL_ATLAS_FINITE_TYPE_AUDIT.md` — exact Paper C
  audit that the visible local atlas and finite-type criterion of
  `107_17` are symbolically consistent.
- `107_60_paper_c_local_atlas_finite_type_audit.py` — exact verifier
  for that local-atlas finite-type audit.
- `107_61_PAPER_C_COMPACTIFIED_SQUARE_CORNER_AUDIT.md` — exact Paper C
  audit that the common-corner receiver logic of `107_16` is already
  visible in a finite symbolic model.
- `107_61_paper_c_compactified_square_corner_audit.py` — exact verifier
  for that compactified-square corner audit.
- `107_62_PAPER_C_CANDIDATE_MODEL_INCIDENCE_AUDIT.md` — exact Paper C
  audit that the visible incidence structure of `107_15` keeps the
  diagonal, rulings, and graph generators noncollapsed.
- `107_62_paper_c_candidate_model_incidence_audit.py` — exact verifier
  for that candidate-model incidence audit.
- `107_63_PAPER_C_UNIVERSAL_MODEL_EXCLUSION_AUDIT.md` — exact Paper C
  audit that the wrong finite-model simplifications around `107_10`
  fail for explicit structural reasons.
- `107_63_paper_c_universal_model_exclusion_audit.py` — exact verifier
  for that universal-model exclusion audit.
- `107_64_PAPER_A_DIAGONAL_COHERENCE_AUDIT.md` — exact Paper A audit
  that the diagonal-coherence claim of `107_05` survives one finite
  matched-cutoff and polarization shadow.
- `107_64_paper_a_diagonal_coherence_audit.py` — exact verifier for
  that diagonal-coherence audit.
- `107_65_PAPER_B_NO_PRESCRIBED_TRACE_AUDIT.md` — exact Paper B audit
  that the visible renormalized trace of `107_09` remains source-defined
  and cannot be read as an arbitrary externally installed functional.
- `107_65_paper_b_no_prescribed_trace_audit.py` — exact verifier for
  that no-prescribed-trace audit.
- `107_66_ZERO_FREE_SOURCE_AUDIT.md` — exact audit that the visible
  arithmetic observables of the source route ignore ambient spectral
  channels and remain reconstructible from source generators.
- `107_66_zero_free_source_audit.py` — exact verifier for that
  zero-free source audit.
- `107_67_HODGE_ROUTE_EXCLUSIVITY_AUDIT.md` — exact audit that the
  Route A / Route B applicability logic of `107_12` rejects hybrid
  Hodge imports and keeps the current phase state pre-applicability.
- `107_67_hodge_route_exclusivity_audit.py` — exact verifier for that
  Hodge-route exclusivity audit.
- `107_68_EQUALITY_CASE_EXACTNESS_AUDIT.md` — exact audit that the
  equality-case gate of `107_11`/`107_13` rejects kernels strictly
  larger than the explicit Weil radical.
- `107_68_equality_case_exactness_audit.py` — exact verifier for that
  equality-case exactness audit.
- `107_69_ARCHIMEDEAN_LOAD_BEARING_AUDIT.md` — exact audit that the
  visible finite-rank algebraic component cannot carry all variation and
  that the separating burden must fall on the Green datum.
- `107_69_archimedean_load_bearing_audit.py` — exact verifier for that
  archimedean load-bearing audit.
- `107_70_PAPER_A_AUDIT_COVERAGE_MATRIX.md` — explicit Paper A coverage
  matrix separating exact component shadows from the still-unaudited
  unified Milestone I synthesis.
- `107_71_PAPER_E1_AUDIT_COVERAGE_MATRIX.md` — explicit E1 coverage
  matrix separating exact finite shadows of applicability/terminal
  logic from the still-unproved realized Hodge bridge.
- `107_72_PAPER_C_GLOBAL_LINE_OBJECT_GLUE_AUDIT.md` — exact Paper C
  audit that the visible descent cocycle of `107_21` defines a glued
  quotient line-object shadow and is stable under gauge re-trivialization.
- `107_72_paper_c_global_line_object_glue_audit.py` — exact verifier
  for that global-line-object gluing audit.
- `107_73_PAPER_C_ADELIC_CLASS_INTRINSICITY_AUDIT.md` — exact Paper C
  audit that the visible chart/root presentations of `107_22` define
  one intrinsic adelic-class quotient shadow and reject extra receiver
  splitting.
- `107_73_paper_c_adelic_class_intrinsicity_audit.py` — exact verifier
  for that adelic-class intrinsicity audit.
- `107_74_PAPER_C_INTEGRABILITY_PROFILE_INTRINSICITY_AUDIT.md` — exact
  Paper C audit that the visible chart/root presentations of `107_23`
  define one intrinsic normal-crossings integrability profile and
  reject extra singular directions.
- `107_74_paper_c_integrability_profile_intrinsicity_audit.py` — exact
  verifier for that integrability-profile intrinsicity audit.
- `107_75_PAPER_A_UNIFIED_SYNTHESIS_AUDIT.md` — exact Paper A audit
  that one finite symbolic model realizes the unified Milestone I
  synthesis of connected extraction, prime-power support, and common
  Green closure.
- `107_75_paper_a_unified_synthesis_audit.py` — exact verifier for that
  unified-synthesis audit.
- `107_76_PAPER_B_JOINT_FIXED_POINT_ASSEMBLY_AUDIT.md` — exact Paper B
  audit that one visible renormalized source package jointly assembles
  the prime, Gamma, and pole sectors while keeping mixed towers out of
  the primitive prime page.
- `107_76_paper_b_joint_fixed_point_assembly_audit.py` — exact verifier
  for that joint fixed-point assembly audit.
- `107_77_PAPER_E1_CLOSURE_READINESS_AUDIT.md` — exact E1 audit that RH
  closure is allowed only when applicability, terminal identity, and
  exact kernel all hold together, and that the current phase is still
  pre-closure.
- `107_77_paper_e1_closure_readiness_audit.py` — exact verifier for that
  E1 closure-readiness audit.
- `107_78_PAPER_C_REALIZATION_DEGREE_ZERO_COVARIANCE_AUDIT.md` — exact
  Paper C audit that primitive correction lands the visible realization
  of `107_11` in degree zero and that finite critical scaling preserves
  that status.
- `107_78_paper_c_realization_degree_zero_covariance_audit.py` — exact
  verifier for that realization degree-zero covariance audit.
- `107_79_PAPER_C_CANDIDATE_ENVELOPE_COHERENCE_AUDIT.md` — exact Paper
  C audit that the visible incidence, boundary, and atlas layers fit
  one coherent candidate envelope without collapsing the two-ruling and
  corner structure.
- `107_79_paper_c_candidate_envelope_coherence_audit.py` — exact
  verifier for that candidate-envelope coherence audit.
- `107_80_PAPER_D_A5_TARGET_PAIRING_ASSEMBLY_AUDIT.md` — exact Paper D
  audit that the transported target pairing stays finite on every
  visible non-diagonal channel and confines the unresolved placeholder
  to the genuine diagonal square.
- `107_80_paper_d_a5_target_pairing_assembly_audit.py` — exact verifier
  for that A5 target-pairing assembly audit.
- `107_81_PAPER_D_A2_A4_METRIC_CHANNEL_DISCIPLINE_AUDIT.md` — exact
  Paper D audit that one visible normal-crossings profile, one
  remainder channel, and one nonnegative local support package coexist
  in the same finite target-side model.
- `107_81_paper_d_a2_a4_metric_channel_discipline_audit.py` — exact
  verifier for that A2/A4 metric-channel discipline audit.
- `107_82_PAPER_C_CANDIDATE_TARGET_ASSEMBLY_AUDIT.md` — exact Paper C
  audit that the visible candidate envelope, intrinsic receiver
  channel, degree-zero realization, and metric profile coexist on one
  common target-side cover.
- `107_82_paper_c_candidate_target_assembly_audit.py` — exact verifier
  for that candidate-target assembly audit.
- `107_83_PAPER_D_ROUTE_A_ASSEMBLED_APPLICABILITY_AUDIT.md` — exact
  Paper D audit that the visible A1--A6 shadows coexist in one
  candidate target state and fail immediately when any one ingredient
  is removed.
- `107_83_paper_d_route_a_assembled_applicability_audit.py` — exact
  verifier for that assembled Route A applicability audit.
- `107_84_PAPER_E1_ASSEMBLED_BRIDGE_AUDIT.md` — exact E1 audit that the
  visible Route A applicability shadow, terminal identity, equality
  case, and closure readiness coexist in one finite bridge state.
- `107_84_paper_e1_assembled_bridge_audit.py` — exact verifier for that
  assembled E1 bridge audit.
- `107_85_PHASE_LEVEL_PREGEOMETRIC_CHAIN_AUDIT.md` — exact phase-level
  audit that the assembled candidate target, assembled Route A
  applicability, and assembled E1 bridge fit one end-to-end finite
  pregeometric chain.
- `107_85_phase_level_pregeometric_chain_audit.py` — exact verifier for
  that phase-level pregeometric chain audit.
- `107_86_PAPER_C_FINITE_SUPPORT_REALIZATION_ASSEMBLY_AUDIT.md` —
  exact Paper C audit that the full-base, degree-one, two-ruling,
  discrete candidate realization architecture coexists with the
  coherent envelope and assembled target-side package in one finite
  state.
- `107_86_paper_c_finite_support_realization_assembly_audit.py` —
  exact verifier for that assembled finite-support realization audit.
- `107_87_PAPER_C_POINT_SPECTRUM_RETENTION_AUDIT.md` — exact Paper C
  audit that the intrinsic single-receiver candidate package retains
  visible point/resonance classes modulo the explicit radical shadow
  and rejects continuous-collapse substitutes.
- `107_87_paper_c_point_spectrum_retention_audit.py` — exact verifier
  for that point-spectrum retention audit.
- `107_88_PAPER_B_ASSEMBLED_NO_PRESCRIBED_TRACE_AUDIT.md` — exact
  Paper B audit that the full renormalized visible fixed-point page
  remains source-determined and rejects externally prescribed edits.
- `107_88_paper_b_assembled_no_prescribed_trace_audit.py` — exact
  verifier for that assembled no-prescribed-trace audit.
- `107_89_PAPER_C_TARGET_SIDE_DIVISOR_SENSITIVITY_AUDIT.md` — exact
  Paper C audit that the intrinsic candidate realization package keeps
  genuine moved-divisor positions visible modulo the explicit radical
  shadow and rejects scalarized substitutes.
- `107_89_paper_c_target_side_divisor_sensitivity_audit.py` — exact
  verifier for that target-side divisor-sensitivity audit.
- `107_90_PAPER_C_ASSEMBLED_ARCHIMEDEAN_LOAD_BEARING_AUDIT.md` —
  exact Paper C audit that the intrinsic finite-support candidate
  package remains faithfully separated only while the Green side keeps
  enough independent channels.
- `107_90_paper_c_assembled_archimedean_load_bearing_audit.py` —
  exact verifier for that assembled archimedean load-bearing audit.
- `107_91_PAPER_D_ASSEMBLED_HODGE_PREAPPLICABILITY_AUDIT.md` — exact
  Paper D audit that the current finite assembled Route A state remains
  only pre-applicable and cannot be promoted by hybrid logic or finite
  assembly alone.
- `107_91_paper_d_assembled_hodge_preapplicability_audit.py` — exact
  verifier for that assembled Hodge pre-applicability audit.
- `107_92_ASSEMBLED_EQUALITY_CASE_GATE_AUDIT.md` — exact audit that the
  current equality-case layer behaves as one assembled gate with kernel
  minimality, non-radical survival, and primitive-quotient identity.
- `107_92_assembled_equality_case_gate_audit.py` — exact verifier for
  that assembled equality-case gate audit.
- `107_93_REAL_ELLIPTIC_BAD_FIBER_INTERSECTION_WITNESS.md` — real local
  arithmetic witness on actual elliptic curves over \(\mathbf Q\),
  checking bad-fiber intersection matrices and the standard Arakelov
  finite-place weight \(\log p\).
- `107_93_real_elliptic_bad_fiber_intersection_witness.py` — exact
  verifier for that real bad-fiber witness.
- `107_94_REAL_KODAIRA_TYPE_LOG_WEIGHT_COMPARISON.md` — real local
  witness that repeated Kodaira type \(I_2\) has the same underlying
  bad-fiber geometry at different primes, with only the target-side
  \(\log p\) factor changing.
- `107_94_real_kodaira_type_log_weight_comparison.py` — exact verifier
  for that real Kodaira-type/log-weight comparison.
- `107_95_SOURCE_TARGET_LOCAL_COMPARISON_BOUNDARY_WITNESS.md` — real
  local comparison boundary showing that the current source-side row of
  `107_04` captures the scalar \(\log p\) layer but not yet the real
  target-side fiber geometry.
- `107_95_source_target_local_comparison_boundary_witness.py` — exact
  verifier for that source-vs-target local comparison boundary.
- `107_96_REAL_COMPONENT_GROUP_BOUNDARY_WITNESS.md` — real local
  boundary witness showing that affine bad-fiber geometry does not by
  itself exhaust the local arithmetic datum, as seen from Tamagawa
  behavior on actual fibers.
- `107_96_real_component_group_boundary_witness.py` — exact verifier
  for that real component-group boundary witness.
- `107_97_SOURCE_VS_FULL_LOCAL_TARGET_BOUNDARY_WITNESS.md` — real local
  synthesis witness locating the current source-side row below real
  fiber geometry and the latter below the fuller local arithmetic
  target datum.
- `107_97_source_vs_full_local_target_boundary_witness.py` — exact
  verifier for that source-vs-full-local-target boundary witness.
- `107_98_REAL_SPLIT_NON_SPLIT_BOUNDARY_WITNESS.md` — real local
  witness that even matching prime, Kodaira type, affine matrix, and
  \(c_p\) still does not determine the full bad-reduction datum, as
  shown by split versus nonsplit multiplicative examples.
- `107_98_real_split_non_split_boundary_witness.py` — exact verifier
  for that real split/non-split boundary witness.
- `107_99_REAL_LOCAL_INFORMATION_HIERARCHY_WITNESS.md` — real local
  synthesis witness organizing the current hierarchy of local target
  information: scalar weight, fiber geometry, \(c_p\), and the finer
  split/nonsplit label.
- `107_99_real_local_information_hierarchy_witness.py` — exact verifier
  for that real local information hierarchy witness.
- `107_100_REAL_COMPONENT_GROUP_FROBENIUS_WITNESS.md` — real local
  witness identifying, in multiplicative bad fibers, the missing
  arithmetic refinement from geometry to \(c_p\) as Frobenius action on
  the geometric component group.
- `107_100_real_component_group_frobenius_witness.py` — exact verifier
  for that real component-group/Frobenius witness.
- `107_101_REAL_ADDITIVE_IV_FROBENIUS_WITNESS.md` — real local witness
  extending the same mechanism to an additive \(IV\) pair: the affine
  \(A_2\) triangle has geometric component group of order \(3\), and
  \(c_p\) is determined by Frobenius acting trivially or by a 3-cycle.
- `107_101_real_additive_iv_frobenius_witness.py` — exact verifier for
  that real additive-\(IV\) component/Frobenius witness.
- `107_102_REAL_ADDITIVE_III_RIGIDITY_WITNESS.md` — real local witness
  for the complementary rigid additive sector \(III\): once the affine
  \(A_1\) geometry is fixed, the geometric component group is of order
  \(2\) and the observed \(c_p\) in the pinned examples is forced.
- `107_102_real_additive_iii_rigidity_witness.py` — exact verifier for
  that real additive-\(III\) rigidity witness.
- `107_103_REAL_LOCAL_RIGIDITY_FLEXIBILITY_ATLAS.md` — exact synthesis
  of the current real local typed behavior: sectors flexible already in
  \(c_p\), sectors rigid in \(c_p\) but flexible in finer reduction
  labels, and sectors rigid at both visible levels.
- `107_103_real_local_rigidity_flexibility_atlas.py` — exact verifier
  for that real local rigidity/flexibility atlas.
- `107_104_SOURCE_LOCAL_DISCRIMINATION_ATLAS.md` — exact comparison of
  the current Paper A source row against the pinned real local atlas,
  showing how many distinct target-side states collapse to one source
  scalar class at fixed prime.
- `107_104_source_local_discrimination_atlas.py` — exact verifier for
  that source local discrimination atlas.
- `107_105_MINIMAL_SOURCE_REFINEMENT_LADDER.md` — exact ladder of
  increasingly informative hypothetical source local signatures, showing
  which additional layers would resolve which parts of the current real
  local target atlas.
- `107_105_minimal_source_refinement_ladder.py` — exact verifier for
  that minimal source refinement ladder.
- `107_106_SOURCE_REFINEMENT_RESIDUAL_AMBIGUITY_MATRIX.md` — exact
  residual matrix of which concrete local target ambiguities remain at
  each source refinement level \(S_0,S_1,S_2,S_3\).
- `107_106_source_refinement_residual_ambiguity_matrix.py` — exact
  verifier for that residual ambiguity matrix.
- `107_107_LOCAL_SOURCE_UPGRADE_NECESSITY_GATE.md` — exact lower-bound
  gate for future Paper A local upgrades: which separation tests must be
  passed before claiming recovery of geometry, \(c_p\), or finer local
  reduction data.
- `107_107_local_source_upgrade_necessity_gate.py` — exact verifier for
  that local source upgrade necessity gate.
- `107_108_S0_FACTOR_LOCAL_REALIZATION_NO_GO.md` — exact no-go
  statement showing that any local comparison still factoring through
  the present `107_04` source signature \(S_0=\log p\) cannot be
  faithful on the pinned real local target atlas.
- `107_108_s0_factor_local_realization_no_go.py` — exact verifier for
  that \(S_0\)-factor local realization no-go.
- `107_109_SOURCE_FACTOR_REALIZATION_NO_GO_LADDER.md` — exact ladder of
  local no-go statements for factorizations through \(S_0\), \(S_1\),
  and \(S_2\), with \(S_3\) as the first visible escape point on the
  pinned real atlas.
- `107_109_source_factor_realization_no_go_ladder.py` — exact verifier
  for that source-factor realization no-go ladder.
- `107_110_SAME_BAD_PRIME_PROFILE_GLOBAL_NO_GO.md` — exact finite
  global no-go showing that two actual curves can share the same bad-
  prime support profile while already differing in their pinned real
  local target data.
- `107_110_same_bad_prime_profile_global_no_go.py` — exact verifier for
  that same-bad-prime-profile global no-go.
- `107_111_SAME_FINITE_LOG_WEIGHT_PACKET_GLOBAL_NO_GO.md` — exact
  finite global no-go in the language closest to `107_04`: two actual
  curves can share the same full packet of finite bad-prime weights
  `{\log p}` while still differing in their pinned real local target
  data.
- `107_111_same_finite_log_weight_packet_global_no_go.py` — exact
  verifier for that same-finite-log-weight-packet global no-go.
- `107_112_GLOBAL_SOURCE_UPGRADE_NECESSITY_GATE.md` — exact governance
  gate for future finite global source upgrades: any claim to recover
  pinned real local target data must distinguish the pair `14.a1/14.a5`
  by information finer than both the bad-prime support profile and the
  full finite `\log p`-packet.
- `107_112_global_source_upgrade_necessity_gate.py` — exact verifier
  for that global source upgrade necessity gate.
- `107_113_CURRENT_FINITE_SOURCE_INSUFFICIENCY_GATE.md` — unified exact
  gate summarizing that the current finite source package remains too
  coarse, both locally and globally, for faithful recovery of the pinned
  real local target atlas.
- `107_113_current_finite_source_insufficiency_gate.py` — exact
  verifier for that current finite source insufficiency gate.
- `107_114_PAPER_A_FINITE_BOUNDARY_AUDIT.md` — exact Milestone I
  boundary audit packaging both sides at once: the current finite Paper
  A pairing package is exact-audited as a symbolic source shadow, but
  still excluded from faithful local/global target recovery by the
  current insufficiency gates.
- `107_114_paper_a_finite_boundary_audit.py` — exact verifier for that
  Paper A finite boundary audit.
- `107_115_PAPER_B_FINITE_BOUNDARY_AUDIT.md` — exact Milestone II
  boundary audit packaging both sides at once: the current finite Paper
  B fixed-point/source package is exact-audited as a symbolic source
  shadow, but still excluded from the full suspended geometric
  fixed-point theorem and target-side realization.
- `107_115_paper_b_finite_boundary_audit.py` — exact verifier for that
  Paper B finite boundary audit.
- `107_116_SOURCE_SIDE_FINITE_BOUNDARY_AUDIT.md` — exact boundary audit
  across Papers A and B together: the current source-side finite
  package is exact-audited as a symbolic source complex, but still
  excluded from geometric realization across both milestones.
- `107_116_source_side_finite_boundary_audit.py` — exact verifier for
  that source-side finite boundary audit.
- `107_01_function_field_preflight.py` — exact arithmetic preflight for
  point counts, closed-point counts and primitive Gram determinants; it
  does not test methodological falsifiers such as F8.

## Status

The program specification is complete and Paper 0 now has a formal draft
on the fixed control curve \(E/\mathbb F_5\).  The exact preflight
continues to certify the arithmetic anchors through \(n=16\), while the
new paper supplies the geometric chain

\[
 \Gamma_{F^n}
 \longrightarrow
 \Gamma_{F^n}\cdot\Delta
 \longrightarrow
 Z_E(u)
 \longrightarrow
 5^{-kd/2}
 \longrightarrow
 G_n^0
 \longrightarrow
 |a_n|\le 2\cdot5^{n/2}.
\]

The next source layer is also now fixed at the algebraic interface
level: `107_03` defines the raw correspondence package, separates
transpose from connected extraction, and presents the finite-support
module \(\operatorname{Div}_{\mathrm{EF}}\) required by Work Package
I-A.

The finite local intersection layer is now fixed as well: `107_04`
promotes the cyclotomic off-diagonal data to determinant lines with
canonical sections, recovers Apostol's exact \(\log p\) support on
prime-power ratios, and preserves the diagonal as an excess-intersection
object to be completed only after the archimedean metric is attached.

That archimedean completion is now written in `107_05`: the metric is
normalized by the exact Gamma--polar determinant and the matched common
cutoff identity, so the diagonal closes inside the same metrized
determinant theory rather than by importing a separate scalar formula.

Paper A is now also synthesized as a single theorem-level deliverable in
`107_06`: the finite-support intersection theorem packages `107_03`,
`107_04`, and `107_05` into one coherent arithmetic determinant theory.
Its finite cyclotomic support law now also has a separate exact audit in
`107_34`, and its connected-extraction layer now has an exact audit in
`107_35`, but the full Paper A package still does not have an audit
layer as strong as Paper 0.

Part II is now formally started as well: `107_07` fixes the algebraic
correspondence category \(\operatorname{Corr}_{\mathrm{EF}}\) and makes
explicit the key separation between raw composition and Eulerian
connected extraction.

The suspension step is now also written in `107_08`: the local prime
circles are glued through a common archimedean phase boundary, producing
an arithmetic flow object whose closed-orbit return category is
\(\operatorname{Corr}_{\mathrm{EF}}\).

Work Package II-C now also has a formal draft in `107_09`: the
renormalized test correspondence \(Z_f\) intersects the diagonal in one
joint fixed-point calculation that recovers the full prime--Gamma--polar
arithmetic side of the explicit formula, with the Davenport--Heilbronn
failure point occurring before any appeal to zeros.
Its same-tower function-field return/composition/Lefschetz shadow is now
also exact-audited in `107_36`, but the full Part II geometry remains
formalized rather than independently closed; `107_37` records the
remaining mixed/phase/archimedean audit gaps explicitly.  The finite
combinatorial shadow of the common-phase gluing is now also
exact-audited in `107_38`, and the finite mixed-tower non-collapse
shadow is now exact-audited in `107_39`.  The external Davenport--
Heilbronn falsifier is now also exact-audited in `107_40`, while the
explicit joint Gamma--pole factor is now consistency-audited in
`107_41`, while the full joint prime--Gamma--polar fixed-point page of
`107_09` remains formalized.

Part III is now also opened in `107_10`: the realization problem is
fixed at the correct level of generality, namely regular proper models
\(\mathcal X_T/\operatorname{Spec}\mathbb Z\) for finite-support data
without deleting places outside the cutoff, and with nontrivial
degree-one geometry retained from the absolute Picard/Jacobian side.

The companion realization target for III-B is now fixed in `107_11`:
the sought divisor map to \(\widehat{\operatorname{Pic}}^0\) or to the
precise Yuan--Zhang adelic category must preserve the source
Gamma--polar metric, transport the intersection pairing, and have real
kernel exactly equal to the explicit Weil radical
\(\mathfrak R_W\).

Part IV is now also laid out at theorem level.  `107_12` records the
only admissible applicability audit for invoking an existing arithmetic
Hodge theorem, distinguishing the classical/adelic route from the
alternative of proving a new Hodge--Rosati theorem in a genuinely new
category.  `107_13` then fixes the terminal identity
\(-\widehat{\deg}(\overline M_f^{\,2})=\mathcal Q_W(f)\) as the unique
new statement whose proof would let the existing Hodge theorem imply
Weil positivity and hence RH.

Part V now also has its own audit artifact in `107_14`: the phase is
tracked paper by paper and falsifier by falsifier, explicitly separating
what is already proved in the current tree from what is only formalized
as a target.  After the foundational gate audit of `107_33`, Paper 0 is
the only source foundation currently carrying an exact audited control;
Papers A and B are written and theorem-level formalized, but not yet
independently pressure-tested to the same standard.  Parts III--IV and
the terminal E1/E2 branch remain open construction/proof fronts.
`107_53` now makes the A1 boundary explicit: the candidate-model package
is structurally real, but regular properness and exact adelic
comparison remain genuine geometric gaps rather than merely editorial
ones.

Part III now also has a first concrete model candidate in `107_15`:
instead of speaking only in terms of universal finite models, the phase
now proposes \(\mathcal X_T^{(1)}\) as the regularized closure of the
finite-support incidence locus inside a compactified square of
Connes--Consani framed arithmetic divisors, together with first
candidate realized generators \(F_{\mathrm v}\), \(F_{\mathrm h}\),
\(\Delta\), \(\Gamma_{p,k}\), and \(Z_\infty\).

That candidate is now sharpened in `107_16`: the compactified framed
divisor square \(\overline{\mathfrak S}\) is equipped with explicit
vertical and horizontal boundary divisors, a common corner
\(C_\infty\), and a boundary metric line \(\mathcal L_\infty\) that is
meant to carry the Gamma--polar descent.  This turns the
compactification/metric-descent problem into a concrete corner and
boundary comparison problem.

That compactification is now pushed one step further in `107_17`: the
compactified framed-divisor factor \(\overline{\mathfrak P}_{\rm fr}\)
is given a minimal local chart atlas in the variables
\((\xi,q,\theta)\), and the closures of the finite-support graphs are
reduced to a first chartwise finite-type criterion.  The load-bearing
unknown of the next step is now isolated as the explicit finite-type
geometry of the framing coordinate \(\xi\).

That framing bottleneck is now partially resolved in `107_18`: at fixed
support level \(T\), the coordinate \(\xi\) is replaced by finite
visible rooted/cyclotomic packets \((n,\chi)\), so the graph equations
become effective finite chart data rather than abstract moduli symbols.

That next bridge is now explicitly written in `107_19`: packet charts,
packet graph loci, and order-forgetting comparison morphisms are fixed
so that the finite-support geometry of Part III can be compared
directly, packet by packet, with the determinant-line package already
proved in `107_04`.

That local missing construction is now supplied in `107_20`: the packet
chart is modeled algebraically by a cyclotomic factor tensored with a
finite idempotent rooted-label algebra, the resulting packet
intersection line is defined by a derived tensor product, and its
off-diagonal canonical norm is proved to descend exactly to Apostol's
resultant.  In particular, the rooted labels are now isolated as
norm-one unit factors in the local determinant package.

That local package is now also globalized in `107_21`: the packet lines
are glued over the candidate surface \(\mathcal X_T^{(1)}\) by
rooted-unit transition maps, producing an order-indexed global line
object whose unique admissible archimedean completion is forced through
the boundary metric line \(\mathcal L_\infty\).

That descended line package is now pushed to the realization interface
in `107_22`: the immediate candid target is fixed as an integrable
adelic metrized Picard candidate, the generatorwise realized class
\(\widehat{\mathcal M}_{f,T}^{\rm cand}\) is written down explicitly,
and the remaining Route A burden is isolated as integrability,
degree-zero, pairing transport, and exact-kernel verification.

That integrability burden is now sharpened in `107_23`: the candidate
metric is reduced to a finite chartwise logarithmic singularity model on
the atlas of `107_17`, which partially discharges the Route A
integrability/finiteness audit off the diagonal and isolates the
remaining risk at the diagonal completion step.

That degree-zero burden is now also reduced in `107_24`: the
polarization candidate is fixed as the symmetric sum of the two rulings,
the visible degree functional is written explicitly, and the primitive
correction protocol of `107_22` is shown to be the unique linear
normalization forcing degree zero with respect to that polarization.

That reduction is now pushed one step further in `107_25`: the
polarization self-intersection is decomposed into its mandatory corner
contribution plus exceptional regularization corrections, giving the
first concrete nonvanishing criterion for the denominator of the
primitive projection and first geometric skeleton formulas for diagonal
and graph degrees.

That denominator audit is now sharpened again in `107_26`: the
exceptional correction package is localized to a finite set of
polarization-active blow-up centers, and a corner-preserving
regularization criterion is stated as a sufficient condition for the
corner contribution to survive in \(H_T^{(1)}\cdot H_T^{(1)}\).

That finite criterion is now pushed down to the atlas in `107_27`: the
actual local center types A--E are listed from the equations of
`107_17`, and each currently visible polarization-active center is
proved corner-preserving under the stated regularization strategy.  The
remaining denominator problem is therefore quantitative rather than
structural.

No arithmetic Lefschetz surface, divisor map over
\(\operatorname{Spec}\mathbb Z\), or proof of RH is claimed at this
stage; those remain later work packages of Phase 107.

One important limitation is now made explicit by `107_28`: the original
elliptic preflight `107_01_function_field_preflight.py` checks the fixed
\(g=1\) control only and does not, by itself, test whether the
primitive diagonal package correctly tracks genus.

That scope correction is now pushed into the Paper 0 base documents by
`107_29`: the elliptic calibration remains proved, but genus-uniform
portability of the primitive diagonal package is explicitly left open
instead of being inferred from the \(g=1\) case.

That specific diagonal gap is now partially closed in `107_30`: the two
primitive diagonal entries and the primitive cross term are derived
uniformly in genus on \(C\times C\) by adjunction and bidegree, so the
genus factor is no longer carried only by the external genus-2
falsifier.

That uniformity is now extended further in `107_31`: composition,
transpose, diagonal trace, connected Euler extraction, and critical
balancing are all written in genus-free source form on \(C\times C\),
leaving the fixed elliptic paper as the exact audited anchor rather than
the only place where the chain is written out.

That genus-free generalization is now integrated in `107_32`: the whole
source chain on \(C\times C\) is gathered into one document, so what
remains open in Paper 0 is no longer mathematical generality but only
whether to replace the fixed-curve exposition by one fully integrated
master paper.

The higher-rank absolute-dimension branch now has a genuine negative
result in `107_147`.  Modeling the Euclidean projective tensor norm on
the square by the trace norm on \(M_2(\mathbb Z)\) produces
superlogarithmically many mandatory primitive boundary rays, so this
natural tensorial mass functional cannot support a Riemann--Roch formula
with dimension linear in the degree.  The exact verifier checks
\(d_*(1)=4\), \(d_*(2)=12\), and the Gaussian-integer witness family.

The natural arithmetic-Jacobian target is also sharply restricted by
`107_148`.  Connes--Consani's published prime class
\(\mathbb Z[1/p]\) is idempotent and noninvertible, so their Picard
monoid cannot receive the signed group \(\operatorname{Div}_{\mathrm{EF}}\)
additively; its Grothendieck completion kills those prime classes.  The
Jacobian remains a support space, but the Phase 107 realization target
must be a non-idempotent enhancement or a genuine metrized Picard group.

The direct Hodge target is dimensionally corrected in `107_149`.
Weil's square has generic dimension two, so its regular proper
arithmetic model has relative dimension two and the Yuan--Zhang form is
the polarized triple intersection
\(\overline M_f^{\,2}\cdot\overline H_T\), with
\(M_f\cdot H_T=0\).  The earlier unpolarized formula belongs only to a
separate curve route that Phase 107 has not constructed.

The square mass inherited from Connes--Consani is fixed in `107_150`.
The projective tensor norm of \(\ell^1\) factors is entrywise
\(\ell^1\), not the trace norm, and its absolute dimension grows
linearly with the divisor degree by `107_146`.  Thus `107_147`
closes only the Euclidean trace-norm branch; the published-CC tensor
branch remains viable for the construction of \(H^0\).

Middle cohomology for the prospective square is constructed formally in
`107_151`.  For any bounded three-term Cech complex inside
Eilenberg--MacLane modules, \(H^1_{\rm tol}\) is the cocycle module with
the bounded-image tolerance relation.  It is functorial, invariant under
complex isomorphism, and recovers ordinary \(H^1\) in the subgroup case.
The remaining obstruction is now the geometric construction of the
square's Cech complex in this abelian ambient category.

The canonical free abelian lift of the 2026 absolute stalk is ruled out
by `107_152` and `107_153`.  Its monomial basis gives
infinite CC dimension, and every nonconstant subgroup stable under the
bilateral local Frobenius has infinite rank.  Hence a viable Cech lift
must be genuinely derived/non-free or place Frobenius between finite
levels instead of preserving each truncation.

That finite-level alternative is constructed in `107_154`.
The coordinates \(c p^j\) give finite bounded modules, bilateral
Frobenius maps them to the next level, and two commuting maps provide
the square rulings.  Their filtered colimit recovers the full absolute
stalk.  What remains is to prove that divisor-controlled Cech
cohomology stabilizes and that the local systems descend globally.

The stabilization question is reduced to an exact criterion in
`107_155`: \(H^0(D)\) stabilizes precisely when the divisor admits
only finitely many monomial rays in the filtered union.  The next
geometric theorem must produce that finite support rule and prove its
Frobenius covariance; taking the full level is provably insufficient.

The published pullback sheaf supplies half of that rule, as recorded in
`107_156`: global sections have finite prime support.  It does
not bound the denominator/Frobenius depth at one prime.  Therefore the
remaining local theorem is now exact: derive a finite depth bound from
the return support \(k\log p\le T\) of the divisor itself.

The older finite-chart terminology is corrected in `107_157`.
Visible orders are divisors of one finite integer \(L_T\), hence form a
gcd/lcm lattice with partial multiplication, not a finite
multiplicative monoid.  Products leaving the lattice pass to the next
support level, consistently with `107_154`.

Here \(L_T=\operatorname{lcm}(1,\ldots,\lfloor e^T\rfloor)\), so
\(\log L_T\sim e^T\) and enumerating its divisors is already impossible
at \(T=5\).  The implementation therefore stores only the exponent
vector \((K_p(T))_p\); this is now a required representation invariant.

With that correction, `107_158` records the immediate local
stabilization corollary for the
rooted sector: \(X_T^\vee=(1/L_T)\mathbb Z/\mathbb Z\) is finite and its
\(p\)-depth is exactly \(\lfloor T/\log p\rfloor\).  The local
rooted/cyclotomic \(H^0\) obstruction is therefore closed; global
descent and construction of a proper square remain open.

The discrete rooted descent is completed in `107_159`.  Level
inclusions, dual frame projections, and Chinese remainder glue the
prime sectors canonically, with limits \(\mathbb Q/\mathbb Z\) and
\(\widehat{\mathbb Z}\).  The unresolved row-(a) work is now
representability of these charts and descent of the metric/intersection
theory to a proper relative-dimension-two model.


The discrete coordinate is represented geometrically in `107_160`
by the finite flat proper regular scheme
\(\coprod_{n\mid L_T}\operatorname{Spec}\mathbb Z[\zeta_n]\).
Packet characters now have exact order \(n\), as required by the
primitive cyclotomic chart.  Only the dynamical and archimedean factors
remain to produce the required relative dimension two.

The cross-prime restriction test is closed negatively in `107_161`.
For the published CC pullback sheaf, the generic stalk is zero and
sections are independent finite-support prime families.  Restriction
maps therefore carry no nonzero datum from one closed prime to another.
Any viable global square must exhibit additional adelic or archimedean
glue rather than attributing that glue to the prime-chart restrictions.

The first Abel--Jacobi square is rejected in `107_162`: equipping the
fiber product only with the pullback of the base structure sheaf leaves
all local equations constant along \(C_p\times C_p\), so neither its
diagonal nor its Frobenius graphs are Cartier.  This is a no-go for the
base-sheaf construction, not for Abel--Jacobi geometry with a relative
orbit sheaf.

The required local relative equations are lifted in `107_163` directly
from the CC rational Frobenius congruence.  The map
\(X^aY^b\mapsto T^{na+mb}\) has kernel generated by the directed family
\(X^{m/p^k}-Y^{n/p^k}\).  At finite depth \(R\), its deepest root is one
exact generator; omitting it fails.  These maps are contractive on the
bounded \(\ell^1\) modules and can therefore enter the tolerant middle
cohomology of `107_151`.

This lift does not descend additively to the reduced Newton square.
`107_164` proves a structural no-go: every additive map from an
idempotent monoid to an abelian group is zero, and convex-hull
identification already kills each individual monomial.  Cohomology must
therefore be built from enriched unreduced supports; reduced Newton
polygons can only be their non-additive tropical shadows.

The minimal global refinement is constructed in `107_165` as the free
support semiring \(\mathbb N[\mathbb Z^2]\), with coefficient ring
\(\mathbb Z[\mathbb Z^2]\).  It is equivariant under both Frobenius
rulings, tropicalizes onto the CC square, and carries the bounded
modules and correspondence kernels already proved locally.

Ordinary derived invariants of that topos are rejected in `107_166`.
With \(r\) visible primes they have Koszul amplitude \([0,2r]\), and
nonzero cohomology above degree two appears immediately.  The required
surface amplitude must therefore come from a genuine geometric Cech or
foliated three-term complex, not from the raw monoid action or an ad hoc
truncation.

That amplitude is verified locally in `107_167`.  The compact CC
mapping tori satisfy
\(H^\bullet(\Gamma(p)\times\Gamma(q))=(1,2,1)\), so their periodic
products carry the required three-term surface complex.

`107_168` realizes the enriched support inside the Fourier algebra of
those mapping tori and proves exact compatibility with Frobenius and
rational correspondences.  It also exposes the next obstruction: the
leafwise derivative multiplies Fourier mode \(q\) by \(2\pi i yq\), so
the CC coefficient mass is not uniformly bounded and the 2022 integer
dimension does not directly apply to the de Rham differential.

The mass-controlled replacement is constructed in `107_169`.  Its
rooted torus chain complex has uniform differential bounds, homology
\((1,2,1)\), and symbolic subdivision maps for \(L_T\mid L_{T'}\), so
production never enumerates \(L_T^2\) cells.

`107_170` prevents overpromotion of that model: its \(H^4\) vanishes,
so every ordinary cup-product intersection of divisor classes is zero,
whereas the fixed function-field control has
\(\Gamma_1\cdot\Delta=N_1=9\).  The cellular complex is an additive
cohomology model only; intersection still requires a relative trace or
a genuine complex-surface top class.

That complex-surface alternative is calibrated positively in `107_171`.
The fixed Paper-0 curve lifts to the rational CM curve with
\(j=-32768\), and the CM element
\(\alpha=(-3+\sqrt{-11})/2\) lifts its Frobenius.  On
\(E_{\rm CM}\times E_{\rm CM}\), graph intersections recover every
\(N_n\), and the centered Hodge form is exactly the Paper-0 form through
all iterates.  This is a theorem for the fixed CM control, not a
construction of the universal arithmetic surface or of row (c) for
Riemann zeta.

`107_172` strengthens this from two matching fibres to one arithmetic
family over
\(\operatorname{Spec}\mathcal O_{\mathbb Q(\sqrt{-11})}[1/11]\):
the graph--diagonal intersection is the finite flat kernel
\(\ker(\alpha^n-1)\), of constant rank \(N_n\).  The fixed
characteristic-5 and complex intersections are its special and generic
fibres.

`107_173` then constructs an everywhere-good model after the explicit
quartic extension \(L=\mathbb Q(\alpha,w)\),
\(w^2=2\alpha+3\).  The integral equation
\(y^2+w y=x^3+\alpha x^2-(\alpha+1)x\) has discriminant 1.  Its square
is therefore a proper smooth relative surface over all of
\(\operatorname{Spec}\mathcal O_L\), carrying the complete Paper-0
package.  The base is not \(\operatorname{Spec}\mathbb Z\), and the
construction realizes the fixed CM elliptic zeta function rather than
Riemann zeta.

`107_174` proves that this fixed-control success does not descend by
Galois averaging.  The oriented CM graph and its conjugate are distinct
(their mutual intersection is 11), while their invariant average
preserves the point-count scalar but not the Frobenius composition law.
The CM graph descent route is therefore closed; a universal construction
must use a genuinely different correspondence, such as the
Galois-sensitive idele translations and arithmetic linking of the 2026
arithmetic Jacobian.

`107_175` then tests that Galois-sensitive channel on the original
20a1/36a4 forcing pair.  Universal linking at 2 contains both required
quadratic signs, but the complete universal source datum is identical
for the two targets.  Choosing different quotient characters would
import the component target rather than derive it.  Rooted/linking data
therefore has the missing Galois capacity but does not by itself reopen
the old \(S3\) gate.

`107_176` proves that the idele action cannot be transferred to an
ordinary smooth Picard group or Tate curve and then intersected with the
diagonal.  Nonidentity group translations have empty equalizer, while
the identity has the whole diagonal.  Five real groups, including a
supersingular elliptic curve and a genus-2 Jacobian, certify the no-go.
The published factor \(1/|1-u|_v\) is necessarily a transverse boundary
weight, not an ordinary fixed-point count.

`107_177` tests the remaining transverse scaling directly.  Its generic
graph intersection has constant multiplicity 1, while
\(1/|1-(1+p^k)|_p=p^k\); over \(\mathbb Z_p\) the closures acquire an
entire vertical excess component.  Thus even the correct normal action
requires equivariant/derived localization and cannot be inserted as an
ordinary arithmetic intersection number.

`107_178` constructs the required replacement locally.  The actual
Koszul differential has Euler class \(1-u\), and equivariant
localization produces \((1-u)^{-1}\); normalized absolute value recovers
the published factor \(1/|1-u|_v\) exactly.  This is a local
equivariant boundary class, not yet a global divisor or a class in the
domain of arithmetic Hodge index.

`107_179` proves that this type mismatch is structural.  The ordinary
forgetful map sends the normal character \(t\) to 1, hence sends the
inverted Euler class \(1-t\) to zero and cannot extend to the localized
coefficient ring.  Applying existing Arakelov/Hodge theorems now
requires either a proved global cancellation of all denominators or a
new equivariant arithmetic Hodge theorem.

`107_180` closes the cancellation alternative in finite-type proper
coherent geometry.  Equivariant localization on \(\mathbb P^1\) cancels
the two fixed-point denominators and produces a regular character; the
same happens for every \(\mathcal O(n)\).  Such a class can enter
ordinary Arakelov theory only after losing the uncancelled local factor.
The remaining architecture requires a renormalized equivariant
arithmetic Hodge theory.

`107_181` supplies the complementary positive calibration.  On the
actual toric surface \(\mathbb P^1_{\mathbb Z}\times\mathbb P^1_{\mathbb
Z}\), evaluated inverse-Euler weights multiply a primitive ruling class
of square \(-2\), so all resulting squares remain negative.  Localized
weights are compatible with Hodge sign after real evaluation; what is
still missing is the global primitive realization map.

`107_182` constructs the finite-prime global Green channel in
\(\Re s>1\).  The reduced local inverse-Euler class is
\(p^{-s}/(1-p^{-s})\); multiplying by \(\log p\) and summing gives
exactly \(-\zeta'/\zeta\).  The channel is genuinely Eulerian and hence
unavailable for Davenport--Heilbronn.  Critical-strip continuation,
Gamma completion, and divisor-valued realization remain separate steps.

`107_183` completes that scalar channel with the unique Gamma and pole
terms, obtaining \(-\xi'/\xi\).  High-precision checks verify the exact
decomposition, odd functional symmetry about \(1/2\), and cancellation
at \(0,1\).  The analytic channel is now complete; Mellin-test
distribution and divisor/Green-current realization remain open.

`107_184` Mellin-inverts the channel on smooth/Schwartz tests.  The
finite part becomes exactly
\(\sum_{p,k}\log p\,g(k\log p)\), while the completed channel defines
the corresponding Gamma/pole distribution.  Independent contour and
prime-power computations agree below \(2.5\times10^{-9}\).  The next
gap is geometric Green-current realization, not the scalar explicit
formula.

`107_185` puts the finite local Green class on Deninger's actual prime
circles.  The twisted operator \(d/dx+s\) on the orbit of length
\(\log p\) has determinant \(1-p^{-s}\), and its periodic Green kernel
returns \(p^{-s}/(1-p^{-s})\).  Orbit length times return value is
exactly the local summand of \(-\zeta'/\zeta\).  This is a genuine
row-(b)/(c) bridge, though not yet an Arakelov Green current.

`107_186` realizes the Gamma contribution as a regularized Green trace.
The Hadamard finite part of the resolvent of the number operator is
\(-\psi(a)\); at \(a=s/2\) it supplies exactly the archimedean term.
Direct sums through one million modes and completed assembly pass.  All
scalar local Green operators now exist, but no global Arakelov current
or intersection pairing has yet been produced.

`107_187` assembles the orbit and number-operator determinants.  The
prime product gives \(\zeta(s)\), the zeta determinant of
\(N+s/2\) gives the reciprocal Gamma factor, and the completed product
is exactly \(\xi(s)\).  Its logarithmic derivative recovers the Green
channel.  This constructs a global analytic determinant function, not
yet a determinant-line sheaf on the arithmetic space.

`107_188` upgrades the finite products to a directed determinant-line
system on Connes--Consani's semilocal index category.  Inclusion of
finite place sets tensors by the missing local Euler factors; all triple
transitions satisfy the cocycle, and the cofinal section converges to
\(\xi\).  Sheaf descent on \(\operatorname{Spec}\mathbb Z\), and then
descent to its absolute square, are not yet asserted.

`107_189` proves the curve-level sheaf descent.  On each semilocal open
of \(\operatorname{Spec}\mathbb Z\), restriction multiplies by the
missing Euler factors; division by the accumulated product trivializes
all restrictions and proves the Cech equalizers.  The resulting
rank-one spectral sheaf has completed generic section \(\xi\) for
\(\Re s>1\).  No external product, diagonal pairing, or square-level
intersection has yet been constructed.

`107_190` constructs the external product on the product semilocal site.
Two-coordinate restrictions and Cech descent are exact after division by
the accumulated factors \(g_S(s_1)g_T(s_2)\); the generic section is
\(\xi(s_1)\xi(s_2)\), and diagonal pullback gives the tensor square with
section \(\xi(s)^2\).  The same gate proves that the specialization
\((s_1,s_2)=(ns,ms)\) yields \(z_p(ns)z_p(ms)\), not a single collapsed
Euler weight, so it does not manufacture the correspondence
\(\Lambda_{n,m}\).  The square-level line sheaf now exists, while the
proper surface, top class, Deligne pairing, Green current, and Hodge form
remain unconstructed.

`107_191` closes the immediate unmetrized pairing route.  The Euler
transition cocycles on the curve and square are explicit coboundaries,
so their ordinary Picard and first-Chern classes vanish.  After the same
gauge change the canonical section is \(Z_\infty\), nowhere zero on
\(\Re s>1\), and contributes no divisor.  Therefore tensor products,
ordinary \(c_1\), or an unmetrized Deligne pairing cannot recover the
prime distribution.  Any surviving route must add a genuinely
nontrivial metric/current, a meromorphic boundary extension, or a
renormalized secondary class.

`107_192` identifies the completed Green channel with the flat
logarithmic connection \(-d\log\xi\).  Its coefficient is exactly
\(-\xi'/\xi\), but \(dd^c\log|\xi|=0\) throughout the Euler
half-plane.  Thus the smooth determinant metric has zero Chern curvature
and cannot supply row (c).  The surviving target is now narrower:
a singular relative extension or an analytic-torsion/Bott--Chern
secondary current on geometry satisfying the arithmetic Lefschetz
hypotheses.

`107_193` performs the singular continuation.  The source-derived entire
determinant satisfies \(dd^c\log|\xi|=[Z_\xi]\), and its logarithmic
connection has the expected integral residues at actual zeta zeros.
Hardy's theorem makes this divisor infinite, so it cannot be the divisor
of a meromorphic section on any proper finite-type algebraic spectral
curve.  This constructs a spectral divisor current while closing the
ordinary proper spectral-compactification route; it still does not put
that current on the Connes--Consani square or supply a Hodge form.

`107_194` closes direct use of the published analytic-torsion current
on a prime orbit.  Each Deninger orbit is a real one-dimensional circle
with no complex/Kahler structure.  Its return translation has derivative
one and zero tangent Euler class, whereas its twisted holonomy
determinant \(1-p^{-s}\) is nonzero.  Hence the orbit determinant of
`107_185` is not already a Koehler--Roessler/Bismut--Goette current.
Any such bridge must construct an ambient complex transverse normal
action and prove comparison with the orbit kernel.

`107_195` tests the standard flat Tate-torus repair.  With
\(q=p^{-s}\), Kronecker's limit formula introduces the full eta tower
\(q^{1/6}\prod_{n\ge1}(1-q^n)^4\), so its determinant is not the
single orbit mode \(|1-q|^2\) up to any universal constant.  Fifteen
fixed real tori reject that identification with controlled product
tails.  A successful complex transverse bridge must now derive a
virtual cancellation or relative determinant rather than truncate the
extra modes by hand.

`107_196` constructs the surviving virtual cancellation.  The exact
number-filtration sequence
\(0\to\mathcal F_{\ge2}\to\mathcal F_{\ge1}\to\mathbb C_{(1)}\to0\)
implies \(D_1(q)/D_2(q)=1-q\) by Fredholm multiplicativity.  At
\(q=p^{-s}\) it recovers both the prime-orbit determinant and its
Green connection.  This is a canonical relative determinant, not an
eta truncation; what remains is to realize the exact sequence in a
geometric/secondary category supporting arithmetic Lefschetz and Hodge.

`107_197` prevents that relative determinant from being mistaken for a
secondary current.  With the standard number-basis metric, every finite
tail sequence is orthogonally split, so its Bott--Chern secondary class
is zero.  The determinant quotient remains nontrivial, but it is not a
metric anomaly.  Any next secondary realization must obtain an
off-diagonal coupling or superconnection from the actual dynamics.

`107_198` rejects the simplest such coupling.  A trace-class weighted
unilateral shift has zero trace in every positive power and Fredholm
determinant one, as does its backward counterpart.  It therefore cannot
produce \(1-q\); adding a diagonal quotient mode does so only by
reinstalling the known target.  The surviving local candidates require
a bidirectional closed loop or a boundary eta class.

`107_199` constructs the bidirectional option.  A two-state loop has
determinant \(1-ab\); requiring return weight \(ab=p^{-s}\) and
transpose symmetry forces \(a=b=p^{-s/2}\).  It recovers the orbit
determinant and Green connection, while asymmetric factorizations are
shown to collide in determinant and fail balance.  This supplies a
canonical local odd operator, but not yet its global secondary current.

`107_200` globalizes those blocks as
\(D_s=\bigoplus_pD_{p,s}\).  The operator is Hilbert--Schmidt on the
whole Euler half-plane, and pairwise cancellation in the
Carleman--Fredholm determinant gives
\(\det_2(1-D_s)=\zeta(s)^{-1}\).  Its logarithmic derivative is exactly
the finite Green channel.  This replaces the formal prime product by
one global Schatten-class operator; continuation across \(\Re s=1\),
Gamma completion, square geometry, and Hodge remain open.

`107_201` determines why that operator does not continue naively.
The balanced family belongs to \(\mathcal S_m\) for \(\Re s>2/m\),
making \(m=5\) minimal on the critical line, but higher regularized
determinants retain even counterterms.  In particular
\(\det_5=\zeta^{-1}\exp(P(s)+P(2s)/2)\) in the common Euler domain.
Replacing \(\det_2\) by \(\det_5\) therefore requires a separate
source-derived global counterterm.

`107_202` excludes the existing Gamma/pole sector as that counterterm.
The combination \(P(s)+P(2s)/2\) cancels its apparent branch at
\(s=1/2\), but retains fractional monodromy at \(s=1/3\) and further
reciprocal integers.  Standard completed archimedean factors are
holomorphic and nonzero at \(1/3\), so they cannot cancel it.  Any
continuation must use prime-side relative branch data.

`107_203` derives that prime-side correction exactly at every finite
support through the universal order-change formula.  Nevertheless its
ordinary cofinal product tends to zero at \(s=1/2\), whereas the
analytic value \(1/\zeta(1/2)\) is nonzero.  Analytic continuation is
therefore not a norm or strong determinant limit of the prime blocks;
the remaining operator route requires nonlocal summation or a
nuclear-space trace.

`107_204` identifies that nuclear trace with Meyer's published
construction.  His quotient is defined from the integer-dilation Zeta
operator, not from a zero list, and its virtual nuclear character is the
explicit formula.  The geometric prime character still requires Euler
factorization, so Davenport--Heilbronn is rejected before that step.
Meyer supplies continuation but no Hodge positivity.

`107_205` proves the exact comparison with the new prime Dirac operator:
under Mellin transform, Meyer's \(Z\) has multiplier \(\zeta(s)\),
which is \(\det_2(1-D_s)^{-1}\).  The finite-prime
determinant-to-nuclear-trace bridge is therefore constructed on
\(\Re s>1\).  The remaining gap is to realize the nuclear character as
a current/intersection on the arithmetic square and prove its Hodge
sign.

`107_206` transports the balanced finite-prime character through the
published Morishita bridge.  Meyer's two nuclear trace halves are
exchanged by the modular involution induced by flow reversal, so their
sum descends while either oriented half does not.  On normalized orbit
traces the bridge has an exact packet kernel: precisely the
coefficient-sum-zero combinations disappear.  Thus the base
Connes--Consani orbit retains the zeta character but not packet/Galois
refinements.  This is a distributional support comparison, not yet a
current or intersection on the arithmetic square.

`107_207` supplies an actual local complex geometry for the relative
Fock determinant.  In the new Connes--Consani absolute curve, the
archimedean-local point moduli is \(\mathbb C\), with a trivial fixed
point at zero and scalar \(W_\infty\)-action.  The Fock tails are the
Hardy completions of \(\mathfrak m^r\), so
\(\mathfrak m/\mathfrak m^2\) is the cotangent line and its normal
Lefschetz determinant is \(1-p^{-s}\), invariant under nonlinear
coordinates.
The proper Tate quotient deletes zero; the fixed ideal sequence has not
yet been compactified or pushed to the arithmetic square.

`107_208` proves that this missing compactification cannot be ordinary.
The orbit \(\{p^n\}\) accumulates at the fixed point, so
\(\mathbb C/p^{\mathbb Z}\) is not even \(T_1\); the projective coarse
quotient fails for the same reason at zero and infinity.  Nor can one
append a Hausdorff boundary to \(E_p\), since it is already compact.
The surviving globalization must push the cotangent class before the
quotient or use a stacky/relative degeneration with a new index theorem.

`107_209` executes the first surviving option locally.  For the regular
embedding of the trivial point in the absolute archimedean moduli line,
the equivariant derived self-intersection is
\(\lambda_{-1}(\mathfrak m/\mathfrak m^2)=1-\chi\).  Evaluating the
scale character at \(\chi=p^{-s}\) recovers the Euler factor
\(1-p^{-s}\), and its logarithmic derivative recovers the prime Green
weight.  This is a genuine local derived intersection formed before the
coarse quotient; a proper numerical pushforward and global square
pairing remain absent.

`107_210` globally assembles those local classes on the Euler
half-plane.  The direct sum of conormal characters
\(Q_s=\bigoplus_p p^{-s}\) is trace class exactly for \(\Re s>1\), and
its Fredholm determinant is the product of the derived
self-intersections, \(\det(1-Q_s)=\zeta(s)^{-1}\).  The logarithmic
trace is the finite Green character.  This constructs a nuclear
analytic pushforward, not a proper geometric pushforward; trace-class
continuation to the critical line is impossible and remains delegated
to Meyer's Frechet quotient.

107_211 supplies the missing proper local pushforward without
contradicting the earlier compactification no-go.  Before taking any
orbit quotient, compactify the absolute moduli line equivariantly to
\(\mathbb P^1\).  In the proper square, the diagonal and scaling graph
have normal determinant \(1-\chi\) at the canonical trivial point, and
the supported derived class pushes to that same numerator with no
infinity contribution.  The inverse Euler pole is still not a coherent
class and ordinary augmentation sends the numerator to zero.  Hence
local properness is closed, while the global arithmetic/Hodge
pushforward remains open.

107_212 gives the finite-support arithmetic realization of the Green
coefficient.  The prime divisor \(\widehat{[p]}\) has arithmetic degree
\(\log p\), and its product with the logarithmic character
\(\chi_p/(1-\chi_p)\) has degree
\(\log p\,p^{-s}/(1-p^{-s})\).  This agrees exactly with the derivative
of the proper Euler numerator and explains why ordinary \(G_0\), which
kills \([\mathbb F_p]\), was too small.  Every finite support now has an
actual localized arithmetic degree; the infinite prime sum is still
only nuclear and no renormalized Hodge theorem is claimed.

107_213 proves that the existing arithmetic Lefschetz theorems do not
yet globalize this class.  Tang works over
\(R(\mu_n)=\mathbb Z[T]/(1-T^n)\), which cannot evaluate at
\(T=p^{-s}\) or approximate it by roots of unity.  The broader
Koehler--Roessler torus residue formula applies to the infinitesimal
algebraic class, but its analytic-torsion identity is proved on the
unit circle, not at the nonunitary prime character.  A holomorphic
nonunitary extension, including its \(R_g\) anomaly, remains necessary.

107_214 proves that the naive extension of that anomaly is impossible.
For a flat normal line, \(R_g\) is a difference of order derivatives of
polylogarithms.  At \(q=p^{-s}\), the reciprocal crosses the standard
cut and creates monodromy \(2\pi i/(s\log p)\).  Multiplication by the
arithmetic prime degree cancels \(\log p\), leaving \(2\pi i/s\).
Thus the anomaly must retain the logarithmic lift \(s\log p\) and be
combined with a generic/white-light subtraction before summing primes;
it cannot be a single-valued function of the torus character alone.

107_215 supplies the minimal scalar boundary correction on that
logarithmic lift.  The forced term \(\log(1-x)/\log x\) cancels the two
lateral values and produces a real relative prime anomaly.  Direct
evaluation on five primes then rules out its identification with the
Gamma Green term prime by prime.  A global generic-point subtraction is
therefore necessary; no nonunitary arithmetic direct-image theorem is
claimed.

107_216 proves that this scalar correction cannot be globalized by an
ordinary prime sum.  Jonquiere inversion reduces it to a digamma
expression and gives
\(R^{\mathrm{rel}}(p^{-s})=\log\log(p^s)+\gamma-1+o(1)\); after
arithmetic weighting, the local terms grow like
\(\log p\,\log\log p\) and do not tend to zero.  Thus the only surviving
route must form a virtual global operator quotient before taking traces,
as in Meyer.  Equality with Meyer's archimedean operator term remains
open.

107_217 returns to row (a) and computes the first genuinely twisted
integral middle cohomology of the finite rooted square.  For a
cyclotomic character twist, \(H^0=O/I\) and \(H^1=I^{-1}/O\) have equal
order \(N(I)\), while \(H^2=0\); prime-power effective character orders
carry torsion that disappears after complexification.  This repairs the
claim that every nontrivial Fourier mode is simply acyclic, but does not
yet construct \(H^1(O(D))\) or its level transitions.

107_218 tests those transitions and finds a structural mismatch.  The
rooted normalization keeps an old root \(\zeta\) fixed, but cellular
subdivision restricts it by the power map \(\zeta\mapsto\zeta^d\).  The
two agree only in exceptional orders dividing \(d-1\), and the apparent
repair \(x\mapsto x'\) is not a map of the quotient rings.  Therefore
the twisted groups of 107_217 do not descend through 107_169 as written;
the next viable model must retain restriction and transfer separately
or work componentwise on the cyclotomic normalization.

107_219 implements the componentwise repair.  For labels of orders
\(n,m\), their two-root Koszul complex lives over
\(\mathbb Z[\zeta_{\operatorname{lcm}(n,m)}]\); open-and-closed inclusion
of normalized components leaves the complex and its cohomology literally
unchanged at every later level.  This constructs finite-support twisted
\(H^1\) descent, including mixed acyclic components and genuine torsion.
The comparison with the published divisor modules \(O(D)\) remains open.

107_220 proves that this comparison cannot be a direct additive map from
the published adelic \(H^1(D)\): \(\mathbb A_\mathbb Q\) is divisible
and every map to the finite cyclotomic torsion is zero.  The comparison
must pass through Pontryagin duality or a derived interface.

107_221 constructs the componentwise Pontryagin-dual interface.  The
correct dual middle group is
\(I^{-1}\mathfrak D^{-1}/\mathfrak D^{-1}\), not \(I^{-1}/O\), and the
trace pairing with \(O/I\) is perfect.  The codifferent is therefore a
forced local dualizing twist.

107_222 globalizes that twist over the finite rooted normalization as
\(\coprod_{n\mid L}\mathfrak D_n^{-1}\).  Pulling back the base canonical
divisor \(-2\{2\}\) alone fails because components ramify at odd primes
such as 3 and 5.  The relative dualizer is constructed and stable, but
absolute Serre duality on the sought square is still open.

107_223 prevents the resulting flat character complexes from being
misidentified with divisor cohomology.  Their Euler class and every
local torsion Euler length vanish, whereas the published CC RR
characteristic grows with the divisor.  The rooted torsion remains valid
as flat local-system cohomology, but a genuine \(O(D)\) realization must
introduce a divisor-dependent nonflat transition, first Chern class, or
bounded/tolerance structure.  The no-go concerns ordinary rank/length
Euler characteristic, not integer dimension after changing tolerances.

107_224 proves where the missing archimedean variation must live.  Any
additive map from the real divisor coefficient to an integral Chern
class or finite-rank Neron--Severi group is zero by divisibility.  Since
the CC integer Euler dimension varies along that real direction, the
variation is forced into metrics, Green functions, mass bounds, or
tolerance relations.  Rounding the real coefficient into a Chern number
is nonadditive and therefore inadmissible.

107_225 tests the finite cyclotomic torsion with the canonical Minkowski
quotient metric and closes it as the archimedean tolerance carrier.  A
finite metric group has bounded, eventually constant tolerant dimension;
the real controls freeze while the CC circle dimension must diverge.
The torsion survives only as a distinguished stratum of the full torus.

107_226 proves that the full covolume-one Minkowski torus has the needed
capacity.  A volume-covering argument forces tolerant dimension at least
\(\lceil\log_3(1/(v_d\lambda^d))\rceil\), recovering the CC slope in
dimension one and multiplying it by the cyclotomic degree.  A matching
balanced-generator upper bound, and hence RR, remain open.

107_227 turns the three preceding obstructions into an exact target
selection theorem. The real archimedean divisor direction is invisible
to every finitely generated algebraic Chern or ordinary Euler target,
but it survives tensor product in the real kernel of a metrized Picard
object. The CC integer dimension must therefore be a nonlinear invariant
of metric, Green, mass, or tolerance data; another finite-rank \(c_1\)
cannot close row (a).

107_228 closes the finite-ray condition of 107_155 as the wrong gate for
the full periodic divisor cohomology. The published Scaling Site RR
theorem forces the filtered topological dimensions of every
positive-degree \(H^0(D)\) to grow like \(p^n\) in normalized dimension,
so they cannot stabilize at finite Frobenius depth. The correct target
is a compatible pro-filtration with a renormalized continuous dimension,
not a divisor-derived finite-depth cutoff. The finite rooted sector may
still stabilize as a discrete factor.

107_229 constructs the first nonzero cofinal pro-dimension on the
two-ruling levels. It proves that the rectangular filtration of 107_154
has normalized density zero and replaces it by the simultaneous real
and \(p\)-adic slope window
\(N_p(A,R)=p^{-R}\mathbb Z\cap[0,A]\). Its mass-one normalized
dimension converges to \(AB\) on the square independently of the
relative depth rates. This is an exact slope-support density, not yet
the covering dimension of the actual divisor module \(H^0(D)\). On one
ruling, however, the full published proof gives the exact dimension
\(\alpha p^n-p+1\); it differs from the norm-adapted support count by
exactly \(p\), so 107_229 now recovers the actual one-ruling continuous
dimension in the limit.

107_230 closes the naive Cartesian square of those actual section
spaces. Their covering dimension is additive, so division by
\(p^nq^m\) forces the two-ruling limit to zero along every cofinal path.
The square must contain genuinely mixed parameters with multiplicative
growth; a Cartesian pair of one-variable sections cannot produce the
bidegree-two RR or intersection term.

107_231 constructs that missing mixed capacity at finite level. The
explicit generators from the published periodic RR proof yield
\((N-p+1)(M-q+1)\) external-sum basis functions with product dominance
rectangles. Independent max-plus coefficient perturbations are recovered
by evaluation, producing an actual bivariate section cell whose
normalized dimension tends cofinally to \(\alpha\beta\). The complete
square sheaf, its upper bound, and descent remain open.

107_232 closes the matching upper bound for special external divisors.
The appendix of the full Scaling-Site paper proves that the CC functions
used in 107_231 are exactly all extremal rays and generate the complete
one-ruling module. Their intrinsic external tensor is therefore
generated by the product set; its exact covering dimension is
\((N-p+1)(M-q+1)\), and its normalized limit is \(\alpha\beta\).
Extension to arbitrary and genuinely mixed divisors, plus global
cross-prime descent, remains open.

107_233 extends the result from special to arbitrary external divisors.
The effective-inclusion and principal-translation maps used in the
published one-ruling RR proof tensorize as embeddings, so the special
product dimensions squeeze the general limit to
\(\max(\deg D,0)\max(\deg E,0)\), independently of the cofinal path and
without discarding the component class. External periodic \(H^0\) is
therefore closed locally; intrinsically mixed divisors and global glue
remain open.

107_234 closes the global tensor carrier for arithmetic divisor sheaves.
Using the Picard/sheaf construction of arXiv:2602.15941v1, it proves exact
finite flat descent and equality of the archimedean projective mass with the
product-divisor mass. A canonical external \(\mathcal O(D)\)-module now exists
on the product topos and retains the rooted/Galois channel. This closes
module-level cross-prime descent, but not the comparison with periodic
tropical \(H^0\), intrinsically mixed divisors, \(H^1\), or RR on the square;
row (a) remains partial.

107_235 rules out the direct comparison from that carrier to periodic
tropical \(H^0\). The former is assembled from countable Gamma modules over
rank-one subgroups of \(\mathbb Q\); the latter contains the real open cells
of 107_231. Cardinality alone forbids surjectivity. Therefore the only
surviving route is scalar extension to \(\mathbb R_{\max}\), or analytic
completion followed by the structure-sheaf tropicalization of
arXiv:2606.06604v1. The divisor-module/eigenspace descent is not proved in
that paper and remains the unique active gate.

107_236 executes the surviving comparison in the correct category. The
published Legendre base change from \(\mathbb B\) to
\(\mathbb R_{\max}\) tensorizes, after functional reduction, to finite
maxima of bivariate affine functions \(hx+ky+c\). This supplies a canonical
Frobenius-covariant structure sheaf on the product Scaling topos and
identifies its external divisor modules with those computed in 107_232--233.
`SCALING_SQUARE_EXTERNAL_H0` is therefore constructed. Intrinsically mixed
correspondence divisors, \(H^1\), and square RR remain open, so row (a) stays
partial.

107_237 constructs the intrinsically mixed correspondence divisor after the
completion forced by continuity. The potential
\(U_f=\int f(\lambda)\max(y-\lambda x,0)d^*\lambda\) is homogeneous DC and
has angular curvature \(f(r)/r\). This simultaneously proves a finite-PL
Cartier no-go and realizes \(D(f)\) as a Frobenius-covariant distributional
divisor current. The two Weil moments become its two ruling degrees and, when
zero, force compact angular support. Intersection and RR for this DC
completion remain open; row (a) stays partial.

107_238 proves that the naive local DC intersection cannot supply the missing
pairing. Homogeneous correspondence potentials have pointwise proportional
rank-one Hessians, so their mixed Monge--Ampere density is zero; distinct
Frobenius rays meet only at the compactification corner. The required Weil
term is therefore forced to be a global corner/diagonal renormalization, not
an interior Hessian integral.

107_239 constructs the resulting numerical corner pairing intrinsically as
the finite part of the semilocal trace after subtracting the generic regular
orbit. The published trace theorem identifies it with the Tate local terms
and therefore with \(N(f\star\widetilde g)\). This realizes the required
number through the full adelic Schwartz/Fourier channel rather than the
finite valuative channel already closed by no-go. It is not yet an
intersection form on DC Picard classes: global nonprincipal descent,
principal invariance, and RR axioms remain open.

107_240 closes that scalar Picard descent branch. The Frobenius pullback law
is incompatible with every nonzero compactly supported scalar section; even
degree normalization forces \(\mathbb Q_+^\times\)-invariance and hence zero.
Finite-PL transitions cannot cancel the diffuse curvature. The surviving
object is an equivariant correspondence representation with a numerical
trace pairing, not a rank-one divisor class in the domain of classical
arithmetic Hodge.

107_241 closes every finite-rank exact-target branch at once. The polarized
Weil convolution form has infinite rank because its Fourier--Laplace support
contains the infinitely many critical zeros, while a finite-rank convolution
distribution has only finite exponential spectrum. The two balance moments
remove at most two dimensions, so the quotient by the exact Weil radical is
still infinite-dimensional. Any faithful realization must therefore retain
an infinite-dimensional Green, distributional, or cohomological component;
Neron--Severi or any other finitely generated additive shadow cannot suffice.
