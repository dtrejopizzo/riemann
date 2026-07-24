# E78.32 - `Delta safe_u` is an exact modulus-plus-angle update

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.31 reduced the sign-side target to the primitive envelope

```text
0 < Delta safe_u_{N+2} <= eta_* Delta safe_u_N.          (DP-1)
```

The natural next question is whether `Delta safe_u` is driven mainly by the
growth of `|u|`, with the phase only supplying a small correction. This note
shows that this is not a heuristic but an exact finite decomposition.

## 2. Exact polar identity

Write

```text
u_N = |u_N| (a_N + i s_N),  where  s_N := Im(u_N)/|u_N|. (DP-2)
```

Since

```text
safe_u,N = 2 Re(i u_N) = -2 Im(u_N),                     (DP-3)
```

the exact shell increment from `N` to `N+2` is

```text
Delta safe_u_N
 := safe_u,N+2 - safe_u,N
  = 2 (Im(u_N+2) - Im(u_N)).                            (DP-4)
```

Substituting `Im(u_N)=|u_N| s_N` gives the exact split

```text
Delta safe_u_N
 = 2 (|u_N+2| - |u_N|) s_N+2
   + 2 |u_N| (s_N+2 - s_N).                              (DP-5)
```

So every shell update decomposes canonically into

```text
modulus gain  +  angular correction.                     (DP-6)
```

## 3. Probe audit

Companion:

```text
E78_32_delta_safeu_polar_probe.py
E78_32_delta_safeu_polar_results.json
```

The probe reconstructs `(DP-5)` directly from the certified `E77.5ac` JSONs.

### Exactness

For both builds, reconstruction holds to roundoff:

```text
max reconstruction error < 1e-16.                        (DP-7)
```

### Zeta

On the audited zeta ladder, the modulus term is the dominant piece.

Representative rows:

```text
sigma=1.0:
  N= 8  delta=0.0318414  modulus=0.0318648  angle=-2.34e-05
  N=14  delta=0.0103299  modulus=0.0102064  angle= 1.24e-04
  N=18  delta=0.00600388 modulus=0.00580836 angle= 1.96e-04

sigma=3.0:
  N= 8  delta=0.0917608  modulus=0.0917687  angle=-7.96e-06
  N=14  delta=0.0305505  modulus=0.0305067  angle= 4.38e-05
  N=18  delta=0.0178497  modulus=0.0177739  angle= 7.58e-05. (DP-8)
```

Quantitatively:

```text
max relative angular correction     = 0.14795098318536765
min modulus share of delta_safe_u   = 0.8520490168146325. (DP-9)
```

So on all audited zeta rows, at least about `85%` of `Delta safe_u` comes from
pure modulus growth of `u`, with the angle contributing only a secondary
correction.

### Planted build

The plant does not show the same structure. The angular term is often the main
driver and can even reverse the sign geometry.

Representative rows:

```text
sigma=1.0:
  N= 8  delta= 0.153108   modulus= 0.00808250  angle= 0.145025
  N=14  delta=-0.00102187 modulus=-0.00055137  angle=-0.00047050

sigma=3.0:
  N= 8  delta= 0.0286172  modulus=-0.0132202   angle= 0.0418374
  N=14  delta=-0.00053593 modulus= 0.00053437  angle=-0.00107031. (DP-10)
```

Quantitatively:

```text
max relative angular correction     = 8.595471345141136
min modulus share of delta_safe_u   = -0.9970901086680051. (DP-11)
```

So the plant fails exactly at the level of angular instability: the shell
increment is no longer a mostly-modulus effect.

## 4. Consequence

This gives a sharper reduced target than E78.31 alone:

```text
to prove the raw geometric envelope for Delta safe_u,
it is enough to control

  (i) positive growth of |u_N|,
  (ii) small angular drift of s_N = Im(u_N)/|u_N|.       (DP-12)
```

More precisely, `(DP-5)` shows that the sign-side target can be pursued through
the nested route

```text
MODULUS-GAIN-DOMINANCE
+ ANGULAR-DRIFT-SMALLNESS
=> DELTA-SAFEU-GEOMETRIC-ENVELOPE.                        (DP-13)
```

## 5. Honest reading

This note does not yet prove either clause in `(DP-13)`. What it does is
identify the correct anatomy:

```text
zeta:
  Delta safe_u is mostly modulus growth of u;

plant:
  angular drift is large enough to dominate or flip the update. (DP-14)
```

That is exactly the kind of reduced target Phase 78 wants: explicit, exact, and
compatible with the falsifier location rule.

## 6. Status

```text
proved:
  Delta safe_u admits the exact polar decomposition (DP-5);

proved:
  the decomposition reconstructs the certified shell data to roundoff for both
  builds;

observed:
  on the audited zeta ladder, at least about 85% of Delta safe_u is explained
  by pure modulus growth of u;

observed:
  the planted build is dominated by angular instability rather than modulus
  growth;

reduced:
  DELTA-SAFEU-GEOMETRIC-ENVELOPE to MODULUS-GAIN-DOMINANCE plus
  ANGULAR-DRIFT-SMALLNESS;

next:
  derive those two clauses from the exact u-sector / theta-logderivative shell
  formulas, starting with an explicit bound on the angular drift term.
```
