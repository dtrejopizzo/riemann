# Independent audit of the ODE effectivity argument

> **Post-audit repair.**  `103_22` now uses \(10^{13}\) in (15) and every
> dependent definition, and it spells out the finite Bessel sum, derivative,
> and energy estimates with the enlarged common bound \(B=10^{12}\).
> Accordingly, the correction required by this audit has been applied.

Audited document: `103_22_ODE_EFFECTIVITY_LOSS_AUDIT.md`, especially
Sections 5.1--5.4.  This audit recomputes the transformations and checks
whether every displayed numerical constant follows from the preceding
inequalities.  It does not treat a numerical experiment as a proof.

## Verdict

The ODE strategy is mathematically viable.  The change of variables, Bessel
normalisation, Volterra kernel, energy transport, and the powers in the two
integral budgets are correct.  There is, however, one definite numerical
gap: the coefficient bound (15) does **not** follow from (13)--(14) with its
stated constant `2·10^12`.  Replacing that number by `10^13` repairs the
argument, with the same exponents and all later conclusions after the
corresponding change in the definitions of `K`, `H`, `H_2`, and `G`.

Thus `103_22` proves effective uniform bounds only after that correction and
after its elementary series assertions in 5.1 are written out as lemmas (the
estimates themselves have sufficient slack).  It does not support the
separate finite threshold 150.

## 1. Exact transformations and normalisation

With

\[
v=x^{\alpha/2+1/2}e^{-x/2}L_N^{(\alpha)}(x),\qquad
\nu=N+(\alpha+1)/2,
\]

direct substitution in the Laguerre equation gives

\[
v''+\left(\frac\nu x-\frac14+\frac{1-\alpha^2}{4x^2}\right)v=0.
\]

Put \(t=2\sqrt{\nu x}\) and \(v=\sqrt t\,w\).  Since
\(d/dx=(2\nu/t)d/dt\), cancellation of the first derivative gives

\[
w''+\left(1+\frac{1-4\alpha^2}{4t^2}\right)w
=\frac{t^2}{16\nu^2}w.
\]

Hence (9) is correct.  The regular solution of the homogeneous equation is
\(\phi_\alpha=\sqrt tJ_\alpha(t)\).  Comparing the leading terms at zero,
using \(L_N^{(\alpha)}(0)=\Gamma(N+\alpha+1)/(\Gamma(\alpha+1)\Gamma(N+1))\),
gives exactly

\[
A_{N,\alpha}=\frac{\Gamma(N+\alpha+1)}
 {2\Gamma(N+1)\nu^{(\alpha+1)/2}}.
\]

So (10), including its factor 2, is correct.  Also
\(W(\sqrt tJ_m,\sqrt tY_m)=2/\pi\), with the convention
\(W(f,g)=fg'-f'g\).

## 2. Bessel and Volterra stage

For \(1\le t\le8\), absolute values in the series for \(J_m\) yield
\(4^m e^{16}/m!<3\cdot10^9\) for \(1\le m\le4\).  The displayed coarse
majorisation of the logarithmic series for \(Y_m\) has enough slack to give
the claimed \(5\cdot10^{10}\) bound; the finite negative-power sum is
bounded on \([1,8]\) and is negligible beside that number.  The recurrence
uses only orders 1 through 4 for derivatives of orders 2 and 3.  For
\(t\ge8\),

\[
q_m(t)=1-\frac{4m^2-1}{4t^2}\ge4/5,\qquad q_m'(t)>0
\]

for \(m=2,3\), and

\[
\left(\frac{W'^2+q_mW^2}{q_m}\right)'
=-\frac{q_m'}{q_m^2}W'^2\le0.
\]

This validates the energy propagation used to obtain (13) and (13a), albeit
the text should display the elementary estimates for the finite sum and the
derivatives rather than merely call them “the same”.

The Green kernel is

\[
G(t,r)=\frac\pi2\,[\phi(r)\chi(t)-\chi(r)\phi(t)],
\]

so (13) gives \(|G|\le\pi B^2\).  With \(T=2\nu^{2/3}\),

\[
\int_1^T\frac{r^2}{16\nu^2}\,dr
\le\frac{T^3}{48\nu^2}=\frac16.
\]

Thus the exponent \(P=\pi B^2/6\) in the Gronwall estimate is correct.
The derivative formula has no upper-limit term because \(G(t,t)=0\), and
gives the factor \(1+P\) in (16a).

### Definite correction to (15)

From (14), \(|w(1)|+|w'(1)|\le2A\), and from (13), each of
\(|\phi(1)|,|\chi(1)|,|\phi'(1)|,|\chi'(1)|\) is at most \(B\).  Cramer's
rule and the Wronskian give

\[
\begin{aligned}
|c_\phi|+|c_\chi|
&\le \pi B\bigl(|w(1)|+|w'(1)|\bigr)\\
&\le2\pi BA<10^{13}A.
\end{aligned}
\]

Consequently the asserted `2·10^12 A` is not derivable: it is smaller than
the valid consequence of the stated input by a factor greater than \(\pi\).
Use instead

\[
 |c_\phi|+|c_\chi|\le10^{13}A.
\]

Then (16) remains valid after replacing its leading `2·10^12` by `10^13`.
No power of \(N\), no integration range, and no later logical step changes.

## 3. Conversion back to \(x\) and the \(\alpha=3\) budget

The exact identities

\[
\sqrt t=\sqrt2\,\nu^{1/4}x^{1/4},\qquad
\frac{dt}{dx}=\frac{2\nu}{t}
\]

validate (18).  In particular the bounds \(A_{N,2}\ll N^{1/2}\) and
\(A_{N,3}\ll N\) yield respectively \(N^{3/4}x^{1/4}\) and
\(N^{5/4}x^{1/4}\); no quarter-power is lost here.

For \(\alpha=3\), the integrand is \(x^{-2}|v(x)|\).  Integrating
\(x^{-7/4}\) from \(a\) to \(M=\nu^{1/3}\) yields
\((4/3)a^{-3/4}\), proving (20).  Cauchy--Schwarz and orthogonality give

\[
\int_M^\infty e^{-x/2}|L_N^{(3)}(x)|dx
\le\left(\frac{(N+1)(N+2)(N+3)}{2M^2}\right)^{1/2}=O(N^{7/6}),
\]

which is indeed at most \(2N^{5/4}\) for \(N\ge149\).  Equations
(20)--(22) have the correct powers.

## 4. The \(\alpha=2\) transport

At \(x_0=\nu^{1/3}\), \(t_0=2\nu^{2/3}\).  Differentiating
\(v=\sqrt t w\) shows that (23) is a safe upper bound (the \(w'\) term is
of order \(A\nu^{2/3}\), while the remaining term is smaller).

For \(Q=Q_{2,N}\), direct differentiation gives

\[
\left(v^2+\frac{v'^2}{Q}\right)'=-\frac{Q'v'^2}{Q^2}.
\]

On the stated interval \(Q>0\), \(Q'<0\); hence the inequality in (24)
has the correct sign.  The two lower bounds in (25) are valid with ample
slack for \(N\ge149\).  Integrating gives

\[
S(x)\le S(x_0)\frac{Q(x_0)}{Q(x)}
\le2S(x_0)\frac{x}{x_0},
\]

and the constants in (26)--(27) are conservative.  The three integrations
in (28)--(30) use respectively \(x^{-5/4}\), \(x^{-1}\), and the exact
orthogonality tail; their exponents and the use of
\(\log(M/x_0)=\frac16\log\nu\) are correct.  The finite-\(N\) conversion
in (32) is also correct.

## Final status

After replacing `2·10^12` in (15) and all dependent definitions by a valid
constant such as `10^13`, the document supplies explicit uniform Laguerre
budgets \(I_2\ll N^{3/4}\), \(I_3\ll N^{5/4}\).  These are enough for the
*eventual conditional* implication \(RH\Rightarrow A1\), once combined
with the already audited tail and a rigorous asymptotic lower bound for the
reserve.  The constants are astronomically large, so this cannot establish
the numerical threshold 150 and it provides no unconditional proof of RH.
