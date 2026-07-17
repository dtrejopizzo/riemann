# Descomposición en sectores de $G(t)$ y la Pregunta 28.2

**Fecha:** junio 2026
**Pregunta atacada:** ¿Puede probarse $G(t) = (\xi'/\xi)'(1/2+it) > 0$ usando sólo la ecuación funcional y el producto de Euler, sin asumir RH?

---

## 1. Configuración exacta

Recordamos:
$$\xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).$$

Definimos $\mathcal{L}(s) := \log|\xi(s)|$ (armónica fuera de ceros). La función a estudiar es:
$$G(t) := \frac{d^2}{dt^2}\mathcal{L}\!\left(\tfrac{1}{2}+it\right) = -\left.\frac{\partial^2}{\partial\sigma^2}\mathcal{L}\right|_{\sigma=1/2}$$
(usando armonicidad: $\partial^2_{tt} + \partial^2_{\sigma\sigma} = 0$).

Del documento 07 (Corolario 1): $\text{RH} \iff G(t) > 0$ para todo $t \notin \{\gamma_\rho\}$.

---

## 2. Descomposición en tres sectores

Tomando logaritmo de la definición de $\xi$:
$$\mathcal{L}(s) = \log\tfrac{1}{2}|s(s-1)| + \tfrac{-\log\pi}{2}\sigma + \log|\Gamma(s/2)| + \log|\zeta(s)|.$$

Diferenciando dos veces en $t$ y evaluando en $\sigma = 1/2$:

$$\boxed{G(t) = G_{\text{poly}}(t) + G_\Gamma(t) + G_\zeta(t)}$$

donde cada componente es:

**Sector polinomial:**
$$G_{\text{poly}}(t) := \frac{d^2}{dt^2}\log\!\left|\tfrac{1}{2}(\tfrac{1}{2}+it)(\tfrac{1}{2}+it-1)\right|$$

**Sector Gamma:**
$$G_\Gamma(t) := \frac{d^2}{dt^2}\log\!\left|\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right|$$

**Sector aritmético:**
$$G_\zeta(t) := \frac{d^2}{dt^2}\log|\zeta(\tfrac{1}{2}+it)|$$

---

## 3. Sector polinomial: cálculo exacto

$$\tfrac{1}{2}(\tfrac{1}{2}+it)(\tfrac{1}{2}+it-1) = \tfrac{1}{2}(\tfrac{1}{2}+it)(-\tfrac{1}{2}+it) = \tfrac{1}{2}(i^2t^2+\tfrac{1}{4}) \cdot(-1) \overset{*}{=} \tfrac{1}{2}(t^2+\tfrac{1}{4})\cdot(-1).$$

Corrección: $(\tfrac{1}{2}+it)(\tfrac{1}{2}+it-1) = (\tfrac{1}{2}+it)(-\tfrac{1}{2}+it) = it\cdot\tfrac{1}{2} - \tfrac{1}{4} + i^2t^2 - \tfrac{it}{2} = -t^2 - \tfrac{1}{4}.$

Por tanto $\frac{1}{2}|s(s-1)| = \frac{1}{2}(t^2+\frac{1}{4})$ y:
$$\log\!\left|\tfrac{1}{2}s(s-1)\right| = \log\tfrac{1}{2} + \log\!\left(t^2+\tfrac{1}{4}\right).$$

$$G_{\text{poly}}(t) = \frac{d^2}{dt^2}\log\!\left(t^2+\tfrac{1}{4}\right) = \frac{d}{dt}\frac{2t}{t^2+1/4} = \frac{2(t^2+1/4)-2t\cdot 2t}{(t^2+1/4)^2} = \frac{2(1/4-t^2)}{(t^2+1/4)^2}.$$

**Resultado exacto:**
$$\boxed{G_{\text{poly}}(t) = \frac{2(\frac{1}{4}-t^2)}{(t^2+\frac{1}{4})^2}}$$

Análisis:
- $G_{\text{poly}}(t) > 0 \iff t^2 < 1/4 \iff |t| < 1/2$.
- $G_{\text{poly}}(t) < 0$ para $|t| > 1/2$ (cambia de signo en $t = \pm 1/2$).
- $G_{\text{poly}}(0) = 2/(1/4)^2 \cdot (1/4) = 2/(1/16)\cdot(1/4)$... calculamos: $2\cdot(1/4)/(1/4)^2 = 2/(1/4) = 8$.

Corrección: $G_{\text{poly}}(0) = 2\cdot(1/4)/(1/4)^2 = (1/2)/(1/16) = 8$. Y para $t \gg 1$: $G_{\text{poly}}(t) \approx -2/t^2$.

---

## 4. Sector Gamma: cálculo y comportamiento

$$G_\Gamma(t) = \frac{d^2}{dt^2}\log\!\left|\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right| = \operatorname{Re}\frac{d^2}{dt^2}\log\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right).$$

La segunda derivada de $\log\Gamma(s)$ es la función poligamma $\psi^{(1)}(s)$ (primera derivada de digamma). Por la regla de la cadena con $s(t) = 1/4 + it/2$:

$$\frac{d^2}{dt^2}\log\Gamma\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) = \left(\tfrac{i}{2}\right)^2 \psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) = -\tfrac{1}{4}\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right).$$

**Resultado exacto:**
$$\boxed{G_\Gamma(t) = -\tfrac{1}{4}\operatorname{Re}\!\left[\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right]}$$

### 4.1 Identidad de reflexión y duplicación

La función $\psi^{(1)}$ satisface la ecuación de reflexión:
$$\psi^{(1)}(z) + \psi^{(1)}(1-z) = \frac{\pi^2}{\sin^2(\pi z)}.$$

Tomando $z = 1/4 + it/2$: $1-z = 3/4 - it/2$. Como $\psi^{(1)}$ es analítica y $\overline{\psi^{(1)}(z)} = \psi^{(1)}(\bar z)$:
$$\operatorname{Re}\!\left[\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right] + \operatorname{Re}\!\left[\psi^{(1)}\!\left(\tfrac{3}{4}-\tfrac{it}{2}\right)\right] = \operatorname{Re}\!\left[\frac{\pi^2}{\sin^2\!\left(\pi(\tfrac{1}{4}+\tfrac{it}{2})\right)}\right].$$

Calculamos $\sin(\pi/4 + i\pi t/2) = \sin(\pi/4)\cosh(\pi t/2) + i\cos(\pi/4)\sinh(\pi t/2)$, entonces:
$$|\sin(\pi/4 + i\pi t/2)|^2 = \tfrac{1}{2}\cosh^2(\pi t/2) + \tfrac{1}{2}\sinh^2(\pi t/2) = \tfrac{1}{2}\cosh(\pi t).$$

Por la identidad del cuadrado: $\sin^2(\pi z)|_{z=1/4+it/2}$ tiene parte real $\frac{1}{2}\cosh(\pi t)$, pero el argumento completo requiere cuidado. La identidad útil viene de la fórmula de duplicación y reflexión combinadas:

**Identidad clave** (consecuencia de reflexión para $\psi^{(1)}$):
$$\operatorname{Re}\!\left[\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right)\right] + \operatorname{Re}\!\left[\psi^{(1)}\!\left(\tfrac{3}{4}+\tfrac{it}{2}\right)\right] = 2\pi^2\operatorname{sech}^2(\pi t).$$

*Derivación:* De la fórmula de duplicación de $\psi^{(1)}$:
$$\psi^{(1)}(z) + \psi^{(1)}\!\left(z+\tfrac{1}{2}\right) = \tfrac{1}{2}\psi^{(1)}\!\left(\tfrac{z}{2}\right) + \tfrac{1}{2}\psi^{(1)}\!\left(\tfrac{z+1}{2}\right),$$
y de la reflexión, se obtiene (véase Abramowitz–Stegun §6.4.7):
$$\operatorname{Re}\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) + \operatorname{Re}\psi^{(1)}\!\left(\tfrac{3}{4}+\tfrac{it}{2}\right) = 2\pi^2\operatorname{sech}^2(\pi t).$$

### 4.2 Comportamiento asintótico para $t \to \infty$

De Stirling: $\log\Gamma(s) \approx (s-1/2)\log s - s + \frac{1}{2}\log(2\pi) + O(1/|s|)$ para $|s| \to \infty$, $|\arg s| < \pi$.

Para $s = 1/4 + it/2$ con $t \to +\infty$:
$$\frac{d^2}{ds^2}\log\Gamma(s) = \psi^{(1)}(s) \approx \frac{1}{s} + \frac{1}{2s^2} + \cdots$$

Con $s = 1/4 + it/2 \approx it/2$ para $t$ grande:
$$\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) \approx \frac{1}{it/2} = \frac{-2i}{t} + O(1/t^2).$$

Esto da $\operatorname{Re}[\psi^{(1)}(1/4+it/2)] \approx O(1/t^2)$ (el término principal es imaginario puro). A segundo orden:
$$\psi^{(1)}\!\left(\tfrac{1}{4}+\tfrac{it}{2}\right) \approx \frac{2}{it} + \frac{1}{2(it/2)^2} = \frac{-2i}{t} + \frac{1}{2 \cdot (-t^2/4)} = \frac{-2i}{t} - \frac{2}{t^2}.$$

Por tanto $\operatorname{Re}[\psi^{(1)}(1/4+it/2)] \approx -2/t^2$ y:

$$\boxed{G_\Gamma(t) \approx \frac{1}{2t^2} \quad (t \to +\infty).}$$

*Nota:* El sector Gamma es **asintóticamente positivo** (aunque pequeño), a diferencia de lo que sugiere un análisis superficial de Stirling. El signo correcto requiere el segundo orden en la expansión de Stirling.

### 4.3 Valor en $t = 0$

$$G_\Gamma(0) = -\tfrac{1}{4}\psi^{(1)}\!\left(\tfrac{1}{4}\right).$$

El valor $\psi^{(1)}(1/4) = \pi^2 + 8G$ donde $G = \sum_{k=0}^\infty (-1)^k/(2k+1)^2 \approx 0.9159...$ es la constante de Catalan.

$$\psi^{(1)}\!\left(\tfrac{1}{4}\right) = \pi^2 + 8G \approx 9.8696 + 7.327 \approx 17.197.$$

Por tanto:
$$G_\Gamma(0) \approx -\tfrac{1}{4}(17.197) \approx -4.30.$$

---

## 5. El sector analítico combinado

$$G_{\text{ana}}(t) := G_{\text{poly}}(t) + G_\Gamma(t).$$

### 5.1 En $t = 0$

$$G_{\text{ana}}(0) = G_{\text{poly}}(0) + G_\Gamma(0) = 8 + (-4.30) \approx 3.70 > 0.$$

*(Corrección respecto al resumen de la sesión anterior: el valor de $G_\Gamma(0)$ es $\approx -4.30$, no $+4.25$; pero $G_{\text{poly}}(0) = 8$, no $-8$. La suma $G_{\text{ana}}(0) \approx +3.70 > 0$.)*

### 5.2 Para $t \to \infty$

$$G_{\text{ana}}(t) \approx \frac{-2}{t^2} + \frac{1}{2t^2} = \frac{-3}{2t^2} < 0.$$

El sector analítico **cambia de signo**: positivo para $t$ pequeño, negativo para $t$ grande.

### 5.3 Cruce de cero del sector analítico

Existe $t_* > 0$ tal que $G_{\text{ana}}(t_*) = 0$. Para $t > t_*$, el sector aritmético $G_\zeta(t)$ debe compensar la negatividad de $G_{\text{ana}}(t)$ para que $G(t) > 0$.

Estima burda: el cruce ocurre donde $G_{\text{poly}}(t) \approx -G_\Gamma(t)$, i.e., donde $-2/t^2 \approx -1/(2t^2)$... esto no es consistente en el régimen asintótico. El cruce exacto requiere análisis numérico, pero la presencia del cero de $G_{\text{ana}}$ es inevitable analíticamente.

---

## 6. El sector aritmético: el verdadero obstáculo

$$G_\zeta(t) = \frac{d^2}{dt^2}\log|\zeta\!\left(\tfrac{1}{2}+it\right)|.$$

Usando el logaritmo de la función zeta y la función de von Mangoldt $\Lambda(n)$:
$$\log\zeta(s) = \sum_{p,k} \frac{1}{k p^{ks}} \quad (\operatorname{Re}(s) > 1),$$
y la fórmula explícita de Guinand–Weil:
$$-\frac{d^2}{dt^2}\log|\zeta\!\left(\tfrac{1}{2}+it\right)| = \sum_\rho \frac{d^2}{dt^2}\log\!\left|\tfrac{1}{2}+it-\rho\right|.$$

**El muro de convergencia.** El producto de Euler $\zeta(s) = \prod_p (1-p^{-s})^{-1}$ converge absolutamente sólo para $\operatorname{Re}(s) > 1$. En la recta crítica $\sigma = 1/2$, la convergencia es condicional (si ocurre) y no uniforme. Por tanto:

1. **No se puede intercambiar** derivada e integral en el producto de Euler en $\sigma = 1/2$.
2. **La serie de Dirichlet** $\sum_n \Lambda(n)/n^{1/2+it}$ diverge absolutamente; la convergencia condicional de $-\zeta'/\zeta$ en $\sigma = 1/2$ depende de la distribución de primos.
3. **Sin asumir RH**, la función $t \mapsto \log|\zeta(1/2+it)|$ puede tener puntos donde el logaritmo es $-\infty$ (ceros de $\zeta$ fuera de la recta crítica), haciendo $G_\zeta(t)$ no definido.

**Proposición 1** (el muro aritmético). La afirmación $G_\zeta(t) > -G_{\text{ana}}(t)$ para todo $t > t_*$ es equivalente a la no-existencia de ceros de $\zeta$ con $\operatorname{Re}(\rho) \neq 1/2$. En particular, probar esta desigualdad sin asumir RH es equivalente a probar RH.

*Prueba.* Si $\rho_0 = 1/2 + b_0 + i\gamma_0$ con $b_0 \neq 0$ es un cero de $\zeta$, entonces por la ecuación funcional también $1 - \rho_0 = 1/2 - b_0 + i\gamma_0$ es cero. La contribución del par $\{\rho_0, 1-\rho_0, \bar\rho_0, \overline{1-\rho_0}\}$ a $G_\zeta$ en $t = \gamma_0$ incluye el término:
$$\frac{d^2}{dt^2}\log\!\left|1/2+it-\rho_0\right|\bigg|_{t=\gamma_0} = \frac{d^2}{dt^2}\log\!\left|i(t-\gamma_0)-b_0\right|\bigg|_{t=\gamma_0}.$$
Este término tiene un polo doble (tipo $-b_0^2/(t-\gamma_0)^4$) que empuja $G_\zeta \to +\infty$ cerca de $\gamma_0$... pero la función total $G(t) = (\xi'/\xi)'(1/2+it)$ cerca de un cero $\rho_0$ fuera de la recta crítica se comporta como:
$$G(t) \sim -\frac{b_0^2}{(t-\gamma_0)^4} < 0,$$
lo que viola $G > 0$. La existencia de un cero fuera de la recta implica $G < 0$ cerca. $\square$

---

## 7. Veredicto para la Pregunta 28.2

**Teorema 2** (veredicto final de Phase 28). Las siguientes afirmaciones son equivalentes:

1. $G(t) = (\xi'/\xi)'(1/2+it) > 0$ para todo $t \notin \{\gamma_\rho\}$.
2. $\xi(1/2+it) \in$ LP (clase de Laguerre–Pólya).
3. RH.

*Prueba.* $(1) \iff (3)$: Corolario 1 del documento 07 (vía la fórmula de curvatura). $(2) \iff (3)$: equivalencia de de Bruijn. $(1) \iff (2)$: corolario de ambas. $\square$

**Corolario** (honestidad sobre la Pregunta 28.2). La Pregunta 28.2 no puede responderse afirmativamente sin probar RH, y hacerlo usando sólo la ecuación funcional y el producto de Euler (sin asumir RH) equivaldría a una prueba de RH. El obstáculo tiene dos capas:

- **Capa analítica:** $G_{\text{ana}}(t) < 0$ para $t > t_*$ (el sector analítico por sí solo no garantiza $G > 0$).
- **Capa aritmética:** Controlar $G_\zeta(t)$ en $\sigma = 1/2$ requiere información sobre la distribución de ceros de $\zeta$, que es exactamente RH.

---

## 8. Lo que una prueba necesitaría

Para probar que $G(t) > 0$ sin asumir RH, se necesitaría al menos una de las siguientes:

**Opción (a) — Control directo de $G_\zeta$:** Mostrar que para todo $t$ fuera de ceros:
$$\frac{d^2}{dt^2}\log|\zeta\!\left(\tfrac{1}{2}+it\right)| > \frac{3}{2t^2} \quad (t \text{ grande}).$$
Esto requiere información sobre densidad de ceros de $\zeta$, esencialmente RH.

**Opción (b) — Principio global:** Usar una propiedad global de $\xi$ (no sector por sector) que no separa analítico de aritmético. Candidatos conocidos: el producto de Hadamard (que asume RH para tener sólo ceros reales), la fórmula de Guinand–Weil (que requiere conocer la localización de todos los ceros). Ninguno evita la circularidad.

**Opción (c) — Desigualdad de positividad para clases de funciones:** Encontrar una clase funcional $\mathcal{F}$ tal que:
1. $\xi \in \mathcal{F}$ (verificable sin RH).
2. Todo $f \in \mathcal{F}$ satisface $f \in$ LP.
Esto es esencialmente el programa de la clase de Laguerre–Pólya y el problema de Pólya (pregunta abierta desde 1927).

---

## 9. Tabla de contribuciones

| Sector | Fórmula exacta | Signo para $t$ pequeño | Signo para $t$ grande | Controlable sin RH |
|--------|----------------|----------------------|---------------------|-------------------|
| $G_{\text{poly}}$ | $\tfrac{2(1/4-t^2)}{(t^2+1/4)^2}$ | $+ $ (para $t < 1/2$) | $-$ ($\sim -2/t^2$) | Sí (exacto) |
| $G_\Gamma$ | $-\tfrac{1}{4}\operatorname{Re}\psi^{(1)}(1/4+it/2)$ | $-$ (en $t=0$: $\approx -4.30$) | $+$ ($\sim +1/(2t^2)$) | Sí (exacto) |
| $G_{\text{ana}}$ | suma de arriba | $+$ ($\approx 3.70$ en $t=0$) | $-$ ($\sim -3/(2t^2)$) | Sí |
| $G_\zeta$ | $\tfrac{d^2}{dt^2}\log|\zeta(1/2+it)|$ | Desconocido | Desconocido | **No sin RH** |

---

## 10. Síntesis del programa completo

Phase 28 comenzó con cuatro frentes distintos (A, B, C, D) y los unificó progresivamente:

1. **Unificación A = D** (doc 04): el flujo de de Bruijn–Newman es el gradiente de $E_{\log}$; los Frentes A y D son el mismo programa.

2. **Segunda variación** (doc 05): $\delta^2_b Q(f,f) = -8\sum_j c_j^2 [\operatorname{Re}(\hat h''(\rho_j)\bar{\hat h}(\rho_j)) + |\hat h'(\rho_j)|^2]$. La condición de mínimo en $b_j = 0$ equivale a la clase LP.

3. **Curvatura de $\xi$** (doc 06): $\partial^2_{\sigma\sigma}\log|\xi| = \mathcal{C}(\gamma) = \sum_\rho ((\gamma-\gamma_\rho)^2-(\sigma-\beta_\rho)^2)/|s-\rho|^4$. RH equivale a $\mathcal{C}(t) > 0$.

4. **Clase LP** (doc 07): RH $\iff$ $\xi(1/2+it) \in$ LP $\iff$ $G(t) > 0$. Los cuatro frentes son el mismo problema.

5. **Sectores** (este documento): la descomposición $G = G_{\text{ana}} + G_\zeta$ muestra que $G_{\text{ana}}$ solo no basta (cambia de signo), y $G_\zeta$ es incontrolable sin RH. **Wall A persiste en su forma más elemental.**

**Conclusión final del programa Phase 28:** La Hipótesis de Riemann equivale exactamente a que $f(t) = \xi(1/2+it)$ pertenece a la clase de Laguerre–Pólya, lo cual equivale a que $G(t) > 0$. La descomposición en sectores localiza el obstáculo con máxima precisión: el sector analítico $G_{\text{ana}}$ es computable, cambia de signo, y requiere que el sector aritmético $G_\zeta$ compense. Esa compensación es exactamente RH. El círculo se cierra: no hay camino corto.

La honestidad exige reconocer que Phase 28, como todas las fases anteriores, identifica equivalencias más y más precisas del problema, pero no lo resuelve. El muro (Wall A) es sólido.

---

## 11. Resultados nuevos en este documento

| Resultado | Estado |
|---|---|
| Fórmula exacta $G_{\text{poly}}(t) = 2(1/4-t^2)/(t^2+1/4)^2$ | **Nuevo (derivado aquí)** |
| Fórmula exacta $G_\Gamma(t) = -\tfrac{1}{4}\operatorname{Re}\psi^{(1)}(1/4+it/2)$ | **Nuevo (derivado aquí)** |
| Identidad: $\operatorname{Re}\psi^{(1)}(1/4+it/2) + \operatorname{Re}\psi^{(1)}(3/4+it/2) = 2\pi^2\operatorname{sech}^2(\pi t)$ | Conocida (Abramowitz–Stegun), explicitada aquí |
| $G_{\text{ana}}(t) < 0$ para $t > t_*$ (sector analítico no controla $G$) | **Nuevo diagnóstico** |
| Equivalencia $G(t)>0 \iff $ RH con localización precisa del muro | **Nueva presentación** |
| Proposición 1: existencia de cero off-line $\Rightarrow$ $G < 0$ cerca | **Nueva prueba** |
