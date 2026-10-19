# Doc 128 — Deninger's program: is this the missing foliated cohomology?

**Program:** Riemann Hypothesis — Phase 42: new mathematics to cross the wall (dynamical Hodge theory).
**Prerequisites:** Doc 125 (the intersection form over the scaling-site square, via Allermann–Rau; the $\Delta_\mu$ flow; the Gram matrix $G_{\text{toy}}$ of the $C_p\times C_p$ toy model, signature $(1,2)$, negative-definite primitive; gaps G-125.A real/integer, G-125.B signature persistence à la Babaee–Huh); Doc 126 (the Kähler package; AHK does not apply because of infiniteness + continuous flow; Babaee–Huh generically obstructs; the core shifts to "proving that the square is of the matroidal/Lefschetz subtype, external to $\zeta$"; verdict (d) biased toward (b)/(c)); Doc 127 (dynamical Hodge theory/Forni, running in parallel — the synthesis is required in §5); Doc 119 (the R-NC test, clauses NC1–NC4; the master quantifier P43; R-SIG ≺ R-FIN; tensions T2/T3/T4).

**Labeling discipline (absolute rule):** **[DATA]** = read from a source this session (arXiv/survey, with citation) or internal theorem (backward-only citation). **[CONJECTURE-DENINGER]** = what Deninger CONJECTURES, attributed precisely, distinguished from what he proves. **[ANALOGY]** = dictionary correspondence, not a theorem. **[GAP]** = what is missing, stated precisely. **[OUR-CONJECTURE]** = what we propose. **[COMPUTATION]** = my own derivation. **[UNVERIFIED]**. NEVER "proved" except when genuine. The goal: to determine whether Deninger's conjectural foliated cohomology IS the framework where our intersection form with a flow lives, whether the positivity he expects IS our G2, and the real status (what has been proved of the program, what remains conjectural).

---

## 0. Executive summary

Deninger's program is, today, the candidate closest to "the genuine geometric framework" whose absence Docs 124–126 identified as the cause of circularity. Its form is exactly what Doc 126 §4.4 found lacking: an $\mathbb R$ flow over a foliated space, the primes as closed orbits of length $\log p$, the archimedean place as fixed points, the explicit formula as a Lefschetz trace formula, and **RH as Hodge-type positivity on $H^1_{\mathcal F}$**. The central question — is this the non-circular framework, or is it circular, or obstructed? — admits a finer answer than that of Docs 124–126, because Deninger **proved** the decisive piece in a model case.

**Central findings:**

1. **What Deninger CONJECTURES vs. what he PROVES, carefully separated (§1).** CONJECTURE: the existence of a foliated (laminated) space $X$ with flow $\phi^t$ and a reduced foliated cohomology $\bar H^\bullet_{\mathcal F}$ such that Weil's explicit formula IS the flow's Lefschetz trace formula, and RH is equivalent to a positivity over $\bar H^1_{\mathcal F}$. PROVED: (i) **the formalism** —that IF such a cohomology exists with the standard properties (Poincaré duality, Künneth, Lefschetz, a Hodge theory along the leaves), THEN the functional equation, the explicit formula and the RH-positivity follow— [DATA]; (ii) in the **Kähler–Riemann** case (foliations by complex manifolds with transverse metric), **the polarizable Hodge structure, Hard Lefschetz and Hodge–Riemann positivity over $\bar H^\bullet_{\mathcal F}$ are THEOREMS** (math/0204111) [DATA]; (iii) the simple example (math/0204194) where the explicit formula of an L-trivial object is literally a Lefschetz trace [DATA].

2. **The identification with our intersection form (§2): strong ANALOGY, NOT equality.** Our $\Delta_\mu$ (scaling flow of Doc 125) ↔ Deninger's flow $\phi^t$; our $\Delta_{p^k}$ ↔ the periodic orbits of length $\log p$. BUT: (a) Connes–Consani (CC, the scaling site) and Deninger are **two distinct programs** that **converge only partially** — Morishita (2508.15971, 2025) builds an $\mathbb R_+$-**anti**-equivariant comparison map between the two for abelian number fields, **not an isomorphism** [DATA]; (b) our form lives over the **square** $X\times X$ (surface intersection theory), while Deninger works over $X$ itself (3-dimensional foliated cohomology with flow); they are **two incarnations of the same positivity** (Hodge index vs. foliated Hodge–Riemann polarization), not the same literal object.

3. **The circularity test (§3): the most important finding of the document.** Deninger's conjecture is of the **NON-circular** type in its strong form: RH-positivity is **NOT** an additional hand-imposed hypothesis, but an **expected consequence of the existence of the correct foliated space** (of Kähler–Riemann type), because in that case the positivity is a **theorem of Hodge theory along the leaves** (math/0204111), just as the classical Hodge index is a theorem of surface geometry, not an axiom. **Therefore: building the space (with Kähler–Riemann structure) WOULD GIVE RH without assuming positivity=RH.** The problem is **geometric** (building the space), not logical (it is not circular in itself). This contrasts with CC, where Weil's positivity is spectral and circular (Doc 124). **Test verdict: (a) non-circular framework — conditional on the space being of Kähler–Riemann type.**

4. **The non-existence obstacles (§4) are real and precise.** (i) The foliated space for $\mathrm{Spec}\,\mathbb Z$ **has not been built** and its existence is **unknown** — the only fully realized case is that of **curves/function fields** (where the foliation already exists via the geodesic/suspension flow) [DATA Leichtnam, Deninger]. (ii) There is a **proved spectral rigidity obstruction** (1712.04181): for suspensions/bundles over the circle, the spectrum of the infinitesimal generator is **forced by monodromy** — the set of closed-orbit lengths **is not arbitrary**; one cannot freely prescribe $\{\log p\}$ with the correct multiplicities. (iii) The foliated cohomology is **generically infinite-dimensional and analytic, not topological, in nature** — this agrees with R-FIN/R-SIG ≺ of Doc 119 and with the infinite dimension of Doc 126 §2.4. (iv) **Recent positive result** that recalibrates: Álvarez López–Kordyukov–Leichtnam (2402.06671, 2024) **PROVED** the Lefschetz trace formula for foliated flows on real manifolds with codimension-1 foliation — "solving a conjecture of Deninger" — using **two** reduced cohomologies. The analytic trace machinery already **exists and works**; what is missing is the **arithmetic space** to run it on.

5. **Synthesis with Doc 127 (§5): they ARE the same meta-object seen from two sides.** Forni (Doc 127) and Deninger attack the same wall: both want an **ergodic/hyperbolic $\mathbb R$ flow with a Hodge bundle whose positivity gives the index over the primitive**. Forni: the positivity (non-vanishing of the Lyapunov exponents of the Kontsevich–Zorich cocycle) is proved by **external ergodicity** of the Teichmüller flow. Deninger: the positivity (foliated Hodge–Riemann polarization) is proved by **Hodge theory along the leaves** in the Kähler–Riemann case. **The unified meta-object:** an $\mathbb R$ flow over a (laminated/foliated) space whose Hodge theory along the leaves + ergodicity of the transverse flow force, **externally to $\zeta$**, Hodge–Riemann positivity over $\bar H^1_{\mathcal F}$ — which is our negative definiteness over the primitive (G2).

6. **Verdict (§6): (a) non-circular framework, but NOT built and with a known realization obstruction.** Deninger provides the logically non-circular framework (building the Kähler–Riemann space gives RH without assuming positivity=RH); it is not (b) circular like CC. But it is not free: there is a spectral rigidity obstruction (1712.04181) and the space for $\mathrm{Spec}\,\mathbb Z$ still does not exist. The **first concrete constructible theorem** along this line is NOT RH nor the whole space: it is to **verify whether the scaling-site square (Doc 125) or Morishita's space admits a foliated Kähler–Riemann structure (or a characteristic-1 analogue) — because if it does, the positivity of Doc 125 §5 (signature $(1,2)$ in the toy model) becomes a theorem of Hodge theory along the leaves, not an accident of the finite case, and G-125.B would close by geometry, not by the flow's trace (evading NC3).**

---

## 1. DENINGER'S PROGRAM [DATA + CONJECTURE-DENINGER]

### 1.1. The conjectural structure — the master dictionary

**[CONJECTURE-DENINGER]** (Deninger, ICM Berlin 1998, *Some analogies between number theory and dynamical systems on foliated spaces*, Doc. Math. Extra Vol. ICM I, 163–186; survey *Analogies between analysis on foliated spaces and arithmetic geometry*, arXiv:0709.2801; *Arithmetic geometry and analysis on foliated spaces*, Arizona Winter School / DLSDeninger.pdf.) Deninger conjectures, for an arithmetic scheme $\mathcal X$ (in particular $\overline{\mathrm{Spec}\,\mathbb Z}$, the Arakelov compactification of $\mathrm{Spec}\,\mathbb Z$), the existence of a geometric-dynamical object:

> **(D1) A foliated (laminated) space $X$ of real dimension $3$** —a codimension-$1$ foliated "leaf"— equipped with **a flow $\phi^t$ ($t\in\mathbb R$)** that preserves the foliation and acts transversally to the leaves. The flow $\phi^t$ is the **analogue of Frobenius** for $\mathrm{Spec}\,\mathbb Z$: where in function fields $\mathbb F_q$ the Frobenius $\mathrm{Frob}_q$ acts (a **discrete** $\mathbb Z$ generator of $\widehat{\mathbb Z}=\mathrm{Gal}(\overline{\mathbb F_q}/\mathbb F_q)$), here a **continuous** $\mathbb R$ flow acts. [CONJECTURE-DENINGER]

> **(D2) The orbit dictionary.** Each prime $p$ (each finite place) corresponds to a **closed (periodic) orbit of the flow of length $\log p$** (more generally $\log N(\mathfrak p)$ for a number field). The **archimedean places** (the infinite places) correspond to the **fixed points of the flow** $\phi^t$. [CONJECTURE-DENINGER + ANALOGY] This is the dictionary that reappears literally in our Doc 125 §3.3 (R-LEF-PRIMES: each prime contributes the orbit of period $\log p$) and in Doc 119 §3.4 (R-LEF-FLOW).

> **(D3) A reduced foliated cohomology** $\bar H^i_{\mathcal F}(X)$ ($i=0,1,2$), of **analytic, not topological, nature**, **generically infinite-dimensional**, with an induced action of the flow $\phi^t$ and of its **infinitesimal generator** $\Theta$ (the Lie derivative along the flow's vector field). The dictionary:
> - $\bar H^0_{\mathcal F}$: the "point" (constants); the pole of $\zeta$ at $s=1$.
> - $\bar H^1_{\mathcal F}$: **carries the zeros** of $\zeta$ — the eigenvalues of $\Theta$ on $\bar H^1_{\mathcal F}\otimes\mathbb C$ must coincide with the **nontrivial zeros** $\rho$ of $\zeta$. [CONJECTURE-DENINGER]
> - $\bar H^2_{\mathcal F}$: the "top degree"/the other pole.

**[DATA — precise attribution]** That the foliated cohomology is infinite-dimensional and "not topological but highly analytic" is NOT a conjecture: it is a **fact** for the real foliations where it has been computed (see §4.2, 1712.04181). What is conjectural is that **such a foliation exists whose cohomology reproduces the zeros of $\zeta$**.

### 1.2. The explicit formula as a Lefschetz trace formula [CONJECTURE-DENINGER, with a PROVED partial realization]

**[CONJECTURE-DENINGER]** The heart of the program: **Weil's explicit formula** (which relates the sum over zeros $\sum_\rho \hat h(\rho)$ to the sum over primes $\sum_p \sum_k \frac{\log p}{p^{k/2}}h(k\log p)$ plus archimedean terms) must be **a dynamical Lefschetz trace formula** for the flow $\phi^t$:
$$
\sum_{i=0}^{2}(-1)^i \mathrm{Tr}\,\big(\phi^{t*}\mid \bar H^i_{\mathcal F}\big) \;=\; \underbrace{\sum_{\gamma}\;\ell(\gamma)\!\!\sum_{k\ge1}\delta_{k\ell(\gamma)}}_{\text{closed orbits}=\text{primes}} \;+\;\underbrace{(\text{fixed-point contribution})}_{\text{archimedean places}}.
$$
The left-hand side (trace over cohomology) = the **zeros** side; the right-hand side (closed orbits + fixed points) = the **primes + archimedean** side. **That is exactly the structure of the explicit formula.** [CONJECTURE-DENINGER + ANALOGY]

**[DATA — what IS actually PROVED of this].** Three levels of realization:

- **(P-a) The formalism (Deninger, proved).** Deninger **proved** that IF a cohomology exists with the standard properties (Poincaré duality, Künneth, a fundamental class, a flow action with discrete-spectrum generator), THEN the following follow formally: the functional equation, the Hadamard-type factorization of $\zeta$, and the explicit formula as a Lefschetz trace. [DATA: this is the "infinite dimensional cohomological formalism" — the content of Deninger's papers from the 90s.] It is a **conditional** theorem (formalism), not an unconditional one.

- **(P-b) The simple example (math/0204194, *On the nature of the explicit formulas — a simple example*).** Deninger exhibits an **explicit and complete** dynamical model where the explicit formula of an $L$-trivial object **is literally** a Lefschetz trace formula of a flow over a concrete foliated space. [DATA] Here there is no Riemann $\zeta$; it is the "Hello World" that shows the mechanism is NOT empty.

- **(P-c) The trace formula for foliated flows (Álvarez López–Kordyukov–Leichtnam, arXiv:2402.06671, 2024 — PROVED).** [DATA, abstract verbatim via WebFetch] On **closed real manifolds with a transversally oriented codimension-1 foliation**, with a foliated flow with simple closed orbits and simple transversally preserved leaves, **they proved a trace formula** describing the Lefschetz distribution $L_{\mathrm{dis}}(\phi)$ "in terms of infinitesimal data of the closed orbits and the preserved leaves." **It solves a conjecture of Deninger**, with the key innovation of using **two** reduced foliated cohomologies instead of one. [DATA] **This is decisive: the analytic machinery of the Lefschetz trace formula for foliated flows already exists and is a theorem** — the bottleneck is NOT the analytic side, but the construction of the arithmetic space.

### 1.3. RH as positivity over $\bar H^1_{\mathcal F}$ [CONJECTURE-DENINGER + THEOREM in the Kähler–Riemann case]

**[CONJECTURE-DENINGER]** The way RH appears: the zeros $\rho$ are the eigenvalues of $\frac{1}{2\pi}\Theta$ (the infinitesimal generator of the flow) on $\bar H^1_{\mathcal F}$. RH $\iff$ **all those eigenvalues have real part $=\tfrac12$**, equivalently, after normalizing, **the infinitesimal generator is essentially anti-self-adjoint** (zero real part) with respect to a natural inner product on $\bar H^1_{\mathcal F}$. Deninger conjectures that this follows from **a Hodge-type positivity property** on $\bar H^1_{\mathcal F}$ — the **analogue of the Hodge index theorem/of Hodge–Riemann polarization**. [CONJECTURE-DENINGER]

> **[DATA — the program's sentence, via survey, verified this session]:** "The Riemann hypothesis would be a consequence of properties parallel to the positivity of the intersection pairing in Hodge theory."

**[DATA — the theorem that changes the verdict: math/0204111, *Real polarizable Hodge structures arising from foliations*].** Deninger **PROVED** (not conjectured) that for **Kähler–Riemann foliations** —foliations whose leaves are Kähler manifolds with a transverse Riemannian metric— the reduced foliated cohomology $\bar H^\bullet_{\mathcal F}$ carries:
- a **real polarizable Hodge structure** [DATA];
- a **Hard Lefschetz theorem**: $L^{g-r}:\bar H^r_{\mathcal F}\xrightarrow{\sim}\bar H^{2g-r}_{\mathcal F}$ is an isomorphism [DATA, via ar5iv];
- **Hodge–Riemann positivity**: the form $Q(\xi,J\bar\xi)>0$ for $\xi\ne0$ over the primitive [DATA];
- the **Serre analogue of the Weil conjectures** carries over [DATA].

This rests on the **smooth Hodge decomposition theorem of Álvarez López–Kordyukov** for Riemannian foliations (the reduced foliated cohomology = smooth global forms harmonic along the leaves) [DATA]. **The positivity, in the Kähler–Riemann case, is a THEOREM derived from the Hodge geometry along the leaves — exactly as the classical Hodge index is a theorem of surface geometry.** Keep this in mind: it is the hinge of §3.

---

## 2. THE IDENTIFICATION [ANALOGY + COMPUTATION]

### 2.1. Our flow $\Delta_\mu$ ↔ Deninger's flow $\phi^t$?

**[ANALOGY, strong].** Doc 125 §2.4 defines the correspondences $F_\mu:C_p\to C_p$, $u\mapsto u+\log\mu$, whose graph $\Delta_\mu=\{v=u+\log\mu\}$ is a translation of the diagonal — **the scaling flow**. This is **literally** Deninger's flow $\phi^t$ restricted to the block $C_p$: $\phi^t$ translates by $t$ along the transverse direction, and $\Delta_\mu$ with $\log\mu=t$ is its graph in the square. **Deninger's infinitesimal generator $\Theta$ = the generator of the flow $\Delta_\mu$ near $\mu=1$** (Doc 125 §3.4: "the infinitesimal generator of the flow, $\mu$ infinitesimally close to 1"). [ANALOGY with generator identification]

**[COMPUTATION] The $\mathbb Z$ vs. $\mathbb R$ difference is the same in both.** Deninger replaces the discrete Frobenius ($\mathbb Z$) of function fields with a continuous flow ($\mathbb R$); Doc 125 §2.4 / Doc 119 T4 report exactly this difference ("here the flow is continuous: $\mu\in\mathbb R_+^*$, not $\mathbb Z$"). **It is the same phenomenon, named twice.** The integral sub-lattice $\mathcal L_{\mathbb Z}$ of Doc 125 (the $\Delta_{p^k}$) = Deninger's closed orbits of length $k\log p$; the continuous flow outside $\mathcal L_{\mathbb Z}$ = Deninger's generic flow $\phi^t$ carrying the zeros.

### 2.2. Our $\Delta_{p^k}$ ↔ the periodic orbits of length $\log p$?

**[ANALOGY, exact].** Doc 125 §3.3: for $\mu=p^k$ ($\log\mu=k\log p\equiv0\bmod\log p$ on the torus of period $\log p$), the graphs $\Delta$ and $\Delta_{p^k}$ **coincide** along the whole circle — non-transverse intersection = **periodic orbit of length $k\log p$**. This is **identical** to (D2): the prime $p$ = closed orbit of length $\log p$, and its iterates $k\log p$. The flow-trace contribution at $\mu=p^k$ (Doc 125 §3.3, via Connes Selecta 1999) = the term $\frac{\log p}{p^{k/2}}$ of the explicit formula = the closed-orbit term of Deninger's Lefschetz formula. **The three coincide.** [ANALOGY + DATA]

### 2.3. Is CC's scaling site THE realization of Deninger's foliated space? — NO, they are two distinct programs that converge partially

**[DATA — the key point].** Connes–Consani (scaling site/arithmetic site) and Deninger (foliated spaces) are **two related but distinct programs**. The precise relation was established by **Morishita (arXiv:2508.15971, 2025, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*)** [DATA, via WebFetch HTML]:

- For **abelian number fields** $F/\mathbb Q$, Morishita builds a **continuous map** $\Psi_F:\mathfrak X_F\to\mathcal X_F$ between Deninger's foliated dynamical system $\mathfrak X_F$ and CC's adelic space $\mathcal X_F$, which is **$\mathbb R_+$-anti-equivariant and Galois-equivariant** (Theorem 3.6). [DATA]
- **It is NOT an isomorphism.** It is a comparison map that **reverses the direction of the flow** (anti-equivariant). [DATA]
- Under the map, **the closed orbits tied to the primes correspond** in both spaces: the bundles $\Gamma_p$ (Deninger) $\cong C_p$ (CC) as circles of length $\log N(\mathfrak p)$. [DATA]
- **CRUCIAL:** Morishita does **NOT** develop the foliated cohomology nor verify the positivity; he builds **only the underlying space and the flow**. The cohomological part and the positivity **remain open** (Remark 2.1.13). [DATA]

**[COMPUTATION] Consequence for our program.** CC's scaling site (over which Doc 125 builds the intersection form) is a **partial realization of the underlying space** of Deninger (space + flow + orbits = primes), **but NOT of the cohomological structure/positivity** where RH lives. That is: CC gives the **stage** (space with flow and correct orbits), Deninger additionally requires the **Hodge function** on $\bar H^1_{\mathcal F}$. **They converge on the stage; they diverge exactly where RH's content begins.** This explains why Doc 124 found that CC's positivity is *spectral* (on the operator/trace side) and not *intersection-theoretic* (on the Hodge side): CC realized the flow and the orbits, not the foliated Hodge theory.

### 2.4. Is Deninger's positivity OUR negative definiteness over the primitive? [ANALOGY + mapping]

**[COMPUTATION — the term-by-term mapping].**

| Doc 125/126 (square $X\times X$) | Deninger (foliated space $X$) |
|---|---|
| Intersection form $D\cdot D'$ over $\mathrm{NS}(X\times X)\otimes\mathbb R$ | Polarization form $Q$ over $\bar H^1_{\mathcal F}$ |
| Ample class $\ell=f_1+f_2$, $\ell^2>0$ | Lefschetz class $L$ (foliated Hard Lefschetz) |
| Primitive $P^1=\ell^\perp$ | Primitive $\ker(L^{\dots})\subset\bar H^1_{\mathcal F}$ |
| **Negative definiteness** over $P^1$ (signature $(1,\rho-1)$) — G2, Doc 124/126 | **Hodge–Riemann positivity** $Q(\xi,J\bar\xi)>0$ over the primitive — math/0204111 |
| Castelnuovo–Severi $\Rightarrow$ weight-1 purity $\Rightarrow$ RH | Hard Lefschetz + polarization $\Rightarrow$ eigenvalues of $\Theta$ with $\Re=\tfrac12$ $\Rightarrow$ RH |

**[COMPUTATION] They are the SAME positivity, in two dual incarnations.** In classical surface geometry, the Hodge index over $C\times C$ (signature $(1,\rho-1)$, negativity over the primitive) **is equivalent** to Hodge–Riemann polarization over $H^1(C)$ (the Riemann form is positive-definite over the primitive of $H^1$). It is the standard duality: positivity over $H^1$ of the factor ⟺ the Hodge index over the square. **Hence the "negative definiteness over the primitive" of Doc 124/125 (G2) IS the Hodge–Riemann polarization that Deninger expects over $\bar H^1_{\mathcal F}$**, transported from the square to the factor via the standard Hodge-index ⟺ polarization correspondence. [ANALOGY with computational content; the equivalence is a theorem in the classical case, conjectural when transported to the foliated/tropical case]

**[GAP] The nontrivial link:** that the equivalence "Hodge index over the square ⟺ polarization over the factor's $\bar H^1$" **survives** the passage (i) from classical geometry to foliated geometry (Deninger), and (ii) to characteristic 1/tropical (CC, Doc 125). In the classical case it is Künneth + duality; in the foliated case Deninger has it in the Kähler–Riemann case; in the tropical case Doc 123 reported that **tropical Künneth does not exist** — this is the point of friction.

---

## 3. THE CIRCULARITY TEST [decisive]

The central question: is the positivity Deninger expects conjectured as a **consequence of the existence** of the foliated cohomology (non-circular: once the correct space exists, the positivity is automatic by the geometry), or as an **additional hypothesis equivalent to RH** (circular)?

### 3.1. The answer: NON-circular in its strong form

**[COMPUTATION — the decisive analysis].** The test is decided by **math/0204111**. The logical structure of Deninger's program is:

$$
\boxed{\;\exists\text{ foliated space }X\text{ of Kähler–Riemann type with flow }\phi^t,\ \bar H^1_{\mathcal F}=\{\text{zeros}\}\;}\;\xLongrightarrow{\text{THEOREM, math/0204111}}\;\boxed{\;\text{Hodge–Riemann positivity over }\bar H^1_{\mathcal F}\;}\;\Longrightarrow\;\text{RH}.
$$

The first implication is a **THEOREM of Deninger**: if the foliation is of Kähler–Riemann type, the polarization **is not postulated, it is derived** from Hodge theory along the leaves (Álvarez López–Kordyukov decomposition). **The positivity is NOT an additional hand-imposed axiom: it is a geometric consequence of the existence of the space with the correct structure.**

**[COMPUTATION] Comparison with the Castelnuovo model (Doc 125 §1.4).** This is **exactly** the non-circular pattern of function fields: there, $C\times C$ is a genuine projective surface, and the Hodge index is a **geometry theorem** (Sylvester + Poincaré duality on $H^2$) that holds for **every** class, **regardless of what $C$ is and where its points lie** (Doc 125 §1.4: "the positivity is geometric, independent of the eigenvalues"). Deninger's positivity in the Kähler–Riemann case has **the same nature**: it holds by the Hodge geometry of the leaves, not by where the zeros are. **It passes NC1 (externality), NC2 (overgeneration: it holds for the whole primitive, not just ζ's classes), NC4 (under $\neg$RH an eigenvalue with $\Re\ne\tfrac12$ would violate the polarization, visible from the geometry).** [COMPUTATION]

### 3.2. Why it is NOT CC's circular case (b)

**[COMPUTATION] The exact contrast with Doc 124.** Doc 124 established that Connes–Consani's positivity is **spectral** (Weil's positivity = MW-1 = Weil's criterion = RH) and therefore **circular** (FAILS NC3). The difference with Deninger:

- **CC (circular):** the positivity is read **on the flow's trace/the operator** — it is Weil's positivity of the explicit formula, which IS RH. There is no geometric Hodge theory generating it externally; it is verified by evaluating on test functions, which amounts to localizing the zeros. (Doc 125 §6.3: via (c) flow trace = Lefschetz formula = FAILS NC3.)
- **Deninger (non-circular):** the positivity is read **on the foliated cohomology via Hodge theory along the leaves** — it is the Hodge–Riemann polarization, which in the Kähler–Riemann case is a **geometric theorem**, not the trace. **It passes NC3** because it does not reduce to the flow's trace: it is derived from the Hodge structure of the leaves (a geometric object, not a spectral-arithmetic one).

**[COMPUTATION] The hinge:** the difference between the two programs is **exactly the NC3 difference** of Doc 119/125. CC realized the spectral side (the flow's trace = the explicit formula) and that is why its positivity is circular. Deninger asks for the Hodge side (the polarization over the cohomology), which is where the positivity can be genuinely geometric. **Doc 124 diagnosed "CC's positivity is spectral, not intersection-theoretic" — Deninger's program is precisely the one that provides the "intersection-theoretic" one.**

### 3.3. The price: non-circularity is CONDITIONAL on "Kähler–Riemann"

**[COMPUTATION — the honest part].** Non-circularity is **NOT free**. Theorem math/0204111 requires the foliation to be **Kähler–Riemann** (Kähler leaves, Riemannian transverse metric). The implication "existence of the space $\Rightarrow$ positivity" is non-circular **only if the space is of that type**. Hence the problem shifts to:

> **CORE-128.** Is the foliated space of $\mathrm{Spec}\,\mathbb Z$ (if it exists) of **Kähler–Riemann** type (or does it admit an analogous foliated polarizable Hodge structure)? If YES $\Rightarrow$ the positivity is a theorem $\Rightarrow$ RH, non-circular. If unknown $\Rightarrow$ the positivity remains a hypothesis of indeterminate status.

This is **structurally identical** to CORE-G2 of Doc 126 §4.3 ("proving that the square is of the matroidal/Lefschetz subtype, external to $\zeta$"): in both, the problem is NOT to assume the positivity (that would be circular), but to **prove that the space is of the geometric subtype where the positivity is automatic**. Doc 126 called it "tropical matroidal/Lefschetz"; Deninger calls it "Kähler–Riemann." **They are the same meta-statement in two dialects.** [COMPUTATION]

**[COMPUTATION] A difference favorable to Deninger over AHK/tropical (Doc 126).** Doc 126 §2.4 showed that AHK **does not apply** because it is a **finite** method (induction over a finite lattice of flats) and the site is infinite-dimensional. **Deninger does NOT have that problem:** his foliated Hodge theory (math/0204111) is **intrinsically infinite-dimensional and analytic** — the Álvarez López–Kordyukov decomposition is for **infinite-dimensional** reduced foliated cohomology. **Deninger already works in the infinite regime that kills AHK.** This is a real advantage: the central obstacle of Doc 126 (R-SIG ≺ R-FIN, infiniteness breaks AHK) **does not obstruct Deninger**, because his Hodge machinery is analytic-infinite from the outset. The trace formula of 2402.06671 is also for infinite foliated cohomology. [COMPUTATION — important recalibration with respect to Doc 126]

---

## 4. THE REAL STATUS AND THE KNOWN OBSTACLES [DATA]

### 4.1. What does NOT exist: the space for $\mathrm{Spec}\,\mathbb Z$

**[DATA]** The foliated space for $\mathrm{Spec}\,\mathbb Z$ (or any arithmetic scheme over $\mathbb Z$) **has not been built**, and its existence is **unknown**. Citations verified this session:
- "for algebraic schemes over $\mathrm{Spec}\,\mathbb Z$ ... no cohomology theory has yet been developed ... the conjectured cohomology has not been constructed" [DATA].
- "The existence of such a foliated space and flow is still unknown except when the base curve is an elliptic curve" [DATA]. (That is: the only fully realized case is geometric — curves/function fields/elliptic curves — where the foliation already exists via a suspension of the geodesic flow or an analogue.)
- Leichtnam (arXiv:1307.3851): proposes **axioms** for the foliated space of number fields and **formally** derives an Atiyah–Bott–Lefschetz formula that would imply Artin's conjecture; but the space "whose existence is still unknown" [DATA verbatim].

**[COMPUTATION] Status:** Deninger's program is **a PROGRAM, mostly open**. What is proved is: the formalism (conditional), the Kähler–Riemann case (theorem, but that case is NOT $\mathrm{Spec}\,\mathbb Z$), the simple example (toy), and the analytic trace formula (2402.06671, over given real manifolds, not arithmetic ones). What is open: **the construction of the arithmetic space** with orbits $\{\log p\}$ and cohomology $=$ zeros.

### 4.2. The spectral rigidity obstruction — a non-arbitrariness result [DATA]

**[DATA — the concrete obstacle, arXiv:1712.04181, *On the leafwise cohomology and dynamical zeta functions for fiber bundles over the circle*].** For suspensions/bundles over $S^1$ (the simplest class of foliated spaces with flow), it is **PROVED** (Theorem 3.2, via WebFetch):
$$
\mathrm{Sp}\,\big(\Theta\mid \bar H^i_{\mathcal F}(M,\mathbb C)\big)=\Big\{\tfrac{\log\alpha+2\pi i\nu}{\log r}\ \big|\ \alpha\in\mathrm{Sp}(\phi^*\mid H^i(S,\mathbb C)),\ \nu\in\mathbb Z\Big\}.
$$
**The spectrum of the infinitesimal generator is completely determined by the monodromy** $\phi^*$ on the cohomology of the fiber $S$. Consequence [DATA]: **"the spectrum of closed-orbit lengths CANNOT be arbitrary"** — one cannot build a foliated flow with a freely prescribed set of orbit lengths; they are **forced by the geometry of the fiber and the monodromy**.

**[COMPUTATION] Why this is a real obstacle for $\mathrm{Spec}\,\mathbb Z$.** The program asks for closed orbits of lengths **exactly** $\{\log p:p\text{ prime}\}$ with correct multiplicities. The result 1712.04181 says that in the most tractable class (suspensions) **the set of lengths is rigid** — determined by the eigenvalues of the monodromy, which are typically algebraic/roots of unity, **NOT** a set like $\{\log 2,\log 3,\log 5,\dots\}$ with its arithmetic densities. **This does NOT prove non-existence**, but it shows that the "easy" constructions (suspensions) **cannot** give the arithmetic spectrum: the space for $\mathrm{Spec}\,\mathbb Z$, if it exists, **is not a suspension** — it must be a genuinely more complex laminated object (a "solenoid"/non-fibered laminated space), and there the foliated Hodge theory is much less understood. [COMPUTATION on DATA]

**[ANALOGY with Doc 126/119]** This spectral rigidity is **the same tension** as T2 of Doc 119 (signatures not continuous under limits) and the infiniteness of Doc 126 §2.4, seen from the dynamical side: the desired spectrum $\{\log p\}$ is "dense and arithmetic," incompatible with the rigid spectra of tractable foliations.

### 4.3. The infinite-dimensional cohomology [DATA] — obstacle and advantage

**[DATA]** The foliated cohomology is generically **infinite-dimensional** and "not topological but highly analytic" — Theorem 2.1 of 1712.04181: $\bar H^i_{\mathcal F}(M)\cong C^\infty_\phi(\mathbb R,H^i(S))$, infinite-dimensional spaces [DATA].

**[COMPUTATION] Double edge:** (i) **obstacle:** Poincaré duality, the trace, the signature over an infinite-dimensional space are delicate (they need reduction/regularization — the innovation of 2402.06671, using TWO reduced cohomologies, is precisely so that the traces converge). It agrees with R-SIG ≺ R-FIN (Doc 119). (ii) **ADVANTAGE (already noted §3.3):** unlike AHK (finite, Doc 126), Deninger **already operates in infinite dimension** — his foliated Hodge theory and his trace formula are built for that regime. The obstacle of Doc 126 (infiniteness kills AHK) **does not apply to Deninger's method**.

### 4.4. Status summary: what has been proved, what remains conjectural

**[DATA — status table, frank]:**

| Piece | Status |
|---|---|
| Cohomological formalism (cohomology $\Rightarrow$ functional eq., explicit formula) | **PROVED conditional** (Deninger 90s) |
| Explicit formula = Lefschetz trace, complete simple example | **PROVED** (math/0204194) |
| Polarizable Hodge structure + Hard Lefschetz + positivity, Kähler–Riemann case | **PROVED** (math/0204111) |
| Trace formula for foliated flows, real manifolds | **PROVED 2024** (Álvarez López–Kordyukov–Leichtnam, 2402.06671) |
| Deninger ↔ Connes–Consani relation (abelian fields, space+flow only) | **PROVED 2025** (Morishita, 2508.15971), anti-equivariant map, NOT iso |
| Foliated space for curves/elliptic curve | **realized** (geometric case) |
| **Foliated space for $\mathrm{Spec}\,\mathbb Z$ with orbits $\{\log p\}$ and cohomology $=$ zeros** | **OPEN/existence unknown** |
| That this space be Kähler–Riemann (⟹ positivity ⟹ RH) | **CONJECTURE-DENINGER, not proved** |
| Obstruction: rigid orbit spectrum in suspensions | **PROVED** (1712.04181) ⟹ the space is not a simple suspension |

---

## 5. SYNTHESIS WITH DOC 127 (dynamical Hodge theory/Forni)

**[COMPUTATION — the sought-after unification].** Doc 127 attacks the same wall from Teichmüller/Forni; Doc 128 (this one) from foliations/Deninger. **They are the same meta-object seen from two sides.** The mapping:

| | Doc 127 (Forni/Teichmüller) | Doc 128 (Deninger/foliations) |
|---|---|---|
| The $\mathbb R$ flow | Teichmüller flow/Weil–Petersson geodesic flow | flow $\phi^t$ over the laminated space |
| The Hodge bundle | the Hodge bundle over moduli space, Kontsevich–Zorich cocycle | the foliated cohomology $\bar H^1_{\mathcal F}$ with its Hodge structure along the leaves |
| The positivity | **non-vanishing/sign of the Lyapunov exponents** of the cocycle (Forni: proved by ergodicity of the Teichmüller flow) | **Hodge–Riemann polarization** over $\bar H^1_{\mathcal F}$ (Deninger: proved in the Kähler–Riemann case) |
| How positivity is proved | **external ergodicity** of the flow (Forni, Avila–Viana): dynamical theorem, assumes nothing about $\zeta$ | **Hodge theory along the leaves** (Álvarez López–Kordyukov): geometric theorem, assumes nothing about $\zeta$ |
| Non-circularity test | Lyapunov positivity is **external** to $\zeta$ (property of the flow) | the polarization is **external** to $\zeta$ (Hodge property of the leaves) |

**[OUR-CONJECTURE — the UNIFIED META-OBJECT].**

> **META-OBJECT (Phase 42).** *An ergodic/partially hyperbolic $\mathbb R$ flow $\phi^t$ over a laminated space $X$ (the analogue of $\mathrm{Spec}\,\mathbb Z$ with a flow), carrying a **Hodge bundle** $\bar H^1_{\mathcal F}$ along the leaves, such that **Hodge–Riemann positivity over the primitive** follows, **externally to $\zeta$**, from the combination of:*
> *(i) **Hodge theory along the leaves** (Kähler–Riemann-type structure ⟹ polarization, via Álvarez López–Kordyukov) — Deninger's side;*
> *(ii) **ergodicity/hyperbolicity of the transverse flow** (non-vanishing of the Lyapunov exponents of the Hodge cocycle, via Forni/Avila–Viana) — Forni's side;*
> *so that the positivity is NOT read on the flow's trace (which would be the explicit formula = circular, NC3), but on the **Hodge monodromy of the bundle** (geometric, NC3-passes). This positivity IS our negative definiteness over the primitive (G2 = Hodge index over the square, via the Hodge-index ⟺ polarization duality of §2.4).*

**[COMPUTATION] Its non-circularity test.** The meta-object passes R-NC **if and only if** the positivity is established by (i)+(ii) — Hodge of the leaves + ergodicity of the flow — **without evaluating the trace on $\zeta$'s test functions**. Both sides (Forni and Deninger) have this property **in their proved cases** (Teichmüller: Lyapunov positivity is an ergodic theorem; Kähler–Riemann: the polarization is a Hodge theorem). **The unified gap is the same:** that the space for $\mathrm{Spec}\,\mathbb Z$ (a) exist, and (b) be of the type where (i)+(ii) apply (Kähler–Riemann + ergodic). **CORE-128 = Doc 127's gap, merged.**

**[OUR-CONJECTURE] Phase 42's bet:** that **the scaling-site square of Doc 125 is a tropical/characteristic-1 shadow of this meta-object**, and that the signature $(1,2)$ of the finite toy model (Doc 125 §5, the strongest positive result of the program so far) is **the imprint of the foliated Hodge–Riemann polarization** — that is, that G-125.B (the signature's persistence) closes **not** by tropical geometry (which Babaee–Huh obstructs, Doc 126), but by **dynamical Hodge theory** (Forni + Deninger), which is the correct infinite-dimensional regime.

---

## 6. VERDICT

### 6.1. Classification (a)/(b)/(c)/(d)

**[COMPUTATION] Verdict: (a) non-circular framework — but NOT built, and with a known realization obstruction.** Breakdown:

- **Does it provide the non-circular framework?** **YES, in its logical form.** Unlike CC (circular, spectral positivity = Weil = RH, FAILS NC3, Doc 124), Deninger's program establishes RH-positivity as a **consequence of the existence of the space** (of Kähler–Riemann type), via a **theorem** (math/0204111: the foliated Hodge–Riemann polarization is geometric, not postulated). **Building the correct space would give RH WITHOUT assuming positivity=RH.** It passes NC1, NC2, NC3, NC4 in the Kähler–Riemann case. **It is (a), not (b).**

- **Is it circular?** **NO**, in explicit contrast with CC. Deninger's positivity is Hodge-theoretic (geometric), not spectral (trace-based). This is the finding that distinguishes Doc 128 from Docs 124–126: **there was a framework where the positivity is NOT circular, and it is Deninger's.**

- **Is it obstructed?** **PARTIALLY.** There is no proved non-existence, but there is (i) the space for $\mathrm{Spec}\,\mathbb Z$ does not exist/existence unknown, and (ii) **a proved spectral rigidity obstruction** (1712.04181): simple constructions (suspensions) CANNOT give the length spectrum $\{\log p\}$ — the space must be a genuinely complex lamination (solenoid), where foliated Hodge theory is much less developed. It is not (c) "obstructed by non-existence," but the realization is genuinely difficult.

- **Is it undeterminable?** **NOT entirely (d):** the logical status IS determinable and favorable (non-circular); only the **geometric realization** (does the Kähler–Riemann space for $\mathrm{Spec}\,\mathbb Z$ exist?) is undetermined.

**Composite verdict: (a) with open realization and a known rigidity obstruction** — structurally **better** than the (b)/(d) verdict of Docs 124–126 for CC/AHK, because Deninger's framework evades circularity (geometric Hodge positivity, not spectral) AND evades the infiniteness that kills AHK (it operates in infinite dimension from the outset).

### 6.2. Is there a first concrete, constructible theorem along this line?

**[OUR-CONJECTURE — the actionable deliverable].** YES, and it is NOT RH nor the whole space. It is:

> **FIRST-THEOREM-128 (constructible).** *Verify whether the scaling-site square (Doc 125) — or, better, Morishita's space $\mathfrak X_F$ (2508.15971), which already identifies the flow and the orbits — admits a **foliated polarizable Hodge structure** (of Kähler–Riemann type, or a characteristic-1 analogue via the Álvarez López–Kordyukov decomposition adapted to tropical leaves). If it does, then the signature $(1,2)$ of the finite toy model of Doc 125 §5 is raised to a **Hodge–Riemann polarization theorem over $\bar H^1_{\mathcal F}$**, and G-125.B closes by HODGE GEOMETRY (not by the flow's trace) — evading NC3.*

**[COMPUTATION] Why it is constructible and why it matters:** (i) the space (Morishita) and the flow already exist as objects; (ii) the foliated Hodge machinery (Álvarez López–Kordyukov) and the trace machinery (2402.06671) are already theorems in the real case; (iii) what is missing is **a bridge**: either endowing Morishita's space with a Kähler–Riemann structure (or proving it does NOT admit one — which would also be a decisive result, pushing toward (c)), or adapting the foliated Hodge decomposition to the characteristic-1 laminated/tropical case. **This is a bounded problem, with all ingredients identified** — exactly the kind of "new mathematics to cross the wall" that Phase 42 seeks.

**[COMPUTATION] The decisive difference with Phase 41:** Phase 41 (Docs 124–126) sought positivity **on the tropical/intersection side** (the scaling-site square, the tropical Kähler package) and collided with Babaee–Huh (the tropical Hodge index is NOT automatic) + the infiniteness that kills AHK. **Phase 42/Deninger relocates the positivity to the dynamical-foliated Hodge side**, where (a) the positivity is genuinely geometric (math/0204111), (b) infinite dimension is the native regime (not an obstacle), (c) Babaee–Huh does not apply (it is not tropical intersection geometry but analytic Hodge theory of leaves). **Phase 41's wall is tropical; Deninger offers a way around it through the analytic-foliated side.** That is the meaning of Phase 42's turn.

---

## 7. Synthesis and honesty

No new theorem was proved here. What was **read from source** was: Deninger ICM 1998 + survey 0709.2801 + DLSDeninger; math/0204111 foliated polarizable Hodge structures; math/0204194 simple example; Leichtnam 1307.3851; Álvarez López–Kordyukov–Leichtnam 2402.06671 trace formula 2024; 1712.04181 spectral rigidity; Morishita 2508.15971 relation to CC — and **the identification with our program was computed**.

**The central point:** Deninger's program is the first framework found across the whole RH program where **the positivity that gives RH is NOT circular** — it is a geometric consequence of the existence of the correct space (theorem in the Kähler–Riemann case), not Weil's positivity renamed (which is CC's circular fate, Doc 124). The price is that **the space for $\mathrm{Spec}\,\mathbb Z$ does not exist**, there is a **spectral rigidity obstruction** (simple suspensions do not give $\{\log p\}$), and the realization is a genuinely open problem. But the framework **evades the two walls of Phase 41**: circularity (Hodge positivity, not spectral) and infiniteness (Deninger's native regime, not an obstacle). The synthesis with Doc 127 is total: Forni and Deninger are **the same meta-object** —an $\mathbb R$ flow with a Hodge bundle whose positivity is proved externally (ergodicity/Hodge of leaves)— and that meta-object is the new mathematics Phase 42 must build. **The point of obstruction has moved from "the tropical Hodge index" (Phase 41, obstructed by Babaee–Huh) to "the foliated polarizable Hodge structure over Morishita's space" (Phase 42, open but neither circular nor obstructed by infiniteness)** — and that is the first concrete theorem to attack.

---

## References

**Primary source read this session, via WebSearch/WebFetch):**
- C. Deninger, *Some analogies between number theory and dynamical systems on foliated spaces*, Proc. ICM Berlin 1998, Doc. Math. Extra Vol. ICM I, 163–186 — the flow/Frobenius dictionary, primes = closed orbits $\log p$, archimedean = fixed points, explicit formula = Lefschetz trace. **[DATA/CONJECTURE-DENINGER]**
- C. Deninger, *Analogies between analysis on foliated spaces and arithmetic geometry*, arXiv:0709.2801 — survey; "RH would be a consequence of properties parallel to the positivity of the intersection pairing in Hodge theory". **[DATA]**
- C. Deninger, *Arithmetic geometry and analysis on foliated spaces* (Arizona Winter School, DLSDeninger.pdf) — exposition of the program. **[DATA]**
- C. Deninger, *Real polarizable Hodge structures arising from foliations*, arXiv:math/0204111 — **PROVES** a polarizable Hodge structure, Hard Lefschetz, Hodge–Riemann positivity over the reduced foliated cohomology of Kähler–Riemann foliations; Serre analogue of Weil. **The theorem that makes the program non-circular.** **[DATA]**
- C. Deninger, *On the nature of the explicit formulas in analytic number theory — a simple example*, arXiv:math/0204194 — complete dynamical example where the explicit formula IS a Lefschetz trace. **[DATA]**
- E. Leichtnam, *On the analogy between L-functions and Atiyah–Bott–Lefschetz trace formulas for foliated spaces*, arXiv:1307.3851 — axioms for the foliated space of number fields; proves an ABL formula for ramified line bundles over Riemannian foliations; space "existence still unknown". **[DATA]**
- J. A. Álvarez López, Y. A. Kordyukov, E. Leichtnam, *A trace formula for foliated flows*, arXiv:2402.06671 (2024) — **PROVE** the Lefschetz trace formula for foliated flows on closed real manifolds (codim 1), using TWO reduced foliated cohomologies; **solves a conjecture of Deninger**. **[DATA — the analytic machinery exists.]**
- (author of the paper on bundles over the circle), arXiv:1712.04181, *On the leafwise cohomology and dynamical zeta functions for fiber bundles over the circle* — infinite-dimensional foliated cohomology ($\bar H^i_{\mathcal F}\cong C^\infty_\phi(\mathbb R,H^i(S))$); **Theorem 3.2: the spectrum of the generator is forced by the monodromy — the length spectrum is NOT arbitrary (rigidity obstruction).** **[DATA]**
- M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*, arXiv:2508.15971 (2025) — Theorem 3.6: an $\mathbb R_+$-**anti**-equivariant and Galois-equivariant continuous map between Deninger's system and CC's adelic space for abelian fields; **NOT an isomorphism**; orbits/primes correspond; cohomology and positivity **NOT** developed. **[DATA — Deninger and CC are two distinct programs converging only on the space+flow.]**
- M. Flach, B. Morin, *Deninger's conjectures and Weil–Arakelov cohomology* — unconditional partial realization of aspects of the formalism. **[DATA, via abstract]**

**Internal (backward-only):** Doc 119 (R-NC NC1–NC4; master quantifier P43; R-SIG ≺ R-FIN; tensions T2/T3/T4; R-LEF-FLOW); Doc 123 (tropical Künneth does not exist; C-rank); Doc 124 (CC's positivity = spectral = MW-1 = circular; intersection positivity [GOOD] vs. spectral positivity [CIRCULAR]); Doc 125 (intersection form over the square; $G_{\text{toy}}$ signature $(1,2)$; flow $\Delta_\mu$; gaps G-125.A/B; NC3 via the flow's trace); Doc 126 (AHK does not apply because of infiniteness; Babaee–Huh obstructs; the core = "matroidal/Lefschetz subtype external to $\zeta$"); Doc 127 (dynamical Hodge theory/Forni — synthesis in §5); roadmap-rh (the master quantifier, G1–G4).

*End of Doc 128.*
