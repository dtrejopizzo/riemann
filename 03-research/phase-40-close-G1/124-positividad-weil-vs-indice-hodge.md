# Doc 124 — ¿Es la positividad de Weil de Connes–Consani el índice de Hodge que falta?

**Programa:** Hipótesis de Riemann — Phase 40: cerrar G1/G2.
**Fecha:** junio 2026.
**Autor:** David Alejandro Trejo Pizzo.
**Prerrequisitos:** Doc 123 (bifurcación C-cok/C-rank del obstáculo del cuadrado; la tolerancia repara C-cok pero NO C-rank; en dim 2 el dato de C-rank es una forma de intersección = G2); Doc 122 (Pedido 122.A: falta una polarización positiva sobre H¹ del cuadrado; la dualidad de CC es de Pontryagin, no da signatura); Doc 119 (R-PESO, R-SIG realizaciones (i)/(ii)/(iii); el test de no-circularidad R-NC, cláusulas NC1–NC4).

**Disciplina de etiquetado (regla absoluta):** **[DATO]** = leído en fuente esta sesión (PDF en `papers-referencia/`, vía la herramienta Read), con cita exacta paper + página/teorema. **[CÁLCULO]** = derivación mía, mostrada. **[GAP]** = lo que falta, con precisión. **[CONJETURA]** / **[NO VERIFICADO]** = como se indica. NUNCA "probado" sobre algo geométrico nuevo. Una falsa victoria es peor que un fracaso. Si la respuesta a la pregunta central es "no se puede determinar en fuente", ese es un resultado válido — se declara con el dato exacto que faltaría.

---

## 0. Resumen ejecutivo

Este documento fija el template geométrico de "qué positividad es la buena" (índice de Hodge sobre una superficie / Castelnuovo–Severi), lee en fuente los dos papers de Connes–Consani provistos, y aplica el test R-NC para decidir si la positividad de Weil que esos papers contienen ES el ingrediente de G2 (positividad-intersección, geométrica, reutilizable) o es la positividad-espectral (la forma cuadrática de la fórmula explícita evaluada en tests, RH-equivalente y por tanto circular para nuestro propósito).

Identificación en fuente de los dos papers:
- **2310.18423v2 = Connes–Consani–Moscovici, *Zeta zeros and prolate wave operators — semilocal adelic operators*** (4 May 2024) **[DATO]**. Es un paper de **operadores espectrales**: cyclic pairs, operador prolate, espacio de Sonine como parte negativa del espectro, matrices de Jacobi hermitianas, transformada de Hardy–Titchmarsh semilocal, espacios de de Branges.
- **2307.06748v1 = Connes–Consani, *On the metaphysics of F₁*** (13 Jul 2023) **[DATO]**. Es un paper de **fundamentos algebraicos / F₁**: anillos de S[μ_{n,+}]-polinomios, el espectro de la esfera 𝕊 como base absoluta, el RR de Z̄ (género de Spec Z = 0); contiene una discusión de la distribución de conteo N(u) del lado de la fórmula explícita y nombra (en nota al pie) la cohomología H¹(**C**) como de dimensión infinita.

**Veredicto de la pregunta central (§6): (c) un FRAGMENTO geométrico del lado espectral, con la parte global francamente (a) circular/espectral.** La única positividad con contenido de signo en el corpus leído es la positividad de Weil del lado espectral (la forma cuadrática de Weil Q_n / la trace formula semilocal), que es RH-equivalente al globalizarse: FALLA NC3. PERO hay un fragmento incondicional —la **estabilidad del espacio de Sonine semilocal bajo amplificación** (CCM Thm 4.6) y la **positividad arquimediana en ventana**— que pasa NC1 y sobregenera (NC2 parcial); ese fragmento es lo más parecido a "una forma definida sobre un subespacio", pero **no es una forma de intersección sobre clases de divisores del cuadrado**: es una restricción del operador prolate (un objeto del lado espectral del lugar arquimediano), no de NS(X×X). Consecuencia para G2: **el ingrediente NO existe en el corpus leído**, ni siquiera en fragmento geométrico-de-intersección; existe en fragmento sólo del **lado espectral**, y extenderlo no da el índice de Hodge sino la positividad de Weil global = RH.

---

## 1. Template [DATO + CÁLCULO]: qué positividad es "la buena"

### 1.1. El teorema del índice de Hodge clásico (superficie proyectiva)

**[DATO clásico, vía Doc 119 §2.3 realización (ii), no re-verificado en fuente esta sesión — es contexto].** Sea S una superficie proyectiva lisa sobre un cuerpo algebraicamente cerrado, NS(S) su grupo de Néron–Severi, ρ = rk NS(S) el número de Picard. La forma de intersección
$$ (\,\cdot\,,\,\cdot\,):\ \mathrm{NS}(S)\otimes\mathbb R \times \mathrm{NS}(S)\otimes\mathbb R \to \mathbb R,\qquad (D,D')\mapsto D\cdot D' $$
es simétrica, no degenerada (por dualidad de Poincaré en H²), y su **signatura es (1, ρ−1)**: tiene exactamente UNA dirección positiva. El teorema del índice de Hodge enuncia: sobre el ortogonal (H·)^⊥ de una clase amplia H (H²>0), la forma de intersección es **definida negativa**. Equivalentemente, para D con D·H=0 se tiene D·D ≤ 0, con igualdad sólo si D≡0 numéricamente.

**[CÁLCULO] Qué tipo de positividad es ésta, con precisión.** Es la positividad de una forma de intersección sobre un subespacio de clases de divisores (codimensión 1 en una superficie). Sus rasgos definitorios:
1. **Es bilineal sobre ℝ, simétrica, sobre UN espacio** (NS(S)⊗ℝ), no entre un grupo y su dual.
2. **Su definitud está restringida a un subespacio** ((H)^⊥), determinado por una clase amplia (una polarización H).
3. **Es geométrica**: D·D' se computa de la geometría de S (intersección de curvas / grados), **independiente de cualquier función L o posición de ceros**.

Ése es exactamente el perfil de la **realización (i)/(ii) de R-SIG** (Doc 119 §2.3): "una forma bilineal/hermitiana con involución sobre un espacio" + "una polarización (operador L) que la vuelve definida en cada pieza". La positividad-intersección.

### 1.2. Cómo Weil la usa para RH sobre cuerpos de funciones

**[DATO clásico, vía Doc 119 §2.3 (i), citas internas Wei48; Mattuck–Tate 1958; Grothendieck 1958].** Para una curva C/𝔽_q, Weil considera la superficie S = C×C. El Frobenius geométrico tiene un grafo Γ_F ⊂ C×C, una correspondencia. La desigualdad de **Castelnuovo–Severi** es la positividad de la forma de intersección restringida al subespacio de NS(C×C) generado por las correspondencias módulo las clases "triviales" (fibras horizontal/vertical):
$$ Z\cdot Z' \ \text{define una forma con signatura controlada por Hodge index sobre } \mathrm{NS}(C\times C). $$
Aplicada a Z = Γ_F y sus iterados/transpuestos, la positividad fuerza la **desigualdad de Cauchy–Schwarz** que da |α| = √q sobre los autovalores de Frobenius α en H¹ — que es la RH para curvas. La cadena lógica es:
$$ \underbrace{\text{positividad de la forma de intersección en NS(C×C)}}_{\text{geométrica, Hodge index/Castelnuovo}} \ \Longrightarrow\ \underbrace{|\alpha|=\sqrt q}_{\text{pureza de pesos = RH}}. $$

**[CÁLCULO] El punto decisivo para nuestro programa.** Lo que hace que esto NO sea circular —y por tanto sea una **prueba** y no una reformulación de RH— es que la positividad de partida es un teorema sobre **TODAS las correspondencias de la superficie**, demostrado por geometría de superficies (Hodge index), que **ignora qué curva es C y dónde están sus puntos**. Esto es precisamente lo que el test R-NC formaliza:
- **NC2 (sobregeneración):** Castelnuovo vale para todo divisor de C×C, no sólo para Γ_F.
- **NC4 (test de dos mundos):** en el mundo ¬RH un autovalor con |α|≠√q produciría una clase con auto-intersección del signo prohibido, visible en la forma sin localizar el cero.

**Esto fija EXACTAMENTE qué positividad es "la buena":** la **positividad-intersección** —Q(D,D)≥0 para D en un subespacio de clases de divisores de una superficie, probada por geometría, independiente de las posiciones de los ceros—. Cualquier otra positividad, en particular la positividad de la forma cuadrática de la fórmula explícita evaluada en funciones de prueba, es **positividad-espectral** y es RH-equivalente (es literalmente el criterio de Weil), por tanto circular para construir G2.

### 1.3. La dicotomía operativa (la que el R-NC decide)

**[CÁLCULO] Resumo el discriminador.**

| | Positividad-INTERSECCIÓN (BUENA) | Positividad-ESPECTRAL (CIRCULAR) |
|---|---|---|
| objeto | Q(D,D)≥0, D∈ subespacio de NS(X×X) | W(f⋆f̃)≥0, f función de prueba |
| espacio | clases de divisores/correspondencias | funciones test en la clase de Weil |
| origen de la positividad | geometría de la superficie (Hodge index) | = criterio de Weil = RH |
| dependencia de los ceros | ninguna | total (ES la condición de RH) |
| R-NC | pasa (NC1,NC2,NC4 con contenido) | FALLA NC3 (es MW-1 del catálogo) |
| reutilizable para G2 | sí | no (renombrar RH no es probarla) |

La pregunta del documento es: ¿de cuál de las dos columnas es la positividad de Weil que CC efectivamente prueban en estos papers?

---

## 2. Lectura en fuente — paper 1: CCM, *Zeta zeros and prolate wave operators* (2310.18423v2)

### 2.1. Qué es el paper y qué positividad maneja

**[DATO]** (2310.18423v2, Abstract, p.1, verbatim): *"We integrate in the framework of the semilocal trace formula two recent discoveries on the spectral realization of the zeros of the Riemann zeta function by introducing a semilocal analogue of the prolate wave operator. The latter plays a key role both in the spectral realization of the low lying zeros of zeta —using the positive part of its spectrum— and of their ultraviolet behavior —using the Sonin space which corresponds to the negative part of the spectrum."*

**[DATO]** (íd., Introducción §1, p.2): *"there exists a property P(n), involving only the Euler factors for primes smaller than n, and whose validity for all n is equivalent to RH. This is derived from Weil's positivity criterion which involves the quadratic form Q_n defined using the Riemann–Weil explicit formulas applied to test functions with support in the compact symmetric interval [1/n, n]. Furthermore, the semilocal trace formula of [7] gives, for each n, a Hilbert space theoretic framework in which the Weil quadratic form Q_n becomes the trace of a simple operator theoretic expression."*

**Lectura estructural [CÁLCULO sobre DATO].** La positividad nombrada es **explícitamente** la **positividad de Weil del criterio de Weil** — la forma cuadrática Q_n de la fórmula explícita aplicada a tests de soporte en [1/n, n]. El propio paper la presenta como **RH-equivalente** ("whose validity for all n is equivalent to RH"). Esto la coloca, de entrada, en la columna ESPECTRAL/CIRCULAR del §1.3. El paper NO prueba la positividad de Q_n (sería RH): la **realiza** como traza de un operador, para *estudiarla* con herramientas operatoriales.

### 2.2. (a) Qué positividad exacta, sobre qué espacio, con qué cuantificador

**[DATO]** (íd., §1 p.2–3): la fuente de la positividad de Weil (en el lugar arquimediano) es *"the Hilbert space representation of the scaling group"*; el radical de la forma cuadrática de Weil es el **rango del mapa ℰ** sobre el Schwartz space S(ℝ)^{ev}_0, ℰ(f)(u) := u^{1/2}∑f(nu) (eq. citada en p.2). Y la conexión con positividad: *"with the Weil functional —which is automatically positive for a selfadjoint operator— ... The conditioning, by the radical of the Weil quadratic form, that worked for the scaling operator in the infrared case will be implemented automatically by the orthogonality of the positive and the negative part of the spectrum of the semilocal prolate operator"* (p.3).

**[CÁLCULO] La forma cuadrática es la de Weil; el espacio es de funciones de prueba; el cuantificador es "para toda f en S(ℝ)^{ev} (o de soporte restringido)".** No hay, en este pasaje, ninguna forma sobre clases de divisores. La positividad que el paper logra **incondicionalmente** es la trivial "tr de un operador autoadjunto ≥ 0" (W(f⋆f̃) = ⟨Tf,f⟩ con T≥0 por ser cuadrado/autoadjunto); el contenido de RH está en que esa positividad **coincida** con Q_n, lo cual el paper no prueba (y no puede sin RH).

### 2.3. (b) El método

**[DATO]** El método es enteramente espectral/operatorial:
1. **Cyclic pairs y operador prolate** (§2, p.5–6): un par cíclico (D,ξ), D autoadjunto, ξ vector cíclico; operador prolate formal ω(D,ξ,λ) := −D² + λ²N, con N el operador de grado de los polinomios ortogonales (Def. 2.2, p.6). **[DATO]**
2. **Caso arquimediano = operador prolate clásico** (§3): W_λ = −𝕊² + 2πλ²(4N+1) − 1/4 (eq. (5), p.4), con 𝕊 el generador autoadjunto del grupo de dilataciones en L²(ℝ)^{ev}. La matriz de Jacobi de 𝕊 tiene entradas 𝕊_{n,n+1} = i√((n+1/2)(n+1)) (p.4). **[DATO]**
3. **Espacio de Sonine** = parte negativa del espectro del prolate (Abstract, y §4.5 Def. 4.4, p.20): S_λ(𝕂,α) := {f∈L²(𝕂) : f(x)=0 & 𝔽_α f(x)=0 ∀|x|<λ}. **[DATO]**
4. **Transformada de Hardy–Titchmarsh semilocal** (§4): construcción del par cíclico semilocal (𝕊, ξ_S) sobre L²(X_S)^{K_S}, con la medida dm_S(s) = |∏_{v∈S} L_v(½−is)|² ds (eq. (6),(48)). **[DATO]**
5. **Estabilidad del Sonine semilocal** (§4.7, Thm 4.6, p.23) y conexión con espacios de de Branges (§4.8). **[DATO]**
6. **Representación metaplectica** (§5): el prolate como elemento del álgebra envolvente de sl(2,ℝ) vía la rep. metaplectica del doble cubrimiento de SL(2,ℝ). **[DATO]**

Es decir: **Sonine + escala + prolate**, exactamente los tres ingredientes que el encargo §4 nombra como candidatos a fragmento. NINGUNO es una forma de intersección.

### 2.4. (c) Clase de funciones de prueba

**[DATO]** La positividad de Weil de partida vive en **funciones de prueba de soporte restringido** [1/n, n] (la Q_n, §1 p.2). El espacio de Sonine semilocal S_λ(X_S, α) está parametrizado por λ>0 (Def. 4.5, p.21) y consiste en funciones de L²(X_S)^{K_S} que se anulan junto con su Fourier en |x|<λ — es decir, una **condición de soporte** (ultravioleta). El resultado central de estabilidad es:

**[DATO]** (Thm 4.6, p.23): *"Let S∋∞ be a finite set of places and λ>0. Then the map θ_S is a hilbertian isomorphism of the Sonin spaces θ_S : S_λ(ℝ,e_∞) → S_λ(X_S, α)"*. Y el comentario clave (p.5): *"This result suggests that the obtained invariantly defined Sonin space should, when suitably equipped with a prolate type operator, play the role of the sought for Weil cohomology."*

**[CÁLCULO] Esto es lo más cerca que el corpus llega a "un objeto invariante candidato a cohomología de Weil".** Pero nótese: es un espacio de Hilbert (Sonine) con un operador prolate, **no** un grupo de clases de divisores con forma de intersección. La frase de los autores es **programática** ("should ... play the role"), no un teorema de que lo sea.

### 2.5. R-NC aplicado a la positividad de 2310.18423

**[CÁLCULO] Aplico el test a la positividad de Weil Q_n / trace-formula que el paper maneja.**

- **NC1 (externalidad).** La construcción del par cíclico, el prolate y el Sonine es funtorial desde adeles/escala; no menciona los ceros en su definición. **PASA.** (Igual que el reporte de Doc 119 §4.3 para la candidata CC.)
- **NC2 (sobregeneración).** La positividad arquimediana (la del operador autoadjunto, ⟨Tf,f⟩≥0) vale para toda f∈S(ℝ)^{ev}, no sólo para la que codifica ζ — sobregenera trivialmente, pero **trivialmente**: cualquier forma "⟨Tf,f⟩ con T≥0" sobregenera, y eso no aporta contenido geométrico. La sobregeneración con contenido (à la Castelnuovo: "vale para toda correspondencia de una superficie por un teorema de superficies") **NO está presente**, porque no hay superficie ni correspondencias. **PASA sólo en el sentido trivial; FALLA en el sentido con contenido.**
- **NC3 (no-reducción a positividades RH-equivalentes catalogadas).** Aquí está la determinación. La positividad cuyo contenido importa —que Q_n ≥ 0 para todo n— es **literalmente** el criterio de Weil = **MW-1** del catálogo (Doc 119 §4.3, NO-GO-LIST). El propio paper lo dice: "whose validity for all n is equivalent to RH" (§2.1 arriba, [DATO]). La versión semilocal (la trace formula de [7] que vuelve Q_n una traza) es su uniformización = **MW-6** (Doc 119 §4.3). **FALLA NC3 rotundamente.**
- **NC4 (test de dos mundos).** En el mundo ¬RH, ¿la positividad falla por una razón computable desde el objeto sin localizar el cero? No: para saber si Q_n<0 hay que evaluar la forma de Weil, cuyo signo ES la posición de los ceros (binariedad inaccesible, Doc 119 §4.3, NC4 / Doc 108). **FALLA NC4.**

**[CÁLCULO] Conclusión para el paper 1.** La positividad de 2310.18423 es **positividad-ESPECTRAL**: FALLA NC3 y NC4. Es la columna circular del §1.3. **No es el índice de Hodge.** Es la realización operatorial de la positividad de Weil, RH-equivalente.

---

## 3. Lectura en fuente — paper 2: CC, *On the metaphysics of F₁* (2307.06748v1)

### 3.1. Qué es el paper

**[DATO]** (2307.06748v1, Abstract, p.1, verbatim): *"we investigate the general notion of rings of 𝕊[μ_{n,+}]-polynomials and relate this concept to the known notion of number systems. The Riemann-Roch theorem for the ring ℤ of the integers that we obtained recently uses the understanding of ℤ as a ring of polynomials 𝕊[X] in one variable over the absolute base 𝕊, where 1+1 = X+X². The absolute base 𝕊 ... thus turns out to be a strong candidate for the incarnation of the mysterious F₁."* Dedicado a Yuri Manin.

El paper es de **fundamentos**: F₁, sistemas de numeración balanceados (X=3, X=−2), el sitio aritmético sobre 𝕊[X], la esfera espectral 𝕊 como base absoluta. **NO es un paper de positividad ni de formas cuadráticas.**

### 3.2. (a) Qué positividad / qué contenido relevante

La única estructura cercana a "positividad" es la **distribución de conteo** N(u) de §2 (Adelic and topos theoretic incarnation of C):

**[DATO]** (íd., §2, eq. (2.4)–(2.5), p.4): N(u) = (d/du)φ(u) + κ(u), φ(u) := ∑_{n<u} n Λ(n), donde **κ(u) es exactamente la distribución que aparece en la fórmula explícita de Riemann–Weil**: ∫₁^∞ κ(u)f(u)d*u = ∫₁^∞ (u²f(u)−f(1))/(u²−1) d*u + cf(1), c = ½(log π + γ). Y: *"One shows that the distribution N(u) is positive on (1,∞)"* (p.4), con la fórmula en términos de ceros (2.5): N(u) = u − d/du(∑_{ρ∈Z} order(ρ) u^{ρ+1}/(ρ+1)) + 1.

**[CÁLCULO] Qué positividad es esta.** "N(u) positiva en (1,∞)" es una positividad de una **distribución de conteo del lado de la fórmula explícita** — su núcleo κ es el núcleo de Weil. No es una forma cuadrática sobre un espacio de clases; es la positividad del análogo de Hasse–Weil de la función de conteo N(q), motivada por "N(1) debería ser −∞" (densidad de ceros). Es del lado espectral/aritmético, y de hecho el paper la usa para conectar con la trace formula de [5] (Connes 1999) y el espacio de clases de adeles X_Q (eq. (2.6)). **No hay forma de intersección.**

### 3.3. El dato decisivo sobre H¹(C) y el RR

**[DATO]** (íd., §2, nota al pie 3, p.3, verbatim): *"the number of zeros of ζ_Q is infinite, and so is the dimension of the (mysterious) cohomology H¹(**C**)."* Y (§1, p.2): el RR de Z̄ *"shows that the genus of Spec Z is zero."*

**[CÁLCULO] Consecuencia para G2/G1.** Este paper **confirma desde otra fuente** el dato base de Doc 119 §2.4: dim H¹(**C**) = ∞ (la cohomología buscada NO es finito-dimensional total). Y el RR que CC tienen (el de Z̄, género 0) es un RR de **dimensión 1** (una "curva" Spec Z, género 0), **no** un RR de superficie con forma de intersección. El paper NO contiene ningún ingrediente de dim-2 (ni cuadrado, ni NS(X×X), ni índice de Hodge). La frase "absolute Descartes powers Spec Z × ⋯ × Spec Z" (cita de Manin, p.3) es señalada como **pregunta abierta**, no como objeto construido.

### 3.4. R-NC aplicado al paper 2

**[CÁLCULO]** No hay aquí una positividad-candidata-a-G2 que testear: la positividad de N(u) es la de una distribución de la fórmula explícita.
- **NC3:** "N(u) positiva en (1,∞)" + "N(1)=−∞ reflejando la densidad de ceros" (p.4, [DATO]) es manifiestamente del lado de la fórmula explícita / densidad de ceros — interderivable con el lado espectral. **FALLA NC3** como candidata geométrica.
- En todo caso, **el paper 2 no propone esta positividad como ingrediente de pureza**; la usa como puente conceptual NCG↔topos↔tropical. No es un candidato a G2.

**Conclusión paper 2:** no aporta positividad-intersección. Aporta (i) confirmación de dim H¹=∞, (ii) que el RR de CC es de género 0 / dim 1, (iii) que el cuadrado (Spec Z × Spec Z) es pregunta abierta, no objeto. Coherente con Doc 123 §1.1.

---

## 4. La pregunta central, decidida

### 4.1. Enunciado de la pregunta (recordatorio)

¿La positividad de Weil que CC prueban ES (o contiene como fragmento) la **positividad-intersección** de tipo Hodge sobre clases de divisores del cuadrado (el ingrediente de G2), o es la **positividad-espectral** (la forma de la fórmula explícita en tests, RH-equivalente, circular)?

### 4.2. Determinación

**[CÁLCULO, la determinación decisiva del documento].**

La positividad **con contenido de signo** en el corpus leído —la única que podría dar una signatura— es la **positividad de Weil del lado espectral**:
- En 2310.18423: la forma cuadrática de Weil Q_n / su realización como traza del prolate (§2.1–2.2). FALLA NC3 y NC4 (§2.5).
- En 2307.06748: la positividad de la distribución de conteo N(u) (§3.2). FALLA NC3 (§3.4), y no es siquiera propuesta como ingrediente de pureza.

**Ninguna de las dos es una forma de intersección sobre clases de divisores.** No hay en ninguno de los dos papers:
- un grupo de clases de divisores de una superficie (NS(X×X)) **[DATO: ausente en ambos; el cuadrado es pregunta abierta, 2307.06748 §1 p.3]**;
- una forma bilineal simétrica sobre UN espacio de clases con signatura (1, ρ−1) **[DATO: ausente]**;
- una clase amplia / polarización H sobre tal espacio **[DATO: ausente — confirma Doc 122 §5.3 y Doc 119 §4.3]**.

**Por tanto la respuesta a la pregunta central es: la positividad de CC es positividad-ESPECTRAL, NO positividad-intersección.** Es la columna circular del §1.3. Para nuestro propósito (construir G2) es, en su forma global, **circular**: globalizar la positividad de Weil semilocal es MW-1/MW-6 = RH.

### 4.3. Por qué no es la positividad-intersección, con precisión categórica

**[CÁLCULO].** Hay una razón estructural, no accidental, anclada en Doc 122:
- La positividad-intersección vive sobre un **espacio de clases con una forma bilineal simétrica** (NS(S)⊗ℝ con D·D').
- La estructura de dualidad de CC es **dualidad de Pontryagin grupo↔dual** (Doc 122 §1.3, [DATO] 2205.01391 Thm 5.3), que **no es una forma sobre un espacio** y **no tiene carácter de simetría** sin una polarización externa (Pedido 122.A).
- La positividad de 2310.18423 es **⟨Tf,f⟩≥0 con T≥0 sobre un espacio de Hilbert de tests/Sonine** — una forma definida positiva sobre funciones, **no** una forma de signatura (1,ρ−1) sobre clases. Es positividad de un operador, no signatura de una intersección.

Las dos cosas son categóricamente distintas: una forma de intersección **tiene una dirección positiva y ρ−1 negativas** (signatura indefinida, es lo que da el índice de Hodge); la positividad espectral de CC es **definida** (todo el espectro positivo, o la separación positivo/negativo del prolate). El objeto que G2 necesita es **indefinido con signatura controlada**; el que CC tienen es **definido (semidefinido)**. No coinciden.

---

## 5. ¿Hay un fragmento geométrico-no-circular en el método? (encargo §4)

El método de CC es Sonine + escala + prolate (§2.3). El candidato a fragmento es el **caso semilocal incondicional**: la positividad/estabilidad para soporte restringido, que es INCONDICIONAL.

### 5.1. Qué es exactamente el fragmento incondicional

**[DATO]** Dos piezas incondicionales en el corpus:
1. **Positividad arquimediana en ventana** (vía Doc 119 §4.3 / Doc 100, [DATO interno]; la fuente externa es 2006.13771, no re-leído esta sesión): W_∞(g⋆g̃)≥0 para tests de soporte en (½,2). Incondicional.
2. **Estabilidad del Sonine semilocal** (2310.18423 Thm 4.6, p.23, [DATO leído esta sesión]): el espacio de Sonine semilocal S_λ(X_S,α) es **independiente de S** (isomorfismo hilbertiano θ_S bajo amplificación del conjunto finito de lugares). Incondicional. Y la frase programática (p.5): *"the obtained invariantly defined Sonin space should ... play the role of the sought for Weil cohomology."*

### 5.2. ¿Es ese fragmento la restricción de una forma de intersección a un subespacio?

**[CÁLCULO, el análisis pedido].** La hipótesis a testear (encargo §4): *si la positividad semilocal incondicional de soporte chico fuera la restricción de una forma de intersección a un subespacio, extenderla al soporte pleno sería el índice de Hodge global = G2, y sabríamos que el ingrediente existe en fragmento.*

Analizo. La positividad incondicional de soporte chico:
- Está sobre un **espacio de funciones** (tests con soporte en una ventana / Sonine con condición de soporte en |x|<λ), **no** sobre un espacio de clases de divisores. **[DATO: Def. 4.4/4.5, p.20–21.]**
- Es una positividad **definida** (⟨Tf,f⟩≥0, o la ortogonalidad positivo/negativo del prolate), **no** una forma indefinida de signatura (1, ρ−1). **[CÁLCULO §4.3.]**
- Su **extensión a soporte pleno** es **exactamente** la positividad de Weil global = el criterio de Weil para todo n = **RH** (MW-1). **[DATO: 2310.18423 §2.1, "validity for all n equivalent to RH".]**

**[CÁLCULO] Veredicto del fragmento.** La positividad semilocal incondicional **NO es la restricción de una forma de intersección a un subespacio**. Es la restricción de la **positividad de Weil del lado espectral** a un soporte chico (donde la suma de primos es finita/dominada, por eso es incondicional — coincide con la localidad automática de Doc 99/Doc 119 §3.3). Extenderla **no** da el índice de Hodge: da la positividad de Weil global = RH. Es decir: **el fragmento existe, pero es un fragmento del lado ESPECTRAL, no del geométrico-de-intersección.** Su extensión cae en NC3 (es MW-6→MW-1), no en un índice de Hodge.

La razón profunda [CÁLCULO]: lo que vuelve incondicional al fragmento es que en soporte chico **la suma de primos no diverge** (la cola Mertens de Doc 105 no aparece; localidad automática Doc 99). Eso es un hecho **analítico-aritmético** (cuántos primos caen en la ventana), no un hecho **geométrico** (no es que una forma de intersección sea definida en un subespacio por una clase amplia). La incondicionalidad viene de truncar la fórmula explícita, no de la geometría de una superficie. Por eso su extensión es RH, no Hodge.

### 5.3. Contraste exacto con Castelnuovo (lo que SÍ sería un fragmento geométrico)

**[CÁLCULO].** Un fragmento geométrico genuino se vería así: una forma bilineal simétrica Q sobre un subespacio V ⊂ "NS del cuadrado", con Q **definida negativa** sobre V por un teorema que diga "V = (clase amplia)^⊥ y la superficie tiene índice de Hodge". Extenderla = quitar la restricción a V = índice de Hodge sobre todo NS. Eso pasaría NC2 con contenido (vale para toda correspondencia) y NC4 (un autovalor malo da auto-intersección prohibida visible).

El fragmento de CC **no tiene esta forma**: no hay V de clases, no hay clase amplia, la positividad es definida (no indefinida con un (H)^⊥), y la extensión es RH no Hodge. **El fragmento que existe es del tipo equivocado.**

---

## 6. Veredicto

### 6.1. La pregunta central

**[CÁLCULO] Veredicto: (c) un fragmento geométrico del lado espectral — con la parte global francamente (a) circular/espectral.** Desglose:

- La positividad **global** de Weil que CC manejan (Q_n para todo n; su uniformización semilocal) es **(a) circular/espectral**: FALLA NC3 (es MW-1) y NC4. Es la columna circular del §1.3. **[DATO + CÁLCULO §2.5.]**
- Existe un **fragmento incondicional** (positividad arquimediana en ventana; estabilidad del Sonine semilocal, Thm 4.6): pasa NC1 y sobregenera (NC2 parcial, trivial). Pero **no es positividad-intersección**: es positividad-espectral restringida a soporte chico. Su extensión es RH, no índice de Hodge. **[CÁLCULO §5.2.]**
- En ningún sentido es **(b) geométrica/intersección**: no hay forma de intersección, ni clases de divisores del cuadrado, ni clase amplia/polarización en el corpus leído. **[DATO §4.2.]**

Por tanto, en la clasificación a/b/c/d del encargo: **NO es (b); la parte global es (a); el fragmento incondicional es (c) pero del lado espectral (no geométrico-de-intersección)**. La componente (d) "indeterminable en fuente" se aplica sólo a una cosa: si la versión semilocal invariante del Sonine, *equipada con un operador prolate aún no construido*, "should play the role of the sought for Weil cohomology" (2310.18423 p.5) **llegará** a tener una forma de intersección — eso es un programa abierto declarado por los propios autores, **indeterminable en la fuente actual** (el paper lo deja "for a forthcoming paper", Abstract).

### 6.2. Consecuencia para G2: ¿el ingrediente existe, existe en fragmento, o no?

**[CÁLCULO] El ingrediente de G2 (la forma de intersección / índice de Hodge sobre el cuadrado) NO existe en el corpus leído — ni siquiera en fragmento geométrico-de-intersección.**

- Lo que existe en fragmento es del **lado espectral** (positividad de Weil incondicional en ventana), cuya extensión es RH (circular), no Hodge.
- La estructura geométrica que G2 necesita —un espacio de clases con forma bilineal simétrica indefinida de signatura (1,ρ−1) y una polarización que la vuelva definida en (H)^⊥— **está ausente**, confirmando por una tercera ruta independiente los hallazgos de Doc 122 (falta una polarización positiva, Pedido 122.A) y Doc 123 (falta la norma de intersección = C-rank = G2). **Tres derivaciones independientes, mismo veredicto.**

Esto **refuta** (honestamente, evitando la falsa victoria que el encargo §5 advertía como de máximo riesgo) la hipótesis optimista de que "la positividad de Weil de CC YA ES el índice de Hodge que falta". No lo es. Es la positividad-espectral, RH-equivalente. El que CC la realicen operatorialmente (prolate, Sonine, Jacobi) es matemática valiosa para *estudiar* la forma de Weil, pero **no la convierte en una forma de intersección geométrica**, y por tanto no provee G2.

### 6.3. Lo que faltaría leer / pedir (lista concreta)

1. **2006.13771** (*Weil positivity...*) en fuente cruda esta sesión NO fue leído (sólo vía Doc 100/120). Confirmar verbatim el enunciado de la positividad arquimediana y su soporte; verificar si en algún lugar CC la fraseasn como "intersection theory of divisors on the square" con una forma bilineal sobre clases (Doc 120 §4.4 reporta la frase "intersection theory ... in development"). **[Pendiente; bajo riesgo de cambiar el veredicto: el catálogo MW ya la clasifica como MW-6.]**
2. **El "forthcoming paper" sobre la rep. de Weil de SL₂(𝔸_S)** anunciado en 2310.18423 (Abstract; §1 p.3) como "second candidate for the semilocal prolate operator": si ese candidato porta una **forma indefinida con signatura** (no sólo positivo/negativo del prolate), sería el primer indicio de algo tipo-Hodge. Indeterminable hoy. **[Pedido a CC / esperar publicación.]**
3. **Si el Sonine semilocal invariante (Thm 4.6) admite una forma bilineal natural** —no el producto hilbertiano definido positivo, sino una forma indefinida proveniente de la dualidad— que dé una signatura. Es la versión, en este lenguaje, del Pedido 122.A. **[Pregunta interna a CCM, decidible por un experto en su formalismo.]**
4. **El texto verbatim de Example 6.5 de Yoshitomi** ya fue leído esta sesión (1001.0448v3, p.34): confirma r(D)=1≠r(D')=0 con H⁰ isomorfos. Cierra el §6.3 punto 1 de Doc 123: la referencia "[yoshi]" ES Yoshitomi, arXiv:1001.0448, *Generators of modules in tropical geometry*. La definición de rango es r(D)=max{r∈ℤ≥−1 : U(D,r)=∅} (p.32, estilo Baker–Norine/Gathmann–Kerber), un invariante de equivalencia lineal vía ord(f,P) — **no del módulo**, y Thm 2.7 da r(D)≤dim(M)−1. **[DATO, ya cerrado.]**

---

## 7. Síntesis y honestidad

Ningún enunciado geométrico nuevo se ha probado aquí. Se ha **leído en fuente** (los dos PDFs de CC + Yoshitomi) y se ha **calculado**:

- **Template fijado:** la positividad "buena" para G2 es la positividad-intersección (forma bilineal simétrica indefinida de signatura (1,ρ−1) sobre clases de divisores de una superficie, definida negativa en (H)^⊥ por el índice de Hodge), que es como Weil prueba RH para curvas vía Castelnuovo–Severi. La positividad "mala" (circular) es la positividad-espectral de la forma de Weil en tests.
- **Paper 1 (CCM, prolate/Sonine):** positividad-ESPECTRAL. La forma cuadrática es la de Weil Q_n, declarada RH-equivalente por los propios autores. FALLA NC3 y NC4. Método: cyclic pairs, prolate, Sonine, Jacobi, Hardy–Titchmarsh semilocal. Ningún objeto de intersección.
- **Paper 2 (CC, metafísica de F₁):** no contiene positividad-candidata-a-G2; la positividad de N(u) es del lado de la fórmula explícita. Confirma dim H¹(**C**)=∞ y que el RR de CC es de género 0 / dim 1; el cuadrado es pregunta abierta.
- **Fragmento:** existe positividad incondicional de soporte chico (ventana arquimediana; estabilidad del Sonine), pero es un fragmento del **lado espectral**, no de intersección; su extensión es RH (MW-1), no índice de Hodge. Es el tipo equivocado de fragmento.
- **Veredicto (c) con global (a):** la positividad de CC es espectral/circular en lo global, fragmento espectral en lo incondicional, **nunca geométrica/intersección**. **El ingrediente de G2 no existe en el corpus leído**, ni en fragmento de intersección.

**El punto de traba ES el resultado, una vez más:** lo que CC tienen es la positividad de Weil realizada operatorialmente (definida positiva, sobre funciones), no una forma de intersección (indefinida, sobre clases, con signatura). La diferencia categórica entre "operador positivo sobre tests" y "forma de signatura (1,ρ−1) sobre NS" es exactamente la diferencia entre la columna circular y la columna buena del §1.3 — y entre RH-reformulada y RH-probada. Triple coincidencia con Doc 119 (R-NC), Doc 122 (falta polarización) y Doc 123 (falta norma de intersección = C-rank): el ingrediente de G2 sigue sin candidato en el corpus.

---

## Referencias

**Fuente primaria leída esta sesión (junio 2026, vía Read sobre PDFs en `papers-referencia/`):**
- A. Connes, C. Consani, H. Moscovici, *Zeta zeros and prolate wave operators — semilocal adelic operators*, arXiv:2310.18423v2 (4 May 2024) — Abstract, §1 (Introducción: Q_n, criterio de Weil RH-equivalente, radical = rango de ℰ, fuente de positividad = rep. del grupo de escala), §2 (cyclic pairs, prolate ω=−D²+λ²N, Def. 2.2), §3 (W_λ=−𝕊²+2πλ²(4N+1)−¼, eq. (5); Jacobi de 𝕊), §4 (semilocal: Hardy–Titchmarsh, eq. (36)–(58); Sonine local Def. 4.4 y semilocal Def. 4.5; Prop. 4.5 σ_p; Thm 4.6 estabilidad del Sonine; de Branges §4.8), §5 (metaplectica). **[DATO]**
- A. Connes, C. Consani, *On the metaphysics of F₁*, arXiv:2307.06748v1 (13 Jul 2023) — Abstract (RR de ℤ, 𝕊 como F₁, género de Spec Z=0), §1 (sistemas balanceados X=3, X=−2), §2 (sitio aritmético; N(u) eq. (2.4)–(2.5) con núcleo de Weil κ, "positiva en (1,∞)", N(1)=−∞; X_Q eq. (2.6); Thm 2.8; nota 3 p.3: dim H¹(**C**)=∞), §3 (𝕊[μ_{n,+}], Eilenberg–MacLane HA). **[DATO]**
- S. Yoshitomi, *Generators of modules in tropical geometry*, arXiv:1001.0448v3 (2 Apr 2011) — §1 (T-módulo M=H⁰(C,O_C(D)); r(D) no invariante del módulo), §6 (Tropical curves: ord(f,P) Prop. 6.1–6.3; divisores; Prop. 6.4 M es T-módulo; r(D)=max{r∈ℤ≥−1:U(D,r)=∅} p.32), Thm 2.7 (r(D)≤dim(M)−1, prueba p.33), **Example 6.5 (p.34: C género 1, C' género 2, H⁰(C,O(D))≅H⁰(C',O(D')) pero r(D)=1≠r(D')=0)**. Identifica "[yoshi]" de 1805.10501. **[DATO]**

**Internas (backward-only):** Doc 119 (R-SIG realizaciones (i)/(ii)/(iii); R-PESO(a)/(b); R-NC NC1–NC4; NO-GO-LIST MW-1/MW-6; orden R-SIG≺R-FIN; §2.4 dim H¹=∞); Doc 122 (dualidad de CC = Pontryagin, sin carácter de simetría; Pedido 122.A polarización/autoapareamiento; §5.3 búsqueda negativa de polarización en el corpus); Doc 123 (bifurcación C-cok/C-rank; C-rank = norma de intersección = G2; Example 6.5 como raíz; tolerancia repara C-cok no C-rank); Doc 121/120/100/105/99/72/108 (vía las anteriores).

**Clásica (contexto, vía Doc 119 §2.3, no re-verificada en fuente esta sesión):** índice de Hodge sobre superficies, signatura (1,ρ−1) de NS(S); Castelnuovo–Severi en NS(C×C); Weil 1948; Mattuck–Tate 1958; Grothendieck 1958.

*Fin del Doc 124.*
