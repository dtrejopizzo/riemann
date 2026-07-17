# E72.357 - Local ideal principal-part theorem

## 1. Purpose

E72.356 states the Xi-divisor certificate as local ideal membership:

```text
Delta(z,w) in (Z(z), Z(w)).
```

This note proves the exact finite local test, including multiplicities.  It replaces the informal
"mixed residues vanish" phrase by a coefficient-level criterion that can be checked with Taylor jets.

## 2. Local setting

Fix two shifted zeros `a,b` of `Z`, with multiplicities `m,n`.  Write

```text
Z(z)=(z-a)^m U(z),        U(a) != 0,
Z(w)=(w-b)^n V(w),        V(b) != 0.
```

Let `Delta(z,w)` be holomorphic in a bidisc around `(a,b)`.

The local ideal is

```text
I_{a,b}:=(Z(z),Z(w)) = ((z-a)^m,(w-b)^n),
```

because `U,V` are units.

## 3. Taylor remainder criterion

Expand

```text
Delta(z,w)=sum_{r,s>=0} c_{r,s}(z-a)^r(w-b)^s.
```

Then

```text
Delta in I_{a,b}
```

if and only if

```text
c_{r,s}=0       for 0<=r<m and 0<=s<n.              (1)
```

Equivalently,

```text
partial_z^r partial_w^s Delta(a,b)=0
```

for every `0<=r<m`, `0<=s<n`.

### Proof

Modulo the ideal `((z-a)^m,(w-b)^n)`, every holomorphic germ has a unique finite remainder

```text
Rem_{a,b} Delta
= sum_{0<=r<m, 0<=s<n} c_{r,s}(z-a)^r(w-b)^s.
```

Thus `Delta` lies in the ideal exactly when this remainder is zero.  The coefficients of the
remainder are the Taylor coefficients in (1).  `QED`

## 4. Principal-part form

Divide by `Z(z)Z(w)`:

```text
Q(z,w)=Delta(z,w)/(Z(z)Z(w)).
```

Since `U,V` are units, the mixed principal part of `Q` at `(a,b)` is determined by the same finite
Taylor block:

```text
PP_{a,b} Q = 0
```

if and only if (1) holds.

For simple zeros, this reduces to:

```text
Delta(a,b)=0.
```

For multiple zeros, all mixed derivatives in the rectangle

```text
0<=r<m, 0<=s<n
```

must vanish.

## 5. Hermite CFIR form

Let `alpha=(a,r)` and `beta=(b,s)` be Hermite slots.  The Lambda-elimination minor is

```text
Delta_{alpha,beta}
=(S_alpha Adj(E))(K_beta Adj(E))
 -(S_beta Adj(E))(K_alpha Adj(E)),
```

or, in the rank-one channel,

```text
Delta_{alpha,beta}
=(S_alpha xi)(K_beta xi)-(S_beta xi)(K_alpha xi).
```

The local ideal theorem says that the full Xi-divisor compatibility is equivalent to the finite
Hermite block of these minors vanishing:

```text
Delta_{(a,r),(b,s)}=0
for 0<=r<m_a, 0<=s<m_b.                              (2)
```

Thus multiplicity bookkeeping is not an extra analytic tail.  It is exactly a finite jet block.

## 6. Polynomial residual version

If exact membership is unavailable, the polynomial version is:

```text
|partial_z^r partial_w^s Delta(a,b)| <= C_{a,b,r,s} L^B
```

for all slots in the finite rectangle.  This is the form needed before applying the maximal
off-line Cauchy block inverse.

## 7. Status

```text
proved: local ideal membership is equivalent to finite Taylor-block vanishing;
proved: principal-part cancellation is the same finite condition;
proved: Hermite multiplicities become finite Lambda-minor jet blocks;
open: prove these blocks for the exact Xi-derived CFIR residual.
```
