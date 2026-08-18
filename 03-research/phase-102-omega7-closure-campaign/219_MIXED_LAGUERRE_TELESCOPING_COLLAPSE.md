# Mixed Laguerre telescoping collapse

## Purpose

`211_MIXED_INTERVAL_OFFDIAGONAL_LOAD_GATE.md` and
`218_MIXED_A0_DEGREE_MISMATCH_AUDIT.md` analyze the cumulative kernel on
the intervals \((T_j,T_{j+1})\) in its raw off-diagonal form.  In that form
it appears to contain all degrees \(k-1\) with \(j+1\le k\le n-1\).

This note records the cancellation built into the weights
\[
  w_{n,k}={1\over2}\left({n(n+1)\over k(k+1)}-1\right).
\]
After a Laguerre telescoping identity, every interval with \(j\ge8\)
collapses to the single terminal polynomial
\[
  -L_{n-1}^{(2)}.
\]

Thus the mixed obstruction is not a high-degree off-diagonal mixture on
the intervals \((T_j,T_{j+1})\) for \(j\ge8\).  It is reduced to a global
single-Laguerre \(L^1\) problem, plus two low-cutoff exceptional intervals.

## Laguerre identity

Use
\[
\boxed{
  uL_{k-1}^{(2)}(u)
  =
  (k+1)L_{k-1}^{(1)}(u)-kL_k^{(1)}(u).
}
\tag{1}
\]

Let
\[
  N=n(n+1).
\]
Then
\[
  w_{n,k}={1\over2}\left({N\over k(k+1)}-1\right),
\]
and the adjacent coefficient difference is
\[
\begin{aligned}
  (r+2)w_{n,r+1}-rw_{n,r}
  &=
  {1\over2}\left({N\over r+1}-(r+2)\right)
  -
  {1\over2}\left({N\over r+1}-r\right)\\
  &=-1.
\end{aligned}
\tag{2}
\]

This constant difference is the whole cancellation.

## Telescoping the off-diagonal sum

For \(7\le j\le n-2\), put
\[
  S_{j,n}(u)
  =
  u\sum_{k=j+1}^{n-1}w_{n,k}L_{k-1}^{(2)}(u).
\]

Applying (1) and (2),
\[
\boxed{
  S_{j,n}(u)
  =
  (j+2)w_{n,j+1}L_j^{(1)}(u)
  -
  \sum_{r=j+1}^{n-2}L_r^{(1)}(u)
  -
  (n-1)w_{n,n-1}L_{n-1}^{(1)}(u).
}
\tag{3}
\]

Since
\[
  (n-1)w_{n,n-1}=1
\]
and
\[
  \sum_{r=j+1}^{n-2}L_r^{(1)}(u)
  =
  L_{n-2}^{(2)}(u)-L_j^{(2)}(u),
\tag{4}
\]
we get
\[
\boxed{
  S_{j,n}(u)
  =
  (j+2)w_{n,j+1}L_j^{(1)}(u)
  -
  L_{n-2}^{(2)}(u)
  +
  L_j^{(2)}(u)
  -
  L_{n-1}^{(1)}(u).
}
\tag{5}
\]

Finally,
\[
  L_m^{(2)}(u)=L_m^{(1)}(u)+L_{m-1}^{(2)}(u).
\tag{6}
\]

## Interior intervals \(8\le j\le n-2\)

From `197`, on \((T_j,T_{j+1})\) with \(8\le j\le n-2\),
\[
\begin{aligned}
  \mathcal H_n(u)
  &=
  S_{j,n}(u)
  -
  w_{n,j}jL_j^{(2)}(u)
  +
  w_{n,j+1}(j+2)L_{j-1}^{(2)}(u).
\end{aligned}
\tag{7}
\]

Using (6),
\[
  L_j^{(1)}(u)+L_{j-1}^{(2)}(u)=L_j^{(2)}(u),
\]
so the \(j\)-level contribution in (7) has coefficient
\[
  1+(j+2)w_{n,j+1}-jw_{n,j}.
\]
By (2), this coefficient is \(0\).  Hence
\[
\boxed{
  \mathcal H_n(u)
  =
  -L_{n-2}^{(2)}(u)-L_{n-1}^{(1)}(u)
  =
  -L_{n-1}^{(2)}(u),
  \qquad T_j<u<T_{j+1},\ 8\le j\le n-2.
}
\tag{8}
\]

Together with the terminal identity from `197`,
\[
  \mathcal H_n(u)=-L_{n-1}^{(2)}(u),
  \qquad T_{n-1}<u<T_n,
\tag{9}
\]
this gives
\[
\boxed{
  \mathcal H_n(u)=-L_{n-1}^{(2)}(u),
  \qquad T_8<u<T_n.
}
\tag{10}
\]

The apparent high-degree cumulative mixture on all intervals after \(T_8\)
therefore collapses exactly.

## Exceptional interval \((T_7,T_8)\)

For \(j=7\), the middle term \(-w_{n,7}7L_7^{(2)}\) is absent because the
cumulative recurrence starts at \(k=8\).  Formula (7) is replaced by
\[
  \mathcal H_n(u)=S_{7,n}(u)+9w_{n,8}L_6^{(2)}(u).
\]

Using (5)--(6),
\[
\boxed{
  \mathcal H_n(u)
  =
  -L_{n-1}^{(2)}(u)
  +
  \alpha_n L_7^{(2)}(u),
  \qquad T_7<u<T_8,
}
\tag{11}
\]
where
\[
\boxed{
  \alpha_n
  =
  1+9w_{n,8}
  =
  {n(n+1)-56\over16}.
}
\tag{12}
\]

Thus the first cutoff interval is a single high-degree Laguerre polynomial
plus one fixed low-degree correction.

## Initial interval \((0,T_7)\)

On \((0,T_7)\), no endpoint correction is present:
\[
  \mathcal H_n(u)=S_{7,n}(u).
\]
Therefore
\[
\boxed{
  \mathcal H_n(u)
  =
  -L_{n-1}^{(2)}(u)
  +
  L_7^{(2)}(u)
  +
  \beta_n L_7^{(1)}(u),
  \qquad 0<u<T_7,
}
\tag{13}
\]
with
\[
\boxed{
  \beta_n=9w_{n,8}={n(n+1)-72\over16}.
}
\tag{14}
\]

Again, the only correction to the terminal Laguerre polynomial has fixed
degree \(7\).

## Collapsed weighted \(L^1\) load

For a relative envelope \(|E(e^u)|\le e^u\varepsilon(u)\), the exact
absolute load becomes
\[
\boxed{
\begin{aligned}
  W_n(\varepsilon)
  &=
  \int_0^{T_7}
  \varepsilon(u)
  \left|
    -L_{n-1}^{(2)}(u)
    +
    L_7^{(2)}(u)
    +
    \beta_nL_7^{(1)}(u)
  \right|du\\
  &\quad+
  \int_{T_7}^{T_8}
  \varepsilon(u)
  \left|
    -L_{n-1}^{(2)}(u)
    +
    \alpha_nL_7^{(2)}(u)
  \right|du\\
  &\quad+
  \int_{T_8}^{T_n}
  \varepsilon(u)|L_{n-1}^{(2)}(u)|\,du .
\end{aligned}
}
\tag{15}
\]

Consequently the absolute diagonal route is now the single theorem
\[
\boxed{
  \mathcal B_n\ge W_n(\varepsilon)
  \qquad(n\ge9),
}
\tag{16}
\]
with \(W_n\) given by (15), together with the already closed base sign
from `217`.

## What this closes

This closes the structural mixed off-diagonal obstruction from `211`.
There is no remaining need for a zero theorem for the raw cumulative
mixtures on \((T_j,T_{j+1})\) with \(j\ge8\), because those mixtures are
identically \(-L_{n-1}^{(2)}\).

It also supersedes the crude no-go in `218`: the triangle estimate of the
un-telescoped sum is indeed too crude, but the correct algebraic step is
not an off-diagonal bound.  It is the telescoping collapse above.

## What remains open

This note does not close A1.  It reduces the absolute route to a sharper
single-Laguerre weighted \(L^1\) theorem:
\[
  \int_{T_8}^{T_n}\varepsilon(u)|L_{n-1}^{(2)}(u)|\,du
\]
plus the two low-cutoff correction intervals (13) and (11).

Thus the remaining absolute-route tasks are:

1. prove the uniform single-Laguerre load bound (16);
2. make the terminal/whole-range threshold effective for the chosen
   Vinogradov--Korobov profile;
3. or replace the absolute route by the signed finite certificate of `190`.

## Status

Closed as a mixed-kernel telescoping theorem.

A1 remains open.  The off-diagonal mixture obstruction is closed, but the
collapsed single-Laguerre \(L^1\) domination still has to be proved.
