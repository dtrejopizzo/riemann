# E95.003 - Bilateral projective Jacobian

## 1. Projective current

Fix a safe base point `z_*` and define

```text
W_t(z,z_*)
 =P(t,mu_t,z)/P(t,mu_t,z_*).                          (1.1)
```

E95.002 gives

```text
partial_t log W_t(z,z_*)
 =K_t(z)-K_t(z_*),                                   (1.2)

K_t(z)
 =Jac(P,chi)(t,mu_t,z)
  /[P(t,mu_t,z)partial_mu chi(t,mu_t)].               (1.3)
```

The factor `partial_mu chi` is independent of `z`; it is retained inside
each term but introduces no projective normalization ambiguity.

## 2. Bilateral safe current

Put `u=s-1/2` and define

```text
BJ_t(s;s_*)
 =K_t(iu)+K_t(-iu)-K_t(iu_*)-K_t(-iu_*).             (2.1)
```

Then

```text
BJ_t(s;s_*)
 =partial_t log
  {[P(t,mu_t,iu)P(t,mu_t,-iu)]
   /[P(t,mu_t,iu_*)P(t,mu_t,-iu_*)]}.                (2.2)
```

## 3. Euler comparison

The independent product deformation has projective current

```text
EJ_L(s;s_*)=J_L(s)-J_L(s_*).                         (3.1)
```

Therefore the exact arithmetic deformation defect is

```text
AJ_t(s;s_*)=BJ_t(s;s_*)-EJ_L(s;s_*).                 (3.2)
```

No zero list or critical-line value occurs in (3.2).

## 4. Status

```text
proved:
  exact bilateral characteristic Jacobian;
  exact projective comparison with the Euler current;

open:
  signed integration and cofinal control of AJ_t.
```

