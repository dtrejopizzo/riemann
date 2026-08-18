# E78.126 - `HALF-AXIS-MODE2(t)` reduces to a signed five-shell profile on the audited safe frontier

**Scope:** front B only, live object `HALF-AXIS-MODE2(t)`.  
**Class:** REDUCCION GENUINA.  
**What we know after this doc that we did not know before:** although the
half-axis transform is not a one-shell object, the first five positive shells
already reproduce it to audited precision once their alternating cancellation is
kept signed.

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
P76.061: respected. The reduction stays in the explicit safe-axis transform.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.125 autopsied the route

```text
zero mode + one/two monotone shells  =>  HALF-AXIS-MODE2(t).             (F-1)
```

The failure was not "too many terms forever", but a more specific one:
alternating cancellation among several early shells.

So the candid next question is whether preserving that signed short profile
already closes the audited safe frontier.

## 2. Five-shell profile

From E78.124,

```text
HALF-AXIS-MODE2(t)
 = -v_2(0)/t + sum_{n>0} K_t(d_n) v_2(n),                   (F-2)
```

with

```text
K_t(d_n) = -2t/(t^2+d_n^2).                                (F-3)
```

Define the signed five-shell truncation

```text
FIVE-SHELL-MODE2(t)
 := -v_2(0)/t + sum_{1<=n<=5} K_t(d_n) v_2(n).             (F-4)
```

This is strictly less information than the full positive-half transform `(F-2)`.

## 3. Probe

Using the audited localization data from

```text
E78_125_half_axis_localization_probe.py
E78_125_half_axis_localization_results.json,
```

the five-shell partial ratio is:

```text
BUILD zeta
N=8:
  t=0.6  -> 1.00015865
  t=1.0  -> 1.00050602
  t=2.0  -> 1.00335520
N=12:
  t=0.6  -> 1.00077855
  t=1.0  -> 1.00257124
  t=2.0  -> 1.01908958.                                     (F-5)

BUILD plant
N=8:
  t=0.6  -> 0.99999809
  t=1.0  -> 0.99999314
  t=2.0  -> 0.99993143
N=12:
  t=0.6  -> 0.99998926
  t=1.0  -> 0.99996115
  t=2.0  -> 0.99959843.                                     (F-6)
```

So on the audited safe frontier the five-shell truncation already reproduces the
full transform to within about `2e-2`, and usually much better.

## 4. Why this is a genuine reduction

The predecessor `HALF-AXIS-MODE2(t)` still required the entire positive half
axis.

The new object `FIVE-SHELL-MODE2(t)` keeps only the zero term plus the first
five positive shells with their exact signed kernel weights.

That is strictly less information than the full half-axis sum.

So this is a genuine reduction on the audited safe frontier:

```text
FIVE-SHELL-MODE2(t)  ~=  HALF-AXIS-MODE2(t)                (F-7)
```

with the approximation quality explicitly measured in `(F-5)`--`(F-6)`.

## 5. Consequence

The live object on this branch is now no longer an infinite half-axis transform
for exploratory purposes on the audited frontier. It is the finite signed
profile

```text
FIVE-SHELL-MODE2(t).                                        (F-8)
```

This is the sharpest explicit finite profile reached so far on the safe-axis
route.

The next admissible question is whether those five signed shell coefficients can
be recognized inside the coupled finite package, or whether that bridge fails
for a named reason.

## 6. Status

```text
candidate closure - pending review

proved:
  the five-shell signed profile reproduces the audited safe transform to
  displayed precision;

reduced:
  HALF-AXIS-MODE2(t) on the audited safe frontier to the finite profile
  FIVE-SHELL-MODE2(t);

next:
  identify the five-shell signed profile inside a finite coupled object, or
  autopsy the exact reason that identification fails.
```
