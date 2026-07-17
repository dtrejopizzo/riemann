# E72.81 -- Dual cofactor transport identity

**Date:** 2026-07-09.
**Role:** factor the bordered-minor certificate into a scalar transport identity involving three Cauchy
transforms.

## 0. From minors to a dual cofactor vector

In E72.79, write:

```text
R_x(s;z)=<a_s,C_E^(-1)b_x(z)>.
```

Let:

```text
y_{x,s}:=C_E^(-1)a_s,
g_{x,s}:=B_xy_{x,s}.
```

Then:

```text
R_x(s;z)=<g_{x,s},W_x(z)>.
```

The vector `g_{x,s}` carries the entire shorting, but it is independent of the root variable `z`.
Therefore the remaining `z`-dependence can be written explicitly.

## 1. Cauchy transforms

For an even vector `f`, define:

```text
C_{g,f}(z):=<g, S_z f>,
S_z=2z(z^2I-D^2)^(-1).
```

Also define:

```text
M_f(z):=<(zI-D)^(-1)1,f>.
```

The HPAC source is:

```text
W_x(z)=iS_zk_x-(exp(izL)-1)L^(-1)S_z1 M_h(z),
h_x=k_x-xi_x.
```

Thus the exact shorted residual is:

```text
R_x(s;z)
 = i C_{g,k}(z)
   - (exp(izL)-1)L^(-1) C_{g,1}(z) M_h(z).                    (DCT)
```

This identity holds off the mesh, without using the finite-root condition.

## 2. Root transport form

At a finite Weyl root:

```text
M_xi(tau_j)=0.
```

Since:

```text
M_h=M_k-M_xi,
```

we obtain:

```text
R_x(s;tau_j)
 = i C_{g,k}(tau_j)
   - (exp(i tau_jL)-1)L^(-1) C_{g,1}(tau_j) M_k(tau_j).        (RT)
```

Therefore EV-CERT is equivalent to the root transport annihilation:

```text
i C_{g,k}(tau_j)
 = (exp(i tau_jL)-1)L^(-1) C_{g,1}(tau_j) M_k(tau_j)
   + o(1)                                                     (RTA)
```

uniformly over the active finite roots and locally uniformly in `s`.

## 3. Why this is sharper than E72.80

E72.80 says the root remainder of a bordered minor must vanish. E72.81 identifies the actual
mechanism inside that minor:

```text
shorting vector g_{x,s}
    +
two model Cauchy channels C_{g,k}, C_{g,1}
    +
finite Weyl-null replacement M_h(tau_j)=M_k(tau_j).
```

So the remaining theorem no longer needs to speak about determinants. It can be stated as a scalar
transport law for the dual cofactor vector `g_{x,s}`.

## 4. Numerical verification

The companion script:

```text
E72_81_dual_cofactor_transport_probe.py
```

checks:

```text
<g,W_z>
 =
i C_{g,k}(z)
-(exp(izL)-1)L^(-1)C_{g,1}(z)M_h(z),
```

and the root replacement:

```text
M_h(tau_j)=M_k(tau_j).
```

Representative differences:

```text
lambda=8, tau=0.559:
  |direct|=1.080e-02, fact.diff=4.34e-19, root.diff=2.74e-16

lambda=10, tau=6.227:
  |direct|=3.566e-03, fact.diff=8.67e-19, root.diff=4.11e-14

lambda=16, tau=8.086:
  |direct|=8.907e-03, fact.diff=8.67e-19, root.diff=1.70e-16
```

## 5. Current minimal theorem

The scalar WRL resonance annihilation is reduced to:

```text
Dual cofactor root transport:
For g_{x,s}=B_xC_E^(-1)B_x^*r_s^even,

max_{tau_j}
| i C_{g,k}(tau_j)
  -(exp(i tau_jL)-1)L^(-1)C_{g,1}(tau_j)M_k(tau_j) | -> 0.
```

This is the most compressed non-circular statement currently obtained. It uses only:

```text
finite CCM divisor roots,
the prolate model vector k_x,
the shorted even dual cofactor vector g_{x,s},
and the exact HPAC boundary factor exp(i tau L)-1.
```

## 6. Status

```text
proved: the bordered-minor residual factors into the dual cofactor transport identity;
proved: at finite roots the displacement Mellin factor is model-only, M_h=M_k;
open:   prove the root transport annihilation uniformly.
```
