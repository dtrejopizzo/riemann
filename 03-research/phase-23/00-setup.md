# Phase 23 — Estructura de dos escalas y compatibilidad espectral del defecto

**Fecha:** junio 2026  
**Predecesora:** Phase 22 (fórmula explícita modificada, auditoría de invariantes, Step 22-D)  
**Estado:** Activa

---

## Punto de partida exacto

Phase 22 estableció:

1. Bajo Hipótesis D: $\psi = \psi_0 - D_m$ exacto.
2. $D_j(e^t)/e^{t/2} = A_j e^{b_j t}\cos(\gamma_j t) + O(e^{-b_j t})$ — crecimiento exponencial.
3. Función de estructura: $S_2^{(D)}(\tau, T) \asymp e^{2b_j T}$ — diverge exponencialmente.
4. El método de Paley-Wiener alcanza exactamente la frontera $\Re(s) = 1$.
5. Los tres candidatos de invariantes fallan o son circulares.

Phase 22 también propuso: si el CMG con $\beta=1$ satisface $S_2 = O(\log T)$, hay incompatibilidad con $e^{2b_j T}$. Esta fue la dirección de Phase 23.

Phase 23 evalúa esa dirección y hace los cálculos exactos.

---

## Reglas absolutas

- No computación numérica, no Python.
- Solo definiciones, lemas, proposiciones, teoremas, demostraciones.
- Todo argumento debe evaluarse según si contribuye a excluir $m \geq 1$.
- Si una línea no lleva a $m = 0$, se abandona y se documenta honestamente.

---

## La pregunta de Phase 23

Bajo Hipótesis D, el cero fuera de línea $\rho_j = \sigma_j + i\gamma_j$ se manifiesta de dos maneras:

**Escala $x$** (variable de conteo de primos): $D_j(x) \asymp x^{1/2+b_j}\cos(\gamma_j\log x)$ — crecimiento algebraico.

**Escala $t$** (alturas imaginarias, variable de $\zeta$ en la línea crítica): efecto en $\log|\zeta(1/2+it)|$ cerca de $t = \gamma_j$ — depresión localizada de profundidad finita.

Preguntas:
1. ¿Cuál es exactamente el efecto en $\log|\zeta(1/2+it)|$? (computable del producto de Hadamard)
2. ¿Es ese efecto compatible o incompatible con el CMG?
3. ¿Puede acotarse $S_2^X(\tau,T)$ desde arriba usando el producto de Euler?
4. ¿Produce alguna contradicción con $m \geq 1$?

---

## Documentos de la fase

- `00-setup.md` — este documento
- `01-exact-hadamard-effect.md` — cálculo exacto del efecto de la órbita fuera de línea en $\log|\zeta(1/2+it)|$
- `02-structure-function-analysis.md` — análisis de $S_2$ desde arriba y abajo
- `03-barrier-formulation.md` — formulación precisa del obstáculo final

## Paper

P34 — `06-papers/P34-two-scale-structure/main.tex`
