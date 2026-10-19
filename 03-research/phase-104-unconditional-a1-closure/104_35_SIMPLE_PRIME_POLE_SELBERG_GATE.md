# 104_35 — Simple-prime–pole channel and the collective Selberg gate

**Status.** The reduction of `104_32` admits an exact representation in
terms of \(\theta(x)-x\), with the boundary term \(-n\) kept. This
localizes the quartic obligation exclusively to the simple primes:

\[
 B_n^{(p+\mathrm{pole})}
 =-n-\int_0^\infty(\theta(e^u)-e^u)e^{-u}
             L_{n-1}^{(2)}(u)\,du.                         \tag{1}
\]

Equation (1) was attacked with the Selberg identity built **only** from
the simple-prime measure. Its non-centered measure is positive and
supported on primes and semiprimes. Inverting the linear Selberg operator
before taking signs gives an exact linear–quadratic collective identity.
The Hankel kernel of that identity is not coercive: for every even index
it is positive at the origin and negative in the tail. Moreover, even
keeping the support on the real primes, positivity, PNT, and the Selberg
symmetry scale survive raising a single prime weight, while (1) can be
made arbitrarily negative for infinitely many indices in the target range.

Hence, removing the higher prime powers does not repair the
Selberg/Vaughan route. A proportional inequality would still have to use
the exact values \(\log p\) of every weight, in a signed and global way.
Neither (26) of `104_32`, nor A1, nor RH is proved.

## 1. Non-duplication audit and falsifier

`103_17` studies local positivity of
\(\Lambda\log+\Lambda*\Lambda\); `103_63` inverts the Selberg operator for
the complete prime-power measure; `103_70` audits Vaughan and the phase
geometry of its blocks; `104_13` gives the Riccati recurrence for the same
complete measure; `104_32` finally separates the powers
\(p^k,\ k\ge2\).

What is new here is:

1. the exact formula (1) for the residual **simple-prime–pole** channel,
   including both boundary terms;
2. the collective Selberg identity formed only from primes and
   semiprimes;
3. the explicit sign of the inverse kernel at the origin and in the tail;
4. a witness that keeps the support on the real primes and preserves the
   PNT/Selberg scales, yet changes the sought functional without bound.

The off-line quartet does not have the Euler product of simple primes with
weights \(\log p\). Hence a future inequality that actually uses those
weights would not automatically apply to the falsifier. By contrast, the
entire weaker package proved below — prime support, Selberg positivity,
and its summatory scales — also holds for the witness of Section 6 and
does not determine the sign. This avoids a false positive: the
information that could only lie in the exact weights is not attributed to
those axioms.

## 2. Exact correlation with \(\theta-x\)

Let

\[
 \theta(x)=\sum_{p\le x}\log p,
 \qquad N=n-1,
\]

and, for \(a>1\), define

\[
 w_{n,a}(u)=a e^{-au}L_N^{(1)}(au),                         \tag{2}
\]

\[
 d\alpha(u)=\sum_p\log p\,\delta_{\log p}(du),
 \qquad d\beta(u)=e^u\,du,
 \qquad d\mu=d\alpha-d\beta.                              \tag{3}
\]

The continuous Laguerre transform is computed with no approximations:

\[
\begin{aligned}
 \langle w_{n,a},\beta\rangle
 &=a\int_0^\infty e^{-(a-1)u}L_N^{(1)}(au)\,du\\
 &=1+{(-1)^{n+1}\over(a-1)^n}
 =n[z^n]\log\left({a\over1-z}-1\right).             \tag{4}
\end{aligned}
\]

The central equality uses the Laguerre generating function; equivalently,
after \(v=au\), it is the elementary Laplace transform of
\(L_N^{(1)}\). On the other hand,

\[
 \langle w_{n,a},\alpha\rangle
 =a\sum_p{\log p\over p^a}L_N^{(1)}(a\log p).                \tag{5}
\]

By (22) of `104_32`, (4)–(5) prove

\[
 B_{n,a}^{(p+\mathrm{pole})}
 :=\langle w_{n,a},\beta-\alpha\rangle,
 \qquad
 B_n^{(p+\mathrm{pole})}=\lim_{a\downarrow1}B_{n,a}^{(p+\mathrm{pole})}.
                                                                    \tag{6}
\]

To display the boundary term, set
\(E_\theta(u)=\theta(e^u)-e^u\). The primitive of \(\mu\) from zero is

\[
 \mu([0,u])=E_\theta(u)+1.                                  \tag{7}
\]

Stieltjes integration of (6), first with \(a>1\), has no boundary term at
zero because (7) vanishes there. Moreover,

\[
 {d\over du}\{e^{-u}L_N^{(1)}(u)\}
 =-e^{-u}L_N^{(2)}(u).                                       \tag{8}
\]

The effective PNT bound used in `104_01` justifies dominated convergence
after the cancellation in (7). Since

\[
 \int_0^\infty e^{-u}L_N^{(2)}(u)\,du=N+1=n,                 \tag{9}
\]

(6)–(9) give exactly (1). In particular, the boundary term is \(-n\), not
\(-1\).

Below the first prime, \(E_\theta(u)=-e^u\). Using
\((L_n^{(1)})'=-L_{n-1}^{(2)}\), (1) also has the form

\[
 \boxed{
 B_n^{(p+\mathrm{pole})}
 =1-L_n^{(1)}(\log2)
 -\int_{\log2}^\infty E_\theta(u)e^{-u}
                       L_{n-1}^{(2)}(u)\,du.}                 \tag{10}
\]

No divergent quantity has been separated in (1) or (10).

## 3. The proportional obligation in the \(\theta\) coordinate

Let \(R_N=P_N^{(\ge2)}(1)\), the absolutely convergent correction of
`104_32`. Its equation (26) is

\[
 3A_n+4B_n^{(p+\mathrm{pole})}
 \ge {A_n\over1001}+4R_N.                                   \tag{11}
\]

Inserting (10), (11) is equivalent to a single simple-prime correlation:

\[
\boxed{
 \int_{\log2}^\infty E_\theta(u)e^{-u}L_{n-1}^{(2)}(u)\,du
 \le
 \left({3\over4}-{1\over4004}\right)A_n
 +1-L_n^{(1)}(\log2)-R_N.}                                  \tag{12}
\]

The term \(R_N\) satisfies \(|R_N|<14n+1\), but it is neither omitted nor
absorbed for \(150\le n<e^{112116}\). Proving (12) uniformly is exactly
the proportional front; (10) does not by itself cheapen it.

## 4. Selberg formed only from primes and semiprimes

For \(\Re s>1\), let

\[
 Q(s)=\int e^{-su}\,d\alpha(u)=\sum_p{\log p\over p^s}.
                                                                    \tag{13}
\]

The prime–Selberg identity is

\[
 -Q'(s)+Q(s)^2=\int e^{-su}\,d\mathcal A_p(u),                \tag{14}
\]

\[
 d\mathcal A_p=u\,d\alpha+\alpha*\alpha\ge0.                \tag{15}
\]

The measure of (15) is supported only on primes and semiprimes. Its
weights are

\[
 \begin{array}{c|c}
 \text{point}&\text{weight}\ \\ \hline
 \log p&(\log p)^2,\\
 2\log p&(\log p)^2,\\
 \log p+\log q&2\log p\log q\quad(p\ne q).
 \end{array}                                                   \tag{16}
\]

Since \((\beta*\beta)(du)=u e^u du=u\,d\beta\), the continuous reference
of (15) is \(2u\,d\beta\). Defining

\[
 d\mathcal B_p=d\mathcal A_p-2u\,d\beta,                     \tag{17}
\]

the substitution \(\alpha=\beta+\mu\) produces, with no piece estimated,

\[
 \boxed{d\mathcal B_p=u\,d\mu+2\beta*\mu+\mu*\mu.}         \tag{18}
\]

This is the Selberg identity centered after removing all higher prime
powers.

## 5. Collective inversion and exact loss of coercivity

For a function \(g\) with sufficient decay, (18) gives

\[
 \langle g,\mathcal B_p\rangle
 =\langle\mathcal Tg,\mu\rangle+\mathcal Q_g(\mu),             \tag{19}
\]

\[
 (\mathcal Tg)(v)
 =vg(v)+2e^{-v}\int_v^\infty e^t g(t)\,dt,
 \qquad
 \mathcal Q_g(\mu)=\iint g(u+v)\,d\mu(u)d\mu(v).             \tag{20}
\]

Instead of separating the three summands of (18), we solve

\[
 \mathcal Tg=w_{n,a}.                                         \tag{21}
\]

The solution decaying at infinity is explicit:

\[
\boxed{
 g_{n,a}(v)={1\over v}\left[
 w_{n,a}(v)-2v^2e^{-v}\int_v^\infty
 {e^t w_{n,a}(t)\over t^3}\,dt\right].}                     \tag{22}
\]

The apparent singularity at zero is removable. The proof consists of
differentiating

\[
 H(v)=v^2e^{-v}\int_v^\infty{e^tw_{n,a}(t)\over t^3}\,dt
\]

and checking that \(H'=(2/v-1)H-w/v\). Then
\(g=-H'-H\), and integrating from infinity recovers (20)–(21).
All the integrals converge absolutely for \(a>1\).

Inserting (21) into (19), the regulated channel is exactly coupled:

\[
 \boxed{
 B_{n,a}^{(p+\mathrm{pole})}
 =-\langle g_{n,a},\mathcal B_p\rangle
   +\mathcal Q_{g_{n,a}}(\mu).}                               \tag{23}
\]

Identity (23) is the absolute-value-free attack sought. It produces no
lower bound because its quadratic form is not positive. Indeed, from
\(L_N^{(1)}(0)=n\) and
\(L_N^{(2)}(0)=n(n+1)/2\) one obtains

\[
 \boxed{
 g_{n,a}(0)=an\left({a(n+1)\over2}-1\right)>0.}               \tag{24}
\]

For \(N=n-1\ge1\), the leading term at infinity is

\[
 \boxed{
 g_{n,a}(v)
 ={(-1)^N a^{N+1}\over N!}e^{-av}v^{N-1}
   \{1+O_{n,a}(v^{-1})\}.}                                   \tag{25}
\]

Hence, for each even \(n\) there exists \(R_{n,a}\) such that

\[
 g_{n,a}(2R)<0\qquad(R\ge R_{n,a}).                           \tag{26}
\]

Taking \(\sigma=c\delta_R\), \(c>0\),

\[
 \mathcal Q_{g_{n,a}}(\sigma)=c^2g_{n,a}(2R)<0.               \tag{27}
\]

So, even in the exclusively prime channel, the Selberg convolution is not
a coercive energy. The loss occurs after keeping the linear and quadratic
terms coupled; it is not a consequence of having taken absolute values.

## 6. Witness on the real prime support

The loss of sign cannot be repaired either by using only the fact that
the atoms are on primes. Fix a real prime \(p_0\), \(R=\log p_0\), and
raise only its weight:

\[
 d\alpha_c=d\alpha+c\delta_R,
 \qquad c>0.                                                   \tag{28}
\]

The measure remains positive, and its support remains exactly a subset of
the real primes. Its Chebyshev function changes by the bounded step
\(c\mathbf1_{u\ge R}\); hence it preserves the same order and every
eventual PNT-type asymptotic relation. It is not claimed to preserve the
same effective constants nor the same initial range of a fixed PNT
inequality.

The non-centered Selberg measure remains positive, and its variation is

\[
 d\mathcal A_{p,c}-d\mathcal A_p
 =cR\delta_R+2c\,\alpha*\delta_R+c^2\delta_{2R}.               \tag{29}
\]

Using the elementary bound
\(\theta(x)\le2(\log2)x\), its accumulated mass up to \(U\) is at most

\[
 cR+4c(\log2)e^{U-R}+c^2=O_{c,R}(e^U).                         \tag{30}
\]

Hence it also preserves the \(O(x)\) scale of the centered Selberg
symmetry.

However, (6) changes exactly by

\[
 B_{n,a}[\alpha_c]-B_{n,a}[\alpha]=-c\,w_{n,a}(R).             \tag{31}
\]

Since the perturbation is a single atom, the critical limit is ordinary
and

\[
 B_n[\alpha_c]-B_n[\alpha]
 =-{c\over p_0}L_{n-1}^{(1)}(\log p_0).                        \tag{32}
\]

If \(n\) is odd, then \(N=n-1\) is even and (2) is positive for every
sufficiently large \(R\). There are arbitrarily large primes, so for each
odd index — in particular for infinitely many
\(n\ge150\) — a real prime can be chosen in the tail and (32) made
arbitrarily negative by increasing \(c\).

This witness does not preserve the canonical value \(\log p_0\); that is
precisely its logical content. It proves that **prime support +
positivity + PNT + Selberg scale** do not imply a proportional bound. A
theorem closing (12) must distinguish the exact weights \(\log p\) from
(28).

## 7. Why Vaughan gains no new direction

For any weight \(W\), the tautological split is

\[
 \sum_p\log p\,W(p)
 =\sum_m\Lambda(m)W(m)
  -\sum_p\sum_{k\ge2}\log p\,W(p^k).                          \tag{33}
\]

In the Laguerre weight of this front, the second term is exactly
\(R_N\), already removed and bounded by `104_32`. Applying Vaughan to the
first term returns the blocks of `103_70`: in logarithmic coordinates its
phase depends only on the sum of the variables, and its Hessian has rank
one. Subtracting \(R_N=O(n)\) creates no curvature in the flat directions
nor a signed estimate between shells. Hence the simple channel does not
unlock standard Type I/II; the missing input remains a joint bound on the
exact weights.

## 8. Decision

```text
proved unconditionally:
  exact theta-Laguerre formula (1) and boundary term -n;
  exact exterior form (10) and proportional obligation (12);
  positive simple-prime/semiprime-only Selberg (14)--(18);
  absolute-value-free collective identity (23);
  sign g(0)>0 and negative tail sign for every even n;
  witness on prime support preserving PNT and Selberg scale.

ruled out:
  positivity of the simple Selberg measure as coercivity of (23);
  prime support + PNT/Selberg scale as a substitute for the log p weights;
  standard Vaughan as a new oscillatory direction after removing p^k.

remains open:
  a signed, global inequality using the exact weights log p that proves
  (12), equivalently (26) of 104_32.

not proved:
  the proportional bound, A1, or RH.
```

`tools/simple_prime_pole_selberg_check.py` checks with `Fraction` the
boundary polynomial identities of (8)–(9) and the algebraic expansion of
the centered measure in (18).
</content>
