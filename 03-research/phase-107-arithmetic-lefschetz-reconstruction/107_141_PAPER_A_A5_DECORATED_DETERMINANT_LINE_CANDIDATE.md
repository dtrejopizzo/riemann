# 107.141 -- Paper A A5 decorated determinant-line candidate

## 1. Purpose

`107_140` gave the `A5` branch its first refined local generators and
line labels.
The next step is to phrase that refinement in language closer to the
determinant-line perspective of `107_04`.

This note proposes a first candidate of the form

\[
\mathcal D_{A5}(row)=
\bigl(\mathcal D_{\mathrm{legacy}}(row),\rho_{32}(row)\bigr),
\]

where \(\mathcal D_{\mathrm{legacy}}(row)\) is the visible finite scalar
projection inherited from the legacy local source packet, and
\(\rho_{32}(row)\) is the new residue decoration.

The intention is simple:

1. the legacy determinant/scalar projection should remain intact;
2. the new decoration should split the real family that legacy support
   cannot separate.

## 2. Exact tests

The verifier checks three real conditions.

### 2.1 Atlas separation

On the fixed visible atlas, equal decorated lines must not land in
different visible target states.

### 2.2 Family purity

On the enlarged additive \(IV^\ast\) family at \(p=2\), no decorated
class may mix different \(c_p\)-values.

### 2.3 Scalar compatibility

On that same family, the legacy scalar projection must remain constant,
while the decorated classes must refine it into multiple
\(\rho_{32}\)-subclasses.

## 3. Exact output

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_COLLISIONS: 0
FAMILY_ROWS: 285
MIXED_DECORATED_CLASSES: 0
REFINED_SCALAR_CLASSES: 1
SCALAR_PROJECTION_CONSTANT_ON_IVSTAR: True

VERDICT: YES
```

So the candidate passes the visible real tests now available.

## 4. Consequence

This still does **not** prove a full determinant theorem for the `A5`
branch.
But it proves the first axiomatic compatibility expected from one:

1. the refined object forgets to the same legacy scalar/determinantal
   projection;
2. the residue decoration splits the real blind class rather than
   altering the visible legacy order law;
3. so the `A5` branch can now be read as a decorated determinant-line
   refinement, not merely as an external label.

So the correct reading is:

\[
\text{the A5 branch now has a first decorated determinant-line}
\]
\[
\text{candidate compatible with the legacy projection and tested on}
\]
\[
\text{real data.}
\]
