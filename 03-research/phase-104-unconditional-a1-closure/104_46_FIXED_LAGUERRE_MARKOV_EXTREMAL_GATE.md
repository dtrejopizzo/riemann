# 104_46 — The fixed Laguerre vector is nearly extremal for the divisor transport

**Status.** The exact possibility `104_44` had left open was attacked: a
gap of the divisor operator not over every vector, but only over

\[
 f_{n,s}(d)=L_{n-1}^{(1)}(s\log d),\qquad s>1,
\tag{1}
\]

after removing its von Mangoldt mean. The result is negative and stronger
than the operator gate of `104_44`. For every \(s>1\) sufficiently close
to \(1\), sequence (1) is itself nearly extremal:

\[
 \boxed{
 {\|\mathsf T_s(f_{n,s}-\mathbb E_{\nu_s}f_{n,s})\|_{L^2(\Pi_s)}^2
  \over
  \|f_{n,s}-\mathbb E_{\nu_s}f_{n,s}\|_{L^2(\nu_s)}^2}
 \longrightarrow1.}
\tag{2}
\]

The reason is not a fixed exceptional prime. Under the quadratic measure
of the degree-\((n-1)\) polynomial, the von Mangoldt divisor is, with
asymptotic probability one, a huge prime; multiplied by a fixed zeta
cofactor, that prime remains recoverable as the largest prime factor of
the product. The conditional expectation then loses only an \(o(1)\)
proportion of the exact vector's energy.

The continuous pole–Gamma comparator does the opposite. For the same
unscaled polynomial, its centered ratio tends to zero. Hence there is no
transfer of Gamma coercivity to the arithmetic channel, not even on the
single ray of interest. Moreover, both centered ratios are blind to the
signed mean difference equal to \(B_n=A_n-\lambda_n\). This rules out the
mechanism

> "prove non-alignment of the Laguerre vector via the Markov transport
> and compare it with the Gamma contraction."

Not ruled out is a signed linear identity that directly estimates the
means. Such an identity would be precisely the new, still-missing,
one-sided arithmetic theorem. Neither \(B_n\le(1501/2002)A_n\), A1, nor
RH is proved.

## 1. Binding audit

`104_28` identifies the Li test with the Laguerre prefix
\(g_n=\sum_{j<n}\phi_j\), but proves that non-alignment in an interior
operator does not automatically transfer to the boundary. `104_30` builds
a positive flag reference evaluating \(A_n\), although its row estimate
again requires the signed second differences of \(A_n-\lambda_n\).
`104_42` allows every degree-dependent positive preconditioner and proves
that its optimum is the modulus of the moment one wanted to bound.
Finally, `104_44` builds the canonical transport associated with
\(\Lambda*1=\log\), proves that its zero-mean norm is one via
\(e_p\), and explicitly leaves open a gap for vector (1).

This document closes only that last opening. It uses no triangular degree
sum, does not rescale the polynomial, and does not separate primes from
prime powers in the final identity. The split by exponents is used only
to prove the asymptotic near-extremality theorem.

## 2. Transport and specific ratio

With the notation of `104_44`,

\[
 \mathcal L_s=-{\zeta'(s)\over\zeta(s)},\qquad
 \nu_s(d)={\Lambda(d)d^{-s}\over\mathcal L_s},\qquad
 \Pi_s(N)={ (\log N)N^{-s}\over-\zeta'(s)},
\tag{3}
\]

and

\[
 (\mathsf T_sh)(N)={1\over\log N}
       \sum_{d\mid N}\Lambda(d)h(d).
\tag{4}
\]

Let \(r=n-1\),

\[
 F_r(x)=L_r^{(1)}(sx),\qquad
 \mu_{r,s}=\mathbb E_{\nu_s}F_r(\log D),\qquad
 \widetilde F_r=F_r-\mu_{r,s}.
\tag{5}
\]

Define

\[
 Q_r(s)={\|\mathsf T_s\widetilde F_r\|_{L^2(\Pi_s)}^2
              \over
              \|\widetilde F_r\|_{L^2(\nu_s)}^2}.
\tag{6}
\]

Jensen gives \(0\le Q_r(s)\le1\). The point is that the upper extreme is
indeed asymptotically attained on (5).

## 3. Prime saddle lemma

The following form of the lemma suffices. The interval of \(s\) need not
be optimized: the Phase 104 argument later takes \(s\downarrow1\).

**Lemma 3.1 (prime-exponent domination).** There exists \(s_0>1\) such
that, for each \(s\in(1,s_0)\), as \(r\to\infty\),

\[
 \begin{aligned}
 \mathcal L_s\,\mathrm{Var}_{\nu_s}(F_r)
 &=(1+o_s(1))M_r,\\
 M_r&:=\sum_{p\ \mathrm{prime}}{\log p\over p^s}
             \bigl(F_r(\log p)-\mu_{r,s}\bigr)^2,
 \end{aligned}
\tag{7}
\]

and the probability measure proportional to the summands of \(M_r\)
escapes to infinity. More precisely, for each \(R>0\),

\[
 {1\over M_r}\sum_{\substack{p\ \mathrm{prime}\\\log p\le R}}
 {\log p\over p^s}
 \bigl(F_r(\log p)-\mu_{r,s}\bigr)^2\longrightarrow0.
\tag{8}
\]

For every finite set of integers \(k\), uniformly over that set,

\[
\begin{aligned}
 &\sum_{p>K}{(\log p+\log k)\over p^s}
 \left[
 {\log p\,F_r(\log p)+C_{r,k}\over\log p+\log k}
 -\mu_{r,s}\right]^2\\
 &\hspace{35mm}=(1+o_s(1))M_r,
 \qquad
 C_{r,k}:=\sum_{d\mid k}\Lambda(d)F_r(\log d).
\end{aligned}
\tag{9}
\]

**Proof.** The scaling details are given because they are precisely what
prevents using the continuous comparator. For \(c>0\), set

\[
 I_r(c)=\int_0^\infty e^{-cx}F_r(x)^2\,dx,
 \qquad \beta={s\over c}.
\tag{10}
\]

Laguerre dilation and
\(L_r^{(1)}=\sum_{k=0}^rL_k\) produce the exact expansion

\[
 F_r(x)=\sum_{j=0}^r a_{rj}(\beta)L_j(cx),
\tag{11}
\]

with

\[
 \sum_{r\ge j}a_{rj}(\beta)z^r
 ={\beta^jz^j\over
   (1-z)(1+(\beta-1)z)^{j+1}}.
\tag{12}
\]

By ordinary orthogonality,

\[
 \boxed{cI_r(c)=\sum_{j=0}^ra_{rj}(\beta)^2.}
\tag{13}
\]

The binomial sums of (12), or equivalently Parseval applied to (11),
give

\[
 \lim_{r\to\infty}I_r(c)^{1/(2r)}
 =2\beta-1={2s-c\over c}.
\tag{14}
\]

For clarity, the upper bound comes from
\(\sum_j|a_{rj}|\le C_\beta(2\beta-1)^r\). When \(\beta>2\), the
coefficients alternate in sign \((-1)^{r-j}\) and

\[
 \sum_j|a_{rj}|=
 { (2\beta-1)^{r+1}+(-1)^r\over2\beta};
\tag{15}
\]

then \(\|a_r\|_1/\sqrt{r+1}\le\|a_r\|_2\le\|a_r\|_1\) also gives the lower
bound. This suffices for exponent \(a=1\); for \(a\ge2\) only the upper
bound is needed.

Transfer to primes requires uniformity because the saddle moves with
\(r\). We detail it. For \(a\ge1\), set

\[
 S_{r,a}:=\sum_p{\log p\over p^{as}}F_r(a\log p)^2.
\tag{16}
\]

With \(x=a\log p\), its Stieltjes form is

\[
 S_{r,a}=\int_0^\infty e^{-sx}F_r(x)^2
                 \,d\vartheta(e^{x/a}),
\qquad
 {1\over a}I_r\!\left(s-{1\over a}\right)
 =\int_0^\infty e^{-sx}F_r(x)^2\,d(e^{x/a}).
\tag{16a}
\]

Let \(c_a=s-1/a>0\). The probability measure with density proportional to
\(e^{-c_ax}F_r(x)^2\) concentrates on a moving interval
\([\delta_ar,C_ar]\). This follows with no pointwise Laguerre asymptotic:
for \(0<t<c_a\), Markov's inequality applied to \(e^{\pm t x}\), (10) and
(14) give

\[
 \begin{aligned}
 \Pr(x\le\delta r)&\le e^{t\delta r}{I_r(c_a+t)\over I_r(c_a)},\\
 \Pr(x\ge Cr)&\le e^{-tCr}{I_r(c_a-t)\over I_r(c_a)}.
 \end{aligned}
\tag{16b}
\]

First \(t\) is fixed, and then small \(\delta_a>0\) and large
\(C_a<\infty\); (14) makes both sides \(O(e^{-\eta_ar})\). On that
interval \(x/a\asymp r\) for each fixed \(a\). The effective PNT form

\[
 \vartheta(e^u)=e^u+O\!\left(e^u
 e^{-c_0u^{3/5}(\log u)^{-1/5}}\right)
\tag{16c}
\]

is therefore uniform over the whole saddle: its relative error is
\(O(e^{-c_ar^{3/5}(\log r)^{-1/5}})\). To convert this into a uniform
statement about the weight, subdivide
\([\delta_ar,C_ar]\) into intervals of length \(h_r=r^{-A}\). For fixed
\(A\), (16c) gives, uniformly over every such cell,

\[
 \vartheta(e^{(x+h_r)/a})-\vartheta(e^{x/a})
 ={e^{x/a}h_r\over a}\,(1+o_{s,a}(1)),
\tag{16d}
\]

because the error of (16c), divided by \(h_r\), still tends to zero. No
pointwise bound on the polynomial is needed. Differentiating (11) and
using \((L_j)'=-\sum_{k<j}L_k\), the differentiation matrix in the
orthogonal basis has prefix sums; Cauchy gives

\[
 \int_0^\infty e^{-c_ax}|F_r'(x)|^2dx
 \le c_a^2r^2 I_r(c_a).
\tag{16e}
\]

Another application of Cauchy–Schwarz then gives

\[
 \int_{\delta_ar}^{C_ar}
 \left|{d\over dx}\{e^{-c_ax}F_r(x)^2\}\right|dx
 \le(c_a+2c_ar)I_r(c_a).
\tag{16f}
\]

Take, e.g., \(A=4\). The upper and lower Darboux sums then differ by
\(o(I_r(c_a))\), and (16d) turns either of them into the leading
integral. Both tails are already
\(O(e^{-\eta_ar})I_r(c_a)\): for the prime measure this follows from
\(\vartheta(y)\le Cy\), integration by parts, and (16e), applying (16b)
to both \(F_r\) and its derivative (which has degree \(r-1\) and the same
linear localization). Hence, for every fixed \(a\),

\[
 S_{r,a}={1+o_{s,a}(1)\over a}
 I_r\!\left(s-{1\over a}\right).
\tag{16g}
\]

By (14), this gives

\[
 \lim_{r\to\infty}S_{r,a}^{1/(2r)}
 ={as+1\over as-1},
\tag{17}
\]

for each fixed \(a\); only this equality for \(a=1\) will be used.
The same argument, or (16b) with fixed \(R\), proves (8). No uniformity
in \(s\) is required.

No limit is now interchanged with the infinite sum over \(a\). To handle
all the higher powers simultaneously, define

\[
 \Theta_{\ge2}(e^X)
 :=\sum_{\substack{p^a\le e^X\\a\ge2}}\log p.
\tag{17a}
\]

Chebyshev's bound \(\vartheta(y)\le C y\) gives

\[
 \Theta_{\ge2}(e^X)
 \le C e^{X/2}+C\sum_{3\le a\le X/\log2}e^{X/a}
 \le C' e^{X/2}.
\tag{17b}
\]

Integration by parts, (16e), and (17b) imply, uniformly,

\[
 \sum_{a\ge2}S_{r,a}
 \le C_s(1+r)I_r\!\left(s-{1\over2}\right).
\tag{17c}
\]

The base of (14) strictly decreases with \(c\). Comparing (17c) with
(16g) for \(a=1\), one obtains, with no need for extra uniformity,

\[
 \sum_{a\ge2}S_{r,a}=o_s(S_{r,1}).
\tag{18}
\]

So (18) covers every prime power at once, not a truncation.

It remains to remove the mean. Its exact generating function is

\[
 \sum_{r\ge0}z^r
 \sum_{m\ge2}{\Lambda(m)\over m^s}F_r(\log m)
 ={1\over(1-z)^2}\,
 \mathcal L\!\left({s\over1-z}\right).
\tag{19}
\]

For \(s\) sufficiently close to one, the pole of \(\mathcal L\) at
\(1\), corresponding to \(z=1-s\), is the singularity closest to the
origin. Consequently,

\[
 |\mu_{r,s}|^2=o_s(S_{r,1}).
\tag{20}
\]

The separation of bases can also be seen in the leading model:

\[
 \int_0^\infty e^{-(s-1)x}F_r(x)\,dx
 ={1\over s}\left\{1+{(-1)^r\over(s-1)^{r+1}}\right\},
\tag{21}
\]

while (14) has base \((s+1)/(s-1)\). The remaining singularities of (19)
are at fixed distance from the pole and do not alter (20) after
shrinking \(s_0\), if necessary.

Equations (18)–(20) prove (7). For (9), write
\(x=\log p,c=\log k\). When \(p>K\),

\[
 (\mathsf T_sF_r)(pk)
 ={xF_r(x)+C_{r,k}\over x+c}.
\tag{22}
\]

After subtracting \(\mu_{r,s}\), the numerator is

\[
 x(F_r(x)-\mu_{r,s})+C_{r,k}-c\mu_{r,s}.
\tag{23}
\]

By (8), \(x/(x+c)\to1\) in the quadratic prime measure. For fixed
\(k\), the classical bound
\(|L_r^{(1)}(y)|\le(r+1)e^{y/2}\) shows that
\(C_{r,k}=O_{s,k}(r)\); (20) and Cauchy eliminate the last two terms of
(23). This proves (9). \(\square\)

## 4. The fixed vector attains norm one

**Theorem 4.1 (Laguerre near-extremality).** For each
\(s\in(1,s_0)\),

\[
 \boxed{\lim_{r\to\infty}Q_r(s)=1.}
\tag{24}
\]

**Proof.** Fix \(K\). The integers

\[
 N=pk,\qquad 1\le k\le K,\quad p>K\text{ prime},
\tag{25}
\]

have a unique representation of this form: \(p\) is the only prime factor
of \(N\) greater than \(K\). Restricting the output norm to states
(25), using (9), and \(-\zeta'(s)=\mathcal L_s\zeta(s)\), one obtains

\[
 \begin{aligned}
 \|\mathsf T_s\widetilde F_r\|_{L^2(\Pi_s)}^2
 &\ge {1+o_s(1)\over\mathcal L_s\zeta(s)}
       \sum_{k=1}^K{k^{-s}}M_r.
 \end{aligned}
\tag{26}
\]

By (7),

\[
 \liminf_{r\to\infty}Q_r(s)
 \ge {\sum_{k=1}^Kk^{-s}\over\zeta(s)}.
\tag{27}
\]

Letting \(K\to\infty\), the right-hand side tends to one. Jensen gives
the upper bound one. \(\square\)

This is an obstruction on the real vector, not on artificial test
functions. It also quantifies the mechanism: for every \(K\), the
asymptotic defect is at most the zeta mass of the cofactors \(k>K\);
there is no positive constant uniform in the degree.

## 5. The Gamma comparator behaves oppositely

Let \(\varepsilon=s-1\), \(X\sim\mathrm{Exp}(\varepsilon)\),
\(U\sim\Gamma(2,\varepsilon)\), and

\[
 (\mathsf C_\varepsilon h)(u)={1\over u}\int_0^u h(x)\,dx.
\tag{28}
\]

Set \(\beta=s/\varepsilon\) and use the coefficients (12) with
\(c=\varepsilon\). Since

\[
 F_r(x)=\sum_{j=0}^ra_{rj}(\beta)L_j(\varepsilon x),
\tag{29}
\]

the constant \(a_{r0}\) is exactly the mean. The identities

\[
 \mathsf C_\varepsilon L_j(\varepsilon x)
 ={1\over j+1}L_j^{(1)}(\varepsilon u)
\tag{30}
\]

and the two orthogonalities give the exact ratio

\[
 \boxed{
 Q_r^\Gamma(s)
 ={\displaystyle\sum_{j=1}^r{a_{rj}(\beta)^2\over j+1}
   \over
   \displaystyle\sum_{j=1}^ra_{rj}(\beta)^2}.}
\tag{31}
\]

For every fixed \(J\), (12) implies

\[
 {\sum_{j=1}^Ja_{rj}(\beta)^2
  \over\sum_{j=1}^ra_{rj}(\beta)^2}\longrightarrow0;
\tag{32}
\]

the denominator contains \(a_{rr}^2=\beta^{2r}\), while each fixed index
has strictly smaller base than \(\beta\). Splitting (31) into
\(j\le J\) and \(j>J\), and then letting \(J\to\infty\), one obtains

\[
 \boxed{Q_r^\Gamma(s)\longrightarrow0.}
\tag{33}
\]

So the continuum's coercivity not only fails to transfer: the continuous
ratio tends to zero while the arithmetic one tends to one.

## 6. The signed difference lives in the means, not in the ratios

The complete combination of `104_44` is

\[
 \mathcal B_{n,s}
 =s\left\{\mathcal L_s\,\mathbb E_{\nu_s}f_{n,s}
 -{1\over\varepsilon}\mathbb E_{\mathrm{Exp}(\varepsilon)}f_{n,s}
 \right\},
 \qquad
 \lim_{s\downarrow1}\mathcal B_{n,s}=B_n.
\tag{34}
\]

Ratios (6) and (31) only see the vectors after separately removing those
two means. There is an algebraic proof that they do not contain the sign
of (34). For any real constant \(c\),

\[
 Q_r(s;F_r+c)=Q_r(s;F_r),\qquad
 Q_r^\Gamma(s;F_r+c)=Q_r^\Gamma(s;F_r),
\tag{35}
\]

but

\[
 \boxed{
 \mathcal B_s[F_r+c]-\mathcal B_s[F_r]
 =sc\left(\mathcal L_s-{1\over\varepsilon}\right).}
\tag{36}
\]

The factor in parentheses is nonzero and tends to \(-\gamma\). Hence the
two ratios can remain identical while the signed form crosses any
threshold as \(c\) varies. For the real polynomial \(c\) is fixed, but
recovering it is not enough: the remaining arithmetic mean in (34) is
exactly the one-sided moment that was to be proved. Recentering has
eliminated it, not estimated it.

## 7. Off-line falsifier

The argument of Sections 3–6 uses the real Euler factorization; it does
not automatically apply to a prescribed divisor of zeros. The relevant
gate appears when attempting to continue (34) to the boundary while
forgetting residues. For the quartet with \(e^\alpha=2\) and
\(\theta=0\), the contribution is exactly

\[
 \lambda_n^{\rm off}
 =8-8\cosh(n\log2)
 =8-4(2^n+2^{-n})<0.
\tag{37}
\]

A transfer of the centered ratios concluding a one-sided bound that did
not preserve (37) would be falsified. The checker file verifies (37) with
rationals; it uses no zero approximations.

## 8. Decision

```text
proved unconditionally:
  the quadratic saddle of the unscaled vector is dominated by primes;
  every power p^a, a>=2, is exponentially smaller there;
  Q_r(s) -> 1 for the centered arithmetic Laguerre vector;
  Q_r^Gamma(s) -> 0, with exact diagonal ratio;
  both ratios are blind to the signed mean difference.

ruled out:
  uniform non-alignment of the fixed vector via T_s;
  transferring the Gamma comparator's coercivity to the von Mangoldt
    channel;
  deducing B_n from centered ratios or Jensen defects.

remains open:
  a direct one-sided linear bound for the mean difference (34),
  preserving its residues when s is carried to the boundary;
  B_n <= (1501/2002) A_n, A1, and RH.
```

`tools/fixed_laguerre_markov_extremal_check.py` checks with `Fraction` the
expansion (11)–(13), the Gamma ratio (31), translation blindness
(35)–(36), the exact row (22), and falsifier (37). The printed ratios are
diagnostics derived from exact integers; no statement uses floating
point.
</content>
