# Phase 27-A/B — Clasificación e interpretación adélica

**Fecha:** junio 2026
**Prerrequisito:** Conjetura 26-C.2 (Teorema Puente) aceptada como hipótesis de trabajo.

---

## 27-A: Clasificación de direcciones negativas → eigenvalores complejos

**Proposición 27-A.1** (de la Conjetura 26-C.2 + Kreĭn–Langer). Bajo Hipótesis D con κ = 2m:

Cada uno de los κ = 2m subespacios negativos de $(\mathcal{K}, Q)$ produce exactamente
un par de eigenvalores complejos $\{\lambda_j, \bar\lambda_j\}$ de $H_C$, con:
$$\lambda_j = \gamma_j - ib_j, \qquad \bar\lambda_j = \gamma_j + ib_j, \qquad b_j > 0.$$

*Prueba.* Directa del Teorema Puente (Conjetura 26-C.2 (ii)): cada órbita $j=1,\ldots,m$
contribuye dos eigenvalores complejos al espectro de $H_C$ en $\mathcal{K}$. El
Teorema de Kreĭn–Langer da la cota superior $\le \kappa$; el puente da la igualdad. $\square$

**Observación 27-A.2.** La Proposición 27-A.1 es casi definitorial dado el puente.
Su contenido no es la prueba (trivial dado 26-C.2) sino la reformulación:
las $2m$ direcciones negativas de $Q$ SON los $2m$ eigenvalores complejos de $H_C$.
Son el mismo objeto en dos lenguajes.

---

## 27-B: Interpretación adélica — eigenvalores complejos como caracteres no-unitarios

**Proposición 27-B.1** (identificación con Grössencharacters). Cada eigenvalor complejo
$\lambda_j = \gamma_j - ib_j$ de $H_C = -ix\partial_x$ corresponde al carácter
$$\chi_j(x) = x^{b_j + i\gamma_j} = |x|^{b_j + i\gamma_j}, \qquad x \in \mathbb{R}^*_+,$$
que satisface $H_C \chi_j = \lambda_j \chi_j$ formalmente.

$\chi_j$ extiende a un Grössencharacter de $C_\mathbb{Q}$ de la forma $|x|_\mathbb{A}^{b_j+i\gamma_j}$
donde $|\cdot|_\mathbb{A}$ es el valor absoluto adélico.

**Proposición 27-B.2** (no-unitaridad). El carácter $\chi_j$ es **no-unitario**:
$$|\chi_j(x)| = |x|^{b_j} \ne 1 \quad \text{para } |x| \ne 1, \text{ pues } b_j > 0.$$

En contraste, el **dual unitario** $\widehat{C_\mathbb{Q}}^{\text{unit}}$ consiste de caracteres
$|x|^{i\gamma}$ con $b = 0$ (puramente imaginario). Por la teoría de Tate (1950),
el espectro de $H_C$ en $L^2(C_\mathbb{Q})$ bajo la descomposición de Plancherel
contiene SÓLO caracteres unitarios.

*Prueba de no-unitaridad.* $|x|^{b_j} \ne 1$ para $x \ne 1$ con $b_j > 0$.
El Plancherel en $L^2(C_\mathbb{Q})$ (medida de Haar = medida de Plancherel en los caracteres)
sólo apoya caracteres con $|\chi(x)| = 1$ para casi todo $x$. $\square$

**Corolario 27-B.3** (la conexión con V.2). La razón por la que $\chi_j \notin L^2(C_\mathbb{Q})$
(obstáculo central de V.2 en Phase 26) es exactamente que $\chi_j$ es un carácter
**no-unitario**. En términos adélicos:

$$\underbrace{x^{b_j+i\gamma_j} \notin L^2(C_\mathbb{Q})}_{\text{obstáculo V.2 (Phase 26)}}
\iff
\underbrace{|\cdot|^{b_j+i\gamma_j} \notin \widehat{C_\mathbb{Q}}^{\text{unit}}}_{\text{no-unitaridad (Phase 27)}}.$$

Esta es la misma afirmación en dos lenguajes: **Phase 26 (V.2) y Phase 27 (27-B) son el
mismo obstáculo.**

---

## La identificación central de Phases 26–27

**Teorema 27-B.4** (identificación V.2 = 27-B, bajo el puente).

Las siguientes afirmaciones son equivalentes:

1. **(V.2, Phase 26):** Los caracteres $x^{b_j+i\gamma_j}$ pertenecen a alguna extensión
   distribucional $\mathcal{K}^+$ de $(\mathcal{K}, Q)$ y son eigenvectores de $H_C$.

2. **(27-B, Phase 27):** Los Grössencharacters no-unitarios $|x|^{b_j+i\gamma_j}$
   aparecen como eigenvalores de $H_C$ en algún espacio que extiende $L^2(C_\mathbb{Q})$.

3. **(Puente, Conjetura 26-C.2):** $H_C$ tiene exactamente 2m eigenvalores complejos en
   $(\mathcal{K}, Q)$.

*Prueba.* Por construcción: (1) y (2) son la misma condición expresada en términos del
espacio de funciones y del dual de $C_\mathbb{Q}$ respectivamente. (3) sigue de (1)/(2)
aplicando el Teorema de Kreĭn–Langer. $\square$

**Consecuencia directa.** Phase 27 no resuelve V.2 — lo reformula en el lenguaje de
Grössencharacters. V.2 permanece como el obstáculo funcional central del programa.

Phase 27-C es donde el programa intenta un ataque genuinamente nuevo: no resolución
directa de V.2, sino exclusión global de caracteres no-unitarios del espectro de $H_C$.
