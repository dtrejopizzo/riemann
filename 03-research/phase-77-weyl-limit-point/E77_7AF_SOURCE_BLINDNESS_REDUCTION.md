# E77.7af - Source-blindness reduction to a full boundary-zero eigenvector

**Run:** 2026-07-18.

## 1. Purpose

After E77.7ae, the singular fixed-section LP bridge is reduced to the
non-vanishing of

```text
(v0^* g)(r(z0)v0),
```

for the simple zero mode `v0` of the shifted inner block

```text
A = H_inner - mu I.
```

This note proves that vanishing of the source factor `v0^* g` is already a
global obstruction: it would produce a full eigenvector of the finite CCM
section with both boundary entries equal to zero.

## 2. Exact mirror symmetry

Let `J` be the reversal matrix on the inner index set:

```text
(Jx)_n = x_{-n}.
```

For the symmetric finite CCM sections used throughout Phase 77, the inner
block is exactly persymmetric:

```text
J A J = A.                                            (AF-1)
```

Likewise the left and right boundary coupling columns are mirror images:

```text
g_left = J g_right.                                   (AF-2)
```

Both identities are exact at the matrix level; they were also verified
numerically in the companion audit below.

## 3. Simple zero mode has definite parity

Assume `0` is a simple eigenvalue of `A` with normalized eigenvector `v0`:

```text
Av0 = 0,
v0^* v0 = 1.                                          (AF-3)
```

Since `A` commutes with `J`, the one-dimensional kernel of `A` is invariant
under `J`.  Therefore there exists `eps in {+1,-1}` such that

```text
J v0 = eps v0.                                        (AF-4)
```

So the zero mode is either even or odd under reversal.

## 4. Right blindness implies left blindness

Using `(AF-2)` and `(AF-4)`:

```text
v0^* g_left
= v0^* J g_right
= (J v0)^* g_right
= eps v0^* g_right.                                  (AF-5)
```

Hence

```text
v0^* g_right = 0
=> v0^* g_left = 0.                                  (AF-6)
```

So source blindness to the right boundary automatically implies blindness to
both boundaries.

## 5. Full boundary-zero extension

Embed `v0` into the full finite section by placing zeros at the two boundary
slots:

```text
V0 = [0; v0; 0].                                      (AF-7)
```

The full section matrix has block form

```text
H - mu I =
[ *         g_left^*     * ]
[ g_left      A        g_right ]
[ *       g_right^*    * ].
```

If `v0^* g_right = 0`, then by `(AF-6)` also `v0^* g_left = 0`, so the first
and last coordinates of `(H-mu I)V0` vanish.  The interior coordinates vanish
because `Av0=0`.  Therefore:

```text
v0^* g_right = 0
=> (H - mu I) V0 = 0.                                (AF-8)
```

That is, right source blindness of the zero mode produces a genuine
eigenvector of the full finite section whose two boundary entries are zero.

## 6. Consequence for the live object

Equation `(AF-8)` gives the exact implication

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE
=> v0^* g_right != 0.                                (AF-9)
```

So the source half of the kernel-double-coupling target is not an
independent Schur problem.  It is a concrete finite-section exclusion:

```text
the moving ground eigenspace of the full section cannot be represented by a
vector vanishing at both outer boundary slots.
```

This aligns exactly with the Phase 77 endpoint audit E77.7k, where the
remaining LP gate was identified as

```text
simplicity + nonzero normalization coupling.
```

## 7. Companion audit

Numerical audit (July 18, 2026) verified the exact matrix symmetries and the
parity of the simple zero mode on the tested zeta ladder:

```text
J A J = A exactly,
g_left = J g_right exactly,
J v0 = +v0 to numerical precision,
v0^* g_left = v0^* g_right to numerical precision.
```

Representative zeta rows:

```text
N=10: |lambda0| = 1.84e-30,  |L-R| = 7.62e-57
N=14: |lambda0| = 2.25e-39,  |L-R| = 3.30e-53.
```

The parity sign happened to be `+1` on the tested rows, but the reduction
only needs `(AF-4)`, not the value of `eps`.

## 8. Status

```text
proved:    source blindness of the simple zero mode implies blindness to both
           outer boundaries by mirror symmetry;
proved:    such blindness yields a full finite-section eigenvector with both
           boundary entries zero;
refined:   the source non-vanishing problem reduces to excluding full
           boundary-zero ground states;
next:      connect that exclusion to the Phase-77 simplicity/nonvanishing
           gate, and isolate the remaining anchor factor r(z0)v0.
```
