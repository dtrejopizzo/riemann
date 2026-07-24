# E77.5ah - Quadratic Cone Certificate

## Statement

E77.5ag reduced the margin threshold to the quadratic cone

```text
Im(u)>0,
Im(u)^2 - 3 Re(u)^2 >= 0,
u = -theta'/(1-theta).
```

Write

```text
theta = x+iy,
theta' = p+iq,
A = 1-x,
B = -y,
D = A^2+B^2.
```

Then

```text
u = -(p+iq)/(A+iB),
Re(u) = -(pA+qB)/D,
Im(u) = (pB-qA)/D.
```

So the signs reduce to finite real numerators:

```text
S = pB-qA,
C = S^2 - 3(pA+qB)^2.
```

The certificate is

```text
S > 0,
C >= 0.
```

## Probe

File:

```text
E77_5ah_quadratic_cone_certificate_probe.py
```

Run:

```text
python3 E77_5ah_quadratic_cone_certificate_probe.py \
  --output E77_5ah_quadratic_cone_certificate_results.json
```

Inputs:

```text
E77_5ag_margin_lower_bound_zeta_sigma1_n24.json
E77_5ac_theta_logderiv_coupling_plant.json
```

The probe reconstructs `u` from `(S,R,D)` to roundoff; maximum printed
errors are below `4.2e-17`.

## Zeta Numerators

At `sigma=1.0`:

| N | mod4 | S | C=S^2-3R^2 | C/(S^2+R^2) |
|---:|---:|---:|---:|---:|
| 8 | 0 | 0.00158028 | 2.46942e-06 | 0.985173313 |
| 10 | 2 | 0.000237977 | 4.88976e-08 | 0.825813288 |
| 12 | 0 | 0.0000590456 | 3.37818e-09 | 0.959041392 |
| 14 | 2 | 0.0000177978 | 2.65627e-10 | 0.795748537 |
| 16 | 0 | 0.00000700850 | 4.65800e-11 | 0.932242310 |
| 18 | 2 | 0.00000289403 | 4.79605e-12 | 0.501232466 |
| 20 | 0 | 0.00000125408 | 1.27604e-12 | 0.763366767 |
| 22 | 2 | 0.000000827007 | 6.81387e-13 | 0.995029425 |

The weakest row is still

```text
N=18, mod2,
C/(S^2+R^2)=0.501232466.
```

## Plant Falsifier

At `sigma=1.0`:

| N | mod4 | S | C=S^2-3R^2 | C/(S^2+R^2) |
|---:|---:|---:|---:|---:|
| 8 | 0 | 0.323503 | -148.240 | -2.99155211 |
| 10 | 2 | 15.1585 | -263016 | -2.98955287 |
| 12 | 0 | -0.359839 | -175.597 | -2.99117728 |
| 14 | 2 | -0.0116981 | -0.518060 | -2.99683355 |
| 16 | 0 | -0.00733260 | -0.462224 | -2.99860478 |
| 18 | 2 | 0.00187053 | -0.244531 | -2.99982831 |
| 20 | 0 | -0.000103908 | -0.0390375 | -2.99999668 |

The plant may have `S>0` in some rows, but it fails `C>=0` throughout.

## Proof-Or-Falsifier

The sector threshold has now been reduced to explicit finite Schur/cell real
forms:

```text
S = pB-qA,
C = S^2 - 3(pA+qB)^2.
```

This is a strict reduction: no phases, inverse norms, or fitted observables
remain.  The live mathematical statement is the sign of two real rational
quantities built from `theta` and `theta'`.

The numerical obstruction is concentrated: zeta has a narrow but positive
margin at the mod2 row `N=18`, then recovers by `N=22`.  Thus a proof should
not chase monotonicity of `C`; it must prove sign despite mod2 dips.

## Status

```text
proved numerically:
  zeta S>0 and C>=0 on the extended sigma=1 window;
  planted fails C>=0 decisively;
  u reconstruction from the rational numerators is exact to roundoff.

open:
  theorem-grade sign proof for S and C.

reduced:
  QUADRATIC-CONE-CERTIFICATE -> CONE-NUMERATOR-SIGN.
```

Reduced target:

```text
CONE-NUMERATOR-SIGN:
  prove S=pB-qA>0 and C=S^2-3(pA+qB)^2>=0 from the explicit finite
  Schur/cell formula for theta and theta'; if this fails, isolate the mod2
  dip residual in C.
```
