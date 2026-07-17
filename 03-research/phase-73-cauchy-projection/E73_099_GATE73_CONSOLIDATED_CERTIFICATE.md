# E73.099 - Consolidated GATE-73 certificate

## 1. Purpose

This document consolidates Phase 73 after the Mellin divisibility work.

The goal is to state one finite certificate whose truth implies the scalar WRL branch.

## 2. The four finite gates

For each natural-height off-line cluster box `A` and scale `L`, define:

```text
GATE-73(A,L)
```

as the conjunction of the following four finite statements.

### Gate 1. Local complete-mesh packet

```text
LOCK-COMP-BUD(A,L):
4(1+e^(sigma L))/sigma * S_FAR(A,L) * N_LC(A,L)
<= C_LC L^-5.
```

This controls the exact complete-mesh paired packet because:

```text
Pair_z^infty(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

### Gate 2. Local finite-tail packet

```text
TAIL-LC-BUD(A,L):
C_K e^(sigma L)L^2/M^2 S_FAR(A,L)Wloc(A,L)N_LC(A,L)
<= C_tail L^-5.
```

This controls the local finite Fourier tail using:

```text
Lcal(B_z^tail)= -2i/L sum_w wG_x(w)R_M(z,w).
```

### Gate 3. Outside rows and high zeros

```text
OUT-FAR(A,L):
OUT-FAR_fin(A,L)+OUT-HIGH(A,L) <= C_out L^-9.
```

Here:

```text
OUT-FAR_fin(A,L)
=
sum_{gamma_k in K_L \ D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|.
```

`OUT-HIGH` is the natural-height high-zero tail of E72.394.

### Gate 4. Three FAR3 main rows

```text
FAR3-MAIN-RAT(A,L):
sum_{gamma_k in D_3(A,L)}
W_k(A,L)|P_x(-gamma_k)|/|D_x(-gamma_k)|
<= C_main L^-5.
```

## 3. Theorem

**Theorem 99.1.**  If `GATE-73(A,L)` holds for every natural-height off-line cluster box at scale
`L`, then the scalar WRL branch holds at scale `L`.

*Proof.*  Gate 1 gives `LOCAL-HWIN-5` by E73.091.  Gate 2 gives the local tail part by E73.094.
Together they give the local `FACTOR-MAIN-5 + TAIL-NODAL-5` input to the balanced packet row gate.

Gate 3 controls all finite rows outside the FAR3 selected set and the high-zero tail beyond
`T_L=e^L L^A` by E73.096 and E72.394.

Gate 4 controls the three main FAR3 WCS terms by E73.098.

Therefore the whole WCS sum splits as:

```text
WCS(A,L)
= FAR3 main + finite complement + high tail
<= C_main L^-5 + C_out L^-9,
```

with the local packet and tail divisibility supplying the corresponding row-main input to the
Phase 72 scalar WRL route.  E73.042 proves:

```text
WCS => scalar WRL.
```

Thus `GATE-73(A,L)` implies scalar WRL at scale `L`. `□`

## 4. Uniform endpoint

The remaining uniform theorem is:

```text
Uniform GATE-73:
there exist constants L0,C_LC,C_tail,C_out,C_main
such that GATE-73(A,L) holds for all L>=L0 and all natural-height off-line cluster boxes A.
```

If `Uniform GATE-73` is proved, the Phase 72 route gives:

```text
Uniform GATE-73
=> scalar WRL
=> Omega7
=> RH.
```

## 5. What is closed

The Mellin spectral divisibility part is closed in the precise sense:

```text
complete mesh: exact ideal membership Pair_z^infty(w) in (H_0(w),H_0(-w));
finite tail: explicit nodal operator controlled by TAIL-LC-BUD;
outside high zeros: polynomial/decaying natural-height tail by E72.394.
```

No hidden Cauchy matrix inverse remains in the certificate.  Every live term is an explicit finite
rational or elementary expression.

## 6. What remains

The remaining problem is not to find the divisor.  It is to prove the four finite inequalities in
`Uniform GATE-73`, especially the dominant three-row rational bound `FAR3-MAIN-RAT`.
