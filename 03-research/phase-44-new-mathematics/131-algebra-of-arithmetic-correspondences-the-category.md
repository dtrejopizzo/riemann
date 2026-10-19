# Doc 131 — The algebra of arithmetic correspondences: the category 𝒜rith

**Program:** Riemann Hypothesis — Phase 44: NEW MATHEMATICS.
**Prerequisites:** Doc 107 (W₂, thickened kernel, autonomous almost-prime side, Theorems 2.4/4.2/4.4/5.5); Doc 125 (tropical intersection form, toy (1,2), correspondences Δ_μ, gaps G-125.A/B); Doc 110 (axioms L1–L6, class ℱ, impossibility Theorem 4.3, Prop. 4.5); Doc 106 (tensor-index identity).
**Creative contract (Phase 44):** **[NEW-DEFINITION]** total freedom; **[THEOREM]/[PROPOSITION]/[LEMMA]** truly proved, with complete proof; **[BRIDGE]** connection with ζ/RH with declared status; **[WISH]** what we want and do not prove; **[DATA]** literature with citation; **[CONSTRUCTION]** designed object with declared status. Freedom lives in the definitions; discipline, in what is called a theorem.

---

## 0. Executive summary

This document invents the category where the two-variable Weil functional (Doc 107)
and the intersection form of the square (Doc 125) live natively. The central move:
the category is defined over **all** arithmetic functions — ζ is ONE object among
many — so that every theorem is external to ζ **by construction** (clause NC2
of the R-NC test stops being verified after the fact: it is in the axioms).

What is proved, without adornment:

1. **(§1)** The ring of two-variable kernels $(\mathcal{K}_2,\star_2)$ with the
   double Dirichlet convolution is a local commutative ring (Theorem 1.4, the
   category's first theorem), and the Dirichlet ring $\mathcal{D}$ is a
   **differential ring** with derivation $a\mapsto a\cdot\log$; the convolution
   exponential characterizes the Euler product: $F$ has an Euler product $\iff$
   its Dirichlet logarithmic derivative is supported on prime powers
   (Theorem 1.9).

2. **(§2–§3)** The category $\mathcal{A}rith$: objects $(a,c,\omega)$ with $a$ an
   arbitrary arithmetic function; correspondences = two-variable kernels plus
   the translations $\Delta_\mu$ of Doc 125, with associative composition and
   a unit (Theorem 2.7). The **degree** of a correspondence is the almost-prime side:
   for every object, $\deg_X(h_{g,\varphi})$ contains the block
   $\sum_N g(N)\sum_{d\mid N}a(d)\,a(N/d)\,\varphi(d^2/N)$ (Theorem 3.3) — the
   formula from Doc 107 with $\Lambda$ replaced by any $a$. The involution
   $\rho\mapsto 1-\bar\rho$ is an involutive functor $\sigma$ (Prop. 2.9).

3. **(§4)** In the spectral subcategory $\mathcal{A}rith^{EF}$ (objects with a divisor),
   the **orbit theorem** (Theorem 4.4): every finite $\sigma$-stable block of
   the divisor produces signature $(n_{\mathrm{on}}+n_{\mathrm{orb}},\,n_{\mathrm{orb}})$ —
   fixed points of $\sigma$ give positive directions, free orbits give hyperbolic
   planes. Universal corollary: **the negative index never exceeds the positive
   one** ($q\le p$) in any object of the category, and every signature with $q\le p$
   is realized (Theorem 4.6, classification). The tensor-index identity of
   Doc 106 is imported and proved (Theorem 4.8).

4. **(§5)** Doc 125's **toy index theorem** becomes a theorem of the
   category: every rank-3 intersection structure with genus $g$ has Gram matrix
   $\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&2-2g\end{psmallmatrix}$, signature
   $(1,2)$, and negative-definite primitive part **if and only if** $g\ge 1$; at
   $g=0$ the form degenerates (Theorem 5.3). The class of objects realizing it: the
   **periodic** objects (of a single prime), with $g=1$, for arbitrary coefficients — the
   signature of Doc 125 is not about ζ: it is about the lattice.

5. **(§6) Axiom H.** Stated without mentioning zeros: $Q_X(f,f):=W_X(f\star\tilde f)
   \ge 0$, with $W_X$ given by the data $(a,c,\omega)$. Verifications carried out:
   the constant function $1$ **fails** (three-line proof); every
   completely multiplicative function without polar mass **fails** (Prop. 6.5, diagonal
   mass); Davenport–Heilbronn **fails unconditionally in blocks** (its off-line zeros
   [DATA] activate the orbit theorem). And the document's central result, the
   **local purity theorem (Theorem 6.7)**: for the one-prime Euler objects
   $F_{p,\alpha}$, $H$ holds $\iff |\alpha|=\sqrt p$ — Axiom H restricted to the
   local subcategory is **decidable and equivalent to purity of weights**, with
   complete proof in both directions (Poisson formula + Mertens two-bump
   test, where the barrier is exactly $|c_m|\le 2p^{m/2}$).
   Consequence: **the Euler product does NOT imply H** ($F_{p,\alpha}$ with
   $|\alpha|\ne\sqrt p$ has an Euler product and violates H); the discriminator is purity, not
   multiplicativity.

6. **(§7) [BRIDGE]** $H(\zeta_{\mathrm{ob}})\iff$ RH: the direction RH$\Rightarrow$H is
   the orbit theorem (proved here for the whole category); the converse is
   Weil's criterion [DATA]. **RH-equivalent, stated without disguise.** What the
   category redistributes: (i) H is decidable in the local subcategory
   (purity) and the finite-divisor subcategory; (ii) the axioms
   **explicitly** violate hypothesis (ii) of Definition 4.2 of Doc 110
   (test-accessibility): the divisor is structural data, not an unknown — the
   impossibility Theorem 4.3 does not apply to the functors of
   $\mathcal{A}rith^{EF}$, and all the non-autonomy is concentrated in
   a single comparison functor. (iii) The [WISH] that remains named: the
   **Conjecture H⁺** ($a\ge 0$ on prime powers + Hermitian + standard polar
   block $\Rightarrow$ H) and the **limit-rigidity lemma** (stability of H
   under the Euler filtration).

7. **(§8)** The free return (theorems independent of RH): classification of
   achievable signatures (q ≤ p, surjective), local purity as a decidable
   criterion, and the differential characterization of the Euler product.

---

## 1. The base ring

### 1.1. The Dirichlet ring and the ring of kernels

**[NEW-DEFINITION 1.1].** $\mathbb{N}^\times := (\mathbb{Z}_{\ge1},\cdot)$, the
multiplicative monoid (free commutative over the primes).
$\mathcal{D} := \{a:\mathbb{N}^\times\to\mathbb{C}\}$ with the Dirichlet convolution
$(a\star b)(n) = \sum_{de=n} a(d)\,b(e)$.
$\mathcal{K}_2 := \{K:\mathbb{N}^\times\times\mathbb{N}^\times\to\mathbb{C}\}$ with the
**two-variable Dirichlet convolution**
$$(K\star_2 L)(m,n) \;:=\; \sum_{m_1m_2=m}\;\sum_{n_1n_2=n} K(m_1,n_1)\,L(m_2,n_2).$$
Both sums are finite for each $(m,n)$ (every integer has finitely many factorizations):
no support or growth condition is imposed. $\mathcal{K}_2$ is the
total algebra of the monoid $\mathbb{N}^\times\times\mathbb{N}^\times$.

**[THEOREM 1.2] (structure of $\mathcal{D}$).** $(\mathcal{D},+,\star)$ is a
commutative, associative $\mathbb{C}$-algebra, with unit $\delta_1$
($\delta_1(1)=1$, $0$ otherwise), local: $a$ is invertible $\iff a(1)\neq 0$, and the
maximal ideal is $\mathfrak{m} = \{a : a(1)=0\}$.

*Proof.* Commutativity: reindex $(d,e)\mapsto(e,d)$. Associativity:
$((a\star b)\star c)(n) = \sum_{def=n} a(d)b(e)c(f) = (a\star(b\star c))(n)$, a
finite sum symmetric in the three factors. Unit: immediate. Invertibility: if
$a(1)\ne0$, define $b(1)=a(1)^{-1}$ and, by recursion on $n$ ordered by
divisibility, $b(n) = -a(1)^{-1}\sum_{d\mid n,\,d>1}a(d)\,b(n/d)$ (the $n/d$ are
proper divisors, already defined); then $a\star b=\delta_1$ by construction.
If $a(1)=0$: $(a\star b)(1)=a(1)b(1)=0\ne1$ for every $b$. Locality: the
complement of $\mathfrak m$ is exactly the group of units. $\square$

**[DATA 1.3].** $(\mathcal{D},\star)$ is moreover an integral domain and a unique
factorization domain (Cashwell–Everett, *The ring of number-theoretic functions*, Pacific J. Math. 9
(1959), 975–985: $\mathcal{D}\cong\mathbb{C}[[x_1,x_2,\dots]]$ via prime
exponents). Not load-bearing below; cited for structural completeness.

**[THEOREM 1.4] (the category's first theorem: $\mathcal{K}_2$).**
$(\mathcal{K}_2,+,\star_2)$ is a commutative associative $\mathbb{C}$-algebra with
unit $\delta_{(1,1)}$, local with maximal ideal $\{K:K(1,1)=0\}$. The tensor
product $a\otimes b\,(m,n):=a(m)b(n)$ is a morphism of algebras
$\mathcal{D}\otimes_{\mathbb{C}}\mathcal{D}\to\mathcal{K}_2$:
$(a\otimes b)\star_2(a'\otimes b') = (a\star a')\otimes(b\star b')$.

*Proof.* Associativity:
$((K\star_2L)\star_2M)(m,n) = \sum_{m_1m_2m_3=m}\sum_{n_1n_2n_3=n}
K(m_1,n_1)L(m_2,n_2)M(m_3,n_3)$, a finite sum symmetric in the three; likewise for
the other parenthesization. Commutativity and unit: as in 1.2. Locality: the same
recursion as in 1.2 over $\mathbb{N}^\times\times\mathbb{N}^\times$ ordered by
divisibility componentwise (the proper divisors of $(m,n)$ are finite and the
recursion is well founded because $\Omega(m)+\Omega(n)$ strictly decreases). The tensor
identity: expand both sides and reindex — $\sum_{m_1m_2=m}a(m_1)a'(m_2)\cdot
\sum_{n_1n_2=n}b(n_1)b'(n_2)$. $\square$

**Remark 1.5.** $\star_2$ is the "monoidal" composition of the category (the
ring structure of discrete arithmetic correspondences); the "matrix"
composition (correspondences as operators) is that of §2.2. The two coexist:
$\mathcal{K}_2$ is the underlying Hopf-monoid algebra, §2.2 is the category.

### 1.2. The differential structure: the Euler product as a ring theorem

**[NEW-DEFINITION 1.6].** The **logarithmic derivation**: $D:\mathcal{D}\to
\mathcal{D}$, $(Da)(n) := a(n)\log n$. For $F$ a normalized unit ($F(1)=1$), the
**Dirichlet logarithmic derivative**: $L(F) := F^{-1}\star DF$. (For
$F\leftrightarrow\sum F(n)n^{-s}$, $L(F)\leftrightarrow -\,d/ds\,\log$ of the series;
for $F$ = the coefficients of $\zeta$, $L(F)=\Lambda$.)

**[LEMMA 1.7].** $D$ is a derivation of $(\mathcal{D},\star)$:
$D(a\star b) = Da\star b + a\star Db$. Consequently $L(F\star G) = L(F)+L(G)$
for normalized units, and $L(F)=0\iff F=\delta_1$.

*Proof.* $D(a\star b)(n) = \log n\sum_{de=n}a(d)b(e) =
\sum_{de=n}(\log d+\log e)\,a(d)b(e)$. Additivity of $L$:
$L(F\star G) = (F\star G)^{-1}\star(DF\star G + F\star DG) = F^{-1}\star DF +
G^{-1}\star DG$. Kernel: if $L(F)=0$ then $DF=0$, i.e. $F(n)\log n=0$ for every
$n$, i.e. $F(n)=0$ for $n\ge2$; with $F(1)=1$, $F=\delta_1$. $\square$

**[NEW-DEFINITION 1.8].** $\exp_\star:\mathfrak m\to 1+\mathfrak m$,
$\exp_\star(g) := \sum_{k\ge0} g^{\star k}/k!$ — well defined because
$g^{\star k}(n)=0$ for $k>\Omega(n)$ (each factor contributes a divisor $>1$): the sum
at each $n$ is finite.

**[THEOREM 1.9] (differential characterization of the Euler product).** Let $F$
be a normalized unit. The following are equivalent:
(i) $F$ is multiplicative with an Euler product: $F(mn)=F(m)F(n)$ for $(m,n)=1$;
(ii) $L(F)$ is supported on prime powers;
(iii) $F = \exp_\star(g)$ with $g$ supported on prime powers.
In that case $g(p^k) = L(F)(p^k)/\log p^k$.

*Proof.* **(iii)$\Rightarrow$(ii):** $D\exp_\star(g) = \exp_\star(g)\star Dg$
(differentiate term by term: $D(g^{\star k}) = k\,g^{\star(k-1)}\star Dg$ by
Lemma 1.7 and induction; the sums are locally finite), hence
$L(\exp_\star g) = Dg$, supported where $g$ is. **(ii)$\Rightarrow$(iii):** given
$\ell:=L(F)$ supported on prime powers, let $g(p^k):=\ell(p^k)/(k\log p)$,
$g:=0$ elsewhere; then $L(\exp_\star g) = Dg = \ell = L(F)$, and by Lemma 1.7
$L(F\star(\exp_\star g)^{-1}) = 0$, hence $F=\exp_\star g$. **(iii)$\Rightarrow$(i):**
write $g=\sum_p g_p$ (components with disjoint $p$-adic support, locally finite
sum); the $g_p$ commute and $g_p\star g_q$ ($p\ne q$) is supported on mixed
integers; $\exp_\star(g) = {\star\!\prod}_p \exp_\star(g_p)$ (locally finite
product: at each $n$ only the $p\mid n$ are involved), and a product of local
factors is multiplicative: $F(mn)$ with $(m,n)=1$ separates the primes of $m$ and of
$n$. **(i)$\Rightarrow$(ii):** if $F$ is multiplicative, $F = {\star\!\prod}_p F_p$
with $F_p :=$ the restriction of $F$ to $p^{\mathbb{N}}$ (extended by $0$; the
identity $F = {\star\!\prod}F_p$ is exactly multiplicativity, evaluated at each $n$).
By additivity of $L$ (extended to locally finite products: at each $n$ only
finitely many factors are $\ne\delta_1$), $L(F) = \sum_p L(F_p)$, and each $L(F_p)$ is
supported on $p^{\mathbb{N}}$ because $F_p$, $F_p^{-1}$ and $DF_p$ are (closed
subalgebra). $\square$

**Remark 1.10 [DATA].** The Dirichlet exponential appears in Rearick,
*Operators on algebras of arithmetic functions*, Duke Math. J. 35 (1968); the
packaging "Euler $\iff$ support of $L(F)$ on prime powers" as a ring theorem is the
form the category needs in §6.7: **the property "having an Euler product" is a
support condition on the object, visible without analyticity** — it is a
categorical predicate on $a=L(F)$, not on the analytic function $F(s)$.

---

## 2. The category $\mathcal{A}rith$

Henceforth $G := \mathbb{R}_+^*$ with Haar measure $d^*x = dx/x$, test
class $C_c^\infty(G)$, Mellin transform $\hat f(s)=\int_0^\infty f(x)x^{s-1}dx$
(entire), and involution $\tilde f(x) := \overline{f(1/x)}\,x^{-1}$, with
$\widehat{\tilde f}(s) = \overline{\hat f(1-\bar s)}$. Multiplicative convolution
$(f_1\star f_2)(x)=\int_G f_1(y)f_2(x/y)\,d^*y$. All as in Doc 107 §1.

### 2.1. Objects

**[NEW-DEFINITION 2.1] (arithmetic object).** An object of $\mathcal{A}rith$ is a
triple $X=(a,c,\omega)$:
- $a:\mathbb{N}^\times\to\mathbb{C}$ **arbitrary** (the discrete datum; no
  growth condition: sums against compactly-supported tests are finite);
- $c$ = finite formal sum $\sum_j c_j\,[s_j]$, $s_j\in\mathbb{C}$, $c_j\in\mathbb{C}$
  (the **polar block**, arbitrary points and weights);
- $\omega$ = even measurable function of polynomial growth on $\mathbb{R}$ (the
  **archimedean block**).

The **Weil functional of the object** is, for $f\in C_c^\infty(G)$:
$$W_X(f) \;:=\; \underbrace{\sum_j c_j\,\hat f(s_j)}_{D_c(f)}
\;-\;\underbrace{\sum_{n\ge1}\Bigl[a(n)\,f(n) + \overline{a(n)}\,n^{-1} f(1/n)\Bigr]}_{P_a(f)}
\;-\;\underbrace{\frac{1}{2\pi}\int_{\mathbb{R}}\hat f\!\left(\tfrac12+it\right)\omega(t)\,dt}_{A_\omega(f)}.$$
All sums are finite or absolutely convergent (compact support +
Paley–Wiener, Doc 107 Lemma 1.2). The sum in $n$ starts at $n=1$: the atom $a(1)$
(mass at $x=1$) is allowed.

**Examples (the working catalogue).**
- **$\zeta_{\mathrm{ob}}$:** $a=\Lambda$ (von Mangoldt), $c = [0]+[1]$,
  $\omega=\Omega$ (Doc 107 Def. 1.3). $W_{\zeta_{\mathrm{ob}}} = \mathcal{W}$ of
  Doc 107's Theorem 1.4.
- **$X_1$ (the constant function):** $a(n)=1\ \forall n$, $c=0$, $\omega=0$.
- **$X_h$ (completely multiplicative):** $h:\mathbb{N}^\times\to\{\pm1\}$
  completely multiplicative (e.g. random Rademacher on the primes);
  $a = h\cdot\Lambda$, $c=0$, $\omega=0$.
- **$F_{p,\alpha}$ (one-prime Euler object):** §6.5; $a(p^m) = -c_m\log p$
  ($m\ge1$) with $c_m=\alpha^m+(p/\bar\alpha)^m$, $c=0$, $\omega\equiv -2\log p$.
- **$X_{DH}$ (Davenport–Heilbronn):** the datum $(a,c,\omega)$ of the
  Davenport–Heilbronn function (combination $\tfrac{1-i\kappa}{2}L(s,\chi)+
  \tfrac{1+i\kappa}{2}L(s,\bar\chi)$, $\chi$ the odd character mod 5), which has
  a functional equation but no Euler product [DATA: Davenport–Heilbronn 1936;
  Titchmarsh §10.25]; its $a$ is the sequence of $-D'/D$, not supported on prime
  powers.
- **Finite-divisor objects:** any finite multiset
  $Z\subset\mathbb{C}$ defines $X_Z := (0, \sum_{\rho\in Z}[\rho], 0)$, with
  $W_{X_Z}(f) = \sum_{\rho\in Z}\hat f(\rho)$. **In the category, "zero" and "pole"
  are the same type of datum with different roles** (cf. Doc 107 Obs. 4.1: in the
  double object the pole/spectrum separation already collapsed; here it is assumed
  from the axiom).

### 2.2. Correspondences and composition

**[NEW-DEFINITION 2.2].** For objects $X,Y$, the space of correspondences is
$$\mathrm{Corr}(X,Y) \;:=\; \Bigl\{\,T \;=\; \sum_{\alpha\ \mathrm{finite}}
\lambda_\alpha\,\Delta_{\mu_\alpha} \;+\; T_h \;:\;
\lambda_\alpha\in\mathbb{C},\ \mu_\alpha\in G,\ h\in C_c^\infty(G\times G)\,\Bigr\},$$
operators on $C_c^\infty(G)$: $(\Delta_\mu f)(x) := f(\mu x)$ (the translation of
Doc 125: the graph $\{y=\mu x\}$), $(T_h f)(x) := \int_G h(x,y)\,f(y)\,d^*y$. (The
space does not depend on $X,Y$ — the category has a constant Hom; the objects weigh
the correspondences via the degree of §3. This is a design choice: the
correspondences are **universal**, the intersection numbers are **of the
object**.)

**[LEMMA 2.3] (faithfulness of the kernel).** The map $(\,(\lambda_\alpha,\mu_\alpha)_\alpha,
h\,)\mapsto T$ is injective: if $T=0$ as an operator, then all the
$\lambda_\alpha=0$ and $h=0$.

*Proof.* Let $T=\sum\lambda_\alpha\Delta_{\mu_\alpha}+T_h=0$ with
distinct $\mu_\alpha$. Apply to $f_\epsilon$ = approximation to the identity at
$x_0\in G$ ($f_\epsilon\ge0$, support in $[x_0e^{-\epsilon},x_0e^{\epsilon}]$,
$\int f_\epsilon\,d^*y=1$): $(T_hf_\epsilon)(x)\to h(x,x_0)$ uniformly on
compact sets, while $(\Delta_\mu f_\epsilon)(x) = f_\epsilon(\mu x)$ is supported
on $x\in x_0\mu^{-1}e^{\pm\epsilon}$ and has $L^1_{d^*x}$ mass
equal to 1 concentrating at the point $x_0/\mu$. Evaluating $\langle Tf_\epsilon, \phi\rangle$
with $\phi\in C_c^\infty$ supported away from the finitely many points $x_0/\mu_\alpha$:
we get $\int h(x,x_0)\phi(x)d^*x=0$ for every such $\phi$ and every $x_0$, hence $h=0$
(continuity). With $h=0$, take $\phi$ = a bump at $x_0/\mu_\beta$ avoiding the
other points: we get $\lambda_\beta\,\phi$-mass $=0$, hence $\lambda_\beta=0$. $\square$

**[THEOREM 2.4] (composition).** $\mathrm{Corr}$ is closed under composition of
operators, the composition is associative, and $\Delta_1=\mathrm{id}$ is the
unit. Explicitly:
$$\Delta_\mu\circ\Delta_\nu = \Delta_{\nu\mu}=\Delta_{\mu\nu},\qquad
\Delta_\mu\circ T_h = T_{h(\mu\,\cdot,\,\cdot)},\qquad
T_h\circ\Delta_\mu = T_{h(\cdot,\,\mu^{-1}\cdot)},$$
$$T_h\circ T_k = T_{h\bullet k},\qquad
(h\bullet k)(x,z) := \int_G h(x,y)\,k(y,z)\,d^*y\ \in C_c^\infty(G\times G).$$

*Proof.* The four formulas: direct computation —
$(\Delta_\mu T_h f)(x) = (T_hf)(\mu x) = \int h(\mu x,y)f(y)d^*y$;
$(T_h\Delta_\mu f)(x) = \int h(x,y)f(\mu y)d^*y = \int h(x,\mu^{-1}u)f(u)d^*u$
(Haar invariance); $(T_hT_kf)(x) = \int h(x,y)\int k(y,z)f(z)\,d^*z\,d^*y$ and
Fubini (compactly supported continuous integrands) gives $T_{h\bullet k}$; $h\bullet k$
is $C^\infty$ (differentiation under the integral with domination on compacts) and of compact
support (projections of compact supports). Closure: the four types of
product land in $\mathrm{Corr}$. Associativity: this is composition of operators on
$C_c^\infty(G)$, associative by definition; by Lemma 2.3 the resulting kernels
are uniquely determined, so associativity also holds at the level of
kernels. Unit: $\Delta_1 f = f$. $\square$

**Remark 2.5 (where Doc 125 ended up).** The $\Delta_\mu$ are exactly the
correspondences of the scaling flow of Doc 125 §2.4, now with exact composition
$\Delta_\mu\circ\Delta_\nu=\Delta_{\mu\nu}$ for **every** $\mu,\nu$ (without the
restriction $\lambda\lambda'\notin\mathbb{Q}$ of 1502.05580: the price is working
over the full $G$ and not over a quotient). The discrete structure $\mathcal{K}_2$
of §1.1 is embedded via $K\mapsto$ weights over the points $(m,n)$; the
continuous↔discrete bridge is the thickened kernel of §3.

**[NEW-DEFINITION 2.6] (involution of correspondences).** For
$h\in C_c^\infty(G^2)$: $\tilde h(x,y) := \overline{h(1/x,1/y)}\,(xy)^{-1}$; for
translations: $\widetilde{\Delta_\mu} := \Delta_{\mu}$ (the graph $\{y=\mu x\}$ is
stable under $(x,y)\mapsto(1/y,1/x)$ — the transposed-reflected map). Antilinear
extension to $\mathrm{Corr}$.

### 2.3. The involution functor $\sigma$ and Hermitian objects

**[NEW-DEFINITION 2.7].** $\sigma:\mathcal{A}rith\to\mathcal{A}rith$:
$$\sigma(a,c,\omega) := \bigl(\bar a,\ \textstyle\sum_j \bar c_j\,[\,1-\bar s_j\,],\ \omega\bigr),
\qquad \sigma(T):=\widetilde{T}.$$

**[PROPOSITION 2.8].** (a) $\sigma^2=\mathrm{id}$. (b) For every object $X$ and every
test $f$: $W_{\sigma X}(f) = \overline{W_X(\tilde f)}$. (c) If $X$ is **Hermitian**
($\sigma X = X$, i.e. $a$ real, $c$ stable under $s\mapsto1-\bar s$ with conjugate
weights, $\omega$ real), then
$$Q_X(f_1,f_2) := W_X(f_1\star\tilde f_2)$$
is a Hermitian form on $C_c^\infty(G)$: $Q_X(f_2,f_1)=\overline{Q_X(f_1,f_2)}$.

*Proof.* (a) Immediate on the data ($1-\overline{(1-\bar s)}=s$).
(b) Block by block. Polar: $\widehat{\tilde f}(s)=\overline{\hat f(1-\bar s)}$ gives
$\overline{D_c(\tilde f)} = \sum\bar c_j\,\hat f(1-\bar s_j) = D_{\sigma c}(f)$.
Discrete: $\tilde f(n) = \overline{f(1/n)}\,n^{-1}$ and
$n^{-1}\tilde f(1/n) = n^{-1}\overline{f(n)}\cdot n\cdot n^{-1}
= \overline{f(n)}\,n^{-1}$… direct computation:
$\overline{P_a(\tilde f)} = \sum_n[\bar a(n)\,\overline{\tilde f(n)} +
a(n)\,n^{-1}\overline{\tilde f(1/n)}]$ with $\overline{\tilde f(n)} = f(1/n)n^{-1}$ and
$\overline{\tilde f(1/n)} = f(n)\cdot n$: we get
$\sum_n[\,a(n)f(n) + \bar a(n)n^{-1}f(1/n)\,]$ with $a\mapsto\bar a$ — exactly
$P_{\bar a}(f)$. Archimedean: $\widehat{\tilde f}(\tfrac12+it) =
\overline{\hat f(\tfrac12+it)}$ and $\omega$ even and real. (c) From (b) with $\sigma X=X$:
$\overline{Q_X(f_1,f_2)} = \overline{W_X(f_1\star\tilde f_2)} =
W_X(\widetilde{f_1\star\tilde f_2}) = W_X(\tilde f_1\star f_2) = Q_X(f_2,f_1)$,
using $\widetilde{(u\star v)} = \tilde u\star\tilde v$ and
$\tilde{\tilde u}=u$ (direct computation on $G$). $\square$

**Remark 2.9 ($\sigma$ is the involution $\rho\mapsto1-\bar\rho$ as a functor).**
On the spectral objects of §4, $\sigma$ acts on the divisor exactly via
$\rho\mapsto1-\bar\rho$ (Prop. 4.2(b)). The target's request — "the involution as
a functor" — is fulfilled at the right level: $\sigma$ is defined on **arithmetic
data**, and the action on zeros is a theorem, not a definition.

---

## 3. The degree of a correspondence is the almost-prime side

### 3.1. Thickened kernels and the degree

**[NEW-DEFINITION 3.1].** Thickened kernel (Doc 107 Def. 3.2):
$h_{g,\varphi}(x,y) := g(xy)\,\varphi(x/y)$, $g,\varphi\in C_c^\infty(G)$. For an
object $X$, the **degree** (or intersection trace) of a correspondence
$h\in C_c^\infty(G^2)$ is
$$\deg_X(h) \;:=\; (W_X\otimes W_X)(h),$$
where $W_X\otimes W_X$ is defined by the **nine-block arithmetic
expansion**: $(D_c-P_a-A_\omega)^{(1)}\otimes(D_c-P_a-A_\omega)^{(2)}$ applied to $h$, each block
with Doc 107's §2.3 formula with $\Lambda\to a$ (plus the mirror
terms $\bar a(n)\,n^{-1}$ at $1/n$), $\{0,1\}\to\{s_j\}$ with weights $c_j$, $\Omega\to\omega$.
Each block is a finite sum or absolutely convergent integral: **the degree is
defined for EVERY object of $\mathcal{A}rith$ and mentions no zeros of anything.**

**[PROPOSITION 3.2] (well-definedness and iteration).** For every $X$ and every
$h\in C_c^\infty(G^2)$, $\deg_X(h) = W_X^{(1)}[x\mapsto W_X^{(2)}[h(x,\cdot)]]$, and the
slice $x\mapsto W_X^{(2)}[h(x,\cdot)]$ lies in $C_c^\infty(G)$. In particular
$\deg_X$ is symmetric in the order of iteration.

*Proof.* Identical to Doc 107 Lemma 2.2(a)(c) with general data: the
discrete block of the slice is a finite sum of evaluations
$h(x,n),\,h(x,1/n)$ ($C_c^\infty$ in $x$); the polar block, partial
Mellin evaluations (entire in $s$, $C_c^\infty$ in $x$ by differentiation under
the integral); the archimedean block, an integral with uniform rapid
decay (Paley–Wiener with a parameter, Doc 107 Lemma 1.2: the proof uses only compact
support and smoothness, nothing about ζ). Expanding the iteration gives the nine
blocks; the symmetry is the manifest symmetry of the
expansion. $\square$

### 3.2. The general almost-prime theorem

**[THEOREM 3.3] (the almost-prime side is the degree, for every arithmetic function).**
Let $X=(a,c,\omega)$ and $h=h_{g,\varphi}$. The discrete$\times$discrete block of
$\deg_X(h)$ is
$$P\!\otimes\!P(h) = \Sigma_{\mathrm{I}}+\Sigma_{\mathrm{II}}+\Sigma_{\mathrm{III}}
+\Sigma_{\mathrm{IV}},\qquad
\boxed{\ \Sigma_{\mathrm{I}} = \sum_{N\ge1} g(N)\,\bigl(a\star_\varphi a\bigr)(N),\quad
(a\star_\varphi a)(N) := \sum_{d\mid N} a(d)\,a(N/d)\,\varphi\!\left(\frac{d^2}{N}\right),}$$
and $\Sigma_{\mathrm{II,III,IV}}$ are the finite mirror sums of Doc 107's Theorem 4.2
with $\Lambda(n_i)\to a(n_i)$ or $\overline{a(n_i)}$ depending on the reflected slot
and corresponding weights $n_i^{-1}$. All sums are finite (compact support of $g$ and
$\varphi$).

*Proof.* Substitute $h(n_1,n_2)=g(n_1n_2)\varphi(n_1/n_2)$ and the three
reflected evaluations into block (4) of the expansion; for $\Sigma_{\mathrm I}$,
group by $N=n_1n_2$: the pair $(n_1,n_2)$ with $n_1n_2=N$ ranges over the divisors
$d=n_1$ of $N$, with $n_1/n_2 = d^2/N$. This is the same computation as Doc 107's
Theorem 4.2, which never used $\Lambda$ as anything more than a coefficient: the
identity holds for arbitrary $a$. Finiteness: only the $N$ (resp. the $n_1n_2$, etc.)
in the compact supports contribute. $\square$

**Remark 3.4 (NC2 by construction — the design point).** In Doc 107, the
autonomy of the almost-prime side was a **finding** (Theorem 4.4: the mixed
terms reabsorb). Here it is a **realized axiom**: $\deg_X$ is defined by the
arithmetic expansion, for every object; the statement "$\deg_X$ mentions no zeros"
is not verified — it is the definition. The overgeneration of the R-NC test
(Doc 119, NC2) is thereby incorporated: any theorem about $\deg$ proved in §4–§6
quantifies over all arithmetic functions, and ζ enters as the point
$a=\Lambda$. The design cost, stated: the equality $\deg_X = $ double sum over
zeros is now a **theorem with hypotheses** (§4.7), not a definition — the
difficulty does not disappear, it moves elsewhere; §7 strikes the balance.

---

## 4. Spectral objects: the subcategory $\mathcal{A}rith^{EF}$

### 4.1. Definition and the comparison functor

**[NEW-DEFINITION 4.1].** A **spectral object** is a pair $(X,Z)$ with
$X\in\mathcal{A}rith$ and $Z$ a countable multiset in $\mathbb{C}$ (the
**divisor**), with bounded real parts and counting function
$N_Z(T):=\#\{\rho\in Z:|\mathrm{Im}\,\rho|\le T\} \ll T^{A}$ for some $A<\infty$,
such that the **explicit formula** holds:
$$\sum_{\rho\in Z}\hat f(\rho) \;=\; W_X(f)\qquad\text{for every } f\in C_c^\infty(G),$$
with absolute convergence of the left-hand side (automatic: Paley–Wiener gives
$|\hat f(\rho)|\ll_N(1+|\mathrm{Im}\,\rho|)^{-N}$ uniformly on strips, and
$N_Z(T)\ll T^A$; Doc 107 Lemma 1.2, same argument). $\mathcal{A}rith^{EF}$ is the
category of such pairs; the **comparison functor**
$U:\mathcal{A}rith^{EF}\to\mathcal{A}rith$ forgets $Z$.

**[DATA].** $(\zeta_{\mathrm{ob}}, Z_\zeta)$ with $Z_\zeta$ = the nontrivial zeros of ζ
is a spectral object: this is Doc 107's Theorem 1.4 (Weil 1952). Likewise for
every Dirichlet $L$-function, and for Davenport–Heilbronn (the explicit formula of a
linear combination of $L$'s with the same functional equation is obtained by the same
contour; its divisor is the zero set of $D$).

**[PROPOSITION 4.2].** (a) The divisor of a spectral object is determined by
$X$ in the following sense: if $(X,Z)$ and $(X,Z')$ are spectral, then
$\sum_{Z}\hat f(\rho)=\sum_{Z'}\hat f(\rho)$ for every $f$. (b) If $(X,Z)$ is
spectral, $(\sigma X,\,\sigma Z)$ is spectral with
$\sigma Z := \{1-\bar\rho:\rho\in Z\}$. In particular, if $X$ is Hermitian, $Z$ is
$\sigma$-stable as a multiset **if** the spectral pair with divisor $\sigma Z$
coincides with that of $Z$ in the sense of (a); for the catalogue's objects
(ζ, Hermitian Dirichlet $L$'s, D–H, $F_{p,\alpha}$) the $\sigma$-stability of the divisor
holds with equality of multisets [DATA: functional equation + Schwarz
reflection].

*Proof.* (a) Both equal $W_X(f)$. (b) By Prop. 2.8(b):
$W_{\sigma X}(f) = \overline{W_X(\tilde f)} = \overline{\sum_Z\widehat{\tilde f}(\rho)}
= \overline{\sum_Z \overline{\hat f(1-\bar\rho)}} = \sum_{\sigma Z}\hat f(\rho)$;
the density and strip bounds are preserved. $\square$

*(Frank statement: I do not claim pointwise uniqueness of the multiset $Z$
from the functional — the category **carries** the divisor as a datum, it does not
reconstruct it; that is exactly the design decision §7 discusses against
Doc 110.)*

### 4.2. The evaluation lemma

**[LEMMA 4.3] (evaluation).** Let $s_1,\dots,s_k\in\mathbb{C}$ be distinct. The map
$\mathrm{ev}:C_c^\infty(G)\to\mathbb{C}^k$, $f\mapsto(\hat f(s_1),\dots,\hat f(s_k))$,
is surjective.

*Proof.* If not, there is $\lambda\ne0$ with $\sum_j\lambda_j\hat f(s_j)=0$ for
every $f$, i.e. $\int_0^\infty f(x)\bigl[\sum_j\lambda_j x^{s_j-1}\bigr]dx=0$ for
every $f\in C_c^\infty$; the continuous function $\sum_j\lambda_j x^{s_j-1}$ is then
identically zero on $(0,\infty)$. With $x=e^u$: $\sum_j\lambda_j e^{(s_j-1)u}=0$
for every $u\in\mathbb{R}$; applying $(d/du)^m$ at $u=0$:
$\sum_j\lambda_j(s_j-1)^m=0$ for every $m\ge0$ — a Vandermonde system on the
$k$ distinct values $s_j-1$, of rank $k$: $\lambda=0$, a contradiction. $\square$

### 4.3. The orbit theorem: the signature of every block

**[THEOREM 4.4] (orbits and signature, for the whole category).** Let $(X,Z)$ be
Hermitian spectral with $Z$ $\sigma$-stable (multiplicities $m_\rho =
m_{\sigma\rho}\in\mathbb{Z}_{\ge1}$). Then:

(a) For every $f$: $Q_X(f,f) = \sum_{\rho\in Z} m_\rho\,\hat f(\rho)\,
\overline{\hat f(\sigma\rho)}$ (absolutely convergent).

(b) Let $S\subseteq Z$ be finite and $\sigma$-stable, $S = S_{\mathrm{on}}\sqcup
S_{\mathrm{orb}}$ with $S_{\mathrm{on}}$ the fixed points of $\sigma$ (i.e.
$\mathrm{Re}\,\rho=\tfrac12$) and $S_{\mathrm{orb}}$ a union of $n_{\mathrm{orb}}$
free orbits $\{\rho,\sigma\rho\}$. The block Hermitian form
$$B_S(v,v) := \sum_{\rho\in S} m_\rho\,v_\rho\,\overline{v_{\sigma\rho}},
\qquad v\in\mathbb{C}^S,$$
has signature exactly
$$\mathrm{sig}(B_S) = \bigl(\,\#S_{\mathrm{on}} + n_{\mathrm{orb}},\ \ n_{\mathrm{orb}}\,\bigr),$$
and by Lemma 4.3 it is realized with full rank over the test class (the evaluation
map over $S$ is surjective).

(c) If $Z$ is finite, $\mathrm{sig}(Q_X) = (\#Z_{\mathrm{on}}+n_{\mathrm{orb}},\,
n_{\mathrm{orb}})$ exactly (as a form on $C_c^\infty(G)/\ker$).

*Proof.* (a) $Q_X(f,f) = W_X(f\star\tilde f) = \sum_Z m_\rho\,
\widehat{f\star\tilde f}(\rho)$ and $\widehat{f\star\tilde f}(\rho) =
\hat f(\rho)\overline{\hat f(1-\bar\rho)} = \hat f(\rho)\overline{\hat f(\sigma\rho)}$.
(b) Orthogonal decomposition by orbits: for fixed $\rho$ ($\sigma\rho=\rho$), the
term is $m_\rho|v_\rho|^2$: a positive direction. For a free orbit
$\{\rho,\rho'\}$ ($\rho'=\sigma\rho\ne\rho$): the two terms are
$m(v_\rho\bar v_{\rho'} + v_{\rho'}\bar v_\rho) = 2m\,\mathrm{Re}(v_\rho\bar v_{\rho'})$
— the hyperbolic plane, eigenvalues $\pm m$: signature $(1,1)$. Summing:
$(\#S_{\mathrm{on}}+n_{\mathrm{orb}},\,n_{\mathrm{orb}})$. Realization: by the
Lemma 4.3 there exists, for every $v\in\mathbb{C}^S$, an $f$ with $\hat f|_S=v$ (and
nothing is required outside $S$). (c) With $Z$ finite, $Q_X(f,f)=B_Z(\mathrm{ev}f,\mathrm{ev}f)$ and
$\mathrm{ev}$ is surjective: the form induced on the quotient is exactly
$B_Z$. $\square$

**[COROLLARY 4.5] (the category's universal inequality).** For every
Hermitian spectral object with finite divisor, $\mathrm{sig}(Q_X)=(p,q)$ satisfies
$$q \;\le\; p,$$
with equality if and only if the divisor does not touch the critical line; and $q=0$ if and only if
$Z\subset\{\mathrm{Re}=\tfrac12\}$. The same holds block by block for infinite
divisors. **At most half of the directions of any block are
negative, for any arithmetic function**: it is the universal fingerprint of the
involution $\sigma$, not of ζ. $\square$

### 4.4. Realization and classification

**[THEOREM 4.6] (classification of achievable signatures).** The map
$$\{\text{Hermitian spectral objects with finite divisor}\}\ \longrightarrow\
\{(p,q)\in\mathbb{Z}_{\ge0}^2\},\qquad X\mapsto\mathrm{sig}(Q_X),$$
has image exactly $\{(p,q): q\le p\}$.

*Proof.* "$\subseteq$": Corollary 4.5. "$\supseteq$": given $q\le p$, let
$Z := \{\tfrac12+i,\dots,\tfrac12+i(p-q)\}\cup\{\tfrac12\pm\delta+i\gamma_j:
j=1..q\}$ (with $\delta\in(0,\tfrac12)$, distinct heights $\gamma_j$, and adding
the conjugates if desired — irrelevant for the count: each quadruple
adds free orbits and the count is adjusted; let us take the minimal version with
pairs $\{\tfrac12+\delta+i\gamma_j,\ \tfrac12-\delta+i\gamma_j\}$, which is already
$\sigma$-stable). The object $X_Z=(0,\sum_{\rho\in Z}[\rho],0)$ is Hermitian
(the polar block is $\sigma$-stable with weights 1) and spectral with divisor $Z$
(trivially: $W_{X_Z}(f)=\sum_Z\hat f(\rho)$ is the definition). It has
$\#Z_{\mathrm{on}}=p-q$ fixed points and $q$ free orbits: signature
$(p-q+q,\,q)=(p,q)$ by Theorem 4.4(c). $\square$

**Remark.** The realization uses that in $\mathcal{A}rith$ the polar block admits
arbitrary points: the "zeros" of the artificial objects are polar atoms. This
is not a trick — it is the content: **the category is genuinely larger than
the L-functions**, and the theorems of §4 hold on that whole breadth. What
distinguishes the L-type objects is the structure of the datum $a$ (§1.2, §6.7), not
the signature.

### 4.5. The tensor-index identity (imported from Doc 106)

**[THEOREM 4.8] (tensor index).** Let $A$, $B$ be non-degenerate Hermitian
forms of signature $(p_1,q_1)$, $(p_2,q_2)$ on finite-dimensional spaces $V,W$.
Then $A\otimes B$ on $V\otimes W$ has signature
$$\mathrm{sig}(A\otimes B) = \bigl(p_1p_2+q_1q_2,\ \,p_1q_2+q_1p_2\bigr).$$

*Proof.* By Sylvester, there are bases in which $A=\mathrm{diag}(\epsilon_i)$,
$B=\mathrm{diag}(\eta_j)$ with $\epsilon_i,\eta_j\in\{\pm1\}$. In the basis
$e_i\otimes f_j$, $A\otimes B = \mathrm{diag}(\epsilon_i\eta_j)$: the number of
$+1$ products is $p_1p_2+q_1q_2$ and of $-1$ products is $p_1q_2+q_1p_2$. The signature is
an invariant of the form (law of inertia). $\square$

**Consequence in the category.** For an off-block of a quadruple ($m=1$:
signature $(2,2)$), the tensor square has negative index
$2\cdot2+2\cdot2=8=(4m)^2/2$ — Doc 106's Prop. 3.5 and Doc 107's Theorem 5.5
(signature $(8,8)$), now as an instance of a linear-algebra theorem of the
category, valid for the off-block of **any** Hermitian spectral object. The
analytic realization of the square (the double functional over thickened
kernels, with $\hat g$ in the sum and $\hat\varphi$ in the difference) is inherited
from Doc 107 §3 unchanged: the computation of the double Mellin (Theorem 3.4
there) uses no ζ.

### 4.6. The double explicit formula for spectral objects

**[THEOREM 4.9].** If $(X,Z)$ is spectral, for every $h\in C_c^\infty(G^2)$:
$$\deg_X(h) \;=\; \sum_{\rho_1\in Z}\sum_{\rho_2\in Z}\hat h(\rho_1,\rho_2),$$
with absolute convergence of the double sum.

*Proof.* As in Doc 107 Lemma 2.2(b): by Prop. 3.2,
$\deg_X(h) = W_X^{(1)}[F]$ with $F(x)=W_X^{(2)}[h(x,\cdot)]\in C_c^\infty$; applying
the explicit formula (Def. 4.1) in variable 1:
$\deg_X(h) = \sum_{\rho_1}\hat F(\rho_1)$, and
$\hat F(\rho_1) = W_X^{(2)}[x_2\mapsto\int h(x_1,x_2)x_1^{\rho_1-1}dx_1] =
\sum_{\rho_2}\hat h(\rho_1,\rho_2)$ — the exchange
$\int dx_1\leftrightarrow W^{(2)}$ is legitimate block by block (finite sums and
absolutely convergent integrals over compacts). Double absolute
convergence: Paley–Wiener in two variables + $N_Z(T)\ll T^A$ in each factor. $\square$

---

## 5. The toy index as a theorem of the category

### 5.1. Intersection structures

**[NEW-DEFINITION 5.1].** A **rank-3 intersection structure of genus
$g\in\mathbb{R}_{\ge0}$** on an object $X$ is a symmetric $\mathbb{R}$-bilinear
form $(\,\cdot\,)$ on the lattice $N_X := \mathbb{Z}f_1\oplus\mathbb{Z}f_2
\oplus\mathbb{Z}\Delta$ of correspondence classes (fibers and diagonal) with the
axioms:
**(I1)** $f_1^2=f_2^2=0$; **(I2)** $f_1\!\cdot\!f_2=1$; **(I3)**
$\Delta\!\cdot\!f_1=\Delta\!\cdot\!f_2=1$; **(I4)** $\Delta^2=2-2g$ (adjunction).
*(The properties that Doc 125 computed in the tropical toy — §4 there — are here
the axioms; the theorem says what they force.)*

**[THEOREM 5.3] (toy index, general).** Let $(\,\cdot\,)$ be an intersection
structure of genus $g$ on any object. Then its Gram matrix in
$(f_1,f_2,\Delta)$ is $G_g=\begin{pmatrix}0&1&1\\1&0&1\\1&1&2-2g\end{pmatrix}$, with
$\det G_g = 2g$, and:

(a) If $g\ge1$ (indeed if $g>0$): signature $(1,2)$; the class $H=f_1+f_2$ satisfies
$H^2=2>0$; and on the primitive part $H^\perp$ the form is **negative definite**, with
matrix $\mathrm{diag}(-2,-2g)$ in the basis $e_1=f_1-f_2$, $e_2=f_1+f_2-\Delta$.

(b) If $g=0$: the form degenerates, with radical generated by $e_2=f_1+f_2-\Delta$
and signature $(1,1,0)$ (one positive, one negative, one zero). **The Hodge index
fails exactly at genus 0.**

*Proof.* Gram: (I1)–(I4). Determinant:
$\det G_g = 0\cdot[0(2-2g)-1] - 1\cdot[(2-2g)-1] + 1\cdot[1-0] = -(1-2g)+1 = 2g$.
(a) $g>0$: $\det>0$; the top-left $2\times2$ minor $\begin{psmallmatrix}0&1\\1&0
\end{psmallmatrix}$ has determinant $-1<0$, hence the form is indefinite; a
non-degenerate real symmetric $3\times3$ form with $\det>0$ has signature $(3,0)$ or
$(1,2)$; indefinite $\Rightarrow(1,2)$. $H^2=(1,1,0)G_g(1,1,0)^T = 2$.
Primitive part: $G_gH = (1,1,2)^T$, condition $x_1+x_2+2x_3=0$; basis $e_1=(1,-1,0)$,
$e_2=(1,1,-1)$. $G_ge_1 = (-1,1,0)^T$, $e_1^TG_ge_1=-2$;
$G_ge_2 = (0,\,0,\,2g)^T$ (third entry: $1+1-(2-2g)=2g$), $e_2^TG_ge_2 = -2g$;
$e_1^TG_ge_2 = 0$. Primitive form $\mathrm{diag}(-2,-2g)$: negative definite
$\iff g>0$. (b) $g=0$: $G_0e_2 = 0$ (the computation above with $g=0$), radical
$\ni e_2$; in the quotient only $f_1,f_2$ remain with form
$\begin{psmallmatrix}0&1\\1&0\end{psmallmatrix}$: signature $(1,1)$. $\square$

### 5.2. Which class of objects realizes it

**[NEW-DEFINITION 5.4].** An object $X=(a,c,\omega)$ is **periodic of period
$L$** if its discrete datum lives on a geometric progression: $a$ supported on
$\{p^m\}$ with $L=\log p$ ("one-prime" objects; more generally, support on
$e^{L\mathbb{Z}}$). Its effective scale group is $C_L := G/e^{L\mathbb{Z}}$, a
circle; its effective correspondences live on the torus $C_L\times C_L$, with
classes $f_1$ (horizontal), $f_2$ (vertical), $\Delta=\Delta_1$, and the
translations $\Delta_\mu$ (Doc 125 §2.4).

**[CONSTRUCTION 5.5] (realization at genus 1; status: imports the tropical
computation of Doc 125, verified there with a double check).** For a periodic
object, the stable Allermann–Rau intersection over $C_L\times C_L$ (Doc 125 §3.1, [DATA
arXiv:0709.3705]) defines an intersection structure on
$N_X=\langle f_1,f_2,\Delta\rangle$ with (I1)–(I3) and $\Delta^2=0$, i.e. **genus
$g=1$** (Doc 125 §4: homology of the torus and tropical adjunction coincide). By
Theorem 5.3(a): signature $(1,2)$, negative-definite primitive part
$\mathrm{diag}(-2,-2)$. **Doc 125's signature $(1,2)$ is not a fact about ζ nor
about the prime $p$: it is Theorem 5.3 evaluated at $g=1$, valid for arbitrary
coefficients $a$ of the periodic object.** The dependence on $p$ is only the
overall scale $\log p$ (which does not change signatures).

**Remark 5.6 (the inherited obstacle, stated).** What is NOT imported: (i) the
step to the infinite lattice of correspondences $\Delta_\mu$ (density of
slopes, reality of the intersection number — G-125.A) and (ii) persistence of the
signature at infinite rank (Babaee–Huh — G-125.B). Theorem 5.3 is rank 3;
its categorical value is separating the content (the signature is a formal
consequence of (I1)–(I4) with $g\ge1$) from the wall (extending (I1)–(I4) to the
full lattice with two incommensurable primes). The wall remains in §9 as a
named goal.

**Remark 5.7 (genus 0 and Spec ℤ).** The RR of Connes–Consani gives genus 0 for
$\mathrm{Spec}\,\mathbb{Z}$ (Doc 124 §3.3, via [DATA arXiv:2307.06748]). In the
category, Theorem 5.3(b) says what that means: **at genus 0 the rank-3
intersection form is degenerate and there is no Hodge index to read.** The
object carrying a useful intersection structure must have genus $\ge1$ — the
periodic blocks have it ($g=1$); the problem of assembling the blocks (a
global object of infinite genus) is the categorical form of gap MW-5/L6.

---

## 6. Axiom H

### 6.1. Statement

**[NEW-DEFINITION 6.1] (Axiom H).** A Hermitian object $X=(a,c,\omega)$
**satisfies H** if
$$Q_X(f,f) \;=\; W_X(f\star\tilde f)\;\ge\;0\qquad\text{for every }f\in C_c^\infty(G).$$
The statement uses only the data $(a,c,\omega)$: **it mentions no zeros of
anything** — $W_X$ is the finite sum/integral of Definition 2.1. Two-variable
version (**H₂**): $\deg_X(h\star_{\!G^2}\tilde h)\ge0$ for every thickened kernel $h$.

**[PROPOSITION 6.2] (H from the line; the whole category).** If $(X,Z)$ is
Hermitian spectral with $Z\subset\{\mathrm{Re}\,s=\tfrac12\}$, then $X$
satisfies H and H₂.

*Proof.* Theorem 4.4(a): $Q_X(f,f) = \sum_Z m_\rho\hat f(\rho)
\overline{\hat f(\sigma\rho)}$ and $\sigma\rho=\rho$ on the line: $Q_X(f,f) =
\sum m_\rho|\hat f(\rho)|^2\ge0$. For H₂: Theorem 4.9 with
$\widehat{h\star\tilde h}(\rho_1,\rho_2) = \hat h(\rho_1,\rho_2)
\overline{\hat h(\sigma\rho_1,\sigma\rho_2)} = |\hat h(\rho_1,\rho_2)|^2$. $\square$

**[THEOREM 6.3] (H by blocks; unconditional converse at block level).** If
$(X,Z)$ is Hermitian spectral and $Z$ contains some $\rho_0$ with
$\mathrm{Re}\,\rho_0\ne\tfrac12$, then **every** block form $B_S$ with
$S\supseteq\{\rho_0,\sigma\rho_0\}$ is indefinite (it has a negative direction
realized on the test class). That is: the block version of H
("$B_S\ge0$ for every finite $\sigma$-stable block") **is equivalent** to
$Z\subset\{\mathrm{Re}=\tfrac12\}$, unconditionally, for every object of
$\mathcal{A}rith^{EF}$.

*Proof.* Theorem 4.4(b): the free orbit $\{\rho_0,\sigma\rho_0\}$ contributes a
hyperbolic plane; Lemma 4.3 realizes the vector $(v_{\rho_0},v_{\sigma\rho_0}) =
(1,-1)$, on which $B = -2m_{\rho_0}<0$. The equivalence: Prop. 6.2 +
this. $\square$

*(The relation H $\Rightarrow$ H-by-blocks in general — i.e. that the negativity of
a block transports to a negativity of the full functional against the positive
tide of the rest of the divisor — is the "Hypothesis D"-type separation of the
program (P35; Doc 96 Theorem 8.1): proved below for lattice divisors (§6.5) and
finite ones; stated as a [BRIDGE] in general. This frankness matters in §6.6.)*

### 6.2. Verification 1: the constant function

**[PROPOSITION 6.4].** $X_1$ ($a\equiv1$, $c=0$, $\omega=0$) does **not** satisfy H.

*Proof.* For real $f$, $g:=f\star\tilde f$ satisfies $g(1/x) =
\overline{g(x)}\,x$ (Hermitianness of $g$: $\tilde g=g$), hence
$n^{-1}g(1/n)=\overline{g(n)}$ and
$Q_{X_1}(f,f) = -\sum_{n\ge1}\bigl[g(n)+\overline{g(n)}\bigr]
= -2\sum_{n\ge1}\mathrm{Re}\,g(n).$
Take $f\ge0$ real, $f\not\equiv0$, with support in $[\tfrac12,3]$ (width greater than
an octave): $g(n) = \int f(y)\,f(y/n)\,(y/n)\,d^*y\ \ge 0$ for every $n$, and
$g(1) = \int f(y)^2\,y\,d^*y > 0$. Then $Q_{X_1}(f,f)\le -2g(1)<0$. $\square$

### 6.3. Verification 2: completely multiplicative functions and diagonal mass

**[PROPOSITION 6.5] (diagonal mass).** Let $X=(a,0,0)$ be Hermitian with $a(1)=0$ and
$a\not\equiv0$. Then $X$ does not satisfy H. In particular, **no**
object $X_h$ ($a = h\Lambda$, $h$ completely multiplicative with values $\pm1$ —
random or not) satisfies H: the failure is deterministic, for every $h$.

*Proof.* Let $n_0\ge2$ be minimal with $a(n_0)\ne0$ ($a$ real by Hermitianness).
Take $u\ge0$ a real bump with support in $[e^{-\epsilon},e^{\epsilon}]$,
$\epsilon<\tfrac14\log n_0$ (smaller than any relevant logarithmic
separation), and $f := u + \tau\,u(\cdot/n_0)$ with $\tau\in\mathbb{R}$. Then
$g=f\star\tilde f$ satisfies: $g(n)=0$ except for $n$ such that $\log n$ is at
distance $<2\epsilon$ from $\{0,\pm\log n_0\}$; the integers thereby reached are at most
$n=1$ and $n=n_0$ (and $1/n_0$, entering via the mirror term). Computation of the
values (weight $(y/x)$ of the kernel $g(x)=\int f(y)\overline{f(y/x)}(y/x)\,d^*y$):
$g(1) = \int|f|^2y\,d^*y = (1+O(\epsilon)) + \tau^2 n_0(1+O(\epsilon))$, but the
coefficient of $g(1)$ is $a(1)=0$: it does not contribute. $g(n_0) =
\tau\int u(y/n_0)^2 (y/n_0)\,d^*y = \tau(1+O(\epsilon))$. Then
$Q_X(f,f) = -\,a(n_0)\bigl[g(n_0)+\overline{g(n_0)}\bigr] =
-2a(n_0)\tau(1+O(\epsilon))$, and choosing the sign of $\tau$ (=$\mathrm{sgn}\,
a(n_0)$, with $|\tau|$ small so the $O(\epsilon)$ does not interfere) gives
$Q_X<0$. For $X_h$: $a(2)=h(2)\log2\ne0$. $\square$

**Structural reading.** H requires **positive mass on the diagonal** (atom at $x=1$,
polar block, or archimedean density): without it, any nonzero discrete coefficient is a
negative direction with a free choice of phase. In ζ, that mass is provided by the
poles $[0]+[1]$ and $-\Omega$ (the zero density); in the $F_{p,\alpha}$
objects below, it is provided by $\omega\equiv-2\log p$. Weil positivity is always
"diagonal versus cross terms" — the category exhibits it as a data dichotomy.

### 6.4. The Poisson formula for Euler factors

**[THEOREM 6.6] (explicit Poisson formula, one factor).** Let $p$ be prime,
$L=\log p$, $\alpha\in\mathbb{C}^\times$, and $Z(\alpha) := \{s:p^s=\alpha\} =
\{\log_p\alpha + 2\pi ik/L : k\in\mathbb{Z}\}$ (a vertical progression). For every
$f\in C_c^\infty(G)$:
$$\sum_{\rho\in Z(\alpha)}\hat f(\rho) \;=\; L\sum_{m\in\mathbb{Z}}\alpha^m f(p^m),$$
both sides absolutely convergent (left: Paley–Wiener; right: finite sum).

*Proof.* Write $\alpha = p^\beta e^{i\phi}$ ($\beta=\log_p|\alpha|$),
$\rho_k = \beta+i(\phi+2\pi k)/L$. With $x=e^t$ and $F(t) := f(e^t)\,e^{\beta t}
e^{i\phi t/L}\in C_c^\infty(\mathbb{R})$:
$\hat f(\rho_k) = \int F(t)\,e^{2\pi ikt/L}\,dt = \widehat F(2\pi k/L)$.
The Poisson summation formula for $F\in C_c^\infty$ [classical DATA; proof:
Fourier series of the periodization $\sum_m F(t+mL)$, which is finite and $C^\infty$]:
$\sum_k\widehat F(2\pi k/L) = L\sum_m F(mL) = L\sum_m f(p^m)\,p^{\beta m}e^{i\phi m}
= L\sum_m \alpha^m f(p^m)$. $\square$

**[NEW-DEFINITION / PROPOSITION 6.6'].** The **one-prime Euler object**
$F_{p,\alpha}$, for $1<|\alpha|<p$: the spectral pair with divisor
$Z_F := Z(\alpha)\sqcup Z(p/\bar\alpha)$ and functional
$$W_F(f) = L\sum_{m\in\mathbb{Z}} c_m\,f(p^m),\qquad c_m := \alpha^m+(p/\bar\alpha)^m.$$
It is an object of $\mathcal{A}rith^{EF}$, Hermitian, with data: $a(p^m) = -L\,c_m$
for $m\ge1$ (and $\bar a$ in the mirror positions: consistent because $c_{-m} = \bar c_m\,
p^{-m}$, direct computation), $c=0$, and the atom $m=0$ ($c_0=2$) realized as the
archimedean block $\omega\equiv-2L$ (inverse Mellin: $f(1) = \tfrac1{2\pi}\int
\hat f(\tfrac12+it)\,dt$). The divisor: two vertical progressions at
$\mathrm{Re}=\beta$ and $\mathrm{Re}=1-\beta$, $\sigma$-stable
($\sigma Z(\alpha) = Z(p/\bar\alpha)$: $1-\bar\rho$ with $p^{\bar\rho}=\bar\alpha$ gives
$p^{1-\bar\rho}=p/\bar\alpha$), linear density. The explicit formula is
Theorem 6.6 summed over the two factors. Note: **$F_{p,\alpha}$ has an Euler
product** in the sense of Theorem 1.9 (its $a$ is supported on powers of a single
prime), and its diagonal mass is archimedean, as in ζ. $\square$

### 6.5. Verification 3 — the central theorem: local purity

**[THEOREM 6.7] (local purity: H is decidable in the one-prime subcategory).**
For $1<|\alpha|<p$:
$$F_{p,\alpha}\ \text{satisfies H}\quad\Longleftrightarrow\quad |\alpha|=\sqrt p
\quad\Longleftrightarrow\quad |c_m|\le 2\,p^{m/2}\ \ \forall m\ge1.$$

*Proof.* **($|\alpha|=\sqrt p\Rightarrow$H):** the divisor falls on
$\mathrm{Re}=\tfrac12$; Prop. 6.2. **(The two right-hand characterizations):**
if $|\alpha|=p^{1/2+\delta'}$, then $|c_m|\ge p^{m(1/2+\delta')} -
p^{m(1/2-\delta')} = p^{m/2}(p^{m\delta'}-p^{-m\delta'})$, which exceeds $2p^{m/2}$
for $m$ large if $\delta'\ne0$; and if $\delta'=0$, $c_m = 2p^{m/2}
e^{im\phi}\cos(0)$… more precisely $\alpha=\sqrt p\,e^{i\phi}$ implies
$p/\bar\alpha = \sqrt p\,e^{i\phi}=\alpha$ and $c_m=2\alpha^m$, $|c_m|=2p^{m/2}$.

**($|\alpha|\ne\sqrt p\Rightarrow\neg$H) — the Mertens two-bump test.** Without
loss of generality $\delta'>0$ (otherwise exchange $\alpha
\leftrightarrow p/\bar\alpha$, the same object). Let $M\ge1$ be fixed later, $\epsilon <
L/4$, $u$ = a real bump $\ge0$, $u(e^t) = \epsilon^{-1/2}\chi(t/\epsilon)$ with
$\chi$ even, $\int\chi^2=1$. Test: $f := u + \theta\,u(\cdot/p^{M})$ with
$\theta\in\mathbb{C}$. Let $g=f\star\tilde f$, $g(x) = \int f(y)\overline{f(y/x)}
\,(y/x)\,d^*y$. By support ($\epsilon<L/4$), $g(p^m)=0$ except for $m\in\{0,\pm M\}$, and:
$$g(1) = \int|f|^2\,y\,d^*y = \bigl(1+|\theta|^2p^{M}\bigr)(1+O(\epsilon)),$$
$$g(p^{M}) = \theta\!\int u(y/p^M)^2\,(y/p^M)\,d^*y = \theta\,(1+O(\epsilon)),
\qquad g(p^{-M}) = \bar\theta\,p^{M}(1+O(\epsilon))$$
(the last: $\int u(y)\overline{\theta u(yp^{M}/p^{M})}\dots$ — direct computation, and
consistent with Hermitianness $g(1/x)=\overline{g(x)}\,x$). Then, using
$c_{-M}\,p^{M} = \bar c_M$:
$$Q_F(f,f) = L\bigl[c_0\,g(1) + c_M\,g(p^M) + c_{-M}\,g(p^{-M})\bigr]
= L\bigl[\,2\bigl(1+|\theta|^2p^{M}\bigr) + 2\,\mathrm{Re}(c_M\theta)\,\bigr]
(1+O(\epsilon)).$$
Choose $\theta = -\,\overline{c_M}\,t/|c_M|$ with $t>0$:
$Q_F/L = \bigl[\,2 + 2p^{M}t^2 - 2|c_M|\,t\,\bigr](1+O(\epsilon))$. The minimum at
$t^* = |c_M|/(2p^{M})$ equals $2 - |c_M|^2/(2p^{M})$, which is $<0$ as soon as
$|c_M| > 2p^{M/2}$ — which occurs for $M$ large enough because
$|c_M|\ge p^{M/2}(p^{M\delta'}-p^{-M\delta'})\to\infty\cdot p^{M/2}$. Fix such $M$,
then $\epsilon$ small enough to absorb the $O(\epsilon)$ terms:
$Q_F(f,f)<0$. $\square$

**Exact remarks.** (i) The barrier of the test is **exactly** $|c_m|\le
2p^{m/2}$: the Ramanujan–purity bound. In the pure case the inequality
$2|\mathrm{Re}(c_M\theta)|\le 2(1+|\theta|^2p^M)$ is exact Cauchy–Schwarz
($|c_M|=2p^{M/2}$): positivity is as tight as it can be. (ii) The test is the
Mertens mechanism ($3+4\cos\theta+\cos2\theta$, two frequencies against the diagonal
mass) in categorical form: bump at $1$ = diagonal mass,
bump at $p^M$ with adversarial phase = coefficient. (iii) **Structural
consequence: the Euler product does not imply H.** $F_{p,\alpha}$ with
$|\alpha|=p^{0.6}$ has an Euler product (Theorem 1.9), a functional equation
(Hermitian), positive diagonal mass — and violates H. The discriminator of H within
the Euler objects is **purity of the local weights**, not multiplicativity.

### 6.6. Verification 4: Davenport–Heilbronn, and the resolved tension

**[DATA].** The Davenport–Heilbronn function has a functional equation of
$\zeta$ type (Hermitian, $\sigma$-stable) and **zeros off the critical line** in
$\tfrac12<\mathrm{Re}\,s<1$ (Davenport–Heilbronn 1936 for zeros in
$\mathrm{Re}\,s>1$; Spira 1968 and Balanzario–Sánchez-Ortiz 2007 exhibit zeros in
the critical strip off the line; Titchmarsh §10.25). It has no Euler product
(it is a linear combination of two $L$'s).

**[PROPOSITION 6.8].** (a) $X_{DH}$ violates the block version of H
**unconditionally**: Theorem 6.3 applied to a free orbit
$\{\rho_0,1-\bar\rho_0\}$ of its divisor produces a hyperbolic block with a
negative direction realized on the test class. (b) The violation of full H
($Q_{DH}(f,f)<0$ for an explicit test) follows from (a) plus the separation of
the block against the on-line tide — the same Hypothesis-D-type statement that the
program states for ζ; status: [BRIDGE], not proved here in general (proved
above when the divisor is a lattice divisor or a finite one).

*Proof.* (a) is Theorem 6.3 + [DATA]. (b) is the frank delimitation of
§6.1. $\square$

**The tension the goal anticipated, resolved.** The question was: "if your Axiom H
holds for D–H, then H cannot imply zeros on the line". The opposite happens and
it is better: **H fails for D–H** (at block level, unconditionally), because in
this category H *does* imply zeros on the line for **all** Hermitian spectral
objects (Theorem 6.3: H-by-blocks $\iff$ divisor on the line — Weil's criterion
categorified, external to ζ by construction). The content question then shifts
to: **what arithmetic data force H?** And there the category
provides answers with proof:
- a functional equation (Hermitian) **is not enough**: D–H;
- Euler product + functional equation + diagonal mass **are not enough**:
  impure $F_{p,\alpha}$ (Theorem 6.7);
- what separates the H cases from the non-H cases in every decidable example is a
  **positivity/purity of the discrete datum** — in $F_{p,\alpha}$, literally
  $|c_m|\le2p^{m/2}$; in ζ, the candidate is $a=\Lambda\ge0$ (the impure
  counterexamples $F_{p,\alpha}$ have $a$ of non-constant or complex sign; D–H too).

**[WISH 6.9] (Conjecture H⁺).** *If $X$ is Hermitian, spectral, with $a\ge0$
supported on prime powers (Euler product), standard polar block
($c=[0]+[1]$), and $\omega$ of archimedean type, then $X$ satisfies H.*
— It implies RH (ζ qualifies): it is RH-hard, nothing is claimed. Its value is
design-level: it is an NC2-conforming statement (it quantifies over a class of
data, not over ζ), and it is **falsifiable within the category**: a
counterexample would be a constructible object (e.g. interference of two primes with
$a\ge0$ and an off-line zero). Looking for the counterexample is a concrete task
for Phase 44; if it does not exist, understanding why is exactly the content of RH
seen from here.

---

## 7. [BRIDGE] H and RH; the position relative to Doc 110

### 7.1. The bridge, without disguise

**[BRIDGE 7.1].** For the object $\zeta_{\mathrm{ob}}$:
$$\mathrm{RH}\ \Longrightarrow\ H(\zeta_{\mathrm{ob}})\quad
\text{(Prop. 6.2, proved here, instance of the categorical theorem)};$$
$$H(\zeta_{\mathrm{ob}})\ \Longrightarrow\ \mathrm{RH}\quad
\text{[DATA: Weil's criterion; Weil 1952, Bombieri 2000]}.$$
**$H(\zeta_{\mathrm{ob}})$ is RH-equivalent. Stated.** The category does not turn
RH into something else; the legitimate question is whether it **redistributes**
the difficulty.

### 7.2. Which hypothesis of the impossibility theorem we violate (Doc 110)

Doc 110's Theorem 4.3 proves that in class
$\mathcal{F}$ (indices $I=\mathrm{neg.ind}(Q|_{V'})$ with $Q$ of explicit-formula
type and $V'$ **test-accessible**, Def. 4.2(ii)) axioms (L2)+(L3)+(L4) are
inconsistent. The axioms of $\mathcal{A}rith^{EF}$ violate **exactly hypothesis
(ii) (test-accessibility)**: the divisor $Z$ is a *structural datum of the
object* — the blocks $B_S$ are indexed by subsets of the divisor, not specified by
supports/windows of tests. That is why Theorem 4.4 (block signatures, integer,
finite a priori — the mechanism of Doc 110's Prop. 4.5: finite rank $\Rightarrow$
readable inertia) coexists without contradiction with the impossibility theorem: we
are not in $\mathcal{F}$.

The price, said plainly: for ζ, the functors of $\mathcal{A}rith^{EF}$
presuppose the divisor. **All the program's non-autonomy is concentrated in a
single place: the comparison functor $U:\mathcal{A}rith^{EF}\to\mathcal{A}rith$ and
the question of which objects of $\mathcal{A}rith$ admit a spectral lift with
divisor on the line.** H is the criterion (it lives below, in $\mathcal{A}rith$,
with no zeros); the orbit theorem is the obstruction (it lives above). Doc 108's
formula §7.4 ("autonomy of the value ≠ autonomy of the inertia") becomes:
*the value lives in $\mathcal{A}rith$, the inertia in $\mathcal{A}rith^{EF}$, and RH is
a property of the functor $U$ restricted to the point ζ.*

### 7.3. What the category redistributes (frank balance)

**In favor (proved):** (i) H is **decidable** in genuine subcategories: finite
divisors (Theorem 4.4(c)), one-prime objects (Theorem 6.7: purity, a closed
criterion), and by blocks in all of $\mathcal{A}rith^{EF}$ (Theorem 6.3). (ii) The
structure theorems (orbits, $q\le p$, tensorial, toy $(1,2)$) are external
to ζ by construction and survive any local refutation: they are mathematics of
the framework, not of the goal. (iii) The constructed counterexamples ($F_{p,\alpha}$
impure) **prove** that certain shortcuts (Euler $\Rightarrow$ H) are false — the
category prunes the space of strategies with theorems, not heuristics.

**Against (stated):** (iv) verifying H for ζ is Weil's criterion:
no direct progress. (v) The block$\to$functional step (separation against the
on-line tide) is Hypothesis D under another name, except in the resolved
subcategories. (vi) The step "H for truncated Euler $\Rightarrow$ H for ζ" collides
with the discontinuity of signatures in limits (T2, Doc 119; Babaee–Huh, Doc 125) —
the next [WISH] names it.

**[WISH 7.2] (Limit-rigidity lemma).** *Let $X_S$ be the family of truncated
Euler objects (data $a\cdot 1_{p\le y}$ with ζ's polar/archimedean block —
CCM's semilocal objects, Doc 110 §3, read in $\mathcal{A}rith$). If each
$X_S$ satisfies H with quantitative gap $\mu_S\ge0$ and the $\deg$-functionals
converge to those of $\zeta_{\mathrm{ob}}$, then $H(\zeta_{\mathrm{ob}})$.* — The
first case (one prime, $p=2$) is the program's Conjecture 100.A. The
category's contribution: the case "one prime, no global archimedean part" is
ALREADY resolved (Theorem 6.7, purity with $|c_m|=2p^{m/2}$ at the boundary): the
first genuinely new link is **two primes** — the object
$F_{p,\alpha}\star F_{q,\alpha'}$ with incommensurable periods, exactly where
Doc 125 located G-125.B.

---

## 8. The free return: what the category pays independently of RH

Three theorems of this document are new or re-founded mathematics that does not depend on
RH nor imply it, and stand on their own:

1. **[THEOREM 4.6 + COROLLARY 4.5] (classification of signatures).** On the
   Hermitian spectral objects with finite divisor, the signatures of the Weil
   form are exactly $\{(p,q):q\le p\}$: the inequality $q\le p$ ("at most
   half the inertia is negative") is the only universal restriction, and it is
   the fingerprint of the involution $\sigma$, valid for any arithmetic function. I
   am not aware of this statement formulated this way in the literature; its content is that
   the "Weil form" is a classification functor for $\sigma$-symmetric divisors,
   with characterized image.

2. **[THEOREM 6.7] (local purity).** For the one-prime Euler objects, Weil
   positivity **is equivalent to purity of the local weights**
   ($|\alpha|=\sqrt p$; equivalently the Ramanujan bound $|c_m|\le2p^{m/2}$),
   with complete elementary proof (Poisson + two-bump test). It is an
   "absolute toy Hodge–Tate theorem": at local rank, positivity =
   purity, decidable. And its negative corollary — **the Euler product does not imply
   Weil positivity** — prunes a persistent intuition of the field with a
   two-line counterexample.

3. **[THEOREM 1.9] (differential characterization of the Euler product).** "Having an
   Euler product" is a support condition on the logarithmic derivative in
   the differential ring $(\mathcal{D},\star,D)$ — a pure algebraic predicate,
   with no analyticity. (Relatives in Rearick 1968 [DATA]; the closed
   exp/log/support form with the categorical application is from this document.)

Minor but original: Theorem 5.3 (the toy index $(1,2)$ as a theorem of abstract
intersection structures, with the exact degeneration at $g=0$ — which
explains in one line why the genus 0 of CC's $\mathrm{Spec}\,\mathbb{Z}$ cannot
carry a rank-3 Hodge index), and Prop. 6.5 (diagonal mass: Weil positivity
of any object requires polar/archimedean mass — "zero density" as a
necessary structural condition).

---

## 9. Map of the framework and the next theorem

**Proved in this document [THEOREM]:**
- $\mathcal{K}_2$ local commutative ring; associativity of $\star_2$ (1.4);
- differential ring $\mathcal{D}$, $\exp_\star$, Euler $\iff$ PP support (1.9);
- category of correspondences with associative composition and unit, kernel
  faithfulness (2.3, 2.4); $\sigma$ involutive functor, $Q_X$ Hermitian (2.8);
- degree = almost-prime side for every arithmetic function (3.2, 3.3);
- evaluation lemma (4.3); orbit theorem and block signature (4.4);
  universal $q\le p$ (4.5); classification/realization (4.6); tensor index (4.8);
  double explicit formula for EF (4.9);
- toy index: $(1,2)$ $\iff g\ge1$, degeneration at $g=0$ (5.3);
- H from the line, for the whole category (6.2); H-by-blocks $\iff$ divisor on
  the line, unconditional (6.3); failures of H: constant (6.4), completely
  multiplicative/diagonal mass (6.5); Poisson–Euler formula (6.6);
  **local purity** (6.7).

**[BRIDGE] (declared status):** $H(\zeta_{\mathrm{ob}})\iff$RH (half proved here,
half Weil's criterion [DATA]); full negativity of $Q$ for D–H and for general
infinite divisors = Hypothesis-D-type separation (proved only for finite and
lattice divisors); the tropical realization of the intersection structure on
periodic objects imports Doc 125's computation [CONSTRUCTION].

**[WISH]:** Conjecture H⁺ (6.9: $a\ge0$ + Euler + standard polar $\Rightarrow$ H);
Limit-rigidity lemma (7.2); extension of the intersection structure to two
incommensurable primes (G-125.B in categorical form).

**The next theorem to attack** — chosen because it is finite, new, and discriminates:
**the two-prime object.** Let $X_{p,q;\alpha,\alpha'}$ be the object with datum
$a$ supported on $\{p^m q^n\}$ given by the convolution of two pure Euler
factors ($|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$). Its functional is computable by
the Poisson formula on each factor; its divisor is NOT a union of lattices (the
periods $\log p,\log q$ are incommensurable) and its form $Q$ is the first case
where positivity is decided neither by finite blocks nor by a lattice.
Prove or refute: *$Q_{X_{p,q}}\ge0$, with a gap, uniformly in the second prime.*
This is Conjecture 100.A rewritten as an internal statement of $\mathcal{A}rith$ on
pure objects — if the category delivers what it promises, this is the place where a
two-prime theorem may exist without touching ζ; and if it fails, the counterexample
would refute H⁺ and would teach what positivity is missing. Either way one learns a
theorem.

---

## References

**Internal (backward-only):** Doc 107 (Weil formula 1–2 variables, thickened
kernel, Theorems 2.4/3.4/4.2/4.4/5.5, Prop. 6.1); Doc 125 (tropical intersection,
$G_{\mathrm{toy}}$, $\Delta_\mu$, G-125.A/B); Doc 110 (L1–L6, class $\mathcal{F}$,
Theorem 4.3, Prop. 4.5, table §5.2); Doc 106 (Prop. 3.5 tensor index, Lemmas
5.2/5.3); Doc 96 (Theorem 8.1); Doc 108 (value/inertia); P35 (Weil form,
$\kappa=2m$, Hypothesis D); Doc 119 (R-NC, NC1–NC4, T2/T3); Doc 124 (genus 0 of
$\mathrm{Spec}\,\mathbb{Z}$).

**Literature [DATA]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Comm. Sém. Math. Lund (1952), 252–265.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
  numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233 (Weil's criterion:
  positivity $\Rightarrow$ RH).
- C. N. Cashwell, C. J. Everett, *The ring of number-theoretic functions*, Pacific
  J. Math. 9 (1959), 975–985.
- D. Rearick, *Operators on algebras of arithmetic functions*, Duke Math. J. 35
  (1968), 761–766 (Dirichlet exp/log).
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series I, II*,
  J. London Math. Soc. 11 (1936), 181–185, 307–312. R. Spira, *Some zeros of the
  Titchmarsh counterexample*, Math. Comp. (1968). E. P. Balanzario,
  J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp.
  76 (2007), 2045–2049. E. C. Titchmarsh, *The Theory of the Riemann
  Zeta-Function*, 2nd ed., §10.25.
- L. Allermann, J. Rau, *First Steps in Tropical Intersection Theory*,
  arXiv:0709.3705. F. Babaee, J. Huh, Duke Math. J. 166 (2017), arXiv:1502.00299
  (via Doc 125).
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. 53, 2004, Ch. 5.

*End of Document 131.*
