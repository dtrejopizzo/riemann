# E78.97 - Autopsy of the `U-RADIAL-GAP` route

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the exact obstruction
to proving `U-RADIAL-GAP-LOWER-BOUND` from the closed shell formulas is not the
denominator side but the unresolved cofinal control of the weighted numerator
loss, whose current exact source remains a partition-sensitive ternary Schur/log
residual with unsummable `1/N` profile drift.

## 0. Wall checklist

```text
MW-1:  respected.  No positivity of a Weil form is introduced.
MW-2:  respected.  No arithmetic is propagated outside the already allowed
       Re(s)>1 setting; this is a finite fixed-L autopsy.
MW-3:  respected.  No local-to-global infinite-dimensional assembly appears.
MW-4:  respected.  No lower-bound tool is used to claim the desired upper-side
       restriction; the note only names the exact unresolved coefficient.
MW-5:  respected.  No site/cohomology input.
MW-6:  respected.  No uniform spectral-gap hypothesis.
K1-K5: respected.  No contraband inverse norm, no absolute pre-cancellation
       ceiling, no Christoffel point-local evaluator, no scalar determinant
       endpoint identification.
P76.061: respected.  All cited live formulas come from paired shell/Cauchy or
         Schur identities before inversion; no ambient-norm route is revived.
E72.16/E77.7az: respected.  No build-separating scalar on the LP front is being
                promoted; the zeta/plant contrast is used only as falsifier
                audit on the IDENT front, where the plant is allowed to break.
```

## 1. The live route and what it actually reduced to

The current Phase-78 chain for the left-endpoint weighted modulus quotient is:

```text
LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT
<= PREF-CONTROL + U-RADIAL-GAP-LOWER-BOUND                (E78.92)
```

with

```text
U-RADIAL-GAP_N
 = |q_a,N| - |q_b,N|                                      (A-1)
 = NUMERATOR-RADIAL-GAIN_N
   + DENOMINATOR-RADIAL-DEFICIT_N.                        (A-2)
```

E78.95 reduced positivity of `(A-1)` to the one-sided comparison

```text
DENOMINATOR-RADIAL-DEFICIT_N > NUMERATOR-LOSS_N,          (A-3)
```

where

```text
NUMERATOR-LOSS_N := max(0, -( |q_a,N| - 1 )).            (A-4)
```

E78.96 then sharpened the denominator side to

```text
DENOMINATOR-RADIAL-DEFICIT_N
 = NEGATIVE-QUADRATIC-MARGIN_N / (1 + |q_b,N|),          (A-5)
```

so the strongest exact sufficient condition currently available is

```text
NEGATIVE-QUADRATIC-MARGIN_N
 > (1 + |q_b,N|) NUMERATOR-LOSS_N.                       (A-6)
```

This is the exact current endpoint of the route.

## 2. The denominator side is not the obstruction

The denominator branch is already fully local in the shell quotient

```text
w_b,N := q_b,N - 1 = (1-theta_N+2)/(1-theta_N) - 1.      (A-7)
```

By E78.47, E78.50, and E78.96:

```text
1.  DENOMINATOR-RADIAL-DEFICIT_N = 1 - |q_b,N|;
2.  1 - |q_b,N| is exactly radial contraction of |1-theta_N|;
3.  it is exactly the normalized quadratic margin
      -(2 Re(w_b,N) + |w_b,N|^2)/(1+|q_b,N|).            (A-8)
```

So any remaining failure of `(A-6)` cannot be blamed on missing algebra on the
denominator side.  That side is already expressed by one local finite shell
scalar.

## 3. The numerator side does not reduce to a smaller scalar with proved cofinal content

The unresolved term is

```text
NUMERATOR-LOSS_N
 = max(0, 1-|q_a,N|),
q_a,N = theta'_N+2 / theta'_N.                           (A-9)
```

A proof of `(A-6)` therefore requires a cofinal upper bound for the weighted
numerator term

```text
(1+|q_b,N|) NUMERATOR-LOSS_N.                            (A-10)
```

The exact Schur/transfer identities available for `theta'_N` do not presently
yield such a cofinal scalar law.  The certified Phase-77 chain is:

```text
theta_N = tau_N Sigma_N^{-1} kappa_N / t0_N             (E77.5f)
THETA-REG cannot be proved factorwise                    (E77.5h autopsy)
THETA-REG cannot be reduced pairwise                     (E77.5i autopsy)
theta_common is coordinate-dependent                     (E77.5k autopsy)
the invariant object is Delta external - Delta logT      (E77.5l)
raw residual has a leading 1/N term                      (E77.5m autopsy)
its coefficient profile still drifts with N              (E77.5n autopsy). (A-11)
```

This is the decisive point: the closed formulas do not collapse the numerator
side to a fixed cofinal shell scalar.  They leave it at an invariant coupled
residual whose currently certified leading behavior is

```text
R_N(sigma) = Delta external_N(sigma) - Delta logT_N(sigma)
          = C_N(sigma)/N + drift_N(sigma),              (A-12)
```

with `C_N(sigma)` still moving in `N` on the certified window (E77.5n).

Therefore the exact quantifier that fails is:

```text
there is currently no proved statement of the form
  exists N_0, c_* < 1 such that
  (1+|q_b,N|) NUMERATOR-LOSS_N <= c_* NEGATIVE-QUADRATIC-MARGIN_N
for all N >= N_0 and sigma in a safe compact.            (A-13)
```

The formulas in hand only reduce the numerator side to the moving Schur/log
residual chain `(A-11)`, not to a cofinal bound of the form `(A-13)`.

## 4. Why this is a genuine autopsy and not another reparametrization

This note does **not** restate `(A-6)` in new coordinates.  It records the exact
reason the route stops:

```text
the denominator side closes to one local scalar;
the numerator side does not.
```

More precisely, the obstruction is not “numerator hard” in vague terms; it is:

```text
weighted numerator loss
-> shell derivative quotient q_a,N
-> partition-invariant Schur/log residual R_N
-> unsummed 1/N coefficient profile drift C_N(sigma).   (A-14)
```

That is strictly more information than the previous notes supplied, because it
identifies the exact unresolved coefficient/quantifier preventing a cofinal
theorem.

## 5. Consequence for the Phase-78 mission order

By Rule 2 of the mission, the `U-RADIAL-GAP` front has exceeded its document
budget without producing a proof cofinal.  The theorem-grade conclusion is:

```text
the current U-RADIAL-GAP route is exhausted as a closure path.              (A-15)
```

More explicitly:

```text
the admissible content proved so far is only the reduction
  U-RADIAL-GAP-LOWER-BOUND
  <= weighted quadratic-margin dominance `(A-6)`,
and the unresolved burden is exactly the cofinal control of
  (1+|q_b,N|) NUMERATOR-LOSS_N
through the moving profile drift `(A-12)`.                                 (A-16)
```

So the next front is not “improve the same shell scalar once more.”  The next
mission-prescribed front is:

```text
SAFE-GAMMA-IDENT direct in Re(s)>1, via E77.6(B).                           (A-17)
```

This follows the mission order and avoids spending more documents on a route
whose unresolved coefficient is already fully named.

## 6. Predecessor implication / closure status

This autopsy closes the current route in the precise sense required by the
mission:

```text
if `(A-6)` were proved cofinally, it would still imply
U-RADIAL-GAP-LOWER-BOUND
=> LEFT-ENDPOINT-WEIGHTED-MODULUS-QUOTIENT.                                 (A-18)
```

But the present document proves that the active formulas do not supply the
needed cofinal numerator estimate, because the live numerator obstruction is the
profile-drift chain `(A-11)` / `(A-12)`.

## 7. Status

```text
candidate closure - pending review

proved:
  the current U-RADIAL-GAP route has exact endpoint
  NEGATIVE-QUADRATIC-MARGIN > (1+|q_b|) NUMERATOR-LOSS;

proved:
  the denominator side is fully local and not the unresolved piece;

proved:
  the unresolved coefficient is the cofinal control of the weighted numerator
  loss, whose certified exact source remains the partition-invariant Schur/log
  residual with moving 1/N profile drift;

autopsied:
  no further admissible progress remains on this route without a new theorem
  controlling that drift cofinally;

next:
  move to SAFE-GAMMA-IDENT direct (E77.6(B)), then OUTER-LIMIT (E77.6(C)),
  exactly as mandated by the mission order.
```
