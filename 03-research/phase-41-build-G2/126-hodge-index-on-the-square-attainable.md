# Doc 126 — The Hodge index on the square: attainable or RH-circular? Analysis of the Kähler package

**Program:** Riemann Hypothesis — Phase 41: BUILD G2.
**Prerequisites:** Doc 124 (G2 = Hodge index, INDEFINITE form of signature (1, ρ−1); the intersection-positivity [GOOD] vs spectral-positivity [CIRCULAR] distinction; verdict: CC's positivity is spectral, not intersection); Doc 123 ((C-cok)/(C-rank) bifurcation; tolerance repairs (C-cok), not (C-rank); in dim 2 the (C-rank) datum IS the intersection form = G2; the structural result "the numerical part of G1 and G2 are the same object"); Doc 119 (R-WEIGHT(b): purity as a geometric THEOREM; the non-circularity test R-NC, clauses NC1 externality / NC2 overgeneration / NC3 non-reduction to the MW catalog / NC4 two worlds; order R-SIG ≺ R-FIN); Doc 80 (arithmetic Castelnuovo–Severi; Proposition 8.1 "no form defined solely in terms of a measure distinguishes the two measures"; Weil's Step A/Step B; the circularity of the measure difference).

**PARALLEL WORK:** Doc 125 (another document in the program) constructs the concrete intersection form on the square. This document does NOT use its explicit form: it works with the **required properties** (signature (1, ρ−1), classes f₁, f₂, Δ, correspondences) and evaluates the **proof strategy**. The properties assumed from the form are labeled **[ASSUMED-FROM-125]**.

**Labeling discipline (absolute rule, maximum false-victory risk):** **[DATA]** = read in source this session (arXiv / survey, with citation), or an internal theorem of the program (backward-only citation). **[CONSTRUCTION]** = what I design/analyze myself, with explicit status. **[CALCULATION]** = my own derivation, shown. **[GAP]** = what is missing, precisely. **[CONJECTURE]** / **[UNVERIFIED]** = as indicated. **[ASSUMED-FROM-125]** = a property of the form I take from Doc 125 without re-deriving. **NEVER "proved"** except for what truly is. The goal is to evaluate WHETHER a Hodge index theorem is attainable for this object and to isolate the irreducible core — NOT to declare it proved. If the core turns out to be RH-equivalent (circular), that is the most important possible result and is stated without hedging.

---

## 0. Executive summary

This document confronts the "Hodge index on the square" strategy (= G2 = purity = RH) with the only body of mathematics where a Kähler package was proved by NEW combinatorial/tropical methods, not by complex geometry: Adiprasito–Huh–Katz (AHK, arXiv:1511.02888) for matroids, and its hard frontier, Babaee–Huh (BH, arXiv:1502.00299), where tropical positivity does NOT imply algebraic positivity. The master question of all of Phase 41 is: is the irreducible core of G2 (a) a genuine tropical Kähler-package theorem (not circular, new but conceivable mathematics), (b) RH-circular in disguise, (c) obstructed à la BH, or (d) undeterminable today?

**Central findings:**

1. **AHK does NOT apply to the square of the scaling site, due to a precise structural obstruction not repairable with the current method:** AHK is a theorem about a graded Chow ring of a **finite** object (finite-rank matroid ⟹ finite simplicial Bergman fan), proved by **finite induction** (deletion–contraction / matroidal flips) over the lattice of subsets. The square of the scaling site is **infinite-dimensional, with continuous flow ℝ₊\*** and "genus = ∞" (infinitely many zeros of ζ); AHK's four hypotheses fail to different degrees, but the one that **breaks the method at its root** is **infinity + continuity**, which destroys the finite induction (§2.4). [CONSTRUCTION/GAP]

2. **Babaee–Huh OBSTRUCTS generically, and the scaling site falls on the obstructed side, NOT the AHK side:** BH exhibit a strongly positive tropical current (2,2) on a 4-dimensional toric variety whose class is **not** a limit of algebraic cycles, "because its intersection form does not have the correct signature of the Hodge index theorem" [DATA, BH abstract verbatim]. The **criterion separating the two cases** is matroidality/Lefschetz: the Bergman fan of a matroid is **strongly extremal** and satisfies Hodge–Riemann (AHK); a generic tropical fan (balanced but non-matroidal) **does not**. The square of the scaling site **has no known reason to be matroidal**; its intersection form is exactly of the type whose signature BH shows can fail. (§3) [DATA + CALCULATION]

3. **The irreducible core (§4):** "The square of the scaling site satisfies the Hodge–Riemann relations in middle degree (signature (1, ρ−1) with negative definiteness on the primitive part)." Subjected to R-NC with maximum rigor: the statement **as a generic Kähler-package theorem** would pass NC1, NC2, NC4 (it is the Castelnuovo situation). **BUT** on **our** object, the positivity on the primitive part restricted to the flow correspondences (Γ_F and its iterates) **IS** the Weil positivity of Doc 124, which **FAILS NC3** (it is MW-1). The verdict bifurcates along a precise axis: **if the signature is a geometric theorem of the square (holding for every correspondence, proved without ζ), it is not circular and G2 is attainable-in-principle; if the signature can only be established on the correspondences of ζ, it is Weil positivity renamed and it is circular.** (§4)

4. **Verdict (§5): (d) undeterminable, with a strong bias toward (b)/(c), and a single narrow path toward (a).** The exact difference with function fields (§4.4): there C×C is a genuine algebraic variety whose Grothendieck intersection theory gives Castelnuovo **free and for every divisor** (NC2 with content); the Hodge index for surfaces is a classical theorem, prior to any ζ. Here the "square" is tropical/characteristic 1 and its intersection theory **is precisely what is missing** (Doc 123 §6.2). BH shows that in the tropical world the Hodge index **is not free** — it fails for generic tropical surfaces. Therefore path (a) requires proving that the square of the scaling site is of the matroidal/Lefschetz subtype where the index DOES hold — a conceivable but today absent genuine tropical Kähler-package theorem, whose R-NC verification crucially depends on it overgenerating (NC2). If instead the only way to prove the signature goes through evaluating the form on the correspondences of ζ, it falls back into (b) circular. **Today there is no way to decide which, because the intersection form of the square does not exist as an object (Doc 123); Doc 125 constructs it, and the verdict depends on its character — geometric-for-every-correspondence vs definable-only-on-ζ.**

---

## 1. THE KÄHLER PACKAGE [DATA]

### 1.1. Precise statement of the three properties

**[DATA]** (AHK, arXiv:1511.02888, Annals of Math. 188 (2018) 381–452; survey Eur–Larson, *Notices AMS* Mar. 2025; survey "Essence of independence," arXiv:2211.05724.) Let $A^\bullet = \bigoplus_{k=0}^{d} A^k$ be a finite real-dimensional commutative graded ring over $\mathbb R$, with $A^0 = \mathbb R$ and $A^d \cong \mathbb R$ (a "top degree" canonically isomorphic to $\mathbb R$ via a degree map $\deg: A^d \to \mathbb R$). The **Kähler package** for $A^\bullet$, with respect to an element (ample / Lefschetz class) $\ell \in A^1$, consists of the three properties:

1. **Poincaré duality (PD).** The pairing
$$ A^k \times A^{d-k} \longrightarrow A^d \xrightarrow{\ \deg\ } \mathbb R, \qquad (x,y)\mapsto \deg(x\cdot y) $$
is **non-degenerate** for every $0\le k\le d$. In particular $\dim A^k = \dim A^{d-k}$.

2. **Hard Lefschetz (HL).** For $0\le k\le d/2$, iterated multiplication by $\ell$,
$$ \ell^{\,d-2k}\cdot:\ A^k \xrightarrow{\ \sim\ } A^{d-k}, $$
is an **isomorphism**. (This implies $\dim A^k$ is unimodal-increasing up to the middle degree.)

3. **Hodge–Riemann relations (HR).** Defining the **primitive part** $P^k := \ker(\ell^{\,d-2k+1}: A^k\to A^{d-k+1})$, the quadratic form
$$ Q_\ell^k(x) := (-1)^k\,\deg(\ell^{\,d-2k}\, x^2), \qquad x\in P^k, $$
is **positive definite** on $P^k$ (for $0\le k\le d/2$).

**[CALCULATION] The Hodge index is the middle-degree case of HR.** On a **surface** ($d=2$), the middle degree is $k=1$, $P^1 = \ker(\ell\cdot: A^1\to A^3=0) = A^1\cap (\text{orthogonal of }\ell)$ — the primitive part is the orthogonal complement of the ample class under the intersection form. HR at $k=1$ says: $Q_\ell^1(x) = -\deg(x^2) = -x\cdot x > 0$ for $x\in P^1\setminus\{0\}$, i.e. **$x\cdot x < 0$ on the orthogonal of the ample class** — exactly the **classical Hodge index theorem**: the intersection form has signature $(1,\rho-1)$, one positive direction (that of $\ell$) and $\rho-1$ negative ones (the primitive part). [Doc 124 §1.1 fixed this profile as the "good" intersection-positivity.]

### 1.2. The Chow ring of a matroid and what structure AHK needs

**[DATA]** (AHK; Eur–Larson; arXiv:2211.05724.) For a matroid $M$ of rank $r$ on a finite ground set $E$, the **Chow ring** $A^\bullet(M)$ is the Chow ring of the **Bergman fan** $\Sigma_M$ (a **finite** simplicial fan in $\mathbb R^E/\mathbb R\mathbf 1$, whose cones correspond to chains of flats of $M$). It is an explicit quotient of a polynomial ring by linear (flat-incidence) and quadratic (Stanley–Reisner) relations. Structural properties:
- **Finite grading** $A^\bullet(M)=\bigoplus_{k=0}^{r-1}A^k(M)$, with $d=r-1$. [DATA]
- **Top degree** $A^{r-1}(M)\cong\mathbb Z$ canonically ("trivial" Poincaré duality). [DATA]
- **Ample class $\ell$:** comes from a **strictly convex piecewise-linear** function on $\Sigma_M$ (in toric language, an ample divisor; in combinatorial language, a submodular assignment). The cone of such $\ell$ is non-empty precisely because $\Sigma_M$ is the fan of a "sufficiently positive" toric variety. [DATA]
- **Induction via flips / deletion–contraction:** the proof relates $A^\bullet(M)$ to $A^\bullet(M\setminus i)$ and $A^\bullet(M/i)$ (deletion and contraction of an element) via exact sequences and "matroidal modifications" (matroidal flips), allowing the rank to be lowered. [DATA]

**[DATA] The minimal structure the AHK method needs** (extracted from the surveys): (i) a **finite-dimensional graded Chow ring** with top degree $\cong\mathbb R$; (ii) **Poincaré duality** (which for fans comes from being the fan of a smooth/simplicial complete toric variety, or from the tropical Poincaré property); (iii) an **ample class** (strictly convex piecewise-linear function / non-empty Kähler cone); (iv) the **flip machinery and a polyhedral order** on a **finite lattice** (the matroid's flats) allowing the induction.

### 1.3. How AHK prove the package: simultaneous induction of the three properties

**[DATA]** (AHK; surveys.) The architecture of the proof —and this is decisive for evaluating transplantability— is:

> PD, HL, and HR are proved **all at once, by simultaneous induction**, NOT one after another. Matroids (or the intermediate fans of a sequence of flips) are ordered and the argument runs: assuming the Kähler package for the "earlier" objects (lower rank, or one flip back), it is deduced for the current object. The engine of the inductive step is:
> - a **Lefschetz map** (multiplication by the ample class $\ell$) whose isomorphism property (HL) is controlled using HR from the previous step;
> - the **signature** of the HR form is a **discrete invariant** (the number of $+$ and $-$ signs); it changes only when an eigenvalue crosses zero; the inductive argument (deforming $\ell$ within the ample cone, which is connected) shows that **no eigenvalue crosses zero** because PD guarantees non-degeneracy along the path, so the signature **transports** from a base object where it is known.

The core of the method is therefore: **(α) a finite lattice to induct over; (β) non-degeneracy (PD) along a deformation of $\ell$ in a connected ample cone; (γ) a base case with known signature; (δ) the rigidity of the signature as a discrete invariant under deformation with non-degeneracy.** Without the finiteness of (α), the induction cannot start; without the connectedness/finiteness of the ample cone in (β), the signature transport is not guaranteed. **[CALCULATION on DATA.]**

**[DATA] Key point for Phase 41:** AHK proved the package **without using any result from complex algebraic geometry** — it is a genuine combinatorial theorem. This is exactly the kind of "new but conceivable mathematics" that path (a) of the verdict would require. The question is whether architecture (α)–(δ) survives transplantation to the scaling site.

---

## 2. DOES AHK APPLY TO THE SQUARE OF THE SCALING SITE? [CONSTRUCTION/GAP]

The scaling site is **not** a Bergman fan nor a matroid: it is a characteristic-1 object with a flow $\mathbb R_+^*$, infinite, with "genus" = (the infinitely many zeros of ζ). I review the four hypotheses (a)–(d) posed.

### 2.1. (a) Is there a Chow ring / graded cohomology of the square?

**[DATA-FROM-123].** Doc 123 constructed —**conditional on three technical gaps A1–A3**— a candidate $H^1_{\mathrm{tol}}(X\times X)$ via Dold–Kan over the tolerant Čech complex. It is an **𝕊-module with tolerance**, not a graded ring with a product. Status:
- **What exists:** a tolerant $H^1$ (object), with the syntactic half of the obstruction (C-cok) repaired. [DATA-FROM-123 §3.1]
- **What does NOT exist:** a **Chow ring** $A^\bullet$ with a graded product and top degree $\cong\mathbb R$. The **ring** structure (the product defining the intersection form $x\cdot y$) is precisely what is missing — Doc 123 §6.2 isolates it as (C-rank) = the intersection norm = G2. [DATA-FROM-123]

**[CALCULATION] Diagnosis of hypothesis (a): PARTIAL/FAILS.** There is a candidate cohomology group (tolerant), but **no graded ring with a product**. AHK needs a whole **Chow ring** $A^\bullet$ (the intersection form IS the product $A^1\times A^1\to A^2$). The product is precisely what is absent. **Hypothesis (a) of AHK does NOT hold today** — and Doc 125 is attempting to construct exactly that product. Without it, HR cannot even be stated.

### 2.2. (b) Is there Poincaré duality?

**[DATA-FROM-120/123].** Doc 120 reports that in the CC corpus there is a **Serre duality with tolerance in dimension 1** (the $H^0(D)\leftrightarrow H^0(-D)$ duality of the type-II RR of the scaling site, 1603.03191 Thm 5.17). Doc 122 reports that CC's global duality is **Pontryagin duality** (group↔dual), **not a form on a space with a symmetry character** (Request 122.A: the polarization is missing). [DATA]

**[CALCULATION] Diagnosis of hypothesis (b): it does NOT extend to the form AHK needs.** The tolerant dim-1 Serre duality is a pairing $H^0\leftrightarrow H^0(-D)$ — a scalar datum (degree), **not** a pairing $A^k\times A^{d-k}\to A^d\cong\mathbb R$ with the structure of a **non-degenerate intersection form**. For PD in the AHK sense one needs:
- the top degree $A^2(X\times X)\cong\mathbb R$ (the "fundamental class" of the square) — **[GAP]**: not constructed (would be the surface RR that CC declare *in development*, Doc 120 §4.4);
- the **non-degeneracy** of the pairing $A^1\times A^1\to A^2\cong\mathbb R$ — **[GAP]**: this is the intersection form itself (= G2).

CC's Pontryagin duality (Doc 122) **is not** PD in the AHK sense: PD is a **symmetric form on a single graded space** ($x\cdot y = y\cdot x$ in $A^1$), while Pontryagin is a group↔dual pairing with no intrinsic symmetry. **AHK-PD is not available.** [ASSUMED-FROM-125: that Doc 125's intersection form, if constructed, satisfies non-degeneracy — this would be the content of PD in degree 1.]

### 2.3. (c) Is there an ample class? What is "ample" on the scaling site?

**[CONSTRUCTION].** The natural candidate for an ample class is $\ell = f_1 + f_2$, the sum of the two fiber classes (horizontal $\{pt\}\times X$ and vertical $X\times\{pt\}$) — the analogue of the $(1,1)$ polarization Weil uses on $C\times C$ [Doc 80 §1.1; Doc 124 §1.2]. [ASSUMED-FROM-125: that $f_1, f_2$, and $\Delta$ (diagonal) are well-defined classes in the analogue of $\mathrm{NS}(X\times X)$, with $f_1^2=f_2^2=0$, $f_1\cdot f_2 = 1$.]

**[CALCULATION] Diagnosis of hypothesis (c): the candidate exists formally, but "ample" lacks an intrinsic definition.** In AHK, "ample" = a strictly convex piecewise-linear function on the fan (explicit Kähler cone, **non-empty by combinatorial construction**). On the scaling site:
- $f_1+f_2$ is the syntactic candidate, but **what makes a class "ample"** on the tropical square? There is no notion in the corpus of an ample cone / strict convexity on the analogue of $\mathrm{NS}(X\times X)$. Convexity exists in dim 1 (the piecewise-affine convex functions of the sheaf $\mathcal O_p$, Doc 123 §4.1), but **the ample cone of divisors of a tropical surface** is not defined. **[GAP]**
- More seriously (feeds §2.4): the flow $\mathbb R_+^*$ is **continuous**; AHK's "ample cone" is a polyhedral cone of a finite object over which the deformation of $\ell$ sweeps a **finite-dimensional** connected set. Here the space of classes is infinite-dimensional (Doc 124 §2.4: dim $H^1=\infty$), and the deformation of $\ell$ — step (β) of the AHK method — has no guarantee of avoiding degenerations.

### 2.4. (d) Infinite dimension / continuous flow breaks AHK's induction — the central obstruction

**[CALCULATION — the decisive analysis of §2].** AHK's induction (§1.3, architecture (α)–(δ)) is **finite and polyhedral at its root**. I locate where each piece dies:

1. **(α) The induction lattice is infinite.** AHK inducts over the **finite lattice of flats** of the matroid (deletion–contraction lowers the rank by 1, and the rank is finite). The scaling site **has no finite rank**: the "genus" is ∞ (infinitely many zeros), dim $H^1=\infty$ [DATA Doc 124 §2.4 / CC *metaphysics of F₁*: "the dimension of $H^1(\mathbf C)$ is infinite"]. **There is no base case reachable in finitely many steps.** The induction does not start. **This is the central obstruction.** [CONSTRUCTION/GAP]

2. **(β) The ample cone is neither finite-dimensional nor evidently connected-controllable.** AHK's signature transport requires deforming $\ell$ within a **connected** ample cone without crossing degenerations, and non-degeneracy (PD) along the path is controlled by finiteness. In infinite dimension, "no eigenvalue crosses zero along the path" **does not follow from PD** — this is exactly **tension T2 of Doc 119 §6.3**: *signatures are not continuous under the limits regularization requires* (discontinuous spectral flow without a uniform spectral gap, Doc 119 [DATA Phi96]). The rigidity of the signature as a discrete invariant (step (δ)) **fails at infinite rank**: [DATA Doc 119 §2.2 / rank-sensitivity roadmap theorem] "at infinite rank the number of negative eigenvalues is not a continuous function of the traces." **(δ) dies for the same reason Route B needs R-FIN.**

3. **Coupling with the order correction of Doc 119/123.** A strong internal coherence emerges here: Doc 119 §2.4 derived (by reverse engineering) that **R-SIG ≺ R-FIN** and that **finiteness belongs to the IMPURE graded piece, not the total** (the pure part, weight 1, is infinite-dimensional: it carries the infinitely many zeros). Translated to AHK: AHK's Kähler package presupposes an object that is **entirely finite** (finite matroid), with NO analogue of "an infinite pure part." The square of the scaling site has **an irreducible infinite part** (the zeros), so that **AHK's machinery is not even of the right type**: AHK would prove signature on a finite object; here the relevant signature ($\kappa(Q)=2m$, Doc 119 = the off-critical quadruples) is that of the **finite impure block** inside an infinite $H^1$. AHK has no machinery for "signature of the finite block of an infinite object." [CONSTRUCTION, consistent with Doc 119 §2.4 + Doc 123 §6.2.]

**[CALCULATION] Conclusion §2:** **AHK does NOT apply.** Of the four hypotheses: (a) Chow ring — the product is missing (= G2); (b) PD — the top degree and non-degeneracy are missing (= G2); (c) ample class — syntactic candidate $f_1+f_2$ with no intrinsic notion of ampleness; (d) **infinity + continuous flow breaks the finite induction at its root** (α dies: no base case; δ dies: signature not rigid at infinite rank). Obstruction (d) is **not repairable** within the AHK method: AHK IS a finite method. Any transplant would require an **infinite-dimensional / "relative signature of the impure block"** version of the Kähler package — new mathematics, without precedent, and exactly the order R-SIG ≺ R-FIN reappearing from the Kähler-package side. **Third independent derivation of the same wall** (Doc 119 reverse engineering; Doc 123 construction of the square; here, AHK).

---

## 3. THE BABAEE–HUH OBSTRUCTION [DATA + analysis]

### 3.1. Exact statement of the result

**[DATA]** (BH, arXiv:1502.00299v3, p.1–3, read verbatim this session.) The framework (Demailly):
- **(HC)** classical Hodge conjecture; **(HC′)** Hodge conjecture for currents (Demailly: HC ⟺ HC′); **(HC⁺)** Hodge conjecture for **strongly positive** currents: every closed strongly positive $(p,p)$ current with rational cohomology class is a weak limit $T=\lim_i\sum_j\lambda_{ij}[Z_{ij}]$ with $\lambda_{ij}\ge0$ **positive** and $Z_{ij}$ subvarieties. Demailly proved **HC⁺ ⟹ HC**, and asked whether HC′ ⟹ HC⁺ (Dem12, Remark 13.43). [DATA]

**[DATA] The counterexample — Theorem 1.1 (BH, p.3, verbatim):**
> *"There is a 4-dimensional smooth projective toric variety $X$ and a $(2,2)$-dimensional strongly positive closed current $\mathcal T$ on $X$ with the following properties: (1) The cohomology class of $\mathcal T$ satisfies $\{\mathcal T\}\in H^4(X,\mathbb Z)/\mathrm{tors}\cap H^{2,2}(X)$. (2) The current $\mathcal T$ is not a weak limit of the form $\lim_i\mathcal T_i$, $\mathcal T_i=\sum_j\lambda_{ij}[Z_{ij}]$, where $\lambda_{ij}$ are nonnegative real numbers and $Z_{ij}$ are algebraic surfaces in $X$."*

That is: **HC⁺ FAILS even on toric varieties where HC holds**. The current $\mathcal T$ generates an **extremal ray** of the cone of strongly positive closed currents (BH p.3). [DATA]

**[DATA] The decisive phrase (BH abstract, verbatim):** *"The counterexample is obtained from a tropical surface in $\mathbb R^4$ whose intersection form does not have the right signature in terms of the Hodge index theorem."*

### 3.2. Which Hodge-index property it breaks — the mechanism

**[DATA]** (BH, §1, p.4–5, read verbatim.) The construction:
- A **tropical current** $\mathcal T_{\mathcal C}$ associated to a **balanced tropical fan cycle** $\mathcal C$ of dimension $p$ in $\mathbb R^n$ (a weighted rational polyhedral complex satisfying the **balancing condition**). Support $|\mathcal T_{\mathcal C}|=\mathrm{Log}^{-1}(\mathcal C)$. [DATA Def. 2.8, Thm 2.9]
- **Theorem 1.3:** a weighted complex $\mathcal C$ is balanced ⟺ the current $\mathcal T_{\mathcal C}$ is closed. [DATA]
- **Theorem 1.5 (key to the mechanism):** the **cohomology class** of the extension $\overline{\mathcal T}_{\mathcal C}$ in the toric variety $X$ is the **recession** $\mathrm{rec}(\mathcal C)\in H^{q,q}(X)$ of the underlying fan. [DATA]
- **§5:** the proof of Theorem 1.1 analyzes a **Laplacian matrix** associated with a 2-dimensional tropical surface $\mathcal C$, viewed as a **geometric graph** $G=G(\mathcal C)\subseteq\mathbb R^n\setminus\{0\}$ with edge weights $w_{ij}$ satisfying the **balancing condition**: at each vertex $u_i$ there exists $d_i$ with $d_i u_i=\sum_{u_i\sim u_j}w_{ij}u_j$. [DATA]

**[CALCULATION] The mechanism of the obstruction, precisely.** The current $\mathcal T$ is strongly positive (tropical positivity: the weights $w_{ij}$ of the balanced complex are positive) and its class is the recession. For $\mathcal T$ to be a limit of **positive algebraic cycles**, its class would have to lie in the cone generated by algebraic surfaces; the obstruction is that **the intersection form on the classes generated by the tropical surface does not have the Hodge index theorem's signature** (abstract). In terms of §1.1: an effective algebraic class (of a surface) in middle degree satisfies the Hodge–Riemann relations (Hodge index ⟹ signature $(1,\rho-1)$, negative definite on the primitive part); the tropical class of $\mathcal T$ **violates** that signature restriction, so it **cannot** be a positive limit of algebraic classes. Extremality (extremal ray of the cone) + wrong signature = not approximable. [CALCULATION on DATA]

**[DATA] The program's phrase that already anticipated this (verified via WebSearch):** *"the direct translation of the Hodge Index theorem fails for tropical surfaces"*. That is: **the Hodge index is NOT free in the tropical world** — it fails for generic tropical surfaces.

### 3.3. The criterion separating AHK (index holds) from BH (index fails)

**[DATA — the decisive criterion, BH p.5 verbatim].**
> *"There is an abundance of strongly extremal tropical varieties. For example, the Bergman fan of any simple matroid is a strongly extremal tropical variety [Huh14, Theorem 38]."*

And (BH p.5): Demailly's first example of a non-analytic extremal current **is** the tropical current associated to the simplest simple matroid (rank 2 on 3 elements). [DATA]

**[CALCULATION — the criterion, formulated].** The axis separating the two worlds is **matroidality / the Lefschetz property**:
- **AHK side (index HOLDS):** tropical fans that are **Bergman fans of matroids**. AHK (arXiv:1511.02888) proved these satisfy the complete Kähler package (PD+HL+HR), so their middle-degree intersection form **has** the correct Hodge-index signature. They are "strongly extremal" but **on the good side**: their signature is that of a projective variety.
- **BH side (index FAILS):** tropical fans that are **balanced but NOT matroidal** (generic). The tropical surface in $\mathbb R^4$ of the counterexample is balanced (closed as a current) but its intersection form **does not** satisfy HR; it is **not** matroidal; it does **not** satisfy the Kähler package.

**The balancing condition (tropical positivity / strongly positive current) does NOT imply the Hodge–Riemann condition.** Balanced = closed and positive; Hodge–Riemann = correct signature. BH shows the implication "tropical positive ⟹ algebraic (correct signature)" **is false in general**, and AHK shows it **is true for the matroidal subtype**. The deciding criterion is: **is the fan matroidal/Lefschetz, or merely balanced?**

### 3.4. Which side does the square of the scaling site fall on?

**[CONSTRUCTION — §3's decisive question.]** The square of the scaling site $X\times X$ is a tropical/characteristic-1 object (Doc 123 §1.1: a semi-ringed topos with a sheaf of 2-dimensional Newton polygons). Its "intersection form" (once it exists, Doc 125) will be a form on the analogue of $\mathrm{NS}(X\times X)$ generated by tropical classes $f_1, f_2, \Delta$, correspondences $\Psi(\lambda)$.

- **Is there a reason for it to be matroidal/Lefschetz?** **NOT known.** [GAP/CONSTRUCTION] The scaling site does not come from a matroid; the flow $\mathbb R_+^*$ is not the structure of a lattice of flats. There is no theorem, nor candidate theorem, saying "the square of the scaling site is of Bergman/matroidal type." The positivity in the CC corpus (Doc 124: Weil positivity, **definite**, on test functions) is exactly of the "balanced/positive" type (spectral positivity), **not** of the "correct $(1,\rho-1)$ signature" type (Hodge–Riemann).
- **The object is of the type where BH obstructs, absent a proof to the contrary.** The intersection form of the square is **precisely** "the intersection form of a tropical surface" — the class of objects where BH demonstrated the signature **can** fail. By default (absent a matroidality theorem), **it falls on the obstructed side.** [CALCULATION]

**[CALCULATION] Verdict §3:** Babaee–Huh **OBSTRUCTS generically** the inference "tropical positivity ⟹ Hodge index," and the square of the scaling site **has no known credential for being on the AHK side** (matroidal). Hence one **cannot assume** that its intersection form has signature $(1,\rho-1)$: that would be **assuming what must be proved**, and BH shows it is **false** in the generic tropical world. The only way out toward (a) is to prove the square is of the matroidal/Lefschetz subtype — a conceivable but today absent theorem. This is the crucial difference with function fields (§4.4), where the surface is genuinely algebraic and the Hodge index is automatic.

---

## 4. THE IRREDUCIBLE CORE [the central deliverable]

### 4.1. The exact statement that would give G2

**[CONSTRUCTION — the isolated core].** Combining §1.1 (Hodge index = HR in middle degree) and §3 (matroidal/Lefschetz criterion):

> **CORE-G2.** *The tropical Chow ring of the square of the scaling site $A^\bullet(X\times X)$ (once constructed, Doc 125) is a graded ring with Poincaré duality, ample class $\ell=f_1+f_2$, satisfying the **Hodge–Riemann relations in middle degree**: the intersection form $D\cdot D'$ on $A^1(X\times X)$ has **signature $(1,\rho-1)$**, **negative** definite on the primitive part $P^1=(f_1+f_2)^\perp$.*

From CORE-G2, G2 = purity follows exactly as for Weil: applied to the graph correspondence of the flow $\Gamma_F$ and its iterates/transposes, negative definiteness on the primitive part forces the Cauchy–Schwarz (Castelnuovo) inequality giving $\mathrm{Re}(\rho)=1/2$ (weight-1 purity) — Doc 119 R-WEIGHT(b-i); Doc 124 §1.2. **CORE-G2 ⟹ G2 ⟹ purity ⟹ RH.** [ASSUMED-FROM-125: existence of the ring $A^\bullet$ with a product; here I evaluate the **strategy for proving the signature**, not the construction of the ring.]

### 4.2. R-NC applied to CORE-G2, with maximum rigor

I apply the non-circularity test of Doc 119 §4.3. The critical question of all of Phase 41 is decided **within NC2 and NC3**.

**NC1 (externality of the definition).** The definition of $A^\bullet(X\times X)$, of the intersection form $D\cdot D'$, and of the ample class $f_1+f_2$ is **functorial from the site** (product topos, Newton polygons): it mentions neither ζ nor its zeros. **PASSES** — same as Castelnuovo (the intersection form of $C\times C$ does not mention which curve $C$ is). [CALCULATION]

**NC2 (overgeneration) — THIS IS WHERE THE VERDICT IS DECIDED.** The discriminator (Doc 119 NC2; Castelnuovo model): is the signature $(1,\rho-1)$ proved for **EVERY** class in $A^1(X\times X)$ / every correspondence, by a uniform method that ignores ζ? Two mutually exclusive scenarios:
- **(NC2-A) The signature is a theorem of the tropical Chow ring, valid for every class.** Then it overgenerates (holds for general correspondences, not only $\Gamma_F$), exactly as AHK proves HR for **the entire** middle degree of the Bergman fan, not for a distinguished class. **PASSES NC2 with content.** This is path (a).
- **(NC2-B) The signature can only be established by evaluating the form on the correspondences of ζ.** Then it does NOT overgenerate: $P$ is a statement about ζ disguised as a surface statement. **FAILS NC2.** This is path (b).

**The current state falls into a zone where NC2-B is the only one available**, by the result of §3.4: **there is no theorem giving the signature for every class** (that would require matroidality/Lefschetz of the square, absent), and BH shows that for a generic tropical surface the signature **is false** for general classes. Hence, today, the only conceivable way to "have" the signature on the primitive part is to **postulate it on the classes that matter** (those of ζ) — which is NC2-B.

**NC3 (non-reduction to catalogued RH-equivalent positivities) — the blow.** The intersection form on the primitive part, **restricted to the flow correspondences** $\Gamma_F$, evaluated as Weil uses it, **IS** Weil positivity. Doc 124 §2.5 already established that global Weil positivity is **MW-1** of the catalog (= Weil's criterion = RH) and its semilocal uniformization is **MW-6**. Therefore:
> In the NC2-B scenario, $P|_{\text{correspondences of }\zeta}$ = Weil positivity = MW-1. **FAILS NC3 outright.** It is Doc 124's spectral-positivity reappearing in surface language — exactly what the master quantifier P43 predicts (Doc 119 §4.2: every property internal to ζ implying weight-1/2 is RH-equivalent).
> In the NC2-A scenario, $P$ is a property of the Chow ring **independent of ζ**; the chain $P\Rightarrow$ purity has Castelnuovo as a link, which does **not** appear in the NO-GO-LIST (it is a surface theorem). **WOULD PASS NC3** — but NC2-A requires the absent matroidality theorem.

**NC4 (two-worlds test).** In the ¬RH world (an off-critical quadruple), is $P$ false for a reason computable from $A^\bullet$ without localizing the zero?
- **NC2-A:** yes — a Frobenius/flow eigenvalue with $\mathrm{Re}(\rho)\ne1/2$ would produce a class with a self-intersection of the forbidden sign on the primitive part, visible in the form without localizing the zero (Castelnuovo model, Doc 124 §1.2). **WOULD PASS NC4.**
- **NC2-B:** no — to decide whether the Weil form is negative one must evaluate where the zeros are (Doc 124 §2.5; inaccessible binarity Doc 108). **FAILS NC4.**

**[CALCULATION] R-NC result:** the verdict is **entirely conditional on the NC2 scenario**:
- If the signature is a **geometric theorem of the square for every class** (NC2-A): it passes NC1, NC2, NC3, NC4 ⟹ **not circular** ⟹ G2 attainable-in-principle.
- If the signature can only be established **on the correspondences of ζ** (NC2-B): FAILS NC2, NC3, NC4 ⟹ **it is Weil positivity renamed** ⟹ circular.

**And §3.4 shows only NC2-B is available today**, because (i) there is no theorem of matroidality of the square, and (ii) BH proves that for generic tropical surfaces the signature is **false** for general classes, so an NC2-A theorem would have to **exclude** the BH case by proving the square is of the good subtype.

### 4.3. Is CORE-G2 a genuine theorem or RH-equivalent in disguise?

**[CALCULATION — the brutally frank answer].** The master quantifier P43 (Doc 119 §4.2) **predicts it reappears**: every property verifiable without zero positions that implies RH must come from a structure **external** to ζ; internal ones are RH-equivalent. The question is whether CORE-G2 is external (genuinely geometric) or internal (Weil renamed).

**It reappears, unless the square is genuinely of the AHK type.** The analysis of §3.4 + §4.2 shows:
- CORE-G2 **in the abstract** (signature for every class) is a **genuine** tropical Kähler-package theorem, of the AHK type — **external**, overgenerating, not circular. It is a **conceivable** statement (AHK proved something analogous for matroids by new methods).
- CORE-G2 **for our concrete object** only becomes plausibly-non-circular **if** it is proved that the square of the scaling site is of the matroidal/Lefschetz subtype. **Without that intermediate theorem**, the only way to "have" the signature is on the correspondences of ζ = Weil positivity = circular.

**Therefore the irreducible core shifts one level:** it is not "proving the signature," but **"proving that the square of the scaling site is of the subtype where the Hodge index holds (tropical matroidal/Lefschetz), and NOT of the BH subtype where it fails"**. THAT is the irreducible statement. And it decides between (a) and (b):
- if that subtype-theorem is **external** (a property of the site independent of ζ, that overgenerates) ⟹ (a) attainable;
- if the only evidence that the square is on the good side is that "the Weil form is positive" ⟹ (b) circular, because positive Weil form IS RH.

### 4.4. Where the analogy with function fields breaks down / holds up

**[CALCULATION — the exact localization, the central point].**

**In function fields (where it worked), Castelnuovo is NOT circular because:**
1. $C\times C$ is a **genuine smooth projective algebraic variety** over $\mathbb F_q$. [Classical DATA]
2. It has a **complete Grothendieck intersection theory**: $\mathrm{NS}(C\times C)$, intersection form $D\cdot D'$, fundamental class, Poincaré duality — all **given by the algebraic geometry**, prior to and independent of ζ. [DATA]
3. The **Hodge index theorem for surfaces** (signature $(1,\rho-1)$) is a **classical theorem** (Hodge; Segre; Grothendieck *Sur une note de Mattuck–Tate* 1958), valid for **every** projective surface, proved **without** mention of L-functions. It is **automatic NC2-A**: the index holds for every class, by geometry. [DATA]
4. The surface is of the **AHK subtype** automatically: smooth projective surfaces **always** satisfy the Hodge index (it is the classical theorem); there is no analogue of BH's failure in the genuine algebraic world. **The BH case cannot occur for a smooth projective algebraic surface** — only for **tropical** surfaces not coming from a variety.

**For Spec ℤ (where we do not know), the analogy BREAKS exactly at point (3)–(4):**
- The "square" is **tropical/characteristic 1** (semi-ringed topos, Newton polygons), **not a genuine algebraic variety**. [DATA Doc 123 §1.1]
- Its intersection theory **is precisely what is missing** (Doc 123 §6.2: the intersection norm = (C-rank) = G2 does not exist in the corpus; CC declare it *in development*). [DATA]
- The Hodge index is **NOT automatic**: BH demonstrates that for tropical surfaces the Hodge index **can fail** (the signature can be wrong). Step (3)–(4) of function fields —"every surface satisfies the index"— **has no tropical analogue**: in the tropical world only the matroidal/Lefschetz subtype satisfies it. [DATA §3]

**The analogy holds in (1)–(2) only partially** (there is a candidate NS and form, via Doc 125), but **it breaks at (3)–(4)**: the theorem that is free in function fields (Hodge index for every surface) is in the tropical world **false in general** (BH) and **open in particular** (is the square of the good subtype?). **That is the exact point of rupture:** genuine algebraic geometry gives the Hodge index for every surface; tropical geometry gives it only for the matroidal subtype, and the square of the scaling site has no credential of belonging to that subtype. The difference $\mathbb Z$ vs $\mathbb R$ (discrete vs continuous flow, Doc 119 T4) reappears here as the difference "algebraic vs tropical / automatic Lefschetz vs Lefschetz to be proved."

---

## 5. VERDICT

### 5.1. Classification (a)/(b)/(c)/(d)

**[CALCULATION] Verdict: (d) undeterminable today, with a strong structural bias toward (b)/(c), and a single narrow but conceivable path toward (a).** Breakdown by sub-question:

- **Does AHK apply?** **NO** (§2). Infinity + continuous flow breaks the finite induction at its root (no base case; signature not rigid at infinite rank); the Chow ring with a product (=G2), AHK-PD (top degree + non-degeneracy = G2), and the intrinsic notion of ampleness are all missing. Third independent derivation of the same wall (R-SIG ≺ R-FIN).

- **Does Babaee–Huh obstruct?** **YES, generically** (§3). BH proves "tropical positivity ⟹ Hodge index" is **false in general** for tropical surfaces (wrong signature). The square of the scaling site **has no known credential of matroidality/Lefschetz**, so it falls by default on the obstructed side. The positivity in the corpus (Weil, definite, spectral, Doc 124) is of the "balanced" type, not the "Hodge–Riemann" type.

- **The exact irreducible core** (§4.3): it is **NOT** "proving the signature $(1,\rho-1)$"; it is **"proving that the square of the scaling site is of the tropical matroidal/Lefschetz subtype where the Hodge index holds (and NOT of the Babaee–Huh subtype where it fails), by a property external to ζ that overgenerates"**. If that subtype-theorem exists and is external ⟹ (a); if the only evidence of being on the good side is Weil positivity ⟹ (b) circular.

- **R-NC verdict** (§4.2): conditional on the NC2 scenario. **NC2-A** (signature for every class, geometric) ⟹ passes everything ⟹ not circular. **NC2-B** (signature only on correspondences of ζ) ⟹ FAILS NC2/NC3/NC4 ⟹ **the positivity on the primitive part = Weil positivity = RH-circular**. **Today only NC2-B is available** ⟹ the current state is **(b) circular**, and (a) requires the absent subtype-theorem.

### 5.2. Is the index on the primitive part genuinely geometric or RH-circular Weil positivity?

**[CALCULATION — the direct answer required].** **Today: RH-circular (Weil positivity in disguise).** Without a theorem establishing the signature **for every class of the Chow ring** (NC2-A, = the matroidal/Lefschetz subtype), the only way to assert "the form is negative on the primitive part" is to restrict it to the correspondences of ζ and observe that the Weil form is positive — which **is** RH (MW-1). The master quantifier P43 reappears **here**, as predicted, because there is (still) no genuine geometric framework evading it: unlike function fields, where algebraic geometry gives the index for every surface for free, here the "square" is tropical and its Hodge index **is not free** (BH) and **is not constructed** (Doc 123).

**The genuine geometric framework would only evade this IF** it is proved —externally to ζ, by new combinatorial/tropical mathematics of the AHK type— that the square of the scaling site is of the subtype where the Kähler package holds. That is **conceivable** (AHK is the precedent) but today **absent**, and obstructed by the infinite dimension / continuous flow (§2.4) that no existing AHK-type theorem covers.

### 5.3. Consequence for the program and list of what would be missing

**[CONSTRUCTION] Consequence:** Phase 41 ("BUILD G2") has a well-defined goal but an **irreducible core that has shifted**: it is not constructing the form (Doc 125) nor directly proving its signature, but **proving the object is of the tropical Kähler-package subtype** — and that theorem, if it exists, must be **external** (NC2-A) to avoid being circular. The current state (NC2-B) is frankly **circular**: it coincides with Doc 124 (Weil positivity = spectral = circular), Doc 123 (the intersection norm = G2, absent), and Doc 80 (arithmetic Castelnuovo–Severi: the form distinguishing the measures is RH-equivalent). **Four independent derivations, same verdict.**

**List of what would be missing (to move from (b)/(d) toward (a)):**

1. **[GAP — Doc 125] The intersection form as an object:** a tropical Chow ring $A^\bullet(X\times X)$ with a graded product, top degree $\cong\mathbb R$, non-degenerate PD. This is the prerequisite for everything (without it HR cannot even be stated). Doc 125 constructs it.

2. **[CONCEPTUAL GAP — the real core] A "tropical matroidality/Lefschetz theorem" for the square:** a statement, external to ζ, that the square of the scaling site satisfies the Hodge–Riemann relations **for every class** (not only those of ζ). It must **explicitly exclude** the BH case (prove the signature is correct, not wrong). It is new mathematics, without precedent for infinite-dimensional objects with continuous flow.

3. **[GAP — the hardest, §2.4] An infinite-dimensional version of the Kähler package** giving "signature of the finite impure block inside an infinite $H^1$" (R-SIG ≺ R-FIN). AHK is finite; here the pure part is infinite. No AHK-type theorem covers this. It is the central obstruction, and it coincides with T1/T2 of Doc 119.

4. **[VERIFICATION] The matroidal criterion on the site:** does there exist any lattice-of-flats / natural submodularity structure on the scaling site making it matroidal? If NOT (the likely case), the square falls on the BH side and G2 is **obstructed** (verdict (c)), not merely undetermined. Deciding this is the most informative experiment of Phase 41.

5. **[CONSULTATION to CC] The status of the "intersection theory of divisors on the square of the Scaling Site" (declared *in development*, 2006.13771):** if its intersection form is defined as a **regularized limit**, tension T2 (signatures do not survive limits without a gap) attacks exactly there — and BH is the warning that the signature can come out wrong.

---

## 6. Synthesis and candor

No new geometric theorem has been proved here. What has been **read in source** (AHK arXiv:1511.02888 + surveys Eur–Larson and arXiv:2211.05724; Babaee–Huh arXiv:1502.00299 verbatim Thm 1.1, 1.3, 1.5, Huh14 Thm 38 via BH) and **calculated**:

- **AHK does NOT apply** to the square of the scaling site: the method is a **finite polyhedral induction** (finite lattice of flats, deformation of the ample class in a finite-dimensional connected cone, signature rigidity at finite rank); the site is **infinite-dimensional with continuous flow**, which kills the induction at its root. Also missing are the Chow ring (product = G2) and AHK-PD.
- **Babaee–Huh OBSTRUCTS generically:** "tropical positivity ⟹ Hodge index" is **false** for tropical surfaces (wrong signature). The criterion separating the good side (AHK) from the bad (BH) is **matroidality/Lefschetz**; the square of the scaling site **has no matroidality credential**, so it falls by default on the obstructed side.
- **The irreducible core** is not "proving the signature" but "**proving the square is of the tropical Kähler-package subtype where the index holds, by a property external to ζ that overgenerates**". Subjected to R-NC: if that theorem is external (NC2-A) ⟹ not circular ⟹ (a); if the signature can only be had on the correspondences of ζ (NC2-B) ⟹ **it is Weil positivity = RH = circular**.
- **Today only NC2-B is available** ⟹ the index on the primitive part is, in the current state, **RH-circular Weil positivity** (coinciding with Docs 124, 123, 80 — four derivations).
- **The analogy with function fields breaks at point (3)–(4) of §4.4:** there, genuine algebraic geometry gives the Hodge index for **every** surface for free (Castelnuovo not circular, automatic NC2-A); here the square is **tropical**, its index **is not free** (BH can break it) and **is not constructed**. The master quantifier P43 reappears exactly where the geometry stops being genuine and becomes tropical-without-guaranteed-index.

**The point of obstruction IS the result:** G2 is not provably obstructed (it has not been proved that the square is on the BH side), but **there is no credential that it is on the AHK side**, and the infinite dimension breaks the only method (AHK) that combinatorially proves Kähler packages. The frank verdict is **(d) undeterminable, with the current state at (b) circular**, and the path to (a) passing through two theorems absent today: the intersection form (Doc 125) and, on top of it, an external infinite-dimensional tropical matroidality/Lefschetz theorem excluding the Babaee–Huh case.

---

## References

**Primary source read this session, via WebFetch/WebSearch on arXiv and surveys, and Read on the BH PDF):**
- K. Adiprasito, J. Huh, E. Katz, *Hodge theory for combinatorial geometries*, arXiv:1511.02888; Annals of Math. 188 (2018) 381–452 — Kähler package (PD+HL+HR) for the Chow ring of a matroid; proof by simultaneous induction without algebraic geometry; resolution of Heron–Rota–Welsh and Mason–Welsh. **[DATA via abstract + surveys]**
- C. Eur, M. Larson, *Combinatorial Hodge theory* (survey), Notices AMS — structure of $A^\bullet(M)$, grading $0..r-1$, PD, ample class, simultaneous induction, indefinite signature in middle degree, essential finiteness (finite rank, finite simplicial fan). **[DATA]**
- *Essence of independence: Hodge theory of matroids since June Huh* (survey), arXiv:2211.05724 — confirms the Chow-ring structure and simultaneous induction of the three properties. **[DATA]**
- F. Babaee, J. Huh, *A tropical approach to a generalized Hodge conjecture for positive currents*, arXiv:1502.00299v3 (22 Mar 2017); Duke Math. J. 166 (2017) — Abstract ("tropical surface in $\mathbb R^4$ whose intersection form does not have the right signature in terms of the Hodge index theorem"); HC/HC′/HC⁺ and Demailly Dem82/Dem12; **Theorem 1.1** (4-fold toric + strongly positive $(2,2)$ current not approximable, extremal ray); Theorem 1.3 (balanced ⟺ closed); **Theorem 1.5** (class = recession); §5 (Laplacian matrix of a 2-dim tropical surface, balancing condition $d_i u_i=\sum w_{ij}u_j$); **Huh14 Thm 38** (Bergman fan of a simple matroid = strongly extremal; Demailly's first extremal example = rank-2-on-3-elements matroid). **[DATA verbatim, pp.1–5]**

**Internal (backward-only):** Doc 124 (intersection-positivity [GOOD] vs spectral-positivity [CIRCULAR]; Weil positivity = MW-1/MW-6; CC's form is definite not indefinite; §1.1 classical Hodge index, §1.2 how Weil uses Castelnuovo, §2.5 R-NC on CC); Doc 123 ((C-cok)/(C-rank) bifurcation; $H^1_{\mathrm{tol}}$ conditional A1–A3; §6.2 the intersection norm = G2 absent; "the numerical part of G1 and G2 are the same object"; §4.1 $C_p$ without $H^1$; no tropical Künneth); Doc 119 (R-SIG/R-FIN/R-LEF/R-WEIGHT/R-NC NC1–NC4; order R-SIG ≺ R-FIN; §2.3 realizations (i)/(ii)/(iii); §4.2 master quantifier P43; tensions T1, T2, T4; §6.1 table, row R-WEIGHT(b) Castelnuovo / Deligne); Doc 80 (arithmetic Castelnuovo–Severi; Prop. 8.1; Weil's Step A/Step B; the RH-equivalent measure difference); Doc 120/122 (Pontryagin duality without symmetry; intersection theory *in development*); roadmap-rh (G1–G4, S1–S3); P35 (κ(Q)=2m); P43/P44 (master quantifier).

**Classical (context, not re-verified in source this session):** Hodge index theorem for projective surfaces (signature $(1,\rho-1)$); Grothendieck, *Sur une note de Mattuck–Tate*, J. reine angew. Math. 200 (1958); Weil 1948 (Castelnuovo–Severi on $\mathrm{NS}(C\times C)$); Demailly (HC for positive currents, Dem82/Dem12).

*End of Doc 126.*
