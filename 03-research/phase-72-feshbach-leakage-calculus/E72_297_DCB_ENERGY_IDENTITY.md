# E72.297 -- Energy identity for the directional commutator bound

**Purpose.** Give the exact spectral form of the new DCB target. This avoids expanding the commutator
into prime cells before using the fact that `xi` is the actual ground vector.

## 1. Exact eigenvector identity

In the pole-even complement,

```text
C_E = B_even^T(H_actual-e_pole I)B_even.
```

Let `xi` be the lowest actual even vector in this complement and let

```text
C_E xi = mu xi.
```

Then, for every finite root parameter `tau`,

```text
[C_E,S_tau]xi
= C_E S_tau xi - S_tau C_E xi
= (C_E-mu I)S_tau xi.                                  (1)
```

Thus DCB is not a global upper-complement statement. It is an energy estimate for the single vector
`S_tau xi` above the ground state.

## 2. Spectral form

Let `{phi_r}` be an orthonormal eigenbasis of `C_E`, with

```text
C_E phi_r = mu_r phi_r,       mu_0=mu,       phi_0=xi.
```

Then

```text
||[C_E,S_tau]xi||^2
= sum_{r>=1} (mu_r-mu)^2 |<phi_r,S_tau xi>|^2.          (2)
```

The `r=0` component vanishes automatically. Therefore the commutator bound is a second spectral
moment of `S_tau xi` away from the ground mode.

## 3. Quadratic-energy sufficient condition

If the following two directional energy estimates hold:

```text
E1(H):  <S_tau xi,(C_E-mu I)S_tau xi> = O_H(L^p),
E2(H):  ||(C_E-mu I) restricted to supp(S_tau xi)_eff|| = O_H(L^q),
```

then

```text
||[C_E,S_tau]xi||^2 <= O_H(L^(p+q)).
```

Hence DCB holds with

```text
alpha=(p+q)/2.
```

The compact-root HPAC proof needs only `alpha<7/2`, i.e.

```text
p+q<7.
```

This is much weaker than a global `||C_E||=O(L^2)` theorem, because `E2` is only required on the
effective spectral support of `S_tau xi`.

## 4. Form identity for E1

Using (1),

```text
<S_tau xi,(C_E-mu I)S_tau xi>
= <S_tau xi,C_E S_tau xi> - mu ||S_tau xi||^2.          (3)
```

The second term is controlled by GAP and VBG:

```text
mu ||S_tau xi||^2 = O_H(L^2) O_H(L^2)=O_H(L^4).
```

Thus the natural target is

```text
<S_tau xi,C_E S_tau xi> = O_H(L^4).
```

If this is proved, then `p=4`. It remains to show that the effective spectral support of `S_tau xi`
has `q<3`; the ideal target is `q=2`, which gives

```text
alpha=3 < 7/2.
```

## 5. New compact-root sufficient package

The compact-root theorem is now reduced to:

```text
GAP:        mu >= cL^2,
VBG:        ||S_tau xi||=O_H(L),
FORM-DCB:   <S_tau xi,C_E S_tau xi>=O_H(L^4),
EFF-SUP:    effective C_E support of S_tau xi is O_H(L^2).
```

Together these imply

```text
||[C_E,S_tau]xi||=O_H(L^3),
```

which is enough for fixed-height HPAC decay.

## 6. Why this is the right replacement

E72.295 shows that high Fourier modes make the global positive part of `Delta_arith` too large.
Equation (2) shows why those modes should not be controlled globally: only their overlap with
`S_tau xi` matters. The next proof should therefore establish `FORM-DCB` and `EFF-SUP`, not APCB.

## 7. E72.298 refinement

E72.298 gives the exact double-commutator identity

```text
<S_tau xi,(C_E-mu I)S_tau xi>
= (1/2)<xi,[S_tau,[C_E,S_tau]]xi>
= -1/2 sum_{m,n} xi_m xi_n (s_m-s_n)^2 C_E(m,n).
```

This removes all diagonal terms and the scalar pole shift. It also gives the direct square target

```text
||[C_E,S_tau]xi||^2
= sum_m |sum_n C_E(m,n)(s_n-s_m)xi_n|^2 <= C_H L^6.
```

If this `DCB-square` inequality is proved, DCB follows with `alpha=3`, and the separate effective
support statement is no longer needed.
