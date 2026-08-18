# Rigorous outer-tail lemma for the RH transport calculation

## Purpose

The numerical budgets in `103_03` and `103_04` stop near the soft edge
\(u=4N\), while their target integral ends at \(T_n\).  This note supplies
the missing *outer-tail* estimate.  It does not turn the measured interior
budgets into uniform theorems.

## Lemma

For \(\alpha>1\), \(N\ge0\), and \(a>0\),
\[
 \boxed{\quad
 \int_a^\infty e^{-u/2}\lvert L_N^{(\alpha)}(u)\rvert\,du
 \le
 \left(
 {\Gamma(N+\alpha+1)\over N!}\,{a^{1-\alpha}\over\alpha-1}
 \right)^{1/2}.
 \quad}
\tag{1}
\]

### Proof

Laguerre orthogonality gives
\[
 \int_0^\infty u^\alpha e^{-u}\bigl(L_N^{(\alpha)}(u)\bigr)^2\,du
 ={\Gamma(N+\alpha+1)\over N!}.
\tag{2}
\]
On \([a,\infty)\), apply Cauchy--Schwarz to
\[
 e^{-u/2}\lvert L_N^{(\alpha)}(u)\rvert
 =\bigl(u^{\alpha/2}e^{-u/2}\lvert L_N^{(\alpha)}(u)\rvert\bigr)
  u^{-\alpha/2}.
\]
The square of the first factor integrates to at most (2), and the square
of the second integrates to
\(\int_a^\infty u^{-\alpha}\,du=a^{1-\alpha}/(\alpha-1)\).
This proves (1). \(\square\)

## Consequences at the soft edge

Taking \(a=4N\) (for \(N\ge1\)) gives
\[
 \int_{4N}^\infty e^{-u/2}|L_N^{(2)}(u)|\,du
 \le \sqrt{\frac{(N+1)(N+2)}{4N}}=O(N^{1/2}),
\tag{3}
\]
and
\[
 \int_{4N}^\infty e^{-u/2}|L_N^{(3)}(u)|\,du
 \le {\sqrt{(N+1)(N+2)(N+3)}\over4\sqrt2\,N}=O(N^{1/2}).
\tag{4}
\]

Hence the portions of the low-zero and integrated high-zero estimates in
`103_04` over \([4N,T_n]\) are bounded by the corresponding expressions
with (3) and (4), independently of the size of \(T_n\).  For the
elementary term, use \(e^{-u}\le e^{-2N}e^{-u/2}\) on this interval, so
its outer tail is exponentially smaller than (3).

## Endpoint term in the integration by parts

The boundary term at \(T=T_n\) is also negligible under the stated cutoff
growth.  Indeed, the coefficient formula for Laguerre polynomials gives
\[
 |L_N^{(\alpha)}(T)|
 \le {T^N\over N!}\exp\!\left({N(N+\alpha)\over T}\right).
\tag{5}
\]
To see this, re-index the coefficient sum by \(j=N-k\), factor out
\(T^N/N!\), and use
\[
 {N!\over(N-j)!}{N+\alpha\choose j}
 \le {\bigl(N(N+\alpha)\bigr)^j\over j!}.
\]
If \(T_n\asymp N^{5/3}(\log N)^2\), Stirling's bound in (5) implies
\[
 e^{-T_n/2}|L_N^{(2)}(T_n)|=o(N^{-A})
 \qquad\text{for every fixed }A>0.
\tag{6}
\]
Thus the boundary term introduced by the high-zero integration by parts is
indeed negligible; the earlier monomial bound for \(L_N^{(2)}\) alone is
not a valid justification of that fact.

## Scope

This repairs only the mismatch between the integration range used in the
scripts and the range stated in the conditional argument.  The principal
unresolved analytic task remains a **uniform interior** estimate on
\([\log2,4N]\), replacing the empirical bounds (5b) and (5b') of
`103_03`.  Consequently this lemma does not establish the advertised
threshold \(n_1=150\), nor an unconditional A1 theorem.
