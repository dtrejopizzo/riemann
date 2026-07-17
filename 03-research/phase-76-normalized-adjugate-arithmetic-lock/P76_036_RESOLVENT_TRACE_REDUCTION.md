# P76.036 - Resolvent-trace reduction of SR-LOG

Let `rho_j(L,N)` denote the paired real zeros of the bilateral boundary
characteristic.  Its canonical product gives the exact positive Stieltjes
formula

```text
d/dsigma log Psi_{L,N}(-i sigma)
 =sum_j 2 sigma/(rho_j(L,N)^2+sigma^2).          (RTS-1)
```

By P76.023, the non-mesh roots are the quotient spectrum of the explicit
rank-one modification

```text
D'=D-(1/(1^T y))D y 1^T
```

on the positive Schur quotient.  Hence `(RTS-1)` is equivalently a finite
resolvent trace of `D'`, plus the known uncancelled mesh tail.  In the direct
Schur form it is exactly `(SL-1)`.

The target has the Euler-safe expansion

```text
2 Xi'(s)/Xi(s)
=2/s+2/(s-1)-log pi+digamma(s/2)
 -2 sum_{n>=2} Lambda(n)n^(-s),  s=1/2+sigma.   (RTS-2)
```

The initially proposed hard-truncation trace formula was:

```text
BTR-TRACE:
Tr_safe(D'_{L,N}) + mesh_tail
 = arch_gamma(s)-2 sum_{n<=lambda^2}Lambda(n)n^(-s)
   + o_{L,N}(1),                                 (RTS-3)
```

locally uniformly for `s>1`.

P76.040 numerically falsifies `(RTS-3)` as a finite identity.  The Schur
quotient is a coupled rational regularization, not the raw truncated Euler
sum.  `(RTS-3)` is retained here only as an autopsied proposal and must not
be used as a proof premise.

The valid trace formulation names the remaining finite object without using its zeros:
the trace is computed from the Schur quotient resolvent or, equivalently,
from `T_+'/T_+`.  The required proof step is to derive `(RTS-3)` directly
from the Gamma-prime cell formula and the rank-two displacement relation,
without replacing it by a hard prime truncation.

## Corrected signed decomposition

P76.037 shows that the uncancelled external sine divisor contributes the
explicit term `B_ext`.  Subtracting it alone changes the observed defect
from positive to negative.  Therefore the theorem-grade comparison must
keep the two high tails coupled:

```text
raw finite trace - Xi trace
= [core Schur trace below R - Xi divisor below R]
 +[external mesh trace above R - Xi divisor above R],  (RTS-4)

R=2*pi*N/L.
```

The second bracket is not discarded termwise.  Its signed asymptotic is
controlled by the explicit mesh sum together with the unconditional
Riemann--von Mangoldt counting law.  The first bracket is the genuinely
arithmetic finite-window trace identity to be obtained from the cell formula.

P76.038 proves the high completed-zeta tail is `O_K(log R/R)` without RH.
Using `Psi_core` removes the external mesh bracket completely.  Thus the
preferred endpoint is the core finite-window identity `CELL-TRACE-WINDOW`.
