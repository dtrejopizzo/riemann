# E77.7p - Singular-section regularization autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7o left the LP interface at the projective bridge

```text
PROJECTIVE-MU-TRANSFER
```

with one major open point:

```text
singular-section regularization.
```

The first candidate was the naive resolvent regularization

```text
x_{N,eta} = (A_N(mu_ref)-i eta I)^(-1)b_N,
Pi_{N,eta}(z)=T_{N,eta}(z)/T_{N,eta}(z_0),
```

and then `eta -> 0`.

This note audits that candidate.

## 2. Probe

Companion:

```text
E77_7p_singular_section_probe.py
E77_7p_singular_section_results.json
```

Command:

```bash
python3 E77_7p_singular_section_probe.py \
  --lambda 6 --max-modes 18 --dps 60
```

For the largest-section frozen point `mu_ref`, the probe records:

```text
1. the nearest inner eigenvalue gap |lambda_0|;
2. the boundary overlap |<u_0,b_N>| of the nearest inner mode;
3. the projective profile Pi_{N,eta} on sigma in {0.6,1,2,3};
4. the max profile step between consecutive etas
   eta = 1e-2,1e-4,1e-6,1e-8.
```

The frozen `mu_ref` is only a finite surrogate for `mu_L`, but this is
exactly the regime where singular behavior should already appear if the
regularization is the right one.

## 3. Result

### Zeta

The inner gap collapses rapidly:

```text
N=10: |lambda_0| = 1.85e-30
N=14: |lambda_0| = 2.26e-39
N=18: |lambda_0| = 2.33e-47.
```

The corresponding nearest-mode boundary overlaps are tiny but nonzero:

```text
|<u_0,b_N>| = 1e-23 down to 1e-33.
```

Despite projective normalization, the profile does **not** stabilize as
`eta -> 0` on the tested ladder.  The final `eta`-step remains macroscopic:

```text
0.05 -- 0.17
```

across `N=6..18`.

So in the near-singular zeta regime, naive `-i eta` regularization does not
produce an `eta`-stable projective coordinate.

### Planted build

The inner gaps stay much larger:

```text
N=10: |lambda_0| = 2.48e-1
N=14: |lambda_0| = 2.13e-2
N=18: |lambda_0| = 4.55e-3.
```

Here the same regularization is essentially stable:

```text
final eta-step = 8.5e-9 up to 1.9e-6.
```

Thus the instability is not a generic flaw of the formula.  It is specific
to the near-null resonant regime.

## 4. Reading

The autopsy is sharp:

```text
1. plain resolvent regularization plus projective normalization is enough
   away from singularity;
2. it fails exactly when the inner gap collapses;
3. therefore the unresolved object is the resonant one-mode contribution,
   not the ordinary safe anchor.
```

The failure mechanism is the expected one.  If

```text
A_N(mu_ref)^(-1)b_N
```

has a large component along the near-null inner eigenvector `u_0`, then both
numerator and denominator of `Pi_{N,eta}` inherit an `eta`-sensitive pole.
Dividing by the anchor removes only the common scalar scale; it does not
remove the changing **directional mix** between the resonant mode and the
regular remainder.

So the naive limit

```text
eta -> 0 of Pi_{N,eta}
```

is not the right singular-section definition in the near-null regime.

## 5. What is refuted

The following candidate is now refuted:

```text
NAIVE-SINGULAR-REGULARIZATION:
define the singular-section projective profile by
Pi_N(z) = lim_{eta->0} T_{N,eta}(z)/T_{N,eta}(z_0)
using the raw resolvent regularization only.
```

It is falsifier-neutral away from singularity, but it does not stabilize in
the very zeta regime where the theorem needs it.

## 6. Smaller live object

The next admissible object is:

```text
RESONANT-MODE-REGULARIZATION:
split the regularized response into

  resonant one-mode part
  + orthogonal regular remainder,

and prove that after removing or explicitly renormalizing the resonant mode,
the projective profile has a stable boundary-relation limit.
```

Equivalently, one needs a theorem in the style:

```text
x_{N,eta}
 = <u_0,b_N>/(lambda_0-i eta) u_0
   + x_{N,eta}^reg,
```

with the boundary Cauchy rows applied to both pieces before taking the
projective quotient.

Then the singular-section bridge would be reduced to the stability of

```text
[r_z x_{N,eta}^reg + resonant scalar(z,eta)]
/
[r_{z0} x_{N,eta}^reg + resonant scalar(z0,eta)].
```

This is strictly smaller than full `PROJECTIVE-MU-TRANSFER`, and it is the
exact finite object exposed by the autopsy.

## 7. Status

```text
observed:  away from singularity (plant), naive eta-regularization is
           projectively stable;
observed:  in the near-null zeta regime, the same regularization has
           O(1e-1) residual motion and does not stabilize;
refuted:   NAIVE-SINGULAR-REGULARIZATION;
open:      RESONANT-MODE-REGULARIZATION;
next:      isolate the one-mode resonant contribution and pair it with the
           safe Cauchy rows before forming the quotient.
```
