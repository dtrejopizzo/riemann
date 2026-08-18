# E78.132 - The `AUX-DMU-SOURCE -> H-DMU-SOURCE` split is exploratory only

**Scope:** front B only, branch at `AUX-DMU-SOURCE`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the exact failed
quantifier in E78.105 is already cofinality in `N`; the reduction from
`AUX-DMU-SOURCE` to `H-DMU-SOURCE` uses only audited-ladder dominance of
`y_b^(h)` over `y_b^(ab)` and does not prove a theorem of the form required by
`SAFE-Y-BOUND`.  So the true return point rises once more, to `SAFE-Y-BOUND`
and the unreduced auxiliary source branch.

## 0. Wall checklist

```text
MW-1:  respected. No positivity/Weil-form target appears.
MW-2:  respected. This remains inside the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No wrong-sign lower-bound mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No uniform spectral-gap hypothesis.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator,
       and no ambient inverse norm is promoted.
P76.061: respected. This note only audits whether the source split carries a
         legal cofinal implication.
E72.16/E77.7az: respected. This is front B; build separation is admissible but
                does not create a closure mechanism.
```

## 1. The exact split

E78.104 reduced the derivative burden to the source target

```text
AUX-DMU-SOURCE(L,K,eta):
  control c_b and y_b cofinally enough to obtain SAFE-Y-BOUND,              (A-1)
```

with

```text
A y_b = h_b + alpha_b s + beta_b 1.                                         (A-2)
```

E78.105 then introduced the exact decomposition

```text
y_b = y_b^(h) + y_b^(ab),
A y_b^(h)  = h_b,
A y_b^(ab) = alpha_b s + beta_b 1,                                          (A-3)
```

and observed on the audited ladder that

```text
||y_b^(ab)|| / ||y_b|| <= 0.18, decreasing through the tested sections.      (A-4)
```

From this, E78.105 declared the next live object

```text
H-DMU-SOURCE(L,K,eta):
  control y_b^(h)=A^(-1)h_b cofinally enough to imply SAFE-Y-BOUND.         (A-5)
```

## 2. Exact failed quantifier

The problem is not the algebraic split `(A-3)`, which is exact.  The problem is
the dominance claim needed to pass from `(A-1)` to `(A-5)`.

What E78.105 actually proves is only:

```text
on the audited ladder, the ratio ||y_b^(ab)|| / ||y_b|| is about 0.10-0.18.  (A-6)
```

It does **not** prove a theorem of the form

```text
exists C<1 and N_0 such that
  ||y_b^(ab)|| <= C ||y_b^(h)||   for all N>=N_0,                            (A-7)
```

nor any compact-uniform bound on `Y_b^(ab), Y_b^(ab),bd, (Y_b^(ab))'` implying
that the scalar branch is asymptotically negligible inside `SAFE-Y-BOUND`.

So the reduction

```text
AUX-DMU-SOURCE  ?=>  H-DMU-SOURCE                                            (A-8)
```

fails exactly at the cofinal quantifier "for all sufficiently large `N`".

## 3. Why this matters for the derivative core

The live derivative chain still requires:

```text
SAFE-Y-BOUND
=> DMU-COUPLED-GENERATOR
=> PAIRED-DMU-LOCAL
=> MU-DIR
=> SAFE-GAMMA-IDENT-CORE.                                                    (A-9)
```

To use `H-DMU-SOURCE` as a predecessor of `SAFE-Y-BOUND`, one needs either:

```text
1. a cofinal theorem that y_b^(ab) is uniformly secondary, or
2. a separate cofinal bound SAFE-YAB-BOUND on the scalar branch.             (A-10)
```

E78.105 provides neither `(A-10.1)` nor `(A-10.2)`.  It only provides the
finite audited portrait `(A-6)`.

Therefore `H-DMU-SOURCE` is not yet a legal cofinal predecessor of
`SAFE-Y-BOUND`.

## 4. Consequence

The candid conclusion is:

```text
the split AUX-DMU-SOURCE -> H-DMU-SOURCE is exploratory only.                (A-11)
```

The exact source-level return point is therefore not `H-DMU-SOURCE`, but

```text
SAFE-Y-BOUND / AUX-DMU-SOURCE,                                               (A-12)
```

unless a future theorem closes `(A-10)`.

This sharpens E78.131 once more: the loss of cofinality happens already at the
source split, before any descent to `H-DMU-SOURCE`, `V-DMU-SOURCE`, or the
later modal portraits.

## 5. Status

```text
candidate closure - pending review

autopsied:
  the reduction AUX-DMU-SOURCE -> H-DMU-SOURCE does not currently carry a
  cofinal implication;

identified exact failed quantifier:
  E78.105 proves only audited-ladder dominance of y_b^(h) over y_b^(ab), not
  an eventual-for-all-N theorem;

archived:
  H-DMU-SOURCE and every descendant branch below it as exploratory unless a
  future theorem closes the scalar branch cofinally;

next:
  return to SAFE-Y-BOUND / AUX-DMU-SOURCE directly, or prove a genuine
  cofinal control of the scalar branch y_b^(ab).
```
