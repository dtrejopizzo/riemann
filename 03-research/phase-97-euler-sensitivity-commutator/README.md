# Phase 97 - Euler sensitivity commutator

## 1. Objective

Sum the determinantal prime-response kernel before estimation by representing
it as the trace pairing of the prime connection with one canonical
determinantal sensitivity.

## 2. Main identity

For

```text
A=Z^(-1)[X,Z],
H_P=A+A^*,                                            (2.1)
```

and every finite sensitivity matrix `K`, cyclicity of the trace converts
`Tr(KH_P)` into two commutators of `K` with the Euler unit and its adjoint.

## 3. Work order

```text
E97.001  characteristic-constrained sensitivity;
E97.002  Euler trace-commutator identity;
E97.003  bilateral determinant application;
E97.004  adjugate commutator polynomial;
E97.005  canonical safe boundary target.
E97.006  finite certification of trace and adjugate signs.
```

## Outcome

Closed; see [`PHASE_97_CLOSURE.md`](PHASE_97_CLOSURE.md) (“Prime sum collapsed to one boundary commutator”). No positivity statement toward Ω7 is proved here; the phase is an exact reduction.
Open items carried forward: `SAFE-DETERMINANT-BOUNDARY`; DIRECT-BORDERED-ANCHOR and Omega7.

## Contents

- `E97_001_CONSTRAINED_SENSITIVITY.md` — E97.001 - Characteristic-constrained sensitivity
- `E97_002_EULER_TRACE_IDENTITY.md` — E97.002 - Euler trace-commutator identity
- `E97_003_BILATERAL_COMMUTATOR_CURRENT.md` — E97.003 - Bilateral commutator current
- `E97_004_ADJUGATE_COMMUTATOR_POLYNOMIAL.md` — E97.004 - Adjugate commutator polynomial
- `E97_005_CANONICAL_BOUNDARY_TARGET.md` — E97.005 - Canonical determinant boundary target
- `E97_006_FINITE_TRACE_CERTIFICATION.md` — E97.006 - Finite trace certification
- `PHASE_97_CLOSURE.md` — Phase 97 closure - Prime sum collapsed to one boundary commutator

## Relation to other phases

Continues [`phase-96-determinantal-prime-response`](../phase-96-determinantal-prime-response/); its open target passes to [`phase-98-sensitivity-shell-split`](../phase-98-sensitivity-shell-split/). The chain of phases 80–101 is the finite real-rooted CCM route to Ω7 (the Li–Keiper positivity statement), opened in phases 71–79.
