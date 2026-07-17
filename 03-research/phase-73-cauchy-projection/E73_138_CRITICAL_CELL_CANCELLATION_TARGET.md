# E73.138 - Critical Cell Cancellation Target

Date: 2026-07-12.

E73.137 identifies the first viable finite identity behind `ROW-KER_17`.

## 1. Cell decomposition

The zeta-coupled CCM matrix is

```text
H_L = W02_L - WR_L - Prime_L.
```

The ground equation is

```text
H_L xi_L = mu_L xi_L.
```

Pairing with a normalized critical row

```text
e_gamma = k_gamma/||k_gamma||,
k_gamma(d_n)=1/(-gamma-d_n),
```

gives the exact identity

```text
<e_gamma,W02_L xi_L>
-<e_gamma,WR_L xi_L>
-<e_gamma,Prime_L xi_L>
=
mu_L <e_gamma,xi_L>.                         (1)
```

`ROW-KER` is the statement that the right-hand scalar

```text
<e_gamma,xi_L>
```

is tiny after row-norm accounting.

## 2. Observed mechanism

E73.137 shows that in the critical rows:

```text
<e_gamma,W02_L xi_L>
```

and

```text
<e_gamma,Prime_L xi_L>
```

have the same scale and cancel to about `L^-18`, while `WR` is lower order.

Thus the real theorem is not a generic spectral statement.  It is:

```text
Critical Cell Cancellation (CCC):
<e_gamma,W02_L xi_L>
-
<e_gamma,Prime_L xi_L>
 =
 <e_gamma,WR_L xi_L>
 + O(L^{-17-p_gamma}).
```

Here one must not divide by `mu_L`: in the finite CCM matrices `mu_L` is
itself extremely small, of order `L^-16` to `L^-19` in the tested range.
The exact equation should instead be used in the form already measured by
E73.137:

```text
<e_gamma,H_L xi_L> - mu_L<e_gamma,xi_L> = 0,
```

with the cancellation proving the scalar channel directly through the same
finite characteristic/evaluation identity, not by division by `mu_L`.

## 3. Finite identity to prove

The target is a finite identity in the explicit cell kernels:

```text
CCC Theorem.
For every natural-height critical row gamma,

<e_gamma,W02_L xi_L>
-
<e_gamma,Prime_L xi_L>
-
<e_gamma,WR_L xi_L>

has cancellation exponent at least 17+p_gamma.
```

Equivalently:

```text
|<e_gamma,H_L xi_L>| <= C L^{-17-p_gamma}.
```

Since `H_L xi_L=mu_L xi_L` and `mu_L` is tiny, this identity is best viewed
as a consistency equation for the critical cell cancellation, not as a
division route to `ROW-KER`.  The proof of `ROW-KER` must identify the same
cell cancellation directly in `<e_gamma,xi_L>`.

## 4. What makes this non-circular

The proof uses:

```text
the explicit W02/WR/Prime cell formulas,
the finite ground equation,
the critical evaluation row,
```

but not:

```text
zeros as roots of Phi_N,
RH/positivity,
de Branges,
global convergence to Xi,
range projection tautologies.
```

## 5. Next computation

E73.139 performs the next expansion.  It shows that the cancellation is not
binwise or monotone in prime-orbit length.  The full finite Euler orbit sum
is needed.

Thus the correct explicit identity is global:

```text
sum_{p^k <= lambda^2}
(log p) p^{-k/2} <e_gamma,Q_{k log p} xi_L>

=
<e_gamma,W02_L xi_L> - <e_gamma,WR_L xi_L>
+ O(L^{-17-p_gamma}).
```

Equivalently,

```text
<e_gamma,W02_L xi_L>
-
<e_gamma,Prime_L xi_L>
-
<e_gamma,WR_L xi_L>
= O(L^{-17-p_gamma}).
```

Important separation:

```text
<e_gamma,H_L xi_L> = mu_L <e_gamma,xi_L>
```

so the cell residual itself can be small because `mu_L` is small.  That
does not by itself prove `ROW-KER`.  The real theorem must identify the
same global Euler-orbit cancellation before division by the small ground
eigenvalue, i.e. as a direct statement about the critical Cauchy evaluation
channel.

The next check is therefore a rowwise margin table with both quantities:

```text
Eval margin: q_gamma-p_gamma, the actual ROW-KER exponent.
Cell margin: -log_L |<e,H xi>| - p_gamma, the consistency exponent.
```

Only the first closes `CSV_17`; the second certifies that the finite Euler
orbit identity is numerically in the correct rowwise scale.
