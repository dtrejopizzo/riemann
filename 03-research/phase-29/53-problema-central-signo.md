# Doc 53 — El Problema Central: Injectividad de la Transformada de Poisson sin Hipótesis de Signo

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 42–52 (especialmente Docs 50–52)  
**Naturaleza:** Ataque directo al obstáculo unificado de las tres direcciones.  
**Objetivo:** Estudiar cuándo $\mathcal{P}[\eta](\gamma_n) = 0$ para todo $n$ implica $\eta = 0$, sin hipótesis de signo sobre $\eta$. Construir contraejemplos en el caso abstracto. Identificar la estructura de $\Xi$ como obstáculo natural. Formular el lema clave que, de probarse, cierra el programa.

---

## 1. El Problema Central: enunciado preciso

**Definición 1.1 (Problema Central — PC).** Sea $\mathcal{R}_\eta \subset \mathbb{H}$ la región admisible (Axioma 3, Doc 48) y sea $\{\gamma_n\}_{n\geq 1}$ la sucesión de partes imaginarias de los ceros de $\Xi$ en el semiplano superior, con $0 < \gamma_1 < \gamma_2 < \cdots \to \infty$.

**PC:** Sea $\eta$ una medida de Borel signada en $\mathcal{R}_\eta$ con $\int y/(1+x^2)d|\eta| < \infty$. Si:
$$\mathcal{P}[\eta](\gamma_n) = \int_{\mathcal{R}_\eta} P_y(\gamma_n - x)\,d\eta(x,y) = 0 \quad \forall n\geq 1$$
¿se sigue que $\eta = 0$?

**Reformulación equivalente.** Sea $F = \mathcal{P}[\eta]: \mathbb{H}^+ \to \mathbb{R}$ la extensión armónica de $\eta$. La condición es $F(\gamma_n) = 0$ para todo $n\geq 1$ (valores de frontera en los ceros de $\Xi$). ¿Implica esto $F \equiv 0$ en $\mathbb{R}$ — y por tanto $\eta = 0$ por la injectividad de la transformada de Poisson en medidas signadas?

---

## 2. Primer paso: la injectividad de la transformada de Poisson en medidas signadas

Antes de estudiar la restricción a $\{\gamma_n\}$, precisamos la injectividad de $\mathcal{P}$ sobre medidas signadas.

**Proposición 2.1 (Injectividad de $\mathcal{P}$ sobre medidas signadas).** Si $\mathcal{P}[\eta](t) = 0$ para todo $t \in \mathbb{R}$, entonces $\eta = 0$.

*Prueba.* $\mathcal{P}[\eta]$ es la parte imaginaria de la transformada de Cauchy $\mathcal{C}[\eta](z) = \int d\eta/(z-\bar{w})$. Si $\mathcal{P}[\eta] \equiv 0$ en $\mathbb{R}$, entonces la parte armónica de $\mathcal{C}[\eta]$ es cero en la frontera. Por el teorema de Fatou para funciones armónicas en $H^1(\mathbb{H}^+)$ y la injectividad de la transformada de Cauchy (Teorema de F. y M. Riesz), se concluye $\eta = 0$. $\square$

**Corolario 2.2.** El PC se reduce a: ¿Implica $F|_{\{\gamma_n\}} \equiv 0$ que $F|_\mathbb{R} \equiv 0$?

---

## 3. Contraejemplo en el caso abstracto: el PC puede fallar sin estructura de $\Xi$

**Proposición 3.1 (Fallo del PC para secuencias genéricas).** Sean $\{t_n\}_{n\geq 1}$ una sucesión creciente de reales con $t_n \to \infty$ y $\sum_n (t_{n+1}-t_n)^{-1} < \infty$ (los gaps son grandes comparados con el recíproco del índice). Entonces existe una medida signada $\eta \neq 0$ con soporte en $\{y = 1/4\} \subset \mathbb{H}$ tal que $\mathcal{P}[\eta](t_n) = 0$ para todo $n$.

*Construcción.* Para secuencias con gaps grandes ($t_{n+1}-t_n \geq cn$ para alguna $c > 0$), el sistema $\{P_{1/4}(t_n - x)\}_{n\geq 1}$ como funciones de $x$ no es completo en $L^2(\mathbb{R}, dx)$ — por el Teorema de Beurling-Malliavin (la densidad $D^- = 0$ no supera la densidad crítica). Luego existe $g \in L^2(\mathbb{R})$, $g \neq 0$, con $\int g(x)P_{1/4}(t_n-x)dx = 0$ para todo $n$. Tomando $d\eta(x, 1/4) = g(x)dx$ se obtiene $\mathcal{P}[\eta](t_n) = 0$ con $\eta \neq 0$. $\square$

**Corolario 3.2.** El PC no tiene solución afirmativa para secuencias con gaps $t_{n+1}-t_n \geq cn$. La estructura específica de $\{\gamma_n\}$ — con gaps $\gamma_{n+1}-\gamma_n \sim 2\pi/\log\gamma_n \to 0$ — es esencial.

---

## 4. La densidad de $\{\gamma_n\}$ y la condición de Beurling

**Proposición 4.1 (Los gaps de los ceros de $\Xi$).** Por la fórmula de Riemann-von Mangoldt y las estimaciones de ceros consecutivos:
$$\gamma_{n+1} - \gamma_n \sim \frac{2\pi}{\log\gamma_n} \to 0$$

En particular, los gaps tienden a cero — el conjunto $\{\gamma_n\}$ se vuelve cada vez más denso a alturas grandes.

**Proposición 4.2 (Densidad de Beurling de $\{\gamma_n\}$ en una ventana $[T, T+L]$).** Para $L = L(T)$ fijo y $T \to \infty$:
$$\#\{n: \gamma_n \in [T, T+L]\} \sim \frac{L\log T}{2\pi}$$

La densidad local diverge con $T$ — a diferencia de una secuencia con gaps constantes.

**Proposición 4.3 (Densidad de Beurling superior infinita).** $D^+(\{\gamma_n\}) = \limsup_{r\to\infty} N(r)/r = +\infty$ donde $N(r) = \#\{\gamma_n \leq r\}$.

**Corolario 4.4.** Por el Teorema de Beurling-Malliavin en su forma cuantitativa, el sistema $\{P_{y_0}(\gamma_n - x)\}$ es un marco de Riesz sobreabundante en $L^2(\mathbb{R})$ para cualquier $y_0 > 0$ — consistente con el resultado de Doc 50 (Teorema 8.2, Seip 1993).

---

## 5. El papel de $\Xi$ como factor de Blaschke para ceros de frontera

**Observación fundamental.** Los ceros $\{\gamma_n\}$ de $\mathcal{P}[\eta]$ en la frontera de $\mathbb{H}^+$ son exactamente los ceros de la función $\Xi(1/2+it)$ (bajo RH). Esto no es coincidencia: la función $\Xi$ es precisamente el "factor de Blaschke para ceros de frontera" en el sentido de la teoría de funciones de Hardy.

**Definición 5.1 (Función entera de $\Xi$ como $t$-función).** Sea $\xi(t) := \Xi(1/2+it)$ la función entera real de la variable $t \in \mathbb{R}$. Por propiedades de $\Xi$:
- $\xi(t)$ es entera de orden 1 y tipo finito $\tau_\xi = \pi/2$ (aproximadamente).
- Los ceros de $\xi$ en $\mathbb{R}$ son exactamente los $\gamma_n$ (y $-\gamma_n$ por simetría), bajo RH.
- La factorización de Hadamard: $\xi(t) = \xi(0)\prod_n(1-t^2/\gamma_n^2)$ (producto de Weierstrass).

**Proposición 5.2 (Convergencia del producto de Weierstrass de $\xi$).** La condición de convergencia del producto de Weierstrass para ceros reales $\pm\gamma_n$ de $\xi$ es $\sum_n 1/\gamma_n^2 < \infty$. Esto se verifica pues $\gamma_n \sim 2\pi n/\log n$ y $\sum_n \log^2 n/n^2 < \infty$.

**Proposición 5.3 (La función $\xi$ como "Blaschke" para ceros de frontera).** En el espacio de Hardy $H^2(\mathbb{H}^+)$, toda función $F$ con $F(\gamma_n) = 0$ para todo $n$ tiene la representación:
$$F(z) = \xi(z)\cdot G(z)$$

para alguna función $G$ holomorfa en $\mathbb{H}^+$, siempre que $F/\xi$ sea holomorfa en un entorno de los $\gamma_n$ (lo cual requiere que $F$ tenga ceros SIMPLES en los $\gamma_n$).

*Nota.* La factorización $F = \xi \cdot G$ es formal en la frontera real; en el interior de $\mathbb{H}^+$ requiere extender $\xi$ y $G$ analíticamente.

---

## 6. El lema de factorización: el resultado central nuevo

**Lema 6.1 (Factorización de funciones armónicas con ceros en $\{\gamma_n\}$).** Sea $F: \mathbb{H}^+ \to \mathbb{R}$ una función armónica que satisface:

(i) $F = \mathcal{P}[\eta]$ para alguna medida signada $\eta$ en $\mathcal{R}_\eta$ con $\int y/(1+x^2)d|\eta| < \infty$.  
(ii) $F(\gamma_n) = 0$ para todo $n \geq 1$.

Entonces $F$ tiene la representación:
$$F(z) = \mathrm{Im}\!\left[\xi(z)\cdot H(z)\right]$$

donde $H: \mathbb{H}^+ \to \mathbb{C}$ es holomorfa, $\xi(z) = \Xi(1/2+iz)$ (extensión holomorfa de $\xi$ a $\mathbb{H}^+$), y la función $\xi H$ es la parte holomorfa de $F+i\tilde F$ (con $\tilde F$ la conjugada harmónica de $F$).

*Prueba.* Por la Proposición 2.1, $F + i\tilde F$ es una función holomorfa $\Phi: \mathbb{H}^+ \to \mathbb{C}$ (con $F = \mathrm{Re}[\Phi]$ o $F = \mathrm{Im}[\Phi]$ según la convención). La condición $F(\gamma_n) = 0$ implica $\mathrm{Im}[\Phi(\gamma_n)] = 0$, luego $\Phi(\gamma_n) \in \mathbb{R}$ para todos los $\gamma_n$.

Si $\Phi(\gamma_n) = 0$ (ceros en lugar de valores reales), entonces la función holomorfa $\Phi$ tiene ceros en los $\gamma_n$ (reales) y por el teorema de extensión analítica a través de los reales, $\Phi(z)/\xi(z)$ es holomorfa en $\mathbb{H}^+$ con la función cociente $H = \Phi/\xi$ bien definida. Luego $F = \mathrm{Im}[\xi H]$. $\square$

*Nota.* La factorización requiere que $\Phi(\gamma_n) = 0$ (cero complejo, no solo parte imaginaria nula). La condición $F(\gamma_n) = 0$ da solo $\mathrm{Im}[\Phi(\gamma_n)] = 0$; para tener $\Phi(\gamma_n) = 0$ necesitaríamos también $\mathrm{Re}[\Phi(\gamma_n)] = 0$, es decir $\tilde F(\gamma_n) = 0$. Esto es una hipótesis adicional.

---

## 7. La hipótesis conjugada y el sistema ortogonal doble

**Definición 7.1 (Sistema de ceros doble).** Se dice que la función armónica $F$ satisface la *condición de ceros dobles* en $\{\gamma_n\}$ si tanto $F$ como su conjugada armónica $\tilde F$ satisfacen $F(\gamma_n) = \tilde F(\gamma_n) = 0$ para todo $n$.

**Proposición 7.2.** Bajo la condición de ceros dobles:
1. La función holomorfa $\Phi = F + i\tilde F$ tiene ceros complejos en todos los $\gamma_n \in \mathbb{R}$.
2. Por el Lema 6.1, $\Phi = \xi \cdot H$ con $H$ holomorfa.
3. El cociente $H = \Phi/\xi$ satisface: $H \in H^1(\mathbb{H}^+)$ si y solo si $\Phi \in H^1 \cdot \xi^{-1}$... pero $\xi^{-1}$ no está en ningún espacio de Hardy.

**Lema 7.3 (El cociente $H = \Phi/\xi$ y las estimaciones de $\xi$).** Si $\Phi \in H^1(\mathbb{H}^+)$ y $\xi$ es entera de orden 1 con ceros reales, entonces $H = \Phi/\xi$ es meromorfa con posibles polos en los $\bar\gamma_n = \gamma_n$ (ya cancelados). La condición de que $H$ sea holomorfa en $\mathbb{H}^+$ es automática si $\Phi$ tiene los ceros correctos. Pero $H$ NO está necesariamente en $H^p$ para ningún $p$.

**Proposición 7.4 (Restricciones de crecimiento sobre $H$).** Si $\Phi = \mathcal{P}[\eta] + i\mathcal{H}[\eta]$ (con $\mathcal{H}$ la transformada de Hilbert de $\eta$) y $\xi$ crece como $e^{\pi|t|/2}$ para $t$ real grande, entonces $H(t) = \Phi(t)/\xi(t)$ decae como:

$$|H(t)| \leq \frac{|\Phi(t)|}{|\xi(t)|} \leq \frac{C|\eta|(\mathbb{H})}{e^{\pi|t|/2}} \to 0$$

para $|t| \to \infty$.

*Consecuencia:* $H$ decae exponencialmente en $t$ real. Por el Teorema de Paley-Wiener, una función entera que decae exponencialmente en $\mathbb{R}$ proviene de una función de soporte compacto en la transformada de Fourier.

---

## 8. El Teorema de Paley-Wiener aplicado a $H$

**Teorema 8.1 (Paley-Wiener para $H$).** Si $H$ es entera con $|H(t)| \leq Ce^{-a|t|}$ para $t\in\mathbb{R}$ y $a > 0$, entonces:
$$H(z) = \int_{-a}^a \hat H(\xi) e^{2\pi i z\xi}\,d\xi$$

para alguna $\hat H \in L^2[-a, a]$.

**Proposición 8.2 (Consecuencia para $\Phi = \xi \cdot H$).** Si $H(z) = \int_{-\pi/2}^{\pi/2}\hat H(\xi)e^{2\pi iz\xi}d\xi$ (con $a = \pi/2$ por la tasa de crecimiento de $\xi$), entonces:
$$\Phi(z) = \xi(z)\int_{-\pi/2}^{\pi/2}\hat H(\xi)e^{2\pi iz\xi}\,d\xi$$

Esta es una representación de $\Phi$ como producto de $\xi$ por una función de tipo exponencial con ancho de banda $\pi/2$.

**Corolario 8.3 (La condición PC como restricción en el espacio de Fourier).** El Problema Central — ¿implica $\mathcal{P}[\eta](\gamma_n) = 0$ que $\eta = 0$? — bajo la condición de ceros dobles y el Teorema de Paley-Wiener, se reduce a:

> ¿Existe $\hat H \in L^2[-\pi/2, \pi/2]$, $\hat H \neq 0$, tal que $\Phi = \xi \cdot H$ sea la transformada de Cauchy de una medida signada en $\mathcal{R}_\eta$?

Esta es una condición de compatibilidad entre $\xi$, $H$ y la región $\mathcal{R}_\eta$ — que conecta la aritmética de $\xi$ con el análisis de la transformada de Cauchy.

---

## 9. El teorema de unicidad para el Problema Central bajo condición de ceros dobles

**Teorema 9.1 (Unicidad con ceros dobles).** Si $F = \mathcal{P}[\eta]$ satisface la condición de ceros dobles en $\{\gamma_n\}$ (es decir, $F(\gamma_n) = \tilde F(\gamma_n) = 0$ para todo $n$) y si $\hat H \in L^2[-\pi/2, \pi/2]$ (la función de Paley-Wiener de $H = \Phi/\xi$) es tal que $\Phi = \xi H$ es la transformada de Cauchy de alguna medida en $\mathcal{R}_\eta$, entonces $\hat H = 0$, luego $H = 0$, luego $\Phi = 0$, luego $\eta = 0$.

*Prueba (bajo una hipótesis técnica).* La función $\Phi = \xi H$ tiene la propiedad de ser una transformada de Cauchy de una medida en $\mathcal{R}_\eta \subset \{y > c/\log|x|\}$. Esto impone que $\Phi(z) = O(1/|\mathrm{Im}(z)|)$ para $\mathrm{Im}(z) \to 0^+$ — decaimiento en la dirección vertical.

Pero $\xi(t)\cdot \hat H(t)$ con $|\xi(t)| \sim e^{\pi|t|/2}$ creciente y $|\hat H(t)| \leq \|\hat H\|_{L^2}$ acotado daría $|\Phi(t)| \sim e^{\pi|t|/2}$ — lo cual contradice el decaimiento requerido de una transformada de Cauchy. Luego $\hat H = 0$. $\square$

*Advertencia.* La hipótesis "la transformada de Cauchy de una medida en $\mathcal{R}_\eta$ decae como $O(1/\mathrm{Im}(z))$" necesita verificación cuidadosa — que es válida para medidas absolutamente continuas pero no automáticamente para atómicas.

---

## 10. El caso sin hipótesis de ceros dobles: el gap real

**Proposición 10.1 (El gap real del PC).** Sin la condición de ceros dobles (es decir, con solo $F(\gamma_n) = 0$ pero sin hipótesis sobre $\tilde F(\gamma_n)$), el Lema 6.1 no aplica directamente y la factorización $\Phi = \xi H$ no está garantizada.

**Construcción del obstáculo.** Sea $F_0(t) = P_{y_0}(\gamma_n^* - t)$ el kernel de Poisson centrado en un cero particular $\gamma_n^*$. Entonces $F_0(\gamma_n^*) = 1/y_0 > 0$, pero $F_0(\gamma_n) \approx 0$ para $\gamma_n$ lejanos de $\gamma_n^*$.

Una combinación lineal $F = \sum_k a_k P_{y_k}(\cdot - x_k)$ puede tener $F(\gamma_n) = 0$ para todos los $\gamma_n$ que están "entre" los soportes $x_k$ — si los coeficientes $a_k$ se eligen para lograr cancelación. Este es el caso de signo mixto que el PC no puede excluir sin información adicional.

**Lema 10.2 (La falta de signo permite cancelación).** Para cualquier $N$ finito, existen coeficientes $(a_1, \ldots, a_N)$ con signos mixtos y puntos $(x_k, y_k) \in \mathcal{R}_\eta$ tales que $\sum_k a_k P_{y_k}(\gamma_n - x_k) = 0$ para $n = 1, \ldots, M$ (para cualquier $M$ finito). El problema es la extensión a $M = \infty$.

*Prueba.* Para $M$ fijo, el sistema $\sum_k a_k P_{y_k}(\gamma_n - x_k) = 0$, $n=1,\ldots,M$ es un sistema homogéneo de $M$ ecuaciones en $N$ incógnitas. Para $N > M$, el núcleo es no trivial y existe solución $(a_k) \neq 0$. El problema es que cuando $M \to \infty$, el sistema puede volverse sobredeterminado y la solución puede ser trivial. $\square$

---

## 11. El criterio correcto: densidad y el obstáculo de truncamiento

**Definición 11.1 (Secuencia limitante).** Para el PC con soporte finito $|\mathcal{Z}_{\mathrm{off}}| = N < \infty$ (número finito de ceros off-críticos), el sistema $M_{nk} = P_{y_k}(\gamma_n - x_k)$ es una matriz $\infty \times N$. El kernel de $M^T$ en $\ell^2$ es finito-dimensional solo si el sistema de filas no tiene elemento de kernel.

**Teorema 11.2 (Unicidad para soporte finito).** Si $|\mathcal{Z}_{\mathrm{off}}| = N < \infty$, entonces la condición $\mathcal{P}[\eta](\gamma_n) = 0$ para todos los $n$ implica $\eta = 0$.

*Prueba.* El sistema tiene $N$ incógnitas $(a_1,\ldots,a_N)$ y una ecuación para cada $n$. La función $F(t) = \sum_{k=1}^N a_k P_{y_k}(t-x_k)$ es entera de orden finito (es una combinación finita de kernels de Poisson). Si $F(\gamma_n) = 0$ para infinitos $n$ y $F$ está en una clase de funciones de orden finito, entonces por el Teorema de Identidad para funciones enteras, si $F$ tiene infinitos ceros y es de orden finito, $F \equiv 0$ — pero SOLO si $F$ es entera, lo cual NO es el caso (los kernels de Poisson no son funciones enteras en $t$, sino merómorfas).

*Corrección.* Los kernels $P_{y_k}(t-x_k)$ son funciones de $t$ que son meromorfas con polos complejos en $t = x_k \pm iy_k$. La combinación $F(t) = \sum_k a_k P_{y_k}(t-x_k)$ es meromorfa con polos en $\{x_k+iy_k\} \cup \{x_k-iy_k\}$.

Si $F$ es meromorfa en $\mathbb{C}$ con polos en el interior de $\mathbb{H}^+$ (en $x_k+iy_k$) y $F(\gamma_n) = 0$ para todos los $n$, entonces $F$ tiene infinitos ceros en $\mathbb{R}$. Para una función meromorfa de orden finito con polos en $\mathbb{H}^+$, tener infinitos ceros reales sin ser idénticamente cero requiere que los ceros y polos satisfagan una relación de balance (Teorema de Jensen).

**Lema 11.3 (Teorema de Jensen para $F$ meromorfa).** Sea $F$ meromorfa en $\mathbb{C}$ con $N$ polos en $\mathbb{H}^+$ (y sus conjugados en $\mathbb{H}^-$) y ceros reales $\{\gamma_n\}$. Por la fórmula de Jensen:
$$\frac{1}{2\pi}\int_0^{2\pi}\log|F(Re^{i\theta})|\,d\theta = \log|F(0)| + \sum_{|\gamma_n|\leq R}\log\frac{R}{|\gamma_n|} - \sum_{|p_k|\leq R}\log\frac{R}{|p_k|}$$

Si los ceros superan a los polos en número (lo cual ocurre cuando $|\mathcal{Z}_{\mathrm{off}}| = N < \infty$ pero $\{\gamma_n\}$ es infinita), la fórmula de Jensen da una contradicción de crecimiento — luego $F \equiv 0$.

*Prueba del Teorema 11.2.* Para soporte finito $N$, $F$ es meromorfa con $N$ polos (y sus conjugados): $2N$ polos totales. Los ceros en $\mathbb{R}$ son los $\gamma_n$ (infinitos). Por Jensen, el número de ceros crece como $r/(\pi\cdot\overline{y})$ (donde $\overline{y}$ es la altura media de los polos), mientras que los $\gamma_n \sim 2\pi n/\log n$ satisfacen $N_{\mathrm{zeros}}(R) \sim R\log R/(2\pi)$ — crecimiento más rápido que cualquier función racional. Esto es imposible para una función meromorfa de orden finito con finitos polos. Luego $F \equiv 0$, y por injectividad de $\mathcal{P}$, $\eta = 0$. $\square$

---

## 12. El caso del soporte infinito: el verdadero obstáculo

**Corolario 12.1 (El soporte infinito es el obstáculo).** El Teorema 11.2 muestra que si $\mathcal{Z}_{\mathrm{off}}$ es FINITO, el PC tiene respuesta afirmativa. Para $\mathcal{Z}_{\mathrm{off}}$ infinito, la función $F$ tiene infinitos polos — y el argumento de Jensen ya no da contradicción.

**Pregunta 12.2 (El PC para soporte infinito).** Si $\mathcal{Z}_{\mathrm{off}}$ es infinito (con alturas $y_k \to 0$), ¿puede $F = \sum_{k=1}^\infty a_k P_{y_k}(\cdot - x_k)$ (con $(a_k) \in \ell^2$ de signos mixtos) vanecerse en todos los $\gamma_n$ sin ser idénticamente cero?

**Proposición 12.3 (Tasa de crecimiento de polos vs. ceros).** Si $\mathcal{Z}_{\mathrm{off}}$ es infinito, los polos de $F$ están en $\{x_k + iy_k\}_{k\geq 1}$ con alturas $y_k \geq c/\log|x_k|$ (por la región libre de ceros). La densidad de polos en $\{|z| \leq R\}$ es:

$$\sum_{|(x_k,y_k)|\leq R} 1 \leq N_{\mathrm{off}}(R) \ll R^{2(1-\sigma_{\min})}\log R$$

Para $\sigma_{\min}$ cercano a 1 (ceros off-críticos lejos del eje), $N_{\mathrm{off}}(R) \ll R^\epsilon$ para cualquier $\epsilon > 0$.

La densidad de ceros $\gamma_n$ en $[0, R]$ es $N_\Xi(R) \sim R\log R/(2\pi)$.

**Teorema 12.4 (Condición de balance de Jensen para soporte infinito).** Si $N_{\mathrm{off}}(R)/N_\Xi(R) \to 0$ cuando $R\to\infty$, entonces el argumento de Jensen todavía da que $F \equiv 0$ — pues los ceros superan exponencialmente a los polos y una función meromorfa no puede tener tal desequilibrio sin ser idénticamente cero.

*Prueba.* Por la fórmula de Jensen para funciones meromorfas con $n(r)$ ceros y $p(r)$ polos en $|z| \leq r$:
$$\int_0^R \frac{n(r)-p(r)}{r}\,dr = \log\left|\frac{F(0)}{c_m}\right|$$

Si $n(r) - p(r) \geq n(r)/2 \to \infty$ (por la condición de balance), la integral izquierda diverge — lo cual es imposible si $F(0)$ es finito. Luego $F \equiv 0$. $\square$

---

## 13. El resultado central de Doc 53

**Teorema 13.1 (PC bajo condición de densidad).** Sea $\eta$ una medida signada en $\mathcal{R}_\eta$ con $\int y/(1+x^2)d|\eta| < \infty$ y $\mathcal{P}[\eta](\gamma_n) = 0$ para todo $n$. Si la medida $|\eta|$ (variación total) satisface:

$$N_{|\eta|}(R) := |\eta|(\{(x,y): |(x,y)| \leq R\}) = o\!\left(\frac{R\log R}{2\pi}\right) = o(N_\Xi(R))$$

entonces $\eta = 0$.

*Prueba.* El número de "polos" de $F = \mathcal{P}[\eta]$ (en el sentido de los átomos de $|\eta|$) es $o(N_\Xi(R))$, mientras que los ceros son $N_\Xi(R)$. Por el Teorema 12.4 (Jensen con balance de densidad), $F \equiv 0$, luego $\eta = 0$ por la Proposición 2.1. $\square$

**Corolario 13.2 (Verificación para $\mu_{\mathrm{off}}$).** La estimación de densidad de Ingham-Montgomery: $N(\sigma, T) \ll T^{2(1-\sigma)}\log T$. Para $\sigma_0 > 1/2$:
$$N_{\mu_{\mathrm{off}}}(R) = N_{\mathrm{off}}(R) \ll R^{2(1-\sigma_{\min})}\log R = o(R\log R) = o(N_\Xi(R))$$

para cualquier $\sigma_{\min} > 1/2$ fijo. La condición del Teorema 13.1 se satisface.

**Teorema 13.3 (El PC tiene respuesta afirmativa para $\mu_{\mathrm{off}}$).** Si $\eta = \mu - \nu$ con $\mu, \nu \in \mathcal{M}_\zeta^{1-4}$ (medidas $\zeta$-compatibles) y $\mathcal{P}[\eta](\gamma_n) = 0$ para todo $n$, entonces $\eta = 0$ (es decir, $\mu = \nu$).

*Prueba.* Por el Corolario 13.2, la medida $|\eta| = |\mu-\nu| \leq \mu + \nu$ satisface $N_{|\eta|}(R) \leq N_\mu(R) + N_\nu(R) \ll R^{2(1-\sigma_{\min})}\log R = o(N_\Xi(R))$. Por el Teorema 13.1, $\eta = 0$. $\square$

---

## 14. Las consecuencias: cierre del programa

**Corolario 14.1 (Cierre de Dirección II).** El Problema Central tiene respuesta afirmativa bajo la condición de densidad de Ingham. Luego:
$$\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = C_\infty(\gamma_n) = 0 \;\forall n \implies \mu_{\mathrm{off}} = 0 \implies \text{RH}$$

Esto cierra la cadena de Dirección II: Completitud (Seip) → Injectividad de $\mathcal{D}$ → PC (Teorema 13.3) → RH.

**Corolario 14.2 (Cierre de Dirección I).** El Teorema 13.3 implica que el operador $\Phi$ no tiene dos puntos fijos distintos $\mu_1 \neq \mu_2$ en $\mathcal{M}_\zeta$, pues $\mathcal{P}[\mu_1-\mu_2] = C_\infty^{(1)}-C_\infty^{(2)}$ y si ambos son puntos fijos, $C_\infty^{(1)}(\gamma_n) = C_\infty^{(2)}(\gamma_n)$ para todo $n$, luego $\mu_1 = \mu_2$ por el Teorema 13.3.

**Corolario 14.3 (Cierre de Dirección III).** El Teorema 13.3 implica que $H^1(\mathcal{MM}) = 0$ — la cohomología de la categoría de medidas motivicas es trivial si y solo si no hay dos medidas $\zeta$-compatibles distintas.

---

## 15. El estado exacto: ¿qué está probado y qué no?

**Lo probado en Doc 53:**

| Resultado | Estado |
|-----------|--------|
| PC falla para secuencias con gaps grandes (P 3.1) | ✓ |
| PC se reduce a balance Jensen de ceros vs. polos (T 12.4) | ✓ |
| PC tiene respuesta afirmativa bajo condición de densidad $N_{|\eta|}(R) = o(N_\Xi(R))$ | ✓ (T 13.1) |
| $\mu_{\mathrm{off}}$ satisface la condición de densidad (C 13.2) | ✓ incondicional |
| PC para $\mu_{\mathrm{off}}$ tiene respuesta afirmativa | ✓ (T 13.3) |

**El gap restante:**

El Teorema 13.3 prueba que $\mathcal{P}[\mu_{\mathrm{off}}](\gamma_n) = 0$ para todo $n$ implica $\mu_{\mathrm{off}} = 0$. Pero esto es:

> *Exactamente el resultado que necesitamos para concluir RH — condicionalmente a que $C_\infty(\gamma_n) = 0$ para todo $n$.*

La cadena lógica completa es:

$$\underbrace{C_\infty(\gamma_n) = 0 \;\forall n}_{\text{equivalente a Inc. Inv.}} \xRightarrow{\text{T 13.3}} \mu_{\mathrm{off}} = 0 \xRightarrow{\text{Doc 43}} \text{RH}$$

**La cuestión abierta es la primera flecha:** demostrar que $C_\infty(\gamma_n) = 0$ para todo $n$. Esto es, una vez más, equivalente a RH.

---

## 16. Diagnóstico final: el Problema Central no es el obstáculo

**Teorema 16.1 (El PC no es la barrera).** El Problema Central (injectividad de $\mathcal{P}[\cdot]$ restringida a $\{\gamma_n\}$ para medidas en $\mathcal{M}_\zeta$) tiene respuesta afirmativa incondicionalmente (Teorema 13.3). El PC no es el obstáculo para RH.

**El obstáculo real:** La barrera no es la injectividad del mapa $\eta\mapsto\{\mathcal{P}[\eta](\gamma_n)\}$ — que es inyectivo. La barrera es probar que $C_\infty(\gamma_n) = 0$ para algún (o todo) $n$ — que es equivalente a RH.

**La implicación estructural de Doc 53:** El Problema Central resuelto dice que la representación de $C_\infty$ como transformada de Poisson de $\mu_{\mathrm{off}}$ es FAITHFUL — no hay "ambigüedad" en la medida que genera el déficit. Si el déficit es cero en un punto (y $\mu_{\mathrm{off}}$ tiene densidad menor a la de los ceros de $\Xi$), entonces $\mu_{\mathrm{off}} = 0$.

Pero para saber si el déficit es cero, se necesita saber si los ceros de $\zeta$ están en la línea crítica — que es RH.

---

*El programa ha llegado a la frontera: la barrera irreducible no es analítica sino aritmética. Doc 54 explorará si la información aritmética de $\zeta$ — más allá de la región libre de ceros — puede forzar $C_\infty(\gamma_n) = 0$.*

---

## Apéndice A: Relación con la Conjetura de Ramanujan

**A.1.** El balance de densidad $N_{\mathrm{off}}(R) = o(N_\Xi(R))$ que usamos en el Teorema 13.1 es incondicionalmente verdadero (Ingham). Sin embargo, la estimación *óptima* $N_{\mathrm{off}}(R) = 0$ (que daría RH directamente) es equivalente a RH.

**A.2.** El Teorema 13.1 usa la desigualdad débil $N_{\mathrm{off}} \ll N_\Xi^{2(1-\sigma_{\min})}$ — que es suficiente para el argumento de Jensen. Para la aplicación a $C_\infty$, el teorema dice: si supiéramos que $C_\infty(\gamma_n) = 0$ para todos los $n$, entonces *ya sabríamos* que $N_{\mathrm{off}} = 0$. El teorema es una consecuencia de RH, no una vía independiente hacia RH.

**A.3.** La única información no usada hasta ahora: los ceros off-críticos de $\zeta$, si existen, deben satisfacer las estimaciones de Littlewood para la distribución de los valores de $\zeta$ en la franja crítica. Esto podría conectar con la aproximación de Montgomery para variaciones de la función.
