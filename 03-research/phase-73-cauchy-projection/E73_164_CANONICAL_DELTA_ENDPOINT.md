# E73.164 - Canonical delta endpoint

Date: 2026-07-12.

## 1. Purpose

E73.163 shows that the strong coefficient-image theorem fails in canonical
coordinates.  After eliminating generated rational and endpoint slots, the
remaining defect lives in the unique `cauchy0` slots:

```text
D_A(d)=sum_{gamma in K_L} delta_A(gamma)DD_L(-gamma,d).
```

E73.164 asks whether this is a genuine simplification of the original
source coefficients

```text
Pi_A(gamma)=Pi_conf(A,i gamma),
```

or merely another coordinate form of the same `CC-PROJ / CRIT-DIV`
obstruction.

## 2. Definition of delta

Use the canonical source basis:

```text
cauchy0_gamma(d)=DD_L(-gamma,d),
rat_{gamma,beta,r}(d)=DD_L(-gamma,d)/(d^2+beta^2)^r,   r>=1,
endpoint_{gamma,q}(d)=d^(2q)DD_L(-gamma,d).
```

Let `B_L(A,K)` be the coefficient action of `(H_L-mu_L I)` from the
canonical primitive module into this source basis.

Choose `y_A` by matching all non-endpoint coefficients in least squares:

```text
y_A = argmin_y ||s_A^principal-B_L(A,K)^principal y||.
```

Then define the canonical defect:

```text
delta_A(gamma)
= [s_A-B_L(A,K)y_A]_{cauchy0_gamma}.
```

This is not an ambient image projection.  It is the principal coefficient
defect after rational and endpoint slots have been separated.

## 3. Result

The numerical audit compares:

```text
||delta_A||/||Pi_A||,
cos(delta_A,Pi_A),
e^(alpha L)|sum_gamma Pi_A(gamma)<xi,DD_gamma>|,
e^(alpha L)|sum_gamma delta_A(gamma)<xi,DD_gamma>|.
```

The results show:

```text
||delta_A||/||Pi_A|| ranges roughly from 0.07 to 0.75;
cos(delta_A,Pi_A) is comparable to the norm ratio, so delta is often aligned
with a nontrivial part of Pi;
the scalar ratio expDelta/expPi is usually order one and sometimes larger.
```

Thus `delta_A` removes some coefficient mass, but it does not uniformly
improve the load-bearing scalar.

## 4. Meaning

The canonical coefficient reduction is useful diagnostically:

```text
it strips away rational and endpoint clutter and isolates the true
principal obstruction.
```

But it does not close the theorem.  The remaining scalar estimate is still:

```text
e^(alpha L)|<xi_L,D_A>| <= L^B.
```

This is equivalent in difficulty to the surviving `CRIT-DIV` gate.  The
proof cannot come from saying that `delta_A` is small as a coefficient vector;
it is not small enough, and its scalar contribution is not uniformly smaller
than the original source scalar.

## 5. Updated final form of the Phase 73 obstruction

The current clean endpoint is:

```text
CANON-CRIT-DIV:
For every natural-height off-line Hermite cluster A with real part alpha>0,
let delta_A be the canonical cauchy0 coefficient defect after eliminating
the finite rational action of (H_L-mu_L I).  Then

e^(alpha L)
|sum_{gamma in K_L} delta_A(gamma)
  (1-e^(i gamma L)) sum_n xi_L(n)/(-gamma-d_n)|
<= L^B.
```

This is finite and explicit.  It contains:

```text
1. no zero tail;
2. no Cauchy inverse hidden in an infinite operator;
3. no pseudoinverse or ambient image projection;
4. no generic positivity assumption.
```

It remains the analytic theorem to prove.

## 6. Relation to earlier gates

`CANON-CRIT-DIV` is not independent of `CRIT-DIV`; it is a cleaned version:

```text
CRIT-DIV:
Pi_conf(A,K_L) applied to critical cancelled Cauchy data is small.

CANON-CRIT-DIV:
the residual cauchy0 component after finite rational action elimination is
small against the same critical cancelled Cauchy data.
```

The advantage is bookkeeping, not an automatic bound.

## 7. Status

```text
proved numerically: canonical elimination localizes the obstruction to
                  cauchy0 critical atoms;
falsified:        canonical delta is uniformly smaller in the scalar channel;
remaining:        prove CANON-CRIT-DIV directly from the finite CCM/Feshbach
                  equation or reduce it to a still sharper finite identity.
```

