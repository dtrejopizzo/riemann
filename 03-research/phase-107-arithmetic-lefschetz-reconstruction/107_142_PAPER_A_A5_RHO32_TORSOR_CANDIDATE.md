# 107.142 -- Paper A A5 rho_32 torsor candidate

## 1. Purpose

`107_141` proposed the first decorated determinant-line candidate for
the `A5` branch:

\[
\mathcal D_{A5}(row)=
\bigl(\mathcal D_{\mathrm{legacy}}(row),\rho_{32}(row)\bigr).
\]

The next structural question is whether the new residue decoration can
already be treated as more than a passive label.

This note proposes the first torsor/cocycle-style law:

\[
\delta_{32}(row_1,row_2)=
\rho_{32}(row_1)-\rho_{32}(row_2)\pmod{32}.
\]

## 2. Candidate laws

The verifier tests the following exact properties on real data.

1. **Transpose law**
   \[
   \delta_{32}(row_2,row_1)=-\delta_{32}(row_1,row_2).
   \]
2. **Cocycle law**
   \[
   \delta_{32}(row_1,row_2)+\delta_{32}(row_2,row_3)
   =\delta_{32}(row_1,row_3).
   \]
3. **Zero-kernel law**
   \[
   \delta_{32}(row_1,row_2)=0
   \Longleftrightarrow
   \rho_{32}(row_1)=\rho_{32}(row_2).
   \]

These are the first compatibility laws one would expect if `rho_32`
were eventually to define a meaningful local decoration/torsor over the
legacy determinant-line picture.

## 3. Exact output

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_ROWS: 4
FAMILY_ROWS: 285
TRANSPOSE_OK: True
COCYCLE_OK: True
ZERO_KERNEL_OK: True
CP_PAIR_DELTA_NONZERO: True
SPLIT_PAIR_DELTA_NONZERO: True

VERDICT: YES
```

So the first torsor-style laws pass on the current real tests.

## 4. Consequence

This still does **not** prove that the `A5` branch has a full derived
determinant theory.
It proves the next structural step:

1. `rho_32` can already be organized as a difference decoration, not
   just a list of residues;
2. that difference decoration is compatible with reversal and with a
   first cocycle law on sampled real triples;
3. so the branch now supports a first genuinely algebraic compatibility
   pattern on top of the legacy determinant-line projection.

So the correct reading is:

\[
\text{the A5 branch now has a first tested torsor/cocycle candidate}
\]
\[
\text{for its local residue decoration.}
\]
