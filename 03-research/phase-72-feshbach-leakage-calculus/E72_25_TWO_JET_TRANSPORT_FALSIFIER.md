# E72.25 -- Two-jet transport falsifier

**Date:** 2026-07-08.
**Role:** test and correct the transport ansatz from E72.24 before it becomes a false proof.

## 0. The ansatz tested

E72.24 introduced the possible identity

```text
(A_x-eps_x)r_x(s)
 = alpha_x(s)r_x(s)+beta_x(s)partial_s r_x(s)+e_x(s),
```

with a Weyl-invisible error. If the full vector error were small, this would be a strong and clean
route to the log-current convergence.

## 1. Numerical falsifier

Using the Phase 71 finite CCM matrix and ground vector, I projected

```text
y_x(s):=(A_x-eps_x)r_x(s)
```

onto

```text
span{r_x(s),partial_s r_x(s)}.
```

Representative residuals:

```text
lambda=4, N=20, s=10+0.2i: residual 9.48e-1
lambda=5, N=20, s=10+0.2i: residual 9.76e-1
lambda=6, N=20, s=10+0.2i: residual 9.83e-1

lambda=4, N=20, s=20+0.2i: residual 2.97e-1
lambda=5, N=20, s=20+0.2i: residual 3.35e-1
lambda=6, N=20, s=20+0.2i: residual 3.94e-1
```

Thus the full two-jet transport identity is false in the naive norm.

## 2. The tautological channel

The same calculation gives

```text
<xi_x,(A_x-eps_x)r_x(s)> = 0
```

to numerical precision. But this is not information: it follows immediately from

```text
A_x xi_x=eps_x xi_x
```

and self-adjointness.

Therefore the identity

```text
0=<xi_x,(A_x-eps_x)r_x(s)>
```

cannot by itself determine `m_x'/m_x`.

If one chooses `alpha_x,beta_x` after seeing `m_x`, the Riccati equation becomes tautological. That is
forbidden.

## 3. Corrected target

The transport theorem must not approximate the full vector `y_x(s)`. It must identify a canonical
finite-rank current projection

```text
Pi_x^{cur}(s)
```

such that:

```text
Pi_x^{cur}(s)(A_x-eps_x)r_x(s)
```

has a two-jet representation, while the complementary part is annihilated by a structural current
identity independent of `xi_x`.

Equivalently, the needed object is not:

```text
vector transport.
```

It is:

```text
current transport / commutator transport.
```

## 4. New proof target

### Current Transport Identity

Construct an operator-valued one-form `J_x(s)` from the finite CCM kernel such that

```text
d log P_x(s)
 = Tr J_x(s)
```

and prove directly that

```text
Tr J_x(s) -> d log Xi(s)
```

on two interior heights, with local normal bounds.

This bypasses the false two-jet vector approximation and attacks the log-current itself.

## 5. Status

```text
falsified: full two-jet vector transport;
survives:  current-level transport, not vector-level transport.
```

E72.24 remains valid as a conditional lemma, but the direct vector ansatz is not the proof.
