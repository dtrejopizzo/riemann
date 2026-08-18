# E100.003 - Euler trace and level velocity

## 1. Determinant velocity

Along `chi(t,mu_t)=0`, E95.002 gives

```text
dot mu_t
 =-[partial_t chi]/[partial_mu chi].                 (1.1)
```

Since `partial_t H_t=-H_P`,

```text
partial_t chi
 =-Tr[adj(K)H_P].                                    (1.2)
```

Substitution yields

```text
dot mu_t=Tr(G_t H_P).                                (1.3)
```

Using `G_t=-Pi_t`, equation (1.3) is the determinant form of

```text
dot mu_t=-Tr(Pi_tH_P).                               (1.4)
```

## 2. Euler commutator form

E97.002 applied to `K=G_t` gives

```text
dot mu_t
 =Tr([Z,G_t]Z^(-1)X)
  +Tr((Z^*)^(-1)[G_t,Z^*]X).                         (2.1)
```

Hence the normalized characteristic-adjugate commutator is exactly the level
velocity.

## 3. Status

```text
proved:
  equality of determinant velocity, signed projection expectation and Euler
  commutator trace.
```

