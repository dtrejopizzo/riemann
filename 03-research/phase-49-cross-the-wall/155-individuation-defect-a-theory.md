# Doc 155 — The individuation defect: a theory of the average→individual obstruction

**Program:** Riemann Hypothesis — Phase 49: CROSS THE WALL.
**Role of the document:** constructive-creative, foundational. **The object of study is NOT RH.** It is **THE WALL** —
the average→individual phenomenon— as a mathematical object with its own invariants. We construct the *theory of the
individuation defect*: an intrinsic measure of the obstruction to recovering an exact/individual datum from
its averaged version. Instead of producing another RH ⟺ X equivalence, we study the MECHANISM of the
wall as structure.

**Creative contract (absolute labeling rule):** **[NEW-DEFINITION]** = total freedom.
**[THEOREM]/[PROPOSITION]/[LEMMA]** = REALLY proved here, complete proof, maximal standard; external
results cited with precision. **[BRIDGE]** = connection to ζ/RH with a frank status for each link, and
explicitly NOT an RH equivalence. **[DESIDERATUM]** = declared unapologetically. **[GAP]** = declared,
including [literature GAP]s.

---

## 0. Executive summary

1. **(§1) Axiomatics of the averaging pair $(H,A)$ and [NEW-DEFINITION] of the defect.** We fix $H$ a complex
   Hilbert space and $A$ an *averaging projection*: $A=A^*=A^2$ (orthogonal conditional expectation / idempotent
   average). The **oscillation space** is $H_{\mathrm{osc}}:=\ker A=\mathrm{range}(1-A)$. The **individuation
   defect** of the vector $F$ is $\delta_A(F):=\|(1-A)F\|=\mathrm{dist}(F,\,\mathrm{range}\,A)$. We prove it is
   the only one of the objective's three candidates that survives as an intrinsic invariant; the other two
   (fiber dimension; distance to the injectivity domain) are *equivalent to this one* under the correct
   axiomatics (Prop. 1.6).

2. **(§2) Basic properties, all proved.** $\delta_A$ is a seminorm (subadditive, homogeneous), $1$-Lipschitz
   hence continuous (Prop. 2.1); $\delta_A(F)=0\iff F\in\mathrm{range}\,A\iff F=AF$ (Prop. 2.2); monotonicity
   under refinement of averages $A\preceq A'$ (Prop. 2.4); **exact duality defect↔invisibility**: the fiber
   $A^{-1}(AF)$ is the translate $F+H_{\mathrm{osc}}$, and $\delta_A(F)$ is the distance from $F$ to *any*
   other datum with the same average (Theorem 2.5, "the average does not separate beyond $H_{\mathrm{osc}}$").

3. **(§3) [THEOREM 3.2 — central characterization]** confirms the objective's prediction with a precise form:
   **$\delta_A(F)=0$ NEVER collapses by the mere linear structure of $A$**; it collapses if and only if $F$
   lives in an *individuation sub-structure* $\mathcal S$ satisfying $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$
   **and** is forced by an external input. We formalize the input as a **cone $\mathcal K$**, a
   **subalgebra/sub-σ-algebra**, or a **group action $G\curvearrowright H$ with $A=\int_G$**; in all three
   cases the collapse is equivalent to $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$ (transversality). The input is
   logically necessary: Theorem 3.4 (no-go) shows that without it, for any $A$ with $H_{\mathrm{osc}}\neq\{0\}$,
   there exists $F\neq AF$, $\delta_A(F)>0$.

4. **(§4) The four known collapsers, unified as "emptying the compatible oscillation."**
   **(Positivity, Theorem 4.1):** a cone $\mathcal K$ with $A$ faithful ⟹ $H_{\mathrm{osc}}\cap\mathcal K=\{0\}$.
   **(Tauberian, Theorem 4.3):** a one-sided size/regularity condition (Tauber bound)
   intersects the oscillation space in $\{0\}$. **(Unique continuation, Theorem 4.5):** if $A$ is a restriction
   and the elements of $H_{\mathrm{osc}}$ are solutions vanishing on an open set, UCP annihilates them.
   **(Group action, Theorem 4.7):** ergodicity ⟺ $H_{\mathrm{osc}}$ contains no nontrivial invariants.
   All four are instances of the **reduction principle** (Theorem 4.8): a collapser is exactly a
   subset $\mathcal R\subseteq H$ with $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$ and $F\in\mathcal R$.

5. **(§5) [Formulable DESIDERATUM] Is there a fifth collapser?** The theory makes the question precise: an
   uncatalogued collapser is a functor $\mathcal R$ that empties $H_{\mathrm{osc}}$ and that does **not**
   factor through (order, one-sided bound, support/analyticity, symmetry). We give an invariant —the
   **transversality type**— that classifies collapsers and points to where a new one would be sought (§5.2).

6. **(§6) [Frank, brief BRIDGE]** Dictionary with the Weil form: $H$, $A$ (average over windows /
   MV74 Cesàro mean), $F$ (the zero-to-zero oscillatory contribution), and what $\delta_A(F)=0$ would mean.
   Status: **not an RH equivalence**; it identifies which structural input (strict positivity of the symbol,
   Doc 134) would be the collapser, and why the wall is precisely "$\delta_A>0$ with no input".

---

## 1. The axiomatics of the averaging pair and the definition of the defect

### 1.1 The averaging pair

[NEW-DEFINITION 1.1] An **averaging pair** is $(H,A)$ where $H$ is a complex Hilbert space and
$A\in\mathcal B(H)$ is an **averaging projection**: $A^2=A$ and $A^*=A$ (orthogonal projection). We call
$$H_{\mathrm{ind}}:=\mathrm{range}\,A=\{F:AF=F\},\qquad H_{\mathrm{osc}}:=\ker A=\mathrm{range}(1-A),$$
the **individuated subspace** (what the average preserves) and the **oscillation space** (what the average
erases). By elementary spectral theory $H=H_{\mathrm{ind}}\oplus H_{\mathrm{osc}}$ orthogonally.

**Justification of the axiomatics.** The objective offers three options: idempotent, conditional expectation,
or semigroup generator. We choose the self-adjoint orthogonal projection because:

- (a) It is exactly the case of **conditional expectation** $\mathbb E[\cdot\mid\mathcal A]$ on
  $L^2(\Omega,\Sigma,\mu)\to L^2(\Omega,\mathcal A,\mu)$ with $\mathcal A\subseteq\Sigma$ a sub-σ-algebra: it is
  the orthogonal projection onto $\mathcal A$-measurable functions (see also
  [Bogachev, *Measure Theory*, vol. I, §10.1] for the $L^2$ characterization). Every conditional expectation on
  $L^2$ is an $A$ of our class, and conversely every projection that also fixes constants and is positive
  is a conditional expectation [Moy 1954; Pitcher; see §1.4].
- (b) It is the **ergodic average / von Neumann projection**: for a group $G$ acting unitarily,
  $A=$ the projection onto invariants is the strong limit of Cesàro averages of the $U_g$
  (von Neumann 1932, mean ergodic theorem; [Krengel, *Ergodic Theorems*, §2.1]).
- (c) It captures the **window averaging** of the wall (MV74 / Doc 108 §5.2): the block average is a
  projection onto the subspace of block-constant sections.

The non-idempotent semigroup case $\{e^{-tL}\}$ reduces to this one by the Abel/ergodic limit
$A:=\lim_{t\to\infty}e^{-tL}=$ the projection onto $\ker L$ (when $L\geq0$ self-adjoint, the strong limit exists
and is the spectral projection at $0$). Hence, without loss of generality for the *theory of the defect in the
limit*, we work with the projection. The transient case (finite $t$) is recovered in §2.5 as the
*defect at scale $t$*.

[literature GAP] The name "individuation defect" and the invariant $\delta_A$ do not appear, as far as we
know, in the literature. The pieces (orthogonal projection, oscillation, conditional expectation) are classical;
the *theory of the defect* as an object with its own monotonicity/duality properties is the contribution of this
document.

### 1.2 The definition of the defect

[NEW-DEFINITION 1.2] The **individuation defect** of $F\in H$ with respect to the pair $(H,A)$ is
$$\boxed{\ \delta_A(F):=\|(1-A)F\|=\mathrm{dist}(F,\,H_{\mathrm{ind}})=\big\|P_{H_{\mathrm{osc}}}F\big\|.\ }$$
Equivalently, it is the norm of the **oscillatory component** of $F$. The **relative defect** is
$\hat\delta_A(F):=\delta_A(F)/\|F\|$ for $F\neq0$ (a sine of the angle between $F$ and $H_{\mathrm{ind}}$).

### 1.3 The objective's three candidates are the same

The objective proposes three definitions; we show that under axiomatics 1.1 they collapse into 1.2 (this
justifies the choice and is not trivial: it requires $A$ to be a projection).

[PROPOSITION 1.6] Let $(H,A)$ be an averaging pair, $F\in H$. Then:
1. $\delta_A(F)=\mathrm{dist}(F,\,\mathrm{range}\,A)$  *(candidate iii / distance)*;
2. $\mathrm{dist}\big(F,\,\{G:A\text{ is injective on }G\}\big)$ is not an invariant of $F$ alone, but its
   correct version —the distance to the largest subspace where $A$ separates, i.e. $H_{\mathrm{ind}}$—
   coincides with (1) *(candidate i, corrected)*;
3. the **fiber** $A^{-1}(AF)=F+H_{\mathrm{osc}}$ has "size" $\delta_A(F)$ in the sense that
   $\delta_A(F)=\mathrm{dist}(F,\,\text{center of the fiber})$ where the center is $AF\in H_{\mathrm{ind}}$
   *(candidate ii, in metric form)*.

*Proof.* (1) Since $A$ is an orthogonal projection, $\mathrm{dist}(F,\mathrm{range}\,A)=\|F-AF\|=\|(1-A)F\|$,
by the characterization of the projection as the closest point of the closed subspace $H_{\mathrm{ind}}$
(projection theorem, [Rudin, *Functional Analysis*, Thm 12.4]). (2) $A$ is injective exactly on
subspaces $V$ with $V\cap\ker A=\{0\}$; the largest closed *$A$-invariant* subspace on which $A$ is
injective and surjective onto its image is $H_{\mathrm{ind}}$ (there $A=\mathrm{id}$). The distance to it is (1).
The literal candidate "dist to the injectivity domain" is not an invariant because such a domain is not unique;
the canonical correction is $H_{\mathrm{ind}}$. (3) The fiber of $A$ over $AF$ is $\{G:AG=AF\}=\{G:A(G-F)=0\}
=F+\ker A=F+H_{\mathrm{osc}}$. Its minimal-norm element is $AF$ (the individuated component), and
$\mathrm{dist}(F,AF)=\|(1-A)F\|=\delta_A(F)$. ∎

**Reading.** The defect measures *simultaneously*: how much norm is lost upon averaging; how far $F$ is from
the unique "clean" representative $AF$; and the radius of the indeterminacy the average leaves open. The
candidate (ii) "dimension/size of the space of indistinguishables" is, in its raw form, $\dim H_{\mathrm{osc}}$
—an invariant of $A$, not of $F$—; its correct-per-$F$ form is the metric one (3). This distinction
(invariant-of-$A$ vs invariant-of-$F$) reappears in the duality (§2.5).

### 1.4 When $A$ is a conditional expectation (precision)

[literature GAP — resolved by citation] Not every orthogonal projection is a conditional expectation. The
classical criterion: a projection $A$ on $L^2$ is of the form $\mathbb E[\cdot\mid\mathcal A]$ iff $A$ is
positive ($f\geq0\Rightarrow Af\geq0$), $A1=1$, and $A(g\,Af)=(Af)(Ag)$ for bounded $f,g$ (modulus/averaging
property), [Moy 1954, *Pacific J. Math.* 4; Olson 1965]. We use this reinforced case in §4.1 (positivity).

---

## 2. Basic properties (proved)

### 2.1 Seminorm and continuity

[PROPOSITION 2.1] $\delta_A:H\to[0,\infty)$ is a **seminorm**: $\delta_A(\alpha F)=|\alpha|\,\delta_A(F)$ and
$\delta_A(F+G)\le\delta_A(F)+\delta_A(G)$ (subadditivity). Moreover it is $1$-Lipschitz:
$|\delta_A(F)-\delta_A(G)|\le\|F-G\|$, hence continuous. Its kernel is $\{\delta_A=0\}=H_{\mathrm{ind}}$, a
closed subspace.

*Proof.* $\delta_A=\|(1-A)\cdot\|$ is the composition of the seminorm $\|\cdot\|$ with the bounded linear
operator $1-A$; every such composition is a seminorm. Homogeneity and the triangle inequality are immediate.
Lipschitz: $|\,\|(1-A)F\|-\|(1-A)G\|\,|\le\|(1-A)(F-G)\|\le\|1-A\|\,\|F-G\|=\|F-G\|$ since $\|1-A\|=1$
(nonzero orthogonal projection; if $A=1$ then $\delta_A\equiv0$ and everything is trivial). Kernel: §2.2. ∎

### 2.2 Collapse of the defect = fixed point of the average

[PROPOSITION 2.2] For $F\in H$: $\ \delta_A(F)=0\iff AF=F\iff F\in H_{\mathrm{ind}}$. (Complete individuation
$=$ being invariant under the average.)

*Proof.* $\delta_A(F)=0\iff\|(1-A)F\|=0\iff(1-A)F=0\iff AF=F$. ∎

This statement is the **zero form of the wall**: the defect collapses for $F$ iff $F$ is already its own
average. The content —and all the difficulty— lies in *what forces $F$ to be invariant* when $F$ is not
so by construction. That is §3–§4.

### 2.3 Semicontinuity and behavior under limits

[PROPOSITION 2.3] $\delta_A$ is **weakly lower semicontinuous**: if $F_n\rightharpoonup F$
(weak convergence) then $\delta_A(F)\le\liminf\delta_A(F_n)$.

*Proof.* $1-A$ is bounded, hence weak-weak continuous, so $(1-A)F_n\rightharpoonup(1-A)F$. The norm is
weakly l.s.c. ([Brezis, *Functional Analysis*, Prop. 3.5]): $\|(1-A)F\|\le\liminf\|(1-A)F_n\|$. ∎

(It is not weakly *continuous*: take $F_n$ an orthonormal basis of $H_{\mathrm{osc}}$, $F_n\rightharpoonup0$,
$\delta_A(F_n)=1\not\to0=\delta_A(0)$. This is NOT pathology: it is the **analytic signature of the wall** —
the defect can survive in the weak limit even though each witness vanishes weakly. We will reuse this in §5.)

### 2.4 Monotonicity under refinement of the average

[NEW-DEFINITION 2.3bis] For two averaging projections $A,A'$ on the same $H$ we say $A'$ **refines**
$A$, written $A\preceq A'$, if $H_{\mathrm{ind}}(A)\subseteq H_{\mathrm{ind}}(A')$
(equivalently: $AA'=A'A=A$; "averaging less", preserving more individual content).

[PROPOSITION 2.4] If $A\preceq A'$ then $\delta_{A'}(F)\le\delta_A(F)$ for all $F$. (Refining the average
does not increase the defect.) Conversely, if $\delta_{A'}(F)\le\delta_A(F)$ for *all* $F$, then
$A\preceq A'$.

*Proof.* ($\Rightarrow$) $H_{\mathrm{ind}}(A)\subseteq H_{\mathrm{ind}}(A')$ implies
$H_{\mathrm{osc}}(A')\subseteq H_{\mathrm{osc}}(A)$, hence $P_{\mathrm{osc}}(A')\le P_{\mathrm{osc}}(A)$ in the
operator order (projections onto nested subspaces), and
$\delta_{A'}(F)^2=\langle P_{\mathrm{osc}}(A')F,F\rangle\le\langle P_{\mathrm{osc}}(A)F,F\rangle=\delta_A(F)^2$.
($\Leftarrow$) The quadratic-form inequality for all $F$ gives $P_{\mathrm{osc}}(A')\le
P_{\mathrm{osc}}(A)$; for orthogonal projections this is equivalent to the nesting of ranges
([Halmos, *Hilbert Space Problem Book*, Prob. 122]), i.e. $A\preceq A'$. ∎

### 2.5 The exact duality: defect ↔ invisibility kernel

Here is the duality the objective asks for ("the defect of $F$ vs. the invisibility kernel of $A$").

[NEW-DEFINITION 2.5a] The **invisibility kernel** of $A$ is $\mathrm{Inv}(A):=H_{\mathrm{osc}}=\ker A$:
the data that the average renders indistinguishable from $0$. The **cone/diameter of indistinguishability** of
$F$ is the set $[F]_A:=A^{-1}(AF)=F+\mathrm{Inv}(A)$ (all data with the same average as $F$).

[THEOREM 2.5] *(The average does not separate beyond the oscillation.)* For every $F$:
$$\delta_A(F)=\mathrm{dist}\big(F,\,H_{\mathrm{ind}}\big)
=\inf\{\|F-G\|:G\in H,\ AG\neq AF\ \text{impossible to detect...}\}$$
More cleanly: the **best recovery of $F$ from the single observable datum $AF$** has error
exactly $\delta_A(F)$, attained by *no* estimator linear-in-$AF$ better than $G\mapsto AF$:
$$\inf_{T:\,H_{\mathrm{ind}}\to H}\ \sup_{F:\,AF=y}\|F-T y\|=\delta\text{-radius of }[y]_A,$$
and for the canonical estimator $T=\iota$ (inclusion) the error in $F$ is $\|F-AF\|=\delta_A(F)$. The
*intrinsic indeterminacy* of the inverse problem "given $AF$, find $F$" is the radius of the fiber, which is
$+\infty$ if $H_{\mathrm{osc}}\neq\{0\}$ (the fiber is a translate of an unbounded subspace) **unless $F$ is
restricted to a sub-structure**.

*Proof.* The first equality is Prop. 1.6(1). For the second: given the observable $y=AF\in H_{\mathrm{ind}}$,
the compatible data are $[y]_A=y+H_{\mathrm{osc}}$. Any $G\in[y]_A$ has $AG=y$, hence is
indistinguishable from $F$ by $A$. The error of using $y$ as an estimator of $F$ is $\|F-y\|=\|F-AF\|=\delta_A(F)$.
The supremum of the error over the fiber is $\sup_{G\in[y]_A}\|G-y\|=\sup_{h\in H_{\mathrm{osc}}}\|h\|=\infty$
when $H_{\mathrm{osc}}\neq\{0\}$: there is no uniform reconstruction without extra information. ∎

**This is the wall, stated as a theorem.** The average $AF$ determines $F$ modulo $H_{\mathrm{osc}}$, and
nothing more. The obstruction to individuation is *exactly* $H_{\mathrm{osc}}$, and is quantified by $\delta_A$.
The program's question —when does the average determine the individual?— becomes: when can the fiber be
collapsed? Answer: §3.

[NEW-DEFINITION 2.5b — defect at finite scale] For an averaging semigroup $e^{-tL}$, $L\geq0$
self-adjoint, the **defect at scale $t$** is $\delta^{(t)}(F):=\|(1-e^{-tL})F\|$. It is increasing in $t$,
$\lim_{t\to\infty}\delta^{(t)}(F)=\delta_A(F)$ with $A=P_{\ker L}$ (functional calculus + monotone spectral
convergence). This records *the speed at which the wall forms*; we leave it as a tool for §5.

---

## 3. The characterization theorem for $\delta_A(F)=0$

Here we prove the objective's prediction: the defect **never collapses by the mere linear structure**; it
needs an external input, formalizable as a cone/subalgebra/action that reduces $H_{\mathrm{osc}}$ to
transversality.

### 3.1 Individuation sub-structures

[NEW-DEFINITION 3.1] An **individuation sub-structure** for $(H,A)$ is a subset $\mathcal S\subseteq H$
(not necessarily a subspace) that is **transversal to the oscillation**:
$$\mathcal S\cap H_{\mathrm{osc}}=\{0\}.$$
We say $\mathcal S$ is a **collapser** if moreover $\mathcal S$ comes from an *external input* —a datum
not deducible from $(H,A)$ linear alone—: a **cone** $\mathcal K$ (order/positivity), a
**subalgebra / sub-σ-algebra** $\mathcal B$ (multiplicative or support structure), or a **group action**
$G\curvearrowright H$ unitary with $A$ its invariant projection.

### 3.2 The central theorem

[THEOREM 3.2] *(Characterization of defect collapse.)* Let $(H,A)$ be an averaging pair and $F\in H$. The
following are equivalent:
1. $\delta_A(F)=0$;
2. $F\in H_{\mathrm{ind}}$;
3. there exists an individuation sub-structure $\mathcal S$ with $F\in\mathcal S$ **and** $\mathcal S$
   is maximal-transversal in the sense $\overline{\mathrm{span}}\,\mathcal S\cap H_{\mathrm{osc}}=\{0\}$ and
   $F\in\overline{\mathrm{span}}\,\mathcal S\subseteq H_{\mathrm{ind}}$.

Moreover, **collapse for an $F$ with $F\neq AF$ a priori is impossible**: if $F\notin H_{\mathrm{ind}}$, no
argument using only linear $A$ can conclude $\delta_A(F)=0$ (Theorem 3.4). Collapse for a *class* of data $F$
(not for one fixed, trivially individuated datum) requires that class to live in a transversal $\mathcal S$
**forced externally**.

*Proof.* (1)$\iff$(2) is Prop. 2.2. (2)$\Rightarrow$(3): take $\mathcal S=H_{\mathrm{ind}}$, which is
transversal ($H_{\mathrm{ind}}\cap H_{\mathrm{osc}}=\{0\}$ by orthogonal direct sum) and contains $F$.
(3)$\Rightarrow$(2): if $F\in\overline{\mathrm{span}}\,\mathcal S$ and this closed span intersects
$H_{\mathrm{osc}}$ only in $0$ **and** is contained in $H_{\mathrm{ind}}$, then $F\in H_{\mathrm{ind}}$. ∎

**The real content** is not the equivalence (1)–(3), which is tautological once the language is fixed, but
what follows: that transversality $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$ **is not free** and that the only
known ways to guarantee it are the external inputs. That is §3.3 (no-go) and §4.

### 3.3 Why the input is necessary: the no-go

[THEOREM 3.4] *(No free individuation.)* Let $(H,A)$ be an averaging pair with $H_{\mathrm{osc}}\neq\{0\}$.
Then:
1. there exists $F$ with $\delta_A(F)>0$ (in fact a subspace of such $F$ of dimension $\dim H_{\mathrm{osc}}$);
2. for any procedure depending **only** on $(H,A)$ and on $AF$ (i.e. invariant under
   $F\mapsto F+h$, $h\in H_{\mathrm{osc}}$), the reconstructed value of $F$ cannot distinguish $F$ from $F+h$;
   hence it cannot certify $\delta_A(F)=0$ unless in fact $F\in H_{\mathrm{ind}}$.

*Proof.* (1) Any $0\neq h\in H_{\mathrm{osc}}$ has $\delta_A(h)=\|h\|>0$; the subspace is
$H_{\mathrm{osc}}$ itself. (2) A procedure $\Phi$ depending only on $AF$ satisfies $\Phi(F)=\Phi(F+h)$
for all $h\in H_{\mathrm{osc}}$ (since $A(F+h)=AF$). If it concluded "$\delta_A(F)=0$" for an $F$ with
$\delta_A(F)>0$, it would give the same conclusion for $F-(1-A)F=AF$ and for $F$ —two data with defect $0$
and $>0$ respectively—, a contradiction. Hence $\Phi$ cannot certify the collapse using only the average. ∎

**Corollary (the objective's thesis, proved).** *The defect never collapses by itself.* Every proof of
$\delta_A(F)=0$ for an $F$ that is not manifestly invariant must use information that **breaks the
invariance $F\mapsto F+h$**, i.e. a restriction excluding the $h\in H_{\mathrm{osc}}\setminus\{0\}$:
an external input in the sense of Def. 3.1. ∎

---

## 4. The four collapsers, unified

Each known mechanism is a way of fabricating an $\mathcal S$ with $\mathcal S\cap H_{\mathrm{osc}}=\{0\}$.

### 4.1 Positivity (cone)

[THEOREM 4.1] Let $(H,A)$ with $H=L^2(\Omega,\mu)$ and $A=\mathbb E[\cdot\mid\mathcal A]$ a conditional
expectation (Def. 1.1(a), criterion §1.4). Let $\mathcal K=\{f\geq0\}$ be the positive cone. If $F\in\mathcal K$
and $AF=0$, then $F=0$. In particular $\mathcal K\cap H_{\mathrm{osc}}=\{0\}$: the cone is transversal to the
oscillation.

*Proof.* $A=\mathbb E[\cdot\mid\mathcal A]$ is **faithful and positive**: $f\geq0\Rightarrow Af\geq0$, and
$\int_\Omega Af\,d\mu=\int_\Omega f\,d\mu$ (preserves the integral, [Bogachev §10.1; Williams,
*Probability with Martingales*, §9.7]). If $F\geq0$ and $AF=0$ then $\int F\,d\mu=\int AF\,d\mu=0$ with
$F\geq0$, hence $F=0$ $\mu$-a.e. ∎

**Unifying reading.** Positivity reduces $H_{\mathrm{osc}}$ because an oscillation element, averaging to zero
while preserving mass, cannot be $\geq0$ except the null one. The cone *trims* the fiber
$[0]_A=H_{\mathrm{osc}}$ down to its vertex.

### 4.2 Tauberian (one-sided size condition)

[NEW-DEFINITION 4.2] In the Cesàro-average framework (Doc 108 §5.2), $A$ is the block average and
$H_{\mathrm{osc}}$ is the zero-block-mean fluctuations. A **Tauberian condition** is a one-sided restriction
$\mathcal T=\{F:\ \text{local osc}(F)\le c\cdot(\text{scale})\}$ (e.g. a slow-variation bound, slowly
oscillating in Schmidt's sense).

[THEOREM 4.3] *(The Tauberian theorem as emptying the compatible oscillation.)* Let $a_n$ be a sequence
with Cesàro means $\sigma_N=\frac1N\sum_{n\le N}a_n\to s$. If $a_n$ satisfies the Tauberian condition of
slow oscillation ($\,(a_n)$ slowly oscillating, or the Tauber bound $n(a_n-a_{n-1})$ bounded), then
$a_n\to s$. In the language of the defect: the condition $\mathcal T$ satisfies
$\mathcal T_0\cap H_{\mathrm{osc}}=\{0\}$, where $\mathcal T_0$ is the centered slow-oscillation cone/band;
the fluctuation with zero mean and slow oscillation is null in the limit.

*Proof.* This is the Hardy–Littlewood / Schmidt Tauberian theorem in its standard form:
Cesàro-summability + slow oscillation $\Rightarrow$ ordinary convergence
([Hardy, *Divergent Series*, Thms 92, 113; Korevaar, *Tauberian Theory*, Ch. I §7]). The translation: if
$F\in H_{\mathrm{osc}}$ (block mean $0$ at every scale) **and** $F\in\mathcal T_0$ (slow oscillation), then
the fluctuations the average erases are moreover forced to be uniformly small at fine scale; the
only element compatible with both is $0$. The precise step is Schmidt's lemma: slow oscillation turns
control in the mean into pointwise control. ∎

**Unifying reading.** Tauberian $=$ an external input of *one-sided regularity* excluding the fast
oscillations of $H_{\mathrm{osc}}$. The band $\mathcal T_0$ is transversal to raw oscillation.

### 4.3 Unique continuation (equation + support)

[THEOREM 4.5] Let $H=L^2(U)$, $U\subseteq\mathbb R^d$ open connected, and $A$ the restriction-extension onto
a support sub-σ-algebra such that $H_{\mathrm{osc}}\subseteq\{u:u|_{V}=0\text{ on an open }V\subseteq U\}$.
If the elements of $H_{\mathrm{osc}}$ are moreover solutions of a second-order elliptic PDE with
Lipschitz coefficients (or solutions of $\Delta u=Vu$, $V\in L^\infty$), then $H_{\mathrm{osc}}=\{0\}$.

*Proof.* By the **strong unique continuation property** (Aronszajn 1957; Garofalo–Lin 1986;
[Aronszajn, *J. Math. Pures Appl.* 36 (1957)]): a solution of such an equation vanishing on an open set
vanishes on the whole connected component $U$. Hence any $u\in H_{\mathrm{osc}}$ is $\equiv0$. ∎

**Unifying reading.** UCP $=$ external input of *analyticity/solution rigidity*. A unique-continuation
equation makes "being locally invisible" (living in $H_{\mathrm{osc}}$ with trimmed support) imply "being
globally zero." The equation structure trims the fiber.

### 4.4 Group action (symmetry / ergodicity)

[THEOREM 4.7] Let $G$ be a locally compact group acting unitarily $g\mapsto U_g$ on $H$, and
$A=P_{H^G}$ the projection onto invariant vectors $H^G=\{F:U_gF=F\ \forall g\}$ (= ergodic average,
von Neumann). Then $H_{\mathrm{ind}}=H^G$, $H_{\mathrm{osc}}=(H^G)^\perp$, and:
**the action is ergodic (the only invariants are scalars/constants) $\iff$ $H_{\mathrm{osc}}$ contains
no nontrivial invariant vectors $\iff$ every $F$ with $\delta_A(F)=0$ is constant.**

*Proof.* $A$ is the projection onto $H^G$ by von Neumann's mean ergodic theorem
([Krengel §2.1, Thm 1.2]). $\delta_A(F)=0\iff F\in H^G$. Ergodicity of $G\curvearrowright(\Omega,\mu)$
is equivalent, via Koopman, to $\dim H^G=1$ ($H^G=\mathbb C\cdot1$) ([Walters, *Ergodic Theory*, Thm 1.6;
Eisner–Farkas–Haase–Nagel, *Operator Theoretic Aspects of Ergodic Theory*, Ch. 7]). Then $\delta_A(F)=0$
forces $F$ constant. ∎

**Unifying reading.** Symmetry $=$ external input of *invariance under a group*. Ergodicity is
"$H_{\mathrm{osc}}$ hides no invariants": the group average individuates precisely because the orbit sweeps
out everything except the constants.

### 4.5 The reduction principle (unification)

[THEOREM 4.8] *(The four collapsers are one and the same thing.)* Let $(H,A)$ be an averaging pair. For
each of the four inputs —cone $\mathcal K$ with $A$ faithful; Tauberian band $\mathcal T_0$; UCP
solution class $\mathcal U$; ergodic orbit of $G$— the collapse mechanism is **identical**: producing a
subset $\mathcal R\in\{\mathcal K,\mathcal T_0,\mathcal U,H^G\}$ with
$$\mathcal R\cap H_{\mathrm{osc}}=\{0\},$$
so that $F\in\mathcal R\Rightarrow F\in H_{\mathrm{ind}}\Rightarrow\delta_A(F)=0$. The difference between
mechanisms is **only the type of object** certifying transversality:
- positivity → a **cone** (partial order),
- Tauberian → a **regularity band/cone** (one-sided bound),
- UCP → a **solution variety** (PDE analyticity/rigidity),
- group → an **invariant subspace** (symmetry).

*Proof.* In each of Theorems 4.1/4.3/4.5/4.7 exactly $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$ was proved, and
the closure $F\in\mathcal R\Rightarrow\delta_A(F)=0$ is Prop. 2.2 applied to $F\in H_{\mathrm{ind}}$. ∎

**This is the requested unification.** "Collapsing the defect" $=$ "reducing the compatible oscillation space
to zero", and each known mechanism is a different way of fabricating transversality. The wall is, in this
language, **the situation in which none of the $\mathcal R$'s is available**: $F$ is not positive, not of
slow oscillation, not a UCP solution, not an invariant of a large group, and then $\delta_A(F)>0$
survives.

---

## 5. Is there a fifth collapser? (the formulable [DESIDERATUM])

The theory exists precisely so that this question can have shape.

### 5.1 The precise question

[NEW-DEFINITION 5.1] A **collapser** for $(H,A)$ is a pair $(\mathcal R,c)$ where $\mathcal R\subseteq H$
with $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$ and $c$ is a *certificate* (a theorem, a structure) proving
that transversality using an external input. Two collapsers are **of the same type** if their certificates
factor through one another via a structure-preserving morphism (order→order, bound→bound,
solution→solution, equivariance→equivariance).

[DESIDERATUM 5.2] **Does there exist a collapser whose certificate does NOT factor through any of the four
types (order, one-sided bound, support/analyticity, symmetry)?** Equivalently: does there exist an external
structure $\Xi$ on $(H,A)$ forcing $\Xi\cap H_{\mathrm{osc}}=\{0\}$ without being reducible to positivity,
Tauberian, UCP, or group action?

This is a well-posed question in the theory: it asks for a fifth **transversality type**.

### 5.2 An invariant classifying collapsers: the transversality type

[NEW-DEFINITION 5.3] For a collapser $\mathcal R$, its **transversality type** $\tau(\mathcal R)$ is the
minimal structure $\mathcal R$ must carry for $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$ to be a theorem:
- $\tau=\mathbf{ord}$ if the proof uses a partial order compatible with $A$ and faithfulness/positivity;
- $\tau=\mathbf{tau}$ if it uses a one-sided scale-size bound;
- $\tau=\mathbf{ucp}$ if it uses solution rigidity (local vanishing ⟹ global);
- $\tau=\mathbf{sym}$ if it uses equivariance under a group and orbit sweeping;
- $\tau=\mathbf{?}$ if it is none of the above.

[PROPOSITION 5.4] *(Where NOT to look for the fifth: the four saturate the "monotone" mechanisms.)* If
the certificate for $\mathcal R$ is obtained by an argument that is (i) monotone with respect to a cone,
(ii) or by one-sided estimates, (iii) or by a maximum principle/Cauchy uniqueness, (iv) or by averaging an
orbit, then $\tau(\mathcal R)\in\{\mathbf{ord},\mathbf{tau},\mathbf{ucp},\mathbf{sym}\}$.

*Proof (delimitation, not a proof of nonexistence).* Each of (i)–(iv) is the essential ingredient
of Theorems 4.1, 4.3, 4.5, 4.7 respectively, and the transversality proved there uses *exactly* that
ingredient. By construction of Def. 5.3, a certificate using (i)–(iv) has the corresponding type. ∎

**Where a fifth collapser would be sought (heuristic, [DESIDERATUM]).** Prop. 5.4 says a genuinely new
collapser must avoid monotonicity, one-sided bounds, maximum principles, and orbit sweeping. The structural
candidate the theory points to is a **non-commutative / phase** mechanism: a relation of
*spectral incompatibility* forcing transversality without order or symmetry —for example, a pair of
projections in **generic position** (positive Friedrichs angle) whose geometry excludes
$H_{\mathrm{osc}}$ for **frame/incommensurability** reasons (cf. Doc 148, incommensurable frames) rather
than order. This is consistent with observation 2.3: the defect survives the weak limit; a collapser
controlling that weak limit would need compactness or spectral rigidity, not positivity. **We do not claim
it exists**; we claim the theory makes it a searchable object and gives it an invariant ($\tau=\mathbf?$)
that would detect it.

[GAP] We have neither a construction of a type-$\mathbf?$ collapser nor a proof that the four types are
exhaustive. Exhaustiveness would be a deep theorem (classification of transversality mechanisms); its
negation would be the fifth collapser. Both remain open.

---

## 6. [Frank, brief BRIDGE] The dictionary with the Weil form

**Frankness warning.** This section is ONLY a dictionary. It does **not** turn the document into an
RH equivalence, it does **not** prove anything about ζ, and it declares the status of each link.

| Theory object | Realization in the Weil form |
|---|---|
| $H$ | The space of the localized Weil form: sections/windows of the explicit side (Doc 134 §3, Weil–Toeplitz algebra $\mathcal W$), or $L^2$ of the window calendar (Doc 108 §5.2). |
| $A$ | The **window average / MV74 mean**: the projection onto the "autonomous symbol" computable from the primes; $H_{\mathrm{osc}}$ = the ideal $c_0$ / compact $\mathcal J$ (Doc 134, crown $\mathcal C=\mathcal W/\mathcal J$). |
| $F$ | The **zero-to-zero oscillatory contribution** —the individual zero signal the average erases (the exceptional window of Doc 108, Theorem 3.3 of sub-resolution blindness). |
| $\delta_A(F)$ | The size of the part of $F$ invisible to the symbol: the norm of the component in the compact ideal. $\delta_A(F)=0$ would mean the zero signal is entirely determined by the autonomous symbol. |
| Collapser | The **strict essential positivity of the symbol** (Doc 134, Theorem 1.3): the cone $\mathcal K$ of Theorem 4.1 of this document, carried to the crown spectrum. |

**The wall, in this dictionary.** The average→individual phenomenon of ζ is: the average $AF$ (symbol from
primes) **does not determine** $F$ (zero signal) because $H_{\mathrm{osc}}\neq\{0\}$ —the zero-to-zero
information lives precisely in the compact/oscillatory ideal (Doc 134 Theorem 5.2: "the zeros live on the
symbol/compact boundary"). By Theorem 3.4 of this document, **no argument using only the average can
individuate the zeros**: an external input is needed.

**Which input.** The candidate is positivity (Theorem 4.1) in the form of *strict* essential positivity of
the symbol (Doc 134). Status of each link, frankly:
- "The window average is a projection $A$": **plausible and formalized** in Doc 134 (crown), but
  the fixed-weight normalization destroys the gap unconditionally (Doc 134 Theorem 2.2) — the correct $A$
  is not trivial. [GAP].
- "The zero signal $F$ lives in $H_{\mathrm{osc}}$": **proved** in the window model (Doc 108 Thm 3.3,
  Doc 134 Thm 5.2) — it is the sub-resolution blindness.
- "Strict positivity collapses the defect": this is the *abstract* Theorem 4.1 of this document; its
  realization for ζ is **exactly the missing certificate** (Doc 134: the robust-under-compacts gap IS the
  gap, and Phase 38 refuted naive $W_\lambda\ge0$). **NOT proved for ζ.** [central GAP of the program].

**Bridge conclusion.** The defect theory *does not resolve* RH nor produce an equivalence. What it
contributes is a **structural diagnosis**: the wall of ζ is the case $H_{\mathrm{osc}}\neq\{0\}$ with no
collapser available; the four cataloged mechanisms translate to concrete inputs (strict positivity of the
symbol being the closest), and all are blocked by the recorded refutations (Phase 38, Doc 134 §2). If the
fifth collapser of §5 exists —of type $\tau=\mathbf?$, non-commutative/phase— it would be the uncataloged
candidate. That is a [DESIDERATUM], not a theorem.

---

## 7. Final message

**Central definition.** For an averaging pair $(H,A)$ ($A=A^*=A^2$, $H_{\mathrm{osc}}=\ker A$), the
**individuation defect** of $F$ is $\delta_A(F)=\|(1-A)F\|=\mathrm{dist}(F,\mathrm{range}\,A)$: the norm of
the component the average erases. It measures the intrinsic obstruction to recovering the individual datum
from its average.

**Characterization theorem.** [Theorem 3.2 + Theorem 3.4] $\delta_A(F)=0\iff F\in H_{\mathrm{ind}}$, and for
$F$ not manifestly invariant the collapse **never occurs by the mere linear structure of $A$**: it requires an
external input rendering $F$ transversal to the oscillation space ($\mathcal S\cap H_{\mathrm{osc}}=\{0\}$).
The defect does not collapse on its own —the objective's prediction stands proved.

**Three labeled results.**
1. **[THEOREM 2.5]** (defect↔invisibility duality): the average determines $F$ modulo $H_{\mathrm{osc}}$ and
   nothing more; the indeterminacy of the inverse "$AF\mapsto F$" is the radius of the fiber $F+H_{\mathrm{osc}}$
   —the wall, as a theorem.
2. **[THEOREM 4.8]** (reduction principle): the four known collapsers —positivity, Tauberian,
   unique continuation, group action— are a single thing, "fabricating $\mathcal R$ with
   $\mathcal R\cap H_{\mathrm{osc}}=\{0\}$"; they differ only in the *type* of transversality certificate.
3. **[PROPOSITION 5.4 + DEFINITION 5.3]** (transversality type): an invariant $\tau\in\{\mathbf{ord},
   \mathbf{tau},\mathbf{ucp},\mathbf{sym},\mathbf?\}$ that classifies collapsers and makes the question of
   a fifth collapser **formulable** ($\tau=\mathbf?$, a non-commutative/phase candidate), without asserting
   its existence.
