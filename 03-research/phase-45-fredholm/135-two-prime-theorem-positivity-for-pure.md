# Doc 135 — The two-prime theorem: positivity for pure $F_{p,\alpha}\star F_{q,\alpha'}$

**Program:** Riemann Hypothesis — Phase 45: FREDHOLM / first theorems of the $\mathcal{A}rith$ category.
**Prerequisites:** Doc 131 (the category $\mathcal{A}rith$; Dirichlet ring $(\mathcal D,\star)$ and Lemma 1.7 $L(F\star G)=L(F)+L(G)$; Definition 2.1 of an object $(a,c,\omega)$ and functional $W_X$; Prop. 2.8 ($\sigma$, $Q_X$ Hermitian); Definition 4.1 (spectral object, explicit formula); Theorem 4.4 (orbits); Theorem 4.9 (double explicit formula); Prop. 6.2 (H from the line); Theorem 6.6 (Poisson for Euler factors); Theorem 6.7 (local purity); Wish 6.9 (Conjecture H⁺); Wish 7.2 (rigidity of the limit); §9 (the target: the two-prime object)).
**Creative contract (Phase 44/45):** **[NEW-DEFINITION]** total freedom; **[THEOREM]/[PROPOSITION]/[LEMMA]** with complete proof, maximal standard; **[COMPUTATION]** verified; **[BRIDGE]** with declared status; **[WISH]** what is wanted and not proved; **[GAP]** what is missing, named; **[DATUM]** cited literature. The discipline lives in what gets called a theorem.

**Conventions (those of Doc 131, fixed once).** $G=\mathbb R_+^*$, $d^*x=dx/x$, tests $f\in C_c^\infty(G)$, Mellin $\hat f(s)=\int_0^\infty f(x)x^{s-1}\,dx$, involution $\tilde f(x)=\overline{f(1/x)}\,x^{-1}$, $\widehat{\tilde f}(s)=\overline{\hat f(1-\bar s)}$, $\sigma(s)=1-\bar s$. For a given $f$, we write
$$F(t):=f(e^t)\,e^{t/2}\in C_c^\infty(\mathbb R),\qquad
\hat F(\xi):=\int_{\mathbb R}F(t)\,e^{i\xi t}\,dt,$$
so that $\hat f(\tfrac12+i\xi)=\hat F(\xi)$ and $\;\|f\|_w^2:=\int_G|f(x)|^2\,x\,d^*x=\|F\|_{L^2(\mathbb R)}^2$.
For a prime $r$ we write $L_r:=\log r$. "Window of length $2T$" = support of $f$ contained in an interval $[\lambda e^{-T},\lambda e^{T}]$ (equivalently: $\mathrm{supp}\,F$ in an interval of length $2T$; the position $\lambda$ is free and, as will be seen, irrelevant).

---

## 0. Executive summary

This document proves the theorem announced in Doc 131 §9. Without ornamentation:

1. **(§1)** The product $\star$ of Euler objects in $\mathcal{A}rith$ and its exact
   composition law (Prop. 1.3): under Dirichlet convolution of the coefficient
   series, **Weil data add up**: $W_{X_1\star X_2}=W_{X_1}+W_{X_2}$.
   The mixed support $\{p^aq^b:a,b\ge1\}$ — where the convolution "mixes" — **carries
   exactly zero Weil mass** (Lemma 1.7 of Doc 131). The fear of cross
   terms on the arithmetic side dissolves as a theorem, not as an accident.

2. **(§2)** The two-prime object $X_{p,q}:=F_{p,\alpha}\star F_{q,\alpha'}$ is
   spectral, Hermitian and admissible, with block $(c,\omega)=(0,\,-2\log pq)$ and
   divisor = union of two vertical progressions of periods
   $2\pi/\log p,\ 2\pi/\log q$ — incommensurable (Lemma 1.5): **it is not a
   lattice**.

3. **(§3) [THEOREM A]** If $|\alpha|=\sqrt p$ and $|\alpha'|=\sqrt q$, then
   $X_{p,q}$ satisfies Axiom H and its double version H₂, with exact spectral
   identity $Q_X(f,f)=2\sum_{\Lambda_p}|\hat F|^2+2\sum_{\Lambda_q}|\hat F|^2$.
   **The first Weil positivity theorem with two primes and
   incommensurable periods, without touching ζ.** Cross terms between
   progressions do not cancel on average (Kronecker): **they do not exist** — the functional is linear in the divisor.

4. **(§4) [THEOREM B]** Converse: if $|\alpha|\ne\sqrt p$ or $|\alpha'|\ne\sqrt q$,
   H fails, with an explicit two-bump test. The diagonal tide of the second
   prime raises the Ramanujan barrier from $2p^{M/2}$ to $2p^{M/2}(1+L_q/L_p)$, but
   no finite tide saves impurity. **Corollary: H is decidable in the
   two-prime subcategory and is equivalent to bilateral purity** — the extension
   of Theorem 6.7 of Doc 131.

5. **(§5)** Fine structure, where Kronecker does appear: **exact** gap
   $Q_X=2\log(pq)\,\|f\|_w^2$ in windows $\le\log\min(p,q)$ (Theorem 5.2); uniform
   gap $2\log q$ up to window $\log q$, **uniform (increasing) in the second
   prime** — the statement of Doc 131 §9 proved; the kernel threshold at
   $2T=\log(pq)$ (Theorem 5.4, via Jensen + explicit construction): the form is
   definite in windows $<\log pq$ and semidefinite with infinite-dimensional
   kernel beyond that. The near-collisions of the two progressions (Kronecker/Weyl)
   prevent uniform separation; with trivial phases, Baker repels them polynomially
   (Prop. 5.6). The uniform gap in intermediate windows is left named: GAP-135.A.

6. **(§6) [COMPUTATION]** The toy model $p=2$, $q=3$, $\alpha=\sqrt2$, $\alpha'=\sqrt3$:
   Mertens test against prime 2: minimum $=\log6-(\log2)^2/\log6\approx1.5236>0$;
   the critical direction of prime 2 (where its perfect square vanishes) is
   rescued by the diagonal of 3 with margin $4\log3$; the doubly
   adversarial test gives minimum $=4\log2\log3/\log6\approx1.7000>0$ — **the margin is twice
   the harmonic mean of $\log2$ and $\log3$, uniform in the heights $M,N$**;
   the adversary at the mixed point $8/9$ (Kronecker near-collision) decouples:
   there is no coefficient to strike.

7. **(§7) [THEOREM A′ + BRIDGE]** The argument is **additive, hence trivially
   inductive**: it holds verbatim for $n$ primes (Theorem 7.1, margin
   $4\sum_{i<j}L_iL_j/\log P$). The induction toward ζ breaks at four localized
   points (B1–B4): divergence of the diagonal mass $\omega_y=-2\theta(y)$;
   **divisor of the limit ≠ limit of divisors** (positivity passes to the limit,
   spectrality does not); the weight mismatch (the local factors of ζ are
   $\sigma$-impure: $c_m=1+p^m$, maximal violation of Ramanujan — the symmetry of ζ
   is global, not factor by factor); and the order of the window/prime limits. The
   transmutation lives in B2+B3, not in the positivity step.

---

## 1. The product $\star$ and the two-prime object

### 1.1. The composition law of $W$ under $\star$

Recall the dictionary of Doc 131 (§1.2, §6.4–6.5). To a Dirichlet series
$E(s)=\sum_n b(n)n^{-s}$ with $b(1)=1$ corresponds the discrete datum
$a:=L(b)=b^{-1}\star Db\in\mathcal D$ (the Dirichlet logarithmic derivative,
$a\leftrightarrow -\,d/ds\log E$). The Euler object of a prime $F_{p,\alpha}$
(Doc 131, Prop. 6.6′) corresponds to the **self-dual local
polynomial**
$$D_{p,\alpha}(s)\;:=\;(1-\alpha p^{-s})\bigl(1-(p/\bar\alpha)\,p^{-s}\bigr),$$
whose Dirichlet coefficients are supported on $\{1,p,p^2\}$, with datum
$a(p^m)=L(b)(p^m)=-L_p\,c_m$, $c_m:=\alpha^m+(p/\bar\alpha)^m$, divisor = zeros of
$D_{p,\alpha}$, and functional
$$W_{F_{p,\alpha}}(f)\;=\;L_p\sum_{m\in\mathbb Z}c_m\,f(p^m),\qquad
c_{-m}=\bar c_m\,p^{-m},\quad c_0=2.$$
*(The factor $(1-\alpha'q^{-s})$ of the target is "half" of the object: the
$\sigma$-stability forces the mirror factor $1-(q/\bar\alpha')q^{-s}$; under purity
both coincide and multiplicity 2 appears. We always work with the complete
self-dual object.)*

**[NEW-DEFINITION 1.1] (product $\star$ of objects).** For objects
$X_1=(a_1,c^{(1)},\omega_1)$, $X_2=(a_2,c^{(2)},\omega_2)$ of $\mathcal{A}rith$:
$$X_1\star X_2\;:=\;\bigl(a_1+a_2,\;c^{(1)}+c^{(2)},\;\omega_1+\omega_2\bigr).$$
The name $\star$ is justified in Prop. 1.3: on objects coming from Dirichlet
series, this operation IS Dirichlet convolution of the coefficient series,
read on the Weil data.

**[PROPOSITION 1.2] (additivity of $W$; trivial but structural).** For every
test $f$: $W_{X_1\star X_2}(f)=W_{X_1}(f)+W_{X_2}(f)$, and
$Q_{X_1\star X_2}(f,f)=Q_{X_1}(f,f)+Q_{X_2}(f,f)$.

*Proof.* The three blocks of Definition 2.1 of Doc 131 ($D_c$, $P_a$,
$A_\omega$) are linear in the data $(a,c,\omega)$. The second identity is the
first applied to $f\star\tilde f$. $\square$

**[PROPOSITION 1.3] (the exact composition law: Dirichlet convolution does not
mix Weil data).** Let $b_1,b_2\in\mathcal D$ be normalized units with
data $a_i=L(b_i)$, and let $b:=b_1\star b_2$ (Dirichlet convolution — for
Euler factors of distinct primes, $b$ is supported on $\{p^aq^b\}$ and genuinely
mixes the two primes). Then the Weil datum of $b$ is
$$L(b_1\star b_2)\;=\;L(b_1)+L(b_2)\;=\;a_1+a_2,$$
that is: the object associated with $b$ is exactly $X_1\star X_2$ in the sense
of Definition 1.1. In particular, if $a_1$ is supported on $p^{\mathbb N}$ and
$a_2$ on $q^{\mathbb N}$ with $p\ne q$, the datum of the product is supported on
$p^{\mathbb N}\sqcup q^{\mathbb N}$: **the mixed support $\{p^aq^b:a,b\ge1\}$ of the
coefficients carries zero Weil mass.**

*Proof.* This is Lemma 1.7 of Doc 131 ($D$ is a derivation of
$(\mathcal D,\star)$, so $L$ is additive on normalized units), plus the
support observation: $a_1+a_2$ lives in the union of the supports, which is
disjoint by unique factorization. $\square$

**Remark 1.4 (the fear of cross terms, dissolved in the right place).** The
target anticipated: *"the Weil functional of the product object is not the sum of the
functionals — Dirichlet convolution mixes"*. Prop. 1.3 shows that the
mixing occurs in the **coefficients** $b(p^aq^b)\ne0$ and disappears **exactly**
(not on average, not asymptotically) in the datum $a=L(b)$, which is what $W$ sees. The
identity responsible is algebraic ($L$ additive = logarithmic derivation), not
Diophantine: Kronecker is not needed for the sign. The cross terms between the
two zero progressions will reappear — but in the **fine geometry of the gap**
(§5), not in positivity. This relocation is one of the findings of the
document. A design point, declared: if one were to define the product object by putting
the raw convolution $b_1\star b_2$ as the discrete datum (in the $a$ slot), the
resulting object would not be of Euler type in the sense of Theorem 1.9 of Doc 131 and
none of what follows would apply; Definition 1.1 is the only one compatible with the
object ↔ series dictionary.

### 1.2. The two-prime object

**[NEW-DEFINITION 1.5] (the two-prime object).** Let $p\ne q$ be primes,
$1<|\alpha|<p$, $1<|\alpha'|<q$. The **two-prime object** is
$$X_{p,q}\;=\;X_{p,q;\alpha,\alpha'}\;:=\;F_{p,\alpha}\star F_{q,\alpha'}
\;=\;\bigl(a,\;0,\;\omega\bigr),$$
with explicit data:
- $a(p^m)=-L_p\,c_m$ ($m\ge1$), $a(q^n)=-L_q\,c'_n$ ($n\ge1$), $a=0$ elsewhere
  (in particular on every $p^aq^b$ with $a,b\ge1$, by Prop. 1.3); here
  $c_m=\alpha^m+(p/\bar\alpha)^m$, $c'_n=\alpha'^n+(q/\bar\alpha')^n$;
- $c=0$ (no polar block);
- $\omega\equiv-2\log(pq)$ (constant: even, measurable, of polynomial growth —
  admissible), which realizes the diagonal atom $c_0+c'_0=2+2$ via Mellin
  inversion $f(1)=\tfrac1{2\pi}\int\hat f(\tfrac12+it)\,dt$:
  $-A_\omega(f)=2\log(pq)\,f(1)$.

The functional, in closed form (a finite sum for each test):
$$\boxed{\;W_{X}(f)\;=\;L_p\sum_{m\in\mathbb Z}c_m\,f(p^m)
\;+\;L_q\sum_{n\in\mathbb Z}c'_n\,f(q^n)\;}$$
where the term $(m,n)=(0,0)$ is counted once with weight
$c_0L_p+c'_0L_q=2\log(pq)$ (this is the $\omega$ block; the $m\ne0,n\ne0$ terms are
the discrete block $-P_a$ with their mirrors $c_{-m}=\bar c_m p^{-m}$).

**[LEMMA 1.6] ($X_{p,q}$ is Hermitian).** $W_{\sigma X}(f)=W_X(f)$ for every $f$,
i.e. $\overline{W_X(\tilde f)}=W_X(f)$; consequently (Doc 131, Prop. 2.8(c) with
the functional identity in place of equality of data) $Q_X(f_1,f_2):=
W_X(f_1\star\tilde f_2)$ is a Hermitian form.

*Proof.* By Prop. 1.2 it suffices to check it factor by factor. For $F_{p,\alpha}$:
$\tilde f(p^m)=\overline{f(p^{-m})}\,p^{-m}$, hence
$$\overline{W_F(\tilde f)}=L_p\sum_m\bar c_m\,f(p^{-m})\,p^{-m}
\;\overset{m\mapsto-m}{=}\;L_p\sum_m\bar c_{-m}\,p^{m}\,f(p^{m}),$$
and $\bar c_{-m}\,p^{m}=\overline{\bar c_m p^{-m}}\,p^{m}\cdot 1=c_m$ using
$c_{-m}=\bar c_m p^{-m}$. The same for the $q$ factor. $\square$

**[LEMMA 1.7] (incommensurability).** $\log p/\log q\notin\mathbb Q$. Moreover, the
frequency progressions
$$\Lambda_p:=\Bigl\{\tfrac{\phi+2\pi k}{L_p}:k\in\mathbb Z\Bigr\},\qquad
\Lambda_q:=\Bigl\{\tfrac{\phi'+2\pi l}{L_q}:l\in\mathbb Z\Bigr\}$$
(with $\phi:=\arg\alpha$, $\phi':=\arg\alpha'$ fixed) share at most **one**
point.

*Proof.* If $\log p/\log q=a/b$ with $a,b\in\mathbb Z_{\ge1}$, then
$p^b=q^a$, impossible by unique factorization. If $\Lambda_p\cap\Lambda_q$ had
two points, the difference would give $2\pi k/L_p=2\pi l/L_q$ with $(k,l)\ne(0,0)$, i.e.
$kL_q=lL_p$, i.e. $\log p/\log q=k/l\in\mathbb Q$, a contradiction. $\square$

---

## 2. [COMPUTATION] The spectral pair: the two sides of $W_X$

**[PROPOSITION 2.1] (zero side).** Let $Z_{p,\alpha}:=\{s:p^s=\alpha\}
=\{\log_p\alpha+2\pi ik/L_p\}$ and similarly $Z_{q,\alpha'}$. The pair
$(X_{p,q},\,Z_X)$ with the multiset
$$Z_X\;:=\;\underbrace{Z_{p,\alpha}\sqcup Z_{p,\,p/\bar\alpha}}_{\text{zeros of }D_{p,\alpha}}
\;\sqcup\;\underbrace{Z_{q,\alpha'}\sqcup Z_{q,\,q/\bar\alpha'}}_{\text{zeros of }D_{q,\alpha'}}$$
is a spectral object of $\mathcal{A}rith^{EF}$ (Doc 131, Def. 4.1):
$$\sum_{\rho\in Z_X}\hat f(\rho)\;=\;W_X(f)\qquad\forall f\in C_c^\infty(G),$$
with absolute convergence, $N_{Z_X}(T)=\tfrac{2}{\pi}\bigl(L_p+L_q\bigr)T+O(1)\ll T$,
and $Z_X$ $\sigma$-stable ($\sigma Z_{p,\alpha}=Z_{p,\,p/\bar\alpha}$).

*Proof.* The Poisson formula for Euler factors (Doc 131, Theorem 6.6)
applied to each of the four progressions:
$\sum_{Z_{p,\alpha}}\hat f(\rho)=L_p\sum_m\alpha^m f(p^m)$ and
$\sum_{Z_{p,p/\bar\alpha}}\hat f(\rho)=L_p\sum_m(p/\bar\alpha)^m f(p^m)$; the sum
of both is $L_p\sum_m c_m f(p^m)$. Likewise for $q$. Summing: the right-hand side is
exactly the closed form of Definition 1.5. The density: each progression
has $\#\{|\mathrm{Im}\,\rho|\le T\}=L_rT/\pi+O(1)$. The $\sigma$-stability:
$p^{1-\bar\rho}=p/\overline{p^{\rho}}=p/\bar\alpha$. $\square$

**Divisor geometry, explicitly.**
- In general (impure $\alpha$): four vertical progressions, at
  $\mathrm{Re}=\log_p|\alpha|$ and $1-\log_p|\alpha|$ (period $2\pi/L_p$) and at
  $\mathrm{Re}=\log_q|\alpha'|$ and $1-\log_q|\alpha'|$ (period $2\pi/L_q$).
- Under **purity** $|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$: $\alpha=p/\bar\alpha$, the
  two progressions of prime $p$ coincide; the divisor is
  $$Z_X\;=\;2\cdot\Bigl\{\tfrac12+i\tfrac{\phi+2\pi k}{L_p}\Bigr\}
  \;\sqcup\;2\cdot\Bigl\{\tfrac12+i\tfrac{\phi'+2\pi l}{L_q}\Bigr\}
  \;=\;2\cdot\bigl(\tfrac12+i\Lambda_p\bigr)\sqcup 2\cdot\bigl(\tfrac12+i\Lambda_q\bigr),$$
  two progressions on the critical line with multiplicity 2 and incommensurable
  periods (Lemma 1.7), and the coefficients equal $c_m=2\alpha^m$,
  $|c_m|=2p^{m/2}$ (Ramanujan's equality, the exact edge of the barrier of
  Doc 131 §6.5).

**Remark 2.2 (this is not a lattice).** For a single prime, the divisor is
a vertical lattice and the object is *periodic* (Doc 131, Def. 5.4): the whole
theory reduces to the circle $G/p^{\mathbb Z}$. For two primes, $\log p$ and
$\log q$ are $\mathbb Q$-linearly independent: the group generated by
$p^{\mathbb Z}q^{\mathbb Z}$ is dense in $G$ (Kronecker) and there is no compact quotient
carrying the object. This is exactly the territory where Doc 125 located
G-125.B and where neither Theorem 4.4(c) of Doc 131 (finite divisors) nor
Theorem 6.7 (a lattice) decide H. That is why this theorem is new.

---

## 3. [THEOREM A] Positivity

**[THEOREM 3.1] (the two-prime theorem).** Let $p\ne q$ be primes and
$|\alpha|=\sqrt p$, $|\alpha'|=\sqrt q$ (bilateral purity, phases
$\phi,\phi'$ arbitrary). Then $X=X_{p,q;\alpha,\alpha'}$ satisfies
Axiom H, with exact spectral identity: for every $f\in C_c^\infty(G)$,
$$Q_X(f,f)\;=\;2\sum_{\xi\in\Lambda_p}\bigl|\hat F(\xi)\bigr|^2
\;+\;2\sum_{\xi\in\Lambda_q}\bigl|\hat F(\xi)\bigr|^2\;\ge\;0,$$
with both sums absolutely convergent. It also satisfies H₂:
$\deg_X(h\star_{G^2}\tilde h)\ge0$ for every $h\in C_c^\infty(G^2)$.

*Proof.* Let $g:=f\star\tilde f$. By Prop. 2.1, $(X,Z_X)$ is spectral,
Hermitian (Lemma 1.6) and $\sigma$-stable, so Theorem 4.4(a) of
Doc 131 applies:
$$Q_X(f,f)=W_X(g)=\sum_{\rho\in Z_X}m_\rho\,\hat f(\rho)\,\overline{\hat f(\sigma\rho)}.$$
Under purity every $\rho\in Z_X$ has $\mathrm{Re}\,\rho=\tfrac12$, so
$\sigma\rho=\rho$ and each term is $m_\rho|\hat f(\rho)|^2\ge0$. With
$\rho=\tfrac12+i\xi$, $\hat f(\rho)=\hat F(\xi)$ and multiplicities $m_\rho=2$ one
obtains the identity in the statement. (Absolute convergence: Paley–Wiener
$|\hat F(\xi)|\ll_N(1+|\xi|)^{-N}$ against linear density.) For H₂: the
Theorem 4.9 of Doc 131 gives
$\deg_X(h\star\tilde h)=\sum_{\rho_1,\rho_2\in Z_X}\hat h(\rho_1,\rho_2)
\overline{\hat h(\sigma\rho_1,\sigma\rho_2)}=\sum_{\rho_1,\rho_2}
|\hat h(\rho_1,\rho_2)|^2\ge0$ (Prop. 6.2 of Doc 131, which covers H and H₂ for
divisors on the line — the polynomial-density hypothesis was verified in 2.1).
$\square$

Equivalently, in purely arithmetic form (without mentioning the divisor):
$$L_p\sum_{m\in\mathbb Z}c_m\,g(p^m)\;+\;L_q\sum_{n\in\mathbb Z}c'_n\,g(q^n)\;\ge\;0
\qquad\text{for every }g=f\star\tilde f,$$
with $c_m=2\alpha^m$, $|c_m|=2p^{m/2}$. This is the statement that was NOT accessible
either by finite blocks or by periodicity, and is now a theorem.

**Remark 3.2 (where the cross terms would have been, and why they are not there).** There
are two places where a "cross term $p$–$q$" could have appeared, and in both
the cancellation is **exact**, not statistical:

1. *Arithmetic side:* the Dirichlet convolution of the coefficients loads the
   mixed support $p^aq^b$; the Weil mass there is zero by Prop. 1.3 (a
   derivation identity, pure algebra).
2. *Spectral side:* $W_X$ is **linear** in the divisor — a single sum over
   $Z_p\sqcup Z_q$, never a double sum. The products
   $\hat f(\rho_1)\overline{\hat f(\rho_2)}$ with $\rho_1\in Z_p$, $\rho_2\in Z_q$
   only appear in the two-variable functional $\deg_X$, where the product
   structure factors them into $|\hat h(\rho_1,\rho_2)|^2$ — positive again.

The incommensurability of $\log p$ and $\log q$ **is not used** in Theorem 3.1
(it holds just the same for $q=p$, which is the lattice case of Doc 131!). Where it IS
used, and essentially, is in: (i) the converse (Theorem 4.1: separating the
supports of adversarial tests — only unique factorization), and (ii) the fine
structure of the gap (§5: Kronecker/Weyl/Baker). The lesson, worth highlighting because it
corrects the target's intuition: **in the Weil formula, interference between primes is a
phenomenon of the gap, not of the sign.**

---

## 4. [THEOREM B] The converse: bilateral purity necessary

**[THEOREM 4.1].** Let $1<|\alpha|<p$, $1<|\alpha'|<q$. If $|\alpha|\ne\sqrt p$ or
$|\alpha'|\ne\sqrt q$, then $X_{p,q;\alpha,\alpha'}$ does **not** satisfy H: there exists
an explicit test $f$ with $Q_X(f,f)<0$.

*Proof.* Without loss of generality the impure factor is that of $p$, with
$|\alpha|=p^{1/2+\delta'}$, $\delta'>0$ (if $\delta'<0$, swap
$\alpha\leftrightarrow p/\bar\alpha$, same object; if the impure one is $q$,
swap the roles of $p$ and $q$; purity or impurity of the other factor is
irrelevant in what follows). We use the two-bump Mertens test of
Doc 131 §6.5, now in the presence of the second prime.

Let $M\ge1$ to be fixed. Take $u\ge0$ real, $u(e^t)=\epsilon^{-1/2}\chi(t/\epsilon)$
with $\chi$ even, $\mathrm{supp}\,\chi\subset[-1,1]$, $\int\chi^2=1$, and the test
$$f\;:=\;u+\theta\,u(\cdot/p^{M}),\qquad\theta\in\mathbb C.$$
Let $g=f\star\tilde f$; $\log\mathrm{supp}\,g\subset\{0,\pm ML_p\}+[-2\epsilon,2\epsilon]$.

*Choice of $\epsilon$ (separation by unique factorization).* The points
sampled by $W_X$ are $p^m$ and $q^n$. For $g(p^m)\ne0$ we need
$|mL_p-\kappa|<2\epsilon$ with $\kappa\in\{0,\pm ML_p\}$; with $\epsilon<L_p/4$ this
forces $m\in\{0,\pm M\}$. For $g(q^n)\ne0$ we need
$|nL_q-\kappa|<2\epsilon$; the candidate $n$'s are finitely many
($|n|\le(ML_p+1)/L_q$) and for each one with $n\ne0$ the quantity
$\min(|nL_q|,\,|nL_q\mp ML_p|)$ is **strictly positive** — $q^n\ne1$ and
$q^n\ne p^{\pm M}$ by unique factorization (Lemma 1.7). We take
$$\epsilon\;<\;\tfrac14\min\Bigl(L_p,\ \min_{0<|n|\le(ML_p+1)/L_q}
\bigl|\,|n|L_q-ML_p\bigr|,\ L_q\Bigr).$$
Then the $q$ factor contributes **only its diagonal term** $n=0$, with
coefficient $c'_0=2$ whatever $\alpha'$ is.

*The values of $g$* (computation from Doc 131 §6.5, unchanged):
$$g(1)=\bigl(1+|\theta|^2p^{M}\bigr)(1+O(\epsilon)),\qquad
g(p^{M})=\theta\,(1+O(\epsilon)),\qquad
g(p^{-M})=\bar\theta\,p^{M}(1+O(\epsilon)).$$
Using $c_{-M}p^{M}=\bar c_M$:
$$Q_X(f,f)=\Bigl[\,2(L_p+L_q)\bigl(1+|\theta|^2p^{M}\bigr)
+2L_p\,\mathrm{Re}\!\bigl(c_M\theta\bigr)\Bigr](1+O(\epsilon)).$$
We choose the adversarial phase $\theta=-(\overline{c_M}/|c_M|)\,t$, $t>0$:
$$\frac{Q_X(f,f)}{2(1+O(\epsilon))}
=(L_p+L_q)\bigl(1+p^{M}t^2\bigr)-L_p\,|c_M|\,t,$$
with minimum at $t^*=L_p|c_M|/\bigl(2(L_p+L_q)p^{M}\bigr)$ of value
$$(L_p+L_q)\;-\;\frac{L_p^2\,|c_M|^2}{4\,(L_p+L_q)\,p^{M}}\;<\;0
\quad\Longleftrightarrow\quad
|c_M|\;>\;2\,p^{M/2}\Bigl(1+\tfrac{L_q}{L_p}\Bigr).$$
Since $|c_M|\ge p^{M(1/2+\delta')}-p^{M(1/2-\delta')}
=p^{M/2}\bigl(p^{M\delta'}-p^{-M\delta'}\bigr)$ and $\delta'>0$, the ratio
$|c_M|p^{-M/2}\to\infty$: there exists $M$ exceeding the barrier. Fix such $M$, then
$\epsilon$ (which depends on $M$) to absorb the $O(\epsilon)$ terms:
$Q_X(f,f)<0$. $\square$

**[COROLLARY 4.2] (bilateral purity: H decidable in the two-prime
subcategory).** For $p\ne q$, $1<|\alpha|<p$, $1<|\alpha'|<q$:
$$X_{p,q;\alpha,\alpha'}\ \text{satisfies H}
\quad\Longleftrightarrow\quad
|\alpha|=\sqrt p\ \text{and}\ |\alpha'|=\sqrt q
\quad\Longleftrightarrow\quad
|c_m|\le2p^{m/2}\ \text{and}\ |c'_n|\le2q^{n/2}\ \ \forall m,n\ge1.$$
*(Theorems 3.1 + 4.1; the second equivalence is that of Doc 131, Theorem 6.7,
factor by factor.)* The local purity theorem extends thus, exactly, from a
lattice to two incommensurable progressions. $\square$

**Quantitative comment.** The diagonal tide of the second prime raises the barrier
of the test from $2p^{M/2}$ to $2p^{M/2}(1+L_q/L_p)$: an unrelated prime **protects**
additively (its diagonal mass adds up) but cannot buy the impurity of another, because
the Ramanujan violation grows geometrically ($p^{M\delta'}$) while the
protection is constant in $M$. In the limit toward ζ this is the account that returns:
the total protection of all primes is $2\theta(y)$, divergent — see §7.

---

## 5. Fine structure: exact gap, kernel, and where Kronecker lives

In this section bilateral purity is always in force. By Theorem 3.1 everything
reduces to the analysis of
$$Q_X(f,f)=2\sum_{\Lambda_p}|\hat F|^2+2\sum_{\Lambda_q}|\hat F|^2 .$$

**[LEMMA 5.1] (Parseval of the periodization).** If $\mathrm{supp}\,F$ is in an
interval of length $\le L_r$, then
$\sum_{\xi\in\Lambda_r}|\hat F(\xi)|^2=L_r\,\|F\|_{L^2}^2$.

*Proof.* Let $F_r(t):=F(t)e^{i\phi_r t/L_r}$ (with $\phi_p=\phi$,
$\phi_q=\phi'$), so that $\hat F(\tfrac{\phi_r+2\pi k}{L_r})=\hat F_r(2\pi k/L_r)$.
The periodization $P(t)=\sum_m F_r(t+mL_r)$ has Fourier coefficients
$\tfrac1{L_r}\hat F_r(2\pi k/L_r)$; Parseval on $[0,L_r]$:
$\sum_k|\hat F_r(2\pi k/L_r)|^2=L_r\int_0^{L_r}|P|^2$. If the support fits in an
interval of length $\le L_r$, the translates do not overlap and
$\int_0^{L_r}|P|^2=\|F_r\|_2^2=\|F\|_2^2$. $\square$

**[THEOREM 5.2] (exact gap in short window; uniform in the second prime).**
Suppose $p<q$.
(a) If $f$ has support in a window of length $2T\le\log p$, then
$$Q_X(f,f)\;=\;2\,\log(pq)\,\|f\|_w^2$$
— an exact identity: in short windows the form is a multiple of the identity
(there are no cross terms of any kind).
(b) If $2T\le\log q$, then $Q_X(f,f)\ge2\,\log q\,\|f\|_w^2$.
In particular the gap is **uniform and increasing in the second prime**: for a fixed
window $2T$, every prime $q\ge e^{2T}$ contributes gap $\ge2\log q$. The statement of
Doc 131 §9 ("with gap, uniformly in the second prime") is thereby proved in this
range of windows.

*Proof.* (a) Via the spectral side: Lemma 5.1 on both lattices
($2T\le L_p<L_q$): $Q_X=2L_p\|F\|^2+2L_q\|F\|^2=2\log(pq)\,\|f\|_w^2$.
Via the arithmetic side (double check, culture of the program): $g=f\star\tilde f$ has
logarithmic support in $(-2T,2T)\subset(-L_p,L_p)$ — it only touches $m=n=0$:
$W_X(g)=2(L_p+L_q)\,g(1)$ and $g(1)=\int|f|^2x\,d^*x=\|f\|_w^2$. They coincide.
(b) Lemma 5.1 only on $\Lambda_q$ and positivity of the $p$ block. $\square$

**[LEMMA 5.3] (characterization of the kernel).** $Q_X(f,f)=0\iff\hat F$ vanishes
on $\Lambda_p\cup\Lambda_q\iff$ the two twisted periodizations
$\sum_mF(t+mL_p)e^{i\phi(t+mL_p)/L_p}$ and its analogue at $q$ are identically
zero — i.e. $f$ is **invisible to both Euler factors**. *(Immediate from the
spectral identity and from Lemma 5.1/Fourier.)* $\square$

**[THEOREM 5.4] (the kernel threshold is $\log pq$).**
(a) If $f\ne0$ has support in a window of length $2T<\log(pq)$, then
$Q_X(f,f)>0$: the form is **definite** in every window shorter than $\log pq$.
(b) For every $2T>\log(pq)$ there exists an infinite-dimensional subspace of tests
supported in a window of length $2T$ with $Q_X(f,f)=0$. In particular $Q_X$
is semidefinite and **there is no global uniform gap** on $C_c^\infty(G)$.

*Proof.* **(a)** Suppose $Q_X(f,f)=0$ with $f\ne0$. If
$\mathrm{supp}\,F\subset[c-T,c+T]$, let $G:=F(\cdot+c)$; then
$\hat F(\xi)=e^{ic\xi}\hat G(\xi)$ with $e^{ic\xi}$ entire and zero-free: $\hat F$ and
$\hat G$ have the same zeros, and $\hat G$ is entire of exponential type $\le T$
($|\hat G(\xi+i\eta)|\le\|G\|_1e^{T|\eta|}$) and bounded on $\mathbb R$ by
$\|G\|_1$. By Lemma 5.3, $\hat G$ vanishes on $\Lambda_p\cup\Lambda_q$. If
$\hat G\not\equiv0$, its real zeros are isolated; choose $\xi_0\in\mathbb R$
with $\hat G(\xi_0)\ne0$. Jensen on the disk $|\xi-\xi_0|\le R$ (for almost every
$R$):
$$\int_0^R\frac{n(r)}{r}\,dr
=\frac1{2\pi}\int_0^{2\pi}\log\bigl|\hat G(\xi_0+Re^{i\vartheta})\bigr|\,d\vartheta
-\log|\hat G(\xi_0)|
\;\le\;\log\|G\|_1+\frac{2TR}{\pi}+C_1,$$
using $|\hat G(\xi_0+Re^{i\vartheta})|\le\|G\|_1e^{TR|\sin\vartheta|}$ and
$\tfrac1{2\pi}\int_0^{2\pi}|\sin\vartheta|\,d\vartheta=\tfrac2\pi$. On the other hand
$n(r)$ counts at least the points of $\Lambda_p\cup\Lambda_q$ in
$[\xi_0-r,\xi_0+r]$: each progression of step $2\pi/L_r$ contributes $\ge rL_r/\pi-2$, and
the overlap is at most one point (Lemma 1.7):
$n(r)\ge\frac{(L_p+L_q)}{\pi}\,r-C_0$. Integrating from a fixed $R_0$:
$$\frac{L_p+L_q}{\pi}\,(R-R_0)-C_0\log\frac{R}{R_0}
\;\le\;\frac{2TR}{\pi}+O(1)\qquad\forall R,$$
whence $L_p+L_q\le2T$, contradicting $2T<\log pq=L_p+L_q$. Hence
$\hat G\equiv0$ and $f=0$. **(b)** Difference operators: for
$g\in C_c^\infty(\mathbb R)$ let
$$(D_r\,g)(t):=g(t)-e^{-i\phi_r}\,g(t-L_r),\qquad
\widehat{D_rg}(\xi)=\bigl(1-e^{i(L_r\xi-\phi_r)}\bigr)\hat g(\xi),$$
which vanishes exactly on $\xi\in\Lambda_r$. Take $g$ a bump of width
$0<\,2T-\log pq\,<\min(2T-\log pq,\,L_p)$ and $F:=D_pD_qg$: then
$\hat F$ vanishes on $\Lambda_p\cup\Lambda_q$, $\mathrm{supp}\,F$ fits in
length $|{\mathrm{supp}\,g}|+L_p+L_q\le2T$, and $F\ne0$ because the extreme
translate $g(\cdot-L_p-L_q)$ has support disjoint from the other three (it is distant
$L_p$ and $L_q$ from the neighbors, more than the width of $g$). The test
$f(e^t):=F(t)e^{-t/2}$ satisfies $Q_X(f,f)=0$, $f\ne0$ (Lemma 5.3). The
infinite dimension: $g\mapsto D_pD_qg$ is injective (nonzero analytic multiplier in
Fourier) on an infinite-dimensional space of bumps. $\square$

**Remark 5.5 (reading).** The kernel is not pathology: these are the tests that no
Euler factor sees, and semidefinite positivity is exactly what H requires. What is
notable is the **arithmetic** threshold $\log(pq)$ = logarithm of the "naive"
conductor of the object: the two-prime form is definite exactly in windows
shorter than $\log$(product of the primes). For $n$ primes the threshold will be
$\log(p_1\cdots p_n)$ (§7) — the window of definiteness grows with the
arithmetic support of the object. This is the quantitative version, in this category, of
the slogan "more primes = more spectrum."

**[PROPOSITION 5.6] (near-collisions and their Diophantine repulsion; trivial
phases).** Let $\alpha=\sqrt p$, $\alpha'=\sqrt q$ ($\phi=\phi'=0$), so that
$\Lambda_p=(2\pi/L_p)\mathbb Z$, $\Lambda_q=(2\pi/L_q)\mathbb Z$.
(a) [Kronecker/Weyl] $\inf\{|\xi-\eta|:\xi\in\Lambda_p\setminus0,\ \eta\in
\Lambda_q\setminus0\}=0$: the two progressions have near-collisions at every
scale — the union is **not uniformly separated**.
(b) [Baker, effective] There exist effective $C,\kappa>0$ (depending on $p,q$) such
that for $\xi=2\pi k/L_p\ne\eta=2\pi l/L_q$ in $[-R,R]$:
$$|\xi-\eta|\;=\;\frac{2\pi}{L_pL_q}\,\bigl|\,k\log q-l\log p\,\bigr|
\;\ge\;C\,R^{-\kappa}.$$

*Proof.* (a) $|2\pi k/L_p-2\pi l/L_q|=\tfrac{2\pi}{L_pL_q}|kL_q-lL_p|$ and
$\{kL_q/L_p \bmod 1\}$ is dense (Lemma 1.7 + Kronecker). (b) This is Baker's theorem on
linear forms in two logarithms [DATUM: Baker 1966; explicit form in
Laurent–Mignotte–Nesterenko 1995]: $|k\log q-l\log p|\ge C'\max(|k|,|l|)^{-\kappa}$
with effective constants; on $[-R,R]$, $|k|\le RL_p/2\pi$, $|l|\le RL_q/2\pi$.
$\square$

**Remark 5.7 (the intermediate region, candid) + [GAP-135.A].** Between the
window $\log q$ (uniform gap proved, Theorem 5.2(b)) and the window $\log pq$
(definiteness without declared gap, Theorem 5.4(a)) the question remains:
$$\mu(T):=\inf\bigl\{Q_X(f,f):\ \|f\|_w=1,\ \text{window }2T\bigr\}\;>\;0
\quad\text{for }\log q<2T<\log pq\ ?$$
This is exactly the question of the **lower frame bound** for the system of
exponentials $\{e^{i\xi t}\}_{\xi\in\Lambda_p\cup\Lambda_q}$ in $L^2$ of an
interval of length $2T$. The necessary Beurling–Landau density
condition holds ($\tfrac{L_p+L_q}{2\pi}>\tfrac{2T}{2\pi}$), but the
standard sufficiency theorems require uniform separation — destroyed by the
near-collisions of 5.6(a). Baker's repulsion 5.6(b) bounds the
collision speed (polynomial) and it is plausible that it suffices for $\mu(T)>0$ with
polynomial loss in the scale, via divided-difference frames [DATUM: Seip,
*Interpolation and sampling*, AMS Univ. Lecture Ser. 33, ch. 2–3]; with generic
phases $\phi,\phi'$ no effective repulsion is known. **GAP-135.A:** decide
$\mu(T)>0$ in the intermediate region, with an explicit constant depending on the
irrationality measure of $\log p/\log q$. Underlined: this gap affects the
**modulus of positivity**, not the sign — Theorem 3.1 does not depend on it. Here, and
only here, does Kronecker live in this problem.

---

## 6. [COMPUTATION] The full toy model: $p=2$, $q=3$, $\alpha=\sqrt2$, $\alpha'=\sqrt3$

Data: $c_m=2\cdot2^{m/2}$, $c'_n=2\cdot3^{n/2}$ (trivial phases),
$L_2=\log2\approx0.6931$, $L_3=\log3\approx1.0986$, $\log6\approx1.7918$.
$$W_X(f)=\log2\sum_m2\cdot2^{m/2}f(2^m)\;+\;\log3\sum_n2\cdot3^{n/2}f(3^n).$$
All tests use the bump $u$ of §4 ($\chi$ even, $\int\chi^2=1$) and the values
of $g=f\star\tilde f$ computed there; the $O(\epsilon)$ terms are omitted (they are
absorbed by choosing $\epsilon$ small at the end, as in §4).

**6.1. Two bumps against prime 2.** $f=u-t\,u(\cdot/2^M)$, $t>0$:
$$\tfrac12\,Q_X=\log6\,(1+2^Mt^2)-\log2\cdot2\cdot2^{M/2}\,t
\;\ge\;\log6-\frac{(\log2)^2}{\log6}\;=\;1.5236\ldots\;>\;0,$$
with minimum at $t^*=\tfrac{\log2}{\log6}\,2^{-M/2}$, **independent of $M$**. The
same test against the one-prime object $F_{2,\sqrt2}$ gives only
$\tfrac12Q=\log2\,(1-2^{M/2}t)^2\cdot\tfrac{2}{2}$ — more precisely
$Q_{F_2}=2\log2\,\bigl(1-2^{M/2}t\bigr)^2$: a **perfect square that vanishes**
at $t=2^{-M/2}$ (the positivity of a pure prime is as tight as it can be:
exact Cauchy–Schwarz, Doc 131 §6.5).

**6.2. The critical direction of 2, rescued by 3.** At the critical test
$t=2^{-M/2}$ of the previous point:
$$Q_X=\underbrace{Q_{F_2}}_{=0}+\;Q_{F_3}=2\log3\,\bigl(1+2^M t^2\bigr)
=2\log3\cdot2=4\log3\approx4.394>0.$$
The diagonal of prime 3 (its $c'_0=2$) fills exactly the zero of prime 2:
**constructive** interference of diagonal masses. (Consistency with §5: this test
lives in window $\approx M\log2>\log2$, outside the identity zone 5.2(a), and its
$Q$ is strictly positive but not proportional to $\|f\|_w^2$ — the square of the
factor-2 term vanished.)

**6.3. The doubly adversarial test (three bumps).**
$f=u-t_1\,u(\cdot/2^M)-t_2\,u(\cdot/3^N)$, $t_1,t_2>0$, $M,N\ge1$. The support
ratios generate points in $\{1,2^{\pm M},3^{\pm N},2^M3^{-N},2^{-M}3^N\}$; by
unique factorization and small $\epsilon$, $W_X$ samples only $1$, $2^{\pm M}$,
$3^{\pm N}$ (the mixed points carry NO coefficient — Prop. 1.3 in action). With
$g(1)=1+t_1^22^M+t_2^23^N$, $g(2^M)=-t_1$, $g(3^N)=-t_2$ (and their mirrors):
$$\tfrac12\,Q_X=\log6\,\bigl(1+2^Mt_1^2+3^Nt_2^2\bigr)
-2\log2\cdot2^{M/2}t_1-2\log3\cdot3^{N/2}t_2.$$
Minimizing separately ($t_1^*=\tfrac{\log2}{\log6}2^{-M/2}$,
$t_2^*=\tfrac{\log3}{\log6}3^{-N/2}$):
$$\min\;\tfrac12\,Q_X=\log6-\frac{(\log2)^2}{\log6}-\frac{(\log3)^2}{\log6}
=\frac{(\log6)^2-(\log2)^2-(\log3)^2}{\log6}
=\frac{2\log2\,\log3}{\log6},$$
that is
$$\boxed{\ \min Q_X\;=\;\frac{4\,\log2\,\log3}{\log2+\log3}\;\approx\;1.7000\;>\;0\ }$$
— **twice the harmonic mean of $\log2$ and $\log3$, uniform in $M,N$**. The
identity behind it: $(\sum_iL_i)^2-\sum_iL_i^2=2\sum_{i<j}L_iL_j$ — the margin of
positivity against the Mertens family is exactly the **cross term of
the diagonal masses**: the cross terms the convolution did not place in the
coefficients reappear, with positive sign, in the square of the
diagonal. Consistency check: with a single prime the margin is $L_p-L_p^2/L_p=0$ —
recovering the perfect square of 6.1. ✓

**6.4. The Kronecker adversary, decoupled.** The most tempting mixed point
near the diagonal: $2^3\cdot3^{-2}=8/9$, $\log(8/9)\approx-0.1178$. Test
$f=u+\theta\,u(\cdot\,\cdot\,(9/8))$ with $\epsilon<\tfrac14|\log(8/9)|$: $g$ lives
in $\log x\in\{0,\pm\log(8/9)\}+[-2\epsilon,2\epsilon]$, and **no** $2^m$ nor
$3^n$ with $m,n\ne0$ falls there: $Q_X=2\log6\cdot g(1)=2\log6\,(1+\tfrac89|\theta|^2)>0$
for every $\theta$. The adversarial phase finds no coefficient: the
multiplicative near-coincidences $2^a\approx3^b$ (Kronecker) do not couple with
the arithmetic side because the Weil mass at $2^a3^{-b}$ is **zero** (Prop. 1.3). In
the impure object this protection does not exist along the impure prime's own
progression — exactly the difference between §3 and §4.

**6.5. Short window, numerical check of 5.2(a).** A real $f$ supported in
$[1,1.9]$ ($2T=\log1.9<\log2$): the ratios $y/y'\in(1/1.9,1.9)$ do not reach
$2^{\pm1},3^{\pm1}$: $Q_X=2\log6\,\|f\|_w^2$, exact. Any truncated modulated
Gaussian in that window gives the same: in a short window the object is blind to
all structure of the test except its norm. ✓

---

## 7. [THEOREM A′ + BRIDGE] The induction and the localization of the wall

### 7.1. The $n$-prime theorem (the induction is trivial — that is information)

**[THEOREM 7.1].** Let $p_1<\dots<p_n$ be primes, $\alpha_i$ pure
($|\alpha_i|=\sqrt{p_i}$), and $X_S:=F_{p_1,\alpha_1}\star\cdots\star F_{p_n,\alpha_n}
=(\sum_ia_i,\,0,\,-2\log(p_1\cdots p_n))$. Then:
(a) $X_S$ satisfies H and H₂, with
$Q_{X_S}(f,f)=2\sum_{i}\sum_{\xi\in\Lambda_{p_i}}|\hat F(\xi)|^2\ge0$.
(b) If some $\alpha_i$ is impure, H fails (two-bump test on $p_i$;
the other primes contribute only the diagonal $2\sum_{j\ne i}L_{p_j}$, barrier
$|c^{(i)}_M|>2p_i^{M/2}\bigl(\sum_jL_{p_j}\bigr)/L_{p_i}$, exceeded for $M$
large): **H $\iff$ purity of all factors.**
(c) Short window $2T\le\log p_1$: $Q_{X_S}=2\log(p_1\cdots p_n)\|f\|_w^2$ exactly;
kernel threshold exactly at $2T=\log(p_1\cdots p_n)$ (definite below,
infinite-dimensional kernel above).
(d) Margin against the multi-bump Mertens family:
$\min Q=\tfrac{4\sum_{i<j}L_{p_i}L_{p_j}}{\sum_iL_{p_i}}$, uniform in the heights.

*Proof.* Verbatim those of §3–§6: (a) additivity (Prop. 1.2, associative by
construction) + Poisson per factor + divisor on the line; (b) the proof of 4.1 with
$L_q\rightsquigarrow\sum_{j\ne i}L_{p_j}$ and separation by unique factorization
($p_i^m\ne$ product of powers of the others — finitely many candidates, small
$\epsilon$); (c) those of 5.2/5.4 with $n$ progressions (the Jensen count sums
densities; the construction uses $D_{p_1}\cdots D_{p_n}g$); (d) the account of 6.3
with $n$ adversaries. $\square$

**The step $n\to n+1$ uses nothing from $n$:** the argument is **additive**, not
inductive in the strong sense. This is information about the wall, not a
disappointment: it means that all the difficulty of RH is in the **limit**, not in any
finite step. Let us localize it precisely.

### 7.2. [BRIDGE] The four breaking points toward ζ

Let $X_y:=\star_{p\le y}F_{p,\alpha_p}$ (all pure) and look at $y\to\infty$.
Prior declaration, without makeup: the limit of the $X_y$ **is not** $\zeta$ — and
understanding exactly why is the content of this bridge.

**B1 (the diagonal mass diverges).** $\omega_y\equiv-2\sum_{p\le y}\log p=-2\theta(y)
\to-\infty$. For a fixed $f$ with $f(1)\ne0$, the primes $p>e^{2T}$ (outside
the window) each contribute $2L_p\,f(1)$: $W_{X_y}(f)=2\theta(y)f(1)+O_f(1)$
**diverges**. The limit object has no admissible $\omega$: renormalization is needed
(subtract $2\theta(y)\delta_1$). In ζ, the role of that infinite diagonal mass
is played by a datum of a different type: the polar block $[0]+[1]$ plus the
Archimedean density $\Omega(t)\sim2\log(t/2\pi)$ — **a divergent constant in $y$
traded for growth in $t$**. That trade is the appearance of the gamma
factor/the conductor, and it is not a step of the category: it is analytic
continuation entering through the window.

**B2 (divisor of the limit ≠ limit of divisors; positivity passes, spectrality does
not).** Each $X_y$ is spectral with divisor = union of lattices
**on the critical line** (purity!), $N_{Z_y}(T)\sim\tfrac{2\theta(y)}{\pi}T$.
If the renormalized functionals converged to a functional $W_\infty$, the
positivity $Q_\infty\ge0$ would pass to the limit effortlessly (pointwise limit of
forms $\ge0$). What does NOT pass to the limit is the **explicit formula**: the
Dirichlet-series analogue $\prod_pD_{p,\alpha_p}(s)^{-1}$-style diverges in the
critical strip, and the zeros of the continuation of the infinite product (if it exists)
are not limits of the zeros of the partial products — the lattices densify
($N(T)/T\to\infty$) and the true limit divisor has $N(T)\sim cT\log T$,
a different growth class. **The transmutation is here: the comparison functor
$U$ (Doc 131 §7.2) commutes with limits in $\mathcal{A}rith$ but not in
$\mathcal{A}rith^{EF}$.** In the program's phrasing: positivity is stable
under weak limits; the *spectrality* (existence of the divisor with EF) is
exactly what the limit must re-prove, and that is analytic continuation +
the Weil contour — RH-hard.

**B3 (the weight mismatch: ζ is not the limit of its own pure factors).**
The pure objects of this document have local weight 1: $|\alpha_p|=\sqrt p$,
symmetry $\sigma:s\mapsto1-\bar s$ **factor by factor**. The Euler factors of
ζ have $\alpha=1$, $|\alpha|=1=\sqrt{p^0}$: weight 0. Read as a one-prime
object in our normalization, ζ's factor has $c_m=1+p^m$ — **maximal**
violation of the Ramanujan barrier $|c_m|\le2p^{m/2}$ (its local zeros
live at $\mathrm{Re}=0$ and $\mathrm{Re}=1$, not at $\tfrac12$): **each ζ
factor is $\sigma$-impure and, in isolation, violates H** (Doc 131, Theorem 6.7). The
symmetry $s\leftrightarrow1-\bar s$ of ζ is not local: it is manufactured by the
global functional equation (pole + gamma) — the recentering of the weight $0$
to $\tfrac12$ is a **global** phenomenon. Consequence for Conjecture H⁺:
our pure objects have **constructive** arithmetic term (the $c_m>0$ enter adding
to the diagonal: in the object's slot, $a(p^m)=-L_pc_m\le0$), while the
class of H⁺ asks for $a\ge0$ ($a=\Lambda$-like): **destructive** regime, where
primes subtract and positivity must come from the polar block. Theorem 3.1 is the
first two-prime theorem of the category, but it lives in the constructive regime;
**it is not yet the inductive step of H⁺** — it is its mirror twin. (It is exactly
the constructive/destructive dichotomy the program already knew at the level of
peaks and valleys; here it appears as the sign of the datum $a$ relative to the
diagonal.)
**[GAP-135.B]:** the first genuine case of H⁺: the semilocal object
$(\Lambda\cdot1_{\{2^m,3^n\}},\,[0]+[1],\,\omega_{\mathrm{std}})$ — two primes,
$a\ge0$, standard polar block. Decide H for that object (it is Conjecture 100.A
of the program in its minimal two-prime version; a counterexample would refute H⁺).
That is the natural Doc 136.

**B4 (the order of the window/prime limits).** The finite theorems live in the
quadrant "primes $\le y$ fixed, window $2T<\log\prod_{p\le y}p=\theta(y)$": the
zone of definiteness grows with $y$ (Theorem 7.1(c)) — the direction is correct.
But the gap below the threshold is, after renormalizing the divergent diagonal
(B1), a statement about $W_{X_y}-2\theta(y)\delta_1$, and the family of tests
relevant to ζ requires $T\to\infty$ **before** $y$ (Weil's criterion
quantifies over all tests at once, and ζ's zeros require arbitrary windows).
The missing fine statement is exactly the limit rigidity lemma (Doc 131, Wish
7.2): gap $\mu_y(T)$ with joint control in $(y,T)$ surviving
$\lim_T\lim_y\ \ne\ \lim_y\lim_T$. Theorems 5.2/5.4/7.1(c) give
the first real quantitative information about $\mu_y(T)$: exact identity in
short window, kernel threshold at $\theta(y)$, and the Diophantine
obstruction (GAP-135.A) as the only missing ingredient in the intermediate region.

**Synthesis of the bridge.** The positivity step is additive and indestructible; the
transmutation toward ζ MUST occur, and it does, at B2 (spectrality of the limit =
analytic continuation) fed by B1 (renormalization of the diagonal) and
masked by B3 (the constructive→destructive regime change: ζ is not in
the closure of the pure weight-1 objects, but in the H⁺ class with polar term). Whoever
wants the limit has to pay exactly there — now the price and the counter are known.

---

## 8. The map

**Proved [THEOREM], with complete proof in this document:**
- Composition law: $W$ additive under $\star$; zero Weil mass on the mixed
  support $p^aq^b$ (Props. 1.2–1.3, via Doc 131 Lemma 1.7).
- $X_{p,q}$ Hermitian, admissible, spectral; divisor = two
  incommensurable progressions, not a lattice (Lemmas 1.6–1.7, Prop. 2.1).
- **Theorem A (3.1):** bilateral purity $\Rightarrow$ H and H₂, exact
  spectral identity — first Weil positivity theorem with two incommensurable
  primes, external to ζ.
- **Theorem B (4.1) and Corollary 4.2:** impurity of any factor $\Rightarrow$
  $\neg$H, with explicit test; H decidable in the two-prime subcategory:
  **H $\iff$ bilateral purity** (barrier shifted to $2p^{M/2}(1+L_q/L_p)$).
- **Fine structure (5.1–5.4):** identity $Q=2\log(pq)\|f\|_w^2$ in window
  $\le\log\min(p,q)$; gap $2\log q$ up to $\log q$, uniform in the second prime;
  kernel threshold exactly at $\log(pq)$ (Jensen + construction); kernel =
  tests invisible to both factors.
- Repulsion of near-collisions by Baker with trivial phases (Prop. 5.6;
  [DATUM] Baker/LMN).
- **Theorem A′ (7.1):** all of the above for $n$ primes, with Mertens margin
  $4\sum_{i<j}L_iL_j/\sum_iL_i$ and kernel threshold $\log(p_1\cdots p_n)$.
- [COMPUTATION §6] The full $2$–$3$ toy model: minima $1.5236$, $4\log3$,
  $4\log2\log3/\log6\approx1.7000$; decoupling of the mixed adversary $8/9$.

**[BRIDGE] (declared status):** B1–B4 (§7.2) — the localization of the wall: the
positivity passes to the limit, spectrality does not; ζ is not the limit of its
factors (weight 0 vs. 1, destructive vs. constructive regime); the trade-off
$\theta(y)\leftrightarrow\Omega(t)$ is analytic continuation. None of this
brings RH closer; it redistributes the difficulty to a named point of the functor $U$.

**[WISH]:** that the additive margin $2\sum_{i<j}L_iL_j/\log P$ have a
renormalized analogue surviving $y\to\infty$ (the strong form of the rigidity lemma,
Doc 131 Wish 7.2).

**[GAP], named:**
- **GAP-135.A:** uniform gap in intermediate windows
  $\log q<2T<\log pq$ — frames of exponentials over two
  incommensurable progressions; the constant must depend on the irrationality
  measure of $\log p/\log q$ (Baker gives the repulsion; the frame theorem is missing).
- **GAP-135.B:** the semilocal object with $a\ge0$ and standard polar block
  (two primes, destructive regime): the first genuine test of H⁺ and the minimal
  content of Conjecture 100.A. **Next document.**

---

## References

**Internal (backward-only):** Doc 131 (category $\mathcal{A}rith$: Def. 2.1,
Lemma 1.7, Prop. 2.8, Def. 4.1, Thm. 4.4, Thm. 4.9, Prop. 6.2, Thm. 6.6, Thm. 6.7,
Wish 6.9, Wish 7.2, §9); Doc 125 (G-125.B: two incommensurable primes);
Doc 107 (two-variable Weil functional, thickened kernel); Doc 110 (class
$\mathcal F$, test-accessibility); Doc 119 (R-NC/NC2).

**Literature [DATUM]:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*,
  Comm. Sém. Math. Lund (1952), 252–265.
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime
  numbers I*, Rend. Mat. Acc. Lincei (9) 11 (2000), 183–233.
- A. Baker, *Linear forms in the logarithms of algebraic numbers*, Mathematika 13
  (1966), 204–216; A. Baker, *Transcendental Number Theory*, CUP 1975.
- M. Laurent, M. Mignotte, Y. Nesterenko, *Formes linéaires en deux logarithmes et
  déterminants d'interpolation*, J. Number Theory 55 (1995), 285–321 (two
  logarithms, explicit constants).
- R. P. Boas, *Entire Functions*, Academic Press 1954 (exponential type, Jensen,
  density of zeros).
- K. Seip, *Interpolation and Sampling in Spaces of Analytic Functions*, AMS Univ.
  Lecture Series 33, 2004 (exponential frames, Beurling–Landau
  densities).
- H. L. Montgomery, R. C. Vaughan, *Multiplicative Number Theory I*, CUP 2007
  (Mertens, $3+4\cos\theta+\cos2\theta$).

*End of Document 135.*
