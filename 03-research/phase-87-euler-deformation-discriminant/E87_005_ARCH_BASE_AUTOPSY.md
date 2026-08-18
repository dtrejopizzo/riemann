# E87.005 - Archimedean-base autopsy and combined anomaly

## 1. Exact finite defect

Define

```text
D_{L,N,t}(s)
 =partial_s log C_{L,N,t}(s)
  -partial_s log E_{L,t}(s).                          (1.1)
```

The deformation identity gives

```text
D_{L,N,1}(s)
 =D_{L,N,0}(s)
  +integral_0^1 partial_s K_{L,N,t}(s)dt.              (1.2)
```

There is no algebraic reason for either term on the right to vanish
separately.

## 2. Finite-scale diagnostic against the correct primitive

At `L=2 log 6` and ten outer modes, compare the bordered current with the
finite product `E_{L,t}`, not with the complete outer product.  At
`sigma=(0.6,0.75,1,1.5,2)`, the defects are

```text
t=0
(-14.9976,-3.5906,-0.1434, 1.3706, 1.8168)

t=0.9
(-10.6431,-0.3304, 1.9410, 2.3281, 2.3122)

t=0.99
(-10.2283,-0.0294, 2.1182, 2.3840, 2.3175)

t=1
(-14.0606,-3.3324,-0.7241,-0.1240,-0.0953).           (2.1)
```

The arithmetic endpoint does not arise as a regular continuation of the
bulk values.  The endpoint layer changes the complete profile.

For comparison, at `t=1` the defect against the complete outer logarithmic
derivative is already

```text
(-0.0263,-0.0329,-0.0440,-0.0662,-0.0887).            (2.2)
```

The difference between (2.1) and (2.2) near `Re s=1` is the explicit missing
Euler tail.  It is not small at fixed `L`; it tends to zero only in the outer
limit on compact subsets of `Re s>1`.

## 3. Decision

The proposed proof split

```text
ARCH-BASE -> 0,
TANGENT-ANOMALY -> 0                                  (3.1)
```

is rejected as an estimation route.  It separates two terms whose exact
role is cancellation.  The admissible target is

```text
COMBINED-DEFORMATION-RDI:
D_{L,0}(s)
+integral_0^1 partial_s K_{L,t}(s)dt
->0                                                   (3.2)
```

after fixed-`L` convergence and then `L->infinity`, with the explicit Euler
tail retained until the outer step.

## 4. Correct bulk-layer organization

For `epsilon=epsilon(L)`, define

```text
BASE-BULK_L(s)
 =D_{L,0}(s)
  +integral_0^(1-epsilon)partial_s K_{L,t}(s)dt,       (4.1)

LAYER_L(s)
 =integral_(1-epsilon)^1 partial_s K_{L,t}(s)dt.       (4.2)
```

The theorem to prove is

```text
BASE-BULK_L+LAYER_L->0.                               (4.3)
```

Neither summand is required to tend to zero.  A proof may calculate
`BASE-BULK_L` by regular deformation and show that the endpoint layer has its
negative as leading term.

## 5. Status

```text
proved:
  exact combined identity (1.2);

rejected as route:
  separate vanishing of the archimedean base and tangent anomaly;
  replacement of the finite Euler primitive by the complete product before
  the outer limit;

open:
  the signed cancellation (4.3).
```

