# 104_66 — Diagonal regulator–Abel and superexponential cancellation gate

**Result.** The diagonal suggested by `104_64` can indeed be taken
rigorously. If
\[
 q=e^{-h},\qquad \varepsilon(h)=e^{-C/h},                 \tag{1}
\]
then, for an explicit universal \(C>0\), the regulated coefficients
\(\lambda_{n,\varepsilon(h)}\) uniformly approximate \(\lambda_n\) on
the main window \(n\le h^{-1}\). The Abel Fermi average can be written
with that single diagonal regulator.

This does not close RH. Before cancellation, the pole and the prime
channel have size \(\exp(C/h^2)\) for \(n\asymp h^{-1}\), while their
paired difference has size at most \(\exp(O(1/h))\). The phase requires
relative precision \(\exp(-C/h^2+O(1/h))\). Separating the channels is a
quantitative no-go; keeping them together returns exactly the unknown
Fermi observable.

---

## 1. Exact paired generating function

Let
\[
 F(s)=(s-1)\zeta(s),\qquad s=s(z)={1\over1-z},\qquad
 \tau={z\over1-z}=s-1.                                    \tag{2}
\]
With the notation of `104_61`--`104_64`,
\[
 \lambda_{n,\varepsilon}
 =A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\qquad
 Q_{n,\varepsilon}
 =\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).                                   \tag{3}
\]
The exact generating functions of `104_62` combine as
\[
\begin{aligned}
 \sum_{n\ge1}{p_n(\varepsilon)-Q_{n,\varepsilon}\over n}z^n
 &=
 \log\!\left(1+{\tau\over\varepsilon}\right)
 -\log\zeta(1+\varepsilon)
 +\log\zeta(1+\varepsilon+\tau)\\
 &=\log F(s+\varepsilon)-\log F(1+\varepsilon).
\end{aligned}                                             \tag{4}
\]
At \(\varepsilon=0\), the right-hand side is
\(\log F(s)-\log F(1)\). Hence, if
\[
 d_{n,\varepsilon}:=\lambda_{n,\varepsilon}-\lambda_n,
\]
then
\[
 \boxed{\sum_{n\ge1}{d_{n,\varepsilon}\over n}z^n
 =D_\varepsilon(z)
 :=\log{F(s(z)+\varepsilon)\over F(s(z))}
 -\log{F(1+\varepsilon)\over F(1)}.}                       \tag{5}
\]
The branch is normalized by \(D_\varepsilon(0)=0\). This is the
cancellation that disappears when \(p_n\) and \(Q_{n,\varepsilon}\) are
separated.

---

## 2. Uniform zero-free disk under shift

Every nontrivial zero \(\rho=\beta+i\gamma\) satisfies
\(0<\beta<1\) and \(|\gamma|>14\). The second bound is an
unconditional certified input, much weaker than the Platt–Trudgian
verification recorded in `104_00`; no zero is localized here beyond
that range. For \(0\le u\le1/2\), the singular point
of \(F(s+u)\) in the variable \(z\) is
\[
 z_{\rho,u}=1-{1\over\rho-u}.                              \tag{6}
\]
Moreover,
\[
\begin{aligned}
 |z_{\rho,u}|^2
 &=1+{1-2\beta+2u\over(\beta-u)^2+\gamma^2}\\
 &\ge1-{1\over\gamma^2}>{195\over196}.                    \tag{7}
\end{aligned}
\]
If the numerator is negative, use
\((\beta-u)^2+\gamma^2\ge\gamma^2\) and
\(1-2\beta+2u\ge-1\); if it is positive, the bound is immediate.
The trivial zeros \(\rho=-2k\) give
\[
 z_{\rho,u}=1+{1\over2k+u}>1.                              \tag{8}
\]
So, with
\[
 r_0=\sqrt{195\over196},\qquad
 v_0=-\log r_0={1\over2}\log{196\over195}<0.00257,         \tag{9}
\]
the functions \(F(s(z)+u)\) are simultaneously zero-free on
\(|z|<r_0\), for \(0\le u\le1/2\), with no RH assumption.

Fix \(0<r<r_0\). By compactness,
\[
 M_r:=\sup_{\substack{|z|\le r\\0\le u\le1/2}}
 \left|{F'\over F}(s(z)+u)\right|<\infty.                  \tag{10}
\]
The formula
\[
 D_\varepsilon(z)=\int_0^\varepsilon
 \left\{{F'\over F}(s(z)+u)-{F'\over F}(1+u)\right\}du    \tag{11}
\]
gives \(\sup_{|z|\le r}|D_\varepsilon(z)|\le2M_r\varepsilon\).
Cauchy applied to (5) proves
\[
 \boxed{|d_{n,\varepsilon}|
 \le2M_r\,n\,\varepsilon r^{-n}.}                          \tag{12}
\]

---

## 3. Universal choice of the diagonal

For \(n\le B/h\), (12) gives
\[
 \sup_{n\le B/h}|d_{n,\varepsilon(h)}|
 \le {2BM_r\over h}
 \exp\!\left(-{C-B\log(1/r)\over h}\right).                \tag{13}
\]
Hence it suffices to have \(C>Bv_0\) to choose
\(e^{-C/B}<r<r_0\). For the main window \(B=1\), one can take
\[
 \boxed{r={199\over200},\qquad C={1\over100}.}              \tag{14}
\]
Indeed,
\[
 {199\over200}<\sqrt{195\over196},\qquad
 \eta:={1\over100}-\log{200\over199}>0.                    \tag{15}
\]
With
\[
 \varepsilon(h)=\exp\!\left(-{1\over100h}\right),          \tag{16}
\]
which lies in \((0,1/2]\) for all sufficiently small \(h\), one
unconditionally obtains
\[
 \boxed{\sup_{1\le n\le1/h}
 |\lambda_{n,\varepsilon(h)}-\lambda_n|
 \le {2M_{199/200}\over h}e^{-\eta/h}\longrightarrow0.}   \tag{17}
\]
The constant \(M_{199/200}\) is finite over an explicit compact set and
does not depend on \(h\); its numerical value does not affect the limit.

---

## 4. A single diagonal limit for Fermi

Let
\[
 \ell(y)={1\over1+e^y},\qquad b_n=\log(n+1),
\]
and define
\[
 \mathfrak A_{t,\varepsilon}(h)
 ={1\over L(h)}\sum_{n\ge1}{e^{-hn}\over n}
 \ell\!\left(t(\lambda_{n,\varepsilon}+b_n)\right),
 \qquad L(h)=-\log(1-e^{-h}).                              \tag{18}
\]
Since \(|\ell'|\le1/4\), the block \(n\le1/h\) of the difference from
the unregulated average is bounded by \(t/4\) times (17). In the tail
only \(0\le\ell\le1\) is used:
\[
 {1\over L(h)}\sum_{n>1/h}{e^{-hn}\over n}
 \le {1\over L(h)}\int_{1/2}^\infty{e^{-u}\over u}\,du=o(1)
 \qquad(0<h\le1/2).                                       \tag{19}
\]
Hence, for every \(t>0\),
\[
 \boxed{\mathfrak A_t(h)
 -\mathfrak A_{t,\varepsilon(h)}(h)\longrightarrow0.}      \tag{20}
\]
By `104_64`,
\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \liminf_{h\downarrow0}\mathfrak A_{t,\varepsilon(h)}(h)=0.}
 \tag{21}
\]
The right-hand side contains, for each \(h>0\), an absolutely
convergent Euler series and no internal limit in \(\varepsilon\).

---

## 5. Precision wall when separating the channels

The first generating function of (4) gives exactly
\[
\begin{aligned}
 \sum_{n\ge1}{p_n(\varepsilon)\over n}z^n
 &=\log\!\left(1+{\tau\over\varepsilon}\right)\\
 &=\log\!\left(1+{1-\varepsilon\over\varepsilon}z\right)
 -\log(1-z),
\end{aligned}                                             \tag{22}
\]
and hence
\[
 \boxed{p_n(\varepsilon)
 =1+(-1)^{n-1}\left({1-\varepsilon\over\varepsilon}\right)^n.}
 \tag{23}
\]
On the diagonal (16), for \(n\asymp h^{-1}\),
\[
 \log|p_n(\varepsilon(h))|
 ={1\over100h^2}+o(h^{-2}).                                \tag{24}
\]
But (3) is equivalent to
\[
 Q_{n,\varepsilon}
 =p_n(\varepsilon)+A_n-\lambda_{n,\varepsilon}.            \tag{25}
\]
The complete block \(A_n-\lambda_{n,\varepsilon}\) grows like
\(\exp(O(n))\) on the earlier uniform disk, while the two terms that
cancel in (25) have size \(\exp(C/h^2)\). Recovering their
difference requires relative precision
\[
 \boxed{\exp\{-C/h^2+O(1/h)\}.}                            \tag{26}
\]

The unitary version does not change the requirement. The polar factor
contains \(\exp\{istp_n(\varepsilon(h))\}\). Even for the microfrequency
\(s=\exp(-c/h)\) of `104_64`,
\[
 s|p_n(\varepsilon(h))|
 =\exp\{C/h^2-c/h+o(h^{-2})\}\longrightarrow\infty.        \tag{27}
\]
The prime factor has the opposite phase at precision (26). Taking
moduli, total variation, or truncating a phase loses the cancellation.
Multiplying first in exact form gives
\[
 e^{ist(A_n+b_n+p_n-Q_{n,\varepsilon})}
 =e^{ist(\lambda_{n,\varepsilon}+b_n)},                    \tag{28}
\]
the unknown observable of (18). This rules out a separate estimate, not
a new identity for the complete product.

### 5.1 Incompatibility with the VK absolute damping

The regulator also does not make useful the absolute bound discarded in
`103_56`. There, with

\[
 U_n=n^{5/3}(\log n)^{1/3},
\]

the unregulated positive charge satisfies

\[
 \log\mathcal B_n\ge
 {2\over3}n\log n+{1\over3}n\log\log n-O(n).               \tag{28a}
\]

The factor \(m^{-\varepsilon}=e^{-\varepsilon u}\) only subtracts
\(\varepsilon U_n+O(\varepsilon)\) from that exponent over
\([U_n,U_n+1]\). To reduce the absolute charge itself to subexponential
scale would require, at minimum,

\[
 \varepsilon U_n\ge
 {2\over3}n\log n+{1\over3}n\log\log n-O(n),
\]

that is,

\[
 \boxed{\varepsilon\gtrsim
 n^{-2/3}(\log n)^{2/3}.}                                  \tag{28b}
\]

In the window \(n\asymp h^{-1}\), the diagonal that approximates the
coefficients instead uses

\[
 \varepsilon(h)=e^{-C/h}=e^{-Cn},
\]

which is smaller than every power of \(n^{-1}\). Hence no choice
covered by the unconditional uniform guarantee (13) can be
simultaneously:

1. small enough for the uniform approximation obtained via Cauchy; and
2. large enough to repair the VK–Laguerre charge in modulus.

This incompatibility does not affect a signed estimate of the full
product. It does close the possibility that merely keeping
\(\varepsilon>0\) makes the absolute-value argument viable.

---

## 6. The regulator does not erase an off-line mode

If hypothetically \(\rho\) exists with \(\Re\rho>1/2\), set
\[
 u_\rho={\rho\over\rho-1},\qquad |u_\rho|>1.
\]
The shift changes the mode by
\[
 u_{\rho-\varepsilon}
 ={\rho-\varepsilon\over\rho-\varepsilon-1},\qquad
 \log u_{\rho-\varepsilon}-\log u_\rho=O_\rho(\varepsilon).
 \tag{29}
\]
For \(n\le1/h\) and (16),
\[
 n\{\log u_{\rho-\varepsilon(h)}-\log u_\rho\}
 =O_\rho(h^{-1}e^{-1/(100h)})=o(1).                        \tag{30}
\]
The diagonal regulator preserves the exponential amplitude and phase of
the off-line mode. It approximates the criterion: it does not smooth it
into becoming true.

In contrast, the exact first-order expansion is

\[
 \log u_{\rho-\varepsilon}-\log u_\rho
 ={\varepsilon\over\rho(\rho-1)}+O_\rho(\varepsilon^2).
 \tag{31}
\]

With a polynomial damping of size (28b), one has
\(n\varepsilon\to\infty\). Such a regulator alters the dominant mode by
a non-uniform exponential factor and cannot be substituted into the
coefficient-by-coefficient detector. This is the same incompatibility
seen from the zeros instead of from the VK charge.

---

## 7. Verdict

**Proved:** the generating function (5), the shifted disk (7)--(9), the
bound \(2M_rn\varepsilon r^{-n}\), the explicit diagonal (16), the
diagonal Fermi equivalence (20)--(21), and the wall (26).

**Gain:** the Abel front lies entirely within Euler's half-plane of
absolute convergence, with a single regulator tied to \(h\).

**Not proved:** a bound for the complete phase (28), the Fermi limit,
A1, or RH. The diagonal removes a limit-interchange problem, not the
arithmetic cancellation.

---

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 diagonal_abel_regulator_gate_check.py
```

The checker verifies (23) against the binomial sum with rational
arithmetic, the inequalities of (14)--(15), the \(C/h^2\) scale, and the
stability of a shifted exterior mode. The analytic bounds are proved in
the text.
