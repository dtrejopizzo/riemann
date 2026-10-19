# Doc 132 — Defect theory: the category 𝒫ol_δ of defective polarized spaces

**Program:** Riemann Hypothesis — Phase 44: NEW MATHEMATICS.
**Role of the document:** constructive-creative. Invert the finding of Doc 130 (Deninger's polarization carries RH inside) following the Fredholm/Pontryagin model: **do not ask for the perfect structure; define the category of objects whose polarization fails, and turn the failure into an invariant with theorems.** RH stops being "the polarized space exists" and becomes "the defect of the ζ-object is 0".

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom, no obligation of precedent. **[THEOREM]/[PROPOSITION]/[LEMMA]** = proved FOR REAL in this document, complete proof, maximum standard; if a step uses an external result, it is cited precisely and what is used is declared. **[BRIDGE]** = connection with ζ/RH, with the frank status of each link (theorem / program conjecture / wish). **[WISH]** = declared without shame, never disguised as a theorem.

**Prerequisites read from source this session:** Doc 130 (the circularity of the Kähler–Riemann route: the metric uses Hasse; MINIMAL-STATEMENT-130: under ¬RH the space must exist with the polarization failing *visibly*); Doc 112 (conditional dichotomy m∈{0,∞}: reduction to LP-112, Prop. 2.6 on zero density, the Rouché + quasi-periods + non-discreteness of {log p} mechanism); Doc 106 §3 (Prop. 3.1: neg.ind(Q₁⊗Q₂)=p₁q₂+q₁p₂; Props. 3.3–3.6: exponential growth and sterility of the abstract tensor); Doc 118 (moment rigidity: Carleman + cone positivity ⟹ the only measure with constant Δₙ is c·m_∞); Doc 125 (intersection form of the square: signature (1,ρ−1) in the toy model; Babaee–Huh: tropical surfaces with the WRONG Hodge-index signature exist).

---

## 0. Executive summary

1. **[NEW-DEFINITION] (§2)** The category **𝒫ol_δ** of *polarized spaces with defect*: objects $(H,Q,P)$ — Hermitian form $Q$ on $H$, marked primitive subspace $P$ — with optional decorations (Weil operator $C$, generator $A$, functional symmetry $S$, real structure $\tau$). The **defect** $\delta(X):=\mathrm{neg.ind}(Q_C|_P)\in\mathbb{N}\cup\{\infty\}$ is *always* defined: it presupposes no perfect existence. $\delta=0$ ⟺ the object is polarized (Hodge–Riemann). The instances: the Pontryagin $(\mathcal K,Q)$ of the program ($\delta=\kappa=2m$, reduced defect $\hat\delta=m$), the intersection form of the square (Doc 125, $\delta$ = excess of positive directions over the primitive), the foliated object of MINIMAL-STATEMENT-130, and — crucially — **Babaee–Huh as proof of population**: in the tropical corner of the category there exist objects with $\delta\geq1$ *in nature*; the category is not an empty name for "polarized or pathological".

2. **[THEOREM A] (§3) Arithmetic of the defect.** $\delta$ is monotone under isometric embeddings, additive under $\oplus$, and under $\otimes$ satisfies the **defect Whitney formula** $\delta(X\otimes Y)=p_1\delta_2+\delta_1 p_2 = d_1\delta_2+d_2\delta_1-2\delta_1\delta_2$ (imported from Doc 106 Prop. 3.1, re-proved). The only additive-multiplicative invariants are the dimension $d$ and the reduced signature $\sigma=p-\delta$ (two characters), and $\delta=(d-\sigma)/2$: **the defect is the difference of the two characters** — in infinite dimension both characters diverge and $\delta$ is what remains: a Fredholm-type invariant, not a character.

3. **[THEOREM B] (§4) Kreĭn rigidity.** (B1) If the Gram operator is invertible, $\delta$ is locally constant under norm deformations (Riesz projections); (B2) $|\delta(Q+R)-\delta(Q)|\leq\mathrm{rank}(R)$; (B3) $\delta$ is lower semicontinuous, and along a continuous path it can only jump at kernel crossings ($0\in\mathrm{spec}\,G_t$); (B4, **Weyl**) if $\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$ — *essential positivity* — then $\delta(G+K)<\infty$ for every compact $K$: **the finiteness of the defect is a Fredholm property**. (B6) The moment rigidity of Doc 118 axiomatized as *cone rigidity*: the separation defect of a criterion is $\dim(\mathrm{Annihilator}\cap\mathrm{Cone})$.

4. **[THEOREM C] (§5) Abstract dichotomy.** If an object has ONE **replicable** negative vector — orbit under a group of $Q$-isometries with unbounded heights and correlation decay $|Q(\gamma v,\gamma'v)|\leq\omega(|h(\gamma)-h(\gamma')|)$, $\omega\to0$ — then $\delta=\infty$. Corollary: in the class of objects where every defect is replicable, $\delta\in\{0,\infty\}$. The proof is Gershgorin on the Gram matrix of the replicas: it turns the Rouché argument of Doc 112 into a category theorem. Approximate version included ($\varepsilon$-isometric replicas suffice).

5. **[THEOREM D] (§6) Parity and classification at low defect.** For spectral objects ($A$ $Q$-symmetric, primitive spectrum of quadruple type $z^2\notin\mathbb R$): the non-real eigenvectors are neutral, the pairs $\{z,\bar z\}$ contribute hyperbolic planes, $\delta=\sum_{\{z,\bar z\}}\dim H[z]$. With the **functional symmetry** $S$ ($SAS^{-1}=-A$) the spectrum comes in quadruples and $\delta$ is **EVEN**: $\delta=1$ is forbidden. Without $S$, the objects with $\delta=1$ are classified: they are exactly the $\Pi_1$-blocks (one hyperbolic plane, unique normal form). The $\kappa=2m$ of P35 is the instance.

6. **[THEOREM E] (§7) The dividend: the tensor flow and the hyperbolic ideal.** The **defect density** $\theta=\delta/d$ composes under $\otimes$ like the bias of a binary symmetric channel: $1-2\theta(X\otimes Y)=(1-2\theta_X)(1-2\theta_Y)$. Complete classification of $\otimes$-stable classes: $\theta=0$ (polarized, tensor subcategory) and $\theta=\tfrac12$ (hyperbolic = Witt-trivial, **absorbing ideal**); everything else flows to $\theta=\tfrac12$ at exact exponential rate $|1-2\theta|^k$. This explains FROM WITHIN the sterility of the tensor (Doc 106 Prop. 3.6) and produces the structural finding for the bridge: **the off-critical part of the ζ-object is hyperbolic (2m,2m), Witt-trivial, $\theta=\tfrac12$: it lives exactly in the absorbing ideal, invisible to every multiplicative invariant.**

7. **[BRIDGE] (§8)** The ζ-object and RH = "$\delta(Z_\zeta)=0$". The program's D-109 architecture is rewritten as the conjunction of the theory's two axes: **RH = (essential positivity: Fredholm axis, B4) ∧ (replicability: symmetry axis, C)**. Total frankness: applied to $Z_\zeta$, the remaining replicability axiom IS LP-112 in disguise — the theory does not prove it; it isolates it as THE axiom, separates the hypotheses already proved (unbounded heights = Lemma 2.2 of D112; cosh anti-models fail where the theory predicts) and shows that the dichotomy only needs data from ONE orbit, with no uniformity. And it reformulates MINIMAL-STATEMENT-130: Deninger's non-circularity ⟺ his construction defines a functor with values in the *total* 𝒫ol_δ (also defined where $\delta>0$), not only on the fiber $\delta=0$.

---

## 1. The creative inversion: from the failure of polarization to the invariant

Doc 130 established (with strong bias) that the "Kähler–Riemann" space of Spec ℤ is not known how to construct without RH: the metric that polarizes uses the localization of the zeros as input. The defensive reaction would be to look for another metric. The **creative** reaction — the Kreĭn lineage — is different:

> When a positive structure does not exist, the right theory is not the one of spaces where it exists, but the one of spaces where it fails *in a measurable way*. Fredholm: non-invertibility becomes the index. Pontryagin: non-positivity becomes $\kappa$. Here: non-polarizability becomes $\delta$.

The design requirement, dictated by MINIMAL-STATEMENT-130: the invariant must be defined **for every object of the relevant type, whether or not the polarization exists** — because the fire test of non-circularity (NC4 of the R-NC test) is precisely that under ¬RH the object exists with the defect *visible*. A category where only perfect objects live cannot even state NC4. 𝒫ol_δ is the receptacle where NC4 is a statement.

Three rigidities from the corpus must be contained as model theorems: the exact arithmetic of the index under products (Doc 106), the dichotomy $m\in\{0,\infty\}$ conditional on a replica lemma (Doc 112), and moment rigidity (Doc 118). All three appear below as Theorems A, C and B6 respectively.

---

## 2. [NEW-DEFINITION] The category 𝒫ol_δ

**Conventions.** Hermitian form = sesquilinear, linear in the first variable, $Q(y,x)=\overline{Q(x,y)}$. For a subspace $W\subseteq H$, $\mathrm{neg.ind}(Q|_W):=\sup\{\dim N: N\subseteq W$ subspace with $Q(x,x)<0\ \forall x\in N\setminus\{0\}\}\in\mathbb{N}\cup\{\infty\}$. Similarly $\mathrm{pos.ind}$.

**Definition 2.1 (object of 𝒫ol_δ).** A *polarized space with defect* is a triple
$$X=(H,\,Q,\,P)$$
where $H$ is a $\mathbb C$-vector space, $Q$ a Hermitian form on $H$ (no non-degeneracy or positivity of anything is required), and $P\subseteq H$ a marked subspace, the **primitive** — the place where the polarization *should* be defined.

**Optional decorations** (each, when present, is part of the object's data and the morphisms respect it):

- **(c)** a *candidate Weil operator* $C\in GL(H)$ with $C^2=\mathrm{id}$, $Q(Cx,Cy)=Q(x,y)$, $CP=P$. It induces the twisted Hermitian form $Q_C(x,y):=Q(Cx,y)$ (Hermitian: $Q_C(y,x)=Q(Cy,x)=\overline{Q(x,Cy)}=\overline{Q(Cx,C^2y)}=\overline{Q_C(x,y)}$). If there is no $C$, take $C=\mathrm{id}$, $Q_C=Q$.
- **(a)** a *generator* $A\in\mathrm{End}(H)$ that is $Q$-symmetric: $Q(Ax,y)=Q(x,Ay)$, $AP\subseteq P$.
- **(s)** a *functional symmetry* $S\in GL(H)$ with $S^2=\mathrm{id}$, $SP=P$, $Q(Sx,Sy)=\epsilon_S\,Q(x,y)$ with $\epsilon_S\in\{+1,-1\}$, and (if there is $A$) $SAS^{-1}=-A$.
- **(r)** a *real structure* $\tau:H\to H$ antilinear, $\tau^2=\mathrm{id}$, $\tau P=P$, $Q(\tau x,\tau y)=Q(y,x)$, and (if there is $A$) $\tau A=A\tau$.

**Definition 2.2 (the defect).**
$$\boxed{\;\delta(X):=\mathrm{neg.ind}\bigl(Q_C|_P\bigr)\;\in\;\mathbb{N}\cup\{\infty\}.\;}$$
When there is also a functional symmetry $S$ and the primitive spectrum is of quadruple type (§6), the **reduced defect** is $\hat\delta(X):=\delta(X)/2$ (an integer by Theorem D).

$\delta$ is defined for EVERY object: it is a supremum of dimensions, it never requires the existence of decompositions, metrics, or completions. The object is **polarized** if $\delta(X)=0$, i.e. $Q_C|_P\geq0$; it is **strictly polarized** if moreover $Q_C|_P$ is definite (the classical Hodge–Riemann bilinear relations).

**Definition 2.3 (morphisms).** $f:X_1\to X_2$ is a linear map $f:H_1\to H_2$ with $Q_2(fx,fy)=Q_1(x,y)$, $f(P_1)\subseteq P_2$, and compatibility with the decorations present ($fC_1=C_2f$, etc.). 𝒫ol_δ has obvious direct sums and tensor products:
$$X_1\oplus X_2=(H_1\oplus H_2,\,Q_1\oplus Q_2,\,P_1\oplus P_2),\qquad
X_1\otimes X_2=(H_1\otimes H_2,\,Q_1\otimes Q_2,\,P_1\otimes P_2),$$
with $(Q_1\otimes Q_2)(u_1\otimes u_2,v_1\otimes v_2)=Q_1(u_1,v_1)Q_2(u_2,v_2)$, $C_{\otimes}=C_1\otimes C_2$. The unit object is $\mathbf 1=(\mathbb C,\,z\bar w,\,\mathbb C)$, with $\delta(\mathbf 1)=0$.

**Definition 2.4 (topological class).** An object is *of Hilbert type* if $H$ is a Hilbert space $(\,\langle\cdot,\cdot\rangle\,)$, $P$ closed, and $Q_C(x,y)=\langle Gx,y\rangle$ with $G=G^*$ bounded (the **Gram operator**). Then (Lemma 4.1) $\delta(X)=\dim\mathrm{ran}\,E_G(-\infty,0)$ on $P$. This class is where the rigidity theorems of §4 live.

### 2.5. The instances (the program's objects ARE objects of 𝒫ol_δ)

**(I1) The program's Pontryagin.** $Z_\zeta:=(\mathcal K,\,Q,\,P_{\mathrm{off}})$, where $(\mathcal K,Q)$ is the space of the program's Weil form with $\kappa(Q)=2m$ (P35: conjectural identification $\kappa=\mathrm{neg.ind}(H_C)$, program V.1–V.4 — status: **program bridge conjecture**, declared), $A=H_C$ (generator of the scaling flow, $Q$-symmetric), $S$ induced by $s\mapsto1-s$, $\tau$ by conjugation, $P_{\mathrm{off}}$ = sum of the radical subspaces with eigenvalue $z=\rho-\tfrac12$, $z^2\notin\mathbb R$. Then $\delta(Z_\zeta)=\kappa=2m$ and $\hat\delta(Z_\zeta)=m$ (Theorem D + P35). **RH ⟺ δ(Z_ζ)=0.**

**(I2) The intersection form of the square (Doc 125).** $X_\square:=(\mathrm{NS}_{\mathbb R}\otimes\mathbb C,\,-Q_{\mathrm{int}},\,H^{\perp})$ with $Q_{\mathrm{int}}$ the intersection form and $H$ an ample class. The Hodge index theorem says $-Q_{\mathrm{int}}|_{H^\perp}>0$; hence $\delta(X_\square)=\mathrm{pos.ind}(Q_{\mathrm{int}}|_{H^\perp})$ = **excess of positive directions** over the primitive. Hodge index ⟺ $\delta(X_\square)=0$. In the toy model $C_p\times C_p$ of Doc 125, $\delta=0$ [CALCULATION from Doc 125, signature $(1,2)$].

**(I3) Babaee–Huh: the category is populated.** [DATA — Doc 125 §5.5, arXiv:1502.00299] There exists a tropical surface whose intersection form does NOT have the signature $(1,\rho-1)$: its object $X_{BH}$ has $\delta(X_{BH})\geq1$. This is decisive for the *legitimacy* of the theory: positive defect **occurs in mathematical nature**, not only in counterfactual ¬RH worlds. 𝒫ol_δ is not the subcategory $\delta=0$ with decoration.

**(I4) The foliated object of MINIMAL-STATEMENT-130.** If the construction requested by Doc 130 §5.3 existed — a foliated polarization over Spec ℤ defined by pure geometry, valid regardless of the position of the zeros — it would define an object $X_{\mathrm{fol}}=(\bar H^1_{\mathcal F},\,Q_{\mathrm{pol}},\,\mathrm{Prim})$ in 𝒫ol_δ with $\delta(X_{\mathrm{fol}})$ computable in both worlds, and NC4 would pass ($\delta\geq1$ visible under ¬RH). Status: **[WISH]** — the object is not constructed; the category is the codomain the wish needs (§8.4).

**(I5) The cosh anti-models (Doc 111/112).** $F=P_1\cdots P_m\cosh(a(s-\tfrac12))$ with $m$ quadruples: analogous Weil form with $\delta=2m$ finite, nonzero, WITHOUT arithmetic. These objects exist in 𝒫ol_δ and the theory must (and will, §5.4) explain why their finite defect does not replicate: their group of symmetries of unbounded height is empty.

**(I6) The classical polarized case.** Every polarized Hodge structure (compact Kähler surface, Castelnuovo–Severi on $C\times C$) is an object with $\delta=0$ proved by geometry external to the spectrum: the "Weil miracle" is, in this language, a **defect-vanishing theorem with external proof**. The whole program seeks the analogue for (I1).

---

## 3. [THEOREM A] The arithmetic of the defect

Throughout §3, objects are finite-dimensional with $Q_C|_P$ **non-degenerate** unless stated otherwise; $d(X):=\dim P$, $(p,\delta)$ = signature of $Q_C|_P$ (Sylvester), $\sigma(X):=p-\delta$ the *reduced signature*. We write $Q$ for $Q_C$ (the twist by $C$ is already absorbed).

**Lemma A.0 (finite-index decomposition; no dimension hypothesis).** Let $Q$ be Hermitian on $W$ with $q:=\mathrm{neg.ind}(Q|_W)<\infty$ and let $N\subseteq W$ be maximal negative ($\dim N=q$). Then $W=N\oplus N^{\perp_Q}$ and $Q\geq0$ on $N^{\perp_Q}$.

*Proof.* $Q|_N$ is negative definite, in particular non-degenerate; hence $W=N\oplus N^{\perp_Q}$ (standard algebra: for $w\in W$, the functional $Q(w,\cdot)|_N$ is represented by a unique $n\in N$, and $w-n\in N^{\perp_Q}$). If there existed $w\in N^{\perp_Q}$ with $Q(w,w)<0$, then $N\oplus\mathbb Cw$ would be negative definite (the Gram matrix is block-diagonal with both blocks negative) of dimension $q+1$, contradicting maximality. $\square$

**Theorem A.1 (monotonicity and additivity).**
(i) If $f:X_1\to X_2$ is a morphism, then $\delta(X_1)\leq\delta(X_2)$. *The defect cannot be erased by an isometric embedding.*
(ii) $\delta(X_1\oplus X_2)=\delta(X_1)+\delta(X_2)$, with no dimension or non-degeneracy hypothesis.

*Proof.* (i) Let $N\subseteq P_1$ be negative. $f|_N$ is injective: $fx=0\Rightarrow Q_1(x,x)=Q_2(fx,fx)=0\Rightarrow x=0$. And $f(N)\subseteq P_2$ is negative because $f$ is isometric. So every witness of $\delta(X_1)$ produces one for $\delta(X_2)$.
(ii) "≥": sum of witnesses. "≤": if some $\delta(X_i)=\infty$ there is nothing to prove. If both finite, by Lemma A.0 write $P_i=N_i\oplus R_i$ with $Q_i\geq0$ on $R_i$, $\dim N_i=\delta(X_i)$. Let $N\subseteq P_1\oplus P_2$ be negative and $\pi:N\to N_1\oplus N_2$ the projection along $R_1\oplus R_2$. $\ker\pi=N\cap(R_1\oplus R_2)$; but $Q_1\oplus Q_2\geq0$ on $R_1\oplus R_2$ and $<0$ on $N\setminus\{0\}$, so $\ker\pi=0$ and $\dim N\leq\delta(X_1)+\delta(X_2)$. $\square$

**Theorem A.2 (defect Whitney formula; Doc 106 Prop. 3.1, re-proved).** For $X_1,X_2$ finite-dimensional with non-degenerate forms of signatures $(p_1,\delta_1)$, $(p_2,\delta_2)$:
$$\mathrm{sig}\bigl(Q_1\otimes Q_2|_{P_1\otimes P_2}\bigr)=(p_1p_2+\delta_1\delta_2,\;p_1\delta_2+\delta_1p_2),
\qquad\text{in particular}\qquad
\boxed{\;\delta(X_1\otimes X_2)=p_1\delta_2+\delta_1p_2.\;}$$

*Proof.* $Q_i$-orthonormal bases $\{e^{(i)}_a\}$ with signs $\varepsilon^{(i)}_a\in\{\pm1\}$ (Sylvester). The basis $\{e^{(1)}_a\otimes e^{(2)}_b\}$ is $Q_1\otimes Q_2$-orthogonal with signs $\varepsilon^{(1)}_a\varepsilon^{(2)}_b$; the sign is $-1$ exactly when the factors differ: $p_1\delta_2+\delta_1p_2$ pairs. Non-degeneracy: orthogonal basis with no isotropic vectors. $\square$

**Corollary A.3 (equivalent forms and consequences).** With $d_i=p_i+\delta_i$, $\sigma_i=p_i-\delta_i$:
(i) **inclusion-exclusion:** $\delta(X_1\otimes X_2)=d_1\delta_2+d_2\delta_1-2\delta_1\delta_2$;
(ii) **two characters:** $d(X_1\otimes X_2)=d_1d_2$ and $\sigma(X_1\otimes X_2)=\sigma_1\sigma_2$; and $\delta=(d-\sigma)/2$;
(iii) **strict super-additivity:** $\delta(X_1\otimes X_2)-(\delta_1+\delta_2)=(p_1-1)\delta_2+(p_2-1)\delta_1\geq0$, strict as soon as one factor has $p\geq2$ and the other $\delta\geq1$;
(iv) **powers:** $\delta(X^{\otimes k})=\tfrac{(p+\delta)^k-(p-\delta)^k}{2}=\tfrac{d^k-\sigma^k}{2}$;
(v) **stability of polarization:** $\delta_1=\delta_2=0\Rightarrow\delta(X_1\otimes X_2)=0$; conversely, if $p_1,p_2\geq1$ and $\delta(X_1\otimes X_2)=0$, then $\delta_1=\delta_2=0$. *Polarized objects form a tensor subcategory, and the defect cannot hide in a product.*

*Proof.* (i)–(iv): direct calculation from A.2 ($\sigma$ multiplicative: $\sigma_{\otimes}=(p_1p_2+\delta_1\delta_2)-(p_1\delta_2+\delta_1p_2)=(p_1-\delta_1)(p_2-\delta_2)$). (v): if $\delta_{\otimes}=p_1\delta_2+\delta_1p_2=0$ with $p_i\geq1$, each summand is zero. $\square$

**Proposition A.4 (the two characters are the only ones; the defect is not a character).** Let $\varphi$ be an isomorphism invariant of finite-dimensional non-degenerate objects, with values in an integral domain of characteristic 0, additive under $\oplus$, multiplicative under $\otimes$, with $\varphi(\mathbf 1)=1$. Then $\varphi=d$ or $\varphi=\sigma$. In particular $\delta$ is not multiplicative, and is half the difference of the two unique characters.

*Proof.* The semiring of isomorphism classes is $\mathbb N^2$ via $(p,\delta)$, with the product of A.2; its Grothendieck ring is $\mathbb Z[\varepsilon]/(\varepsilon^2-1)$ identifying the class of $X$ with $p+\delta\varepsilon$ (check: $(p_1+\delta_1\varepsilon)(p_2+\delta_2\varepsilon)=(p_1p_2+\delta_1\delta_2)+(p_1\delta_2+\delta_1p_2)\varepsilon$ ✓). A ring homomorphism $\varphi$ to an integral domain is determined by $u:=\varphi(\varepsilon)$, which satisfies $u^2=1$, so $u=\pm1$ (integral domain). $u=1$ gives $d$; $u=-1$ gives $\sigma$. $\square$

**Corollary A.5 (infinite dimension: the defect is Fredholm, not a character; Doc 106 Prop. 3.4 as an instance).** If $p(X)=\infty$ and $\delta(X)\geq1$, then $\delta(X\otimes X)=\infty$. *Proof.* With $v_-$ negative and $\{e_n\}\subseteq P$ positive orthonormal, the $e_n\otimes v_-$ are orthogonal of square $-1$. $\square$
Reading: in infinite dimension the two characters $d,\sigma$ diverge and the formula $\delta=(d-\sigma)/2$ loses meaning; what survives is §4: $\delta$ as the dimension of a negative spectral subspace, stable under perturbations — exactly the format of the Fredholm index. **The defect is to polarization what the index is to invertibility.**

**Proposition A.6 (dual and conjugate).** For $X$ finite-dimensional non-degenerate: $\delta(X^*)=\delta(X)$ and $\delta(\bar X)=\delta(X)$, where $X^*=(H^*,Q^*,P^{*})$ with $Q^*(\varphi_x,\varphi_y):=Q(y,x)$ via the anti-isomorphism $y\mapsto\varphi_y=Q(\cdot,y)$, and $\bar X$ the conjugate with $\bar Q(x,y):=Q(y,x)$.

*Proof.* In an orthonormal basis of signs $\varepsilon_a$, $Q^*(\varphi_{e_a},\varphi_{e_a})=Q(e_a,e_a)=\varepsilon_a$ and $\bar Q(e_a,e_a)=\varepsilon_a$: same signatures. $\square$

---

## 4. [THEOREM B] Rigidity: when the defect does not move

Objects of Hilbert type (Def. 2.4): $Q(x,y)=\langle Gx,y\rangle$ on $P$ (we write $H$ for $P$ to lighten notation), $G=G^*\in\mathcal B(H)$.

**Lemma 4.1 (the defect is spectral).** $\delta=\dim\mathrm{ran}\,E_G(-\infty,0)$, where $E_G$ is the spectral measure of $G$.

*Proof.* On $N_-:=\mathrm{ran}\,E_G(-\infty,0)$: $\langle Gx,x\rangle=\int_{(-\infty,0)}\lambda\,d\|E_\lambda x\|^2<0$ for $x\neq0$: $N_-$ is negative, so $\delta\geq\dim N_-$. Conversely, if $N$ is negative, $E_G(-\infty,0)|_N$ is injective: if $E_G(-\infty,0)x=0$ then $x\in\mathrm{ran}\,E_G[0,\infty)$ and $\langle Gx,x\rangle\geq0$, impossible on $N\setminus\{0\}$. So $\dim N\leq\dim N_-$. $\square$

**Theorem B.1 (Riesz stability: the defect is locally constant in the non-degenerate regime).** Let $G$ be invertible, $g:=\mathrm{dist}(0,\mathrm{spec}\,G)>0$. Then for every $G'=G'^*$ with $\|G'-G\|<g$: $G'$ is invertible and $\delta(G')=\delta(G)$.

*Proof.* For $|\lambda|<g-\|G'-G\|$, $G'-\lambda=(G-\lambda)\bigl(1+(G-\lambda)^{-1}(G'-G)\bigr)$ is invertible since $\|(G-\lambda)^{-1}\|\leq(g-|\lambda|)^{-1}$ and $\|(G-\lambda)^{-1}(G'-G)\|<1$: the spectral gap around $0$ persists, of width $\geq g':=g-\|G'-G\|$ along the whole segment $G_t:=G+t(G'-G)$, $t\in[0,1]$, with $M:=\sup_t\|G_t\|\leq\|G\|+g$. Let $\Gamma$ be the boundary of the rectangle $\{-M-1\leq\mathrm{Re}\,z\leq-g'/2,\ |\mathrm{Im}\,z|\leq M+1\}$: $\Gamma$ encloses $\mathrm{spec}(G_t)\cap(-\infty,0)$ and is at distance $\geq\rho:=\min(g'/2,1)$ from $\mathrm{spec}(G_t)$ for every $t$ (the spectrum is real and avoids $(-g',g')$). By Riesz functional calculus, $E_t:=E_{G_t}(-\infty,0)=\frac{1}{2\pi i}\oint_\Gamma(z-G_t)^{-1}dz$, and by the resolvent identity
$$\|E_t-E_s\|\leq\frac{|\Gamma|}{2\pi}\,\rho^{-2}\,\|G_t-G_s\|.$$
Partitioning $[0,1]$ into steps with $\|E_t-E_s\|<1$, it suffices to use the classical lemma: if $P,Q$ are orthogonal projections with $\|P-Q\|<1$ then $\dim\mathrm{ran}\,P=\dim\mathrm{ran}\,Q$ ($P|_{\mathrm{ran}\,Q}$ is injective: $x\in\mathrm{ran}\,Q$, $Px=0\Rightarrow\|x\|=\|(Q-P)x\|<\|x\|$; and symmetrically). With Lemma 4.1, $\delta(G_t)$ is constant. $\square$

**Theorem B.2 (finite-rank perturbation).** For $R=R^*$ of rank $r<\infty$: $|\delta(G+R)-\delta(G)|\leq r$ (with the convention $\infty-n=\infty$: if one side is infinite, so is the other).

*Proof.* Let $N$ be negative for $G+R$ with $\dim N=n$ (any $n\leq\delta(G+R)$). On $N\cap\ker R$ (codimension $\leq r$ in $N$, since $\ker R=(\mathrm{ran}\,R)^\perp$ has codimension $r$): $\langle Gx,x\rangle=\langle(G+R)x,x\rangle<0$. So $\delta(G)\geq n-r$, i.e. $\delta(G)\geq\delta(G+R)-r$. Swapping $G\leftrightarrow G+R$ (with $-R$) gives the other inequality. $\square$

**Theorem B.3 (semicontinuity and localization of jumps).** (i) $\delta$ is lower semicontinuous in norm: if $\delta(G)\geq n$, there exists $\varepsilon>0$ such that $\delta(G')\geq n$ for $\|G'-G\|<\varepsilon$. (ii) Along a norm-continuous path $t\mapsto G_t$, the function $t\mapsto\delta(G_t)$ is constant on each subinterval where $G_t$ is invertible; **it can only change at kernel crossings** $\{t:0\in\mathrm{spec}\,G_t\}$.

*Proof.* (i) Take $N$ negative, $\dim N=n<\infty$; by compactness of the unit sphere of $N$, $\langle Gx,x\rangle\leq-c\|x\|^2$ on $N$ for some $c>0$; any $\|G'-G\|<c$ keeps $N$ negative. (ii) Immediate from B.1 plus connectedness. $\square$

**Theorem B.4 (Weyl: finiteness of the defect is Fredholm).** If $\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$ (**essential positivity**: $G$ positive modulo compacts with gap), then $\delta(G)<\infty$; and for every self-adjoint compact $K$, $\delta(G+K)<\infty$.

*Proof.* If $\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$, then $\mathrm{spec}(G)\cap(-\infty,0]$ consists of isolated eigenvalues of finite multiplicity; their only possible accumulation points would belong to $\mathrm{spec}_{\mathrm{ess}}(G)$, which is disjoint from $(-\infty,0]$; since that set is also compact (bounded spectrum) and discrete, it is finite, and each contributes finite multiplicity: $\dim\mathrm{ran}\,E_G(-\infty,0)<\infty$, i.e. $\delta(G)<\infty$ (Lemma 4.1). By Weyl's theorem on the invariance of the essential spectrum under compact perturbations [Kato, *Perturbation Theory*, Thm. IV.5.35; Reed–Simon IV, §XIII.4], $\mathrm{spec}_{\mathrm{ess}}(G+K)=\mathrm{spec}_{\mathrm{ess}}(G)\subseteq(0,\infty)$, and the above applies to $G+K$. $\square$

**Remark 4.2 (the lineage phrase, now a theorem).** B.4 states exactly: *finite defect = compact failure of positivity*. Essential positivity is "polarization modulo compacts"; the defect is the dimension of the subspace where the failure is realized. It is the literal translation of the Fredholm scheme (invertibility modulo compacts ⟹ finite index) into polarization. Note the delimiting counterexample: $G=\mathrm{diag}(-1/n)$ has $\mathrm{spec}_{\mathrm{ess}}=\{0\}\subseteq[0,\infty)$ but $\delta=\infty$ — the essential gap ($0\notin\mathrm{spec}_{\mathrm{ess}}$) is not decorative.

**Proposition B.5 (which deformations do NOT move the defect — synthesis).** $\delta$ is invariant under: (a) isomorphisms of 𝒫ol_δ; (b) continuous deformations in the non-degenerate regime (B.1, B.3); (c) finite-rank perturbations, modulo error $\leq r$ (B.2); and the *finiteness class* $\{\delta<\infty\}$ is invariant under compact perturbations in the presence of an essential gap (B.4). $\delta$ can only jump at kernel crossings, and the jump at a kernel crossing of dimension $k$ is $\leq k$ (B.2 applied to the spectral range that crosses, when finite). $\square$ (recombination of B.1–B.4).

**Proposition B.6 (cone rigidity: the skeleton of Doc 118, axiomatized).** Let $V$ be a real vector space, $\mathcal C\subseteq V$ a salient convex cone ($\mathcal C\cap-\mathcal C=\{0\}$), $\Phi=\{\varphi_n\}_{n\in\mathbb N}\subseteq V^{\vee}$ a family of functionals ("the criterion"), $M:=\bigcap_n\ker\varphi_n$. We define the **separation defect** $\mathrm{sep}(\Phi,\mathcal C):=\dim\,\mathrm{span}(M\cap\mathcal C)$. Then:
(i) the criterion "$x\in\mathcal C,\ \varphi_n(x)=0\ \forall n\Rightarrow x=0$" holds ⟺ $\mathrm{sep}(\Phi,\mathcal C)=0$;
(ii) if $M\cap\mathcal C=\mathbb R_{\geq0}\,e$ with $e\neq0$ (separation defect 1), it suffices to add ONE functional $\psi$ with $\psi(e)\neq0$: for every $x\in\mathcal C$ with $\varphi_n(x)=0\ \forall n$ and $\psi(x)=0$ one concludes $x=0$. Indeed, $x\in M\cap\mathcal C=\mathbb R_{\geq0}e$ gives $x=ce$ with $c\geq0$, and $0=\psi(x)=c\,\psi(e)\Rightarrow c=0$.

*Proof.* (i) is a restatement. (ii) is contained in the statement. $\square$

**Remark 4.3 (the dictionary with Doc 118 — the model rigidity theorem).** In Doc 118: $V$ = even signed measures with finite moments, $\mathcal C$ = positive measures, $\varphi_n=\nu\mapsto\int\kappa_n\,d\nu$, and the central computation (Thm. 5.3, via Carleman with the exact $a_n^\infty$) is exactly "$M\cap\mathcal C=\mathbb R_{\geq0}\,m_\infty$": separation defect 1, eliminated by the Hardy functional ($\tilde g(\gamma_*)=0$). The structural lesson the theory adopts: **a useful rigidity does not require a trivial annihilator; it requires an annihilator-within-the-cone of known finite dimension, plus one external functional per dimension.** The role of positivity ($d\nu\geq0$, Doc 83) is to be membership in $\mathcal C$: without a cone there is no rigidity (moment problems are not rigid for signed measures — Doc 118 Obs. 5.4). In 𝒫ol_δ, that cone is the operative substitute for the lost polarization.

---

## 5. [THEOREM C] The abstract dichotomy: replicable defect ⟹ infinite defect

This section turns the Rouché proof of Doc 112 (Theorem 2.3) into a category theorem. The structure used by Doc 112, distilled: (1) an off-critical zero gives a negative vector *localized in a compact window of heights*; (2) a quasi-period $\tau$ transports the window to height $+\tau$ producing a *new* negative vector; (3) distant windows correlate weakly. We abstract (1)–(3) without mentioning ζ.

**Definition 5.1 (replicable vector).** Let $X=(H,Q,P)$ be an object. A vector $v\in P$ with $Q(v,v)=-c<0$ is **replicable** if there exist:
- a subgroup $\Gamma\subseteq\mathrm{Aut}(X)$ (automorphisms = bijective $Q$-isometries preserving $P$ and the decorations),
- a **height** homomorphism $h:\Gamma\to(\mathbb R,+)$ with **unbounded** image,
- a **correlation decay** modulus $\omega:[0,\infty)\to[0,\infty)$, non-increasing, $\omega(t)\to0$ as $t\to\infty$,

such that for all $\gamma,\gamma'\in\Gamma$ with $h(\gamma)\neq h(\gamma')$:
$$\bigl|Q(\gamma v,\,\gamma' v)\bigr|\;\leq\;\omega\bigl(|h(\gamma)-h(\gamma')|\bigr).$$

(Interpretation: $h(\gamma)$ is the displacement of the window; $\omega$ measures how much two replicas at separated windows "see" each other. NOTHING is required about the action of $\Gamma$ outside the orbit of $v$: the dichotomy is a phenomenon of ONE orbit.)

**Theorem C.1 (replication ⟹ infinite defect).** If $X$ has a replicable negative vector in $P$, then $\delta(X)=\infty$.

*Proof.* Fix $n\in\mathbb N$; I produce a negative subspace of dimension $n$ inside $P$. Since $\omega(t)\to0$, there exists $T_n$ with $\omega(T_n)<\dfrac{c}{2n}$. Since $h(\Gamma)$ is an unbounded subgroup of $\mathbb R$, there exists $\gamma\in\Gamma$ with $|h(\gamma)|\geq T_n$; replacing $\gamma$ by $\gamma^{-1}$ if necessary, $h(\gamma)\geq T_n$. Define $v_j:=\gamma^j v\in P$, $j=1,\dots,n$ ($\gamma^j\in\Gamma$, $h(\gamma^j)=jh(\gamma)$). The Gram matrix $A=(A_{jk})$, $A_{jk}:=Q(v_j,v_k)$, is Hermitian and satisfies:
- $A_{jj}=Q(\gamma^jv,\gamma^jv)=Q(v,v)=-c$ ($\gamma^j$ is a $Q$-isometry);
- for $j\neq k$: $|A_{jk}|\leq\omega(|j-k|\,h(\gamma))\leq\omega(h(\gamma))\leq\omega(T_n)<\dfrac{c}{2n}$ ($\omega$ non-increasing).

Off-diagonal row sums: $\sum_{k\neq j}|A_{jk}|<(n-1)\dfrac{c}{2n}<\dfrac c2$. By the Gershgorin disc theorem applied to the Hermitian matrix $A$ (real eigenvalues), every eigenvalue lies in $\bigcup_j\,[\,-c-\tfrac c2,\;-c+\tfrac c2\,]\subseteq(-\infty,-\tfrac c2]$: $A$ is negative definite. Consequently: (a) the $v_j$ are linearly independent (if $\sum\xi_jv_j=0$ with $\xi\neq0$, then $0=Q(\sum\xi_jv_j,\sum\xi_kv_k)=\xi^{\!*}\!A\,\xi<0$, absurd); (b) on $N_n:=\mathrm{span}\{v_1,\dots,v_n\}\subseteq P$, $Q(x,x)=\xi^*A\xi<0$ for $x\neq0$. So $\delta(X)\geq n$ for every $n$. $\square$

**Corollary C.2 (dichotomy).** Let $\mathcal R$ be the class of objects $X$ with the property: *if $\delta(X)\geq1$, then some negative vector of $P$ is replicable* (Axiom R). Then for every $X\in\mathcal R$:
$$\delta(X)\in\{0,\infty\}.$$
$\square$ (C.1 plus the definition.)

**Theorem C.3 (approximate version: imperfect replicas suffice).** Let $v\in P$, $Q(v,v)=-c<0$. Suppose that for each $n$ there exist vectors $u_1,\dots,u_n\in P$ (not required to come from isometries) with
$$\bigl|Q(u_j,u_k)-(-c)\,\delta_{jk}\bigr|\;\leq\;\frac{c}{2n}\qquad(1\leq j,k\leq n).$$
Then $\delta(X)=\infty$.

*Proof.* The Gram matrix is $-cI+E$ with $\|E\|_{\text{rows}}<\tfrac c2+\tfrac{c}{2n}\cdot$… let us be precise: $|E_{jk}|\leq\tfrac{c}{2n}$ for all $j,k$ (including the diagonal), so each row sum of $|E|$ is $\leq n\cdot\tfrac{c}{2n}=\tfrac c2$; Gershgorin gives eigenvalues $\leq-c+\tfrac c2<0$. Conclude as in C.1. $\square$

**Remark 5.2 (what quantifier C.3 asks for — structural frankness).** C.3 asks, for each $n$, for $n$ replicas with error $O(c/n)$ in the cross products. It is a $\Pi_2$ statement over the family of replicas — exactly the shape of LP-112 (a sequence $\tau_k$ of increasing quality). The theory does NOT dodge P43's master quantifier; what it does is (i) reduce it to data from ONE orbit (no uniformity over configurations: compare with Doc 112 §2.6, "finiteness protects the internal arguments"), and (ii) separate the three hypotheses of Def. 5.1, which have VERY different status on the ζ-object (§8.3).

### 5.4. Model checks (mandatory)

**(M1) Doc 112 is the instance.** Dictionary: $v$ = the negative vector associated with the hypothetical off-critical quadruple (via P35, the eigenvector-pair in $\mathcal K_{\mathrm{off}}$; in D112's analytic coordinate, the zero $\rho_0$ seen in its window $D(\rho_0,r)$); $\Gamma$ = the (desired) group of pointwise quasi-periods acting by vertical translation $s\mapsto s+i\tau$; $h(\gamma)=\tau$; the unboundedness of $h(\Gamma)$ = "sequence $\tau_k\to\infty$"; the decay $\omega$ = decay of the correlation of the Weil form between separated spectral windows (in the CCM model, the kernel $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Doc 98/95, decays amply). Theorem 2.3 of D112 ("LP-112 ⟹ m∈{0,∞}") is C.2 read through that dictionary: LP-112 is the analytic form of Axiom R for the ζ-object. The gain of the abstraction: C.1 shows that the mechanism does NOT use Rouché, nor holomorphy, nor anything about ζ — it uses isometry + unbounded heights + decay. Rouché was, in D112, the *certificate* that the quasi-period produces a genuine replica; in the category, that certificate is the isometry axiom.

**(M2) The cosh anti-models fail where they should.** The objects (I5) have $\delta=2m$ finite and nonzero; by C.2 they CANNOT be in $\mathcal R$. Independent verification: Lemma 3.2 of Doc 112 proves that the cosh class admits NO self-approximation sequence ($|F(s+i\tau)|\to\infty$ in the disc): the group of symmetries of unbounded height required by Def. 5.1 does not exist for them — their available $\Gamma$ is trivial (or of bounded height). The theory correctly predicts in which class the finite-defect counterexamples live: **in the class with no symmetries of unbounded height.** And the exact periodicity of $\cosh$ does not help: its period translations do not preserve the polynomial factor $P_1\cdots P_m$ (they are not automorphisms of the full object), an abstract reflection of the fact from D112 §3.2 (a discrete group of exact periods maps the zeros onto themselves and multiplies nothing — in our version: if the replicas are not *new*, the Gram matrix is not that of C.1; the novelty is guaranteed by $h(\gamma)\neq0$ together with decay, which forces $Q(v,\gamma v)\approx0\neq-c$, i.e. $\gamma v\not\sim v$).

**(M3) Consistency with Davenport–Heilbronn.** DH (no Euler product, with functional equation) realized $m=\infty$ [DH36, via D112 §3.3]: consistent with DH having the quasi-periodicity of its Dirichlet series (the hypotheses of C.1 plausibly hold for its object, and the conclusion $\delta=\infty$ is the one observed). No known member of the "Dirichlet series + functional equation" class has finite nonzero $\delta$ — the pattern $\delta\in\{0,\infty\}$ has no counterexample in that class (GAP of D111 Obs. 2.4, still open, now with a categorical statement).

---

## 6. [THEOREM D] Parity and classification at low defect

Spectral objects: $X=(H,Q,P)$ with generator $A$ ($Q$-symmetric: $Q(Ax,y)=Q(x,Ay)$), where $P$ is the (algebraic) sum of finite-dimensional radical subspaces $H[z]:=\bigcup_m\ker(A-z)^m$, with eigenvalues $z$ such that $z^2\notin\mathbb R$ (equivalent: $z\notin\mathbb R\cup i\mathbb R$), and $Q|_P$ non-degenerate.

**Lemma D.1 (radical orthogonality).** If $u\in\ker(A-z)^p$, $v\in\ker(A-w)^q$ and $w\neq\bar z$, then $Q(u,v)=0$.

*Proof.* Induction on $p+q$. If $p+q=2$ ($u,v$ eigenvectors): $zQ(u,v)=Q(Au,v)=Q(u,Av)=\overline{w}\,Q(u,v)$ (sesquilinearity in the second variable: $Q(u,wv)=\bar wQ(u,v)$), and $z\neq\bar w$ forces $Q(u,v)=0$. Step: let $u':=(A-z)u\in\ker(A-z)^{p-1}$, $v':=(A-w)v\in\ker(A-w)^{q-1}$. Then
$$Q(u',v)+zQ(u,v)=Q(Au,v)=Q(u,Av)=Q(u,v')+\bar wQ(u,v),$$
i.e. $(z-\bar w)Q(u,v)=Q(u,v')-Q(u',v)=0-0$ by the induction hypothesis (both pairs have sum of exponents $p+q-1$). Since $z\neq\bar w$, $Q(u,v)=0$. $\square$

**Lemma D.2 (isotropy and hyperbolic pairing).** For non-real $z$: $H[z]$ is totally isotropic; if moreover $Q$ is non-degenerate on $H[z]\oplus H[\bar z]$ (it is, by D.1 and global non-degeneracy on $P$), then $\dim H[z]=\dim H[\bar z]=:d_z$ and
$$\mathrm{sig}\bigl(Q|_{H[z]\oplus H[\bar z]}\bigr)=(d_z,\,d_z).$$

*Proof.* Isotropy: D.1 with $w=z$ (and $z\neq\bar z$). Pairing: since $H[z]$ is isotropic and $Q$ is non-degenerate on the sum, the map $H[\bar z]\to H[z]^*$, $v\mapsto Q(\cdot,v)|_{H[z]}$, is injective (a $v$ in its kernel would be $Q$-orthogonal to $H[z]$, to $H[\bar z]$ by isotropy, and to everything else by D.1: $v=0$), and symmetrically: $\dim H[z]=\dim H[\bar z]$. Choosing dual bases, the Gram matrix on $H[z]\oplus H[\bar z]$ is $\begin{pmatrix}0&B\\B^*&0\end{pmatrix}$ with $B\in GL_{d_z}$. By singular value decomposition $B=U\Sigma V^*$ ($\Sigma>0$ diagonal), the matrix is unitarily congruent to $\begin{pmatrix}0&\Sigma\\\Sigma&0\end{pmatrix}$, a direct sum of blocks $\begin{pmatrix}0&\sigma_i\\\sigma_i&0\end{pmatrix}$ with eigenvalues $\pm\sigma_i$: signature $(d_z,d_z)$. $\square$

**Theorem D.3 (structure and exact value of the spectral defect).** For $X$ spectral as above:
$$\delta(X)\;=\;\sum_{\substack{\text{pairs }\{z,\bar z\}\subseteq\mathrm{spec}(A|_P)\\ \mathrm{Im}\,z>0}} d_z.$$

*Proof.* By D.1, $P=\bigoplus_{\{z,\bar z\}}\bigl(H[z]\oplus H[\bar z]\bigr)$ is a $Q$-orthogonal decomposition; by additivity (Theorem A.1(ii)) and D.2, $\delta(X)=\sum d_z$. $\square$

**Theorem D.4 (parity: functional symmetry forces even defect).** If $X$ also has a functional symmetry $S$ ($S^2=\mathrm{id}$, $SAS^{-1}=-A$, $Q(Sx,Sy)=\epsilon_SQ(x,y)$, $SP=P$), then for each $z$: $S\,H[z]=H[-z]$, the pairs $\{z,\bar z\}$ and $\{-z,-\bar z\}$ are disjoint (since $z^2\notin\mathbb R$ ⟹ $\bar z\neq-z$ and $z\neq-z$), $d_z=d_{-z}$, and so the primitive spectrum organizes into **quadruples** $\{z,\bar z,-z,-\bar z\}$ with
$$\delta(X)\;=\;2\sum_{\substack{\text{quadruples}\\ \mathrm{Im}\,z>0,\ \mathrm{Re}\,z>0}}d_z\;\in\;2\mathbb N\cup\{\infty\}.$$
**In particular $\delta(X)=1$ is impossible**, and the reduced defect $\hat\delta=\delta/2$ is an integer: the number of quadruples counted with multiplicity.

*Proof.* $A(Sx)=-SAx=-zSx$ for $x\in\ker(A-z)$, and inductively $S\ker(A-z)^m=\ker(A+z)^m$: $SH[z]=H[-z]$, bijective ($S^2=1$), so $d_z=d_{-z}$. The four numbers $z,\bar z,-z,-\bar z$ are distinct: $z\neq\bar z$ ($z\notin\mathbb R$), $z\neq-z$ ($z\neq0$), $z\neq-\bar z$ ($z\notin i\mathbb R$). D.3 sums $d_z$ over conjugate pairs; the two pairs of each quadruple contribute $d_z+d_{-z}=2d_z$. $\square$

**Theorem D.5 (classification at defect 1, without functional symmetry).** The spectral objects with $\delta(X)=1$ are, up to isomorphism of 𝒫ol_δ, exactly the
$$\Pi_1(z):\qquad H=P=\mathbb Cu\oplus\mathbb C\bar u,\quad A=\mathrm{diag}(z,\bar z),\quad
Q=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad z\in\mathbb C,\ z^2\notin\mathbb R,\ \mathrm{Im}\,z>0,$$
and $\Pi_1(z)\cong\Pi_1(z')$ ⟺ $z=z'$. That is: the minimal defect has a rigid normal form — a single hyperbolic plane with a single simple spectral pair.

*Proof.* By D.3, $\delta=1$ forces a unique pair $\{z,\bar z\}$ with $d_z=1$ and no other primitive spectrum. $H[z]=\mathbb Cu_0$, $H[\bar z]=\mathbb Cv_0$, $Q(u_0,u_0)=Q(v_0,v_0)=0$, $b:=Q(u_0,v_0)\neq0$. Moreover $A$ is semisimple on each (dimension 1). Rescaling $v_0\mapsto v_0/\bar b$ achieves $Q(u_0,v_0)=1$ without touching $A$. Any isomorphism must preserve $\mathrm{spec}(A|_P)=\{z,\bar z\}$ with $\mathrm{Im}\,z>0$ fixing the label: $z$ is invariant. Conversely, the $\Pi_1(z)$ realize $\delta=1$ (D.2). $\square$

**Remark 6.1 (reading for the program).** D.4 answers "what symmetry forbids $\delta=1$?": **anti-commutation with the generator** — the abstract shadow of the functional equation $s\mapsto1-s$. P35's $\kappa=2m$ stops being a model computation and becomes a category theorem: *every* spectral object with functional symmetry has even defect. Combined with C.2: in the class $\mathcal R\cap\{\text{spectral with }S\}$, $\delta\in\{0,\infty\}$, and outside $\mathcal R$, $\delta\in2\mathbb N\cup\{\infty\}$ — the cosh anti-models occupy exactly the stratum $2\mathbb N\setminus\{0\}$ allowed by D.4 and forbidden by Axiom R. The stratification is coherent with EVERYTHING known from the corpus.

---

## 7. [THEOREM E] The dividend: defect density, the tensor flow, and the hyperbolic ideal

Finite dimension, non-degenerate forms; notation of §3.

**Definition 7.1 (defect density).** $\theta(X):=\delta(X)/d(X)\in[0,1]$. The **bias** is $\beta(X):=1-2\theta(X)=\sigma(X)/d(X)\in[-1,1]$.

**Theorem E.1 (binary channel composition).** $\beta(X_1\otimes X_2)=\beta(X_1)\,\beta(X_2)$; equivalently
$$\theta(X_1\otimes X_2)=\theta_1+\theta_2-2\theta_1\theta_2,$$
the composition law for the noise of a binary symmetric channel (the "odd parity" probability of two independent noises). In particular $\theta(X^{\otimes k})=\tfrac12\bigl(1-\beta(X)^k\bigr)$.

*Proof.* $\beta=\sigma/d$ and both $\sigma$ and $d$ are multiplicative (Cor. A.3(ii)). The identity $\theta_\otimes=\theta_1+\theta_2-2\theta_1\theta_2$ is the restatement of $1-2\theta_\otimes=(1-2\theta_1)(1-2\theta_2)$. $\square$

(Probabilistically: assign to $X$ the $\pm1$ variable that equals $-1$ with probability $\theta$ — the "sign of a random direction"; the tensor multiplies independent signs, and $\beta$ is the expectation. The defect composes like the XOR of noisy bits. This reading is not decorative: it is the source of E.2–E.4.)

**Theorem E.2 (classification of ⊗-stable classes).** The only defect densities invariant under $X\mapsto X\otimes Y$ within their class are:
(i) $\theta=0$ (**polarized** objects): tensor subcategory ($\beta=1$ is the neutral element of the sign product);
(ii) $\theta=\tfrac12$ (**hyperbolic** objects, $\sigma=0$): **absorbing ideal** — if $\theta(X)=\tfrac12$ then $\theta(X\otimes Y)=\tfrac12$ for EVERY $Y$.
The class $\theta=1$ (negative definite) is NOT stable: $\theta(X^{\otimes2})=0$. And for every $X$ with $0<\theta(X)<1$:
$$\Bigl|\theta(X^{\otimes k})-\tfrac12\Bigr|=\tfrac12\,|\beta(X)|^{k}\;\longrightarrow\;0\quad\text{exponentially.}$$
*Every strict defect flows to the hyperbolic ideal; the rate is exact.*

*Proof.* Everything follows at once from E.1: $\beta=0$ absorbs; $|\beta|<1$ ⟹ $\beta^k\to0$; $\beta=-1$ ($\theta=1$) alternates $\pm1$. The identification "$\sigma=0$ ⟺ hyperbolic" is the Witt decomposition for complex Hermitian forms: the anisotropic part of a complex Hermitian form is definite (every non-definite form in dim ≥ 2 has an isotropic vector: if $Q(u,u)>0>Q(w,w)$, the segment $t\mapsto Q(u+tw,u+tw)$ with real $t$ crosses 0), and a nonzero definite part gives $\sigma\neq0$; so $\sigma=0$ ⟹ anisotropic part zero ⟹ orthogonal sum of hyperbolic planes. $\square$

**Corollary E.3 (the sterility of Doc 106, explained from within).** Prop. 3.6 of Doc 106 (no tensor amplification scheme with a subadditive bound can coexist with $\delta\geq1$) is the quantitative case of E.2: the tensor flow does NOT separate the defect — it THERMALIZES it. Amplifying with $\otimes$ pushes every defective object toward $\theta=\tfrac12$, the maximum-entropy sign state, where the defect is half the dimension and distinguishes nothing. The deep reason that "both sides are computed with the same data" (Obs. 3.7 of Doc 106): after passing to the Grothendieck ring, the only multiplicative data are $d$ and $\sigma$ (Prop. A.4), and the RH-relevant dichotomy lives in $\delta$, which is not a character. **No multiplicative invariant will ever see the defect of the ζ-object** (§8.2 aggravates this). $\square$

**Theorem E.4 (rigidity of the polarized cone under the tensor flow).** (i) $\theta=0$ is the unique attractor-free fixed point: if $\theta(X)=0$, every power and every product with polarized objects stays at $\theta=0$, and moreover $\delta(X\otimes Y)=d(X)\,\delta(Y)$ grows *linearly in the defect of the cofactor* — the polarized factor is transparent. (ii) First-step detection: $\delta(X\otimes\bar X)=2p\delta\geq2\delta$, and $\delta(X\otimes\bar X)=0\iff\delta(X)=0$ or $p(X)=0$: the Hermitian square detects the defect if and only if there is at least one positive direction. (iii) But the detection in (ii) is again $\delta$, not a character: there is no multiplicative function implementing it (A.4) — detection requires *reading a signature*, i.e. the inertia of P43.

*Proof.* (i) and (ii) are A.2 with $(p_2,\delta_2)=(p,\delta)$ of the conjugate (A.6: same signature): $\delta(X\otimes\bar X)=p\delta+\delta p=2p\delta$. (iii) is A.4. $\square$

**Remark 7.2 (status of novelty — frankness).** The ingredients of §7 are classical (Sylvester, Witt, multiplicativity of the signature). The synthesis — defect density as the bias of a binary channel, the E.2 classification of ⊗-stable classes with the absorbing hyperbolic ideal as structural explanation of the sterility of tensor amplifiers, and the D.4 + C.2 stratification of the defect — I do not know it written in the Kreĭn-space literature in this form. It is the kind of statement an expert would recognize as "organized folklore plus two small new theorems" (C.1 and D.4/D.5 in this generality). The claim of strong novelty rests on C.1: *"a Kreĭn space with a replicable negative vector — orbit of isometries with unbounded heights and decreasing correlations — has infinite negative index"* is, as far as the corpus and my knowledge reach, a statement not written before, elementary but with content (the Pontryagin dichotomy without Pontryagin). **[Declared: no external bibliographic search was done this session; the claim is "not written in the corpus nor known to me", not "provably nonexistent".]**

---

## 8. [BRIDGE] The ζ-object in 𝒫ol_δ, and what each theorem bites into

### 8.1. The dictionary and the statement

$$Z_\zeta=(\mathcal K,\,Q,\,P_{\mathrm{off}};\;A=H_C,\;S,\;\tau)\in\mathcal Pol_\delta,\qquad
\boxed{\;\mathrm{RH}\iff\delta(Z_\zeta)=0.\;}$$

Status of each link, without makeup:
- The form $Q$ (Weil) and its $\kappa(Q)=2m$: **a theorem of the corpus** (P35 and antecedents) in the sense $\kappa(Q)=2m$ on the quadruple model; the identification with $\mathrm{neg.ind}$ of the operator $H_C$ in the Pontryagin is the **P35 bridge conjecture** (program V.1–V.4). The statement "RH ⟺ δ=0" already holds at the level of the Weil form without going through the bridge: $\delta=\kappa=2m$ and $m=0$ ⟺ RH. **This link is solid.**
- $A=H_C$ $Q$-symmetric, $S$ of the functional equation with $SAS^{-1}=-A$: structure of the Phase 26 model; the parity $\delta=2m$ is now the **Theorem D.4** applied (before: a computation; now: an instance of a category theorem).
- $P_{\mathrm{off}}$ = spectral part with $z^2\notin\mathbb R$: well defined in the model (spectral decomposition of Doc 96 via Doc 106 §3.2/R2).

### 8.2. Which theorems bite on $Z_\zeta$ — and the Witt finding

**(a) Theorem D bites already:** $\delta(Z_\zeta)$ is even; $\hat\delta=m$; the $\delta=1$ objects are forbidden by functional symmetry alone. (New content: any attempt to build a "half-quadruple" as an intermediate obstacle is categorically empty.)

**(b) The structural finding (Theorems A/E on the off part):** the signature of $Q|_{\mathcal K_{\mathrm{off}}}$ is $(2m,2m)$ (Doc 106 §3.2: sum of hyperbolic planes — re-derived here as D.2+D.4). Hence
$$\sigma(\mathcal K_{\mathrm{off}})=0,\qquad\theta(\mathcal K_{\mathrm{off}})=\tfrac12:$$
**the defective part of the ζ-object is Witt-trivial and lives exactly in the absorbing ideal of E.2.** Proved consequences: every additive-multiplicative invariant assigns it the same value as the zero object of its dimension (A.4); every tensor flow leaves it in the ideal (E.2); its defect is invisible to characters and only legible as *inertia* (E.4(iii)). This is the internal, theorem-backed explanation of WHY they failed: the tensor amplifier (Doc 104/106), every "multiplicative detector function", and every attempt to read $m$ from an averaged value — P43's value/inertia wall is, in 𝒫ol_δ, the statement "δ is not a character" (A.4). This is not an analogy: it is the same fact in algebraic coordinates.

**(c) Theorem B bites on the architecture:** the program's identity D-109, RH = (m<∞) ∧ (m∈{0,∞}), is rewritten as the conjunction of the theory's two axes:
$$\mathrm{RH}\;=\;\underbrace{\bigl[\;\delta(Z_\zeta)<\infty\;\bigr]}_{\text{Fredholm axis (B.4): essential positivity}}\;\wedge\;\underbrace{\bigl[\;\delta(Z_\zeta)\in\{0,\infty\}\;\bigr]}_{\text{symmetry axis (C.2): replicability}}.$$
B.4 gives the exact form of objective L8: **it suffices to prove that the Gram operator of the Weil form is essentially positive** (positive modulo compacts, with essential gap) to obtain $m<\infty$. Status: NOT proved for $Z_\zeta$; but the statement is new in this form and is strictly weaker than positivity ($\delta=0$): it is "polarization modulo compacts". [WISH 8.D1 below.] And B.3 bounds the behavior under deformations: in any norm-continuous De Bruijn–Newman-type family $\{Q_t\}$, $\delta(t)$ only jumps at kernel crossings — the characterization $\Lambda=\inf\{t:T_\lambda(t)=0\}$ of Doc 70 is a candidate for "first kernel crossing of the flow"; **status: analogy, not proved identification** (the topology of the DBN flow on the Gram operator is not verified as norm-continuous). [Partial bridge.]

**(d) Theorem C bites conditionally — and here the total frankness (the question of the objective).** Applying C.2 to $Z_\zeta$ requires Axiom R: *every negative vector of $P_{\mathrm{off}}$ is replicable*. Breakdown of the three hypotheses of Def. 5.1 on $Z_\zeta$, in the analytic coordinate where replicas are vertical translations (dictionary M1):

| abstract hypothesis | analytic form on ζ | status |
|---|---|---|
| $h(\Gamma)$ unbounded | quasi-periods of heights $\tau\to\infty$ with relative density | **THEOREM** at the B² level (D112 Lemmas 2.1–2.2, unconditional, via ℚ-linear independence of $\{\log p\}$) |
| decay $\omega$ of correlations between replicas at separated windows | decay of the Weil pairing between distant spectral windows; in the CCM model, $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$ | **plausible and partially established in the model** (Doc 98/95); NOT verified as a statement about the exact object $Z_\zeta$ — [GAP-132.ω, declared] |
| $\gamma$ acts by **$Q$-isometry** on the orbit of $v$ (or $\varepsilon$-isometric replicas, C.3) | $\sup_D|\zeta(s+i\tau_k)-\zeta(s)|\to0$: the translation is POINTWISE self-approximation in the zero's window | **OPEN = LP-112.** |

**Direct answer to the question of the objective:** the hypothesis remaining when applying the abstract dichotomy to the ζ-object **is old LP-112 in disguise — yes, it is it, and declaring it is mandatory.** Defect theory does not manufacture the pointwise quasi-period; nothing elementary could, because Prop. 2.6 of D112 proves that its witnesses have zero density under ¬RH and P43's master quantifier blocks the non-generic selection. What the theory DOES add, and was not there: (i) the dichotomy needs only data from ONE orbit and ONE vector (C.1/C.3), with constants internal to the world — confirming and abstracting D112 §2.6's finding that finiteness freezes the constants; (ii) it separates LP-112 (the isometry axiom) from the other two hypotheses, which have better status (one is a theorem, the other is model [GAP-132.ω], attackable without touching pointwise ζ); (iii) it shows that Rouché's role was only to certify the approximate isometry — any OTHER certificate of $\varepsilon$-isometry on the orbit (not necessarily complex-analytic) would feed C.3 just the same. The space of attacks on LP-112 is wider than the one via Rouché. That is a genuine reframing, not a solution.

### 8.3. The categorical reformulation of MINIMAL-STATEMENT-130

Doc 130 §5.3 asks for: a foliated construction over Spec ℤ whose good definition does not presuppose the localization of the zeros, such that under ¬RH the space exists with the polarization visibly failing. In the language of 𝒫ol_δ:

> **MINIMAL-STATEMENT-130, categorical form.** Deninger's route is non-circular if and only if its construction defines a functor $\mathfrak D:\{\text{arithmetic worlds}\}\to\mathcal Pol_\delta$ with **total domain** — the object $\mathfrak D(\text{world})$ exists and its $\delta$ is defined in EVERY world — and RH is the statement $\delta(\mathfrak D)=0$. The circularity diagnosed by Doc 130 is exactly: the Kähler–Riemann construction only defines the object **within the fiber $\delta=0$** (the metric uses Hasse; without the analogue, neither is the measure invariant nor does the trace converge). A functor defined only where its invariant vanishes states nothing.

The category 𝒫ol_δ is the missing codomain for NC4 to be even formulable. And instance (I3) (Babaee–Huh) proves that the codomain is not empty in its defective stratum: there are frank (tropical) geometries whose object has visible $\delta\geq1$. The corresponding [WISH] is named below.

### 8.4. Bite table

| Theorem | does it bite on $Z_\zeta$? | what it gives | what is missing |
|---|---|---|---|
| A (arithmetic) | yes, unconditional | $\delta$ monotone/additive; Whitney; $\delta$ is not a character | — |
| E (hyperbolic ideal) | yes, unconditional | $\mathcal K_{\mathrm{off}}$ is Witt-trivial, $\theta=\frac12$: invisible to every multiplicative invariant — structural closure of the amplifier route | — |
| D (parity) | yes, unconditional on the model | $\delta=2m$ even; $\delta=1$ forbidden; $\hat\delta=m$ theorem | P35 bridge for the operatorial version |
| B.4 (Fredholm) | new statement of the objective | $m<\infty$ ⟸ essential positivity of the Weil Gram operator | prove essential positivity [WISH 8.D1] |
| B.1–B.3 (rigidity) | partial | $\delta$ jumps only at kernel crossings; framework for DBN | continuity of the DBN flow on the Gram operator [not verified] |
| C (dichotomy) | conditional | $\delta\in\{0,\infty\}$ under Axiom R; 2 of 3 hypotheses with better status than LP-112 | the isometry axiom = **LP-112** (declared) + [GAP-132.ω] |
| B.6 (cone rigidity) | yes, as a lens | Doc 118 = separation defect 1 + Hardy functional | — |

---

## 9. [WISH] The wishes, without shame

**[WISH 8.D1 — essential positivity.]** Prove that the Gram operator of the Weil form (in a Hilbert-type realization of the test domain, e.g. the CCM) is **essentially positive**: $\mathrm{spec}_{\mathrm{ess}}\subseteq(0,\infty)$. By B.4 this would give $m<\infty$ — the L8 target — and it is strictly weaker than every positivity pursued before: it allows ANY finite amount of negative directions and any compact perturbation. It is "RH modulo compacts". No refutation in the corpus ($W_\lambda\geq0$ falling, etc.) touches this statement: the refuted positivities were pointwise/kernel positivities, not essential-spectral ones.

**[WISH 8.D2 — the total functor.]** Construct $\mathfrak D$ with total domain (§8.3) even if only for a substitute of Spec ℤ (Morishita's $\mathfrak X_F$, via Doc 128/130): a foliated object of 𝒫ol_δ whose existence does not use localization. The test of success is cold: compute $\delta$ of the object in a toy ¬RH world (a foliated Davenport–Heilbronn) and see it positive.

**[WISH 8.D3 — the non-Rouché certificate.]** An $\varepsilon$-isometry certificate on the orbit of a negative vector (C.3) that does not go through uniform self-approximation on discs: e.g. approximate isometry only on the hyperbolic plane of the quadruple (4 dimensions, not a whole disc of functions). LP-112 asks for $\sup_D$ over a disc; C.3 asks for $n^2$ numbers. The gap between the two is a legitimate wish for Phase 45.

**[WISH 8.D4 — spectral theory in the ideal.]** A theory of "relative index in the hyperbolic ideal": since $\mathcal K_{\mathrm{off}}$ is Witt-trivial, the fine invariant must be relative to a reference (the pair $(Q,Q_{\mathrm{ref}})$, of spectral-flow / Fredholm-pair-index type). The defect as the **spectral flow** of a family interpolating the Weil form with its on-line version: $\delta=\mathrm{sf}(Q_t)$. B.3 is the first step (jumps only at crossings); the theory of the crossing is missing.

---

## 10. The final map

**PROVED in this document (unconditional, complete proof):**
1. **Lemma A.0** (finite-index decomposition) and **Theorem A.1** (monotonicity; additivity of $\delta$ under $\oplus$ with no dimension hypothesis).
2. **Theorem A.2 / Corollary A.3** (defect Whitney formula $\delta_\otimes=p_1\delta_2+\delta_1p_2$, inclusion-exclusion, super-additivity, powers, stability of polarization) — A.2 re-proves Doc 106 Prop. 3.1 within the category.
3. **Proposition A.4** (the only characters are $d$ and $\sigma$; $\delta=(d-\sigma)/2$ is not a character) and **A.5/A.6** (Fredholm in infinite dimension; dual and conjugate).
4. **Theorems B.1–B.4** (rigidity: local Riesz constancy; $|\Delta\delta|\leq\mathrm{rank}$; semicontinuity and jumps only at kernel crossings; essential positivity ⟹ finite defect, stable under compacts — Weyl cited precisely) and **B.6** (cone rigidity; Doc 118 as an instance with separation defect 1).
5. **Theorem C.1** (replicable negative vector ⟹ $\delta=\infty$; Gershgorin on the Gram matrix of the orbit), **Corollary C.2** (dichotomy $\delta\in\{0,\infty\}$ under Axiom R), **Theorem C.3** (approximate-replicas version) — the exact abstraction of Doc 112's mechanism, with model checks M1–M3 (Doc 112 is an instance; the cosh models fail the correct hypothesis; DH consistent).
6. **Lemmas D.1–D.2 and Theorems D.3–D.5** (radical orthogonality; hyperbolic $(d,d)$ pairing; exact value of the spectral defect; PARITY under functional symmetry — $\delta=1$ forbidden; $\Pi_1(z)$ classification of minimal defect).
7. **Theorems E.1–E.4** (defect density as binary-channel bias; classification of ⊗-stable classes: polarized = subcategory, hyperbolic = absorbing ideal; exact exponential thermalization; sterility of Doc 106 explained; the Hermitian square detects but only as inertia).

**BRIDGE (declared status):** $Z_\zeta\in\mathcal Pol_\delta$ with RH ⟺ $\delta(Z_\zeta)=0$ (solid at the level of the Weil form; operatorial = P35 conjecture). Biting unconditionally: D (parity, $\hat\delta=m$), E (**finding: $\mathcal K_{\mathrm{off}}$ is Witt-trivial, $\theta=\tfrac12$, in the absorbing ideal** — theorem-level closure of every multiplicative/amplifying route), A.4 (P43's value/inertia wall = "δ is not a character"). Biting conditionally: B.4 (reformulates L8 as essential positivity — a new statement, weaker than every previous positivity), C (dichotomy under Axiom R: **the remaining hypothesis about ζ is LP-112 in disguise**, declared without mitigation; the other two hypotheses have theorem / model-gap status). MINIMAL-STATEMENT-130 reformulated: Deninger's non-circularity = functor with total domain in 𝒫ol_δ; Babaee–Huh populates the defective stratum.

**WISH:** 8.D1 (essential positivity of the Weil Gram operator ⟹ L8), 8.D2 (the total functor, tested in a toy ¬RH world), 8.D3 (non-Rouché $\varepsilon$-isometry certificate for C.3), 8.D4 (defect as relative spectral flow in the hyperbolic ideal).

**NEXT THEOREM (the most attackable, in order):**
1. **[GAP-132.ω]** the correlation decay of Def. 5.1 for $Z_\zeta$ in the CCM model ($\omega$ from $K_\lambda(\gamma)\asymp\gamma^{-1/2}e^{-\pi\gamma/2}$, Doc 98/95): it is a model statement, with no master quantifier, and would leave the dichotomy hanging on ONE single axiom (isometry).
2. **8.D1 in toy version:** essential positivity of the Weil Gram operator for Davenport–Heilbronn and for the cosh class (where the answer is known another way: calibration).
3. **B.3→DBN:** verify the norm-continuity of the De Bruijn–Newman flow on the Gram operator in the CCM realization, to turn "Λ = first kernel crossing" from analogy into theorem.

---

## References

**Internal (backward-only):** Doc 130 (circularity of the Kähler–Riemann metric; MINIMAL-STATEMENT-130); Doc 129/128/127 (foliated context); Doc 125 (intersection form of the square; toy model $(1,2)$; Babaee–Huh [arXiv:1502.00299, via Doc 125 §5.5]); Doc 119 (R-NC test); Doc 118 (moment rigidity: Carleman + cone; Theorem 5.3); Doc 117; Doc 114 (refutation $W_\lambda\geq0$); Doc 112 (LP-112; Theorem 2.3; Prop. 2.6 zero density; Lemmas 2.1–2.2, 3.1–3.3); Doc 111 (cosh class; Cor. 2.3); Doc 109 (identity D-109); Doc 106 §3 (Props. 3.1, 3.3, 3.4, 3.6; Obs. 3.7); Doc 105; Doc 104; Doc 98 (cost $2\delta^2K_\lambda(\gamma)$); Doc 96 (spectral decomposition of $\mathcal K_{\mathrm{off}}$); Doc 95 (decay of $dm_\infty$); Doc 89; Doc 83 ($d\nu\geq0$); P43 (master quantifier; value/inertia); P35 (bridge conjecture $\kappa=\mathrm{neg.ind}(H_C)=2m$; program V.1–V.4).

**Literature (classical, verifiable):**
- T. Kato, *Perturbation Theory for Linear Operators*, Springer, 2nd ed. 1976. (Thm. IV.5.35: invariance of the essential spectrum under compact perturbation — used in B.4; Riesz projections and continuity — used in B.1.)
- M. Reed, B. Simon, *Methods of Modern Mathematical Physics IV*, Academic Press, 1978, §XIII.4. (Weyl's theorem; alternative citation for B.4.)
- J. Bognár, *Indefinite Inner Product Spaces*, Springer, 1974. (General theory of indefinite forms; orthogonality of radical subspaces of $Q$-symmetric operators — D.1 is proved here self-contained, the reference is for context.)
- I. S. Iohvidov, M. G. Kreĭn, H. Langer, *Introduction to the Spectral Theory of Operators in Spaces with an Indefinite Metric*, Akademie-Verlag, 1982. ($\Pi_\kappa$ spaces; context for D.5 and for C.1's "Pontryagin dichotomy without Pontryagin" reading.)
- W. Scharlau, *Quadratic and Hermitian Forms*, Springer, 1985. (Witt decomposition; multiplicativity of the signature — context for A.2–A.4, E.2; the proofs used are self-contained.)
- S. Gershgorin, *Über die Abgrenzung der Eigenwerte einer Matrix*, Izv. Akad. Nauk SSSR 1931. (Gershgorin discs — C.1, C.3.)
- F. R. Gantmacher, *The Theory of Matrices*, Chelsea, 1959. (Inertia, Hankel forms; context.)
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. 11 (1936). [via Doc 112 §3.3 — calibration M3.]

*End of Doc 132.*
