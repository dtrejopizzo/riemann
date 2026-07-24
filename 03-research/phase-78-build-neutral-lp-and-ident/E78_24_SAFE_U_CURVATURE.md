# E78.24 - Theta sign stability as a second-drift law for `safe_u`

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.23 separated

```text
THETA-DOMINANCE
 = THETA-SIGN-STABILITY + T0-SMALLNESS.                   (SU-1)
```

The remaining question for the sign half is:

```text
what exact finite object actually carries sign(Q_theta)?
```

The answer is already present in E77.5ac, but it had not yet been promoted to
the current front:

```text
Q_theta is the second drift coefficient of safe_u = 2 Re(iu). (SU-2)
```

This note records that identity as the correct endpoint for the sign problem.

## 2. Exact second-drift identity

From E77.5ac,

```text
safe_u,N := 2 Re(i u_N),                                  (SU-3)
Delta safe_u_N := safe_u,N - safe_u,N+2.                  (SU-4)
```

The probe defining `Q_theta` uses exactly

```text
Q_theta,N
 = N^2 ( N Delta safe_u_N - (N+2) Delta safe_u_{N+2} ).   (SU-5)
```

So the sign of `Q_theta` is not a mysterious Schur byproduct. It is the sign
of the weighted discrete curvature of the `safe_u` sequence.

This yields the exact reformulation:

```text
THETA-SIGN-STABILITY
<=>
SAFE-U-CURVATURE-SIGN:
  the second drift (SU-5) keeps the required sign on the zeta cofinal path.
                                                             (SU-6)
```

## 3. Probe audit

Companion:

```text
E78_24_safe_u_curvature_probe.py
E78_24_safe_u_curvature_results.json
```

The probe reconstructs `(SU-5)` directly from the certified E77.5ac JSONs.

Reconstruction is exact to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0:
  N= 8  Delta safe_u = 0.0318414   Q_theta =  3.11409
  N=10  Delta safe_u = 0.0206073   Q_theta =  3.75203
  N=14  Delta safe_u = 0.0103299   Q_theta =  4.29756

sigma=3.0:
  N= 8  Delta safe_u = 0.0917608   Q_theta =  8.44953
  N=10  Delta safe_u = 0.0602062   Q_theta = 10.59749
  N=14  Delta safe_u = 0.0305505   Q_theta = 12.49579.     (SU-7)
```

All audited zeta rows satisfy

```text
Q_theta > 0.                                              (SU-8)
```

so the weighted curvature of `safe_u` keeps a stable positive sign.

### Planted build

Representative rows:

```text
sigma=1.0:
  N=12  Delta safe_u =  0.00173850   Q_theta =  5.06422
  N=14  Delta safe_u = -0.00102187   Q_theta = -1.33932
  N=16  Delta safe_u = -0.00046706   Q_theta = -2.78891
  N=18  Delta safe_u =  0.00019007   Q_theta =  1.95681

sigma=3.0:
  N=12  Delta safe_u =  0.00446761   Q_theta =  8.80048
  N=14  Delta safe_u = -0.00053593   Q_theta = -0.56858
  N=16  Delta safe_u = -0.00028763   Q_theta = -5.49534
  N=18  Delta safe_u =  0.00093689   Q_theta =  6.74411.   (SU-9)
```

So the plant loses sign stability exactly by oscillating the second drift of
`safe_u`.

## 4. Consequence

This is the cleanest honest reduction of the sign problem so far:

```text
u-sector geometry
  gives the sign geometry of safe_u,
and the open sign target is the weighted curvature sign of safe_u. (SU-10)
```

So the current front becomes

```text
SAFE-U-CURVATURE-SIGN
+ T0-SMALLNESS
+ ratio-to-one for |Q_logT|/|Q_ext|
+ section-lag curvature
=> LOGT-CANCEL-COFINAL.                                   (SU-11)
```

## 5. Honest reading

This note still does **not** prove the zeta sign theorem. What it does is strip
away one more layer of indirection:

```text
sign(Q_theta) is exactly a second-drift sign law for safe_u.
```

That matters because `safe_u` is directly tied to the `u`-sector object from
E77.5ad/E77.5ae, whereas `Q_theta` looked one step more opaque.

So the next exact question is no longer

```text
"why is Q_theta positive?"
```

but

```text
"why does the weighted second drift of safe_u stay positive on zeta?" (SU-12)
```

That is a much better theorem-grade target.

## 6. Status

```text
proved:
  Q_theta is exactly the weighted second drift of safe_u = 2 Re(iu);

proved:
  the E77.5ac construction reconstructs this identity to roundoff for both
  zeta and the planted build;

observed:
  zeta keeps the safe_u curvature sign positive on the audited ladder;

observed:
  the planted build loses that sign by oscillating the second drift of safe_u;

reduced:
  THETA-SIGN-STABILITY to SAFE-U-CURVATURE-SIGN;

next:
  combine the exact u-sector law with the second-drift formula (SU-5) to seek
  a theorem-grade positive curvature mechanism for zeta.
```
