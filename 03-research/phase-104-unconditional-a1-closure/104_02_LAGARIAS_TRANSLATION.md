# 104_02 — Sign erratum and corrected translation of Lagarias toward A1

**Objective:** audit the sign of the incomplete Li term before using Lagarias's Theorem 6.1.
This document entirely replaces the earlier translation.

**Binding status.** The printed equations (1.15), (1.17), (6.2), and step (6.7) of
Lagarias carry the opposite sign to the residue of the integrand appearing in his own proof.
Hence the former Theorem A, its form A′, and the former corollaries B1–B2 are withdrawn. The
correct exact coordinate of A1 contains
\(-\lambda_n(\sqrt n)\), not \(+\lambda_n(\sqrt n)\).

The search carried out on 25-Jul-2026 on the arXiv record math/0404394, the article's page on
Numdam, and the results linked from both **found no corrigendum**. This does not turn the
erratum into an official correction by the author: it is an internal audit based on the
residue computation reproduced below.

---

## 1. Printed statement and local residue computation

Lagarias defines (eq. (1.14), also (6.1))

\[
\lambda_n(T,\pi)=
\sum_{\substack{\rho\in Z(\pi)\\ |\Im\rho|<T}}
\left[1-\left(1-\frac1\rho\right)^n\right]
\]

and in (6.4)

\[
k_n(s)=\left(1+\frac1s\right)^n-1.
\]

The integrand of the proof of Theorem 6.1 is

\[
F_n(s)=k_n(s)\left(-\frac{L'}L(s+1,\pi)\right).
\]

Let \(\rho\) be a nontrivial zero of multiplicity \(m_\rho\), and let
\(s_0=\rho-1\). Locally,

\[
\frac{L'}L(s+1,\pi)=\frac{m_\rho}{s-s_0}+O(1).
\]

Then, with no global convention or estimate whatsoever,

\[
\boxed{
\mathop{\mathrm{Res}}_{s=\rho-1}F_n(s)
=-m_\rho k_n(\rho-1)
=m_\rho\left[1-\left(\frac{\rho}{\rho-1}\right)^n\right].}
\tag{1.1}
\]

The minus sign comes exclusively from \(-L'/L\). The printed proof uses, in the deformation,
the residue \(+m_\rho k_n(\rho-1)\).

Let \(C_1\) be the small circle and \(C_2\) the large rectangle, both oriented
counterclockwise as in the article. For nested contours,

\[
\frac1{2\pi i}\int_{C_2}F_n
-\frac1{2\pi i}\int_{C_1}F_n
=\sum_{C_2\setminus C_1}\mathrm{Res}\,F_n.
\tag{1.2}
\]

There is a second typographical inconsistency here in the source: §6 defines
\(I_2=\int_{C_2}F_n(s)\,ds\), without \((2\pi i)^{-1}\), but equation (6.7)
uses it as a normalized integral. To avoid inheriting that ambiguity, we define

\[
 \widehat I_2(n):={1\over2\pi i}\int_{C_2}F_n(s)\,ds.           \tag{1.3}
\]

The normalized integral over \(C_1\) is \(S_f(n,\pi)\). Moreover, using the zero symmetry
employed in the article itself,

\[
\sum_{\substack{\rho\in Z(\pi)\\|\Im\rho|<T}}
m_\rho k_n(\rho-1)
=-\lambda_n(T,\pi^\vee).
\tag{1.4}
\]

Combining (1.1)–(1.4), the corrected and normalized equation (6.7) is

\[
\boxed{
\widehat I_2(n)=S_f(n,\pi)+\lambda_n(T,\pi^\vee)+O(1),}
\tag{1.5}
\]

not \(S_f-\lambda_n(T,\pi^\vee)+O(1)\). The rest of the §6 contour estimate proves
\(\widehat I_2(n)=O_\pi(\sqrt n\log n)\), but not literally with its printed
choice \(T=\sqrt n+\varepsilon_n\). This point must also be repaired before
extracting the conclusion.

### 1.1. Repair of the horizontal segment

The printed equation (6.12) only gives, when moving one unit to the right,

\[
 {\lvert k_n(s+1)+1\rvert\over\lvert k_n(s)+1\rvert}
 \le e^{n/T^2}.
\]

With \(T^2=n\), combining it with the factor \(1/2\) of the Dirichlet series
majorant yields \(e/2>1\), not geometric decay. We instead fix

\[
 T=2\sqrt n+\varepsilon_n,\qquad 0<\varepsilon_n<1,                 \tag{1.6a}
\]

chosen at distance \(\gg_\pi1/\log n\) from every zero ordinate in that
band. Such a choice exists by the local zero count used in the article itself.

On the horizontal sides \(s=\sigma\pm iT\), for \(\lvert\sigma\rvert\le3\),

\[
 \left\lvert1+{1\over s}\right\rvert^2
 =1+{2\sigma+1\over\sigma^2+T^2}
 \le1+{7\over4n},
\]

so that \(\lvert k_n(s)\rvert\le e^{7/8}+1\); formula (6.8) and the chosen
separation give \(\lvert L'/L(s+1,\pi)\rvert\ll_\pi(\log n)^2\).
For \(\sigma\ge3\), set

\[
 G_n(s)=k_n(s)+1=\left(1+{1\over s}\right)^n.
\]

The exact identity

\[
 {G_n(s+1)\over G_n(s)}
 =\left(1-{1\over(s+1)^2}\right)^n
\]

implies

\[
 \left\lvert{G_n(s+1)\over G_n(s)}\right\rvert
 \le(1+T^{-2})^n\le e^{1/4}.                       \tag{1.6b}
\]

By absolute convergence of the Euler logarithm, the **absolute majorant**
of the Dirichlet series of \(L'/L(s+1,\pi)\) gains a factor of at most
\(1/2\) when \(\sigma\) is increased by one unit. Within each cell,
\(0\le t\le1\), one also has

\[
 \left({1+1/(s+t)\over1+1/s}\right)^n
 =\left(1-{t\over(s+t)(s+1)}\right)^n,
\]

whose modulus is at most \((1+T^{-2})^n\le e^{1/4}\). Hence the majorant of the
term \(G_n(s)L'/L(s+1,\pi)\) decreases block by block with ratio

\[
 q={e^{1/4}\over2}<1,                               \tag{1.6c}
\]

and the term coming from \(k_n=G_n-1\) decreases at least with ratio
\(1/2\). This proves the geometric integrability of the two horizontal
sides. The vertical sides retain the bound
\(O_\pi(\sqrt n\log n)\), since changing \(T\) by a fixed factor does not alter
their argument. Consequently,

\[
 \widehat I_2(n)=O_\pi(\sqrt n\log n).              \tag{1.6d}
\]

Finally, if \(\sqrt n\le\lvert\gamma\rvert\le2\sqrt n+1\) and
\(0<\beta<1\), then

\[
 \left\lvert1-{1\over\rho}\right\rvert^{2n}
 =\left(1+{1-2\beta\over\lvert\rho\rvert^2}\right)^n
 \le(1+1/n)^n\le e.                                \tag{1.6e}
\]

Each Li summand in that band has modulus at most \(1+e^{1/2}\), and
the zero count gives \(O_\pi(\sqrt n\log n)\) zeros. Hence

\[
 \lambda_n(2\sqrt n+\varepsilon_n,\pi^\vee)
 -\lambda_n(\sqrt n,\pi^\vee)
 =O_\pi(\sqrt n\log n).                            \tag{1.6f}
\]

Equations (1.5) and (1.9)–(1.11) prove, now with the horizontal gap
repaired, that

\[
\boxed{
S_f(n,\pi)=-\lambda_n(\sqrt n,\pi^\vee)
+O_\pi(\sqrt n\log n).}
\tag{L1c}
\]

This is the corrected version of the printed equations (1.15) and (6.2).

### 1.2. Another adjacent sign typo that is not imported

The specialization to \(\zeta\) printed in (4.13) writes

\[
 S_f(n,\pi_{\rm triv})
 =\sum_{j=1}^n(-1)^{j-1}{n\choose j}\eta_{j-1}.       \tag{1.6}
\]

That alternating factor simultaneously contradicts:

1. Definition 4.2,
   \(-\zeta'/\zeta(1+s)=s^{-1}+\sum_{j\ge0}\eta_js^j\);
2. the general definition (4.8),
   \(S_f(n)=\sum_{j=1}^n{n\choose j}\eta_{j-1}\);
3. the residue extraction on the small circle (6.5), because
   \(k_n(s)=\sum_{j=1}^n{n\choose j}s^{-j}\).

Already at \(n=2\), (4.8)/(6.5) give \(2\eta_0+\eta_1\), while (4.13) gives
\(2\eta_0-\eta_1\). The chain used here adopts the general definition and
residue, with no alternation. This adjacent typo does not change (L1c), but it confirms
that the §4–§6 signs must be recomputed and not copied by reference.

For a non-self-dual representation, the published PDF also mixes
\(\pi\) and \(\pi^\vee\) in (4.6). The form compatible with the derivation is

\[
 \lambda_n(\pi)=S_\infty(n,\pi^\vee)-S_f(n,\pi^\vee)+\delta(\pi), \tag{1.7}
\]

or its dual. Since \(S_\infty(n,\pi)=S_\infty(n,\pi^\vee)\) and \(\zeta\) is
self-dual, this editorial inconsistency also does not alter the A1 specialization.

---

## 2. Corrected unconditional asymptotics

The exact arithmetic formula of the article is

\[
\lambda_n(\pi)=S_\infty(n,\pi^\vee)-S_f(n,\pi^\vee)+\delta(\pi^\vee).
\tag{2.1}
\]

With
\(S_\infty(n,\pi)=\frac N2n\log n+C_1(\pi)n+O_\pi(1)\)
and (L1c), we obtain

\[
\boxed{
\lambda_n(\pi)=\frac N2n\log n+C_1(\pi)n
+\lambda_n(\sqrt n,\pi)+O_\pi(\sqrt n\log n).}
\tag{L2c}
\]

Thus the printed equation (1.17) must carry a **plus** sign before the incomplete
coefficient. The formula under RH does not change, because under RH
\(\lambda_n(\sqrt n,\pi)=O_\pi(\sqrt n\log n)\).

For \(\zeta\), \(N=1\), \(Q=1\), \(\pi^\vee=\pi\), and

\[
C_1=\frac12(\gamma-1-\log2\pi).
\]

Our exact block satisfies

\[
A_n=\frac n2(\log n+\gamma-1-\log2\pi)+O(\log n).
\tag{2.2}
\]

We define the exact remainder with the corrected sign:

\[
\boxed{
\widetilde\varepsilon_n:=A_n-\lambda_n+\lambda_n(\sqrt n).}
\tag{2.3}
\]

It is a real number, not an \(O\)-symbol. From (L2c) and (2.2) one obtains

\[
\boxed{
|\widetilde\varepsilon_n|\le C_*\sqrt n\log n}
\qquad(n\ge2),
\tag{2.4}
\]

for some absolute constant \(C_*>0\) not made explicit by Lagarias's argument.

The quantity used in the withdrawn version was

\[
\varepsilon_n^-:=A_n-\lambda_n-\lambda_n(\sqrt n).
\]

The two are related exactly by

\[
\boxed{
\varepsilon_n^-=\widetilde\varepsilon_n-2\lambda_n(\sqrt n).}
\tag{2.5}
\]

Therefore **no** unconditional
\(|\varepsilon_n^-|\ll\sqrt n\log n\) is available. If RH fails, the second term of (2.5) can be
exponential along a subsequence. The former claim that only a constant needed to be made
effective for \(\varepsilon_n^-\) is withdrawn.

---

## 3. Corrected prime-side form

Let

\[
\mathcal J_n:=\int_0^\infty E(u)K_n(u)\,du,
\qquad
\lambda_n=A_n-n-\mathcal J_n.
\tag{3.1}
\]

By definition (2.3), with no estimate used,

\[
\boxed{
\mathcal J_n+n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n.}
\tag{A'_c}
\]

This replaces the former Theorem A′. The incomplete term enters with a minus sign.

---

## 4. A1 in the corrected coordinate

Let \(a=\log2\), \(\theta\in(0,\tfrac12)\), let \(T_n(\theta)\) be as in 104_01, and

\[
q_{n,\theta}=(1-\theta)A_n+1-L_n^{(1)}(a).
\]

The exact decomposition already proved gives

\[
\mathrm{A1}_\theta
\iff
\mathcal J_n+n+R_n(T_n(\theta))\le(1-\theta)A_n.
\tag{4.1}
\]

Substituting (A′c), we obtain the exact statement that replaces the former Theorem B:

\[
\boxed{
\mathrm{A1}_\theta
\iff
-\lambda_n(\sqrt n)+\widetilde\varepsilon_n
+R_n(T_n(\theta))\le(1-\theta)A_n.}
\tag{B_c}
\]

There is no \(O\) in this equivalence. Both
\(\widetilde\varepsilon_n\) and \(R_n\) keep their exact sign.

Equivalently,

\[
\lambda_n(\sqrt n)
\ge -(1-\theta)A_n+\widetilde\varepsilon_n+R_n(T_n(\theta)).
\tag{4.2}
\]

Thus the corrected translation reduces the difficulty to a **lower bound**, not an upper one,
for the incomplete block.

### Corrected one-sided corollaries

Using (2.4) and \(|R_n(T_n(\theta))|\le\theta A_n\):

\[
\boxed{
\lambda_n(\sqrt n)\ge
-(1-2\theta)A_n+C_*\sqrt n\log n
\quad\Longrightarrow\quad\mathrm{A1}_\theta.}
\tag{B1_c}
\]

Conversely,

\[
\boxed{
\mathrm{A1}_\theta
\quad\Longrightarrow\quad
\lambda_n(\sqrt n)\ge-A_n-C_*\sqrt n\log n.}
\tag{B2_c}
\]

The gap between the two conditions remains
\(2\theta A_n+2C_*\sqrt n\log n\), but now both are **lower** bounds. Neither can be
replaced by an upper bound on the incomplete coefficient.

For \(\theta=\tfrac14\), the exact target is

\[
\boxed{
-\lambda_n(\sqrt n)+\widetilde\varepsilon_n+R_n(T_n(\tfrac14))
\le\frac34A_n,\qquad n\ge150.}
\tag{4.3}
\]

---

## 5. What a verified height actually controls

If all zeros with \(|\gamma|<\sqrt n\) are on the critical line, each pair contributes

\[
2-2\cos(n\theta_\rho)\in[0,4],
\]

and hence

\[
0\le\lambda_n(\sqrt n)\le4N(\sqrt n).
\tag{5.1}
\]

For the corrected coordinate, the first inequality is now what matters. From (B1c), a
sufficient condition is

\[
C_*\sqrt n\log n\le(1-2\theta)A_n,
\tag{5.2}
\]

together with localization of the zeros up to \(\sqrt n\). Since \(C_*\) is not made explicit,
this does not by itself produce a certified numerical range. And even if it were made explicit,
it would still be a finite corollary: it does not prove A1 uniformly.

The editorial discrepancy between
\(T^2/[2(\log T)^2]\) in the published article and
\(T^2/[4(\log T)^2]\) in the arXiv source is kept as a bibliographic datum, but it does not
enter the closure of A1.

---

## 6. Off-line quartet and the critical direction

Let \(w_\rho=1-1/\rho\). For a symmetric off-line quartet one can write
\(w=e^{\alpha+i\vartheta}\), with \(\alpha>0\), and the full contribution is

\[
4-4\cosh(n\alpha)\cos(n\vartheta).
\tag{6.1}
\]

Once the quartet's height is less than \(\sqrt n\), the same contribution appears in
\(\lambda_n(\sqrt n)\). It takes exponentially large values of both signs along
subsequences, with Bombieri–Lagarias's precise formulation needed to avoid assuming an
isolated phase. That is why a uniform lower bound like (4.2) is still RH-strength.

The factor \(4\) corresponds to the Li coefficient, which sums the four zeros once. The
Weil-form/autocorrelation form \(2\mathrm{Re}\,\lambda_n\) doubles this expression and
produces \(8-8\cosh(n\alpha)\cos(n\vartheta)\); the two normalizations must not be mixed.

The erratum does not prove A1; it correctly identifies the side that must be attacked.

---

## 7. Diagnostic verification

The tool tools/lagarias_translation_check.py now computes

\[
\widetilde D_n:=\lambda_n-A_n-\lambda_n(\sqrt n)
=-\widetilde\varepsilon_n,
\tag{7.1}
\]

not the former residual
\(\lambda_n-A_n+\lambda_n(\sqrt n)\). It uses two radii to detect instability of the
Cauchy extraction. The result is exclusively diagnostic in float64; it certifies neither
\(C_*\), nor A1, nor RH.

The decisive sign test is algebraic and is given in (1.1): the program only checks that the
low-rank numerical data are consistent with the corrected translation.

**Run of 25-Jul-2026.** The rows stable between the two radii go up to \(n=1600\);
\(n=2000\) and \(n=2400\) are discarded by the 1% guard. In the stable sample,
\[
\max\frac{|\widetilde D_n|}{\sqrt n\log n}=0.2457
\]
is attained at \(n=8\). These figures are not certified intervals nor an effective constant.

---

## 8. Binding ledger

1. **Withdrawn:**
   \(A_n-\lambda_n=+\lambda_n(\sqrt n)+O(\sqrt n\log n)\).
2. **Withdrawn:**
   \(|A_n-\lambda_n-\lambda_n(\sqrt n)|\ll\sqrt n\log n\) unconditional.
3. **Withdrawn:** the former B1 and B2, which required upper bounds on the incomplete block.
4. **Adopted:**
   \(A_n-\lambda_n=-\lambda_n(\sqrt n)+\widetilde\varepsilon_n\), with
   \(|\widetilde\varepsilon_n|\le C_*\sqrt n\log n\).
5. **Exact target:** (4.3), equivalent to A1, which requires controlling from below the
   incomplete block together with the two signed remainders.
</content>
