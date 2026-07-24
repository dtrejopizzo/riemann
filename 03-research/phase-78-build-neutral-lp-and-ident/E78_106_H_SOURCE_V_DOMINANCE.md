# E78.106 - The intrinsic `h_b` source is completely dominated by the `b_b v` branch on the audited ladder

**Run:** 2026-07-19.  
**Scope:** front B only, live object `H-DMU-SOURCE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** inside
`h_b = a_b u + b_b v`, the growth of `A^(-1)h_b` on the audited safe ladder is
carried entirely by the `b_b v` branch; the `a_b u` branch is negligible.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. The analysis stays in the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No spectral-gap hypothesis.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator, no
       ambient inverse norm.
P76.061: respected. The split remains entirely inside the finite coupled algebra.
E72.16/E77.7az: respected. This is front B; planted separation remains admissible.
```

## 1. Starting point

From E78.105, the live intrinsic source is

```text
y_b^(h)=A^(-1) h_b,                                         (V-1)
```

with

```text
h_b = a_b u + b_b v.                                        (V-2)
```

Define the exact branch split

```text
y_b^(h) = y_b^(u) + y_b^(v),                                (V-3)

A y_b^(u) = a_b u,
A y_b^(v) = b_b v.                                          (V-4)
```

Then any theorem-grade control of `y_b^(v)` plus a separate secondary control of
`y_b^(u)` implies the predecessor `H-DMU-SOURCE`.

## 2. Why this is a genuine reduction

Before this split, the live target asked to control

```text
A^(-1)(a_b u + b_b v)                                       (V-5)
```

as a whole.  After `(V-3)`--`(V-4)` we can identify which branch actually
drives the growth.  If one branch is negligible on the audited ladder, the live
front can be reduced to the dominant branch.

That is strictly less information than controlling the full sum from scratch.

## 3. Probe

Companion files:

```text
E78_106_h_source_v_dominance_probe.py
E78_106_h_source_v_dominance_results.json
```

The audited split gives:

```text
BUILD zeta
N= 6: ||y_u|| = 2.10e20,  ||y_v|| = 4.37e24,  ratio_v/total = 1.0
N= 8: ||y_u|| = 3.72e27,  ||y_v|| = 4.02e32,  ratio_v/total = 1.0
N=10: ||y_u|| = 6.61e32,  ||y_v|| = 6.53e37,  ratio_v/total = 1.0
N=12: ||y_u|| = 1.25e41,  ||y_v|| = 1.96e46,  ratio_v/total = 1.0      (V-6)

BUILD plant
N= 6: ||y_u|| = 1.14e19,  ||y_v|| = 1.25e23,  ratio_v/total = 1.0
N= 8: ||y_u|| = 1.48e27,  ||y_v|| = 2.30e31,  ratio_v/total = 1.0
N=10: ||y_u|| = 1.75e28,  ||y_v|| = 1.50e33,  ratio_v/total = 1.0
N=12: ||y_u|| = 1.86e35,  ||y_v|| = 1.83e40,  ratio_v/total = 1.0.     (V-7)
```

Numerically, the `u` branch is invisible at the displayed scale: `y_b^(v)` is
already the whole source to roundoff on the audited ladder.

## 4. Consequence

The audited evidence `(V-6)`--`(V-7)` shows that the honest next live target is
no longer the full intrinsic source `H-DMU-SOURCE`, but the single branch

```text
V-DMU-SOURCE(L,K,eta):
  control y_b^(v) = A^(-1)(b_b v) cofinally enough to imply H-DMU-SOURCE. (V-8)
```

If a later theorem controls `y_b^(u)` separately, `(V-8)` plus that bound
reconstructs the predecessor by `(V-3)`.

## 5. Status

```text
candidate closure - pending review

proved:
  the exact branch split y_b^(h) = y_b^(u) + y_b^(v);

localized:
  on the audited ladder the branch y_b^(v) dominates the intrinsic source in
  both builds;

reduced:
  H-DMU-SOURCE to the single-branch target V-DMU-SOURCE, modulo future
  separate control of the negligible u-branch;

next:
  attack A^(-1)(b_b v) directly, or autopsy which factor inside b_b v forces
  its cofinal growth.
```
