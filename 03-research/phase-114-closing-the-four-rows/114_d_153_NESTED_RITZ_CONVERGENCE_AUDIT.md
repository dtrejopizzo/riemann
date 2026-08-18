# D.153 — Exploratory nested Ritz audit at N=200

## Scope

This is a convergence diagnostic, not an interval certificate and not a
statement about the full endpoint.  It uses the directed D.147/D.100 matrix
assembly, but reports binary64 eigenvalues after orthonormalizing the exact
Tate graph.

## Run

- `N=200`, Gamma precision: 1700 decimal digits.
- Polynomial-exact directed contacts: 2048 bits.
- Contact assembly: 758.75 seconds, 62.6 MB maximum RSS.
- Gamma, Tate graph, Ritz extraction and congruence: 269.63 seconds,
  380.8 MB maximum RSS.
- Saved data: `/tmp/d153_nested200.npz`, containing the completed Legendre
  centre `A`, Tate graph `Z`, physical Ritz values, and physical Legendre
  coefficient vectors.

The first physical constrained Ritz values at `N=200` are

```text
3.11336437e-12
6.25444560e-10
3.11759310e-07
3.12085199e-05
2.08735114e-03
5.85139876e-02
```

The smallest graph-coordinate value was `3.11323303e-12`.  Graph-coordinate
eigenvalues are not physical Ritz values; they are used only by the directed
positivity congruence.

## Nested trend

Using leading principal blocks of the same completed `A_200` and the
corresponding truncated exact Tate graph gives the following approximate
smallest physical Ritz values:

| N | smallest Ritz value |
|---:|---:|
| 80  | `3.180e-12` |
| 120 | `3.146e-12` |
| 150 | `3.128e-12` |
| 170 | `3.122e-12` |
| 200 | `3.113e-12` |

The sequence is still falling slowly and therefore is not numerically fully
converged, but it remains on the same positive scale.  Binary64 diagonalizing
errors affect approximately the last `1e-15` in the smallest value.

## N=170 to N=200 shell diagnostic

For the lowest physical `N=170` Ritz vector, extended by zero to 200 modes,

\[
 \|(P_{200}-P_{170})A v_{170}\|^2
 =2.3949949804328049\times10^{-14}.
\]

This is below `0.218 * 3.12e-12 = 6.8016e-13` by a factor of about 28.4.
It measures only modes 170 through 199; the shell beyond mode 199 remains
unmeasured and must not be inferred from this finite audit.

## Verdict

The `N=170` small margin is not a visibly unstable truncation artifact, but
the monotone-scale decrease has not stopped.  The data support proceeding to
the rigorous Feshbach residual bound; they do not replace it.
