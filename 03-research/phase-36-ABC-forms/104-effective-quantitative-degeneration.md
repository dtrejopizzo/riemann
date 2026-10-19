# Doc 104 — Effective $SR_d$: quantitative degeneration as $d\to0$

**Phase 36 — Forms A/B/C ·**
**Answers: Problem 8.1 (Form C) of P41 (`06-papers/P41-exhaustion-1d-propagation/main.tex`, §Form C)**
**Main input: Doc 102 (`phase-35-five-fronts/102-audit-of-the-bagchi-criterion-strong-recurrence.md`), §§3–6**

---

## 0. Executive summary

Problem 8.1 of P41 poses a dichotomy: if the constants of the unconditional proofs of
$(\mathrm{SR}_d)$ degenerate exponentially ($e^{-c/|d|}$) as
$d\to0$, the line closes as quantified MW-2; if they degenerate polynomially in $1/|d|$,
there is genuine tension with the Rouché argument. This document resolves the problem, and the
result is finer than either branch: **the dichotomy, as posed, is false
— and the line closes all the same, for a more precise reason than either branch.**

Findings:

1. **The limiting density does not degenerate.** There exists $d_0(\varepsilon)>0$ such that for all
   $0<|d|<d_0(\varepsilon)$ the lower density $\delta(d,\varepsilon)$ of
   $(\mathrm{SR}_d)$ admits a lower bound $\delta_*(\varepsilon)>0$ **uniform in
   $d$** (Theorem 4.1, with a declared and bounded technical gap). Moreover: below
   $d_0(\varepsilon)$ **all of diophantine theory disappears** — rational, algebraic, and
   transcendental become indistinguishable at precision $\varepsilon$ (Proposition 3.1).
   Baker and the six exponentials theorem only work in the band $|d|\ge d_0(\varepsilon)$.
2. **What degenerates is the scale, and it degenerates linearly.** The first $T$ from which
   positive density is visible satisfies $T_0(d,\varepsilon)\asymp
   C(\varepsilon)/|d|$: upper bound by effective equidistribution (Theorem 4.1), lower
   bound $\ge \eta/|d|$ unconditional-structural, and, under $\neg$RH with $K$ anchored at
   the zero, genuine (Proposition 4.3). **Polynomial — in fact linear — degradation in
   $1/|d|$**: the "tension" branch of the dichotomy.
3. **And yet there is no tension.** The Rouché argument does not need
   $(\mathrm{SR}_d)$ at large scale: it needs its density **inside the anchored window**
   $J_d=\{\tau: d\tau\approx\gamma_0\}$, of measure $\asymp 1/|d|$ — exactly the scale
   where the effective theorem still delivers nothing and where the slow copy
   $\zeta(s+id\tau)$ is **frozen**. There the statement collapses to approximating the fixed
   target $\zeta(\cdot+i\gamma_0)$, which has a zero: forbidden target, provably exactly $0$
   density (Bagchi's Module 5, Hurwitz). The gap is not a rate: it is the binary
   wall $0$ vs $>0$.
4. **The exact quantitative gap (Theorems 5.2–5.3).** With $\sigma=\beta_0-3\eta$ and
   $\kappa(\sigma)>0$ the exponent of the zero-density theorem
   ($\kappa=(2\sigma-1)^2$ with Carlson; $\kappa=(2\sigma-1)/(2-\sigma)$ with Ingham):
   anchored density $\ge c\,|d|^{\kappa'}$ with $\kappa'<\kappa$ along a sequence
   $d\to0$ **would imply RH** (Theorem 5.2); but under $\neg$RH the true anchored
   density is bounded by $C\,|d|^{\kappa}$ — **the same exponent** (Theorem 5.3).
   What is necessary and what is maximally possible differ only by constants, and what is
   provable is $0$. Improving the zero-density theorem moves both sides at once: the
   mechanism is **self-blocking**. This is quantified MW-2.
5. **A moving $d=d(T)$ evades nothing (Lemma 6.1, complementarity):** anchoring requires
   $|d(T)|\,T=O(1)$ (frozen slow copy ⟹ collapse to $\mathrm{SR}_0$); equidistributing
   the slow copy requires $|d(T)|\,T\to\infty$ (no anchor ⟹ at most $o(T)$ zeros, no
   contradiction). The two regimes are exhaustive and disjoint for every function
   $d(T)$.

**VERDICT: ROUTE CLOSED** — with the dichotomy of 8.1 corrected: polynomial
(linear) degradation of the scale, none at all in the density, and clean closure because the quantity
Rouché needs is neither of the two: it is the density in the anchored window, where the
wall is binary (Hurwitz), not quantitative. §9.

---

## 1. The problem, notation, and verified state of the art

### 1.1 Statements

For $d\in\mathbb{R}$, $K\subset D(1/2,1)=\{s:1/2<\mathrm{Re}\,s<1\}$ compact with
connected complement and $\varepsilon>0$:

$$(\mathrm{SR}_d)\qquad
\liminf_{T\to\infty}\ \frac1T\,\mathrm{meas}\Big\{\tau\in[0,T]\ :\ \sup_{s\in K}\big|\zeta(s+i\tau)-\zeta(s+id\tau)\big|<\varepsilon\Big\}\ >\ 0.$$

We write $\delta(d,\varepsilon;K)$ for the liminf and $\delta(d,\varepsilon)$ when $K$
is fixed. $(\mathrm{SR}_0)=(\mathrm{SR})$ is RH (Bagchi 1987; Doc 102, Theorem 2.2).

### 1.2 State of the art (verified in this session)

- $d$ **algebraic irrational**: $(\mathrm{SR}_d)$ unconditional — Nakamura, *The
  generalized strong recurrence for non-zero rational parameters*, Arch. Math. **95**
  (2010), 549–555 (the algebraic part), via joint universality + **Baker's theorem**.
- $d$ **transcendental**: Pańkowski, via the **six exponentials theorem**
  (presented in Matsumoto, arXiv:1407.4216, §9).
- $d=a/b$ **rational**, $(a,b)=1$, $|a-b|\neq1$: Nakamura–Pańkowski, Arch. Math. **99**
  (2012), 43–47 (corrigendum; verified via arXiv:1203.1393: the corrigendum proves
  it for $\zeta$ for $|a-b|\neq1$ and for $\log\zeta$ for all $d\neq0$). The case $|a-b|=1$ was
  resolved later by Pańkowski for every rational $d\neq0,\pm1$ [reported in secondary
  sources; the specific paper NOT VERIFIED in full text].
- **Short intervals**: Garunkštis et al. (Symmetry **17** (2025), art. 2075) show
  that self-approximation **in short intervals** with $d=0$ is again
  RH-equivalent [verified only at the abstract level; NOT VERIFIED in detail]. This
  is consistent with — and anticipates — §5.4 of this document.

**Remark 1.1 (rationals near $0$ are not problematic).** If $d=a/b$ with
$0<|d|<1/2$ and $(a,b)=1$, then $|a|<b/2$, so $|a-b|>b/2\ge1$. The technical case
$|a-b|=1$ (the only one that was open) **does not occur in any neighborhood of $d=0$**: for
the question of this document, the 2012 corrigendum already covers all the relevant
rationals. ∎

### 1.3 What exactly Form C asks for

P41, Problem 8.1: behavior of the proof constants as $d\to0$;
dichotomy $e^{-c/|d|}$ (MW-2 closure) vs polynomial (tension with Rouché). The
relevant constants are two, and the document's first result is that they behave oppositely:

- $\delta(d,\varepsilon)$ — the lower density (does it sink as $d\to0$?);
- $T_0(d,\varepsilon)$ — the scale from which the density becomes visible
  (equivalently, the first guaranteed $\tau$).

---

## 2. Anatomy of the proof of $(\mathrm{SR}_d)$: where $d$ enters (question i)

### 2.1 The five modules in bivariate form

The proof of $(\mathrm{SR}_d)$ is the Bagchi machinery (Doc 102, §3) run on the
**pair** of shifts. Let $\Omega=\prod_p\mathbb{T}_p$ be the Bohr torus. The dynamical
object is the orbit
$$\tau\ \longmapsto\ \big(\,(p^{-i\tau})_p,\ (p^{-id\tau})_p\,\big)\ \in\ \Omega\times\Omega,$$
with closure $H_d:=\overline{\{\cdot\}}\le\Omega\times\Omega$, a closed connected subgroup.
The characters of $\Omega\times\Omega$ are pairs $(n,m)$ of integer vectors of finite
support indexed by primes, and they act on the orbit by $e^{-i\tau\lambda_{n,m}(d)}$ with

$$\boxed{\ \lambda_{n,m}(d)\ =\ \Lambda_0(n)+d\,S(m),\qquad
\Lambda_0(n)=\sum_p n_p\log p,\quad S(m)=\sum_p m_p\log p.\ }$$

All of the theory's dependence on $d$ enters through the **frequency spectrum**
$\{\lambda_{n,m}(d)\}$ and the **lattice of relations**
$R_d=\{(n,m):\lambda_{n,m}(d)=0\}$, which determines $H_d$ (the annihilator of $R_d$).

- **Modules 1–2 (torus and flow):** the bivariate flow is translation by the
  one-parameter subgroup of frequencies $\{\log p\}\cup\{d\log p\}$; it is uniquely ergodic on
  $H_d$ (rotation of a compact group, Walters GTM 79).
- **Module 3 (random elements):** the pair $(\zeta(s,\omega_1),\zeta(s,\omega_2))$
  with $(\omega_1,\omega_2)\sim$ Haar$(H_d)$.
- **Module 4 (limit theorem):** the empirical statistics of the pair of shifts converge
  to the law of the random pair. Inputs: mean squares of $\zeta$ in $\sigma>1/2$
  (each copy separately, **independent of $d$** except for rescaling the slow
  copy, §4) and Birkhoff over $H_d$.
- **Module 5 (support + positivity):** the self-approximation event has
  positive limiting probability. Here the situation is **better** than in universality: the
  target of the pair is the **diagonal** ("the two copies close to each other"), not an
  external function. The point $(\omega_0,\omega_0)$ (trivial phases in both copies)
  belongs to $H_d$ for **every** $d$ (it is the orbit at $\tau=0$), and in a neighborhood of
  $(\omega_0,\omega_0)$ the two truncated Euler products are both close to
  $\zeta_X(s)$, which **does not vanish**. The Hurwitz wall is not touched — as long as the
  target is the diagonal and not $\zeta$ itself. (This is the structural reason why
  $(\mathrm{SR}_d)$, $d\neq0$, is provable and $(\mathrm{SR}_0)$ is not: in
  $(\mathrm{SR}_0)$ the second copy IS $\zeta$, with its zeros.)

### 2.2 The role of each diophantine class of $d$

The lattice $R_d$: $(n,m)\in R_d$ $\iff$ $\Lambda_0(n)=-d\,S(m)$.

**(a) $d$ algebraic irrational — Baker.** A relation with $(n,m)\neq(0,0)$ would force
$\sum_p(n_p+d\,m_p)\log p=0$, a linear combination of $\{\log p\}$ with not-all-zero
algebraic coefficients. Since $\{\log p\}$ is linearly independent over
$\mathbb{Q}$ (unique factorization), **Baker's theorem** (1966–67: linear
independence over $\mathbb{Q}$ of logarithms of algebraic numbers implies independence over
$\overline{\mathbb{Q}}$) gives a contradiction. Hence $R_d=0$, $H_d=\Omega\times\Omega$, and the
limit is the **independent pair** $(\zeta(s,\omega_1),\zeta(s,\omega_2))$, product
Haar measure.

**(b) $d$ transcendental — six exponentials.** Transcendence does NOT prevent relations:
$d=\log3/\log2$ is transcendental (Gelfond–Schneider) and satisfies $d\log2-\log3=0$. What
the **six exponentials theorem** gives: the multiplicative group
$G_d=\{r\in\mathbb{Q}_{>0}: r^d\in\mathbb{Q}\}$ has rank $\le2$. (If $r_1,r_2,r_3$
were multiplicatively independent with $r_j^d\in\mathbb{Q}$: take $x_1=1,x_2=d$
— linearly independent over $\mathbb{Q}$ since $d\notin\mathbb{Q}$ — and $y_j=\log r_j$ — l.i. by
multiplicative independence; the six numbers $e^{x_iy_j}\in\{r_j,r_j^d\}$ would all be
algebraic, contradicting the theorem.) The relations of $R_d$ are confined to a
rank-$\le2$ subgroup of "bad" primes, effectively finitely generated; Pańkowski's proof
excludes these generators from the phase game and works with the rest (Module 5's
steering only needs cofinitely many primes). $H_d$ is a subtorus of
codimension $\le2$ in the sense of characters, containing the diagonal at
$(\omega_0,\omega_0)$.

**(c) $d=a/b$ rational — large subtorus.** $R_d=\{(n,m): b\,\Lambda_0(n)+a\,S(m)=0\}
=\{(n,m)=(-a\,k,\,b\,k)\}$ (using independence of $\{\log p\}$): a lattice of infinite
rank but of **coarse index $\max(|a|,b)$**: every relation has coefficients
that are multiples of $(a,b)$. $H_d=\{(\omega^{\,b},\omega^{\,a}):\omega\in\Omega\}$. The
limit pair is $(\zeta(s,\omega^b),\zeta(s,\omega^a))$ — **dependent** — and Module 5's
positivity requires navigating the dependence; that is where the difficulty $|a-b|=1$
lived. By Remark 1.1, irrelevant near $d=0$; moreover the relation coefficients
have size $\ge b\ge 1/|d|\to\infty$ — the key point of §3.

### 2.3 The constant structure of an effective version

Any effectivization of the above scheme (not written in the literature for
$\mathrm{SR}_d$; standard structure) has three internal parameters for precision
$\varepsilon$ over $K$:

- $X(\varepsilon)$: prime truncation — $\zeta_X(s)=\prod_{p\le X}(1-p^{-s})^{-1}$
  (or a smoothed version) approximates $\zeta$ in mean square over shifts:
  $\frac1T\int_0^T\sup_K|\zeta(s+i\tau)-\zeta_X(s+i\tau)|^2\,d\tau<\varepsilon_1$ for
  $T\ge T_1(X)$. Unconditional, via second moments in $\sigma>1/2$;
  **independent of $d$** (applies to each copy; for the slow copy, see §4.1).
- $M(\varepsilon)$: maximum degree of the characters of the finite torus
  $\mathbb{T}^{2\pi(X)}$ needed to resolve the event (regularization of the
  event's indicator function by trigonometric polynomials).
- equidistribution: Weyl sums
  $\big|\frac1T\int_0^Te^{i\lambda_{n,m}(d)\tau}d\tau\big|\le\frac{2}{T\,|\lambda_{n,m}(d)|}$
  for all characters $0<\max(|n|_\infty,|m|_\infty)\le M$, support in $p\le X$,
  $(n,m)\notin R_d$.

**All the dependence on $d$ is in the third point**: lower bounds for
$|\lambda_{n,m}(d)|$ (small denominators) and the structure of $R_d$. This is exactly
where Problem 8.1 expects to find Baker. The surprise is §3.

---

## 3. The diophantine-free regime: $|d|<d_0(\varepsilon)$ (new)

**Proposition 3.1.** *Let $X\ge2$, $M\ge1$. Define*
$$d_0(X,M)\ :=\ \frac{e^{-2MX}}{4MX}.$$
*Then for every real $d$ with $0<|d|<d_0(X,M)$ and every character $(n,m)$ with support in
$p\le X$, heights $|n_p|,|m_p|\le M$, $(n,m)\neq(0,0)$:*

*(a) $\lambda_{n,m}(d)\neq0$ — there is NO relation visible at precision $(X,M)$,
whatever the diophantine class of $d$;*

*(b) quantitatively:*
$$|\lambda_{n,m}(d)|\ \ge\ \begin{cases}
\tfrac12\,e^{-2MX} & \text{if } n\neq0,\\[2pt]
|d|\,\log 2 & \text{if } n=0,\ m\neq0.
\end{cases}$$

*Proof.* If $n\neq0$: $\Lambda_0(n)=\log(A/B)$ with $A=\prod_{n_p>0}p^{n_p}$,
$B=\prod_{n_p<0}p^{-n_p}$ coprime integers, $A\neq B$ (unique factorization),
$\max(A,B)\le\prod_{p\le X}p^{M}=e^{M\theta(X)}\le e^{2MX}$. By
$|\log(A/B)|\ge|A-B|/\max(A,B)\ge1/\max(A,B)$:
$|\Lambda_0(n)|\ge e^{-2MX}$. On the other hand
$|d\,S(m)|\le|d|\,M\,\theta(X)\le|d|\cdot2MX<e^{-2MX}/2$ by the definition of $d_0$.
Hence $|\lambda_{n,m}(d)|\ge|\Lambda_0(n)|-|d\,S(m)|\ge\frac12 e^{-2MX}>0$.
If $n=0,m\neq0$: $\lambda=d\,S(m)$ and $|S(m)|\ge\log2$ (it is the $\log$ of a rational
$\neq1$ with numerator and denominator $\ge1$, the minimum being $\log2$). ∎

**Corollary 3.2 (collapse of the diophantine classes).** For $|d|<d_0(X(\varepsilon),
M(\varepsilon))=:d_0(\varepsilon)$, the finite-dimensional equidistribution that the proof
of $(\mathrm{SR}_d)$ needs at precision $\varepsilon$ **uses no diophantine
theorem whatsoever**: not Baker, not six exponentials, not the rational-subtorus analysis. The
exact relations that rational $d$ or $d=\log r_1/\log r_2$ possess have coefficients
of size $\ge c/(|d|\,X)$ (for $d=a/b$: size $\ge b\ge1/|d|$), invisible under the
truncation $(X,M)$. At fixed precision, **all classes of $d$ behave the same
as $d\to0$**. ∎

**Interpretation.** Problem 8.1 presupposes that the degradation as $d\to0$ comes from
transcendence theory (Baker constants $C(n)\,h(d)\,\prod\log A_i$). Proposition
3.1 shows it does not: transcendence theory governs the regime $|d|\ge d_0(\varepsilon)$
(fixed, $\varepsilon\to0$), not the regime $d\to0$ ($\varepsilon$ fixed). In the limit
$d\to0$ the only small frequency is the **trivial** one: the pure characters of the slow
copy, $\lambda_{0,m}=d\,S(m)$, linear in $d$. The degradation is **kinematic, not
arithmetic**.

### 3.3 The regime $|d|\ge d_0(\varepsilon)$: where Baker actually lives (question ii, diophantine part)

To complete the answer to (i)–(ii) in the complementary regime (which is NOT the limit
$d\to0$, but Problem 8.1 asks for the translation):

- **$d=a/b$ rational, or algebraic:** $b\,\lambda_{n,m}(d)=b\,\Lambda_0(n)+a\,S(m)$ is
  a linear form in $\{\log p\}_{p\le X}$ with integer coefficients of size
  $\le\max(|a|,b)\,M$. Baker–Wüstholz (1993): for a nonzero linear form
  $\Lambda=\sum_{i=1}^{N} b_i\log\alpha_i$ with $\alpha_i$ algebraic and $b_i$ integers,
  $$\log|\Lambda|\ \ge\ -\,C(N,D)\,h'(\alpha_1)\cdots h'(\alpha_N)\,\log B,\qquad
  C(N,D)=18\,(N+1)!\,N^{N+1}(32D)^{N+2}\log(2ND),$$
  with $B=\max|b_i|$, $D$ the degree of the field, $h'$ modified heights. Here $N=\pi(X)$,
  $\alpha_i=p_i$, $h'(p)\asymp\log p$, $B\le\max(|a|,b)M\asymp M/|d|$. Result:
  $$|\lambda_{n,m}(d)|\ \ge\ \exp\big(-C(\varepsilon)\,\log(M/|d|)\big)\ =\
  c(\varepsilon)\,|d|^{\,C(\varepsilon)},\qquad
  C(\varepsilon)=C(\pi(X),1)\,\textstyle\prod_{p\le X}\log p,$$
  **polynomial in $1/|d|$** with a gigantic exponent $C(\varepsilon)$
  (super-exponential in $X(\varepsilon)$) but independent of $d$. The diophantine
  degradation, where it exists, is polynomial — never $e^{-c/|d|}$.
- **$d$ transcendental:** there is no general irrationality measure; there exist
  "Liouville-logarithmic type" transcendental $d$ (extremely well approximable by
  quotients $\Lambda_0(n)/S(m)$) for which $T_0(d,\varepsilon)$ at FIXED $d$ is
  arbitrarily large: the six-exponentials proof is **ineffective** and cannot be made
  effective uniformly. But again: for $|d|<d_0(\varepsilon)$ this is irrelevant
  (Prop. 3.1 is unconditional and uniform).

---

## 4. The real quantitative degeneration (question ii)

### 4.1 Upper bound: the uniform effective theorem

**Theorem 4.1 (effective structure of $\mathrm{SR}_d$ near $d=0$).** *Fix $K\subset
D(1/2,1)$ compact with connected complement and $\varepsilon>0$. There exist
$d_0(\varepsilon)>0$, $\delta_*(\varepsilon)>0$ and $C(\varepsilon)<\infty$ such that for
every real $d$ with $0<|d|<d_0(\varepsilon)$:*

*(a) $\delta(d,\varepsilon)\ \ge\ \delta_*(\varepsilon)$ — **uniform in $d$**: the
lower density does NOT tend to $0$;*

*(b) the density is visible from scale $C(\varepsilon)/|d|$: for every
$T\ge C(\varepsilon)/|d|$,*
$$\frac1T\,\mathrm{meas}\big\{\tau\in[0,T]:\ \sup_K|\zeta(s+i\tau)-\zeta(s+id\tau)|<\varepsilon\big\}\ \ge\ \tfrac12\,\delta_*(\varepsilon).$$

*Proof sketch (with declared gaps).* (1) Mean-square reduction: with
$X=X(\varepsilon)$, both copies are replaced by $\zeta_X$ outside a set of
$\tau$ of density $<\delta_*/10$; for the fast copy this holds for $T\ge
T_1(\varepsilon)$; for the slow copy, the change of variable $u=d\tau$ gives
$\frac1T\int_0^T f(d\tau)\,d\tau=\frac1{|d|T}\int_0^{|d|T}f(u)\,du$, so that the
same unconditional input applies as soon as $|d|T\ge T_1(\varepsilon)$ — first
source of the factor $1/|d|$. (2) The truncated event depends on the $2\pi(X)$
coordinates $(p^{-i\tau},p^{-id\tau})_{p\le X}$; it is regularized by trigonometric
polynomials of degree $\le M(\varepsilon)$ (smoothing of the event's boundary). (3) Weyl + Proposition 3.1:
all nontrivial characters have
$|\lambda|\ge\min(\frac12e^{-2MX},\,|d|\log2)$, so the empirical means of the
degree-$\le M$ polynomials are within distance $<\delta_*/10$ of their Haar
means on $\mathbb{T}^{2\pi(X)}\times\mathbb{T}^{2\pi(X)}$ as soon as
$T\ge C'(\varepsilon)/|d|$ — second, and dominant, source of the factor $1/|d|$. Note:
by Prop. 3.1 the finite-dimensional limiting measure is **full Haar** for EVERY
$0<|d|<d_0$, rational included — the subtorus $H_d$ is $(X,M)$-dense. (4) $d$-independent
positivity: the limiting event contains the neighborhood
$\{(\vec\theta_1,\vec\theta_2):|\theta_{j,p}|<\rho(\varepsilon)\ \forall p\le X\}$ of the
diagonal identity, over which both truncated products are within $<\varepsilon/4$ of
$\zeta_X(s)$ (which does not vanish and need not vanish: the target is the diagonal, §2.1,
Module 5); its Haar measure is $\delta_*(\varepsilon):=\prod_{p\le X}(\rho/\pi)^2>0$, with no
$d$-dependence. ∎(sketch)

**Declared TECHNICAL GAP (G4.1):** steps (1) and (2) — making the mean-square
approximation and the regularization of the event's boundary effective with explicit
constants — are standard but lengthy and are not written in the literature for the pair
$(\tau,d\tau)$; the new and fully proved claim here is the **structure of
the dependence on $d$**: $d$ enters ONLY through (i) the rescaling $|d|T\ge T_1$ and (ii) the
frequencies of Prop. 3.1, both linear in $1/|d|$. No constant in (1)–(2) nor
positivity (4) depends on $d$. Bound (a), as a fully formal theorem, remains
conditional on G4.1; we classify it as routine, not open in a strong sense.

### 4.2 Direct answer to question (ii)

- **Does $\delta(d,\varepsilon)\to0$ as $d\to0$? NO.** It is uniformly positive on
  $0<|d|<d_0(\varepsilon)$ (Theorem 4.1(a)). The intuition of Problem 8.1 (the density
  sinks with $d$) is false: the limiting measure does not even change with $d$ in that range.
- **First guaranteed $\tau$:** $\tau(d,\varepsilon)\le C(\varepsilon)/|d|$, and this
  order is optimal (§4.3). **Linear degradation in $1/|d|$** — the mildest end
  of the "polynomial" branch of the dichotomy.
- The non-uniformity of the double limit is thereby quantified:
  $\lim_{d\to0}\lim_{T\to\infty}$ (= $\delta_*>0$) $\neq$
  $\lim_{T\to\infty}\lim_{d\to0}$ (= density of $\mathrm{SR}_0$, RH). The exchange
  fails exactly because the useful range of $T$ starts at $C(\varepsilon)/|d|\to\infty$.

### 4.3 Lower bound for the scale: the linearity is exact

**Proposition 4.3 (under $\neg$RH, anchoring $K$ at the zero, the scale $1/|d|$ is
genuine).** *Suppose $\zeta$ has a zero $\rho_0=\beta_0+i\gamma_0$ with
$\beta_0>1/2$, $\gamma_0>0$. Let $\eta>0$ with $\overline B(\rho_0,4\eta)\subset
D(1/2,1)$, $\zeta$ having no other zeros in $\overline B(\rho_0,4\eta)$, and
$K=\overline B(\rho_0,3\eta)$, $\varepsilon\le\frac14\min_{2\eta\le|w-\rho_0|\le4\eta}|\zeta(w)|$.
Then there exists $\eta_1>0$ such that for every $d\neq0$ and every $T\le\eta_1/|d|$:*
$$\frac1T\,\mathrm{meas}\big\{\tau\in[0,T]:\sup_K|\zeta(s+i\tau)-\zeta(s+id\tau)|<\varepsilon\big\}
\ \le\ \frac{C_K\,N(\beta_0-3\eta,\,T+\gamma_0+3\eta)}{T}\ =\ o(1)\quad(T\to\infty).$$

*Proof.* For $T\le\eta_1/|d|$ and $\tau\in[0,T]$: $|d\tau|\le\eta_1$. By uniform
continuity of $\zeta$ on a compact neighborhood of $K$, choose $\eta_1$ with
$\sup_K|\zeta(s+id\tau)-\zeta(s)|<\varepsilon$ for $|d\tau|\le\eta_1$. Then the
event implies $\sup_K|\zeta(s+i\tau)-\zeta(s)|<2\varepsilon$; since the circle
$|w-\rho_0|=3\eta$ is contained in the ring $2\eta\le|w-\rho_0|\le4\eta$, the choice
of $\varepsilon$ gives $2\varepsilon\le\frac12\min_{\partial K}|\zeta|<\min_{\partial K}|\zeta|$,
and by Rouché $\zeta(\cdot+i\tau)$ has a zero in
$B(\rho_0,3\eta)$, i.e. $\zeta$ has a zero with real part $>\beta_0-3\eta>1/2$ and
height in $[\tau+\gamma_0-3\eta,\tau+\gamma_0+3\eta]$. Each zero absorbs $\tau$-measure
$\le6\eta$; the count gives measure $\le6\eta\,N(\beta_0-3\eta,T+\gamma_0+3\eta)=o(T)$ by
Carlson (Doc 102, Theorem 2.3). ∎

That is: with $K$ anchored at the hypothetical zero, **below scale $\eta_1/|d|$
the density is $o(1)$** (the event collapses to local $\mathrm{SR}_0$, forbidden), and
above $C(\varepsilon)/|d|$ it is $\ge\delta_*/2$ (Theorem 4.1 — with admissible $K$ and $\varepsilon$;
note that Theorem 4.1 requires nothing about zeros). The transition is real and
occurs at $T\asymp1/|d|$: **the quantitative degeneration of $\mathrm{SR}_d$ as $d\to0$
is exactly linear in $1/|d|$, neither exponential nor better than linear.**

---

## 5. The coupling with Rouché: the quantitative gap (question iii)

### 5.1 Why global $(\mathrm{SR}_d)$ does not feed the amplifier

Bagchi's amplifier (Doc 102, §4.2, asset A1) needs an **anchor**: a fixed disk
around the hypothetical zero $\rho_0$ and comparisons of $\zeta(\cdot+i\tau)$ with
a function that **has a zero in that disk with controlled modulus on the boundary**. In
$(\mathrm{SR}_d)$ both copies escape: $\tau\to\infty$ and $d\tau\to\infty$. The slow
copy is only near the anchor when $d\tau\in[\gamma_0-\eta,\gamma_0+\eta]$, i.e.

$$\tau\in J_d:=\Big[\frac{\gamma_0-\eta}{d},\ \frac{\gamma_0+\eta}{d}\Big],
\qquad \mathrm{meas}(J_d)=\frac{2\eta}{d}\quad(d>0\ \text{WLOG}).$$

**Lemma 5.1.** The fraction of $[0,T]$ useful for anchoring is
$\mathrm{meas}(J_d)/T=2\eta/(dT)\to0$ for fixed $d$. The global positive density of
$(\mathrm{SR}_d)$ — however large and uniform it may be — **says nothing** about the measure of the
event inside $J_d$: a liminf over $[0,T]$ is compatible with zero measure in
any sub-window of null density. ∎

That is why not even the strongest conceivable version of Theorem 4.1 (perfect
constants, huge $\delta_*$, exact $T_0=1/|d|$) produces tension: Rouché does not consume the
quantity the theorem delivers. The right question is: what density **inside
$J_d$** would make the argument work?

### 5.2 Sufficiency: the threshold $|d|^{\kappa}$

Notation: for $\sigma\in(1/2,1)$ let $\kappa(\sigma)>0$ be an admissible zero-density
exponent, i.e. $N(\sigma,T)\ll_\sigma T^{1-\kappa(\sigma)}$. Unconditional values:
Carlson (1920) gives $\kappa(\sigma)=(2\sigma-1)^2-\epsilon$ (from
$N\ll T^{4\sigma(1-\sigma)+\epsilon}$); Ingham (1940),
$N\ll T^{3(1-\sigma)/(2-\sigma)}\log^5T$, gives
$\kappa(\sigma)=\frac{2\sigma-1}{2-\sigma}-\epsilon$.

**Theorem 5.2 (anchored density sufficient for RH).** *Suppose $\neg$RH, with zero
$\rho_0=\beta_0+i\gamma_0$, $\beta_0>1/2$, $\gamma_0>0$. Let $\eta,K,\varepsilon$ be as
in Proposition 4.3 with additionally $\eta<(\beta_0-\tfrac12)/4$, and
$\sigma:=\beta_0-3\eta>\tfrac12$. If there existed $c>0$, $\kappa'<\kappa(\sigma)$ and a
sequence $d_k\downarrow0$ such that*
$$\mathrm{meas}\Big\{\tau\in J_{d_k}:\ \sup_{s\in K-i\gamma_0+id_k\tau\ \text{(see proof)}}
|\zeta(s+i\tau)-\zeta(s+id_k\tau)|<\varepsilon\Big\}\ \ge\ c\,d_k^{\,\kappa'}\cdot\mathrm{meas}(J_{d_k}),$$
*then this contradicts $N(\sigma,T)\ll T^{1-\kappa(\sigma)}$. Consequently, such a
bound — uniform over a sequence $d\to0$, proved unconditionally —
would imply RH.*

*Proof.* Fix $k$, write $d=d_k$, and take the fixed compact
$K_0=\overline B(\beta_0+i0,3\eta)$ translated: for $\tau\in J_d$ set
$t:=d\tau\in[\gamma_0-\eta,\gamma_0+\eta]$. The function $w\mapsto\zeta(w)$ has its zero
$\rho_0$ at distance $\le\eta$ from the center $\beta_0+it$ of the disk
$B(\beta_0+it,3\eta)$, and its boundary falls in the ring $2\eta\le|w-\rho_0|\le4\eta$, where
$|\zeta|\ge4\varepsilon$. (Formally: the sup in the statement is over
$s\in\overline B(\beta_0,3\eta)$ evaluating $\zeta(s+id\tau)$ and $\zeta(s+i\tau)$ — a
fixed compact set, the statement is legitimate as an instance of localized self-approximation.)
For each good $\tau$, on $|s-\beta_0|=3\eta$:
$|\zeta(s+i\tau)-\zeta(s+it)|<\varepsilon<|\zeta(s+it)|$, and Rouché gives
$\zeta(\cdot+i\tau)$ at least one zero in $B(\beta_0,3\eta)$: a zero of $\zeta$ with
real part $\ge\sigma$ and height in $[\tau-3\eta,\tau+3\eta]$. The good measure is
$\ge c\,d^{\kappa'}\cdot\frac{2\eta}{d}$ and each zero absorbs measure $\le6\eta$:
$$\#\{\text{zeros}\}\ \ge\ \frac{c}{3}\,d^{\,\kappa'-1},\qquad\text{heights}\ \le\
T':=\frac{\gamma_0+\eta}{d}+3\eta\ \le\ \frac{2\gamma_0}{d}\ \ (d\ \text{small}).$$
Hence $N(\sigma,T')\ge\frac{c}{3}d^{\kappa'-1}\ge c'\,(T')^{1-\kappa'}$. But
$N(\sigma,T')\ll(T')^{1-\kappa(\sigma)}$ and $\kappa'<\kappa(\sigma)$: contradiction for
$k$ large. ∎

### 5.3 The ceiling: under $\neg$RH the true anchored density has the SAME exponent

**Theorem 5.3 (unconditional-in-the-window ceiling).** *Under $\neg$RH and with the
configuration of Theorem 5.2, for every sufficiently small $d>0$ the TRUE anchored
density satisfies*
$$\frac{1}{\mathrm{meas}(J_d)}\,\mathrm{meas}\Big\{\tau\in J_d:\ \sup_{|s-\beta_0|\le3\eta}
|\zeta(s+i\tau)-\zeta(s+id\tau)|<\varepsilon\Big\}\ \le\ \frac{6\eta\,N(\sigma,2\gamma_0/d)}{2\eta/d}
\ \ll\ d^{\,\kappa(\sigma)}.$$

*Proof.* The same Rouché transport as in the previous proof (which only uses the
lower bound for $|\zeta|$ on the ring, available by the choice of $\eta,\varepsilon$):
each good $\tau$ in $J_d$ produces a zero of $\zeta$ with $\mathrm{Re}\ge\sigma$ and
height $\le2\gamma_0/d$; each zero absorbs measure $\le6\eta$; apply
$N(\sigma,T)\ll T^{1-\kappa(\sigma)}$ with $T=2\gamma_0/d$. ∎

**Corollary 5.4 (the quantitative gap, precise statement — this IS quantified MW-2).**
Define, for the anchored configuration $(\rho_0,\eta,K,\varepsilon)$:

- $\delta^{\mathrm{anc}}_{\mathrm{nec}}(d)$ := the minimal anchored density producing the
  contradiction of Theorem 5.2: $\delta^{\mathrm{anc}}_{\mathrm{nec}}(d)=d^{\,\kappa(\sigma)-\epsilon}$
  (any $\epsilon>0$, along a sequence $d\to0$);
- $\delta^{\mathrm{anc}}_{\mathrm{ver}}(d)$ := the true anchored density under
  $\neg$RH: $\delta^{\mathrm{anc}}_{\mathrm{ver}}(d)\ll d^{\,\kappa(\sigma)}$ (Theorem 5.3);
- $\delta^{\mathrm{anc}}_{\mathrm{dem}}(d)$ := the anchored density the unconditional
  machinery proves: $\delta^{\mathrm{anc}}_{\mathrm{dem}}(d)=0$ (§5.5).

Then:
$$\delta^{\mathrm{anc}}_{\mathrm{dem}}\ =\ 0\ \ \ll\ \ \delta^{\mathrm{anc}}_{\mathrm{ver}}\ \ \ll\ d^{\kappa}
\ \ \approx\ \ \delta^{\mathrm{anc}}_{\mathrm{nec}}=d^{\kappa-\epsilon}.$$

Two readings, both exact:

1. **Self-blocking of exponents.** What is necessary ($d^{\kappa-\epsilon}$) and what is maximally
   possible under $\neg$RH ($d^{\kappa}$) differ only by $\epsilon$: the same zero-density
   theorem that gives the contradiction in Theorem 5.2 bounds the input in
   Theorem 5.3. **Any improvement to the zero-density theorem**
   (Ingham→density hypothesis→whatever: larger $\kappa$) **moves both sides simultaneously**: the
   threshold drops and the ceiling drops with it. The mechanism cannot beat itself by
   improving $\kappa$. This explains structurally why no refinement of
   Carlson/Ingham has ever turned self-approximation into an attack: the amplifier
   and its input are dual with respect to the same $N(\sigma,T)$.
2. **The real gap is binary.** The operative distance is not between $d^{\kappa-\epsilon}$
   and $d^{\kappa}$ (that would be "just constants"): it is between what is provable ($0$
   exactly) and what is necessary ($>0$). See §5.5.

### 5.4 Why what is provable in the anchored window is exactly zero

Inside $J_d$, the slow copy traverses $d\tau\in[\gamma_0-\eta,\gamma_0+\eta]$: a
window of heights of length $2\eta=O(1)$. At the scale of its own equidistribution
(frequencies $\asymp d\cdot\log p$, periods $\asymp1/d$), the slow copy is
**frozen**: throughout the window, $\zeta(s+id\tau)=\zeta(s+i\gamma_0)+O(\eta)$
uniformly on $K$. The statement "positive anchored density" then becomes, modulo
$O(\eta)$:

$$\mathrm{meas}\big\{\tau\in J_d:\ \sup_K|\zeta(s+i\tau)-g(s)|<\varepsilon'\big\}\ \ge\ c\cdot\mathrm{meas}(J_d),
\qquad g:=\zeta(\cdot+i\gamma_0),$$

that is: **universality with fixed target $g$ on the interval (short relative to its
height) $J_d$ — where $g$ has a zero in $K$.** This is the forbidden target of
Module 5 (Doc 102, §3): by the support theorem + Hurwitz, the limiting density
provable by Bagchi's machinery for targets with zeros is **exactly
$0$** — not "small", not "poorly bounded": the target is outside the support of the
limiting measure, and the machinery assigns zero mass to all of its small
neighborhoods. (And Matsumoto's Corollary 2 — the amplifier itself — forbids
any other machinery from giving positive density over the full $[0,T]$;
on short windows it is not forbidden that it be TRUE under $\neg$RH — Theorem 5.3
allows up to $d^\kappa$ — but it is indeed outside every known method, and proving it
unconditionally with an exponent $<\kappa$ would, by Theorem 5.2, prove RH.)

The $d\to0$ degeneration of $(\mathrm{SR}_d)$ is thus precisely identified:

> **As $d\to0$, the proofs of $(\mathrm{SR}_d)$ do not lose density nor gain
> bad constants: they lose the ONLY piece of $\tau$-space the amplifier can
> consume.** The unconditional information lives at $\tau\gg C(\varepsilon)/|d|$ (two
> copies generic relative to one another); the anchor lives at $\tau\asymp\gamma_0/|d|$
> (frozen slow copy = fixed arithmetic target with a zero). The ratio between the
> delivered scale and the useful scale is $\ge C(\varepsilon)/\gamma_0\cdot$ (constant),
> $>1$ always — and within the useful scale the problem is indistinguishable from
> local $\mathrm{SR}_0$. MW-2 in quantitative form: **relative genericity is
> provable; genericity with respect to the frozen arithmetic point is RH** (Doc 102,
> Prop. 7.2, now with rates).

### 5.5 The cascade: the only scheme that would evade the anchor, and why it does not get off the ground

For completeness (program rule: also close off the variants). An alternative
to the fixed anchor: **bootstrapping between generations of zeros.** Under $\neg$RH, the
zero $\rho_0$ produces (if there were anchored density $c$ in $J_d$) $\asymp c\,\eta/(d\,\eta)$
zeros at heights $\asymp\gamma_0/d$; each of these would serve as an anchor for a window
at $\tau\asymp\gamma_0/d^2$, etc. The count in generation $k$:
$N_k\asymp(c/d)^k$ zeros at heights $T_k\asymp\gamma_0/d^k$, that is
$$N_k\ \asymp\ T_k^{\,1-\frac{\log(1/c)}{\log(1/d)}}\ =\ T_k^{\,1-o(1)}\quad(d\to0),$$
which would crush any $N(\sigma,T)\ll T^{1-\kappa}$. The cascade is arithmetically
viable — BUT each generation consumes exactly the same forbidden input: density of
approximation to a frozen target **with a zero** ($\zeta(\cdot+it_1)$, $t_1$ = height of
a zero of the previous generation) in a short window. The scheme multiplies the
benefit of the input, it does not weaken it: the first generation already requires the
nonexistent lemma. No version of the cascade reduces the requirement below
"forbidden target on a short interval." ∎

**The missing lemma, named (for the program's map):**

> **(LF-104) Localized universality with a forbidden target.** There exists
> $\theta\in(0,1)$ such that: for some compact $K$ and $g\in H^c(K)$ WITH a zero in $K$,
> and for every large $T$, $\mathrm{meas}\{\tau\in[T,T+T^{1-\theta'}]:\sup_K|\zeta(s+i\tau)-g(s)|<\varepsilon\}
> \ge c\,T^{1-\theta'-\theta}$ with $\theta<\kappa(\sigma_K)$, for windows positioned
> at prescribed heights.

By Theorem 5.2, (LF-104) with $g=\zeta(\cdot+i\gamma_0)$ implies RH; by Theorem
5.3 its generic version is bounded by the same exponent; by Module 5 it is outside the
reach of all universality machinery. It is the "short intervals" form of the
decisive theorem I2b that Doc 102 §8 named — it coincides in substance with the direction
recent literature explores (self-approximation on short intervals, Garunkštis
et al. 2025, where the short $d=0$ version is again RH-equivalent [NOT VERIFIED in
detail]).

---

## 6. Moving $d=d(T)$ (question iv)

Can a height-dependent speed, $d(T)\to0$, recombine "information at scale $T$" with
"anchor at scale $1/d$"? No, and the reason is an exhaustive disjunction.

**Lemma 6.1 (anchor/equidistribution complementarity).** *Let $d(T)\to0$ be any
function. Consider the statement $(\mathrm{SR}_{d(T)})$: positive density (or bound
$\rho(T)$) of $\tau\in[0,T]$ with
$\sup_K|\zeta(s+i\tau)-\zeta(s+id(T)\tau)|<\varepsilon$. There are exactly two regimes:*

*(a) $d(T)\,T\to\infty$ (the slow copy escapes). Then no $\tau\le T$ has the
slow copy anchored except those in the window $J_{d(T)}\cap[0,T]$, of measure
$\le2\eta/d(T)=o(T)$; the number of off-critical zeros that the WHOLE event (anchored or not)
can certify via Rouché from the single known zero $\rho_0$ is
$\le\frac{2\eta}{6\eta\,d(T)}\cdot(1+o(1))=o(T)$ — no contradiction with
$N(\sigma,T)=o(T)$, by definition of $o$. For the $\tau$ outside the window, the
event compares two copies at heights $\to\infty$ about which no zero is known: zero
transfer.*

*(b) $d(T)\,T=O(1)$ (the slow copy stays in a bounded window $[0,\Lambda]$ of
heights for every $\tau\le T$). Then $\zeta(s+id(T)\tau)$ traverses the compact set
$\{\zeta(s+iu):u\in[0,\Lambda]\}$: the statement is the approximation of a FIXED
COMPACT FAMILY of arithmetic targets. If the family avoids zeros in $K$ (i.e. if
$\zeta\neq0$ on $K+i[0,\Lambda]$ — under $\neg$RH false for anchored $K$ and
$\Lambda\ge\gamma_0$), it is classical universality; if it contains the zero, it is the
forbidden target: provably $0$ density (§5.4), and by Carlson the true one is $o(1)$
(Proposition 4.3). In both cases the content is that of $\mathrm{SR}_0$:
nothing is gained relative to $d=0$.*

*There is no third regime, and intermediate cases by sequences split between (a) and
(b) along subsequences. ∎*

**Requested examples.** $d(T)=1/\log T$: regime (a) — the useful window has measure
$2\eta\log T=o(T)$; it produces at most $O(\log T)$ zeros: nothing. $d(T)=T^{-\theta}$,
$0<\theta<1$: regime (a); the useful window has measure $2\eta T^{\theta}$; if the
anchored density were uniformly positive there, $\asymp T^\theta$ zeros would appear
up to height $T$, contradicting Ingham as soon as
$\theta>\frac{3(1-\sigma)}{2-\sigma}$ — a real margin for $\beta_0$ not too close
to $1/2$ (e.g. $\beta_0=0.9$: $\theta>0.28$ suffices). **But** the provable anchored
density is $0$ (§5.4) and the true one under $\neg$RH is capped by the same
exponent (Theorem 5.3 rescaled): the margin is illusory — it is another
reparametrization of Corollary 5.4, with $d\leftrightarrow T^{-\theta}$. $d(T)=\gamma_0/T$: regime (b)
exactly — the statement becomes literally "$\zeta(\cdot+i\tau)$ approximates
$\zeta(\cdot+iu)$, $u\in[0,\gamma_0]$, with positive density in $[0,T]$", which for the
sub-window $u\approx\gamma_0$ is anchored $\mathrm{SR}_0$: RH-equivalent, provably
$0$ density.

**Exact breaking point:** the anchor requires the height range of the slow copy to
be $O(1)$ (otherwise it does not stably contain the zero $\rho_0$ with modulus control on the
boundary); equidistribution of the slow copy — the only input unconditional proofs
know how to use — requires that range to tend to $\infty$ (this is the condition
$|d|T\ge T_1(\varepsilon)$ of Theorem 4.1, step (1), and the Weyl condition of step
(3)). They are the negation of each other. No $d(T)$ can satisfy both; the
moving parameter only redistributes the $\tau$ between the two sterile regimes.

---

## 7. Synthesis: answer to Problem 8.1 and position in the program

### 7.1 Summary table of the degeneration

| Quantity | Behavior as $d\to0$ | Result |
|---|---|---|
| Global density $\delta(d,\varepsilon)$ | $\ge\delta_*(\varepsilon)>0$ uniform on $0<|d|<d_0(\varepsilon)$ | Theorem 4.1(a) — does NOT degenerate |
| Scale/first $\tau$: $T_0(d,\varepsilon)$ | $\asymp C(\varepsilon)/|d|$ — exactly linear | Theorem 4.1(b) + Proposition 4.3 |
| Diophantine input (Baker/6exp) | irrelevant for $|d|<d_0(\varepsilon)$; for $|d|\ge d_0$: polynomial $|d|^{C(\varepsilon)}$ (rational/algebraic), ineffective (transcendental) | Prop. 3.1, §3.3 |
| Provable anchored density | exactly $0$ (forbidden target, Hurwitz) | §5.4 |
| True anchored density under $\neg$RH | $\ll|d|^{\kappa(\sigma)}$ | Theorem 5.3 |
| Anchored density sufficient for RH | $\ge|d|^{\kappa(\sigma)-\epsilon}$ along a sequence | Theorem 5.2 |
| Moving $d(T)$ | two exhaustive sterile regimes | Lemma 6.1 |

### 7.2 The dichotomy of 8.1, corrected

- The branch "$e^{-c/|d|}$ ⟹ quantified MW-2 and closure" had the right conclusion with
  a false premise: there is no exponential degradation anywhere (not even the
  diophantine one: §3.3).
- The branch "polynomial ⟹ genuine tension with Rouché" had the correct premise (the
  degradation is polynomial, in fact linear, and the density does not degenerate at all)
  with a false conclusion: there is no tension, because Rouché does not consume the
  global quantity but the anchored one, and there the wall is **binary** ($0$ provable
  vs $>0$ necessary), not quantitative. The dichotomy's test was aimed at the wrong constant.
- Quantified MW-2 is not a degeneration rate: it is **Corollary 5.4** — the
  identity of exponents $\kappa(\sigma)$ between what is necessary and what is maximally true
  (the amplifier's self-blocking with respect to its own zero-density theorem), mounted
  on the exact zero of what is provable (Hurwitz). The rated version of Prop. 7.2
  of Doc 102.

### 7.3 New assets for the program

- **(A1') Refinement of asset A1 (Doc 102):** the Rouché-density amplifier is
  self-blocking against self-approximation-type inputs: any input expressible as
  "density of approximation to a frozen target with a zero" has ceiling $|d|^{\kappa}$
  under $\neg$RH with the same $\kappa$ as the contradiction threshold (Theorems
  5.2–5.3). For A1 to ever fire, its input must come from a source NOT
  majorizable by $N(\sigma,T)$ — a new filtering criterion for future
  recurrence proposals.
- **(A2') The diophantine-free regime (Prop. 3.1):** near the RH-equivalent point
  $d=0$, the family $\mathrm{SR}_d$ is not a problem of transcendence theory but of
  pure kinematics ($T\asymp1/|d|$). The Baker constants, which the corpus cited as
  the family's cost, are not the marginal cost at the boundary.
- **(LF-104)** as the exact statement of what is missing, in short-interval
  form (§5.5), connected to the 2025 literature.

---

## 8. Declared gaps

- **G4.1 (routine):** the full effectivization of steps (1)–(2) of Theorem 4.1
  (effective mean square of the pair and regularization of the event's boundary) is not
  written either here or in the literature; the structure of dependence on $d$ (all of the
  theorem's content used by this document) is proved. No conclusion of §§5–7
  depends on G4.1: Theorems 5.2, 5.3, Prop. 4.3, and Lemma 6.1 are
  unconditional and complete as stated.
- The resolution of the rational case $|a-b|=1$ by Pańkowski (all $d\neq0,\pm1$ rational)
  is cited from secondary sources [NOT VERIFIED in full text]; it is irrelevant
  for $d\to0$ by Remark 1.1.
- The short-intervals paper (Symmetry 17 (2025), art. 2075) verified only at the
  statement/abstract level [NOT VERIFIED in detail].
- The Baker–Wüstholz constant cited in §3.3 is the standard form of the 1993
  theorem (J. reine angew. Math. 442); used only illustratively in the regime
  $|d|\ge d_0(\varepsilon)$, outside the document's critical path.

---

## 9. VERDICT

**ROUTE CLOSED.**

**Precise reason:** the Form C question is answered in a sense stronger than its
own dichotomy. The degeneration of $(\mathrm{SR}_d)$ as $d\to0$ is **polynomial — in
fact exactly linear: $T_0(d,\varepsilon)\asymp C(\varepsilon)/|d|$ — and the density
$\delta(d,\varepsilon)$ does not degenerate at all** (uniformly positive on
$0<|d|<d_0(\varepsilon)$, with all diophantine classes of $d$ collapsed:
Proposition 3.1, Theorem 4.1). According to P41's dichotomy this should have opened a "genuine
tension with Rouché"; it does not, because the Rouché argument does not consume the
global density but the density in the anchored window $J_d=\{\tau:d\tau\approx\gamma_0\}$, of
measure $\asymp1/|d|$, where the slow copy is frozen and the statement collapses to
universality with a forbidden target ($\zeta(\cdot+i\gamma_0)$, which carries the zero):
provably exactly $0$ density (Hurwitz/Module 5). The exact quantitative gap is
Corollary 5.4: what suffices for RH is anchored density $|d|^{\kappa(\sigma)-\epsilon}$
(Theorem 5.2), what is true under $\neg$RH is capped by $|d|^{\kappa(\sigma)}$ with the
**same exponent** (Theorem 5.3) — the amplifier is self-blocking with respect to its
own zero-density theorem — and what is provable is $0$. The wall is not a rate:
it is binary, with MW-2 rated around it. The moving parameter $d(T)$ evades nothing:
anchoring and equidistributing the slow copy are complementary conditions
($|d|T=O(1)$ vs $|d|T\to\infty$) for every function $d(T)$ (Lemma 6.1).

**The only thing that would reopen the line:** lemma (LF-104) — localized universality in
short intervals with a forbidden target and an exponent better than $\kappa(\sigma)$ — which
by Theorem 5.2 implies RH, by Theorem 5.3 sits at the exact edge of what is
consistent, and by Module 5 is outside all existing universality machinery. It is not a
direction of work: it is the re-encoding of RH in short-interval coordinates, and is
recorded as such.

---

## References

**External literature:**
- B. Bagchi, *Recurrence in topological dynamics and the Riemann hypothesis*, Acta Math.
  Hungar. **50** (1987), 227–240.
- K. Matsumoto, *A survey on the theory of universality for zeta and L-functions*,
  arXiv:1407.4216 (2014) — §9 for the family $\mathrm{SR}_d$ (formulas (9.3)–(9.4),
  Thm. 21).
- T. Nakamura, *The generalized strong recurrence for non-zero rational parameters*,
  Arch. Math. **95** (2010), 549–555.
- T. Nakamura, Ł. Pańkowski, *Erratum/corrigendum*, Arch. Math. **99** (2012), 43–47;
  arXiv:1203.1393 (verified: $\zeta$ for $d=a/b$, $|a-b|\neq1$; $\log\zeta$ for all
  $d\neq0$; $d=0$ for $\log\zeta$ is equivalent to RH).
- Ł. Pańkowski, resolution of the remaining rational case $d\neq0,\pm1$ [reported; NOT
  VERIFIED in full text].
- R. Garunkštis, *Self-approximation of Dirichlet L-functions*, J. Number Theory **131**
  (2011) / arXiv:1006.1507.
- R. Garunkštis et al., *On self-approximation of the Riemann zeta function in short
  intervals*, Symmetry **17** (2025), art. 2075 [abstract verified].
- A. Baker, *Linear forms in the logarithms of algebraic numbers I–III*, Mathematika
  13–14 (1966–67); A. Baker, G. Wüstholz, J. reine angew. Math. **442** (1993), 19–62.
- S. Lang, *Introduction to Transcendental Numbers* — six exponentials theorem.
- F. Carlson (1920); A. E. Ingham (1940) — $N(\sigma,T)\ll T^{4\sigma(1-\sigma)+\epsilon}$,
  $N(\sigma,T)\ll T^{3(1-\sigma)/(2-\sigma)}\log^5T$.
- P. Walters, *An Introduction to Ergodic Theory*, Springer GTM 79.

**Internal docs (backward-only):**
- Doc 102 (`phase-35-five-fronts/102-audit-of-the-bagchi-criterion-strong-recurrence.md`) — modules 1–5,
  amplifier A1, Prop. 7.2, family $\mathrm{SR}_d$, verdict FAIL I2b.
- P41 (`06-papers/P41-exhaustion-1d-propagation/main.tex`) — Problem 8.1 / Form C.
- `COMPLETE-PROGRAM-SUMMARY.md` — MW-2, MW-7.

---

*Doc 104 · Phase 36*
