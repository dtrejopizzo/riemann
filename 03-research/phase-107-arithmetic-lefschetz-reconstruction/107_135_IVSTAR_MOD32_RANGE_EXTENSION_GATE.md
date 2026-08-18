# 107.135 -- IV* mod-32 range extension gate

## 1. Purpose

`107_131` identified modulus \(32\) as the first tested residue depth at
which the scanned additive \(IV^\ast\) family at \(p=2\) stopped mixing
\(c_p\), but only in the conductor range \(11 \le N \le 500\).
`107_134` then used mod-\(32\) residue as part of the first local
grammar that survived the fixed visible \(S_3\) atlas.

The next exact question is:

\[
\text{does the mod-32 separation phenomenon persist on a substantially}
\]
\[
\text{larger real family, or was it only a small-range accident?}
\]

This note tests that directly.

## 2. Fixed real family

The verifier uses the same family definition as `107_131`, but extends
the conductor range:

1. elliptic curves over \(\mathbf Q\);
2. local prime \(p=2\);
3. additive reduction;
4. Kodaira type \(IV^\ast\);
5. common coarse local packet
   \[
   (2,4,6,8,4,IV^\ast,2,0,1);
   \]
6. conductor range \(11 \le N \le 2000\).

So the family is fixed before calculation, and the test can return `NO`
if a mixed mod-\(32\) residue class appears anywhere in that larger real
scan.

## 3. Exact extended scan

Running the verifier on Saturday, August 1, 2026 finds:

```text
ROWS: 285
mod 16 groups 6 mixed 6
mod 32 groups 24 mixed 0
mod 64 groups 91 mixed 0
```

So in the enlarged real family:

1. mod \(16\) is still too coarse;
2. mod \(32\) still has no mixed \(c_p\)-classes;
3. mod \(64\) also stays clean, as expected from refinement.

## 4. Binary outcome

The verifier returns:

```text
VERDICT: YES
```

where `YES` means:
mod-\(32\) residue still separates the scanned \(IV^\ast\) family at
\(p=2\) through conductor \(2000\).

## 5. Consequence

This does **not** prove that mod-\(32\) residue is the correct Phase 107
source channel, nor that it is derivable from the prime/Gamma/pole
grammar of `107.00`.

It does prove a stronger robustness statement than `107_131`:

1. the mod-\(32\) separation is not just a \(N \le 500\) artifact in
   this family;
2. the first surviving candidate grammar of `107_134` now has a real
   family-level range extension behind it;
3. the local search has therefore advanced from “one atlas survives” to
   “one atlas survives and its decisive additive subchannel persists on
   a much larger real scan.”

So the correct reading is:

\[
\text{current row (c) remains closed,}
\]
\[
\text{A5 still survives the fixed atlas,}
\]
\[
\text{and the mod-32 additive subchannel remains robust on the real}
\]
\[
IV^\ast\text{ family through conductor }2000.
\]
