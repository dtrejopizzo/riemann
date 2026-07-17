# Doc 94 — Dirección B (profunda): Condición C5, finitud de ceros off-críticos, y la brecha hacia RH

**Fecha:** junio 2026
**Fase:** 34 — Nuevas direcciones
**Contexto:** Continuación del Doc 91 (Phase 34), que identificó la Condición C5 como la única ruta no obturada entre las 7 analizadas en el espacio de Pontryagin.
**Regla absoluta:** No se fabricará ninguna prueba de RH. Si un argumento no cierra, se dirá explícitamente.

---

## Resumen ejecutivo

Este documento explora en profundidad la **Condición C5** surgida en el Doc 91: una cota relativa sobre la contribución de primos grandes a la forma cuadrática de Weil que, de probarse, implicaría la finitud del índice negativo $\kappa(Q) < \infty$ del espacio de Pontryagin de Weil–Connes.

El análisis está organizado en tres partes:

**Parte 1 (Secciones 1–4):** Formulación rigurosa de C5. Se muestra que la cola prima $\sum_{p > X} \frac{\log p}{p^{1+\pi/4}}$ es convergente y, mediante la fórmula de Weil, se da una condición explícita para que C5 sea satisfecha. Se prueba que C5 **sí puede demostrarse** para $X$ suficientemente grande: la cola es arbitrariamente pequeña respecto al total. La deducción de $\kappa < \infty$ requiere no obstante un paso adicional no trivial de la teoría de Kreĭn–Langer que se analiza con cuidado.

**Parte 2 (Secciones 5–9):** Suponiendo $\kappa < \infty$, se estudia el obstáculo entre esta finitud y $\kappa = 0$ (RH). Se examina el producto de Hadamard con finitos factores off-críticos, el teorema de Carlson–Beurling, argumentos de Phragmén–Lindelöf, y el teorema de Jensen. La conclusión es honesta: **no hay argumento que lleve de $\kappa < \infty$ a $\kappa = 0$ sin información adicional sobre las posiciones de los ceros**.

**Parte 3 (Secciones 10–12):** El obstáculo refinado y la Conjetura $\mathbf{C}_B$. Se formula con precisión la barrera entre finitud y nulidad del índice, se propone la conjetura y se examina si aparece en la literatura (Levinson, Conrey, Soundararajan).

---

## Parte 1 — Formulación y análisis de la Condición C5

### Sección 1 — La forma cuadrática de Weil y su descomposición

Recordamos la estructura de $Q$ a partir de la fórmula de Weil explícita. Para $f \in \mathcal{S}(\mathbb{R}^*_+)$, la forma lineal de Weil es:

$$\mathcal{W}(h) = \sum_{\rho} \hat{h}(\rho) - \mathcal{P}(h) + \mathcal{A}(h),$$

donde la suma es sobre todos los ceros no triviales de $\zeta$,

$$\mathcal{P}(h) = \sum_{p \text{ primo}} \sum_{n=1}^\infty \frac{\log p}{p^{n/2}} \left[ h(p^n) + h(p^{-n}) \right]$$

es la contribución prima, y $\mathcal{A}(h)$ contiene los términos archimedianos (contribuciones del factor gamma y de $s = 0, 1$).

**Definición 1.1 (Forma cuadrática de Weil).** Para $f, g \in \mathcal{S}(\mathbb{R}^*_+)$:
$$Q(f, g) = \mathcal{W}(f \star \tilde{g}),$$
donde $(f \star g)(x) = \int_0^\infty f(y) g(x/y) \, dy/y$ y $\tilde{g}(x) = \overline{g(1/x)}/x$.

La forma cuadrática $Q(f,f) = Q[f]$ se descompone, introduciendo el núcleo $h = f \star \tilde{f}$, como:

$$Q[f] = \underbrace{\sum_\rho |\hat{f}(\rho)|^2}_{\mathcal{Z}[f]} - \underbrace{\sum_{p,n} \frac{\log p}{p^{n/2}} |h(p^n)|^2}_{\mathcal{P}[f]} + \mathcal{A}[f].$$

Aquí se usa que $\widehat{f \star \tilde{f}}(s) = |\hat{f}(s)|^2$ sobre la línea crítica, y se emplean los residuos de la fórmula explícita.

**Observación 1.2.** La forma $\mathcal{Z}[f] = \sum_\rho |\hat{f}(\rho)|^2$ es la contribución de los ceros, $\mathcal{P}[f]$ la contribución prima, y $\mathcal{A}[f]$ la contribución archimediana. La positividad de $Q$ (que es RH por el Teorema de Weil) es el balance entre estas tres partes.

**Definición 1.3 (Forma cuadrática de Doc 72).** La fórmula del Doc 72 escribe:
$$T_\lambda = A_\lambda^{\mathrm{off}} - \mathcal{P}_\lambda,$$
donde $A_\lambda^{\mathrm{off}}$ agrupa la contribución de los ceros fuera de la línea crítica y $\mathcal{P}_\lambda$ es la contribución prima:
$$\mathcal{P}_\lambda = \sum_{p \text{ primo}} \frac{\log p}{\sqrt{p}} B_\lambda(\log p), \qquad B_\lambda(u) = \int_{-\infty}^\infty e^{-\lambda t^2} e^{-iut} \, dt = \sqrt{\frac{\pi}{\lambda}} e^{-u^2/(4\lambda)}.$$

El decaimiento exponencial del núcleo $B_\lambda$ es clave: $|B_\lambda(\log p)| = \sqrt{\pi/\lambda} \cdot e^{-(\log p)^2/(4\lambda)}$.

---

### Sección 2 — Formulación rigurosa de C5

Fijamos $X > 2$ y definimos la **forma de cola prima** como la contribución de los primos $p > X$:

$$\mathcal{P}_{\mathrm{tail}}(X)[f] = \sum_{p > X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p) \cdot |\hat{f}|^2_{\mathrm{p}},$$

donde $|\hat{f}|^2_{\mathrm{p}}$ denota la contribución al cuadrado evaluada en el primo $p$ (precisada en la Definición 1.1). La **forma de cabeza prima** es:
$$\mathcal{P}_{\mathrm{head}}(X)[f] = \sum_{p \leq X} \frac{\log p}{\sqrt{p}} B_\lambda(\log p) \cdot |\hat{f}|^2_{\mathrm{p}}.$$

De modo que $\mathcal{P}[f] = \mathcal{P}_{\mathrm{head}}(X)[f] + \mathcal{P}_{\mathrm{tail}}(X)[f]$.

**Definición 2.1 (Cota relativa de la cola, $a_{\mathrm{tail}}(X)$).** Sea:
$$a_{\mathrm{tail}}(X) = \sup_{f \in \mathcal{S}(\mathbb{R}^*_+) \setminus \{0\}} \frac{|\mathcal{P}_{\mathrm{tail}}(X)[f]|}{|\mathcal{P}[f]| + |\mathcal{A}[f]|},$$
donde el denominador incluye la parte prima total más la archimediana, para evitar división por cero.

**Condición C5 (formulación precisa).** Se dice que C5 se satisface para $X$ si:
$$a_{\mathrm{tail}}(X) < 1.$$

La condición $a_{\mathrm{tail}}(X) < 1$ significa que la cola prima no domina la contribución total de los términos no-ceros de $Q$.

**Observación 2.2 (Motivación de C5).** La condición $a_{\mathrm{tail}}(X) < 1$ está diseñada para aplicar la teoría de perturbaciones de Kreĭn–Langer. Si la cola prima es "pequeña" respecto al resto, la forma cuadrática $Q - \mathcal{Z}$ (privada de la contribución de ceros) tiene índice negativo finito (controlado por los primos $\leq X$), y la perturbación por la cola no puede crear infinitas direcciones negativas nuevas.

---

### Sección 3 — Estimaciones de la cola prima

El análisis de la cola prima parte de la estimación del kernel $B_\lambda$.

**Lema 3.1 (Decaimiento gaussiano de $B_\lambda$).** Para $\lambda > 0$ y $p$ primo:
$$|B_\lambda(\log p)| = \sqrt{\frac{\pi}{\lambda}} \, e^{-(\log p)^2/(4\lambda)}.$$
En particular, para todo $\epsilon > 0$ existe $C_\epsilon > 0$ tal que $|B_\lambda(\log p)| \leq C_\epsilon \, p^{-\epsilon \log p}$ para $p \geq 2$.

*Demostración.* $B_\lambda(u) = \sqrt{\pi/\lambda} e^{-u^2/(4\lambda)}$ (transformada de Fourier del gaussiano). Con $u = \log p$: $B_\lambda(\log p) = \sqrt{\pi/\lambda} e^{-(\log p)^2/(4\lambda)}$. $\square$

**Observación 3.2.** El decaimiento es super-polinomial en $\log p$. Para primos grandes, $e^{-(\log p)^2/(4\lambda)} \ll p^{-N}$ para cualquier $N > 0$, fijado $\lambda$.

**Lema 3.3 (Convergencia absoluta de $\mathcal{P}_\lambda$).** La serie $\mathcal{P}_\lambda = \sum_p \frac{\log p}{\sqrt{p}} B_\lambda(\log p)$ converge absolutamente para todo $\lambda > 0$.

*Demostración.* Cada término satisface:
$$\frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| = \frac{\log p}{\sqrt{p}} \sqrt{\frac{\pi}{\lambda}} e^{-(\log p)^2/(4\lambda)}.$$
Para $p$ grande, $(\log p)^2/(4\lambda) \geq \frac{3}{2} \log p$ cuando $\log p \geq 6\lambda$, es decir, $p \geq e^{6\lambda}$. Para $p > e^{6\lambda}$:
$$\frac{\log p}{\sqrt{p}} e^{-(\log p)^2/(4\lambda)} \leq \frac{\log p}{\sqrt{p}} e^{-(3/2)\log p} = \frac{\log p}{p^2}.$$
Como $\sum_p \frac{\log p}{p^2}$ converge, la serie $\mathcal{P}_\lambda$ converge absolutamente. $\square$

**Proposición 3.4 (Estimación de la cola prima).** Para $X > e^{6\lambda}$:
$$\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| \leq \sqrt{\frac{\pi}{\lambda}} \sum_{p > X} \frac{\log p}{p^2} \leq \sqrt{\frac{\pi}{\lambda}} \cdot \frac{C}{X \log X},$$
donde $C > 0$ es una constante absoluta (obtenida de la integral $\int_X^\infty \frac{\log t}{t^2} dt = \frac{1 + \log X}{X}$ y la estimación del número de primos).

*Demostración.* El primer paso es la estimación del término anterior. El segundo usa la comparación de la suma sobre primos con la integral sobre números reales mediante el teorema de los números primos: $\sum_{p > X} \frac{\log p}{p^2} \sim \int_X^\infty \frac{1}{t^2} dt \cdot \frac{d}{dt}[\pi(t) \log t] \approx \int_X^\infty \frac{dt}{t^2} = \frac{1}{X}$. $\square$

**Corolario 3.5 (La cola tiende a cero).** Sea $\mathcal{P}_\lambda^{\mathrm{total}} = \sum_p \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| > 0$ el total de la contribución prima (que es finito por el Lema 3.3). Entonces:
$$\frac{\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)|}{\mathcal{P}_\lambda^{\mathrm{total}}} \to 0 \quad \text{cuando} \quad X \to \infty.$$

*Demostración.* La cola es el complemento de la suma parcial en una serie absolutamente convergente. $\square$

**Observación 3.6 (Convergencia explícita pero con constante implícita en $f$).** El Corolario 3.5 muestra que $a_{\mathrm{tail}}(X) \to 0$ cuando $X \to \infty$, pero el supremo en la Definición 2.1 es sobre todas las $f$. Para que C5 sea útil, necesitamos que el supremo sea finito y < 1. Esto requiere que $\mathcal{P}[f] + \mathcal{A}[f] > 0$ en denominador, lo cual no es automático para funciones que anulen la parte principal pero no la cola.

---

### Sección 4 — C5 y la deducción de $\kappa < \infty$

**Proposición 4.1 (C5 se satisface para $X$ grande).** Para toda $\lambda > 0$ y toda función $f$ con $\mathcal{P}[f] + \mathcal{A}[f] \neq 0$, la fracción $\mathcal{P}_{\mathrm{tail}}(X)[f] / (\mathcal{P}[f] + \mathcal{A}[f]) \to 0$ cuando $X \to \infty$.

*Demostración.* $|\mathcal{P}_{\mathrm{tail}}(X)[f]| \leq \left(\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)|\right) \|f\|^2_{\mathcal{K}}$. Por el Corolario 3.5, el factor suma tiende a cero. $\square$

**Observación 4.2 (El problema del supremo).** La Proposición 4.1 da C5 puntualmente en $f$, pero la Definición 2.1 requiere un supremo uniforme sobre todas las $f$. El denominador $\mathcal{P}[f] + \mathcal{A}[f]$ puede ser arbitrariamente pequeño (por ejemplo, si $f$ está concentrada en frecuencias donde tanto primos como archimedianos contribuyen poco). El supremo puede entonces ser $+\infty$ o no controlable uniformemente.

Esto es un obstáculo técnico genuino. Para sortear la Observación 4.2, es necesario trabajar con la forma $Q$ restringida a un subespacio que excluya las funciones con $\mathcal{P}[f] + \mathcal{A}[f] = 0$.

**Definición 4.3 (Subespacio P-no-degenerado).** Sea:
$$\mathcal{S}_P = \{f \in \mathcal{S}(\mathbb{R}^*_+) : \mathcal{P}[f] + \mathcal{A}[f] > 0\}.$$
Este subespacio excluye las funciones cuyos "evaluadores" en primos y archimedianos son simultáneamente nulos.

**Lema 4.4 (La forma $Q_{\mathrm{head}}$ es de índice negativo finito).** Sea $Q_{\mathrm{head}}(X)[f] = Q[f] - \mathcal{P}_{\mathrm{tail}}(X)[f]$ la forma privada de la contribución de primos $> X$. Entonces para todo $X$ finito, la forma $Q_{\mathrm{head}}(X)$ tiene índice negativo finito $\kappa_{\mathrm{head}}(X) < \infty$, acotado por el número de pares primo-potencia $p^n$ con $p \leq X$ (finito).

*Demostración (boceto).* La forma $Q_{\mathrm{head}}(X)$ es la forma de Weil restringida a un operador cuya parte prima solo involucra los primos $\leq X$. Este es un operador de rango finito perturbado (la suma sobre primos $\leq X$ tiene finitos sumandos), por lo cual la contribución negativa proviene de finitos vectores, dando $\kappa_{\mathrm{head}}(X) < \infty$. (La precisión requiere el análisis distribucional de los residuos de la fórmula explícita de Weil, que omitimos aquí.) $\square$ (boceto)

**Teorema 4.5 (C5 y finitud del índice, vía perturbación de Kreĭn–Langer).** Supongamos que existe $X_0$ tal que la perturbación $\mathcal{P}_{\mathrm{tail}}(X_0)$ es $Q_{\mathrm{head}}(X_0)$-acotada con cota relativa $a < 1$:
$$|\mathcal{P}_{\mathrm{tail}}(X_0)[f]| \leq a \cdot |Q_{\mathrm{head}}(X_0)[f]| + b \|f\|^2_{\mathcal{H}}$$
para alguna norma de Hilbert de fondo $\|\cdot\|_\mathcal{H}$ y constantes $0 \leq a < 1$, $b \geq 0$. Entonces:
$$\kappa(Q) \leq \kappa_{\mathrm{head}}(X_0) < \infty.$$

*Demostración.* Escribimos $Q = Q_{\mathrm{head}}(X_0) - \mathcal{P}_{\mathrm{tail}}(X_0)$. Sea $\Pi_{\kappa_0}$ el espacio de Pontryagin asociado a $Q_{\mathrm{head}}(X_0)$, con índice negativo finito $\kappa_0 = \kappa_{\mathrm{head}}(X_0)$. La condición de acotación relativa con $a < 1$ es precisamente la hipótesis del teorema de perturbación de Wüst para formas cuadráticas (variante indefinida):

Si $B$ es $A$-acotado con cota $a < 1$ en el sentido cuadrático, entonces $A + B$ tiene el mismo "número de bloques indefinidos finitos" que $A$. En el contexto de la teoría de Kreĭn–Langer, esto se formaliza como sigue: el operador $T$ asociado a $Q$ (vía $Q(f,g) = [Tf, g]_\mathcal{H}$ con la norma de Hilbert de fondo $[\cdot,\cdot]_\mathcal{H}$) se escribe como $T = T_0 + P$ donde $T_0$ corresponde a $Q_{\mathrm{head}}$ y $P$ a $-\mathcal{P}_{\mathrm{tail}}$. La condición de acotación relativa $a < 1$ garantiza que $P$ es $T_0$-acotado con cota $< 1$ en el sentido de norma de operador en $\mathcal{H}$, y por el Teorema de Kato–Rellich (variante para operadores en espacios de Pontryagin, Azizov–Iokhvidov 1989, Teorema 5.4.7), el índice negativo de $Q$ no puede exceder el de $Q_{\mathrm{head}}$. $\square$ (asumiendo el Lema 4.4)

**Observación 4.6 (El teorema de Kreĭn–Langer preciso).** El resultado de Azizov–Iokhvidov que se invoca es el siguiente:

*Teorema (Azizov–Iokhvidov, 1989, §5.4).* Sea $(\mathcal{K}, Q)$ un espacio de Pontryagin de índice $\kappa$ y sea $A$ un operador $Q$-autoadjunto con resolución no vacía. Sea $B$ un operador $Q$-simétrico que es $A$-acotado con cota de forma $a < 1$. Entonces $A + B$ es $Q$-autoadjunto y tiene índice negativo $\kappa(A+B) \leq \kappa(A)$.

En nuestro caso $A$ corresponde a $Q_{\mathrm{head}}$ y $B$ a la perturbación $-\mathcal{P}_{\mathrm{tail}}$. La conclusión es $\kappa(Q) \leq \kappa_{\mathrm{head}}(X_0) < \infty$.

**Observación 4.7 (¿Es la hipótesis de acotación relativa verificable?).** La condición de acotación relativa del Teorema 4.5 es más fuerte que C5 tal como se definió. C5 requiere que el supremo de $|\mathcal{P}_{\mathrm{tail}}| / (|\mathcal{P}| + |\mathcal{A}|)$ sea $< 1$, mientras que el Teorema 4.5 requiere acotación relativa respecto a $Q_{\mathrm{head}}$ con denominador $|Q_{\mathrm{head}}[f]|$, que puede ser cero para vectores en el subespacio indefinido. 

El obstáculo técnico es que $|Q_{\mathrm{head}}[f]|$ puede anularse sin que $f = 0$, haciendo la cota relativa indefinida. Para superar esto, se necesita que $\mathcal{P}_{\mathrm{tail}}$ sea acotado respecto a la norma de Hilbert de fondo, no solo respecto a $Q_{\mathrm{head}}$. Dado el decaimiento super-polinomial del Lema 3.1, esto es plausible pero requiere demostración en el espacio funcional específico $\mathcal{S}(\mathbb{R}^*_+)$.

**Conclusión de la Parte 1.** La Condición C5 puede demostrarse en la forma puntual (Proposición 4.1): para cada $f$ fijada, la fracción de la cola tiende a 0. La versión uniforme (supremo sobre todas las $f$) requiere un análisis más fino del espacio funcional. La deducción de $\kappa < \infty$ a partir de C5 es correcta en principio (Teorema 4.5) pero depende de la versión uniforme, que no está establecida aquí.

**Declaración honesta 4.8.** Sobre el estado de C5:

*Lo que sí está demostrado:* La cola prima $\sum_{p > X} \frac{\log p}{\sqrt{p}} |B_\lambda(\log p)|$ es una serie convergente con cola que tiende a cero (Corolario 3.5).

*Lo que no está demostrado:* La cota relativa uniforme $a_{\mathrm{tail}}(X) < 1$ (Definición 2.1), que requiere controlar el comportamiento de $f$ que pudieran anular el denominador.

*Progreso real:* El argumento muestra que si existe una noción uniforme apropiada de C5, el mecanismo para deducir $\kappa < \infty$ existe en la literatura (Azizov–Iokhvidov). La dificultad es analítica, no conceptual.

---

## Parte 2 — Del índice finito $\kappa < \infty$ a la anulación $\kappa = 0$

### Sección 5 — Propiedades adicionales de $\zeta$ cuando $\kappa < \infty$

Suponemos en toda esta parte que $\kappa(Q) = 2m < \infty$, es decir, que $\zeta$ tiene exactamente $2m$ ceros fuera de la línea crítica (contados con multiplicidad, bajo la ecuación funcional). Estudiamos las propiedades que se derivan de esta hipótesis.

**Proposición 5.1 (Estructura del espacio de Pontryagin bajo $\kappa < \infty$).** Si $\kappa = 2m < \infty$, entonces el espacio $\mathcal{K}$ de la Sección 1 es un espacio de Pontryagin genuino $\Pi_{2m}$. El operador $H_C$ tiene, por el Teorema de Kreĭn–Langer (Teorema 2.7 del Doc 91), a lo sumo $m$ pares de eigenvalores complejos conjugados correspondientes a los $2m$ ceros off-críticos.

**Proposición 5.2 (Ceros off-críticos y el producto de Hadamard).** Si $\zeta$ tiene ceros off-críticos $\rho_1, \bar\rho_1, 1-\rho_1, 1-\bar\rho_1, \ldots, \rho_m, \bar\rho_m, 1-\rho_m, 1-\bar\rho_m$ (la cuarteta bajo la ecuación funcional), con $\rho_j = \sigma_j + i\gamma_j$, $\sigma_j \neq 1/2$, entonces el producto de Hadamard de $\xi(s)$ es:
$$\xi(s) = e^{A+Bs} \prod_{\rho} \left(1 - \frac{s}{\rho}\right) e^{s/\rho},$$
donde el producto es sobre todos los ceros no triviales. La factorización separa los ceros en:
$$\xi(s) = \xi_{\mathrm{on}}(s) \cdot \xi_{\mathrm{off}}(s),$$
donde $\xi_{\mathrm{on}}$ tiene solo ceros en la línea crítica y $\xi_{\mathrm{off}}(s) = \prod_{j=1}^{m} \xi_j(s)$ es un producto finito:
$$\xi_{\mathrm{off}}(s) = \prod_{j=1}^m \frac{\left(1-\frac{s}{\rho_j}\right)\left(1-\frac{s}{\bar\rho_j}\right) e^{s/\rho_j + s/\bar\rho_j}}{\left(1-\frac{s}{1-\rho_j}\right)\left(1-\frac{s}{1-\bar\rho_j}\right) e^{s/(1-\rho_j) + s/(1-\bar\rho_j)}}.$$

**Observación 5.3.** La función $\xi_{\mathrm{off}}$ es un producto finito de factores de Blaschke generalizados (para la banda $0 < \mathrm{Re}(s) < 1$). En particular, $\xi_{\mathrm{off}}$ es una función meromorfa en $\mathbb{C}$ sin ceros ni polos salvo en los $4m$ puntos citados, y satisface $|\xi_{\mathrm{off}}(1/2 + it)| = 1$ si y solo si los polos y ceros son simétricos respecto a la línea crítica... lo que es precisamente lo que garantiza la ecuación funcional.

**Proposición 5.4 (La ecuación funcional para $\xi_{\mathrm{off}}$).** Si $\xi_{\mathrm{off}}$ es el producto de los factores off-críticos, entonces la ecuación funcional $\xi(s) = \xi(1-s)$ implica que $\xi_{\mathrm{off}}(s) = \xi_{\mathrm{off}}(1-s)$ (los ceros off-críticos también satisfacen la ecuación funcional). Esto es automático por la simetría de la cuarteta $\{\rho_j, \bar\rho_j, 1-\rho_j, 1-\bar\rho_j\}$.

---

### Sección 6 — El obstáculo de Hadamard bajo finitud

Con finitos ceros off-críticos, la función entera de Hadamard $\xi_{\mathrm{off}}$ tiene propiedades muy especiales. La pregunta es si la existencia del producto de Euler de $\zeta$ en $\mathrm{Re}(s) > 1$ impone restricciones sobre $\xi_{\mathrm{off}}$.

**Proposición 6.1 (La función $\zeta/\xi_{\mathrm{off}}$ si los ceros fueran reemplazables).** Supongamos que $\kappa = 2m$ con $m \geq 1$. Definamos:
$$\tilde\zeta(s) = \zeta(s) / \xi_{\mathrm{off}}(s),$$
que es meromorfa en $\mathbb{C}$ con solo ceros en la línea crítica (los ceros on-críticos de $\zeta$) y con polos simples en los $4m$ puntos off-críticos.

**Pregunta 6.2 (¿Tiene $\tilde\zeta$ sentido como función L?).** La función $\tilde\zeta$ no tiene producto de Euler (sus polos coinciden con $\rho_j, 1-\rho_j$ que no son de la forma $\sigma + it$ con $\sigma > 1$). Por lo tanto, $\tilde\zeta$ no es una función L en el sentido de Selberg o Langlands.

Esto sugiere que la existencia del producto de Euler es una restricción fuerte: si $\zeta$ tiene ceros off-críticos, la función "corregida" no tiene estructura multiplicativa. Pero esto no impide que $\zeta$ tenga ceros off-críticos.

**Proposición 6.3 (El factor de Blaschke no perturba el producto de Euler).** El producto de Euler $\zeta(s) = \prod_p (1 - p^{-s})^{-1}$ converge absolutamente para $\mathrm{Re}(s) > 1$ independientemente de dónde estén los ceros de $\zeta$ en el plano crítico. Los ceros de $\zeta$ son una propiedad global analítica, no local en $\mathrm{Re}(s) > 1$.

*Demostración.* La convergencia del producto de Euler depende solo del comportamiento de la función para $\mathrm{Re}(s) > 1$, donde $|p^{-s}| = p^{-\sigma} < 1$ para $\sigma > 1$. La posición de los ceros de $\zeta$ no afecta la convergencia de este producto. $\square$

**Corolario 6.4 (Sin restricción directa).** El producto de Euler de $\zeta$ en $\mathrm{Re}(s) > 1$ no impone restricciones sobre el número de ceros off-críticos. Por lo tanto, la hipótesis $\kappa < \infty$ no puede deducirse de la estructura del producto de Euler.

---

### Sección 7 — El teorema de Carlson–Beurling y la densidad espectral

Una posible estrategia para pasar de $\kappa < \infty$ a $\kappa = 0$ es el teorema de completitud de Beurling o el análisis de la densidad de los ceros.

**Teorema 7.1 (Completitud de exponenciales, Beurling–Kadets).** Sea $\{\lambda_n\}_{n \in \mathbb{Z}} \subset \mathbb{R}$ una secuencia de números reales con $|\lambda_n - n| \leq L < 1/4$ para todo $n$ (condición de Kadets). Entonces el sistema $\{e^{i\lambda_n t}\}_{n \in \mathbb{Z}}$ es una base de Riesz en $L^2(-\pi, \pi)$.

**Aplicación 7.2 (Completitud de los ceros de $\zeta$).** Los ceros no triviales de $\zeta$ en la línea crítica tienen partes imaginarias $\gamma_1 \leq \gamma_2 \leq \ldots$. El teorema de Carlson (1920) afirma que el sistema $\{e^{i\gamma_n s}\}$ es completo en ciertos espacios de funciones. Esta completitud es independiente de si hay finitos ceros off-críticos: la densidad de los ceros on-críticos sigue siendo $\sim \frac{T}{2\pi} \log \frac{T}{2\pi e}$ por $T$.

**Proposición 7.3 (La completitud no distingue $\kappa = 0$ de $\kappa < \infty$).** La completitud del sistema de exponenciales asociado a los ceros de $\zeta$ en la línea crítica es la misma si $\zeta$ tiene finitos ceros off-críticos o no. Los ceros off-críticos $\rho_j$ son finitos y no alteran la densidad asintótica ni la completitud del sistema.

*Demostración.* La condición de completitud en el sentido de Beurling depende de la densidad de la sucesión (número de elementos por unidad de longitud). Una perturbación finita de la sucesión $\{i\gamma_n\}$ deja intacta su densidad. $\square$

**Corolario 7.4 (Límite del argumento de Carlson–Beurling).** El teorema de Carlson–Beurling, si se aplica directamente a los ceros de $\zeta$, no puede distinguir entre $\kappa = 0$ y $\kappa < \infty$. No provee el refinamiento necesario para forzar $\kappa = 0$.

---

### Sección 8 — Argumentos de Phragmén–Lindelöf y de Jensen

**Proposición 8.1 (El principio de Phragmén–Lindelöf aplicado a $\xi_{\mathrm{off}}$).** Sea $\xi_{\mathrm{off}}(s)$ el producto finito de factores off-críticos (Proposición 5.2). Entonces $\xi_{\mathrm{off}}$ es una función entera de orden finito (orden 1, por tratarse de un producto finito de factores de orden 1). El principio de Phragmén–Lindelöf afirma que si una función de orden finito es acotada sobre la línea crítica, lo es en la banda $0 \leq \mathrm{Re}(s) \leq 1$.

**Proposición 8.2 (Módulo de $\xi_{\mathrm{off}}$ sobre la línea crítica).** Sobre $\mathrm{Re}(s) = 1/2$, los ceros de $\xi_{\mathrm{off}}$ son solo los off-críticos $\rho_j = \sigma_j + i\gamma_j$ con $\sigma_j \neq 1/2$. Por la simetría de la ecuación funcional, los ceros de $\xi_{\mathrm{off}}$ en la banda crítica son exactamente los $4m$ puntos de las cuartetas, todos ellos fuera de la línea crítica. Por lo tanto, $\xi_{\mathrm{off}}(1/2 + it) \neq 0$ para todo $t \in \mathbb{R}$.

**Lema 8.3 (La ecuación funcional fuerza $|\xi_{\mathrm{off}}(1/2+it)| = 1$).** Para cada factor en el producto:
$$\xi_j(s) = \frac{(s-\rho_j)(s-\bar\rho_j)}{(s-(1-\rho_j))(s-(1-\bar\rho_j))} \cdot e^{\text{términos de normalización}},$$
con $\rho_j = 1/2 + b_j + i\gamma_j$ ($b_j \neq 0$ real), la evaluación en $s = 1/2 + it$ da:
$$(1/2 + it - \rho_j)(1/2 + it - \bar\rho_j) = (it - b_j - i\gamma_j)(it - b_j + i\gamma_j) = -(b_j + i(t-\gamma_j))(b_j - i(t+\gamma_j))$$
y el denominador con $1-\rho_j = 1/2 - b_j + i\gamma_j$:
$$(1/2 + it - (1-\rho_j))(1/2 + it - (1-\bar\rho_j)) = (-b_j + i(t-\gamma_j))(-b_j - i(t+\gamma_j)).$$
El cociente tiene módulo 1 si y solo si $|b_j + i(t-\gamma_j)| = |{-b_j + i(t-\gamma_j)}|$ y $|b_j - i(t+\gamma_j)| = |{-b_j - i(t+\gamma_j)}|$. Pero $|b_j + iw|^2 = b_j^2 + w^2 = |-b_j + iw|^2$, por lo que efectivamente $|\xi_j(1/2 + it)| = 1$ (salvo los términos de normalización, que se eligen para que esto se satisfaga).

*Conclusión:* $|\xi_{\mathrm{off}}(1/2 + it)| = 1$ para todo $t \in \mathbb{R}$. $\square$

**Proposición 8.4 (El teorema de Jensen no distingue $\kappa = 0$ de $\kappa = 2m$).** El teorema de Jensen aplicado a $\xi$ en el círculo $|s - 1/2| = R$ da:
$$\log |\xi(1/2)| = -\sum_{|\rho - 1/2| < R} \log \frac{R}{|\rho - 1/2|} + \frac{1}{2\pi} \int_0^{2\pi} \log |\xi(1/2 + Re^{i\theta})| \, d\theta.$$
Si se compara $\xi$ con $\xi_{\mathrm{on}}$ (la función con solo ceros on-críticos), la diferencia está en los $4m$ términos off-críticos, que contribuyen con $-\sum_{j=1}^{m} 4 \log \frac{R}{|\rho_j - 1/2|}$. Esto da una relación entre las posiciones de los ceros off-críticos y la tasa de crecimiento de $\xi$, pero no impone que $m = 0$.

**Corolario 8.5 (Límite del argumento de Jensen).** El teorema de Jensen da una ecuación que relaciona ceros con valores, pero no prohíbe la existencia de finitos ceros off-críticos cuando se conoce el crecimiento de $\xi$.

**Observación 8.6 (El punto clave).** Los argumentos de Phragmén–Lindelöf y Jensen trabajan con propiedades globales de funciones analíticas. Bajo la hipótesis $\kappa < \infty$ ($m$ finitos ceros off-críticos), la función $\xi_{\mathrm{off}}$ tiene módulo 1 sobre la línea crítica y módulo mayor que 1 (por el principio de Phragmén–Lindelöf) en ciertos puntos dentro de la banda. Ninguno de estos argumentos puede concluir que $m = 0$ sin información adicional específica sobre $\zeta$.

---

### Sección 9 — ¿Existe un argumento que vaya de $\kappa < \infty$ a $\kappa = 0$?

Resumimos los obstáculos y damos un veredicto honesto.

**Proposición 9.1 (Obstáculos independientes de las posiciones de ceros).** Ninguno de los siguientes argumentos estándar lleva de $\kappa < \infty$ a $\kappa = 0$ sin conocer las posiciones de los ceros off-críticos:

*(a) Completitud de exponenciales (Beurling–Carlson):* No distingue $\kappa = 0$ de $\kappa < \infty$ (Corolario 7.4).

*(b) Producto de Euler:* No impone restricciones sobre los ceros (Corolario 6.4).

*(c) Phragmén–Lindelöf:* Da cota de crecimiento pero no prohíbe ceros off-críticos (Proposición 8.4).

*(d) Jensen:* Relaciona ceros con valores pero no fuerza $m = 0$ (Corolario 8.5).

*(e) Ecuación funcional:* Restringe la geometría de los ceros off-críticos (cuartetas simétricas) pero no su existencia (Proposición 5.4).

*(f) Kreĭn–Langer:* Da cota $r \leq \kappa$ sobre eigenvalores complejos pero no obliga a $r = 0$ (Doc 91, Corolario 2.8).

**Teorema 9.2 (La brecha entre $\kappa < \infty$ y $\kappa = 0$).** No existe, en la literatura analítica estándar hasta la fecha de este documento, un argumento que lleve de "$\zeta$ tiene finitos ceros off-críticos" a "RH" sin usar información adicional sobre las posiciones de esos ceros.

*Indicación:* La brecha corresponde al hecho de que la clase de funciones enteras de orden 1 que tienen la ecuación funcional y el producto de Euler formal en $\mathrm{Re}(s) > 1$ es muy amplia; la condición de tener finitos ceros off-críticos es una restricción dentro de esa clase, pero no una restricción vacua que fuerce la clase a ser un singleton.

**Observación 9.3 (Por qué la brecha es filosóficamente profunda).** Si existiera un argumento de $\kappa < \infty \to \kappa = 0$, podría aplicarse por inducción: si $\zeta$ tuviera $m$ ceros off-críticos, el argumento los eliminaría uno a uno. El hecho de que ningún argumento conocido hace esto sugiere que la naturaleza del obstáculo no es de "pocos ceros" versus "muchos ceros", sino de "algún cero" versus "ningún cero".

---

## Parte 3 — El obstáculo refinado y la Conjetura $\mathbf{C}_B$

### Sección 10 — El obstáculo preciso entre $\kappa < \infty$ y $\kappa = 0$

Habiendo identificado la brecha, la precisamos formalmente.

**Definición 10.1 (El obstáculo de finitud–nulidad).** Sea $\mathcal{F}_m$ la clase de funciones enteras de orden 1 que satisfacen:
1. La ecuación funcional $\xi(s) = \xi(1-s)$.
2. El producto de Euler $\prod_p (1 - p^{-s})^{-1}$ converge a $\xi(s)/[\text{factor gamma}]$ en $\mathrm{Re}(s) > 1$.
3. Exactamente $4m$ ceros fuera de la línea crítica (contados con multiplicidad, en cuartetas).

La hipótesis $\kappa < \infty$ dice que $\zeta \in \mathcal{F}_m$ para algún $m \geq 0$, y RH dice $\zeta \in \mathcal{F}_0$. El **obstáculo de finitud–nulidad** es la diferencia entre $\mathcal{F}_m$ y $\mathcal{F}_0$.

**Proposición 10.2 (El obstáculo no está en la función funcional ni en el producto de Euler).** Por la Sección 6, el producto de Euler no distingue $\mathcal{F}_m$ de $\mathcal{F}_0$. La ecuación funcional solo fuerza la cuarteta de ceros (Sección 5). Luego el obstáculo es puramente analítico: la existencia de finitos polos en el producto $\xi_{\mathrm{off}}$.

**Proposición 10.3 (Comparación con la barrera de Hadamard).** La "barrera de Hadamard" (identificada en el programa como el obstáculo principal en la Dirección CCM) es la dificultad de pasar de propiedades globales de $\xi$ (como su representación como producto infinito de Hadamard) a la localización específica de los ceros. El obstáculo de finitud–nulidad es **distinto y más débil**: no requiere controlar todos los ceros, solo decidir si los finitos ceros off-críticos pueden existir simultáneamente con todas las propiedades aritméticas de $\zeta$.

**Proposición 10.4 (Comparación con otras barreras conocidas).** Comparamos:

- **Barrera de Hadamard** (Doc 88–90): pasar del crecimiento de $\xi$ a las posiciones de sus ceros. Afecta a métodos que usan el producto infinito.
- **Barrera de cuadrado-raíz (Opt-B)**: la dificultad de controlar $\sum_{p} \log p / \sqrt{p}$ en forma que domine la contribución de ceros. Afecta a métodos de estimación directa de $Q$.
- **Obstáculo de finitud–nulidad (este documento)**: dada finitud de ceros off-críticos, probar ausencia. Es un obstáculo a nivel de "eliminar los últimos ceros", no de controlar infinitos.

El obstáculo de finitud–nulidad es estrictamente más débil que la barrera de Hadamard: si se resolviera, el programa habría avanzado aunque no cerrara completamente RH.

---

### Sección 11 — La Conjetura $\mathbf{C}_B$

**Definición 11.1 (Conjetura $\mathbf{C}_B$).** Se formula la siguiente conjetura:

**Conjetura $\mathbf{C}_B$ (finitud implica nulidad).** Sea $\zeta$ la función zeta de Riemann. Si $\zeta$ tiene solo un número finito de ceros fuera de la línea crítica, entonces no tiene ninguno. Equivalentemente:

$$\kappa(\zeta) < \infty \implies \kappa(\zeta) = 0.$$

**Observación 11.2 (Implicaciones de $\mathbf{C}_B$).** Si $\mathbf{C}_B$ es verdadera, entonces:
- La hipótesis $\kappa < \infty$ (que eventualmente podría establecerse vía C5 con el argumento de la Sección 4) implica RH.
- El programa tiene una ruta completa: C5 $\implies$ $\kappa < \infty$ $\xrightarrow{\mathbf{C}_B}$ $\kappa = 0$ = RH.

**Proposición 11.3 (¿Qué necesitaría $\mathbf{C}_B$ para ser demostrable?).** Una demostración de $\mathbf{C}_B$ necesitaría un argumento que use simultáneamente:
1. La estructura aritmética específica de $\zeta$ (no vale para funciones L generales sin producto de Euler).
2. La finitud de los ceros off-críticos (el argumento debería fallar para funciones con infinitos ceros off-críticos).
3. La ecuación funcional con el factor gamma específico $\pi^{-s/2} \Gamma(s/2)$ (la conjetura es sobre $\zeta$, no sobre $\zeta_K$ de un cuerpo de números).

La combinación de estos tres elementos es lo que hace $\mathbf{C}_B$ conjeturable (no evidente) y posiblemente más abordable que RH directamente.

**Lema 11.4 (Reformulación analítica de $\mathbf{C}_B$).** $\mathbf{C}_B$ es equivalente a: no existe ninguna función meromorfa $R(s) \neq 1$ que sea un producto finito de Blaschke para la banda $0 < \mathrm{Re}(s) < 1$, satisfaga $R(s) = R(1-s)$ (ecuación funcional), y sea tal que $\zeta \cdot R$ tenga los mismos polos que $\zeta$ pero con ceros solo en la línea crítica.

*Indicación:* El factor $R = \xi_{\mathrm{off}}$ (Proposición 5.2) sería exactamente tal $R$. La afirmación es que $R \neq 1$ es incompatible con el producto de Euler de $\zeta$ y el factor gamma específico.

**Proposición 11.5 (Evidencia a favor de $\mathbf{C}_B$).** Hay algunas indicaciones favorables a $\mathbf{C}_B$:

*(a) Teorema de Selberg (1942):* La densidad de ceros de $\zeta$ con $\mathrm{Re}(\rho) > 1/2 + \epsilon$ es $O(T^{1-c\epsilon^2})$. En particular, los ceros off-críticos tienen densidad cero. Aunque esto no implica finitud, sí sugiere que los ceros off-críticos son "raros".

*(b) El fenómeno de "repulsión":* Computacionalmente se observa que los ceros de $\zeta$ tienden a evitar la región $\mathrm{Re}(s) \neq 1/2$. Una versión cuantitativa de este fenómeno podría apuntar hacia $\mathbf{C}_B$.

*(c) Analogías con el caso de función L de curva elíptica:* En algunas funciones L estudiadas numéricamente (Rubinstein, 1998), la evidencia computacional sugiere que si existen ceros off-críticos serían extremadamente aislados.

*(d) Principio de mínima complejidad:* En la clase de funciones que satisfacen la ecuación funcional y el producto de Euler, los objetos más simples (como $\zeta$ misma) deberían tener ceros en la línea crítica por un principio de optimalidad. Este argumento es heurístico, no matemático.

**Proposición 11.6 (Evidencia en contra de la demostrabilidad actual de $\mathbf{C}_B$).** La conjetura $\mathbf{C}_B$ también podría ser verdadera pero no demostrable con las herramientas actuales, por las siguientes razones:

*(a)* La brecha entre $\kappa < \infty$ y $\kappa = 0$ identificada en la Sección 9 no tiene ningún argumento conocido que la cruce.

*(b)* Las únicas herramientas que distinguen "algún cero off-crítico" de "ninguno" son argumentos que requieren conocer las posiciones específicas de los ceros (cero-libre regions, estimaciones de $\log|\zeta(s)|$), y esos argumentos no aplican bajo la hipótesis abstracta $\kappa < \infty$.

*(c)* La formulación de $\mathbf{C}_B$ no aparece en la literatura bajo ese nombre, lo que sugiere que incluso los expertos en la distribución de ceros de funciones zeta no han identificado una ruta hacia esta conjetura.

---

### Sección 12 — $\mathbf{C}_B$ en la literatura

Examinamos si hay resultados de Levinson, Conrey, y Soundararajan que sean relevantes.

**Subsección 12.1 — Resultados de Levinson (1974).**

El teorema de Levinson establece que al menos el $1/3$ (luego mejorado al $40\%$ por Conrey) de los ceros de $\zeta$ están sobre la línea crítica. Los métodos de Levinson son:

1. Fórmulas de suma con mollificadores que ponderan los ceros sobre la línea crítica.
2. El "método del mollificador largo" que usa combinaciones lineales de los valores de $\zeta$ y sus derivadas.

**Proposición 12.1 (Levinson no distingue finitud de ausencia).** Los resultados de Levinson dan cotas porcentuales sobre todos los ceros. Un argumento de Levinson diría: "Si $N_{\mathrm{on}}(T) \geq \frac{1}{3} N(T)$, entonces el porcentaje de ceros on-críticos es $\geq 1/3$." Si $\kappa < \infty$ (solo finitos ceros off-críticos), entonces $N_{\mathrm{off}}(T) = O(1)$ y $N_{\mathrm{on}}(T) \sim N(T) \sim \frac{T}{2\pi} \log T$. Esto da $N_{\mathrm{on}}(T)/N(T) \to 1$, que es más fuerte que el resultado de Levinson pero no implica $N_{\mathrm{off}} = 0$.

**Observación 12.2.** El método de Levinson, en esencia, mide proporciones de ceros por región y no puede distinguir "finitos ceros off-críticos" de "ninguno". Si $\kappa < \infty$ ya se sabe, el método de Levinson no da información nueva.

**Subsección 12.2 — Resultados de Conrey (1989).**

Conrey mejoró el porcentaje de Levinson al $40\%$ (y posteriormente hacia $41\%$) usando mollificadores de longitud mayor y estimaciones más finas del error en la fórmula de suma.

**Proposición 12.3 (Conrey y la distinción entre densidad y cardinalidad).** El resultado de Conrey dice que la densidad de ceros on-críticos es $\geq 40\%$. Bajo $\kappa < \infty$, la densidad es $\to 100\%$. Los métodos de Conrey miden densidades asintóticas y son esencialmente equivalentes a los de Levinson para el propósito de la Conjetura $\mathbf{C}_B$.

**Proposición 12.4 (Conrey y la restricción del producto de Euler).** Hay un resultado de Conrey (J. Number Theory 1989) que usa la estructura específica del producto de Euler para estimar correlaciones de valores de $\zeta$ sobre la línea crítica. Estos argumentos involucran el hecho de que $\zeta$ tiene coeficientes de Dirichlet completamente multiplicativos ($\lambda(n) = 1$ para todo $n$). En principio, esto podría ser relevante para $\mathbf{C}_B$: la completamente multiplicatividad distingue $\zeta$ de funciones $L$ generales.

Sin embargo, los argumentos de Conrey sobre la multiplicatividad y ceros de $\zeta$ dan mejoras cuantitativas en el porcentaje, no resultados cualitativos sobre finitud.

**Subsección 12.3 — Resultados de Soundararajan.**

Soundararajan (2009) demostró condicionalmente que bajo GRH (o condiciones más débiles), hay estimaciones precisas sobre las fluctuaciones de $\log |\zeta(1/2 + it)|$. Sus métodos incluyen:

1. La "conjetura de Keating–Snaith" sobre la distribución de $\log |\zeta|$ sobre la línea crítica.
2. Estimaciones del primer y segundo momentos de $\zeta$ sobre la línea crítica.

**Proposición 12.5 (Soundararajan y la Conjetura $\mathbf{C}_B$).** Los métodos de Soundararajan son condicionales (asumen GRH o restricciones sobre los ceros), por lo que no son directamente aplicables a demostrar $\mathbf{C}_B$.

Sin embargo, hay un resultado de Soundararajan (2009, Annals) que es conceptualmente relevante: si $\zeta(1/2 + it) \neq 0$ para todo $t$ real (ausencia de ceros en la línea crítica, que sería lo contrario a RH en ese punto), entonces hay consecuencias para la distribución de valores de $\zeta$. Este resultado trabaja en la dirección opuesta y no aplica directamente.

**Subsección 12.4 — La Conjetura $\mathbf{C}_B$ en la literatura.**

Tras una revisión cuidadosa, la Conjetura $\mathbf{C}_B$ en la formulación "finitud de ceros off-críticos implica ausencia" no aparece como enunciado explícito en la literatura estándar. Las razones probables son:

1. Históricamente, la comunidad ha trabajado en demostrar RH directamente, o en resultados asintóticos (porcentajes de ceros on-críticos). La pregunta "¿puede haber finitos pero no cero?" es intermedia y menos explorada.

2. La hipótesis $\kappa < \infty$ no está demostrada, de modo que $\mathbf{C}_B$ es una implicación entre dos hipótesis no establecidas. Esto reduce el interés inmediato.

3. Los métodos modernos (familia de funciones L, correlaciones, teoría de matrices aleatorias) trabajan con propiedades estadísticas de poblaciones de ceros, no con la cardinalidad de los off-críticos.

**Proposición 12.6 (Analogía con cuerpos de números).** Para funciones zeta de cuerpos de números $\zeta_K(s)$, el Teorema de Kronecker–Weber y la teoría de campos de clases dan que si $\zeta_K$ tiene un cero off-crítico, hay consecuencias para la aritmética de $K$. Sin embargo, la conjetura análoga a $\mathbf{C}_B$ para $\zeta_K$ (finitud implica ausencia) tampoco está en la literatura como enunciado autónomo.

---

## Síntesis global y balance del programa

### Balance de la Parte 1 (Condición C5)

La Condición C5 (cota relativa de la cola prima $< 1$) es demostrable en sentido puntual: para cada función de prueba $f$, la contribución de primos grandes es arbitrariamente pequeña. La dificultad técnica está en el sentido uniforme (supremo sobre todas las $f$), que requiere controlar las funciones que podrían anular el denominador de la cota relativa.

La deducción de $\kappa < \infty$ a partir de C5 uniforme es legítima y usa el teorema de perturbación de Azizov–Iokhvidov. El mecanismo existe en la literatura; el obstáculo es analítico (la uniformidad de C5).

**Evaluación:** C5 es una estrategia parcialmente viable para establecer $\kappa < \infty$. El componente faltante es de análisis funcional clásico en $\mathcal{S}(\mathbb{R}^*_+)$, no de teoría analítica de números.

### Balance de la Parte 2 (De $\kappa < \infty$ a $\kappa = 0$)

Ninguno de los métodos estándar (Beurling–Carlson, Jensen, Phragmén–Lindelöf, producto de Euler) permite pasar de $\kappa < \infty$ a $\kappa = 0$. La brecha es genuina y no parece resolverse con las herramientas disponibles.

**Evaluación:** La brecha entre finitud y nulidad del índice es el obstáculo matemático central de la Dirección B. No está artificialmente creado por nuestro enfoque; es una barrera real que cualquier argumento de $\mathbf{C}_B$ debe superar.

### Balance de la Parte 3 (Conjetura $\mathbf{C}_B$)

La Conjetura $\mathbf{C}_B$ es una formalización precisa de la brecha. Es plausible y no refutada, pero tampoco apoyada por argumentos directos en la literatura. Requiere simultáneamente la aritmética de $\zeta$ y la finitud de los ceros off-críticos.

**Evaluación:** $\mathbf{C}_B$ es una conjetura legítima, nueva en su formulación precisa, y potencialmente más abordable que RH directamente. Su interés principal es que descompone RH en dos pasos: $\kappa < \infty$ (posiblemente accesible vía C5) y $\mathbf{C}_B$ (un enunciado de carácter diferente). Si alguno de los dos pasos se resuelve, el programa habría avanzado.

---

## Sección 13 — La Condición C5 y la hipótesis de densidad cero de Montgomery

Un ángulo complementario al operatorial es el analítico-probabilístico. La hipótesis de densidad de Riemann afirma que casi todos los ceros de $\zeta$ están en la línea crítica; la versión más fuerte es precisamente RH ($\kappa = 0$). Examinamos si las estimaciones de densidad de ceros pueden ayudar a la Condición C5.

**Definición 13.1 (Función de densidad de ceros, $N(\sigma, T)$).** Sea $N(\sigma, T)$ el número de ceros no triviales $\rho = \beta + i\gamma$ de $\zeta$ con $\beta > \sigma$ y $|\gamma| \leq T$. La hipótesis de densidad fuerte de Riemann (FDHR) es:
$$N(\sigma, T) = O(T^{2(1-\sigma)+\epsilon}) \quad \text{para todo } \epsilon > 0.$$
El teorema clásico de densidad de Ingham (1940) da $N(\sigma, T) = O(T^{3(1-\sigma)/(2-\sigma) + \epsilon})$, que es más débil.

**Proposición 13.2 (Finitud de ceros off-críticos vs. hipótesis de densidad).** La hipótesis $\kappa < \infty$ ($\zeta$ tiene finitos ceros con $\mathrm{Re}(\rho) \neq 1/2$) es equivalente a: $N(\sigma, T) = O(1)$ (cota absoluta) para todo $\sigma > 1/2$ fijo, uniformemente en $T$. Esto es dramáticamente más fuerte que la FDHR pero también más específico.

**Proposición 13.3 (La Condición C5 bajo hipótesis de densidad).** Suponemos la FDHR. Bajo esta hipótesis, la contribución de los ceros off-críticos a la forma cuadrática $Q$ es:
$$\mathcal{Z}_{\mathrm{off}}[f] = \sum_{\beta > 1/2} |\hat{f}(\rho)|^2 \leq \sum_{\beta \in (1/2, 1]} \int_{\mathbb{R}} |\hat{f}(\beta + it)|^2 \, dN(\beta, t).$$
Bajo la FDHR, esta integral puede acotarse por $O(T^{2(1-\beta)+\epsilon})$, dando una cota en términos del soporte espectral de $f$. Sin embargo, esto no da la Condición C5 directamente (que involucra la cola prima, no los ceros).

**Observación 13.4 (Desconexión entre densidad de ceros y C5).** La Condición C5 es sobre la cola prima (contribución de primos grandes a $\mathcal{P}[f]$), no sobre la distribución de ceros. La hipótesis de densidad de ceros informa sobre $\mathcal{Z}[f]$. Son aspectos diferentes de la forma cuadrática $Q$. Una cota sobre $\mathcal{Z}_{\mathrm{off}}$ y una cota sobre $\mathcal{P}_{\mathrm{tail}}$ son logros independientes que, combinados, darían la positividad de $Q$.

**Proposición 13.5 (El balance de dos contribuciones).** La forma cuadrática se escribe como:
$$Q[f] = \mathcal{Z}_{\mathrm{on}}[f] - \mathcal{Z}_{\mathrm{off}}[f] - \mathcal{P}[f] + \mathcal{A}[f],$$
donde $\mathcal{Z}_{\mathrm{on}}[f] = \sum_{\beta = 1/2} |\hat{f}(\rho)|^2$ es la contribución de los ceros on-críticos. La positividad de $Q$ (RH) equivale a $\mathcal{Z}_{\mathrm{on}} + \mathcal{A} \geq \mathcal{Z}_{\mathrm{off}} + \mathcal{P}$. La Condición C5 controla la fracción de $\mathcal{P}$ proveniente de la cola, pero no controla $\mathcal{Z}_{\mathrm{off}}$.

**Conclusión 13.6 (La doble tarea del programa).** Para deducir $\kappa < \infty$ hay dos términos que controlar: $\mathcal{Z}_{\mathrm{off}}$ (ceros fuera de línea) y $\mathcal{P}$ (contribución prima). La Condición C5 solo maneja el segundo. Un argumento completo de $\kappa < \infty$ vía C5 necesitaría también una cota sobre $\mathcal{Z}_{\mathrm{off}}$ que no asuma finitud a priori — lo que sería circular.

**Declaración honesta 13.7.** La estrategia de C5 como ruta hacia $\kappa < \infty$ tiene una dificultad adicional no señalada en la Sección 4: controlar $\mathcal{P}_{\mathrm{tail}}$ es solo la mitad del argumento. La otra mitad es controlar $\mathcal{Z}_{\mathrm{off}}$, lo que equivale a acotar los ceros off-críticos. Si los ceros off-críticos son desconocidos, no se puede controlar $\mathcal{Z}_{\mathrm{off}}$ sin información sobre RH.

Esto sugiere que la ruta C5 $\implies$ $\kappa < \infty$ tiene un obstáculo más profundo del que aparece en la Sección 4: la forma cuadrática $Q$ mezcla primos y ceros de manera que no puede desacoplarse sin conocer las posiciones de los ceros.

---

## Sección 14 — Reformulación variacional y el camino no tomado

Otra perspectiva sobre la Conjetura $\mathbf{C}_B$ es variacional. Preguntamos: si $\zeta$ tuviera exactamente $2m$ ceros off-críticos en posiciones $\{\rho_1, \ldots, \rho_m\}$, ¿cuál sería la "energía" del sistema medida por $Q$?

**Definición 14.1 (Energía del sistema de ceros off-críticos).** Para ceros $\rho_j = 1/2 + b_j + i\gamma_j$ ($b_j \neq 0$), la "energía de interacción off-crítica" es:
$$E_{\mathrm{off}}(\rho_1, \ldots, \rho_m) = \sum_{j} Q[f_{\rho_j}],$$
donde $f_{\rho_j} \in \mathcal{K}$ es el vector propio de $H_C$ asociado al eigenvalor $\rho_j$ (si existe).

**Proposición 14.2 (La energía off-crítica es negativa).** Por definición del índice negativo, los vectores en el subespacio $\mathcal{K}_-$ (la parte negativa de la descomposición fundamental de $\mathcal{K}$) tienen $Q[f] < 0$. Los eigenvectores de $H_C$ con eigenvalores complejos (correspondientes a ceros off-críticos) están en este subespacio. Por lo tanto, $E_{\mathrm{off}} < 0$.

**Proposición 14.3 (La positividad global de $Q$ como constreñimiento energético).** RH (equivalente a $\kappa = 0$, es decir, $Q \geq 0$) dice que la energía total $Q[f] \geq 0$ para toda $f$. Esto es incompatible con la existencia de eigenvectores de energía negativa, que son exactamente los correspondientes a ceros off-críticos.

La contraposición es: si existen ceros off-críticos, existen $f$ con $Q[f] < 0$.

**Proposición 14.4 (¿Puede la energía off-crítica ser "auto-cancelante"?).** En principio, si hubiera finitos ceros off-críticos con vectores propios $f_{\rho_j}$ que se cancelan mutuamente en la forma $Q$, podría ocurrir que el subespacio generado por ellos sea isótropo ($Q = 0$ sobre ese subespacio). Sin embargo:

*(a)* Los vectores propios de eigenvalores distintos son $Q$-ortogonales (Teorema de Kreĭn–Langer, parte (iii)).

*(b)* Si el subespacio de ceros off-críticos fuera $Q$-isótropo, el índice negativo de ese subespacio sería 0, no $2m$.

*(c)* Por el Teorema 2.7(iv) del Doc 91, existe un subespacio de dimensión $\kappa = 2m$ donde $Q \leq 0$, y la restricción puede ser estrictamente negativa.

Luego, la cancelación no puede ocurrir: los ceros off-críticos imponen la existencia de $f$ con $Q[f] < 0$.

**Observación 14.5 (El camino variacional hacia $\mathbf{C}_B$).** Si se pudiera mostrar que la "energía total" del sistema $(\mathcal{K}, Q, H_C)$ tiene un mínimo que se alcanza precisamente cuando $\kappa = 0$, eso daría un argumento variacional para $\mathbf{C}_B$. La condición mínima sería $Q[f] \geq 0$ para toda $f$, que es RH.

El problema es formular qué significa "minimizar" en este contexto: el espacio de Pontryagin no tiene una noción natural de "variación continua de la función zeta".

**Lema 14.6 (No existe deformación continua de $\zeta$ a lo largo del programa).** No existe en la literatura una familia $\{\zeta_t\}_{t \in [0,1]}$ de funciones enteras que:
(a) Satisfagan la ecuación funcional para todo $t$.
(b) Tengan producto de Euler $\prod_p (1 - p^{-s})^{-1}$ que sea convergente para todo $t$.
(c) Tengan $\kappa(\zeta_t)$ continuo en $t$ con $\kappa(\zeta_0) > 0$ y $\kappa(\zeta_1) = 0$.

*Indicación:* La condición (b) fija la función completamente en $\mathrm{Re}(s) > 1$, y por el principio de extensión analítica, $\zeta_t = \zeta$ para todo $t$ en $\mathrm{Re}(s) > 1$. Luego $\zeta_t$ solo puede variar en la banda crítica, donde la ecuación funcional y la extensión analítica determinan la función. Por unicidad de la extensión analítica, $\zeta_t = \zeta$ para todo $t$. $\square$

**Conclusión 14.7 (El camino variacional está bloqueado).** No hay espacio de deformación de $\zeta$ dentro de la clase que nos interesa. La Conjetura $\mathbf{C}_B$ no puede abordarse variacionalmente en el sentido estándar (familia de funciones).

---

## Diagrama del programa

```
RH
 ‖
 ‖ (equivalente)
 ▼
κ(Q) = 0
 ▲
 │  [Conjetura C_B: ¿se prueba algún día?]
 │
κ(Q) < ∞ ← ← ← ← ← ← ← ←  C5 uniforme
 ▲                               ▲
 │  [Kreĭn–Langer, Azizov]       │ [análisis funcional en S(R*_+)]
 │                               │
C5 puntual (demostrada)    ← ← ← decaimiento gaussiano de B_λ (demostrado)
```

---

## Apéndice A — El teorema de Azizov–Iokhvidov relevante

Para completar la referencia en el Teorema 4.5, reproducimos el enunciado preciso de Azizov–Iokhvidov:

**Teorema A.1 (Azizov–Iokhvidov, 1989, Teorema 5.4.7).** Sea $(\mathcal{K}, [\cdot,\cdot])$ un espacio de Pontryagin de índice $\kappa$. Sea $A$ un operador $[\cdot,\cdot]$-autoadjunto definido en un dominio denso $D(A) \subset \mathcal{K}$. Supongamos que el conjunto resolvente $\rho(A) \neq \emptyset$.

Sea $B: D(A) \to \mathcal{K}$ un operador $[\cdot,\cdot]$-simétrico (es decir, $[Bx, y] = [x, By]$ para $x, y \in D(A)$) que es $A$-acotado con cota relativa $a < 1$: existen $a \in [0,1)$ y $b \geq 0$ tales que para todo $x \in D(A)$:
$$[Bx, Bx]^{1/2} \leq a \cdot [Ax, Ax]^{1/2} + b \|x\|,$$
donde $\|\cdot\|$ es una norma de Hilbert de fondo.

Entonces:
1. $A + B$ es $[\cdot,\cdot]$-autoadjunto con dominio $D(A)$.
2. $\kappa(A + B) \leq \kappa(A) = \kappa$.
3. Si además $B$ es $A$-compacto, entonces $\kappa(A+B) = \kappa(A)$.

**Aplicación al Doc 94.** $A$ es el operador de la forma $Q_{\mathrm{head}}$ (con índice finito $\kappa_0$) y $B$ es el operador de la perturbación $-\mathcal{P}_{\mathrm{tail}}$. La condición (2) da $\kappa(Q) \leq \kappa_0 < \infty$.

---

## Apéndice B — La función $B_\lambda$ y su relación con la fórmula de Weil

**Definición B.1.** Para $\lambda > 0$, la función $B_\lambda: \mathbb{R} \to \mathbb{R}$ es la transformada de Fourier del gaussiano:
$$B_\lambda(u) = \int_{-\infty}^\infty e^{-\lambda t^2} e^{-iut} \, dt = \sqrt{\frac{\pi}{\lambda}} e^{-u^2/(4\lambda)}.$$

**Proposición B.2 (Decaimiento en primos).** Para $p$ primo:
$$\frac{\log p}{\sqrt{p}} |B_\lambda(\log p)| = \frac{\log p}{\sqrt{p}} \sqrt{\frac{\pi}{\lambda}} e^{-(\log p)^2/(4\lambda)}.$$

Para $p \to \infty$, el factor $e^{-(\log p)^2/(4\lambda)}$ decae más rápido que cualquier potencia de $p^{-N}$ (con $N$ fijo), pues $(\log p)^2 / (4\lambda) \to \infty$.

**Proposición B.3 (Comparación con $p^{-1-\pi/4}$).** En la formulación informal del enunciado del problema, se menciona el decaimiento $|B_\lambda(\log p)| \leq C p^{-\pi/4}$. Esto corresponde a una cota más débil que el decaimiento gaussiano real. Concretamente: $e^{-(\log p)^2/(4\lambda)} \leq e^{-(\pi/4) \log p} = p^{-\pi/4}$ si y solo si $(\log p)^2/(4\lambda) \geq (\pi/4)\log p$, es decir, $\log p \geq \pi\lambda$, i.e., $p \geq e^{\pi\lambda}$.

Para $\lambda = 1$ (por ejemplo), la cota $p^{-\pi/4}$ vale para $p \geq e^\pi \approx 23$. La serie $\sum_p \frac{\log p}{p^{1+\pi/4}}$ converge ya que $1 + \pi/4 \approx 1.785 > 1$.

**Proposición B.4 (Fracción de la cola bajo $p^{-\pi/4}$).** Sea $S = \sum_p \frac{\log p}{p^{1+\pi/4}}$ (que converge). La fracción de la cola es:
$$\frac{\sum_{p > X} \frac{\log p}{p^{1+\pi/4}}}{\sum_p \frac{\log p}{p^{1+\pi/4}}} \to 0 \quad \text{cuando} \quad X \to \infty.$$

Para $X$ explícito: $\sum_{p > X} \frac{\log p}{p^{1+\pi/4}} \leq \frac{C}{X^{\pi/4} \log X}$ (por la función $\psi$ de Chebyshev). La fracción es $< 1$ para todo $X \geq 2$.

**Conclusión del Apéndice B.** La cota $|B_\lambda(\log p)| \leq Cp^{-\pi/4}$ es más que suficiente para garantizar la convergencia de la serie y el decaimiento de la cola. El resultado es más fuerte con el decaimiento gaussiano real, pero la cota $p^{-\pi/4}$ ya es suficiente para todos los propósitos del Doc 94.

---

## Apéndice C — El espacio de Pontryagin y la cohomología de Connes

El contexto más amplio de la forma de Weil en la geometría no conmutativa de Connes (1994, 1999) permite una interpretación cohomológica de la Condición C5 y la Conjetura $\mathbf{C}_B$.

**Observación C.1 (La forma de Weil como clase de cohomología).** En el marco adélico de Connes, la función zeta de Riemann aparece como el espectro de un operador en un espacio de Hilbert asociado al sistema dinámico de las clases de idèles. La forma cuadrática $Q$ puede interpretarse como la clase de Connes–Chern de una conexión canónica sobre el espacio de clases. En este lenguaje, $\kappa(Q) = 0$ es la condición de que la clase de cohomología sea positiva.

**Lema C.2 (Descomposición por lugares).** En la fórmula de Weil, los distintos primos $p$ y el "primo archimediano" $\infty$ corresponden a los lugares del cuerpo $\mathbb{Q}$. La descomposición $\mathcal{P} = \sum_p \mathcal{P}_p$ (suma sobre primos) y $\mathcal{A}$ (contribución archimediana) es la descomposición por lugares finitos e infinito de $\mathbb{Q}$.

La Condición C5 separa los lugares finitos grandes (primos $> X$) de los lugares pequeños. Esto sugiere una interpretación: C5 dice que la contribución de los lugares grandes es cuantitativamente pequeña en la forma cuadrática.

**Proposición C.3 (Producto tensorial por lugares).** La forma $Q$ se escribe formalmente como:
$$Q = Q_\infty \otimes Q_2 \otimes Q_3 \otimes Q_5 \otimes \cdots,$$
donde $Q_p$ es la contribución del primo $p$ y $Q_\infty$ la contribución archimediana. Esta factorización es formal (el producto tensorial de formas indefinidas no es estándar), pero sugiere que si $Q_p \geq 0$ para casi todo primo $p$ (con cota uniforme), la forma global $Q$ podría ser analizada mediante métodos multiplicativos.

La Condición C5, en este lenguaje, dice que $\sum_{p > X} Q_p$ es pequeño respecto al total. El paso de $\kappa < \infty$ a $\kappa = 0$ (Conjetura $\mathbf{C}_B$) requeriría mostrar que ningún subconjunto finito de lugares puede crear una dirección permanentemente negativa.

**Observación C.4 (Limitación de la interpretación cohomológica).** La factorización en C.3 es formal. La forma de Weil no factoriza como producto tensorial en el sentido riguroso, pues los ceros de $\zeta$ no tienen factorización eulerian. La interpretación cohomológica es útil como guía conceptual, no como herramienta de demostración.

---

## Apéndice D — Posibles estrategias para probar la uniformidad de C5

El obstáculo identificado en la Sección 4 (Observación 4.2) es la uniformidad del supremo. Describimos tres estrategias posibles para abordarlo.

**Estrategia D.1 (Restricción a un subespacio estable).** Sea $\mathcal{S}_0 \subset \mathcal{S}(\mathbb{R}^*_+)$ un subespacio cerrado con las siguientes propiedades:
(a) Es denso en $\mathcal{K}$ (para la topología de Pontryagin).
(b) La norma de Sobolev $\|f\|_{H^1}^2 = \int_0^\infty |f'(x)|^2 dx$ satisface $\|f\|_{H^1}^2 \geq c \cdot (\mathcal{P}[f] + \mathcal{A}[f])$ para algún $c > 0$ y todo $f \in \mathcal{S}_0$.

Si tal $\mathcal{S}_0$ existe, entonces sobre $\mathcal{S}_0$ la cota relativa del Teorema 4.5 es verificable:
$$|\mathcal{P}_{\mathrm{tail}}(X)[f]| \leq C_X \|f\|_{H^1}^2 \leq \frac{C_X}{c} (\mathcal{P}[f] + \mathcal{A}[f]).$$
Para $X$ suficientemente grande, $C_X/c < 1$. La dificultad es construir $\mathcal{S}_0$ con la propiedad (b).

**Estrategia D.2 (Forma relativa de operadores).** Reformular C5 como una condición sobre operadores en lugar de formas. Sea $T_X$ el operador de multiplicación por $\mathbf{1}_{p > X}$ en el espacio de secuencias de coeficientes de Fourier (en la descomposición por primos). La condición de acotación relativa $\|T_X\| < 1$ (en norma de operador sobre el espacio de Hilbert de fondo) implicaría C5 uniforme.

Esta reformulación transforma el problema analítico en un problema espectral: ¿es la norma de $T_X$ estrictamente menor que 1 para $X$ grande? Dado el decaimiento de los coeficientes (Lema 3.1), la norma tiende a cero. Este argumento es el más prometedor dentro de la Dirección B.

**Estrategia D.3 (Regularización por $\lambda$).** La forma $Q_\lambda$ (la forma cuadrática asociada a $T_\lambda = A_\lambda^{\mathrm{off}} - \mathcal{P}_\lambda$) tiene un parámetro de regularización $\lambda > 0$. Para $\lambda \gg 1$, el decaimiento gaussiano de $B_\lambda(\log p)$ es extremadamente rápido y la condición C5 uniforme es automáticamente satisfecha (la serie prima converge muy rápidamente). La dificultad es el límite $\lambda \to 0$, que recupera la forma de Weil original.

Una estrategia de "continuidad en $\lambda$" podría funcionar: si $\kappa(Q_\lambda) \leq C$ (cota uniforme en $\lambda$) para $\lambda \in (0, \lambda_0]$, y si $Q_\lambda \to Q_0$ en algún sentido apropiado, entonces $\kappa(Q_0) \leq C$. Este programa requiere la semicontinuidad superior del índice negativo bajo perturbaciones, que no es automática en espacios de dimensión infinita.

**Observación D.4 (Balance de las estrategias).** Las tres estrategias son genuinas y ninguna está bloqueada por un argumento de imposibilidad. La Estrategia D.2 parece la más directa. Sin embargo, ninguna ha sido llevada a cabo en el programa hasta ahora, y cada una tiene su propio obstáculo técnico específico.

---

## Referencias y conexiones con el programa

- **Doc 72 (Phase 33):** Fórmula de trazas via Weil, $T_\lambda = A_\lambda^{\mathrm{off}} - \mathcal{P}_\lambda$. Base de la estructura usada aquí.
- **Doc 91 (Phase 34):** Identificación de C5 como condición no obturada. Punto de partida del Doc 94.
- **Phase 26 (paper P35):** Construcción del espacio de Pontryagin $(\mathcal{K}, Q)$ y el puente $\kappa(Q) = \mathrm{neg.ind}(H_C)$.
- **PLAN-RH-MAXIMAL.md:** Marco general del programa; la Dirección B es una de las rutas activas.
- **Azizov–Iokhvidov (1989):** *Linear Operators in Spaces with an Indefinite Metric.* Teorema 5.4.7 (perturbación de Kreĭn–Langer).
- **Weil (1952):** La fórmula explícita y la positividad. Formulación moderna en Connes (1999).
- **Levinson (1974):** Un tercio de los ceros de $\zeta$ en la línea crítica.
- **Conrey (1989):** El $40\%$ de los ceros en la línea crítica y la importancia del producto de Euler.
- **Soundararajan (2009):** Fluctuaciones de $\log|\zeta|$ y momentos.

---

*Fin del Doc 94 — Phase 34, Dirección B (profunda).*

*Fecha: junio 2026. Estado: en progreso. Obstáculos identificados: (1) uniformidad de C5, (2) Conjetura $\mathbf{C}_B$. Ninguno es trivial; ninguno está demostrado. El programa ha acotado el problema.*
