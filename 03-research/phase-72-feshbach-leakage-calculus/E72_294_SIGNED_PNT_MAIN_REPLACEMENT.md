# E72.294 -- Signed PNT-main replacement for H-GERSH

**Purpose.** Correct the next analytic target. The absolute high-band Gershgorin estimate from
E72.291 is too crude as an asymptotic theorem: it destroys the sign of the PNT main term. The right
high-band statement is a signed decomposition

```text
Delta_arith = Delta_main + Delta_rem,
```

where the full-translation component of `Delta_main` is non-positive on the Fourier mesh and only the
positive part of `Delta_rem` must be bounded after paying a pure one-sided boundary compression cost.
More precisely, the full-translation main symbol is non-positive for `Delta_arith`; the one-sided
finite operator differs from it by a model boundary term.

## 1. Closed formula for the autocorrelation cell

For the Fourier mesh

```text
e_m(t)=L^(-1/2) exp(2pi i m t/L),        omega_m=2pi m/L,
```

E72.285 gives

```text
<v,Q_yv> = 2 Re int_0^(L-y) f_v(t+y) overline(f_v(t)) dt.
```

Therefore the matrix entries are exactly

```text
Q_y(m,m) = 2(1-y/L) cos(omega_m y),
```

and, for `m != n`,

```text
Q_y(m,n)
= [sin(omega_m y)-sin(omega_n y)]/[pi(n-m)].
```

This is the formula implemented in E72.158. No spectral input is hidden here.

## 2. Why absolute H-GERSH is the wrong analytic target

The arithmetic perturbation is

```text
Delta_arith = - sum_{n<=exp(L)} Lambda(n)n^(-1/2) Q_{log n}.
```

If one applies absolute row sums directly, the diagonal contribution already contains

```text
sum_{n<=exp(L)} Lambda(n)n^(-1/2) |2(1-log n/L)cos(omega_m log n)|.
```

By the PNT main density this has natural size comparable to

```text
int_0^L e^(y/2)(1-y/L)|cos(omega_m y)| dy,
```

which is of exponential scale in `L`, not `L^2`, for any fixed mesh frequency band
`|omega_m|>=4`. Thus an absolute Gershgorin proof cannot be the asymptotic mechanism behind APCB.
Its small numerical size in the current windows is not a uniform theorem.

This is not a failure of APCB; it is a failure of the proof target. The sign of the PNT main term is
load-bearing.

## 3. PNT-main operator

Replace the prime measure by its main density:

```text
sum Lambda(n)n^(-1/2) F(log n)
  ~ int_0^L e^(y/2)F(y) dy.
```

Define the main autocorrelation operator

```text
M_L := int_0^L e^(y/2) Q_y dy,
Delta_main := -M_L.
```

For a mesh function `f(t)=L^(-1/2)sum v_m exp(omega_m i t)`, one has

```text
<v,M_L v>
= 2 Re int_0^L e^(y/2) int_0^(L-y) f(t+y)overline(f(t)) dt dy.
```

Changing variables `r=t+y` gives

```text
<v,M_L v>
= 2 Re int_{0<=t<=r<=L} e^((r-t)/2) f(r)overline(f(t)) dt dr.
```

Set `g(t)=e^(-t/2)f(t)`. Then

```text
e^((r-t)/2) f(r)overline(f(t)) = e^r g(r)overline(g(t)).
```

Hence

```text
<v,M_L v>
= 2 Re int_0^L e^r g(r) [int_0^r overline(g(t))dt] dr.
```

This formula is not manifestly positive. However, on the exact Fourier mesh the full-line symbol of
the same main translation is explicit:

```text
P_main(omega_m)
 = int_0^L e^(y/2) exp(i omega_m y) dy
 = (e^(L/2)-1)/(1/2+i omega_m),
```

because `exp(i omega_m L)=1`. Therefore

```text
Re P_main(omega_m)
 = (e^(L/2)-1) * (1/2)/((1/2)^2+omega_m^2) > 0.
```

The full translation main contribution to `Delta_arith` is consequently non-positive:

```text
-2 Re P_main(omega_m) <= 0.
```

The finite one-sided compression differs from this diagonal full-translation main by boundary
Hankel terms. These boundary terms are model/geometric, not arithmetic.

## 4. Correct high-band theorem

The high-band APCB estimate should be restated as:

```text
SIGNED-HIGH:
lambda_max(P_high Delta_arith P_high)_+
 <= lambda_max(P_high Delta_rem P_high)_+ + O(L^2),
```

where

```text
Delta_rem
= - sum_{n<=exp(L)} Lambda(n)n^(-1/2)Q_{log n}
   + int_0^L e^(y/2)Q_y dy,
```

and the `O(L^2)` term is the boundary compression cost between the one-sided main operator and its
negative full-translation diagonal part.

Equivalently, the old `H-GERSH` should be replaced by:

```text
H-SIGNED(C):
lambda_max(P_high Delta_rem P_high)_+ <= C L^2
after subtracting the signed PNT-main operator.
```

This keeps the coherent sign that absolute row sums erased.

## 5. What must now be proved

The new analytic proof target has two parts.

### Lemma A: boundary cost

For the high-band projection used in E72.290,

```text
lambda_max(
  P_high[-M_L - T_main^full]P_high
)_+ <= C_b L^2,
```

where `T_main^full` is the diagonal full-translation main operator with symbol
`-2 Re P_main(omega_m)`.

This is a pure model estimate. It should follow from the explicit formula for `Q_y(m,n)` and the
`1/|m-n|` off-diagonal denominator after high-band projection.

### Lemma B: arithmetic remainder

For every high-band vector `v`,

```text
| <v,Delta_rem v>_+ | <= C_r L^2 ||v||^2.
```

This is the real arithmetic input. It is strictly sharper than PNT error in a fixed scalar frequency:
the kernel family and high-band projection must be used before any absolute values are taken.

## 6. Consequence for the Phase 72 route

The APCB block package becomes

```text
LOW-FIN + H-SIGNED + CROSS-HS => APCB.
```

The previous row-sum `H-GERSH` remains a finite-window diagnostic, but it is not the asymptotic proof
target. The corrected route preserves the sign of the PNT main term and puts the remaining difficulty
exactly where it belongs: a compressed, high-band arithmetic remainder estimate.
