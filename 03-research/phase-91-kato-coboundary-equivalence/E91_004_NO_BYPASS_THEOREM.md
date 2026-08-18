# E91.004 - No-bypass theorem for the Kato current

## 1. Statement

Assume the simple-line and nonvanishing hypotheses of E90--E91.  Any proof of
the projective line-current identity by an explicit vector formula has the
form

```text
Q_tH_P^inv_t=C_tu_t+e_t,                             (1.1)

J_t=L_t(u_t)+L_t(C_t^(-1)e_t).                       (1.2)
```

Conversely, every decomposition (1.1) gives the exact current formula (1.2).
Therefore an explicit integration of the Kato current is neither weaker nor
stronger than a line-source coboundary together with safe reduced leakage.

## 2. Euler candidate

The finite Euler unit supplies an algebraic candidate for the `A` part of
`H_P=A+A^*`, but E91.003 shows that it necessarily carries the derivation
defect

```text
(I-Z^(-1))delta v_t                                  (2.1)
```

and its adjoint counterpart.  Dropping these terms would amount to imposing
`delta v_t=0`, which is impossible for a nonzero physical spectral vector.

## 3. Minimal live theorem

The direct-gauge route is therefore reduced to

```text
LINE-EULER-COBOUNDARY:
construct u_t without C_t^(-1) and prove, after bilateral base-point
subtraction,

integral_I L_t(C_t^(-1)e_t)dt ->0,                   (3.1)
```

with the explicit term `integral_I L_t(u_t)dt` included in the signed
`BASE-BULK` cancellation.

This is the deformation-line version of the reduced leakage target already
present in E84.003--E84.004.  It does not prove that the two sources are
identical; it proves that they have the same cohomological obstruction.

## 4. Consequence for strategy

The prime-cell expansion of Phase 90 remains useful as an exact observable,
but the Euler gauge does not remove the force-bearing step.  Further progress
must prove one of the following genuinely quantitative assertions:

```text
1. LINE-EULER-COBOUNDARY with safe reduced leakage;
2. PROJECTIVE-KATO-EULER directly as a signed prime-response estimate;
3. RDI-ANCHOR by an independent Stieltjes or determinant normalization. (4.1)
```

## 5. Status

```text
proved:
  no-bypass equivalence;
  exact location of the Euler derivation defect;

rejected:
  ground-vector gauge integration of the physical resonant line;

open:
  the three equivalent-strength quantitative routes in (4.1).
```

