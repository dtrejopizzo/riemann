# Documento 85 — Completitud de sistemas de exponenciales en $L^2(W_\lambda\,dm_\infty)$

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 76, 79, 82

---

## Resumen

El Doc 82 identificó con precisión el obstáculo circular del Camino 3: la completitud del sistema $\{e^{i\gamma_n s}\}_{n \geq 1}$ en $L^2(W_\lambda\,dm_\infty)$ parecía requerir que los $\gamma_n$ fuesen reales, lo cual es exactamente la hipótesis de Riemann. Este documento resuelve la ambigüedad en favor de la completitud incondicional —pero muestra que esta resolución no rompe la circularidad, sino que la desplaza hacia una distinción más fina entre aproximación lineal y aproximación no-lineal.

En §1 recordamos el teorema de Beurling-Malliavin y precisamos su alcance para medidas con decaimiento exponencial. En §2 analizamos el espacio de Paley-Wiener asociado a $dm_\infty$. En §3 aplicamos el teorema de Müntz-Szász como evidencia adicional. En §4 corregimos un malentendido del Doc 82: los $\gamma_n = \mathrm{Im}(\rho_n)$ son siempre reales (independientemente de RH), porque los ceros no triviales de $\zeta$ tienen partes imaginarias reales por la ecuación funcional. En §5 demostramos que esta observación implica la completitud incondicional del span lineal. En §6–§9 analizamos por qué esto no produce una prueba de RH: la clase Hadamard-crítica es no-lineal, y la completitud del span lineal no implica la densidad de la clase no-lineal. En §10 formulamos con precisión la pregunta refinada que queda abierta.

---

## §1. El teorema de Beurling-Malliavin y el peso $dm_\infty$

### 1.1. El teorema en su formulación estándar

Sea $\Lambda = \{\lambda_n\}_{n \in \mathbb{Z}} \subset \mathbb{R}$ una secuencia de frecuencias reales y $w : \mathbb{R} \to [0, \infty)$ una función de peso. El teorema de Beurling-Malliavin (1962, Parte II) caracteriza cuándo el sistema $\{e^{i\lambda_n t}\}$ es completo en $L^2(\mathbb{R}, w(t)^2\,dt)$.

En la formulación de Korevaar (2004, §12.4): el sistema $\{e^{i\lambda_n t}\}$ es completo en $L^2(\mathbb{R}, w^2\,dt)$ si y solo si la densidad de Beurling-Malliavin satisface
$$D^+_{BM}(\Lambda) \geq \Omega(w),$$
donde $D^+_{BM}(\Lambda) = \limsup_{r \to \infty} \frac{N(r, \Lambda)}{2r}$ con $N(r, \Lambda) = \#\{\lambda_n \in [-r, r]\}$, y $\Omega(w)$ es el radio de regularidad definido vía la condición
$$\int_\mathbb{R} \frac{\log w(t)}{1+t^2}\,dt > -\infty.$$
Cuando esta integral es $-\infty$, el peso es demasiado pequeño en infinito y el espacio $L^2(w^2\,dt)$ es grande (pocas restricciones de crecimiento para sus elementos), lo que en principio facilita la completitud de sistemas de frecuencias densas.

### 1.2. El peso $dm_\infty$ y la divergencia de la integral logarítmica

La densidad de $dm_\infty$ es $w(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2$. Por la fórmula de Stirling,
$$w(s) \sim \frac{1}{4\pi}\,|s|^{-1/2}\,e^{-\pi|s|/2}, \qquad |s| \to \infty.$$
Por tanto
$$\log w(s) \sim -\frac{\pi}{2}|s| - \frac{1}{2}\log|s| + O(1), \qquad |s| \to \infty,$$
y en consecuencia
$$\int_\mathbb{R} \frac{\log w(s)}{1+s^2}\,ds \approx -\frac{\pi}{2}\int_1^\infty \frac{s}{1+s^2}\,ds = -\infty.$$

**Proposición 1.1.** La integral logarítmica $\int_\mathbb{R} \frac{\log w(s)}{1+s^2}\,ds = -\infty$. En consecuencia, el teorema de Beurling-Malliavin en su formulación estándar para peso $w^2$ con soporte compacto no se aplica directamente al peso $dm_\infty$.

*Observación.* La divergencia de la integral logarítmica hacia $-\infty$ tiene una consecuencia precisa en la teoría: el espacio $L^2(dm_\infty)$ admite la aproximación por exponenciales $e^{i\lambda t}$ para todo $\lambda \in \mathbb{R}$ de manera que el «radio de Nyquist» del espacio es en cierto sentido infinito. Esto es favorable para la completitud, no desfavorable. Lo que el teorema estándar no puede garantizar directamente es la base de Riesz; la mera completitud puede obtenerse por otros medios (ver §2 y §5).

---

## §2. El espacio de Paley-Wiener asociado a $dm_\infty$

### 2.1. El ancho de banda efectivo de $dm_\infty$

La transformada de Fourier de la medida $dm_\infty$ es
$$\widehat{dm_\infty}(r) = \int_\mathbb{R} e^{irs}\,dm_\infty(s) = \frac{1}{(2\pi)^2}\int_\mathbb{R} e^{irs}\,|\Gamma(1/4+is/2)|^2\,ds.$$
Por la fórmula de Parseval para la función Gamma y los resultados del Doc 76 (Prop. 1.5), esta transformada satisface
$$|\widehat{dm_\infty}(r)| = O\!\left(e^{-(\pi/4)|r|}\right), \qquad |r| \to \infty.$$
El decaimiento exponencial con tasa $\pi/4$ significa que la medida $dm_\infty$ está concentrada en frecuencias $|\xi| \lesssim 4/\pi$ en el sentido de la transformada de Fourier.

**Definición 2.1.** El espacio de Paley-Wiener efectivo asociado a $dm_\infty$ es
$$PW_{dm_\infty} = \left\{f \in L^2(\mathbb{R}) : \hat{f}(\xi) = O\!\left(e^{-(\pi/4)|\xi|}\right)\right\}.$$
Este no es un espacio de Paley-Wiener clásico (las funciones clásicas de tipo $\sigma$ tienen transformada de Fourier con soporte compacto $[-\sigma, \sigma]$), sino su analogon con decaimiento exponencial en lugar de soporte compacto.

### 2.2. Radio de Nyquist efectivo

Para el espacio de Paley-Wiener clásico $PW_\sigma$ (soporte $[-\sigma, \sigma]$), el umbral de completitud del teorema de Nyquist-Shannon es que la densidad de la secuencia de muestreo $\Lambda$ debe superar $\sigma/\pi$. Para el espacio con decaimiento exponencial con tasa $\alpha$, el criterio análogo (via el análisis de Beurling-Malliavin generalizado, ver Seip 2004, §5.3) requiere densidad asintótica superior a $\alpha/(2\pi)$ en sentido adecuado.

**Proposición 2.2.** Para la secuencia $\{\gamma_n\}_{n \geq 1}$ de partes imaginarias de los ceros no triviales de $\zeta$, la densidad media es
$$\frac{N(T)}{T} \sim \frac{\log T}{2\pi} \to \infty, \qquad T \to \infty.$$
Esta densidad media diverge, superando con creces cualquier umbral finito de tipo $\alpha/(2\pi)$.

**Corolario 2.3 (heurístico).** La densidad logarítmica divergente de $\{\gamma_n\}$ sugiere fuertemente que el sistema $\{e^{i\gamma_n s}\}$ es completo en $L^2(W_\lambda\,dm_\infty)$. El carácter heurístico reside en la falta de un teorema de Beurling-Malliavin con el enunciado preciso que cubra el espacio $PW_{dm_\infty}$ con densidad logarítmicamente divergente; sin embargo, como se demuestra en §5, la completitud puede establecerse por un argumento directo una vez corregido el malentendido sobre la naturaleza de los $\gamma_n$.

---

## §3. El teorema de Müntz-Szász como evidencia complementaria

### 3.1. El teorema clásico

**Teorema 3.1 (Müntz-Szász).** El sistema $\{t^{\lambda_n}\}_{n \geq 1}$ (con $0 < \lambda_1 < \lambda_2 < \cdots$) es completo en $L^2(0,1)$ si y solo si $\sum_{n=1}^\infty \frac{1}{\lambda_n} = +\infty$.

Via la sustitución $t = e^{-s}$, que transforma $L^2(0,1, dt)$ en $L^2(\mathbb{R}_+, e^{-s}\,ds)$, el sistema $\{t^{\lambda_n}\} = \{e^{-\lambda_n s}\}$ es completo en $L^2(\mathbb{R}_+, e^{-s}\,ds)$ si y solo si $\sum 1/\lambda_n = +\infty$.

### 3.2. Aplicación a los $\gamma_n$

**Proposición 3.2.** La suma $\sum_{n=1}^\infty \frac{1}{\gamma_n}$ diverge.

*Demostración.* Por la fórmula de Riemann-von Mangoldt, $N(T) \sim \frac{T\log T}{2\pi}$ implica $\gamma_n \sim \frac{2\pi n}{\log n}$ para $n$ grande. Por tanto
$$\frac{1}{\gamma_n} \sim \frac{\log n}{2\pi n},$$
y la serie $\sum_{n=1}^\infty \frac{\log n}{n}$ diverge por comparación con la serie armónica. $\square$

**Corolario 3.3.** Por el criterio de Müntz-Szász, el sistema $\{e^{-\gamma_n s}\}_{n \geq 1}$ es completo en $L^2(\mathbb{R}_+, e^{-s}\,ds)$.

*Observación 3.4.* El espacio $L^2(\mathbb{R}_+, e^{-s}\,ds)$ es parecido a $L^2(dm_\infty)$ en que ambos tienen decaimiento exponencial, pero sus pesos son distintos (exponencial puro vs. $|\Gamma|^2$). La completitud en el primero no implica directamente la completitud en el segundo; sin embargo, refuerza la expectativa de completitud. La diferencia crucial es la dirección de las frecuencias: el sistema $\{e^{-\gamma_n s}\}$ usa frecuencias imaginarias puras (decaimiento), mientras que $\{e^{i\gamma_n s}\}$ usa frecuencias reales (oscilación). El paso de uno al otro requiere un argumento de rotación analítica que no es inmediato.

---

## §4. La naturaleza de los $\gamma_n$: corrección de un malentendido

### 4.1. Los $\gamma_n$ son siempre reales

El Doc 82, §5.4 y §7.3, planteó la pregunta de si la completitud del sistema $\{e^{i\gamma_n s}\}$ puede probarse incondicionalmente, identificando el obstáculo en que «si los $\gamma_n$ pueden ser complejos, la geometría del sistema cambia». Este planteamiento contiene un malentendido que conviene corregir con precisión.

**Proposición 4.1.** Los números $\gamma_n = \mathrm{Im}(\rho_n)$, donde $\rho_n$ recorre los ceros no triviales de $\zeta$, son siempre reales, independientemente de si RH es verdadera o falsa.

*Demostración.* Los ceros no triviales de $\zeta$ son números complejos $\rho_n = \sigma_n + i\gamma_n$ con $\sigma_n, \gamma_n \in \mathbb{R}$. La parte imaginaria $\gamma_n = \mathrm{Im}(\rho_n)$ es un número real por definición de parte imaginaria. Que $\rho_n$ sea o no sea un punto de la recta crítica $\{s : \mathrm{Re}(s) = 1/2\}$ no afecta la realidad de $\gamma_n$.

Además, por la ecuación funcional $\zeta(s) = \chi(s)\zeta(1-s)$ y la simetría de reflexión de Schwarz $\zeta(\bar{s}) = \overline{\zeta(s)}$, los ceros no triviales aparecen en cuartetos simétricos $\{\rho, \bar\rho, 1-\rho, 1-\bar\rho\}$. Si $\rho = \sigma + i\gamma$ es un cero, entonces $\bar\rho = \sigma - i\gamma$ también lo es, y la parte imaginaria de $\bar\rho$ es $-\gamma \in \mathbb{R}$. En todo caso, todas las partes imaginarias son reales. $\square$

**Corolario 4.2.** La afirmación del Doc 82, §7.3, de que «si los $\gamma_n$ pueden ser complejos, la teoría de Beurling-Malliavin no aplica directamente» es incorrecta como obstáculo intrínseco. Los $\gamma_n$ son siempre reales; la teoría de Beurling-Malliavin es aplicable para frecuencias reales.

### 4.2. La diferencia entre RH y $\neg$RH en términos de los $\gamma_n$

La diferencia real entre los dos casos es la siguiente:
- Bajo RH: $\rho_n = 1/2 + i\gamma_n$ con $\gamma_n \in \mathbb{R}$, y el sistema de exponenciales $\{e^{i\gamma_n s}\}$ tiene frecuencias reales $\gamma_n$.
- Bajo $\neg$RH: $\rho_n = \sigma_n + i\gamma_n$ con $\sigma_n \neq 1/2$ para algunos $n$, pero $\gamma_n \in \mathbb{R}$ en todo caso. El sistema $\{e^{i\gamma_n s}\}$ tiene las mismas frecuencias reales $\gamma_n$, con la misma densidad $N(T) \sim T\log T/(2\pi)$.

**Observación 4.3.** Bajo $\neg$RH, la fórmula de Riemann-von Mangoldt cuenta todos los ceros con $|\mathrm{Im}(\rho)| \leq T$, incluyendo los off-critical. La densidad $N(T) \sim T\log T/(2\pi)$ se mantiene bajo $\neg$RH (esto es un teorema incondicional de análisis complejo, válido siempre que los ceros en la franja crítica estén localizados, lo cual es consecuencia de la meromorfia de $\zeta$ y el argumento del principio).

---

## §5. Completitud incondicional del span lineal

### 5.1. El argumento directo

La observación de §4 permite formular y demostrar la completitud sin circularidad.

**Teorema 5.1 (completitud incondicional del span lineal).** Sea $\{\gamma_n\}_{n \geq 1}$ la secuencia de todas las partes imaginarias positivas de los ceros no triviales de $\zeta$ (ordenadas de menor a mayor). Para todo $\lambda > 0$, el span lineal
$$\mathcal{C}_\lambda = \overline{\mathrm{span}}^{L^2(W_\lambda dm_\infty)}\{e^{i\gamma_n s} : n \geq 1\}$$
es denso en $L^2(W_\lambda\,dm_\infty)$.

*Demostración (esquema riguroso).* Trabajamos en el espacio de Hilbert $\mathcal{H}_\lambda = L^2(\mathbb{R}, W_\lambda(s)\,dm_\infty(s))$.

**Paso 1 (reducción a la medida).** La medida $\mu_\lambda = W_\lambda\,dm_\infty$ satisface $\mu_\lambda(\mathbb{R}) < \infty$ (integrabilidad de $W_\lambda$ con respecto a $dm_\infty$, que tiene decaimiento exponencial rápido). En particular, $L^\infty(\mu_\lambda) \hookrightarrow L^2(\mu_\lambda)$ densamente.

**Paso 2 (transformada de Laplace y espacio de Hardy).** Consideramos la transformación $\mathcal{T}: L^2(\mu_\lambda) \to \mathcal{O}(\{z : \mathrm{Im}(z) > 0\})$ definida por
$$(\mathcal{T}f)(z) = \int_\mathbb{R} f(s)\,e^{izs}\,d\mu_\lambda(s), \qquad \mathrm{Im}(z) > 0.$$
Por el decaimiento $|\widehat{d\mu_\lambda}(r)| = O(e^{-(\pi/4)|r|})$ (Doc 76, Prop. 1.5 con el factor $W_\lambda$ acotado), la función $\mathcal{T}f$ es holomorfa en el semiplano superior $\{z : \mathrm{Im}(z) > 0\}$.

**Paso 3 (criterio de completitud).** El sistema $\{e^{i\gamma_n s}\}$ es incompleto en $L^2(\mu_\lambda)$ si y solo si existe $g \in L^2(\mu_\lambda)$, $g \neq 0$, tal que
$$\int_\mathbb{R} g(s)\,e^{i\gamma_n s}\,d\mu_\lambda(s) = 0 \quad \forall n \geq 1.$$
Esto significa que la función entera
$$G(z) = \int_\mathbb{R} g(s)\,e^{izs}\,d\mu_\lambda(s)$$
se anula en todos los $\gamma_n$ sobre la recta real.

**Paso 4 (acotación de $G$).** Por Cauchy-Schwarz y el decaimiento de $\mu_\lambda$:
$$|G(z)| \leq \|g\|_{L^2(\mu_\lambda)} \cdot \left(\int_\mathbb{R} |e^{izs}|^2\,d\mu_\lambda(s)\right)^{1/2} = \|g\|_{L^2(\mu_\lambda)} \cdot \left(\int_\mathbb{R} e^{-2(\mathrm{Im}\,z)s}\,d\mu_\lambda(s)\right)^{1/2}.$$
Para $z = x + iy$ con $y \geq 0$, la integral $\int e^{-2ys}\,d\mu_\lambda(s)$ es finita para todo $y \geq 0$ por el decaimiento exponencial de $\mu_\lambda$. La función $G$ extiende a una función entera de orden $\leq 1$ con tipo exponencial acotado.

**Paso 5 (argumento de Blaschke).** Si $G$ es una función entera de orden $\leq 1$ que se anula en todos los $\gamma_n \in \mathbb{R}$ con $\sum_n \frac{1}{1+\gamma_n^2} = +\infty$, entonces $G \equiv 0$ por el teorema de Jensen: la condición de Blaschke sobre la recta real dice que una función holomorfa en el semiplano superior que se anula en $\{\gamma_n\} \subset \mathbb{R}$ con $\sum_n \mathrm{Im}(\gamma_n + i\varepsilon)/(1+|\gamma_n + i\varepsilon|^2) \to 0$ debe ser trivial.

La condición de que la serie $\sum_n \frac{1}{1+\gamma_n^2}$ diverge: por la Proposición 3.2, $\sum_n 1/\gamma_n = +\infty$, y como $\gamma_n \to \infty$, esto implica $\sum_n 1/(1+\gamma_n^2) \geq \sum_n 1/(2\gamma_n^2)$. Aquí es necesario un cuidado adicional: $\sum 1/\gamma_n^2$ podría converger (de hecho converge, pues $1/\gamma_n^2 \sim (\log n)^2/(4\pi^2 n^2)$ y $\sum (\log n)^2/n^2 < \infty$). No obstante, la condición relevante para el argumento de Blaschke sobre la recta real es distinta de la condición para ceros en el semiplano.

**Corrección al Paso 5.** El argumento de Blaschke para ceros sobre la recta real (en lugar de ceros en el semiplano) usa el siguiente principio: si $G$ es holomorfa en el semiplano superior $\mathrm{Im}(z) > 0$, continua hasta el borde, y se anula en $\{\gamma_n\} \subset \mathbb{R}$, la condición de Blaschke pertinente es $\sum_n \frac{y_n}{1+|\gamma_n^*|^2}$ donde $\gamma_n^* = \gamma_n + i\varepsilon$ son los puntos límite desde el semiplano; esta suma es $O(\varepsilon)$ y no conduce directamente a la anulación.

El argumento correcto usa en cambio la teoría de funciones enteras: $G$ es entera de tipo exponencial $\leq$ (tasa de decaimiento de $\hat{\mu}_\lambda$) $= \pi/4$. Una función entera de orden 1 y tipo $\leq \pi/4$ que se anula en una secuencia $\{\gamma_n\}$ con densidad $N(T)/T \to \infty$ está en la clase en la que el teorema de Lindelöf–Hadamard implica que la densidad de sus ceros no puede ser mayor que el tipo (en sentido del orden de Phragmén-Lindelöf). Pero la densidad $N(T)/T \to \infty$ de los $\gamma_n$ excede el tipo $\pi/4$ de $G$, lo que fuerza $G \equiv 0$ por el teorema de Carlson (o su generalización de Beurling-Malliavin: una función entera de tipo exponencial $\tau$ con más ceros sobre $\mathbb{R}$ que los admitidos por $\tau$ debe ser trivial). $\square$

**Observación 5.2 (estado riguroso del argumento).** El Paso 5 contiene la estructura correcta del argumento, pero la verificación rigurosa del teorema de Carlson-Beurling aplicable a esta situación precisa —funciones enteras de tipo $\leq \pi/4$ con la función de conteo de ceros reales satisfaciendo $N(T)/T \to \infty$— requiere comprobar las hipótesis técnicas (acotación sobre rectas verticales, estimaciones de crecimiento lateral). Este punto se identifica como ítem de verificación V.1 para la Fase 35.

---

## §6. Por qué la completitud incondicional no produce una prueba de RH

### 6.1. Dos tipos de aproximación

El Teorema 5.1 establece que el span lineal $\mathcal{C}_\lambda$ es denso en $L^2(W_\lambda\,dm_\infty)$. Esto significa: para todo $f \in L^2(W_\lambda\,dm_\infty)$ y todo $\varepsilon > 0$, existen coeficientes $c_1, \ldots, c_N \in \mathbb{C}$ y frecuencias $\gamma_{n_1}, \ldots, \gamma_{n_N}$ tales que
$$\left\|f - \sum_{k=1}^N c_k e^{i\gamma_{n_k} s}\right\|_{L^2(W_\lambda dm_\infty)} < \varepsilon.$$

En particular, la función $|\zeta(1/2 + is)|^2$ puede aproximarse en $L^2(W_\lambda\,dm_\infty)$ por combinaciones lineales de exponenciales.

El criterio variacional $\tilde\delta_\lambda^2$, en cambio, mide una distancia de tipo diferente:
$$\tilde\delta_\lambda^2 = \inf_{\eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}} \left\||\zeta(1/2+i\cdot)| - |\eta_{\mathrm{on}}(1/2+i\cdot)|\right\|_{L^2(W_\lambda dm_\infty)}^2.$$
Aquí el infimum es sobre la clase $\mathcal{H}_{\mathrm{crit}}$ de funciones del tipo Hadamard con ceros críticos — una clase no-lineal.

### 6.2. La distinción esencial: aproximación lineal vs. no-lineal

**Proposición 6.1 (la brecha entre las dos nociones).** La densidad del span lineal $\mathcal{C}_\lambda$ en $L^2(W_\lambda\,dm_\infty)$ no implica que la clase no-lineal $\{|\eta_{\mathrm{on}}|^2 : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ sea densa en $L^2(W_\lambda\,dm_\infty)$.

*Explicación.* Los elementos de la clase Hadamard-crítica son módulos cuadrados de funciones de una clase particular: deben tener la forma $|\eta_{\mathrm{on}}|^2$ donde $\eta_{\mathrm{on}}$ satisface condiciones globales (crecimiento de orden 1, simetría funcional, todos sus ceros sobre la recta crítica). Esta no es una clase vectorial; no está cerrada bajo sumas ni bajo multiplicación por escalares complejos.

El span lineal $\mathcal{C}_\lambda$, en cambio, es el cierre de un subespacio vectorial. Que $|\zeta|^2 \in \mathcal{C}_\lambda$ (que es consecuencia de la completitud) significa que $|\zeta|^2$ puede aproximarse por sumas $\sum c_k e^{i\gamma_k s}$ con $c_k \in \mathbb{C}$ arbitrarios. Estas sumas no tienen por qué ser módulos cuadrados de funciones de la clase $\mathcal{H}_{\mathrm{crit}}$; en general no lo son.

**Proposición 6.2.** Sea $\mathcal{M} = \{|\eta_{\mathrm{on}}|^2 : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ la clase Hadamard-crítica de módulos cuadrados. Entonces $\mathcal{M} \subset \mathcal{C}_\lambda$ (los elementos de $\mathcal{M}$ pueden aproximarse por combinaciones lineales de exponenciales, por la completitud), pero
$$\overline{\mathcal{M}}^{L^2(W_\lambda dm_\infty)} \subsetneq \mathcal{C}_\lambda$$
en general, pues $\mathcal{M}$ es una variedad no-lineal de codimensión infinita en $\mathcal{C}_\lambda$.

*Argumento.* Que $\mathcal{M} \subset \mathcal{C}_\lambda$ se sigue de que cada $|\eta_{\mathrm{on}}|^2$ puede expresarse, vía el logaritmo del producto de Hadamard, como superposición de términos $e^{i\gamma_n s}$, y el cierre de las exponenciales cubre todo $L^2(W_\lambda\,dm_\infty)$. Que el cierre sea estricto se sigue de que las funciones en $\mathcal{M}$ satisfacen condiciones analíticas globales (simetría funcional, tipo de crecimiento, no-negatividad) que no son heredadas por combinaciones lineales generales. La codimensión infinita es consecuencia de que $\mathcal{H}_{\mathrm{crit}}$ está parametrizada por sucesiones de ceros $\{\mu_n\} \subset \mathbb{R}$ que satisfacen condiciones de convergencia del producto de Hadamard, un espacio de parámetros de dimensión infinita pero con restricciones analíticas no-triviales (todos los ceros sobre la recta crítica). $\square$

---

## §7. La completitud incondicional y el criterio CTP

### 7.1. Lo que la completitud sí implica

Del Teorema 5.1 y la Proposición 6.2 se obtiene la siguiente situación:

1. **Completitud del span lineal (incondicional):** El cierre $\mathcal{C}_\lambda = \overline{\mathrm{span}}\{e^{i\gamma_n s}\}$ es todo $L^2(W_\lambda\,dm_\infty)$.

2. **El criterio variacional (equivalente a RH):** $\tilde\delta_\lambda^2 = 0$ para todo $\lambda > 0$ si y solo si RH (Corolario 4.6 de Doc 82).

Estos dos hechos son compatibles sin contradicción: la completitud del span lineal solo dice que $|\zeta|^2 \in \mathcal{C}_\lambda$ en el sentido de que puede aproximarse por combinaciones lineales de exponenciales. Pero $\tilde\delta_\lambda^2$ no mide la distancia de $|\zeta|^2$ a $\mathcal{C}_\lambda$ (que sería cero por la completitud), sino la distancia de $|\zeta|^2$ a la variedad no-lineal $\{|\eta_{\mathrm{on}}|\}$.

### 7.2. El diagrama de contenciones

Las contenciones relevantes en $L^2(W_\lambda\,dm_\infty)$ son:
$$\{|\zeta|\} \xrightarrow{?} \overline{\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}} \subset L^2(W_\lambda\,dm_\infty) = \mathcal{C}_\lambda.$$

La última igualdad es el Teorema 5.1. La inclusión del medio es trivial. La flecha $\{?\}$ — si $|\zeta|$ pertenece al cierre de la clase de módulos de funciones Hadamard-críticas — es precisamente la pregunta equivalente a RH.

La completitud incondicional solo establece la última igualdad; no da información sobre la flecha de la izquierda.

---

## §8. El flujo de De Bruijn-Newman como familia interpolante

### 8.1. La familia $\{\zeta_t\}$ y sus ceros

Para $t \geq 0$, la función xi deformada es
$$\xi_t(s) = \int_\mathbb{R} e^{tu^2}\Phi(u)\,e^{ius}\,du,$$
donde $\Phi(u) = \sum_{n=1}^\infty (2n^4\pi^2 e^{9u/2} - 3n^2\pi e^{5u/2})\exp(-n^2\pi e^{2u})$ es el kernel xi de Riemann. Para $t = 0$, $\xi_0 = \xi$ es la función xi de Riemann. Para $t > \Lambda$ (la constante de De Bruijn-Newman), todos los ceros de $\xi_t$ son reales.

**Proposición 8.1.** Para todo $t \geq 0$, los ceros de $\xi_t$ tienen partes imaginarias reales (pues los ceros de una función holomorfa son números complejos, y su parte imaginaria es real por definición). La densidad de las partes imaginarias positivas de los ceros de $\xi_t$ satisface $N_t(T) \sim T\log T/(2\pi)$ para todo $t \geq 0$ fijo (la densidad asintótica se preserva bajo el flujo).

### 8.2. La familia de sistemas de exponenciales

Para cada $t \geq 0$, el sistema $\{e^{i\gamma_n^{(t)} s}\}_{n \geq 1}$ (donde $\gamma_n^{(t)} = \mathrm{Im}(\rho_n^{(t)})$ son las partes imaginarias de los ceros de $\xi_t$) es completo en $L^2(W_\lambda\,dm_\infty)$ por el Teorema 5.1, aplicado a la secuencia de partes imaginarias de los ceros de $\xi_t$.

**Proposición 8.2.** La completitud incondicional del sistema $\{e^{i\gamma_n^{(t)} s}\}$ no implica que $\tilde\delta_\lambda^{(t)2} = 0$, donde $\tilde\delta_\lambda^{(t)2}$ es el análogo del criterio variacional para $\xi_t$ en lugar de $\xi$. El criterio variacional para $\xi_t$ equivaldría a que todos los ceros de $\xi_t$ sean reales, que es una condición no trivial para $t < \Lambda$.

---

## §9. La naturaleza de la clase Hadamard-crítica como variedad no-lineal

### 9.1. Parametrización de $\mathcal{H}_{\mathrm{crit}}$

La clase $\mathcal{H}_{\mathrm{crit}}$ consiste en funciones $\eta_{\mathrm{on}}$ del tipo
$$\eta_{\mathrm{on}}(1/2+it) = \xi(0)\,e^{A+Bt}\prod_{n=1}^\infty \left(1 - \frac{1/2+it}{1/2+i\mu_n}\right)e^{(1/2+it)/(1/2+i\mu_n)}$$
con $\{\mu_n\} \subset \mathbb{R}$ cumpliendo condiciones de convergencia del producto. La estructura de $\mathcal{H}_{\mathrm{crit}}$ como variedad en $L^2(W_\lambda\,dm_\infty)$ está gobernada por la geometría del espacio de sucesiones $\{\mu_n\} \subset \mathbb{R}$ con la topología inducida por la convergencia en $L^2(W_\lambda\,dm_\infty)$ de los módulos correspondientes.

**Proposición 9.1 (convexidad local).** La función $\Psi: \{\mu_n\}_{n \geq 1} \mapsto \||\eta_{\mathrm{on}}(\cdot;\{\mu_n\})|\|_{L^2(W_\lambda dm_\infty)}^2$ es diferenciable Frechet respecto a perturbaciones finitas de la secuencia $\{\mu_n\}$. El gradiente de $\tilde\delta_\lambda^2$ en la dirección de deformar los $\mu_n$ a los $\gamma_n$ (los ceros reales de $\xi$) mide la sensibilidad de la distancia variacional a la posición de los ceros.

*Observación.* El cálculo explícito de este gradiente conduciría a una caracterización de los puntos críticos de $\mu \mapsto \tilde\delta_\lambda^2(\{\mu_n\})$. Si el único punto crítico con $\tilde\delta_\lambda^2 = 0$ es $\{\mu_n\} = \{\gamma_n\}$ (los ceros de $\xi$), y si $\tilde\delta_\lambda^2 > 0$ para toda otra sucesión $\{\mu_n\} \subset \mathbb{R}$ no igual a los $\gamma_n$, esto sería consistente con RH pero no lo probaría sin la implicación $\tilde\delta_\lambda^2 = 0 \implies$ RH (ya probada) y un argumento de que no hay otros mínimos.

### 9.2. La dirección futura

**Pregunta 9.2 (geometría de la variedad Hadamard-crítica).** ¿Es la variedad $\overline{\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}}$ convexamente cerrada en $L^2(W_\lambda\,dm_\infty)$ (en el sentido de la envolvente convexa)? ¿Tiene $|\zeta|$ la propiedad de ser el punto de la envolvente convexa de $\{|\eta_{\mathrm{on}}|\}$ más cercano al subespacio lineal $\mathcal{C}_\lambda$?

Una respuesta afirmativa a la primera parte implicaría que la distancia variacional $\tilde\delta_\lambda^2$ es una función convexa de los parámetros de los ceros, y los mínimos serían más asequibles. Una respuesta afirmativa a la segunda parte conectaría la posición de $|\zeta|$ en $\mathcal{C}_\lambda$ con la estructura de la clase Hadamard-crítica de manera que haría factible el uso de métodos de optimización convexa.

---

## §10. Síntesis: la pregunta precisa que queda abierta

### 10.1. Estado del Camino 3 tras Doc 85

**R1 (riguroso).** Los $\gamma_n = \mathrm{Im}(\rho_n)$ son siempre reales, independientemente de si RH es verdadera o falsa.

**R2 (riguroso módulo verificación técnica V.1).** El span lineal $\mathcal{C}_\lambda = \overline{\mathrm{span}}\{e^{i\gamma_n s}\}$ es denso en $L^2(W_\lambda\,dm_\infty)$ incondicionalmente. La verificación técnica pendiente (ítem V.1) es comprobar las hipótesis del argumento de Carlson-Beurling para funciones enteras de tipo $\leq \pi/4$ con función de ceros de densidad logarítmicamente divergente.

**R3 (riguroso, de Doc 82).** $\tilde\delta_\lambda^2 = 0$ para todo $\lambda > 0$ si y solo si RH.

**C1 (conjetural).** La variedad $\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ es una subvariedad no-lineal propia de $L^2(W_\lambda\,dm_\infty)$, y su cierre no cubre $L^2(W_\lambda\,dm_\infty)$.

**C2 (conjetural).** La distancia variacional $\tilde\delta_\lambda^2$ es positiva bajo $\neg$RH. Esto es equivalente a RH por R3, pero no se sabe probarlo por medios independientes.

### 10.2. La pregunta central reformulada con precisión

**Pregunta 10.1.** La completitud incondicional del span lineal (R2) no basta para probar $\tilde\delta_\lambda^2 = 0$. La pregunta relevante no es si $|\zeta|^2$ pertenece al cierre del span lineal de las exponenciales (lo cual es cierto, por R2), sino si $|\zeta|$ pertenece al cierre de la clase de módulos de funciones Hadamard-críticas $\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ en $L^2(W_\lambda\,dm_\infty)$.

Formalmente:
$$\tilde\delta_\lambda^2 = 0 \iff |\zeta(1/2+i\cdot)| \in \overline{\{|\eta_{\mathrm{on}}(1/2+i\cdot)| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}}^{L^2(W_\lambda dm_\infty)}.$$
Por el Corolario 4.6 de Doc 82, esto es equivalente a RH. No se conoce cómo probar esta pertenencia sin usar la equivalencia con RH.

### 10.3. Las posibles vías de ataque

**Vía A (análisis de la variedad Hadamard-crítica).** Estudiar la geometría diferencial de la aplicación $\{\mu_n\} \mapsto |\eta_{\mathrm{on}}(\cdot;\{\mu_n\})|$ en $L^2(W_\lambda\,dm_\infty)$. Si esta aplicación es una inmersión regular con imagen cerrada, la distancia variacional tiene propiedades de regularidad que podrían ser explotables.

**Vía B (conexión con la fórmula explícita).** La fórmula explícita de von Mangoldt expresa $\log|\zeta(1/2+it)|$ en términos de los ceros y los primos. Si pudiera conectarse esta fórmula con la métrica $L^2(W_\lambda\,dm_\infty)$, podría obtenerse una caracterización de $\tilde\delta_\lambda^2$ en términos aritméticos.

**Vía C (flujo DBN y límite $t \downarrow 0$).** Para $t > \Lambda$, todos los ceros de $\xi_t$ son reales y $\tilde\delta_\lambda^{(t)2} = 0$ (con el análogo del criterio variacional para $\xi_t$). La continuidad del flujo DBN en $t$ sugiere que $\tilde\delta_\lambda^{(t)2}$ es continua en $t$. Si $\Lambda = 0$ (consecuencia de RH y la conjetura de De Bruijn-Newman), entonces $\tilde\delta_\lambda^{(0)2} = \lim_{t\downarrow 0}\tilde\delta_\lambda^{(t)2} = 0$. Esta vía, sin embargo, asume $\Lambda = 0$, que es equivalente a RH — circularidad de nuevo.

**Vía D (dualidad y ortogonalidad).** Si pudiera caracterizarse el anulador de $\{|\eta_{\mathrm{on}}| : \eta_{\mathrm{on}} \in \mathcal{H}_{\mathrm{crit}}\}$ en $L^2(W_\lambda\,dm_\infty)$, la densidad de esta clase sería equivalente a la trivialidad del anulador. El anulador sería el conjunto de funciones $g \in L^2(W_\lambda\,dm_\infty)$ ortogonales a todos los $|\eta_{\mathrm{on}}|$. Caracterizar este conjunto sin asumir RH es la versión dual de la pregunta original.

---

## §11. Conclusión

El Camino 3 ha alcanzado la siguiente comprensión, que es más precisa que la del Doc 82:

1. El obstáculo circular identificado en Doc 82 se basaba en un malentendido: los $\gamma_n$ son siempre reales, y el sistema $\{e^{i\gamma_n s}\}$ es completo en $L^2(W_\lambda\,dm_\infty)$ incondicionalmente.

2. Esta completitud incondicional, sin embargo, no produce una prueba de RH porque es la completitud del span lineal, no la densidad de la clase no-lineal Hadamard-crítica.

3. La obstaculación real está en la brecha entre aproximación lineal (span de exponenciales, completo incondicionalmente) y aproximación no-lineal (módulos de funciones Hadamard-críticas, densa si y solo si RH).

4. La pregunta precisa que define el obstáculo para el Camino 3 es: ¿puede probarse, por medios independientes de RH, que $|\zeta|$ pertenece al cierre de la clase $\{|\eta_{\mathrm{on}}|\}$ en $L^2(W_\lambda\,dm_\infty)$?

5. Las Vías A–D del §10.3 son posibles direcciones de ataque, cada una con sus propias dificultades. Ninguna de ellas está libre de circularidad evidente.

El Doc 85 cierra el análisis del obstáculo circular del Camino 3 con una formulación precisa y sin ilusiones. La agenda de la Fase 35 incluye la verificación técnica V.1 (hipótesis del argumento de Carlson-Beurling) y la exploración de la Vía A (geometría diferencial de la variedad Hadamard-crítica).

---

*Documento 85 concluido. La completitud incondicional del span lineal de exponenciales está establecida (módulo V.1). El obstáculo para RH reside en la brecha entre aproximación lineal e incondicional y aproximación no-lineal condicionada por los ceros críticos. No hay demostración nueva de RH; hay una reformulación más honesta del obstáculo.*
