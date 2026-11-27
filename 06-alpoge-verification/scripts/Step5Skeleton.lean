import Main

/-!
Statement-level skeleton of the archive. For every theorem of the project: the head constant of
its conclusion and the head constants of its hypotheses. For every definition: whether it is a
named proposition. A theorem with no hypotheses whose conclusion is a named proposition `P` is a
closed proof of `P`.
-/

open Lean Elab Command

namespace Step5S

def projMod (m : Name) : Bool :=
  let r := m.getRoot
  !(r == `Mathlib || r == `Lean || r == `Init || r == `Std || r == `Batteries || r == `Aesop || r == `Qq
    || r == `ProofWidgets || r == `Plausible || r == `ImportGraph || r == `LeanSearchClient || r == `Lake || r == `Cli)

def headOf (e : Expr) : String :=
  match e.getAppFn with
  | .const n _ => n.toString
  | _ => "_"

/-- binder heads and conclusion head of a type -/
partial def split (e : Expr) (acc : Array String) : Array String × String :=
  match e with
  | .forallE _ d b _ => split b (acc.push (headOf d))
  | .mdata _ b => split b acc
  | _ => (acc, headOf e)

partial def endsInProp (e : Expr) : Bool :=
  match e with
  | .forallE _ _ b _ => endsInProp b
  | .mdata _ b => endsInProp b
  | .sort l => l.isZero
  | _ => false

partial def arity (e : Expr) (k : Nat) : Nat :=
  match e with
  | .forallE _ _ b _ => arity b (k + 1)
  | .mdata _ b => arity b k
  | _ => k

run_cmd do
  let env ← getEnv
  let mods := env.header.moduleNames
  let dir := "/home/lean/skeleton-out"
  IO.FS.createDirAll dir
  let ht ← IO.FS.Handle.mk s!"{dir}/theorems.tsv" .write
  let hd ← IO.FS.Handle.mk s!"{dir}/prop-defs.tsv" .write
  ht.putStrLn "theorem\tmodule\tn_binders\tconclusion_head\tbinder_heads"
  hd.putStrLn "definition\tmodule\tarity"
  let mut nt := 0
  let mut nd := 0
  for (n, ci) in env.constants.map₁ do
    let some i := env.getModuleIdxFor? n | continue
    let m := mods[i.toNat]!
    if !projMod m then continue
    match ci with
    | .thmInfo v =>
      let (hs, c) := split v.type #[]
      let hs' := hs.filter (· != "_")
      ht.putStrLn s!"{n}\t{m}\t{hs.size}\t{c}\t{",".intercalate hs'.toList}"
      nt := nt + 1
    | .defnInfo v =>
      if endsInProp v.type then
        hd.putStrLn s!"{n}\t{m}\t{arity v.type 0}"
        nd := nd + 1
    | .inductInfo v =>
      if endsInProp v.type then
        hd.putStrLn s!"{n}\t{m}\t{arity v.type 0}"
        nd := nd + 1
    | _ => pure ()
  ht.flush; hd.flush
  IO.FS.writeFile s!"{dir}/DONE" s!"theorems={nt}\tprop_defs={nd}\n"
  logInfo s!"theorems={nt} prop_defs={nd}"

end Step5S
