# E101.047 - Range cancellation and tail recombination

## 1. Bilinear finite section

Let `Q` be a bilinear distribution, let `{phi_i}` be the selected row tests,
and let `{psi_j}` be the selected column tests.  Define

```text
(R_N Q f)_i=Q(f,phi_i),
J_N v=sum_j v_j psi_j,
M_N=R_N Q J_N.                                      (1.1)
```

Thus `M_N` is the rectangular matrix of the same distribution in the chosen
row and column families.  Let `ell_N`, `y_N`, `c_z`, `B_(y_N)(z)` and the
dual row `p_(N,z)` be as in E101.046.  Put

```text
q_(N,z)=c_z-B_(y_N)(z)ell_N.                        (1.2)
```

The dual equation is

```text
p_(N,z)M_N=q_(N,z).                                 (1.3)
```

## 2. Exact cancellation on the finite source range

### Theorem 2.1 - Range cancellation

For every finite coefficient vector `v`,

```text
p_(N,z)R_N Q J_N v=q_(N,z)v.                       (2.1)
```

Consequently an arbitrarily large dual response on the full row space does
not amplify residuals which remain in the represented source range.  On
that range it is exactly the elementary functional

```text
q_(N,z)v=c_zv-B_(y_N)(z)ell_Nv.                    (2.2)
```

### Proof

Substitute (1.1) into the left side of (2.1) and use (1.3). `QED`

This identity is invariant under every equation-row preconditioning by
E101.046(6.3).

## 3. Source projection and the only amplified remainder

Let `P_N` be a coefficient extraction satisfying

```text
P_NJ_N=I                                             (3.1)
```

on the finite coefficient space.  Every source `f` has the exact split

```text
f=J_NP_Nf+u_N(f),
u_N(f)=(I-J_NP_N)f.                                 (3.2)
```

Applying `R_NQ` and then the dual row gives

```text
p_(N,z)R_NQf
=q_(N,z)P_Nf+p_(N,z)R_NQ u_N(f).                   (3.3)
```

The first term contains no inverse and no bordered amplification.  All such
amplification has been confined to the out-of-band source tail `u_N(f)`.

### Corollary 3.1

Suppose `K` is a safe compact set and

```text
sup_N sup_(z in K)|B_(y_N)(z)|<infinity.            (3.4)
```

Then

```text
sup_(z in K)|q_(N,z)P_Nf|
<=C_K ||P_Nf||_1,                                   (3.5)
```

where

```text
C_K=sup_(N,z in K,j)|z/(z-d_j)|
    +sup_(N,z in K)|B_(y_N)(z)|.                   (3.6)
```

For a safe axis separated from the real mesh, `C_K` is finite.  Hence
`||P_Nf||_1->0` closes the represented part of the directional tail.

### Proof

Use (2.2), `|ell_Nv|<=||v||_1`, and

```text
|c_zv|<=sup_j|z/(z-d_j)| ||v||_1.                  (3.7)
```

This proves (3.5). `QED`

## 4. Application to the PROLATE residual

Set

```text
f_lambda=k_lambda-k.                                (4.1)
```

The PROLATE row residual of P76.063 and E80.008 is

```text
t^P_(L,N)=R_N Q_W f_lambda.                         (4.2)
```

Equation (3.3) gives the exact recombination

```text
p_(N,z)t^P_(L,N)
=q_(N,z)P_Nf_lambda
 +p_(N,z)R_NQ_W u_N(f_lambda).                     (4.3)
```

The first term is `PROLATE-INBAND`.  The physical localization estimates
and repeated Fourier integration of P76.065 motivate a rapidly decreasing
coefficient topology.  The precise cofinal statement still required here is

```text
||P_Nf_lambda||_1->0,                               (4.4)
```

Under (4.4), Corollary 3.1 closes `PROLATE-INBAND`.  This is an explicit
source-space condition and is not inferred merely from pointwise physical
decay.

The second term in (4.3) is not a new physical-tail obligation.  It is the
Fourier collar of the prolate difference and belongs to the same shell
module as `E_(FOURIER,N)`.  Therefore the previous split

```text
DS-1  RDP-SHELL;
DS-2  unrestricted directional continuity for PROLATE              (4.5)
```

can be sharpened to

```text
DS-1' RDP-SHELL for the recombined Fourier collar;
DS-2' l1 source convergence (4.4) plus the LP bound (3.4).          (4.6)
```

The difficult dual response occurs only in `DS-1'`; it is no longer applied
to the in-band prolate error.

## 5. WEIL-TAIL range-transfer criterion

Let

```text
t^W_(L,N)=R_N(Q_(W,L)-Q_W)k.                       (5.1)
```

If one can construct a coefficient vector `h_(L,N)` and a row remainder
`r_(L,N)` such that

```text
t^W_(L,N)=M_N h_(L,N)+r_(L,N),                     (5.2)
```

then Theorem 2.1 gives

```text
p_(N,z)t^W_(L,N)
=q_(N,z)h_(L,N)+p_(N,z)r_(L,N).                    (5.3)
```

This suggests the strictly smaller replacement for unrestricted
directional continuity:

```text
WEIL-RANGE-TRANSFER:
  choose (5.2) so that
  sup_(z in K)|q_(N,z)h_(L,N)|->0,
  while r_(L,N) is a summable shell residual.       (5.4)
```

The construction of `h_(L,N)` must use the coupled Gamma-prime truncation.
Choosing it through an arbitrary right inverse of `M_N` would merely rename
the original problem and is not admissible.

## 6. Revised radical-tail cut

Combining (4.3) and (5.3), the complete paired residual becomes

```text
p_(N,z)(t^P+t^W+t^F)
=q_(N,z)[P_N(k_lambda-k)+h_(L,N)]
 +p_(N,z)[
      R_NQ_Wu_N(k_lambda-k)+r_(L,N)+t^F].           (6.1)
```

The first bracket is a direct source observation.  The second bracket is a
single recombined shell residual.  This is the correct place to apply the
rank-two displacement law; applying it separately to the original three
terms destroys cancellations.

E101.048 supplies the construction in `RT-1` by a shifted endpoint
coboundary.  The directional tail front is consequently reduced to:

```text
RT-0  prove the cofinal l1 source convergence (4.4);
RT-2  prove RDP-SHELL for the single recombined collar in (6.1);
RT-3  prove the shifted safe leakage isolated in E101.048.          (6.2)
```

## 7. Attribution

Range cancellation is pure finite algebra and holds for both zeta and
planted blocks.  The arithmetic discriminator cannot lie in Theorem 2.1.
E101.048 shows that the `RT-1` construction is also exact finite algebra.
The discriminator can enter only through the cofinal direct source and
shifted-leakage limits in (6.1).

This agrees with E101.045: LP and displacement propagation supply the
stable transport, while IDENT must identify the transported arithmetic
source.

## 8. Status

```text
proved:
  exact cancellation of the dual Green row on the represented source range;
  confinement of bordered amplification to the out-of-band source tail;
  direct l1 estimate for the in-band term;
  exact recombination formula (6.1);

reduced:
  PROLATE-INBAND to the explicit l1 convergence (4.4);
  the former PROLATE directional-continuity module to the Fourier collar;
  the WEIL directional-continuity module to WEIL-RANGE-TRANSFER;

open:
  cofinal verification of (4.4);
  RT-2, the recombined shell estimate.

closed in E101.048:
  construction half of WEIL-RANGE-TRANSFER;

transferred to E101.048:
  its shifted safe-leakage estimate.
```
