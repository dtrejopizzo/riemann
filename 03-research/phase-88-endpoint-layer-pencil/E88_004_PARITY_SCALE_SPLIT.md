# E88.004 - Parity scale split of the endpoint pencil

## 1. Exact diagonalization by parity

The deformation `H_t=H_A-tH_P` commutes with mesh reversal for every `t`.
If `P` contains one endpoint eigenline of each parity, then the effective
Feshbach pencil is diagonal:

```text
F_t=diag(F_t^E,F_t^O).                                (1.1)
```

### Proof

Every block entering the Feshbach formula preserves parity.  The off-diagonal
matrix element between an even and an odd vector is therefore zero, before and
after the Schur correction. `QED`

Thus a two-dimensional layer can be analyzed through two scalar Feshbach
functions.

## 2. Test of a common scale

Choose

```text
rho_N=lambda_{N,1}^O,                                 (2.1)
```

the closest odd endpoint eigenvalue.  The scaled pencils at
`t=1-rho_N tau` are

```text
outer modes  lambda_E/rho_O   tau   F_E/rho_O   F_O/rho_O
4            1.35e-3          0     1.35e-3      1
                              1     2.19          0.777
                              10    22.43         0.0174

6            2.44e-3          0     2.44e-3      1
                              1     1.53          0.890
                              10    15.19         0.230

8            1.18e-3          0     1.18e-3      1
                              1     1.23          0.934
                              10    12.27         0.458.               (2.2)
```

The off-diagonal scaled entries are below the working multiprecision floor,
as required by (1.1).

## 3. Two intrinsic layer scales

Write `r=1-t` and expand at the endpoint:

```text
F_{1-r}^E=lambda_E+kappa_E r+O(r^2),
F_{1-r}^O=lambda_O+kappa_O r+O(r^2).                  (3.1)
```

When the derivatives are nonzero, define

```text
rho_E=lambda_E/|kappa_E|,
rho_O=lambda_O/|kappa_O|.                             (3.2)
```

The one-step slopes extracted from (2.2) give

```text
outer modes   kappa_E     kappa_O     rho_E/rho_base  rho_O/rho_base
4             2.19        -0.223      6.2e-4          4.5
6             1.52        -0.110      1.6e-3          9.1
8             1.23        -0.066      9.6e-4          15.1,            (3.3)
```

where `rho_base=lambda_O`.  The displayed slopes are finite diagnostics; the
definitions (3.1)--(3.2) are exact.

The even and odd layers are separated by several orders of magnitude.  On
the common scale `rho_base`, the limiting endpoint matrix has one vanishing
entry, so the invertibility hypothesis in E88.002 fails at `tau=0`.

## 4. Decision

```text
single fixed two-dimensional scale: rejected;
parity-separated nested scales: retained.             (4.1)
```

The correct matched expansion must treat

```text
inner layer: r=rho_E tau_E,
outer layer: r=rho_O tau_O,                            (4.2)
```

and match their projective bordered numerators in an overlap region.  The two
contributions cannot be multiplied independently because they enter the same
scalar numerator

```text
G_t=G_t^reg
    -h_t^E b_t^E/F_t^E
    -h_t^O b_t^O/F_t^O.                               (4.3)
```

## 5. Status

```text
proved:
  exact parity diagonalization of the effective pencil;

refuted as actual CCM scaling:
  a single invertible fixed-dimensional endpoint pencil;

opened:
  a two-layer matched parity expansion of the common bordered numerator.
```

