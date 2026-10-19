# 104_81 — On/off-line controls of the deep observable

**Result.** The deep observable of 104_75 does not vanish by a
normalization tautology. Two pairs of exact controls separate it:

\[
\begin{array}{c|c|c}
\text{control}&\text{zero location}&
\text{deep logarithmic density}\\ \hline
\text{critical quartet}&|w|=1&0\\
\text{outer quartet}&|w|\ne1&1/8\\
\text{lattice Euler }Z_+&\Re\rho=1/2&0\\
\text{lattice Euler }Z_-&\Re\rho\ne1/2&1/4.
\end{array}
\]

The second pair keeps non-negative Mangoldt weights, unitary prime
towers, an Euler product and a functional equation. Hence the detector
correctly tells apart an on-line model from an off-line one even after
incorporating formal arithmetic.

This **does not prove** that the observable is zero for the ordinary
weights \(\Lambda(m)\). The Euler models are lattice models and do not
satisfy the continuous PNT or Riemann zeta's Gamma factor. The result is
an adversarial control of the gate, not a proof of A1 or RH.

---

## 1. The abstract observable

For a real sequence \(\ell=(\ell_n)\), set

\[
 {\cal D}_X(\ell):={1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\ell_n+\log(n+1)\le-e^{\sqrt X}\}},
 \qquad H_X=\sum_{n\le X}{1\over n}.                    \tag{1}
\]

If

\[
 F(z)=\prod_{j=1}^{N}\left(1-{z\over a_j}\right),
\]

then, in the disk of convergence,

\[
 -{F'(z)\over F(z)}
 =\sum_{n\ge1}\left(\sum_{j=1}^{N}a_j^{-n}\right)z^{n-1}.
                                                               \tag{2}
\]

The finite analogue of the Li coefficient is therefore

\[
 \ell_n=N-\sum_{j=1}^{N}a_j^{-n}.                       \tag{3}
\]

This convention has exactly the sign of 104_80: an interior pole of
\(-F'/F\) contributes \(+a^{-n}\) to (2), and hence \(-a^{-n}\) to
\(\ell_n\).

## 2. Critical control: the event never occurs

Take the multiset

\[
 \{a_j\}=\{i,-i,i,-i\}.
\]

All its points lie on the unit circle and

\[
 \ell_n^{(0)}
 =4-4\cos\left({\pi n\over2}\right)\in\{0,4,8\}.        \tag{4}
\]

Hence

\[
 \boxed{{\cal D}_X(\ell^{(0)})=0\quad\text{for all }X.} \tag{5}
\]

No estimate is used: the indicator in (1) is identically zero.

## 3. Outer control: exact density \(1/8\)

Fix

\[
 1<R<e^{1/100},\qquad\text{for instance }R={201\over200},
\]

and take

\[
 \{a_j\}=\{Ri,-Ri,i/R,-i/R\}.
\]

The quartet is stable under conjugation and inversion, and

\[
 \ell_n^{(R)}
 =4-2(R^n+R^{-n})\cos\left({\pi n\over2}\right).        \tag{6}
\]

For odd \(n\) it equals \(4\); for \(n\equiv2\pmod4\) it is positive; and
for \(4\mid n\),

\[
 \ell_n^{(R)}=4-2(R^n+R^{-n})
             =-(2+o(1))R^n.                            \tag{7}
\]

The event in (1) begins, up to \(O(1)\) degrees, at

\[
 n_X={\sqrt X-\log2\over\log R}+O(1).                   \tag{8}
\]

Since only one class mod \(4\) survives,

\[
\begin{aligned}
 \sum_{\substack{n_X\le n\le X\\4\mid n}}{1\over n}
 &= {1\over4}\log {X\over n_X}+O(1)\\
 &= {1\over8}\log X+O(1).
\end{aligned}                                           \tag{9}
\]

Dividing by \(H_X=\log X+O(1)\),

\[
 \boxed{\lim_{X\to\infty}{\cal D}_X(\ell^{(R)})={1\over8}.} \tag{10}
\]

The choice \(R<e^{1/100}\) also checks the diagonal phase regulator. If
\(\varepsilon_X=e^{-X/100}\) shifts each point by \(O(\varepsilon_X)\),
the uniform perturbation over degrees \(n\le X\) is

\[
 O(X\varepsilon_XR^X)
 =\exp\{-(1/100-\log R)X+O(\log X)\}=o(1).              \tag{11}
\]

So (10) is not an artifact of having removed the regulator. A value like
\(R=2\) works for the unregulated quartet, but not for this literal
diagonal test.

## 4. Two controls with a positive Euler product

The quartets prove the sign and the scale. To check that the observable
also does not depend on having omitted the whole Euler structure,
consider first

\[
 Z_+(T)={1+4T^2\over(1-T)(1-4T)},\qquad T=4^{-s}.       \tag{12}
\]

Using the necklace polynomials

\[
 M_d(r)={1\over d}\sum_{e\mid d}\mu(e)r^{d/e},
\]

its number of formal primes of degree \(d\) is

\[
 \pi_d^+=M_d(4)+M_d(1)
 +{\bf1}_{2\mid d}M_{d/2}(4)
 -{\bf1}_{4\mid d}M_{d/4}(16).                         \tag{13}
\]

It is a non-negative integer. For \(4\nmid d\) this is immediate. For
\(4\mid d\), interpreting \(M_q(16)\) as the number of aperiodic
necklaces gives \(M_q(16)\le16^q/q\); together with the elementary lower
bound,

\[
 M_d(4)\ge {4^d\over d}-2^d,\qquad
 M_{d/4}(16)\le {4\,2^d\over d}
\]

give non-negativity for \(d\ge4\), and the initial degrees are checked
directly. The logarithmic derivative is

\[
 \Psi_k^+=4^k+1-(2i)^k-(-2i)^k,                        \tag{14}
\]

and

\[
 Z_+(1/(4T))=Z_+(T).                                    \tag{15}
\]

The corresponding completed function can be taken as

\[
 \Xi_+(s)=4^s+4^{1-s}.                                  \tag{16}
\]

All of its zeros satisfy

\[
 \Re\rho={1\over2},\qquad
 \Im\rho={ (2j+1)\pi\over2\log4}.
\]

The even canonical product of \(\cosh((s-\tfrac12)\log4)\) leaves no
exponential factor. Pairing conjugates, each Li summand is
\(2(1-\cos(n\theta_j))=|1-e^{in\theta_j}|^2\ge0\). Moreover the zeros up
to height \(n\) number \(O(n)\), and the tail is bounded by
\(O(n^2\sum_{j>n}j^{-2})=O(n)\). Hence its coefficients are non-negative
and \(O(n)\); in particular the deep event never occurs:

\[
 \boxed{{\cal D}_X(\lambda^+)=0\quad\text{for all }X.} \tag{17}
\]

The off-line control is the fully proved falsifier of 104_78:

\[
 Z_-(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},\qquad T=6^{-s}, \tag{18}
\]

\[
 \pi_d^-=M_d(6)+M_d(1)-M_d(3)-M_d(2)\ge0,\qquad
 \Psi_k^-=6^k+1-3^k-2^k,                               \tag{19}
\]

\[
 Z_-(1/(6T))=Z_-(T).                                    \tag{20}
\]

Its completion

\[
 \Xi_-(s)=6^s-5+6^{1-s}
\]

has zeros with real parts \(\log_6 2\) and \(\log_6 3\). The dominant
singularity produces

\[
 \lambda_n^-=-(1+o(1))
 \left({\log3\over\log2}\right)^n
 \quad(n\ \text{even}),
\]

and 104_78, including the diagonal regulator, proves

\[
 \boxed{\lim_{X\to\infty}{\cal D}_X(\lambda^-)={1\over4}.} \tag{21}
\]

## 5. Verdict

The controls prove three distinct facts:

1. the observable is exactly harmless on the critical control;
2. an off-line quartet generates the deep tail with positive density and
   the sign predicted by the identity of 104_80;
3. the same separation survives in two systems with an Euler product,
   positive Mangoldt weights and a functional equation.

Hence the possibility that the limit is zero by a normalization, a sign
error, or a universal Eulerian property is **falsified**. The observable
is also thereby **validated** as a detector.

What remains open is specific: proving (17) for the real zeta, that is,
for the ordinary placement of the weights \(\Lambda(m)\), its Gamma
factor and its continuous PNT. Doing so would exclude the interior poles
of 104_80 and prove RH; none of the controls above supplies that
exclusion.

## Reproduction

Run from the tools directory:

    python3 on_off_line_deep_observable_check.py
