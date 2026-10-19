# Doc 123 — Construction of the cohomology of the square via tolerance

**Program:** Riemann Hypothesis — Phase 40: attempting to CLOSE G1.
**Prerequisites:** Doc 119 (axioms R-SIG, R-FIN, R-LEF, R-WEIGHT, R-NC; dependency order; tension T1); Doc 120 (in-source inventory of the CC/CCM corpus; §6.3 obstacle of the square; §3.2 absolute RR with tolerance); Doc 121 (Crossing B, rated TECHNICAL with nil RH risk; the 5 steps; the test case C_p × C_p; the 121.E experiment of Crossing A).

**Labeling discipline (absolute rule):[DATA]** = read in source this session (arXiv, with citation; or internal program theorem with backward-only citation). **[CONSTRUCTION]** = my own design, with explicit status (what it assumes, what it defines, what remains to be verified). **[GAP]** = what is missing, with precision. **[CONJECTURE]** = what I believe without deriving. **[NOT VERIFIED]** = from memory or not found in source. **NEVER "proved".** The objective is NOT to declare G1 closed: it is to construct everything constructible and precisely isolate the core that is missing. If the construction gets stuck, the sticking point IS the result.

---

## 0. Executive summary

This document attempts to construct the H¹ of the square X × X of the scaling site by handling Connes–Consani's (CC) "null elements" with the tolerance technique, and ends at outcome **(iii) PARTIAL**, with the core isolated.

The source finding that organizes everything (§1.3): CC themselves name the **root** of the null-elements obstacle — *"The root of this problem had been already unearthed in the Example 6.5 of [yoshi]"* (1805.10501, Introduction) **[DATA]**. That example (in the style of tropical / Yoshida-type literature) exhibits **pairs (C, D), (C′, D′) of tropical curves and divisors whose rank invariants r(D), r(D′) DIFFER even though the modules H⁰ are isomorphic** **[DATA]**. That is: the root of the obstacle is NEITHER analytic NOR one of size — it is that **the isomorphism of idempotent modules does not see the tropical rank**. The "null element" (the absorbing element −∞ of max-plus) is the vehicle: it allows Čech cocycles whose "vanishing" is not a linear condition, and those parasitic cocycles change the rank without changing the module's isomorphism class.

Central diagnosis (§3): tolerance (2205.01391) is exactly a **cokernel repairer** for a *presented* short complex ψ — it neutralizes the obstruction "there is no good quotient in the idempotent world". This **overlaps** with one half of the square's obstacle (the "ill-defined cokernel" half) but **does not touch** the other half (the non-invariance of rank under module isomorphism = absence of a functorial dimension). Tolerance kills the null elements *when H¹ is presented as the cokernel of a single morphism with controlled norm*; it does not kill them when they appear as Čech cocycles of a cover with multiple intersections, which is the genuine regime of dimension 2.

The test case C_p × C_p (§4): the calculation is frank but **gets stuck at the step of presenting the Čech complex of the square as a single ψ**. In dimension 1 (C_p) there is no H¹ at all (its role is played by H⁰(−D), §2.4) **[DATA]**; on the square, a naive Künneth produces a term H¹(C_p) ⊗ H⁰(C_q) that **does not exist as an object** because H¹(C_p) is not defined. Conclusion: the square does not inherit its H¹ from the factors; it has to be built *de novo* on the cover of the product, and there the absorbing cocycles reappear.

Finiteness (§5): the only finiteness attainable in G1 is the **finiteness of the Čech groups graded by degree/support** of the cover — a combinatorial finiteness of the nerve, NOT the finiteness of the impure part (R-FIN), which needs the weight grading (G2) that we do not have. I distinguish them precisely.

Missing core (§6): **two** pieces, one TECHNICAL and one CONCEPTUAL. (a) [TECHNICAL] present the Čech complex of the square as a complex of Γ-𝕊-modules with tolerance (base change from idempotent semirings to Γ-rings in dimension 2). (b) [CONCEPTUAL] the real core: a **functorial notion of dimension/rank invariant under isomorphism** on the square — exactly what Example 6.5 of [yoshi] shows does NOT exist naively, and what tolerance provides in dim 1 (dim_𝕊 = minimum number of generators with norm) but not obviously in dim 2.

---

## 1. STEP 1 — The square and the obstacle, in source

### 1.1. What exactly "the square" is for CC

**[DATA]** (1805.10501, Introduction, textual): *"in the process to formulate a Riemann-Roch theorem on the square of the Scaling Site one faces a substantial difficulty."* This sentence is the only characterization: the "square of the scaling site" appears as the object on which a Weil-type RR is wanted (the characteristic-zero adaptation of Weil's proof via Mattuck–Tate and Grothendieck, §6.3 of Doc 120). **CC do NOT construct the square as a finished object in this paper.** They name it as a goal and declare the difficulty. **[DATA]**

What DOES exist in the corpus as a precedent for the square **[DATA]** (Doc 120 §1.3, §6.1; 1502.05580 §6):
- The square of the **arithmetic site** exists as a **semi-ringed topos**: the non-reduced square carries structure sheaf $\mathbb Z_{\min} \otimes_{\mathbb B} \mathbb Z_{\min}$; the reduced one has **Newton polygons** (convex-hull operations) as its sections.
- Its points over $\mathbb R_+^{\max}$ are the **product** of the points of the site (Prop. 6.11).
- The Frobenius correspondences $\Psi(\lambda)$ live on it as subvarieties, with exact composition only for $\lambda\lambda' \notin \mathbb Q$.

**[CONSTRUCTION] (status: reading of the source, not a CC claim).** The "square of the scaling site" that Weil's RR needs is the scaling analogue (scalar extension to $\mathbb R_+^{\max}$) of the square of the arithmetic site: the **fiber product of the scaling site's topos with itself over the base** (over $\mathbb B$, or over $\mathbb R_+^{\max}$ after extension), with structure sheaf the idempotent tensor product $\mathcal O \otimes_{\mathbb B} \mathcal O$ of the sheaves of piecewise-affine convex functions. Its local sections are two-dimensional Newton polygons (convex hulls in $\mathbb R^2$ of piecewise-affine convex functions in each variable). **What remains to be verified:** that this tensor product commutes with tropicalization and with the hull operation (it is Step 1 of Crossing B's verification program, Doc 121 §2.2.2; declared risk there: "the tensor product over 𝔹 and the product over 𝕊 may not commute with tropicalization"). **[TECHNICAL GAP]**, see §6.

### 1.2. The Čech cover and the complex

**[DATA]** (1805.10501, §2, textual): *"In [CC5] we have developed the beginning of a general homological algebra machine in characteristic one (i.e. for tropical structures) exactly to aim for a definition of the above H¹. In particular, we proved the existence of non trivial Ext-functors and we were also able to input the resolution of the diagonal to obtain the tropical analogue of the Čech complex."* Here [CC5] = **arXiv:1703.02325, *Homological algebra in characteristic one*** (Higher Structures 3 (2019) 155–247) **[DATA]**.

**[DATA]** (1703.02325, abstract + source search): the base category is $\mathbb B\text{mod}$, modules over the Boolean semifield $\mathbb B = \{0,1\}$, *"the replacement for the category of abelian groups"*. $\mathbb B\text{mod}$ *"fulfills analogues of the axioms AB1 and AB2 for abelian categories"* but **is semi-additive, not additive**: there is no subtraction (idempotency $a \oplus a = a$). They build Ext via *"a precise comonad on Bmod"* and the associated Kleisli and Eilenberg–Moore categories. **[DATA]**

**[CONSTRUCTION] (status: synthesis of the two previous data points).** CC's tropical Čech complex for a cover $\mathcal U = \{U_i\}$ of the square is the idempotent cosimplicial complex
$$ \check C^0 = \prod_i \mathcal O(U_i) \;\to\; \check C^1 = \prod_{i<j} \mathcal O(U_{ij}) \;\to\; \check C^2 = \prod_{i<j<k}\mathcal O(U_{ijk}) \;\to\cdots $$
with differential $\delta$ = alternation of restrictions, **computed with $\oplus = \max$ instead of the signed alternating sum** (there are no signs in characteristic 1). $H^0 = \ker\delta^0$ (global sections), $H^1 = \ker\delta^1 / \mathrm{im}\,\delta^0$ **— and here is the problem**: "$/\mathrm{im}\,\delta^0$" is a quotient that in $\mathbb B\text{mod}$ is not well defined (there is no subtraction; the categorical cokernel does not coincide with the set-theoretic quotient). **[DATA that the quotient is problematic: 1703.02325, semi-additivity without subtraction]** + **[CONSTRUCTION: the identification that THAT is where the null elements enter]**.

### 1.3. The EXACT obstacle — the null elements and their root

**[DATA]** (1805.10501, Introduction, full textual quote with the context missing in Doc 120):

> *"The problem, which is still open at this time, has to do with an appropriate definition of the sheaf cohomology (as idempotent monoid) $H^1$... when applied to Čech covers, the presence of the null elements creates unwanted contributions to the cohomology which so far we are unable to handle. **The root of this problem had been already unearthed in the Example 6.5 of [yoshi].**"*

**[DATA]** (1805.10501, description of that Example 6.5, textual per the extracted source): *"This example provides pairs (C,D), (C′,D′) of tropical curves and divisors on them, for which the tropical invariants r(D) and r(D′) ... are different, while the modules themselves are isomorphic."*

This is decisive and reorients the whole attack. **What the null elements are and why they obstruct, precisely:**

1. **What they are [DATA].** The "null element" is the absorbing element of the idempotent semiring: $-\infty$ in max-plus $\mathbb R_{\max} = (\mathbb R \cup\{-\infty\}, \max, +)$ (the "0" of the semiring: $-\infty \oplus x = x$, $-\infty \otimes x = -\infty$). In an idempotent module it is the neutral element of $\oplus$.

2. **In which degree they appear [DATA].** In **degree 1**: *"unwanted contributions to the cohomology"* in $H^1$ (the context is the definition of $H^1$). **[DATA]** (the phrase is in the paragraph about $H^1$).

3. **Why they cannot be handled — the root [DATA + CONSTRUCTION].** Example 6.5 says that **two divisors with isomorphic H⁰ modules can have different tropical ranks**. Translation into the Čech machinery: the isomorphism class of the cocycle module **does not determine the cohomological invariant**. The concrete mechanism **[CONSTRUCTION, status: my reading of the why, to be verified by an expert]**: in $\mathbb B\text{mod}$ a cocycle $\zeta \in \ker\delta^1$ is declared "trivial" if $\zeta = \delta^0(\eta)$ for some $\eta$; but since there is no subtraction, "$\zeta - \delta^0\eta = 0$" is not a linear condition — it is replaced by "$\zeta = \delta^0\eta \oplus (\text{null})$", and absorbing $-\infty$ terms inserted in some components allow a NON-trivial cocycle to look trivial (or vice versa). The "null elements" are precisely those $-\infty$ components that a cocycle may have at some intersections $U_{ij}$ but not others: they create parasitic classes because the idempotent cokernel does not quotient them out properly. The consequence is exactly the pathology of Example 6.5: the group $H^1$ (via cokernel) is not an invariant of the object but depends on presentations, and the rank slips away.

**Conclusion of Step 1 [CONSTRUCTION].** The obstacle of the square has **two layers**:
- **(C-cok)** The cokernel $\ker\delta^1 / \mathrm{im}\,\delta^0$ is not well defined in $\mathbb B\text{mod}$ (no subtraction).
- **(C-rank)** Even defining *some* object $H^1$, its numerical invariant (rank/dimension) **is not functorial**: isomorphic modules can give different ranks (Example 6.5). This is the deep layer, the "root" that CC point to.

This split is the key to the Step 3 diagnosis: tolerance attacks (C-cok); the core is (C-rank).

---

## 2. STEP 2 — The tolerance technique, in source, and its abstract mechanism

### 2.1. What tolerance is, exactly

**[DATA]** (2205.01391, Prop. 2.2(ii) and Appendix A, textual per source): for the divisor $D$, with the presentation morphism
$$ \psi:\; H\mathbb Q \times H\mathcal O(D) \;\longrightarrow\; H\mathbb A_{\mathbb Q} $$
(exact analogue of Weil's adelic presentation for function fields), one defines
$$ H^1(D) := (H\mathbb A_{\mathbb Q},\, \mathcal R), \qquad \mathcal R_k := \{(x,y)\in H\mathbb A_{\mathbb Q}(k_+)^2 \;:\; x - y \in \mathrm{Image}\,\psi(k_+)\}. $$
**[DATA]** This is **not a quotient**: it is *"a reflexive relation encoded within the 𝕊-module structure itself"* — the **whole module** $H\mathbb A_{\mathbb Q}$ is **kept**, and the tolerance relation $\mathcal R$ is **added** to it. The object lives in the category $\Gamma\mathcal T_+$ of **𝕊-modules with tolerance**. The construction goes through Dold–Kan (Appendix B): $\psi$, viewed as a short complex, is associated with a Γ-space $H(D)$, and $H^1(D) = \pi_1^{\mathcal T}(H(D))$ as an 𝕊-module with tolerance. **[DATA]**

**[DATA]** (2205.01391, Def. A.2): the **dimension** $\dim_{\mathbb S[\pm1]}$ is the **minimum cardinality of a generating set** $F$ such that every $x$ is written $x = \sum_{f\in F}\alpha(f)f$ with $\alpha(f)\in\{-1,0,1\}$ and norm control $\sum|\alpha(f)f| \le e^a$ (archimedean part of $D$). For $H^0$: $\dim_{\mathbb S[\pm1]}H^0(D) = \lceil \log(2n+1)/\log 3\rceil$ (Prop. 3.3). **[DATA]**

### 2.2. Why it works in dim 1 — the abstract mechanism

**[DATA]** (2205.01391, §2, source reading): *"in arithmetic, elements arbitrarily close to zero create pathologies in classical quotients. Tolerance relations preserve the full module while adding an equivalence structure that does not quotient out the abelian group structure."*

**[CONSTRUCTION] The mechanism of tolerance, stated in the abstract (status: synthesis of the source, to be verified):**

> Tolerance neutralizes a precise class of obstruction: one in which **the cohomological invariant would require a quotient $M/N$ that is ill-defined** (because the category has no subtraction, or because $N$ has a "tail near zero" that a classical quotient collapses pathologically). The replacement "$x\sim y \iff x-y\in N$" **kept as a relation, not carried out as a quotient**, recovers (i) a well-defined object in an enriched category ($\Gamma\mathcal T_+$), and (ii) **a functorial dimension** via "minimum of generators modulo the relation with controlled norm".

Point (ii) is the one that matters for Step 3: tolerance not only repairs the cokernel (i) — **it also restores a functorial numerical invariant** (the $\dim_{\mathbb S}$). In the language of Step 1, tolerance attacks **(C-cok)** directly and **(C-rank) in the particular case of an H¹ presented as the cokernel of a single $\psi$**: there the rank is "minimum of generators with norm", which IS an isomorphism invariant in $\Gamma\mathcal T_+$.

**[Critical delimiting DATA]** (2205.01391, structure): tolerance is applied to a **short complex of length 1** — a single morphism $\psi$ whose cokernel is $H^1$. This is the dimension-1 situation (a curve: $H^0$, $H^1$, and nothing more). **There is, in 2205.01391, no Čech complex of a cover with triple intersections nor anything resembling the complex of §1.2.** CC's $H^1$ in dim 1 is NOT computed by Čech: it is computed by the **adelic presentation** $\psi$ (kernel = $H^0$, cokernel = $H^1$). **[DATA — and this is the hinge of Step 3.]**

---

## 3. STEP 3 — THE CENTRAL DIAGNOSIS: same type of obstacle?

The question that decides Crossing (B): **are the null elements of the square (Step 1) of the same type as the problematic elements that tolerance neutralizes in dim 1 (Step 2)?**

Answer: **(iii) PARTIAL.** I develop the why with the (C-cok)/(C-rank) split of §1.3.

### 3.1. The part that DOES match: (C-cok)

**[CONSTRUCTION, status: structural argument, not a theorem].** Both obstacles share the root "there is no good quotient in the idempotent world":
- In dim 1, the cokernel of $\psi$ is not a legitimate quotient in $\mathbb B\text{mod}$ → tolerance.
- On the square, $\ker\delta^1/\mathrm{im}\,\delta^0$ is not a legitimate quotient in $\mathbb B\text{mod}$ → *in principle*, tolerance.

The formal translation is direct: the Čech complex of the square's cover can be seen as a (longer) complex of 𝕊-modules, and the Dold–Kan machinery CC use for $\psi$ **applies to complexes of any length**, not only to short complexes. This gives:

**[CONSTRUCTION] (the square's tolerant H¹ — conditional construction, status: defines, assumes, leaves to be verified).**
Let $\mathcal U$ be a finite cover of the square $X\times X$ by opens of the product topos. After the base change from $\mathbb B\text{mod}$ (idempotent semirings) to $\Gamma$-rings over $\mathbb S$ (the base change that in dim 1 takes the tropical RR to the absolute RR), the Čech complex $\check C^\bullet(\mathcal U)$ is rewritten as a complex of $\Gamma$-𝕊-modules. Applying Dold–Kan to $\check C^\bullet$ and taking the generalized homotopy with tolerance:
$$ H^1_{\mathrm{tol}}(X\times X,\mathcal O) := \pi_1^{\mathcal T}\big(\mathrm{DK}(\check C^\bullet(\mathcal U))\big), $$
an 𝕊-module with tolerance, **in which cocycles supported on absorbing elements $-\infty$ fall into trivial tolerance classes** (because $\zeta$ with $-\infty$ components satisfies $\zeta - \delta^0\eta \in$ a tolerance band controlled by norm, exactly as in dim 1).
- **Assumes:** (A1) the base change $\mathbb B\to\mathbb S$ is functorial in dim 2 and commutes with the convex hull (Step 1 of the Crossing B program, Doc 121; **[TECHNICAL GAP]**). (A2) Dold–Kan gives the correct object for a complex of length $\ge 2$ with the "$-\infty$ component" tolerance relation (not shown by CC beyond length 1). (A3) independence from the cover $\mathcal U$ (that $H^1_{\mathrm{tol}}$ is an invariant of the square and not of the chosen nerve).
- **Defines:** a candidate object $H^1_{\mathrm{tol}}$.
- **Remains to be verified:** ALL of the above (A1–A3) and, above all, what follows in §3.2.

**This is the best frank construction of "tolerance applies" — and note it is entirely conditional.** It repairs (C-cok). But it does not touch (C-rank), which is the root CC point to.

### 3.2. The part that does NOT match: (C-rank) — the core

**[CONSTRUCTION, status: the decisive argument of this document].**

Tolerance restores a functorial dimension $\dim_{\mathbb S}$ **in dim 1 because there $H^1$ is the cokernel of ONE morphism $\psi$ with a canonical norm $e^a$ (the archimedean part of the divisor)**, and "minimum of generators with $\sum|\alpha f|\le e^a$" is an invariant because **the norm comes from the divisor, an external well-defined datum**.

On the square, Example 6.5 of [yoshi] says precisely that **the tropical rank is not an invariant of the module's isomorphism class** **[DATA]**. For tolerance to fix it, we would need a **canonical norm on the Čech cocycles of the square** playing the role $e^a$ plays in dim 1. And here is the exact sticking point:

> **[CONCEPTUAL GAP — the core].** In dim 1 the norm $e^a$ defining $\dim_{\mathbb S}$ comes from the archimedean part of the **Arakelov divisor** on $\overline{\mathrm{Spec}\,\mathbb Z}$ — a real-degree datum of a **codimension-1** object. On the square, the analogue of "divisor" is a class of **codimension 1 on a surface** (an analogue of $\mathrm{NS}(C\times C)$, the Néron–Severi group), and **there is no canonical norm in the CC corpus on such classes** — that would precisely be an **intersection form** (the dimension-2 Arakelov metric), which is G2 and does not exist (Doc 119 §2.3; Doc 120 §8). Without that norm, "minimum of generators with controlled norm" has no "norm", and tolerance does not produce a functorial dimension: Example 6.5 reappears.

**Therefore:** tolerance handles the (C-cok) half of the obstacle (the syntactic one, "there is no good quotient") and **leaves the (C-rank) half untouched** (the semantic one, "there is no functorial numerical invariant"). And (C-rank) in dim 2 **is not of the same type** as the problem tolerance solves in dim 1, because in dim 1 the norm that rescues functoriality is a codimension-1 datum (the Arakelov divisor), while in dim 2 the analogous datum is an intersection form of codimension 1 on a surface — which is exactly G2.

### 3.3. The exact difference, stated

**[CONSTRUCTION].** I characterize the difference requested in objective outcome (ii), now as a precise statement about outcome (iii):

> **The obstacle of the square decomposes as (C-cok) ⊕ (C-rank). Tolerance is a "repair" isomorphism on (C-cok) in any dimension (conditional on A1–A3). On (C-rank), tolerance depends on the existence of a canonical norm on the cocycles; that norm exists in dim 1 (= the Arakelov divisor, codim 1) and does NOT exist in dim 2 (it would be the surface's intersection form, codim 1 in dim 2 = G2). 1D tolerance is not "non-functorial under products" (A2 is plausible); the problem is that the INPUT that makes it functorial (the norm) is not available in dim 2 without G2.**

This refines the verdict of Doc 121 (Crossing B "TECHNICAL, nil RH risk"): the TECHNICAL part (C-cok, conditional on A1–A3) is real and risk-free with respect to RH; but **underneath the TECHNICAL part lies a dependency on G2** that Doc 121 had not isolated. Crossing B *does not*, by itself, unblock G1: it unblocks the **object** $H^1_{\mathrm{tol}}$ but not its **functorial dimension**, and the dimension is what G1 needs (G1 = *finite-dimensional* cohomology).

**RH risk:** still **nil** in the (C-cok) part. The dependency on G2 I isolate introduces no circularity with RH — it introduces a **phase dependency** (G1 rests on G2 for its numerical part), which is exactly the order $\text{R-SIG}\prec\text{R-FIN}$ of Doc 119 §2.4 reappearing from the side of the square's construction. **[CONSTRUCTION]** + **[DATA Doc 119 §2.4]**. Strong internal coherence: two independent derivations (the reverse engineering of Doc 119 and the direct construction here) reach the same order.

---

## 4. STEP 4 — The test case C_p × C_p

I make the diagnosis concrete on the square of ONE periodic orbit, the scaling site's simplest toy object.

### 4.1. The factors: what exists and what doesn't in C_p

**[DATA]** (1603.03191, §5, Thm 5.6, Thm 5.17):
- $C_p = \mathbb R_+^*/p^{\mathbb Z}$, a quasi-tropical circle of length $\log p$ (in $u=\log\lambda$, the torus $\mathbb R/\log p\,\mathbb Z$). Sheaf $\mathcal O_p$: periodic, convex, piecewise-affine functions, with slopes in $H_p\subset\mathbb Q$ (power-of-$p$ denominator).
- $H^0(D) = \{f\in\mathcal K(C_p): D+(f)\ge 0\}$, an **idempotent module over $\mathbb R_{\max}$**, not a vector space.
- **Continuous real dimension:** $\mathrm{Dim}_{\mathbb R}H^0(D) = \lim_n p^{-n}\dim_{\mathrm{top}}H^0(D)^{(p^n)}$ (normalized Lebesgue covering dimension).
- **RR (Thm 5.17):** $\mathrm{Dim}_{\mathbb R}H^0(D) - \mathrm{Dim}_{\mathbb R}H^0(-D) = \deg D$.
- **THERE IS NO $H^1$ on $C_p$** **[DATA]**: the text does not define it; its role is played by $H^0(-D)$. RR is an identity involving only $H^0$.
- Class group: $\mathrm{Div}(C_p)/\mathcal P \cong \mathbb R\times\mathbb Z/(p-1)\mathbb Z$ (real degree + torsional characteristic).

### 4.2. The computation on the square, step by step, and where it gets stuck

**[CONSTRUCTION].** $C_p\times C_p$ in coordinates $(u,v)\in (\mathbb R/\log p\,\mathbb Z)^2$: a **two-dimensional tropical torus** of area $(\log p)^2$. I want $H^1(C_p\times C_p, \mathcal O)$.

**Attempt A — Künneth.** The natural thing would be
$$ H^1(C_p\times C_p) \;\overset{?}{=}\; \big(H^0(C_p)\otimes H^1(C_p)\big)\,\oplus\,\big(H^1(C_p)\otimes H^0(C_p)\big). $$
**It gets stuck immediately [GAP]:** $H^1(C_p)$ **does not exist** (§4.1). The square **cannot inherit its $H^1$ from the factors** because the factors have no $H^1$ — they have a type-II RR that *avoids* $H^1$ by using $H^0(-D)$. The duality $H^0(-D)$ is a scalar substitute for $H^1$ that **does not tensor** (it is not an object, it is the other side of a dimension subtraction). Partial conclusion: **there is no tropical Künneth available**; the square's $H^1$, if it exists, is genuinely two-dimensional and must be built on the cover of the product.

**Attempt B — Direct Čech on the 2D torus.** I take the minimal cover of the torus $(\mathbb R/\log p\,\mathbb Z)^2$ by, say, four open rectangles $U_{00},U_{01},U_{10},U_{11}$ (the standard cover computing the torus's simplicial cohomology: nerve = the torus as a CW complex with 1 zero-cell, 2 one-cells, 1 two-cell). The idempotent Čech complex:
$$ \check C^0 = \textstyle\prod_i \mathcal O(U_i),\quad \check C^1 = \prod_{i<j}\mathcal O(U_{ij}),\quad \check C^2 = \prod \mathcal O(U_{ijk}). $$

**What would be computed WITHOUT tolerance (underlying topological cohomology) [CONSTRUCTION, symbolic toy computation]:** the real torus $T^2=(\mathbb R/\log p\,\mathbb Z)^2$ has $H^1(T^2;\mathbb R)=\mathbb R^2$, $H^2=\mathbb R$. I develop the complex explicitly. With the four-chart cover $U_i$ ($i=00,01,10,11$), the sections of $\mathcal O$ on a chart are piecewise-affine convex functions $f(u,v)$ with $\partial_u f,\partial_v f\in H_p$. The $\delta^0$ coboundary of a $0$-cochain $(f_i)_i$ is, in characteristic 1,
$$(\delta^0 f)_{ij} = f_j|_{U_{ij}} \;\text{"}{-}\text{"}\; f_i|_{U_{ij}},$$
where the "subtraction" is the problem: it does not exist in $\mathbb R_{\max}$. The idempotent substitute for "cocycle" is the condition of **slope compatibility** at the overlaps: a $1$-cochain $(\zeta_{ij})$ is cocyclic if the slope jumps cancel around each $2$-cell. The solutions modulo coboundaries are indexed by the **two slope-monodromy classes** around the two generating cycles $\gamma_u:u\mapsto u+\log p$ and $\gamma_v:v\mapsto v+\log p$: each class corresponds to the **net slope increment** $\oint_{\gamma}\!d(\partial f)\in H_p$ after going around the cycle. That is, **naively**
$$H^1(C_p\times C_p)\;\cong\; H_p\,\gamma_u \;\oplus\; H_p\,\gamma_v \qquad(\text{2 copies of the slope group}).$$
But $H_p=\{m/p^n:m\in\mathbb Z,n\ge 0\}$ is **dense in $\mathbb R$**; taking the type-II continuous dimension (filtration by $p^{-n}$, same as in the RR of §4.1) each copy contributes **real dimension, not integer**, and
$$\mathrm{Dim}_{\mathbb R}H^1(C_p\times C_p)\;=\;2\cdot(\text{type-II continuous dimension of the slope group}),$$
a positive real, not an integer. (The factor $2$ is the two cycles of the torus; each cycle is a $C_p$, so the type-II dimension of one factor reappears.) **[CONSTRUCTION, status: symbolic computation of the torus; the precise definition of the monodromy classes and the type-II normalization in degree 1 remain to be verified.]**

Comparison with the divisor: the above computation is for $\mathcal O$ (trivial divisor); for $\mathcal O(D)$ with $D$ a divisor on the square (a tropical curve inside $C_p\times C_p$, e.g. the diagonal or a correspondence $\Psi(\lambda)$), the classes are twisted by $D$ and the dependency the RR should govern appears — but without a functorial $H^1$ there is no surface RR to write. This is where the toy calculation hits the wall.

**Do null elements appear? YES [CONSTRUCTION].** At the intersections of the rectangles, a section of $\mathcal O(U_{ij})$ can take value $-\infty$ (absorbing) on part of the intersection if the convex function "goes to $-\infty$" there (piecewise-affine convex functions on an idempotent compact set admit the value $-\infty$ as the module's "zero"). A cocycle $\zeta$ with a $-\infty$ component on $U_{01}$ but finite on $U_{10}$ **is the coboundary of no global $\eta$** in $\mathbb B\text{mod}$ (because subtracting $-\infty$ is undefined), and produces a **parasitic class** — exactly the "unwanted contribution" of 1805.10501. **[CONSTRUCTION, status: explicit instance of the mechanism of §1.3 on the 2D torus.]**

**Does tolerance kill them? PARTIALLY [CONSTRUCTION].** With the relation $\mathcal R_k=\{(\zeta,\zeta'):\zeta-\zeta'\in\mathrm{im}\,\delta^0(k_+)\}$ (tolerance: they differ by a norm-controlled coboundary), cocycles differing only in $-\infty$ components fall into the same tolerance class. Concretely: if $\zeta$ has $-\infty$ on $U_{01}$ and $\zeta'$ is finite there but they agree elsewhere, then $\zeta-\zeta'$ is "supported on the absorbing element" and the tolerance relation declares it equivalent to $0$ **without** carrying out the forbidden subtraction (precisely the mechanism of §2.2: keep the module, add the relation). → **the parasitic classes (C-cok) collapse.** This is genuine and is what tolerance contributes.

BUT: to say "the dimension of $H^1_{\mathrm{tol}}(C_p\times C_p)$ is such-and-such a number" I need $\dim_{\mathbb S}=$ "minimum of generators with $\sum|\alpha(f)f|\le N$", and here **there is no $N$**: in dim 1, $N=e^a$ came from the archimedean part of the Arakelov divisor; on the 2D torus **there is no codimension-1 Arakelov divisor on a surface without an intersection form** that could provide the norm. Without $N$, "minimum of generators with norm" degenerates to "minimum of generators" plain — which, by the density of $H_p$ and the freedom of the slopes, is **unbounded / continuous**, not an integer. Result: $H^1_{\mathrm{tol}}(C_p\times C_p)$ **exists as an object with tolerance (parasitic classes collapsed), but its dimension remains real/continuous (type II) and non-integer**, and depends on the normalization as long as the norm is not fixed. Exactly Example 6.5 reappearing: the object $H^1_{\mathrm{tol}}$ is well defined as a module-with-tolerance, but its **rank is not functorial** without the intersection norm.

### 4.3. The result of the test case, unembellished

**[CONSTRUCTION — summary of the toy case]:**
1. **Do null elements appear:** yes, explicitly (cocycles with a $-\infty$ component at the cover's intersections of the torus).
2. **Does tolerance kill them:** yes, as far as (C-cok) is concerned — the parasitic classes collapse to trivial tolerance. The object $H^1_{\mathrm{tol}}$ ends up well defined (conditional on A1–A3).
3. **Is the resulting dimension finite and integer:** **NO.** It remains **real-valued / continuous type II** (due to the density of $H_p$ in $\mathbb R$, identical to the $\mathrm{Dim}_{\mathbb R}$ phenomenon of the tropical RR), because the canonical norm that in dim 1 came from the Arakelov divisor is missing. The dimension is of order "2 × (type-II continuous dimension)" — the "2" from the torus's two cycles, each with continuous dimension.
4. **Künneth does not exist** (the factors have no $H^1$); the square's $H^1$ is genuinely 2D.

**Verdict of Step 4:** the test case **does NOT close G1**. It confirms exactly the Step 3 diagnosis: tolerance delivers the **object** but not the **integer finiteness**; integer finiteness needs the norm = intersection form = G2. **It is the best frank evidence that Crossing B works for (C-cok) and gets stuck at (C-rank).**

---

## 5. STEP 5 — Finiteness (R-FIN): the two finitenesses, distinguished

**[DATA Doc 119 §2.4]:** the **total** $\dim H^1$ must be $\infty$ (infinitely many zeros); what must be finite is the **impure** part (weight $\ne 1/2$, or $\ne 1$ depending on normalization), and the separation into weights **is G2**, which I do not have. I must therefore be frank about **which finiteness** I am addressing.

**[CONSTRUCTION] There are three distinct finitenesses at play, and only the first belongs to G1:**

1. **Combinatorial finiteness of the nerve (G1, attainable).** The finite cover $\mathcal U$ has a finite nerve (in C_p × C_p: 4 opens, finitely many intersections). The Čech groups $\check C^p(\mathcal U)$ are **graded by simplicial degree $p$ and by support** (which intersection), and in each degree the module is of **finite type as a generated idempotent module** (finitely many combinatorial generators: the cover's "tropical monomials"). **This finiteness I DO obtain** (conditional on A1–A3): $H^1_{\mathrm{tol}}$ is a **finitely presented** 𝕊-module with tolerance in the combinatorial sense. It is a finiteness of **presentation**, not of **dimension**.

2. **Finiteness of the type-II dimension (NOT obtained as an integer).** $\mathrm{Dim}_{\mathbb R}H^1_{\mathrm{tol}}$ is a finite real number (it is a compact torus), but **real, not integer** (§4.3). "Finite" in the sense of "bounded real number", yes; "finite" in the sense of G1 ("dimension = integer = rank of an object"), **no**. The norm is missing.

3. **Finiteness of the impure part (R-FIN, NOT attainable in G1).** It requires the weight grading $W$ to define "impure"; without $W$ (= without G2) the statement "$\dim(\bigoplus_{w\ne 1}\mathrm{gr}^W_w H^1) < \infty$" **is not even formulable** (Doc 119 §2.4, "R-FIN is not statable without R-SIG"). **[DATA]**

**Frank statement of which I obtain [CONSTRUCTION]:** I obtain **the combinatorial finiteness of the Čech groups graded by degree/support** (finiteness of type 1), conditional on A1–A3. I do **NOT** obtain the integer finiteness of the dimension (type 2: the norm is missing), much less the finiteness of the impure part (type 3: that is R-FIN, which needs G2). This is exactly what the objective anticipated: "the finiteness attainable in G1 is the finiteness of the Čech groups graded by degree/support, NOT the finiteness of the impure part".

**Consistency with tension T1 (Doc 119 §6.3) [CONSTRUCTION].** T1 states: a totally finite-dimensional $H^1$ cannot carry the trace with singular support at $\{k\log p\}$. My construction is consistent with T1: $H^1_{\mathrm{tol}}(C_p\times C_p)$ has **infinite/continuous** type-II dimension (density of $H_p$), not finite — so it **can** carry the singular support. The finiteness I obtain (type 1, combinatorial) is one of *presentation*, not of the module's *size*. No contradiction with T1. Good.

---

## 6. STEP 6 — THE MISSING CORE: the "G1-remainder"

I close with the exact statement of what was left unconstructed, separating the TECHNICAL from the CONCEPTUAL.

### 6.1. The TECHNICAL part (feasible, nil RH risk)

**[TECHNICAL GAP — T1] The base change in dimension 2.** Verify A1: that the idempotent tensor product $\mathcal O\otimes_{\mathbb B}\mathcal O$ of the square's sheaf can be rewritten as a $\Gamma$-𝕊-module commuting with the convex hull and with tropicalization. It is Step 1 of Crossing B (Doc 121). Known type (CC did it in dim 1).

**[TECHNICAL GAP — T2] Dold–Kan for complexes of length $\ge 2$ with tolerance.** Verify A2: that the machinery $\pi_1^{\mathcal T}\circ\mathrm{DK}$ CC use for the short complex $\psi$ (length 1) gives the correct object for the square's Čech complex (length $\ge 2$), and that cocycles with a $-\infty$ component fall into trivial tolerance. Plausible; known type (Dold–Kan is general).

**[TECHNICAL GAP — T3] Independence from the cover.** Verify A3: that $H^1_{\mathrm{tol}}$ does not depend on the nerve $\mathcal U$. Requires a tolerant Čech comparison theorem (refinements). Known type in topology; new in this idempotent formalism, but with no conceptual risk.

**These three together = "constructing the object $H^1_{\mathrm{tol}}(X\times X)$".** This is what Crossing B promised, and it is genuinely TECHNICAL: it closes (C-cok). The CC team can do it with their 2017–2023 machinery.

### 6.2. The CONCEPTUAL part (the real core)

**[CONCEPTUAL GAP — the core of the G1-remainder] The canonical norm on the square's cocycles = functorial integer dimension.**

Exact statement:
> A **canonical norm** $\|\cdot\|$ on the square's Čech cocycles (or on the classes of the analogue of $\mathrm{NS}(X\times X)$) is missing, such that $\dim_{\mathbb S}H^1_{\mathrm{tol}} := $ (minimum of generators with $\|\cdot\|$ controlled) is **(a) an integer, (b) an isomorphism invariant, (c) computable from the site**. Without it, Example 6.5 of [yoshi] guarantees that the rank is not functorial and G1 (finite-dimensional cohomology, with dimension = integer) is not obtained.

**Why it is CONCEPTUAL and not technical:** that norm, in dim 1, IS the degree of the Arakelov divisor (codim 1, a scalar datum). In dim 2, the analogous codimension-1 datum with a numerical invariant on a surface is an **intersection form** $D\cdot D'$ — which is **exactly G2** (the signature structure, Doc 119 §2.3 realization (i); the "intersection theory of divisors on the square of the Scaling Site" that CC declare *in development* since 2021, Doc 120 §4.4). **There is no candidate in the corpus.** It is new mathematics.

**[CONSTRUCTION — the structural result of this document]:**
> **G1 is not independent of G2.** The construction of the square via tolerance splits G1 into (C-cok), which is TECHNICAL and closable, and (C-rank), whose resolution *is* the intersection norm, which *is* G2. The "wall" is not between G1 and G2 as two sequential nodes: **the numerical part of G1 (integer finiteness) and G2 (signature) are the same object** — an intersection form on the square. Tolerance builds the receptacle; the numerical content of the receptacle is G2.

This matches, via a second independent route, the order inversion of Doc 119 §2.4 ($\text{R-SIG}\prec\text{R-FIN}$: "the G2 wall is upstream of the very formulation of finiteness"). **Two independent derivations, same verdict** — it is the strongest evidence of frankness in the diagnosis. **[CONSTRUCTION]** + **[DATA Doc 119]**.

### 6.3. What is needed from Connes — a concrete list

1. **The full text of Example 6.5 of [yoshi]** (the "yoshi" reference in 1805.10501). The exact bibliographic identification and the example verbatim are needed: it is the most precise existing formulation of (C-rank), and my whole diagnosis rests on reading it correctly. **[Question to CC / pending bibliographic search.]** My reading is that it is an example from the tropical literature (Yoshida-style) where $r(D)$ is not an isomorphism invariant of modules; confirm it and read the exact mechanism.

2. **Is there an unpublished continuation of 1703.02325 (*Homological algebra in characteristic one*) into dimension 2?** Specifically: did they define tolerant Ext / Čech for complexes of length $\ge 2$? If A2 (§6.1) has already been done by them unpublished, T2 closes.

3. **Do they have a canonical norm on codim-1 classes of the square?** This is the core question (§6.2). Their phrase "intersection theory of divisors on the square of the Scaling Site, still in development" (2006.13771) suggests they ARE working on it — it is necessary to know **what state that intersection norm is in**, because it IS the conceptual core of G1+G2.

4. **The treatment of the divergent term $2h(1)\log\lambda$** of 2602.15941 §9.3: if the intersection norm is defined as a regularized limit, that term is where it would be defined — and Doc 119's tension T2 (signatures do not survive gapless limits) attacks exactly there. It is necessary to know whether their regularization preserves a signature.

5. **Clarification on the base change $\mathbb B\to\mathbb S$ in dim 2** (A1): does the square's idempotent tensor product commute with the Γ-ring presentation? It is the only purely technical piece that might hold a surprise (its own "declared risk" in Step 1 of Crossing B).

---

## 7. Synthesis and frankness

**I do not declare G1 closed.** The test case (Step 4) **does not close** and the construction (Step 3) **is not complete**: it produces the object $H^1_{\mathrm{tol}}$ (conditional on three technical gaps) but not its functorial integer dimension.

**What was built (all [CONSTRUCTION], to be verified by experts, NEVER [DATA]):**
- The identification of the **(C-cok)/(C-rank) split** of the square's obstacle, anchored in the source quote about the root (Example 6.5 of [yoshi]).
- The **conditional construction of $H^1_{\mathrm{tol}}(X\times X)$** via Dold–Kan on the tolerant Čech complex (§3.1), with its three assumptions isolated.
- The **toy computation C_p × C_p** (§4): explicit null elements, collapse of parasitic classes by tolerance, dimension that **remains type II / continuous** for lack of a norm.
- The **distinction of the three finitenesses** (§5) and the frank statement that only the combinatorial one is obtained.
- The **isolation of the core** (§6.2): the intersection norm = functorial integer dimension = G2, with the structural consequence that the numerical part of G1 and G2 are the same object.

**The sticking point IS the result:** tolerance builds the receptacle (C-cok, technical); the numerical content of the receptacle (C-rank) is an intersection form that is G2 and does not exist. Crossing B, correctly understood, **is not independent of the wall** — it is its syntactic half.

---

## References

**Internal (backward-only):** Doc 119 (R-SIG, R-FIN, order $\text{R-SIG}\prec\text{R-FIN}$, §2.3–2.4, tension T1/T2); Doc 120 (§1.3, §3.2, §4.4, §6.1, §6.3, §8 — in-source inventory); Doc 121 (Crossing B: 5 steps, case C_p × C_p, §2.2; Crossing A / experiment 121.E); roadmap-rh (G1–G4, S1–S3).

**CC/CCM corpus (read/re-read in source this session, via ar5iv):**
- A. Connes, C. Consani, *The Riemann-Roch strategy, Complex lift of the Scaling Site*, arXiv:1805.10501 — Introduction (the null-elements obstacle; "root ... in Example 6.5 of [yoshi]"); §2 (resolution of the diagonal, tropical Čech, ref. [CC5]); §3.2 (tropical descent); §4 (Bohr almost-periodic functions). **[DATA]**
- A. Connes, C. Consani, *Homological algebra in characteristic one*, arXiv:1703.02325 (Higher Structures 3 (2019) 155–247) [= [CC5]] — $\mathbb B\text{mod}$, AB1/AB2 without AB-additivity (semi-additive, no subtraction), comonad, Kleisli/Eilenberg–Moore, non-trivial Ext. **[DATA]**
- A. Connes, C. Consani, *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$*, arXiv:2205.01391 — Prop. 2.2(ii) (tolerance $\mathcal R_k$); Appendices A (category $\Gamma\mathcal T_+$, Def. A.2 dimension by generators with norm) and B (Dold–Kan); Prop. 3.3; §5 / Prop. 5.2 / Thm 1.2 (Pontryagin duality with tolerance, $K=-2\{2\}$, $U(1)_{1/4}$). **[DATA]**
- A. Connes, C. Consani, *Geometry of the scaling site*, arXiv:1603.03191 — §5 (C_p, $\mathcal O_p$, $\Delta_2 f$), Thm 5.6 (divisor class $\mathbb R\times\mathbb Z/(p-1)\mathbb Z$), Thm 5.17 (type-II RR, $\mathrm{Dim}_{\mathbb R}$, no $H^1$). **[DATA]**
- A. Connes, C. Consani, *Weil positivity...*, arXiv:2006.13771 — "intersection theory of divisors on the square of the Scaling Site, still in development" (via Doc 120 §4.4). **[DATA]**

**Pending identification [NOT VERIFIED]:** the reference "[yoshi]" of 1805.10501 (Example 6.5; conjecturally Yoshida-style tropical literature on divisor rank not being a module-isomorphism invariant). It is source piece #1 to obtain (§6.3).

*End of Doc 123.*
