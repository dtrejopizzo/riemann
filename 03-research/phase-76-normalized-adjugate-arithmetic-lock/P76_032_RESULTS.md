# P76.032 - Legacy-cache precision autopsy

The legacy Phase-61 cache produced growing zeta errors and enormous
Davenport-Heilbronn errors for the bilateral safe-axis observable.  These
numbers are not admissible evidence for `SA-SAFE` because an entry-level
comparison found discrepancies of approximately `5e-18` between the cached
matrices and the Phase-76 multiprecision builder.

That discrepancy is tiny on the `O(1e-2)` entry scale but enormous relative
to the lowest CCM eigenvalues and gaps.  The boundary Schur solve amplifies
it.  The cache also stores `L` as a binary float even though its matrices are
decimal strings.

Decision:

```text
legacy cache: suitable for coarse entry/spectral diagnostics;
legacy cache: rejected for boundary-characteristic scaling;
SA-SAFE scaling: must rebuild every entry and L at working precision.
```

The cache experiment remains useful as a precision falsifier: the bilateral
observable discriminates DH dramatically, but it cannot certify zeta
asymptotics under contaminated low spectral data.
