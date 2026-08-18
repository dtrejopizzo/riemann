# Phase 85 - Parity Weyl defect

## 1. Objective

Resolve the safe reduced response left by Phase 84 without replacing it by an
ambient inverse estimate.

The exact target is

```text
COFINAL-PARITY-CLUSTER:
choose a cofinal parity-balanced spectral cluster for which the two safe
parity responses of C^(-1)QD Mg vanish locally uniformly, together with one
safe derivative.                                      (1.1)
```

## 2. Strategy

The rank-two displacement equation determines every matrix element of `D`
between eigenvectors of opposite parity.  This converts the reduced response
into two normalized finite Weyl defects.  No eigenvector matrix element of
`D` remains unknown.

## 3. Work order

```text
E85.001  exact spectral-ratio formula.
E85.002  normalized Weyl-defect form.
E85.003  separation of the two defects on the safe axis.
E85.004  cofinal cluster criteria and obstruction audit.
```

