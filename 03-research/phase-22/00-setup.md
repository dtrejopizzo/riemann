# Phase 22 — Consecuencias Aritméticas del Defecto Finito de Pontryagin

**Fecha:** junio 2026  
**Predecesora:** Phase 21 (geometría del espacio negativo, P32)  
**Estado:** Activa

---

## Punto de partida

Phase 21 estableció:

1. **Teorema de Paridad** (incondicional): $\kappa = 2m$, $m \geq 0$.
2. **Descomposición de Lorentz** (incondicional): $\mathcal{N} \cong \bigoplus_{j=1}^m \mathbb{R}^{1,1}_j$.
3. **Teorema 9.1 / Corolario 9.2** (condicional a $\kappa < \infty$): bajo $\kappa = 2m < \infty$,
   $$\xi = \xi_0 \cdot P_{4m}$$
   donde $\xi_0$ es entera con todos los ceros en la línea crítica y $P_{4m}$ es el polinomio de los $4m$ ceros fuera de línea.
4. **Conjetura EX**: $\kappa \in \{0\} \cup \{\infty\}$ (sin valor finito positivo).
5. **Wall W4-RSRP**: pared candidata, Rigidez Espectral del Régimen de Pontryagin.

Phase 22 parte de la hipótesis $0 < \kappa = 2m < \infty$ (que llamamos **hipótesis D**) y
pregunta: ¿qué deja en el conteo de primos un conjunto **finito** de ceros fuera de línea?

---

## Reglas absolutas de la fase

Esta fase NO usa:
- experimentos numéricos ni Python
- par-correlación como axioma
- sistemas de de Branges como input
- SURF, Hilbert–Pólya, GUE como hipótesis
- ningún criterio equivalente a RH como punto de partida
- derivaciones no-rigurosas de fórmulas explícitas

Todo resultado debe derivarse de:
- la fórmula de Perron + la factorización $\xi = \xi_0 P_{4m}$
- el producto de Euler de $\zeta$
- la ecuación funcional
- álgebra/análisis complejo puro

---

## Objeto central

Bajo hipótesis D, definir:

$$D_m(x) := \sum_{\rho \in Z_{\text{off}}} \frac{x^\rho}{\rho}, \qquad
Z_{\text{off}} = \{\text{ceros fuera de línea de } \zeta\}$$

Llamamos a $D_m(x)$ el **defecto aritmético de grado** $m$.

Preguntas:
1. ¿Cuál es la forma exacta de $D_m(x)$?
2. ¿Qué invariantes de $\psi(x)$ quedan marcados por $D_m$?
3. ¿Puede $D_m$ ser compatible con la estructura del producto de Euler?
4. ¿Conecta $D_m$ con la clase $\omega$ (caos multiplicativo)?

---

## Objetivos

### 22-A: Fórmula Explícita Modificada (Clase B — demostrable)

Derivar rigurosamente la descomposición:
$$\psi(x) = \psi_0(x) - D_m(x) + O(\log^2 x)$$

donde $\psi_0(x)$ es el análogo de Chebyshev de $\xi_0$ y $D_m$ es la suma finita de oscilaciones.

Calcular los coeficientes exactos: amplitudes, fases, tasas de crecimiento.

### 22-B: Anatomía del Defecto (Clase B — demostrable)

Para cada órbita $\mathcal{O}_j = \{\sigma_j \pm i\gamma_j, (1-\sigma_j) \pm i\gamma_j\}$ con $b_j = \sigma_j - \frac{1}{2} > 0$:

- Calcular $D_j(x)$ explícitamente.
- Estudiar la estructura del **bloque de Lorentz** vía la fórmula explícita.
- Calcular la "energía del defecto" $\mathcal{E}_j(X) = \int_X^{2X} |D_j(t)|^2 t^{-2}\,dt$.

### 22-C: Invariantes Incompatibles (Exploratoria → potencial Clase A)

Buscar un funcional $\mathcal{F}$ tal que:
- $\mathcal{F}(\psi)$ tiene valor conocido (del producto de Euler)
- $\mathcal{F}(\psi_0 - D_m)$ es incompatible con el valor anterior para todo $m \geq 1$

Candidatos: momentos del segundo tipo de Selberg, la función de Mertens, integrales de tipo tamiz.

### 22-D: Conexión con clase $\omega$ (Exploratoria)

Vía el caos multiplicativo (M13 y predecesores): ¿puede la fluctuación $D_m$ coexistir con las estadísticas del caos de grano fino?

---

## Documentos de la fase

- `00-setup.md` — este documento
- `01-modified-explicit-formula.md` — Steps 22-A y 22-B
- `02-invariants.md` — Step 22-C (a escribir)
- `03-omega-connection.md` — Step 22-D (a escribir)

## Paper

P33 — `06-papers/P33-arithmetic-defect/main.tex`
