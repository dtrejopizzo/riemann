# E72.127 -- Minimal mass gate

**Date:** 2026-07-09.
**Role:** remove the unnecessary bad-subspace burden from the final scalar WRL route.

## 0. The point

E72.116--E72.126 developed a strong bad-subspace route:

```text
PFLB + BUP -> S-FIN -> MOP and top-mode annihilation.
```

This is sufficient, but it is not minimal.  The centered spectral-divergence theorem E72.108 shows
that the flux channel only needs bounded flux, not vanishing top singular energy.

Therefore the finite route can be compressed.

## 1. Minimal assumptions

Fix a compact Cauchy window `K`, a finite physical band `H`, and a finite root-height window `T`.
Let:

```text
Y_x(tau_j)
```

be the post-main packet, and let:

```text
m_xY_x(tau_j)
```

be the mass channel of the post-main cofactor.  Let `R_x` be the shorted pushforward of E72.112.

Assume:

```text
CGE-K:
the Cauchy-channel physical tail vanishes as in E72.120;

ROP:
sup_{tau_j<=T} ||R_xY_x(tau_j)|| = O(1);

MG:
sup_{tau_j<=T} |m_xY_x(tau_j)| -> 0.
```

Then scalar WRL resonance annihilation follows.

## 2. Proof

By E72.108, the post-main finite-band cofactor decomposes exactly as:

```text
phi_{x,H,tau_j}^{pm}
 = m_xY_x(tau_j)e_M + div_h Psi_{x,H,tau_j}.
```

The mass term contributes:

```text
|m_xY_x(tau_j)| sup_{s in K}|R_s(H)| -> 0
```

by `(MG)`.

For the divergence term, E72.109 identifies the centered flux with `R_xY_x(tau_j)` in the finite band:

```text
||Psi_{x,H,tau_j}||_2 = ||R_xY_x(tau_j)||_2.
```

Since the band `0<=d<=H` has `M=O_H(L)` mesh points and `h=2*pi/L`,

```text
h||Psi||_1 <= h sqrt(M)||Psi||_2
           <= C_H L^(-1/2)||R_xY_x(tau_j)||_2
           -> 0
```

by `(ROP)`.

E72.108 gives:

```text
D2_x^{pm}(H,s;tau_j)->0
```

uniformly for `s in K` and `tau_j<=T`.  Combining with `(CGE-K)` via E72.105 and E72.120 gives scalar
WRL resonance annihilation. `QED`

## 3. Relation to the stronger bad-subspace route

`BUP` remains a valid sufficient mechanism because it implies `(MG)` and can force top singular
energy to vanish.  But top singular energy is not needed for scalar WRL after the centered
summation-by-parts gain.

The current minimal endpoint is therefore:

```text
CGE-K + ROP + MG.
```

In the scale language of E72.122:

```text
ROP is exactly the scalar product bound sigma_1(R_x)||Y_x||=O(1).
```

So only one genuinely new estimate remains after the already separated Cauchy tail:

```text
MG:
m_xY_x(tau_j)->0.
```

## 4. Numerical status

E72.112 verifies `ROP` in the tested windows:

```text
E72.112 operator split probe
 lam   N roots  max||Y||   max||R||   max prod   maxFlux2  relCheck
   6  18     3 3.830e+01 2.578e-02  9.873e-01 5.504e-02   4.1e-16
   8  24     4 5.914e+01 1.877e-02  1.110e+00 6.287e-02   3.8e-16
  10  28     3 8.708e+01 9.900e-03  8.620e-01 3.929e-02   3.9e-16
  12  32     4 1.227e+02 8.450e-03  1.037e+00 2.291e-02   7.8e-16
  14  36     4 1.378e+02 4.607e-03  6.349e-01 2.312e-02   1.7e-16
```

E72.115 shows the mass itself decreasing:

```text
E72.115 mass alignment probe
 lam   N roots  max||Y||   ||m||    maxProd   max|mass|  maxRatio
   6  18     3 3.830e+01 1.96e-02 7.500e-01  9.332e-02 1.28e-01
   8  24     4 5.914e+01 1.09e-02 6.469e-01  4.973e-02 8.40e-02
  10  28     3 8.708e+01 6.17e-03 5.375e-01  4.051e-02 8.17e-02
  12  32     4 1.227e+02 4.92e-03 6.039e-01  2.100e-02 3.94e-02
  14  36     4 1.378e+02 2.37e-03 3.260e-01  1.601e-02 5.20e-02
```

## 5. Status

```text
proved: CGE-K + ROP + MG imply scalar WRL annihilation;
proved: the full bad-subspace/BUP route is stronger than needed for scalar WRL;
observed: ROP is stable and MG decreases in the finite harness;
open:   prove MG uniformly from the finite CCM root equation and post-main shorting.
```
