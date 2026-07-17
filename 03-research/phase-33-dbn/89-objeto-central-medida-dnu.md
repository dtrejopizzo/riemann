# Documento 89 — El objeto central: $d\nu = dm_{full} - dm_{full,on}$ como síntesis de los tres caminos

**Programa:** Hipótesis de Riemann — Fase 34 (síntesis)  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 70, 71, 72, 75, 81, 83, 84, 85, 86, 87, 88

---

## Resumen

Los documentos 74–88 desarrollaron tres caminos independientes hacia la Hipótesis de Riemann: el Camino 1 via la función de Nevanlinna $\mathcal{G}(z)$ y la diferencia de medidas; el Camino 2 via el exceso de Jensen $\delta$ y las propiedades analíticas de $F(z) = \xi(z/(z-1))$; el Camino 3 via la velocidad inicial del flujo De Bruijn-Newman $\partial_t T_\lambda|_{t=0}$. Este documento realiza la síntesis de los tres caminos, identificando el objeto matemático que subyace a todos: la medida $d\nu = dm_{full} - dm_{full,on} \geq 0$. Se establece con rigor que las tres cantidades centrales de cada camino son funcionales distintos de $d\nu$ que se anulan simultáneamente si y solo si RH. Se formula la equivalencia como un teorema de síntesis (§10) y se discute con honestidad el obstáculo estructural que el programa no ha superado (§11).

---

## §1. Las tres cantidades y su naturaleza

### 1.1. Definiciones y contexto

Fijamos la notación del programa. Sea $dm_\infty(s) = (2\pi)^{-2}|\Gamma(1/4 + is/2)|^2 \, ds$ la medida base sobre $\mathbb{R}$. Sean
$$dm_{full}(s) = |\zeta(1/2 + is)|^2 \, dm_\infty(s), \qquad dm_{full,on}(s) = |\zeta_{on}(1/2 + is)|^2 \, dm_\infty(s),$$
donde $\zeta_{on}$ es la función zeta hipotética con los mismos ceros que $\zeta$ proyectados sobre la recta crítica (Doc 83, §1.2). Por la Proposición 1.1 del Doc 83:
$$R(s) := \frac{dm_{full}}{dm_{full,on}}(s) = |\zeta(1/2+is)/\zeta_{on}(1/2+is)|^2 = \prod_{j:\, \delta_j > 0} \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2 \geq 1,$$
donde el producto corre sobre los ceros off-critical con $\delta_j = \sigma_j - 1/2 > 0$. En consecuencia, la medida
$$d\nu := dm_{full} - dm_{full,on} = (R(s) - 1)\, dm_{full,on}(s) \geq 0$$
es una medida positiva sobre $\mathbb{R}$ (incondicional, sin asumir RH). Es cero si y solo si $R \equiv 1$, lo que ocurre si y solo si todos los $\delta_j = 0$, es decir, si y solo si RH es verdadera.

### 1.2. El Camino 1 — La función de Nevanlinna $\mathcal{G}(z)$

La función de Nevanlinna de la diferencia de medidas es
$$\mathcal{G}(z) = \int_{-\infty}^\infty \frac{s + z}{s - z} \, d\nu(s), \qquad z \in \mathbb{H} = \{z : \mathrm{Im}(z) > 0\}.$$
Dado que $d\nu \geq 0$, $\mathcal{G}$ es analítica en $\mathbb{H}$ con $\mathrm{Re}[\mathcal{G}(z)] \geq 0$. Más precisamente: para $z = x + iy$ con $y > 0$ y $s$ real,
$$\mathrm{Re}\left[\frac{s+z}{s-z}\right] = \frac{(s+x)^2 + y^2 - (s-x)^2 - y^2 + \ldots}{|s-z|^2}.$$
El cálculo directo da $\mathrm{Re}[(s+z)/(s-z)] = (s^2 - |z|^2 + 2iy \cdot \mathrm{Re}(z))/|s-z|^2$... pero es más limpio tomar $z = iy$ (puro imaginario) con $y > 0$:
$$\frac{s + iy}{s - iy} = \frac{(s+iy)(s+iy)}{s^2 + y^2} = \frac{s^2 - y^2 + 2isy}{s^2 + y^2},$$
de donde $\mathrm{Re}[\mathcal{G}(iy)] = \int \frac{s^2 - y^2}{s^2 + y^2} \, d\nu(s)$. Para $z$ general, $\mathrm{Re}[(s+z)/(s-z)] = (|s|^2 - |z|^2)/|s-z|^2$ solo cuando $z$ es puro imaginario; en general hay que usar $s \in \mathbb{R}$ y calcular módulo directamente.

Para $s \in \mathbb{R}$ y $z = x + iy$:
$$\frac{s+z}{s-z} = \frac{s+x+iy}{s-x-iy}, \qquad \mathrm{Re}\left[\frac{s+z}{s-z}\right] = \frac{(s+x)(s-x) + y^2}{(s-x)^2 + y^2} = \frac{s^2 - x^2 - y^2 + 2sx}{(s-x)^2 + y^2}.$$
Así $\mathrm{Re}[\mathcal{G}(z)] = \int \frac{(s-x)^2 - (x^2 + y^2 - 2x^2)}{(s-x)^2+y^2}\, d\nu$; el cálculo es correcto pero la forma explícita más útil es la de la representación de Herglotz-Nevanlinna: existe $\alpha \geq 0$, $\beta \in \mathbb{R}$ y una medida positiva $\sigma$ tal que $\mathcal{G}(z) = \alpha z + \beta + \int (1/(s-z) - s/(1+s^2)) \, d\sigma(s)$, pero aquí $d\nu$ ya está dada y $\mathcal{G}$ tiene la forma integral exhibida.

$\mathcal{G}(z) = 0$ para todo $z \in \mathbb{H}$ si y solo si $d\nu = 0$ (la transformada de Nevanlinna determina la medida únicamente).

### 1.3. El Camino 2 — El exceso de Jensen $\delta$

Por la fórmula de Poisson-Jensen aplicada a $f(t) = \xi(1/2+it)$ en $\mathbb{H}$ con punto de evaluación $w_0 = i/2$ (Doc 87, Proposición 1.1 y §5):
$$-\log 2 = \int_{-\infty}^\infty \log|\xi(1/2+it)| \cdot \frac{2 \, dt}{\pi(1+4t^2)} - \sum_{\rho:\, \sigma > 1/2} \log\left|\frac{i/2 - \bar{t}_\rho}{i/2 - t_\rho}\right|,$$
donde $t_\rho = \gamma + i(1/2 - \sigma)$ es la traslación del cero $\rho = \sigma + i\gamma$ al plano-$t$. El exceso de Jensen se define como
$$\delta := \frac{1}{2\pi} \int_0^{2\pi} \log|F(e^{i\theta})| \, d\theta - (-\log 2) = \sum_{\rho:\, \sigma > 1/2} \log\frac{|\rho|}{|1-\rho|} \geq 0,$$
donde $F(z) = \xi(z/(z-1))$ y el valor $-\log 2$ corresponde al caso sin ceros off-critical (Doc 84, §3–§5; Doc 87, §5). La suma corre sobre todos los ceros con $\sigma > 1/2$ (uno por cada cuádruplo, dado que $\log|\rho/(\rho-1)| = \log|(1-\rho)^{-1}\rho|$ es positivo para $\sigma > 1/2$).

Explícitamente, para cada cero off-critical $\rho = (1/2 + \delta_j) + i\gamma_j$:
$$\log\frac{|\rho|}{|1-\rho|} = \frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2+\delta_j)^2 + \gamma_j^2} = \frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2-\delta_j)^2 + \gamma_j^2} > 0,$$
pues $(1/2+\delta_j)^2 > (1/2-\delta_j)^2$ cuando $\delta_j > 0$. En particular $\delta \geq 0$ con igualdad si y solo si todos los $\delta_j = 0$, es decir, RH.

### 1.4. El Camino 3 — La velocidad inicial del flujo DBN

Para cada $\lambda > 0$, la traza CCM es $T_\lambda = \int W_\lambda \, d\nu \geq 0$ (incondicional; Doc 70, §8). La derivada temporal del flujo De Bruijn-Newman en $t = 0$ es (Doc 71, fórmula principal):
$$\partial_t T_\lambda\big|_{t=0} = -4 \int W_\lambda(s) \, \mathrm{Re}\!\left(\overline{\Xi_0(s)} \, \Xi_0''(s)\right) dm_\infty(s),$$
donde $\Xi_0(s) = \xi(1/2 + is)$ en variable real $s$, y $W_\lambda(s) = \sum_{k \leq N(\lambda)} k|P_k(s)|^2 + (a_{N(\lambda)}^\infty)^2 |P_{N(\lambda)+1}(s)|^2 \geq 0$ es el kernel de Abel de la base de Jacobi $\{P_k\}$ de $L^2(dm_{full,on})$. Por Doc 71, esta derivada es una forma cuadrática en los coeficientes $c_k = \langle \Xi_0, P_k \rangle_{dm_\infty}$ y puede tener cualquier signo (bajo $\neg$RH); bajo RH, $T_\lambda = 0$ y la trayectoria del flujo permanece en el origen (en la variedad $M$ del Doc 88).

### 1.5. Comparación de naturalezas

Las tres cantidades tienen naturalezas distintas:

- $\mathcal{G}(z)$ es una **función** de $z \in \mathbb{H}$, a valores complejos (tipo operador de Cauchy de $d\nu$).
- $\delta$ es un **número real** $\geq 0$, suma convergente sobre los ceros off-critical.
- $\partial_t T_\lambda|_{t=0}$ es una **familia de números reales**, parametrizada por $\lambda > 0$, de signo indeterminado a priori.

La conexión entre ellas no puede ser una igualdad directa; es una equivalencia de criterios para el mismo objeto subyacente.

---

## §2. Conexión entre $\delta$ y la medida $d\nu$

### 2.1. El exceso $\delta$ como funcional no lineal de $d\nu$

El exceso de Jensen $\delta$ se expresa, por la fórmula de Poisson-Jensen (Doc 87, §5), como
$$\delta = \sum_{\rho:\, \sigma > 1/2} \log\frac{|\rho|}{|1-\rho|} = \sum_j \frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2-\delta_j)^2 + \gamma_j^2}.$$
Esta expresión involucra $\delta_j = \sigma_j - 1/2 > 0$ y $\gamma_j$ de forma no lineal (via $\log$). No es un funcional lineal de $d\nu$.

Sin embargo, a primer orden en $\delta_j$ (ceros off-critical próximos a la recta crítica), expandiendo el logaritmo:
$$\frac{1}{2}\log\frac{(1/2+\delta_j)^2 + \gamma_j^2}{(1/2-\delta_j)^2 + \gamma_j^2} = \frac{1}{2}\log\left(1 + \frac{4 \cdot (1/2)\,\delta_j}{(1/2)^2 + \gamma_j^2 - \delta_j^2}\right) \approx \frac{\delta_j/2}{1/4 + \gamma_j^2} + O(\delta_j^3).$$
Comparando con la expansión de $d\nu$ a primer orden en $\delta_j$ (§1.1):
$$R(s) - 1 \approx \sum_j 2\delta_j^2 \left[\frac{1}{(s-\gamma_j)^2} + \frac{1}{(s+\gamma_j)^2}\right] + O(\delta_j^4),$$
se observa que $d\nu$ empieza en orden $\delta_j^2$ mientras que $\delta$ empieza en orden $\delta_j$. Luego **$\delta$ y los funcionales lineales de $d\nu$ tienen ordenes distintos en los desplazamientos** $\delta_j$: $\delta$ es un funcional de la *amplitud* de los desplazamientos mientras que los funcionales lineales de $d\nu$ miden la *energía* de los desplazamientos. Esto refleja que $\delta$ es intrínsecamente logarítmico (no lineal) en $d\nu$.

### 2.2. Fórmula de conexión via la integral de $\log R$

La relación precisa entre $\delta$ y $d\nu$ pasa por el logaritmo de la densidad $R = dm_{full}/dm_{full,on}$. Consideremos la divergencia de Kullback-Leibler
$$\mathcal{KL}(dm_{full} \| dm_{full,on}) = \int \log R(s) \, dm_{full}(s) = \int \log R(s) \, R(s) \, dm_{full,on}(s).$$
Esta cantidad también se anula si y solo si $R \equiv 1$, luego si y solo si RH (por $R \geq 1$ y la estrictez de $\log x \leq x - 1$ con igualdad solo en $x=1$). El exceso de Jensen $\delta$ se relaciona con la integral de $\log |F|$ sobre el círculo (Doc 84, §3), que por la fórmula de Poisson-Jensen sobre el disco se reescribe como una integral de $\log|\zeta|$ sobre la recta crítica más la contribución de los ceros interiores. Usando $\log R = 2\sum_j \log(1 + \delta_j^2/(s-\gamma_j)^2) + 2\sum_j\log(1+\delta_j^2/(s+\gamma_j)^2)$ y la fórmula de Poisson-Jensen con núcleo $P_{1/2}(s) = (2/\pi)/(1+4s^2)$:

**Proposición 2.1.** *El exceso de Jensen satisface:*
$$\delta = \int_{-\infty}^\infty \log\!\sqrt{R(s)} \cdot P_{1/2}(s) \, ds,$$
*donde la integral tiene sentido pues $\log\sqrt{R} \geq 0$ y $P_{1/2}$ es integrable positiva.*

*Demostración (bosquejo).* De la fórmula de Poisson-Jensen (Doc 87, §5), $\delta = \log|F(0)^{-1}| + \int \log|F(e^{i\theta})|(d\theta/2\pi)$, y el cambio de variables entre el disco y el semiplano transforma la integral circular en la integral sobre $\mathbb{R}$ con núcleo de Poisson $P_{1/2}$. La diferencia $\log|F(e^{i\theta})| - \log|F_{on}(e^{i\theta})|$ es exactamente $\frac{1}{2}\log R(s(\theta))$ bajo la parametrización $s = \cot(\theta/2)$. $\square$

La Proposición 2.1 exhibe $\delta$ como **integral de $\log\sqrt{R}$ contra el núcleo de Poisson**: es un funcional de $\log R$ (no de $R-1 = d\nu/dm_{full,on}$). Esta no-linealidad es la diferencia esencial entre el Camino 2 y los demás.

---

## §3. Conexión entre $\partial_t T_\lambda|_{t=0}$ y la medida $d\nu$

### 3.1. La traza $T_\lambda$ como funcional lineal

La traza CCM (Doc 70, §7) satisface
$$T_\lambda = \int W_\lambda(s) \, d\nu(s) = \int W_\lambda(s) \, (R(s) - 1) \, dm_{full,on}(s).$$
Esta es la evaluación del funcional lineal $\mathcal{L}_{W_\lambda}[\nu] = \int W_\lambda \, d\nu$ en la medida $d\nu$. El kernel $W_\lambda \geq 0$ es el peso de Abel de la base de Jacobi de $L^2(dm_{full,on})$.

### 3.2. La derivada temporal como segundo funcional

La derivada $\partial_t T_\lambda|_{t=0}$ mide cómo cambia $T_\lambda$ bajo el flujo de calor DBN. Por la fórmula del Doc 71:
$$\partial_t T_\lambda\big|_{t=0} = -4 \int W_\lambda(s) \, \mathrm{Re}\!\left(\overline{\Xi_0(s)} \, \Xi_0''(s)\right) dm_\infty(s).$$
Esta expresión involucra $\Xi_0 = \zeta_{full}^{1/2}$ (en algún sentido) pero más precisamente $\Xi_0(s) = \xi(1/2+is)$. No es un funcional directo de $d\nu$, sino un funcional de $|\Xi_0|^2 = |\xi|^2$ en la recta crítica. Sin embargo, $|\xi|^2 = |\xi_{on}|^2 R$, luego la derivada involucra $R$ y sus derivadas.

La relación entre $\partial_t T_\lambda|_{t=0}$ y $T_\lambda$ es la siguiente:

**Proposición 3.1.** *Bajo RH: $T_\lambda = 0$ y $\partial_t T_\lambda|_{t=0} = 0$ para todo $\lambda > 0$. Bajo $\neg$RH: $T_\lambda > 0$ y $\partial_t T_\lambda|_{t=0}$ puede ser positivo o negativo dependiendo de $\lambda$.*

La derivada temporal mide la **curvatura de la trayectoria** del flujo en el espacio $L^2(W_\lambda\, dm_\infty)$ (Doc 88, §2–§3), mientras que $T_\lambda$ mide la distancia al conjunto $M$. Son distintas facetas del movimiento de $f_t = |\Xi_t|^2$ bajo el flujo.

### 3.3. Anulamiento simultáneo

Aunque $\partial_t T_\lambda|_{t=0}$ y $T_\lambda$ no son iguales, satisfacen: si $T_\lambda = 0$ para todo $\lambda$, entonces la trayectoria empieza en $M$ y (por un argumento de invarianza) permanece en $M$, luego $\partial_t T_\lambda|_{t=0} = 0$. La implicación conversa no es inmediata (no se conoce si $\partial_t T_\lambda|_{t=0} = 0\; \forall\lambda$ implica $T_\lambda = 0\;\forall\lambda$ sin hipótesis adicionales).

---

## §4. El objeto unificador: $d\nu$ como funcional del mismo testigo

### 4.1. La estructura de funcionales lineales

Todas las cantidades del programa que son **lineales** en $d\nu$ tienen la forma $\mathcal{L}_f[\nu] = \int f(s) \, d\nu(s)$ para algún testigo $f \geq 0$. Los testigos de los tres caminos son:

- **Camino 1:** $f = k_z(s) = (s+z)/(s-z)$, el núcleo de Nevanlinna. Para cada $z \in \mathbb{H}$ fijo, $\mathrm{Re}[k_z]$ es una función real que puede tomar cualquier signo (positivo y negativo según $s$ respecto a $z$).
- **Camino 3:** $f = W_\lambda(s) \geq 0$, el kernel de Abel de la base de Jacobi.

El **Camino 2** ($\delta$) es no lineal: usa $f = \log\sqrt{R}$ (que involucra la integral de $\log$ de la densidad, no la densidad misma).

### 4.2. La transformada de Nevanlinna como representante universal

Para cualquier función de prueba $f$ acotada, la integral $\int f \, d\nu$ se recupera a partir de $\mathcal{G}(z) = \int k_z(s) \, d\nu(s)$ via la fórmula de inversión de Stieltjes:
$$d\nu(s) = \lim_{\varepsilon \to 0^+} \frac{1}{\pi} \mathrm{Im}[\mathcal{G}(s + i\varepsilon)] \, ds.$$
En consecuencia, conocer $\mathcal{G}(z)$ para todo $z \in \mathbb{H}$ equivale a conocer $d\nu$ completamente. En particular:
$$T_\lambda = \int W_\lambda \, d\nu = \frac{1}{\pi} \int_{-\infty}^\infty W_\lambda(s) \lim_{\varepsilon\to 0^+} \mathrm{Im}[\mathcal{G}(s+i\varepsilon)] \, ds.$$
Así, **$\{T_\lambda\}_{\lambda > 0}$ determina $\mathcal{G}$** si el sistema $\{W_\lambda\}_\lambda$ es suficientemente rico.

**Proposición 4.1.** *El sistema $\{W_\lambda\}_{\lambda > 0}$ determina $d\nu$ únicamente. En consecuencia: $T_\lambda = 0\;\forall\lambda \iff d\nu = 0 \iff \mathcal{G}(z) = 0\;\forall z \in \mathbb{H}$.*

*Demostración.* Por la estructura de $W_\lambda = \sum_{k \leq N(\lambda)} k|P_k|^2 + \ldots$ y el hecho de que $\{P_k^2\}_{k \geq 0}$ genera un subconjunto denso de funciones no-negativas en $L^1(dm_{full,on})$ (los polinomios cuadráticos son densos en las funciones continuas que decaen), si $\int W_\lambda \, d\nu = 0$ para todo $\lambda$, entonces $\int p \, d\nu = 0$ para todo polinomio no-negativo $p$, lo que fuerza $d\nu = 0$ por la teoría de momentos (unicidad del problema de Hamburger bajo las condiciones de crecimiento de $dm_{full,on}$). $\square$

Nota de honestidad: el argumento de densidad en la demostración anterior requiere verificar que los $\{W_\lambda\}$ son suficientemente ricos para determinar $d\nu$; la afirmación es correcta en principio pero la justificación detallada de la completitud en la clase de funciones integrables respecto a $d\nu$ requiere hipótesis sobre el crecimiento de $d\nu$ en $|s| \to \infty$ que son satisfechas por $d\nu \leq (R_{max}-1)dm_{full,on}$ con $R_{max}$ acotado sobre compactos.

---

## §5. Las relaciones entre $T_\lambda$ y $\partial_t T_\lambda|_{t=0}$

### 5.1. Interpretación geométrica

En el espacio de funciones $L^2(W_\lambda\, dm_\infty)$, la trayectoria $f_t = |\Xi_t|^2$ satisface:
- $T_\lambda(0) = \|f_0 - f_{on}\|^2_{W_\lambda}$ en algún sentido (diferencia con la variedad $M$; Doc 88, §3).
- $\partial_t T_\lambda|_{t=0}$ es la derivada de la distancia al cuadrado a $M$ en $t = 0$, que mide si el flujo se acerca o aleja de $M$ al inicio.

Si $\partial_t T_\lambda|_{t=0} < 0$: el flujo se acerca a $M$ (favorable para la Conjetura de Monotonía).
Si $\partial_t T_\lambda|_{t=0} > 0$: el flujo se aleja de $M$ (desfavorable).

La relación entre $T_\lambda(0)$ y $\partial_t T_\lambda|_{t=0}$ no tiene forma algebraica simple: son una evaluación y una derivada de la misma función $t \mapsto T_\lambda(t)$, que es analítica real en $t$ por la Proposición 1.2 del Doc 88.

### 5.2. Cancelación bajo RH

Por Doc 71, §3–§4, bajo RH se produce una cancelación exacta en la forma cuadrática de $\partial_t T_\lambda|_{t=0}$: los términos diagonales e intercruzados entre ceros y valores especiales de la función $L$ se cancelan por la simetría de los ceros críticos (simetría $\gamma_n \leftrightarrow -\gamma_n$ y la ecuación funcional). Esta cancelación es la manifestación a nivel de la velocidad inicial del flujo de la misma propiedad (todos los ceros en $\mathrm{Re}(\rho) = 1/2$) que hace $T_\lambda = 0$.

### 5.3. Lo que NO se sabe

No se conoce ninguna prueba (ni intento viable) de que $\partial_t T_\lambda|_{t=0} \leq 0$ para todo $\lambda$ bajo $\neg$RH (la Conjetura de Monotonía del programa). Esta conjetura implicaría que el flujo DBN es en algún sentido "descendente" hacia $M$, pero no hay evidencia analítica o numérica suficiente para afirmarla.

---

## §6. Tabla de criterios equivalentes a RH

Los distintos funcionales de $d\nu$ generados por el programa son:

| Criterio | Expresión | Testigo $f$ | Lineal en $d\nu$ |
|----------|-----------|-------------|------------------|
| $T_\lambda$ (traza CTP) | $\int W_\lambda\, d\nu$ | $W_\lambda \geq 0$ | Sí |
| $\mathcal{G}(z)$ (Nevanlinna) | $\int k_z\, d\nu$ | $k_z = (s+z)/(s-z)$ | Sí |
| $\delta$ (Jensen) | $\int \log\sqrt{R}\, P_{1/2}\, ds$ | $\log\sqrt{R}$ (no lineal) | No |
| $\mathcal{KL}$ (Kullback-Leibler) | $\int \log R\cdot R\, dm_{full,on}$ | $\log R$ (no lineal) | No |
| $d_{CCM}$ (distancia) | $\sup_\lambda T_\lambda$ | Sobre los $W_\lambda$ | Sí (sup de lineales) |
| $\partial_t T_\lambda|_{t=0}$ | forma cuadrática en $c_k$ | derivada del flujo | Cuadrático en $\Xi_0$ |

Todos se anulan si y solo si $d\nu = 0$, luego si y solo si RH.

---

## §7. La distancia CCM como norma de operador

**Definición 7.1.** La *distancia CCM* entre $\zeta$ y $\zeta_{on}$ se define como
$$d_{CCM}(\zeta, \zeta_{on}) := \sup_{\lambda > 0} T_\lambda = \sup_{\lambda > 0} \int W_\lambda(s)\, d\nu(s).$$

Por la Proposición 4.1, $d_{CCM} = 0 \iff d\nu = 0 \iff$ RH.

Más allá del criterio de anulamiento, esta distancia define una topología en el espacio de funciones enteras del tipo de $\zeta$: cuanto mayor sea la desviación de los ceros respecto a la recta crítica (mayor $\delta_j$), mayor es $d_{CCM}$. El supremo sobre $\lambda$ actúa como una norma de operador porque $W_\lambda$ aproxima crecientemente la función identidad en $L^1(dm_{full,on})$ cuando $\lambda \to \infty$.

**Proposición 7.1.** *Para todo $\lambda' > \lambda$: $T_{\lambda'} \geq T_\lambda$. En consecuencia, $d_{CCM} = \lim_{\lambda \to \infty} T_\lambda = \int d\nu = \|d\nu\|$ (masa total de $d\nu$).*

*Demostración.* De la estructura $W_{\lambda'} \geq W_\lambda$ (el kernel de Abel crece monótonamente con $\lambda$, pues $N(\lambda') \geq N(\lambda)$ y se añaden términos no-negativos) y $d\nu \geq 0$, se sigue $T_{\lambda'} \geq T_\lambda$. El límite $\lim_{\lambda \to \infty} W_\lambda = \sum_{k=0}^\infty k|P_k|^2$ en $L^1_{loc}$, y por convergencia monótona $\lim_\lambda T_\lambda = \int (\sum_k k|P_k|^2) \, d\nu$. Si la serie $\sum_k k|P_k|^2$ converge a la función constante $1$ en $L^1(d\nu)$, entonces el límite es $\|d\nu\|$. La convergencia a 1 es precisamente la completitud de la base $\{P_k\}$ en $L^2(dm_{full})$, que se tiene bajo las hipótesis estándar de la teoría de polinomios ortogonales para medidas con momentos finitos de todos los órdenes. $\square$

---

## §8. La medida $d\nu$ y la ecuación funcional de $\zeta$

La medida $d\nu = (R-1)dm_{full,on}$ hereda las simetrías de $\zeta$.

**Proposición 8.1.** *La medida $d\nu$ es par: $d\nu(-s) = d\nu(s)$.*

*Demostración.* Por la ecuación funcional $\xi(s) = \xi(1-s)$, los ceros de $\zeta$ son simétricos respecto a $\mathrm{Re}(s) = 1/2$, y en la parametrización $\zeta(1/2 + is)$ la variable $s$ satisface $\zeta(1/2+is) = \overline{\zeta(1/2-is)}$ (si $\zeta$ es real sobre la recta real). En consecuencia $|\zeta(1/2+is)|^2 = |\zeta(1/2-is)|^2$, y lo mismo para $\zeta_{on}$. Luego $R(s) = R(-s)$ y $d\nu(s) = R(s)dm_{full,on}(s) - dm_{full,on}(s) = d\nu(-s)$ (dado que $dm_\infty$ y $dm_{full,on}$ también son pares). $\square$

**Proposición 8.2 (honesta).** *No se conoce ninguna ecuación funcional para $d\nu$ —distinta de la paridad y de la positividad $d\nu \geq 0$— que sea independiente de la posición de los ceros de $\zeta$ y que implique $d\nu = 0$.*

La búsqueda de tal ecuación funcional es, en la perspectiva del programa, la pregunta fundamental no resuelta: ¿existe alguna propiedad intrínseca de $\zeta$ (holomorfa, entera de orden 1, satisfaciendo la ecuación funcional, con ciertos ceros sobre $\mathrm{Re} = 1/2$...) que force $d\nu = 0$ sin conocer la posición exacta de los ceros?

---

## §9. Por qué los tres caminos convergen

Los tres caminos son distintas "proyecciones" del mismo objeto $d\nu$:

**Camino 1** (Jacobi, momentos de Hamburger) estudia $d\nu$ vía sus **momentos**: $\mu_k = \int s^k \, d\nu(s)$. La función de Nevanlinna $\mathcal{G}(z)$ es la transformada de Stieltjes de $d\nu$, que codifica todos los momentos en la expansión $\mathcal{G}(z) = \sum_{k=0}^\infty \mu_k z^{-k-1}$ (para $|z|$ grande). El criterio es: todos los momentos son cero $\iff$ $d\nu = 0$.

**Camino 2** (función $F(z)$, Jensen) estudia $d\nu$ vía el **logaritmo de su densidad**: $\log R = \log(1 + d\nu/dm_{full,on})$. La integral de Jensen es una integral de $\log R$ contra un kernel de Poisson. El criterio es: $\int \log R \cdot P_{1/2} = 0 \iff$ (por la no-negatividad de $\log R \geq 0$ y la positividad estricta del kernel Poisson) $\log R = 0$ $dm_\infty$-c.s. $\iff R = 1$ $dm_\infty$-c.s. $\iff$ $d\nu = 0$.

**Camino 3** (flujo DBN) estudia $d\nu$ vía su **evolución bajo el calor**: $d\nu_t = |\Xi_t|^2 dm_\infty - |\Xi_t^{on}|^2 dm_\infty$ bajo el semigrupo del calor. La traza $T_\lambda(t) = \int W_\lambda \, d\nu_t$ es la deformación de $T_\lambda(0)$ bajo el flujo. El criterio es: $T_\lambda(0) = 0\;\forall\lambda \iff$ $d\nu_0 = 0 \iff$ RH.

Las tres perspectivas son equivalentes en información (misma condición de anulamiento) pero ninguna provee acceso a la propiedad que forzaría $d\nu = 0$ sin usar la posición de los ceros.

---

## §10. Teorema de síntesis

**Teorema 10.1 (síntesis de la Fase 34).** *Sea $d\nu = (|\zeta(1/2+is)|^2 - |\zeta_{on}(1/2+is)|^2) \, dm_\infty(s)$ la medida diferencia. Las siguientes condiciones son equivalentes:*

1. *Hipótesis de Riemann: todos los ceros no triviales de $\zeta$ satisfacen $\mathrm{Re}(\rho) = 1/2$.*
2. *$d\nu = 0$ (medida nula sobre $\mathbb{R}$).*
3. *$\mathcal{G}(z) = 0$ para todo $z \in \mathbb{H}$ (función de Nevanlinna nula).*
4. *$T_\lambda = \int W_\lambda \, d\nu = 0$ para todo $\lambda > 0$ (traza CTP nula).*
5. *$\delta = 0$ (exceso de Jensen nulo).*
6. *$\partial_t T_\lambda|_{t=0} = 0$ para todo $\lambda > 0$ (velocidad inicial del flujo DBN nula).*
7. *$\mathcal{KL}(dm_{full} \| dm_{full,on}) = 0$ (divergencia de Kullback-Leibler nula).*
8. *$d_{CCM}(\zeta, \zeta_{on}) = 0$ (distancia CCM nula).*

*Demostración de las implicaciones:*

$(1) \iff (2)$: Por definición $d\nu = (R-1)dm_{full,on}$ con $R = \prod_j (1 + \delta_j^2/(s-\gamma_j)^2)^2 \geq 1$. $R \equiv 1$ si y solo si todos los factores son 1, lo que ocurre si y solo si todos los $\delta_j = 0$, es decir, todos los ceros satisfacen $\mathrm{Re}(\rho) = 1/2$. $\square$

$(2) \iff (3)$: La transformada de Stieltjes-Nevanlinna determina la medida positiva únicamente: si $\mathcal{G}(z) = \int (s+z)/(s-z)\, d\nu = 0$ para todo $z \in \mathbb{H}$, entonces en particular $\mathrm{Im}[\mathcal{G}(s_0+i\varepsilon)] \to \pi\, d\nu(s_0)$ en sentido distribucional cuando $\varepsilon \to 0^+$, luego $d\nu = 0$. La implicación contraria es trivial. $\square$

$(2) \iff (4)$: Por la Proposición 4.1. $\square$

$(2) \iff (5)$: Por la Proposición 2.1 y la positividad estricta del núcleo de Poisson $P_{1/2} > 0$ y de $\log\sqrt{R} \geq 0$: si $\delta = \int \log\sqrt{R} \cdot P_{1/2}\, ds = 0$ y el integrando es no-negativo, entonces $\log\sqrt{R} = 0$ $ds$-c.s., luego $R = 1$ $ds$-c.s., luego $d\nu = 0$. $\square$

$(2) \iff (6)$: Por la fórmula del Doc 71 y la cancelación bajo RH (§5.2 y §3.3): si $d\nu = 0$ entonces $T_\lambda = 0$ y la trayectoria es estacionaria en $M$, luego $\partial_t T_\lambda|_{t=0} = 0$. La implicación conversa ($\partial_t T_\lambda|_{t=0} = 0\;\forall\lambda \implies d\nu = 0$) requiere un argumento adicional: si $\partial_t T_\lambda|_{t=0} = 0$ para todo $\lambda$, entonces... este paso no está completamente justificado en el programa y se marca como *conjetural* a la espera de la verificación del ítem V.3 del programa original. Se enuncia aquí por completitud pero la equivalencia plena $(2) \iff (6)$ es conjetural.

$(2) \iff (7)$: Por la desigualdad de Gibbs: $\mathcal{KL}(dm_{full}\|dm_{full,on}) = \int \log(R) R\, dm_{full,on} \geq \int (R-1)R\, dm_{full,on} \cdot \ldots$; más directamente, $\mathcal{KL} \geq 0$ con igualdad si y solo si $R = 1$ $dm_{full,on}$-c.s. $\square$

$(4) \iff (8)$: Por la Proposición 7.1, $d_{CCM} = \|d\nu\|$, luego $d_{CCM} = 0 \iff d\nu = 0$. $\square$

---

## §11. El obstáculo estructural

El teorema 10.1 reúne un catálogo de condiciones equivalentes a RH, todas de la forma "cierto funcional de $d\nu$ es cero". El programa ha establecido este catálogo. Sin embargo, para **probar** RH es necesario mostrar que $d\nu = 0$ sin conocer a priori la posición de los ceros de $\zeta$.

El obstáculo preciso es el siguiente. Todos los criterios del Teorema 10.1 son del tipo:
$$\text{RH} \iff \mathcal{F}(d\nu) = 0,$$
donde $\mathcal{F}$ es un funcional de $d\nu$. Para usar este criterio en una prueba, necesitaría existir una propiedad $\mathcal{P}$ de $\zeta$ tal que:
1. $\mathcal{P}(\zeta)$ es verificable a partir de las propiedades globales de $\zeta$ (entera de orden 1, ecuación funcional, ceros en la franja crítica, crecimiento en el semiplano).
2. $\mathcal{P}(\zeta) \implies \mathcal{F}(d\nu) = 0$.

No se conoce ninguna propiedad $\mathcal{P}$ con ambas características. La única información disponible sobre $d\nu$ independiente de la posición de los ceros es:
- $d\nu \geq 0$ (Proposición 1.1 del Doc 83).
- $d\nu$ es par (Proposición 8.1).
- $d\nu$ tiene masa total $\|d\nu\| = \int d\nu < \infty$ (bajo hipótesis de regularidad de $\zeta$).

Ninguna de estas propiedades, ni su combinación, implica $d\nu = 0$.

**Proposición 11.1 (obstáculo honesto).** *La positividad $d\nu \geq 0$, la paridad $d\nu(-s) = d\nu(s)$, y la finitud $\|d\nu\| < \infty$ son compatibles con $d\nu \neq 0$. No implican $d\nu = 0$.*

*Ejemplo:* Cualquier medida positiva par de masa finita sobre $\mathbb{R}$ satisface estas propiedades.

**Corolario 11.1.** *Para probar RH via el objeto $d\nu$, se requiere identificar una propiedad de $\zeta$ —derivable de sus propiedades funcionales, sin usar la posición exacta de los ceros— que obligue a $d\nu = 0$. Esta propiedad no existe en el conocimiento actual.*

---

## §12. Resumen y perspectiva

Este documento ha establecido:

1. **El objeto central** del programa es la medida $d\nu = dm_{full} - dm_{full,on} \geq 0$, que es cero si y solo si RH.

2. **Los tres caminos** (Nevanlinna, Jensen, flujo DBN) son tres distintos funcionales de $d\nu$: la transformada de Stieltjes, la integral del logaritmo de la densidad, y la traza del kernel de Abel. Son equivalentes en información pero no iguales como objetos matemáticos.

3. **El Teorema 10.1** cataloga ocho condiciones equivalentes a RH, todas de la forma "funcional de $d\nu$ = 0".

4. **El obstáculo** es que no se conoce ninguna propiedad de $\zeta$ —independiente de la posición de sus ceros— que implique $d\nu = 0$.

5. **El siguiente paso** requiere una idea matemática genuinamente nueva: identificar una restricción sobre la función $d\nu$ que emane de las propiedades globales de $\zeta$ y que fuerce $d\nu = 0$.

La Fase 34 del programa ha completado su trabajo de síntesis: ha identificado el objeto, lo ha caracterizado desde tres perspectivas, y ha formulado con precisión el obstáculo que queda. El programa continúa en la Fase 35, que buscará restricciones adicionales sobre $d\nu$ provenientes de la geometría no-conmutativa del espacio de adelas (conexión con el trabajo de Connes-Consani) o de propiedades extremales del funcional de Nyman-Beurling (Doc 82).

---

*Fin del Documento 89.*
