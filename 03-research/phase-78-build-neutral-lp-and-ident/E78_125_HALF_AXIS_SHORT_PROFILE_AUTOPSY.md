# E78.125 - `HALF-AXIS-MODE2(t)` is not a one-shell or monotone-short-profile object

**Scope:** front B only, live object `HALF-AXIS-MODE2(t)`.  
**Class:** AUTOPSIA theorem-grade.  
**What we know after this doc that we did not know before:** the half-axis
transform does not localize to the zero mode, to the first positive shell, or
to any monotone short truncation. Its value is produced by alternating
cancelation among several early positive shells.

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
P76.061: respected. The autopsy stays inside the exact safe-axis transform.
E72.16/E77.7az: respected. This is front B; planted failure is admissible.
```

## 1. Starting point

E78.124 reduced the live object to

```text
HALF-AXIS-MODE2(t)
 = -v_2(0)/t - 2t sum_{n>0} v_2(n)/(t^2+d_n^2).            (P-1)
```

The next natural hope is that `(P-1)` might be controlled by the zero mode plus
the first one or two positive shells.

## 2. Probe

Companion files:

```text
E78_125_half_axis_localization_probe.py
E78_125_half_axis_localization_results.json
```

The audited localization pattern is:

```text
BUILD zeta
N=8,12:
  |zero term| / |full| ranges from 1.09 up to 2.55,
  after one shell the ratio ranges from 1.02 up to 1.49,
  after two shells it drops as low as 0.51,
  after three shells it overshoots again above 1,
  and only by four/five shells does it settle near 1.               (P-2)

BUILD plant
N=8,12:
  the same qualitative pattern holds, with zero term ratios
  1.18 to 4.11, strong undershoot after the first shell for large t,
  overshoot after the second shell, and stabilization only after
  several early shells.                                             (P-3)
```

So the transform is not produced by a single dominant shell, nor by a monotone
partial-sum law.

## 3. Autopsy

This closes the route

```text
HALF-AXIS-MODE2(t)  ?=  zero mode + one-shell or monotone short truncation. (P-4)
```

The exact failure is:

```text
the half-axis transform is built by alternating cancellation among several
early positive shells.                                              (P-5)
```

The zero term alone overshoots; the first shell partially cancels it; the
second shell often overshoots in the opposite direction; and only after several
terms does the sum settle near the full value.

Therefore the remaining live structure is not a one- or two-shell localization
problem. It is an organized short-profile cancellation problem.

## 4. Consequence

The honest next live object must preserve that multi-shell cancellation, e.g.

```text
1. a signed short-profile transform built from the first few positive shells,
   or
2. a finite coupled coefficient whose exact value already packages those
   cancellations.                                                   (P-6)
```

Any route that assumes a dominant zero term or a monotone first-shell closure
is now dead.

## 5. Status

```text
candidate closure - pending review

autopsied:
  the route "HALF-AXIS-MODE2(t) localizes to zero mode + one/few monotone
  shells";

proved:
  the transform is produced by alternating cancellation among several early
  shells on both builds;

closed:
  one-shell and monotone-short-profile explanations of HALF-AXIS-MODE2(t);

next:
  attack a signed short-profile package, or identify a finite coupled object
  that carries the same multi-shell cancellation.
```
