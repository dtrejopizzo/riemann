# E72.357 results - local ideal principal-part probe

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_357_local_ideal_principal_part_probe.py
```

The probe verifies the local algebra:

```text
Delta in ((z-a)^m,(w-b)^n)
```

if and only if the forbidden Taylor block

```text
0<=r<m, 0<=s<n
```

vanishes.  Equivalently, the mixed principal part of

```text
Delta/(Z(z)Z(w))
```

vanishes at `(a,b)`.

## Table

```text
m   n degZ degW kind       remNorm       ppNorm
1   1    5    5 member     0.00000e+00   0.00000e+00
1   1    5    5 nonmember  1.03078e+00   1.03078e+00

2   1    6    5 member     0.00000e+00   0.00000e+00
2   1    6    5 nonmember  1.03078e+00   1.03078e+00

1   3    5    7 member     0.00000e+00   0.00000e+00
1   3    5    7 nonmember  1.03078e+00   1.03078e+00

3   2    7    6 member     0.00000e+00   0.00000e+00
3   2    7    6 nonmember  1.03078e+00   1.03078e+00

4   3    8    7 member     0.00000e+00   0.00000e+00
4   3    8    7 nonmember  1.03078e+00   1.03078e+00
```

## Reading

The finite test is exact in the polynomial model:

```text
member    => remNorm=ppNorm=0;
nonmember => remNorm=ppNorm>0.
```

Thus the Xi-divisor gate can be implemented without ambiguity:

```text
for every zero pair (a,b) with multiplicities (m,n),
check the finite Hermite rectangle 0<=r<m, 0<=s<n.
```

This is the precise multiplicity version of E72.356.

## Consequence for CFIR

The next CFIR certificate should not ask for global vanishing of the compatibility minor.  It should
ask for the local Hermite block

```text
partial_z^r partial_w^s Delta_{c,d}(a,b)=O(L^B),
0<=r<m_a, 0<=s<m_b.
```

That is the finite, explicit form of

```text
Delta_{c,d} in (Z(z),Z(w)) + O(L^B).
```
