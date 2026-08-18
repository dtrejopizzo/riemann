# Row (d) endpoint certificates — `T = ½log3` and `T = log2`

This directory backs Theorem *Certified primitive initial interval*
(`thm:certifiedendpoints`) and Corollary *Certified initial interval*
(`cor:certifiedinitialinterval`) of `main.tex`: strict positivity of the complete
primitive operator on `P_T` for every `0 < T ≤ log 2`.

These are **endpoint theorems**. They do not claim that row (d) is globally closed.
The global statement remains open; see the closure ledger in `main.tex`.

## What is here

| File | Role |
|---|---|
| `114_d_85_LOG2_FULL_SPACE_ENDPOINT_CERTIFICATE.md` | The `T = log2` certificate: scope, directed ingredients, and every stated bound |
| `114_d_77_LOG3_LEGENDRE_ARB_ENDPOINT_CERTIFICATE.md` | The `T = ½log3` endpoint certificate |
| `114_d_85_log2_full_space_manifest.json` | SHA-256 pins for the five load-bearing files, plus the exact reproduction commands |
| `114_d_85_two_level_endpoint_budget_verify.py` | **Tier 1** — recombines the certified enclosures into the final positivity margins. Standard library only |
| `114_d_84_log2_degree23_projected_gap_arb_verify.py` | **Tier 2** — directed projected-complement gap at `T=log2`, degree 23 |
| `114_d_85_fixed_vector_analytic_verify.py` | **Tier 2** — analytic ODE assembly for the fixed low modes `v₁, v₂, v_o` |
| `114_d_85_capacity_arb_prototype.py` | **Tier 2** — positive Gamma-tail capacity; also stores the `v₁` binary64 data |
| `114_d_77_log3_legendre_arb_verify.py` | **Tier 2** — the D.77 Legendre/Arb assembly both endpoints build on |
| `114_d_79_stable_projected_tangency_verify.py` | **Tier 2** — the D.79 exact shift mesh driver |

Dependency closure of the entry point `114_d_84_…`:
`114_d_84 → {114_d_79 → 114_d_77, 114_d_85_capacity, 114_d_85_fixed_vector → {114_d_77, 114_d_85_capacity}}`.
All of it is present here; nothing is referenced from outside this directory.

## Two tiers, and exactly what each one establishes

**Tier 1 — runs anywhere, no dependencies.**

```
python3 114_d_85_two_level_endpoint_budget_verify.py
```

Reproduces, from the certified enclosures, the four quantities the proof of
`thm:certifiedendpoints` combines:

```
PASS two-level endpoint budget
big-block gap lower:              0.46597814251161183846...   (main.tex: > 0.4659)
v2/complement gap lower:          0.00203369728246969981...   (main.tex: > 0.0020336972824697)
capacity threshold / lower:       1.21106727883961186698... / 1.83281360220952728854e-6
final capacity margin:            8.63386022095124852109e-8   ( > 0 )
odd complement / final lower:     0.04975274401048942490... / 8.13856175478998041797e-6
```

This is the *recombination* step: it shows the enclosures stated in the paper do
compose into a strictly positive margin, with the arithmetic redone at 80 digits.
It does **not** recompute the enclosures themselves.

**Tier 2 — recomputes the Arb interval enclosures.** Requires `python-flint`
(Arb/FLINT bindings) and `numpy`, neither of which is in the standard library.
The manifest records the exact invocations:

```
D84_DEG=9 D84_HIGH_GAP=1 PYTHONPATH=<flint> python3 114_d_84_log2_degree23_projected_gap_arb_verify.py
D84_DEG=9 D84_ODD_GAP=1  PYTHONPATH=<flint> python3 114_d_84_log2_degree23_projected_gap_arb_verify.py
                         PYTHONPATH=<flint> python3 114_d_85_fixed_vector_analytic_verify.py
D85_VECTOR=2             PYTHONPATH=<flint> python3 114_d_85_fixed_vector_analytic_verify.py
D85_VECTOR=odd           PYTHONPATH=<flint> python3 114_d_85_fixed_vector_analytic_verify.py
D85_GENERIC_BOUNDS=1     PYTHONPATH=<flint> python3 114_d_85_fixed_vector_analytic_verify.py
                         PYTHONPATH=<flint> python3 114_d_85_capacity_arb_prototype.py
```

The `python_flint_path` field in the manifest records `/tmp/d61-flint`, the
throwaway location used in the original run. Substitute any working
`python-flint` installation.

Floating point enters only to *select* the fixed vectors `v₁, v₂, v_o` and to
precondition congruences; every stated inequality is recomputed with Arb balls,
and the fixed vectors are stored exactly as binary64 input data. Selecting a
vector badly can only weaken a bound, never invalidate one.

## Integrity

```
python3 -c "
import json,hashlib,pathlib
m=json.load(open('114_d_85_log2_full_space_manifest.json'))
for n,w in m['sha256'].items():
    g=hashlib.sha256(pathlib.Path(n).read_bytes()).hexdigest()
    print(('OK  ' if g==w else 'FAIL'),n)
"
```

All five pinned files verify as shipped.

## Scope, stated plainly

- What is certified: strict positivity of the **complete operator on the full
  Hilbert space** `P_T` at `T = ½log3` and `T = log2` — not the sign of a finite
  Galerkin matrix.
- What is *not* certified here: any statement about `T > log2`, and therefore
  row (d), condition G, or the Riemann Hypothesis.
- The endpoint `T = ½log5` is **not** claimed. An earlier version of that
  calculation was invalid; `main.tex` records the retraction and the reason (the
  five-column Gram was formed after eliminating two finite safe blocks, so it did
  not control the complement of the whole space). The surviving pieces of that
  computation remain rigorous as separate statements but do not prove positivity
  at that endpoint.
- Prior art: that *some* initial window is positive is not new — it is
  Yoshida's Lemma 2, reproved unconditionally in Suzuki. What is new here is the
  quantitative, interval-certified reach to `log 2`, with the margins above.
