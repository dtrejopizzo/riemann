# P75.007-P75.009 - Cutoff, root transport, and Schur transfer audit

## P75.007 cutoff audit

Four cutoff classes were considered:

```text
hard cutoff;
C-infinity cutoff;
Gevrey cutoff;
Paley-Wiener compact-support cutoff.
```

The hard cutoff preserves the Phase 71/72 CCM builder but gives boundary and
mesh tails that cannot be integrated by parts to all orders.

Smooth and Gevrey cutoffs improve formal integration by parts, but they
change the exact finite CCM matrix unless the Hilbert/product-rule identities
are rebuilt with the new weight.  When rebuilt honestly, the resulting signed
remainder is still the recombined Euler/Gamma object from P75.004-P75.006.

Paley-Wiener compact support is incompatible with simultaneously keeping the
same finite mesh interpretation and an all-orders compact physical cutoff:
one gains decay on one side by paying analytic growth on the dual side.

Conclusion:

```text
No cutoff redesign produced MeshTail_L+PrimeTail_L=O_M(L^-M)
while preserving CCM, self-adjointness, falsifiers, and the Phase 72-74 chain.
```

This is P75.015 outcome D for cutoff-only closure attempts.

## P75.008 derivative separation

The finite identity

```text
C_L(gamma)=C'_L(theta)(gamma-tau_L)
```

reduces root locking to numerator divisibility only under polynomial
separation:

```text
L^-B <= |C'_L(tau_L)| / normalization <= L^B.
```

Phase 74 probes support polynomial behavior on resolved zeta windows, and
P75.010 continues to measure it.  However, derivative separation alone does
not prove smallness of `C_L(gamma)`; it only transports smallness after
`ARITH-LOCK` is known.

Conclusion:

```text
Derivative separation is a transfer lemma, not a source of arithmetic
divisibility.
```

## P75.009 Schur transfer

The exact Phase 74 transfer is:

```text
QH(I-P)xi=T Qxi,
T=mu I-QHQ*(QQ*)^-1.
```

Uniform closure requires polynomial conditioning of `T`, or equivalently a
finite compression estimate

```text
c_L QQ* <= QH_LQ* <= C_L QQ*
```

on resolved windows.  The zeta numerics have `T/L` close to `-I`, but the
lower bound is exactly the unresolved signed coupled estimate
`CAUCHY-COMP`.

Using global Weil positivity would prove a stronger object than the phase is
allowed to assume.  Termwise sector positivity loses the prime/archimedean
coupling and fails the planted/DH discrimination test.

Conclusion:

```text
Schur transfer remains conditional on ARITH-LOCK/CAUCHY-COMP.
It cannot be used as an independent input.
```

This is P75.015 outcome E for Schur-only closure attempts.

