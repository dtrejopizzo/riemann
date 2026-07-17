# E73.173 - Eigenline Cauchy-transform audit

Date: 2026-07-14.

## 1. Purpose

E73.172 reduces `QG` to three scalar forms:

```text
ell_r(G_L) = a_r(L) dot xi_L,       r=1,2,3.
```

This note tests whether these forms are immediate consequences of the finite
eigenline equation:

```text
(H_L-mu_L) xi_L = 0.
```

## 2. Row-space route

If `a_r` were a well-conditioned row of `H_L-mu_L`, then

```text
a_r dot xi_L = 0
```

would follow directly.  More generally, one can try to solve

```text
a_r = y_r^*(H_L-mu_L) + residual_r.
```

Then

```text
ell_r(G_L) = residual_r dot xi_L.
```

The numerical audit shows that this is not a useful proof mechanism:

```text
preB = log_L ||y_r||
```

is typically between `6` and `10` in trusted rows.  Thus the inverse row-space
certificate is extremely ill-conditioned.

Conclusion:

```text
Do not prove QG-LF by inverting H_L-mu_L.
```

That would reintroduce a large hidden condition loss.

## 3. Exact transformed eigenline identity

Write

```text
H_L = H_arch,L - P_prime,L.
```

For every quotient row `a_r`,

```text
a_r H_arch,L xi_L - a_r P_prime,L xi_L
= mu_L a_r xi_L.
```

Equivalently:

```text
Arch_r(L) - Prime_r(L) = mu_L ell_r(G_L).
```

This identity is exact.  It is the finite Cauchy-transform version of the
eigenline equation.

## 4. Diagnostic meaning

The table in E73.173 shows:

```text
Arch_r(L) and Prime_r(L) are much larger than mu_L ell_r(G_L),
```

often by many powers of `L`.  Therefore `QG-LF` is not produced by a small
prime term or a small archimedean term separately.  It is produced by
high-order matching:

```text
Arch_r(L) ~= Prime_r(L)
```

in the three quotient Cauchy forms.

This is the current exact analytic frontier:

```text
QG-MATCH:
Arch_r(L) - Prime_r(L) = O(mu_L L^B e^(-alpha L)),
r=1,2,3.
```

After dividing by `mu_L`, this is exactly `QG-LF`.

## 5. What this rules out

The following proof routes are rejected for `QG`:

1. row-space inversion of `H_L-mu_L`, because the prevector is too large;
2. absolute bounds on the prime transform, because the prime term is not
   itself small enough;
3. a unilateral positivity argument, because the observed mechanism is a
   signed arch/prime matching.

## 6. What remains

The next proof-facing theorem is not a large RFBD/Green-cycle estimate.  It
is the three-form matching theorem:

```text
For the quotient rows a_r(L),

|a_r H_arch,L xi_L - a_r P_prime,L xi_L|
<= |mu_L| L^B e^(-alpha L),     r=1,2,3.
```

This is finite, explicit, and uses the actual CCM/Feshbach eigenline.

## 7. Status

```text
proved:   exact transformed eigenline identity;
rejected: row-space inversion as proof of QG;
open:     prove the arch/prime matching estimate QG-MATCH.
```
