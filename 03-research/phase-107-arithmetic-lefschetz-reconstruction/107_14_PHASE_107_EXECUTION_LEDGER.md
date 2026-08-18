# 107.14 -- Phase 107 execution ledger and falsifier audit

## 1. Purpose

This note executes the program-management requirements of Part V in
`107_00`.  Its role is not to add new geometry, but to record the
current execution state of Phase 107 in a form that can be audited
against the actual deliverables, stop tests, and mandatory falsifiers.

The operative distinction is:

\[
 \text{formal target stated}
 \neq
 \text{target proved}
 \neq
 \text{phase complete}.
 \tag{1.1}
\]

This ledger therefore separates:

1. what has already been written and checked in the workspace;
2. what is presently specified only as a theorem target or blueprint;
3. what remains unbuilt.

## 2. Status vocabulary

Every item below is assigned one of four statuses.

### `proved`

The requirement is explicitly derived in a Phase 107 document or exact
verifier already present in the workspace.

### `formalized`

The requirement has been turned into a precise theorem target,
construction blueprint, or audit statement, but no proof or realization
has yet been completed.

### `partial`

Some supporting components exist, but the requirement itself is not yet
closed even at theorem level or depends on missing comparisons.

### `open`

No completed construction or proof in the current Phase 107 tree yet
establishes the requirement.

## 3. Paper-by-paper ledger

### Paper 0 — Function-field calibration

Status: `proved`

Evidence:

1. `107_01_PAPER_0_FUNCTION_FIELD_CALIBRATION_SPEC.md` fixes the control
   curve \(E/\mathbb F_5\) and the required chain.
2. `107_02_PAPER_0_FUNCTION_FIELD_CALIBRATION.md` proves the
   Frobenius--Lefschetz--Hodge calibration on that fixed control.
3. `107_01_function_field_preflight.py` provides an exact arithmetic
   verifier.
4. `107_28_PAPER_0_GENUS_2_DIAGONAL_SENSITIVITY_AUDIT.md` and
   `107_28_genus2_diagonal_sensitivity.py` add an auxiliary exact
   genus-2 falsifier audit for the primitive diagonal entries, now with
   both one supersingular equality-case control and one ordinary
   non-extremal control.
5. `107_29_PAPER_0_RECALIBRATION_AFTER_GENUS_AUDIT.md` recalibrates the
   scope of Paper 0 after that auxiliary audit.
6. `107_30_PAPER_0_GENUS_UNIFORM_PRIMITIVE_INTERSECTION_FORM.md` proves
   the genus-uniform primitive intersection formulas at the source
   \(C\times C\) level.
7. `107_31_PAPER_0_GENUS_UNIFORM_SOURCE_CHAIN.md` extends the source
   generalization to composition, Lefschetz trace, Euler extraction, and
   balancing on \(C\times C\).
8. `107_32_PAPER_0_GENUS_FREE_SOURCE_CALIBRATION.md` integrates those
   source-uniform pieces into one genus-free calibration statement.

Closed obligations from `107_00` §21:

1. rulings and Frobenius graphs inside \(E\times E\);
2. degrees, transpose, composition, diagonal intersections;
3. closed-point Euler expansion via connected projection;
4. balanced factor \(q^{-nd/2}\);
5. primitive intersection matrix;
6. Hodge-sign derivation of the Weil bound.

Residual note:
Paper 0 does not address the proper-global finite-support mechanism over
\(\mathrm{Spec}\,\mathbb Z\), by design.
The original elliptic preflight is also genus-1 specific; the new
genus-2 audit isolates diagonal genus sensitivity, but `107_02` itself
has not yet been rewritten as a genus-uniform source-construction
theorem.
Paper 0 should therefore be read as `proved` for the fixed elliptic
control; the primitive Gram package is now proved genus-uniformly at the
classical source-intersection level, and the rest of the source chain is
now also proved genus-uniformly on \(C\times C\).  What remains open is
a single editorial replacement of the fixed-curve exposition of
`107_02`, not the genus dependence of the underlying classical
operations.  What remains delicate is that `107_30` derives the genus
factor by classical adjunction on \(C\times C\), not yet by the full
arithmetic Phase 107 route over \(\mathrm{Spec}\,\mathbf Z\).

### Paper A — Local arithmetic intersection lines

Status: `partial`

Evidence:

1. `107_03` gives the free arithmetic divisor module.
2. `107_04` gives finite-place determinant lines.
3. `107_05` gives the Gamma--polar Green metric.
4. `107_06` synthesizes these as the finite-support intersection
   theorem.
5. `107_34_PAPER_A_PRIME_POWER_SUPPORT_AUDIT.md` and
   `107_34_paper_a_prime_power_support_preflight.py` provide an exact
   arithmetic audit for the prime-power resultant support law and the
   diagonal resultant vanishing of `107_04`.
6. `107_35_PAPER_A_CONNECTED_EXTRACTION_AUDIT.md` and
    `107_35_paper_a_connected_extraction_preflight.py` provide an exact
    audit for the Eulerian primitive extractor of `107_03` and its
    function-field specialization to the fixed Paper 0 control.
7. `107_64_PAPER_A_DIAGONAL_COHERENCE_AUDIT.md` and
    `107_64_paper_a_diagonal_coherence_audit.py` provide an exact audit
    for the finite diagonal-coherence shadow of `107_05`: matched-cutoff
    stabilization, one common Green functional for cross and diagonal
    pairings, exact polarization, and failure of diagonal-only shifts.
8. `107_70_PAPER_A_AUDIT_COVERAGE_MATRIX.md` records explicitly which
    parts of `107_03`--`107_06` are now exact-audited shadows and which
    remain theorem-level or only partially exact-audited.
9. `107_75_PAPER_A_UNIFIED_SYNTHESIS_AUDIT.md` and
    `107_75_paper_a_unified_synthesis_audit.py` provide an exact audit
    of one finite unified shadow of `107_06`: connected extraction
    kills decomposable Euler mass before pairing, only visible
    prime-power support survives in the finite sector, the same Green
    functional governs cross and diagonal pairings, and diagonal-only
    shifts remain exactly detectable.
10. `107_117` through `107_120` pin a real local discrimination ladder:
    coarse valuative packets fail, a split-sensitive packet succeeds on
    the fixed atlas, and the visible \(S_3\) threshold can be expressed
    in Frobenius language through \(a_p^\flat\).
11. `107_121_CURRENT_107_04_TO_A4_FROBENIUS_NO_GO.md` and
    `107_121_current_107_04_to_a4_frobenius_no_go.py` exact-check that
    the current finite observable of `107_04`, namely \(\log p\), does
    not recover the Frobenius coefficient needed by that successful
    atlas-level packet.
12. `107_122_CURRENT_107_03_107_04_SOURCE_PACKET_TO_A4_NO_GO.md` and
    `107_122_current_107_03_107_04_source_packet_to_a4_no_go.py`
    strengthen that obstruction from the scalar \(\log p\) to the full
    current finite source packet
    \(\bigl(p,(1,p),p^{-1/2},\log p\bigr)\).
13. `107_123_ADDITIVE_VALUATIVE_EULER_CP_NO_GO.md` and
    `107_123_additive_valuative_euler_cp_no_go.py` exact-check on the
    real pair `20a1@2` / `36a4@2` that once \(c_p\) is retained in the
    target, standard additive valuative/Euler data are structurally
    insufficient.
14. `107_124_CURRENT_TARGET_NON_EULERIAN_SOURCE_NECESSITY_GATE.md` and
    `107_124_current_target_non_eulerian_source_necessity_gate.py`
    convert that pair into a governance gate: any future faithful local
    source upgrade for the current target must add a non-Eulerian,
    Galois-sensitive channel.
15. `107_125_CURRENT_PHASE107_FINITE_SOURCE_ROW_CP_NO_GO.md` and
    `107_125_current_phase107_finite_source_row_cp_no_go.py` restate the
    same real obstruction in the exact language of the present finite
    source row of `107_03`--`107_04`, namely
    \((Z_{p,1},(1,p),p^{-1/2},\log p)\).
16. `107_126_TARGET_BIFURCATION_GATE_CP_VS_KODAIRA.md` and
    `107_126_target_bifurcation_gate_cp_vs_kodaira.py` exact-check the
    design fork on the same real forcing pair:
    keeping \(c_p\) in the target gives `NO` for the present finite
    source row, while reducing the target to Kodaira type alone gives
    `YES` on that pair.
17. `107_127_CURRENT_SOURCE_RULE_LOCAL_CP_NO_GO.md` and
    `107_127_current_source_rule_local_cp_no_go.py` lift the same
    forcing pair one level higher: the finite local source-rule
    vocabulary allowed already in `107_00`, namely
    \((\Lambda(p^k),\log p,p^{-k/2},a_p,L_p^{\mathrm{loc}})\), is
    exact-checked as too coarse for the current target when \(c_p\) is
    retained.
18. `107_128_LOCAL_MINIMAL_MODEL_RESIDUE_CHANNEL_WITNESS.md` and
    `107_128_local_minimal_model_residue_channel_witness.py` provide a
    first positive local witness on the same forcing pair: the residue
    class of the local minimal-model Weierstrass coefficients already
    separates `20a1@2` from `36a4@2`, so the current obstruction is
    specific to the present source vocabulary rather than to all local
    arithmetic data.
19. `107_130_IVSTAR_MOD8_RESIDUE_CP_NO_GO.md` and
    `107_130_ivstar_mod8_residue_cp_no_go.py` close the next local
    ambiguity on real data: inside the scanned \(IV^\ast\) additive
    family at \(p=2\), the mod-8 minimal-model residue channel persists
    across many curves but still does not determine \(c_p\) by itself.
20. `107_131_IVSTAR_RESIDUE_THRESHOLD_GATE.md` and
    `107_131_ivstar_residue_threshold_gate.py` add a quantitative local
    threshold on the same scanned \(IV^\ast\) family: residues modulo
    \(2,4,8,16\) still mix \(c_p\), while modulus \(32\) is the first
    tested residue depth at which the family stops mixing \(c_p\).
21. `107_132_FIXED_ATLAS_TARGET_CP_NO_GO.md` and
    `107_132_fixed_atlas_target_cp_no_go.py` close the current local
    fork in the tranche-required format: on a fixed atlas of five real
    curves, including one supersingular elliptic control and one
    genus-\(2\) control, the current source-rule packet still collapses
    `20a1@2` / `36a4@2` while the current target distinguishes them by
    \(c_p\), so the exact binary verdict is `NO`.
22. `107_133_CURRENT_ROW_C_CLOSURE_GATE.md` and
    `107_133_current_row_c_closure_gate.py` promote that fixed-atlas
    failure to an explicit phase-state decision for the current local
    route: with the current target still retaining \(c_p\), the same
    tranche-compliant atlas now returns
    `ROW_C_STATUS: CLOSED_BY_NO_GO`.
23. `107_134_S3_ATTEMPT_A5_LOCAL_MOD32_RESIDUE_GATE.md` and
    `107_134_s3_attempt_a5_local_mod32_residue_gate.py` test a
    genuinely different local grammar on a fixed real atlas: the packet
    \((p,v(c_4),v(c_6),v(\Delta),v(j),\mathrm{ainv}_{\min}\bmod 32)\)
    separates every visible elliptic target state on that atlas and
    therefore returns `VERDICT: YES`.
24. `107_135_IVSTAR_MOD32_RANGE_EXTENSION_GATE.md` and
    `107_135_ivstar_mod32_range_extension_gate.py` extend the additive
    robustness scan behind that candidate grammar: in the \(IV^\ast\)
    family at \(p=2\) with common coarse packet
    \((2,4,6,8,4,IV^\ast,2,0,1)\), the mod-\(32\) residue channel still
    has no mixed \(c_p\)-classes through conductor \(2000\), across
    `ROWS: 285`, and so returns `VERDICT: YES`.
25. `107_136_MOD32_NON_DERIVABILITY_FROM_CURRENT_SOURCE_RULE.md` and
    `107_136_mod32_non_derivability_from_current_source_rule.py`
    establish the missing grammar-level restriction behind `A5`: on the
    same enlarged \(IV^\ast\) family with `ROWS: 285`, the current
    `107.00` finite source-rule packet is constant, while the mod-\(32\)
    channel splits into `MOD32_CLASSES: 24` with `MIXED_MOD32_CLASSES: 0`,
    so derivability from the present grammar returns `VERDICT: NO`.
26. `107_137_A5_BRANCH_ADMISSION_GATE.md` and
    `107_137_a5_branch_admission_gate.py` compress the whole local
    decision chain into one operational gate: with `ROW_C_CLOSED: True`,
    `A5_ATLAS_COLLISIONS: 0`, `FAMILY_ROWS: 285`,
    `FAMILY_MIXED_MOD32_CLASSES: 0`, and
    `NON_DERIVABLE_FROM_CURRENT_RULE: True`, the verifier returns
    `OPEN_A5_BRANCH: YES`.
27. `107_138_PAPER_A_LOCAL_BRANCH_FORMALIZATION.md` and
    `107_138_paper_a_branch_formalization_gate.py` lift that
    operational gate into the planning layer of Paper A itself: with
    `LEGACY_ROW_C_STATUS: CLOSED`, `A5_ATLAS_STATUS: LIVE`,
    `A5_FAMILY_STATUS: LIVE`, and `A5_NOT_CURRENT_RULE: True`, the
    verifier returns `PAPER_A_LOCAL_BRANCH_STATE: BIFURCATED`.
28. `107_139_PAPER_A_A5_SOURCE_EXTENSION_CANDIDATE.md` and
    `107_139_paper_a_a5_source_extension_candidate.py` provide the
    first positive source-side candidate attached to that live branch:
    the extension
    \(\mathcal S_{A5}=(\mathcal S_{\mathrm{legacy}},\rho_{32})\).
    On the fixed atlas it has `ATLAS_COLLISIONS: 0`; on the enlarged
    additive family it has `FAMILY_MIXED_EXTENSION_CLASSES: 0`; and it
    genuinely refines the legacy packet with
    `LEGACY_CLASSES_REFINED_BY_RHO32: 1`, so the verifier returns
    `VERDICT: YES`.
29. `107_140_PAPER_A_A5_REFINED_LOCAL_LINE_CANDIDATE.md` and
    `107_140_paper_a_a5_refined_local_line_candidate.py` move the A5
    branch from packet level to first local-object level: refined local
    generators and line labels carry \(\rho_{32}\) while still
    forgetting to the same legacy support class.  On real data the
    verifier finds `ATLAS_COLLISIONS: 0`,
    `LEGACY_CLASSES_SPLIT_BY_RHO32: 1`, and
    `SAMPLE_LINE_SUPPORT_OK: True`, so it returns `VERDICT: YES`.
30. `107_141_PAPER_A_A5_DECORATED_DETERMINANT_LINE_CANDIDATE.md` and
    `107_141_paper_a_a5_decorated_determinant_line_candidate.py` push
    the same branch into the first determinantal refinement language:
    the candidate
    \(\mathcal D_{A5}=(\mathcal D_{\mathrm{legacy}},\rho_{32})\)
    preserves the legacy scalar projection on the enlarged \(IV^\ast\)
    family while refining it into multiple decorated classes.  The
    verifier reports `ATLAS_COLLISIONS: 0`,
    `MIXED_DECORATED_CLASSES: 0`,
    `REFINED_SCALAR_CLASSES: 1`, and
    `SCALAR_PROJECTION_CONSTANT_ON_IVSTAR: True`, so it returns
    `VERDICT: YES`.
31. `107_142_PAPER_A_A5_RHO32_TORSOR_CANDIDATE.md` and
    `107_142_paper_a_a5_rho32_torsor_candidate.py` add the first
    algebraic compatibility law on that same branch: the difference
    cocycle \(\delta_{32}(row_1,row_2)\).  On real data the verifier
    reports `TRANSPOSE_OK: True`, `COCYCLE_OK: True`,
    `ZERO_KERNEL_OK: True`, `CP_PAIR_DELTA_NONZERO: True`, and
    `SPLIT_PAIR_DELTA_NONZERO: True`, so it returns `VERDICT: YES`.
32. `107_143_PAPER_A_A5_LOCAL_TRANSPORT_COMPOSITION_GATE.md` and
    `107_143_paper_a_a5_local_transport_composition_gate.py` add the
    first local transport/composition law on top of that cocycle:
    sampled real arrows satisfy `TRANSPORT_OK: True` and
    `INVERSE_OK: True`, while remaining nontrivial on both the `c_p`
    forcing pair and the split/nonsplit pair, so the verifier returns
    `VERDICT: YES`.
33. `107_144_LOCAL_NERON_COMPONENT_NO_GO.md` and
    `107_144_local_neron_component_no_go.py` supersede the A5 branch
    state and strengthen the legacy no-go.  On the real forcing pair,
    the exact affine-\(E_6\) component calculation gives correction
    magnitude \(4\log(2)/3\) for a rational nonidentity component of
    `20a1`, while `36a4` has trivial rational component group over
    \(\mathbf Q_2\).  Over the fixed unramified quadratic extension,
    explicit order-three sections recover the two nonidentity
    components of `36a4`, isolating Galois descent as the missing data.
    Integral admissible changes also prove that \(\rho_{32}\) changes
    on each fixed curve.  The verifier returns
    `TARGET_COMPONENT_DATA_NECESSARY: YES`, `RHO32_DESCENDS: NO`,
    `LEGACY_ROW_C: CLOSED_NO_GO`,
    `A5_STATUS: REJECTED_NONINVARIANT`, and `VERDICT: YES`.

Closed claims:

1. connected/disconnected return separation;
2. transpose before connected extraction;
3. prime-power-only local support;
4. diagonal and cross-terms from one metrized determinant theory;
5. finite-support symmetric intersection package.

Residual note:
`107_06` closes Milestone I at theorem level, but Paper A is now best
read as `partial`: several load-bearing layers of `107_03`--`107_05`
have exact finite shadows, while the full analytic archimedean metric
theorem and the theorem-level synthesis of `107_06` still lack an audit
layer comparable to Paper 0.
The finite local support law of `107_04` is now exact-audited by
`107_34`, and the new `107_75` verifier now exact-audits one finite
unified Milestone I synthesis shadow tying that support law to
connected extraction and common Green closure.  What still lacks that
stronger audit layer is the full analytic metric theorem and the
target-side realization.
The connected-extraction layer of `107_03` is now also exact-audited by
`107_35`.  The new `107_64` verifier exact-audits a finite
diagonal-coherence shadow of `107_05`, but it does not prove the full
analytic Green metric theorem or the target-side realization.
The new `107_75` verifier exact-audits one finite unified synthesis
shadow of `107_06`, tying together connected extraction, prime-power
finite support, and common Green closure in one exact model.  It still
does not prove the full analytic metric theorem or a target-side
realization over a proved arithmetic surface.
The new `107_121` and `107_122` gates now make one further limitation
exact: the successful atlas-level Frobenius packet of `107_120` is not
derivable from the current finite source observables of `107_03`--`107_04`.
And `107_123` through `107_125` sharpen that limitation under the
current target design: because the present target retains \(c_p\), the
real additive pair `20a1@2` / `36a4@2` already blocks the current
finite Paper A row itself.  So Paper A remains `partial` not only
because the global realization is unbuilt, but because the present
finite local source row is now exact-checked as insufficient for the
current target unless a genuinely Galois-sensitive new source channel is
added.  The new `107_126` gate makes the fork explicit in one binary
test on that same pair: under the current target with \(c_p\), the
present row fails; under a reduced Kodaira-only target, that particular
local obstruction disappears.  So the next substantive Phase 107 design
decision is no longer hidden: either keep \(c_p\) and search for a new
Galois-sensitive source channel, or weaken the local target.  The new
`107_127` gate sharpens this once more: under the present source rule of
`107_00`, even the finite local rule-level vocabulary itself is already
blocked on the real forcing pair if \(c_p\) remains in the target.  So
the unresolved choice is now explicit at the phase-design level rather
than only at the Paper A implementation level.  The new `107_128`
witness adds the first concrete positive direction for that search:
finer local arithmetic data, already visible through the residue class
of the local minimal model at \(p=2\), do separate the forcing pair.
So the present obstruction should now be read as a limitation of the
current source grammar, not as evidence that no local arithmetic channel
can distinguish the pair.  The new `107_130` gate then sharpens that
positive direction into a new boundary: even this finer mod-8 residue
channel is still insufficient by itself to recover \(c_p\) on the real
\(IV^\ast\) family.  So the local search space is now bracketed from
both sides: the present source grammar is too coarse, but the first
visible finer arithmetic channel is not yet fine enough.  The new
`107_131` gate turns that into a concrete quantitative boundary on the
same real family: in the scanned data, the first tested residue depth
at which mixed \(c_p\)-classes disappear is modulus \(32\).  This does
not prove that mod \(32\) is the correct missing Phase 107 channel, but
it does replace an open-ended request for “finer local information” by
an exact lower-bound phenomenon visible on real arithmetic data.  The
new `107_132` gate then packages the whole obstruction in the exact
format required by the next tranche: one fixed atlas with at least five
real curves, one supersingular elliptic control, one genus-\(2\)
control, and one binary verdict.  That verdict is `NO` for the current
target retaining \(c_p\).  So the local no-go is no longer just a
forcing-pair observation or a family scan; it is now recorded as a
tranche-compliant fixed-atlas failure of the current finite local source
rule.  The new `107_133` gate then closes the remaining governance gap:
for the current workspace target, that failure is now elevated to an
explicit route status, namely `ROW_C_STATUS: CLOSED_BY_NO_GO`.  So row
\((c)\) is no longer merely “awaiting refinement” under the current
target; it is closed in its present form unless a genuinely new source
grammar is introduced.  The new `107_134` gate provides the first exact
fixed-atlas evidence for such a different grammar: adding local
minimal-model residue modulo \(32\) to the valuative packet survives the
same visible \(S_3\) atlas with `VERDICT: YES`.  This does not prove
that the mod-\(32\) route is derivable from the Phase 107 source rule,
but it does show that the local search has moved from pure obstruction
to one explicit surviving candidate grammar.  The new `107_135` gate
then upgrades that from atlas-level survival to a family-level
robustness statement on the additive side: the decisive mod-\(32\)
subchannel remains free of mixed \(c_p\)-classes on `ROWS: 285` real
\(IV^\ast\) curves through conductor \(2000\).  So the current state is
no longer “closed row and one small surviving toy”; it is “closed
current row, plus one concrete alternate grammar whose additive
subchannel now survives both a fixed atlas and a substantially enlarged
real family.”  The new `107_136` gate then removes the last ambiguity
about how to read that survival: the mod-\(32\) channel is not merely a
clever repackaging of the current prime/Gamma/pole source rule, because
on the same `ROWS: 285` family the present rule-level packet is
constant while the mod-\(32\) channel is not.

This next block is historical only: it records the temporary state of
the workspace before `107_144` falsified `A5`.  At that stage, the row
\((c)\) obstruction had already closed the legacy packet, while the
mod-\(32\) branch still looked like a surviving alternate grammar.  The
new `107_137` gate then turned that diagnosis into an explicit
operational state: `OPEN_A5_BRANCH: YES`.  The new `107_138` gate wrote
the same fact at the planning level rather than only the gate level:
Paper A local work was formally bifurcated into one closed branch and
one live branch.  The new `107_139` note then supplied the first
positive source object on that historical live branch: not yet a
derivation from the original `107.00` rule, but an explicit extension
candidate
\(\mathcal S_{A5}=(\mathcal S_{\mathrm{legacy}},\rho_{32})\) that passes
the current atlas and family tests.
The new `107_140` note pushes the same branch one level deeper into the
Paper A local geometry: the residue symbol now appears directly on
refined local generators and line labels, while still forgetting to the
legacy support class of `107_04`.
The new `107_141` note then adds the first decorated determinant-line
candidate on top of that geometry: the old scalar projection survives
unchanged, while the \(\rho_{32}\) decoration splits the blind
\(IV^\ast\) class on real data.  So the A5 branch now has a first
candidate not only at packet level and object level, but also at the
determinantal-decoration level.
The new `107_142` note adds the first explicit compatibility law on top
of that decorated level: \(\rho_{32}\) now comes with a tested
difference cocycle satisfying transpose symmetry and a first cocycle
identity on real data.  So the A5 branch has advanced from a separating
decoration to a first algebraically structured decoration.  The new
`107_143` gate then adds the first transport/composition reading of the
same structure: the A5 differences now behave like local arrows that
compose additively and invert under reversal on the tested real data.

The A5 claims in `107_134`--`107_143` are now historical
candidate-level evidence, not a live branch.  `107_144` supplies the
missing coordinate-change falsifier: integral admissible
transformations preserve the real curve and local minimal discriminant
but change \(\rho_{32}\).  Therefore the packet, decorated line, and
difference-arrow packaging do not descend to the curve; the cocycle and
transport identities were formal identities on chosen coordinates.
A5 is rejected.  The same artifact proves that component descent
affects an actual degree-zero local vertical correction, so the legacy
row is closed for the full Neron/Arakelov local target rather than only
for a target table that listed \(c_p\).

### Paper B — Decorated absolute Frobenius category

Status: `partial`

Evidence:

1. `107_07` fixes the decorated correspondence category.
2. `107_08` fixes the suspension to the arithmetic flow.
3. `107_09` fixes the arithmetic Lefschetz formula from fixed points.
4. `107_36_PAPER_B_FUNCTION_FIELD_RETURN_LEFSCHETZ_AUDIT.md` and
   `107_36_paper_b_return_lefschetz_preflight.py` provide an exact audit
   of the same-tower function-field return/composition/Lefschetz shadow
   on the fixed control \(E/\mathbf F_5\).
5. `107_37_PAPER_B_AUDIT_COVERAGE_MATRIX.md` records explicitly which
   subclaims of Part II are now exact-audited and which remain only
   theorem-level formalized.
6. `107_38_PAPER_B_COMMON_PHASE_GLUING_AUDIT.md` and
   `107_38_paper_b_common_phase_gluing_preflight.py` provide an exact
   combinatorial audit for the load-bearing common-phase gluing shadow
   of `107_08`.
7. `107_39_PAPER_B_MIXED_TOWER_REFINEMENT_AUDIT.md` and
   `107_39_paper_b_mixed_tower_refinement_preflight.py` provide an
   exact combinatorial audit for the non-collapse of mixed-tower
   composition into primitive returns.
8. `107_40_PAPER_B_DAVENPORT_HEILBRONN_EXTERNAL_WITNESS.md` and
   `107_40_davenport_heilbronn_external_witness.py` provide an exact
   external arithmetic witness that the Davenport--Heilbronn control is
   non-Eulerian already at the coefficient stage.
9. `107_41_PAPER_B_JOINT_GAMMA_POLAR_FACTOR_AUDIT.md` and
   `107_41_joint_gamma_polar_factor_consistency.py` provide a
   high-precision consistency audit for the explicit coupled
   Gamma--pole factor used by `107_05` and `107_09`.
10. `107_65_PAPER_B_NO_PRESCRIBED_TRACE_AUDIT.md` and
    `107_65_paper_b_no_prescribed_trace_audit.py` provide an exact
    audit of the finite no-prescribed-trace shadow behind `107_09`:
    diagonal renormalization cleans only the identity channel, the
    visible boundary page produces Gamma and pole jointly, and the
    renormalized visible trace has trivial kernel relative to the source
    generators.
11. `107_76_PAPER_B_JOINT_FIXED_POINT_ASSEMBLY_AUDIT.md` and
    `107_76_paper_b_joint_fixed_point_assembly_audit.py` provide an
    exact audit of one finite joint shadow behind `107_09`: same-tower
    returns produce only prime data, the common boundary page produces
    Gamma and pole jointly, diagonal renormalization removes only the
    identity channel, and mixed-tower refinements remain visible
    without collapsing into the primitive prime page.
12. `107_88_PAPER_B_ASSEMBLED_NO_PRESCRIBED_TRACE_AUDIT.md` and
    `107_88_paper_b_assembled_no_prescribed_trace_audit.py` provide an
    exact audit of one assembled no-prescribed-trace shadow behind
    `107_09`: the renormalized visible fixed-point page remains
    source-determined as one package, and external retouching breaks the
    current Paper B assembly immediately.

Closed claims:

1. derived-fiber-product composition;
2. transpose, degree, connected cyclic trace;
3. suspension to prime orbits of length \(\log p\);
4. no definitional installation of the explicit formula;
5. joint prime--Gamma--polar fixed-point output;
6. Davenport--Heilbronn failure at the Euler/correspondence stage.

Residual note:
`107_09` closes Milestone II at theorem level, but Paper B is now best
read as `partial`: several load-bearing layers of `107_07`--`107_09`
have exact shadows, while the full suspended-geometry/fixed-point
theorem is still not independently audited to the standard of Paper 0.
The comparison with the classical
explicit formula is formalized in `107_09`, while the spectral zero-side
comparison remains an after-the-fact identification rather than a
construction input.  The same-tower function-field shadow is now
exact-audited by `107_36`, but the mixed-tower refinement, common-phase
suspension, and joint prime--Gamma--polar fixed-point package are not
yet audited to that same standard; `107_37` records that boundary
explicitly.  `107_38` now exact-audits the finite combinatorial shadow
of the common-phase gluing, but not the full suspension geometry.
`107_39` now exact-audits the finite mixed-tower non-collapse shadow,
but not the full derived-fiber-product geometry of the mixed refinement
squares.  `107_40` now exact-audits the external Davenport--Heilbronn
falsifier at the arithmetic coefficient/Euler-product stage.  `107_41`
now exact-audits the explicit coupled Gamma--pole factor, but not yet
the full one-step joint prime--Gamma--polar fixed-point production.
`107_65` now exact-audits the visible no-prescribed-trace shadow of
`107_09`, but not the full suspended-flow fixed-point theorem.
The new `107_76` verifier exact-audits one finite joint fixed-point
assembly shadow of `107_09`, tying together prime returns, boundary
jointness, mixed-tower separation, and identity cleanup in one
renormalized source model.  It still does not prove the full suspended
flow geometry or the real one-step fixed-point theorem.
The new `107_88` verifier exact-audits one further assembled visible
shadow of `107_09`: the full renormalized prime--Gamma--pole--mixed
page remains source-determined and rejects external retouching as an
exact failure.  It still does not prove the full suspended flow
geometry or the real one-step fixed-point theorem.

### Paper C — Surface and Jacobian realization

Status: `partial`

Evidence:

1. `107_10` fixes the finite proper-model target \(\mathcal X_T\).
2. `107_11` fixes the Picard/Jacobian realization target and exact
   radical audit.
3. `107_15` gives a first concrete candidate model
   \(\mathcal X_T^{(1)}\) and first candidate realized generators.
4. `107_16` gives a first compactification candidate
   \(\overline{\mathfrak S}\), its corner \(C_\infty\), and the boundary
   metric line \(\mathcal L_\infty\).
5. `107_17` gives a first local chart atlas for
   \(\overline{\mathfrak P}_{\rm fr}\) and a chartwise finite-type
   criterion for \(\overline{\Gamma}_n^{\rm fr}\).
6. `107_18` replaces the abstract framing coordinate by finite visible
   rooted/cyclotomic packets \((n,\chi)\) at fixed support level \(T\).
7. `107_19` fixes packet charts, packet graph loci, and packet-to-
   cyclotomic comparison morphisms toward the determinant-line package.
8. `107_20` constructs the local packet determinant line and proves its
   off-diagonal norm comparison with the determinant package of
   `107_04`.
9. `107_21` descends those local packet lines to a global order-indexed
   line object on the candidate model \(\mathcal X_T^{(1)}\).
10. `107_22` packages that descended line object into a candidate
    integrable adelic metrized realization for finite-support divisors.
11. `107_23` gives a chartwise logarithmic integrability criterion for
    that candidate metric and partially closes the finiteness audit.
12. `107_24` fixes the candidate polarization and reduces the degree-zero
    audit to finitely many visible intersection calculations.
13. `107_25` derives the first polarization intersection identities and
   localizes the denominator \(H_T^{(1)}\cdot H_T^{(1)}\) to the corner
   contribution plus explicit exceptional corrections.
14. `107_26` localizes those exceptional corrections to a finite class of
   polarization-active centers and gives a corner-preserving
   regularization criterion.
15. `107_27` enumerates the currently visible polarization-active local
   centers in the chart atlas and proves them corner-preserving.
16. `107_42_PAPER_C_LOCAL_PACKET_UNIT_FACTOR_AUDIT.md` and
    `107_42_paper_c_packet_unit_factor_preflight.py` provide an exact
    audit of the finite local packet algebra of `107_20`: rooted labels
    contribute only norm-one unit factors off the diagonal and do not
    change the diagonal vanishing/excess-intersection stop.
17. `107_43_PAPER_C_AUDIT_COVERAGE_MATRIX.md` records explicitly which
    Part III claims now have exact local audits and which remain only
    theorem-level or blueprint-level.
18. `107_44_PAPER_C_PACKET_DESCENT_COCYCLE_AUDIT.md` and
    `107_44_paper_c_packet_descent_cocycle_preflight.py` provide an
    exact audit of the finite rooted descent shadow behind `107_21`:
    connected packet descent groupoids for fixed order pairs, cocycle
    compatibility on rooted transitions, route-independent descended
    section, and compatibility with the visible finite action.
19. `107_72_PAPER_C_GLOBAL_LINE_OBJECT_GLUE_AUDIT.md` and
    `107_72_paper_c_global_line_object_glue_audit.py` provide an exact
    audit of the next finite `107_21` shadow: the visible descent
    cocycle defines a representative-independent quotient line object,
    preserves the order-only norm, and is stable under visible gauge
    re-trivialization.
20. `107_45_PAPER_C_LOGARITHMIC_CHART_AUDIT.md` and
    `107_45_paper_c_logarithmic_chart_audit.py` provide an exact audit
    of the finite logarithmic chart shadow behind `107_23`: stability of
    the admissible local form under the chart transitions of `107_17`,
    tensor additivity of boundary/diagonal coefficients, and exclusion
    of stronger-than-log singular support in the normal-crossings model.
21. `107_74_PAPER_C_INTEGRABILITY_PROFILE_INTRINSICITY_AUDIT.md` and
    `107_74_paper_c_integrability_profile_intrinsicity_audit.py`
    provide an exact audit of the next finite `107_23` shadow: the
    visible chart/root presentations determine one intrinsic
    normal-crossings profile on the divisor slots
    \((B_{\rm v}, B_{\rm h}, \Delta)\), with one order-only remainder
    class and no hidden fourth singular direction.
22. `107_46_PAPER_C_PRIMITIVE_DEGREE_ZERO_AUDIT.md` and
    `107_46_paper_c_primitive_degree_zero_audit.py` provide an exact
    audit of the finite primitive degree-zero shadow behind `107_24`:
    uniqueness of the linear primitive correction once \(h_T\neq0\),
    exact denominator bookkeeping, and correction-channel compatibility
    with the currently visible corner-preserving center types.
23. `107_47_PAPER_C_CORRECTION_SUM_AUDIT.md` and
    `107_47_paper_c_correction_sum_audit.py` provide an exact audit of
    the finite quantitative shadow behind `107_25`--`107_27`: additive
    aggregation of the correction package over the finite center list,
    boundary-only invisibility of the corner term, and the fact that
    cancellation of \(-2c_T\) is a genuinely signed numerical equality
    rather than a structural consequence of the center types.
24. `107_48_PAPER_C_EXACT_KERNEL_SHADOW_AUDIT.md` and
    `107_48_paper_c_exact_kernel_shadow_audit.py` provide an exact audit
    of the finite equality-case shadow behind `107_11`: radical modes
    may map to torsion and then vanish after realification, while
    non-radical witnesses survive and the real kernel is checked as an
    exact equality rather than a mere inclusion.
25. `107_49_PAPER_C_PAIRING_TRANSPORT_SHADOW_AUDIT.md` and
    `107_49_paper_c_pairing_transport_shadow_audit.py` provide an exact
    audit of the finite bilinear shadow behind the pairing-transport
    target of `107_11` and the comparison logic of `107_13`: generator
    comparison, bilinear extension, primitive self-pairing compatibility,
    and radical compatibility are checked exactly in one finite model.
26. `107_78_PAPER_C_REALIZATION_DEGREE_ZERO_COVARIANCE_AUDIT.md` and
    `107_78_paper_c_realization_degree_zero_covariance_audit.py`
    provide an exact audit of one further `107_11` shadow: primitive
    correction lands the visible realization in exact target-side degree
    zero, finite critical scaling preserves that status, and the same
    visible classes remain compatible with pairing transport and the
    explicit radical.
27. `107_51_PAPER_D_A6_FUNCTORIALITY_SHADOW_AUDIT.md` and
    `107_51_paper_d_a6_functoriality_shadow_audit.py` provide an exact
    audit of the finite A6 shadow behind `107_12`: additivity,
    transpose, discrete scaling covariance, and one visible
    pullback/pairing compatibility pattern are checked exactly in one
    functoriality model.
28. `107_52_PAPER_D_A5_FINITENESS_SHADOW_AUDIT.md` and
    `107_52_paper_d_a5_finiteness_shadow_audit.py` provide an exact
    audit of the finite A5 shadow behind `107_12`: off-diagonal and
    mixed visible pairings are finite, the remaining unresolved sector
    is isolated explicitly to the completed diagonal excess-intersection
    package, and no hidden off-diagonal or boundary divergence is
    needed.
29. `107_53_PAPER_D_A1_REGULAR_PROPERNESS_BOUNDARY_AUDIT.md` records
    explicitly that `107_10`, `107_15`, `107_16`, and `107_17` give
    structural support and exclusion of bad envelopes for A1, but do
    not yet prove a regular proper model or an exact adelic comparison
    theorem.
30. `107_54_PAPER_D_A4_LOG_EFFECTIVITY_SHADOW_AUDIT.md` and
    `107_54_paper_d_a4_log_effectivity_shadow_audit.py` provide an
    exact audit of the finite A4 shadow behind `107_12`: the visible
    polarization-active blow-ups of `107_27` preserve the nonnegative
    local logarithmic support cone of the candidate polarization.
31. `107_55_PAPER_D_A2_REMAINDER_COHERENCE_AUDIT.md` and
    `107_55_paper_d_a2_remainder_coherence_audit.py` provide an exact
    audit of the finite A2 shadow behind `107_12`: on the visible
    packet/chart cover, the regular remainder channel is order-only,
    route-independent, and compatible with the single Gamma--polar
    receiver of `107_22`.
32. `107_80_PAPER_D_A5_TARGET_PAIRING_ASSEMBLY_AUDIT.md` and
    `107_80_paper_d_a5_target_pairing_assembly_audit.py` provide an
    exact audit of one finite A5 target-side shadow: the transported
    pairing stays finite on every visible non-diagonal channel, and the
    explicit unresolved placeholder remains confined to the genuine
    diagonal square.
33. `107_81_PAPER_D_A2_A4_METRIC_CHANNEL_DISCIPLINE_AUDIT.md` and
    `107_81_paper_d_a2_a4_metric_channel_discipline_audit.py` provide
    an exact audit of one joint A2/A4 target-side shadow: the visible
    normal-crossings profile, the single remainder channel, and the
    nonnegative local support package coexist in one finite model
    without creating extra singular or remainder channels.
34. `107_83_PAPER_D_ROUTE_A_ASSEMBLED_APPLICABILITY_AUDIT.md` and
    `107_83_paper_d_route_a_assembled_applicability_audit.py` provide
    an exact audit of one assembled Route A shadow: the candidate
    envelope, degree-zero realization, metric discipline, target-pairing
    finiteness, and visible functoriality coexist in one finite target
    state, while removing any one A1--A6 ingredient makes the assembled
    applicability shadow fail immediately.
35. `107_56_PAPER_D_TERMINAL_IDENTITY_PRIMITIVE_QUOTIENT_AUDIT.md` and
    `107_56_paper_d_terminal_identity_primitive_quotient_audit.py`
    provide an exact audit of the finite `107_13` shadow: after
    primitive projection and quotient by the explicit radical, the
    source and target quadratic forms still match exactly with the
    required sign and equality case.
36. `107_57_PAPER_C_CANDIDATE_REALIZATION_PACKAGING_AUDIT.md` and
    `107_57_paper_c_candidate_realization_packaging_audit.py` provide
    an exact audit of the finite `107_22` shadow: the candidate
    realization package is additive, uses one archimedean receiver
    channel, ignores rooted refinements at the package level, and
    remains compatible with primitive correction.
37. `107_73_PAPER_C_ADELIC_CLASS_INTRINSICITY_AUDIT.md` and
    `107_73_paper_c_adelic_class_intrinsicity_audit.py` provide an
    exact audit of the next finite `107_22` shadow: visible chart/root
    presentations determine one intrinsic adelic-class quotient shadow,
    preserve one total archimedean receiver channel, and reject extra
    receiver splitting.
38. `107_58_PAPER_C_PACKET_CYCLOTOMIC_BRIDGE_AUDIT.md` and
    `107_58_paper_c_packet_cyclotomic_bridge_audit.py` provide an
    exact audit of the finite `107_19` shadow: rooted packet labels do
    not alter the order-only support law or off-diagonal norm, the
    bridge is transpose invariant, and the diagonal remains in
    excess-intersection territory.
39. `107_59_PAPER_C_VISIBLE_FRAMING_COORDINATE_AUDIT.md` and
    `107_59_paper_c_visible_framing_coordinate_audit.py` provide an
    exact audit of the finite `107_18` shadow: the visible rooted
    framing coordinate factors through finite order-dividing character
    packets, the action \(\mu_m\) is genuinely finite combinatorial
    data, and graph closures reduce to finitely many packet equations.
40. `107_60_PAPER_C_LOCAL_ATLAS_FINITE_TYPE_AUDIT.md` and
    `107_60_paper_c_local_atlas_finite_type_audit.py` provide an exact
    audit of the finite `107_17` shadow: the visible chart transitions,
    diagonal equations, graph equations, chartwise finite-type
    criterion, and local corner generator are symbolically consistent.
41. `107_61_PAPER_C_COMPACTIFIED_SQUARE_CORNER_AUDIT.md` and
    `107_61_paper_c_compactified_square_corner_audit.py` provide an
    exact audit of the finite `107_16` shadow: the common corner is a
    real shared receiver for boundary, diagonal, graph, and boundary-
    metric data in the visible model.
42. `107_62_PAPER_C_CANDIDATE_MODEL_INCIDENCE_AUDIT.md` and
    `107_62_paper_c_candidate_model_incidence_audit.py` provide an
    exact audit of the finite `107_15` shadow: the visible incidence
    locus contains the diagonal, both rulings, and the graph
    generators without collapsing the required candidate-model
    structure.
43. `107_79_PAPER_C_CANDIDATE_ENVELOPE_COHERENCE_AUDIT.md` and
    `107_79_paper_c_candidate_envelope_coherence_audit.py` provide an
    exact audit of one joint `107_15`--`107_17` shadow: the visible
    incidence locus, compactified boundary receiver, and local atlas fit
    one coherent candidate envelope with one finite regularization-
    center list and without collapsing the two-ruling/corner structure.
44. `107_82_PAPER_C_CANDIDATE_TARGET_ASSEMBLY_AUDIT.md` and
    `107_82_paper_c_candidate_target_assembly_audit.py` provide an
    exact audit of one assembled candidate-target shadow: the visible
    candidate envelope, the intrinsic receiver channel, the degree-zero
    realization logic, and the single-profile metric package coexist on
    one common cover without forcing extra target-side channels.
45. `107_63_PAPER_C_UNIVERSAL_MODEL_EXCLUSION_AUDIT.md` and
    `107_63_paper_c_universal_model_exclusion_audit.py` provide an
    exact audit of the finite `107_10` exclusion shadow: base
    truncation loses prime channels, genus-zero envelopes lose the
    degree-one carrier, ruling collapse destroys the visible
    diagonal/transpose package, and absolutely continuous completions
    erase the point/resonance classes needed later in Part III.
46. `107_86_PAPER_C_FINITE_SUPPORT_REALIZATION_ASSEMBLY_AUDIT.md` and
    `107_86_paper_c_finite_support_realization_assembly_audit.py`
    provide an exact audit of one assembled `107_10` shadow: full-base
    support, degree-one carrier, two-ruling/discrete realization data,
    coherent candidate envelope, and assembled target-side packaging
    coexist in one finite realization state, while the standard bad
    substitutions fail immediately.
47. `107_87_PAPER_C_POINT_SPECTRUM_RETENTION_AUDIT.md` and
    `107_87_paper_c_point_spectrum_retention_audit.py` provide an exact
    audit of one finite `107_11` retention shadow: visible
    point/resonance classes survive inside one intrinsic single-
    receiver package after quotient by the explicit radical shadow,
    while continuous completion or channel collapse erases them.
48. `107_89_PAPER_C_TARGET_SIDE_DIVISOR_SENSITIVITY_AUDIT.md` and
    `107_89_paper_c_target_side_divisor_sensitivity_audit.py` provide
    an exact audit of one finite `107_11` sensitivity shadow: genuinely
    moved divisors remain distinguishable as target-side classes inside
    the intrinsic package after primitive correction and radical
    quotienting, while scalarized or location-blind substitutes fail.
49. `107_90_PAPER_C_ASSEMBLED_ARCHIMEDEAN_LOAD_BEARING_AUDIT.md` and
    `107_90_paper_c_assembled_archimedean_load_bearing_audit.py`
    provide an exact audit of one assembled load-bearing shadow:
    intrinsic single-receiver packaging, finite-support realization,
    and point-spectrum retention remain finitely faithful only while the
    Green side keeps enough independent separating channels.
50. `107_93_REAL_ELLIPTIC_BAD_FIBER_INTERSECTION_WITNESS.md` and
    `107_93_real_elliptic_bad_fiber_intersection_witness.py` provide a
    real arithmetic local witness on actual elliptic curves over
    \(\mathbf Q\): selected bad fibers from LMFDB realize the expected
    affine-Dynkin component-intersection matrices, and the finite-place
    Arakelov weight appears as the standard target-side factor
    \(\log p\).
51. `107_94_REAL_KODAIRA_TYPE_LOG_WEIGHT_COMPARISON.md` and
    `107_94_real_kodaira_type_log_weight_comparison.py` provide a
    second real local witness: for the same real Kodaira fiber type
    \(I_2\) appearing at different bad primes, the unweighted
    intersection geometry stays fixed while the target-side local object
    changes only by the scalar factor \(\log p\).
52. `107_95_SOURCE_TARGET_LOCAL_COMPARISON_BOUNDARY_WITNESS.md` and
    `107_95_source_target_local_comparison_boundary_witness.py` provide
    a first real source-vs-target local comparison boundary: the current
    Paper A local row reproduces the scalar weight \(\log p\), but does
    not yet distinguish different real Kodaira fiber geometries at the
    same prime.
53. `107_96_REAL_COMPONENT_GROUP_BOUNDARY_WITNESS.md` and
    `107_96_real_component_group_boundary_witness.py` provide a second
    real local arithmetic boundary: the affine-Dynkin intersection
    matrix of a bad fiber does not by itself exhaust the local target
    datum, since real Tamagawa behavior can diverge from the raw
    component geometry.
54. `107_97_SOURCE_VS_FULL_LOCAL_TARGET_BOUNDARY_WITNESS.md` and
    `107_97_source_vs_full_local_target_boundary_witness.py` package the
    local comparison chain explicitly: the current source-side row of
    `107_04` sits below real local fiber geometry, which itself still
    sits below the full local arithmetic datum visible on actual bad
    fibers.
55. `107_98_REAL_SPLIT_NON_SPLIT_BOUNDARY_WITNESS.md` and
    `107_98_real_split_non_split_boundary_witness.py` provide an even
    finer real local boundary: two actual fibers can share the same
    prime, the same Kodaira type, the same affine matrix, and the same
    Tamagawa number, yet still differ by split versus nonsplit
    multiplicative reduction.
56. `107_99_REAL_LOCAL_INFORMATION_HIERARCHY_WITNESS.md` and
    `107_99_real_local_information_hierarchy_witness.py` package the
    real local boundary layers into one exact hierarchy: source scalar
    weight, affine fiber geometry, intermediate \(c_p\)-data, and the
    finer split/nonsplit reduction label.
57. `107_100_REAL_COMPONENT_GROUP_FROBENIUS_WITNESS.md` and
    `107_100_real_component_group_frobenius_witness.py` identify one
    exact arithmetic mechanism on real multiplicative fibers: the
    geometric component group is \(\mathbf Z/n\mathbf Z\) for \(I_n\),
    and the recorded Tamagawa number \(c_p\) is recovered as the size
    of the Frobenius-fixed subgroup, so the missing local refinement is
    arithmetic action on component data rather than another scalar
    normalization.
58. `107_101_REAL_ADDITIVE_IV_FROBENIUS_WITNESS.md` and
    `107_101_real_additive_iv_frobenius_witness.py` extend that exact
    mechanism to a real additive pair of type \(IV\): the affine
    \(A_2\) triangle has geometric component group of order \(3\), and
    the real Tamagawa numbers \(1\) and \(3\) are recovered as sizes of
    Frobenius-fixed subgroups under a 3-cycle action and the trivial
    action, respectively.
59. `107_102_REAL_ADDITIVE_III_RIGIDITY_WITNESS.md` and
    `107_102_real_additive_iii_rigidity_witness.py` record the
    complementary rigid additive sector \(III\): the affine \(A_1\)
    geometry gives geometric component group \(\mathbf Z/2\mathbf Z\),
    and the pinned real examples realize the forced value \(c_p=2\).
60. `107_103_REAL_LOCAL_RIGIDITY_FLEXIBILITY_ATLAS.md` and
    `107_103_real_local_rigidity_flexibility_atlas.py` synthesize the
    current real local picture into one exact atlas: \(I_9\) is already
    flexible at the \(c_p\)-level, \(I_2\) is rigid in \(c_p\) but not
    in the finer split/nonsplit datum, \(IV\) is flexible at the
    \(c_p\)-level, and the pinned \(III\) sector is rigid at both
    visible levels.
61. `107_104_SOURCE_LOCAL_DISCRIMINATION_ATLAS.md` and
    `107_104_source_local_discrimination_atlas.py` compare that full
    real local atlas directly with the present Paper A finite-place row:
    on the pinned real examples, the source distinguishes only the
    prime via \(\log p\), while multiple distinct local target states
    collapse to one source class at fixed prime.
62. `107_105_MINIMAL_SOURCE_REFINEMENT_LADDER.md` and
    `107_105_minimal_source_refinement_ladder.py` organize the next
    exact lower bounds on any future local source upgrade: adding only
    Kodaira geometry yields five classes, adding \(c_p\) yields six,
    and adding the finer reduction label yields seven on the pinned real
    atlas.
63. `107_106_SOURCE_REFINEMENT_RESIDUAL_AMBIGUITY_MATRIX.md` and
    `107_106_source_refinement_residual_ambiguity_matrix.py` make those
    source refinements fully explicit at the collision level: the
    remaining \(S_1\) ambiguity is exactly the \(IV\) pair, the
    remaining \(S_2\) ambiguity is exactly the split/nonsplit `I_2`
    pair, and \(S_3\) resolves all pinned local collisions.
64. `107_107_LOCAL_SOURCE_UPGRADE_NECESSITY_GATE.md` and
    `107_107_local_source_upgrade_necessity_gate.py` convert that
    refinement ladder into a governance gate for future Paper A claims:
    seeing local geometry requires at least \(S_1\)-level separation,
    seeing \(c_p\) requires at least \(S_2\), and seeing the finer
    visible local datum requires at least \(S_3\).
65. `107_108_S0_FACTOR_LOCAL_REALIZATION_NO_GO.md` and
    `107_108_s0_factor_local_realization_no_go.py` strengthen that
    governance into a local no-go statement: any comparison or
    realization still factoring through the present `107_04` signature
    \(S_0=\log p\) must collapse several distinct pinned real local
    target states and therefore cannot be faithful on that atlas.
66. `107_109_SOURCE_FACTOR_REALIZATION_NO_GO_LADDER.md` and
    `107_109_source_factor_realization_no_go_ladder.py` extend that
    obstruction to the next two minimal source refinements: any local
    comparison factoring through \(S_1\) still collapses the \(IV\) and
    `I2` ambiguity pairs, any comparison factoring through \(S_2\)
    still collapses the split/nonsplit `I2` pair, and only \(S_3\)
    resolves all visible collisions of the pinned real atlas.
67. `107_110_SAME_BAD_PRIME_PROFILE_GLOBAL_NO_GO.md` and
    `107_110_same_bad_prime_profile_global_no_go.py` lift that local
    obstruction to a first finite global no-go: the actual curves
    `14.a1` and `14.a5` have the same conductor \(14\) and hence the
    same bad-prime profile \(\{2,7\}\), yet already differ in their
    pinned real local target signature at \(p=2\).
68. `107_111_SAME_FINITE_LOG_WEIGHT_PACKET_GLOBAL_NO_GO.md` and
    `107_111_same_finite_log_weight_packet_global_no_go.py` restate the
    same obstruction in the exact finite-place language of `107_04`:
    the actual curves `14.a1` and `14.a5` share the same full packet
    of finite bad-prime weights \(\{\log 2,\log 7\}\), yet already
    differ in their pinned real local target signature at \(p=2\).
69. `107_112_GLOBAL_SOURCE_UPGRADE_NECESSITY_GATE.md` and
    `107_112_global_source_upgrade_necessity_gate.py` turn those finite
    global no-go statements into a governance test: any future finite
    global source upgrade claiming pinned local target recovery must
    distinguish the actual pair `14.a1/14.a5` by information strictly
    finer than both the support profile \(\{2,7\}\) and the present
    finite log-weight packet \(\{\log 2,\log 7\}\).
70. `107_113_CURRENT_FINITE_SOURCE_INSUFFICIENCY_GATE.md` and
    `107_113_current_finite_source_insufficiency_gate.py` package the
    whole current boundary into one exact statement: the present finite
    source layers \(S_0,S_1,S_2\) remain locally insufficient on the
    pinned atlas, and the coarse finite global packets \(G_0,G_1\)
    remain globally insufficient on the actual pair `14.a1/14.a5`.
71. `107_114_PAPER_A_FINITE_BOUNDARY_AUDIT.md` and
    `107_114_paper_a_finite_boundary_audit.py` convert those positive
    and negative finite facts into one Milestone I boundary statement:
    the current Paper A finite package is exact-audited as a symbolic
    pairing shadow, but it is still excluded from faithful target-side
    local/global recovery by the active insufficiency gates.
72. `107_115_PAPER_B_FINITE_BOUNDARY_AUDIT.md` and
    `107_115_paper_b_finite_boundary_audit.py` do the analogous job for
    Milestone II: the current Paper B finite package is exact-audited
    as a symbolic source/fixed-point shadow, but it is still excluded
    from the full suspended geometric fixed-point theorem and any
    target-side realization.
73. `107_116_SOURCE_SIDE_FINITE_BOUNDARY_AUDIT.md` and
    `107_116_source_side_finite_boundary_audit.py` synthesize those two
    milestone-level boundaries into one source-side statement: the
    current finite source package across Papers A and B is exact-audited
    as a symbolic source complex, but it is still excluded from
    geometric realization on both sides simultaneously.
74. `107_145_CLASSICAL_ABEL_JACOBI_TARGET_CONTROL.md` and
    `107_145_classical_abel_jacobi_target_control.py` add one genuine
    III-B target-side control on actual Jacobian objects.  On five
    elliptic curves over \(\mathbf Q\), the verifier checks that
    torsion classes are exactly the visible real-kernel classes and
    that the canonical-height Gram matrix is positive definite on the
    sampled free quotient.  On the fixed Paper 0 control
    \(E/\mathbf F_5: y^2=x^3+x+1\) and on the genus-\(2\) control
    \(C/\mathbf F_5: y^2=x^5+x+1\), explicit point-minus-infinity
    classes are nontrivial in the classical Jacobian targets.  The
    verifier returns `DIVISOR_TO_PICARD_FAITHFUL_MOD_TORSION: YES`,
    `PAPER0_JACOBIAN_CONTROL: YES`,
    `GENUS2_JACOBIAN_SEPARATION: YES`, and `VERDICT: YES`.
75. `107_147_TRACE_NORM_SQUARE_NO_GO.md` and
    `107_147_trace_norm_square_no_go.py` close the genuine Euclidean
    projective-tensor mass candidate for the square.  Primitive
    rank-one integer matrices on the nuclear boundary are mandatory
    generators.  For \(n_k\) a product of \(k\) distinct primes
    congruent to \(1\pmod4\), the exact Gaussian-integer count gives
    \(d_*(n_k)\ge2^{k+1}\), hence superlogarithmic growth in \(n_k\)
    and failure of linear Riemann--Roch growth in \(\deg D\).  The
    verifier also proves the exact small values \(d_*(1)=4\) and
    \(d_*(2)=12\), and returns `TRACE_NORM_BRANCH: CLOSED_NO_GO` and
    `VERDICT: YES`.
76. `107_148_CC_JACOBIAN_SIGNED_DIVISOR_NO_GO.md` and
    `107_148_cc_jacobian_signed_divisor_no_go.py` reject the published
    Connes--Consani Picard/Jacobian monoid as the additive target of
    `107_11`.  Its prime class \(H_p=\mathbb Z[1/p]\) is idempotent and
    noninvertible, whereas \(\mathrm{Div}_{\mathrm{EF}}\) is a
    signed abelian group.  Group completion kills every idempotent
    \(H_p\).  The verifier returns
    `SIGNED_SOURCE_ADDITIVE_MAP_EXISTS: NO`,
    `CC_JACOBIAN_AS_III_B_TARGET: REJECTED`, and `VERDICT: YES`.
77. `107_149_DIMENSIONAL_HODGE_CORRECTION.md` and
    `107_149_dimensional_hodge_correction.py` correct a dimensional
    type error in the direct square route.  A model of Weil's square
    has generic dimension two and total Krull dimension three over
    \(\mathbb Z\), so Yuan--Zhang requires the primitive condition
    \(M_f\cdot H_T=0\) and the polarized intersection
    \(\overline M_f^{\,2}\cdot\overline H_T\).  The former unpolarized
    terminal formula is valid only on a separately constructed curve
    route.  The verifier returns
    `POLARIZATION_FACTOR_REQUIRED: YES`,
    `UNPOLARIZED_TERMINAL_IDENTITY_VALID: NO`, and `VERDICT: YES`.
78. `107_150_CC_PROJECTIVE_TENSOR_MASS.md` and
    `107_150_cc_projective_tensor_mass.py` fix the square mass
    inherited from Connes--Consani's published \(\ell^1\) construction.
    The projective tensor norm of two \(\ell^1\) factors is exactly
    entrywise \(\ell^1\), not the trace norm.  Consequently the linear
    growth theorem of `107_146` applies to this tensor branch,
    while `107_147` remains a no-go only for Euclidean factors.
    The verifier returns
    `CC_L1_PROJECTIVE_TENSOR_IS_ENTRYWISE_L1: YES`,
    `DIMENSION_GROWTH_IN_DEGREE: LINEAR`, and `VERDICT: YES`.
79. `107_151_MIDDLE_TOLERANCE_COHOMOLOGY.md` and
    `107_151_middle_tolerance_cohomology.py` construct middle
    cohomology for a bounded three-term complex as a tolerant
    \(\mathbb S[\pm1]\)-module.  The construction is functorial,
    invariant under isomorphisms of bounded complexes, retains genuinely
    nontransitive bounded images, and recovers
    \(\ker d_1/\mathrm{im}\,d_0\) when the image is a subgroup.
    The verifier returns `NONTRANSITIVE_IMAGE_HANDLED: YES`,
    `SUBGROUP_CASE_RECOVERS_QUOTIENT: YES`, and `VERDICT: YES`.
80. `107_152_NAIVE_STALK_LINEARIZATION_NO_GO.md` and
    `107_152_naive_stalk_linearization_no_go.py` reject the
    direct ordinary linearization of the 2026 absolute stalks.  The
    monoid rings \(\mathbb Z[T^{\mathbb Z[1/p]_+}]\) and their square
    have infinitely many independent monomial rays, so their positive
    mass balls have infinite integer dimension.  The verifier returns
    `NAIVE_Z_LINEARIZATION_RR_FINITE: NO` and `VERDICT: YES`.
81. `107_153_FROBENIUS_STABLE_LINEARIZATION_NO_GO.md` and
    `107_153_frobenius_stable_linearization_no_go.py` strengthen
    that obstruction: every nonconstant additive subgroup stable under
    the invertible local Frobenius has infinite rank, because a bilateral
    Frobenius orbit is linearly independent in a Laurent-polynomial
    summand.  Thus no nonconstant, Frobenius-stable, finite-dimensional
    bounded submodule exists in the ordinary additive lift.  The verifier
    returns `ADDITIVE_STALK_TRUNCATION_ROUTE: CLOSED_NO_GO` and
    `VERDICT: YES`.
82. `107_154_PRO_FINITE_FROBENIUS_STALK.md` and
    `107_154_pro_finite_frobenius_stalk.py` construct the
    surviving finite-level alternative.  Exponents are cut by their
    unique coordinates \(c p^j\); every level has finite CC dimension,
    Frobenius and its inverse map isometrically to the next level, the
    two square rulings commute, and the filtered colimit recovers the
    full 2026 stalk.  The verifier returns
    `FROBENIUS_BETWEEN_LEVELS: YES`,
    `TWO_RULINGS_COMMUTE: YES`,
    `FULL_STALK_RECOVERED_AS_FILTERED_COLIMIT: YES`, and
    `VERDICT: YES`.
83. `107_155_DIVISOR_SUPPORT_STABILIZATION_CRITERION.md` and
    `107_155_divisor_support_stabilization_criterion.py` prove
    the exact \(H^0\) stabilization criterion for the pro-system:
    finite-level CC dimensions stabilize if and only if the union of
    divisor-admitted monomial rays is finite.  Frobenius covariance is
    compatible with this condition across different divisors, not as
    invariance of one level.  The verifier returns
    `FINITE_SUPPORT_STABILIZES: YES`,
    `INFINITE_SUPPORT_STABILIZES: NO`, and `VERDICT: YES`.
84. `107_156_ZARISKI_SUPPORT_VS_FROBENIUS_DEPTH.md` and
    `107_156_zariski_support_vs_frobenius_depth.py` combine the
    published pullback-sheaf theorem with an exact local obstruction.
    Zariski sections are nonzero at only finitely many primes, but at one
    prime the bounded sequence \(p^{-k}\) cannot be generated by any
    finite signed family.  Thus finite prime support is already
    geometric, while finite Frobenius depth is the additional theorem
    still required from each divisor.  The verifier returns
    `FINITE_PRIME_SUPPORT_IMPLIES_FINITE_DIMENSION: NO`,
    `REQUIRED_EXTRA_CUTOFF: FROBENIUS_DEPTH`, and `VERDICT: YES`.
85. `107_157_VISIBLE_ORDER_PARTIAL_MONOID_CORRECTION.md` and
    `107_157_visible_order_partial_monoid_correction.py` correct
    the finite chart algebra in `107_15` and `107_18`.
    The visible orders are the divisors of
    \(L_T=\prod p^{\lfloor T/\log p\rfloor}\), a finite gcd/lcm lattice,
    not a multiplicative monoid.  Multiplication is partial at fixed
    level and otherwise maps to a larger level, exactly as required by
    `107_154`.  The verifier returns
    `MULTIPLICATIVE_MONOID_AT_FIXED_LEVEL: NO`,
    `MULTIPLICATION_STRUCTURE: PARTIAL`, `DIVISORS_ENUMERATED: NO`, and
    `VERDICT: YES`.  Since \(\log L_T\sim e^T\), all computations use
    the exponent vector and never enumerate the divisor lattice.
86. `107_158_ROOTED_SECTOR_STABILIZATION.md` and
    `107_158_rooted_sector_stabilization.py` record the immediate
    corollary that closes the local
    support problem for the rooted/cyclotomic sector.  The visible dual
    is exactly
    \(X_T^\vee=(1/L_T)\mathbb Z/\mathbb Z\), cyclic of order \(L_T\);
    its \(p\)-depth is \(K_p(T)=\lfloor T/\log p\rfloor\).  Hence the
    rooted \(H^0\) support is finite before dimension and satisfies the
    stabilization criterion of `107_155`.  The verifier returns
    `ROOTED_DUAL_EQUALS_1_OVER_L: YES`,
    `ROOTED_H0_SUPPORT_STABILIZES: YES`, and `VERDICT: YES`.
87. `107_159_GLOBAL_ROOTED_DESCENT.md` and
    `107_159_global_rooted_descent.py` close the discrete global
    descent of those rooted sectors.  The inclusions for \(L_T\mid
    L_{T'}\), their dual frame projections, and the Chinese-remainder
    decomposition glue all prime-primary sectors canonically.  Their
    colimit is \(\mathbb Q/\mathbb Z\) and the frame limit is
    \(\widehat{\mathbb Z}\).  The verifier returns
    `CANONICAL_LEVEL_TRANSITIONS: YES`,
    `CRT_PRIME_GLUE: YES`,
    `ROOTED_COLIMIT_RECOVERS_Q_OVER_Z: YES`, and `VERDICT: YES`.
88. `107_160_CYCLOTOMIC_CHART_REPRESENTABILITY.md` and
    `107_160_cyclotomic_chart_representability.py` represent the
    discrete rooted coordinate by the finite flat proper regular scheme
    \(\mathcal R_T=\coprod_{n\mid L_T}\mathrm{Spec}
    \mathbb Z[\zeta_n]\).  They also correct packet labels to
    \(\mathrm{ord}(\chi)=n\), eliminating duplicate lower-order
    characters from the primitive chart \(V(\Phi_n)\).  The verifier
    returns `CYCLOTOMIC_FACTORIZATION_EXACT: YES`,
    `GENERIC_DEGREE_EQUALS_ROOTED_ORDER: YES`, and `VERDICT: YES`.
89. `107_161_CROSS_PRIME_RESTRICTION_NO_GO.md` and
    `107_161_cross_prime_restriction_no_go.py` test the restriction
    mechanism of the published CC pullback sheaf itself.  The generic
    stalk is zero, distinct prime values extend independently, and
    restrictions delete prime coordinates.  Thus prime-chart
    restrictions cannot carry nonzero cross-prime coupling; an
    additional global adelic/archimedean morphism is required.  The
    verifier reads the published TeX source, uses the fixed real prime
    atlas \(2,3,5,7,11\), rejects a nonzero-generic negative control,
    and returns `NONZERO_CROSS_PRIME_RESTRICTION: NO`,
    `ADDITIONAL_GLOBAL_GLUE_REQUIRED: YES`, and `VERDICT: YES`.
90. `107_162_NAIVE_ABEL_JACOBI_SQUARE_NO_GO.md` and
    `107_162_naive_abel_jacobi_square_no_go.py` reject the topological
    Abel--Jacobi fiber product equipped only with the inverse-image
    sheaf from the base.  Base-pulled zero loci are fiber-saturated and
    cannot cut the diagonal or Frobenius graphs in the torus
    \(C_p\times C_p\).  Relative-coordinate controls do cut both.  The
    verifier returns `BASE_PULLBACK_CUTS_DIAGONAL: NO`,
    `REQUIRED_EXTENSION: RELATIVE_ORBIT_SHEAF`, and `VERDICT: YES`.
91. `107_163_LINEAR_FROBENIUS_CONGRUENCE_LIFT.md` and
    `107_163_linear_frobenius_congruence_lift.py` lift the published CC
    rational correspondence into monoid algebras by
    \(X^aY^b\mapsto T^{na+mb}\).  The exact stalk kernel is generated by
    \(X^{m/p^k}-Y^{n/p^k}\), \(k\ge0\); at finite depth \(R\), the
    deepest root is a single exact generator.  The verifier checks 100
    real-prime/depth/ratio instances and rejects the omission of that
    root, returning `SHALLOW_ROOT_SUFFICES_AT_NEXT_LEVEL: NO`,
    `DIRECTED_KERNEL_COLIMIT_REQUIRED: YES`, and `VERDICT: YES`.
92. `107_164_ADDITIVE_NEWTON_REDUCTION_NO_GO.md` and
    `107_164_additive_newton_reduction_no_go.py` prove that this abelian
    lift cannot descend through reduced Newton polygons.  Any additive
    map from an idempotent monoid to an abelian group is zero; explicitly,
    adding a midpoint between incomparable exponents preserves the upper
    Newton polygon and forces that midpoint basis vector to vanish.  The
    verifier checks all 289 lattice points in \([-8,8]^2\), returning
    `LINEAR_SUPPORT_LIFT_DESCENDS_TO_REDUCED_NEWTON_SQUARE: NO`,
    `REQUIRED_COHOMOLOGY_SOURCE: ENRICHED_UNREDUCED_SUPPORT`, and
    `VERDICT: YES`.
93. `107_165_UNIVERSAL_SUPPORT_ENRICHMENT.md` and
    `107_165_universal_support_enrichment.py` construct the initial
    coefficient-sensitive refinement \(\mathbb N[M]\) of the
    idempotent square and its group completion \(\mathbb Z[M]\).
    Positive tropicalization is a Frobenius-equivariant semiring map;
    signed cancellation is deliberately non-additive.  The verifier
    checks 117 exact identities and returns
    `TWO_FROBENIUS_RULINGS_EQUIVARIANT: YES`,
    `SIGNED_CANCELLATION_CHANGES_NEWTON_SHADOW: YES`, and
    `VERDICT: YES`.
94. `107_166_MONOID_TOPOS_COHOMOLOGICAL_DIMENSION_NO_GO.md` and
    `107_166_monoid_topos_cohomological_dimension_no_go.py` prove that
    raw derived invariants of the monoid-action square do not have
    surface amplitude.  For \(r\) visible primes, the constant module
    has \(\mathrm{Ext}^k\cong\bigwedge^k\mathbb Z^{2r}\), nonzero
    through degree \(2r\).  On the actual \(T=2,3,4,5\) atlases the
    verifier returns `COHOMOLOGY_ABOVE_DEGREE_TWO: YES`,
    `RAW_MONOID_TOPOS_HAS_SURFACE_AMPLITUDE: NO`, and `VERDICT: YES`.
95. `107_167_PERIODIC_FOLIATED_SQUARE_AMPLITUDE.md` and
    `107_167_periodic_foliated_square_amplitude.py` use the published
    de Rham equivalence \(\Gamma(p)\simeq_{\rm dR}S^1\) and Kunneth to
    prove periodic-product Betti numbers \((1,2,1)\).  Exact cellular
    matrices for five real prime pairs return
    `PERIODIC_PRODUCT_BETTI_NUMBERS: 1,2,1`,
    `COHOMOLOGY_ABOVE_DEGREE_TWO: NO`, and `VERDICT: YES`.
96. `107_168_FOURIER_LIFT_AND_MASS_OBSTRUCTION.md` and
    `107_168_fourier_lift_and_mass_obstruction.py` embed the integral
    support lift into the published Fourier algebra
    \(\mathbb C[\mathbb Q]\), intertwining Frobenius and all rational
    correspondence maps.  They also prove that the leafwise operator
    \(X(e_q)=2\pi i yq e_q\) has no uniform bound for the CC \(\ell^1\)
    mass.  Across 4,757 exact compatibility checks, the verifier returns
    `RATIONAL_CORRESPONDENCE_INTERTWINED: YES`,
    `UNIFORM_L1_BOUND_FOR_LEAFWISE_X: NO`, and `VERDICT: YES`.
97. `107_169_ROOTED_CELLULAR_SQUARE_COMPLEX.md` and
    `107_169_rooted_cellular_square_complex.py` construct an integral
    torus complex over \(R_L\) with uniform mass bounds and symbolic
    subdivision maps for \(L\mid L'\).  Exact matrices and transition
    identities return `HOMOLOGY_STABILIZES: YES`,
    `DIFFERENTIAL_L1_BOUND_D2: 4`, and `VERDICT: YES`.
98. `107_170_CELLULAR_CUP_PRODUCT_INTERSECTION_NO_GO.md` and
    `107_170_cellular_cup_product_intersection_no_go.py` prove that this
    additive model cannot supply divisor intersections: \(H^4=0\), so
    all degree-two cup products vanish, while direct counting on the
    fixed Paper-0 curve gives \(\Gamma_1\cdot\Delta=N_1=9\).  The
    verifier returns `CELLULAR_CUP_PRODUCT_RECOVERS_INTERSECTION: NO`,
    `REQUIRED_INTERSECTION_SOURCE: RELATIVE_TRACE_OR_COMPLEX_SURFACE_TOP_CLASS`,
    and `VERDICT: YES`.
99. `107_171_CM_COMPLEX_LIFT_OF_PAPER_0.md` and
    `107_171_cm_complex_lift_of_paper_0.py` realize the complete Paper-0
    intersection chain on the genuine complex abelian surface
    \(E_{\rm CM}\times E_{\rm CM}\).  The fixed curve over
    \(\mathbb F_5\) is the reduction of the rational CM model with
    \(j=-32768\), and the graphs of
    \(\alpha=(-3+\sqrt{-11})/2\) satisfy
    \(\Gamma_{\alpha^n}\cdot\Delta=N(\alpha^n-1)=N_n\).
    The verifier independently checks the reduction, CM polynomial,
    point counts, centered intersections, and Hodge determinants through
    \(n=16\), returning `PAPER_0_COMPLEX_LIFT: PROVED_FOR_FIXED_CONTROL`
    and `VERDICT: YES`.  This entry does not promote any universal
    arithmetic-surface claim.
100. `107_172_GOOD_OPEN_ARITHMETIC_CM_LIFT.md` and
    `107_172_good_open_arithmetic_cm_lift.py` connect the Paper-0
    finite-field and complex constructions inside one proper smooth
    arithmetic family over
    \(\mathrm{Spec}\,\mathcal O_K[1/11]\).  Scheme-theoretically,
    \(\Gamma_{\alpha^n}\cap\Delta=\ker(\alpha^n-1)\), finite flat of
    rank \(N_n\).  The verifier fixes the prime \((\alpha)\) over 5,
    checks the real curve and number-field data, and returns
    `FINITE_FLAT_KERNEL_RANKS_MATCH_NN: YES`, `FULL_SPEC_Z_MODEL: NO`,
    and `VERDICT: YES`.
101. `107_173_EVERYWHERE_GOOD_CM_ARITHMETIC_SURFACE.md` and
    `107_173_everywhere_good_cm_arithmetic_surface.py` remove the sole
    bad place after the explicit extension
    \(L=\mathbb Q(\alpha,w)\), \(w^2=2\alpha+3\).  The integral CM model
    has discriminant 1 and conductor \((1)\), so its self-product is
    proper and smooth over all of \(\mathrm{Spec}\,\mathcal O_L\).
    Exact Sage checks return `EVERYWHERE_GOOD_REDUCTION: YES`,
    `ALL_GRAPH_KERNEL_DEGREES_MATCH: YES`, `BASE_IS_SPEC_Z: NO`, and
    `VERDICT: YES`.  This is a fixed-control construction, not a row-(a)
    promotion for \(\mathrm{Spec}\,\mathbb Z\).
102. `107_174_CM_FROBENIUS_GRAPH_DESCENT_NO_GO.md` and
    `107_174_cm_frobenius_graph_descent_no_go.py` close the direct
    descent of the CM calibration.  Galois exchanges
    \(\Gamma_\alpha\) and \(\Gamma_{\bar\alpha}\); their mutual
    intersection is 11, so the oriented graph is not invariant.  The
    orbit average doubles every \(N_n\), and division by two restores
    the scalar but introduces mixed graphs under composition.  Exact
    checks return `ORIENTED_CM_GRAPH_DESCENDS_TO_Q: NO`,
    `GALOIS_AVERAGING_PRESERVES_COMPOSITION: NO`, and `VERDICT: YES`.
    This closes only CM graph descent, not the idele-translation channel.
103. `107_175_UNIVERSAL_LINKING_SELECTOR_NO_GO.md` and
    `107_175_universal_linking_selector_no_go.py` test the 2026 rooted
    arithmetic-linking channel on the real 20a1/36a4 pair.  The universal
    Artin datum at 2 contains quadratic characters with both signs, but
    it is the same source object for both curves, whose geometric
    \(\mathbb Z/3\mathbb Z\) component groups require opposite
    Frobenius actions.  The verifier returns
    `UNIVERSAL_LINKING_HAS_BOTH_SIGNS: YES`,
    `TARGET_INDEPENDENT_SELECTOR_REALIZES_BOTH: NO`,
    `ROOTED_LINKING_REOPENS_S3: NO`, and `VERDICT: YES`.  A canonical
    source-derived quotient character remains missing.
104. `107_176_GROUP_TRANSLATION_INTERSECTION_NO_GO.md` and
    `107_176_group_translation_intersection_no_go.py` prove that an
    ordinary smooth group cannot geometrize the local idele-translation
    trace.  A nonidentity translation has empty graph--diagonal
    equalizer and the identity equalizer is positive-dimensional.  The
    verifier enumerates all translations on four real elliptic groups
    and one genus-2 Jacobian, returning
    `LOCAL_TERM_INTERSECTION_MISMATCH: YES`,
    `SMOOTH_GROUP_TRANSLATION_ROUTE: CLOSED_NO_GO`, and `VERDICT: YES`.
    The surviving mechanism is monoid-boundary fixed strata with
    transverse scaling.
105. `107_177_TRANSVERSE_SCALING_ORDINARY_INTERSECTION_NO_GO.md` and
    `107_177_transverse_scaling_ordinary_intersection_no_go.py` compare
    the actual local graph \(x\mapsto ux\) with the published
    distributional factor.  Across 20 exact pairs
    \((p,u=1+p^k)\), generic intersection length is always 1, while the
    required weights are \(p^k\); the integral special fibre has
    dimension-one excess.  The verifier returns
    `ORDINARY_INTERSECTION_RECOVERS_LOCAL_FACTOR: NO`,
    `REQUIRED_REFINEMENT: EQUIVARIANT_DERIVED_EXCESS_CLASS`, and
    `VERDICT: YES`.
106. `107_178_EQUIVARIANT_BOUNDARY_LOCAL_CLASS.md` and
    `107_178_equivariant_boundary_local_class.py` construct the local
    replacement.  The graph--diagonal Koszul determinant is
    \(e_u=1-u\), and localization gives \(e_u^{-1}\), with normalized
    absolute value \(1/|1-u|_v\).  Twenty p-adic checks, archimedean
    checks, coordinate changes, and direct sums return
    `PADIC_LOCAL_TERM_RECOVERED: YES`,
    `DIRECT_SUM_MULTIPLICATIVITY: YES`, and `VERDICT: YES`.  The artifact
    explicitly leaves the global bilinear pairing unconstructed.
107. `107_179_EQUIVARIANT_TO_ARAKELOV_FORGETFUL_NO_GO.md` and
    `107_179_equivariant_to_arakelov_forgetful_no_go.py` prove that the
    localized class has no standard forgetful map to ordinary
    arithmetic intersection theory.  Augmentation sends \(t\) to 1 and
    the inverted Euler class \(1-t\) to zero, contradicting the
    universal property of localization.  Exact coefficient-ring checks
    return `ORDINARY_AUGMENTATION_EXTENDS: NO`,
    `DIRECT_MAP_TO_ORDINARY_ARAKELOV: NO`, and `VERDICT: YES`.  The only
    remaining bridges are global denominator cancellation or an
    equivariant Hodge theory.
108. `107_180_PROPER_COMPACTIFICATION_DENOMINATOR_CANCELLATION_NO_GO.md`
    and `107_180_proper_compactification_denominator_cancellation_no_go.py`
    close the first fork for finite-type proper coherent geometry.
    Localization on \(\mathbb P^1\) cancels the two inverse Euler
    factors, and for \(\mathcal O(n)\) yields the regular character
    \(1+t+\cdots+t^n\).  Exact checks through \(n=16\) return
    `PROPER_GLOBAL_CHARACTERS_REGULAR: YES`,
    `UNCANCELLED_LOCAL_FACTOR_SURVIVES_PROPER_SUM: NO`, and
    `VERDICT: YES`.  Preserving the explicit local distribution now
    requires a renormalized equivariant arithmetic Hodge theory.
109. `107_181_EVALUATED_EQUIVARIANT_HODGE_CALIBRATION.md` and
    `107_181_evaluated_equivariant_hodge_calibration.py` show that real
    evaluation of inverse-Euler weights is not a local sign obstruction.
    On Sage's actual toric \(\mathbb P^1\times\mathbb P^1\), the
    primitive ruling class has square \(-2\), and 24 local weights plus
    signed finite combinations remain nonpositive.  The verifier returns
    `ALL_EVALUATED_PRIMITIVE_SQUARES_NEGATIVE: YES`,
    `LOCAL_SIGN_OBSTRUCTION: NONE`, and `VERDICT: YES`, while leaving the
    global primitive realization map open.
110. `107_182_GLOBAL_EULER_BOUNDARY_GREEN_CHANNEL.md` and
    `107_182_global_euler_boundary_green_channel.py` assemble the local
    inverse-Euler classes in the half-plane of absolute convergence.
    The reduced class \(p^{-s}/(1-p^{-s})\), weighted by \(\log p\),
    sums to \(-\zeta'/\zeta\).  Exact prime-power labels and prime
    truncations through \(10^5\) return
    `EULER_LOG_DERIVATIVE_RECOVERED: YES`,
    `GLOBAL_FINITE_PRIME_GREEN_CHANNEL: CONSTRUCTED_FOR_RE_S_GT_1`, and
    `VERDICT: YES`.  Gamma completion and distributional continuation
    remain open.
111. `107_183_COMPLETED_BOUNDARY_GREEN_CHANNEL.md` and
    `107_183_completed_boundary_green_channel.py` add the forced Gamma
    and pole terms and obtain the exact completed channel
    \(-\xi'/\xi\).  Independent and decomposed evaluations agree below
    \(10^{-81}\); functional symmetry and endpoint cancellation return
    `FUNCTIONAL_SYMMETRY_ODD: YES`, `ENDPOINT_CANCELLATION: YES`, and
    `VERDICT: YES`.  The Mellin-test distribution and divisor-valued
    realization are not yet constructed.
112. `107_184_MELLIN_TEST_BOUNDARY_DISTRIBUTION.md` and
    `107_184_mellin_test_boundary_distribution.py` Mellin-invert the
    boundary channel and prove
    \(\mathcal D_{\rm fin}(g)=\sum_{p,k}\log p\,g(k\log p)\).
    Three fixed Gaussian tests compare independent contour and
    prime-power computations with maximum error below
    \(2.5\times10^{-9}\), returning
    `MELLIN_INVERSION_RECOVERS_PRIME_DISTRIBUTION: YES` and
    `VERDICT: YES`.  The scalar completed distribution is constructed;
    geometric Green-current realization remains open.
113. `107_185_PERIODIC_ORBIT_TWISTED_GREEN_KERNEL.md` and
    `107_185_periodic_orbit_twisted_green_kernel.py` realize the finite
    inverse-Euler class on Deninger's actual orbit
    \(C_p=\mathbb R/(\log p)\mathbb Z\).  The twisted operator
    \(d/dx+s\) has determinant \(1-p^{-s}\) and Green return value
    \(p^{-s}/(1-p^{-s})\).  Fifteen real-prime/spectral checks return
    `GREEN_UNIT_JUMP: YES`,
    `FINITE_ROW_B_TO_ROW_C_GREEN_BRIDGE: CONSTRUCTED`, and
    `VERDICT: YES`.  Arakelov Green-current comparison remains open.
114. `107_186_ARCHIMEDEAN_NUMBER_OPERATOR_GREEN_TRACE.md` and
    `107_186_archimedean_number_operator_green_trace.py` realize the
    Gamma term as a regularized resolvent trace of the number operator.
    Direct sums through \(10^6\) modes converge to \(-\psi(a)\) with
    error below \(2.3\times10^{-6}\), and the completed assembly agrees
    below \(10^{-61}\).  The verifier returns
    `ARCHIMEDEAN_GREEN_TRACE: CONSTRUCTED`,
    `COMPLETED_GREEN_ASSEMBLY: YES`, and `VERDICT: YES`.  A global
    Arakelov Green current remains open.
115. `107_187_COMPLETED_ORBIT_DETERMINANT.md` and
    `107_187_completed_orbit_determinant.py` assemble the prime holonomy
    determinants and the zeta determinant of \(N+s/2\) into \(\xi(s)\).
    Independent Hurwitz differentiation reaches error below
    \(8\times10^{-50}\), the prime product through \(10^5\) approximates
    the completed determinant within \(10^{-6}\), and the logarithmic
    derivative agrees below \(10^{-100}\).  It returns
    `COMPLETED_ORBIT_DETERMINANT: CONSTRUCTED` and `VERDICT: YES`, while
    leaving the determinant-line sheaf open.
116. `107_188_SEMILOCAL_DETERMINANT_LINE_SYSTEM.md` and
    `107_188_semilocal_determinant_line_system.py` construct determinant
    lines on every finite semilocal chart and transition maps given by
    the missing inverse Euler factors.  Exact nested-set checks return
    `TRIPLE_TRANSITION_COCYCLE: YES`; the cofinal canonical section
    converges to \(\xi\) with final error below \(5\times10^{-7}\).
    The verifier returns `SEMILOCAL_DETERMINANT_LINE_SYSTEM: CONSTRUCTED`
    and `VERDICT: YES`, without claiming absolute-square sheaf descent.
117. `107_189_SPECTRAL_DETERMINANT_LINE_SHEAF_ON_SPEC_Z.md` and
    `107_189_spectral_determinant_line_sheaf_on_spec_z.py` prove sheaf
    descent on the semilocal Zariski basis of
    \(\mathrm{Spec}\,\mathbb Z\).  The inverse-Euler restrictions
    are units for \(\Re s>1\), and a frame change identifies the system
    with a constant rank-one sheaf.  Exact cover equalizers return
    `UNIQUE_SHEAF_GLUE: YES`,
    `SPECTRAL_DETERMINANT_LINE_SHEAF_ON_SPEC_Z: CONSTRUCTED_FOR_RE_S_GT_1`,
    and `VERDICT: YES`.  The absolute-square line bundle and
    self-intersection remain open.
118. `107_190_EXTERNAL_PRODUCT_SPECTRAL_LINE_ON_SEMILOCAL_SQUARE.md` and
    `107_190_external_product_spectral_line_on_semilocal_square.py`
    construct the external-product line on the product semilocal site.
    Row and column restrictions commute, the product Cech equalizers
    glue uniquely, and diagonal pullback retains tensor multiplicity.
    The verifier also rejects the false identification
    \(z_p(ns)z_p(ms)=z_p((n+m)s)\), so spectral specialization is not
    promoted to the algebraic Frobenius correspondence.  It returns
    `SEMILOCAL_SQUARE_EXTERNAL_PRODUCT_LINE: CONSTRUCTED` and
    `VERDICT: YES`.  A top class, Deligne pairing, proper absolute
    surface, and intersection form remain open.
119. `107_191_UNMETRIZED_SPECTRAL_LINE_INTERSECTION_NO_GO.md` and
    `107_191_unmetrized_spectral_line_intersection_no_go.py` prove that
    the spectral transition cocycle is an explicit coboundary on both
    the curve and product sites.  The ordinary Picard and first-Chern
    classes vanish, while the canonical section has empty divisor on
    \(\Re s>1\).  A deliberately corrupted edge is rejected by the exact
    exponent-vector cocycle test.  It returns
    `UNMETRIZED_DELIGNE_PAIRING_ROUTE: CLOSED_NO_GO` and `VERDICT: YES`.
    Metrics, currents, critical-strip extension, and secondary classes
    are not excluded.
120. `107_192_FLAT_GREEN_CONNECTION_CURVATURE_NO_GO.md` and
    `107_192_flat_green_connection_curvature_no_go.py` realize the
    completed Green channel as the logarithmic connection one-form
    \(-d\log\xi\) on \(\Re s>1\), then prove that its connection and
    Chern curvatures vanish.  The decomposition agrees below \(2\times
    10^{-81}\); a deliberately nonflat metric mutation has curvature
    four and is detected.  It returns
    `SMOOTH_DETERMINANT_METRIC_C1_ROUTE: CLOSED_NO_GO` and
    `VERDICT: YES`.  Singular boundary and secondary-current routes
    remain open.
121. `107_193_SINGULAR_SPECTRAL_DIVISOR_CURRENT.md` and
    `107_193_singular_spectral_divisor_current.py` extend the flat Green
    connection singularly and obtain the Poincare--Lelong divisor
    current of the source-derived entire determinant.  Twelve actual
    zeta zeros are distinct; six contour integrals recover multiplicity
    one below \(5\times10^{-60}\), while an empty contour rejects a
    false atom.  Hardy's infinite-zero theorem proves that no proper
    finite-type algebraic spectral curve with a finite-degree line can
    carry the full divisor.  It returns
    `FINITE_TYPE_PROPER_SPECTRAL_COMPACTIFICATION: CLOSED_NO_GO` and
    `VERDICT: YES`.  A Green current on the arithmetic square remains
    unconstructed.
122. `107_194_PRIME_ORBIT_SECONDARY_CURRENT_APPLICABILITY_NO_GO.md` and
    `107_194_prime_orbit_secondary_current_applicability_no_go.py` prove
    that an isolated Deninger prime circle cannot carry the published
    Koehler--Roessler/Bismut--Goette secondary current.  It is odd
    dimensional and noncomplex; nonreturn translations have no fixed
    locus, while returns are the identity with zero tangent Euler class.
    On five real prime orbits the twisted determinant remains nonzero,
    proving that holonomy is not the missing normal Euler class.  It
    returns `DIRECT_SECONDARY_CURRENT_ON_PRIME_ORBIT: CLOSED_NO_GO` and
    `VERDICT: YES`.  An ambient complex transverse realization remains
    open.
123. `107_195_FLAT_TATE_TORUS_DETERMINANT_NO_GO.md` and
    `107_195_flat_tate_torus_determinant_no_go.py` test the standard
    flat compact complexification with \(q=p^{-s}\).  Kronecker's
    determinant contains the full eta Fourier tower.  Across 15 fixed
    real Tate tori the ratio to \(|1-q|^2\) has spread
    \(0.323299590336\), while the omitted product tail is bounded below
    \(10^{-50}\).  It returns
    `STANDARD_FLAT_TATE_TORUS_BRIDGE: CLOSED_NO_GO` and `VERDICT: YES`.
    Virtual cancellation and relative determinants remain open.
124. `107_196_RELATIVE_FOCK_DETERMINANT_CANCELLATION.md` and
    `107_196_relative_fock_determinant_cancellation.py` construct the
    virtual cancellation left open by `107_195`.  The canonical
    number-filtration exact sequence gives \(D_1/D_2=1-q\), with no
    discarded tail.  Five primes, three real/complex parameters, and
    four cutoffs agree below \(8\times10^{-71}\); the Green derivative
    agrees below \(2\times10^{-72}\), and a wrong shift is rejected.
    It returns `RELATIVE_FOCK_DETERMINANT: CONSTRUCTED` and
    `VERDICT: YES`.  Secondary geometric realization remains open.
125. `107_197_ORTHOGONALLY_SPLIT_FOCK_BOTT_CHERN_NO_GO.md` and
    `107_197_orthogonally_split_fock_bott_chern_no_go.py` prove that the
    canonical Fock-tail sequence has zero standard Bott--Chern anomaly.
    Five finite cutoffs are exact, orthogonal, and number-equivariant;
    determinant multiplicativity holds below \(10^{-60}\), while an
    off-diagonal metric mutation is detected.  It returns
    `STANDARD_FOCK_BOTT_CHERN_ROUTE: CLOSED_NO_GO` and `VERDICT: YES`.
    A dynamically derived off-diagonal superconnection remains open.
126. `107_198_ONE_WAY_SHIFT_SUPERCONNECTION_NO_GO.md` and
    `107_198_one_way_shift_superconnection_no_go.py` prove that a pure
    raising or lowering trace-class weighted shift has Fredholm
    determinant one.  Across 150 real/complex finite matrices all
    positive trace powers vanish and both determinants are exactly one;
    a diagonal quotient mutation produces \(1-q\) and is detected.
    It returns `ONE_WAY_SHIFT_SUPERCONNECTION: CLOSED_NO_GO` and
    `VERDICT: YES`.  Bidirectional loops and boundary eta classes remain
    open.
127. `107_199_BALANCED_BIDIRECTIONAL_DIRAC_LOOP.md` and
    `107_199_balanced_bidirectional_dirac_loop.py` construct the
    transpose-symmetric two-state local loop with half-weight
    \(p^{-s/2}\).  Fifteen real/complex matrices recover
    \(1-p^{-s}\), its Green derivative, and eigenvalues
    \(\pm p^{-s/2}\) below \(2\times10^{-72}\).  Three asymmetric
    exponent families collide in determinant but fail transpose and are
    rejected.  It returns `BALANCED_BIDIRECTIONAL_DIRAC_LOOP:
    CONSTRUCTED` and `VERDICT: YES`.  Global glue and a secondary
    current remain open.
128. `107_200_GLOBAL_BALANCED_DIRAC_HILBERT_SCHMIDT_DETERMINANT.md` and
    `107_200_global_balanced_dirac_hilbert_schmidt_determinant.py`
    globalize all prime blocks in one Hilbert--Schmidt operator and
    prove \(\det_2(1-D_s)=\zeta(s)^{-1}\) for \(\Re s>1\).  Pairwise
    exponential corrections cancel exactly.  Using 9,592 primes, the
    product error is below \(4.9\times10^{-7}\), the Green error below
    \(10^{-5}\), Hilbert--Schmidt tails stabilize, trace norms grow in
    the non-trace-class strip, and an unpaired mutation is rejected.
    It returns `GLOBAL_BALANCED_PRIME_DIRAC_DET2:
    CONSTRUCTED_FOR_RE_S_GT_1` and `VERDICT: YES`.
129. `107_201_HIGHER_SCHATTEN_DETERMINANT_COUNTERTERM_NO_GO.md` and
    `107_201_higher_schatten_determinant_counterterm_no_go.py` compute
    every paired higher-determinant counterterm and prove that order
    five is minimal on the critical line.  Orders 3, 5, and 6 differ
    from the Euler determinant; the finite global order-five formula
    contains \(\exp(P(s)+P(2s)/2)\).  Four orders agree with the exact
    formula below \(2\times10^{-61}\).  It returns
    `UNCORRECTED_HIGHER_SCHATTEN_CONTINUATION: CLOSED_NO_GO` and
    `VERDICT: YES`.  A derived global counterterm remains open.
130. `107_202_ARCHIMEDEAN_COUNTERTERM_CANCELLATION_NO_GO.md` and
    `107_202_archimedean_counterterm_cancellation_no_go.py` prove that
    Gamma and pole blocks cannot cancel the order-five counterterm.
    Exact Mobius coefficients cancel the half-line branch but leave
    coefficients \(-1/3\) and \(-1/4\); numerical continuation recovers
    the one-third slope as \(0.333393849102\), while the archimedean
    factor is regular there.  It returns
    `GAMMA_POLE_COUNTERTERM_CANCELLATION: CLOSED_NO_GO` and
    `VERDICT: YES`.  Prime-side relative branch data remains open.
131. `107_203_FINITE_ORDER_CHANGE_RENORMALIZATION_AND_COFINAL_NO_GO.md`
    and `107_203_finite_order_change_renormalization_and_cofinal_no_go.py`
    derive the exact finite-support order-change correction, then prove
    that its ordinary critical cofinal limit is not analytic
    continuation.  The finite identity holds below \(3\times10^{-71}\);
    at one million primes the critical log product is
    \(-178.317170545\), while \(1/\zeta(1/2)=-0.68476523609\).  It
    returns `CRITICAL_NORM_DETERMINANT_CONTINUATION: CLOSED_NO_GO` and
    `VERDICT: YES`.  Nonlocal summation or a nuclear trace remains open.
132. `107_204_MEYER_NUCLEAR_CONTINUATION_BRIDGE.md` and
    `107_204_meyer_nuclear_continuation_bridge.py` import Meyer's
    published nuclear continuation with its exact scope.  Mobius
    inversion passes through \(n=500\), while 254 coprime
    Davenport--Heilbronn failures reject the prime-orbit character
    before spectral continuation.  It returns
    `MEYER_NUCLEAR_CONTINUATION: PUBLISHED_AND_ADMISSIBLE`,
    `MEYER_HODGE_POSITIVITY: NOT_SUPPLIED`, and `VERDICT: YES`.
133. `107_205_MELLIN_SYMBOL_COMPARISON_PRIME_DIRAC_TO_MEYER.md` and
    `107_205_mellin_symbol_comparison_prime_dirac_to_meyer.py` prove
    that Mellin transform identifies Meyer's Zeta operator with the
    inverse \(\det_2\) symbol of the global balanced prime Dirac
    operator.  Three independent Mellin integrals agree below
    \(1.6\times10^{-61}\), while a mutated dilation coefficient is
    rejected.  It returns `DIRAC_TO_MEYER_MELLIN_COMPARISON:
    CONSTRUCTED_ON_RE_S_GT_1` and `VERDICT: YES`.
134. `107_206_MORISHITA_BALANCED_LOCAL_CHARACTER_PUSHFORWARD.md` and
    `107_206_morishita_balanced_local_character_pushforward.py` prove
    that Meyer's two-sided finite-prime character is invariant under
    the modular flow inversion induced by Morishita's
    anti-equivariant bridge.  Five actual prime orbits pass below
    (9.1\times10^{-72}), while every oriented half fails by at least
    (0.4386).  The same theorem identifies the exact packet-trace
    kernel as the coefficient-sum-zero hyperplane.  It returns
    `MORISHITA_FINITE_CHARACTER_PUSHFORWARD: CONSTRUCTED`,
    `PACKET_SENSITIVE_BASE_CURRENT: NOT_CONSTRUCTED`, and
    `VERDICT: YES`.  No square current or intersection is claimed.
135. `107_207_ARCHIMEDEAN_GERM_GEOMETRIZES_FOCK_DETERMINANT.md` and
    `107_207_archimedean_germ_geometrizes_fock_determinant.py` use the
    archimedean-local complex-point moduli of Connes--Consani
    (arXiv:2606.06604v1) to realize the Fock tails of `107_196` as the
    completed powers of the maximal ideal at the trivial fixed point.
    The quotient is the intrinsic cotangent line and its Lefschetz
    normal determinant is (1-p^{-s}).  Five primes, three spectral
    parameters, and nonlinear exact jet changes pass, with maximum
    numerical error (5.6\times10^{-71}).  It returns
    `CC_ARCHIMEDEAN_GERM_FOCK_REALIZATION: CONSTRUCTED`,
    `PROPER_GLOBAL_FIXED_SECTION: NOT_CONSTRUCTED`, and `VERDICT: YES`.
    The compact Tate quotient removes the fixed point, so no global
    square pushforward is promoted.
136. `107_208_FIXED_POINT_TATE_COMPACTIFICATION_NO_GO.md` and
    `107_208_fixed_point_tate_compactification_no_go.py` close the
    ordinary compactification route for the fixed germ.  The orbit
    \(\{p^n\}\) accumulates at zero (and at infinity on
    \(\mathbb P^1\)), so retaining the fixed point makes the coarse
    quotient non-\(T_1\).  Conversely, the Tate curve is already compact
    and cannot be a proper dense open subset of a larger Hausdorff
    compactification.  Five primes and 25 exact neighborhood tests pass.
    It returns `ORDINARY_FIXED_POINT_COMPACTIFICATION:
    CLOSED_NO_GO`, `STACKY_OR_RELATIVE_BOUNDARY_ROUTE: OPEN`, and
    `VERDICT: YES`.
137. `107_209_EQUIVARIANT_DERIVED_FIXED_POINT_INTERSECTION.md` and
    `107_209_equivariant_derived_fixed_point_intersection.py` form the
    fixed-point class before the forbidden coarse quotient.  For the
    regular embedding of the trivial point, the equivariant derived
    self-intersection is
    \(\lambda_{-1}(\mathfrak m/\mathfrak m^2)=1-\chi\); evaluating
    \(\chi=p^{-s}\) gives exactly \(1-p^{-s}\).  Exact Tor tests,
    nonlinear jet conjugacies, and 15 prime/parameter Green derivatives
    pass below \(4.6\times10^{-72}\), while underived pullback is
    rejected.  It returns `EQUIVARIANT_DERIVED_LOCAL_INTERSECTION:
    CONSTRUCTED`, `PROPER_NUMERICAL_PUSHFORWARD: NOT_CONSTRUCTED`, and
    `VERDICT: YES`.
138. `107_210_GLOBAL_NUCLEAR_PUSHFORWARD_OF_LOCAL_INTERSECTIONS.md` and
    `107_210_global_nuclear_pushforward_of_local_intersections.py`
    assemble the conormal lines into the trace-class operator
    \(Q_s=\bigoplus_p p^{-s}\) on \(\Re s>1\).  Its Fredholm determinant
    is the product of the local derived self-intersections and equals
    \(\zeta(s)^{-1}\); its logarithmic trace is
    \(-\zeta'/\zeta\).  The first 9,592 primes pass at real and complex
    parameters, with observed errors below \(8.1\%\) of fixed explicit
    omitted-tail bounds.  Critical trace-norm growth is detected.  It
    returns `GLOBAL_NUCLEAR_INTERSECTION_PUSHFORWARD:
    CONSTRUCTED_ON_RE_S_GT_1`, `CRITICAL_LINE_TRACE_CLASS_PUSHFORWARD:
    CLOSED_NO_GO`, and `VERDICT: YES`.
139. 107_211_PROPER_EQUIVARIANT_PUSHFORWARD_OF_EULER_NUMERATOR.md and
    107_211_proper_equivariant_pushforward_of_euler_numerator.py
    compactify the CC local line equivariantly to \(\mathbb P^1\) before
    quotienting.  On the proper square, the diagonal and scaling graph
    have normal determinant \(1-\chi\) at the canonical trivial point.
    The supported derived class pushes properly to the same numerator,
    with zero infinity contribution.  The structure-sheaf mutation
    instead exhibits the denominator cancellation of 107_180, and
    ordinary augmentation kills the numerator.  Five prime characters
    pass.  It returns PROPER_EQUIVARIANT_EULER_NUMERATOR: CONSTRUCTED,
    RENORMALIZED_ARITHMETIC_HODGE_PUSHFORWARD: NOT_CONSTRUCTED, and
    VERDICT: YES.
140. 107_212_ARITHMETIC_DEGREE_OF_LOCALIZED_PRIME_CLASS.md and
    107_212_arithmetic_degree_of_localized_prime_class.py construct,
    for every finite prime support, the localized arithmetic class
    \(\widehat{[p]}\chi_p/(1-\chi_p)\).  Its arithmetic degree at
    \(\chi_p=p^{-s}\) is exactly
    \(\log p\,p^{-s}/(1-p^{-s})\), and the return series is the
    logarithmic character of the proper Euler numerator from 107_211.
    Ordinary \(G_0\) kills the prime torsion class, while arithmetic
    degree retains \(\log p\).  The first 9,592 primes pass, with global
    error below \(7.98\%\) of the fixed tail bound and determinant-degree
    mismatch below \(3.9\times10^{-62}\).  It returns
    FINITE_SUPPORT_ARITHMETIC_GREEN_CLASS: CONSTRUCTED,
    INFINITE_SUPPORT_ARITHMETIC_DIVISOR: NOT_CONSTRUCTED, and
    VERDICT: YES.
141. 107_213_PUBLISHED_ARITHMETIC_LRR_NONUNITARY_APPLICABILITY_NO_GO.md
    and 107_213_published_arithmetic_lrr_nonunitary_applicability_no_go.py
    separate the two published arithmetic Lefschetz routes.  Tang's
    coefficient ring forces \(T^n=1\), so no specialization or
    finite-cyclic limit reaches \(p^{-s}\) with \(\Re s>0\).
    Koehler--Roessler's full torus residue formula validates the
    infinitesimal arithmetic localization shape, but its analytic
    torsion identity is proved for unitary circle elements, not the
    required nonunitary character.  Fifteen actual prime characters are
    rejected with radial gap at least \(0.5795\), while unitary controls
    are accepted.  It returns KR_NONUNITARY_TORSION_IDENTITY:
    NOT_PROVED, PUBLISHED_ARITHMETIC_LRR_CLOSES_GLOBAL_PUSHFORWARD: NO,
    and VERDICT: YES.
142. 107_214_R_GENUS_NONUNITARY_MONODROMY_AND_LOG_LIFT.md and
    107_214_r_genus_nonunitary_monodromy_and_log_lift.py compute the
    degree-zero Bismut \(R_g\) anomaly of a flat normal line through the
    order derivative of the polylogarithm.  At \(q=p^{-s}\), its
    reciprocal argument crosses the polylogarithm cut and produces
    discontinuity \(2\pi i/(s\log p)\).  Therefore no single-valued
    extension depending only on \(q\) exists.  Arithmetic weighting by
    \(\log p\) cancels the prime dependence and leaves \(2\pi i/s\),
    forcing a logarithmic lift and a global white-light subtraction.
    Ten actual prime lifts pass with maximum error
    \(8.5\times10^{-13}\).  It returns UNLIFTED_NONUNITARY_R_GENUS:
    CLOSED_NO_GO, LOG_LIFTED_RELATIVE_R_GENUS: OPEN, and VERDICT: YES.
143. 107_215_MINIMAL_RELATIVE_R_GENUS_AND_POINTWISE_GAMMA_NO_GO.md and
    107_215_minimal_relative_r_genus_and_pointwise_gamma_no_go.py
    construct the unique minimal scalar boundary correction
    \(D^{\mathrm{rel}}(x)=D(x)+\log(1-x)/\log x\).  It cancels the two
    lateral values of the nonunitary reciprocal polylogarithm and gives
    a real log-lifted relative anomaly on the positive character ray.
    Arithmetic weighting still varies with the prime at fixed spectral
    parameter, so it cannot equal the Gamma Green term prime by prime.
    Ten actual prime anomalies pass with boundary and reality errors
    below \(4.7\times10^{-13}\).  It returns
    LOG_LIFTED_RELATIVE_R_GENUS: CONSTRUCTED_SCALAR_LEVEL,
    POINTWISE_PRIME_ANOMALY_EQUALS_GAMMA: NO,
    GLOBAL_GAMMA_COMPARISON: NOT_CONSTRUCTED, and VERDICT: YES.
144. 107_216_RELATIVE_R_GENUS_PRIME_SUM_NO_GO.md and
    107_216_relative_r_genus_prime_sum_no_go.py derive an exact
    Jonquiere--digamma expression for the corrected anomaly and prove
    \(R^{\mathrm{rel}}(p^{-s})=\log\log(p^s)+\gamma-1+o(1)\).  Hence
    its arithmetic weighting grows like
    \(\log p\,\log\log p\), so the ordinary prime sum cannot converge:
    its terms do not tend to zero.  Ten lateral-value identities and
    five fixed large actual primes certify the branches and constants;
    the weighted controls grow from 15.37 to 88.74 while the asymptotic
    error falls to 0.00129.  It returns ORDINARY_PRIME_SUM:
    CLOSED_NO_GO, GLOBAL_NUCLEAR_QUOTIENT_REQUIRED: YES, and
    VERDICT: YES.  No global Gamma comparison or arithmetic direct image
    follows.
145. 107_217_CYCLOTOMICALLY_TWISTED_CELLULAR_H1.md and
    107_217_cyclotomically_twisted_cellular_h1.sage compute the integral
    middle cohomology of the rooted cellular square with a genuine
    cyclotomic rank-one twist.  For
    \(I=(\zeta_n^u-1,\zeta_n^v-1)\), they prove
    \(H^0=O/I\), \(H^1=I^{-1}/O\), and \(H^2=0\) off the trivial
    character, with equal torsion orders \(N(I)\).  The torsion survives
    exactly when the effective character order is a prime power; the
    trivial character recovers free ranks \((1,2,1)\).  Eight actual
    cyclotomic integer rings pass integral Smith/homology calculations,
    including torsion order 27 at level 9, while a sign mutation is
    rejected.  It returns FINITE_ROOTED_MIDDLE_COHOMOLOGY: CONSTRUCTED,
    DIVISOR_SHEAF_H1: NOT_CONSTRUCTED, and VERDICT: YES.
146. 107_218_ROOTED_INCLUSION_VS_CELLULAR_SUBDIVISION_NO_GO.md and
    107_218_rooted_inclusion_vs_cellular_subdivision_no_go.sage prove
    that the two transition systems used around 107_169 are not one
    descent datum.  Rooted normalization retains \(\zeta\), whereas
    cellular subdivision \(x\mapsto x'^d\) restricts characters by
    \(\zeta\mapsto\zeta^d\); they agree only when the character order
    divides \(d-1\).  Sending \(x\mapsto x'\) cannot repair the mismatch
    because it does not respect \(x^L=1\) at a larger level.  Six actual
    cyclotomic transitions move every fixed primitive control, while an
    exceptional fixed-label control passes.  It returns
    ROOTED_CELLULAR_COMMON_DESCENT: CLOSED_NO_GO,
    TWISTED_H1_DIRECT_SYSTEM: NOT_CONSTRUCTED, and VERDICT: YES.
147. 107_219_COMPONENTWISE_CYCLOTOMIC_H1_DESCENT.md and
    107_219_componentwise_cyclotomic_h1_descent.sage repair that no-go
    on the disjoint cyclotomic normalization.  A pair of labels of
    orders \(n,m\) defines a Koszul complex over
    \(\mathbb Z[\zeta_{\mathrm{lcm}(n,m)}]\).  Because every old
    normalized component is open and closed at every larger level,
    finite-support direct sums and their integral cohomology stabilize
    strictly by extension by zero.  Five actual mixed components detect
    both acyclicity and torsion of orders 4, 5, and 27; their integral
    differentials are unchanged at levels \(L,2L,6L\), while the old
    power-subdivision transition is rejected.  It returns
    FINITE_SUPPORT_TWISTED_H1_DESCENT: CONSTRUCTED,
    DIVISOR_MODULE_COMPARISON: NOT_CONSTRUCTED, and VERDICT: YES.
148. 107_220_DIRECT_ADELIC_TO_CYCLOTOMIC_H1_NO_GO.md and
    107_220_direct_adelic_to_cyclotomic_h1_no_go.sage close the direct
    comparison with the published adelic \(H^1(D)\).  Its underlying
    group \(\mathbb A_\mathbb Q\) is divisible, whereas the nonzero
    cyclotomic middle groups are finite; every additive image is
    therefore zero.  The fixed mixed atlas recomputes targets
    \(C_2^2,C_5,C_3^3\), verifies that none is divisible, and accepts
    nonzero lattice maps as a negative control.  It returns
    DIRECT_DIVISOR_H1_COMPARISON: CLOSED_NO_GO,
    PONTRYAGIN_DUAL_COMPARISON_REQUIRED: YES, and VERDICT: YES.
149. 107_221_CODIFFERENT_SERRE_DUALITY_FOR_CYCLOTOMIC_H1.md and
    107_221_codifferent_serre_duality_for_cyclotomic_h1.sage construct
    that dual interface componentwise.  The trace pairing identifies
    \((O/I)^\vee\) with
    \(I^{-1}\mathfrak D^{-1}/\mathfrak D^{-1}\), the middle cohomology
    of the Koszul complex twisted by the codifferent.  Three actual
    components have matching indices 4, 5, and 27 and integral
    unimodular trace matrices; naive self-duality of \(O\) is rejected by
    discriminants 256, 125, and 19683.  It returns
    COMPONENTWISE_SERRE_DUALITY: CONSTRUCTED,
    GLOBAL_CANONICAL_DIVISOR_COMPARISON: NOT_CONSTRUCTED, and
    VERDICT: YES.
150. 107_222_RELATIVE_CODIFFERENT_DUALIZER_ON_ROOTED_NORMALIZATION.md
    and
    107_222_relative_codifferent_dualizer_on_rooted_normalization.sage
    show that the base canonical divisor \(-2\{2\}\) cannot alone
    dualize all rooted components: cyclotomic differents have forced
    support at odd ramified primes.  They construct the strict relative
    dualizing system \(\coprod_{n\mid L}\mathfrak D_n^{-1}\), retained
    under every open-and-closed level enlargement.  Six conductors
    verify different norm equals discriminant and detect supports at
    2, 3, and 5.  It returns RELATIVE_ROOTED_DUALIZER: CONSTRUCTED,
    BASE_K_SUPPORT_ONLY_AT_2_SUFFICIENT: NO,
    GLOBAL_ABSOLUTE_SERRE_DUALITY: NOT_CONSTRUCTED, and VERDICT: YES.
151. 107_223_FLAT_CHARACTER_COMPLEX_RR_NO_GO.md and
    107_223_flat_character_complex_rr_no_go.sage prove that the
    stabilized character complexes cannot themselves be the divisor
    RR complexes.  Every flat Koszul complex has Euler class
    \([M]-2[M]+[M]=0\); its finite \(H^0,H^1\) lengths cancel place by
    place, including after the codifferent twist.  The published CC
    divisors at radii 1, 4, 13, and 40 instead have Euler dimensions
    1, 2, 3, and 4.  Three actual torsion components verify zero local
    Euler characteristic, and a rank-mutated nonflat control produces a
    nonzero value.  It returns
    ORDINARY_FLAT_EULER_AS_DIVISOR_RR: CLOSED_NO_GO,
    DIVISOR_DEPENDENT_METRIC_TOLERANCE_OR_C1_REQUIRED: YES, and
    VERDICT: YES.  The result does not exclude a divisor-dependent
    bounded/tolerance structure on the same underlying complex.
152. 107_224_ARCHIMEDEAN_C1_ASSIGNMENT_NO_GO.md and
    107_224_archimedean_c1_assignment_no_go.py prove that the real
    Arakelov divisor direction cannot be stored additively in an
    integral Chern class or any finite-rank Neron--Severi group.  The
    source \(\mathbb R\{\infty\}\) is divisible, while finitely generated
    targets have no nonzero divisible subgroup.  The fixed CC radii
    1, 4, 13, 16, and 40 also reject the raw and zero-normalized integer
    dimensions as additive Chern assignments.  It returns
    ARCHIMEDEAN_REAL_TO_FINITE_RANK_C1: ZERO_ONLY,
    ARCHIMEDEAN_VARIATION_MUST_BE_METRIC_OR_TOLERANCE: YES, and
    VERDICT: YES.
153. 107_225_FINITE_TORSION_TOLERANCE_NO_GO.md and
    107_225_minkowski_tolerance_metric_probe.sage equip the finite
    cyclotomic middle groups with the canonical normalized Minkowski
    quotient metric and exhaust their CC tolerant generators.  Their
    dimensions freeze at \((2,2,2)\), \((2,2,2)\), and \((3,3,3)\) over
    radii \(1/2,1/6,1/18\).  In general every finite metric group has a
    positive minimum distance, so its tolerant dimension is bounded and
    eventually constant, unlike the unbounded CC circle dimension.  It
    returns FINITE_TORSION_H1_AS_CC_TOLERANT_H1: CLOSED_NO_GO,
    FULL_MINKOWSKI_TORUS_REQUIRED: YES, and VERDICT: YES.
154. 107_226_MINKOWSKI_TORUS_TOLERANCE_LOWER_BOUND.md and
    107_226_minkowski_torus_tolerance_lower_bound.sage prove the volume
    bound
    \(\dim(T_\lambda)\ge\lceil\log_3(1/(v_d\lambda^d))\rceil\)
    on every covolume-one Euclidean torus.  It recovers the exact CC
    lower bound at \(d=1\) and forces asymptotic slope
    \(d/\log3\).  Actual degree-4 cyclotomic tori give fixed bounds
    \((2,6,10)\), the degree-6 torus gives \((3,9,15)\), and a
    dimension-blind mutation is rejected.  It returns
    FULL_MINKOWSKI_TORUS_HAS_UNBOUNDED_TOLERANCE_CAPACITY: YES,
    MATCHING_BALANCED_UPPER_BOUND: NOT_CONSTRUCTED, and VERDICT: YES.
155. 107_227_METRIC_KERNEL_TARGET_SELECTION_THEOREM.md and
    107_227_metric_kernel_target_selection_theorem.py prove the exact
    target restriction selected by 107_223--107_225. Every additive map
    from the real archimedean divisor direction to a finitely generated
    algebraic shadow is zero, but tensor-compatible metrized objects
    retain a nonzero additive real kernel; the CC integer dimension is a
    forced nonlinear invariant of that kernel. A rounded metric mutation
    is rejected. It returns FINITE_RANK_ALGEBRAIC_CHANNEL:
    CONSTANT_ON_REAL_DIVISORS, TENSOR_COMPATIBLE_METRIC_CHANNEL:
    NONTRIVIAL, CC_INTEGER_DIMENSION_ADDITIVE: NO, SURVIVING_TARGET:
    METRIZED_OR_TOLERANT_PICARD, and VERDICT: YES.
156. 107_228_FINITE_RAY_STABILIZATION_VS_PERIODIC_RR_NO_GO.md and
    107_228_finite_ray_stabilization_vs_periodic_rr_no_go.py correct the
    open gate of 107_155 Section 4. The published periodic RR theorem
    gives \(p^{-n}\mathrm{tdim}\,H^0(D)^{p^n}\to\deg D>0\), so the
    filtered dimensions are necessarily unbounded; finite-ray
    stabilization cannot model the full periodic \(H^0\). The finite
    stages survive only as a pro-filtration with renormalized continuous
    dimension. The verifier reads the published TeX source and returns
    FINITE_RAY_STABILIZATION_AS_FULL_H0: CLOSED_NO_GO,
    REQUIRED_LIMIT: RENORMALIZED_CONTINUOUS_PRO_DIMENSION, and
    VERDICT: YES.
157. 107_229_NORM_ADAPTED_PRO_DIMENSION_ON_THE_TWO_RULINGS.md and
    107_229_norm_adapted_pro_dimension.py prove that the rectangular
    levels of 107_154 have zero density under the published \(p^{-R}\)
    normalization and replace them with
    \(N_p(A,R)=p^{-R}\mathbb Z\cap[0,A]\). These levels have exact
    Frobenius covariance and \(\lfloor Ap^R\rfloor+1\) rays. At
    coefficient mass one, the independently normalized two-ruling
    dimension converges to \(AB\) along every cofinal path, with an
    explicit error bound. It returns TWO_RULING_COFINAL_LIMIT:
    PRODUCT_OF_WINDOW_LENGTHS and ONE_RULING_ACTUAL_H0_LIMIT: MATCHED.
    The latter uses the published exact formula
    \(\mathrm{tdim}\,H^0(\alpha\{1\})^{p^n}=\alpha p^n-p+1\):
    the support count differs by exactly \(p\), hence has the same
    normalized limit. FULL_PERIODIC_H0_DIMENSION remains
    NOT_CONSTRUCTED, and VERDICT: YES.
158. 107_230_CARTESIAN_SECTION_PRODUCT_BIDEGREE_NO_GO.md and
    107_230_cartesian_section_product_bidegree_no_go.py prove that the
    Cartesian product of the two published periodic section spaces has
    dimension \(d_{p,n}+d_{q,m}\), hence zero limit after the required
    \(p^{-n}q^{-m}\) normalization along every cofinal path. The proof
    uses the published parameter cells for the lower bound and the
    covering-dimension product theorem for the upper bound. A mixed
    product control retains a nonzero \(\alpha\beta\) limit. It returns
    CARTESIAN_BIDEGREE_NORMALIZED_LIMIT: ZERO,
    MIXED_PARAMETER_CHANNEL_REQUIRED: YES, and VERDICT: YES.
159. 107_231_MIXED_TROPICAL_EXTERNAL_SECTION_CELL.md and
    107_231_mixed_tropical_external_section_cell.py construct the first
    genuine bivariate section family with product dimension. Starting
    from the published CC generators, the external sums
    \(B_{ij}(x,y)=g_i(x)+h_j(y)\) have product dominance rectangles.
    Small independent coefficient perturbations are recovered by
    evaluation on those rectangles, giving an embedded open cell of
    exact dimension \((N-p+1)(M-q+1)\) and normalized cofinal limit
    \(\alpha\beta\). A row-plus-column mutation is rejected. It returns
    MIXED_EXTERNAL_SECTION_CELL: CONSTRUCTED, CELL_DIMENSION: PRODUCT,
    GLOBAL_SQUARE_H0: NOT_CONSTRUCTED, and VERDICT: YES.
160. 107_232_EXACT_EXTERNAL_TENSOR_H0_FOR_SPECIAL_DIVISORS.md and
    107_232_exact_external_tensor_h0.py use the published theorem that
    the \(N-p+1\) CC functions are all extremal rays and generate the
    complete module \(\mathcal E_{N,p}\). Their external tensor image is
    therefore generated by exactly \((N-p+1)(M-q+1)\) mixed rays.
    The coefficient parametrization gives the matching upper bound and
    107_231 gives the lower cell, proving exact covering dimension and
    cofinal limit \(\alpha\beta\). It returns
    FULL_SPECIAL_EXTERNAL_H0_DIMENSION: PRODUCT, FRAME_DEPENDENCE: NO,
    and VERDICT: YES.
161. 107_233_ARBITRARY_EXTERNAL_DIVISOR_CONTINUOUS_DIMENSION.md and
    107_233_arbitrary_external_divisor_continuous_dimension.py extend
    the exact tensor dimension to every external divisor on a fixed
    periodic product. The published principal-translation/effective-
    inclusion squeeze maps tensorize as embeddings, so special degrees
    \(\alpha_-\beta_-\) and \(\alpha_+\beta_+\) squeeze the arbitrary
    module to
    \(\max(\deg D,0)\max(\deg E,0)\). Component classes are retained and
    cofinal paths are unrestricted. It returns
    ARBITRARY_EXTERNAL_DIVISOR_SQUEEZE: CONVERGENT,
    COFINAL_PATH_DEPENDENCE: NONE, and VERDICT: YES.
162. 107_234_ARITHMETIC_DIVISOR_SHEAF_TENSOR_DESCENT.md and
    107_234_arithmetic_divisor_sheaf_tensor_descent.py close the global
    module carrier required by that local result. Using the arithmetic
    Picard and divisor sheaves constructed in arXiv:2602.15941v1, they
    prove that multiplication identifies
    \(L_1\otimes_{\mathbb Z}L_2\) with \(L_1L_2\), that no derived
    torsion term occurs, and that the projective archimedean mass is
    exactly the product-divisor mass. Thus
    \(\mathcal O(\mathcal D_1)\widehat\otimes_{\mathcal O,\pi}
    \mathcal O(\mathcal D_2)\simeq
    \mathcal O(\mathcal D_1\mathcal D_2)\), and a canonical external
    module exists on the product topos. It returns
    ARITHMETIC_DIVISOR_SHEAF_TENSOR_DESCENT: CLOSED and VERDICT: YES.
    Row (a) remains partial: comparison with Scaling-Site periodic
    \(H^0\), intrinsically mixed divisors, \(H^1\), and square RR are
    not proved.
163. 107_235_DIRECT_DIVISOR_SHEAF_TO_PERIODIC_H0_NO_GO.md and
    107_235_direct_divisor_sheaf_to_periodic_h0_no_go.py close the
    direct form of that comparison. Every unextended Gamma-module
    stalk built from \(L\subset\mathbb Q\) is countable, and finite
    tensors, countable sheafification, and filtered stalk colimits stay
    countable. Positive-degree periodic \(H^0\), by contrast, contains
    the real open cells proved in 107_231 and has continuum cardinality.
    Thus no direct map can be surjective. The 2026 absolute-geometry
    paper supplies tropicalization only at structure-sheaf level and
    explicitly leaves periodic eigenspace descent open. It returns
    DIRECT_COMPARISON_SURJECTIVE: NO,
    REAL_MAX_BASE_CHANGE_REQUIRED: YES, and VERDICT: YES. The unique
    surviving comparison must extend scalars to \(\mathbb R_{\max}\)
    or pass through analytic completion before restricting to \(C_p\).
164. 107_236_BIVARIATE_LEGENDRE_BASE_CHANGE_COMPARISON.md and
    107_236_bivariate_legendre_base_change_comparison.py execute that
    surviving scalar extension in the correct characteristic-one
    category. They tensorize the published Legendre identification
    \(H_{\max}\widehat\otimes_{\mathbb B}\mathbb R_{\max}
    \simeq\mathcal R(H)\) and prove that functional reduction of
    \(\mathcal R(H)\otimes_{\mathbb R_{\max}}\mathcal R(K)\) is the
    semiring of finite maxima \(hx+ky+c\). The construction sheafifies
    on the product Scaling topos, is Frobenius-covariant, and identifies
    its external divisor module with the modules of 107_232--107_233.
    It returns PERIODIC_EXTERNAL_H0_COMPARISON: ISOMORPHIC,
    SCALING_SQUARE_EXTERNAL_H0: CONSTRUCTED, and VERDICT: YES. This
    closes the external \(H^0\) package, not intrinsically mixed
    correspondence divisors, \(H^1\), or square RR.
165. 107_237_CONTINUOUS_CORRESPONDENCE_DIVISOR_DC_COMPLETION.md and
    107_237_continuous_correspondence_divisor_dc_completion.py close
    existence of the intrinsically mixed divisor in a necessary
    completion. The ray \(y=\lambda x\) has potential
    \(P_\lambda=\max(y-\lambda x,0)\), and
    \(U_f=\int f(\lambda)P_\lambda d^*\lambda\) is a homogeneous DC
    potential with angular curvature \(u_f''(r)=f(r)/r\). This proves
    that non-atomic \(f\) cannot produce a finite-PL Cartier divisor,
    while its distributional divisor is exactly the continuous
    superposition of Frobenius rays. The two source moments are exactly
    its ruling degrees and force compact angular support. The map is
    injective and Frobenius-covariant. It returns
    FINITE_PL_CARTIER_REPRESENTATION: NO,
    DC_CORRESPONDENCE_CURRENT: CONSTRUCTED, and VERDICT: YES.
    The potentials are chart-local equations, not a proved global
    rational function or invertible module; global line-bundle descent,
    intersection, diagonal renormalization, and RR remain open.
166. 107_238_LOCAL_DC_INTERSECTION_VANISHING_THEOREM.md and
    107_238_local_dc_intersection_vanishing.py determine the local
    intersection completely. Every homogeneous potential
    \(U=xu(y/x)\) has rank-one Hessian, and the Hessians of any two such
    potentials are pointwise proportional. Their mixed determinant and
    ordinary local Monge--Ampere intersection vanish. Distinct
    Frobenius rays meet only at the excluded corner \((0,0)\). Hence no
    nonzero Weil pairing can come from an interior local Hessian
    integral; it must be a global corner/diagonal renormalization. It
    returns LOCAL_MIXED_MONGE_AMPERE: ZERO,
    GLOBAL_DIAGONAL_RENORMALIZATION_REQUIRED: YES, and VERDICT: YES.
167. 107_239_RENORMALIZED_CORNER_TRACE_PAIRING.md and
    107_239_renormalized_corner_trace_pairing.py construct the forced
    nonlocal numerical pairing without defining it by the explicit
    formula. For \(h=f\star\widetilde g\), they use the geometrically
    fixed semilocal representation, phase-space cutoff
    \(R_\Lambda=\widehat P_\Lambda P_\Lambda\), and subtraction of the
    generic regular term \(2h(1)\log\Lambda\). The published semilocal
    trace theorem identifies the finite limit with the Tate-normalized
    local fixed-point terms, and the global identity gives
    \(I_\partial(D_f,D_g)=N(f\star\widetilde g)\). Compact support makes
    the place set stabilize. It returns DC_CORNER_PAIRING: CONSTRUCTED,
    PAIRING_VALUE: WEIL_N, and VERDICT: YES. This is not yet a pairing
    on DC Picard classes: nonprincipal line-bundle descent, principal
    invariance, and RR intersection axioms remain open.
168. 107_240_SCALAR_PICARD_DESCENT_NO_GO.md and
    107_240_scalar_picard_descent_no_go.py close that rank-one descent
    branch. The exact pullback law is
    \(T_{m,n}^*U_f=nU_{f(n\,\cdot/m)}\). Literal scalar descent fails
    already for \(m=n=2\); degree-normalized descent would make \(f\)
    invariant under the dense, unbounded \(\mathbb Q_+^\times\)-orbit,
    which is incompatible with nonzero compact support. Finite-PL
    transitions cannot repair a continuous curvature discrepancy. It
    returns SCALAR_DC_PICARD_DESCENT: CLOSED_NO_GO,
    ROW_D_CLASSICAL_HODGE_APPLICABLE: NO, and VERDICT: YES. The
    completed object is a correspondence representation, not a scalar
    divisor class.
What is now available:

1. regular proper models over the full arithmetic base;
2. two rulings and diagonal;
3. faithful Abel--Jacobi/Picard target;
4. exact kernel target \(\ker=\mathfrak R_W\).
5. a first explicit incidence-closure construction protocol for
   \(\mathcal X_T^{(1)}\).
6. a first explicit compactification/boundary protocol for the
   Gamma--polar descent.
7. a first local finite-type test for graph closures.
8. an effective finite-level model for the framing coordinate.
9. a first explicit comparison target between packetwise Part III
   geometry and the determinant lines of Part I.
10. a local algebraic construction proving that rooted packet labels
    contribute only norm-one unit factors off the diagonal.
11. an exact finite audit of that local packet algebra, verifying for
    all visible labels with \(n\le 12\) that the packet norm equals the
    cyclotomic resultant norm and that the diagonal still vanishes.
12. an exact finite audit of the rooted descent cocycle behind the
    `107_21` gluing protocol, verifying route-independent descent on all
    visible packet labels with \(n\le 12\).
13. an exact finite audit that the same visible cocycle defines a
    representative-independent quotient line object stable under gauge
    re-trivialization.
14. a globalization protocol that glues those local packet lines on the
    candidate compactified model and identifies the boundary completion
    receiver.
15. a first concrete candidate object for the realized metrized Picard
    class required by `107_11`.
16. an exact finite audit of the logarithmic chart template behind
    `107_23`, verifying stability under atlas transitions and additive
    normal-crossings singular bookkeeping.
17. an exact finite audit that the visible chart/root presentations of
    `107_23` define one intrinsic normal-crossings integrability
    profile with no hidden fourth singular direction.
18. an exact finite audit of the primitive degree-zero bookkeeping
    behind `107_24`, verifying the uniqueness of the linear correction
    and the correction-channel logic of the denominator package.
19. a finite chartwise criterion reducing the adelic integrability audit
    to explicit visible singularity checks.
20. a finite reduction of the degree-zero audit to generator-vs-
    polarization intersection data.
21. an exact finite audit of the correction-sum bookkeeping behind
    `107_25`--`107_27`, reducing the remaining denominator issue to the
    real signed values of the exceptional corrections.
22. a first geometric decomposition of the polarization denominator and
    of the diagonal/graph degrees into corner and exceptional parts.
23. a finite exceptional-locus control criterion for preserving the
    corner contribution in the polarization denominator.
24. an explicit local-center audit excluding structural corner collapse
    in the present atlas.
25. an explicit A1 boundary audit separating candidate-model support
    from a real regular-properness closure for Route A.
26. an explicit finite A4 shadow audit for preservation of local
    log-effectivity under the visible polarization-active blow-ups.
27. an explicit finite A2 shadow audit for visible remainder-channel
    coherence under descent, overlaps, and finite action.
28. an explicit finite target-side degree-zero/covariance shadow behind
    the `107_11` realization target.
29. an explicit finite A5 target-pairing assembly shadow with the
    unresolved placeholder confined to the genuine diagonal square.
30. an explicit finite A2/A4 metric-discipline shadow with one
    singular profile, one remainder channel, and one nonnegative local
    support package.
31. an explicit finite terminal-identity shadow on the primitive
    quotient modulo the explicit radical.
32. an explicit finite packaging shadow for the candidate realized
    object of `107_22`.
33. an explicit finite intrinsic-class shadow for the candidate adelic
    object of `107_22`.
34. an explicit finite packet-to-cyclotomic bridge shadow for `107_19`.
35. an explicit finite visible framing-coordinate shadow for `107_18`.
36. an explicit finite local-atlas and finite-type shadow for `107_17`.
37. an explicit finite common-corner receiver shadow for `107_16`.
38. an explicit finite candidate-model incidence shadow for `107_15`.
39. an explicit finite candidate-envelope coherence shadow spanning
    the visible `107_15`--`107_17` package.
40. an explicit finite assembled candidate-target shadow combining one
    envelope, one receiver channel, one degree-zero realization, and
    one metric profile on the same cover.
41. an explicit finite assembled Route A applicability shadow joining
    A1--A6 on one candidate target state.
42. an explicit finite structural-exclusion shadow for the wrong
    universal-model simplifications around `107_10`.
43. an explicit finite assembled realization shadow tying the full-base,
    degree-one, two-ruling, discrete candidate architecture of
    `107_10` to one coherent target-side realization state.
44. an explicit finite point-spectrum retention shadow tying the
    intrinsic single-receiver candidate package of `107_11` to visible
    discrete point/resonance classes modulo the explicit radical.
45. an explicit finite target-side divisor-sensitivity shadow tying the
    intrinsic candidate package of `107_11` to genuine moved-divisor
    visibility modulo the explicit radical.
46. an explicit assembled archimedean load-bearing shadow tying the
    intrinsic candidate package of `107_22` and the retention shadows of
    `107_11` to genuinely separating Green-side data.
47. an explicit real local arithmetic witness that actual bad fibers of
    selected elliptic curves over \(\mathbf Q\) carry affine-Dynkin
    intersection matrices with the standard finite-place Arakelov
    weight \(\log p\).
48. an explicit real local comparison showing that repeated real
    Kodaira types have the same underlying intersection matrix and
    differ only by the standard target-side \(\log p\) factor.
49. an explicit real local boundary witness showing that the current
    source-side row of `107_04` matches the scalar \(\log p\) layer but
    not yet the target-side fiber geometry.
50. an explicit real local boundary witness showing that even the target
    affine-fiber geometry does not by itself exhaust the local
    arithmetic datum, as seen by Tamagawa behavior on real fibers.
51. an explicit real local synthesis witness locating the current source
    row strictly below real fiber geometry and the latter strictly below
    the fuller local arithmetic target datum.
52. an explicit real local witness showing that even matching prime,
    Kodaira type, affine matrix, and \(c_p\) still does not determine
    the full local reduction datum.
53. an explicit real local hierarchy witness organizing the current
    local target information layers that the Phase 107 source row still
    fails to recover.

What remains open:

1. actual construction of \(\mathcal X_T\);
2. actual realization of the source cycles on \(\mathcal X_T\);
3. proof that the target metric is admissible/integrable;
4. identification of the descended packet line with a genuine Deligne
   pairing or adelic analogue;
5. proof of exact kernel identity.

Residual note:
`107_20` is now exact-audited only at the local finite algebra level.
The new `107_42` verifier confirms that rooted labels behave as
rank-one norm-one packet factors and do not alter the cyclotomic
resultant norm off the diagonal, across all visible labels in the
window \(n\le 12\).  But that does not yet audit the globalization step
of `107_21`, the adelic metric candidates of `107_22`--`107_23`, or the
polarization package of `107_24`--`107_27`.  The new `107_44` verifier
now exact-audits the finite rooted descent cocycle shadow of `107_21`,
including connected packet descent groupoids, cocycle compatibility,
route-independent descended sections, and visible-action compatibility.
That still does not prove a genuine global line object on a proved
arithmetic surface.  `107_43` fixes that coverage boundary explicitly so
later forward construction cannot silently overpromote Paper C.
The new `107_72` verifier exact-audits one step more of the same visible
descent package: the cocycle quotient really behaves like a glued line
object in the finite symbolic model and is stable under visible
re-trivialization.  It still does not prove algebraicity, Deligne
pairing descent, or existence of a genuine global line object in a
proved arithmetic surface category.
The new `107_73` verifier exact-audits one step more of the visible
`107_22` realization package: chart/root presentations now determine
one intrinsic quotient-class shadow with one receiver channel only, and
extra archimedean splitting is rejected exactly in the finite model.
It still does not prove existence of a true adelic Picard class or an
actual metric descent theorem on a proved arithmetic surface.
The new `107_145` control adds one candid geometric anchor on the
target side: exact-kernel behavior modulo torsion and nondegeneracy of
the free quotient now occur on actual elliptic and genus-\(2\)
Jacobians computed in Sage.  This still does not build the Phase 107
map of `107_11`, so Paper C remains `partial`, but III-B is now tied to
genuine Jacobian behavior rather than only symbolic finite shadows.
The new `107_147` result removes the trace norm from the candidate list
for a tensorial absolute dimension on the square.  It does not construct
the missing \(H^1\), and it does not rule out every alternative mass
functional; it proves that the most direct Euclidean projective tensor
norm has the wrong asymptotic growth.
The new `107_148` result also narrows III-B: the Connes--Consani
Jacobian remains useful as geometric support for prime orbits and rooted
boundary data, but its published idempotent monoid law cannot carry the
signed source divisor group or the required height pairing.  A
non-idempotent enhancement or a classical/adelic Picard group is now
mandatory.
The new `107_149` result corrects the direct Hodge target before further
construction: the square must be a surface over \(\mathbb Q\), its
arithmetic model has relative dimension two, and the terminal pairing
has one polarization factor.  This does not build that model; it
prevents a dimension-one Hodge theorem from being applied to it.
The new `107_150` result resolves the mass-functional fork in favor
of the CC-inherited entrywise \(\ell^1\) norm.  This supplies a
Riemann--Roch-compatible growth input for constructing \(H^0\), but it
does not construct the square sheaf or the missing \(H^1\).
The new `107_151` result constructs the formal \(H^1\) operation
for any bounded abelian Cech lift.  It does not provide that lift for the
Scaling Site square, but it removes nontransitivity of the image relation
as a formal obstruction: the relation is retained rather than quotiented.
The new `107_152`--`107_153` results reject the simplest
attempt to supply the missing abelian Cech lift.  Free additive
linearization has infinite dimension, and no Frobenius-stable finite
truncation with nonconstant sections can repair it.
Likewise, the new `107_45` verifier exact-audits only the finite
chart-transition shadow of `107_23`; it does not prove the actual
analytic coefficients, the global integrability of the remainder term,
or the full published Yuan--Zhang hypotheses.
The new `107_74` verifier exact-audits one step more of the same
visible `107_23` package: the chart/root presentations now determine
one intrinsic normal-crossings profile on the visible divisor slots and
cannot hide a fourth singular direction in the finite model.  It still
does not prove the actual analytic coefficients or theorem-level
integrability on a proved arithmetic surface.
The new `107_46` verifier exact-audits only the finite symbolic shadow
of `107_24`; it does not prove the actual nonvanishing of \(h_T\) on a
constructed surface, the real numerical generator intersections, or the
transport of primitive correction into the final Picard realization.
The new `107_47` verifier exact-audits only the finite correction-sum
architecture behind `107_25`--`107_27`; it does not compute the actual
signs or magnitudes of the exceptional corrections on the real model,
and therefore it does not by itself prove \(h_T\neq0\).
The new `107_48` verifier exact-audits only the finite kernel logic
behind `107_11`; it does not construct the actual Picard/Jacobian
realization, prove pairing transport, or prove the real geometric kernel
equals \(\mathfrak R_W\) on the final target category.
The new `107_49` verifier exact-audits only the finite bilinear
comparison logic behind `107_11` and `107_13`; it does not prove the
actual generator comparison on the realized target classes, the true
Gamma--polar metric comparison, or the full terminal identity.
The new `107_78` verifier exact-audits one further finite `107_11`
shadow: primitive correction lands the visible realization in exact
target-side degree zero and finite critical scaling preserves that
status.  It still does not prove actual target-side degree zero or full
continuous scaling covariance on a realized arithmetic surface or
adelic target.
The new `107_79` verifier exact-audits one further finite A1/Part III
shadow: the visible incidence, boundary, and atlas layers really fit a
single candidate envelope with one finite center list, and collapse of
the corner/two-ruling structure is exactly detectable.  It still does
not prove regular properness or a published adelic comparison theorem.
The new `107_80` verifier exact-audits one further finite A5 shadow:
the transported target pairing stays finite on every visible
non-diagonal channel, and the unresolved placeholder remains confined
to the genuine diagonal square.  It still does not prove finiteness of
the actual completed diagonal self-pairing or target-side finiteness on
a realized arithmetic surface or adelic category.
The new `107_81` verifier exact-audits one joint A2/A4 target-side
shadow: one visible normal-crossings profile, one remainder channel,
and one nonnegative local support package coexist in the same finite
model without creating extra singular or remainder channels.  It still
does not prove actual analytic admissibility or semipositivity on a
realized arithmetic surface or adelic category.
The new `107_82` verifier exact-audits one further assembled Paper C
target-side shadow: the candidate envelope, intrinsic adelic receiver,
degree-zero realization, and metric discipline coexist on one visible
cover without forcing extra target-side channels.  It still does not
prove a genuine regular proper model, realized Picard class, or global
metric theorem.
The new `107_86` verifier exact-audits one further assembled `107_10`
shadow: the current finite-support realization package keeps the full
arithmetic base, degree-one carrier, two-ruling/discrete incidence
architecture, coherent candidate envelope, and assembled target-side
package on one finite state, while base truncation, genus-zero
collapse, ruling collapse, continuous completion, or target-free
packaging are all rejected exactly.  It still does not prove existence
of a genuine regular proper arithmetic surface or the full finite-
support realization theorem.
The new `107_87` verifier exact-audits one further finite `107_11`
shadow: visible point/resonance classes survive inside the current
intrinsic single-receiver candidate package and remain distinguishable
modulo the explicit radical shadow, while continuous completion or
channel collapse erases them exactly.  It still does not prove a
genuine Picard/Jacobian realization or point-spectrum retention on a
realized arithmetic surface or adelic target.
The new `107_89` verifier exact-audits one further finite `107_11`
shadow: visible moved divisors remain distinguishable as target-side
classes inside the current intrinsic package after primitive correction
and radical quotienting, while scalarized or location-blind target
substitutes fail exactly.  It still does not prove a genuine
Picard/Jacobian realization or divisor sensitivity on a realized
arithmetic surface or adelic target.
The new `107_90` verifier exact-audits one further assembled shadow
behind `107_22` and `107_11`: the current intrinsic finite-support
package, the retention shadows, and the Green-side separation burden fit
one exact load-bearing state, while algebraic-only storage or truncated
Green channels destroy that faithfulness shadow immediately.  It still
does not prove the actual realized Green datum or an infinite-
dimensional theorem on a realized arithmetic surface or adelic target.
The new `107_93` verifier is different in kind from the symbolic audit
layer: it checks actual bad fibers of actual elliptic curves over
\(\mathbf Q\), using local data downloaded from LMFDB and exact
affine-Dynkin intersection matrices.  It witnesses that the target-side
finite-place weight \(\log p\) is already built into the real Arakelov
normalization of those local intersections.  It still does not show
that the current Phase 107 source package reproduces that local
geometry.
The new `107_94` verifier sharpens that same local arithmetic point:
for repeated real Kodaira type \(I_2\) at different bad primes, the
underlying component-intersection matrix is unchanged and only the
target-side scalar \(\log p\) varies.  This isolates, on real objects,
the distinction between fiber geometry and finite-place normalization.
The new `107_95` verifier pushes one step further: it compares that real
target-side local picture with the current source-side finite row of
`107_04`, and shows that the present source law reproduces only the
scalar \(\log p\) normalization, not yet the local fiber geometry.
The new `107_96` verifier sharpens the local target boundary itself:
even after one reaches real affine-Dynkin fiber geometry, one still has
not exhausted the local arithmetic datum, since the real Tamagawa
behavior can diverge from the raw component cofactor.
The new `107_97` verifier packages these local real boundaries into one
comparison chain: the current source row of `107_04` captures only the
scalar prime-weight layer, the real fiber geometry adds Kodaira-type
structure, and the full local target datum can still distinguish more.
The new `107_98` verifier sharpens that local conclusion one step
further: even two real fibers with the same prime, the same \(I_2\)
geometry, and the same \(c_p\) can still differ by split versus
nonsplit multiplicative reduction.
The new `107_99` verifier packages these local distinctions into one
exact hierarchy of information, making the current local comparison
problem reusable as structured evidence instead of as separate examples.
The new `107_83` verifier exact-audits one assembled Route A shadow:
the candidate envelope, degree-zero realization, metric discipline,
target-pairing finiteness, and visible functoriality coexist in one
finite target state, while removing any one A1--A6 ingredient makes the
assembled applicability shadow fail immediately.  It still does not
prove theorem-level Route A applicability on a realized target.
The new `107_85` verifier exact-audits one further phase-level chain
shadow: the assembled Paper C target state, the assembled Route A
applicability state, and the assembled E1 bridge state now fit together
as one end-to-end finite pregeometric chain, and any attempt to bypass
the candidate target assembly is exactly rejected.  It still does not
prove a realized arithmetic surface, realized target category, or the
geometric terminal identity.
The new `107_51` verifier exact-audits only the finite functoriality
shadow behind A6 of `107_12`; it does not prove the real target-side
pullback/pushforward theorem or the full continuous scaling covariance
of the realized map.
The new `107_52` verifier exact-audits only the finite A5 shadow behind
`107_12`; it does not prove finiteness of the actual completed diagonal
self-pairing or finiteness of the realized target pairing on a true
arithmetic surface or adelic category.  The new `107_53` audit isolates
the remaining A1 boundary explicitly: the current Part III package gives
candidate-model structure and excludes obvious wrong envelopes, but it
still does not prove regular properness or exact adelic comparison on
the target side.  The new `107_54` verifier exact-audits only the
finite local A4 shadow behind `107_12`; it does not prove the actual
archimedean curvature is semipositive, nor theorem-level admissibility
of the realized metric in a published Yuan--Zhang category.  The new
`107_55` verifier exact-audits only the finite visible A2 remainder
shadow behind `107_12`; it does not prove global analytic continuity or
theorem-level integrability of the true archimedean remainder term.  The
new `107_56` verifier exact-audits only the finite primitive-quotient
shadow behind `107_13`; it does not prove the actual geometric terminal
identity on a realized arithmetic surface or adelic category.  The new
`107_57` verifier exact-audits only the finite packaging shadow behind
`107_22`; it does not prove existence of the true adelic Picard class
or the completed target pairing.  The new `107_58` verifier exact-
audits only the finite visible bridge shadow behind `107_19`; it does
not construct the true packet intersection line or the global
comparison morphism on a realized model.  The new `107_59` verifier
exact-audits only the finite visible-coordinate shadow behind `107_18`;
it does not prove global chart gluing or proper compactification of the
full framed-divisor space.  The new `107_60` verifier exact-audits only
the finite local-atlas shadow behind `107_17`; it does not prove the
full algebraic gluing or global compactification theorem.  The new
`107_61` verifier exact-audits only the finite common-corner shadow
behind `107_16`; it does not prove the full compactification or metric
descent theorem.  The new `107_62` verifier exact-audits only the
finite visible incidence shadow behind `107_15`; it does not prove the
actual regular proper model or the correctness of the global blow-up
construction.  The new `107_63` verifier exact-audits only the finite
structural-exclusion shadow behind `107_10`; it does not prove
existence of a universal finite model or a regular proper arithmetic
surface over the full base.

### Paper E1 — Classical/adelic Hodge bridge

Status: `partial`

Evidence:

1. `107_12` fixes the applicability audit.
2. `107_13` fixes the terminal identity and RH closure logic.
3. `107_50_PAPER_D_ROUTE_A_APPLICABILITY_COVERAGE_MATRIX.md` records
   explicitly which Route A items A1--A6 now have exact finite shadows
   and which remain only theorem-level hypotheses on the target side.
4. `107_51` exact-audits the finite functoriality shadow behind A6,
   upgrading that Route A item from mere structural support to a real
   exact finite witness.
5. `107_52` exact-audits the finite A5 shadow behind the target
   finiteness checklist, sharpening the claim that the remaining risk is
   isolated to the diagonal completion sector.
6. `107_53` boundary-audits A1 directly, fixing the claim that the
   present candidate-model package is structurally meaningful but still
   not a proved regular proper model theorem.
7. `107_54` exact-audits a finite local A4 shadow, upgrading that Route
   A item from mere structural support to a real exact witness for the
   visible log-effectivity pattern preserved by the current blow-up
   protocol.
8. `107_55` exact-audits a second finite A2 shadow, sharpening the
   candidate metric story from a logarithmic singular template alone to
   a route-independent visible remainder channel on the packet/chart
   cover.
9. `107_56` exact-audits a finite `107_13` shadow directly on the
   primitive quotient, sharpening the terminal identity from bilinear
   transport alone to quadratic equality with the correct radical
   equality case in one visible model.
10. `107_71_PAPER_E1_AUDIT_COVERAGE_MATRIX.md` records explicitly which
    parts of `107_12`--`107_13` now have exact finite shadows and which
    remain theorem-level on the realized target side.
11. `107_77_PAPER_E1_CLOSURE_READINESS_AUDIT.md` and
    `107_77_paper_e1_closure_readiness_audit.py` provide an exact audit
    of one finite E1 closure gate: RH closure is allowed only when one
    Hodge route is genuinely applicable, the terminal identity is exact,
    and the equality case is exact, with the current phase state
    certified as still pre-closure.
12. `107_84_PAPER_E1_ASSEMBLED_BRIDGE_AUDIT.md` and
    `107_84_paper_e1_assembled_bridge_audit.py` provide an exact audit
    of one assembled E1 bridge state: assembled Route A applicability,
    primitive-quotient terminal identity, exact equality case, and RH
    closure readiness coexist in one finite bridge shadow, while
    removing any one ingredient breaks the bridge immediately.
13. `107_91_PAPER_D_ASSEMBLED_HODGE_PREAPPLICABILITY_AUDIT.md` and
    `107_91_paper_d_assembled_hodge_preapplicability_audit.py` provide
    an exact audit of one assembled IV-A governance shadow: the current
    finite assembled Route A state remains pre-applicable rather than
    genuinely applicable, and hybrid or promotion-by-assembly states
    fail exactly.
13. `107_85_PHASE_LEVEL_PREGEOMETRIC_CHAIN_AUDIT.md` and
    `107_85_phase_level_pregeometric_chain_audit.py` provide an exact
    audit of one end-to-end phase-level chain state: assembled
    candidate target, assembled Route A applicability, primitive-
    quotient terminal identity, exact equality case, and RH closure
    logic coexist on one finite pregeometric chain, while bypassing any
    load-bearing layer makes the chain fail immediately.

What is now available:

1. line-by-line applicability checklist for Faltings--Hriljac /
   Yuan--Zhang;
2. exact identity
   \(-\widehat{\deg}(\overline M_f^{\,2})=\mathcal Q_W(f)\);
3. equality-case transfer to \(\mathfrak R_W\);
4. formal deduction of Weil positivity and RH once the identity is
   proved.
5. an explicit coverage boundary for Route A:
   A2 and A3 are now backed by exact finite shadows,
   A4, A5, and A6 now also have exact finite shadows,
   and A1 is now boundary/exclusion-audited at the finite shadow level
   even though no regular proper model theorem is proved yet.
6. an explicit E1 coverage boundary separating exact finite shadows of
   applicability and terminal-identity logic from the still-unproved
   realized Hodge bridge.
7. an explicit finite closure-readiness gate requiring applicability,
   terminal identity, and exact kernel simultaneously before RH
   closure is allowed.
8. an explicit finite assembled E1 bridge shadow joining applicability,
   terminal identity, exact kernel, and closure logic on one bridge
   state.
9. an explicit finite end-to-end pregeometric chain shadow joining the
   assembled candidate target, assembled Route A applicability,
   terminal identity, exact kernel, and closure logic on one phase
   state.

What remains open:

1. proof of applicability on actual realized Phase 107 objects;
2. proof of the terminal identity itself.
3. proof that the published target-side hypotheses A1--A6 hold in one
   actual classical or adelic category, not merely in finite shadows.
4. proof that the closure-readiness gate is realized geometrically, not
   only in a finite symbolic model.
5. proof that the assembled E1 bridge is realized geometrically, not
   only in a finite symbolic model.
6. proof that the end-to-end pregeometric chain is realized
   geometrically, not only as one finite symbolic phase state.

### Paper E2 — Absolute Hodge index

Status: `open`

Evidence:

1. `107_12` names it as the only admissible alternative if E1 fails.

No current Phase 107 document proves:

1. a primitive decomposition in a new absolute category;
2. a Hodge--Rosati index theorem there;
3. compatibility of that theorem with the Phase 107 Lefschetz
   intersection package.

## 4. Mandatory falsifier audit

This section checks the ten mandatory falsifiers of `107_00` §19 against
the current workspace state.

### F1. Function-field positive control

Status: `proved`

Evidence:

1. `107_01`, `107_02`, and `107_01_function_field_preflight.py` prove
   the fixed elliptic control.
2. `107_28` adds a separate exact genus-2 diagonal-sensitivity audit.

Residual note:
The elliptic control is proved as stated, but genus-sensitive
portability of the primitive diagonal formulas is now tracked
explicitly as a separate auxiliary falsifier rather than being silently
inherited from the \(g=1\) case.

### F2. Zero-free source audit

Status: `partial`

Evidence:

1. `107_03`--`107_09` define the source constructions using only primes,
   Gamma, pole, correspondences, and determinant data.
2. `107_09` explicitly postpones the zero-side comparison until after
   the arithmetic side is derived.
3. `107_36` exact-audits the function-field same-tower return/Lefschetz
   shadow without importing any zero-side spectral input.
4. `107_66_ZERO_FREE_SOURCE_AUDIT.md` and
   `107_66_zero_free_source_audit.py` exact-audit the finite zero-free
   source shadow: the visible arithmetic observables are source-defined,
   ignore ambient spectral channels, and detect any tampered
   constructor that reads them.

Residual note:
The later RH closure of `107_13` of course invokes Weil's criterion, but
the constructions before that stage are source-defined.  The audit is
now pressure-tested in a finite symbolic shadow, but it still lives
inside the presently formalized Paper A/B source package rather than an
independently closed geometric foundation.

### F3. Davenport--Heilbronn audit

Status: `proved` at the arithmetic falsifier level, `formalized` at the full geometric packaging level

Evidence:

1. `107_03` stop tests separate Eulerian orbit structure from raw sums.
2. `107_07` and `107_08` require primitive closed-orbit towers and
   common-phase gluing.
3. `107_09` states explicitly that Davenport--Heilbronn fails before any
   zero comparison.
4. `107_40` gives an exact external arithmetic witness: the normalized
   Davenport--Heilbronn coefficients are not multiplicative, so there is
   no Euler product and no unchanged primitive return tower.

### F4. Diagonal coherence

Status: `partial`

Evidence:

1. `107_04` preserves the diagonal as an excess-intersection line.
2. `107_05` closes the diagonal with the same Gamma--polar metric used
   for cross terms.
3. `107_06` packages both into one coherent theorem.
4. `107_34` exact-audits the finite diagonal warning
   \(\mathrm{Res}(\Phi_n,\Phi_n)=0\) in a nontrivial finite
   window.
5. `107_64` exact-audits the finite diagonal-coherence shadow:
   matched-cutoff stabilization, one common Green functional for cross
   and diagonal pairings, exact polarization, and failure of
   diagonal-only renormalization shifts.

Gap:
Diagonal coherence is now pressure-tested at the finite shadow level,
but the full analytic Green metric theorem is not yet proved on the
realized target.

### F5. Divisor sensitivity

Status: `proved` at the source level, `formalized` at the target level

Evidence:

1. `107_05` includes the scalar moving-divisor stop test and its failure
   mode.
2. `107_03`--`107_06` retain divisor positions in the source package.
3. `107_11` demands exact faithfulness in the target.
4. `107_89` exact-audits one target-side sensitivity shadow behind
   `107_11`: nontrivial moved-divisor classes remain distinguishable in
   the current intrinsic candidate package modulo the explicit radical,
   while scalarized/location-blind substitutes fail.

Gap:
Target-level divisor sensitivity is now pressure-tested in one finite
candidate shadow, but it still remains to be realized and proved
geometrically together with III-B.

### F6. Finite-support realization

Status: `partial`

Evidence:

1. `107_10` states the requirement that every compactly supported test
   lives on one proper model \(\mathcal X_T\).
2. `107_15` provides a first explicit candidate family
   \(\mathcal X_T^{(1)}\) built from finite-support incidence loci.
3. `107_16` provides the boundary/corner compactification data that the
   candidate family needs in order to formulate metric descent.
4. `107_17` reduces chartwise finite-typeness to explicit conditions on
   the local framing coordinate, scale coordinate, and common phase.
5. `107_18` identifies the local framing coordinate with finite visible
   rooted/cyclotomic packets.
6. `107_19` identifies the next comparison theorem target between those
   packets and the determinant-line package of `107_04`.
7. `107_63` exact-audits the finite structural exclusions behind
   `107_10`: base truncation, genus-zero envelopes, ruling collapse,
   and absolutely continuous completions all fail in explicit ways.
8. `107_86` exact-audits one assembled finite-support realization
   shadow behind `107_10`: the full-base, degree-one, two-ruling,
   discrete candidate architecture coexists with the coherent envelope
   and assembled target-side package in one finite state.
9. `107_93` provides a real local arithmetic witness on actual elliptic
   curves over \(\mathbf Q\): selected bad fibers already realize
   standard affine-Dynkin intersection matrices with the finite-place
   Arakelov weight \(\log p\).
10. `107_94` provides a sharper real local comparison: repeated real
    Kodaira type \(I_2\) at different bad primes carries the same
    unweighted intersection matrix, and only the target-side factor
    \(\log p\) changes.
11. `107_95` provides the first real local source-vs-target comparison:
    the current source-side local row of `107_04` matches the scalar
    \(\log p\) layer but does not yet distinguish different real
    Kodaira geometries at the same prime.
12. `107_96` provides a second real local boundary: even the affine
    target-side geometry of a real bad fiber does not by itself recover
    all local arithmetic data, as shown by the contrast with real
    Tamagawa behavior.
13. `107_97` packages the current local comparison chain: the source row
    of `107_04` captures only the scalar \(\log p\) layer, real fiber
    geometry carries more, and the full local arithmetic datum carries
    more again.
14. `107_98` provides a still finer real local boundary: even after
    fixing the prime, Kodaira type, affine matrix, and \(c_p\), actual
    bad-reduction data can still differ by split versus nonsplit
    multiplicative behavior.
15. `107_99` packages the current real local information hierarchy:
    source scalar weight is coarser than fiber geometry, \(c_p\) is an
    intermediate local arithmetic invariant, and split/nonsplit
    reduction can still distinguish more.
16. `107_100` sharpens the multiplicative part of that hierarchy:
    between affine geometry and the arithmetic number \(c_p\), the
    missing mechanism is Frobenius action on the geometric component
    group \(\mathbf Z/n\mathbf Z\).
17. `107_101` shows that this is not only multiplicative: in a real
    additive \(IV\) pair, the same geometry-to-\(c_p\) refinement is
    again controlled by Frobenius action on geometric component data.
18. `107_102` shows the complementary rigid behavior: for the pinned
    real additive \(III\) examples, the geometric component group is
    already rigid enough to force the observed value \(c_p=2\).
19. `107_103` packages those local sectors into one typed atlas:
    flexibility already in \(c_p\), rigidity in \(c_p\) but not in the
    full datum, and rigidity at both visible levels now appear as exact
    separate regimes on real fibers.
20. `107_104` turns that target-side atlas back against the current
    source row of `107_04`: at the present stage, the finite-place
    source package still discriminates only by prime, not by local
    Kodaira regime, \(c_p\), or finer reduction label.
21. `107_105` then packages the minimal refinement ladder visible from
    those same real rows: prime only, prime plus Kodaira type, prime
    plus Kodaira type plus \(c_p\), and finally the finer reduction
    label.
22. `107_106` then records the exact residual ambiguity at each of
    those levels, identifying which concrete local collisions still
    survive before the next refinement.
23. `107_107` then turns those residual patterns into explicit
    necessary tests for future local source upgrades.
24. `107_108` then shows that these are not only policy gates but
    actual obstructions: the present \(S_0\)-factor row cannot support
    a faithful realization of the pinned real local target atlas.
25. `107_109` extends that to a full local no-go ladder across the
    minimal refinement levels \(S_0,S_1,S_2\).
26. `107_110` shows that these local obstructions persist even after
    passing to a coarse finite global profile of actual curves.
27. `107_111` shows that the obstruction persists even in the more
    faithful finite-source language of global bad-prime \(\log p\)
    packets.
28. `107_112` then makes that global obstruction normative for future
    finite source upgrades.
29. `107_113` then synthesizes the local and global finite-source
    boundary into one unified insufficiency gate.
30. `107_114` then packages that unified insufficiency together with the
    already exact-audited finite symbolic successes of Paper A into one
    Milestone I boundary audit.
31. `107_115` does the analogous synthesis for Paper B.
32. `107_116` then packages Milestones I and II together into one
    source-side finite boundary audit.

Gap:
No candidate family has yet been proved to satisfy the full realization
theorem.  The new `107_86` verifier exact-audits one assembled
finite-support realization shadow tying the current candidate-model and
target-side layers together, but it remains only a finite symbolic
state, not a proved arithmetic surface theorem.  The new `107_93`
witness reaches genuine local arithmetic fibers, but it still does not
construct the global Phase 107 realization or compare the source
package directly to those real local targets.  The new `107_94` witness
sharply separates real local geometry from the standard \(\log p\)
weight, but still does not determine whether the current source row has
any arithmetic content beyond that normalization.  The new `107_95`
witness makes that boundary explicit for the current row of `107_04`:
as presently formalized, it captures the scalar finite-place weight but
not yet the real local fiber geometry.  The new `107_96` witness then
shows that even that real local fiber geometry is still only part of the
full local target datum.  The new `107_97` witness packages the whole
strict comparison chain in one exact local statement.  The new
`107_98` witness then shows that even prime + geometry + \(c_p\) does
not yet exhaust the full local reduction datum.  The new `107_99`
witness organizes that whole strict hierarchy in one exact local
statement.  The new `107_100` witness then identifies, for the
multiplicative examples already pinned in the workspace, the exact
arithmetic mechanism behind the geometry-to-\(c_p\) gap: Frobenius acts
on the geometric component group and its fixed subgroup has size
\(c_p\).  The new `107_101` witness shows that the same mechanism
already appears in one additive Kodaira sector as well: two real
\(IV\)-fibers share the same affine \(A_2\) geometry while Frobenius
action distinguishes the cases \(c_p=1\) and \(c_p=3\).
The new `107_102` witness then records the complementary rigid additive
sector: two real \(III\)-fibers again share the same affine geometry,
but here the geometric component group already forces the observed
value \(c_p=2\), so no further local ambiguity appears in this pinned
pair.  The new `107_103` witness then packages the whole current local
picture into one exact atlas, separating \(c_p\)-flexible,
\(c_p\)-rigid-but-label-flexible, and fully rigid sectors.
The new `107_104` witness then compares that typed target atlas to the
current Paper A source row itself, making the present local blindness
exact: several distinct real local target states still collapse to the
single source scalar class \(\log p\) at fixed prime.
The new `107_105` witness then turns that blindness statement into a
minimal refinement ladder, quantifying exactly what each extra layer of
local source information would recover on the current real atlas.
The new `107_106` witness then records the residual ambiguity matrix
behind that ladder, so the current local source gap is now explicit
both numerically and collision by collision.
The new `107_107` witness then makes that hierarchy normative: stronger
future Paper A local claims must pass exact separation gates on the
pinned real atlas before they can be credited.
The new `107_108` witness then upgrades the current local blindness to a
genuine no-go for any still-\(S_0\)-factored local realization on those
same real target states.
The new `107_109` witness then extends that to the whole minimal source
refinement ladder, identifying \(S_3\) as the first visible escape
point from the local no-go on the pinned atlas.
The new `107_110` witness then lifts the same issue to a finite global
obstruction: even the whole bad-prime support profile of an actual
curve remains too coarse to recover the pinned real local atlas.
The new `107_111` witness then sharpens that statement to the present
finite-place source language itself: even the full bad-prime
\(\log p\)-packet remains too coarse to recover the pinned real local
atlas.
The new `107_112` witness then turns that finite global obstruction
into an exact necessity gate for future source upgrades.
The new `107_113` witness then packages the whole currently verified
finite-source boundary into one unified insufficiency gate.
The new `107_114` witness then turns that into an explicit Paper A
boundary statement: exact finite symbolic pairing yes, faithful
target-side local/global recovery not yet.
The new `107_115` witness then turns the current Part II audit state
into the corresponding Paper B boundary statement: exact finite
fixed-point/source shadow yes, full suspended geometric production not
yet.
The new `107_116` witness then combines those two milestone boundaries
into one exact source-side boundary statement for the phase.

### F7. Point-spectrum retention

Status: `partial`

Evidence:

1. `107_10`, `107_11`, and `107_12` explicitly exclude absolutely
   continuous completions that erase resonant divisor classes.
2. `107_63` exact-audits the finite structural-exclusion shadow behind
   that requirement: absolutely continuous completion erases the
   point/resonance classes needed for graph and Euler packaging.
3. `107_87` exact-audits one assembled retention shadow behind
   `107_11`: the current intrinsic candidate package keeps visible
   point/resonance classes as discrete target-side data modulo the
   explicit radical shadow, while continuous completion or channel
   collapse destroys that visibility.

Gap:
Retention is now pressure-tested at the finite exclusion-shadow level,
and at one finite intrinsic candidate-retention shadow, but not yet
realized or proved on a concrete target.

### F8. No prescribed trace

Status: `partial`

Evidence:

1. `107_09` derives the arithmetic side from fixed-point sectors and
   explicitly rejects definitional installation of the explicit formula.
2. `107_65` exact-audits the finite no-prescribed-trace shadow:
   diagonal renormalization cleans only the identity channel, the
   visible boundary page couples Gamma and pole, and the renormalized
   source-to-trace map has trivial kernel in one symbolic visible
   window.
3. `107_76` exact-audits one finite joint fixed-point assembly shadow:
   prime, Gamma, pole, and mixed sectors coexist in one renormalized
   source package without mixed collapse into the primitive prime page.
4. `107_88` exact-audits one assembled no-prescribed-trace shadow:
   that whole renormalized visible page remains source-determined and
   rejects external retouching as an exact failure.

Gap:
The no-prescribed-trace rule is now pressure-tested in a finite shadow,
in one finite joint assembly shadow, and in one finite assembled source-
determined-page shadow, but the full one-step geometric fixed-point
production of `107_09` remains unproved.

### F9. Hodge-category audit

Status: `partial`

Evidence:

1. `107_12` states the exact applicability audit for the classical/adelic
   branch and the alternative new-theorem branch.
2. `107_50` records explicitly which Route A items A1--A6 now have
   exact finite shadows and which remain unsupported on the target side.
3. `107_67_HODGE_ROUTE_EXCLUSIVITY_AUDIT.md` and
   `107_67_hodge_route_exclusivity_audit.py` exact-audit the route
   exclusivity shadow of IV-A: Route A and Route B are mutually
   exclusive, hybrid analogy imports fail exactly, and the present phase
   state is certified as still pre-applicability.
4. `107_91` exact-audits one assembled IV-A pre-applicability shadow:
   the current finite assembled Route A state is certified as still
   pre-applicable because theorem-level A1--A6 gaps remain open, and
   finite assembly alone cannot promote applicability.

Gap:
The audit is now pressure-tested at the route-logic level and at one
assembled pre-applicability shadow, but its target-side hypotheses are
not yet verified on a completed realization.

### F10. Equality-case audit

Status: `partial`

Evidence:

1. `107_11` states the exact kernel target.
2. `107_12` requires equality-case verification before applying Hodge.
3. `107_13` propagates equality cases through the terminal identity.
4. `107_48` exact-audits the finite kernel shadow required by that
   equality-case logic.
5. `107_56` exact-audits the primitive-quotient quadratic equality case
   behind `107_13`.
6. `107_68_EQUALITY_CASE_EXACTNESS_AUDIT.md` and
   `107_68_equality_case_exactness_audit.py` exact-audit the sharp
   exactness shadow: larger kernels than \(\mathfrak R_W\) are rejected
   explicitly, not merely left unattributed.
7. `107_92_ASSEMBLED_EQUALITY_CASE_GATE_AUDIT.md` and
   `107_92_assembled_equality_case_gate_audit.py` exact-audit one
   assembled equality-case shadow: kernel minimality, non-radical
   survival, primitive-quotient identity, and rejection of enlarged
   kernels coexist as one exact gate.

Gap:
No current Phase 107 construction yet proves
\(\ker(f\mapsto\overline M_f)=\mathfrak R_W\) geometrically on the final
target.  The equality-case gate is now pressure-tested both at the
kernel-shadow level, at the primitive-quotient exactness level, and as
one assembled finite gate, but not yet proved by the realization
theorem itself.

## 5. Infinite-dimensional load-bearing audit

`107_00` §20 predicts that most infinite-dimensional variation must live
in the archimedean Green datum rather than in algebraic divisor classes.

Current status: `partial`

Evidence:

1. `107_05` places the archimedean Gamma--polar metric at the center of
   the diagonal closure.
2. `107_10` records that finite-rank algebraic divisor classes cannot by
   themselves store the full test-space variation.
3. `107_11` requires the realized Picard/Jacobian map to preserve the
   source metric and remain faithful modulo \(\mathfrak R_W\).
4. `107_69_ARCHIMEDEAN_LOAD_BEARING_AUDIT.md` and
   `107_69_archimedean_load_bearing_audit.py` exact-audit the finite
   load-bearing shadow: fixed finite-rank algebraic storage produces
   non-radical collisions, full Green channels separate them, and fixed
   finite-rank Green truncations collide again.
5. `107_90` exact-audits one assembled load-bearing shadow: the current
   intrinsic finite-support candidate package and the current retention
   shadows remain faithful only while the Green side keeps enough
   separating channels.

Gap:
No current Phase 107 document yet proves that the realized Green
component indeed carries the required infinite-dimensional faithfulness.
The new `107_90` verifier exact-audits one assembled finite shadow
showing that the current intrinsic candidate package depends on that
separating Green burden, but it remains only a finite symbolic gate.

## 6. Current closure state of the phase

As of Saturday, August 1, 2026, the current state is:

1. Part 0 is closed at the fixed positive control.
2. Part I is closed at the source determinant/intersection level.
3. Part II is closed at the source correspondence/Lefschetz level.
4. Part III has moved from purely formalized to partially instantiated:
   a first concrete candidate \(\mathcal X_T^{(1)}\) now exists on
   paper, together with a first compactification/boundary protocol, but
   no realization theorem is proved yet.
5. The framing-coordinate bottleneck of Part III is now partially
   resolved: \(\xi\) has an effective finite-level rooted/cyclotomic
   model.
6. The local packet determinant bottleneck is now also partially
   resolved: `107_20` proves, in a local packet algebra model, that the
   off-diagonal packet line is the cyclotomic determinant line tensored
   with a norm-one rooted-label factor.
7. That globalization bottleneck is now also partially resolved:
   `107_21` glues the local packet determinant package into a global
   order-indexed line object on \(\mathcal X_T^{(1)}\) and pins the
   archimedean completion to \(\mathcal L_\infty\).
8. That metrized-target bottleneck is now also partially resolved:
   `107_22` fixes the candidate integrable adelic realized class
   \(\widehat{\mathcal M}_{f,T}^{\rm cand}\) and the degree-zero
   normalization protocol.
9. That integrability bottleneck is now also partially resolved:
   `107_23` reduces admissibility/integrability to a finite chartwise
   logarithmic singularity audit and closes off-diagonal finiteness on
   the candidate model.
10. That degree-zero bottleneck is now also partially resolved:
   `107_24` fixes the candidate polarization and reduces A3 to finitely
   many visible generator-vs-polarization intersections.
11. That first intersection bottleneck is now also partially resolved:
   `107_25` decomposes the polarization denominator into the corner term
   and explicit exceptional corrections, and does the same for diagonal
   and graph degrees.
12. That exceptional-locus bottleneck is now also partially resolved:
   `107_26` reduces nonvanishing of the polarization denominator to a
   finite audit of polarization-active blow-up centers and their
   corner-preserving behavior.
13. The equality-case bottleneck of `107_11` is now partially resolved
    at the finite shadow level: `107_48` exact-audits the required
    radical-to-torsion / non-radical-survival pattern after
    realification, but not the actual geometric realization map.
14. The pairing-transport bottleneck linking `107_11` to `107_13` is now
    also partially resolved at the finite shadow level: `107_49`
    exact-audits generator comparison, bilinear extension, primitive
    self-pairing compatibility, and radical compatibility in one exact
    bilinear model, but not the actual geometric comparison theorem.
13. That local-center bottleneck is now also partially resolved:
   `107_27` enumerates the visible local center types and excludes
   structural corner collapse in the present chart atlas.
14. The next load-bearing unknown inside Part III is now the signed
   quantitative control of the remaining correction package.
15. Part IV is fully formalized as a proof target, but not yet completed.
16. The E1 and E2 terminal branches remain unresolved in the current
   workspace.

Therefore the phase is not complete.  The present evidence supports the
stronger statement:

\[
 \text{Phase 107 has a complete audited roadmap through Part IV, but not yet a proved terminal branch.}
 \tag{6.1}
\]

## 7. Immediate next technical fronts

Given the ledger above, the next non-cosmetic fronts are:

1. construct an actual candidate family \(\mathcal X_T\) for III-A;
2. analyze the resulting correction terms in the polarization
   intersections;
3. prove the required generator-vs-polarization intersections and the
   nonvanishing \(H_T^{(1)}\cdot H_T^{(1)}\);
4. prove the primitive degree-zero condition for the candidate realized
   class on the chosen polarization;
5. prove that the candidate metric satisfies the exact published
   integrability hypotheses of the chosen adelic theorem;
6. identify the descended metrized packet package with a genuine
   Deligne-pairing or adelic analogue;
7. build the Picard/Jacobian realization map of III-B on those
   generators;
8. verify the metric lands in the domain of Faltings--Hriljac /
   Yuan--Zhang, if pursuing E1;
9. compare target self-intersections with the source quadratic form to
   attack the terminal identity.

These are the first genuinely proof-bearing tasks not yet discharged by
the current Phase 107 tree.

## 8. Status

This ledger is the current authoritative audit companion for Phase 107.
It should be updated whenever a formerly formalized/open item becomes
proved, or whenever a claimed route fails one of the mandatory
falsifiers.

## Entry 166 -- infinite Weil quotient / finite-target no-go

Artifact: `107_241_INFINITE_WEIL_QUOTIENT_NO_GO.md`.

The completed polarized Weil form has infinite algebraic rank: finite rank
would force its convolution distribution to be an exponential polynomial,
contradicting the infinitely many spectral frequencies supplied
unconditionally by Hardy's theorem. The balanced moment conditions have
codimension at most two and cannot change infinite rank to finite rank.
Consequently the balanced source modulo the exact Weil radical is
infinite-dimensional, and no finite-dimensional real target can realize the
kernel identity required by `107_00`. This closes the NS-only and every
other finite-rank exact-target branch. Rows (a) and (d) remain open only in
an infinite-dimensional, nonclassical category.

Status: `FINITE_RANK_EXACT_TARGET: CLOSED_NO_GO`; no paper status promoted.
