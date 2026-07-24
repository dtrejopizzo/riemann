# E79.81 - The degenerate rows do not select the geometric point

**Scope:** `GAP-Z` only, audit of the remaining normalization hope after
E79.79-E79.80.  
**Class:** AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** the degenerate
rows `N=8` and `N=14` carry no extra coefficient-selection information. They do
not cut the admissible cone further; they are exact duplicates in the relevant
packet coordinates.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure finite-family audit on existing E79 results.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

After E79.79-E79.80 the only obvious cheap hope left was:

```text
perhaps the degenerate rows N=8 and N=14 impose an exact tie or symmetry
condition that singles out (0.36, 0.14).                                (81-1)
```

This note checks that directly.

## 2. Audit

The relevant packet coordinates are the two geometric modes from E79.78:

```text
u(S) := start(S) - card(S),
v(S) := span(S).                                                        (81-2)
```

### Row N=14

The frontier packets are literally the same support:

```text
suffix = triple = {10,11,12}.                                           (81-3)
```

So every packet-level statistic agrees exactly:

```text
mismatch, surcharge, u, v, support.                                     (81-4)
```

This row contributes no new equality beyond tautological duplication.

### Row N=8

Here the two frontier points are different supports:

```text
pair   = {5,7},
triple = {6,7,8},                                                       (81-5)
```

but they have the same geometric coordinates:

```text
u(pair)   = start-card = 5-2 = 3,
u(triple) = start-card = 6-3 = 3,                                       (81-6)

v(pair)   = span = 3,
v(triple) = span = 3.                                                   (81-7)
```

Therefore every geometric functional of the E79.78 form

```text
a u(S) + b v(S)                                                         (81-8)
```

gives the **same** value on both supports, for every `(a,b)`. So the row is
degenerate for a stronger reason than E79.76 first suggested: it does not just
have nearly equal surcharge, it has exactly the same two geometric modes.

The only surviving difference at `N=8` is mismatch:

```text
pair   mismatch = 0.029900...,
triple mismatch = 0.027405....                                          (81-9)
```

So this row collapses to pure mismatch and imposes no coefficient constraint.

## 3. Reading

The hoped-for normalization from the degenerate rows is dead.

Neither row cuts the cone from E79.79:

```text
N=14: exact support duplication,
N=8 : exact equality of the two geometric modes u and v.                (81-10)
```

So the current point `(0.36, 0.14)` is not being selected by:

```text
- tradeoff winner data,
- max-margin robustness,
- degenerate-row exact ties.                                            (81-11)
```

## 4. Consequence

This localizes the remaining normalization burden even more sharply.

Any real canonicity of `(0.36,0.14)` must come from something outside the
packet-level frontier bookkeeping already extracted in E79.69-E79.80.

The plausible sources left are now of a different kind:

```text
1. a normalization inherited from an earlier common-cloud scalar law,
2. an exact identity tying the coefficients to the shell profile moments,
3. or the honest conclusion that the point is not canonical and only the cone
   is structurally meaningful.                                           (81-12)
```

## 5. Status

```text
proved by direct audit:
  the degenerate rows N=8 and N=14 add no new coefficient-selection
  information;

clarified:
  N=14 is a literal support duplicate, while N=8 is a duplicate in the exact
  geometric coordinates (start-card, span);

killed:
  the hope that the remaining canonicity comes from degenerate-row exact ties;

open:
  either find a source of normalization outside the frontier bookkeeping, or
  accept that only the admissible cone is structural;

next:
  compare (0.36,0.14) against earlier scalar-law coordinates from E79.58-E79.66
  to see whether it is inherited from that branch rather than selected here.
```
