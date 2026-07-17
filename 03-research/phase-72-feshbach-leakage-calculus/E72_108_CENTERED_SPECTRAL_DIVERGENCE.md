# E72.108 -- Centered spectral divergence criterion

**Date:** 2026-07-09.
**Role:** split the post-main cofactor obstruction into an explicit mass channel and a flux channel.

## 0. Reason for the correction

E72.107 stated the clean zero-mass divergence gate:

```text
phi=div_h Psi,       h||Psi||_1 -> 0.
```

The first probe shows that the post-main cofactor has a small but nonzero finite mass:

```text
sum_n phi_n != 0
```

and that both the mass and the spectral flux appear to decrease.  Therefore the sharper finite theorem
should not hide the mass in a generic error.  It should split it explicitly.

## 1. Exact centered decomposition

For any finite band vector:

```text
phi=(phi_0,...,phi_M),
```

define its mass:

```text
m(phi)=sum_{n=0}^M phi_n.
```

Put the mass at the right endpoint and define:

```text
phi^0_n=phi_n,             0<=n<M,
phi^0_M=phi_M-m(phi).
```

Then:

```text
sum_n phi^0_n=0.
```

Define the canonical centered flux:

```text
Psi_{n+1/2}=sum_{j=0}^n phi^0_j,       0<=n<M,
Psi_{M+1/2}=0.
```

Then:

```text
phi^0_0      =  Psi_{1/2},
phi^0_n      =  Psi_{n+1/2}-Psi_{n-1/2},       1<=n<=M-1,
phi^0_M      = -Psi_{M-1/2}.
```

So every finite vector decomposes exactly as:

```text
phi = m(phi)e_M + div_h Psi(phi).                            (CSD)
```

No estimate has been used.

## 2. Exact pairing identity

Let:

```text
R_s(d)=s/(s^2-d^2).
```

Using E72.107 summation by parts on `phi^0`, we get:

```text
sum_{n=0}^M R_s(d_n)phi_n
 = m(phi)R_s(d_M)
   -sum_{n=0}^{M-1}Psi_{n+1/2}
      [R_s(d_{n+1})-R_s(d_n)].                              (CPAIR)
```

This is the exact finite Cauchy decomposition into:

```text
mass channel,
spectral flux channel.
```

## 3. Centered SDF theorem

### Theorem 72.108

Fix `H`, a compact Cauchy window `K`, and a finite root-height window `T`.  Let
`phi_{x,H,tau_j}^{pm}` be the post-main finite-band cofactor of E72.106.  Let:

```text
m_{x,H,tau_j}=m(phi_{x,H,tau_j}^{pm}),
Psi_{x,H,tau_j}=Psi(phi_{x,H,tau_j}^{pm}).
```

Assume:

```text
sup_{tau_j<=T}|m_{x,H,tau_j}| -> 0,                          (MASS)
sup_{tau_j<=T}h||Psi_{x,H,tau_j}||_1 -> 0,                   (FLUX)
```

and the same bounds for the one `s`-derivative channel.  Then:

```text
sup_{s in K,tau_j<=T}|D2_x^{pm}(H,s;tau_j)| -> 0.
```

### Proof

By `(CPAIR)`:

```text
|D2_x^{pm}|
 <= |m_{x,H,tau_j}| sup_{s in K}|R_s(H)|
    + C_{K,H}h||Psi_{x,H,tau_j}||_1.
```

The right side tends to zero by `(MASS)` and `(FLUX)`.  The derivative statement follows by replacing
`R_s` by `partial_sR_s`, whose endpoint value and mesh Lipschitz constant are uniformly bounded on
`K`. `QED`

## 4. What must now be proved

The post-main root transport theorem is reduced to two scalar finite estimates:

```text
MASS:
sum_n phi_{x,H,tau_j}^{pm}(n) -> 0,

FLUX:
h sum_{n<M}|sum_{j<=n}(phi_{x,H,tau_j}^{pm}(j)-m e_M(j))| -> 0.
```

Both are after:

```text
post-main subtraction,
Loewner commutator construction,
Feshbach shorting,
finite physical-band projection.
```

This is narrower than bounding the raw Chebyshev transforms `sigma_n^E` and narrower than proving
`||phi||->0`.

## 5. Interpretation

The mass channel is the only remaining scalar zero-frequency leakage of the post-main cofactor.  The
flux channel measures whether the rest of the cofactor is a discrete derivative invisible to Cauchy
tests at mesh scale.

This is the first version of the endpoint theorem where the finite numerical signal and the proof
mechanism match:

```text
D2pm decreases,
mass decreases,
h||flux||_1 decreases.
```

## 6. Status

```text
proved: every post-main cofactor splits exactly into mass plus centered spectral divergence;
proved: MASS + FLUX imply post-main finite-band root transport;
open:   prove MASS and FLUX from the integrated Loewner-Feshbach equations.
```
