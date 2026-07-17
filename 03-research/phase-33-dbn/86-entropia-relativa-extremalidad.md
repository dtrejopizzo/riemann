# Documento 86 — Entropía relativa y extremalidad de $dm_{full}$: síntesis del Camino 1

**Programa:** Hipótesis de Riemann — Fase 33 DBN-CCM  
**Fecha:** 2026-06-09  
**Prerrequisitos:** Docs 74, 77, 80, 83

---

## Resumen

El Documento 83 estableció la dominación puntual $dm_{full} \geq dm_{full,on}$ como medidas y diagnosticó que ningún argumento de dominación de medidas puede, por sí solo, probar RH: la transición de $\geq$ a $=$ es precisamente el contenido no trivial de la hipótesis. El presente documento explora si el lenguaje de la teoría de la información —en particular la entropía relativa (divergencia de Kullback-Leibler) y sus variantes— ofrece una entrada nueva al problema.

La conclusión es que no. La entropía relativa $\mathcal{KL}(dm_{full}\|dm_{full,on})$, la divergencia de Jensen-Shannon, la distancia de Wasserstein y la función de Herglotz asociada a la diferencia de medidas son todas reformulaciones del mismo criterio: son cero si y solo si RH. Cada una añade una perspectiva técnica limpia, pero ninguna proporciona un medio de verificación independiente. En §10 se formaliza el obstáculo como la "barrera de Hadamard" y se formula un problema abierto preciso que resume el estado del Camino 1.

---

## §1. La entropía relativa entre $dm_{full}$ y $dm_{full,on}$

### 1.1. Definición y primera fórmula

Adoptamos la notación del Doc 83. Para $s \in \mathbb{R}$ escribimos $d m_{full}(s) = |\zeta(1/2+is)|^2 dm_\infty(s)$ y $dm_{full,on}(s) = |\zeta_{on}(1/2+is)|^2 dm_\infty(s)$, donde $dm_\infty$ es la medida espectral de referencia del operador de Jacobi asociado a la función zeta completa (normalizada de modo que las dos medidas tengan la misma masa finita; su valor exacto no es esencial aquí).

La **divergencia de Kullback-Leibler** de $dm_{full}$ respecto a $dm_{full,on}$ se define como

$$\mathcal{KL}(dm_{full} \| dm_{full,on}) = \int_{\mathbb{R}} \log\frac{dm_{full}}{dm_{full,on}}\, dm_{full} = \int_{\mathbb{R}} \log\left(\frac{|\zeta(1/2+is)|^2}{|\zeta_{on}(1/2+is)|^2}\right) |\zeta(1/2+is)|^2\, dm_\infty(s).$$

Por la Proposición 1.1 del Doc 83, el cociente de densidades $R(s) := |\zeta(1/2+is)|^2/|\zeta_{on}(1/2+is)|^2$ se expresa mediante el producto de Hadamard como

$$R(s) = \prod_{j:\,\delta_j>0} \left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2,$$

donde el producto corre sobre los ceros off-critical con parte real $1/2+\delta_j > 1/2$ (uno de cada cuádruplo). En particular $R(s) \geq 1$ para todo $s$ real (fuera de los ceros de $\zeta_{on}$), con igualdad puntual $R(s) = 1$ para todo $s$ si y solo si todos los $\delta_j = 0$, es decir si y solo si RH.

La función $\log R(s)$ admite la representación

$$\log R(s) = 2\sum_{j:\,\delta_j>0} \log\left(1 + \frac{\delta_j^2}{(s-\gamma_j)^2}\right).$$

Cada sumando es no negativo y se anula si y solo si $\delta_j = 0$.

### 1.2. La entropía relativa es no negativa y se anula exactamente bajo RH

**Proposición 1.1.** $\mathcal{KL}(dm_{full}\|dm_{full,on}) \geq 0$, con igualdad si y solo si $dm_{full} = dm_{full,on}$ $dm_\infty$-casi en todo punto. Esta última condición equivale a RH.

*Demostración.* La desigualdad $\mathcal{KL} \geq 0$ es la desigualdad de Gibbs estándar: para cualquier par de medidas de probabilidad $\mu \ll \nu$, se tiene $\int \log(d\mu/d\nu)\,d\mu \geq 0$ por la convexidad de $x \mapsto x\log x$ y la desigualdad de Jensen. (Para medidas de masa finita no unitaria el argumento es análogo.) La igualdad se da si y solo si la densidad $d\mu/d\nu$ es constante $\mu$-c.t.p., lo que aquí significa $R(s) = 1$ casi en todo punto. Pero $R(s)$ es una función analítica real (fuera de los $\gamma_j$, que forman un conjunto discreto), de modo que $R \equiv 1$ c.t.p. implica $R \equiv 1$ en todo $\mathbb{R}$, y esto es equivalente a que todos los $\delta_j = 0$, es decir RH. $\square$

Este resultado es correcto y su demostración es elemental. La observación importante es que no hay contenido nuevo: la equivalencia "$\mathcal{KL} = 0 \Leftrightarrow \text{RH}$" es una reformulación, no una prueba.

---

## §2. Relación entre $\mathcal{KL}$ y la traza $T_\lambda$

### 2.1. Las dos funcionales comparadas

Recordamos del Doc 70 que la traza relevante del criterio CTP es

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\, (dm_{full} - dm_{full,on})(s) = \int_{\mathbb{R}} W_\lambda(s)\, (R(s)-1)\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s),$$

donde $W_\lambda \geq 0$ es el núcleo de peso del operador de De Bruijn-Newman al nivel $\lambda$.

La divergencia KL puede reescribirse como

$$\mathcal{KL}(dm_{full}\|dm_{full,on}) = \int_{\mathbb{R}} \log R(s)\cdot R(s)\cdot |\zeta_{on}(1/2+is)|^2\, dm_\infty(s).$$

### 2.2. Comparación mediante la desigualdad $\log x \leq x - 1$

Para todo $x > 0$ se tiene $\log x \leq x - 1$. Aplicando a $x = R(s) \geq 1$:

$$\log R(s) \leq R(s) - 1.$$

Multiplicando ambos miembros por $R(s) \geq 1$ y por $|\zeta_{on}|^2 dm_\infty \geq 0$:

$$\log R(s) \cdot R(s) \cdot |\zeta_{on}|^2 \leq (R(s)-1)\cdot R(s)\cdot |\zeta_{on}|^2.$$

Esto da

$$\mathcal{KL}(dm_{full}\|dm_{full,on}) \leq \int_{\mathbb{R}} (R(s)-1)\, R(s)\, |\zeta_{on}|^2\, dm_\infty = \int_{\mathbb{R}} (R(s)-1)\, |\zeta(1/2+is)|^2\, dm_\infty,$$

que no involucra $W_\lambda$ y que difiere de $T_\lambda$ tanto por el peso (se integra contra $|\zeta|^2 dm_\infty$ en lugar de $W_\lambda |\zeta_{on}|^2 dm_\infty$) como por la presencia del factor adicional $R$.

**Proposición 2.1.** No existe una relación de comparación directa entre $T_\lambda$ y $\mathcal{KL}(dm_{full}\|dm_{full,on})$ que sea válida incondicionalmente. Las dos funcionales son comparables solo si se dispone de cotas sobre $R(s)$ uniformes en $s$, y tales cotas dependen de la posición de los ceros off-critical.

*Argumento.* $T_\lambda$ integra $(R-1)|\zeta_{on}|^2$ con el peso $W_\lambda$, mientras que $\mathcal{KL}$ integra $(\log R)\cdot R \cdot |\zeta_{on}|^2$ con peso 1. En regiones donde $R(s)$ es grande (cerca de un cero off-critical $\gamma_j$, donde $R(s) \sim \delta_j^2/(s-\gamma_j)^2 \to \infty$), el integrando de $\mathcal{KL}$ domina al de $T_\lambda$ (si $W_\lambda(\gamma_j)$ es finito). En regiones donde $R \approx 1$, los dos integrandos son comparables a primer orden en $\delta_j^2$. Sin cotas sobre los $\delta_j$ y los $\gamma_j$ no se puede establecer la comparación global.

### 2.3. La expansión a primer orden en $\delta_j^2$

Para $\delta_j$ pequeños, expandiendo $R(s) = 1 + 2\sum_j \delta_j^2/(s-\gamma_j)^2 + O(\delta_j^4)$ y $\log R(s) = 2\sum_j \delta_j^2/(s-\gamma_j)^2 + O(\delta_j^4)$:

$$\mathcal{KL} = \int_{\mathbb{R}} \left(2\sum_j \frac{\delta_j^2}{(s-\gamma_j)^2} + O(\delta_j^4)\right) |\zeta_{on}|^2\, dm_\infty + O(\delta_j^4),$$

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s) \left(2\sum_j \frac{\delta_j^2}{(s-\gamma_j)^2} + O(\delta_j^4)\right)|\zeta_{on}|^2\, dm_\infty + O(\delta_j^4).$$

A este orden, $T_\lambda$ y $\mathcal{KL}$ difieren solo por el peso $W_\lambda$ frente a $1$: si $W_\lambda \leq 1$ uniformemente, entonces $T_\lambda \leq \mathcal{KL}$ a primer orden en $\delta_j^2$. Pero esta comparación es solo perturbativa y no transfiere ninguna información nueva.

---

## §3. La entropía relativa como funcional sobre la clase de Hadamard

### 3.1. La clase de medidas de Hadamard

Definimos la clase

$$\mathcal{M}_{Hd} = \left\{d\mu = |\eta(1/2+is)|^2 dm_\infty(s) : \eta \text{ entera de orden 1, misma masa total que }\zeta \right\},$$

donde la condición "misma masa total" significa $\int |\eta|^2 dm_\infty = \int |\zeta|^2 dm_\infty$. En esta clase se incluyen tanto $dm_{full}$ (con la distribución real de ceros de $\zeta$) como $dm_{full,on}$ (con todos los ceros proyectados a la recta crítica).

La entropía de Shannon de $\mu \in \mathcal{M}_{Hd}$ (respecto a $dm_\infty$) se define como

$$H(\mu) = -\int \log\left(\frac{d\mu}{dm_\infty}\right) d\mu = -\int \log(|\eta|^2) |\eta|^2\, dm_\infty.$$

### 3.2. ¿Es $dm_{full,on}$ el maximizador de entropía?

**Proposición 3.1.** La medida $dm_{full,on}$ no es, en general, el maximizador de $H(\mu)$ en $\mathcal{M}_{Hd}$. El principio de máxima entropía en esta clase no impone que los ceros estén sobre la recta crítica.

*Argumento.* El maximizador de $H(\mu) = -\int \log(|\eta|^2)|\eta|^2\, dm_\infty$ sobre la clase $\mathcal{M}_{Hd}$ con la única restricción de masa fija es la medida con densidad $|\eta|^2 = C$ constante, es decir la medida absolutamente continua respecto a $dm_\infty$ con densidad uniforme. Esta solución no corresponde ni a $dm_{full}$ ni a $dm_{full,on}$ (cuyas densidades no son constantes, puesto que tienen ceros en los $\pm \gamma_j$ con multiplicidad).

Si se añaden restricciones de tipo "los momentos de la distribución de ceros están sobre la recta crítica", el problema de maximización con restricciones puede tener como solución $dm_{full,on}$. Pero tales restricciones son exactamente equivalentes a imponer RH como condición a priori, de modo que el argumento es circular.

**Conclusión de §3.** El principio de máxima entropía no proporciona una caracterización independiente de $dm_{full,on}$ dentro de $\mathcal{M}_{Hd}$. La relación entre la distribución de ceros y la entropía de la medida espectral no tiene la estructura de un problema variacional convexo con solución única determinada por la posición de los ceros.

---

## §4. La divergencia de Jensen-Shannon

### 4.1. Definición

Sea $dm_M = (dm_{full} + dm_{full,on})/2$ la mezcla aritmética de las dos medidas. La **divergencia de Jensen-Shannon** es

$$\mathcal{JS}(dm_{full}, dm_{full,on}) = \frac{1}{2}\mathcal{KL}(dm_{full}\|dm_M) + \frac{1}{2}\mathcal{KL}(dm_{full,on}\|dm_M).$$

A diferencia de $\mathcal{KL}$, la divergencia $\mathcal{JS}$ es simétrica y acotada: $0 \leq \mathcal{JS} \leq \log 2$.

### 4.2. Expresión explícita usando $R(s) \geq 1$

Las densidades relativas son $dm_{full}/dm_M = 2R(s)/(R(s)+1)$ y $dm_{full,on}/dm_M = 2/(R(s)+1)$. Por tanto

$$\mathcal{JS} = \frac{1}{2}\int \log\!\left(\frac{2R(s)}{R(s)+1}\right) R(s) |\zeta_{on}|^2 dm_\infty + \frac{1}{2}\int \log\!\left(\frac{2}{R(s)+1}\right) |\zeta_{on}|^2 dm_\infty.$$

Usando $R(s) \geq 1$: el factor $2R(s)/(R(s)+1) \in [1,2)$ para $R \geq 1$, así que $\log(2R/(R+1)) \geq 0$; el factor $2/(R(s)+1) \in (0,1]$ para $R \geq 1$, así que $\log(2/(R+1)) \leq 0$. Los dos sumandos tienen signos opuestos y la positividad de $\mathcal{JS}$ resulta de la convexidad de $x \mapsto x\log x$ (no de un argumento signo a signo).

**Proposición 4.1.** $\mathcal{JS}(dm_{full}, dm_{full,on}) \geq 0$ con igualdad si y solo si $R(s) \equiv 1$ (iff RH). La acotación $\mathcal{JS} \leq \log 2$ es universal.

La cota superior $\mathcal{JS} \leq \log 2$ es interesante pues acota la "distancia relativa" entre $dm_{full}$ y $dm_{full,on}$ independientemente de la distribución de ceros. Pero, de nuevo, la condición $\mathcal{JS} = 0$ equivale a RH y no proporciona una nueva vía de prueba.

---

## §5. El cociente $R(s)$ y sus propiedades analíticas

### 5.1. Estructura de $R(s)$ como función real-analítica

El cociente $R(s) = |\zeta(1/2+is)|^2/|\zeta_{on}(1/2+is)|^2$ es una función real-analítica en $\mathbb{R} \setminus \{\gamma_j\}_{j}$. En los puntos $s = \gamma_j$ (ceros de $\zeta_{on}$ sobre la recta crítica), la función $|\zeta_{on}(1/2+is)|^2$ se anula, mientras que $|\zeta(1/2+is)|^2$ puede o no anularse dependiendo de si $\gamma_j$ es también cero de $\zeta$ (en cuyo caso los órdenes de anulación se comparan).

Para los propósitos de esta sección consideramos los puntos genéricos $s \neq \gamma_j$ donde $R(s)$ está bien definido.

**Proposición 5.1.** $R(s) = 1$ para todo $s \in \mathbb{R} \setminus \{\gamma_j\}$ si y solo si todos los $\delta_j = 0$ (RH). Bajo $\neg$RH, $R(s) > 1$ para todo $s \in \mathbb{R} \setminus \{\gamma_j\}$, y $\inf_{s \in \mathbb{R}} R(s) = 1$ (el ínfimo se alcanza en el límite $|s| \to \infty$, donde todos los factores tienden a 1).

*Demostración.* El producto de Hadamard muestra que $R(s) = \prod_j (1+\delta_j^2/(s-\gamma_j)^2)^2 \geq 1$ con igualdad puntual solo si todos los $\delta_j = 0$. Para $|s| \to \infty$, cada factor $(1+\delta_j^2/(s-\gamma_j)^2) \to 1$, y la convergencia del producto (que requiere $\sum_j \delta_j^2/\gamma_j^2 < \infty$, válida por la densidad de ceros de $\zeta$) garantiza $R(s) \to 1$. $\square$

### 5.2. La función $\log R$ cerca de $s = \gamma_j$

Cerca de $s = \gamma_j$, el factor $j$-ésimo de $R(s)$ es $(1+\delta_j^2/(s-\gamma_j)^2)^2 \sim \delta_j^4/(s-\gamma_j)^4$, de modo que $\log R(s) \sim 4\log(\delta_j/(s-\gamma_j)) \to +\infty$. La singularidad es logarítmica y la integral $\int \log R(s)\, |\zeta_{on}|^2\, dm_\infty$ converge porque $|\zeta_{on}(1/2+is)|^2 \sim (s-\gamma_j)^2$ cerca de $s = \gamma_j$ (cero simple de $\zeta_{on}$), y $(s-\gamma_j)^2 \log(1/(s-\gamma_j)) \to 0$.

Esta convergencia es otro modo de ver que $\mathcal{KL}$ está bien definida.

---

## §6. La función $\log R$ y la traza $T_\lambda$ a todos los órdenes

### 6.1. Representación de $T_\lambda$ en términos del cociente $R$

Usando $R(s) - 1 = (|\zeta|^2 - |\zeta_{on}|^2)/|\zeta_{on}|^2$:

$$T_\lambda = \int_{\mathbb{R}} W_\lambda(s)\, (R(s)-1)\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s).$$

### 6.2. Expansión en serie de $\delta_j^2$

Para ceros off-critical con desplazamientos $\delta_j$ arbitrarios (no necesariamente pequeños), la expansión del producto de Hadamard da

$$R(s) - 1 = \prod_j \left(1+\frac{\delta_j^2}{(s-\gamma_j)^2}\right)^2 - 1 = \sum_j \frac{2\delta_j^2}{(s-\gamma_j)^2} + \sum_{j<k}\frac{4\delta_j^2\delta_k^2}{(s-\gamma_j)^2(s-\gamma_k)^2} + \cdots$$

donde los términos de orden superior en $\delta^2$ son positivos. En particular $R(s)-1 \geq \sum_j 2\delta_j^2/(s-\gamma_j)^2$.

**Proposición 6.1.** Se tiene la cota inferior

$$T_\lambda \geq 2\sum_{j:\,\delta_j>0} \delta_j^2 \int_{\mathbb{R}} \frac{W_\lambda(s)}{(s-\gamma_j)^2}\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s).$$

Cada término del lado derecho es no negativo (pues $W_\lambda \geq 0$, $|\zeta_{on}|^2 \geq 0$ y $(s-\gamma_j)^{-2} \geq 0$). Si algún $\delta_j > 0$ y la integral es estrictamente positiva (lo que ocurre siempre que $\zeta_{on}$ no sea idénticamente cero en un entorno de $\gamma_j$), entonces $T_\lambda > 0$.

Esto confirma el criterio CTP de los Docs 70–72: $T_\lambda > 0$ bajo $\neg$RH. Pero, como se indicó en el Doc 83, la implicación inversa ($T_\lambda = 0 \Rightarrow$ RH) es el contenido no trivial del criterio y no se deduce de esta estimación.

Definimos el núcleo de Poisson generalizado

$$K_\lambda(\gamma_j) := \int_{\mathbb{R}} \frac{W_\lambda(s)}{(s-\gamma_j)^2}\, |\zeta_{on}(1/2+is)|^2\, dm_\infty(s) > 0,$$

de modo que $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j)$. La desigualdad es estricta si hay algún $\delta_j > 0$.

---

## §7. La distancia de Wasserstein

### 7.1. Definición

La **distancia de Wasserstein de orden 2** entre $dm_{full}$ y $dm_{full,on}$ es

$$W_2(dm_{full}, dm_{full,on})^2 = \inf_{\pi} \int_{\mathbb{R}^2} (s-t)^2\, d\pi(s,t),$$

donde el ínfimo es sobre todos los acoplamientos (medidas con márgenes $dm_{full}$ y $dm_{full,on}$ respectivamente).

### 7.2. El acoplamiento de dominación

Dado que $dm_{full} \geq dm_{full,on}$ como medidas positivas, se puede construir el acoplamiento de dominación: escribir $dm_{full} = dm_{full,on} + d\nu$ donde $d\nu = (R(s)-1)|\zeta_{on}|^2\, dm_\infty \geq 0$. Un acoplamiento natural es la suma del acoplamiento diagonal $\delta_{s=t}$ sobre $dm_{full,on}$ más un acoplamiento de la masa extra $d\nu$ a cualquier punto. Para el acoplamiento diagonal sobre $dm_{full,on}$ más el "exceso" acoplado a su origen:

$$\pi^*(s,t) = dm_{full,on}(s)\,\delta_s(dt) + d\nu(s)\,\delta_{s_0}(dt)$$

para algún punto de referencia $s_0$. Este acoplamiento no es óptimo en general, pero da la cota

$$W_2^2 \leq \int (s-t)^2\, d\pi^* = \int (s-s_0)^2\, d\nu(s) = \int (s-s_0)^2(R(s)-1)|\zeta_{on}|^2\, dm_\infty.$$

La cota óptima requiere resolver el problema de transporte óptimo, que es no trivial en este contexto.

**Proposición 7.1.** $W_2(dm_{full}, dm_{full,on}) = 0$ si y solo si $dm_{full} = dm_{full,on}$ (iff RH). Sin información adicional sobre los ceros off-critical no se puede calcular $W_2$ explícitamente.

### 7.3. Comparación con $T_\lambda$

La traza $T_\lambda = \int W_\lambda (dm_{full} - dm_{full,on})$ es el primer momento de la medida diferencia $dm_{full} - dm_{full,on}$ contra el peso $W_\lambda$. La distancia de Wasserstein $W_2$ es el segundo momento del transporte óptimo. Son cantidades de naturaleza diferente y no son comparables directamente sin hipótesis adicionales.

---

## §8. La condición de Radon-Nikodym extremal

### 8.1. Planteamiento

La densidad de Radon-Nikodym de $dm_{full}$ respecto a $dm_{full,on}$ es $R(s) \geq 1$. RH equivale a que esta densidad sea identicamente 1. La pregunta es: ¿existe una condición espectral o analítica sobre $R$ que sea más fácil de verificar que RH mismo y que implique $R \equiv 1$?

### 8.2. El teorema de Helson-Szegő y su alcance

El teorema de Helson-Szegő (1960) caracteriza, sobre el círculo unidad, las medidas $d\mu = w\,dm$ para las cuales el operador de proyección de Hardy (operador de Szegő) es acotado en $L^2(d\mu)$: la condición es que $\log w = u + \tilde{v}$ donde $u \in L^\infty$, $v \in L^\infty$ real con $\|v\|_\infty < \pi/2$, y $\tilde{v}$ es el conjugado armónico de $v$.

En nuestro contexto, $w(s) = R(s) = |\zeta|^2/|\zeta_{on}|^2$ y la medida base es $dm_{full,on}$. Una aplicación del espíritu del teorema de Helson-Szegő requeriría:

1. Trasladar el problema de la recta real al círculo unidad (vía una transformación de Möbius).
2. Identificar el operador de Szegő asociado con el operador de Jacobi relevante.
3. Verificar que la condición de acotación del operador de Szegő se puede comprobar sin conocer los ceros de $\zeta$.

El paso 3 es el que fracasa. La acotación del operador de Szegő para la medida $dm_{full}$ en $L^2(dm_{full,on})$ es equivalente a condiciones sobre $R(s)$ que dependen de la estructura global de los ceros off-critical. No se dispone de un criterio autónomo para esta acotación.

**Conclusión de §8.** El teorema de Helson-Szegő sugiere una dirección interesante (conectar la densidad de Radon-Nikodym $R$ con la acotación de operadores de Szegő) pero no proporciona una vía directa a RH con las herramientas disponibles.

---

## §9. La función de Herglotz y la extremalidad

### 9.1. La función de Herglotz asociada a $dm_{full}$

Para $z \in \mathbb{C}$ con $\operatorname{Im}(z) > 0$, la **función de Herglotz** (también llamada función de Cauchy-Stieltjes o de Carathéodory, según la normalización) asociada a $dm_{full}$ es

$$\mathcal{F}(z) = \int_{\mathbb{R}} \frac{s+z}{s-z}\, dm_{full}(s).$$

Esta función satisface $\operatorname{Re}\mathcal{F}(z) > 0$ para $\operatorname{Im}(z) > 0$ (es una función de Carathéodory). Análogamente se define $\mathcal{F}_{on}(z)$ con $dm_{full,on}$.

### 9.2. La diferencia $\mathcal{F}(z) - \mathcal{F}_{on}(z)$

**Proposición 9.1.** La diferencia

$$\mathcal{G}(z) := \mathcal{F}(z) - \mathcal{F}_{on}(z) = \int_{\mathbb{R}} \frac{s+z}{s-z}\, (dm_{full} - dm_{full,on})(s)$$

es también una función de Herglotz: $\operatorname{Re}\mathcal{G}(z) \geq 0$ para $\operatorname{Im}(z) > 0$, con $\operatorname{Re}\mathcal{G}(z) = 0$ (identicamente) si y solo si $dm_{full} = dm_{full,on}$ (iff RH).

*Demostración.* Para $\operatorname{Im}(z) > 0$ y $s \in \mathbb{R}$, el cociente $(s+z)/(s-z)$ tiene parte real $\operatorname{Re}[(s+z)/(s-z)] = [(s^2-|z|^2)/|s-z|^2 + 2s\operatorname{Im}(z)/|s-z|^2\cdot\operatorname{Re}(z/z)]$... calculamos directamente: escribamos $z = x+iy$, $y > 0$. Entonces $s-z = (s-x)-iy$ y $s+z = (s+x)+iy$. El cociente

$$\frac{s+z}{s-z} = \frac{(s+x+iy)(s-x+iy)}{(s-x)^2+y^2} = \frac{(s^2-x^2+y^2) + 2iys}{(s-x)^2+y^2}.$$

La parte real es $(s^2-x^2+y^2)/((s-x)^2+y^2)$, cuyo signo puede ser positivo o negativo dependiendo de $s$. Corrijamos la afirmación.

Para $z = iy$ puramente imaginario con $y > 0$: $\operatorname{Re}[(s+iy)/(s-iy)] = (s^2-y^2+y^2)/(s^2+y^2) = s^2/(s^2+y^2) \geq 0$. Para $z$ general la parte real no es necesariamente no negativa.

La corrección relevante es la siguiente: $\mathcal{G}(z)$ es una función de Nevanlinna (con parte imaginaria no negativa) en el semiplano superior, no necesariamente de Carathéodory. Pero para la representación de Nevanlinna:

$$\operatorname{Im}\mathcal{G}(z) = \int_{\mathbb{R}} \operatorname{Im}\!\left[\frac{s+z}{s-z}\right] (dm_{full}-dm_{full,on})(s).$$

Para $z = x+iy$, $y > 0$:

$$\operatorname{Im}\!\left[\frac{s+z}{s-z}\right] = \operatorname{Im}\!\left[\frac{(s+x+iy)(s-x+iy)}{|s-z|^2}\right] = \frac{y(s+x) + y(s-x)}{|s-z|^2} = \frac{2ys}{|s-z|^2}.$$

Esto tiene el signo de $s$, no es no negativo en general.

La representación de Nevanlinna correcta utiliza la fórmula de Poisson-Stieltjes. Lo que sí se puede afirmar es que $\mathcal{G}$ tiene una representación de Nevanlinna con medida espectral $dm_{full} - dm_{full,on} \geq 0$, lo cual es una función de Nevanlinna con medida espectral positiva —esto corresponde a la clase de funciones Pick con medida de representación positiva.

**Proposición 9.1 (corregida).** La función $\mathcal{G}(z) = \mathcal{F}(z) - \mathcal{F}_{on}(z)$ admite la representación de Nevanlinna

$$\mathcal{G}(z) = \int_{\mathbb{R}} \frac{1+sz}{s-z}\, (dm_{full}-dm_{full,on})(s) + \alpha + \beta z$$

para ciertas constantes reales $\alpha, \beta \geq 0$ (con las normalizaciones estándar). La medida espectral de $\mathcal{G}$ es la medida positiva $dm_{full} - dm_{full,on} \geq 0$.

$\mathcal{G}(z) \equiv 0$ si y solo si $dm_{full} = dm_{full,on}$ como medidas, es decir si y solo si RH.

### 9.3. Los operadores de Jacobi y la función $\mathcal{G}$

La función de Nevanlinna $\mathcal{G}$ con medida espectral $dm_{full} - dm_{full,on} \geq 0$ define un tercer operador de Jacobi $J_\mathcal{G}$ cuyos coeficientes $\{a_k^\mathcal{G}, b_k^\mathcal{G}\}$ están determinados por los momentos de la medida diferencia. Las relaciones entre $J_\mathcal{G}$, $J_{full}$ y $J_{on}$ no son simples (los coeficientes de Jacobi no son lineales en la medida espectral).

La condición RH $\equiv \mathcal{G} \equiv 0 \equiv J_\mathcal{G} = 0$ podría —en principio— conectarse con propiedades del operador de Jacobi del CCM. Pero no se conoce ningún camino directo.

---

## §10. Síntesis: el Camino 1 y el obstáculo final formalizado

### 10.1. La cadena de equivalencias

**Teorema 10.1 (síntesis del Camino 1).** Las siguientes condiciones son mutuamente equivalentes:

1. **RH:** todos los ceros no triviales de $\zeta$ tienen parte real $1/2$.
2. **Igualdad de medidas:** $dm_{full} = dm_{full,on}$ (como medidas en $\mathbb{R}$).
3. **Criterio CTP:** $T_\lambda = 0$ para todo $\lambda \geq 0$.
4. **Entropía relativa nula:** $\mathcal{KL}(dm_{full}\|dm_{full,on}) = 0$.
5. **Divergencia JS nula:** $\mathcal{JS}(dm_{full}, dm_{full,on}) = 0$.
6. **Wasserstein cero:** $W_2(dm_{full}, dm_{full,on}) = 0$.
7. **Densidad trivial:** $R(s) \equiv 1$ para $dm_\infty$-c.t.p. $s \in \mathbb{R}$.
8. **Herglotz nula:** $\mathcal{G}(z) \equiv 0$ en el semiplano superior.

*Demostración.* Las implicaciones $1 \Leftrightarrow 2$ y $2 \Rightarrow$ todos los demás son inmediatas de las definiciones. Las implicaciones inversas ($3,4,5,6,7,8 \Rightarrow 2$) se siguen todas de la positividad estricta de las respectivas funcionales bajo $\neg$RH (establecida en las proposiciones anteriores y en el Doc 83) y de la analiticidad de $R$ (que impide que $R \equiv 1$ c.t.p. sin $R \equiv 1$ en todas partes). La equivalencia $2 \Leftrightarrow 3$ es el criterio CTP de los Docs 64 y 70. $\square$

### 10.2. Lo que cada reformulación añade

Cada reformulación de las condiciones 2–8 ilumina un aspecto diferente de la estructura:

- Las condiciones 2 y 7 (igualdad de medidas / densidad trivial) son las más directas: RH en términos de medidas espectrales.
- La condición 3 (criterio CTP) es la entrada del programa DBN-CCM y conecta con el flujo de De Bruijn-Newman.
- Las condiciones 4 y 5 (entropía relativa y JS) colocan el problema en el marco de la teoría de la información: RH es la condición de "indistinguibilidad informacional" entre las dos medidas.
- La condición 6 (Wasserstein) lo coloca en el marco del transporte óptimo.
- La condición 8 (Herglotz) lo conecta con la teoría de funciones de Nevanlinna y los operadores de Jacobi.

Ninguna de estas reformulaciones proporciona por sí sola una vía de demostración. Lo que ofrecen es un vocabulario preciso para articular el obstáculo.

### 10.3. La barrera de Hadamard

**Problema 10.1 (Barrera de Hadamard).** ¿Existe alguna propiedad $\mathcal{P}$ de la función $\zeta$ que satisfaga simultáneamente:

(a) $\mathcal{P}$ es verificable a partir de propiedades analíticas conocidas de $\zeta$ (la ecuación funcional, el orden de crecimiento, la distribución asintótica de ceros, las estimaciones de momentos de la función zeta) sin asumir la posición de los ceros no triviales;

(b) $\mathcal{P}$ implica alguna de las condiciones equivalentes del Teorema 10.1?

El Camino 1 no ha encontrado ninguna propiedad que satisfaga (a) y (b) simultáneamente. Todos los criterios de las condiciones 2–8 son verificables condicionalmente a RH (trivialmente: si RH, entonces $R \equiv 1$, etc.) pero no incondicionalmente.

El obstáculo es estructural: el producto de Hadamard expresa $R(s)-1$ como una suma de contribuciones de los ceros off-critical con peso $\delta_j^2/(s-\gamma_j)^2$. Para probar $R \equiv 1$ sin información sobre los ceros hay que probar que ningún cero puede estar fuera de la recta crítica, lo cual es exactamente RH. No hay cortocircuito.

### 10.4. Diagnóstico final del Camino 1

El Camino 1 ha producido los siguientes resultados positivos, todos incondicionales:

- **Dominación puntual** $|\zeta(1/2+is)|^2 \geq |\zeta_{on}(1/2+is)|^2$ para todo $s \in \mathbb{R}$ (Proposición 1.1, Doc 83).
- **Dominación de medidas** $dm_{full} \geq dm_{full,on}$ como medidas positivas (Corolario 1.2, Doc 83).
- **Positividad de $T_\lambda$** bajo $\neg$RH: $T_\lambda \geq 2\sum_j \delta_j^2 K_\lambda(\gamma_j) > 0$ (Proposición 6.1 del presente documento).
- **Equivalencias** entre múltiples formulaciones del criterio RH: entropía relativa, distancia de Wasserstein, función de Herglotz (Teorema 10.1).
- **Formalización del obstáculo** como la Barrera de Hadamard (Problema 10.1).

Lo que el Camino 1 no ha conseguido: ningún argumento que no use la posición de los ceros y que implique alguna de las condiciones 2–8 del Teorema 10.1. La barrera es robusta: cualquier función $\zeta$ con un cero off-critical tiene $R(s) > 1$ en todo punto, $\mathcal{KL} > 0$, $T_\lambda > 0$, etc., y ninguna de estas desigualdades estrictas puede ser refutada por propiedades globales de $\zeta$ conocidas incondicionalmente.

### 10.5. La conexión más prometedora: $\mathcal{G}$ y el Camino 2

La función de Nevanlinna $\mathcal{G}(z) = \mathcal{F}(z) - \mathcal{F}_{on}(z)$ con medida espectral $dm_{full} - dm_{full,on}$ es el objeto natural que "mide" el alejamiento de RH desde la perspectiva del Camino 1. Esta función tiene una representación espectral positiva y está conectada con el operador de Jacobi $J_\mathcal{G}$.

Por otro lado, el Camino 2 (funciones L y reciprocidad) trabaja directamente con la función zeta como función analítica en el plano complejo y con sus relaciones con la distribución de primos. La conexión posible es la siguiente: si los coeficientes de Jacobi de $J_\mathcal{G}$ pueden expresarse en términos de sumas sobre primos (como sugiere la fórmula explícita de Weil del Doc 72), entonces la condición $\mathcal{G} \equiv 0$ podría reformularse como una identidad entre sumas sobre primos y sumas sobre ceros —una identidad que quizás sea accesible por reciprocidad.

Esta conexión no está desarrollada y queda como la dirección más prometedora para el trabajo futuro.

---

## Apéndice: resumen de objetos y notación del Camino 1

| Símbolo | Definición |
|---------|-----------|
| $dm_{full}$ | Medida espectral $\lvert\zeta(1/2+is)\rvert^2 dm_\infty$ |
| $dm_{full,on}$ | Ídem con ceros de $\zeta$ proyectados a la recta crítica |
| $R(s)$ | Cociente $\lvert\zeta(1/2+is)\rvert^2/\lvert\zeta_{on}(1/2+is)\rvert^2 \geq 1$ |
| $\delta_j$ | Distancia del $j$-ésimo cero off-critical a la recta crítica |
| $T_\lambda$ | Traza $\int W_\lambda\,(dm_{full}-dm_{full,on})$ |
| $\mathcal{KL}$ | Divergencia de Kullback-Leibler de $dm_{full}$ respecto a $dm_{full,on}$ |
| $\mathcal{JS}$ | Divergencia de Jensen-Shannon (simétrica) entre las dos medidas |
| $W_2$ | Distancia de Wasserstein de orden 2 entre las dos medidas |
| $\mathcal{F}$, $\mathcal{F}_{on}$ | Funciones de Herglotz/Nevanlinna de $dm_{full}$ y $dm_{full,on}$ |
| $\mathcal{G}$ | $\mathcal{F} - \mathcal{F}_{on}$: función de Nevanlinna con medida espectral $dm_{full}-dm_{full,on}$ |
| Barrera de Hadamard | Problema 10.1: inexistencia conocida de verificación incondicional de $R \equiv 1$ |

---

**Fin del Documento 86**
