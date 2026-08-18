# 114.a.98 — H7: scalar-invisible rigid bits exist, but full-bio probes kill the even moves

```
+-------------------------------------------------------------------------+
| BIT 0       Pair partition 12|34 under a color-1 root.                   |
| BIT 1       Pair partition 13|24 under the same root.                     |
| SAME SCALAR At x_1=...=x_4=1 both equal 2^(u+1) for every u.             |
| SAME FOLD   Both fold to x_1+x_2+x_3+x_4.                                |
| RIGID       Fixed input labels make the two partitions nonisomorphic.     |
| PROBE       On support {1,2}, bit 0 gives 2^u and bit 1 gives 2.          |
| NO-GO       Full-bio block extraction distinguishes any changed part, so  |
|             the required parity even moves cannot be equivalences.        |
| OPEN        Intrinsic rigidity without any extractable separating probe.  |
+-------------------------------------------------------------------------+
```

## 1. A scalar-invisible pair

On the fixed labelled input set `X={1,2,3,4}`, define

\[
 D_0=\delta_1\bigl(\delta_2(x_1,x_2),\delta_2(x_3,x_4)\bigr),
                                                                         \tag{1.1}
\]

\[
 D_1=\delta_1\bigl(\delta_2(x_1,x_3),\delta_2(x_2,x_4)\bigr).          \tag{1.2}
\]

Both have the same reduced colored-tree shape, but different labelled leaf
partitions.  An isomorphism in the operation set with fixed external inputs
must preserve the labels, so it cannot carry partition `12|34` to `13|24`.
The pair-probe theorem of `a73` gives the same distinction intrinsically.

Under the diagonal fold both operations become

\[
 x_1+x_2+x_3+x_4.                                                     \tag{1.3}
\]

In the positive real bio, put all inputs equal to one.  Each inner color-2
pair has value `2^u`, so

\[
 D_0(1,1,1,1)=2^{u+1}=D_1(1,1,1,1)                                  \tag{1.4}
\]

for every `u>0`.  Hence scalar all-ones weights do not distinguish the bits:
this pair passes the scalar ratio obstruction of `a97`.

## 2. Full-bio visibility

Evaluate on the Boolean vector of support `{1,2}`.  Then

\[
 D_0(1,1,0,0)=2^u,qquad D_1(1,1,0,0)=2.                             \tag{2.1}
\]

For `u>1` these values differ.  Thus the full higher-arity bio separates
the two decorations even though their unary scalar shadows agree.

This is exactly the partition-recovery mechanism of `a73`, extended to the
all-depth reconstruction of `a74`.

## 3. Consequence for parity even moves

Insert `D_0,D_1` as the two bits in each part of the parity skeleton.  A
putative even move, for example `000~011`, changes the bit in parts two and
three.  In any block-extractable product context, set the inputs in all
unchanged/unused parts to their neutral probes and apply (2.1) in part two.
The images differ, so the full-bio homomorphism forbids the equivalence.

### Proposition 3.1

No parity rigidification by independently extractable decorations separated
by a full-bio probe can realize all three even moves of `a94`.

### Proof

For a move changing parts `i,j`, extract part `i`.  Functoriality preserves
the alleged equality, but the separating probe gives different target
values.  Contradiction.  QED.

Therefore the explicit scalar-invisible pair (1.1)--(1.2) does not produce
parity endpoints.  It upgrades the remaining requirement to

> **H7-NONEXTRACTABLE-RIGID.** Find intrinsically nonisomorphic same-fold
> decorations that cannot be separated after any functorial block/sandwich
> extraction available in the parity context, while the three paired even
> replacements remain equivalent.

This condition lies precisely outside the block/read-once sectors already
closed by `a72`--`a75`: it must use genuinely entangled bilateral or repeated
contraction data.  Merely hiding the distinction from unary scalar moments
is insufficient.

The scalar-invisible read-once rigidification is closed negatively.
H7-NONEXTRACTABLE-RIGID, H7-PRIME-REG and row A remain open.

## 4. Verification scope

`114_a_98_h7_scalar_invisible_full_bio_verify.py` checks the two labelled
partitions, equal folds and all-ones values for several exact power models,
the Boolean pair separation, and the abstract block-extraction implication.
It enforces the negative scope and remaining gate.
