# 107.126 -- Target bifurcation gate: c_p versus Kodaira

## 1. Purpose

The recent local no-go chain leaves one design decision exposed:

\[
\text{must the local target retain }c_p,
\quad\text{or is Kodaira type alone enough?}
\]

This note turns that question into an exact binary gate on the decisive
real pair

\[
20a1@2,\qquad 36a4@2.
\]

The goal is not to settle the whole phase in one step.
The goal is to formalize, on real data, how the answer to that design
question changes the fate of the current finite source row.

## 2. Current source row

On this pair, the present finite source row of `107_03`--`107_04` is the
same on both sides:

\[
\mathcal S_{107}=
\bigl(Z_{2,1},(1,2),2^{-1/2},\log 2\bigr).
\]

So any difference in verdict comes entirely from the choice of target.

## 3. Two target designs

The verifier compares two targets on the same real pair.

### Target A: current workspace target

\[
T_{\rm cp}(row)=
(\text{Kodaira symbol},c_p,\text{reduction label}).
\]

This is the target currently used by the S3 gates in the workspace.

### Target B: reduced Kodaira-only target

\[
T_{\rm Kod}(row)=
(\text{Kodaira symbol}).
\]

This is the minimal target suggested by the design bifurcation: forget
\(c_p\) and ask only for geometric fiber type.

## 4. Exact real comparison

Sage computes on the real pair:

\[
T_{\rm cp}(20a1@2)=(IV^\ast,3,\text{additive}),
\qquad
T_{\rm cp}(36a4@2)=(IV^\ast,1,\text{additive}),
\]

so the current source row fails for \(T_{\rm cp}\).

But also:

\[
T_{\rm Kod}(20a1@2)=T_{\rm Kod}(36a4@2)=IV^\ast,
\]

so the same current source row succeeds for \(T_{\rm Kod}\).

## 5. Binary outcome

Running the verifier on Saturday, August 1, 2026 returns:

```text
TARGET_WITH_CP: NO
TARGET_KODAIRA_ONLY: YES
```

This is the exact bifurcation:

1. if the target includes \(c_p\), the present finite source row is
   blocked on real data;
2. if the target is reduced to Kodaira type, that specific blockage
   disappears on the same pair.

## 6. Consequence

This note does not decide which target Phase 107 *should* keep.
It does decide, exactly, what is at stake:

1. keeping \(c_p\) commits the phase to finding a genuinely new
   Galois-sensitive source channel;
2. dropping \(c_p\) preserves viability of the current finite source row
   on the real forcing pair, but weakens the target accordingly.

So the correct reading is:

\[
\text{the design fork is real,}
\]
\[
\text{and the pair }20a1@2/36a4@2\text{ already decides its local effect.}
\]
