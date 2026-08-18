# A1 binomial-barrier attempt: Abel aggregation and the pole--prime collision

## Result

This note tries to prove the first- or second-difference barriers isolated in
`103_52` by summing their binomial combination **before** passing to the Li
base point.  The result is an exact Abel-regularised correlation with one
Laguerre kernel:

\[
 \Delta^2P_n=-\lim_{\varepsilon\downarrow0}
 \int_0^\infty E(u)e^{-(1+\varepsilon)u}
 \bigl((1+\varepsilon)L_{n+1}^{(0)}(u)-\varepsilon L_n^{(0)}(u)\bigr)\,du,
 \qquad P_n=\lambda_n^{\rm prime}.
\tag{1}
\]

Consequently the convexity criterion \(\Delta^2D_n\ge0\) is exactly

\[
\boxed{\quad
\lim_{\varepsilon\downarrow0}
 \int_0^\infty E(u)e^{-(1+\varepsilon)u}
 \bigl((1+\varepsilon)L_{n+1}^{(0)}(u)-\varepsilon L_n^{(0)}(u)\bigr)\,du
 \ \le\ {1\over2}\sum_{\ell\ \rm odd}{(1-1/\ell)^n\over\ell^2}.
 \quad}
\tag{2}
\]

The integral at every \(\varepsilon>0\) is ordinary and absolutely
convergent.  Formula (2) is therefore a legitimate aggregated-kernel
barrier, rather than a formal use of the divergent prime expansion at
\(s=1\).

The criterion is in fact false for the actual zeta sequence: `103_55`
certifies \(\Delta^2D_{147}<0\).  The Abel calculation remains useful as a
no-go diagnosis.  The pole and prime sums which make up (1)
are each of order \(\varepsilon^{-n-2}\); the permitted Chebyshev bound
produces an absolute Abel load of exactly that divergent order.  Moreover,
this divergence sits on the **final sign-definite Laguerre ray**, past all
lobes.  Thus lobe pairing cannot remove it.  A proof would need a new,
quantitative pole--prime cancellation for the actual weights \(\Lambda(m)\),
which is again the missing RH-strength input.  No assertion of A1 or RH is
made.

## 1. A regulator which keeps the pole paired with the primes

For \(\varepsilon>0\), define, up to an irrelevant additive constant,

\[
 f_\varepsilon(t)=
 \log\bigl((t+\varepsilon)\zeta(1+\varepsilon+t)\bigr),
 \qquad
 F_\varepsilon(z)=f_\varepsilon\!\left({z\over1-z}\right),
\tag{3}
\]

and set

\[
 P_n(\varepsilon):=n[z^n]F_\varepsilon(z).
\tag{4}
\]

Subtracting \(f_\varepsilon(0)\) in (3), if desired, changes no
coefficient in (4).  On a fixed sufficiently small circle about \(t=0\),
\((t+\varepsilon)\zeta(1+\varepsilon+t)\) converges uniformly to
\(t\zeta(1+t)\).  Therefore ordinary local analyticity gives

\[
 \lim_{\varepsilon\downarrow0}P_n(\varepsilon)=P_n
 \quad\hbox{for every fixed }n.
\tag{5}
\]

This is a shifted Abel regulator in the natural \(t=s-1\) coordinate.  It
is preferable here to regulating a bare prime sum: its \(1/(t+\varepsilon)\)
term is retained from the outset.

For \(\Re t>0\), the Euler logarithmic derivative is absolutely
convergent and gives

\[
 f_\varepsilon'(t)
 ={1\over t+\varepsilon}
 -\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon+t}}.
\tag{6}
\]

Let \(E(u)=\psi(e^u)-e^u\).  Since \(E(0)=-1\), Stieltjes summation gives
the exact paired identity

\[
\begin{aligned}
 f_\varepsilon'(t)
 &=-\int_{[0,\infty)}e^{-(1+\varepsilon+t)u}\,dE(u)\\
 &=-1-(1+\varepsilon+t)
 \int_0^\infty E(u)e^{-(1+\varepsilon+t)u}\,du.
\end{aligned}
\tag{7}
\]

Here the boundary at infinity vanishes already from the elementary bound
\(|E(u)|\le e^u\), because \(\varepsilon+\Re t>0\).  Thus every operation
in (7) occurs in an absolutely convergent half-plane; no zero-location
statement has entered.

## 2. The aggregated first and second differences

For any analytic \(f\), if \(P_n=n[z^n]f(z/(1-z))\), then

\[
 \sum_{n\ge1}(P_{n+1}-P_n)z^n
 ={f'(z/(1-z))\over1-z}-f'(0).
\tag{8}
\]

The subtracted constant affects only the coefficient of \(z^0\).  Insert
(7), use the Laguerre generating function, and extract the coefficients of
\(z^n\), \(n\ge1\).  This yields the exact ordinary integrals

\[
 \boxed{\quad
 \Delta P_n(\varepsilon)
 =-1-\int_0^\infty E(u)e^{-(1+\varepsilon)u}
 \bigl((1+\varepsilon)L_n^{(1)}(u)
       -\varepsilon L_{n-1}^{(1)}(u)\bigr)\,du.
 \quad}
\tag{9}
\]

Indeed,

\[
 {(1+t)(1+\varepsilon+t)}e^{-tu}
 ={1+\varepsilon-\varepsilon z\over(1-z)^2}
 \exp\!\left(-{uz\over1-z}\right),
\tag{10}
\]

whose \(z^n\) coefficient is
\((1+\varepsilon)L_n^{(1)}-\varepsilon L_{n-1}^{(1)}\).

Taking one further forward difference and using
\(L_{j+1}^{(\alpha)}-L_j^{(\alpha)}=L_{j+1}^{(\alpha-1)}\) gives

\[
 \boxed{\quad
 \Delta^2P_n(\varepsilon)
 =-\int_0^\infty E(u)e^{-(1+\varepsilon)u}
 \bigl((1+\varepsilon)L_{n+1}^{(0)}(u)
       -\varepsilon L_n^{(0)}(u)\bigr)\,du.
 \quad}
\tag{11}
\]

All integrals in (9)--(11) are absolutely convergent: for fixed \(n\) the
Laguerre factor is a polynomial and
\(|E|e^{-(1+\varepsilon)u}\le e^{-\varepsilon u}\).  Now use (5) and
pass to the limit coefficientwise.  The terms carrying a factor
\(\varepsilon\) in (9) and (11) have no separately asserted limit; the
correct statement is the combined Abel limit.  It is

\[
 \Delta P_n=-1-\operatorname {Abel}\!\int_0^\infty
 E(u)e^{-u}L_n^{(1)}(u)\,du,
\tag{12}
\]

\[
\Delta^2P_n=-\operatorname {Abel}\!\int_0^\infty
 E(u)e^{-u}L_{n+1}^{(0)}(u)\,du,
\tag{13}
\]

where ``Abel'' in (13) means precisely the combined family
\((1+\varepsilon)L_{n+1}^{(0)}-\varepsilon L_n^{(0)}\) in (11), not the
naive damping of \(L_{n+1}^{(0)}\) alone.  It is not an unqualified
improper integral.  In particular, the \(\varepsilon L_n^{(0)}\) term must
not be discarded before the limit.

Combining (13) with the exact archimedean identity from `103_52`,

\[
 \Delta^2A_n=\sum_{\ell\ \rm odd}{(1-1/\ell)^n\over\ell^2},
\tag{14}
\]

gives (1)--(2).  The first-difference induction has the equally exact
Abel form obtained by combining (9) with

\[
 \Delta A_n=-{\gamma+\log(4\pi)\over2}
 +\sum_{\ell\ \rm odd}{1-(1-1/\ell)^n\over\ell}.
\tag{15}
\]

Thus the requested binomial combinations have genuinely been summed before
the singular limit is taken.

## 3. The same identity as a pole--prime block sum

Equation (6) also gives a useful exact diagnostic.  Direct coefficient
extraction, still for \(\varepsilon>0\), yields

\[
 \boxed{\quad
 \Delta^2P_n(\varepsilon)
 ={(-1)^{n+1}(1-\varepsilon)^n\over\varepsilon^{n+2}}
 +{1\over n+1}\sum_{m\ge2}{\Lambda(m)\log m\over m^{1+\varepsilon}}
 L_n^{(1)}(\log m).
 \quad}
\tag{16}
\]

For clarity, the first summand is the pole \(1/(t+\varepsilon)\), while
the second is the prime-power block.  Both are ordinary quantities for
\(\varepsilon>0\), and (16) equals (11) exactly.  In particular, it is
invalid to discard the first summand and then let \(\varepsilon\) tend to
zero.

Partitioning the prime sum in (16) at the successive zeros of
\(L_n^{(1)}\) is an exact lobe decomposition.  Every block has a fixed
sign from its Laguerre factor, but consecutive blocks alternate.  The
formula supplies no inequality comparing their actual prime-power masses.
It has, however, located the cancellation more sharply: the block sum must
cancel a pole of size \(\varepsilon^{-n-2}\), not merely compensate the
bounded archimedean moment in (14).

## 4. Quantified failure of absolute Abel and lobe estimates

The obstruction in the previous paragraph is not a loss caused by an
overly crude finite cutoff.  For a fixed nonnegative integer \(N\), the
leading coefficient of \(L_N^{(0)}\) and the substitution \(v=\varepsilon u\)
give the elementary asymptotic

\[
 \boxed{\quad
 \int_0^\infty e^{-\varepsilon u}|L_N^{(0)}(u)|\,du
 =\varepsilon^{-N-1}(1+O_N(\varepsilon))
 \qquad(\varepsilon\downarrow0).
 \quad}
\tag{17}
\]

For completeness, multiply the polynomial by \(\varepsilon^N\) after
the substitution.  It converges pointwise to \((-1)^Nv^N/N!\), and a
fixed polynomial majorant times \(e^{-v}\) proves dominated convergence.
The limiting integral is \(N!/N!=1\).

Apply the elementary Chebyshev estimate \(|E(u)|\le e^u\) to (11).  The
same scaling proof as (17), now for the polynomial
\((1+\varepsilon)L_{n+1}^{(0)}-\varepsilon L_n^{(0)}\), gives the
absolute Abel load

\[
 \int_0^\infty e^{-\varepsilon u}
 \left|(1+\varepsilon)L_{n+1}^{(0)}(u)-\varepsilon L_n^{(0)}(u)\right|du
 =\varepsilon^{-n-2}(1+O_n(\varepsilon)).
\tag{18}
\]

It bounds the integral in (11), and is exactly the scale of the pole in
(16).  In contrast, the entire
available archimedean budget in (2) is bounded above by

\[
 {1\over2}\sum_{\ell\ \rm odd}{1\over\ell^2}={\pi^2\over16}.
\tag{19}
\]

Hence an absolute estimate is not merely too large by a power of \(n\): it
does not survive the Abel limit at all.

There is also no rescue by pairing the finitely many oscillatory lobes.
Let \(x_{N}\) be the largest zero of \(L_N^{(0)}\).  On the final ray
\((x_N,\infty)\), the polynomial has the constant sign \((-1)^N\), and
the same proof as (17), with the lower limit replaced by \(x_N\), gives

\[
 \int_{x_N}^\infty e^{-\varepsilon u}|L_N^{(0)}(u)|\,du
 =\varepsilon^{-N-1}(1+O_N(\varepsilon)).
\tag{20}
\]

Thus the whole divergent Abel load is already on the sign-definite final
ray.  Adjacent-lobe transport can only rearrange the bounded oscillatory
interval before that ray; it cannot prove the pole--prime cancellation
needed in (16).  This is a quantified failure of the lobe ansatz, not a
claim that the actual weighted prime sum has the bad sign.

## 5. Eliminated convexity criterion and the surviving direction

The exact remaining theorem can now be stated without any hidden limit:

> **Eliminated Abel pole--prime criterion.**  For every \(n\ge1\), prove that the
> finite part on the right side of (16) obeys
> \[
> \lim_{\varepsilon\downarrow0}\left[
> {(-1)^{n+1}(1-\varepsilon)^n\over\varepsilon^{n+2}}
> +{1\over n+1}\sum_{m\ge2}{\Lambda(m)\log m\over m^{1+\varepsilon}}
> L_n^{(1)}(\log m)\right]
> \ge-{1\over2}\sum_{\ell\ \rm odd}{(1-1/\ell)^n\over\ell^2}.
> \]
> 
> This is equivalent to \(\Delta^2D_n\ge0\).

The inequality uses the actual values \(\Lambda(p^k)=\log p\) and is not
supplied by nonnegativity, support, a pointwise envelope for \(E\), or
Laguerre lobe geometry.  But it is no longer a target: the finite
counterexample in `103_55` falsifies it rigorously.

The natural remaining simple barrier is first-difference monotonicity,
which permits negative curvature.  From (9), put
\[
 \mathcal I_n^{(1)}:=\lim_{\varepsilon\downarrow0}
 \int_0^\infty E(u)e^{-(1+\varepsilon)u}
 \bigl((1+\varepsilon)L_n^{(1)}(u)-\varepsilon L_{n-1}^{(1)}(u)\bigr)du.
\]
Then exactly
\[
 \Delta D_n=\Delta A_n-2-2\mathcal I_n^{(1)},
 \qquad
 \Delta D_n\ge0\ \Longleftrightarrow\ 
 \mathcal I_n^{(1)}\le\tfrac12\Delta A_n-1.
\]
This is a possible RH-strength sufficient theorem, not an assertion made
here.  `103_55` checks that it survives the certified indices adjacent to
the failed convexity test; a cumulative-curvature budget is another
surviving formulation.

## Status

The attempted binomial route has produced a valid aggregated Abel kernel and
an exact pole--prime block identity.  Its convexity sign is now rigorously
eliminated, rather than merely unproved.  The only unconditional estimate
available from the elementary Chebyshev bound diverges at the same rate as
the pole, and the final sign-definite Laguerre ray prevents a lobe-pairing
repair.  A1 remains open.
