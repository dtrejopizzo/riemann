# E72.393 - Gate status after tail absorption

## 1. What changed

Before E72.390--E72.392 the transformed compact branch had two separate analytic gates:

```text
PAIR-Z:     control the paired zero interpolation sum;
TAIL-POLY:  control the finite Fourier tail.
```

This split is no longer the sharp formulation.

E72.391 proves the exact identity

```text
Lcal(b_m)= -2i/L sum_w wG_x(w)/(w^2+d_m^2),
```

so the finite Fourier tail is a rational kernel applied to the same nodal vector `{G_x(w)}` as
`PAIR-Z`.

E72.392 then proves that, on a maximal off-line cluster and for

```text
M >= L^(1+epsilon),
```

the tail block is a lower-order perturbation of the leading Cauchy block:

```text
relative size <= C_K L^2/M^2 = O(L^(-2epsilon)).
```

## 2. Updated compact branch

The compact branch is now:

```text
maximal Cauchy block invertibility
+ tail perturbation absorption
+ outside-window zero bound
+ nodal-to-strip propagation
=> PW-Cauchy
=> SQB
=> CB
=> RNS
=> MC-NZ
=> NZ-MSD
=> compact-root HPAC decay.
```

The finite Fourier tail is no longer an independent wall.

## 3. Closed gates in this segment

```text
closed: SFREQ via second variation at natural height                 [E72.388]
closed: D2BV-K under polynomial active bandwidth                     [E72.389]
closed: apparent 1/m tail coefficient by pole-even parity            [E72.390]
closed: tail coefficient collapse to Cauchy nodal moment             [E72.391]
closed: tail perturbative in zero-node system for M>=L^(1+epsilon)   [E72.392]
```

The polynomial cutoff required by E72.392 is compatible with E72.389, because E72.389 allows any
fixed polynomial active bandwidth at the cost of increasing the harmless power `L^B`.

## 4. Remaining load-bearing theorem

The remaining analytic theorem is now a single nodal theorem:

```text
NZ-NODAL:
For every fixed shifted zero height window, the full finite nodal system

   maximal Cauchy block + lower-real-part couplings + absorbed tail + outside-window remainder

forces

   G_x(a)=O(e^(-Re a L)L^B)

for every off-line shifted zero representative a in the window.
```

The already proved Cauchy determinant handles the maximal block.  E72.392 handles the finite Fourier
tail.  The two remaining terms are:

```text
1. outside-window zero contribution;
2. propagation from nodal suppression to strip PW-Cauchy.
```

## 5. Next analytic target

The next document should prove the outside-window bound in the already transformed variables:

```text
OUT-NODAL:
sum_{w outside A_T} Pair_a(w) + tail-kernel outside part
= polynomial after symmetric divisor summation and nodal induction.
```

This must be done by contour/symmetric-pair estimates, not by absolute zero sums.

