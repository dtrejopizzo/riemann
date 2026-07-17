# P76.041 - Two-generator logarithmic formula

Use the notation of P76.015.  Put

```text
p=v^T R_b(s-S_b1),
q=u^T R_b(s-S_b1),

a_b=2/L+4p/L^2,
b_b=-2S_b/L-4q/L^2.                            (TG-1)
```

Define the two Cauchy transforms and boundary constants

```text
U(z)=sum_n u_n/(z-d_n),    U_b=sum_n u_n/(d_n-d_b),
V(z)=sum_n v_n/(z-d_n),    V_b=sum_n v_n/(d_n-d_b). (TG-2)
```

The partial-fraction identity

```text
1/[(z-d_n)(d_n-d_b)]
 =[1/(z-d_n)+1/(d_n-d_b)]/(z-d_b)              (TG-3)
```

turns the full pole-linear-wedge formula into

```text
T_b(z)=F_b(z)/(z-d_b),                          (TG-4)

F_b(z)=1+a_b[U(z)+U_b]+b_b[V(z)+V_b].           (TG-5)
```

Consequently

```text
T_b'(z)/T_b(z)=F_b'(z)/F_b(z)-1/(z-d_b),        (TG-6)

F_b'(z)=a_b U'(z)+b_b V'(z).                    (TG-7)
```

Equations `(TG-4)`--`(TG-7)` are exact.  The large linear and wedge terms
are never estimated separately; their signed cancellation is encoded in
`a_b,b_b` before taking a logarithm.

## Reduced endpoint

Substitution in P76.037 gives

```text
J_core(sigma)
=L coth(sigma L/2)
 +2 Re[iF_b'(i sigma)/F_b(i sigma)-i/(i sigma-d_b)]
 -B_ext(sigma).                                 (TG-8)
```

Thus the false hard-Euler trace of P76.040 is replaced by the exact
two-generator symbol `(TG-8)`.  The remaining analytic task is to identify
the continuum limits of the coupled transforms

```text
a_b U+b_b V,
a_b U'+b_b V'
```

directly from the cell equations `Au=s`, `Av=1`.
