import Main

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

open Lean Elab Command

namespace Step5X

def projMod (m : Name) : Bool :=
  let r := m.getRoot
  !(r == `Mathlib || r == `Lean || r == `Init || r == `Std || r == `Batteries || r == `Aesop || r == `Qq
    || r == `ProofWidgets || r == `Plausible || r == `ImportGraph || r == `LeanSearchClient || r == `Lake || r == `Cli)

def modOf (mods : Array Name) (env : Environment) (n : Name) : Name :=
  match env.getModuleIdxFor? n with
  | some i => mods[i.toNat]!
  | none => `Step5

def directDeps (ci : ConstantInfo) : Array Name := Id.run do
  let mut out : Array Name := ci.type.getUsedConstants
  match ci with
  | .defnInfo v => out := out ++ v.value.getUsedConstants
  | .thmInfo v => out := out ++ v.value.getUsedConstants
  | .opaqueInfo v => out := out ++ v.value.getUsedConstants
  | .inductInfo v => out := out ++ v.ctors.toArray
  | .ctorInfo v => out := out.push v.induct
  | .recInfo v => out := out ++ v.all.toArray
  | _ => pure ()
  return out

def kindOf : ConstantInfo → String
  | .thmInfo _ => "theorem" | .defnInfo _ => "def" | .opaqueInfo _ => "opaque" | .axiomInfo _ => "axiom"
  | .inductInfo _ => "inductive" | .ctorInfo _ => "ctor" | .recInfo _ => "rec" | .quotInfo _ => "quot"

/-- project declarations reachable from `start`, and the non-project frontier -/
def depClosure (mods : Array Name) (env : Environment) (start : Array Name) : Std.HashSet Name × Std.HashSet Name := Id.run do
  let mut seen : Std.HashSet Name := {}
  let mut front : Std.HashSet Name := {}
  let mut stack : Array Name := start
  while !stack.isEmpty do
    let n := stack.back!
    stack := stack.pop
    if seen.contains n || front.contains n then continue
    if !projMod (modOf mods env n) then
      front := front.insert n
      continue
    seen := seen.insert n
    match env.find? n with
    | none => pure ()
    | some ci => for c in directDeps ci do
        if !(seen.contains c || front.contains c) then stack := stack.push c
  return (seen, front)

def dump (mods : Array Name) (dir : String) (tag : String) (start : Array Name) (edges : Bool) : CommandElabM String := do
  let env ← getEnv
  let (s, f) := depClosure mods env start
  let h ← IO.FS.Handle.mk s!"{dir}/{tag}.decls.tsv" .write
  h.putStrLn "name\tkind\tmodule\tline_start\tline_end\tn_direct_deps_project"
  let he ← IO.FS.Handle.mk s!"{dir}/{tag}.edges.tsv" .write
  let mut thms := 0
  let mut defs := 0
  let mut lines := 0
  let mut usedMods : Std.HashSet Name := {}
  for n in s do
    let m := modOf mods env n
    usedMods := usedMods.insert m
    let rng ← liftCoreM (findDeclarationRanges? n)
    let (l0, l1) := match rng with
      | some r => (r.range.pos.line, r.range.endPos.line)
      | none => (0, 0)
    let some ci := env.find? n | continue
    let k := kindOf ci
    if k == "theorem" then thms := thms + 1
    if k == "def" then defs := defs + 1
    if l0 > 0 then lines := lines + (l1 - l0 + 1)
    let ds := (directDeps ci).filter fun c => s.contains c && c != n
    let dsU : Std.HashSet Name := ds.foldl (fun acc c => acc.insert c) {}
    h.putStrLn s!"{n}\t{k}\t{m}\t{l0}\t{l1}\t{dsU.size}"
    if edges then
      for c in dsU do he.putStrLn s!"{n}\t{c}"
  h.flush; he.flush
  IO.FS.writeFile s!"{dir}/{tag}.frontier.txt" ("\n".intercalate (f.toList.map toString))
  IO.FS.writeFile s!"{dir}/{tag}.modules.txt" ("\n".intercalate (usedMods.toList.map toString))
  let line := s!"{tag}\tdecls={s.size}\ttheorems={thms}\tdefs={defs}\tsource_lines={lines}\tmodules={usedMods.size}\tnonproject_frontier={f.size}"
  let hs ← IO.FS.Handle.mk s!"{dir}/SUMMARY.partial.txt" .append
  hs.putStrLn line; hs.flush
  return line

run_cmd do
  let dir := "/home/lean/step5-out2"
  IO.FS.createDirAll dir
  let env ← getEnv
  let mods := env.header.moduleNames
  let mut summ : Array String := #[]
  summ := summ.push (← dump mods dir "step5_families" #[`Step5.families] true)
  summ := summ.push (← dump mods dir "step5_topG" #[`Step5.topG] false)
  summ := summ.push (← dump mods dir "step5_vwin" #[`Step5.vwin] false)
  summ := summ.push (← dump mods dir "step5_hosts" #[`Step5.hosts] false)
  summ := summ.push (← dump mods dir "riemannHypothesis" #[`riemannHypothesis] false)
  -- named intermediate results, located by suffix
  let sufs : List String := ["Deduction.ch_top", "UpperTheory.Top.supplyChi", "UpperTheory.One.vwin_of_row",
    "UpperTheory.Top.shape_closed_link_n_of_green", "UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound",
    "UpperTheory.Gal.Int.galoisLocalGlobalStrong_recParameter", "UpperTheory.Zero.LLC.recTExists",
    "UpperTheory.Top.zeroFreeAll_of_topG", "UpperTheory.FinalTheorems.everyCharacter",
    "SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt", "GlobalTheory.GreenBridge.green_of_regular"]
  let mut found : Array Name := #[]
  for suf in sufs do
    let cands := env.constants.fold (init := (#[] : Array Name)) fun acc n _ =>
      if !n.isInternal && (n.toString == suf || n.toString.endsWith ("." ++ suf)) then acc.push n else acc
    for c in cands do found := found.push c
  for t in found do
    summ := summ.push (← dump mods dir ("node_" ++ t.toString) #[t] false)
  let total := env.constants.fold (init := 0) fun acc n _ => if projMod (modOf mods env n) then acc + 1 else acc
  summ := summ.push s!"ALL_PROJECT_CONSTANTS\t{total}"
  IO.FS.writeFile s!"{dir}/SUMMARY.txt" ("\n".intercalate summ.toList ++ "\n")
  logInfo ("\n".intercalate summ.toList)

end Step5X
