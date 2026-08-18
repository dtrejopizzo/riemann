# E78.5 - IDENT frontier reset: the absolute Euler tail is not the live object

**Run:** 2026-07-18.
**Scope:** IDENT only (`FIXED-L-WEYL`, `SAFE-GAMMA-IDENT`, `OUTER-LIMIT`).

## 1. Purpose

After the Phase-78 cleanup on the LP side, the next question is where the
genuine difficulty still sits inside IDENT.  This note isolates the exact live
object and proves that one tempting formulation is already dead:

```text
OUTER-LIMIT is NOT blocked by the absolute Euler tail itself.
The live obstruction is the exact comparison object on the finite/fixed-L side.
```

## 2. What is already theorem-grade

Three inputs are already in the ledger.

### 2.1 Cofinal glue

E77.6 proved:

```text
FIXED-L-WEYL + SAFE-GAMMA-IDENT + OUTER-LIMIT
=> SR-LOG-2SCALE => IDENT.
```

So IDENT is already correctly localized to those three obligations.

### 2.2 Absolute Euler tail

P76.039 proved, uniformly on compact subsets of `Re(s) >= 1 + delta`,

```text
sum_{n > e^L} Lambda(n) n^(-s) = O_delta(e^(-delta L)).     (ID-1)
```

Equivalently,

```text
-2 sum_{n <= e^L} Lambda(n) n^(-s)
-> 2 zeta'(s)/zeta(s)                                       (ID-2)
```

locally uniformly in `Re(s) > 1`.

This is RH-free and uses only the Chebyshev bound plus partial summation.

### 2.3 Hard Euler trace is dead

P76.040 proved that the naive finite identity

```text
J_{L,N}(sigma)
 ?= arch_gamma(s) - 2 sum_{n <= e^L} Lambda(n) n^(-s) + o(1)
```

is false at finite scale.  The exact coupled object is instead

```text
J_{L,N}(sigma)
 = L coth(sigma L/2)
   + 2 Re(i T'_{L,N}(i sigma)/T_{L,N}(i sigma))
   - B_ext,L,N(sigma),                                    (ID-3)
```

and the difficulty is to identify its signed continuum limit *before* replacing
it by a hard Dirichlet truncation.

## 3. Reduction of OUTER-LIMIT

Define the exact fixed-L candidate limit

```text
G_L(sigma) = lim_{N->infinity} J_{L,N}(sigma),
```

whenever the limit exists locally uniformly on safe compacta.  Suppose one
proves the following exact comparison statement:

```text
CELL-SMOOTHED-EULER-COMPARISON.
For every safe compact K subset (1/2,infinity),

sup_{sigma in K}
|G_L(sigma) - H_L(1/2+sigma)| -> 0                         (ID-4)

as L->infinity, where

H_L(s) = 2/s + 2/(s-1) - log(pi) + digamma(s/2)
         - 2 sum_{n <= e^L} Lambda(n) n^(-s).             (ID-5)
```

Then `OUTER-LIMIT` follows.

### Proof

Fix a compact `K subset (1/2,infinity)` and let

```text
K' = { s = 1/2 + sigma : sigma in K } subset {Re(s) > 1 }.
```

Choose `delta > 0` with `Re(s) >= 1 + delta` on `K'`.  By `(ID-1)` / `(ID-2)`,

```text
sup_{s in K'}
|H_L(s) - 2 Xi'(s)/Xi(s)| -> 0                            (ID-6)
```

because

```text
2 Xi'(s)/Xi(s)
= 2/s + 2/(s-1) - log(pi) + digamma(s/2)
  - 2 sum_{n >= 2} Lambda(n) n^(-s).                     (ID-7)
```

Combining `(ID-4)` and `(ID-6)` with the triangle inequality gives

```text
sup_{sigma in K}
|G_L(sigma) - 2 Xi'(1/2+sigma)/Xi(1/2+sigma)| -> 0,
```

which is exactly `OUTER-LIMIT`.  QED.

## 4. Reading

Section 3 shows that the absolute Euler part is not the live obstruction.  The
live obstruction is the exact finite/fixed-L comparison:

```text
G_L  versus  H_L.
```

So the candid open object is **not**

```text
"control the prime tail better"
```

and not

```text
"improve Euler truncation near s=1".
```

Those are already outside the real bottleneck.  The bottleneck is:

```text
derive or identify the exact cell-smoothed comparison object whose L->infinity
limit matches the safe Euler truncation.
```

This is exactly consistent with P76.040's autopsy.

## 5. Consequence for the ledger

The IDENT front should now be read as:

```text
FIXED-L-WEYL:
  finite sections -> intrinsic fixed-L object G_L;

SAFE-GAMMA-IDENT:
  identify G_L as the exact cell-smoothed fixed-L derivative;

OUTER-LIMIT:
  reduced to CELL-SMOOTHED-EULER-COMPARISON + P76.039.
```

So the smallest candid next finite object on the arithmetic side is:

```text
CELL-SMOOTHED-EULER-COMPARISON
=> OUTER-LIMIT.
```

This is a genuine reduction because the implication is proved in Section 3.

## 6. What does not count anymore

The following are explicitly archived as non-live:

```text
1. hard prime truncation as a direct finite proxy for J_{L,N};   dead by P76.040;
2. any attempt to force IDENT by prime-only bounds before the coupled
   Gamma-prime/cell identity is formed;                           forbidden by
   P76.040 / E77.6;
3. improving the absolute Euler remainder in isolation.          already enough.
```

## 7. Status

```text
proved:
  OUTER-LIMIT reduces to CELL-SMOOTHED-EULER-COMPARISON plus the already-proved
  absolute Euler tail P76.039;

clarified:
  the absolute Euler tail is not the active arithmetic obstruction;

reset:
  the smallest candid next IDENT object is the exact cell-smoothed comparison
  G_L vs H_L, not raw Euler truncation;

live:
  CELL-SMOOTHED-EULER-COMPARISON;

next:
  extract the exact fixed-L comparison object from the coupled Gamma-prime/cell
  algebra and test it against the zeta/plant builds without decoupling the
  Schur solve.
```
