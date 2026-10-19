# 104_44 — Divisor–Markov transport and the Laguerre scale gate

**Status.** The exact identity

\[
 \Lambda*1=\log
\tag{1}
\]

does define a positive multiplicative transport that jointly preserves
every prime, all its powers, and the test's phase. If \(N\) is chosen with
weight \((\log N)N^{-s}\), the divisor \(D\mid N\) chosen with probability
\(\Lambda(D)/\log N\) has exactly the von Mangoldt law, and the quotient
\(N/D\) is independent with the zeta law. The Laguerre addition formula
then gives an exact convolution in the degree, with no triangle
inequality.

The transport, however, does not supply the missing proportional
coercivity:

1. its Markov contraction has exactly zero spectral gap, even on the
   zero-mean subspace;
2. inverting the exact degree convolution is precisely Möbius inversion,
   already audited in `104_12`;
3. the continuous pole–Gamma analogue contracts degree \(r\) by
   \(1/\sqrt{r+1}\), but only in the scaled basis
   \(L_r((s-1)x)\); expressing the unscaled A1 kernel in that basis has
   absolute load \((2/(s-1)-1)^r\), which for \(s-1=1/n\) is
   \(\exp((1+o(1))n\log n)\).

Hence the following argument is ruled out as an autonomous mechanism:
"use (1), conditional-expectation contraction, and Laguerre addition to
obtain a proportional bound." A special estimate on the **fixed, unscaled
vector**, with no positive inversion and no separation of degrees, would
still be new mathematics; the transport does not refute it, but neither
does it supply it. Neither \(B_n\le(1501/2002)A_n\), A1, nor RH is
proved.

## 1. Non-duplication audit

`103_70` applies Vaughan/Heath–Brown and proves that the factorization
variables enter the phase only through the sum of their logarithms. It
also records Laguerre addition, but does not interpret it as a
probability disintegration.

`104_12` uses the dual identity \(\Lambda=\mu*\log\), obtains the signed
convolution in the degree, and rules out a positive adjoint for Möbius.
`104_13` proves that Selberg–Riccati loses the pole–prime collision if
estimated piecewise. `104_35` and `104_38` keep the prime–pole channel
and show that the canonical Selberg square either cancels exactly or
leaves a negative diagonal.

What is new here is narrower:

* the canonical Markov disintegration associated with \(\Lambda*1=\log\);
* its exact continuous analogue as a uniform partition of a Gamma(2);
* the proof of zero gap via atoms at real primes;
* the exact quantification of the cost of switching from the natural
  scale \((s-1)x\) to the Laguerre scale of A1.

Vaughan is not reopened, Möbius positivity is not postulated, and no
Selberg square is used.

## 2. Exact multiplicative disintegration

Fix \(s>1\) and write

\[
 Z_s=\zeta(s),\qquad
 \mathcal L_s=-{\zeta'(s)\over\zeta(s)}
             =\sum_{d\ge2}{\Lambda(d)\over d^s}.
\tag{2}
\]

Define two probabilities

\[
 \nu_s(d)={\Lambda(d)d^{-s}\over\mathcal L_s},\qquad
 \eta_s(k)={k^{-s}\over Z_s}.
\tag{3}
\]

Let \(D\sim\nu_s\), \(K\sim\eta_s\) be independent and \(N=DK\).

**Theorem 2.1 (divisor–Markov transport).** The law of \(N\) is

\[
 \boxed{
 \Pi_s(N)={ (\log N)N^{-s}\over-\zeta'(s)}}
 \qquad(N\ge2),
\tag{4}
\]

and its inverse disintegration is

\[
 \boxed{
 \mathbb P_s(D=d\mid N)
 ={\Lambda(d)\over\log N}\,\mathbf1_{d\mid N}.}
\tag{5}
\]

**Proof.** For each \(N\ge2\), (1) gives

\[
\begin{aligned}
 \mathbb P(DK=N)
 &=\sum_{d\mid N}{\Lambda(d)d^{-s}\over\mathcal L_s}
                  {(N/d)^{-s}\over Z_s}\\
 &={N^{-s}\over\mathcal L_sZ_s}\sum_{d\mid N}\Lambda(d)
 ={(\log N)N^{-s}\over-\zeta'(s)}.
\end{aligned}
\]

Dividing the joint mass by (4) proves (5). \(\square\)

The divisor operator and its multiplicative adjoint are

\[
 (\mathsf T_sf)(N)
 ={1\over\log N}\sum_{d\mid N}\Lambda(d)f(d),
\tag{6}
\]

\[
 (\mathsf P_sF)(d)
 ={1\over Z_s}\sum_{k\ge1}{F(dk)\over k^s}.
\tag{7}
\]

By construction,

\[
 \langle \mathsf T_sf,F\rangle_{L^2(\Pi_s)}
 =\langle f,\mathsf P_sF\rangle_{L^2(\nu_s)},
 \qquad \mathsf T_s1=\mathsf P_s1=1,
\tag{8}
\]

and Jensen's inequality gives

\[
 \boxed{
 \|\mathsf T_sf\|_{L^2(\Pi_s)}
 \le\|f\|_{L^2(\nu_s)}.}
\tag{9}
\]

This is a genuine contraction using the complete canonical weights; the
decisive question is whether it contains a strict gap.

## 3. The Markov gap is exactly zero

Let \(p\) be prime and

\[
 e_p(d)=\mathbf1_{d=p},\qquad
 q_p=\nu_s(p)={ (\log p)p^{-s}\over\mathcal L_s}.
\tag{10}
\]

From (6),

\[
 (\mathsf T_se_p)(N)
 ={\log p\over\log N}\mathbf1_{p\mid N}.
\tag{11}
\]

A direct sum using (4) gives

\[
 {\|\mathsf T_se_p\|_{L^2(\Pi_s)}^2
  \over\|e_p\|_{L^2(\nu_s)}^2}
 =R_p(s):={1\over Z_s}\sum_{k\ge1}{k^{-s}\log p
                              \over\log p+\log k}.
\tag{12}
\]

Each summand of (12) lies between zero and \(k^{-s}/Z_s\), and for fixed
\(k\) its logarithmic factor tends to one as \(p\to\infty\). By dominated
convergence,

\[
 \boxed{\lim_{p\to\infty}R_p(s)=1.}
\tag{13}
\]

This also holds after removing constants. Indeed, for

\[
 f_p=e_p-q_p
\]

one has \(\langle f_p,1\rangle_{\nu_s}=0\) and

\[
 {\|\mathsf T_sf_p\|_2^2\over\|f_p\|_2^2}
 ={R_p(s)-q_p\over1-q_p}\longrightarrow1,
\tag{14}
\]

because \(q_p\to0\). Together with (9), this proves

\[
 \boxed{
 \|\mathsf T_s\|_{L^2_0(\nu_s)\to L^2_0(\Pi_s)}=1.}
\tag{15}
\]

Hence there is no \(\delta_s>0\) such that

\[
 \|\mathsf T_sf\|_2^2
 \le(1-\delta_s)\|f\|_2^2
 \qquad(f\perp1).
\tag{16}
\]

The witness uses real primes and the exact weight \(\log p\); it is not a
perturbation of the arithmetic measure. The geometric reason is that the
conditional row of a prime parent is deterministic.

Equation (15) rules out a gap in the **operator coordinate**. It does not
rule out that some special sequence of vectors has a ratio less than one;
such a claim would have to be proved directly for that sequence.

## 4. Laguerre addition with no triangles

For \(j\ge0\), set

\[
 p_j(s)=\sum_{d\ge2}{\Lambda(d)\over d^s}L_j(\log d),
 \qquad
 z_j(s)=\sum_{k\ge1}{1\over k^s}L_j(\log k),
\tag{17}
\]

and

\[
 b_N(s)=\sum_{m\ge2}{\log m\over m^s}
                         L_N^{(1)}(\log m).
\tag{18}
\]

All the series converge absolutely. The formula

\[
 L_N^{(1)}(x+y)=\sum_{j=0}^NL_j(x)L_{N-j}(y)
\tag{19}
\]

and the joint law of Section 2 give, with no moduli,

\[
 \boxed{b_N(s)=\sum_{j=0}^Np_j(s)z_{N-j}(s).}
\tag{20}
\]

With \(t=z/(1-z)\), (20) is equivalent to

\[
 { -\zeta'(s+t)\over(1-z)^2}
 =\left\{{\mathcal L(s+t)\over1-z}\right\}
  \left\{{\zeta(s+t)\over1-z}\right\}.
\tag{21}
\]

This is exactly \(-\zeta'=\mathcal L\zeta\). Solving for the von Mangoldt
moments in (20) requires dividing by the second brace of (21), that is,
introducing \(1/\zeta\). Coefficient by coefficient this is the Möbius
inversion of `104_12`, not a positive Markov inverse. Keeping (20)
complete preserves every sign, but then a bound for its factor
\(p_j\) remains exactly the new sought input.

## 5. Continuous analogue: where coercivity does appear

Let \(\varepsilon=s-1>0\). The analogue of the pole takes independent
\(X,Y\) with exponential law

\[
 \varepsilon e^{-\varepsilon x}\,dx,
\]

and sets \(U=X+Y\). Then \(U\) has density

\[
 \varepsilon^2u e^{-\varepsilon u}\,du,
\tag{22}
\]

and \(X\mid U=u\) is uniform on \([0,u]\). Hence

\[
 (\mathsf C_\varepsilon f)(u)={1\over u}\int_0^u f(x)\,dx
\tag{23}
\]

is the exact analogue of (6).

For the scaled degree

\[
 f_r(x)=L_r(\varepsilon x),
\]

the Laguerre integral identity gives

\[
 \boxed{
 (\mathsf C_\varepsilon f_r)(u)
 ={1\over r+1}L_r^{(1)}(\varepsilon u).}
\tag{24}
\]

Laguerre orthogonality implies

\[
 \|f_r\|_{L^2(\mathrm{Exp}(\varepsilon))}^2=1,
 \qquad
 \|\mathsf C_\varepsilon f_r\|_{L^2(\Gamma(2,\varepsilon))}^2
 ={1\over r+1}.
\tag{25}
\]

So the continuum has exactly the per-degree coercivity one would want to
transport. The problem is that A1 does not use \(L_r(\varepsilon x)\), but
the unscaled degree \(L_r(x)\). The associated test satisfies
\(L_{n-1}^{(1)}=\sum_{r=0}^{n-1}L_r\); hence the scale problem is already
present in each ordinary component. It is not claimed that those
components could be estimated separately: doing so would be precisely
losing their relative cancellation.

### 5.1 Joint signed form with the pole

The discrete and continuous transports can be combined before
estimating. For \(n\ge1\), define the same complete channel of `104_41`,
now with \(s=1+\varepsilon\):

\[
\begin{aligned}
 \mathcal B_{n,s}:={}&s\sum_{m\ge2}{\Lambda(m)\over m^s}
       L_{n-1}^{(1)}(s\log m)\\
 &-s\int_1^\infty y^{-s}L_{n-1}^{(1)}(s\log y)\,dy .
\end{aligned}
\tag{25a}
\]

Setting \(f_{n,s}(x)=L_{n-1}^{(1)}(sx)\), the two disintegrations give the
exact identity

\[
 \boxed{
 \mathcal B_{n,s}
 =s\left\{
  \mathcal L_s\,\mathbb E_{\Pi_s}[\mathsf T_sf_{n,s}]
  -{1\over\varepsilon}
       \mathbb E_{\Gamma(2,\varepsilon)}
                    [\mathsf C_\varepsilon f_{n,s}]
 \right\}.}
\tag{25b}
\]

Indeed, the conditional expectations of (25b) recover, respectively,
\(\mathbb E_{\nu_s}f_{n,s}\) and
\(\mathbb E_{\mathrm{Exp}(\varepsilon)}f_{n,s}\); the second integral of
(25a), after \(y=e^x\), is
\(\varepsilon^{-1}\mathbb E_{\mathrm{Exp}(\varepsilon)}f_{n,s}\).
By `104_41`,

\[
 \lim_{s\downarrow1}\mathcal B_{n,s}=B_n=A_n-\lambda_n.
\tag{25c}
\]

Equations (25a)–(25c) keep, in a single difference, the primes, prime
powers, pole, and phase. They do not license estimating the two
expectations separately: both have divergent terms as
\(\varepsilon\downarrow0\), and finiteness lies in their signed collision.
Contraction (9) acts within the first probability and (25) within the
second; neither compares their means with the required sign.

## 6. The change of scale costs \(\exp(n\log n)\)

The exact dilation formula is

\[
 \boxed{
 L_r(\beta x)=\sum_{j=0}^r{r\choose j}
       \beta^j(1-\beta)^{r-j}L_j(x).}
\tag{26}
\]

Taking \(x=\varepsilon u\) and \(\beta=1/\varepsilon\), one obtains

\[
 L_r(u)=\sum_{j=0}^r{r\choose j}
 \varepsilon^{-j}(1-\varepsilon^{-1})^{r-j}
 L_j(\varepsilon u).
\tag{27}
\]

For \(0<\varepsilon<1\), the absolute load of (27) is exactly

\[
 \boxed{
 \sum_{j=0}^r{r\choose j}\varepsilon^{-j}
       |1-\varepsilon^{-1}|^{r-j}
 =\left({2\over\varepsilon}-1\right)^r.}
\tag{28}
\]

At the natural diagonal choice \(\varepsilon=1/n\), \(r=n-1\),

\[
 (2n-1)^{n-1}=\exp\{(1+o(1))n\log n\}.
\tag{29}
\]

Applying (25) degree by degree and summing magnitudes loses exactly, by
(29), the scale A1 needs to cancel. If magnitudes are not taken, the
alternating coefficients of (27) must be kept whole; recombining them
returns to \(L_r(u)\) and no inequality has been obtained. This is the
Markov version of the collision stop-gate of `104_13`.

## 7. Off-line falsifier and logical scope

The off-line quartet does not by itself satisfy (1) with the canonical
arithmetic weights; hence a future inequality that genuinely uses
disintegration (5) need not transfer to the quartet. But the only
automatic inequalities obtained here are (9) and Jensen, and (15) proves
they have no margin even before reaching the spectral level. They
"prove" no bound for the quartet nor for the real arithmetic.

If an attempt is made to carry the contraction from \(s>1\) to the
boundary via a continuation that forgets (5), the off-line residues of
`104_41` reappear exactly; there the quartet is the binding falsifier.
Hence this transport does not evade the residue gate.

## 8. Decision

```text
proved unconditionally:
  exact multiplicative disintegration (4)--(5);
  adjunction and Markov contraction (8)--(9);
  zero spectral gap, even on the zero mean, (12)--(15);
  exact Laguerre convolution with no triangles (20);
  continuous Gamma analogue and contraction 1/sqrt(r+1) (24)--(25);
  exact cost (2/epsilon-1)^r of switching to the A1 scale (28).

ruled out:
  a uniform operator gap for the divisor transport;
  positive inversion of the degree convolution;
  transferring Gamma coercivity degree by degree via triangles;
  using the transport as an autonomous closure of the proportional bound.

remains open:
  a specific one-sided estimate for the unscaled Laguerre vector,
  keeping the alternating sum (27), the Gamma block, and the boundary
  terms fully intact;
  B_n <= (1501/2002) A_n, A1, and RH.
```

`tools/divisor_markov_laguerre_check.py` checks with `Fraction` the
divisor identity, the addition formula, the continuous operator (24), and
the dilation (26)–(28). It uses neither zeros of zeta nor floating point.
</content>
