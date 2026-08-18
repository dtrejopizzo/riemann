# 107.138 -- Paper A local branch formalization

## 1. Purpose

The recent local gates left Paper A in a state that was clear in the
ledger but not yet recorded as a formal planning consequence:

1. the legacy local row (c) is closed under the current target;
2. `A5`, based on local minimal-model residue modulo \(32\), survives
   the fixed visible \(S_3\) atlas;
3. its decisive additive subchannel survives a larger real family;
4. it does not factor through the current finite source rule of
   `107.00`.

This note turns that into one exact planning statement:

\[
\text{Paper A local work is now bifurcated.}
\]

## 2. Formal criterion

The verifier returns `YES` only if all four of the following are true:

1. `LEGACY_ROW_C_STATUS: CLOSED`;
2. `A5_ATLAS_STATUS: LIVE`;
3. `A5_FAMILY_STATUS: LIVE`;
4. `A5_NOT_CURRENT_RULE: True`.

This is stricter than merely saying that one candidate looks promising.
It requires the old route to be actually closed and the new route to be
actually distinct.

## 3. Exact output

Running the verifier on Saturday, August 1, 2026 returns:

```text
LEGACY_ROW_C_STATUS: CLOSED
A5_ATLAS_STATUS: LIVE
A5_FAMILY_STATUS: LIVE
A5_NOT_CURRENT_RULE: True
FAMILY_ROWS: 285
FAMILY_MOD32_CLASSES: 24

PAPER_A_LOCAL_BRANCH_STATE: BIFURCATED
VERDICT: YES
```

So the branch state is no longer provisional.

## 4. Consequence

This does **not** prove that `A5` is the final correct local grammar.
It proves the narrower but operationally decisive point:

1. the old local Paper A route must now be read as a closed branch;
2. `A5` must be read as a distinct live branch rather than an
   interpretation of the old one;
3. future local-source work in Paper A should be written against that
   bifurcated state explicitly.

So the correct reading is:

\[
\text{Paper A local planning has split into two named branches:}
\]
\[
\text{legacy row (c), closed; A5, live.}
\]
