# D.166 — Directed nested finite certificate at (N=200)

## Scope

This certificate proves strict positivity of the endpoint operator restricted
to the exact two-Tate-moment polynomial space (V_{200}).  It does **not**
estimate the coupling to the infinite-dimensional complement (Q_{200}).

The decomposition used by the certificate is

\[
 V_{200}=D_5\oplus S_{163}\oplus Y_{30},
\]

where (D_5) is the endpoint-flat dangerous frame, (S_{163}) is its exact
orthogonal complement inside (V_{170}), and (Y_{30}) is the exact
orthogonal complement of (V_{170}) inside (V_{200}).  Both Tate moments
are imposed by an Arb two-by-two graph solve.

The archimedean Gamma block is assembled from the directed Hurwitz--Lerch
formula at 1700 decimal digits.  The finite contacts use the directed,
polynomial-exact Gauss enclosure.  Every Schur complement is formed with Arb
matrix arithmetic.  Positivity is certified by a floating Cholesky
preconditioner followed by an interval Gershgorin test; the floating
eigenvalues below are diagnostics only.

## Directed result

| block | smallest centre eigenvalue | directed Gershgorin lower enclosure |
|---|---:|---:|
| shell (Y_{30}) | (3.27356009) | ([0.9999999999999995\mathbin{+/-}7.08\cdot10^{-17}]) |
| safe Schur (S_{163}) | (0.05844291) | ([1.000000000000\mathbin{+/-}8.08\cdot10^{-14}]) |
| final Schur (D_5) | (3.11556559\cdot10^{-12}) | ([1.00\mathbin{+/-}1.72\cdot10^{-4}]) |

The five centre eigenvalues of the last Schur complement are

\[
3.11556559\cdot10^{-12},\quad
6.25443534\cdot10^{-10},\quad
3.11761665\cdot10^{-7},\quad
3.12478861\cdot10^{-5},\quad
2.10421920\cdot10^{-3}.
\]

All three directed lower endpoints are strictly positive.  In particular,
the interval solves did not widen catastrophically.

## Reproduction

```bash
PYTHONPATH=/tmp/d61-flint D166_DPS=1700 \
python3 114_d_166_nested200_directed_schur.py
```

The script writes midpoint data to
`/tmp/d166_nested200_centres.npz` only for subsequent diagnostics.  Those
binary64 midpoints are not part of this positivity proof.

## Remaining endpoint obligation

The result is a finite-section theorem.  Closing the endpoint additionally
requires a directed bound for the projected coupling

\[
 Q_{200} A P_{200}
\]

on the five-dimensional dangerous graph after the two safe finite Schur
eliminations, together with the already available positive lower bound on
the (Q_{200}) block.  No ambient second-moment identity is used here: such
an identity would omit the intervening Tate projection.
