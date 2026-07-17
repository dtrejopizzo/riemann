# E72.17 -- Maximal resonance block and the failure of automatic symmetry cancellation

**Date:** 2026-07-08.
**Role:** test the last possible non-circular escape left by E72.16: cancellation of the maximal
off-critical resonance block by finite CCM/prolate symmetry.

## 0. Setup

Assume an off-critical zero exists. Let

```text
beta_* := max{ Re rho : Xi(rho)=0, Re rho>1/2 in the working window }.
```

The maximal block in the E72.15 expansion is

```text
B_x(beta_*) := sum_{rho: Re rho=beta_*} R_x(rho)/rho.
```

ACD can still hold in the presence of off-line zeros only if

```text
B_x(beta_*) = o((lambda_{x,1}^D)^(1/2))                (MRC)
```

after projection away from lower-real-part terms.

## 1. Functional-equation pairing does not cancel the maximal block

The functional equation pairs

```text
rho = beta+i gamma
```

with

```text
1-rho = 1-beta-i gamma.
```

If `beta>1/2`, the partner has real part `<1/2`, hence contributes to the explicit formula at size
`x^(1-beta)`, while the maximal term has size `x^beta`. Therefore it cannot cancel the maximal block.

In the resonance-vector language:

```text
||R_x(1-rho)|| is lower order than ||R_x(rho)||
```

whenever the Mellin response has the natural scale

```text
R_x(s) ~ x^s times a non-vanishing boundary/mean response.
```

Thus the functional equation is not a maximal-block cancellation mechanism.

## 2. Conjugation only creates real oscillation

Real-valued kernels give

```text
R_x(conj rho)=conj R_x(rho)
```

in scalar projections, and the conjugate pair contributes

```text
R_x(rho)/rho + R_x(conj rho)/conj rho
  = 2 Re( R_x(rho)/rho ).
```

This can vanish at isolated phases, but it is not a Hilbert-norm cancellation theorem. In norm, the
maximal conjugate block is small only if the vector itself is phase-orthogonal in every dual direction:

```text
Re <R_x(rho)/rho, eta> = o((lambda_{x,1}^D)^(1/2))
```

for all unit `eta` after accounting for the other zeros with the same `beta`.

That is a zero-dependent phase assertion, not a consequence of real symmetry.

## 3. The finite-block obstruction

### Theorem 72.17

Let `Z_beta` be the finite set of zeros in the working window with real part `beta>1/2`. Assume:

1. the explicit-formula expansion of E72.15 holds;
2. lower-real-part zero blocks are lower order;
3. the vector family `{R_x(rho)/rho : rho in Z_beta}` has a Gram matrix whose least nonzero singular
   value is not `o((lambda_{x,1}^D)^(1/2))` along a subsequence.

Then ACD fails along that subsequence.

### Proof

Let

```text
V_x(beta)=span{R_x(rho)/rho : rho in Z_beta}.
```

Project `T_x` from E72.15 onto `V_x(beta)`. Lower-real-part terms, trivial terms, and cutoff terms are
lower order by assumptions 1 and 2. The projected maximal block is

```text
- sum_{rho in Z_beta} R_x(rho)/rho.
```

By assumption 3, this vector cannot be

```text
o((lambda_{x,1}^D)^(1/2))
```

unless the coefficient vector of the zero block lies in an asymptotic null direction of the Gram
matrix. But the coefficients are fixed nonzero numbers `1/rho`. Hence the maximal block remains
visible. Therefore

```text
||T_x||_{H_x} not= o((lambda_{x,1}^D)^(1/2)),
```

so ACD fails. `QED`

## 4. Consequence

The only way a vector-cancellation proof can work is by proving a genuinely new finite-CCM identity:

```text
the coefficient vector (1/rho)_{rho in Z_beta}
lies in an asymptotic null direction of the resonance Gram matrix
G_x(rho,sigma)=<R_x(rho),R_x(sigma)>_{H_x}.
```

This identity would have to be proved without knowing `Z_beta` in advance. If the null direction is
constructed after seeing the zeros, the proof is circular. If it follows from the finite CCM algebra,
that would be the missing theorem.

## 5. Verdict on the current route

Phase 72 has reduced the problem to the sharp possible place:

```text
prove an intrinsic null-vector identity for maximal off-line resonance Gram blocks.
```

But neither the functional equation nor real symmetry supplies it. Any proof now must exhibit a new
finite-dimensional identity in the actual CCM/prolate resonance Gram matrix.
