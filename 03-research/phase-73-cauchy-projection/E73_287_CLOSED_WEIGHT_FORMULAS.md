# E73.287 - Closed weight formulas

Date: 2026-07-14.

## 1. Purpose

E73.286 showed that finite-difference derivatives of `W_omega` do not recover
`V_omega` accurately enough.  E73.287 derives and verifies direct closed
formulas for the frequency weights:

```text
W_omega = W^A_omega-W^P_omega,
V_omega = V^A_omega-V^P_omega.
```

These are the weights needed for `BLOCK-FREQ-DIV`.

## 2. Prime weights

The finite Euler part is exact:

```text
W^P_omega
= sum_{p^k<=e^L} (log p)p^(-k/2)e^(i omega klog p),
```

and

```text
V^P_omega
= sum_{p^k<=e^L} (log p)p^(-k/2)(klog p)e^(i omega klog p).
```

No limiting argument is involved.

## 3. Archimedean weights

For the Dirichlet representative used in the eta-packet center:

```text
F^A[B]
= int_0^L B(y)(e^(y/2)+e^(-y/2))dy
 - int_0^L e^(y/2)B(y)/(2sinh y)dy,
```

the basis weights are:

```text
W^A_omega
= I_0(1/2+iomega)+I_0(-1/2+iomega)
 - sum_{r>=0} I_0(-(2r+1/2)+iomega),
```

and

```text
V^A_omega
= I_1(1/2+iomega)+I_1(-1/2+iomega)
 - sum_{r>=0} I_1(-(2r+1/2)+iomega),
```

where

```text
I_0(a)=int_0^L e^(ay)dy=(e^(aL)-1)/a,
```

and

```text
I_1(a)=int_0^L y e^(ay)dy
      =(e^(aL)(aL-1)+1)/a^2.
```

The `a=0` cases are interpreted by continuity.

## 4. Gauge issue

The full Weil representative differs from this Dirichlet representative on
the `W` block by terms proportional to `B(0)`.  In frequency coordinates this
is a constant shift of `W_omega`.  Since E73.236 proved:

```text
sum c_omega=0,
```

that difference is invisible for the APR eta-packets.  Thus the Dirichlet
representative is the correct proof-facing weight.

The probe confirms:

```text
raw W error      = constant gauge;
gauged W error   ~ L^(-14) to L^(-16);
V error          ~ L^(-13) to L^(-17).
```

## 5. Consequence

The next theorem can now be written with explicit finite formulas:

```text
BLOCK-FREQ-DIV:
sum c_omega (W^A_omega-W^P_omega-alpha_L)
= -sum l_omega (V^A_omega-V^P_omega-beta_L)
   + O_M(L^(-M)).
```

Here `alpha_L,beta_L` are arbitrary constant gauges justified by:

```text
sum c_omega=sum l_omega=0.
```

All objects are now explicit finite sums plus elementary archimedean series.

## 6. Status

```text
proved: finite prime formulas for W,V;
proved: elementary/series archimedean formulas for W,V;
verified: formulas match the reference functional modulo the allowed W gauge;
open: prove BLOCK-FREQ-DIV from these explicit formulas and eta-packet
      coefficient relations.
```
