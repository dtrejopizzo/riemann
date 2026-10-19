# Phase 178 — fermionic interference and the sign gate

## Verdict

The proposed non-quasi-free CAR cumulant does not supply the missing sign.
The obstruction already occurs for two fermionic modes and is independent of
all analytic details of the Weil form.  The affine Robertson variant also
reduces to a Gram inequality already present in the corpus.  Both verdicts are
`PROVED NO-GO`; no conclusion about row D is claimed.

## 1. The proposed connected fermionic term

Let `CAR(C^2)` have number projections

\[
 N_j=a^*(e_j)a(e_j),\qquad j=1,2,
\]

and let `omega` be an even gauge-invariant state.  The connected four-point
term attached to the two modes is

\[
 \kappa_\omega(N_1,N_2)
 =\omega(N_1N_2)-\omega(N_1)\omega(N_2).                 \tag{1}
\]

This is the smallest term that could retain interference between two prime
channels after the disconnected Wick terms are removed.

### Theorem 1 (the connected sign obstruction). `PROVED`

Among positive even gauge-invariant states on `CAR(C^2)`, the quantity (1)
takes positive, negative and zero values.  Explicitly, in the occupation basis
`|00>,|10>,|01>,|11>`, put

\[
 \rho_+=\tfrac12(|00\rangle\langle00|+|11\rangle\langle11|),\quad
 \rho_-=\tfrac12(|10\rangle\langle10|+|01\rangle\langle01|),\quad
 \rho_0=\tfrac14 I.
\]

Then

\[
 \kappa_{\rho_+}=\tfrac14,\qquad
 \kappa_{\rho_-}=-\tfrac14,\qquad
 \kappa_{\rho_0}=0.                                      \tag{2}
\]

**Proof.**  For `rho_+`, the joint occupation law is equally supported on
`(0,0)` and `(1,1)`, so `E(N_1N_2)=1/2` and
`E(N_1)E(N_2)=1/4`.  For `rho_-`, it is equally supported on `(1,0)` and
`(0,1)`, so the two quantities are `0` and `1/4`.  For `rho_0` the occupations
are independent Bernoulli variables of parameter `1/2`.  The three density
matrices are positive, diagonal, even and gauge invariant.  This proves (2).
`QED`

### Corollary 2 (the exact dichotomy). `PROVED`

Subtracting disconnected terms preserves the desired cross-channel
information but destroys positivity.  Retaining the full covariance matrix

\[
 C_{ij}=\omega((N_i-\omega N_i)(N_j-\omega N_j))
\]

restores positivity only in the matrix sense:

\[
 \sum_{i,j}\bar z_iC_{ij}z_j
 =\omega\!\left(\left|\sum_i z_i(N_i-\omega N_i)\right|^2\right)\ge0.
                                                               \tag{3}
\]

Equation (3) is an ordinary Gram square.  Its off-diagonal entries still have
both signs by Theorem 1.  Hence state positivity alone cannot give the sign of
the connected Euler–Euler or Euler–Poisson component.  A higher non-quasi-free
sector does not repair the missing implication unless it adds a new theorem
that constrains the state beyond positivity.

This closes the residual higher-sector opening in `G1_B10_R5` for the proposed
use: higher sectors may contain new correlations, but those correlations have
no universal scalar sign.

## 2. The affine uncertainty variant

The affine integer carrier of `P122_024` has

\[
 V_p^*HV_p=H+(\log p)I,
 \qquad [H,V_p]=(\log p)V_p,                         \tag{4}
\]

and `V_pS=S^pV_p`.  Thus a commutator can indeed manufacture the exact
coefficient `log p` before the spectrum is introduced.

### Theorem 3 (Robertson does not orient the contact). `PROVED`

Let `A,B` be self-adjoint observables on a common domain and `u` a unit vector.
Robertson's inequality

\[
 \operatorname{Var}_u(A)\operatorname{Var}_u(B)
 \ge \tfrac14|\langle u,[A,B]u\rangle|^2             \tag{5}
\]

cannot supply an oriented linear Euler term.

**Proof.**  Formula (5) is the nonnegativity of the `2 by 2` Gram determinant
of `(A-\langle A\rangle)u` and `(B-\langle B\rangle)u`.  It contains the
commutator only through its absolute square, so it is invariant under
`[A,B] -> -[A,B]`.  If `A,B` have real matrices and `u` is real, then
`[A,B]` is real skew-symmetric and `\langle u,[A,B]u\rangle=0`.  If complex
phases are allowed, replacing `u` by its conjugate reverses the imaginary
commutator expectation while leaving both variances fixed.  Therefore (5)
does not choose the orientation required by the Weil prime term. `QED`

For `A=H` and a self-adjoint combination of `V_p,V_p^*`, (4) gives the right
coefficient but Theorem 3 loses its sign.  This is compatible with
`R160_C8_R1`, where Robertson's commutator vanishes on real tests, and with
`P122_028`, where the affine Green energy detects the seam but does not force
zero flux.

## 3. Consequence for the search

The following necessary condition is now exact.

> A successful interference mechanism cannot obtain its scalar sign merely
> from positivity of a state, a connected cumulant, or a two-observable Gram
> determinant.  It must prove an arithmetic restriction on the admissible
> joint state that excludes `rho_-`, while simultaneously retaining an
> oriented term linear in the affine commutator (4).

This restriction must use `Lambda*1=log` and Poisson–Tate jointly.  Without it,
the construction lands on one side of the dichotomy above: signed but
indefinite connected interference, or positive but unoriented Gram energy.

## 4. Status map

```text
higher CAR sector retains cross-prime interference       PROVED
connected fourth cumulant has a fixed sign                REFUTED
full covariance is positive                               PROVED
full covariance gives an oriented prime term              REFUTED
affine commutator produces log p                           PROVED (P122_024)
Robertson preserves the commutator orientation             REFUTED
arithmetic restriction excluding anticorrelation rho_-     OPEN
row D                                                       OPEN
```

