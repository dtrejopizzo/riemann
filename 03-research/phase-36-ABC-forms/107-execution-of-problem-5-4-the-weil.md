# Doc 107 — Execution of Problem 5.4: the Weil formula in two variables with diagonal multiplicative kernel

**Phase 36 — Forms A/B/C ·**
**Prerequisites:** Doc 106 (§3 Prop. 3.5, §5 Lemmas 5.2/5.3, Problem 5.4); Doc 98 (toy model, Prop. 6.1); Doc 96 (Theorem 8.1); Doc 94 (condition C5); P35 (Weil form, Hypothesis D); P41 §7.
**Absolute rule:** no proof is fabricated. Every step is either a complete proof or a declared GAP.

---

## 0. Executive summary

This document executes the experiment of Problem 5.4 of Doc 106: formulate the
explicit Weil formula in two variables, insert the thickened diagonal multiplicative
kernel $h(x_1,x_2) = g(x_1x_2)\,\varphi(x_1/x_2)$, and decide whether the resulting
functional $\mathcal{W}_2$ is a candidate for Missing Lemma 5.2 (analytic realization of
the tensor square) or whether MW-7 reappears.

**Main findings:**

1. **(§2) The double formula exists and is unconditional.** $\mathcal{W}_2 := \mathcal{W}
   \otimes \mathcal{W}$ is well defined on $C_c^\infty((\mathbb{R}_+^*)^2)$ by
   iterating the one-variable formula; the double zero side converges
   **absolutely** (Paley–Wiener + zero density), and the full expansion of the
   product has nine blocks (poles², poles×primes, poles×∞, primes², primes×∞, ∞²,
   and symmetric ones), all written out in §2.3.

2. **(§3) The thickened kernel produces the Minkowski sum.** The crude diagonal
   restriction $g(x_1x_2)$ diverges (Lemma 3.1: the transverse integral $\int_0^\infty
   v^{s_1-s_2-1}dv$ diverges for every value of the exponent). With the thickening
   $h = g(x_1x_2)\varphi(x_1/x_2)$ and the change $u = x_1x_2$, $v = x_1/x_2$ (Jacobian
   $dx_1dx_2 = \tfrac{1}{2v}\,du\,dv$, transverse exponent $v^{(s_1-s_2)/2-1}$):
   $$\hat h(s_1,s_2) = \tfrac12\,\hat g\!\left(\tfrac{s_1+s_2}{2}\right)
     \hat\varphi\!\left(\tfrac{s_1-s_2}{2}\right),$$
   and the zero term is $\tfrac12\sum_{\rho_1,\rho_2}
   \hat g\bigl(\tfrac{\rho_1+\rho_2}{2}\bigr)\hat\varphi\bigl(\tfrac{\rho_1-\rho_2}{2}\bigr)$:
   exactly the spectrum of $\tfrac12(H_C\otimes I + I\otimes H_C)$ with spectral weight
   on the difference. Condition 1 of Lemma 5.2 is verified (§5).

3. **(§4) The arithmetic side is AUTONOMOUS.** The primes×primes term is a
   **weighted transform of $\Lambda\star\Lambda$**: $\sum_N g(N)\sum_{d\mid N}
   \Lambda(d)\Lambda(N/d)\,\varphi(d^2/N)$ plus three finite-support terms — it lives in
   the semigroup of almost-primes with explicit arithmetic coefficients, computable without
   positions of zeros. **The mixed zeros×primes terms get reabsorbed**: they are
   artifacts of the semi-expanded presentation; iterated application of the
   one-variable formula turns them into arithmetic×arithmetic terms. **MW-7 does NOT
   reappear in the functional.** Where it would reappear (and this is delimited precisely, §4.5): if
   a *genuine one-variable* explicit formula were demanded for the double object in
   the sum variable $\sigma$ alone — the multiplicity function $w_\varphi(\sigma)$ depends
   on the zeros. Lemma 5.2 does not demand that.

4. **(§5) The $(8,8)$ signature of the tensor block SURVIVES.** In the toy model
   ($m=1$, quadruple $\{1/2\pm\delta\pm i\gamma_0\}$), the 16 pairs $(\rho_i,\rho_j)$
   pair up under the involution $(\rho_1,\rho_2)\mapsto(1-\bar\rho_1,1-\bar\rho_2)$ into
   **8 fixed-point-free orbits** = 8 hyperbolic planes: signature $(8,8)$,
   negative index $8 = (4m)^2/2$, exactly Proposition 3.5 of Doc 106. The weight
   $\hat\varphi$ **does not degenerate** the signature — on the contrary, it is what saves it: within
   the degenerate eigenspaces of the sum ($\sigma = 0, \pm i\gamma_0$) only the
   difference variable separates the pairs. And the statement's conjecture ("do the
   real sums $\pm 2\delta$ carry the negative index?") turns out **instructively
   false**: the real sums carry only $2$ of the $8$ negatives; **half the
   negative index lives in purely imaginary sums** ($\rho_i+\rho_j-1 \in
   i\mathbb{R}$), where off-criticality is stored in the difference variable
   that only $\hat\varphi$ sees.

5. **(§6) Balance against Lemmas 5.2/5.3.** Lemma 5.2: condition 1 ✓, condition 2 ✓ —
   **Lemma 5.2 has a candidate**: $X_2 = \mathcal{W}_2$ restricted to thickened
   kernels. The entire weight transfers to Lemma 5.3 (finiteness bound), where the
   analysis identifies, for the first time in the program, a genuinely non-spectral and
   unconditional source of bounds: **sieve upper bounds on the
   almost-prime semigroup** (Selberg; the parity problem blocks asymptotics, not upper
   bounds). The exact gap that remains is the **sieve→index bridge** (Missing
   Lemma 7.2). Documented transmutation risk: if the required bound turned out to need
   the *asymptotic* of $\Lambda\star\Lambda$, the wall is pair correlation/
   Hardy–Littlewood (via Montgomery / Goldston–Montgomery) — a parity wall,
   **not** CAP.

**VERDICT: LIVE CANDIDATE** (§8). Lemma 5.2 has an explicit candidate; MW-7 does not
reappear either in the mixed terms or on the almost-prime side; the $(8,8)$ block is
verified without degeneration. The next lemma to be proved is stated precisely
(Missing Lemma 7.2).

---

## 1. Normalization: the explicit Weil formula in one variable

### 1.1. Test class and transform

**Definition 1.1 (test class).** Throughout the document, the class of test
functions is $C_c^\infty(\mathbb{R}_+^*)$ (smooth, compactly supported on $(0,\infty)$); in
two variables, $C_c^\infty((\mathbb{R}_+^*)^2)$. For $f \in C_c^\infty(\mathbb{R}_+^*)$,
the Mellin transform is
$$\hat f(s) = \int_0^\infty f(x)\,x^{s-1}\,dx,$$
entire in $s$ (compact support). The involution is $\tilde f(x) =
\overline{f(1/x)}\,x^{-1}$, with $\widehat{\tilde f}(s) = \overline{\hat f(1-\bar s)}$.

**Lemma 1.2 (multiplicative Paley–Wiener and absolute convergence of the zero side).**
Let $f \in C_c^\infty(\mathbb{R}_+^*)$ with $\mathrm{supp}\,f \subseteq [e^{-a}, e^{a}]$.
Then for every $N \geq 0$ and every $\sigma$ in a compact subset of $\mathbb{R}$:
$$|\hat f(\sigma+it)| \;\leq\; C_N(f,\sigma)\,(1+|t|)^{-N}.$$
Consequently, $\sum_\rho |\hat f(\rho)| < \infty$, where $\rho$ ranges over the non-trivial
zeros of $\zeta$ (with multiplicity).

*Proof.* With $x = e^u$: $\hat f(\sigma+it) = \int_{\mathbb{R}}
f(e^u)e^{\sigma u}\,e^{itu}\,du$ is the Fourier transform of the function
$u \mapsto f(e^u)e^{\sigma u} \in C_c^\infty([-a,a])$; integration by parts $N$ times
gives the bound, uniform for $\sigma$ in compact sets because $e^{\sigma u} \leq e^{|\sigma| a}$
on the support. For the sum over zeros: every $\rho = \beta + i\gamma$ has
$\beta \in (0,1)$ (compact), and the number of zeros with $|\gamma| \leq T$ is
$N(T) \ll T\log T$ (von Mangoldt; [IK04], Thm. 5.8 or Titchmarsh Ch. IX). Then
$\sum_\rho |\hat f(\rho)| \ll \sum_\rho (1+|\gamma|)^{-3} \ll \int_1^\infty
\frac{\log T}{T^3}\,dT\cdot C + C' < \infty$. $\square$

### 1.2. The explicit formula

**Definition 1.3 (the three arithmetic blocks).** For $f \in
C_c^\infty(\mathbb{R}_+^*)$:
$$D(f) := \hat f(0) + \hat f(1) \qquad \text{(poles: } s=1 \text{ of } \zeta
\text{ and the reflection } s=0\text{)},$$
$$P(f) := \sum_{n\geq 2} \Lambda(n)\,\bigl[f(n) + n^{-1} f(1/n)\bigr]
\qquad \text{(primes; } \Lambda = \text{von Mangoldt; sum FINITE by compact
support)},$$
$$A(f) := \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat f\!\left(\tfrac12 + it\right)
\Omega(t)\,dt, \qquad
\Omega(t) := \log\pi - \mathrm{Re}\,\frac{\Gamma'}{\Gamma}\!\left(\tfrac14 +
\tfrac{it}{2}\right) \quad \text{(archimedean)}.$$
$\Omega$ is real, even in $t$, and $\Omega(t) = -\log|t| + O(1)$; the integral converges
absolutely by Lemma 1.2.

**Theorem 1.4 (Weil 1952; declared normalization).** For every $f \in
C_c^\infty(\mathbb{R}_+^*)$:
$$\boxed{\;\mathcal{W}(f) \;:=\; \sum_\rho \hat f(\rho)
\;=\; D(f) \;-\; P(f) \;-\; A(f).\;}$$

*Status of the proof and of the normalization.* This is the classical explicit formula
[Weil 1952; Bombieri 2000; IK04, Thm. 5.12 specialized to $\zeta$ and rewritten in
multiplicative variable $x = e^u$ with trivial weight]: it is obtained by integrating
$-\frac{\xi'}{\xi}(s)\hat f(s)$ over a contour enclosing the critical strip, using
$\xi(s) = \pi^{-s/2}\Gamma(s/2)\zeta(s)$, $-\frac{\zeta'}{\zeta}(s) = \sum_n
\Lambda(n)n^{-s}$ on $\mathrm{Re}(s) = 2$, the functional equation for the line
$\mathrm{Re}(s) = -1$ (which produces the mirror term $n^{-1}f(1/n)$ via
$\frac{1}{2\pi i}\int \hat f(s)n^{s-1}ds = n^{-1}f(1/n)$ on the reflected line), and
the factor $\Gamma_{\mathbb{R}}$ for $A$. **Precision statement:** the exact form
of $\Omega$ (constants $\log\pi$, $\gamma$, and the $x$-space version of the
archimedean term as a principal value) varies between equivalent presentations
[Weil 1952, Bombieri 2000]; in this document **only** two properties of $A$ are used:
(A1) it is computable without positions of zeros; (A2) it is the integral of $\hat f$ over the
critical line against a fixed even weight of logarithmic growth. No result of
§§2–8 depends on the exact constants of $\Omega$. The P35 normalization
(Def. weil, with weight $p^{-n/2}$) corresponds to the unitary change $f \mapsto x^{1/2}f$;
the structural results are invariant under that change.

**Remark 1.5 (the Weil distribution).** Theorem 1.4 says that the tempered
distribution (in $u = \log x$)
$$W \;=\; \underbrace{\delta_{\hat\cdot=0} + \delta_{\hat\cdot=1}}_{D}
\;-\; \underbrace{\textstyle\sum_n \Lambda(n)\,[\delta_n + n^{-1}\delta_{1/n}]}_{P}
\;-\; \underbrace{A}_{\text{smooth kernel}}$$
has the zero-counting measure as its "spectral transform". The whole
document exploits an asymmetry: **the right-hand (arithmetic) side does not mention the zeros**.

---

## 2. (i) The Weil formula in two variables: full expansion

### 2.1. Iterated definition and well-definedness

**Definition 2.1 (double functional).** For $h \in C_c^\infty((\mathbb{R}_+^*)^2)$:
$$\mathcal{W}_2(h) \;:=\; \mathcal{W}^{(1)}\Bigl[\,x_1 \longmapsto
\mathcal{W}^{(2)}\bigl[h(x_1,\cdot)\bigr]\Bigr],$$
where $\mathcal{W}^{(i)}$ is the Weil functional (Theorem 1.4) applied in the
$i$-th variable.

**Lemma 2.2 (well-definedness, symmetry, and two presentations).** For every
$h \in C_c^\infty((\mathbb{R}_+^*)^2)$:

(a) The function $F(x_1) := \mathcal{W}^{(2)}[h(x_1,\cdot)]$ belongs to
$C_c^\infty(\mathbb{R}_+^*)$, so Definition 2.1 makes sense, and the
result is symmetric: iterating in the opposite order gives the same value.

(b) **Spectral presentation:**
$$\mathcal{W}_2(h) = \sum_{\rho_1}\sum_{\rho_2} \hat h(\rho_1,\rho_2),
\qquad \hat h(s_1,s_2) := \int_0^\infty\!\!\int_0^\infty
h(x_1,x_2)\,x_1^{s_1-1}x_2^{s_2-1}\,dx_1\,dx_2,$$
with **absolute** convergence of the double sum.

(c) **Arithmetic presentation:** $\mathcal{W}_2(h) = \langle (D-P-A)\otimes(D-P-A),\,
h\rangle$, expanded in §2.3, **with no positions of zeros**.

*Proof.* (a) We use the arithmetic presentation of $\mathcal{W}^{(2)}$:
$F(x_1) = D^{(2)}h - P^{(2)}h - A^{(2)}h$ where
$D^{(2)}h = \int h(x_1,x_2)\,\frac{dx_2}{x_2} + \int h(x_1,x_2)\,dx_2$,
$P^{(2)}h = \sum_n \Lambda(n)[h(x_1,n) + n^{-1}h(x_1,1/n)]$ (finite sum: only the $n$
with $n$ or $1/n$ in the projection of the support), and $A^{(2)}h$ is the integral of the
archimedean kernel against the partial transform $\int h(x_1,x_2)x_2^{-1/2+it}dx_2$, which is
smooth of compact support in $x_1$ and of rapid decay in $t$ with all derivatives
in $x_1$ (Lemma 1.2 with parameter, differentiation under the integral sign with uniform
dominance over the compact support). Each of the three blocks is $C_c^\infty$ in
$x_1$ with support contained in the projection of the support of $h$. Order symmetry
follows from (b)–(c): both presentations are manifestly symmetric and are proved
for the iterated definition in either order. (b) Applying Theorem 1.4 in
variable 1 to $F$: $\mathcal{W}_2(h) = \sum_{\rho_1}\hat F(\rho_1)$, and
$\hat F(\rho_1) = \mathcal{W}^{(2)}[\,x_2 \mapsto \int h(x_1,x_2)x_1^{\rho_1-1}dx_1\,]
= \sum_{\rho_2}\hat h(\rho_1,\rho_2)$, where the interchange
$\int dx_1 \leftrightarrow (D-P-A)^{(2)}$ is legitimate (finite sums and
absolutely convergent integrals over compact supports). Absolute convergence of the
double sum: by the argument of Lemma 1.2 in two variables,
$|\hat h(\rho_1,\rho_2)| \ll_N (1+|\gamma_1|)^{-N}(1+|\gamma_2|)^{-N}$ uniformly in
the (compact) real parts, and $N(T) \ll T\log T$ in each factor. (c) Apply the
arithmetic presentation in both variables; each cross term is a finite sum or an
absolutely convergent integral. $\square$

**Remark 2.3 (factorization).** If $h(x_1,x_2) = f_1(x_1)f_2(x_2)$, then
$\hat h(s_1,s_2) = \hat f_1(s_1)\hat f_2(s_2)$ and $\mathcal{W}_2(h) =
\mathcal{W}(f_1)\,\mathcal{W}(f_2)$: the double formula factorizes as
$\mathcal{W}\otimes\mathcal{W}$, as the experiment requires. The non-trivial content of
Definition 2.1 is that it extends $\mathcal{W}\otimes\mathcal{W}$ to **non-factorizable**
kernels — which is what the diagonal kernel needs.

### 2.2. Notation for the expansion

We write the one-variable formula as $\mathcal{W} = D - P - A$ and expand the
tensor product. With signs:
$$\mathcal{W}_2 = (D-P-A)\otimes(D-P-A)
= D{\otimes}D - D{\otimes}P - D{\otimes}A - P{\otimes}D + P{\otimes}P + P{\otimes}A
- A{\otimes}D + A{\otimes}P + A{\otimes}A.$$

### 2.3. The nine blocks, explicitly

For a general $h \in C_c^\infty((\mathbb{R}_+^*)^2)$:

**(1) Poles×poles:**
$$D{\otimes}D(h) = \hat h(0,0) + \hat h(0,1) + \hat h(1,0) + \hat h(1,1).$$

**(2) and (2') Poles×primes:**
$$D{\otimes}P(h) = \sum_{n}\Lambda(n)\Bigl[\hat h_1(0;n) + \hat h_1(1;n)
+ n^{-1}\hat h_1(0;1/n) + n^{-1}\hat h_1(1;1/n)\Bigr],$$
where $\hat h_1(s;y) := \int_0^\infty h(x_1,y)\,x_1^{s-1}dx_1$ (partial Mellin in the
first variable, second one evaluated). $P{\otimes}D$ is the symmetric term.

**(3) and (3') Poles×archimedean:** $D{\otimes}A(h) = \frac{1}{2\pi}\int \Omega(t)
\bigl[\hat h(0,\tfrac12+it) + \hat h(1,\tfrac12+it)\bigr]dt$; symmetric for
$A{\otimes}D$.

**(4) Primes×primes:**
$$P{\otimes}P(h) = \sum_{n_1,n_2}\Lambda(n_1)\Lambda(n_2)\Bigl[
h(n_1,n_2) + n_2^{-1}h(n_1,\tfrac{1}{n_2}) + n_1^{-1}h(\tfrac{1}{n_1},n_2)
+ (n_1n_2)^{-1}h(\tfrac{1}{n_1},\tfrac{1}{n_2})\Bigr],$$
finite sum (compact support in both variables).

**(5) and (5') Primes×archimedean:** $P{\otimes}A(h) = \frac{1}{2\pi}\sum_n
\Lambda(n)\int\Omega(t)\bigl[\hat h_2(n;\tfrac12+it) + n^{-1}
\hat h_2(\tfrac1n;\tfrac12+it)\bigr]dt$, with $\hat h_2(y;s) := \int h(y,x_2)
x_2^{s-1}dx_2$; symmetric for $A{\otimes}P$.

**(6) Archimedean×archimedean:**
$$A{\otimes}A(h) = \frac{1}{4\pi^2}\iint \Omega(t_1)\Omega(t_2)\,
\hat h\!\left(\tfrac12+it_1,\,\tfrac12+it_2\right)dt_1\,dt_2.$$

**Theorem 2.4 (Weil formula in two variables).** For every
$h \in C_c^\infty((\mathbb{R}_+^*)^2)$:
$$\sum_{\rho_1,\rho_2}\hat h(\rho_1,\rho_2)
= D{\otimes}D(h) - D{\otimes}P(h) - P{\otimes}D(h) - D{\otimes}A(h) - A{\otimes}D(h)$$
$$\qquad\qquad + P{\otimes}P(h) + P{\otimes}A(h) + A{\otimes}P(h) + A{\otimes}A(h),$$
with all blocks absolutely convergent and **none dependent on the
positions of the zeros**.

*Proof.* Lemma 2.2(b)(c) with the sign expansion of §2.2. $\square$

**Remark 2.5 (where the mixed zeros×primes terms live).** In the product of
two one-variable formulas for a factorizable $h = f_1 f_2$, one can write
$\mathcal{W}(f_1)\mathcal{W}(f_2) = \bigl(\sum_{\rho_1}\hat f_1(\rho_1)\bigr)\cdot
\bigl(D-P-A\bigr)(f_2)$: "zeros×primes" terms appear,
$-\sum_{\rho_1}\hat f_1(\rho_1)\cdot P(f_2)$. That is a **semi-expanded
presentation**: it mixes the spectral side of one factor with the arithmetic side of the other. The
Theorem 2.4 shows that the **fully arithmetic** expansion exists and contains no
zeros. The fine analysis of this reabsorption for the non-factorizable kernel — the point
where the experiment is decided — is in §4.4.

---

## 3. (ii) The diagonal multiplicative kernel

### 3.1. The crude restriction diverges

**Lemma 3.1 (divergence of the crude diagonal).** Let $g \in
C_c^\infty(\mathbb{R}_+^*)$, $g \not\equiv 0$, $g \geq 0$, and $h_0(x_1,x_2) :=
g(x_1x_2)$. Then the double Mellin integral
$$\int_0^\infty\!\!\int_0^\infty g(x_1x_2)\,x_1^{s_1-1}x_2^{s_2-1}\,dx_1\,dx_2$$
**diverges for every** $(s_1,s_2) \in \mathbb{C}^2$.

*Proof.* Change $u = x_1x_2$, $v = x_1$: $x_2 = u/v$, Jacobian
$dx_1\,dx_2 = \frac{du\,dv}{v}$, integrand $g(u)\,v^{s_1-1}(u/v)^{s_2-1} =
g(u)\,u^{s_2-1}\,v^{s_1-s_2}$. The integral separates:
$$\Bigl(\int_0^\infty g(u)u^{s_2-1}du\Bigr)\cdot\Bigl(\int_0^\infty
v^{s_1-s_2-1}\,dv\Bigr),$$
and $\int_0^\infty v^{c-1}dv$ diverges for every $c \in \mathbb{C}$ (at $0$ if
$\mathrm{Re}\,c \leq 0$, at $\infty$ if $\mathrm{Re}\,c \geq 0$; at both if
$\mathrm{Re}\,c = 0$). The defect is geometric: $h_0$ is constant along the
hyperbolas $x_1x_2 = \mathrm{const}$, which are the non-compact orbits of the
anti-diagonal flow $(x_1,x_2)\mapsto(\lambda x_1,\lambda^{-1}x_2)$; $h_0 \notin
C_c^\infty((\mathbb{R}_+^*)^2)$ and is not in the domain of $\mathcal{W}_2$. $\square$

### 3.2. The thickened kernel and the exact change of variables

**Definition 3.2 (thickened kernel).** For $g, \varphi \in
C_c^\infty(\mathbb{R}_+^*)$:
$$h_{g,\varphi}(x_1,x_2) := g(x_1x_2)\,\varphi(x_1/x_2)
\;\in\; C_c^\infty((\mathbb{R}_+^*)^2),$$
(compact support: $x_1 = \sqrt{uv}$, $x_2 = \sqrt{u/v}$ with $u \in \mathrm{supp}\,g$,
$v \in \mathrm{supp}\,\varphi$ compact).

**Lemma 3.3 (sum/difference coordinates).** The map $\Phi(x_1,x_2) := (u,v) =
(x_1x_2,\,x_1/x_2)$ is a **group isomorphism** $(\mathbb{R}_+^*)^2 \to
(\mathbb{R}_+^*)^2$, with inverse $x_1 = (uv)^{1/2}$, $x_2 = (u/v)^{1/2}$, and
$$dx_1\,dx_2 = \frac{du\,dv}{2v}, \qquad
\frac{dx_1\,dx_2}{x_1x_2} = \frac{1}{2}\,\frac{du\,dv}{u\,v}.$$

*Proof.* Bijection and homomorphism: immediate ($u,v$ are multiplicative
characters of $(x_1,x_2)$ and the inverse is globally defined because
$\mathbb{R}_+^*$ admits a unique square root). Jacobian: with $x_1 = u^{1/2}v^{1/2}$,
$x_2 = u^{1/2}v^{-1/2}$,
$$\frac{\partial(x_1,x_2)}{\partial(u,v)} = \det\begin{pmatrix}
\tfrac12 u^{-1/2}v^{1/2} & \tfrac12 u^{1/2}v^{-1/2}\\[2pt]
\tfrac12 u^{-1/2}v^{-1/2} & -\tfrac12 u^{1/2}v^{-3/2}\end{pmatrix}
= -\tfrac14 v^{-1} - \tfrac14 v^{-1} = -\frac{1}{2v},$$
hence $dx_1dx_2 = \frac{du\,dv}{2v}$; dividing by $x_1x_2 = u$ gives the Haar
measure: $\Phi$ pushes $d^*x_1\,d^*x_2$ to $\tfrac12\,d^*u\,d^*v$. $\square$

**Theorem 3.4 (double Mellin of the thickened kernel).** For every $(s_1,s_2) \in
\mathbb{C}^2$:
$$\hat h_{g,\varphi}(s_1,s_2)
= \frac{1}{2}\;\hat g\!\left(\frac{s_1+s_2}{2}\right)\,
\hat\varphi\!\left(\frac{s_1-s_2}{2}\right).$$

*Proof.* With Lemma 3.3:
$$x_1^{s_1-1}x_2^{s_2-1} = (uv)^{\frac{s_1-1}{2}}\,(u/v)^{\frac{s_2-1}{2}}
= u^{\frac{s_1+s_2}{2}-1}\;v^{\frac{s_1-s_2}{2}},$$
so the full integrand with respect to $du\,dv$ is
$$g(u)\,\varphi(v)\;u^{\frac{s_1+s_2}{2}-1}\;v^{\frac{s_1-s_2}{2}}\cdot\frac{1}{2v}
= \frac{1}{2}\,g(u)\,u^{\frac{s_1+s_2}{2}-1}\;\varphi(v)\,v^{\frac{s_1-s_2}{2}-1}.$$
**Verification of the $v$-exponent requested by the experiment: it is exactly
$v^{(s_1-s_2)/2\,-\,1}$** (the $-1$ comes from the Jacobian $\frac{1}{2v}$). Integrating,
the variables separate into two one-variable Mellin transforms. $\square$

**Remark 3.5 (the normalization $\hat g(\rho_1+\rho_2-1)$ of the statement).** The
statement of Problem 5.4 expected $\hat g(\rho_1+\rho_2-1)$. The two forms are the
same information: setting $G(t) := g(t^2)$, the substitution $u = t^2$ gives
$\hat g\bigl(\tfrac{s_1+s_2}{2}\bigr) = 2\,\hat G(s_1+s_2-1)$. We use the symmetric form
$\hat g\bigl(\tfrac{s_1+s_2}{2}\bigr)$ because it has the virtue that **the critical axis
of the double object is the same axis $\mathrm{Re} = 1/2$**: if $\rho_1,\rho_2$ are on
the critical line, so is $\tfrac{\rho_1+\rho_2}{2}$. The crude version with $u = x_1x_2$
and $v = x_1$ (Lemma 3.1) would have given $\hat g(s_2)\cdot(\text{divergent})$; the
symmetric thickening is what produces the genuine sum variable.

### 3.3. The double zero term: Minkowski sum with spectral weight

**Corollary 3.6 (spectral side of the diagonal functional).** For $h = h_{g,\varphi}$:
$$\mathcal{W}_2(h_{g,\varphi})
= \frac{1}{2}\sum_{\rho_1,\rho_2}
\hat g\!\left(\frac{\rho_1+\rho_2}{2}\right)
\hat\varphi\!\left(\frac{\rho_1-\rho_2}{2}\right),$$
with absolute convergence (Lemma 2.2(b)).

In the spectral parameter $z = \rho - \tfrac12$ (eigenvalue of $H_C$; Doc 96,
Prop. 4.10): $\tfrac{\rho_1+\rho_2}{2} = \tfrac12 + \tfrac{z_1+z_2}{2}$ and
$\tfrac{\rho_1-\rho_2}{2} = \tfrac{z_1-z_2}{2}$, hence
$$\mathcal{W}_2(h_{g,\varphi}) = \frac{1}{2}\sum_{z_1,z_2}
\hat g\!\left(\tfrac12 + \tfrac{z_1+z_2}{2}\right)
\hat\varphi\!\left(\tfrac{z_1-z_2}{2}\right):$$
**$\hat g$ sees the Minkowski sum of the spectra** $\{z_1+z_2\}$ (rescaled by the
harmless factor $\tfrac12$) **and $\hat\varphi$ places a spectral weight on the difference**
$z_1 - z_2$, exactly as Problem 5.4 anticipated.

**Proposition 3.7 (identification with $H_C\otimes I + I\otimes H_C$).** The diagonal
scaling flow $U^{(2)}_\lambda h(x_1,x_2) := h(\lambda x_1, \lambda x_2)$ acts on
the thickened kernels by $g(u) \mapsto g(\lambda^2 u)$, $\varphi$ invariant; its
generator is $H^{(2)} = H_C\otimes I + I\otimes H_C$ (with $H_C = -ix\partial_x$ in each
variable), which in coordinates $(u,v)$ is $2\,H_C^{(u)}\otimes I_v$. On the formal
spectral vectors $v_{z_1}\otimes v_{z_2}$ (residual functionals $\hat h \mapsto
\hat h(\rho_1,\rho_2)$, cf. Doc 98 Rem. 6.3), $H^{(2)}$ has eigenvalue $z_1+z_2$. The
Corollary 3.6 says that the spectral side of the diagonal functional is the sum, over
the spectrum of $H^{(2)}$, of $\hat g$ evaluated at $\tfrac12 + \tfrac{z_1+z_2}{2}$
(equivalently: $\hat G$ at $1 + (z_1+z_2)$ with $G(t) = g(t^2)$, Rem. 3.5), with
multiplicities resolved by the transverse weight $\hat\varphi\bigl(\tfrac{z_1-z_2}{2}
\bigr)$. **This is the spectrum that condition 1 of Lemma 5.2 requires.** The verification
that the tensor block $(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ appears with
its full signature requires the quadratic structure and is done in §5. $\square$

**Remark 3.8 (connection with Montgomery's pair correlation).** If all
zeros are on the line ($z_j = i\gamma_j$), Corollary 3.6 becomes
$$\frac{1}{2}\sum_{\gamma_1,\gamma_2} \hat g\!\left(\tfrac12 +
i\tfrac{\gamma_1+\gamma_2}{2}\right)\hat\varphi\!\left(i\tfrac{\gamma_1-\gamma_2}{2}
\right):$$
a form of **windowed smoothed pair correlation**, of the family studied by
Montgomery [Mon73] ($F(\alpha,T)$ is the case of a Lorentzian window and pure
exponential weight $\hat\varphi(it) = T^{i\alpha t}$-type). This is not a coincidence and is exploited in §7: the
identity "double zero side = almost-prime side" that this document establishes for the
thickened kernel is the two-test-function generalization of Montgomery's and
Goldston–Montgomery's pair-correlation ↔ primes dictionary [GM87].

---

## 4. (iii) The arithmetic side of the diagonal functional: the decisive question

We evaluate the nine blocks of Theorem 2.4 at $h = h_{g,\varphi}$. Notation:
$\sigma := \tfrac{s_1+s_2}{2}$, $\tau := \tfrac{s_1-s_2}{2}$.

### 4.1. Polar and archimedean blocks

**(1) Poles×poles.** By Theorem 3.4 with $(s_1,s_2) \in \{0,1\}^2$:
$$D{\otimes}D(h_{g,\varphi}) = \tfrac12\Bigl[\hat g(0)\hat\varphi(0)
+ \hat g\bigl(\tfrac12\bigr)\hat\varphi\bigl(-\tfrac12\bigr)
+ \hat g\bigl(\tfrac12\bigr)\hat\varphi\bigl(\tfrac12\bigr)
+ \hat g(1)\hat\varphi(0)\Bigr].$$

**Remark 4.1 (pole-pole resonance on the double critical axis).** The mixed pairs
$(s_1,s_2) = (0,1), (1,0)$ contribute at $\sigma = \tfrac12$: **the cross poles of the
double object fall on the same axis $\mathrm{Re}\,\sigma = \tfrac12$ where the
on-line zero sums live**. In the double object, "pole" and "critical spectrum" cease to be
separated by a strip: any positivity analysis of the spectral block must
first subtract this interior polar contribution, of rank $\leq 2$. It is recorded as a
structural feature (not an obstruction: it is finite rank and computable).

**(3)(3') Poles×archimedean and (6) archimedean².** By Theorem 3.4:
$$D{\otimes}A + A{\otimes}D = \frac{1}{4\pi}\int\Omega(t)\Bigl[
\hat g\bigl(\tfrac14{+}\tfrac{it}{2}\bigr)\hat\varphi\bigl({-}\tfrac14{+}\tfrac{it}{2}\bigr)
+ \hat g\bigl(\tfrac34{+}\tfrac{it}{2}\bigr)\hat\varphi\bigl(\tfrac14{-}\tfrac{it}{2}\bigr)
+ (\text{symmetric in } \tau \mapsto -\tau)\Bigr]dt,$$
$$A{\otimes}A(h_{g,\varphi}) = \frac{1}{8\pi^2}\iint\Omega(t_1)\Omega(t_2)\,
\hat g\bigl(\tfrac12 + i\tfrac{t_1+t_2}{2}\bigr)\,
\hat\varphi\bigl(i\tfrac{t_1-t_2}{2}\bigr)\,dt_1\,dt_2.$$
Absolutely convergent integrals of explicit data ($\Omega$, $\hat g$,
$\hat\varphi$): **computable with no zeros**.

### 4.2. The primes×primes block: the transform of $\Lambda\star\Lambda$

We evaluate the four summands of $P{\otimes}P$ at $h_{g,\varphi}$. With
$h(y_1,y_2) = g(y_1y_2)\varphi(y_1/y_2)$:
$$h(n_1,n_2) = g(n_1n_2)\,\varphi(n_1/n_2), \qquad
h(n_1,\tfrac1{n_2}) = g(n_1/n_2)\,\varphi(n_1n_2),$$
$$h(\tfrac1{n_1},n_2) = g(n_2/n_1)\,\varphi\bigl(\tfrac{1}{n_1n_2}\bigr), \qquad
h(\tfrac1{n_1},\tfrac1{n_2}) = g\bigl(\tfrac{1}{n_1n_2}\bigr)\,\varphi(n_2/n_1).$$

**Theorem 4.2 (almost-prime structure of the $P{\otimes}P$ block).** Let
$h = h_{g,\varphi}$. Then
$$P{\otimes}P(h) = \Sigma_{\mathrm{I}} + \Sigma_{\mathrm{II}} + \Sigma_{\mathrm{III}}
+ \Sigma_{\mathrm{IV}},$$
with:

**(I) Main term — weighted transform of $\Lambda\star\Lambda$:**
$$\Sigma_{\mathrm{I}} = \sum_{n_1,n_2 \geq 2}\Lambda(n_1)\Lambda(n_2)\,
g(n_1n_2)\,\varphi(n_1/n_2)
\;=\; \sum_{N \geq 4} g(N)\;(\Lambda\star_\varphi\Lambda)(N),$$
$$\text{where}\quad (\Lambda\star_\varphi\Lambda)(N)
:= \sum_{d \mid N}\Lambda(d)\,\Lambda(N/d)\,\varphi\!\left(\frac{d^2}{N}\right).$$
The support of $\Sigma_{\mathrm{I}}$ is the semigroup of **almost-primes**
$\{p_1^{k_1}p_2^{k_2}\}$ (integers with at most two distinct prime factors),
intersected with $\mathrm{supp}\,g$, and with the eccentricity
restriction $d^2/N \in \mathrm{supp}\,\varphi$.

**(II)–(IV) Finite-support terms (with $g$ and $\varphi$ exchanged):**
$$\Sigma_{\mathrm{II}} = \sum_{n_1,n_2}\frac{\Lambda(n_1)\Lambda(n_2)}{n_2}\,
g(n_1/n_2)\,\varphi(n_1n_2), \quad
\Sigma_{\mathrm{III}} = \sum_{n_1,n_2}\frac{\Lambda(n_1)\Lambda(n_2)}{n_1}\,
g(n_2/n_1)\,\varphi\!\bigl(\tfrac{1}{n_1n_2}\bigr),$$
$$\Sigma_{\mathrm{IV}} = \sum_{n_1,n_2}\frac{\Lambda(n_1)\Lambda(n_2)}{n_1n_2}\,
g\!\bigl(\tfrac{1}{n_1n_2}\bigr)\,\varphi(n_2/n_1).$$
In each, the variable $n_1n_2$ (or its inverse) is confined to the compact support of
$\varphi$ (resp. $g$): only finitely many pairs $(n_1,n_2)$ contribute, with explicit
cutoff bounds $n_1n_2 \leq \max(\mathrm{supp})$.

All coefficients are explicit arithmetic ones ($\Lambda$, rational weights);
**none requires positions of zeros**.

*Proof.* Direct substitution of the four evaluations of $h$ into the formula of
block (4) of §2.3. For (I): group by $N = n_1n_2$; the pair $(n_1,n_2)$ with
$n_1n_2 = N$ and $\Lambda(n_1)\Lambda(n_2) \neq 0$ runs over the divisors $d = n_1$ of $N$
that are prime powers with a prime-power cofactor, and $\Lambda(d)\Lambda(N/d) =
0$ otherwise, so the inner sum is exactly $\sum_{d\mid N}\Lambda(d)
\Lambda(N/d)\varphi(d^2/N)$ with $n_1/n_2 = d/(N/d) = d^2/N$. The almost-prime support:
$\Lambda(d)\Lambda(N/d) \neq 0$ requires $d = p_1^{k_1}$, $N/d = p_2^{k_2}$. Finiteness in
(II)–(IV): e.g. in (II), $\varphi(n_1n_2) \neq 0$ requires $n_1n_2 \in
\mathrm{supp}\,\varphi$ compact, and there are only finitely many integers $\geq 4$ in a compact set.
$\square$

### 4.3. Poles×primes blocks

**Proposition 4.3.** With $M_0(y) := \int_0^\infty g(t)\,\varphi(y^2/t)\,\tfrac{dt}{t}$ and
$M_1(y) := \tfrac1y\int_0^\infty g(t)\,\varphi(y^2/t)\,dt$ (explicit multiplicative
convolutions of $g$ and $\varphi$, smooth of compact support in $y$):
$$D{\otimes}P(h_{g,\varphi}) + P{\otimes}D(h_{g,\varphi})
= \sum_n \Lambda(n)\Bigl[c_0(n) + c_1(n) + n^{-1}c_0(1/n) + n^{-1}c_1(1/n)
+ (\text{symmetric})\Bigr],$$
where $c_0(y) = \hat h_1(0;y) = \int h(x_1,y)\tfrac{dx_1}{x_1}$ and $c_1(y) =
\hat h_1(1;y) = \int h(x_1,y)\,dx_1$ are computed in closed form: with $t = x_1y$,
$$c_0(y) = \int_0^\infty g(x_1y)\,\varphi(x_1/y)\,\frac{dx_1}{x_1}
= \int_0^\infty g(t)\,\varphi(t/y^2)\,\frac{dt}{t},
\qquad c_1(y) = \frac{1}{y}\int_0^\infty g(t)\,\varphi(t/y^2)\,dt.$$
(The $c_i$ and $M_i$ differ by $\varphi \mapsto \check\varphi(v) := \varphi(1/v)$;
both are multiplicative convolutions of test data.) Finite sum over $n$
(compact support at $y = n$ or $1/n$): **computable with no zeros**. $\square$

### 4.4. The mixed zeros×primes terms: reabsorption (the deciding point)

We state the risk precisely. In the semi-expanded presentation of the double
functional (applying the explicit formula ONLY in variable 2), one gets
$$\mathcal{W}_2(h) = \sum_{\rho_2}\,\mathcal{W}^{(1)}\bigl[x_1 \mapsto
\hat h_2'(x_1;\rho_2)\bigr]
\quad\leadsto\quad \text{terms } -\sum_{\rho_2}\sum_n \Lambda(n)\,
\bigl[\cdots(\rho_2, n)\cdots\bigr],$$
which mix a zero with a prime. For the thickened kernel, explicitly: the partial
Mellin transform in variable 2 is
$$\hat h_2'(x_1;s) := \int_0^\infty g(x_1x_2)\,\varphi(x_1/x_2)\,x_2^{s-1}\,dx_2
\;\overset{t = x_1x_2}{=}\; x_1^{-s}\int_0^\infty g(t)\,\varphi(x_1^2/t)\,t^{s-1}\,dt,$$
so the mixed zeros×primes term of that presentation is
$$-\sum_{\rho_2}\sum_n \Lambda(n)\Bigl[n^{-\rho_2}\,J_{\rho_2}(n)
+ n^{\rho_2-1}\,J_{\rho_2}(1/n)\Bigr], \qquad
J_s(y) := \int g(t)\,\varphi(y^2/t)\,t^{s-1}dt.$$
The powers $n^{-\rho_2}$ **do** involve positions of zeros: if this term were
irreducible, MW-7 would reappear exactly here.

**Theorem 4.4 (reabsorption of the mixed terms).** For every $h \in
C_c^\infty((\mathbb{R}_+^*)^2)$ — in particular for $h_{g,\varphi}$ — the mixed
terms of any semi-expanded presentation are reabsorbed: the sum over $\rho_2$
at fixed $n$ is, by the one-variable formula applied to the test function
$x_2 \mapsto h(n, x_2)$ (resp. $h(1/n, x_2)$), equal to
$$\sum_{\rho_2} n^{-\rho_2} J_{\rho_2}(n) = \sum_{\rho_2}\widehat{h(n,\cdot)}(\rho_2)
= (D - P - A)\bigl[h(n,\cdot)\bigr],$$
which is a purely arithmetic datum (Definition 1.3 applied to the slice). Summing over
$n$ with weights $\Lambda(n)$ recovers exactly the blocks $P{\otimes}D$,
$P{\otimes}P$, $P{\otimes}A$ of Theorem 2.4. Consequently:

**(1)** the mixed terms DO get reabsorbed — not on the spectral side, but on the
arithmetic one: they are the half-expanded presentation of
arithmetic×arithmetic blocks;

**(2)** the full functional $\mathcal{W}_2(h_{g,\varphi})$ is computable with no
positions of zeros (Theorem 2.4 + Theorem 4.2 + Proposition 4.3 + §4.1);

**(3)** no irreducible mixed term remains. **MW-7 does not reappear in the
thickened diagonal functional.**

*Proof.* The slice $x_2 \mapsto h(n,x_2)$ is in
$C_c^\infty(\mathbb{R}_+^*)$ for each fixed $n$ (restriction of a $C_c^\infty$
function of two variables to a coordinate line), and its Mellin transform is
$\widehat{h(n,\cdot)}(s) = n^{-s}J_s(n)$ by the above computation (with $y = n$). The
Theorem 1.4 applied to that slice gives the identity shown, term by term in $n$;
the sum over $n$ is finite (compact support). The identification with the blocks of
Theorem 2.4 is the iterated definition (Lemma 2.2). $\square$

### 4.5. Honest delimitation: where MW-7 would reappear

Theorem 4.4 is not a trick: it is the observation that the object $\mathcal{W}_2 =
\mathcal{W}\otimes\mathcal{W}$ inherits **two** presentations (spectral and arithmetic)
from each factor, and therefore has a fully arithmetic presentation. But there is a
neighboring, stronger statement that remains false/inaccessible, and it is worth
delimiting it so the verdict is not misread:

**Remark 4.5 (the "genuine" explicit formula of the double object does not exist as a
one-variable object).** The spectral side of Corollary 3.6 can be rewritten as a
sum over the sum variable alone:
$$\mathcal{W}_2(h_{g,\varphi}) = \frac12\sum_{\sigma \in S}
\hat g\bigl(\tfrac12+\sigma\bigr)\,w_\varphi(\sigma), \qquad
S := \Bigl\{\tfrac{z_1+z_2}{2}\Bigr\}, \quad
w_\varphi(\sigma) := \sum_{\substack{(z_1,z_2):\\ z_1+z_2 = 2\sigma}}
\hat\varphi\bigl(\tfrac{z_1-z_2}{2}\bigr).$$
A "genuine explicit formula" of the double object — analogous to that of an
L-function, with spectrum $S$ and multiplicities — would require knowing the
**multiplicity function** $w_\varphi(\sigma)$, which depends on the relative positions of
the zeros: this is where MW-7 would reappear (it is the quantitative version of the
OPEN GAP 3.8 of Doc 106: the Minkowski-sum object is not an L-function). **The point of
the experiment is that Lemma 5.2 does not need that statement**: it asks for a
functional $\mathcal{W}_2$ with (1) a tensor spectral block and (2) an autonomous
arithmetic side — and both exist without resolving $w_\varphi$. The multiplicity is not computed: it is
**transported** (the two presentations of Theorem 2.4 are equal as numbers, not
term by term).

**Explicit answers to (iii):**
(a) Computable without positions of zeros? **Yes** (Theorem 4.4(2)).
(b) Does it live in the almost-prime semigroup with explicit coefficients? **Yes**: the
dominant block is $\sum_N g(N)(\Lambda\star_\varphi\Lambda)(N)$, a weighted transform
of $\Lambda\star\Lambda$ — exactly the second term of Selberg's second-order
von Mangoldt function $\Lambda_2(N) = \Lambda(N)\log N + (\Lambda\star\Lambda)(N)$
[Sel49]. Precise difference from $\Lambda_2$: the diagonal functional weighs each
factorization $N = d\cdot(N/d)$ by $\varphi(d^2/N)$ (localization in the
*eccentricity* of the factorization), whereas $\Lambda_2$ sums with weight 1; the
$\Lambda(N)\log N$ term of $\Lambda_2$ (which detects pure prime powers) does not appear in
$\Sigma_{\mathrm{I}}$ — its analogue is the diagonal sector $n_1 = n_2$ ($\varphi$
evaluated at 1) already included in the sum. Note that $\Lambda_2 = \mu \star \log^2$
[Sel49]: like $\Lambda_2$, the almost-prime block is at finite convolution distance
from completely elementary functions.
(c) Mixed terms: **options (1)+(2) simultaneously** — they get reabsorbed on the
arithmetic side and the total is computable with no zeros (Theorem 4.4); option (3) (MW-7) remains
confined to the neighboring statement of Remark 4.5, which Lemma 5.2 does not require.

---

## 5. (iv) Quadratic-form structure: the tensor block of the quadruple

### 5.1. The diagonal quadratic form $Q_2$

**Definition 5.1.** On $C_c^\infty((\mathbb{R}_+^*)^2)$, with the multiplicative
convolution $(h_1\star h_2)(x) = \int_{(\mathbb{R}_+^*)^2} h_1(y)\,h_2(x/y)\,d^*y$
($d^*y = \frac{dy_1dy_2}{y_1y_2}$, componentwise quotients) and the involution
$\tilde h(x_1,x_2) := \overline{h(1/x_1,1/x_2)}\,(x_1x_2)^{-1}$:
$$Q_2(h_1,h_2) := \mathcal{W}_2(h_1 \star \tilde h_2).$$
This is the exact analogue of $Q(f,g) = \mathcal{W}(f\star\tilde g)$ from P35 (Def. weil).

**Lemma 5.2 (closure of the thickened class and spectral side of $Q_2$).**

(a) In coordinates $(u,v) = \Phi(x_1,x_2)$ of Lemma 3.3, the thickened kernels are
exactly the product functions $g(u)\varphi(v)$; since $\Phi$ is a group
isomorphism, the thickened class is closed under $\star$ and under
$\widetilde{(\cdot)}$:
$$h_{g_1,\varphi_1} \star h_{g_2,\varphi_2} = \tfrac12\, h_{\,g_1\star g_2,\;
\varphi_1\star\varphi_2}, \qquad
\widetilde{h_{g,\varphi}} = h_{\,\tilde g,\;\varphi^\vee}, \quad
\varphi^\vee(v) := \overline{\varphi(1/v)},$$
(the weight $u^{-1} = (x_1x_2)^{-1}$ of the involution falls entirely on the factor $g$;
$\widehat{\varphi^\vee}(\tau) = \overline{\hat\varphi(-\bar\tau)}$).

(b) Mellin transform of the double involution: $\widehat{\tilde h}(s_1,s_2) =
\overline{\hat h(1-\bar s_1,\,1-\bar s_2)}$. Consequently, the spectral side of the
form is
$$Q_2(h,h) = \sum_{\rho_1,\rho_2} \hat h(\rho_1,\rho_2)\;
\overline{\hat h\bigl(1-\bar\rho_1,\,1-\bar\rho_2\bigr)},$$
an absolutely convergent sum, hermitian because the set of zeros is stable under
$\rho \mapsto 1-\bar\rho$ (functional equation + Schwarz reflection).

*Proof.* (a) Direct computation: $u(1/x_1,1/x_2) = 1/u$, $v(1/x_1,1/x_2) = 1/v$ and
$(x_1x_2)^{-1} = u^{-1}$, hence $\tilde h$ corresponds to
$\overline{g(1/u)}u^{-1}\cdot\overline{\varphi(1/v)} = \tilde g(u)\varphi^\vee(v)$. The
factor $\tfrac12$ of the convolution is the Haar pushforward of Lemma 3.3. (b) With
$y_i = 1/x_i$: $x_i^{s_i-1}dx_i = y_i^{-s_i}\,dy_i\cdot y_i^{\,0}$ after
$dx_i = dy_i/y_i^2$, gives $\widehat{\tilde h}(s) = \overline{\int h(y)\,
y_1^{-\bar s_1}y_2^{-\bar s_2}\,dy} = \overline{\hat h(1-\bar s_1, 1-\bar s_2)}$.
Then $\widehat{h\star\tilde h} = \hat h\cdot\widehat{\tilde h}$ and Lemma 2.2(b)
applies. Consistency with (a): $\sigma(1-\bar s_1, 1-\bar s_2) = 1 - \bar\sigma$,
$\tau \mapsto -\bar\tau$, which is exactly $(\widehat{\tilde g},
\widehat{\varphi^\vee})$. $\square$

**Remark 5.3 (positivity under RH and the two sides).** If all zeros satisfy
$\rho = 1-\bar\rho$ (RH), the pairing of Lemma 5.2(b) is diagonal and
$Q_2(h,h) = \sum |\hat h(\rho_1,\rho_2)|^2 \geq 0$. The functional $Q_2(h,h)$ also has
an arithmetic presentation (Theorem 2.4 applied to $h\star\tilde h$, which remains in
the thickened class by (a)): the equality of both presentations is the
quadratic version of the dictionary of §4.

### 5.2. The toy model: the 16 pairs of the quadruple

Now take the Doc 98 configuration: off-critical zeros exactly
$\{1/2\pm\delta\pm i\gamma_0\}$, simple; in the parameter $z = \rho-\tfrac12$:
$$z_1 = \delta+i\gamma_0,\quad \bar z_1 = \delta-i\gamma_0,\quad
z_2 = -\delta+i\gamma_0,\quad \bar z_2 = -\delta-i\gamma_0.$$
The 16 spectral vectors of the double off×off block are $v_{ij} := v_{z_i}\otimes
v_{z_j}$, functionals $h \mapsto \hat h(\rho_i,\rho_j)$. On the thickened class,
$\hat h(\rho_i,\rho_j) = \tfrac12\,\hat g(\tfrac12+\sigma_{ij})\,
\hat\varphi(\tau_{ij})$ with $\sigma_{ij} = \tfrac{z_i+z_j}{2}$,
$\tau_{ij} = \tfrac{z_i-z_j}{2}$.

**Full enumeration (task (iv)).** The values $(\sigma,\tau)$ of the 16 ordered
pairs — equivalently $\rho_i+\rho_j-1 = 2\sigma$, which runs over
$\{\pm2\delta\pm2i\gamma_0,\ \pm2\delta,\ \pm2i\gamma_0,\ 0\}$ as the statement required:

| # | pair $(z_i,z_j)$ | $\sigma = \frac{z_i+z_j}{2}$ | $\tau = \frac{z_i-z_j}{2}$ | sum type |
|---|---|---|---|---|
| 1 | $(z_1,z_1)$ | $\delta+i\gamma_0$ | $0$ | full off |
| 2 | $(\bar z_1,\bar z_1)$ | $\delta-i\gamma_0$ | $0$ | full off |
| 3 | $(z_2,z_2)$ | $-\delta+i\gamma_0$ | $0$ | full off |
| 4 | $(\bar z_2,\bar z_2)$ | $-\delta-i\gamma_0$ | $0$ | full off |
| 5 | $(z_1,\bar z_1)$ | $\delta$ | $i\gamma_0$ | **real** $+2\delta$ |
| 6 | $(\bar z_1,z_1)$ | $\delta$ | $-i\gamma_0$ | **real** $+2\delta$ |
| 7 | $(z_2,\bar z_2)$ | $-\delta$ | $i\gamma_0$ | **real** $-2\delta$ |
| 8 | $(\bar z_2,z_2)$ | $-\delta$ | $-i\gamma_0$ | **real** $-2\delta$ |
| 9 | $(z_1,z_2)$ | $i\gamma_0$ | $\delta$ | imaginary |
| 10 | $(z_2,z_1)$ | $i\gamma_0$ | $-\delta$ | imaginary |
| 11 | $(\bar z_1,\bar z_2)$ | $-i\gamma_0$ | $\delta$ | imaginary |
| 12 | $(\bar z_2,\bar z_1)$ | $-i\gamma_0$ | $-\delta$ | imaginary |
| 13 | $(z_1,\bar z_2)$ | $0$ | $z_1$ | null |
| 14 | $(\bar z_2,z_1)$ | $0$ | $-z_1$ | null |
| 15 | $(\bar z_1,z_2)$ | $0$ | $\bar z_1$ | null |
| 16 | $(z_2,\bar z_1)$ | $0$ | $-\bar z_1$ | null |

The map $(z_i,z_j) \mapsto (\sigma,\tau)$ is a bijective linear map: the 16 points
$(\sigma_{ij},\tau_{ij}) \in \mathbb{C}^2$ are **distinct** (although the $\sigma$'s alone
repeat: $\sigma = 0$ four times, $\sigma = \pm\delta, \pm i\gamma_0$ twice
each — the degeneracy that $\hat\varphi$ resolves).

**What $\hat g$ sees in each class (the statement's question):** on the full-off
sums, points genuinely off the double axis ($\mathrm{Re}\,\sigma = \pm\delta$,
$\mathrm{Im}\,\sigma = \pm\gamma_0$); on the **real** sums $\pm2\delta$, the points
$\tfrac12 \pm \delta$ **on the real axis** — the direct detector of the
shift $\delta$, with no frequency; on the imaginary and null sums, points **on the
double critical axis** $\tfrac12 \pm i\gamma_0$ and $\tfrac12$: for $\hat g$ they are
indistinguishable from sums of on-line zeros — there, off-criticality is invisible to
$\hat g$ and only $\hat\varphi(\tau)$ with $\mathrm{Re}\,\tau \neq 0$ registers it
(rows 9–16: $\tau \in \{\pm\delta, \pm z_1, \pm\bar z_1\}$, all with real part
$\pm\delta \neq 0$).

### 5.3. The Gram matrix of the block: 8 hyperbolic planes

**Lemma 5.4 (independence of the 16 evaluations on the thickened class).** The 16
functionals $h_{g,\varphi} \mapsto \hat g(\tfrac12+\sigma_{ij})\,
\hat\varphi(\tau_{ij})$ are linearly independent over the span (finite linear
combinations) of thickened kernels; equivalently, the evaluation map
$\mathrm{ev}: \mathrm{span}\{h_{g,\varphi}\} \to \mathbb{C}^{16}$,
$h \mapsto (\hat h(\rho_i,\rho_j))_{ij}$, is **surjective**.

*Proof.* Suppose $\sum_{ij} c_{ij}\,\hat g(\tfrac12+\sigma_{ij})
\hat\varphi(\tau_{ij}) = 0$ for all $g,\varphi \in C_c^\infty(\mathbb{R}_+^*)$.
Step 1 (separate by $\sigma$): take $g = g_{c,\epsilon}$ a smooth approximation of the
multiplicative delta at $x = e^c$; then $\hat g(\tfrac12+\sigma) \to
e^{c(\sigma-1/2)}\cdot e^{c}\,(1+o(1))$ — more precisely, $\hat g_{c,\epsilon}
(\tfrac12+\sigma) = e^{c(\sigma+1/2)}(1+O_\sigma(\epsilon))$ — so the condition
implies, for all $c \in \mathbb{R}$ and all $\varphi$:
$\sum_{\sigma \in \Sigma} e^{c\sigma}\,\bigl[\sum_{ij:\,\sigma_{ij}=\sigma}
c_{ij}\hat\varphi(\tau_{ij})\bigr] = 0$, where $\Sigma$ is the set of the 9 distinct
values of $\sigma$. The functions $c \mapsto e^{c\sigma}$ with distinct $\sigma$ are
linearly independent over $\mathbb{R}$ (independence of Artin characters, or
Vandermonde Wronskian), so each bracket vanishes. Step 2 (separate by $\tau$
within each group): within each value of $\sigma$, the $\tau_{ij}$ are distinct
(table §5.2), and the same argument with $\hat\varphi$ and approximate deltas at $e^{d}$ gives
$c_{ij} = 0$. Surjectivity of $\mathrm{ev}$ is the dual statement in finite
dimension. $\square$

**Theorem 5.5 (signature of the double block of the quadruple: $(8,8)$).** Let $B$ be the
hermitian form induced by $Q_2$ on $\mathbb{C}^{16} = \mathrm{ev}(\mathrm{span}\,
\{h_{g,\varphi}\})$ via the contribution of the off×off block on the spectral side
(Lemma 5.2(b)), i.e. for $a = (a_{ij}) = \mathrm{ev}(h)$:
$$B(a,a) = \sum_{i,j} a_{ij}\,\overline{a_{i^*j^*}}, \qquad
\text{where } z_{i^*} := -\bar z_i \;\;(\text{i.e. } \rho_{i^*} = 1-\bar\rho_i).$$
Then:

(a) The involution $(i,j) \mapsto (i^*,j^*)$ is **fixed-point-free** on the 16
pairs (a fixed point would require $z_i, z_j \in i\mathbb{R}$, impossible with
$\mathrm{Re}\,z = \pm\delta \neq 0$), and pairs them into exactly **8 orbits**:
$$\{1,3\},\;\{2,4\},\;\{5,7\},\;\{6,8\},\;\{9,10\},\;\{11,12\},\;\{13,16\},\;
\{14,15\}$$
(table §5.2 numbering; verified with $z_1^* = z_2$, $\bar z_1^{\,*} =
\bar z_2$ and vice versa).

(b) On each orbit $\{(ij),(i^*j^*)\}$, $B$ restricts to the hyperbolic plane
$a\,\bar b + b\,\bar a$: signature $(1,1)$.

(c) Hence
$$\boxed{\;\mathrm{sig}(B) = (8,8), \qquad \mathrm{neg.ind}(B) = 8
= \frac{(4m)^2}{2}\Big|_{m=1},\;}$$
**exactly the prediction of Proposition 3.5 of Doc 106** for
$(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ with $\mathrm{sig}(2,2)^{\otimes 2}
= (2\cdot2+2\cdot2,\;2\cdot2+2\cdot2)$.

(d) The weight $\hat\varphi$ **neither breaks nor degenerates** the signature: by
Lemma 5.4 the evaluation map is surjective, so $B$ is realized with its full rank 16 on
the thickened class. Moreover, $\hat\varphi$ is **necessary** for non-degeneracy:
the orbits $\{9,10\}$, $\{11,12\}$, $\{13,16\}$, $\{14,15\}$ live inside
degenerate eigenspaces of the sum variable ($\sigma$ identical for both members, or
$\sigma = 0$ shared by four vectors); a functional that only saw $\hat g$
(forgetting $\varphi$) would collapse those directions and lose 4 of the 8 negatives.

*Proof.* (a) Direct computation from the table: e.g. $(z_1,z_1)^* = (z_2,z_2)$
(orbit $\{1,3\}$); $(z_1,\bar z_1)^* = (-\bar z_1, -z_1)\,\hat=\,(z_2,\bar z_2)$
(orbit $\{5,7\}$, since $-\bar z_1 = z_2$ and $-z_1 = \bar z_2$); $(z_1,z_2)^* =
(z_2,z_1)$ (orbit $\{9,10\}$); $(z_1,\bar z_2)^* = (z_2,\bar z_1)$ (orbit
$\{13,16\}$); $(\bar z_2, z_1)^* = (\bar z_1, z_2)$ (orbit $\{14,15\}$); the rest
by conjugation. Fixed point: $(i^*,j^*) = (i,j)$ requires $z_i = -\bar z_i$, i.e.
$\mathrm{Re}\,z_i = 0$: excluded. (b) In the orbit's basis, $B = \bigl(
\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\bigr)$ (the weights are 1: simple zeros,
multiplicity 1 in the spectral sum), eigenvalues $\pm1$. (c) Orthogonal sum of 8
$(1,1)$ planes. (d) Lemma 5.4 and the table. $\square$

**Corollary 5.6 (localization of the negative index — answer to the central question of
(iv)).** The distribution of the 8 negatives by sum type $\rho_i+\rho_j-1 =
2\sigma$:

| sum type | orbits | negatives |
|---|---|---|
| full off ($\pm2\delta\pm2i\gamma_0$) | $\{1,3\},\{2,4\}$ | $2$ |
| **real** ($\pm2\delta$) | $\{5,7\},\{6,8\}$ | $2$ |
| imaginary ($\pm2i\gamma_0$) | $\{9,10\},\{11,12\}$ | $2$ |
| null ($0$) | $\{13,16\},\{14,15\}$ | $2$ |

**The statement's conjecture ("the contributions with $\rho_i+\rho_j-1 = \pm2\delta$
carry the negative index") is instructively FALSE**: the real sums
carry only $2$ of the $8$ negatives. Half the negative index ($4$) lives in
**purely imaginary or null** sums — that is, $\hat g$ sees them on the double
critical axis, indistinguishable from on-line pairs, and off-criticality is stored
exclusively in the difference variable $\tau$ with $\mathrm{Re}\,\tau = \pm\delta$,
visible only to $\hat\varphi$. Structural lesson: **in the double object, the
transverse variable $\varphi$ is not a mere thickening regularizer — it carries
half the index**. Any attempt to collapse $\varphi$ (e.g. taking
$\hat\varphi \to 1$, un-thickening) not only diverges (Lemma 3.1): it loses half the
negative spectral signal.

**Remark 5.7 (declared caveats of Theorem 5.5).** (i) The statement concerns the
form $B$ induced by the **off×off block of the spectral side** of $Q_2$ on the
evaluation quotient — the doubled analogue of the localization
$\mathcal{K} = \mathcal{K}_{\mathrm{crit}}\oplus_Q\mathcal{K}_{\mathrm{off}}$ (Doc 96,
Theorem 8.1) is not re-proved here for the double object; the separation of the block
from the rest of the double spectrum uses the same spectral-projection argument of
$H^{(2)}$ and remains inherited structure modulo doubled V.1 (same status as in
Doc 98 §6, GAPs G4/G5 declared there). (ii) The weights of the planes are 1 for
simple zeros (toy hypothesis T1); with multiplicities, the weights are
$m_{\rho_i}m_{\rho_j} > 0$ and the signature does not change. (iii) The identification of $B$
with the Gram matrix of $(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ uses the
pairing convention $z \leftrightarrow -\bar z$ ($\rho \leftrightarrow
1-\bar\rho$), which is the one the involution $\tilde h$ of Definition 5.1 produces; Doc 98
(Rem. 6.2) already recorded that both conventions give two hyperbolic planes per
quadruple in one variable — here the convention is **fixed by the computation of
Lemma 5.2(b)**, which in turn answers GAP G5 of Doc 98 for the double form: the
natural involution of $Q_2$ pairs $\rho \leftrightarrow 1-\bar\rho$.

---

## 6. (v) Balance against Missing Lemmas 5.2 and 5.3 of Doc 106

### 6.1. Lemma 5.2, condition 1 (tensor spectral block): SATISFIED

The candidate is
$$X_2 := \Bigl(\,\mathcal{W}_2\ \text{restricted to the thickened class}\
\{h_{g,\varphi}\},\ \ Q_2(h,h') = \mathcal{W}_2(h\star\tilde h')\,\Bigr).$$
By Corollary 3.6 and Proposition 3.7, its spectral side is indexed by the
eigenvalues $z_1+z_2$ of $H_C\otimes I + I\otimes H_C$; by Theorem 5.5, in the
toy model the off×off block is exactly
$(Q|_{\mathcal{K}_{\mathrm{off}}})^{\otimes 2}$ with signature $(8,8)$ and no
degeneracy. Condition 1 of Missing Lemma 5.2 is verified (modulo the structural
inheritance declared in Rem. 5.7(i)).

### 6.2. Lemma 5.2, condition 2 (autonomous arithmetic side): SATISFIED

By Theorem 4.4: $\mathcal{W}_2(h_{g,\varphi})$ — and by Lemma 5.2(a) also
$Q_2(h,h)$, since $h\star\tilde h$ remains thickened — has a fully
arithmetic presentation: poles (§4.1), almost-primes with coefficients
$\Lambda(d)\Lambda(N/d)\varphi(d^2/N)$ (Theorem 4.2), pole-prime convolutions
(Prop. 4.3), and explicit archimedean terms. No positions of zeros. **Missing
Lemma 5.2 has a candidate.** This was the binary result that Problem 5.4 asked for.

### 6.3. The structural warning: the index of the full double object is infinite

Before declaring partial victory, what the candidate does NOT give. The thickened
class, via $\Phi$, is dense in $C_c^\infty((\mathbb{R}_+^*)^2)$ (sums
$\sum g_\alpha(u)\varphi_\alpha(v)$ approximate any two-variable test function in
the Schwartz topology on compact sets). Hence $Q_2$ is the form $Q\otimes Q$ on (a
dense subset of) the full $\mathcal{K}\otimes\mathcal{K}$, and Proposition 3.4 of
Doc 106 applies:

**Proposition 6.1 (the global index of $Q_2$ is $0$ or $\infty$).** Under RH,
$Q_2 \geq 0$ (Rem. 5.3). Under ¬RH (toy), $\kappa(Q_2) = \infty$: the mixed
off×on pairs $(\rho_{\mathrm{off}}, \tfrac12+i\gamma_j)$, $j \geq 1$, form, for each
on-line zero, a family of 4 spectral vectors with the same fixed-point-free
involution in the first component ($(z_i, i\gamma_j)^* = (z_{i^*}, i\gamma_j)$), i.e. 2
hyperbolic planes per $\gamma_j$: infinitely many negatives.

*Proof.* Identical to Theorem 5.5(a)(b) with $z_j = i\gamma_j$ fixed in the second
slot: the involution acts only on the first, with no fixed points because
$\mathrm{Re}\,z_i = \pm\delta \neq 0$; each orbit $\{(z_i,i\gamma_j),
(z_{i^*},i\gamma_j)\}$ is a hyperbolic plane. Independence of the evaluations
for any finite subfamily is Lemma 5.4 (the points $(\sigma,\tau)$ remain
distinct). $\square$

**Consequence.** The invariant useful for amplification is NOT the global
$\kappa(Q_2)$ (which is $0/\infty$, binary) but the **index of the relative off×off
block** — finite, equal to $8 = (4m)^2/2$ — exactly the regularization (R2) of Doc 106 §3.1.3. This
is consistent with the design of Candidate 2 (relative tensor), but means that the
Lemma 5.3 (bound) must bound the index **of the block**, and the arithmetic side is a
global functional that does not come pre-localized. The gap between "computable global
arithmetic functional" and "index bound of a spectral block" is where all the
difficulty now lives.

### 6.4. Lemma 5.3: is there a non-spectral finiteness source on the almost-prime side?

This is the question of the analogue of Deligne's rationality. Three remarks, in
order of increasing frankness.

**(α) For the first time, a candidate second source exists that passes I2a.** The
almost-prime side $\sum_N g(N)(\Lambda\star_\varphi\Lambda)(N)$ admits
**unconditional sieve upper bounds**: for the model problem (correlations
$\sum_{n\leq x}\Lambda(n)\Lambda(n+h)$, and likewise for short weighted sums of
$\Lambda\star\Lambda$) the Selberg method gives upper bounds of the correct order of
magnitude with an absolute constant [HR74, Ch. 3; the value of the constant is not
load-bearing here]. The sieve parity problem — the Arc A wall — blocks the
**asymptotics** and non-trivial **lower bounds**, but NOT upper bounds. And what
the Deligne skeleton needs (Doc 106, Theorem 1.4(b)) is a BOUND, not an
asymptotic. This is the first time in the program that an unconditional input appears,
independent of the zeros, on the correct side of the inequality, that is not a CAP
positivity: a sieve bound is a majorized count, not a non-negative quadratic
form. The Doc 99 transmutation pattern does not apply automatically.

**(β) The real gap: the sieve→index bridge.** An upper bound
$|P{\otimes}P(h\star\tilde h)| \leq C(\mathrm{supp})\cdot\|\cdot\|$ of the
almost-prime block does NOT by itself bound $\mathrm{neg.ind}$ of a spectral block: the
negative index is a rank/inertia property, not a size property. The mechanism that
converts bounds on the arithmetic side into index bounds exists in the corpus — it is
condition C5 of Doc 94 (the positivity defect is concentrated in a controlled
finite "head") — but its instance for $Q_2$ is not proved. What exactly is missing
is stated as Lemma 7.2 below.

**(γ) The transmutation risk, localized.** If the bridge (β) required not a bound
but the **asymptotic** of the almost-prime functional uniform in $(g,\varphi)$ — e.g. to
separate the off×off block from the on×on tail within the global functional —, then the
required input is exactly the asymptotic of correlations of
$\Lambda\star\Lambda$, which by the Montgomery / Goldston–Montgomery dictionary
[Mon73; GM87] is inter-derivable with the pair correlation of the zeros and of
Hardy–Littlewood type strength (generalized twin primes). Note precisely which wall that
is: **it is not CAP** (it is not an RH-equivalent positivity; pair correlation does
not imply RH nor vice versa), **it is the parity/almost-prime-asymptotic wall** — the
same one that blocked Arc A, but now attacked from the opposite side: Arc A needed
to distinguish $\omega(n) \bmod 2$ (signed asymptotic); here at most one would need
to majorize an almost-prime bilinear functional. The majorize/asymptotize distinction is
exactly the boundary between what sieves give and what parity forbids. The
experiment leaves the difficulty on the good side of that boundary **if and only if**
bridge (β) can be closed with one-sided bounds; if not, it transmutes to parity
(Doc 99 pattern, with a destination different from CAP — new data in itself).

### 6.5. Budget for powers $k \geq 3$ (sketch, no proof claimed)

The same computation iterates: the $k$-thickened kernel $h = g(x_1\cdots x_k)\,
\Phi(\vec v)$, with $\vec v$ the $k-1$ transverse coordinates ($\Phi \in
C_c^\infty((\mathbb{R}_+^*)^{k-1})$), gives, by the group isomorphism analogous to
Lemma 3.3:
$$\hat h(s_1,\dots,s_k) = \frac{1}{k}\;\hat g\!\left(\frac{s_1+\cdots+s_k}{k}\right)
\widehat\Phi(\text{combinations of differences}),$$
zero term $\frac1k\sum_{\rho_1..\rho_k}\hat g(\frac{\sum\rho_i}{k})
\widehat\Phi(\cdots)$ — the spectrum of $\sum_i H_C^{(i)}$ —, and arithmetic side
supported on $k$-almost-primes $p_1^{a_1}\cdots p_k^{a_k}$ with
$\Lambda^{\star k}$-weighted coefficients, plus mixed finite-support blocks. The reabsorption of
mixed terms (Theorem 4.4) iterates slot by slot. The budget of the final
contradiction would be: index of the block $(4m)^k/2$ (Doc 106, Prop. 3.5) against a sieve
bound of the $k$-almost-prime side; sieve upper bounds for order-$k$ correlations
typically grow like $C^k$ (geometric constants in $k$ [HR74]). The comparison
$C^k$ vs $(4m)^k/2$ requires $C < 4m$ with $m$ unknown: for the contradiction to
kill all $m \geq 1$ one needs $C < 4$. **Nothing is asserted here**: neither that
bridge (β) exists, nor the value of $C$; it is recorded that the budget is geometric
against geometric — the precise quantitative form remains inside Lemma 7.2. (Reminder of
Doc 106 §5.2: by the exponential strength of (a), a subexponential $f(k)$ suffices; that
relaxes $C < 4$ to any $C$ if the sieve bound were $C^{o(k)}\cdot$polynomial, which is
also not asserted.)

---

## 7. The next lemma

### 7.1. What this document leaves proved

**Theorem 7.1 (executable summary).** Unconditionally (without RH, without Hypothesis D for
(i)–(iii); with the toy configuration for (iv)):

(i) $\mathcal{W}_2 = \mathcal{W}\otimes\mathcal{W}$ is well defined on
$C_c^\infty((\mathbb{R}_+^*)^2)$ with a double spectral/arithmetic presentation
(Theorem 2.4).

(ii) On the thickened kernel, the spectral side is the Minkowski sum of spectra
with transverse weight: $\tfrac12\sum\hat g(\tfrac{\rho_1+\rho_2}{2})
\hat\varphi(\tfrac{\rho_1-\rho_2}{2})$ (Theorem 3.4, Corollary 3.6).

(iii) The arithmetic side is autonomous: $\varphi$-weighted transform of
$\Lambda\star\Lambda$ over almost-primes + finite-support blocks + poles +
archimedean; the mixed zeros×primes terms get reabsorbed (Theorems 4.2, 4.4).

(iv) In the toy model, the off×off block of $Q_2$ has signature $(8,8)$, confirming
Prop. 3.5 of Doc 106, with the weight $\hat\varphi$ as the necessary carrier of half
the index (Theorem 5.5, Corollary 5.6); the global index of $Q_2$ is $\infty$ under
¬RH (Prop. 6.1).

### 7.2. The exact statement that is missing

**Missing Lemma 7.2 (sieve→index bridge; the new incarnation of Lemma 5.3).** *Prove
that there exists a function $f$ with $f(2) < \infty$ coming only from arithmetic
data (sieve bounds of the almost-prime block, poles, archimedean term — with no
positions of zeros) such that the positivity defect of $Q_2$ on the thickened class is of
rank bounded by $f(2)$: there exists a subspace $\mathcal{H}_2 \subseteq
\mathrm{span}\{h_{g,\varphi}\}$ of codimension $\leq f(2)$ with
$Q_2|_{\mathcal{H}_2} \geq -\varepsilon$-small in the C5 sense of Doc 94 — or, in the
block version: the negative index of every spectral block of $Q_2$ associated with
a compact window of the sum variable is bounded by $f(2)$ uniformly in the
window. And its extension to $k$: $f(k)$ subexponential in $k$ from the same source.*

Two ways to die and one to live, for Lemma 7.2: (death 1) if every proof of
the bound requires the uniform almost-prime asymptotic, it transmutes to parity/pair
correlation (§6.4(γ)) — Doc 99 pattern with a new wall; (death 2) if it requires positivity of
the critical block of the double object, it transmutes to CAP — classic Doc 99
pattern; (life) if one-sided sieve upper bounds suffice for C5-type rank
control — the only scenario in which the Deligne skeleton closes. The I2a discriminator must
be applied to each attempt.

**Remark 7.3 (why Prop. 6.1 does not kill the candidate).** That
$\kappa(Q_2) = \infty$ under ¬RH is not the death mode of Prop. 3.4 of Doc 106
(invariant collapse): the amplification datum of Form B uses the index of the
**relative block** (tensor on $\mathcal{K}_{\mathrm{off}}$, regularization R2 already
adopted), and this document shows that that block is **realized within a
functional with an autonomous arithmetic side** — which was what was missing. The global
infinity is the reason Lemma 7.2 asks for a bound *by block/by window*, not global.

---

## 8. VERDICT

**VERDICT: LIVE CANDIDATE.**

**Precise reason.** The experiment of Problem 5.4 had two outcomes: "if the
arithmetic side of the diagonal functional turns out expressible in almost-primes with
computable coefficients, Lemma 5.2 has a candidate; if it requires the positions of the zeros,
MW-7 reappears and Candidate 2 dies". The former happened, with proof:

1. **The mixed zeros×primes terms — the designated reappearance point of MW-7 — get
   reabsorbed** (Theorem 4.4): they are artifacts of the semi-expanded presentation, and the
   full functional $\mathcal{W}_2(h_{g,\varphi})$ is computable with no positions of
   zeros. MW-7 remains confined to the neighboring statement (*genuine* one-variable explicit
   formula for the sum object, Rem. 4.5), which Lemma 5.2 does not need.

2. **The almost-prime side is autonomous and structured** (Theorem 4.2): a
   $\varphi$-weighted transform of $\Lambda\star\Lambda$ — the exact relative of Selberg's
   almost-prime term in $\Lambda_2$ — plus finite-support blocks.

3. **The tensor signature $(8,8)$ survives the thickened diagonal restriction**
   (Theorem 5.5): 8 hyperbolic planes, no degeneracy, confirming Prop. 3.5
   of Doc 106 in its first analytic realization. Unanticipated finding: half
   the negative index lives in purely imaginary sums and is carried by the
   transverse weight $\hat\varphi$ (Corollary 5.6) — the conjecture "the negatives are in the
   real sums $\pm2\delta$" is false.

**Honest qualification of "LIVE".** Live means: Missing Lemma 5.2 of Doc 106
went from a named gap to a **candidate with explicit construction and verification in
the toy model**. It does not mean Form B is close to closing: all the weight is now on
Missing Lemma 7.2 (sieve→index bridge, heir of 5.3), with its two documented
transmutation modes (parity, CAP) and a precise life scenario (one-sided sieve
bounds ⇒ C5 rank control). The real strategic novelty of this
document: for the first time in the program, the candidate source of finiteness is an
unconditional, non-spectral, non-CAP input (sieve upper bounds on the
almost-prime semigroup), and the identified potential wall (parity/asymptotic) is
**different** from CAP — the program gains a second independent front instead of
re-encountering the same wall under another name.

**Next step:** Lemma 7.2, starting with its single-window case in the toy model:
does the sieve bound of $\sum_N g(N)(\Lambda\star_\varphi\Lambda)(N)$ bound the
negative index of the $Q_2$ block in a compact window of $\sigma$ containing
$\{\pm\delta, \pm i\gamma_0, 0, \pm\delta\pm i\gamma_0\}$?

---

## References

**Internal (backward-only):** Doc 106 (Prop. 3.5: $\mathrm{neg.ind}(Q_1\otimes Q_2) =
p_1q_2+q_1p_2$, $\kappa(\psi^{\otimes k}) = (4m)^k/2$; Prop. 3.4: collapse to
$\kappa=\infty$; Missing Lemmas 5.2/5.3; Problem 5.4); Doc 98 (toy model,
Prop. 6.1: two hyperbolic planes, $\kappa=2$; Rem. 6.2: pairing conventions;
Rem. 6.3: residual generators); Doc 96 (Theorem 8.1: localization
$\mathcal{K}_{\mathrm{off}}$; Prop. 4.10: eigenvalues $\rho-1/2$ of $H_C$); Doc 94
(condition C5: positivity defect concentrated in a finite head); Doc 99 (transmutation
pattern; discriminator I2a); P35 (Def. weil: $\mathcal{W}$, $Q(f,g) =
\mathcal{W}(f\star\tilde g)$, Hypothesis D, $\kappa = 2m$); P41 §7 (Form B).

**Verified literature:**
- A. Weil, *Sur les "formules explicites" de la théorie des nombres premiers*, Comm.
  Sém. Math. Univ. Lund (1952), 252–265. (Explicit formula and positivity criterion.)
- E. Bombieri, *Remarks on Weil's quadratic functional in the theory of prime numbers I*,
  Rend. Mat. Acc. Lincei (9) **11** (2000), 183–233. (Equivalent forms of the
  archimedean term; Weil's quadratic functional.)
- H. Iwaniec, E. Kowalski, *Analytic Number Theory*, AMS Colloq. Publ. 53, 2004,
  Ch. 5 (Thm. 5.12: general explicit formula; Thm. 5.8: $N(T)$).
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, in Analytic
  Number Theory, Proc. Sympos. Pure Math. **24**, AMS (1973), 181–193. [Mon73]
- D. A. Goldston, H. L. Montgomery, *Pair correlation of zeros and primes in short
  intervals*, in Analytic Number Theory and Diophantine Problems, Birkhäuser Progr.
  Math. **70** (1987), 183–203. [GM87] (Equivalence of pair correlation ↔ variance of
  primes in short intervals; the double-zeros/almost-primes dictionary.)
- A. Selberg, *An elementary proof of the prime-number theorem*, Ann. of Math. (2)
  **50** (1949), 305–313. [Sel49] ($\Lambda_2(n) = \Lambda(n)\log n +
  \sum_{d\mid n}\Lambda(d)\Lambda(n/d) = \sum_{d\mid n}\mu(d)\log^2(n/d)$.)
- H. Halberstam, H.-E. Richert, *Sieve Methods*, Academic Press, 1974. [HR74] (Sieve
  upper bounds for correlations of $\Lambda$; absolute constants. The exact value
  of the constants cited in §6.5: [NOT VERIFIED in detail; not load-bearing
  — no result of this document depends on it].)

*End of Doc 107.*
