# E72.8 -- The Feshbach-Sonin corrector equation: full attempt

**Date:** 2026-07-08.
**Role:** try to construct the non-circular coboundary primitive `u_x` required by E72.7.

## 0. Target

The Phase 72 target is no longer raw residual smallness. It is the reduced coboundary identity

```text
b_x := Q_x(H_x-H_x^0)k_x = C_x u_x + r_x,
||u_x|| -> 0,
||C_x^{-1}r_x|| -> 0.
```

The non-circularity rule from E72.7 is strict:

```text
u_x must not be defined as C_x^{-1}b_x.
```

It must come from the Sonin/prolate boundary calculus before solving the Feshbach inverse equation.

## 1. What the prolate/Sonin machinery can honestly supply

The previous phases supply the following usable pieces.

### P1 -- exact support restriction

Phase 60, `2b_part_i_EXACT.md`, proves:

```text
A_lambda = A_infty restricted to E_lambda.
```

There is no prime tail to estimate. The finite prime cutoff is exact by support.

### P2 -- ground-state/Doob transform

Phase 60 and Phase 63 repeatedly use the finite positive ground state `u_0` and the Doob transform:

```text
f = u_0 g,
<f,(A_lambda-epsilon_0)f> = D_lambda(g,g).
```

This separates shape from sign. The transformed form is positive at finite `lambda`, but any uniform
lower coercivity of the rescaled form was previously identified as RH-hard if it implies `epsilon_0>0`
uniformly.

### P3 -- high-mode contamination is real

The full ambient residual is too large. The only safe quantity is the shorted/reduced one:

```text
C_x^{-1}b_x.
```

This is why E72.3 is the right correction.

### P4 -- constant-coefficient Dirichlet/prolate identifications were refuted

Several older documents warn that one cannot simply assert:

```text
limit operator = free Dirichlet Laplacian
```

or that individual prolate modes are the exact limiting eigenvectors. The robust fact is weaker:
low-spectrum ratios look Dirichlet-like; the actual limit operator has variable/boundary-layer
structure, and proving lower coercivity is the hard part.

## 2. The only plausible corrector ansatz

Let the actual compressed complement be

```text
C_x = Q_x(H_x - mu_x^0 - a_x)Q_x.
```

Let the residual force functional be

```text
F_x(v) = <v,(H_x-H_x^0)k_x>,       v in Q_xH.
```

The only admissible Sonin/prolate corrector is a boundary corrector `U_x` satisfying a first-order
integration-by-parts identity of the form

```text
F_x(v) = Bdry_x(v) + Bulk_x(v),
```

where

```text
Bdry_x(v) = <C_x v, u_x>
```

for an explicit small boundary primitive `u_x`, and

```text
Bulk_x(v)
```

is small in the dual `C_x`-graph norm.

Thus the corrector equation is not:

```text
C_x u_x = b_x.
```

It is:

```text
F_x(v) - <C_xv,u_x> = E_x(v),
sup_v |E_x(v)|/||C_xv|| -> 0.
```

## 3. Candidate construction of `u_x`

The prolate/Sonin boundary calculus suggests the following structure.

### Boundary coordinate

Let `theta` be the prolate edge coordinate from the earlier Phase 60/63 analyses. The slow sector is
described by functions of `theta`, after Doob conjugation by the finite ground state.

### Boundary mismatch

The model vector `k_x` satisfies the model Euler-Lagrange equation:

```text
Q_x(H_x^0-mu_x^0)k_x = 0.
```

The actual residual is therefore the failure of `k_x` to satisfy the actual Euler-Lagrange equation:

```text
b_x = Q_x(H_x-mu_x^0-a_x)k_x
```

up to the diagonal scalar recentering. In a boundary-layer calculus, this residual should be caused by
the mismatch between:

```text
actual finite CCM boundary condition
```

and

```text
model prolate/Sonin boundary condition.
```

So the natural primitive is:

```text
u_x = boundary layer solution of the homogeneous complement equation
      with boundary data = actual-model boundary mismatch of k_x.
```

In ordinary Sturm-Liouville language, this is exactly how one proves a residual is a coboundary: solve
the homogeneous boundary corrector and leave only a small bulk forcing term.

## 4. Why this is not yet a proof

To make the construction above rigorous, one needs three estimates.

### C1 -- boundary trace theorem in the actual Feshbach graph norm

One must define a boundary trace map

```text
Tr_x : Dom(C_x) -> Boundary_x
```

with a uniform estimate

```text
||Tr_x v|| <= K ||C_x v||.
```

This cannot be the old pointwise Christoffel trace at zeta zeros. It must be a genuine graph trace for
the actual compressed complement.

### C2 -- explicit boundary mismatch is small

The mismatch of `k_x` between actual and model boundary conditions must satisfy

```text
||mismatch_x(k_x)||_{Boundary_x^*} -> 0.
```

This is the only place where the arithmetic content may enter. It must be proved from the finite CCM
construction and the support-exact prime action, not from the zero divisor.

### C3 -- bulk forcing is reduced-small

After subtracting the boundary corrector, the remaining bulk term must obey

```text
sup_v |Bulk_x(v)|/||C_xv|| -> 0.
```

This is the reduced-tail/tightness estimate of E72.6 in variational form.

## 5. The obstruction check against Phase 60

The danger is C1. Phase 60 already found:

```text
uniform lower Dirichlet coercivity of the re-scaled form is RH-hard
```

when it controls the sign/scale of the bottom Weil form.

Therefore C1 is admissible only if it is a **graph trace upper bound** for the already assembled positive
complement `C_x`, not a lower coercivity statement for the full Weil form.

This distinction is crucial:

- allowed: `||Tr_x v|| <= K ||C_xv||`;
- forbidden: `C_x >= c * Dirichlet form` if that is equivalent to `epsilon_0>0` or RH-local.

If the proof of C1 needs the forbidden lower coercivity, Phase 72 collapses back to the Phase 60 wall.

## 6. The honest theorem we can prove now

### Theorem 72.8 -- boundary-corrector principle

Assume there exist:

1. boundary spaces `Boundary_x`;
2. trace maps `Tr_x : Dom(C_x)->Boundary_x`;
3. explicit boundary mismatch functionals `m_x in Boundary_x^*`;
4. explicit vectors `u_x in Q_xH`;
5. remainders `E_x`;

such that, for every `v in Dom(C_x)`,

```text
<v,(H_x-H_x^0)k_x> = m_x(Tr_x v) + E_x(v),
```

and

```text
m_x(Tr_x v) = <C_xv,u_x>,
```

with

```text
||u_x|| -> 0,
sup_{v != 0}|E_x(v)|/||C_xv|| -> 0.
```

Then

```text
||C_x^{-1}Q_x(H_x-H_x^0)k_x|| -> 0.
```

Consequently, by E72.3,

```text
theta_x -> k_x.
```

Combined with E71.16/E71.17, this yields stable-divisor convergence to `Xi`, and hence RH.

### Proof

By the identity,

```text
<v,b_x> = <C_xv,u_x> + E_x(v).
```

Taking the supremum over `v` with `||C_xv||=1`, E72.4 gives

```text
||C_x^{-1}b_x||
 <= ||u_x|| + sup_{v != 0}|E_x(v)|/||C_xv|| -> 0.
```

Then E72.3 applies. `QED`

## 7. What remains genuinely open

The theorem above is not yet the desired proof. It isolates the exact missing construction:

```text
build the boundary trace/mismatch/corrector triple (Tr_x, m_x, u_x)
from actual CCM/Sonin variables.
```

The first concrete lemma is:

### Missing Lemma 72.8.C1 -- graph trace for the actual complement

There is a boundary trace `Tr_x` on the prolate/Sonin slow boundary such that

```text
||Tr_x v|| <= K ||C_xv||
```

uniformly in `x`, and this estimate is a graph upper bound for the already shorted complement, not a
hidden lower-coercivity statement equivalent to RH.

The second is:

### Missing Lemma 72.8.C2 -- vanishing actual/model boundary mismatch

For `k_x=k_lambda`, the actual CCM boundary condition and the prolate model boundary condition differ by
a functional `m_x` satisfying

```text
||m_x||_{Boundary_x^*} -> 0.
```

The third is:

### Missing Lemma 72.8.C3 -- reduced bulk tightness

The post-corrector bulk term satisfies

```text
sup_v |E_x(v)|/||C_xv|| -> 0.
```

## 8. Verdict

The corrector cannot be honestly closed from the existing documents alone.

What is closed here is the exact implication:

```text
boundary-corrector trace identity
  => reduced leakage
  => theta_x -> k_x
  => stable divisor convergence
  => RH.
```

The load-bearing new mathematics is now no longer vague. It is precisely the construction of a
non-circular boundary trace/mismatch/corrector triple for the actual Feshbach-compressed CCM complement.

If C1 uses RH-hard lower coercivity, the route dies. If C1 is a genuine graph trace upper bound and C2/C3
are proved from the finite CCM/Sonin boundary calculus, Phase 72 closes.

