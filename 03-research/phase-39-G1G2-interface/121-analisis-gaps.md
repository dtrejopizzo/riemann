# Doc 121 — Análisis de gaps: la maquinaria CC medida contra los axiomas forzados

**Programa:** Hipótesis de Riemann — Phase 39, interfaz G1↔G2
**Fecha:** junio 2026
**Autor:** David Alejandro Trejo Pizzo
**Prerrequisitos:** Doc 119 (axiomas R-SIG, R-FIN, R-LEF-{POLO,PRIMOS,REG,FLUJO}, R-PESO(a)(b), R-NC, R-TRZ-1/2; orden R-SIG ≺ R-FIN ≺ R-LEF ≺ Newton; tensiones T1–T4); Doc 120 (inventario en fuente del corpus CC/CCM, junio 2026); roadmap-rh (nodos G1–G4, rutas A/B, especificación S1–S3, Thm. rank-sensitivity); Doc 110 (Thm. 4.3 de imposibilidad en ℱ; Prop. 4.5); Doc 108 (binariedad por ventana); Doc 105 (Thm. 5.5, divergencia de Mertens); Doc 100 (positividad arquimediana; Obstáculo O_SL); P35 (κ(Q)=2m); P43/P44 (cuantificador maestro; dicotomía).

**Disciplina de etiquetado (regla absoluta de esta fase):** cada enunciado lleva UNA etiqueta:
**[REQUISITO]** = derivado en Doc 119. **[DATO]** = verificado: del corpus CC vía Doc 120
(con su cita), o teorema del programa (con cita interna). **[GAP]** = lo que falta, con
precisión (qué propiedad, en qué espacio, con qué cuantificador). **[CONJETURA-INTERFAZ]**
= propuesta de puente, SIEMPRE como conjetura, con su falsador. **[NO VERIFICADO]** = de
memoria o no encontrado en fuente. NUNCA "probado" para nada nuevo. Una falsa victoria es
peor que un fracaso.

**Escala de calificación de gaps:**
- **COSMÉTICO** — notación/traducción; cerrable por reescritura.
- **TÉCNICO** — trabajo duro pero de tipo conocido (existe método con precedente).
- **CONCEPTUAL** — matemática nueva; no hay método con precedente directo.
- **POSIBLEMENTE-EQUIVALENTE-A-RH** — cerrar el gap parece RH-disfrazada (falla el test
  R-NC del Doc 119 en algún eslabón, o el eslabón está en NO-GO-LIST).

---

## 0. Resumen ejecutivo

La medición axioma por axioma (§1) y los cuatro cruces (§2) producen este mapa en
miniatura:

| axioma (Doc 119) | pieza CC más cercana (Doc 120) | calificación del gap |
|---|---|---|
| R-SIG | dualidad de Serre/Pontryagin con tolerancia (2205.01391, Thm 1.2) | **CONCEPTUAL** (con sub-experimento finito: cruce A) |
| R-FIN | dimensiones enteras dim_𝕊 en dim 1 (2306.00456) | **CONCEPTUAL** (bloqueado aguas arriba por R-SIG; el mecanismo Newton es TÉCNICO una vez haya N₀) |
| R-LEF-POLO | positividad/realización arquimediana (2006.13771; Doc 100 §4) | **TÉCNICO** (prueba de fuego parcial ya pasada) |
| R-LEF-PRIMOS | órbitas C_p del sitio de escala + traza de Connes 1999 | **TÉCNICO condicional a G1** (la identidad existe; falta el portador cohomológico) |
| R-LEF-REG | valor principal de Weil; término divergente 2h(1)log λ pendiente (2602.15941 §9.3) | **TÉCNICO**, con riesgo T2 declarado |
| R-LEF-FLUJO | flujo Frobenius 𝔽r_λ; correspondencias Ψ(λ) | mitad dinámica: **TÉCNICO**; mitad graduación: **CONCEPTUAL** |
| R-PESO(a) | (nada; solo los enteros del sitio: pendientes, grados) | **CONCEPTUAL** — el corazón del muro |
| R-PESO(b) | positividad arquimediana CC 2021 como "germen del índice de Hodge" (cita §4.4 Doc 120) | **CONCEPTUAL** en forma geométrica; **POSIBLEMENTE-EQUIVALENTE-A-RH** en toda uniformización analítica (MW-6/O_SL) |
| R-NC | (es un test, no un gap) | transversal; aplicado en §2 |
| R-TRZ-1 | tests C_c^∞ con soporte compacto del marco semilocal | **TÉCNICO**, con el paso de riqueza generadora amenazado por O_SL |
| R-TRZ-2 | (disciplina de orden) | **COSMÉTICO** como enunciado; bloqueado aguas arriba |

Veredicto de los cruces: **(A)** dualidad→signatura: el divisor autodual EXISTE y es
explícito (D₀ = −{2}, exactamente K−D₀ = D₀, con χ(D₀) = 0: el análogo de una
característica theta); el cruce produce un experimento finito decisivo (¿el apareamiento
inducido es simétrico o alternante?) — pero aun en el mejor caso vive en dimensión 1,
donde no hay ceros: es el PROTOTIPO del mecanismo, no el mecanismo. **(B)**
tolerancia→cuadrado: el gap mejor calificado del documento (TÉCNICO, alto valor, riesgo
RH nulo); caso de prueba concreto: C_p × C_p. **(C)** Pick/Loewner→inercia: la matriz de
Weil truncada es exactamente un núcleo de tipo Loewner/Nevanlinna y la teoría clásica
(Krein–Langer, clases N_κ) es teoría de inercia — pero el análisis riguroso (§2.3.4)
muestra que **cae dentro de la clase ℱ del Doc 110 Thm 4.3**: no esquiva el teorema de
imposibilidad; su valor real es como infraestructura de la Ruta B *después* de R-FIN.
**(D)** Jacobiano→flujo espectral: especulativo, CONCEPTUAL, a estacionar.

**Experimento mínimo decisivo de la fase (§3.3):** computar el carácter de simetría del
apareamiento inducido por la dualidad de Serre con tolerancia en el punto autodual
D₀ = −{2}. Finito, en la categoría de CC, dos salidas limpias.

**Síntesis (§4):** G1 es "ellos ya casi lo tienen y no lo han cruzado" (años); G2 es
"nadie tiene una signatura en ninguna parte del corpus" (sin cota superior honesta de
tiempo); y el cuantificador maestro reaparece, en lenguaje geométrico, en exactamente
dos lugares identificados: la uniformización semilocal→global y la pertenencia de clase
de Krein–Langer.

---

## 1. LA TABLA CENTRAL: axioma por axioma

Formato de cada sección: (a) pieza CC más cercana [DATO]; (b) qué da exactamente hoy;
(c) el GAP preciso; (d) la [CONJETURA-INTERFAZ] de puente más corta, si existe, con
falsador; (e) calificación.

### 1.1. R-SIG — graduación de pesos con signatura entera

**[REQUISITO]** (Doc 119 §2.3). Descomposición W-graduada de H estable bajo el flujo,
pesos aditivos en ⊗, dualidad w ↔ 2d−w, y un criterio interno (forma, polarización o
valor absoluto) que decide pertenencia sin input externo; la graduación como dato
primitivo, NO el espectro del generador.

**(a) Pieza más cercana.** **[DATO]** (Doc 120 §3.2, arXiv:2205.01391 Thm 1.2): la
dualidad de Serre con tolerancia para Spec ℤ̄ sobre 𝕊[±1]:
H⁰(K−D) ≅ Hom_{ΓT∗}(H¹(D), U(1)_{1/4}), con divisor canónico K = −2{2}
(deg K = −2 log 2) y dualizante U(1)_{1/4} = H¹(K). Es el único apareamiento de dualidad
genuino del corpus. Secundaria: **[DATO]** (Doc 120 §7.2) la coexistencia de Dim_ℝ
(tipo II, 1603.03191) y dim_𝕊 (entera, 2306.00456): CC ya cruzaron "promedios → enteros"
en dimensión 1 *para dimensiones*.

**(b) Qué da hoy.** Un apareamiento de dualidad **perfecto entre dos espacios
distintos** (H¹ del divisor contra H⁰ del divisor dual), con valores en U(1) y con una
relación de tolerancia (no una igualdad estricta) como parte constitutiva. Dimensiones
enteras de ambos lados. Simetría de dualidad D ↔ K−D — el análogo formal de w ↔ 2d−w en
grados: deg D + deg(K−D) = deg K, constante. Nada más: **[DATO]** (Doc 120 §7.7,
búsqueda negativa) la palabra "signatura/índice de inercia" no aparece como invariante
en ningún texto leído del corpus; la única estructura de signo es
positividad/lower-boundedness.

**(c) [GAP]** Con cuantificadores: falta una forma bilineal (o cuadrática, o hermitiana)
B: V × V → ℝ (o a un ordenado donde "signatura" tenga sentido) sobre UN espacio V
asociado funtorialmente al sitio (en última instancia: al cuadrado), tal que (i) B es
simétrica — no alternante —, (ii) su inercia (p, q) está definida y es estable, (iii)
existe una graduación W con V_impuro = soporte de la parte indefinida. Hoy: no existe B,
no existe V, no existe W, en ninguna dimensión, sobre ninguna base. Lo que existe es el
ingrediente del que clásicamente se FABRICA B: una dualidad perfecta más una involución
candidata (D ↦ K−D).

**(d) [CONJETURA-INTERFAZ]** La del cruce A (§2.1): el punto fijo explícito D₀ = −{2}
de la involución de Serre convierte la dualidad en un apareamiento de un solo divisor, y
la suma H⁰(D₀) ⊕ H¹(D₀) porta una forma inducida cuya simetría es decidible por cómputo
finito. Falsadores en §2.1.5. Aun si el puente se tiende, queda en dimensión 1: el
espacio que porta los ceros es otro (ver (e)).

**(e) Calificación: CONCEPTUAL.** La traducción dualidad→forma es clásica (COSMÉTICA en
geometría ordinaria), pero aquí hay tres obstrucciones no clásicas: la tolerancia (¿rompe
la bilinealidad?), el dualizante U(1) (¿se deja linealizar a ℝ con signos?), y — la
decisiva — que todo ocurre en dimensión 1, donde H¹(D) ≅ U(1)_λ es minúsculo y **no ve
ceros**. El R-SIG verdadero debe vivir sobre el cuadrado (G1), que no existe. El gap es
matemática nueva con un experimento finito adentro.

### 1.2. R-FIN — finitud de la parte impura de H¹, a priori, acotando κ(Q)

**[REQUISITO]** (Doc 119 §2.4): dim(⊕_{w≠1} gr^W_w H¹) < ∞, acotada a priori por datos
del sitio, con teorema de acompañamiento "toda dirección negativa de Q proviene de ahí"
cuya prueba no mencione ceros. No enunciable sin R-SIG.

**(a) Pieza más cercana.** **[DATO]** (Doc 120 §3.3, arXiv:2306.00456): dimensiones
enteras dim_𝕊 H⁰(D), dim_𝕊 H¹(D) en dimensión 1, con fórmula RR exacta
χ(D) = ⌈deg₂ D⌉′ + 1 ("analogía perfecta con género 0", textual de CC), y H¹(D) ≅
(U(1), d)_λ explícito con dim = m si 2^{−m−1} ≤ λ < 2^{−m}. Secundaria: **[DATO]**
(Doc 120 §7.4, 2511.22755 Prop. 3.3): QW_λ es acotada por abajo — CCM trabajan de facto
en el régimen κ < ∞ sin nombrar jamás el índice negativo como invariante.

**(b) Qué da hoy.** Enteros computados del sitio (de la base absoluta), sin input de
ceros: exactamente la mitad "característica de Euler" de la prueba de fuego del Doc 119
§2.5. La otra mitad — el teorema de acompañamiento — no existe ni puede existir todavía:
**[DATO]** (Doc 120 §8, fila S1) todo el RR de CC produce características de Euler,
nunca signaturas; **[DATO]** (Doc 119 §2.2, Doc 110 §5.2 L6) una característica de Euler
no determina inercia en rango infinito.

**(c) [GAP]** Doble, y ordenado: (i) gap de enunciabilidad — sin W (R-SIG) no hay
"parte impura" que medir; el cuantificador faltante es "∃ V ⊂ H¹ funtorial, dim V ≤ N₀
computable del sitio, ∀ dirección negativa de Q: proviene de V"; (ii) gap de portador —
los enteros de CC son de Spec ℤ̄ en dimensión 1; la parte impura, si existe, vive en el
H¹ del cuadrado (las clases asociadas a cuádruplos off-críticos son objetos del análogo
de NS(C×C), no de Pic(C)).

**(d) [CONJETURA-INTERFAZ]** La más corta disponible es derivada, no directa: si el
cruce B (§2.2) entrega un H¹ del cuadrado con dimensiones enteras tipo dim_𝕊, y el cruce
A entrega el mecanismo dualidad→forma, entonces N₀ = dim_𝕊 (graduado impuro del H¹ del
cuadrado) sería el candidato. Falsador inmediato heredado del Doc 119 §2.4: si el H¹ del
cuadrado resulta finito-dimensional EN TOTAL, la propuesta muere por T1 (un H finito no
puede portar la traza con soporte singular en {k log p}); la finitud debe ser de un
graduado, y eso vuelve a presuponer R-SIG.

**(e) Calificación: CONCEPTUAL** — pero con precisión: el componente "leer la inercia
desde N₀ trazas" es TÉCNICO y ya probado (**[DATO]** Doc 110 Prop. 4.5; roadmap Thm.
rank-sensitivity); el componente "obtener N₀ del sitio con el teorema de
acompañamiento" es CONCEPTUAL y es, junto con R-PESO, el muro mismo. Riesgo señalado: si
alguien propone obtener N₀ como límite de cotas por ventana, eso está en NO-GO-LIST
(**[DATO]** Doc 108 Prop. 2.5 vía Doc 110 Thm 4.3(b): cota uniforme de índice por
ventana es RH-de-peaje) — esa variante sería POSIBLEMENTE-EQUIVALENTE-A-RH y debe
rechazarse en la puerta.

### 1.3. R-LEF-POLO — H⁰/H² de rango uno produciendo ĥ(±i/2)

**(a) Pieza más cercana.** **[DATO]** (Doc 100 §4 vía Doc 119 §3.2; CC Selecta 27
(2021)): el término arquimediano + polar de la fórmula de Weil tiene realización
operatorial positiva en soporte (1/2, 2) — única prueba de fuego parcial ya pasada por
la candidata CC. Además **[DATO]** (Doc 120 §3.4, 2602.15941 §9): la acción de C_ℚ sobre
el Picard enmarcado produce una fórmula de trazas tipo Lefschetz con localización en
órbitas periódicas.

**(b) Qué da hoy.** Los VALORES correctos del bloque polar en una ventana, desde una
construcción operatorial. No da: los portadores H⁰, H² como objetos cohomológicos de
rango 1 y pesos 0 y 2 con el flujo actuando por los caracteres triviales.

**(c) [GAP]** Falta exhibir, en la teoría del cuadrado (cuando exista), dos objetos de
rango uno cuya traza de flujo sea exactamente ĥ(−i/2) + ĥ(i/2), ∀ h en la clase 𝒯. En
dimensión 1 absoluta hay un candidato natural no explorado: H⁰(0) y H¹(K) = U(1)_{1/4}
(el dualizante mismo) como análogos de H⁰ y H² de la curva. **[NO VERIFICADO]** que CC
hagan esa identificación en parte alguna.

**(d) [CONJETURA-INTERFAZ]** El par (H⁰(0), H¹(K)) del RR absoluto es el par
(H⁰, H²) del objeto-curva, y la traza del flujo de escala sobre ellos reproduce el
bloque polar. Falsador: cómputo finito — la acción de ℝ₊^× sobre U(1)_{1/4} está
determinada en su categoría; si el carácter resultante no es el módulo (el carácter de
escala), la identificación es falsa. Es una verificación de tipo conocido.

**(e) Calificación: TÉCNICO.** El único axioma donde la candidata ya pasó media prueba.

### 1.4. R-LEF-PRIMOS — trazas locales = distribuciones W_p

**(a) Pieza más cercana.** **[DATO]** (Doc 120 §2.2): las órbitas periódicas
C_p = ℝ₊^*/p^ℤ del sitio de escala, una por primo, de longitud log p — la estructura
local pedida existe como GEOMETRÍA. Y **[DATO]** (Doc 119 §3.4; Connes, Selecta 5
(1999)): la traza distribucional del flujo sobre el espacio de clases de adeles
reproduce el lado aritmético término a término — la identidad es un teorema, en la
realización de adeles.

**(b) Qué da hoy.** Las dos mitades por separado: la geometría local (C_p, con su RR
tropical, Jacobiano ℤ/(p−1)) y la identidad analítica (traza de Connes). No da: la traza
local computada DESDE la cohomología de un H del cuadrado, porque ese H no existe.

**(c) [GAP]** Con cuantificador: ∀ p, la traza local del flujo sobre la pieza de H
correspondiente a C_p (o sobre la fibra de la correspondencia en p) debe = W_p, computada
desde H con ambos lados independientes (prueba de fuego R-LEF-FLUJO del Doc 119: si es
definición, G3 es vacuo). El gap no es la identidad — es el portador.

**(d) [CONJETURA-INTERFAZ]** Si el cruce B produce H¹ con tolerancia sobre C_p × C_p,
la traza de la correspondencia de Frobenius restringida a esa pieza debería dar W_p; el
caso de prueba de §2.2 incluye esta verificación como su paso 4. Falsador: la traza
computada da W_p solo tras normalización dependiente de p no explicable por el
determinante transverso de Guillemin.

**(e) Calificación: TÉCNICO condicional a G1.** Sin G1 no hay dónde computar; con G1,
el patrón (Guillemin + Connes 1999) es de tipo conocido.

### 1.5. R-LEF-REG — regularización arquimediana como contrapeso

**(a) Pieza más cercana.** **[DATO]** (Doc 100 §5 vía Doc 119): la aditividad por
lugares del lado geométrico de Weil es incondicional, y el lugar arquimediano tiene su
realización (CC 2021). **[DATO]** (Doc 120 §3.4): en 2602.15941 §9.3 queda un término
divergente 2h(1) log λ en la fórmula semilocal "cuyo tratamiento riguroso está
pendiente" — CC están tocando exactamente esta pared ahora mismo.

**(b) Qué da hoy.** El valor principal de Weil funciona en la fórmula explícita
analítica (clásico); en la realización geométrica nueva (Picard/Jacobiano 2026) la
divergencia reaparece sin tratar.

**(c) [GAP]** Falta: una contribución local arquimediana del MISMO TIPO formal que las
p-ádicas (órbita/punto del sitio) tal que la identidad de trazas valga para la suma
total regularizada, en una clase de tests con margen ε. Y — la tensión T2 (Doc 119
§6.3) — compatibilidad declarada con R-SIG: la signatura debe definirse antes del límite
regularizador, no leerse de él. **[DATO]** (Doc 105 Thm. 5.5): en la frontera de la
clase de Weil la suma de primos diverge tipo Mertens; cualquier teoría que herede esa
frontera hereda la ilegitimidad de la lectura por términos.

**(d) [CONJETURA-INTERFAZ]** El punto {2} ya juega en el RR absoluto el rol de "punto
en el infinito" (interpretación registrada en Doc 120 §3.3); conjetura: el lugar
arquimediano del sitio admite una presentación como órbita degenerada (longitud
infinitesimal) cuyo determinante transverso regularizado ES el valor principal de Weil.
Falsador: si el término 2h(1) log λ de 2602.15941 §9.3 no es cancelable por NINGUNA
contribución local del borde del monoide de Picard (los fenómenos de borde que CC
declaran constitutivos), la presentación no existe en su marco.

**(e) Calificación: TÉCNICO** — con la advertencia de que es el requisito sin análogo
en char p (Doc 119 §3.3): "de tipo conocido" aquí significa "del tipo de Weil 1952 y
Connes 1999", no "del template".

### 1.6. R-LEF-FLUJO — traza de Guillemin + graduación independiente del espectro

**(a) Pieza más cercana.** **[DATO]** (Doc 120 §1.3, 1502.05580 Thm 1.1): el flujo de
escala ES Frobenius (la acción de 𝔽r_λ sobre los puntos = grupo de clases de ideles); y
Thm 1.2: el semigrupo de correspondencias Ψ(λ) sobre el cuadrado, con composición exacta
para λλ′ ∉ ℚ. **[DATO]** (Doc 106 Prop. 3.10 vía Doc 120 §7.6): sobre (𝒦, Q) las
correspondencias de Frobenius actúan por isometrías — miden, no generan, el defecto.

**(b) Qué da hoy.** La mitad dinámica entera: flujo, correspondencias, traza
distribucional (en adeles), órbitas correctas. La mitad estructural — la graduación W
como dato primitivo dentro del cual el flujo actúa — en cero.

**(c) [GAP]** Dos: (i) la discontinuidad racional de la composición Ψ(λ)∘Ψ(λ′) ≠
Ψ(λλ′) para λλ′ ∈ ℚ — el análogo de "Frobenius compuesto exacto" falla justo en los
valores aritméticos; cuantificador: ∀ λ, λ′ (sin excepción) o bien una explicación
estructural de la excepción (¿es el fenómeno de borde del monoide?); (ii) la graduación
sobre la que el flujo actúe: no existe (es R-SIG otra vez).

**(d) [CONJETURA-INTERFAZ]** La discontinuidad racional de Ψ y los "boundary/singular
phenomena" del paso grupo→monoide (2602.15941) son el mismo fenómeno visto en dos
lugares; el cuadrado correcto debe construirse sobre el monoide (no el grupo) para que
la composición sea exacta. Falsador: reformular Ψ(λ) en el lenguaje de Picard-monoide y
verificar la composición en un caso racional concreto; si la anomalía persiste, la
conjetura es falsa. **[NO VERIFICADO]** — nadie ha escrito Ψ(λ) en ese lenguaje.

**(e) Calificación:** mitad dinámica **TÉCNICO**; mitad graduación **CONCEPTUAL**
(es R-SIG). La prueba de fuego del Doc 119 ("ambos lados computados por separado")
no es evaluable hasta tener portador.

### 1.7. R-PESO(a) — el invariante w computable desde H, no desde ρ

**(a) Pieza más cercana.** Estrictamente: ninguna. Los únicos enteros funtoriales del
sitio son **[DATO]** (Doc 120 §2.2, §3): pendientes enteras del haz de estructura,
grados (reales, no enteros) de divisores tropicales, la característica torsional
χ ∈ ℤ/(p−1) de C_p, y las dim_𝕊 del RR absoluto.

**(b) Qué da hoy.** Materia prima de enteros, sin ninguna asignación clase-de-cero →
entero. **[DATO]** (Doc 120 §8, lectura 1): CC tienen dualidad pero "ninguna forma
bilineal sobre un solo espacio con índice de inercia"; la pregunta de la interfaz
("¿qué condición hace que la dualidad de la diagonal se refine a una forma con
signatura?") no está planteada en su corpus.

**(c) [GAP]** El central del programa: ∀ clase c_ρ ∈ H¹ (cuando H¹ exista), un
w(c_ρ) ∈ ℤ computable por pertenencia a graduado/signo bajo forma/clase algebraica que
la corta — sin mencionar ρ. **[DATO]** (Doc 110 Thm 4.3(b); Doc 108 §7.4): dentro de la
clase ℱ esto es imposible; el gap es construir la categoría DONDE sea posible.

**(d) [CONJETURA-INTERFAZ]** Ninguna corta y honesta. La más cercana es la composición
de los cruces A y B: forma del punto autodual (mecanismo) + H¹ del cuadrado con
tolerancia (portador) + signo bajo la forma como definición de w. Tres eslabones, dos de
ellos conjeturas a su vez. Se declara la cadena, no se acorta.

**(e) Calificación: CONCEPTUAL.** Es el muro. Sin sub-experimento propio: sus
sub-experimentos son los de los cruces A y B.

### 1.8. R-PESO(b) — pureza como teorema desde positividad geométrica

**(a) Pieza más cercana.** **[DATO]** (Doc 120 §4.2, 2006.13771 Thm 1 y Thm 6.11): la
positividad arquimediana W_∞(g∗g^*) ≥ Tr(ϑ(g)𝐒ϑ(g)^*) ≥ 0 en soporte (1/2,2), con
defecto cuantificado 13 < c < 17 en una sola dirección ĝ(0). **[DATO]** (Doc 120 §4.4,
cita clave): CC mismos la presentan como parte de "a novel geometric landscape still in
development for an intersection theory of divisors (on the square of the Scaling
Site)" — para ellos ES el germen analítico del índice de Hodge del cuadrado.

**(b) Qué da hoy.** Una positividad incondicional REAL (la única del corpus), con
sobregeneración parcial (vale ∀ test de soporte en (1/2,2) — pasa parcialmente NC2,
**[DATO]** Doc 119 §4.3), en un lugar.

**(c) [GAP]** Con cuantificadores, el gap tiene dos formas y SOLO una es legítima:
- Forma analítica: ∀ S finito de lugares, positividad semilocal, y uniformización
  S → todos los lugares. **[DATO]** (Doc 100, Obstáculo O_SL; Doc 119 §4.3, "estado de
  la candidata"): la uniformización en λ es MW-6 — **este camino está en NO-GO-LIST**.
- Forma geométrica: UNA desigualdad de tipo Castelnuovo sobre el cuadrado, ∀ divisor
  (no solo la gráfica del flujo), probada por método uniforme de superficies, de la que
  la cota de pesos se siga por el argumento de Weil. No existe ni el cuadrado con
  divisores.

**(d) [CONJETURA-INTERFAZ]** La de CC, explicitada: su positividad arquimediana es la
restricción a la gráfica-cerca-de-la-diagonal de una desigualdad de intersección del
cuadrado aún no formulada. Falsador estructural (test NC2): cuando exista la teoría de
intersección, la desigualdad debe ser demostrable para divisores que NO codifican ζ
(p. ej. divisores soportados en una sola órbita C_p × C_q); si solo se puede verificar
para el objeto que codifica ζ, era MW-1 con disfraz.

**(e) Calificación: bifurcada y hay que decirlo sin rodeos.** La forma geométrica:
**CONCEPTUAL** (el precedente Castelnuovo/Mattuck–Tate muestra que PUEDE ser
no-circular: un teorema de superficies que ignora qué curva es). Toda variante que pase
por uniformización semilocal→global en la categoría analítica:
**POSIBLEMENTE-EQUIVALENTE-A-RH** — es MW-6, catalogado, y es la amenaza de §4.3.

### 1.9. R-NC — el test de no-circularidad

No es un gap de CC sino el instrumento de medición. Estado de aplicación: **[DATO]**
(Doc 119 §4.3) la positividad CC 2021 pasa NC1, parcialmente NC2, y FALLA hoy NC3 en el
paso global (MW-6). En este documento, R-NC se aplica a cada cruce de §2 (resultados:
cruce A pasa NC1–NC2 en su construcción, §2.1.6; cruce B pasa trivialmente, §2.2.4;
cruce C falla NC4 — cae en ℱ, §2.3.4). Calificación: **transversal, no calificable**.

### 1.10. R-TRZ-1 — clase de tests con margen y riqueza generadora

**(a) Pieza más cercana.** **[DATO]** (Doc 120 §4.2): la clase de tests del marco
semilocal CC: g ∈ C_c^∞ con soporte compacto multiplicativo (ventana (1/2,2);
condición Supp(f) ⊂ (p^{−1}, p) que crece con S, **[DATO]** Doc 100 §5).

**(b) Qué da hoy.** Margen ε resuelto con creces: para soporte compacto multiplicativo,
el lado de primos es una SUMA FINITA (solo finitos p^k caen en el soporte) — mejor que
el margen estricto pedido; la divergencia de Mertens del Doc 105 no toca esta clase.
Numerabilidad: trivial (densidad separable de C_c^∞).

**(c) [GAP]** La riqueza generadora (cláusula (b) de R-TRZ-1) choca con la geometría de
la ventana: una test de soporte en (p^{−1}, p) solo "ve" los primos < p; para que la
familia {h_n} genere (triangularidad sobre polinomios pares, Doc 118 Lema 5.2) los
soportes deben crecer sin cota — y el comportamiento uniforme en ese crecimiento es
exactamente el Obstáculo O_SL. Cuantificador del gap: ∃ {h_n} ⊂ 𝒯 generadora TAL QUE
las identidades de traza usadas por la Ruta B solo requieran cada h_n por separado
(nunca uniformidad en n).

**(d) [CONJETURA-INTERFAZ]** Con R-FIN en mano (N₀ conocido), bastan N₀ tests de
soportes FIJOS (los primeros N₀ de la familia triangular): la uniformidad en n
desaparece del circuito porque el cuantificador universal se trunca. Falsador: si la
compresión al bloque impuro (R-TRZ-2) requiere tests de soporte creciente para
separarlo, la truncación no se da y O_SL reentra.

**(e) Calificación: TÉCNICO**, condicional al orden: después de R-FIN es rutina; antes
de R-FIN, cualquier intento de usar esta clase para leer inercia reabre O_SL
(POSIBLEMENTE-EQUIVALENTE-A-RH por esa puerta).

### 1.11. R-TRZ-2 — el orden R-SIG ≺ R-FIN ≺ R-LEF/R-TRZ-1 ≺ Newton

**(a)–(b)** No corresponde a una pieza CC: es disciplina del programa. La medición
relevante: **[DATO]** (Doc 120 §5.5, interpretación registrada): la línea "zeta spectral
triples" de CCM viola de facto este orden — evalúa trazas truncadas y posterga TODA la
estructura a un enunciado de convergencia, que es el patrón O_SL.

**(c) [GAP]** Ninguno propio; hereda los de aguas arriba.

**(e) Calificación: COSMÉTICO** como enunciado (es un protocolo), con valor de
detector: cualquier propuesta de interfaz que evalúe trazas antes de exhibir N₀ se
rechaza por este axioma sin examinar el resto.

---

## 2. LOS CRUCES PROMETEDORES

### 2.1. Cruce A — DUALIDAD→SIGNATURA: el divisor autodual del RR absoluto

#### 2.1.1. El dato de partida

**[DATO]** (Doc 120 §3.2; arXiv:2205.01391, Thm 1.2 y Prop. 5.2): dualidad de Serre con
tolerancia H⁰(K−D) ≅ Hom_{ΓT∗}(H¹(D), U(1)_{1/4}), derivada de dualidad de Pontryagin
para 𝕊[±1]-módulos con tolerancia; K = −2{2}, deg K = −2 log 2; dimensiones enteras de
ambos lados. El apareamiento subyacente: P: H¹(D) × H⁰(K−D) → U(1), perfecto.

**[REQUISITO]** (R-SIG, Doc 119 §2.3, realización (i)): una forma sobre UN espacio con
involución, cuya signatura sea el invariante.

La pregunta de interfaz, en su forma clásica: un apareamiento de dualidad
P: A × B → U(1) se convierte en forma sobre A cuando hay un isomorfismo B ≅ A — es
decir, cuando el divisor está en posición autodual respecto de la involución de Serre
σ: D ↦ K−D.

#### 2.1.2. El divisor autodual existe y es explícito

La condición de punto fijo es D ~ K − D, i.e. 2D ~ K = −2{2}. Hay una solución **exacta
a nivel de divisores, no solo de clases**:

$$D_0 := -\{2\}, \qquad K - D_0 = -2\{2\} + \{2\} = -\{2\} = D_0.$$

**[DATO]** (aritmética inmediata de los enunciados verificados en Doc 120 §3.2–3.3; no
requiere nada nuevo de la fuente): D₀ = −{2} es punto fijo EXACTO (no salvo equivalencia
lineal) de la involución de Serre, con deg D₀ = −log 2, deg₂ D₀ = −1.

Tres consecuencias computables con las fórmulas verificadas de CC:

1. **χ(D₀) = 0.** Por RR sobre 𝕊 (2306.00456, Thm 1.1): χ(D₀) = ⌈deg₂ D₀⌉′ + 1 =
   ⌈−1⌉′ + 1 = 0. **[DATO]** (consecuencia aritmética directa de la fórmula verificada).
2. **El análogo clásico es exacto:** en una curva de género g, χ(D) = 0 ⟺ deg D = g−1,
   y los puntos con 2D ~ K son las **características theta**; D₀ es la característica
   theta de Spec ℤ̄. En el modelo declarado por CC ("género 0"): deg K_{ℙ¹} = −2,
   característica theta O(−1), χ = 0, h⁰ = h¹ = 0 genéricamente. La consistencia es
   perfecta. **[CONJETURA-INTERFAZ]** la lectura "D₀ = característica theta aritmética";
   **[DATO]** cada igualdad numérica por separado.
3. **D₀ está en el borde de salto de la dimensión:** con λ = e^{deg D₀} = 1/2, la
   Prop. 4.2 de 2306.00456 (dim_𝕊 U(1)_λ = m si 2^{−m−1} ≤ λ < 2^{−m}) evalúa λ = 1/2
   exactamente en el extremo del intervalo (m = 0, con λ = 2^{−m−1} en el borde
   inferior). El punto autodual cae en el lugar de salto de h⁰/h¹ — el análogo del
   divisor theta {h⁰ > 0} ⊂ Pic^{g−1}. **[DATO]** la evaluación; **[INTERPRETACIÓN]**
   etiquetada como tal: que el salto sea significativo y no un artefacto de
   normalización. Conexión con el cruce D: los saltos de dimensión son los "boundary
   phenomena" que CC declaran constitutivos del paso grupo→monoide.

#### 2.1.3. La conjetura central, por pasos

**[CONJETURA-INTERFAZ] (121.A — dualidad→forma en el punto autodual).** Existe una
forma sobre un solo espacio, construida así:

- **Paso 1 (identificación).** En D₀, la dualidad da H⁰(D₀) ≅ Hom(H¹(D₀), U(1)_{1/4}):
  un apareamiento perfecto P: H¹(D₀) × H⁰(D₀) → U(1).
- **Paso 2 (el espacio único).** Defínase V := H⁰(D₀) ⊕ H¹(D₀) (el análogo del
  H¹ de De Rham total: en una curva clásica, H¹(C) = H⁰(K_θ) ⊕ H¹(O_θ) para la
  polarización en la característica theta). La involución de Serre actúa sobre V
  intercambiando los sumandos.
- **Paso 3 (las dos formas candidatas).** Sobre V, P induce
  B_±((a,b),(a′,b′)) := P(b, a′) ± P(b′, a), con valores en U(1). B₊ es simétrica,
  B₋ es alternante; cuál de las dos es la CANÓNICA (la compatible con la estructura de
  ΓT∗ y con la involución) es un hecho de su categoría, no una elección nuestra: la
  decide el carácter de simetría del isomorfismo de dualidad
  (si el cuadrado de la dualidad H¹ → (H¹)^∨∨ es +1 o −1 — el análogo exacto de la
  dicotomía dualidad simétrica/simpléctica de las teorías de Weil, donde H^i con i impar
  porta forma ALTERNANTE por cup product).
- **Paso 4 (linealización).** Para hablar de signatura, B debe levantarse de U(1) a ℝ:
  un refinamiento cuadrático q: V → ℝ con B(x,y) = q(x+y) − q(x) − q(y) compatible con
  la tolerancia 1/4.
- **Paso 5 (la signatura candidata).** sig(V, B₊ linealizada) es el candidato a
  invariante R-SIG en dimensión 1 — el PROTOTIPO del mecanismo que el cuadrado debería
  repetir en grande.

#### 2.1.4. Los falsadores, en orden de letalidad

- **F-A1 (simetría — el decisivo).** Si el carácter de la dualidad es antisimétrico
  (B₋ canónica, B₊ no definible), la forma es simpléctica: NO HAY signatura, solo
  invariantes mod 2 (Arf). El precedente clásico es desfavorable y hay que decirlo: en
  TODA cohomología de Weil, el cup product en H¹ (grado impar) es alternante, y la
  teoría clásica de características theta produce exactamente una forma cuadrática
  mod 2 sobre la 2-torsión (Mumford; Atiyah) cuyo invariante es la PARIDAD de h⁰(θ) —
  un bit, no un entero. Si Spec ℤ̄ sigue ese patrón, el cruce A entrega ℤ/2 donde R-SIG
  pide ℤ: insuficiente para κ(Q) = 2m (que ya es par: la paridad es ciega a m). La vía
  de escape clásica también existe y hay que nombrarla: la signatura entera NO sale del
  cup product solo sino de la POLARIZACIÓN (Hodge–Riemann: i^{p−q} y primitividad
  convierten la forma alternante en hermitiana definida por piezas). Traducción: aun en
  el mejor desenlace, el cruce A necesita el análogo del operador de Lefschetz/estrella
  de Hodge, que en el corpus CC no existe. El falsador F-A1 decide si el camino se corta
  en el paso 3 o sigue al paso 4.
- **F-A2 (tolerancia vs bilinealidad).** La dualidad es "con tolerancia": los morfismos
  ΓT∗ respetan relaciones R_k, no igualdades. Si la tolerancia hace que P esté bien
  definida solo hasta una relación no transitiva, B no es una forma sino una
  "forma hasta tolerancia", y la inercia puede no estar definida (los autovalores cerca
  de 0 quedan dentro de la banda de tolerancia — exactamente la situación T2 del
  Doc 119: signaturas no sobreviven límites sin gap). Verificación: ¿la tolerancia 1/4
  de U(1)_{1/4} induce en B una ambigüedad aditiva acotada (inofensiva para signos de
  autovalores grandes) o multiplicativa (letal)? Es computable en su categoría.
- **F-A3 (linealización).** U(1) no es ordenado; el levantamiento q: V → ℝ puede no
  existir (obstrucción tipo Bockstein de la sucesión ℝ → U(1)). Si no existe, hay
  "forma de enlace" (linking form, como en 3-variedades: torsión con valores en
  ℚ/ℤ) — invariantes finitos, no signatura. De nuevo: datos de torsión donde se piden
  enteros con signo.
- **F-A4 (trivialidad).** Si dim H⁰(D₀) = dim H¹(D₀) = 0 (lectura genérica del punto
  borde, §2.1.2.3), la forma es vacía y el contenido del cruce está enteramente en el
  SALTO (el comportamiento al perturbar D₀) — es decir, en una teoría de degeneración
  que conecta con el cruce D, no en un cómputo puntual.

#### 2.1.5. El test R-NC aplicado al cruce A

- **NC1 (externalidad):** PASA. La construcción usa divisores de Arakelov sobre
  Spec ℤ̄, Γ-anillos, la involución de Serre: ζ no aparece, ni sus ceros, ni operadores
  cuyo espectro los codifique. El discriminador de sustitución se satisface: la
  construcción no sabe qué L-función "es" — de hecho ese es su defecto (ver abajo).
- **NC2 (sobregeneración):** PASA en su nivel: la involución σ está definida ∀ D, la
  construcción de B en cualquier punto fijo de σ módulo equivalencia (∀ D con 2D ~ K),
  y los falsadores F-A1–F-A3 son preguntas sobre TODA la categoría ΓT∗, no sobre un
  objeto que codifique ζ.
- **NC3/NC4:** NO EVALUABLES aún — y esta es la calificación honesta: la forma del
  cruce A, si existe, es un teorema de SU geometría (dimensión 1), y precisamente por
  eso **no individúa ceros**: H¹(D₀) no porta clases c_ρ. La positividad/signatura de
  B sería matemática de CC, no RH-disfrazada — porque está demasiado lejos de ζ para
  disfrazar nada. El riesgo de circularidad se traslada íntegro al momento (futuro) de
  repetir el mecanismo sobre el cuadrado, donde NC3/NC4 deberán aplicarse de nuevo.

**Calificación del cruce A: CONCEPTUAL con núcleo experimental finito.** Valor real:
es el único lugar del corpus mundial donde "dualidad aritmética absoluta" y "forma con
posible signatura" están a UN isomorfismo explícito de distancia, y el desenlace
(simétrica/alternante; linealizable/no) es decidible por cómputo en una categoría que
ya existe. Valor acotado: todo ocurre en dimensión 1 — es el banco de pruebas del
mecanismo, no el mecanismo.

### 2.2. Cruce B — TOLERANCIA→CUADRADO: los null elements de Čech

#### 2.2.1. Los dos datos y la cronología que importa

**[DATO]** (Doc 120 §6.3; arXiv:1805.10501, textual): el bloqueo auto-declarado de CC
para RR en el cuadrado del sitio de escala es "an appropriate definition of the sheaf
cohomology (as idempotent monoid) H¹... when applied to Čech covers, the presence of
the null elements creates unwanted contributions to the cohomology which so far we are
unable to handle".

**[DATO]** (Doc 120 §3.2, §6.4): la técnica de TOLERANCIA (𝕊-módulos con relación R_k,
Dold–Kan sobre Γ-anillos) que produce el primer H¹ del programa CC es de 2022–23 —
POSTERIOR a la declaración del bloqueo (2018) — y funciona en dimensión 1 para
Spec ℤ̄. **[DATO]** (Doc 120 §6.4): CC no enuncian explícitamente la conexión
"tolerancia resuelve los null elements"; es lectura del programa, registrada como
plausible y NO VERIFICADA como afirmación de ellos.

El diagnóstico estructural de por qué la conjetura es natural: el problema de los
elementos nulos es que en un semianillo idempotente el 0 es absorbente y la "igualdad a
cero" en cociclos de Čech no es una condición lineal — produce clases parásitas. La
relación de tolerancia reemplaza "x = y" por "x − y ∈ imagen(ψ) con control de norma":
es exactamente un mecanismo para declarar despreciables elementos casi-nulos sin
cocientar por ellos (cociente que en el mundo idempotente no existe bien). Que el
mecanismo diseñado para el conúcleo de ψ en dim 1 sea el adecuado para los cociclos del
cuadrado es la conjetura — no un hecho.

#### 2.2.2. La conjetura y el programa de verificación ordenado

**[CONJETURA-INTERFAZ] (121.B — tolerancia sobre el cuadrado).** El complejo de Čech
del cuadrado del sitio de escala, reformulado en la categoría de 𝕊-módulos (o
𝕊[±1]-módulos) con tolerancia vía el cambio de base de semianillos idempotentes a
Γ-anillos, tiene H¹ bien definido: los null elements de 1805.10501 quedan en clases de
tolerancia triviales.

Programa de verificación, en orden de costo creciente:

1. **Cambio de base en dim 2 local.** Expresar el haz del cuadrado
   (ℤ_min ⊗_𝔹 ℤ_min; polígonos de Newton, **[DATO]** Doc 120 §6.1) como Γ-𝕊-módulo,
   verificando que la operación de envolvente convexa sobrevive al cambio de base.
   Riesgo: el producto tensorial sobre 𝔹 y el producto sobre 𝕊 pueden no conmutar con
   la tropicalización.
2. **El complejo de Čech con tolerancia.** Definir, para un recubrimiento finito del
   cuadrado, el complejo con relaciones R_k en cada grado, y Dold–Kan como en
   2205.01391 §5.
3. **El test de los null elements.** Identificar en un ejemplo mínimo las
   "unwanted contributions" exactas de 1805.10501 (cociclos soportados en elementos
   absorbentes) y computar su clase de tolerancia.
4. **EL CASO DE PRUEBA: C_p × C_p.** El cuadrado de UNA órbita periódica: compacto,
   con RR tropical conocido en cada factor (**[DATO]** Doc 120 §3.1), Jacobianos
   finitos ℤ/(p−1). Allí: (i) ¿H¹ con tolerancia es de dimensión 𝕊-entera computable?
   (ii) ¿vale un Künneth con los H⁰/H¹ del factor? (iii) ¿la traza de la
   correspondencia de Frobenius restringida reproduce el bloque W_p (conexión con
   R-LEF-PRIMOS, §1.4)? — tres salidas verificables.
5. **Funtorialidad bajo Ψ(λ)** y comportamiento en la anomalía racional (§1.6).

**Falsador del cruce:** el paso 3/4 — si en C_p × C_p los cociclos nulos persisten como
clases de tolerancia NO triviales (o si H¹ resulta de dimensión 𝕊-infinita sin
graduación que lo dome), la técnica de dim 1 no se extiende y el bloqueo de 2018 sigue
en pie con su formulación original.

#### 2.2.3. Qué entrega y qué NO entrega si cierra

Si la conjetura 121.B se verifica: **G1 se mueve** — habría por primera vez un H¹ sobre
(una pieza de) el cuadrado con dimensiones de tipo entero. Lo que NO entrega, dicho sin
adorno (**[DATO]** Doc 120 §8, lectura 2): G2 seguiría intacto — ni en dimensión 1,
donde la técnica YA funciona, hay signatura; la tolerancia produce característica de
Euler, y S1 exige signatura. El cruce B desbloquea el portador; el mecanismo de signos
es el cruce A.

#### 2.2.4. R-NC y calificación

NC1–NC2: pasa trivialmente (construcción de topos + álgebra categórica, sin ζ; método
uniforme para todos los recubrimientos). NC3/NC4: no aplican (no se pretende deducir
pureza de esto). Riesgo de RH-equivalencia: **nulo** — es el gap más limpio del
documento en ese eje.

**Calificación: TÉCNICO.** Trabajo duro de tipo conocido: el tipo es exactamente el que
CC ejecutaron en 2022–23 un piso más abajo. Es además el único gap de toda la tabla
cuyo cierre depende SOLO de matemática que el equipo CC ya domina — la definición
operativa de "ellos ya casi lo tienen y no lo han cruzado".

### 2.3. Cruce C — PICK/LOEWNER→INERCIA: ¿esquiva el teorema de imposibilidad?

#### 2.3.1. El dato

**[DATO]** (Doc 120 §5.2, §7.3; arXiv:2511.22755): la forma de Weil truncada de los
triples espectrales zeta tiene, en la base {V_n}, la estructura τ_ii = a_i,
τ_ij = (b_i − b_j)/(i − j) para i ≠ j, con paridades a_{−j} = a_j, b_{−j} = −b_j; CCM
la usan exclusivamente para autoadjunción de la perturbación de rango uno (vía la
extensión de Carathéodory–Fejér para matrices de Toeplitz).

La observación correcta del encargo: τ_ij = (b_i − b_j)/(i − j) es **exactamente una
matriz de Loewner**: L_Φ = [(Φ(x_i) − Φ(x_j))/(x_i − x_j)] con nodos x_i = i y valores
b_i = Φ(i). Y la teoría clásica de matrices de Loewner/Pick ES teoría de inercia:

**[DATO]** (literatura clásica): (i) Loewner 1934: Φ es operador-monótona ⟺ toda matriz
de Loewner de Φ es semidefinida positiva; (ii) Krein–Langer (clases N_κ de funciones de
Nevanlinna generalizadas): Φ ∈ N_κ ⟺ el núcleo de Nevanlinna
K_Φ(z, w) = (Φ(z) − Φ(w̄)^*)/(z − w̄) tiene a lo sumo κ cuadrados negativos, y
exactamente κ para colecciones suficientemente grandes de puntos — es decir, **la
inercia negativa de las matrices de Pick/Loewner truncadas se ESTABILIZA en un valor
finito κ característico de la clase de la función generadora** [Krein–Langer, *Über
einige Fortsetzungsprobleme...*, Math. Nachr. 77 (1977), y la serie sobre espacios Π_κ]
**[NO VERIFICADO el dato editorial exacto en esta sesión; el contenido matemático es
clásico y estable]**; (iii) la teoría de inercia de matrices de Hankel/Loewner
(Iohvidov; Fiedler) computa (p, q) por menores y reglas de saltos.

La rima con el programa es exacta y hay que registrarla: los espacios donde vive la
teoría N_κ son los espacios de Pontryagin Π_κ — la MISMA categoría donde P35 probó
κ(Q) = 2m. **[DATO]** (P35) + **[DATO]** (Krein–Langer) comparten hasta la letra κ.

#### 2.3.2. La conjetura

**[CONJETURA-INTERFAZ] (121.C — Loewner como lector de inercia).** Existe una función
generadora Φ (construida de los datos aritméticos b_i de la fórmula explícita) tal que
(i) la parte Loewner de QW_λ^N es la matriz de Pick de Φ en los nodos enteros; (ii)
Φ ∈ N_κ con κ = 2m (los cuadrados negativos del núcleo = el índice de la forma de
Weil); (iii) la estabilización de Krein–Langer de la inercia truncada en N → ∞ es la
versión Loewner de R-FIN.

#### 2.3.3. La pregunta decisiva: ¿la estructura especial esquiva el Thm 4.3 del Doc 110?

Esta es la pregunta técnica del cruce y se responde con rigor y en negativo.

**[DATO]** (Doc 110, Thm 4.3): en la clase ℱ de funcionales cuadráticos aritméticos con
compresiones test-accesibles, (L2 autonomía) + (L3 detección de inercia) + (L4
estabilidad sin peaje RH) son inconsistentes; **[DATO]** (Doc 108 vía Doc 110): los
índices por ventana son binarios (0 o ≍ m log T) y la inercia no es test-accesible en
rango infinito.

Análisis de pertenencia a ℱ, en tres pasos:

1. **Los datos de la matriz de Loewner son test-accesibles.** Las entradas a_i, b_i de
   QW_λ^N son valores de los funcionales de la fórmula explícita contra tests concretas
   (**[DATO]** Doc 120 §5.2: "the construction only involves the Euler products over
   the primes p ≤ λ²"). Por tanto TODA función de la matriz truncada — incluida su
   inercia — es un funcional cuadrático aritmético con compresiones test-accesibles:
   **la matriz de Loewner truncada está, entrada por entrada, DENTRO de la clase ℱ.**
   La "estructura especial" no añade información: es una propiedad sintáctica de cómo
   se organizan los mismos valores accesibles.
2. **Dónde estaría la información extra: en la CLASE de Φ, no en sus valores.** Lo que
   Krein–Langer convierte en finito (la estabilización en κ) es un atributo GLOBAL de
   la función generadora: pertenencia a N_κ, i.e. prolongación meromorfa con κ polos
   "negativos" en el semiplano. Para la función aritmética relevante eso no es neutral:
   **[DATO]** (catálogo del programa; clásico): "la derivada logarítmica de ξ
   (normalizada) es Herglotz/Pick en el semiplano Re s > 1/2" es una reformulación
   EXACTA de RH (todo cero off-crítico introduce un polo del lado prohibido = un
   cuadrado negativo). Por tanto el enunciado (ii) de la conjetura 121.C —
   "Φ ∈ N_κ con κ = 2m" — no es un puente: es la DEFINICIÓN de m en otro lenguaje.
   Pertenece a la familia MW (positividad de Weil reescrita como pertenencia a N_0);
   NC3 lo detecta: el eslabón "Φ ∈ N_0" ES MW-1 con disfraz de teoría de funciones.
3. **El umbral de estabilización no es a priori.** Krein–Langer garantiza que la
   inercia truncada alcanza κ para "suficientes puntos" — pero CUÁNTOS depende de dónde
   están las singularidades de Φ (los polos generalizados: las posiciones de los ceros
   off-críticos). Sin conocerlas, el N de estabilización no es computable: para todo N
   finito, inercia truncada 0 es compatible tanto con κ = 0 como con κ = 2m de ceros
   muy altos. Es EXACTAMENTE la binariedad del Doc 108 reescrita: el test NC4 falla
   (para saber si la propiedad falla en el mundo ¬RH hay que saber dónde está el
   cuádruplo). **Conclusión: la estructura Pick/Loewner cae dentro de la clase ℱ; no
   esquiva el teorema de imposibilidad.** La razón profunda: Loewner/Krein–Langer es
   maquinaria de LECTURA de inercia dado un κ finito de la clase; no es maquinaria de
   PRODUCCIÓN de la finitud de κ. La finitud de la clase es el input — y el input es
   R-FIN, que tiene que venir de otra parte (de la geometría).

#### 2.3.4. Lo que el cruce C sí vale

Rebajado de "cruce del muro" a su valor real, que no es pequeño:

- **Infraestructura de la Ruta B.** **[DATO]** (Doc 110 Prop. 4.5): con N₀ conocido,
  Newton lee la inercia de N₀ trazas. La forma Loewner mejora ese mecanismo: la teoría
  de inercia de Loewner/Hankel (reglas de Iohvidov, algoritmos de menores) computa
  (p, q) directamente de las entradas — sin pasar por potencias de la matriz — y la
  identificación con N_κ daría estabilidad estructural (la inercia leída es la κ de
  una clase, no un accidente del truncamiento). Si R-FIN llega algún día por vía
  geométrica, el dialecto Loewner es probablemente el formato en que la Ruta B se
  ejecuta.
- **El diccionario de categorías correcto.** La coincidencia Π_κ (P35) = Π_κ
  (Krein–Langer) sugiere enunciar el puente G4→P35 en lenguaje de funciones N_κ:
  "RH ⟺ Φ ∈ N_0" es la versión teoría-de-funciones del criterio del programa, con
  literatura técnica madura (modelos de de Branges, espacios Π_κ). Útil como lengua
  franca; no como atajo.

**Calificación del cruce C: POSIBLEMENTE-EQUIVALENTE-A-RH como cierre de R-FIN**
(el eslabón "pertenencia a N_κ con κ a priori" es MW-disfrazado y NC4 falla);
**TÉCNICO y valioso como infraestructura post-R-FIN de la Ruta B**. La pregunta del
encargo queda respondida: no esquiva el Thm 4.3 — cae dentro de su clase.

### 2.4. Cruce D — JACOBIANO→FLUJO ESPECTRAL (breve)

**[DATO]** (Doc 120 §3.4, arXiv:2602.15941): el Picard de Spec ℤ̄ es un MONOIDE
(semi-normas con degeneración permitida), y CC declaran textualmente que el paso
grupo→monoide es "a necessary step for incorporating boundary and singular phenomena…
precisely the features required for the spectral realization". **[DATO]** (Doc 110,
Thm 3.2): RH ⟺ sf = 0 para la filtración de Euler, con cruce en λ₀ finito bajo ¬RH.

**[CONJETURA-INTERFAZ] (121.D).** El flujo espectral de la filtración de Euler se
realiza como una trayectoria en el monoide de Picard, y los cruces de autovalor por
cero corresponden a toques de la trayectoria con el estrato de borde (semi-normas
degeneradas): sf = número de intersección con el divisor de borde. Coherencia interna a
favor: en el cruce A, el punto autodual D₀ cayó exactamente en el borde de salto de
dimensión (§2.1.2.3) — los dos cruces señalan el mismo estrato.

Falsadores: (F-D1) el borde del monoide es demasiado chico — la degeneración de una
semi-norma de rango 1 es un fenómeno de UN parámetro y podría no distinguir
multiplicidades del cruce espectral; (F-D2) la trayectoria de la filtración de Euler
podría no tocar el borde nunca en el mundo RH y la identificación sería vacua de un
lado (falla NC4 por la puerta opuesta); (F-D3) el término divergente 2h(1) log λ
(§9.3 de 2602.15941, pendiente para ellos) está exactamente donde la trayectoria se
definiría — sin su regularización el cruce no se puede ni formular.

**Calificación: CONCEPTUAL, especulativo.** Valor de archivo: es el único lenguaje del
corpus CC donde "degeneración/borde" — el hábitat natural de los índices de inercia en
familias — es estructura declarada y no accidente. A estacionar hasta que (a) CC traten
su término divergente o (b) el cruce A confirme la relevancia del estrato de borde.

---

## 3. EL MAPA DE PRIORIDADES

### 3.1. Ordenación por (valor si cierra) × (probabilidad de cierre sin resolver RH)

| # | gap/cruce | valor si cierra | prob. de cierre sin RH | producto (cualitativo) |
|---|---|---|---|---|
| 1 | **Cruce B** (tolerancia→cuadrado; caso C_p × C_p) | alto: desbloquea G1, da portador a R-LEF-PRIMOS | alta: método existente, equipo activo, riesgo RH nulo | **máximo** |
| 2 | **Cruce A** (forma en el punto autodual D₀) | medio-alto: decide si el ÚNICO mecanismo de dualidad disponible puede producir signaturas (prototipo de R-SIG) | alta para el experimento (cómputo finito); media para el puente completo | **alto** |
| 3 | R-LEF-POLO (identificación H⁰(0), H¹(K) ↔ bloque polar) | medio: cierra el axioma más barato, valida el diccionario | alta (cómputo en categoría existente) | medio-alto |
| 4 | R-LEF-REG (término 2h(1) log λ; arquimediano como órbita de borde) | medio | media (CC ya lo trabajan; T2 al acecho) | medio |
| 5 | **Cruce C** reformateado (dialecto N_κ/Loewner para la Ruta B) | medio condicional (solo paga después de R-FIN) | alta como traducción; nula como cierre | medio-bajo |
| 6 | R-PESO(a)/(b) directos | máximo (es el muro) | baja: sin método; la variante analítica es MW | bajo hoy — sube si 1 y 2 cierran |
| 7 | **Cruce D** (flujo espectral en el monoide) | alto en el límite | baja (especulativo, bloqueado por §9.3 de CC) | bajo |

La lectura estratégica del producto: **la fase debe gastar en 1 y 2**, que son
independientes entre sí, complementarios (portador + mecanismo), y ninguno toca la
NO-GO-LIST. El muro (6) no se ataca de frente: se ataca construyendo el terreno (1) y
el arma (2) y recién entonces midiendo si el ataque es formulable.

### 3.2. Qué puede hacer CC vs qué podemos hacer nosotros (modo especificación)

- **CC (tienen la maquinaria):** el cruce B entero; el término divergente de su §9.3;
  la pregunta del carácter de simetría de su propia dualidad (cruce A, pasos 1–3) es un
  enunciado interno a 2205.01391 que un experto en su formalismo decide probablemente
  en semanas.
- **Nosotros (modo especificación, sin generar matemática de su categoría):** redactar
  los tres experimentos como problemas autocontenidos con falsador (este documento es
  la base); aplicar R-NC a cada output; mantener el catálogo NO-GO actualizado para que
  ningún cierre parcial se sobrevenda. Y la tarea propia: el diccionario N_κ del cruce
  C (es teoría de operadores clásica, terreno del programa, no de CC).

### 3.3. EL EXPERIMENTO MÍNIMO DECISIVO de la fase

Análogo del Problema 5.4 de fases anteriores: finito, dos salidas limpias, decide la
dirección de todo lo demás.

> **Problema 121.E (el carácter de simetría de la dualidad aritmética).** En la
> categoría ΓT∗ de 2205.01391, sea D₀ = −{2} el punto fijo exacto de la involución de
> Serre σ: D ↦ K−D. Determinar el carácter de simetría del apareamiento
> P: H¹(D₀) × H⁰(D₀) → U(1) bajo σ — equivalentemente, el signo ε ∈ {+1, −1} con que
> el isomorfismo de bidualidad actúa (¿la dualidad de Pontryagin con tolerancia de
> Prop. 5.2, compuesta consigo misma vía σ, es simétrica o antisimétrica?).
>
> **Salida (+1):** existe forma SIMÉTRICA inducida en V = H⁰(D₀) ⊕ H¹(D₀); el camino
> dualidad→signatura queda abierto y los siguientes obstáculos son F-A2 (tolerancia) y
> F-A3 (linealización) — la fase continúa por el cruce A.
> **Salida (−1):** la forma es alternante; el mecanismo de dualidad de CC produce a lo
> sumo invariantes mod 2 (Arf/paridad de la característica theta), ciegos a m; R-SIG
> necesita una POLARIZACIÓN además de la dualidad (el análogo de Lefschetz/Hodge ★), y
> la fase debe redirigirse a especificar ese ingrediente — que en todo el corpus CC no
> tiene ni candidato.
>
> Es finito: H⁰(D₀) y H¹(D₀) están computados explícitamente en sus papers (espacios
> chicos: λ = 1/2, caso borde de la Prop. 4.2 de 2306.00456); el apareamiento es
> explícito; el signo es UN bit. No usa ζ ni ceros: pasa NC1 por construcción. Ninguna
> de las dos salidas prueba ni refuta nada sobre RH — decide hacia dónde cavar.

Por qué este y no el caso de prueba C_p × C_p del cruce B: el cruce B es el mejor
producto valor×probabilidad pero no es UN experimento con salida binaria — es un
programa de 5 pasos. El 121.E es estrictamente binario, más barato en orden de
magnitud, y su resultado condiciona la interpretación de TODO lo demás (si la dualidad
es alternante, incluso un cruce B exitoso entrega un portador sin mecanismo de signos,
y la especificación de la polarización pasa a ser el problema número uno del programa).

---

## 4. SÍNTESIS HONESTA

### 4.1. ¿Años o décadas?

Separando por nodo, sin promediar lo imparangonable:

- **G1 (portador): años.** Es "ellos ya casi lo tienen y no lo han cruzado" en sentido
  estricto: el obstáculo nombrado en 2018 (null elements en Čech idempotente) es
  anterior a su propia herramienta de 2022–23 (tolerancia sobre 𝕊), que lo resuelve un
  piso más abajo; nadie — ni ellos — ha escrito la combinación. Calificación TÉCNICO;
  con el equipo CC activo (papers de 2025 y 2026 en el corpus), el orden razonable es
  años, no décadas. Misma categoría: R-LEF-POLO, R-LEF-REG, la mitad dinámica de
  R-LEF-FLUJO.
- **G2 (mecanismo): sin cota superior honesta.** No hay UNA signatura en todo el corpus
  CC (búsqueda negativa verificada, Doc 120 §7.7); no hay forma sobre un solo espacio;
  no hay polarización; y el precedente clásico advierte que la dualidad sola
  (probablemente alternante en grado 1) no basta — hace falta el análogo de la teoría
  de Hodge de la polarización, del que no existe candidato. Esto es "nadie tiene idea"
  — CON una excepción medible: el experimento 121.E puede convertir "nadie tiene idea"
  en "se sabe exactamente qué ingrediente falta", que es un estado epistémico
  estrictamente mejor. Decir "décadas" aquí sería fingir una estimación que no tenemos;
  lo honesto es: G2 no está acotado por trabajo de tipo conocido.

La distancia G1→G2 total es, por tanto, la suma de un tramo corto medible y un tramo no
medible. Quien pregunte "¿cuánto falta?" debe recibir esta respuesta de dos partes, no
un promedio.

### 4.2. La partición "casi lo tienen" / "nadie tiene idea"

**Casi lo tienen (y no lo han cruzado):** H¹ del cuadrado vía tolerancia (cruce B); la
identificación del bloque polar (§1.3); el carácter de simetría de su propia dualidad
(121.E — es un enunciado SOBRE sus definiciones que nadie ha evaluado); la composición
exacta de Ψ(λ) en el lenguaje del monoide (§1.6). Patrón común: cada pieza está a una
combinación de DOS resultados suyos ya publicados.

**Nadie tiene idea:** el criterio interno de peso (R-PESO(a)); la polarización (el
ingrediente que 121.E probablemente revele como faltante); la desigualdad de
Castelnuovo del cuadrado (R-PESO(b) geométrico); el teorema de acompañamiento de R-FIN
("toda dirección negativa viene de V" sin mencionar ceros). Patrón común: todas son la
MISMA incógnita vista de cuatro lados — la estructura que produce signos enteros desde
la geometría. El muro es uno.

### 4.3. El gap que amenaza con tragarse la interfaz

Sí existe, y hay que nombrarlo sin eufemismo. Es **R-PESO(b) en su forma analítica**, y
tiene la propiedad venenosa de OFRECERSE como atajo en cada cruce: el cuantificador
maestro (P43) reaparece en lenguaje geométrico cada vez que una construcción finita
(ventana, truncamiento, conjunto S de lugares, matriz N×N) necesita un enunciado
uniforme para globalizarse. Las tres apariciones detectadas en este documento:

1. **O_SL** (uniformización semilocal→global de positividades): MW-6, catalogado.
2. **Krein–Langer** (cruce C): la estabilización de la inercia truncada exige la clase
   N_κ a priori — que es la positividad de Weil con disfraz de teoría de funciones.
   Detectado y neutralizado en §2.3.3.
3. **La convergencia de los triples espectrales** (Doc 120 §5.4–5.5): CCM declaran
   textualmente que probar su convergencia "would amount to a proof of RH" — el
   patrón O_SL en su forma más pura, declarada por los autores.

La defensa de la interfaz contra el monstruo es estructural y ya está instalada: el
orden R-SIG ≺ R-FIN ≺ R-TRZ (Doc 119) prohíbe usar enunciados uniformes-en-truncamiento
como sustituto de la finitud a priori, y NC3/NC4 los detectan sintácticamente. La regla
operativa de la fase, derivada de este análisis: **toda propuesta de puente que
contenga la frase "y en el límite N→∞ / S→todos los lugares / λ→∞, uniformemente" se
audita contra MW ANTES de invertir trabajo en ella.** Los cruces A y B pasan esta
auditoría (no contienen límites uniformes en su enunciado); el cruce C la falló y quedó
reformateado; el cruce D no es auditable todavía.

### 4.4. Cierre

Ningún enunciado geométrico nuevo se ha probado en este documento. Se ha medido: seis
axiomas contra catorce papers, con el resultado de que el corpus CC contiene el
portador a distancia TÉCNICA (cruce B), el prototipo del mecanismo a distancia de un
bit (experimento 121.E), una herramienta de lectura para después (cruce C,
reformateado), un receptáculo especulativo (cruce D) — y ninguna signatura en ninguna
parte. La fase tiene ahora su Problema 5.4: el carácter de simetría de la dualidad
aritmética en el punto autodual D₀ = −{2}. Una falsa victoria es peor que un fracaso:
si 121.E sale (−1), eso también es un éxito de la fase — sabríamos, por primera vez con
precisión, que lo que falta no es dualidad sino polarización, y la búsqueda cambiaría
de objeto.

---

## Referencias

**Internas (backward-only):** Doc 119 (axiomas R-*, orden de dependencias, tensiones
T1–T4, test R-NC); Doc 120 (inventario CC verificado en fuente, junio 2026 — todas las
citas a arXiv de este documento pasan por su verificación); roadmap-rh (G1–G4, S1–S3,
Thm. rank-sensitivity, Rutas A/B); Doc 110 (Thm 4.3, Prop. 4.5, Prop. 3.4, §5.2);
Doc 108 (binariedad por ventana, §7.4, Prop. 2.5); Doc 105 (Thm 5.5, Obs. 5.6);
Doc 100 (positividad arquimediana, Obstáculo O_SL, Conjetura 100.A); Doc 99 (QW_λ,
Lema 5.1 — vía Docs 100/105); Doc 106 (Prop. 3.10 — vía Doc 120 §7.6); Doc 118
(Lema 5.2, Thm 5.3, Thm 5.6, gap G-118.1); P35 (κ(Q)=2m en Pontryagin); P43
(cuantificador maestro); P44 (dicotomía; anti-Siegel); NO-GO-LIST (MW-1…MW-7).

**Corpus CC/CCM (vía Doc 120, con verificación en fuente declarada allí):**
arXiv:1405.4527, 1502.05580 (sitio aritmético; Ψ(λ); cuadrado con polígonos de Newton);
1507.05818, 1603.03191 (sitio de escala; C_p; RR tropical Thm 5.17); 1509.05576
(*Essay*; las tres estrategias; "yet unclear if this is the right set-up");
1805.10501 (*RR strategy*; el obstáculo de los null elements, textual); 2205.01391
(RR para Spec ℤ̄; Thm 1.1; Thm 1.2 dualidad de Serre con tolerancia; K = −2{2};
U(1)_{1/4}); 2306.00456 (RR sobre 𝕊; χ = ⌈deg₂ D⌉′ + 1; Prop. 4.2: H¹(D) ≅ U(1)_λ);
2602.15941 (Jacobiano de Spec ℤ̄; monoide de Picard; §9.3 término divergente
2h(1) log λ; "boundary and singular phenomena"); 2006.13771 (positividad arquimediana;
Thm 6.11, defecto 13 < c < 17; "intersection theory of divisors (on the square of the
Scaling Site)"); 2310.18423 (prolatos semilocales); 2511.22755 (*Zeta Spectral
Triples*; τ_ij = (b_i − b_j)/(i − j); Prop. 3.3 lower-boundedness); 2602.04022
(la carta de Connes).

**Literatura clásica (verificable):**
- K. Löwner, *Über monotone Matrixfunktionen*, Math. Z. 38 (1934), 177–216.
- M. G. Krein, H. Langer, serie sobre clases N_κ y espacios Π_κ (Math. Nachr. 77
  (1977) y relacionados) [NO VERIFICADO el dato editorial exacto en esta sesión].
- I. S. Iohvidov, *Hankel and Toeplitz Matrices and Forms*, Birkhäuser, 1982 (teoría
  de inercia de formas de Hankel) [NO VERIFICADO el dato editorial exacto].
- D. Mumford, *Theta characteristics of an algebraic curve*, Ann. Sci. ÉNS 4 (1971),
  181–192; M. F. Atiyah, *Riemann surfaces and spin structures*, Ann. Sci. ÉNS 4
  (1971), 47–62 (paridad de características theta; formas cuadráticas mod 2 / Arf).
- A. Mattuck, J. Tate (1958); A. Grothendieck (1958); A. Weil (1948): vía Doc 119.
- V. Guillemin, Duke Math. J. 44 (1977); A. Connes, Selecta Math. 5 (1999): vía
  Doc 119.

*Fin del Doc 121.*
