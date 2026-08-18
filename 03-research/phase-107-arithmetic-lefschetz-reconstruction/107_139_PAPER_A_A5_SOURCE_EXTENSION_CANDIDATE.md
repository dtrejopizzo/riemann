# 107.139 -- Paper A A5 source-extension candidate

## 1. Purpose

`107_138` formalized the local planning state of Paper A as

\[
\text{legacy row (c): closed},\qquad
\text{A5: live branch}.
\]

The next useful move is no longer another governance gate.
It is the first **positive** local source candidate written in Paper A
language.

This note proposes the minimal extension:

\[
\mathcal S_{A5}(row)=
\bigl(\mathcal S_{\mathrm{legacy}}(row),\rho_{32}(row)\bigr),
\]

where

\[
\mathcal S_{\mathrm{legacy}}(row)=
(\Lambda(p),\log p,p^{-1/2},a_p,L_p^{\mathrm{loc}})
\]

is the current finite source-rule packet, and
\(\rho_{32}(row)\) is the residue class modulo \(32\) of the local
minimal-model Weierstrass coefficient tuple.

## 2. What this candidate is claiming

This candidate is deliberately modest.
It does **not** claim that \(\rho_{32}\) has already been derived from
the prime/Gamma/pole grammar of `107.00`.

It claims only that:

1. adjoining \(\rho_{32}\) gives a genuine refinement of the current
   source packet;
2. this refinement cures the visible local target failures already
   exposed in the workspace.

That is the right first step for a live new branch.

## 3. Real tests performed

The verifier checks three exact conditions.

### 3.1 Atlas separation

On the fixed real atlas used by `107_134`, no two elliptic rows with the
same extended packet \(\mathcal S_{A5}\) may land in different visible
target states.

### 3.2 Family-level additive cleanliness

On the enlarged additive \(IV^\ast\) family at \(p=2\) used by
`107_135`, no one extended packet may mix curves with different
\(c_p\).

### 3.3 Genuine refinement of the legacy packet

On that same enlarged family, the verifier also checks that the new
symbol \(\rho_{32}\) really does refine the legacy packet rather than
restate it trivially.
Concretely, at least one legacy packet class must split into multiple
\(\rho_{32}\)-classes.

## 4. Exact output

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_SIZE: 6
HAS_GENUS_GE_2_CONTROL: True
HAS_SUPERSINGULAR_CONTROL: True
ATLAS_COLLISIONS: 0
FAMILY_ROWS: 285
FAMILY_MIXED_EXTENSION_CLASSES: 0
LEGACY_CLASSES_REFINED_BY_RHO32: 1

VERDICT: YES
```

So this first source-extension candidate passes the visible real tests
currently available.

## 5. Consequence

This does **not** prove that Paper A is solved locally.
It proves something narrower and very useful:

1. there is now a concrete source-extension candidate for the `A5`
   branch, not just a surviving target-side packet;
2. that candidate is a real refinement of the legacy source packet;
3. on the fixed atlas and the enlarged additive family, it removes the
   visible collisions of the closed legacy route.

So the correct reading is:

\[
\text{Paper A now has its first positive A5 source candidate:}
\]
\[
\text{legacy packet plus the new residue symbol }\rho_{32}.
\]
