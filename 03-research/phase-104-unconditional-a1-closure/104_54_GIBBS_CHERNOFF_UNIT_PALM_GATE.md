# 104_54 — Gibbs--Chernoff gate for the unitary Palm defect

**Result.** The non-additive front suggested by `104_50` does not admit a
Chernoff bound. For

\[
 f_{n,s}(x)=L_{n-1}^{(1)}(sx),\qquad s>1,                 \tag{1}
\]

let the unitary defect be

\[
 D_{n,s}(N)=
 \sum_{p^{a_p}\parallel N}(\log p)
       \sum_{k=1}^{a_p}f_{n,s}(k\log p)
 -{1-L_n(s\log N)\over s}.                               \tag{2}
\]

Then, for every integer \(n\ge4\), in particular for every
\(n\ge150\),

\[
 \boxed{\mathbb E_s e^{tD_{n,s}}=+\infty
        \quad\hbox{for every }t\in\mathbb R\setminus\{0\}.} \tag{3}
\]

The obstruction is bilateral and arithmetic. On large primes,
\(D_{n,s}\) has sign \((-1)^{n-1}\) and size
\(\asymp(\log p)^n\). On products of two primes with comparable
logarithms it has the opposite sign and the same order. The zeta weight
\(N^{-s}\) only contributes \(-s\log N\) to the logarithm of the term; it
cannot compete with \(c(\log N)^n\).

Reinserting the pole does not change the verdict. The completed variable
from `104_50`,

\[
 Z_{n,s}=D_{n,s}+T_s(f_{n,s}),                              \tag{4}
\]

differs from \(D_{n,s}\) by a finite constant. The same holds when
subtracting the budget \(\kappa A_n/s\),
\(\kappa=1501/2002\). Hence none of the three variables has a nontrivial
exponential moment on either sign.

The Gibbs variational form confirms that this is not a bad choice of
parameter. For \(t\ne0\), delta measures supported on the prime or
semiprime sequences make

\[
 t\,\mathbb E_QD_{n,s}-\mathrm{KL}(Q\|\mathbb P_s)
 \longrightarrow+\infty.                                  \tag{5}
\]

Thus the best entropic bound is literally \(+\infty\). No finite
inequality appears that could be compared with

\[
 B_n\le{1501\over2002}A_n.                                 \tag{6}
\]

The shifted falsifier passes this gate. For
\(Z_c(s)=\zeta(s+c)\zeta(s-c)\), the correct selector coincides
**exactly** with the unitary one on primes and squarefree semiprimes. The
same two sequences prove bilateral divergence of its Gibbs functional,
even though the completed \(\xi(s+c)\xi(s-c)\) has zeros off the critical
line.

The narrow mechanism

```text
unitary Palm defect before centering
+ exponential tilt / Gibbs / Chernoff
+ optimization in t
    => one-sided bound proportional to B_n.
```

is ruled out. A bounded or truncated transformation accompanied by a
uniform arithmetic tail theorem is not ruled out. Such a theorem would
have to control precisely the two sequences that cause (3), and would not
be a consequence of Chernoff. This document does not prove (6), A1 or RH.

## 0. No internal duplication

`104_49` proves that the defect (2) changes sign at degree \(151\).
`104_50` constructs its covariance and shows that the completed square
loses the orientation of the margin. `104_52`--`104_53` prove that
connected cumulants cancel the interactions between distinct towers.

None of those results is counted again here. The addition is the complete
classification of exponential integrability for **every**
\(n\ge4\), the divergence of the variational formula via delta measures,
and the exact transfer of the two witnesses to the shifted divisor.

## 1. Two exact expansions of the defect

Write

\[
 P_n(x)=L_{n-1}^{(1)}(x).
\]

Its leading coefficient is

\[
 P_n(x)={(-1)^{n-1}\over(n-1)!}x^{n-1}+O_n(x^{n-2}).       \tag{7}
\]

The exact antiderivative is

\[
 \int_0^X P_n(sx)\,dx={1-L_n(sX)\over s}.                 \tag{8}
\]

### 1.1. Prime fiber

If \(N=p\) and \(x=\log p\), (2) gives

\[
 D_{n,s}(p)=xP_n(sx)-{1-L_n(sx)\over s}.                   \tag{9}
\]

Comparing the leading coefficients of (7)--(8),

\[
 \boxed{
 D_{n,s}(p)
 ={(-1)^{n-1}s^{n-1}(n-1)\over n!}x^n
 +O_{n,s}(x^{n-1}).}                                      \tag{10}
\]

Hence there exists \(x_0(n,s)\) such that, for every prime
\(p>e^{x_0}\),

\[
 \mathrm{sgn}\,D_{n,s}(p)=(-1)^{n-1},\qquad
 |D_{n,s}(p)|\ge c_{n,s}(\log p)^n                         \tag{11}
\]

with some \(c_{n,s}>0\).

### 1.2. Two-tower fiber

If \(N=pq\), with \(p\ne q\) primes, \(x=\log p\), \(y=\log q\),
the unitary multiplicity produces exactly

\[
 D_{n,s}(pq)=xP_n(sx)+yP_n(sy)
             -{1-L_n(s(x+y))\over s}.                     \tag{12}
\]

Its homogeneous part of degree \(n\) is

\[
 \boxed{
 {(-1)^{n-1}s^{n-1}\over(n-1)!}
 \left\{x^n+y^n-{(x+y)^n\over n}\right\}.}               \tag{13}
\]

For each \(J\ge1\), Bertrand's postulate allows choosing

\[
 2^J<p_J<2^{J+1},\qquad
 2^{J+1}<q_J<2^{J+2}.                                      \tag{14}
\]

The intervals are disjoint and

\[
 {\log p_J\over J\log2}\longrightarrow1,\qquad
 {\log q_J\over J\log2}\longrightarrow1.                \tag{15}
\]

Dividing (13) by \((J\log2)^n\), the bracket converges to

\[
 2-{2^n\over n}<0\qquad(n\ge4).                            \tag{16}
\]

The lower-degree terms vanish. Consequently, for every
\(J\) large enough,

\[
 \mathrm{sgn}\,D_{n,s}(p_Jq_J)=(-1)^n,\qquad
 |D_{n,s}(p_Jq_J)|\ge c'_{n,s}
       \{\log(p_Jq_J)\}^n                                 \tag{17}
\]

with \(c'_{n,s}>0\). Equations (11) and (17) give unbounded tails of
both signs for every \(n\ge4\).

## 2. Complete classification of the exponential moments

The expectation under the zeta law is

\[
 \mathbb E_se^{tD_{n,s}}
 ={1\over\zeta(s)}\sum_{m\ge1}m^{-s}e^{tD_{n,s}(m)}.       \tag{18}
\]

All of its terms are positive. If \(t(-1)^{n-1}>0\), use the prime
sequence of (11). If \(t(-1)^{n-1}<0\), use the semiprime sequence of
(17). In both cases there exists \(m_j\to\infty\) such that

\[
 tD_{n,s}(m_j)-s\log m_j-\log\zeta(s)
 \ge |t|c\{\log m_j\}^n-s\log m_j-\log\zeta(s)
 \longrightarrow+\infty.                                  \tag{19}
\]

The terms of (18) do not even tend to zero along that subsequence.
This proves (3).

In contrast, the ordinary mean exists absolutely. For a constant
\(C_{n,s}\),

\[
 |D_{n,s}(m)|\le C_{n,s}\{1+(\log m)^n\},                 \tag{20}
\]

and \(\sum m^{-s}(\log m)^n<\infty\). Thus the failure of Gibbs does not
come from the linear functional being undefined: it comes from tails
heavier than any exponential linear in \(D_{n,s}\).

Since \(T_s(f_{n,s})\) and \(\kappa A_n/s\) are finite constants,

\[
 \mathbb E_s e^{tZ_{n,s}}
 =e^{tT_s(f_{n,s})}\mathbb E_s e^{tD_{n,s}},               \tag{21}
\]

and the same identity, with another finite factor, holds for
\(Z_{n,s}-\kappa A_n/s\). By (3), both expectations are infinite for
every \(t\ne0\).

## 3. The best variational bound is infinite

The extended Gibbs formula is

\[
 \log\mathbb E_s e^{tD_{n,s}}
 =\sup_{Q\ll\mathbb P_s}
 \left\{t\mathbb E_QD_{n,s}
             -\mathrm{KL}(Q\|\mathbb P_s)\right\}.  \tag{22}
\]

There is no need to import (22) to prove the divergence: its witnesses
are explicit. For \(Q_j=\delta_{m_j}\),

\[
 \mathrm{KL}(Q_j\|\mathbb P_s)
 =s\log m_j+\log\zeta(s).                                  \tag{23}
\]

By (19),

\[
 t\mathbb E_{Q_j}D_{n,s}
 -\mathrm{KL}(Q_j\|\mathbb P_s)\longrightarrow+\infty.
                                                                    \tag{24}
\]

For \(t>0\), the Jensen--Chernoff inequality only yields

\[
 \mathbb E_sD_{n,s}\le{1\over t}
       \log\mathbb E_se^{tD_{n,s}}=+\infty.                \tag{25}
\]

For \(t<0\), the analogous lower bound is equally vacuous. Optimizing in
\(t\) does not help: the effective domain of the log-Laplace transform is
the singleton \(\{0\}\).

## 4. The shifted divisor exactly preserves the witnesses

Let

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c)
       =\sum_{m\ge1}{a_c(m)\over m^s},\qquad 0<c<{1\over2}, \tag{26}
\]

and \(s>1+c\). Its logarithmic weights are

\[
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0.                 \tag{27}
\]

The correct selector is

\[
 J_{f,c}(m)={1\over a_c(m)}\sum_{d\mid m}
       \omega_c(d)a_c(m/d)f(\log d).                       \tag{28}
\]

For a prime \(p\),

\[
 a_c(p)=p^c+p^{-c},\qquad
 \omega_c(p)=(\log p)a_c(p),                               \tag{29}
\]

and therefore

\[
 J_{f,c}(p)=(\log p)f(\log p).                             \tag{30}
\]

If \(p\ne q\) are primes, multiplicativity gives

\[
 a_c(pq)=a_c(p)a_c(q),
\]

while \(\omega_c(pq)=0\). Hence

\[
 \boxed{J_{f,c}(pq)
 = (\log p)f(\log p)+(\log q)f(\log q).}                  \tag{31}
\]

The shifted variables

\[
 D_{n,s,c}(m)=J_{f_{n,s},c}(m)
       -{1-L_n(s\log m)\over s}                            \tag{32}
\]

coincide exactly with (9) and (12) on the two witness sequences.
Moreover, \(a_c(p),a_c(pq)>1\). Thus, under the positive law

\[
 \mathbb P_{s,c}(N=m)={a_c(m)m^{-s}\over Z_c(s)},          \tag{33}
\]

the corresponding terms of
\(\mathbb E_{s,c}e^{tD_{n,s,c}}\) are larger than those of (18), up to a
normalizing constant. The bilateral divergence (3) again holds.

The exact example

\[
 c={\log2\over\log5}\in(0,1/2),                           \tag{34}
\]

may be taken, because \(2<\sqrt5\). The completed
\(\Xi_c(s)=\xi(s+c)\xi(s-c)\) has zeros
\(1/2\pm c+i\gamma\) off the critical line. Hence the failure of Gibbs
integrability is compatible with an off-line system and cannot encode the
Li margin.

## 5. Verdict and successor

The following is proved unconditionally:

1. the two exact signs of the prime and semiprime fibers (10)--(17);
2. the bilateral divergence of all exponential moments (3);
3. the existence of the ordinary mean (20);
4. the explicit divergence of the Gibbs supremum via deltas (23)--(24);
5. the exact stability of the witnesses under the shifted divisor
   (29)--(33).

The following is ruled out:

```text
linear tilt exp(t D_{n,s}) for any t != 0;
one-sided Chernoff in either of the two signs;
Gibbs/Donsker--Varadhan as an automatic generator of coercivity;
regularizing only through the pole or the archimedean budget.
```

The minimal successor, if a variational method is insisted upon, must
truncate or nonlinearly compress \(D_{n,s}\) **and** prove a uniform
signed bound on the truncation error. The present identities do not
supply that bound; removing the truncation brings back the two tails of
(11) and (17).

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 gibbs_chernoff_unit_palm_gate_check.py
```

The checker uses only integers, `Fraction` and rational polynomials. It
verifies the leading coefficients of (10) and (13), the signs of (16), the
exact superlinear dominance for even and odd degrees, and the shifted
local identities (29)--(31). It does not evaluate zeta, A1 or RH.
