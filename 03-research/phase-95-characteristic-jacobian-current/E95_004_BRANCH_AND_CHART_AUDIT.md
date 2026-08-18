# E95.004 - Branch and chart audit

## 1. Simple branch intervals

On an interval where `partial_mu chi` and the four safe numerator values are
nonzero, E95.003 integrates to

```text
log[W_(t_1)(s;s_*)/W_(t_0)(s;s_*)]
 =integral_(t_0)^(t_1) BJ_t(s;s_*)dt.                (1.1)
```

## 2. Safe chart zeros

If one safe numerator value vanishes, the projective determinant is not
singular; only the chosen logarithmic chart is.  Replace `z_*` by another safe
evaluation and use the overlap ratio.  Endpoint quotients are defined
algebraically without integrating through a chart zero.

## 3. Multiple characteristic level

If

```text
partial_mu chi(t_0,mu_0)=0,                          (3.1)
```

formula E95.002(2.2) is not a valid single-branch coordinate.  The bordered
polynomial `P(t,mu,z)` and the characteristic equation remain defined.  A
proof must either

```text
1. prove simplicity of the selected finite branch on the integration path;
2. subdivide through an analytic spectral cluster and use its determinant;
3. compare endpoint projective values without a tangent parameterization. (3.2)
```

No division by `partial_mu chi` is permitted at a multiple point.

## 4. Decision

The Jacobian current removes the moving-level derivative but does not prove
branch simplicity.  The direct endpoint quotient of Phase 92 remains the
canonical formulation; E95.003 is its local algebraic coordinate.

## 5. Status

```text
proved:
  exact chart transition principle;
  precise validity domain of the Jacobian current;

open only if a tangent proof is used:
  simplicity or cluster passage along t.
```

