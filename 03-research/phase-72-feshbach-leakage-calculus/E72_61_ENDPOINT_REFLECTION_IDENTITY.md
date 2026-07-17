# E72.61 -- Endpoint reflection identity for LFDC

**Date:** 2026-07-08.
**Role:** turn the corrected post-main LFDC scalar into an exact reflected Loewner-Stieltjes pairing.

## 0. Setup

Let:

```text
L=log x,             D=diag(2*pi*n/L),
r=L-y,              J=11^T.
```

For the Cauchy-compressed vector and prolate ground vector write:

```text
v=v_{x,s}=C_x^(-1)Q_x(sI-D)^(-1)1,
k=k_x,
a(y)=<v,Q_x(y)k>.
```

The corrected post-main scalar discrepancy from E72.60 is:

```text
D_x(s;z)
 = sum_{n<=x} Lambda(n)(n/x)^z n^(-1/2)a(log n)
   - int_0^L exp(z(y-L))exp(y/2)a(y)dy.          (D)
```

## 1. Exact endpoint reflection

### Lemma 72.61.1

For every `0<=r<=L`,

```text
Q_x(L-r) = (2/L)Lo_r,                             (REF)
```

where:

```text
Lo_r(m,n) = [sin(d_mr)-sin(d_nr)]/(d_m-d_n),       m != n,
Lo_r(n,n)=r cos(d_nr).
```

### Proof

For `m=n`,

```text
q_nn(L-r)=2(1-(L-r)/L)cos(d_n(L-r))
        =2(r/L)cos(d_nr)
        =(2/L)Lo_r(n,n),
```

because `d_nL=2*pi*n`.

For `m != n`,

```text
q_mn(L-r)
 = [sin(d_m(L-r))-sin(d_n(L-r))]/[pi(n-m)]
 = [-sin(d_mr)+sin(d_nr)]/[pi(n-m)].
```

Since:

```text
d_m-d_n=2*pi(m-n)/L=-2*pi(n-m)/L,
```

we get:

```text
(2/L)Lo_r(m,n)
 = (2/L)[sin(d_mr)-sin(d_nr)]/(d_m-d_n)
 = [sin(d_nr)-sin(d_mr)]/[pi(n-m)].
```

This is the previous display. `QED`

Thus the endpoint rank-one expansion in E72.56 is the first Taylor term of an exact identity, not only
an asymptotic statement.

## 2. Reflected Chebyshev measure

Define the endpoint-pushed Chebyshev measure:

```text
dPsi_x^leftarrow(r) := sum_{n<=x} Lambda(n) delta_{log(x/n)}(r),
```

and its PNT main:

```text
dm_x^leftarrow(r) := x exp(-r)dr.
```

Set:

```text
dE_x^leftarrow(r):=dPsi_x^leftarrow(r)-dm_x^leftarrow(r).
```

For:

```text
b_{x,s}(r):=<v_{x,s},Lo_r k_x>,
phi_{x,s,z}(r):=exp(-(z-1/2)r)b_{x,s}(r),
```

the corrected scalar discrepancy has the exact form:

```text
D_x(s;z)
 = (2/(L sqrt(x))) int_0^L phi_{x,s,z}(r)dE_x^leftarrow(r).       (RLFDC)
```

### Proof

If `n=xe^{-r_n}`, then:

```text
(n/x)^z n^(-1/2)=x^(-1/2)exp(-(z-1/2)r_n).
```

By `(REF)`,

```text
a(log n)=a(L-r_n)=(2/L)b(r_n).
```

Therefore the discrete term in `(D)` is:

```text
(2/(L sqrt(x))) int_0^L exp(-(z-1/2)r)b(r)dPsi_x^leftarrow(r).
```

For the continuous main, use `y=L-r`, `dy=-dr`:

```text
int_0^L exp(z(y-L))exp(y/2)a(y)dy
 = (2 sqrt(x)/L)int_0^L exp(-(z+1/2)r)b(r)dr
 = (2/(L sqrt(x)))int_0^L exp(-(z-1/2)r)b(r)xexp(-r)dr.
```

Subtracting gives `(RLFDC)`. `QED`

## 3. Abel form from the endpoint

Let the endpoint cumulative error be:

```text
E_x^leftarrow(R)
 := int_0^R dE_x^leftarrow(r)
 = Psi(x)-Psi(xe^(-R))-x(1-e^(-R)).
```

For any smooth approximation to the Stieltjes endpoints:

```text
int_0^L phi(r)dE_x^leftarrow(r)
 = phi(L)E_x^leftarrow(L)-int_0^L E_x^leftarrow(r)phi'(r)dr.       (ABEL-left)
```

Here `E_x^leftarrow(0)=0`. Also:

```text
phi'(r)
 = exp(-(z-1/2)r)
   ( <v,partial_rLo_r k> -(z-1/2)<v,Lo_rk> ).                    (PHI')
```

The derivative still has finite Loewner structure:

```text
[D,partial_rLo_r]=[Dcos(rD),J].                                  (DLo)
```

## 4. Exact sufficient theorem

### Theorem 72.61.2 -- Endpoint reflected LFDC criterion

Fix compact Cauchy-height and `z` windows with `Re z>1/2`. Assume:

```text
sup_{s,z}|phi_{x,s,z}(L)E_x^leftarrow(L)| = o(L sqrt(x)),          (BND)
```

and:

```text
sup_{s,z}|int_0^L E_x^leftarrow(r)phi'_{x,s,z}(r)dr|
     = o(L sqrt(x)).                                               (ERI)
```

Then LFDC holds:

```text
sup_{s,z}|D_x(s;z)| -> 0.
```

The same conclusion for one `s`-derivative follows if `(BND)` and `(ERI)` also hold after replacing
`v_{x,s}` by `partial_s v_{x,s}`.

### Proof

Insert `(ABEL-left)` into `(RLFDC)`:

```text
D_x(s;z)
 = (2/(L sqrt(x)))
   [ phi(L)E_x^leftarrow(L)-int_0^L E_x^leftarrow(r)phi'(r)dr ].
```

The two assumptions make the bracket `o(L sqrt(x))`, uniformly on the chosen windows. `QED`

## 5. What has genuinely changed

The remaining estimate is no longer an operator-norm statement and no longer a raw prime endpoint sum.
It is the scalar reflected endpoint inequality `(ERI)` for the single test family:

```text
phi'_{x,s,z}(r)
 = exp(-(z-1/2)r)
   ( <v,partial_rLo_r k> -(z-1/2)<v,Lo_rk> ).
```

This family is fixed by:

```text
C_xv=Q_x(sI-D)^(-1)1,
H_x^0k=mu_x^0k,
[D,partial_rLo_r]=[Dcos(rD),J].
```

Thus the exact open theorem is:

```text
Endpoint Reflected Inequality:
int_0^L E_x^leftarrow(r)phi'_{x,s,z}(r)dr = o(L sqrt(x)).
```

This is strictly sharper than the incoherent PNT bound. PNT alone gives only `E_x^leftarrow(r)=o(x)`;
the missing content is that the specific Loewner-Feshbach test `phi'` is orthogonal to the endpoint
Chebyshev discrepancy at half-power scale.

## 6. Status

```text
proved: exact endpoint reflection Q_x(L-r)=(2/L)Lo_r;
proved: corrected LFDC equals a reflected Loewner-Stieltjes Chebyshev pairing;
proved: Endpoint Reflected Inequality plus endpoint boundary control implies LFDC;
open:   prove ERI from the Feshbach equation and the Loewner commutator.
```
