# Doc 128 — El programa de Deninger: ¿es ésta la cohomología foliada que falta?

**Programa:** Hipótesis de Riemann — Phase 42: matemática nueva para cruzar el muro (Hodge dinámica).
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 125 (la forma de intersección sobre el cuadrado del sitio de escala, vía Allermann–Rau; el flujo $\Delta_\mu$; la matriz de Gram $G_{\text{toy}}$ del juguete $C_p\times C_p$, signatura $(1,2)$, primitivo definido negativo; gaps G-125.A real/entero, G-125.B persistencia de signatura à la Babaee–Huh); Doc 126 (el paquete de Kähler; AHK no aplica por infinitud + flujo continuo; Babaee–Huh obstruye genéricamente; el núcleo se desplaza a "probar que el cuadrado es del subtipo matroidal/Lefschetz, externo a $\zeta$"; veredicto (d) con sesgo a (b)/(c)); Doc 127 (Hodge dinámica / Forni, que corre en paralelo — la síntesis se exige en §5); Doc 119 (el test R-NC, cláusulas NC1–NC4; el cuantificador maestro P43; R-SIG ≺ R-FIN; tensiones T2/T3/T4).

**Disciplina de etiquetado (regla absoluta):** **[DATO]** = leído en fuente esta sesión (arXiv / survey, con cita) o teorema interno (cita backward-only). **[CONJETURA-DENINGER]** = lo que Deninger CONJETURA, atribuido con precisión, distinguido de lo que él prueba. **[ANALOGÍA]** = correspondencia de diccionario, no teorema. **[GAP]** = lo que falta, con precisión. **[CONJETURA-NUESTRA]** = lo que proponemos. **[CÁLCULO]** = derivación mía. **[NO VERIFICADO]**. NUNCA "probado" salvo lo genuino. El objetivo: determinar si la cohomología foliada conjetural de Deninger ES el marco donde vive nuestra forma de intersección con flujo, si la positividad que él espera ES nuestra G2, y el estado real (qué se ha probado del programa, qué sigue conjetural).

---

## 0. Resumen ejecutivo

El programa de Deninger es, hoy, el candidato más cercano a "el marco geométrico genuino" cuya ausencia los Docs 124–126 identificaron como la causa de la circularidad. Su forma es exactamente la que Doc 126 §4.4 echó en falta: un flujo $\mathbb R$ sobre un espacio foliado, los primos como órbitas cerradas de longitud $\log p$, el lugar arquimediano como puntos fijos, la fórmula explícita como una fórmula de trazas de Lefschetz, y **RH como positividad de tipo Hodge sobre $H^1_{\mathcal F}$**. La pregunta del encargo —¿es éste el marco no circular, o es circular, u obstruido?— admite una respuesta más fina que la de Docs 124–126, porque Deninger **probó** la pieza decisiva en un caso modelo.

**Hallazgos centrales:**

1. **Lo que Deninger CONJETURA vs lo que PRUEBA, separado con cuidado (§1).** CONJETURA: la existencia de un espacio foliado (laminado) $X$ con flujo $\phi^t$ y una cohomología foliada reducida $\bar H^\bullet_{\mathcal F}$ tal que la fórmula explícita de Weil ES la fórmula de trazas de Lefschetz del flujo, y RH equivale a una positividad sobre $\bar H^1_{\mathcal F}$. PRUEBA: (i) **el formalismo** —que SI tal cohomología existe con las propiedades estándar (Poincaré, Künneth, Lefschetz, una teoría de Hodge a lo largo de las hojas), ENTONCES la ecuación funcional, la fórmula explícita y la positividad-RH se siguen— [DATO]; (ii) en el caso **Kähler–Riemann** (foliaciones por variedades complejas con métrica transversa), **la estructura de Hodge polarizable, Hard Lefschetz y la positividad de Hodge–Riemann sobre $\bar H^\bullet_{\mathcal F}$ son TEOREMAS** (math/0204111) [DATO]; (iii) el ejemplo simple (math/0204194) donde la fórmula explícita de un L-trivial es literalmente una traza de Lefschetz [DATO].

2. **La identificación con nuestra forma de intersección (§2): ANALOGÍA fuerte, NO igualdad.** Nuestro $\Delta_\mu$ (flujo de escala de Doc 125) ↔ el flujo $\phi^t$ de Deninger; nuestras $\Delta_{p^k}$ ↔ las órbitas periódicas de longitud $\log p$. PERO: (a) Connes–Consani (CC, el sitio de escala) y Deninger son **dos programas distintos** que **convergen sólo parcialmente** — Morishita (2508.15971, 2025) construye un mapa de comparación $\mathbb R_+$-**anti**-equivariante entre ambos para cuerpos abelianos, **no un isomorfismo** [DATO]; (b) nuestra forma vive sobre el **cuadrado** $X\times X$ (teoría de intersección de superficie), mientras Deninger trabaja sobre $X$ mismo (cohomología foliada de dimensión 3 con flujo); son **dos encarnaciones de la misma positividad** (índice de Hodge vs polarización de Hodge–Riemann foliada), no el mismo objeto literal.

3. **El test de circularidad (§3): el resultado más importante del documento.** La conjetura de Deninger es del tipo **NO circular** en su forma fuerte: la positividad-RH **NO** es una hipótesis adicional puesta a mano, sino una **consecuencia esperada de la existencia del espacio foliado correcto** (de tipo Kähler–Riemann), porque en ese caso la positividad es un **teorema de teoría de Hodge a lo largo de las hojas** (math/0204111), igual que el índice de Hodge clásico es un teorema de geometría de superficies, no un axioma. **Por tanto: construir el espacio (con la estructura Kähler–Riemann) DARÍA RH sin asumir positividad=RH.** El problema es **geométrico** (construir el espacio), no lógico (no es circular en sí). Esto contrasta con CC, donde la positividad de Weil es espectral y circular (Doc 124). **Veredicto del test: (a) marco no circular — condicionado a que el espacio sea de tipo Kähler–Riemann.**

4. **Los obstáculos de no-existencia (§4) son reales y precisos.** (i) El espacio foliado para $\operatorname{Spec}\mathbb Z$ **no está construido** y su existencia es **desconocida** — el único caso plenamente realizado es el de **curvas / cuerpos de funciones** (donde la foliación ya existe vía el flujo geodésico/suspensión) [DATO Leichtnam, Deninger]. (ii) Hay una **obstrucción de rigidez espectral probada** (1712.04181): para suspensiones/fibrados sobre el círculo, el espectro del generador infinitesimal está **forzado por la monodromía** — el conjunto de longitudes de órbitas cerradas **no es arbitrario**; no se puede prescribir libremente $\{\log p\}$ con las multiplicidades correctas. (iii) La cohomología foliada es **genéricamente de dimensión infinita y de naturaleza analítica, no topológica** — esto coincide con R-FIN/R-SIG ≺ de Doc 119 y con la dimensión infinita de Doc 126 §2.4. (iv) **Resultado positivo reciente** que recalibra: Álvarez López–Kordyukov–Leichtnam (2402.06671, 2024) **PROBARON** la fórmula de trazas de Lefschetz para flujos foliados sobre variedades reales con foliación de codimensión 1 — "resolviendo una conjetura de Deninger" — usando **dos** cohomologías reducidas. La maquinaria analítica de trazas ya **existe y funciona**; lo que falta es el **espacio aritmético** sobre el que correrla.

5. **Síntesis con Doc 127 (§5): SON el mismo objeto-meta visto de dos lados.** Forni (Doc 127) y Deninger atacan el mismo muro: ambos quieren un **flujo $\mathbb R$ ergódico/hiperbólico con un fibrado de Hodge cuya positividad da el índice sobre el primitivo**. Forni: la positividad (no-anulación de los exponentes de Lyapunov del cociclo de Kontsevich–Zorich) se prueba por **ergodicidad externa** del flujo de Teichmüller. Deninger: la positividad (polarización de Hodge–Riemann foliada) se prueba por **teoría de Hodge a lo largo de las hojas** en el caso Kähler–Riemann. **El objeto-meta unificado:** un flujo $\mathbb R$ sobre un espacio (laminado/foliado) cuya teoría de Hodge a lo largo de las hojas + ergodicidad del flujo transverso fuerzan, **externamente a $\zeta$**, la positividad de Hodge–Riemann sobre $\bar H^1_{\mathcal F}$ — que es nuestra negatividad definida sobre el primitivo (G2).

6. **Veredicto (§6): (a) marco no circular, pero NO construido y con obstrucción de realización conocida.** Deninger provee el marco lógicamente no circular (construir el espacio Kähler–Riemann da RH sin asumir positividad=RH); no es (b) circular como CC. Pero no es libre: hay obstrucción de rigidez espectral (1712.04181) y el espacio de $\operatorname{Spec}\mathbb Z$ sigue sin existir. El **primer teorema concreto construible** en esta línea NO es RH ni el espacio completo: es **verificar si el cuadrado del sitio de escala (Doc 125) o el espacio de Morishita admite una estructura Kähler–Riemann foliada (o un análogo de característica 1) — porque si la admite, la positividad de Doc 125 §5 (signatura $(1,2)$ en el juguete) se vuelve un teorema de Hodge a lo largo de las hojas, no un accidente del caso finito, y G-125.B se cerraría por geometría, no por la traza del flujo (evadiendo NC3).**

---

## 1. EL PROGRAMA DE DENINGER [DATO + CONJETURA-DENINGER]

### 1.1. La estructura conjetural — el diccionario maestro

**[CONJETURA-DENINGER]** (Deninger, ICM Berlín 1998, *Some analogies between number theory and dynamical systems on foliated spaces*, Doc. Math. Extra Vol. ICM I, 163–186; survey *Analogies between analysis on foliated spaces and arithmetic geometry*, arXiv:0709.2801; *Arithmetic geometry and analysis on foliated spaces*, Arizona Winter School / DLSDeninger.pdf.) Deninger conjetura, para un esquema aritmético $\mathcal X$ (en particular $\overline{\operatorname{Spec}\mathbb Z}$, la compactificación de Arakelov de $\operatorname{Spec}\mathbb Z$), la existencia de un objeto geométrico-dinámico:

> **(D1) Un espacio foliado (laminado) $X$ de dimensión real $3$** —una "lámina" foliada de codimensión $1$— equipado con **un flujo $\phi^t$ ($t\in\mathbb R$)** que preserva la foliación y actúa transversalmente a las hojas. El flujo $\phi^t$ es el **análogo del Frobenius** para $\operatorname{Spec}\mathbb Z$: donde en cuerpos de funciones $\mathbb F_q$ actúa el Frobenius $\operatorname{Frob}_q$ (un generador **discreto** $\mathbb Z$ de $\widehat{\mathbb Z}=\operatorname{Gal}(\overline{\mathbb F_q}/\mathbb F_q)$), aquí actúa un flujo **continuo** $\mathbb R$. [CONJETURA-DENINGER]

> **(D2) El diccionario de órbitas.** Cada primo $p$ (cada plaza finita) corresponde a una **órbita cerrada (periódica) del flujo de longitud $\log p$** (más generalmente $\log N(\mathfrak p)$ para un cuerpo de números). Las **plazas arquimedianas** (los lugares infinitos) corresponden a los **puntos fijos del flujo** $\phi^t$. [CONJETURA-DENINGER + ANALOGÍA] Este es el diccionario que reaparece literalmente en nuestro Doc 125 §3.3 (R-LEF-PRIMOS: cada primo aporta la órbita de período $\log p$) y en Doc 119 §3.4 (R-LEF-FLUJO).

> **(D3) Una cohomología foliada reducida** $\bar H^i_{\mathcal F}(X)$ ($i=0,1,2$), de **naturaleza analítica, no topológica**, **genéricamente de dimensión infinita**, con una acción inducida del flujo $\phi^t$ y de su **generador infinitesimal** $\Theta$ (la derivada de Lie a lo largo del campo del flujo). El diccionario:
> - $\bar H^0_{\mathcal F}$: el "punto" (constantes); el polo de $\zeta$ en $s=1$.
> - $\bar H^1_{\mathcal F}$: **porta los ceros** de $\zeta$ — los autovalores de $\Theta$ en $\bar H^1_{\mathcal F}\otimes\mathbb C$ deben coincidir con los **ceros no triviales** $\rho$ de $\zeta$. [CONJETURA-DENINGER]
> - $\bar H^2_{\mathcal F}$: el "grado tope" / el otro polo.

**[DATO — atribución precisa]** Que la cohomología foliada sea de dimensión infinita y "no topológica sino muy analítica" NO es una conjetura: es un **hecho** para las foliaciones reales donde se ha calculado (ver §4.2, 1712.04181). Lo conjetural es que **exista una tal foliación cuya cohomología reproduzca los ceros de $\zeta$**.

### 1.2. La fórmula explícita como fórmula de trazas de Lefschetz [CONJETURA-DENINGER, con realización parcial PROBADA]

**[CONJETURA-DENINGER]** El corazón del programa: la **fórmula explícita de Weil** (que relaciona la suma sobre los ceros $\sum_\rho \hat h(\rho)$ con la suma sobre primos $\sum_p \sum_k \frac{\log p}{p^{k/2}}h(k\log p)$ más términos arquimedianos) debe ser **una fórmula de trazas de Lefschetz dinámica** para el flujo $\phi^t$:
$$
\sum_{i=0}^{2}(-1)^i \operatorname{Tr}\big(\phi^{t*}\mid \bar H^i_{\mathcal F}\big) \;=\; \underbrace{\sum_{\gamma}\;\ell(\gamma)\!\!\sum_{k\ge1}\delta_{k\ell(\gamma)}}_{\text{órbitas cerradas}=\text{primos}} \;+\;\underbrace{(\text{contribución de puntos fijos})}_{\text{plazas arquimedianas}}.
$$
El lado izquierdo (traza sobre cohomología) = lado de los **ceros**; el lado derecho (órbitas cerradas + puntos fijos) = lado de los **primos + arquimediano**. **Ésa es exactamente la estructura de la fórmula explícita.** [CONJETURA-DENINGER + ANALOGÍA]

**[DATO — lo que SÍ está PROBADO de esto].** Tres niveles de realización:

- **(P-a) El formalismo (Deninger, probado).** Deninger **probó** que SI existe una cohomología con las propiedades estándar (dualidad de Poincaré, Künneth, una clase fundamental, una acción del flujo con generador de espectro discreto), ENTONCES se siguen formalmente: la ecuación funcional, la factorización tipo Hadamard de $\zeta$, y la fórmula explícita como traza de Lefschetz. [DATO: éste es el "infinite dimensional cohomological formalism" — el contenido de los papers de Deninger de los 90.] Es un teorema **condicional** (formalismo), no incondicional.

- **(P-b) El ejemplo simple (math/0204194, *On the nature of the explicit formulas — a simple example*).** Deninger exhibe un modelo dinámico **explícito y completo** donde la fórmula explícita de un objeto $L$-trivial **es literalmente** una fórmula de trazas de Lefschetz de un flujo sobre un espacio foliado concreto. [DATO] Aquí no hay $\zeta$ de Riemann; es el "Hello World" que demuestra que el mecanismo NO es vacío.

- **(P-c) La fórmula de trazas para flujos foliados (Álvarez López–Kordyukov–Leichtnam, arXiv:2402.06671, 2024 — PROBADA).** [DATO, abstract verbatim vía WebFetch] Sobre **variedades cerradas reales con foliación de codimensión 1 transversalmente orientada**, con un flujo foliado de órbitas cerradas simples y hojas preservadas transversalmente simples, **probaron una fórmula de trazas** que describe la distribución de Lefschetz $L_{\mathrm{dis}}(\phi)$ "en términos de datos infinitesimales de las órbitas cerradas y las hojas preservadas". **Resuelve una conjetura de Deninger**, con la innovación clave de usar **dos cohomologías foliadas reducidas** en vez de una. [DATO] **Esto es decisivo: la maquinaria analítica de la fórmula de trazas de Lefschetz para flujos foliados ya existe y es un teorema** — el cuello de botella NO es el lado analítico, sino la construcción del espacio aritmético.

### 1.3. RH como positividad sobre $\bar H^1_{\mathcal F}$ [CONJETURA-DENINGER + TEOREMA en el caso Kähler–Riemann]

**[CONJETURA-DENINGER]** La forma en que RH aparece: los ceros $\rho$ son los autovalores de $\frac{1}{2\pi}\Theta$ (el generador infinitesimal del flujo) sobre $\bar H^1_{\mathcal F}$. RH $\iff$ **todos esos autovalores tienen parte real $=\tfrac12$**, equivalentemente, tras normalizar, **el generador infinitesimal es esencialmente anti-autoadjunto** (parte real cero) respecto de un producto interno natural sobre $\bar H^1_{\mathcal F}$. Deninger conjetura que esto se sigue de **una propiedad de positividad de tipo Hodge** sobre $\bar H^1_{\mathcal F}$ — el **análogo del teorema del índice de Hodge / de la polarización de Hodge–Riemann**. [CONJETURA-DENINGER]

> **[DATO — la frase del programa, vía survey, verificada esta sesión]:** "The Riemann hypothesis would be a consequence of properties parallel to the positivity of the intersection pairing in Hodge theory."

**[DATO — el teorema que cambia el veredicto: math/0204111, *Real polarizable Hodge structures arising from foliations*].** Deninger **PROBÓ** (no conjeturó) que para las **foliaciones Kähler–Riemann** —foliaciones cuyas hojas son variedades de Kähler con métrica transversa de Riemann— la cohomología foliada reducida $\bar H^\bullet_{\mathcal F}$ porta:
- una **estructura de Hodge real polarizable** [DATO];
- un **teorema de Hard Lefschetz**: $L^{g-r}:\bar H^r_{\mathcal F}\xrightarrow{\sim}\bar H^{2g-r}_{\mathcal F}$ es isomorfismo [DATO, vía ar5iv];
- la **positividad de Hodge–Riemann**: la forma $Q(\xi,J\bar\xi)>0$ para $\xi\ne0$ sobre el primitivo [DATO];
- el **análogo de Serre de las conjeturas de Weil** se traslada [DATO].

Esto descansa en el **teorema de descomposición de Hodge suave de Álvarez López–Kordyukov** para foliaciones Riemannianas (la cohomología foliada reducida = formas globales suaves armónicas a lo largo de las hojas) [DATO]. **La positividad, en el caso Kähler–Riemann, es un TEOREMA derivado de la geometría de Hodge a lo largo de las hojas — exactamente como el índice de Hodge clásico es un teorema de geometría de superficies.** Retén esto: es el quicio de §3.

---

## 2. LA IDENTIFICACIÓN [ANALOGÍA + CÁLCULO]

### 2.1. ¿Nuestro flujo $\Delta_\mu$ ↔ el flujo $\phi^t$ de Deninger?

**[ANALOGÍA, fuerte].** Doc 125 §2.4 define las correspondencias $F_\mu:C_p\to C_p$, $u\mapsto u+\log\mu$, cuyo grafo $\Delta_\mu=\{v=u+\log\mu\}$ es una traslación de la diagonal — **el flujo de escala**. Esto es **literalmente** el flujo $\phi^t$ de Deninger restringido al bloque $C_p$: $\phi^t$ traslada por $t$ a lo largo de la dirección transversa, y $\Delta_\mu$ con $\log\mu=t$ es su grafo en el cuadrado. **El generador infinitesimal $\Theta$ de Deninger = el generador del flujo $\Delta_\mu$ cerca de $\mu=1$** (Doc 125 §3.4: "el generador infinitesimal del flujo, $\mu$ infinitesimalmente cercano a 1"). [ANALOGÍA con identificación de generadores]

**[CÁLCULO] La diferencia $\mathbb Z$ vs $\mathbb R$ es la misma en ambos.** Deninger reemplaza el Frobenius discreto ($\mathbb Z$) de cuerpos de funciones por un flujo continuo ($\mathbb R$); Doc 125 §2.4 / Doc 119 T4 reportan exactamente esta diferencia ("aquí el flujo es continuo: $\mu\in\mathbb R_+^*$, no $\mathbb Z$"). **Es el mismo fenómeno, nombrado dos veces.** La sub-red entera $\mathcal L_{\mathbb Z}$ de Doc 125 (las $\Delta_{p^k}$) = las órbitas cerradas de longitud $k\log p$ de Deninger; el flujo continuo fuera de $\mathcal L_{\mathbb Z}$ = el flujo $\phi^t$ genérico de Deninger que porta los ceros.

### 2.2. ¿Nuestras $\Delta_{p^k}$ ↔ las órbitas periódicas de longitud $\log p$?

**[ANALOGÍA, exacta].** Doc 125 §3.3: para $\mu=p^k$ ($\log\mu=k\log p\equiv0\bmod\log p$ en el toro de período $\log p$), los grafos $\Delta$ y $\Delta_{p^k}$ **coinciden** a lo largo de todo el círculo — intersección no transversal = **órbita periódica de longitud $k\log p$**. Esto es **idéntico** a (D2): el primo $p$ = órbita cerrada de longitud $\log p$, y sus iterados $k\log p$. La contribución de la traza del flujo en $\mu=p^k$ (Doc 125 §3.3, vía Connes Selecta 1999) = el término $\frac{\log p}{p^{k/2}}$ de la fórmula explícita = el término de órbita cerrada de la fórmula de Lefschetz de Deninger. **Las tres coinciden.** [ANALOGÍA + DATO]

### 2.3. ¿El sitio de escala de CC ES la realización del espacio foliado de Deninger? — NO, son dos programas distintos que convergen parcialmente

**[DATO — el punto que el encargo marca como clave].** Connes–Consani (sitio de escala / sitio aritmético) y Deninger (espacios foliados) son **dos programas relacionados pero distintos**. La relación precisa la estableció **Morishita (arXiv:2508.15971, 2025, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*)** [DATO, vía WebFetch HTML]:

- Para **cuerpos de números abelianos** $F/\mathbb Q$, Morishita construye un **mapa continuo** $\Psi_F:\mathfrak X_F\to\mathcal X_F$ entre el sistema dinámico foliado de Deninger $\mathfrak X_F$ y el espacio adélico de CC $\mathcal X_F$, que es **$\mathbb R_+$-anti-equivariante y Galois-equivariante** (Theorem 3.6). [DATO]
- **NO es un isomorfismo.** Es un mapa de comparación que **invierte la dirección del flujo** (anti-equivariante). [DATO]
- Bajo el mapa, las **órbitas cerradas atadas a los primos se corresponden** en ambos espacios: los paquetes $\Gamma_p$ (Deninger) $\cong C_p$ (CC) como círculos de longitud $\log N(\mathfrak p)$. [DATO]
- **CRUCIAL:** Morishita **NO** desarrolla la cohomología foliada ni verifica la positividad; construye **sólo el espacio subyacente y el flujo**. Lo cohomológico y la positividad **quedan abiertos** (Remark 2.1.13). [DATO]

**[CÁLCULO] Consecuencia para nuestro programa.** El sitio de escala de CC (sobre el que Doc 125 construye la forma de intersección) es una **realización parcial del espacio subyacente** de Deninger (espacio + flujo + órbitas = primos), **pero NO de la estructura cohomológica/positividad** que es donde vive RH. Es decir: CC da el **escenario** (espacio con flujo y órbitas correctas), Deninger pide además la **función de Hodge** sobre $\bar H^1_{\mathcal F}$. **Convergen en el escenario; divergen exactamente donde empieza el contenido de RH.** Esto explica por qué Doc 124 encontró que la positividad de CC es *espectral* (del lado del operador / la traza) y no *de intersección* (del lado de Hodge): CC realizó el flujo y las órbitas, no la teoría de Hodge foliada.

### 2.4. ¿La positividad de Deninger ES nuestra negatividad definida sobre el primitivo? [ANALOGÍA + mapeo]

**[CÁLCULO — el mapeo término a término].**

| Doc 125 / 126 (cuadrado $X\times X$) | Deninger (espacio foliado $X$) |
|---|---|
| Forma de intersección $D\cdot D'$ sobre $\mathrm{NS}(X\times X)\otimes\mathbb R$ | Forma de polarización $Q$ sobre $\bar H^1_{\mathcal F}$ |
| Clase amplia $\ell=f_1+f_2$, $\ell^2>0$ | Clase de Lefschetz $L$ (Hard Lefschetz foliado) |
| Primitivo $P^1=\ell^\perp$ | Primitivo $\ker(L^{\dots})\subset\bar H^1_{\mathcal F}$ |
| **Negatividad definida** sobre $P^1$ (signatura $(1,\rho-1)$) — G2, Doc 124/126 | **Positividad de Hodge–Riemann** $Q(\xi,J\bar\xi)>0$ sobre el primitivo — math/0204111 |
| Castelnuovo–Severi $\Rightarrow$ pureza peso 1 $\Rightarrow$ RH | Hard Lefschetz + polarización $\Rightarrow$ autovalores de $\Theta$ con $\Re=\tfrac12$ $\Rightarrow$ RH |

**[CÁLCULO] Son la MISMA positividad, en dos encarnaciones duales.** En geometría de superficies clásica, el índice de Hodge sobre $C\times C$ (signatura $(1,\rho-1)$, negatividad sobre el primitivo) **es equivalente** a la polarización de Hodge–Riemann sobre $H^1(C)$ (la forma de Riemann es definida positiva sobre el primitivo de $H^1$). Es la dualidad estándar: la positividad sobre $H^1$ del factor ⟺ el índice de Hodge sobre el cuadrado. **Por tanto la "negatividad definida sobre el primitivo" de Doc 124/125 (G2) ES la polarización de Hodge–Riemann que Deninger espera sobre $\bar H^1_{\mathcal F}$**, transportada del cuadrado al factor vía la correspondencia estándar índice-de-Hodge ⟺ polarización. [ANALOGÍA con contenido de cálculo; la equivalencia es teorema en el caso clásico, conjetural en transportar al caso foliado/tropical]

**[GAP] El eslabón no trivial:** que la equivalencia "índice de Hodge sobre el cuadrado ⟺ polarización sobre $\bar H^1$ del factor" **sobreviva** al paso (i) de la geometría clásica a la foliada (Deninger), y (ii) a característica 1 / tropical (CC, Doc 125). En el caso clásico es Künneth + dualidad; en el foliado Deninger la tiene en el caso Kähler–Riemann; en el tropical Doc 123 reportó que **Künneth tropical no existe** — éste es el punto de fricción.

---

## 3. EL TEST DE CIRCULARIDAD [decisivo]

La pregunta del encargo: la positividad que Deninger espera, ¿la conjetura como **consecuencia de la existencia** de la cohomología foliada (no circular: una vez que existe el espacio correcto, la positividad es automática por la geometría), o como una **hipótesis adicional equivalente a RH** (circular)?

### 3.1. La respuesta: NO circular en su forma fuerte

**[CÁLCULO — el análisis decisivo].** El test se decide por **math/0204111**. La estructura lógica del programa de Deninger es:

$$
\boxed{\;\exists\text{ espacio foliado }X\text{ de tipo Kähler–Riemann con flujo }\phi^t,\ \bar H^1_{\mathcal F}=\{\text{ceros}\}\;}\;\xLongrightarrow{\text{TEOREMA, math/0204111}}\;\boxed{\;\text{positividad de Hodge–Riemann sobre }\bar H^1_{\mathcal F}\;}\;\Longrightarrow\;\text{RH}.
$$

El primer implica es un **TEOREMA de Deninger**: si la foliación es de tipo Kähler–Riemann, la polarización **no se postula, se deriva** de la teoría de Hodge a lo largo de las hojas (descomposición de Álvarez López–Kordyukov). **La positividad NO es un axioma adicional puesto a mano: es una consecuencia geométrica de la existencia del espacio con la estructura correcta.**

**[CÁLCULO] Comparación con el modelo de Castelnuovo (Doc 125 §1.4).** Esto es **exactamente** el patrón no circular de cuerpos de funciones: allá, $C\times C$ es una superficie proyectiva genuina, y el índice de Hodge es un **teorema de geometría** (Sylvester + dualidad de Poincaré en $H^2$) que vale para **toda** clase, **independientemente de cuál sea $C$ y dónde estén sus puntos** (Doc 125 §1.4: "la positividad es geométrica, independiente de los autovalores"). La positividad de Deninger en el caso Kähler–Riemann tiene **la misma naturaleza**: vale por la geometría de Hodge de las hojas, no por dónde estén los ceros. **Pasa NC1 (externalidad), NC2 (sobregeneración: vale para todo el primitivo, no sólo las clases de $\zeta$), NC4 (en $\neg$RH un autovalor con $\Re\ne\tfrac12$ violaría la polarización, visible por la geometría).** [CÁLCULO]

### 3.2. Por qué NO es el caso (b) circular de CC

**[CÁLCULO] El contraste exacto con Doc 124.** Doc 124 estableció que la positividad de Connes–Consani es **espectral** (positividad de Weil = MW-1 = criterio de Weil = RH) y por tanto **circular** (FALLA NC3). La diferencia con Deninger:

- **CC (circular):** la positividad se lee **sobre la traza del flujo / el operador** — es la positividad de Weil de la fórmula explícita, que ES RH. No hay teoría de Hodge geométrica que la genere externamente; se verifica evaluando sobre las funciones test, lo que equivale a localizar los ceros. (Doc 125 §6.3: vía (c) traza del flujo = fórmula de Lefschetz = FALLA NC3.)
- **Deninger (no circular):** la positividad se lee **sobre la cohomología foliada vía teoría de Hodge a lo largo de las hojas** — es la polarización de Hodge–Riemann, que en el caso Kähler–Riemann es **teorema geométrico**, no la traza. **Pasa NC3** porque no se reduce a la traza del flujo: se deriva de la estructura de Hodge de las hojas (un objeto geométrico, no espectral-aritmético).

**[CÁLCULO] El quicio:** la diferencia entre los dos programas es **exactamente la diferencia NC3** de Doc 119/125. CC realizó el lado espectral (la traza del flujo = la fórmula explícita) y por eso su positividad es circular. Deninger pide el lado de Hodge (la polarización sobre la cohomología), que es donde la positividad puede ser geométrica genuina. **Doc 124 diagnosticó "la positividad de CC es espectral, no de intersección" — el programa de Deninger es precisamente el que provee la "de intersección".**

### 3.3. El precio: la no-circularidad es CONDICIONAL a "Kähler–Riemann"

**[CÁLCULO — la honestidad].** La no-circularidad **NO es gratis**. El teorema math/0204111 requiere que la foliación sea **Kähler–Riemann** (hojas Kähler, métrica transversa Riemann). El implica "existencia del espacio $\Rightarrow$ positividad" es no circular **sólo si el espacio es de ese tipo**. Por tanto el problema se desplaza a:

> **NÚCLEO-128.** ¿Es el espacio foliado de $\operatorname{Spec}\mathbb Z$ (si existe) de tipo **Kähler–Riemann** (o admite una estructura de Hodge polarizable foliada análoga)? Si SÍ $\Rightarrow$ la positividad es teorema $\Rightarrow$ RH, no circular. Si NO se sabe $\Rightarrow$ la positividad queda como hipótesis cuyo estatus es indeterminado.

Esto es **estructuralmente idéntico** al NÚCLEO-G2 de Doc 126 §4.3 ("probar que el cuadrado es del subtipo matroidal/Lefschetz, externo a $\zeta$"): en ambos, el problema NO es asumir la positividad (eso sería circular), sino **probar que el espacio es del subtipo geométrico donde la positividad es automática**. Doc 126 lo llamó "matroidal/Lefschetz tropical"; Deninger lo llama "Kähler–Riemann". **Son el mismo enunciado-meta en dos dialectos.** [CÁLCULO]

**[CÁLCULO] Diferencia favorable a Deninger sobre AHK/tropical (Doc 126).** Doc 126 §2.4 mostró que AHK **no aplica** porque es un método **finito** (inducción sobre red de flats finita) y el sitio es infinito-dimensional. **Deninger NO tiene ese problema:** su teoría de Hodge foliada (math/0204111) es **intrínsecamente infinito-dimensional y analítica** — la descomposición de Álvarez López–Kordyukov es para cohomología foliada reducida de **dimensión infinita**. **Deninger ya trabaja en el régimen infinito que mata a AHK.** Esto es una ventaja real: el obstáculo central de Doc 126 (R-SIG ≺ R-FIN, la infinitud rompe AHK) **no obstruye a Deninger**, porque su maquinaria de Hodge es analítica-infinita desde el origen. La fórmula de trazas de 2402.06671 también es para cohomología foliada infinita. [CÁLCULO — recalibración importante respecto de Doc 126]

---

## 4. EL ESTADO REAL Y LOS OBSTÁCULOS CONOCIDOS [DATO]

### 4.1. Lo que NO existe: el espacio para $\operatorname{Spec}\mathbb Z$

**[DATO]** El espacio foliado para $\operatorname{Spec}\mathbb Z$ (o cualquier esquema aritmético sobre $\mathbb Z$) **no está construido**, y su existencia es **desconocida**. Citas verificadas esta sesión:
- "for algebraic schemes over $\operatorname{Spec}\mathbb Z$ ... no cohomology theory has yet been developed ... the conjectured cohomology has not been constructed" [DATO].
- "The existence of such a foliated space and flow is still unknown except when the base curve is an elliptic curve" [DATO]. (Es decir: el único caso plenamente realizado es geométrico — curvas / cuerpos de funciones / curvas elípticas — donde la foliación ya existe vía suspensión del flujo geodésico o análogo.)
- Leichtnam (arXiv:1307.3851): propone **axiomas** para el espacio foliado de cuerpos de números y deriva **formalmente** una fórmula de Atiyah–Bott–Lefschetz que implicaría la conjetura de Artin; pero el espacio "whose existence is still unknown" [DATO verbatim].

**[CÁLCULO] Estatus:** el programa de Deninger es **un PROGRAMA, mayormente abierto**. Lo probado es: el formalismo (condicional), el caso Kähler–Riemann (teorema, pero ese caso NO es $\operatorname{Spec}\mathbb Z$), el ejemplo simple (toy), y la fórmula de trazas analítica (2402.06671, sobre variedades reales dadas, no aritméticas). Lo abierto: **la construcción del espacio aritmético** con las órbitas $\{\log p\}$ y la cohomología $=$ ceros.

### 4.2. La obstrucción de rigidez espectral — un resultado de NO-arbitrariedad [DATO]

**[DATO — el obstáculo concreto, arXiv:1712.04181, *On the leafwise cohomology and dynamical zeta functions for fiber bundles over the circle*].** Para suspensiones / fibrados sobre $S^1$ (la clase más simple de espacios foliados con flujo), se **PRUEBA** (Theorem 3.2, vía WebFetch):
$$
\operatorname{Sp}\big(\Theta\mid \bar H^i_{\mathcal F}(M,\mathbb C)\big)=\Big\{\tfrac{\log\alpha+2\pi i\nu}{\log r}\ \big|\ \alpha\in\operatorname{Sp}(\phi^*\mid H^i(S,\mathbb C)),\ \nu\in\mathbb Z\Big\}.
$$
**El espectro del generador infinitesimal está completamente determinado por la monodromía** $\phi^*$ sobre la cohomología de la fibra $S$. Consecuencia [DATO]: **"el espectro de longitudes de órbitas cerradas NO puede ser arbitrario"** — no se puede construir un flujo foliado con un conjunto prescrito libremente de longitudes de órbitas; están **forzadas por la geometría de la fibra y la monodromía**.

**[CÁLCULO] Por qué esto es un obstáculo real para $\operatorname{Spec}\mathbb Z$.** El programa pide órbitas cerradas de longitudes **exactamente** $\{\log p:p\text{ primo}\}$ con multiplicidades correctas. El resultado 1712.04181 dice que en la clase más manejable (suspensiones) **el conjunto de longitudes es rígido** — determinado por los autovalores de la monodromía, que son algebraicos/raíces de unidad típicamente, **NO** un conjunto como $\{\log 2,\log 3,\log 5,\dots\}$ con sus densidades aritméticas. **Esto NO prueba la no-existencia**, pero muestra que las construcciones "fáciles" (suspensiones) **no pueden** dar el espectro aritmético: el espacio de $\operatorname{Spec}\mathbb Z$, si existe, **no es una suspensión** — debe ser un objeto laminado genuinamente más complejo (un "solenoide" / espacio laminado no fibrado), y ahí la teoría de Hodge foliada es mucho menos comprendida. [CÁLCULO sobre DATO]

**[ANALOGÍA con Doc 126/119]** Esta rigidez espectral es **la misma tensión** que T2 de Doc 119 (signaturas no continuas bajo límites) y que la infinitud de Doc 126 §2.4, vista desde el lado dinámico: el espectro deseado $\{\log p\}$ es "denso y aritmético", incompatible con los espectros rígidos de las foliaciones manejables.

### 4.3. La cohomología infinito-dimensional [DATO] — obstáculo y ventaja

**[DATO]** La cohomología foliada es genéricamente de **dimensión infinita** y "no topológica sino muy analítica" — Theorem 2.1 de 1712.04181: $\bar H^i_{\mathcal F}(M)\cong C^\infty_\phi(\mathbb R,H^i(S))$, espacios de dimensión infinita [DATO]. 

**[CÁLCULO] Doble filo:** (i) **obstáculo:** la dualidad de Poincaré, la traza, la signatura sobre un espacio de dimensión infinita son delicadas (necesitan reducción/regularización — la innovación de 2402.06671 de usar DOS cohomologías reducidas es precisamente para que las trazas converjan). Coincide con R-SIG ≺ R-FIN (Doc 119). (ii) **VENTAJA (ya señalada §3.3):** a diferencia de AHK (finito, Doc 126), Deninger **ya opera en dimensión infinita** — su teoría de Hodge foliada y su fórmula de trazas están construidas para ese régimen. El obstáculo de Doc 126 (la infinitud mata AHK) **no se aplica al método de Deninger**.

### 4.4. Resumen de estado: qué se ha probado, qué sigue conjetural

**[DATO — tabla de estado, honesta]:**

| Pieza | Estatus |
|---|---|
| Formalismo cohomológico (cohomología $\Rightarrow$ ec. funcional, fórmula explícita) | **PROBADO condicional** (Deninger 90s) |
| Fórmula explícita = traza de Lefschetz, ejemplo simple completo | **PROBADO** (math/0204194) |
| Estructura de Hodge polarizable + Hard Lefschetz + positividad, caso Kähler–Riemann | **PROBADO** (math/0204111) |
| Fórmula de trazas para flujos foliados, variedades reales | **PROBADO 2024** (Álvarez López–Kordyukov–Leichtnam, 2402.06671) |
| Relación Deninger ↔ Connes–Consani (cuerpos abelianos, sólo espacio+flujo) | **PROBADO 2025** (Morishita, 2508.15971), mapa anti-equivariante, NO iso |
| Espacio foliado para curvas / curva elíptica | **realizado** (caso geométrico) |
| **Espacio foliado para $\operatorname{Spec}\mathbb Z$ con órbitas $\{\log p\}$ y cohomología $=$ ceros** | **ABIERTO / existencia desconocida** |
| Que ese espacio sea Kähler–Riemann (⟹ positividad ⟹ RH) | **CONJETURA-DENINGER, no probado** |
| Obstrucción: espectro de órbitas rígido en suspensiones | **PROBADO** (1712.04181) ⟹ el espacio no es una suspensión simple |

---

## 5. SÍNTESIS CON EL DOC 127 (Hodge dinámica / Forni)

**[CÁLCULO — la unificación que el encargo pide].** Doc 127 ataca el mismo muro desde Teichmüller/Forni; Doc 128 (éste) desde foliaciones/Deninger. **Son el mismo objeto-meta visto de dos lados.** El mapeo:

| | Doc 127 (Forni / Teichmüller) | Doc 128 (Deninger / foliaciones) |
|---|---|---|
| El flujo $\mathbb R$ | flujo de Teichmüller / flujo geodésico de Weil–Petersson | flujo $\phi^t$ sobre el espacio laminado |
| El fibrado de Hodge | el fibrado de Hodge sobre el espacio de móduli, cociclo de Kontsevich–Zorich | la cohomología foliada $\bar H^1_{\mathcal F}$ con su estructura de Hodge a lo largo de las hojas |
| La positividad | **no-anulación / signo de los exponentes de Lyapunov** del cociclo (Forni: probado por ergodicidad del flujo de Teichmüller) | **polarización de Hodge–Riemann** sobre $\bar H^1_{\mathcal F}$ (Deninger: probado en caso Kähler–Riemann) |
| Cómo se prueba la positividad | **ergodicidad externa** del flujo (Forni, Avila–Viana): teorema dinámico, no asume nada de $\zeta$ | **teoría de Hodge a lo largo de las hojas** (Álvarez López–Kordyukov): teorema geométrico, no asume nada de $\zeta$ |
| Test de no-circularidad | la positividad de Lyapunov es **externa** a $\zeta$ (propiedad del flujo) | la polarización es **externa** a $\zeta$ (propiedad de Hodge de las hojas) |

**[CONJETURA-NUESTRA — el OBJETO-META UNIFICADO].**

> **OBJETO-META (Phase 42).** *Un flujo $\mathbb R$ ergódico/parcialmente hiperbólico $\phi^t$ sobre un espacio laminado $X$ (el análogo de $\operatorname{Spec}\mathbb Z$ con flujo), portando un **fibrado de Hodge** $\bar H^1_{\mathcal F}$ a lo largo de las hojas, tal que la **positividad de Hodge–Riemann sobre el primitivo** se sigue, **externamente a $\zeta$**, de la combinación de:*
> *(i) **teoría de Hodge a lo largo de las hojas** (estructura tipo Kähler–Riemann ⟹ polarización, vía Álvarez López–Kordyukov) — el lado de Deninger;*
> *(ii) **ergodicidad/hiperbolicidad del flujo transverso** (no-anulación de los exponentes de Lyapunov del cociclo de Hodge, vía Forni/Avila–Viana) — el lado de Forni;*
> *de modo que la positividad NO se lee sobre la traza del flujo (que sería la fórmula explícita = circular, NC3), sino sobre la **monodromía de Hodge del fibrado** (geométrica, NC3-pasa). Esta positividad ES nuestra negatividad definida sobre el primitivo (G2 = índice de Hodge sobre el cuadrado, vía la dualidad índice-de-Hodge ⟺ polarización de §2.4).*

**[CÁLCULO] Su test de no-circularidad.** El objeto-meta pasa R-NC **si y sólo si** la positividad se establece por (i)+(ii) —Hodge de las hojas + ergodicidad del flujo— **sin evaluar la traza sobre las funciones test de $\zeta$**. Ambos lados (Forni y Deninger) tienen esta propiedad **en sus casos probados** (Teichmüller: la positividad de Lyapunov es un teorema ergódico; Kähler–Riemann: la polarización es un teorema de Hodge). **El gap unificado es el mismo:** que el espacio de $\operatorname{Spec}\mathbb Z$ (a) exista, y (b) sea del tipo donde (i)+(ii) aplican (Kähler–Riemann + ergódico). **NÚCLEO-128 = el gap de Doc 127, fusionados.**

**[CONJETURA-NUESTRA] La apuesta de Phase 42:** que **el cuadrado del sitio de escala de Doc 125 sea una sombra tropical/característica-1 de este objeto-meta**, y que la signatura $(1,2)$ del juguete finito (Doc 125 §5, el resultado positivo más fuerte del programa hasta ahora) sea **la huella de la polarización de Hodge–Riemann foliada** — es decir, que G-125.B (la persistencia de la signatura) se cierre **no** por geometría tropical (que Babaee–Huh obstruye, Doc 126), sino por **teoría de Hodge dinámica** (Forni + Deninger), que es el régimen infinito-dimensional correcto.

---

## 6. VEREDICTO

### 6.1. Clasificación (a)/(b)/(c)/(d)

**[CÁLCULO] Veredicto: (a) marco no circular — pero NO construido, y con obstrucción de realización conocida.** Desglose:

- **¿Provee el marco no circular?** **SÍ, en su forma lógica.** A diferencia de CC (circular, positividad espectral = Weil = RH, FALLA NC3, Doc 124), el programa de Deninger establece la positividad-RH como **consecuencia de la existencia del espacio** (de tipo Kähler–Riemann), vía un **teorema** (math/0204111: la polarización de Hodge–Riemann foliada es geométrica, no postulada). **Construir el espacio correcto daría RH SIN asumir positividad=RH.** Pasa NC1, NC2, NC3, NC4 en el caso Kähler–Riemann. **Es (a), no (b).**

- **¿Es circular?** **NO**, en contraste explícito con CC. La positividad de Deninger es de Hodge (geométrica), no espectral (de la traza). Éste es el hallazgo que distingue Doc 128 de Docs 124–126: **había un marco donde la positividad NO es circular, y es el de Deninger.**

- **¿Está obstruido?** **PARCIALMENTE.** No hay no-existencia probada, pero sí (i) el espacio de $\operatorname{Spec}\mathbb Z$ no existe / existencia desconocida, y (ii) **una obstrucción de rigidez espectral probada** (1712.04181): las construcciones simples (suspensiones) NO pueden dar el espectro de longitudes $\{\log p\}$ — el espacio debe ser un laminado genuinamente complejo (solenoide), donde la teoría de Hodge foliada está mucho menos desarrollada. No es (c) "obstruido por no-existencia", pero la realización es genuinamente difícil.

- **¿Indeterminable?** **NO del todo (d):** el estatus lógico ES determinable y favorable (no circular); lo indeterminado es sólo la **realización geométrica** (existe el espacio Kähler–Riemann para $\operatorname{Spec}\mathbb Z$?).

**Veredicto compuesto: (a) con realización abierta y obstrucción de rigidez conocida** — estructuralmente **mejor** que el veredicto (b)/(d) de Docs 124–126 para CC/AHK, porque el marco de Deninger evade la circularidad (positividad geométrica de Hodge, no espectral) Y evade la infinitud que mata AHK (opera en dimensión infinita desde el origen).

### 6.2. ¿Hay un primer teorema concreto, construible, en esta línea?

**[CONJETURA-NUESTRA — el deliverable accionable].** SÍ, y NO es RH ni el espacio completo. Es:

> **PRIMER-TEOREMA-128 (construible).** *Verificar si el cuadrado del sitio de escala (Doc 125) — o, mejor, el espacio de Morishita $\mathfrak X_F$ (2508.15971) que ya identifica el flujo y las órbitas — admite una estructura de **Hodge polarizable foliada** (de tipo Kähler–Riemann, o un análogo de característica 1 vía la descomposición de Álvarez López–Kordyukov adaptada a láminas tropicales). Si la admite, entonces la signatura $(1,2)$ del juguete finito de Doc 125 §5 se eleva a un **teorema de polarización de Hodge–Riemann sobre $\bar H^1_{\mathcal F}$**, y G-125.B se cierra por GEOMETRÍA DE HODGE (no por la traza del flujo) — evadiendo NC3.*

**[CÁLCULO] Por qué es construible y por qué importa:** (i) el espacio (Morishita) y el flujo ya existen como objetos; (ii) la maquinaria de Hodge foliada (Álvarez López–Kordyukov) y la de trazas (2402.06671) ya son teoremas en el caso real; (iii) lo que falta es **un puente**: o bien dotar al espacio de Morishita de una estructura Kähler–Riemann (o probar que NO la admite — que también sería un resultado decisivo, empujando hacia (c)), o bien adaptar la descomposición de Hodge foliada al caso laminado/tropical de característica 1. **Éste es un problema acotado, con todos los ingredientes identificados** — exactamente el tipo de "matemática nueva para cruzar el muro" que Phase 42 busca.

**[CÁLCULO] La diferencia decisiva con Phase 41:** Phase 41 (Docs 124–126) buscó la positividad **del lado tropical/intersección** (cuadrado del sitio de escala, paquete de Kähler tropical) y chocó con Babaee–Huh (índice de Hodge tropical NO automático) + la infinitud que mata AHK. **Phase 42 / Deninger relocaliza la positividad al lado de Hodge dinámico-foliado**, donde (a) la positividad es geométrica genuina (math/0204111), (b) la dimensión infinita es el régimen nativo (no un obstáculo), (c) Babaee–Huh no aplica (no es geometría tropical de intersección sino Hodge analítica de hojas). **El muro de Phase 41 es tropical; Deninger ofrece rodearlo por lo analítico-foliado.** Ése es el sentido del giro de Phase 42.

---

## 7. Síntesis y honestidad

Ningún teorema nuevo se probó aquí. Se **leyó en fuente** (Deninger ICM 1998 + survey 0709.2801 + DLSDeninger; math/0204111 estructuras de Hodge polarizables foliadas; math/0204194 ejemplo simple; Leichtnam 1307.3851; Álvarez López–Kordyukov–Leichtnam 2402.06671 fórmula de trazas 2024; 1712.04181 rigidez espectral; Morishita 2508.15971 relación con CC) y se **calculó** la identificación con nuestro programa.

**Lo central:** el programa de Deninger es el primer marco encontrado en todo el programa RH donde **la positividad que da RH NO es circular** — es una consecuencia geométrica de la existencia del espacio correcto (teorema en el caso Kähler–Riemann), no la positividad de Weil renombrada (que es el destino circular de CC, Doc 124). El precio es que **el espacio para $\operatorname{Spec}\mathbb Z$ no existe**, hay **obstrucción de rigidez espectral** (las suspensiones simples no dan $\{\log p\}$), y la realización es un problema genuinamente abierto. Pero el marco **evade los dos muros de Phase 41**: la circularidad (positividad de Hodge, no espectral) y la infinitud (régimen nativo de Deninger, no obstáculo). La síntesis con Doc 127 es total: Forni y Deninger son **el mismo objeto-meta** —flujo $\mathbb R$ con fibrado de Hodge cuya positividad se prueba externamente (ergodicidad / Hodge de hojas)— y ese objeto-meta es la matemática nueva que Phase 42 debe construir. **El punto de traba se ha movido del "índice de Hodge tropical" (Phase 41, obstruido por Babaee–Huh) al "estructura de Hodge polarizable foliada sobre el espacio de Morishita" (Phase 42, abierto pero no circular ni obstruido por infinitud)** — y ése es el primer teorema concreto a atacar.

---

## Referencias

**Fuente primaria leída esta sesión (junio 2026, vía WebSearch/WebFetch):**
- C. Deninger, *Some analogies between number theory and dynamical systems on foliated spaces*, Proc. ICM Berlin 1998, Doc. Math. Extra Vol. ICM I, 163–186 — el diccionario flujo/Frobenius, primos = órbitas cerradas $\log p$, arquimediano = puntos fijos, fórmula explícita = traza de Lefschetz. **[DATO/CONJETURA-DENINGER]**
- C. Deninger, *Analogies between analysis on foliated spaces and arithmetic geometry*, arXiv:0709.2801 — survey; "RH would be a consequence of properties parallel to the positivity of the intersection pairing in Hodge theory". **[DATO]**
- C. Deninger, *Arithmetic geometry and analysis on foliated spaces* (Arizona Winter School, DLSDeninger.pdf) — exposición del programa. **[DATO]**
- C. Deninger, *Real polarizable Hodge structures arising from foliations*, arXiv:math/0204111 — **PRUEBA** estructura de Hodge polarizable, Hard Lefschetz, positividad de Hodge–Riemann sobre cohomología foliada reducida de foliaciones Kähler–Riemann; análogo de Serre de Weil. **El teorema que hace NO circular al programa.** **[DATO]**
- C. Deninger, *On the nature of the explicit formulas in analytic number theory — a simple example*, arXiv:math/0204194 — ejemplo dinámico completo donde la fórmula explícita ES una traza de Lefschetz. **[DATO]**
- E. Leichtnam, *On the analogy between L-functions and Atiyah–Bott–Lefschetz trace formulas for foliated spaces*, arXiv:1307.3851 — axiomas para el espacio foliado de cuerpos de números; prueba fórmula ABL para fibrados de línea ramificados sobre foliaciones Riemannianas; espacio "existence still unknown". **[DATO]**
- J. A. Álvarez López, Y. A. Kordyukov, E. Leichtnam, *A trace formula for foliated flows*, arXiv:2402.06671 (2024) — **PRUEBAN** la fórmula de trazas de Lefschetz para flujos foliados en variedades cerradas reales (codim 1), usando DOS cohomologías foliadas reducidas; **resuelve una conjetura de Deninger**. **[DATO — la maquinaria analítica existe.]**
- (autor del paper sobre fibrados sobre el círculo), arXiv:1712.04181, *On the leafwise cohomology and dynamical zeta functions for fiber bundles over the circle* — cohomología foliada infinito-dimensional ($\bar H^i_{\mathcal F}\cong C^\infty_\phi(\mathbb R,H^i(S))$); **Theorem 3.2: el espectro del generador está forzado por la monodromía — el espectro de longitudes NO es arbitrario (obstrucción de rigidez).** **[DATO]**
- M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*, arXiv:2508.15971 (2025) — Theorem 3.6: mapa continuo $\mathbb R_+$-**anti**-equivariante y Galois-equivariante entre el sistema de Deninger y el espacio adélico de CC para cuerpos abelianos; **NO isomorfismo**; órbitas/primos se corresponden; cohomología y positividad **NO** desarrolladas. **[DATO — Deninger y CC son dos programas distintos que convergen sólo en el espacio+flujo.]**
- M. Flach, B. Morin, *Deninger's conjectures and Weil–Arakelov cohomology* — realización parcial incondicional de aspectos del formalismo. **[DATO, vía abstract]**

**Internas (backward-only):** Doc 119 (R-NC NC1–NC4; cuantificador maestro P43; R-SIG ≺ R-FIN; tensiones T2/T3/T4; R-LEF-FLUJO); Doc 123 (Künneth tropical no existe; C-rank); Doc 124 (positividad de CC = espectral = MW-1 = circular; positividad-intersección [BUENA] vs positividad-espectral [CIRCULAR]); Doc 125 (forma de intersección sobre el cuadrado; $G_{\text{toy}}$ signatura $(1,2)$; flujo $\Delta_\mu$; gaps G-125.A/B; NC3 vía traza del flujo); Doc 126 (AHK no aplica por infinitud; Babaee–Huh obstruye; el núcleo = "subtipo matroidal/Lefschetz externo a $\zeta$"); Doc 127 (Hodge dinámica/Forni — síntesis en §5); roadmap-rh (el cuantificador maestro, G1–G4).

*Fin del Doc 128.*
</content>
</invoke>
