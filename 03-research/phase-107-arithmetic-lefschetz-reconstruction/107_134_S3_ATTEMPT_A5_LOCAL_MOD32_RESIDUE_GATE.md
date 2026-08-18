# 107.134 -- S3 attempt A5: local mod-32 residue gate

## 1. Purpose

`107_131` showed that, inside the scanned additive \(IV^\ast\) family at
\(p=2\), mod-\(32\) is the first tested residue depth at which mixed
\(c_p\)-classes disappear.
`107_132` and `107_133` then closed the **current** finite local source
row by no-go under the current target.

This note tests the next concrete possibility:

\[
\text{can a genuinely new local arithmetic channel,}
\]
\[
\text{namely minimal-model residue modulo }32,
\]
\[
\text{reopen visible }S_3\text{ on a fixed real atlas?}
\]

The point is not to claim derivability from the present source rule.
The point is to test, on real data, whether this specific refined
grammar is at least target-faithful on the atlas that exposes the known
obstructions.

## 2. Fixed atlas

The verifier fixes the following real atlas before calculation:

1. `14a5 @ 7` — multiplicative \(I_2\), split pair;
2. `21a1 @ 7` — multiplicative \(I_2\), nonsplit pair;
3. `20a1 @ 2` — additive \(IV^\ast\), \(c_p=3\);
4. `36a4 @ 2` — additive \(IV^\ast\), \(c_p=1\);
5. `14a1 @ 5` — supersingular elliptic control;
6. `y^2=x^5+x+1 @ 5` — genus-\(2\) hyperelliptic control.

So the tranche constraints are preserved: the atlas is fixed in advance,
contains at least five real curves, includes a supersingular case, and
includes a genus-\(\ge 2\) control.

## 3. Tested source packet

For elliptic local rows, the new source packet is

\[
R_{A5}(row)=
\bigl(
p,\ v(c_4),\ v(c_6),\ v(\Delta),\ v(j),\ \mathrm{ainv}_{\min}\bmod 32
\bigr).
\]

Here \(\mathrm{ainv}_{\min}\bmod 32\) means the residue class of
the five Weierstrass coefficients of the local minimal model modulo
\(32\).

The target remains the current workspace target

\[
T_{\mathrm{current}}(row)=
(\text{Kodaira symbol},c_p,\text{reduction label}).
\]

## 4. Exact real check

The verifier groups all elliptic atlas rows by the source packet
\(R_{A5}\) and asks whether any one source packet still maps to two
different target states.

This is the exact faithfulness question on the fixed atlas:

\[
R_{A5}(row_1)=R_{A5}(row_2)
\quad\Longrightarrow\quad
T_{\mathrm{current}}(row_1)=T_{\mathrm{current}}(row_2)?
\]

If the answer is yes for every elliptic row in the fixed atlas, then
this refined local grammar survives the currently visible \(S_3\) test.

## 5. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns:

```text
ATLAS_SIZE: 6
HAS_GENUS_GE_2_CONTROL: True
HAS_SUPERSINGULAR_CONTROL: True
ELLIPTIC_ROWS: 5
COLLISION_COUNT: 0

VERDICT: YES
```

So on this fixed real atlas, the valuative-plus-mod-\(32\)-residue
packet separates every visible elliptic target state.

## 6. Consequence

This is not yet a theorem that Phase 107 has found the correct local
source grammar.
It proves a narrower but real statement:

1. the current row (c) is closed by no-go;
2. a specific new local arithmetic refinement, using minimal-model
   residue modulo \(32\), survives the same atlas rather than failing on
   it;
3. therefore the route is not dead in principle, but it must reopen as
   a **different** local grammar than the current one.

So the correct reading is:

\[
\text{current row (c) closed,}
\]
\[
\text{A5 mod-32 residue refinement survives the fixed real atlas,}
\]
\[
\text{derivability from the Phase 107 source rule still open.}
\]
