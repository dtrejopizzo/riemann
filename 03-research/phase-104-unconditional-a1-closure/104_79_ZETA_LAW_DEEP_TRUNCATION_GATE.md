# 104_79 — Completed zeta law and deep truncation gate

**Result.** The prime--pole block of `104_75` has an exact probabilistic
representation that uses the ordinary weights \(\Lambda(m)\) before
taking the logarithm. If

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad
 Y\sim\mathrm{Exp}(s-1),
 \tag{1}
\]

are independent and

\[
 \begin{aligned}
 P_n(u)&=L_{n-1}^{(1)}(u),\\
 J_n(N)&=\sum_{d\mid N}\Lambda(d)P_n(\log d),\\
 U_n(y)&=\int_0^yP_n(u)\,du=1-L_n^{(0)}(y),\\
 Z_{n,s}&=J_n(N)-U_n(Y),
 \end{aligned}                                             \tag{2}
\]

use the normalizations of `104_75`, written here explicitly:

\[
 Q_{n,\varepsilon}=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 P_n(\log m),\qquad
 p_n(\varepsilon)=\int_0^\infty e^{-\varepsilon u}P_n(u)\,du
 =1-\left(1-{1\over\varepsilon}\right)^n.
\]

then, with \(s=1+\varepsilon\),

\[
 \boxed{\mathbb E_s Z_{n,s}=Q_{n,\varepsilon}-p_n(\varepsilon).}
 \tag{3}
\]

This identity keeps all the prime exponents and the pole together.
However, the diagonal

\[
 \varepsilon_X=e^{-X/100},\qquad X/2\le n\le X             \tag{4}
\]

is not uniformly integrable, not even at the extremely permissive
\(e^{\sqrt X}\) level of `104_75`. There exists \(X_0\) such that, for
every integer \(X\ge X_0\) and every integer \(X/2\le n\le X\),

\[
 \boxed{
 \begin{aligned}
 \mathbb E_s\!\left[(Z_{n,s}-e^{\sqrt X})_+\right]
    &\ge e^{X^2/500},\\
 \mathbb E_s\!\left[(-Z_{n,s}-e^{\sqrt X})_+\right]
    &\ge e^{X^2/500}.
 \end{aligned}}                                           \tag{5}
\]

The two bounds are proved over real arithmetic fibers: a prime fiber
gives the sign \((-1)^{n-1}\), and a squarefree semiprime fiber gives the
opposite sign. Their probabilities are only \(\gg\varepsilon_X\) and
\(\gg\varepsilon_X/n\) respectively, but on them
\(|Z_{n,s}|\ge e^{X^2/400}\). Hence a bounded transformation can assign
them mass tending to zero while each one carries an expectation of order
\(e^{cX^2}\).

This closes the narrow attack

```text
represent Q-p as an expectation under independent prime exponents
+ truncate/compress Z at level exp(sqrt(X))
+ control the error via concentration or tail probability
    => deep gate of 104_75.
```

It does not rule out a signed identity that jointly computes the
difference of the two tails up to relative precision \(e^{-cX^2}\). But
that difference is exactly the mean (3); recovering it returns the
prime--pole cancellation that was to be proved. This document does not
prove the deep gate, A1 or RH.

**No internal duplication.** `104_54` proves, for fixed \(n,s\), that the
Palm defect has infinite two-sided exponential moments. The new result
here is diagonal and quantitative: the defect is completed with an
independent polar variable, the exact diagonal of `104_75` is used, and
it is shown that both **first tail moments** above \(e^{\sqrt X}\) grow
like \(e^{cX^2}\), uniformly over a band of degrees of length
proportional to \(X\).

---

## 1. Exact representation before the logarithm

Under (1), for every integer \(d\ge1\),

\[
 \mathbb P_s(d\mid N)
 ={1\over\zeta(s)}\sum_{k\ge1}(dk)^{-s}=d^{-s}.           \tag{6}
\]

The unitary renewal

\[
 \sum_{d\mid m}\Lambda(d)=\log m                         \tag{7}
\]

further guarantees that \(J_n\) is precisely the divisor selector of
`104_43`/`104_49`, with no auxiliary multiplicities. Absolute convergence,
valid because \(s>1\) and \(P_n\) is a polynomial, allows using Fubini
and gives

\[
 \mathbb E_sJ_n(N)
 =\sum_{d\ge2}{\Lambda(d)\over d^s}P_n(\log d)
 =Q_{n,s-1}.                                              \tag{8}
\]

On the other hand,

\[
 \begin{aligned}
 \mathbb EU_n(Y)
 &=\mathbb E\int_0^Y P_n(u)\,du\\
 &=\int_0^\infty e^{-(s-1)u}P_n(u)\,du
 =p_n(s-1).                                               \tag{9}
 \end{aligned}
\]

The last equality is the Laguerre transform used in `104_61` and
`104_75`. Equations (8)--(9) prove (3). In particular, the deep target

\[
 Q_{n,\varepsilon_X}-p_n(\varepsilon_X)
 \ge A_n+\log(n+1)+e^{\sqrt X}                            \tag{10}
\]

is an inequality for the **mean** of \(Z_{n,s}\), not for a tail of its
law.

---

## 2. Two uniform polynomial lemmas

The exact expansion is

\[
 P_n(u)=\sum_{k=1}^n(-1)^{k-1}{n\choose k}{u^{k-1}\over(k-1)!},
 \qquad
 U_n(u)=\sum_{k=1}^n(-1)^{k-1}{n\choose k}{u^k\over k!}.
 \tag{11}
\]

### 2.1 Prime fiber

If \(N=p\), \(x=\log p\) and \(0\le y\le x\), then

\[
 xP_n(x)-U_n(y)
 =\sum_{k=1}^n(-1)^{k-1}{n\choose k}
 {kx^k-y^k\over k!}.                                    \tag{12}
\]

The leading term has sign \((-1)^{n-1}\) and modulus at least
\((n-1)x^n/n!\). The sum of the moduli of the lower terms, divided by
that modulus, is at most

\[
 {n+1\over n-1}
 \sum_{j=1}^{n-1}{(n^2/x)^j\over j!}
 \le2\{e^{n^2/x}-1\}.                                   \tag{13}
\]

Here we used

\[
 {n!{n\choose n-j}\over(n-j)!}
 =\frac{(n!)^2}{j!\{(n-j)!\}^2}
 \le {n^{2j}\over j!}.                                  \tag{14}
\]

Hence, if \(n\ge3\) and \(x\ge8n^2\),

\[
 \boxed{(-1)^{n-1}\{xP_n(x)-U_n(y)\}
 \ge {n-1\over2n!}x^n.}                                 \tag{15}
\]

### 2.2 Semiprime fiber

Let \(N=pq\), \(p\ne q\), \(x=\log p\), \(z=\log q\),
\(w=x+z\), and suppose

\[
 {1\over1.1}\le{x\over z}\le1.1,
 \qquad w\le y\le(1+1/n)w.                              \tag{16}
\]

Then

\[
 xP_n(x)+zP_n(z)-U_n(y)
 =\sum_{k=1}^n(-1)^{k-1}{n\choose k}
 {k(x^k+z^k)-y^k\over k!}.                                \tag{17}
\]

For \(n\ge5\),

\[
 n(x^n+z^n)\le{w^n\over2},                              \tag{18}
\]

because \(\max(x,z)/w\le1.1/2.1=11/21\) and
\(2n(11/21)^n\le1/2\) from \(n=5\) on. Then the leading term of (17)
has sign \((-1)^n\) and modulus at least \(w^n/(2n!)\). Since
\(y^k\le e w^k\), the ratio of the sum of the lower terms to that leading
term is at most

\[
 6n\sum_{j=1}^{n-1}{(n^2/w)^j\over j!}
 \le6n\{e^{n^2/w}-1\}.                                  \tag{19}
\]

Also, \(6n\{e^{1/(100n)}-1\}<1/2\). Thus, for \(n\ge5\) and
\(w\ge100n^3\),

\[
 \boxed{(-1)^n\{xP_n(x)+zP_n(z)-U_n(y)\}
 \ge {w^n\over4n!}.}                                    \tag{20}
\]

The constants 8 and 100 only fix a threshold; on the diagonal (4),
\(x,z\asymp\varepsilon_X^{-1}=e^{X/100}\), so both conditions hold
uniformly for \(n\le X\).

---

## 3. Real mass of the fibers

Set

\[
 L=\varepsilon^{-1},\qquad
 I_\varepsilon=\{p:\ L\le\log p\le1.1L\},
 \qquad
 S_\varepsilon=\sum_{p\in I_\varepsilon}p^{-1-\varepsilon}.
 \tag{21}
\]

The PNT and partial summation give

\[
 S_\varepsilon\longrightarrow
 c_0:=\int_1^{1.1}{e^{-v}\over v}\,dv>0                 \tag{22}
\]

as \(\varepsilon\downarrow0\). Also
\(\zeta(1+\varepsilon)^{-1}\sim\varepsilon\). Hence, for \(\varepsilon\)
small enough,

\[
 \mathbb P_s\{N=p\in I_\varepsilon\}\ge c_1\varepsilon.
 \tag{23}
\]

Since \(Y\) is independent and, on that fiber,
\(\mathbb P(Y\le\log p)\ge1-e^{-1}\), (23) and (15) show that the sign
\((-1)^{n-1}\) occurs with probability at least \(c_2\varepsilon\).

For the semiprime fiber, write

\[
 \sum_{\substack{p<q\\p,q\in I_\varepsilon}}(pq)^{-s}
 ={1\over2}\left\{S_\varepsilon^2-
       \sum_{p\in I_\varepsilon}p^{-2s}\right}
 \ge c_3>0.                                              \tag{24}
\]

The last sum tends to zero because each \(p\ge e^L\). If
\(w=\log(pq)\), then \(2\le\varepsilon w\le2.2\), and

\[
 \begin{aligned}
 \mathbb P\{w\le Y\le(1+1/n)w\}
 &=e^{-\varepsilon w}{1-e^{-\varepsilon w/n}\}\\
 &\ge {c_4\over n}.                                      \tag{25}
 \end{aligned}
\]

From (24)--(25), the fiber with sign \((-1)^n\) has probability at least
\(c_5\varepsilon/n\).

---

## 4. Two-sided blow-up above the deep gate

**Theorem 4.1 (two-sided failure of deep uniformity).** Take (4). For
\(X/2\le n\le X\), elementary Stirling
\(n!\le n^n\) gives, uniformly,

\[
 \log{L^n\over n!}
 \ge n\left({X\over100}-\log X\right)
 \ge {X^2\over400}                                      \tag{26}
\]

from some absolute \(X_0\). On the prime fiber, (15) is at least
\(L^n/n!\) for \(n\ge3\); on the semiprime fiber, (20) is at least
\((2L)^n/(4n!)\ge L^n/n!\). Hence, over the fibers of §§2--3,

\[
 |Z_{n,s}|\ge e^{X^2/400}>e^{\sqrt X}.                   \tag{27}
\]

One of them gives the positive tail and the other the negative tail,
according to the parity of \(n\). Since
\(e^{X^2/400}-e^{\sqrt X}\ge\tfrac12e^{X^2/400}\) for large \(X\),
multiplying the excess above the threshold by the probabilities of
(23)/(25) produces

\[
 {c\varepsilon_X\over n}e^{X^2/400}
 \ge e^{X^2/500}                                        \tag{28}
\]

for large \(X\), which proves both inequalities of (5) simultaneously.

Note the separation of scales:

\[
 \underbrace{\mathbb P(\text{witness fiber})}_{\to0}
 \times
 \underbrace{|Z_{n,s}|}_{\exp(\Theta(X^2))}
 =\underbrace{\text{tail moment}}_{\exp(\Theta(X^2))}.
 \tag{29}
\]

A probability bound, a median, or a bounded compression sees only the
first factor; the exact mean (3) depends on the product and on the
cancellation between the two signs.

---

## 5. Logical scope

For every integrable variable and every \(a>0\),

\[
 \mathbb EZ
 =\mathbb E\mathrm{clip}_{[-a,a]}(Z)
  +\mathbb E(Z-a)_+-\mathbb E(-Z-a)_+,                 \tag{30}
\]

Take \(a=e^{\sqrt X}\). The two excess terms of (30) are, by (5), at
least \(e^{X^2/500}\), while the clipped term has modulus at most
\(e^{\sqrt X}\). Hence an argument that tries to recover the difference
by estimating **separately** both positive terms with uniform relative
errors must reach the scale \(\exp\{-X^2/500+\sqrt X\}\). Truncating them
separately, using absolute value, or replacing them with a bounded
probability does not control that additive error.

This result does not claim that every imaginable bounded transformation
is useless, nor that every joint estimate of the tails requires that
relative precision. It states the precise no-go that has been proved:
the completed zeta law does not satisfy uniformity of first tail moments
at the level of the deep target, so concentration plus a separate
truncation error does not carry (3) over to `104_75`. A successor would
have to supply a signed arithmetic identity that cancels the prime and
semiprime fibers together with all the others; by (3), its output is
again \(Q-p\).

The same test also explains why unit multiplicity does not suffice as an
isolated probabilistic principle. The prime and semiprime fiber formulas
use exactly \(\Lambda(p)=\log p\), but the shifted selector of `104_54`
coincides with them on these two fibers. To distinguish the real zeta,
a global interaction is still needed that does not reduce to
concentration of its independent exponents.

---

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 zeta_law_deep_truncation_check.py
```

The checker uses `Fraction` to verify the expansions (11)--(12)/(17),
the signs of the leading terms, the dominance bounds at rational points
and the scale separation of (26)--(28). The prime mass estimate (22) is
proved analytically via the PNT; it is not replaced by a numerical sum
over astronomically large primes.
