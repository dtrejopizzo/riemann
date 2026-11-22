# Phase 88 - Endpoint layer pencil

## 1. Objective

Resolve the singular arithmetic deformation layer by replacing the ambient
inverse with an exact effective pencil at the cascade scale.

## 2. Scaling

Let `rho_N` be the low-cluster scale at the full arithmetic endpoint and put

```text
t=1-rho_N tau.                                        (2.1)
```

The load-bearing object is the Feshbach pencil

```text
K_N(tau)=rho_N^(-1)F_N(1-rho_N tau).                  (2.2)
```

## 3. Target

```text
LAYER-SCATTERING-ANCHOR:
the normalized bordered layer quotient converges to the effective pencil
scattering quotient, and its outer limit cancels the base-bulk deformation
defect in the relative Euler--Gamma determinant.                       (3.1)
```

## 4. Work order

```text
E88.001  exact Feshbach formula for the bordered numerator.
E88.002  abstract scaled-pencil limit theorem.
E88.003  tangent integral as a layer scattering quotient.
E88.004  parity scale split and single-scale falsifier.
```

## Outcome

Closed at exact-Feshbach and falsification grade; see [`PHASE_88_CLOSURE.md`](PHASE_88_CLOSURE.md) (“exact layer pencil and scale split”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: nested even and odd layer limits; their matching in the common scalar numerator; combined deformation RDI and Omega7.

## Contents

- `E88_001_EXACT_FESHBACH_LAYER.md` — E88.001 - Exact Feshbach formula for the layer numerator
- `E88_002_SCALED_PENCIL_LIMIT.md` — E88.002 - Abstract scaled-pencil limit theorem
- `E88_003_LAYER_SCATTERING_QUOTIENT.md` — E88.003 - Layer tangent integral as a scattering quotient
- `E88_004_PARITY_SCALE_SPLIT.md` — E88.004 - Parity scale split of the endpoint pencil
- `PHASE_88_CLOSURE.md` — Phase 88 closure - exact layer pencil and scale split

## Relation to other phases

Continues [`phase-87-euler-deformation-discriminant`](../phase-87-euler-deformation-discriminant/); its open target passes to [`phase-89-projective-layer-rotation`](../phase-89-projective-layer-rotation/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
