# E101.008 - Euler duality of the covariant current

## 1. Euler functional

Let

```text
A=Z^(-1)[X,Z],
H_P=A+A^*.                                           (1.1)
```

For a finite-rank covector `S`, define

```text
Euler_Z(S)=Tr[S(A+A^*)].                             (1.2)
```

E97.002 gives

```text
Euler_Z(S)
 =Tr([Z,S]Z^(-1)X)
  +Tr((Z^*)^(-1)[S,Z^*]X).                           (1.3)
```

## 2. Primal-dual identity

Let `T_z` and `S_z=Cot_K(T_z)` be as in E101.007.  Then

```text
Tr[T_z Hor_K(H_P)]
 =Tr(S_zH_P)
 =Euler_Z(S_z).                                      (2.1)
```

### Proof

The first equality is E101.007(2.2).  The second is the definition (1.2).
`QED`

Thus the horizontal bordered current of E101.002 and the Euler commutator
current of Phases 97--99 are identical before any limit.

## 3. Location of the level correction

The two coordinates distribute the same correction differently:

```text
Hor_K(H_P)=H_P+Tr(GH_P)I,                            (3.1)

Cot_K(T_z)=T_z+Tr(T_z)G.                             (3.2)
```

In the primal coordinate it is the scalar shift in (3.1).  In the dual
coordinate its commutator is

```text
[Z,Cot_K(T_z)]
 =[Z,T_z]+Tr(T_z)[Z,G].                              (3.3)
```

Equation (3.3) is the bordered source plus the normalized characteristic
commutator of Phase 99.  E100.004 identifies the second summand with the
moving-level factor.  Neither coordinate creates an additional term.

## 4. Boundary representation

Apply the adjugate sandwich identity to `[Z,T_z]`, the signed-projection
identity to `[Z,G]`, and the shell split of E98.002.  Equation (1.3) then gives
exactly

```text
covariant bordered source sandwich
 + Fourier shell.                                    (4.1)
```

Therefore the boundary representation is already complete.  What remains is
the signed cofinal evaluation of (4.1) against the independent Euler current.

## 5. Status

```text
proved:
  exact primal-dual Euler identity;
  exact transfer of the level correction between the two coordinates;
  compatibility with the adjugate boundary and shell decomposition.
```

