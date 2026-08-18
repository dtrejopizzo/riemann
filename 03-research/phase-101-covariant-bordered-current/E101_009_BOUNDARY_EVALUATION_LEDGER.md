# E101.009 - Boundary evaluation ledger

## 1. Exact finite identity

For the bilateral covector

```text
S_t^bil
 =S_(iu)+S_(-iu)-S_(iu_*)-S_(-iu_*),                (1.1)
```

E101.008 and the sign of `H_t=H_A-tH_P` give

```text
BJ_t(s;s_*)=-Euler_Z(S_t^bil).                       (1.2)
```

The internal-shell decomposition is exact:

```text
BJ_t=COVBOUND_t+SHELL_t.                             (1.3)
```

Here `COVBOUND_t` contains, as one coupled scalar,

```text
archimedean endpoint commutator;
adjoint Euler endpoint commutator;
bordered column translation;
safe Cauchy-row translation;
horizontal level correction.                        (1.4)
```

## 2. Already closed

The following are algebraic identities, not remaining hypotheses:

```text
one-sided shift semigroup and Mobius inverse;
prime connection A=Z^(-1)[X,Z];
physical-to-Fourier shell split;
adjugate sandwich reduction;
characteristic tangent projection;
moving-level recombination.                          (2.1)
```

In particular, no additional finite-divergence theorem is needed.

## 3. The sole analytic assertion in this coordinate

Define

```text
RES_(L,N,t)(s;s_*)
 =COVBOUND_(L,N,t)(s;s_*)
  +SHELL_(L,N,t)(s;s_*)
  -[J_L(s)-J_L(s_*)].                                (3.1)
```

Then the unresolved assertion is exactly

```text
BASE_(L,N)(s;s_*)
 +integral_0^1 RES_(L,N,t)(s;s_*)dt
 ->0                                                 (3.2)
```

locally uniformly on the safe domain along one resolved directed family.

Equation (3.2), not an estimate on any entry in (1.4), is the boundary
evaluation theorem.

## 4. No admissible termwise replacement

The five terms in (1.4) depend on the chosen primal or dual coordinate.  Their
sum does not.  Hence separate convergence or separate smallness of these terms
is neither necessary nor invariant under the tangent-cotangent transfer.

An admissible proof may use a signed identity, a common scalar majorant after
recombination, or a normal-family argument for the complete quotient.  It may
not replace (3.2) by absolute summability of the individual boundary blocks.

## 5. Status

```text
closed:
  exact boundary ledger and removal of duplicate open labels;

open:
  the single signed boundary evaluation (3.2), equivalently the direct
  bordered anchor and Omega7.
```

