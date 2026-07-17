# E73.066 - ROW-MAIN target

## 1. Reason for refinement

E73.060 introduced the sufficient split

```text
Pref_k(A,L) <= C_pref L^5,
|C_x(-gamma_k)| <= C_cauchy L^-10.
```

This proves `Main_3=O(L^-5)`, but E73.065 shows that the split is stronger than necessary.
The finite data support the product bound directly, while the Cauchy exponent alone varies from
node to node.

The theorem target should therefore be the WCS term itself.

## 2. Setup

Let

```text
E_x=H_x-mu_x I,
E_x xi_x=0,
||xi_x||=1,
d_n=2 pi n/L,
k_t(n)=1/(t-d_n).
```

Here `xi_x` is the exact normalized ground eigenvector.  The symmetric pole-even gauge vector is not
used in the proof statement.

For a FAR3 node `gamma_k`, put `t=-gamma_k` and

```text
Pref_k(A,L)
= e^(alpha L)G_theta,m(a,i gamma_k)|1-exp(i gamma_k L)|.
```

Then the corresponding main WCS contribution is

```text
T_k=Pref_k(A,L)|<xi_x,k_t>|.
```

## 3. Exact projection lemma

Assume `H_x` is self-adjoint and `mu_x` is a simple eigenvalue with normalized eigenvector `xi_x`.
Then

```text
Row(E_x)=xi_x^perp
```

and for every real `t` outside the pole set `{d_n}`,

```text
dist(k_t,Row(E_x))=|<xi_x,k_t>|.
```

Proof.  Since `E_x` is self-adjoint,

```text
Row(E_x)^perp = Ker(E_x).
```

The kernel is `span{xi_x}` by simplicity.  Hence `Row(E_x)=xi_x^perp`.
The orthogonal projection of `k_t` onto `Row(E_x)^perp` is `<xi_x,k_t>xi_x`, so its norm is
`|<xi_x,k_t>|`.

Therefore

```text
T_k=Pref_k(A,L) dist(k_t,Row(E_x)).
```

## 4. The sharp main estimate

The main estimate needed for FAR3 is:

```text
ROW-MAIN-5:
sum_{gamma_k in FAR3(A,L)}
Pref_k(A,L) dist(k_{-gamma_k},Row(E_x))
<= C_main L^-5.
```

Equivalently, by the projection lemma,

```text
sum_{gamma_k in FAR3(A,L)}
Pref_k(A,L)|C_x(-gamma_k)|
<= C_main L^-5.
```

This is exactly the `MAIN` half of `BUD-5/9`.

## 5. Relation to previous targets

The old sufficient chain was:

```text
PREF-5 + CMAIN-10 => MAIN.
```

The refined chain is:

```text
ROW-MAIN-5 => MAIN.
```

The refined statement is strictly better as a proof target because it preserves the measured
tradeoff between the Hermite-mesh prefactor and the signed Cauchy rowspace defect.

## 6. Analytic content

The open theorem is no longer a product inequality for `P_x/D_x` alone.  It is a spectral
divisibility statement:

```text
the FAR3 Cauchy rows are close enough to Row(H_x-mu_x I), after the exact Hermite prefactor.
```

This is where the CCM autoadjointness enters the final gate.  A proof must use the finite equation

```text
(H_x-mu_x I)xi_x=0
```

to construct, for each FAR3 row `k_t`, an explicit row vector `r_t` such that

```text
||k_t-r_t E_x|| <= C L^-5 / Pref_k(A,L).
```

This constructive form avoids positive `L1` ceilings and keeps the signed cancellation inside the
operator equation.

## 7. Remaining phase chain

The current sufficient chain is now:

```text
ROW-MAIN-5 + Tail_3<=C_tail L^-9
=> BUD-5/9
=> FAR3-nodewise
=> FAR3
=> FAR-DNS
=> ADNS
=> DNS
=> WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

This replaces `DEN-GAP-10` as the sharp arithmetic core for the main term.

E73.068--E73.069 fix the numerical gauge: `ROW-MAIN-5` is to be tested and proved with the exact
eigenline of `H_x`, not with a symmetrized proxy.
