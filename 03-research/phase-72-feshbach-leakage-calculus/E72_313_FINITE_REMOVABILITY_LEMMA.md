# E72.313 -- Finite removability lemma for the RNS contour

**Purpose.** Prove the finite algebraic part `REM` left open in E72.312. This is a closed lemma:
the contour integrand has no finite residues coming from the Fourier mesh or from the kinematic
denominator at an active finite Weyl root.

## 1. Work in the unreduced Cauchy form

For this lemma it is cleaner not to use the parity-reduced quotient. Use the exact E72.310 factor:

```text
F_tau(s)
= (1-e^(zL)) z tau^2/(tau^2+z^2) C_x(iz),
z=s-1/2,
C_x(w)=sum_m xi_m/(w-d_m).
```

The contour integrand is

```text
F_tau(s) Xi'(s)/Xi(s).
```

Only the finite poles of `F_tau` matter for `REM`.

## 2. Mesh poles are removable

The Cauchy transform has a possible simple pole when

```text
iz=d_m,
```

that is,

```text
z=-i d_m.
```

The Fourier mesh is

```text
d_m=2pi m/L.
```

At `z_m=-i d_m`,

```text
e^(z_m L)=e^(-i d_m L)=e^(-2pi i m)=1.
```

Hence

```text
1-e^(zL)
```

has a simple zero at `z=z_m`, since its derivative is `-L e^(z_m L)=-L`.

Near `z_m`,

```text
C_x(iz)=xi_m/(iz-d_m)+holomorphic
      =xi_m/(i(z-z_m))+holomorphic.
```

Therefore

```text
(1-e^(zL))C_x(iz)
```

is holomorphic at `z_m`. Explicitly its limiting value is

```text
lim_{z->z_m}(1-e^(zL))C_x(iz)
= iL xi_m.
```

Thus every Fourier-mesh pole is removable.

## 3. Kinematic poles are removable at active finite roots

The factor

```text
z tau^2/(tau^2+z^2)
```

has possible simple poles at

```text
z=i tau,        z=-i tau.
```

At `z=-i tau`,

```text
iz=tau,
```

so the finite Weyl root equation gives

```text
C_x(iz)=C_x(tau)=0.
```

At `z=i tau`,

```text
iz=-tau.
```

Since the pole-even symmetry gives `C_x(-w)=-C_x(w)`, the same root equation gives

```text
C_x(iz)=C_x(-tau)=-C_x(tau)=0.
```

Therefore both kinematic poles are removable.

## 4. Consequence

For every active finite Weyl root `tau` which is not itself a Fourier mesh pole, the function

```text
F_tau(s)
```

is holomorphic at:

```text
all Fourier-mesh Cauchy poles,
z=i tau,
z=-i tau.
```

Hence the finite-pole residue term in E72.312 vanishes:

```text
sum_{a pole of F_tau}
Res_{s=a} F_tau(s)Xi'(s)/Xi(s)=0.
```

The RNS contour identity is therefore exactly

```text
sum_{rho in R_T} m_rho F_tau(rho)
= (1/2pi i) int_{partial R_T} F_tau(s)Xi'(s)/Xi(s)ds.
```

## 5. Status

```text
proved: MESH-REM;
proved: KIN-REM;
proved: REM for active finite roots away from the Fourier mesh;
open:   prove the contour bound CB from E72.312.
```

The compact branch has now lost one algebraic obstruction. The only remaining compact-root theorem is
the analytic contour estimate `CB`.
