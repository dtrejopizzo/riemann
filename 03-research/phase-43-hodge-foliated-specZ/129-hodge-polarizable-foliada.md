# Doc 129 — ¿Admite el espacio foliado de Spec ℤ una estructura de Hodge polarizable foliada?

**Programa:** Hipótesis de Riemann — Phase 43: matemática nueva — la estructura compleja de las hojas.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 128 (el programa de Deninger; veredicto (a) no circular *condicional a Kähler–Riemann*; math/0204111 es el teorema de positividad-derivada; Morishita 2508.15971 da el espacio+flujo pero NO la cohomología; la rigidez espectral 1712.04181; el objeto-meta unificado); Doc 127 (por qué la ruta dinámica/Forni es circular: la positividad debe venir de las HOJAS, no del flujo; el flujo de escala "lleva ζ adentro"); Doc 125 (el juguete $C_p\times C_p$, matriz de Gram $G_{\text{toy}}$ signatura $(1,2)$, primitivo definido negativo; G-125.A real/entero; G-125.B persistencia de signatura à la Babaee–Huh).

**Disciplina de etiquetado (regla absoluta, máximo riesgo de falsa victoria):** **[DATO]** = leído en fuente esta sesión (arXiv, cita exacta) o teorema interno backward-only. **[CONSTRUCCIÓN]** = objeto que diseño, con estatus condicional. **[CÁLCULO]** = derivación mía. **[GAP]** = lo que falta, con precisión. **[CONJETURA]** = lo que propongo. **[NO VERIFICADO]**. NUNCA "probado" salvo lo genuino. **El objetivo NO es probar que la estructura existe — es determinar SI puede existir, construir lo construible, y aislar el núcleo + el test de circularidad.** Si la estructura compleja necesaria resulta ser ζ metida a mano, ese es el resultado (lo dictamina el Doc 130 en paralelo; aquí, el pre-test).

---

## 0. Resumen ejecutivo

El veredicto del Doc 128 fue: el programa de Deninger es el primer marco *no circular* (la positividad-RH es un teorema de Hodge a lo largo de las hojas, math/0204111, no la positividad de Weil renombrada), **condicionado a que el espacio sea de tipo Kähler–Riemann**. Este documento ataca la condición frontalmente: ¿el espacio foliado de Spec ℤ (en la única encarnación que hoy existe como objeto, la de Morishita) **tiene hojas que sean variedades complejas Kähler**, como math/0204111 EXIGE? Y si las tuviera, ¿de qué **dimensión compleja**, y cierra esa dimensión con el cuadrado de Doc 125 (la forma de intersección de signatura $(1,2)$)?

**Hallazgos centrales:**

1. **Lo que prueba math/0204111 (§1) [DATO].** Para una **foliación Kähler–Riemann** —foliación cuyas hojas son **variedades complejas que portan, hoja a hoja, una métrica Kähler**, con la estructura compleja $J$ sobre $T\mathcal F$ integrable en cada hoja y variando suavemente en la dirección transversa, *más* una métrica transversa que la hace foliación Riemanniana (bundle-like)— Deninger–Singhof prueban: (i) **Hard Lefschetz foliado** $L^{g-r}:\bar H^r_{\mathcal F}\xrightarrow{\sim}\bar H^{2g-r}_{\mathcal F}$ (Prop. 4.3), donde $g=\dim_{\mathbb C}$ de la hoja; (ii) **estructura de Hodge real polarizable** de peso $r$ sobre el primitivo $P^r_{\mathcal F}$ (Prop. 4.4); (iii) la **positividad de Hodge–Riemann** $Q(\xi,J\bar\xi)>0$ para $\xi\ne0$. La **fuente** de la positividad es EXACTAMENTE la polarización de Hodge clásica de una variedad Kähler compacta, transportada hoja a hoja vía la descomposición de Hodge suave de Álvarez López–Kordyukov (las clases de $\bar H^\bullet_{\mathcal F}$ = formas globales suaves armónicas a lo largo de las hojas; el producto $L^2$ hoja-a-hoja es definido positivo). **La estructura compleja Kähler de las hojas NO es opcional: es la hipótesis que enciende todo.** [DATO, verbatim §1.3]

2. **El espacio de Morishita (§2) [DATO].** Morishita 2508.15971 construye el sistema dinámico foliado de Deninger $\mathfrak X_K=\check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+$. Estructura **verificada en fuente HTML**: el transversal $\check X_K(\mathbb C)$ es **totalmente disconexo (profinito, dimensión 0)** — un límite inductivo de conjuntos de pares $(\mathfrak p,P)$ con $P\in\mathrm{Hom}(W_{\mathrm{rat}}(\kappa(\mathfrak p)),\mathbb C)$; las **hojas** son las imágenes de $\check X_K(\mathbb C)\times\{u\}$, y la única dirección con dimensión genuina es la **del flujo $\mathbb R_+$** (1-dim). Las **órbitas cerradas** del flujo (los primos) son círculos $\gamma_{\mathfrak p}$ de longitud $\log N\mathfrak p$. **CRÍTICO: el paper afirma que NO hay estructura compleja ni Kähler en ninguna parte; todas las estructuras son reales, y la dirección "geométrica" es la del flujo, con transversal profinito de dimensión 0.** [DATO, verbatim §2]

3. **El primer punto de quiebre: las hojas de Morishita NO son variedades complejas (§2.4) [DATO + CÁLCULO].** En $\mathfrak X_K$, la "hoja" es un objeto cuya única dirección continua es el flujo $\mathbb R_+$ (con transversal profinito de dim 0). **No es una variedad compleja de ninguna dimensión** — es un solenoide/lámina 1-dimensional real (la dirección de escala) sobre un Cantor aritmético. La hipótesis central de math/0204111 (hojas Kähler de dim_ℂ $g\ge1$) **FALLA literalmente** en el espacio que hoy existe. La Hodge foliada de Deninger **no aplica al espacio de Morishita tal como está construido.** Este es el primer veredicto firme: **(c) las hojas no tienen estructura compleja.** [CÁLCULO sobre DATO]

4. **El mismatch dimensional, con precisión (§3) — el corazón [CÁLCULO + GAP].** Para que la forma de intersección del cuadrado de Doc 125 (signatura $(1,2)$, primitivo definido negativo) sea la polarización de Hodge–Riemann de math/0204111, hace falta que el apareamiento viva en el **grado medio** de una hoja Kähler de **dimensión compleja $g=2$ (una superficie compleja)**: allí $\bar H^2_{\mathcal F}=\bar H^{1,1}_{\mathcal F}\oplus(\text{partes }2,0\ y\ 0,2)$, y la polarización sobre $P^2_{\mathcal F}\cap H^{1,1}$ tiene la signatura del índice de Hodge $(1,h^{1,1}-1)$ — exactamente $(1,2)$ si $h^{1,1}_{\text{prim}}+1=3$. **Pero el espacio existente (Morishita) tiene hojas de dim_ℂ $0$, y el espacio del ejemplo simple de Deninger (math/0204194) tiene hojas $\mathcal F_{\mathcal L}$ de dim_ℂ $1$ (curvas/superficies de Riemann), no superficies.** **La dimensión NO cierra por dos vías a la vez:** (i) Morishita: dim_ℂ hoja $=0$, ni siquiera hay Hodge; (ii) el caso geométrico realizado (curva elíptica): dim_ℂ hoja $=1$, da el índice de Hodge de una *curva* ($H^1$, signatura simpléctica $(g,g)$), no el índice de Hodge de una *superficie* ($H^2$, signatura $(1,\rho-1)$) que es lo que el cuadrado necesita. **El cuadrado $C_p\times C_p$ es bidimensional (una superficie); la hoja de Deninger es 1-dimensional (una curva o menos). Mismatch de dimensión $2$ vs $\le1$.** [CÁLCULO — éste es el núcleo, §3]

5. **El veredicto (§7): (b)/(c) — la dimensión NO cierra Y las hojas (en el espacio existente) no son complejas.** No es (a): el espacio de Morishita no admite la Hodge foliada de Deninger porque sus hojas son reales de dim 0. Aun *suponiendo* que se construyera un espacio con hojas complejas (como en el ejemplo simple), la dimensión de la hoja sería $1$ (curva), y el objeto que da la signatura $(1,2)$ del cuadrado vive en el $H^2$ de una **superficie** (dim 2). **El cuadrado del sitio de escala NO corresponde a una hoja del espacio de Deninger, sino al producto de dos copias del espacio total** (§5) — y el producto de dos espacios foliados de dimensión 1 (flujo) sobre transversales profinitos NO es una variedad Kähler de dim_ℂ 2; es un objeto laminado de dimensión real 2 (dos flujos) sobre un transversal profinito, sin estructura compleja. **El mismatch es estructural y doble: dimensión (curva vs superficie) y naturaleza (real-laminado vs Kähler).**

6. **El pre-test de circularidad (§6) [CONJETURA].** Si, *forzando*, se quisiera dotar a las hojas de Morishita de una estructura compleja de dim_ℂ adecuada para que la polarización dé $(1,2)$, **¿de dónde saldría esa estructura compleja?** En el caso geométrico (curva elíptica / cuerpos de funciones) la estructura compleja de las hojas viene de la **geometría externa** (la superficie de Riemann subyacente $X(\mathbb C)$ que ya existe). Para Spec ℤ NO hay tal superficie de Riemann ambiente — el lugar arquimediano da un único punto, no una curva compleja. La única manera conocida de "fabricar" una variación de estructura de Hodge con los autovalores correctos sería **inyectar los ceros de ζ como periodos** — exactamente la inyección circular que el Doc 130 debe diagnosticar a fondo. **Lectura preliminar [CONJETURA]: la estructura compleja necesaria NO es externa (no hay geometría arquimediana que la provea para Spec ℤ); su candidata es ζ metida a mano. Veredicto fino al Doc 130.**

---

## 1. EL TEOREMA DE POSITIVIDAD-DERIVADA: math/0204111 [DATO, fijado con máxima precisión]

### 1.1. Las hipótesis: qué estructura debe tener el espacio foliado

**[DATO — definición verbatim, vía ar5iv de math/0204111 (Deninger–Singhof, *Real polarizable Hodge structures arising from foliations*)].**

La estructura de partida es una **foliación Kähler** y, además, **Riemanniana**:

> "A Kähler foliation $(X,\mathcal F,h=S-2i\omega_{\mathcal F})$ which is also a Riemannian foliation is called a **Kähler–Riemann foliation**."

Desglose de las hipótesis (cada una es necesaria):

- **(H1) Las hojas son variedades complejas Kähler.** La foliación $\mathcal F$ porta una **estructura compleja**: una estructura casi-compleja $J$ sobre el fibrado tangente a las hojas $T\mathcal F$ tal que **toda restricción $J|_{\text{hoja}}$ es integrable** — luego **cada hoja es una variedad compleja**, y estas estructuras holomorfas **varían suavemente en la dirección transversa** [DATO, confirmado por WebSearch: *"A complex structure on a foliation F is an almost complex structure J on TF such that all restrictions J|F to the leaves are integrable. Then the leaves carry holomorphic structures which vary smoothly in the transverse direction."*]. La hoja tiene **dimensión real $2g$ = dimensión compleja $g$**, con $g=\dim_{\mathbb C}$ de la hoja. La forma de Kähler hoja-a-hoja $\omega_{\mathcal F}$ satisface $d_{\mathcal F}\omega_{\mathcal F}=0$ (cerrada *a lo largo de las hojas*).

- **(H2) Métrica transversa Riemanniana (foliación Riemanniana / bundle-like).** El plano normal a las hojas porta una métrica que hace la foliación Riemanniana (bundle-like); esto es lo que permite la **descomposición de Hodge suave** y que la cohomología foliada reducida sea manejable. [DATO]

- **(H3) Codimensión y orientación transversa.** La dirección transversa está orientada y con métrica complementaria. En el caso aritmético, la codimensión "geométrica" la juega el flujo $\mathbb R$ (codim 1 transversal al cual están las hojas). [DATO]

**[CÁLCULO — el punto que retengo para todo el documento].** La hipótesis H1 es **inflexible**: *las hojas deben ser variedades complejas, de una dimensión compleja $g\ge1$ definida.* Sin estructura compleja en las hojas no hay descomposición de Hodge $H^{1,0}\oplus H^{0,1}$, no hay operador $J$, no hay forma $Q(\cdot,J\bar\cdot)$, no hay polarización. **Todo el teorema cuelga de que las hojas sean Kähler.**

### 1.2. La conclusión: Hard Lefschetz + Hodge–Riemann + positividad

**[DATO — enunciados verbatim].**

- **Hard Lefschetz foliado (Prop. 4.3).** Para $r<g$:
$$ L^{g-r}:\ \bar H^r_{\mathcal F}(X,\mathbb C)\ \xrightarrow{\ \sim\ }\ \bar H^{2g-r}_{\mathcal F}(X,\mathbb C), $$
isomorfismo, donde $L=\wedge\,[\omega_{\mathcal F}]$ es el operador de Lefschetz (cup con la clase de Kähler foliada) y $g=\dim_{\mathbb C}$ de la hoja. **El $g$ que aparece en el exponente $L^{g-r}$ es la dimensión compleja de la hoja.** [DATO]

- **Estructura de Hodge polarizable (Prop. 4.4).** "$Q$ defines a polarization of weight $r$ of the real Hodge structure $P^r_{\mathcal F}(X)$", con la descomposición de Lefschetz $\bar H^r_{\mathcal F}(X,\mathbb C)=\bigoplus_s L^s(P^{r-2s}_{\mathcal F}(X))$ en partes primitivas. [DATO]

- **Positividad de Hodge–Riemann (de §3.3).** La forma bilineal cumple
$$ Q(\xi,J\bar\xi)>0\quad\text{para }\xi\ne0 $$
sobre el primitivo. [DATO]

- **Análogo Kähleriano de Serre de las conjeturas de Weil** se traslada. [DATO]

### 1.3. DE DÓNDE sale la positividad — el origen exacto (la fuente "externa")

**[DATO — el quicio].** La positividad descansa en la **descomposición de Hodge suave de Álvarez López–Kordyukov** (ref. [1] del paper):

> "the smooth Hodge decomposition theorem of Álvarez López and Kordyukov ... expresses $\bar H^r_{\mathcal F}(X)$ as the space of smooth global forms on $X$ along $\mathcal F$ whose restrictions to the leaves are harmonic"

y la descomposición $\mathcal A^\bullet_{\mathcal F}(X)=\mathcal H^\bullet_{\mathcal F}(X)\oplus\mathrm{im}\,d_{\mathcal F}\oplus\mathrm{im}\,d^*_{\mathcal F}$, con $\bar H^\bullet_{\mathcal F}(X,\mathbb C)\cong\mathcal H^\bullet_{\mathcal F}(X)$ como espacios de Fréchet.

**[CÁLCULO] El mecanismo de la positividad, paso a paso.** Las clases de $\bar H^r_{\mathcal F}$ se representan por formas **armónicas a lo largo de cada hoja**. Cada hoja es una variedad **Kähler compacta** (o con la analiticidad/completitud necesaria), y sobre una variedad Kähler compacta la teoría de Hodge clásica da: las relaciones bilineales de Hodge–Riemann, es decir, que la forma $Q(\xi,J\bar\xi)=\int_{\text{hoja}}\xi\wedge\overline{*\,\xi}$ (con los signos de Weil) es **definida positiva sobre las formas primitivas armónicas**. Esta positividad es la **polarización de Hodge de la hoja Kähler**, integrada hoja-a-hoja contra la medida transversa invariante. **La fuente de la positividad es, literalmente, la polarización de Hodge clásica de una variedad Kähler compacta — la misma que da el índice de Hodge en geometría algebraica — aplicada en cada hoja y promediada transversalmente.** [DATO + CÁLCULO]

**[CÁLCULO — la implicación que lo hace no circular (recordatorio de Doc 128 §3).** La positividad **no se postula**: se **deriva** de que las hojas sean Kähler. Es geométrica, vale para *toda* clase primitiva, ignora dónde están los ceros de ζ. Pasa NC1/NC2/NC4. **Pero la hipótesis H1 (hojas Kähler) es donde se concentra todo el contenido:** la no-circularidad de Deninger ES la afirmación "construir el espacio Kähler ⟹ positividad", y el precio es construir un espacio con hojas Kähler de la dimensión correcta. **Este documento testea precisamente si ese espacio existe / puede existir para Spec ℤ.**

---

## 2. EL ESPACIO DE MORISHITA: 2508.15971 [DATO]

### 2.1. Qué espacio construye exactamente

**[DATO — vía HTML arxiv.org/html/2508.15971].** Para un cuerpo de números $K$ (en el resultado principal, abeliano), Morishita construye el **sistema dinámico foliado de Deninger**:
$$ \mathfrak X_K\ :=\ \check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+, $$
el cociente de $\check X_K(\mathbb C)\times\mathbb R_+$ por la acción a derecha de $\mathbb Q_+$.

- **El transversal $\check X_K(\mathbb C)$.** Es un **límite inductivo** $\check X_K(\mathbb C)=\varinjlim_{n}\dot X_K(\mathbb C)$, donde cada $\dot X_K(\mathbb C)$ son pares $(\mathfrak p,P)$ con $\mathfrak p\in X_K$ (un primo) y $P\in\mathrm{Hom}(W_{\mathrm{rat}}(\kappa(\mathfrak p)),\mathbb C)$. **$\check X_K(\mathbb C)$ es totalmente disconexo (profinito, dimensión topológica 0)**, con la topología de convergencia puntual. [DATO verbatim]

- **El flujo (Frobenius $\mathbb R_+$-flow).** $\phi^t([(\mathfrak p,P),u]):=[(\mathfrak p,P),tu]$ — el flujo de escala. [DATO]

- **Las hojas.** "taking the images of $\check X_K(\mathbb C)\times\{u\}$ ($u\in\mathbb R_+$) as leaves" — foliación de **codimensión 1**, transversal al flujo. [DATO]

- **Las órbitas cerradas (los primos).** Para $\mathfrak p$ sobre $p$: $\gamma_{\mathfrak p}$ es un **círculo de longitud $\log N\mathfrak p$** (órbita $\mathbb R_+$ cerrada); el paquete $\Gamma_{\mathfrak p}$ es el toro de aplicación (mapping torus) de la multiplicación por $\mathrm{lk}_p$ en $\hat{\mathbb Z}^\times_{(p)}$ (Thm 2.2.8). [DATO]

### 2.2. La dimensión y la naturaleza de las hojas — el dato decisivo

**[DATO — verbatim de la fuente].** "There is **no complex or Kähler structure** on leaves anywhere in this paper. All structures are real." La dirección con dimensión genuina es **la del flujo $\mathbb R_+$ (1-dim)**; el transversal es **profinito (dim 0)**. La hoja (imagen de $\check X_K(\mathbb C)\times\{u\}$) hereda la topología del transversal profinito: es **0-dimensional como subespacio del transversal**, y el espacio total $\mathfrak X_K$ es "genuinely 1-dimensional in the flow direction ($\mathbb R_+$) crossed with a totally disconnected (0-dimensional) transversal". [DATO verbatim]

### 2.3. El mapa de comparación con Connes–Consani

**[DATO, confirmando Doc 128 §2.3].** El mapa $\Psi_F:\mathfrak X_F\to\mathscr X_F$ (al espacio adélico de CC) es **$\mathbb R_+$-anti-equivariante** (los dos espacios tienen direcciones de flujo opuestas) y **NO es isomorfismo**. Envía órbitas $\mathbb R_+$ cerradas de Deninger a los círculos $C_{\mathfrak p}$ adélicos de CC. **No aparece ninguna estructura compleja en la comparación.** [DATO]

### 2.4. PRIMER PUNTO DE QUIEBRE: las hojas de Morishita no son variedades complejas

**[CÁLCULO — veredicto firme sobre el espacio existente].** La hipótesis H1 de math/0204111 exige **hojas que sean variedades complejas Kähler de dimensión $g\ge1$**. En el espacio de Morishita:

- la hoja tiene **dimensión real 0 en la dirección transversal** (transversal profinito) y la única dirección continua del espacio es el **flujo $\mathbb R_+$ (dim 1)**, que es **transversal a las hojas, no tangente a ellas**;
- por tanto la hoja **no es una variedad diferenciable de dimensión $\ge1$**, y *a fortiori* **no es una variedad compleja**;
- **no hay estructura casi-compleja $J$, no hay descomposición $H^{1,0}\oplus H^{0,1}$, no hay forma $Q(\cdot,J\bar\cdot)$, no hay polarización.**

> **VEREDICTO-129.A [CÁLCULO sobre DATO].** *La Hodge foliada de Deninger (math/0204111) **NO aplica** al espacio de Morishita 2508.15971 tal como está construido: sus hojas son reales de dimensión 0 (transversal profinito), no variedades complejas Kähler. El espacio de Morishita realiza el **escenario** (espacio + flujo + órbitas = primos, exactamente como Doc 128 §2.3 estableció), pero **NO la categoría geométrica (Kähler) donde la positividad-derivada es un teorema.* Es la confirmación, del lado del espacio, de lo que Doc 128 §2.3 ya dijo del lado de la cohomología: Morishita da el espacio subyacente, NO la estructura de Hodge.**

**[CÁLCULO — matiz importante, no exagerar].** Esto NO prueba que *ningún* espacio foliado de Spec ℤ pueda tener hojas Kähler. Prueba que **el único objeto hoy construido** (Morishita) no las tiene. La pregunta "¿puede existir uno que sí?" es la del §3–§5. Pero ya fija que **el camino directo —tomar Morishita y aplicarle math/0204111— está cerrado.**

---

## 3. LA DIMENSIÓN Y LA ESTRUCTURA COMPLEJA: el corazón [CONSTRUCCIÓN / GAP]

Aquí hago el análisis dimensional que el encargo marca como núcleo: ¿qué dimensión compleja de hoja se necesita para que $H^1$ del cuadrado (Doc 125, signatura $(1,2)$) sea el $H^{1,1}$ primitivo de una hoja Kähler donde Hodge–Riemann da definida negativa?

### 3.1. El grado y la signatura que el cuadrado exige

**[DATO — recordatorio de Doc 125].** La forma de intersección sobre $\langle f_1,f_2,\Delta\rangle\subset \mathrm{NS}(C_p\times C_p)$ (el cuadrado, una **superficie tropical de dimensión 2**) tiene matriz de Gram $G_{\text{toy}}=\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}$, signatura $(1,2)$, definida negativa sobre el primitivo. Esto vive en el **grado 2** de la superficie (clases de divisores = $H^2$ / $\mathrm{NS}$), que es el **grado medio** de una superficie (dim_ℝ 4, dim_ℂ 2). [DATO]

**[CÁLCULO — la traducción Hodge clásica].** En geometría algebraica clásica, la signatura $(1,\rho-1)$ del índice de Hodge sobre $\mathrm{NS}(S)$ de una superficie $S$ es **exactamente** la polarización de Hodge–Riemann sobre $H^{1,1}_{\mathrm{prim}}(S)$: sobre $H^2$ de una superficie Kähler, la forma de intersección restringida a $H^{1,1}\cap H^2(\mathbb R)$ tiene signatura $(1,h^{1,1}-1)$ (una positiva = la clase de Kähler, resto negativas = primitivo), y esto **es** la relación bilineal de Hodge–Riemann en peso $r=2$ sobre una variedad Kähler de **dimensión compleja $g=2$**. [DATO clásico]

### 3.2. La dimensión compleja de hoja que se requiere

**[CÁLCULO — el diccionario explícito].** Para que math/0204111 produzca la signatura $(1,2)$ del cuadrado como polarización foliada, hace falta:

| Objeto del cuadrado (Doc 125) | Objeto Kähler–Riemann requerido (math/0204111) |
|---|---|
| Superficie tropical $C_p\times C_p$, dim_ℂ 2 | Hoja Kähler de **dim_ℂ $g=2$** |
| Grado de las clases: $\mathrm{NS}=H^2$ (grado medio) | $\bar H^2_{\mathcal F}$, peso $r=2$ (grado medio, $r=g$) |
| Signatura $(1,2)$, primitivo definido negativo | Polarización $Q$ sobre $P^2_{\mathcal F}\cap\bar H^{1,1}_{\mathcal F}$, índice de Hodge $(1,h^{1,1}_{\text{prim}})$ |
| Hard Lefschetz: clase amplia $\ell=f_1+f_2$, $\ell^2>0$ | $L^{g-r}=L^0=\mathrm{id}$ en grado medio $r=g=2$; HL relaciona $r<g$ con $2g-r$ |

> **Requisito dimensional [CÁLCULO]:** *la hoja debe ser una **superficie compleja (dim_ℂ 2)**, y el apareamiento de Doc 125 debe vivir en su **grado medio $\bar H^2_{\mathcal F}=\bar H^{2,0}\oplus\bar H^{1,1}\oplus\bar H^{0,2}$**, con la signatura $(1,2)$ alojada en la parte $(1,1)$ primitiva.*

### 3.3. POR QUÉ NO CIERRA: el mismatch dimensional exacto

**[CÁLCULO + GAP — el núcleo del documento].** La dimensión NO cierra, y falla por DOS vías independientes, ambas hacia abajo:

**(Mismatch-I) El espacio existente (Morishita): hoja dim_ℂ $=0$.** Como §2.4, la hoja de $\mathfrak X_K$ tiene dimensión 0 (transversal profinito). $0\ne2$. No hay siquiera $H^1$ de hoja, mucho menos $H^2$ de superficie. El déficit es total: faltan **dos dimensiones complejas enteras** y la estructura compleja misma. [CÁLCULO]

**(Mismatch-II) El caso geométrico realizado (math/0204194, curva elíptica): hoja dim_ℂ $=1$.** [DATO — verbatim de math/0204194]. El **único ejemplo donde Deninger SÍ realiza la Hodge foliada** es el de la curva elíptica sobre cuerpo finito. Allí el espacio es **3-dimensional real**, $X=\tilde X/H$ con $\tilde X=\mathbb C\times V_\xi\Gamma\times\mathbb R$; las hojas $\mathcal L$ son reales de dim 3, pero dentro de cada hoja hay una **sub-foliación $\mathcal F_{\mathcal L}$ cuyas hojas son curvas complejas de dimensión 1 (superficies de Riemann)** — "the union of the tangent spaces to the $\mathcal F_{\mathcal L}$-leaves is naturally a rank 2 vector bundle on $X$" (rango 2 real = dim_ℂ 1). La fórmula explícita aparece como $\mathrm{Ind}_t(d_{\mathcal F_{\mathcal L}})(\alpha)$, el **índice transversal del complejo de de Rham a lo largo de las hojas holomorfas de dim_ℂ 1**. [DATO]

> **El mismatch exacto [CÁLCULO]:** *La hoja compleja de Deninger, en el único caso donde existe, es una **curva (dim_ℂ 1)**, cuya teoría de Hodge vive en $H^1$ con signatura **simpléctica $(g,g)$** (la forma de Riemann sobre $H^{1,0}\oplus H^{0,1}$ — Doc 127 §1.1). El cuadrado de Doc 125 necesita el $H^2$ de una **superficie (dim_ℂ 2)**, con signatura **del índice de Hodge $(1,\rho-1)$**. Son objetos de **grado y dimensión distintos**: $H^1$ de curva ($g,g$) vs $H^2$ de superficie $(1,\rho-1)$. La hoja de Deninger es de dimensión $1$; el cuadrado es de dimensión $2$. **Falta una dimensión compleja entera.***

### 3.4. La reconciliación que Doc 128 §2.4 había propuesto, y por qué el mismatch la limita

**[CÁLCULO].** Doc 128 §2.4 sugirió que "índice de Hodge sobre el cuadrado ⟺ polarización sobre $\bar H^1$ del factor" por la dualidad estándar Künneth. En el caso clásico de curvas, esto es correcto: el índice de Hodge sobre $H^2(C\times C)$ se reduce a la polarización de $H^1(C)$ vía Künneth $H^2(C\times C)=\bigoplus H^i(C)\otimes H^{2-i}(C)$, y la pieza $H^1\otimes H^1$ porta el contenido. **Esto reubica la positividad del cuadrado (dim 2) al factor (dim 1).** En este sentido, la **hoja de dim_ℂ 1 de Deninger SÍ sería el objeto correcto si el cuadrado se redujera a su factor vía Künneth.**

**[GAP — por qué esto no salva el cierre dimensional].** Tres obstrucciones, en orden creciente de gravedad:

1. **Künneth tropical no existe** (Doc 123 [DATO], citado en Doc 128 §2 GAP): la reducción cuadrado→factor que en el caso clásico es Künneth **no está disponible** en el sitio de escala tropical (los factores $C_p$ no tienen $H^1$; el RR es de tipo II). Sin Künneth, el contenido del cuadrado no se reubica limpiamente en un $H^1$ de factor. [DATO/GAP]

2. **El factor $C_p$ no es una curva compleja.** Incluso aceptando la reducción, el "factor" sería $C_p$ = círculo tropical de período $\log p$ (dim_ℝ 1, **real**, no una superficie de Riemann compleja). Su "$H^1$" tropical es real de tipo II, **sin estructura $H^{1,0}\oplus H^{0,1}$** porque no hay estructura compleja. La polarización de Hodge–Riemann necesita la descomposición de Hodge, que necesita $J$, que **no existe sobre $C_p$**. [CÁLCULO]

3. **Aun en el caso geométrico, la hoja de Deninger NO es el factor.** En math/0204194 la hoja compleja $\mathcal F_{\mathcal L}$ es la **superficie de Riemann $X(\mathbb C)$ asociada al lugar arquimediano de la curva elíptica** — una geometría que **existe porque hay un punto complejo arquimediano genuino con su estructura de Riemann**. Para Spec ℤ, el lugar arquimediano es **un solo punto** $\infty$ (la valoración real $|\cdot|_\infty$), **no una curva compleja**. **No hay superficie de Riemann ambiente de la que la hoja herede su estructura compleja.** Éste es el quiebre que §6 (pre-test de circularidad) recoge. [CÁLCULO + DATO]

---

## 4. SI LA DIMENSIÓN CERRARA [CONSTRUCCIÓN — el escenario contrafáctico]

**[CONSTRUCCIÓN — estatus: hipotético, contingente a un espacio que NO existe].** Supongamos, *contra los hechos de §2–§3*, que existiera un espacio foliado $\mathfrak X_{\mathbb Z}$ para $\overline{\mathrm{Spec}\,\mathbb Z}$ con:
- hojas que fueran **superficies complejas Kähler (dim_ℂ 2)**, con estructura compleja $J$ integrable hoja-a-hoja variando suavemente en transversal;
- métrica transversa Riemanniana (foliación Riemanniana);
- flujo $\phi^t$ con órbitas cerradas de longitud $\{\log p\}$ y la cohomología foliada $\bar H^\bullet_{\mathcal F}$ portando los ceros de ζ en $\bar H^1_{\mathcal F}$ (o el grado adecuado).

**[CONSTRUCCIÓN — qué daría].** Entonces math/0204111 produciría, **como teorema** (no postulado):
- Hard Lefschetz foliado $L^{g-r}$ con $g=2$;
- una estructura de Hodge real polarizable sobre $P^2_{\mathcal F}$;
- la positividad $Q(\xi,J\bar\xi)>0$ sobre el primitivo de $\bar H^2_{\mathcal F}\cap\bar H^{1,1}$.

**[CONSTRUCCIÓN — cómo elevaría la signatura $(1,2)$ del juguete].** La matriz $G_{\text{toy}}$ de Doc 125 (signatura $(1,2)$, primitivo definido negativo) **sería la sombra finita/tropical de la polarización de Hodge–Riemann sobre $\bar H^{1,1}_{\mathcal F,\mathrm{prim}}$ de la hoja-superficie**. La "negatividad definida sobre el primitivo" (G2) **sería un teorema de Hodge a lo largo de las hojas**, no un accidente del caso finito ni la traza del flujo. Esto cerraría G-125.B (la persistencia de la signatura) **por geometría de Hodge, evadiendo Babaee–Huh** (que obstruye la vía *tropical-de-intersección*, pero no la vía *Hodge-analítica-de-hojas*, Doc 128 §3.3) y **evadiendo NC3** (la positividad no se leería sobre la traza del flujo = fórmula explícita, sino sobre la polarización de las hojas, geométrica). [CONSTRUCCIÓN]

**[GAP — qué quedaría por verificar en este escenario contrafáctico, en orden de dificultad].**
1. **[GAP-CF1, existencia]** Que exista $\mathfrak X_{\mathbb Z}$ con hojas-superficie Kähler de dim_ℂ 2 y órbitas $\{\log p\}$. **No existe; ni siquiera para hojas de dim_ℂ 1 (curvas) está construido para Spec ℤ** — el único caso realizado es la curva elíptica (math/0204194). La rigidez espectral (1712.04181, Doc 128 §4.2) dice además que las construcciones simples (suspensiones) no dan el espectro $\{\log p\}$. [GAP — el más profundo]
2. **[GAP-CF2, la dimensión de hoja]** Por qué la hoja debería ser una **superficie** (dim_ℂ 2) y no una **curva** (dim_ℂ 1). El programa de Deninger conjetura, para $\overline{\mathrm{Spec}\,\mathbb Z}$ (objeto de dimensión aritmética 1 = "curva aritmética"), un espacio foliado de **dimensión real 3** con hojas de dimensión... — y en el análogo geométrico (curva) las hojas complejas son **curvas (dim_ℂ 1)**, NO superficies. **El cuadrado vive en dim 2 precisamente porque es el PRODUCTO; el espacio de Deninger es de $X$, no de $X\times X$.** Esto es el §5. [GAP]
3. **[GAP-CF3, infinito-dimensionalidad]** $\bar H^\bullet_{\mathcal F}$ es de dimensión infinita (los ceros); la polarización de math/0204111 es para cohomología foliada reducida de dim infinita (eso es una *ventaja* sobre AHK, Doc 128 §3.3) — pero la signatura $(1,\infty)$ y la persistencia bajo el ensamblaje infinito (T2, Doc 119) siguen sin gap conocido. [GAP]

---

## 5. SI NO CIERRA: caracterización precisa del mismatch [GAP — el resultado dominante]

**[CÁLCULO — el mismatch, aislado con precisión].** La dimensión NO cierra. Hay **tres mismatches anidados**, cada uno fatal por sí solo:

### 5.1. Mismatch de existencia de estructura compleja (el más básico)

El espacio existente (Morishita 2508.15971) tiene **hojas reales de dimensión 0** (transversal profinito); **no hay estructura compleja en ninguna hoja**. La Hodge foliada de Deninger no aplica. **(c) las hojas no tienen estructura compleja** — literal, para el espacio que hoy existe. [§2.4]

### 5.2. Mismatch de dimensión de hoja (curva vs superficie)

Aun en el caso geométrico realizado (math/0204194), la hoja compleja es una **curva (dim_ℂ 1)**, con teoría de Hodge en $H^1$ de signatura simpléctica $(g,g)$. El cuadrado de Doc 125 es una **superficie (dim_ℂ 2)** con índice de Hodge $(1,\rho-1)$ en $H^2$. **Falta una dimensión compleja**: la hoja de Deninger es de dim 1, el cuadrado de dim 2. [§3.3]

### 5.3. Mismatch de localización: el cuadrado NO es una hoja, es el producto del espacio total

**[CÁLCULO — el mismatch estructural más importante, que el encargo §5 anticipa].** Éste es el quiebre conceptual decisivo:

- **El espacio de Deninger $\mathfrak X$ es el análogo de $X$** (un esquema aritmético, $\overline{\mathrm{Spec}\,\mathbb Z}$), **no de $X\times X$.** Su cohomología foliada $\bar H^\bullet_{\mathcal F}$ porta los ceros en $\bar H^1_{\mathcal F}$ (grado 1, no grado 2).
- **El cuadrado de Doc 125 ($C_p\times C_p$) es el análogo de $X\times X$** — la *superficie* sobre la que se hace teoría de intersección de superficies (el template de Castelnuovo–Severi/Weil).
- **Por tanto el cuadrado NO corresponde a una HOJA del espacio de Deninger.** Corresponde al **producto $\mathfrak X\times\mathfrak X$ de dos copias del espacio total.** Y el producto de dos espacios foliados de dimensión real 1 (cada uno la dirección del flujo) sobre transversales profinitos es un objeto laminado de **dimensión real 2 (dos flujos $\mathbb R_+\times\mathbb R_+$)** sobre un transversal profinito — **NO una variedad Kähler de dim_ℂ 2**, sino un objeto real-laminado sin estructura compleja. [CÁLCULO]

> **VEREDICTO-129.B [CÁLCULO].** *Hay una **confusión de niveles** entre los dos programas: Deninger pone la positividad-RH sobre $\bar H^1_{\mathcal F}(\mathfrak X)$ (grado 1 del espacio total $X$, vía la polarización de las hojas, que en el caso geométrico son curvas dim_ℂ 1); el programa del cuadrado (Doc 124–125) pone la positividad sobre $H^2(X\times X)=\mathrm{NS}$ (grado 2 del producto, índice de Hodge de superficie). **Son dos encarnaciones DUALES de la misma positividad** (Doc 128 §2.4: índice de Hodge sobre el cuadrado ⟺ polarización sobre $H^1$ del factor), **pero la dualidad que las identifica es Künneth, y Künneth tropical no existe (Doc 123).** Sin Künneth, el cuadrado (dim 2, superficie) y la hoja de Deninger (dim 1, curva) **no se identifican**, y el cierre dimensional falla.*

### 5.4. Resumen del mismatch

| Vía | Objeto | dim_ℂ | Grado/signatura | ¿Cierra con el cuadrado $(1,2)$? |
|---|---|---|---|---|
| Morishita (existe) | hoja real | 0 | sin Hodge | NO — no hay estructura compleja |
| math/0204194 (caso geométrico) | hoja = curva | 1 | $H^1$, simpléctica $(g,g)$ | NO — grado/dim equivocados (falta 1 dim) |
| Cuadrado Doc 125 | superficie $C_p\times C_p$ | (2, tropical) | $H^2=\mathrm{NS}$, $(1,2)$ | es el PRODUCTO, no una hoja |
| Lo que se necesitaría | hoja-superficie Kähler | 2 | $H^2$, $(1,\rho-1)$ | sí, pero NO existe (§4 GAP-CF1) |

**[CÁLCULO] El obstáculo exacto, en una frase:** *el espacio de Deninger es de dimensión equivocada para el cuadrado (es el análogo de $X$ —hojas de dim_ℂ $\le1$, curvas— no de $X\times X$ —superficie de dim_ℂ 2—), su realización existente (Morishita) ni siquiera tiene hojas complejas (dim_ℂ 0), y el puente que las identificaría (Künneth, dualidad índice-de-Hodge ⟺ polarización) no existe tropicalmente.*

---

## 6. EL PRE-TEST DE CIRCULARIDAD [CONJETURA — preliminar; veredicto fino al Doc 130]

La pregunta: la estructura compleja de las hojas que math/0204111 requiere — ¿proviene de la geometría del espacio (externa, no circular) o hay que construirla USANDO los ceros/valores de ζ (circular)?

### 6.1. En el caso geométrico (curva / cuerpo de funciones): la estructura compleja es EXTERNA [DATO]

**[DATO].** En math/0204194 (curva elíptica $E/\mathbb F_q$), la estructura compleja de las hojas $\mathcal F_{\mathcal L}$ (curvas dim_ℂ 1) **viene de la geometría compleja genuina del lugar arquimediano**: hay una superficie de Riemann ambiente $E(\mathbb C)$ (o su análogo en la suspensión) cuya estructura compleja la hoja **hereda**. Es **externa a la función zeta**: la estructura de Riemann de $E(\mathbb C)$ existe antes y sin conocer ningún cero. Esto es lo que hace que la positividad-derivada de math/0204111 sea no circular **en ese caso** (Doc 128 §3.1): igual que el índice de Hodge clásico es geometría de superficies, independiente de dónde estén los puntos. [DATO + CÁLCULO]

### 6.2. Para Spec ℤ: NO hay geometría arquimediana que provea la estructura compleja [CONJETURA]

**[CÁLCULO — el punto que el Doc 130 debe profundizar].** Para $\overline{\mathrm{Spec}\,\mathbb Z}$:
- el lugar arquimediano es **un único punto** $\infty$ (la valoración real $|\cdot|_\infty$ sobre $\mathbb Q$), **no una curva compleja**. No hay una "superficie de Riemann ambiente $X(\mathbb C)$" de la que la hoja herede una estructura compleja. (Contraste: para una curva sobre $\mathbb F_p$, el "constante field" $\mathbb F_p$ y el lugar geométrico dan la estructura; para $\mathbb Z$, el campo base es $\mathbb F_1$, sin geometría compleja genuina.)
- Por tanto **la fuente externa de la estructura compleja —la geometría arquimediana— está ausente.** No hay de dónde sacar el $J$ de las hojas "gratis".

**[CONJETURA — lectura preliminar, el pre-veredicto que el Doc 130 debe confirmar/refinar].**

> *La estructura compleja de las hojas que math/0204111 requiere para Spec ℤ **no proviene de una geometría externa** (no la hay: el arquimediano es un punto, no una curva). La única manera conocida de fabricar una variación de estructura de Hodge sobre las hojas con los **autovalores correctos** (los ceros de ζ en $\bar H^1_{\mathcal F}$) sería **prescribir los periodos / la polarización usando los ceros de ζ mismos** — es decir, **inyectar ζ a mano** en la definición de $J$. Ésa sería la circularidad: la estructura compleja no se deriva de la geometría, sino que se diseña para que su Hodge reproduzca los ceros, con lo que "la positividad ⟹ RH" se vuelve "RH ⟹ RH".*

**[CÁLCULO — por qué esto es el mismo fenómeno de Doc 127, visto desde las hojas].** Doc 127 mostró que **el flujo** del sitio de escala lleva ζ adentro (su traza es la fórmula explícita), por eso la ruta dinámica/Forni es circular. El presente pre-test sugiere lo **dual desde las hojas**: si el flujo lleva ζ, y la estructura compleja transversa al flujo debe ser compatible con él, entonces la estructura compleja heredaría el contenido aritmético del flujo — **a menos que haya una geometría arquimediana independiente que la fije, y para Spec ℤ no la hay.** El encargo de Phase 42–43 (Doc 127 §5.3) insistía: *"la positividad debe venir de las HOJAS, no del flujo"*. El pre-test dice: **para Spec ℤ las hojas no tienen una fuente de estructura compleja independiente del flujo (= de ζ), porque falta la geometría arquimediana.** [CONJETURA — el quiebre fino lo certifica el Doc 130]

### 6.3. El test de circularidad sobre la construcción candidata

**[CÁLCULO — preliminar].** Aplico el espíritu de R-NC (Doc 119) a la hipotética estructura compleja de hoja:
- **NC1 (externalidad de la definición):** ¿se define $J$ sin mencionar ζ? **En el caso geométrico SÍ** (heredada de $X(\mathbb C)$). **Para Spec ℤ, dudoso** — no hay candidato externo. *Pre-falla.*
- **NC2 (sobregeneración):** ¿la estructura Kähler vale para todo el espacio independientemente de los ceros? En el caso geométrico sí; para Spec ℤ, si $J$ se construye desde los ceros, **no sobregenera** (solo "funciona" para la ζ verdadera). *Pre-falla.*
- **NC3 (no-reducción a la traza del flujo):** la estructura compleja transversa al flujo de escala — si el flujo lleva ζ (Doc 127), $J$ compatible la heredaría. *Riesgo alto.*

**[CONJETURA] Pre-veredicto de circularidad: la estructura compleja para Spec ℤ es, en la lectura preliminar, ζ-dependiente (circular), por ausencia de geometría arquimediana externa. Confianza media; el veredicto fino — incluido si existe alguna construcción externa no obvia (p.ej. vía la geometría de $\mathbb F_1$, o un solenoide complejo à la 1712.04181 con $J$ de la monodromía) — queda al Doc 130.**

---

## 7. VEREDICTO

### 7.1. Clasificación (a)/(b)/(c)/(d)

**[CÁLCULO] Veredicto: (c) dominante con (b) — las hojas (en el espacio existente) NO tienen estructura compleja, Y la dimensión NO cierra para el cuadrado (mismatch estructural caracterizado).**

Desglose:

- **¿(a) puede existir y la dimensión cierra?** **NO.** Requeriría un espacio foliado de Spec ℤ con hojas-superficie Kähler de dim_ℂ 2 y órbitas $\{\log p\}$; tal espacio **no existe** (ni para dim_ℂ 1; el único caso realizado es la curva elíptica), y aunque existiera, su hoja sería de dim_ℂ $\le1$ (el espacio de Deninger es el análogo de $X$, no de $X\times X$). No es (a).

- **¿(b) la dimensión NO cierra (mismatch estructural)?** **SÍ, caracterizado con precisión (§5).** Triple mismatch anidado: (i) Morishita tiene hojas dim_ℂ 0 (sin estructura compleja); (ii) el caso geométrico tiene hojas dim_ℂ 1 (curva), pero el cuadrado necesita dim_ℂ 2 (superficie) — falta una dimensión; (iii) **el cuadrado NO es una hoja sino el producto del espacio total $X\times X$**; la identificación cuadrado↔factor requiere Künneth, que no existe tropicalmente.

- **¿(c) las hojas no tienen estructura compleja?** **SÍ, literal para el espacio que hoy existe (Morishita).** Sus hojas son reales de dim 0; no hay $J$, no hay Hodge foliada. La Hodge polarizable de Deninger (math/0204111) **no aplica al espacio de Morishita.** [§2.4]

- **¿(d) indeterminable?** **NO.** El estatus ES determinable: para el espacio existente, las hojas son reales (c); para cualquier espacio que diera el cuadrado, la dimensión no cierra (b). Lo único genuinamente abierto es si *podría* construirse un espacio nuevo con hojas-superficie Kähler externas a ζ — y el pre-test (§6) sugiere que NO (falta geometría arquimediana), pendiente del Doc 130.

> **VEREDICTO COMPUESTO: (c)+(b).** *El espacio foliado de Spec ℤ que hoy existe (Morishita 2508.15971) **no admite estructura de Hodge polarizable foliada** porque sus hojas son reales de dimensión 0, no variedades complejas Kähler (c). Aun postulando un espacio con hojas complejas, **la dimensión no cierra para el cuadrado de Doc 125**: la hoja de Deninger es una curva (dim_ℂ 1, $H^1$ simpléctico), el cuadrado es una superficie (dim_ℂ 2, $H^2$ índice de Hodge), y el cuadrado corresponde al **producto $X\times X$, no a una hoja**; el puente Künneth que los identificaría no existe tropicalmente (b).*

### 7.2. Contraste con el veredicto (a) de Doc 128

**[CÁLCULO].** Doc 128 dio veredicto **(a) no circular, condicional a Kähler–Riemann**, sobre el **estatus lógico del programa de Deninger en abstracto**. Doc 129 es más fino y más severo: **al exigir que el espacio concreto (Morishita) tenga la estructura Kähler que la condición de Doc 128 requiere, la condición FALLA** — las hojas son reales de dim 0. La no-circularidad de Doc 128 era *condicional a un espacio que no existe con la estructura correcta*. Doc 129 muestra que **la condición no se cumple en el único espacio realizado**, y que aun realizándola la dimensión no casaría con el cuadrado. **El veredicto (a) de Doc 128 era correcto sobre el formalismo; (c)+(b) de Doc 129 es el veredicto sobre la realización concreta.**

### 7.3. Lista de lo que faltaría (en orden de dificultad)

1. **[GAP, decisivo]** Construir un espacio foliado de $\overline{\mathrm{Spec}\,\mathbb Z}$ con **hojas que sean variedades complejas Kähler** (no reales de dim 0). Hoy no existe; Morishita da hojas reales profinitas. La obstrucción de rigidez espectral (1712.04181) impide las construcciones simples.
2. **[GAP, dimensional]** Que esas hojas sean de la **dimensión compleja correcta** para el objeto que da la signatura. Si el contenido vive en $\bar H^1_{\mathcal F}$ (programa de Deninger), hojas dim_ℂ 1 (curvas) — pero entonces la signatura es simpléctica $(g,g)$, no el índice de Hodge $(1,\rho-1)$ del cuadrado; hay que **decidir en qué grado y dimensión vive realmente la positividad-RH** y reconciliar con Doc 125.
3. **[GAP, Künneth]** Un análogo de Künneth tropical / una dualidad índice-de-Hodge-sobre-el-cuadrado ⟺ polarización-sobre-el-factor que funcione en característica 1 / sobre el sitio de escala, para identificar el cuadrado (dim 2) con la hoja (dim 1). Doc 123 lo declaró inexistente tropicalmente.
4. **[GAP, circularidad — al Doc 130]** Una fuente **externa a ζ** de la estructura compleja de las hojas para Spec ℤ. El pre-test (§6) sugiere que no la hay (falta geometría arquimediana: el arquimediano es un punto, no una curva). Si se confirma, la estructura compleja sería ζ metida a mano = circular = el resultado que el encargo anticipa.

---

## 8. Honestidad y registro

Ningún teorema nuevo se probó. Se **leyó en fuente** (math/0204111 vía ar5iv: definición de foliación Kähler–Riemann, hojas Kähler dim_ℂ $g$, Hard Lefschetz Prop. 4.3, polarización Prop. 4.4, positividad $Q(\xi,J\bar\xi)>0$, origen en la descomposición de Álvarez López–Kordyukov; math/0204194 vía ar5iv: el ejemplo de la curva elíptica, hojas $\mathcal F_{\mathcal L}$ = curvas complejas dim_ℂ 1, fórmula explícita = índice transversal; Morishita 2508.15971 vía HTML: $\mathfrak X_K=\check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+$, transversal profinito dim 0, hojas reales, **sin estructura compleja**, mapa $\Psi_F$ anti-equivariante; WebSearch: la definición de estructura compleja foliada y la confirmación de que el espacio de Spec ℤ sigue sin construirse) y se **calculó** el diccionario dimensional con el cuadrado de Doc 125.

**Lo central:**
- **math/0204111 prueba** que para foliaciones Kähler–Riemann (hojas Kähler de dim_ℂ $g$), la cohomología foliada reducida porta Hard Lefschetz + estructura de Hodge polarizable + positividad de Hodge–Riemann; **la positividad viene EXACTAMENTE de la polarización de Hodge clásica de cada hoja Kähler compacta, promediada transversalmente.** La hipótesis "hojas Kähler" es inflexible.
- **El espacio de Morishita** tiene transversal **profinito (dim 0)** y la única dirección continua es el **flujo $\mathbb R_+$**; sus hojas son **reales de dim 0, SIN estructura compleja**. La Hodge foliada de Deninger **no aplica.** **Primer quiebre: (c).**
- **La dimensión NO cierra para el cuadrado:** la hoja de Deninger (en el único caso realizado) es una **curva (dim_ℂ 1, $H^1$ simpléctico)**; el cuadrado de Doc 125 es una **superficie (dim_ℂ 2, $H^2$ índice de Hodge $(1,2)$)**; y el cuadrado corresponde al **producto $X\times X$, NO a una hoja**. El puente (Künneth) no existe tropicalmente. **Segundo quiebre: (b).**
- **Pre-test de circularidad:** para Spec ℤ no hay geometría arquimediana (el arquimediano es un punto, no una curva) de la que las hojas hereden estructura compleja externa; la candidata es **ζ metida a mano** = circular. **[CONJETURA, al Doc 130.]**

**El punto de traba ES el resultado:** Doc 128 declaró el marco de Deninger *no circular condicional a Kähler–Riemann*. Doc 129 muestra que **la condición Kähler–Riemann FALLA en el único espacio realizado (Morishita: hojas reales dim 0)**, y que **aun forzándola, la dimensión no casa con el cuadrado** (curva dim 1 vs superficie dim 2; hoja vs producto; sin Künneth). **Veredicto: (c)+(b)** — las hojas del espacio existente no son complejas, y el cuadrado vive en una dimensión y nivel (producto, dim 2) que ninguna hoja de Deninger (dim $\le1$) realiza. La pieza que faltaría —un espacio de Spec ℤ con hojas Kähler de la dimensión correcta, con estructura compleja **externa a ζ**— no existe, y el pre-test sugiere que su estructura compleja sería ζ-dependiente. El Doc 130 dicta el veredicto fino de circularidad.

---

## Referencias

**Fuente externa leída esta sesión (junio 2026, vía WebFetch/WebSearch):**
- C. Deninger, W. Singhof, *Real polarizable Hodge structures arising from foliations*, arXiv:math/0204111 (vía ar5iv) — **definición de foliación Kähler–Riemann** (hojas Kähler de dim_ℂ $g$, foliación Riemanniana bundle-like); **Prop. 4.3** Hard Lefschetz foliado $L^{g-r}:\bar H^r_{\mathcal F}\xrightarrow{\sim}\bar H^{2g-r}_{\mathcal F}$; **Prop. 4.4** $Q$ polariza el Hodge real de peso $r$ sobre $P^r_{\mathcal F}$; **positividad $Q(\xi,J\bar\xi)>0$**; origen en la **descomposición de Hodge suave de Álvarez López–Kordyukov** (clases = formas armónicas a lo largo de las hojas). **[DATO]**
- C. Deninger, W. Singhof, *On the nature of the explicit formulas in analytic number theory — a simple example*, arXiv:math/0204194 (vía ar5iv) — el espacio $X=\tilde X/H$, $\tilde X=\mathbb C\times V_\xi\Gamma\times\mathbb R$, 3-dim real; hojas $\mathcal L$ reales de dim 3 con sub-foliación $\mathcal F_{\mathcal L}$ cuyas **hojas son curvas complejas dim_ℂ 1 (superficies de Riemann)**, fibrado tangente de rango 2; fórmula explícita $=\mathrm{Ind}_t(d_{\mathcal F_{\mathcal L}})$ índice transversal; solenoide generalizado. **[DATO — el único caso geométrico realizado, hoja dim_ℂ 1.]**
- M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*, arXiv:2508.15971 (2025, vía HTML) — $\mathfrak X_K=\check X_K(\mathbb C)\times_{\mathbb Q_+}\mathbb R_+$; **transversal $\check X_K(\mathbb C)$ totalmente disconexo / profinito (dim 0)**; hojas = imágenes de $\check X_K(\mathbb C)\times\{u\}$, **reales, SIN estructura compleja ni Kähler**; flujo $\phi^t$ Frobenius; órbitas cerradas $\gamma_{\mathfrak p}$ círculos de longitud $\log N\mathfrak p$; paquete $\Gamma_{\mathfrak p}$ = mapping torus; $\Psi_F$ $\mathbb R_+$-anti-equivariante, NO iso. **[DATO — el espacio existente NO tiene hojas complejas.]**
- arXiv:1712.04181, *On the leafwise cohomology and dynamical zeta functions for fiber bundles over the circle* — cohomología foliada infinito-dimensional; rigidez espectral (espectro del generador forzado por la monodromía); el espacio de Spec ℤ sigue sin construirse. **[DATO, vía abstract + Doc 128.]**
- J. A. Álvarez López, Y. A. Kordyukov — teorema de descomposición de Hodge suave para foliaciones Riemannianas (referencia [1] de math/0204111). **[DATO, vía math/0204111.]**
- WebSearch (junio 2026): confirmación de que (i) la estructura compleja de una foliación = $J$ casi-compleja sobre $T\mathcal F$ con restricciones integrables a las hojas, que portan estructuras holomorfas variando suavemente en transversal; (ii) el espacio foliado de Spec ℤ **sigue sin construirse** (solo la curva elíptica, 2002). **[DATO]**

**Internas (backward-only):** Doc 119 (R-NC NC1–NC4; T2 signaturas no continuas bajo límites; R-LEF-FLUJO); Doc 123 (Künneth tropical no existe; los factores $C_p$ sin $H^1$); Doc 124 (G2 = índice de Hodge indefinido $(1,\rho-1)$; positividad CC espectral = circular); Doc 125 ($C_p\times C_p$; $G_{\text{toy}}$ signatura $(1,2)$, primitivo definido negativo; G-125.A real/entero; G-125.B persistencia à la Babaee–Huh); Doc 127 (la ruta dinámica/Forni es circular: el flujo de escala lleva ζ adentro; la positividad debe venir de las HOJAS, no del flujo); Doc 128 (el programa de Deninger; veredicto (a) no circular *condicional a Kähler–Riemann*; math/0204111 es el teorema de positividad-derivada; Morishita da espacio+flujo no la cohomología; el objeto-meta unificado).

*Fin del Documento 129.*
