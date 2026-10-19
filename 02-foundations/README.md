# Foundations

This folder holds the shared computational base of the project: the numerical engine for the
Connes–Consani–Moscovici spectral triple, tabulated zeros of the zeta function, and a
reproducibility notebook. Later research phases import or cite these files instead of rebuilding
them, so they act as the common reference point for every numerical check in the corpus.
Numerics are used only where a proof step strictly needs them.

## Contents

- `engine/` — Python implementation of the Weil quadratic form and the spectral-triple operator
  (float64 and high-precision versions, an earlier reference version, and a symbol positivity
  detector). Has its own README.
- `zeros-data/` — JSON tables of imaginary parts of nontrivial zeros of the zeta function.
- `validation/` — a notebook that reruns the basic checks of the engine and data.

## Related folders

- [../03-research/phase-60-discriminant/](../03-research/phase-60-discriminant/) — where the engine was first validated.
- [../03-research/](../03-research/) — research phases that use these tools.
- [../00-references/](../00-references/) — third-party papers behind the constructions.
- [../07-calculos-adicionales/](../07-calculos-adicionales/) — additional calculations.
