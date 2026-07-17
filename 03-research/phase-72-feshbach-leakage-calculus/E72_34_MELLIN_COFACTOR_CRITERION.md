# E72.34 -- Mellin cofactor criterion for finite spectral divisibility

**Date:** 2026-07-08.
**Role:** turn the open divisibility statement

```text
M_x(s;z)=P_x(z)A_x(s;z)+E_x(s;z)
```

into an exact finite cofactor condition for the bordered CCM pencil. This is the next object to prove,
not another asymptotic slogan.

## 0. Mellin cell operator

For the scalar WRL kernel from E72.31, define the Mellin cell operator

```text
Tcal_x(z) := z int_1^x u^{z-1} T_{x,u}du,
```

with the finite/interpolated cell convention of E72.14. Then

```text
M_x(s;z)
 := z int_1^x u^{z-1}L_x(s;u)du
  = <v_{x,s}, Tcal_x(z)k_x>
    - <k_x,Tcal_x(z)k_x><v_{x,s},k_x>.          (M0)
```

In the compressed gauge `v_{x,s}=Q_xv_{x,s}`, the second term vanishes:

```text
M_x(s;z)=<v_{x,s},Tcal_x(z)k_x>.                (M1)
```

## 1. Bordered pencil and finite divisor

Recall the bordered pencil:

```text
B_x(z)= [ 0        xi_x^T ]
        [ 1_x      zI-D_x ],

P_x(z)=-det B_x(z).
```

The finite divisor is `P_x(z)=0`.

The divisibility target is:

```text
M_x(s;z)/P_x(z) is holomorphic in z.             (DIV)
```

## 2. Cofactor criterion

### Theorem 72.34

Assume `P_x` has simple zeros in the compact region under consideration. Then `(DIV)` is equivalent to:

```text
M_x(s;r)=0        for every r with P_x(r)=0.      (VZ)
```

Equivalently, if `c_x(r)` is any nonzero right null vector of `B_x(r)` and `d_x(r)` any nonzero left
null vector, then the residue of `M_x/P_x` at `r` is

```text
Res_{z=r} M_x(s;z)/P_x(z)
 = M_x(s;r) / P_x'(r),
```

and divisibility is exactly vanishing of all these cofactor residues.

### Proof

Since `P_x` is a polynomial with simple zeros, `M_x/P_x` is meromorphic with at most simple poles at
the finite divisor. A simple pole at `r` has residue `M_x(s;r)/P_x'(r)`. Therefore the quotient is
holomorphic iff all residues vanish, iff `M_x(s;r)=0` at every zero. `QED`

## 3. Zero-free cofactor form

The previous criterion still mentions roots. To avoid using them as input, use the adjugate identity:

```text
B_x(z) adj(B_x(z)) = det(B_x(z)) I = -P_x(z)I.
```

At a simple zero `r`, `adj(B_x(r))` is rank one and equals, up to a scalar,

```text
c_x(r)d_x(r)^T.
```

Thus a root-free way to prove `(VZ)` is to find holomorphic bordered vectors/functions

```text
a_x(s;z), b_x(s;z), c_x(s;z)
```

such that

```text
B_x(z)b_x(s;z)=P_x(z)c_x(s;z),                  (C1)
M_x(s;z)=a_x(s;z)^T B_x(z)b_x(s;z).             (C2)
```

Then

```text
M_x(s;z)=P_x(z)a_x(s;z)^Tc_x(s;z),
```

so `P_x` divides `M_x`.

Equivalently, it is enough to construct a holomorphic vector `b_x` whose image under `B_x` has an
explicit factor `P_x`, while the scalar Mellin current is obtained by pairing this image with
`a_x`.

The symmetric left version is also valid:

```text
a_x(s;z)^TB_x(z)=P_x(z)c_x(s;z)^T,
M_x(s;z)=a_x(s;z)^TB_x(z)b_x(s;z).
```

This corrects a tempting but false shortcut: an arbitrary scalar of the form `a^TBb` does **not**
vanish when `B` is singular. One needs the stronger factorized image condition `(C1)`.

## 4. What `(CF)` means for the scalar kernel

Using `(M1)`, the identity says:

```text
<v_{x,s},Tcal_x(z)k_x>
 = a_x(s;z)^TB_x(z)b_x(s;z),
B_x(z)b_x(s;z)=P_x(z)c_x(s;z).                  (CF-M)
```

This is the exact finite algebraic form of the desired new mathematics.

It must be proved by expanding:

```text
Tcal_x(z),
v_{x,s}=C_x^(-1)Q_x(sI-D_x)^(-1)1_x,
B_x(z).
```

No zeta zeros, no limiting divisor, and no sign of the Weil form may enter.

## 5. Why this is sharper than E72.33

E72.33 said "prove divisibility." E72.34 gives the finite identity that would prove it without
evaluating roots:

```text
M_x = a_x^T B_x b_x,   with   B_x b_x=P_x c_x.
```

This is now a concrete algebraic target. If it holds, scalar WRL annihilation follows by E72.33 and the
Phase 72 current chain. If it fails, the scalar WRL route has no remaining non-circular mechanism.

## 6. Status

```text
proved: divisibility by P_x is equivalent to vanishing of finite cofactor residues;
proved: a factorized B_x-coboundary identity (CF-M) is a root-free sufficient condition;
open:   construct a_x,b_x,c_x satisfying (CF-M) from the explicit finite CCM data.
```

The next step is to try to construct `(CF-M)` by solving the bordered cohomological equation.
