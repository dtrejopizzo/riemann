# 108.36 — The assembly of the correspondence functionals is $-\zeta'/\zeta$

## 0. Result

> Summing the shell functionals of 108_34, in the normalization of 108_35,
> over all primes and all positive shells gives
> \[
>  \boxed{\;\sum_{p}\sum_{k\ge1}\Gamma^{\mathrm{Tate}}_{p,k}(f_s)
>  =\sum_{p}\sum_{k\ge1}(\log p)\,p^{-ks}
>  =\sum_{n\ge1}\Lambda(n)n^{-s}
>  =-\frac{\zeta'}{\zeta}(s)\;}
> \]
> absolutely convergent for $\Re s>1$ and continued meromorphically.

No zero of $\xi$ enters the definition: the left-hand side is built from the
shell decomposition of $\mathbb Q_p^\times$ and a choice of Haar measure.
The identification with $-\zeta'/\zeta$ is a theorem.

## 1. The identity

> ### Theorem 1.1
> For $\Re s>1$ the double sum converges absolutely and equals
> $-\zeta'/\zeta(s)$.

**Proof.**  Every integer $n\ge2$ is uniquely a prime power $p^k$ or is not a
prime power, and $\Lambda(n)=\log p$ exactly when $n=p^k$.  Hence
$\sum_p\sum_{k\ge1}(\log p)p^{-ks}=\sum_{n\ge2}\Lambda(n)n^{-s}$, which is the
classical von Mangoldt Dirichlet series, absolutely convergent for
$\Re s>1$ with sum $-\zeta'/\zeta(s)$.  Absolute convergence follows from
$\sum_n\Lambda(n)n^{-\sigma}\le\sum_n(\log n)n^{-\sigma}<\infty$ for
$\sigma>1$. $\square$

Verified against a direct prime-power summation: at $s=3$ the two agree to
$1.3\times10^{-14}$, at $s=2$ to $4.1\times10^{-9}$, the residuals being the
differing truncation depths of the two computations.

> ### Corollary 1.2 (the mirror family)
> $\sum_p\sum_{m\ge1}\Gamma^{\mathrm{Tate}}_{p,-m}(f_s)
> =\sum_p\sum_{m\ge1}(\log p)p^{m(s-1)}=-\dfrac{\zeta'}{\zeta}(1-s)$,
> absolutely convergent for $\Re s<0$.

## 2. The convergence domains, and why they are disjoint from the strip

The two half-planes $\Re s>1$ and $\Re s<0$ are exchanged by
$s\mapsto1-s$ and are disjoint from the critical strip.  This is not a new
obstruction: it is exactly the statement of 108_06 Theorem 4.1, that the
naive sum over all places diverges throughout $0<\Re s<1$, now seen at the
level of the correspondence functionals rather than of the local terms.

> ### Proposition 2.1
> On the strip the assembly exists only as the meromorphic continuation, not
> as a convergent sum.  The continuation is $-\zeta'/\zeta$, whose poles are
> the pole of $\zeta$ at $1$ and the zeros of $\zeta$.

This is a statement about the continuation, not a definition using zeros:
the object is defined for $\Re s>1$ by Theorem 1.1 and continued by standard
analytic continuation.

## 3. What the assembly does and does not give

**Gives.**  The finite part of Weil's explicit formula, term by term, with
the correct coefficient $\Lambda(p^k)/\sqrt{p^k}$ at $s=\tfrac12$
(108_35 Theorem 2.1), assembled into a single meromorphic object.

**Does not give.**  The archimedean term, which is Stage 4; and the
identification of this object with an intersection number, which is Stage 5.
Theorem 1.1 is an identity between a sum of functionals and a Dirichlet
series; nothing here makes either side an intersection pairing.

## 4. Scope

Proved: Theorem 1.1, Corollary 1.2, Proposition 2.1.

Verified numerically: the identity at three values of $s$ against direct
prime-power summation.

Not established: convergence anywhere on the strip (Proposition 2.1 states
the opposite); the archimedean completion; any intersection-theoretic
reading.

`ROW_A_STATUS` unchanged.  Nothing here bears on RH.

## 5. Verifier

`108_36_the_assembly_is_the_logarithmic_derivative.py` checks the identity
against direct prime-power summation at several $s$ with matched truncation;
that the von Mangoldt coefficients are correctly produced; absolute
convergence for $\Re s>1$ and its failure at $\Re s\le1$ by a threshold-free
growth comparison; and the mirror statement.
