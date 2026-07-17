# E72.11 -- Doob-Poisson transport form of the commutator target

**Date:** 2026-07-08.
**Role:** reduce the model commutator equation of E72.10 to a one-source Poisson equation in the
ground-state/Doob coordinates of the prolate model.

## 0. Starting point

E72.10 reduced PSC to the model commutator equation

```text
Q_xR_xk_x = Q_x[C_x^0,A_x]k_x + e_x.
```

This document computes what that equation means in model boundary coordinates. The point is that the
commutator against a ground state is not a mysterious second-order object. After the Doob transform, it
is a Poisson equation for a single source.

## 1. Model Sturm-Liouville form

On the prolate boundary coordinate `theta`, write the model complement locally as

```text
L_x^0 f = -partial_theta(p_x partial_theta f) + q_x f,
```

with model ground state

```text
L_x^0 k_x = 0
```

after recentering by `mu_x^0`. The complement operator `C_x^0` is the restriction of `L_x^0` to the
orthogonal complement of `k_x`, with pole/ground line removed.

This notation is local/model notation only. It does not assert that the actual arithmetic complement
`C_x` is a free Dirichlet operator.

## 2. Ground-state factorization

Let

```text
w = A_x k_x.
```

Write

```text
w = k_x h.
```

Then, using `L_x^0 k_x=0`,

```text
L_x^0(k_x h)
  = k_x D_x h,
```

where the Doob/ground-state generator is

```text
D_x h
  := - k_x^{-2} partial_theta( p_x k_x^2 partial_theta h ).
```

### Proof

Compute:

```text
L_x^0(kh)
 = -partial(p partial(kh)) + qkh
 = -partial(p(k'h+kh')) + qkh
 = -partial(pk'h) - partial(pkh') + qkh.
```

Since `L_x^0k=0`, we have

```text
qk = partial(pk').
```

Thus

```text
L_x^0(kh)
 = -partial(pk')h - pk'h' - partial(pkh') + partial(pk')h
 = -pk'h' - partial(pkh')
 = -k^{-1}partial(pk^2h').
```

So

```text
L_x^0(kh) = k[-k^{-2}partial(pk^2h')] = kD_xh.
```

`QED`

## 3. MCC becomes a Poisson equation

Let the residual force density be

```text
F_x := Q_xR_xk_x.
```

If `A_xk_x = k_x h_x`, then

```text
Q_x[C_x^0,A_x]k_x = C_x^0Q_xA_xk_x = Q_x L_x^0(k_xh_x).
```

Using the factorization above, the model commutator equation becomes:

```text
Q_x( k_x D_x h_x ) = F_x - e_x.                 (P)
```

Thus the new proof target is:

```text
solve the one-source Doob-Poisson equation D_xh_x = F_x/k_x
modulo the ground line and a reduced-small error,
with ||k_xh_x|| -> 0.
```

This is still not solved, but it is now a classical-looking Poisson problem for the model Doob generator.

## 4. Why this is not the forbidden inverse

Solving

```text
D_x h_x = F_x/k_x
```

looks like applying a model inverse. That is allowed only because:

```text
D_x is the explicit model Doob generator;
C_x^0 is the explicit prolate complement;
the actual inverse C_x^{-1} is not used to define h_x.
```

The forbidden move would be solving:

```text
C_x u = F_x.
```

E72.11 solves only the model Poisson problem and then asks separately for the one-vector replacement
estimate from model graph to actual graph.

## 5. Solvability condition

The Doob generator `D_x` has constants in its kernel. Therefore the Poisson equation is solvable only
after the source has zero mean with respect to the ground-state measure

```text
dpi_x := k_x^2 dtheta.
```

The condition is:

```text
int (F_x/k_x) dpi_x = <k_x,F_x> = 0.
```

This is automatic because

```text
F_x = Q_xR_xk_x
```

lies in the complement of `k_x`.

So the pole/ground projection is not cosmetic: it is exactly the Fredholm solvability condition for the
model Poisson equation.

## 6. Size of the primitive

Let `D_x^+` be the model Doob inverse on mean-zero functions. The formal solution is

```text
h_x = D_x^+(F_x/k_x),
w_x = k_x h_x.
```

The PSC smallness condition

```text
||w_x|| -> 0
```

is equivalent to:

```text
||k_x D_x^+(F_x/k_x)|| -> 0.
```

This is a one-source model smoothing estimate.

It is weaker than uniform control of `D_x^+` on all sources. Uniform control would be the old Phase 60
wall. The required statement is only for the specific residual source `F_x/k_x`.

## 7. Low/high split in Doob variables

Let `{psi_{x,j}}` be the mean-zero eigenfunctions of `D_x` in `L^2(dpi_x)`:

```text
D_x psi_{x,j} = nu_{x,j} psi_{x,j},      j>=1.
```

Expand

```text
F_x/k_x = sum_{j>=1} f_{x,j} psi_{x,j}.
```

Then

```text
h_x = sum_{j>=1} f_{x,j}/nu_{x,j} psi_{x,j},
||w_x||^2 = int |h_x|^2 dpi_x = sum_{j>=1} |f_{x,j}|^2/nu_{x,j}^2.
```

Therefore the Doob-Poisson version of PSC is:

```text
for every fixed M, sum_{j<=M}|f_{x,j}|^2/nu_{x,j}^2 -> 0;
lim_{M->infty} limsup_x sum_{j>M}|f_{x,j}|^2/nu_{x,j}^2 = 0.
```

This is the E72.6 reduced low/high criterion in model Doob coordinates.

## 8. The new named target

### DPS -- Doob-Poisson Smoothing for the residual force

For the actual residual force

```text
F_x = Q_x(H_x-H_x^0)k_x,
```

the mean-zero Doob-Poisson solution

```text
h_x = D_x^+(F_x/k_x)
```

satisfies:

```text
||h_x||_{L^2(dpi_x)} -> 0,
```

and the actual/model replacement term satisfies:

```text
||C_x^{-1}(C_x-C_x^0)(k_xh_x)|| -> 0.
```

DPS implies MCC, hence PSC, hence reduced leakage.

## 9. What DPS asks arithmetically

DPS says the residual force is not merely small after cancellation. It says the residual force is a
high Doob derivative:

```text
F_x/k_x = D_x h_x
```

with a primitive `h_x` that vanishes in `L^2(dpi_x)`.

Equivalently:

```text
the actual/model force has no persistent low Doob modes.
```

This is a precise, one-vector statement. It does not ask for the whole arithmetic operator to converge
to the prolate operator.

## 10. Kill tests

DPS fails as new mathematics if:

```text
K1. The estimate is upgraded to all sources, becoming uniform-source PSC.
K2. The proof uses lower coercivity equivalent to the Phase 60 sign wall.
K3. The low Doob coefficients are identified by locating zeta zeros.
K4. The high tail is bounded by absolute prime sums.
K5. The replacement term uses additive local inverses for C_x^{-1}.
```

## 11. Status

```text
proved:   MCC reduces to a Doob-Poisson equation for the one residual source;
proved:   DPS => MCC => PSC => reduced leakage;
open:     prove DPS for F_x=Q_x(H_x-H_x^0)k_x from the explicit finite CCM/Sonin formula.
```

This is the most concrete form so far. The next calculation is no longer "find a quantum algebra" or
"prove Feshbach convergence"; it is:

```text
compute the Doob coefficients f_{x,j} of the single residual source F_x/k_x,
prove their reduced square sum tends to zero.
```

