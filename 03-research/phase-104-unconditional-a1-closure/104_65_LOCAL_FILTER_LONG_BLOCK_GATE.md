# 104_65 — Local filter gate and long-block rate detector

**Question.** Can a consecutive, arbitrarily long block be obtained in
which

\[
 \lambda_n\geq-1,                                           \tag{1}
\]

by first controlling moving averages, finite differences, or a local
generating function of the coefficients?

**Verdict.** Not via a fixed finite linear filter. If RH is false,
every filter whose transfer function does not kill the maximal exterior
modes retains exponential negative excursions on a syndetic set. This
includes all fixed-order finite differences and all fixed-length uniform
moving averages. If the filter does kill the mode, it can erase the
falsifier completely: for the quadruple \(w=2i\),
\(E^2+4\) leaves a strictly positive sequence even though the original
is negative at every fourth index.

A bounded **negative exponential rate** detector is also constructed,

\[
 \Psi_{V,n}(x)=\min\!\left\{V,{1\over n}\log\max(1,-x)\right\},
                                                               \tag{2}
\]

whose logarithmic average has lower limit zero if and only if RH. Unlike
the logistics of `104_61`--`104_64`, (2) does not need to resolve a
microfrequency \(e^{-cn}\): it measures the rate \(c\) directly. But its
prime–Laguerre representation keeps the finite-part cancellation
intact; separating pole and primes again costs
\(\log(1/\varepsilon)\).

This document proves a quantitative no-go and an exact coordinate. It
proves neither (1), A1, nor RH.

---

## 1. Logical audit and mandatory falsifier

The correct direction is

\[
 \boxed{
 \text{blocks of (1) of unbounded length}
 \ \Longrightarrow\ \mathrm{RH}.}                          \tag{3}
\]

Under RH, (1) holds on the whole half-line because \(\lambda_n\geq0\). If
RH is false, `104_56`, Theorem 3.1, produces a syndetic set on which
\(\lambda_n\leq-cR^n\), with \(R>1\). So (1) fails at least once in
every sufficiently long interval. The occurrence of the blocks is not a
signature of RH's falsity, but a sufficient criterion for its truth.

Every local mechanism tested here must reject the rational quadruple

\[
 w=2i,\qquad
 Q_n=4-2\mathrm{Re}(w^n+w^{-n}).                    \tag{4}
\]

For \(n\equiv0\pmod4\),

\[
 Q_n=4-2(2^n+2^{-n})<-1\qquad(n\geq4),                    \tag{5}
\]

while in the other three classes \(Q_n\geq4\). So there is no
good block of length four in the tail of (4).

---

## 2. Rigidity theorem under local filters

Let \(E\) be the shift \((Ea)_n=a_{n+1}\), and let

\[
 P(z)=\sum_{h=0}^Jp_hz^h\in\mathbb R[z],\qquad
 (P(E)a)_n=\sum_{h=0}^Jp_ha_{n+h}.                          \tag{6}
\]

Suppose RH is false. Use the dominant decomposition of `104_56` and
group conjugates and multiplicities. There exist \(R>1\),
\(1<R_1<R\), nonzero angles \(\phi_1,\ldots,\phi_K\), multiplicities
\(m_j>0\), and a constant \(C_0\), such that

\[
 \lambda_n=C_0-2R^n\mathrm{Re}
 \sum_{j=1}^Km_je^{in\phi_j}
 +O(n^2R_1^n+n^2).                                          \tag{7}
\]

Here equal characters have been combined; two opposite angles belong to
the same real pair. Set

\[
 u_j=Re^{i\phi_j},\qquad
 F_P(x)=2\mathrm{Re}
 \sum_{j=1}^Km_jP(u_j)e^{ix_j}.                             \tag{8}
\]

Applying (6) to (7) gives exactly

\[
 \boxed{
 (P(E)\lambda)_n=C_0P(1)-R^nF_P(n\phi)
 +O_P(n^2R_1^n+n^2).}                                      \tag{9}
\]

**Theorem 2.1 (filter–mode dichotomy).** One of the following two
alternatives holds:

1. \(P(u_j)=0\) for every maximal exterior mode;
2. there exist \(c_P>0\), \(n_P\) and a syndetic set
   \(D_P\subset\mathbb N\), of positive natural density, such that

   \[
    (P(E)\lambda)_n\leq-c_PR^n
    \qquad(n\in D_P,\ n\geq n_P).                          \tag{10}
   \]

**Proof.** Let

\[
 H=\overline{\{n\phi:n\in\mathbb Z\}}\subset\mathbb T^K.
\]

Distinct characters of a compact group are linearly
independent. Since the conjugates were already grouped, \(F_P\) is
identically zero on \(H\) exactly when all coefficients
\(P(u_j)\) vanish. If not all vanish, \(F_P\) is a nonzero continuous
real function. Each character of (8) is nontrivial —the nontrivial
zeros have nonzero ordinate—, so the Haar integral of
\(F_P\) is zero. Hence \(F_P\) attains some positive value.

Choose \(\eta>0\) such that

\[
 U=\{x\in H:F_P(x)>2\eta\}
\]

is nonempty and its boundary has zero Haar measure. The returns of the
minimal rotation to \(U\) have positive natural density and
form a syndetic set, by the same compact argument of `104_56`, §3. On
that set, (9) and \(R_1<R\) give, after raising the threshold,

\[
 (P(E)\lambda)_n\leq-\eta R^n.
\]

This proves (10), with \(c_P=\eta\). \(\square\)

The first alternative is no gain: the filter has incorporated as
zeros precisely the modes it was supposed to detect. If other exterior
modes remain, the argument is repeated with the next modulus. Killing
them all requires knowing a finite off-line divisor that arithmetic does
not supply.

### 2.1 Differences and moving averages

For a fixed difference of order \(k\),

\[
 P(z)=(z-1)^k.                                               \tag{11}
\]

Its only zero is \(1\), so it does not kill any \(|u_j|>1\). For the
uniform moving average of length \(J+1\),

\[
 P_J(z)={1+z+\cdots+z^J\over J+1}.                          \tag{12}
\]

All its zeros lie on \(|z|=1\), so it also does not kill an exterior
mode. Moreover, if \(|u|=R>1\),

\[
 |P_J(u)|={|u^{J+1}-1|\over(J+1)|u-1|}
 \geq {R^{J+1}-1\over(J+1)(R+1)}.                           \tag{12a}
\]

So a longer window does not dampen the exterior mode: at fixed modulus
it amplifies it exponentially, though it may change its phase.
Theorem 2.1 implies, for each fixed \(k,J\):

\[
\boxed{
\begin{aligned}
 \mathrm {RH}\quad\Longleftrightarrow\quad&
 \Delta^k\lambda_n\geq-e^{\sqrt n}
 \text{ on blocks of unbounded length},\tag{13a}\\
 \mathrm {RH}\quad\Longleftrightarrow\quad&
 {1\over J+1}\sum_{h=0}^J\lambda_{n+h}\geq-1
 \text{ on blocks of unbounded length}.\tag{13b}
\end{aligned}}
\]

Under RH, \(\lambda_n=O(n\log n)\), so every finite combination
\(\Delta^k\lambda_n\) is \(O_k(n\log n)\) and satisfies the
subexponential barrier of (13a). In (13b), RH makes every term
nonnegative. The directions toward RH follow from (10): under non-RH
the filtered excursion of rate \(R^n\) beats \(e^{\sqrt n}\) and any
constant on a syndetic set. The barrier \(-1\) is not set in (13a),
because the positivity of \(\lambda_n\) gives no sign to its finite
differences.

In particular, neither differencing nor averaging reduces the rate
\(R\). It only multiplies its amplitude by \(P(u_j)\).

### 2.2 The generating function keeps the same pole

Let

\[
 G(z)=\sum_{n\geq1}\lambda_nz^n.
\]

Up to a boundary polynomial,

\[
 \sum_{n\geq1}(P(E)\lambda)_nz^n=P(z^{-1})G(z).             \tag{14}
\]

If \(z_0=u_j^{-1}\) is an interior pole produced by a maximal mode, its
residue in (14) gets multiplied by \(P(u_j)\). Hence the radius of
convergence does not improve except by exact cancellation. The Cauchy
bounds for the filtered generating function face the same pole as those
of `104_63`; they do not manufacture the blocks of (1).

---

## 3. An annihilator that bypasses the quadruple

The cancellation alternative is a real failure, not a formality. In (4),
take

\[
 P(z)=z^2+4.                                                 \tag{15}
\]

Since \(P(2i)=P(-2i)=0\), the two exterior modes disappear and

\[
\begin{aligned}
 (P(E)Q)_n
 &=Q_{n+2}+4Q_n\\
 &=20-{15\over2}\mathrm{Re}(w^{-n}).                \tag{16}
\end{aligned}
\]

Hence

\[
 \boxed{(P(E)Q)_n\geq20-{15\over2^{n+1}}>0\qquad(n\geq1),} \tag{17}
\]

even though (5) forbids good blocks of length four for \(Q_n\).

More generally, for any \(P\in\mathbb R[z]\),

\[
 \boxed{
 (P(E)Q)_n=4P(1)-2\mathrm{Re}
 \{w^nP(w)+w^{-n}P(w^{-1})\}.}                              \tag{18}
\]

If \(P(w)\ne0\), one of the four classes mod four makes
\(\mathrm{Re}(i^nP(w))\) positive. On that class, (18) satisfies

\[
 (P(E)Q)_n\leq-c_P2^n                                      \tag{19}
\]

for every sufficiently large \(n\), with

\[
 c_P=\max\{|\mathrm{Re}\,P(2i)|,
             |\mathrm{Im}\,P(2i)|\}>0                 \tag{20}
\]

after reducing the constant by a fixed factor. The set of (19)
has density \(1/4\) and gaps of at most four. If \(P(w)=0\), (16)
shows the filter can end up strictly positive. This is the
quantitative witness of Theorem 2.1's dichotomy.

---

## 4. Logarithmic negative-rate detector

Fix \(V>0\) and define (2). It is a continuous function, bounded between
\(0\) and \(V\), vanishing exactly when \(x\geq-1\). It has the layer
identity

\[
 \boxed{
 \Psi_{V,n}(x)=\int_0^V
 {\bf1}_{\{x<-e^{nv}\}}\,dv.}                              \tag{21}
\]

The pointwise rate \(n^{-1}\log(1+\lambda_n^-)\) already appears in
`104_61`, (9). What is new in this section is only its bounded
truncation, its logarithmic average, and the large-deviation identity
(21); no new zero criterion independent of Bombieri–Lagarias is claimed.

With \(H_X=\sum_{n\leq X}1/n\), set

\[
 \boxed{
 \mathfrak R_V(X)={1\over H_X}
 \sum_{n\leq X}{\Psi_{V,n}(\lambda_n)\over n}.}            \tag{22}
\]

**Theorem 4.1 (logarithmic-rate criterion).** For each \(V>0\),

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak R_V(X)=0.}                 \tag{23}
\]

**Proof.** Under RH, \(\lambda_n\geq0\), so (22) is zero for
all \(X\). If RH is false, `104_56` gives \(R>1\), \(c>0\) and a
syndetic set \(D\) of natural and logarithmic density \(d>0\) such that
\(\lambda_n\leq-cR^n\) on \(D\). Set \(a=\log R\). For \(n\) large
in \(D\),

\[
 {1\over n}\log(-\lambda_n)\geq {a\over2}.
\]

So

\[
 \liminf_{X\to\infty}\mathfrak R_V(X)
 \geq d\min\!\left(V,{a\over2}\right)>0,                  \tag{24}
\]

contradicting the second side of (23). \(\square\)

For the quadruple (4), the three nonnegative classes do not contribute
and

\[
 {1\over n}\log(-Q_n)\longrightarrow\log2
 \qquad(4\mid n).
\]

Hence

\[
 \boxed{
 \mathfrak R_V^{\mathcal O}(X)\longrightarrow
 {1\over4}\min(V,\log2).}                                  \tag{25}
\]

The variable \(v\) of (21) is the diagonal rate of `104_62`, but here
no oscillatory transform is introduced. The statement that would still
need proving is the one-sided large deviation

\[
 {1\over H_X}\sum_{n\leq X}{1\over n}
 {\bf1}_{\{\lambda_n<-e^{nv}\}}\longrightarrow0
 \quad\text{for almost every }v\in(0,V),                    \tag{26}
\]

or directly the integral (22). Theorem 4.1 shows that (26) still
carries RH strength; it does not prove it.

---

## 5. Paired arithmetic form and regulator gate

Use the convention of `104_61`:

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 ={}&A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 ={}&\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m),\\
 \lambda_{n,\varepsilon}&\longrightarrow\lambda_n.
\end{aligned}                                               \tag{27}
\]

Since the outer sum of (22) is finite and \(\Psi_{V,n}\) is continuous,

\[
\boxed{
 \mathfrak R_V(X)=\lim_{\varepsilon\downarrow0}{1\over H_X}
 \sum_{n\leq X}{1\over n}
 \Psi_{V,n}\!\left(A_n+p_n(\varepsilon)
 -\sum_{m\geq2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m)\right).}                             \tag{28}
\]

Formula (28) keeps the pole, archimedean block, primes, and prime
powers together until after applying the detector.

Concavity of the root or of the logarithm does not allow separating
them. For fixed \(n\), `104_63`, (20), gives

\[
\begin{aligned}
 p_n(\varepsilon)
 &=(-1)^{n-1}\varepsilon^{-n}(1+O_n(\varepsilon)),\\
 Q_{n,\varepsilon}
 &=p_n(\varepsilon)+A_n-\lambda_n+o(1).                    \tag{29}
\end{aligned}
\]

Consequently,

\[
 {1\over n}\log(1+|p_n(\varepsilon)|)
 =\log{1\over\varepsilon}+o_n(1),\qquad
 {1\over n}\log(1+|Q_{n,\varepsilon}|)
 =\log{1\over\varepsilon}+o_n(1).                         \tag{30}
\]

The paired term of (28) has a finite limit, but any triangle
inequality applied before pairing introduces a rate that diverges like
\(\log(1/\varepsilon)\). In the root coordinate, the same loss is

\[
 |p_n(\varepsilon)|^{1/n},
 |Q_{n,\varepsilon}|^{1/n}\sim\varepsilon^{-1}.             \tag{31}
\]

This closes the elementary "\(n\)-th root subadditivity" attack. It is
not a no-go for a new inequality applied directly to the finite paired
part of (28).

---

## 6. Balance

**Proved.** The general dichotomy (9)--(10), its specialization to
differences and moving averages, the preservation of the pole in the
generating function, the exact annihilator (16)--(17), the rate
criterion (21)--(24), the off-line value (25), and the regulator gate
(29)--(31).

**Ruled out as a shortcut.** Any fixed number of differences; any
fixed-length moving average; estimating the filtered generating
function instead of the original; or separating the root/logarithm from
the pole and the Mangoldt sum.

**Front that survives.** A large-deviation inequality for the
**paired** finite part of (28), sufficient for (26), or a direct
construction of blocks of (1). Unlike Fermi, detector (22) is already
at the correct exponential scale and pays no microfrequency; unlike an
\(H^2\) energy, it is bounded and one-sided. The arithmetic bound was
not obtained.

**Not proved.** The existence of even one new block for the real
coefficients beyond the certified ranges, the zero limit of (22), A1, or
RH.

---

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 local_filter_long_block_check.py
```

The checker uses `Fraction` and rational Gaussian integers. It verifies
(4)--(5), the filter identity (18), the annihilator (16)--(17), the
absence of exterior zeros of (11)--(12) at the test \(w=2i\), and the
periodic excursions of the non-annihilating filters. Theorem 2.1 and the
logarithmic limits are proved in the text; they are not certified by
sampling.
