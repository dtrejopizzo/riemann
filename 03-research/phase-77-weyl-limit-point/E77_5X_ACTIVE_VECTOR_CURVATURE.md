# E77.5x - Active Vector Curvature

## Statement

E77.5w refuted a direct state law for the phase-aligned active vector.  This
probe tests the next smaller object:

```text
ACTIVE-VECTOR-CURVATURE:
  Q_N is controlled by the signed first/second differences of the
  phase-aligned active-vector path.
```

The test uses only the complex vectors already computed in E77.5w.  No matrix
is inverted here, and no zero data enters except the planted falsifier.

## Probe

File:

```text
E77_5x_active_vector_curvature_probe.py
```

Run:

```text
python3 E77_5x_active_vector_curvature_probe.py \
  --output E77_5x_active_vector_curvature_results.json
```

Inputs:

```text
E77_5w_complex_active_vector_zeta.json
E77_5w_complex_active_vector_plant_n18.json
```

## Zeta Results

At `sigma=3.0`:

| diagnostic | value |
|---|---:|
| mod0 tangent 8 -> 12 | 0.079085005808202588 |
| mod0 tangent 12 -> 16 | 0.036050002650009363 |
| mod0 curvature norm 8,12,16 | 0.043865222705183657 |
| mod0 signed curvature | 0.01139800147336106 |
| mod0 Q second difference | -0.31663148715353362 |
| mod2 tangent 10 -> 14 | 0.049905564691063393 |
| mod2 tangent 14 -> 18 | 0.027183009440102667 |
| mod2 curvature norm 10,14,18 | 0.02372596043756111 |
| mod2 signed curvature | 0.003423863455005048 |
| mod2 Q second difference | 4.7492910793725249 |
| cross midpoint defect N=10 | 0.012895560618315998 |
| cross Q midpoint defect N=10 | -1.2601184496446036 |
| cross midpoint defect N=14 | 0.0048550925136612967 |
| cross Q midpoint defect N=14 | -1.9533207798183794 |

The vector path is regularizing: both branch tangents decrease.  The mod2
scalar `Q` acceleration moves in the opposite direction: the mod2 second
difference is large and positive while the signed vector curvature is smaller
than the mod0 signed curvature.

## Plant Falsifier

At `sigma=3.0`:

| diagnostic | value |
|---|---:|
| mod0 tangent 8 -> 12 | 1.03994531577725 |
| mod0 tangent 12 -> 16 | 0.37172891241787392 |
| mod0 curvature norm 8,12,16 | 1.1778862223830886 |
| mod0 signed curvature | -0.22899104151965899 |
| mod0 Q second difference | -17.410821388488039 |
| mod2 tangent 10 -> 14 | 0.49624322496788131 |
| cross midpoint defect N=10 | 0.49574799538984743 |
| cross Q midpoint defect N=10 | 1.8279171287961482 |
| cross midpoint defect N=14 | 0.35029807799347529 |
| cross Q midpoint defect N=14 | -8.6731817993092548 |

The plant again breaks zeta-like regular transport, but this does not rescue
the curvature law: the proposed curvature scalar is not the object that
carries the zeta spike.

## Proof-Or-Falsifier

`ACTIVE-VECTOR-CURVATURE` is refuted as a direct scalar law.  In the zeta
window, the mod2 second difference of `Q` is

```text
4.7492910793725249,
```

but the corresponding signed curvature is only

```text
0.003423863455005048,
```

and has the same sign as the much larger mod0 signed curvature

```text
0.01139800147336106,
```

where the `Q` second difference is negative.  Therefore neither branch
tangent, branch curvature norm, nor the simple Hermitian signed curvature can
be the missing finite scalar.

## Status

```text
proved:
  zeta active-vector transport is smoother than the planted transport;
  simple first/second vector differences do not encode the Q spike.

refuted:
  ACTIVE-VECTOR-CURVATURE as a direct closure mechanism.

open:
  derive the exact scalar functional that maps the Schur active response plus
  external log tail to Q_N.
```

Reduced target:

```text
Q-FUNCTIONAL-IDENTITY:
  stop searching scalar observables; derive the exact finite identity
  expressing Q_N from the active Schur cell, the external tail increment,
  and the inserted-anchor normalization.
```
