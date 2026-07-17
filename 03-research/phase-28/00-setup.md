# Phase 28 — Cuatro frentes simultáneos

**Fecha:** junio 2026
**Prerrequisito:** Resultados de Phases 26–27 aceptados; conjetura del puente 26-C.2 como hipótesis de trabajo.

---

## El diagnóstico de Phase 27

Phase 27 identificó que todos los obstáculos del programa se reducen al mismo objeto:
construir la cohomología aritmética $H^1(\operatorname{Spec}\mathbb{Z})$ con forma de
intersección positiva (Wall A = sitio aritmético de Connes–Consani). Pero también
identificó que ese wall lleva décadas sin cerrarse.

Phase 28 abandona la estrategia de reformulación y abre cuatro frentes que atacan
**mecanismos causales**, no equivalencias. La distinción es precisa:

> Una reformulación equivalente a RH responde: *¿qué significa RH?*
> Un mecanismo causal responde: *¿por qué los ceros no pueden abandonar la recta crítica?*

Phase 28 busca mecanismos causales.

---

## Los cuatro frentes

| Frente | Pregunta central | Herramienta nueva |
|---|---|---|
| **A** | ¿Es el flujo de de Bruijn–Newman el flujo gradiente de la energía logarítmica? | Dinámica de ceros, ODE de Csordas–Norfolk–Varga |
| **B** | ¿Es el $\eta$-invariante de APS del operador de Weil idénticamente cero? | Teoría de índice de Atiyah–Patodi–Singer |
| **C** | ¿Es la proyección espectral negativa $[P_-]$ la clase trivial en $K_0(C^*(C_\mathbb{Q}))$? | K-teoría de C*-álgebras, Baum–Connes |
| **D** | ¿Es la recta crítica el único mínimo de una energía aritmética canónica? | Problema variacional, energía transversal |

---

## El resultado central: A y D son el mismo frente

Antes de empezar: la observación más importante de Phase 28 es que los Frentes A y D
son el **mismo programa en dos lenguajes**.

El flujo de de Bruijn–Newman sobre los ceros de $H_t$ es exactamente el flujo gradiente
de la energía logarítmica:
$$E_{\log}(Z) = -\sum_{j \ne k} \log|z_j - z_k|.$$

Esto fue establecido por Csordas–Norfolk–Varga (1988): la ecuación de evolución de los
ceros es:
$$\frac{dz_n}{dt} = \sum_{k \ne n} \frac{2}{z_k - z_n}.$$

Entonces la pregunta del Frente A (¿el flujo disminuye monotónamente el índice de Kreĭn?)
y la pregunta del Frente D (¿la energía aritmética tiene mínimo único en la recta crítica?)
son la misma pregunta: ¿el flujo gradiente de $E_{\log}$, sujeto a las restricciones
aritméticas de $\zeta$, converge a la configuración con $b_j = 0$?

Documentaremos los dos frentes por separado para claridad, pero la unificación es el
resultado estructural más importante de Phase 28.

---

## Criterio de éxito por frente

| Frente | Éxito completo | Éxito parcial (publicable) |
|---|---|---|
| A | $\kappa_t$ estrictamente no-creciente bajo el flujo DBN → RH | Fórmula exacta $\Lambda = b_{\max}^2/2$ |
| B | $\eta(T_0) = 0$ por simetría aritmética → $\kappa = 0$ | Cálculo explícito de $\eta(T_0)$ |
| C | $[P_-] = 0$ en $K_0$ por Baum–Connes → RH | Identificación precisa de la imagen de $[P_-]$ |
| D | Energía aritmética con mínimo único en $b_j = 0$ → RH | Condición necesaria y suficiente en términos de $b_j$ |

---

## Documentos de Phase 28

- `phase-28/01-front-A.md` — Frente A: flujo DBN y monotonía de Kreĭn
- `phase-28/02-front-B.md` — Frente B: flujo espectral y $\eta$-invariante
- `phase-28/03-front-C.md` — Frente C: K-teoría y clase de obstrucción
- `phase-28/04-front-D.md` — Frente D: energía transversal y recta crítica como atractor
