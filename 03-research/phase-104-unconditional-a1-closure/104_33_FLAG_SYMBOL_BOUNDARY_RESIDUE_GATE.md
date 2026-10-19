# 104_33 — Flag symbol and the exact boundary–residue gate

**Role.** Attack the first moment of `104_30` via the Toeplitz symbol of
the prime–pole form, and determine whether a boundary estimate can produce
the missing proportional coercivity.

The symbol admits a closed form. However, it is meromorphic on the disc
exactly when zeros exist to the right of the critical line. Deforming the
prefix moment to the boundary produces an interior residue term that is not
a technical artifact: an off-line quartet leaves the real boundary symbol
unchanged and puts all its exponential load in those residues.

Hence, a proof using only the real boundary symbol is circular if it
omits the residues or assumes holomorphy on the disc. This document does
not rule out a signed arithmetic estimate that jointly controls boundary
and residues, but shows exactly which RH-strength term it would have to
control.

This document proves neither A1 nor RH.

**Pre-registration.** The tested statement is the first-moment ceiling
\(B_n/A_n\le1501/2002\) on the flag prefixes. The only inputs are: the
Euler product on \(\Re s>1\), meromorphic continuation, the functional
equation, conjugation, the paired Hadamard product, and the Laguerre
identities of `104_30`; all are unconditional. The mandatory falsifier is a
reciprocal off-line quartet. A deduction using only the symmetric inputs
must fail for that quartet; if it does not fail, it has omitted the
transversal zero datum.

## 1. Non-duplication audit

`103_26_INTEGRATED_STRONG_MARGIN_AUDIT.md` contains the Fejér identity
for another completed margin and rules out pointwise positivity of the
symbol. `phase-102/175_LOG_DERIVATIVE_RH_EQUIVALENCE.md` identifies
positivity of \(\xi'/\xi\) in the half-plane with RH. `104_30` builds the
positive flag reference and computes the entries \(q_d\).

What is added here is:

1. the exact closed sum of the **prime–pole** symbol of `104_30`;
2. a boundary–residue deformation formula for its prefix moment;
3. the closed residue of each right-hand zero;
4. a quartet falsifier that keeps the boundary exactly fixed and
   exponentially changes the flag ratio.

## 2. The exact prime–pole symbol

Let

\[
 h_\varepsilon(z)
 :=q_0(\varepsilon)+2\sum_{d\ge1}q_d(\varepsilon)z^d,
 \qquad s=s(z):={1\over1-z}.
 \tag{1}
\]

The triangular identity (18) of `104_30` gives

\[
 \sum_{n\ge1}P_{n,\varepsilon}z^{n-1}
 ={h_\varepsilon(z)\over(1-z)^2}.                    \tag{2}
\]

On the other hand,

\[
 \sum_{n\ge1}L_{n-1}^{(1)}(x)z^{n-1}
 ={1\over(1-z)^2}
   \exp\!\left(-{xz\over1-z}\right).                \tag{3}
\]

Applying (3) first in the half-plane of absolute convergence of the Euler
product,

\[
\begin{aligned}
 \sum_{n\ge1}P_{n,\varepsilon}z^{n-1}
 ={1\over(1-z)^2}\left[
 -{\zeta'\over\zeta}\!\left(1+\varepsilon+{z\over1-z}\right)
 -{1\over\varepsilon+z/(1-z)}\right].
\end{aligned}                                                 \tag{4}
\]

Since \(1+z/(1-z)=s\), (2)–(4) prove

\[
 \boxed{
 h_\varepsilon(z)
 =-{\zeta'\over\zeta}(s+\varepsilon)
  -{1\over s+\varepsilon-1}.}
 \tag{5}
\]

Removing the regulator, the singularity at \(s=1\) cancels, leaving the
regular germ

\[
 \boxed{
 h(z)=q_0+2\sum_{d\ge1}q_dz^d
 =-{\zeta'\over\zeta}(s)-{1\over s-1},
 \qquad h(0)=-\gamma.}
 \tag{6}
\]

Equation (6) is first a germ identity at \(z=0\) and then a meromorphic
continuation. RH is not assumed.

If \(B_n=A_n-\lambda_n\), then

\[
 \boxed{
 B_n=nq_0+2\sum_{d=1}^{n-1}(n-d)q_d.}
 \tag{7}
\]

By (24) and (30) of `104_30`, (7) is exactly the first moment of the flag
on any finite section \(K_{M,N}\) with \(N\ge n\):

\[
 {B_n\over A_n}=\langle u_n,K_{M,N}u_n\rangle.       \tag{8}
\]

## 3. Meromorphic Fejér lemma

Define the Fejér polynomial as a Laurent polynomial

\[
 \mathcal F_n(z)
 :=n+\sum_{d=1}^{n-1}(n-d)(z^d+z^{-d})
 ={(1-z^n)(1-z^{-n})\over(1-z)(1-z^{-1})}.          \tag{9}
\]

On \(|z|=1\),

\[
 \mathcal F_n(e^{i\theta})
 =\left|\sum_{j=0}^{n-1}e^{ij\theta}\right|^2\ge0.  \tag{10}
\]

**Lemma 3.1 (boundary plus residues).** Let \(H\) be a germ with real
coefficients at zero that continues meromorphically to a neighborhood of
the closed disc, with no poles on the circle, and with simple poles \(p\)
inside the disc, of residues \(r_p\). If

\[
 H(z)=a_0+\sum_{d\ge1}a_dz^d
\]

in its local Taylor disc, then

\[
\begin{aligned}
 &na_0+\sum_{d=1}^{n-1}(n-d)a_d\\
 &\quad={1\over2\pi}\int_{-\pi}^{\pi}
   \Re H(e^{i\theta})\,\mathcal F_n(e^{i\theta})\,d\theta
   -\sum_{|p|<1}r_p{\mathcal F_n(p)\over p},
\end{aligned}                                                 \tag{11}
\]

where non-real poles are grouped with their conjugates. In particular,
the right-hand side is real.

*Proof.* Subtract the principal parts and apply Fourier orthogonality to
the holomorphic part. Only one pole \(r/(z-p)\) needs to be computed. Its
local expansion and its expansion on the circle are, respectively,

\[
 {r\over z-p}=-\sum_{d\ge0}{r\over p^{d+1}}z^d,
 \qquad
 {r\over z-p}=\sum_{d\ge1}rp^{d-1}z^{-d}.           \tag{12}
\]

The difference between the local moment of the first series and the
boundary moment of the second is

\[
 -r\left[
 {n\over p}+\sum_{d=1}^{n-1}(n-d)
       (p^{d-1}+p^{-d-1})\right]
 =-r{\mathcal F_n(p)\over p}.                       \tag{13}
\]

Summing over the poles gives (11). \(\square\)

The finiteness hypothesis can be removed by meromorphic limits whenever
the sum in (13) converges absolutely. That is precisely what happens for
the logarithmic derivative of \(\xi\) with \(n\) fixed, as checked in the
next section. Poles on the circle are incorporated via the symmetric
radial limit/finite part; in particular, the critical zeros are part of
the boundary distribution and are not discarded by taking the pointwise
value away from their ordinates.

## 4. Specialization to the zeros of \(\zeta\)

For a nontrivial zero \(\rho\), write

\[
 w_\rho=1-{1\over\rho}.
\]

Then

\[
 |w_\rho|^2
 =1+{1-2\Re\rho\over|\rho|^2}.                     \tag{14}
\]

So \(w_\rho\) lies inside the disc exactly when
\(\Re\rho>1/2\). If \(m_\rho\) is the multiplicity, (6) and
\(ds/dz=s^2\) give

\[
 \boxed{
 \mathop{\rm Res}_{z=w_\rho}h(z)=-{m_\rho\over\rho^2}.}
 \tag{15}
\]

To fix the first term of the following formula without ambiguity, partial
sums of the logarithmic derivative of \(\xi\) are taken over complete
functional orbits and increasing height. In each finite sum, the interior
boundary distributional trace is used: the ordinary value away from the
critical poles and the normal Abel limit at those poles. Lemma 3.1 is
applied, with small symmetric indentations, and then the height is sent to
infinity. We denote the resulting limit by
\(\mathcal I_n^\partial(h)\). Local convergence of the Hadamard product
fixes its coefficients at zero, and the absolute convergence indicated in
(17) separately fixes the interior residues. No critical support is
assumed in this definition.

Hence (11), in that symmetric limit, becomes

\[
 \boxed{
 B_n=\mathcal I_n^\partial(h)
 +\sum_{\Re\rho>1/2}
   {m_\rho\over\rho(\rho-1)}\,\mathcal F_n(w_\rho).}
 \tag{16}
\]

Here \(\mathcal I_n^\partial(h)\) denotes the moment of the radial
boundary distribution, including the poles corresponding to zeros on the
line. For fixed \(n\), the sum of residues in (16) converges absolutely:
\(w_\rho\to1\), \(\mathcal F_n(w_\rho)=n^2+O_n(|\rho|^{-1})\), and

\[
 \sum_\rho {m_\rho\over1+|\Im\rho|^2}<\infty.        \tag{17}
\]

The flag formula becomes, with no abbreviation,

\[
 \boxed{
 \langle u_n,K_{M,N}u_n\rangle
 ={\mathcal I_n^\partial(h)\over A_n}
 +{1\over A_n}\sum_{\Re\rho>1/2}
   {m_\rho\mathcal F_n(w_\rho)\over\rho(\rho-1)}.}
 \tag{18}
\]

The Phase 104 sufficient ceiling is

\[
 \langle u_n,K_{M,N}u_n\rangle
 \le {1501\over2002}\qquad(n\ge150).                \tag{19}
\]

The sum in (18), not an operator norm, is the term any proof of (19) must
preserve.

## 5. What the boundary actually contains

From the completed definition

\[
 \xi(s)={1\over2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

one derives

\[
 h(z)={1\over s}-{1\over2}\log\pi
       +{1\over2}\psi(s/2)-{\xi'\over\xi}(s).       \tag{20}
\]

On \(z=e^{i\theta}\ne1\),

\[
 s={1\over2}+{i\over2}\cot{\theta\over2}.          \tag{21}
\]

The function \(\xi(1/2+it)\) is real. Away from its zeros,
\(\xi'/\xi(1/2+it)\) is purely imaginary. Hence the real boundary
pointwise value is only

\[
 \Re h(e^{i\theta})
 =\Re\left[{1\over s}-{1\over2}\log\pi
                  +{1\over2}\psi(s/2)\right].       \tag{22}
\]

This does not license erasing the \(\xi'/\xi\) part: critical zeros
appear as mass in the radial limit of (22), and the right-hand zeros
appear in the residue sum of (16).

In particular,

\[
 h\text{ holomorphic on }\mathbb D
 \quad\Longleftrightarrow\quad
 \zeta\text{ has no zeros with }\Re\rho>1/2
 \quad\Longleftrightarrow\quad \mathrm{RH},          \tag{23}
\]

where the last equivalence uses the functional symmetry. Treating (6) as
a Hardy symbol holomorphic throughout the disc already imports RH.

## 6. Exact falsifier: same boundary, different coercivity

Let \(\rho\) be a point with \(1/2<\Re\rho<1\), and let

\[
 \mathcal O(\rho)=\{\rho,\bar\rho,1-\rho,1-\bar\rho\},
 \qquad
 Q_\rho(s)=\prod_{\eta\in\mathcal O(\rho)}(s-\eta). \tag{24}
\]

Multiplying the completed divisor by \(Q_\rho^M\) preserves conjugation
and the functional equation. In the symbol it produces

\[
 \widetilde h(z)=h(z)-M{Q_\rho'\over Q_\rho}(s(z)).  \tag{25}
\]

If \(s=1/2+it\), then \(Q_\rho(s)\) is real and nonzero. Hence

\[
 \boxed{
 \Re\widetilde h(e^{i\theta})=\Re h(e^{i\theta})}
 \tag{26}
\]

throughout the boundary, also in the distributional sense: the quartet
adds no zeros on the line.

Set \(w=w_\rho\), so that \(|w|<1\). The elementary identity

\[
 {\mathcal F_n(w)\over\rho(\rho-1)}
 ={(1-w)^2\over w}\mathcal F_n(w)
 =w^n+w^{-n}-2                                      \tag{27}
\]

proves that the residues of the two right-hand zeros contribute

\[
\begin{aligned}
 2M\Re\left({\mathcal F_n(w)\over\rho(\rho-1)}\right)
 &=2M\Re(w^n+w^{-n}-2)\\
 &=-M Q_n,
\end{aligned}                                                 \tag{28}
\]

where

\[
 Q_n=4-2\Re(w^n+w^{-n})
 =4-4\cosh(n\alpha)\cos(n\vartheta),
 \quad w=e^{-\alpha+i\vartheta}.                    \tag{29}
\]

Here \(Q_n\) is the quartet's contribution to the **Li coefficient**. The
Weil form \(2\Re\lambda_n\) doubles it and carries the factor \(8\) used
in other documents; the two normalizations are not mixed in (28)–(29).

This matches exactly the change
\(\widetilde B_n-B_n=-M Q_n\), since the quartet adds \(M Q_n\) to the Li
coefficient and does not change \(A_n\).

Now use the falsifier already fixed in `104_26`,

\[
 w={1\over2}e^{74\pi i/75},\qquad \rho={1\over1-w}. \tag{30}
\]

At \(n=150\), \(\cos(150\cdot74\pi/75)=1\), and

\[
 -Q_{150}=4\bigl(\cosh(150\log2)-1\bigr)>0.         \tag{31}
\]

Quantity (31), multiplied by \(M\), exceeds any fixed multiple of
\(A_{150}\), while (26) leaves invariant every estimate that sees only the
real boundary symbol. Consequently:

> no uniform bound of (19) can be deduced exclusively from
> \(\Re h|_{\partial\mathbb D}\), the functional equation, and the
> symmetry. It must control the signed residue sum in (18), or use
> arithmetic that rejects the quartet.

The result does not claim that such arithmetic control is impossible. It
claims that replacing it with a boundary-symbol bound erases exactly the
datum that decides RH.

## 7. Rational verification

The file `tools/flag_symbol_residue_check.py` uses the rational quartet

\[
 w={i\over2},\qquad \rho={1\over1-w}={4+2i\over5},
\]

and checks with `Fraction`, with no floating point:

1. identity (27) for \(1\le n\le20\);
2. that the residue of the right-hand pair is \(-Q_n\);
3. that \(Q_\rho'/Q_\rho(1/2+it)\) has zero real part on a rational grid
   of \(t\).

Reproduced with

    cd 03-research/phase-104-unconditional-a1-closure/tools
    python3 flag_symbol_residue_check.py

## Status

* **Proved:** the closed symbol (5)–(6), the boundary–residue lemma
  (11), each zero's residue (15), the first-moment formula (16)–(18),
  and the quartet's boundary invariance (26)–(31).
* **Ruled out:** obtaining (19) from a bound on the real boundary
  symbol, or invoking Hardy/Toeplitz theory while unprovenly assuming
  that \(h\) is holomorphic on the disc.
* **Remains:** a signed arithmetic estimate, specific to
  \(\zeta\), for the full term of (18). It must reject the quartet and
  cannot separate the boundary from its residues via absolute values.
* **Not proved:** (19), A1, and RH.
</content>
