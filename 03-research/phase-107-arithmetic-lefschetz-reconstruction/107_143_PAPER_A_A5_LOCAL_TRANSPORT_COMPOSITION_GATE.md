# 107.143 -- Paper A A5 local transport/composition gate

## 1. Purpose

`107_142` showed that the residue decoration \(\rho_{32}\) admits a
first difference cocycle

\[
\delta_{32}(row_1,row_2)=\rho_{32}(row_1)-\rho_{32}(row_2)\pmod{32}.
\]

The next local structural question is whether this can already be read
as a transport/composition law for refined local arrows in the `A5`
branch.

This note tests exactly that.

## 2. Candidate local arrows

For visible local rows, define the refined arrow

\[
\mathsf A_{A5}(row_1,row_2)=\delta_{32}(row_1,row_2).
\]

The proposed laws are:

1. **transport/composition**
   \[
   \mathsf A_{A5}(row_1,row_2)+\mathsf A_{A5}(row_2,row_3)
   =
   \mathsf A_{A5}(row_1,row_3);
   \]
2. **inverse under reversal**
   \[
   \mathsf A_{A5}(row_2,row_1)=-\mathsf A_{A5}(row_1,row_2).
   \]

These are the first concrete transport laws one would expect before any
full derived composition theorem is even formulated.

## 3. Exact output

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_ROWS: 4
FAMILY_ROWS: 285
TRANSPORT_OK: True
INVERSE_OK: True
CP_ARROW_NONTRIVIAL: True
SPLIT_ARROW_NONTRIVIAL: True

VERDICT: YES
```

So the refined local arrows satisfy the tested transport laws on real
data.

## 4. Consequence

This does **not** prove the full compatibility of `A5` with the
decorated correspondence composition of Paper B.
It proves the local precursor:

1. the `A5` decoration can already be organized as nontrivial local
   arrows;
2. those arrows compose additively on sampled real triples;
3. reversal gives the expected inverse arrow.

So the correct reading is:

\[
\text{the A5 branch now has a first tested local transport/composition}
\]
\[
\text{law, not just a residue label or a static cocycle.}
\]
