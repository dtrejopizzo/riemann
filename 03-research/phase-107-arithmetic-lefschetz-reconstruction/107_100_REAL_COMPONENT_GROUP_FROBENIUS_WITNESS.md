# 107.100 -- Real component-group Frobenius witness

## 1. Purpose

`107_93` through `107_99` established, on actual bad fibers of actual
elliptic curves over \(\mathbf Q\), that the current Paper A local row
sees only the scalar weight \(\log p\), while real target-side local
data contains affine fiber geometry, Tamagawa behavior, and finer
split/nonsplit labels.

This note isolates one more exact structural fact in that real local
chain:
for multiplicative fibers of Kodaira type \(I_n\), the geometric
component group is the cyclic group \(\mathbf Z/n\mathbf Z\), while the
arithmetic Tamagawa number \(c_p\) is the size of the Frobenius-fixed
subgroup.  So the missing local arithmetic datum is not another scalar
normalization; it is Frobenius action on the geometric component group.

## 2. Real objects used here

The verifier `107_100_real_component_group_frobenius_witness.py` uses
the same pinned local-data snapshots already confirmed from LMFDB for:

1. `14.a1 @ p=2`, with Kodaira type \(I_9\), nonsplit multiplicative,
   and Tamagawa number \(c_2=1\);
2. `14.a1 @ p=7`, with Kodaira type \(I_2\), split multiplicative, and
   Tamagawa number \(c_7=2\);
3. `14.a5 @ p=2`, with Kodaira type \(I_2\), nonsplit multiplicative,
   and Tamagawa number \(c_2=2\);
4. `489762.dv3 @ p=2`, with Kodaira type \(I_2\), split multiplicative,
   and Tamagawa number \(c_2=2\).

These are genuine multiplicative bad fibers of genuine elliptic curves
over \(\mathbf Q\).

## 3. Exact checks performed

The verifier:

1. builds the reduced Cartan matrix of type \(A_{n-1}\) for the
   geometric \(I_n\) fiber;
2. computes its Smith normal form exactly, verifying that the geometric
   component group has order \(n\) and cyclic structure
   \(\mathbf Z/n\mathbf Z\);
3. models the arithmetic Frobenius action on that cyclic group:
   trivial action in the split multiplicative case and inversion
   \(x\mapsto -x\) in the nonsplit multiplicative case;
4. computes the exact number of Frobenius-fixed elements, namely
   \(n\) in the split case and \(\gcd(2,n)\) in the nonsplit case;
5. checks on the four pinned real examples that those fixed-subgroup
   sizes agree exactly with the recorded Tamagawa numbers \(c_p\).

So the witness identifies the local arithmetic refinement of the
affine-Dynkin geometry in the multiplicative sector as

\[
 \text{geometric component group}
 \;+\;
 \text{Frobenius action}
 \longrightarrow
 c_p.
 \]

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All real component-group Frobenius checks passed.
```

So the workspace now contains an exact real local witness that
Tamagawa behavior in multiplicative fibers is produced by arithmetic
Frobenius on a real geometric component group, not by the scalar
\(\log p\) normalization alone.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. in the multiplicative real examples already pinned in the workspace,
   the gap between affine fiber geometry and arithmetic \(c_p\)-data is
   exactly explained by Frobenius action on the geometric component
   group;
2. the current local comparison problem can therefore be phrased more
   sharply: Phase 107 would need to recover not just a weighted
   intersection matrix, but the relevant local arithmetic action on the
   associated component data;
3. the real local benchmark is now stronger than a mere geometry-vs-log
   comparison, because it names the missing arithmetic mechanism.

It does **not** prove:

1. that the current Phase 107 source package recovers that Frobenius
   action;
2. any analogous statement for additive fibers;
3. any global realization theorem;
4. the terminal identity or RH.

So the correct reading is:

\[
 \text{multiplicative real component-group/Frobenius mechanism exact-checked},
 \qquad
 \text{full Phase 107 geometric realization still open}.
 \]
