# E78.67 - On the old-old chain, `PAIRNUM_N` is exactly the real log-q update

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.66 proved that the live shell numerator is exactly encoded by the old-old
transfer ratio

```text
q_N := q_old(N) = 1-theta_old(N) = T_N/t0_N,             (OLQ-1)
```

and that

```text
PAIRNUM_N
 = Re((q_N-q_{N+2}) conj(q_N)).                          (OLQ-2)
```

This note pushes one step further and rewrites the same object through the
old-old log increment already stored in E77.5g.

## 2. Exact log-q bridge

E77.5g stores the old-old increment

```text
Delta ell_N := log(1-theta_old(N)) - log(1-theta_old(N+2))
            = log q_N - log q_{N+2}.                     (OLQ-3)
```

Therefore

```text
q_{N+2} = q_N exp(-Delta ell_N).                         (OLQ-4)
```

Substituting `(OLQ-4)` into `(OLQ-2)` gives the exact identity

```text
PAIRNUM_N
 = Re( q_N (1-exp(-Delta ell_N)) conj(q_N) )
 = |q_N|^2 Re(1-exp(-Delta ell_N)).                      (OLQ-5)
```

So the shell numerator is not just a transfer-ratio polarization. It is the
real part of the old-old logarithmic update of that transfer ratio, weighted by
`|q_N|^2`.

## 3. Consequence

This is the cleanest bridge so far from the denominator front to the invariant
logarithmic front:

```text
PAIRNUM-SIGN
<=>
sign of Re(1-exp(-Delta ell_N))
along the old-old shell chain.                           (OLQ-6)
```

Since `Delta ell_N` is precisely the E77.5g object and is the shell side of the
E77.5l/E77.5y LOGT machinery, the live shell numerator now sits directly on a
logarithmic update law rather than on a raw ternary expansion.

## 4. Probe audit

Companion:

```text
E78_67_old_old_logq_bridge_probe.py
E78_67_old_old_logq_bridge_results.json
```

On the common certified ladder:

```text
zeta:
  max q_{N+2} reconstruction error <= 1.11e-16
  max PAIRNUM reconstruction error <= 4.86e-17

plant:
  max q_{N+2} reconstruction error <= 2.67e-15
  max PAIRNUM reconstruction error <= 2.84e-14.          (OLQ-7)
```

So both the multiplicative update `(OLQ-4)` and the shell numerator identity
`(OLQ-5)` hold to roundoff on the certified artifacts.

## 5. Honest reading

This does not yet prove the required sign. But it changes the live object in a
useful way.

Instead of proving sign directly for

```text
-Re((A_N+B_N+C_N) conj(1-theta_N)),
```

we can now seek a theorem-grade control of the old-old logarithmic update

```text
Re(1-exp(-Delta ell_N)),                                 (OLQ-8)
```

where `Delta ell_N` is already native to the E77.5g/E77.5l front.

So the next admissible target sharpens to

```text
OLD-OLD-LOGQ-CONTRACTION:
  derive the sign/contraction law for Re(1-exp(-Delta ell_N)) from the
  invariant LOGT-CELL update.                            (OLQ-9)
```

## 6. Status

```text
proved:
  on the old-old chain, q_{N+2} = q_N exp(-Delta ell_N) with Delta ell_N taken
  from the certified E77.5g log increment;

proved:
  PAIRNUM_N = |q_N|^2 Re(1-exp(-Delta ell_N)) exactly on that chain;

reduced:
  OLD-OLD-TRANSFER-CONTRACTION to OLD-OLD-LOGQ-CONTRACTION;

next:
  identify Delta ell_N directly inside the invariant E77.5l LOGT-CELL update
  and control the sign of Re(1-exp(-Delta ell_N)).
```
