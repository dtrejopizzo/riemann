# E72.298 -- Double-commutator form of FORM-DCB

**Purpose.** Convert `FORM-DCB` into an exact finite kernel identity. This is the first place where the
high Fourier obstruction of E72.295 disappears for structural reasons.

## 1. Algebraic identity

Let `C=C_E`, let `C xi=mu xi`, and let `S=S_tau` be the diagonal self-adjoint operator with entries

```text
s_m(tau)=1/(tau-d_m)+1/(-tau-d_m)=2d_m/(tau^2-d_m^2).
```

Then

```text
<Sxi,(C-mu I)Sxi>
= (1/2)<xi,[S,[C,S]]xi>.                              (1)
```

Indeed,

```text
[S,[C,S]]=2SCS-S^2C-CS^2.
```

Taking the expectation against `xi` and using `Cxi=mu xi` gives

```text
<xi,[S,[C,S]]xi>
=2<Sxi,CSxi>-2mu||Sxi||^2
=2<Sxi,(C-mu I)Sxi>.
```

## 2. Entrywise form

Since `S` is diagonal,

```text
([S,[C,S]])_{mn}=-(s_m-s_n)^2 C_{mn}.
```

Therefore

```text
FORM(tau)
:=<S_tau xi,(C_E-mu I)S_tau xi>
= -1/2 sum_{m,n} xi_m xi_n (s_m-s_n)^2 C_E(m,n).       (2)
```

The diagonal terms vanish automatically. In particular, the high-mode obstruction of E72.295, which
lived on `Q_y(m,m)`, is invisible to `FORM-DCB`.

The scalar pole shift also vanishes: `-e_pole I` commutes with `S_tau`, so it contributes nothing to
(2).

## 3. Model/arithmetic split

Write

```text
C_E = C_model + Delta_arith,
Delta_arith = - sum_{r<=e^L} Lambda(r)r^(-1/2) Q_{log r}.
```

Then

```text
FORM(tau)=FORM_model(tau)+FORM_arith(tau),
```

with

```text
FORM_model(tau)
= -1/2 sum_{m,n} xi_m xi_n (s_m-s_n)^2 C_model(m,n),
```

and

```text
FORM_arith(tau)
=  1/2 sum_{r<=e^L} Lambda(r)r^(-1/2)
      sum_{m,n} xi_m xi_n (s_m-s_n)^2 Q_{log r}(m,n).  (3)
```

Equation (3) is the finite arithmetic identity to prove, not a spectral norm statement.

## 4. Exact DCB norm identity

The full directional commutator bound itself is

```text
||[C_E,S_tau]xi||^2
= sum_m | sum_n C_E(m,n)(s_n-s_m)xi_n |^2.             (4)
```

This is a second finite identity, stronger than (2). It contains one commutator difference in each
factor. The previous global estimates tried to control `C_E` before this difference was inserted; (4)
shows that this was the wrong order.

## 5. Correct finite targets

The corrected finite targets are:

```text
FORM-DCB:
sup_{tau_j<=H} |FORM(tau_j)| <= C_H L^4,
```

and, preferably, the direct stronger target

```text
DCB-square:
sup_{tau_j<=H} sum_m |sum_n C_E(m,n)(s_n-s_m)xi_n|^2 <= C_H L^6.
```

`DCB-square` implies `DCB` with `alpha=3`, which is enough for compact-root HPAC decay.

## 6. Next analytic inequality

The next proof must start from (3) or (4). The admissible order is:

```text
insert the commutator difference,
use the cancellation of the diagonal,
only then apply PNT/Abel summation or model kernel bounds.
```

Any estimate that takes absolute values of `Delta_arith` before inserting `s_m-s_n` recreates the
false APCB obstruction.

E72.299 isolates the arithmetic scalar kernel

```text
F_tau(y)=sum_{m,n}xi_mxi_n(s_m-s_n)^2Q_y(m,n),
```

proves `F_tau(0)=F_tau(L)=0`, and gives the exact Abel identity for `FORM_arith`.
