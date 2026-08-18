# E101.006 - Boundary-coordinate decision

## 1. What the horizontal lift removes

The covariant current contains no separate occurrence of

```text
partial_mu P;
Gamma_t dot mu_t;
[Z,G_t];
the characteristic scale chi_mu;
a reduced characteristic inverse.                   (1.1)
```

All these quantities are absorbed into the tangent direction
`Hor_(K_t)(H_P)`.

## 2. What it does not remove

The identity

```text
[Z,Hor_K(Y)]=[Z,Y]                                   (2.1)
```

holds because the horizontal correction is scalar.  Therefore the correction
does not create a new Euler boundary source.  Nevertheless, its bordered
cofactor pairing does not vanish:

```text
Tr[adj(B_z)beta_z(Hor_K(Y))]
 =Tr[adj(B_z)beta_z(Y)]
  +Tr(GY)Tr[adj(B_z)J].                              (2.2)
```

Consequently, discarding the scalar correction after passing to commutator
coordinates would discard the moving-level chain rule.  Equation (2.2) must
be kept before or after the boundary conversion.

## 3. Force-bearing remainder

The exact remaining theorem is now one signed pairing:

```text
horizontal bordered cofactor current
 + Fourier shell
 - independent Euler current.                       (3.1)
```

Its cofinal cancellation is equivalent to `DIRECT-BORDERED-ANCHOR`; the
horizontal factorization is a coordinate simplification, not a proof of that
anchor.

## 4. Decision

Phases 97--99 already give an exact finite Euler-commutator and boundary-source
representation of (3.1).  Therefore the unresolved task is not the existence
of a divergence coordinate.  It is the signed evaluation of that coordinate
after the horizontal correction, the bordered row and column, and the Fourier
shell have been kept together.

The correct next analysis must act on this full scalar pairing.  Separate
estimates for the fixed-level current and the level correction are not
invariant and are not required.

## 5. Status

```text
closed:
  identification of the covariant tangent direction;
  removal of the characteristic commutator as an independent source;
  reconciliation with the existing Euler boundary representation;

open:
  signed cofinal evaluation of the complete horizontal boundary pairing;
  signed cofinal cancellation and Omega7.
```
