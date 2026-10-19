# Doc 127 — Dynamical Hodge theory as a framework for the foliated Kähler package: the Forni / Eskin–Kontsevich–Zorich precedent and the circularity test

**Program:** Riemann Hypothesis — Phase 42: new mathematics to cross the wall (Hodge positivity over the square with a continuous flow).
**Prerequisites:** Doc 126 (AHK does not apply because of the continuous flow + infiniteness; Babaee–Huh generically obstructs; the core = the tropical-FOLIATED Kähler package; verdict (d) biased toward (b)/(c); the difference "algebraic = free index" vs "tropical = index to be proved"); Doc 125 (the Allermann–Rau intersection form over $C_p\times C_p$; the toy model with $G_{\text{toy}}=\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}$, signature $(1,2)$, negative-definite primitive; G-125.A real/integer; G-125.B signature persistence à la Babaee–Huh; route (c) flow-trace = Lefschetz formula = circular FAILS NC3); Doc 119 (R-SIG/R-FIN/R-LEF/R-WEIGHT; R-LEF-FLOW; test R-NC NC1–NC4; tensions T2 "signatures are not continuous under limits", T3 "the more explicit the trace, the higher the risk that the geometry IS the explicit formula"); P43 (master quantifier: value/inertia — the VALUE of a quadratic functional is computed from the primes alone, but its INERTIA / the partition of the negative index into blocks is not determined without the positions of the zeros; the mean→uniform barrier).

**PARALLEL WORK / GOAL OF THE DOC:** this document does NOT attempt to prove Hodge positivity over the square. It establishes WHETHER **dynamical Hodge theory** (the Kontsevich–Zorich cocycle over the Teichmüller flow; Forni's theorem; Eskin–Kontsevich–Zorich) is the **correct framework** for the missing foliated Kähler package (G-125.B), WHICH theorem of it is the analogue of "the signature persists," and — critically — whether that positivity would be **NON-CIRCULAR** (external to ζ, like Forni) or **collapses to RH** (because the flow of the scaling site carries ζ inside it). If it collapses, that is the result.

**Labeling discipline (absolute rule, maximum risk of a false victory):** **[DATA]** = read from a source this session (with citation) or an internal theorem proved (backward-only citation). **[ANALOGY]** = a structural correspondence I propose, with an explicit degree of fit: **tight** (same mathematical structure) / **partial** (analogous with named differences) / **speculative** (forced). **[COMPUTATION]** = my own derivation. **[GAP]**, **[CONJECTURE]**, **[UNVERIFIED]** = as indicated. **NEVER "proved"** except when genuine.

---

## 0. Executive summary

The dynamical Hodge theory precedent is the only body of work where a **positivity/signature gap of a Hodge bundle with an indefinite form** was proved by an **external, variational-ergodic** method (Forni 2002; Kontsevich–Forni; EKZ 2014) — assuming nothing about the object one wants to bound. It is exactly the architecture that Doc 126 §5.3 asked for as "what would be missing" to move G2 from (b)/(d) toward (a): a positivity that **overgenerates** and comes from outside. That is why it is the most serious candidate for a framework for the foliated Kähler package.

**Central findings:**

1. **The precedent is real and the structure is surprisingly close (§1, §2).** The Hodge bundle $H^1$ over moduli space carries an **indefinite symplectic intersection form** (the same category as our intersection form of signature $(1,\rho-1)$); the Kontsevich–Zorich cocycle is the action of a **flow** (Teichmüller) on that bundle; and Forni proves a **spectral gap** ($\lambda_2<\lambda_1$) and **non-vanishing** of exponents via a **curvature formula** (Kontsevich–Forni: $\lambda_1+\dots+\lambda_g=\int \mathrm{tr}(B_\omega B_\omega^*)\,d\mu$) integrated against the **Masur–Veech measure**. Several arrows of the analogy are **tight**: indefinite form ↔ indefinite form; cocycle over flow ↔ $\Delta_\mu$ transport; curvature positivity ↔ Hodge index. [DATA + ANALOGY tight]

2. **BUT the analogy breaks at TWO structural points, both decisive (§2.4, §4):**
   - **(R1) ergodicity/hyperbolicity:** the Teichmüller flow is **non-uniformly hyperbolic and ergodic/mixing** with respect to a measure (Masur–Veech) that is **pure geometry of moduli space**. The $\mathbb R_+^*$ flow of the scaling site is an **isometric translation** (irrational rotation over $C_p$), **NOT hyperbolic**, with no nontrivial Lyapunov exponents of its own. The analogy "Lyapunov exponents ↔ zeros of ζ" is **speculative**, and where one tries to make it tight (§2.3) it falls back on Connes's trace formula.
   - **(R2, THE DECISIVE ONE) the source of the measure:** the Masur–Veech measure is defined by the **flat geometry of translation surfaces**, PRIOR to any L-function. The "ergodicity/curvature" of the scaling site that would give the analogous positivity **is NOT external geometry**: the distributional trace of the $\mathbb R_+^*$ flow **IS** the arithmetic side of Weil's explicit formula (Connes 1999; R-LEF-FLOW Doc 119) — the flow **carries ζ inside it**. [DATA + COMPUTATION]

3. **The analogue of "the signature persists" (§3):** would be a **foliated Forni spectral gap** — a statement that the intersection form of the square, transported by the cocycle of the $\mathbb R_+^*$ flow, preserves its signature $(1,\rho-1)$ because the **curvature form of the foliated Hodge bundle is semidefinite with the correct sign** (non-vanishing of the "second exponent" = absence of excess positive directions over the primitive = absence of off-critical quadruples $m=\kappa(Q)/2=0$). Precise statement in §3.3.

4. **The circularity test (§4) — the most important question of the doc, SHARP ANSWER:** in Teichmüller theory, Forni's positivity is **external** because the flow is pure geometry (moduli spaces of flat surfaces) and the Masur–Veech measure knows no L-function; the curvature of the Hodge bundle is computed from the **varying complex structure**, external to the bounded object. On the scaling site, **the $\mathbb R_+^*$ flow is NOT pure geometry: it is defined so that its trace reproduces $\sum_p\log p\cdot(\dots)$ = the prime side of the explicit formula**, and the "curvature/measure" that would give the Forni-analogous positivity is, via Weil's formula, **secretly equivalent to the zeros↔primes cancellation = RH**. **The flow carries ζ inside it.** Hence the Forni-analogous positivity **is circular** (it falls back on P43: the VALUE of the functional is external — computed from the primes — but its INERTIA/signature is the position of the zeros).

5. **VERDICT (§5): (b) — correct framework but CIRCULAR**, with a nuance of (c) in the hyperbolicity arrow. Dynamical Hodge theory is the **structurally correct** framework (the only precedent of positivity of an indefinite Hodge bundle by an external method) — and that is informative, it validates the direction of Doc 126 §5.3. But Forni's **source of externality** (a moduli measure foreign to ζ) **has no non-circular analogue** on the scaling site, because the flow of the scaling site **is** the flow whose trace is the explicit formula. The exact difference: **the Teichmüller flow is geometry; the flow of the scaling site is the explicit formula disguised as geometry.** This is Doc 119's tension T3 in its sharpest form, and it agrees with the NC3 verdict of Doc 125 §6.3 (the flow-trace route = Lefschetz = circular) via a fourth independent route.

---

## 1. THE PRECEDENT [DATA, fixed with precision]

### 1.1. The Hodge bundle and its indefinite intersection form

**[DATA]** (Forni, *Deviation of ergodic averages for area-preserving flows on surfaces of higher genus*, Annals of Math. (2) 155 (2002) 1–103; survey Forni *On the Lyapunov exponents of the Kontsevich–Zorich cocycle*, Handbook of Dynamical Systems vol. 1B, chap. 8; Matheus, *Disquisitiones Mathematicae*, Hubert 2012 Bourbaki notes; confirmed via WebSearch/WebFetch this session.)

Let $\mathcal H_g$ (or a stratum $\mathcal H(\kappa)$) be the moduli space of **translation surfaces** = pairs $(X,\omega)$ with $X$ a Riemann surface of genus $g$ and $\omega$ a holomorphic 1-form (abelian differential) with zero divisor of type $\kappa$. Over $\mathcal H_g$ lives the **Hodge bundle** $H^1$: the fiber over $(X,\omega)$ is $H^1(X,\mathbb R)$ (real, of rank $2g$), or its complexification $H^1(X,\mathbb C)=H^{1,0}\oplus H^{0,1}$.

- **Intersection form.** Over $H^1(X,\mathbb R)$ lives the **symplectic intersection form** (cup product) $\langle\alpha,\beta\rangle=\int_X\alpha\wedge\beta$, **antisymmetric, non-degenerate** (Poincaré). Its complexification, restricted to the holomorphic part with the Hodge sign, gives the **Hermitian Hodge form** $h(\alpha,\beta)=\tfrac{i}{2}\int_X\alpha\wedge\bar\beta$, which is **positive-definite on $H^{1,0}$ (holomorphic forms) and negative-definite on $H^{0,1}$** — that is, of **signature $(g,g)$**, **INDEFINITE**. [DATA]

> **Point I fix for the whole analogy:** the natural form of the Hodge bundle is **INDEFINITE** (signature $(g,g)$ in the Hermitian version; symplectic in the real one). It is the **same category** as our intersection form of the square, signature $(1,\rho-1)$ (Doc 124, Doc 125 §5.1). This is what makes the precedent relevant and not a false lead: both worlds are about **positivity-on-a-subspace within an indefinite form**, not global positivity.

### 1.2. The Kontsevich–Zorich cocycle (the action of the flow on $H^1$)

**[DATA].** The **Teichmüller flow** $g_t$ acts on $\mathcal H_g$ by $g_t\cdot(X,\omega)=(X,e^{t}\,\Re\omega+i\,e^{-t}\,\Im\omega)$ — it stretches the horizontal direction by $e^t$ and contracts the vertical one by $e^{-t}$ (it is the diagonal part of the $SL(2,\mathbb R)$ action on flat surfaces). The **Kontsevich–Zorich cocycle** $G_t^{KZ}$ is the action of $g_t$ on the Hodge bundle, via the **Gauss–Manin parallel transport** of cohomology along the Teichmüller orbit, **renormalized** by the flow. [DATA]

- $G_t^{KZ}$ is a **symplectic cocycle** (it preserves the intersection form $\langle\cdot,\cdot\rangle$): Gauss–Manin transport preserves the integral structure $H^1(X,\mathbb Z)$ and the cup form. [DATA — **this is the key property for the analogy**: the flow cocycle **preserves the indefinite form**, just as we will ask of the $\mathbb R_+^*$ flow on the square.]
- The **Lyapunov exponents** of the cocycle (with respect to a $g_t$-invariant ergodic measure $\mu$) form a symmetric spectrum
$$ 1=\lambda_1\ge\lambda_2\ge\dots\ge\lambda_g\ge 0\ge-\lambda_g\ge\dots\ge-\lambda_1=-1 $$
(symmetric by symplectic simplicity; $\lambda_1=1$ always, the "tautological" direction of $\omega$ itself). [DATA]

### 1.3. Forni's theorem: non-vanishing and gap, by an EXTERNAL method

**[DATA]** (Forni 2002 Annals; Kontsevich–Forni formula; confirmed via WebFetch Matheus this session.) The two statements that matter:

**(F1) Non-vanishing / hyperbolicity of the KZ cocycle.** For the **Masur–Veech measure** $\mu_{MV}$ (the natural, absolutely continuous measure on the stratum), **all Lyapunov exponents are nonzero**: $\lambda_g>0$. The KZ cocycle is **non-uniformly hyperbolic** (Pesin); the number of strictly positive exponents is exactly $g$ (= the symplectic half). [DATA]

**(F2) Spectral gap.** Forni proves that for ergodic measures over the **principal stratum**, $\lambda_2<\lambda_1=1$ — a **strict gap** below the tautological exponent. [DATA]

**(F3) — THE MECHANISM, decisive for the circularity test.** The proof is **variational-ergodic via a curvature formula**, NOT a hypothesis about the exponents. The **Kontsevich–Forni formula**:
$$ \lambda_1^\mu+\lambda_2^\mu+\dots+\lambda_g^\mu \;=\; \int_{\mathcal H} \big(\Lambda_1(\omega)+\dots+\Lambda_g(\omega)\big)\,d\mu(\omega), $$
where $\Lambda_i(\omega)$ are the **eigenvalues of the matrix $H_\omega=B_\omega B_\omega^*$**, and $B_\omega$ is the **second fundamental form** (Kodaira–Spencer map) of the holomorphic subbundle $H^{1,0}\subset H^1\otimes\mathbb C$ with the Gauss–Manin connection. [DATA]

**[DATA] Why the right-hand side is $\ge 0$ — the source of positivity.** The integrand $\mathrm{tr}(B_\omega B_\omega^*)\ge 0$ because it is the trace of $B B^*$ with $B^*$ the **adjoint with respect to the Hodge Hermitian product, which is positive-definite on $H^{1,0}$** (§1.1). It is the **curvature form of the Hodge bundle**, a $(1,1)$-form that is **positive-semidefinite** by geometric construction. The positivity of the exponents (and the gap) comes from **integrating a non-negative curvature against the invariant measure** — a differential-geometry + ergodicity argument, **that uses no information about the $\lambda_i$ one wants to conclude.** [DATA — **this is the pure externality that must be compared**.]

### 1.4. Eskin–Kontsevich–Zorich: the sum of exponents = geometry

**[DATA]** (Eskin–Kontsevich–Zorich, *Sum of Lyapunov exponents of the Hodge bundle with respect to the Teichmüller geodesic flow*, Publ. Math. IHÉS 120 (2014) 207–333; arXiv:1112.5872; confirmed via WebSearch this session.) The formula:
$$ \lambda_1+\dots+\lambda_g \;=\; \kappa_\mu \;+\; \frac{\pi^2}{3}\,c_{\mathrm{area}}(\mathcal C), $$
where $\kappa_\mu$ is an **explicit combination of the orders of the zeros of $\omega$** (a "line bundle degree" term over the stratum — tautological / Lyapunov classes = degrees) and $c_{\mathrm{area}}(\mathcal C)$ is the **Siegel–Veech constant** of the component (asymptotic count of cylinders/saddle connections — periodic-orbit counting geometry). [DATA]

> **What EKZ fixes for us:** the sum of exponents is a **geometric-topological invariant** (bundle degrees + Siegel–Veech count), computable **without** integrating the cocycle, **without** knowing the individual exponents. It is the model case of "a spectral positivity/bound reduced to external geometry." The type of theorem that Doc 126 §5.3 point 2 asked for: a structural invariant that gives the signature, external to the bounded object.

**[DATA — what type of positivity/signature they prove and how, summarized]:** Forni/KF/EKZ prove **non-vanishing and a gap in a Lyapunov spectrum of a symplectic cocycle over a bundle with an indefinite form**, by **(i) ergodicity of the flow with respect to Masur–Veech + (ii) a positive-semidefinite curvature formula (Kontsevich–Forni) + (iii) an identification of the sum with geometric degrees (EKZ)**. The source is **external**: the measure and the curvature are defined by the **flat geometry / varying complex structure** of the surfaces, with no hypothesis about the exponents and no L-function.

---

## 2. THE ANALOGY [ANALOGY, honest degree of fit, arrow by arrow]

I build the candidate dictionary and classify each arrow as **tight / partial / speculative**.

### 2.1. Correspondence table

| Teichmüller object | Scaling-site object | Fit |
|---|---|---|
| Moduli space $\mathcal H_g$ of translation surfaces | (?) the "moduli space" of the square / family of the $C_p\times C_p$ | **partial** (§2.2) |
| Teichmüller flow $g_t$ (geodesic, hyperbolic) | Scaling flow $\mathbb R_+^*$, $u\mapsto u+\log\mu$ | **speculative** (§2.4) — breaking point R1 |
| Hodge bundle $H^1$, INDEFINITE symplectic/Hermitian form $(g,g)$ | Intersection form of the square, signature $(1,\rho-1)$ | **tight** (§2.1bis) |
| KZ cocycle $G_t^{KZ}$ (Gauss–Manin, preserves the form) | Transport of correspondences $\Delta_\mu$ by the flow (preserves $D\cdot D'$) | **partial→tight** (§2.3) |
| Masur–Veech measure $\mu_{MV}$ (flat geometry, ergodic) | (?) invariant measure of the $\mathbb R_+^*$ flow = Haar measure of $\mathbb R_+^*$ / type II | **partial but POISONED** (§2.4, §4) |
| Lyapunov exponents $\lambda_i$ | Zeros of ζ / imaginary parts / $\kappa(Q)=2m$ | **speculative** (§2.3) |
| Gap $\lambda_2<\lambda_1$ / non-vanishing $\lambda_g>0$ | RH = exact signature $(1,\rho-1)$ = $m=0$ | **partial** (§3) |
| Kontsevich–Forni curvature formula (external) | (?) a curvature formula of the foliated Hodge bundle of the square | **the wish — the §4 test decides whether a non-circular one exists** |

### 2.1bis. The TIGHT arrow: indefinite form ↔ indefinite form

**[ANALOGY tight].** The Hodge form on $H^1$ is indefinite (signature $(g,g)$); our intersection form is indefinite (signature $(1,\rho-1)$). In **both** cases the relevant positivity is **on a subspace**: in Forni, curvature positivity over $H^{1,0}$ (the "holomorphic primitive"); in ours, **negative** definiteness over the primitive $P^1=(f_1+f_2)^\perp$ (Doc 125 §5.2). The structure "positivity of a definite form inside an indefinite form, transported by a flow that preserves the indefinite form" is **literally the same**. This arrow is **tight** and is the reason the precedent deserves the document. [Agrees with Doc 124 §1.1: Hodge index = intersection positivity over the primitive.]

### 2.2. The moduli-space arrow: PARTIAL

**[ANALOGY partial].** Teichmüller theory has a **genuine moduli space** $\mathcal H_g$ of finite dimension, with a **family of geometric objects** (flat surfaces) over which the flow moves, and the **complex structure varies** from fiber to fiber (hence the nontrivial curvature of the Hodge bundle). On the scaling site, the square $C_p\times C_p$ is **a fixed object** per prime $p$; there is no "family of squares with varying complex structure" over which the $\mathbb R_+^*$ flow moves a base point. The $\mathbb R_+^*$ flow acts **inside** a fixed square (translation of the diagonal), not over a moduli space of squares.

**Consequence (the deepest difference, feeding §4):** in Forni's setting the curvature of the Hodge bundle is **nontrivial because the complex structure changes** along the orbit (the Hodge period $H^{1,0}\subset H^1$ rotates). On the scaling site **there is no varying complex structure** — the $\mathbb R_+^*$ flow is an **isometry** of the tropical torus $C_p\times C_p$, which **does not change the intersection form nor "rotate the Hodge period."** Hence the geometric source of Forni's curvature **has no counterpart**: there is no complex-structure variation generating the second fundamental form $B_\omega$. [ANALOGY: partial, with an asymmetry that turns fatal in §4.]

### 2.3. The cocycle and "exponents" arrow: PARTIAL → SPECULATIVE

**[ANALOGY partial → tight for the structural part].** The KZ cocycle is the transport of the form along the flow, preserving it. The analogue is clear and reasonable: the $\mathbb R_+^*$ flow transports the correspondence classes $\Delta_\mu$ (Doc 125 §2.4: $\Delta_\mu=\{v=u+\log\mu\}$, translation of the diagonal), and the composition of correspondences / the intersection form $D\cdot D'$ is transported. The stable intersection of Allermann–Rau **is invariant under translation** (it is an isometry of the torus), so the "cocycle" preserves the intersection form. **This structural part is tight**: there is a symplectic-tropical cocycle of the flow. [ANALOGY tight for the cocycle+form *structure*.]

**[ANALOGY speculative — the "exponents ↔ zeros" arrow, where the strain is greatest].** What is the "Lyapunov spectrum" of the $\mathbb R_+^*$ flow's cocycle? Here the analogy is stretched to its limit. Two attempts:
- **(i) Identifying the exponents with the zeros of ζ.** The distributional trace of the $\mathbb R_+^*$ flow over the CCM Hilbert space **has as spectrum precisely the imaginary parts of the zeros** (Connes 1999: the scaling operator $D=u\partial_u$ has eigenvalues at the zeros; the trace formula gives $\sum_\rho\hat h(\rho)$). In that sense, the "exponents/frequencies" of the scaling flow **ARE** the zeros. But this **is NOT a Lyapunov spectrum** (exponential growth rates of a cocycle); it is a **frequency spectrum** of an isometric flow. The isometric translation has **all Lyapunov exponents zero** — a purely point/rotational spectrum, not hyperbolic. The "Lyapunov exponents ↔ zeros" arrow is therefore **speculative and, worse, categorically wrong**: it confuses the Lyapunov spectrum (hyperbolicity) with the frequency spectrum (rotation).
- **(ii) Identifying the "excess of positive directions" $m=\kappa(Q)/2$ with a gap defect.** More promising structurally (§3): off-critical quadruples = excess positive directions over the primitive = "exponents that crossed to the wrong side." This is **partial**: it has the right flavor (a gap that is preserved ↔ absence of excess) but there is no real hyperbolic cocycle to support it.

### 2.4. Breaking point R1: is the $\mathbb R_+^*$ flow ERGODIC and HYPERBOLIC like the Teichmüller one?

**[DATA — the Teichmüller property].** The Teichmüller flow is **non-uniformly hyperbolic (Pesin), ergodic and exponentially mixing** with respect to Masur–Veech (Veech; Avila–Gouëzel–Yoccoz for exponential mixing; confirmed via WebSearch this session: "the Teichmüller flow is non-uniformly hyperbolic in the sense of Pesin theory; the Kontsevich–Zorich cocycle is non-uniformly hyperbolic, all Lyapunov exponents nonzero"). **The hyperbolicity of the base flow is what generates nontrivial Lyapunov exponents of the cocycle.** [DATA]

**[COMPUTATION — the property of the scaling flow].** The $\mathbb R_+^*$ flow over $C_p=\mathbb R/(\log p)\mathbb Z$ is $u\mapsto u+\log\mu$: an **irrational translation/rotation** (when $\log\mu/\log p\notin\mathbb Q$). Properties:
- **Ergodic**: yes, with respect to the Haar (Lebesgue) measure of $C_p$ — an irrational rotation is uniquely ergodic. [COMPUTATION — but this is **rotational** ergodicity, not hyperbolicity.]
- **Mixing**: **NO** — a rotation is not mixing (it has point spectrum). [COMPUTATION]
- **Hyperbolic**: **NO** — it is an isometry, **all Lyapunov exponents of the flow itself are zero**. There are no exponential stable/unstable directions. [COMPUTATION]

> **R1 — THE ANALOGY BREAKS HERE AT ITS DYNAMICAL LEVEL.** The Teichmüller flow is hyperbolic and mixing; the $\mathbb R_+^*$ flow of the scaling site is an **isometry/rotation**, not hyperbolic, not mixing. Forni's machinery **needs the hyperbolicity of the base flow** for the cocycle to have nontrivial exponents and for the curvature integral against the invariant measure to have the content of a "growth rate." Over an isometric flow, **the Hodge cocycle does not grow exponentially** (the exponents are zero), and the Kontsevich–Forni formula would give $\sum\lambda_i=0$ — **trivial, no gap, no spectral content**.

**[COMPUTATION] Important nuance — where the analogy might be rescued, and why it falls back on ζ.** One could object: the relevant flow is not the translation over **one** $C_p$, but the **global** scaling flow over the whole site (all primes at once), whose trace **does** have spectral content (the zeros). Indeed: the global scaling operator $D=u\partial_u$ on $L^2$ of adelic classes (Connes) has a rich spectrum. BUT that spectrum **is not Lyapunov (hyperbolic) but of frequencies**, and —critically— **the global scaling flow with spectral content IS the flow whose trace is the explicit formula**. That is: as soon as the flow is enriched to have "nontrivial spectrum" like Teichmüller's, that enrichment **is** the introduction of ζ. **R1 and R2 are the same break seen twice: either the flow is isometric (pure geometry, but with no spectral content = an empty analogy), or it has spectral content (but then it is the explicit formula = circular).** This is the central dilemma of the document.

---

## 3. THE ANALOGUE OF "THE SIGNATURE PERSISTS" [the heart of it]

### 3.1. Which Forni property plays the role of "Hodge index over the primitive"

**[ANALOGY].** In Docs 124–125, G2/RH = "the intersection form is **negative-definite over the primitive** $P^1=(f_1+f_2)^\perp$, exact signature $(1,\rho-1)$, no excess positive directions." The **excess positive directions** over the primitive = the off-critical quadruples = $m=\kappa(Q)/2$ (Doc 119; P35). RH $\iff m=0$ $\iff$ no extra positive direction.

In the language of dynamical Hodge theory, the natural analogue is:
- the **primitive** $\leftrightarrow$ the subspace of the Hodge bundle where the curvature form must have a sign;
- "no excess positive direction" $\leftrightarrow$ **the spectral gap / the non-vanishing**: that no exponent "crosses" to the forbidden side, or that the second fundamental form has no eigenvalue of the wrong sign.

### 3.2. The three target candidates, evaluated

**[COMPUTATION]**
- **(a) Forni's spectral gap ($\lambda_2<\lambda_1$) ↔ the signature.** Fit **partial**. Forni's gap says "the second exponent is strictly below the first" — a statement of **separation within the positive half-spectrum**. Its analogue would be "the single positive direction (the broad one $f_1+f_2$, $\lambda_1$) is strictly separated from the rest, which is negative (the primitive)." This is **exactly the signature $(1,\rho-1)$**: one positive, separated from $\rho-1$ negatives. **This is the best arrow.** Forni's gap ↔ the isolated "1" of the signature $(1,\rho-1)$.
- **(b) Non-vanishing of exponents ($\lambda_g>0$) ↔ absence of off-critical zeros.** Fit **speculative**. Non-vanishing says "no exponent collapses to 0" (the cocycle is hyperbolic). The analogue "no zero lies off the critical line" is not structurally the same thing: an off-critical zero is not "a vanishing exponent" but "a direction with the wrong signature." The more natural arrow for off-critical is **(a)** (extra positive direction), not (b).
- **(c) Spectral simplicity (Avila–Viana) ↔ multiplicity of zeros.** Fit **speculative but suggestive**. Avila–Viana proved that the KZ spectrum is **simple** (all $\lambda_i$ distinct) for Masur–Veech. The analogue "all zeros simple" is a classical conjecture (simplicity of the zeros of ζ). Structurally: simplicity of the Lyapunov spectrum ↔ simplicity of the zeros. **It is the prettiest arrow**, but (i) the simplicity of zeros is NOT RH, it is orthogonal to RH; (ii) it rests on the "exponents ↔ zeros" identification that §2.3 declared categorically wrong. It remains a decorative, non-operative analogy.

### 3.3. The precise statement of the "signature persists" analogue

**[CONJECTURE — the statement that, within the dynamical framework, would give G2/RH].**

> **FOLIATED-GAP (analogue of Forni for the square).** *Over the foliated Hodge bundle of the scaling-site square — the bundle whose fiber is $(A^1(X\times X), D\cdot D')$ with its intersection form of signature $(1,\rho-1)$, transported by the cocycle of the $\mathbb R_+^*$ flow — the **curvature form of the Hodge metric** (the analogue of $B_\omega B_\omega^*$ of Kontsevich–Forni) is **semidefinite with the sign that forces the signature $(1,\rho-1)$ to persist under transport**: equivalently, integrated against the invariant measure of the flow, its "foliated second exponent" satisfies the gap, so that the number of excess positive directions over the primitive is $m=\kappa(Q)/2=0$.*

From FOLIATED-GAP it would follow that G2 = exact signature $(1,\rho-1)$ = $m=0$ = RH, exactly as Forni's positive-semidefinite curvature forces the gap $\lambda_2<\lambda_1$. **The analogue of "the signature persists" is: the curvature of the foliated Hodge bundle has the correct sign, and that —via ergodic integration against the invariant measure— forces the gap = the signature.** [CONJECTURE, partial structural fit; the operative arrow is 3.2(a).]

**[COMPUTATION] The parallel with G-125.B.** FOLIATED-GAP is **exactly** what Doc 125 §6.2 called G-125.B: "the persistence of the signature $(1,\rho-1)$ of the finite toy model over the full lattice of correspondences." Dynamical Hodge theory **renames G-125.B** as "foliated spectral gap via curvature." The value of the precedent is that it **gives a candidate method** (curvature + ergodicity) where Doc 125 only had the open gap. The §4 question is whether that method is external or circular.

---

## 4. THE CIRCULARITY TEST [decisive — the most important question of the doc]

I apply R-NC (Doc 119 §4.3) to FOLIATED-GAP, comparing with Forni's externality.

### 4.1. Why Forni is genuinely external (non-circular) — the pattern to match

**[DATA + COMPUTATION].** In Teichmüller theory, Forni's positivity **assumes nothing about the exponents**. The two sources of externality:
1. **The measure $\mu_{MV}$ is pure geometry.** Masur–Veech is defined by the **flat structure** of translation surfaces (area, periods, saddle-connection lengths) — an object of **moduli-space geometry**, defined **before and without** any L-function, any dynamical zeta function, anything arithmetic. [DATA]
2. **The curvature $B_\omega B_\omega^*$ is pure differential geometry.** It is computed from the **variation of the complex structure** (Kodaira–Spencer), from the Hodge period $H^{1,0}\subset H^1$ that rotates along the orbit. It is geometry of the variation of Hodge structure, **external to the Lyapunov spectrum one wants to bound**. [DATA]

**Result: Forni PASSES an analogue of NC1 (the measure and the curvature mention no exponent), NC2 (the formula holds for the WHOLE stratum, every generic surface — it massively overgenerates), NC4 (an exponent that vanished would force a degenerate curvature, visible geometrically without "localizing" anything).** It is the model of external positivity.

### 4.2. Is the scaling-site flow pure geometry or does it carry ζ inside it? — THE DECISION

**[DATA — the fact that decides everything].** (Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999); R-LEF-FLOW Doc 119 §3.4; Doc 125 §3.3 via (c).) The **distributional trace of the scaling flow $\mathbb R_+^*$** over the CCM space **reproduces the arithmetic side of Weil's explicit formula**:
$$ \mathrm{Tr}_{\mathrm{distr}}\Big(\int h(u)\,(\text{scaling flow})\,du\Big) \;=\; \sum_p\sum_{m\ge1}\frac{\log p}{p^{m/2}}\,\hat h(m\log p)\;+\;(\text{archimedean term}), $$
and the explicit formula equates this to $\sum_\rho\hat h(\rho)$. **The periodic orbits of the scaling flow are the primes** (period $\log p$); **the spectrum of the generator is the zeros.** [DATA]

**[COMPUTATION — the direct, brutally frank answer]:**

> **The $\mathbb R_+^*$ flow of the scaling site CARRIES ζ INSIDE IT. It is not pure geometry.** Unlike the Teichmüller flow — whose periodic orbits are the closed geodesics of the Teichmüller metric, objects of moduli geometry with no arithmetic content — the **periodic orbits of the scaling flow ARE the primes**, and its trace **IS** the explicit formula. The scaling flow **is defined (in its spectrally-contentful version, the only useful one for the analogy, §2.4) precisely so that its trace is $\sum_p\log p/p^{m/2}$**. The arithmetic structure is not external to the flow: **it is the flow.**

**Consequence for the "curvature/measure" of FOLIATED-GAP.** The invariant measure with content (the one that would have "nontrivial exponents," §2.4) is the one that makes the trace the explicit formula; the "curvature form of the foliated Hodge bundle" that would measure the gap would be **a rewriting of the second variation of the Weil form under the flow**. And by P43 (master quantifier): the **VALUE** of that quadratic functional is computed **from the primes alone** (it is the arithmetic side, external in appearance), but its **INERTIA** —the partition of its negative index into blocks, = the signature, = $m=\kappa(Q)/2$, = the "gap"— **is not determined without the positions of the zeros**. The foliated gap **is the inertia**, not the value. And the inertia is RH. [COMPUTATION, agrees with P43 §autonomy.]

### 4.3. R-NC applied to FOLIATED-GAP

**[COMPUTATION]**
- **NC1 (externality of the definition):** the intersection form $D\cdot D'$ and the classes $f_1,f_2,\Delta$ are functorial from the site (Doc 125 §6.3 already conceded this). **PASSES** — but it is the same superficial externality as Forni's: so far so good.
- **NC2 (overgeneration):** does the foliated gap hold for EVERY class / every correspondence by curvature, the way Forni's holds for the whole stratum? **HERE IT FAILS.** In Forni's setting the curvature formula holds for every generic surface because the measure and the curvature are geometric. On the scaling site, the only measure with spectral content is the one that reproduces the explicit formula; the "curvature" only has content **evaluated on the correspondences of the flow = those that carry the primes/zeros**. It does not overgenerate to classes unrelated to ζ with nontrivial content (on unrelated classes the curvature is that of the isometric flow = trivial, §2.4). **FAILS NC2** — exactly as in Doc 125 §6.3 NC2-conditional/G-125.B.
- **NC3 (no reduction to catalogued RH-equivalent positivities):** the foliated curvature with content **IS** the second variation of the Weil form under the scaling flow = the flow's Lefschetz trace = MW-1/MW-6 of the catalogue (Doc 124 §2.5). **FAILS NC3 flatly** — identical to the verdict of Doc 125 §6.3 (the flow-trace route is the Lefschetz formula, circular) and to tension T3 of Doc 119.
- **NC4 (two-worlds test):** under ¬RH (an off-critical quadruple, $m\ge1$), is FOLIATED-GAP false for a reason computable from the curvature without localizing the zero? **FAILS** — by P43: the VALUE does not distinguish (it is computed from the primes in both worlds); only the INERTIA distinguishes, and the inertia requires the positions of the zeros (inaccessible binariness, Doc 108). **FAILS NC4.**

**[COMPUTATION] R-NC verdict:** FOLIATED-GAP **passes NC1 but FAILS NC2, NC3, NC4** — **it is circular**. The difference with Forni is **exactly NC2**: Forni's curvature overgenerates (it holds for the whole geometric stratum, external to any ζ); the scaling site's foliated curvature **only has content over the correspondences of ζ**, because **the flow carries ζ inside it**, and without ζ the flow is isometric-trivial (§2.4 R1).

### 4.4. The difference that decides everything, in one sentence

**[COMPUTATION].** **The Teichmüller flow is pure geometry (moduli spaces of flat surfaces); its Forni positivity is external because the Masur–Veech measure and the curvature of the Hodge bundle are defined without ζ. The scaling-site flow, as soon as it has the spectral content the analogy needs, IS the explicit formula (its periodic orbits are the primes, its trace is $\sum_p\log p\,\hat h(m\log p)$); hence the Forni-analogous positivity is not external: it is Weil's positivity = RH, rewritten in the language of foliated curvature.** The dynamical Hodge precedent reproduces **the structure** (indefinite form + cocycle + curvature → gap) but **not the source of externality**, because Forni's source of externality is moduli geometry, and our flow is not moduli geometry: it is arithmetic disguised as a flow.

---

## 5. VERDICT

### 5.1. Classification (a)/(b)/(c)/(d)

**[COMPUTATION] Verdict: (b) — correct framework but CIRCULAR, with a component of (c) in the dynamical arrow (R1).**

Breakdown:
- **Is it the correct framework?** **YES, structurally.** Dynamical Hodge theory is the **only known precedent** of a positivity/gap of a Hodge bundle **with an indefinite form**, transported by a flow cocycle, proved by an **external** method (curvature + ergodicity). The arrows indefinite-form↔indefinite-form (§2.1bis) and cocycle-preserves-form↔transport-preserves-intersection (§2.3) are **tight**. This validates the direction Doc 126 §5.3 asked for and gives a precise name to the candidate method: **a Kontsevich–Forni-type curvature formula + ergodic integration**. The identification Forni-gap ↔ the isolated "1" of the signature $(1,\rho-1)$ (§3.2a) is the strongest operative arrow.

- **Is it non-circular?** **NO.** The §4 test is sharp: Forni's externality rests on the **Teichmüller flow and the Masur–Veech measure being pure moduli geometry, foreign to ζ**. The scaling-site flow, in its spectrally-contentful version (the only one giving a non-empty analogy), **carries ζ inside it**: its periodic orbits are the primes, its trace is the explicit formula. The foliated curvature that would give the gap **is** the second variation of the Weil form = MW-1 = RH. FAILS NC2/NC3/NC4. **Circular.** (b).

- **The (c) component — structural break in R1.** There is also a genuine dynamical break: the $\mathbb R_+^*$ flow over $C_p$ is an **isometry/rotation, NOT hyperbolic nor mixing**, unlike the Teichmüller flow. Over an isometric flow the Hodge cocycle **does not grow**, the Lyapunov exponents are **zero**, the Kontsevich–Forni formula is **trivial**. The analogy "Lyapunov exponents ↔ zeros" is **categorically wrong** (§2.3i): the spectrum of the zeros is one of **frequencies** (rotation), not of **Lyapunov** (hyperbolicity). To rescue spectral content one must pass to the global flow, and there R1 collapses into R2 (the flow with content = the explicit formula). **The flow is not hyperbolic in the way Forni requires** — that is (c). The combination is: the analogy breaks structurally at the dynamical level (c) **and**, where it is forced to have content, it becomes circular (b). **(b) is the dominant verdict because it captures the root cause: the source of non-triviality IS ζ.**

### 5.2. Does the flow carry ζ inside it, or is it external geometry — the direct answer

**[COMPUTATION] IT CARRIES ζ INSIDE IT.** This is the answer to the most important question raised. The Teichmüller flow is pure geometry: its closed geodesics are moduli objects with no arithmetic. The scaling-site flow **is defined so that its distributional trace is the prime side of the explicit formula** (Connes 1999); its periodic orbits **are the primes**; its generator has **the zeros** as its spectrum. There is no way to extract spectral content from it without extracting ζ. Hence the Forni-analogous positivity, which in Teichmüller theory is external, **on the scaling site is Weil's positivity renamed**. A fourth independent derivation of the same wall (Doc 119 reverse engineering; Doc 124/125 intersection form; Doc 126 AHK/Babaee–Huh; here, dynamical Hodge theory).

### 5.3. What would be missing, and whether there is a path to (a)

**[CONSTRUCTION] The only conceivable path toward (a)** —and it is very narrow— would be to find a **measure and a curvature of the foliated Hodge bundle of the square that are geometric in a sense independent of the ζ-laden scaling flow**, that is, a "tropical square moduli" structure with **genuine structure (complex/Hodge) variation** generating a nontrivial second fundamental form **without** that variation being the scaling flow. This would require:

1. **[GAP — the deepest one] A variation of Hodge structure over a family of squares, external to the scaling flow.** In Teichmüller theory the curvature comes from the complex structure **changing** over $\mathcal H_g$. On the fixed square $C_p\times C_p$ the $\mathbb R_+^*$ flow is isometric (it does not change the structure). One would have to exhibit a **moduli space of tropical squares** with a Hodge bundle of nontrivial curvature **whose flow is NOT the arithmetic scaling one**. There is no candidate. If one existed, its relation to ζ would be the new circularity test.

2. **[GAP] The infinite-dimensional FOLIATED Kähler package** (Doc 126 §5.3 point 3, R-SIG≺R-FIN): even with external curvature, the obstruction persists that the pure part is infinite-dimensional and signatures are not continuous under the limit (T2). Forni's is finite-dimensional ($2g$); the infinite-dimensional analogue of the Kontsevich–Forni formula **does not exist**.

3. **[VERIFICATION — the decisive experiment of Phase 42] Is there any foliation of the square, distinct from the scaling flow, with nontrivial Hodge curvature external to ζ?** If NOT (the likely answer, because the only natural dynamics of the site is the scaling one = arithmetic), then (a) is **closed** and the verdict hardens to definitive (b)/(c), not merely undetermined.

**[COMPUTATION] First concrete step, if (a) is pursued:** try to define, over the tropical torus $C_p\times C_p$, a **variation of "tropical Hodge structure"** (an analogue of the $H^{1,0}\oplus H^{0,1}$ decomposition, tropically, via the Allermann–Rau metric and a polarization) and compute its **second fundamental form** under a deformation of the polarization **that is NOT the scaling translation**. If the resulting curvature is nontrivial and its integral controls the signature **without** invoking the flow's trace, there is a seed of (a). If every natural deformation of the polarization turns out to be the scaling flow (= arithmetic), (a) is closed. **Frank prediction: it is closed**, because the only structure that distinguishes the positive/negative directions of the primitive is the one that knows where the zeros are (P43 inertia), and that is ζ.

### 5.4. Synthesis

**[COMPUTATION]** Dynamical Hodge theory is the **structurally correct framework** —it faithfully reproduces the architecture "indefinite form + flow cocycle + semidefinite curvature → gap = signature"— and that is why it was worth identifying: it names the candidate method (Kontsevich–Forni-type curvature) and the operative arrow (Forni's gap ↔ the "1" of the signature). **But it fails at the one thing that matters for non-circularity: the source of externality.** Forni's positivity is external because the Teichmüller flow is pure moduli geometry; the foliated analogous positivity is **circular** because the scaling-site flow **is** the explicit formula (periodic orbits = primes, trace = the arithmetic side of Weil). The precedent, far from crossing the wall, **explains why the wall is where it is**: the wall is the difference between "geometric flow (Teichmüller)" and "arithmetic flow (scaling)," which is the P43 difference between the **value** (computable from the primes) and the **inertia** (the position of the zeros). The foliated gap is inertia. The inertia is RH.

**Overall verdict: (b) correct framework but CIRCULAR**, with a structural break (c) in the hyperbolicity arrow (the scaling flow is isometric, not hyperbolic). It is not (a) because Forni's externality does not transplant; it is not (d) because the §4 test is conclusive (the flow carries ζ inside it, via Connes 1999, a firm datum). The (a) path would require a foliation of the square with Hodge curvature external to ζ, today absent and probably nonexistent (the only dynamics of the site is arithmetic).

---

## 6. Honesty and record

No new theorem was proved. What was **read from source** was: Forni 2002 Annals + survey chap. 8 Handbook; the Kontsevich–Forni formula $\sum\lambda_i=\int\mathrm{tr}(BB^*)d\mu$ via Matheus's Bourbaki notes; EKZ Publ. IHÉS 2014 $\sum\lambda_i=\kappa_\mu+\tfrac{\pi^2}{3}c_{\mathrm{area}}$; ergodicity/non-uniform-hyperbolicity of the Teichmüller flow with respect to Masur–Veech; Avila–Viana simplicity — and it was **compared** with the internal corpus:

- **The precedent is genuine and the structure is tight** in two arrows (indefinite form; cocycle preserves form). Dynamical Hodge theory **is** the correct framework for "positivity of an indefinite Hodge bundle by an external method."
- **The analogy breaks at R1 (dynamics):** the scaling flow is isometric/rotational, not hyperbolic/mixing; its own Lyapunov exponents are zero; the Kontsevich–Forni formula would be trivial. "Exponents ↔ zeros" is categorically wrong (frequencies vs. Lyapunov).
- **The analogy breaks at R2 (circularity, the decisive one):** Forni's externality comes from Masur–Veech and the curvature being **pure moduli geometry, without ζ**; the scaling flow with spectral content **IS the explicit formula** (Connes 1999), so the analogous foliated curvature **is** the Weil form = MW-1 = RH. FAILS NC2/NC3/NC4.
- **The analogue of "the signature persists" is FOLIATED-GAP** (§3.3) = G-125.B renamed as a foliated spectral gap; the operative arrow is **Forni's gap ↔ the isolated "1" of the signature $(1,\rho-1)$**.
- **The scaling-site flow CARRIES ζ INSIDE IT** (answer to the central question). The Teichmüller one is geometry; the scaling one is arithmetic disguised as geometry. That is the difference that decides.
- **Verdict: (b) circular, with a (c) component.** A fourth independent derivation of the same wall. The precedent does not cross it: it **explains** it (wall = external-value/internal-inertia, P43).

**The obstruction IS the result:** dynamical Hodge theory gives the correct language and method, and precisely because of that it shows, with maximum clarity, that the source of positivity which in Teichmüller theory is external, on the scaling site **coincides with ζ itself** — because the scaling-site flow is not a geometric flow over a moduli space, but the flow whose trace is the explicit formula.

---

## References

**External source read this session, WebSearch/WebFetch):**
- G. Forni, *Deviation of ergodic averages for area-preserving flows on surfaces of higher genus*, Annals of Math. (2) 155 (2002) 1–103 — non-vanishing and spectral gap of the Kontsevich–Zorich cocycle; variational-ergodic method via the Hodge metric. **[DATA]**
- G. Forni, *On the Lyapunov exponents of the Kontsevich–Zorich cocycle*, Handbook of Dynamical Systems vol. 1B, chap. 8 (PDF Lanneau/Grenoble) — structure of the Hodge bundle, intersection form, second fundamental form $B_\omega$. **[DATA, via survey]**
- M. Kontsevich, G. Forni — formula $\lambda_1+\dots+\lambda_g=\int(\Lambda_1+\dots+\Lambda_g)\,d\mu$, $\Lambda_i$ eigenvalues of $H_\omega=B_\omega B_\omega^*$, right-hand side $\ge0$ by positivity of the Hodge Hermitian product. **[DATA, via Matheus's Bourbaki notes, Disquisitiones Mathematicae 2012.]**
- A. Eskin, M. Kontsevich, A. Zorich, *Sum of Lyapunov exponents of the Hodge bundle with respect to the Teichmüller geodesic flow*, Publ. Math. IHÉS 120 (2014) 207–333; arXiv:1112.5872 — $\sum\lambda_i=\kappa_\mu+\tfrac{\pi^2}{3}c_{\mathrm{area}}(\mathcal C)$ (bundle degrees + Siegel–Veech constant). **[DATA]**
- Veech; A. Avila, S. Gouëzel, J.-C. Yoccoz, *Exponential mixing for the Teichmüller flow*, Publ. Math. IHÉS 104 (2006) — ergodicity, exponential mixing, non-uniform hyperbolicity (Pesin) of the Teichmüller flow with respect to Masur–Veech. **[DATA, via WebSearch]**
- A. Avila, M. Viana — simplicity of the Lyapunov spectrum of the KZ cocycle (Kontsevich–Zorich conjecture). **[DATA, via WebSearch]**

**Internal (backward-only):** Doc 126 (AHK does not apply; Babaee–Huh obstructs; tropical-foliated Kähler package; verdict (d) biased toward (b)/(c)); Doc 125 (Allermann–Rau intersection form; $G_{\text{toy}}$ signature $(1,2)$; G-125.A real/integer; G-125.B signature persistence; NC3 via (c) = Lefschetz = circular); Doc 124 (G2 = indefinite Hodge index; Weil positivity = MW-1/MW-6); Doc 119 (R-SIG/R-FIN/R-LEF-FLOW; R-NC NC1–NC4; tensions T2, T3); Doc 80 (arithmetic Castelnuovo–Severi; the form that distinguishes measures is RH-equivalent); P35 (κ(Q)=2m); P43 (master quantifier; value/inertia distinction; mean→uniform barrier).

**Classical / CC corpus (context, via internal Docs):** A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999) — trace of the scaling flow = arithmetic side of the explicit formula; periodic orbits = primes. **[DATA, via Doc 119 §3.4.]** Connes–Consani, *Geometry of the Scaling Site*, arXiv:1603.03191.

*End of Doc 127.*
