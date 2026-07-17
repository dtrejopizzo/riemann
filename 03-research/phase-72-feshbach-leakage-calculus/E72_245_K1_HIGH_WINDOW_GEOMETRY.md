# E72.245 - K1 high-window geometry

## Purpose

E72.243 reduced the low trace condition to:

```text
t_B<0
<=> sum_{n in S_1} beta_n K1(u_n)>0,

K1(u)=Tr(PM_uP),
beta_n=Lambda(n)/sqrt(n),
u_n=log n/L.
```

This note checks whether the positivity is geometric, arithmetical, or both.

## Diagnostic

Script:

```text
E72_245_k1_high_window_geometry_probe.py
```

Output:

```text
E72.245 K1 high-window geometry probe
K1(u)=Tr(P M_u P). primeAvg=sum beta K1 / sum beta; sumBetaK1=-tB.
lam minK1 maxK1 meanK1 negFrac intK1 sumBetaK1 primeAvg mass count
 12 -1.955596e-02 +2.683682e-02 +1.135746e-02 0.165 +1.139373e-02 +2.018045e-01 +1.366502e-02 1.476796e+01    35
 16 -9.368683e-03 +1.624013e-02 +8.764808e-03 0.090 +8.798346e-03 +1.908920e-01 +8.900117e-03 2.144825e+01    55
 20 -1.365306e-04 +1.458338e-02 +8.316061e-03 0.022 +8.334914e-03 +2.119065e-01 +7.504729e-03 2.823639e+01    79
 24 -3.774794e-03 +1.278093e-02 +6.838225e-03 0.067 +6.859931e-03 +2.375759e-01 +6.933629e-03 3.426429e+01   105
 28 -6.857912e-03 +1.110898e-02 +5.094156e-03 0.122 +5.111672e-03 +2.162864e-01 +5.271645e-03 4.102826e+01   136
 32 -1.917067e-03 +9.820132e-03 +3.210423e-03 0.085 +3.210994e-03 +1.153524e-01 +2.400028e-03 4.806295e+01   171
 36 -2.929272e-03 +7.612780e-03 +4.202606e-03 0.102 +4.216708e-03 +2.388454e-01 +4.388385e-03 5.442673e+01   206
```

## Reading

The positivity of `sum beta K1` is primarily geometric:

```text
average_{u in (0.6,1)} K1(u) > 0.
```

The prime-power weighted average tracks the continuous average and remains positive:

```text
primeAvg > 0.
```

The kernel is not pointwise nonnegative, but its negative region is limited:

```text
negFrac ~= 0.02--0.17.
```

The delicate `lambda=32` window is explained by discrepancy:

```text
intK1 ~= 3.21e-3,
primeAvg ~= 2.40e-3.
```

The average remains positive, but with reduced margin.

## Proof Target

Prove:

```text
int_{0.6}^1 K1(u)du >= c_K/L
```

and a prime-power discrepancy bound:

```text
| (sum beta_n K1(u_n))/(sum beta_n)
  - average(K1) |
<= error_K(L),
```

with:

```text
average(K1)-error_K(L)>0.
```

Then `t_B<0` follows without zero information.
