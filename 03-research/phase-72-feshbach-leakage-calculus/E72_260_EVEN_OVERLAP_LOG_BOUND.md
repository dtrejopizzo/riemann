# E72.260 -- Even-overlap logarithmic Green bound

**Purpose.** Replace the empirical full-even overlap estimate by a proof-facing bound. This is one of
the Green/model inputs needed for the resonant degree-two part of RFBD.

Let

```text
F_N = span{e^{2 pi i n t}: -N <= n <= N},
E_+ = even projection on F_N,
U_u = finite interval/shift operator,       0 <= u <= 1,
a = 1-u.
```

The numerical quantity used in E72.220--E72.223 is

```text
||E_+ U_u E_+||_HS^2.
```

## Lemma

For all `N>=1` and `0<=u<=1`,

```text
||E_+ U_u E_+||_HS^2
<= (N+1)(1-u) + H_N/(2 pi),
```

where `H_N=sum_{n=1}^N 1/n`.

Equivalently, if `dim_even=N+1`,

```text
||E_+ U_u E_+||_HS^2
<= dim_even (1-u) + O(log N).
```

## Proof

Work on the normalized circle with Fourier basis indexed by `[-N,N]`. The interval/shift operator has
matrix coefficients

```text
(U_u)_{mn} = c_{n-m},
```

up to harmless unit phases, where `c_r` are Fourier coefficients of an interval of length `a=1-u`:

```text
c_0=a,
|c_r| <= min(a, 1/(pi |r|))       (r != 0).
```

Since `E_+` is an orthogonal projection,

```text
||E_+ U_u E_+||_HS^2
= Tr(E_+ U_u^* E_+ U_u E_+)
<= Tr(E_+ U_u^* U_u E_+).
```

Write `E_+=(I+R)/2`, with `R e_n=e_{-n}`. Then

```text
Tr(E_+ U_u^*U_u E_+)
= 1/2 Tr(U_u^*U_u) + 1/2 Tr(R U_u^*U_u).
```

The full trace is bounded by Parseval:

```text
Tr(U_u^*U_u)
= sum_{m,n=-N}^N |c_{n-m}|^2
<= (2N+1) sum_{r in Z} |c_r|^2
= (2N+1)a.
```

For the reflected trace, only the `m+n=0` Fourier differences enter. Hence

```text
|Tr(R U_u^*U_u)|
<= a + 2 sum_{n=1}^N |c_{2n}|
<= a + (1/pi) H_N.
```

Combining,

```text
Tr(E_+ U_u^*U_u E_+)
<= 1/2(2N+1)a + 1/2(a + H_N/pi)
= (N+1)a + H_N/(2pi).
```

This proves the bound.

## Numerical check

The probe verifies the bound directly on the same finite matrices:

```text
bound=(N+1)(1-u)+H_N/(2pi).
```

The bound is intentionally not sharp near the middle of the interval; its role is to be uniform,
zero-free, and proof-facing.

## Consequence for RFBD

Together with the projection identity of E72.220,

```text
||B^* U_u B||_HS^2 <= ||E_+ U_u E_+||_HS^2,
```

this gives the model overlap input

```text
||B^* U_u B||_HS^2
<= dim_even(1-u) + H_N/(2pi).
```

After model coercivity `lambda_min(C_model) >= c_C L^2`, the resonant degree-two energy is bounded by
positive prime-power sums:

```text
sum_{p^k<=e^L} (log p)^2/p^k * ((dim_even)(1-k log p/L)+H_N/(2pi)) / lambda_min(C_model)^2.
```

Thus the degree-two resonant channel is reduced to an elementary positive PNT estimate plus the
quadratic coercivity theorem.
