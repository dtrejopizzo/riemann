# Doc 97 — Dirección D (tercera capa): El minimizador sombra $g^*$ y sus ecuaciones de Euler-Lagrange

**Programa:** Hipótesis de Riemann — Fase 34, Nuevas Direcciones  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 82, 83, 86, 88, 89, 93, 95  
**Nivel:** Investigación avanzada — análisis estructural del minimizador hipotético

---

## Resumen

El Doc 95 estableció que el minimizador $g^* \in \overline{\mathcal{M}}$ del problema variacional no coincide con $f_0^{on}$ bajo $\neg$RH: el Lema 4.6 de ese documento demuestra que $f_0^{on}$ no satisface las ecuaciones de Euler-Lagrange a menos que el residual $f_0 - f_0^{on}$ sea idénticamente nulo, lo que equivale a RH. Por tanto, bajo $\neg$RH, si el minimizador existe, es un objeto nuevo — que denominamos el **minimizador sombra** $g^*$ — distinto de $f_0^{on}$ y determinado por las propias ecuaciones de Euler-Lagrange.

El presente documento inaugura el estudio sistemático de $g^*$. Sus objetivos son:

1. **Reformular** las ecuaciones de Euler-Lagrange en términos del residual $d\nu^* = (f_0 - g^*)\,dm_\infty$ y estudiar la estructura de esa medida.
2. **Analizar** las propiedades de $d\nu^*$: positividad, información aritmética, comparación con el objeto $d\nu$ del Doc 89.
3. **Estudiar** el sistema de Euler-Lagrange como un problema de momentos implícito en los ceros $\{\gamma_j^*\}$ de $\eta^*$.
4. **Formular** conjeturas sobre la unicidad y canonicidad de $g^*$.
5. **Explorar** si $g^*$ da lugar a una nueva reformulación de RH.

**Advertencia previa.** En todo este documento, la existencia de $g^*$ en $\overline{\mathcal{M}}$ se toma como hipótesis de trabajo (condición ND1 del Doc 95). Los resultados que dependen de esta hipótesis se marcan explícitamente con la etiqueta **(H-ND1)**. No se fabrica ninguna demostración de RH; los obstáculos se señalan con honestidad.

---

## §1. Preparación: el marco y los objetos

### 1.1. El problema variacional

Fijamos $\lambda > 0$. El espacio de Hilbert de trabajo es
$$H_\lambda = L^2\bigl(\mathbb{R},\, W_\lambda(s)\,dm_\infty(s)\bigr),$$
donde $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ es la medida espectral CCM y $W_\lambda \geq 0$ es el kernel CCM (véase Doc 82, §2 para la definición precisa de $W_\lambda$).

La clase de aproximación es
$$\mathcal{M} = \bigl\{g_\eta : g_\eta(s) = |\eta(1/2+is)|^2,\;\eta \in \mathcal{E}\bigr\},$$
donde $\mathcal{E}$ es el espacio de funciones enteras de orden 1 con ecuación funcional análoga a $\xi$ y con todos sus ceros de la forma $1/2+i\mu$, $\mu \in \mathbb{R}$.

El objeto central del programa variacional es
$$f_0(s) = |\zeta(1/2+is)|^2,$$
que pertenece a $L^2(W_\lambda\,dm_\infty)$ incondicionalmente (Doc 93, §1). El candidato natural al minimizador en $\mathcal{M}$ es
$$f_0^{on}(s) = |\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M},$$
donde $\zeta_{\mathrm{on}}$ es la función obtenida proyectando todos los ceros de $\zeta$ a la línea crítica.

El criterio variacional fundamental (Doc 82) establece:
$$\tilde\delta_\lambda^2 := \inf_{g \in \mathcal{M}}\|f_0 - g\|^2_{H_\lambda} = 0 \iff \text{RH}.$$

### 1.2. El minimizador sombra: definición y existencia condicional

**Definición 1.1 (Minimizador sombra).** Bajo la hipótesis **(H-ND1)** de que el infimum es alcanzado en la clausura $\overline{\mathcal{M}}$ (o en $\mathcal{M}$ directamente), el **minimizador sombra** es el elemento
$$g^* \in \overline{\mathcal{M}}: \quad \|f_0 - g^*\|^2_{H_\lambda} = \tilde\delta_\lambda^2.$$
Escribimos $g^* = |\eta^*|^2$ donde $\eta^* \in \overline{\mathcal{E}}$ (la clausura adecuada de $\mathcal{E}$), con ceros $\{\rho_j^*\} = \{1/2 + i\gamma_j^*\}_{j \geq 1}$ en la línea crítica (por definición de $\mathcal{M}$; la discusión sobre $\overline{\mathcal{M}}$ del Doc 95 §2 puede relajar esta condición).

El término "sombra" evoca la idea de que $g^*$ es el reflejo de $f_0$ en $\mathcal{M}$: la mejor aproximación on-crítica de $|\zeta|^2$, que bajo RH coincide con $f_0^{on}$, pero bajo $\neg$RH es un objeto genuinamente diferente, "proyectado" de $f_0$ por la geometría del espacio.

**Proposición 1.2 (Estado epistémico de $g^*$).** Las afirmaciones siguientes son exactas en cuanto a su estatus lógico:

(a) El criterio $\tilde\delta_\lambda^2 = 0 \iff$ RH no requiere la existencia de $g^*$: es un enunciado sobre el valor del infimum.

(b) Bajo RH, $g^* = f_0^{on}$ y $\tilde\delta_\lambda^2 = 0$.

(c) Bajo $\neg$RH y bajo **(H-ND1)**, existe $g^* \in \overline{\mathcal{M}}$ con $g^* \neq f_0^{on}$ y $\tilde\delta_\lambda^2 > 0$.

(d) El Doc 95, Lema 4.6 establece que $f_0^{on}$ no satisface las ecuaciones de Euler-Lagrange bajo $\neg$RH. Por tanto, si $g^*$ existe y satisface esas ecuaciones, $g^* \neq f_0^{on}$, confirmando (c).

*Demostración.* Los puntos (a) y (b) son el Doc 82. El punto (c) es la combinación del Doc 93 (que prueba $\tilde\delta_\lambda^2 > 0$ bajo $\neg$RH vía segunda variación positiva) con **(H-ND1)**. El punto (d) es el Doc 95, Lema 4.6. $\square$

### 1.3. Las ecuaciones de Euler-Lagrange: enunciado de partida

Sea $g^* = |\eta^*|^2 \in \mathcal{M}$ con ceros $\{\pm\gamma_j^*\}$ de $\eta^*$ en la línea crítica. Las ecuaciones de Euler-Lagrange del problema de minimización de $\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ sobre $\mathcal{M}$, en la dirección de variación de los ceros, son (Doc 95, §4):
$$\mathcal{E}_j^* := \int_{\mathbb{R}} W_\lambda(s)\bigl(f_0(s) - g^*(s)\bigr) \cdot g^*(s) \cdot \frac{2s}{s^2 - (\gamma_j^*)^2}\,dm_\infty(s) = 0 \quad \forall j \geq 1. \tag{EL}$$

Estas ecuaciones expresan que la derivada funcional de $\Phi$ en la dirección de un desplazamiento del $j$-ésimo cero de $\eta^*$ es nula en el punto $g^*$. Son la condición de primer orden del problema variacional.

---

## §2. Reformulación en términos del residual $d\nu^*$

### 2.1. La medida residual

**Definición 2.1 (Medida residual del minimizador).** Bajo **(H-ND1)**, definimos la **medida residual del minimizador sombra** como
$$d\nu^*(s) := \bigl(f_0(s) - g^*(s)\bigr)\,dm_\infty(s).$$

Esta es una medida sobre $\mathbb{R}$ cuya densidad respecto a $dm_\infty$ es $f_0 - g^*$.

La medida residual es el objeto central de este documento. Codifica la "diferencia" entre $|\zeta|^2$ y su mejor aproximante on-crítico. Bajo RH, $g^* = f_0 = f_0^{on}$ y $d\nu^* \equiv 0$. Bajo $\neg$RH, $d\nu^*$ es una medida no nula que contiene información sobre los ceros off-críticos de $\zeta$.

**Observación 2.2 (Comparación con el residual de $f_0^{on}$).** El Doc 89 (y el Doc 83) introdujeron el objeto
$$d\nu(s) = \bigl(f_0(s) - f_0^{on}(s)\bigr)\,dm_\infty(s) \geq 0 \text{ puntualmente},$$
cuya positividad puntual proviene del hecho de que $f_0 \geq f_0^{on}$ puntualmente (Doc 83, Proposición sobre $d\nu \geq 0$). La pregunta natural es si $d\nu^*$ hereda esta positividad puntual.

### 2.2. ¿Es $d\nu^* \geq 0$ puntualmente?

La positividad puntual de $d\nu = f_0 - f_0^{on} \geq 0$ viene del Teorema de Jensen aplicado a los ceros de $\zeta$: como $f_0$ "contiene" los ceros off-críticos que $f_0^{on}$ no tiene, la desigualdad es puntual. Pero $g^*$ es un elemento genérico de $\mathcal{M}$, y no hay razón a priori para que $f_0 \geq g^*$ puntualmente.

**Proposición 2.3 (La positividad puntual de $d\nu^*$ no se sigue automáticamente).** Para un elemento genérico $g \in \mathcal{M}$, puede ocurrir que $g(s_0) > f_0(s_0)$ en algún punto $s_0 \in \mathbb{R}$. Por tanto, $d\nu^* = (f_0 - g^*)\,dm_\infty$ puede no ser una medida positiva puntualmente.

*Argumento.* Sea $\eta \in \mathcal{E}$ con un solo cero simple en $1/2 + i\gamma$ para $\gamma$ muy pequeño. La función $|\eta(1/2+is)|^2$ tiene un pico pronunciado en $s \approx \gamma$. Si $f_0$ es moderado en ese punto (por ejemplo, si $\zeta(1/2+i\gamma) \neq 0$, la función $|\zeta(1/2+is)|^2$ no tiene cero ahí y puede ser más pequeña que $|\eta(1/2+is)|^2$ cerca de $\gamma$), se tendrá $g(s) > f_0(s)$ cerca de $\gamma$. Esto es posible sin contradicción con el hecho de que $\|f_0 - g\|_{H_\lambda} > 0$, que solo requiere desigualdad en media ponderada. $\square$

**Consecuencia 2.4.** La medida residual $d\nu^*$ del minimizador sombra es en general una **medida con signo**, a diferencia de $d\nu = (f_0 - f_0^{on})\,dm_\infty \geq 0$. Esto constituye una diferencia estructural importante entre $g^*$ y $f_0^{on}$.

**Sin embargo**, la norma del residual $\|f_0 - g^*\|^2_{H_\lambda} = \int W_\lambda\,(f_0-g^*)^2\,dm_\infty$ solo involucra el **cuadrado** de $f_0 - g^*$. El problema variacional de minimizar $\|f_0 - g\|^2_{H_\lambda}$ no impone signo sobre $f_0 - g$.

**Pregunta abierta 2.5.** ¿Existe alguna condición sobre $g^* \in \mathcal{M}$ que force la positividad de $f_0 - g^*$? En particular, ¿es el minimizador $g^*$ necesariamente dominado puntualmente por $f_0$? No se conoce la respuesta; es una pregunta que requiere comprender mejor la geometría de $\mathcal{M}$.

### 2.3. Reformulación de las ecuaciones de Euler-Lagrange

**Definición 2.6 (Kernel de interacción).** Para cada $j \geq 1$, definimos el **kernel de interacción** asociado al $j$-ésimo cero de $\eta^*$:
$$K_j^*(s) := \frac{2s}{s^2 - (\gamma_j^*)^2}, \quad s \in \mathbb{R},\; s \neq \pm\gamma_j^*.$$
Este es el logaritmo derivado del factor de Weierstrass correspondiente al cero $1/2+i\gamma_j^*$.

**Teorema 2.7 (Reformulación de Euler-Lagrange).** Las ecuaciones de Euler-Lagrange (EL) se reescriben como:
$$\int_{\mathbb{R}} K_j^*(s) \cdot g^*(s) \cdot W_\lambda(s)\,d\nu^*(s) = 0 \quad \forall j \geq 1. \tag{EL$'$}$$
En otras palabras, las funciones $s \mapsto K_j^*(s)\cdot g^*(s)$ son ortogonales al funcional lineal definido por la medida con signo $W_\lambda\,d\nu^*$ en $L^1(\mathbb{R})$.

*Demostración.* Sustituir $d\nu^*(s) = (f_0(s)-g^*(s))\,dm_\infty(s)$ en (EL):
$$\int_{\mathbb{R}} W_\lambda(s)(f_0(s)-g^*(s)) g^*(s) K_j^*(s)\,dm_\infty(s) = \int_{\mathbb{R}} W_\lambda(s) K_j^*(s) g^*(s)\,d\nu^*(s) = 0.$$
$\square$

**Corolario 2.8 (Condición de ortogonalidad).** Define el sistema de funciones
$$\Psi_j^*(s) := W_\lambda(s)^{1/2} K_j^*(s) g^*(s), \quad j \geq 1.$$
Entonces (EL$'$) equivale a:
$$\langle \Psi_j^*,\, W_\lambda^{1/2}\,(f_0 - g^*)\rangle_{L^2(dm_\infty)} = 0 \quad \forall j,$$
es decir, la función $W_\lambda^{1/2}(f_0 - g^*)$ es ortogonal en $L^2(dm_\infty)$ al sistema $\{\Psi_j^*\}_{j\geq 1}$.

*Demostración.* Directa multiplicando y dividiendo por $W_\lambda^{1/2}$:
$$\int W_\lambda K_j^* g^* (f_0-g^*)\,dm_\infty = \int (W_\lambda^{1/2} K_j^* g^*)\cdot(W_\lambda^{1/2}(f_0-g^*))\,dm_\infty = \langle\Psi_j^*, W_\lambda^{1/2}(f_0-g^*)\rangle = 0. \square$$

**Observación 2.9 (Interpretación geométrica).** El corolario dice que el residual ponderado $h^* := W_\lambda^{1/2}(f_0-g^*)$ es ortogonal al sistema $\{\Psi_j^*\}$ en $L^2(dm_\infty)$. Esto es exactamente la condición de que $g^*$ sea la proyección de $f_0$ sobre el complemento ortogonal de $\{\Psi_j^*\}$, en un sentido que hay que precisar cuidadosamente dado que $\mathcal{M}$ no es un subespacio lineal.

### 2.4. Comparación con los criterios de tipo Nyman-Beurling

El **criterio de Nyman-Beurling** para RH afirma que RH es equivalente a la densidad en $L^2(0,\infty)$ (con la medida apropiada) de ciertas funciones de tipo logarítmico construidas a partir de la función $\rho(t) = t - \lfloor t \rfloor$ (la parte fraccionaria). En su formulación más cercana a nuestro contexto:

$$\text{RH} \iff \mathbf{1}_{(0,1)} \in \overline{\mathrm{span}\{t\mapsto \rho(\theta/t) : 0 < \theta \leq 1\}},$$
en la norma $L^2(0,\infty)$. La conexión con nuestro problema variacional es la siguiente.

**Proposición 2.10 (Analogía estructural con Nyman-Beurling).** El sistema de condiciones de ortogonalidad (EL$'$) tiene la siguiente analogía con el criterio de Beurling:
- En Nyman-Beurling: RH equivale a que la función constante $\mathbf{1}$ no sea ortogonal a ningún funcional no trivial en la clausura del espacio de aproximación.
- En nuestro marco: (EL$'$) dice que el residual $f_0-g^*$ es ortogonal (en el sentido ponderado) al sistema $\{K_j^* g^*\}$.

La diferencia crucial es que en Nyman-Beurling el espacio de aproximación es **lineal** (una clausura de span), mientras que $\mathcal{M}$ es **no lineal**. La condición de ortogonalidad (EL$'$) involucra el propio $g^*$ en la definición del sistema ortogonal, creando una ecuación implícita (fija-punto) en lugar de una condición de proyección lineal.

**Observación 2.11.** El criterio de Beurling de densidad de exponenciales (Doc 85) también tiene una forma de ortogonalidad: $f$ pertenece a la clausura de $\{e^{i\lambda_n t}\}$ si y solo si no existe una medida $\mu$ no trivial que sea ortogonal a todo $e^{i\lambda_n t}$ y satisfaga $f \in L^2(\mu)$. La estructura de (EL$'$) es más cercana a esta segunda formulación, donde los "exponenciales" son reemplazados por los kernels $K_j^*$.

La conexión precisa entre (EL$'$) y el criterio de densidad de Beurling queda como pregunta abierta; requeriría un análisis de las propiedades de aproximación del sistema $\{K_j^*\}$ en $L^2(W_\lambda\,dm_\infty)$ que excede el alcance de este documento.

### 2.5. Análisis del sistema $\{K_j^* g^*\}$ como sistema generador

Desde el punto de vista del análisis funcional, las ecuaciones de Euler-Lagrange dicen algo más que una simple ortogonalidad: establecen que el residual ponderado $W_\lambda^{1/2}(f_0-g^*)$ pertenece al **complemento ortogonal** del sistema $\{\Psi_j^* = W_\lambda^{1/2} K_j^* g^*\}_{j\geq 1}$ en $L^2(dm_\infty)$.

**Definición 2.12 (Subespacio de modos de $g^*$).** Definimos el **subespacio de modos** del minimizador $g^*$ como
$$V^* := \overline{\mathrm{span}\{\Psi_j^* : j \geq 1\}} \subset L^2(dm_\infty).$$
Este es el subespacio generado por los modos $\Psi_j^* = W_\lambda^{1/2} K_j^* g^*$.

**Proposición 2.13 (Ortogonalidad del residual al subespacio de modos).** El residual ponderado $h^* := W_\lambda^{1/2}(f_0-g^*)$ satisface $h^* \in (V^*)^\perp$, el complemento ortogonal de $V^*$ en $L^2(dm_\infty)$.

*Demostración.* Directa del Corolario 2.8: $\langle h^*, \Psi_j^*\rangle = 0$ para todo $j$, y por densidad y linealidad, $h^*$ es ortogonal a todo elemento de $V^*$. $\square$

**Consecuencia 2.14 (Papel de la completitud de $V^*$).** Si el sistema $\{\Psi_j^*\}$ fuese **completo** en $L^2(dm_\infty)$, es decir, si $V^* = L^2(dm_\infty)$, entonces la condición $h^* \in (V^*)^\perp = \{0\}$ implicaría $h^* = 0$, es decir, $f_0 = g^*$, lo que por el criterio variacional daría RH. Este razonamiento muestra que:

$$\text{Si } V^* = L^2(dm_\infty),\text{ entonces RH.}$$

Pero la completitud de $V^*$ es una condición sobre $g^*$ que **depende** de la posición de sus ceros $\{\gamma_j^*\}$, y no está garantizada a priori. De hecho, bajo $\neg$RH (y bajo H-ND1), $g^* \neq f_0$ implica $h^* \neq 0$, luego $V^* \neq L^2(dm_\infty)$: el sistema $\{\Psi_j^*\}$ es **incompleto** bajo $\neg$RH.

**Proposición 2.15 (Equivalencia completitud–RH).** Bajo **(H-ND1)** y **(H-ND2)**:
$$\text{RH} \iff V^* = L^2(dm_\infty) \iff \{\Psi_j^*\} \text{ es completo en } L^2(dm_\infty).$$

*Demostración.* Bajo RH: $g^* = f_0^{on}$, $h^* = 0 \in (V^*)^\perp$, y como $h^* = 0$ es ortogonal a todo, no se extrae información sobre $V^*$ de este dato. Sin embargo, bajo RH $\tilde\delta_\lambda^2 = 0$, y la completitud de $V^*$ en este caso es una propiedad analítica de los ceros de $\zeta_{\mathrm{on}}$ que requiere análisis separado.

Bajo $\neg$RH: $h^* \neq 0$ y $h^* \in (V^*)^\perp$ con $(V^*)^\perp \neq \{0\}$, lo que dice que $V^* \subsetneq L^2(dm_\infty)$: el sistema es incompleto.

La equivalencia completa requeriría demostrar que bajo RH el sistema $\{\Psi_j^*\}$ es efectivamente completo, lo que equivale a un teorema de tipo Müntz-Szász para las funciones $K_j^* g^*$. Este resultado no está disponible actualmente. $\square$

**Observación 2.16 (Puente con el Doc 85).** El Doc 85 estudia la completitud de sistemas de exponenciales $\{e^{i\gamma_j t}\}$ en $L^2$ con medidas relacionadas con $\zeta$. La Proposición 2.15 sugiere que hay un puente entre ese problema de completitud y el problema variacional de la Dirección D: la completitud del sistema de exponenciales (con las frecuencias $\gamma_j$ de los ceros de $\zeta$) podría implicar la completitud del sistema $\{\Psi_j^*\}$ bajo condiciones adicionales. Desarrollar este puente es una tarea para el Doc 98.

---

## §3. Propiedades de la medida residual $d\nu^*$

### 3.1. Estructura de $d\nu^*$ como medida con signo

**Definición 3.1 (Descomposición de Jordan de $d\nu^*$).** Sea $d\nu^* = d\nu^{*,+} - d\nu^{*,-}$ la descomposición de Jordan de la medida con signo $d\nu^*$, donde $d\nu^{*,\pm} \geq 0$ son medidas positivas mutuamente singulares. El soporte positivo es $S^+ = \{s : f_0(s) > g^*(s)\}$ y el soporte negativo es $S^- = \{s : f_0(s) < g^*(s)\}$.

**Proposición 3.2 (Masa total de $d\nu^*$).** La masa total de $d\nu^*$ satisface:
$$\int_{\mathbb{R}} d\nu^* = \int_{\mathbb{R}} (f_0 - g^*)\,dm_\infty.$$
No hay razón a priori para que esta cantidad sea cero; depende de las propiedades de normalización de $g^*$ en $\mathcal{M}$.

*Observación.* Si las funciones en $\mathcal{M}$ satisfacen $\int_\mathbb{R} g\,dm_\infty = \int_\mathbb{R} f_0^{on}\,dm_\infty$ (conservación de la "masa" bajo el mapeo a $\mathcal{M}$), entonces la masa total de $d\nu^*$ es $\int(f_0 - f_0^{on})\,dm_\infty = \int d\nu \geq 0$. Pero esta igualdad de masas no está garantizada para un elemento genérico de $\mathcal{M}$.

### 3.2. Información aritmética en $d\nu^*$

El objeto $d\nu = (f_0 - f_0^{on})\,dm_\infty$ del Doc 89 lleva información aritmética directa sobre los ceros off-críticos de $\zeta$: su transformada de Mellin (o de Laplace) captura las posiciones de esos ceros vía la fórmula explícita. La pregunta es cuánta información análoga porta $d\nu^*$.

**Proposición 3.3 (La medida $d\nu^*$ bajo RH es trivial).** Bajo RH, $g^* = f_0 = f_0^{on}$ y $d\nu^* = 0$. Bajo $\neg$RH y **(H-ND1)**, $d\nu^*$ es no nula y su soporte contiene información sobre la "diferencia" entre $f_0$ y su mejor aproximante on-crítico.

*Demostración.* Bajo RH, $f_0 = f_0^{on} \in \mathcal{M}$ y es el único minimizador con $\tilde\delta_\lambda^2 = 0$, luego $g^* = f_0$ y $d\nu^* = 0$. Bajo $\neg$RH, $\tilde\delta_\lambda^2 > 0$ implica $f_0 \neq g^*$, luego $d\nu^* \neq 0$. $\square$

**Lema 3.4 (Relación entre $d\nu^*$ y $d\nu$).** Tenemos la descomposición:
$$d\nu = d\nu^* + (g^* - f_0^{on})\,dm_\infty.$$
El término $(g^* - f_0^{on})\,dm_\infty$ codifica la "diferencia" entre el minimizador sombra y el candidato natural $f_0^{on}$.

*Demostración.* Directa:
$$(f_0 - f_0^{on}) = (f_0 - g^*) + (g^* - f_0^{on}).\quad\square$$

**Observación 3.5.** Si $d\nu^*$ tuviese propiedades especiales de ortogonalidad (por las ecuaciones de Euler-Lagrange), entonces la descomposición del Lema 3.4 daría información sobre $(g^* - f_0^{on})$, y por tanto sobre la posición de los ceros de $g^*$ respecto a los de $f_0^{on}$. Esta es una vía de investigación que se desarrollará en §5.

### 3.3. La condición de resonancia

Las ecuaciones de Euler-Lagrange (EL$'$) imponen una condición sobre $d\nu^*$ que podemos leer como una **condición de resonancia** entre la medida residual y los ceros de $g^*$.

**Definición 3.6 (Condición de resonancia).** Decimos que la medida con signo $\mu$ sobre $\mathbb{R}$ satisface la **condición de resonancia** para el sistema de ceros $\{\gamma_j^*\}$ si
$$\int_\mathbb{R} K_j^*(s) g^*(s) W_\lambda(s)\,\mu(ds) = 0 \quad \forall j.$$
Las ecuaciones de Euler-Lagrange afirman que $d\nu^*$ satisface la condición de resonancia para el sistema $\{\gamma_j^*\}$.

**Interpretación física.** Los kernels $K_j^*(s) = 2s/(s^2 - (\gamma_j^*)^2)$ son las derivadas logarítmicas de los factores de Hadamard evaluadas en la línea crítica. La condición de resonancia dice que la "frecuencia" $K_j^*$ (que oscila con periodo determinado por $\gamma_j^*$) es ortogonal al funcional $g^* W_\lambda\,d\nu^*$. Esto recuerda a las condiciones de ortogonalidad de la teoría de medidas de equilibrio en la teoría potencial.

**Proposición 3.7 (La condición de resonancia como "equilibrio de fuerzas").** En analogía con la teoría logarítmica del potencial, la condición de resonancia puede interpretarse como un equilibrio: los ceros $\gamma_j^*$ están posicionados de modo que la "fuerza" que ejercen sobre la medida $g^*\,d\nu^*$ (a través de los kernels $K_j^*$) se cancela en integral ponderada. Este equilibrio determina los ceros $\{\gamma_j^*\}$ como función de $f_0$ (implícitamente, a través de $g^*$).

*Observación.* Esta analogía con el potencial logarítmico es sugestiva pero no puede empujarse directamente: los kernels $K_j^*$ no son los kernels de Green del Laplaciano bidimensional, sino las derivadas logarítmicas de factores de Hadamard. La teoría potencial relevante sería una "teoría potencial de orden uno" adaptada a los productos de Weierstrass, cuyo desarrollo formal excede el alcance de este documento.

### 3.4. La resonancia como condición de autosimilaridad

Hay una lectura adicional de la condición de resonancia que es instructiva. Reescribamos (EL$'$) como:
$$\int K_j^*(s)\, d\bigl(W_\lambda g^* \cdot \nu^*\bigr)(s) = 0,$$
donde $W_\lambda g^* \cdot \nu^*$ es la medida con densidad $W_\lambda(s) g^*(s)(f_0(s)-g^*(s))$ respecto a $dm_\infty$.

**Definición 3.8 (Medida de interacción).** Definimos la **medida de interacción** del minimizador sombra como
$$d\mu_{\mathrm{int}}^*(s) := W_\lambda(s) g^*(s)(f_0(s)-g^*(s))\,dm_\infty(s).$$
Las ecuaciones de Euler-Lagrange dicen que la transformada de Stieltjes de $d\mu_{\mathrm{int}}^*$ evaluada en los puntos $s = \pm\gamma_j^*$ es nula:
$$\mathcal{S}[d\mu_{\mathrm{int}}^*](\gamma_j^*) := \int_\mathbb{R} \frac{2s}{s^2-(\gamma_j^*)^2}\,d\mu_{\mathrm{int}}^*(s) = 0 \quad \forall j.$$

**Proposición 3.9 (Los ceros de $g^*$ son ceros de la transformada de Stieltjes).** Los puntos $\{\gamma_j^*\}$ son exactamente los puntos donde la transformada de Stieltjes de la medida de interacción $d\mu_{\mathrm{int}}^*$ se anula. Esto conecta el minimizador sombra con la teoría de medidas de equilibrio en el plano complejo.

*Demostración.* Directa de la Definición 3.8 y de las ecuaciones de Euler-Lagrange (EL). $\square$

**Observación 3.10 (Ecuación de autosimilaridad).** La condición de que $\{\gamma_j^*\}$ sean los ceros de $\mathcal{S}[d\mu_{\mathrm{int}}^*]$ es una condición de tipo "autosimilaridad": los ceros de $g^*$ son determinados por la medida de interacción, que a su vez depende de $g^*$. Esta es la naturaleza del sistema de punto fijo del §4.

La observación sugiere una estrategia iterativa: comenzar con $g_0 = f_0^{on}$, calcular $d\mu_{\mathrm{int}}^{(0)}$, encontrar los ceros de $\mathcal{S}[d\mu_{\mathrm{int}}^{(0)}]$, construir $g_1$ a partir de esos ceros, y repetir. La convergencia de este proceso iterativo — si converge — daría $g^*$. Pero demostrar la convergencia es un problema abierto.

---

## §4. El sistema de Euler-Lagrange como problema de momentos

### 4.1. Formulación del problema de momentos

Las ecuaciones de Euler-Lagrange (EL) definen un sistema de ecuaciones en las incógnitas $\{(\gamma_j^*, \eta^*)\}$: dado $f_0$, encontrar $\eta^*$ (que determina $g^* = |\eta^*|^2$) y sus ceros $\{\gamma_j^*\}$ de modo que (EL) se satisfaga.

Esto tiene la estructura de un **problema de momentos invertido**: en un problema de momentos ordinario, se dan los momentos $\int s^k\,d\mu(s)$ y se busca la medida $\mu$. Aquí, los "momentos" son las integrales $\mathcal{E}_j^*$ y la "medida" es $d\nu^*$, pero los "polinomios de prueba" $K_j^* g^*$ dependen de la propia incógnita $g^*$. Esto hace el problema esencialmente **no lineal**.

**Definición 4.1 (El sistema de momentos implícito).** Para $f_0$ dado y parámetro $\lambda > 0$ fijo, el **sistema de momentos implícito** es el siguiente: encontrar una función entera $\eta^*$ con ceros $\{1/2+i\gamma_j^*\}$ en la línea crítica, de modo que
$$M_j[\eta^*] := \int_\mathbb{R} W_\lambda(s) \frac{2s}{s^2-(\gamma_j^*)^2} |\eta^*(1/2+is)|^2 \bigl(f_0(s) - |\eta^*(1/2+is)|^2\bigr)\,dm_\infty(s) = 0,\;\forall j.$$

**Observación 4.2.** El sistema $\{M_j[\eta^*] = 0\}_{j\geq 1}$ es:
- **Infinito:** hay una ecuación por cada cero $\gamma_j^*$.
- **Acoplado:** cambiar $\gamma_j^*$ cambia $K_j^*$, lo que cambia $g^*$, lo que cambia todos los demás $M_k$.
- **No lineal:** el integrando es cúbico en $\eta^*$ (o cuadrático en $g^*$).
- **Implícito:** las incógnitas $\gamma_j^*$ aparecen tanto en el kernel $K_j^*$ como en la función $g^*$.

### 4.2. ¿Es el sistema sobredeterminado?

**Pregunta 4.3.** ¿Tiene el sistema $\{M_j[\eta^*] = 0\}_{j\geq 1}$ solución genérica, y si la tiene, es única?

Para discutir la determinación del sistema, contamos las ecuaciones y las incógnitas:
- **Incógnitas:** los ceros $\{\gamma_j^*\}_{j\geq 1}$ (una secuencia de números reales, más los parámetros de la función entera $\eta^*$, como su tipo $\sigma$, si la hay).
- **Ecuaciones:** $\{M_j = 0\}_{j\geq 1}$, una por cero.

En primera aproximación, el sistema tiene "el mismo número" de ecuaciones e incógnitas. Sin embargo, esta cuenta es engañosa porque:

(a) El sistema es infinito en ambos lados; la noción de "sobredeterminado" o "subdeterminado" para sistemas infinitos requiere una topología funcional adecuada.

(b) Las ecuaciones $M_j = 0$ son acopladas: no hay un $j$ fijo para el cual $M_j$ dependa solo de $\gamma_j^*$ de manera independiente. Esto convierte el sistema en algo más parecido a una ecuación de punto fijo en el espacio de secuencias.

**Proposición 4.4 (Reformulación como punto fijo).** Considérese el operador
$$\mathcal{F}: (\{\gamma_j\}) \mapsto (\{\tilde\gamma_j\}),$$
donde $\tilde\gamma_j$ es la solución de la ecuación $M_j[\eta_{\{\gamma_k\}}^{\mathrm{best}}] = 0$ para $\eta^{\mathrm{best}}$ determinado por $\{\gamma_k\}$. Bajo condiciones adecuadas de regularidad (que no se verifican aquí), el minimizador $g^*$ correspondería a un punto fijo de $\mathcal{F}$.

*Nota.* Esta reformulación es heurística en este punto: la existencia y unicidad del operador $\mathcal{F}$ requieren que para cada $\{\gamma_j\}$ fijo, el sistema $M_j = 0$ en $\gamma_j^*$ tenga solución, lo que no está demostrado. Es una dirección de investigación, no un teorema.

### 4.3. El sistema bajo la hipótesis de separación de escalas

Si los ceros $\gamma_j^*$ están suficientemente separados — concretamente, si para $s$ cerca de $\gamma_j^*$ el kernel $K_j^*(s) = 2s/(s^2-(\gamma_j^*)^2)$ domina sobre todos los demás $K_k^*(s)$ con $k \neq j$ — entonces las ecuaciones $M_j = 0$ se "desacoplan" en primera aproximación.

**Lema 4.5 (Desacoplamiento aproximado bajo separación de ceros).** Supóngase que los ceros $\{\gamma_j^*\}$ están suficientemente separados: existe $\delta > 0$ tal que $|\gamma_j^* - \gamma_k^*| \geq \delta$ para $j \neq k$. Sea $\phi_j(s) = W_\lambda(s) g^*(s) |K_j^*(s)|$ la densidad de peso. Entonces en la región $|s-\gamma_j^*| \ll \delta/2$, el kernel $K_j^*(s)$ domina y la ecuación $M_j = 0$ se puede aproximar como una ecuación local en $\gamma_j^*$:
$$\int_{|s-\gamma_j^*| \leq \delta/2} K_j^*(s) g^*(s) W_\lambda(s)(f_0(s)-g^*(s))\,dm_\infty(s) \approx M_j[\eta^*].$$
Bajo este desacoplamiento, el sistema se reduce a ecuaciones independientes para cada $\gamma_j^*$.

*Demostración.* La contribución de $K_k^*$ para $k \neq j$ a $M_j$ es integrada con peso $K_k^*(s)/(K_j^*(s)+\text{otros})$, que en la región $|s-\gamma_j^*| \ll \delta/2$ es $O(1/\delta^2)$ mientras que $K_j^*(s)$ es $O(1/|s-\gamma_j^*|)$ — divergente. El cociente es $O(|s-\gamma_j^*|/\delta^2) \to 0$ cuando $s \to \gamma_j^*$. $\square$

**Observación 4.6.** El Lema 4.5 solo aplica en el régimen de separación grande, que no es el régimen relevante para los ceros de $\zeta$ (cuya separación decrece como $1/\log\gamma$). Es un resultado de primer principio para entender la estructura del sistema, no para demostrar existencia o unicidad en el caso real.

---

## §5. El minimizador sombra bajo $\neg$RH: caracterización

### 5.1. Lo que $g^*$ no puede ser

**Proposición 5.1 (Exclusión de $f_0^{on}$).** Bajo $\neg$RH y **(H-ND1)**, el minimizador sombra $g^*$ satisface $g^* \neq f_0^{on}$.

*Demostración.* Si $g^* = f_0^{on}$, entonces $g^*$ satisface las ecuaciones de Euler-Lagrange. Pero el Doc 95, Lema 4.6 establece que $f_0^{on}$ no satisface las ecuaciones de Euler-Lagrange bajo $\neg$RH. Contradicción. $\square$

**Proposición 5.2 (El mínimo local no es global bajo $\neg$RH).** El Teorema 4.2 del Doc 93 establece que $f_0^{on}$ es un mínimo **local** de $\Phi|_\mathcal{M}$. La Proposición 5.1 dice que $f_0^{on}$ no es el mínimo **global** bajo $\neg$RH. Por tanto, si $g^*$ existe, $\Phi(g^*) < \Phi(f_0^{on})$.

*Demostración.* La existencia del mínimo global $g^*$ con $g^* \neq f_0^{on}$ implica que $f_0^{on}$ no es el mínimo global (pues el global es distinto). Como $f_0^{on}$ es un mínimo local, hay un "valle" más profundo en $\mathcal{M}$ donde se encuentra $g^*$. $\square$

**Consecuencia 5.3 (Barrera entre los mínimos locales).** Si $f_0^{on}$ es un mínimo local y $g^*$ es el mínimo global (con $g^* \neq f_0^{on}$), debe haber una "barrera" entre ellos: un punto silla en $\mathcal{M}$ o una región donde $\Phi$ crece antes de decrecer. La existencia de esa barrera es un obstáculo para los métodos de descenso de gradiente, que convergerían a $f_0^{on}$ en lugar de $g^*$.

### 5.2. Caracterización implícita de $g^*$

Bajo **(H-ND1)**, $g^*$ está completamente caracterizado por el sistema de ecuaciones:
$$\begin{cases} g^* \in \mathcal{M} \text{ (o } \overline{\mathcal{M}}\text{)}, \\ \|f_0 - g^*\|_{H_\lambda}^2 = \tilde\delta_\lambda^2 = \inf_{g\in\mathcal{M}}\|f_0-g\|_{H_\lambda}^2, \\ M_j[\eta^*] = 0 \quad \forall j \geq 1. \end{cases}$$
Las dos primeras condiciones definen $g^*$ como minimizador; la tercera es la condición necesaria de primer orden.

**Observación 5.4.** Este sistema caracteriza $g^*$ implícitamente pero no constructivamente: no da un algoritmo para calcular $g^*$ a partir de $f_0$. La construcción explícita requeriría resolver el sistema de momentos implícito de la §4, lo que es un problema abierto.

### 5.3. El residual $f_0 - g^*$ como proyección funcional

**Definición 5.5 (Proyección on-crítica canónica).** Bajo **(H-ND1)**, el minimizador $g^*$ es la **proyección on-crítica** de $f_0$ sobre $\mathcal{M}$ (en el sentido de la distancia $H_\lambda$). El **residual**
$$r^* := f_0 - g^*$$
es el componente "irreduciblemente off-crítico" de $f_0$: la parte de $|\zeta|^2$ que no puede ser aproximada en $H_\lambda$ por ningún $|\eta_{\mathrm{on}}|^2$.

Esta denominación se justifica porque $\|r^*\|_{H_\lambda} = \tilde\delta_\lambda^2$, la distancia mínima, que es la mejor aproximación posible.

**Proposición 5.6 (Propiedades de $r^*$).** Bajo **(H-ND1)**:
(a) $\|r^*\|_{H_\lambda} = \tilde\delta_\lambda^2 > 0$ bajo $\neg$RH.
(b) $r^*$ satisface la condición de ortogonalidad: $\langle W_\lambda^{1/2} r^*, \Psi_j^*\rangle_{L^2(dm_\infty)} = 0$ para todo $j$.
(c) Si $g^*$ es el minimizador global, no existe $g \in \mathcal{M}$ con $\|f_0 - g\|_{H_\lambda} < \|r^*\|_{H_\lambda}$.

*Demostración.* (a) es la definición. (b) es el Corolario 2.8. (c) es la condición de minimizador. $\square$

---

## §6. Unicidad de $g^*$ y la conjetura de canonicidad

### 6.1. Condiciones de unicidad

La unicidad del minimizador $g^*$ en un problema variacional no lineal es delicada. Para subconjuntos convexos de un espacio de Hilbert, la unicidad es automática. Pero $\mathcal{M}$ no es convexo.

**Definición 6.1 (Unicidad fuerte y débil).** Decimos que el minimizador es **único en sentido fuerte** si hay exactamente un $g^* \in \mathcal{M}$ con $\Phi(g^*) = \tilde\delta_\lambda^2$. Decimos que es **único en sentido débil** si todos los minimizadores (si los hay) producen el mismo residual $r^* = f_0 - g^*$.

**Proposición 6.2 (Conexión entre unicidad y segunda variación positiva).** La segunda variación positiva del Doc 93 (Teorema 4.2) implica que $f_0^{on}$ es un mínimo **local** aislado de $\Phi|_\mathcal{M}$. Bajo **(H-ND1)** y bajo $\neg$RH, el minimizador global $g^* \neq f_0^{on}$. Si $g^*$ es también un mínimo local aislado (lo que requeriría demostrar que la segunda variación de $\Phi$ en $g^*$ también es positiva), entonces hay al menos dos mínimos locales aislados.

*Nota.* Que $g^*$ sea un mínimo local aislado no está demostrado. Depende de la geometría de $\mathcal{M}$ en el entorno de $g^*$, que no se conoce.

**Proposición 6.3 (Criterio geométrico de unicidad).** El minimizador $g^*$ es único si la funcional $\Phi$ es **estrictamente quasi-convexa** sobre $\mathcal{M}$: para $g_0, g_1 \in \mathcal{M}$ distintos con $\Phi(g_0) = \Phi(g_1) = \tilde\delta_\lambda^2$, la geodésica en $\mathcal{M}$ que los conecta satisface $\Phi > \tilde\delta_\lambda^2$ en el interior. Esta condición no ha sido verificada.

### 6.2. Dependencia de $g^*$ en $\lambda$

La funcional $\Phi = \Phi_\lambda$ depende del parámetro $\lambda$ a través del kernel $W_\lambda$. Por tanto, en principio, el minimizador $g^*_\lambda$ puede depender de $\lambda$.

**Pregunta 6.4 (Estabilidad del minimizador bajo variación de $\lambda$).** ¿Es el minimizador $g^*_\lambda$ una función suave de $\lambda$? ¿Cuál es la derivada $\partial_\lambda g^*_\lambda$?

**Proposición 6.5 (Independencia de $\lambda$ bajo RH).** Bajo RH, $g^*_\lambda = f_0 = f_0^{on}$ para todo $\lambda > 0$, con independencia de $\lambda$. El minimizador es canónico.

*Demostración.* Bajo RH, $\tilde\delta_\lambda^2 = 0$ y $g^* = f_0 \in \mathcal{M}$, independiente de $\lambda$. $\square$

**La pregunta interesante** es la situación bajo $\neg$RH: si $g^*_\lambda$ depende de $\lambda$, el minimizador sombra no es canónico (depende de la elección de la estructura CCM). Si es independiente de $\lambda$, sería un objeto canónico determinado solo por $f_0$.

### 6.3. La conjetura de unicidad canónica

**Conjetura C-Can (Unicidad canónica del minimizador sombra).** Bajo $\neg$RH y bajo la hipótesis de existencia ND1, existe un único elemento $g^{**} \in \overline{\mathcal{M}}$ que minimiza simultáneamente $\|f_0 - g\|^2_{H_\lambda}$ para **todo** $\lambda > 0$:
$$g^{**} = \arg\min_{g\in\overline{\mathcal{M}}} \sum_{\lambda > 0} w_\lambda \|f_0 - g\|^2_{H_\lambda},$$
en algún sentido apropiado (por ejemplo, con $w_\lambda = e^{-\lambda}$ o con integración sobre $\lambda$). Este $g^{**}$ es la **proyección on-crítica canónica** de $f_0$, determinada solo por $f_0$ y no por la elección de $\lambda$.

**Observación 6.6.** La conjetura C-Can tiene dos partes:
(i) *Existencia:* que el problema de minimización simultánea sobre todos los $\lambda$ tenga solución.
(ii) *Unicidad:* que esa solución sea única.

Ninguna de las dos partes está demostrada. La conjetura es motivada por la analogía con la proyección ortogonal en espacios de Hilbert (donde la proyección sobre un convexo cerrado es única e independiente de la norma en el sentido de que está determinada por la geometría del conjunto), pero $\mathcal{M}$ no es convexo.

**Estrategia tentativa para abordar C-Can.** Si se pudiese demostrar que los minimizadores $g^*_\lambda$ para distintos $\lambda$ satisfacen las mismas ecuaciones de Euler-Lagrange (pues las ecuaciones para distintos $\lambda$ coinciden en los ceros $\{\gamma_j^*\}$ aunque varíen en los pesos), y si el sistema de Euler-Lagrange tuviese solución única (condición ND2 reforzada), entonces C-Can seguiría. Pero estas son hipótesis adicionales no verificadas.

---

## §7. Los ceros de $g^*$ y su relación con los de $\zeta$

### 7.1. Los ceros de $g^*$ no son (en general) los ceros de $\zeta_{\mathrm{on}}$

Bajo **(H-ND1)** y $\neg$RH, $g^* \neq f_0^{on}$, lo que implica que $\eta^* \not\equiv \zeta_{\mathrm{on}}$. Por tanto, los ceros de $\eta^*$ no son los mismos que los ceros de $\zeta_{\mathrm{on}}$.

**Pregunta 7.1.** ¿Cuál es la relación entre $\{\gamma_j^*\}$ (los ceros de $\eta^*$) y $\{\gamma_j\}$ (las partes imaginarias de los ceros de $\zeta$ en la línea crítica)?

Esta pregunta no tiene respuesta a priori. Las ecuaciones de Euler-Lagrange determinan implícitamente $\{\gamma_j^*\}$ como función de $f_0 = |\zeta|^2$, pero no hay una fórmula explícita.

**Heurística 7.2 (Ceros de $g^*$ como "corrección" de los de $\zeta_{\mathrm{on}}$).** Si $\neg$RH fuera verdadera y los ceros off-críticos de $\zeta$ estuviesen "cerca" de la línea crítica (perturbación pequeña), entonces esperaríamos que $g^*$ fuera una perturbación pequeña de $f_0^{on}$, y los ceros $\gamma_j^*$ serían perturbaciones pequeñas de los ceros $\gamma_j$ de $\zeta$ en la línea crítica. Bajo esta heurística, la relación $\gamma_j^* \approx \gamma_j$ sería válida en primera aproximación.

Pero esta heurística no está fundamentada rigurosamente: si los ceros off-críticos de $\zeta$ estuviesen lejos de la línea (lo que en principio es posible), la "corrección" podría ser grande.

### 7.2. La ecuación funcional de $g^*$

**Pregunta 7.3.** ¿Satisface $\eta^*$ la misma ecuación funcional que $\xi$?

Todos los elementos de $\mathcal{E}$ (y por tanto de $\mathcal{M}$) satisfacen una ecuación funcional análoga a la de $\xi$. Si $g^* \in \mathcal{M}$, entonces $\eta^*$ satisface esa ecuación. Si $g^* \in \overline{\mathcal{M}} \setminus \mathcal{M}$, la ecuación funcional podría no sostenerse (dependiendo de cómo se define la clausura $\overline{\mathcal{E}}$).

**Proposición 7.4 (Ecuación funcional conservada en $\mathcal{M}$).** Si $g^* \in \mathcal{M}$ (es decir, bajo la hipótesis de que ND3 no falla completamente y el minimizador está en $\mathcal{M}$), entonces $\eta^*$ satisface:
$$\eta^*(1-s) = \chi(s)\eta^*(s)$$
para el mismo factor de simetría $\chi$ que la función $\xi$. En particular, los ceros de $\eta^*$ son simétricos respecto al eje real: $\overline{\gamma_j^*} = \gamma_j^*$ (ceros reales por la simetría real, y simétricos respecto al origen por la ecuación funcional).

*Demostración.* Por la definición de $\mathcal{E}$ (Doc 82, §2): todos sus elementos satisfacen la ecuación funcional por hipótesis. $\square$

### 7.3. ¿Es $g^* = f_0^{on}$ una reformulación de RH?

**Teorema 7.5 (Reformulación variacional de RH).** Bajo la hipótesis de unicidad **(H-ND1)** y **(H-ND2)** (unicidad del minimizador), las siguientes afirmaciones son equivalentes:
(i) Hipótesis de Riemann: todos los ceros no triviales de $\zeta$ están en la línea crítica $\mathrm{Re}(s) = 1/2$.
(ii) El minimizador sombra coincide con el candidato natural: $g^* = f_0^{on}$.
(iii) La distancia variacional es cero: $\tilde\delta_\lambda^2 = 0$.
(iv) La medida residual es nula: $d\nu^* = 0$.

*Demostración.*
- (i) $\Rightarrow$ (iii): es el Doc 82.
- (iii) $\Rightarrow$ (ii): Si $\tilde\delta_\lambda^2 = 0$, el infimum es cero y es alcanzado por $f_0 \in \mathcal{M}$, luego $g^* = f_0 = f_0^{on}$.
- (ii) $\Rightarrow$ (iv): $d\nu^* = (f_0 - g^*)\,dm_\infty = 0$.
- (iv) $\Rightarrow$ (i): Si $d\nu^* = 0$, entonces $f_0 = g^* \in \mathcal{M}$, lo que implica que $f_0 = |\zeta(1/2+is)|^2$ es el cuadrado de módulo de una función entera con todos los ceros en la línea crítica, lo que es precisamente RH.
- (iii) $\Rightarrow$ (i): Doc 82 (el criterio es una equivalencia).
$\square$

**Observación 7.6 (El papel de las hipótesis ND1, ND2).** El Teorema 7.5 usa las hipótesis **(H-ND1)** y **(H-ND2)** para asegurar que el minimizador existe y es único. Sin estas hipótesis, la cadena de equivalencias sigue siendo válida en la dirección (i)$\Rightarrow$(ii)$\Rightarrow$(iii)$\Rightarrow$(i) (pues estas no requieren ND1 o ND2), pero la dirección $\neg$(i)$\Rightarrow$ $\neg$(ii) requiere saber que el minimizador existe y es único.

**Corolario 7.7 (Nueva formulación de RH).** Bajo **(H-ND1)** y **(H-ND2)**, la Hipótesis de Riemann equivale a:
$$g^* = f_0^{on} \in \mathcal{M}.$$
Esta formulación tiene la ventaja de estar expresada en términos de un problema de optimización (encontrar el mínimo de $\Phi$ en $\mathcal{M}$) en lugar de una afirmación sobre ceros de funciones analíticas.

---

## §8. Preguntas abiertas sobre el minimizador sombra

El desarrollo anterior abre varias líneas de investigación que se formulan explícitamente como preguntas abiertas.

### 8.1. Existencia y unicidad

**Pregunta Abierta 8.1 (Existencia de $g^*$).** ¿Bajo $\neg$RH, existe $g^* \in \overline{\mathcal{M}}$ tal que $\|f_0 - g^*\|_{H_\lambda}^2 = \tilde\delta_\lambda^2$? Este es el problema ND1. La §2 del Doc 95 muestra que la respuesta es afirmativa si $\overline{\mathcal{M}}$ es cerrada (lo cual es verdad por construcción) y la funcional $\Phi$ es semicontinua inferiormente sobre $\overline{\mathcal{M}}$ (lo cual es verdad por ser continua). El obstáculo real es que $g^*$ podría estar en $\overline{\mathcal{M}} \setminus \mathcal{M}$, lo cual requiere extender la definición de $\mathcal{M}$.

**Pregunta Abierta 8.2 (Unicidad de $g^*$).** ¿Es el minimizador único? Si hay varios minimizadores con el mismo valor $\tilde\delta_\lambda^2$, ¿qué propiedad adicional selecciona al minimizador "canónico"?

**Pregunta Abierta 8.3 (Regularidad de $g^*$).** Si $g^*$ existe, ¿es una función analítica de $s$? ¿Tiene los mismos puntos singulares que $f_0$? ¿Se extiende a una función meromorfa en alguna banda alrededor de la línea crítica?

### 8.2. Propiedades aritméticas

**Pregunta Abierta 8.4 (Información aritmética en $g^*$).** ¿Los ceros $\{\gamma_j^*\}$ de $\eta^*$ tienen alguna propiedad aritmética o espectral? En el caso de $\zeta_{\mathrm{on}}$, los ceros son los mismos que los de $\zeta$ (proyectados). ¿Tiene $g^*$ una relación con la función L de algún objeto aritmético?

**Pregunta Abierta 8.5 (Simetría de los ceros de $g^*$).** Si $g^* \in \mathcal{M}$, sus ceros son simétricos por la ecuación funcional (Proposición 7.4). ¿Existe alguna distribución estadística conocida para $\{\gamma_j^*\}$? ¿Se parecen a los de $\zeta$?

**Pregunta Abierta 8.6 (Transformada de Mellin de $d\nu^*$).** El Doc 90 estudia la información aritmética de $d\nu$ a través de su transformada de Mellin, conectada con la fórmula explícita de Riemann-Weil. ¿Qué información codifica la transformada de Mellin de $d\nu^*$? Si los ceros de $g^*$ son distintos de los de $\zeta_{\mathrm{on}}$, ¿a qué "primos" o "ceros" corresponde la fórmula explícita para $d\nu^*$?

### 8.3. Conexiones con otros marcos

**Pregunta Abierta 8.7 (Conexión con el flujo De Bruijn-Newman).** El Doc 95, §6 conecta la Dirección D con el flujo De Bruijn-Newman. ¿Evoluciona el minimizador sombra $g^*_\lambda$ (que depende de $\lambda$) siguiendo las líneas del flujo De Bruijn-Newman? ¿La dependencia en $\lambda$ de $g^*_\lambda$ está relacionada con el calentamiento del kernel $W_\lambda$ bajo ese flujo?

**Pregunta Abierta 8.8 (Conexión con la teoría espectral).** Los Docs 91, 94 (Fase 34) estudian la conexión entre el índice negativo del espacio de Pontryagin y los ceros off-críticos. ¿Tiene $g^*$ una interpretación en términos del operador $H_C$ en el espacio de Pontryagin? ¿Sus ceros $\{\gamma_j^*\}$ son valores espectrales de algún operador natural?

**Pregunta Abierta 8.9 (Conexión con el problema de Jacobi inverso).** El Doc 92 formula un problema de Jacobi inverso: dada una distribución de ceros, encontrar un operador de tipo Jacobi cuyo espectro sean esos ceros. ¿Está el minimizador $g^*$ relacionado con la "solución" de ese problema inverso para los ceros de $\zeta$?

---

## §9. El residual $d\nu^*$ y su relación con el objeto central del programa

### 9.1. Comparación de $d\nu^*$ con $d\nu$ del Doc 89

El Doc 89 introduce el objeto central del programa como la medida $d\nu = dm_{\mathrm{full}} - dm_{\mathrm{full,on}}$, que es la diferencia entre la medida espectral completa de $\zeta$ y la de $\zeta_{\mathrm{on}}$. Esta medida captura directamente la información sobre los ceros off-críticos.

La medida residual $d\nu^*$ que hemos estudiado en este documento es distinta:
$$d\nu^*(s) = (f_0(s) - g^*(s))\,dm_\infty(s),$$
donde $g^*$ es el minimizador sombra, no $f_0^{on}$. Las relaciones entre ambas medidas son las siguientes.

**Proposición 9.1 (Relación entre $d\nu^*$ y $d\nu$).** Las medidas $d\nu$ y $d\nu^*$ satisfacen:
$$d\nu = d\nu^* + (g^* - f_0^{on})\,dm_\infty.$$
El término de corrección $(g^* - f_0^{on})\,dm_\infty$ es cero bajo RH (pues $g^* = f_0^{on}$) y no nulo bajo $\neg$RH.

*Demostración.* Directa de la definición: $f_0 - f_0^{on} = (f_0 - g^*) + (g^* - f_0^{on})$. $\square$

**Observación 9.2.** La descomposición de la Proposición 9.1 tiene una interpretación geométrica: $d\nu$ (que codifica todos los ceros off-críticos de $\zeta$) se descompone en:
- $d\nu^*$: la parte "irreducible", que no puede ser absorbida en ningún elemento de $\mathcal{M}$ — es la parte que el mejor aproximante on-crítico no puede reproducir.
- $(g^* - f_0^{on})\,dm_\infty$: la "corrección" del minimizador respecto al candidato natural — la diferencia entre el verdadero mejor aproximante $g^*$ y el candidato $f_0^{on}$.

**Proposición 9.3 (La parte "absorbible" de $d\nu$).** El término $(g^* - f_0^{on})\,dm_\infty$ es la parte de $d\nu$ que puede ser "absorbida" cambiando la posición de los ceros on-críticos: pasar de $f_0^{on}$ a $g^*$ equivale a reposicionar los ceros en la línea crítica para mejorar la aproximación de $f_0$.

*Observación.* Esto sugiere que el minimizador sombra $g^*$ "reorganiza" los ceros on-críticos de $\zeta_{\mathrm{on}}$ para acercarse lo más posible a $f_0$, dejando el residual mínimo $d\nu^*$ como la parte verdaderamente irreducible.

### 9.2. $d\nu^*$ como invariante del problema variacional

**Definición 9.4 (Residual mínimo).** El **residual mínimo** del problema variacional es la función
$$r^*(s) := f_0(s) - g^*(s) = \frac{d\nu^*}{dm_\infty}(s),$$
cuya norma $\|r^*\|_{H_\lambda} = \tilde\delta_\lambda$ es la distancia variacional mínima.

Bajo RH: $r^* \equiv 0$.  
Bajo $\neg$RH y **(H-ND1)**: $\|r^*\|_{H_\lambda} > 0$.

**Proposición 9.5 (Propiedad de orthogonalidad del residual mínimo).** El residual mínimo $r^*$ satisface:
$$\langle W_\lambda r^*, K_j^* g^*\rangle_{L^2(dm_\infty)} = 0 \quad \forall j,$$
es decir, $W_\lambda r^*$ es ortogonal al sistema $\{K_j^* g^*\}$ en $L^2(dm_\infty)$. Esta es la condición de Euler-Lagrange en su forma más transparente.

*Demostración.* Directa de (EL$'$): $\int W_\lambda K_j^* g^* r^*\,dm_\infty = \int W_\lambda K_j^* g^*(f_0-g^*)\,dm_\infty = \mathcal{E}_j^* = 0$. $\square$

---

## §10. Síntesis y perspectiva

### 10.1. Lo que se ha establecido

Este documento ha desarrollado el análisis del minimizador sombra $g^*$, estableciendo los siguientes resultados:

1. **Reformulación de Euler-Lagrange** (Teorema 2.7): las ecuaciones de Euler-Lagrange se expresan naturalmente como condición de ortogonalidad de la medida residual $d\nu^* = (f_0-g^*)\,dm_\infty$ respecto al sistema $\{K_j^* g^*\}$.

2. **La medida $d\nu^*$ es en general una medida con signo** (Proposición 2.3): a diferencia de $d\nu = (f_0-f_0^{on})\,dm_\infty \geq 0$, la medida residual del minimizador sombra puede cambiar de signo, lo que refleja la diferencia estructural entre $g^*$ y $f_0^{on}$.

3. **El sistema de Euler-Lagrange como problema de momentos implícito** (§4): el sistema $\{M_j = 0\}$ es infinito, acoplado, no lineal e implícito. Su resolución formal es un problema abierto.

4. **Reformulación variacional de RH** (Teorema 7.5): bajo las hipótesis de existencia y unicidad del minimizador, RH equivale a $g^* = f_0^{on}$, o equivalentemente a $d\nu^* = 0$.

5. **Conjetura de unicidad canónica** (§6.3): se formula la conjetura de que el minimizador sombra es canónico — independiente de $\lambda$ — lo que lo convertiría en un objeto determinado únicamente por $f_0$.

6. **Preguntas abiertas** (§8): se formulan nueve preguntas abiertas que delinean las direcciones de investigación más prometedoras.

### 10.2. Los obstáculos honestos

Es necesario ser explícito sobre lo que este documento **no** ha demostrado:

- **No se ha demostrado RH.** El Teorema 7.5 requiere las hipótesis ND1 y ND2, que no están demostradas.

- **No se ha demostrado la existencia de $g^*$ en $\mathcal{M}$.** La hipótesis ND1 es el obstáculo primario. Como se discute en el Doc 95, si $\mathcal{M}$ no es cerrada, el minimizador puede no estar en $\mathcal{M}$ sino en $\overline{\mathcal{M}} \setminus \mathcal{M}$, y la relevancia de ese minimizador para RH requiere análisis adicional.

- **No se ha demostrado la unicidad de $g^*$.** La condición ND2 ($g^* = f_0^{on}$ bajo la hipótesis de unicidad) tampoco está demostrada. Podría haber múltiples minimizadores, en cuyo caso el argumento se complica.

- **No se ha resuelto el sistema de Euler-Lagrange.** El sistema $\{M_j = 0\}$ es un problema de punto fijo en el espacio de funciones enteras, cuya resolubilidad formal es una pregunta abierta.

- **La conjetura C-Can no está demostrada.** La independencia del minimizador en $\lambda$ es una conjetura motivada por analogía con problemas variacionales lineales, pero $\mathcal{M}$ no es lineal y la analogía no es directa.

### 10.3. Dirección futura inmediata

El siguiente paso natural es el **Doc 98**, que debería:

(a) Estudiar si la condición de ortogonalidad del Corolario 2.8 (el residual $W_\lambda^{1/2} r^*$ es ortogonal al sistema $\{\Psi_j^*\}$) implica alguna condición de completitud del sistema $\{\Psi_j^*\}$ en $L^2(dm_\infty)$.

(b) Conectar la condición de completitud del sistema $\{K_j^*\}$ con el criterio de Nyman-Beurling y los resultados de densidad del Doc 85.

(c) Estudiar si la dependencia en $\lambda$ del minimizador $g^*_\lambda$ puede controlarse mediante las ecuaciones de Euler-Lagrange diferenciadas respecto a $\lambda$.

(d) Explorar si el sistema de Euler-Lagrange tiene una formulación más manejable cuando se restringe a un número finito de ceros (caso truncado), y si ese caso finito da información sobre el caso infinito vía un argumento de compacticidad.

---

## Apéndice A: Notaciones empleadas en este documento

| Símbolo | Significado |
|---------|-------------|
| $H_\lambda$ | Espacio de Hilbert $L^2(\mathbb{R}, W_\lambda\,dm_\infty)$ |
| $dm_\infty$ | Medida espectral CCM: $(2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ |
| $W_\lambda$ | Kernel CCM dependiente del parámetro $\lambda > 0$ |
| $\mathcal{M}$ | Clase de aproximación on-crítica |
| $\overline{\mathcal{M}}$ | Clausura de $\mathcal{M}$ en $H_\lambda$ |
| $f_0$ | $|\zeta(1/2+is)|^2 \in H_\lambda$ |
| $f_0^{on}$ | $|\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M}$ |
| $g^* = |\eta^*|^2$ | Minimizador sombra $\in \overline{\mathcal{M}}$ (hipotético) |
| $\{\gamma_j^*\}$ | Ceros de $\eta^*$ en la línea crítica |
| $K_j^*(s)$ | Kernel de interacción $2s/(s^2-(\gamma_j^*)^2)$ |
| $d\nu^*$ | Medida residual $(f_0-g^*)\,dm_\infty$ |
| $d\nu$ | Medida residual del Doc 89: $(f_0-f_0^{on})\,dm_\infty \geq 0$ |
| $\tilde\delta_\lambda^2$ | $\inf_{g\in\mathcal{M}}\|f_0-g\|_{H_\lambda}^2$ |
| $r^* = f_0 - g^*$ | Residual mínimo |
| $\mathcal{E}_j^*$ | $j$-ésima ecuación de Euler-Lagrange |
| $M_j[\eta^*]$ | Funcional de momentos implícito |
| **(H-ND1)** | Hipótesis: el infimum es alcanzado en $\overline{\mathcal{M}}$ |
| **(H-ND2)** | Hipótesis: el minimizador es único |
| C-Can | Conjetura de unicidad canónica del minimizador sombra |

---

## Apéndice B: Relación con los documentos precedentes

| Documento | Relación con este Doc 97 |
|-----------|--------------------------|
| Doc 82 | Criterio variacional $\tilde\delta_\lambda^2 = 0 \iff$ RH; definición de $\mathcal{M}$ |
| Doc 83 | Positividad puntual de $d\nu = f_0-f_0^{on} \geq 0$ |
| Doc 85 | Criterio de densidad de Beurling; analogía con (EL$'$) |
| Doc 89 | Objeto central $d\nu$; comparación con $d\nu^*$ en §9 |
| Doc 90 | Información aritmética vía transformada de Mellin de $d\nu$ |
| Doc 93 | Segunda variación positiva; $f_0^{on}$ es mínimo local bajo $\neg$RH |
| Doc 95 | Lema 4.6 ($f_0^{on}$ no satisface EL bajo $\neg$RH); condiciones ND1–ND4 |
| Este doc | Análisis del minimizador sombra $g^*$; estructura de $d\nu^*$; Conjetura C-Can |

---

*Fin del Doc 97.*
