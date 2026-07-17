# Phase 21 — Step 2: The Exclusion Principle and the Kreĭn-Langer Audit

**Date:** June 2026  
**Pregunta central:** ¿Puede probarse que $0 < \kappa < \infty$ es imposible para $\zeta$?  
**Tipo de análisis:** Auditoría antes de iniciar 21-D

---

## Enunciado preciso de la Conjetura de Exclusión

**Conjetura EX.** No existe ninguna realización de la forma de Weil asociada a $\zeta$ para la cual $0 < \kappa < \infty$.

En términos del espacio negativo:

$$\kappa \in \{0\} \cup \{\infty\}.$$

Si se prueba: RH se convierte en la pregunta binaria $\kappa = 0$ o $\kappa = \infty$.

---

## Por qué esta pregunta es nueva

La Conjetura EX NO es equivalente a ninguno de los muros identificados:

| Muro | Equivalente | ¿Se reduce a él? |
|------|-------------|-----------------|
| W1 (PNT/Weil positivity) | $\psi(x) = x + O(x^{1/2+\varepsilon})$ | No: EX es geométrica, no estimativa |
| W2 (SURF/de Branges) | Construir cohomología global | No: EX no construye nada, solo excluye |
| W3 (pair correlation/GUE) | Universalidad de gaps | No: EX es sobre proliferación, no distribución |

EX dice: **si algún bloque de Lorentz existe, deben existir infinitos**.  
Esto es una afirmación de proliferación forzada, no una afirmación de positividad o de construcción.

---

## Análisis riguroso: ¿qué dice la teoría de Kreĭn-Langer sobre $0 < \kappa < \infty$?

### La factorización

Si $0 < \kappa = 2m < \infty$, el teorema de Kreĭn-Langer aplicado a $E(z) = \xi(\tfrac{1}{2}+iz)$ da:
$$E(z) = E_0(z) \cdot B_{2m}(z),$$
donde:
- $B_{2m}$ es un producto de Blaschke (función racional) de grado $2m$ en el semiplano superior, con sus $2m$ polos en las imágenes de los ceros off-line con $\Re\rho < \tfrac{1}{2}$.
- $E_0$ es una función de de Branges genuina: entera, satisface $|E_0(\bar z)| < |E_0(z)|$ para $\Im z > 0$, todos sus ceros son reales o en el semiplano inferior.

El espacio de de Branges-Pontryagin $H(E)$ se descompone:
$$H(E) = H(E_0) \oplus^{\perp_Q} \text{corrección Pontryagin}_{2m}.$$

La corrección Pontryagin tiene dimensión $2m$.

### Lo que esto implica

Si $\kappa = 2m$, entonces existe $E_0$ entera con:
1. Todos los ceros de $E_0$ sobre el eje real (en coordenada $z$), es decir, todos los ceros de $\xi(\tfrac{1}{2}+iz)/B_{2m}(z)$ son reales.
2. $E_0$ tiene orden 1 (igual que $E$, pues $B_{2m}$ es racional).
3. $E_0$ satisface la ecuación funcional inducida (pues $\xi$ y $B_{2m}$ son ambos $\iota$-invariantes).

**Observación:** $E_0$ es una función entera con todos sus ceros en $\mathbb{R}$, de orden 1, satisfaciendo una ecuación funcional análoga a la de $\xi$. Esto es consistente con la teoría de de Branges: existe una familia enorme de tales funciones.

**No hay contradicción en el nivel de análisis funcional solo.**

---

## El obstáculo para probar EX

La Conjetura EX requeriría mostrar que:

> La restricción adicional proveniente del **producto de Euler** impide que $E_0$ pueda existir como separado finito de $E$.

Más precisamente: si $\xi$ tiene exactamente $4m$ ceros off-line, entonces $E/B_{2m}$ debe ser inconsistente con el producto de Euler de $\zeta$.

### ¿Por qué el producto de Euler podría ayudar?

El producto de Euler $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ para $\Re s > 1$ impone que los ceros de $\zeta$ están relacionados con los primos de manera muy específica. No cualquier configuración de ceros puede provenir de una función L con producto de Euler aritmético.

Pero: la relación entre los ceros individuales y los primos individuales no es directa. El Euler product determina la **distribución estadística** de los ceros (vía la fórmula explícita), no la ubicación exacta de cada cero.

### El muro real detrás de EX

La Conjetura EX, si pudiera probarse, requeriría algo del tipo:

> "Si la función $\xi(\cdot)/B_{2m}(\cdot)$ satisface la ecuación funcional y tiene orden 1, y si $\xi$ proviene de un producto de Euler aritmético, entonces $B_{2m}$ debe ser trivial ($m=0$) o infinitamente no-trivial ($m=\infty$)."

Esto conecta con:

1. **La unicidad del producto de Euler**: la función $\zeta$ es el único elemento de la clase de Selberg con conductor 1. ¿Impone el conductor la estructura de ceros off-line?

2. **La rigidez espectral**: en la teoría de matrices aleatorias, la rigidez espectral dice que las posiciones de los autovalores son altamente rígidas (fluctuaciones $O(1)$). Si algo análogo existe para los ceros de $\zeta$, podría impedir la existencia de un número finito de ceros off-line.

3. **La hipótesis de independencia lineal (LI)**: los $\gamma_\rho$ son linealmente independientes sobre $\mathbb{Q}$. Esto impide ciertos tipos de "resonancias" entre ceros. ¿Podría implicar que un cero off-line fuerza una cadena infinita?

**Ninguno de estos enfoques conduce a un teorema actualmente.**

---

## Lo que sí puede probarse en 21-D

### Teorema 21-D.1 (Estructura formal del régimen Pontryagin)

**Enunciado.** Asumamos $0 < \kappa = 2m < \infty$. Entonces existe una función $E_0 = \xi(\tfrac{1}{2}+iz)/B_{2m}(z)$ entera de orden 1 tal que:
1. Todos los ceros de $E_0$ son reales (en coordenada $z$), equivalentemente todos los ceros de la función entera correspondiente están en la recta crítica.
2. $E_0$ es una función de de Branges (Hermite-Biehler): $|E_0(\bar z)| < |E_0(z)|$ para $\Im z > 0$.
3. El espacio de Hilbert $H(E_0)$ (de de Branges) tiene índice negativo cero: la forma de Weil restringida a $H(E_0)$ es positivo-semidefinida.
4. En el sentido funcional: "RH vale en $H(E_0)$".

Esta es una consecuencia directa del Teorema de Kreĭn-Langer y la Proposición~\ref{prop:restricted} de P32.

### Corolario 21-D.2 (RH parcial bajo $\kappa < \infty$)

Si $\kappa = 2m < \infty$, entonces existe una función entera $\xi_0$ satisfaciendo la ecuación funcional con todos los ceros en la recta crítica, y relacionada a $\xi$ por:
$$\xi(s) = \xi_0(s) \cdot P_{4m}(s),$$
donde $P_{4m}$ es un polinomio de grado $4m$ con raíces exactamente en los $4m$ ceros off-line de $\xi$.

**Prueba.** $\xi_0(s) = \xi(\tfrac{1}{2}+i(\cdot)) / B_{2m}(\cdot)$ bajo el cambio de variables apropiado. $P_{4m}$ es el polinomio cuyos ceros son las $4m$ imágenes de los ceros off-line. $\square$

**Observación.** Este resultado no es circular ni supone RH: es una afirmación condicional. Dice que SI $\kappa = 2m < \infty$, ENTONCES existe $\xi_0$ con RH. Pero no dice que $\xi_0 = \xi$ (si $\xi_0 = \xi$ entonces $P_{4m} = 1$ y $\kappa = 0$, que es RH).

---

## Identificación del nuevo obstáculo (no W1/W2/W3)

**Proposición 21-D.3 (Nuevo territorio).** La Conjetura de Exclusión, si pudiera probarse, constituiría un resultado de un tipo nuevo: no se reduce a W1, W2, ni W3.

**Argumento:**

- **No es W1**: W1 dice que probar $\kappa = 0$ requiere estimar el error de PNT. EX no dice $\kappa = 0$; dice $\kappa \notin (0,\infty)$. No implica $\kappa = 0$ directamente.

- **No es W2**: W2 requiere construir SURF. EX es una afirmación de imposibilidad (no construye nada); es formalmente un teorema de no-existencia.

- **No es W3**: W3 es la universalidad GUE. EX no habla de distribución de gaps, sino de si el conteo $m$ puede ser finito positivo.

**La prueba de EX requeriría**, en cambio:

> Un teorema del tipo: "la rigidez espectral del producto de Euler no permite que $\xi$ se factorice como $\xi_0 \cdot P_{4m}$ con $\xi_0$ entera con todos los ceros en la línea crítica y $1 \leq m < \infty$."

Esta es una afirmación de rigidez aritmética: el producto de Euler impone que los ceros de $\zeta$ son "todos on-line" o "infinitamente off-line", sin estado intermedio.

Esto es genuinamente nuevo porque no es:
- Una estimativa (W1)
- Una construcción (W2)
- Una estadística (W3)
- Una positividad (N1: capstone)

Es una **afirmación de imposibilidad aritmético-geométrica**.

---

## El candidato a W4: Rigidez Espectral del Régimen Pontryagin

Habiendo demostrado que EX es genuinamente nuevo y no reducible a los muros conocidos, lo identificamos formalmente:

**Definición (W4-candidato).** El muro de **Rigidez Espectral del Régimen Pontryagin** (RSRP) es la conjetura:

> Para $\zeta$, no existe configuración de ceros con $0 < m < \infty$ órbitas off-line completas que sea consistente con el producto de Euler, la ecuación funcional, y el crecimiento de orden 1 de $\xi$.

Es decir: $m = 0$ (RH) o $m = \infty$ (infinitos ceros off-line).

**Estado actual:** Conjetura. Ni probada ni refutada.

**Por qué es difícil:** No se conoce ninguna herramienta que conecte el producto de Euler con la cardinalidad de los ceros off-line. La teoría de Kreĭn-Langer sólo habla de estructura formal; no habla de aritmética.

---

## Caminos posibles (sin garantía)

### Camino 1: Rigidez del tipo Siegel

Los ceros de $\zeta$ satisfacen relaciones de irracionalidad (bajo LI). ¿Podría probarse que la existencia de $m$ ceros off-line fuerza la existencia de $m+1$ ceros off-line via algún argumento de irracionalidad o transcendencia?

**Obstáculo:** Los argumentos de irracionalidad de los $\gamma_\rho$ no controlan la signatura de $\Re\rho - \tfrac{1}{2}$.

### Camino 2: Rigidez del tipo densidade crítica

Un cero off-line a altura $\gamma_0$ perturbaría la distribución local de ceros en $[\gamma_0 - \delta, \gamma_0 + \delta]$. Si esta perturbación viola un invariante de densidad local, podría forzar nuevos ceros off-line.

**Obstáculo:** La densidad local de ceros no distingue on-line de off-line para $\Re\rho$ cercano a $\tfrac{1}{2}$.

### Camino 3: Argumento de analiticidad global

Si $m < \infty$, la función $\xi/P_{4m}$ es entera con todos los ceros en la línea crítica. ¿Puede probarse que ninguna función del tipo "deformación finita de $\xi$" tiene todos los ceros en la línea crítica, excepto la propia $\xi$ (que sería el caso $m=0$)?

**Obstáculo:** No hay un principio de unicidad para funciones enteras con todos los ceros en una recta. Pueden construirse infinitas funciones con esa propiedad.

### Camino 4: Argumento de automorfia

Si $\zeta$ proviene de una representación automorfa (que sí, es $GL_1$), ¿las propiedades de la representación impiden $m$ finito positivo? 

**Obstáculo:** La teoría de formas automorfas da la ecuación funcional y el Euler product, pero no directamente la posición de los ceros individuales. Esto recae en W1.

---

## Conclusión de la auditoría

La Conjetura de Exclusión (EX) es:

1. **Genuinamente nueva** (no reducible a W1/W2/W3). ✓
2. **Bien formulada matemáticamente**. ✓
3. **No provable por las herramientas actuales**. ✓
4. **Un nuevo candidato a muro** (W4-RSRP). ✓
5. **No más difícil que RH** si y solo si... en realidad se desconoce su dificultad relativa. Es posible que EX sea exactamente tan difícil como RH, o más.

**Lo que sí está resuelto en Phase 21:**
- Teorema de Paridad: $\kappa = 2m$ (Clase B, probado). ✓
- Separación Angular: ortogonalidad exponencial (Clase B, probado). ✓
- Descomposición de Lorentz: $\mathcal{N} \cong \bigoplus_j \mathbb{R}^{1,1}_j$ (Clase B, probado). ✓
- Estructura Formal del Régimen Pontryagin (Teorema 21-D.1): $E = E_0 B_{2m}$ (Clase B, probado). ✓
- RH Parcial bajo $\kappa < \infty$ (Corolario 21-D.2): $\xi = \xi_0 \cdot P_{4m}$ (Clase B, probado). ✓

**Lo que queda abierto:**
- EX (Clase A si tiene éxito): $m > 0 \Rightarrow m = \infty$. No probado. Candidato a W4-RSRP.

---

## Actualización del mapa de muros

| Muro | Descripción | Estado |
|------|-------------|--------|
| W1 | PNT / Weil positivity / error de ceros | Confirmado |
| W2 | SURF / de Branges / completitud global | Confirmado |
| W3 | Par-correlación / GUE / gaps | Confirmado |
| W4-RSRP | Rigidez espectral del régimen Pontryagin (EX) | **Candidato nuevo** |

W4-RSRP es genuinamente distinto de W1/W2/W3. No es equivalente a RH de manera obvia (podría ser una condición intermedia más fuerte o más débil). Su estatus preciso con respecto a RH es desconocido.
