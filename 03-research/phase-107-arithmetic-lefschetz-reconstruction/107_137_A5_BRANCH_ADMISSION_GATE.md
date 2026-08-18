# 107.137 -- A5 branch admission gate

## 1. Purpose

The local part of Phase 107 has now reached a precise intermediate
state:

1. the current row (c) is closed by no-go under the current target;
2. the `A5` grammar using local minimal-model residue modulo \(32\)
   survives the fixed visible \(S_3\) atlas;
3. its decisive additive subchannel remains robust on a larger real
   \(IV^\ast\) family;
4. that channel is not derivable from the current `107.00` finite
   source-rule vocabulary.

This note turns those four facts into one operational gate:

\[
\text{should Phase 107 open an explicit A5 local-grammar branch?}
\]

## 2. Admission criterion

The verifier returns `YES` only if all of the following are true on real
data:

1. row (c) is closed under the current target;
2. `A5` has no collisions on the fixed visible atlas;
3. the mod-\(32\) additive subchannel remains clean on the enlarged
   \(IV^\ast\) family through conductor \(2000\);
4. the surviving `A5` channel is not already contained in the present
   finite source rule of `107.00`.

If any one of those conditions fails, the branch is not admitted.

## 3. Exact output

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_SIZE: 6
HAS_GENUS_GE_2_CONTROL: True
HAS_SUPERSINGULAR_CONTROL: True
ROW_C_CLOSED: True
A5_ATLAS_COLLISIONS: 0
FAMILY_ROWS: 285
FAMILY_MOD32_CLASSES: 24
FAMILY_MIXED_MOD32_CLASSES: 0
NON_DERIVABLE_FROM_CURRENT_RULE: True

OPEN_A5_BRANCH: YES
VERDICT: YES
```

So the admission gate is passed.

## 4. Consequence

This does **not** prove that `A5` is the final correct source grammar
for Phase 107.
It proves the narrower operational statement that matters now:

1. continuing to work inside the current row (c) grammar is no longer
   candid, because that route is already closed;
2. there is now one concrete alternate grammar that survives the visible
   real tests performed so far;
3. pursuing that route requires an explicit branch in Paper A rather
   than silent drift inside the old source rule.

So the correct reading is:

\[
\text{the old local route is closed,}
\]
\[
\text{A5 is admitted as a new live branch,}
\]
\[
\text{and future local-source progress must treat it as a genuine}
\]
\[
\text{grammar change.}
\]
