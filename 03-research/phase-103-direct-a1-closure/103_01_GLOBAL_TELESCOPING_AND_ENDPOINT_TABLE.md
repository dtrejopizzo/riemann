# Global telescoping identity and endpoint table

Work order step 1 of `PHASE_103_A1_DIRECT_CLOSURE_GUIDE.md`.

## Purpose

Prove the global Stieltjes identity (7) of the guide with exact endpoint
conventions, derive the closed form of the reserve \(Q_n\), and prove that
the resulting inequality
\[
  \mathcal R_n\le Q_n
\]
is *identical* to the direct certificate (3), not a stronger sufficient
condition.

## Notation

Throughout \(n\ge9\) and
\[
  N=n-1,
  \qquad
  G_N(u)=e^{-u}L_N^{(1)}(u),
  \qquad
  K_n(u)=e^{-u}L_{n-1}^{(2)}(u),
\]
\[
  \omega_n(u)=G_N(T_n)-G_N(u),
  \qquad
  \Phi(u)=\psi(e^u),
  \qquad
  E(u)=\psi(e^u)-e^u .
\]
\(\Phi\) is right continuous and nondecreasing, \(\Phi(u)=0\) for
\(u<\log2\).  \(T_7<T_8<\dots<T_n\) are the A0 cutoffs;  \(T_8\) is fixed.

## Lemma 1 (kernel derivative)

For every \(m\ge0\) and every \(\alpha\),
\[
  {d\over du}\Bigl(e^{-u}L_m^{(\alpha-1)}(u)\Bigr)
  =-e^{-u}L_m^{(\alpha)}(u).
\tag{1}
\]

*Proof.*  \(\frac{d}{du}L_m^{(\beta)}=-L_{m-1}^{(\beta+1)}\) and
\(L_m^{(\beta+1)}=L_m^{(\beta)}+L_{m-1}^{(\beta+1)}\).  Hence
\[
  e^{u}{d\over du}\bigl(e^{-u}L_m^{(\alpha-1)}\bigr)
  =-L_{m-1}^{(\alpha)}-L_m^{(\alpha-1)}
  =-L_m^{(\alpha)} .\qquad\square
\]

Two consequences used constantly:
\[
  \boxed{\ \omega_n'(u)=K_n(u),\qquad \omega_n(T_n)=0,\ }
\tag{2}
\]
\[
  \boxed{\ {d\over du}L_n^{(1)}(u)=-L_{n-1}^{(2)}(u),
  \qquad L_n^{(1)}(0)=n+1 .\ }
\tag{3}
\]

## Lemma 2 (global telescoping with endpoints)

Let \(f\in C^1[a,b]\).  With the convention that the high block is
\[
  \sum_{a\le\log m\le b}\Lambda(m)f(\log m)
  =\int_{[a,b]}f\,d\Phi ,
\]
one has, writing \(\Phi(a-)=\lim_{v\uparrow a}\Phi(v)\),
\[
\boxed{
\begin{aligned}
  \int_{[a,b]}f\,d\Phi
  &=\int_a^b f(u)e^u\,du
   +f(b)E(b)-f(a)E(a-)
   -\int_a^bE(u)f'(u)\,du .
\end{aligned}}
\tag{4}
\]

*Proof.*  Riemann–Stieltjes integration by parts on the closed interval
gives \(\int_{[a,b]}f\,d\Phi=f(b)\Phi(b)-f(a)\Phi(a-)-\int_a^b\Phi f'\,du\).
Substitute \(\Phi(u)=e^u+E(u)\) and integrate the smooth part by parts once
more,
\(\int_a^be^uf'\,du=f(b)e^b-f(a)e^a-\int_a^bf(u)e^u\,du\).  \(\square\)

Applying (4) with \(f=\omega_n\), \(a=T_8\), \(b=T_n\), and using
\(\omega_n(T_n)=0\) and \(\omega_n'=K_n\):

\[
\boxed{
\begin{aligned}
  \sum_{T_8\le\log m\le T_n}\Lambda(m)\,\omega_n(\log m)
  &=\int_{T_8}^{T_n}\omega_n(u)e^u\,du
   -E(T_8-)\,\omega_n(T_8)\\
  &\qquad-\int_{T_8}^{T_n}E(u)K_n(u)\,du .
\end{aligned}}
\tag{5}
\]

This is equation (7) of the guide, now with the conventions fixed.

## Endpoint table

| location | prime power \(m\) with \(\log m=\) endpoint | term produced | convention sensitivity |
|---|---|---|---|
| right endpoint \(T_n\) | \(\Lambda(m)\omega_n(T_n)\) | \(0\), since \(\omega_n(T_n)=0\) | **none** |
| right endpoint \(T_n\), boundary term | \(\omega_n(T_n)E(T_n)\) | \(0\) | **none** |
| left endpoint \(T_8\), included in block | contributes \(\Lambda(m)\omega_n(T_8)\) | boundary term uses \(E(T_8-)\) | matched |
| left endpoint \(T_8\), excluded from block | contributes \(0\) | boundary term uses \(E(T_8)\) | matched |

The first row is the decisive one: **the moving endpoint carries no
convention ambiguity at all**, because the cutoff enters the certificate
only through \(\omega_n\), which vanishes there.  The only convention that
must be declared is at the fixed endpoint \(T_8\), and the two admissible
declarations differ by the finite, explicitly computable quantity
\[
  \Bigl(\sum_{\log m=T_8}\Lambda(m)\Bigr)\omega_n(T_8)
  =\bigl(E(T_8)-E(T_8-)\bigr)\omega_n(T_8),
\]
which is \(0\) unless \(e^{T_8}\) is itself a prime power.  Since \(T_8\) is
chosen by the A0 inequality of `102_A0_UNIFORM_TAIL_THEOREM.md` and may be
increased by any amount without weakening A0, we fix once and for all:

> **Convention C.**  \(T_8\) is chosen so that \(e^{T_8}\) is not a prime
> power, and the high block is \(T_8\le\log m\le T_n\).

Under Convention C, \(E(T_8-)=E(T_8)\) and all endpoint corrections vanish
except the single term \(-E(T_8)\omega_n(T_8)\) already displayed in (5).

## The reserve and the correlation

Define, exactly as in the guide,
\[
  Q_n=B_n^{\rm base}
      +\int_{T_8}^{T_n}\omega_n(u)e^u\,du
      -E(T_8)\,\omega_n(T_8),
\tag{6}
\]
\[
  \mathcal R_n=\int_{T_8}^{T_n}E(u)K_n(u)\,du .
\tag{7}
\]

By (5), the direct certificate (3) of the guide reads
\[
  B_n^{\rm base}+\sum_{T_8\le\log m\le T_n}\Lambda(m)\omega_n(\log m)
  =Q_n-\mathcal R_n\ \ge0 .
\]

Hence:

> **Proposition 1 (no strengthening).**
> \[
>   \mathcal R_n\le Q_n
>   \iff
>   B_n^{\rm base}+\sum_{T_8\le\log m\le T_n}\Lambda(m)\omega_n(\log m)\ge0
>   \iff
>   C_n(T_n)\ge0 .
> \]
> The three statements are the same inequality written in three
> coordinate systems; (10) is not a sufficient condition stronger than (3).

The last equivalence is `226` combined with `150`.

## Closed form of the reserve

From `150`, eq. (2),
\[
  C_n(T)= {3\over4}A_n-n-\int_0^{T}E(u)K_n(u)\,du,
  \qquad A_n=\lambda_n^{\rm arch}.
\tag{8}
\]
Taking \(T=T_n\) and splitting the integral at \(T_8\),
\[
  C_n(T_n)=\Bigl[{3\over4}A_n-n-\int_0^{T_8}E K_n\,du\Bigr]-\mathcal R_n .
\]
Comparing with \(C_n(T_n)=Q_n-\mathcal R_n\) gives the closed form demanded
by step 2 of the work order:

> **Theorem 2 (exact reserve).**
> \[
> \boxed{\ Q_n={3\over4}A_n-n-\int_0^{T_8}E(u)K_n(u)\,du\ }
> \tag{9}
> \]
> for every \(n\ge9\).  In particular \(Q_n\) depends on the arithmetic only
> through the prime powers below \(e^{T_8}\), i.e. through fixed finite data,
> exactly as required by (11) of the guide.

No separate expansion of \(B_n^{\rm base}\), of
\(\int\omega_ne^u\,du\), or of the pole term \(P_n\) is needed: those three
quantities are individually of size \(e^{T_n}\)-ish and cancel identically.
Formula (9) is the cancelled form.  This is the single most useful
simplification of the phase: **the reserve never has to be assembled from
the astronomically large pieces the lobe picture suggests.**

## Splitting off the empty range \(m<2\)

Since \(\psi(e^u)=0\) for \(u<\log2\), one has \(E(u)=-e^u\) there, so by (3)
\[
  \int_0^{\log2}E(u)K_n(u)\,du
  =-\int_0^{\log2}L_{n-1}^{(2)}(u)\,du
  =-(n+1)+L_n^{(1)}(\log2).
\tag{10}
\]

Substituting into (9):

> **Corollary 3 (normal form of the reserve).**
> \[
> \boxed{\ Q_n={3\over4}A_n+1-L_n^{(1)}(\log2)
>            -\int_{\log2}^{T_8}E(u)K_n(u)\,du .\ }
> \tag{11}
> \]

This is the decomposition \(Q_n=q(n,T_n)+q_8(n,T_7,T_8)\) of (11) in the
guide, in its sharpest form:

* \(q(n,T_n)=\frac34A_n+1-L_n^{(1)}(\log2)\) is a pure archimedean +
  Laguerre endpoint expression, **independent of \(T_n\) and of all
  arithmetic**;
* \(q_8=-\int_{\log2}^{T_8}EK_n\,du\) involves only primes below
  \(e^{T_8}\).

Note that the \(-n\) of (9) has been cancelled exactly by the trivial
"no primes below 2" contribution \(+(n+1)\).  The apparent linear deficit in
the reserve is an artefact of the pole normalisation, not a real cost.

## Status

Closed.  Step 1 of the work order is complete: the global telescoping
identity holds with the endpoint table above, the moving endpoint is
convention-free because \(\omega_n(T_n)=0\), and \(\mathcal R_n\le Q_n\) is
proved to be *identical* to the direct certificate, hence to
\(C_n(T_n)\ge0\).

Step 2 is prepared: the reserve has the closed form (9), equivalently (11).
Its size, sign and threshold are established in
`103_02_EXACT_RESERVE_THEOREM.md`.
