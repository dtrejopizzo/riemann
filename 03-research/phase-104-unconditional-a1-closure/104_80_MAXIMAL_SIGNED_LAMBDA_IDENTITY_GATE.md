# 104_80 — Maximal signed Mangoldt identity and non-removable pole

**Result.** The requested joint cancellation between the real weights
\(\Lambda(m)\), all prime powers and the polar comparator has a closed
form. For

\[
 P_n(u)=L_{n-1}^{(1)}(u),\qquad
 t={z\over1-z},\qquad s_\varepsilon(z)=1+\varepsilon+t,
\]

\[
 Q_{n,\varepsilon}=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 P_n(\log m),\qquad
 p_n(\varepsilon)=\int_0^\infty e^{-\varepsilon u}P_n(u)\,du,
\]

one has, initially on the explicit disk where the double series used
below converge absolutely,

\[
 |z|<r_\varepsilon:={\varepsilon\over1+\varepsilon},
\]

\[
 \boxed{
 \sum_{n\ge1}\{Q_{n,\varepsilon}-p_n(\varepsilon)\}z^{n-1}
 =-{d\over dz}\log\!\left[
  (s_\varepsilon(z)-1)\zeta(s_\varepsilon(z))\right].}       \tag{1}
\]

The inversion \(\Lambda=\mu*\log\) and the Laguerre addition formula
produce exactly the same identity as a signed convolution. No additional
cross term that could receive a sign remains inside this linear
expansion.

Identity (1) **does not prove** the deep limit of `104_75`. If \(\rho\)
is a non-trivial zero of multiplicity \(m_\rho\), then the right-hand
side has a pole at

\[
 z_{\rho,\varepsilon}
 ={\rho-1-\varepsilon\over\rho-\varepsilon},              \tag{2}
\]

and

\[
 |z_{\rho,\varepsilon}|<1
 \quad\Longleftrightarrow\quad
 \Re\rho>{1\over2}+\varepsilon.                           \tag{3}
\]

Its principal part is

\[
 \boxed{
 -{d\over dz}\log\!\left[
  (s_\varepsilon(z)-1)\zeta(s_\varepsilon(z))\right]
 ={m_\rho/z_{\rho,\varepsilon}
       \over1-z/z_{\rho,\varepsilon}}+\text{holomorphic}.} \tag{4}
\]

Hence it contributes exactly \(m_\rho z_{\rho,\varepsilon}^{-n}\) to the
degree-\(n-1\) coefficient. No absolutely convergent rearrangement of the
Möbius--divisor expansion (10)--(13) can erase (4): all of them represent
the same meromorphic germ, and uniqueness of continuation preserves its
poles and residues. A Palm or cumulant formulation is included in this
conclusion only when, once expanded, it is such a rearrangement of the
same germ.

Thus the joint identity exists and is exact, but it turns the target
into the statement that there are no poles (2) inside the disk as
\(\varepsilon\downarrow0\). Requiring this for every \(\varepsilon>0\)
excludes zeros with \(\Re\rho>1/2\); the functional symmetry
\(\rho\leftrightarrow1-\overline\rho\) then also excludes
\(\Re\rho<1/2\). That statement is precisely RH. This document closes the
attack via **additional algebraic identity**; it does not prove the deep
limit, A1 or RH.

---

## 1. Simultaneous sum over all degrees

The ordinary Laguerre generating function gives

\[
 \sum_{n\ge1}P_n(u)z^{n-1}
 ={1\over(1-z)^2}\exp\!\left(-{uz\over1-z}\right).
                                                                    \tag{5}
\]

To justify the interchange, set \(r=|z|\). Since the coefficients of
\(P_n(u)=L_{n-1}^{(1)}(u)\) alternate in sign, for \(u\ge0\)

\[
 |P_n(u)|\le L_{n-1}^{(1)}(-u),
\]

and (5) gives

\[
 \sum_{n\ge1}|P_n(u)|r^{n-1}
 \le {1\over(1-r)^2}
       \exp\!\left({ur\over1-r}\right).                 \tag{5a}
\]

If \(r<\varepsilon/(1+\varepsilon)\), then
\(\varepsilon-r/(1-r)>0\), and therefore

\[
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 \sum_{n\ge1}|P_n(\log m)|r^{n-1}
 \le {1\over(1-r)^2}
 \sum_{m\ge2}{\Lambda(m)\over
 m^{1+\varepsilon-r/(1-r)}}<\infty.                    \tag{5b}
\]

The same bound, integrated against \(e^{-\varepsilon u}du\), justifies
the polar series. Tonelli for the moduli and then Fubini for the complex
series give

\[
\begin{aligned}
 \sum_{n\ge1}Q_{n,\varepsilon}z^{n-1}
 &={1\over(1-z)^2}
   \sum_{m\ge2}{\Lambda(m)\over
       m^{1+\varepsilon+z/(1-z)}}\\
 &={1\over(1-z)^2}
   \left(-{\zeta'\over\zeta}\right)(s_\varepsilon(z)).
                                                               \tag{6}
\end{aligned}
\]

Likewise,

\[
 \sum_{n\ge1}p_n(\varepsilon)z^{n-1}
 ={1\over(1-z)^2}
   \int_0^\infty e^{-(\varepsilon+t)u}\,du
 ={1\over(1-z)^2}{1\over s_\varepsilon(z)-1}.           \tag{7}
\]

Since \(s_\varepsilon'(z)=(1-z)^{-2}\), subtracting (7) from (6)
proves (1):

\[
 {1\over(1-z)^2}
 \left\{-{\zeta'\over\zeta}(s)-{1\over s-1}\right\}
 =-{d\over dz}\log\{(s-1)\zeta(s)\}.                   \tag{8}
\]

Multiplying (1) by \(z\) gives the version with powers \(z^n\):

\[
 \sum_{n\ge1}(Q_{n,\varepsilon}-p_n(\varepsilon))z^n
 =-z{d\over dz}\log\{(s_\varepsilon(z)-1)
                         \zeta(s_\varepsilon(z))\}.      \tag{9}
\]

## 2. The Möbius involution produces the same function

The Dirichlet convolution identity is

\[
 \Lambda(r)=\sum_{d\mid r}\mu(d)\log(r/d).              \tag{10}
\]

In combinatorial form, if
\(r=\prod_{j=1}^kp_j^{a_j}\), expand \(\log(r/d)\) in the marks
\(\log p_j\). For \(k\ge2\), each summand with mark \(j\) is paired by
switching the presence in \(d\) of any prime \(p_h\ne p_j\); the Möbius
signs are opposite. Only over a single tower \(r=p^a\) does
\(a-(a-1)=1\) copy of \(\log p\) survive. This is an exact
sign-reversing involution, not an estimate.

The addition formula

\[
 L_{n-1}^{(1)}(x+y)
 =\sum_{j=0}^{n-1}L_j(x)L_{n-1-j}(y)                    \tag{11}
\]

turns (10), with \(a=1+\varepsilon\), into

\[
 \boxed{
 Q_{n,\varepsilon}=\sum_{j=0}^{n-1}M_j(a)C_{n-1-j}(a),} \tag{12}
\]

where

\[
 M_j(a)=\sum_{d\ge1}{\mu(d)\over d^a}L_j(\log d),
 \qquad
 C_k(a)=\sum_{m\ge1}{\log m\over m^a}L_k(\log m).       \tag{13}
\]

Everything converges absolutely for \(a>1\). Summing (12) over the
degree returns (6). Incorporating (7), the convolution is exactly the
logarithmic quotient (1). In particular, the cancellation of multiprime
fibers generates no reserve: it leaves precisely the towers that form
\(-\zeta'/\zeta\).

## 3. Non-removable pole lemma

Let \(F_\varepsilon(z)=(s_\varepsilon(z)-1)
\zeta(s_\varepsilon(z))\). If \(\rho\) is a non-trivial zero of order
\(m_\rho\), then locally

\[
 F_\varepsilon(z)=
 (s_\varepsilon(z)-\rho)^{m_\rho}H(z),\qquad H(z_\rho)\ne0.
\]

Since \(s_\varepsilon'(z_\rho)\ne0\),

\[
 -{F_\varepsilon'(z)\over F_\varepsilon(z)}
 =-{m_\rho\over z-z_{\rho,\varepsilon}}+O(1),           \tag{14}
\]

which is (4). Moreover,

\[
 |\rho-\varepsilon|^2-|\rho-1-\varepsilon|^2
 =2\Re\rho-1-2\varepsilon.                              \tag{15}
\]

Equations (2)--(3) follow immediately. The multiplicity \(m_\rho\) is
positive, while the complex residue of \(-F_\varepsilon'/F_\varepsilon\)
at \(z_{\rho,\varepsilon}\) is \(-m_\rho\). Another zero at the same
point adds the same contribution and does not subtract it. The polar
comparator is already contained in \(F_\varepsilon\), and the Gamma part
is holomorphic at the image of a non-trivial zero, so nothing cancels
(14).

**Corollary 3.1 (maximality within the regroupings).** Every identity
obtained from (10)--(13) by absolutely convergent rearrangements agrees
with (1) in a neighborhood of zero. In \(\mathbb C\setminus\{1\}\), its
meromorphic continuation has, at each preimage (2) of a zero \(\rho\) of
\(\zeta\), a pole of residue \(-m_\rho\). These are all its poles there;
the trivial zeros also appear via (2), but they fall outside the unit
disk. Hence the identity cannot imply holomorphy of the disk without an
additional input that excludes the interior non-trivial poles.

The conclusion uses only uniqueness of continuation. It does not claim
that every future arithmetic inequality is impossible: a specific
inequality about the location of the ordinary primes could, in
principle, show that the poles do not exist. What is ruled out is
obtaining that conclusion from a new **exact rewriting** of the same
convolution.

## 4. Exact relation to the deep observable

For the diagonal of `104_75`, \(\varepsilon_X=e^{-X/100}\), one has

\[
 \lambda_{n,\varepsilon_X}
 =A_n+p_n(\varepsilon_X)-Q_{n,\varepsilon_X},
 \qquad
 \sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|=o(1).
                                                               \tag{16}
\]

If a zero with \(\Re\rho>1/2\) exists, then for large \(X\)
\(\varepsilon_X<\Re\rho-1/2\), and (3) places its pole inside the disk.
The interior poles of minimal modulus produce, by simultaneous
recurrence of their phases, a syndetic set \(D\) and constants
\(c>0,R>1\) with

\[
 \lambda_n\le-cR^n\qquad(n\in D)                         \tag{17}
\]

from a fixed index on (`104_56`). For any \(K>1/\log R\), (17) crosses
\(-e^{\sqrt X}\) in \(D\cap[K\sqrt X,X]\), whose harmonic mass is a
positive proportion of \(H_X\). By (16), the deep arithmetic event then
has positive liminf.

Conversely, proving that this event has zero logarithmic density
excludes every interior pole and proves RH. Identity (1) does not insert
a weaker lemma between these two statements: it shows they are the same
obstruction in Euler and meromorphic coordinates.

## 5. Decision

```text
proved:
  exact joint identity (1)/(9);
  sign-reversing Möbius involution and Laguerre convolution (12);
  exact location and residue of each zero (2)--(4);
  impossibility of erasing the pole via another absolutely convergent
  rearrangement of (10)--(13).

ruled out:
  another absolutely convergent rearrangement of (10)--(13)
  (including Palm/cumulant forms that reduce to it)
  + a new algebraic identity of the same germ
  => deep limit.

not ruled out:
  a new analytic inequality, specific to the ordinary primes,
  that directly proves the interior poles do not exist.

not proved:
  the deep limit, A1 or RH.
```

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 maximal_signed_lambda_identity_check.py
```

The checker uses `Fraction`. It verifies the addition formula (11), the
involution of (10) over formal factorizations, the modulus equivalence
(15) and the geometric coefficients of (4). It is a verification of the
algebraic identities; the analytic proof is in the text.
