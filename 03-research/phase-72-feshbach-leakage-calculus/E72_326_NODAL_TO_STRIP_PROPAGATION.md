# E72.326 -- Nodal-to-strip propagation for PW-Cauchy

**Purpose.** Prove the propagation step left open in E72.325: once the zero-node system suppresses
off-line nodal values, the scalar packet equation propagates that control to fixed shifted strips.

This lemma is conditional on the genuine finite remainder. E72.334 later replaces the split
`OUT-POLY + TAIL-POLY` by the single finite contour gate `UREM-POLY`.

## 1. Paired equation in a fixed compact strip

Let `K` be a compact subset of the shifted `z`-plane avoiding the finite kinematic poles and the
finite mesh. E72.321 gives

```text
(mu+e_pole-2kappa_L)G_x(z)
= sum_{w in Div(Z)/+-} Pair_z(w)
   - Lcal(B_z^tail).                                  (1)
```

For `z in K`, split the paired zero divisor into:

```text
Off_T  = off-line representatives in |Im w|<=T,
Crit_T = critical-line representatives in |Im w|<=T,
Out_T  = remaining representatives.
```

## 2. Kernel bounds on compact z-sets

For fixed `K,T`, the paired kernel coefficient is uniformly bounded:

```text
|Pair_z(w)| <= C_{K,T} ( |G_x(w)| + |G_x(z)| indicator_{w near z} )
```

with the removable self-pair convention. Since `z in K` is separated from the finite set `Off_T union
Crit_T` unless one explicitly evaluates at a node, the non-self terms satisfy

```text
|Pair_z(w)| <= C_{K,T}|G_x(w)|.
```

If `z` equals a node, E72.322/E72.325 supply the corresponding Hermite-removable value.

## 3. Assumptions

Assume, for the fixed `K,T`:

```text
OFF-NODAL:
for every off-line zero representative w in Off_T with Re w=alpha_w>0,
|G_x^(p)(w)| <= C_{K,T} e^(-alpha_w L)L^B
for the needed Hermite orders p.

CRIT-POLY:
for every critical-line representative w in Crit_T,
|G_x^(p)(w)| <= C_{K,T}L^B.

UREM-POLY:
the finite packet remainder outside the chosen zero window satisfies
|Rem_T^M(z)| <= C_{K,T}L^B uniformly for z in K.
```

Finally assume the pole-even coefficient has the gap scale

```text
|mu+e_pole-2kappa_L| >= c L^2
```

or at least a positive polynomial lower bound.

## 4. Propagation theorem

Under the assumptions above,

```text
sup_{z in K}|G_x(z)| <= C_{K,T}L^B.                    (PW-K)
```

Thus `PW-Cauchy` holds on `K`.

### Proof

For `z in K`, equation (1) gives

```text
|mu+e_pole-2kappa_L||G_x(z)|
<= |sum_{Off_T}Pair_z^M(w)|
 + |sum_{Crit_T}Pair_z^M(w)|
 + |Rem_T^M(z)|.
```

The off-line part is polynomial because each coefficient is fixed-window rational/exponential and the
nodal value carries the matching factor `e^(-Re(w)L)` from `OFF-NODAL`. The critical-line part is
polynomial by `CRIT-POLY`, since `Re w=0` produces no exponential growth. The remaining finite
remainder is polynomial by `UREM-POLY`.

Dividing by the polynomial lower bound for the left coefficient proves `(PW-K)`, after increasing the
polynomial exponent if needed. `QED`

## 5. Consequence

E72.324--E72.325 prove the algebraic part of `OFF-NODAL` once the maximal-cluster errors are
polynomial. Therefore the remaining analytic gates for `PW-Cauchy` are exactly:

```text
1. CRIT-POLY on critical-line zero nodes;
2. UREM-POLY for the finite packet remainder;
3. polynomial lower bound for mu+e_pole-2kappa_L (E72.328/E72.330).
```

## 6. Status

```text
proved: OFF-NODAL + CRIT-POLY + UREM-POLY imply PW-Cauchy on fixed compact strips;
closed: CRIT-POLY in E72.327 under polynomial active dimension;
closed: left coefficient lower bound in E72.330;
reduced: nodal-to-strip propagation to UREM-POLY.
```
