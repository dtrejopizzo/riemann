# E78.44 - The denominator direction law is exactly a centered quotient

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.43 reduced the denominator side to the directional defect

```text
DIRINC_N = det(Delta d_N, d_N) / (|Delta d_N| |d_N|),    (DCQ-1)
```

with

```text
d_N := 1-theta_N,
Delta d_N := d_N+2 - d_N.                                 (DCQ-2)
```

This note identifies that direction defect with the argument of a single
centered quotient.

## 2. Exact centered quotient identity

Whenever `d_N != 0`, define

```text
w_N := Delta d_N / d_N = (d_N+2 / d_N) - 1.              (DCQ-3)
```

Then

```text
Delta d_N = w_N d_N,                                      (DCQ-4)
```

so the angle from `d_N` to `Delta d_N` is exactly `arg(w_N)`. Therefore

```text
DIRINC_N = sin(arg(w_N)) = Im(w_N) / |w_N|.              (DCQ-5)
```

Equivalently,

```text
Im((1-theta_N+2)/(1-theta_N))
 = (|Delta d_N|/|d_N|) DIRINC_N
 = Im(w_N).                                               (DCQ-6)
```

Thus the denominator obstruction is exactly the imaginary part of the centered
shell quotient `w_N = Delta d_N / d_N`, while the direction defect is simply
its normalized imaginary part.

## 3. Conditional half-plane corollary

If a cofinal ladder satisfies

```text
Re(w_N) <= -c < 0,                                        (DCQ-7)
```

then `(DCQ-5)` gives the quantitative bound

```text
|DIRINC_N| <= |Im(w_N)| / c.                              (DCQ-8)
```

So, under a negative-real-part barrier, denominator direction control reduces
to smallness of the centered imaginary part alone.

This corollary is conditional because the half-plane barrier is not yet proved
cofinally; it is only audited numerically below.

## 4. Probe audit

Companion:

```text
E78_44_den_centered_quotient_probe.py
E78_44_den_centered_quotient_results.json
```

The probe reconstructs `w_N = Delta d_N / d_N` directly from the certified
Phase-77 theta rows and verifies `(DCQ-5)` to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0:
  N=10->12  w_N = -0.5057771151848590 + 0.0009740448567951873 i
  N=12->14  w_N = -0.3951413384976973 - 0.0015061500854115753 i
  N=20->22  w_N = -0.2668712275493552 - 0.0006119092046593115 i

sigma=3.0:
  N=10->12  w_N = -0.4849446991894159 + 0.0030512468816820130 i
  N=12->14  w_N = -0.3819257889454510 - 0.0046017478508082510 i
  N=20->22  w_N = -0.2641863357714149 - 0.0018405994704980577 i.   (DCQ-9)
```

Across the audited zeta ladder:

```text
min(-Re(w_N))        = 0.2617363100173541
median(-Re(w_N))     = 0.30723536116529215
max |Im(w_N)|        = 0.004601747850808251
median |Im(w_N)/Re(w_N)| = 0.004058996163569521
max    |Im(w_N)/Re(w_N)| = 0.012048801060316722.         (DCQ-10)
```

So the audited zeta centered quotient sits stably in the left half-plane and is
very close to the negative real axis.

### Planted build

Representative rows:

```text
sigma=1.0:
  N=10->12  w_N =  6.453477023497479  + 2.2988076646191633 i
  N=12->14  w_N = -0.4580720697283445 + 0.2137902151325551 i

sigma=3.0:
  N=10->12  w_N =  6.238679573947946  + 2.2817795781118035 i
  N=12->14  w_N = -0.4812804491208942 + 0.2603806034900981 i.      (DCQ-11)
```

Across the audited planted ladder:

```text
median |DIRINC_N|    = 0.11949996690414152
median |Im(w_N)/Re(w_N)| = 0.12040318836238478
max    |Im(w_N)/Re(w_N)| = 0.541016374061545.            (DCQ-12)
```

The plant fails already at the centered-quotient level: early steps leave the
left half-plane entirely, and even the steps that return there keep an order-one
imaginary-to-real skew.

## 5. Consequence

This yields a smaller denominator endpoint than E78.43:

```text
DEN-CENTERED-QUOTIENT-HORIZONTALITY:
  prove that w_N = Delta d_N / d_N is asymptotically real
  (preferably with Re(w_N) < 0 on a cofinal safe ladder).         (DCQ-13)
```

Then `(DCQ-5)` gives denominator direction control immediately, and `(DCQ-6)`
returns to the denominator rigidity chain.

## 6. Honest reading

This note still does not prove the left-half-plane barrier or the centered
imaginary part is small cofinally. It proves something cleaner: the live
denominator content is no longer an angle in the plane, but the skew of a single
normalized shell increment `Delta d_N / d_N`.

That is a stricter finite quotient target than E78.43.

## 7. Status

```text
proved:
  DIRINC_N = Im(Delta d_N / d_N) / |Delta d_N / d_N| exactly;

proved:
  Im((1-theta_N+2)/(1-theta_N)) = Im(Delta d_N / d_N) exactly;

observed:
  on the audited zeta ladder, Delta d_N / d_N stays in the left half-plane and
  within about 1.21e-2 relative skew of the negative real axis;

observed:
  the planted build violates that horizontality strongly at the early failing
  steps;

reduced:
  DEN-DIRECTIONAL-INCREMENT-SMALLNESS to DEN-CENTERED-QUOTIENT-HORIZONTALITY;

next:
  either prove a finite recurrence or quotient law forcing the centered shell
  increment Delta d_N / d_N to stay nearly real on the safe ladder, or autopsy
  that skew into an even smaller signed increment residual.
```
