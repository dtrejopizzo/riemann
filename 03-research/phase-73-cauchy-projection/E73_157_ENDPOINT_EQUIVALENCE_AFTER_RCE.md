# E73.157 - Endpoint equivalence after RCE

Date: 2026-07-12.

## 1. Purpose

E73.153--E73.156 re-entered the transformed packet route from a different
side:

```text
forced Mellin rows -> Cauchy divisor rows -> Cauchy-plane residual equation
-> strong critical TPW / Strong-PAIRZ.
```

This note records the audit result: after importing the late Phase 72 tail
absorption and the early Phase 73 Cauchy projection reduction, the endpoint
is again exactly the finite critical-source projection

```text
NAT-SRC / CC-PROJ.
```

Thus the current work has not produced a second independent gate.  It has
confirmed that all transformed/Mellin/Cauchy formulations collapse to the
same finite identity.

## 2. The collapse chain

E73.153 proves:

```text
M_L(w)^(-1)[P_{z_1,w}^{signed};P_{z_2,w}^{signed}]
= [q_w;q_-w],
q_w(n)=1/(w+i d_n).
```

Therefore the signed forced-row endpoint is exactly the Cauchy divisor:

```text
H0-DIV_17:
|H_0(w)|+|H_0(-w)| <= C L^-17.
```

E73.154 rewrites this through the Cauchy-plane residual equation:

```text
(mu I-A(w))h = rho(w)xi_L.
```

E73.155 splits the residual:

```text
rho(w)xi_L = rho_model(w)xi_L-rho_prime(w)xi_L.
```

E73.156 identifies this with the exponent-strong critical-node version of
E72.317--E72.321:

```text
Strong-PAIRZ_17 + Tail_17.
```

But E72.391--E72.392 absorb the finite Fourier tail into the nodal system,
and E72.394 closes the high outside-zero tail by switching to natural height.
E72.396 then proves that the remaining finite assertion is:

```text
NAT-PROJ:
max_{a in O_L} e^(Re a L)
 |(C_OO^(-1)C_OKG_K)_a| <= L^B.
```

Finally, E73.001--E73.003 remove the matrix inverse and rewrite this as:

```text
NAT-SRC:
max_{b in O_L} e^(Re b L)
 |sum_m xi_m S_b(d_m)| <= L^B,
```

or equivalently E73.023:

```text
CC-PROJ:
max_{b in O_L} e^(Re b L)
 |sum_{k in K_L} Pi(b,k)g_cancelled(k)| <= L^B.
```

## 3. Meaning for the current Omega7 route

The active finite obstruction is not:

```text
rowspace,
pseudoinverse,
choice of two Mellin rows,
termwise model/prime estimates,
or finite Fourier tail.
```

It is the finite critical-source cancellation:

```text
sum_m xi_m S_b(d_m)
```

after the rational Cauchy projection kernel `Pi(b,k)` has mixed the critical
cancelled Cauchy data.

This is why the RCE cancellation in E73.155 looks real but does not by
itself close anything: it is a numerical shadow of the same `CC-PROJ`
identity.

## 4. Strong versus polynomial form

Phase 72 needed `NAT-PROJ` with a polynomial right side in the exponentially
weighted off-line norm:

```text
e^(Re b L)|CC-PROJ_b| <= L^B.
```

The Phase 73 standard-box route asks for a stronger critical-node exponent
in local rows, but after the transformed/nodal reduction the correct
load-bearing object is still the same finite projection.  Therefore the
right strengthened statement is:

```text
Strong-CC-PROJ:
for the natural-height window W_L and the standard-box critical data,
the finite source S_b satisfies the weighted projection bound with the
power required by CSV_17 after the E73.123 envelopes.
```

In practice, the exponent bookkeeping is:

```text
Strong-CC-PROJ
=> Strong-PAIRZ_17 + absorbed tail
=> RCE_17
=> H0-DIV_17 / LDIV_17
=> CSV_17
=> Uniform GATE-73.
```

## 5. Exact finite identity left

The final identity can be written without zero tails, Cauchy inverses, or
Mellin-row choices:

```text
For every off-line representative b in O_L,

SRC_b(L)
:= sum_m xi_L(m)
   sum_{k=i gamma in K_L}
      Pi(b,k)
      DD_L(u_k,d_m)

must satisfy

e^(Re b L)|SRC_b(L)| <= L^B
```

with the precise divided-difference kernel from E73.003:

```text
DD_L(u,d)=[e^(-idL)-e^(-iuL)]/(u-d),
u=-gamma.
```

Thus the exact form is:

```text
SRC_b(L)
= sum_m xi_L(m)
   sum_{k=i gamma in K_L} Pi(b,k)DD_L(-gamma,d_m).
```

No hidden analytic object remains in this expression.

## 6. Next proof direction

The only plausible non-circular route left is:

```text
Use the finite pole-even CCM equation for xi_L to prove
<xi_L,S_b> is exponentially small in the weighted off-line norm.
```

Equivalently, show that each source vector `S_b` lies in the image of
`H_L-mu_L I`, up to the required exponentially small null component, but
without using adjugate or pseudoinverse as the source of cancellation.

This is the same lesson as E73.149--E73.153, now in the correct final
coordinates.

## 7. Status

proved:

```text
RCE/Strong-PAIRZ returns to NAT-SRC/CC-PROJ;
finite tail and outside-zero tail are not separate remaining gates;
the remaining identity is finite and explicit.
```

open:

```text
prove Strong-CC-PROJ / NAT-SRC from the finite CCM/Feshbach equation.
```

This is the present exact frontier.
