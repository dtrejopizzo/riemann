# Doc 127 — Teoría de Hodge dinámica como marco del paquete de Kähler foliado: el precedente de Forni / Eskin–Kontsevich–Zorich y el test de circularidad

**Programa:** Hipótesis de Riemann — Phase 42: matemática nueva para cruzar el muro (la positividad de Hodge sobre el cuadrado con flujo continuo).
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 126 (AHK no aplica por flujo continuo + infinitud; Babaee–Huh obstruye genéricamente; el núcleo = paquete de Kähler tropical-FOLIADO; el veredicto (d) con sesgo a (b)/(c); la diferencia "algebraico = índice gratis" vs "tropical = índice a probar"); Doc 125 (la forma de intersección de Allermann–Rau sobre $C_p\times C_p$; el juguete con $G_{\text{toy}}=\begin{psmallmatrix}0&1&1\\1&0&1\\1&1&0\end{psmallmatrix}$, signatura $(1,2)$, primitivo definido negativo; G-125.A real/entero; G-125.B persistencia de signatura à la Babaee–Huh; la vía (c) traza-del-flujo = fórmula de Lefschetz = circular FALLA NC3); Doc 119 (R-SIG/R-FIN/R-LEF/R-PESO; R-LEF-FLUJO; test R-NC NC1–NC4; tensiones T2 "signaturas no son continuas bajo límites", T3 "cuanto más explícita la traza, mayor riesgo de que la geometría SEA la fórmula explícita"); P43 (cuantificador maestro: valor/inercia — el VALOR de un funcional cuadrático se computa de los primos solos, pero su INERCIA / partición del índice negativo en bloques no se determina sin las posiciones de los ceros; la barrera media→uniforme).

**TRABAJO EN PARALELO / META DEL DOC:** este documento NO intenta probar la positividad de Hodge sobre el cuadrado. Establece SI la **teoría de Hodge dinámica** (cociclo de Kontsevich–Zorich sobre el flujo de Teichmüller; teorema de Forni; Eskin–Kontsevich–Zorich) es el **marco correcto** para el paquete de Kähler foliado que falta (G-125.B), QUÉ teorema de ella es el análogo de "la signatura persiste", y —crítico— si esa positividad sería **NO-CIRCULAR** (externa a ζ, como Forni) o **colapsa a RH** (porque el flujo del sitio de escala lleva ζ adentro). Si colapsa, ese es el resultado.

**Disciplina de etiquetado (regla absoluta, máximo riesgo de falsa victoria):** **[DATO]** = leído en fuente esta sesión (con cita) o teorema interno probado (cita backward-only). **[ANALOGÍA]** = correspondencia estructural que propongo, con grado de ajuste explícito: **tight** (misma estructura matemática) / **parcial** (análoga con diferencias nombradas) / **especulativa** (forzada). **[CÁLCULO]** = derivación mía. **[GAP]**, **[CONJETURA]**, **[NO VERIFICADO]** = como se indican. **NUNCA "probado"** salvo lo genuino.

---

## 0. Resumen ejecutivo

El precedente de teoría de Hodge dinámica es el único corpus donde una **positividad/gap de signatura de un fibrado de Hodge con forma indefinida** se probó por un método **externo, variacional-ergódico** (Forni 2002; Kontsevich–Forni; EKZ 2014) — no asumiendo nada sobre el objeto que se quiere acotar. Es exactamente la arquitectura que Doc 126 §5.3 pedía como "lo que faltaría" para mover G2 de (b)/(d) hacia (a): una positividad **que sobregenere** y venga de afuera. Por eso es el candidato más serio a marco del paquete de Kähler foliado.

**Hallazgos centrales:**

1. **El precedente es real y la estructura es sorprendentemente cercana (§1, §2).** El fibrado de Hodge $H^1$ sobre el espacio de móduli lleva una forma de intersección **simpléctica indefinida** (la misma categoría que nuestra forma de intersección de signatura $(1,\rho-1)$); el cociclo de Kontsevich–Zorich es la acción de un **flujo** (Teichmüller) sobre ese fibrado; y Forni prueba un **gap espectral** ($\lambda_2<\lambda_1$) y la **no-anulación** de exponentes por una **fórmula de curvatura** (Kontsevich–Forni: $\lambda_1+\dots+\lambda_g=\int \mathrm{tr}(B_\omega B_\omega^*)\,d\mu$) integrada contra la **medida de Masur–Veech**. Varias flechas de la analogía son **tight**: forma indefinida↔forma indefinida; cociclo sobre flujo↔transporte $\Delta_\mu$; positividad de curvatura↔índice de Hodge. [DATO + ANALOGÍA tight]

2. **PERO la analogía se rompe en DOS puntos estructurales, ambos decisivos (§2.4, §4):**
   - **(R1) ergodicidad/hiperbolicidad:** el flujo de Teichmüller es **no-uniformemente hiperbólico y ergódico/mixing** respecto de una medida (Masur–Veech) que es **geometría pura del espacio de móduli**. El flujo $\mathbb R_+^*$ del sitio de escala es una **traslación isométrica** (rotación irracional sobre $C_p$), **NO hiperbólica**, sin exponentes de Lyapunov no triviales propios. La analogía "exponentes de Lyapunov ↔ ceros de ζ" es **especulativa**, y donde se intentaría hacerla tight (§2.3) recae sobre la fórmula de traza de Connes.
   - **(R2, EL DECISIVO) la fuente de la medida:** la medida de Masur–Veech se define por la **geometría plana de las superficies de traslación**, ANTES de cualquier función L. La "ergodicidad/curvatura" del sitio de escala que daría la positividad-análoga **NO es geometría externa**: la traza distribucional del flujo $\mathbb R_+^*$ **ES** el lado aritmético de la fórmula explícita de Weil (Connes 1999; R-LEF-FLUJO Doc 119) — el flujo **lleva ζ adentro**. [DATO + CÁLCULO]

3. **El análogo de "la signatura persiste" (§3):** sería un **gap espectral de Forni foliado** — un enunciado de que la forma de intersección del cuadrado, transportada por el cociclo del flujo $\mathbb R_+^*$, conserva su signatura $(1,\rho-1)$ porque la **forma de curvatura del fibrado de Hodge foliado es semidefinida del signo correcto** (no-anulación del "segundo exponente" = ausencia de direcciones positivas en exceso sobre el primitivo = ausencia de cuádruplos off-críticos $m=\kappa(Q)/2=0$). Enunciado preciso en §3.3.

4. **El test de circularidad (§4) — la pregunta más importante del doc, RESPUESTA NÍTIDA:** en Teichmüller, la positividad de Forni es **externa** porque el flujo es geometría pura (espacios de móduli de superficies planas) y la medida de Masur–Veech NO conoce ninguna función L; la curvatura del fibrado de Hodge se calcula de la **estructura compleja variable**, externa al objeto acotado. En el sitio de escala, **el flujo $\mathbb R_+^*$ NO es geometría pura: está definido de modo que su traza reproduce $\sum_p\log p\cdot(\dots)$ = el lado de primos de la fórmula explícita**, y la "curvatura/medida" que daría la positividad-Forni-análoga es, vía la fórmula de Weil, **secretamente equivalente a la cancelación ceros↔primos = RH**. **El flujo lleva ζ adentro.** Por tanto la positividad-Forni-análoga **es circular** (recae en P43: el VALOR del funcional es externo —se computa de los primos— pero su INERCIA/signatura es la posición de los ceros).

5. **VEREDICTO (§5): (b) — marco correcto pero CIRCULAR**, con un matiz de (c) en la flecha de hiperbolicidad. La teoría de Hodge dinámica es el marco **estructuralmente correcto** (el único precedente de positividad-de-fibrado-de-Hodge-indefinido por método externo) — y eso es informativo, valida la dirección de Doc 126 §5.3. Pero la **fuente de externalidad** de Forni (medida geométrica de móduli ajena a ζ) **no tiene análogo no-circular** en el sitio de escala, porque el flujo del sitio de escala **es** el flujo cuya traza es la fórmula explícita. La diferencia exacta: **el flujo de Teichmüller es geometría; el flujo del sitio de escala es la fórmula explícita disfrazada de geometría.** Esto es la tensión T3 de Doc 119 en su forma más aguda, y coincide con el veredicto NC3 de Doc 125 §6.3 (la vía traza-del-flujo = Lefschetz = circular) por una cuarta ruta independiente.

---

## 1. EL PRECEDENTE [DATO, fijado con precisión]

### 1.1. El fibrado de Hodge y su forma de intersección indefinida

**[DATO]** (Forni, *Deviation of ergodic averages for area-preserving flows on surfaces of higher genus*, Annals of Math. (2) 155 (2002) 1–103; survey Forni *On the Lyapunov exponents of the Kontsevich–Zorich cocycle*, Handbook of Dynamical Systems vol. 1B, cap. 8; Matheus, *Disquisitiones Mathematicae*, notas Bourbaki Hubert 2012; confirmado WebSearch/WebFetch esta sesión.)

Sea $\mathcal H_g$ (o un estrato $\mathcal H(\kappa)$) el espacio de móduli de **superficies de traslación** = pares $(X,\omega)$ con $X$ superficie de Riemann de género $g$ y $\omega$ una 1-forma holomórfica (diferencial abeliana) con divisor de ceros de tipo $\kappa$. Sobre $\mathcal H_g$ vive el **fibrado de Hodge** $H^1$: la fibra sobre $(X,\omega)$ es $H^1(X,\mathbb R)$ (real, de rango $2g$), o su complexificación $H^1(X,\mathbb C)=H^{1,0}\oplus H^{0,1}$.

- **Forma de intersección.** Sobre $H^1(X,\mathbb R)$ está la **forma de intersección simpléctica** (producto cup) $\langle\alpha,\beta\rangle=\int_X\alpha\wedge\beta$, **antisimétrica, no degenerada** (Poincaré). Su complexificada, restringida a la parte holomorfa con el signo de Hodge, da la **forma hermitiana de Hodge** $h(\alpha,\beta)=\tfrac{i}{2}\int_X\alpha\wedge\bar\beta$, que es **positiva-definida sobre $H^{1,0}$ (formas holomorfas) y negativa-definida sobre $H^{0,1}$** — es decir, de **signatura $(g,g)$**, **INDEFINIDA**. [DATO]

> **Punto que fijo para toda la analogía:** la forma natural del fibrado de Hodge es **INDEFINIDA** (signatura $(g,g)$ en la versión hermitiana; simpléctica en la real). Es la **misma categoría** que nuestra forma de intersección del cuadrado, signatura $(1,\rho-1)$ (Doc 124, Doc 125 §5.1). Esto es lo que hace que el precedente sea pertinente y no una falsa pista: ambos mundos son de **positividad-sobre-un-subespacio dentro de una forma indefinida**, no de positividad global.

### 1.2. El cociclo de Kontsevich–Zorich (la acción del flujo sobre $H^1$)

**[DATO].** El **flujo de Teichmüller** $g_t$ actúa sobre $\mathcal H_g$ por $g_t\cdot(X,\omega)=(X,e^{t}\,\Re\omega+i\,e^{-t}\,\Im\omega)$ — estira la dirección horizontal por $e^t$ y contrae la vertical por $e^{-t}$ (es la parte diagonal de la acción $SL(2,\mathbb R)$ sobre las superficies planas). El **cociclo de Kontsevich–Zorich** $G_t^{KZ}$ es la acción de $g_t$ sobre el fibrado de Hodge, vía el **transporte paralelo de Gauss–Manin** de la cohomología a lo largo de la órbita de Teichmüller, **renormalizado** por el flujo. [DATO]

- $G_t^{KZ}$ es un **cociclo simpléctico** (preserva la forma de intersección $\langle\cdot,\cdot\rangle$): el transporte de Gauss–Manin preserva la estructura entera $H^1(X,\mathbb Z)$ y la forma cup. [DATO — **esta es la propiedad clave para la analogía**: el cociclo del flujo **preserva la forma indefinida**, igual que pediremos del flujo $\mathbb R_+^*$ sobre el cuadrado.]
- Los **exponentes de Lyapunov** del cociclo (respecto de una medida $g_t$-invariante ergódica $\mu$) forman un espectro simétrico
$$ 1=\lambda_1\ge\lambda_2\ge\dots\ge\lambda_g\ge 0\ge-\lambda_g\ge\dots\ge-\lambda_1=-1 $$
(simétrico por la simplicidad simpléctica; $\lambda_1=1$ siempre, dirección "tautológica" del propio $\omega$). [DATO]

### 1.3. El teorema de Forni: no-anulación y gap, por método EXTERNO

**[DATO]** (Forni 2002 Annals; Kontsevich–Forni formula; confirmado WebFetch Matheus esta sesión.) Los dos enunciados que importan:

**(F1) No-anulación / hiperbolicidad del cociclo KZ.** Para la **medida de Masur–Veech** $\mu_{MV}$ (la medida natural, absolutamente continua, sobre el estrato), **todos los exponentes de Lyapunov son no nulos**: $\lambda_g>0$. El cociclo KZ es **no-uniformemente hiperbólico** (Pesin); el número de exponentes estrictamente positivos es exactamente $g$ (= la mitad simpléctica). [DATO]

**(F2) Gap espectral.** Forni prueba que para medidas ergódicas sobre el **estrato principal**, $\lambda_2<\lambda_1=1$ — **gap estricto** bajo el exponente tautológico. [DATO]

**(F3) — EL MECANISMO, lo decisivo para el test de circularidad.** La prueba es **variacional-ergódica vía una fórmula de curvatura**, NO una hipótesis sobre los exponentes. La **fórmula de Kontsevich–Forni**:
$$ \lambda_1^\mu+\lambda_2^\mu+\dots+\lambda_g^\mu \;=\; \int_{\mathcal H} \big(\Lambda_1(\omega)+\dots+\Lambda_g(\omega)\big)\,d\mu(\omega), $$
donde $\Lambda_i(\omega)$ son los **autovalores de la matriz $H_\omega=B_\omega B_\omega^*$**, y $B_\omega$ es la **segunda forma fundamental** (mapa de Kodaira–Spencer) del subfibrado holomorfo $H^{1,0}\subset H^1\otimes\mathbb C$ con la conexión de Gauss–Manin. [DATO]

**[DATO] Por qué el lado derecho es $\ge 0$ — la fuente de la positividad.** El integrando $\mathrm{tr}(B_\omega B_\omega^*)\ge 0$ porque es la traza de $B B^*$ con $B^*$ el **adjunto respecto del producto hermitiano de Hodge, que es definido positivo sobre $H^{1,0}$** (§1.1). Es la **forma de curvatura del fibrado de Hodge**, una $(1,1)$-forma **semidefinida positiva** por construcción geométrica. La positividad de los exponentes (y el gap) sale de **integrar una curvatura no negativa contra la medida invariante** — un argumento de geometría diferencial + ergodicidad, **que no usa ninguna información sobre los $\lambda_i$ que se quiere concluir.** [DATO — **esta es la externalidad pura que hay que comparar**.]

### 1.4. Eskin–Kontsevich–Zorich: la suma de exponentes = geometría

**[DATO]** (Eskin–Kontsevich–Zorich, *Sum of Lyapunov exponents of the Hodge bundle with respect to the Teichmüller geodesic flow*, Publ. Math. IHÉS 120 (2014) 207–333; arXiv:1112.5872; confirmado WebSearch esta sesión.) La fórmula:
$$ \lambda_1+\dots+\lambda_g \;=\; \kappa_\mu \;+\; \frac{\pi^2}{3}\,c_{\mathrm{area}}(\mathcal C), $$
donde $\kappa_\mu$ es una **combinación explícita de los órdenes de los ceros de $\omega$** (un término de "grados de fibrados de líneas" sobre el estrato — clases tautológicas / de Lyapunov = grados) y $c_{\mathrm{area}}(\mathcal C)$ es la **constante de Siegel–Veech** del componente (cuenta asintótica de cilindros/conexiones de silla — geometría de conteo de órbitas periódicas). [DATO]

> **Lo que EKZ fija para nosotros:** la suma de exponentes es un **invariante geométrico-topológico** (grados de fibrados + conteo de Siegel–Veech), calculable **sin** integrar el cociclo, **sin** conocer los exponentes individuales. Es el caso modelo de "una positividad/cota espectral reducida a geometría externa". El tipo de teorema que Doc 126 §5.3 punto 2 pedía: un invariante de la estructura que da la signatura, externo al objeto acotado.

**[DATO — qué tipo de positividad/signatura prueban y cómo, resumido]:** Forni/KF/EKZ prueban **no-anulación y gap de un espectro de Lyapunov de un cociclo simpléctico sobre un fibrado de forma indefinida**, por **(i) ergodicidad del flujo respecto de Masur–Veech + (ii) una fórmula de curvatura semidefinida positiva (Kontsevich–Forni) + (iii) una identificación de la suma con grados geométricos (EKZ)**. La fuente es **externa**: la medida y la curvatura se definen por la **geometría plana / estructura compleja variable** de las superficies, sin ninguna hipótesis sobre los exponentes ni ninguna función L.

---

## 2. LA ANALOGÍA [ANALOGÍA, grado de ajuste honesto, flecha por flecha]

Construyo el diccionario candidato y clasifico cada flecha como **tight / parcial / especulativa**.

### 2.1. Tabla de correspondencia

| Objeto de Teichmüller | Objeto del sitio de escala | Ajuste |
|---|---|---|
| Espacio de móduli $\mathcal H_g$ de superficies de traslación | (¿) el "espacio de móduli" del cuadrado / familia de las $C_p\times C_p$ | **parcial** (§2.2) |
| Flujo de Teichmüller $g_t$ (geodésico, hiperbólico) | Flujo de escala $\mathbb R_+^*$, $u\mapsto u+\log\mu$ | **especulativa** (§2.4) — el punto de ruptura R1 |
| Fibrado de Hodge $H^1$, forma simpléctica/hermitiana INDEFINIDA $(g,g)$ | Forma de intersección del cuadrado, signatura $(1,\rho-1)$ | **tight** (§2.1bis) |
| Cociclo KZ $G_t^{KZ}$ (Gauss–Manin, preserva la forma) | Transporte de las correspondencias $\Delta_\mu$ por el flujo (preserva $D\cdot D'$) | **parcial→tight** (§2.3) |
| Medida de Masur–Veech $\mu_{MV}$ (geometría plana, ergódica) | (¿) medida invariante del flujo $\mathbb R_+^*$ = medida de Haar de $\mathbb R_+^*$ / tipo II | **parcial pero ENVENENADA** (§2.4, §4) |
| Exponentes de Lyapunov $\lambda_i$ | Ceros de ζ / partes imaginarias / $\kappa(Q)=2m$ | **especulativa** (§2.3) |
| Gap $\lambda_2<\lambda_1$ / no-anulación $\lambda_g>0$ | RH = signatura $(1,\rho-1)$ exacta = $m=0$ | **parcial** (§3) |
| Fórmula de curvatura de Kontsevich–Forni (externa) | (¿) una fórmula de curvatura del fibrado de Hodge foliado del cuadrado | **el deseo — el test §4 decide si existe no-circular** |

### 2.1bis. La flecha TIGHT: forma indefinida ↔ forma indefinida

**[ANALOGÍA tight].** La forma de Hodge sobre $H^1$ es indefinida (signatura $(g,g)$); nuestra forma de intersección es indefinida (signatura $(1,\rho-1)$). En **ambos** casos la positividad relevante es **sobre un subespacio**: en Forni, la positividad-de-curvatura sobre $H^{1,0}$ (el "primitivo holomorfo"); en nosotros, la definitud **negativa** sobre el primitivo $P^1=(f_1+f_2)^\perp$ (Doc 125 §5.2). La estructura "positividad de una forma definida dentro de una forma indefinida transportada por un flujo que preserva la forma indefinida" es **literalmente la misma**. Esta flecha es **tight** y es la razón por la que el precedente merece el documento. [Coincide con Doc 124 §1.1: índice de Hodge = positividad-intersección sobre el primitivo.]

### 2.2. La flecha del espacio de móduli: PARCIAL

**[ANALOGÍA parcial].** Teichmüller tiene un **espacio de móduli genuino** $\mathcal H_g$ de dimensión finita, con una **familia de objetos geométricos** (las superficies planas) sobre la que el flujo se mueve, y la **estructura compleja varía** de fibra a fibra (de ahí la curvatura no trivial del fibrado de Hodge). En el sitio de escala, el cuadrado $C_p\times C_p$ es **un objeto fijo** por primo $p$; no hay una "familia de cuadrados con estructura compleja variable" sobre la que el flujo $\mathbb R_+^*$ mueva un punto-base. El flujo $\mathbb R_+^*$ actúa **dentro** de un cuadrado fijo (traslación de la diagonal), no sobre un espacio de móduli de cuadrados.

**Consecuencia (la diferencia más profunda, alimenta §4):** en Forni la curvatura del fibrado de Hodge es **no trivial porque la estructura compleja cambia** a lo largo de la órbita (el período de Hodge $H^{1,0}\subset H^1$ rota). En el sitio de escala **no hay estructura compleja variable** — el flujo $\mathbb R_+^*$ es una **isometría** del toro tropical $C_p\times C_p$, que **no cambia la forma de intersección ni "rota el período de Hodge"**. Por tanto la fuente geométrica de la curvatura de Forni **no tiene contraparte**: no hay variación de estructura compleja que genere la segunda forma fundamental $B_\omega$. [ANALOGÍA: parcial, con una asimetría que se vuelve fatal en §4.]

### 2.3. La flecha del cociclo y de los "exponentes": PARCIAL → ESPECULATIVA

**[ANALOGÍA parcial → tight en la parte estructural].** El cociclo KZ es el transporte de la forma a lo largo del flujo, preservándola. El análogo es claro y razonable: el flujo $\mathbb R_+^*$ transporta las clases de correspondencia $\Delta_\mu$ (Doc 125 §2.4: $\Delta_\mu=\{v=u+\log\mu\}$, traslación de la diagonal), y la composición de correspondencias / la forma de intersección $D\cdot D'$ se transporta. La intersección estable de Allermann–Rau **es invariante por la traslación** (es una isometría del toro), luego el "cociclo" preserva la forma de intersección. **Esta parte estructural es tight**: hay un cociclo simpléctico-tropical del flujo. [ANALOGÍA tight para la *estructura* cociclo+forma.]

**[ANALOGÍA especulativa — la flecha "exponentes ↔ ceros", donde más se fuerza].** ¿Qué es el "espectro de Lyapunov" del cociclo del flujo $\mathbb R_+^*$? Aquí la analogía se tensa al máximo. Dos intentos:
- **(i) Identificar los exponentes con los ceros de ζ.** La traza distribucional del flujo $\mathbb R_+^*$ sobre el espacio de Hilbert de CCM **tiene como espectro precisamente las partes imaginarias de los ceros** (Connes 1999: el operador de escala $D=u\partial_u$ tiene autovalores en los ceros; la fórmula de traza da $\sum_\rho\hat h(\rho)$). En ese sentido, los "exponentes/frecuencias" del flujo de escala **SON** los ceros. Pero esto **NO es un espectro de Lyapunov** (tasas de crecimiento exponencial de un cociclo); es un **espectro de frecuencias** de un flujo isométrico. La traslación isométrica tiene **todos los exponentes de Lyapunov nulos** — espectro puramente puntual/rotacional, no hiperbólico. La flecha "exponentes de Lyapunov ↔ ceros" es por tanto **especulativa y, peor, categorialmente equivocada**: confunde espectro de Lyapunov (hiperbolicidad) con espectro de frecuencias (rotación).
- **(ii) Identificar el "exceso de direcciones positivas" $m=\kappa(Q)/2$ con un defecto del gap.** Más prometedor estructuralmente (§3): los cuádruplos off-críticos = direcciones positivas en exceso sobre el primitivo = "exponentes que cruzaron al lado equivocado". Esto es **parcial**: tiene el sabor correcto (un gap que se preserva ↔ ausencia de exceso) pero no hay un cociclo hiperbólico real que lo soporte.

### 2.4. El punto de ruptura R1: ¿es el flujo $\mathbb R_+^*$ ERGÓDICO e HIPERBÓLICO como el de Teichmüller?

**[DATO — la propiedad de Teichmüller].** El flujo de Teichmüller es **no-uniformemente hiperbólico (Pesin), ergódico y exponencialmente mixing** respecto de Masur–Veech (Veech; Avila–Gouëzel–Yoccoz para mixing exponencial; confirmado WebSearch esta sesión: "the Teichmüller flow is non-uniformly hyperbolic in the sense of Pesin theory; the Kontsevich–Zorich cocycle is non-uniformly hyperbolic, all Lyapunov exponents nonzero"). **La hiperbolicidad del flujo de base es la que genera exponentes de Lyapunov no triviales del cociclo.** [DATO]

**[CÁLCULO — la propiedad del flujo de escala].** El flujo $\mathbb R_+^*$ sobre $C_p=\mathbb R/(\log p)\mathbb Z$ es $u\mapsto u+\log\mu$: una **traslación / rotación irracional** (cuando $\log\mu/\log p\notin\mathbb Q$). Propiedades:
- **Ergódico**: sí, respecto de la medida de Haar (Lebesgue) de $C_p$ — una rotación irracional es únicamente ergódica. [CÁLCULO — pero es ergodicidad de **rotación**, no de hiperbolicidad.]
- **Mixing**: **NO** — una rotación no es mixing (tiene espectro puntual). [CÁLCULO]
- **Hiperbólico**: **NO** — es una isometría, **todos los exponentes de Lyapunov del propio flujo son nulos**. No hay direcciones estables/inestables exponenciales. [CÁLCULO]

> **R1 — LA ANALOGÍA SE ROMPE AQUÍ EN SU NIVEL DINÁMICO.** El flujo de Teichmüller es hiperbólico y mixing; el flujo $\mathbb R_+^*$ del sitio de escala es una **isometría/rotación**, no hiperbólica, no mixing. La maquinaria de Forni **necesita la hiperbolicidad del flujo de base** para que el cociclo tenga exponentes no triviales y para que la integral de curvatura contra la medida invariante tenga el contenido de "tasa de crecimiento". Sobre un flujo isométrico, **el cociclo de Hodge no crece exponencialmente** (los exponentes son nulos), y la fórmula de Kontsevich–Forni daría $\sum\lambda_i=0$ — **trivial, sin gap, sin contenido espectral**.

**[CÁLCULO] Matiz importante — dónde la analogía podría rescatarse, y por qué recae en ζ.** Se podría objetar: el flujo relevante no es la traslación sobre **un** $C_p$, sino el flujo de escala **global** sobre todo el sitio (todos los primos a la vez), cuya traza **sí** tiene contenido espectral (los ceros). En efecto: el operador de escala global $D=u\partial_u$ sobre $L^2$ de las clases adélicas (Connes) tiene un espectro rico. PERO ese espectro **no es de Lyapunov (hiperbólico) sino de frecuencias**, y —crítico— **el flujo global de escala con contenido espectral ES el flujo cuya traza es la fórmula explícita**. Es decir: en cuanto se enriquece el flujo para que tenga "espectro no trivial" como el de Teichmüller, ese enriquecimiento **es** la introducción de ζ. **R1 y R2 son la misma ruptura vista dos veces: o el flujo es isométrico (geometría pura, pero sin contenido espectral = analogía vacía), o tiene contenido espectral (pero entonces es la fórmula explícita = circular).** Esta es la disyuntiva central del documento.

---

## 3. EL ANÁLOGO DE "LA SIGNATURA PERSISTE" [el corazón]

### 3.1. Qué propiedad de Forni juega el papel de "índice de Hodge sobre el primitivo"

**[ANALOGÍA].** En Doc 124–125, G2/RH = "la forma de intersección es **definida negativa sobre el primitivo** $P^1=(f_1+f_2)^\perp$, signatura exacta $(1,\rho-1)$, sin direcciones positivas en exceso". Las **direcciones positivas en exceso** sobre el primitivo = los cuádruplos off-críticos = $m=\kappa(Q)/2$ (Doc 119; P35). RH $\iff m=0$ $\iff$ ninguna dirección positiva extra.

En el lenguaje de Hodge dinámica, el análogo natural es:
- el **primitivo** $\leftrightarrow$ el subespacio del fibrado de Hodge donde la forma de curvatura debe tener un signo;
- "ninguna dirección positiva en exceso" $\leftrightarrow$ **el gap espectral / la no-anulación**: que ningún exponente "cruce" al lado prohibido, o que la segunda forma fundamental no tenga un autovalor del signo equivocado.

### 3.2. Los tres candidatos del encargo, evaluados

**[CÁLCULO]**
- **(a) Gap espectral de Forni ($\lambda_2<\lambda_1$) ↔ la signatura.** Ajuste **parcial**. El gap de Forni dice "el segundo exponente está estrictamente bajo el primero" — un enunciado de **separación dentro del semiespectro positivo**. Su análogo sería "la única dirección positiva (la amplia $f_1+f_2$, $\lambda_1$) está estrictamente separada del resto, que es negativo (el primitivo)". Esto es **exactamente la signatura $(1,\rho-1)$**: una positiva separada de $\rho-1$ negativas. **Esta es la mejor flecha.** El gap de Forni ↔ el "1" de la signatura $(1,\rho-1)$ aislado.
- **(b) No-anulación de exponentes ($\lambda_g>0$) ↔ ausencia de ceros off-críticos.** Ajuste **especulativo**. La no-anulación dice "ningún exponente colapsa a 0" (el cociclo es hiperbólico). El análogo "ningún cero está fuera de la línea crítica" no es estructuralmente lo mismo: un cero off-crítico no es "un exponente que se anula" sino "una dirección de signatura equivocada". La flecha más natural para off-crítico es **(a)** (dirección positiva extra), no (b).
- **(c) Simplicidad del espectro (Avila–Viana) ↔ multiplicidad de ceros.** Ajuste **especulativo pero sugerente**. Avila–Viana probaron que el espectro KZ es **simple** (todos los $\lambda_i$ distintos) para Masur–Veech. El análogo "todos los ceros simples" es una conjetura clásica (simplicidad de ceros de ζ). Estructuralmente: simplicidad del espectro de Lyapunov ↔ simplicidad de los ceros. **Es la flecha más bonita**, pero (i) la simplicidad de ceros NO es RH, es ortogonal a RH; (ii) descansa sobre la identificación "exponentes ↔ ceros" que §2.3 declaró categorialmente equivocada. Queda como analogía decorativa, no operativa.

### 3.3. El enunciado preciso del análogo de "la signatura persiste"

**[CONJETURA — el enunciado que, en el marco dinámico, daría G2/RH].**

> **GAP-FOLIADO (análogo de Forni para el cuadrado).** *Sobre el fibrado de Hodge foliado del cuadrado del sitio de escala — el fibrado cuya fibra es $(A^1(X\times X), D\cdot D')$ con su forma de intersección de signatura $(1,\rho-1)$, transportado por el cociclo del flujo $\mathbb R_+^*$ — la **forma de curvatura de la métrica de Hodge** (el análogo de $B_\omega B_\omega^*$ de Kontsevich–Forni) es **semidefinida del signo que fuerza la signatura $(1,\rho-1)$ a persistir bajo el transporte**: equivalentemente, integrada contra la medida invariante del flujo, su "segundo exponente foliado" satisface el gap, de modo que el número de direcciones positivas en exceso sobre el primitivo es $m=\kappa(Q)/2=0$.*

De GAP-FOLIADO se seguiría G2 = la signatura $(1,\rho-1)$ exacta = $m=0$ = RH, exactamente como la curvatura semidefinida positiva de Forni fuerza el gap $\lambda_2<\lambda_1$. **El análogo de "la signatura persiste" es: la curvatura del fibrado de Hodge foliado tiene el signo correcto, y eso —vía integración ergódica contra la medida invariante— fuerza el gap = la signatura.** [CONJETURA, ajuste estructural parcial; la flecha operativa es 3.2(a).]

**[CÁLCULO] El paralelo con G-125.B.** GAP-FOLIADO es **exactamente** lo que Doc 125 §6.2 llamó G-125.B: "la persistencia de la signatura $(1,\rho-1)$ del juguete finito sobre la red completa de correspondencias". La teoría de Hodge dinámica **renombra G-125.B** como "gap espectral foliado vía curvatura". El valor del precedente es que **da un método candidato** (curvatura + ergodicidad) donde Doc 125 solo tenía el gap abierto. La pregunta del §4 es si ese método es externo o circular.

---

## 4. EL TEST DE CIRCULARIDAD [decisivo — la pregunta más importante del doc]

Aplico R-NC (Doc 119 §4.3) a GAP-FOLIADO, comparando con la externalidad de Forni.

### 4.1. Por qué Forni es genuinamente externo (no circular) — el patrón a igualar

**[DATO + CÁLCULO].** En Teichmüller, la positividad de Forni **NO asume nada sobre los exponentes**. Las dos fuentes de externalidad:
1. **La medida $\mu_{MV}$ es geometría pura.** Masur–Veech se define por la **estructura plana** de las superficies de traslación (área, períodos, longitudes de conexiones de silla) — un objeto de **geometría de espacios de móduli**, definido **antes de y sin** ninguna función L, ninguna función zeta dinámica, nada aritmético. [DATO]
2. **La curvatura $B_\omega B_\omega^*$ es geometría diferencial pura.** Se calcula de la **variación de la estructura compleja** (Kodaira–Spencer), del período de Hodge $H^{1,0}\subset H^1$ que rota a lo largo de la órbita. Es geometría de la variación de estructura de Hodge, **externa al espectro de Lyapunov que se quiere acotar**. [DATO]

**Resultado: Forni PASA un análogo de NC1 (la medida y la curvatura no mencionan los exponentes), NC2 (la fórmula vale para TODO el estrato, toda superficie genérica — sobregenera masivamente), NC4 (un exponente que se anulara forzaría una curvatura degenerada, visible geométricamente sin "localizar" nada).** Es el modelo de positividad externa.

### 4.2. ¿El flujo del sitio de escala es geometría pura o lleva ζ adentro? — LA DECISIÓN

**[DATO — el hecho que decide todo].** (Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999); R-LEF-FLUJO Doc 119 §3.4; Doc 125 §3.3 vía (c).) La **traza distribucional del flujo de escala $\mathbb R_+^*$** sobre el espacio de CCM **reproduce el lado aritmético de la fórmula explícita de Weil**:
$$ \mathrm{Tr}_{\mathrm{distr}}\Big(\int h(u)\,(\text{flujo de escala})\,du\Big) \;=\; \sum_p\sum_{m\ge1}\frac{\log p}{p^{m/2}}\,\hat h(m\log p)\;+\;(\text{término arquimediano}), $$
y la fórmula explícita iguala esto a $\sum_\rho\hat h(\rho)$. **Las órbitas periódicas del flujo de escala son los primos** (período $\log p$); **el espectro del generador son los ceros.** [DATO]

**[CÁLCULO — la respuesta directa, brutalmente honesta]:**

> **El flujo $\mathbb R_+^*$ del sitio de escala LLEVA ζ ADENTRO. No es geometría pura.** A diferencia del flujo de Teichmüller —cuyas órbitas periódicas son las geodésicas cerradas de la métrica de Teichmüller, objetos de geometría de móduli sin contenido aritmético— las **órbitas periódicas del flujo de escala SON los primos**, y su traza **ES** la fórmula explícita. El flujo de escala **está definido (en su versión con contenido espectral, la única útil para la analogía, §2.4) precisamente para que su traza sea $\sum_p\log p/p^{m/2}$**. La estructura aritmética no es externa al flujo: **es el flujo.**

**Consecuencia para la "curvatura/medida" de GAP-FOLIADO.** La medida invariante con contenido (la que tendría "exponentes no triviales", §2.4) es la que hace que la traza sea la fórmula explícita; la "forma de curvatura del fibrado de Hodge foliado" que mediría el gap sería **una reescritura de la segunda variación de la forma de Weil bajo el flujo**. Y por P43 (cuantificador maestro): el **VALOR** de ese funcional cuadrático se computa **de los primos solos** (es el lado aritmético, externo en apariencia), pero su **INERCIA** —la partición de su índice negativo en bloques, = la signatura, = $m=\kappa(Q)/2$, = el "gap"— **NO se determina sin las posiciones de los ceros**. El gap-foliado **es la inercia**, no el valor. Y la inercia es RH. [CÁLCULO, coincide con P43 §autonomy.]

### 4.3. R-NC sobre GAP-FOLIADO

**[CÁLCULO]**
- **NC1 (externalidad de la definición):** la forma de intersección $D\cdot D'$ y las clases $f_1,f_2,\Delta$ son funtoriales desde el sitio (Doc 125 §6.3 ya lo concedió). **PASA** — pero es la misma externalidad superficial que Forni: hasta aquí todo bien.
- **NC2 (sobregeneración):** ¿el gap-foliado vale para TODA clase / toda correspondencia por la curvatura, como Forni vale para todo el estrato? **AQUÍ FALLA.** En Forni la fórmula de curvatura vale para toda superficie genérica porque la medida y la curvatura son geométricas. En el sitio de escala, la única medida con contenido espectral es la que reproduce la fórmula explícita; la "curvatura" solo tiene contenido **evaluada sobre las correspondencias del flujo = las que portan los primos/ceros**. No sobregenera a clases ajenas a ζ con contenido no trivial (sobre clases ajenas la curvatura es la del flujo isométrico = trivial, §2.4). **FALLA NC2** — exactamente como Doc 125 §6.3 NC2-condicional/G-125.B.
- **NC3 (no-reducción a positividades RH-equivalentes catalogadas):** la curvatura-foliada con contenido **ES** la segunda variación de la forma de Weil bajo el flujo de escala = la traza de Lefschetz del flujo = MW-1/MW-6 del catálogo (Doc 124 §2.5). **FALLA NC3 rotundamente** — idéntico al veredicto de Doc 125 §6.3 (la vía (c) traza-del-flujo es la fórmula de Lefschetz, circular) y a la tensión T3 de Doc 119.
- **NC4 (test de dos mundos):** en ¬RH (un cuádruplo off-crítico, $m\ge1$), ¿GAP-FOLIADO es falso por una razón computable de la curvatura sin localizar el cero? **FALLA** — por P43: el VALOR no distingue (se computa de los primos en ambos mundos); solo la INERCIA distingue, y la inercia requiere las posiciones de los ceros (binariedad inaccesible, Doc 108). **FALLA NC4.**

**[CÁLCULO] Veredicto R-NC:** GAP-FOLIADO **pasa NC1 pero FALLA NC2, NC3, NC4** — **es circular**. La diferencia con Forni es **exactamente NC2**: la curvatura de Forni sobregenera (vale para todo el estrato geométrico, externo a cualquier ζ); la curvatura-foliada del sitio de escala **solo tiene contenido sobre las correspondencias de ζ**, porque **el flujo lleva ζ adentro** y sin ζ el flujo es isométrico-trivial (§2.4 R1).

### 4.4. La diferencia que decide todo, en una frase

**[CÁLCULO].** **El flujo de Teichmüller es geometría pura (espacios de móduli de superficies planas); su positividad de Forni es externa porque la medida de Masur–Veech y la curvatura del fibrado de Hodge se definen sin ζ. El flujo del sitio de escala, en cuanto tiene el contenido espectral que la analogía necesita, ES la fórmula explícita (sus órbitas periódicas son los primos, su traza es $\sum_p\log p\,\hat h(m\log p)$); por tanto la positividad-de-Forni-análoga no es externa: es la positividad de Weil = RH, reescrita en lenguaje de curvatura foliada.** El precedente de Hodge dinámica reproduce **la estructura** (forma indefinida + cociclo + curvatura → gap) pero **no la fuente de externalidad**, porque la fuente de externalidad de Forni es la geometría de móduli, y nuestro flujo no es geometría de móduli: es aritmética disfrazada de flujo.

---

## 5. VEREDICTO

### 5.1. Clasificación (a)/(b)/(c)/(d)

**[CÁLCULO] Veredicto: (b) — marco correcto pero CIRCULAR, con un componente de (c) en la flecha dinámica (R1).**

Desglose:
- **¿Es el marco correcto?** **SÍ, estructuralmente.** La teoría de Hodge dinámica es el **único precedente conocido** de una positividad/gap de un fibrado de Hodge **de forma indefinida**, transportado por un cociclo de un flujo, probada por método **externo** (curvatura + ergodicidad). Las flechas forma-indefinida↔forma-indefinida (§2.1bis) y cociclo-preserva-forma↔transporte-preserva-intersección (§2.3) son **tight**. Esto valida la dirección que Doc 126 §5.3 pedía y le da un nombre preciso al método candidato: **fórmula de curvatura tipo Kontsevich–Forni + integración ergódica**. La identificación gap-de-Forni ↔ el "1" aislado de la signatura $(1,\rho-1)$ (§3.2a) es la flecha operativa más fuerte.

- **¿Es no-circular?** **NO.** El test §4 es nítido: la externalidad de Forni descansa sobre que **el flujo de Teichmüller y la medida de Masur–Veech son geometría pura de móduli, ajenas a ζ**. El flujo del sitio de escala, en su versión con contenido espectral (la única que da una analogía no vacía), **lleva ζ adentro**: sus órbitas periódicas son los primos, su traza es la fórmula explícita. La curvatura-foliada que daría el gap **es** la segunda variación de la forma de Weil = MW-1 = RH. FALLA NC2/NC3/NC4. **Circular.** (b).

- **El componente de (c) — ruptura estructural en R1.** Hay además una ruptura dinámica genuina: el flujo $\mathbb R_+^*$ sobre $C_p$ es una **isometría/rotación, NO hiperbólica ni mixing**, a diferencia del flujo de Teichmüller. Sobre un flujo isométrico el cociclo de Hodge **no crece**, los exponentes de Lyapunov son **nulos**, la fórmula de Kontsevich–Forni es **trivial**. La analogía "exponentes de Lyapunov ↔ ceros" es **categorialmente equivocada** (§2.3i): el espectro de los ceros es de **frecuencias** (rotación), no de **Lyapunov** (hiperbolicidad). Para rescatar contenido espectral hay que pasar al flujo global, y ahí R1 colapsa en R2 (el flujo con contenido = la fórmula explícita). **El flujo no es hiperbólico del modo que Forni requiere** — eso es (c). La combinación es: la analogía se rompe estructuralmente en lo dinámico (c) **y**, donde se la fuerza a tener contenido, se vuelve circular (b). **(b) es el veredicto dominante porque captura la causa raíz: la fuente de no-trivialidad ES ζ.**

### 5.2. El flujo lleva ζ adentro o es geometría externa — la respuesta directa

**[CÁLCULO] LLEVA ζ ADENTRO.** Esta es la respuesta a la pregunta que el encargo marcó como la más importante. El flujo de Teichmüller es geometría pura: sus geodésicas cerradas son objetos de móduli sin aritmética. El flujo del sitio de escala **está definido de modo que su traza distribucional es el lado de primos de la fórmula explícita** (Connes 1999); sus órbitas periódicas **son los primos**; su generador tiene a **los ceros** por espectro. No hay manera de extraerle contenido espectral sin extraerle ζ. Por tanto la positividad-de-Forni-análoga, que en Teichmüller es externa, **en el sitio de escala es la positividad de Weil renombrada**. Cuarta derivación independiente del mismo muro (Doc 119 ingeniería inversa; Doc 124/125 forma de intersección; Doc 126 AHK/Babaee–Huh; aquí, Hodge dinámica).

### 5.3. Lo que faltaría, y si hay un camino (a)

**[CONSTRUCCIÓN] El único camino concebible hacia (a)** —y es muy estrecho— sería encontrar una **medida y una curvatura del fibrado de Hodge foliado del cuadrado que sean geométricas en un sentido independiente del flujo de escala-con-ζ**, es decir, una estructura de "móduli del cuadrado tropical" con **variación de estructura (compleja/de Hodge) genuina** que genere una segunda forma fundamental no trivial **sin** que esa variación sea el flujo de escala. Esto requeriría:

1. **[GAP — el más profundo] Una variación de estructura de Hodge sobre una familia de cuadrados, externa al flujo de escala.** En Teichmüller la curvatura viene de que la estructura compleja **cambia** sobre $\mathcal H_g$. En el cuadrado fijo $C_p\times C_p$ el flujo $\mathbb R_+^*$ es isométrico (no cambia la estructura). Habría que exhibir un **espacio de móduli de cuadrados tropicales** con un fibrado de Hodge de curvatura no trivial **cuyo flujo NO sea el de escala-aritmético**. No hay candidato. Si existiera, su relación con ζ sería el nuevo test de circularidad.

2. **[GAP] El paquete de Kähler FOLIADO infinito-dimensional** (Doc 126 §5.3 punto 3, R-SIG≺R-FIN): incluso con curvatura externa, persiste la obstrucción de que la parte pura es infinito-dimensional y las signaturas no son continuas bajo el límite (T2). Forni es finito-dimensional ($2g$); el análogo infinito-dimensional de la fórmula de Kontsevich–Forni **no existe**.

3. **[VERIFICACIÓN — el experimento decisivo de Phase 42] ¿Existe alguna foliación del cuadrado, distinta del flujo de escala, con curvatura de Hodge no trivial y externa a ζ?** Si NO (lo probable, porque la única dinámica natural del sitio es la de escala = aritmética), entonces (a) está **cerrado** y el veredicto se endurece a (b)/(c) definitivo, no solo indeterminado.

**[CÁLCULO] Primer paso concreto, si se persigue (a):** intentar definir, sobre el toro tropical $C_p\times C_p$, una **variación de "estructura de Hodge tropical"** (un análogo de la descomposición $H^{1,0}\oplus H^{0,1}$ tropical, vía la métrica de Allermann–Rau y una polarización) y calcular su **segunda forma fundamental** bajo una deformación de la polarización **que NO sea la traslación de escala**. Si la curvatura resultante es no trivial y su integral controla la signatura **sin** invocar la traza del flujo, hay un germen de (a). Si toda deformación natural de la polarización resulta ser el flujo de escala (= aritmética), (a) está cerrado. **Predicción honesta: está cerrado**, porque la única estructura que distingue las direcciones positivas/negativas del primitivo es la que sabe dónde están los ceros (P43 inercia), y eso es ζ.

### 5.4. Síntesis

**[CÁLCULO]** La teoría de Hodge dinámica es el **marco estructuralmente correcto** —reproduce con fidelidad la arquitectura "forma indefinida + cociclo de un flujo + curvatura semidefinida → gap = signatura"— y por eso es valioso haberlo identificado: nombra el método candidato (curvatura tipo Kontsevich–Forni) y la flecha operativa (gap de Forni ↔ el "1" de la signatura). **Pero falla en la única cosa que importa para no-circularidad: la fuente de externalidad.** La positividad de Forni es externa porque el flujo de Teichmüller es geometría pura de móduli; la positividad-foliada-análoga es **circular** porque el flujo del sitio de escala **es** la fórmula explícita (órbitas periódicas = primos, traza = lado aritmético de Weil). El precedente, lejos de romper el muro, **explica por qué el muro está donde está**: el muro es la diferencia entre "flujo geométrico (Teichmüller)" y "flujo aritmético (escala)", que es la diferencia P43 entre el **valor** (computable de los primos) y la **inercia** (la posición de los ceros). El gap-foliado es inercia. La inercia es RH.

**Veredicto global: (b) marco correcto pero CIRCULAR**, con ruptura estructural (c) en la flecha de hiperbolicidad (el flujo de escala es isométrico, no hiperbólico). No es (a) porque la externalidad de Forni no transplanta; no es (d) porque el test §4 es concluyente (el flujo lleva ζ adentro, vía Connes 1999, dato firme). El camino (a) requeriría una foliación del cuadrado con curvatura de Hodge externa a ζ, hoy ausente y probablemente inexistente (la única dinámica del sitio es aritmética).

---

## 6. Honestidad y registro

Ningún teorema nuevo se probó. Se **leyó en fuente** (Forni 2002 Annals + survey cap. 8 Handbook; fórmula de Kontsevich–Forni $\sum\lambda_i=\int\mathrm{tr}(BB^*)d\mu$ vía notas Bourbaki Matheus; EKZ Publ. IHÉS 2014 $\sum\lambda_i=\kappa_\mu+\tfrac{\pi^2}{3}c_{\mathrm{area}}$; ergodicidad/no-uniform-hiperbolicidad del flujo de Teichmüller respecto de Masur–Veech; simplicidad de Avila–Viana) y se **comparó** con el corpus interno:

- **El precedente es genuino y la estructura es tight** en dos flechas (forma indefinida; cociclo preserva forma). La teoría de Hodge dinámica **es** el marco correcto para "positividad de un fibrado de Hodge indefinido por método externo".
- **La analogía se rompe en R1 (dinámica):** el flujo de escala es isométrico/rotacional, no hiperbólico/mixing; los exponentes de Lyapunov propios son nulos; la fórmula de Kontsevich–Forni sería trivial. "Exponentes ↔ ceros" es categorialmente erróneo (frecuencias vs Lyapunov).
- **La analogía se rompe en R2 (circularidad, el decisivo):** la externalidad de Forni viene de que Masur–Veech y la curvatura son **geometría pura de móduli, sin ζ**; el flujo de escala con contenido espectral **ES la fórmula explícita** (Connes 1999), luego la curvatura-foliada análoga **es** la forma de Weil = MW-1 = RH. FALLA NC2/NC3/NC4.
- **El análogo de "la signatura persiste" es GAP-FOLIADO** (§3.3) = G-125.B renombrado como gap espectral foliado; la flecha operativa es **gap de Forni ↔ el "1" aislado de la signatura $(1,\rho-1)$**.
- **El flujo del sitio de escala LLEVA ζ ADENTRO** (respuesta a la pregunta central). El de Teichmüller es geometría; el de escala es aritmética disfrazada de geometría. Esa es la diferencia que decide.
- **Veredicto: (b) circular, con componente (c).** Cuarta derivación independiente del mismo muro. El precedente no lo cruza: lo **explica** (muro = valor-externo/inercia-interna, P43).

**El punto de traba ES el resultado:** la teoría de Hodge dinámica da el lenguaje y el método correctos, y precisamente por eso deja ver, con máxima nitidez, que la fuente de positividad que en Teichmüller es externa, en el sitio de escala **coincide con ζ misma** — porque el flujo del sitio de escala no es un flujo geométrico sobre un espacio de móduli, sino el flujo cuya traza es la fórmula explícita.

---

## Referencias

**Fuente externa leída esta sesión (junio 2026, WebSearch/WebFetch):**
- G. Forni, *Deviation of ergodic averages for area-preserving flows on surfaces of higher genus*, Annals of Math. (2) 155 (2002) 1–103 — no-anulación y gap espectral del cociclo de Kontsevich–Zorich; método variacional-ergódico vía la métrica de Hodge. **[DATO]**
- G. Forni, *On the Lyapunov exponents of the Kontsevich–Zorich cocycle*, Handbook of Dynamical Systems vol. 1B, cap. 8 (PDF Lanneau/Grenoble) — estructura del fibrado de Hodge, forma de intersección, segunda forma fundamental $B_\omega$. **[DATO, vía survey]**
- M. Kontsevich, G. Forni — fórmula $\lambda_1+\dots+\lambda_g=\int(\Lambda_1+\dots+\Lambda_g)\,d\mu$, $\Lambda_i$ autovalores de $H_\omega=B_\omega B_\omega^*$, lado derecho $\ge0$ por positividad del producto hermitiano de Hodge. **[DATO, vía notas Bourbaki de Matheus, Disquisitiones Mathematicae 2012.]**
- A. Eskin, M. Kontsevich, A. Zorich, *Sum of Lyapunov exponents of the Hodge bundle with respect to the Teichmüller geodesic flow*, Publ. Math. IHÉS 120 (2014) 207–333; arXiv:1112.5872 — $\sum\lambda_i=\kappa_\mu+\tfrac{\pi^2}{3}c_{\mathrm{area}}(\mathcal C)$ (grados de fibrados + constante de Siegel–Veech). **[DATO]**
- Veech; A. Avila, S. Gouëzel, J.-C. Yoccoz, *Exponential mixing for the Teichmüller flow*, Publ. Math. IHÉS 104 (2006) — ergodicidad, mixing exponencial, no-uniform hiperbolicidad (Pesin) del flujo de Teichmüller respecto de Masur–Veech. **[DATO, vía WebSearch]**
- A. Avila, M. Viana — simplicidad del espectro de Lyapunov del cociclo KZ (conjetura de Kontsevich–Zorich). **[DATO, vía WebSearch]**

**Internas (backward-only):** Doc 126 (AHK no aplica; Babaee–Huh obstruye; paquete de Kähler tropical-foliado; veredicto (d) con sesgo (b)/(c)); Doc 125 (forma de intersección de Allermann–Rau; $G_{\text{toy}}$ signatura $(1,2)$; G-125.A real/entero; G-125.B persistencia de signatura; NC3 vía (c) = Lefschetz = circular); Doc 124 (G2 = índice de Hodge indefinido; positividad de Weil = MW-1/MW-6); Doc 119 (R-SIG/R-FIN/R-LEF-FLUJO; R-NC NC1–NC4; tensiones T2, T3); Doc 80 (Castelnuovo–Severi aritmético; la forma que distingue medidas es RH-equivalente); P35 (κ(Q)=2m); P43 (cuantificador maestro; distinción valor/inercia; barrera media→uniforme).

**Clásica / corpus CC (contexto, vía Docs internos):** A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5 (1999) — traza del flujo de escala = lado aritmético de la fórmula explícita; órbitas periódicas = primos. **[DATO, vía Doc 119 §3.4.]** Connes–Consani, *Geometry of the Scaling Site*, arXiv:1603.03191.

*Fin del Doc 127.*
