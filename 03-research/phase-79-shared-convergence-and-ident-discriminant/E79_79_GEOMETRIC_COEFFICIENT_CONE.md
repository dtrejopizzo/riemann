# E79.79 - The geometric coefficients are not forced: they live in an open cone

**Scope:** `GAP-Z` only, admissible-coefficient audit for the geometric side of
the frontier rule.  
**Class:** REDUCCION GENUINA + AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** the geometric
coefficients in E79.78 are not singled out by the audited frontier decisions.
Those decisions only determine an open cone in coefficient space. So the real
burden is no longer "why exactly `0.36` and `0.14`?", but why the program lands
at that particular point inside a much larger admissible region.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Pure algebra on the audited frontier inequalities.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. No endpoint identity is imported.
```

## 1. Starting point

E79.78 showed that the geometric side is exactly

```text
cost_{a,b}(S) := a (start-card) + b span,                               (79-1)
```

with the current audited selector corresponding to

```text
(a,b) = (0.36, 0.14).                                                   (79-2)
```

The next honest question is whether the audited tradeoff rows force this pair,
or only constrain it.

## 2. Frontier inequalities

On a genuine tradeoff row, with low-cost point `L` and high-cost point `H`,
define

```text
Delta_u := (start-card)(H) - (start-card)(L),
Delta_v := span(H) - span(L),                                           (79-3)
Delta_m := mismatch(L) - mismatch(H).                                   (79-4)
```

Then the E79.76 winner condition is

```text
choose H  <=>  a Delta_u + b Delta_v < Delta_m,                         (79-5)
```

and choose `L` when the inequality reverses.

For the three genuine tradeoff rows this becomes:

```text
N=10:  choose low  <=>  -a + 3b > 0.0207805...,                         (79-6)
N=12:  choose high <=>   2a - 3b < 0.3307238...,                        (79-7)
N=16:  choose high <=>   a        < 0.3786042....                       (79-8)
```

So the whole audited geometric burden is already an intersection of three open
half-planes.

## 3. Probe

Companion files:

```text
E79_79_geometric_coefficient_cone_probe.py
E79_79_geometric_coefficient_cone_results.json
```

The probe scans a coarse box

```text
a,b in {0.00, 0.01, ..., 0.80},                                         (79-9)
```

and records which pairs preserve the E79.76 winner on all three genuine
tradeoff rows.

## 4. Result

The admissible set is large:

```text
2793 grid points in the audited 81 x 81 box preserve the same frontier
decisions.                                                              (79-10)
```

In particular:

```text
(0.36, 0.14) is admissible,
but it is far from unique.                                              (79-11)
```

For small `a`, the admissible band in `b` is especially wide; for instance:

```text
a = 0.00  ->  b can range from about 0.01 to 0.80,
a = 0.10  ->  b can range from about 0.05 to 0.80,
a = 0.20  ->  b can range from about 0.08 to 0.80.                      (79-12)
```

So the current coefficients are not being pinned down by the audited tradeoff
data alone.

## 5. Reading

This is the honest answer to the coefficient-forcing question.

The audited frontier rows determine:

```text
an open cone of admissible geometric exchange rates,                     (79-13)
```

not a unique coefficient pair.

So the remaining burden is strictly smaller and more precise:

```text
not "why these are the only coefficients,"
but
"what extra normalization or exact identity selects this point inside the cone?"
                                                                      (79-14)
```

That is a better-posed structural question.

## 6. Consequence

After E79.79 the live object sharpens again:

```text
1. mismatch side: one sigma-rigid excess scalar |eps|;
2. geometry side: one exact two-mode cone a(start-card) + b span;
3. frontier decisions: only constrain (a,b) to an open admissible region. (79-15)
```

So the next honest step is no longer coefficient hunting by decision
preservation. It is to search for:

```text
- a normalization that canonically selects one point in the cone, or
- an exact relation tying a and b to already-named finite objects.      (79-16)
```

## 7. Status

```text
proved by algebra + probe:
  the audited tradeoff rows do not force the geometric coefficients;
  they only define an open cone of admissible pairs (a,b);

clarified:
  (0.36, 0.14) is one interior admissible point, not a uniquely determined
  endpoint of the audited frontier law;

killed:
  the hope that the current audited decisions alone determine the geometric
  weights;

open:
  identify the extra normalization or exact packet identity that selects the
  specific point (0.36, 0.14) inside the admissible cone;

next:
  inspect whether the chosen point is characterized by a symmetry,
  minimality, or exact tie condition on the degenerate rows N=8 and N=14.
```
