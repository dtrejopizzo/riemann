# E90.003 - Prime-cell expansion of the projective current

## 1. Exact prime matrix

The truncated shift representation gives

```text
H_P^in
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2) Q_(log n)^in,                   (1.1)
```

where `Q_y` is the symmetric shift cell and the superscript denotes the same
inner compression used in `M_t`.

Substitution of (1.1) into E90.002 gives a finite sum, so no interchange of
limits is involved.

## 2. Arithmetic response kernel

Define

```text
K_t(z,z_*;y)
 =sum_q Delta_(t,q)(z,z_*)
   [q_t^T Q_y^in v_t]/(kappa_(q,t)-kappa_t).          (2.1)
```

Then the exact projective current is

```text
J_t(z,z_*)
 =sum_(2<=n<=exp L)
   Lambda(n)n^(-1/2)
   K_t(z,z_*;log n).                                 (2.2)
```

This is the first formula in the endpoint route in which the surviving
projective current is displayed as an explicit von Mangoldt sum without any
zero input.

## 3. Resolvent form

Let

```text
S_t=(M_t-kappa_t I)^dagger                            (3.1)
```

be the reduced resolvent, zero on `span(v_t)`.  With the sign convention in
(3.1),

```text
S_t
 =sum_q q_t q_t^T/(kappa_(q,t)-kappa_t).             (3.2)
```

Equations (2.1)--(2.2) can equivalently be written as

```text
K_t(z,z_*;y)
 =[h_z S_t Q_y^in v_t]/[h_zv_t]
  -[h_(z_*) S_t Q_y^in v_t]/[h_(z_*)v_t],            (3.3)

J_t(z,z_*)
 =sum_n Lambda(n)n^(-1/2)
  K_t(z,z_*;log n).                                  (3.4)
```

## 4. Exact remaining kernel target

The prime weights alone do not identify the Euler object.  The required
information is the cofinal behavior of the response kernel (3.3).  In
particular, termwise convergence of `K_t` is neither asserted nor needed;
the finite signed von Mangoldt sum is the primary quantity.

## 5. Status

```text
proved:
  exact finite von Mangoldt expansion of the projective line current;
  equivalent reduced-resolvent kernel;

open:
  arithmetic identification of its integrated bilateral form.
```
