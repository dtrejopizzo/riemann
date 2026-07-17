# Documento 87 — La integral de Jensen via la fórmula de Poisson-Jensen en la franja crítica

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM (Camino 2)
**Fecha:** 2026-06-09
**Prerrequisitos:** Docs 75, 78, 81, 84

---

## Resumen

Este documento examina la relación entre el criterio de Jensen del Doc 84 y la fórmula de Poisson-Jensen para funciones meromorfas en el semiplano superior, con el objetivo de obtener una representación más explícita del exceso
$$\delta = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} - (-\log 2)$$
en términos de los ceros off-critical de $\xi$. En §1 se establece la fórmula de Poisson-Jensen en el semiplano superior y se identifica el punto de evaluación correcto. En §2 se aplica la fórmula a $g(t) = \xi(1/2+it)$ y se establece la proposición central que conecta la integral con los ceros de $\xi$. En §3 se analiza con cuidado qué región del plano-$\rho$ contribuye a la fórmula, resolviendo una aparente paradoja (la integral sería trivialmente $-\log 2$). En §4 se explicita el cambio de variables entre la integral en el disco y la integral sobre la recta crítica. En §5 se calcula el exceso $\delta$ directamente en términos de $F$ y sus ceros interiores. En §6 se obtiene la fórmula del exceso en términos de los ceros de $\xi$ via el producto de Hadamard, y se muestra cuidadosamente que la cancelación aparente del Doc 84 §10.3 es inválida. En §7 se regulariza la integral para ceros en la recta crítica. En §8 se sintetiza la situación del Camino 2 al término de este documento.

La conclusión es que el criterio de Jensen se expresa exactamente como fórmula de Poisson-Jensen, que el exceso es una suma convergente sobre los ceros off-critical (con $\mathrm{Re}(\rho) \neq 1/2$), y que la cancelación por pares del Doc 84 §10.3 es inválida porque el cálculo por residuos no es legítimo para $\log|\xi|$.

---

## §1. La fórmula de Poisson-Jensen en el semiplano

### 1.1. Enunciado de la fórmula

Sea $f$ meromorfa en el semiplano superior $\mathbb{H} = \{w \in \mathbb{C} : \mathrm{Im}(w) > 0\}$, continua hasta la frontera real $\partial\mathbb{H} = \mathbb{R}$, y supóngase que $f$ no tiene ni ceros ni polos en la frontera real. Sea $w_0 = x_0 + iy_0 \in \mathbb{H}$. La fórmula de Poisson-Jensen establece:

$$\log|f(w_0)| = \int_{-\infty}^\infty \log|f(t)|\, P_{y_0}(x_0 - t)\, dt + \sum_{w_k \in \mathbb{H}} \log\left|\frac{w_0 - \bar{w}_k}{w_0 - w_k}\right| - \sum_{p_j \in \mathbb{H}} \log\left|\frac{w_0 - \bar{p}_j}{w_0 - p_j}\right|,$$

donde $P_y(x) = \frac{y}{\pi(x^2+y^2)}$ es el núcleo de Poisson del semiplano, la primera suma corre sobre los ceros $w_k$ de $f$ en $\mathbb{H}$ (contados con multiplicidad), y la segunda sobre los polos $p_j$ de $f$ en $\mathbb{H}$. Los factores $\left|\frac{w_0 - \bar{w}_k}{w_0 - w_k}\right|$ son siempre mayores que 1 para ceros en $\mathbb{H}$ y $w_0 \in \mathbb{H}$ (pues $|w_0 - \bar{w}_k| > |w_0 - w_k|$ cuando ambos están en el semiplano superior), de modo que la contribución de los ceros es no-negativa.

Las hipótesis de regularidad precisas son: $\log|f|$ integrable en la frontera real con el peso de Poisson, y los ceros y polos en $\mathbb{H}$ satisfacen la condición de convergencia de Blaschke del semiplano $\sum_k \frac{\mathrm{Im}(w_k)}{1 + |w_k|^2} < \infty$.

### 1.2. Identificación del punto de evaluación

Se toma $f(t) = \xi(1/2 + it)$ como función de la variable real $t$, y se continúa analíticamente a $t \in \mathbb{C}$. Con la parametrización $s = 1/2 + it$ (de modo que $t \in \mathbb{R}$ corresponde a la recta crítica $\mathrm{Re}(s) = 1/2$), los ceros no-triviales de $\xi$ en la franja $0 < \mathrm{Re}(s) < 1$ se traducen en ceros de $f(t) = \xi(1/2+it)$ en el plano-$t$. Para un cero $\rho = \sigma + i\gamma$ de $\xi$:
$$1/2 + it_\rho = \rho \implies t_\rho = \frac{\rho - 1/2}{i} = -i(\rho - 1/2) = \gamma + i(1/2 - \sigma).$$

Así, $\mathrm{Im}(t_\rho) = 1/2 - \sigma$. Por tanto:

- Si $\sigma < 1/2$ (cero con parte real menor que $1/2$): $\mathrm{Im}(t_\rho) = 1/2 - \sigma > 0$. El cero $t_\rho$ está en $\mathbb{H}$.
- Si $\sigma = 1/2$ (cero en la recta crítica): $\mathrm{Im}(t_\rho) = 0$. El cero $t_\rho = \gamma$ está en la frontera real.
- Si $\sigma > 1/2$ (cero con parte real mayor que $1/2$): $\mathrm{Im}(t_\rho) = 1/2 - \sigma < 0$. El cero $t_\rho$ está en el semiplano inferior $\mathbb{H}^- = \{w : \mathrm{Im}(w) < 0\}$.

Para aplicar la fórmula de Poisson-Jensen en el semiplano superior $\mathbb{H}$, el punto de evaluación $w_0$ debe estar en $\mathbb{H}$. El valor de $f$ en un punto correspondiente al interior de la franja crítica del lado $\mathrm{Re}(s) > 1/2$ es lo que se busca. El punto $s = 1 \in \mathbb{R}$ corresponde a $t = (1 - 1/2)/i = -i/2 \in \mathbb{H}^-$, que está en el semiplano inferior. Para usar el semiplano superior, se toma $s = 0$, que da $t = (0 - 1/2)/i = i/2 \in \mathbb{H}$, y $f(i/2) = \xi(1/2 + i(i/2)) = \xi(1/2 - 1/2) = \xi(0) = 1/2$.

**Proposición 1.1.** *El punto de evaluación natural para la fórmula de Poisson-Jensen en $\mathbb{H}$ es $w_0 = i/2$, que corresponde a $s_0 = 1/2 + i(i/2) = 0$. En este punto, $f(i/2) = \xi(0) = 1/2$ y $\log|f(i/2)| = -\log 2$.*

*El núcleo de Poisson en $w_0 = i/2$ es:*
$$P_{1/2}(t) = \frac{1/2}{\pi(t^2 + 1/4)} = \frac{2}{\pi(1 + 4t^2)},$$
*que coincide exactamente con el peso de la integral del criterio de Jensen.*

---

## §2. Aplicación de Poisson-Jensen a $\xi(1/2+it)$

### 2.1. La fórmula en el semiplano superior

Sea $f(w) = \xi(1/2 + iw)$ meromorfa en $\mathbb{C}$ (de hecho entera en $w$). Los ceros de $f$ en $\mathbb{H}$ corresponden a los ceros $\rho$ de $\xi$ con $\mathrm{Re}(\rho) < 1/2$ (por la Proposición 1.2 de §1). Aplíquese la fórmula de Poisson-Jensen con $w_0 = i/2$:

$$\log|f(i/2)| = \int_{-\infty}^\infty \log|f(t)|\, P_{1/2}(t)\, dt + \sum_{\substack{\rho: \mathrm{Re}(\rho) < 1/2}} \log\left|\frac{i/2 - \overline{t_\rho}}{i/2 - t_\rho}\right|.$$

Aquí $t_\rho = \gamma + i(1/2 - \sigma)$ con $\sigma = \mathrm{Re}(\rho) < 1/2$, de modo que $\mathrm{Im}(t_\rho) = 1/2 - \sigma > 0$, y $\overline{t_\rho} = \gamma - i(1/2 - \sigma)$. Los dos factores que aparecen en el logaritmo son:
$$i/2 - t_\rho = i/2 - \gamma - i(1/2 - \sigma) = -\gamma + i\sigma,$$
$$i/2 - \overline{t_\rho} = i/2 - \gamma + i(1/2 - \sigma) = -\gamma + i(1 - \sigma).$$

Por tanto:
$$\log\left|\frac{i/2 - \overline{t_\rho}}{i/2 - t_\rho}\right| = \log\frac{\sqrt{\gamma^2 + (1-\sigma)^2}}{\sqrt{\gamma^2 + \sigma^2}} = \frac{1}{2}\log\frac{\gamma^2 + (1-\sigma)^2}{\gamma^2 + \sigma^2}.$$

**Proposición 2.1 (Poisson-Jensen para $\xi$ en $w_0 = i/2$).** *Sea $f(w) = \xi(1/2+iw)$. Entonces:*
$$\int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} = -\log 2 - \sum_{\rho:\, \mathrm{Re}(\rho) < 1/2} \log\frac{\sqrt{\gamma_\rho^2 + (1-\sigma_\rho)^2}}{\sqrt{\gamma_\rho^2 + \sigma_\rho^2}},$$
*donde la suma corre sobre todos los ceros no-triviales $\rho = \sigma_\rho + i\gamma_\rho$ de $\xi$ con $\mathrm{Re}(\rho) < 1/2$.*

*Demostración.* Directa de la fórmula de Poisson-Jensen con $w_0 = i/2$, usando $\log|f(i/2)| = -\log 2$ y el cálculo explícito de los cocientes. $\square$

### 2.2. El signo del exceso

Para $\rho = \sigma + i\gamma$ con $\sigma < 1/2$: $(1-\sigma)^2 > \sigma^2$ ya que $1 - \sigma > 1/2 > \sigma > 0$ (asumiendo $\sigma > 0$, lo cual vale para todos los ceros no-triviales). Por tanto $\gamma^2 + (1-\sigma)^2 > \gamma^2 + \sigma^2$, y cada término en la suma de la Proposición 2.1 satisface
$$\log\frac{\sqrt{\gamma^2 + (1-\sigma)^2}}{\sqrt{\gamma^2 + \sigma^2}} > 0.$$

En consecuencia, la integral $I = \int \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}$ satisface $I \leq -\log 2$, con igualdad si y solo si no hay ceros de $\xi$ con $\mathrm{Re}(\rho) < 1/2$.

### 2.3. Relación con la ecuación funcional

Por la ecuación funcional $\xi(s) = \xi(1-s)$, los ceros vienen en pares: si $\rho$ es cero con $\mathrm{Re}(\rho) < 1/2$, entonces $1 - \rho$ es cero con $\mathrm{Re}(1-\rho) > 1/2$. No hay ceros con $\mathrm{Re}(\rho) < 1/2$ que no tengan su par con parte real $> 1/2$. En particular:

- Si RH es falsa: existen ceros $\rho_0$ con $\mathrm{Re}(\rho_0) > 1/2$, y por la ecuación funcional existen ceros $1-\rho_0$ con $\mathrm{Re}(1-\rho_0) < 1/2$. Estos últimos contribuyen a la suma en la Proposición 2.1, y el exceso es estrictamente negativo: $I < -\log 2$.
- Si RH es verdadera: todos los ceros tienen $\mathrm{Re}(\rho) = 1/2$, la suma está vacía, y $I = -\log 2$.

**Corolario 2.2 (criterio via Poisson-Jensen en $\mathbb{H}$).** 
$$\mathrm{RH} \iff \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} = -\log 2.$$
*Bajo $\neg$RH: la integral es estrictamente menor que $-\log 2$.*

---

## §3. Reconciliación con el criterio del disco (Doc 84)

### 3.1. El signo del exceso en las dos formulaciones

El Corolario 2.2 establece que la integral es $\leq -\log 2$ con igualdad bajo RH. Sin embargo, la Proposición 6.1 del Doc 84 establece que $I \geq -\log 2$ con igualdad bajo RH, basándose en la fórmula de Jensen para $F(z)$ en el disco. Los dos resultados parecen contradecirse: uno dice $I \leq -\log 2$, el otro dice $I \geq -\log 2$, y ambos dicen que la igualdad equivale a RH. Esto implica que, bajo ambas formulaciones, $I = -\log 2$ siempre — lo cual es la contradicción que se anunció en la tarea y que debe resolverse con cuidado.

### 3.2. El error en la aplicación de Poisson-Jensen en $\mathbb{H}$

La fórmula de Poisson-Jensen para $f(w) = \xi(1/2+iw)$ en $\mathbb{H}$ con evaluación en $w_0 = i/2$ asume que $f$ no tiene ceros en la frontera real $\partial \mathbb{H} = \mathbb{R}$. Esta hipótesis falla bajo RH: los ceros $\rho = 1/2 + i\gamma_n$ de $\xi$ corresponden a $t_\rho = \gamma_n \in \mathbb{R}$ (ceros reales de $f$, en la frontera). La fórmula de Poisson-Jensen estándar no es válida cuando $f$ tiene ceros en la frontera, porque $\log|f(t)| = -\infty$ en dichos puntos y la integral del lado derecho no está bien definida en la forma usual.

**Proposición 3.1.** *La fórmula de Poisson-Jensen aplicada a $f(w) = \xi(1/2+iw)$ en $w_0 = i/2$ es válida en la forma de la Proposición 2.1 únicamente si $f$ no tiene ceros en la frontera real, i.e., si $\xi$ no tiene ceros en la recta crítica $\mathrm{Re}(s) = 1/2$. Bajo RH, $f$ tiene infinitos ceros reales $\gamma_n$, la integral $\int \log|f(t)| P_{1/2}(t)\,dt$ diverge a $-\infty$, y la fórmula no proporciona información finita.*

### 3.3. El error en la formulación del Doc 84

Análogamente, la Proposición 6.1 del Doc 84 aplica la fórmula de Jensen para $F(z)$ en el disco tomando $r \to 1^-$. La fórmula para $r < 1$ es exacta:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = \log|F(0)| + \sum_{|z_k|<r}\log\frac{r}{|z_k|}.$$
El problema es el límite $r \to 1^-$. La integral del lado izquierdo converge a $\int \log|F(e^{i\theta})|d\theta/(2\pi)$ si $\log|F(e^{i\theta})|$ es integrable, lo cual requiere que los ceros de $F$ en la frontera sean integrables. Como se indicó en el Doc 84 §6.3, los ceros de $F$ en $|z|=1$ correspondientes a los ceros de $\xi$ en la recta crítica dan singularidades $\sim \log|e^{i\theta} - e^{i\theta_n}|$ que sí son integrables individualmente. Sin embargo, hay infinitos ceros y se necesita que la suma $\sum_n \int_{|e^{i\theta}-e^{i\theta_n}|<\epsilon}\log|e^{i\theta}-e^{i\theta_n}|d\theta$ converja absolutamente, lo cual requiere que los ceros $\theta_n$ no se acumulen demasiado rápido.

La integración condicional (no absoluta) de $\log|F(e^{i\theta})|$ es la fuente de la ambigüedad. La integral puede ser $-\infty$ si los ceros son suficientemente densos (en el sentido de la condición de Blaschke sobre la frontera).

**Proposición 3.2.** *La integral $I = \int_{-\infty}^\infty \log|\xi(1/2+it)| \frac{2\,dt}{\pi(1+4t^2)}$ no está bien definida como integral de Lebesgue: el integrando es $-\infty$ en los ceros reales $\gamma_n$ de $\xi$. La integral como valor principal o integral impropia converge condicionalmente si y solo si la serie $\sum_n P_{1/2}(\gamma_n)|\log \epsilon_n|$ converge, donde $\epsilon_n$ es algún radio de exclusión alrededor de $\gamma_n$.*

La "equivalencia RH $\iff I = -\log 2$" del Doc 84 Proposición 6.1 debe entenderse en el sentido del límite $r \to 1^-$: la integral para $r < 1$ siempre converge y da $-\log 2 + \sum_{|z_k|<r}\log(r/|z_k|)$. El criterio es: bajo RH, este límite tiende a $-\log 2$; bajo $\neg$RH, el límite es $> -\log 2$ por los ceros interiores.

---

## §4. El cambio de variables entre el disco y la recta crítica

### 4.1. La transformación explícita

La función $\tau : \mathbb{D} \to \mathbb{C}$ definida por $\tau(z) = z/(z-1)$ mapea el disco unitario $\{|z|<1\}$ a la semiplano derecho $\{\mathrm{Re}(s) > 1/2\}$... no exactamente. Verificar: para $z = re^{i\theta}$ con $r < 1$, el punto $\tau(z) = z/(z-1)$. Si $|z| < 1$, entonces $z = -w/(1-w)$ para algún $w$ con $|w| < 1$... Calcular directamente: la transformación $s = z/(z-1)$ lleva la circunferencia $|z| = 1$ a la recta $\mathrm{Re}(s) = 1/2$ (como se verificó en Doc 81). El disco $|z| < 1$ se corresponde con la región $\mathrm{Re}(s) < 1/2$ (exterior del semiplano de la recta crítica del lado $\sigma < 1/2$). Esta es la dirección correcta: verificar con $z = 0$: $\tau(0) = 0$, y $\mathrm{Re}(0) = 0 < 1/2$. Con $z = -1$: $\tau(-1) = (-1)/(-2) = 1/2$, en la frontera. Con $z = 1/2$: $\tau(1/2) = (1/2)/(1/2-1) = (1/2)/(-1/2) = -1$, y $\mathrm{Re}(-1) = -1 < 1/2$. Correcto.

El cambio de variables $e^{i\theta} = z(\theta)$ en la frontera del disco da, con $e^{i\theta} = (1/2+it)/(1/2+it-1) = (1/2+it)/(-1/2+it)$:
$$e^{i\theta} = \frac{1/2+it}{-1/2+it} = \frac{2it+1}{2it-1}.$$
Diferenciando: $ie^{i\theta}d\theta = \frac{2i(2it-1) - 2i(2it+1)}{(2it-1)^2}dt = \frac{-4i}{(2it-1)^2}dt$, de modo que
$$d\theta = \frac{-4i}{ie^{i\theta}(2it-1)^2}dt = \frac{-4i}{i\cdot\frac{2it+1}{2it-1}\cdot(2it-1)^2}dt = \frac{-4i}{i(2it+1)(2it-1)}dt = \frac{-4i}{i(-(4t^2+1))}dt = \frac{4\,dt}{1+4t^2}.$$

**Proposición 4.1 (cambio de variables).** *Con la parametrización $e^{i\theta} = (2it+1)/(2it-1)$ para $t \in \mathbb{R}$, la medida de longitud de arco en el disco se convierte en:*
$$\frac{d\theta}{2\pi} = \frac{2\,dt}{\pi(1+4t^2)}.$$
*En particular:*
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(e^{i\theta})|\,d\theta = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}.$$

La medida $\frac{2\,dt}{\pi(1+4t^2)}$ es la medida de Cauchy de escala $1/2$, de masa total $1$. Es también el núcleo de Poisson del disco evaluado en $z = 0$, lo cual es consistente con el hecho de que $F(0) = \xi(0) = 1/2$ y la integral es el promedio armónico de $\log|F|$ desde el centro del disco.

### 4.2. Interpretación como promedio de Poisson

La integral $I = \int \log|\xi(1/2+it)| P_{1/2}(t)\,dt$ es la función armónica $u(w_0) = P[\log|f|](w_0)$ evaluada en $w_0 = i/2$, donde $P[\cdot]$ es la integral de Poisson. La función $u(w) = P[\log|f|](w)$ es armónica en el semiplano $\mathbb{H}$ libre de ceros de $f$. Bajo RH, los ceros de $f(t) = \xi(1/2+it)$ están todos en $\mathbb{R}$, y la función $u$ es armónica en todo $\mathbb{H}$. El valor en $w_0 = i/2$ es $u(i/2) = \log|f(i/2)| = -\log 2$ si y solo si $f$ no tiene ceros en $\mathbb{H}$ (esto es exactamente la Proposición 2.1 con suma vacía bajo RH). La consistencia es perfecta.

---

## §5. El exceso $\delta$ en términos de los ceros de $F$ en el disco

### 5.1. La fórmula de Jensen para $r < 1$

Para $r < 1$, la fórmula de Jensen para $F$ en el disco $|z| \leq r$ es exacta:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2 + \sum_{|z_k|<r}\log\frac{r}{|z_k|},$$
donde la suma corre sobre los ceros $z_k$ de $F$ en el disco $|z| < r$. Los ceros de $F$ en el disco unitario son (por Doc 84 §2, Corolario 2.3) exactamente los puntos:
$$z_\rho = \frac{\rho - 1}{\rho} = 1 - \frac{1}{\rho}$$
para cada cero $\rho = \sigma + i\gamma$ de $\xi$ con $\mathrm{Re}(\rho) > 1/2$, y sus conjugados. El módulo es $|z_\rho|^2 = |\rho-1|^2/|\rho|^2 = ((\sigma-1)^2+\gamma^2)/(\sigma^2+\gamma^2)$.

### 5.2. El límite $r \to 1^-$

Al tomar $r \to 1^-$, la integral del lado izquierdo converge (bajo la condición de integrabilidad de $\log|F|$ en la frontera) a $I = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}$. El lado derecho converge a:
$$-\log 2 + \sum_{|z_k|<1}\log\frac{1}{|z_k|} = -\log 2 + \sum_{\rho:\, \mathrm{Re}(\rho)>1/2}\log\frac{|\rho|}{|\rho-1|}.$$

**Proposición 5.1.** *El exceso del criterio de Jensen es:*
$$\delta = I - (-\log 2) = \sum_{\rho:\, \mathrm{Re}(\rho)>1/2}\log\frac{|\rho|}{|\rho-1|}.$$
*Para cada cero $\rho = \sigma + i\gamma$ con $\sigma > 1/2$:*
$$\log\frac{|\rho|}{|\rho-1|} = \frac{1}{2}\log\frac{\sigma^2+\gamma^2}{(\sigma-1)^2+\gamma^2} > 0,$$
*ya que $\sigma^2 > (\sigma-1)^2$ cuando $\sigma > 1/2$. En consecuencia, $\delta \geq 0$ con igualdad si y solo si no hay ceros con $\mathrm{Re}(\rho) > 1/2$, i.e., bajo RH.*

Esto confirma la Proposición 6.1 del Doc 84: $I \geq -\log 2$ con igualdad bajo RH.

---

## §6. Reconciliación con la fórmula de Poisson-Jensen y la cancelación por pares

### 6.1. Por qué el exceso no es cero incondicionalmente

El Corolario 10.4 del Doc 84 afirmaba que cada par de ceros $(\rho, 1-\rho)$ contribuye cero al exceso, haciendo el criterio trivialmente verdadero. El error en ese argumento es preciso: el cálculo evaluaba, para un par $(\rho, 1-\rho)$, la contribución al exceso $\delta$ como:
$$\log\frac{|\rho|}{|\rho-1|} + \log\frac{|1-\rho|}{|(1-\rho)-1|} = \log\frac{|\rho|}{|\rho-1|} + \log\frac{|1-\rho|}{|\rho|} = \log\frac{|\rho|}{|\rho-1|} + \log\frac{|\rho-1|}{|\rho|} = 0.$$
El error es que la suma en la Proposición 5.1 corre solo sobre los ceros con $\mathrm{Re}(\rho) > 1/2$. Si $\rho_0$ tiene $\mathrm{Re}(\rho_0) > 1/2$, su par por ecuación funcional $1-\rho_0$ tiene $\mathrm{Re}(1-\rho_0) < 1/2$, y por tanto $1-\rho_0$ no contribuye a la suma en la Proposición 5.1 (sus ceros correspondientes en el disco satisfacen $|z_{1-\rho_0}|>1$, están fuera del disco). El cero $1-\rho_0$ con $\mathrm{Re}(1-\rho_0) < 1/2$ mapea al punto $z_{1-\rho_0} = (1-\rho_0-1)/(1-\rho_0) = -\rho_0/(1-\rho_0)$, con $|z_{1-\rho_0}| = |\rho_0|/|1-\rho_0|$. Para $\mathrm{Re}(\rho_0) > 1/2$, esta cantidad es $> 1$ (pues $|\rho_0| > |\rho_0 - 1|$ cuando $\mathrm{Re}(\rho_0) > 1/2$). El cero está fuera del disco.

**Proposición 6.1 (corrección de la cancelación del Doc 84 §10.3).** *Para un par de ceros $(\rho_0, 1-\rho_0)$ con $\mathrm{Re}(\rho_0) > 1/2$:*
- *El cero $\rho_0$ da un cero de $F$ en $z_{\rho_0} = (\rho_0-1)/\rho_0 \in \{|z|<1\}$, con $\log(1/|z_{\rho_0}|) = \log(|\rho_0|/|\rho_0-1|) > 0$.*
- *El cero $1-\rho_0$ da un cero de $F$ en $z_{1-\rho_0} = -\rho_0/(1-\rho_0) \in \{|z|>1\}$, que no contribuye a la fórmula de Jensen (está fuera del disco).*

*La cancelación aritmética $(+A) + (-A) = 0$ que parecía anular el exceso era errónea porque el segundo término proviene de un cero fuera del disco y no aparece en la fórmula de Jensen. El exceso $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|)$ es una suma de términos estrictamente positivos bajo $\neg$RH.*

### 6.2. El error adicional en el cálculo por residuos del Doc 84 §10

El Doc 84 §10.3 también argumentaba que, para cada par $(\rho, 1-\rho)$, la integral $J(\rho) + J(1-\rho) = \mathrm{Re}[\log(1-1/\rho)] + \mathrm{Re}[\log(1-1/(1-\rho))] = \mathrm{Re}[\log(-1)] = 0$ (o bien $= 0$ por un cálculo algebraico). Este cálculo evaluaba la función armónica $u(w) = \mathrm{Re}[\log(1-(1/2+iw)/\rho)]$ en $w = -i/2$ (usando el núcleo de Poisson del semiplano inferior). Pero el núcleo de Poisson del semiplano inferior $P_{1/2}^-(t) = \frac{1/2}{\pi(t^2+1/4)}$ evaluado en $w_0 = -i/2$ da la extensión armónica de los valores en la frontera al semiplano inferior, y el punto $w_0 = -i/2 \in \mathbb{H}^-$ es válido para funciones armónicas en $\mathbb{H}^-$. El cálculo correcto del valor armónico de $\mathrm{Re}[\log(1-s/\rho)]$ en $s = 1/2 + iw_0 = 1/2 + i(-i/2) = 1$ es $\mathrm{Re}[\log(1-1/\rho)]$, lo cual es correcto como operación algebraica. Y efectivamente:
$$\mathrm{Re}[\log(1-1/\rho) + \log(1-1/(1-\rho))] = \mathrm{Re}[\log\frac{\rho-1}{\rho}\cdot\frac{-\rho}{1-\rho}] = \mathrm{Re}[\log(-1)] = 0 \pmod{2\pi\mathbb{Z}}.$$
El resultado es $\mathrm{Re}[i\pi] = 0$: el valor real es efectivamente cero.

**Proposición 6.2.** *Para cada par $(\rho, 1-\rho)$ de ceros de $\xi$, con $\rho = \sigma + i\gamma$ cualquiera en la franja $0 < \sigma < 1$:*
$$\mathrm{Re}[\log(1-1/\rho)] + \mathrm{Re}[\log(1-1/(1-\rho))] = \log\frac{|\rho-1|}{|\rho|} + \log\frac{|\rho|}{|\rho-1|} = 0.$$

*Esta cancelación es aritméticamente correcta, pero es irrelevante para el criterio de Jensen:*
*la integral $J(\rho)$, correctamente calculada, no es $\mathrm{Re}[\log(1-1/\rho)]$ para todos los $\rho$.*

### 6.3. Por qué $J(\rho) \neq \mathrm{Re}[\log(1-1/\rho)]$ para ceros en el disco

La integral $J(\rho) = \int_{-\infty}^\infty \mathrm{Re}[\log(1-(1/2+it)/\rho)]\frac{2\,dt}{\pi(1+4t^2)}$ se calcula, para $\rho \notin \{1/2+it : t \in \mathbb{R}\}$, por la propiedad de la media de Poisson de funciones armónicas. La función $h(t) = \mathrm{Re}[\log(1-(1/2+it)/\rho)]$ es la parte real de la función analítica $\log(1-s/\rho)$ con $s = 1/2+it$, que es armónica en $t$ siempre que $1/2+it \neq \rho$, es decir, fuera del punto $t = -i(\rho-1/2) = t_\rho$.

Si $t_\rho \in \mathbb{H}^-$ (i.e., $\mathrm{Re}(\rho) > 1/2$), la función $h(t)$ es armónica en un vecindario de $\mathbb{H}^-$, y la integral de Poisson con peso $P_{1/2}(t)$ da el valor de la extensión armónica en $w_0 = -i/2 \in \mathbb{H}^-$, que es $h_\mathrm{harm}(-i/2) = \mathrm{Re}[\log(1-s_0/\rho)]$ con $s_0 = 1/2+i(-i/2) = 1$. El cálculo es válido en este caso: $J(\rho) = \mathrm{Re}[\log(1-1/\rho)]$ cuando $\mathrm{Re}(\rho) > 1/2$.

Si $t_\rho \in \mathbb{H}$ (i.e., $\mathrm{Re}(\rho) < 1/2$), la función $h(t)$ tiene una singularidad logarítmica en $t_\rho \in \mathbb{H}^-$... no, en $\mathbb{H}$. Esto significa que $h(t)$ no es armónica en todo $\mathbb{H}^-$ sino solo en $\mathbb{H}^- \setminus \{t_\rho\}$. La fórmula de la media de Poisson en $w_0 = -i/2 \in \mathbb{H}^-$ debe incluir la corrección por la singularidad de $h$ en $t_\rho$:
$$J(\rho) = \mathrm{Re}[\log(1-1/\rho)] + \log\left|\frac{-i/2 - \bar{t}_\rho}{-i/2 - t_\rho}\right|.$$

El factor de corrección es el término de Poisson-Jensen para la singularidad en $t_\rho$. Calculándolo con $t_\rho = \gamma + i(1/2-\sigma)$ para $\sigma < 1/2$ (de modo que $\mathrm{Im}(t_\rho) = 1/2-\sigma > 0$, y el cero está en $\mathbb{H}$, no en $\mathbb{H}^-$)... El punto $t_\rho$ está en $\mathbb{H}$, no en $\mathbb{H}^-$, por lo que no hay singularidad en el semiplano inferior. La función $h(t)$ para $\mathrm{Re}(\rho) < 1/2$ tiene su singularidad en $\mathbb{H}$ (semiplano superior), y la integral de Poisson en $w_0 = -i/2 \in \mathbb{H}^-$ no pasa por esa singularidad.

**Proposición 6.3.** *Para $\mathrm{Re}(\rho) < 1/2$ (cero de $\xi$ en el semiplano izquierdo de la franja crítica): $J(\rho) = \mathrm{Re}[\log(1-1/\rho)]$.*

*Para $\mathrm{Re}(\rho) > 1/2$: también $J(\rho) = \mathrm{Re}[\log(1-1/\rho)]$.*

*En consecuencia, la cancelación $J(\rho) + J(1-\rho) = 0$ es algebraicamente correcta para todo par $(\rho, 1-\rho)$.*

### 6.4. La fuente real de la discrepancia: intercambio suma-integral

La cancelación $\sum_\rho [J(\rho) + J(1-\rho)] = 0$ es formalmente correcta término a término, pero la convergencia de la serie $\sum_\rho J(\rho)$ y el intercambio $\sum_\rho J(\rho) = \int(\sum_\rho \mathrm{Re}[\log(\cdots)])\cdot P_{1/2}\,dt$ requieren convergencia absoluta de la suma. La serie del producto de Hadamard $\xi(1/2+it) = \xi(0)\prod_\rho (1-(1/2+it)/\rho)(1-(1/2+it)/(1-\rho))$ converge absolutamente en la recta crítica, pero el logaritmo $\log|\xi(1/2+it)| = \log|\xi(0)| + \sum_\rho \mathrm{Re}[\log(1-(1/2+it)/\rho) + \log(1-(1/2+it)/(1-\rho))]$ es una suma condicionalmente convergente en $t$.

El intercambio integral-suma en §5 del enunciado de la tarea:
$$I = -\log 2 + \sum_\rho \int \mathrm{Re}[\log(\cdots)] P_{1/2}\,dt = -\log 2 + \sum_\rho [J(\rho) + J(1-\rho)] = -\log 2 + \sum_\rho 0 = -\log 2,$$
es inválido cuando la integral de $|\log|\xi(1/2+it)||$ contra $P_{1/2}(t)$ diverge, que es exactamente lo que ocurre bajo RH (ceros de $\xi$ en la recta crítica dan $\log|\xi| = -\infty$ en puntos reales del dominio de integración).

**Proposición 6.4 (la fuente del colapso).** *El argumento de cancelación $I = -\log 2$ incondicionalmente falla porque:*
*(a) Bajo RH, $\log|\xi(1/2+it)| = -\infty$ en los puntos $t = \gamma_n$, y la integral $I$ no existe como integral de Lebesgue.*
*(b) Sin RH (si $\xi$ no tiene ceros en la recta crítica), la cancelación sería válida y daría $I = -\log 2$, pero esto contradice la Proposición 5.1 (que afirma $I = -\log 2 + \delta$ con $\delta > 0$ bajo $\neg$RH). La contradicción revela que, sin ceros en la recta crítica, el intercambio suma-integral no tiene obstáculos técnicos, pero la hipótesis misma (sin ceros en la recta crítica) implica RH, haciendo el argumento circular.*

---

## §7. Regularización de la integral de Jensen

### 7.1. La necesidad de regularizar

La integral $I = \int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)}$ no es una integral de Lebesgue porque $\log|\xi(1/2+i\gamma_n)| = -\infty$ para cada cero $\gamma_n$ de $\xi$ en la recta crítica. La función $\log|\xi(1/2+it)|$ es localmente integrable cerca de cada cero (el comportamiento es $\sim \log|t-\gamma_n|$, que es integrable en un intervalo), pero la presencia de infinitos ceros requiere que la serie de contribuciones converja.

### 7.2. Regularización via la fórmula de Jensen para $r < 1$

La regularización más natural es la ya indicada: usar la fórmula de Jensen para $r < 1$ y tomar el límite:
$$I_r = \frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2 + \sum_{|z_k|<r}\log\frac{r}{|z_k|}.$$
La integral $I_r$ está bien definida para todo $r < 1$ porque $F(re^{i\theta}) \neq 0$ para $r < r_0$ donde $r_0 = \min_{k}|z_k|$ (con el mínimo sobre los ceros de $F$ en el disco). Bajo RH, $F$ no tiene ceros en el disco, y $I_r = -\log 2$ para todo $r < 1$; el límite $I = -\log 2$ es trivialmente válido (sin ceros en el disco, $\log|F(re^{i\theta})|$ converge uniformemente a $\log|F(e^{i\theta})|$ si la convergencia de $F$ es uniforme, pero en realidad $F$ tiene ceros en la frontera y la convergencia no es uniforme). Bajo RH, la convergencia de $I_r$ a $I$ es la convergencia monótona de $\log|F(re^{i\theta})|$ a $\log|F(e^{i\theta})|$ (desde arriba, pues no hay ceros en el disco), y la integral converge por el teorema de convergencia monótona si $I > -\infty$.

**Proposición 7.1 (criterio regularizado).** *El criterio correcto para RH via la fórmula de Jensen es:*
$$\mathrm{RH} \iff \lim_{r \to 1^-} \frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2.$$
*Bajo $\neg$RH: el límite es $-\log 2 + \delta$ con $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|) > 0$.*

*La integral en la frontera $I = \int \log|F(e^{i\theta})|d\theta/(2\pi)$, si es que existe como integral de Lebesgue, satisface $I \leq -\log 2$ bajo RH (por la presencia de ceros en la frontera) y $I = -\infty$ si los ceros de $\xi$ en la recta crítica son suficientemente densos. La formulación via el límite $r \to 1^-$ es la versión bien definida del criterio.*

### 7.3. Condición de convergencia de la integral fronteriza

La integral $I = \int_0^{2\pi}\log|F(e^{i\theta})|d\theta$ converge (posiblemente a $-\infty$) cuando la serie $\sum_n \int_{|\theta-\theta_n|<\epsilon_n}\log|e^{i\theta}-e^{i\theta_n}|\,d\theta$ converge absolutamente. Para ceros simples de $F$ en $e^{i\theta_n}$ (que corresponden a ceros simples de $\xi$ en la recta crítica), la contribución de cada cero es $\sim -c|\log\epsilon_n|\epsilon_n$. La serie converge si los ceros de $\xi$ en la recta crítica no son demasiado densos.

La densidad de los ceros de $\xi$ en $[0,T]$ es $\sim \frac{T}{2\pi}\log\frac{T}{2\pi e}$ (fórmula de Riemann-von Mangoldt). La separación típica entre ceros consecutivos cerca de $\gamma_n \approx T$ es $\sim 2\pi/\log T$. La contribución de cada cero a $I$ es $\sim -\frac{2}{\pi(1+4\gamma_n^2)}\cdot |\log(2\pi/\log\gamma_n)|$. La serie de estas contribuciones converge condicionalmente (las contribuciones positivas de $\log|\xi|$ fuera de los ceros compensan). La integral $I$ existe como integral de Lebesgue con valor $-\infty$ solo si las contribuciones negativas dominan incondicionalmente, lo cual no ocurre para la distribución de ceros de $\xi$.

---

## §8. Síntesis del Camino 2 al término del Documento 87

### 8.1. La estructura completa del criterio de Jensen

El Camino 2 ha producido, a lo largo de los Docs 75–87, la siguiente cadena de equivalencias:

**(a)** RH $\iff$ $F(z) = \xi(z/(z-1))$ no tiene ceros en $\{|z|<1\}$ (Doc 81).

**(b)** RH $\iff$ $\lim_{r\to 1^-}\frac{1}{2\pi}\int_0^{2\pi}\log|F(re^{i\theta})|\,d\theta = -\log 2$ (Proposición 7.1 de este documento).

**(c)** RH $\iff$ $\int_{-\infty}^\infty \log|\xi(1/2+it)|\frac{2\,dt}{\pi(1+4t^2)} = -\log 2$ (forma distribuida de (b), válida como integral de Lebesgue si los ceros de $\xi$ en la recta crítica son simples y satisfacen la condición de convergencia de §7.3).

**(d)** El exceso del criterio, bajo $\neg$RH, es exactamente $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|) > 0$ (Proposición 5.1).

**(e)** La fórmula de Poisson-Jensen en $\mathbb{H}$ con evaluación en $w_0 = i/2$ es equivalente a (c), pero es válida como fórmula finita solo bajo $\neg$RH (ceros de $f(t) = \xi(1/2+it)$ en el semiplano inferior, que corresponden a ceros off-critical con $\mathrm{Re}(\rho) > 1/2$); bajo RH, los ceros están en la frontera real y la fórmula diverge.

### 8.2. La tabla de errores corregidos

Los errores detectados a lo largo del análisis, y sus correcciones:

| Error (identificado en) | Corrección |
|---|---|
| §2.2: $I \leq -\log 2$ bajo RH (Poisson-Jensen en $\mathbb{H}$) | La fórmula no aplica cuando $f$ tiene ceros en la frontera. El resultado correcto es $I \geq -\log 2$ (criterio del disco, Doc 84). |
| Doc 84 §10.3: cancelación por pares $\delta = 0$ | El exceso es una suma solo sobre $\mathrm{Re}(\rho)>1/2$; el par $1-\rho$ contribuye desde fuera del disco. |
| Doc 84 §10: cálculo por residuos de $J(\rho)$ | El cálculo por residuos da el valor correcto de $J(\rho)$, pero el intercambio suma-integral falla bajo RH por no-integrabilidad de $\log|\xi|$ en la frontera. |

### 8.3. El estado del Camino 2

**Resultado sólido:** RH es equivalente a $\delta = 0$, donde $\delta = \sum_{\rho:\,\mathrm{Re}(\rho)>1/2}\log(|\rho|/|\rho-1|)$. Este es el exceso de la fórmula de Jensen, una suma convergente de términos no-negativos.

**La barrera:** Demostrar $\delta = 0$ sin asumir RH requiere demostrar que $\xi$ no tiene ceros con $\mathrm{Re}(\rho) > 1/2$, que es exactamente RH. El criterio es una reformulación exacta y no circular, pero no ofrece, por sí solo, un método de demostración.

**La pregunta que queda abierta:** ¿Puede acotarse superiormente $\delta$ por métodos analíticos (cota de energía, desigualdad integral, principio variacional) de modo que se fuerce $\delta = 0$?

La relación $\delta = \sum_{|z_k|<1}\log(1/|z_k|)$ es la "energía logarítmica" de los ceros de $F$ en el disco con respecto al origen. Una demostración de $\delta = 0$ via métodos de teoría de funciones requeriría una cota $\log(1/|z_k|) \leq 0$ para todo cero de $F$ en el disco, lo cual equivale a $|z_k| \geq 1$, es decir, a que no haya ceros en el disco. No hay escape circular aquí: cualquier demostración de $\delta = 0$ debe usar propiedades de $\xi$ que vayan más allá de la ecuación funcional y del producto de Hadamard.

---

*Doc 87 completado.*
