# E79.48 - The zeta residual is already captured by an affine sigma template

**Scope:** `GAP-Z` only, first explicit low-dimensional template after E79.47.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the residual
left by the first packet is not just monotone on the zeta side; it is already
well captured by a 2-parameter affine function of `sigma` on the audited safe
grid, while the planted build typically is not.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the already-audited residual data from E79.44.
E72.16/E77.7az: respected. This is a finite template audit, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why affine is the first candid template

E79.47 showed that the zeta residual is monotone in `sigma` with small discrete
curvature. The first natural question is then:

```text
is the residual already close to a straight line in sigma?            (48-1)
```

If yes, the next object is no longer just "some smooth profile", but an
explicit 2-parameter template.

## 2. Probe

Companion files:

```text
E79_48_AFFINE_SIGMA_TEMPLATE_PROBE.py
E79_48_affine_sigma_template_results.json
```

For the best mean-aggregated packet from E79.44, the probe fits the residual
mismatch values on

```text
sigma in {0.75, 1.0, 1.5, 2.0}                                       (48-2)
```

by two affine templates:

```text
- least-squares affine fit;
- endpoint line through the first and last sigma values.              (48-3)
```

The outputs are the normalized max and RMS fitting errors.

## 3. Result

On the zeta side, the affine errors are small across the whole audited ladder.
In particular the least-squares normalized max error stays well below the
natural residual scale.

Numerically:

```text
zeta least-squares normalized max error:
N= 8   0.0120
N=10   0.0333
N=12   0.00792
N=14   0.00832
N=16   0.00445                                                   (48-3a)
```

By contrast, on the planted hard sections `N=8,10,14`, the affine fit is much
worse, reflecting the mixed / high-curvature behavior already seen in E79.47.

```text
plant least-squares normalized max error:
N= 8   0.495
N=10   0.445
N=12   0.00899
N=14   0.227
N=16   0.0134                                                    (48-3b)
```

So the plant does not fail affine fit at every audited section; it fails it
precisely on the hard rows that were already rough in E79.47, while the two
smooth rows `N=12,16` remain low-curvature and therefore affine-compatible.

So the residual law sharpens from:

```text
smooth in sigma                                                       (48-4)
```

to:

```text
approximately affine in sigma on the zeta side.                       (48-5)
```

## 4. Reading

This is the first explicit low-dimensional template on the residual side.

That matters because it turns the next object into something that can plausibly
transport in `N`:

```text
residual(sigma; N) ~ a_N sigma + b_N.                                (48-6)
```

So the next finite question is no longer "is there a profile?" but:

```text
what are the transport laws of the coefficients a_N and b_N?         (48-7)
```

## 5. Consequence

After E79.47-E79.48, the frontier sharpens once more:

```text
primitive packet + affine residual template in sigma.                (48-8)
```

That is a much more concrete candidate bridge toward a theorem-grade
cancellation law than the earlier support-only descriptions.

## 6. Status

```text
proved by probe:
  the zeta residual after the first packet is well captured by an affine
  template in sigma on the audited safe grid;

observed:
  the planted build fails that affine regularity on the hard sections N=8,10,14,
  while N=12,16 remain affine-compatible but at much larger residual scale;

reduced:
  the next object past the packet can be named as an affine sigma-profile with
  section-dependent coefficients;

open:
  identify the N-transport law for those coefficients, and test whether the
  plant fails any comparable transport law;

next:
  audit the coefficient transport (a_N, b_N) across N.
```
