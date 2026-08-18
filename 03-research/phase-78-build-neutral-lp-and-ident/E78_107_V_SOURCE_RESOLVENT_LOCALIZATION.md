# E78.107 - `V-DMU-SOURCE` localizes to the resolvent branch `A^(-1)v`, not to the scalar coefficient `b_b`

**Run:** 2026-07-19.  
**Scope:** front B only, live object `V-DMU-SOURCE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the growth of
`y_b^(v)=A^(-1)(b_b v)` is not driven by the scalar coefficient `b_b`; it is
driven by the resolvent branch `A^(-1)v`.

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

From E78.106, the live source is the single branch

```text
y_b^(v)=A^(-1)(b_b v).                                      (R-1)
```

Since `b_b` is scalar,

```text
y_b^(v)=b_b A^(-1)v.                                        (R-2)
```

Thus the branch splits exactly into:

```text
scalar coefficient:     b_b,
resolvent response:     A^(-1)v.                            (R-3)
```

## 2. Why this is a genuine reduction

Before this split, the live target asked to control `y_b^(v)` as a whole.
After `(R-2)`, if the coefficient branch is shown not to carry the growth on the
audited ladder, then the live target can be reduced to the resolvent response
alone.

That is strictly less information than controlling the product from scratch.

## 3. Probe

Companion files:

```text
E78_107_v_source_resolvent_probe.py
E78_107_v_source_resolvent_results.json
```

The audited anatomy gives:

```text
BUILD zeta
N= 6: |b| = 5.92e-7,   ||A^-1 v|| = 7.38e30,  ||y_v|| = 4.37e24
N= 8: |b| = 2.40e-6,   ||A^-1 v|| = 1.68e38,  ||y_v|| = 4.02e32
N=10: |b| = 2.40e-8,   ||A^-1 v|| = 2.73e45,  ||y_v|| = 6.53e37
N=12: |b| = 7.48e-7,   ||A^-1 v|| = 2.61e52,  ||y_v|| = 1.96e46.   (R-4)

BUILD plant
N= 6: |b| = 1.21e-5,   ||A^-1 v|| = 1.03e28,  ||y_v|| = 1.25e23
N= 8: |b| = 7.42e-2,   ||A^-1 v|| = 3.10e32,  ||y_v|| = 2.30e31
N=10: |b| = 1.82e-5,   ||A^-1 v|| = 8.23e37,  ||y_v|| = 1.50e33
N=12: |b| = 2.55e-4,   ||A^-1 v|| = 7.17e43,  ||y_v|| = 1.83e40.   (R-5)
```

The coefficient `|b_b|` fluctuates over several orders of magnitude and remains
small on most audited rows; it does not track the monotone explosion of
`||y_v||`.  By contrast, `||A^(-1)v||` grows violently and consistently in both
builds, exactly matching the growth of the source branch.

## 4. Consequence

The audited evidence `(R-4)`--`(R-5)` shows that the candid next live target is
not "control `b_b`" but

```text
V-RESOLVENT-SOURCE(L,K,eta):
  control A^(-1)v cofinally enough to control y_b^(v).     (R-6)
```

Any later separate theorem controlling `b_b` can be combined with `(R-6)` via
`(R-2)`, but the burden is already localized to the resolvent branch.

## 5. Status

```text
candidate closure - pending review

proved:
  the exact scalar/resolvent split y_b^(v)=b_b A^(-1)v;

localized:
  on the audited ladder the blowup of y_b^(v) is carried by A^(-1)v, not by b_b;

reduced:
  V-DMU-SOURCE to the resolvent target V-RESOLVENT-SOURCE;

next:
  attack A^(-1)v directly from the operator equation Av=1, or autopsy the exact
  coefficient inside that resolvent response that forces the cofinal growth.
```
