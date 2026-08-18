# E100.001 - Normalized characteristic adjugate

## 1. Simple level

Let

```text
K=H_t-mu_t I                                         (1.1)
```

be real symmetric with a simple zero eigenvalue.  Let `Pi_t` be the
orthogonal projection onto `ker K` and let the nonzero eigenvalues of `K` be
`lambda_2,...,lambda_m`.

Then

```text
adj(K)=(product_(j=2)^m lambda_j)Pi_t.                (1.2)
```

### Proof

Diagonalize `K` orthogonally.  The adjugate of
`diag(0,lambda_2,...,lambda_m)` has only its first diagonal entry nonzero,
equal to the product of the remaining eigenvalues.  Conjugation back gives
(1.2). `QED`

## 2. Characteristic normalization

For

```text
chi(t,mu)=det(H_t-mu I),                              (2.1)
```

differentiation in `mu` gives

```text
partial_mu chi(t,mu_t)
 =-product_(j=2)^m lambda_j.                         (2.2)
```

Therefore

```text
G_t
 =adj(K)/partial_mu chi(t,mu_t)
 =-Pi_t.                                             (2.3)
```

In particular, `Tr G_t=-1`.

## 3. Status

```text
proved:
  exact signed-projection identity for the normalized characteristic
  adjugate.
```

