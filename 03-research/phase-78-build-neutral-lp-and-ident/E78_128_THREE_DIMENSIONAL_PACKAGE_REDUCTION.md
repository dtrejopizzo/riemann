# E78.128 - On the audited safe frontier, the five-shell profile reduces to a 3D coupled span

**Scope:** front B only, live object `FIVE-SHELL-MODE2(t)`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** although the
five-shell profile refuses any simple one-parameter shell law, it is already
captured to high accuracy by a three-dimensional subspace of the finite coupled
package, essentially `span(u,v,c)`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral gap is assumed.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       no ambient inverse norm is used as a theorem.
P76.061: respected. The reduction stays inside finite objects already present
         in the coupled package.
E72.16/E77.7az: respected. This is front B; planted separation is admissible.
```

## 1. Starting point

E78.127 autopsied the route

```text
FIVE-SHELL-MODE2(t)  ?=  one universal alternating-geometric shell law.     (D-1)
```

So the next candid question is not "what one scalar explains the profile?", but
"does the full signed five-shell vector already live in a low-dimensional
finite subspace of the coupled package?"

## 2. The finite candidate span

From the coupled-generator package of E78.103, the natural finite vectors are

```text
u = A^-1 s,
v = A^-1 1,
c = A^-1 g,
h = a_b u + b_b v.                                          (D-2)
```

Restrict each of these vectors to the nonnegative five-shell slots

```text
(0,1,2,3,4,5).                                             (D-3)
```

The question is whether the signed five-shell mode-2 vector lies close to
`span(u,v,c)` there.

## 3. Probe

Companion files:

```text
E78_128_package_span_probe.py
E78_128_package_span_results.json
```

Using stable Gram-Schmidt projection on the truncated slots, the audited
capture scores are:

```text
BUILD zeta
N=8:
  span(u)         -> 0.167
  span(v)         -> 0.018
  span(c)         -> 0.0028
  span(v,c)       -> 0.742
  span(u,v,c)     -> 0.923.                                 (D-4)

N=12:
  span(u)         -> 0.165
  span(v)         -> 0.014
  span(c)         -> 0.0040
  span(v,c)       -> 0.700
  span(u,v,c)     -> 0.951.                                 (D-5)

BUILD plant
N=8:
  span(v)         -> 0.997
  span(c)         -> 0.910
  span(h)         -> 0.977
  span(u,v,c)     -> 0.999815.                              (D-6)

N=12:
  span(v)         -> 0.9987
  span(c)         -> 0.929
  span(h)         -> 0.992
  span(u,v,c)     -> 0.999944.                              (D-7)
```

So the profile is not one-dimensional, but the three-dimensional coupled span
already captures it very strongly, and `h` adds no new dimension beyond `u,v`.

## 4. Why this is a genuine reduction

The predecessor `FIVE-SHELL-MODE2(t)` carried the full six-coordinate signed
vector.

The present step reduces that vector to a three-dimensional coupled subspace:

```text
THREE-DIM-PACKAGE-MODE2:
  the projection of the signed five-shell vector onto span(u,v,c).          (D-8)
```

That is strictly less information than the raw signed shell vector.

So this is a genuine reduction on the audited safe frontier:

```text
THREE-DIM-PACKAGE-MODE2  =>  FIVE-SHELL-MODE2(t).          (D-9)
```

with explicit audited capture quality `(D-4)`--`(D-7)`.

## 5. Consequence

The remaining exploratory live object on this branch is no longer the raw
five-shell vector, but its three-dimensional coupled projection:

```text
THREE-DIM-PACKAGE-MODE2.                                   (D-10)
```

This is the sharpest finite coupled reduction reached so far on the safe-axis
route.

The next admissible question is whether the corresponding three scalar
coordinates in `span(u,v,c)` have a cleaner interpretation, or whether one of
them carries the remaining zeta-specific content.

## 6. Status

```text
candidate closure - pending review

proved:
  on the audited safe frontier the signed five-shell profile is strongly
  captured by the three-dimensional coupled span span(u,v,c);

reduced:
  FIVE-SHELL-MODE2(t) to the finite object THREE-DIM-PACKAGE-MODE2;

next:
  identify the three coupled coordinates explicitly, or autopsy the exact
  reason no cleaner one- or two-dimensional package can carry the zeta side.
```
