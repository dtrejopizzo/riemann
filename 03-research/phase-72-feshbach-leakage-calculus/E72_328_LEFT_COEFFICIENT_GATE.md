# E72.328 -- Left coefficient gate for the transformed packet equation

**Purpose.** Isolate the harmless-looking but load-bearing denominator in E72.326:

```text
mu+e_pole-2kappa_L.
```

The compact transformed route only needs this coefficient to have a polynomial lower bound. This gate
is independent of zeta zeros.

## 1. Source of the coefficient

E72.317 gives

```text
(mu+e_pole)G_x(z)
= transformed model/archimedean/prime terms.
```

E72.319 retains the endpoint renormalization in the packet Abel identity and obtains

```text
Arch_0(B_z)=2kappa_LG_x(z).
```

Thus the endpoint-renormalized equation has left coefficient

```text
Lambda_L:=mu+e_pole-2kappa_L.                         (1)
```

## 2. Required bound

The propagation lemma E72.326 needs:

```text
LCOEF:
|Lambda_L| >= c L^a
```

for some fixed `a>0`, uniformly in the pole-even windows under consideration.

The natural expected scale is `a=2`, inherited from the pole-even gap:

```text
mu >= c_mu L^2.                                      (GAP)
```

## 3. Sufficient zero-free conditions

`LCOEF` follows from:

```text
GAP:       mu >= c_mu L^2,
EP-SCALE:  |e_pole| <= C L^2,
K-SUB:     |kappa_L| <= C L^b with b<2,
NO-CANCEL: mu+e_pole is not tuned to 2kappa_L at L^2 scale.
```

In the expected pole-relative normalization, `e_pole` is already included as the model pole energy and
`mu` is the actual pole-even gap above that energy. The only new endpoint scalar is `kappa_L`, coming
from the finite-part difference between `WR` and the explicit trivial-lattice integral.

Thus the proof-facing sufficient version is:

```text
K-SUB:
kappa_L=O(log L) or O(1).
```

Then `LCOEF` follows from `GAP` for large `L`.

## 4. How to verify `K-SUB`

By E72.319,

```text
kappa_L=Arch_0(1),
```

where

```text
Arch_0(B)
= Ren int_0^L e^(y/2)B(y)/(2sinh y)dy - WR(B).
```

For `B=1`, both terms use the same finite-part subtraction at `y=0`. Therefore `kappa_L` is an
explicit scalar depending only on the chosen WR normalization:

```text
kappa_L
= Ren int_0^L e^(y/2)/(2sinh y)dy
 - [ 1/2(LOG4PI+gamma)
     + int_0^L (e^(y/2)-1)/(2sinh y)dy
     + 1/2 log(tanh(L/2)) ].
```

After cancellation of the common singular integral, this reduces to an elementary expression with at
most logarithmic growth.

## 5. Status

```text
closed: E72.330 proves kappa_L is an L-independent finite-part constant;
closed: left coefficient lower bound follows from the pole-even gap.
```

This gate is not arithmetic and does not involve the zero divisor.
