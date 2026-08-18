# Direct A1 oriented Chebyshev minimal theorem

## Purpose

The direct A1 route has now been reduced past the coefficientwise and
absolute-envelope attempts.  This note records the exact theorem that remains
after `226`, `298`, `299`, and `313`.

It has two roles:

1. state the minimal non-circular direct theorem whose proof would close A1;
2. show that the apparent monotonicity proof is not a proof, because
   nonnegative prime-power mass must be placed with the correct Laguerre
   orientation.

## Direct coefficient form

For \(n\ge9\), set
\[
  G_N(u)=e^{-u}L_N^{(1)}(u),\qquad N=n-1,
\]
and on the high block
\[
  \omega_n(u)=G_N(T_n)-G_N(u),\qquad T_8\le u\le T_n.
\]

The direct certificate of `226` is
\[
\boxed{
  B_n^{\rm base}
  +
  \sum_{T_8\le\log m\le T_n}
  \Lambda(m)\omega_n(\log m)
  \ge0.
}
\tag{1}
\]

Here \(B_n^{\rm base}\) contains the fixed low window, the pole term, and
the archimedean contribution.  The moving high block is the only remaining
oscillatory arithmetic component.

## Lobe partition

Let
\[
  T_8=a_{n,0}<a_{n,1}<\cdots<a_{n,J_n}=T_n
\]
be the partition obtained by inserting the zeros of \(\omega_n\).  On each
open interval \((a_{n,j},a_{n,j+1})\), the sign of \(\omega_n\) is fixed.
Define
\[
  H_{n,j}
  =
  \sum_{a_{n,j}\le\log m<a_{n,j+1}}
  \Lambda(m)\omega_n(\log m).
\]

Then (1) is exactly
\[
\boxed{
  B_n^{\rm base}+\sum_jH_{n,j}\ge0.
}
\tag{2}
\]

Equivalently, with
\[
  H_n^+=\sum_{\omega_n\ge0}H_{n,j},
  \qquad
  H_n^-=-\sum_{\omega_n\le0}H_{n,j},
\]
the direct route is
\[
\boxed{
  H_n^+-H_n^-+B_n^{\rm base}\ge0.
}
\tag{3}
\]

Thus the direct theorem is an oriented dominance theorem.  A bound for
\(H_n^++H_n^-\) is not enough.

## Partial-summation normal form

On a lobe \([a,b)\), define the local prime-power step function
\[
  \Theta_a(u)=\psi(e^u)-\psi(e^a-)
\]
and the local Chebyshev discrepancy
\[
  \mathcal E_a(u)
  =
  \psi(e^u)-e^u-\left(\psi(e^a-)-e^a\right).
\]

Since
\[
  \omega_n'(u)=e^{-u}L_{n-1}^{(2)}(u),
\]
Stieltjes partial summation gives
\[
\boxed{
  H_{[a,b)}
  =
  \Theta_a(b)\omega_n(b)
  -
  \int_a^b\Theta_a(u)e^{-u}L_{n-1}^{(2)}(u)\,du.
}
\tag{4}
\]

Splitting \(\Theta_a(u)=(e^u-e^a)+\mathcal E_a(u)\), write
\[
  H_{[a,b)}=H_{[a,b)}^{\rm main}+H_{[a,b)}^{\rm err},
\]
where
\[
\boxed{
  H_{[a,b)}^{\rm err}
  =
  \mathcal E_a(b)\omega_n(b)
  -
  \int_a^b\mathcal E_a(u)e^{-u}L_{n-1}^{(2)}(u)\,du.
}
\tag{5}
\]

The main terms are explicit endpoint-polynomial quantities.  Therefore the
direct A1 route is exactly the following theorem.

## Minimal direct theorem

For every \(n\ge9\), with the lobe partition above,
\[
\boxed{
  \sum_j H_{n,j}^{\rm err}
  \ge
  -B_n^{\rm base}-\sum_jH_{n,j}^{\rm main}.
}
\tag{6}
\]

Together with the already certified base index \(n=8\), (6) proves
\[
  C_n(T_n)\ge0\qquad(n\ge8).
\]

Conversely, (6) is just the direct certificate after exact lobe partial
summation.  So it is not a sufficient condition stronger than A1; it is the
minimal direct signed Chebyshev theorem still unproved.

## Why the monotonicity proof fails

The tempting shortcut is:
\[
  \Lambda(m)\ge0
  \quad\hbox{and}\quad
  \psi(e^u)\hbox{ is increasing}
  \quad\Longrightarrow\quad
  \sum_m\Lambda(m)\omega_n(\log m)\ge0.
\]

This implication is false because \(\omega_n\) changes sign.  More
precisely, if \(\omega_n\) has one negative lobe \(I^-\) and one positive
lobe \(I^+\), two nonnegative step measures with the same total mass can
place their mass in \(I^-\) or in \(I^+\).  The resulting values of
\[
  \int\omega_n\,d\Theta
\]
then have opposite signs.  Monotonicity of \(\Theta\) controls only the
positivity of the measure, not its placement relative to the Laguerre sign
partition.

The actual prime-power measure may still satisfy (3), but proving that is
exactly the oriented arithmetic theorem.  It cannot be replaced by
positivity of \(\Lambda\), monotonicity of \(\psi\), or a symmetric
Chebyshev envelope.

## Status

Closed as the minimal direct-route theorem and monotonicity no-go.

A proof of (6), for every \(n\ge9\), would complete the direct A1 path.
Without (6) or an equivalent margin-tail/global theorem, the direct route
remains open.
