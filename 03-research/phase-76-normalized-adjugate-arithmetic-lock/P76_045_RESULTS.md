# P76.045 - Core safe-log falsifiers

At `lambda=6,N=9`, maximum relative errors over
`sigma=0.6,0.75,1,1.5,2` are:

```text
zeta:    0.509
planted: 50.97
random:  60.90
```

The planted and random errors are large across the full safe interval, not
only at a selected critical ordinate.  Therefore `CORE-SR-LOG` carries
arithmetic discrimination absent from generic finite positivity,
real-rootedness and near-interlacing.

This is a necessary falsifier gate, not a proof of convergence for zeta.
