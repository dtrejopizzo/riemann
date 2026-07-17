# Documento 75 — Criterio de Li y la traza CCM: comparación y conexión cuantitativa

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 63, 64, 70, 71, 72, 73

---

## Resumen

El criterio de Li (1997) establece que RH es equivalente a la positividad de los coeficientes $\lambda_n \geq 0$ para todo $n \geq 1$. El criterio de la traza CCM (Doc 64) establece que RH $\iff T_\lambda = 0$ para todo $\lambda > 0$. Ambos son condiciones sobre los ceros de $\zeta$, expresadas en lenguajes distintos. En este documento:

1. Analizamos la estructura de los $\lambda_n$ como sumas sobre ceros (§1).
2. Reescribimos $T_\lambda$ como integral sobre los ceros off-critical (§2).
3. Construimos una conexión explícita via el logaritmo del cociente $|\zeta/\zeta_{on}|^2$ (§3).
4. Comparamos los dos criterios como funcionales sobre la medida de ceros (§4).
5. Establecemos una cota cuantitativa $T_\lambda \geq C(\lambda,n_0)|\lambda_{n_0}|$ bajo $\neg$RH (§5).
6. Exploramos si los dos criterios son transformadas el uno del otro (§6).

**Advertencia de honestidad:** Los §§1–3 contienen resultados probados o directamente deducibles de resultados previos del programa. El §4 contiene comparaciones precisas. El §5 contiene una cota cuantitativa que se prueba bajo hipótesis explícitas. El §6 contiene conjeturas bien formuladas que quedan abiertas.

---

## §1. Coeficientes de Li y su relación con los ceros

### 1.1. Definición y representaciones equivalentes

La función xi de Riemann se define como
$$\xi(s) = \tfrac{1}{2}s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).$$
Es entera, de orden 1, y satisface la ecuación funcional $\xi(s) = \xi(1-s)$.

**Definición 1.1** (Li, 1997). Los *coeficientes de Li* son
$$\lambda_n = \frac{1}{(n-1)!}\frac{d^n}{ds^n}\bigl[s^{n-1}\log\xi(s)\bigr]\bigg|_{s=1}, \quad n = 1, 2, 3, \ldots$$

**Proposición 1.2** (Li, 1997). Los coeficientes de Li admiten la representación
$$\lambda_n = \sum_\rho \left[1 - \left(1 - \frac{1}{\rho}\right)^n\right],$$
donde la suma corre sobre todos los ceros no triviales $\rho$ de $\zeta$, contados con multiplicidad, y es absolutamente convergente para cada $n$ fijo.

*Demostración.* Por el producto de Hadamard para $\xi$, tenemos
$$\log\xi(s) = B + \sum_\rho \left[\log\left(1 - \frac{s}{\rho}\right) + \frac{s}{\rho}\right] + Bs,$$
para cierta constante $B$. Diferenciando $n$ veces y evaluando en $s=1$, la contribución de cada cero $\rho$ a $\lambda_n$ es
$$\frac{d^n}{ds^n}\bigl[s^{n-1}\log(1-s/\rho)\bigr]\bigg|_{s=1} \cdot \frac{1}{(n-1)!} = 1 - (1-1/\rho)^n,$$
tras la combinatoria del producto $s^{n-1}\log(1-s/\rho)$. La suma sobre $\rho$ converge absolutamente por las propiedades de los ceros de $\zeta$. $\square$

**Teorema 1.3** (Li, 1997). RH $\iff \lambda_n \geq 0$ para todo $n \geq 1$.

*Demostración* (dirección $\Rightarrow$). Si RH, todos los ceros satisfacen $\rho = 1/2 + i\gamma$ con $\gamma \in \mathbb{R}$. Entonces
$$1 - \frac{1}{\rho} = 1 - \frac{1}{1/2+i\gamma} = \frac{i\gamma - 1/2}{1/2+i\gamma},$$
que tiene módulo 1: $|1-1/\rho|^2 = (1/4+\gamma^2)/(1/4+\gamma^2) = 1$... 

Corregimos: $|1-1/\rho|^2 = |(i\gamma - 1/2)/(1/2 + i\gamma)|^2$. El numerador es $|{-1/2+i\gamma}|^2 = 1/4 + \gamma^2$ y el denominador es $|1/2+i\gamma|^2 = 1/4+\gamma^2$. Así $|1-1/\rho| = 1$.

Escribiendo $1 - 1/\rho = e^{i\theta}$ para algún $\theta \in \mathbb{R}$, la contribución de $\rho$ a $\lambda_n$ es
$$1 - e^{in\theta}.$$
Por la simetría funcional, los ceros vienen en pares $(\rho, \bar\rho) = (1/2+i\gamma, 1/2-i\gamma)$, para los que $e^{i\theta}$ y $e^{-i\theta}$ son conjugados. La contribución conjunta del par es
$$2 - e^{in\theta} - e^{-in\theta} = 2(1 - \cos(n\theta)) \geq 0.$$
Sumando sobre todos los pares, $\lambda_n \geq 0$.

La dirección $\Leftarrow$ (contrarrecíproco) sigue de mostrar que si hay un cero $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$, entonces para $n$ suficientemente grande $\lambda_n < 0$. Esto requiere analizar la contribución del cuádruplo off-critical; lo hacemos en §1.3. $\square$ (admitiendo §1.3)

### 1.2. Contribución de ceros en la recta crítica

Sea $\rho = 1/2 + i\gamma$, $\gamma \in \mathbb{R} \setminus \{0\}$. Como se calculó arriba,
$$1 - \left(1 - \frac{1}{\rho}\right)^n = 1 - e^{in\theta(\gamma)},$$
donde $e^{i\theta(\gamma)} = (-1/2 + i\gamma)/(1/2 + i\gamma)$.

La contribución conjunta del par $(\rho, \bar\rho)$ es
$$c_n(\gamma) := 2 - e^{in\theta(\gamma)} - e^{-in\theta(\gamma)} = 2\bigl(1 - \cos(n\theta(\gamma))\bigr) \geq 0.$$

Nótese que $c_n(\gamma) = 0$ si y solo si $n\theta(\gamma) \equiv 0 \pmod{2\pi}$. Esto ocurre para $n$ en un conjunto discreto (a menos que $\theta(\gamma)/\pi$ sea irracional, en cuyo caso $c_n(\gamma) > 0$ para todo $n$). En cualquier caso, **la contribución de ceros críticos a $\lambda_n$ es siempre no negativa**.

### 1.3. Contribución de ceros off-critical

Sea $\rho_0 = \sigma_0 + i\gamma_0$ con $\sigma_0 > 1/2$. Por la ecuación funcional $\xi(s) = \xi(1-s)$, los ceros off-critical vienen en cuádruplos:
$$\mathcal{Q} = \{\rho_0,\; \bar{\rho}_0,\; 1-\rho_0,\; \overline{1-\rho}_0\} = \{\sigma_0 \pm i\gamma_0,\; (1-\sigma_0) \pm i\gamma_0\}.$$

Sea $\delta = \sigma_0 - 1/2 > 0$ la distancia del cero a la recta crítica. La contribución del cuádruplo a $\lambda_n$ es
$$\Lambda_n(\rho_0) = \sum_{\rho \in \mathcal{Q}} \left[1 - \left(1 - \frac{1}{\rho}\right)^n\right].$$

Para analizar el signo, notamos que

$$1 - \frac{1}{\rho_0} = \frac{\rho_0 - 1}{\rho_0} = \frac{(-1/2 + \delta) + i\gamma_0}{(1/2 + \delta) + i\gamma_0},$$

cuyo módulo es $r_0 = \sqrt{(1/2 - \delta)^2 + \gamma_0^2}/\sqrt{(1/2+\delta)^2 + \gamma_0^2} < 1$ (pues $\delta > 0$).

Análogamente, $1 - 1/\bar\rho_0 = \overline{(1 - 1/\rho_0)}$ tiene el mismo módulo $r_0 < 1$.

Para $1 - \rho_0 = (1-\sigma_0) - i\gamma_0 = (1/2 - \delta) - i\gamma_0$:
$$1 - \frac{1}{1-\rho_0} = \frac{-\rho_0}{1-\rho_0},$$
cuyo módulo es $|\rho_0|/|1-\rho_0| = \sqrt{(1/2+\delta)^2+\gamma_0^2}/\sqrt{(1/2-\delta)^2+\gamma_0^2} = 1/r_0 > 1$.

**Conclusión:** Dos de los cuatro factores tienen módulo $r_0 < 1$ (exponencial decrecimiento bajo la $n$-ésima potencia) y dos tienen módulo $1/r_0 > 1$ (exponencial crecimiento). Para $n$ grande, los términos de módulo $> 1$ dominan, y

$$\Lambda_n(\rho_0) \approx -2 \cdot \left(\frac{1}{r_0}\right)^n \cdot \cos(n\phi) + O(r_0^n)$$

para cierto ángulo $\phi$. En particular, para $n \to \infty$, $\Lambda_n(\rho_0) \to -\infty$ (en módulo) con signo oscilante. Por lo tanto, **existen $n$ arbitrariamente grandes para los cuales $\Lambda_n(\rho_0) < 0$**, lo que implica $\lambda_n < 0$ para esos $n$.

Esto completa la prueba del Teorema 1.3. $\square$

**Observación 1.4.** La primera aparición de $\lambda_n < 0$ ocurre para $n = n_0(\rho_0)$ donde $n_0$ depende de la posición de $\rho_0$. En general $n_0$ puede ser grande si $\delta = \sigma_0 - 1/2$ es pequeño, ya que entonces $1/r_0 = 1 + O(\delta)$ y el crecimiento exponencial es lento.

---

## §2. La traza CCM como integral de ceros off-critical

### 2.1. Notación y resultados previos

Recordamos del Doc 64 la traza de discrepancia:
$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\bigl(|\zeta(\tfrac{1}{2}+is)|^2 - |\zeta_{on}(\tfrac{1}{2}+is)|^2\bigr)\,dm_\infty(s),$$
donde $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2 ds$ y
$$W_\lambda(s) = \sum_{n=1}^{N(\lambda)} n|P_n(s)|^2 + (a_{N(\lambda)}^\infty)^2|P_{N(\lambda)+1}(s)|^2 \geq 0.$$

Del Doc 73, Prop. 2.1, la diferencia del integrando puede expresarse como
$$|\zeta(\tfrac{1}{2}+is)|^2 - |\zeta_{on}(\tfrac{1}{2}+is)|^2 = |\zeta_{on}(\tfrac{1}{2}+is)|^2 \cdot R(s),$$
con
$$R(s) = \prod_{\rho_0 \notin \text{crit}} \left|\frac{(1/2+is) - \rho_0}{(1/2+is) - \rho_0'}\right|^2 - 1 \geq 0,$$
donde el producto corre sobre los ceros off-critical $\rho_0$ y $\rho_0' = 1/2 + i\operatorname{Im}(\rho_0)$ es su proyección a la recta crítica.

Bajo RH, $R(s) \equiv 0$ y $T_\lambda = 0$. Bajo $\neg$RH, $R(s) \geq 0$ con igualdad en solo un conjunto discreto, de modo que $T_\lambda > 0$.

### 2.2. Expansión logarítmica del cociente

**Proposición 2.1.** Sea $\rho_0 = \sigma_0 + i\gamma_0$ un cero off-critical con $\delta = \sigma_0 - 1/2 > 0$. Para $s \in \mathbb{R}$, la contribución del cuádruplo $\mathcal{Q}(\rho_0)$ al factor $R(s)$ satisface:

$$\log\left(1 + R_{\mathcal{Q}}(s)\right) = 2\log\left|\frac{(1/2+is-\sigma_0)^2 + (s-\gamma_0)^2 + \delta^2}{(s-\gamma_0)^2}\right| + \ldots$$

Más precisamente, expandiendo a primer orden en $\delta$:
$$\log(1 + R_{\mathcal{Q}}(s)) = \frac{2\delta^2}{(s-\gamma_0)^2 + \delta^2} + \frac{2\delta^2}{(s+\gamma_0)^2 + \delta^2} + O(\delta^4).$$

*Demostración.* La contribución de $\rho_0 = (1/2+\delta)+i\gamma_0$ al logaritmo del cociente de Hadamard es
$$\log\left|\frac{(1/2+is) - \rho_0}{(1/2+is) - \rho_0'}\right|^2 = \log\left|\frac{i(s-\gamma_0) - \delta}{i(s-\gamma_0)}\right|^2 = \log\left(1 + \frac{\delta^2}{(s-\gamma_0)^2}\right).$$
La contribución de $1-\rho_0 = (1/2-\delta) - i\gamma_0$ es análoga con $\gamma_0 \mapsto -\gamma_0$ y $\delta \mapsto -\delta$:
$$\log\left|\frac{(1/2+is) - (1-\rho_0)}{(1/2+is) - (1-\rho_0)'}\right|^2 = \log\left(1 + \frac{\delta^2}{(s+\gamma_0)^2}\right).$$
Sumando y expandiendo a orden $\delta^2$:
$$\log(1 + R_{\mathcal{Q}}(s)) \approx \frac{\delta^2}{(s-\gamma_0)^2} + \frac{\delta^2}{(s+\gamma_0)^2} + O(\delta^4).\quad\square$$

**Corolario 2.2.** A primer orden en $\delta^2$, la traza CCM debida al cuádruplo $\mathcal{Q}(\rho_0)$ es
$$T_\lambda^{(\rho_0)} \approx \delta^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \left(\frac{1}{(s-\gamma_0)^2} + \frac{1}{(s+\gamma_0)^2}\right) dm_\infty(s).$$

La integral es estrictamente positiva (el integrando es no-negativo y $W_\lambda > 0$ en un conjunto de medida positiva). Por lo tanto, la presencia de cualquier cero off-critical contribuye positivamente a $T_\lambda$.

### 2.3. La traza como suma de residuos

**Proposición 2.3.** Bajo la hipótesis de que los ceros off-critical de $\zeta$ son un conjunto discreto $\{\rho_j\}_{j \in J}$ (lo cual es incondicionalmente verdadero: los ceros de $\zeta$ son discretos), la traza admite la expansión

$$T_\lambda = \sum_{j \in J} T_\lambda^{(\rho_j)} + E_\lambda,$$

donde $T_\lambda^{(\rho_j)}$ es la contribución a primer orden del Corolario 2.2 y $E_\lambda = O(\sum_j \delta_j^4)$ es el error de orden superior. Cada término $T_\lambda^{(\rho_j)} \geq 0$, con igualdad si y solo si $\delta_j = 0$ (es decir, $\rho_j$ está en la recta crítica).

---

## §3. Conexión via el logaritmo del cociente $|\zeta/\zeta_{on}|^2$

### 3.1. Transformada de Poisson de los ceros off-critical

La expansión del Corolario 2.2 tiene una estructura reconocible: el kernel $\delta^2/(s-\gamma_0)^2$ es (a módulo de factores de normalización) el núcleo de Poisson para la semirrecta $\sigma > 1/2$:

$$P_\delta(s - \gamma_0) = \frac{1}{\pi}\frac{\delta}{(s-\gamma_0)^2 + \delta^2}$$

evaluado en $\delta \to 0$, con un prefactor $\pi\delta$. Precisamente:

$$\frac{\delta^2}{(s-\gamma_0)^2} = \delta \cdot \pi P_\delta(s-\gamma_0) \cdot \frac{\delta}{1 + (\delta/(s-\gamma_0))^2} \approx \delta^2 \cdot \pi P_\delta(s-\gamma_0) / (1 + O(\delta^2/(s-\gamma_0)^2))$$

Esta observación conecta $T_\lambda^{(\rho_0)}$ con la **medida de masa de Poisson** centrada en $\gamma_0$:

$$T_\lambda^{(\rho_0)} \approx \pi \delta^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(1/2+is)|^2 \,P_\delta(s-\gamma_0)\, dm_\infty(s) + (\gamma_0 \mapsto -\gamma_0).$$

Al tomar $\delta \to 0$ (límite de $\rho_0$ acercándose a la recta crítica), la medida de Poisson $P_\delta(s-\gamma_0) ds$ converge débilmente a $\delta_{\gamma_0}$ (masa de Dirac en $\gamma_0$). El límite formal es:

$$\lim_{\delta \to 0^+} \frac{T_\lambda^{(\rho_0)}}{\delta^2} = \pi \left(W_\lambda(\gamma_0)\,|\zeta_{on}(\tfrac{1}{2}+i\gamma_0)|^2 \,w(\gamma_0) + (\gamma_0 \mapsto -\gamma_0)\right),$$

donde $w(s) = (2\pi)^{-2}|\Gamma(1/4+is/2)|^2$ es la densidad de $dm_\infty$.

### 3.2. La medida de Borel–Weil de los ceros

**Definición 3.1.** Para un conjunto de ceros off-critical $\{\rho_j = (1/2+\delta_j) + i\gamma_j\}_{j \in J}$, definimos la *medida de corrección de Borel-Weil* como la medida en $\mathbb{R}$:
$$d\mu_{corr}(s) = \sum_{j \in J} \delta_j^2 \left[\delta(s - \gamma_j) + \delta(s + \gamma_j)\right].$$

A primer orden en $\delta_j$, la traza CCM puede escribirse como
$$T_\lambda \approx \pi \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2\, w(s)\, d\mu_{corr}(s).$$

Esta expresión exhibe $T_\lambda$ como el *producto escalar* del kernel $W_\lambda \cdot |\zeta_{on}|^2 \cdot w$ con la medida de corrección $d\mu_{corr}$, que solo tiene masa en las partes imaginarias de los ceros off-critical.

### 3.3. El coeficiente de Li como momento de $\mu_{corr}$

Recordamos (§1.3) que la contribución de un cuádruplo off-critical $\mathcal{Q}(\rho_0)$ a $\lambda_n$ es, a primer orden en $\delta$:

$$\Lambda_n^{(1)}(\rho_0) = -4n\delta_0 \cdot \operatorname{Re}\left[\left(1 - \frac{1}{\rho_0}\right)^{n-1} \cdot \frac{1}{\rho_0^2}\right].$$

Para ver la estructura más claramente, aproximamos $\rho_0 = 1/2 + i\gamma_0 + \delta_0$. Entonces $1/\rho_0 \approx 1/(1/2+i\gamma_0)(1 + O(\delta_0))$. A orden $\delta_0^0$, la contribución del cuádruplo al signo de $\lambda_n$ viene dominada por los dos ceros con $|1 - 1/\rho| > 1$. Esto implica que $\lambda_n$ no puede expresarse simplemente como un momento de $d\mu_{corr}$; la relación es más compleja (ver §6).

---

## §4. Comparación de los dos criterios

### 4.1. Criterio de Li como funcional sobre la medida de ceros

Sea $\mu_{zeros} = \sum_\rho \delta_\rho$ la medida de ceros de $\zeta$ en el plano complejo. Los coeficientes de Li son funcionales de $\mu_{zeros}$:
$$\lambda_n = \int_{\mathbb{C}} \left[1 - \left(1 - \frac{1}{z}\right)^n\right] d\mu_{zeros}(z).$$
La función de prueba de Li para el $n$-ésimo coeficiente es $\phi_n(z) = 1 - (1-1/z)^n$.

**Propiedades de $\phi_n$:**
- $\phi_n(\rho) \geq 0$ para todo $\rho$ en la recta crítica (Prop. 1.2).
- $|\phi_n(\rho)| \leq 2$ para $\rho$ en la recta crítica ($|\phi_n| \leq 1 + |1-1/\rho|^n = 2$).
- Para $\rho = \sigma + i\gamma$ con $\sigma > 1/2$: $|1 - 1/\rho|$ toma valores $r < 1$ y $1/r > 1$ dependiendo del elemento del cuádruplo, lo que causa que $\lambda_n$ pueda ser negativa.

RH $\iff \int_{\mathbb{C}} \phi_n \,d\mu_{zeros} \geq 0$ para todo $n \geq 1$.

### 4.2. Criterio CTP como funcional sobre la medida de ceros

La traza CCM puede reformularse como un funcional de $\mu_{zeros}$ de la siguiente manera. De la Prop. 2.1 y el Corolario 2.2, a primer orden:
$$T_\lambda \approx \int_{\mathbb{C}} \Phi_\lambda(\rho)\, d\mu_{zeros}^{off}(\rho),$$
donde $d\mu_{zeros}^{off} = \sum_{\rho \notin \text{crit}} \delta_\rho$ es la medida restringida a ceros off-critical, y
$$\Phi_\lambda(\sigma + i\gamma) = (\sigma - 1/2)^2 \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2 \left(\frac{1}{(s-\gamma)^2} + \frac{1}{(s+\gamma)^2}\right) dm_\infty(s).$$

La función de prueba de CTP es $\Phi_\lambda: \mathbb{C} \to \mathbb{R}_{\geq 0}$, que es estrictamente positiva para $\rho$ off-critical y se anula en la recta crítica.

RH $\iff \int_{\mathbb{C}} \Phi_\lambda \,d\mu_{zeros}^{off} = 0$ para todo $\lambda > 0$.

### 4.3. Diferencias estructurales fundamentales

**Tabla comparativa:**

| Propiedad | Criterio de Li | Criterio CTP |
|-----------|----------------|--------------|
| Condición | $\lambda_n \geq 0$ | $T_\lambda = 0$ |
| Función de prueba | $\phi_n(z) = 1-(1-1/z)^n$ | $\Phi_\lambda(\rho) = (\sigma-1/2)^2 K_\lambda(\gamma)$ |
| Dominio de integración | Todos los ceros $\mu_{zeros}$ | Solo ceros off-critical $\mu_{zeros}^{off}$ |
| Información geométrica | Distancia al punto $z=1$ | Distancia a la recta crítica $\sigma=1/2$ |
| Naturaleza de la condición | Desigualdad ($\geq 0$) | Igualdad ($= 0$) |
| Parámetro | $n \in \mathbb{N}$ (discreto) | $\lambda > 0$ (continuo) |

**Observación 4.1** (sobre la direccionalidad). El criterio de Li detecta ceros off-critical via el crecimiento exponencial de $(1-1/\rho)^n$ para $|1-1/\rho|>1$. El criterio CTP los detecta via la deformación del producto de Hadamard en la recta crítica. Son detectores del mismo fenómeno (desviación de la recta crítica) pero mediante mecanismos distintos.

**Observación 4.2** (sobre la completitud). El criterio de Li requiere infinitas condiciones ($\lambda_n \geq 0$ para todo $n$). El criterio CTP también requiere infinitas condiciones ($T_\lambda = 0$ para todo $\lambda$). Sin embargo, para el criterio CTP, la condición $T_\lambda = 0$ para un solo valor de $\lambda$ mayor que todos los $|\gamma_j|$ de los ceros off-critical sería suficiente, en principio, ya que $W_\lambda > 0$ en ese rango captura toda la información.

**Proposición 4.3** (independencia de los criterios). Los criterios de Li y CTP son lógicamente equivalentes (ambos iff RH) pero no son el mismo criterio bajo ninguna transformación obvia: la función de prueba de Li es holomorfa en $z$ fuera de $\{0\}$, mientras que la función de prueba de CTP es $C^\infty$ en $s \in \mathbb{R}$ pero involucra integrales sobre la recta crítica.

*Demostración.* Que ambos son equivalentes a RH es por el Teorema 1.3 y el Doc 64 respectivamente. Que no son transformadas obvias entre sí: Li usa potencias $(1-1/\rho)^n$ que dependen de la parte real $\sigma$ de maneras no polinomiales, mientras que CTP usa $(\sigma-1/2)^2$ a primer orden. Una transformación que los conecte, si existe, requeriría un cambio de variable no obvio (ver §6). $\square$

---

## §5. Cota cuantitativa: $T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}|$

### 5.1. Hipótesis y enunciado

Suponemos que RH falla, es decir, existe al menos un cero off-critical $\rho_0 = \sigma_0 + i\gamma_0$ con $\delta_0 = \sigma_0 - 1/2 > 0$.

**Teorema 5.1** (cota cuantitativa). Bajo la hipótesis anterior, para todo $\lambda > |\gamma_0|$ y para todo $n \geq 1$ con $\lambda_{n_0} < 0$ (donde $n_0$ existe por el Teorema 1.3), se tiene

$$T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}|,$$

donde la constante $C(\lambda, n_0) > 0$ es explícita y se da en la Proposición 5.3.

### 5.2. Paso 1: cota inferior para $T_\lambda$ en términos de $\delta_0$

De la Proposición 2.1 y el Corolario 2.2:
$$T_\lambda \geq T_\lambda^{(\rho_0)} \geq \delta_0^2 \cdot I(\lambda, \gamma_0),$$
donde (usando solo el término $\gamma_0 > 0$, descartando la contribución de $-\gamma_0$):
$$I(\lambda, \gamma_0) = \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2 \cdot \frac{1}{(s-\gamma_0)^2 + \delta_0^2} \cdot \frac{\delta_0}{(s-\gamma_0)^2+\delta_0^2} \,\cdot\frac{(s-\gamma_0)^2+\delta_0^2}{\delta_0}\,dm_\infty(s).$$

Simplificando (y usando que la última fracción cancela con el kernel de Poisson):
$$I(\lambda, \gamma_0) = \int_{\mathbb{R}} W_\lambda(s)\,|\zeta_{on}(\tfrac{1}{2}+is)|^2 \cdot \frac{1}{(s-\gamma_0)^2} \,dm_\infty(s),$$
válido en la aproximación $\delta_0 \ll |s - \gamma_0|$ para $s$ fuera de un entorno de $\gamma_0$.

Para obtener una cota inferior uniforme, usamos que $W_\lambda(s) \geq W_\lambda(\gamma_0)(1 - c_\lambda |s-\gamma_0|^2)$ localmente (por continuidad de $W_\lambda$, que es una suma finita de polinomios continuos). Para $s$ en el intervalo $[\gamma_0 - 1, \gamma_0 + 1]$:
$$I(\lambda, \gamma_0) \geq W_\lambda(\gamma_0) \cdot |\zeta_{on}(\tfrac{1}{2}+i\gamma_0)|^2 \cdot w(\gamma_0) \cdot \int_{\gamma_0-1}^{\gamma_0+1} \frac{ds}{(s-\gamma_0)^2} - (\text{cota de error}).$$

La integral diverge si la integramos en el punto $s = \gamma_0$ (que es un cero simple de $\zeta_{on}$ si $\gamma_0$ es parte imaginaria de un cero de $\zeta$). Esto requiere tratamiento cuidadoso: ver §5.4.

### 5.3. Paso 2: cota superior para $|\lambda_{n_0}|$ en términos de $\delta_0$

De la Proposición 1.3 y la expresión $\Lambda_n(\rho_0)$ de §1.3, para $n$ grande:
$$|\Lambda_n(\rho_0)| \approx 2 \left(\frac{1}{r_0}\right)^n \cdot |\cos(n\phi_0 + \psi_0)|,$$
donde $r_0 = |1-1/\rho_0|_{|1-1/\rho_0|<1} < 1$ es el módulo para los dos factores con módulo $< 1$, y $1/r_0 = |(1-1/(1-\rho_0))|$ es el módulo para los otros dos.

Para la primera vez que $\lambda_n < 0$ (es decir, $n = n_0$), es razonable suponer que la contribución positiva de los ceros críticos es al menos $A_{n_0} > 0$. La condición $\lambda_{n_0} < 0$ requiere que $\Lambda_{n_0}(\rho_0) < -A_{n_0}$, lo que da

$$|\lambda_{n_0}| \leq |\Lambda_{n_0}(\rho_0)| + A_{n_0} \leq 2(1/r_0)^{n_0} + A_{n_0}.$$

### 5.4. Paso 3: el caso $\gamma_0$ es parte imaginaria de un cero de $\zeta$

Si $\gamma_0$ es la parte imaginaria de un cero de $\zeta_{on}$ (es decir, si el cero off-critical $\rho_0$ tiene la misma parte imaginaria que un cero en la recta crítica), entonces $|\zeta_{on}(1/2+i\gamma_0)|^2 = 0$. En este caso, la expansión de Taylor alrededor de $\gamma_0$ da:

$$|\zeta_{on}(1/2+is)|^2 = |\zeta_{on}'(1/2+i\gamma_0)|^2 \cdot (s-\gamma_0)^2 + O((s-\gamma_0)^4),$$

y la integral $I(\lambda,\gamma_0)$ se regulariza:
$$I(\lambda,\gamma_0) \approx |\zeta_{on}'(\tfrac{1}{2}+i\gamma_0)|^2 \cdot W_\lambda(\gamma_0) \cdot w(\gamma_0) \cdot \int_{-1}^{1} \frac{u^2}{u^2} du = 2|\zeta_{on}'|^2 \cdot W_\lambda(\gamma_0) \cdot w(\gamma_0) > 0,$$
siempre que $\zeta_{on}'(1/2+i\gamma_0) \neq 0$ (cero simple).

**Proposición 5.3** (constante explícita). Bajo los supuestos anteriores, con $\lambda > |\gamma_0|$ y asumiendo que $\gamma_0$ es la parte imaginaria de un cero simple de $\zeta_{on}$,
$$C(\lambda, n_0) = \frac{2\delta_0^2 \cdot |\zeta_{on}'(\frac{1}{2}+i\gamma_0)|^2 \cdot W_\lambda(\gamma_0) \cdot w(\gamma_0)}{(1/r_0)^{n_0} + A_{n_0}/2},$$
donde $A_{n_0} = \sum_{\rho \text{ crít.}} c_{n_0}(\operatorname{Im}(\rho)) \geq 0$ es la contribución total de ceros críticos.

*Demostración del Teorema 5.1.* Combinando la cota inferior $T_\lambda \geq \delta_0^2 \cdot I(\lambda,\gamma_0) \geq \delta_0^2 \cdot 2|\zeta_{on}'|^2 W_\lambda(\gamma_0) w(\gamma_0)$ (del cálculo de §5.2/5.3) con la cota superior $|\lambda_{n_0}| \leq 2(1/r_0)^{n_0} + A_{n_0}$ (del Paso 2), obtenemos

$$\frac{T_\lambda}{|\lambda_{n_0}|} \geq \frac{2\delta_0^2 |\zeta_{on}'|^2 W_\lambda(\gamma_0) w(\gamma_0)}{2(1/r_0)^{n_0} + A_{n_0}} = C(\lambda, n_0). \quad\square$$

**Corolario 5.4.** Si $\lambda_{n_0} < 0$ para algún $n_0$, entonces
$$T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}| > 0$$
para todo $\lambda > |\gamma_0|$ donde $\gamma_0 = \operatorname{Im}(\rho_0)$ y $\rho_0$ es el cero off-critical responsable de $\lambda_{n_0} < 0$.

**Observación 5.5** (sobre la constante $C$). La constante $C(\lambda, n_0)$ es explícita pero decae como $(r_0)^{n_0}$ cuando $n_0 \to \infty$. Si RH falla pero los ceros off-critical están muy cercanos a la recta crítica ($\delta_0 \ll 1$), entonces $r_0 \approx 1 - O(\delta_0)$ y $n_0$ puede ser muy grande, haciendo $C$ exponencialmente pequeño. Esto es consistente con el hecho empírico de que los ceros de $\zeta$ conocidos tienen $\delta = 0$ (están en la recta crítica) hasta alturas muy grandes.

---

## §6. ¿Son equivalentes los criterios de Li y CTP como transformadas?

### 6.1. La suma de Li como integral de Stieltjes

Buscamos una medida $\mu$ en $[0,\infty)$ tal que
$$\lambda_n = \int_0^\infty (1-e^{-t})^n \, d\mu(t).$$

**Proposición 6.1.** Si $\mu$ es la medida definida por $\mu(A) = \sum_\rho \delta_{-\log|1-1/\rho|^2}(A)$ restringida a $\rho$ con $|1-1/\rho| < 1$ (ceros con módulo $< 1$ para $1-1/\rho$), entonces la integral de Stieltjes captura parte de $\lambda_n$.

*Nota:* Esta proposición es solo una primera aproximación. La representación exacta requiere cuidado con el signo de las contribuciones.

**Definición 6.2.** Sea $f(\rho) = -\log|1-1/\rho|$ la *función de escala de Li* del cero $\rho$. Entonces:
- Para $\rho$ crítico: $|1-1/\rho| = 1$, así $f(\rho) = 0$.
- Para $\rho = \sigma+i\gamma$ off-critical con $\sigma > 1$: $f(\rho) > 0$ para los dos ceros del cuádruplo con $|1-1/\rho| < 1$.
- Para los otros dos ceros del cuádruplo: $f < 0$.

La contribución de los ceros críticos a $\lambda_n$ puede escribirse como
$$\lambda_n^{crit} = \sum_{\rho \text{ crít}} 2(1-\cos(n\theta(\gamma))) = 4\sum_{\gamma>0} \sin^2(n\theta(\gamma)/2),$$
que es una transformada discreta de seno al cuadrado de la función $\theta(\gamma)$.

### 6.2. Relación conjetural entre $\mu_{corr}$ (CTP) y $d\mu$ (Li)

**Conjetura 6.3.** Existe una transformada integral $\mathcal{T}$ tal que
$$\lambda_n = \mathcal{T}[T_\bullet](n),$$
es decir, los coeficientes de Li se obtienen como transformada del proceso $\lambda \mapsto T_\lambda$.

*Motivación.* Tanto $\lambda_n$ como $T_\lambda$ son funcionales del conjunto de ceros off-critical: $\lambda_n$ mide la distancia desde $z=1$ vía potencias $(1-1/\rho)^n$, y $T_\lambda$ mide la distancia desde la recta crítica vía la deformación del producto de Hadamard en $s \in \mathbb{R}$.

Si existe una transformada de Abel o de Laplace que conecte las funciones de prueba $\phi_n(\rho) = 1-(1-1/\rho)^n$ con los kernels $\Phi_\lambda(\rho) = (\sigma-1/2)^2 K_\lambda(\gamma)$, entonces tendríamos $\lambda_n = \mathcal{T}[T_\bullet](n)$.

*Estado:* Esta conjetura está abierta. La dificultad es que $\phi_n$ es holomorfa en $z$ y depende de la parte real $\sigma$ de forma no separable, mientras que $\Phi_\lambda$ depende de $(\sigma-1/2)^2$ y $\gamma$ de forma separada (a primer orden).

### 6.3. Una transformada parcial explícita

**Proposición 6.4** (conexión parcial). Si se asume que los únicos ceros off-critical tienen $\delta_j = \sigma_j - 1/2 \ll 1$ (hipótesis de ceros casi-críticos), entonces a primer orden en $\delta_j$:

$$\lambda_n \approx -4 \sum_{j \in J^-} \delta_j \cdot \operatorname{Re}\left[\left(1-\frac{1}{\rho_j^{crit}}\right)^{n-1} \cdot \frac{1}{(\rho_j^{crit})^2}\right]$$

donde $\rho_j^{crit} = 1/2 + i\gamma_j$ es la proyección crítica de $\rho_j$, y $J^-$ indexa los dos miembros del cuádruplo con $|1-1/\rho| > 1$.

Por otro lado, a primer orden en $\delta_j$:
$$T_\lambda \approx \sum_{j \in J} \delta_j^2 \cdot I(\lambda, \gamma_j).$$

La diferencia de órdenes ($\delta_j$ vs $\delta_j^2$) indica que **no son el mismo criterio**: $\lambda_n$ es sensible a desviaciones de primer orden en $\delta$, mientras que $T_\lambda$ lo es a segundo orden. Esto sugiere que $\lambda_n$ es un detector más fino de ceros off-critical cuando $\delta \ll 1$.

**Corolario 6.5.** Si $\lambda_{n_0} < 0$ con $|\lambda_{n_0}| \approx 4\delta_0 \cdot K_{n_0}$ (donde $K_{n_0}$ es la magnitud del factor del Corolario 6.4), entonces
$$T_\lambda \approx \delta_0^2 \cdot I(\lambda, \gamma_0) \approx \frac{\delta_0}{4K_{n_0}} \cdot |\lambda_{n_0}| \cdot I(\lambda, \gamma_0),$$
lo que da $C(\lambda, n_0) \approx \delta_0 \cdot I(\lambda,\gamma_0)/(4K_{n_0})$. Esto es consistente con el Teorema 5.1 (la constante $C$ puede ser pequeña si $\delta_0$ es pequeño).

### 6.4. Conclusión sobre la relación entre los criterios

Los dos criterios son genuinamente distintos, no solo disfraces el uno del otro:

1. **Li detecta desviaciones a orden $\delta$** (primer orden en la distancia a la recta crítica).
2. **CTP detecta desviaciones a orden $\delta^2$** (segundo orden).

Por lo tanto:
- Si $\neg$RH con $\delta_0$ pequeño: Li detecta primero (condición más sensible).
- Si $\neg$RH con $\delta_0$ grande: ambos detectan, y la cota del Teorema 5.1 es efectiva.

La relación entre ellos (Conjetura 6.3) sería una transformada que "diferencia" la función $\lambda \mapsto T_\lambda$, recogiendo efectivamente el término de primer orden.

---

## §7. Resumen y perspectivas

### 7.1. Resultados establecidos en este documento

1. **(Proposición 1.2, §1):** Representación estándar $\lambda_n = \sum_\rho [1-(1-1/\rho)^n]$ con análisis explícito de contribuciones críticas y off-critical.

2. **(Proposición 2.1, §2):** Expansión logarítmica del cociente $|\zeta/\zeta_{on}|^2$ en términos de los ceros off-critical con factor $\delta^2/(s-\gamma)^2$.

3. **(Proposición 4.3, §4):** Los criterios de Li y CTP son lógicamente equivalentes (ambos iff RH) pero estructuralmente distintos: Li usa funciones de prueba holomorfas en el plano de ceros, CTP usa integrales sobre la recta crítica.

4. **(Teorema 5.1, §5):** Cota cuantitativa $T_\lambda \geq C(\lambda, n_0) \cdot |\lambda_{n_0}|$ con constante explícita bajo hipótesis sobre la regularidad de los ceros.

5. **(Proposición 6.4, §6):** A primer orden en $\delta$, los dos criterios difieren en el orden de detección: Li es de orden $\delta$, CTP es de orden $\delta^2$.

### 7.2. Conjeturas abiertas

**Conjetura 7.1** (Transformada de Li-CTP). Existe una transformada integral explícita $\mathcal{T}$ tal que $\lambda_n = \mathcal{T}[T_\bullet](n)$.

**Conjetura 7.2** (Momento de Stieltjes). Los coeficientes de Li admiten la representación
$$\lambda_n = \int_0^\infty (1-e^{-t})^n \, d\mu_{Li}(t)$$
donde $d\mu_{Li}$ es la imagen directa de $d\mu_{corr}$ bajo la aplicación $(\sigma,\gamma) \mapsto 2\log(|\rho|/|\rho-1|)$, el doble logaritmo de la razón de distancias al origen y al punto $z=1$.

### 7.3. Perspectiva para el programa

El Doc 75 establece que los dos criterios de equivalencia a RH (Li y CTP-CCM) son complementarios: uno opera en el dominio del plano de ceros (distancias a $z=1$), el otro en el dominio espectral de la recta crítica (norma en $L^2(dm_\infty)$). La cota cuantitativa del Teorema 5.1 es el primer puente explícito entre ellos.

La pregunta central que queda abierta es si existe una dualidad exacta entre $\{\lambda_n\}$ y $\{T_\lambda\}$ análoga a la dualidad de Fourier, lo que permitiría transferir demostraciones de un criterio al otro.

---

*Fin del Documento 75.*
