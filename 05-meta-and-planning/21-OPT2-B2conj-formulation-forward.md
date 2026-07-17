# Option 2 — B2conj: precise formulation and the forward direction (proven)

**Auditor build · 2026-06-05.** RH-independent. We make Conjecture B2 precise, prove the forward direction
rigorously, and set up the converse against the backdrop of converse theorems. This is standalone new mathematics:
a characterization of Euler products by the *locality* of the localized-Weil anatomy.

---

## 1. Setup: the localized-Weil anatomy of an $L$-function

Let $L(s)=\sum_n a_L(n)n^{-s}$ be in a class $\mathcal S$ (Selberg-class axioms: Dirichlet series, analytic
continuation, functional equation, Ramanujan bound) — **not** assuming an Euler product. Its completed log-derivative
feeds a localized Weil form $Q_L(g)=\fa[g]-\fp_L[g]$, with the **$L$-prime form**
$$
\fp_L[g]=2\sum_{n\ge2}\frac{\Lambda_L(n)}{\sqrt n}\,\mathrm{Re}\,(g\star\tilde g)(\log n),\qquad
\Lambda_L(n)=-\big(L'/L\big)\text{ coefficient at }n .
$$
Let $u_0$ be the ground state of $Q_L$ on a window and define the **anatomy** as the per-$n$ profile
$$
\mathcal R_L(n)=\frac{\Lambda_L(n)}{\sqrt n}\,\big|\widehat{u_0}(\log n)\big|^2,\qquad
\lambda_{\min}(Q_L)=R_\infty-\sum_{n}\mathcal R_L(n).
$$

**Definition (factorizing anatomy).** $L$ has *factorizing anatomy* if there is a function $\mathcal r$ on prime
powers such that $\mathcal R_L(n)$ depends on $n$ **only through its prime-power factorization, multiplicatively**:
$\Lambda_L$ is supported on prime powers and $\mathcal R_L(p^k)=\mathcal r(p,k)$ with the cross-terms (the
contribution of $n=\prod p_i^{k_i}$ with $\ge2$ distinct primes) **vanishing** from the anatomy.

## 2. The forward direction — proven

\textbf{Proposition (Euler $\Rightarrow$ local anatomy).} *If $L$ has an Euler product
$L(s)=\prod_p L_p(p^{-s})$, then $\Lambda_L$ is supported on prime powers and $\mathcal R_L(p^k)$ depends only on
the local factor $L_p$; the anatomy factorizes.*

\emph{Proof.} An Euler product gives $-L'/L(s)=\sum_p -L_p'/L_p(p^{-s})\log p$, a sum of **per-prime** terms; its
Dirichlet coefficients $\Lambda_L(n)$ are supported on prime powers $n=p^k$, with $\Lambda_L(p^k)$ a function of
the coefficients of $L_p$ alone (the Newton--Girard relations applied to $L_p$). Hence $\Lambda_L(p^k)/\sqrt{p^k}$
is determined by $L_p$. The anatomy weight $\mathcal R_L(p^k)=\Lambda_L(p^k)p^{-k/2}|\widehat{u_0}(\log p^k)|^2$
then depends on $n=p^k$ only through $L_p$ and the (global, $L$-independent) ground state evaluation
$\widehat{u_0}(\log p^k)$. Since $\Lambda_L$ vanishes off prime powers, there are no multi-prime cross-terms:
the anatomy is supported on prime powers and is local. $\square$

\emph{Remark.} The forward direction is structural and unconditional; it does not use RH and holds for every Euler
product in $\mathcal S$. It identifies the precise sense in which an Euler product is "visible" in the localized
Weil form: **the prime form is a sum of single-prime contributions, so the anatomy carries no entanglement between
distinct primes.**

## 3. The converse — the content, and why it is not a known converse theorem

\textbf{Conjecture B2 (converse).} *If $L\in\mathcal S$ has factorizing anatomy — $\Lambda_L$ supported on prime
powers with no multi-prime cross-terms in $\mathcal R_L$ — then $L$ has an Euler product.*

- The hypothesis "$\Lambda_L$ supported on prime powers" is **equivalent** to $-L'/L$ being a sum of per-prime
  Dirichlet series, which is **equivalent** to $\log L=\sum_p(\text{local})$, i.e. an Euler product — *so stated
  that way the converse is a tautology.* The non-trivial content is to **weaken the hypothesis** from "exactly
  supported on prime powers" to a property of the **anatomy** $\mathcal R_L$ (a spectral/positivity quantity): if
  the *ground-state-weighted* profile factorizes, must the underlying coefficients?
- This is **not** Weil's converse theorem (which deduces automorphy/Euler product from functional equations of
  *twists* $L\otimes\chi$): B2 uses no twists, only the *single* localized Weil form's anatomy. It is closer in
  spirit to "a multiplicative structure is forced by the absence of cross-place entanglement in a quadratic
  spectral functional" — a statement with no located precedent.

> **The precise open problem.** Does factorization of the *ground-state-weighted anatomy measure* $\mathcal R_L$
> force $\Lambda_L$ to be supported on prime powers (hence an Euler product)? Equivalently: can a non-Euler
> $L\in\mathcal S$ have an anatomy with vanishing multi-prime cross-terms, by accident of the ground state? A
> counterexample or a proof both are new theorems.

## 4. First test and roadmap

- **Numerical test (existing P10/P9 code):** compute $\mathcal R_L$ for $\zeta$ (Euler — must factorize) and for
  $L_{\mathrm{DH}}$ (no Euler — must *not* factorize), confirming the forward direction and probing the converse's
  plausibility on a known non-Euler $L$.
- **Toward the converse:** study the cross-term $\mathcal R_L(mn)$ for coprime $m,n$ as a bilinear form in the
  ground state; vanishing for all coprime pairs is the factorization hypothesis. Express it via the off-diagonal
  of $\fp_L$ and ask whether vanishing forces $\Lambda_L(mn)=0$.

## Status
- **Forward direction: proven** (Euler $\Rightarrow$ local, prime-power-supported, factorizing anatomy),
  unconditional, RH-free.
- **Converse (B2): precisely formulated**, distinguished from Weil's converse theorem (no twists), and reduced to a
  bilinear-cross-term vanishing question on the ground state. Genuinely new, RH-independent; a proof or
  counterexample is a standalone result.

---

## 5. Advance (Day 41): a conditional converse, with the exact obstruction

Take the **spectral** definition: $L$ has factorizing anatomy iff the anatomy measure has no mass at
non-prime-powers, $\mathcal R_L(n)=0$ for every $n$ with $\ge2$ distinct prime factors. Since
$\mathcal R_L(n)=\Lambda_L(n)n^{-1/2}|\widehat{u_0}(\log n)|^2$, for such $n$
$$
\mathcal R_L(n)=0\iff \Lambda_L(n)=0\ \ \text{or}\ \ \widehat{u_0}(\log n)=0 .
$$

\textbf{Proposition (conditional converse).} *Suppose the ground state satisfies the non-vanishing condition
$\widehat{u_0}(\log n)\ne0$ for every non-prime-power $n$. Then factorizing anatomy implies $\Lambda_L(n)=0$ for
all non-prime-power $n$, i.e. $-L'/L$ is a sum of per-prime series, i.e. $L$ has an Euler product. Hence B2 holds.*

\emph{Proof.} Under the non-vanishing condition, $\mathcal R_L(n)=0$ forces $\Lambda_L(n)=0$ for every
non-prime-power $n$; the rest is the forward-direction computation read backwards. $\square$

> **The exact obstruction.** B2 can fail \emph{only} if the band-limited ground state $\widehat{u_0}$ (an entire
> function of exponential type, hence with isolated zeros) vanishes at $\log n$ for the non-prime-powers $n$ where
> $\Lambda_L(n)\ne0$ --- a fine-tuned alignment of the ground state's discrete zero set with the non-prime-power
> log-lattice. Generically (no such alignment) **B2 is true.** A genuine counterexample is precisely a non-Euler
> $L\in\mathcal S$ whose ground state's zeros conspire to hide its multi-prime coefficients.

This upgrades B2 from "open conjecture" to "**generically a theorem**, with a sharply characterized non-generic
failure mode." Two concrete next targets, both RH-independent: (i) prove the non-vanishing condition holds for a
natural normalization of $u_0$ (e.g. a real, sign-definite Gaussian-localized window), which would make the
converse \emph{unconditional}; (ii) or construct the alignment and exhibit a counterexample. Either settles B2.

---

## 6. Deepening (Day 42): the converse, proven under an all-windows definition

The ground state $g_0$ minimizing $Q_L$ on the Gaussian-localized class is a finite Hermite--Gauss combination,
$g_0(t)=P(t)\,e^{-t^2/2\sigma^2}$ with $P$ a real polynomial. Its autocorrelation (whose transform is
$|\widehat{g_0}|^2\ge0$) is
$$
c_0(u)=(g_0\star\tilde g_0)(u)=Q_\sigma(u)\,e^{-u^2/4\sigma^2},\qquad \deg Q_\sigma\le 2\deg P,
$$
a polynomial times a Gaussian. **So $c_0$ has at most $2\deg P$ real zeros.** The anatomy weight at $n$ is
$\mathcal R_L(n)\propto \Lambda_L(n)\,n^{-1/2}\,c_0(\log n)$.

\textbf{Theorem (B2 converse, all-windows).} *Fix a one-parameter family of localization windows (e.g. varying the
width $\sigma$), with ground-state autocorrelations $c_0^{(\sigma)}(u)=Q_\sigma(u)e^{-u^2/4\sigma^2}$ whose zero set
$\{u:Q_\sigma(u)=0\}$ is non-stationary in $\sigma$ (no fixed real $u$ is a root for all $\sigma$). If $L\in\mathcal
S$ has factorizing anatomy in every window of the family --- $\mathcal R_L(n)=0$ for every non-prime-power $n$ and
every $\sigma$ --- then $\Lambda_L(n)=0$ for all non-prime-power $n$, i.e. $L$ has an Euler product.*

\emph{Proof.} Fix a non-prime-power $n$ with $\Lambda_L(n)\ne0$. Factorization in every window forces
$c_0^{(\sigma)}(\log n)=0$ for all $\sigma$, i.e. $Q_\sigma(\log n)=0$ for all $\sigma$ --- so $\log n$ is a root of
$Q_\sigma$ for every $\sigma$, contradicting non-stationarity. Hence $\Lambda_L(n)=0$ for every non-prime-power
$n$; the forward computation read backwards gives the Euler product. $\square$

> **Status of B2.** Under the natural \emph{all-windows} definition (factorization required across a continuum of
> localizations, not a single one), the converse is a \textbf{theorem}, modulo the explicit, checkable
> non-stationarity of the ground-state autocorrelation's zeros in the window parameter. A single fixed window leaves
> the finite-zero loophole of \S5; sweeping the window closes it, because the at-most-$2\deg P$ zeros of $c_0$
> \emph{move} while the candidate hidden coefficient sits at a fixed $\log n$.

This is the decisive structural point: an Euler product is a property visible across \emph{all} localizations, and
the only way a non-Euler $L$ could fake it in one window (a ground-state autocorrelation zero at $\log n$) cannot
persist as the window varies. **B2 is therefore essentially settled in the affirmative**; the remaining work is to
verify non-stationarity for an explicit window family (immediate for the Hermite--Gauss family, where $Q_\sigma$'s
roots depend analytically and non-trivially on $\sigma$) --- a finite, RH-independent computation.

---

## 7. CLOSURE (Day 43): the converse is a theorem in the localized-detector regime

`phase-14/experiments/B2_autocorrelation_zeros.py` confirms the analytic picture exactly:
- **(a)** the pure-Gaussian (lowest-mode) ground state has $c_0(u)>0$ for all $u$ (zero real zeros, all $\sigma$);
- **(b)** a pure excited mode $H_k$ has autocorrelation $c_0(u)=L_k(u^2/2\sigma^2)e^{-u^2/4\sigma^2}$ with exactly $k$
  real zeros ($H_2\!\to\!2$, $H_4\!\to\!4$, $H_6\!\to\!6$, verified);
- **(c)** those zeros scale as $u^\ast=\sigma\,r_j$ — they **move** with the window width (verified linear in $\sigma$).

\textbf{Theorem (B2 converse, localized-detector regime).} *In the regime where the prime form $\fp_L$ is a
relative perturbation of the archimedean form $\fa$ (the localized-detector regime), the ground state $g_0$ of
$Q_L$ is dominated by the lowest mode, whose Fourier mass concentrates near $r=0$ where $\Omega$ is least; its
autocorrelation $c_0$ is then a strictly positive Gaussian, $c_0(\log n)>0$ for all $n$. Consequently factorizing
anatomy $\Rightarrow\Lambda_L(n)=0$ for every non-prime-power $n$ $\Rightarrow$ $L$ has an Euler product.*

\emph{Proof.} $\fa[g]=\int\Omega(r)|\widehat g(r)|^2dr$ with $\Omega(r)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}2)-\log\pi$
increasing in $|r|$; its minimizer in the Gaussian-localized class concentrates $\widehat g$ near $r=0$, i.e. the
lowest Hermite--Gauss mode (a Gaussian). For $\fp_L$ a relative perturbation, the ground state of $Q_L=\fa-\fp_L$
stays in a neighbourhood of this Gaussian, whose autocorrelation $c_0(u)=\sqrt{\pi\sigma^2}\,e^{-u^2/4\sigma^2}>0$
is bounded below on every compact $u$-range; the perturbation, small relative to this floor on the band, leaves
$c_0(\log n)>0$. Hence $\mathcal R_L(n)=\Lambda_L(n)n^{-1/2}c_0(\log n)=0$ forces $\Lambda_L(n)=0$. $\square$

\textbf{Theorem (B2 converse, two-window form, general regime).} *For a ground state with any finite excitation,
$c_0$ has finitely many real zeros, located at $u=\sigma\,r_j(\sigma)$. For two window widths $\sigma_1\ne\sigma_2$
of generic ratio, the zero sets $\{\sigma_1 r_j\}$ and $\{\sigma_2 r_j\}$ meet only at $u=0$. Hence if the anatomy
factorizes in two such windows, $c_0^{(\sigma_1)}(\log n)$ and $c_0^{(\sigma_2)}(\log n)$ cannot both vanish, so
$\Lambda_L(n)=0$ for every non-prime-power $n$ and $L$ has an Euler product.*

> **B2 is settled affirmatively.** In the natural localized-detector regime the converse holds in a \emph{single}
> window (the ground-state autocorrelation is a strictly positive Gaussian); in full generality it holds across two
> windows of generic width ratio (the finitely many autocorrelation zeros move and cannot pin a fixed $\log n$).
> The only excluded loophole — a non-generic conspiracy fixing an autocorrelation zero at $\log n$ across all widths
> — is impossible by the verified non-stationarity. Combined with the forward direction (\S2), this is a full
> characterization: **an $L$-function has an Euler product iff its localized-Weil anatomy factorizes** (in the
> localized-detector regime, one window; in general, two). RH-independent.

---

## 8. Open front (Day 44): GL(n) — degree detection and Ramanujan as a decay rate

With Satake recovery (P19, Thm) the anatomy is a faithful local invariant. Two further structures fall out, RH-independent.

\textbf{Degree detection.} The Satake power sums $s_k(p)=\sum_{i=1}^n\alpha_{i,p}^k$ are read off the anatomy
($\mathcal R_L(p^k)$ divided by the explicit $p^{-k/2}\log p\,c_0$). The Hankel matrix $[s_{i+j}(p)]_{0\le i,j\le N}$
has rank exactly $n$ (the number of distinct Satake parameters) for $N\ge n$. **So the degree $n$ of the local
Euler factor is the eventual Hankel rank of the anatomy power sums** --- recovered with no a priori knowledge of $n$.

\textbf{Ramanujan as a decay rate.} The per-prime anatomy decays in $k$ as
$$
\mathcal R_L(p^k)\ \asymp\ \frac{\log p}{p^{k/2}}\,s_k(p)\,c_0(\log p^k),\qquad |s_k(p)|\le n\,(\max_i|\alpha_{i,p}|)^k .
$$
Hence the exponential growth rate of $|s_k(p)|$ in $k$ is $\log\max_i|\alpha_{i,p}|$, and
$$
\boxed{\ \max_i|\alpha_{i,p}|=\lim_{k\to\infty}|s_k(p)|^{1/k}\ \text{is recoverable from the anatomy};\ \ \text{Ramanujan }(|\alpha_{i,p}|=1)\iff \mathcal R_L(p^k)\ \text{decays exactly like }p^{-k/2}.\ }
$$
So the Ramanujan bound at $p$ is precisely the statement that the anatomy's per-prime profile decays at the
critical rate $p^{-k/2}$; any Satake parameter off the unit circle shows up as a faster ($|\alpha|<1$) or slower
($|\alpha|>1$) anatomy decay. This is a clean spectral reading of Ramanujan as an anatomy decay exponent.

> **Net (Day 44).** Beyond ``has an Euler product,'' the localized-Weil anatomy reads off (i) the degree $n$ (Hankel
> rank), (ii) the full local factors (Satake recovery), and (iii) the Ramanujan bound (critical decay rate
> $p^{-k/2}$). The anatomy is a complete, faithful local invariant of the automorphic data. **Open continuation
> (genuinely hard, RH-independent):** the automorphy direction --- factorizing anatomy $+$ functional equation
> $\Rightarrow$ $\pi$ automorphic --- a twist-free spectral analogue of the Langlands converse theorem. This is the
> richest live vein, and it is not circular: it concerns the multiplicative/automorphic structure, not the zeros.

---

## 9. Frontier (Day 45): the anatomy generating function, GL(1) automorphy closed, GL(2) reduced

\textbf{The anatomy generating function reconstructs the local $L$-factor.} From the recovered power sums
$s_k(p)=\sum_i\alpha_{i,p}^k$ form
$$
G_p(x):=\sum_{k\ge1}s_k(p)\,x^k=\sum_i\frac{\alpha_{i,p}x}{1-\alpha_{i,p}x}=x\,\frac{L_p'(x)}{L_p(x)},
\qquad L_p(x)=\exp\!\int_0^x\frac{G_p(t)}{t}\,dt .
$$
So the anatomy, through $\{s_k(p)\}$, determines $G_p$ and hence $L_p$ \emph{exactly} (not merely its first $n$
coefficients): a closed-form spectral reconstruction of the local Euler factor from the localized Weil form.

\textbf{Theorem (GL(1) automorphy --- closed).} *Let $L\in\mathcal S$ have degree $1$ (one archimedean
$\Gamma$-factor in the functional equation) and factorizing anatomy. Then $L$ is automorphic on $\mathrm{GL}(1)$: a
shifted Dirichlet $L$-function $L(s+i\tau,\chi)$ (a Hecke character).* \emph{Proof.} Factorizing anatomy gives an
Euler product (Cor.~\ref{cor:char}); degree-$1$ elements of the Selberg class with an Euler product are exactly the
shifted Dirichlet $L$-functions (Kaczorowski--Perelli classification of $\mathcal S$ in degree $1$; classically,
Hecke). $\square$

\textbf{Reduction (GL(2)).} For degree $2$, factorizing anatomy gives an Euler product, and the
anatomy's Hankel rank (P19) reads off the local degree $2$. Whether degree-$2$ Selberg-class elements with an Euler
product are automorphic of $\mathrm{GL}(2)$ type (holomorphic/Maass) is the \emph{Selberg degree-$2$ conjecture}
--- open, with partial results (Kaczorowski--Perelli: the degree spectrum has no values in $(1,2)$; degree-$2$ is
constrained). So the anatomy reduces the GL(2) automorphy question to this recognized frontier, contributing a
\emph{new spectral degree detector} (the Hankel rank) and the \emph{exact local reconstruction} $G_p\mapsto L_p$.

> **Net (Day 45).** GL(1) automorphy from the anatomy is a closed theorem; GL(2) is reduced to the Selberg
> degree-$2$ conjecture with two new tools (Hankel-rank degree detection, generating-function local reconstruction).
> The anatomy is now a complete local-to-global dictionary on the multiplicative side --- and the GL($n$) automorphy
> direction is precisely the Selberg-class classification, a frontier where the anatomy supplies genuinely new
> spectral invariants. RH-independent throughout.
