# P76.065 - Radical, Fourier tail and limit-point split

## Full radical identity

Let `k=E(h)` be the full Connes/Riemann kernel.  In the explicit-formula
spectral representation of the Weil bilinear distribution,

```text
Q_W(k,phi)=sum_rho K(rho) Phi_phi(rho).
```

The transform `K` contains the completed factor `Xi`, so `K(rho)=0` on the
complete zeta divisor, including any hypothetical off-critical zeros.
Therefore

```text
Q_W(k,phi)=0                                    (RFL-1)
```

for every admissible test vector.  This radical identity is unconditional
with respect to RH.

## Physical and Fourier truncation

On the centered interval `[-L/2,L/2]`, let `k_L` be the localized/prolate
kernel and `c_n(L)` its Fourier coefficients.  Repeated integration by parts
gives, for every fixed `M`,

```text
|c_n(L)|
 <=C_M(L)(1+|n|)^(-M)+Endpoint_M(L)/|n|.        (RFL-2)
```

The Riemann kernel and its derivatives have double-exponential physical
tails; hence `Endpoint_M(L)->0` faster than every power along the prolate
localization.  The cell overlap bound

```text
||Q_y||<=2(1-y/L)
```

then converts `(RFL-2)` into a signed Fourier-tail estimate for every fixed
row window.  P76.064 certifies the predicted cancellation numerically.

These estimates explain why `M_{L,N}P_N k_L` is asymptotically shell
supported plus a rapidly decreasing interior remainder.

## Remaining limit-point theorem

Tail smallness alone does not identify the normalized finite boundary
solution because the bordered inverse has an enormous ambient norm
(P76.061).  What remains is uniqueness in the directional topology:

```text
SAFE-LIMIT-POINT:
among l2 solutions of the infinite rectangular CCM equation, the condition
r_{z_0}v=1 selects a unique safe Cauchy transform, namely that of k_L.
```

Equivalently, every normalized finite boundary solution converges to `k_L`
in safe ratios, even if vector-norm convergence is unavailable.

`SAFE-LIMIT-POINT` plus `RDP-SHELL` proves `SAFE-PROLATE-BRIDGE`.  Connes's
transform convergence and P76.034 then give Omega7.

This is the current sharp endpoint.  It is weaker than simplicity of the
full ground eigenvector: only uniqueness of its safe Cauchy transform is
required.
