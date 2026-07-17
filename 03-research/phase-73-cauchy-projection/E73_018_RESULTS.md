# E73.018 results - mesh rational collapse

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_018_mesh_rational_collapse_probe.py
```

Output:

```text
E73.018 mesh rational collapse probe
   L      gamma      maxAbsErr
 4.159  14.134725      1.732e-14
 4.159  21.022040      2.665e-14
 4.159  25.010858      8.521e-15
 4.605  14.134725      1.121e-14
 4.605  21.022040      1.943e-14
 4.605  25.010858      2.176e-14
 4.970  14.134725      4.308e-14
 4.970  21.022040      3.642e-14
 4.970  25.010858      1.821e-14
 5.278  14.134725      1.954e-14
 5.278  21.022040      1.443e-14
 5.278  25.010858      1.723e-13
 5.545  14.134725      8.729e-15
 5.545  21.022040      2.320e-14
 5.545  25.010858      2.389e-13
```

Conclusion:

```text
DD_L(-gamma,d_n) = (exp(i gamma L)-1)/(gamma+d_n)
```

is numerically exact to floating precision on the CCM pole mesh.  The local ideal is therefore a
rational Cauchy module, not a transcendental Paley-Wiener module.
