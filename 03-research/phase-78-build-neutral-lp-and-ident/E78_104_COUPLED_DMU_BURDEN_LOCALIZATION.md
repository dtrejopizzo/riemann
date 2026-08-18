# E78.104 - The coupled `d_mu` burden localizes to the auxiliary branch `c_b -> y_b`

**Run:** 2026-07-19.  
**Scope:** front B only, live object `DMU-COUPLED-GENERATOR` from E78.103.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** within the exact
coupled-generator derivative package, the hard growth does not originate in the
safe denominator `F_b`; it is carried by the auxiliary branch
`c_b -> (alpha_b,beta_b) -> y_b`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. The argument stays entirely inside the fixed-L / Re(s)>1 front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used as a forcing step.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No spectral-gap hypothesis.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator, no
       ambient inverse norm.
P76.061: respected. The derivative remains in the paired finite algebra before
         any estimate.
E72.16/E77.7az: respected. This is front B, so planted separation remains admissible.
```

## 1. Starting point from E78.103

E78.103 proved the exact identity

```text
partial_mu(F_b'/F_b)
 = Y_b'/F_b - F_b' (Y_b+Y_b^bd)/F_b^2,                     (L-1)
```

where

```text
A c_b = g_b,
A y_b = h_b + alpha_b s + beta_b 1,                       (L-2)
```

and

```text
alpha_b = 4 v^T c_b / L^2,
beta_b  = -4 u^T c_b / L^2.                               (L-3)
```

So the exact derivative package is

```text
(F_b,F_b',Y_b,Y_b' ; c_b,y_b ; alpha_b,beta_b).            (L-4)
```

## 2. Elementary burden split

For one fixed `L`, one safe compact `K`, and one box `|mu|<=eta`,

```text
|partial_mu(F_b'/F_b)|
 <= |Y_b'|/|F_b|
  + |F_b'| |Y_b+Y_b^bd| / |F_b|^2.                        (L-5)
```

Therefore any proof of `DMU-COUPLED-GENERATOR` can be split into:

```text
SAFE-F-NONVANISHING:
  |F_b(i sigma;mu)| >= m_{L,K,eta} > 0;                   (L-6)

SAFE-H-BOUND:
  |F_b'(i sigma;mu)| <= M_{L,K,eta};                       (L-7)

SAFE-Y-BOUND:
  |Y_b(i sigma;mu)| + |Y_b^bd(mu)| + |Y_b'(i sigma;mu)|
  <= N_{L,K,eta}.                                          (L-8)
```

Then `(L-5)` yields

```text
SAFE-F-NONVANISHING + SAFE-H-BOUND + SAFE-Y-BOUND
=> DMU-COUPLED-GENERATOR.                                  (L-9)
```

This is a genuine reduction: the predecessor asked for a bound on the whole
logarithmic derivative, while the new split isolates the denominator side from
the auxiliary source side.

## 3. Probe

Companion files:

```text
E78_104_coupled_dmu_burden_probe.py
E78_104_coupled_dmu_burden_results.json
```

The additional burden-localization sweep gives:

```text
BUILD zeta
N= 6: min|F|=2.57e3,   ||c||=5.80e3,   ||y||=4.58e24
N= 8: min|F|=3.25e6,   ||c||=6.06e6,   ||y||=4.15e32
N=10: min|F|=7.98e6,   ||c||=1.27e7,   ||y||=6.70e37
N=12: min|F|=5.28e10,  ||c||=7.31e10,  ||y||=2.00e46      (L-10)

BUILD plant
N= 6: min|F|=6.24e3,   ||c||=1.35e4,   ||y||=1.30e23
N= 8: min|F|=1.12e9,   ||c||=1.94e9,   ||y||=2.36e31
N=10: min|F|=1.96e7,   ||c||=2.86e7,   ||y||=1.53e33
N=12: min|F|=2.63e10,  ||c||=3.32e10,  ||y||=1.86e40.     (L-11)
```

On the audited safe ladder:

```text
1. F_b is not small; its minimum size is large in both builds.
2. The auxiliary branch c_b grows, and y_b grows much faster.
3. The huge values of partial_mu(F_b'/F_b) seen in E78.103 are therefore
   consistent with the numerator/source branch, not with loss of the
   denominator F_b.                                        (L-12)
```

This is not yet a theorem of nonvanishing, but it localizes the live burden.

## 4. Consequence

After `(L-9)` and the audit `(L-10)`--`(L-12)`, the candid next target is no
longer the full `DMU-COUPLED-GENERATOR`, and it is not "maybe `F_b` has zeros".
The active source term is:

```text
AUX-DMU-SOURCE(L,K,eta):
  control c_b and y_b cofinally enough to obtain SAFE-Y-BOUND.      (L-13)
```

So the next admissible attacks are:

```text
1. prove SAFE-F-NONVANISHING from the existing fixed-L transfer package, if
   available at theorem-grade;
2. attack AUX-DMU-SOURCE directly through the inhomogeneous equations for c_b
   and y_b;
3. if that fails, autopsy which coefficient inside
   h_b + alpha_b s + beta_b 1
   causes the cofinal blowup.                                (L-14)
```

## 5. Status

```text
candidate closure - pending review

proved:
  SAFE-F-NONVANISHING + SAFE-H-BOUND + SAFE-Y-BOUND
  => DMU-COUPLED-GENERATOR;

localized:
  on the audited safe ladder the derivative burden is carried by the auxiliary
  branch c_b -> y_b, not by small F_b;

reduced:
  the next live object from the whole coupled derivative package to the
  auxiliary source control AUX-DMU-SOURCE;

next:
  attack c_b / y_b directly, or autopsy the exact source coefficient that
  forces their cofinal growth.
```
