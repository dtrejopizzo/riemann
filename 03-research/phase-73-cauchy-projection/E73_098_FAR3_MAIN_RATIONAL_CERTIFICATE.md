# E73.098 - FAR3 main rational certificate

## 1. Purpose

This note states the last finite piece of `GATE-73`: the three FAR3 main nodewise rational bounds.

All other pieces have already been reduced to finite certificates:

```text
LOCK-COMP-BUD;    E73.091
TAIL-LC-BUD;      E73.094
OUT-FAR;          E73.096
```

## 2. FAR3 main terms

For a natural-height off-line cluster `A`, let:

```text
D_3(A,L)= three critical rows selected by FAR score
F_k(A,L)=W_k(A,L)dist(-gamma_k,Div(P_x)).
```

For each selected row define:

```text
T_k(A,L)
:=
W_k(A,L)|C_x(i gamma_k)|.
```

Using the finite Cauchy divisor:

```text
C_x(i gamma_k)=P_x(-gamma_k)/D_x(-gamma_k),
```

this is the explicit rational quantity:

```text
T_k(A,L)
=
e^(alpha L)G_theta,m(a,i gamma_k)|1-e^(i gamma_k L)|
|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

## 3. Certificate

Define `FAR3-MAIN-RAT(A,L)` to be the existence of nonnegative budgets `b_k(A,L)` for
`gamma_k in D_3(A,L)` such that:

```text
T_k(A,L) <= b_k(A,L)L^-5,
```

and:

```text
sum_{gamma_k in D_3(A,L)} b_k(A,L) <= C_main.
```

Equivalently:

```text
sum_{gamma_k in D_3(A,L)} T_k(A,L) <= C_main L^-5.
```

The nodewise form is kept because it is the version compatible with interval certificates on cluster
boxes.

## 4. Theorem

**Theorem 98.1.**  `FAR3-MAIN-RAT(A,L)` gives the main part of the WCS budget:

```text
sum_{gamma_k in D_3(A,L)}
W_k(A,L)|C_x(i gamma_k)|
<= C_main L^-5.
```

*Proof.*  This is the sum of the three nodewise inequalities in the definition.  The equality with
the rational expression follows from `C_x=P_x/D_x`, proved in E73.038. `□`

## 5. Relation to ROW-MAIN

E73.066 states the same content in rowspace language:

```text
T_k(A,L)=Pref_k(A,L)dist(k_{-gamma_k},Row(E_x)).
```

E73.098 is the rational certificate version:

```text
dist(k_{-gamma_k},Row(E_x))
= |P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

Thus no extra Hilbert-space object remains in the certificate.

## 6. Status

```text
finite certificate: stated;
numeric validation: E73.097;
uniform theorem still needed: prove FAR3-MAIN-RAT over all natural-height cluster boxes.
```
