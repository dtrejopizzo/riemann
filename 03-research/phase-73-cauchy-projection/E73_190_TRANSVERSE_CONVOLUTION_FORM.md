# E73.190 - Transverse convolution form

Date: 2026-07-14.

## 1. Purpose

E73.189 reduced the load-bearing theorem to a Dirichlet explicit-formula
matching for

```text
B_a(y)=q_a Q_L(y) eta,
q_a(m)=1/(a+i d_m),
eta=(I-P_w)xi_L,
q_w eta=q_-w eta=0.
```

This note rewrites `B_a` as a one-dimensional convolution packet and records
the exact differential identity supplied by the Cauchy denominator.  This is
the analytic form in which one should try to prove the matching.

## 2. Finite Fourier packets

Let

```text
A_a(r)=sum_m q_a(m)e^(i d_m r),
E(r)=sum_n eta_n e^(i d_n r),
D(r)=sum_m e^(i d_m r).
```

The finite Weyl kernel has the exact integral representation

```text
Q_L(y)_{mn}
= 1/L int_0^(L-y)
   [ e^(i d_m(t+y)) e^(-i d_n t)
     + e^(-i d_m(t+y)) e^(i d_n t) ] dt.          (1)
```

Therefore

```text
B_a(y)
= 1/L int_0^(L-y)
   [ A_a(t+y) E^*(-t)
     + A_a^#(t+y) E(t) ] dt,                      (2)
```

where

```text
E^*(-t)=sum_n eta_n e^(-i d_n t),
A_a^#(r)=sum_m q_a(m)e^(-i d_m r).
```

No approximation or limit is used.

## 3. Cauchy differential identity

Since

```text
i d_m/(a+i d_m)=1-a/(a+i d_m),
```

one has the exact identity

```text
A_a'(r)=D(r)-a A_a(r).                            (3)
```

Similarly,

```text
(A_a^#)'(r)=-D(-r)+a A_a^#(r).                    (4)
```

This is the correct derivative rule for the transverse Cauchy packet.  It is
the analogue of E72.337, but with no endpoint multiplier and with a source
vector satisfying the two Cauchy moment conditions.

## 4. Endpoint and moment consequences

The two Cauchy constraints are

```text
q_w eta=0,       q_-w eta=0.
```

For the corresponding rows this gives

```text
B_a(0)=2q_a eta=0,        a in {w,-w}.
```

Also `B_a(L)=0` because the integral interval in (2) collapses.

The derivative at the left endpoint follows from the universal kernel identity
`Q_L'(0)_{mn}=-2/L`:

```text
B_a'(0)=-(2/L)(sum_m q_a(m))(sum_n eta_n).          (5)
```

Thus the first derivative is rank-one.  This is important because it shows the
Dirichlet condition alone does not force all low Taylor data to vanish; a
proof must either control or cancel the scalar source mass `sum eta_n`.

## 5. Proof-facing theorem

Substituting (2) into the Dirichlet explicit-formula matching gives an exact
finite convolution identity:

```text
A_L[B_a]-P_L[B_a]=O_R(L^-R),
```

where `A_L` has the simplified Dirichlet form from E73.189 and `P_L` samples
`B_a(k log p)`.

The theorem should be proved using only:

```text
1. convolution form (2);
2. Cauchy derivative identities (3)--(4);
3. endpoint zeros B_a(0)=B_a(L)=0;
4. two moment constraints q_w eta=q_-w eta=0;
5. the finite eigenvector origin of eta, but not the smallness of Q_w xi_L.
```

## 6. Status

```text
proved: exact convolution representation of B_a;
proved: exact derivative identities A_a'=D-aA_a and (A_a^#)'=-D(-r)+aA_a^#;
proved: B_a'(0) is rank-one;
open: prove model-prime matching from this convolution/moment structure.
```
