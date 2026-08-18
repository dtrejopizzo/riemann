# E78.15 - Re-import of theta-logderivative into the IDENT front

**Run:** 2026-07-18.
**Scope:** IDENT only.

## 1. Purpose

E78.14 established the clean split

```text
t0        = transfer-scale geometry,
-theta'/(1-theta) = signed defect geometry.
```

The remaining question is admissibility.  In Phase 77, several build-separating
objects were archived as detectors by the attribution gate E77.7az.  This note
records why the `theta`-logderivative package is *not* excluded on the current
front: it is being used inside IDENT, which is exactly where the arithmetic
discriminant is allowed to live.

## 2. The relevant gate

E77.7az's verdict was:

```text
LP-side build-discriminating shell scalars are detectors and cannot be used as
forcing mechanisms for BTG-DIV-L / operational LP.
```

The reason was location:

```text
Outcome A places the plant break in IDENT, not in LP.
```

So the same order-one zeta/plant separation has opposite meaning depending on
which front it is attached to:

```text
on LP:     inadmissible surplus arithmetic (detector);
on IDENT:  the expected discriminant.
```

## 3. Why theta-logderivative now belongs to IDENT

By E78.7 and E78.14:

```text
W-QUOTIENT-DELTA
 = Delta[T'/T]
 = Delta[t0'/t0 - theta'/(1-theta)].
```

E78.13 and E78.14 already separated the transfer-scale layer:

```text
t0 drives |T|,
but does not carry the signed defect.
```

Therefore the active signed part of the current IDENT front is precisely

```text
u = -theta'/(1-theta).                                      (TR-1)
```

This is not a return to the dead LP-side detector spiral.  It is the exact
signed ingredient of the fixed-L arithmetic symbol after the LP-neutral scale
factor has been peeled off.

## 4. What may be imported, and what may not

The Phase-77 `theta` machinery splits into two categories.

### Admissible imports

The following belong to the current IDENT front:

```text
1. exact identities:
   T=t0(1-theta),
   T'/T=t0'/t0-theta'/(1-theta),
   Q_logT=Q_t0+Q_theta;

2. the coupled complex object
   u=-theta'/(1-theta);

3. sector-style signed targets for u
   (E77.5ac / 5ad / 5ae),
   because they are statements about the arithmetic break inside IDENT.
```

### Forbidden imports

The following remain inadmissible:

```text
1. any attempt to recycle theta-sector separation as an LP forcing mechanism;
2. magnitude-only positivity/cone claims as if they were already proved;
3. any route that forgets the exact coupling and replaces u by standalone
   numerator or denominator bounds.
```

So the admissible front is *not*

```text
"theta is small" or "|1-theta| follows a power law"
```

but rather

```text
the exact signed complex law for u=-theta'/(1-theta).       (TR-2)
```

## 5. Smallest candid signed object

Among the imported Phase-77 candidates, the smallest candid signed target is:

```text
U-SECTOR-IDENT:
prove that on the zeta cofinal path, the exact finite Schur/cell quantity

  u=-theta'/(1-theta)

stays in the zeta sector near +i with a quantitative margin strong enough to
control the signed Q_theta envelope; planted/off-line builds must fail this.
```

This is exactly the content isolated in E77.5ac--5ae, now relocated
*legitimately* into IDENT.

## 6. Why this does not overclaim

This note does **not** claim that the sector certificate is already proved.
Phase 77 only established it numerically/audit-level.  What is proved here is
the organizational reduction:

```text
after separating t0-scale geometry,
the remaining signed IDENT ingredient is u=-theta'/(1-theta),
and this ingredient is admissible because it lives on the IDENT side.
```

That is a theorem-grade ledger correction, not a closure claim.

## 7. Consequence for the live front

The current fixed-L IDENT front can now be read as:

```text
geometric side:
  t0-driven transfer scale;

signed arithmetic side:
  U-SECTOR-IDENT / theta-logderivative coupling;

bridge:
  Delta[T'/T] = Delta[t0'/t0] + Delta u.
```

So the candid next target is no longer a vague "interaction of T and Delta[T'/T]"
but the sharper coupled law:

```text
T0-scale + U-sector => W-QUOTIENT-DELTA / LOGT-CELL.
```

## 8. Status

```text
proved:
  theta-logderivative belongs to the IDENT front after the transfer-scale t0
  factor is separated;

clarified:
  the attribution gate E77.7az blocks build-separating theta objects only on
  the LP side, not on IDENT where the discriminant is supposed to live;

reduced:
  the signed part of the live IDENT front to U-SECTOR-IDENT;

forbidden:
  reusing theta-sector separation as LP forcing, or replacing u by magnitude-only
  surrogates;

next:
  phrase the current IDENT endpoint as
    t0-scale geometry + U-sector-IDENT
  and identify the exact residual still missing for a theorem-grade proof.
```
