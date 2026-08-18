# E89.002 - Cancellation of scalar resonance factors

## 1. Exact factorization

The dominant residue is

```text
a_t(z)=c_t phi_t(z),                                  (1.1)

c_t=p_t^T b_t^eff,
phi_t(z)=h_(t,z)^eff p_t.                             (1.2)
```

Both `c_t` and `lambda_t` are independent of the safe variable `z`.

### Theorem 1.1

Under the dominance hypotheses of E89.001,

```text
G_t(z)/G_t(z_*)
 ->phi_t(z)/phi_t(z_*),                               (1.3)

partial_z log G_t(z)
 ->partial_z log phi_t(z).                            (1.4)
```

No asymptotic estimate of `lambda_t` or `c_t` is needed beyond nonvanishing of
the dominant product.

### Proof

E89.001 replaces the normalized numerator by `a_t(z)/a_t(z_*)`.  Substitute
(1.1); `c_t` cancels.  Differentiation also removes both scalar factors.
`QED`

## 2. Consequence for the cascade

The following data are normalization only:

```text
rate of eigenvalue collapse;
rate of the boundary overlap;
absolute size of the resonant solution.                (2.1)
```

They matter for proving dominance, but they cannot themselves identify the
Euler--Gamma target.  The projective content is entirely the transported
resonant Cauchy profile `phi_t`.

This explains why ambient inverse estimates and bottom-coupling lower bounds
repeatedly detect a huge scale without closing RDI.

## 3. Status

```text
proved:
  exact cancellation of the eigenvalue and boundary-overlap scales in the
  projective layer;

localized:
  the endpoint arithmetic current to the rotation of phi_t.
```
