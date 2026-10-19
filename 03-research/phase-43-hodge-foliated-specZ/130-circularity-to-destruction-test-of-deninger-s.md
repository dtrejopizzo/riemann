# Doc 130 — Circularity-to-destruction test of Deninger's foliated Hodge route

**Program:** Riemann Hypothesis — Phase 43: foliated Hodge over Spec ℤ.
**Role of the document:** adversarial. Hunt for circularity in the "non-circular route" that Doc 128 declared with verdict (a). Standard of proof for "non-circular": HIGH. The program has been wrong before (W_λ≥0 survived for months; the "phase transition" r4/r5 was refuted by canonical re-verification). If Deninger's leafwise-Hodge route turns out to be circular, that is the MOST valuable result.

**Prerequisites read in source this session:** Doc 128 (verdict (a) non-circular; "in the Kähler–Riemann case positivity is DERIVED, not postulated"); Doc 127 (why Forni is circular: the flow carries ζ inside; the R1/R2 dichotomy); Doc 119 §4.3 (R-NC test, clauses NC1–NC4, verbatim); P43 main.tex (master quantifier: average→individual, value→inertia, Thm. autonomy, Principle boundary). **External source read this session (WebFetch ar5iv):** Deninger, *Real polarizable Hodge structures arising from foliations* (math/0204111, with Singhof); Deninger, *On the nature of the explicit formulas — a simple example* (math/0204194).

**Labeling discipline (absolute rule):** **[DATA]** = read in source this session (arXiv/internal with citation). **[ANALYSIS]** = my own adversarial reasoning. **[NC-VERDICT]** = result of the NC1–NC4 test. **[GAP]** = what is missing. **[NOT VERIFIED]**. NEVER "non-circular" without having attacked to destruction.

---

## 0. Executive summary — the attack and its result

Doc 128 closed with verdict **(a) non-circular framework**, resting on a single pillar: the theorem math/0204111, which proves that on a **Kähler–Riemann** foliation the Hodge–Riemann positivity over the reduced leafwise cohomology is a **theorem of leaf geometry**, not an axiom. Doc 128's logic: *if the foliated space of Spec ℤ exists and is Kähler–Riemann, positivity is derived → RH, without assuming positivity=RH.*

This document attacks that conclusion by reading in source HOW Deninger puts the complex/Kähler structure in the two cases he DID carry out (math/0204111 abstract-geometric; math/0204194 elliptic curve over 𝔽_q), and transferring the recipe to Spec ℤ. The finding is sharp and **corrects Doc 128**:

1. **[DATA] The Kähler structure of the leaves in math/0204111 is pure differential geometry, external to ζ.** The polarization theorem assumes a leafwise Kähler form $\omega_{\mathcal F}$ and a bundle-like transverse metric as a **given datum**, and derives positivity via the smooth Hodge decomposition of Álvarez López–Kordyukov + classical Kähler–Lefschetz identities. **It uses no ζ, no Mellin transform, no zero positions, no spectrum.** This confirms Doc 128's claim — *but only for the conditional implication* "Kähler–Riemann space ⟹ positivity". (§1)

2. **[DATA — THE TWIST] In the only arithmetic case carried out (math/0204194, elliptic curve), the metric that makes the space Kähler–Riemann USES Hasse's theorem |ξ|²=q as INPUT.** Verbatim from the source: the metric $g=e^t\,\mathrm{Re}(\xi\bar\eta)$ is defined *after* invoking Hasse ("according to a theorem of Hasse — the Riemann conjecture for elliptic curves over function fields — we have $|\xi|^2=q$"). Hasse = RH-for-E is **input** to the construction of the Kähler–Riemann space, not **output** of positivity. (§2)

3. **[ANALYSIS] Therefore the case actually carried out does NOT inherit Weil's miracle — it inverts it.** In Weil, the Hodge index over $C\times C$ (Castelnuovo–Severi) is a theorem of surface geometry proved WITHOUT knowing the position of the Frobenius eigenvalues, and RH-for-C is DERIVED from it. In Deninger-elliptic, RH-for-E (Hasse) is **assumed** to build the space, and RH then "follows" from an index computation on the already-constructed space. The direction of the implication is **inverted** with respect to Weil: the externality of Weil's miracle **is not replicated**. (§2.3)

4. **[ANALYSIS] P43's point of maximum suspicion materializes exactly where P43 predicted it.** The value→inertia step is: the underlying space + flow + orbits (= primes) is the **value** (external geometry, exists without RH — confirmed: the sheet $X=\tilde X/H$ exists by Hasse, which for Spec ℤ does not exist, but the analogous "space + orbits $\{\log p\}$" would indeed be external). The **Kähler–Riemann** structure (the one giving positivity) is the **inertia**: it encodes $|\xi|=\sqrt q$, i.e. where the eigenvalues are. Building the space *as Kähler–Riemann* IS putting in the zero-localization information. Doc 128's non-circularity is **empty** in P43's sense: the bare geometric space exists without RH, but the space *with the structure from which positivity is derived* is not known to be constructible without RH. (§3)

5. **[ANALYSIS] Deninger's leafwise positivity is NOT literally the same form as Connes–Consani's (Doc 124), but it collapses to the same content via a different route.** CC: spectral positivity over test functions = trace of the flow = explicit formula = RH (circular via NC3, evaluation on tests). Deninger: Hodge positivity over leaf cohomology classes = a geometric theorem **conditioned on the space being Kähler–Riemann**, and *that condition* is the one that (in the carried-out case) uses the eigenvalue localization. They are **different objects** (spectral form over tests vs polarization form over $\bar H^1_{\mathcal F}$), but **the same master quantifier separates them from RH**: CC on the value axis (the trace), Deninger on the inertia axis (the Kähler structure splitting the index). It is not "the same form renamed"; it is "the same wall in another coordinate", exactly as P43 predicts. (§4)

6. **[NC-VERDICT] INDETERMINATE with strong bias toward CIRCULAR.** The implication "Kähler–Riemann ⟹ positivity" cleanly passes NC1/NC2 (math/0204111 is pure geometry, overgenerating to every Kähler–Riemann foliation). But the antecedent "the space of Spec ℤ is Kähler–Riemann" is where the content lives, and there: in the only arithmetic witness, the Kähler–Riemann property is **installed using** the analogous RH (Hasse). It FAILS NC4 (under ¬RH it is unknown whether the space would exist non-Kähler or not exist — genuine gap), and FAILS NC3 in the carried-out case (the Kähler–Riemann property, restricted to the arithmetic object, uses $|\xi|=\sqrt q$, which for Spec ℤ is exactly the localization of the zeros). The minimal statement that would rescue non-circularity is hard and is named in §5. (§5)

**The sticking point IS the result:** Deninger relocates positivity from the *value/trace* axis (where CC is circular) to the *geometric structure of the space* axis. But P43 already said the wall reappears in value→inertia, and here it reappears exactly: the space's **Kähler–Riemann** structure IS the inertia, and the inertia is RH. Doc 128 confused "the conditional implication is geometric" (true) with "the route is non-circular" (does not follow: the antecedent of the implication is where the RH is).

---

## 1. WHERE ζ ENTERS — PART I: the Kähler structure in math/0204111 is external [DATA]

### 1.1. What the polarization theorem assumes and what it derives

**[DATA — math/0204111, Deninger–Singhof, via WebFetch ar5iv this session].** The central theorem ("real polarizable Hodge structures on the reduced leafwise cohomology of Kähler–Riemann foliations") has the following logical structure:

- **Hypothesis (given datum):** a *Kähler–Riemann foliation* $(X,\mathcal F,h=S-2i\omega_{\mathcal F})$ — i.e. a Kähler foliation (leafwise Kähler form $\omega_{\mathcal F}$ with $d_{\mathcal F}\omega_{\mathcal F}=0$, Hermitian metric $h$ on the tangent bundle to the leaves) that is **also** a Riemannian foliation (there exists a bundle-like metric on the ambient $X$). The Kähler form and the transverse metric **are assumed as input**, not derived. [Verbatim DATA: *"a Kähler foliation $(X,\mathcal F,h=S-2i\omega_{\mathcal F})$ which is also a Riemannian foliation is called a Kähler–Riemann foliation"*; *"a bundle-like Riemannian metric on the ambient manifold X is also assumed to exist"*.]
- **Conclusion (derived):** the reduced leafwise cohomology $\bar H^\bullet_{\mathcal F}(X)$ carries a real polarizable Hodge structure; Hard Lefschetz and the Hodge–Riemann bilinear relations hold on the primitive part.
- **How it is derived:** via Álvarez López–Kordyukov's smooth Hodge decomposition theorem ($\bar H^\bullet_{\mathcal F}(X)$ = global smooth forms whose restrictions to the leaves are harmonic) + the **classical Kähler–Lefschetz identities** on non-compact Kähler manifolds (the leaves). [Verbatim DATA: *"proofs being mostly consequences of the classical Kähler–Lefschetz identities on non-compact Kähler manifolds"*; *"No zeta functions or spectral arguments are used for the polarization structure in sections 2–4"*.]

**[DATA] The complex structure $J$ on $T\mathcal F$ is pure differential geometry:** it is defined as an almost-complex structure on the tangent bundle to the leaves, and its integrability follows from Newlander–Nirenberg. *It uses no arithmetic input.* The number-theoretic motivation (Serre's analogue of the Weil conjectures, §4.5 of their paper) is a **separate application**, not part of the construction of the Kähler structure.

### 1.2. [ANALYSIS] What this confirms and what it does NOT

**Confirms:** Doc 128 §1.3/§3.1 was right that the implication
$$
\boxed{\text{(Kähler–Riemann foliation)}}\;\xLongrightarrow{\text{math/0204111}}\;\boxed{\text{Hodge–Riemann polarization on }\bar H^1_{\mathcal F}}
$$
is a **genuine theorem**, whose proof is leafwise geometry external to ζ. The consequent (positivity) is NOT postulated. Up to here, NC1 (externality of the definition of positivity, given the space) is satisfied: the polarization form is defined by $Q(\xi,J\bar\xi)$ with $J,\omega_{\mathcal F}$ geometric, without mentioning ζ.

**Does NOT confirm — and here the attack begins:** the non-circularity of a *proof route for RH* is not decided by the conditional implication. It is decided by the **antecedent**: can it be established that the space of Spec ℤ is Kähler–Riemann without using ζ/RH? A frank, geometric implication "$A\Rightarrow B$" is perfectly compatible with $A$ **being equivalent to (or stronger than) RH**. Doc 128 verified the geometricity of "$A\Rightarrow B$" and concluded the non-circularity of the route — **invalid step**. The circularity question has shifted entirely to the antecedent $A$ = "the space is Kähler–Riemann". §2 attacks there.

> **[ANALYSIS] Diagnosis of Doc 128's fallacy.** Doc 128 treated "positivity is derived, not postulated" as if it were the whole of the test. But "deriving positivity **from a hypothesis $A$**" is not non-circular if $A$ already contains RH. Weil's miracle is not just that the Hodge index implies RH; it is that the Hodge index is proved **unconditionally** by surface geometry. Doc 128 verified the first half (the implication) and **assumed** the second (that $A$ be establishable without RH). The second half is precisely what §2 disproves in the witness case.

---

## 2. WHERE ζ ENTERS — PART II: in the carried-out case, the Kähler structure USES RH [DATA, the twist]

### 2.1. The witness: the elliptic curve of math/0204194

**[DATA — math/0204194, via WebFetch ar5iv this session].** Deninger builds, for an elliptic curve $E_0/\mathbb F_q$, a 3-dimensional laminated space $X=\tilde X/H$ with $\tilde X=\mathbb C\times V_\xi\Gamma\times\mathbb R$, where:
- the construction starts from a **lift to characteristic zero** of $(E_0,\varphi_0)$ via Witt vectors;
- it uses the complex uniformization $E(\mathbb C)\cong\mathbb C/\Gamma$ with the Frobenius $\xi$ action;
- it forms the $\xi$-adic Tate modules $V_\xi\Gamma=T_\xi\Gamma\otimes\mathbb Q$;
- the actions are by translations ($V$) and by the scale $\Lambda=(\log q)\mathbb Z$.

**[DATA] The existence of the underlying space $X$ is unconditional:** it requires only the structure of the elliptic curve and Hasse's theorem $|\xi|^2=q$ (proved unconditionally for elliptic curves). The space exists independently of "where the zeros are" in the sense that they are already where Hasse places them.

### 2.2. [DATA] The leafwise metric — the one making the space Kähler–Riemann — explicitly invokes Hasse

Here is the fact that decides this document. The metric on the leafwise tangent bundle is
$$
g_{(z,\hat v,t)}(\xi,\eta)=e^{t}\,\mathrm{Re}(\xi\bar\eta),
$$
and the source says, **verbatim**, that this metric is defined *after* invoking Hasse:

> **[Verbatim DATA, math/0204194 via ar5iv]:** *"According to a theorem of Hasse — the Riemann conjecture for elliptic curves over function fields — we have $|\xi|^2=q$."* And: *"The metric $g=e^t\,\mathrm{Re}(\xi\bar\eta)$ is then defined using this established norm. There is no derivation of Hasse from the foliation's conformal structure alone — the conformal structure is built after Hasse is known."* And: *"Hasse is used as input to construct X and its metric ... and to verify $|\xi|^2=q$, which is essential to the H-invariance of the measure $\tilde\mu$. The RH follows from the index computation on this pre-constructed space, not from positivity alone."*

**[DATA] Important nuance about the complex structure (not the metric):** the *leafwise* complex structure $\mathbb C/\Gamma$ is indeed fixed, intrinsic to $E(\mathbb C)$, independent of the argument of $\xi$. That is: the leaves' **complex structure** is external; but the **metric/polarization** (the datum that makes the space Kähler–*Riemann* and controls the $H$-invariance of the measure and the trace-class property of the operator) **uses $|\xi|^2=q$ = Hasse = RH-for-E**.

### 2.3. [ANALYSIS] The carried-out case does NOT inherit Weil's miracle — it inverts the arrow

Surgical comparison with Weil's externality:

| | **Weil (C×C, Castelnuovo–Severi)** | **Deninger-elliptic (math/0204194)** |
|---|---|---|
| The space | $C\times C$, projective surface, pure geometry | sheet $X=\tilde X/H$, pure geometry of the Witt lift |
| The positivity form | Hodge index over $\mathrm{NS}(C\times C)$ | Hodge–Riemann polarization over $\bar H^1_{\mathcal F}$ |
| **How positivity is established** | **THEOREM of surface geometry, proved WITHOUT knowing the Frobenius eigenvalues** (Sylvester + Poincaré duality in $H^2$) | the metric supporting it **is built USING $|\xi|^2=q$ (Hasse)** |
| Direction of the implication | Hodge index (external) $\Rightarrow$ RH-for-C | Hasse (RH-for-E) $\Rightarrow$ build metric $\Rightarrow$ index computation "$\Rightarrow$" RH |
| Genuine externality? | **YES** — positivity does not know where the eigenvalues are | **NO** — positivity is mounted on the already-known localization |

**[ANALYSIS] Witness conclusion.** In Weil, the miracle is that positivity is **prior and unrelated** to the localization of the eigenvalues: $C\times C$ is a surface and its Hodge index holds whatever the curve is. In Deninger-elliptic, the positivity/metric is **posterior and dependent** on the localization ($|\xi|=\sqrt q$ already known by Hasse). The carried-out witness **does not replicate Weil's externality**; it **inverts** it. This is exactly the opposite of what Doc 128 §3.1 asserted ("Deninger's positivity in the Kähler–Riemann case has the same nature [as Castelnuovo]: it holds by the Hodge geometry of the leaves, not by where the zeros are"). Doc 128 **did not read the metric construction**; had it done so, it would have seen that the leafwise metric uses Hasse.

> **[ANALYSIS] The frank objection to my own attack, and its refutation.** *Objection:* "For elliptic curves Hasse is ALREADY a theorem; using it is not circular, because it is proved by another route (geometry of $E\times E$ / Weil). The Kähler–Riemann space of $E$ is legitimately constructible because Hasse is legitimately known. Deninger's construction is then an *after-the-fact repackaging* of an already-proved fact, not a circular proof." — *Response:* correct for elliptic curves, and that is why math/0204194 is a frank "Hello World" (it does not claim to prove Hasse; it illustrates it). **But the adversarial point is the transfer to Spec ℤ:** there, the analogue of Hasse IS RH, which is NOT proved by another route. If the recipe for making the space of Spec ℤ "Kähler–Riemann" replicates the recipe of math/0204194, then it would require as input the analogue of $|\xi|^2=q$ = "the zeros are on $\Re s=1/2$" = **RH itself**. Constructing the Kähler–Riemann space of Spec ℤ would use RH as input. **That is circularity.** The carried-out witness, far from proving non-circularity, exhibits the recipe and the recipe uses RH.

### 2.4. [ANALYSIS] Summary of where ζ enters, with surgical precision

The central question: does ζ enter only in the orbits (external datum, like geodesics), or also in the Kähler structure on which positivity depends? Three-part answer, now grounded in source:

- **(α) In the orbits/lengths $\{\log p\}$:** YES ζ enters, but in an **external and benign** way — like the lengths of closed geodesics of a hyperbolic surface are geometric data. This is "value" in P43's language. It is not the source of circularity. (The obstacle here is one of *existence/spectral rigidity*, Doc 128 §4.2, 1712.04181, not of circularity.)
- **(β) In the leafwise complex structure $J$:** ζ does NOT enter — it is pure differential geometry (Newlander–Nirenberg), both in math/0204111 (abstract) and in math/0204194 (fixed $\mathbb C/\Gamma$). This is what Doc 128 saw correctly.
- **(γ) In the Kähler–Riemann metric/polarization (the one that GIVES positivity):** **YES ζ/RH enters, and here is the circularity.** In the only arithmetic case carried out, the metric $g=e^t\mathrm{Re}(\xi\bar\eta)$ is built using $|\xi|^2=q$ = RH-for-E. The datum that turns the foliation from "Kähler" into "Kähler–**Riemann**" (the bundle-like transverse metric, the $H$-invariance of the measure, the trace-class property) is the one that uses the localization of the eigenvalues.

**[ANALYSIS] The (β) vs (γ) distinction is the key Doc 128 missed.** Doc 128 reasoned "the complex structure is external (β) ⟹ positivity is external". But Hodge–Riemann positivity does not depend only on $J$ (the complex structure); it depends on the **polarization** = $J$ + the **metric/Kähler form** that makes it positive-definite on the primitive part. And that metric (γ) is the one that uses RH. The complex structure alone does not give positivity; it gives a decomposition $H^{1,0}\oplus H^{0,1}$. The *definiteness* (the sign) comes from the metric, and the metric comes from Hasse.

---

## 3. THE POINT OF MAXIMUM SUSPICION — does the space exist without RH? [ANALYSIS]

### 3.1. P43's prediction and where it lands on Deninger's route

**[DATA — P43 main.tex, Principle/Theorem autonomy].** The master quantifier: RH is obtained from an unconditional theorem by inverting a quantifier (average→individual). In operator-theoretic coordinates (Obs. after Thm. autonomy): *"the value is the averaged (trace-like) datum; the inertia is the individual (spectral-resolution) datum. Computing a trace is averaging; resolving a signature is individuating."* The **value** of a quadratic functional is autonomous (computable from the primes); the **inertia** (the partition of the negative index) is NOT (it requires the zero positions).

**[ANALYSIS] Mapping the value→inertia step onto Deninger's route.** P43 predicts that circularity reappears in value→inertia. In Deninger:

- **The "value" = the underlying space + flow + orbits (= primes) + the leafwise cohomology as a graded vector space.** This is external geometry: the orbits $\{\log p\}$ are benign arithmetic data; the cohomology $\bar H^1_{\mathcal F}$ as a space (without polarization) is functorial. The **value** = "which space, with which orbits, which trace" — computable from the primes, external.
- **The "inertia" = the Kähler–Riemann structure = the polarization = the sign of $Q$ on the primitive part.** This is exactly the **signature** $(1,\rho-1)$ / the definite negativity on the primitive part / $m=\kappa(Q)/2=0$. And by §2.2, in the carried-out case **the metric fixing that sign uses $|\xi|=\sqrt q$** = the localization of the eigenvalues = P43's **individual inertia**.

> **[ANALYSIS] The point of maximum suspicion confirmed.** Building the space of Spec ℤ **as a bare object** (space + flow + orbits $\{\log p\}$ + graded cohomology) is plausibly external to RH — it is the "value". But building it **as Kähler–Riemann** (with the metric/polarization from which positivity is derived) IS putting in the "inertia", and the inertia, by P43 + by witness math/0204194, is RH. **The existence of the Kähler–Riemann-space presupposes RH; the existence of the bare-space does not.** Doc 128 said "building the Kähler–Riemann space gives RH without assuming positivity=RH" — but building the space *as Kähler–Riemann* is precisely where the localization is assumed.

### 3.2. [ANALYSIS] Under ¬RH: non-Kähler (good) or non-existent (bad)?

The correct question is the following: under ¬RH (off-line zeros), would the foliated space exist but with NON-Kähler leaves (breaking positivity **without circularity** — the good scenario, Weil-type), or would it simply not exist (hidden circularity — the bad scenario)?

**[ANALYSIS] The witness strongly suggests the bad/intermediate scenario.** Reasoning by analogy with math/0204194:
- If we imitate the recipe, the metric of the Spec ℤ space would be of the type $g\sim e^t\,(\text{form using }|\rho|\text{ or }\Re\rho)$. Under ¬RH, a zero $\rho$ with $\Re\rho\neq1/2$ would give a weight $e^{t}$ with the "wrong" exponent in the corresponding direction.
- **Good scenario (Weil-like):** the underlying space still exists (the orbits $\{\log p\}$ do not change — they are the primes, not the zeros), but the polarization form on $\bar H^1_{\mathcal F}$ stops being positive-definite on the primitive part — a vector of negative norm appears where positivity demanded positivity. This would be **non-circular**: positivity fails *visibly in the structure* without needing to localize the zero, satisfying NC4. **If this occurs, the route is non-circular** and Doc 128 would be right.
- **Bad scenario (circular):** the analogous metric $e^t\mathrm{Re}(\xi\bar\eta)$ CANNOT even be *defined* under ¬RH because its well-definedness (trace class, $H$-invariance of the measure) **requires** $|\xi|^2=q$. Without the analogue of Hasse, the trace operator is not trace-class, the measure is not invariant, and the Kähler–Riemann space **does not exist as such**. Then "building the space" IS "proving RH", and non-circularity is empty.

**[ANALYSIS] Which of the two: the witness evidence points to the bad one, but it is NOT conclusive.** In math/0204194, the source is explicit: $|\xi|^2=q$ is *"essential to the H-invariance of the measure"* and to the trace-class property of the operator $S_j(\alpha)$. That is: in the carried-out case, **without Hasse the Kähler–Riemann space is not well defined** (the measure is not invariant, the trace does not converge). This is the bad scenario. BUT: (i) for elliptic curves Hasse ALWAYS holds, so the case ¬(Hasse) is a vacuous counterfactual — we cannot observe what would happen; (ii) it is conceivable that for Spec ℤ there exists a construction of the space that does NOT copy the recipe of the metric $e^t\mathrm{Re}(\xi\bar\eta)$ and whose well-definedness does not require the localization. **Nobody knows this.** It is the central [GAP].

> **[GAP — the unknown fact about Spec ℤ that decides everything].** Does there exist a construction of the Kähler–Riemann foliated space of Spec ℤ whose well-definedness (invariant measure, trace class, polarization) does NOT require the analogue of $|\xi|^2=q$ (= that the zeros lie on $\Re s=1/2$)? If YES ⟹ non-circular (good scenario). If NO (as in the only witness) ⟹ circular (bad scenario). **Indeterminate with what is known.**

### 3.3. [ANALYSIS] Spectral rigidity (1712.04181) reinforces the bias toward circular

**[DATA — Doc 128 §4.2, 1712.04181].** For suspensions/bundles over $S^1$, the spectrum of the infinitesimal generator is **forced by the monodromy**: $\mathrm{Sp}(\Theta\mid\bar H^i_{\mathcal F})=\{(\log\alpha+2\pi i\nu)/\log r\}$, $\alpha\in\mathrm{Sp}(\phi^*\mid H^i(S))$. The length spectrum is not arbitrary.

**[ANALYSIS] Adversarial reading.** If the generator's spectrum (= the zeros, by Deninger's dictionary D3) is **forced by the geometry/monodromy of the space**, then the geometry of the space **determines where the zeros are**. There are two readings:
- **Optimistic (Doc 128):** rigidity says the space is hard to construct (it is not a suspension), but if constructed, it forces the zeros into place — and if that place is $\Re=1/2$, RH follows from the geometry. Non-circular.
- **Adversarial (this doc):** if the space's geometry FORCES the spectrum into $\{$zeros$\}$ with $\Re=1/2$, then **constructing that specific geometry IS having put in RH**. The question is not "is the spectrum rigid?" but "can the geometry be built without knowing beforehand that the forced spectrum will land on $\Re=1/2$?". If the only geometry that gives the correct spectrum is the one that already places it on the line, it is circular. **Spectral rigidity is neutral to the circularity test by itself** — it cuts both ways — but combined with §2.2 (the metric uses the localization), it tilts toward circular: the geometry that forces the correct spectrum is built using the localization.

---

## 4. IS DENINGER'S POSITIVITY THE SAME AS CONNES–CONSANI'S? [DATA + ANALYSIS]

### 4.1. [DATA] What is established about CC (Doc 124, via Doc 127/119)

**[DATA].** CC's Weil positivity is **spectral**: global Weil positivity = MW-1 = Weil's criterion = RH. It is read by evaluating the Weil form on test functions; that evaluation = the trace of the scaling flow = the explicit formula (Connes 1999). **Circular: FAILS NC3** (it is an item in the catalogue of RH-equivalent positivities) and **NC4** (under ¬RH the binarity of the index is inaccessible without localizing). Doc 127 confirmed it via a fourth route: the scaling flow carries ζ inside.

### 4.2. [ANALYSIS] Concrete test: same form under a dictionary?

The concrete test is needed: both are "positivity of a form associated with the explicit formula"; CC on test functions (spectral), Deninger on leaf cohomology classes (geometric). Same form or different?

**[ANALYSIS] They are genuinely different objects — but the same wall separates them from RH.**

- **Different as objects.** CC's form is a quadratic form on a **space of test functions** $h$, evaluated as $\sum_\rho\hat h(\rho)$ (spectral side) = $\sum_p\dots$ (arithmetic side). Deninger's form is the **Hodge–Riemann polarization** $Q(\xi,J\bar\xi)$ on $\bar H^1_{\mathcal F}$, a space of **leafwise cohomology classes**. There is a dictionary (Doc 128 §2.4: Hodge index over the square ⟺ polarization over the factor) but **not a literal identity**: CC's lives on the *value/trace* axis (computed by evaluating against tests = averaging = the trace), Deninger's lives on the *inertia/signature* axis (it is the sign of a form over a space of classes = individuating the partition).
- **The same wall (P43) separates them from RH, on different axes.** By P43's Obs. after Thm. autonomy: the value is the trace-like (averaged) datum; the inertia is the spectral-resolution (individual) datum. **CC attacks via value/trace** (and fails because the value is autonomous but the trace IS the explicit formula = RH only when evaluating the full criterion — NC3). **Deninger attacks via inertia/signature** (and fails, in the carried-out case, because the structure fixing the sign — the Kähler–Riemann metric — uses the zero localization = the individual inertia). **It is not "the same form renamed"; it is the same master quantifier catching them on their two coordinates.**

> **[ANALYSIS] The precise answer to "are they the same?".** NO, they are not the same form (CC: form on tests, value axis; Deninger: polarization on cohomology, inertia axis). Hence Deninger **is not CC renamed**, and Doc 128 was right that it is a distinct object. BUT: Deninger **does not improve the circularity situation**, because it attacks the side (inertia) that P43 identifies as the NON-autonomous one, and witness math/0204194 shows that the structure giving that inertia uses RH. CC is circular via value/trace (NC3); Deninger is circular (or indeterminate) via inertia/polarization (NC3/NC4 via the metric). **Two distinct circularities, same P43 origin.** This is consistent with P43's central thesis: "a wall in many coordinates".

### 4.3. [ANALYSIS] What DOES separate Deninger from CC (and why it matters)

To be fair to the route: there is ONE real structural difference favorable to Deninger. CC's positivity, **even in principle**, has no geometric mechanism generating it externally — it is verified by evaluating, and evaluating = the explicit formula. Deninger's **has a candidate mechanism** (math/0204111: if the space is Kähler–Riemann, positivity is a theorem). Deninger's problem is not "positivity is the explicit formula" (that is CC); it is "the Kähler–Riemann antecedent uses the localization". **This difference matters:** Deninger's route could become non-circular if a construction of the Kähler–Riemann space of Spec ℤ is exhibited that does not copy the metric-using-Hasse recipe. For CC there is no such escape (the trace IS the explicit formula by construction). That is why Deninger's verdict is INDETERMINATE-with-circular-bias, while CC's is firmly CIRCULAR.

---

## 5. FINAL NC-VERDICT [application of NC1–NC4]

I apply R-NC (Doc 119 §4.3) to the property $P$ = "Hodge–Riemann positivity on $\bar H^1_{\mathcal F}$ of the foliated space of Spec ℤ", from which purity (= RH) is to be deduced.

### 5.1. Clause by clause

- **NC1 (externality of the definition of $P$).** The polarization form $Q(\xi,J\bar\xi)$ is defined with $J,\omega_{\mathcal F}$ geometric; *given the Kähler–Riemann space*, the definition of $P$ does not mention ζ. **PASSES** — but, as in the case of CC (Doc 119 §4.3 end) and of GAP-FOLIATED (Doc 127 §4.3), this is the superficial externality: everything functorial from the site passes NC1. The content is not in NC1.

- **NC2 (overgeneration).** Does $P$ get proved for a class of objects strictly larger than the one encoding ζ, by a uniform method? Theorem math/0204111 **DOES overgenerate**: it holds for EVERY Kähler–Riemann foliation, not only the arithmetic one. **PASSES for the conditional implication.** BUT — and this is the nuance NC2 requires (Doc 119: "$P$ verifiable only for the specific object encoding ζ ⟹ FAILS") — the *hypothesis* "it is Kähler–Riemann" in the carried-out arithmetic case **is only verified** using the specific structure that encodes the eigenvalues (the metric via Hasse, §2.2). The abstract theorem's overgeneration does not transfer to the arithmetic antecedent. **NC2: the framework-theorem PASSES, the arithmetic-antecedent FAILS.** Exact replica of the pattern of Doc 127 §4.3 NC2 (curvature overgenerates on Teichmüller; on the site it only has content over the correspondences of ζ).

- **NC3 (non-reduction to catalogued RH-equivalent positivities).** Is the verification of $P$, restricted to the object encoding ζ, equivalent to an item in the catalogue (MW-1…MW-7, etc.)? In the carried-out case: the property "the space is Kähler–Riemann" uses $|\xi|^2=q$ = the analogue of Hasse = the analogue of "$\Re\rho=1/2$". For Spec ℤ, that is **literally the localization of the zeros** = RH. **FAILS NC3** in the carried-out case: the geometric property $A$ (Kähler–Riemann), restricted to the arithmetic object, uses the position of the zeros. The chain $A\Rightarrow$ purity has $A$ as a link that **is** RH disguised as "well-defined metric".

- **NC4 (two-worlds test).** Under ¬RH, is $P$ false for a reason computable from $H$ without localizing the quadruple? **FAILS / INDETERMINATE.** By §3.2: it is not known whether under ¬RH the space exists non-Kähler (NC4 would pass — visible negative-norm vector) or does not exist (NC4 fails — the metric is not even defined without the analogue of Hasse, and deciding whether it fails requires knowing where the zero is). Witness math/0204194 suggests the second (the $H$-invariance of the measure *requires* $|\xi|^2=q$), which is a NC4 FAILURE. But the counterfactual ¬(Hasse) is vacuous for elliptic curves, so it is not conclusive.

### 5.2. Verdict

> **[NC-VERDICT] INDETERMINATE, with strong bias toward CIRCULAR.**
>
> The conditional implication "Kähler–Riemann space ⟹ positivity" is **genuine geometry, external to ζ** (math/0204111, passes NC1/NC2 as a framework-theorem) — Doc 128 was RIGHT about THAT. But the non-circularity of a *proof route for RH* depends on the **antecedent** "the space of Spec ℤ is Kähler–Riemann", and there:
> - **NC3 FAILS in the only arithmetic witness:** the Kähler–Riemann structure (the metric/polarization) is built USING the analogue of RH (Hasse, $|\xi|^2=q$), which for Spec ℤ is the localization of the zeros.
> - **NC4 FAILS/INDETERMINATE:** it is unknown whether under ¬RH the space exists non-Kähler (non-circular) or does not exist (circular); the witness suggests the latter.
>
> Doc 128 made an inference error: it verified that the **implication** is geometric and concluded that the **route** is non-circular, without attacking the **antecedent**, which is where — confirmed by source this session — RH enters. **Doc 128's verdict (a) is hereby revoked to INDETERMINATE-with-circular-bias.**
>
> This is **better than CC** (firmly CIRCULAR via value/trace, with no escape): Deninger has a candidate geometric mechanism, and circularity could break IF a construction of the space is exhibited that does not copy the metric-via-Hasse recipe. But the standard of proof for "non-circular" is HIGH, and the route does NOT meet it today.

### 5.3. [GAP] The minimal statement to establish to confirm non-circularity

To move the verdict from INDETERMINATE to NON-CIRCULAR, a precise statement must be established, and it is NOT RH nor the full space:

> **MINIMAL-STATEMENT-130 (the fire test of non-circularity for Deninger's route).** *Exhibit a construction of the Kähler–Riemann foliated space (or of an analogous foliated polarization structure) over Spec ℤ — or over Morishita's space $\mathfrak X_F$ (2508.15971), which already gives the underlying space + flow + orbits — whose well-definedness (leafwise complex structure $J$, Kähler form $\omega_{\mathcal F}$, bundle-like transverse metric, $H$-invariance of the measure, trace-class property of the operator) does **NOT require as input the analogue of $|\xi|^2=q$**, i.e. does **not presuppose that the zeros lie on $\Re s=1/2$**. Equivalently: a leafwise metric/polarization defined by pure geometry of the arithmetic solenoid, such that the Hodge–Riemann positivity derived from it is a theorem that holds **whatever the position of the zeros** — so that under ¬RH the space keeps existing but with the polarization failing (visible negative-norm vector, NC4-passes), not with the space ceasing to exist.*

**[ANALYSIS] Why this is the correct fire test.** It exactly replicates the condition that makes Weil non-circular: in $C\times C$, the Hodge index is proved **before** and **without** knowing the Frobenius eigenvalues, and that is why RH is derived. MINIMAL-STATEMENT-130 asks for the same priority: the leafwise polarization must be constructible without the localization. If achieved, NC3 and NC4 pass and the route is genuinely non-circular. If it is proved that **every** construction of the leafwise metric over Spec ℤ requires the analogue of Hasse (as in math/0204194), then the route is firmly CIRCULAR and closes — an equally valuable result (it saves years).

**[ANALYSIS] Frank prediction.** Bias toward it being closed / circular, due to three convergences: (i) the carried-out witness uses Hasse for the metric; (ii) P43 places the inertia (= the polarization) as the NON-autonomous datum; (iii) spectral rigidity (1712.04181) says the geometry forcing the correct spectrum is the one that already places it. But it is NOT conclusive: nobody has proved that every leafwise metric over Spec ℤ must use the localization. The [GAP] is genuine and is the first concrete theorem to attack in Phase 43 — and its negative form ("every foliated polarization over Spec ℤ requires RH as input") would be just as decisive as the positive one.

---

## 6. Synthesis and frankness

**[ANALYSIS] What changed relative to Doc 128.** Doc 128 read the abstract of math/0204111 and the formalism, and concluded (a) non-circular. This document read the **construction of the metric** in the carried-out arithmetic case (math/0204194) and found that **the Kähler–Riemann structure uses the analogue of RH (Hasse) as input**. Doc 128 confused the geometricity of the conditional implication ("Kähler–Riemann ⟹ positivity", true) with the non-circularity of the route (which depends on the antecedent, where RH enters). **Verdict revoked: (a) → INDETERMINATE-with-circular-bias.**

**[ANALYSIS] Where ζ enters, in one sentence.** ζ enters benignly in the orbits $\{\log p\}$ (the value, external) and does NOT enter the leafwise complex structure $J$ (pure geometry); but it enters **fatally in the Kähler–Riemann metric/polarization** (the inertia, the sign) — and it is the metric, not the complex structure, that gives positivity. Doc 128 saw $J$ as external and deduced positivity was external; the leap is invalid.

**[ANALYSIS] Weil's miracle is NOT inherited.** In Weil, positivity (the Hodge index) is prior and unrelated to the eigenvalue localization; in Deninger-carried-out the metric giving positivity is posterior and dependent on it ($|\xi|^2=q$). The arrow is inverted. Deninger's route does not inherit Weil's miracle — it needs it and does not have it over Spec ℤ.

**[ANALYSIS] Same form as CC, no.** Different object (CC: form on tests, value axis; Deninger: polarization on cohomology, inertia axis). But the same master quantifier (P43) separates them from RH on their two coordinates: CC falls via value/trace (NC3), Deninger via inertia/polarization (NC3/NC4 via the Hasse-metric). "A wall in many coordinates."

**[ANALYSIS] The point of maximum suspicion, resolved in its conditional form.** The **bare** space (space + flow + orbits) plausibly exists without RH (it is the value). The **Kähler–Riemann** space (with the polarization from which positivity is derived) plausibly does NOT exist without RH (it is the inertia, and the witness confirms it: without Hasse the measure is not invariant nor does the trace converge). Building the space *as Kähler–Riemann* is where the localization is assumed. Doc 128's "non-circularity" is empty unless the construction of the polarization is separated from the localization — MINIMAL-STATEMENT-130.

**[Final NC-VERDICT]:** **INDETERMINATE with strong bias toward CIRCULAR.** Not (a) non-circular (the Kähler–Riemann antecedent uses RH in the witness). Not firmly CIRCULAR like CC (Deninger has a candidate geometric mechanism and a conceivable escape). The escape is MINIMAL-STATEMENT-130, hard and probably closed, but not proved closed. **The HIGH standard for "non-circular" is NOT met; Doc 128 declared victory prematurely without reading the metric construction.**

No new theorem was proved. Source was **read** (math/0204111 hypotheses of the polarization theorem; math/0204194 construction of the sheet and of the metric $e^t\mathrm{Re}(\xi\bar\eta)$ with Hasse as input) and R-NC was **applied** with adversarial discipline. The decisive finding: the metric that makes Kähler–**Riemann** the only carried-out arithmetic space uses the analogue of RH as input. That, transferred to Spec ℤ, is circularity — unless MINIMAL-STATEMENT-130 is established, which nobody has done.

---

## References

**External source read this session, WebFetch ar5iv):**
- C. Deninger, W. Singhof, *Real polarizable Hodge structures arising from foliations*, arXiv:math/0204111 — the polarization theorem ASSUMES the Kähler–Riemann foliation (leafwise Kähler form $\omega_{\mathcal F}$, bundle-like transverse metric) as given datum, and derives Hodge–Riemann via Álvarez López–Kordyukov + Kähler–Lefschetz identities, **without ζ or spectrum**; pure complex structure $J$ (Newlander–Nirenberg). **[DATA — the conditional implication is geometric.]**
- C. Deninger, *On the nature of the explicit formulas in analytic number theory — a simple example*, arXiv:math/0204194 — 3-dim sheet for elliptic curve $E/\mathbb F_q$; underlying space $X=\tilde X/H$ unconditionally constructible (Witt lift, Tate module); **BUT the leafwise metric $g=e^t\mathrm{Re}(\xi\bar\eta)$ is defined USING Hasse $|\xi|^2=q$**, essential to the $H$-invariance of the measure and to the trace-class property. **[DATA — the Kähler–Riemann structure uses the analogue of RH as input; Weil's miracle is NOT replicated.]**

**Internal (backward-only):** Doc 128 (verdict (a) non-circular, HEREBY REVOKED; the implication "Kähler–Riemann ⟹ positivity"; the Hodge-index⟺polarization dictionary; CORE-128; spectral rigidity 1712.04181; Morishita 2508.15971); Doc 127 (Forni circular, the flow carries ζ inside; GAP-FOLIATED; R-NC on the foliated curvature; the R1/R2 dichotomy); Doc 119 §4.3 (R-NC NC1–NC4 verbatim; the catalogue of RH-equivalent positivities; the gray zone of sufficiency); Doc 124 (CC's positivity = spectral = MW-1 = circular; intersection-positivity [GOOD] vs spectral-positivity [CIRCULAR]); P43 (master quantifier; autonomous value / non-autonomous inertia, Thm. autonomy; "a wall in many coordinates"; Principle boundary: the missing mechanism must read inertia, not value — cohomological over Spec ℤ).

*End of Doc 130.*
