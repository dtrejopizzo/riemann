# 104_99 — Exact Eratosthenes, parity identity and energy gate

## Result

Let

\[
 P(z)=\prod_{p\le z}p,
 \qquad
 \Phi(x,z)=\#\{1\le n\le x:(n,P(z))=1\},
 \tag{1}
\]

where \(x\ge2\) is real and the counting functions use
\(n\le\lfloor x\rfloor\). Eratosthenes' inclusion--exclusion gives

\[
 \Phi(x,z)=\sum_{d\mid P(z)}\mu(d)\left\lfloor{x\over d}\right\rfloor.
 \tag{2}
\]

At the natural cutoff \(z=\sqrt x\), the only integers counted are \(1\)
and the primes in \((\sqrt x,x]\). Hence

\[
 \boxed{
 \pi(x)=\pi(\sqrt x)-1+
 \sum_{d\mid P(\sqrt x)}\mu(d)
       \left\lfloor{x\over d}\right\rfloor.}
 \tag{3}
\]

Setting

\[
 V(z)=\prod_{p\le z}\left(1-{1\over p}\right),
 \qquad
 R_E(x,z)=\sum_{d\mid P(z)}\mu(d)
 \left(\left\lfloor{x\over d}\right\rfloor-{x\over d}\right),
 \tag{4}
\]

one obtains the complete signed identity

\[
 \boxed{
 \pi(x)-\mathrm{Li}_2(x)
 =R_E(x,\sqrt x)+xV(\sqrt x)+\pi(\sqrt x)-1
  -\mathrm{Li}_2(x).}
 \tag{5}
\]

No absolute value was taken and the prime-power towers were not split: all the
Eratosthenes correlation remains in \(R_E\). However, (5) does not give
a new estimate. Inserting it into the energy of `104_94`, the missing
bound is exactly

\[
 \sum_{m\le N}{{R_E(m,\sqrt m)+mV(\sqrt m)+\pi(\sqrt m)-1
 -\mathrm{Li}_2(m)}^2\over m(m+1)}=N^{o(1)}.
 \tag{6}
\]

The term \(\pi(\sqrt m)-1\) has finite energy, but the cancellation
between \(R_E(m,\sqrt m)\), \(mV(\sqrt m)\) and
\(\mathrm{Li}_2(m)\) preserves the full content of RH.

There is also an exact identity that localizes the parity barrier within
the complete residue. Let

\[
 \lambda_L(n)=(-1)^{\Omega(n)},
 \qquad
 L(y)=\sum_{n\le y}\lambda_L(n),
 \tag{7}
\]

with \(L(y)=L(\lfloor y\rfloor)\). Then

\[
 \boxed{
 \sum_{d\mid P(\sqrt x)}L(x/d)
 =1+\pi(\sqrt x)-\pi(x).}
 \tag{8}
\]

In particular, again removing the finite-energy block,

\[
 \boxed{
 \mathrm {RH}\Longleftrightarrow
 \sum_{m\le N}{1\over m(m+1)}
 \left\{\mathrm{Li}_2(m)+
 \sum_{d\mid P(\sqrt m)}L(m/d)\right\}^{\!2}=N^{o(1)}.}
 \tag{9}
\]

Equivalence (9) is not a proof of its right-hand side. It exposes what must
cancel in a proof by Eratosthenes: the **complete** sum, up to
level \(d\asymp x\), of the Liouville primitives.

Finally, every stable truncation at level
\(D\le x^{1-\eta}\), with \(\eta>0\) fixed, is ruled out by a
quantitative falsifier. The two nonnegative sequences

\[
 a_n^+=1+\lambda_L(n),
 \qquad
 a_n^-=1-\lambda_L(n)
 \tag{10}
\]

have divisibility data indistinguishable to any power of
\(1/\log x\) at that level, but their sifted masses at \(z=\sqrt x\)
differ at scale \(x/\log x\). Thus, Brun, Selberg or a linear
inclusion--exclusion whose coefficients grow at most as a
power of \(\log x\) cannot produce (6) from truncated data.

This document proves an **incomplete-level-of-distribution no-go** and
the exact reduction (8)--(9). It does not prove that a global identity
specific to the ordinary primes is impossible. Nor does it prove (6),
Deep-\(\Lambda\), A1 nor RH.

---

## 1. Eratosthenes without loss of correlation

For each \(n\),

\[
 {\mathbf 1}_{(n,P(z))=1}=\sum_{d\mid(n,P(z))}\mu(d).
 \tag{11}
\]

Summing (11) for \(1\le n\le x\) proves (2), with finite sums. If
\(z=\sqrt x\) and \(1<n\le x\) is composite, it has a prime divisor
\(p\le\sqrt n\le\sqrt x\), and is therefore not counted by \(\Phi\). If it is
prime and exceeds \(\sqrt x\), it is counted. Hence

\[
 \Phi(x,\sqrt x)=1+\pi(x)-\pi(\sqrt x),
 \tag{12}
\]

which, together with (2), proves (3).

Splitting (2) into floor and continuous term,

\[
 \sum_{d\mid P(z)}{\mu(d)\over d}=V(z),
 \qquad
 \Phi(x,z)=xV(z)+R_E(x,z).
 \tag{13}
\]

Equations (12)--(13) prove (5). It is important not to estimate
\(R_E\) term by term: the bound

\[
 |R_E(x,\sqrt x)|\le 2^{\pi(\sqrt x)}
 \tag{14}
\]

destroys exactly the cancellation being sought. Mertens alone is also
not enough: \(xV(\sqrt x)\sim2e^{-\gamma}x/\log x\), so the residue must
already cancel a term of order \(x/\log x\) before one sees the
critical-scale fluctuation.

## 2. Exact parity identity

Consider the divisibility data from (10),

\[
 A_d^\pm(x)=\sum_{\substack{n\le x\\d\mid n}}a_n^\pm.
 \tag{15}
\]

The Liouville function is completely multiplicative, and therefore

\[
 \boxed{
 A_d^\pm(x)=\left\lfloor{x\over d}\right\rfloor
 \pm\lambda_L(d)L(x/d).}
 \tag{16}
\]

Now sift both sequences with all primes \(p\le\sqrt x\):

\[
 S^\pm(x)=\sum_{\substack{n\le x\\(n,P(\sqrt x))=1}}a_n^\pm.
 \tag{17}
\]

By (12), only \(1\) and the primes greater than \(\sqrt x\) survive. Since

\[
 a_1^+=2,\quad a_1^-=0,\qquad
 a_p^+=0,\quad a_p^-=2,
 \tag{18}
\]

one has exactly

\[
 S^+(x)=2,\qquad
 S^-(x)=2\{\pi(x)-\pi(\sqrt x)\}.
 \tag{19}
\]

On the other hand, inclusion--exclusion and (16) give

\[
\begin{aligned}
 S^-(x)-S^+(x)
 &=\sum_{d\mid P(\sqrt x)}\mu(d)
       \{A_d^-(x)-A_d^+(x)\}\\
 &=-2\sum_{d\mid P(\sqrt x)}
       \mu(d)\lambda_L(d)L(x/d).
\end{aligned}
 \tag{20}
\]

Every divisor of \(P(\sqrt x)\) is squarefree, so
\(\lambda_L(d)=\mu(d)\) and \(\mu(d)\lambda_L(d)=1\). Comparing
(19) and (20) proves (8).

This is the exact location of parity: the Möbius signs of
Eratosthenes are absorbed by the Liouville signs and leave a
global sum with no coefficients. Truncating it before the full level loses
the mass that distinguishes (19).

## 3. Translation into the ordinary energy

Define

\[
 T_m=\sum_{d\mid P(\sqrt m)}L(m/d),
 \qquad H_m=1+\pi(\sqrt m).
 \tag{21}
\]

Identity (8) is equivalent to

\[
 \pi(m)-\mathrm{Li}_2(m)
 =H_m-\{T_m+\mathrm{Li}_2(m)\}.
 \tag{22}
\]

The elementary Chebyshev bound gives

\[
 H_m\ll1+{\sqrt m\over\log(2m)}.
 \tag{23}
\]

Consequently

\[
 \sum_{m=2}^\infty{H_m^2\over m(m+1)}<\infty.
 \tag{24}
\]

The triangle inequality in the Hilbert space with weights
\(1/[m(m+1)]\) shows that adding or removing \(H\) preserves both bounded
energy and \(N^{o(1)}\) growth. Equivalence (9) follows from
`104_93` and `104_94`.

Note that (8) has not gained an inequality: inserted into (22), it recovers
exactly \(\pi(m)\). Its usefulness is adversarial: any proof that
declares \(T_m+\mathrm{Li}_2(m)\) small must exhibit a
global cancellation among all the \(L(m/d)\), not a bound on each one.

## 4. Quantitative gate for every subcomplete level

Fix \(0<\eta<1\) and \(D=x^{1-\eta}\). The classical zero-free
region applied to

\[
 \sum_{n\ge1}{\lambda_L(n)\over n^s}
 ={\zeta(2s)\over\zeta(s)}
 \tag{25}
\]

gives, unconditionally, for every \(A>0\),

\[
 |L(y)|\ll_A {y\over(\log y)^A}.
 \tag{26}
\]

Only this weak consequence of the effective Vinogradov--Korobov-type
bound is needed. For \(d\le D\), \(x/d\ge x^\eta\); using (16),

\[
\begin{aligned}
 \sum_{d\le D}|A_d^+(x)-A_d^-(x)|
 &\le2\sum_{d\le D}|L(x/d)|\\
 &\ll_{A,\eta}{x\over(\log x)^A}
                  \sum_{d\le D}{1\over d}\\
 &\ll_{A,\eta}{x\over(\log x)^{A-1}}.
\end{aligned}
 \tag{27}
\]

In particular, the left-hand side is
\(O_{B,\eta}(x/\log^B x)\) for every \(B>0\). But PNT and (19) give

\[
 S^-(x)-S^+(x)
 =2\{\pi(x)-\pi(\sqrt x)-1\}
 \sim {2x\over\log x}.
 \tag{28}
\]

From this follows the following precise statement.

**Non-distinction theorem.** There is no family of linear forms

\[
 \mathcal F_x(A)=\sum_{d\le x^{1-\eta}}c_d(x)A_d,
 \qquad |c_d(x)|\le(\log x)^K,
 \tag{29}
\]

that approximates \(S(A,\sqrt x)\) with error \(o(x/\log x)\), uniformly
for every nonnegative sequence \(A=(a_n)\). Indeed, (27) with
\(B>K+2\) would give

\[
 |\mathcal F_x(A^+)-\mathcal F_x(A^-)|=o(x/\log x),
 \tag{30}
\]

contradicting (28). The same argument covers any uniformly
Lipschitz functional, with constant \(O((\log x)^K)\), for the
\(\ell^1\) norm of the data \((A_d)_{d\le D}\).

This includes the linear truncations of inclusion--exclusion and the
stable outputs of Brun/Selberg supported at that level. It does not include the
exact sum (2), which uses data up to \(d\asymp x\). Precisely there,
\(x/d\) can be \(O(1)\), (27) stops being small and the parity
information reappears.

## 5. Verdict

The Eratosthenes attack produces two exact results:

1. the sought energy turns into (6), preserving the entire
   signed sum;
2. identity (8) shows that this complete sum is a Liouville
   cancellation, and (27)--(30) rule out all its stable truncations at
   level \(x^{1-\eta}\).

No technical Bonferroni error remains nor a constant to optimize.
To advance from this coordinate, a global inequality is needed that
uses the divisors \(d\) up to scale \(x\) and that is specific to
the ordinary weights. Proving it would amount to proving (9), and hence RH.

## 6. No-duplication audit

`No-go NG-A4` from the initial phases and from the *obstruction ledger* deals
with the impossibility of separating classes of \(\omega(n)\bmod2\) via a
standard sieve. It does not contain (8), does not work with the Cramér
energy and does not quantify the level \(x^{1-\eta}\). `104_94` uses Möbius
inversion between prime powers and ordinary primes, but it also does not use the pair
\(1\pm\lambda_L\). The additional content here is:

* the complete Eratosthenes identity (5) in the exact norm of
  `104_93`;
* the coefficient-free parity identity (8);
* the energy equivalence (9);
* the quantitative falsifier (27)--(30) for every fixed
  subcomplete level.

The general parity barrier of sieve theory is not claimed as new here.
What is new within the project is its exact localization within the
observable one is trying to bound.

## 7. Reproduction

From `tools/`:

```bash
python3 eratosthenes_parity_energy_gate_check.py
```

The checker verifies, with integers and exact fractions, (2)--(5),
(8), (16), (19)--(20) for all integers \(2\le x\le300\). It also
shows in a table the separation of the sifted mass and the concentration
of the divisibility-data difference as it approaches the complete level.
The asymptotic part (26)--(30) is the analytic argument above, not a
numerical inference.
