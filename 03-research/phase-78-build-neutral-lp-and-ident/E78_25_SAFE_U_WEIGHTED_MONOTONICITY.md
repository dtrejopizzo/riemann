# E78.25 - `Q_theta` sign as weighted monotonicity of `Delta safe_u`

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.24 reduced the sign problem to

```text
SAFE-U-CURVATURE-SIGN:
  Q_theta,N = N^2 (N Delta safe_u_N - (N+2) Delta safe_u_{N+2}).  (WM-1)
```

Since `N^2 > 0`, the sign of `Q_theta,N` is exactly the sign of

```text
N Delta safe_u_N - (N+2) Delta safe_u_{N+2}.              (WM-2)
```

This note promotes `(WM-2)` as the cleanest current endpoint of the sign front.

## 2. Exact weighted monotonicity law

Define

```text
D_N := Delta safe_u_N.                                    (WM-3)
```

Then E78.24 becomes

```text
Q_theta,N = N^2 ( N D_N - (N+2) D_{N+2} ).                (WM-4)
```

Therefore

```text
sign(Q_theta,N)
 = sign( N D_N - (N+2) D_{N+2} ).                         (WM-5)
```

Equivalently, whenever `D_N` and `D_{N+2}` are positive,

```text
Q_theta,N > 0
<=> N D_N > (N+2) D_{N+2}.                                (WM-6)
```

So the sign target is no longer an abstract curvature statement. It is a
weighted monotonicity statement for the real sequence `D_N = Delta safe_u_N`.

## 3. Probe audit

Companion:

```text
E78_25_safe_u_weighted_monotonicity_probe.py
E78_25_safe_u_weighted_monotonicity_results.json
```

The probe checks the exact sign agreement in `(WM-5)`.

### Zeta

On the audited `sigma in {1,3}` ladder:

```text
same-sign count = 10
fail count      = 0.                                      (WM-7)
```

Representative rows:

```text
sigma=1.0:
  N= 8  weighted diff = 0.0486577   Q_theta =  3.11409
  N=10  weighted diff = 0.0375203   Q_theta =  3.75203
  N=14  weighted diff = 0.0219263   Q_theta =  4.29756

sigma=3.0:
  N= 8  weighted diff = 0.132024    Q_theta =  8.44953
  N=10  weighted diff = 0.105975    Q_theta = 10.59749
  N=14  weighted diff = 0.0637540   Q_theta = 12.49579.   (WM-8)
```

So zeta satisfies a strict positive weighted monotonicity law on every audited
row where the second drift is defined.

### Planted build

On the planted build:

```text
same-sign count = 10
fail count      = 0,                                      (WM-9)
```

but the weighted difference itself changes sign:

```text
sigma=1.0:
  N=12  weighted diff =  0.0351682   Q_theta =  5.06422
  N=14  weighted diff = -0.00683324  Q_theta = -1.33932
  N=16  weighted diff = -0.0108942   Q_theta = -2.78891

sigma=3.0:
  N=12  weighted diff =  0.0611144   Q_theta =  8.80048
  N=14  weighted diff = -0.00290094  Q_theta = -0.568584
  N=16  weighted diff = -0.0214662   Q_theta = -5.49534.  (WM-10)
```

So the plant fails not by violating `(WM-5)` but by flipping the weighted
monotonicity sign itself.

## 4. Consequence

This gives the sharpest current finite sign target:

```text
SAFE-U-WEIGHTED-MONOTONICITY:
  prove that

    N Delta safe_u_N > (N+2) Delta safe_u_{N+2}

  on the zeta cofinal path.                               (WM-11)
```

Because of `(WM-4)`, this implies

```text
SAFE-U-WEIGHTED-MONOTONICITY
=> SAFE-U-CURVATURE-SIGN
=> THETA-SIGN-STABILITY.                                  (WM-12)
```

This is genuinely better than the previous phrasing: it asks for a one-step
order relation between consecutive real scalars, rather than a sign theorem for
an already-compressed second drift.

## 5. Candid reading

This note still does not prove the zeta monotonicity theorem.  But it names the
right endpoint very clearly:

```text
the sign front is a weighted one-step decay law for Delta safe_u.
```

That is probably the most actionable theorem-grade form reached so far, because
it is:

```text
- exact;
- one-dimensional;
- expressed directly in terms of the u-sector scalar safe_u;
- falsified by the planted build through explicit sign flips.           (WM-13)
```

## 6. Status

```text
proved:
  sign(Q_theta) is exactly sign of the weighted difference
    N Delta safe_u_N - (N+2) Delta safe_u_{N+2};

observed:
  zeta satisfies strict positive weighted monotonicity on the audited ladder;

observed:
  the planted build flips that weighted monotonicity sign exactly where
  Q_theta changes sign;

reduced:
  SAFE-U-CURVATURE-SIGN to SAFE-U-WEIGHTED-MONOTONICITY;

next:
  combine the u-sector law with a quantitative decay law for Delta safe_u to
  seek a theorem-grade proof of positive weighted monotonicity on zeta.
```
