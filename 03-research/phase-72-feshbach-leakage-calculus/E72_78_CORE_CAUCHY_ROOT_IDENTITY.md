# E72.78 -- Core Cauchy root identity

**Date:** 2026-07-08.
**Role:** identify the unshorted actual-divisor core as an exact divided difference of the finite Weyl
function.

## 0. Finite Weyl function

Let:

```text
m_x(z):=xi_x^T(zI-D)^(-1)1.
```

Since `xi_x` is even:

```text
m_x(z)=xi_x^T z(z^2I-D^2)^(-1)1.                                (EV-M)
```

At a finite root:

```text
P_x(tau_j)=0,
```

we have:

```text
m_x(tau_j)=0.                                                    (ROOT)
```

## 1. Hermitian Cauchy identity

The even Cauchy test is:

```text
r_s^even=s(s^2I-D^2)^(-1)1.
```

The actual-divisor core vector is:

```text
S_jxi_x=2tau_j(tau_j^2I-D^2)^(-1)xi_x.
```

With the Hilbert-space convention linear in the second variable:

```text
<r_s^even,S_jxi_x>
 = -2tau_j m_x(conjugate(s))/(conjugate(s)^2-tau_j^2).           (CR)
```

### Proof

Entrywise:

```text
<r_s^even,S_jxi_x>
 = sum_n conjugate( s/(s^2-d_n^2) )
         2tau_j/(tau_j^2-d_n^2) xi_n.
```

Therefore:

```text
<r_s^even,S_jxi_x>
 = 2tau_j conjugate(s)
   sum_n xi_n / ((conjugate(s)^2-d_n^2)(tau_j^2-d_n^2)).
```

Partial fractions give:

```text
1/((conjugate(s)^2-d^2)(tau_j^2-d^2))
 = [1/(tau_j^2-d^2)-1/(conjugate(s)^2-d^2)]
   /(conjugate(s)^2-tau_j^2).
```

Using `(EV-M)` and `(ROOT)`:

```text
sum_n xi_n/(tau_j^2-d_n^2)=m_x(tau_j)/tau_j=0,
sum_n xi_n/(conjugate(s)^2-d_n^2)=m_x(conjugate(s))/conjugate(s).
```

Substitution gives `(CR)`. `QED`

## 2. Meaning for CORE-C

CORE-C is not the unshorted identity `(CR)`. It is:

```text
<Q r_s^even,C_even^(-1)Q iS_jxi_x> -> 0.                         (CORE-C)
```

The root identity explains why the core is small but does not prove CORE-C by itself. The remaining
content is the Feshbach shorting:

```text
S_jxi_x
  -> Q S_jxi_x
  -> C_even^(-1)Q S_jxi_x.
```

Thus a proof of CORE-C must show that the shorted core is Weyl-invisible, not merely that
`m_x(tau_j)=0`.

## 3. Numerical check

The identity `(CR)` was checked against the finite harness. Representative absolute differences:

```text
lambda=8:
  tau=0.728  diff=4.34e-17
  tau=2.708  diff=1.31e-17
  tau=4.053  diff=1.33e-17

lambda=12:
  tau=0.825  diff=1.21e-19
  tau=2.135  diff=6.41e-16

lambda=20:
  tau=0.241  diff=2.62e-19
  tau=4.351  diff=2.06e-18
```

## 4. Status

```text
proved: the unshorted core pairing is an exact divided difference of m_x;
clarified: CORE-C requires additional Feshbach shorting, not just finite-root nullity;
open: prove Weyl invisibility of C_even^(-1)Q S_jxi_x.
```
