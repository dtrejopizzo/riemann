# 107.189 -- The semilocal determinant system descends to a line sheaf on Spec Z

## 1. Coefficient domain and semilocal basis

Let

\[
 \mathcal H=\{s\in\mathbb C:\Re(s)>1\},
 \qquad A=\mathcal O(\mathcal H).
\]

For a finite set \(S\) of rational primes, put

\[
 U_S=\mathrm{Spec}\,\mathbb Z\setminus S.
\]

If \(S\subset T\), then \(U_T\subset U_S\).  On \(\mathcal H\), every
local Euler section

\[
 z_p(s)=(1-p^{-s})^{-1}
\]

is a unit of \(A\).

## 2. Line presheaf

Define a free rank-one \(A\)-module on each semilocal basic open:

\[
 \mathscr L(U_S)=A e_S.
\]

For \(S\subset T\), define restriction by

\[
 r_{S,T}(f e_S)
 =f\prod_{p\in T\setminus S}z_p\,e_T.
 \tag{2.1}
\]

The transition cocycle of `107_188` proves functoriality.

## 3. Sheaf descent

Set

\[
 g_S=\prod_{p\in S}z_p.
\]

The frame change

\[
 \phi_S:Ae_S\longrightarrow A,
 \qquad \phi_S(f e_S)=f/g_S
 \tag{3.1}
\]

intertwines every restriction (2.1) with the identity restriction on
the constant rank-one \(A\)-module:

\[
 \phi_T(r_{S,T}(f e_S))={f\prod_{T\setminus S}z_p\over
 g_S\prod_{T\setminus S}z_p}={f\over g_S}.
\]

Therefore \(\mathscr L\) satisfies sheaf descent on the semilocal
Zariski basis.  Explicitly, for distinct primes \(p,q\), the Cech
equalizer for

\[
 U_{S\cup\{p\}}\cup U_{S\cup\{q\}}=U_S
\]

is exact: compatible local sections \(a e_{S,p}\), \(b e_{S,q}\)
satisfy

\[
 az_q=bz_p
\]

and glue uniquely to \((a/z_p)e_S=(b/z_q)e_S\).

Hence \(\mathscr L\) is an invertible spectral determinant-line sheaf
on \(\mathrm{Spec}\,\mathbb Z\) with coefficients in
\(\mathcal O(\mathcal H)\).

## 4. Canonical section and generic completion

Let

\[
 Z_\infty(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2).
\]

The chartwise sections

\[
 \sigma_S=Z_\infty(s)g_S(s)e_S
 \tag{4.1}
\]

are compatible under (2.1), so they define a global section of
\(\mathscr L\).  In the completed generic frame obtained by taking the
cofinal product over all primes, (4.1) is

\[
 \sigma_\eta(s)=\xi(s)
 \qquad(\Re s>1).
\]

## 5. Exact scope

This constructs a genuine rank-one sheaf on the arithmetic **curve**
\(\mathrm{Spec}\,\mathbb Z\), using the actual semilocal
restrictions.  It is spectral-parameter-valued and its completed generic
section is \(\xi\).

It is not yet the line bundle needed on the absolute arithmetic
**square**.  No external product, diagonal pullback, Deligne pairing,
metric, or self-intersection is constructed here.  Extension from
\(\mathcal H\) across the critical strip also requires meromorphic or
derived coefficients because individual Euler frames cease to be units.

## 6. Falsifier

The verifier checks basis-cover equalizers, unique gluing, frame-change
trivialization, restriction of the canonical section, and generic
cofinal convergence at real and complex parameters.  Any failed descent
or nonunique glue returns `VERDICT: NO`.
