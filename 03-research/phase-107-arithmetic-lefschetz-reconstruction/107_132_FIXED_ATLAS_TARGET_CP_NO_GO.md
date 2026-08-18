# 107.132 -- Fixed real atlas target-with-\(c_p\) no-go

## 1. Purpose

The `107_123`--`107_127` chain already exposed the decisive local
forcing pair

\[
20a1@2,\qquad 36a4@2,
\]

but the next tranche imposed a stricter delivery rule:

1. the atlas must be fixed before calculation;
2. it must contain at least five real curves;
3. it must include at least one genus-\(\ge 2\) curve and one
   supersingular case;
4. the artifact must return one binary verdict on \(S_3\).

This note packages the current local obstruction in exactly that form.

## 2. Fixed atlas

The verifier fixes the following five real curve inputs before running
any calculation:

1. `20a1 @ 2` — elliptic forcing row, additive \(IV^\ast\);
2. `36a4 @ 2` — elliptic forcing row, additive \(IV^\ast\);
3. `14a1 @ 5` — elliptic supersingular control, good reduction with
   \(a_5=0\);
4. `11a1 @ 5` — elliptic ordinary control, good reduction with
   \(a_5=1\);
5. `y^2=x^5+x+1 @ 5` — hyperelliptic genus-\(2\) control.

So the atlas satisfies the tranche constraints before any source/target
comparison is made.

## 3. Current source and target used

For elliptic local rows, the verifier records the current finite
source-rule packet tested in the recent local chain:

\[
\mathcal S_{\mathrm{rule}}(row)=
\bigl(\log p,\log p,p^{-1/2},a_p,L_p^{\mathrm{flag}}\bigr),
\]

with \(L_p^{\mathrm{flag}}=1\) in the additive forcing case and
`euler` otherwise.

The current local target in the workspace remains

\[
T_{\mathrm{current}}(row)=
(\text{Kodaira symbol},c_p,\text{reduction label}).
\]

That is not a new choice made in this note; it is the target already
used in `107_104`, `107_117`--`107_127`.

## 4. Exact forcing collision on the fixed atlas

On the forcing pair, Sage computes:

\[
T_{\mathrm{current}}(20a1@2)=(IV^\ast,3,\text{additive}),
\]
\[
T_{\mathrm{current}}(36a4@2)=(IV^\ast,1,\text{additive}),
\]

while the current source packets coincide exactly:

\[
\mathcal S_{\mathrm{rule}}(20a1@2)=
\mathcal S_{\mathrm{rule}}(36a4@2)=
(\log 2,\log 2,2^{-1/2},0,1).
\]

So inside the fixed atlas:

1. the forcing pair has the same prime;
2. the same Kodaira symbol;
3. the same reduction label;
4. different \(c_p\);
5. identical current source-rule packets.

That is precisely the obstruction.

## 5. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_SIZE: 5
HAS_GENUS_GE_2: True
HAS_SUPERSINGULAR_CONTROL: True
FORCING_PAIR_SAME_SOURCE: True
FORCING_PAIR_SAME_KODAIRA: True
FORCING_PAIR_SAME_REDUCTION: True
FORCING_PAIR_DIFFERENT_CP: True
FORCING_PAIR_DIFFERENT_TARGET: True

VERDICT: NO
```

Here `NO` means:
the current Phase 107 finite local source rule does **not** reach the
current \(S_3\)-level local target on the fixed real atlas.

## 6. Consequence

This closes the design fork for the **current** target definition.

If Phase 107 keeps

\[
(\text{Kodaira symbol},c_p,\text{reduction label})
\]

as its local target, then the current prime/Gamma/pole finite source
vocabulary is already blocked on real data.

So the next step is no longer another valuative or Eulerian refinement
of the same source grammar.
Either:

1. a genuinely new Galois-sensitive source channel is constructed; or
2. row (c) is closed by no-go for the current target design.

For the current workspace target, this note records the second outcome
locally and exactly on a tranche-compliant atlas.
