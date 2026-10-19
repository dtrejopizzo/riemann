# Phase 27-A/B — Classification and adelic interpretation

**Prerequisite:** Conjecture 26-C.2 (Bridge Theorem) accepted as a working hypothesis.

---

## 27-A: Classification of negative directions → complex eigenvalues

**Proposition 27-A.1** (from Conjecture 26-C.2 + Kreĭn–Langer). Under Hypothesis D with κ = 2m:

Each of the κ = 2m negative subspaces of $(\mathcal{K}, Q)$ produces exactly
one pair of complex eigenvalues $\{\lambda_j, \bar\lambda_j\}$ of $H_C$, with:
$$\lambda_j = \gamma_j - ib_j, \qquad \bar\lambda_j = \gamma_j + ib_j, \qquad b_j > 0.$$

*Proof.* Direct from the Bridge Theorem (Conjecture 26-C.2 (ii)): each orbit $j=1,\ldots,m$
contributes two complex eigenvalues to the spectrum of $H_C$ on $\mathcal{K}$. The
Kreĭn–Langer theorem gives the upper bound $\le \kappa$; the bridge gives equality. $\square$

**Remark 27-A.2.** Proposition 27-A.1 is almost definitional given the bridge.
Its content is not the proof (trivial given 26-C.2) but the reformulation:
the $2m$ negative directions of $Q$ ARE the $2m$ complex eigenvalues of $H_C$.
They are the same object in two languages.

---

## 27-B: Adelic interpretation — complex eigenvalues as non-unitary characters

**Proposition 27-B.1** (identification with Grössencharacters). Each complex eigenvalue
$\lambda_j = \gamma_j - ib_j$ of $H_C = -ix\partial_x$ corresponds to the character
$$\chi_j(x) = x^{b_j + i\gamma_j} = |x|^{b_j + i\gamma_j}, \qquad x \in \mathbb{R}^*_+,$$
which formally satisfies $H_C \chi_j = \lambda_j \chi_j$.

$\chi_j$ extends to a Grössencharacter of $C_\mathbb{Q}$ of the form $|x|_\mathbb{A}^{b_j+i\gamma_j}$
where $|\cdot|_\mathbb{A}$ is the adelic absolute value.

**Proposition 27-B.2** (non-unitarity). The character $\chi_j$ is **non-unitary**:
$$|\chi_j(x)| = |x|^{b_j} \ne 1 \quad \text{for } |x| \ne 1, \text{ since } b_j > 0.$$

In contrast, the **unitary dual** $\widehat{C_\mathbb{Q}}^{\text{unit}}$ consists of characters
$|x|^{i\gamma}$ with $b = 0$ (purely imaginary). By Tate's theory (1950),
the spectrum of $H_C$ on $L^2(C_\mathbb{Q})$ under the Plancherel decomposition
contains ONLY unitary characters.

*Proof of non-unitarity.* $|x|^{b_j} \ne 1$ for $x \ne 1$ with $b_j > 0$.
The Plancherel measure on $L^2(C_\mathbb{Q})$ (Haar measure = Plancherel measure on the characters)
only supports characters with $|\chi(x)| = 1$ for almost every $x$. $\square$

**Corollary 27-B.3** (the connection with V.2). The reason why $\chi_j \notin L^2(C_\mathbb{Q})$
(the central obstacle of V.2 in Phase 26) is exactly that $\chi_j$ is a
**non-unitary** character. In adelic terms:

$$\underbrace{x^{b_j+i\gamma_j} \notin L^2(C_\mathbb{Q})}_{\text{obstacle V.2 (Phase 26)}}
\iff
\underbrace{|\cdot|^{b_j+i\gamma_j} \notin \widehat{C_\mathbb{Q}}^{\text{unit}}}_{\text{non-unitarity (Phase 27)}}.$$

This is the same statement in two languages: **Phase 26 (V.2) and Phase 27 (27-B) are the
same obstacle.**

---

## The central identification of Phases 26–27

**Theorem 27-B.4** (identification V.2 = 27-B, under the bridge).

The following statements are equivalent:

1. **(V.2, Phase 26):** The characters $x^{b_j+i\gamma_j}$ belong to some distributional
   extension $\mathcal{K}^+$ of $(\mathcal{K}, Q)$ and are eigenvectors of $H_C$.

2. **(27-B, Phase 27):** The non-unitary Grössencharacters $|x|^{b_j+i\gamma_j}$
   appear as eigenvalues of $H_C$ in some space extending $L^2(C_\mathbb{Q})$.

3. **(Bridge, Conjecture 26-C.2):** $H_C$ has exactly 2m complex eigenvalues on
   $(\mathcal{K}, Q)$.

*Proof.* By construction: (1) and (2) are the same condition expressed in terms of the
function space and of the dual of $C_\mathbb{Q}$ respectively. (3) follows from (1)/(2)
by applying the Kreĭn–Langer theorem. $\square$

**Direct consequence.** Phase 27 does not solve V.2 — it reformulates it in the language of
Grössencharacters. V.2 remains the central functional obstacle of the program.

Phase 27-C is where the program attempts a genuinely new attack: not a direct
resolution of V.2, but a global exclusion of non-unitary characters from the spectrum of $H_C$.
