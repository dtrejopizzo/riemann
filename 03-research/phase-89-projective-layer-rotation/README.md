# Phase 89 - Projective layer rotation

## 1. Objective

Determine which part of the nested endpoint layer survives after the
projective normalization required by RDI.

## 2. Main observation

The dominant resonant contribution has the form

```text
G_t(z)
 =-[h_(t,z)^eff p_t][p_t^T b_t^eff]/lambda_t
  +remainder.                                         (2.1)
```

The eigenvalue and boundary overlap are independent of `z`.  They disappear
from normalized safe ratios.  Only the lifted Cauchy profile
`h_z tilde p_t=h_(t,z)^eff p_t` can carry a nontrivial layer current.

## 3. Work order

```text
E89.001  projective dominance theorem.
E89.002  cancellation of scalar resonance factors.
E89.003  exact profile-rotation current.
E89.004  endpoint dominance audit and final layer target.
E89.005  exact crosswalk from the layer profile to LP and IDENT.
```

## 4. Phase result

The eigenvalue cascade is normalization data.  After projective
normalization, the surviving endpoint object is exactly the safe Cauchy
profile already present in LP and IDENT.  The next phase expands its
base-point-subtracted Kato current in the prime-shift algebra.
