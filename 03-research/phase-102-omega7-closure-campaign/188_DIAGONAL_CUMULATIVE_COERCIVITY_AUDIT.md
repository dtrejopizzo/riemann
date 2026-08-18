# Diagonal cumulative coercivity audit

## Purpose

`186_CUMULATIVE_DIAGONAL_FORCING_KERNEL.md` reduces the diagonal induction
route to the finite signed inequality
\[
\begin{aligned}
  \mathcal S_n
  &=
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right)\\
  &\quad+
  \int_0^{T_n}E(e^u)e^{-u}\mathcal H_n(u)\,du
  \ge0
  \qquad(n\ge9),
\end{aligned}
\tag{1}
\]
where
\[
  w_{n,k}
  =
  {1\over2}
  \left({n(n+1)\over k(k+1)}-1\right)>0
  \qquad(8\le k\le n-1).
\tag{2}
\]

This note audits whether (1) has an automatic coercive positivity principle.
The conclusion is negative for the natural symmetric classes: a coercive
bound that uses only a two-sided envelope for \(E=\psi-y\) collapses exactly
to the absolute-value bound.  Therefore the diagonal cumulative form is a
valid exact target, but it does not by itself create a sign advantage.

## Normalized form

Define the explicit base-archimedean term
\[
\boxed{
  \mathcal B_n
  =
  C_8^\ast
  +
  {n(n+1)-72\over16}\Delta_8^\ast
  +
  \sum_{k=8}^{n-1}
  w_{n,k}\left(1+{3\over4}D_k^{\rm arch}\right).
}
\tag{3}
\]

Also define the signed measure
\[
  d\mu_n(u)=e^{-u}\mathcal H_n(u)\,du
  \qquad(0\le u\le T_n).
\tag{4}
\]

Then (1) is simply
\[
\boxed{
  \mathcal S_n=\mathcal B_n+\int_0^{T_n}E(e^u)\,d\mu_n(u)\ge0.
}
\tag{5}
\]

Thus every diagonal-induction proof must produce
\[
\boxed{
  \int_0^{T_n}E(e^u)\,d\mu_n(u)\ge-\mathcal B_n.
}
\tag{6}
\]

The question is whether (6) follows from a coercive property of
\(\mu_n\), independent of a signed arithmetic theorem for \(E\).

## Symmetric-envelope lemma

Let \(R(u)\ge0\) be any measurable envelope on \([0,T_n]\).  Consider all
signed functions \(G\) satisfying
\[
  |G(u)|\le R(u).
\tag{7}
\]

For the linear functional
\[
  L_n(G)=\int_0^{T_n}G(u)\,d\mu_n(u),
\tag{8}
\]
one has the exact variational identity
\[
\boxed{
  \inf_{|G|\le R} L_n(G)
  =
  -\int_0^{T_n}R(u)\,d|\mu_n|(u)
  =
  -\int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
}
\tag{9}
\]

Indeed, the lower bound follows from
\[
  L_n(G)\ge-\int_0^{T_n}|G(u)|\,d|\mu_n|(u)
  \ge-\int_0^{T_n}R(u)\,d|\mu_n|(u).
\tag{10}
\]
Equality is obtained, up to the usual null-set convention, by choosing
\[
  G(u)=-R(u)\,\mathrm{sgn}\,\mathcal H_n(u).
\tag{11}
\]

Therefore any proof that uses only the symmetric information
\[
  |E(e^u)|\le R(u)
\tag{12}
\]
can prove at most
\[
\boxed{
  \mathcal S_n
  \ge
  \mathcal B_n
  -
  \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du.
}
\tag{13}
\]

This is exactly the absolute-value estimate.  It contains no hidden
coercive gain from the cumulative weights \(w_{n,k}\).

## Consequence for diagonal coercivity

A symmetric-envelope route can close the diagonal induction only if it
proves the explicit sufficient inequality
\[
\boxed{
  \mathcal B_n
  \ge
  \int_0^{T_n}R(u)e^{-u}|\mathcal H_n(u)|\,du
  \qquad(n\ge9).
}
\tag{14}
\]

This is a legitimate sufficient theorem, but it is not a new signed
mechanism.  It is the same loss-of-sign strategy that A1 was designed to
avoid, now applied to the cumulative diagonal kernel.

In particular:

1. positivity of the weights \(w_{n,k}\) does not imply
   \(\mathcal H_n\ge0\);
2. even if \(\mathcal H_n\ge0\) on some subinterval, a two-sided bound on
   \(E\) still gives the lower extremizer \(G=-R\);
3. any coercive inequality stronger than (13) must use arithmetic
   information excluding the extremal sign pattern (11).

Thus the cumulative diagonal form has no automatic Hilbert-space
coercivity analogous to
\[
  \int |P|^2\,d\nu\ge0.
\]
It is a linear signed pairing, not a quadratic positive form.

## One-sided arithmetic information that would suffice

The preceding no-go is only for symmetric envelopes.  A proof can still
close (6) by giving a one-sided arithmetic theorem adapted to \(\mu_n\).

For example, suppose \(E\) is decomposed as
\[
  E(e^u)=E_+(u)-E_-(u)
\tag{15}
\]
and the positive and negative variations of \(\mu_n\) are
\[
  \mu_n=\mu_n^+-\mu_n^-.
\tag{16}
\]

Then
\[
  \int E\,d\mu_n
  =
  \int E\,d\mu_n^+
  -
  \int E\,d\mu_n^-.
\tag{17}
\]

A useful theorem would have to prove a genuine imbalance such as
\[
\boxed{
  \int_0^{T_n}E(e^u)\,d\mu_n(u)
  +
  \mathcal B_n
  \ge0
}
\tag{18}
\]
directly from prime-power structure, or else prove sharper one-sided
controls on the four pairings
\[
  \int E_\pm\,d\mu_n^\pm
\tag{19}
\]
that are incompatible with the extremizer (11).

This is the exact meaning of a coercive diagonal theorem: it must show that
the actual Chebyshev error does not align with the negative sign pattern of
\(\mathcal H_n\) strongly enough to defeat \(\mathcal B_n\).

## Finite certificate form

Because \(\mathcal H_n\) is supported on \([0,T_n]\), (18) is a finite
prime-power statement.  Writing \(X_n=e^{T_n}\), the integral can be expanded
as
\[
  \int_0^{T_n}(\psi(e^u)-e^u)e^{-u}\mathcal H_n(u)\,du.
\tag{20}
\]

After integrating the step function \(\psi(e^u)\), this becomes
\[
  \sum_{m\le X_n}\Lambda(m)
  \int_{\log m}^{T_n}e^{-u}\mathcal H_n(u)\,du
  -
  \int_0^{T_n}\mathcal H_n(u)\,du.
\tag{21}
\]

Thus the useful target is the finite inequality
\[
\boxed{
  \mathcal B_n
  +
  \sum_{m\le X_n}\Lambda(m)
  \int_{\log m}^{T_n}e^{-u}\mathcal H_n(u)\,du
  -
  \int_0^{T_n}\mathcal H_n(u)\,du
  \ge0
  \qquad(n\ge9).
}
\tag{22}
\]

This is not a numerical certificate unless proved uniformly in \(n\), but it
is the exact arithmetic form of diagonal coercivity.

## No-go statement

The following proof pattern is invalid:

1. combine the diagonal recurrence into \(\mathcal H_n\);
2. note that the cumulative weights \(w_{n,k}\) are positive;
3. apply a two-sided PNT or Chebyshev envelope to \(E\);
4. claim a coercive lower bound better than (13).

Step 4 is impossible by the symmetric-envelope lemma.  The extremal
two-sided function \(G=-R\,\mathrm{sgn}\,\mathcal H_n\) saturates the
absolute-value loss.

Therefore the diagonal cumulative route remains viable only in one of two
forms:

- prove the absolute sufficient inequality (14), with constants strong
  enough on the compact range; or
- prove the genuinely signed finite arithmetic inequality (22), or an
  equivalent one-sided balance theorem, uniformly for every \(n\ge9\).

## Exact status

Closed as a coercivity audit.  A1 remains open.

The cumulative diagonal kernel is an exact compression of the induction
route, but it is not a positive kernel and it does not create coercivity
from symmetric size bounds.  The remaining proof load is a one-sided
arithmetic theorem for the finite prime-power expression (22), or a
successful absolute bound of the explicit form (14).
