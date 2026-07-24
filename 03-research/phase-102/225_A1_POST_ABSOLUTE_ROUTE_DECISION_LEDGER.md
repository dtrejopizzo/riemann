# A1 post-absolute-route decision ledger

## Purpose

This ledger records the current decision state after `217`--`224`.

The important change is that the absolute VK route has been audited to the
end of its natural life:

1. the base sign \(C_8^\ast>0\) is closed;
2. the terminal asymptotic obstruction is closed;
3. the raw mixed off-diagonal kernel collapses algebraically;
4. the resulting absolute single-Laguerre \(L^1\) load is too large for VK
   envelopes;
5. the integrated \(B\)-envelope variant fails for the same reason.

Therefore A1 should no longer spend effort on symmetric VK-size estimates.
The remaining viable routes must use signed arithmetic information or an
RH-strength theorem.

## Closed gates

### Base sign

`217_N8_BASE_MARGIN_CERTIFICATE.md` proves
\[
  \lambda_8-{1\over2}\lambda_8^{\rm arch}>0.
\]
Together with A0,
\[
  C_8^\ast>0.
\]

### Terminal asymptotic sign

`215` and `220` give
\[
  \Gamma_{\mathcal B}>{25\over64},
\]
while the canonical VK terminal load is \(O(\log n)\).  Hence the terminal
interval is absorbed for all sufficiently large \(n\).  The remaining
terminal task is only the finite rational threshold certificate
\[
  \mathfrak D_n=\mathcal B_n-\Theta_n\ge0.
\]

### Mixed structural obstruction

`219` proves
\[
  \mathcal H_n(u)=-L_{n-1}^{(2)}(u)
  \qquad(T_8<u<T_n),
\]
with only two low-cutoff degree-7 correction intervals.  Thus the raw
off-diagonal mixture obstruction is closed.

## Discarded gates

### Absolute VK \(L^1\)

`221` shows that the collapsed absolute load contains the bulk term
\[
  \int_{T_8}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du.
\]
For VK envelopes this is exponential in \(n\), because Laguerre bulk growth
has factor \(e^{u/2}\) on \(u\asymp n\), while VK relative decay is only
subexponential.  It cannot be dominated by
\[
  \mathcal B_n=O(n^2).
\]

### Symmetric \(B\)-envelope

`223` shows that the integrated signed route cannot be closed by a
two-sided envelope for
\[
  B(U)=\int_0^U(\psi(e^v)-e^v)\,dv.
\]
Such an envelope creates an absolute load for \(L_{n-1}^{(3)}\), and the
same bulk obstruction applies.

## Current exact signed target

The smallest signed target is `222`:
\[
\boxed{
  \mathcal A_n+\Pi_n^{\rm tel}
  +\sum_{m\le e^{T_n}}\Lambda(m)\Xi_n^{\rm tel}(m)\ge0
  \qquad(n\ge9).
}
\tag{1}
\]

This is a finite prime-power inequality for each \(n\), with only two
cutoff jumps \(T_7,T_8\).  It is not yet proved uniformly.

## Remaining viable closure routes

A1 can now close only through one of the following:

1. prove the signed finite inequality (1) uniformly in \(n\);
2. prove a one-sided tail theorem that gives sign information stronger than
   A0;
3. prove the strong margin
   \[
     \lambda_n\ge {1\over2}\lambda_n^{\rm arch}
     \qquad(n\ge8),
   \]
   which `224` identifies as RH-strength;
4. prove a non-circular comparative Loewner--Schur theorem;
5. prove the global half-plane theorem.

## Status

Closed as a decision ledger.

A1 remains open.  The absolute VK strategy is discarded; the next work must
target signed arithmetic or an RH-strength theorem.
