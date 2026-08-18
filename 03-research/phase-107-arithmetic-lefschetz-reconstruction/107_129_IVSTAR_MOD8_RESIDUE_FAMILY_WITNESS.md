# 107.129 -- IV* mod-8 residue family witness

## 1. Purpose

`107_128` shows on one forcing pair that the residue class of the local
minimal model at \(p=2\) separates two curves that the current finite
source grammar does not.

This note tests whether that is merely an isolated accident or the first
visible piece of a broader arithmetic pattern.

The verifier scans actual elliptic curves over \(\mathbf Q\) in the
local family singled out by the previous obstruction:

1. additive reduction at \(p=2\);
2. Kodaira type \(IV^\ast\);
3. the same coarse valuative/Euler packet
   \[
   (p,v(c_4),v(c_6),v(\Delta),v(j),\text{Kodaira},f_p,a_p,L_p^{\rm loc})
   =
   (2,4,6,8,4,IV^\ast,2,0,1).
   \]

The question is then:

\[
\text{does the mod-8 residue of the local minimal model see real
structure inside that whole family?}
\]

## 2. Scan performed

The verifier scans the local Cremona database for conductors
\(11\le N\le 500\), extracts every curve satisfying the coarse local
packet above, and records:

1. the curve label;
2. the Tamagawa number \(c_2\);
3. the minimal-model Weierstrass tuple
   \(\mathbf a_{\min}(E,2)\);
4. its residue class modulo \(8\).

## 3. Exact outcome

Running the verifier on Saturday, August 1, 2026 finds:

1. `count = 60` real curves in this family;
2. `cp_set = [1, 3]`;
3. exactly three mod-8 residue classes:
   \[
   (0,0,0,1,6),\qquad
   (0,1,0,4,4),\qquad
   (0,7,0,4,0).
   \]

So the witness of `107_128` is not isolated.
Inside one fixed coarse local packet, a nontrivial residue-level local
arithmetic structure appears repeatedly across many real curves.

## 4. What this proves

This witness proves a narrow but useful point:

1. the pair `20a1@2` / `36a4@2` is not a one-off curiosity;
2. the same coarse additive \(IV^\ast\) packet occurs many times in real
   data with \(c_2\in\{1,3\}\);
3. the residue class of the local minimal model organizes that family
   into only a few arithmetic subclasses, so it is a serious candidate
   for the kind of finer local channel Phase 107 would need if it keeps
   \(c_p\) in the target.

It does **not** prove:

1. that the mod-8 residue class alone determines \(c_2\) for every such
   curve;
2. that this channel belongs to the present source grammar of `107.00`;
3. any global realization theorem or closure of row (c).

## 5. Binary outcome

The verifier returns

```text
VERDICT: YES
```

where `YES` means:
the local minimal-model residue channel persists as a real family-level
signal across many curves sharing the same coarse \(IV^\ast\) local
packet at \(p=2\).

## 6. Interpretation

Phase 107 now has both sides of the local story:

1. the current finite source grammar is too coarse for the present
   target if \(c_p\) is retained (`107_123`--`107_127`);
2. a concrete finer local arithmetic signal does exist on real data and
   is not confined to one pair (`107_128`, this note).

So the next viable move, if \(c_p\) stays in the target, is no longer
an abstract request for “more local information.”  It is a search for a
source-legal mechanism capable of recovering a residue-type local
arithmetic channel of this kind.
