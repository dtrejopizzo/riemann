# Phase 66 — The rank-one escape dichotomy (CAND-1, operator convergence, not positivity)

**Opened:** 2026-07-05
**Route:** CAND-1 (Zeta Spectral Triples, Connes–Consani–Moscovici 2025–26, arXiv:2511.22755).
**Why this and not the positivity routes:** the operators are self-adjoint BY CONSTRUCTION
(Carathéodory–Fejér), so there is **no Weil positivity to prove** — Master Wall MW-1 is sidestepped.
The open obstacle is **operator convergence / boundedness**, a different category. Consult
`NO-GO-LIST.md` before every step; positivity-side ideas (envelope, partition, prolate domination,
Hodge intersection form) are MW-1/MW-5 and are dead ends here.

---

## 1. The exact open statement (from phase-64, `CONSTRUCTION-TW-canonical-system.md §5`)

The finite Tate–Weil canonical Hamiltonians $d\mathcal H_P\ge0$ (von Mangoldt positivity) give positive
canonical Gram kernels $K_P=\int Y_P^*\,d\mathcal H_P\,Y_P\succeq0$ (proved, canonical Gram identity).
Positivity is **free**. The single wall is the boundedness/escape statement:

> **Rank-one escape (RH-strength).**
> $$\sup_P\big\|P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\big\|<\infty,\qquad
>   P_{\mathrm{prim}}=I-\frac{|H\rangle\langle H|}{\langle H,H\rangle},$$
> i.e. all divergent mass of $K_P$ ($\operatorname{Tr}K_P\sim\tfrac12(\log P)^2$) escapes **only**
> through the pole direction $H$.

**Corollary (escape ⟹ RH).** Uniform boundedness ⟹ weak-$*$ limit $K_{\mathrm{crit}}\succeq0$ ⟹
$S_\kappa$ Schur ⟹ $m=-\Xi'/\Xi$ Herglotz ⟹ RH. An off-line zero $\rho=\beta+i\gamma$, $\beta>\tfrac12$,
is a **second escape direction** with growth $\lambda^{2\beta-1}$. Hence
$$\text{rank-one escape}\iff\text{no off-line zeros}\iff\textnormal{RH}.$$

**Three faces (any one closes it), phase-64 §7:**
- **(A) Central adelic large sieve** at the *critical* exponent: $\sup_X\|\sum_{n\le
  X}\frac{\Lambda(n)}{\sqrt n}\Pi_{\mathrm{prim}}(F_{\log n})\|<\infty$ — far stronger than PNT/zero-free
  (edge) bounds.
- **(B) Primitive finite-part Hodge index** (the arithmetic-site face; = MW-5).
- **(C) Canonical-system compactness** at exponent $\tfrac12$.

---

## 2. Honest scope: what is RH-strength and what is genuinely below it

The escape statement itself **is RH** (all three faces). This phase does NOT aim to prove it. The
deliverables below are the things that are (a) genuinely open, (b) NOT catalogued as failed, and
(c) either provably below RH or a sharp structural clarification. Anything that turns out to be a
positivity restatement (MW-1) or the arithmetic site (MW-5, face B) is logged and dropped.

### Deliverable D1 — the dichotomy is SHARP (no partial regime). [target: theorem]
Prove: a **single** off-line zero already forces $\|P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\|\to\infty$
at rate $\lambda^{2\beta-1}$; hence there is no "finitely many off-line zeros ⟹ bounded escape"
intermediate result. Consequence: boundedness $\iff$ RH with no slack, and the hoped-for partial
(bounded index ⟹ finite off-line count) does **not** exist. This is a real structural lemma (it closes
a tempting sub-route) and is below RH (it is the *easy* direction: ¬RH ⟹ unbounded).

### Deliverable D2 — the escape-norm detector. [target: reproducible numerics]
Compute $\|P_{\mathrm{prim}}K_PP_{\mathrm{prim}}\|$ (or its validated operator proxy from E101/E107) vs
$P$ for $\zeta$ (expect bounded) and for the DH falsifier / a planted off-line zero (expect growth
$\lambda^{2\beta-1}$). Faithful, falsifiable detector — a criterion, not a proof (stated as such).

### Deliverable D3 — locate face (A) against the classical large sieve. [target: precise reduction]
State exactly the exponent gap between what the unconditional large sieve (Montgomery–Vaughan) gives
(edge, $n^{-\sigma}$, $\sigma>\tfrac12$) and what escape needs (critical $\sigma=\tfrac12$), and whether
the primitive projection $\Pi_{\mathrm{prim}}$ (killing the pole/principal channel) buys anything. This
pinpoints the "new mathematics" of face (A) as a named, quantified open problem — real orientation,
below RH.

---

## 3. Protocol (per NO-GO-LIST §VI)
Every candidate step: (1) check NO-GO-LIST; (2) name the wall it depends on — if MW-1 (positivity) or
MW-5 (arithmetic site) it is a dead end, log and drop; (3) each new failure appended here. Proven,
below-RH results flow to paper **P53**. Nothing committed as "toward RH" that is a positivity
restatement.
