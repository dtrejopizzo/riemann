# E101.007 - Dual cotangent projection

## 1. Raw bordered covector

Let `beta_z` be the border restriction of E101.002.  Define its trace adjoint
by the identity

```text
Tr(T_zY)
 =Tr[adj(B_z)beta_z(Y)]/P(t,mu_t,z)                  (1.1)
```

for every full matrix direction `Y`.  Thus `T_z` is the pullback of the raw
bordered cofactor sensitivity.

Since `beta_z(I)=J`,

```text
Tr T_z
 =Tr[adj(B_z)J]/P
 =-gamma_t(z).                                       (1.2)
```

## 2. Cotangent projection

For every matrix covector `T`, define

```text
Cot_K(T)=T+Tr(T)G,                                   (2.1)
```

where `G=adj(K)/chi_mu` and `Tr G=-1`.

### Theorem 2.1

The map `Cot_K` is the trace-pairing adjoint of `Hor_K`:

```text
Tr[T Hor_K(Y)]=Tr[Cot_K(T)Y].                        (2.2)
```

It is a projection with

```text
range Cot_K={S:Tr S=0},
kernel Cot_K=span{G}.                                (2.3)
```

### Proof

Using E101.001,

```text
Tr[T Hor_K(Y)]
 =Tr(TY)+Tr(T)Tr(GY)
 =Tr[(T+Tr(T)G)Y],                                  (2.4)
```

which proves (2.2).  Also

```text
Tr Cot_K(T)=Tr(T)+Tr(T)Tr(G)=0.                      (2.5)
```

Consequently `Cot_K(Cot_K(T))=Cot_K(T)`.  Moreover `Cot_K(G)=0`, and if
`Cot_K(T)=0`, then `T=-Tr(T)G`.  This proves (2.3). `QED`

## 3. Constrained sensitivity recovered

Apply (2.1) to `T_z`.  By (1.2),

```text
S_z=Cot_K(T_z)=T_z-gamma_t(z)G.                      (3.1)
```

This is exactly the characteristic-constrained sensitivity of E97.001.  In
particular,

```text
Tr S_z=0,
R_z(I)=0.                                            (3.2)
```

The physical response can be written in either of the equal forms

```text
R_z(Y)
 =Tr[T_z Hor_K(Y)]
 =Tr(S_zY).                                          (3.3)
```

## 4. Status

```text
proved:
  dual cotangent projection;
  trace-free constrained sensitivity;
  exact equivalence of primal horizontal and dual constrained coordinates.
```

