# 107.130 -- IV* mod-8 residue to c_p no-go

## 1. Purpose

`107_129` exact-checks that, inside the real additive \(IV^\ast\) family
at \(p=2\) with one fixed coarse local packet, the residue class modulo
\(8\) of the local minimal model is a genuine family-level arithmetic
signal.

The next exact question is sharper:

\[
\text{does that mod-8 residue channel already determine }c_p?
\]

If yes, it would be a strong candidate for the missing local source
refinement.
If no, then even this finer channel is still insufficient by itself.

## 2. Fixed real family

The verifier uses exactly the same scanned family as `107_129`:

1. elliptic curves over \(\mathbf Q\);
2. local prime \(p=2\);
3. additive reduction;
4. Kodaira type \(IV^\ast\);
5. coarse packet
   \[
   (2,4,6,8,4,IV^\ast,2,0,1).
   \]

Within that family, `107_129` found

1. `count = 60` curves;
2. `cp_set = [1,3]`;
3. three mod-8 residue classes:
   \[
   (0,0,0,1,6),\quad
   (0,1,0,4,4),\quad
   (0,7,0,4,0).
   \]

## 3. Exact obstruction

The verifier groups the real family by mod-8 residue class and checks
whether \(c_p\) is constant on each group.

It finds explicit counterexamples immediately.

For example:

\[
20a1,\quad 20a3
\]

have the same residue class

\[
(0,1,0,4,4)\pmod 8,
\]

but different Tamagawa numbers:

\[
c_2(20a1)=3,\qquad c_2(20a3)=1.
\]

Likewise:

\[
36a2,\quad 36a4
\]

share

\[
(0,0,0,1,6)\pmod 8,
\]

but

\[
c_2(36a2)=3,\qquad c_2(36a4)=1.
\]

So mod-8 residue does **not** determine \(c_p\) even inside this highly
restricted family.

## 4. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns

```text
VERDICT: NO
```

where `NO` means:
the mod-8 local minimal-model residue channel is not sufficient by
itself to recover \(c_p\) on the scanned real \(IV^\ast\) family.

## 5. Interpretation

This closes an important ambiguity created by `107_128` and `107_129`.

What is now exact-checked is:

1. the current finite source grammar is too coarse;
2. a finer local arithmetic residue channel does exist and persists
   across a real family;
3. but that single residue channel still does not recover \(c_p\) by
   itself.

So the correct reading is:

\[
\text{the next viable source refinement must be finer than the current
grammar,}
\]
\[
\text{but mod-8 minimal-model residue alone is still not enough.}
\]
