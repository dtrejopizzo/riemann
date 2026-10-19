# 104_73 — Bernstein representation of pressure and variable-width gate

**Result.** The pressure ratio of `104_72`, keeping the complete
prime–pole difference within a single variable,

\[
 \Phi_\tau(D)
 :=\log {1+e^D\over1+e^{D-\tau}},\qquad D=Q-C,
 \tag{1}
\]

admits an exact positive Bernstein–Gumbel representation. If
\(q=e^{-\tau}\), \(z=e^D\), then

\[
 \boxed{
 \Phi_\tau(D)
 =\int_0^\infty(1-e^{-tz})
 {e^{-t}-e^{-t/q}\over t}\,dt.}
 \tag{2}
\]

The measure of (2) is positive. However, this positivity does not yield
a bound on the functional from a linear average of \(D\): every global
affine majorant of \(\Phi_\tau\) is the trivial majorant \(\tau\), and
every positive linearization of (2) by powers returns to the
exponential partitions of `104_70`--`104_71`.

Allowing the width \(\tau=\tau_L\) to grow also does not break the
precision wall. Every subexponential width preserves the block
criterion. Setting
\(w(\tau)=\tau/\tanh(\tau/4)\), for an individual factor it replaces
the additive scale \(O(1)\) by \(O(w(\tau_L))\); transporting the sum
of \(L\) factors with a uniform error requires the scale
\(o(w(\tau_L)/L)\). Note that \(w(\tau)\to4\) as \(\tau\downarrow0\)
and \(w(\tau)\sim\tau\) as \(\tau\to\infty\). In both cases, on the
Euler diagonal of `104_72` the relative cost remains

\[
 \exp\{-X_L^2/100+o(X_L)\}.
 \tag{3}
\]

A width large enough to absorb the polar channel has scale
\(\exp(\Theta(X_L^2))\) and stops detecting **any** exterior mode of
scale \(R^{X_L}\). Three routes are thus ruled out quantitatively:

1. affine monotonicity in the complete difference;
2. Jensen/Bernstein followed by a positive moment;
3. widening the transition to dampen the pole.

This gate does not rule out a special signed inequality for the real
weights \(\Lambda(m)\) that directly estimates (1). It does not prove
\(G_L\to0\), A1, or RH.

---

## 1. Exact Bernstein representation

Define

\[
 f_q(z)=\log(1+z)-\log(1+qz),\qquad 0<q<1.
 \tag{4}
\]

Its derivative has the positive Laplace transform

\[
\begin{aligned}
 f_q'(z)
 &= {1\over1+z}-{q\over1+qz}\\
 &=\int_0^\infty e^{-zt}\{e^{-t}-e^{-t/q}\}\,dt.
\end{aligned}
\tag{5}
\]

Integrating from \(0\) to \(z\), Tonelli applies because the integrand
is nonnegative. Since \(f_q(0)=0\), (2) is obtained. In particular,
\(f_q\) is a Bernstein function and

\[
 (-1)^{k-1}f_q^{(k)}(z)
 =(k-1)!\left\{{1\over(1+z)^k}
 -{q^k\over(1+qz)^k}\right\}>0
 \quad(k\ge1).
 \tag{6}
\]

The representation can be read probabilistically: for each \(t\),
\(1-e^{-t e^D}\) is the probability that a Poisson of intensity
\(t e^D\) is nonzero. By Frullani's formula,

\[
 \int_0^\infty {e^{-t}-e^{-t/q}\over t}\,dt
 =\log(1/q)=\tau,
\]

so the measure of (2), divided by \(\tau\), is a probability. The
mixture is positive, but the
intensity still contains the complete activity \(e^{Q-C}\); it does
not separate \(Q\) and \(C\).

For \(0<\alpha\le1\), the inequality
\(1-e^{-u}\le u^\alpha\) and (2) give the Mellin majorant

\[
 \boxed{
 {1\over\tau}\Phi_\tau(D)
 \le {\Gamma(\alpha)(1-e^{-\alpha\tau})\over\tau}
 e^{\alpha D}.}
 \tag{7}
\]

Indeed,

\[
 \int_0^\infty t^{\alpha-1}
 (e^{-t}-e^{-t/q})\,dt
 =\Gamma(\alpha)(1-q^\alpha).
 \tag{8}
\]

Applied to \(D_n=-\lambda_n-\log(n+1)\), (7) becomes

\[
 G_L
 \le {\Gamma(\alpha)(1-e^{-\alpha\tau})\over\tau}
 \sum_{n\in I_L}{e^{-\alpha\lambda_n}\over(n+1)^\alpha}.
 \tag{9}
\]

For \(\alpha=1\), (9) is the activity bound of `104_72`, with the
improved constant \((1-e^{-\tau})/\tau\). For
\(\alpha=1/\tau\) and \(\tau\to\infty\), its prefactor tends to
\(1-e^{-1}\), while the right-hand side is exactly a partition of
temperature \(t=1/\tau\). So the positive linearization of the
pressure creates no new arithmetic quantity: it returns to the
variable-temperature gate of `104_70`.

---

## 2. No nontrivial affine majorant exists

Function (1) satisfies

\[
 \Phi_\tau(-\infty)=0,\qquad
 \Phi_\tau(+\infty)=\tau.
 \tag{10}
\]

**Lemma 2.1.** If \(aD+b\ge\Phi_\tau(D)\) for all
\(D\in\mathbb R\), then \(a=0\) and \(b\ge\tau\). If
\(aD+b\le\Phi_\tau(D)\) for all \(D\), then \(a=0\) and
\(b\le0\).

**Proof.** For a majorant, the limit \(D\to-\infty\)
excludes \(a>0\), while \(D\to+\infty\) excludes \(a<0\). So
\(a=0\), and (10) forces \(b\ge\tau\). The argument for a minorant is
identical. \(\square\)

The local curvature confirms there is also no global Jensen
orientation. With \(\sigma(u)=(1+e^{-u})^{-1}\),

\[
 \Phi_\tau''(D)=\sigma'(D)-\sigma'(D-\tau),
 \tag{11}
\]

which is positive for \(D<\tau/2\), zero at \(D=\tau/2\), and negative
for \(D>\tau/2\). So knowing
\(\sum_{n\in I_L}(Q_n-C_n)\), even exactly, does not give, via a global
affine majorant nor via a single Jensen orientation, the bound required
for the pressure ratio. The missing datum in those routes is the
distribution of the individual differences across the transition.

---

## 3. The criterion survives a variable width

Let

\[
 I_L=\{L^2,\ldots,L^2+L-1\},\qquad X_L=L^2+L-1,
 \tag{12}
\]

and take any sequence \(\tau_L>0\) such that

\[
 \boxed{\log(1+\tau_L)=o(L^2).}
 \tag{13}
\]

Define

\[
 G_L^{(\tau_L)}
 =\sum_{n\in I_L}{1\over\tau_L}
 \Phi_{\tau_L}(-\lambda_n-\log(n+1)).
 \tag{14}
\]

**Theorem 3.1.** Under (13),

\[
 \boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
 G_L^{(\tau_L)}\longrightarrow0.}
 \tag{15}
\]

More precisely, under RH one has \(G_L^{(\tau_L)}\le L^{-1}\),
while under non-RH there exist \(M<\infty\) and \(L_0\) such that

\[
 \liminf_{L\to\infty}{G_L^{(\tau_L)}\over L}\ge {1\over M}.
 \tag{16}
\]

**Proof.** Equation (7) with \(\alpha=1\) and
\((1-e^{-\tau})/\tau\le1\) gives

\[
 {1\over\tau_L}\Phi_{\tau_L}
 (-\lambda_n-\log(n+1))
 \le {e^{-\lambda_n}\over n+1}.
 \tag{17}
\]

Under RH, \(\lambda_n\ge0\); summing (17) over (12) gives
\(G_L^{(\tau_L)}\le L/(L^2+1)\le L^{-1}\).

If RH is false, `104_56` provides \(c>0\), \(R>1\), a
syndetic set \(S\), and a gap bound \(M\), such that
\(\lambda_n\le-cR^n\) on \(S\). Condition (13) implies
\(\tau_L=o(R^{L^2})\). Uniformly for \(n\in S\cap I_L\),

\[
 \lambda_n+\log(n+1)+\tau_L\longrightarrow-\infty.
 \tag{18}
\]

Representation

\[
 {1\over\tau}\Phi_\tau(-x)
 ={1\over\tau}\int_0^\tau {ds\over1+e^{x+s}}
 \tag{19}
\]

then shows that every site of \(S\cap I_L\) contributes \(1-o(1)\).
Every subinterval of \(M\) integers contains one of those sites; the
same count as in `104_72` proves (16). \(\square\)

So the width can grow polynomially, or even like
\(\exp(\sqrt{X_L})\), and in general in any subexponential way in the
degree. Relaxing the width does not lose the exterior falsifier.

---

## 4. Exact width–pole incompatibility

On the diagonal of `104_72`,

\[
 \varepsilon_L=e^{-X_L/100},\qquad
 |p_{X_L}(\varepsilon_L)-1|
 =\left({1-\varepsilon_L\over\varepsilon_L}\right)^{X_L},
 \tag{20}
\]

and hence

\[
 \log|p_{X_L}(\varepsilon_L)-1|
 ={X_L^2\over100}+o(1).
 \tag{21}
\]

The derivative of the normalized pressure with respect to \(D\)
satisfies

\[
 0< {d\over dD}\,{\Phi_\tau(D)\over\tau}
 \le {\tanh(\tau/4)\over\tau}< {1\over\tau}.
 \tag{22}
\]

Indeed,

\[
 \Phi_\tau'(D)=\sigma(D)-\sigma(D-\tau)
 ={\sinh(\tau/2)\over
   \cosh(D-\tau/2)+\cosh(\tau/2)},
\]

whose maximum is attained exactly at \(D=\tau/2\) and equals
\(\tanh(\tau/4)\).

Let \(D_{n,L}\) and \(\widetilde D_{n,L}\) be two families of
differences. From (22) follows the block transport bound

\[
 \left|\sum_{n\in I_L}{\Phi_{\tau_L}(D_{n,L})
                    -\Phi_{\tau_L}(\widetilde D_{n,L})\over\tau_L}\right|
 \le {\tanh(\tau_L/4)\over\tau_L}
      \sum_{n\in I_L}|D_{n,L}-\widetilde D_{n,L}|.
 \tag{22a}
\]

Define the effective width

\[
 w(\tau):={\tau\over\tanh(\tau/4)}.
 \tag{22b}
\]

So it suffices that the sum of errors be \(o(w(\tau_L))\); under a
uniform per-site bound this requires
\(\sup_{n\in I_L}|D_{n,L}-\widetilde D_{n,L}|
=o(w(\tau_L)/L)\). This scale is also the correct one for a uniform
guarantee based only on absolute errors: the derivative attains the
maximum of (22) at \(D=\tau/2\), and errors of the same sign at the
\(L\) sites saturate the bound to first order. Separating two channels
of size (21) with that uniform tolerance requires the relative-precision
scale

\[
 \boxed{
 {w(\tau_L)\over L|p_{X_L}(\varepsilon_L)-1|}
 =\exp\{-X_L^2/100+\log w(\tau_L)-\log L+o(1)\}.}
 \tag{23}
\]

For a width sequence fixed in advance to detect every possible
exterior radius \(R>1\), one needs

\[
 \tau_L=o(R^{X_L})\quad\hbox{for every }R>1,
 \tag{24}
\]

which is equivalent to \(\log(1+\tau_L)=o(X_L)\). Since
\(w(\tau)\to4\) at zero and \(w(\tau)\sim\tau\) at infinity, (24)
implies \(\log w(\tau_L)=o(X_L)\). Hence (23) is precisely

\[
 \exp\{-X_L^2/100+o(X_L)\}.                               \tag{25}
\]

Conversely, if the width made the logarithmic cost of (23) lose its
quadratic scale, in the precise sense that the logarithm of (23) were
\(-o(X_L^2)\), then (23) first gives
\(\log w(\tau_L)=X_L^2/100-o(X_L^2)\). In particular
\(w(\tau_L)\to\infty\), hence \(\tau_L\to\infty\),
\(w(\tau_L)\sim\tau_L\), and necessarily

\[
 \log\tau_L={X_L^2\over100}-o(X_L^2).
 \tag{26}
\]

But (26) implies \(R^{X_L}/\tau_L\to0\) for every \(R>1\). An exterior
excursion \(-cR^{X_L}\) then falls within the nearly linear region of
width \(\tau_L\) and its normalized contribution tends to zero. The
detector has been destroyed.

To resolve a single factor the two \(L\) factors in (22a) and (23) are
omitted; this only removes \(-\log L=o(X_L)\) and does not change
(25)--(26). This incompatibility is independent of how the two
channels are estimated separately: it only compares the maximum
tolerance compatible with the criterion and the exact polar size. It is
not a no-go for a direct estimate of the already-canceled difference
\(Q-C\).

---

## 5. Verdict

**Proved:** the positive representation (2), the Mellin majorant (7),
the affine classification of Lemma 2.1, the curvature change (11), the
variable-width criterion (15)--(16), and the quantitative
incompatibility (23)--(26).

**Ruled out:** obtaining \(G_L\to0\) exclusively via a global affine
majorant of the linear average of \(Q-C\), via a global Jensen
orientation on the positive representation, or by growing the width
until the regulated pole becomes numerically benign.

**Survives:** a signed arithmetic inequality that directly controls the
distribution of the complete differences
\(Q_{n,\varepsilon_L}-C_{n,\varepsilon_L}\) for the exact weights
\(\Lambda(m)\), without separating the channels or replacing the
pressure by an exponential moment.

**Not proved:** that direct control, \(G_L\to0\), A1, or RH.

---

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 bernstein_pressure_width_check.py
```

The checker numerically verifies (2), the signs of (6), the Mellin
bound, the curvature change, the criterion on the quadruple, and the
scales of (23)--(26). The asymptotic claims and the affine
classification are proved in the text.
