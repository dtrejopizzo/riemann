# E72.18 -- Finite residue cobordism

**Date:** 2026-07-08.
**Role:** introduce a new finite identity that converts the maximal resonance block into a boundary
loss between the finite CCM real-zero divisor and the global `Xi` divisor.

## 0. Why this object is needed

E72.15-E72.17 show that the Abel-Chebyshev route cannot be closed by:

```text
PNT-size bounds,
absolute kernel estimates,
functional-equation pairing,
or real conjugation.
```

The only remaining non-circular source of cancellation is the finite CCM fact:

```text
the finite divisor has only real zeros.
```

So the new object must compare:

```text
finite real-zero residue current   vs.   global Xi residue current
```

without inserting the global zero set as input.

## 1. Finite residue current

Let `F_x` be the finite CCM entire/rational spectral function whose zeros are the intrinsic finite
divisor. In the Phase 71 notation this is the finite real-zero function obtained from the Weyl
`m`-function numerator, not the determinant of `QW_x`.

Let `G_x` be the prolate model spectral function, normalized in the same Cartwright gauge. Define the
relative finite residue current

```text
dM_x(s) := d log F_x(s) - d log G_x(s).
```

For a holomorphic vector test `Phi_x(s)` with values in a Hilbert space `H_x`, define

```text
Res_x(Phi)
 := (1/(2pi i)) int_{partial Omega} Phi_x(s)dM_x(s),
```

where `Omega` is any compact contour avoiding the real finite divisor and the model divisor.

Because all zeros of `F_x` and `G_x` are real in the working strip, if `Omega` is disjoint from the real
axis then

```text
Res_x(Phi)=0.                                      (FRC0)
```

This is the finite residue cobordism identity.

## 2. Global residue current

The global target current is

```text
dM(s) := d log Xi(s) - d log G(s),
```

where `G` is the Cartwright limit of the prolate model. For a contour enclosing a non-real zero block
`Z_beta`, Cauchy's theorem gives

```text
Res(Phi)
 := (1/(2pi i)) int_{partial Omega} Phi(s)dM(s)
  = sum_{rho in Z_beta} Phi(rho) mult(rho)
    - model residues inside Omega.                 (GRC)
```

If `Phi=R_x(s)/s` and the model term is subtracted by the same relative gauge as in E72.14, the global
residue is exactly the maximal resonance block:

```text
Res(R_x/s) = sum_{rho in Z_beta} R_x(rho)/rho
             + lower-order/model terms.            (RB)
```

Thus the desired null-vector identity is equivalent to proving that the finite identity `(FRC0)`
passes to the global current with no boundary loss.

## 3. The finite cobordism theorem

### Theorem 72.18

Let `Omega` be a compact contour in the strip, disjoint from the real axis. Assume:

1. `F_x` has only real zeros in the strip;
2. `G_x` has only real zeros in the strip;
3. `Phi_x` is holomorphic in a neighborhood of `Omega`;
4. the relative current convergence holds:

```text
int_{partial Omega} Phi_x(s)dM_x(s)
  - int_{partial Omega} Phi_x(s)dM(s) -> 0.        (RCC)
```

Then the global residue of `Phi_x` inside `Omega` vanishes asymptotically:

```text
(1/(2pi i))int_{partial Omega} Phi_x(s)dM(s) -> 0.
```

In particular, if `Phi_x(s)=R_x(s)/s` and the model residues are already subtracted, then

```text
sum_{rho in Omega} R_x(rho)/rho -> 0.
```

### Proof

By assumptions 1 and 2, neither `F_x` nor `G_x` has zeros inside `Omega`, since `Omega` is disjoint
from the real axis. Therefore `dM_x` is holomorphic inside `Omega`, and Cauchy's theorem gives

```text
int_{partial Omega} Phi_x(s)dM_x(s)=0.
```

Subtracting the convergence assumption `(RCC)` gives

```text
int_{partial Omega} Phi_x(s)dM(s)
 = int_{partial Omega} Phi_x(s)dM_x(s)+o(1)
 = o(1).
```

The residue statement follows from Cauchy's residue theorem. `QED`

## 4. The new theorem that would close the resonance block

The previous theorem reduces the missing identity to a precise no-boundary-loss statement:

### Relative Cartwright Current Convergence

For every off-real contour `Omega` and for the specific vector tests

```text
Phi_x(s)=R_x(s)/s,
```

one has

```text
int_{partial Omega} Phi_x(s)
  d log(F_x/G_x)(s)
 -
int_{partial Omega} Phi_x(s)
  d log(Xi/G)(s)
 -> 0.                                           (RCCC)
```

This is not an estimate on primes by absolute value. It is a residue-current convergence theorem in a
Cartwright/de Branges gauge.

## 5. Why this is new relative to the earlier walls

The Phase 70 Abel wall tried to pass positivity to the boundary:

```text
positive forms in an Euler region -> critical form.
```

That loses exactly at off-line resonances.

The finite residue cobordism route instead uses:

```text
finite real-zero divisor -> zero off-real residue current
```

and asks for convergence of relative currents against the specific resonance tests. This is a different
object. It does not ask for Weil positivity. It asks that the finite CCM real-zero current be a
Cartwright-current approximation to the global relative current.

## 6. Non-circularity gate

`RCCC` is admissible only if it is proved from:

```text
finite CCM Weyl data,
the prolate model gauge,
Cartwright growth bounds,
and real-axis/current convergence of the finite construction.
```

It is not admissible if it uses:

```text
zero locations of Xi,
the sign of the Weil form,
or ACD itself.
```

## 7. Status

```text
proved: finite off-real residue current is zero;
proved: relative current convergence implies maximal-resonance cancellation;
open:   prove RCCC from finite CCM/prolate Cartwright control.
```

The next move is to prove a Cartwright compactness theorem strong enough to give `RCCC` from real-axis
finite CCM convergence, rather than from RH.
