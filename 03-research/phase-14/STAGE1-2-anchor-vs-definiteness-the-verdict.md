# Stages 1 & 2: does the Landau anchor survive the function-field test? — Verdict: it collapses, informatively

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
The audit authorized Stage 1 (formalize the framework ζ-free) and Stage 2 (test the anchor against the one
**proven** RH — function fields), for one purpose: decide whether the Landau anchor is a **genuinely new object**
or a sophisticated **renaming** of known machinery (self-adjointness, Weil positivity, Hodge, the pole). The audit
named the precise danger: that the function-field anchor turns out to be *"just the trivial cohomology class."*
**That is exactly what happened.** Below: Stage 1 (the object exists ζ-free, but its ceiling is the *edge*), Stage
2 (the one proven RH does **not** use a center-anchor; it uses a *definiteness* theorem), and the corrected
taxonomy that separates the two — which the framework had wrongly merged (the same over-reach as N8).

---

## Stage 1 — the framework is ζ-free, but it is classical edge-region machinery

**Theorem A (abstract, ζ-free).** Let $\nu\ge0$ be a measure on $(0,\infty)$ with abscissa of convergence
$\sigma_a$, and $F$ meromorphic of finite order with $\log F(s)=\int_0^\infty e^{-su}\,d\nu(u)$ for
$\Re s>\sigma_a$, with a pole of order $\rho\ge1$ at the Landau point $s=\sigma_a$, and a convexity budget
$\log|F(\sigma+it)|\le B(t)$. Let $P(\theta)=\sum_{k=0}^N a_k\cos k\theta\ge0$ with $a_0,a_1>0$. Then $F$ has no
zero $\beta+i\gamma$ with $\beta>\sigma_a-\dfrac{c(P,\rho)}{B(\gamma)}$.

*Proof is the de la Vallée Poussin argument with abstract data:* $\sum_k a_k\log|F(\sigma+ik\gamma)|=\int
e^{-\sigma u}P(\gamma u)\,d\nu\ge0$; the $k=0$ term is the anchor $a_0\log F(\sigma)\sim a_0\rho\log\frac1{\sigma-\sigma_a}$;
the partial-fraction term from a putative zero contributes $-a_1/(\sigma-\beta)$; the budget bounds the rest. $\square$

- **No "$\zeta$" appears in the statement.** So the anchor has **independent mathematical existence**: Stage 1's
  test is passed. ✅
- **But the statement is recognizably the classical zero-free-region theorem for Dirichlet series with
  non-negative coefficients** (the "$3+4\cos\theta+\cos2\theta$" technique, used for Dedekind/Rankin–Selberg
  $L$-functions). The "anchor $=$ Landau singularity" is a clean *conceptualization*, not new machinery.
- **Decisive limitation — the ceiling is the EDGE.** Theorem A's reach is $\asymp1/B(\gamma)$ *to one side of the
  abscissa* $\sigma_a$. The anchor sits at $\sigma_a$ (where $\nu$'s transform diverges, by Landau). **It produces
  only a shrinking edge region; it never reaches a fixed distance, let alone the center.** This is structural: a
  Landau singularity is *at the abscissa*, and there is no positive measure of arithmetic relevance whose abscissa
  is the critical line.

## Stage 2 — the one proven RH does NOT use a center-anchor (the cohomology/pole dictionary)

Take $C/\mathbb F_q$ a curve, $Z(C,T)=\dfrac{P_1(T)}{(1-T)(1-qT)}$, $P_1(T)=\prod_{i=1}^{2g}(1-\alpha_iT)$, and
$\zeta_C(s)=Z(C,q^{-s})$. The dictionary:

| object | cohomology | location in $s$ ($T=q^{-s}$) |
|---|---|---|
| pole at $T=1$ | $H^0$ (trivial) | $s=0$ |
| pole at $T=1/q$ | $H^2$ (trivial) | $s=1$ |
| **zeros** $\alpha_i$, $|\alpha_i|=\sqrt q$ | $H^1$ (primitive) | $\Re s=\tfrac12$ (this is RH) |

> **The Landau anchors of $\zeta_C$ — its poles — are at $s=0$ and $s=1$, coming from the TRIVIAL cohomology
> $H^0,H^2$.** There is **no anchor at $s=\tfrac12$.** Exactly as for $\zeta(s)$ (one pole, at $s=1$).

How is function-field RH actually proven (Weil)? On the surface $S=C\times C$, with the Néron–Severi intersection
form: the **Hodge index theorem** gives signature $(1,\rho-1)$ — the form is **negative-definite** on the
primitive part $\langle f_1,f_2\rangle^\perp$ (orthogonal to the two fiber classes $f_1,f_2$, $f_i^2=0$,
$f_1\!\cdot\!f_2=1$). Applied to the Frobenius graph, this negative-definiteness forces $|\alpha_i|=\sqrt q$.

- The **fiber classes $f_1,f_2$** — the positive/ample directions anchoring the hyperbolic plane — correspond
  precisely to $H^0,H^2$, i.e., to the **edge poles** at $s=0,1$. *The "anchor" in the geometric proof is the
  trivial cohomology — exactly the danger the audit flagged.*
- **RH (the center) is forced by the Hodge index theorem — a DEFINITENESS (signature) statement on $H^1$ — NOT by
  any singularity at the center.** The mechanism that reaches $\Re s=\tfrac12$ is the *negative-definiteness of a
  form*, a different kind of object than a Landau anchor.

## The corrected taxonomy (the framework had merged two distinct objects)

| mechanism | mathematical type | where it acts | gives | for $\zeta$? |
|---|---|---|---|---|
| **Landau anchor** (de la Vallée Poussin, Vinogradov–Korobov) | *singularity* of a positive-measure transform | the **edge** $\sigma_a$ | shrinking edge region | **present** (pole at $s=1$) |
| **Definiteness** (Hodge index, Weil positivity, self-adjointness) | *signature* of a form / operator | the **center** | RH | **absent/unproven** (the capstone) |

My earlier framework (§3 of the anchor document) listed Hilbert–Pólya / Weil / Hodge as *"anchors at $\sigma=\tfrac12$."*
**That was wrong — the same over-reach as N8.** They are **not** anchors (singularities); they are **definiteness**
statements. Stage 2 separates them cleanly: every true Landau anchor lives at the edge and is present for $\zeta$;
the object that actually reaches the center is a definiteness theorem, and *that* is what $\zeta$ lacks.

## Verdict on the bifurcation (the question Stages 1–2 were run to settle)

> **Q(anchor) is NOT a genuinely new object for RH. It collapses.** The anchor is the **trivial-cohomology edge
> pole**, present in both the number-field and function-field worlds; it is *not* the discriminator. The mechanism
> that proves RH where RH is proven is the **Hodge index theorem (a definiteness/signature theorem) on the surface
> $C\times C$** — which is **Weil positivity**, already audited as the capstone. The function-field test detected
> precisely the danger named: the geometric anchor is "just the trivial cohomology class."

So Q(anchor) joins the audited list — but, unlike a dead end, it **sharpens the wall to its exact geometric
content**:

> **The precise missing ingredient (the residue of value).** Not "an anchor at the center." It is a **Hodge index
> theorem on an arithmetic surface for $\operatorname{Spec}\mathbb Z$** — i.e., an object playing the role of
> $C\times C$ (a "$\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$"), carrying an
> intersection form whose **negative-definiteness on a primitive part** would force the zeros to $\Re s=\tfrac12$.
> The anchor (edge pole) is already there; what is missing is **the surface and its index theorem.** This is
> exactly the Connes–Consani / Deninger / Arakelov target — and it **is** Weil positivity, hence RH-equivalent
> (the capstone), now pinpointed not as "a missing positivity" in the abstract but as **a missing
> two-dimensional arithmetic geometry with a Hodge index theorem.**

## Honest status

- **Stage 1:** ✅ the anchor is ζ-free (Theorem A) — a real object — **but** it is classical positive-coefficient
  zero-free-region machinery, and its ceiling is the **edge**; it never reaches the center, structurally.
- **Stage 2:** ✅ the one proven RH uses a **definiteness** theorem (Hodge index on $H^1$), **not** a center-anchor;
  the function-field "anchor" is the trivial-cohomology edge pole, present for $\zeta$ too.
- **Bifurcation resolved:** Q(anchor) **collapses** to Weil/Hodge positivity (the capstone). It is *not* a new
  RH-relevant object. The framework's merge of "anchor" and "definiteness" was an over-reach, now corrected.
- **The sharpened wall (genuine value):** the missing ingredient is a **Hodge index theorem on a 2-dimensional
  arithmetic geometry over $\operatorname{Spec}\mathbb Z$** — the anchor is present, the *surface* is what is
  absent. This is the most precise statement of the RH wall the program has reached, and it is RH-equivalent.
