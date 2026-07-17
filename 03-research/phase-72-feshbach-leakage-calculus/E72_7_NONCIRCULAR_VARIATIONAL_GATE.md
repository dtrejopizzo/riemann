# E72.7 -- Non-circular gate for the Feshbach-Sonin variational identity

**Date:** 2026-07-08.
**Role:** prevent E72.6 from becoming a tautological restatement of reduced leakage; state exactly what
new arithmetic input must enter.

## 0. The danger

E72.6 proves the exact criterion

```text
||C_x^{-1}b_x|| -> 0
```

if and only if the low reduced channels vanish and the high reduced tail is tight. This is useful, but
by itself it is still equivalent to the target. It becomes a proof only if the two conditions are derived
from structures that do not already encode the answer.

The forbidden move is:

```text
define u_x := C_x^{-1}b_x,
then write b_x = C_x u_x.
```

That proves nothing. The vector `u_x` must be constructed independently.

## 1. The admissible source of `u_x`

The only non-circular source allowed by the prior audits is:

```text
u_x = an explicit Sonin/prolate boundary-corrector built from k_lambda,
      the pole shorting, and the archimedean/prolate calculus,
      before using the arithmetic residual b_x.
```

It may depend on:

- `k_lambda`;
- the pole line and its Feshbach projection;
- the prolate coordinate `theta`;
- the archimedean CCM/Sonin operator;
- finite prime truncation only through the explicit action of `H_x-H_x^0` on `k_lambda`.

It may not depend on:

- diagonalizing `C_x`;
- solving `C_xu=b_x`;
- the known zero divisor of `Xi`;
- endpoint identification `G_P^circ=G_Xi^{G5}`;
- a sourced Euler product or additive inverse.

## 2. The non-circular variational lemma

The theorem that would actually advance Phase 72 is:

### Arithmetic Feshbach-Sonin Coboundary Lemma

There are explicit vectors `u_x` in the primitive complement and remainders `r_x` such that

```text
Q_x(H_x-H_x^0)k_lambda = C_x u_x + r_x,
```

with

```text
||u_x|| -> 0,
||C_x^{-1}r_x|| -> 0,
```

where `u_x` and `r_x` are obtained by a pole-relative integration-by-parts formula in the CCM/Sonin
variables, not by applying `C_x^{-1}` to the residual.

This is the non-circular form of the missing identity.

## 3. Equivalent dual form

Equivalently, for every primitive complement test `v`,

```text
<v,(H_x-H_x^0)k_lambda>
   = <C_x v, u_x> + E_x(v),
```

with

```text
||u_x|| -> 0,
sup_{v != 0} |E_x(v)|/||C_xv|| -> 0.
```

This is the safest formulation because it never opens `C_x^{-1}` as a local sum. The Feshbach inverse
remains inside the graph norm.

## 4. Low/high version

In the E72.6 low/high split, the lemma may be proved in two pieces:

### Low finite channels

For each fixed `M`, construct `u_x^{(M)}` explicitly so that

```text
Pi_{x,M} b_x = Pi_{x,M} C_x u_x^{(M)} + r_x^{(M)}
```

and

```text
||Pi_{x,M}u_x^{(M)}|| -> 0,
||C_x^{-1}r_x^{(M)}|| -> 0.
```

This is finite-dimensional; it should be the first place to test the identity.

### High reduced tail

Prove a uniform graph-tail bound:

```text
lim_{M->infty} limsup_x
sup_{v in E_x(M)^\perp_C}
 |<v,b_x>|/||C_xv|| = 0.
```

This is not a prime-by-prime absolute bound. It must use the actual high-frequency coercivity of the
compressed complement.

## 5. Kill tests

A candidate identity fails if any of the following happens.

### K1 -- inverse smuggling

The construction of `u_x` uses `C_x^{-1}b_x`, Riesz projections of the unknown low spectral island, or
the endpoint resolvent. Then it is circular.

### K2 -- local inverse smuggling

The proof expands `C_x^{-1}` as a sum over prime-place inverses. This repeats the Phase 65 additive Green
mistake.

### K3 -- absolute ceiling

The proof bounds

```text
sum_{p,k} |cell_{p,k}|
```

before cancellation. This repeats the Phase 67 incoherent ceiling.

### K4 -- point-local kernel

The proof makes a Christoffel/Jacobi kernel into an evaluator at a zeta zero. This repeats Phase 32.

### K5 -- endpoint identification

The proof identifies the limiting source Hessian with `G_Xi^{G5}` using only the scalar determinant.
This repeats the corrected D9 error from Phase 65.

## 6. The first buildable subproblem

The smallest nontrivial target is the one-channel identity:

```text
<e_{x,1},(H_x-H_x^0)k_lambda>/lambda_{x,1} -> 0.
```

But even this must be proved without defining `e_{x,1}` from the unknown endpoint. The admissible version
is:

```text
for every normalized v_x with ||C_x v_x|| <= O(lambda_{x,1})
and v_x in the first compact Sonin slow family,
<v_x,(H_x-H_x^0)k_lambda>/||C_xv_x|| -> 0.
```

This asks for cancellation against a compact family of slow Sonin tests, not against zero-localized
kernels.

## 7. Status

```text
proved:   exact reduced leakage, dual norm, and low/high criterion;
new gate: a proof must construct the coboundary primitive u_x independently of C_x^{-1}b_x;
open:     build the explicit Sonin/prolate boundary-corrector u_x.
```

This is the exact place where new mathematics has to enter.

