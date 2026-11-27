import Development.AutomorphicArithmetic.CharacterBoxes.MainConclusion
import Development.AutomorphicArithmetic.CharacterBoxes.SupplyChi
import Development.AutomorphicArithmetic.CharacterBoxes.ZeroFreeAllOfTopG
import Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.TopPlug
import Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.SiegelEisensteinSecondTermHypotheses
import Development.AutomorphicArithmetic.ThetaCorrespondence.ThetaPairLifts.ThirdPlaceSeries.EveryCharacterOfLiteratureOfVWin

/-!
Step (5) of Paper 46 as a single Lean statement: existence of character families carrying a
column package with uniform constants, for the trivial character and windows of exponent 3/2.
The proof terms are the ones used inside Alpoge's development (TopPlug.lean,
SiegelEisensteinSecondTermHypotheses.lean, EveryCharacterOfLiteratureOfVWin.lean,
MainConclusion.lean), re-assembled so that the statement has a name.
-/

set_option synthInstance.maxHeartbeats 200000
set_option maxHeartbeats 4000000

noncomputable section
namespace Step5

open Formalism.BasicNotions Formalism.MainNotions Formalism.HC GlobalTheory.EX GlobalTheory.Fc UpperTheory.Top

def lit : UpperTheory.LiteratureTheorems.OpenLiteratureStatements :=
  ⟨UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter, UpperTheory.Zero.LLC.recTExists,
   UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter⟩

/-- Input: the Selmer window bound for every primitive character. -/
theorem vwin : UpperTheory.Top.VWin :=
  UpperTheory.One.vwin_of_row UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter

/-- Input: hosts on windows of exponent 3/2 (trivial character). -/
theorem hosts : HostExW (3 / 2) (GChi PChar.one).req :=
  UpperTheory.Top.supplyChi PChar.one (vwin PChar.one)

/-- The family theorem in its general form (any class, any window exponent). -/
theorem topG : UpperTheory.Top.TopG :=
  let O := lit
  let P := UpperTheory.LiteratureTheorems.published_results_eigen O
  let F := UpperTheory.LiteratureTheorems.published_results_first O
  let hA := (UpperTheory.LiteratureTheorems.theta_integrals_agree_and_local_matching_of_literature O).1
  let hM := (UpperTheory.LiteratureTheorems.theta_integrals_agree_and_local_matching_of_literature O).2
  let hX := _root_.SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt (_root_.UpperTheory.LiteratureTheorems.resolution_char_zero_of_literature O) (_root_.UpperTheory.LiteratureTheorems.principalisation_char_zero_of_literature O) (_root_.UpperTheory.LiteratureTheorems.poincare_lelong_inv_of_literature O) PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsUse_outright PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright (_root_.UpperTheory.LiteratureTheorems.fargues_exact_of_literature O) (_root_.UpperTheory.LiteratureTheorems.zarhin_statement O) (_root_.UpperTheory.LiteratureTheorems.nef_rr_of_literature O) (_root_.UpperTheory.LiteratureTheorems.siegel_toroidal_integral_of_literature O) (_root_.UpperTheory.LiteratureTheorems.toroidal_for_fan_ks_of_literature O) (_root_.UpperTheory.LiteratureTheorems.semi_abelian_lie_seminegative_of_literature O) (_root_.UpperTheory.LiteratureTheorems.point_separation_pair_of_literature O) (_root_.UpperTheory.LiteratureTheorems.ar_degree_of_literature O) (_root_.UpperTheory.LiteratureTheorems.published_results_arithmetic O) (_root_.UpperTheory.LiteratureTheorems.grothendieck_deformation_of_literature O)
  let hL := UpperTheory.LiteratureTheorems.local_langlands_gl_recT_exists_of_literature O
  (_root_.UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound P F hA hM hX hL fun cDep =>
      _root_.UpperTheory.N.boundAtTwoThree_linked_of_recT P.nLink (_root_.GlobalTheory.Mem.Top.Bl.parametersOfDependence hL cDep)).elim fun h =>
    _root_.GlobalTheory.Fc.forall_goal_of_shape_of_hyps _ _ _ _
      (_root_.UpperTheory.Top.shape_closed_link_n_of_green (GlobalTheory.GreenBridge.green_of_regular P.greenRegularCharacters)) trivial trivial h

/-- STEP (5): families with a column package and uniform constants, trivial character, exponent 3/2. -/
theorem families : FamilyClassConnected ((GChi PChar.one).cls (3 / 2)) :=
  topG (3 / 2) (GChi PChar.one) (by norm_num) hosts (fun Fm h => UpperTheory.Top.hypV_of_cls PChar.one (3 / 2) Fm h)

end Step5
end

#check @Step5.families
#print axioms Step5.families
#print axioms Step5.topG
#print axioms Step5.vwin
#print axioms Step5.hosts


open Lean Elab Command in
run_cmd do
  let env ← getEnv
  let ms := env.header.moduleNames
  let proj := ms.filter fun m =>
    let r := m.getRoot
    !(r == `Mathlib || r == `Lean || r == `Init || r == `Std || r == `Batteries || r == `Aesop || r == `Qq
      || r == `ProofWidgets || r == `Plausible || r == `ImportGraph || r == `LeanSearchClient || r == `Lake || r == `Cli)
  IO.FS.writeFile "/home/lean/step5-import-closure.txt" ("\n".intercalate (proj.toList.map toString) ++ "\n")
  logInfo s!"imported modules: {ms.size}, of the archive: {proj.size}"
