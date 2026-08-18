# 107.105 -- Minimal source refinement ladder

## 1. Purpose

`107_104` exact-checks the current local blindness of the present
finite-place source row of `107_04`: on the pinned real examples, the
source still distinguishes only the prime through \(\log p\).

This note records the next exact question:
what is the smallest kind of additional source information that would
resolve each layer of the current real local target atlas?

The point is not to claim that Phase 107 already has these refinements.
The point is to identify a sharp ladder of minimal improvements.

## 2. Real local states used

The verifier `107_105_minimal_source_refinement_ladder.py` uses the same
real local states already fixed in `107_104`:

1. `14.a1 @ p=2`, \(I_9\), \(c_2=1\), nonsplit multiplicative;
2. `14.a5 @ p=2`, \(I_2\), \(c_2=2\), nonsplit multiplicative;
3. `489762.dv3 @ p=2`, \(I_2\), \(c_2=2\), split multiplicative;
4. `20.a1 @ p=2`, \(IV\), \(c_2=1\), additive;
5. `36.a4 @ p=2`, \(IV\), \(c_2=3\), additive;
6. `36.a4 @ p=3`, \(III\), \(c_3=2\), additive;
7. `4225.m2 @ p=5`, \(III\), \(c_5=2\), additive.

## 3. Exact refinement ladder

The verifier compares four signatures.

### Level 0: current Phase 107 source row

\[
 S_0(row)=\log p.
 \]

This is the current behavior of `107_04`.

### Level 1: geometric source refinement

\[
 S_1(row)=(p,\text{Kodaira type}).
 \]

This is the smallest refinement that would distinguish the presently
visible geometric sectors above a fixed prime.

### Level 2: component-size refinement

\[
 S_2(row)=(p,\text{Kodaira type},c_p).
 \]

This resolves sectors like the two \(IV\) rows at \(p=2\), where the
geometry is the same but \(c_p\) differs.

### Level 3: full visible local refinement

\[
 S_3(row)=(p,\text{Kodaira type},c_p,\text{reduction label}).
 \]

This resolves the remaining split/nonsplit multiplicative ambiguity.

## 4. Exact checks performed

The verifier checks:

1. `S_0` yields \(3\) classes on the pinned real rows;
2. `S_1` yields \(5\) classes, separating the visible geometric sectors;
3. `S_2` yields \(6\) classes, resolving the \(IV\) ambiguity in
   \(c_p\);
4. `S_3` yields \(7\) classes, resolving the split/nonsplit `I_2`
   ambiguity as well;
5. each refinement is strictly stronger than the previous one on the
   pinned real atlas.

So the minimal source refinement ladder presently visible in Phase 107
is

\[
 \log p
 \;<\;
 (p,\text{Kodaira})
 \;<\;
 (p,\text{Kodaira},c_p)
 \;<\;
 (p,\text{Kodaira},c_p,\text{reduction}).
 \]

## 5. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All minimal source refinement ladder checks passed.
```

So the workspace now contains an exact typed answer to the question
"what kind of new local source information would buy what amount of real
local discrimination?"

## 6. What this proves and what it does not

This witness proves a narrow but useful point:

1. the current local gap of `107_04` is no longer only qualitative; it
   is organized into an exact sequence of increasingly informative
   source signatures;
2. the pinned real target atlas now determines a lower bound on the
   granularity any future local source upgrade would need;
3. future Paper A claims can now be tested against a typed refinement
   ladder rather than against an undifferentiated demand for "more
   local information".

It does **not** prove:

1. that these signatures are geometrically realizable in the present
   Phase 107 source package;
2. that the final source-to-target comparison must stop exactly at
   Level 3;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{minimal source refinement ladder exact-checked},
 \qquad
 \text{full geometric realization of such refinements still open}.
 \]
