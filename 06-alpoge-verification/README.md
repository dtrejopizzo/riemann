# Verification of Alpoge's Lean archive

The argument that closes row D (Paper 46 and its companions, Papers 49–56) is the work of Levent
Alpoge, released as a Lean 4 formalization (<https://alpo.ge/remark.pdf>). In the first version
of Paper 46 it entered as one statement, called step (5) there: the existence of families of
characters carrying a column package with uniform constants. His development proves the Riemann hypothesis on its own.

This folder is the record of an independent compilation of his archive: the build logs, the axiom
check of the main theorems, the checksums of everything that was compiled, and the scripts that
were run. Nothing in the archive was modified.

## Result

The verification succeeded. The whole archive compiles, and the main theorems depend only on the
three standard axioms of Lean.

| Check | Outcome |
|---|---|
| Archive | `lean.tar.gz` from <https://alpo.ge>, 14 parts, SHA-256 `9631b4f0…49c7fc` (full list in [`source-metadata/SHA256SUMS`](source-metadata/SHA256SUMS)) |
| Toolchain | Lean 4.33.1 (commit `819816b2`), Mathlib at revision `0df444a3`, as pinned by the archive |
| Build | `lake build` ends with `Build completed successfully (183903 jobs)`, exit status 0 |
| Modules | 175,187 source files in the archive; 175,187 compiled `.olean` files, one for each |
| Errors | none: no failed job, no `error:` line, no use of `sorry` |
| Axioms | `riemannHypothesis` and the four other main theorems depend on `propext`, `Classical.choice`, `Quot.sound` only |

The three axioms are the standard ones of Lean 4 and Mathlib. No other axiom and no `sorryAx`
appears. The output of the axiom check ([`results/axioms.log`](results/axioms.log)), in full:

```
riemannHypothesis : RiemannHypothesis
'riemannHypothesis' depends on axioms: [propext, Classical.choice, Quot.sound]
'riemannZeta_eq_zero_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'LFunction_ne_zero_of_half_lt_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'LFunction_eq_zero_re' depends on axioms: [propext, Classical.choice, Quot.sound]
'LFunction_eq_zero_re_of_isPrimitive' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The statements being proved are in [`source-metadata/Statements.lean`](source-metadata/Statements.lean)
(16 lines) and the theorems in [`source-metadata/Main.lean`](source-metadata/Main.lean).

## What this does and does not establish

- It establishes that the archive, exactly as published, is accepted by the Lean 4 kernel with the
  pinned toolchain and library, and that its main theorems rest on the three standard axioms.
- It does not review the mathematics by hand. Whether `RiemannHypothesis` in `Statements.lean` says
  what it should is a matter of reading those 16 lines against Mathlib's definitions.
- The checksums below let anyone compare their own compilation with this one.

## The run

Machine: AWS `r7a.48xlarge` (192 vCPU AMD EPYC 9R14, 1.5 TB RAM), Ubuntu 24.04, 1.3 TB disk.
The build was completed on 24 November 2026; the logged `lake build` took 4 h 05 min of wall-clock
time and ended with exit status 0. The 183,903 jobs are the 175,187 modules of the
archive together with Mathlib and its dependencies. The compiled tree occupies about 1 TB.

The build emits many linter warnings (unused variables, style). They are not errors and are left
in the logs as produced.

## Contents

| Path | Contents |
|---|---|
| `results/axioms.log` | The axiom check of the main theorems. |
| `results/step5-statement.log` | The check of step (5) as a single statement, with its axioms (see below). |
| `results/logs/build.log.gz` | The log of the build, ending in `Build completed successfully`. |
| `results/logs/build-check.log.gz` | `lake build` on the completed tree: all 183,903 jobs up to date, with every warning of the tree. |
| `results/logs/mathlib-cache.log` | Download of the Mathlib cache. |
| `results/checksums/source-files.sha256.gz` | SHA-256 of each of the 175,187 `.lean` files that were compiled. |
| `results/checksums/compiled-modules.txt.gz` | The list of the 175,187 compiled modules. |
| `SHA256SUMS.results` | SHA-256 of every file under `results/`. |
| `source-metadata/` | The archive's `lakefile.toml`, `lake-manifest.json`, `lean-toolchain`, `Main.lean`, `Statements.lean`, `MainTheorems.lean`, and the checksums of the archive parts. |
| `scripts/` | The code that was run: machine setup and build (`cloud-init-build.sh`, `run.sh`), the checks (`run-checks.sh`, `AxiomCheck.lean`), and the files on step (5) (`Step5Statement.lean`, `Step5Standalone.lean`, `Step5Extract.lean`, `Step5Skeleton.lean`). |

## Step (5) as a single Lean statement

In the archive, step (5) of the first version of Paper 46 is not a named theorem: it is assembled inside the final
chain. [`scripts/Step5Statement.lean`](scripts/Step5Statement.lean) gives it a name,
`Step5.families`, using the same proof terms as the archive, for the trivial character and windows
of exponent 3/2. Lean accepts it, with the same three axioms
([`results/step5-statement.log`](results/step5-statement.log)):

```
Step5.families : UpperTheory.Top.FamilyClassConnected fun {eps} =>
  (UpperTheory.Top.GChi Formalism.HC.PChar.one).cls (3 / 2)
'Step5.families' depends on axioms: [propext, Classical.choice, Quot.sound]
```

The three auxiliary statements of that file (`Step5.topG`, `Step5.vwin`, `Step5.hosts`) depend on
the same three axioms.

[`scripts/Step5Extract.lean`](scripts/Step5Extract.lean) computes the declarations of the archive
on which this statement depends: 1,264,752 declarations, of which 1,074,616 are theorems, in
146,371 of the 175,187 modules. Step (5) is most of the archive. The log of this computation
(`step5-extract.log`) is not among the files of `results/`; the figures are those of the run.

## Relation to the rest of the repository

- [`../04-papers/46-row-d-sign-radial-intersection-form/`](../04-papers/46-row-d-sign-radial-intersection-form/):
  Paper 46, the main paper of row D; Papers 49–56 write the argument out on paper as three
  theorems. The first version of Paper 46, where step (5) is used, is in the history of the
  repository.
- [`../03-research/phase-214-explicit-bounds-and-reconstruction/`](../03-research/phase-214-explicit-bounds-and-reconstruction/): notes that rewrite the arithmetic
  inputs of step (5) on paper.
- [`../README.md`](../README.md): the place of this check in the whole project.

## Reproducing

1. Download the 14 parts of `lean.tar.gz` from <https://alpo.ge> and check them against
   `source-metadata/SHA256SUMS`.
2. Run `scripts/run.sh` (it installs `elan`, fetches the Mathlib cache and runs `lake build`).
   Allow 1.3 TB of disk.
3. Copy `AxiomCheck.lean`, `Step5Statement.lean` and `Step5Extract.lean` into the project folder,
   run `scripts/run-checks.sh`, and compare `axioms.log` and `step5-statement.log` with the files
   of the same name in `results/`.
4. Check the files of `results/` against `SHA256SUMS.results` with `sha256sum -c SHA256SUMS.results`.
