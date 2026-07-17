# E73.112 - Possible-set box certificate

## 1. Purpose

E73.111 shows that rigorous Hermite enclosures can be loose enough to add competing FAR rows.  The
budget still passes.  Therefore the box certificate should not require a single stable FAR3 set.

This note states the robust possible-set version.

## 2. FAR interval data

For each row `k` in the finite natural-height window, compute interval enclosures:

```text
FAR_k^- <= FAR_k(A,L) <= FAR_k^+
```

for all `A` in the cluster box `B`.

Also compute the main budget upper bound:

```text
B_k^+ >= L^5 T_k(A,L)
```

for all `A in B`.

## 3. Possible selected rows

A row `k` is possible if it can be among the top three FAR scores:

```text
#{j : FAR_j^- > FAR_k^+} < 3.
```

Let:

```text
P_3(B,L):={k : k is possible}.
```

Then the true selected set satisfies:

```text
D_3(A,L) subset P_3(B,L)
```

for every `A in B`.

## 4. Possible-set certificate

The robust sufficient condition is:

```text
sum of the three largest B_k^+ over k in P_3(B,L) <= C_main.
```

Then every possible FAR3 selection has normalized budget at most `C_main`.

## 5. Theorem

**Theorem 112.1.**  If the possible-set certificate holds on `B`, then `FAR3-MAIN-RAT(A,L)` holds
for every `A in B`.

*Proof.*  For a fixed `A`, every row in `D_3(A,L)` belongs to `P_3(B,L)` by definition.  Therefore:

```text
L^5 sum_{k in D_3(A,L)} T_k(A,L)
<=
sum_{k in D_3(A,L)} B_k^+
<=
sum of the three largest B_k^+ over P_3(B,L)
<= C_main.
```

Divide by `L^5`. `□`

## 6. Why this is better than set stability

Set stability requires:

```text
min selected FAR^- > max unselected FAR^+.
```

This can fail only because enclosures are conservative, even when the budget is safe.  The possible-set
certificate avoids unnecessary subdivision by paying only for rows that could enter the top three.

E73.111 shows exactly this case: a conservative row near `21.0` can enter the upper selected set, but
the total budget remains below `C_main=1`.

## 7. Current endpoint

The rigorous main certificate becomes:

```text
HERM-BOX + POSSIBLE-SET <= 1
=> FAR3-MAIN-RAT.
```

Together with the other three gates:

```text
FAR3-MAIN-RAT + LOCK-COMP-BUD + TAIL-LC-BUD + OUT-FAR
=> GATE-73
=> scalar WRL.
```
