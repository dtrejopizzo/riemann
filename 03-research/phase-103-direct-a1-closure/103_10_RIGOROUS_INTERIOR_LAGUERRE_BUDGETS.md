# Rigorous interior Laguerre budgets

> **Effectivity update.**  The argument below proves the exponents from a
> published uniform estimate but does not expose its hidden constant.
> `103_22`, equations (22) and (31), now gives an independent elementary
> proof with explicit numerical constants for \(N\ge149\).  Those constants
> are intentionally enormous and do not certify the former threshold 150.

## Statement

Put \(a=\log2\), \(N\ge1\), and
\[
 I_\alpha(a;N)=\int_a^{4N}e^{-u/2}\lvert L_N^{(\alpha)}(u)\rvert\,du.
\]
Then there are constants \(C_2,C_3>0\), independent of \(N\), such that
\[
 \boxed{I_2(\log2;N)\le C_2N^{3/4},\qquad
        I_3(\log2;N)\le C_3N^{5/4}.}
\tag{1}
\]

Thus the budgets required in `103_04` are theorems, not numerical fits. No
explicit numerical values for \(C_2,C_3\) are claimed here; consequently
this result establishes an eventual conditional threshold, not the prior
numerical value \(150\).

## Uniform pointwise input

We use the following standard uniform Laguerre estimate. For every fixed
\(\alpha>-1\), there is \(A_\alpha>0\) such that, for \(N\ge1\) and
\(u>0\),
\[
 e^{-u/2}\lvert L_N^{(\alpha)}(u)\rvert
 \le A_\alpha N^{\alpha/2}
 (N^{-1}+u)^{-\alpha/2-1/4}
 \bigl(N^{1/3}+\lvert u-4N\rvert\bigr)^{-1/4}\Phi_N(u),
\tag{2}
\]
where \(0<\Phi_N(u)\le1\). On \(0<u\le4N\), \(\Phi_N(u)=1\).

This is the simplified uniform estimate stated as Lemma 2.2 in Y. Shi and
Z. Li, *Multipliers of \(H^1\) into \(\ell^q\)*, J. Math. Soc. Japan 68
(2016), 797--805, which in turn cites the Laguerre asymptotics of
Muckenhoupt and the uniform forms of Li--Shi. It is precisely the
hard-edge/bulk/Airy estimate: the term \(N^{1/3}+|u-4N|\) regularizes the
soft edge, so no false global Plancherel--Rotach supremum is used.

## Proof of (1)

Write
\[
 p_\alpha={\alpha\over2}+{1\over4}.
\]
Since \(a\le u\le4N\), (2) becomes
\[
 e^{-u/2}|L_N^{(\alpha)}(u)|
 \le A_\alpha N^{\alpha/2}
 (N^{-1}+u)^{-p_\alpha}
 (N^{1/3}+4N-u)^{-1/4}.
\tag{3}
\]

Split the integral at \(2N\).

On \([a,2N]\),
\[
 (N^{1/3}+4N-u)^{-1/4}\le(2N)^{-1/4},
 \qquad (N^{-1}+u)^{-p_\alpha}\le u^{-p_\alpha}.
\]
As \(p_\alpha>1\) for \(\alpha=2,3\),
\[
 \begin{aligned}
 \int_a^{2N}e^{-u/2}|L_N^{(\alpha)}(u)|\,du
 &\le {A_\alpha\over2^{1/4}}
       N^{\alpha/2-1/4}\int_a^\infty u^{-p_\alpha}\,du\\
 &= {A_\alpha\over2^{1/4}(p_\alpha-1)}
    a^{1-p_\alpha}N^{\alpha/2-1/4}.
 \end{aligned}
\tag{4}
\]

On \([2N,4N]\),
\[
 (N^{-1}+u)^{-p_\alpha}\le(2N)^{-p_\alpha},
\]
and, with \(v=4N-u\),
\[
 \int_{2N}^{4N}(N^{1/3}+4N-u)^{-1/4}\,du
 =\int_0^{2N}(N^{1/3}+v)^{-1/4}\,dv
 \le {4\over3}(N^{1/3}+2N)^{3/4}
 \le B N^{3/4},
\tag{5}
\]
where \(B=\frac43\,3^{3/4}\) works for \(N\ge1\). Hence
\[
 \int_{2N}^{4N}e^{-u/2}|L_N^{(\alpha)}(u)|\,du
 \le A_\alpha B2^{-p_\alpha}N^{1/2}.
\tag{6}
\]

Combining (4) and (6), and using \(N^{1/2}\le N^{\alpha/2-1/4}\) for
\(\alpha=2,3\), gives
\[
 I_\alpha(a;N)\le
 \left(
 {A_\alpha a^{1-p_\alpha}\over2^{1/4}(p_\alpha-1)}
 +A_\alpha B2^{-p_\alpha}
 \right)N^{\alpha/2-1/4}.
\tag{7}
\]
For \(\alpha=2\) and \(3\), this is exactly (1). \(\square\)

## Consequence for the transport calculation

Together with `103_09`, (1) controls the entire interval
\([\log2,T_n]\). Under RH, the low-zero contribution is
\(O(N^{3/4}\log^2N)\), the once-integrated high-zero contribution is
\(O(N^{3/4}\log N)\), and the elementary contribution is
\(O(N^{3/4})\). Therefore the conditional comparison with
\(q(n)\sim\frac38n\log n\) holds for all sufficiently large \(n\).

Making this an explicit numerical threshold still requires explicit
numerical versions of \(A_2,A_3\), an explicit lower bound for \(q(n)\),
and an interval certificate for the remaining finite range.
