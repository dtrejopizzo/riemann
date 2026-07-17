# E73.267 - Cell commutator formula for the remaining theorem

Date: 2026-07-14.

## 1. Purpose

E73.265 leaves the non-circular target:

```text
q_a[H_L^A,R_w]xi_L-q_a[H_L^P,R_w]xi_L=O_M(L^-M).
```

This note expands the target down to the finite cell level.  This is the
proof-facing form of the remaining Mellin spectral divisibility.

## 2. Cell matrices

For mesh indices `m,n` let

```text
Q_y(m,n)=q_{mn}(y),
```

where `q_{mn}` is the finite CCM cell function used in the matrix construction.
Then the prime part is exactly

```text
H_L^P
=sum_{p^k<=e^L} (log p)p^(-k/2) Q_{klog p}.       (1)
```

The archimedean part is the corresponding linear functional:

```text
H_L^A=mathcal A_L[Q_y].                            (2)
```

Here `mathcal A_L` denotes the explicit Gamma/polar archimedean cell
functional already implemented in the CCM matrix entries.

## 3. Commutator-cell identity

Since `q_aR_w=0`, for either `X=A` or `X=P`,

```text
q_a[H_L^X,R_w]xi_L=q_aH_L^XR_wxi_L.               (3)
```

Therefore the prime commutator is the finite sum

```text
q_a[H_L^P,R_w]xi_L
=sum_{p^k<=e^L} (log p)p^(-k/2)
  q_a Q_{klog p} R_w xi_L.                        (4)
```

The archimedean commutator is

```text
q_a[H_L^A,R_w]xi_L
=mathcal A_L[ y -> q_a Q_y R_w xi_L ].            (5)
```

Thus E73.265 becomes the explicit cell identity:

```text
mathcal A_L[ y -> q_a Q_y R_w xi_L ]
-
sum_{p^k<=e^L} (log p)p^(-k/2) q_a Q_{klog p}R_wxi_L
=O_M(L^-M).                                      (CELL-CTM)
```

This is exactly the closed eta-packet center in cell language.

## 4. Why this is the right finite identity

`CELL-CTM`:

```text
1. does not use zeros as input;
2. does not use Q_wxi_L as a small input;
3. does not assert row norm smallness;
4. keeps the archimedean and prime terms coupled before absolute values;
5. is finite for each L.
```

Taking absolute values termwise would return to the incoherent ceiling already
rejected in earlier phases.  The theorem must preserve the signed
Gamma-prime pairing.

## 5. Numerical audit

The companion script verifies the prime part:

```text
q_aH_L^PR_wxi_L
=sum_{p^k<=e^L} (log p)p^(-k/2)q_aQ_{klog p}R_wxi_L.
```

It also reports the absolute cell sum.  The expected diagnostic is:

```text
prime cell formula matches direct H_L^P;
absolute cell sum is much larger than the signed prime pairing.
```

The latter confirms again that the proof must be signed/coupled.

## 6. The theorem left

```text
Cell Commutator Transport Matching.
For the actual Gamma-prime eigenline xi_L and every admissible Cauchy
row/window,

|mathcal A_L[q_aQ_yR_wxi_L]
 -sum_{p^k<=e^L}(log p)p^(-k/2)q_aQ_{klog p}R_wxi_L|
<= A_M L^-M
```

for every `M`.

Together with E73.262--E73.266, this is equivalent to `UNIF-ETA`.

## 7. Status

```text
proved: commutator transport matching has finite cell form CELL-CTM;
open: prove CELL-CTM analytically from the Gamma-prime eigenline structure.
```

