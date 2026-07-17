# Doc 123 — Construcción de la cohomología del cuadrado vía tolerancia

**Programa:** Hipótesis de Riemann — Phase 40: intentar CERRAR G1.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 119 (axiomas R-SIG, R-FIN, R-LEF, R-PESO, R-NC; orden de dependencias; tensión T1); Doc 120 (inventario en fuente del corpus CC/CCM; §6.3 obstáculo del cuadrado; §3.2 RR absoluto con tolerancia); Doc 121 (Cruce B, calificado TÉCNICO con riesgo-RH nulo; los 5 pasos; el caso de prueba C_p × C_p; el experimento 121.E del Cruce A).

**Disciplina de etiquetado (regla absoluta):** **[DATO]** = leído en fuente esta sesión (arXiv, junio 2026), con cita; o teorema interno del programa con cita backward-only. **[CONSTRUCCIÓN]** = lo que diseño yo, con su estatus explícito (qué asume, qué define, qué queda por verificar). **[GAP]** = lo que falta, con precisión. **[CONJETURA]** = lo que creo sin derivar. **[NO VERIFICADO]** = de memoria o no hallado en fuente. **NUNCA "probado".** El objetivo NO es declarar G1 cerrado: es construir todo lo construible y aislar con precisión el núcleo que falta. Si la construcción se traba, el punto de traba ES el resultado.

---

## 0. Resumen ejecutivo

Este documento intenta construir la H¹ del cuadrado X × X del sitio de escala manejando los "null elements" de Connes–Consani (CC) con la técnica de tolerancia, y termina en la salida **(iii) PARCIAL**, con el núcleo aislado.

El hallazgo de fuente que organiza todo (§1.3): CC mismos nombran la **raíz** del obstáculo de los null elements — *"The root of this problem had been already unearthed in the Example 6.5 of [yoshi]"* (1805.10501, Introducción) **[DATO]**. Ese ejemplo (estilo Yoshida / literatura tropical) exhibe **pares (C, D), (C′, D′) de curvas tropicales y divisores cuyos invariantes de rango r(D), r(D′) DIFIEREN aunque los módulos H⁰ son isomorfos** **[DATO]**. Es decir: la raíz del obstáculo NO es analítica ni de tamaño — es que **el isomorfismo de módulos idempotentes no ve el rango tropical**. El "null element" (el elemento absorbente −∞ del max-plus) es el vehículo: permite cociclos de Čech cuya "anulación" no es una condición lineal, y esos cociclos parásitos cambian el rango sin cambiar la clase de isomorfismo del módulo.

Diagnóstico central (§3): la tolerancia (2205.01391) es exactamente un **reparador de conúcleo** para un complejo corto *presentado* ψ — neutraliza la obstrucción "no hay buen cociente en el mundo idempotente". Eso **se solapa** con una mitad del obstáculo del cuadrado (la mitad "cokernel mal definido"), pero **no toca** la otra mitad (la no-invarianza del rango bajo isomorfismo de módulos = ausencia de una dimensión funtorial). La tolerancia mata los null elements *cuando el H¹ se presenta como conúcleo de un único morfismo con norma controlada*; no los mata cuando aparecen como cociclos de Čech de un recubrimiento con intersecciones múltiples, que es el régimen genuino de dimensión 2.

El caso de prueba C_p × C_p (§4): el cálculo es honesto pero **se traba en el paso de presentar el complejo de Čech del cuadrado como un único ψ**. En dimensión 1 (C_p) no hay H¹ en absoluto (su rol lo juega H⁰(−D), §2.4) **[DATO]**; en el cuadrado, un Künneth ingenuo produce un término H¹(C_p) ⊗ H⁰(C_q) que **no existe como objeto** porque H¹(C_p) no está definido. Conclusión: el cuadrado no hereda su H¹ de los factores; hay que construirlo *de novo* sobre el recubrimiento del producto, y ahí reaparecen los cociclos absorbentes.

Finitud (§5): la única finitud abordable en G1 es la **finitud de los grupos de Čech graduados por grado/soporte** del recubrimiento — una finitud combinatoria del nervio, NO la finitud de la parte impura (R-FIN), que necesita la graduación de pesos (G2) que no tenemos. Las distingo con precisión.

Núcleo que falta (§6): **dos** piezas, una TÉCNICA y una CONCEPTUAL. (a) [TÉCNICA] presentar el complejo de Čech del cuadrado como complejo de Γ-𝕊-módulos con tolerancia (cambio de base de semianillos idempotentes a Γ-anillos en dimensión 2). (b) [CONCEPTUAL] el núcleo real: una **noción funtorial de dimensión/rango invariante bajo isomorfismo** sobre el cuadrado — exactamente lo que Example 6.5 de [yoshi] muestra que NO existe ingenuamente, y lo que la tolerancia provee en dim 1 (dim_𝕊 = mínimo de generadores con norma) pero no obviamente en dim 2.

---

## 1. PASO 1 — El cuadrado y el obstáculo, en fuente

### 1.1. Qué es exactamente "el cuadrado" para CC

**[DATO]** (1805.10501, Introducción, textual): *"in the process to formulate a Riemann-Roch theorem on the square of the Scaling Site one faces a substantial difficulty."* La frase es la única caracterización: el "cuadrado del sitio de escala" aparece como el objeto sobre el que se quiere un RR de tipo Weil (la adaptación en característica cero de la prueba de Weil vía Mattuck–Tate y Grothendieck, §6.3 de Doc 120). **CC NO construyen el cuadrado como objeto terminado en este paper.** Lo nombran como meta y declaran la dificultad. **[DATO]**

Lo que SÍ existe en el corpus como precedente del cuadrado **[DATO]** (Doc 120 §1.3, §6.1; 1502.05580 §6):
- El cuadrado del **sitio aritmético** existe como **topos semi-anillado**: el cuadrado no reducido lleva haz de estructura $\mathbb Z_{\min} \otimes_{\mathbb B} \mathbb Z_{\min}$; el reducido tiene por secciones **polígonos de Newton** (operaciones de envolvente convexa).
- Sus puntos sobre $\mathbb R_+^{\max}$ son el **producto** de los puntos del sitio (Prop. 6.11).
- Las correspondencias de Frobenius $\Psi(\lambda)$ viven en él como subvariedades, con composición exacta solo para $\lambda\lambda' \notin \mathbb Q$.

**[CONSTRUCCIÓN] (estatus: lectura de fuente, no afirmación de CC).** El "cuadrado del sitio de escala" que el RR de Weil necesita es el análogo de escala (extensión de escalares a $\mathbb R_+^{\max}$) del cuadrado del sitio aritmético: el **producto fibrado del topos del sitio de escala consigo mismo sobre la base** (sobre $\mathbb B$, o sobre $\mathbb R_+^{\max}$ tras extensión), con haz de estructura el producto tensorial idempotente $\mathcal O \otimes_{\mathbb B} \mathcal O$ de los haces de funciones convexas afines a trozos. Sus secciones locales son los polígonos de Newton bidimensionales (envolventes convexas en $\mathbb R^2$ de funciones convexas afines a trozos en cada variable). **Lo que queda por verificar:** que ese producto tensorial conmute con la tropicalización y con la operación de envolvente (es el Paso 1 del programa de verificación del Cruce B, Doc 121 §2.2.2; riesgo declarado allí: "el producto tensorial sobre 𝔹 y el producto sobre 𝕊 pueden no conmutar con la tropicalización"). **[GAP TÉCNICO]**, ver §6.

### 1.2. El recubrimiento de Čech y el complejo

**[DATO]** (1805.10501, §2, textual): *"In [CC5] we have developed the beginning of a general homological algebra machine in characteristic one (i.e. for tropical structures) exactly to aim for a definition of the above H¹. In particular, we proved the existence of non trivial Ext-functors and we were also able to input the resolution of the diagonal to obtain the tropical analogue of the Čech complex."* Aquí [CC5] = **arXiv:1703.02325, *Homological algebra in characteristic one*** (Higher Structures 3 (2019) 155–247) **[DATO]**.

**[DATO]** (1703.02325, abstract + búsqueda en fuente): la categoría base es $\mathbb B\text{mod}$, módulos sobre el semicuerpo booleano $\mathbb B = \{0,1\}$, *"the replacement for the category of abelian groups"*. $\mathbb B\text{mod}$ *"fulfills analogues of the axioms AB1 and AB2 for abelian categories"* pero **es semi-aditiva, no aditiva**: no hay sustracción (idempotencia $a \oplus a = a$). Construyen Ext vía *"a precise comonad on Bmod"* y las categorías de Kleisli y Eilenberg–Moore asociadas. **[DATO]**

**[CONSTRUCCIÓN] (estatus: síntesis de los dos datos anteriores).** El complejo de Čech tropical de CC para un recubrimiento $\mathcal U = \{U_i\}$ del cuadrado es el complejo cosimplicial idempotente
$$ \check C^0 = \prod_i \mathcal O(U_i) \;\to\; \check C^1 = \prod_{i<j} \mathcal O(U_{ij}) \;\to\; \check C^2 = \prod_{i<j<k}\mathcal O(U_{ijk}) \;\to\cdots $$
con diferencial $\delta$ = alternancia de restricciones, **calculada con $\oplus = \max$ en lugar de la suma alternada de signos** (no hay signos en característica 1). $H^0 = \ker\delta^0$ (secciones globales), $H^1 = \ker\delta^1 / \operatorname{im}\delta^0$ **— y aquí está el problema**: "$/\operatorname{im}\delta^0$" es un cociente que en $\mathbb B\text{mod}$ no está bien definido (no hay sustracción; el conúcleo categórico no coincide con el cociente conjuntista). **[DATO que el cociente es problemático: 1703.02325, semi-aditividad sin sustracción]** + **[CONSTRUCCIÓN: la identificación de que ESE es el punto donde entran los null elements]**.

### 1.3. El obstáculo EXACTO — los null elements y su raíz

**[DATO]** (1805.10501, Introducción, cita textual completa con el contexto que faltaba en Doc 120):

> *"The problem, which is still open at this time, has to do with an appropriate definition of the sheaf cohomology (as idempotent monoid) $H^1$... when applied to Čech covers, the presence of the null elements creates unwanted contributions to the cohomology which so far we are unable to handle. **The root of this problem had been already unearthed in the Example 6.5 of [yoshi].**"*

**[DATO]** (1805.10501, descripción de ese Example 6.5, textual según fuente extraída): *"This example provides pairs (C,D), (C′,D′) of tropical curves and divisors on them, for which the tropical invariants r(D) and r(D′) ... are different, while the modules themselves are isomorphic."*

Esto es decisivo y reorienta todo el ataque. **Qué son los null elements y por qué obstruyen, con precisión:**

1. **Qué son [DATO].** El "null element" es el elemento absorbente del semianillo idempotente: $-\infty$ en el max-plus $\mathbb R_{\max} = (\mathbb R \cup\{-\infty\}, \max, +)$ (el "0" del semianillo: $-\infty \oplus x = x$, $-\infty \otimes x = -\infty$). En un módulo idempotente es el elemento neutro de $\oplus$.

2. **En qué grado aparecen [DATO].** En **grado 1**: *"unwanted contributions to the cohomology"* en $H^1$ (el contexto es la definición de $H^1$). **[DATO]** (la frase está en el párrafo sobre $H^1$).

3. **Por qué no pueden manejarlos — la raíz [DATO + CONSTRUCCIÓN].** El Example 6.5 dice que **dos divisores con módulos H⁰ isomorfos pueden tener rangos tropicales distintos**. Traducción a la maquinaria de Čech: la clase de isomorfismo del módulo de cociclos **no determina el invariante cohomológico**. El mecanismo concreto **[CONSTRUCCIÓN, estatus: mi lectura del porqué, a verificar por experto]**: en $\mathbb B\text{mod}$ un cociclo $\zeta \in \ker\delta^1$ se declara "trivial" si $\zeta = \delta^0(\eta)$ para algún $\eta$; pero como no hay sustracción, "$\zeta - \delta^0\eta = 0$" no es una condición lineal — se reemplaza por "$\zeta = \delta^0\eta \oplus (\text{null})$", y los términos absorbentes $-\infty$ insertados en algunas componentes permiten que un cociclo NO trivial parezca trivial (o viceversa). Los "null elements" son justamente esas componentes $-\infty$ que un cociclo puede tener en algunas intersecciones $U_{ij}$ pero no en otras: crean clases parásitas porque el conúcleo idempotente no las cocientea bien. La consecuencia es exactamente la patología de Example 6.5: el grupo $H^1$ (vía conúcleo) no es un invariante del objeto, sino que depende de presentaciones, y el rango se le escapa.

**Conclusión del Paso 1 [CONSTRUCCIÓN].** El obstáculo del cuadrado tiene **dos capas**:
- **(C-cok)** El conúcleo $\ker\delta^1 / \operatorname{im}\delta^0$ no está bien definido en $\mathbb B\text{mod}$ (no hay sustracción).
- **(C-rank)** Aun definiendo *algún* objeto $H^1$, su invariante numérico (rango/dimensión) **no es funtorial**: módulos isomorfos pueden dar rangos distintos (Example 6.5). Esta es la capa profunda, la "raíz" que CC señalan.

Esta bifurcación es la clave para el diagnóstico del Paso 3: la tolerancia ataca (C-cok); el corazón es (C-rank).

---

## 2. PASO 2 — La técnica de tolerancia, en fuente, y su mecanismo abstracto

### 2.1. Qué es la tolerancia, exactamente

**[DATO]** (2205.01391, Prop. 2.2(ii) y Apéndice A, textual según fuente): para el divisor $D$, con el morfismo de presentación
$$ \psi:\; H\mathbb Q \times H\mathcal O(D) \;\longrightarrow\; H\mathbb A_{\mathbb Q} $$
(análogo exacto de la presentación adélica de Weil para cuerpos de funciones), se define
$$ H^1(D) := (H\mathbb A_{\mathbb Q},\, \mathcal R), \qquad \mathcal R_k := \{(x,y)\in H\mathbb A_{\mathbb Q}(k_+)^2 \;:\; x - y \in \operatorname{Image}\psi(k_+)\}. $$
**[DATO]** Esto **no es un cociente**: es *"a reflexive relation encoded within the 𝕊-module structure itself"* — se **conserva el módulo entero** $H\mathbb A_{\mathbb Q}$ y se le **añade** la relación de tolerancia $\mathcal R$. El objeto vive en la categoría $\Gamma\mathcal T_+$ de **𝕊-módulos con tolerancia**. La construcción pasa por Dold–Kan (Apéndice B): a $\psi$ visto como complejo corto se le asocia un Γ-espacio $H(D)$, y $H^1(D) = \pi_1^{\mathcal T}(H(D))$ como 𝕊-módulo con tolerancia. **[DATO]**

**[DATO]** (2205.01391, Def. A.2): la **dimensión** $\dim_{\mathbb S[\pm1]}$ es el **mínimo cardinal de un conjunto generador** $F$ tal que todo $x$ se escribe $x = \sum_{f\in F}\alpha(f)f$ con $\alpha(f)\in\{-1,0,1\}$ y control de norma $\sum|\alpha(f)f| \le e^a$ (parte arquimediana de $D$). Para $H^0$: $\dim_{\mathbb S[\pm1]}H^0(D) = \lceil \log(2n+1)/\log 3\rceil$ (Prop. 3.3). **[DATO]**

### 2.2. Por qué resuelve en dim 1 — el mecanismo abstracto

**[DATO]** (2205.01391, §2, lectura de fuente): *"in arithmetic, elements arbitrarily close to zero create pathologies in classical quotients. Tolerance relations preserve the full module while adding an equivalence structure that does not quotient out the abelian group structure."*

**[CONSTRUCCIÓN] El mecanismo de la tolerancia, formulado en abstracto (estatus: síntesis de fuente, a verificar):**

> La tolerancia neutraliza una clase precisa de obstrucción: aquella en que **el invariante cohomológico requeriría un cociente $M/N$ que está mal definido** (porque la categoría no tiene sustracción, o porque $N$ tiene "cola cerca de cero" que un cociente clásico colapsa patológicamente). El reemplazo "$x\sim y \iff x-y\in N$" **conservado como relación, no ejecutado como cociente**, recupera (i) un objeto bien definido en una categoría enriquecida ($\Gamma\mathcal T_+$), y (ii) **una dimensión funtorial** vía "mínimo de generadores módulo la relación con norma controlada".

El punto (ii) es el que importa para el Paso 3: la tolerancia no solo repara el conúcleo (i) — **también restaura un invariante numérico funtorial** (la $\dim_{\mathbb S}$). En el lenguaje del Paso 1, la tolerancia ataca **(C-cok)** directamente y **(C-rank) en el caso particular de un H¹ presentado como conúcleo de un único $\psi$**: ahí el rango es "mínimo de generadores con norma", que SÍ es invariante de iso en $\Gamma\mathcal T_+$.

**[DATO crítico de delimitación]** (2205.01391, estructura): la tolerancia se aplica a un **complejo corto de longitud 1** — un único morfismo $\psi$ cuyo conúcleo es $H^1$. Es la situación de dimensión 1 (una curva: $H^0$, $H^1$, y nada más). **No hay, en 2205.01391, ningún complejo de Čech de un recubrimiento con intersecciones triples ni nada que se parezca al complejo de §1.2.** El $H^1$ de CC en dim 1 NO se computa por Čech: se computa por la **presentación adélica** $\psi$ (núcleo = $H^0$, conúcleo = $H^1$). **[DATO — y es el quicio del Paso 3.]**

---

## 3. PASO 3 — EL DIAGNÓSTICO CENTRAL: ¿mismo tipo de obstáculo?

La pregunta que decide el Cruce (B): **¿los null elements del cuadrado (Paso 1) son del mismo tipo que los elementos problemáticos que la tolerancia neutraliza en dim 1 (Paso 2)?**

Respuesta: **(iii) PARCIAL.** Desarrollo el porqué con la bifurcación (C-cok)/(C-rank) de §1.3.

### 3.1. La parte que SÍ coincide: (C-cok)

**[CONSTRUCCIÓN, estatus: argumento estructural, no teorema].** Ambos obstáculos comparten la raíz "no hay buen cociente en el mundo idempotente":
- En dim 1, el conúcleo de $\psi$ no es un cociente legítimo en $\mathbb B\text{mod}$ → tolerancia.
- En el cuadrado, $\ker\delta^1/\operatorname{im}\delta^0$ no es un cociente legítimo en $\mathbb B\text{mod}$ → *en principio*, tolerancia.

La traducción formal es directa: el complejo de Čech del recubrimiento del cuadrado puede verse como un complejo (más largo) de 𝕊-módulos, y la maquinaria Dold–Kan que CC usan para $\psi$ **se aplica a complejos de cualquier longitud**, no solo a complejos cortos. Esto da:

**[CONSTRUCCIÓN] (la H¹ tolerante del cuadrado — construcción condicional, estatus: define, asume, deja por verificar).**
Sea $\mathcal U$ un recubrimiento finito del cuadrado $X\times X$ por abiertos del topos producto. Tras el cambio de base de $\mathbb B\text{mod}$ (semianillos idempotentes) a $\Gamma$-anillos sobre $\mathbb S$ (el cambio de base que en dim 1 lleva el RR tropical al RR absoluto), el complejo de Čech $\check C^\bullet(\mathcal U)$ se reescribe como complejo de $\Gamma$-𝕊-módulos. Aplicando Dold–Kan a $\check C^\bullet$ y tomando la homotopía generalizada con tolerancia:
$$ H^1_{\mathrm{tol}}(X\times X,\mathcal O) := \pi_1^{\mathcal T}\big(\mathrm{DK}(\check C^\bullet(\mathcal U))\big), $$
un 𝕊-módulo con tolerancia, **en el cual los cociclos soportados en elementos absorbentes $-\infty$ caen en clases de tolerancia triviales** (porque $\zeta$ con componentes $-\infty$ cumple $\zeta - \delta^0\eta \in$ banda de tolerancia controlada por norma, exactamente como en dim 1).
- **Asume:** (A1) el cambio de base $\mathbb B\to\mathbb S$ es functorial en dim 2 y conmuta con la envolvente convexa (Paso 1 del programa Doc 121; **[GAP TÉCNICO]**). (A2) Dold–Kan da el objeto correcto para un complejo de longitud $\ge 2$ con la relación de tolerancia "componente $-\infty$" (no demostrado por CC más allá de longitud 1). (A3) la independencia del recubrimiento $\mathcal U$ (que $H^1_{\mathrm{tol}}$ sea un invariante del cuadrado y no del nervio elegido).
- **Define:** un candidato a objeto $H^1_{\mathrm{tol}}$.
- **Queda por verificar:** TODO lo anterior (A1–A3) y, sobre todo, lo de §3.2.

**Esta es la mejor construcción honesta de "la tolerancia se aplica" — y nótese que es enteramente condicional.** Repara (C-cok). Pero no toca (C-rank), que es la raíz que CC señalan.

### 3.2. La parte que NO coincide: (C-rank) — el núcleo

**[CONSTRUCCIÓN, estatus: el argumento decisivo de este documento].**

La tolerancia restaura una dimensión funtorial $\dim_{\mathbb S}$ **en dim 1 porque allí $H^1$ es el conúcleo de UN morfismo $\psi$ con una norma canónica $e^a$ (la parte arquimediana del divisor)**, y "mínimo de generadores con $\sum|\alpha f|\le e^a$" es un invariante porque **la norma viene del divisor, dato externo bien definido**.

En el cuadrado, el Example 6.5 de [yoshi] dice precisamente que **el rango tropical no es invariante de la clase de isomorfismo del módulo** **[DATO]**. Para que la tolerancia lo arregle, necesitaríamos una **norma canónica sobre los cociclos de Čech del cuadrado** que juegue el papel que $e^a$ juega en dim 1. Y aquí está la traba exacta:

> **[GAP CONCEPTUAL — el núcleo].** En dim 1 la norma $e^a$ que define $\dim_{\mathbb S}$ proviene de la parte arquimediana del **divisor de Arakelov** sobre $\overline{\mathrm{Spec}\,\mathbb Z}$ — un dato de grado real de un objeto de **codimensión 1**. En el cuadrado, el análogo de "divisor" es una clase de **codimensión 1 en una superficie** (un análogo de $\mathrm{NS}(C\times C)$, el grupo de Néron–Severi), y **no hay en el corpus CC ninguna norma canónica sobre tales clases** — eso sería precisamente una **forma de intersección** (la métrica de Arakelov de dimensión 2), que es G2 y no existe (Doc 119 §2.3; Doc 120 §8). Sin esa norma, "mínimo de generadores con norma controlada" no tiene "norma", y la tolerancia no produce dimensión funtorial: reaparece Example 6.5.

**Por tanto:** la tolerancia maneja la mitad (C-cok) del obstáculo (la sintáctica, "no hay buen cociente") y **deja intacta la mitad (C-rank)** (la semántica, "no hay invariante numérico funtorial"). Y (C-rank) en dim 2 **no es del mismo tipo** que el problema que la tolerancia resuelve en dim 1, porque en dim 1 la norma que rescata la funtorialidad es un dato de codimensión 1 (el divisor de Arakelov), mientras que en dim 2 el dato análogo es una forma de intersección de codimensión 1 en una superficie — que es justamente G2.

### 3.3. La diferencia exacta, enunciada

**[CONSTRUCCIÓN].** Caracterizo la diferencia pedida en la salida (ii) del encargo, ahora como una afirmación precisa sobre la salida (iii):

> **El obstáculo del cuadrado se descompone como (C-cok) ⊕ (C-rank). La tolerancia es un isomorfismo de "reparación" sobre (C-cok) en cualquier dimensión (condicional a A1–A3). Sobre (C-rank), la tolerancia depende de la existencia de una norma canónica sobre los cociclos; esa norma existe en dim 1 (= divisor de Arakelov, codim 1) y NO existe en dim 2 (sería la forma de intersección de la superficie, codim 1 en dim 2 = G2). La tolerancia 1D no es "no functorial bajo producto" (A2 es plausible); el problema es que el INPUT que la hace funtorial (la norma) no está disponible en dim 2 sin G2.**

Esto refina el veredicto del Doc 121 (Cruce B "TÉCNICO, riesgo-RH nulo"): la parte TÉCNICA (C-cok, condicional a A1–A3) es real y sin riesgo RH; pero **bajo la parte TÉCNICA late una dependencia de G2** que el Doc 121 no había aislado. El Cruce B *no* desbloquea G1 por sí solo: desbloquea el **objeto** $H^1_{\mathrm{tol}}$ pero no su **dimensión funtorial**, y la dimensión es lo que G1 necesita (G1 = cohomología *finito-dimensional*).

**Riesgo RH:** aun así **nulo** en la parte (C-cok). La dependencia de G2 que aíslo no introduce circularidad con RH — introduce una **dependencia de fase** (G1 reposa sobre G2 para su parte numérica), que es exactamente el orden $\text{R-SIG}\prec\text{R-FIN}$ del Doc 119 §2.4 reapareciendo desde el lado de la construcción del cuadrado. **[CONSTRUCCIÓN]** + **[DATO Doc 119 §2.4]**. Coherencia interna fuerte: dos derivaciones independientes (la ingeniería inversa de Doc 119 y la construcción directa de aquí) llegan al mismo orden.

---

## 4. PASO 4 — El caso de prueba C_p × C_p

Hago concreto el diagnóstico en el cuadrado de UNA órbita periódica, el objeto de juguete más simple del sitio de escala.

### 4.1. Los factores: qué hay y qué no en C_p

**[DATO]** (1603.03191, §5, Thm 5.6, Thm 5.17):
- $C_p = \mathbb R_+^*/p^{\mathbb Z}$, círculo cuasi-tropical de longitud $\log p$ (en $u=\log\lambda$, el toro $\mathbb R/\log p\,\mathbb Z$). Haz $\mathcal O_p$: funciones periódicas, convexas, afines a trozos, con pendientes en $H_p\subset\mathbb Q$ (denominador potencia de $p$).
- $H^0(D) = \{f\in\mathcal K(C_p): D+(f)\ge 0\}$, **módulo idempotente sobre $\mathbb R_{\max}$**, no espacio vectorial.
- **Dimensión continua real:** $\mathrm{Dim}_{\mathbb R}H^0(D) = \lim_n p^{-n}\dim_{\mathrm{top}}H^0(D)^{(p^n)}$ (dimensión de recubrimiento de Lebesgue, normalizada).
- **RR (Thm 5.17):** $\mathrm{Dim}_{\mathbb R}H^0(D) - \mathrm{Dim}_{\mathbb R}H^0(-D) = \deg D$.
- **NO HAY $H^1$ en $C_p$** **[DATO]**: el texto no lo define; su rol lo juega $H^0(-D)$. La RR es una identidad solo con $H^0$.
- Grupo de clases: $\mathrm{Div}(C_p)/\mathcal P \cong \mathbb R\times\mathbb Z/(p-1)\mathbb Z$ (grado real + característica torsional).

### 4.2. El cálculo del cuadrado, paso a paso, y dónde se traba

**[CONSTRUCCIÓN].** $C_p\times C_p$ en coordenadas $(u,v)\in (\mathbb R/\log p\,\mathbb Z)^2$: un **toro tropical bidimensional** de área $(\log p)^2$. Quiero $H^1(C_p\times C_p, \mathcal O)$.

**Intento A — Künneth.** Lo natural sería
$$ H^1(C_p\times C_p) \;\overset{?}{=}\; \big(H^0(C_p)\otimes H^1(C_p)\big)\,\oplus\,\big(H^1(C_p)\otimes H^0(C_p)\big). $$
**Se traba inmediatamente [GAP]:** $H^1(C_p)$ **no existe** (§4.1). El cuadrado **no puede heredar su $H^1$ de los factores** porque los factores no tienen $H^1$ — tienen una RR de tipo II que *evita* $H^1$ usando $H^0(-D)$. La dualidad $H^0(-D)$ es un sustituto escalar del $H^1$ que **no tensoriza** (no es un objeto, es el otro lado de una resta de dimensiones). Conclusión parcial: **no hay Künneth tropical disponible**; el $H^1$ del cuadrado, si existe, es genuinamente bidimensional y hay que construirlo sobre el recubrimiento del producto.

**Intento B — Čech directo sobre el toro 2D.** Tomo el recubrimiento mínimo del toro $(\mathbb R/\log p\,\mathbb Z)^2$ por, digamos, cuatro rectángulos abiertos $U_{00},U_{01},U_{10},U_{11}$ (el recubrimiento estándar del toro que calcula su cohomología simplicial: nervio = el toro como complejo CW con 1 celda-0, 2 celdas-1, 1 celda-2). El complejo de Čech idempotente:
$$ \check C^0 = \textstyle\prod_i \mathcal O(U_i),\quad \check C^1 = \prod_{i<j}\mathcal O(U_{ij}),\quad \check C^2 = \prod \mathcal O(U_{ijk}). $$

**Qué se calcularía SIN tolerancia (cohomología topológica subyacente) [CONSTRUCCIÓN, cálculo de juguete simbólico]:** el toro real $T^2=(\mathbb R/\log p\,\mathbb Z)^2$ tiene $H^1(T^2;\mathbb R)=\mathbb R^2$, $H^2=\mathbb R$. Desarrollo el complejo explícitamente. Con el recubrimiento de cuatro cartas $U_i$ ($i=00,01,10,11$), las secciones de $\mathcal O$ sobre una carta son funciones convexas afines a trozos $f(u,v)$ con $\partial_u f,\partial_v f\in H_p$. El cociclo $\delta^0$ de una $0$-cocadena $(f_i)_i$ es, en característica 1,
$$(\delta^0 f)_{ij} = f_j|_{U_{ij}} \;\text{"}{-}\text{"}\; f_i|_{U_{ij}},$$
donde la "resta" es el problema: en $\mathbb R_{\max}$ no existe. El sustituto idempotente de "cociclo" es la condición de **compatibilidad de pendientes** en los solapes: una $1$-cocadena $(\zeta_{ij})$ es cocíclica si los saltos de pendiente se cancelan alrededor de cada $2$-celda. Las soluciones módulo cobordes están indexadas por las **dos clases de monodromía de pendiente** alrededor de los dos ciclos generadores $\gamma_u:u\mapsto u+\log p$ y $\gamma_v:v\mapsto v+\log p$: a cada clase le corresponde el **incremento neto de pendiente** $\oint_{\gamma}\!d(\partial f)\in H_p$ tras recorrer el ciclo. Es decir, **ingenuamente**
$$H^1(C_p\times C_p)\;\cong\; H_p\,\gamma_u \;\oplus\; H_p\,\gamma_v \qquad(\text{2 copias del grupo de pendientes}).$$
Pero $H_p=\{m/p^n:m\in\mathbb Z,n\ge 0\}$ es **denso en $\mathbb R$**; al tomar la dimensión continua tipo II (filtración por $p^{-n}$, igual que en la RR de la §4.1) cada copia aporta **dimensión real, no entera**, y
$$\mathrm{Dim}_{\mathbb R}H^1(C_p\times C_p)\;=\;2\cdot(\text{dimensión continua tipo II del grupo de pendientes}),$$
un real positivo, no un entero. (El factor $2$ son los dos ciclos del toro; cada ciclo es un $C_p$, así que reaparece la dimensión tipo II de un factor.) **[CONSTRUCCIÓN, estatus: cálculo simbólico del toro; a verificar la definición precisa de las clases de monodromía y la normalización tipo II en grado 1.]**

Comparación con el divisor: el cálculo anterior es para $\mathcal O$ (divisor trivial); para $\mathcal O(D)$ con $D$ un divisor del cuadrado (una curva tropical dentro de $C_p\times C_p$, p.ej. la diagonal o una correspondencia $\Psi(\lambda)$), las clases se tuercen por $D$ y aparece la dependencia que el RR debería gobernar — pero sin $H^1$ funtorial no hay RR de superficie que escribir. Es donde el cálculo de juguete toca el muro.

**¿Aparecen null elements? SÍ [CONSTRUCCIÓN].** En el cruce de los rectángulos, una sección de $\mathcal O(U_{ij})$ puede tener valor $-\infty$ (absorbente) en parte de la intersección si la función convexa "se va a $-\infty$" allí (las funciones convexas afines a trozos en un compacto idempotente admiten el valor $-\infty$ como el "cero" del módulo). Un cociclo $\zeta$ con componente $-\infty$ en $U_{01}$ pero finita en $U_{10}$ **no es coborde de ninguna $\eta$ global** en $\mathbb B\text{mod}$ (porque restar $-\infty$ no está definido), y produce una **clase parásita** — exactamente la "unwanted contribution" de 1805.10501. **[CONSTRUCCIÓN, estatus: instancia explícita del mecanismo de §1.3 en el toro 2D.]**

**¿La tolerancia los mata? PARCIALMENTE [CONSTRUCCIÓN].** Con la relación $\mathcal R_k=\{(\zeta,\zeta'):\zeta-\zeta'\in\operatorname{im}\delta^0(k_+)\}$ (tolerancia: difieren por un coborde controlado por norma), los cociclos que difieren solo en componentes $-\infty$ caen en la misma clase de tolerancia. Concretamente: si $\zeta$ tiene $-\infty$ en $U_{01}$ y $\zeta'$ es finita allí pero coinciden en lo demás, entonces $\zeta-\zeta'$ está "soportado en el absorbente" y la relación de tolerancia lo declara equivalente a $0$ **sin** ejecutar la resta prohibida (precisamente el mecanismo de §2.2: conservar el módulo, añadir la relación). → **las clases parásitas (C-cok) se colapsan.** Esto es genuino y es lo que la tolerancia aporta.

PERO: para decir "la dimensión de $H^1_{\mathrm{tol}}(C_p\times C_p)$ es tal número" necesito $\dim_{\mathbb S}=$ "mínimo de generadores con $\sum|\alpha(f)f|\le N$", y aquí **no hay $N$**: en dim 1, $N=e^a$ venía de la parte arquimediana del divisor de Arakelov; en el toro 2D **no hay divisor de Arakelov de codim 1 sobre una superficie sin forma de intersección** que provea la norma. Sin $N$, "mínimo de generadores con norma" degenera a "mínimo de generadores" a secas — que por la densidad de $H_p$ y la libertad de las pendientes es **no acotado / continuo**, no un entero. Resultado: $H^1_{\mathrm{tol}}(C_p\times C_p)$ **existe como objeto con tolerancia (clases parásitas colapsadas), pero su dimensión sigue siendo real/continua (tipo II) y no entera**, y depende de la normalización mientras no se fije la norma. Exactamente Example 6.5 reapareciendo: el objeto $H^1_{\mathrm{tol}}$ está bien definido como módulo-con-tolerancia, pero su **rango no es funtorial** sin la norma de intersección.

### 4.3. El resultado del caso de prueba, sin adorno

**[CONSTRUCCIÓN — resumen del juguete]:**
1. **Aparecen null elements:** sí, explícitamente (cociclos con componente $-\infty$ en las intersecciones del recubrimiento del toro).
2. **La tolerancia los mata:** sí, en cuanto a (C-cok) — las clases parásitas se colapsan a tolerancia trivial. El objeto $H^1_{\mathrm{tol}}$ queda bien definido (condicional a A1–A3).
3. **La dimensión resultante es finita y entera:** **NO.** Sigue siendo **real-valuada / continua tipo II** (por la densidad de $H_p$ en $\mathbb R$, idéntico al fenómeno de $\mathrm{Dim}_{\mathbb R}$ de la RR tropical), porque falta la norma canónica que en dim 1 venía del divisor de Arakelov. La dimensión es del orden de "2 × (dimensión continua tipo II)" — el "2" de los dos ciclos del toro, cada uno con dimensión continua.
4. **El Künneth no existe** (los factores no tienen $H^1$); el $H^1$ del cuadrado es genuinamente 2D.

**Veredicto del Paso 4:** el caso de prueba **NO cierra G1**. Confirma exactamente el diagnóstico del Paso 3: la tolerancia entrega el **objeto** pero no la **finitud entera**; la finitud entera necesita la norma = forma de intersección = G2. **Es la mejor evidencia honesta de que el Cruce B funciona para (C-cok) y se traba en (C-rank).**

---

## 5. PASO 5 — Finitud (R-FIN): las dos finitudes, distinguidas

**[DATO Doc 119 §2.4]:** la $\dim H^1$ **total** debe ser $\infty$ (infinitos ceros); lo que debe ser finito es la parte **impura** (peso $\ne 1/2$, o $\ne 1$ según normalización), y la separación en pesos **es G2**, que no tengo. Por tanto debo ser honesto sobre **qué finitud** estoy abordando.

**[CONSTRUCCIÓN] Hay tres finitudes distintas en juego, y solo la primera es de G1:**

1. **Finitud combinatoria del nervio (G1, abordable).** El recubrimiento finito $\mathcal U$ tiene un nervio finito (en C_p × C_p: 4 abiertos, finitas intersecciones). Los grupos de Čech $\check C^p(\mathcal U)$ están **graduados por grado simplicial $p$ y por soporte** (qué intersección), y en cada grado el módulo es de **tipo finito como módulo idempotente generado** (finitos generadores combinatorios: los "monomios tropicales" del recubrimiento). **Esta finitud SÍ la obtengo** (condicional a A1–A3): $H^1_{\mathrm{tol}}$ es un 𝕊-módulo con tolerancia **finitamente presentado** en el sentido combinatorio. Es finitud de **presentación**, no de **dimensión**.

2. **Finitud de la dimensión tipo II (NO la obtengo entera).** $\mathrm{Dim}_{\mathbb R}H^1_{\mathrm{tol}}$ es un número real finito (es un toro compacto), pero **real, no entero** (§4.3). "Finito" en el sentido de "número real acotado", sí; "finito" en el sentido de G1 ("dimensión = entero = rango de un objeto"), **no**. Falta la norma.

3. **Finitud de la parte impura (R-FIN, NO abordable en G1).** Requiere la graduación de pesos $W$ para definir "impura"; sin $W$ (= sin G2) el enunciado "$\dim(\bigoplus_{w\ne 1}\mathrm{gr}^W_w H^1) < \infty$" **no es ni siquiera formulable** (Doc 119 §2.4, "R-FIN no es enunciable sin R-SIG"). **[DATO]**

**Declaración honesta de cuál obtengo [CONSTRUCCIÓN]:** obtengo **la finitud combinatoria de los grupos de Čech graduados por grado/soporte** (finitud de tipo 1), condicional a A1–A3. **NO** obtengo la finitud entera de la dimensión (tipo 2: falta la norma), ni mucho menos la finitud de la parte impura (tipo 3: es R-FIN, necesita G2). Esto es exactamente lo que el encargo anticipaba: "la finitud que podés abordar en G1 es la finitud de los grupos de Čech graduados por grado/soporte, NO la finitud de la parte impura".

**Coherencia con la tensión T1 (Doc 119 §6.3) [CONSTRUCCIÓN].** T1 dice: un $H^1$ finito-dimensional total no puede portar la traza con soporte singular en $\{k\log p\}$. Mi construcción es consistente con T1: $H^1_{\mathrm{tol}}(C_p\times C_p)$ tiene dimensión tipo II **infinita/continua** (densidad de $H_p$), no finita — así que **puede** portar el soporte singular. La finitud que obtengo (tipo 1, combinatoria) es de la *presentación*, no del *tamaño* del módulo. No hay contradicción con T1. Bien.

---

## 6. PASO 6 — EL NÚCLEO QUE FALTA: el "G1-restante"

Cierro con el enunciado exacto de lo que quedó sin construir, separando lo TÉCNICO de lo CONCEPTUAL.

### 6.1. La parte TÉCNICA (factible, riesgo-RH nulo)

**[GAP TÉCNICO — T1] El cambio de base en dimensión 2.** Verificar A1: que el producto tensorial idempotente $\mathcal O\otimes_{\mathbb B}\mathcal O$ del haz del cuadrado se reescribe como $\Gamma$-𝕊-módulo conmutando con la envolvente convexa y la tropicalización. Es el Paso 1 del Cruce B (Doc 121). Tipo conocido (CC lo hicieron en dim 1).

**[GAP TÉCNICO — T2] Dold–Kan para complejos de longitud $\ge 2$ con tolerancia.** Verificar A2: que la maquinaria $\pi_1^{\mathcal T}\circ\mathrm{DK}$ que CC usan para el complejo corto $\psi$ (longitud 1) da el objeto correcto para el complejo de Čech del cuadrado (longitud $\ge 2$), y que los cociclos con componente $-\infty$ caen en tolerancia trivial. Plausible; tipo conocido (Dold–Kan es general).

**[GAP TÉCNICO — T3] Independencia del recubrimiento.** Verificar A3: que $H^1_{\mathrm{tol}}$ no depende del nervio $\mathcal U$. Requiere un teorema de comparación de Čech tolerante (refinamientos). Tipo conocido en topología; nuevo en este formalismo idempotente, pero sin riesgo conceptual.

**Estos tres juntos = "construir el objeto $H^1_{\mathrm{tol}}(X\times X)$".** Es lo que el Cruce B prometía, y es genuinamente TÉCNICO: cierra (C-cok). Lo puede hacer el equipo CC con su maquinaria de 2017–2023.

### 6.2. La parte CONCEPTUAL (el núcleo real)

**[GAP CONCEPTUAL — el núcleo del G1-restante] La norma canónica sobre cociclos del cuadrado = dimensión funtorial entera.**

Enunciado exacto:
> Falta una **norma canónica** $\|\cdot\|$ sobre los cociclos de Čech del cuadrado (o sobre las clases del análogo de $\mathrm{NS}(X\times X)$) tal que $\dim_{\mathbb S}H^1_{\mathrm{tol}} := $ (mínimo de generadores con $\|\cdot\|$ controlada) sea **(a) un entero, (b) invariante de isomorfismo, (c) computable del sitio**. Sin ella, Example 6.5 de [yoshi] garantiza que el rango no es funtorial y G1 (cohomología *finito-dimensional*, con dimensión = entero) no se obtiene.

**Por qué es CONCEPTUAL y no técnico:** esa norma, en dim 1, ES el grado del divisor de Arakelov (codim 1, un dato escalar). En dim 2, el dato análogo de codim 1 en una superficie con un invariante numérico es una **forma de intersección** $D\cdot D'$ — que es **exactamente G2** (la estructura de signatura, Doc 119 §2.3 realización (i); la "intersection theory of divisors on the square of the Scaling Site" que CC declaran *in development* desde 2021, Doc 120 §4.4). **No hay candidato en el corpus.** Es matemática nueva.

**[CONSTRUCCIÓN — el resultado estructural de este documento]:**
> **G1 no es independiente de G2.** La construcción del cuadrado vía tolerancia separa G1 en (C-cok), que es TÉCNICO y cerrable, y (C-rank), cuya resolución *es* la norma de intersección, que *es* G2. El "muro" no está entre G1 y G2 como dos nodos secuenciales: **la parte numérica de G1 (finitud entera) y G2 (signatura) son el mismo objeto** — una forma de intersección sobre el cuadrado. La tolerancia construye el receptáculo; el contenido numérico del receptáculo es G2.

Esto coincide, por una segunda ruta independiente, con la inversión de orden de Doc 119 §2.4 ($\text{R-SIG}\prec\text{R-FIN}$: "el muro G2 está aguas arriba de la propia formulación de la finitud"). **Dos derivaciones independientes, mismo veredicto** — es la evidencia más fuerte de honestidad del diagnóstico. **[CONSTRUCCIÓN]** + **[DATO Doc 119]**.

### 6.3. Qué necesito de Connes — lista concreta

1. **El texto completo de Example 6.5 de [yoshi]** (la referencia "yoshi" de 1805.10501). Necesito la identificación bibliográfica exacta y el ejemplo verbatim: es la formulación más precisa que existe de (C-rank), y mi diagnóstico entero descansa en leerlo bien. **[Pregunta a CC / búsqueda bibliográfica pendiente.]** Mi lectura es que es un ejemplo de la literatura tropical (estilo Yoshida) donde $r(D)$ no es invariante de iso de módulos; confirmarlo y leer el mecanismo exacto.

2. **¿Existe continuación no publicada de 1703.02325 (*Homological algebra in characteristic one*) hacia dimensión 2?** Específicamente: ¿definieron Ext / Čech tolerante para complejos de longitud $\ge 2$? Si A2 (§6.1) ya está hecho por ellos sin publicar, T2 se cierra.

3. **¿Tienen una norma canónica sobre clases de codim 1 del cuadrado?** Es la pregunta del núcleo (§6.2). Su frase "intersection theory of divisors on the square of the Scaling Site, still in development" (2006.13771) sugiere que SÍ lo están trabajando — necesito saber **en qué estado está esa norma de intersección**, porque ES el núcleo conceptual de G1+G2.

4. **El tratamiento del término divergente $2h(1)\log\lambda$** de 2602.15941 §9.3: si la norma de intersección se define como límite regularizado, ese término es donde se define — y la tensión T2 de Doc 119 (signaturas no sobreviven límites sin gap) ataca exactamente ahí. Necesito saber si su regularización preserva una signatura.

5. **Aclaración sobre el cambio de base $\mathbb B\to\mathbb S$ en dim 2** (A1): ¿conmuta el producto tensorial idempotente del cuadrado con la presentación en Γ-anillos? Es la única pieza puramente técnica que podría tener una sorpresa (su propio "riesgo declarado" en el Paso 1 del Cruce B).

---

## 7. Síntesis y honestidad

**No declaro G1 cerrado.** El caso de prueba (Paso 4) **no cierra** y la construcción (Paso 3) **no es completa**: produce el objeto $H^1_{\mathrm{tol}}$ (condicional a tres gaps técnicos) pero no su dimensión entera funtorial.

**Lo construido (todo [CONSTRUCCIÓN], a verificar por expertos, NUNCA [DATO]):**
- La identificación de la **bifurcación (C-cok)/(C-rank)** del obstáculo del cuadrado, anclada en la cita de fuente sobre la raíz (Example 6.5 de [yoshi]).
- La **construcción condicional de $H^1_{\mathrm{tol}}(X\times X)$** vía Dold–Kan sobre el complejo de Čech tolerante (§3.1), con sus tres asunciones aisladas.
- El **cálculo de juguete C_p × C_p** (§4): null elements explícitos, colapso de las clases parásitas por tolerancia, dimensión que **permanece tipo II / continua** por falta de norma.
- La **distinción de las tres finitudes** (§5) y la declaración honesta de que solo obtengo la combinatoria.
- El **aislamiento del núcleo** (§6.2): la norma de intersección = dimensión entera funtorial = G2, con la consecuencia estructural de que la parte numérica de G1 y G2 son el mismo objeto.

**El punto de traba ES el resultado:** la tolerancia construye el receptáculo (C-cok, técnico); el contenido numérico del receptáculo (C-rank) es una forma de intersección que es G2 y no existe. El Cruce B, correctamente entendido, **no es independiente del muro** — es su mitad sintáctica.

---

## Referencias

**Internas (backward-only):** Doc 119 (R-SIG, R-FIN, orden $\text{R-SIG}\prec\text{R-FIN}$, §2.3–2.4, tensión T1/T2); Doc 120 (§1.3, §3.2, §4.4, §6.1, §6.3, §8 — inventario en fuente); Doc 121 (Cruce B: 5 pasos, caso C_p × C_p, §2.2; Cruce A / experimento 121.E); roadmap-rh (G1–G4, S1–S3).

**Corpus CC/CCM (leído/re-leído en fuente esta sesión, junio 2026, vía ar5iv):**
- A. Connes, C. Consani, *The Riemann-Roch strategy, Complex lift of the Scaling Site*, arXiv:1805.10501 — Introducción (obstáculo de los null elements; "root ... in Example 6.5 of [yoshi]"); §2 (resolución de la diagonal, Čech tropical, ref. [CC5]); §3.2 (descenso tropical); §4 (funciones casi-periódicas de Bohr). **[DATO]**
- A. Connes, C. Consani, *Homological algebra in characteristic one*, arXiv:1703.02325 (Higher Structures 3 (2019) 155–247) [= [CC5]] — $\mathbb B\text{mod}$, AB1/AB2 sin AB-aditividad (semi-aditiva, sin sustracción), comonad, Kleisli/Eilenberg–Moore, Ext no triviales. **[DATO]**
- A. Connes, C. Consani, *Riemann-Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$*, arXiv:2205.01391 — Prop. 2.2(ii) (tolerancia $\mathcal R_k$); Apéndices A (categoría $\Gamma\mathcal T_+$, Def. A.2 dimensión por generadores con norma) y B (Dold–Kan); Prop. 3.3; §5 / Prop. 5.2 / Thm 1.2 (dualidad de Pontryagin con tolerancia, $K=-2\{2\}$, $U(1)_{1/4}$). **[DATO]**
- A. Connes, C. Consani, *Geometry of the scaling site*, arXiv:1603.03191 — §5 (C_p, $\mathcal O_p$, $\Delta_2 f$), Thm 5.6 (clase de divisores $\mathbb R\times\mathbb Z/(p-1)\mathbb Z$), Thm 5.17 (RR tipo II, $\mathrm{Dim}_{\mathbb R}$, sin $H^1$). **[DATO]**
- A. Connes, C. Consani, *Weil positivity...*, arXiv:2006.13771 — "intersection theory of divisors on the square of the Scaling Site, still in development" (vía Doc 120 §4.4). **[DATO]**

**Pendiente de identificar [NO VERIFICADO]:** la referencia "[yoshi]" de 1805.10501 (Example 6.5; conjeturalmente literatura tropical estilo Yoshida sobre rango de divisores no invariante de iso de módulos). Es la pieza de fuente #1 a conseguir (§6.3).

*Fin del Doc 123.*
