# E95.002 - Characteristic Jacobian tangent theorem

## 1. Level derivative

Differentiate `chi(t,mu_t)=0` at a simple point:

```text
dot mu_t
 =-[partial_t chi(t,mu_t)]/[partial_mu chi(t,mu_t)].  (1.1)
```

This is the determinant form of the level velocity.

## 2. Bordered derivative

Define the characteristic Jacobian

```text
Jac(P,chi)
 =(partial_t P)(partial_mu chi)
  -(partial_mu P)(partial_t chi).                     (2.1)
```

### Theorem 2.1

Along every simple characteristic branch and at every point where `P` is
nonzero,

```text
d/dt log P(t,mu_t,z)
 =Jac(P,chi)(t,mu_t,z)
  /[P(t,mu_t,z)partial_mu chi(t,mu_t)].               (2.2)
```

### Proof

The chain rule gives

```text
d/dt P(t,mu_t,z)
 =partial_t P+dot mu_t partial_mu P.                  (2.3)
```

Insert (1.1), put the two terms over the common denominator
`partial_mu chi`, and divide by `P`. `QED`

## 3. Cofactor nature

Every partial derivative in (2.1) is a sum of cofactors.  Thus (2.2) is an
inverse-free rational expression in finite Gamma--prime matrix entries.  It
contains neither `dot mu_t` nor an eigenvector.

## 4. Status

```text
proved:
  exact determinant formula for the moving level;
  exact characteristic Jacobian current.
```

