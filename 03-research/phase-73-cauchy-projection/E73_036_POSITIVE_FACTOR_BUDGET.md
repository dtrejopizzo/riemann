# E73.036 - Positive factor budget

## 1. Definitions

Let `A` be a natural-height off-line Hermite cluster centered at

```text
a = alpha + i tau, alpha>0,
```

with multiplicity `m`.  Let `K_L={i gamma_k}` be the critical natural-height window.

For every critical node define the raw finite Cauchy transform

```text
C_x(i gamma_k) := sum_n xi_n/(-gamma_k-d_n),
```

and the mesh multiplier

```text
M_L(gamma_k) := 1-exp(i gamma_k L).
```

Let

```text
h_A(k) := C_conf(A)^(-1)v_k
```

be the confluent Hermite projection coefficient from E73.026/E73.027, and use the Hermite norm

```text
||c||_Herm := sum_{r=0}^{m-1} |c_r|/r!.
```

The final signed output is

```text
Out(A,L) := sum_{k in K_L} h_A(k) M_L(gamma_k) C_x(i gamma_k).
```

## 2. Lemma: positive budget implies the signed gate

Assume that for some fixed `B`

```text
FBUD(A,L):
e^(alpha L) sum_{k in K_L}
||h_A(k)||_Herm |M_L(gamma_k)| |C_x(i gamma_k)|
<= L^B
```

holds uniformly for every natural-height off-line cluster `A`.

Then `DATA-HERM` holds:

```text
e^(alpha L)||Out(A,L)||_Herm <= L^B.
```

## 3. Proof

By the triangle inequality in the finite Hermite norm,

```text
||Out(A,L)||_Herm
= ||sum_k h_A(k)M_L(gamma_k)C_x(i gamma_k)||_Herm
<= sum_k ||h_A(k)||_Herm |M_L(gamma_k)| |C_x(i gamma_k)|.
```

Multiplying by `e^(alpha L)` and applying `FBUD(A,L)` gives the claim.

Together with E73.032 and E73.023,

```text
FBUD => DATA-HERM => CC-PROJ => NAT-PROJ.
```

By E72.396, `NAT-PROJ` gives the scalar WRL branch needed for the compact route.

## 4. Why this is not the old incoherent ceiling

Earlier absolute estimates failed because they summed raw Cauchy/Haar words before the correct
shorted and confluent normalization.  The present budget is applied only after:

```text
1. C_OO^{-1} has been replaced by the exact residue kernel Pi;
2. close off-line clusters have been converted to confluent Hermite coordinates;
3. the critical datum has been factorized as M_L times C_x.
```

E73.036 shows that this budget is close to the actual output in tested natural-height windows.

## 5. Remaining theorem

The proof problem is now the positive product divisibility estimate:

```text
PFD:
e^(alpha L) sum_{gamma_k in K_L}
||h_A(i gamma_k)||_Herm
|1-exp(i gamma_k L)|
|C_x(i gamma_k)|
<= L^B.
```

This is strictly stronger than the signed `CRIT-DIV-FACT`, but it is finite, explicit, and avoids
the false universal moment-cancellation route.
