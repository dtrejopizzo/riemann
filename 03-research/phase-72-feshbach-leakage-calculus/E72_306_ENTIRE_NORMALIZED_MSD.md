# E72.306 -- Entire normalized form of NZ-MSD

**Purpose.** Refine E72.305. The tempting residue conversion of

```text
sum_rho M_tau(rho-1/2)
```

to finite mesh-pole residues does not work: `M_tau` is entire. This note records the cancellation and
states the correct normalized divisibility target.

## 1. Apparent mesh poles are removable

E72.302 gives

```text
M_tau(z)
= (1-e^(zL))
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [Phi_z(d_m)-Phi_z(d_n)]/[pi(n-m)],
Phi_z(d)=d/(z^2+d^2).
```

The rational terms have apparent poles at

```text
z= +/- i d_m.
```

But `d_m=2pi m/L`, so

```text
1-e^(zL)=0       at       z=i d_m.
```

The zero is simple and cancels the simple pole of `Phi_z(d_m)`. The same happens at `z=-i d_m`.
This is forced by the original definition

```text
M_tau(z)=int_0^L e^(zy)F_tau(y)dy,
```

which is entire.

Thus there is no finite mesh-residue identity obtained by integrating
`(xi'/xi)(1/2+z)M_tau(z)`: the only residues inside the contour come from the nontrivial zeros of
`xi`, plus boundary integrals.

## 2. Normalized entire quotient

Define the normalized finite transform

```text
N_tau(z):=M_tau(z)/(1-e^(zL)).
```

Away from the mesh points this is

```text
N_tau(z)
= sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [Phi_z(d_m)-Phi_z(d_n)]/[pi(n-m)].                (1)
```

At `z= +/- i d_m`, it is defined by the removable limit. Therefore `N_tau` is meromorphic only before
removable completion; `M_tau` is entire and the normalized formula is a finite divided-difference
object with removable mesh singularities.

The compact nontrivial-zero target becomes

```text
NZ-MSD:
sum_rho (1-e^((rho-1/2)L)) N_tau(rho-1/2) = O_H(L^4).      (2)
```

This is the exact finite Mellin divisibility condition in normalized form.

## 3. Off-line zero pressure

Let

```text
z_rho = rho-1/2 = a+i gamma.
```

If `a>0`, then the factor in (2) has size

```text
|1-e^(z_rho L)| ~ e^(aL)
```

away from accidental phase cancellation. Therefore a single off-line zero can be harmless only if the
normalized divided-difference value satisfies

```text
N_tau(z_rho)=O_H(L^4 e^(-aL))
```

or if it cancels coherently with the symmetric zero packet. This is the exact pressure that scalar WRL
places on the finite transform.

## 4. Symmetric zero packet form

The completed zeta zeros occur in the packet

```text
rho, 1-rho, conjugate(rho), 1-conjugate(rho).
```

In shifted variables this is

```text
z, -z, conjugate(z), -conjugate(z).
```

Since `F_tau` is real-valued,

```text
M_tau(conjugate(z))=conjugate(M_tau(z)).
```

The packet contribution is therefore determined by

```text
M_tau(z)+M_tau(-z)+conjugates.
```

In normalized form:

```text
Packet_tau(z)
= (1-e^(zL))N_tau(z)+(1-e^(-zL))N_tau(-z)+conjugates.  (3)
```

For `Re z>0`, the dominant term is `(1-e^(zL))N_tau(z)`. Thus the packet version of NZ-MSD requires
the same exponential annihilation unless the finite transform has a symmetry forcing cancellation
between `N_tau(z)` and `N_tau(-z)`.

## 5. Correct next theorem

The next proof target is not a mesh-pole residue theorem. It is one of the following equivalent
finite statements:

```text
NZ-MSD:
sup_{tau_j<=H}|sum_rho (1-e^((rho-1/2)L))N_tau_j(rho-1/2)| <= C_H L^4,
```

or the stronger pointwise divisibility pressure:

```text
POINT-MSD:
for every off-line packet z with Re z>0,
N_tau_j(z)=O_H(L^4 e^(-Re(z)L))
after packet symmetrization.
```

`POINT-MSD` is stronger than needed, but it exposes exactly what would rule out an off-line zero in
the compact FORM channel.

## 6. Reading

E72.306 prevents a false closure by residues at the Fourier mesh. The finite Fourier mesh cancels its
own apparent poles. What remains is sharper and harder: prove exponential annihilation of the
normalized divided-difference transform on off-line shifted zero packets, or prove the weaker summed
NZ-MSD identity directly.

E72.307 rewrites the normalized transform as

```text
N_tau(z)=(2/L)<xi,[S_tau,[L_z,S_tau]]xi>,
```

where `L_z` is the Loewner matrix of `Phi_z(d)=d/(z^2+d^2)`.
