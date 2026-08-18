# E83.002 - Gamma--Euler intertwiner criterion

## 1. Abstract data

Let `C_N=Q_NM_NQ_N` be the CCM complement from E82.005.  Let
`J_N` map the finite Euler module into `ran Q_N`.  Let `Z_N` be a finite or
Abel-regularized Euler unit and let `delta_N` be the scale derivation.

Fix a model vector `k_N` and put

```text
w_N=(Z_N-I)k_N,
u_N=J_N Z_N^(-1)w_N.                                  (1.1)
```

The vector `u_N` is constructed without `C_N^{-1}`.

## 2. One-vector intertwining defect

Define

```text
d_N
 = C_N J_N Z_N^(-1)w_N
   -J_N Z_N^(-1)delta_N w_N.                          (2.1)
```

Assume the projected coupled source has the exact decomposition

```text
Q_N f_N
 = J_N A_N k_N+r_N^src,                               (2.2)
```

where `A_N=Z_N^{-1}delta_N Z_N` and `delta_N k_N=0` in the model module.

### Theorem 2.1

Under (2.1)--(2.2),

```text
Q_N f_N=C_N u_N+e_N,                                  (2.3)

e_N=r_N^src-d_N.                                      (2.4)
```

Consequently, if for every safe compact `K`,

```text
sup_{z in K}|ell_{N,z}(C_N^(-1)e_N)| -> 0             (2.5)
```

and likewise after one safe derivative, then `u_N` proves the two-generator
arithmetic coboundary of E82.005.

### Proof

By E83.001 and `delta_N k_N=0`,

```text
A_N k_N=Z_N^(-1)delta_N w_N.                           (2.6)
```

Equation (2.1) gives

```text
J_N A_N k_N=C_Nu_N-d_N.
```

Insert this in (2.2) to obtain (2.3)--(2.4).  Estimate (2.5) is exactly the
criterion of E82.005. `QED`

## 3. Smallest live clauses

The theorem separates the required new mathematics into three clauses:

```text
GE-1  SOURCE REPRESENTATION:
      prove (2.2) from the finite Gamma-prime cell formula;

GE-2  ONE-VECTOR INTERTWINING:
      construct J_N and control d_N in the safe reduced topology;

GE-3  REDUCED DEFECT:
      prove (2.5) for r_N^src-d_N without defining a corrector by inversion.
                                                                    (3.1)
```

`GE-1`--`GE-3` imply the arithmetic coboundary and hence enter the proved
chain to RDI-ANCHOR.

## 4. Status

```text
proved:
  the exact intertwiner criterion;

reduced:
  TWO-GENERATOR-ARITHMETIC-COBOUNDARY to GE-1--GE-3;

open:
  construction of J_N;
  GE-1, GE-2 and GE-3;

next:
  prove that Euler algebra alone cannot supply GE-2, thereby locating the
  precise Gamma compatibility that must be added.
```

