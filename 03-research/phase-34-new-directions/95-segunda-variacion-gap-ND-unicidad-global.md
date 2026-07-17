# Doc 95 — Dirección D (profunda): Gap ND1–ND4, cerradura de $\mathcal{M}$, y unicidad global del minimizador

**Programa:** Hipótesis de Riemann — Fase 34, Nuevas Direcciones  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 82, 83, 86, 88, 89, 93  
**Nivel:** Investigación avanzada — análisis de obstáculos, resultados parciales, obstáculos honestos

---

## Resumen

El Doc 93 estableció que la segunda variación de la funcional de distancia variacional
$$\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{L^2(W_\lambda\,dm_\infty)}$$
en la dirección transversal al espacio $\mathcal{M}$ es positiva bajo $\neg$RH: $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$. Este resultado es estrictamente local: caracteriza la geometría de $\mathcal{M}$ en el entorno de $f_0^{on}$, pero no dice nada sobre el comportamiento global de la funcional $\Phi$.

El presente documento profundiza en la Dirección D atacando las cuatro condiciones no demostradas ND1–ND4 que separan el resultado local del Doc 93 de una demostración de RH:

- **ND1:** El infimum $\tilde\delta_\lambda^2 > 0$ bajo $\neg$RH es alcanzado por algún $g^* \in \mathcal{M}$.
- **ND2:** Si el infimum es alcanzado, el minimizador es único: $g^* = f_0^{on}$.
- **ND3:** $\mathcal{M}$ es cerrada en $L^2(W_\lambda\,dm_\infty)$.
- **ND4:** La barrera de Hadamard extendida: la información sobre posiciones de ceros que se necesita para controlar el mínimo positivo.

**Resultados de este documento:**

- (§2) ND3 es probablemente falsa en su formulación fuerte; se estudia la clausura $\overline{\mathcal{M}}$ y su posible contenido de funciones con ceros off-critical.
- (§3) Bajo la hipótesis de que ND3 falla, se analiza lo que implica para ND1: el infimum puede no ser alcanzado, siendo un límite de funciones en $\mathcal{M}$.
- (§4) Se estudian las ecuaciones de Euler-Lagrange del problema variacional, bajo la hipótesis condicional de que ND1 sea verdadera.
- (§5) Se analiza la conectividad y topología de $\mathcal{M}$, con especial atención a los argumentos de punto crítico único.
- (§6) Se conecta la Dirección D con el flujo De Bruijn-Newman.
- (§7) Se formula el obstáculo residual con precisión.
- (§8) Se formula la Conjetura $\mathbf{C}_D$ y se discute si es más débil, equivalente, o más fuerte que RH.

**Conclusión:** El análisis revela que ND3 es el obstáculo primario: si $\mathcal{M}$ no es cerrada, el argumento variacional clásico no aplica. La clausura $\overline{\mathcal{M}}$ puede contener objetos que no corresponden a funciones enteras con ceros críticos, lo que introduce una degeneración esencial. La Conjetura $\mathbf{C}_D$, tal como se formula en §8, es una conjetura nueva cuya relación con RH es una equivalencia bajo hipótesis adicionales no verificadas, pero que constituye una dirección de investigación precisa.

---

## §1. Recapitulación del estado del arte: Doc 93 y el gap

### 1.1. La situación

Recordamos el marco. Para $\lambda > 0$ fijo, el espacio de Hilbert es
$$H_\lambda = L^2\bigl(\mathbb{R},\, W_\lambda(s)\,dm_\infty(s)\bigr),$$
con $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2\,ds$ y $W_\lambda \geq 0$ el kernel CCM. La clase de aproximación es
$$\mathcal{M} = \bigl\{g_\eta : g_\eta(s) = |\eta(1/2+is)|^2,\; \eta \in \mathcal{E}\bigr\},$$
donde $\mathcal{E}$ es el espacio de funciones enteras de orden 1, con ecuación funcional análoga a $\xi$, y con todos sus ceros de la forma $1/2+i\mu$, $\mu \in \mathbb{R}$.

El criterio variacional del Doc 82 establece:
$$\tilde\delta_\lambda^2 = \inf_{g \in \mathcal{M}} \|f_0 - g\|^2_{H_\lambda} = 0 \iff \text{RH}.$$

El candidato natural al minimizador es $f_0^{on} = |\zeta_{\mathrm{on}}(1/2+is)|^2 \in \mathcal{M}$, donde $\zeta_{\mathrm{on}}$ proyecta todos los ceros a la línea crítica.

El Doc 93 demostró: bajo $\neg$RH, la segunda variación transversal de $\Phi$ en $f_0^{on}$ es positiva. Esto caracteriza $f_0^{on}$ como mínimo local de $\Phi|_\mathcal{M}$ en las direcciones normales estudiadas.

### 1.2. Las condiciones ND1–ND4 formuladas precisamente

Para pasar de la convexidad local al cierre del argumento se necesitan las cuatro condiciones siguientes:

**ND1 (Existencia del minimizador).** Bajo $\neg$RH, $\tilde\delta_\lambda^2 > 0$. La condición ND1 afirma que el infimum es alcanzado: existe $g^* \in \mathcal{M}$ tal que $\|f_0 - g^*\|^2_{H_\lambda} = \tilde\delta_\lambda^2$.

**ND2 (Unicidad del minimizador).** Bajo la hipótesis de que ND1 es verdadera, ND2 afirma que el minimizador $g^*$ es único y que $g^* = f_0^{on}$.

**ND3 (Cerradura de $\mathcal{M}$).** La clase $\mathcal{M}$ es cerrada en $H_\lambda$. Esta condición es una hipótesis analítica sobre el comportamiento de sucesiones en $\mathcal{M}$: si $g_n \in \mathcal{M}$ y $g_n \to g$ en $H_\lambda$, entonces $g \in \mathcal{M}$.

**ND4 (Barrera de Hadamard extendida).** Existe una desigualdad cuantitativa que conecta la distancia $\|f_0 - g\|_{H_\lambda}$ con las posiciones de los ceros de la función entera $\eta$ que define $g = |\eta|^2$, de tal modo que si la distancia es positiva bajo $\neg$RH, las posiciones de los ceros de $g^*$ se pueden controlar.

**Relaciones lógicas entre las condiciones.** Nótese que:
- ND3 implica ND1 cuando $\mathcal{M}$ es nonempty y $f_0 \in H_\lambda$ (argumento clásico de existencia de proyección en cerrado).
- ND2 no se sigue de ND3 sin hipótesis adicionales sobre la convexidad de $\mathcal{M}$.
- ND4 es independiente de ND1–ND3 y tiene un carácter distinto: es una estimación cuantitativa, no una afirmación cualitativa sobre el espacio.

### 1.3. El papel de la segunda variación

El Teorema 4.2 del Doc 93 establece que $f_0^{on}$ es un **mínimo local** de $\Phi|_\mathcal{M}$ bajo $\neg$RH, en el sentido de que todo desplazamiento transversal pequeño aumenta $\Phi$. Pero esto no implica que sea el único mínimo local, ni que sea el mínimo global. El análisis de este documento tiene precisamente el objetivo de estudiar estos puntos.

---

## §2. Ataque a ND3: ¿es $\mathcal{M}$ cerrada en $H_\lambda$?

### 2.1. La pregunta precisa

**Pregunta 2.1.** Sea $(g_n)_{n\geq 1}$ una sucesión en $\mathcal{M}$, de modo que $g_n = |\eta_n|^2$ con $\eta_n \in \mathcal{E}$ para cada $n$. Supóngase que $g_n \to g$ en $H_\lambda$, es decir,
$$\|g_n - g\|^2_{H_\lambda} = \int_\mathbb{R} W_\lambda(s)|g_n(s) - g(s)|^2\,dm_\infty(s) \to 0.$$
¿Se concluye que $g \in \mathcal{M}$?

Para responder a esta pregunta necesitamos entender la relación entre:
(a) la convergencia en $H_\lambda$ de las funciones $g_n = |\eta_n|^2$, y
(b) la convergencia de las funciones enteras $\eta_n$ (o alguna de sus subsucesiones) en alguna topología adecuada.

### 2.2. El peso $W_\lambda\,dm_\infty$ y el decaimiento exponencial

**Lema 2.2 (Decaimiento del peso).** El peso $W_\lambda(s)\,dm_\infty(s)$ tiene decaimiento exponencial en $|s|$. Más precisamente, para $|s| \to \infty$:
$$W_\lambda(s)\,dm_\infty(s) \lesssim |s|^{-1/2} e^{-\pi|s|/2}\,ds.$$

*Demostración (esquema).* La fórmula de Stirling para $\Gamma(1/4+is/2)$ da $|\Gamma(1/4+is/2)|^2 \sim 2\pi\sqrt{|s|/\pi}\,e^{-\pi|s|/2}$ para $|s| \to \infty$ (Abramowitz-Stegun, fórmula 6.1.23). El kernel $W_\lambda(s)$ del formalismo CCM tiene a lo sumo crecimiento polinomial en $|s|$ (Doc 82, §2). El producto da el decaimiento exponencial enunciado. $\square$

**Consecuencia 2.3.** La convergencia $g_n \to g$ en $H_\lambda$ es una condición **débil** sobre el comportamiento de $g_n$ para $|s|$ grande: el peso exponencial suprime las contribuciones de la cola. La convergencia en $H_\lambda$ no controla el comportamiento de $g_n$ en regiones compactas de manera directa.

Sin embargo, la convergencia en $H_\lambda$ implica, por el Lema de Schur (o por la estimación de Chebyshev), que para cualquier compacto $K \subset \mathbb{R}$ y cualquier $\epsilon > 0$:
$$\sup_{s \in K} |g_n(s) - g(s)|^2 \leq \frac{1}{\inf_{s\in K} W_\lambda(s) \cdot dm_\infty(s)/ds} \cdot \|g_n - g\|^2_{H_\lambda} \cdot \frac{1}{\mathrm{meas}(K)} + \epsilon$$
siempre que $W_\lambda > 0$ en $K$. Esto no da convergencia uniforme en compactos directamente, sino solo en media.

### 2.3. Del cuadrado de módulo a la función entera: el problema de levantar la convergencia

El obstáculo fundamental para demostrar ND3 es el siguiente. La convergencia $g_n = |\eta_n|^2 \to g$ en $H_\lambda$ nos dice que los cuadrados de módulo convergen en media ponderada. Pero para concluir que $g \in \mathcal{M}$, necesitamos extraer una función entera $\eta^* \in \mathcal{E}$ tal que $g = |\eta^*|^2$.

El problema tiene dos pasos:

**Paso I:** Extraer de $(\eta_n)$ una subsucesión convergente en alguna topología útil (por ejemplo, convergencia localmente uniforme sobre $\mathbb{C}$).

**Paso II:** Verificar que el límite $\eta^*$ de la subsucesión satisface: (a) es entera de orden 1, (b) tiene ecuación funcional adecuada, (c) tiene todos sus ceros en $\mathrm{Re}(s) = 1/2$.

El Paso I es potencialmente accesible mediante el Teorema de Montel; el Paso II es donde aparecen los obstáculos esenciales.

### 2.4. Aplicación del Teorema de Montel

**Teorema de Montel (forma general).** Sea $\Omega \subset \mathbb{C}$ un dominio y sea $\mathcal{F}$ una familia de funciones holomorfas en $\Omega$. Si $\mathcal{F}$ es localmente acotada (para cada compacto $K \subset \Omega$, existe $C_K > 0$ tal que $|f(z)| \leq C_K$ para toda $f \in \mathcal{F}$ y $z \in K$), entonces $\mathcal{F}$ es normal, es decir, toda sucesión en $\mathcal{F}$ tiene una subsucesión que converge localmente uniformemente en $\Omega$.

**Pregunta 2.4.** ¿Es la familia $\{\eta_n\}_{n\geq 1}$ localmente acotada en $\mathbb{C}$?

Para responder necesitamos vincular la cota en $H_\lambda$ (que involucra $|\eta_n|^2$ sobre la recta $\mathrm{Re}(s) = 0$, es decir, $s$ real) con cotas para $\eta_n$ en el plano complejo.

**Lema 2.5 (Condición necesaria para aplicar Montel).** Sea $\eta \in \mathcal{E}$. La restricción $s \mapsto \eta(1/2+is)$ es una función de la variable real $s$. Para poder usar Montel, necesitamos que la familia $\{\eta_n(1/2+is)\}$ sea localmente acotada como funciones holomorfas de $s$ extendidas al plano complejo.

Si $\eta_n \in \mathcal{E}$ son funciones enteras de orden 1, satisfacen por definición las estimaciones de crecimiento:
$$|\eta_n(z)| \leq C_n \cdot e^{A_n |z|}$$
para constantes $C_n, A_n > 0$ que dependen de $\eta_n$.

La convergencia $\|g_n\|_{H_\lambda} = \||\eta_n|^2\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + \|f_0 - g_n\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + C$ (si la sucesión es acotada en $H_\lambda$) controla la norma $L^2(W_\lambda\,dm_\infty)$ de $|\eta_n(\cdot+1/2\cdot i)|^2$ sobre la recta real. **Pero no controla directamente las constantes $C_n, A_n$.**

**Ejemplo 2.6 (Por qué la cota en $H_\lambda$ no controla el crecimiento de $\eta_n$).** Sea $\eta_n(z) = e^{n(z-1/2)^2}\cdot\eta_0(z)$, donde $\eta_0 \in \mathcal{E}$. Sobre la recta $\mathrm{Re}(z) = 1/2$ (es decir, $z = 1/2+is$), se tiene $e^{n(z-1/2)^2} = e^{n(is)^2} = e^{-ns^2}$. Luego $\eta_n(1/2+is) = e^{-ns^2}\eta_0(1/2+is)$, cuya norma en $H_\lambda$ tiende a cero cuando $n \to \infty$ (el factor $e^{-ns^2}$ decae rápidamente). Pero en el plano complejo, la función $\eta_n(z) = e^{n(z-1/2)^2}\eta_0(z)$ crece sin cota en la dirección real.

Este ejemplo (aunque artificial) muestra que la cota en $H_\lambda$ sobre la línea real no controla el crecimiento en el plano complejo: la familia $\{\eta_n\}$ puede no ser localmente acotada incluso si $\{g_n = |\eta_n|^2\}$ es acotada en $H_\lambda$.

### 2.5. Un caso manejable: normas adicionales

Si se impone a la sucesión $(\eta_n)$ la hipótesis adicional de que las constantes de crecimiento $A_n$ están uniformemente acotadas, el Teorema de Montel sí aplica.

**Proposición 2.7 (Compacidad bajo cota de orden).** Sea $(\eta_n)_{n\geq 1}$ una sucesión en $\mathcal{E}$ con las siguientes propiedades:
(i) $g_n = |\eta_n|^2 \to g$ en $H_\lambda$.
(ii) Existe $A > 0$ tal que $|\eta_n(z)| \leq C e^{A|z|}$ para toda $n$ y todo $z \in \mathbb{C}$ (cota uniforme de orden).
(iii) La sucesión $(\eta_n)$ es normada de manera que $\eta_n(0) = 1$ para todo $n$ (normalización de fase).

Entonces existe una subsucesión $(\eta_{n_k})$ que converge localmente uniformemente en $\mathbb{C}$ a una función entera $\eta^*$ de orden $\leq 1$.

*Demostración.* Bajo la condición (ii), la familia $\{\eta_n\}$ es localmente acotada en $\mathbb{C}$: para cada $R > 0$, $|\eta_n(z)| \leq Ce^{AR}$ para $|z| \leq R$. El Teorema de Montel garantiza la existencia de una subsucesión localmente uniformemente convergente. El límite $\eta^*$ es holomorfo (por el Teorema de Weierstrass para convergencia uniforme de funciones holomorfas) y de orden $\leq 1$ (por la Proposición de Hadamard: si la cota de crecimiento es $Ce^{A|z|}$, el límite tiene orden $\leq 1$). $\square$

**Corolario 2.8.** Bajo las hipótesis de la Proposición 2.7, el límite $g = |\eta^*|^2$ sobre la recta real. Sin embargo, no se garantiza que $\eta^* \in \mathcal{E}$: en particular, no se garantiza que todos los ceros de $\eta^*$ estén en $\mathrm{Re}(s) = 1/2$.

*Prueba del corolario.* La convergencia localmente uniforme $\eta_{n_k} \to \eta^*$ implica $|\eta_{n_k}(1/2+is)|^2 \to |\eta^*(1/2+is)|^2$ uniformemente en compactos de $\mathbb{R}$. Como $g_{n_k} \to g$ en $H_\lambda$ (que implica convergencia en medida), y el límite puntual es $|\eta^*|^2$, se concluye $g = |\eta^*|^2$ casi en todas partes respecto a $W_\lambda\,dm_\infty$. $\square$

**Observación 2.9 (El obstáculo real).** El corolario muestra que la función $g$ es el cuadrado de módulo de una función entera. El problema es que $\eta^*$ puede tener ceros fuera de la línea crítica. Por el Teorema de Hurwitz (convergencia de ceros bajo convergencia localmente uniforme), si los ceros de $\eta_{n_k}$ están todos en $\mathrm{Re}(s) = 1/2$ y convergen a un cero de $\eta^*$, ese cero de $\eta^*$ está también en $\mathrm{Re}(s) = 1/2$. Pero si los ceros de $\eta_{n_k}$ "escapan a infinito" (su parte imaginaria tiende a $\pm\infty$), el límite $\eta^*$ puede perder esos ceros, obteniendo así una función con menos ceros que las aproximantes.

### 2.6. La clausura $\overline{\mathcal{M}}$: descripción tentativa

**Definición 2.10 (Clausura de $\mathcal{M}$).** Definimos la clausura de $\mathcal{M}$ en $H_\lambda$ como
$$\overline{\mathcal{M}} = \bigl\{g \in H_\lambda : \exists (g_n) \subset \mathcal{M} \text{ con } g_n \to g \text{ en } H_\lambda\bigr\}.$$

La pregunta es: ¿qué funciones pertenecen a $\overline{\mathcal{M}} \setminus \mathcal{M}$?

**Proposición 2.11 (Contenido tentativo de $\overline{\mathcal{M}} \setminus \mathcal{M}$).** Sea $g \in \overline{\mathcal{M}}$. Bajo las hipótesis de la Proposición 2.7 (cota uniforme de orden), $g = |\eta^*|^2$ con $\eta^*$ entera de orden $\leq 1$, pero con los siguientes escenarios posibles:

(a) **$\eta^*$ tiene todos sus ceros en $\mathrm{Re}(s) = 1/2$**: en este caso $g \in \mathcal{M}$.

(b) **$\eta^*$ ha "perdido" algunos ceros al paso al límite (ceros que escaparon a infinito)**: en este caso $\eta^*$ tiene menos ceros que las funciones de la sucesión, con los ceros restantes aún en $\mathrm{Re}(s) = 1/2$. Esto corresponde a funciones enteras de orden $< 1$ o con product de Hadamard truncado. Formalmente, $g \notin \mathcal{M}$ si la función no tiene la ecuación funcional correcta.

(c) **Caso degenerado: $\eta^* \equiv 0$**: esto ocurriría si $\|\eta_{n_k}\|_{H_\lambda} \to 0$, pero es incompatible con la hipótesis de acotamiento.

*Demostración.* El Teorema de Hurwitz para convergencia localmente uniforme establece: si $\eta_{n_k}(z_0) = 0$ para todos $k$ suficientemente grandes, entonces $\eta^*(z_0) = 0$. Pero si los ceros de $\eta_{n_k}$ en la sucesión se van acumulando en conjuntos que escapan a infinito, estos ceros no contribuyen al límite. El resultado es una función $\eta^*$ con un subconjunto de los ceros de las $\eta_{n_k}$. $\square$

**Corolario 2.12 (ND3 es probablemente falsa en su formulación fuerte).** La clausura $\overline{\mathcal{M}}$ contiene funciones que no pertenecen a $\mathcal{M}$, correspondientes al caso (b) de la Proposición 2.11. Por tanto, $\mathcal{M}$ no es cerrada en $H_\lambda$.

*Justificación heurística.* Considérese una sucesión de funciones $\eta_n \in \mathcal{E}$ cuyos ceros son $\{1/2 + i\gamma_k^{(n)}\}_{k\geq 1}$, donde $\gamma_k^{(n)} = \gamma_k$ para $k \leq n$ (los primeros $n$ ceros de $\zeta_{\mathrm{on}}$) y $\gamma_k^{(n)} \to +\infty$ para $k > n$ (los ceros restantes se alejan). Al tomar $n \to \infty$, los ceros que escapan contribuyen cada vez menos a $g_n = |\eta_n|^2$ en la norma de $H_\lambda$ (por el decaimiento exponencial del peso), y la sucesión converge en $H_\lambda$ a una función que corresponde a un producto parcial de Hadamard con los primeros ceros únicamente. Esta función límite no tiene la ecuación funcional completa de $\xi$, y no pertenece a $\mathcal{M}$ en el sentido estricto.

### 2.7. Consecuencias para el problema variacional

**Consecuencia 2.13.** Si $\mathcal{M}$ no es cerrada, el infimum $\tilde\delta_\lambda^2 = \inf_{g\in\mathcal{M}}\|f_0 - g\|^2_{H_\lambda}$ puede no ser alcanzado por ningún elemento de $\mathcal{M}$. En ese caso, ND1 falla.

**Consecuencia 2.14.** El infimum puede, sin embargo, ser alcanzado en la clausura $\overline{\mathcal{M}}$. Sea $g^* \in \overline{\mathcal{M}}$ el elemento que minimiza $\|f_0 - g\|_{H_\lambda}$ sobre $\overline{\mathcal{M}}$ (si $\overline{\mathcal{M}}$ es cerrada, lo cual es verdad por definición).

Si $g^* \in \mathcal{M}$, el infimum es alcanzado y ND1 es verdadera.
Si $g^* \in \overline{\mathcal{M}} \setminus \mathcal{M}$, el infimum no es alcanzado en $\mathcal{M}$.

**Consecuencia 2.15.** La condición $\tilde\delta_\lambda^2 = 0 \iff$ RH (Doc 82) continúa siendo válida aunque $\mathcal{M}$ no sea cerrada, pues el criterio solo involucra el valor del infimum, no si es alcanzado. El cierre del argumento no requiere que el mínimo sea alcanzado: lo que se necesita es demostrar que el infimum es cero si y solo si RH.

---

## §3. Análisis del infimum cuando ND3 falla: el infimum como límite

### 3.1. El problema de aproximación en la clausura

Supóngase que ND3 falla, es decir, que $\mathcal{M}$ no es cerrada. El criterio variacional $\tilde\delta_\lambda^2 = 0 \iff$ RH sigue siendo válido, pero el argumento de proyección al convexo cerrado no aplica (pues $\mathcal{M}$ no es convexo ni cerrado).

Para estudiar las propiedades del infimum, definimos la **funcional extendida**:
$$\tilde\Phi(g) = \|f_0 - g\|^2_{H_\lambda} \quad \text{para } g \in \overline{\mathcal{M}}.$$

El problema variacional extendido es:
$$\tilde\delta_\lambda^2 = \inf_{g \in \overline{\mathcal{M}}} \tilde\Phi(g).$$

Por densidad de $\mathcal{M}$ en $\overline{\mathcal{M}}$ y continuidad de $\tilde\Phi$, el infimum sobre $\mathcal{M}$ y sobre $\overline{\mathcal{M}}$ coinciden.

**Proposición 3.1 (El infimum es alcanzado en $\overline{\mathcal{M}}$).** Para todo $\lambda > 0$, el infimum $\tilde\delta_\lambda^2$ es alcanzado en $\overline{\mathcal{M}}$.

*Demostración.* Sea $(g_n) \subset \mathcal{M}$ una sucesión minimizante: $\Phi(g_n) \to \tilde\delta_\lambda^2$. La sucesión $(g_n)$ es acotada en $H_\lambda$ (pues $\|g_n\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + \|f_0 - g_n\|_{H_\lambda} \leq \|f_0\|_{H_\lambda} + \sqrt{\tilde\delta_\lambda^2} + 1$ para $n$ suficientemente grande). En el espacio de Hilbert $H_\lambda$, toda sucesión acotada tiene una subsucesión débilmente convergente: $g_{n_k} \rightharpoonup g^*$ en $H_\lambda$. Como $\tilde\Phi$ es convexa (en $g$) y continua en la topología débil, se concluye que $\tilde\Phi(g^*) \leq \liminf_k \tilde\Phi(g_{n_k}) = \tilde\delta_\lambda^2$. Por definición del infimum, $\tilde\Phi(g^*) \geq \tilde\delta_\lambda^2$, luego $\tilde\Phi(g^*) = \tilde\delta_\lambda^2$. Finalmente, $g^* \in \overline{\mathcal{M}}$ (la clausura es débilmente cerrada como subconjunto convexo... pero $\mathcal{M}$ no es convexo). $\square$

**Advertencia 3.2.** La demostración anterior tiene un defecto: se usa la semicontinuidad débil inferior de $\tilde\Phi$, que sí se cumple al ser $\tilde\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ una función convexa en $g$. Pero la clausura débil de $\mathcal{M}$ es más grande que la clausura fuerte $\overline{\mathcal{M}}$: la clausura débil puede incluir elementos muy ajenos a las funciones de la forma $|\eta|^2$ con $\eta$ entera. Por tanto, el minimizador $g^*$ obtenido por el argumento de semicontinuidad débil puede no tener ninguna relación con funciones enteras.

**Conclusión 3.3.** La existencia de un minimizador en $\overline{\mathcal{M}}$ (en sentido fuerte) requiere un argumento más delicado que combine el Teorema de Montel y las estimaciones de crecimiento, como se discutió en §2. La cuestión queda abierta en general: si la familia de funciones aproximantes no está uniformemente acotada de orden, el límite puede escapar de las funciones enteras.

### 3.2. El caso en que el infimum es positivo: implicaciones bajo $\neg$RH

Bajo $\neg$RH, $\tilde\delta_\lambda^2 > 0$. Si el infimum es alcanzado por $g^* \in \overline{\mathcal{M}}$, hay dos subcasos:

**Subcaso 3.4(a):** $g^* \in \mathcal{M}$. Entonces $g^* = |\eta^*|^2$ con $\eta^* \in \mathcal{E}$: todos los ceros de $\eta^*$ están en la línea crítica y $g^*$ es el minimizador "honesto". Las condiciones ND1 y ND3 serían verdaderas.

**Subcaso 3.4(b):** $g^* \in \overline{\mathcal{M}} \setminus \mathcal{M}$. Entonces $g^* = |\eta^*|^2$ con $\eta^*$ entera, pero $\eta^*$ tiene algún cero fuera de la línea crítica, o bien $\eta^*$ corresponde a un producto de Hadamard "incompleto" (infinitely many ceros de $\mathcal{E}$ han escapado a infinito). En este caso, el infimum es alcanzado en la clausura pero no en $\mathcal{M}$: ND1 falla, ND3 falla, y el criterio variacional sigue siendo válido.

**Observación 3.5.** El Subcaso 3.4(b) es el más peligroso para el programa. Si el mínimo se alcanza fuera de $\mathcal{M}$, no podemos concluir nada sobre RH directamente del minimizador. El criterio variacional del Doc 82 dice que el infimum **sobre $\mathcal{M}$** es cero iff RH, pero si el verdadero mínimo (alcanzado en $\overline{\mathcal{M}} \setminus \mathcal{M}$) es positivo, eso no contradice RH.

---

## §4. Ecuaciones de Euler-Lagrange bajo la hipótesis ND1

### 4.1. Planteamiento del problema variacional condicionado

Supóngase (condicionalmente) que ND1 es verdadera: existe $g^* \in \mathcal{M}$ que minimiza $\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ sobre $\mathcal{M}$. Escribimos $g^* = |\eta^*|^2$ con $\eta^* \in \mathcal{E}$.

Para todo $\eta \in \mathcal{E}$ y todo $t \in \mathbb{R}$ suficientemente pequeño, la perturbación $\eta^*_t = \eta^* + t\cdot v$ (con $v$ una "variación tangente" a $\mathcal{E}$ en $\eta^*$) da una curva de funciones en $H_\lambda$. Las ecuaciones de Euler-Lagrange corresponden a la condición de que la primera variación de $\Phi$ se anule en $\eta^*$ en toda dirección tangente admisible.

**Definición 4.1 (Variación admisible).** Decimos que $v : \mathbb{R} \to \mathbb{R}$ es una **variación admisible** en $\eta^* \in \mathcal{E}$ si existe una curva $\epsilon \mapsto \eta_\epsilon \in \mathcal{E}$ con $\eta_0 = \eta^*$ y $\frac{d}{d\epsilon}\eta_\epsilon|_{\epsilon=0} = v$. Las variaciones admisibles son las que corresponden a mover los ceros de $\eta^*$ dentro de la línea crítica (variaciones tangentes) o a deformar la normalización de la ecuación funcional.

**Proposición 4.2 (Ecuación de Euler-Lagrange).** Si $g^* = |\eta^*|^2$ minimiza $\Phi$ sobre $\mathcal{M}$, entonces para toda variación admisible $v$:
$$\langle f_0 - g^*, \delta_{v}(|\eta^*|^2)\rangle_{H_\lambda} = 0,$$
donde $\delta_v(|\eta^*|^2)$ es la variación primera de $|\eta^*|^2$ en la dirección $v$.

*Demostración.* Por la condición de mínimo, $\frac{d}{d\epsilon}\Phi(\eta^*_\epsilon)\big|_{\epsilon=0} = 0$. Desarrollando:
$$\frac{d}{d\epsilon}\|f_0 - |\eta_\epsilon^*|^2\|^2_{H_\lambda}\bigg|_{\epsilon=0} = -2\langle f_0 - |\eta^*|^2,\, \partial_\epsilon|\eta^*_\epsilon|^2\big|_{\epsilon=0}\rangle_{H_\lambda} = 0.$$
El resultado enunciado es la reescritura de esta condición. $\square$

### 4.2. Desarrollo de las ecuaciones de Euler-Lagrange para variaciones tangentes

Sea $v_j$ la variación tangencial que mueve el $j$-ésimo par de ceros $1/2 \pm i\gamma_j^*$ de $\eta^*$ al punto $1/2 \pm i(\gamma_j^* + \epsilon)$. Como se calculó en el Doc 93 §2 y §3, la variación de $|\eta^*|^2$ en esta dirección es:
$$\delta_{v_j}(|\eta^*|^2)(s) = \frac{\partial}{\partial\epsilon}|\eta^*_\epsilon(1/2+is)|^2\bigg|_{\epsilon=0} = -2g^*(s) \cdot \left[\frac{1}{(s-\gamma_j^*)} + \frac{1}{(s+\gamma_j^*)}\right] + \text{(términos de fase)}.$$

La ecuación de Euler-Lagrange para la variación $v_j$ es entonces:
$$\int_\mathbb{R} W_\lambda(s)\,(f_0(s) - g^*(s)) \cdot g^*(s) \cdot \left[\frac{1}{s - \gamma_j^*} + \frac{1}{s + \gamma_j^*}\right] dm_\infty(s) = 0.$$

**Observación 4.3.** Esta ecuación tiene una estructura interesante: es una condición de ortogonalidad entre $f_0 - g^*$ (el residuo) y la variación $g^*(s)/((s-\gamma_j^*)(s+\gamma_j^*))$ (que involucra la posición del $j$-ésimo cero de $g^*$). Para cada cero $\gamma_j^*$ del minimizador, hay una ecuación de este tipo.

**Proposición 4.4 (Sistema de ecuaciones del minimizador).** Si $g^* = |\eta^*|^2$ es el minimizador y $\{\gamma_j^*\}$ son las partes imaginarias de los ceros de $\eta^*$, entonces para todo $j$:
$$\int_\mathbb{R} W_\lambda(s)\, (f_0(s) - g^*(s)) \cdot g^*(s) \cdot \frac{2s}{s^2 - (\gamma_j^*)^2}\, dm_\infty(s) = 0.$$

*Demostración.* Se simplifica la suma $\frac{1}{s-\gamma_j^*} + \frac{1}{s+\gamma_j^*} = \frac{2s}{s^2 - (\gamma_j^*)^2}$ y se sustituye en la ecuación de Euler-Lagrange. $\square$

### 4.3. ¿Implican las ecuaciones de Euler-Lagrange que $g^* = f_0^{on}$?

**Pregunta 4.5.** Sea $g^*$ un minimizador de $\Phi$ sobre $\mathcal{M}$. ¿Satisface necesariamente $g^* = f_0^{on}$?

Para responder, comparamos las ecuaciones de Euler-Lagrange de $g^*$ con las de $f_0^{on}$.

Si $g^* = f_0^{on}$ (con ceros en $\gamma_j^* = \gamma_j$, las partes imaginarias de los ceros de $\zeta_{\mathrm{on}}$), las ecuaciones son:
$$\int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_0^{on}(s)) \cdot f_0^{on}(s) \cdot \frac{2s}{s^2 - \gamma_j^2}\, dm_\infty(s) = 0 \quad \forall j.$$

Esta es una condición de ortogonalidad del residuo $f_0 - f_0^{on}$ contra las funciones $f_0^{on}(s) \cdot s / (s^2 - \gamma_j^2)$.

**Lema 4.6 (No-ortogonalidad bajo $\neg$RH).** Bajo $\neg$RH, la condición de Euler-Lagrange para $g^* = f_0^{on}$ NO se satisface en general.

*Demostración.* Si RH es falsa, $f_0 \neq f_0^{on}$ y el residuo $D_0 = f_0 - f_0^{on} > 0$ en un conjunto de medida positiva. Para que la ecuación de Euler-Lagrange se satisfaga con $g^* = f_0^{on}$, necesitaríamos que $D_0(s) \cdot f_0^{on}(s) \cdot s / (s^2 - \gamma_j^2)$ fuera ortogonal a $1$ en $L^2(W_\lambda\,dm_\infty)$ para cada $j$. No hay razón general por la que esto se cumpla: $D_0$ tiene una estructura específica determinada por los ceros off-critical de $\zeta$, y la condición de ortogonalidad es una condición adicional no evidente. $\square$

**Consecuencia 4.7.** El Lema 4.6 muestra que, bajo $\neg$RH, $f_0^{on}$ no satisface las ecuaciones de Euler-Lagrange del problema variacional. Esto es consistente con el hecho de que, bajo $\neg$RH, $f_0^{on}$ no es el minimizador global de $\Phi|_\mathcal{M}$ (el minimizador global, si existe, es algún $g^* \neq f_0^{on}$). El Doc 93 estableció que $f_0^{on}$ es un mínimo local, pero el mínimo global puede estar en otro lugar.

**Observación 4.8 (El papel del Doc 82).** El criterio del Doc 82 no afirma que $f_0^{on}$ sea el minimizador bajo $\neg$RH: afirma que el infimum es positivo bajo $\neg$RH. El candidato $f_0^{on}$ es un punto de $\mathcal{M}$ que está "cerca" de $f_0$, pero no necesariamente el más cercano.

### 4.4. Ecuación funcional heredada y rigidez del minimizador

**Pregunta 4.9.** Si $g^* = |\eta^*|^2$ es el minimizador, ¿satisface $\eta^*$ alguna ecuación funcional heredada de $\zeta$?

La función $\zeta$ satisface la ecuación funcional $\xi(s) = \xi(1-s)$. La función $\zeta_{\mathrm{on}}$ fue construida para satisfacer la misma ecuación funcional (todos los ceros proyectados simétricamente). Un minimizador general $\eta^* \in \mathcal{E}$ también satisface la ecuación funcional análoga por definición de $\mathcal{E}$.

Sin embargo, la pregunta es si la ecuación de Euler-Lagrange junto con la ecuación funcional determina unívocamente al minimizador.

**Proposición 4.10 (Restricción del sistema de Euler-Lagrange).** El sistema de ecuaciones del minimizador (Proposición 4.4) junto con la condición de que $\eta^* \in \mathcal{E}$ (orden 1, ecuación funcional, ceros en la línea crítica) forma un sistema sobredeterminado en general. Específicamente:

- Hay infinitas incógnitas: los ceros $\{\gamma_j^*\}_{j\geq 1}$ del minimizador.
- Hay infinitas ecuaciones: una para cada $j$.
- Las ecuaciones son acopladas entre sí (el factor $g^*(s) = \prod_k |s^2 - (\gamma_k^*)^2 + \ldots|^{-1}$ involucra todos los ceros).

La existencia de solución a este sistema (es decir, la existencia del minimizador) no está garantizada, y la unicidad de la solución tampoco.

**Observación 4.11.** Este análisis apunta a una conclusión importante: incluso bajo la hipótesis ND1 (existencia del minimizador), el estudio de las ecuaciones de Euler-Lagrange no resuelve el problema de unicidad (ND2). El sistema de ecuaciones es demasiado general para determinar de manera única al minimizador, a menos que se impongan condiciones adicionales.

---

## §5. Conectividad y topología de $\mathcal{M}$

### 5.1. $\mathcal{M}$ como espacio parametrizado

La clase $\mathcal{M}$ puede describirse mediante los imaginarios de los ceros:
$$\mathcal{M} \simeq \bigl\{\{\gamma_n\}_{n\geq 1} \subset \mathbb{R} : \gamma_1 \leq \gamma_2 \leq \cdots, \text{ con la condición de integrabilidad adecuada}\bigr\} / \sim,$$
donde la equivalencia $\sim$ identifica sucesiones que definen la misma función en $H_\lambda$.

Más precisamente, una función $\eta \in \mathcal{E}$ está determinada (salvo normalización) por la sucesión de sus ceros $\{1/2 + i\gamma_n\}_{n\geq 1}$ con $\gamma_n \in \mathbb{R}$, mediante el producto de Hadamard:
$$\eta(s) = e^{A+Bs} \prod_{n\geq 1} \left(1 - \frac{s}{1/2+i\gamma_n}\right)\left(1 - \frac{s}{1/2-i\gamma_n}\right) e^{2s/(1+4\gamma_n^2)}.$$

La condición de que $\eta \in H_\lambda$ (es decir, $|\eta|^2 \in H_\lambda$) impone restricciones sobre la densidad de los ceros $\gamma_n$.

**Definición 5.1 (Espacio de parámetros).** Denotamos por
$$\mathcal{P} = \bigl\{\Gamma = \{\gamma_n\}_{n\geq 1} \subset \mathbb{R} : \Gamma \text{ tiene la densidad adecuada y define } \eta_\Gamma \in \mathcal{E} \text{ con } \eta_\Gamma \in H_\lambda\bigr\}$$
el espacio de sucesiones de ceros que parametrizan las funciones de $\mathcal{E}$ relevantes.

### 5.2. Conectividad de $\mathcal{M}$ por caminos

**Proposición 5.2 (Conectividad por caminos de $\mathcal{M}$).** $\mathcal{M}$ es conexo por caminos en la topología de $H_\lambda$.

*Demostración.* Sean $g_0 = |\eta_0|^2$ y $g_1 = |\eta_1|^2$ dos elementos de $\mathcal{M}$, con ceros $\Gamma_0 = \{\gamma_n^{(0)}\}$ y $\Gamma_1 = \{\gamma_n^{(1)}\}$ respectivamente. Definimos el camino lineal en el espacio de parámetros:
$$\Gamma_t = \{(1-t)\gamma_n^{(0)} + t\gamma_n^{(1)}\}_{n\geq 1} \quad \text{para } t \in [0,1].$$

Para cada $t$, la sucesión $\Gamma_t$ define (formalmente) una función entera $\eta_t \in \mathcal{E}$ mediante el producto de Hadamard. Todos los ceros de $\eta_t$ son de la forma $1/2 + i\gamma_n^{(t)}$ con $\gamma_n^{(t)} \in \mathbb{R}$, luego $\eta_t \in \mathcal{E}$ y $g_t = |\eta_t|^2 \in \mathcal{M}$.

La continuidad del mapa $t \mapsto g_t$ en $H_\lambda$ se sigue de la convergencia uniforme en compactos de los productos de Hadamard bajo perturbaciones continuas de los ceros, más el decaimiento exponencial del peso $W_\lambda\,dm_\infty$. (La regularización a través del control de los factores exponenciales en la integrabilidad es un argumento técnico estándar que omitimos.)

Así, $t \mapsto g_t$ es un camino en $\mathcal{M}$ que conecta $g_0$ con $g_1$. $\square$

**Observación 5.3 (Precaución).** La demostración anterior es un esquema; los detalles técnicos sobre la continuidad del mapa $\Gamma \mapsto g_\Gamma \in H_\lambda$ requieren estimaciones cuidadosas sobre la convergencia de productos de Hadamard con ceros variables. En particular, cuando los ceros $\gamma_n^{(0)}$ o $\gamma_n^{(1)}$ no son acotados, la interpolación lineal puede no definir funciones en $\mathcal{E}$ para todo $t$.

### 5.3. Conectividad y unicidad del mínimo local

**Proposición 5.4 (Conectividad no implica unicidad del mínimo).** El hecho de que $\mathcal{M}$ sea conexo por caminos no implica que la funcional $\Phi|_\mathcal{M}$ tenga un único mínimo local.

*Demostración.* Es un hecho general en análisis variacional: una funcional continua en un espacio conexo por caminos puede tener múltiples mínimos locales. El ejemplo más simple: $f(x) = (x^2-1)^2$ en $\mathbb{R}$ tiene dos mínimos locales en $x = \pm 1$ y el dominio $\mathbb{R}$ es conexo por caminos. $\square$

**Sin embargo,** la conectividad sí proporciona información cuando se combina con la positividad de la segunda variación:

**Proposición 5.5 (Unicidad bajo curvatura positiva global).** Si la funcional $\Phi|_\mathcal{M}$ satisface que su hessiana (en el sentido de la segunda variación en todas las direcciones tangentes y normales) es positiva definida en todos los puntos de $\mathcal{M}$, y si $\mathcal{M}$ es conexo, entonces $\Phi|_\mathcal{M}$ tiene a lo más un mínimo local, que es necesariamente el mínimo global.

*Demostración.* La positividad de la hessiana en todo punto implica que $\Phi|_\mathcal{M}$ es estrictamente convexa (en el sentido geodésico). En una variedad conexa con funcional estrictamente convexa, no puede haber dos mínimos locales. $\square$

**Advertencia 5.6.** La hipótesis de la Proposición 5.5 (positividad de la hessiana en todos los puntos) es mucho más fuerte que lo demostrado en el Doc 93 (positividad de la segunda variación transversal en el punto $f_0^{on}$). El Doc 93 solo dice que $f_0^{on}$ es un mínimo local bajo $\neg$RH. No hay información sobre la segunda variación en otros puntos de $\mathcal{M}$.

### 5.4. El espacio de parámetros y su topología

**Descripción 5.7 (Topología del espacio de parámetros $\mathcal{P}$).** El espacio $\mathcal{P}$ de sucesiones de ceros reales admisibles es un espacio métrico con la distancia:
$$d(\Gamma, \Gamma') = \sum_{n\geq 1} \frac{|\gamma_n - \gamma_n'|}{1 + |\gamma_n - \gamma_n'|} \cdot w_n,$$
donde $\{w_n\}$ son pesos apropiados que garantizan la convergencia de la serie. El mapa $\Gamma \mapsto g_\Gamma \in H_\lambda$ es continuo respecto a esta métrica (bajo hipótesis técnicas sobre el crecimiento de $|\gamma_n|$).

La topología de $\mathcal{P}$ como subconjunto del espacio de sucesiones es compleja: es un espacio de dimensión infinita, no localmente compacto en general.

**Observación 5.8.** La complejidad topológica de $\mathcal{P}$ es precisamente lo que hace difícil el análisis global de $\Phi|_\mathcal{M}$. A diferencia de los problemas variacionales en dimensión finita, donde se puede usar la compacidad para garantizar la existencia del mínimo, el problema infinito-dimensional requiere cotas adicionales sobre las sucesiones minimizantes.

---

## §6. Conexión con el flujo De Bruijn-Newman

### 6.1. Recapitulación del flujo DBN

El flujo De Bruijn-Newman (DBN) define una familia uniparamétrica de funciones enteras $\Xi_t$ por:
$$\Xi_t(s) = \int_0^\infty \Phi(u) e^{tu^2} \cos(su)\,du,$$
donde $\Phi(u)$ es la función de De Bruijn. Para cada $t \geq 0$, $\Xi_t$ es una función entera de orden 1 (bajo RH: de orden $\leq 1$). La constante De Bruijn-Newman $\Lambda$ es el ínfimo de los valores de $t$ para los cuales $\Xi_t$ tiene todos sus ceros reales. Se sabe (Rodgers-Tao, 2020) que $0 \leq \Lambda \leq 1/2$.

Las curvas $t \mapsto f_t = |\Xi_t|^2$ (evaluadas en $\mathbb{R}$) definen una trayectoria en $H_\lambda$ (bajo hipótesis de integrabilidad). Para $t > \Lambda$, los ceros de $\Xi_t$ están en $\mathbb{R}$, lo que corresponde a que $f_t \in \mathcal{M}$ (identificando ceros reales de $\Xi_t$ con los puntos $s = \gamma$ de la línea crítica $1/2 + is$).

Para $t = 0$, $\Xi_0 = \xi$ (la función xi de Riemann), y $\Lambda = 0 \iff$ RH.

### 6.2. El flujo DBN como curva en $H_\lambda$

**Proposición 6.1 (La trayectoria DBN en $H_\lambda$).** La curva $t \mapsto f_t = |\Xi_t(1/2+i\cdot)|^2$ es una curva suave en $H_\lambda$ para $t > 0$, con derivada:
$$\partial_t f_t(s) = 2|\Xi_t(1/2+is)|^2 \cdot \mathrm{Re}\left[\frac{\partial_t \Xi_t(1/2+is)}{\Xi_t(1/2+is)}\right].$$

Para $t > \Lambda$ (todos los ceros de $\Xi_t$ son reales), los puntos $f_t \in \mathcal{M}$ (identificando los ceros con la parametrización de $\mathcal{E}$).

*Demostración (esquema).* La diferenciabilidad en $t$ se sigue de la fórmula integral de $\Xi_t$ y de estimaciones sobre la convergencia de la diferenciación bajo el signo integral. Para $t > \Lambda$, los ceros de $\Xi_t$ son reales, luego $\Xi_t(1/2+is) = |\Xi_t(1/2+is)|e^{i\phi_t(s)}$ con $\phi_t(s)$ la fase. El valor real de $\Xi_t$ sobre la recta real (ya que $\phi$ es entero con ceros reales) implica $f_t \in \mathcal{M}$ en el sentido adecuado. $\square$

### 6.3. Monotonía de $\tilde\delta_\lambda^2(t) = \|f_0 - f_t\|^2_{H_\lambda}$

**Definición 6.2.** Para $t > \Lambda$, definimos la distancia de la trayectoria DBN a $f_0$:
$$D(t) = \|f_0 - f_t\|^2_{H_\lambda} = \int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_t(s))^2\,dm_\infty(s).$$

**Pregunta 6.3.** ¿Es $D(t)$ monótona en $t$?

**Proposición 6.4 (Derivada temporal de $D(t)$).** Para $t > \Lambda$:
$$\frac{d}{dt}D(t) = -2\int_\mathbb{R} W_\lambda(s)\,(f_0(s) - f_t(s))\,\partial_t f_t(s)\,dm_\infty(s).$$

*Demostración.* Derivación directa bajo el signo integral, justificada por la diferenciabilidad de $f_t$ en $H_\lambda$. $\square$

**Observación 6.5.** El signo de $\frac{d}{dt}D(t)$ depende de la correlación entre el residuo $f_0 - f_t$ y la velocidad $\partial_t f_t$ del flujo. Si el flujo DBN "empuja" $f_t$ hacia $f_0$, esperamos $\frac{d}{dt}D(t) < 0$, es decir, que la distancia decrece.

### 6.4. Relación entre la segunda variación y la monotonía del flujo

El Doc 93 estableció que la segunda variación transversal de $\Phi$ en el punto $f_0^{on}$ es positiva: $\psi''(0) = 8\mathcal{Q}_\lambda^{(j)} > 0$. Esto significa que, en el entorno de $f_0^{on}$, la funcional $\Phi$ crece en la dirección transversal. Si el flujo DBN pasa cerca de $f_0^{on}$ (lo cual esperamos dado que $f_0^{on}$ es el "punto más cercano" a $f_0$ en $\mathcal{M}$), la curvatura positiva debería "empujar" la trayectoria de vuelta hacia $\mathcal{M}$.

**Proposición 6.6 (Conexión heurística entre curvatura y flujo).** Sea $t_0 > \Lambda$ y supóngase que $f_{t_0}$ está cerca de $f_0^{on}$ en $H_\lambda$. Si la velocidad del flujo DBN en $t_0$ tiene componente en la dirección transversal $b_j$ (es decir, $\langle \partial_t f_t|_{t=t_0}, b_j\rangle_{H_\lambda} \neq 0$), entonces la segunda variación positiva implica que la derivada de $D(t)$ en la dirección transversal es positiva: el flujo aleja $f_t$ de $\mathcal{M}$ en la dirección $b_j$ en un primer momento, pero la curvatura positiva de $\Phi$ garantiza que $D(t)$ crecerá si el flujo se aleja transversalmente.

*Demostración (informal).* Sea $\epsilon$ pequeño y $f_{t_0+\epsilon} \approx f_{t_0} + \epsilon \partial_t f_t|_{t_0}$. Si $\partial_t f_t|_{t_0} = \alpha b_j + (\text{componentes tangentes})$ con $\alpha \neq 0$, entonces:
$$D(t_0 + \epsilon) \approx D(t_0) + \epsilon \langle f_t|_{t_0} - f_0, \partial_t f_t|_{t_0}\rangle_{H_\lambda} + \frac{\epsilon^2}{2} \psi''(0).$$
La positividad de $\psi''(0)$ garantiza que la variación cuadrática es positiva, pero el término lineal puede tener cualquier signo. La proposición no da conclusión definitiva sobre la monotonía de $D(t)$. $\square$

**Advertencia 6.7.** La Proposición 6.6 es heurística y no establece una conclusión rigurosa. La conexión precisa entre la segunda variación en un punto de $\mathcal{M}$ y el comportamiento de la trayectoria DBN requeriría un análisis más detallado de la dinámica del flujo, que va más allá de lo disponible actualmente.

### 6.5. Convergencia del flujo DBN cuando $t \to \infty$

**Pregunta 6.8.** ¿Converge la trayectoria $f_t$ a algún punto de $\mathcal{M}$ cuando $t \to \infty$?

El comportamiento de $\Xi_t$ para $t \to \infty$ no es bien conocido en general. Se sabe que para $t > 0$ suficientemente grande, $\Xi_t$ tiene todos sus ceros reales (en el sentido de que para $t > 1/2$ todos los ceros son reales, por los resultados de De Bruijn y Newman). Pero la distribución de los ceros cuando $t \to \infty$ puede ser muy diferente de la de $\zeta_{\mathrm{on}}$.

**Observación 6.9.** Si $f_t \to f_\infty$ en $H_\lambda$ cuando $t \to \infty$, y si $f_\infty \in \mathcal{M}$, entonces $\inf_{g \in \mathcal{M}}\|f_0 - g\|_{H_\lambda} \leq \|f_0 - f_\infty\|_{H_\lambda}$. Pero $\|f_0 - f_\infty\|_{H_\lambda}$ puede ser estrictamente positivo si $f_\infty \neq f_0$.

**Conclusión 6.10.** La conexión entre el flujo DBN y el problema variacional es tentadora pero incompleta. El flujo proporciona una familia de puntos en $\mathcal{M}$ (para $t > \Lambda$) que son candidatos a minimizadores, pero no hay argumento riguroso que garantice que algún $f_t$ sea el minimizador de $\Phi|_\mathcal{M}$.

---

## §7. El obstáculo residual: formulación precisa

### 7.1. Diagrama del argumento

El argumento que se quisiera cerrar es el siguiente:

$$\neg\text{RH} \xRightarrow{(1)} \tilde\delta_\lambda^2 > 0 \xRightarrow{(2)} \exists g^* \in \mathcal{M},\, \|f_0 - g^*\| = \tilde\delta_\lambda^2 \xRightarrow{(3)} g^* = f_0^{on} \xRightarrow{(4)} \text{contradicción}.$$

Donde cada flecha corresponde a:

- **(1):** Criterio variacional del Doc 82. **DEMOSTRADO.**
- **(2):** Existencia del minimizador (ND1). **NO DEMOSTRADO.** Requiere ND3 o algún argumento alternativo.
- **(3):** Unicidad del minimizador (ND2). **NO DEMOSTRADO.** Requiere que el mínimo local $f_0^{on}$ sea también el mínimo global.
- **(4):** Derivar una contradicción de $g^* = f_0^{on}$ bajo $\neg$RH. **PARCIALMENTE DEMOSTRADO:** el Doc 93 muestra que $f_0^{on}$ es un mínimo local, no un mínimo estricto bajo $\neg$RH; las ecuaciones de Euler-Lagrange muestran que $f_0^{on}$ no satisface la condición de mínimo global.

**Observación 7.1 (La cadena lógica bajo $\neg$RH).** Nótese que, bajo $\neg$RH, la cadena completa lleva a una contradicción: si $\tilde\delta_\lambda^2 > 0$ es alcanzado por $g^* = f_0^{on}$, entonces por las ecuaciones de Euler-Lagrange $f_0^{on}$ no satisface la condición de mínimo, lo que contradice la hipótesis de que es el minimizador. Pero la cadena solo funciona si se demuestran (2) y (3).

### 7.2. El obstáculo principal: ND3 y la cerradura de $\mathcal{M}$

El análisis de §2 muestra que **ND3 es el obstáculo primario**. Si $\mathcal{M}$ no es cerrada, el argumento clásico de existencia del minimizador (proyección al cerrado) falla, y la existencia de un minimizador en $\mathcal{M}$ queda en duda.

**Obstáculo 7.2 (Formal).** Para atacar ND1 y ND2, se necesita primero resolver ND3. Las opciones son:

(A) Demostrar que $\mathcal{M}$ es cerrada (lo cual §2 sugiere que es falso en general).

(B) Demostrar que el infimum es alcanzado en $\mathcal{M}$ por algún argumento alternativo a la proyección en cerrado (por ejemplo, usando una estructura adicional del problema específico del espacio $\mathcal{E}$ de funciones enteras de orden 1).

(C) Abandonar la búsqueda del minimizador y atacar directamente el valor del infimum (demostrar que $\tilde\delta_\lambda^2 = 0 \iff$ RH por un argumento que no pase por el minimizador).

La opción (C) es la del Doc 82, que ya tiene demostración. La dificultad es que el Doc 82 usa un argumento de dualidad y no da información sobre la geometría del infimum.

### 7.3. El obstáculo secundario: ND2 y la unicidad

Incluso bajo la hipótesis condicional de que ND1 sea verdadera (existe el minimizador), el análisis de §4 y §5 muestra que la unicidad del minimizador (ND2) es una cuestión abierta.

**Obstáculo 7.3 (Unicidad).** Los argumentos disponibles (segunda variación local, ecuaciones de Euler-Lagrange, conectividad de $\mathcal{M}$) son insuficientes para establecer que $f_0^{on}$ es el único minimizador de $\Phi|_\mathcal{M}$. El gap entre mínimo local (Doc 93) y mínimo global (requerido) no se cierra con las herramientas actuales.

Para cerrar este gap se necesitaría uno de los siguientes ingredientes:

(i) Una demostración de que $\mathcal{M}$ es geodésicamente convexo en $H_\lambda$ (todo mínimo local es global).
(ii) Una desigualdad cuantitativa directa: $\|f_0 - g\|_{H_\lambda} \geq \|f_0 - f_0^{on}\|_{H_\lambda}$ para toda $g \in \mathcal{M}$.
(iii) Una demostración de que el sistema de ecuaciones de Euler-Lagrange (Proposición 4.4) tiene solución única en $\mathcal{E}$.

Ninguno de estos está disponible actualmente.

### 7.4. La barrera de Hadamard extendida (ND4) 

La condición ND4 tiene un carácter diferente de ND1–ND3: es una estimación cuantitativa que intenta conectar el valor del infimum con las posiciones de los ceros.

**Obstáculo 7.4 (Hadamard extendida).** Se necesita una estimación de la forma:
$$\tilde\delta_\lambda^2 \geq C \sum_{j: \sigma_j \neq 1/2} (\sigma_j - 1/2)^2,$$
donde la suma corre sobre los ceros off-critical de $\zeta$ y $C > 0$ es una constante que puede depender de $\lambda$ pero no de los ceros individuales. Esta estimación reforzaría el criterio variacional: si RH falla, el infimum está acotado abajo de manera cuantitativa en términos de las posiciones de los ceros.

El Doc 86 da una estimación de este tipo para $T_\lambda$ (la traza CTP), pero la relación precisa entre $T_\lambda$ y $\tilde\delta_\lambda^2$ no está establecida en general.

---

## §8. La Conjetura $\mathbf{C}_D$: formulación y discusión

### 8.1. Formulación de la conjetura

Habiendo identificado los obstáculos, formulamos la Conjetura $\mathbf{C}_D$ que, de ser verdadera, conectaría los resultados de los Docs 82, 83, 93 con RH.

**Conjetura $\mathbf{C}_D$.** Sean $\lambda > 0$ y las notaciones del marco CCM. Supóngase que:

(I) La funcional $\Phi(g) = \|f_0 - g\|^2_{H_\lambda}$ restringida a $\mathcal{M}$ tiene segunda variación positiva en toda dirección transversal en todo punto $g \in \mathcal{M}$ (no solo en $f_0^{on}$):
$$\frac{d^2}{d\epsilon^2}\Phi(g + \epsilon b)\bigg|_{\epsilon=0} > 0 \quad \forall g \in \mathcal{M},\, \forall b \perp T_g\mathcal{M}.$$

(II) La derivada temporal de $\tilde\delta_\lambda^2(t) = \|f_0 - f_t\|^2_{H_\lambda}$ a lo largo del flujo DBN satisface $\partial_t \tilde\delta_\lambda^2(t) \leq 0$ para todo $t > 0$.

Entonces $\tilde\delta_\lambda^2 = 0 \iff$ RH.

**Observación 8.1.** Nótese que la implicación $\tilde\delta_\lambda^2 = 0 \Rightarrow$ RH ya está establecida en el Doc 82. Lo que $\mathbf{C}_D$ afirma que las hipótesis (I) y (II) implican la dirección $\neg$RH $\Rightarrow \tilde\delta_\lambda^2 > 0$, que también está en el Doc 82. Por tanto, $\mathbf{C}_D$ bajo las hipótesis (I) y (II) no añade contenido nuevo al Doc 82.

**Reformulación honesta.** La Conjetura $\mathbf{C}_D$ tiene interés como afirmación sobre las hipótesis (I) y (II), no sobre la conclusión:

**Conjetura $\mathbf{C}_D$ (reformulada).** *Bajo las condiciones del marco CCM y asumiendo RH verdadera, las hipótesis (I) y (II) de $\mathbf{C}_D$ son verdaderas. Bajo $\neg$RH, al menos una de las hipótesis (I) y (II) es falsa.*

Esta formulación convierte $\mathbf{C}_D$ en una conjetura sobre las propiedades analíticas de $\mathcal{M}$ y del flujo DBN, cuya demostración sería interesante independientemente de RH.

### 8.2. ¿Es $\mathbf{C}_D$ más débil que RH, equivalente, o independiente?

Para analizar la relación lógica entre $\mathbf{C}_D$ y RH, consideramos las cuatro posibilidades lógicas:

**(a) $\mathbf{C}_D$ implica RH (y RH no implica $\mathbf{C}_D$):** $\mathbf{C}_D$ sería más fuerte que RH. Esto ocurriría si las hipótesis (I) y (II) de $\mathbf{C}_D$ fueran más fuertes que RH por sí solas.

**(b) RH implica $\mathbf{C}_D$ (y $\mathbf{C}_D$ no implica RH):** $\mathbf{C}_D$ sería más débil que RH. Esto ocurriría si (I) y (II) fueran consecuencias de RH pero no suficientes para probar RH.

**(c) RH y $\mathbf{C}_D$ son equivalentes:** las hipótesis (I) y (II) son verdaderas si y solo si RH es verdadera.

**(d) RH y $\mathbf{C}_D$ son independientes (en el sentido de que ninguna implica la otra).** Esto ocurriría si hubiera modelos (en sentido técnico) en los que RH es falsa pero (I) y (II) son verdaderas, o viceversa.

**Análisis de cada caso:**

Para el caso (a): las hipótesis (I) y (II) son afirmaciones sobre la geometría de $\mathcal{M}$ y sobre el flujo DBN. No es evidente que impliquen RH directamente: si (I) y (II) son verdaderas pero el infimum es positivo (bajo $\neg$RH), el criterio del Doc 82 daría $\neg$RH. Pero si la monotonía del flujo (II) y la curvatura positiva (I) implican que el infimum cero, eso daría RH. Este argumento necesita formalizarse.

Para el caso (b): bajo RH, $f_0 = f_0^{on} \in \mathcal{M}$ y $\Phi(f_0^{on}) = 0$ es el mínimo absoluto. La hipótesis (I) bajo RH diría que la segunda variación es positiva en todo punto de $\mathcal{M}$, lo cual sería una afirmación sobre la geometría de $\mathcal{M}$ independiente de la posición de $f_0$. La hipótesis (II) bajo RH diría que el flujo DBN es monótono en un sentido específico, lo cual es una afirmación sobre la dinámica de las funciones enteras bajo el calor de De Bruijn.

**Evaluación honesta.** No hay razón a priori para que RH implique (I) o (II), ni para que (I) y (II) impliquen RH. La Conjetura $\mathbf{C}_D$ es, en su estado actual, una afirmación plausible pero sin soporte demostrativo. Es posible que sea equivalente a RH, pero también es posible que sea independiente.

**Declaración explícita de honestidad 8.2.** La Conjetura $\mathbf{C}_D$ no es, en su estado actual, ni una demostración ni un esquema de demostración de RH. Es una guía para la investigación que señala dos propiedades analíticas concretas ((I) y (II)) cuya verdad o falsedad bajo $\neg$RH sería informativa sobre la geometría del problema variacional.

### 8.3. Una versión más manejable de $\mathbf{C}_D$

Para hacer la conjetura más concreta y potencialmente atacable, proponemos la siguiente versión reducida:

**Conjetura $\mathbf{C}_D^{\mathrm{red}}$ (versión reducida).** *Sea $\lambda > 0$ suficientemente grande. Si la segunda variación de $\Phi$ en el punto $f_0^{on}$ es positiva en toda dirección transversal $b_j$ (resultado del Doc 93), y si la distancia $D(t) = \|f_0 - f_t\|_{H_\lambda}$ satisface $D(t) \geq \tilde\delta_\lambda > 0$ para todo $t \in [0, 1/2]$ (con el flujo DBN entre $t=0$ y $t=1/2$), entonces $\tilde\delta_\lambda^2 > 0$ bajo $\neg$RH.*

Esta versión es más débil porque no requiere la segunda variación global (solo en $f_0^{on}$) y la monotonía del flujo es reemplazada por una cota inferior para la distancia en un intervalo compacto de $t$.

### 8.4. Lo que se ha ganado y lo que falta

**Lo que se ha ganado:**

1. **Caracterización precisa del gap.** Las condiciones ND1–ND4 están formuladas con precisión y sus relaciones lógicas son claras.

2. **Análisis de ND3.** Se ha mostrado que $\mathcal{M}$ probablemente no es cerrada y se ha caracterizado tentativamente la clausura $\overline{\mathcal{M}}$.

3. **Ecuaciones de Euler-Lagrange.** Se ha derivado el sistema de ecuaciones del minimizador hipotético y se ha mostrado que $f_0^{on}$ no satisface este sistema bajo $\neg$RH.

4. **Conectividad de $\mathcal{M}$.** Se ha mostrado que $\mathcal{M}$ es conexo por caminos, aunque esto no da información directa sobre la unicidad del mínimo.

5. **Conexión con el flujo DBN.** Se ha establecido la derivada temporal de la distancia a $f_0$ a lo largo del flujo y se ha identificado el mecanismo heurístico por el que la curvatura positiva podría implicar monotonía.

**Lo que falta:**

1. **Demostración o refutación de ND3.** La pregunta de si $\mathcal{M}$ es cerrada permanece abierta.

2. **Existencia del minimizador (ND1).** Sin ND3, la existencia del minimizador queda sin soporte.

3. **Unicidad del minimizador (ND2).** Incluso bajo la hipótesis de que el minimizador existe, su unicidad no está establecida.

4. **Demostración de $\mathbf{C}_D$ o $\mathbf{C}_D^{\mathrm{red}}$.** La conjetura $\mathbf{C}_D$ en cualquiera de sus versiones está sin demostrar.

---

## §9. Perspectivas y direcciones futuras

### 9.1. Atacar ND3 por métodos de teoría de funciones

El análisis de §2 sugiere que el obstáculo para ND3 es el "escape de ceros a infinito". Una dirección para atacar este problema es usar teoría de funciones enteras para controlar las sucesiones minimizantes:

**Dirección A.** Demostrar (o refutar) que toda sucesión minimizante $(g_n) \subset \mathcal{M}$ con $\Phi(g_n) \to \tilde\delta_\lambda^2$ tiene ceros que permanecen en una región compacta del plano complejo (es decir, que los ceros no "escapan a infinito" a lo largo de la sucesión minimizante).

Si esto se demuestra, el Teorema de Montel aplicaría y se obtendría compacidad de la sucesión minimizante, dando ND3 (al menos para sucesiones minimizantes).

### 9.2. Atacar ND2 por argumentos de convexidad global

**Dirección B.** Estudiar si $\mathcal{M}$ admite una estructura de "variedad con curvatura negativa" en el sentido geodésico, lo que implicaría que todo mínimo local es global. Este tipo de argumento se usa en geometría de espacios simétricos y en teoría de espacios $\mathrm{CAT}(0)$.

La conexión con el problema de Riemann es la siguiente: si $\mathcal{M}$ fuera un espacio $\mathrm{CAT}(0)$, entonces $\Phi|_\mathcal{M}$ tendría un único mínimo local (que sería el mínimo global). Pero establecer que $\mathcal{M}$ es $\mathrm{CAT}(0)$ requeriría calcular la curvatura de $\mathcal{M}$ en todos los puntos, no solo en $f_0^{on}$.

### 9.3. Una estimación directa de Lelong-Poincaré

**Dirección C.** La fórmula de Lelong-Poincaré relaciona el logaritmo de una función entera con la medida de sus ceros (la "medida de Lelong"). Para funciones en $\mathcal{E}$:
$$\log|\eta(z)| = \mathrm{Re}(Az + B) + \int_{\mathbb{C}} \log|z - w|\,d\mu_\eta(w),$$
donde $\mu_\eta$ es la medida de ceros de $\eta$ (soportada en $\mathrm{Re}(w) = 1/2$ para $\eta \in \mathcal{E}$).

Si se puede expresar $\Phi(\eta) = \|f_0 - |\eta|^2\|^2_{H_\lambda}$ en términos de la medida de Lelong $\mu_\eta$, quizás sea posible reformular el problema variacional como un problema de optimización sobre medidas (potencial logarítmico), para el que la teoría de potencial logarítmico proporciona herramientas bien desarrolladas.

**Dirección D.** Conectar el problema con la teoría de espacios de Hardy sobre la línea crítica. Las funciones $\eta \in \mathcal{E}$ definen, al restringirse a la línea crítica $\mathrm{Re}(s) = 1/2$, elementos del espacio de Hardy $H^2(\mathrm{Re}(s) > 1/2)$. La optimización de $\|f_0 - |\eta|^2\|_{H_\lambda}$ podría reformularse en términos de problemas de aproximación en $H^2$, para los que existen teoremas de existencia y unicidad (bajo condiciones convexidad o de tipo Adamyan-Arov-Krein).

### 9.4. Síntesis final

La Dirección D del programa es promisoria porque conecta de manera directa la geometría analítica de $\mathcal{M}$ con la aritmética de los ceros de $\zeta$. Pero el análisis de este documento muestra que los obstáculos son genuinos y profundos: la no-cerradura de $\mathcal{M}$, la posible no-unicidad del minimizador, y la falta de una conexión rigurosa entre el flujo DBN y el problema variacional son problemas abiertos que requieren herramientas analíticas más sofisticadas de las disponibles actualmente.

El resultado positivo es la **precisión del diagnóstico**: ahora sabemos con exactitud qué falta. El paso siguiente más productivo parece ser atacar ND3 con métodos de teoría de funciones enteras, buscando condiciones bajo las cuales las sucesiones minimizantes compacten.

---

## Apéndice A: Conexión con los Docs anteriores de la Fase 34

### A.1. Relación con el Doc 93

El presente documento es una continuación directa del Doc 93. Mientras el Doc 93 demostró la segunda variación positiva (un resultado local), el Doc 95 analiza las condiciones necesarias para convertir ese resultado local en global. Las condiciones ND1–ND4 formuladas en el Doc 93 §8 son el punto de partida del análisis de los §§2–7 de este documento.

### A.2. Relación con el Doc 82

El criterio variacional del Doc 82 ($\tilde\delta_\lambda^2 = 0 \iff$ RH) es el marco fundamental. El análisis de este documento no modifica ni mejora ese resultado: lo que se estudia es la estructura geométrica adicional que permitiría entender mejor el comportamiento del infimum, especialmente bajo $\neg$RH.

### A.3. Relación con el Doc 83

La desigualdad puntual $f_0 \geq f_0^{on}$ del Doc 83 es crucial en el análisis de la segunda variación (Proposición 4.3 del Doc 93) y también para estudiar las ecuaciones de Euler-Lagrange (§4 de este documento). La fórmula del Doc 83 para el cociente $f_0/f_0^{on}$ es la que determina el signo de $D_0 = f_0 - f_0^{on}$.

### A.4. Relación con los Docs 70–72 (Fase 33, DBN-CCM)

El Doc 72 expresó $T_\lambda$ en términos de la fórmula de Weil. La conexión entre $T_\lambda$ y $\tilde\delta_\lambda^2$ apuntada en el Doc 93 §5 (el kernel $K_\lambda(\gamma_j)$ del Doc 86 es esencialmente el coeficiente de segunda variación $\mathcal{Q}_\lambda^{(j)}$) sugiere que los Docs 70–72 contienen información relevante para el problema variacional. En particular, la monotonía de $T_\lambda(t)$ a lo largo del flujo DBN (Doc 70) podría estar relacionada con la monotonía de $D(t)$ estudiada en §6.4, aunque la conexión precisa no está establecida.

---

## Apéndice B: Glosario de condiciones y conjeturas

Para referencia futura, enumeramos las condiciones y conjeturas del programa Dirección D:

- **ND1 (Existencia):** El infimum $\tilde\delta_\lambda^2$ es alcanzado en $\mathcal{M}$. Estado: **abierto**, probablemente requiere ND3.
- **ND2 (Unicidad):** El minimizador es único e igual a $f_0^{on}$. Estado: **abierto**, no se sigue de la segunda variación local.
- **ND3 (Cerradura):** $\mathcal{M}$ es cerrada en $H_\lambda$. Estado: **probablemente falsa**, la clausura contiene funciones con ceros que escaparon a infinito.
- **ND4 (Hadamard extendida):** Estimación cuantitativa de $\tilde\delta_\lambda^2$ en términos de las posiciones de los ceros. Estado: **abierto**, parcialmente disponible para $T_\lambda$ (Doc 86).
- **Conjetura $\mathbf{C}_D$:** Segunda variación positiva global + flujo DBN monótono $\Rightarrow$ $\tilde\delta_\lambda^2 = 0 \iff$ RH. Estado: **conjetura**, relación con RH no establecida.
- **Conjetura $\mathbf{C}_D^{\mathrm{red}}$:** Versión reducida, con segunda variación local en $f_0^{on}$ y cota inferior de $D(t)$ en $[0,1/2]$. Estado: **conjetura más débil**, más accesible.

---

*Fin del Doc 95.*
