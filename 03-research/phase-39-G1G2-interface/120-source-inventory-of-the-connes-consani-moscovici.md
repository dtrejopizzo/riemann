# Doc 120 — Source inventory of the Connes–Consani(–Moscovici) machinery

**Phase 39 — G1↔G2 interface..**

---

## §0. Purpose, method and labeling discipline

This document catalogues, reading from the source (arXiv), **what structures exist today** in the
Connes–Consani(–Moscovici) program [hereafter CC / CCM], with precise statements, to
measure them afterward against the program roadmap's "shopping list"
(`06-papers/roadmap-rh/roadmap-rh.tex`): nodes **G1** (finite-dimensional cohomology
on the square of the scaling site), **G2** (weight/signature structure — *the wall*),
**G3** (Lefschetz formula = explicit formula), **G4** (a priori bound
$\kappa(Q) = 2m < \infty$), and specification **S1–S3** (finiteness of *signature*, not
Euler characteristic; autonomous arithmetic traces; unconditionality).

**Labeling discipline (absolute rule of this document):**

- **[VERIFIED]** — read in the source in this session, via arXiv
  (abs page, ar5iv, or the paper's HTML), with exact citation of paper and section/theorem.
  *Declared methodological caveat:* the reading was done via assisted extraction of
  the source text; the textual quotations reproduced below come from the paper's text
  as extracted. Theorem numbers and statements are reported as they
  appear in the extracted source.
- **[PREVIOUSLY VERIFIED — Doc 100]** — verified against the complete source in the
  Doc 100 session, reused here with its original citation.
- **[UNVERIFIED]** — from memory, from a secondary source, or not found in the source in
  this session.
- **[INTERPRETATION]** — a reading of mine/of the program; it is **not** a claim by CC.

**Sources read in this session** (all accessed:

| arXiv | Exact title | Status |
|---|---|---|
| 1405.4527 | *The Arithmetic Site* | abs read |
| 1502.05580 | *Geometry of the arithmetic site* | abs + full text (ar5iv) |
| 1507.05818 | *The Scaling Site* | abs read |
| 1603.03191 | *Geometry of the scaling site* | abs + full text (ar5iv) |
| 1509.05576 | *An essay on the Riemann Hypothesis* (Connes alone) | text (ar5iv), passages on the RR strategy |
| 1805.10501 | *The Riemann-Roch strategy, Complex lift of the Scaling Site* | text (ar5iv) |
| 2205.01391 | *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$* | abs + text (ar5iv) |
| 2306.00456 | *Riemann-Roch for the ring $\mathbb Z$* | abs + text (ar5iv) |
| 2602.15941 | *On the Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$* | text (arXiv HTML v1) |
| 2006.13771 | *Weil positivity and Trace formula, the archimedean place* | abs + text (ar5iv); also Doc 100 |
| 2310.18423 | *Zeta zeros and prolate wave operators* (CCM) | abs; text verified in Doc 100 |
| 2511.22755 | *Zeta Spectral Triples* (CCM) | abs + text (arXiv HTML v1) |
| 2602.04022 | *The Riemann Hypothesis: Past, Present and a Letter Through Time* (Connes) | abs + text (arXiv HTML v1) |
| 2008.10974 | *Quasi-inner functions and local factors* | [PREVIOUSLY VERIFIED — Doc 100] |

Corrections to the target's references: semilocal positivity is **not** in
2310.18423 (that is the paper on semilocal prolate operators, and positivity for
$|S|\ge 2$ remains a declared strategy, not a theorem — see §4 and §5);
"Riemann-Roch for Spec Z̄" is **arXiv:2205.01391** (v2 March 2023, published — the
search returns the journal version via Bull. Sci. Math. on ScienceDirect
[UNVERIFIED the exact bibliographic datum of the journal]); there is a second paper,
**arXiv:2306.00456**, that improves the formula; "On the Jacobian of Spec Z̄" **exists**:
**arXiv:2602.15941**. Connes's "letter" is **arXiv:2602.04022**
(submitted to the Journal of Open Mathematical Problems on 2025-09-19, posted 2026-02-03).

---

## §1. Piece 1 — THE ARITHMETIC SITE

### 1.1 Verified references

- A. Connes, C. Consani, *The Arithmetic Site*, arXiv:1405.4527 (May 2014; CRAS note).
  **[VERIFIED]** (abs).
- A. Connes, C. Consani, *Geometry of the arithmetic site*, arXiv:1502.05580
  (February 2015; Adv. Math. according to program memory [UNVERIFIED the journal
  datum in this session — the abs page does not list it]). **[VERIFIED]** (full text).

### 1.2 Defined objects

1. **The topos $\widehat{\mathbb N^\times}$**: the topos of sets with an action of the
   multiplicative monoid $\mathbb N^\times$ of nonzero positive integers (functors
   $\mathbb N^\times \to \mathfrak{Sets}$). **[VERIFIED]** (1502.05580, abstract:
   *"The underlying topological space of the arithmetic site is the topos of functors
   from the multiplicative semigroup of non-zero natural numbers to the category of
   sets"*).
2. **The structure sheaf $\mathbb Z_{\max} := (\mathbb Z \cup \{-\infty\}, \max, +)$**,
   a semiring of characteristic 1 (the "tropical integers"), with $\mathbb N^\times$
   acting by **Frobenius endomorphisms** $\mathrm{Fr}_n(x) = nx$. **[VERIFIED]**
   (1502.05580, Definition 3.1, textual: *"The arithmetic site
   $(\widehat{\mathbb N^\times}, \mathbb Z_{\max})$ is the topos
   $\widehat{\mathbb N^\times}$ endowed with the structure sheaf
   $\mathcal O := \mathbb Z_{\max}$ viewed as a semiring in the topos using the action
   of $\mathbb N^\times$ by the Frobenius endomorphisms"*).
3. **The semifield $\mathbb R_+^{\max}$** (tropical reals) with its group of
   Frobenius automorphisms $\mathrm{Fr}_\lambda$, $\lambda \in \mathbb R_+^*$.
   **[VERIFIED]** (ibid., Theorem 1.1 and abstract).

### 1.3 Main theorems

- **Theorem (points over $\mathbb R_+^{\max}$).** Textual (1502.05580, Theorem 1.1):
  *"The set of points of the arithmetic site over $\mathbb R_+^{\max}$ coincides with
  the quotient of $\mathbb A_{\mathbb Q}/\mathbb Q^\times$ by the action of
  $\hat{\mathbb Z}^\times$. The action of the Frobenius automorphisms
  $\mathrm{Fr}_\lambda$ of $\mathbb R_+^{\max}$ on these points corresponds to the
  action of the idèle class group."* **[VERIFIED]**.
  That is: the points of the countable combinatorial object
  $(\widehat{\mathbb N^\times}, \mathbb Z_{\max})$ over the tropical semifield
  **are** the adele class space modulo the maximal compact subgroup, and the scaling
  flow (the action of $\mathbb R_+^* \subset C_{\mathbb Q}$ whose fixed-point spectrum
  gives the zeros of $\zeta$ in Connes's 1999 trace) **is** Frobenius.
- **Theorem (semigroup of Frobenius correspondences).** Textual (1502.05580,
  Theorem 1.2 / §6): there exist correspondences $\Psi(\lambda)$, $\lambda \in \mathbb R_+^*$,
  subvarieties of the square of the site, such that *"for
  $\lambda, \lambda' \in \mathbb R_+^\times$ such that $\lambda\lambda' \notin \mathbb Q$,
  one has $\Psi(\lambda) \circ \Psi(\lambda') = \Psi(\lambda\lambda')$."*
  **[VERIFIED]**. Note the condition $\lambda\lambda' \notin \mathbb Q$: the composition
  law is as expected **only generically**; at rational values there is a
  discontinuity phenomenon ("the law of composition... holds unconditionally only up
  to a subtlety" — paraphrase; the exact conditional statement is the one quoted).
  Matches what is recorded in Doc 106 §3.3 **[PREVIOUSLY VERIFIED — Doc 106]**.
- **The square of the site already appears here**: the non-reduced square carries the
  structure sheaf $\mathbb Z_{\min} \otimes_{\mathbb B} \mathbb Z_{\min}$, and in the
  reduced square the sections are **Newton polygons** with convex-hull
  operations. And (1502.05580, Proposition 6.11, textual): *"The points of the square of the
  arithmetic site over $\mathbb R_+^{\max}$ coincide with the product of the points of
  the arithmetic site over $\mathbb R_+^{\max}$."* **[VERIFIED]**. See §6.

### 1.4 What is NOT there

- No cohomology of the site (neither $H^0$ nor $H^1$ of sheaves over
  $\widehat{\mathbb N^\times}$) is defined in these papers. **[VERIFIED — evident from
  the statement: the papers define a topos, a sheaf, points and correspondences; there is no
  cohomological theory]**.
- No bilinear form, pairing or intersection theory on the square: the
  $\Psi(\lambda)$ compose but do not intersect. **[VERIFIED — evident]**.
- The Frobenius composition law at rational values is not exact (condition
  $\lambda\lambda' \notin \mathbb Q$). **[VERIFIED]**.

---

## §2. Piece 2 — THE SCALING SITE

### 2.1 Verified references

- A. Connes, C. Consani, *The Scaling Site*, arXiv:1507.05818 (July 2015; CRAS note).
  **[VERIFIED]** (abs).
- A. Connes, C. Consani, *Geometry of the scaling site*, arXiv:1603.03191 (March 2016;
  Selecta Math. according to memory [UNVERIFIED journal]). **[VERIFIED]** (text).

### 2.2 Defined objects

1. **The scaling site** $\mathscr S = ([0,\infty) \rtimes \mathbb N^\times, \mathcal O)$:
   a scalar extension of the arithmetic site over $\mathbb B$ to $\mathbb R_+^{\max}$;
   the semi-direct-product topos of the Euclidean half-line by the multiplicative
   action of $\mathbb N^\times$. Structure sheaf: *"convex, piecewise affine functions with
   integral slopes"*, with values in $\mathbb R_{\max}$ (sum = max, product = +).
   **[VERIFIED]** (1603.03191, abstract and §2).
2. **Points** = again the adele class space
   $\mathbb A_{\mathbb Q}/\mathbb Q^\times$ modulo $\hat{\mathbb Z}^\times$, which now
   **inherits a tropical curve structure** from the topos. **[VERIFIED]** (abstract).
3. **The periodic orbits $C_p = \mathbb R_+^*/p^{\mathbb Z}$**, one for each prime
   $p$: quasi-tropical circles, characteristic-1 analogues of the Jacobi
   uniformization $E = \mathbb C^*/q^{\mathbb Z}$ of elliptic curves. Sheaf $\mathcal O_p$:
   periodic functions $f(p\lambda) = f(\lambda)$, convex, piecewise affine, with
   slopes in $H_p \subset \mathbb Q$ (rationals with denominator a power of $p$).
   **[VERIFIED]** (1603.03191, §3; 1507.05818 abstract).
4. **Cartier divisors on $C_p$**, real degree, theta functions. **[VERIFIED]**.

### 2.3 Main theorems

- **Group of divisor classes** (1603.03191, Theorem 5.6 in the extracted text's
  numbering): the pair (degree, torsion character) induces an isomorphism
  $$\mathrm{Div}(C_p)/\mathcal P \;\xrightarrow{\;(\deg,\chi)\;}\; \mathbb R \times \mathbb Z/(p-1)\mathbb Z.$$
  **[VERIFIED]**. In 1507.05818 (abstract) they state it as: the periodic orbits
  give analogues of elliptic curves *"whose Jacobians are cyclic groups of order $p-1$"*
  — i.e., $J(C_p) = (\mathrm{Div}^0/\mathcal P) \cong \mathbb Z/(p-1)\mathbb Z$.
  **[VERIFIED]** (abs). The degree is **real**, not an integer (reflecting $H_p$).
- **Theta functions** (1603.03191, §5): one constructs
  $\theta(\lambda) = \sum_{m\ge 0} (0 \vee (1 - p^m \lambda)) + \sum_{m\ge 1} (0 \vee (p^{-m}\lambda - 1))$
  (an infinite tropical sum, not a product), and (Theorem 5.12 of the extracted text) every
  rational function on $C_p$ is expressed in finite combinations of thetas
  $\Theta(h,\mu)$ plus linear and constant terms. **[VERIFIED]**.
- **Tropical Riemann–Roch on $C_p$** — see Piece 3, §3.1.

### 2.4 What plays the role of genus?

- **There is no genus term in their RR formula on $C_p$** (see §3.1): the formula is
  exactly $\dim_{\mathbb R} H^0(D) - \dim_{\mathbb R} H^0(-D) = \deg D$.
  **[VERIFIED]** (1603.03191, Theorem 5.17 of the extracted text).
- **[INTERPRETATION]**: the shape of the formula is that of an **elliptic**
  curve ($g = 1$, $K = 0$): on a classical elliptic curve
  $\ell(D) - \ell(K - D) = \deg D$ with $K = 0$, so that the substitute for Serre
  duality here is the involution $D \mapsto -D = K - D$ with a **trivial canonical
  divisor**. This is consistent with CC's declared analogy ($C_p$ as the analogue of
  $\mathbb C^*/q^{\mathbb Z}$) and with $J(C_p)$ a finite cyclic group (analogous to the
  points of an elliptic curve over $\mathbb F_p$... in fact $|J(C_p)| = p - 1 = $ the
  number of points of $\mathbb G_m(\mathbb F_p)$ — which rather suggests a "multiplicative"
  genus). CC do **not** call this Serre duality in this paper. **[VERIFIED that the paper
  does not develop Serre duality or bilinear pairings — evident from the text]**.

### 2.5 What is NOT there

- $H^1$ cohomology of sheaves: the RR uses only $H^0$ and the involution $D \mapsto -D$.
- Intersection theory on $C_p \times C_p$ or on $\mathscr S \times \mathscr S$.
- No bilinear pairing. **[VERIFIED — evident]**.
- What is declared open (abstract/Introduction): extending characteristic-1 geometry
  to capture the full zeta function; transplanting the proof of RH from function fields.
  **[VERIFIED]** (paraphrase of the extracted text).

---

## §3. Piece 3 — RIEMANN–ROCH: tropical, absolute, and the 2026 Jacobian

This is the piece where the target asked for maximum precision. There are **four**
distinct RR theorems in the CC corpus, of increasing strength:

### 3.1 Tropical RR on the periodic orbit $C_p$ (1603.03191)

- **Cohomologies**: only $H^0(D) := \{f$ rational $: D + (f) \ge 0\}$ (modulo
  the idempotent, not a vector space). **There is no $H^1$**: its role is played by
  $H^0(-D)$.
- **Dimension**: **continuous, real-valued**, defined as a normalized limit
  $$\mathrm{Dim}_{\mathbb R}(H^0(D)) := \lim_{n\to\infty} p^{-n} \dim_{\mathrm{top}}(H^0(D)^{(p^n)}),$$
  textually from the paper (filtration by the slopes $p^{-n}$). CC themselves point out the
  analogy with **type II continuous von Neumann dimension**. **[VERIFIED]**
  (1603.03191, §5; the type II analogy is in the text).
- **Formula** (Theorem 5.17, textual): *"$\mathrm{Dim}_{\mathbb R}(H^0(D)) -
  \mathrm{Dim}_{\mathbb R}(H^0(-D)) = \deg(D), \;\forall D \in \mathrm{Div}(C_p)$."*
  **[VERIFIED]**. $\chi = \deg$, with no genus term, real-valued degrees and dimensions.
- **What is NOT there**: Serre duality with a non-trivial dualizing sheaf; integers (everything is
  real-valued — exactly what S1/G2 of the roadmap diagnoses as insufficient:
  *averages, not integers*). **[VERIFIED — evident]** + **[INTERPRETATION]** the
  S1 reading.

### 3.2 RR for $\overline{\mathrm{Spec}\,\mathbb Z}$ over $\mathbb S[\pm 1]$ (arXiv:2205.01391, v2 2023)

The qualitative leap: **integer** dimensions and **genuine Serre duality**.

- **Absolute base**: $\mathbb S[\pm 1]$, the spherical semiring $\{0, \pm 1\}$, formalized
  with **Segal's $\Gamma$-rings** (functors $\Gamma^{op} \to \mathfrak{Sets}_*$);
  building on their earlier theory of "universal arithmetic over the sphere spectrum".
  **[VERIFIED]** (textual abstract: *"Both the definitions of the cohomologies and of
  their dimensions rely on a universal arithmetic theory over the sphere spectrum that
  we had previously introduced using Segal's Gamma rings"*).
- **$H^0(D)$**: for an Arakelov divisor $D$ with archimedean part $a$, the
  $\mathbb S[\pm 1]$-module $\|H\mathbb Z\|_{e^a}$ — textual: *"associates to a finite
  pointed set $X$ the $\mathbb Z$-valued divisors $\sum_i n_i x_i$... fulfilling
  $\sum_i |n_i| \le e^a$"*; it is the **kernel** of the morphism
  $\psi: H\mathbb Q \times H\mathcal O(D) \to H\mathbb A_{\mathbb Q}$ (an exact
  parallel of Weil's adelic proof for function fields). **[VERIFIED]**.
- **$H^1(D)$**: the **cokernel** of $\psi$, defined as an **$\mathbb S$-module with
  tolerance** (the pair $(H\mathbb A_{\mathbb Q}, \mathcal R)$ with
  $\mathcal R_k := \{(x,y) : x - y \in \mathrm{Image}\,\psi(k_+)\}$), via Dold–Kan
  applied to the short complex $\psi$. **[VERIFIED]**. *This is the first $H^1$ that CC
  manage to define in the whole program* — compare with the obstacle declared in
  1805.10501 (§6.3 below). **[INTERPRETATION]** the comparison; **[VERIFIED]** both
  extremes.
- **Integer dimension**: $\dim_{\mathbb S[\pm1]} H^0(D)$ := minimum number of
  **linear generators** (with coefficients in $\{-1,0,1\}$ and norm control
  $\sum |\alpha(f) f| \le e^a$); analogously, with the tolerance relation, for
  $H^1$. **[VERIFIED]**.
- **RR formula** (Theorem 1.1, textual from the extracted text):
  $$\dim_{\mathbb S[\pm1]} H^0(D) - \dim_{\mathbb S[\pm1]} H^1(D) = \big\lceil \deg' D + \log' 2 \big\rceil' - \mathbb 1_L,$$
  with $\deg' = \deg/\log 3$, $\log' 2 = \log 2/\log 3$, $\lceil\cdot\rceil'$ the
  odd extension of the ceiling function, and $\mathbb 1_L$ an indicator function of an
  exceptional set $L$ (a countable union of intervals
  $(\log'(3^k/2), \log'((3^k{+}1)/2))$). **[VERIFIED]**.
- **SERRE DUALITY — exists and is a theorem** (Theorem 1.2, textual):
  $$H^0(K - D) \simeq \overline{\mathrm{Hom}}_{\Gamma \mathcal T_*}\big(H^1(D),\, U(1)_{1/4}\big),$$
  with **canonical divisor $K = -2\{2\}$** ($\deg K = -2\log 2$) and **dualizing
  module $U(1)_{1/4} = H^1(K)$**. The duality *"derives from Pontryagin duality for tolerance
  $\mathbb S[\pm1]$-modules"* (Proposition 5.2), *"paralleling Weil's adelic
  construction for function fields"* (abstract: *"including the use of Pontryagin
  duality"*). **[VERIFIED]**.
- **Direct answer to the target's question (is there a bilinear form/pairing?):**
  YES, a pairing exists in their theory: the **Pontryagin duality** pairing
  $H^1(D) \times H^0(K-D) \to U(1)$ underlying Theorem 1.2. It is a perfect
  duality pairing **between distinct spaces** ($H^1$ against $H^0$ of the
  dual divisor), **not** a symmetric bilinear form on a single space, and it
  carries **no** notion of signature/inertia index. **[VERIFIED]** the theorem;
  **[INTERPRETATION]** the classification relative to G2.

### 3.3 RR for the ring $\mathbb Z$ over $\mathbb S$ (arXiv:2306.00456, June 2023)

- Working over the absolute base $\mathbb S$ (the categorical version of the sphere
  spectrum) instead of $\mathbb S[\pm 1]$ **improves** the formula: the exceptional term
  disappears — textual: *"The term $\mathbb 1_L$ involving the exceptional set $L$ in
  the earlier formula is now eliminated."* **[VERIFIED]**.
- **Formula** (Theorem 1.1, textual): $\dim_{\mathbb S} H^0(D) - \dim_{\mathbb S} H^1(D)
  = \lceil \deg_2 D \rceil' + 1$, with $\deg_2 = \deg/\log 2$. For $\deg_2 D \ge 0$:
  $H^1 = 0$ and $\dim H^0 = \lceil \deg_2 D \rceil + 1$. **[VERIFIED]**.
- **Genus analogy they declare**, textual: *"(1.1) displays a perfect
  analogy with the Riemann-Roch formula holding for curves of genus 0."* That is:
  according to CC, $\overline{\mathrm{Spec}\,\mathbb Z}$ over $\mathbb S$ behaves like
  **a genus-0 curve** ($\chi = \deg + 1$), with $\mathbb Z = \mathbb S[X]$,
  "$1+1 = X + X^2$" with generator $-2$, and $K = -2\{2\}$ of integer degree
  $\deg_2 K = -2$ (like $K_{\mathbb P^1}$). **[VERIFIED]** (both quotes and the
  $K$ datum); the reading "$\{2\}$ plays the role of the point at infinity of
  $\mathbb P^1$" is **[INTERPRETATION]**.
- **Explicit $H^1$**: $H^1(D) \simeq (U(1), d)_\lambda$ with $U(1) = \mathbb R/\mathbb Z$
  metrized and $\lambda = e^{\deg D}$; $\dim_{\mathbb S} U(1)_\lambda = m$ if
  $2^{-m-1} \le \lambda < 2^{-m}$ (Proposition 4.2 of the extracted text). **[VERIFIED]**.
- **What is NOT there**: the extracted text contains no separate Serre-duality
  statement in this paper (the duality is that of paper 2205.01391); there is no mention
  of the square nor of dimension 2 as a declared next step. **[VERIFIED — with the
  extraction caveat]**.

### 3.4 The Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$ (arXiv:2602.15941,

**The paper exists** — confirmed in the source (arXiv HTML v1) and in the publication
list of Consani (math.jhu.edu/~kc/Publ2026.pdf). **[VERIFIED]**.

- **Abstract** (textual, according to the source): *"We interpret the structure of the adele class
  space of the rationals—and specifically its Riemann sector—as the natural monoidal
  extension of the Picard group of the arithmetic curve $\overline{\mathrm{Spec}\,\mathbb Z}$.
  We identify the elements of this space with torsion-free rank-1 abelian groups $L$
  endowed with rigidifying data."* **[VERIFIED]**.
- **Objects**: the **Picard monoid** $\mathrm{Pic}(\overline{\mathrm{Spec}\,\mathbb Z})$
  = moduli of $(L, \|\cdot\|)$ with $L$ a torsion-free rank-1 abelian group and
  $\|\cdot\|$ a **semi**-norm on $L \otimes \mathbb R$ (extending Arakelov's metrized
  line bundles while **allowing norm degeneration**); the **arithmetic
  Jacobian** = the quotient by the scaling action $\mathbb R_+^\times$;
  the **Riemann sector** $X_{\mathbb Q} = \mathbb Q^\times \backslash \mathbb A /
  \hat{\mathbb Z}^\times$. **[VERIFIED]**.
- **Theorem 1.1** (textual according to the source): the assignment $a \mapsto (L_a, \|\cdot\|_a)$
  induces *"a canonical monoid isomorphism
  $X_{\mathbb Q} \cong \mathrm{Pic}(\overline{\mathrm{Spec}\,\mathbb Z})$"*; with an
  explicit realization $L_a = \{q \in \mathbb Q : a_f q \in \hat{\mathbb Z}\}$,
  $\|v\|_a = |a_\infty| |v|$ (Theorem 3.4 of the extracted text). There is also a
  uniformization (Theorem 1.4): a monoid isomorphism between the adelic monoid
  $Y_{\mathbb Q}$ and the moduli of **framed** arithmetic divisors $(L, \xi, \tau)$,
  with the adele product = the tensor product of frames. **[VERIFIED]**.
- **Spectral realization** (§9 of the paper): the translation action of the idele
  class group $C_{\mathbb Q}$ on $\widetilde{\mathrm{Pic}}$ produces a Lefschetz-type
  trace formula whose contributions localize on periodic orbits;
  a divergent term $2h(1)\log\lambda$ remains in the semilocal formula whose
  rigorous treatment is pending (§9.3). **[VERIFIED]** (according to the extracted text).
- **Key closing sentence** (textual according to the source): the step from Picard groups to
  **monoids** *"is not merely a generalization. Rather, it is a necessary step for
  incorporating boundary and singular phenomena into the geometric framework—precisely
  the features required for the spectral realization."* **[VERIFIED]**.
- **What is NOT there** (verified by searching the extracted text): **no mention**
  of intersection theory, the square of the site, Hodge index, Weil positivity,
  nor RH as a direct goal of the paper. **[VERIFIED — with the extraction caveat]**.

### 3.5 Synthesis of Piece 3 for the G1↔G2 interface

**[INTERPRETATION]** (mine, for the program): the CC RR corpus today has a
**fork of virtues with no intersection**: (i) tropical RR (3.1) lives on the
scaling site — the natural carrier of G1 — but with **real** dimensions (type II)
and no $H^1$ or duality; (ii) absolute RR (3.2–3.3) has **integers, $H^1$, a canonical
divisor and Serre/Pontryagin duality** — exactly the kind of structure G2
calls for — but it lives on $\overline{\mathrm{Spec}\,\mathbb Z}$ in dimension 1, **not**
on the square, and its duality is a duality pairing (perfect,
$H^1 \times H^0 \to U(1)$), not a form with signature. The Jacobian paper (3.4) is
the declared bridge between the adelic-spectral side and the Picard-geometric side, in
dimension 1. **Nobody has yet crossed "absolute RR" with "the square".**

---

## §4. Piece 4 — WEIL POSITIVITY

### 4.1 Verified references

- A. Connes, C. Consani, *Weil positivity and Trace formula, the archimedean place*,
  arXiv:2006.13771; Selecta Math. 27, 77 (2021). **[VERIFIED]** (abs + text;
  also full text in Doc 100).
- A. Connes, C. Consani, *Quasi-inner functions and local factors*, J. Number Theory
  226 (2021) 139–167; arXiv:2008.10974. **[PREVIOUSLY VERIFIED — Doc 100]**.
- CCM, *Zeta zeros and prolate wave operators*, Ann. Funct. Anal. 15 (2024);
  arXiv:2310.18423. **[VERIFIED]** (abs; text in Doc 100). — **This paper does NOT prove
  semilocal positivity**; it is the semilocal prolate infrastructure.

### 4.2 What exact positivity do they prove

- **Theorem 1 of CC 2021** (textual according to the source): for test functions
  $g \in C_c^\infty([2^{-1/2}, 2^{1/2}])$ (support in the window $(1/2,2)$ after
  convolution, i.e., a single visible archimedean place) with $\hat g(i/2) = \hat g(0) = 0$:
  $$W_\infty(g * g^*) \;\ge\; \mathrm{Tr}\big(\vartheta(g)\,\mathbf S\,\vartheta(g)^*\big) \;\ge\; 0,$$
  where $\vartheta$ is the scaling action on $L^2(\mathbb R)^{\mathrm{ev}}$ and
  $\mathbf S$ is the projection onto the **Sonine space** (orthogonal complement of the
  range of the cutoff projections $\mathcal P_1 \vee \widehat{\mathcal P}_1$,
  parameter $\Lambda = 1$). **[VERIFIED]** (matches what was verified in Doc 100 §2).
- **Quantitative form** (Theorem 6.11 according to the extracted text): there exists a finite
  $c$, $13 < c < 17$, with $W_\infty(g * g^*) \ge \mathrm{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)
  - c\,|\hat g(0)|^2$ — a **single direction of conditioning** $\hat g(0)$ with a
  finite-rank defect. CC's phrase about the extra contribution on the critical line:
  *"as if one would multiply $\zeta(z)$ by $(z - 1/2)^{17}$"*. **[VERIFIED]**
  (+ Doc 100, Corollary 2).
- **Method**: (i) Connes's 1999 semilocal trace formula (unconditional theorem);
  (ii) compression of the scaling action to the Sonine space — positivity **by
  construction** (it is a trace $\mathrm{Tr}(T \cdot T^*)$); (iii) the Weil−Sonine
  discrepancy expressed in **prolate spheroidal functions** and controlled with
  **Hermitian Toeplitz matrices**; (iv) the representation of the infinite dihedral
  group $\mathbb Z \rtimes \mathbb Z/2$ generated by $(\mathcal P_1,
  \widehat{\mathcal P}_1)$. **[VERIFIED]** (textual abstract + Doc 100 §2.4).

### 4.3 What THEY say about the global/semilocal extension

- Abstract of 2006.13771, textual: *"All the ingredients and tools used above make
  sense in the general semi-local case, where Weil positivity implies RH."*
  **[VERIFIED]**.
- Introduction, textual (according to the source): *"It is thus natural to implement this
  fundamental positivity in the semi-local framework applied to the finite set of
  places $\{\infty, 2, 3, \ldots, p\}$"* — with the support condition
  $\mathrm{Supp}(f) \subset (p^{-1}, p)$, which **grows** with the set of places
  (verified in Doc 100 §5: the "the test space shrinks" version of the obstacle
  was refuted). **[VERIFIED]**.
- CCM 2024 (textual, Doc 100 §2.5b): semilocal positivity for $|S| \ge 2$ is a
  **declared strategy, not a theorem**: *"We expect that the use of such operator
  theoretic tools in the semilocal case will open a way to treat Weil positivity as in
  [CC 2021]..."*. **[PREVIOUSLY VERIFIED — Doc 100]**.
- **No proof exists**, as far as found, of semilocal positivity with any
  finite place ($P(n)$, $n > 2$ in Doc 100's notation). **[UNVERIFIED that it
  exists; negative search in this session and in Doc 100]**.

### 4.4 Connection they declare with the square (a key quote!)

In 2006.13771 (introduction, textual according to the source): the geometric approach
*"unveiled a novel geometric landscape still in development for an **intersection
theory of divisors (on the square of the Scaling Site)**"*. **[VERIFIED]**. This is
CC's explicit statement that their own archimedean positivity theorem is, in
their reading, a fragment of the still-nonexistent intersection theory on the square.
See §6.

---

## §5. Piece 5 — ZETA SPECTRAL TRIPLES

### 5.1 Verified references

- CCM, *Zeta zeros and prolate wave operators*, arXiv:2310.18423, Ann. Funct. Anal. 15
  (2024). **[VERIFIED]** (abs): *"We integrate in the framework of the semilocal
  trace formula two recent discoveries on the spectral realization of the zeros of the
  Riemann zeta function by introducing a semilocal analogue of the prolate wave
  operator."*
- CCM, *Zeta Spectral Triples*, arXiv:2511.22755 (27; *"to appear in EMS
  Lecture Notes... Applications of Noncommutative Geometry..."*). **[VERIFIED]**
  (abs + HTML text).
- A. Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time*,
  arXiv:2602.04022 (3; submitted to the Journal of Open Mathematical Problems
  2025-09-19). **[VERIFIED]** (abs + HTML text). The target's reference was
  correct.

### 5.2 What operators they build (2511.22755)

- **The operator**: $D_{\log}^{(\lambda,N)}$, a **rank-one perturbation** of the
  scaling operator $D_{\log}^{(\lambda)} = -i u\,\partial_u$ on
  $L^2([\lambda^{-1}, \lambda], d^*u)$ with periodic boundary conditions (free
  spectrum $2\pi n/L$, $L = 2\log\lambda$). **[VERIFIED]**.
- **The arithmetic input**: Weil's quadratic form $QW_\lambda$ (polarization of
  the explicit formula: $W_\infty$ + $\sum_p W_p$ + pole terms $W_{0,2}$)
  restricted to finite-dimensional subspaces $E_N$; textual: *"the construction
  only involves the Euler products over the primes $p \le x = \lambda^2$."*
  **[VERIFIED]**.
- **Structure of the truncated matrix** (relevant to Piece 7): in the basis $\{V_n\}$,
  $\tau_{ii} = a_i$, $\tau_{ij} = (b_i - b_j)/(i - j)$ for $i \ne j$, with
  $a_{-j} = a_j$, $b_{-j} = -b_j$; self-adjointness of the rank-one perturbation is
  guaranteed with *"the extension... of the classical Carathéodory–Fejér theorem for
  Toeplitz matrices."* **[VERIFIED]**.

### 5.3 What they prove vs what they observe (2511.22755)

- **Proved** (Theorem 1.1 according to the extracted text): (i) $D_{\log}^{(\lambda,N)}$ is
  self-adjoint on $E_N' \oplus E_N^\perp$ with the inner product
  $QW_\lambda^N - \epsilon_N\langle\cdot|\cdot\rangle$; (ii) the regularized determinant
  is $\det_{\mathrm{reg}}(D_{\log}^{(\lambda,N)} - z) = -i \lambda^{-iz}
  \widehat{\xi}(z)$ with $\xi$ the minimal eigenvector; (iii) $\widehat{\xi}(z)$ is
  **entire with all its zeros real**, and those zeros are the spectrum.
  **[VERIFIED]**. — That is: what is proved is that the approximating zeros
  lie **exactly on the critical line** (real self-adjointness), for each
  finite $(\lambda, N)$.
- **Observed, not proved**: that those spectra converge to the zeros of $\zeta$.
  With primes $\le 13$: the first 50 zeros with error between $2.5 \times 10^{-55}$
  and $10^{-3}$; textual: *"The probability of achieving such precise approximations by
  chance is approximately $10^{-1235}$."* **[VERIFIED]**.

### 5.4 What they declare open

- Textual (2511.22755): *"Establishing this convergence rigorously would amount to a
  proof of the Riemann Hypothesis."* **[VERIFIED]**.
- The main obstacle they name (§7 of the paper, textual): *"Justifying rigorously this
  step is the main remaining obstacle to our approach to RH"* — the step being that the
  "educated guess" $k_\lambda$ (a deformation of **prolate** eigenfunctions via the
  operator $PW_\lambda = -\partial_x[(\lambda^2 - x^2)\partial_x] + (2\pi\lambda x)^2$)
  rigorously approximates the minimal eigenvector $\xi_\lambda$ of $QW_\lambda$.
  **[VERIFIED]**.
- Secondary declared strategy: convergence of the normalized regularized determinants
  toward Riemann's $\Xi$ function (with Hurwitz used to transfer the
  zeros). **[VERIFIED]**.
- On the "CF" role from the target: in the extracted text of 2511.22755 **there is no
  mention of continued fractions**; if the target meant Carathéodory–Fejér,
  that role IS present (self-adjointness via Toeplitz). **[VERIFIED — negative search
  with extraction caveat]**.
- In 2602.04022 (Connes alone), the "letter to Riemann" extremizes Weil's quadratic
  form with primes $< 13$ using nineteenth-century mathematics; it **proves**
  that the approximating values fall exactly on the critical line (textual: *"we prove a general
  result that these approximating values lie exactly on the critical line"*); and
  concludes, textual: *"While the numerical evidence in support of this is
  overwhelming, evidence alone is not a proof"* and *"It is of course possible that a
  complete proof along these lines may encounter serious obstacles."* It proposes as a
  path the convergence of zeros of finite Euler products to infinite ones via
  trace formulas, highlighting that the advantage of the semilocal space $Y_S$ over
  the full adelic one is **measure-theoretic**. **[VERIFIED]**.

### 5.5 [INTERPRETATION] for the program

The "zeta spectral triples" line is the operator-theoretic embodiment of the **analytic/
Route A** of the roadmap, not of the G1–G4 spine: it produces self-adjointness (= critical
line) by construction at every finite level and shifts ALL of RH's content to a
convergence/perturbation statement — structurally isomorphic to the obstacle $\mathbf O_{SL}$
(non-uniformity in $n$) already catalogued in Doc 100 §5. It does not by itself contribute
the weight/signature structure of G2; it does, however, contribute the explicit
**truncated quadratic form** $QW_\lambda^N$ with its Toeplitz-plus-finite-rank
structure (see §7).

---

## §6. Piece 6 — THE SQUARE: what they have written about the arithmetic $C \times C$

This is the central piece for G1↔G2. Chronology of CC's explicit statements:

### 6.1 The square of the arithmetic site (1502.05580, 2015)

It exists as a semi-ringed topos: the non-reduced square with sheaf
$\mathbb Z_{\min} \otimes_{\mathbb B} \mathbb Z_{\min}$, the reduced one with sections =
**Newton polygons** (convex-hull operations); its points over
$\mathbb R_+^{\max}$ are the product of the points of the site (Prop. 6.11); and the
Frobenius correspondences $\Psi(\lambda)$ live on it as subvarieties, with
composition exact only for $\lambda\lambda' \notin \mathbb Q$. **[VERIFIED]** (§1.3).
**What is missing in 2015**: any theory of divisors, intersection, or cohomology
on that square. **[VERIFIED — evident]**.

### 6.2 Connes's diagnosis in the *Essay* (1509.05576, 2015)

- Connes describes **three strategies** toward RH, textual (according to the source): (1) *"based on
  Riemannian spaces and Selberg's work on the trace formula"*; (2) *"based on algebraic
  geometry and the Riemann-Roch theorem"*; (3) *"based on the development of a suitable
  'Weil cohomology', the role of Segal's $\Gamma$-rings"*. **[VERIFIED]**.
- On the model proof (Weil via Mattuck–Tate/Grothendieck): he applies a positivity
  lemma to the quadratic form $\mathfrak s(D, D') = D \cdot D'$ on
  $C \times C$, and the role of RR is, textually: *"if $D.D > 0$ then after a suitable
  rescaling... one gets $\ell(nD) > 1$"* — RR as a **section producer** that
  feeds the Hodge index. **[VERIFIED]** (passages according to the source).
- Connes's diagnosis, textual: *"it is highly desirable to find a geometric
  framework for the Riemann zeta function itself, in which the Hasse-Weil formula, the
  geometric interpretation of the explicit formulas, the Frobenius correspondences...
  all make sense"* and — crucially candid — *"It is yet unclear if this is the
  right set-up for the final Riemann-Roch step."* **[VERIFIED]**.

### 6.3 *The Riemann-Roch strategy* (1805.10501, 2018) — the most explicit statement

- Declared goal, textual: *"adapting in characteristic zero Weil's proof, of RH in
  positive characteristic, following the ideas of Mattuck-Tate and Grothendieck."*
  **[VERIFIED]**.
- **The obstacle they name**, textual: *"However, in the process to formulate
  a Riemann-Roch theorem on the square of the Scaling Site one faces a substantial
  difficulty"* — and the difficulty is **$H^1$ in characteristic 1**: *"The problem, which
  is still open at this time, has to do with an appropriate definition of the sheaf
  cohomology (as idempotent monoid) $H^1$... when applied to Čech covers, the presence
  of the null elements creates unwanted contributions to the cohomology which so far we
  are unable to handle."* **[VERIFIED]**. — This is THEIR diagnosis of what is missing:
  not positivity, not the trace formula, but **the idempotent $H^1$ cohomology
  on the square**, blocked by the null elements in the Čech covers.
- **Their tactical response**: **tropical descent** — textual: *"deduce existence
  results in characteristic one from available Riemann-Roch theorems in complex
  geometry"*, via almost-periodic functions (Bohr–Jessen–Tornehave): every convex
  function is the tropicalization of an almost-periodic analytic function. And the
  construction of the **complex lift** of the adele class space:
  $\mathcal C_{\mathbb Q} = \mathbb Q^\times \backslash (G \times \mathbb A_{\mathbb Q})$,
  interpreted as a moduli space of elliptic curves with triangular
  structure ($\mathbb Q$-parabolic lattices), the equivalence relation generated by
  **isogenies**, foliated by 1-dimensional complex leaves. **[VERIFIED]**.
- **[INTERPRETATION]**: note the strategic inversion: instead of building RR on the
  tropical square, they sidestep it by lifting to $\mathbb C$ and descending existence.
  There is no published continuation completing either RR in tropical
  dimension 2 or RR on the complex lift (negative search). **[UNVERIFIED that
  a continuation exists]**.

### 6.4 The 2020–2026 state

- 2006.13771 (2021): the §4.4 quote — archimedean positivity is presented as
  part of *"a novel geometric landscape still in development for an intersection
  theory of divisors (on the square of the Scaling Site)"*. **[VERIFIED]**. In other words:
  for CC, **their positivity theorem IS the analytic germ of the Hodge index of
  the square** — but intersection theory as such remains "in development".
- 2205.01391/2306.00456 (2022–23): they resolve $H^1$ **in dimension 1** on the
  absolute base ($\Gamma$-rings + tolerance + Dold–Kan), with duality. **[VERIFIED]**.
  **[INTERPRETATION]**: it is plausible to read this development as their attack on
  the 1805.10501 obstacle via a change of base (from idempotent semirings to
  $\mathbb S$-modules), where the "null elements" problem of Čech is tamed
  with tolerances; but CC do not state that connection explicitly in the texts
  read. **[UNVERIFIED as a claim by them]**.
- 2602.15941 (2026): Picard/Jacobian of $\overline{\mathrm{Spec}\,\mathbb Z}$ in
  dimension 1, with no mention of the square or of intersection. **[VERIFIED]**.
- **Conclusion of Piece 6**: there does **not exist in the published CC corpus**:
  RR on the square of the scaling site; a theory of intersection of divisors on
  the square (only announced as "in development" in 2021); an analogue of the
  Hodge/Castelnuovo index; an intersection form with signature. The self-declared
  obstacle (1805.10501) is the idempotent $H^1$ in dimension 2; their new tool
  (tolerance over $\mathbb S$) resolves it for now only in dimension 1. **[VERIFIED the
  negative within what was read/searched]**.

---

## §7. Piece 7 — SIDE FINDINGS relevant to weights/signatures/forms

1. **Pontryagin duality with tolerance** (2205.01391, Prop. 5.2 + Thm 1.2):
   the only genuine duality pairing in the corpus; dualizer $U(1)_{1/4} = H^1(K)$,
   $K = -2\{2\}$. **[VERIFIED]**. **[INTERPRETATION]**: for G2 this matters because an
   intersection form with signature on the square should, in any
   formalization, induce on the diagonal a duality of this type; CC already have the
   "diagonal side" in dimension 1. The reverse direction (from duality to signature) is
   exactly what is NOT there.
2. **Type II continuous dimension vs integer dimension**: the coexistence in the same
   corpus of $\mathrm{Dim}_{\mathbb R}$ (normalized limit $p^{-n}\dim_{\mathrm{top}}$,
   1603.03191) and $\dim_{\mathbb S}$ (minimum number of generators with tolerance,
   2306.00456) is structurally the "averages → integers" transition that the roadmap
   calls wall G2. CC have crossed it **in dimension 1, for cohomology
   dimensions** — not for signatures. **[VERIFIED both extremes; INTERPRETATION
   the reading]**.
3. **The fine structure of the truncated Weil form** (2511.22755): the matrix
   $\tau_{ij} = (b_i - b_j)/(i-j)$ off the diagonal (**Pick/Loewner** type, not
   pure Toeplitz) plus diagonal $a_i$; parities $a_{-j} = a_j$, $b_{-j} = -b_j$.
   **[VERIFIED]**. **[INTERPRETATION]**: Loewner matrices are the classical
   machinery of **operator monotonicity and inertia indices**; that the truncated Weil
   form is exactly of that type is a potentially direct datum for the
   computation of $\kappa(Q)$ window by window (connection with Doc 91/100) that CC use only
   for self-adjointness, not for signature.
4. **Lower-bounded, not definite, positivity** (2511.22755, Prop. 3.3 according to the
   text): $QW_\lambda$ is **lower bounded** and semicontinuous — CCM work
   systematically with "lower bounded + compact/finite perturbation", never with
   definite forms. **[VERIFIED]**. This is exactly the regime
   $\kappa(Q) < \infty$ of the program (S1), without them ever naming the negative
   index as an invariant. **[INTERPRETATION]**.
5. **The group → monoid step** (2602.15941): CC's insistence that Picard
   must be a **monoid** (degenerate seminorms, boundary phenomena) *"precisely the
   features required for the spectral realization."* **[VERIFIED]**.
   **[INTERPRETATION]**: boundary/degeneration phenomena are where inertia
   indices live in families of forms (eigenvalue crossings = norm degeneration);
   CC's monoidal language could be the natural receptacle for a
   spectral flow, something they do not say.
6. **Frobenius does not amplify**: on $(\mathcal K, Q)$ the Frobenius
   correspondences act by isometries (Doc 106, Prop. 3.10) — the site's Frobenius
   measures, rather than generates, the defect. **[PREVIOUSLY VERIFIED — Doc 106, a
   program result, not CC's]**.
7. **Negative search for "signature"**: in none of the texts read in this
   session does the word signature/inertia index appear as an invariant of their
   theories (the only sign structure is positivity/lower-boundedness).
   **[VERIFIED — negative, with extraction caveat]**.

---

## §8. Mapping against the G1–G4 / S1–S3 shopping list

| Node | What CC have today (verified) | What is missing (declared by them or evident) |
|---|---|---|
| **G1** (finite-dim. cohomology on the square) | The square exists as a semi-ringed topos (1502.05580 §6); tropical RR in dim 1 (1603.03191); $H^0, H^1$ + integer dims in absolute dim 1 (2205.01391, 2306.00456) | Idempotent $H^1$ in dim 2: self-declared obstacle (1805.10501, "null elements" in Čech); no cohomology on the square |
| **G2** (weight/signature) | Serre/Pontryagin duality in dim 1 (Thm 1.2 of 2205.01391); integer dimensions; archimedean positivity with finite defect $c < 17$ (2006.13771) | No intersection form, no Hodge index, no notion of signature in the whole corpus; the "intersection theory on the square" declared *in development* since 2021 with no subsequent publication |
| **G3** (Lefschetz = explicit formula) | Semilocal trace formula (theorem, Connes 1999); action of $C_{\mathbb Q}$ on $\widetilde{\mathrm{Pic}}$ localized on periodic orbits (2602.15941 §9) | The global case is equivalent to RH, not a theorem; divergent term $2h(1)\log\lambda$ pending (2602.15941 §9.3) |
| **G4** ($\kappa(Q) = 2m < \infty$ a priori) | "Lower bounded + finite rank" regime proved only in the window $(1/2,2)$, one place | No uniformity mechanism across the window (Obstacle $\mathbf O_{SL}$, Doc 100); CC do not even formulate the negative index as a goal |
| **S1** (signature, not Euler) | — | Exactly the gap: all their RR produces Euler characteristics (integer in dim 1), never signatures |
| **S2** (autonomous traces) | Weil's explicit formula + the semilocal trace (theorems) | The cohomological evaluation of the traces |
| **S3** (unconditionality) | CC 2021 is unconditional in its window | Everything else conditional or numerical |

**[INTERPRETATION] — the three operative readings for Phase 39:**

1. **The G2 gap is real and is exactly where CC stop.** They have duality
   (a perfect pairing $H^1 \times H^0 \to U(1)$) but no bilinear form on
   a single space with an inertia index. The G1↔G2 interface should ask: what
   condition on a theory on the square makes the diagonal Pontryagin duality
   refine into an intersection form with signature? CC do not ask this.
2. **Their diagnosis of the square is cohomological, not analytic**: the blockage named
   is idempotent Čech $H^1$ (1805.10501), and their 2022–23 progress (tolerance over
   $\mathbb S$) resolves it in dim 1. If that technique extends to the square, G1 would
   move; G2 would remain open because there is no signature even in dim 1.
3. **The 2021 Weil positivity is, by their own account, the germ of the
   intersection theory of the square** ("novel geometric landscape still in development for an
   intersection theory of divisors (on the square of the Scaling Site)"). For the
   program this legitimizes reading $\kappa(Q)$ (the negative index of the Weil form) as
   the invariant the intersection form should compute — the identification
   $\kappa(Q) = $ Hodge-index defect is consistent with their language, but it is
   ours, not theirs.

---

## §9. What could NOT be verified in this session

- Journal bibliographic data for 1502.05580 (Adv. Math.?), 1603.03191
  (Selecta?), 2205.01391 (the search points to an article on ScienceDirect/Bull.
  Sci. Math. but the journal page was not read). **[UNVERIFIED]**.
- 1405.4527 and 1507.05818: only abstracts in this session (the fine theorems
  were verified in the long versions 1502.05580 and 1603.03191).
- The full text of 2310.18423 beyond what was verified in Doc 100 (Theorems 1 and 2
  semilocal: measure $dm_S = |\prod_{v\in S} L_v(\frac12 - is)|^2 ds$ and stability
  of the Sonine space $\theta_S$). **[PREVIOUSLY VERIFIED — Doc 100]**.
- Whether any published continuation of 1805.10501 exists (RR on the square, tropical or
  complex-lifted): negative search, which is not proof of nonexistence.
  **[UNVERIFIED]**.
- Consani's survey *On the notion of geometry over $\mathbb F_1$* and technical
  interviews: not read in this session; the statements about the square were
  verified in primary sources (1509.05576, 1805.10501, 2006.13771), which are stronger.
  **[UNVERIFIED the survey]**.
- The exact numbering of some cited theorems (e.g., "Theorem 5.6/5.12/5.17" of
  1603.03191, "Theorem 6.11" of 2006.13771, "Proposition 4.2" of 2306.00456) comes
  from the extracted text; the statement is faithful but the numbering should be
  re-confirmed against the PDF before citing it in a paper. **[VERIFIED with caveat]**.

---

*End of Doc 120.*
