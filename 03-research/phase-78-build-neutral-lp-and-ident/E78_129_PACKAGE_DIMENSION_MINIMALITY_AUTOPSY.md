# E78.129 - The package reduction does not collapse below dimension three on the zeta side

**Scope:** front B only, live object `THREE-DIM-PACKAGE-MODE2`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the exact failed
quantifier in the current reduction is the package dimension itself: on the
audited safe frontier, no one- or two-coordinate package built from `(u,v,c)`
captures the zeta side, so dimension three is the minimal candid finite
package reached so far.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This stays in the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       and no ambient inverse norm enters.
P76.061: respected. Everything remains inside finite coupled package pairings.
E72.16/E77.7az: respected. This is front B; planted separation is admissible.
```

## 1. Starting point

E78.128 reduced the signed five-shell vector to the finite coupled object

```text
THREE-DIM-PACKAGE-MODE2 = projection onto span(u,v,c).      (M-1)
```

The next admissible question is whether one coordinate dominates, or at least
whether some two-coordinate package already closes the zeta side.

## 2. Probe

Companion files:

```text
E78_129_package_dimension_probe.py
E78_129_package_dimension_results.json
```

On the same audited safe frontier as E78.128, Gram-Schmidt coordinates inside
`span(u,v,c)` give:

```text
BUILD zeta
N=8:
  u -> 0.305652
  v -> 0.526218
  c -> 0.162218
  total capture -> 0.994088.                               (M-2)

N=12:
  u -> 0.302034
  v -> 0.533084
  c -> 0.162524
  total capture -> 0.997642.                               (M-3)

BUILD plant
N=8:
  u -> 0.412907
  v -> 0.587092
  c -> 0.00000126
  total capture -> 0.99999997.                             (M-4)

N=12:
  u -> 0.434968
  v -> 0.565032
  c -> 0.00000028
  total capture -> 0.999999997.                            (M-5)
```

So on the zeta side no single coordinate dominates: the content is split
stably between `u` and `v`, with a genuine `c` correction around `0.16`.

The two-coordinate captures are:

```text
BUILD zeta
N=8:
  span(u,v) -> 0.589963
  span(u,c) -> 0.568871
  span(v,c) -> 0.742069.                                   (M-6)

N=12:
  span(u,v) -> 0.593944
  span(u,c) -> 0.583556
  span(v,c) -> 0.700262.                                   (M-7)

BUILD plant
N=8:
  span(u,v) -> 0.998861
  span(u,c) -> 0.986293
  span(v,c) -> 0.999235.                                   (M-8)

N=12:
  span(u,v) -> 0.999465
  span(u,c) -> 0.992798
  span(v,c) -> 0.999586.                                   (M-9)
```

Hence every two-coordinate package misses a substantial part of the zeta
vector, while the planted side almost collapses to `span(u,v)`.

## 3. Exact failure

The route

```text
THREE-DIM-PACKAGE-MODE2  ?=  one coordinate or one two-coordinate package.   (M-10)
```

fails at the dimension quantifier:

- one coordinate fails because neither `u` nor `v` exceeds about `0.54` of the
  zeta package mass, and `c` is smaller but still macroscopic;
- two coordinates fail because every pair remains far from full capture on the
  zeta side, with best audited score only about `0.74`.                       (M-11)

So dimension three is not cosmetic here. It is the first package dimension
that candidly carries the zeta side on the audited safe frontier.

## 4. Consequence

The current finite reduction of this branch stops exactly at dimension three:

```text
no 1D or 2D package object built from (u,v,c)
closes THREE-DIM-PACKAGE-MODE2 on the zeta side.                             (M-12)
```

That is a real autopsy, not a reparametrization: it names the failed
quantifier and closes the route "search for a master coordinate inside the
package".

The live object therefore remains

```text
THREE-DIM-PACKAGE-MODE2,                                            (M-13)
```

and the next admissible step must use the coupled three-coordinate structure
itself, not hunt for a single scalar separator.

## 5. Status

```text
candidate closure - pending review

autopsied:
  the route "collapse THREE-DIM-PACKAGE-MODE2 to one or two package
  coordinates" fails exactly at the package-dimension quantifier;

proved by probe:
  on the audited safe frontier, zeta needs all three coordinates (u,v,c),
  whereas the planted side nearly collapses to span(u,v);

next:
  attack the coupled three-coordinate law directly, or leave this branch and
  return to the cofinal front once no asymptotic implication can be extracted.
```
