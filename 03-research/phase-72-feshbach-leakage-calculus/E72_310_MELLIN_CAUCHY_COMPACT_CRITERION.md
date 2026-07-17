# E72.310 -- Mellin-Cauchy compact criterion

**Purpose.** Rewrite the root-reduced `NZ-MSD` target of E72.309 in terms of the finite Cauchy
transform of the actual even ground vector. This is the most compact scalar form of the compact-root
Mellin obstruction.

## 1. Finite Cauchy transform

Define

```text
C_x(w):=sum_m xi_m/(w-d_m).
```

Because `xi_m=xi_-m`, the paired sum gives

```text
C_x(iz)
= sum_m xi_m/(iz-d_m)
= -iz sum_m xi_m/(z^2+d_m^2).
```

Therefore

```text
U_0(z)=sum_m xi_m/(z^2+d_m^2)= i C_x(iz)/z.          (1)
```

The finite Weyl roots are the real zeros of the same Cauchy transform:

```text
C_x(tau)=0.
```

Thus the compact MSD obstruction is controlled by the Cauchy transform on the rotated points
`w=i(rho-1/2)`.

## 2. Rank-one NZ-MSD in Cauchy form

E72.309 gives

```text
N_tau(z)= -16 z^2 tau^2/(L(tau^2+z^2)) U_0(z)R_tau,
```

where

```text
R_tau=sum_m xi_m/(tau^2-d_m^2)^2.
```

Using (1),

```text
N_tau(z)
= -16 i z tau^2/(L(tau^2+z^2)) C_x(iz) R_tau.       (2)
```

Substituting into the normalized nontrivial-zero target gives:

```text
NZ-MSD-Cauchy:
R_tau * sum_rho
  (1-e^((rho-1/2)L))
  ((rho-1/2) tau^2)/(tau^2+(rho-1/2)^2)
  C_x(i(rho-1/2))
= O_H(L^5).                                         (3)
```

The constant factor `-16i/L` is absorbed into the `L^5` budget.

## 3. Packet version

For an off-line shifted packet

```text
z, -z, conjugate(z), -conjugate(z),
```

the packet contribution in (3) is determined by

```text
P_tau(z)
= (1-e^(zL)) z tau^2/(tau^2+z^2) C_x(iz)
 + (1-e^(-zL))(-z)tau^2/(tau^2+z^2) C_x(-iz)
 + conjugates.
```

The pointwise packet pressure is

```text
P_tau(z)=O_H(L^5 e^0/R_tau)
```

or, for `Re z>0`, exponential suppression of the dominant term unless the packet symmetry cancels it:

```text
C_x(iz)=O_H(L^5 e^(-Re(z)L)/R_tau)
```

after the common rational factor is accounted for.

## 4. Final compact-root scalar target

The compact root theorem can now use:

```text
MC-NZ:
sup_{tau_j<=H}
|R_tau_j * sum_rho
  (1-e^((rho-1/2)L))
  ((rho-1/2)tau_j^2)/(tau_j^2+(rho-1/2)^2)
  C_x(i(rho-1/2))|
<= C_H L^5.
```

Then `NZ-MSD` follows, hence by E72.303:

```text
GAP + VBG + MC-NZ + (EFF-SUP or DCB-square)
=> fixed-height compact-root HPAC decay.
```

## 5. Reading

The compact-root Mellin obstruction has been reduced to one finite Cauchy transform:

```text
C_x(w)=sum_m xi_m/(w-d_m).
```

The same function has zeros at the finite Weyl roots `tau`; scalar WRL demands controlled values at
the rotated off-line spectral points `w=i(rho-1/2)`.

This is the current sharpest finite scalar formulation of the compact-root branch.
