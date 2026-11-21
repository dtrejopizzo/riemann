# Paper 05 — The ω-hierarchy of the Riemann zeta function: per-prime weights, moment exponents and the branching picture of the maximum

An expository note. It relates three descriptions of the size of ζ on the critical line — the moment
exponents $(\log T)^{k^2}$, the exponents $\beta^2$ attached to $|\zeta(\tfrac12+it)|^{2\beta}$, and the
Fyodorov–Hiary–Keating law for the maximum of $\log|\zeta|$ on short intervals — to the weight
$z^{\omega(n)}$, where $\omega(n)$ is the number of distinct prime factors of $n$. No statement assumes or
bears on the Riemann hypothesis.

## Contents

Proved (routine consequences of the Selberg–Delange method and of Mertens' theorem):

- Lemma 2.1: a uniform Selberg–Delange asymptotic for $\sum_{n\le N} g(n)/n$ when
  $\sum g(n)n^{-s}=\zeta(s)^z H(s)$ with $H$ an absolutely convergent Dirichlet series on
  $\mathrm{Re}\,s\ge 1-\delta$; in particular $\sum_{n\le N} z^{\omega(n)}/n\sim C(z)(\log N)^z$ for $z>0$.
- Proposition 3.1 and Theorem 3.2: $d_k(n)=k^{\omega(n)}$ on squarefree $n$; the diagonal sum
  $\sum_{n\le N} d_k(n)^2/n$ (the mean square of the Dirichlet polynomial of $\zeta^k$) is
  $\sim A_k(\log N)^{k^2}$; the squarefree sum $\sum^\flat z^{\omega(n)}/n\sim C^\flat(z)(\log N)^z$.
- Proposition 4.1: $\sum_{n\le N} d_\beta(n)^2/n\sim A_\beta(\log N)^{\beta^2}$ for real $\beta>0$.
- Theorem 5.1: under the probability measure proportional to $z^{\omega(n)}/n$ on $n\le N$, for every
  $z>0$, $\omega(n)$ concentrates at $z\log\log N$ and $(\omega(n)-z\log\log N)/\sqrt{z\log\log N}$ is
  asymptotically Gaussian.
- Proposition 6.2: the primes with $\lfloor\log\log p\rfloor=j$ contribute variance $\tfrac12+O(e^{-j})$ to
  the prime model of $\log|\zeta|$; the total variance for $p\le T$ is
  $\tfrac12\log\log T+\tfrac M2+O(1/\log T)$.

Heuristic (stated as such in the paper):

- The arrows of the summary chain in Section 9.1 (substitutions $z=k^2$, $z=\beta^2$; an analogy between
  prime factors and levels; the passage to the maximum) are not theorems.
- Remark 4.2: the link $z=\beta^2$ between the weight and the powers $|\zeta|^{2\beta}$; the critical value
  $\beta_c=1$ of the short-interval chaos corresponds formally to the trivial weight $z=1$, and the
  $\omega$-weighted sum has no transition there.
- Heuristic 7.1: a branching random walk with $\log\log T$ generations, $\log T$ leaves (branching rate $\kappa=1$) and
  increment variance $\tfrac12$ has maximum $\log\log T-\tfrac34\log\log\log T+O_{\mathbb P}(1)$.

Numerical (Section 8, small scale, $\log\log N<3$; illustrations only): fitted slopes of
$\log\sum_{n\le N}z^{\omega(n)}/n$ against $\log\log N$ and comparison with $C(z)$, $C^\flat(z)$; the mean of
$\omega$ under the tilted weight; the level variances for $p\le 10^7$; the maximum of the prime model over
windows of length 1 (compared with the two-term expression for windows of length 2; the difference is $O(1)$).

## Known and new

Everything proved here is classical in substance: $d_k(n)=k^{\omega(n)}$ on squarefree $n$, the
Selberg–Delange asymptotics, Mertens' theorem, and the Erdős–Kac/Sathe–Selberg description of $\omega(n)$;
the branching picture of the maximum and the theorems on it are due to Fyodorov–Hiary–Keating,
Arguin–Belius–Bourgade–Radziwiłł–Soundararajan, Najnudel, Arguin–Bourgade–Radziwiłł and Harper. The note
contributes the arrangement of these facts around the weight $z^{\omega(n)}$, with complete proofs of the
arithmetic statements in the form used (in particular Theorem 5.1 for the harmonic weight, all $z>0$).

## Files

- [`main.tex`](main.tex) — LaTeX source.
- [`omega-hierarchy-chaos.pdf`](omega-hierarchy-chaos.pdf) — compiled paper (11 pages).
- [`numerics.py`](numerics.py) — script producing the numbers of Section 8 (Python 3 with numpy).
- [`numerics_output.txt`](numerics_output.txt) — its output.

## Relation to other papers

Independent of Papers 02–03 in its proofs; it shares with them only the grading of integers by $\omega(n)$.
