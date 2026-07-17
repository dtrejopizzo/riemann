# E74.24 - Endpoint autopsy after the Schur and nodal audits

Date: 2026-07-16.

## Proven reductions

The current endpoint has the exact chain

```text
HPR-DIV
<=> T_{w,L} Q_w xi_L=O_M(L^(-M))                 (E74.17)
<=> Q_w xi_L=O_M(L^(-M))                         (conditional on CAUCHY-COMP)
<=> P_L(+-gamma)/D_L(+-gamma)=O_M(L^(-M))        (E74.21)
<=> |tau_{j,L}-gamma_j|=O_M(L^(-M))              (derivative separation).
```

E74.18--E74.20 isolate plausible polynomial conditioning hypotheses for the
first equivalence.  The load-bearing all-orders theorem is therefore

```text
CCM-ROOT-LOCK.
```

## Routes rejected in this pass

```text
QLIFT / quotient residual: loses the coupled cancellation;
one-shot gap or Davis--Kahan: gives only fixed-order localization;
BOOT-CELL regularity: higher Cauchy jets are not small;
universal Cauchy algebra: planted off-line data retain the algebra but fail;
numerical root matching: observes the endpoint but supplies no uniform rate.
```

## Why the remaining theorem is irreducible here

The finite CCM numerator is real-rooted.  The planted experiment shows that
an off-line explicit-formula contribution displaces its real roots instead of
creating complex roots.  Thus the RH content of this construction is exactly
the assertion that the real finite divisor locks onto the full zeta divisor
without a displacement floor.

This is the convergence detector already identified in Phase 71 and the
nodal restriction of `PW-Cauchy/NUM-GROW` from Phase 72.  Phase 74 has not
derived a new independent estimate that proves it.

## Honest status

```text
proved: finite Schur, compression, Feshbach, numerator, and root-transport
        equivalences;
falsified: quotient, generic regularity, and universal-gap closure routes;
passed: planted off-line falsifier for the live observable;
not proved: CAUCHY-COMP uniformly, CCM-ROOT-LOCK, CAUCHY-EIG-LOC, Omega7;
next object: a zero-independent Euler/Gamma error formula for
             P_L(gamma), equivalently a quantitative stable-divisor theorem.
```

Any continuation should work on that Euler/Gamma error formula directly.  A
new finite projection, quotient, or eigenline detector would only rename the
same endpoint.

