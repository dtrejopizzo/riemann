# R170_888 — Minimality ledger in Z_N coordinates and the parity wall

## 0. Result

Under REG/C1, at fixed cutoff `M,N`, and inside a chamber with no
births, the derivative of the minimal eigenvalue admits an exact
expansion in the same coordinates `Z_N=S_N-C_N` of R170_885. The
minimality sign reaches the full sum, but not the linear
Euler--Maclaurin residue.

Set

\[
 \mathscr B_N:=(PS_NP)^{-1},\qquad
 \mathcal P_{C,A}:=C_N\dot A_M-\dot C_NA_M.               \tag{0.1}
\]

Then R170_856(9.4) gives

\[
\boxed{
 P\dot A_MF=
 \mathscr B_NP(Z_N\dot A_M-\dot Z_NA_M)F
 +\mathscr B_NP\mathcal P_{C,A_M}F
 +\mathcal P^{\rm comb}_{N,T}(F).}                       \tag{0.2}
\]

Inserting it into the moving Hellmann--Feynman derivative gives the
identity

\[
\boxed{
\begin{aligned}
 \nu={}&\operatorname{Re}
  (F,\mathscr B_NP(Z_N\dot A_M-\dot Z_NA_M)F)\\
 &+\operatorname{Re}(F,\mathscr B_NP\mathcal P_{C,A_M}F)\\
 &+\operatorname{Re}(F,\mathcal P^{\rm comb}_{N,T}(F))\\
 &+2\operatorname{Re}(A_MF,(\dot P-\dot R_T)F)\le0.
\end{aligned}}                                           \tag{0.3}
\]

This is the minimality equation correctly coupled to the polar term and
the Tate port. The sum is gauge-invariant; none of its four lines is
invariant nor carries a sign on its own.

## 1. Derivation

For the normalized branch

\[
 \Pi_sA_{M,s}\Pi_sF_s=\lambda_sF_s,
 \qquad \Pi_s=P_s-R_{T,s},                               \tag{1.1}
\]

R170_887 gives

\[
 \nu=\operatorname{Re}(F,\dot A_MF)
 +2\operatorname{Re}(A_MF,(\dot P-\dot R_T)F).           \tag{1.2}
\]

Since `F` is supported and primitive,
`(F,dot A_MF)=(F,P dot A_MF)`. Substituting the exact identity (0.2)
proves (0.3). The polar term is not separated before applying the causal
inverse, and `P` is not moved across the operators.

Under an infinitesimal gauge change with anti-adjoint generator `Omega`,
`dot A` changes by a commutator and `dot Pi` by the opposite commutator. At
contact, their contributions to (1.2) cancel. This verifies the
invariance of the sum and forbids attributing intrinsic meaning to a single
isolated line of (0.3).

## 2. Content of the three blocks

The first block keeps the full renormalized PC. Its expansion
contains the incomplete hyperbola `H_(M,N)`, `A_raw`, and its tail in
`N<k<=MN`; the Chebyshev jet has already cancelled as in R170_856.

The second block keeps the polar continuum, including the moving
face of `dot C_N`. The third is

\[
 \mathcal P^{\rm comb}_{N,T}(F)
 =\mathscr B_NP\dot S_NA_MF
  -\mathscr B_NPS_NQ\dot A_MF,                            \tag{2.1}
\]

and it retains the routes that cross the window and their atoms. The
last line of (0.3) contains the motion of the support and the Tate
connection.

In the coordinates of R170_885, the linear residue also keeps

\[
 Q\partial_t[R_M^*b+\mathcal E_{N,T}b
 -\mathcal L^{\rm cont}_{N,T}b],                          \tag{2.2}
\]

`(R_M+R_M^*)dot F`, and the other occurrences of `R_M`. Here
`mathcal E_(N,T)` contains the tail `U_N`. None of these tails cancels
when passing from R170_887 to (0.3).

## 3. The exact wall

Identity (0.3) is quadratic and even:

\[
 \nu(-F)=\nu(F).                                         \tag{3.1}
\]

The residue of R170_885 and its covariant completion R170_887(5.1) are
linear and odd. Hence they cannot be a single isolated line of (0.3), nor
inherit the sign `nu<=0`. A one-sided inequality for that functional
on the whole radical already implies its vanishing by applying it to `F` and
`-F`.

This rules out the strategy of identifying `R_EM` with `dot lambda`.
Minimality can only enter via an additional odd identity
linking the EM anchor to the branch connection and making the sum of
R170_887(5.1) zero.

## 4. Unconditional version on the collar

Without REG/C1, `dot P`, `dot Pi`, and `dot lambda` are not proved to be
operators. The available identity is the finite collar difference of
R162_405(2.2lambda):

\[
 (\lambda_\delta-\lambda_0)
 \langle F_\delta,E_\delta F\rangle
 =\langle\xi_F^\delta,F_\delta|_{C_\delta}\rangle.        \tag{4.1}
\]

At first contact `lambda_0=0`. Equation (4.1) incorporates the motion
of the window and the births of new prime powers. It only signs the
total pairing. To get an unconditional law, the EM vanishing must be
lifted to (4.1) before taking `delta->0`.

## 5. Status

```text
Z_N ledger of the minimal derivative, (0.3)                PROVED UNDER REG/C1
preservation of the polar term, port, U_N, and R_M          PROVED
sign of the full sum                                        PROVED VIA MINIMALITY
separate sign of the linear EM residue                       REFUTED BY PARITY
identification R_EM=dot lambda                                REFUTED
available finite collar identity                               IMPORTED FROM R162_405
odd lift of EM to the finite identity                           OPEN
VIR--LB / D                                                     OPEN
```
