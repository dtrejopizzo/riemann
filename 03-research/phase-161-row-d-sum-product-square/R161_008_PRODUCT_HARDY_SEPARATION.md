# R161_008 — Product regularisation gives separated Hardy ports

## 0. Verdict

For a phase-121 first-contact state, the Chebyshev-regularised oriented current of `R161_007` has an `L2` boundary
after one explicit polar/Tate correction. Since its inverse Laplace distribution is causal, it belongs to the right
Hardy space. Reflection gives a left Hardy port.

The correction is a multiple of `zeta(s)` times an entire causal Tate transform. It removes the pole at `s=1` but
vanishes at every nontrivial zero of zeta. Therefore it does not alter the critical value

`-zeta'(rho)K_F(rho-1/2)`.

This supplies the global causal structure absent from the phase-121 universal conormal countermodel. The remaining
line is now a precise cross-port identity: prove that the strong zero commutator is the sum of these two separated
Hardy representatives after the crossed Tate correction. If so, uniqueness of the Hardy decomposition makes both
ports zero and closes D.

## 1. Regularity available only on a first-contact radical

Phase 121 proves that the zero extension `u=E_TF` of every first-contact vector satisfies

```
u in H^s(R) for every 0<s<1/2.                                  (1.1)
```

Fix

```
1/4+eta < s < 1/2.                                               (1.2)
```

Classical convexity and a Cauchy estimate on a slightly wider strip give

```
|zeta(1/2+i tau)|+|zeta'(1/2+i tau)|
 <= C_eta(1+|tau|)^(1/4+eta).                                   (1.3)
```

Logarithmic factors are absorbed by decreasing `eta` in (1.2).

The compact prehistory

```
Q_(+,T)(z)=integral_(log2-T)^T Y_+(t)e^(-zt)dt                    (1.4)
```

is obtained from finitely many translations and interval restrictions of `F`. Multiplication by an interval is
bounded on `H^s` for `|s|<1/2`. Hence

```
K_F(i tau), Q_(+,T)(i tau) in L2((1+tau^2)^s d tau).             (1.5)
```

Equations (1.2)--(1.5) imply

```
zeta'(1/2+i tau)K_F(i tau) in L2(d tau),
zeta(1/2+i tau)Q_(+,T)(i tau) in L2(d tau).                      (1.6)
```

This is the regularity gain: the logarithmic current itself need not be `H2`, but its product with the Poisson
factor has an `L2` boundary.

## 2. Causal polar correction

Let

```
H_+(z)=-(zeta'/zeta)(1/2+z)K_F(z)-Q_(+,T)(z),
G_+(z)=zeta(1/2+z)H_+(z).                                       (2.1)
```

The only singularity of `G_+` in the open right half-plane is the polar point `z=1/2`; all nontrivial-zero poles of
`H_+` have been cancelled by the product.

Choose once and for all `theta_T in C_c^infinity((T,T+1))` whose Laplace transform

```
Theta_T(z)=integral theta_T(t)e^(-zt)dt                           (2.2)
```

does not vanish at `z=1/2`. There is a unique scalar `c_+(F)` such that

```
G_+^0(z):=G_+(z)-c_+(F)zeta(1/2+z)Theta_T(z)                     (2.3)
```

is holomorphic at `z=1/2`. Indeed `zeta(1/2+z)` has a simple pole there, so its multiple can cancel the principal
part of `G_+` uniquely.

At every nontrivial zero `rho=1/2+i gamma`,

```
G_+^0(i gamma)=G_+(i gamma)=-zeta'(rho)K_F(i gamma).              (2.4)
```

Thus the polar correction changes no critical jet of interest.

## 3. Hardy membership

**Theorem 3.1 (right product-Hardy port; PROVED).** For every first-contact vector,

```
e^(Tz)G_+^0(z) in H2(C_+).                                       (3.1)
```

*Proof.* In `Re z>1/2`, `H_+` is the Laplace transform of the right arithmetic tail supported in `[T,infinity)`.
Multiplication by the absolutely convergent Dirichlet series `zeta(1/2+z)` is convolution with nonnegative
logarithmic delays and preserves that support. The correction in (2.3) has the same property because `theta_T` is
supported to the right of `T`. Hence `G_+^0` is the Laplace transform of a distribution supported in
`[T,infinity)`.

It is holomorphic in `C_+`: the nontrivial-zero singularities cancel algebraically and (2.3) removes the polar
singularity. Equations (1.6), together with the Schwartz boundary of `Theta_T`, show that its boundary value on
`iR` belongs to `L2`. The Paley--Wiener theorem for causal distributions then promotes that distribution to an
`L2(T,infinity)` function and gives (3.1). ∎

Reflection gives a corrected left port `G_-^0` with

```
e^(-Tz)G_-^0(z) in H2(C_-),                                       (3.2)
```

and critical normal symbol opposite to (2.4) in the phase-121 orientation convention.

## 4. Why this escapes the old F2 countermodel

The universal model of `P121_F2_DIRECT_CLOSURE_AUDIT` has two abstract conormal values `(-c,+c)`, Real covariance
and zero scalar sum. It contains no global support condition. Theorem 3.1 adds exactly such a condition:

```
right symbol = boundary of a right-causal H2 function,
left symbol  = boundary of a left-causal H2 function.             (4.1)
```

The intersection of the corresponding `L2` causal subspaces is zero. Therefore, if the first-contact equation gives

```
g_+^0+g_-^0=0 in L2(R),                                           (4.2)
```

where `g_+^0` and `g_-^0` are the inverse boundary transforms, then their disjoint half-line supports imply

```
g_+^0=g_-^0=0.                                                    (4.3)
```

Equation (2.4) then gives `K_F(i gamma)=0` at every simple critical zero, and the phase-121 Cartwright theorem gives
`F=0`.

## 5. The exact last identity

The strong phase-121 graph theorem proves that the **completed symmetric** zeta--Gamma commutator is zero on a
first-contact radical. To finish the argument one must show that, under the finite Poisson--Chebyshev regularisation,
that completed commutator has the literal Hardy decomposition (4.2), including the canonical crossed Tate
coefficients.

This is no longer an estimate. It is the equality

```
PC graph limit = g_+^0+g_-^0                                    (5.1)
```

in `L2(R)`. All terms except the two polar coefficients are fixed by `R161_006`--`R161_008`. The coefficients must
be compared with the two-by-two crossed Tate system of phase 121; choosing them independently as in Section 2 is
not sufficient for (5.1).

If (5.1) holds with those coefficients, D closes by (4.2)--(4.3), with no positivity estimate and no spectral gap.

## 6. Status

- first-contact weighted boundary estimate (1.6): **PROVED**;
- causal polar correction preserving all critical values: **PROVED**;
- separated right/left Hardy memberships: **PROVED**;
- uniqueness once the corrected ports sum to zero: **PROVED**;
- identification of the polar coefficients with the crossed Tate forcing in the PC graph limit: **OPEN**;
- row D: **OPEN pending that exact two-scalar identity**.
