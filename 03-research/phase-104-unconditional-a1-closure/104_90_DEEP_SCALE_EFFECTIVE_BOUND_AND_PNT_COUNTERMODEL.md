# 104_90 — Effective bound on the Deep scale and PNT countermodel

**Result.** The unconditional information formed by a verified height
\(H\), a Vinogradov--Korobov zero-free region, and the effective zero
count controls the deep observable only up to

\[
 \boxed{\limsup_{X\to\infty}\mathcal D_X(\lambda)\le{1\over2}.} \tag{1}
\]

It does not produce the zero limit of 104_75. With \(H=3\cdot10^{12}\),
the same estimate makes the event empty, up to the bookkeeping of minor
constants, up to scale \(X\asymp4H^4=3.24\cdot10^{50}\). After that it
asymptotically leaves half the harmonic mass uncontrolled.

A countermodel is further constructed that preserves nonnegative Euler
coefficients on ordinary prime powers, a continuous PNT with VK-type
error, and an entire completion with a functional equation, but has
zeros off the line and positive Deep density. The model introduces
additional Euler poles and changes the weights of the \(7^k\) tower.
Hence it is not a counterexample to RH nor to the exact axioms of
zeta. It does prove that PNT, positivity, prime support, and a broad
functional equation do not substitute for the literal values
\(\Lambda(p^k)=\log p\).

This document does not prove Deep-\(\Lambda\), A1, or RH. It closes the
attack based only on the radial scale of the zeros and on PNT
consequences of the weights.

---

## 1. Radial shift over a verified height

Let \(\rho=\beta+i\gamma\), \(\gamma>0\), with
\(1/2\le\beta<1\), representing a functional orbit. Set

\[
 a(\beta,\gamma)
 =\log\left|{\rho\over\rho-1}\right|
 ={1\over2}\log{\beta^2+\gamma^2
                 \over(1-\beta)^2+\gamma^2}.            \tag{2}
\]

If a zero-free region gives
\(\beta\le1-\delta(\gamma)\), then

\[
 a(\beta,\gamma)
 \le a_{\rm VK}(\gamma)
 :={1\over2}\log\left(
 1+{1-2\delta(\gamma)\over
       \gamma^2+\delta(\gamma)^2}\right).               \tag{3}
\]

Suppose all zeros with \(|\gamma|\le H\) are certified on the line, and
define

\[
 a_H=\sup_{\gamma>H}a_{\rm VK}(\gamma).
\]

The universal bound of 104_76 gives

\[
 \boxed{a_H<{1\over2H^2}.}                              \tag{4}
\]

Even though \(a_H\) is tiny, it is fixed, and the factor \(e^{a_Hn}\)
eventually exceeds every barrier \(e^{o(n)}\).

## 2. Effective bound for the Li coefficients

The numerical count of 103_58, §2, is

\[
 \mathcal N(T)\le25T\log T\qquad(T\ge10),               \tag{5}
\]

where both signs of the ordinates and multiplicities are counted. For
\(n\ge\max(5,H/2)\), split the orbits into
\(H<\gamma\le2n\) and \(\gamma>2n\).

In the first band there are at most \(50n\log(2n)\) labels. The
quartet identity of 104_76 and (3) give

\[
 |q_n(\rho)|\le4(1+e^{a_Hn}),                            \tag{6}
\]

and a total cost no larger than

\[
 200n\log(2n)(1+e^{a_Hn}).                               \tag{7}
\]

For \(\gamma>2n\), the short phase expansion gives

\[
 |q_n(\rho)|\le {9n^2\over\gamma^2}.                    \tag{8}
\]

Partial summation of (5) implies

\[
 \sum_{|\gamma|>2n}{m_\rho\over\gamma^2}
 \le {25\{\log(2n)+1\}\over n},                         \tag{9}
\]

so that the second band costs at most
\(225n\{\log(2n)+1\}\). Zeros up to \(H\) contribute nonnegatively.
Combining and rounding up,

\[
 \boxed{
 \lambda_n\ge
 -500n\{\log(2n)+1\}(1+e^{a_Hn}).}                     \tag{10}
\]

The sign of no unverified zero has been used.

For \(n<H/2\), all unverified zeros are already in the band
\(|\gamma|>2n\). The same partial summation, now starting from \(H\),
gives

\[
 \lambda_n\ge
 -{450n^2\{\log H+1\}\over H}.                          \tag{10a}
\]

This prefix is finite and its cost grows only polynomially; hence it
cannot cross \(-e^{\sqrt X}\) once \(X\) is large enough.

## 3. Consequence for the deep event

Recall

\[
 \mathcal D_X(\lambda)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \mathbf1_{\{\lambda_n+\log(n+1)\le-e^{\sqrt X}\}}.    \tag{11}
\]

For \(X\) large enough, (10)--(10a) show that every index counted in
(11) must satisfy

\[
 n\ge L_H(X):=
 {\sqrt X-\log[2000X\{\log(2X)+1\}]\over a_H}.          \tag{12}
\]

If \(L_H(X)>X\), the event is empty. Otherwise,

\[
 \mathcal D_X(\lambda)
 \le {H_X-H_{\lceil L_H(X)\rceil-1}\over H_X}.          \tag{13}
\]

Since \(a_H\) is fixed,

\[
 \log L_H(X)={1\over2}\log X-\log a_H+o(\log X),       \tag{14}
\]

and (1) follows from (13). The constant \(1/2\) is optimal for the
pointwise radial information alone (10): the adversarial sequence
\(-e^{a_Hn}\) attains it. It is not claimed to be optimal within the
much more rigid class of genuine zeta functions. A single fixed
exterior quartet allowed by these inputs already produces positive
density; that is enough to prove they cannot give the zero limit.

With \(H=3\cdot10^{12}\), (4) gives

\[
 a_H<5.556\cdot10^{-26},
 \qquad L_H(X)\sim1.8\cdot10^{25}\sqrt X.              \tag{15}
\]

The crossover \(L_H(X)\approx X\) occurs around
\(X\approx3.24\cdot10^{50}\). This is a diagnostic scale, not a
certified range: a literal threshold must preserve the logarithmic
terms of (12) and all constants of the chosen zero-free region.

## 4. Continuous countermodel with PNT

Use the exterior lattice model of 104_78,

\[
 Z_-(T)={(1-3T)(1-2T)\over(1-T)(1-6T)},
 \qquad Z_-(T)=Z_-\!\left({1\over6T}\right),            \tag{16}
\]

and subordinate it to the tower of the prime \(7\):

\[
 T(s)=\sqrt{7\over6}\,7^{-s},
 \qquad W(s)=Z_-(T(s)),
 \qquad F(s)=\zeta(s)W(s).                              \tag{17}
\]

The additional logarithmic derivative lives only on \(7^\ell\):

\[
 -{W'(s)\over W(s)}
 =\sum_{\ell\ge1}{b(7^\ell)\over7^{\ell s}},           \tag{18}
\]

\[
 \boxed{
 b(7^\ell)=\log7\left({7\over6}\right)^{\ell/2}
 (6^\ell+1-3^\ell-2^\ell)>0.}                          \tag{19}
\]

Positivity is exact because

\[
 6^\ell+1-3^\ell-2^\ell=(3^\ell-1)(2^\ell-1).         \tag{20}
\]

Moreover,

\[
 \sum_{7^\ell\le x}b(7^\ell)=O(x^\sigma),
 \qquad
 \sigma={\log42\over2\log7}=0.960391\ldots<1.          \tag{21}
\]

Hence

\[
 \psi_F(x)=x+O\!\left(xe^{-\eta(x)}+x^\sigma\right),   \tag{22}
\]

which asymptotically preserves a VK-type error, after adjusting the
threshold and the constant.

Write

\[
 r(s)={1\over2}+{\log7\over\log6}
                   \left(s-{1\over2}\right).           \tag{23}
\]

Since \(T(s)=6^{-r(s)}\), the completion

\[
 \xi(s)\,\Xi_-(r(s)),
 \qquad \Xi_-(r)=6^r-5+6^{1-r},                        \tag{24}
\]

is entire and invariant under \(s\mapsto1-s\). Its exterior zeros have
real parts

\[
 \boxed{
 {1\over2}\pm{\log(3/2)\over2\log7}
 =0.395816\ldots,\ 0.604184\ldots.}                    \tag{25}
\]

The corresponding Li sequence therefore has exponential excursions and
positive Deep density.

### Precise scope

The Euler factor \(W\) has additional poles in the vertical families
with real parts \(\sigma\) and \(1-\sigma\); the factor
\(\Xi_-(r(s))\) cancels them in the completion. The model also does
not preserve the exact Gamma factor nor the values \(\Lambda(7^\ell)\).
Consequently,

\[
 \begin{gathered}
 \text{PNT/VK + nonnegative weights + prime support + broad FE}
 \not\Longrightarrow \mathrm{RH},\\
 \text{but the model does not satisfy the full exact data of }\zeta.
 \end{gathered}                                         \tag{26}
\]

## 5. Verdict

The scale \(e^{\sqrt X}\) does not make the Deep limit elementary. It
only moves the obstruction to heights \(\gamma\lesssim X^{1/4}\), as
104_76 already proved. A fixed verified height ultimately leaves half
the harmonic mass undecided. Even a very strong continuous PNT does
not eliminate an exterior factor if positive changes in a single prime
tower are allowed.

The successor, if it exists, must jointly use the exact values of all
ordinary towers; neither the radial scale, nor PNT, nor the positivity
of the weights can supply it separately.

## 6. Reproduction

From the tools directory:

    python3 deep_scale_pnt_countermodel_check.py

The checker verifies the rational functional equation, the positive
factorization of each added height, the exponent \(\sigma<1\), the
exterior real parts, and the numerical scales for \(H=3\cdot10^{12}\).
