# Doc 46 — El Quiebre: Tres Estructuras Matemáticas Nuevas para RH

**Programa:** CCM Zeta Spectral Triples — Phase 29/32  
**Fecha:** junio 2026  
**Prerrequisitos:** Docs 38–45  
**Naturaleza:** Documento estratégico — propuesta de matemática nueva. No es un paper de resultados probados. Es una hoja de ruta para construir estructuras que hoy no existen.

---

## Prólogo: por qué "dar vueltas" no basta

Docs 42–45 demostraron la siguiente verdad incómoda: cada ruta analítica al Problema de la Medida de Cero ($\mu_{\mathrm{off}} = 0$) termina con una condición equivalente a RH. Las herramientas existentes — Fourier, potencial armónico, transformada de Poisson, correlaciones de pares (Montgomery), función de Hardy $H^1$ — todas son *traductoras*, no *proofas*. Traducen RH a otro lenguaje igualmente difícil.

El patrón histórico en matemática es bien conocido: cuando el obstáculo persiste después de agotar las herramientas disponibles, la solución requiere crear las herramientas que faltan. La prueba de Fermat (Wiles) necesitó la teoría de formas modulares y representaciones de Galois. La prueba de Poincaré (Perelman) necesitó el flujo de Ricci. La prueba de Weil para curvas (las "pruebas sencillas" de RH) necesitó el álgebra de cohomología de Lefschetz aplicada a superficies algebraicas.

Lo que falta aquí es análogo: una estructura donde la condición $\mu_{\mathrm{off}} = 0$ no sea una *equivalencia* a demostrar sino una *consecuencia* de axiomas más profundos.

Este documento propone tres estructuras matemáticas genuinamente nuevas.

---

## I. La Teoría de Medidas $\zeta$-Compatibles

### I.1 El objeto central

El programa ha identificado $\mu_{\mathrm{off}}$ como el objeto fundamental: una medida de Borel positiva en $\mathbb{H} = \{(x,y): y > 0\}$ que satisface un conjunto de restricciones impuestas por la aritmética de $\zeta$. La pregunta es: ¿cuáles son *todas* las restricciones? ¿Y son suficientes para forzar $\mu_{\mathrm{off}} = 0$?

**Definición I.1 (Medida $\zeta$-compatible).** Una medida de Borel positiva $\mu$ en $\mathbb{H}$ es *$\zeta$-compatible* si satisface:

1. **Simetría de Hadamard:** $\mu$ es invariante bajo conjugación $(x,y)\mapsto(-x,y)$ (los ceros vienen en pares $(\rho,\bar\rho)$).

2. **Cuarteto funcional:** Si $(x,y) \in \text{sop}(\mu)$, entonces $(-x,y)$, $(x,1-y-1/2)$... [más precisamente: si $\sigma_0+i\gamma_0$ es soporte, también lo es $(1-\sigma_0)+i\gamma_0$, pero con $1-\sigma_0 < 1/2$ que cae fuera de $\mathbb{H}$ en nuestra parameterización — la restricción es que la medida "imagen" por la ecuación funcional es la misma medida reflejada].

3. **Restricción de la región libre de ceros:** $\text{sop}(\mu) \subset \{(x,y): y \leq 1/2 - c/\log(|x|+2)\}$ (region libre de ceros clásica de Korobov-Vinogradov).

4. **Restricción de densidad:** Para todo $R > 0$ y $\sigma_0-1/2 = y_0$: $\mu(\{|x|\leq R, y = y_0\}) \leq C R^{2(1-\sigma_0)}\log R$ (estimación de Ingham-Montgomery).

5. **Condición de Poisson:** La transformada de Poisson $\mathcal{P}[\mu]$ se extiende a función armónica positiva en $\mathbb{H}^+$ cuya traza en $\mathbb{R}$ coincide con $C_\infty = \mathcal{P}[\mu_{\mathrm{off}}]$ (auto-consistencia).

6. **Condición de integrabilidad:** $\int_\mathbb{H} y\,d\mu(x,y) < \infty$ (masa finita pesada).

### I.2 El teorema de clasificación (conjetural)

**Conjetura I.2 (Clasificación de medidas $\zeta$-compatibles).**

$$\mathcal{M}_\zeta := \{\mu \text{ positiva en } \mathbb{H} : \mu \text{ es $\zeta$-compatible}\} = \{0\}$$

Es decir, la *única* medida $\zeta$-compatible es la medida nula. Esta conjetura es equivalente a RH.

### I.3 Por qué esta formulación es nueva

Las condiciones 1–6 son todas consecuencia de propiedades conocidas de $\zeta$ — pero *nunca se han estudiado juntas como sistema*. La pregunta "¿qué medidas positivas en $\mathbb{H}$ satisfacen simultáneamente todas estas condiciones?" es nueva en la literatura.

Cada condición por separado admite medidas no nulas. La pregunta es si el sistema *completo* es vacío (aparte de $\mu = 0$). Esto es un problema de *rigidez de sistemas de restricciones*, análogo a los problemas de rigidez en geometría diferencial (Mostow, Margulis) donde un conjunto de condiciones simétricas fuerza la trivialidad.

### I.4 Programa de investigación

**Paso I.A:** Demostrar que las condiciones 1–4 implican que $\text{sop}(\mu)$ tiene densidad cero (i.e., es un conjunto muy disperso en $\mathbb{H}$). Esto usaría la estimación de densidad de Ingham de forma cuantitativa.

**Paso I.B:** Demostrar que las condiciones 4–5 juntas implican que si $\mu \neq 0$, entonces $\mathcal{P}[\mu]$ no puede ser auto-consistente (viola la condición 5). Esta es la parte genuinamente nueva: la auto-consistencia de la condición de Poisson como restricción sobre la medida generatriz.

**Paso I.C:** Demostrar que las condiciones 1–2 (simetría) más 3 (región libre) implican que $\text{sop}(\mu)$ debe estar lejos del eje $y=0$, pero la condición 6 (masa finita) hace imposible que una medida alejada del eje tenga soporte no vacío compatible con las condiciones de densidad.

---

## II. El Operador de Déficit como Mapa de Resolución

### II.1 La idea central

En la teoría de sheaves y cohomología, la forma de probar que un objeto es cero es encontrar una *resolución* — una secuencia exacta de objetos más simples que "resuelve" el objeto. Si todos los objetos en la resolución son triviales, el objeto original es trivial.

La idea aquí: tratar $\mu_{\mathrm{off}}$ no como una medida estática sino como el *núcleo de un operador de deformación*. Si podemos construir un operador $\mathcal{D}$ tal que $\ker(\mathcal{D}) = \{\mu_{\mathrm{off}} : \text{RH falla}\}$, y si $\mathcal{D}$ tiene propiedades de Fredholm (índice 0, kernel trivial bajo condiciones apropiadas), entonces RH es la afirmación de que $\ker(\mathcal{D}) = \{0\}$.

### II.2 Construcción del operador

**Definición II.1 (El operador de Déficit-Hadamard).** Sea $\mathcal{H}$ el espacio de Hilbert:
$$\mathcal{H} = L^2\!\left(\mathbb{H}, \frac{d\mu_{\mathrm{off}}(x,y)}{y}\right)$$

(si $\mu_{\mathrm{off}} \neq 0$, esto es un espacio no trivial). Definimos el operador $\mathcal{D}: \mathcal{H} \to \ell^2(\mathbb{N})$ por:
$$\mathcal{D}[f](n) = \int_\mathbb{H} f(x,y) P_y(\gamma_n - x)\,\frac{d\mu_{\mathrm{off}}(x,y)}{y}$$

Este es el operador que evalúa la transformada de Poisson de $f \cdot \mu_{\mathrm{off}}$ en los puntos $\gamma_n$.

**Proposición II.2.** $\mathcal{D}[1] = \{C_\infty(\gamma_n)\}_{n\geq 1}$, es decir, la imagen del vector constante $f=1$ bajo $\mathcal{D}$ es exactamente la sucesión del déficit.

**Conjetura II.3 (Injectividad de $\mathcal{D}$).** Si el operador $\mathcal{D}$ es inyectivo, entonces la condición $\mathcal{D}[1] = 0$ (RH) implica $\mu_{\mathrm{off}} = 0$.

*Esto no es circular:* la injectividad de $\mathcal{D}$ es una propiedad del operador, no de $\mu_{\mathrm{off}}$. Si $\mathcal{D}$ resulta ser inyectivo por razones independientes (e.g., porque el conjunto $\{\gamma_n\}$ es "suficientemente denso" relativo a la medida $\mu_{\mathrm{off}}$), entonces $C_\infty(\gamma_n)=0$ $\forall n$ implicaría $\mu_{\mathrm{off}} = 0$.

### II.3 La pregunta de la injectividad

¿Cuándo es inyectivo $\mathcal{D}$? El núcleo de $\mathcal{D}$ consiste en funciones $f\in\mathcal{H}$ tales que $\int f(x,y)P_y(\gamma_n-x)\,d\mu_{\mathrm{off}}/y = 0$ para todo $n$. Esto es una condición de ortogonalidad: $f$ es ortogonal a todas las funciones $P_y(\gamma_n - \cdot)$ en $\mathcal{H}$.

**Propuesta II.4 (Completitud del sistema de núcleos).** Si el sistema $\{P_y(\gamma_n - \cdot)\}_{n\geq 1}$ es *completo* en $\mathcal{H}$ (genera un subespacio denso), entonces $\ker(\mathcal{D}) = \{0\}$ y $\mathcal{D}$ es inyectivo.

La completitud del sistema de núcleos de Poisson en $\mathcal{H}$ depende de la densidad del conjunto $\{\gamma_n\}$ relativa a la medida $\mu_{\mathrm{off}}$. Por el teorema de Müntz-Szász generalizado a núcleos de Poisson, esto está relacionado con la convergencia de la serie $\sum_n 1/\gamma_n^2$ — que converge, luego la completitud NO está garantizada por el criterio de Müntz-Szász estándar.

**Aquí hay una apertura genuina**: el problema de completitud del sistema $\{P_y(\gamma_n-\cdot)\}$ en el espacio $L^2(\mu_{\mathrm{off}}/y)$ no ha sido estudiado en la literatura. Si se prueba la completitud (por métodos nuevos), se obtiene injectividad de $\mathcal{D}$ y por lo tanto RH.

---

## III. Geometría Aritmética de la Medida de Déficit: Un Objeto Motivico Nuevo

### III.1 El paradigma del campo de funciones

La única prueba completa de RH que existe es la de Weil (1948) para zetas de curvas sobre campos finitos $\mathbb{F}_q$. El método usa:

1. **Un espacio geométrico:** la curva $C$ sobre $\bar{\mathbb{F}}_q$.
2. **El Frobenius:** un endomorfismo $\phi: C \to C$ cuyas eigenvalores son exactamente las raíces de la función zeta.
3. **La positividad de la traza:** el teorema de Riemann-Roch da $|\text{Tr}(\phi^n)| \leq 2g\cdot q^{n/2}$, que implica que las eigenvalores tienen módulo $q^{1/2}$.

Para el zeta de Riemann, el paso 3 (positividad/traza) es lo que falta. Los pasos 1 y 2 existen en distintas formulaciones incompletas (Deninger, Connes).

### III.2 La nueva propuesta: el espacio de medidas como la "curva" faltante

**Idea central:** en vez de buscar un espacio geométrico del cual $\zeta$ es la función L, construimos un espacio del cual $\mu_{\mathrm{off}}$ es la *medida espectral*.

**Definición III.1 (Variedad de Déficit).** Sea $\mathcal{V}_\zeta$ el espacio formal de medidas $\zeta$-compatibles (Definición I.1). Dotamos $\mathcal{V}_\zeta$ de la topología débil* sobre medidas de Radon en $\mathbb{H}$.

En este espacio:
- RH corresponde a $\mathcal{V}_\zeta = \{0\}$ (el espacio es el punto).
- No-RH corresponde a $\mathcal{V}_\zeta \ni \mu_{\mathrm{off}} \neq 0$.

**El objetivo:** probar que $\mathcal{V}_\zeta$ es un *espacio algebraico* (en alguna categoría apropiada) cuyo único punto es $\{0\}$.

### III.3 El Frobenius aritmético sobre $\mathcal{V}_\zeta$

La ecuación funcional de $\zeta$ actúa sobre $\mu_{\mathrm{off}}$ como una simetría del cuarteto (Doc 44, §8). Esta simetría es el "Frobenius aritmético" $\phi_\zeta: \mathcal{V}_\zeta \to \mathcal{V}_\zeta$ dado por:
$$\phi_\zeta(\mu)(A) = \mu(\sigma_{\mathrm{funct}}(A))$$

donde $\sigma_{\mathrm{funct}}$ es la transformación del cuarteto $(x,y)\mapsto(-x,y)$ compuesta con la reflexión de la ecuación funcional.

**Proposición III.2.** $\phi_\zeta$ es un automorfismo de $\mathcal{V}_\zeta$ de orden 4 (un cuarteto exactamente).

**El programa:** construir la teoría de cohomología de $\mathcal{V}_\zeta$ con la acción de $\phi_\zeta$, tal que:

1. La traza de $\phi_\zeta$ sobre $H^1(\mathcal{V}_\zeta)$ sea igual a $\sum_{\rho_0}(\sigma_0-1/2)$ (la masa de $\mu_{\mathrm{off}}$).
2. La positividad de la forma de intersección en $H^1 \otimes H^1$ implique que la traza sea cero.
3. Traza cero $\Rightarrow$ $\sum_{\rho_0}(\sigma_0-1/2) = 0$ $\Rightarrow$ $\mu_{\mathrm{off}} = 0$ $\Rightarrow$ RH.

Este programa es el *análogo de Weil* para el zeta de Riemann, con el rol de la "curva" jugado por $\mathcal{V}_\zeta$.

### III.4 La categoría correcta

Para que este programa tenga sentido, $\mathcal{V}_\zeta$ debe vivir en una categoría donde:

- Los objetos son "espacios medibles con simetría aritmética".
- Los morfismos son "mapas compatibles con la acción de $\phi_\zeta$".
- Existe una noción de cohomología con los teoremas de comparación correctos.

La candidata más natural es la categoría de **motivos mixtos** de Voevodsky, donde las medidas de Hausdorff sobre espacios aritméticos son objetos naturales. Alternativamente, la **categoría de C*-álgebras** con la acción del grupo de Galois aritmético $\widehat{\mathbb{Z}}^\times$.

**Lo genuinamente nuevo:** ningún paper en la literatura ha construido el "espacio de medidas $\zeta$-compatibles" como un objeto motivico o en C*-álgebras. Esto es matemática nueva que no existe todavía.

---

## IV. El Problema de Completitud de Poisson: La Apertura Más Concreta

De las tres direcciones, esta es la que tiene la ruta más concreta al trabajo inmediato.

### IV.1 El problema

**Pregunta IV.1.** Sea $\mu$ una medida positiva de Radon en $\mathbb{H}$ con soporte en $\{y \leq 1/2\}$. ¿Es el sistema de núcleos de Poisson $\{P_y(\gamma_n - x)\}_{n\geq 1}$ *completo* en $L^2(\mathbb{H}, \mu)$?

Aquí, "completo" significa que el subespacio lineal generado por $\{P_y(\gamma_n - x)\}_{n\geq 1}$ es denso en $L^2(\mathbb{H}, \mu)$.

### IV.2 Por qué es nueva

El problema de completitud de *sistemas de translaciones del kernel de Poisson* es un problema de análisis harmónico en semiplano que, hasta donde sabemos, no tiene solución en la literatura para conjuntos de evaluación $\{\gamma_n\}$ con la distribución asintótica de los ceros de $\zeta$.

Los problemas de completitud más cercanos en la literatura son:
- **Completitud de exponenciales** (Paley-Wiener, Beurling): $\{e^{i\gamma_n t}\}$ en $L^2[-\pi,\pi]$ — bien estudiado.
- **Completitud del sistema de Poisson** para ceros equiespaciados: conocido.
- **Completitud para ceros de $\zeta$**: no resuelto.

### IV.3 El resultado que se necesita

**Teorema conjetural IV.2.** Si $\{\gamma_n\}$ son los ordenes imaginarias de los ceros de $\zeta$ en la línea crítica (con densidad asintótica $\sim T\log T/(2\pi T)$), entonces para cualquier medida positiva $\mu$ en $\mathbb{H}$ con $\text{sop}(\mu) \subset \{0 < y \leq 1/2\}$ y $\int_\mathbb{H} (1+|x|)^{-2}\,d\mu < \infty$:

$$\overline{\text{span}}\{P_y(\gamma_n - x) : n \geq 1\} = L^2(\mathbb{H}, \mu)$$

**Si este teorema es cierto**, entonces el operador $\mathcal{D}$ de §II es inyectivo, y la condición $C_\infty(\gamma_n) = 0$ para todo $n$ implica $\mu = 0$, que en el caso $\mu = \mu_{\mathrm{off}}$ da RH.

### IV.4 Estrategia de prueba

El Teorema IV.2 se atacaría por:

1. **Versión de Müntz-Szász para kernels de Poisson:** generalizar el criterio clásico (completitud de $\{x^{\lambda_n}\}$ en $L^2[0,1]$ iff $\sum 1/\lambda_n = \infty$) al caso de kernels de Poisson. La condición análoga sería $\sum_n 1/\gamma_n$ — que diverge (pues $\gamma_n \sim 2\pi n/\log n$ y $\sum 1/n$ diverge).

2. **Teorema de Beurling para densidad de Poisson:** Beurling demostró que sistemas de exponenciales son completos cuando la densidad del conjunto $\{\gamma_n\}$ supera la densidad de Nyquist. Un teorema análogo para kernels de Poisson requeriría definir la "densidad de Nyquist para Poisson" — nueva.

3. **Conexión con la teoría de Hardy:** $P_y(\gamma_n - x)$ son los valores de frontera de funciones de Cauchy en $\mathbb{H}^+$. La completitud en $L^2(\mu)$ equivale a la densidad del espacio $H^2(\mathbb{H}^+)$ en $L^2(\partial\mathbb{H}^+, d\mu)$ — un problema de teoría de operadores en espacio de Hardy.

---

## V. Jerarquía de dificultad y hoja de ruta

Las tres estructuras propuestas tienen distintos niveles de concreción y dificultad:

| Dirección | Concreción | Dificultad estimada | Herramientas necesarias |
|-----------|-----------|---------------------|------------------------|
| I. Medidas $\zeta$-compatibles | Alta | Media-Alta | Análisis funcional, estimaciones de densidad |
| II. Completitud de Poisson | Muy alta | Alta | Teoría de Hardy, Müntz-Szász para Poisson |
| III. Geometría motivica de $\mathcal{V}_\zeta$ | Media | Muy Alta | Motivos, C*-álgebras, cohomología aritmética |

**Recomendación de prioridad:**

1. **Inmediato (Docs 47–50):** Desarrollar la Dirección II. El problema de completitud de Poisson es concreto, tiene bibliografía adyacente (Paley-Wiener, Beurling, Müntz-Szász), y si se resuelve produce RH. Es el frente más atacable.

2. **Paralelo (Docs 47–52):** Formalizar la Dirección I. Definir el espacio $\mathcal{M}_\zeta$ con precisión y comenzar a estudiar sus propiedades. Es trabajo de análisis puro.

3. **A largo plazo:** La Dirección III requiere colaboración con geometría aritmética — es el programa más ambicioso y el más parecido al "nuevo lenguaje" que Wiles construyó para Fermat.

---

## VI. El quiebre conceptual: de "traducir RH" a "construir donde RH es consecuencia"

El cambio de paradigma que propone este documento es el siguiente:

**Paradigma viejo (Docs 39–45):**
> Tomar RH y encontrar formulaciones equivalentes. La dificultad es siempre la misma porque la equivalencia la preserva.

**Paradigma nuevo (Doc 46 en adelante):**
> Construir estructuras matemáticas donde RH no es un axioma ni una equivalencia, sino una consecuencia de propiedades más básicas:
> - Completitud de un sistema de funciones (Dirección II)
> - Rigidez de un sistema de restricciones (Dirección I)
> - Positividad de una forma cohomológica (Dirección III)

El camino de Wiles siguió exactamente este patrón: no intentó probar el Último Teorema de Fermat directamente, sino que construyó un mundo (formas modulares, representaciones de Galois, deformaciones de Hecke) donde la afirmación de Fermat era una consecuencia automática de propiedades de ese mundo.

La pregunta para este programa es: ¿cuál es el "mundo de Wiles" para RH? La respuesta propuesta aquí:

> **El espacio de medidas $\zeta$-compatibles $\mathcal{V}_\zeta$, dotado del operador de completitud de Poisson $\mathcal{D}$ y la acción del Frobenius aritmético $\phi_\zeta$, es el mundo donde RH es una consecuencia del teorema de rigidez $\mathcal{V}_\zeta = \{0\}$.**

---

## VII. Qué construir inmediatamente

**Tarea concreta para Doc 47:** Probar la versión más simple del Teorema de Completitud de Poisson:

> Sea $\mu = \delta_{(x_0, y_0)}$ (medida de Dirac en un punto). ¿Es $\{P_{y_0}(\gamma_n - x_0)\}_{n\geq 1}$ completo en $L^2(\mathbb{H}, \delta)$? (Esto es equivalente a preguntarse si la sucesión $\{P_{y_0}(\gamma_n - x_0)\}$ no tiene ninguna función ortogonal no trivial — trivialmente cierto, pues $\delta$ es una medida de masa 1 concentrada en un punto y el subespacio generado es todo $\mathbb{R}$.)

Para medidas con soporte infinito, el problema es genuinamente difícil. El Doc 47 debe identificar la versión correcta del problema de completitud y demostrar el primer caso no trivial.

**Tarea concreta para Doc 48:** Formalizar $\mathcal{M}_\zeta$ y demostrar que las condiciones 1–4 (sin la condición 5 de auto-consistencia) admiten medidas no nulas — confirmando que la condición 5 es la que carga el peso de la restricción.

---

*Siguiente documento (Doc 47): El Teorema de Completitud de Poisson — primera versión y casos especiales.*

---

## Apéndice: ¿Por qué la Dirección III es la más profunda?

La Dirección III (geometría motivica) es la más profunda porque conecta con el programa de Langlands. Las funciones L de Langlands se conjectira que satisfacen RH generalizado. Si $\mu_{\mathrm{off}}$ puede interpretarse como un "motivo mixto" $M_\zeta$ tal que la función L de $M_\zeta$ sea relacionada con $\zeta$, y si los motivos mixtos tienen positividad cohomológica (Beilinson-Deligne), entonces RH sería consecuencia de la conjetura estándar de Grothendieck sobre la positividad de la forma de intersección en cohomología motivica.

Este no es el camino inmediato — pero es el camino correcto a largo plazo. La razón: la única prueba de RH en algún contexto (campos finitos, curvas) siempre usó cohomología con positividad. Sin positividad, ningún método puramente analítico ha funcionado — y no es accidental. La positividad es el axioma profundo que falta.

La tesis de Doc 46, en su versión más radical, es esta:

> **RH no se probará con análisis. Se probará con geometría — cuando se encuentre el espacio correcto sobre el cual la positividad de la forma de intersección implica RH.**

Ese espacio podría ser $\mathcal{V}_\zeta$. O podría ser algo que hoy no imaginamos. Pero el programa CCM, al haber identificado $\mu_{\mathrm{off}}$ como el objeto central, ha dado el primer paso hacia esa geometría.
