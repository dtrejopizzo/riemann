# E99.001 - Constrained determinant sensitivity

## 1. Formula on a simple characteristic branch

Let

```text
B_z=[[M,b],[h_z,1]],
K=H_t-mu I.                                          (1.1)
```

Assume `det B_z` is nonzero and `mu` is a simple characteristic level.  Thus

```text
det K=0,
partial_mu chi !=0.                                  (1.2)
```

A full matrix direction `Y` induces a bordered direction `widehat Y_z`.  The
constrained response of E97.001 is

```text
R_z(Y)
 =Tr(adj(B_z)widehat Y_z)/det B_z
  -gamma_z Tr(GY),                                   (1.3)

gamma_z=partial_mu P/P,
G=adj(K)/partial_mu chi.                             (1.4)
```

### Proof

Use the cofactor derivative formulas

```text
delta_Y P=Tr(adj(B_z)widehat Y_z),
delta_Y chi=Tr(adj(K)Y)                              (1.5)
```

in E97.001(1.2). `QED`

## 2. Normalization

Because `partial_mu K=-I`,

```text
partial_mu chi=-Tr(adj K),
Tr G=-1.                                             (2.1)
```

Thus `G` is the signed cofactor projector of the simple characteristic line.
It is defined without choosing an eigenvector normalization.

## 3. Status

```text
proved:
  exact constrained sensitivity on the singular characteristic curve;
  normalized cofactor projector formula;

forbidden:
  K^(-1) on det K=0.
```
