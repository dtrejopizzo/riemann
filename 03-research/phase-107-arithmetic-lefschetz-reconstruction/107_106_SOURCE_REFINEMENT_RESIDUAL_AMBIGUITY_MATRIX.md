# 107.106 -- Source refinement residual ambiguity matrix

## 1. Purpose

`107_105` exact-checks how many source classes arise from each minimal
refinement level

\[
 S_0<S_1<S_2<S_3.
 \]

This note records the complementary information:
which concrete local ambiguities still survive at each level.

The goal is not another class-count summary.  The goal is an exact
residual matrix for the pinned real local atlas.

## 2. Real rows used

The verifier `107_106_source_refinement_residual_ambiguity_matrix.py`
uses exactly the same seven real local rows as `107_105`:

1. `14.a1 @ p=2`, \(I_9\), \(c_2=1\), nonsplit multiplicative;
2. `14.a5 @ p=2`, \(I_2\), \(c_2=2\), nonsplit multiplicative;
3. `489762.dv3 @ p=2`, \(I_2\), \(c_2=2\), split multiplicative;
4. `20.a1 @ p=2`, \(IV\), \(c_2=1\), additive;
5. `36.a4 @ p=2`, \(IV\), \(c_2=3\), additive;
6. `36.a4 @ p=3`, \(III\), \(c_3=2\), additive;
7. `4225.m2 @ p=5`, \(III\), \(c_5=2\), additive.

## 3. Exact residual matrix

The verifier studies the same four source signatures:

1. \(S_0(row)=\log p\);
2. \(S_1(row)=(p,\text{Kodaira type})\);
3. \(S_2(row)=(p,\text{Kodaira type},c_p)\);
4. \(S_3(row)=(p,\text{Kodaira type},c_p,\text{reduction label})\).

It then records the exact surviving collisions.

### Level \(S_0\)

At \(p=2\), one source class still contains five distinct target rows:

\[
 I_9,\quad I_2^{\rm ns},\quad I_2^{\rm sp},\quad IV(c_p=1),\quad IV(c_p=3).
 \]

So \(S_0\) keeps the full local ambiguity at fixed prime.

### Level \(S_1\)

After adding Kodaira type, two nontrivial collisions remain:

1. the two \(IV\) rows at \(p=2\);
2. the two \(I_2\) rows at \(p=2\), still unresolved because geometry
   alone does not see split versus nonsplit reduction.

So geometry resolves the \(I_9\) separation from \(I_2\) and \(IV\), but
it still does not resolve either the \(IV\) difference in \(c_p\) or the
finer split/nonsplit distinction inside \(I_2\).

### Level \(S_2\)

After adding \(c_p\), only one nontrivial collision remains:
the two \(I_2\) rows with the same \(c_p=2\) but different split versus
nonsplit labels.

So \(c_p\) resolves the \(IV\) ambiguity, but not the finest
multiplicative local distinction.

### Level \(S_3\)

No nontrivial collision remains.

So \(S_3\) resolves every visible local ambiguity in the pinned atlas.

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All source refinement residual ambiguity checks passed.
```

So the workspace now contains an exact residual ambiguity table for the
current local source-refinement ladder.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. the local source gap is now described not only by class counts but
   by the exact residual collision pattern at each refinement level;
2. the next unresolved local obstruction after adding geometry is the
   \(IV\) \(c_p\)-ambiguity, and the next unresolved obstruction after
   adding \(c_p\) is the split/nonsplit `I_2` ambiguity;
3. future local upgrades of Paper A can now be checked against a
   precise residual matrix rather than only against total counts.

It does **not** prove:

1. that the present source package can realize any of these refinements;
2. that the pinned atlas exhausts all local phenomena relevant to Phase
   107;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{source refinement residual ambiguity matrix exact-checked},
 \qquad
 \text{full geometric realization still open}.
 \]
