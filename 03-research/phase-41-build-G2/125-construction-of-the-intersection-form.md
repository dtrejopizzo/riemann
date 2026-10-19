# Doc 125 — Construction of the intersection form on the square of the scaling site

**Program:** Riemann Hypothesis — Phase 41: BUILD G2.
**Prerequisites:** Doc 80 (arithmetic Castelnuovo–Severi: why the Jacobi trace and Markov–Stieltjes do not give the form; the semidefinite form $Q$ does not distinguish measures); Doc 119 (R-SIG realizations (i)/(ii)/(iii); R-LEF; R-WEIGHT; the R-NC test, clauses NC1–NC4); Doc 123 (C-cok/C-rank bifurcation; the toy model $C_p\times C_p$; null elements; C-rank = the missing intersection norm/number = G2); Doc 124 (G2 = Hodge index on the square, INDEFINITE signature $(1,\rho-1)$; CC's positivity is DEFINITE, a different category; the ingredient does not exist in the CC corpus).

**Labeling discipline (absolute rule, maximum false-victory risk):** every statement carries **[DATA]** (in source/proved, with exact citation), **[CONSTRUCTION]** (an object I design — with its status: what it assumes, what remains to be verified), **[CALCULATION]** (my own derivation, shown step by step), **[GAP]**, **[CONJECTURE]**, **[UNVERIFIED]**. NEVER "proved" except for what is genuinely proved. The goal is NOT to declare G2 constructed — it is to build everything buildable, compute the toy model frankly, and isolate the core. **If the construction gets stuck, the point of obstruction IS the result.**

---

## 0. Executive summary

This document attempts to construct $G_2$, the intersection form on the square $X\times X$ of the scaling site, following exactly Weil's template (Hodge index on $C\times C$ gives RH for curves). The method: fix the classical mechanism with surgical precision (§1), define the tropical square and its distinguished classes (§2), propose and compare three routes for the intersection number (§3), compute the standard intersection relations (§4), and —the central deliverable— **explicitly** compute the Gram matrix on $\langle f_1,f_2,\Delta\rangle$ in the toy model $C_p\times C_p$ (§5).

**Results, without embellishment:**

1. **Route that works for the intersection number (§3):** the stable intersection of Allermann–Rau / Mikhalkin (fan displacement) **[DATA]** is well defined on the tropical torus $C_p\times C_p$ and gives a **symmetric, bilinear over $\mathbb{R}$** pairing $D\cdot D'$. Routes (b) RR degree and (c) flow trace coincide with it where they overlap **[CALCULATION]**, but the coincidence with (c) **is exactly the Lefschetz formula** and that is where the R-NC test bites (§6).

2. **The number is REAL, not an integer (§3.4, §5.4):** on the relevant classes —the correspondences of the flow $F_\mu$ with $\mu\notin p^{\mathbb{Q}}$— the degree of the intersection 0-cycle is generically **real**, not an integer. There is an **integral sub-lattice** (the correspondences with $\mu\in p^{\mathbb{Z}}$, the "integer Frobenii") where the number is an integer; but that sub-lattice is **countably thin** in the space of correspondences and does NOT contain the flow generator. **Doc 123's C-rank remains real. NOT resolved.**

3. **The Gram matrix in $C_p\times C_p$ (§5):** over $\langle f_1,f_2,\Delta\rangle$ with the relations of §4 reproduces
$$ G=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}\quad(\text{scaled by }(\log p)\text{; with }\Delta^2=2-2g=0\text{ for }g=1). $$
Its signature is $(1,2)$ **[CALCULATION]** — i.e. $(1,\rho_{\text{toy}}-1)$ with $\rho_{\text{toy}}=3$: **the Hodge-index signature DOES appear in the toy model.** On the primitive part (orthogonal to the ample plane $\langle f_1+f_2\rangle$) the form is **negative definite** — Hodge index OK on this finite subspace. This is encouraging and is the document's strongest piece.

4. **BUT (§5.5):** upon adding a generic correspondence $F_\mu$, the lattice of classes ceases to be of finite rank (the slopes in $H_p$ are dense in $\mathbb{R}$, Doc 123 §4.2) and the signature control of the finite case **does not survive the passage to infinite rank** — it is the T2 tension of Doc 119 (signatures are not continuous under the required limits) and it is the Babaee–Huh phenomenon **[DATA]**: there exists a tropical surface whose intersection form **does not have** the Hodge-index signature. The toy model's correct signature does NOT propagate automatically.

5. **The core (§6):** two gaps remain. (G-125.A, real/integer) the integrality of the intersection number over the flow correspondences —without it there is no integer "rank," Yoshitomi's Example 6.5 reappears. (G-125.B, signature, the deep core) whether the signature $(1,\rho-1)$ of the finite toy model **persists** over the complete lattice of correspondences —which is precisely what Babaee–Huh shows CAN FAIL tropically. The R-NC test: the eventual positivity is NOT geometric-reusable; it reduces to the Lefschetz formula = arithmetic side = circular (FAILS NC3). **The G2 ingredient is not constructed; it is isolated with precision.**

---

## 1. The classical mechanism, fixed with surgical precision

### 1.1. The object: $C\times C$ and its Néron–Severi group

**[Classical DATA, Hartshorne *Algebraic Geometry* V.1; Mumford *Abelian Varieties*; Bai *Intersection Theory on Surfaces and RH for Curves* (SRCF expos.), confirmed by WebSearch §0].** Let $C$ be a smooth projective curve of genus $g$ over $\overline{\mathbb{F}_q}$. The surface $S=C\times C$ has Néron–Severi group $\mathrm{NS}(S)$. Three distinguished classes:
- $f_1=C\times\{pt\}$ (horizontal fiber, fiber of the first projection $p_1$);
- $f_2=\{pt\}\times C$ (vertical fiber, fiber of $p_2$);
- $\Delta\subset C\times C$ (the diagonal).

To these are added the **correspondences**: for a morphism $\phi:C\to C$, its graph $\Gamma_\phi=\{(x,\phi(x))\}\subset C\times C$. The diagonal is $\Gamma_{\mathrm{id}}$; the graph of the geometric Frobenius $\Gamma_{\mathrm{Frob}}$ is the key correspondence.

### 1.2. The intersection relations (the calculation that must be reproduced)

**[Classical DATA].** The intersection form $D\cdot D'$ on $\mathrm{NS}(C\times C)$, restricted to $\langle f_1,f_2,\Delta\rangle$:
$$ f_1^2=0,\quad f_2^2=0,\quad f_1\cdot f_2=1,\quad \Delta\cdot f_1=1,\quad \Delta\cdot f_2=1,\quad \Delta^2=2-2g. $$
- $f_1^2=0$: two distinct horizontal fibers are disjoint (the fiber can be moved within its class to a disjoint one). Same for $f_2^2=0$.
- $f_1\cdot f_2=1$: a horizontal fiber and a vertical one meet at the single point $(pt_1,pt_2)$, transversally.
- $\Delta\cdot f_1=1$: the diagonal meets $C\times\{pt\}$ at the single point $(pt,pt)$.
- $\Delta^2=2-2g$: by adjunction/self-intersection, $\Delta^2=\deg(N_{\Delta/S})=\deg(T_C)=2-2g=-\deg K_C$. Equivalently $\Delta^2=\chi_{\text{top}}(C)$ (the self-intersection of the diagonal = topological Euler characteristic, **[DATA]** confirmed by WebSearch §0: "the topological Euler characteristic equals the self-intersection number of the diagonal in the Cartesian product").

The Gram matrix in the ordered basis $(f_1,f_2,\Delta)$:
$$ G_{\text{clas}}=\begin{pmatrix}0&1&1\\1&0&1\\1&1&2-2g\end{pmatrix}. $$

### 1.3. The signature and where the bound comes from (the heart of Weil)

**[CALCULATION] Signature of $G_{\text{clas}}$.** Determinant: expanding,
$$ \det G_{\text{clas}}=0\cdot(0\cdot(2-2g)-1)-1\cdot(1\cdot(2-2g)-1)+1\cdot(1-0)=-(2-2g-1)+1=-(1-2g)+1=2g. $$
For $g\ge1$, $\det>0$. Trace $=2-2g\le0$. The upper-left $2\times2$ minor is $\det\begin{pmatrix}0&1\\1&0\end{pmatrix}=-1<0$. A symmetric $3\times3$ form with a $2\times2$ minor of determinant $-1$ has **at least one positive direction and at least one negative one** in that plane; the sign of the total determinant ($+$, for $g\ge1$) together with trace $\le0$ forces signature $(1,2)$ (one positive, two negative). This is the **Hodge index: signature $(1,\rho-1)$** with the unique positive direction in the "ample cone."

**[DATA] The Hodge index theorem** (over all of $\mathrm{NS}(S)\otimes\mathbb{R}$, not just the plane): signature $(1,\rho-1)$; on $(H)^\perp$ (orthogonal to an ample class $H$, $H^2>0$) the form is **negative definite**.

**[CALCULATION] The chain toward RH.** The ample plane is $P=\langle f_1,f_2\rangle$ (ample class $H=f_1+f_2$, $H^2=2>0$). For a correspondence $Z$ of bidegree $(a,b)$, its primitive part $Z_0=Z-a\,f_2-b\,f_1$ satisfies $Z_0\cdot f_1=Z_0\cdot f_2=0$, i.e. $Z_0\in P^\perp$. Hodge index $\Rightarrow Z_0^2\le0$. This is the **Castelnuovo–Severi inequality**:
$$ Z^2\le 2\,(Z\cdot f_1)(Z\cdot f_2)\quad\Longleftrightarrow\quad Z_0^2\le0. $$
Applied to $Z=\Gamma_{\mathrm{Frob}^n}$ (graph of the $n$-th Frobenius, bidegree $(1,q^n)$, $\Gamma\cdot\Delta=\#C(\mathbb{F}_{q^n})=N_n$) the associated Cauchy–Schwarz inequality gives $|\alpha_i|=\sqrt q$ for the Frobenius eigenvalues in $H^1$ — **RH for curves**.

**[CALCULATION] Why it is NOT circular** (this is the hinge, I stress it here for the R-NC test below): the starting positivity ($Z_0^2\le0$) is a theorem about **ALL primitive classes of the surface**, proved by surface geometry (Hodge index = Poincaré duality in $H^2$ + Sylvester's theorem of inertia), which **ignores what $C$ is and where its points are**. The positivity is geometric, independent of the eigenvalues. This is what the R-NC test (Doc 119 §4.3) calls NC2 (overgeneration with content) + NC4 (in $\neg$RH a bad eigenvalue gives a self-intersection of the forbidden sign, visible without localizing anything). **This is the exact pattern that must be reproduced tropically — or where the obstruction must be documented.**

---

## 2. The base object and the square [DATA + CONSTRUCTION]

### 2.1. The scaling site as a 1-dimensional tropical object [DATA]

**[DATA]** (Connes–Consani *Geometry of the Scaling Site*, arXiv:1603.03191; via Doc 123 §4.1): the scaling site is, in its analytic version, the quotient $[0,\infty)\rtimes\mathbb{R}_+^*$ / topos of the scaling semigroup; its "building block" associated to the prime $p$ is
$$ C_p=\mathbb{R}_+^*/p^{\mathbb{Z}},\qquad\text{in the coordinate }u=\log\lambda:\quad C_p=\mathbb{R}/(\log p)\,\mathbb{Z}, $$
a **tropical circle of period $\log p$**, dimension 1, **tropical genus 1** (a loop). The sheaf $\mathcal{O}_p$: periodic, convex, piecewise-affine functions, with slopes in $H_p=\{m/p^n\}\subset\mathbb{Q}$.

**[DATA]** (1603.03191, Thm 5.17): tropical RR of type II,
$$ \mathrm{Dim}_{\mathbb{R}}H^0(D)-\mathrm{Dim}_{\mathbb{R}}H^0(-D)=\deg D, $$
with $\mathrm{Dim}_{\mathbb{R}}$ the continuous dimension (normalized limit $p^{-n}\dim_{\text{top}}$). **There is NO $H^1$ on $C_p$**; its role is played by $H^0(-D)$ (tropical Serre duality).

**[DATA]** (Yoshitomi, arXiv:1001.0448, via Doc 124 §6.3 point 1): the Baker–Norine/Gathmann–Kerber/Yoshitomi tropical RR has the form
$$ r(D)-r(K-D)=\deg D-g+1, $$
with $r(D)=\max\{r\in\mathbb{Z}_{\ge-1}:U(D,r)=\emptyset\}$ the **linear-equivalence rank**, defined via $\mathrm{ord}(f,P)$ — an invariant of linear equivalence **NOT visible from the module structure** of $H^0$. **Example 6.5** exhibits $(C,D),(C',D')$ with $H^0$ isomorphic as modules but $r(D)=1\ne r(D')=0$ **[DATA]**. This is the datum that poisons the integrality of the rank (the "root" of Doc 123).

**[CALCULATION] The tropical canonical divisor of $C_p$.** For a tropical curve $\Gamma$ of genus $g$ (first Betti number of the graph), the Baker–Norine canonical divisor is $K=\sum_{v}(\mathrm{val}(v)-2)\,v$, of degree $\deg K=2g-2$. For $C_p$ seen as a single smooth loop (a circle, with no vertices of valence $\ne2$), $g=1$, $\deg K=0$, $K\sim0$. Consistent with the RR above: $g=1\Rightarrow\deg K=0$.

### 2.2. The genus tied to the zeros [DATA + CONJECTURE]

**[DATA]** (Doc 124 §3.3, via Connes–Consani *Metaphysics of $F_1$*, arXiv:2307.06748, note 3): the sought cohomology $H^1(\mathbf{C})$ is **infinite-dimensional** (infinitely many zeros of $\zeta$), and the RR that CC have for $\overline{\mathrm{Spec}\,\mathbb{Z}}$ gives **genus 0** for $\mathrm{Spec}\,\mathbb{Z}$ (a dim-1 object, genus 0). The "genus" relevant for the square is not that of a factor but that of the product, and there (Doc 119 §2.4) the impure part must be finite but the total infinite.

**[CONJECTURE]** The "tropical genus" of the complete scaling site (not of the block $C_p$) is infinite, indexed by the zeros; the square inherits Doc 123's problem: there is no Künneth formula because the factors have no $H^1$. I therefore work on the block $C_p$ (genus 1), where everything is finite and computable, and state at the end what does and does not survive assembly.

### 2.3. The square $X\times X$ as a 2-dimensional object [CONSTRUCTION]

**[CONSTRUCTION] (status: defines the product, assumes commutation with tropicalization, leaves the exact category to be verified).** I define $X\times X$ in the category of **tropical spaces / $\mathbb{R}_{\max}$-schemes** as the fiber product of the topos of the scaling site with itself over $\mathbb{B}$ (extended to $\mathbb{R}_+^{\max}$), with structure sheaf the idempotent tensor product $\mathcal{O}\otimes_{\mathbb{B}}\mathcal{O}$ (sections = two-dimensional Newton polygons).
- **For the block:** $C_p\times C_p=(\mathbb{R}/(\log p)\mathbb{Z})^2$, a **two-dimensional tropical torus** of area $(\log p)^2$, with coordinates $(u,v)$.
- **Divisors (codim 1):** tropical "curves" within the surface — rational straight graphs of slope in $H_p$, and their balanced combinations (codim-1 tropical cycles with integer weights).
- **Assumes (A0):** that $\otimes_{\mathbb{B}}$ commutes with tropicalization and convex hull (Step 1 of Crossing B, Doc 121; **[TECHNICAL GAP]** inherited from Doc 123 §6.1).
- **To be verified:** whether it is smooth/free of tropical singularities (necessary for the tropical Hodge index of surfaces à la Babaee–Huh/surfaces to have the controlled signature — §5.5).

### 2.4. The distinguished classes [CONSTRUCTION]

In $C_p\times C_p=(\mathbb{R}/(\log p)\mathbb{Z})^2$:
- $f_1=C_p\times\{v_0\}$ (horizontal curve, a "$v=$ const" circle): codim-1 tropical cycle, slope 0 in the $u$ direction.
- $f_2=\{u_0\}\times C_p$ (vertical curve, "$u=$ const").
- $\Delta=\{u=v\}$ (the diagonal, slope 1).
- **Correspondences** $F_\mu$: the graph of the scaling flow $F_\mu:C_p\to C_p$, $u\mapsto u+\log\mu$ — that is, $\Delta_\mu=\{v=u+\log\mu\}$, a **translate of the diagonal**. For $\mu=p^k$, $F_{p^k}$ is the $k$-th "integer Frobenius" (it closes the loop onto itself $k$ times when composed with the slope). These are the **analogue of the Frobenius graphs** $\Gamma_{\mathrm{Frob}^n}$ of §1.

**[CALCULATION] Bidegree remark.** $\Delta_\mu$ has slope $1$ (bidegree $(1,1)$ in the sense of the projections), same as $\Delta=\Delta_1$. General slopes $v=su+c$ with $s\in H_p$ give correspondences of "multi-bidegree" $(1,s)$ — the analogue of the bidegree $(1,q^n)$ of the Frobenius is the slope $s$. **Here the flow is continuous: $\mu\in\mathbb{R}_+^*$, not $\mathbb{Z}$** (R-LEF-FLOW, Doc 119 §3.4). This is the decisive structural difference with curves.

---

## 3. The intersection number — the central piece (the C-rank) [CONSTRUCTION]

I define $D\cdot D'$ and evaluate the three candidate routes.

### 3.1. Route (a) — Stable intersection of Allermann–Rau / Mikhalkin

**[DATA]** (Allermann–Rau, arXiv:0709.3705 *First Steps in Tropical Intersection Theory*; Mikhalkin; confirmed WebSearch §0): there exists a **stable intersection product** of tropical cycles with integer weights, well defined as a tropical cycle (without passing to rational equivalence). Two equivalent constructions **[DATA]**: (i) Mikhalkin's **fan displacement rule** —generically perturb one of the cycles and count the cells of transversal intersection with multiplicity = index of the weight lattices—; (ii) Allermann–Rau's **reduction to the diagonal + Cartier divisors**. They coincide (in the limit).

**[CONSTRUCTION — definition of the pairing.] For two tropical 1-cycles $D,D'$ in the torus $C_p\times C_p$, I define**
$$ D\cdot D' \;:=\; \deg\big(\,\mathrm{st}(D,D')\,\big)\in\mathbb{R}, $$
where $\mathrm{st}(D,D')$ is the stable intersection (a tropical 0-cycle = formal sum of points with weights) and $\deg$ sums the weights. **Multiplicity at a transversal point** $P$ where $D$ has primitive direction $\xi$ (weight $m$) and $D'$ direction $\xi'$ (weight $m'$):
$$ \mathrm{mult}_P(D\cdot D')=m\,m'\cdot\big|\det(\xi,\xi')\big|_{\text{lattice index}}, $$
the index of the sublattice $\mathbb{Z}\xi+\mathbb{Z}\xi'$ in the ambient lattice.
- **Status:** well defined for 1-cycles with rational directions (slopes in $H_p$). **Symmetric, bilinear over $\mathbb{R}$** (weights may be real after the type-II normalization of Doc 123 §4). **The "lattice-index $\det$" is the source of integrality when directions are integral, and of reality when they are not.**

### 3.2. Route (b) — Degree of the RR restriction

**[CONSTRUCTION].** For $D'$ an irreducible tropical curve and $D$ a divisor of the square, $D\cdot D'=\deg_{D'}(\mathcal{O}(D)|_{D'})$ = degree of the divisor induced by restricting $\mathcal{O}(D)$ to $D'$, via the tropical RR of $D'$ (which is a $C_p$, dim 1, type-II RR of §2.1). **[CALCULATION]** For $D=f_1$, $D'=\Delta$: the restriction of $\mathcal{O}(f_1)$ to the diagonal $\Delta\cong C_p$ is a divisor of degree = number of points $\Delta\cap f_1$ counted with multiplicity = (via RR) $\deg=1$. Coincides with route (a).

**[CALCULATION] Compatibility (a)$\leftrightarrow$(b).** On the smooth torus, the stable intersection of $D$ with a curve $D'$ equals the degree of the restricted bundle, by the tropical projection formula (Allermann–Rau, push-forward/pull-back). **They coincide wherever both are defined** (rational irreducible curves). ✓

### 3.3. Route (c) — Trace of the flow (fixed points / periodic orbits)

**[CONSTRUCTION].** $D\cdot\Delta_\mu$ = weighted number of fixed points of the correspondence $F_\mu$ = the tropical analogue of the Lefschetz term. For $\Delta_\mu=\{v=u+\log\mu\}$ and $\Delta=\{v=u\}$:
$$ \Delta\cdot\Delta_\mu=\#\{(u,v):v=u\text{ and }v=u+\log\mu\}=\#\{u:\log\mu\equiv0\ (\mathrm{mod}\ \log p)\}. $$
- If $\mu\in p^{\mathbb{Z}}$ (i.e. $\log\mu=k\log p$): the condition is empty as a pointwise equation but the graphs **coincide** (they overlap along the whole circle) — non-transversal intersection; after stable perturbation (fan displacement) the number is that of the self-intersection $\Delta^2$ weighted, **a periodic orbit of length $k\log p$**. This reproduces R-LEF-PRIMES (Doc 119 §3.3): each prime $p$ contributes the orbit of period $\log p$.
- If $\mu\notin p^{\mathbb{Q}}$ (generic, $\log\mu/\log p$ irrational): the two graphs are translates that intersect transversally in **one point per fundamental cell**, $\Delta\cdot\Delta_\mu=1$ — but the **position** of the point densely sweeps the circle as $\mu$ varies, and weighted by the type-II measure the contribution is **real**.

**[CALCULATION — the critical datum].** Route (c) **IS the Lefschetz formula/trace of the Guillemin–Connes flow** (Doc 119 §3.4 R-LEF-FLOW, [DATA] Connes Selecta 1999: the distributional trace of the scaling flow reproduces the arithmetic side of the explicit formula, periodic orbits of length $\log p$). It coincides with (a) at transversal points. **But its coincidence with the arithmetic side is exactly where R-NC will bite (§6.3): the "geometry" (c) IS the explicit formula repackaged (tension T3 of Doc 119).**

### 3.4. The real/integer tension — the core of the problem [CALCULATION]

**This is the core of Doc 123 (C-rank), treated with full care.**

**[CALCULATION] When the number is an integer.** The multiplicity $\mathrm{mult}_P=m\,m'|\det(\xi,\xi')|$ is integral **if and only if** the directions $\xi,\xi'$ are vectors of the integer lattice $\mathbb{Z}^2$ and the weights $m,m'$ are integers. For $f_1,f_2,\Delta$ the directions are $(1,0),(0,1),(1,1)$ — **integral** — and the natural weights are 1. **That is why §4 will give integers.** For $\Delta_\mu$ with $\log\mu=k\log p$ ($\mu\in p^{\mathbb{Z}}$): direction $(1,1)$, integral → integer.

**[CALCULATION] When the number is real.** For generic $\Delta_\mu$ ($\mu\notin p^{\mathbb{Q}}$), or for a curve with general slope $s\in H_p$: the slope lattice $H_p=\{m/p^n\}$ is **dense in $\mathbb{R}$** (Doc 123 §4.2). The "lattice-index $\det$" between $(1,0)$ and $(1,s)$ is $|s|$, which for $s\in H_p$ is rational but **unbounded in denominator**; and under the type-II normalization (necessary for $\mathrm{Dim}_{\mathbb{R}}$ to exist, §2.1) the effective weight is **real**. The degree of the intersection 0-cycle is then **a generic real number**.

**[CONSTRUCTION — the integral sub-class, and why it is not enough].**
> **Integral sub-lattice $\mathcal{L}_{\mathbb{Z}}$:** the classes generated by $\{f_1,f_2,\Delta\}$ and the correspondences $\Delta_{p^k}$ ($k\in\mathbb{Z}$) — directions in $\mathbb{Z}^2$, integer weights. **On $\mathcal{L}_{\mathbb{Z}}$ the intersection number IS an integer** (it is the lattice of "integer Frobenii," the monoid $\mathbb{N}^\times$ acting, Doc 119 §3.4 convenient version).
>
> **Why it is not enough (the exact obstruction):** the scaling flow R-LEF needs is **continuous**, $\mu\in\mathbb{R}_+^*$. The **infinitesimal generator** of the flow (the one giving the spectral side $\sum_\rho\hat h(\rho)$, Doc 119 §3.4 point 3) is NOT in $\mathcal{L}_{\mathbb{Z}}$: it corresponds to $\mu$ infinitesimally close to 1, slope $1$ but an irrational translation. The signature/bound RH needs is read on the correspondences of the **continuous flow**, not on the integral sub-lattice. $\mathcal{L}_{\mathbb{Z}}$ is **countably thin** and does not contain the object encoding the zeros.

**[CALCULATION] Verdict §3.4: Doc 123's C-rank remains REAL.** The intersection number is integral on $\mathcal{L}_{\mathbb{Z}}$ (reproducing classical §4) but **real on the continuous-flow correspondences** (where the RH content lives). This is exactly the dichotomy of Doc 123 §4: the object exists, the dimension/number remains type II / real. **NOT resolved. This is G-125.A.**

---

## 4. The intersection relations [CALCULATION]

I compute on $\mathcal{L}_{\mathbb{Z}}\supset\langle f_1,f_2,\Delta\rangle$ in $C_p\times C_p$, via route (a) stable intersection. I normalize the fundamental cell area to 1 (absorbing the $\log p$ factor at the end).

**$f_1\cdot f_1$ [CALCULATION]:** $f_1=\{v=v_0\}$, direction $(1,0)$. I perturb to $f_1'=\{v=v_0'\}$ with $v_0'\ne v_0$: two parallel horizontal circles, **disjoint** on the torus. $\Rightarrow f_1^2=0$. ✓ (same as classical).

**$f_2\cdot f_2=0$** [CALCULATION]: likewise by symmetry. ✓

**$f_1\cdot f_2$ [CALCULATION]:** $f_1=\{v=v_0\}$ dir $(1,0)$, $f_2=\{u=u_0\}$ dir $(0,1)$. They meet at the unique point $(u_0,v_0)$ of the torus, transversally, $|\det\begin{pmatrix}1&0\\0&1\end{pmatrix}|=1$. $\Rightarrow f_1\cdot f_2=1$. ✓

**$\Delta\cdot f_1$ [CALCULATION]:** $\Delta=\{v=u\}$ dir $(1,1)$, $f_1=\{v=v_0\}$ dir $(1,0)$. Intersection: $u=v_0$, unique point $(v_0,v_0)$. $|\det\begin{pmatrix}1&1\\1&0\end{pmatrix}|=|-1|=1$. $\Rightarrow\Delta\cdot f_1=1$. ✓

**$\Delta\cdot f_2=1$** [CALCULATION]: likewise. ✓

**$\Delta\cdot\Delta$ [CALCULATION — the self-intersection, via perturbation].** $\Delta=\{v=u\}$. I perturb to $\Delta'=\{v=u+\epsilon\}$ (translation, $=\Delta_\mu$ with $\log\mu=\epsilon$ small irrational). $\Delta$ and $\Delta'$ are parallel (both dir $(1,1)$): **they do not meet transversally on a line of $\mathbb{R}^2$**, but **on the torus** $(\mathbb{R}/(\log p)\mathbb{Z})^2$ the line $v=u+\epsilon$ wraps around and meets $v=u$ at the points where $\epsilon\equiv0\pmod{\log p}$ along the transversal direction. For a slope-1 line on the square torus of side $L=\log p$: the number of self-intersections of a closed curve of homology class $(1,1)$ is, by the **intersection form of the torus** $H_1(T^2)\times H_1(T^2)\to\mathbb{Z}$, $\langle(1,1),(1,1)\rangle=\det\begin{pmatrix}1&1\\1&1\end{pmatrix}=0$.

But the **geometric** self-intersection (adjunction) should give $2-2g$. For $g=1$ (the torus/circle $C_p$ has genus 1): $2-2g=0$. **They coincide! $\Delta^2=0$ for $g=1$.** ✓

**[CALCULATION — cross-check with tropical adjunction].** The diagonal $\Delta\cong C_p$ is a genus-1 curve; its self-intersection by tropical adjunction is $\Delta^2=-\deg(K_\Delta)=-(2g-2)=2-2g=0$ for $g=1$. The two routes (torus homology vs adjunction) **coincide**: $\Delta^2=0$. This is a genuine consistency check of the construction. ✓

**[CALCULATION] The toy model's Gram matrix** (basis $(f_1,f_2,\Delta)$, $g=1$, $\log p$ factor restored at the end as a global positive scale that does not change the signature):
$$ \boxed{\,G_{\text{toy}}=\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}\,} $$
Note: this is $G_{\text{clas}}$ with $2-2g=0$ ($g=1$). **The toy model exactly reproduces the classical template at genus 1.**

---

## 5. The toy model $C_p\times C_p$ — the frank evidence [CALCULATION]

### 5.1. Signature of $G_{\text{toy}}$ [CALCULATION]

Eigenvalues of $\begin{pmatrix}0&1&1\\1&0&1\\1&1&0\end{pmatrix}$. Characteristic polynomial: this is $J-I$ where $J$ is the all-ones $3\times3$ matrix. $J$ has eigenvalues $3,0,0$; hence $J-I$ has eigenvalues $3-1=2$ and $0-1=-1$ (double):
$$ \mathrm{spec}(G_{\text{toy}})=\{\,2,\,-1,\,-1\,\}. $$
**Signature $(1,2)$** — one positive direction (the eigenvector $(1,1,1)$, eigenvalue $+2$), two negative. This is **exactly $(1,\rho_{\text{toy}}-1)$** with $\rho_{\text{toy}}=\dim\langle f_1,f_2,\Delta\rangle=3$. **The Hodge index appears in the toy model.** [Matches the classical calculation §1.3 evaluated at $g=1$: $\det G=2g=2>0$, trace $=0$, signature $(1,2)$.]

### 5.2. The form on the primitive part [CALCULATION]

Ample class $H=f_1+f_2$ (coordinates $(1,1,0)$). $H^2=(1,1,0)G_{\text{toy}}(1,1,0)^T=2(f_1\cdot f_2)=2>0$. ✓ ample.

Primitive part $P^\perp=\{x:x^TG_{\text{toy}}H=0\}$. $G_{\text{toy}}H=G_{\text{toy}}(1,1,0)^T=(1,1,2)^T$. Condition: $x_1+x_2+2x_3=0$. Basis of the primitive part: $e_1=(1,-1,0)$, $e_2=(1,1,-1)$ (check: $1+1-2=0$ ✓).

Restricted form:
- $e_1^TGe_1=(1,-1,0)G(1,-1,0)^T$. $G e_1=G(1,-1,0)^T=(0\cdot1+1\cdot(-1)+1\cdot0,\,1\cdot1+0+0,\,1\cdot1-1+0)^T=(-1,1,0)^T$. $e_1\cdot Ge_1=1\cdot(-1)+(-1)(1)+0=-2$.
- $e_2^TGe_2$: $Ge_2=G(1,1,-1)^T=(0+1-1,\,1+0-1,\,1+1+0)^T=(0,0,2)^T$. $e_2\cdot Ge_2=1\cdot0+1\cdot0+(-1)(2)=-2$.
- $e_1^TGe_2$: $e_1\cdot Ge_2=(1,-1,0)\cdot(0,0,2)=0$.

Matrix of the form on the primitive part: $\begin{pmatrix}-2&0\\0&-2\end{pmatrix}$ — **negative definite.** ✓✓

**[CALCULATION] Verdict §5:** on the finite subspace $\langle f_1,f_2,\Delta\rangle$ of the toy model $C_p\times C_p$, the tropical intersection form (via Allermann–Rau) has **signature $(1,2)$**, ample class $H=f_1+f_2$ with $H^2=2>0$, and is **negative definite on the primitive part** $(H)^\perp$. **The Hodge index is exactly reproduced in the toy model.** This is the document's strongest positive result: in the simplest, finite case, the correct signature DOES appear.

### 5.3. Adding an integer correspondence $\Delta_{p}$ [CALCULATION]

Let $\Delta_p=\Delta_\mu$ with $\log\mu=\log p$ — but on the torus of period $\log p$, $\log\mu=\log p\equiv0$, so $\Delta_p$ is **homologous to $\Delta$** (same class $(1,1)$). In the single-block toy model, integer correspondences collapse to the class of $\Delta$: they do not enlarge $\rho$. **[CALCULATION]** This reflects that a single $C_p$ sees only the prime $p$; to see the non-trivial "Frobenius" one must go to the **product over several primes** $C_p\times C_q$ ($p\ne q$), where $\Delta$ (diagonal correspondence) and the mixed-bidegree correspondences ARE independent. This enlarges $\rho$ but **keeps integer directions** as long as the periods are commensurable — and the periods $\log p,\log q$ are **incommensurable** ($\log p/\log q\notin\mathbb{Q}$), reintroducing reality. (Consistent with 1502.05580 / Doc 123 §1.1: exact composition of correspondences only for $\lambda\lambda'\notin\mathbb{Q}$.)

### 5.4. Integer or real? [CALCULATION — the toy model's answer]

**On $\langle f_1,f_2,\Delta\rangle$: INTEGER** (matrix $G_{\text{toy}}$ with entries in $\{0,1\}$, §4). **On the continuous-flow correspondences $\Delta_\mu$ ($\mu\notin p^{\mathbb{Q}}$): REAL** (§3.4). The boundary is exactly $\mathcal{L}_{\mathbb{Z}}$ vs the continuous flow. **The toy model confirms: there is a sub-class (finite, integral) where everything works, but it is NOT the class carrying RH content.**

### 5.5. The passage to infinite rank — where the signature can break [CALCULATION + DATA]

**[CALCULATION] The problem.** The complete lattice of correspondences $\{\Delta_\mu:\mu\in\mathbb{R}_+^*\}\cup\{$slopes in $H_p\}$ is NOT of finite rank: the slopes are dense in $\mathbb{R}$ (Doc 123 §4.2). The calculation of §5.1–5.2 (signature $(1,2)$, negative-definite primitive part) is on a **finite** subspace. The G2 question is whether the signature $(1,\rho-1)$ **persists** over the whole lattice.

**[DATA — the Babaee–Huh counterexample].** (Babaee–Huh, *A tropical approach to a generalized Hodge conjecture for positive currents*, Duke Math. J. 2017, arXiv:1502.00299; confirmed WebSearch §0): **there exists a tropical surface in $\mathbb{R}^4$ whose intersection form does NOT have the correct signature of the Hodge index theorem.** Concretely they construct a tropical current (class $(1,1)$ / $(p,p)$) that is strongly positive, closed, of rational class, but NOT approximable by positive combinations of integration currents — and the obstruction is precisely that **the intersection form of the underlying tropical surface has the wrong signature** (not $(1,\rho-1)$).

**[CALCULATION] The consequence for G2 — the deep obstruction.** Babaee–Huh shows it is **NOT automatic** for a tropical surface to have the Hodge index. The tropical Hodge index DOES hold for **non-singular smooth** tropical 2-complexes (WebSearch §0: "Hodge index theorem for the intersection product on a tropical surface ... at most one positive eigenvalue" — for non-singular complexes, via the Cartwright line / tropical surfaces), but fails in the presence of tropical singularities (which is what Babaee–Huh exploits). Therefore:
> The correct signature $(1,2)$ of the **finite and smooth** toy model does NOT propagate freely to the infinite lattice of correspondences of the square, because (i) the passage to infinite rank (density of $H_p$) is a limit, and **signatures are not continuous under limits** (tension T2 of Doc 119 §6.3); (ii) the square of the scaling site could have tropical singularities (not verified to be smooth — §2.3 to be verified), and in the presence of singularities the Hodge index **can fail** (Babaee–Huh).

**[CALCULATION] Verdict §5:** the finite toy model gives the correct signature $(1,2)$ — genuinely positive evidence. But the propagation to the complete lattice is **exactly what Babaee–Huh shows can fail tropically**, and depends on (a) smoothness of the square (not verified), (b) that the finite-rank→infinite-rank limit preserves signature (T2, no known gap). **G-125.B.**

---

## 6. The status — what was constructed, what is missing [GAP/CONJECTURE] + R-NC test

### 6.1. What was constructed (with conditional status)

**[CONSTRUCTION, to be verified by experts, NEVER [DATA]]:**
1. The **definition of the pairing** $D\cdot D'=\deg(\mathrm{st}(D,D'))$ via Allermann–Rau stable intersection (§3.1), symmetric and bilinear over $\mathbb{R}$. **Route (a) is the one that works**; it coincides with (b) RR-degree where they overlap; it coincides with (c) flow-trace at transversal points —but (c) is the Lefschetz formula (the R-NC problem).
2. The **intersection relations** $f_1^2=f_2^2=0$, $f_1\cdot f_2=\Delta\cdot f_i=1$, $\Delta^2=2-2g$ **reproduced tropically** in $C_p\times C_p$ (§4), with double check (torus homology vs tropical adjunction) for $\Delta^2=0$ at $g=1$. **Genuine, within the toy model.**
3. The **Gram matrix $G_{\text{toy}}$ and its signature $(1,2)$** with negative-definite primitive part (§5.1–5.2). **The Hodge index appears in the finite toy model.**

### 6.2. The two gaps

**[GAP G-125.A — real/integer, Doc 123's C-rank].** The intersection number is **integral on $\mathcal{L}_{\mathbb{Z}}$** (sub-lattice of integer directions: $f_1,f_2,\Delta$, integer Frobenii $\Delta_{p^k}$) but **real on the continuous-flow correspondences** $\Delta_\mu$, $\mu\notin p^{\mathbb{Q}}$ (density of $H_p$, type-II normalization). The flow carrying the zeros (the infinitesimal generator) lives outside $\mathcal{L}_{\mathbb{Z}}$. **Without integrality on the flow correspondences, there is no functorial integer "rank"; Yoshitomi's Example 6.5 reappears.** Not resolved.

**[GAP G-125.B — signature, the deep core].** Whether the signature $(1,\rho-1)$ of the finite toy model **persists** over the complete lattice of correspondences. Potential failure due to (i) discontinuity of signatures in the finite-rank→infinite limit (T2), (ii) **the Babaee–Huh phenomenon** [DATA 1502.00299]: tropical surfaces with the wrong intersection signature exist, and the square of the scaling site has not been verified to be smooth. **The tropical Hodge index is NOT automatic.** Core not resolved.

### 6.3. The R-NC test applied (Doc 119 §4.3)

**[CALCULATION]** The positivity G2 eventually needs is $Z_0^2\le0$ on the primitive part (tropical Castelnuovo–Severi). Is it geometric (reusable, holds for general correspondences) or does it reduce to RH (circular)?

- **NC1 (externality):** the definition of $D\cdot D'$ (stable intersection) and of the classes $f_i,\Delta$ is functorial from the site, mentioning neither $\zeta$ nor its zeros. **PASSES.**
- **NC2 (overgeneration):** does $Z_0^2\le0$ hold for EVERY correspondence of the square by a surface theorem (as Castelnuovo)? **In the finite toy model YES** (it is the Hodge index of $G_{\text{toy}}$, §5.2, holds for every primitive vector). **PASSES in the finite toy model.** But on the infinite lattice it is **exactly G-125.B, not proved** — and Babaee–Huh says it can fail. **PASSES conditionally, depending on G-125.B.**
- **NC3 (non-reduction to catalogued RH-equivalent positivities):** this is where it bites. Route (c) of the intersection number **IS the flow trace = Lefschetz formula = arithmetic side of the explicit formula** (§3.3, [DATA] Connes 1999). If the positivity is verified **via (c)**, it is Weil positivity repackaged = MW-1/MW-6 (tension T3 of Doc 119: "the more explicit the trace formula, the greater the risk that the geometry is the explicit formula repackaged"). **FAILS NC3 if the positivity goes through the flow trace.** The only way out is to verify it via (a)/(b) —pure surface geometry— **independently** of the trace; but that is exactly G-125.B, unresolved.
- **NC4 (two-worlds test):** in $\neg$RH, does a bad Frobenius eigenvalue give a class with a self-intersection of the forbidden sign, visible without localizing the zero? **In the finite toy model, in principle yes** (a $Z_0^2>0$ would violate the Hodge index). But since the signature over the infinite lattice is not controlled (G-125.B), **the violation cannot be certified without knowing where the zero is** — falling into the inaccessible binarity of Doc 108. **FAILS NC4 while G-125.B remains open.**

**[CALCULATION] R-NC verdict:** the toy model's intersection form **passes NC1 and NC2 in the finite case** (genuinely geometric there). But it **FAILS NC3 and NC4 on the infinite lattice**: the positivity, evaluated via the flow trace, is the explicit formula; evaluated via pure geometry, it is unresolved G-125.B. **The positivity is not yet geometric-reusable in the regime that matters; it is either circular (via c) or an open gap (via a/b).**

---

## 7. Synthesis and candor

**I do not declare G2 constructed.** What is constructed is frank and bounded:

- **The intersection form IS DEFINED** (via Allermann–Rau, §3.1), it is symmetric and bilinear; the three candidate routes coincide where they overlap, but route (c) flow-trace is the Lefschetz formula and that is the origin of the circularity (R-NC NC3).
- **The Gram matrix in $C_p\times C_p$ comes out $G_{\text{toy}}=\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}$, signature $(1,2)$, negative-definite primitive part** (§5): the Hodge index **DOES appear in the finite toy model**. It exactly reproduces the classical $C\times C$ template evaluated at $g=1$ ($\Delta^2=2-2g=0$), with a double check (torus homology ↔ tropical adjunction). **This is the strongest positive evidence: in the simplest case, the correct signature emerges.**
- **The intersection number comes out INTEGER on the sub-lattice $\mathcal{L}_{\mathbb{Z}}$ (integer directions: $f_1,f_2,\Delta$, integer Frobenii) and REAL on the continuous-flow correspondences** (density of $H_p$, type II). The integral sub-class exists but **it is countably thin and does not contain the flow generator** that carries the zeros. **Doc 123's C-rank remains real (G-125.A, unresolved).**

**The core that remains — TWO precise gaps:**
1. **(G-125.A) Integrality over the continuous-flow correspondences.** Without it there is no functorial integer rank; Example 6.5 reappears. It is Doc 123's C-rank, now localized at the $\mathcal{L}_{\mathbb{Z}}$ vs continuous-flow boundary.
2. **(G-125.B, the deep core) Persistence of the signature $(1,\rho-1)$ of the finite toy model to the infinite lattice of correspondences.** Babaee–Huh **[DATA]** shows that tropical surfaces with the **wrong** intersection signature exist: the tropical Hodge index is NOT automatic. Depends on (a) smoothness of the square (unverified) and (b) continuity of the signature under the finite-rank→infinite limit (tension T2, no known gap).

**The point of obstruction IS the result:** the intersection form is constructed and, in the finite and smooth toy model, **has the Hodge-index signature** — this is new and encouraging, and more than Doc 124 concluded was available. But the RH content lives on the **continuous-flow correspondences**, where (i) the number is real, not integer (G-125.A), and (ii) the signature is not controlled and **can fail à la Babaee–Huh** (G-125.B). The R-NC test confirms: the positivity is either verified via the flow trace (= explicit formula, circular, FAILS NC3) or via pure geometry (= G-125.B, open gap). **G2 is not constructed; it remains with its core isolated: G-125.B —the tropical Hodge index on the complete square, avoiding the Babaee–Huh phenomenon— is the missing piece, and it is new mathematics, not present in the corpus.**

---

## References

**Tropical source (WebSearch/literature):**
- L. Allermann, J. Rau, *First Steps in Tropical Intersection Theory*, arXiv:0709.3705 (Math. Z. 264 (2010)) — stable intersection, Cartier divisors, reduction to the diagonal, push/pull. **[DATA]**
- G. Mikhalkin — fan displacement rule; equivalence with Allermann–Rau (via literature, *On Tropical Intersection Theory* arXiv:2107.12067, Selecta 2022). **[DATA]**
- F. Babaee, J. Huh, *A tropical approach to a generalized Hodge conjecture for positive currents*, Duke Math. J. 166 (2017), arXiv:1502.00299 — **tropical surface in $\mathbb{R}^4$ with intersection form of wrong signature (not Hodge index)**; strongly positive current not approximable. **[DATA — the central counterexample of G-125.B.]**
- Tropical Hodge index for non-singular 2-complexes (tropical-surfaces line; WebSearch §0). **[DATA]**
- S. Yoshitomi, *Generators of modules in tropical geometry*, arXiv:1001.0448 — Example 6.5: $r(D)$ not a module-isomorphism invariant. **[DATA, via Doc 124 §6.3.]**
- D. Bai, *Intersection Theory on Surfaces and the Riemann Hypothesis for Curves* (expos., SRCF) — $C\times C$ template. **[DATA, via WebSearch; standard calculation §1.]**

**CC/CCM corpus (via internal Docs, not re-read in source this session):**
- A. Connes, C. Consani, *Geometry of the Scaling Site*, arXiv:1603.03191 — $C_p$, type-II RR, $\mathrm{Dim}_{\mathbb{R}}$. **[DATA, via Doc 123 §4.1.]**
- A. Connes, Selecta Math. 5 (1999) — distributional trace of the scaling flow = arithmetic side of the explicit formula. **[DATA, via Doc 119 §3.4.]**
- A. Connes, C. Consani, *The Riemann-Roch strategy / Complex lift of the Scaling Site*, arXiv:1805.10501 — the square as the goal, null elements. **[DATA, via Doc 123 §1.]**

**Internal (backward-only):** Doc 80 (arithmetic Castelnuovo–Severi: the semidefinite form $Q$ does not distinguish measures); Doc 119 (R-SIG (i)/(ii)/(iii); R-LEF-FLOW; R-WEIGHT; R-NC NC1–NC4; tensions T2/T3); Doc 123 (C-cok/C-rank bifurcation; toy model $C_p\times C_p$; intersection norm = C-rank = G2); Doc 124 (G2 = INDEFINITE Hodge index $(1,\rho-1)$; CC's positivity is DEFINITE, a different category; ingredient absent from the corpus).

*End of Document 125.*
