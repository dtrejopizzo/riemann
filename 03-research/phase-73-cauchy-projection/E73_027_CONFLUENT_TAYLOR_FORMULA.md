# E73.027 - Confluent Taylor formula

## 1. Hermite interpolation problem

For a cluster centered at `a`, `Re a>0`, use the Hermite ansatz

```text
H(s)=sum_{p=0}^{m-1} h_p/(s+a)^(p+1).
```

For one critical node `k`, match

```text
H(s)=1/(s+k)    modulo (s-a)^m.
```

The normalized jet system is

```text
C_conf h = v_k,
```

where

```text
C_conf[q,p]=(-1)^q binom(p+q,p)/(2a)^(p+q+1),
v_k[q]=(-1)^q/(a+k)^(q+1).
```

## 2. Taylor change of variable

Let

```text
z=s-a,
w=(2a+z)^(-1),
beta=k-a.
```

Then

```text
s+a = 2a+z = 1/w,
```

and

```text
1/(s+k)=1/(a+k+z)=w/(1+beta w).
```

Therefore the Hermite coefficients `h_p` are exactly the coefficients of the polynomial in `w`

```text
P_m(w)=sum_{p=0}^{m-1} h_p w^(p+1)
```

whose expansion at

```text
w0=1/(2a)
```

matches

```text
f_beta(w)=w/(1+beta w)
```

through order `m-1`.

## 3. Consequence

The apparently ill-conditioned confluent matrix has a simple analytic meaning:

```text
C_conf^(-1)v_k = Taylor_m[f_beta at w0] converted to powers of w.
```

This gives the natural bound:

```text
||C_conf^(-1)v_k||_Herm
<= C_m(a,k)
```

where `C_m(a,k)` is controlled by the distance from `w0` to the pole

```text
w=-1/beta = -1/(k-a).
```

Thus local confluent growth can only occur when this pole approaches the Taylor center in the
`w`-plane, not when separated nodes coalesce.

## 4. Status

```text
proved: confluent Cauchy inversion equals rational Taylor matching;
validated: E73.027 exact numerical agreement;
feeds: CONFL-PI-NH.
```
