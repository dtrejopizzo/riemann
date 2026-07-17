# E73.027 results - confluent Taylor formula

Command:

```text
python3 03-research/phase-73-cauchy-projection/E73_027_confluent_formula_probe.py
```

Result:

```text
maxErr = 0.000e+00
```

for all tested `sigma,t,m`.  The Hermite coefficients obtained by solving the confluent Cauchy
matrix are exactly the coefficients of the truncated Taylor matching system.

This validates the algebraic identification:

```text
C_conf h = v_k
```

is the finite Taylor problem

```text
sum_{p=0}^{m-1} h_p/(s+a)^(p+1)
= 1/(s+k)        modulo (s-a)^m.
```

Equivalently, with

```text
z=s-a,
w=(2a+z)^(-1),
beta=k-a,
```

the target is

```text
1/(s+k) = w/(1+beta w).
```

Thus confluent Cauchy inversion is a rational Taylor truncation problem, not an opaque ill-conditioned
matrix inversion.
