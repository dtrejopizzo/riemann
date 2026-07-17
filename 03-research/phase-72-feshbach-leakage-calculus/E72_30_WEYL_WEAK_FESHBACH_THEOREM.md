# E72.30 -- Weyl-weak Feshbach theorem

**Date:** 2026-07-08.
**Role:** replace norm convergence of ground vectors by the weakest convergence needed for divisor
currents.

## 0. Endpoint from E72.29

The scalar bordered current only needs:

```text
(xi_x-k_x)^T(sI-D_x)^(-1)1_x -> 0
```

on two interior heights, plus the derivative version. This is Weyl-weak convergence, not vector norm
convergence.

## 1. Feshbach expansion

Let:

```text
H_x^0 k_x = mu_x^0 k_x,
H_x = H_x^0 + R_x,
theta_x = actual normalized ground vector,
Q_x=1-|k_x><k_x|,
C_x=Q_x(H_x-mu_x^0-a_x)Q_x,
a_x=<k_x,R_xk_x>.
```

The reduced Feshbach equation gives, to first order and with the usual normalization,

```text
Q_x theta_x = - C_x^(-1) Q_x R_x k_x + higher_x.       (F)
```

E72.3 used this in norm. Here we test it only against Weyl resolvents.

## 2. Weyl test functionals

For `s` off the real pole mesh, define

```text
ell_{x,s}(v) := <(sI-D_x)^(-1)1_x, v>.
```

The Weyl-weak target is:

```text
ell_{x,s}(theta_x-k_x) -> 0.
```

Since `theta_x-k_x` is in the complement up to a scalar normalization correction, the leading term is

```text
- ell_{x,s}( C_x^(-1)Q_xR_xk_x ).
```

## 3. The theorem

### Theorem 72.30

Assume:

1. the finite Feshbach expansion `(F)` holds with

```text
ell_{x,s}(higher_x) -> 0
```

on two interior heights;
2. the Weyl-reduced leakage vanishes:

```text
ell_{x,s}( C_x^(-1)Q_xR_xk_x ) -> 0              (WRL)
```

distributionally in `t` for `s=t+i eta`, at two interior heights;
3. the same holds after one `s`-derivative:

```text
partial_s ell_{x,s}( C_x^(-1)Q_xR_xk_x ) -> 0;
```

4. the slab normal bounds from E72.22 hold.

Then the finite CCM divisor currents converge Schur-free to the prolate/`Xi` current. Consequently RH
follows by E72.19-E72.22 and E72.29.

### Proof

By the Feshbach expansion,

```text
ell_{x,s}(theta_x-k_x)
 = - ell_{x,s}(C_x^(-1)Q_xR_xk_x)
   + ell_{x,s}(higher_x).
```

Assumptions 1 and 2 give Weyl-weak ground convergence:

```text
ell_{x,s}(theta_x-k_x) -> 0.
```

Assumption 3 gives the derivative convergence needed for the log-current. E72.29 converts this into
scalar bordered current convergence. E72.22 rules out hidden inner defects. E72.20 and E72.19 then give
the divisor-current closure and RH. `QED`

## 4. The new minimal arithmetic estimate

The exact remaining estimate is now:

### WRL -- Weyl-reduced leakage

For `s=t+i eta`, `eta != 0`,

```text
< (sI-D_x)^(-1)1_x, C_x^(-1)Q_x(H_x-H_x^0)k_x > -> 0
```

distributionally in `t`, and likewise after `partial_s`.

This is weaker than:

```text
||C_x^(-1)Q_x(H_x-H_x^0)k_x|| -> 0.
```

It asks only that the reduced leakage be invisible to the Weyl Cauchy tests that generate the divisor
current.

## 5. Why this is the sharp target

Every previous target implies WRL:

```text
norm reduced leakage => WRL;
PSC/CC/ACD          => norm reduced leakage => WRL;
BTE full trace      => Weyl-weak convergence => WRL.
```

But WRL is the first target that is exactly matched to the finite spectral current. It does not ask for
more convergence than the divisor needs.

## 6. Status

```text
proved: WRL + derivative WRL + normal bounds => Schur-free current convergence => RH;
open:   prove WRL from the explicit arithmetic/prolate structure.
```

The proof attempt must now estimate a single scalar Cauchy transform of the Feshbach leakage, not the
full leakage vector.
