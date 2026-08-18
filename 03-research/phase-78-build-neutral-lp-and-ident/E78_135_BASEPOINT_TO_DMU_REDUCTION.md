# E78.135 - The derivative-specific burden reduces from `SAFE-H + SAFE-Y` to `SAFE-Y` plus shared basepoint clauses

**Scope:** front B only, current exact `DMU-COUPLED-GENERATOR` burden.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** once the
two-generator denominator and derivative are viewed as functions of `mu`, both
`SAFE-F-NONVANISHING` and `SAFE-H-BOUND` follow from their shared basepoint
(`mu=0`) versions together with the single source bound `SAFE-Y-BOUND`.  So
the only genuinely new derivative-specific clause is `SAFE-Y-BOUND`.

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
P76.061: respected. The reduction uses only the exact paired two-generator
         identities before any inversion estimate.
E72.16/E77.7az: respected. This is front B; planted separation is admissible.
```

## 1. Exact `mu`-transport identities

E78.103 proved the exact derivative formulas

```text
partial_mu F_b(z;mu)   = Y_b(z;mu) + Y_b^bd(mu),                            (R-1)
partial_mu F_b'(z;mu)  = Y_b'(z;mu).                                        (R-2)
```

Therefore, for every `|mu|<=eta`,

```text
F_b(z;mu)  = F_b(z;0)  + int_0^mu [Y_b(z;t)+Y_b^bd(t)] dt,                  (R-3)
F_b'(z;mu) = F_b'(z;0) + int_0^mu Y_b'(z;t) dt.                             (R-4)
```

These are exact fundamental-theorem-of-calculus identities inside the same
finite package.

## 2. Shared basepoint clauses

At `mu=0`, the two-generator package is exactly the fixed-`L` IDENT package of
E78.6 / P76.041:

```text
F_b(z;0)  = 1 + W_{L,N}(z),                                                  (R-5)
F_b'(z;0) = W'_{L,N}(z).                                                     (R-6)
```

So define the shared basepoint conditions

```text
BASE-F-NONVANISHING(L,K):
  there exist m>0, N_0 such that for all N>=N_0, sigma in K,
  |F_b(i sigma;0)| >= 2m;                                                    (R-7)

BASE-H-BOUND(L,K):
  there exist M_0, N_0 such that for all N>=N_0, sigma in K,
  |F_b'(i sigma;0)| <= M_0.                                                  (R-8)
```

These are not new derivative objects: by `(R-5)`--`(R-6)` they belong to the
same fixed-`L` two-generator front as `1+W_{L,N}` and `W'_{L,N}`.

## 3. The single genuinely new clause

E78.104 already isolated

```text
SAFE-Y-BOUND(L,K,eta):
  there exists N_Y such that for all N>=N_Y, sigma in K, |t|<=eta,
  |Y_b(i sigma;t)| + |Y_b^bd(t)| + |Y_b'(i sigma;t)| <= N_{L,K,eta}.         (R-9)
```

This is the only clause involving the new `mu`-derivative source solve `y_b`.

## 4. Exact implication to `SAFE-F` and `SAFE-H`

Assume `(R-7)` and `(R-9)`.  Then for `N>=max(N_0,N_Y)`, `sigma in K`,
`|mu|<=eta`,

```text
|F_b(i sigma;mu)-F_b(i sigma;0)|
 <= |mu| sup_{|t|<=eta} (|Y_b(i sigma;t)|+|Y_b^bd(t)|)
 <= eta N_{L,K,eta}.                                                            (R-10)
```

Hence if

```text
eta N_{L,K,eta} <= m,                                                        (R-11)
```

then

```text
|F_b(i sigma;mu)|
 >= |F_b(i sigma;0)| - |F_b(i sigma;mu)-F_b(i sigma;0)|
 >= 2m - m = m > 0,                                                         (R-12)
```

which is exactly `SAFE-F-NONVANISHING`.

Likewise, from `(R-4)` and `(R-9)`,

```text
|F_b'(i sigma;mu)|
 <= |F_b'(i sigma;0)| + |mu| sup_{|t|<=eta}|Y_b'(i sigma;t)|
 <= M_0 + eta N_{L,K,eta}.                                                  (R-13)
```

So `BASE-H-BOUND + SAFE-Y-BOUND` implies `SAFE-H-BOUND`.

Therefore:

```text
BASE-F-NONVANISHING
+ BASE-H-BOUND
+ SAFE-Y-BOUND
=> SAFE-F-NONVANISHING + SAFE-H-BOUND + SAFE-Y-BOUND.                       (R-14)
```

Combining with E78.104 `(L-9)`:

```text
BASE-F-NONVANISHING
+ BASE-H-BOUND
+ SAFE-Y-BOUND
=> DMU-COUPLED-GENERATOR
=> PAIRED-DMU-LOCAL.                                                        (R-15)
```

## 5. Why this is a genuine reduction

Before this note, the derivative package appeared to require three clauses:

```text
SAFE-F-NONVANISHING + SAFE-H-BOUND + SAFE-Y-BOUND.                           (R-16)
```

After `(R-14)`--`(R-15)`, only one clause is genuinely new on the derivative
side:

```text
new derivative clause: SAFE-Y-BOUND;                                        (R-17)
shared basepoint clauses: BASE-F-NONVANISHING, BASE-H-BOUND.                (R-18)
```

This is strictly less new information than carrying `(R-16)` as if all three
clauses were born under `MU-DIR`.

## 6. What this does not prove

This note does **not** prove any of the three clauses theorem-grade.  In
particular:

```text
1. BASE-F-NONVANISHING remains tied to the fixed-`L` denominator front;
2. BASE-H-BOUND remains tied to fixed-`L` control of W'_{L,N};
3. SAFE-Y-BOUND remains the genuinely new derivative source burden.         (R-19)
```

The point is structural: the derivative route introduces only `(R-19.3)` as
new work.

## 7. Consequence

The candid derivative-side burden is now:

```text
shared fixed-`L` basepoint clauses for F_b and F_b'
+ the single new source clause SAFE-Y-BOUND.                                 (R-20)
```

So the next admissible front-B step is to attack `SAFE-Y-BOUND` directly, or
to reduce it further by an exact cofinal implication, while treating the
denominator/basepoint derivative as inherited clauses from the same fixed-`L`
two-generator package.

## 8. Status

```text
candidate closure - pending review

proved:
  exact mu-transport identities for F_b and F_b' from the source package y_b;

proved:
  BASE-F-NONVANISHING + BASE-H-BOUND + SAFE-Y-BOUND
  => SAFE-F-NONVANISHING + SAFE-H-BOUND + SAFE-Y-BOUND
  => DMU-COUPLED-GENERATOR;

reduced:
  the genuinely new derivative-specific burden to the single clause
  SAFE-Y-BOUND, modulo shared fixed-`L` basepoint clauses;

next:
  attack SAFE-Y-BOUND directly, or reduce it cofinally without descending back
  into audited finite portraits.
```
