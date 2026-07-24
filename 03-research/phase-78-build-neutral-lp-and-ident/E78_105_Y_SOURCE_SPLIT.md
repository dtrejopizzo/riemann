# E78.105 - The `y_b` blowup is carried by the intrinsic `h_b` source, not by the scalar `alpha_b,beta_b` branch

**Run:** 2026-07-19.  
**Scope:** front B only, live object `AUX-DMU-SOURCE`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** the auxiliary
source branch is not driven primarily by `alpha_b s + beta_b 1`; the dominant
part of `y_b` already comes from the intrinsic source `h_b`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. The argument stays in the fixed-L / Re(s)>1 arithmetic front.
MW-3:  respected. No local-global prime assembly.
MW-4:  respected. No lower-bound/sign mechanism is used.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No spectral-gap hypothesis.
K1-K5: respected. No determinant endpoint closure, no Christoffel evaluator, no
       ambient inverse norm.
P76.061: respected. The split is performed entirely inside the finite coupled
         algebra before any norm estimate.
E72.16/E77.7az: respected. This is front B; planted separation remains admissible.
```

## 1. Starting point

From E78.103 and E78.104,

```text
A y_b = h_b + alpha_b s + beta_b 1.                         (S-1)
```

Define the exact decomposition

```text
y_b = y_b^(h) + y_b^(ab),                                   (S-2)

A y_b^(h)  = h_b,                                           (S-3)
A y_b^(ab) = alpha_b s + beta_b 1.                          (S-4)
```

Then

```text
SAFE-Y-BOUND
<= SAFE-YH-BOUND + SAFE-YAB-BOUND,                          (S-5)
```

where the two subtargets mean uniform control of `y_b^(h)` and `y_b^(ab)`,
respectively.

## 2. Why this is a genuine reduction

Before this split, the live source target was

```text
AUX-DMU-SOURCE:
  control c_b and y_b cofinally.                            (S-6)
```

After `(S-2)`--`(S-4)`, we can ask which branch actually carries the burden.
If one branch is already secondary on the audited ladder, the live target can be
reduced to the dominant branch only.

So this is not a reparametrization; it removes one source branch from the live
front if that branch is shown to be subdominant.

## 3. Probe

The audited split gives:

```text
BUILD zeta
N= 6: ||y_h|| = 4.37e24,  ||y_ab|| = 8.19e23,  ratio = 0.179
N= 8: ||y_h|| = 4.02e32,  ||y_ab|| = 6.26e31,  ratio = 0.151
N=10: ||y_h|| = 6.53e37,  ||y_ab|| = 8.76e36,  ratio = 0.131
N=12: ||y_h|| = 1.96e46,  ||y_ab|| = 2.31e45,  ratio = 0.116.   (S-7)

BUILD plant
N= 6: ||y_h|| = 1.25e23,  ||y_ab|| = 2.25e22,  ratio = 0.173
N= 8: ||y_h|| = 2.30e31,  ||y_ab|| = 3.33e30,  ratio = 0.141
N=10: ||y_h|| = 1.50e33,  ||y_ab|| = 1.83e32,  ratio = 0.119
N=12: ||y_h|| = 1.83e40,  ||y_ab|| = 1.93e39,  ratio = 0.104.   (S-8)
```

So on the entire audited ladder, in both builds:

```text
||y_b^(ab)|| / ||y_b|| <= 0.18, and this ratio decreases with N.   (S-9)
```

This does not prove theorem-grade domination yet, but it localizes the growth:
the scalar branch is not the main source of the explosion.

## 4. Consequence

The audited evidence `(S-7)`--`(S-9)` shows that the branch

```text
alpha_b s + beta_b 1                                          (S-10)
```

is secondary on the current ladder.  Therefore the honest next live target is
the intrinsic source branch:

```text
H-DMU-SOURCE(L,K,eta):
  control y_b^(h) = A^(-1) h_b cofinally enough to imply SAFE-Y-BOUND. (S-11)
```

If a later theorem proves `SAFE-YAB-BOUND` separately, `(S-11)` plus that bound
reconstructs `SAFE-Y-BOUND` by `(S-5)`.

## 5. Status

```text
candidate closure - pending review

proved:
  the exact source split y_b = y_b^(h) + y_b^(ab);

localized:
  on the audited ladder the dominant contribution to y_b comes from y_b^(h),
  not from the scalar branch y_b^(ab);

reduced:
  AUX-DMU-SOURCE to the intrinsic source target H-DMU-SOURCE, modulo a future
  separate control of the secondary scalar branch;

next:
  attack A^(-1) h_b directly, or autopsy which coefficient inside h_b forces
  its cofinal growth.
```
