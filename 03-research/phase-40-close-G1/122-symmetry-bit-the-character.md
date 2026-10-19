# Doc 122 — The symmetry bit: the character of the duality pairing at the self-dual divisor

**Program:** Riemann Hypothesis — Phase 40, closing G1
**Prerequisites:** Doc 119 (R-SIG: realizations (i)/(ii)/(iii) of a signature; minimal core of R-SIG; R-NC test); Doc 120 (in-source CC inventory; §3.2 Serre duality with tolerance of 2205.01391; §7.7 negative search for "signature"); Doc 121 (crossing A; Conjecture 121.A; self-dual divisor D₀=−{2}; falsifiers F-A1..F-A4; **Problem 121.E**, which this document executes).

**Source read in this session:** A. Connes, C. Consani, *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$*, arXiv:2205.01391, via the arXiv PDF (extracted with `pdftotext`; the verbatim quotes from §5 and §1–2 below come from that extracted text, with equation numbers as they appear). What Doc 120 verified by assisted extraction is here **re-verified against the raw text of §5** (Duality section, lines 1004–1315 of the extract), which is the primary source for the bit requested.

**Labeling discipline (absolute rule):** **[DATA]** = read in source this session, with exact citation (paper + equation/theorem). **[COMPUTATION]** = my own derivation, shown step by step. **[GAP]** = what could not be determined, with the reason and the exact datum that would be needed. **[CONJECTURE]** / **[NOT VERIFIED]** = as indicated. NEVER "proved" about anything geometrically new. A false victory is worse than a failure.

---

## 0. Executive summary

Problem 121.E asked for a bit: the symmetry character (±1) of the Connes–Consani (hereafter CC) Serre duality pairing with tolerance, restricted to the self-dual divisor D₀ = −{2}. The answer, after reading §5 of 2205.01391 in the raw source, **is neither +1 nor −1: it is that the question, as formulated (Step 3 of Conjecture 121.A), presupposes a structure the source does NOT have** — and the reason is structural, not accidental.

The central finding, in one line:

> **[DATA]** CC's "Serre duality pairing with tolerance" **is the Pontryagin duality of locally compact abelian groups**: the underlying pairing is **character evaluation** $\langle\chi, x\rangle = \chi(x) \in U(1)$ between an abelian group $A$ and its dual group $\widehat A$ (2205.01391, Prop. 5.2 + Thm. 5.3). It is NEITHER a cup product (→ alternating) NOR an Ext-type duality form over a single space (→ possibly symmetric). It is of a **third** kind: a perfect pairing **between a group and its dual, two generically non-isomorphic objects**, with no involution, no values in a field, no notion of bilinearity-over-a-single-space.

For a Pontryagin evaluation $\widehat A \times A \to U(1)$ the "symmetric/alternating" dichotomy **is not defined**: symmetry requires domain and codomain of the pairing to be the same object, and here they are $\widehat A$ and $A$. The "symmetry character" only makes sense after **identifying** $\widehat A \cong A$, and that identification is exactly what is missing at the self-dual point — where, moreover, **both spaces turn out to be zero** (§3).

**Verdict of the bit (§5): structural GAP, with a precise diagnosis.** It is neither −1 (alternating) nor +1 (symmetric): CC's duality is simply not of the kind that has a symmetry character. The consequence for R-SIG is **stronger than a −1**: one does not even reach the point where Arf/parity (the −1 outcome of 121.E) would be the invariant. The exact datum one would need to ask Connes is in §5: **a self-pairing** — a natural isomorphism $H^1(D_0) \cong \widehat{H^1(D_0)}$ (a "principal polarization" of the tolerance module) — that the theory does not currently provide and which, at $D_0$, is vacuous because $H^1(D_0)=0$.

---

## 1. What the source says, verbatim (re-verification of §5 of 2205.01391)

This section replaces the assisted reading of Doc 120 §3.2 with the raw text of section 5 ("Duality") of the PDF.

### 1.1. The divisors: INTEGER coefficients at finite primes

**[DATA]** (2205.01391, §5, Thm. 5.3, opening line, verbatim from the extract):

> "Let $D = \sum_j a_j\{p_j\} + a\{\infty\}$ be an Arakelov divisor on $\mathrm{Spec}\,\mathbb Z$."

and (introduction / §2, verbatim):

> the coefficients satisfy $a_j \in \mathbb Z$ at finite primes $p_j$ and $a \in \mathbb R$ at the archimedean place $\{\infty\}$ ($|\cdot|_\infty$).

**[DATA]** The canonical divisor is $K := -2\{2\}$, $\deg K = -2\log 2$ (Thm. 1.2 and §5, verbatim "where $K$ is the divisor $K=-2\{2\}$").

**Immediate consequence for the admissibility of D₀** [COMPUTATION]: $D_0 = -\{2\}$ has coefficient $a_2 = -1 \in \mathbb Z$ at the finite prime $2$, and archimedean coefficient $a=0$. It is therefore an **admissible Arakelov divisor** in the strict sense of their §5: integer coefficient at a finite prime, real coefficient (here zero) at $\infty$. **No half-integers nor real coefficients at finite primes are needed.** Crossing (A) does NOT die from D₀'s inadmissibility: the fixed point exists within their category of divisors. (This closes, affirmatively, the Step 2 sub-check of the objective: the doubt "is −1 at place 2 admissible?" is resolved YES.)

[COMPUTATION] Verification of the fixed point, exact at the level of divisors (not classes):
$$K - D_0 = -2\{2\} - (-\{2\}) = -2\{2\} + \{2\} = -\{2\} = D_0.$$
The Serre involution $\sigma: D \mapsto K-D$ fixes $D_0$ **on the nose**. Matches Doc 121 §2.1.2.

### 1.2. The objects H⁰ and H¹: modules over 𝕊[±1] with tolerance

**[DATA]** (2205.01391, §1–2, verbatim):

- $H^0(D)$ is the $\mathbb S[\pm1]$-module $\|H\mathbb Z\|_{e^a}$: on the pointed set $k_+$, families $m = \sum \alpha(f) f$ with total norm $\sum|\alpha(f)f| \le e^a$. For an archimedean divisor $D=a\{\infty\}$, it "depends only upon the integer part $n=\lfloor e^a\rfloor$".
- $H^1(D)$ is the **cokernel** of $\psi$ in (1.2), realized as the **pair $(\,H\mathbb A_{\mathbb Q},\,\mathcal R\,)$** — a *tolerance $\mathbb S[\pm1]$-module* — where $\mathcal R$ relates pairs whose difference is in $\mathrm{Im}\,\psi$. Verbatim (§1, on the archimedean case):

> "the dimension of $H^1(D)$ is the same as the dimension of the pair $(H(\mathbb R/\mathbb Z), R)$, where the relation $R$ on $H(\mathbb R/\mathbb Z)(1_+)=\mathbb R/\mathbb Z$ is given by $(x,y)\in R \iff d(x,y)\le e^a$" (1.4),

with $d$ the invariant Riemannian metric of length 1 on $\mathbb R/\mathbb Z$.

**[DATA]** Dimension of $H^1$ of the archimedean divisor (2205.01391, Prop. 4.1, eq. (1.5), verbatim):
$$\dim_{\mathbb S[\pm1]}(H(\mathbb R/\mathbb Z), R) = \left\lceil \frac{-a-\log 2}{\log 3}\right\rceil.$$

### 1.3. The duality IS Pontryagin's: the pairing is character evaluation

This is the heart of the document. I quote §5 in block (verbatim from the extract, eqs. (5.11), Prop. 5.2(i)–(ii), Thm. 5.3):

**[DATA]** Opening of §5 "Duality":

> "In this section we prove an absolute analogue of Serre's duality, namely the following isomorphism of $\mathbb S[\pm1]$-modules, for any divisor $D$ on $\mathrm{Spec}\,\mathbb Z$:
> $$H^0(D) \simeq \mathrm{Hom}_{\Gamma\mathcal T_*}(H^1(K-D),\, U(1)_{\frac14}). \quad$$
> Here, the divisor $K=-2\{2\}$ plays the role of the canonical divisor. The choice of the tolerant $\mathbb S[\pm1]$-module $(U(1),d)_{\frac14}$ as dualizing module is motivated by Pontryagin duality. One has $\dim_{\mathbb S[\pm1]}(U(1)_{\frac14})=1$."

**[DATA]** Definition of the dualizing module (§5.2, verbatim):

> "we consider, for $\lambda>0$, the $\mathbb S[\pm1]$-module $U(1)_\lambda = (U(1),d)_\lambda$, where $U(1)$ is the abelian group $\mathbb R/\mathbb Z$ endowed with its canonical metric $d$ of length 1. For a metric abelian group $(A,d)$, we denote by $\widehat A$ the abelian group of continuous characters, i.e. of continuous group homomorphisms $A\to U(1)$."

**[DATA]** Proposition 5.2(i) (verbatim):

> "For $\lambda,\mu\in\mathbb R_{>0}$, the $\mathbb S[\pm1]$-module $\mathrm{Hom}_{\Gamma\mathcal T_*}((A,d)_\lambda, U(1)_\mu)$ is isomorphic to the sub $\mathbb S[\pm1]$-module of $H\widehat A$ which, on the set $k_+$, is given by $k$-tuples $(\chi_j)$, $1\le j\le k$ of continuous characters $\chi_j\in\widehat A$ such that, with $|x|:=d(x,0)$, and for all finite collections $\{x_i\}\subset A$, fulfill
> $$\sum_i |x_i|\le\lambda \;\Rightarrow\; \sum_{i,j}|\chi_j(x_i)|\le\mu. \quad(5.8)$$"

And in the proof (verbatim): "This shows that $\mathrm{Hom}_{\Gamma\mathcal T_*}((A,d)_\lambda,U(1)_\mu)$ consists exactly of the group homomorphisms $\chi: A\to U(1)$ fulfilling (5.8)."

**[DATA]** Proof of Thm. 5.3 (verbatim, core): with $\lambda=\exp a$, $H^1(D)=\pi^*((\mathbb R/L,d)_\lambda)$; by Prop. 5.2(ii) it reduces to $\mathrm{Hom}_{\Gamma\mathcal T_*}((\mathbb R/\mathbb Z,d)_\lambda, U(1)_{\frac14})$; and one identifies

> "with $A=\mathbb R/\mathbb Z$ and $\mu=\frac14$. One has $\widehat A=\mathbb Z$ and the characters $\chi_n\in\widehat A$ are given by multiplication by $n$, i.e. $\chi_n(s):=ns\in\mathbb R/\mathbb Z$, $\forall s\in\mathbb R/\mathbb Z$."

resulting in the submodule $\|H\mathbb Z\|_{1/4\lambda}$.

**Structural reading [mixed COMPUTATION/DATA, each clause labeled]:**

1. **[DATA]** CC's Serre dual $H^0(K-D) = \mathrm{Hom}_{\Gamma\mathcal T_*}(H^1(D), U(1)_{1/4})$ is **literally a group of characters** $\widehat{A}$ of the abelian group $A$ on which $H^1(D)$ is built (here $A=\mathbb R/\mathbb Z$, $\widehat A = \mathbb Z$), cut down by the tolerance condition (5.8).
2. **[DATA]** The "pairing" that realizes the duality is, therefore, **Pontryagin evaluation**
   $$\langle\,\cdot\,,\,\cdot\,\rangle:\ \widehat A \times A \longrightarrow U(1),\qquad (\chi, x)\longmapsto \chi(x),$$
   that is, $(n, s)\mapsto ns \bmod 1$ in the explicit case. It is a group homomorphism in each variable (biadditive), perfect (Pontryagin), with values in the **group** $U(1)=\mathbb R/\mathbb Z$.
3. **[DATA/COMPUTATION]** This pairing couples **two different objects**: $A$ (group) and $\widehat A$ (its dual). Generically $A\not\cong\widehat A$ (here $A=\mathbb R/\mathbb Z$ is compact connected, $\widehat A=\mathbb Z$ is discrete: they are not even of the same topological type). There is NOT one single space on which the duality is a form.

---

## 2. Why "symmetry character" is not defined for a Pontryagin evaluation

The objective (Step 4) asked to distinguish TWO possibilities and say which one is CC's:

- **(cup product)** $H^1\times H^1\to H^2$: in every Weil cohomology it is **alternating** in odd degree (symplectic form, principal polarization of the jacobian). Outcome −1.
- **(Serre duality of Ext type)** $H^1(D)\times H^0(K-D)\to k$ with $k$ a field: at the self-dual point it can induce a **symmetric** form on $H^1$. Outcome +1.

The source forces a third answer, and it is worth displaying the algebra behind why the two classical dichotomies do not apply.

### 2.1. The algebraic requirement of "symmetry" and where it fails

[COMPUTATION] A bilinear form $B: V\times V\to T$ has symmetry character $\varepsilon\in\{\pm1\}$ when $B(x,y)=\varepsilon\,B(y,x)$. This **presupposes**:
- (a) **a single space** $V$ in both slots (for $B(y,x)$ to make sense one must be able to put $y\in V$ in the first slot and $x\in V$ in the second);
- (b) a codomain $T$ where the equality $B(x,y)=\varepsilon B(y,x)$ is a meaningful equation (an abelian group is enough for this).

CC's pairing, $P:\widehat A\times A\to U(1)$, $P(\chi,x)=\chi(x)$:
- **(a) FAILS.** The two slots are $\widehat A$ and $A$, different objects. $P(x,\chi)$ is not defined: $x\in A$ is not a character, it cannot be evaluated at $\chi$. The expression "$P(y,x)$ vs $P(x,y)$" has no referent.
- (b) would hold (U(1) is an abelian group), but is irrelevant without (a).

**[COMPUTATION] Conclusion: the symmetry character $\varepsilon$ of $P$ is NOT defined in the source.** It is not that it is +1 or −1 and CC do not say so: it is that the structure CC build (Pontryagin duality group↔dual) is not of the kind that has an $\varepsilon$. To have one, a **prior identification** $j: A \xrightarrow{\sim} \widehat A$ (a "polarization") would be needed, after which $B(x,y):=P(j(x), y)=\langle j(x), y\rangle$ lives on $V=A$ and DOES have a character $\varepsilon$. That $j$ is external input; it is not in 2205.01391.

### 2.2. Why it is not a cup product (rules out the "easy" −1 outcome)

[DATA+COMPUTATION] The cup product of a Weil cohomology is a product **internal to the cohomology algebra** $H^\bullet$, $H^i\otimes H^j\to H^{i+j}$, with the graded antisymmetry $a\cup b=(-1)^{ij}b\cup a$ as a **property of the product**. In 2205.01391:
- There is no graded cohomology algebra $H^\bullet$ with a product: there are $H^0$ and $H^1$ of a **divisor** (not of a total space), and the only operation between them is the morphism $\psi$ of the short exact sequence and its Pontryagin dualization. **[DATA]** (no cup product appears in the text; the index of §5 is "Serre and Pontrjagin dualities", not "cup product").
- The "$H^2$" where a cup product would land **does not exist** in their dimension-1 theory (it is a "curve", $\mathrm{Spec}\,\mathbb Z$, not a surface). The target of the duality is $U(1)_{1/4}=H^1(K)$, not an $H^2$.

Therefore **the warning of Doc 121 §2.1.4 (F-A1: "in odd degree the cup product is alternating") does not apply to CC's object**: there is no cup product. This is partial good news — the path is NOT cut off via the classical unfavorable route — but bad news replaces it: there is also no Ext-type symmetric form, because there is no field of values and no single space.

### 2.3. Why it is not Serre duality "of Ext type over a field" (rules out the "easy" +1 outcome)

[DATA+COMPUTATION] Classical Serre duality $H^1(D)\times H^0(K-D)\to H^1(K)\cong k$ takes values in the **base field** $k$, and the pairing is $k$-**bilinear**; that allows, via an isomorphism $H^0(K-D)\cong H^1(D)^\vee$ and self-duality $2D=K$, building a $k$-bilinear form on $H^1(D)$ whose $\varepsilon$ can be computed.

In CC the target is $U(1)_{1/4}=H^1(K)$, which **is not a field**: it is the group $\mathbb R/\mathbb Z$ with a tolerance. The pairing is **biadditive ($\mathbb Z$-bilinear of groups), not $k$-bilinear over a field**. The machinery "duality isomorphism + self-duality ⟹ form with $\varepsilon$" requires linearity over a field so that the transpose $B^t$ lives in the same space of forms and the comparison $B$ vs $B^t$ yields a scalar $\varepsilon$. Over an abelian group with no field structure, "transposing" a character does not return a character of the same group (it returns an element of the bidual, via evaluation) — and that is precisely Pontryagin reflexivity $A\cong\widehat{\widehat A}$, **not** a symmetry $\widehat A\cong A$.

[COMPUTATION] Let us make explicit the only "symmetry character" that DOES exist here, so as not to confuse it with the one requested. Pontryagin duality has a canonical **biduality isomorphism**
$$\mathrm{ev}: A \xrightarrow{\ \sim\ } \widehat{\widehat A},\qquad \mathrm{ev}(x)(\chi)=\chi(x).$$
Its "square" (the compatibility $\widehat{\mathrm{ev}_A}\circ\mathrm{ev}_{\widehat A}=\mathrm{id}$) is always **+1** — but this is reflexivity, a fact of every Pontryagin duality, and it is **NOT** the bit of 121.E. 121.E asked for the $\varepsilon$ of a form on $H^1(D_0)$; biduality instead gives that $H^1(D_0)$ is reflexive. Conflating the two would be the false victory to avoid: "+1 of biduality" is not "+1 of a symmetric form". **[COMPUTATION, labeled as an anti-circularity warning.]**

---

## 3. The self-dual point D₀: both spaces vanish (falsifier F-A4 confirmed)

Even granting, *for the sake of argument*, that an identification $j:H^1(D_0)\cong\widehat{H^1(D_0)}$ existed, one must compute which object $H^1(D_0)$ is. The source gives it exactly.

[COMPUTATION] $D_0=-\{2\}$ has $\deg D_0 = -\log 2$, archimedean part $a=0$. But the $H^1$ of a divisor supported at a finite prime reduces (Thm. 5.3, "we can assume that $D=a\{\infty\}$ with $a=\deg D$") to the $H^1$ of the archimedean divisor of **the same degree**. So we take $a=\deg D_0=-\log 2$ and apply (1.5):
$$\dim_{\mathbb S[\pm1]} H^1(D_0) = \left\lceil \frac{-a-\log 2}{\log 3}\right\rceil = \left\lceil \frac{\log 2-\log 2}{\log 3}\right\rceil = \lceil 0\rceil = 0.$$

[DATA] And by the RR formula (Thm. 1.1) with $\chi(D_0)=0$ (Doc 121 §2.1.2; here re-derived: $\dim H^0-\dim H^1=0$ at the self-dual point because $\deg D_0+\log2=0$ in the numerator of the ceiling term), it follows that
$$\dim_{\mathbb S[\pm1]} H^0(D_0) = \dim_{\mathbb S[\pm1]} H^1(D_0) = 0.$$

**[COMPUTATION] Verdict of the pointwise computation: at $D_0$ both cohomologies are ZERO.** Any form on $V=H^0(D_0)\oplus H^1(D_0)=0$ is the empty form: its signature is $(0,0)$, its symmetry character is vacuously anything, its Arf is trivial. **The pointwise computation of 121.E carries no information**: it is falsifier **F-A4** of Doc 121 §2.1.4, now confirmed in source, not conjectured.

This refines the diagnosis: the content of crossing A, if any, **is not at the point $D_0$ but in the JUMP** — the variation of $(\dim H^0,\dim H^1)$ upon perturbing $D_0$ (recall Doc 121 §2.1.2.3: $\lambda=1/2$ falls at the edge of the jump interval $2^{-m-1}\le\lambda<2^{-m}$ with $m=0$). The object that could carry a signature is not the fiber at $D_0$ but the **degeneration behavior** around $D_0$ — which connects with crossing D (spectral flow in the Picard monoid), not with a pointwise pairing. **[COMPUTATION + reference to Doc 121 §2.4.]**

---

## 4. Synthesis of the bit: the objective's dichotomy, resolved by a third option

I recap the three species of pairing and where CC falls.

| species | domain of the pair | codomain | character $\varepsilon$ | is it CC? |
|---|---|---|---|---|
| cup product $H^1\times H^1\to H^2$ | one space, with itself | field | **−1** (alternating, odd degree) | **NO** (no cup product, no $H^2$) |
| Serre–Ext $H^1\times H^0(K-D)\to k$ + self-duality | one space after iso | field $k$ | $\pm1$ computable | **NO** (target $U(1)$ not a field; biadditive, not $k$-bilinear) |
| **Pontryagin $\widehat A\times A\to U(1)$** | **a group and its dual (different)** | **group** $U(1)$ | **not defined** (missing iso $A\cong\widehat A$) | **YES** (Prop. 5.2 + Thm. 5.3) |

**[COMPUTATION/DATA] CC's pairing is of the third species.** Hence:
- It does not inherit the cup product's alternating property (it is not one): the Weil-precedent "automatic −1" outcome **does not apply**.
- It does not admit Ext-type symmetrization (no field, no single space): the "+1" outcome **does not apply either**.
- Its only "canonical +1" is biduality reflexivity, which **is not the requested bit**.

The bit of 121.E is therefore, a **GAP** — but a GAP of a higher type than expected: it is not that one does not know whether it is +1 or −1; it is that **the invariant "symmetry character" is not an attribute of the structure CC have**. CC's duality lives in the category of abelian groups with tolerance, where "bilinear form with signature" is not a native notion.

---

## 5. Verdict and the EXACT datum to ask Connes

### 5.1. Verdict

**The bit of Problem 121.E: structural GAP.** Not +1, not −1. The Serre duality with tolerance of 2205.01391 is **Pontryagin duality group↔dual** (character evaluation $\widehat A\times A\to U(1)$, Prop. 5.2(i), Thm. 5.3), not a pairing over a single space; the "symmetry character" is not defined for it without an external identification $A\cong\widehat A$. And at the concrete self-dual point $D_0=-\{2\}$, **both spaces vanish** ($\dim H^0(D_0)=\dim H^1(D_0)=0$, eq. (1.5) with $a=-\log2$), so even the weaker version of the experiment (Arf/parity, the −1 outcome of 121.E) is vacuous.

This is, on the scale of Doc 119, **worse than −1 for R-SIG**: the −1 outcome of 121.E kept a mod-2 invariant alive and named "polarization" as what was missing; the structural GAP says that **a layer further down is missing** — the very category of forms is missing. But it is, by the discipline of the objective, a **valuable and frank result**: it turns "we don't know the sign" into "we know the sign is not an attribute of this duality, and we know exactly what would have to be added".

Impact on crossing A (Doc 121 §2.1) and on R-SIG (Doc 119 §2.3, realization (i)): realization (i) of R-SIG ("a bilinear/hermitian form with involution on a space") **is not obtained from CC's duality as it stands**. CC's duality realizes, at most, **Poincaré duality** (the perfect pairing $H^1\times H^0(K-D)\to$ dualizing module), which is the **prior ingredient** to a form, not the form itself. To go from Poincaré-Pontryagin to a form-with-signature the second classical ingredient is needed: a **polarization** (an isomorphism of the object with its dual, compatible and "positive"). It is exactly the diagnosis Doc 121 §4.2 had anticipated as the −1 scenario ("R-SIG needs a polarization in addition to the duality"), now confirmed and aggravated: it is not optional nor a refinement, it is the missing link that defines the problem.

### 5.2. The exact request to Connes (the datum that would close/move the bit)

Formulated as a statement internal to 2205.01391, self-contained:

> **Request 122.A (self-pairing / polarization of the tolerance module).** In the category $\Gamma\mathcal T_*$ of $\mathbb S[\pm1]$-modules with tolerance, does there exist, for a self-dual divisor $2D=K$ (in particular $D_0=-\{2\}$), a **natural isomorphism** $j_D: H^1(D)\xrightarrow{\sim}\mathrm{Hom}_{\Gamma\mathcal T_*}(H^1(D),U(1)_{1/4})$ — that is, an isomorphism of $H^1(D)$ with its **own** Pontryagin-with-tolerance dual (not with the $\widehat A$ of an auxiliary group) — compatible with the Serre involution $\sigma$? If it exists, the composition $B_D(x,y):=\langle j_D(x), y\rangle\in U(1)_{1/4}$ is a biadditive form on $H^1(D)$, and **its symmetry character $\varepsilon$ (is $j_D^\vee=\pm j_D$ under biduality?) is the bit of 121.E**. Dependent question: is $j_D$ **positive** in some sense (a "metric", a definite form) that linearizes $U(1)_{1/4}$ to $\mathbb R$ with sign (saving F-A3)?

Which theorem/object of which paper would resolve it:
1. **In 2205.01391 directly:** a theorem of **self-duality** (not merely duality) for tolerance modules at the point $2D=K$ — the analogue of the classical fact "at the theta characteristic, $H^0(K-D)\cong H^0(D)$ canonically, and Serre's form becomes a form on $H^0(D)$". CC have $H^0(K-D)\cong\widehat{H^1(D)}$ (duality) but **not** an $H^1(D)\cong\widehat{H^1(D)}$ (self-duality). The bit lives in that isomorphism, which is not written down.
2. **The ingredient their corpus has no candidate for (confirmed search, below):** a **polarization / positive form / metric** on the $H^1$ — the analogue of the Lefschetz operator $L$ or the Hodge star $\star$, which in classical geometry turns Poincaré duality into an intersection form with signature (Hodge–Riemann). Without that ingredient, CC's Pontryagin duality stays at Poincaré and never reaches signature — in dimension 1 **nor on the square**.

### 5.3. Confirmatory search: is there a polarization/positive form in the CC corpus?

[DATA] Doc 120 §7.7 (negative search): "signature/inertia index" does not appear as an invariant in any text read; the only sign structure is positivity/lower-boundedness.

Targeted re-check for this document (building on what Doc 120 verified, without a new fetch session so as not to exceed the scope of the objective, which focused the reading on 2205.01391):
- In **2205.01391** (read in the raw source this session): the only metric structure is the **tolerance** $d$ of length 1 on $\mathbb R/\mathbb Z$ and the parameter $\lambda$; there is **no** positive form on $H^1$, no operator $L$, no self-duality isomorphism. The "$1/4$" of $U(1)_{1/4}$ is a tolerance parameter chosen "by the invariance of the Riemann-Roch formula when one switches $H^0$ and $H^1$" (§5, verbatim) — combinatorial, not a polarization. **[DATA]**
- In **2602.15941** (Jacobian, via Doc 120 §3.4): the Picard group is a **monoid** with **semi-norms** (degeneration allowed); a semi-norm is the closest thing to a "metric/positivity" in the corpus, but it is on the moduli of rank-1 bundles, **not** on an $H^1$ of the square, and CC do not use it as a polarization of an intersection form. **[DATA, via Doc 120; NOT VERIFIED in source this session that "polarization"/"positive form" appears as a term in 2602.15941 — Doc 120 §3.4 reports a negative search for "intersection theory"/"Hodge index" in that paper].**
- In **2006.13771** (archimedean positivity): there is a real **positivity** ($W_\infty(g*g^*)\ge0$ in the window), which CC themselves call the germ of "an intersection theory of divisors on the square of the Scaling Site" (Doc 120 §4.4). It is the closest thing to a definite form — but it is **analytic, at one place, on tests**, not a polarization of the algebraic $H^1$ of 2205.01391, and globalizing it is MW-6 (O_SL, Doc 121 §4.3). **[DATA, via Doc 120.]**

**Conclusion of the search:** it **confirms** the Doc 120 report: there is, in the CC corpus, no polarization (object↔dual positive isomorphism) on the $H^1$ that turns Pontryagin duality into a form with signature. The only candidate for "positivity" (2006.13771) is of a different nature (analytic, not the self-duality of the tolerance module) and RH-equivalent once globalized. **The ingredient the bit reveals as missing has no candidate.**

---

## 6. R-NC applied to this result

[COMPUTATION] The result of this document (a structural GAP and a request) is not a bridge proposal, so R-NC is applied to **Request 122.A** to ensure that, if Connes were to answer it, it would not be RH-in-disguise:
- **NC1 (externality):** Request 122.A is formulated entirely in $\Gamma\mathcal T_*$ and Arakelov divisors; it mentions neither $\zeta$ nor zeros. **PASSES.** (It is a statement about CC's category, not about L-functions.)
- **NC2 (overgeneration):** it requests self-duality for **every** self-dual divisor $2D=K$ and polarization as a property of the category, not of the object encoding $\zeta$ (which does not exist in dim 1). **PASSES** at its level (dim 1, far from zeros — the same verdict as Doc 121 §2.1.5 for crossing A).
- **NC3/NC4:** not evaluable in dim 1 (they do not individuate zeros); the risk is carried over entirely to the moment of repeating the mechanism on the square. Identical to Doc 121 §2.1.5.

Request 122.A is, therefore, a legitimate (non-circular) and cheap question for an expert in CC's formalism: it is a statement about their own definitions in §5.

---

## 7. Closing

No new geometric statement has been proved here. What has been **read in source** (raw text of §5 of 2205.01391) and **computed** is that: (i) $D_0=-\{2\}$ is an admissible divisor and an exact fixed point of $\sigma$ — crossing A does not die from inadmissibility; (ii) CC's duality is **Pontryagin** duality (character evaluation group↔dual), of a third kind distinct both from the cup product (alternating) and from Serre duality over a field (symmetrizable); (iii) therefore the "symmetry character" **is not defined** for it without an external polarization; (iv) at $D_0$ both $H^\bullet$ vanish, so the pointwise computation is vacuous (F-A4). The bit of 121.E is a **structural GAP**, and the exact datum to ask Connes is **Request 122.A**: a self-duality isomorphism $H^1(D)\cong\widehat{H^1(D)}$ at the self-dual point and a positive polarization on it — the analogue of the Lefschetz/Hodge operator, for which the entire CC corpus has no candidate.

For the program: the outcome is the worst of the three outcomes of 121.E for R-SIG, and at the same time the most informative. What is missing is not "choosing between symmetric or alternating duality" but **building the category of forms** (a polarization of the tolerance module's $H^1$) that CC do not have. Phase 40 must, consequently: (a) NOT expect a signature from the pointwise crossing A; (b) redirect crossing A to its **degeneration/jump** version around $D_0$ (bridge with crossing D, Picard monoid, §3); (c) keep Request 122.A as the internal-to-CC statement that an expert in $\Gamma\mathcal T_*$ can decide, and whose positive answer (if $j_D$ exists with $\varepsilon$ and positivity) would reopen the duality→signature path — this time with the correct ingredient identified.

---

## References

**Primary source read this session:** A. Connes, C. Consani, *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$*, arXiv:2205.01391 (PDF, via `pdftotext`): §1 (eqs. (1.3)–(1.6)), §2 (cohomologies $H^0,H^1$), §4 (Prop. 4.1, eq. (1.5)), §5 "Duality" (eq. (5.11), Lemma 5.1, Prop. 5.2(i)–(ii) eqs. (5.8)–(5.10), Thm. 5.3, eq. (5.12)), Appendix A (tolerance relations: "reflexive and symmetric relation").

**Internal (backward-only):** Doc 119 (R-SIG realizations (i)/(ii)/(iii); R-NC); Doc 120 (CC inventory; §3.2, §4.4, §7.7); Doc 121 (crossing A; Conjecture 121.A steps 1–5; falsifiers F-A1..F-A4; Problem 121.E; §2.1.5 R-NC of crossing A; §4.2 scenario −1 ⟹ polarization).

**Classical (context, via Doc 119/121, not re-verified this session):** Pontryagin duality of locally compact abelian groups (reflexivity $A\cong\widehat{\widehat A}$); Hodge–Riemann / Lefschetz operator as the polarization that turns Poincaré duality into a form with signature; Mumford (1971), Atiyah (1971) on the parity of theta characteristics (the −1/Arf outcome NOT reached here).

*End of Doc 122.*
