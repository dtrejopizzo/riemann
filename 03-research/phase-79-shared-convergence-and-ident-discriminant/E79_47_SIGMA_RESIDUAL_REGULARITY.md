# E79.47 - The first-packet residual has a smooth sigma profile on the zeta side and an erratic one on the plant side

**Scope:** `GAP-Z` only, first residual-law audit after E79.46.  
**Class:** REDUCCION GENUINA + AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** after fixing
the first raw packet, the remaining mismatch as a function of `sigma` is
already highly regular on the zeta side, while the planted build is typically
erratic. So the next object past the support is better modeled as a residual
sigma-profile than as another support law.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the already-audited multisigma mismatch data from E79.44.
E72.16/E77.7az: respected. This is a residual anatomy probe, not a forcing step.
Circularity: respected. No new endpoint identity enters; only the packet residual
             already computed in E79.44.
```

## 1. Why this is the next candid move

E79.44-E79.46 eliminated three simpler possibilities:

```text
- the packet is not a one-sigma accident;
- there is no second packet in the same grammar;
- there is no fixed low-complexity support-only transport law.         (47-1)
```

So the natural next question is not about another support. It is:

```text
does the residual left by the first packet already obey a simple sigma-profile
law?                                                                   (47-2)
```

## 2. Probe

Companion files:

```text
E79_47_SIGMA_RESIDUAL_REGULARITY_PROBE.py
E79_47_sigma_residual_regularity_results.json
```

The input is the best mean-aggregated multisigma packet from E79.44. For each
section and build, the probe reads the residual mismatch values at

```text
sigma in {0.75, 1.0, 1.5, 2.0},                                       (47-3)
```

then records:

```text
- the monotonicity direction;
- the total variation across sigma;
- the discrete second differences (curvature);
- the maximum curvature normalized by the residual scale.              (47-4)
```

So the question is whether the residual profile is already a smooth one-parameter
object.

## 3. Result

On the zeta side, every audited section has a monotone residual profile:

```text
N= 8   nondecreasing
N=10   nonincreasing
N=12   nonincreasing
N=14   nondecreasing
N=16   nonincreasing                                                (47-5)
```

and the normalized curvature stays small.

Numerically:

```text
zeta normalized max curvature:
N= 8   0.0448
N=10   0.1226
N=12   0.0292
N=14   0.0309
N=16   0.0164                                                     (47-5a)
```

By contrast, the plant side is irregular exactly on the hard sections:

```text
plant:
N= 8   mixed,         normalized max curvature 1.361
N=10   mixed,         normalized max curvature 1.340
N=12   nondecreasing, normalized max curvature 0.023
N=14   mixed,         normalized max curvature 0.524
N=16   nondecreasing, normalized max curvature 0.042                (47-5b)
```

So the plant does not fail by universal roughness at every `N`; it fails by
losing the clean zeta-style regularity precisely on the sections where its
packet side was already least coherent.

So the first packet does not leave behind another combinatorial object. It
leaves behind a residual sigma profile that is already smooth on the zeta side
and unstable on the plant side.

## 4. Reading

This is exactly the kind of shift in object type that E79.45-E79.46 hinted at.

The next layer is not:

```text
support -> support -> support.                                        (47-6)
```

It is closer to:

```text
support -> smooth residual profile in sigma.                          (47-7)
```

That is a cleaner finite object, and it is more plausible as a bridge toward a
theorem-grade cancellation law because it already speaks the language of the
safe axis.

## 5. Consequence

After E79.43-E79.47, the frontier sharpens again:

```text
the first packet is primitive;
what remains is not another packet law but a residual profile law.    (47-8)
```

So the next candid reduction should try one of:

```text
- fit the zeta residual to a one-parameter template across sigma;
- compare that template across N;
- or prove that the plant fails any such smooth profile law.          (47-9)
```

## 6. Status

```text
proved by probe:
  the residual mismatch of the first packet is already monotone in sigma on the
  whole audited zeta ladder;

observed:
  the planted build is mixed/high-curvature on the hard sections N=8,10,14,
  while N=12,16 remain smooth but at a much larger residual scale;

reduced:
  the next object past the packet is better modeled as a residual sigma-profile
  than as another support or support-transport law;

open:
  identify the right low-dimensional sigma-profile law and its transport in N;

next:
  test whether the zeta residual is captured by a one-parameter template across
  sigma, while the plant is not.
```
