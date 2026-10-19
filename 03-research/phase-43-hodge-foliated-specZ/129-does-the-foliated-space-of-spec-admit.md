# Doc 129 — Does the foliated space of Spec ℤ admit a foliated polarizable Hodge structure?

**Program:** Riemann Hypothesis — Phase 43: new mathematics — the complex structure of the leaves.
**Prerequisites:** Doc 128 (Deninger's program; verdict (a) non-circular *conditional on Kähler–Riemann*; math/0204111 is the derived-positivity theorem; Morishita 2508.15971 gives the space+flow but NOT the cohomology; spectral rigidity 1712.04181; the unified meta-object); Doc 127 (why the dynamical/Forni route is circular: the positivity must come from the LEAVES, not the flow; the scaling flow "carries ζ inside it"); Doc 125 (the $C_p\times C_p$ toy model, Gram matrix $G_{\text{toy}}$ signature $(1,2)$, negative-definite primitive; G-125.A real/integer; G-125.B signature persistence à la Babaee–Huh).

**Labeling discipline (absolute rule, maximum risk of a false victory):** **[DATA]** = read from a source this session (arXiv, exact citation) or internal backward-only theorem. **[CONSTRUCTION]** = object I design, with conditional status. **[COMPUTATION]** = my own derivation. **[GAP]** = what is missing, stated precisely. **[CONJECTURE]** = what I propose. **[UNVERIFIED]**. NEVER "proved" except when genuine. **The goal is NOT to prove that the structure exists — it is to determine WHETHER it can exist, build what is buildable, and isolate the core + the circularity test.** If the required complex structure turns out to be ζ smuggled in by hand, that is the result (Doc 130 will rule on it in parallel; here, the pre-test).

---

## 0. Executive summary

Doc 128's verdict was: Deninger's program is the first *non-circular* framework (RH-positivity is a theorem of Hodge theory along the leaves, math/0204111, not Weil's positivity renamed), **conditional on the space being of Kähler–Riemann type**. This document attacks the condition head-on: does the foliated space of Spec ℤ (in the only incarnation that exists today as an object, Morishita's) **have leaves that are Kähler complex manifolds**, as math/0204111 REQUIRES? And if it did, of what **complex dimension**, and does that dimension close with the square of Doc 125 (the intersection form of signature $(1,2)$)?

**Central findings:**

1. **What math/0204111 proves (§1) [DATA].** For a **Kähler–Riemann foliation** —a foliation whose leaves are **complex manifolds carrying, leaf by leaf, a Kähler metric**, with the complex structure $J$ on $T\mathcal F$ integrable on each leaf and varying smoothly in the transverse direction, *plus* a transverse metric making it a Riemannian foliation (bundle-like)— Deninger–Singhof prove: (i) **foliated Hard Lefschetz** $L^{g-r}:\bar H^r_{\mathcal F}\xrightarrow{\sim}\bar H^{2g-r}_{\mathcal F}$ (Prop. 4.3), where $g=\dim_{\mathbb C}$ of the leaf; (ii) a **real polarizable Hodge structure** of weight $r$ over the primitive $P^r_{\mathcal F}$ (Prop. 4.4); (iii) **Hodge–Riemann positivity** $Q(\xi,J\bar\xi)>0$ for $\xi\ne0$. The **source** of the positivity is EXACTLY the classical Hodge polarization of a compact Kähler manifold, transported leaf by leaf via the Álvarez López–Kordyukov smooth Hodge decomposition (the classes of $\bar H^\bullet_{\mathcal F}$ = smooth global forms harmonic along the leaves; the leaf-by-leaf $L^2$ product is positive-definite). **The Kähler complex structure of the leaves is NOT optional: it is the hypothesis that turns everything on.** [DATA, verbatim §1.3]

2. **Morishita's space (§2) [DATA].** Morishita 2508.15971 builds Deninger's foliated dynamical system $\mathfrak X_K=\check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+$. Structure **verified from the HTML source**: the transversal $\check X_K(\mathbb C)$ is **totally disconnected (profinite, dimension 0)** — an inductive limit of sets of pairs $(\mathfrak p,P)$ with $P\in\mathrm{Hom}(W_{\mathrm{rat}}(\kappa(\mathfrak p)),\mathbb C)$; the **leaves** are the images of $\check X_K(\mathbb C)\times\{u\}$, and the only direction with genuine dimension is **that of the flow $\mathbb R_+$** (1-dim). The flow's **closed orbits** (the primes) are circles $\gamma_{\mathfrak p}$ of length $\log N\mathfrak p$. **CRITICAL: the paper states there is NO complex or Kähler structure anywhere; all structures are real, and the "geometric" direction is that of the flow, with a profinite transversal of dimension 0.** [DATA, verbatim §2]

3. **The first breaking point: Morishita's leaves are NOT complex manifolds (§2.4) [DATA + COMPUTATION].** In $\mathfrak X_K$, the "leaf" is an object whose only continuous direction is the flow $\mathbb R_+$ (with a profinite transversal of dim 0). **It is not a complex manifold of any dimension** — it is a solenoid/1-dimensional real leaf (the scaling direction) over an arithmetic Cantor set. The central hypothesis of math/0204111 (Kähler leaves of dim_ℂ $g\ge1$) **literally FAILS** in the space that exists today. Deninger's foliated Hodge theory **does not apply to Morishita's space as it is currently built.** This is the first firm verdict: **(c) the leaves have no complex structure.** [COMPUTATION on DATA]

4. **The dimensional mismatch, precisely stated (§3) — the core [COMPUTATION + GAP].** For the intersection form of the square of Doc 125 (signature $(1,2)$, negative-definite primitive) to be the Hodge–Riemann polarization of math/0204111, the pairing would need to live in the **middle degree** of a Kähler leaf of **complex dimension $g=2$ (a complex surface)**: there $\bar H^2_{\mathcal F}=\bar H^{1,1}_{\mathcal F}\oplus(\text{parts }2,0\ \text{and}\ 0,2)$, and the polarization over $P^2_{\mathcal F}\cap H^{1,1}$ has the Hodge-index signature $(1,h^{1,1}-1)$ — exactly $(1,2)$ if $h^{1,1}_{\text{prim}}+1=3$. **But the existing space (Morishita) has leaves of dim_ℂ $0$, and the space of Deninger's simple example (math/0204194) has leaves $\mathcal F_{\mathcal L}$ of dim_ℂ $1$ (curves/Riemann surfaces), not surfaces.** **The dimension fails to close along two routes at once:** (i) Morishita: leaf dim_ℂ $=0$, there is not even Hodge theory; (ii) the realized geometric case (elliptic curve): leaf dim_ℂ $=1$, giving the Hodge index of a *curve* ($H^1$, symplectic signature $(g,g)$), not the Hodge index of a *surface* ($H^2$, signature $(1,\rho-1)$) which is what the square needs. **The square $C_p\times C_p$ is two-dimensional (a surface); Deninger's leaf is 1-dimensional (a curve or less). Dimension mismatch $2$ vs. $\le1$.** [COMPUTATION — this is the core, §3]

5. **The verdict (§7): (b)/(c) — the dimension does NOT close AND the leaves (in the existing space) are not complex.** It is not (a): Morishita's space does not admit Deninger's foliated Hodge theory because its leaves are real of dim 0. Even *supposing* a space with complex leaves were built (as in the simple example), the leaf's dimension would be $1$ (curve), and the object that gives the square's signature $(1,2)$ lives in the $H^2$ of a **surface** (dim 2). **The scaling-site square does NOT correspond to a leaf of Deninger's space, but to the product of two copies of the total space** (§5) — and the product of two foliated spaces of dimension 1 (flow) over profinite transversals is NOT a Kähler manifold of dim_ℂ 2; it is a laminated object of real dimension 2 (two flows) over a profinite transversal, with no complex structure. **The mismatch is structural and twofold: dimension (curve vs. surface) and nature (real-laminated vs. Kähler).**

6. **The circularity pre-test (§6) [CONJECTURE].** If one tried, *by force*, to endow Morishita's leaves with a complex structure of suitable dim_ℂ so that the polarization gives $(1,2)$, **where would that complex structure come from?** In the geometric case (elliptic curve/function fields) the complex structure of the leaves comes from **external geometry** (the underlying Riemann surface $X(\mathbb C)$, which already exists). For Spec ℤ there is NO such ambient Riemann surface — the archimedean place gives a single point, not a complex curve. The only known way to "manufacture" a variation of Hodge structure with the correct eigenvalues would be to **inject the zeros of ζ as periods** — exactly the circular injection that Doc 130 must diagnose in depth. **Preliminary reading [CONJECTURE]: the complex structure needed is NOT external (there is no archimedean geometry to provide it for Spec ℤ); its candidate source is ζ smuggled in by hand. Fine-grained verdict deferred to Doc 130.**

---

## 1. THE DERIVED-POSITIVITY THEOREM: math/0204111 [DATA, fixed with maximum precision]

### 1.1. The hypotheses: what structure the foliated space must have

**[DATA — verbatim definition, via ar5iv of math/0204111 (Deninger–Singhof, *Real polarizable Hodge structures arising from foliations*)].**

The starting structure is a **Kähler foliation** which is, in addition, **Riemannian**:

> "A Kähler foliation $(X,\mathcal F,h=S-2i\omega_{\mathcal F})$ which is also a Riemannian foliation is called a **Kähler–Riemann foliation**."

Breakdown of the hypotheses (each one is necessary):

- **(H1) The leaves are Kähler complex manifolds.** The foliation $\mathcal F$ carries a **complex structure**: an almost-complex structure $J$ on the tangent bundle to the leaves $T\mathcal F$ such that **every restriction $J|_{\text{leaf}}$ is integrable** — hence **each leaf is a complex manifold**, and these holomorphic structures **vary smoothly in the transverse direction** [DATA, confirmed by WebSearch: *"A complex structure on a foliation F is an almost complex structure J on TF such that all restrictions J|F to the leaves are integrable. Then the leaves carry holomorphic structures which vary smoothly in the transverse direction."*]. The leaf has **real dimension $2g$ = complex dimension $g$**, with $g=\dim_{\mathbb C}$ of the leaf. The leaf-by-leaf Kähler form $\omega_{\mathcal F}$ satisfies $d_{\mathcal F}\omega_{\mathcal F}=0$ (closed *along the leaves*).

- **(H2) Riemannian transverse metric (Riemannian/bundle-like foliation).** The normal plane to the leaves carries a metric that makes the foliation Riemannian (bundle-like); this is what allows the **smooth Hodge decomposition** and makes the reduced foliated cohomology tractable. [DATA]

- **(H3) Codimension and transverse orientation.** The transverse direction is oriented and has a complementary metric. In the arithmetic case, the "geometric" codimension is played by the $\mathbb R$ flow (codimension 1 transverse to which the leaves lie). [DATA]

**[COMPUTATION — the point I keep for the whole document].** Hypothesis H1 is **inflexible**: *the leaves must be complex manifolds, of a definite complex dimension $g\ge1$.* Without complex structure on the leaves there is no Hodge decomposition $H^{1,0}\oplus H^{0,1}$, no operator $J$, no form $Q(\cdot,J\bar\cdot)$, no polarization. **The whole theorem hangs on the leaves being Kähler.**

### 1.2. The conclusion: Hard Lefschetz + Hodge–Riemann + positivity

**[DATA — verbatim statements].**

- **Foliated Hard Lefschetz (Prop. 4.3).** For $r<g$:
$$ L^{g-r}:\ \bar H^r_{\mathcal F}(X,\mathbb C)\ \xrightarrow{\ \sim\ }\ \bar H^{2g-r}_{\mathcal F}(X,\mathbb C), $$
an isomorphism, where $L=\wedge\,[\omega_{\mathcal F}]$ is the Lefschetz operator (cup with the foliated Kähler class) and $g=\dim_{\mathbb C}$ of the leaf. **The $g$ appearing in the exponent $L^{g-r}$ is the complex dimension of the leaf.** [DATA]

- **Polarizable Hodge structure (Prop. 4.4).** "$Q$ defines a polarization of weight $r$ of the real Hodge structure $P^r_{\mathcal F}(X)$", with the Lefschetz decomposition $\bar H^r_{\mathcal F}(X,\mathbb C)=\bigoplus_s L^s(P^{r-2s}_{\mathcal F}(X))$ into primitive parts. [DATA]

- **Hodge–Riemann positivity** (from §3.3). The bilinear form satisfies
$$ Q(\xi,J\bar\xi)>0\quad\text{for }\xi\ne0 $$
over the primitive. [DATA]

- The **Kählerian Serre analogue of the Weil conjectures** carries over. [DATA]

### 1.3. WHERE the positivity comes from — the exact origin (the "external" source)

**[DATA — the hinge].** The positivity rests on the **smooth Hodge decomposition theorem of Álvarez López–Kordyukov** (ref. [1] of the paper):

> "the smooth Hodge decomposition theorem of Álvarez López and Kordyukov ... expresses $\bar H^r_{\mathcal F}(X)$ as the space of smooth global forms on $X$ along $\mathcal F$ whose restrictions to the leaves are harmonic"

and the decomposition $\mathcal A^\bullet_{\mathcal F}(X)=\mathcal H^\bullet_{\mathcal F}(X)\oplus\mathrm{im}\,d_{\mathcal F}\oplus\mathrm{im}\,d^*_{\mathcal F}$, with $\bar H^\bullet_{\mathcal F}(X,\mathbb C)\cong\mathcal H^\bullet_{\mathcal F}(X)$ as Fréchet spaces.

**[COMPUTATION] The mechanism of positivity, step by step.** The classes of $\bar H^r_{\mathcal F}$ are represented by forms **harmonic along each leaf**. Each leaf is a **compact Kähler manifold** (or with the necessary analyticity/completeness), and over a compact Kähler manifold classical Hodge theory gives: the Hodge–Riemann bilinear relations, i.e., the form $Q(\xi,J\bar\xi)=\int_{\text{leaf}}\xi\wedge\overline{*\,\xi}$ (with Weil's signs) is **positive-definite over the primitive harmonic forms**. This positivity is the **Hodge polarization of the Kähler leaf**, integrated leaf by leaf against the invariant transverse measure. **The source of the positivity is, literally, the classical Hodge polarization of a compact Kähler manifold — the same one that gives the Hodge index in algebraic geometry — applied on each leaf and averaged transversally.** [DATA + COMPUTATION]

**[COMPUTATION — the implication that makes it non-circular (reminder of Doc 128 §3).** The positivity is **not postulated**: it is **derived** from the leaves being Kähler. It is geometric, holds for *every* primitive class, and ignores where ζ's zeros are. It passes NC1/NC2/NC4. **But hypothesis H1 (Kähler leaves) is where all the content is concentrated:** Deninger's non-circularity IS the statement "building the Kähler space ⟹ positivity," and the price is building a space with Kähler leaves of the correct dimension. **This document tests precisely whether such a space exists / can exist for Spec ℤ.**

---

## 2. MORISHITA'S SPACE: 2508.15971 [DATA]

### 2.1. What space it exactly builds

**[DATA — via HTML arxiv.org/html/2508.15971].** For a number field $K$ (in the main result, abelian), Morishita builds **Deninger's foliated dynamical system**:
$$ \mathfrak X_K\ :=\ \check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+, $$
the quotient of $\check X_K(\mathbb C)\times\mathbb R_+$ by the right action of $\mathbb Q_+$.

- **The transversal $\check X_K(\mathbb C)$.** It is an **inductive limit** $\check X_K(\mathbb C)=\varinjlim_{n}\dot X_K(\mathbb C)$, where each $\dot X_K(\mathbb C)$ consists of pairs $(\mathfrak p,P)$ with $\mathfrak p\in X_K$ (a prime) and $P\in\mathrm{Hom}(W_{\mathrm{rat}}(\kappa(\mathfrak p)),\mathbb C)$. **$\check X_K(\mathbb C)$ is totally disconnected (profinite, topological dimension 0)**, with the topology of pointwise convergence. [DATA verbatim]

- **The flow (Frobenius $\mathbb R_+$-flow).** $\phi^t([(\mathfrak p,P),u]):=[(\mathfrak p,P),tu]$ — the scaling flow. [DATA]

- **The leaves.** "taking the images of $\check X_K(\mathbb C)\times\{u\}$ ($u\in\mathbb R_+$) as leaves" — a foliation of **codimension 1**, transverse to the flow. [DATA]

- **The closed orbits (the primes).** For $\mathfrak p$ over $p$: $\gamma_{\mathfrak p}$ is a **circle of length $\log N\mathfrak p$** (closed $\mathbb R_+$ orbit); the bundle $\Gamma_{\mathfrak p}$ is the mapping torus of multiplication by $\mathrm{lk}_p$ in $\hat{\mathbb Z}^\times_{(p)}$ (Thm 2.2.8). [DATA]

### 2.2. The dimension and nature of the leaves — the decisive datum

**[DATA — verbatim from the source].** "There is **no complex or Kähler structure** on leaves anywhere in this paper. All structures are real." The direction with genuine dimension is **that of the flow $\mathbb R_+$ (1-dim)**; the transversal is **profinite (dim 0)**. The leaf (image of $\check X_K(\mathbb C)\times\{u\}$) inherits the topology of the profinite transversal: it is **0-dimensional as a subspace of the transversal**, and the total space $\mathfrak X_K$ is "genuinely 1-dimensional in the flow direction ($\mathbb R_+$) crossed with a totally disconnected (0-dimensional) transversal". [DATA verbatim]

### 2.3. The comparison map with Connes–Consani

**[DATA, confirming Doc 128 §2.3].** The map $\Psi_F:\mathfrak X_F\to\mathscr X_F$ (to CC's adelic space) is **$\mathbb R_+$-anti-equivariant** (the two spaces have opposite flow directions) and **is NOT an isomorphism**. It sends Deninger's closed $\mathbb R_+$ orbits to CC's adelic circles $C_{\mathfrak p}$. **No complex structure appears in the comparison.** [DATA]

### 2.4. FIRST BREAKING POINT: Morishita's leaves are not complex manifolds

**[COMPUTATION — firm verdict about the existing space].** Hypothesis H1 of math/0204111 requires **leaves that are Kähler complex manifolds of dimension $g\ge1$**. In Morishita's space:

- the leaf has **real dimension 0 in the transverse direction** (profinite transversal), and the only continuous direction of the space is the **flow $\mathbb R_+$ (dim 1)**, which is **transverse to the leaves, not tangent to them**;
- hence the leaf **is not a differentiable manifold of dimension $\ge1$**, and *a fortiori* **is not a complex manifold**;
- **there is no almost-complex structure $J$, no decomposition $H^{1,0}\oplus H^{0,1}$, no form $Q(\cdot,J\bar\cdot)$, no polarization.**

> **VERDICT-129.A [COMPUTATION on DATA].** *Deninger's foliated Hodge theory (math/0204111) **does NOT apply** to Morishita's space 2508.15971 as it is built: its leaves are real of dimension 0 (profinite transversal), not Kähler complex manifolds. Morishita's space realizes the **stage** (space + flow + orbits = primes, exactly as Doc 128 §2.3 established), but **NOT the geometric category (Kähler) where the derived positivity is a theorem.** This confirms, from the space side, what Doc 128 §2.3 already said from the cohomology side: Morishita gives the underlying space, NOT the Hodge structure.*

**[COMPUTATION — important nuance, not to overstate].** This does NOT prove that *no* foliated space of Spec ℤ can have Kähler leaves. It proves that **the only object built today** (Morishita's) does not have them. The question "could one that does exist?" is that of §3–§5. But it already fixes that **the direct route —take Morishita's and apply math/0204111 to it— is closed.**

---

## 3. THE DIMENSION AND THE COMPLEX STRUCTURE: the core [CONSTRUCTION / GAP]

Here I carry out the dimensional analysis that the assignment marks as the core: what complex dimension of leaf is needed for $H^1$ of the square (Doc 125, signature $(1,2)$) to be the primitive $H^{1,1}$ of a Kähler leaf where Hodge–Riemann gives negative-definiteness?

### 3.1. The degree and the signature the square requires

**[DATA — reminder of Doc 125].** The intersection form over $\langle f_1,f_2,\Delta\rangle\subset \mathrm{NS}(C_p\times C_p)$ (the square, a **tropical surface of dimension 2**) has Gram matrix $G_{\text{toy}}=\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}$, signature $(1,2)$, negative-definite over the primitive. This lives in **degree 2** of the surface (divisor classes = $H^2$/$\mathrm{NS}$), which is the **middle degree** of a surface (dim_ℝ 4, dim_ℂ 2). [DATA]

**[COMPUTATION — the classical Hodge translation].** In classical algebraic geometry, the signature $(1,\rho-1)$ of the Hodge index over $\mathrm{NS}(S)$ of a surface $S$ is **exactly** the Hodge–Riemann polarization over $H^{1,1}_{\mathrm{prim}}(S)$: over $H^2$ of a Kähler surface, the intersection form restricted to $H^{1,1}\cap H^2(\mathbb R)$ has signature $(1,h^{1,1}-1)$ (one positive = the Kähler class, the rest negative = primitive), and this **is** the Hodge–Riemann bilinear relation in weight $r=2$ over a Kähler manifold of **complex dimension $g=2$**. [classical DATA]

### 3.2. The required leaf complex dimension

**[COMPUTATION — the explicit dictionary].** For math/0204111 to produce the square's signature $(1,2)$ as a foliated polarization, one needs:

| Square object (Doc 125) | Required Kähler–Riemann object (math/0204111) |
|---|---|
| Tropical surface $C_p\times C_p$, dim_ℂ 2 | Kähler leaf of **dim_ℂ $g=2$** |
| Degree of the classes: $\mathrm{NS}=H^2$ (middle degree) | $\bar H^2_{\mathcal F}$, weight $r=2$ (middle degree, $r=g$) |
| Signature $(1,2)$, negative-definite primitive | Polarization $Q$ over $P^2_{\mathcal F}\cap\bar H^{1,1}_{\mathcal F}$, Hodge index $(1,h^{1,1}_{\text{prim}})$ |
| Hard Lefschetz: ample class $\ell=f_1+f_2$, $\ell^2>0$ | $L^{g-r}=L^0=\mathrm{id}$ in middle degree $r=g=2$; HL relates $r<g$ with $2g-r$ |

> **Dimensional requirement [COMPUTATION]:** *the leaf must be a **complex surface (dim_ℂ 2)**, and the pairing of Doc 125 must live in its **middle degree $\bar H^2_{\mathcal F}=\bar H^{2,0}\oplus\bar H^{1,1}\oplus\bar H^{0,2}$**, with the signature $(1,2)$ housed in the primitive $(1,1)$ part.*

### 3.3. WHY IT DOES NOT CLOSE: the exact dimensional mismatch

**[COMPUTATION + GAP — the core of the document].** The dimension does NOT close, and it fails along TWO independent routes, both falling short:

**(Mismatch-I) The existing space (Morishita): leaf dim_ℂ $=0$.** As in §2.4, the leaf of $\mathfrak X_K$ has dimension 0 (profinite transversal). $0\ne2$. There is not even a leaf $H^1$, let alone a surface's $H^2$. The deficit is total: **two whole complex dimensions** and the complex structure itself are missing. [COMPUTATION]

**(Mismatch-II) The realized geometric case (math/0204194, elliptic curve): leaf dim_ℂ $=1$.** [DATA — verbatim from math/0204194]. The **only example where Deninger DOES realize the foliated Hodge theory** is that of the elliptic curve over a finite field. There the space is **3-dimensional real**, $X=\tilde X/H$ with $\tilde X=\mathbb C\times V_\xi\Gamma\times\mathbb R$; the leaves $\mathcal L$ are real of dim 3, but inside each leaf there is a **sub-foliation $\mathcal F_{\mathcal L}$ whose leaves are complex curves of dimension 1 (Riemann surfaces)** — "the union of the tangent spaces to the $\mathcal F_{\mathcal L}$-leaves is naturally a rank 2 vector bundle on $X$" (real rank 2 = dim_ℂ 1). The explicit formula appears as $\mathrm{Ind}_t(d_{\mathcal F_{\mathcal L}})(\alpha)$, the **transverse index of the de Rham complex along the holomorphic leaves of dim_ℂ 1**. [DATA]

> **The exact mismatch [COMPUTATION]:** *Deninger's complex leaf, in the only case where it exists, is a **curve (dim_ℂ 1)**, whose Hodge theory lives in $H^1$ with **symplectic signature $(g,g)$** (the Riemann form over $H^{1,0}\oplus H^{0,1}$ — Doc 127 §1.1). The square of Doc 125 needs the $H^2$ of a **surface (dim_ℂ 2)**, with **Hodge-index signature $(1,\rho-1)$**. These are objects of **different degree and dimension**: curve $H^1$ ($g,g$) vs. surface $H^2$ $(1,\rho-1)$. Deninger's leaf is of dimension $1$; the square is of dimension $2$. **A whole complex dimension is missing.***

### 3.4. The reconciliation Doc 128 §2.4 had proposed, and why the mismatch limits it

**[COMPUTATION].** Doc 128 §2.4 suggested that "Hodge index over the square ⟺ polarization over $\bar H^1$ of the factor" via the standard Künneth duality. In the classical case of curves, this is correct: the Hodge index over $H^2(C\times C)$ reduces to the polarization of $H^1(C)$ via Künneth $H^2(C\times C)=\bigoplus H^i(C)\otimes H^{2-i}(C)$, and the $H^1\otimes H^1$ piece carries the content. **This relocates the square's positivity (dim 2) to the factor (dim 1).** In this sense, **Deninger's dim_ℂ 1 leaf WOULD be the correct object if the square reduced to its factor via Künneth.**

**[GAP — why this does not save the dimensional closure].** Three obstructions, in increasing order of severity:

1. **Tropical Künneth does not exist** (Doc 123 [DATA], cited in Doc 128 §2 GAP): the square→factor reduction that in the classical case is Künneth **is not available** on the tropical scaling site (the factors $C_p$ have no $H^1$; the RR is of type II). Without Künneth, the square's content does not relocate cleanly into a factor's $H^1$. [DATA/GAP]

2. **The factor $C_p$ is not a complex curve.** Even accepting the reduction, the "factor" would be $C_p$ = a tropical circle of period $\log p$ (dim_ℝ 1, **real**, not a complex Riemann surface). Its tropical "$H^1$" is real of type II, **with no $H^{1,0}\oplus H^{0,1}$ structure** because there is no complex structure. Hodge–Riemann polarization needs the Hodge decomposition, which needs $J$, which **does not exist on $C_p$**. [COMPUTATION]

3. **Even in the geometric case, Deninger's leaf is NOT the factor.** In math/0204194 the complex leaf $\mathcal F_{\mathcal L}$ is the **Riemann surface $X(\mathbb C)$ associated with the archimedean place of the elliptic curve** — a geometry that **exists because there is a genuine archimedean complex point with its Riemann structure**. For Spec ℤ, the archimedean place is **a single point** $\infty$ (the real valuation $|\cdot|_\infty$), **not a complex curve**. **There is no ambient Riemann surface for the leaf to inherit its complex structure from.** This is the break that §6 (circularity pre-test) picks up. [COMPUTATION + DATA]

---

## 4. IF THE DIMENSION CLOSED [CONSTRUCTION — the counterfactual scenario]

**[CONSTRUCTION — status: hypothetical, contingent on a space that does NOT exist].** Suppose, *against the facts of §2–§3*, that a foliated space $\mathfrak X_{\mathbb Z}$ existed for $\overline{\mathrm{Spec}\,\mathbb Z}$ with:
- leaves that were **Kähler complex surfaces (dim_ℂ 2)**, with integrable complex structure $J$ varying smoothly transversally, leaf by leaf;
- a Riemannian transverse metric (Riemannian foliation);
- a flow $\phi^t$ with closed orbits of length $\{\log p\}$ and foliated cohomology $\bar H^\bullet_{\mathcal F}$ carrying ζ's zeros in $\bar H^1_{\mathcal F}$ (or the appropriate degree).

**[CONSTRUCTION — what it would give].** Then math/0204111 would produce, **as a theorem** (not postulated):
- foliated Hard Lefschetz $L^{g-r}$ with $g=2$;
- a real polarizable Hodge structure over $P^2_{\mathcal F}$;
- the positivity $Q(\xi,J\bar\xi)>0$ over the primitive of $\bar H^2_{\mathcal F}\cap\bar H^{1,1}$.

**[CONSTRUCTION — how it would elevate the toy model's signature $(1,2)$].** The matrix $G_{\text{toy}}$ of Doc 125 (signature $(1,2)$, negative-definite primitive) **would be the finite/tropical shadow of the Hodge–Riemann polarization over $\bar H^{1,1}_{\mathcal F,\mathrm{prim}}$ of the leaf-surface**. "Negative definiteness over the primitive" (G2) **would be a theorem of Hodge theory along the leaves**, not an accident of the finite case nor the flow's trace. This would close G-125.B (the signature's persistence) **by Hodge geometry, evading Babaee–Huh** (which obstructs the *tropical-intersection* route, but not the *analytic-Hodge-of-leaves* route, Doc 128 §3.3) and **evading NC3** (the positivity would not be read on the flow's trace = explicit formula, but on the leaves' polarization, geometric). [CONSTRUCTION]

**[GAP — what would remain to verify in this counterfactual scenario, in order of difficulty].**
1. **[GAP-CF1, existence]** That $\mathfrak X_{\mathbb Z}$ exists with Kähler leaf-surfaces of dim_ℂ 2 and orbits $\{\log p\}$. **It does not exist; not even for dim_ℂ 1 leaves (curves) has it been built for Spec ℤ** — the only realized case is the elliptic curve (math/0204194). Spectral rigidity (1712.04181, Doc 128 §4.2) further says that simple constructions (suspensions) do not give the spectrum $\{\log p\}$. [GAP — the deepest]
2. **[GAP-CF2, the leaf dimension]** Why the leaf should be a **surface** (dim_ℂ 2) and not a **curve** (dim_ℂ 1). Deninger's program conjectures, for $\overline{\mathrm{Spec}\,\mathbb Z}$ (an object of arithmetic dimension 1 = "arithmetic curve"), a foliated space of **real dimension 3** with leaves of dimension... — and in the geometric analogue (curve) the complex leaves are **curves (dim_ℂ 1)**, NOT surfaces. **The square lives in dim 2 precisely because it is the PRODUCT; Deninger's space is that of $X$, not of $X\times X$.** This is §5. [GAP]
3. **[GAP-CF3, infinite-dimensionality]** $\bar H^\bullet_{\mathcal F}$ is infinite-dimensional (the zeros); the polarization of math/0204111 is for infinite-dimensional reduced foliated cohomology (that is an *advantage* over AHK, Doc 128 §3.3) — but the signature $(1,\infty)$ and its persistence under the infinite assembly (T2, Doc 119) still have no known gap. [GAP]

---

## 5. IF IT DOES NOT CLOSE: precise characterization of the mismatch [GAP — the dominant result]

**[COMPUTATION — the mismatch, precisely isolated].** The dimension does NOT close. There are **three nested mismatches**, each fatal on its own:

### 5.1. Mismatch of existence of complex structure (the most basic)

The existing space (Morishita 2508.15971) has **real leaves of dimension 0** (profinite transversal); **there is no complex structure on any leaf**. Deninger's foliated Hodge theory does not apply. **(c) the leaves have no complex structure** — literally, for the space that exists today. [§2.4]

### 5.2. Leaf-dimension mismatch (curve vs. surface)

Even in the realized geometric case (math/0204194), the complex leaf is a **curve (dim_ℂ 1)**, with Hodge theory in $H^1$ of symplectic signature $(g,g)$. The square of Doc 125 is a **surface (dim_ℂ 2)** with Hodge index $(1,\rho-1)$ in $H^2$. **A complex dimension is missing**: Deninger's leaf is dim 1, the square is dim 2. [§3.3]

### 5.3. Localization mismatch: the square is NOT a leaf, it is the product of the total space

**[COMPUTATION — the most important structural mismatch, foreshadowed].** This is the decisive conceptual break:

- **Deninger's space $\mathfrak X$ is the analogue of $X$** (an arithmetic scheme, $\overline{\mathrm{Spec}\,\mathbb Z}$), **not of $X\times X$.** Its foliated cohomology $\bar H^\bullet_{\mathcal F}$ carries the zeros in $\bar H^1_{\mathcal F}$ (degree 1, not degree 2).
- **The square of Doc 125 ($C_p\times C_p$) is the analogue of $X\times X$** — the *surface* over which surface intersection theory is done (the Castelnuovo–Severi/Weil template).
- **Hence the square does NOT correspond to a LEAF of Deninger's space.** It corresponds to the **product $\mathfrak X\times\mathfrak X$ of two copies of the total space.** And the product of two foliated spaces of real dimension 1 (each the flow direction) over profinite transversals is a laminated object of **real dimension 2 (two flows $\mathbb R_+\times\mathbb R_+$)** over a profinite transversal — **NOT a Kähler manifold of dim_ℂ 2**, but a real-laminated object with no complex structure. [COMPUTATION]

> **VERDICT-129.B [COMPUTATION].** *There is a **confusion of levels** between the two programs: Deninger places RH-positivity over $\bar H^1_{\mathcal F}(\mathfrak X)$ (degree 1 of the total space $X$, via the leaves' polarization, which in the geometric case are dim_ℂ 1 curves); the square program (Doc 124–125) places the positivity over $H^2(X\times X)=\mathrm{NS}$ (degree 2 of the product, surface Hodge index). **They are two DUAL incarnations of the same positivity** (Doc 128 §2.4: Hodge index over the square ⟺ polarization over $H^1$ of the factor), **but the duality identifying them is Künneth, and tropical Künneth does not exist (Doc 123).** Without Künneth, the square (dim 2, surface) and Deninger's leaf (dim 1, curve) **do not get identified**, and the dimensional closure fails.*

### 5.4. Summary of the mismatch

| Route | Object | dim_ℂ | Degree/signature | Does it close with the square $(1,2)$? |
|---|---|---|---|---|
| Morishita (exists) | real leaf | 0 | no Hodge theory | NO — no complex structure |
| math/0204194 (geometric case) | leaf = curve | 1 | $H^1$, symplectic $(g,g)$ | NO — wrong degree/dim (one dim short) |
| Square Doc 125 | surface $C_p\times C_p$ | (2, tropical) | $H^2=\mathrm{NS}$, $(1,2)$ | is the PRODUCT, not a leaf |
| What would be needed | Kähler leaf-surface | 2 | $H^2$, $(1,\rho-1)$ | yes, but does NOT exist (§4 GAP-CF1) |

**[COMPUTATION] The exact obstacle, in one sentence:** *Deninger's space is of the wrong dimension for the square (it is the analogue of $X$ —leaves of dim_ℂ $\le1$, curves— not of $X\times X$ —a surface of dim_ℂ 2), its existing realization (Morishita) does not even have complex leaves (dim_ℂ 0), and the bridge that would identify them (Künneth, the Hodge-index ⟺ polarization duality) does not exist tropically.*

---

## 6. THE CIRCULARITY PRE-TEST [CONJECTURE — preliminary; fine-grained verdict deferred to Doc 130]

The question: the complex structure of the leaves that math/0204111 requires — does it come from the geometry of the space (external, non-circular), or must it be built USING the zeros/values of ζ (circular)?

### 6.1. In the geometric case (curve/function field): the complex structure is EXTERNAL [DATA]

**[DATA].** In math/0204194 (elliptic curve $E/\mathbb F_q$), the complex structure of the leaves $\mathcal F_{\mathcal L}$ (dim_ℂ 1 curves) **comes from the genuine complex geometry of the archimedean place**: there is an ambient Riemann surface $E(\mathbb C)$ (or its analogue in the suspension) whose complex structure the leaf **inherits**. It is **external to the zeta function**: the Riemann structure of $E(\mathbb C)$ exists prior to and without knowing any zero. This is what makes the derived positivity of math/0204111 non-circular **in that case** (Doc 128 §3.1): just as the classical Hodge index is surface geometry, independent of where the points lie. [DATA + COMPUTATION]

### 6.2. For Spec ℤ: there is no archimedean geometry to provide the complex structure [CONJECTURE]

**[COMPUTATION — the point Doc 130 must deepen].** For $\overline{\mathrm{Spec}\,\mathbb Z}$:
- the archimedean place is **a single point** $\infty$ (the real valuation $|\cdot|_\infty$ over $\mathbb Q$), **not a complex curve**. There is no "ambient Riemann surface $X(\mathbb C)$" for the leaf to inherit a complex structure from. (Contrast: for a curve over $\mathbb F_p$, the "constant field" $\mathbb F_p$ and the geometric place give the structure; for $\mathbb Z$, the base field is $\mathbb F_1$, with no genuine complex geometry.)
- Hence **the external source of the complex structure —archimedean geometry— is absent.** There is nowhere to get the leaves' $J$ "for free."

**[CONJECTURE — preliminary reading, the pre-verdict Doc 130 must confirm/refine].**

> *The complex structure of the leaves that math/0204111 requires for Spec ℤ **does not come from external geometry** (there is none: the archimedean place is a point, not a curve). The only known way to manufacture a variation of Hodge structure on the leaves with the **correct eigenvalues** (ζ's zeros in $\bar H^1_{\mathcal F}$) would be to **prescribe the periods/the polarization using the zeros of ζ themselves** — that is, to **inject ζ by hand** into the definition of $J$. That would be the circularity: the complex structure would not be derived from the geometry, but designed so that its Hodge theory reproduces the zeros, turning "positivity ⟹ RH" into "RH ⟹ RH".*

**[COMPUTATION — why this is the same phenomenon as Doc 127, seen from the leaves].** Doc 127 showed that **the flow** of the scaling site carries ζ inside it (its trace is the explicit formula), which is why the dynamical/Forni route is circular. The present pre-test suggests the **dual, from the leaves**: if the flow carries ζ, and the complex structure transverse to the flow must be compatible with it, then the complex structure would inherit the flow's arithmetic content — **unless there is an independent archimedean geometry fixing it, and for Spec ℤ there is none.** Phase 42–43 (Doc 127 §5.3) insisted: *"the positivity must come from the LEAVES, not the flow."* The pre-test says: **for Spec ℤ the leaves have no source of complex structure independent of the flow (= of ζ), because archimedean geometry is missing.** [CONJECTURE — the fine-grained break is certified by Doc 130]

### 6.3. The circularity test applied to the candidate construction

**[COMPUTATION — preliminary].** I apply the spirit of R-NC (Doc 119) to the hypothetical leaf complex structure:
- **NC1 (externality of the definition):** is $J$ defined without mentioning ζ? **In the geometric case YES** (inherited from $X(\mathbb C)$). **For Spec ℤ, doubtful** — there is no external candidate. *Pre-fails.*
- **NC2 (overgeneration):** does the Kähler structure hold for the whole space regardless of the zeros? In the geometric case yes; for Spec ℤ, if $J$ is built from the zeros, **it does not overgenerate** (it only "works" for the true ζ). *Pre-fails.*
- **NC3 (non-reduction to the flow's trace):** the complex structure transverse to the scaling flow — if the flow carries ζ (Doc 127), a compatible $J$ would inherit it. *High risk.*

**[CONJECTURE] Circularity pre-verdict: the complex structure for Spec ℤ is, in the preliminary reading, ζ-dependent (circular), due to the absence of external archimedean geometry. Medium confidence; the fine-grained verdict — including whether some non-obvious external construction exists (e.g., via $\mathbb F_1$ geometry, or a complex solenoid à la 1712.04181 with $J$ from the monodromy) — is left to Doc 130.**

---

## 7. VERDICT

### 7.1. Classification (a)/(b)/(c)/(d)

**[COMPUTATION] Verdict: (c) dominant with (b) — the leaves (in the existing space) have NO complex structure, AND the dimension does NOT close for the square (structural mismatch characterized).**

Breakdown:

- **Can (a) exist and does the dimension close?** **NO.** It would require a foliated space of Spec ℤ with Kähler leaf-surfaces of dim_ℂ 2 and orbits $\{\log p\}$; such a space **does not exist** (not even for dim_ℂ 1; the only realized case is the elliptic curve), and even if it existed, its leaf would be of dim_ℂ $\le1$ (Deninger's space is the analogue of $X$, not of $X\times X$). Not (a).

- **Does (b) the dimension NOT close (structural mismatch)?** **YES, precisely characterized (§5).** A triple nested mismatch: (i) Morishita has leaves of dim_ℂ 0 (no complex structure); (ii) the geometric case has leaves of dim_ℂ 1 (curve), but the square needs dim_ℂ 2 (surface) — one dimension is missing; (iii) **the square is NOT a leaf but the product of the total space $X\times X$**; the identification square↔factor requires Künneth, which does not exist tropically.

- **Do (c) the leaves lack complex structure?** **YES, literally for the space that exists today (Morishita).** Its leaves are real of dim 0; there is no $J$, no foliated Hodge theory. Deninger's polarizable Hodge theory (math/0204111) **does not apply to Morishita's space.** [§2.4]

- **Is it (d) undeterminable?** **NO.** The status IS determinable: for the existing space, the leaves are real (c); for any space that would give the square, the dimension does not close (b). The only genuinely open question is whether a new space with Kähler leaf-surfaces external to ζ *could* be built — and the pre-test (§6) suggests NO (archimedean geometry is missing), pending Doc 130.

> **COMPOSITE VERDICT: (c)+(b).** *The foliated space of Spec ℤ that exists today (Morishita 2508.15971) **does not admit a foliated polarizable Hodge structure** because its leaves are real of dimension 0, not Kähler complex manifolds (c). Even postulating a space with complex leaves, **the dimension does not close for the square of Doc 125**: Deninger's leaf is a curve (dim_ℂ 1, symplectic $H^1$), the square is a surface (dim_ℂ 2, Hodge-index $H^2$), and the square corresponds to the **product $X\times X$, not to a leaf**; the Künneth bridge that would identify them does not exist tropically (b).*

### 7.2. Contrast with Doc 128's verdict (a)

**[COMPUTATION].** Doc 128 gave verdict **(a) non-circular, conditional on Kähler–Riemann**, about the **logical status of Deninger's program in the abstract**. Doc 129 is finer and more severe: **when requiring that the concrete space (Morishita) have the Kähler structure that Doc 128's condition requires, the condition FAILS** — the leaves are real of dim 0. Doc 128's non-circularity was *conditional on a space that does not exist with the correct structure*. Doc 129 shows that **the condition is not met in the only realized space**, and that even if it were met the dimension would not match the square. **Doc 128's verdict (a) was correct about the formalism; Doc 129's (c)+(b) is the verdict about the concrete realization.**

### 7.3. List of what would be missing (in order of difficulty)

1. **[GAP, decisive]** Build a foliated space of $\overline{\mathrm{Spec}\,\mathbb Z}$ with **leaves that are Kähler complex manifolds** (not real of dim 0). It does not exist today; Morishita gives real profinite leaves. The spectral rigidity obstruction (1712.04181) blocks simple constructions.
2. **[GAP, dimensional]** That those leaves be of the **correct complex dimension** for the object giving the signature. If the content lives in $\bar H^1_{\mathcal F}$ (Deninger's program), leaves of dim_ℂ 1 (curves) — but then the signature is symplectic $(g,g)$, not the square's Hodge index $(1,\rho-1)$; one must **decide in what degree and dimension RH-positivity really lives** and reconcile with Doc 125.
3. **[GAP, Künneth]** A tropical Künneth analogue / a Hodge-index-over-the-square ⟺ polarization-over-the-factor duality that works in characteristic 1/over the scaling site, to identify the square (dim 2) with the leaf (dim 1). Doc 123 declared it nonexistent tropically.
4. **[GAP, circularity — to Doc 130]** A source **external to ζ** of the leaves' complex structure for Spec ℤ. The pre-test (§6) suggests there is none (archimedean geometry is missing: the archimedean place is a point, not a curve). If confirmed, the complex structure would be ζ smuggled in by hand = circular = the anticipated result.

---

## 8. Honesty and record

No new theorem was proved. What was **read from source** was: math/0204111 via ar5iv (definition of Kähler–Riemann foliation, Kähler leaves of dim_ℂ $g$, Hard Lefschetz Prop. 4.3, polarization Prop. 4.4, positivity $Q(\xi,J\bar\xi)>0$, origin in the Álvarez López–Kordyukov decomposition); math/0204194 via ar5iv (the elliptic curve example, leaves $\mathcal F_{\mathcal L}$ = dim_ℂ 1 complex curves, explicit formula = transverse index); Morishita 2508.15971 via HTML ($\mathfrak X_K=\check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+$, profinite transversal dim 0, real leaves, **no complex structure**, anti-equivariant map $\Psi_F$); WebSearch (the definition of foliated complex structure and confirmation that the space for Spec ℤ still has not been built) — and **the dimensional dictionary with the square of Doc 125 was computed**.

**The central point:**
- **math/0204111 proves** that for Kähler–Riemann foliations (Kähler leaves of dim_ℂ $g$), the reduced foliated cohomology carries Hard Lefschetz + a polarizable Hodge structure + Hodge–Riemann positivity; **the positivity comes EXACTLY from the classical Hodge polarization of each compact Kähler leaf, averaged transversally.** The "Kähler leaves" hypothesis is inflexible.
- **Morishita's space** has a **profinite (dim 0)** transversal and the only continuous direction is the **flow $\mathbb R_+$**; its leaves are **real of dim 0, WITHOUT complex structure**. Deninger's foliated Hodge theory **does not apply.** **First break: (c).**
- **The dimension does NOT close for the square:** Deninger's leaf (in the only realized case) is a **curve (dim_ℂ 1, symplectic $H^1$)**; the square of Doc 125 is a **surface (dim_ℂ 2, Hodge index $H^2$ $(1,2)$)**; and the square corresponds to the **product $X\times X$, NOT to a leaf**. The bridge (Künneth) does not exist tropically. **Second break: (b).**
- **Circularity pre-test:** for Spec ℤ there is no archimedean geometry (the archimedean place is a point, not a curve) for the leaves to inherit an external complex structure from; the candidate is **ζ smuggled in by hand** = circular. **[CONJECTURE, deferred to Doc 130.]**

**The obstruction IS the result:** Doc 128 declared Deninger's framework *non-circular, conditional on Kähler–Riemann*. Doc 129 shows that **the Kähler–Riemann condition FAILS in the only realized space (Morishita: real leaves of dim 0)**, and that **even forcing it, the dimension does not match the square** (dim-1 curve vs. dim-2 surface; leaf vs. product; no Künneth). **Verdict: (c)+(b)** — the existing space's leaves are not complex, and the square lives at a dimension and level (product, dim 2) that no Deninger leaf (dim $\le1$) realizes. The missing piece —a space for Spec ℤ with Kähler leaves of the correct dimension, with complex structure **external to ζ**— does not exist, and the pre-test suggests its complex structure would be ζ-dependent. Doc 130 will render the fine-grained circularity verdict.

---

## References

**External source read this session, via WebFetch/WebSearch):**
- C. Deninger, W. Singhof, *Real polarizable Hodge structures arising from foliations*, arXiv:math/0204111 (via ar5iv) — **definition of Kähler–Riemann foliation** (Kähler leaves of dim_ℂ $g$, bundle-like Riemannian foliation); **Prop. 4.3** foliated Hard Lefschetz $L^{g-r}:\bar H^r_{\mathcal F}\xrightarrow{\sim}\bar H^{2g-r}_{\mathcal F}$; **Prop. 4.4** $Q$ polarizes the real Hodge structure of weight $r$ over $P^r_{\mathcal F}$; **positivity $Q(\xi,J\bar\xi)>0$**; origin in the **smooth Hodge decomposition of Álvarez López–Kordyukov** (classes = forms harmonic along the leaves). **[DATA]**
- C. Deninger, W. Singhof, *On the nature of the explicit formulas in analytic number theory — a simple example*, arXiv:math/0204194 (via ar5iv) — the space $X=\tilde X/H$, $\tilde X=\mathbb C\times V_\xi\Gamma\times\mathbb R$, 3-dim real; leaves $\mathcal L$ real of dim 3 with sub-foliation $\mathcal F_{\mathcal L}$ whose **leaves are dim_ℂ 1 complex curves (Riemann surfaces)**, rank-2 tangent bundle; explicit formula $=\mathrm{Ind}_t(d_{\mathcal F_{\mathcal L}})$ transverse index; generalized solenoid. **[DATA — the only realized geometric case, dim_ℂ 1 leaf.]**
- M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*, arXiv:2508.15971 (2025, via HTML) — $\mathfrak X_K=\check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+$; **transversal $\check X_K(\mathbb C)$ totally disconnected/profinite (dim 0)**; leaves = images of $\check X_K(\mathbb C)\times\{u\}$, **real, WITHOUT complex or Kähler structure**; flow $\phi^t$ Frobenius; closed orbits $\gamma_{\mathfrak p}$ circles of length $\log N\mathfrak p$; bundle $\Gamma_{\mathfrak p}$ = mapping torus; $\Psi_F$ $\mathbb R_+$-anti-equivariant, NOT iso. **[DATA — the existing space does NOT have complex leaves.]**
- arXiv:1712.04181, *On the leafwise cohomology and dynamical zeta functions for fiber bundles over the circle* — infinite-dimensional foliated cohomology; spectral rigidity (the generator's spectrum forced by the monodromy); the space for Spec ℤ still has not been built. **[DATA, via abstract + Doc 128.]**
- J. A. Álvarez López, Y. A. Kordyukov — smooth Hodge decomposition theorem for Riemannian foliations (reference [1] of math/0204111). **[DATA, via math/0204111.]**
- WebSearch: confirmation that (i) the complex structure of a foliation = an almost-complex $J$ on $T\mathcal F$ with integrable restrictions to the leaves, which carry holomorphic structures varying smoothly transversally; (ii) the foliated space for Spec ℤ **still has not been built** (only the elliptic curve, 2002). **[DATA]**

**Internal (backward-only):** Doc 119 (R-NC NC1–NC4; T2 signatures not continuous under limits; R-LEF-FLOW); Doc 123 (tropical Künneth does not exist; the factors $C_p$ have no $H^1$); Doc 124 (G2 = indefinite Hodge index $(1,\rho-1)$; CC's positivity spectral = circular); Doc 125 ($C_p\times C_p$; $G_{\text{toy}}$ signature $(1,2)$, negative-definite primitive; G-125.A real/integer; G-125.B persistence à la Babaee–Huh); Doc 127 (the dynamical/Forni route is circular: the scaling flow carries ζ inside it; the positivity must come from the LEAVES, not the flow); Doc 128 (Deninger's program; verdict (a) non-circular *conditional on Kähler–Riemann*; math/0204111 is the derived-positivity theorem; Morishita gives space+flow not the cohomology; the unified meta-object).

*End of Document 129.*
