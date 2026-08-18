# 107.107 -- Local source upgrade necessity gate

## 1. Purpose

`107_104`, `107_105`, and `107_106` already measure the current local
blindness of the finite-place source row of `107_04`, its minimal
refinement ladder, and the exact residual collisions at each level.

This note turns those observations into a gate:
any future local source upgrade in Phase 107 must pass certain exact
separation tests before it can candidly claim to recover

1. local geometry,
2. local \(c_p\)-data, or
3. the finer visible local reduction datum.

The point is to replace vague promises of "more local information" by
explicit necessary conditions on the pinned real atlas.

## 2. Pinned real test pairs

The verifier `107_107_local_source_upgrade_necessity_gate.py` uses
three already-fixed real comparison pairs:

1. geometry gate pair:
   `14.a1 @ p=2` (\(I_9\), \(c_2=1\), nonsplit) versus
   `14.a5 @ p=2` (\(I_2\), \(c_2=2\), nonsplit);
2. \(c_p\)-gate pair:
   `20.a1 @ p=2` (\(IV\), \(c_2=1\), additive) versus
   `36.a4 @ p=2` (\(IV\), \(c_2=3\), additive);
3. fine-label gate pair:
   `14.a5 @ p=2` (\(I_2\), \(c_2=2\), nonsplit) versus
   `489762.dv3 @ p=2` (\(I_2\), \(c_2=2\), split).

These are genuine local bad fibers of genuine elliptic curves over
\(\mathbf Q\).

## 3. Exact necessity gate

The verifier studies the same four source signatures as before:

1. \(S_0=\log p\);
2. \(S_1=(p,\text{Kodaira})\);
3. \(S_2=(p,\text{Kodaira},c_p)\);
4. \(S_3=(p,\text{Kodaira},c_p,\text{reduction})\).

It then checks the following exact implications on the pinned atlas.

### Geometry necessity

Any source upgrade claiming to see local geometry must separate the
geometry gate pair above.

On the pinned rows:

1. \(S_0\) fails this test;
2. \(S_1,S_2,S_3\) pass it.

So recovering local geometry requires at least \(S_1\)-level
discrimination.

### \(c_p\)-necessity

Any source upgrade claiming to see local component-size arithmetic must
separate the \(IV\) \(c_p\)-gate pair above.

On the pinned rows:

1. \(S_0\) fails;
2. \(S_1\) still fails;
3. \(S_2,S_3\) pass.

So recovering visible \(c_p\)-behavior requires at least
\(S_2\)-level discrimination.

### Fine-label necessity

Any source upgrade claiming to see the finer visible local datum must
separate the split/nonsplit `I_2` pair.

On the pinned rows:

1. \(S_0,S_1,S_2\) all fail;
2. only \(S_3\) passes.

So recovering the full visible local target state requires at least
\(S_3\)-level discrimination.

## 4. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All local source upgrade necessity gate checks passed.
```

So the workspace now contains an exact lower-bound gate for future Paper
A local upgrades.

## 5. What this proves and what it does not

This witness proves a narrow but useful point:

1. Phase 107 now has exact necessary local tests for claims of source
   improvement beyond the present `107_04` row;
2. the current local target atlas yields concrete lower bounds on what
   any future source package must distinguish before stronger local
   claims are allowed;
3. the source-side governance of Paper A is now sharper than “looks more
   informative”: it is tied to exact separation gates on real fibers.

It does **not** prove:

1. that any present Phase 107 construction achieves \(S_1\), \(S_2\),
   or \(S_3\);
2. that these are sufficient conditions for the full local comparison
   problem;
3. any global realization theorem, the terminal identity, or RH.

So the correct reading is:

\[
 \text{local source upgrade necessity gate exact-checked},
 \qquad
 \text{full geometric realization still open}.
 \]
