# R161_009 — The Hardy polar coefficients are the crossed Tate collar currents

## 0. Verdict

The two polar coefficients left open in `R161_008` are not new unknowns. They are exactly the exterior Tate moments
already computed by the phase-121 collar theorem. Primitivity collapses their apparently infinite prime sums to the
finite active contact set `n<e^(2T)`, and the Gamma contribution is the continuous collar in the same theorem.

Therefore the polar corrections of the separated Hardy ports are canonically fixed by the first-contact forcing
`(alpha,beta)`. There is no remaining two-scalar choice. The only open line is now the global equality saying that
the two canonically corrected product-Hardy ports sum to the strong graph commutator.

## 1. Residue of the product port

Let

```
H_+(z)=integral_T^infinity Y_+(t)e^(-zt)dt
      =-(zeta'/zeta)(1/2+z)K_F(z)-Q_(+,T)(z).                     (1.1)
```

Because `K_F(1/2)=0`, `H_+` is holomorphic at `z=1/2`. Since `Res_(s=1)zeta(s)=1`,

```
Res_(z=1/2)[zeta(1/2+z)H_+(z)]=H_+(1/2).                         (1.2)
```

Thus the coefficient removed in `R161_008` is the literal exterior Tate moment

```
c_+^prime(F)=integral_T^infinity e^(-t/2)Y_+(t)dt.                (1.3)
```

## 2. The infinite tail becomes a finite collar

Insert

```
Y_+(t)=sum_(n>=2) Lambda(n)n^(-1/2)F(t-log n)                    (2.1)
```

and change variables `u=t-log n`. Tonelli is valid first with a safe exponential shift and then by the finite
identity obtained below. One gets

```
c_+^prime(F)
 =sum_(n>=2) Lambda(n)/n
   integral_(max(-T,T-log n))^T e^(-u/2)F(u)du.                  (2.2)
```

If `n>=e^(2T)`, the integral in (2.2) is the full primitive moment `K_F(1/2)=0`. Hence

```
c_+^prime(F)
 =sum_(2<=n<e^(2T)) Lambda(n)/n
   integral_(T-log n)^T e^(-u/2)F(u)du.                          (2.3)
```

This is precisely the `Lambda(n)/n` right-collar coefficient in the phase-121 exact Tate-collar localization. In
particular, the product-Hardy polar residue depends only on the finite active contact set even though the causal
prime current itself contains every prime power.

Reflection gives the other near-edge coefficient with weight `Lambda(n)` and exchanges the two Tate characters,
exactly as in phase 121:

```
Lambda(n)n^(-1/2)e^(+log(n)/2)=Lambda(n),
Lambda(n)n^(-1/2)e^(-log(n)/2)=Lambda(n)/n.                       (2.4)
```

## 3. Adding the Gamma exterior

The full first-contact exterior port is

```
ell_T(F)=(1-P_T)A_infinity F.                                    (3.1)
```

Phase 121 proves that the Gamma exterior Tate moments are the continuous collars

```
integral_0^(2T)c_Gamma(u)
 [e^(sigma u/2)R_(sigma,u)(F)+e^(-sigma u/2)L_(sigma,u)(F)]du.   (3.2)
```

Adding (2.3) and its reflected analogue gives exactly the boundary currents `J_+(F),J_-(F)` of the crossed Tate
system

```
[2T       2sinh T] [alpha] = [J_+(F)],
[2sinh T  2T     ] [beta ]   [J_-(F)].                            (3.3)
```

The determinant `4(T^2-sinh^2 T)` is nonzero for `T>0`. Therefore the two full polar coefficients of the product-
Hardy ports and the two forcing coefficients `(alpha,beta)` determine each other uniquely.

**Theorem 3.1 (canonical polar match; PROVED).** The causal polar corrections required in `R161_008` can be chosen
canonically from the first-contact Tate forcing. With that choice:

1. both product ports are holomorphic in their respective half-planes;
2. their boundary values are `L2`;
3. their values at every nontrivial zero remain
   `+/- zeta'(rho)K_F(rho-1/2)`;
4. no free scalar boundary parameter remains.

*Proof.* Equations (1.2)--(2.4) identify the discrete residues. Formula (3.2) identifies the Gamma residues. The
phase-121 collar theorem gives (3.3), whose invertibility fixes the correction uniquely. Every correction is zeta
times an entire Tate transform, so it vanishes at nontrivial zeros and leaves the critical values unchanged. The
Hardy assertion is Theorem 3.1 of `R161_008`. ∎

## 4. Consequence in the first chamber above `0.8`

For

```
0.8<T<(1/2)log 5,
```

formula (2.3) contains only `n=2,3,4`. The entire polar match is therefore a finite expression involving

```
log2/2, log3/3, log2/4                                           (4.1)
```

and the corresponding three collars, plus the explicit Gamma integral (3.2). There is no limiting prime sum in the
polar matching step.

## 5. Remaining identity

Let `g_+^can` and `g_-^can` be the inverse boundary transforms of the two canonically corrected product-Hardy ports.
They satisfy

```
supp g_+^can subset [T,infinity),
supp g_-^can subset (-infinity,-T].                               (5.1)
```

All scalar terms having now been matched, the last statement required for closure is the vector identity

```
[Z,D_Gamma]E_TF = g_+^can+g_-^can                                (5.2)
```

in the common `L2` graph. The left side is zero for a first-contact radical. If (5.2) holds, disjoint support gives
`g_+^can=g_-^can=0`; evaluation at the critical zeros then gives `F=0`.

Unlike the previous versions of the target, (5.2) has no unspecified completion, scalar correction or norm. It is a
literal equality between the already constructed finite-PC graph limit and two explicit Hardy boundary functions.

## 6. Status

- discrete polar coefficient and finite-collar collapse: **PROVED**;
- Gamma coefficient and crossed Tate match: **PROVED by the phase-121 collar theorem**;
- canonical corrected Hardy ports: **PROVED**;
- graph decomposition (5.2): **OPEN**;
- closure of D from (5.2): **PROVED conditionally by disjoint support and the critical-jet theorem**.
