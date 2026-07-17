# E72.24 -- Weyl Riccati transport from the finite CCM eigenvector equation

**Date:** 2026-07-08.
**Role:** derive the exact mechanism that would prove the two-height Weyl current convergence of
E72.23 from the finite eigenvector equation, without root tracking.

## 0. Setup

Let

```text
D_x = diag(d_{x,k}),
r_x(s) := (s-D_x)^(-1)1,
m_x(s) := <r_x(s), xi_x>.
```

Then

```text
m_x'(s) = - <(s-D_x)^(-2)1, xi_x>
        = <partial_s r_x(s), xi_x>.
```

Let the finite CCM operator be

```text
A_x := QW_x,
A_x xi_x = eps_x xi_x.
```

The goal from E72.23 is to prove convergence of

```text
m_x'(s)/m_x(s) + Q_x'(s)/Q_x(s)
```

on two interior horizontal lines.

## 1. Resolvent transport identity

The needed algebraic structure is:

```text
(A_x-eps_x)r_x(s)
 = alpha_x(s) r_x(s)
   + beta_x(s) partial_s r_x(s)
   + e_x(s).                                      (RT)
```

This identity is non-circular if `alpha_x`, `beta_x`, and `e_x` are computed from the explicit CCM
kernel, not from `Xi` or from finite roots.

## 2. Riccati consequence

### Lemma 72.24

Assume `(RT)`. Then, wherever `m_x(s) != 0` and `beta_x(s) != 0`,

```text
m_x'(s)/m_x(s)
 = - alpha_x(s)/beta_x(s)
   - <e_x(s),xi_x>/(beta_x(s)m_x(s)).             (WR)
```

### Proof

Pair `(RT)` with `xi_x`. Since `A_x` is self-adjoint and `A_x xi_x=eps_x xi_x`,

```text
< (A_x-eps_x)r_x(s), xi_x >
 = < r_x(s), (A_x-eps_x)xi_x >
 = 0.
```

The right side of `(RT)` gives

```text
0 = alpha_x(s)<r_x(s),xi_x>
    + beta_x(s)<partial_s r_x(s),xi_x>
    + <e_x(s),xi_x>.
```

Using

```text
<r_x(s),xi_x>=m_x(s),
<partial_s r_x(s),xi_x>=m_x'(s),
```

and dividing by `beta_x(s)m_x(s)` gives `(WR)`. `QED`

## 3. Current convergence theorem

### Theorem 72.24

Fix a compact horizontal segment `K_eta={t+i eta : t in K}`, `eta != 0`. Assume:

1. the transport identity `(RT)` holds on a neighborhood of `K_eta`;
2. the transport coefficients satisfy

```text
- alpha_x(s)/beta_x(s) + Q_x'(s)/Q_x(s)
   -> Xi'(s)/Xi(s)
```

distributionally on `K_eta`;
3. the error is invisible in the Weyl channel:

```text
<e_x(s),xi_x>/(beta_x(s)m_x(s)) -> 0
```

distributionally on `K_eta`;
4. the same estimates hold on a second height and the local normal bounds of E72.22 hold in the slab.

Then Schur-free current convergence holds in that slab. Consequently, by E72.19-E72.22, no off-real
`Xi` divisor can lie in the slab.

### Proof

By Lemma 72.24,

```text
m_x'/m_x+Q_x'/Q_x
 = -alpha_x/beta_x+Q_x'/Q_x
   - <e_x,xi_x>/(beta_x m_x).
```

Assumptions 2 and 3 give the two-height log-current convergence `(WTCC)` from E72.23. Assumption 4
applies E72.22, ruling out hidden off-real current. E72.19 then gives the divisor conclusion. `QED`

## 4. What must be constructed

The proof is now concentrated in one explicit algebraic problem:

### CCM Resolvent Transport

For the explicit finite CCM kernel `A_x`, prove `(RT)` with:

```text
alpha_x, beta_x  -> explicit Gamma/Euler transport coefficients,
e_x              -> Weyl-invisible error.
```

The ratio

```text
-alpha_x/beta_x + Q_x'/Q_x
```

must converge to `Xi'/Xi` on interior horizontal lines.

## 5. Non-circularity gate

This is admissible only if:

```text
alpha_x, beta_x, e_x
```

are derived by applying `A_x` to the explicit resolvent vector `r_x(s)`.

It is circular if:

```text
alpha_x/beta_x
```

is chosen after comparing to `Xi'/Xi`.

## 6. Status

```text
proved: a resolvent transport identity implies WTCC and Schur-free current convergence;
open:   prove the transport identity for the explicit CCM matrix.
```

The next calculation is therefore not spectral. It is direct: compute `(A_x-eps_x)r_x(s)` and project
it onto the two-dimensional jet span `{r_x(s), partial_s r_x(s)}`.
