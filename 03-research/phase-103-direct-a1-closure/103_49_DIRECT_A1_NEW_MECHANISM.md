# Direct A1: divisor-theta square attempt and a regulated scalar flow

## Verdict

The exact strong-margin target is
\[
 D_n=2\lambda_n-\lambda_n^{\rm arch}\ge0.                       \tag{1}
\]
This note first records explicitly why an all-index proof is RH-strength.
It then tests the most direct new square mechanism: after combining the
two completed xi factors, \(\zeta(s)^2\) has positive divisor coefficients
and a positive theta-type Mellin density. The required polynomial
\(s(s-1)^2\), however, applies a differential operator whose one-term
kernel changes sign. Thus the proposed termwise divisor-theta square is
false.

The failure leaves an exact scalar alternative, rather than merely a
no-go: a regulator flow in \(a>1\). Its prime series is absolutely
convergent, it gives an exact recurrence in \(n\), and it yields a
one-sided integrated-flow sufficient condition for \(D_n>0\). The simple
monotone version of that condition is already falsified by certified low
coefficients, so any continuation must estimate the positive part of the
flow increments. No assertion of (1), A1, or RH is made.

## 1. Logical strength and circularity boundary

Let \(A_n=\lambda_n^{\rm arch}\). The archimedean positivity already
available in the phase gives \(A_n>0\) for \(n\ge8\). Therefore the
uniform strong margin (1) would imply
\[
 \lambda_n\ge {A_n\over2}>0\qquad(n\ge8).                       \tag{2}
\]
Together with the finite certificate for \(1\le n\le7\), this proves all
Li inequalities and hence RH. Independently, 103_24 shows that (1),
combined with A0, implies the compact A1 inequality. Conversely,
103_07 proves that uniform A1, modulo its finite range, is itself
equivalent to RH.

Thus a uniform proof of either A1 or (1) is not expected to follow from
formal positivity alone. This is a logical consequence of the already
proved implication chain, not an assumption about zero locations. In
particular, the arguments below do not use a zero product, RH, a
Herglotz representation, or any boundary assertion on a Carathéodory
symbol.

## 2. The exact divisor-theta square candidate

Put
\[
 X_{\rm arch}(s)=s\pi^{-s/2}\Gamma(s/2),\qquad
 Y(s)={\xi(s)^2\over X_{\rm arch}(s)}.                           \tag{3}
\]
The logarithmic coefficients of
\(Y((1-z)^{-1})/Y(1)\) are exactly \(D_n\). Direct cancellation in the
completed product gives, for \(s>1\),
\[
 \boxed{\quad
 Y(s)={1\over4}s(s-1)^2\pi^{-s/2}\Gamma(s/2)\zeta(s)^2.
 \quad}                                                         \tag{4}
\]
The square \(\zeta(s)^2=\sum_{m\ge1}d(m)m^{-s}\) has positive divisor
coefficients. Define
\[
 F(u)=\sum_{m\ge1}d(m)e^{-\pi m^2e^{2u}}.
                                                                    \tag{5}
\]
Tonelli's theorem and the change of variable \(t=e^{2u}\) give the
positive Mellin identity
\[
 \pi^{-s/2}\Gamma(s/2)\zeta(s)^2
 =2\int_{\mathbb R}e^{su}F(u)\,du\qquad(s>1).                   \tag{6}
\]
At first sight, (4)--(6) look like the desired positive square
decomposition.

To test it candidly, first truncate (5) at \(m\le M\). All boundary terms
then vanish when integrating by parts for \(s>1\). With \(A=-d/du\),
\[
 s(s-1)^2\int_{\mathbb R}e^{su}F_M(u)\,du
 =\int_{\mathbb R}e^{su}A(A-1)^2F_M(u)\,du.                     \tag{7}
\]
For a single summand \(q_x(u)=e^{-x}\), \(x=\pi m^2e^{2u}\), direct
differentiation yields
\[
 \boxed{\quad
 A(A-1)^2q_x
 =\bigl(8x^3-32x^2+18x\bigr)e^{-x}
 =2x(4x^2-16x+9)e^{-x}.
 \quad}                                                         \tag{8}
\]
The polynomial in (8) is negative at \(x=1\):
\[
 8-32+18=-6<0.                                                   \tag{9}
\]
It is also negative on the nonempty interval
\[
 2-{\sqrt7\over2}<x<2+{\sqrt7\over2}.                           \tag{10}
\]
The limit \(M\to\infty\) in (7) is justified for \(s>1\): after absolute
integration, each differentiated term is bounded by a constant depending
on \(s\) times \(d(m)m^{-s}\), whose sum converges.

Consequently, the positive divisor theta series does not remain positive
after the exact factors needed for \(Y\) are transferred to its density.
This is an exact counterexample to the *termwise* square ansatz. It does
not prove that the full summed kernel in (7) has a negative sign
everywhere, and makes no statement about \(D_n\); it proves only that a
proof assigning a nonnegative square to each divisor term cannot work.

## 3. Pivot: an exact absolutely convergent flow in \(a\)

For \(a>1\), define
\[
 \mathcal F(a,z)=
 \log {Y(a/(1-z))\over Y(a)}
 =\sum_{n\ge1}{D_n(a)\over n}z^n.                               \tag{11}
\]
This is analytic near \(z=0\), and
\[
 \lim_{a\downarrow1}D_n(a)=D_n                                \tag{12}
\]
for every fixed \(n\), because the completed function \(Y\) is analytic
and nonzero near \(s=1\).

Its real-axis logarithmic derivative is the paired Euler--Gamma quantity
\[
 L(s):={Y'(s)\over Y(s)}
 ={1\over s}+{2\over s-1}-{\log\pi\over2}
 +{1\over2}\psi(s/2)+2{\zeta'\over\zeta}(s).                    \tag{13}
\]
For \(s>1\), the last term is the absolutely convergent prime-power sum
\[
 2{\zeta'\over\zeta}(s)
 =-2\sum_{m\ge2}\Lambda(m)m^{-s}.                               \tag{14}
\]
Thus (11)--(14) give a genuinely completed, prime-accessible coordinate
without splitting the pole at \(a=1\).

Taylor expansion at \(a\), followed by
\([z^n](z/(1-z))^k={n-1\choose k-1}\), gives the exact scalar formula
\[
 \boxed{\quad
 D_n(a)=n\sum_{k=1}^n{a^k\over k!}{n-1\choose k-1}
 L^{(k-1)}(a).
 \quad}                                                         \tag{15}
\]
Differentiating (11) in the two variables gives the equivalent flow
identity
\[
 a\,\partial_a\mathcal F=(1-z)\partial_z\mathcal F-aL(a),
\]
and hence, for every \(n\ge1\),
\[
 \boxed{\qquad
 D_{n+1}(a)=D_n(a)+{a\over n}D_n'(a).
 \qquad}                                                        \tag{16}
\]
Equations (15)--(16) are exact identities, not asymptotic recurrences.

For each fixed \(n\), the flow has a positive high-\(a\) end. Indeed,
the elementary real-axis Gamma and Euler estimates in (13)--(14) give
\[
 L(a)={1\over2}\log{a\over2\pi}+O(a^{-1}),\qquad
 L^{(j)}(a)=O_j(a^{-j})\quad(j\ge1).                             \tag{17}
\]
Substitution in (15) yields
\[
 D_n(a)={n a\over2}\log{a\over2\pi}+O_n(a)>0
 \qquad(a\ \hbox{sufficiently large, with \(n\) fixed}).        \tag{18}
\]
No information about zeros is used in (17): the zeta term in (14) and all
its derivatives are exponentially small on the positive real axis.

## 4. The scalar integrated-flow criterion

Integrating (16) from \(1\) to \(A>1\) gives
\[
 D_n
 =D_n(A)-n\int_1^A{D_{n+1}(a)-D_n(a)\over a}\,da.                \tag{19}
\]
In particular, the following is a direct sufficient condition:
\[
 \boxed{\quad
 D_n(A)>
 n\int_1^A{(D_{n+1}(a)-D_n(a))_+\over a}\,da
 \quad\Longrightarrow\quad D_n>0.
 \quad}                                                         \tag{20}
\]
Unlike the false divisor-term square, (20) is a scalar inequality for the
paired completed object and needs no sign assignment to individual primes.
For \(a>1\), every quantity in it can be expressed by the absolutely
convergent formulae (13)--(15). A uniform proof of (20), with suitable
\(A=A_n\), would therefore be a legitimate direct route to the strong
margin without any assumed zero location.

There is a simple but false shortcut: if
\(D_{n+1}(a)\le D_n(a)\) held on \([1,A]\), then (18)--(19) would
immediately transport positivity backwards to \(a=1\). It already fails
at the base point. From the certified intervals recorded in 103_31,
\[
 b_1=D_1,\qquad b_2={D_2+D_1^2\over2},
\]
and therefore
\[
 D_2-D_1=2b_2-b_1^2-b_1
 >0.458919458323093272580725>0.                                \tag{21}
\]
By (16), \(D_1'(1)=D_2-D_1>0\). Thus no uniform backward-monotonicity
theorem can be inserted into (19).

The surviving mechanism is specifically the positive-part budget in (20):
it permits sign changes in the flow and asks only that their total upward
cost be dominated by the explicit high-\(a\) reserve. Establishing that
budget uniformly is still RH-strength by Section 1, but it is not ruled
out by the local Euler-factor, pointwise-symbol, Loewner, or
backward-monotonicity no-go results.

## Status and circularity audit

* The divisor-theta calculation (4)--(10) is carried out in \(s>1\) with
  finite truncations before the limiting interchange. Its failure is an
  exact sign computation, not a numerical diagnostic.
* The flow (11)--(20) uses only the completed real-axis function and the
  absolutely convergent Euler series for \(a>1\). It does not invoke RH or
  an assertion about nontrivial zeros.
* Proving (20) for every \(n\), then passing through (2), would prove RH.
  This is the required RH-strength input, not a hidden consequence of the
  identities.

The new live target is therefore an explicit, regulator-uniform bound on
the positive part of the scalar flow increment in (20). No such bound is
proved here.
