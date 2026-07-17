# Doc 126 — El índice de Hodge sobre el cuadrado: ¿alcanzable o RH-circular? Análisis del paquete de Kähler

**Programa:** Hipótesis de Riemann — Phase 41: CONSTRUIR G2.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 124 (G2 = índice de Hodge, forma INDEFINIDA de signatura (1, ρ−1); la distinción positividad-intersección [BUENA] vs positividad-espectral [CIRCULAR]; veredicto: la positividad de CC es espectral, no de intersección); Doc 123 (bifurcación (C-cok)/(C-rank); la tolerancia repara (C-cok), no (C-rank); en dim 2 el dato de (C-rank) ES la forma de intersección = G2; el resultado estructural "la parte numérica de G1 y G2 son el mismo objeto"); Doc 119 (R-PESO(b): pureza como TEOREMA geométrico; el test de no-circularidad R-NC, cláusulas NC1 externalidad / NC2 sobregeneración / NC3 no-reducción a catálogo MW / NC4 dos mundos; orden R-SIG ≺ R-FIN); Doc 80 (Castelnuovo–Severi aritmético; Proposición 8.1 "ninguna forma definida solo en términos de una medida distingue las dos medidas"; el Paso A/Paso B de Weil; la circularidad de la diferencia de medidas).

**TRABAJO EN PARALELO:** Doc 125 (otro documento del programa) construye la forma de intersección concreta sobre el cuadrado. Este documento NO usa su forma explícita: trabaja con las **propiedades requeridas** (signatura (1, ρ−1), clases f₁, f₂, Δ, correspondencias) y evalúa la **estrategia de prueba**. Las propiedades que supongo de la forma se etiquetan **[SUPUESTO-DE-125]**.

**Disciplina de etiquetado (regla absoluta, máximo riesgo de falsa victoria):** **[DATO]** = leído en fuente esta sesión (arXiv / survey, con cita), o teorema interno del programa (cita backward-only). **[CONSTRUCCIÓN]** = lo que diseño/analizo yo, con estatus explícito. **[CÁLCULO]** = derivación mía mostrada. **[GAP]** = lo que falta, con precisión. **[CONJETURA]** / **[NO VERIFICADO]** = como se indica. **[SUPUESTO-DE-125]** = propiedad de la forma que tomo de Doc 125 sin re-derivar. **NUNCA "probado"** salvo lo que lo esté. El objetivo es evaluar SI un teorema del índice de Hodge es alcanzable para este objeto y aislar el núcleo irreducible — NO declararlo probado. Si el núcleo resulta RH-equivalente (circular), ese es el resultado más importante posible y se declara sin rodeos.

---

## 0. Resumen ejecutivo

Este documento confronta la estrategia "índice de Hodge sobre el cuadrado" (= G2 = la pureza = RH) con el único corpus de matemática donde un paquete de Kähler se probó por métodos combinatorios/tropicales NUEVOS, no por geometría compleja: Adiprasito–Huh–Katz (AHK, arXiv:1511.02888) para matroides, y su frontera dura, Babaee–Huh (BH, arXiv:1502.00299), donde la positividad tropical NO implica la algebraica. La pregunta maestra de toda la Phase 41 es: ¿el núcleo irreducible de G2 es (a) un teorema de Kähler-package tropical genuino (no circular, matemática nueva pero concebible), (b) RH-circular disfrazado, (c) obstruido tipo BH, o (d) indeterminable hoy?

**Hallazgos centrales:**

1. **AHK NO aplica al cuadrado del sitio de escala, por una obstrucción estructural precisa y no reparable con el método actual:** AHK es un teorema sobre un anillo de Chow graduado de un objeto **finito** (matroide de rango finito ⟹ abanico de Bergman simplicial finito), probado por **inducción finita** (deletion–contraction / flips matroidales) sobre la red de subconjuntos. El cuadrado del sitio de escala es **infinito-dimensional, con flujo continuo ℝ₊\*** y "género = ∞" (infinitos ceros de ζ); las cuatro hipótesis de AHK fallan en grados distintos, pero la que **rompe el método de raíz** es la **infinitud + continuidad**, que destruye la inducción finita (§2.4). [CONSTRUCCIÓN/GAP]

2. **Babaee–Huh OBSTRUYE genéricamente, y el sitio de escala cae del lado obstruido, NO del lado AHK:** BH exhiben una corriente tropical fuertemente positiva (2,2) en una 4-variedad tórica cuya clase **no** es límite de ciclos algebraicos, "porque su forma de intersección no tiene la signatura correcta del Hodge index theorem" [DATO, BH abstract verbatim]. El **criterio que separa los dos casos** es matroidalidad/Lefschetz: el abanico de Bergman de un matroide es **fuertemente extremal** y satisface Hodge–Riemann (AHK); un abanico tropical genérico (balanceado pero no matroidal) **no**. El cuadrado del sitio de escala **no tiene razón conocida para ser matroidal**; su forma de intersección es exactamente del tipo cuya signatura BH muestra que puede fallar. (§3) [DATO + CÁLCULO]

3. **El núcleo irreducible (§4):** "El cuadrado del sitio de escala satisface las relaciones de Hodge–Riemann en grado medio (signatura (1, ρ−1) con definitud negativa sobre el primitivo)". Sometido a R-NC con máximo rigor: el enunciado **como teorema de paquete de Kähler genérico** pasaría NC1, NC2, NC4 (es la situación de Castelnuovo). **PERO** sobre **nuestro** objeto, la positividad sobre el primitivo restringida a las correspondencias del flujo (Γ_F y sus iterados) **ES** la positividad de Weil del Doc 124, que **FALLA NC3** (es MW-1). El veredicto se bifurca según un eje preciso: **si la signatura es un teorema geométrico del cuadrado (vale para toda correspondencia, probado sin ζ), no es circular y G2 es alcanzable-en-principio; si la signatura sólo puede establecerse sobre las correspondencias de ζ, es la positividad de Weil renombrada y es circular.** (§4)

4. **Veredicto (§5): (d) con sesgo fuerte hacia (b)/(c), y un único camino estrecho hacia (a).** La diferencia exacta con cuerpos de funciones (§4.4): allá C×C es una variedad algebraica genuina cuya teoría de intersección de Grothendieck da Castelnuovo **gratis y para todo divisor** (NC2 con contenido); el índice de Hodge para superficies es un teorema clásico, anterior a cualquier ζ. Acá el "cuadrado" es tropical/característica 1 y su teoría de intersección **es justamente lo que falta** (Doc 123 §6.2). BH muestra que en el mundo tropical el índice de Hodge **no es gratis** — falla para superficies tropicales genéricas. Por tanto el camino (a) requiere probar que el cuadrado del sitio de escala es del subtipo matroidal/Lefschetz donde el índice SÍ vale — un teorema de Kähler-package tropical genuino, concebible pero hoy ausente, y cuya verificación R-NC depende crucialmente de que sobregenere (NC2). Si en cambio la única vía de probar la signatura pasa por evaluar la forma sobre las correspondencias de ζ, recae en (b) circular. **Hoy no hay manera de decidir cuál, porque la forma de intersección del cuadrado no existe como objeto (Doc 123); Doc 125 la construye, y de su carácter — geométrico-para-toda-correspondencia vs definible-solo-sobre-ζ — depende el veredicto.**

---

## 1. EL PAQUETE DE KÄHLER [DATO]

### 1.1. Enunciado preciso de las tres propiedades

**[DATO]** (AHK, arXiv:1511.02888, Annals of Math. 188 (2018) 381–452; survey Eur–Larson, *Notices AMS* mar. 2025; survey "Essence of independence", arXiv:2211.05724.) Sea $A^\bullet = \bigoplus_{k=0}^{d} A^k$ un anillo graduado conmutativo de dimensión real finita sobre $\mathbb R$, con $A^0 = \mathbb R$ y $A^d \cong \mathbb R$ (un "grado tope" canónicamente isomorfo a $\mathbb R$ por un morfismo de grado $\deg: A^d \to \mathbb R$). El **paquete de Kähler** para $A^\bullet$, respecto de un elemento (clase amplia / de Lefschetz) $\ell \in A^1$, consiste en las tres propiedades:

1. **Dualidad de Poincaré (PD).** El emparejamiento
$$ A^k \times A^{d-k} \longrightarrow A^d \xrightarrow{\ \deg\ } \mathbb R, \qquad (x,y)\mapsto \deg(x\cdot y) $$
es **no degenerado** para todo $0\le k\le d$. En particular $\dim A^k = \dim A^{d-k}$.

2. **Hard Lefschetz (HL).** Para $0\le k\le d/2$, la multiplicación iterada por $\ell$,
$$ \ell^{\,d-2k}\cdot:\ A^k \xrightarrow{\ \sim\ } A^{d-k}, $$
es un **isomorfismo**. (Implica que $\dim A^k$ es unimodal-creciente hasta el grado medio.)

3. **Relaciones de Hodge–Riemann (HR).** Definida la **parte primitiva** $P^k := \ker(\ell^{\,d-2k+1}: A^k\to A^{d-k+1})$, la forma cuadrática
$$ Q_\ell^k(x) := (-1)^k\,\deg(\ell^{\,d-2k}\, x^2), \qquad x\in P^k, $$
es **definida positiva** sobre $P^k$ (para $0\le k\le d/2$).

**[CÁLCULO] El índice de Hodge es el caso de grado medio de HR.** En una **superficie** ($d=2$), el grado medio es $k=1$, $P^1 = \ker(\ell\cdot: A^1\to A^3=0) = A^1\cap (\text{ortogonal de }\ell)$ — el primitivo es el ortogonal de la clase amplia bajo la forma de intersección. HR en $k=1$ dice: $Q_\ell^1(x) = -\deg(x^2) = -x\cdot x > 0$ para $x\in P^1\setminus\{0\}$, es decir **$x\cdot x < 0$ sobre el ortogonal de la clase amplia** — exactamente el **teorema del índice de Hodge clásico**: la forma de intersección tiene signatura $(1,\rho-1)$, una dirección positiva (la de $\ell$) y $\rho-1$ negativas (el primitivo). [Doc 124 §1.1 fijó este perfil como la positividad-intersección "buena".]

### 1.2. El anillo de Chow de un matroide y qué estructura necesita AHK

**[DATO]** (AHK; Eur–Larson; arXiv:2211.05724.) Para un matroide $M$ de rango $r$ sobre un conjunto base $E$ finito, el **anillo de Chow** $A^\bullet(M)$ es el anillo de Chow del **abanico de Bergman** $\Sigma_M$ (un abanico simplicial **finito** en $\mathbb R^E/\mathbb R\mathbf 1$, cuyos conos corresponden a cadenas de flats de $M$). Es un cociente explícito de un anillo de polinomios por relaciones lineales (de incidencia de flats) y cuadráticas (de Stanley–Reisner). Propiedades estructurales:
- **Graduación finita** $A^\bullet(M)=\bigoplus_{k=0}^{r-1}A^k(M)$, con $d=r-1$. [DATO]
- **Grado tope** $A^{r-1}(M)\cong\mathbb Z$ canónicamente (Poincaré "trivial"). [DATO]
- **Clase amplia $\ell$:** proviene de una función **estrictamente convexa lineal a trozos** sobre $\Sigma_M$ (en lenguaje tórico, un divisor amplio; en lenguaje combinatorio, una asignación submodular). El cono de tales $\ell$ es no vacío precisamente porque $\Sigma_M$ es el abanico de una variedad tórica "suficientemente positiva". [DATO]
- **Inducción por flips / deletion–contraction:** la prueba relaciona $A^\bullet(M)$ con $A^\bullet(M\setminus i)$ y $A^\bullet(M/i)$ (borrado y contracción de un elemento) mediante secuencias exactas y "modificaciones matroidales" (matroidal flips), permitiendo bajar el rango. [DATO]

**[DATO] La estructura mínima que el método AHK necesita** (extraída de los surveys): (i) un **anillo de Chow graduado de dimensión finita** con grado tope $\cong\mathbb R$; (ii) **dualidad de Poincaré** (que para abanicos viene de ser un abanico de variedad tórica suave/simplicial completo, o de la propiedad de Poincaré tropical); (iii) una **clase amplia** (función estrictamente convexa lineal a trozos / cono de Kähler no vacío); (iv) la **maquinaria de flips y un orden poliédrico** sobre una **red finita** (los flats del matroide) que permita la inducción.

### 1.3. Cómo AHK prueban el paquete: inducción simultánea de las tres propiedades

**[DATO]** (AHK; surveys.) La arquitectura de la prueba —y esto es lo decisivo para evaluar la transplantabilidad— es:

> Se prueban **PD, HL y HR a la vez, por inducción simultánea**, NO una tras otra. Se ordenan los matroides (o los abanicos intermedios de una secuencia de flips) y se argumenta: suponiendo el paquete de Kähler para los objetos "anteriores" (rango menor, o un flip atrás), se deduce para el objeto actual. El motor del paso inductivo es:
> - un **mapa de Lefschetz** (multiplicación por la clase amplia $\ell$) cuyo carácter de isomorfismo (HL) se controla con HR del paso anterior;
> - la **firma/signatura** de la forma HR es un **invariante discreto** (número de signos $+$ y $-$); cambia sólo por cruce de cero de un autovalor; el argumento inductivo (deformación de $\ell$ dentro del cono amplio, conexo) muestra que **ningún autovalor cruza cero** porque PD garantiza no-degeneración a lo largo del camino, luego la signatura se **transporta** desde un objeto base donde es conocida.

El núcleo del método es por tanto: **(α) una red finita sobre la que inducir; (β) la no-degeneración (PD) a lo largo de una deformación de $\ell$ en un cono amplio conexo; (γ) un caso base con signatura conocida; (δ) la rigidez de la signatura como invariante discreto bajo deformación con no-degeneración.** Sin la finitud de (α), la inducción no arranca; sin la conexidad/finitud del cono amplio en (β), el transporte de signatura no está garantizado. **[CÁLCULO sobre DATO.]**

**[DATO] Punto clave para Phase 41:** AHK probaron el paquete **sin usar ningún resultado de geometría algebraica compleja** — es un teorema combinatorio genuino. Esto es exactamente el tipo de "matemática nueva pero concebible" que el camino (a) del veredicto requeriría. La pregunta es si la arquitectura (α)–(δ) sobrevive al sitio de escala.

---

## 2. ¿APLICA AHK AL CUADRADO DEL SITIO DE ESCALA? [CONSTRUCCIÓN/GAP]

El sitio de escala **no** es un abanico de Bergman ni un matroide: es un objeto de característica 1 con un flujo $\mathbb R_+^*$, infinito, con "género" = (los infinitos ceros de ζ). Reviso las cuatro hipótesis (a)–(d) del encargo.

### 2.1. (a) ¿Hay un anillo de Chow / cohomología graduada del cuadrado?

**[DATO-DE-123].** Doc 123 construyó —**condicional a tres gaps técnicos A1–A3**— un candidato $H^1_{\mathrm{tol}}(X\times X)$ vía Dold–Kan sobre el complejo de Čech tolerante. Es un **𝕊-módulo con tolerancia**, no un anillo graduado con producto. Estatus:
- **Lo que hay:** un $H^1$ tolerante (objeto), con la mitad sintáctica del obstáculo (C-cok) reparada. [DATO-DE-123 §3.1]
- **Lo que NO hay:** un **anillo de Chow** $A^\bullet$ con producto graduado y grado tope $\cong\mathbb R$. La estructura de **anillo** (el producto que define la forma de intersección $x\cdot y$) es precisamente lo que falta — Doc 123 §6.2 lo aísla como (C-rank) = la norma de intersección = G2. [DATO-DE-123]

**[CÁLCULO] Diagnóstico hipótesis (a): PARCIAL/FALLA.** Hay un grupo de cohomología candidato (tolerante), pero **no un anillo graduado con producto**. AHK necesita un **anillo de Chow** entero $A^\bullet$ (la forma de intersección ES el producto $A^1\times A^1\to A^2$). El producto es justamente lo ausente. **La hipótesis (a) de AHK NO se cumple hoy** — y Doc 125 está intentando construir precisamente ese producto. Sin él, ni siquiera se puede enunciar HR.

### 2.2. (b) ¿Hay dualidad de Poincaré?

**[DATO-DE-120/123].** Doc 120 reporta que en el corpus CC hay una **dualidad de Serre con tolerancia en dimensión 1** (la dualidad $H^0(D)\leftrightarrow H^0(-D)$ de la RR tipo II del sitio de escala, 1603.03191 Thm 5.17). Doc 122 reporta que la dualidad global de CC es de **Pontryagin** (grupo↔dual), **no una forma sobre un espacio con carácter de simetría** (Pedido 122.A: falta la polarización). [DATO]

**[CÁLCULO] Diagnóstico hipótesis (b): NO se extiende a la forma que AHK necesita.** La dualidad de Serre tolerante de dim 1 es un emparejamiento $H^0\leftrightarrow H^0(-D)$ — un dato escalar (grado), **no** un emparejamiento $A^k\times A^{d-k}\to A^d\cong\mathbb R$ con la estructura de **forma de intersección no degenerada**. Para PD en el sentido de AHK se necesita:
- el grado tope $A^2(X\times X)\cong\mathbb R$ (la "clase fundamental" del cuadrado) — **[GAP]**: no construido (sería el RR de superficie que CC declaran *in development*, Doc 120 §4.4);
- la **no-degeneración** del emparejamiento $A^1\times A^1\to A^2\cong\mathbb R$ — **[GAP]**: es la forma de intersección misma (= G2).

La dualidad de Pontryagin de CC (Doc 122) **no es** PD en el sentido de AHK: PD es una forma **simétrica sobre un único espacio graduado** ($x\cdot y = y\cdot x$ en $A^1$), mientras Pontryagin es un apareamiento grupo↔dual sin simetría intrínseca. **PD-AHK no está disponible.** [SUPUESTO-DE-125: que la forma de intersección de Doc 125, si se construye, satisfaga la no-degeneración — esto sería el contenido de PD en grado 1.]

### 2.3. (c) ¿Hay una clase amplia? ¿Qué es "amplio" en el sitio de escala?

**[CONSTRUCCIÓN].** El candidato natural a clase amplia es $\ell = f_1 + f_2$, la suma de las dos clases de fibra (horizontal $\{pt\}\times X$ y vertical $X\times\{pt\}$) — el análogo de la polarización $(1,1)$ que Weil usa en $C\times C$ [Doc 80 §1.1; Doc 124 §1.2]. [SUPUESTO-DE-125: que $f_1, f_2$ y $\Delta$ (diagonal) sean clases bien definidas en el análogo de $\mathrm{NS}(X\times X)$, con $f_1^2=f_2^2=0$, $f_1\cdot f_2 = 1$.]

**[CÁLCULO] Diagnóstico hipótesis (c): el candidato existe formalmente, pero "amplio" carece de definición intrínseca.** En AHK, "amplio" = función estrictamente convexa lineal a trozos sobre el abanico (cono de Kähler explícito y **no vacío por construcción combinatoria**). En el sitio de escala:
- $f_1+f_2$ es el candidato sintáctico, pero **¿qué hace a una clase "amplia"** en el cuadrado tropical? No hay en el corpus una noción de cono amplio / convexidad estricta sobre el análogo de $\mathrm{NS}(X\times X)$. La convexidad existe en dim 1 (las funciones convexas afines a trozos del haz $\mathcal O_p$, Doc 123 §4.1), pero **el cono amplio de divisores de una superficie tropical** no está definido. **[GAP]**
- Más grave (alimenta §2.4): el flujo $\mathbb R_+^*$ es **continuo**; el "cono amplio" en AHK es un cono poliédrico de un objeto finito sobre el que la deformación de $\ell$ recorre un conjunto conexo **finito-dimensional**. Aquí el espacio de clases tiene dimensión infinita (Doc 124 §2.4: dim $H^1=\infty$), y la deformación de $\ell$ — el paso (β) del método AHK — no tiene garantía de no cruzar degeneraciones.

### 2.4. (d) La dimensión infinita / el flujo continuo rompe la inducción de AHK — la obstrucción central

**[CÁLCULO — el análisis decisivo de §2].** La inducción de AHK (§1.3, arquitectura (α)–(δ)) es **finita y poliédrica de raíz**. Localizo dónde cada pieza muere:

1. **(α) La red de inducción es infinita.** AHK induce sobre la **red finita de flats** del matroide (deletion–contraction baja el rango en 1, y el rango es finito). El sitio de escala **no tiene rango finito**: el "género" es ∞ (infinitos ceros), dim $H^1=\infty$ [DATO Doc 124 §2.4 / CC *metaphysics of F₁*: "the dimension of $H^1(\mathbf C)$ is infinite"]. **No hay caso base alcanzable en finitos pasos.** La inducción no arranca. **Esta es la obstrucción central.** [CONSTRUCCIÓN/GAP]

2. **(β) El cono amplio no es finito-dimensional ni evidentemente conexo-controlable.** El transporte de signatura de AHK exige deformar $\ell$ dentro de un cono amplio **conexo** sin cruzar degeneraciones, y la no-degeneración (PD) a lo largo del camino se controla por finitud. En dimensión infinita, "ningún autovalor cruza cero a lo largo del camino" **no se sigue de PD** — es exactamente la **tensión T2 de Doc 119 §6.3**: *las signaturas no son continuas bajo los límites que la regularización exige* (flujo espectral discontinuo sin gap espectral uniforme, Doc 119 [DATO Phi96]). La rigidez de la signatura como invariante discreto (paso (δ)) **falla en rango infinito**: [DATO Doc 119 §2.2 / roadmap Thm. rank-sensitivity] "en rango infinito el número de autovalores negativos no es función continua de las trazas". **(δ) muere por la misma razón que la Ruta B necesita R-FIN.**

3. **Acoplamiento con la corrección de orden de Doc 119/123.** Aquí emerge una coherencia interna fuerte: Doc 119 §2.4 derivó (por ingeniería inversa) que **R-SIG ≺ R-FIN** y que **la finitud es del graduado IMPURO, no del total** (la parte pura, peso 1, es infinito-dimensional: porta los infinitos ceros). Traducido a AHK: el paquete de Kähler de AHK presupone un objeto **enteramente finito** (matroide finito), donde NO hay análogo de "parte pura infinita". El cuadrado del sitio de escala tiene **una parte infinita irreductible** (los ceros), de modo que **la maquinaria de AHK no es siquiera del tipo correcto**: AHK probaría signatura sobre un objeto finito; aquí la signatura relevante ($\kappa(Q)=2m$, Doc 119 = los cuádruplos off-críticos) es la del **bloque impuro finito** dentro de un $H^1$ infinito. AHK no tiene maquinaria para "signatura del bloque finito de un objeto infinito". [CONSTRUCCIÓN, coherencia con Doc 119 §2.4 + Doc 123 §6.2.]

**[CÁLCULO] Conclusión §2:** **AHK NO aplica.** De las cuatro hipótesis: (a) anillo de Chow — falta el producto (= G2); (b) PD — falta el grado tope y la no-degeneración (= G2); (c) clase amplia — candidato sintáctico $f_1+f_2$ sin noción intrínseca de amplitud; (d) **la infinitud + flujo continuo rompe la inducción finita de raíz** (α muere: sin caso base; δ muere: signatura no rígida en rango infinito). La obstrucción (d) es **no reparable** dentro del método AHK: AHK ES un método finito. Cualquier transplante requeriría una versión **infinito-dimensional / de "signatura relativa del bloque impuro"** del paquete de Kähler — matemática nueva, sin precedente, y exactamente el orden R-SIG ≺ R-FIN reapareciendo desde el lado del paquete de Kähler. **Tercera derivación independiente del mismo muro** (Doc 119 ingeniería inversa; Doc 123 construcción del cuadrado; aquí, AHK).

---

## 3. LA OBSTRUCCIÓN DE BABAEE–HUH [DATO + análisis]

### 3.1. Enunciado exacto del resultado

**[DATO]** (BH, arXiv:1502.00299v3, p.1–3, leído verbatim esta sesión.) El marco (Demailly):
- **(HC)** conjetura de Hodge clásica; **(HC′)** conjetura de Hodge para corrientes (Demailly: HC ⟺ HC′); **(HC⁺)** conjetura de Hodge para corrientes **fuertemente positivas**: toda corriente cerrada fuertemente positiva $(p,p)$ con clase de cohomología racional es límite débil $T=\lim_i\sum_j\lambda_{ij}[Z_{ij}]$ con $\lambda_{ij}\ge0$ **positivos** y $Z_{ij}$ subvariedades. Demailly probó **HC⁺ ⟹ HC**, y preguntó si HC′ ⟹ HC⁺ (Dem12, Remark 13.43). [DATO]

**[DATO] El contraejemplo — Theorem 1.1 (BH, p.3, verbatim):**
> *"There is a 4-dimensional smooth projective toric variety $X$ and a $(2,2)$-dimensional strongly positive closed current $\mathcal T$ on $X$ with the following properties: (1) The cohomology class of $\mathcal T$ satisfies $\{\mathcal T\}\in H^4(X,\mathbb Z)/\mathrm{tors}\cap H^{2,2}(X)$. (2) The current $\mathcal T$ is not a weak limit of the form $\lim_i\mathcal T_i$, $\mathcal T_i=\sum_j\lambda_{ij}[Z_{ij}]$, where $\lambda_{ij}$ are nonnegative real numbers and $Z_{ij}$ are algebraic surfaces in $X$."*

Es decir: **HC⁺ FALLA incluso sobre variedades tóricas donde HC vale**. La corriente $\mathcal T$ genera un **rayo extremal** del cono de corrientes fuertemente positivas cerradas (BH p.3). [DATO]

**[DATO] La frase decisiva (BH abstract, verbatim):** *"The counterexample is obtained from a tropical surface in $\mathbb R^4$ whose intersection form does not have the right signature in terms of the Hodge index theorem."*

### 3.2. Qué propiedad del índice de Hodge rompe — el mecanismo

**[DATO]** (BH, §1, p.4–5, leído verbatim.) La construcción:
- Una **corriente tropical** $\mathcal T_{\mathcal C}$ asociada a un **ciclo de abanico tropical balanceado** $\mathcal C$ de dimensión $p$ en $\mathbb R^n$ (un complejo poliédrico racional ponderado, con la **condición de balanceo**). Soporte $|\mathcal T_{\mathcal C}|=\mathrm{Log}^{-1}(\mathcal C)$. [DATO Def. 2.8, Thm 2.9]
- **Theorem 1.3:** un complejo ponderado $\mathcal C$ es balanceado ⟺ la corriente $\mathcal T_{\mathcal C}$ es cerrada. [DATO]
- **Theorem 1.5 (clave para el mecanismo):** la **clase de cohomología** de la extensión $\overline{\mathcal T}_{\mathcal C}$ en la tórica $X$ es la **recession** $\mathrm{rec}(\mathcal C)\in H^{q,q}(X)$ del abanico subyacente. [DATO]
- **§5:** la prueba del Theorem 1.1 analiza una **matriz Laplaciana** asociada a una superficie tropical 2-dimensional $\mathcal C$, vista como **grafo geométrico** $G=G(\mathcal C)\subseteq\mathbb R^n\setminus\{0\}$ con pesos de arista $w_{ij}$ que satisfacen la **condición de balanceo**: en cada vértice $u_i$ existe $d_i$ con $d_i u_i=\sum_{u_i\sim u_j}w_{ij}u_j$. [DATO]

**[CÁLCULO] El mecanismo de la obstrucción, con precisión.** La corriente $\mathcal T$ es fuertemente positiva (positividad tropical: los pesos $w_{ij}$ del complejo balanceado son positivos) y su clase es la recession. Para que $\mathcal T$ fuese límite de **ciclos algebraicos positivos**, su clase tendría que estar en el cono generado por superficies algebraicas; la obstrucción es que **la forma de intersección sobre las clases generadas por la superficie tropical no tiene la signatura del Hodge index theorem** (abstract). En términos del §1.1: una clase algebraica efectiva (de superficie) en el grado medio satisface las relaciones de Hodge–Riemann (índice de Hodge ⟹ signatura $(1,\rho-1)$, definida negativa en el primitivo); la clase tropical de $\mathcal T$ **viola** esa restricción de signatura, luego **no puede** ser límite positivo de clases algebraicas. La extremalidad (rayo extremal del cono) + la signatura equivocada = no aproximable. [CÁLCULO sobre DATO]

**[DATO] La frase del programa que ya lo anticipaba (WebSearch verificada):** *"the direct translation of the Hodge Index theorem fails for tropical surfaces"*. Es decir: **el índice de Hodge NO es gratis en el mundo tropical** — falla para superficies tropicales genéricas.

### 3.3. El criterio que separa AHK (índice vale) de BH (índice falla)

**[DATO — el criterio decisivo, BH p.5 verbatim].**
> *"There is an abundance of strongly extremal tropical varieties. For example, the Bergman fan of any simple matroid is a strongly extremal tropical variety [Huh14, Theorem 38]."*

Y (BH p.5): Demailly's primer ejemplo de corriente extremal no analítica **es** la corriente tropical asociada al matroide simple más simple (rango 2 en 3 elementos). [DATO]

**[CÁLCULO — el criterio, formulado].** El eje que separa los dos mundos es **matroidalidad / propiedad de Lefschetz**:
- **Lado AHK (índice VALE):** abanicos tropicales que son **abanicos de Bergman de matroides**. AHK (arXiv:1511.02888) probó que estos satisfacen el paquete de Kähler completo (PD+HL+HR), luego su forma de intersección en grado medio **tiene** la signatura correcta del índice de Hodge. Son "fuertemente extremales" pero **del lado bueno**: su signatura es la de una variedad proyectiva.
- **Lado BH (índice FALLA):** abanicos tropicales **balanceados pero NO matroidales** (genéricos). La superficie tropical en $\mathbb R^4$ del contraejemplo es balanceada (cerrada como corriente) pero su forma de intersección **no** satisface HR; **no** es matroidal; **no** satisface el paquete de Kähler.

**La condición de balanceo (positividad tropical / corriente fuertemente positiva) NO implica la condición de Hodge–Riemann.** Balanceo = cerrada y positiva; Hodge–Riemann = signatura correcta. BH muestra que la implicación "positivo tropical ⟹ algebraico (signatura correcta)" **es falsa en general**, y AHK muestra que **es verdadera para el subtipo matroidal**. El criterio que decide es: **¿es el abanico matroidal/Lefschetz, o sólo balanceado?**

### 3.4. ¿De qué lado cae el cuadrado del sitio de escala?

**[CONSTRUCCIÓN — la pregunta decisiva de §3.]** El cuadrado del sitio de escala $X\times X$ es un objeto tropical/característica 1 (Doc 123 §1.1: topos semi-anillado con haz de polígonos de Newton bidimensionales). Su "forma de intersección" (cuando exista, Doc 125) será una forma sobre el análogo de $\mathrm{NS}(X\times X)$ generada por clases tropicales $f_1, f_2, \Delta$, correspondencias $\Psi(\lambda)$.

- **¿Hay razón para que sea matroidal/Lefschetz?** **NO conocida.** [GAP/CONSTRUCCIÓN] El sitio de escala no proviene de un matroide; el flujo $\mathbb R_+^*$ no es la estructura de una red de flats. No hay teorema, ni candidato a teorema, que diga "el cuadrado del sitio de escala es de tipo Bergman/matroidal". La positividad que el corpus CC tiene (Doc 124: positividad de Weil, **definida**, sobre funciones test) es exactamente del tipo "balanceado/positivo" (positividad espectral), **no** del tipo "signatura $(1,\rho-1)$ correcta" (Hodge–Riemann).
- **El objeto es del tipo donde BH obstruye, salvo prueba en contra.** La forma de intersección del cuadrado es **precisamente** una "forma de intersección de una superficie tropical" — la clase de objetos donde BH demostró que la signatura **puede** fallar. Por defecto (sin un teorema de matroidalidad), **cae del lado obstruido**. [CÁLCULO]

**[CÁLCULO] Veredicto §3:** Babaee–Huh **OBSTRUYE genéricamente** la inferencia "positividad tropical ⟹ índice de Hodge", y el cuadrado del sitio de escala **no tiene credencial conocida para estar del lado AHK** (matroidal). Por tanto **no se puede suponer** que su forma de intersección tenga la signatura $(1,\rho-1)$: eso sería **asumir lo que hay que probar**, y BH muestra que en el mundo tropical genérico es **falso**. La única salida hacia (a) es probar que el cuadrado es del subtipo matroidal/Lefschetz — un teorema concebible pero hoy ausente. Esta es la diferencia crucial con cuerpos de funciones (§4.4), donde la superficie es algebraica genuina y el índice de Hodge es automático.

---

## 4. EL NÚCLEO IRREDUCIBLE [el deliverable central]

### 4.1. El enunciado exacto que daría G2

**[CONSTRUCCIÓN — el núcleo aislado].** Combinando §1.1 (índice de Hodge = HR en grado medio) y §3 (criterio matroidal/Lefschetz):

> **NÚCLEO-G2.** *El anillo de Chow tropical del cuadrado del sitio de escala $A^\bullet(X\times X)$ (cuando se construya, Doc 125) es un anillo graduado con dualidad de Poincaré, clase amplia $\ell=f_1+f_2$, que satisface las **relaciones de Hodge–Riemann en grado medio**: la forma de intersección $D\cdot D'$ sobre $A^1(X\times X)$ tiene **signatura $(1,\rho-1)$**, definida **negativa** sobre el primitivo $P^1=(f_1+f_2)^\perp$.*

De NÚCLEO-G2 se sigue G2 = la pureza exactamente como Weil: aplicado a la correspondencia gráfica del flujo $\Gamma_F$ y sus iterados/transpuestos, la definitud negativa sobre el primitivo fuerza la desigualdad de Cauchy–Schwarz (Castelnuovo) que da $\mathrm{Re}(\rho)=1/2$ (pureza de peso 1) — Doc 119 R-PESO(b-i); Doc 124 §1.2. **NÚCLEO-G2 ⟹ G2 ⟹ pureza ⟹ RH.** [SUPUESTO-DE-125: la existencia del anillo $A^\bullet$ con producto; aquí evalúo la **estrategia de probar la signatura**, no la construcción del anillo.]

### 4.2. R-NC aplicado a NÚCLEO-G2, con máximo rigor

Aplico el test de no-circularidad de Doc 119 §4.3. La pregunta crítica de toda la Phase 41 se decide **dentro de NC2 y NC3**.

**NC1 (externalidad de la definición).** La definición de $A^\bullet(X\times X)$, de la forma de intersección $D\cdot D'$, y de la clase amplia $f_1+f_2$ es **funtorial desde el sitio** (topos producto, polígonos de Newton): no menciona ζ ni sus ceros. **PASA** — igual que Castelnuovo (la forma de intersección de $C\times C$ no menciona qué curva es $C$). [CÁLCULO]

**NC2 (sobregeneración) — AQUÍ SE DECIDE EL VEREDICTO.** El discriminador (Doc 119 NC2; modelo Castelnuovo): ¿se prueba la signatura $(1,\rho-1)$ para **TODA** clase de $A^1(X\times X)$ / toda correspondencia, por un método uniforme que ignora ζ? Dos escenarios mutuamente excluyentes:
- **(NC2-A) La signatura es un teorema del anillo de Chow tropical, válido para toda clase.** Entonces sobregenera (vale para correspondencias generales, no sólo $\Gamma_F$), exactamente como AHK prueba HR para **todo** el grado medio del abanico de Bergman, no para una clase distinguida. **PASA NC2 con contenido.** Este es el camino (a).
- **(NC2-B) La signatura sólo puede establecerse evaluando la forma sobre las correspondencias de ζ.** Entonces NO sobregenera: $P$ es un enunciado sobre ζ con disfraz de superficie. **FALLA NC2.** Este es el camino (b).

**El estado actual cae en una zona donde NC2-B es lo único disponible**, por el resultado de §3.4: **no hay teorema que dé la signatura para toda clase** (eso requeriría matroidalidad/Lefschetz del cuadrado, ausente), y BH muestra que para una superficie tropical genérica la signatura **es falsa** para clases generales. Luego, hoy, la única manera concebible de "tener" la signatura sobre el primitivo es **postularla sobre las clases que importan** (las de ζ) — que es NC2-B.

**NC3 (no-reducción a positividades RH-equivalentes catalogadas) — el golpe.** La forma de intersección sobre el primitivo, **restringida a las correspondencias del flujo** $\Gamma_F$, evaluada como Weil la usa, **ES** la positividad de Weil. Doc 124 §2.5 ya estableció que la positividad de Weil global es **MW-1** del catálogo (= criterio de Weil = RH) y su uniformización semilocal **MW-6**. Por tanto:
> En el escenario NC2-B, $P|_{\text{correspondencias de }\zeta}$ = positividad de Weil = MW-1. **FALLA NC3 rotundamente.** Es la positividad-espectral del Doc 124 reapareciendo en lenguaje de superficies — exactamente lo que el cuantificador maestro P43 predice (Doc 119 §4.2: toda propiedad interna a ζ que implique pesos = 1/2 es RH-equivalente).
> En el escenario NC2-A, $P$ es una propiedad del anillo de Chow **independiente de ζ**; la cadena $P\Rightarrow$ pureza tiene a Castelnuovo como eslabón, que **no** figura en NO-GO-LIST (es un teorema de superficies). **PASARÍA NC3** — pero NC2-A requiere el teorema de matroidalidad ausente.

**NC4 (test de los dos mundos).** En el mundo ¬RH (un cuádruplo off-crítico), ¿$P$ es falsa por una razón computable desde $A^\bullet$ sin localizar el cero?
- **NC2-A:** sí — un autovalor de Frobenius/flujo con $\mathrm{Re}(\rho)\ne1/2$ produciría una clase con auto-intersección del signo prohibido sobre el primitivo, visible en la forma sin localizar el cero (modelo Castelnuovo, Doc 124 §1.2). **PASARÍA NC4.**
- **NC2-B:** no — para decidir si la forma de Weil es negativa hay que evaluar dónde están los ceros (Doc 124 §2.5; binariedad inaccesible Doc 108). **FALLA NC4.**

**[CÁLCULO] Resultado R-NC:** El veredicto es **enteramente condicional al escenario NC2**:
- Si la signatura es un **teorema geométrico del cuadrado para toda clase** (NC2-A): pasa NC1, NC2, NC3, NC4 ⟹ **no circular** ⟹ G2 alcanzable-en-principio.
- Si la signatura sólo se establece **sobre las correspondencias de ζ** (NC2-B): FALLA NC2, NC3, NC4 ⟹ **es la positividad de Weil renombrada** ⟹ circular.

**Y §3.4 muestra que hoy sólo NC2-B está disponible**, porque (i) no hay teorema de matroidalidad del cuadrado, y (ii) BH demuestra que para superficies tropicales genéricas la signatura es **falsa** para clases generales, de modo que un teorema NC2-A tendría que **excluir** el caso BH probando que el cuadrado es del subtipo bueno.

### 4.3. ¿Es NÚCLEO-G2 un teorema genuino o RH-equivalente disfrazado?

**[CÁLCULO — la respuesta brutalmente honesta].** El cuantificador maestro P43 (Doc 119 §4.2) **predice que reaparece**: toda propiedad verificable sin posiciones de ceros que implique RH debe provenir de una estructura **externa** a ζ; las internas son RH-equivalentes. La pregunta es si NÚCLEO-G2 es externo (geométrico genuino) o interno (Weil renombrado).

**Reaparece, salvo que el cuadrado sea genuinamente del tipo AHK.** El análisis de §3.4 + §4.2 muestra:
- NÚCLEO-G2 **en abstracto** (signatura para toda clase) es un teorema de paquete de Kähler tropical **genuino**, del tipo AHK — **externo**, sobregenera, no circular. Es un enunciado **concebible** (AHK probó algo análogo para matroides por métodos nuevos).
- NÚCLEO-G2 **para nuestro objeto concreto** sólo se vuelve probable-sin-circularidad **si** se demuestra que el cuadrado del sitio de escala es del subtipo matroidal/Lefschetz. **Sin ese teorema intermedio**, la única forma de "tener" la signatura es sobre las correspondencias de ζ = positividad de Weil = circular.

**Por tanto el núcleo irreducible se desplaza un nivel:** no es "probar la signatura", sino **probar que el cuadrado del sitio de escala es del subtipo donde el índice de Hodge vale (matroidal/Lefschetz tropical), y NO del subtipo BH donde falla**. ESE es el enunciado irreducible. Y es el que decide entre (a) y (b):
- si ese subtipo-teorema es **externo** (una propiedad del sitio independiente de ζ, que sobregenera) ⟹ (a) alcanzable;
- si la única evidencia de que el cuadrado está del lado bueno es que "la forma de Weil es positiva" ⟹ (b) circular, porque la forma de Weil positiva ES RH.

### 4.4. Dónde se rompe / se sostiene la analogía con cuerpos de funciones

**[CÁLCULO — la localización exacta, el corazón del encargo].**

**En cuerpos de funciones (donde funcionó), Castelnuovo NO es circular porque:**
1. $C\times C$ es una **variedad algebraica proyectiva lisa genuina** sobre $\mathbb F_q$. [DATO clásico]
2. Tiene **teoría de intersección de Grothendieck** completa: $\mathrm{NS}(C\times C)$, forma de intersección $D\cdot D'$, clase fundamental, dualidad de Poincaré — todo **dado por la geometría algebraica**, anterior y ajeno a ζ. [DATO]
3. El **índice de Hodge para superficies** (signatura $(1,\rho-1)$) es un **teorema clásico** (Hodge; Segre; Grothendieck *Sur une note de Mattuck–Tate* 1958), válido para **toda** superficie proyectiva, demostrado **sin** mención de funciones L. Es **NC2-A automático**: el índice vale para toda clase, por geometría. [DATO]
4. La superficie es del **subtipo AHK** de manera automática: las superficies proyectivas lisas **siempre** satisfacen el índice de Hodge (es el teorema clásico); no hay análogo del fracaso BH en el mundo algebraico genuino. **El caso BH no puede ocurrir para una superficie algebraica proyectiva** — sólo para superficies **tropicales** que no provienen de una variedad.

**En Spec ℤ (donde no sabemos), la analogía se ROMPE en exactamente el punto (3)–(4):**
- El "cuadrado" es **tropical/característica 1** (topos semi-anillado, polígonos de Newton), **no una variedad algebraica genuina**. [DATO Doc 123 §1.1]
- Su teoría de intersección **es justamente lo que falta** (Doc 123 §6.2: la norma de intersección = (C-rank) = G2 no existe en el corpus; CC la declaran *in development*). [DATO]
- El índice de Hodge **NO es automático**: BH demuestra que para superficies tropicales el índice de Hodge **puede fallar** (la signatura puede ser la equivocada). El paso (3)–(4) de cuerpos de funciones —"toda superficie satisface el índice"— **no tiene análogo tropical**: en tropical sólo el subtipo matroidal/Lefschetz lo satisface. [DATO §3]

**La analogía se sostiene en (1)–(2) sólo parcialmente** (hay un candidato a $\mathrm{NS}$ y a forma, vía Doc 125), pero **se rompe en (3)–(4)**: el teorema que en cuerpos de funciones es gratis (índice de Hodge para toda superficie) es en el mundo tropical **falso en general** (BH) y **abierto en particular** (¿es el cuadrado del subtipo bueno?). **Ese es el punto exacto de ruptura:** la geometría algebraica genuina da el índice de Hodge para toda superficie; la geometría tropical lo da sólo para el subtipo matroidal, y el cuadrado del sitio de escala no tiene credencial de pertenecer a ese subtipo. La diferencia $\mathbb Z$ vs $\mathbb R$ (flujo discreto vs continuo, Doc 119 T4) reaparece aquí como diferencia "algebraico vs tropical / Lefschetz automático vs Lefschetz a probar".

---

## 5. VEREDICTO

### 5.1. Clasificación (a)/(b)/(c)/(d)

**[CÁLCULO] Veredicto: (d) indeterminable hoy, con sesgo estructural fuerte hacia (b)/(c), y un único camino estrecho y concebible hacia (a).** Desglose por subpregunta:

- **¿Aplica AHK?** **NO** (§2). La infinitud + flujo continuo rompe la inducción finita de raíz (sin caso base; signatura no rígida en rango infinito); falta el anillo de Chow con producto (=G2), la PD-AHK (grado tope + no-degeneración = G2), y la noción intrínseca de amplitud. Tercera derivación independiente del mismo muro (R-SIG ≺ R-FIN).

- **¿Obstruye Babaee–Huh?** **SÍ, genéricamente** (§3). BH demuestra que "positividad tropical ⟹ índice de Hodge" es **falso en general** para superficies tropicales (signatura equivocada). El cuadrado del sitio de escala **no tiene credencial conocida de matroidalidad/Lefschetz**, luego cae por defecto del lado obstruido. La positividad que el corpus tiene (Weil, definida, espectral, Doc 124) es del tipo "balanceado", no del tipo "Hodge–Riemann".

- **El núcleo irreducible exacto** (§4.3): **NO** es "probar la signatura $(1,\rho-1)$"; es **"probar que el cuadrado del sitio de escala es del subtipo matroidal/Lefschetz tropical donde el índice de Hodge vale (y NO del subtipo Babaee–Huh donde falla), por una propiedad externa a ζ que sobregenera"**. Si ese subtipo-teorema existe y es externo ⟹ (a); si la única evidencia de estar del lado bueno es la positividad de Weil ⟹ (b) circular.

- **Veredicto R-NC** (§4.2): condicional al escenario NC2. **NC2-A** (signatura para toda clase, geométrica) ⟹ pasa todo ⟹ no circular. **NC2-B** (signatura sólo sobre correspondencias de ζ) ⟹ FALLA NC2/NC3/NC4 ⟹ **la positividad sobre el primitivo = positividad de Weil = RH-circular**. **Hoy sólo NC2-B está disponible** ⟹ el estado actual es **(b) circular**, y (a) requiere el subtipo-teorema ausente.

### 5.2. ¿El índice sobre el primitivo es geométrico genuino o positividad de Weil RH-circular?

**[CÁLCULO — la respuesta directa que el encargo exige].** **Hoy: RH-circular (positividad de Weil disfrazada).** Sin un teorema que establezca la signatura **para toda clase del anillo de Chow** (NC2-A, = el subtipo matroidal/Lefschetz), la única forma de afirmar "la forma es negativa sobre el primitivo" es restringirla a las correspondencias de ζ y constatar que la forma de Weil es positiva — que **es** RH (MW-1). El cuantificador maestro P43 reaparece **acá**, como predijo, porque no hay (todavía) marco geométrico genuino que lo evada: a diferencia de cuerpos de funciones, donde la geometría algebraica da el índice para toda superficie gratis, aquí el "cuadrado" es tropical y su índice de Hodge **no es gratis** (BH) y **no está construido** (Doc 123).

**El marco geométrico genuinamente lo evadiría SÓLO SI** se prueba —externamente a ζ, por matemática combinatoria/tropical nueva del tipo AHK— que el cuadrado del sitio de escala es del subtipo donde el paquete de Kähler vale. Eso es **concebible** (AHK es el precedente) pero hoy **ausente**, y obstruido por la dimensión infinita / flujo continuo (§2.4) que ningún teorema de tipo AHK existente cubre.

### 5.3. Consecuencia para el programa y lista de lo que faltaría

**[CONSTRUCCIÓN] Consecuencia:** Phase 41 ("CONSTRUIR G2") tiene un objetivo bien definido pero un **núcleo irreducible que se ha desplazado**: no es construir la forma (Doc 125) ni probar su signatura directamente, sino **probar que el objeto es del subtipo Kähler-package tropical** — y ese teorema, si existe, debe ser **externo** (NC2-A) para no ser circular. El estado actual (NC2-B) es honestamente **circular**: coincide con Doc 124 (positividad de Weil = espectral = circular), Doc 123 (la norma de intersección = G2, ausente), y Doc 80 (Castelnuovo–Severi aritmético: la forma que distingue las medidas es RH-equivalente). **Cuatro derivaciones independientes, mismo veredicto.**

**Lista de lo que faltaría (para mover de (b)/(d) hacia (a)):**

1. **[GAP — Doc 125] La forma de intersección como objeto:** un anillo de Chow tropical $A^\bullet(X\times X)$ con producto graduado, grado tope $\cong\mathbb R$, PD no degenerada. Es el prerrequisito de todo (sin él HR ni se enuncia). Lo construye Doc 125.

2. **[GAP CONCEPTUAL — el núcleo real] Un "teorema de matroidalidad/Lefschetz tropical" para el cuadrado:** un enunciado, externo a ζ, de que el cuadrado del sitio de escala satisface las relaciones de Hodge–Riemann **para toda clase** (no sólo las de ζ). Debe **excluir explícitamente** el caso BH (probar que la signatura es la correcta, no la equivocada). Es matemática nueva, sin precedente para objetos infinito-dimensionales con flujo continuo.

3. **[GAP — el más duro, §2.4] Una versión infinito-dimensional del paquete de Kähler** que dé "signatura del bloque impuro finito dentro de un $H^1$ infinito" (R-SIG ≺ R-FIN). AHK es finito; aquí la parte pura es infinita. Ningún teorema de tipo AHK cubre esto. Es la obstrucción central, y coincide con T1/T2 de Doc 119.

4. **[VERIFICACIÓN] El criterio matroidal sobre el sitio:** ¿existe alguna estructura de red de flats / submodularidad natural sobre el sitio de escala que lo haga matroidal? Si NO (lo probable), el cuadrado cae del lado BH y G2 está **obstruido** (veredicto (c)), no sólo indeterminado. Decidir esto es el experimento más informativo de Phase 41.

5. **[CONSULTA a CC] El estado de la "intersection theory of divisors on the square of the Scaling Site" (declarada *in development*, 2006.13771):** si su forma de intersección se define como **límite regularizado**, la tensión T2 (signaturas no sobreviven límites sin gap) ataca exactamente ahí — y BH es la advertencia de que la signatura puede salir equivocada.

---

## 6. Síntesis y honestidad

Ningún teorema geométrico nuevo se ha probado aquí. Se ha **leído en fuente** (AHK arXiv:1511.02888 + surveys Eur–Larson y arXiv:2211.05724; Babaee–Huh arXiv:1502.00299 verbatim Thm 1.1, 1.3, 1.5, Huh14 Thm 38 vía BH) y se ha **calculado**:

- **AHK NO aplica** al cuadrado del sitio de escala: el método es una **inducción finita poliédrica** (red de flats finita, deformación de clase amplia en cono finito-dimensional conexo, rigidez de signatura en rango finito); el sitio es **infinito-dimensional con flujo continuo**, lo que mata la inducción de raíz. Faltan además el anillo de Chow (producto = G2) y la PD-AHK.
- **Babaee–Huh OBSTRUYE genéricamente:** "positividad tropical ⟹ índice de Hodge" es **falso** para superficies tropicales (signatura equivocada). El criterio que separa el lado bueno (AHK) del malo (BH) es **matroidalidad/Lefschetz**; el cuadrado del sitio de escala **no tiene credencial de matroidalidad**, luego cae por defecto del lado obstruido.
- **El núcleo irreducible** no es "probar la signatura" sino "**probar que el cuadrado es del subtipo Kähler-package tropical donde el índice vale, por una propiedad externa a ζ que sobregenera**". Sometido a R-NC: si ese teorema es externo (NC2-A) ⟹ no circular ⟹ (a); si la signatura sólo se tiene sobre las correspondencias de ζ (NC2-B) ⟹ **es la positividad de Weil = RH = circular**.
- **Hoy sólo NC2-B está disponible** ⟹ el índice sobre el primitivo es, en el estado actual, **positividad de Weil RH-circular** (coincidente con Docs 124, 123, 80 — cuatro derivaciones).
- **La analogía con cuerpos de funciones se rompe en el punto (3)–(4) de §4.4:** allá la geometría algebraica genuina da el índice de Hodge para **toda** superficie gratis (Castelnuovo no circular, NC2-A automático); acá el cuadrado es **tropical**, su índice **no es gratis** (BH lo puede romper) y **no está construido**. El cuantificador maestro P43 reaparece exactamente donde la geometría deja de ser genuina y se vuelve tropical-sin-índice-garantizado.

**El punto de traba ES el resultado:** G2 no está obstruido de manera demostrada (no se ha probado que el cuadrado sea del lado BH), pero **no hay credencial de que esté del lado AHK**, y la dimensión infinita rompe el único método (AHK) que prueba paquetes de Kähler combinatoriamente. El veredicto honesto es **(d) indeterminable, con el estado actual en (b) circular**, y el camino a (a) pasando por dos teoremas hoy ausentes: la forma de intersección (Doc 125) y, sobre ella, un teorema externo de matroidalidad/Lefschetz tropical infinito-dimensional que excluya el caso Babaee–Huh.

---

## Referencias

**Fuente primaria leída esta sesión (junio 2026, vía WebFetch/WebSearch sobre arXiv y surveys, y Read sobre el PDF de BH):**
- K. Adiprasito, J. Huh, E. Katz, *Hodge theory for combinatorial geometries*, arXiv:1511.02888; Annals of Math. 188 (2018) 381–452 — paquete de Kähler (PD+HL+HR) para el anillo de Chow de un matroide; prueba por inducción simultánea sin geometría algebraica; resolución de Heron–Rota–Welsh y Mason–Welsh. **[DATO vía abstract + surveys]**
- C. Eur, M. Larson, *Combinatorial Hodge theory* (survey), Notices AMS, marzo 2025 — estructura de $A^\bullet(M)$, graduación $0..r-1$, PD, clase amplia, inducción simultánea, signatura indefinida en grado medio, finitud esencial (rango finito, abanico simplicial finito). **[DATO]**
- *Essence of independence: Hodge theory of matroids since June Huh* (survey), arXiv:2211.05724 — confirma estructura del anillo de Chow e inducción simultánea de las tres propiedades. **[DATO]**
- F. Babaee, J. Huh, *A tropical approach to a generalized Hodge conjecture for positive currents*, arXiv:1502.00299v3 (22 Mar 2017); Duke Math. J. 166 (2017) — Abstract ("tropical surface in $\mathbb R^4$ whose intersection form does not have the right signature in terms of the Hodge index theorem"); HC/HC′/HC⁺ y Demailly Dem82/Dem12; **Theorem 1.1** (4-fold tórica + corriente $(2,2)$ fuertemente positiva no aproximable, rayo extremal); Theorem 1.3 (balanceado ⟺ cerrado); **Theorem 1.5** (clase = recession); §5 (matriz Laplaciana de superficie tropical 2-dim, condición de balanceo $d_i u_i=\sum w_{ij}u_j$); **Huh14 Thm 38** (abanico de Bergman de matroide simple = fuertemente extremal; Demailly's primer ejemplo extremal = matroide rango 2 en 3 elementos). **[DATO verbatim, pp.1–5]**

**Internas (backward-only):** Doc 124 (positividad-intersección [BUENA] vs positividad-espectral [CIRCULAR]; positividad de Weil = MW-1/MW-6; la forma de CC es definida no indefinida; §1.1 índice de Hodge clásico, §1.2 cómo Weil usa Castelnuovo, §2.5 R-NC sobre CC); Doc 123 (bifurcación (C-cok)/(C-rank); $H^1_{\mathrm{tol}}$ condicional A1–A3; §6.2 la norma de intersección = G2 ausente; "la parte numérica de G1 y G2 son el mismo objeto"; §4.1 $C_p$ sin $H^1$; Künneth tropical no existe); Doc 119 (R-SIG/R-FIN/R-LEF/R-PESO/R-NC NC1–NC4; orden R-SIG ≺ R-FIN; §2.3 realizaciones (i)/(ii)/(iii); §4.2 cuantificador maestro P43; tensiones T1, T2, T4; §6.1 tabla, fila R-PESO(b) Castelnuovo / Deligne); Doc 80 (Castelnuovo–Severi aritmético; Prop. 8.1; Paso A/Paso B de Weil; la diferencia de medidas RH-equivalente); Doc 120/122 (dualidad de Pontryagin sin simetría; intersection theory *in development*); roadmap-rh (G1–G4, S1–S3); P35 (κ(Q)=2m); P43/P44 (cuantificador maestro).

**Clásica (contexto, no re-verificada en fuente esta sesión):** índice de Hodge para superficies proyectivas (signatura $(1,\rho-1)$); Grothendieck, *Sur une note de Mattuck–Tate*, J. reine angew. Math. 200 (1958); Weil 1948 (Castelnuovo–Severi en $\mathrm{NS}(C\times C)$); Demailly (HC para corrientes positivas, Dem82/Dem12).

*Fin del Doc 126.*
