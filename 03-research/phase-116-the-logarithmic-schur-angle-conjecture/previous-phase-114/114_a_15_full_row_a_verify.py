#!/usr/bin/env python3
"""Run the complete phase-114 row-A verification suite.

This is an orchestrator, not an additional mathematical proof.  It checks
that every finite/symbolic verifier cited by the row-A ledger exits cleanly.
"""

from pathlib import Path
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parent
SCRIPTS = [
    "114_a_01_the_growth_dichotomy.py",
    "114_a_02_the_absolute_quadric.py",
    "114_a_03_the_candidate_ledger.py",
    "114_a_04_lambda_gauge.py",
    "114_a_05_i7_kernel_verify.py",
    "114_a_07_toric_realisation_verify.py",
    "114_a_08_g2_r8_verify.py",
    "114_a_09_i7_no_go_verify.py",
    "114_a_11_g1_binary_constant_verify.py",
    "114_a_12_haran_source_and_picard_verify.py",
    "114_a_13_g3_boundary_verify.py",
    "114_a_14_h7_kunneth_verify.py",
    "114_a_16_h7_descent_source_verify.py",
    "114_a_17_h7_prime_incidence_verify.py",
    "114_a_18_h7_prime_picard_verify.py",
    "114_a_19_h7_discrete_bigrade_verify.py",
    "114_a_20_h7_axis_sections_verify.py",
    "114_a_21_h7_off_diagonal_entropy_verify.py",
    "114_a_22_h7_scalarization_verify.py",
    "114_a_23_h7_arity_inflation_verify.py",
    "114_a_24_h7_intrinsic_rank_verify.py",
    "114_a_25_h7_power_evaluation_verify.py",
    "114_a_26_h7_laurent_gate_verify.py",
    "114_a_27_h7_differential_injectivity_verify.py",
    "114_a_28_h7_real_boundary_verify.py",
    "114_a_30_h7_bounded_laurent_tree_verify.py",
    "114_a_31_h7_lnf_upper_nogo_verify.py",
    "114_a_32_h7_selective_acceptance_verify.py",
    "114_a_33_h7_finite_moment_verify.py",
    "114_a_34_h7_optimal_rank_rr_verify.py",
    "114_a_35_h7_general_arity_verify.py",
    "114_a_36_i7_witt_operator_verify.py",
    "114_a_37_i7_witt_graph_verify.py",
    "114_a_38_i7_scalar_transport_nogo_verify.py",
    "114_a_39_h7_twisted_field_verify.py",
    "114_a_40_h7_universal_twisted_bio_verify.py",
    "114_a_41_i7_witt_excess_verify.py",
    "114_a_42_i7_standard_cone_nogo_verify.py",
    "114_a_43_i7_witt_prime_node_verify.py",
    "114_a_44_i7_prime_power_contact_verify.py",
    "114_a_45_i7_global_contact_verify.py",
    "114_a_46_i7_geometric_contact_sheaf_verify.py",
    "114_a_47_i7_contact_shadow_verify.py",
    "114_a_48_i7_ruling_span_nogo_verify.py",
    "114_a_49_h7_homogeneous_endobio_verify.py",
    "114_a_50_h7_cofinal_moment_verify.py",
    "114_a_51_h7_full_tree_bio_moment_verify.py",
    "114_a_52_h7_global_finite_effective_verify.py",
    "114_a_53_h7_picard_normalization_verify.py",
    "114_a_54_h7_moment_saturation_verify.py",
    "114_a_55_h7_bounded_cross_interpolation_verify.py",
    "114_a_56_h7_selective_moment_quotient_verify.py",
    "114_a_57_h7_global_denominator_nogo_verify.py",
    "114_a_58_h7_den_trans_span_derived_witt_verify.py",
    "114_a_59_g3_two_point_polarization_verify.py",
    "114_a_60_g3_effectivity_equivalence_verify.py",
    "114_a_61_i7_faithful_picard_lift_verify.py",
    "114_a_62_i7_cartier_prime_regularity_verify.py",
    "114_a_63_h7_fraction_pullback_admissibility_verify.py",
    "114_a_64_h7_prime_regularity_saturation_verify.py",
    "114_a_65_h7_abstract_picard_pullback_verify.py",
    "114_a_66_h7_type_audit_verify.py",
    "114_a_67_h7_typed_cartier_act_verify.py",
    "114_a_68_h7_cotangent_lci_gate_verify.py",
    "114_a_69_h7_split_cotangent_verify.py",
    "114_a_70_i7_decorated_diagonal_verify.py",
    "114_a_71_h7_fold_fiber_verify.py",
    "114_a_72_h7_all_arity_block_regular_verify.py",
    "114_a_73_h7_depth_two_regular_verify.py",
    "114_a_74_h7_read_once_hessian_verify.py",
    "114_a_75_h7_signed_read_once_verify.py",
    "114_a_76_h7_cancellation_purity_verify.py",
    "114_a_77_h7_cut_and_local_bundle_verify.py",
    "114_a_78_h7_single_site_confluence_verify.py",
    "114_a_79_h7_core_critical_pairs_verify.py",
    "114_a_80_h7_odd_prime_and_sign_orbit_verify.py",
    "114_a_81_h7_k22_two_torsion_verify.py",
    "114_a_82_h7_rectangular_macro_smith_verify.py",
    "114_a_83_h7_aggregated_fiber_smith_verify.py",
    "114_a_84_h7_tame_scalar_reduction_verify.py",
    "114_a_85_h7_macro_context_graph_verify.py",
    "114_a_86_h7_p_convex_boundary_verify.py",
    "114_a_87_h7_characteristic_zero_residual_verify.py",
    "114_a_88_h7_real_bio_marginal_blindness_verify.py",
    "114_a_89_h7_two_level_marginal_verify.py",
    "114_a_90_h7_laminar_nested_verify.py",
    "114_a_91_h7_binary_matching_verify.py",
    "114_a_92_h7_parity_fiber_verify.py",
    "114_a_93_h7_parity_smith_verify.py",
    "114_a_94_h7_fold_zero_parity_verify.py",
    "114_a_95_h7_parity_swap_verify.py",
    "114_a_96_h7_parity_rigid_verify.py",
    "114_a_97_h7_positive_rigid_no_go_verify.py",
    "114_a_98_h7_scalar_invisible_full_bio_verify.py",
    "114_a_99_h7_tame_retract_dichotomy_verify.py",
    "114_a_100_h7_finite_set_retract_verify.py",
    "114_a_101_h7_split_coefficient_retract_verify.py",
    "114_a_102_h7_augmentation_flatness_verify.py",
    "114_a_103_h7_cross_defect_tameness_verify.py",
    "114_a_104_h7_signed_plane_nontame_verify.py",
    "114_a_105_h7_first_jet_prime_regular_verify.py",
    "114_a_106_h7_universal_rational_jet_verify.py",
    "114_a_107_h7_scalar_differential_z2_verify.py",
    "114_a_108_h7_explicit_scalar_two_torsion_verify.py",
    "114_a_109_h7_z_regular_reflection_verify.py",
    "114_a_110_h7_regular_pro_square_verify.py",
    "114_a_111_h7_prime_cartier_subgroup_verify.py",
    "114_a_112_h7_all_prime_cartier_lattice_verify.py",
    "114_a_113_h7_same_ruling_intersection_verify.py",
    "114_a_114_h7_reduced_cross_intersection_verify.py",
    "114_a_115_h7_contact_vs_rr_verify.py",
    "114_a_116_h7_rr_descent_antidiagonal_verify.py",
    "114_a_117_h7_calibrated_selective_quotient_verify.py",
    "114_a_118_h7_fresh_block_reevaluation_verify.py",
    "114_a_119_h7_pseudofinite_bio_verify.py",
    "114_a_120_h7_all_ray_calibrated_interpolation_verify.py",
    "114_a_121_h7_section_rr_descent_verify.py",
    "114_a_122_h7_reflected_antidiagonal_verify.py",
    "114_a_123_h7_global_numerical_green_verify.py",
    "114_a_124_h7_metrized_green_biextension_verify.py",
    "114_a_125_h7_fresh_exactness_type_verify.py",
    "114_a_126_h7_fresh_open_restriction_verify.py",
    "114_a_127_h7_fresh_cartier_nogo_verify.py",
    "114_a_128_h7_antidiagonal_principal_verify.py",
    "114_a_129_h7_framed_divisor_exact_verify.py",
    "114_a_130_h7_mixed_boundary_detector_verify.py",
    "114_a_131_h7_global_reflection_type_verify.py",
    "114_a_132_h7_supportwise_local_reg_verify.py",
    "114_a_133_i7_diagonal_chow_nogo_verify.py",
    "114_a_134_i7_torsor_linearization_gate_verify.py",
    "114_a_135_h7_real_point_base_change_verify.py",
    "114_a_136_h7_rational_sphere_no_retraction_verify.py",
    "114_a_137_r8_scope_verify.py",
    "114_a_138_h7_cech_unit_criterion_verify.py",
    "114_a_139_i7_integration_scope_verify.py",
    "114_a_140_i7_contact_framed_verify.py",
    "114_a_141_h7_contact_determinant_verify.py",
    "114_a_142_h7_asymptotic_rr_determinant_verify.py",
    "114_a_143_h7_valued_boundary_norm_verify.py",
    "114_a_144_a4_strong_metrized_square_verify.py",
    "114_d3_01_imported_index_theorems.py",
    "114_d3_02_linear_vs_quadratic_chi.py",
    "114_d3_03_acceptance_tests.py",
]


failures = []
suite_start = time.monotonic()
for script in SCRIPTS:
    start = time.monotonic()
    try:
        run = subprocess.run(
            [sys.executable, str(ROOT / script)],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=360,
            check=False,
        )
        elapsed = time.monotonic() - start
        verdicts = [line.strip() for line in run.stdout.splitlines()
                    if "VERDICT" in line or "FAILED CHECKS" in line]
        detail = verdicts[-1] if verdicts else "exit-only verifier"
        if run.returncode == 0:
            print(f"PASS  {script:<48} {elapsed:7.2f}s  {detail}", flush=True)
        else:
            print(f"FAIL  {script:<48} {elapsed:7.2f}s  exit={run.returncode}", flush=True)
            print("\n".join(run.stdout.splitlines()[-25:]), flush=True)
            failures.append(script)
    except subprocess.TimeoutExpired as exc:
        elapsed = time.monotonic() - start
        print(f"FAIL  {script:<48} {elapsed:7.2f}s  TIMEOUT", flush=True)
        failures.append(script)

elapsed = time.monotonic() - suite_start
print("=" * 96)
if failures:
    print(f"VERDICT: ROW-A SUITE FAILED ({len(failures)} scripts; {elapsed:.2f}s)")
    print("FAILED: " + ", ".join(failures))
    raise SystemExit(1)
print(f"VERDICT: ALL {len(SCRIPTS)} ROW-A VERIFIERS PASS ({elapsed:.2f}s)")
