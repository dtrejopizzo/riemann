# Documento 109 — El principio de anclaje crítico: ¿qué fuerza Λ=0?

**Programa:** Hipótesis de Riemann — Fase 37 (modo físico)
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo — dtrejopizzo@gmail.com
**Prerrequisitos:** P43 (cuantificador maestro), Docs 70–72 (con las correcciones del Doc 105), Doc 83 ($d\nu\ge 0$), Doc 102 (Bagchi), Doc 103 (criterio de traza a escala única), Doc 108 (valor vs inercia, diana L8).
**Literatura externa:** de Bruijn (1950); Newman (1976); Csordas–Smith–Varga (1994); Ki–Kim–Lee (2009); Rodgers–Tao (arXiv:1801.05914, Forum of Math. Pi 2020); Polymath15 (Λ ≤ 0.22); Davenport–Heilbronn (1936); Bohr–Landau (1914); Montgomery (1973); Speiser (1934); Levinson–Montgomery (1974); Bagchi (1981).

---

## Resumen

Λ ≥ 0 (Rodgers–Tao) junto con RH ⟺ Λ = 0 dice que, si RH es cierta, el sistema de ceros está sentado **exactamente** en el punto crítico del flujo de De Bruijn–Newman — "barely so", en la frase de Newman. En física ningún sistema genérico ocupa su punto crítico sin un mecanismo que lo fuerce. Este documento examina los cinco mecanismos físicos candidatos — (a) simetría protectora, (b) criticalidad auto-organizada, (c) principio variacional, (d) punto fijo de renormalización, (e) ajuste fino — y pasa cada uno por el cuantificador maestro de P43.

**Resultados principales:**

1. **(§2–§3)** La prueba de Rodgers–Tao ES una instancia del mecanismo (b), pero estructuralmente **unilateral**: excluye el lado post-crítico (Λ < 0) porque su parámetro de orden — rigidez cristalina de los espaciados — es **extensivo** (visible en promedios). El lado pre-crítico (Λ > 0) tiene parámetro de orden $m$ (número de cuádruplos off-críticos), que es **intensivo** y de densidad cero (Bohr–Landau): invisible a todo promedio. La dualización "extensivo/intensivo" es el cuantificador maestro en coordenadas termodinámicas. El sándwich de relajación es inconcebible por estadísticas promediadas (Prop. 5.2).

2. **(§4)** La simetría sola no protege (Davenport–Heilbronn: ecuación funcional, sin producto de Euler, ceros off-críticos abundantes). El producto de Euler da una **protección estadística probada** (densidad cero de defectos) pero no individual. La sub-pregunta "0 o infinitos" produce el hallazgo central del documento: la **dicotomía de defectos D-109** ($m \in \{0,\infty\}$) es un enunciado *individual→individual* que NO requiere invertir el cuantificador promedio→individual, y la identidad arquitectónica
$$\mathrm{RH} \;=\; \underbrace{(m < \infty)}_{\text{L8, lado de cotas/criba}} \;\wedge\; \underbrace{(m \in \{0,\infty\})}_{\text{D-109, lado de rigidez}}$$
descompone RH en dos mitades de naturaleza distinta, ninguna de las cuales es individualmente equivalente a RH [salvo verificación en contrario, §4.6].

3. **(§6–§7)** Los mecanismos (c) y (d) colapsan: toda energía libre aritmética es evaluable solo en $t=0$ (el flujo de calor destruye el producto de Euler — $t=0$ es el único "tiempo multiplicativo"), y la cuantización entera del índice $\kappa = 2m$ es exactamente la inercia no-autónoma de P43.

**VEREDICTO: PARCIAL** — sin mecanismo demostrado, pero con un enunciado falsable nuevo (D-109) que vive fuera del muro del cuantificador maestro, y con la identificación precisa de por qué Rodgers–Tao no se dualiza.

---

## §1. Marco: el flujo, la constante, y la taxonomía de mecanismos

### §1.1 Hechos establecidos (todos teoremas, literatura verificada)

Sea $\Phi(u) = \sum_{n\ge1}(2\pi^2 n^4 e^{9u} - 3\pi n^2 e^{5u})\exp(-\pi n^2 e^{4u})$ y
$$H_t(x) = \int_0^\infty e^{tu^2}\,\Phi(u)\cos(xu)\,du,$$
de modo que $H_0(x) = \tfrac18\,\xi\!\left(\tfrac12 + \tfrac{ix}2\right)$ (normalización de Rodgers–Tao). Hechos:

- **(H1)** [de Bruijn 1950] Si los ceros de $H_{t_0}$ son todos reales, los de $H_t$ lo son para todo $t \ge t_0$; además $H_t$ tiene solo ceros reales para $t \ge 1/2$. El flujo hacia adelante **preserva la realidad**.
- **(H2)** [Newman 1976] Existe $\Lambda \in (-\infty, 1/2]$ tal que los ceros de $H_t$ son todos reales exactamente cuando $t \ge \Lambda$. RH ⟺ $\Lambda \le 0$.
- **(H3)** [Ki–Kim–Lee 2009] $\Lambda < 1/2$ estricto.
- **(H4)** [Csordas–Smith–Varga 1994] Cada "par de Lehmer" (par de ceros consecutivos anómalamente próximos) da una cota inferior explícita para $\Lambda$; con el par cerca de $\gamma \approx 7005$ obtuvieron $\Lambda > -5.895\times10^{-9}$. Mejoras posteriores con pares más finos llevaron la cota cerca de $-10^{-11}$ [Saouter–Gourdon–Demichel 2011, Math. Comp.; NO VERIFICADO el valor exacto].
- **(H5)** [Rodgers–Tao 2018/2020] $\Lambda \ge 0$ (conjetura de Newman). Por tanto **RH ⟺ Λ = 0**.
- **(H6)** [Polymath15, 2019] $\Lambda \le 0.22$.
- **(H7)** Bajo el flujo, los ceros reales $x_j(t)$ obedecen (donde la suma converge en valor principal)
$$\frac{dx_j}{dt} \;=\; -2\sum_{k\neq j}\frac{1}{x_k - x_j} \;=\; 2\sum_{k\neq j}\frac{1}{x_j - x_k},$$
es decir, **repulsión coulombiana 1D determinista** (dinámica de Dyson sin ruido), con la ecuación de calor hacia atrás en $x$: $\partial_t H = -\partial_{xx} H$.
- **(H8)** [Programa, D70 con la corrección de signo del Doc 105] $\Lambda = \inf\{t : T_\lambda(t) = 0\}$, donde $T_\lambda(t)$ es la traza CCM del estado evolucionado.

### §1.2 La observación física de partida

(H2)+(H5) dicen: **si RH es cierta, el presente aritmético $t=0$ coincide exactamente con el punto crítico $\Lambda$ del flujo.** Más fuerte aún, (H5) tiene una lectura incondicional notable:

> **Para todo $t < 0$, $H_t$ tiene al menos un cero no-real.** (Esto es exactamente $\Lambda \ge 0$.)

Es decir, incondicionalmente, en todo el pasado del flujo hay pares complejos; RH afirma que el instante en que el último par toca el eje real es **exactamente** el instante $t=0$ — ni antes (eso sería $\Lambda<0$, ya refutado) ni después. El estado aritmético sería el estado de **última colisión**.

En física, un sistema sentado en su punto crítico exacto exige explicación. Taxonomía estándar:

| Mecanismo | Ejemplo físico | ¿Qué lo haría riguroso aquí? |
|---|---|---|
| (a) Simetría protectora | transiciones protegidas por simetría | ecuación funcional + X ⟹ ceros en el eje |
| (b) Criticalidad auto-organizada (SOC) | pilas de arena, el punto crítico es atractor | la dinámica + estadística excluye $\Lambda \neq 0$ |
| (c) Principio variacional | el estado minimiza energía libre | $F(t)$ aritmética con mínimo forzado en $t=0$ |
| (d) Punto fijo de renormalización | criticalidad = punto fijo del RG | $t=0$ punto fijo de un flujo de re-escalado |
| (e) Ajuste fino externo | constantes cosmológicas | — (la aritmética no tiene ajustador) |

La pregunta del documento: ¿cuál de (a)–(d) tiene contraparte matemática rigurosa, y produce un enunciado falsable nuevo?

---

## §2. Anatomía de Rodgers–Tao: SOC unilateral con parámetro de orden extensivo

### §2.1 La estructura lógica de la prueba (verificada en fuente: arXiv:1801.05914 y el post de Tao del 19/01/2018)

La prueba es por contradicción con una estructura de tres pasos:

**Paso 0 (el truco lógico).** Supóngase $\Lambda < 0$. Entonces los ceros de $H_0$ son reales, es decir, **RH es verdadera bajo la hipótesis de contradicción**. Esto autoriza el uso de todos los resultados condicionales a RH (Montgomery, Littlewood condicional, etc.) dentro del argumento. Este paso es crucial y es lo que rompe la simetría con el lado dual (§2.3).

**Paso 1 (relajación).** Si $\Lambda < 0$, el sistema de ceros, todos reales ya en $t = \Lambda < 0$, evoluciona durante un tiempo $|\Lambda| > 0$ bajo la dinámica repulsiva (H7) antes de llegar al presente. Rodgers–Tao demuestran que esta evolución produce **convergencia a equilibrio local**: en $t=0$ los ceros se parecen localmente (en promedio) a una progresión aritmética, con espaciados pegados al espaciado medio global. Tao lo describe explícitamente como análogo al "local relaxation flow" de Erdős–Schlein–Yau en matrices aleatorias; el funcional de energía $E(t) = \sum_{j<k}\log\frac{1}{|x_j-x_k|}$-tipo decrece con $\partial_t H(t) = -4E(t)$ (disipación manifiesta). Físicamente: la repulsión determinista, sin ruido, **cristaliza** localmente la configuración.

**Paso 2 (contradicción estadística).** La rigidez cristalina local contradice las estimaciones de correlación de pares de los ceros de ζ — Montgomery (1973, condicional a RH, que está disponible por el Paso 0) y resultados relacionados (Conrey–Ghosh–Goldston–Gonek–Heath-Brown). Los ceros reales de ζ tienen fluctuaciones de espaciado demasiado grandes (compatibles con GUE, incompatibles con un reticulado local).

**Conclusión.** El estado real en $t=0$ es "demasiado desordenado" para ser el estado post-relajación de la dinámica. Por tanto $\Lambda \ge 0$.

### §2.2 Lectura SOC: respuesta a la pregunta (i), primera mitad

**Sí: la prueba es una instancia rigurosa del mecanismo (b), en su mitad excluyente.** El contenido físico exacto es:

> *El estado presente no puede estar en la fase post-crítica, porque la fase post-crítica tiene un orden detectable (rigidez cristalina de los espaciados) y el estado presente, medible en promedio, no lo tiene.*

Nótese qué tipo de cantidad separa $\Lambda < 0$ de $\Lambda \ge 0$: una **estadística promediada de espaciados** — varianza de conteo en ventanas mesoscópicas, forma de la correlación de pares. Es una propiedad **extensiva**: si $\Lambda<0$, la rigidez afecta a *todos* los ceros (proporción 1), y por eso un promedio sobre $[T, 2T]$ la ve. En el lenguaje de P43: la cantidad separadora del lado $\Lambda<0$ vive en el lado **promedio** del cuantificador, y por eso es demostrable.

### §2.3 Por qué el argumento no corre simétrico: la asimetría extensivo/intensivo

Intentemos el argumento dual. Supóngase $\Lambda > 0$. Entonces:

1. **El Paso 0 se invierte en contra.** $\Lambda > 0$ ⟺ ¬RH: hay ceros complejos en $t=0$. Ya no se puede usar ninguna herramienta condicional a RH. El arsenal estadístico disponible se reduce drásticamente (inventario en §5.1).

2. **El parámetro de orden cambia de naturaleza.** ¿Qué distingue, en $t=0$, una configuración con $\Lambda = 0$ de una con $\Lambda > 0$? Exactamente la presencia de $m \ge 1$ cuádruplos off-críticos ($m$ = número de cuádruplos, $\kappa = 2m$ en el puente de P35). Pero:

   - **[TEOREMA, Bohr–Landau 1914]** Para todo $\delta > 0$, $N(\tfrac12+\delta, T) = O(T)$, mientras $N(T) \sim \tfrac{T}{2\pi}\log T$: la proporción de ceros a distancia $\ge \delta$ del eje crítico tiende a 0. Los defectos tienen **densidad cero**.
   - Por tanto el parámetro de orden del lado $\Lambda > 0$ es **intensivo**: $m$ puede ser finito, o infinito pero de densidad cero. En ambos casos, su contribución a cualquier estadística promediada sobre $[T,2T]$ es $o(1)$.

3. **Consecuencia.** No existe estadística promediada de los ceros (reales o no) en $t=0$ que separe $\Lambda = 0$ de $\Lambda > 0$. La formalización es la Proposición 5.2.

**Respuesta a la pregunta clave de (i):** la cantidad estadística que separa $\Lambda=0$ de $\Lambda<0$ es de tipo **promedio** (varianza de espaciados — por eso Rodgers–Tao existe como teorema). La cantidad que separaría $\Lambda=0$ de $\Lambda>0$ es de tipo **individual** (existencia de $m\ge1$ defectos de densidad cero — por eso el lado dual es RH misma y el cuantificador maestro la bloquea). La asimetría de la prueba de Rodgers–Tao no es un accidente técnico: es el cuantificador maestro expresado en coordenadas termodinámicas:

$$\boxed{\text{extensivo} = \text{promedio (demostrable)}, \qquad \text{intensivo de densidad cero} = \text{individual (RH)}}$$

### §2.4 Refinamiento: qué vería un observador con acceso a promedios

Vale la pena precisarlo porque cuantifica el muro. Si $\Lambda > 0$ con $m$ finito, las estadísticas locales de los ceros reales en $t=0$ difieren de las del caso $\Lambda=0$ solo en $O(m)$ ventanas locales de tamaño $O(1)$ (las vecindades de las alturas $\gamma$ de los cuádruplos, donde la fórmula explícita local y la dinámica acoplan el par complejo con los ceros reales vecinos — ver §5.3). Fracción afectada: $O(m / (T\log T)) \to 0$. Incluso $m = \infty$ con densidad cero da fracción $o(1)$. Un observador que solo mide límites de promedios obtiene **exactamente los mismos números** en ambos mundos. Esta es la versión física de la frase de P43: "el objeto aritmético vive en el conjunto excepcional de medida nula de su propio comportamiento genérico".

---

## §3. El significado físico de Λ = 0 exacto: criticalidad con fluctuaciones a todas las escalas

### §3.1 Qué significa Λ=0 en términos de la historia del flujo

Respuesta cuidadosa a la pregunta planteada en (iii). $\Lambda = 0$ significa, por definición de ínfimo, dos cosas a la vez:

- **(λ1)** Para todo $t \ge 0$: todos los ceros de $H_t$ son reales. En particular RH.
- **(λ2)** Para todo $t < 0$: existe al menos un par de ceros complejos de $H_t$.

(λ2) es incondicional (es Rodgers–Tao). (λ1) es RH. Físicamente: **en todo el pasado del flujo hay pares complejos vivos, y el presente $t=0$ es el primer instante de realidad total.** No es que "la última colisión ocurre en $t=0$" en el sentido de una colisión única: (λ2) es compatible con una sucesión infinita de colisiones en tiempos $t_1 < t_2 < \cdots \to 0^-$, acumulándose en el presente. De hecho esta es la imagen correcta, por lo siguiente.

### §3.2 Los pares de Lehmer como fluctuaciones críticas [HEURÍSTICA + teorema CSV]

El mecanismo de Csordas–Smith–Varga (H4) es la mitad constructiva de la imagen: un par de ceros reales consecutivos anómalamente próximos en $t=0$ ("par de Lehmer") es, corriendo el flujo hacia atrás, un par que **acaba de colisionar**: para $t$ ligeramente negativo era un par complejo. Cada par de Lehmer de calidad $q$ certifica $\Lambda > -\epsilon(q)$ con $\epsilon(q) \to 0$.

Ahora bien, la estadística GUE (β=2) predice densidad de espaciados normalizados $p(s) \propto s^2$ cuando $s \to 0$: **no hay gap mínimo**. Espaciados arbitrariamente pequeños (relativos a la media) ocurren con frecuencia positiva en cada escala. Si los ceros de ζ siguen GUE localmente (apoyado por Montgomery condicional y por toda la evidencia numérica de Odlyzko), entonces hay pares de Lehmer de calidad arbitrariamente alta, y por el mecanismo CSV, $\Lambda \ge 0$. Rodgers–Tao convirtieron esta heurística en teorema por otra vía (rigidez), pero la imagen física es la misma:

> **La estadística del presente "sabe" que $\Lambda \ge 0$:** las casi-colisiones a todas las escalas son fluctuaciones críticas visibles en promedio. **La estadística no puede saber que $\Lambda \le 0$:** eso requiere certificar que ninguna casi-colisión fue, en el pasado, una colisión real consumada — un evento individual por defecto.

Esto completa la respuesta a (i): el sistema exhibe la fenomenología de un punto crítico (fluctuaciones sin escala característica, casi-degeneraciones arbitrariamente finas, ausencia de gap), y la mitad demostrable de esa fenomenología (la cota $\Lambda \ge 0$) está demostrada. La criticalidad **observable** está establecida; la criticalidad **exacta** ($\Lambda = 0$, no $\Lambda > 0$) es RH.

### §3.3 Tensión conceptual honesta: equilibrio ruidoso vs dinámica determinista [HEURÍSTICA]

Hay una observación estructural que no hemos visto explotada y registramos como heurística estricta. El flujo (H7) es la dinámica de Dyson **sin ruido** (determinista). Su equilibrio local, bajo confinamiento, es el **cristal** (espaciados iguales) — eso es lo que usa Rodgers–Tao. La estadística GUE, en cambio, es la medida de equilibrio de la dinámica de Dyson **con ruido browniano** (Dyson Brownian motion a β=2). Los ceros de ζ:

- evolucionan (en $t$) bajo la dinámica SIN ruido,
- pero exhiben (en $t=0$, conjeturalmente y en promedio demostrablemente hasta cierto rango de Fourier) la estadística de equilibrio de la dinámica CON ruido.

Es decir: el estado aritmético está en la clase de universalidad del equilibrio ruidoso sin que el flujo tenga ruido. ¿De dónde sale el "ruido"? La única fuente disponible es la aritmética misma (los primos, vía la fórmula explícita, actúan como desorden congelado — "quenched disorder" — no como ruido dinámico). En esta lectura, RH es la afirmación de que el desorden congelado de los primos reproduce exactamente, en $t=0$, un estado del borde de la clase ruidosa que el flujo determinista no puede haber preparado (si lo hubiera preparado, Rodgers–Tao se violaría). El estado en $t=0$ no es el resultado de relajación del flujo: es una **condición inicial** dictada desde fuera del flujo (por la aritmética). Esto descarta la versión fuerte de SOC — el punto crítico NO es atractor de la dinámica DBN; la dinámica no "eligió" $t=0$. Lo que ancla el presente al punto crítico, si algo lo hace, no es la dinámica: hay que buscarlo en la estructura que existe solo en $t=0$ (§6.2).

---

## §4. Simetría protectora: qué protege la ecuación funcional, qué protege Euler, y la dicotomía de defectos

### §4.1 La simetría sola no protege [TEOREMA, verificado]

La ecuación funcional $\xi(s) = \xi(1-s)$ es la simetría $\mathbb{Z}_2$ del sistema (reflexión respecto del eje crítico; en coordenadas $x$, realidad de $H_0$). ¿Protege por sí sola la criticalidad? **No**, y el contraejemplo es clásico y está verificado:

- **[Davenport–Heilbronn 1936]** La función $f(s) = \sum_n \xi_5(n)n^{-s}$ (combinación lineal explícita de dos L-funciones de Dirichlet mod 5) satisface una ecuación funcional del tipo de la de ζ y **tiene infinitos ceros con $\sigma > 1$** (y, como se sabe hoy, abundantes ceros en la banda $\tfrac12 < \sigma < 1$; cómputos explícitos en Balanzario–Sánchez-Ortiz, Math. Comp. 76 (2007)).
- La diferencia estructural decisiva: $f$ **no tiene producto de Euler** (es combinación lineal de dos funciones que sí lo tienen, pero la combinación lo destruye).
- Más aún, para combinaciones lineales no-triviales de L-funciones hay resultados generales de existencia de muchos ceros off-críticos vía universalidad (Nakamura–Pańkowski 2012 y trabajos posteriores; el orden de magnitud exacto del conteo off-crítico que dan esos teoremas: [NO VERIFICADO en detalle], pero la infinitud es teorema).

Conclusión rigurosa: **simetría sin multiplicatividad no protege nada** — ni siquiera estadísticamente: los defectos de Davenport–Heilbronn no son raros.

### §4.2 Lo que el producto de Euler sí protege (y está probado): protección estadística

Para ζ (simetría + producto de Euler) la situación es radicalmente distinta, y la diferencia es teorema:

- **[Bohr–Landau 1914]** $N(\sigma, T) = O(T)$ para cada $\sigma > 1/2$: densidad relativa cero de defectos. La prueba usa el producto de Euler de manera esencial (segundo momento de $\zeta$/polinomios de Dirichlet, mollifiers).
- **[Teoremas de densidad, Carlson en adelante]** $N(\sigma,T) = O(T^{c(\sigma)})$ con $c(\sigma) < 1$ para $\sigma > 1/2$, mejorando hacia la hipótesis de densidad.

Es decir: el enunciado físico "simetría + producto de Euler ⟹ criticalidad protegida" tiene una versión **estadística probada** (los defectos tienen densidad cero — la fase off-crítica nunca es extensiva) y una versión **individual** (no hay defectos: $m=0$) que es exactamente RH y exactamente MW-2. La brecha entre ambas es, una vez más, el cuantificador maestro: densidad cero (promedio) vs conjunto vacío (individual). Hasta aquí, todo colapsa al muro conocido.

### §4.3 La sub-pregunta genuina: ¿0 o infinitos? Estado del arte

Pregunta: ¿puede el producto de Euler coexistir con **exactamente un** cuádruplo off-crítico? ¿Hay rigidez "0 o ∞"?

**Inventario honesto de lo que se sabe (tipo "si hay un cero off-crítico entonces [estructura]"):**

1. **[Speiser 1934]** RH ⟺ $\zeta'$ no tiene ceros en $0 < \sigma < 1/2$. Contrapositivo individual: un cero de ζ off-crítico fuerza un cero de $\zeta'$ a la izquierda del eje.
2. **[Levinson–Montgomery 1974]** Versión cuantitativa: $N_1^-(T) = N^-(T) + O(\log T)$ — los conteos de ceros de $\zeta$ y de $\zeta'$ a la izquierda del eje crítico coinciden salvo $O(\log T)$. Rigidez de apareamiento defecto↔defecto-derivada, pero no produce multiplicación de defectos.
3. **[Bagchi 1981 + Bohr–Landau; cf. Doc 102]** RH ⟺ ζ es fuertemente recurrente (se autoaproxima) en $\tfrac12<\sigma<1$. La dirección relevante aquí es el contrapositivo de la mitad fácil: **si ζ tiene un cero off-crítico, entonces ζ NO es fuertemente recurrente.** La prueba es el mecanismo de clonación: si ζ se autoaproximara con densidad positiva de casi-períodos, Rouché clonaría el cero off-crítico en $\gg T$ copias hasta altura $T$, contradiciendo Bohr–Landau. Esto es un teorema genuino del tipo buscado: **un solo defecto individual destruye una propiedad dinámica global** (la recurrencia fuerte). Es la pieza de rigidez individual→global más fuerte que conocemos en la literatura.
4. **Lo que NO se sabe:** ningún teorema publicado que conozcamos prueba "$m \ge 1 \Rightarrow m = \infty$" para ζ. La búsqueda en la literatura no arroja un resultado de dicotomía; lo declaramos **abierto** [estado verificado hasta donde alcanza la búsqueda; NO VERIFICADO exhaustivamente].

### §4.4 La dicotomía de defectos D-109: enunciado falsable

**Enunciado D-109 (dicotomía de defectos).** *El conjunto de ceros off-críticos de ζ es vacío o infinito: $m \in \{0, \infty\}$. Equivalentemente: ζ no puede tener un número finito positivo de cuádruplos off-críticos.*

Generalización natural (más falsable): *ningún elemento de la clase de Selberg tiene un número finito positivo de ceros no-triviales fuera de su eje crítico.*

**Por qué es físicamente plausible (heurística declarada):** en sistemas con interacción de largo alcance, un defecto aislado en un medio crítico es inestable: o se aniquila o nuclea una fase. La clonación de Bagchi es la sombra matemática de la nucleación: un defecto + recurrencia ⟹ defectos extensivos. Lo que falta es el régimen intermedio: un defecto + recurrencia débil ⟹ defectos infinitos (no necesariamente extensivos).

**Por qué las rutas conocidas no la prueban (honestidad):** la ruta natural es clonar el cero por casi-periodicidad. Lo incondicional es la casi-periodicidad $B^2$ (en media cuadrática) de ζ en $\sigma > 1/2$ — los casi-períodos en media existen y son relativamente densos. Pero Rouché necesita aproximación **uniforme en un disco específico** alrededor del cero, y media cuadrática sobre la recta no da control puntual sobre el disco individual: es el paso media→uniforme, el mismo muro. La versión fuerte (recurrencia con densidad positiva) clona demasiado ($\gg T$ ceros, contradicción con Bohr–Landau) y por eso es equivalente a RH (Bagchi); la versión débil (clonación a lo largo de alguna sucesión $\tau_k \to \infty$, que daría exactamente D-109) requiere control puntual en los $\tau_k$ — más débil que invertir el cuantificador en todas partes, pero puntual al fin. **GAP ABIERTO.** Lo que registramos: D-109 necesita una versión *secuencial* del cuantificador, no la inversión total; queda estrictamente entre lo incondicional y RH.

### §4.5 Por qué D-109 importa: la descomposición arquitectónica de RH

Aquí está el hallazgo estructural del documento. El ledger de P43 dejó como diana L8 (Doc 108, §8.2): una cota de índices por ventana $\kappa_W \le C\cdot n_W$ daría $m \le C/2$ — es decir, **finitud de los defectos** ($m < \infty$), un objetivo estrictamente más débil que RH, del lado de las cotas de criba (lo que la paridad no bloquea: acotar, no distinguir). Combinándola con D-109:

$$\mathrm{RH} \;\Longleftrightarrow\; \big(m < \infty\big) \;\wedge\; \big(m \in \{0, \infty\}\big).$$

La identidad es trivial como lógica; lo no-trivial es que **parte RH en dos mitades de tipo distinto**:

- **Mitad L8 (finitud):** es una COTA. Las cotas son promedio-compatibles: no piden distinguir el signo de nada, solo majorizar. Doc 108 mostró que la versión disponible está detrás del muro, pero su *forma* (cota superior de un índice) es la forma de enunciado que los métodos de promedio podrían en principio alcanzar — no exige certificar un cero exacto, solo un techo finito.
- **Mitad D-109 (dicotomía):** es una RIGIDEZ individual→individual: "un defecto fuerza infinitos defectos". **No requiere invertir el cuantificador promedio→individual** — su hipótesis y su conclusión son ambas individuales. El muro de P43 no se aplica *a su enunciado* (sí, como vimos, a las rutas de prueba conocidas).

Ninguna de las dos mitades es, por separado y de manera obvia, equivalente a RH (verificación pendiente en §4.6). Esta es la primera descomposición de RH que el programa produce en la que el cuantificador maestro no bloquea ambas piezas por la misma razón.

### §4.6 Auditoría de la descomposición [honestidad]

¿Es alguna mitad secretamente equivalente a RH?

- ¿$(m<\infty) \Rightarrow$ RH? No de manera conocida: un mundo con $m=3$ cuádruplos satisface finitud y viola RH. La finitud NO es RH disfrazada *como enunciado*; la diana L8 es genuinamente más débil. (Que su prueba por la ruta del Doc 108 exigiera RH es propiedad de la ruta, no del enunciado.)
- ¿D-109 $\Rightarrow$ RH? No: D-109 es compatible con $m=\infty$ (mundo con infinitos defectos de densidad cero). Tampoco RH ⟹ D-109 trivialmente... sí: si RH, $m=0 \in \{0,\infty\}$. D-109 es consecuencia de RH, estrictamente más débil (un mundo ¬RH con $m=\infty$ satisface D-109).
- ¿Las rutas se contaminan? El riesgo real: que toda prueba imaginable de D-109 pase por recurrencia fuerte (=RH, Bagchi). No demostrado; la versión secuencial identificada en §4.4 es lógicamente más débil que la recurrencia fuerte. GAP ABIERTO, pero no colapso demostrado.

**Respuesta a (ii):** la simetría protege solo junto con el producto de Euler; la protección probada es estadística (densidad cero); la versión parcial demostrable nueva más prometedora no es una mejora de densidad sino la dicotomía D-109, que vive en un eje ortogonal al muro (individual→individual) y que, combinada con la diana L8 ya nombrada por el programa, recompone RH.

---

## §5. La dinámica de Dyson y el sándwich de relajación

### §5.1 Inventario de estadísticas incondicionales de los ceros reales

Para evaluar si el lado $\Lambda \le 0$ podría probarse por "sub-relajación detectable", inventariamos qué se sabe SIN RH (recordar §2.3: bajo $\Lambda>0$, RH es falsa y lo condicional se cae):

| Estadística | Resultado | ¿Condicional? |
|---|---|---|
| Conteo global $N(T) = \tfrac{T}{2\pi}\log\tfrac{T}{2\pi e} + \tfrac78 + S(T) + O(1/T)$ | Riemann–von Mangoldt | NO |
| $S(T) = O(\log T)$ | Backlund/clásico | NO |
| Momentos de $S(T)$: $\int_0^T S(t)^{2k}dt \sim c_k T(\tfrac1{2\pi^2}\log\log T)^k$ (CLT gaussiano) | Selberg | **NO** (la versión incondicional existe; bajo RH mejora constantes) |
| Densidad cero off-eje | Bohr–Landau, Carlson | NO |
| Proporción positiva de ceros EN el eje | Selberg; ≥ 41% Conrey/mejoras | NO |
| Correlación de pares $F(\alpha)$, $|\alpha|<1$ | Montgomery 1973 | **SÍ (RH)** |
| Espaciados: $\liminf \tilde\delta_n < 1 < \limsup \tilde\delta_n$ (gaps menores y mayores que la media) | Selberg, luego mejoras (bajo RH las mejoras fuertes) | parcialmente NO |
| Varianza de conteo en ventanas / Fujii | bajo RH las formas fuertes | mayormente SÍ |

Lo esencial: lo incondicional robusto es **Selberg** (CLT de $S(T)$: fluctuaciones gaussianas de tamaño $\sqrt{\log\log T}$) y la **densidad cero**. La correlación de pares fina es condicional.

### §5.2 El sándwich es inconcebible por promedios [riguroso, casi tautológico, pero hay que decirlo]

**Proposición 5.2 (invisibilidad del lado pre-crítico).** Sea $S$ cualquier funcional de la configuración de ceros de $H_0$ definido como límite de promedios locales: $S = \lim_{T\to\infty}\frac{1}{N(T)}\sum_{\gamma_n \le T} \phi(\text{configuración local normalizada en } \gamma_n)$ con $\phi$ acotada (esto incluye correlaciones de pares con test integrable, distribuciones de espaciados, varianzas de conteo normalizadas). Sean $Z_0$ una configuración con $\Lambda = 0$ y $Z_1$ una configuración con $\Lambda > 0$ cuyo conjunto de defectos tiene densidad cero (lo cual es automático por Bohr–Landau) y que coincide con $Z_0$ fuera de las ventanas de los defectos. Entonces $S(Z_0) = S(Z_1)$.

*Demostración.* Los sumandos en que las configuraciones difieren son $o(N(T))$ por densidad cero, y $\phi$ es acotada; el límite del promedio no cambia. $\square$

El contenido no-tautológico es la entrada de Bohr–Landau: **todo** mundo ¬RH tiene defectos de densidad cero — la naturaleza no nos concede un mundo ¬RH "extensivo" que un promedio pudiera ver. Por tanto:

> **El sándwich (Λ≥0 por sobre-relajación + Λ≤0 por sub-relajación estadística) es inconcebible.** La mitad Λ≥0 existe (Rodgers–Tao) porque la sobre-relajación es extensiva. La mitad Λ≤0 no puede provenir de ninguna estadística promediada: requiere información individual. Es el cuantificador maestro, sin escapatoria por el lado dinámico.

### §5.3 ¿Qué dejaría un defecto en los ceros reales vecinos? [HEURÍSTICA cuantificada]

Para completitud: si hay un par complejo $x_0 \pm iy$ en $t=0$ (cuádruplo con la simetría), su huella sobre los ceros reales vecinos es real pero local. En el modelo desacoplado, la ecuación de calor hacia atrás $\partial_t H = -\partial_{xx}H$ aplicada a $(x-x_0)^2 + y^2$ da ceros $x_0 \pm i\sqrt{y^2 - 2t}$: el par colisiona en $t = y^2/2$. Antes de la colisión, el par ejerce sobre un cero real a distancia $d$ una fuerza $\sim -2\cdot 2(x-x_0)/((x-x_0)^2+y^2)$ — una perturbación dipolar de alcance $O(1)$ en unidades de espaciado local. Tras la colisión ($t > y^2/2$), los dos ceros nuevos reales empujan a sus vecinos y la perturbación se relaja difusivamente. Huella total en $t=0$ futuro: deformación $O(1)$ de $O(1)$ espaciados por defecto. Con $m$ defectos: $O(m)$ espaciados anómalos entre $\sim T\log T$. Detectabilidad por máximos (no promedios): un solo espaciado anómalo es, de nuevo, un evento individual. Cierra coherentemente con la Prop. 5.2.

**Respuesta a (iii):** Λ=0 significa que el presente es el primer instante de realidad total con colisiones acumulándose en todo el pasado inmediato (λ2 incondicional); el dual de Rodgers–Tao no existe porque la sub-relajación que dejaría $\Lambda>0$ es local y de densidad cero — el lado $\Lambda\le0$ del sándwich requiere inevitablemente información individual.

---

## §6. ¿Principio variacional? El tiempo multiplicativo único

### §6.1 La energía libre del programa y su evaluación

El candidato natural del programa: $F(t) := T_\lambda(t)$ (traza CCM del estado evolucionado), con (H8): $\Lambda = \inf\{t : T_\lambda(t) = 0\}$ (D70, corregido Doc 105). Con el criterio a escala única (Doc 103): RH ⟺ $T_{\lambda_0}(0) = 0$. La estructura variacional deseada sería: $F$ computable desde los primos, $F \ge 0$, $F(t) = 0$ exactamente en $t \ge \Lambda$, y una evaluación aritmética que fuerce $F(0) = 0$.

Estado real de cada pieza:

- $F \ge 0$ y la caracterización del ínfimo: lado de ceros, riguroso (D70/D103, con $d\nu \ge 0$ de D83).
- Lado aritmético en $t=0$: D72 da $T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p (\log p/\sqrt p)\,B_\lambda(\log p)$ vía fórmula de Weil — pero el Doc 105 probó que la serie de primos **diverge** como $(5\sqrt2/8)\log X$: la fórmula es estrictamente formal. La evaluación aritmética honesta de $F(0)$ no está disponible ni siquiera formalmente regularizada sin pasar por los ceros.
- $\partial_t F|_0$: D71 mostró cancelación exacta bajo RH; el Doc 105 corrigió que el signo bajo ¬RH es GAP ABIERTO.

### §6.2 La obstrucción estructural: el flujo destruye la multiplicatividad

Hay una razón de fondo, más limpia que los detalles anteriores, por la que **todo** principio variacional aritmético sobre el flujo colapsa, y conviene dejarla aislada:

**Observación 6.2 (el tiempo multiplicativo único).** $H_0$ es, salvo normalización, $\xi(\tfrac12 + \tfrac{ix}{2})$: tiene detrás una serie de Dirichlet con producto de Euler. Para $t \neq 0$, $H_t$ es una deformación de calor de $\Phi$; el coeficiente $e^{tu^2}$ destruye la estructura multiplicativa — $H_t$ no es (que se sepa, y genéricamente no puede ser) la función ξ de ningún objeto aritmético con producto de Euler. **El eje temporal del flujo interseca a la aritmética en exactamente un punto: $t=0$.**

Consecuencias:

1. Cualquier "energía libre aritmética" $F(t)$ solo puede evaluarse desde los primos en $t = 0$. Para localizar el mínimo (o el borde del conjunto de anulación) se necesita comparar $F$ en un entorno de $t=0$ — y para $t \neq 0$ el único acceso es el lado de ceros. **Transmutación, patrón Doc 99:** la información variacional que decidiría RH se obtiene exactamente de aquello que RH afirma. El mecanismo (c) colapsa.
2. Pero la observación reformula el problema de manera iluminadora: RH es la afirmación de que **el tiempo crítico del flujo analítico coincide con el tiempo multiplicativo:**
$$\Lambda \;=\; t_{\mathrm{arit}} \;(=0).$$
Dos estructuras ajenas — la ecuación de calor (aditiva, analítica) y el producto de Euler (multiplicativo, aritmético) — comparten un punto, y RH dice que ese punto compartido es además el punto crítico de la primera estructura. Ningún principio interno al flujo puede saber dónde está $t_{\mathrm{arit}}$ (el flujo no ve los primos: conmuta con la pérdida de la serie de Dirichlet); ningún principio interno a la aritmética ve el flujo (los primos viven solo en $t=0$). El acople es exactamente el contenido de RH. Esta es la forma "física" de MW-2 (la información multiplicativa no se propaga), ahora en coordenadas de flujo: **la información multiplicativa no se propaga en $t$ porque la multiplicatividad no existe en $t\neq0$.**

**Respuesta a (iv):** no encontramos — y damos la razón estructural de que no puede encontrarse por esta vía — una energía libre aritmética cuyo mínimo localice $\Lambda$: la evaluación aritmética existe en un solo punto del eje $t$, y un principio variacional necesita comparar puntos vecinos. Mecanismo (c): colapsa por transmutación.

---

## §7. ¿Renormalización o protección topológica?

### §7.1 Los puntos fijos del flujo y su clase de universalidad

El flujo DBN tiene una estructura de renormalización pobre: hacia adelante ($t \to +\infty$, tras re-escalar) el atractor es el **cristal** (de Bruijn: para $t \ge 1/2$ realidad; asintóticamente los ceros se aproximan a un reticulado — la clase "clock"). Es el punto fijo trivial/orden. No hay punto fijo no-trivial conocido del flujo determinista que tenga la estadística GUE; GUE es el punto fijo de la dinámica **con ruido** (§3.3). El estado en $t=0$ no es punto fijo de nada: el flujo lo atraviesa. Mecanismo (d) en sentido literal: **no aplica** — la criticalidad de $t=0$ no es un punto fijo de re-escalado del propio flujo.

### §7.2 Cuantización del índice: protección topológica y su lectura honesta

La versión más seria de (a)/(d) en el programa es la cuantización entera del parámetro de orden: $\kappa = \mathrm{neg.ind} = 2m \in 2\mathbb{Z}_{\ge0}$ (P35; cada cuádruplo aporta exactamente 2). Un parámetro de orden entero es el sello de la protección topológica: no puede variar continuamente, solo saltar. ¿Protege esto la criticalidad? Análisis:

- Lo que la cuantización SÍ da: la transición $m=0 \to m=1$ es discreta; no hay "RH casi-verdadera". El conjunto de mundos ¬RH está separado del mundo RH por un salto entero del índice. Esto es estructura genuina (y es exactamente lo que hace falsable la dicotomía D-109: $m$ no puede ser "medio cuádruplo").
- Lo que la cuantización NO da: una cota inferior de $\Lambda$ en función de $m$. Del modelo de §5.3: un cuádruplo a distancia $y$ del eje realifica en tiempo $\sim y^2/2$; con $y$ arbitrariamente pequeño, $\Lambda$ puede ser arbitrariamente pequeño con $m = 1$. **No hay teorema de gap "$\Lambda \in \{0\} \cup [c, \infty)$"** y la dinámica no lo sugiere: la cuantización vive en $m$, no en $\Lambda$. (Si tal gap existiera con $c$ explícito, RH sería verificable por cómputo finito vía Polymath15-style: razón de más para no esperarlo barato.)
- Y el golpe final es P43: leer $m$ (la inercia) requiere las posiciones de los ceros — la inercia no es autónoma (Doc 108). La protección topológica existe *ontológicamente* pero su detector no es accesible aritméticamente. Mecanismo (a)/(d) en versión topológica: **colapsa exactamente en el muro valor/inercia.**

---

## §8. La pasada por el cuantificador maestro (P43)

Tabla final, mecanismo por mecanismo — la pregunta de (v): ¿la versión matemática del mecanismo requiere invertir promedio→individual?

| Mecanismo | Versión matemática | ¿Dónde está el cuantificador? | Veredicto |
|---|---|---|---|
| (a) Simetría protectora | ec. funcional + Euler ⟹ ceros en el eje | la protección probada es estadística (densidad cero); la individual ES MW-2 | **Colapsa** (es el muro) |
| (b) SOC / Rodgers–Tao | exclusión post-crítica por rigidez | lado Λ<0: parámetro de orden extensivo → demostrable (¡y demostrado!); lado Λ>0: parámetro intensivo de densidad cero → individual | **Mitad probada, mitad ES el muro**; dual imposible (Prop. 5.2) |
| (c) Variacional | $F(t)$ aritmética con mínimo en Λ | la aritmética existe solo en $t=0$ (tiempo multiplicativo único); comparar vecinos = lado de ceros | **Colapsa** (transmutación, Doc 99) |
| (d) RG / topológico | cuantización $\kappa = 2m$ | el invariante es entero (individual) pero leerlo = inercia no autónoma | **Colapsa** (valor/inercia, Doc 108) |
| (e) Ajuste fino | — | — | vacío: la aritmética no tiene ajustador; si RH es cierta sin mecanismo, es "accidental" — ininteresante y no falsable |
| **D-109 (nuevo)** | un defecto ⟹ infinitos defectos | hipótesis individual, conclusión individual: **no hay inversión promedio→individual en el enunciado** | **NO colapsa como enunciado**; las rutas de prueba conocidas (clonación por recurrencia) sí reencuentran el muro en versión secuencial debilitada |

La salida esperada se confirma: (a), (c), (d) colapsan; (b) está medio probado y su otra mitad es el muro. Lo que no colapsa *como enunciado* es D-109 — precisamente porque no es un mecanismo de anclaje de Λ sino una rigidez del conjunto de defectos, ortogonal al eje promedio/individual.

Una precisión brutalmente honesta, para no sobrevender D-109: que el enunciado no requiera la inversión del cuantificador no significa que su prueba sea más fácil que RH — significa que el argumento de imposibilidad de P43 **no se aplica a él**. P43 mostró que toda forma de argumento del programa muere en la inversión promedio→individual; D-109 es el primer objetivo natural del programa cuyo enunciado no contiene esa inversión. Puede haber (y seguramente hay) otros muros; el identificado en §4.4 es el paso media-cuadrática→puntual-secuencial de la casi-periodicidad, que es una forma estrictamente más débil de la misma dificultad (se necesita en una sucesión de puntos, no uniformemente). Si ese paso debilitado es tan duro como el original es, hoy, GAP ABIERTO — y es la pregunta correcta que este documento deja.

---

## §9. VEREDICTO

**PARCIAL.**

**Lo que el modo físico estableció:**

1. **El anclaje crítico tiene su mitad demostrada y su mitad imposible-por-promedios.** Rodgers–Tao es genuinamente el mecanismo (b) — exclusión de la fase post-crítica por exceso de desorden — y funciona porque el orden post-crítico es extensivo. El lado pre-crítico tiene parámetro de orden intensivo de densidad cero (Bohr–Landau lo garantiza en TODO mundo ¬RH), de modo que ninguna estadística promediada separa $\Lambda = 0$ de $\Lambda > 0$ (Prop. 5.2). El sándwich de relajación es inconcebible; el cuantificador maestro reaparece como dicotomía extensivo/intensivo. No hay mecanismo dinámico de anclaje: el punto crítico no es atractor del flujo, y $t=0$ es condición inicial aritmética, no estado relajado.

2. **El tiempo multiplicativo único (Obs. 6.2).** El flujo de calor destruye el producto de Euler; el eje $t$ toca la aritmética en exactamente un punto. RH = "el tiempo crítico del flujo coincide con el tiempo multiplicativo". Esto entierra el mecanismo variacional (c) por razón estructural, no técnica, y reformula MW-2 en coordenadas de flujo.

3. **La cuantización protege ontológicamente, no epistémicamente.** $\kappa = 2m$ es entero (protección topológica real), pero su lectura es la inercia no-autónoma de P43. No hay gap theorem para $\Lambda$ ($\Lambda$ puede ser arbitrariamente pequeño con $m=1$).

**El enunciado falsable más prometedor:**

> **D-109 (dicotomía de defectos):** el conjunto de ceros off-críticos de ζ es vacío o infinito ($m \in \{0,\infty\}$). Versión fuerte: ningún elemento de la clase de Selberg tiene un número finito positivo de ceros fuera de su eje crítico.

Con la identidad arquitectónica $\mathrm{RH} = (m<\infty) \wedge (m\in\{0,\infty\})$: la mitad izquierda es la diana L8 del ledger (cota de criba, forma promedio-compatible); la mitad derecha es D-109 (rigidez individual→individual, fuera del alcance del no-go de P43). Es la primera partición de RH producida por el programa en la que las dos piezas no están bloqueadas por la misma razón.

**Falsadores de D-109:**
- Directo: construir un elemento de la clase de Selberg (con producto de Euler y ecuación funcional) con exactamente un cuádruplo off-crítico, o demostrar la consistencia relativa de $m=1$ para ζ con la fórmula explícita + $d\nu \ge 0$ + positividad sub-resolución (Thm 3.3 del Doc 108).
- Indirecto (falsador de su utilidad): demostrar que toda prueba de D-109 requiere la recurrencia fuerte de Bagchi (= RH), es decir, que la versión secuencial del paso media→puntual identificada en §4.4 es equivalente a la versión uniforme. Eso devolvería D-109 al muro y el veredicto bajaría a SIN MECANISMO.

**Próximo paso concreto (Phase 37 continuación):** atacar la versión secuencial — ¿existe una sucesión $\tau_k \to \infty$ con $\zeta(s + i\tau_k) \to \zeta(s)$ uniformemente en un disco compacto fijo de $\tfrac12 < \sigma < 1$, incondicionalmente? (Nótese: para D-109 basta que exista *alguna*; la casi-periodicidad $B^2$ incondicional da candidatas en media; el gap es media→puntual en una sucesión, no en densidad positiva.)

---

## Apéndice: referencias externas citadas (todas verificadas salvo marca)

- N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. 17 (1950), 197–226.
- C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. 61 (1976), 245–251.
- G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann Hypothesis*, Constr. Approx. 10 (1994), 107–129.
- H. Ki, Y.-O. Kim, J. Lee, *On the de Bruijn–Newman constant*, Adv. Math. 222 (2009), 281–306.
- B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, Forum of Math. Pi 8 (2020), e6; arXiv:1801.05914. [Estructura de la prueba verificada en fuente: dinámica $\dot x_j = 2\sum_{k\neq j}(x_j-x_k)^{-1}$, relajación a equilibrio local estilo Erdős–Schlein–Yau, contradicción con correlación de pares de Montgomery y CGGGH-B, uso del hecho de que $\Lambda<0 \Rightarrow$ RH habilita herramientas condicionales.]
- D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ-function, and a new upper bound for the de Bruijn–Newman constant*, Res. Math. Sci. (2019); $\Lambda \le 0.22$.
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. 11 (1936), 181–185 y 307–312.
- E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp. 76 (2007), 2045–2049.
- H. Bohr, E. Landau, *Ein Satz über Dirichletsche Reihen mit Anwendung auf die ζ-Funktion und die L-Funktionen*, Rend. Circ. Mat. Palermo 37 (1914), 269–272. [Densidad cero off-eje.]
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Symp. Pure Math. 24 (1973), 181–193. [Condicional a RH.]
- A. Speiser, *Geometrisches zur Riemannschen Zetafunktion*, Math. Ann. 110 (1934), 514–521.
- N. Levinson, H. L. Montgomery, *Zeros of the derivatives of the Riemann zeta-function*, Acta Math. 133 (1974), 49–65.
- B. Bagchi, *A joint universality theorem for Dirichlet L-functions* / tesis (1981); recurrencia fuerte ⟺ RH. [Cf. Doc 102 del programa.]
- A. Selberg, *Contributions to the theory of the Riemann zeta-function* (1946). [CLT incondicional para $S(T)$.]
- T. Nakamura, Ł. Pańkowski, trabajos sobre ceros off-críticos de combinaciones lineales de L-funciones (2012–) [infinitud verificada; conteos precisos NO VERIFICADOS].
- Y. Saouter, X. Gourdon, P. Demichel, *An improved lower bound for the de Bruijn–Newman constant*, Math. Comp. 80 (2011) [valor exacto NO VERIFICADO].

Citas internas del programa: P35, P39, P41, P42, P43; Docs 70, 71, 72 (con correcciones del Doc 105), 83, 89, 99, 102, 103, 104, 105, 106, 107, 108.

---

*Fin del Documento 109.*
