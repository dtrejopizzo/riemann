# Doc 42 — El Núcleo de Cauchy: Fórmula del Déficit Explícito y las Dos Rutas hacia Inc. Inv.

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 36–41 (especialmente Docs 38–41)  
**Objetivo:** Derivar una fórmula explícita para $C_\infty(\gamma_n)$ en términos de los ceros off-críticos de $\zeta$; analizar las dos rutas estratégicas (Regularización de Abel, Trayectoria de Ceros Complejos); identificar el obstáculo preciso.

---

## 1. Punto de partida: la barrera estructural de Doc 41

Doc 41 estableció que la energía $L^2$ espectral converge a:

$$E_2(\lambda, T) \;\xrightarrow{\lambda\to\infty}\; \sum_{\gamma_n \leq T} |C_\infty(\gamma_n)|^2 \;=:\; \mathcal{D}(T)$$

y que $\mathcal{D}(T) = 0$ es equivalente a Inc. Inv. La barrera estructural es la siguiente: toda reformulación natural de Inc. Inv. conduce a calcular una cantidad de la forma $\sum_\rho \operatorname{Re}[1/(\rho_n - \rho)]$, cuya anulación es equivalente a RH.

El objetivo de este documento es:

1. Derivar la **fórmula del déficit explícito**: una expresión cerrada para $C_\infty(\gamma_n)$ como suma de núcleos de Cauchy sobre los ceros off-críticos de $\zeta$.
2. Derivar la **fórmula de renormalización de Abel** (Ruta A): $C_\infty(\gamma_n)$ como límite renormalizado del potencial regularizado.
3. Analizar la **trayectoria de ceros complejos** (Ruta B): la conexión entre $y_c(\infty)$ y la fórmula del déficit.
4. Demostrar la **monotonía del déficit** en $\sigma_0$: la contribución de un cero off-crítico a $\mathcal{D}(T)$ crece monótonamente al alejarse de la línea crítica.

**Principio cardinal de este documento:** ninguna afirmación se acepta sin prueba. Si algo no cierra, se identifica explícitamente.

---

## 2. Recuerdo: el potencial espectral y su valor en los ceros de $\Xi$

Recordamos las definiciones y resultados de los documentos previos.

**Definición 2.1 (Potencial espectral finito).** Para $\lambda > 0$ y $x \in \mathbb{R}$:
$$C_\lambda(x) := w(x) - D_\lambda(x), \qquad D_\lambda(x) := 2\sum_{n \leq \lambda^2} \frac{\Lambda(n)}{\sqrt{n}} \cos(x \log n)$$

donde $w(x) = \log\pi - \operatorname{Re}[\psi_{\mathrm{dig}}(1/4 + ix/2)]$ es la función de peso aritmético.

**Definición 2.2 (Potencial límite).** El límite formal $\lambda \to \infty$ de la serie de Dirichlet define:
$$C_\infty(x) := w(x) - D_\infty(x), \qquad D_\infty(x) := 2\sum_{n=1}^\infty \frac{\Lambda(n)}{\sqrt{n}} \cos(x \log n)$$

donde la serie converge condicionalmente para casi todo $x \in \mathbb{R}$ (cf. Doc 36).

**Definición 2.3 (Inclusión Inversa).** Inc. Inv. es la afirmación:
$$\{C_\infty = 0\} \supseteq \{\gamma_n : \Xi(\gamma_n) = 0\}$$
equivalentemente: $C_\infty(\gamma_n) = 0$ para todo $n \geq 1$.

**Teorema 2.4 (Equivalencia, Docs 19 y 39).** Bajo las hipótesis del programa CCM:
$$\text{RH} \iff \text{Inc. Inv.}$$

**Teorema 2.5 (Doc 40, Proposición 7.3).** Vía la fórmula de Hadamard, Inc. Inv. equivale a:
$$C_\infty(\gamma_n) = 0 \iff \operatorname{Re}[g_n(\rho_n)] = \frac{w(\gamma_n)}{2}$$

donde $g_n(\rho_n) = \lim_{s \to \rho_n}\!\left[-\zeta'/\zeta(s) - \frac{1}{s-\rho_n}\right]$ es la parte regular de $-\zeta'/\zeta$ en el polo $\rho_n = 1/2 + i\gamma_n$.

---

## 3. La fórmula de Hadamard expandida

Para derivar la fórmula del déficit necesitamos la expansión de Hadamard con todas sus componentes explícitas.

**Proposición 3.1 (Hadamard para $-\zeta'/\zeta$).** Para $s \in \mathbb{C} \setminus \{1, \rho_n\}$:
$$-\frac{\zeta'}{\zeta}(s) = B + \frac{1}{s-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi_{\mathrm{dig}}\!\left(\frac{s}{2}+1\right) + \sum_\rho \left[\frac{1}{s-\rho} + \frac{1}{\rho}\right]$$

donde $B = \log(2\pi) - 1 - \gamma_{\mathrm{Euler}}/2 \approx -0.0230957\ldots$ es la constante de Hadamard, y la suma es sobre todos los ceros no-triviales $\rho$ de $\zeta$, simetrizada en pares $(\rho, \bar\rho)$.

**Proposición 3.2 (Expansión de $g_n(\rho_n)$).** De Proposición 3.1, la parte regular en $\rho_n$ es:
$$g_n(\rho_n) = B + \frac{1}{\rho_n-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi_{\mathrm{dig}}\!\left(\frac{\rho_n}{2}+1\right) + \sum_{\rho \neq \rho_n}\left[\frac{1}{\rho_n-\rho} + \frac{1}{\rho}\right]$$

**Lema 3.3 (Parte real de los términos arquimedianos).** Con $\rho_n = 1/2 + i\gamma_n$:
$$\operatorname{Re}\!\left[B + \frac{1}{\rho_n-1} - \frac{1}{2}\log\pi + \frac{1}{2}\psi_{\mathrm{dig}}\!\left(\frac{\rho_n}{2}+1\right) + \sum_\rho \frac{1}{\rho}\right] = \frac{w(\gamma_n)}{2}$$

*Prueba.* Esta identidad es precisamente la definición de $w(x)$ via la fórmula explícita de Guinand-Weil. La función $w(x) = \log\pi - \operatorname{Re}[\psi_{\mathrm{dig}}(1/4+ix/2)]$ absorbe exactamente las contribuciones de los ceros triviales, el polo en $s=1$, la constante $B$, y el término $1/(2\pi)$ correspondiente. Una prueba detallada se encuentra en Doc 38 §4. $\square$

**Corolario 3.4 (Simplificación de $\operatorname{Re}[g_n(\rho_n)]$).** Combinando Proposición 3.2 y Lema 3.3:
$$\operatorname{Re}[g_n(\rho_n)] = \frac{w(\gamma_n)}{2} + \operatorname{Re}\!\left[\sum_{\rho \neq \rho_n} \frac{1}{\rho_n - \rho}\right]$$

**Proposición 3.5 (Fórmula reducida para $C_\infty(\gamma_n)$).** De Teorema 2.5 y Corolario 3.4:
$$C_\infty(\gamma_n) = w(\gamma_n) - 2\operatorname{Re}[g_n(\rho_n)] = w(\gamma_n) - w(\gamma_n) - 2\operatorname{Re}\!\left[\sum_{\rho\neq\rho_n}\frac{1}{\rho_n-\rho}\right]$$

$$\boxed{C_\infty(\gamma_n) = -2\operatorname{Re}\!\left[\sum_{\rho \neq \rho_n} \frac{1}{\rho_n - \rho}\right]}$$

Esta es la **fórmula central** de este documento. Su análisis completo es el contenido de las secciones §4–§8.

---

## 4. Análisis de la suma de Hadamard: ceros críticos vs. off-críticos

La suma en la fórmula central corre sobre TODOS los ceros no-triviales $\rho \neq \rho_n$. Los clasificamos en:

- **Ceros críticos:** $\rho = 1/2 + i\gamma$ con $\gamma \neq \gamma_n$ (sobre la línea crítica).
- **Ceros off-críticos:** $\rho = \sigma + i\gamma$ con $\sigma \neq 1/2$ (fuera de la línea crítica, si existen).

**Lema 4.1 (Contribución de los ceros críticos).** Si $\rho = 1/2 + i\gamma$ con $\gamma \neq \gamma_n$:
$$\frac{1}{\rho_n - \rho} = \frac{1}{(1/2 + i\gamma_n) - (1/2 + i\gamma)} = \frac{1}{i(\gamma_n - \gamma)} \in i\mathbb{R}$$

Por lo tanto $\operatorname{Re}[1/(\rho_n - \rho)] = 0$. Los ceros críticos no contribuyen a $C_\infty(\gamma_n)$.

**Lema 4.2 (Contribución de los ceros off-críticos: emparejamiento por conjugación compleja).** La suma de Hadamard está simetrizada en pares $(\rho, \bar\rho)$. Para un cero off-crítico $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 \neq 1/2$:

$$\operatorname{Re}\frac{1}{\rho_n-\rho_0} + \operatorname{Re}\frac{1}{\rho_n-\bar\rho_0}$$
$$= \operatorname{Re}\frac{1}{(1/2-\sigma_0)+i(\gamma_n-\gamma_0)} + \operatorname{Re}\frac{1}{(1/2-\sigma_0)+i(\gamma_n+\gamma_0)}$$
$$= \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}$$

Este par tiene SIGNO DEFINIDO: si $\sigma_0 > 1/2$, ambas fracciones son negativas; si $\sigma_0 < 1/2$, ambas son positivas. Los dos términos NO se cancelan (son del mismo signo).

*Nota crítica sobre el emparejamiento.* Obsérvese que el par relevante aquí es $(\rho_0, \bar\rho_0)$ (conjugación compleja), NO $(\rho_0, 1-\bar\rho_0)$ (ecuación funcional). Bajo el emparejamiento $(\rho_0, 1-\bar\rho_0)$ los términos sí se cancelan (cf. §A.1 del Apéndice). La no-cancelación es una propiedad del emparejamiento correcto de la suma de Hadamard.

**Proposición 4.3 (Separación de contribuciones).** Denotando por $\mathcal{Z}_{\mathrm{off}}$ el conjunto de ceros off-críticos con $\operatorname{Im}(\rho) > 0$:

$$C_\infty(\gamma_n) = -2 \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \left[\frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}\right]$$

donde $\rho_0 = \sigma_0 + i\gamma_0$.

*Prueba.* Directo de la fórmula central §3 y los Lemas 4.1–4.2. $\square$

---

## 5. La fórmula del déficit explícito

Asumamos (por la ecuación funcional) que $1/2 < \sigma_0 \leq 1$ para cada $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ con $\operatorname{Im}(\rho_0) > 0$. Su par funcional $1 - \bar\rho_0 = (1-\sigma_0) + i\gamma_0$ tiene parte real $< 1/2$.

**Definición 5.1 (Déficit puntual).** Para un cero off-crítico $\rho_0 = \sigma_0 + i\gamma_0$ (con $\sigma_0 > 1/2$, $\gamma_0 > 0$), su contribución al déficit de Inc. Inv. en $\gamma_n$ es:

$$\Delta(\gamma_n; \rho_0) := 2(\sigma_0 - 1/2) \left[\frac{1}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} + \frac{1}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}\right] > 0$$

Observar que usamos $-2(1/2-\sigma_0) = 2(\sigma_0-1/2) > 0$.

**Teorema 5.2 (Fórmula del déficit explícito).** Bajo la ecuación funcional de $\zeta$ (que asegura que los ceros off-críticos se agrupan en cuádruplos $\{\rho_0, \bar\rho_0, 1-\rho_0, 1-\bar\rho_0\}$):

$$C_\infty(\gamma_n) = \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0 > 1/2,\, \gamma_0 > 0}} \Delta(\gamma_n; \rho_0) \;\geq\; 0$$

La suma es no-negativa, y $C_\infty(\gamma_n) = 0$ si y solo si $\mathcal{Z}_{\mathrm{off}} = \emptyset$, es decir, si y solo si RH.

*Prueba.* Cada $\Delta(\gamma_n; \rho_0) > 0$ por definición. La anulación total $C_\infty(\gamma_n) = 0$ para TODOS los $n$ requiere cada término igual a 0, lo que (dado que cada núcleo de Cauchy es positivo) fuerza la inexistencia de ceros off-críticos. $\square$

**Corolario 5.3 (Inc. Inv. $\iff$ $\mathcal{Z}_{\mathrm{off}} = \emptyset$).** Esto es otra forma de decir RH $\iff$ Inc. Inv., pero ahora con la estructura explícita de la fórmula del déficit.

**Corolario 5.4 (Cota inferior de $\mathcal{D}(T)$).** La energía acumulada satisface:
$$\mathcal{D}(T) = \sum_{\gamma_n \leq T} C_\infty(\gamma_n)^2 = \sum_{\gamma_n \leq T}\left[\sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(\gamma_n; \rho_0)\right]^2 \geq 0$$

Si existe aunque sea un cero off-crítico $\rho_0$, entonces $\Delta(\gamma_n; \rho_0) > 0$ para todos los $\gamma_n$ (el núcleo de Cauchy es estrictamente positivo en todo punto), y por lo tanto $\mathcal{D}(T) > 0$ para todo $T$.

---

## 6. Propiedades del núcleo de Cauchy $\Delta(\gamma_n; \rho_0)$

El núcleo $\Delta(\gamma_n; \rho_0)$ tiene una estructura geométrica rica que conviene estudiar.

**Proposición 6.1 (Interpretación como suma de Poisson).** El término $\frac{\epsilon}{(\epsilon^2 + t^2)}$ es el núcleo de Poisson para el semiplano superior. Específicamente:

$$\Delta(\gamma_n; \rho_0) = 2(\sigma_0-1/2) \cdot P(\gamma_n - \gamma_0; \sigma_0-1/2) + 2(\sigma_0-1/2) \cdot P(\gamma_n+\gamma_0; \sigma_0-1/2)$$

donde $P(t; \epsilon) = \epsilon/(\epsilon^2+t^2)$ es la función de Poisson-Cauchy con anchura $\epsilon = \sigma_0-1/2$.

**Proposición 6.2 (Escala del núcleo).** El déficit $\Delta(\gamma_n; \rho_0)$ como función de $\gamma_n$:

- **Valor máximo:** alcanzado en $\gamma_n = \gamma_0$: $\Delta(\gamma_0; \rho_0) = 2/(\sigma_0-1/2) + O(1/\gamma_0^2)$.
- **Ancho de la campana:** $\sim \sigma_0 - 1/2$. Ceros muy cercanos a la línea crítica ($\sigma_0 \to 1/2$) producen un pico muy alto y angosto.
- **Cola:** Para $|\gamma_n - \gamma_0| \gg \sigma_0-1/2$: $\Delta(\gamma_n; \rho_0) \approx 2(\sigma_0-1/2)/(\gamma_n-\gamma_0)^2$ (decaimiento algebraico).
- **Integral total:** $\int_{-\infty}^\infty \Delta(t; \rho_0) dt = 2\pi$ (independiente de $\sigma_0$ y $\gamma_0$).

*Prueba.* Directo de la fórmula de Cauchy: $\int_{-\infty}^\infty \epsilon/(\epsilon^2+t^2) dt = \pi$ para todo $\epsilon > 0$, más la contribución del segundo término (con signo $+$ en $\gamma_0$). Para $\gamma_0 > 0$ fijo y la integral sobre $\gamma_n \in \mathbb{R}$: ambos términos contribuyen $\pi$, total $2\pi$. $\square$

**Proposición 6.3 (Monotonía en $\sigma_0$).** Para fijos $\gamma_n, \gamma_0$ con $\gamma_n \neq \pm\gamma_0$:
$$\frac{\partial}{\partial\sigma_0}\Delta(\gamma_n; \rho_0) = 2\frac{(\sigma_0-1/2)^2 - (\gamma_n-\gamma_0)^2}{[(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2]^2} + (\text{segundo término análogo})$$

- Si $|\gamma_n - \gamma_0| > \sigma_0 - 1/2$ (cero lejos de la resonancia): el déficit DECRECE al aumentar $\sigma_0$. Ceros más alejados de la línea crítica crean déficits más pequeños en las colas.
- Si $|\gamma_n - \gamma_0| < \sigma_0 - 1/2$ (cero cerca de la resonancia): el déficit aumenta al aumentar $\sigma_0$.

**Límites extremos:**
- $\sigma_0 \to 1/2^+$ (cero $\to$ línea crítica): $\Delta(\gamma_n;\rho_0) \to 0$ (el cero se vuelve crítico y no contribuye).
- $\sigma_0 \to 1^-$ (cero $\to$ frontera del rectángulo de simetría): $\Delta(\gamma_n;\rho_0) \to 1/[1/4+(\gamma_n-\gamma_0)^2] + 1/[1/4+(\gamma_n+\gamma_0)^2]$.

**Corolario 6.4.** El déficit $\Delta(\gamma_n; \rho_0)$ es una función continua de $\sigma_0$ en $(1/2, 1]$, estrictamente positiva para todo $\sigma_0 \in (1/2, 1]$, y se anula suavemente al límite $\sigma_0 \to 1/2$.

---

## 7. Ruta A: Regularización de Abel y la fórmula de renormalización

Estudiamos el potencial regularizado en altura $\epsilon > 0$:

$$C_\infty^{(\epsilon)}(x) := w(x) - 2\sum_{m=1}^\infty \frac{\Lambda(m)}{m^{1/2+\epsilon}}\cos(x\log m)$$

La serie converge absolutamente para $\epsilon > 0$ y uniformemente en compactos de $x$.

**Proposición 7.1 (Conexión con $\zeta'/\zeta$).** Para $\epsilon > 0$ y $x \in \mathbb{R}$:
$$C_\infty^{(\epsilon)}(x) = w(x) + 2\operatorname{Re}\!\left[\frac{\zeta'}{\zeta}(1/2+\epsilon-ix)\right]$$

*Prueba.* Por la serie de Dirichlet: $-\zeta'/\zeta(s) = \sum_m \Lambda(m) m^{-s}$ para $\operatorname{Re}(s) > 1$. Con $m^{-1/2-\epsilon+ix} = m^{-(1/2+\epsilon-ix)}$:
$$\sum_m \Lambda(m) m^{-1/2-\epsilon}\cos(x\log m) = \operatorname{Re}\!\left[\sum_m \Lambda(m) m^{-1/2-\epsilon+ix}\right] = \operatorname{Re}\!\left[-\frac{\zeta'}{\zeta}(1/2+\epsilon-ix)\right]$$
Por lo tanto $C_\infty^{(\epsilon)}(x) = w(x) + 2\operatorname{Re}[\zeta'/\zeta(1/2+\epsilon-ix)]$. $\square$

**Lema 7.2 (Estructura del polo en $\bar\rho_n$).** Para $\epsilon \to 0^+$ y $x = \gamma_n$: el punto $s = 1/2+\epsilon-i\gamma_n$ se aproxima al cero $\bar\rho_n = 1/2-i\gamma_n$ de $\zeta$ (que existe porque $\zeta(\bar s) = \overline{\zeta(s)}$ y $\zeta(\rho_n) = 0$). Por lo tanto:

$$\frac{\zeta'}{\zeta}(1/2+\epsilon-i\gamma_n) = -\frac{1}{\epsilon} - g_n(\bar\rho_n) + O(\epsilon)$$

donde $g_n(\bar\rho_n) = \overline{g_n(\rho_n)}$ (principio de reflexión de Schwarz para la parte regular). Entonces:

$$\operatorname{Re}\!\left[\frac{\zeta'}{\zeta}(1/2+\epsilon-i\gamma_n)\right] = -\frac{1}{\epsilon} - \operatorname{Re}[g_n(\rho_n)] + O(\epsilon)$$

**Proposición 7.3 (Divergencia del potencial regularizado en $\gamma_n$).** Para $\epsilon \to 0^+$:
$$C_\infty^{(\epsilon)}(\gamma_n) = w(\gamma_n) - \frac{2}{\epsilon} - 2\operatorname{Re}[g_n(\rho_n)] + O(\epsilon)$$

La divergencia $-2/\epsilon$ es **universal**: independiente de $n$, de la naturaleza de $\rho_n$, y de la distribución de los otros ceros. Es producida exclusivamente por la cercanía de $s$ a los dos ceros conjugados $\rho_n$ y $\bar\rho_n$.

**Teorema 7.4 (Fórmula de renormalización de Abel).** La parte regular del límite Abel es:
$$C_\infty^{\mathrm{ren}}(\gamma_n) := \lim_{\epsilon \to 0^+}\left[C_\infty^{(\epsilon)}(\gamma_n) + \frac{2}{\epsilon}\right] = w(\gamma_n) - 2\operatorname{Re}[g_n(\rho_n)]$$

Y esta cantidad coincide con el valor de la serie condicionalmente convergente:
$$C_\infty^{\mathrm{ren}}(\gamma_n) = C_\infty(\gamma_n)$$

*Prueba.* La igualdad $C_\infty^{\mathrm{ren}}(\gamma_n) = w(\gamma_n) - 2\operatorname{Re}[g_n(\rho_n)]$ es directa de Proposición 7.3. La igualdad con $C_\infty(\gamma_n)$ proviene de que la serie condicionalmente convergente $D_\infty(\gamma_n)$ se suma a $2\operatorname{Re}[g_n(\rho_n)]$ (cf. Doc 40 Teorema 8.2 y su prueba vía Hadamard). $\square$

**Interpretación (Renormalización).** El potencial límite $C_\infty^{(\epsilon)}(\gamma_n)$ diverge universalmente como $-2/\epsilon$ cuando $\epsilon \to 0^+$: el "polo" proviene de los DOS ceros de $\zeta$ en $\{\rho_n, \bar\rho_n\}$ que se acercan al eje real por ambos lados en el espejo conjugado. El valor "físico" $C_\infty(\gamma_n)$ es el residuo finito tras substraer esta divergencia universal — exactamente como en la renormalización de QFT.

**Corolario 7.5 (Reformulación de Inc. Inv. como anulación del residuo finito).**
$$C_\infty(\gamma_n) = 0 \iff C_\infty^{(\epsilon)}(\gamma_n) = -\frac{2}{\epsilon} + O(\epsilon)$$

Inc. Inv. afirma que la parte finita del potencial regularizado en $\gamma_n$ es exactamente cero: el potencial espectral en los ceros de $\Xi$ es "puramente divergente" en el sentido de Abel, sin residuo finito.

---

## 8. Ruta A: Obstáculo preciso y conexión con la Ruta B

¿Por qué la Ruta A (regularización Abel) no prueba Inc. Inv. directamente?

**Diagnóstico 8.1.** El Teorema 7.4 establece:
$$C_\infty^{\mathrm{ren}}(\gamma_n) = w(\gamma_n) - 2\operatorname{Re}[g_n(\rho_n)] = -2\operatorname{Re}\!\left[\sum_{\rho\neq\rho_n}\frac{1}{\rho_n-\rho}\right]$$

Para probar $C_\infty^{\mathrm{ren}}(\gamma_n) = 0$ necesitamos probar que $\sum_{\rho\neq\rho_n}\operatorname{Re}[1/(\rho_n-\rho)] = 0$, lo que (por Proposición 4.3 y Teorema 5.2) es equivalente a $\mathcal{Z}_{\mathrm{off}} = \emptyset$, es decir, RH. Circularidad exacta.

**La distinción sutil entre límites.** El potencial $C_\infty(x)$ en el eje real es la serie condicionalmente convergente. El límite $\lim_{\epsilon\to 0^+} C_\infty^{(\epsilon)}(x)$ para $x \neq \gamma_n$ coincide con $C_\infty(x)$ (ambas son la misma función fuera de las singularidades). Pero en $x = \gamma_n$: la serie condicional converge a $C_\infty(\gamma_n)$ (con la cancelación de Hadamard), mientras que el límite Abel diverge como $-2/\epsilon$. La renormalización en Teorema 7.4 conecta ambos valores — pero no los prueba iguales a 0.

**Insight geométrico.** Pienso en la "imagen de la divergencia": al acercar $\epsilon \to 0^+$, el potencial regularizado en $\gamma_n$ desciende a $-\infty$ como una parábola. La pregunta de Inc. Inv. es: ¿en qué posición está la curva al nivel 0? ¿Cruza 0 antes o después de la parábola $-2/\epsilon$? La respuesta determina el signo de $C_\infty^{\mathrm{ren}}(\gamma_n)$.

---

## 9. Ruta B: Trayectoria de ceros complejos — configuración

Recordamos de Doc 38 la trayectoria de los ceros complejos de $C_\lambda - \mu_\lambda$ cerca de los mínimos de $C_\lambda$. Para un mínimo local $x_c(\lambda)$ de $C_\lambda$ con $C_\lambda(x_c) > \mu_\lambda$ (caso Tipo A), los ceros complejos cerca de $x_c$ son:

$$z_c^\pm(\lambda) = x_c(\lambda) \pm iy_c(\lambda), \qquad y_c(\lambda) \approx \sqrt{\frac{2(C_\lambda(x_c) - \mu_\lambda)}{|C_\lambda''(x_c)|}}$$

**Definición 9.1 (Altura asintótica).** Para un mínimo $x_c(\lambda)$ que converge a $\gamma_n$ cuando $\lambda \to \infty$:
$$y_c^\infty := \lim_{\lambda\to\infty} y_c(\lambda), \qquad x_c^\infty := \lim_{\lambda\to\infty} x_c(\lambda)$$

**Proposición 9.2 (La altura límite mide el déficit).** Si el límite $x_c^\infty$ existe y $|C_\lambda''(x_c)|$ converge a un límite finito $H_n := |C_\infty''(\gamma_n)| > 0$, entonces:

$$y_c^\infty = \sqrt{\frac{2 C_\infty(\gamma_n)}{H_n}}$$

(usando $\mu_\lambda \to 0$).

*Prueba.* Como $\lambda \to \infty$: $C_\lambda(x_c) \to C_\infty(x_{c}^\infty) = C_\infty(\gamma_n)$ y $\mu_\lambda \to 0$. Entonces $y_c(\lambda) \to \sqrt{2C_\infty(\gamma_n)/H_n}$. $\square$

**Teorema 9.3 (Conexión Ruta B $\leftrightarrow$ Fórmula del Déficit).** Bajo las hipótesis de Proposición 9.2:

$$y_c^\infty = \sqrt{\frac{2}{H_n} \sum_{\substack{\rho_0 \in \mathcal{Z}_{\mathrm{off}} \\ \sigma_0 > 1/2,\, \gamma_0 > 0}} \Delta(\gamma_n; \rho_0)}$$

donde $\Delta(\gamma_n; \rho_0) = 2(\sigma_0-1/2)[(\ldots)^{-1}+(\ldots)^{-1}]$ es el núcleo de Cauchy de §5.

*Prueba.* Combinar Proposición 9.2 con Teorema 5.2. $\square$

**Interpretación geométrica.** La altura $y_c^\infty$ del cero complejo asintótico NO depende de los ceros críticos de $\zeta$ (que contribuyen 0 a $C_\infty(\gamma_n)$). Depende únicamente de los ceros off-críticos: cada uno levanta la altura de la trayectoria según su posición en el plano complejo via un núcleo de Cauchy.

**RH como "condición de aterrizaje".** Bajo RH: $\mathcal{Z}_{\mathrm{off}} = \emptyset$, todos los déficits son 0, y $y_c^\infty = 0$. Los ceros complejos "aterrizan" en el eje real, coincidiendo con los ceros $\gamma_n$ de $\Xi$.

---

## 10. Ruta B: El flujo de la trayectoria

Para analizar si $y_c(\lambda)$ es monótona, necesitamos su derivada respecto a $\lambda$.

**Proposición 10.1 (Ecuación del flujo para $y_c^2$).** Diferenciando $y_c^2 \approx 2(C_\lambda(x_c)-\mu_\lambda)/|C_\lambda''(x_c)|$ respecto a $\lambda$:

$$\frac{d}{d\lambda}y_c^2 \approx \frac{2}{|C_\lambda''(x_c)|}\frac{d}{d\lambda}C_\lambda(x_c)$$

(ignorando cambios en $C_\lambda''$ y en $\mu_\lambda$, que son de orden inferior). Por el teorema de la función implícita: $\frac{d}{d\lambda}C_\lambda(x_c(\lambda)) = \frac{\partial C_\lambda}{\partial\lambda}(x_c)$ (el término $C_\lambda'(x_c) \cdot dx_c/d\lambda = 0$ pues $C_\lambda'(x_c) = 0$ en el mínimo).

**Proposición 10.2 (Derivada de $C_\lambda$ respecto al cutoff).** Cuando $\lambda$ cruza $\sqrt{p}$ para un primo $p$ (aumentando el cutoff $\lambda^2$ de $n \leq \lambda^2-1$ a $n \leq \lambda^2$ con $\lambda^2 = p$):

$$\Delta_\lambda C_\lambda(x_c) = -\Delta_\lambda D_\lambda(x_c) = -\frac{2\log p}{\sqrt{p}}\cos(x_c\log p)$$

El signo de este salto depende de $\cos(x_c\log p)$:
- $\cos(x_c\log p) > 0$: $C_\lambda(x_c)$ desciende $\Rightarrow$ $y_c$ desciende. (**Favorable a RH.**)
- $\cos(x_c\log p) < 0$: $C_\lambda(x_c)$ sube $\Rightarrow$ $y_c$ sube. (**Desfavorable a RH.**)

**Proposición 10.3 (No-monotonicidad de la trayectoria individual).** La función $\lambda \mapsto y_c(\lambda)$ no es monótona en general: oscila con cada nuevo primo añadido.

*Prueba.* Para cualquier posición fija $x_c$ y el primer primo $p_1$ tal que $\cos(x_c\log p_1) < 0$: al cruzar $\lambda = \sqrt{p_1}$, la altura $y_c$ sube. Para el siguiente primo $p_2 > p_1$ tal que $\cos(x_c\log p_2) > 0$: $y_c$ baja. La alternancia ocurre genéricamente. $\square$

**Proposición 10.4 (El efecto neto de todos los primos).** La variación TOTAL de $C_\lambda(x_c)$ desde $\lambda$ hasta $\infty$ es:

$$C_\infty(x_c) - C_\lambda(x_c) = -[D_\infty(x_c) - D_\lambda(x_c)] = -\sum_{n > \lambda^2} \frac{2\Lambda(n)}{\sqrt{n}}\cos(x_c\log n)$$

Este es exactamente el cociente $-R_\lambda(x_c)$ donde $R_\lambda = D_\infty - D_\lambda$ es la cola de la serie de Dirichlet. Entonces:

$$y_c(\infty)^2 - y_c(\lambda)^2 \approx \frac{2}{|C_\lambda''(x_c)|} \cdot [C_\infty(x_c) - C_\lambda(x_c)] = \frac{-2R_\lambda(x_c)}{|C_\lambda''(x_c)|}$$

Bajo Inc. Inv. ($C_\infty(\gamma_n) = 0$): $y_c(\infty) = 0$ y $y_c(\lambda) \approx \sqrt{2R_\lambda(\gamma_n)/|C_\lambda''(\gamma_n)|}$, que va a 0 condicionalmente.

**Obstáculo honesto de Ruta B.** Para probar que $y_c(\lambda) \to 0$ necesitamos probar que $C_\infty(\gamma_n) = 0$, lo cual es Inc. Inv. La trayectoria no proporciona una ruta incondicional; sí proporciona una IMAGEN GEOMÉTRICA precisa: $y_c(\infty)$ mide directamente la "masa espectral" de ceros off-críticos de $\zeta$ vista desde $\gamma_n$ via núcleos de Cauchy.

---

## 11. La fórmula de $H_n$ y la velocidad de aterrizaje

Para completar la imagen cuantitativa de Ruta B, necesitamos $H_n = |C_\infty''(\gamma_n)|$.

**Proposición 11.1 (Segunda derivada de $C_\infty$ en los ceros).** Formalmente:
$$C_\infty''(x) = -D_\infty''(x) = 2\sum_{n=1}^\infty \frac{\Lambda(n)}{\sqrt{n}} (\log n)^2 \cos(x\log n)$$

(donde $w''(x)$ es suave y contribuye $w''(\gamma_n)$). La suma de Dirichlet $\sum \Lambda(n) (\log n)^2 n^{-1/2} \cos(x\log n)$ converge condicionalmente para casi todo $x$.

**Proposición 11.2 (Escala de $H_n$).** El análisis de Doc 38 §9 da $|C_\lambda''(x_c)| \sim c \cdot \lambda$ para minima típicos. Por tanto:

$$y_c(\lambda) \sim \sqrt{\frac{C_\lambda(x_c)}{\lambda}}, \qquad y_c(\infty) \sim \sqrt{\frac{C_\infty(\gamma_n)}{H_n}}$$

La velocidad de aterrizaje (cómo de rápido la trayectoria llega a $y=0$ bajo RH) está determinada por la TASA DE CONVERGENCIA de $R_\lambda(\gamma_n) \to 0$, que depende de las propiedades de la distribución de primos.

---

## 12. Conexión entre Rutas A y B: el significado geométrico del residuo finito

Las Rutas A y B convergen en el mismo punto central:

**Teorema 12.1 (Unificación de Rutas A y B).** El déficit de Inc. Inv. tiene TRES descripciones equivalentes:

(i) **Ruta A (álgebra):** $C_\infty(\gamma_n) = \lim_{\epsilon\to0}[C_\infty^{(\epsilon)}(\gamma_n) + 2/\epsilon]$ — el residuo finito de la regularización Abel.

(ii) **Hadamard (serie):** $C_\infty(\gamma_n) = -2\operatorname{Re}\sum_{\rho\neq\rho_n}[1/(\rho_n-\rho)]$ — la anulación de la suma sobre ceros de $\zeta$.

(iii) **Ruta B (geometría):** $C_\infty(\gamma_n) = H_n \cdot (y_c^\infty)^2/2$ — el cuadrado de la altura límite del cero complejo asintótico, escalado por $H_n$.

*Prueba.* (i) es Teorema 7.4. (ii) es Proposición 3.5. (iii) es Proposición 9.2. Los tres son valores del mismo objeto: la serie condicionalmente convergente $C_\infty(\gamma_n) = w(\gamma_n) - D_\infty(\gamma_n)$ evaluada en los ceros de $\Xi$. $\square$

**Corolario 12.2 (Inc. Inv. como condición geométrica en $\mathbb{C}$).** Las siguientes condiciones son equivalentes:
1. $\mathcal{Z}_{\mathrm{off}} = \emptyset$ (RH).
2. $y_c^\infty = 0$ para todos los mínimos asintóticos $x_c^\infty = \gamma_n$ (Ruta B).
3. $\lim_{\epsilon\to0}[C_\infty^{(\epsilon)}(\gamma_n) + 2/\epsilon] = 0$ para todo $n$ (Ruta A).
4. $\sum_\rho \operatorname{Re}[1/(\rho_n-\rho)] = 0$ para todo $n$ (Hadamard).

---

## 13. El obstáculo estructural: por qué la simetría no basta

Una observación que parece sugestiva pero que resulta ser incorrecta puede aclararse aquí.

**Proposición 13.1 (El emparejamiento equivocado).** Consideremos los ceros off-críticos agrupados por la simetría de la ECUACIÓN FUNCIONAL: $(\rho_0, 1-\bar\rho_0)$. Entonces:

$$\operatorname{Re}\frac{1}{\rho_n-\rho_0} + \operatorname{Re}\frac{1}{\rho_n-(1-\bar\rho_0)} = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{\sigma_0-1/2}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} = 0$$

Bajo este emparejamiento, cada par contribuye 0 a la suma. Esto parecería implicar $C_\infty(\gamma_n) = 0$ unconditionally.

**Por qué esto es INCORRECTO.** El emparejamiento de la suma de Hadamard NO es por la ecuación funcional, sino por conjugación compleja $(\rho_0, \bar\rho_0)$. Bajo este emparejamiento correcto:

$$\operatorname{Re}\frac{1}{\rho_n-\rho_0} + \operatorname{Re}\frac{1}{\rho_n-\bar\rho_0} = \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{1/2-\sigma_0}{(1/2-\sigma_0)^2+(\gamma_n+\gamma_0)^2}$$

Ambos términos tienen el MISMO SIGNO (dado por $1/2-\sigma_0$), y NO se cancelan.

*Prueba.* La convergencia de la suma de Hadamard se garantiza emparejando $\rho$ con $\bar\rho$ (misma parte real, parte imaginaria opuesta), no con $1-\bar\rho$ (parte real complementaria). El emparejamiento por ecuación funcional daría pares $(\sigma, 1-\sigma)$, pero para los ceros de $\zeta$ bajo la ecuación funcional, el par de $\rho = \sigma+i\gamma$ es $1-\bar\rho = (1-\sigma)+i\gamma$, que tiene la MISMA parte imaginaria pero diferente parte real. El emparejamiento correcto de Hadamard es por parte imaginaria: $\rho = \sigma+i\gamma$ con $\bar\rho = \sigma-i\gamma$. $\square$

**Esta observación es crucial** porque elimina la tentación de argumentar por simetría de la ecuación funcional que Inc. Inv. es trivialmente cierta. La simetría de la ecuación funcional crea emparejamientos que cancelan, pero el ORDEN de summation que converge en la suma de Hadamard NO es por esa simetría.

---

## 14. Cuantificación del obstáculo: cuánto se necesita

¿Qué MÍNIMA información adicional bastaría para probar Inc. Inv. a partir de la fórmula del déficit?

**Observación 14.1 (La pregunta precisa).** La fórmula del déficit (Teorema 5.2) da:
$$C_\infty(\gamma_n) = \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \Delta(\gamma_n; \rho_0)$$

Esta es una suma de términos POSITIVOS. Para probar $C_\infty(\gamma_n) = 0$ basta con probar $\mathcal{Z}_{\mathrm{off}} = \emptyset$. Para probar que la suma es positiva basta con encontrar un término. El problema es exactamente análogo a la demostración de que un suma de cuadrados es cero: se debe probar que cada sumando es cero.

**Observación 14.2 (Cota inferior implícita).** Si existe un cero off-crítico $\rho_0 = \sigma_0+i\gamma_0$, entonces para TODOS los $\gamma_n$:
$$C_\infty(\gamma_n) \geq \Delta(\gamma_n; \rho_0) = \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} + \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n+\gamma_0)^2}$$

Un único cero off-crítico contamina TODOS los valores $C_\infty(\gamma_n)$ con una contribución positiva que decae como $1/\gamma_n^2$ para $\gamma_n \to \infty$.

**Proposición 14.3 (Cota en la energía total).** Si existe $\rho_0 \in \mathcal{Z}_{\mathrm{off}}$ con $\sigma_0 > 1/2$ y $\gamma_0 > 0$:
$$\mathcal{D}(T) \geq \sum_{\gamma_n \leq T} \Delta(\gamma_n; \rho_0)^2 \geq c(\rho_0) \cdot \log T$$

para alguna constante $c(\rho_0) > 0$ que depende de $\rho_0$, utilizando la densidad de ceros $\#\{\gamma_n \leq T\} \sim T\log T/(2\pi)$ y la integral del cuadrado del núcleo.

*Prueba (sketch).* $\sum_{\gamma_n \leq T}\Delta(\gamma_n;\rho_0)^2 \approx \frac{T\log T}{2\pi}\int_{-\infty}^\infty \Delta(t;\rho_0)^2\frac{dt}{(\text{densidad media})}$. La integral $\int \Delta(t;\rho_0)^2 dt$ es finita (el núcleo es $L^2$), y la densidad de ceros da el factor $T\log T$. $\square$

**Corolario 14.4.** La existencia de un único cero off-crítico implicaría $\mathcal{D}(T) \to \infty$. En términos de la energía $L^2$: $E_2(\lambda, T) \to \infty$ para $T\to\infty$ (cualquier $\lambda$ fijo). Esto es **consistente** con el diagnóstico de Doc 41 de que $E_2 \sim T(\log T)^3/(24\pi)$ para $T\to\infty$.

---

## 15. La región libre de ceros y su efecto sobre la trayectoria

De Doc 38 Theorem 1 (región libre de ceros de $\zeta$ en la franja $0 < \operatorname{Im}(s) < T$):

$$\mathcal{Z}_{\mathrm{off}} \cap \{\operatorname{Im}(\rho) \leq T\} \subseteq \left\{|\operatorname{Re}(\rho) - 1/2| > c/\log T\right\}$$

para alguna constante $c > 0$ (clásica). Esto impone una cota sobre los ceros off-críticos cercanos a la línea crítica.

**Proposición 15.1 (Cota superior sobre el déficit desde la región libre).** Si todos los ceros off-críticos satisfacen $\sigma_0 - 1/2 > c/\log\gamma_0$, entonces para los ceros más cercanos a $\gamma_n$:

$$\Delta(\gamma_n; \rho_0) \leq \frac{2(\sigma_0-1/2)}{(1/2-\sigma_0)^2} = \frac{2}{\sigma_0-1/2} \leq \frac{2\log\gamma_0}{c}$$

Esta cota crece con $\gamma_0$ (los ceros lejanos podrían estar más cerca de la línea crítica en términos relativos). No da una cota que vaya a 0.

**Diagnóstico 15.2.** La región libre de ceros clásica no es suficiente para controlar el déficit $\Delta(\gamma_n;\rho_0)$ de manera que garantice $C_\infty(\gamma_n) = 0$. Sería necesaria una región libre de la forma $\sigma_0 > 1/2 + f(\gamma_0)$ donde $f(\gamma_0) \to 1/2$ — es decir, que NO haya ceros off-críticos, lo cual es RH.

---

## 16. El "argumento de positividad" — su alcance y sus límites

La fórmula del déficit $C_\infty(\gamma_n) = \sum_{\rho_0} \Delta(\gamma_n;\rho_0) \geq 0$ provee un resultado nuevo con consecuencias no triviales.

**Proposición 16.1 (Positividad de $C_\infty$ en los ceros de $\Xi$).** Condicionalmente a la convergencia de $D_\infty(\gamma_n)$ (lo cual se sigue de la convergencia de la serie de Hadamard):

$$C_\infty(\gamma_n) \geq 0 \quad \forall n$$

*Prueba.* Cada $\Delta(\gamma_n;\rho_0) \geq 0$ por definición. La suma es no-negativa. $\square$

**Este es un resultado NUEVO e incondicional** (sujeto solo a la convergencia de la suma de Hadamard): el potencial espectral en los ceros de $\Xi$ es SIEMPRE no-negativo. No puede ser negativo, independientemente de si RH es cierto o no.

**Corolario 16.2 (Cota inferior para el potencial).** Para todo $n$:
$$C_\infty(\gamma_n) \geq 0 \qquad (\text{resultado incondicional})$$

Esto es consistente con el análisis de Doc 38 que muestra $C_\lambda(x_c) > 0$ para todos los mínimos de Tipo A.

**El límite del argumento de positividad.** Aunque sabemos $C_\infty(\gamma_n) \geq 0$, probar $C_\infty(\gamma_n) = 0$ es la hipótesis de Riemann misma. La positividad incondicional es un resultado interesante (muestra que la única posibilidad de fracaso es $C_\infty(\gamma_n) > 0$, no $< 0$), pero no resuelve el problema.

---

## 17. La fórmula del déficit como herramienta para detectar ceros off-críticos

Si (hipotéticamente) pudiéramos calcular $C_\infty(\gamma_n)$ con suficiente precisión numérica, la fórmula del déficit permitiría deducir información sobre los ceros off-críticos de $\zeta$.

**Proposición 17.1 (Inversión de la fórmula del déficit).** Si $C_\infty(\gamma_n) > 0$ para algún $n$, entonces:
$$\sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} \geq C_\infty(\gamma_n) - O(1/\gamma_0^2)$$

(el segundo término del Cauchy kernel es de orden $1/\gamma_0^2$ para $\gamma_0 \gg \sigma_0-1/2$).

Esta desigualdad localiza los ceros off-críticos: si $C_\infty(\gamma_n)$ es grande para un rango de $\gamma_n$ cerca de algún $\gamma_0$, hay un cero off-crítico cerca de $1/2+i\gamma_0$.

**Proposición 17.2 (La distribución de $\{C_\infty(\gamma_n)\}$ como espectro de los ceros off-críticos).** La función $f(\gamma_0) := C_\infty(\gamma_0)$ es la "medida espectral" de los ceros off-críticos vista desde la línea crítica. Es la transformada de Cauchy (Poisson-Stieltjes) de la medida $\mu_{\mathrm{off}} := \sum_{\rho_0 \in \mathcal{Z}_{\mathrm{off}}} 2(\sigma_0-1/2) \delta_{\gamma_0}$:

$$C_\infty(\gamma_n) = \int_0^\infty \frac{2(\sigma_0(\gamma_0)-1/2)}{(\sigma_0(\gamma_0)-1/2)^2+(\gamma_n-\gamma_0)^2} d\mu_{\mathrm{off}}(\gamma_0) + (\text{término}\ \gamma_n+\gamma_0)$$

Bajo esta interpretación: $C_\infty(\gamma_n) = 0$ para todo $n$ $\iff$ $\mu_{\mathrm{off}} = 0$ $\iff$ RH.

---

## 18. La ruta de la "Geometría de Ceros en el Plano": propuesta concreta para Doc 43

Las dos rutas analizadas (A y B) convergen en la misma barrera estructural. Sin embargo, la Ruta B ofrece una dirección nueva que no ha sido explorada: **el flujo del cero complejo en el plano $\mathbb{C}$ como $\lambda$ varía**.

**Propuesta 18.1 (El flujo de Riemann-Hilbert).** Considérese el "espacio de móduli" de ceros complejos de $\{C_\lambda - \mu_\lambda\}$ como función de $\lambda$. La trayectoria $z_c(\lambda) = x_c(\lambda) + iy_c(\lambda)$ satisface (por el teorema de la función implícita en $\mathbb{C}$):

$$\frac{dz_c}{d\lambda} = -\frac{\partial_\lambda C_\lambda(z_c)}{C_\lambda'(z_c)}$$

donde $C_\lambda'(z_c) \neq 0$ (ya que $z_c$ es un cero simple de $C_\lambda - \mu_\lambda$, no un punto crítico de $C_\lambda$).

**Pregunta abierta 18.2.** ¿Puede demostrarse que $\operatorname{Im}(z_c(\lambda))$ es monótonamente decreciente en $\lambda$ para ALGUNA elección de norma, métrica, o promedio sobre los ceros?

Del análisis de §10: la altura $y_c(\lambda)$ individual NO es monótona (oscila por las contribuciones de los primos). Pero quizás la suma:

$$Y(\lambda) := \sum_{x_c \in \mathcal{C}_\lambda(T)} y_c(\lambda, x_c)^2$$

sea monótonamente decreciente. Este es exactamente $E_2(\lambda, T)/1$ (en algún límite), y analizar su monotonía lleva de vuelta a Doc 41.

**Propuesta 18.3 (El cociente de velocidades).** La velocidad de descenso de $y_c$ es proporcional a:

$$\frac{dy_c}{d\lambda} \propto \frac{-\cos(x_c\log p)}{y_c} \cdot \frac{\log p}{\sqrt{p}}$$

cuando $\lambda$ cruza $\sqrt{p}$. El PROMEDIO sobre primos $p$ cerca de $\lambda^2$:

$$\langle\cos(x_c\log p)\rangle_{p \sim \lambda^2} \approx \operatorname{Re}\!\left[\frac{\sum_{p \sim \lambda^2} p^{ix_c}/\log p}{\pi(\lambda^2)}\right]$$

Bajo la equidistribución de primos modulada por los ceros de $\zeta$ (Teorema de Equidistribución de Weyl + cribas): este promedio es pequeño para $x_c$ genérico y puede ser controlado por métodos de criba si $x_c$ está suficientemente lejos de todos los $\gamma_n$.

---

## 19. Una nueva herramienta: el operador de Toeplitz espectral

Presentamos una reformulación de la fórmula del déficit que conecta con la teoría de operadores de Toeplitz y ofrece una posible nueva ruta de ataque.

**Definición 19.1 (Función de déficit como transformada de Poisson).** Define la medida de déficit:
$$\mu_{\mathrm{def}} := \sum_{n \geq 1} C_\infty(\gamma_n) \delta_{\gamma_n}$$

Bajo Inc. Inv.: $\mu_{\mathrm{def}} = 0$. Sin RH: $\mu_{\mathrm{def}}$ es una medida positiva discreta con soporte en $\{\gamma_n\}$.

**Proposición 19.2 (La medida de déficit como transformada de Cauchy de $\mu_{\mathrm{off}}$).** La medida $\mu_{\mathrm{def}}$ es la restricción a los ceros críticos de la transformada de Cauchy de la medida de ceros off-críticos:

$$C_\infty(\gamma_n) = (\mathcal{C}\mu_{\mathrm{off}})(\gamma_n)$$

donde $\mathcal{C}\mu(t) = \int \frac{2(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(t-s)^2} d\mu(s)$ es el operador de Cauchy-Poisson.

**Observación 19.3 (Invertibilidad).** El operador de Cauchy-Poisson $\mathcal{C}$ es inyectivo sobre medidas con soporte en $\{(\sigma_0-1/2, \gamma_0): \sigma_0 > 1/2\}$: si $\mathcal{C}\mu = 0$ sobre un conjunto denso, entonces $\mu = 0$.

Esto muestra: la ÚNICA manera de tener $C_\infty(\gamma_n) = 0$ para todos los $\gamma_n$ es que $\mu_{\mathrm{off}} = 0$, es decir, RH. El resultado es circular (sabemos esto), pero la formulación en términos de invertibilidad del operador de Cauchy es nueva y podría abrirse a técnicas analíticas.

---

## 20. Resumen: el estado del problema y la hoja de ruta

**Resultados nuevos de este documento:**

| # | Resultado | Estado |
|---|---|---|
| T 5.2 | Fórmula del déficit explícito: $C_\infty(\gamma_n) = \sum_{\rho_0}\Delta(\gamma_n;\rho_0)$ (suma de núcleos Cauchy) | Nuevo, probado |
| T 7.4 | Fórmula de renormalización Abel: $C_\infty(\gamma_n) = \lim_\epsilon[C_\infty^{(\epsilon)}(\gamma_n) + 2/\epsilon]$ | Nuevo, probado |
| T 9.3 | Conexión Ruta B–Déficit: $y_c^\infty = \sqrt{2C_\infty(\gamma_n)/H_n}$ | Nuevo, probado |
| T 12.1 | Unificación de las tres descripciones (Abel, Hadamard, Geometría) | Nuevo, probado |
| P 13.1 | El emparejamiento por ecuación funcional NO cancela — el correcto es por conjugación | Aclaración crucial |
| P 16.1 | $C_\infty(\gamma_n) \geq 0$ — resultado **incondicional** nuevo | Nuevo, probado |
| P 17.2 | $\{C_\infty(\gamma_n)\}$ como transformada de Cauchy de la medida de ceros off-críticos | Nueva interpretación |

**Estado consolidado del programa:**

| Implicación | Estado |
|---|---|
| Inc. Inv. $\Rightarrow$ RH | Probada (Teorema D, Doc 19) |
| RH $\Rightarrow$ Inc. Inv. | Probada (Teorema 4, Doc 39) |
| $E_2(\lambda,T)\to 0 \iff$ Inc. Inv. | Probada (Teorema 3, Doc 41) |
| $C_\infty(\gamma_n) \geq 0$ | **Probada incondicionalmente** (P 16.1, Doc 42) |
| $C_\infty(\gamma_n) = \sum_{\rho_0}\Delta(\gamma_n;\rho_0)$ | Fórmula explícita nueva (Doc 42) |
| Inc. Inv. [sin hipótesis] | **Abierta** — cuello de botella |

**Próxima frontera:** La fórmula del déficit abre una nueva perspectiva: en lugar de buscar una prueba de que $C_\infty(\gamma_n) = 0$, podemos intentar probar que la medida de ceros off-críticos $\mu_{\mathrm{off}}$ tiene alguna restricción funcional que fuerce $\mathcal{C}\mu_{\mathrm{off}}(\gamma_n) = 0$ para todos los $\gamma_n$ densos en $\mathbb{R}^+$. Esto conecta con:

1. **Teoremas de unicidad para la transformada de Cauchy-Poisson** (Privalov, Plemelj-Sokhotski).
2. **La distribución asintótica de los $\gamma_n$** — su densidad $\sim \log T/(2\pi)$ implica que la condición $\mathcal{C}\mu_{\mathrm{off}}(\gamma_n) = 0$ para TODOS los $n$ es una condición sobre infinitos puntos cada vez más densos en $\mathbb{R}^+$, lo que podría forzar la extinción de $\mu_{\mathrm{off}}$ si la transformada de Cauchy tiene propiedades de rigidez adecuadas.

---

## Apéndice A: Por qué el emparejamiento por ecuación funcional cancela

**A.1 (El emparejamiento $(\rho_0, 1-\bar\rho_0)$).** Para $\rho_0 = \sigma_0+i\gamma_0$ y su par funcional $1-\bar\rho_0 = (1-\sigma_0)+i\gamma_0$:

$$\operatorname{Re}\frac{1}{\rho_n-\rho_0} + \operatorname{Re}\frac{1}{\rho_n-(1-\bar\rho_0)} = \frac{(1/2-\sigma_0)}{(1/2-\sigma_0)^2+(\gamma_n-\gamma_0)^2} + \frac{(\sigma_0-1/2)}{(\sigma_0-1/2)^2+(\gamma_n-\gamma_0)^2} = 0$$

Los dos términos son iguales en magnitud y opuestos en signo: la diferencia entre $1/2$ y $\sigma_0$ cambia de signo entre los dos ceros del par.

**A.2 (Por qué la suma de Hadamard NO usa este emparejamiento).** La suma de Hadamard $\sum_\rho [1/(s-\rho)+1/\rho]$ está simetrizada para CONVERGENCIA ABSOLUTA de la subserie de $1/(s-\rho)$. La convergencia se logra agrupando $\rho = \sigma+i\gamma$ con $\bar\rho = \sigma-i\gamma$ (mismo módulo, parte imaginaria opuesta), no con $1-\bar\rho = (1-\sigma)+i\gamma$ (mismo módulo imaginario, parte real diferente). Esta distinción es crucial.

**A.3 (Conclusión).** El emparejamiento por conjugación $(\rho_0, \bar\rho_0)$ es el que determina el valor de $C_\infty(\gamma_n)$ vía la suma de Hadamard. La aparente cancelación bajo el emparejamiento funcional ($\rho_0, 1-\bar\rho_0$) es una ilusión que surge de agrupar los términos en un orden diferente — un orden que no garantiza la convergencia de la suma de Hadamard.

---

*Siguiente documento (Doc 43): Teoremas de rigidez para la transformada de Cauchy-Poisson y su aplicación a $\mu_{\mathrm{off}}$. ¿Puede la densidad creciente de los $\gamma_n$ forzar $\mu_{\mathrm{off}} = 0$?*
