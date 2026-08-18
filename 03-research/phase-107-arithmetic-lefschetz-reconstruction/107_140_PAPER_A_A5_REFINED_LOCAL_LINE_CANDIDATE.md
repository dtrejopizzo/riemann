# 107.140 -- Paper A A5 refined local-line candidate

## 1. Purpose

`107_139` produced the first positive source-side packet for the `A5`
branch:

\[
\mathcal S_{A5}=(\mathcal S_{\mathrm{legacy}},\rho_{32}).
\]

The next step is to push that one notch closer to the language of
`107_04`, where the central object is not merely a packet but a
finite-place line attached to local generators.

This note proposes the first refined local object:

1. replace a legacy local generator by a refined generator carrying the
   extra residue symbol \(\rho_{32}\);
2. define the refined local line label as the ordered pair of those
   refined generators;
3. require that forgetting \(\rho_{32}\) recovers the same legacy
   support class.

## 2. Candidate object

For a visible elliptic local row, define the refined generator

\[
G_{A5}(row)=
\bigl(\mathcal S_{\mathrm{legacy}}(row),\rho_{32}(row)\bigr).
\]

The corresponding refined local line label is

\[
\mathcal L_{A5}(row_1,row_2)=
\bigl(G_{A5}(row_1),G_{A5}(row_2)\bigr).
\]

This is still only a candidate source object, not yet a derived
determinant line theorem.
Its purpose is to record explicitly how the new residue symbol enters
the local Paper A objects.

## 3. Exact tests

The verifier checks two things on real data.

### 3.1 Visible target separation on the fixed atlas

On the fixed atlas, equal refined generators must not land in different
visible target states.

### 3.2 Genuine refinement of one legacy support class

On the enlarged additive \(IV^\ast\) family at \(p=2\), the verifier
checks that one legacy source class really does split into multiple
refined generators, so the new line labels preserve the old support
class while resolving its hidden arithmetic ambiguity.

## 4. Exact output

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_ROWS: 4
ATLAS_COLLISIONS: 0
FAMILY_ROWS: 285
LEGACY_CLASSES_SPLIT_BY_RHO32: 1
SAMPLE_LINE_SUPPORT_OK: True

VERDICT: YES
```

So the first refined local-line candidate passes the visible tests now
available.

## 5. Consequence

This does **not** yet prove the full local determinant theory of the
`A5` branch.
It proves the first object-level statement one step above `107_139`:

1. the new residue symbol \(\rho_{32}\) can be attached directly to the
   local generator level of Paper A;
2. doing so preserves the underlying legacy support class;
3. while splitting exactly the real family on which the old local route
   was blind.

So the correct reading is:

\[
\text{the A5 branch now has not only a source packet but also a first}
\]
\[
\text{refined local-generator/line candidate compatible with the}
\]
\[
\text{Paper A viewpoint of }107.04.
\]
