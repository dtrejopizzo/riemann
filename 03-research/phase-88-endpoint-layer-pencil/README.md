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
