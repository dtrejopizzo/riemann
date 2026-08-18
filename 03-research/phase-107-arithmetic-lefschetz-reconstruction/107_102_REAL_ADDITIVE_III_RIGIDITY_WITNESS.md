# 107.102 -- Real additive III rigidity witness

## 1. Purpose

`107_100` and `107_101` identified real local sectors where the affine
fiber geometry does not by itself determine the Tamagawa number:
one must also know the arithmetic Frobenius action on the geometric
component group.

This note records the complementary phenomenon for Kodaira type
\(III\): in this additive sector the geometric component group has order
\(2\), and the resulting arithmetic Tamagawa number is rigid in the
examples considered here.  So not every bad-fiber type carries the same
local arithmetic ambiguity.

## 2. Real objects used here

The verifier `107_102_real_additive_iii_rigidity_witness.py` uses the
following real local rows already visible on LMFDB:

1. `36.a4 @ p=3`, with Tamagawa number \(c_3=2\), Kodaira type
   \(III\), and additive reduction;
2. `4225.m2 @ p=5`, with Tamagawa number \(c_5=2\), Kodaira type
   \(III\), and additive reduction.

These are genuine additive bad fibers of genuine elliptic curves over
\(\mathbf Q\).

## 3. Exact checks performed

The verifier:

1. writes the affine \(A_1\) component-intersection matrix of the
   geometric \(III\) fiber exactly;
2. computes the reduced Cartan matrix of type \(A_1\) and its Smith
   normal form, verifying that the geometric component group has cyclic
   order \(2\);
3. checks that the only automorphism of that cyclic group preserves the
   full group, so the fixed subgroup also has size \(2\);
4. verifies on the two pinned real examples that the observed local
   Tamagawa number is exactly \(c_p=2\).

So the witness records the rigid local pattern

\[
 \text{geometric }A_1\text{ fiber}
 \longrightarrow
 \mathbf Z/2\mathbf Z
 \longrightarrow
 c_p=2.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real additive III rigidity checks passed.
```

So the workspace now contains a complementary real local witness: some
bad-fiber types exhibit genuine geometry-to-\(c_p\) arithmetic freedom,
while others are rigid once the geometry is fixed.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the local comparison problem of Phase 107 is type-sensitive even on
   genuine elliptic bad fibers over \(\mathbf Q\);
2. the additive type \(III\) examples used here do not show the same
   extra local ambiguity that appears for multiplicative \(I_n\) and
   additive \(IV\);
3. Phase 107 now has real local witnesses for both flexible and rigid
   Kodaira sectors.

It does **not** prove:

1. that every \(III\) fiber over \(\mathbf Q\) must behave identically
   in every arithmetic refinement of interest;
2. any analogous statement for all additive Kodaira types;
3. that the current Phase 107 source package recovers this rigidity;
4. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{real additive }III\text{ rigidity exact-checked},
 \qquad
 \text{full Phase 107 geometric realization still open}.
 \]
