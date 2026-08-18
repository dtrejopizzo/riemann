# 107.101 -- Real additive IV Frobenius witness

## 1. Purpose

`107_100` identified, for real multiplicative fibers \(I_n\), the
precise arithmetic mechanism behind the gap between affine geometry and
the Tamagawa number: the geometric component group is
\(\mathbf Z/n\mathbf Z\), and \(c_p\) is the size of the subgroup fixed
by Frobenius.

This note extends that mechanism to one genuinely additive case on
actual elliptic curves over \(\mathbf Q\):
Kodaira type \(IV\).  The geometric special fiber is the affine
\(A_2\) triangle, whose geometric component group has order \(3\).  The
real arithmetic Tamagawa number then depends on how Frobenius acts on
that triangle: trivial action gives \(c_p=3\), while a 3-cycle gives
\(c_p=1\).

## 2. Real objects used here

The verifier `107_101_real_additive_iv_frobenius_witness.py` uses the
following pinned local-data snapshots from LMFDB:

1. `20.a1 @ p=2`, with Tamagawa number \(c_2=1\), Kodaira type \(IV\),
   and additive reduction;
2. `36.a4 @ p=2`, with Tamagawa number \(c_2=3\), Kodaira type \(IV\),
   and additive reduction.

These are genuine additive bad fibers of genuine elliptic curves over
\(\mathbf Q\).

## 3. Exact checks performed

The verifier:

1. writes the affine \(A_2\) component-intersection matrix of the
   geometric \(IV\) fiber exactly;
2. computes the reduced Cartan matrix of type \(A_2\) and its Smith
   normal form, verifying that the geometric component group has cyclic
   order \(3\);
3. models two arithmetic Frobenius actions on the triangle:
   the trivial action and a 3-cycle permutation of the non-identity
   components;
4. computes the exact number of fixed elements in the geometric
   component group under each action, obtaining \(3\) in the trivial
   case and \(1\) in the 3-cycle case;
5. checks that those two fixed-subgroup sizes agree exactly with the
   real local Tamagawa numbers of `36.a4 @ p=2` and `20.a1 @ p=2`.

So the additive \(IV\) local mechanism is recorded as

\[
 \text{geometric }A_2\text{ triangle}
 \;+\;
 \text{Frobenius action}
 \longrightarrow
 c_p.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real additive IV Frobenius checks passed.
```

So the workspace now contains an additive real local witness showing
that the geometry-to-\(c_p\) refinement is again arithmetic Frobenius on
geometric component data, not a second scalar normalization.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the “geometry + Frobenius action = local arithmetic” mechanism of
   `107_100` is not confined to multiplicative fibers; it already
   appears on a concrete additive \(IV\) pair over \(\mathbf Q\);
2. Phase 107 now has real local arithmetic witnesses in both a
   multiplicative and an additive Kodaira sector;
3. the local comparison problem is sharpened further: reproducing a
   bad-fiber matrix is still not enough unless the source package also
   recovers the arithmetic action on the associated component data.

It does **not** prove:

1. an analogous statement for every additive Kodaira type;
2. that the current Phase 107 source package recovers this additive
   Frobenius action;
3. any global realization theorem;
4. the terminal identity or RH.

So the correct reading is:

\[
 \text{real additive }IV\text{ component/Frobenius mechanism exact-checked},
 \qquad
 \text{full Phase 107 geometric realization still open}.
 \]
