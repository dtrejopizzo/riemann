# R161_007 — The Chebyshev-regularised critical jet

## 0. Verdict

Multiplying the oriented logarithmic Euler current by the Poisson/Muntz factor removes its critical pole without
removing its coefficient. This is the exact analytic point at which `Lambda*1=log` and additive Poisson must be used
together.

At a simple critical zero `rho`, the product has value

`-zeta'(rho)K_F(rho-1/2)`.

Thus the phase-121 residue condition is equivalent to ordinary vanishing of a holomorphic product, rather than to a
pole-removal statement. This proves the first half of the PC-port theorem of `R161_005`: identification of its
critical normal symbol. Equality-state vanishing of that value remains to be derived.

## 1. The oriented current and its product regularisation

Put `s=1/2+z` and recall the right-tail current

```
H_(+,T)F(z)=-(zeta'/zeta)(s)K_F(z)-Q_(+,T)(z),                    (1.1)
```

where `Q_(+,T)` is entire. Define its Chebyshev regularisation by

```
G_(+,T)F(z):=zeta(s)H_(+,T)F(z)
            =-zeta'(s)K_F(z)-zeta(s)Q_(+,T)(z).                  (1.2)
```

The second equality is an identity first in `Re s>1` and then meromorphically. In the initial half-plane it is
exactly

```
(sum 1(n)n^(-s)) (sum Lambda(d)d^(-s))
 =sum log(k)k^(-s),                                               (1.3)
```

namely `Lambda*1=log`. Equation (1.2) is its analytically continued, source-weighted version.

## 2. Exact critical value

**Theorem 2.1 (critical jet extraction; PROVED).** If `rho=1/2+i gamma` is a simple zero of `zeta`, then

```
G_(+,T)F(i gamma)=-zeta'(rho)K_F(i gamma).                        (2.1)
```

In particular,

```
G_(+,T)F(i gamma)=0  <=>  K_F(i gamma)=0.                         (2.2)
```

*Proof.* The expression on the right of (1.2) is holomorphic at `rho`. Since `zeta(rho)=0`, its second term vanishes
there and (2.1) follows. Simplicity gives `zeta'(rho)!=0`, proving (2.2). ∎

For a zero of multiplicity `m`, write `zeta(s)=(s-rho)^m a(s)`, `a(rho)!=0`. Then

```
G_(+,T)F(z)=-m(s-rho)^(m-1)a(rho)K_F(rho-1/2)+O((s-rho)^m).       (2.3)
```

Thus the coefficient of order `m-1` is the same conormal datum. The simple family is sufficient for the phase-121
Cartwright argument.

## 3. Divisibility dictionary

At a simple zero the following are equivalent:

1. `H_(+,T)F` is holomorphic at `z=i gamma`;
2. `K_F(i gamma)=0`;
3. `G_(+,T)F(i gamma)=0`;
4. `G_(+,T)F` belongs locally to the ideal `(zeta(1/2+z))`.

The equivalence of 1 and 2 is the phase-121 residue theorem; 2 and 3 are Theorem 2.1; and 1.2 shows that quotienting
`G` by `zeta` gives `H`.

This is useful because the target is now typed without division by zeta:

> show that a source-defined holomorphic product has a zero at each critical point.

The forbidden circular operation would be to define its quotient by zeta and assume that quotient is physical.

## 4. Relation to the finite Poisson--Chebyshev anomaly

In `Re s>1`, the arithmetic product in `(PC)` is finite approximation to (1.3). The hyperbola remainder `H_(M,N)`
is exactly the coefficient error made by replacing the full product with a finite rectangle. The polar
renormalisation of `R161_003` supplies the analytic continuation of the Muntz factor before the product is taken.

Consequently the critical boundary value sought in `R161_005` is not an unspecified constant: after the two Tate
terms of `R161_006` are removed, its right-oriented symbol must be (2.1), and the reflected symbol is its opposite
under the phase-121 orientation convention.

This also corrects the interpretation of the sign-blind square in `R161_002`. A generic norm of `A_MF` cannot prove
`A_M>=0`. But on a hypothetical first-contact radical, a source identity forcing the **completed** PC square to
vanish would be enough, because its critical trace contains

```
sum_(rho simple, critical) |zeta'(rho)K_F(rho-1/2)|^2             (4.1)
```

locally, with positive weights. Sign-blindness is fatal for direct positivity but not for equality-state rigidity.

## 5. Exact remaining compatibility

Phase 121 proves that, on a first-contact state, the completed sum of the two causal currents is zero in the common
zeta--Gamma graph. It does not prove that either orientation vanishes: their critical symbols are `(-c,+c)`.

The sum--product route closes D if it proves the stronger compatibility

```
graph completion of the right PC port
 = Chebyshev regularisation G_(+,T)F                              (5.1)
```

in a topology preserving evaluation at the critical jet, and if the equality equation makes the left side zero
after the explicit Tate cancellation. Under (5.1), Theorem 2.1 gives `K_F(i gamma)=0` on the unconditional
superlinear simple critical family; Cartwright uniqueness gives `F=0`.

The distinction is sharp:

- `L2` convergence of the **sum** of the ports only gives `-c+c=0`;
- local uniform convergence of the product in one orientation preserves `c`;
- convergence of values without first jets can give only `zeta(rho)K_F=0`, which is empty.

## 6. Status

- source-defined product regularisation (1.2): **PROVED**;
- exact critical normal symbol (2.1)--(2.3): **PROVED**;
- equivalence with physical oriented divisibility: **PROVED locally**;
- identification with one separated graph port in a critical-jet topology: **OPEN**;
- equality-state vanishing of that separated port: **OPEN**.

The next object is therefore a one-oriented graph closure whose norm controls first jets, not another scalar
Stieltjes form and not the symmetric `L2` graph already known to vanish.
