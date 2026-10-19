# 104_69 — Finite Fermi criterion in \(\log X\) and single Euler diagonal

**Result.** Define

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},\qquad
 \mathfrak F(X)={1\over H_X}\sum_{n\le X}{a_n\over n},
 \qquad H_X=\sum_{n\le X}{1\over n}.                       \tag{1}
\]

Then

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \mathfrak F(X)\longrightarrow0.}                          \tag{2}
\]

Moreover, with

\[
 \varepsilon_X=e^{-X/100},                                \tag{3}
\]

all degrees \(1\le n\le X\) can be replaced simultaneously by their
regulated prime–Laguerre form. The difference between the two averages
tends exponentially to zero, and for each \(X\) a single absolutely
convergent Euler formula remains.

This normalizes the front of 104_61--104_66 in finite form. It
contributes no new upper bound for (1), A1, or RH.

**No internal duplication.** 104_68 uses the same \(a_n\) inside
deterministic windows and keeps the order
\(\varepsilon\downarrow0\) with the window fixed. Here the observable is
the global logarithmic average, and the new contribution is removing
that internal limit via the single regulator \(\varepsilon_X=e^{-X/100}\),
uniform over all degrees \(n\le X\).

---

## 1. Finite logarithmic criterion

The choice \(t=1\), \(b_n=\log(n+1)\) in 104_61 gives exactly

\[
 {1\over1+\exp(\lambda_n+b_n)}
 ={1\over1+(n+1)e^{\lambda_n}}=a_n.                        \tag{4}
\]

**Theorem 1.1.** Equivalence (2) is unconditional.

**Proof.** Under RH, Li gives \(\lambda_n\ge0\), so

\[
 0\le a_n\le{1\over n+2},\qquad
 0\le\sum_{n\le X}{a_n\over n}
 \le\sum_{n\ge1}{1\over n(n+2)}={3\over4}.                \tag{5}
\]

Since \(H_X\to\infty\), \(\mathfrak F(X)\to0\).

If RH is false, 104_56 produces \(c>0\), \(R>1\), and a set \(D\) of
natural density \(d>0\) such that

\[
 \lambda_n\le-cR^n\qquad(n\in D)                           \tag{6}
\]

from some index on. On \(D\),

\[
 (n+1)e^{\lambda_n}\le(n+1)e^{-cR^n}\longrightarrow0,
 \qquad a_n\longrightarrow1.                              \tag{7}
\]

Natural density implies logarithmic density,

\[
 {1\over H_X}\sum_{\substack{n\le X\\n\in D}}{1\over n}
 \longrightarrow d,                                       \tag{8}
\]

and hence

\[
 \liminf_{X\to\infty}\mathfrak F(X)\ge d>0.                \tag{9}
\]

This proves (2) and also

\[
 \boxed{\mathrm {RH}\quad\Longleftrightarrow\quad
 \liminf_{X\to\infty}\mathfrak F(X)=0.}                    \tag{10}
\]
\(\square\)

---

## 2. Simultaneous approximation of the first \(X\) degrees

Use the regularization of 104_66:

\[
\begin{aligned}
 \lambda_{n,\varepsilon}
 &=A_n+p_n(\varepsilon)-Q_{n,\varepsilon},\\
 Q_{n,\varepsilon}
 &=\sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon}}
 L_{n-1}^{(1)}(\log m).
\end{aligned}                                             \tag{11}
\]

The paired generating function and the shifted disk of 104_66 prove,
for

\[
 r={199\over200},\qquad M=M_{199/200}<\infty,
\]

that

\[
 |\lambda_{n,\varepsilon}-\lambda_n|
 \le2Mn\varepsilon r^{-n}
 \qquad(0<\varepsilon\le1/2).                              \tag{12}
\]

Set

\[
 C={1\over100},\qquad
 \eta=C-\log{200\over199}>0.                               \tag{13}
\]

For every integer \(X\ge70\), \(\varepsilon_X\le1/2\). If \(n\le X\),

\[
\begin{aligned}
 |\lambda_{n,\varepsilon_X}-\lambda_n|
 &\le2MXe^{-X/100}\left({200\over199}\right)^X\\
 &=2MXe^{-\eta X}.
\end{aligned}                                             \tag{14}
\]

Thus,

\[
 \boxed{\sup_{1\le n\le X}
 |\lambda_{n,\varepsilon_X}-\lambda_n|
 \le2MXe^{-\eta X}\longrightarrow0.}                      \tag{15}
\]

There is no tail in the degree: a single regulator approximates all
the terms of (1).

---

## 3. Finite diagonal criterion

Define

\[
 a_{n,\varepsilon}
 ={1\over1+(n+1)e^{\lambda_{n,\varepsilon}}},
\qquad
 \mathfrak F_\varepsilon(X)
 ={1\over H_X}\sum_{n\le X}{a_{n,\varepsilon}\over n}.     \tag{16}
\]

The derivative of \(x\mapsto(1+e^x)^{-1}\) has modulus at most \(1/4\).
Using (15),

\[
\begin{aligned}
 |\mathfrak F_{\varepsilon_X}(X)-\mathfrak F(X)|
 &\le {1\over4H_X}\sum_{n\le X}{1\over n}
 |\lambda_{n,\varepsilon_X}-\lambda_n|\\
 &\le {M\over2}Xe^{-\eta X}.
\end{aligned}                                             \tag{17}
\]

**Theorem 3.1 (finite diagonal criterion).**

\[
 \boxed{
 \mathfrak F_{\varepsilon_X}(X)-\mathfrak F(X)\to0,\qquad
 \mathrm {RH}\Longleftrightarrow
 \liminf_{X\to\infty}\mathfrak F_{\varepsilon_X}(X)=0.}    \tag{18}
\]

The exponential constant is explicit; \(M\) is a fixed factor on the
zero-free compact set of 104_66 and does not affect the limit.

---

## 4. A single prime–Laguerre Euler formula

Substituting (11) into (16), for each \(X\ge70\),

\[
\boxed{
\begin{aligned}
 \mathfrak F_{\varepsilon_X}(X)
 ={1\over H_X}\sum_{n\le X}{1\over n}
 \Bigg[1
 &+(n+1)e^{A_n+p_n(\varepsilon_X)}\\
 &\times\prod_{m\ge2}
 \exp\!\left(
 -{\Lambda(m)\over m^{1+\varepsilon_X}}
 L_{n-1}^{(1)}(\log m)\right)
 \Bigg]^{-1}.
\end{aligned}}                                            \tag{19}
\]

Since \(\varepsilon_X>0\),

\[
 \sum_{m\ge2}{\Lambda(m)\over m^{1+\varepsilon_X}}
 |L_{n-1}^{(1)}(\log m)|<\infty\qquad(n\le X).             \tag{20}
\]

The product converges absolutely and the outer sum is finite. The
formula keeps Gamma, pole, primes, and prime powers together until
after forming the logistic. It contains no
\(\varepsilon\downarrow0\) limit. The effective tail of 104_61 allows
truncating it, but does not give a useful uniform bound as
\(X\to\infty\).

---

## 5. Off-line falsifier

For

\[
 Q_n=4-2\mathrm{Re}\,\{(2i)^n+(2i)^{-n}\},            \tag{21}
\]

set \(a_n^Q=[1+(n+1)e^{Q_n}]^{-1}\). Then

\[
\begin{array}{c|c|c}
 n\bmod4&Q_n&a_n^Q\\ \hline
 0&-2^{n+1}+O(1)&1+o(1)\\
 1,3&4&O(1/n)\\
 2&+2^{n+1}+O(1)&o(1).
\end{array}                                                \tag{22}
\]

The errors are summable after multiplying by \(1/n\), while

\[
 \sum_{\substack{n\le X\\4\mid n}}{1\over n}
 ={1\over4}H_{\lfloor X/4\rfloor}
 ={1\over4}H_X+O(1).
\]

Consequently,

\[
 \boxed{{1\over H_X}\sum_{n\le X}{a_n^Q\over n}
 \longrightarrow{1\over4}.}                              \tag{23}
\]

The criterion rejects the off-line divisor. A proof based solely on
absolute convergence, positivity of weights, or unitary moduli cannot
automatically declare that (19) tends to zero.

---

## 6. Cost of separating pole and primes

The exact polar term is

\[
 p_n(\varepsilon)
 =1+(-1)^{n-1}
 \left({1-\varepsilon\over\varepsilon}\right)^n.           \tag{24}
\]

At \(n=X\),

\[
\begin{aligned}
 \log|p_X(\varepsilon_X)-1|
 &=X\log(e^{X/100}-1)\\
 &={X^2\over100}+X\log(1-e^{-X/100})
 ={X^2\over100}+o(1).
\end{aligned}                                             \tag{25}
\]

But

\[
 Q_{n,\varepsilon_X}
 =p_n(\varepsilon_X)+A_n-\lambda_{n,\varepsilon_X}.       \tag{26}
\]

The paired residual grows at most like \(\exp(O(X))\), while the two
separate channels reach \(\exp(X^2/100+o(1))\). Recovering their
difference requires relative precision

\[
 \boxed{\exp\{-X^2/100+O(X)\}.}                            \tag{27}
\]

Taking moduli, truncating one channel, or estimating their phases
separately destroys this precision. Combining them exactly returns
(19). It is a conditioning cost, not a no-go for every future signed
identity.

---

## 7. Verdict

**Proved:** (2)/(10), the uniform approximation (15), the diagonal
criterion (18), the absolute Euler formula (19), the \(1/4\) value of
the quadruple, and the cost (27).

**Gain:** the final formulation needs neither Abel, an infinite outer
sum, nor a regulator limit. For each \(X\) it is finite in the degree
and absolutely convergent arithmetically.

**Not proved:** that (19) tends to zero for the real weights
\(\Lambda(m)\), A1, or RH.

---

## 8. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 finite_logx_diagonal_fermi_check.py
```

The checker verifies the diagonal constant, the polar identity, the
\(1/4\) limit of the quadruple, and the scales (15), (25). The
analytic theorems are proved in the text.
