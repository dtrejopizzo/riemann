# E73.026 - Confluent Pi certificate

## 1. Problem

E73.025 showed that the separated-node Lebesgue factor

```text
e^(Re b L)sum_k |Pi(b,k)|
```

can blow up super-exponentially when off-line nodes form an exponentially tight cluster.  This could
be either:

```text
real obstruction,
or coordinate singularity.
```

E73.026 tests the second possibility by switching to Hermite/confluent Cauchy coordinates.

## 2. Hermite projection block

Let an off-line cluster of multiplicity `m` be centered at `a`, with `Re a>0`.  Instead of separate
poles at nearby `b_j`, use the Hermite rational ansatz

```text
H(s)=sum_{p=0}^{m-1} h_p/(s+a)^(p+1).
```

Match the first `m` normalized jets of

```text
Q(s)=sum_k G_k/(s+k)
```

at `s=a`:

```text
(1/q!) H^(q)(a) = (1/q!) Q^(q)(a),     0<=q<m.
```

The confluent Cauchy matrix is

```text
C_conf[q,p]
= (1/q!) partial_s^q (s+a)^(-p-1)|_{s=a}
= (-1)^q binom(p+q,p)/(2a)^(p+q+1).
```

The contribution of one critical node `k` to the right side is

```text
v_k[q]=(-1)^q/(a+k)^(q+1).
```

Therefore the Hermite projection coefficients are explicit:

```text
h(k)=C_conf^(-1)v_k.
```

## 3. Confluent Lebesgue quantity

The Hermite analogue of the row Lebesgue factor is

```text
Leb_conf(a,m;K)
= e^(Re a L) sum_{k in K} sum_{p=0}^{m-1} |h_p(k)|/p!.
```

The factorial normalization matches normalized Hermite jets.  Other equivalent Hermite norms change
only finite-dimensional constants for fixed `m`.

## 4. Result

E73.026 compares:

```text
Leb_sep(epsilon)    from separated nodes a,a+i epsilon,...
Leb_conf            from the Hermite limit.
```

As `epsilon=exp(-cL)` shrinks, `Leb_sep` explodes by inverse powers of `epsilon`, while `Leb_conf`
remains fixed.  Thus the E73.025 blow-up is not intrinsic to the Cauchy projection; it is a coordinate
singularity.

## 5. Consequence for the route

The corrected sufficient gate is not separated `PI-LEB-NH`.  It is:

```text
CONFL-PI-NH:
For each natural-height off-line cluster, after replacing separated node coordinates by normalized
Hermite jet coordinates, the weighted confluent Cauchy projection satisfies

e^(alpha L) sum_{k in K_L} ||C_conf(A)^(-1)v_k||_Herm <= L^B.
```

Then, together with E72.327:

```text
CONFL-PI-NH + CRIT-POLY
=> Hermite NAT-PROJ
=> scalar WRL.
```

## 6. What remains

Two finite checks remain before this becomes a proof route:

```text
1. rewrite the Phase 72 natural-height nodal system fully in normalized Hermite coordinates;
2. prove the natural-height bound for the confluent Cauchy projection over all clusters.
```

E73.026 closes only the local cluster singularity.  It does not yet control the global number,
placement, or condition of all natural-height clusters.
