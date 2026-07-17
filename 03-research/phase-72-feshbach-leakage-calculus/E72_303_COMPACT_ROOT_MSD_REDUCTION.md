# E72.303 -- Compact-root reduction to MSD-FORM

**Purpose.** Package the corrected compact-root route after E72.295--E72.302. This is the current
load-bearing theorem stack from the finite Mellin spectral identity to HPAC decay.

## 1. Inputs already reduced to explicit identities

For each finite Weyl root `tau_j <= H`, define

```text
S_tau = (tau I-D)^(-1)+(-tau I-D)^(-1),
F_tau(y)=sum_{m,n}xi_mxi_n(s_m-s_n)^2Q_y(m,n).
```

The following are exact:

```text
F_tau(0)=F_tau(L)=0,
```

```text
<S_tau xi,(C_E-mu I)S_tau xi>
= -1/2 sum_{m,n}xi_mxi_n(s_m-s_n)^2C_E(m,n),
```

and

```text
FORM_actual(tau)=ARCH_tau - 1/2 PNTERR_tau,
```

where

```text
ARCH_tau=1/2 int_0^L e^(-5y/2)/(1-e^(-2y))F_tau(y)dy.
```

After E72.305, the arithmetic/error plus archimedean bookkeeping has the compact spectral form

```text
FORM_actual(tau)=-(1/2)sum_rho M_tau(rho-1/2),
```

with

```text
M_tau(z)
= (1-e^(zL))
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [Phi_z(d_m)-Phi_z(d_n)]/[pi(n-m)],
Phi_z(d)=d/(z^2+d^2).
```

## 2. Compact-root theorem

Assume, uniformly for `tau_j<=H`:

```text
GAP:        mu >= cL^2,
VBG:        ||S_tau_j xi||=O_H(L),
NZ-MSD-FORM: |sum_rho M_tau_j(rho-1/2)| <= C_H L^4.
```

Then

```text
<S_tau_j xi,(C_E-mu I)S_tau_j xi> = O_H(L^4).          (FORM-DCB)
```

If in addition either

```text
EFF-SUP:  S_tau_j xi has effective C_E support O_H(L^2),
```

or the stronger direct square estimate

```text
DCB-square:
||[C_E,S_tau_j]xi||^2
= sum_m |sum_n C_E(m,n)(s_n-s_m)xi_n|^2 <= C_H L^6
```

holds, then

```text
||[C_E,S_tau_j]xi|| = O_H(L^3).                       (DCB)
```

This is enough for the compact-root commutator contribution in the inverse-collapse identity, because

```text
mu^(-1)||a_s^perp||||C_E^(-1)|| ||[C_E,S_tau_j]xi||
= O(L^(-2))O_K(L^(1/2))O(L^(-2))O_H(L^3)
= O_{K,H}(L^(-1/2)).
```

The diagonal contribution was already closed by the Cauchy-factor identity and VBG. Therefore:

```text
GAP + VBG + NZ-MSD-FORM + (EFF-SUP or DCB-square)
=> fixed-height compact-root HPAC decay.
```

After E72.310--E72.311, the preferred replacement for `NZ-MSD-FORM` is the scalar numerator form
`RNS`: write the finite Cauchy transform as `C_x(w)=P_x(w)/D_x(w)`, reduce by pole-even parity to the
height-plane numerator `p_x(r)`, and prove the rotated bound

```text
R_tau_j * sum_rho
  (1-e^((rho-1/2)L))
  ((rho-1/2)tau_j^2)/(tau_j^2+(rho-1/2)^2)
  p_x(-(rho-1/2)^2)/Delta_x(rho-1/2)
= O_H(L^5).
```

This is no longer a matrix estimate. It is a finite scalar contour/residue theorem.

## 3. What NZ-MSD-FORM must supply

The finite Mellin spectral divisibility is now precisely:

```text
NZ-MSD-FORM:
sum_rho M_tau(rho-1/2) = O_H(L^4),
```

where `M_tau` is the closed divided-difference transform above.

Equivalently, every off-line zero contribution must be annihilated by the finite transform
`M_tau(z)` at `z=rho-1/2`, up to the polynomial `L^4` budget. This is the exact point where scalar WRL
divisibility enters the compact-root proof.

## 4. Remaining outside this compact-root theorem

This theorem does not yet close the full Phase 72 route. The remaining gates are:

```text
1. GAP as an analytic model theorem.
2. NZ-MSD-FORM as the finite Mellin spectral divisibility identity.
3. EFF-SUP or DCB-square.
4. Corrected HPAC source theorem.
5. High-root tail beyond fixed H.
6. Transport gates CGE-K, ROP, MSB.
7. Bordered-minor divisibility connecting the compact-root theorem to scalar WRL.
```

But the former global APCB/UCB branch is no longer part of the proof.

E72.304 sharpens `ARCH-FORM + MSD-FORM`: both are values of the same finite Mellin transform `M_tau`.
The archimedean residual is the shifted trivial-zero lattice

```text
ARCH_tau=1/2 sum_{k>=0} M_tau(-(5/2+2k)).
```

The next target is the unified explicit-formula bookkeeping identity `UMSD-FORM`.

E72.305 proves the bookkeeping identity: the shifted trivial-zero lattice cancels `ARCH_tau` exactly.
Thus the compact FORM channel is

```text
FORM_actual(tau)=-(1/2)sum_rho M_tau(rho-1/2),
```

with the sum over nontrivial zeros in the symmetric explicit-formula sense.

E72.306 rewrites this as the normalized condition

```text
sum_rho (1-e^((rho-1/2)L))N_tau(rho-1/2)=O_H(L^4),
```

where `N_tau=M_tau/(1-e^(zL))` is the finite divided-difference transform with removable mesh
singularities.

E72.307 gives the operator form

```text
N_tau(z)=(2/L)<xi,[S_tau,[L_z,S_tau]]xi>,
```

with `L_z` the Loewner matrix of `Phi_z(d)=d/(z^2+d^2)`.

E72.308 factors this Loewner matrix and gives the rank-two scalar form

```text
N_tau(z)=-(4/L)(z^2U_0(z)U_2(z)+V_1(z)^2).
```

E72.309 uses the finite Weyl root relation to collapse this to

```text
N_tau(z)= -16 z^2 tau^2/(L(tau^2+z^2)) U_0(z)R_tau,
R_tau=sum_m xi_m/(tau^2-d_m^2)^2.
```

E72.310 identifies `U_0(z)=iC_x(iz)/z`, where

```text
C_x(w)=sum_m xi_m/(w-d_m).
```

Thus the compact NZ-MSD target is a Mellin-Cauchy condition on `C_x(i(rho-1/2))`.
