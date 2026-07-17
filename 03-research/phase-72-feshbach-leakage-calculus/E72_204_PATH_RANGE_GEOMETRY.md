# E72.204 - Path-range geometry audit

## Purpose

E72.201 refuted a scalar kernel depending only on the final displacement `R`. The next geometric
candidate is stronger: signed translation words should depend on the whole path of partial
displacements, not only on the endpoint.

For signed shifts `a_1,...,a_r`, define partial sums

```text
s_0=0,      s_k=a_1+...+a_k,
```

and the path range

```text
range(a)=max_k s_k - min_k s_k.
```

In the ideal unprojected translation picture on `[0,L]`, the surviving interval length is

```text
ell(a)=(L-range(a))_+.
```

The tempting bare formula is

```text
Tr prod_i U_{a_i}
 ~= ell(a)/L * D_N(sum_i a_i),
```

where `D_N` is the finite Dirichlet kernel of the Fourier pole mesh.

## Diagnostic

Script:

```text
E72_204_path_range_probe.py
```

Output:

```text
E72.204 bare path-range trace probe
checks Tr prod U_a = pathLength/L * Dirichlet_N(totalShift)
L N shifts direct formula relErr
5.0  8 +0.7,-0.7              +1.418912811408e+01 +1.462000000000e+01 3.037e-02
5.0  8 +1.1,+0.8,-1.9         +1.003074379585e+01 +1.054000000000e+01 5.077e-02
5.0  8 +0.6,-1.4,+0.8         +1.175077213392e+01 +1.224000000000e+01 4.163e-02
5.0  8 +1.2,-0.5,+0.9         -6.920408551951e-01 -7.911088930268e-01 1.432e-01
5.0  8 +2.0,-0.7,-0.4,+0.3    +5.021435628219e-02 +2.179746740679e-01 3.341e+00
5.0 16 +0.7,-0.7              +2.788209487073e+01 +2.838000000000e+01 1.786e-02
5.0 16 +1.1,+0.8,-1.9         +1.988389489160e+01 +2.046000000000e+01 2.897e-02
5.0 16 +0.6,-1.4,+0.8         +2.320296110587e+01 +2.376000000000e+01 2.401e-02
5.0 16 +1.2,-0.5,+0.9         +7.465394321459e-01 +7.911088930268e-01 5.970e-02
5.0 16 +2.0,-0.7,-0.4,+0.3    -3.423790794066e-01 -2.179746740679e-01 3.634e-01
5.0 32 +0.7,-0.7              +5.533354765948e+01 +5.590000000000e+01 1.024e-02
5.0 32 +1.1,+0.8,-1.9         +3.965476773187e+01 +4.030000000000e+01 1.627e-02
5.0 32 +0.6,-1.4,+0.8         +4.617381016177e+01 +4.680000000000e+01 1.356e-02
5.0 32 +1.2,-0.5,+0.9         +5.503047347187e-01 +4.733871277812e-01 1.398e-01
5.0 32 +2.0,-0.7,-0.4,+0.3    -7.945874018467e-01 -8.335933419848e-01 4.909e-02
```

## Reading

The path-range formula is not an exact finite-section identity. It improves with larger `N` in many
cases, but finite Fourier projections introduce diffraction corrections. This is already visible
before inserting the model Green operator.

Thus the exact signed Green-word kernel has three layers:

```text
1. path-range geometry of truncated translations,
2. finite-section Fourier diffraction from intermediate projections,
3. model Green insertions from Feshbach whitening.
```

The failure of the scalar `W(log R)` picture is therefore natural: the word depends on the path of
partial displacements and on finite-section diffraction, not only on the final product `R`.

## Consequence

The next closed theorem should not be stated as a scalar displacement kernel. The honest target is a
path-sensitive group-algebra inequality:

```text
sum_{words} beta(word) TraceGreenPath(word) <= certificate threshold.
```

The path-range formula may still be useful as a comparison background, but the exact proof must carry
the finite-section correction.
