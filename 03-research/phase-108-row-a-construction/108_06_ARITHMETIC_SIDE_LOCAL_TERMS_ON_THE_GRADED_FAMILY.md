# 108.06 — The arithmetic-side local terms of $\mathfrak T_S$ on the graded family

## 0. What this settles

Stage 1 asks for a measure-valued extension of the corner trace to
$\mathcal G=\{f_a(x)=x^{-a}\}$.  This note computes the **arithmetic side**
in closed form and determines exactly where it converges.

The result is a sharp dichotomy: the local terms converge **precisely on the
critical strip**, and the sum over all places diverges **everywhere on that
strip**.  Both halves are proved.

No zero of $\xi$ enters any definition here, in accordance with 108_00 §2.
This is why the arithmetic side, not the zero side, is used — see §1.

## 1. Why the arithmetic side

107_239 (2.1) gives two expressions agreeing on compactly supported data:

\[
 \text{(arithmetic)}\quad
 \mathfrak T_S(h)=\sum_{v\in S}\int_{\mathbb Q_v^\times}'
 \frac{h(u^{-1})}{|1-u|_v}\,d^\times u,
 \qquad
 \text{(zeros)}\quad
 N(h)=\hat h(0)+\hat h(1)-\sum_\rho\hat h(\rho).
\]

The zero side is unusable for the extension, for two independent reasons.

1. It would put a zero of $\xi$ into a definition, which 108_00 §2 forbids.
2. **It diverges.**  Under the cutoff of 108_05 the truncated Mellin
   transform of $f_a$ at $s$ is $2\sinh((s-a)\log T)/(s-a)$, of modulus
   $\asymp T^{|\Re(s-a)|}$.  At any zero $\rho$ with $\Re\rho\ne a$ this is
   unbounded, and smearing in $a$ against $\varphi$ supported near $a$ does
   not help, since $|\Re\rho-a|$ stays bounded away from $0$ on the support.

So the extension is built on the arithmetic side, which mentions no zeros.

## 2. The graded family diagonalises the convolution

> ### Proposition 2.1
> For $g$ a test function and $\tilde g(x)=\overline{g(1/x)}$,
> \[
>  f_a\star\tilde g \;=\; c_g(a)\,f_a,
>  \qquad
>  c_g(a)=\int_0^\infty t^{-a}\,\overline{g(t)}\,d^\times t .
> \]

**Proof.**
$(f_a\star\tilde g)(x)=\int_0^\infty y^{-a}\overline{g(y/x)}\,d^\times y$;
substituting $y=xt$ and using invariance of $d^\times y$ gives
$x^{-a}\int_0^\infty t^{-a}\overline{g(t)}\,d^\times t$. $\square$

For $g$ compactly supported in $(0,\infty)$, $c_g(a)$ is entire in $a$.
Verified numerically to $3\times10^{-10}$ relative error over two profiles,
four complex grades and three arguments.

> **Consequence.**  The whole of Stage 1 reduces to computing
> $\mathfrak T_S(f_a)$ for a single monomial; the test function contributes
> only the scalar $c_g(a)$.

## 3. The local term at a finite place, in closed form

Embed through the module, $h(u)=h(|u|)$, so $f_a(u^{-1})=|u|_v^{a}$.  Then

\[
 W_p(f_a)=\int_{\mathbb Q_p^\times}'\frac{|u|_p^{a}}{|1-u|_p}\,d^\times u .
\]

Decompose $\mathbb Q_p^\times$ into shells $|u|_p=p^{-n}$, each of
$d^\times u$-measure $1$ with $\int_{\mathbb Z_p^\times}d^\times u=1$:

* $n\ge1$: $|u|_p<1$, so $|1-u|_p=1$; contribution $p^{-na}$;
* $n\le-1$: $|u|_p>1$, so $|1-u|_p=|u|_p$; with $m=-n$, contribution $p^{m(a-1)}$;
* $n=0$: $|u|_p=1$, contribution $C_p:=\int'_{\mathbb Z_p^\times}d^\times u/|1-u|_p$,
  the Tate principal value — **independent of $a$**, since $|u|_p^a=1$ there.

> ### Theorem 3.1
> \[
>  \boxed{\;
>  W_p(f_a)=\frac{p^{-a}}{1-p^{-a}}+\frac{p^{a-1}}{1-p^{a-1}}+C_p\;}
> \]
> with $C_p$ independent of $a$, and the two series converge if and only if
> $\Re a>0$ and $\Re a<1$ respectively.

**Proof.**  Summing the shell contributions gives two geometric series,
$\sum_{n\ge1}p^{-na}$ with ratio $p^{-a}$, convergent iff $|p^{-a}|<1$ iff
$\Re a>0$; and $\sum_{m\ge1}p^{m(a-1)}$ with ratio $p^{a-1}$, convergent iff
$\Re a<1$.  Their sums are as displayed. $\square$

Verified to $1.2\times10^{-15}$ relative error against direct shell summation
for six primes and six complex grades.

> ### Corollary 3.2 (the convergence region is the critical strip)
> $W_p(f_a)$ converges **exactly** for
> \[
>  0<\Re a<1 ,
> \]
> and the two boundary lines $\Re a=0$ and $\Re a=1$ are genuinely excluded.

Convergence depends only on $\Re a$; verified along $\Re a=\tfrac12$ up to
$|\Im a|=500$.

**This is worth stating plainly:** the critical strip appears here from
purely local $p$-adic analysis of a monomial, with no input from zeros, from
the functional equation, or from the Weil form.

## 4. The global sum diverges everywhere on the strip

> ### Theorem 4.1
> For every $a$ with $0<\Re a<1$, **both**
> \[
>  \sum_p\frac{p^{-a}}{1-p^{-a}}
>  \qquad\text{and}\qquad
>  \sum_p\frac{p^{a-1}}{1-p^{a-1}}
> \]
> diverge.

**Proof.**  $\frac{p^{-a}}{1-p^{-a}}\sim p^{-a}$ and
$\frac{p^{a-1}}{1-p^{a-1}}\sim p^{a-1}$ as $p\to\infty$.  By Mertens/PNT,
$\sum_{p\le x}p^{-s}$ diverges for $\Re s\le1$.  The first series has
$s=a$ with $\Re a<1$; the second has $s=1-a$ with $\Re(1-a)<1$ since
$\Re a>0$.  Both exponents lie in the divergent range. $\square$

Verified threshold-free: the partial sums follow the Mertens growth
$x^{1-a}/\log x$, with fitted log–log slopes $0.805, 0.600, 0.394, 0.201,
0.066$ against the theoretical $1-a = 0.9, 0.7, 0.5, 0.3, 0.1$ (the gap is
the expected $1/\log x$ correction).

### 4.2 What this means

The two convergence requirements are **complementary and exhaustive**:
$\Re a>0$ makes the first local series converge but the first global sum
diverge; $\Re a<1$ does the same for the second.  There is no $a$ at which
both the local and the global conditions hold.

This is the precise failure of the stabilization argument of 107_239 §3.
There, compact support bounds the contributing primes by $p^k\le e^T$, so
$S$ is finite and the sum is trivially convergent.  The graded family has no
compact support (108_02), every prime contributes, and Theorem 4.1 applies.

## 5. Status of Stage 1

> **Semilocal Stage 1 is established.**  For any *finite* set $S$ of places,
> $\mathfrak T_S(f_a\star\tilde g)=c_g(a)\sum_{v\in S}W_v(f_a)$ is defined by
> Proposition 2.1 and Theorem 3.1, holomorphic in $a$ on the strip
> $0<\Re a<1$ away from the poles of the closed form.
>
> **Global Stage 1 is not established, and Theorem 4.1 shows it cannot be
> reached by summing the local terms as they stand.**  A genuine global
> regularization — not merely a cutoff in $x$ — is required.

## 6. Scope

Proved:

* Proposition 2.1: monomials diagonalise the convolution;
* Theorem 3.1: the closed form of $W_p(f_a)$ and the $a$-independence of $C_p$;
* Corollary 3.2: the convergence region is exactly $0<\Re a<1$;
* Theorem 4.1: the sum over all primes diverges throughout that strip.

Not established, and explicitly not claimed:

* any global regularization of $\sum_p W_p(f_a)$;
* the comparison with the zero side — the interchange of the weak limit with
  the conditionally convergent sum over zeros is untouched here, and §1
  shows the naive route to it diverges;
* the value of $C_p$, which is not needed for anything above;
* the archimedean local term, not computed here;
* measure-valuedness in $a$: what is obtained on the strip is *holomorphic*,
  not merely distributional, so 108_05 Corollary 4.1's expectation is not yet
  tested at the global level;
* any change to `ROW_A_STATUS`, which remains `partial`.

## 7. Verifier

`108_06_arithmetic_side_local_terms.py` checks Proposition 2.1 numerically;
the closed form of Theorem 3.1 against direct shell summation; the exact
convergence region including the exclusion of both boundaries and dependence
on $\Re a$ only; divergence of both global sums for five grades in $(0,1)$;
and the Mertens growth law by threshold-free log–log regression against
theory.
