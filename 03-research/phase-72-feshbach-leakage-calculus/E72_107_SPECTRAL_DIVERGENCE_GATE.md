# E72.107 -- Spectral divergence gate for the post-main cofactor

**Date:** 2026-07-09.
**Role:** replace norm-smallness of the post-main cofactor by a finite summation-by-parts identity.

## 0. Why another gate is needed

E72.92 showed that the transported cofactor is not norm-small.  E72.94 showed that low moments do not
vanish for free.  E72.105--E72.106 corrected the source to the post-main object:

```text
Z_x^{pm}(tau)=(2/(L sqrt(x)))K_x^E(tau)k_x.
```

The remaining finite-band defect is:

```text
D2_x^{pm}(H,s;tau_j)
 = <r_s^even,phi_{x,H,tau_j}^{pm}>,
phi_{x,H,tau}^{pm}
 = B_xC_E^(-1)B_x^*1_{|d|<=H}Z_x^{pm}(tau).
```

The correct substitute for norm-smallness is:

```text
phi_{x,H,tau}^{pm} is a spectral divergence with small flux.
```

This uses the Cauchy form of `r_s^even` and gains one mesh factor by summation by parts.

## 1. Mesh notation

On the even physical band write:

```text
0=d_0<d_1<...<d_M<=H,       h=2*pi/L.
```

For the two-sided even Cauchy vector the relevant scalar test is:

```text
R_s(d_n)=s/(s^2-d_n^2),
```

with `s` in a compact Cauchy window `K` separated from the real band.

For a band vector `phi=(phi_0,...,phi_M)`, define a flux
`Psi=(Psi_{1/2},...,Psi_{M+1/2})` by:

```text
phi_0      =  Psi_{1/2},
phi_n      =  Psi_{n+1/2}-Psi_{n-1/2},       1<=n<=M-1,
phi_M      = -Psi_{M-1/2}+Psi_{M+1/2}.
```

We impose the boundary condition:

```text
Psi_{M+1/2}=0.                                             (BD)
```

Then:

```text
sum_{n=0}^M phi_n = 0.
```

The zero-mass condition is natural: constants are invisible to the commutator
`[D,K_x^E]=[Sigma_x^E,11^T]` after the Feshbach centering.

## 2. Exact summation-by-parts identity

### Lemma 72.107.1

If `phi=div_h Psi` with `(BD)`, then:

```text
sum_{n=0}^M R_s(d_n)phi_n
 = -sum_{n=0}^{M-1} Psi_{n+1/2}[R_s(d_{n+1})-R_s(d_n)].       (SBP)
```

### Proof

Insert the definition of `phi`:

```text
sum R_n phi_n
 = R_0Psi_{1/2}
   +sum_{n=1}^{M-1}R_n(Psi_{n+1/2}-Psi_{n-1/2})
   +R_M(-Psi_{M-1/2})
```

after using `Psi_{M+1/2}=0`.  Collect the coefficient of each `Psi_{n+1/2}`.  It is
`R_n-R_{n+1}`.  This gives `(SBP)`. `QED`

## 3. Cauchy gain

For `s` in a compact window `K` with positive distance from `[-H,H]`, the derivative:

```text
partial_d R_s(d)=2sd/(s^2-d^2)^2
```

is uniformly bounded on `0<=d<=H`.  Hence:

```text
|R_s(d_{n+1})-R_s(d_n)| <= C_{K,H}h.
```

Combining with `(SBP)`:

```text
|<r_s^even,phi>| <= C_{K,H}h ||Psi||_1.                      (GAIN)
```

The same bound holds after one `s`-derivative because `partial_sR_s(d)` has the same uniform Lipschitz
property on the chosen window.

## 4. Spectral Divergence Forcing criterion

### Theorem 72.107 -- SDF implies post-main root transport

Fix `H`, a compact Cauchy window `K`, and a finite root-height window `T`.  Suppose that for every
finite root `tau_j<=T` the post-main cofactor admits:

```text
phi_{x,H,tau_j}^{pm}=div_h Psi_{x,H,tau_j}+eps_{x,H,tau_j},
```

with:

```text
sup_{tau_j<=T} h ||Psi_{x,H,tau_j}||_1 -> 0,                 (FLUX)
sup_{s in K,tau_j<=T}|<r_s^even,eps_{x,H,tau_j}>| -> 0,       (ERR)
```

and the same two estimates after one `s`-derivative.  Then:

```text
sup_{s in K,tau_j<=T}|D2_x^{pm}(H,s;tau_j)| -> 0.
```

### Proof

Use:

```text
D2_x^{pm}(H,s;tau_j)
 = <r_s^even,phi_{x,H,tau_j}^{pm}>.
```

Apply `(GAIN)` to the divergence part and `(ERR)` to the remainder:

```text
|D2_x^{pm}|
 <= C_{K,H}h||Psi_{x,H,tau_j}||_1
    + |<r_s^even,eps_{x,H,tau_j}>|.
```

The right side tends to zero uniformly.  The differentiated statement is identical with
`R_s` replaced by `partial_sR_s`. `QED`

## 5. Why this is not the incoherent ceiling

The incoherent ceiling estimates:

```text
sum_n |sigma_n^E|,
sum_n |dot_sigma_n^E|.
```

SDF estimates instead the cumulative flux of the **already paired and shorted** post-main cofactor:

```text
phi_{x,H,tau}^{pm}
 = B_xC_E^(-1)B_x^*1_{|d|<=H}(2/(L sqrt(x)))K_x^E(tau)k_x.
```

The possible cancellation is therefore allowed to use all three structures at once:

```text
post-main Chebyshev discrepancy,
integrated Loewner commutator,
Feshbach shorting.
```

This is exactly what the earlier absolute or termwise estimates did not see.

## 6. New remaining theorem

The current mathematical target is:

```text
Post-main Spectral Divergence:
phi_{x,H,tau_j}^{pm}
 = div_h Psi_{x,H,tau_j}+eps_{x,H,tau_j}
```

with `(FLUX)` and `(ERR)` uniformly on finite root-height windows, without using the limiting zeta
zeros.

If this is proved, then E72.105 gives scalar WRL resonance annihilation.

## 7. Status

```text
proved: spectral divergence with h||Psi||_1=o(1) forces post-main D2->0;
proved: the proof uses only finite summation by parts and Cauchy analyticity;
open:   derive the SDF decomposition from [D,K_x^E]=[Sigma_x^E,11^T] and the Feshbach equation.
```

## 8. First diagnostic

The companion script:

```text
E72_107_spectral_divergence_probe.py
```

constructs `Z_x^{pm}`, shortens it through `C_E^(-1)`, and reports:

```text
max |D2pm|,
max mass=sum phi,
max h||flux||_1,
max ||phi||.
```

Representative output:

```text
E72.107 spectral-divergence probe for post-main cofactor
 lam   N roots  max|D2pm|    max|mass|   max h||flux||1   max ||phi||
   6  18     3  1.607e-02   9.332e-02       1.627e-01    6.279e-02
   8  24     4  8.291e-03   4.973e-02       1.952e-01    2.091e-02
  10  28     3  5.647e-03   4.051e-02       1.006e-01    2.184e-02
  12  32     4  4.960e-03   2.100e-02       6.499e-02    9.781e-03
```

The flux is computed on the compact physical band, with the mass placed at the band endpoint.  This is
the correct finite version of E72.107; zero-padding outside the band gives an artificial plateau and
overestimates the flux.  Exact zero mass is still too strict at finite `x`, so the right criterion
includes a small mass channel plus the spectral flux channel.
