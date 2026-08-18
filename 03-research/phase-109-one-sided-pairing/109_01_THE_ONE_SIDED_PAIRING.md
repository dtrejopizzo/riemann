# 109.01 — The one-sided pairing: construction, convergence, bilinearity,
# symmetry type

## 0. Result

> A genuine bilinear pairing built from the positive-shell functionals
> $\{\Gamma_{p,k}:k\ge1\}$ **does exist**. It is
> $$B(f,g):=\sum_p\sum_{k\ge1}(\log p)\,\Gamma_{p,k}(f)\,\Gamma_{p,k}(g)
> =\sum_{n\ge2}\Lambda(n)\,f(n)\,g(n),$$
> absolutely convergent on an explicit vector space $\mathcal G_B\subset
> \mathcal G$ (Definition 1.2 below), genuinely bilinear (Theorem 2.1),
> symmetric but **not** Hermitian (Theorem 2.2), and its restriction to the
> graded family recovers 108_36's object exactly: $B(f_s,f_t)=-\zeta'/\zeta(s+t)$
> on the sharp domain $\Re(s+t)>1$ (Theorem 3.1), so that $B(f_s,f_0)=-\zeta'/\zeta(s)$
> is 108_36's assembly at $t=0$.
>
> The "main risk" flagged in the mission — that the one-sided sum might be
> only a Dirichlet series with no bilinear structure — **does not
> materialize**. Step 1 is not a no-go.

No zero of $\xi$ enters any definition below.

## 1. The construction

Recall from 108_34 (Definition 1.2, Lemma 1.3): for $k\ge1$,
$\Gamma_{p,k}(h_0)=h_0(p^k)$ exactly (the factor $p^{\min(k,0)}$ is $1$ for
$k\ge1$), a linear, everywhere-finite point-evaluation functional on
$\mathcal G=C^0((0,\infty),\mathbb C)$.

> ### Definition 1.1 (the bilinear square of a point evaluation)
> For a linear functional $\ell$ on $\mathcal G$, its **bilinear square** is
> $(f,g)\mapsto\ell(f)\ell(g)$. For $\ell=\Gamma_{p,k}$ this is
> $\Gamma_{p,k}(f)\Gamma_{p,k}(g)=f(p^k)g(p^k)$, $k\ge1$.

This is the *canonical* — not chosen to fit an answer — bilinearization of a
linear functional: it is rank-one, symmetric, and it is literally forced by
what $\Gamma_{p,k}$ already is (a point evaluation), since point evaluation
is multiplicative: $\delta_x(f)\delta_x(g)=f(x)g(x)=\delta_x(fg)$. No free
parameter is chosen here; there is exactly one bilinear form of rank $1$
built from a single linear functional, up to the trivial rescaling already
fixed by 108_35/108_36's $\log p$ normalization (quoted, not re-derived).

> ### Definition 1.2 (the domain $\mathcal G_B$)
> $$\mathcal G_B:=\Big\{f\in\mathcal G:\ \sum_{n\ge2}\Lambda(n)\,|f(n)|^2<\infty\Big\},$$
> the $\ell^2(\Lambda)$-type sections, where the sum ranges over all
> integers $n\ge2$ and $\Lambda(n)=\log p$ if $n=p^k$ ($p$ prime, $k\ge1$),
> $\Lambda(n)=0$ otherwise (von Mangoldt).

> ### Definition 1.3 (the one-sided pairing)
> For $f,g\in\mathcal G_B$,
> $$B(f,g):=\sum_p\sum_{k\ge1}(\log p)\,\Gamma_{p,k}(f)\,\Gamma_{p,k}(g).$$

> ### Lemma 1.4 (closed form)
> $B(f,g)=\sum_{n\ge2}\Lambda(n)f(n)g(n)$.

**Proof.** Every pair $(p,k)$ with $p$ prime, $k\ge1$, corresponds to a
unique prime power $n=p^k\ge2$, with $\Lambda(n)=\log p$, and
$\Gamma_{p,k}(f)\Gamma_{p,k}(g)=f(p^k)g(p^k)=f(n)g(n)$ by Definition 1.1.
Summing over all $(p,k)$ is summing over all prime powers $n$; extending the
sum to all $n\ge2$ adds only zero terms ($\Lambda(n)=0$ off prime powers).
$\square$

This closed form is the working definition for everything below.

## 2. Convergence, bilinearity, symmetry type

> ### Theorem 2.1 (well-defined, bilinear)
> For every $f,g\in\mathcal G_B$, the series defining $B(f,g)$ converges
> absolutely, and $B:\mathcal G_B\times\mathcal G_B\to\mathbb C$ is
> $\mathbb C$-bilinear: linear in $f$ for fixed $g$, and linear in $g$ for
> fixed $f$.

**Proof.** *Convergence.* By Cauchy–Schwarz for the measure $\Lambda(n)$
on $\{n\ge2\}$ (a genuine measure: $\Lambda(n)\ge0$),
$$\sum_n\Lambda(n)|f(n)g(n)|\le\Big(\sum_n\Lambda(n)|f(n)|^2\Big)^{1/2}
\Big(\sum_n\Lambda(n)|g(n)|^2\Big)^{1/2}<\infty$$
since $f,g\in\mathcal G_B$. This bounds the defining series of $B(f,g)$
absolutely.

*Bilinearity.* For $f_1,f_2,g\in\mathcal G_B$ and $c_1,c_2\in\mathbb C$,
term by term, $\Lambda(n)(c_1f_1(n)+c_2f_2(n))g(n)=c_1\Lambda(n)f_1(n)g(n)
+c_2\Lambda(n)f_2(n)g(n)$; since all three series converge absolutely
(Cauchy–Schwarz applies to $c_1f_1+c_2f_2\in\mathcal G_B$, a linear space,
as well as to $f_1,f_2$ individually), the sums may be split, giving
$B(c_1f_1+c_2f_2,g)=c_1B(f_1,g)+c_2B(f_2,g)$. Linearity in the second slot
is identical by the symmetry of the summand. $\square$

> ### Theorem 2.2 (symmetric, not Hermitian)
> $B(f,g)=B(g,f)$ for all $f,g\in\mathcal G_B$ (symmetric $\mathbb C$-bilinear
> form). $B$ is **not** Hermitian: there exist $f,g\in\mathcal G_B$ (indeed
> among the graded family) with $\overline{B(g,f)}\ne B(f,g)$.

**Proof.** *Symmetry.* $\Lambda(n)f(n)g(n)=\Lambda(n)g(n)f(n)$ termwise
(commutativity of multiplication in $\mathbb C$), so the two series are
identical term by term, hence equal.

*Not Hermitian.* Hermitian would require $\overline{B(g,f)}=B(f,g)$ for
all $f,g$; combined with symmetry ($B(g,f)=B(f,g)$) this would force
$B(f,g)=\overline{B(f,g)}$, i.e. $B(f,g)\in\mathbb R$ always. But
Theorem 3.1 below gives $B(f_s,f_t)=-\zeta'/\zeta(s+t)$ for $\Re(s+t)>1$;
taking $s=2,t=\tfrac12+i$ (so $\Re(s+t)=2.5>1$), $-\zeta'/\zeta(2.5+i)$ is
not real (checked numerically in the verifier, §5). A single non-real value
refutes Hermiticity. $\square$

So $B$ is symmetric $\mathbb C$-bilinear, structurally the same type of
object as a real (non-sesquilinear) quadratic form — consistent with the
one-sided assembly being, in 108_36's own words, "unsymmetrized": there is
no conjugate-linear structure here because there is no $s\mapsto1-s$
involution being paired against its own conjugate; $B$ pairs $f$ against
$g$ directly, with no complex conjugation anywhere in the definition.

## 3. Specialization to the graded family; recovering 108_36

> ### Theorem 3.1 (graded specialization)
> $f_s\in\mathcal G_B$ iff $\Re s>\tfrac12$ (since $\sum_n\Lambda(n)n^{-2\Re s}$
> converges iff $2\Re s>1$, 108_36 Theorem 1.1's convergence criterion
> applied at exponent $2\Re s$). For $\Re(s+t)>1$ (a strictly larger region
> than "$\Re s>\frac12$ and $\Re t>\frac12$"),
> $$B(f_s,f_t)=\sum_{n\ge2}\Lambda(n)n^{-(s+t)}=-\frac{\zeta'}{\zeta}(s+t),$$
> by 108_36 Theorem 1.1 applied at the single complex variable $s+t$.

**Proof.** The convergence claim for $f_s\in\mathcal G_B$ is immediate from
Definition 1.2. For the pairing formula: whenever $\Re(s+t)>1$,
$\sum_n\Lambda(n)|n^{-s}n^{-t}|=\sum_n\Lambda(n)n^{-\Re(s+t)}<\infty$ by
108_36 Theorem 1.1 (absolute convergence of $\sum\Lambda(n)n^{-\sigma}$ for
$\sigma>1$), so the double sum defining $B(f_s,f_t)$ converges absolutely
and equals $\sum_n\Lambda(n)n^{-(s+t)}$, identified with $-\zeta'/\zeta(s+t)$
by 108_36 Theorem 1.1 (read from source, not re-derived). $\square$

> ### Corollary 3.2 (108_36 is the slice $t=0$)
> $f_0\equiv1$ (the constant function). $B(f_s,f_0)=-\zeta'/\zeta(s)$ for
> $\Re s>1$, exactly 108_36 Theorem 1.1's object.

**Proof.** Immediate from Theorem 3.1 at $t=0$. $\square$

**Caveat, stated precisely so as not to overclaim.** $f_0\equiv1$ is
*not* in $\mathcal G_B$ ($\sum_n\Lambda(n)\cdot1=\infty$), so the pair
$(f_s,f_0)$ lies in the *sharp* convergence region $\Re(s+t)>1$ established
directly by Theorem 3.1's proof, but outside the "safe" region
$\mathcal G_B\times\mathcal G_B$ guaranteed by Cauchy–Schwarz. This is not a
contradiction — $\Re(s+t)>1$ genuinely is a larger convergence region than
what Cauchy–Schwarz alone certifies — but it means Corollary 3.2 is an
**extension** of $B$ beyond $\mathcal G_B\times\mathcal G_B$ by direct
absolute convergence of the specific series, not a statement located inside
the vector space on which Step 2 computes the radical. Step 2 works
entirely inside $\mathcal G_B$ (Definition 1.2), where this subtlety does
not arise, because every partner function used there (compactly supported
bumps) lies in $\mathcal G_B$ trivially.

## 4. What $B$ does and does not give

**Gives.** A genuine, non-circular bilinear pairing on $\mathcal G_B$,
built from nothing but the shell functionals already proved in 108_34, whose
diagonal-in-$(s,t)$-sum specialization recovers 108_36's meromorphic object
exactly, and whose $(s,t)$-plane continuation has $-\zeta'/\zeta(s+t)$'s
poles along the lines $s+t=1$ and $s+t=\rho$ (zeros of $\xi$) — but see the
remark below on why this is *not* the same phenomenon as a radical.

**Does not give.** Any claim yet about $\mathrm{rad}\,B$ — that is Step 2.

> **Remark 4.1 (poles are not the radical).** A pole of the *continued
> numerical value* $B(f_s,f_t)=-\zeta'/\zeta(s+t)$ along $s+t=\rho$ says the
> pairing, evaluated at those specific graded arguments and analytically
> continued past its region of absolute convergence, blows up. A radical
> direction is the opposite: a vector that pairs to *zero* with everything,
> inside the region where $B$ is an candid (convergent, finite) bilinear
> form. The appearance of zeros of $\xi$ in the pole locus of the numerical
> family $s\mapsto B(f_s,f_t)$ is therefore not evidence, one way or the
> other, about the shape of $\mathrm{rad}\,B$; that has to be computed
> directly, which is exactly what Step 2 does.

## 5. Scope

**Proved here:** Definition 1.1's forcedness (no free parameter); Lemma 1.4
(closed form); Theorem 2.1 (convergence + bilinearity on $\mathcal G_B$);
Theorem 2.2 (symmetric, not Hermitian); Theorem 3.1 and Corollary 3.2
(graded specialization, recovering 108_36 exactly at $t=0$); Remark 4.1.

**Read from source, not re-derived:** 108_34 Definition 1.2/Lemma 1.3
($\Gamma_{p,k}$, $k\ge1$, is point evaluation); 108_36 Theorem 1.1
($\sum\Lambda(n)n^{-\sigma}=-\zeta'/\zeta(\sigma)$ and its convergence
domain, its poles).

**Verified numerically:** the pairing formula $B(f_s,f_t)=-\zeta'/\zeta(s+t)$
against direct truncated summation, with error shrinking under refinement,
at several $(s,t)$; bilinearity and symmetry as exact finite-sum identities;
non-Hermiticity via an explicit non-real value; divergence (non-Cauchy
partial sums) at $\Re(s+t)\le1$.

**Not established, and explicitly not claimed:** anything about
$\mathrm{rad}\,B$ (Step 2); any intersection-theoretic reading; any
statement about RH.

## 6. Verifier

`109_01_the_one_sided_pairing.py` checks: the closed-form identity of
Lemma 1.4 against the double-sum definition; bilinearity and symmetry as
exact finite-truncation identities (not approximate); non-Hermiticity via
an explicit non-real value of $B(f_s,f_t)$, with a control clause confirming
$B$ *is* symmetric on the very same pair; convergence of the truncated sum
to $-\zeta'/\zeta(s+t)$ with the error shrinking under refinement (three
increasing truncation depths, strictly decreasing error, compared against
mpmath's $\zeta,\zeta'$); and divergence (partial sums that fail to
stabilize) at $\Re(s+t)\le1$, by comparing successive partial-sum
increments rather than any fixed threshold.
