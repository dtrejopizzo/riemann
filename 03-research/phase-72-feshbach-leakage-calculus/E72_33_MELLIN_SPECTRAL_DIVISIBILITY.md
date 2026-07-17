# E72.33 -- Mellin spectral divisibility and scalar WRL annihilation

**Date:** 2026-07-08.
**Role:** formulate the only algebraic identity strong enough to prove scalar WRL resonance
annihilation, and show exactly what it requires.

## 0. Mellin transform of the scalar kernel

For fixed Cauchy height variable `s`, define

```text
M_x(s;z) := z int_1^x u^{z-1}L_x(s;u)du.
```

When `L_x(s;1)=0`, the scalar WRL resonance is

```text
R_x^{WRL}(s;z)=M_x(s;z).
```

Thus the target is:

```text
M_x(s;rho) -> 0
```

for every off-critical zero `rho`.

## 1. Finite spectral polynomial

Let `P_x(z)` be the finite CCM Weyl numerator from E72.26:

```text
P_x(z)=-det B_x(z).
```

It has only real zeros at every finite `x`.

The strongest possible intrinsic algebraic explanation for scalar annihilation is:

```text
M_x(s;z) = P_x(z) A_x(s;z) + E_x(s;z),           (MSD)
```

with:

```text
A_x(s;z) locally normal,
E_x(s;z)->0 locally uniformly.
```

Call this Mellin spectral divisibility.

## 2. Divisibility theorem

### Theorem 72.33

Assume Mellin spectral divisibility `(MSD)` on a compact set `K` in the strip, and assume the normalized
finite spectral polynomials converge locally uniformly:

```text
P_x(z)/P_x(0) -> Xi(z)/Xi(0).                    (PC)
```

Then scalar WRL resonance annihilation holds on `K`:

```text
M_x(s;rho) -> 0
```

for every zero `rho` of `Xi` in `K`, provided `A_x(s;rho)` is locally bounded and `E_x(s;rho)->0`.

### Proof

Let `rho in K` with `Xi(rho)=0`. By `(PC)`,

```text
P_x(rho)/P_x(0) -> 0.
```

Using `(MSD)`,

```text
M_x(s;rho)
 = P_x(rho)A_x(s;rho)+E_x(s;rho).
```

After the same normalization used in `(PC)`, local boundedness of `A_x` and convergence of `E_x` give

```text
M_x(s;rho)->0.
```

`QED`

## 3. Converse obstruction

The converse direction explains why this is hard. Suppose scalar WRL annihilation holds for a family of
Cauchy tests `s` rich enough that the functions

```text
M_x(s;z)
```

separate local divisor mass. Then every off-critical zero of `Xi` lies in the asymptotic common zero
set of the Mellin transforms. By the zero-filter theorem E72.16, any locally normal nonzero limit of
these transforms has a divisor containing the off-critical zeta divisor.

Thus scalar WRL annihilation itself manufactures a zero-filter unless it is explained by finite
spectral divisibility.

## 4. What would be a real proof

A non-circular proof must establish `(MSD)` directly from the finite CCM construction:

```text
M_x(s;z) = -det B_x(z) * A_x(s;z) + E_x(s;z),
```

where `B_x` is the bordered pencil of E72.26, and then prove the convergence of `P_x` to `Xi` through
the prolate/finite current route.

But notice:

```text
P_x -> Xi
```

is already the Phase 71 stable divisor convergence theorem. Therefore `(MSD)` is useful only if it
allows proving `P_x -> Xi` indirectly, through current identities, rather than assuming it.

## 5. Current endpoint

The requested scalar annihilation is not an independent lemma. It is equivalent, in Mellin form, to one
of:

```text
1. finite spectral divisibility by P_x plus P_x -> Xi;
2. a zero-filter containing the Xi divisor;
3. Schur-free current convergence.
```

Options 1 and 3 are legitimate if proved from finite CCM data. Option 2 is circular unless the filter is
intrinsic.

## 6. Status

```text
proved: spectral divisibility + finite spectral convergence implies scalar WRL annihilation;
proved: scalar WRL annihilation without divisibility creates a zero-filter;
open:   prove Mellin spectral divisibility from the explicit scalar kernel L_x.
```

The next possible calculation is direct: compute `M_x(s;z)` from the finite matrix formula for `L_x`
and test whether division by `P_x(z)` is regular.
