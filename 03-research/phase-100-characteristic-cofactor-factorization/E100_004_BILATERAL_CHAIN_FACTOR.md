# E100.004 - Bilateral moving-level factor

## 1. Safe scalar

Let

```text
gamma_t(z)
 =partial_mu log P(t,mu_t,z).                         (1.1)
```

Define its bilateral base-point combination

```text
Gamma_t(s;s_*)
 =gamma_t(iu)+gamma_t(-iu)
  -gamma_t(iu_*)-gamma_t(-iu_*).                     (1.2)
```

## 2. Factorization

The characteristic part of the bilateral constrained current is exactly

```text
CHAR_t(s;s_*)=Gamma_t(s;s_*) dot mu_t.                (2.1)
```

### Proof

The characteristic component of the sensitivity is `-gamma_t(z)G_t`.
The deformation current has the sign `-Tr(SH_P)`.  Hence its contribution at
`z` is

```text
gamma_t(z)Tr(G_tH_P)=gamma_t(z)dot mu_t              (2.2)
```

by E100.003.  Form the bilateral base-point combination. `QED`

## 3. Meaning

Equation (2.1) is precisely the `dot mu_t partial_mu log P` part of the chain
rule for `P(t,mu_t,z)`.  It is not an independent endpoint anomaly.

## 4. Status

```text
proved:
  exact scalar factorization of the characteristic constraint.
```

