# E72.380 - Actual packet WWR certificate

## 1. Purpose

E72.379 reduced the finite-height wall problem to weighted wall regularity `WWR`.  Until now the
numerics used toy packets.  This note installs the actual Phase 72 finite Feshbach packet:

```text
B_z^M(y)=sum_{m,n in active} a_m(z) xi_n Q_y(m,n),
a_m(z)=(1-e^(zL))/(iz-d_m).
```

The goal is to make `WWR` an auditable finite statement for the real eigenvector packet.

## 2. Exact finite packet

For active indices `idx` and `d_m=2pi m/L`,

```text
Q_y(m,m)=2(1-y/L)cos(d_m y),
```

and for `m != n`,

```text
Q_y(m,n)= [sin(d_m y)-sin(d_n y)]/[pi(n-m)].
```

Thus every value

```text
B_z^M(y)
```

is a finite matrix-vector contraction.  No zero data or asymptotic model is used.

## 3. Actual WWR quantities

For `c>1/2`, `T>0`, and `delta=T^(-1/2)`, define

```text
g_z(t)=e^(ct)B_z^M(|t|)1_{|t|<=L}.
```

The finite-height prime-wall error is

```text
ErrPrime_T(z)
=sum_{n<=e^L} Lambda(n)n^(-1/2-c)
  int_{-L}^{L} g_z(t)D_T(t-log n)dt
 -sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n).          (1)
```

The local weighted scale is

```text
NearWWR_T(z)
=log(2+Tdelta)
  [ sum_{n<=e^L} Lambda(n)n^(-1/2)
      sup_{|t-log n|<=delta}|B_z^M(t)-B_z^M(log n)|
    + c delta sum_{n<=e^L} Lambda(n)n^(-1/2)|B_z^M(log n)| ].
```

The crude forbidden comparator is

```text
CrudeVar_T(z)=Var_{[-L,L]}(e^(ct)B_z^M(|t|)).
```

## 4. What the certificate tests

The diagnostic table reports:

```text
errPrime    = |ErrPrime_T(z)|,
nearWeighted= NearWWR_T(z),
crudeVar    = CrudeVar_T(z),
mass        = sum Lambda(n)n^(-1/2)|B_z^M(log n)|.
```

The expected signature for the correct route is:

```text
errPrime << nearWeighted << crudeVar
```

or at least `nearWeighted` growing much more mildly than `crudeVar`.  That means the wall gauge has
been cancelled locally by the prime weight before taking absolute values.

## 5. Status

```text
specified: exact finite construction of B_z^M;
specified: actual-packet WWR quantities;
validated numerically in E72.380_RESULTS;
open: prove polynomial bounds for NearWWR, FarWall, Endpoint, and finite-mesh tail uniformly.
```
